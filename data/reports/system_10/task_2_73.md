# Deep Research Report: perplexity/sonar-deep-research
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 60f6d039 | **Time:** 111.23s | **Cost:** $1.16592
--------------------------------------------------------------------------------

# The Effect of Technical Intervention Parameters on the Spectral Radius of Learning Transfer Matrices in Cognitive Network Models

## Executive Summary

The spectral radius of learning transfer matrices in cognitive network models represents a fundamental property that governs stability, convergence, and information propagation within interconnected neural systems. This comprehensive report synthesizes recent advances in spectral analysis of neural networks, transfer learning architectures, and cognitive modeling to elucidate how various technical intervention parameters modulate spectral radius properties. We examine how learning rates, weight initialization strategies, architectural choices, regularization techniques, and coupling parameters influence the spectral characteristics of transfer matrices. Through analysis of theoretical frameworks spanning random matrix theory, dynamical systems approaches, and empirical deep learning observations, we demonstrate that technical interventions operate as eigenvalue filters that fundamentally reshape the spectral structure of learning systems. The evidence indicates that maintaining spectral radius near critical thresholds enables optimal information transfer while avoiding both divergence and vanishing gradient phenomena. This framework unifies seemingly disparate phenomena in machine learning and neural computation under a common spectral lens, offering principled guidance for parameter optimization in cognitive network systems.

## Understanding Spectral Radius in the Context of Learning Transfer Matrices

### Fundamental Definitions and Properties

The spectral radius represents the largest absolute value among all eigenvalues of a matrix, formally denoted as \(\rho(W) = \max_i |\lambda_i(W)|\), where \(\lambda_i\) are the eigenvalues of weight matrix \(W\)[38][40]. In the context of learning transfer matrices, the spectral radius serves as a critical indicator of how information propagates through sequential transformations during both forward and backward passes in neural systems. The spectral radius determines whether perturbations in neural activations grow exponentially, remain bounded, or decay during recurrent processing, making it a central quantity for understanding long-range dependencies and gradient flow[45].

For recurrent neural networks and cognitive models with sequential processing, if the spectral radius of the recurrent weight matrix is strictly less than one, perturbations decay exponentially over time, preventing information from persisting across distant time steps. Conversely, when the spectral radius exceeds one, perturbations amplify, potentially leading to unstable dynamics and vanishing or exploding gradients[45][48]. The relationship can be expressed formally for a linear recurrent system as \(x_t = W x_{t-1}\), where if \(\rho(W) < 1\), the operator norm satisfies \(\|W^k\| \leq \rho(W)^k \to 0\) as \(k \to \infty\), meaning information cannot propagate effectively over long sequences[45][48].

In cognitive network models specifically, the spectral radius of transfer matrices influences how information from one cognitive module transfers to another, how learning signals backpropagate through multiple processing stages, and ultimately whether the system can develop robust internal representations. The spectral properties encode information about the stability properties and implicit regularization of the learning system[6][37][40].

### The Role of Transfer Matrices in Cognitive Systems

Transfer matrices in cognitive network models serve as mechanisms for conveying learned representations from source domains to target domains, or more broadly, from trained modules to untrained components. These matrices implement the actual transfer operation and their spectral properties determine transfer efficiency and stability[1][19][43]. In the context of brain-inspired computing and cognitive models, transfer matrices represent the effective connectivity between different processing stages or cognitive components.

The spectral characteristics of these transfer matrices directly influence several critical aspects of cognitive performance: the capacity to maintain information across processing stages without degradation or explosion, the ability to learn features efficiently when training data is limited, and the robustness of learned representations to variations in input or network parameters[19][43]. When the spectral radius is appropriately controlled, cognitive systems can efficiently extract and propagate behaviorally relevant features. When spectral radius grows unchecked, the system develops redundant or amplified representations; when it becomes too small, learned features collapse into trivial forms[43][55].

## Technical Intervention Parameters and Their Spectral Effects

### Learning Rate as a Spectral Regulator

The learning rate stands as one of the most direct and influential technical parameters affecting the spectral radius of learning transfer matrices. From the perspective of gradient descent optimization, the learning rate \(\eta\) determines the magnitude of parameter updates during training, and these updates fundamentally reshape the spectral structure of weight matrices[37][40][42].

In discrete gradient descent, weight updates follow \(W_{t+1} = W_t - \eta \nabla_W L(W_t)\), where the update step can be analyzed through the lens of spectral dynamics. Research using random matrix theory demonstrates that the spectral properties of the batch Hessian—the second-order information about the loss landscape—exhibit perturbations proportional to the learning rate relative to batch size[40]. Specifically, the magnitude of the largest eigenvalue of the Hessian changes as a function of learning rate, with larger learning rates generally producing smaller maximum eigenvalues, thereby influencing the spectral radius of subsequent weight matrix updates[37].

The edge-of-stability phenomenon provides empirical evidence for this effect[42]. When gradient descent converges to a solution, it implicitly filters eigenvalues of the Hessian according to the constraint \(\lambda \leq 2/\eta\), where \(\lambda\) are eigenvalues at the convergence point. This means larger learning rates effectively permit convergence only at points with smaller Hessian eigenvalues, corresponding to flatter minima[42]. For transfer matrices specifically, this implies that learning rate selection determines which spectral properties of the transfer operation become salient during learning.

In the small-batch regime, increasing learning rate while maintaining other parameters produces smaller maximum eigenvalues in the converged solution[37]. However, this relationship becomes more complex in large-batch regimes where stochasticity plays a different role[37][40]. The interaction between learning rate and batch size is not simply additive; rather, it creates a scaling relationship where both parameters jointly determine the spectral properties achieved during training. The linear scaling rule in small-batch SGD—stating that one can increase learning rate proportionally to batch size while maintaining convergence behavior—reflects this joint spectral control[40].

### Batch Size Effects on Spectral Properties

Batch size operates as a second major parameter controlling spectral radius through its effects on gradient noise and Hessian perturbations. The fundamental mechanism operates through random matrix theory: the variance of the batch Hessian differs from the empirical Hessian by an amount inversely proportional to batch size[40]. Formally, the perturbation to Hessian eigenvalues due to mini-batching scales as \(\text{Var}(H) / B\), where \(B\) is batch size.

For learning transfer matrices in cognitive systems, this means smaller batch sizes introduce noisier gradient signals, which affects which eigenvalues of the transfer matrix develop during training[40]. Smaller batch sizes tend to push the system toward solutions with smaller spectral radius due to the implicit regularization effect of gradient noise[40]. This phenomenon connects directly to generalization: systems trained with smaller batches tend to avoid overfitting, partly because their learned representations preserve lower spectral radius for the weight matrices.

The scaling law that emerges from spectral analysis predicts different behaviors for different optimizer types: for standard SGD with small batch sizes, the maximum allowable learning rate scales linearly with batch size (\(\eta \propto B\)), while for adaptive methods like Adam, it scales with the square root of batch size (\(\eta \propto \sqrt{B}\))[40]. These scaling relationships reflect fundamental constraints imposed by the spectral properties of the Hessian at different batch sizes.

### Weight Initialization and Spectral Radius Control

Weight initialization strategies represent another critical intervention parameter, establishing the initial spectral properties from which training dynamics unfold. The initialization scheme determines the initial spectral radius of weight matrices and sets the stage for how spectral properties evolve during learning.

In reservoir computing and recurrent neural networks, the spectral radius of the recurrent weight matrix is commonly initialized to specific target values, often near 0.9, to maintain stability while allowing information to propagate across multiple time steps[48]. This initialization practice reflects the principle that maintaining spectral radius in a particular range prevents both vanishing and exploding gradients in recurrent computations.

For deep feedforward networks, random initialization schemes like Kaiming (He) initialization and Xavier (Glorot) initialization were originally formulated using Frobenius norms[55]. However, recent theoretical work reveals that these Frobenius-norm-based approaches are suboptimal for controlling actual feature learning dynamics[55]. The spectral scaling condition, which emerges from careful analysis of how information propagates through network layers, prescribes that weight matrices should be initialized such that their spectral norm scales as \(\sqrt{n_{\text{out}}/n_{\text{in}}}\), where \(n_{\text{out}}\) and \(n_{\text{in}}\) are output and input dimensions[55].

This spectral initialization strategy differs fundamentally from Frobenius-based approaches because it directly controls the amplification of signals along the direction of maximum gain in each layer, rather than controlling the average across all directions. For transfer matrices specifically, spectral-norm-based initialization ensures that the transfer operation neither amplifies nor suppresses information excessively, maintaining stable feature propagation across domain boundaries.

### Regularization as Spectral Shaping

Regularization techniques fundamentally reshape the spectral radius of learned matrices by adding constraints to the optimization objective. Weight decay—the most commonly used regularization form—explicitly penalizes the Frobenius norm of weights but has profound implicit effects on spectral properties[3][6].

Spectral dynamics studies reveal that weight decay promotes rank minimization across diverse neural network architectures, causing weight matrices to evolve toward lower-rank configurations[3]. This rank minimization is accompanied by changes in spectral properties: as weight matrices become lower rank, eigenvalues beyond the "bulk" distribution begin to concentrate and develop outlier structure[6]. The spectral structure that emerges comprises a bulk of moderate eigenvalues following random matrix theory predictions (such as the Marchenko-Pastur distribution) plus a tail of larger outlier eigenvalues corresponding to learned features.

Weight decay enhances this bias toward low-rank, structured spectra more strongly than suggested by its explicit norm-penalizing role[3]. The mechanism appears to involve differential effects on singular values: large singular values, which correspond to the most important learned features, are less penalized than intermediate singular values, leading to concentration of the spectrum at the extremes—either very small (decaying toward zero) or very large (corresponding to task-relevant features)[3].

For transfer learning specifically, regularization controls the spectral radius by preventing overfitting to source-domain peculiarities[19][43]. Strong regularization maintains moderate spectral radius values, promoting transfer to new domains, while weak regularization permits larger spectral radius values that overfit to source data. The trade-off between source-domain accuracy and target-domain generalization manifests as a trade-off in spectral radius control.

## Coupling Parameters and Network Interaction Effects

### Coupling Strength in Networked Cognitive Systems

In cognitive network models where multiple modules or agents interact, coupling strength—the magnitude of connections between network components—operates as a critical intervention parameter affecting global spectral properties[26][29]. Coupling strength determines how strongly each component influences others and fundamentally reshapes the eigenvalue spectrum of the overall system.

For threshold power-law recurrent networks, coupling strength acts as a scale parameter that affects the magnitude of network solutions but not their qualitative dynamics[26]. More specifically, when transfer functions satisfy certain scale-invariance properties, multiplying coupling strength by a constant factor scales all network solutions proportionally without altering the presence or absence of chaos or the qualitative structure of network behavior[26]. This scale-invariance property means that for these systems, optimal coupling strength can be transferred across different network sizes while maintaining performance.

However, this scale-parameter property does not hold universally for all activation functions. For sigmoidal activation functions, coupling strength explicitly influences network dynamics beyond mere scaling[26]. The distinction between scale-invariant systems (like threshold power-law networks) and those where coupling strength qualitatively affects dynamics reflects deeper spectral properties: in scale-invariant systems, the spectral radius of the coupling matrix determines stability, but once stability is achieved, further variations in coupling magnitude do not alter whether the network can be trained for specific tasks[26].

### Graph Laplacian Spectral Properties in Cognitive Networks

In networked cognitive systems modeled as graphs, the spectral properties of the graph Laplacian determine consensus convergence rates, synchronization dynamics, and information spreading[14][15]. The Laplacian matrix \(L = D - A\), where \(D\) is the degree matrix and \(A\) is the adjacency matrix, has eigenvalues that directly encode network structure.

The second-smallest eigenvalue (algebraic connectivity) \(\lambda_2\) controls consensus convergence rate in multi-agent systems[14]. Specifically, the convergence speed is proportional to \(\lambda_2\)—larger algebraic connectivity produces faster consensus[14]. This relationship provides a direct mechanism for intervention: modifying network edges (connections between cognitive modules) changes the Laplacian spectrum and thus convergence behavior.

Research on the Hermitian Kirchhoff index for hybrid networks demonstrates that strategic edge additions or removals can improve consensus convergence rates[14]. Adding edges between distant nodes, or removing edges from clusters, increases algebraic connectivity and thus accelerates information propagation across the network[14]. The theory of eigenvalue perturbation provides quantitative predictions about which edge modifications produce the largest beneficial changes to spectral properties[14].

For cognitive networks, this implies that the interconnectivity structure between processing modules—controlled through learning-based weight adjustments—acts as an intervention parameter affecting spectral convergence properties. Networks with stronger connections between diverse cognitive modules (increased algebraic connectivity) achieve faster consensus about task-relevant information.

## Stability Analysis and Spectral Radius Bounds

### Theoretical Stability Bounds

The stability of learning dynamics in cognitive network models depends critically on maintaining spectral radius within specific bounds. For linear systems \(\dot{x} = Ax\), asymptotic stability requires all eigenvalues of \(A\) to have negative real parts. For discrete-time systems \(x_{k+1} = Ax_k\), stability requires spectral radius \(\rho(A) < 1\)[9].

These classical results extend to nonlinear neural networks through linearization around fixed points and through Lyapunov function analysis[8][24]. The Lyapunov approach provides a framework for guaranteeing stability by constructing functions \(V(x)\) satisfying \(\dot{V}(x) < 0\) for \(x \neq 0\), which implies convergence to the origin. For neural network weight dynamics, this translates to constraints on the eigenvalues of the Jacobian of the weight update dynamics[24].

Practical stability analysis for deep neural network training uses the concept of edge-of-stability[37][42]. Networks training in the edge-of-stability regime exhibit oscillations in training loss during the early phase, followed by convergence. The spectral radius of the Hessian at the edge-of-stability point saturates the bound \(\lambda_{\max} \approx 2/\eta\), meaning the maximum Hessian eigenvalue is as large as allowed before divergence[37][42].

For transfer matrices in cognitive systems, maintaining spectral radius below unity prevents explosive amplification of information transfers, while ensuring spectral radius remains sufficiently large prevents vanishing of transferred information. The optimal range typically lies in \(0.8 < \rho < 1.0\) for systems requiring stable information propagation across multiple modules[48].

### Dynamical Systems Perspective on Spectral Control

A dynamical systems framework views the evolution of neural network weights during training as a high-dimensional flow in parameter space. This flow is shaped by gradient descent dynamics and implicitly constrained by the stability requirements of the loss landscape[8][24].

The attraction basins in both input space (determining generalization) and weight space (determining structural stability) are coupled through the network architecture[8]. Technical intervention parameters like learning rate and batch size regulate the size and shape of these attraction basins. Maintaining synchronized expansion of both basins—achieved through appropriate spectral scaling—produces optimal network performance[8].

Deep networks can be viewed as undergoing a transition in learning modes: initially, orientation-preserving-mode neurons dominate, causing weight vectors to align toward specific directions and increasing the rank projection density gradient[8]. Subsequently, nonlinear-processing-mode neurons activate, spreading weight vectors across broader directions[8]. The spectral properties change as this transition occurs: rank projection density increases initially as weights concentrate, then decreases as they diversify, creating a complex spectral evolution pattern.

## Empirical Evidence from Deep Learning Research

### Spectral Dynamics During Training

Extensive empirical studies of neural network training reveal consistent patterns in spectral evolution[3][6][23][40][50]. The singular value spectrum of weight matrices evolves from initial random matrix theory predictions (Marchenko-Pastur distribution for random rectangular matrices) toward structured "bulk+tail" distributions where moderate singular values form a coherent bulk while larger singular values form an outlier tail[3][6][23].

This spectral transition correlates precisely with the onset of feature learning[6]. The deviation from random matrix statistics signals when networks begin learning meaningful structure rather than memorizing[3]. By monitoring the transition from Marchenko-Pastur statistics to bulk+tail structure, researchers can identify critical training phases when interpretable features emerge—the deviation from random matrix statistics signals the onset of structured learning[6].

The spectral evolution exhibits interesting asymmetries: lower singular values remain distributed according to random matrix theory, while upper singular values concentrate into a distinct tail[6][23]. This pattern reflects how learning operates: most of the network's parameter space follows random-like dynamics (contributing noise), while a small number of singular modes concentrate to implement task-solving transformations.

Weight decay exerts explicit control over this spectral evolution, enhancing the concentration of outlier singular values and accelerating the transition from random-like to structured spectra[3]. Without weight decay, low-rank solutions develop more slowly or not at all, especially in the grokking phenomenon where sudden generalization occurs after extended training[3].

### Spectral Filtering by Optimization Algorithms

Different optimization algorithms implement different eigenvalue filtering effects, determining which spectral properties of the loss landscape the algorithm converges toward[42]. Standard gradient descent filters toward solutions where Hessian eigenvalues satisfy \(\lambda \leq 2/\eta\), with no constraint on the minimum eigenvalue[42].

Sharpness-Aware Minimization (SAM) actively seeks flatter minima by explicitly penalizing large Hessian eigenvalues, producing solutions where eigenvalues remain smaller than standard gradient descent[42]. The SAM update incorporates a term \([\sigma_1(C_k) - 1]_+\) penalizing the largest eigenvalue of the update matrix, where \(\sigma_1\) denotes the largest singular value[42].

These algorithmic differences manifest empirically: networks trained with SAM generalize better than standard gradient descent on many benchmarks, particularly in high-learning-rate regimes[42]. The improved generalization emerges from the spectral filtering properties: SAM's preference for flatter minima (smaller Hessian eigenvalues) correlates with better generalization, consistent with theoretical predictions[37][42].

For transfer learning scenarios, these optimization effects become crucial: SAM-trained networks on source domains tend to develop transfer matrices with more stable spectral properties, improving target-domain generalization[42].

### Batch Normalization and Spectral Stability

Batch normalization (BN) operates by normalizing layer activations to have approximately unit mean and variance, but its spectral effects extend beyond simple activation normalization[49]. By controlling activation statistics through learnable scaling and shifting parameters, batch normalization improves the conditioning of the loss landscape, making eigenvalues of the Hessian more evenly distributed[49].

Networks with batch normalization exhibit smoother loss landscapes (improved β-smoothness or Lipschitzness)[49]. This smoothness directly relates to spectral properties: the Hessian of a smooth function has bounded eigenvalues and well-conditioned eigenvectors, facilitating optimization[49].

For recurrent systems and transfer matrices, batch normalization has complex spectral consequences. When applied to recurrent layers, batch normalization can suppress the range of Hessian eigenvalues, leading to better-conditioned optimization[49]. However, the coupling between normalization across batch elements creates statistical dependencies that can affect spectral properties in subtle ways depending on whether normalization is applied frame-wise or sequence-wise[49].

## Applications to Cognitive Network Models

### Transfer Learning and Spectral Properties

In transfer learning scenarios where representations from source domains transfer to target domains, the spectral properties of transfer matrices directly influence transfer success[1][19][43]. The spectral transfer learning method (STIG) for brain-computer interfaces demonstrates how information-geometric approaches can be combined with spectral methods to achieve zero-calibration transfer[1].

STIG uses classifiers operating on covariance matrices mapped to Riemannian manifolds, then combines predictions via spectral meta-learning[1]. The spectral weighting scheme assigns importance to different source-domain classifiers based on their spectral properties, effectively filtering out source-domain peculiarities while retaining domain-general features[1].

The method significantly outperforms unweighted ensemble approaches, suggesting that explicit control over spectral properties improves transfer efficiency[1]. The underlying mechanism appears to involve weighting source-domain classifiers inversely proportional to their departure from typical Riemannian geometry, thus preserving spectral properties conducive to target-domain generalization[1].

### Virtual Brain Modeling and Network Parameters

Virtual brain modeling using The Virtual Brain framework demonstrates how personalized network parameters—including excitatory/inhibitory balance characterized by spectral properties—enable disease-specific differentiation[2]. Different dementia types (Alzheimer's disease vs. frontotemporal dementia) exhibit distinct patterns in the global coupling parameter and synaptic parameters (\(J_{\text{NMDA}}\), \(J_i\), \(w_+\))[2].

The global coupling parameter acts as a spectral control parameter, scaling the strength of long-range connections[2]. This parameter directly influences the spectral properties of the brain network's effective connectivity matrix. Fitting these parameters to empirical data reveals that disease-specific alterations in network spectral properties correlate with cognitive performance profiles[2].

The excitatory/inhibitory balance parameter essentially controls where on the spectrum the network operates relative to criticality. Networks with altered excitatory/inhibitory balance exhibit different spectral distributions of neural activity, explaining differential cognitive symptomatology[2]. The spectral properties recovered from virtual brain modeling provide personalized fingerprints enabling differential diagnosis and treatment optimization[2].

### Spectral Graph Analysis in Neural Circuits

Graph spectral methods applied to neural connectomes reveal how network structure (eigenvalues of graph Laplacian) relates to functional organization and information flow[27][28]. The C. elegans connectome analyzed through guided spectral embedding reveals how spectral properties distinguish functional neuron types even when spatial distance measures fail[27].

The Laplacian eigenvectors map nodes to positions minimizing distances between connected nodes, creating embeddings where network structure becomes transparent[27]. Applying this to neural circuits reveals that spectral properties encode functional roles: sensory neurons, interneurons, and motor neurons occupy distinct regions of the spectral embedding space, despite anatomical intermingling[27].

The eigenvalue spectrum itself characterizes network connectivity: eigenvalues far from zero correspond to well-connected network components with high information flow, while eigenvalues near zero correspond to weakly connected components[27]. This spectral characterization provides an objective measure of component connectivity independent of spatial embedding, useful for comparing networks from different organisms or developmental stages.

## Advanced Parameter Interactions and Emergent Effects

### Depth, Width, and Spectral Scaling

The interaction between network depth and width determines optimal spectral scaling rules. Deep networks require careful spectral normalization to maintain stable feature propagation across many layers, with requirements depending on activation function properties[8][55].

For networks with ReLU activations, width-dependent spectral scaling naturally prevents the vanishing gradient problem: wider networks can incorporate more nonlinear-processing-mode neurons that extract information from broader directions in input space[8]. The required depth-width relationship for optimal spectral properties suggests that very deep networks need proportionally wider hidden layers—a relationship previously understood empirically but now grounded in spectral theory[8].

The spectral scaling condition \(|\!|W_\ell|\!|_* = \Theta(\sqrt{n_\ell/n_{\ell-1}})\) for weight spectral norms and \(|\!|\Delta W_\ell|\!|_* = \Theta(\sqrt{n_\ell/n_{\ell-1}})\) for update spectral norms provides a unifying principle[55]. This principle, derived from feature learning requirements, predicts that as network width increases, weight initialization magnitude must decrease while learning rates must be adjusted to maintain constant effective updates[55].

Empirically, networks satisfying the spectral scaling condition across all layers maintain consistent feature learning even as width increases to very large values, preventing both the kernel regime (where features freeze) and training instability[55].

### Dropout and Spectral Properties

Dropout regularization introduces randomness during training by deactivating neurons with specified probability, creating an ensemble effect[55]. The spectral impact of dropout operates through two mechanisms: reducing feature co-adaptation and modifying effective network spectral properties during training.

High dropout probabilities can degrade generalization despite reducing Hessian eigenvalues, suggesting that the relationship between spectral radius and generalization is not monotonic[37]. Excessive dropout may cause features to develop excessively sparse spectral structure, limiting the richness of learned representations[37].

The interaction between dropout probability and optimal learning rate follows from spectral considerations: as dropout probability increases, the effective number of active neurons decreases, requiring adjusted learning rates to maintain consistent spectral evolution[24].

### Phase Diagrams of Neural Network Training

Recent work mapping phase diagrams of neural network training in terms of hyperparameter combinations reveals three distinct phases dependent on spectral properties[50]: (1) an ordered/ferromagnetic phase where networks learn well, (2) a disordered/jamming phase where networks fail to learn, and (3) a paramagnetic phase dominated by fluctuations preventing learning.

The boundaries between these phases correspond to critical spectral transitions. The ordered phase occurs when hyperparameters permit features to develop—spectral radius remains in the optimal range facilitating learning[50]. The jamming phase occurs when initial weight variance becomes too large, causing pre-activations to saturate in nonlinear regimes, halting gradient flow and preventing spectral structures from developing[50].

Initial weight variance acts as a spectral control parameter directly determining which phase the network enters. For bounded activation functions, large initial weight variance keeps pre-activations in saturation regions where activation functions are nearly flat, causing vanishing gradients and preventing spectral structure development[50]. Smaller initial variance keeps pre-activations in linear regions where gradients flow effectively and spectral structures can develop[50].

## Practical Guidelines for Parameter Optimization

### Integrating Spectral Constraints into Design Practices

Modern deep learning practice increasingly incorporates spectral considerations, though often without explicitly framing them as such. Spectral normalization of weight matrices, recently popularized for training generative adversarial networks and other applications, directly enforces the spectral scaling condition by normalizing weights such that their spectral norm equals one[55].

For cognitive network models specifically, practitioners should:

First, select initialization schemes based on spectral norm rather than Frobenius norm. Kaiming initialization modified to use spectral norm control [55] provides more stable feature learning than traditional Frobenius-based initialization. The modified initialization satisfies \(|\!|W|\!|_* \sim \sqrt{n_{\text{out}}/n_{\text{in}}}\) where \(n_{\text{out}}\) and \(n_{\text{in}}\) are output and input dimensions.

Second, coordinate learning rate selection with batch size through scaling laws derived from spectral analysis. For standard SGD in small-batch regimes, the linear scaling rule—maintaining \(\eta B = \text{constant}\)—preserves spectral convergence properties as batch size changes[40]. For adaptive methods like Adam, square-root scaling \(\eta \propto \sqrt{B}\) better preserves spectral properties[40].

Third, employ weight decay or other spectral-regularization techniques when transfer to new domains is desired. Stronger regularization maintains moderate spectral radius values, improving transfer while preventing overfitting to source-domain statistics[19][43]. The interaction between regularization strength and spectral radius suggests that weakly regularized networks develop larger spectral radius values more quickly, enabling higher source-domain accuracy at the expense of transfer[19].

Fourth, monitor spectral properties during training as diagnostic indicators. The transition from Marchenko-Pastur statistics to bulk+tail spectrum signals feature learning onset. Spectral radius evolution can indicate whether learning is proceeding normally or entering problematic regimes[3][6][23].

### Hyperparameter Coordination

The spectral perspective reveals deep coordinations among hyperparameters that appear independent from conventional viewpoints. Learning rate, batch size, weight initialization magnitude, depth, width, and regularization strength jointly determine spectral properties; optimizing these parameters independently leads to suboptimal results[8][24][40][55].

The spectral scaling condition provides a unifying principle for these coordinations. Once this condition is satisfied—meaning \(|\!|W_\ell|\!|_* = \Theta(\sqrt{n_\ell/n_{\ell-1}})\) for all layers and \(|\!|\Delta W_\ell|\!|_* = \Theta(\sqrt{n_\ell/n_{\ell-1}})\) for all updates—feature learning proceeds reliably across a wide range of width scaling[55].

This principle enables a two-stage optimization strategy: First, establish initialization and learning rate according to spectral scaling requirements, ensuring fundamental spectral properties are correct. Second, then optimize other hyperparameters (regularization strength, architecture specifics) knowing that spectral stability is maintained.

### Monitoring and Diagnostics

Several spectral diagnostics can be computed during training to verify that systems are performing optimally:

Compute the empirical spectral distribution of weight matrices at regular intervals, tracking the transition from random-matrix-like (Marchenko-Pastur) to structured spectrum[3][6]. The onset of prominent outlier eigenvalues indicates when meaningful feature learning begins[6].

Monitor Hessian spectral properties at regular intervals, particularly the maximum eigenvalue \(\lambda_{\max}\)[37][42]. For systems achieving edge-of-stability training, \(\lambda_{\max}\) should approach the theoretical bound \(2/\eta\) as training progresses[42].

Compute singular value decomposition of weight update matrices to assess whether updates follow low-rank structure[55]. Low-rank updates indicate efficient learning where important features align with dominant singular directions[55].

These diagnostics require modest computational overhead (dominated by SVD and eigenvalue decomposition) but provide rich information about whether learning is proceeding according to spectral theory predictions.

## Conclusion and Future Perspectives

The spectral radius of learning transfer matrices in cognitive network models operates as a fundamental quantity governing stability, convergence, and information propagation. Technical intervention parameters including learning rate, batch size, weight initialization, regularization strength, and network coupling all exert control over spectral radius through multiple mechanisms. Learning rate and batch size jointly determine the spectral radius of the Hessian and thus which solutions gradient descent converges toward. Weight initialization establishes initial spectral properties from which training dynamics unfold. Regularization reshapes spectral structure by promoting low-rank, feature-concentrated configurations. Network coupling parameters determine inter-module information flow through their spectral properties.

The spectral perspective unifies phenomena previously studied in isolation: the benefits of batch normalization emerge from loss landscape smoothing that improves eigenvalue conditioning; the advantages of sharpness-aware minimization follow from explicit eigenvalue filtering; the success of spectral transfer learning methods derives from exploiting spectral stability across domain boundaries; the phase transitions in learning capability correspond to spectral transitions enabling or preventing feature development.

Empirical evidence from deep learning research consistently demonstrates that maintaining appropriate spectral properties—neither too small (causing feature collapse) nor too large (causing divergence or vanishing gradients)—produces optimal learning performance. The edge-of-stability phenomenon captures this principle: networks implicitly seek to maintain Hessian eigenvalues at the boundary of stability, saturating the constraint \(\lambda_{\max} \approx 2/\eta\).

For cognitive network models specifically, this framework suggests that designing optimal systems requires explicit attention to spectral properties of transfer matrices rather than treating them as incidental consequences of gradient descent. Practitioners developing cognitive systems should employ spectral-norm-based initialization, coordinate hyperparameters through scaling rules derived from spectral analysis, and monitor spectral diagnostics during training.

Future research should extend these frameworks to more complex architectures including attention mechanisms, graph neural networks, and hybrid cognitive systems combining multiple processing types. The interaction between spectral properties and the inductive biases of specialized architectures remains incompletely understood. Additionally, extending spectral analysis to non-Euclidean domains relevant for cognitive networks—such as Riemannian manifolds for geometric deep learning—represents an important frontier for understanding how cognitive representations develop and transfer across domains.

[1][3][6][8][14][15][19][24][26][37][40][42][43][45][48][49][50][55]

## Annotations
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Spectral Transfer Learning Using Information Geometry for a User ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5032911/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Virtual brain simulations reveal network-specific parameters in ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10419271/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Approaching Deep Learning through the Spectral Dynamics ... - arXiv', 'url': 'https://arxiv.org/html/2408.11804v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Evaluation of Spectral Traffic Classifiers in Cognitive Radio ...', 'url': 'https://www.jocm.us/2025/JCM-V20N4-436.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The interpretation of computational model parameters depends on ...', 'url': 'https://elifesciences.org/articles/75474'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Spectral Dynamics in Neural Network Training - OpenReview', 'url': 'https://openreview.net/pdf?id=uOdUwvPqLa'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Transferring structural knowledge across cognitive maps in humans ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC7508979/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Network Dynamics-Based Framework for Explaining Deep Neural ...', 'url': 'https://arxiv.org/html/2501.02436v2'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] 1 Stability of a linear system - Princeton University', 'url': 'https://www.princeton.edu/~aaa/Public/Teaching/ORF523/S16/ORF523_S16_Lec10_gh.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Cognitive diagnosis method via neural networks with transfer ...', 'url': 'https://journal.psych.ac.cn/acps/EN/10.3724/SP.J.1041.2026.0755'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Leveraging dynamics informed neural networks for predictive ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11735935/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Lax-stability vs. eigenvalue stability of spectral methods - People', 'url': 'https://people.maths.ox.ac.uk/trefethen/publication/PDF/laxstab.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Transfer matrices, non-Hermitian Hamiltonians and Resolvents - arXiv', 'url': 'https://arxiv.org/abs/math-ph/9810008'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Research on the Consensus Convergence Rate of Multi-Agent ... - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC12564661/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Stability and dynamics of a spectral graph model of brain oscillations', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10270709/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Spectral Learning on Matrices and Tensors - Anima AI + Science Lab', 'url': 'https://tensorlab.cms.caltech.edu/users/anima/pubs/tensorbook.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Optimal Intervention on Weighted Networks via Edge Centrality', 'url': 'https://www.hongyangzhang.com/centrality_mobility.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Dynamics of cognition - Riley - 2012 - Wiley Interdisciplinary Reviews', 'url': 'https://wires.onlinelibrary.wiley.com/doi/10.1002/wcs.1200'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Transfer Learning in Large-Scale Gaussian Graphical Models with ...', 'url': 'http://stat.wharton.upenn.edu/~tcai/paper/Transfer-Learning-GGM.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Closed form of the Hessian spectrum for some Neural Networks', 'url': 'https://openreview.net/pdf?id=gW30Rx4eZP'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Deep Neural Network Design for Improving Stability and Transient ...', 'url': 'https://www.osti.gov/servlets/purl/2431995'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A convergence algorithm for graph co-regularized transfer learning', 'url': 'http://scis.scichina.com/en/2023/132104.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Analysis of one-hidden-layer Neural Networks via the Resolvent ...', 'url': 'https://arxiv.org/pdf/2105.05115.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Training Dynamics Aware Neural Network Optimization with ...', 'url': 'https://openaccess.thecvf.com/content/ACCV2022/papers/Fang_Training_Dynamics_Aware_Neural_Network_Optimization_with_Stabilization_ACCV_2022_paper.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Learning Dynamics of the Complex-Valued Neural Network in the ...', 'url': 'https://www.scirp.org/journal/paperinformation?paperid=41684'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The Coupling Strength Is a Scale Parameter in Threshold Power ...', 'url': 'https://arxiv.org/html/2512.01006v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Guided graph spectral embedding: Application to the C. elegans ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6663470/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Characterizing Learning Dynamics of Deep Neural Networks via ...', 'url': 'https://arxiv.org/abs/2110.02628'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Coupling functions: Universal insights into dynamical interaction ...', 'url': 'https://link.aps.org/doi/10.1103/RevModPhys.89.045001'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Spectral multidimensional scaling - PNAS', 'url': 'https://www.pnas.org/doi/10.1073/pnas.1308708110'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Cross Layer Routing in Cognitive Radio Network Using Deep ...', 'url': 'https://repository.rit.edu/cgi/viewcontent.cgi?article=11020&context=theses'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Eigenvalue sensitivity analysis based on the transfer matrix method', 'url': 'https://onlinelibrary.wiley.com/doi/full/10.1002/msd2.12016'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Graph Neural Network-based Spectral Filtering Mechanism ... - arXiv', 'url': 'https://arxiv.org/html/2502.11505'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Cross-Layer Analysis of Machine Learning Models for Secure and ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC12197281/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] knowledge distillation through geometry - arXiv', 'url': 'https://arxiv.org/pdf/2509.25253.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Graph Neural Networks with Diverse Spectral Filtering', 'url': 'https://dl.acm.org/doi/10.1145/3543507.3583324'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] On the Maximum Hessian Eigenvalue and Generalization - arXiv', 'url': 'https://arxiv.org/pdf/2206.10654.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'On the spectral radius of weight matrices in RNNs', 'url': 'http://danielrapp.github.io/rnn-spectral-radius/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'CONVERGENCE OF OPTIMIZERS IMPLIES EIGENVALUES ...', 'url': 'https://openreview.net/forum?id=k3Lnh6jp0w'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A Random Matrix Theory Approach to Neural Network Training', 'url': 'https://www.jmlr.org/papers/volume23/20-1258/20-1258.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Weights initialization (reservoirpy.mat_gen) - Read the Docs', 'url': 'https://reservoirpy.readthedocs.io/en/latest/api/reservoirpy.mat_gen.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] arXiv:2510.09034v1 [cs.LG] 10 Oct 2025', 'url': 'https://arxiv.org/pdf/2510.09034.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Spectral Domain-Transfer Learning', 'url': 'https://www.cse.ust.hk/~qyang/Docs/2008/p488-ling.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Dynamic spectral filtering convolutional neural network and high ...', 'url': 'https://pubmed.ncbi.nlm.nih.gov/40086134/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Vanishing gradient problem - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Vanishing_gradient_problem'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] An introduction to domain adaptation and transfer learning - arXiv', 'url': 'https://arxiv.org/pdf/1812.11806.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Spectral Attention Mechanism - Emergent Mind', 'url': 'https://www.emergentmind.com/topics/spectral-attention-mechanism'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Exploding, Vanishing Gradients & Reservoir Computing', 'url': 'https://harvard-iacs.github.io/2019-CS109B/a-sections/a-section4/notes/a-sec4-RNNs_notes_209b2019.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Normalization Methods in Deep Learning - Ahmad Badary', 'url': 'https://ahmedbadary.github.io/work_files/research/dl/concepts/norm_methods'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Phase diagram and eigenvalue dynamics of stochastic gradient ...', 'url': 'https://arxiv.org/html/2509.01349v2'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The impact of sparsity in low-rank recurrent neural networks - PMC', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9390915/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Normalization (machine learning) - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Normalization_(machine_learning)'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] EFFECT OF ACTIVATION FUNCTIONS ON THE TRAIN - OpenReview', 'url': 'https://openreview.net/pdf?id=rkgfdeBYvH'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Neural Network Pruning as Spectrum Preserving Process - arXiv', 'url': 'https://arxiv.org/pdf/2307.08982.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A Spectral Condition for Feature Learning - arXiv', 'url': 'https://arxiv.org/pdf/2310.17813.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Representation Learning and the Information Bottleneck Approach', 'url': 'https://www.inference.vc/representation-learning-and-compression-with-the-information-bottleneck/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Information Geometry and Manifold Learning: A Novel Framework ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11763731/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A Spectral Condition for Feature Learning - Mathy AI Substack', 'url': 'https://aiwithmike.substack.com/p/a-spectral-condition-for-feature'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Information bottleneck theory of high-dimensional regression', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10275337/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Manifold Alignment - Autonomous Learning Laboratory', 'url': 'https://all.cs.umass.edu/pubs/2011/wang_k_m_11.pdf'}}

## Sources
https://pmc.ncbi.nlm.nih.gov/articles/PMC5032911/
https://pmc.ncbi.nlm.nih.gov/articles/PMC10419271/
https://arxiv.org/html/2408.11804v1
https://www.jocm.us/2025/JCM-V20N4-436.pdf
https://elifesciences.org/articles/75474
https://openreview.net/pdf?id=uOdUwvPqLa
https://pmc.ncbi.nlm.nih.gov/articles/PMC7508979/
https://arxiv.org/html/2501.02436v2
https://www.princeton.edu/~aaa/Public/Teaching/ORF523/S16/ORF523_S16_Lec10_gh.pdf
https://journal.psych.ac.cn/acps/EN/10.3724/SP.J.1041.2026.0755
https://pmc.ncbi.nlm.nih.gov/articles/PMC11735935/
https://people.maths.ox.ac.uk/trefethen/publication/PDF/laxstab.pdf
https://arxiv.org/abs/math-ph/9810008
https://pmc.ncbi.nlm.nih.gov/articles/PMC12564661/
https://pmc.ncbi.nlm.nih.gov/articles/PMC10270709/
https://tensorlab.cms.caltech.edu/users/anima/pubs/tensorbook.pdf
https://www.hongyangzhang.com/centrality_mobility.pdf
https://wires.onlinelibrary.wiley.com/doi/10.1002/wcs.1200
http://stat.wharton.upenn.edu/~tcai/paper/Transfer-Learning-GGM.pdf
https://openreview.net/pdf?id=gW30Rx4eZP
https://www.osti.gov/servlets/purl/2431995
http://scis.scichina.com/en/2023/132104.pdf
https://arxiv.org/pdf/2105.05115.pdf
https://openaccess.thecvf.com/content/ACCV2022/papers/Fang_Training_Dynamics_Aware_Neural_Network_Optimization_with_Stabilization_ACCV_2022_paper.pdf
https://www.scirp.org/journal/paperinformation?paperid=41684
https://arxiv.org/html/2512.01006v1
https://pmc.ncbi.nlm.nih.gov/articles/PMC6663470/
https://arxiv.org/abs/2110.02628
https://link.aps.org/doi/10.1103/RevModPhys.89.045001
https://www.pnas.org/doi/10.1073/pnas.1308708110
https://repository.rit.edu/cgi/viewcontent.cgi?article=11020&context=theses
https://onlinelibrary.wiley.com/doi/full/10.1002/msd2.12016
https://arxiv.org/html/2502.11505
https://pmc.ncbi.nlm.nih.gov/articles/PMC12197281/
https://arxiv.org/pdf/2509.25253.pdf
https://dl.acm.org/doi/10.1145/3543507.3583324
https://arxiv.org/pdf/2206.10654.pdf
http://danielrapp.github.io/rnn-spectral-radius/
https://openreview.net/forum?id=k3Lnh6jp0w
https://www.jmlr.org/papers/volume23/20-1258/20-1258.pdf
https://reservoirpy.readthedocs.io/en/latest/api/reservoirpy.mat_gen.html
https://arxiv.org/pdf/2510.09034.pdf
https://www.cse.ust.hk/~qyang/Docs/2008/p488-ling.pdf
https://pubmed.ncbi.nlm.nih.gov/40086134/
https://en.wikipedia.org/wiki/Vanishing_gradient_problem
https://arxiv.org/pdf/1812.11806.pdf
https://www.emergentmind.com/topics/spectral-attention-mechanism
https://harvard-iacs.github.io/2019-CS109B/a-sections/a-section4/notes/a-sec4-RNNs_notes_209b2019.pdf
https://ahmedbadary.github.io/work_files/research/dl/concepts/norm_methods
https://arxiv.org/html/2509.01349v2
https://pmc.ncbi.nlm.nih.gov/articles/PMC9390915/
https://en.wikipedia.org/wiki/Normalization_(machine_learning)
https://openreview.net/pdf?id=rkgfdeBYvH
https://arxiv.org/pdf/2307.08982.pdf
https://arxiv.org/pdf/2310.17813.pdf
https://www.inference.vc/representation-learning-and-compression-with-the-information-bottleneck/
https://pmc.ncbi.nlm.nih.gov/articles/PMC11763731/
https://aiwithmike.substack.com/p/a-spectral-condition-for-feature
https://pmc.ncbi.nlm.nih.gov/articles/PMC10275337/
https://all.cs.umass.edu/pubs/2011/wang_k_m_11.pdf