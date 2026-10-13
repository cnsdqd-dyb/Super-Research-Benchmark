# Deep Research Report: perplexity/sonar-deep-research
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 6b997264 | **Time:** 135.12s | **Cost:** $1.15567
--------------------------------------------------------------------------------

# The Jordan Form Structure of Social Stratification Matrices and Its Constraints on Ergodic Mobility Boundaries in Counter-Globalization Fields

This comprehensive analysis examines the mathematical relationships between Jordan normal form decompositions of social stratification matrices and the ergodic properties of mobility functions operating within counter-globalization flow systems. The central finding is that the Jordan block structure of social stratification matrices fundamentally constrains the ergodic boundary conditions of intergenerational mobility functions, with significant implications for understanding whether counter-globalization movements can achieve their goal of reducing global inequality through redistributive mechanisms.

## Introduction: Synthesizing Linear Algebra and Social Dynamics

The intersection of linear algebra and social dynamics has emerged as a powerful framework for understanding complex social processes. When social stratification is represented as a transition matrix—a mathematical object that describes the probability of individuals moving between social classes across generations—the structural properties of that matrix determine fundamental characteristics of the social system's long-term behavior.[14][16][17] The **Jordan normal form** of such a matrix provides a canonical decomposition that reveals whether a social system can achieve ergodic mixing (where all individuals eventually have equal probability of occupying any social position) or whether structural barriers prevent such mixing.[1][4] This report explores how the Jordan block structure of social stratification matrices creates mathematical constraints on the ergodicity boundaries of mobility functions, and what implications these constraints hold for counter-globalization movements seeking to transform global economic systems.[3][6]

Counter-globalization movements represent organized social resistance to neoliberal economic models that have produced widening wealth gaps and reduced social mobility in many nations.[3][6] These movements operate as complex flow systems in which information, people, and organizational energy move through networks attempting to disrupt existing hierarchical structures and create more equitable distributions of resources. Understanding whether such movements can fundamentally alter the ergodic properties of global social systems—transforming them from systems with permanently fixed hierarchies into fully mixing systems—requires deep engagement with the mathematical structures underlying social stratification. The Jordan form provides precisely this analytical tool, revealing the defects and rigidities in social structures that constrain mobility. This analysis demonstrates that counter-globalization movements face fundamental mathematical obstacles embedded in the Jordan block structure of existing social stratification matrices, constraints that become more evident when one examines the complete trajectory of generational mobility.

## Mathematical Foundations: Jordan Normal Form and Its Structural Implications

The Jordan normal form is a mathematical decomposition that transforms any square matrix into a nearly diagonal form consisting of Jordan blocks.[1][4][31][34] Understanding this concept is essential to analyzing social stratification matrices because the Jordan form reveals the fundamental structure underlying complex systems. While a general matrix may appear opaque in its raw form, the Jordan normal form exposes its eigenvalue structure, multiplicities, and the geometric relationships between eigenvectors and generalized eigenvectors that determine system dynamics.[1][4]

**The Essential Components of Jordan Decomposition**

When a square matrix \(A\) representing a social system is transformed through similarity transformation using an invertible matrix \(P\), it can be written as \(P^{-1}AP = J\), where \(J\) is the Jordan normal form.[1][4][31][34] The Jordan form \(J\) is block diagonal, with each block taking the specific form of a Jordan block corresponding to a particular eigenvalue. Each Jordan block for eigenvalue \(\lambda\) takes the form where \(\lambda\) appears on the main diagonal and ones appear on the superdiagonal.[1][4][34] The critical insight for social analysis is that the **size of Jordan blocks** directly reflects the geometric versus algebraic multiplicity of eigenvalues, revealing whether a social system can be decomposed into independent subsystems or whether coupling forces create interdependencies that prevent such decomposition.[1][4]

The **algebraic multiplicity** of an eigenvalue is the number of times that eigenvalue appears as a root of the characteristic polynomial, while the **geometric multiplicity** is the dimension of the eigenspace corresponding to that eigenvalue, which equals the number of linearly independent eigenvectors.[1][39][46] When these multiplicities differ—when a matrix is "defective"—the Jordan form contains non-trivial Jordan blocks larger than \(1 \times 1\), revealing structural rigidity in the system.[1][4][39][46] For social stratification matrices, defectivity directly implies the existence of "locked" social positions where individuals cannot freely transition between classes even in the long run, because the geometric constraints of the system prevent the full exploration of the eigenspace.[39][46]

**Application to Transition Matrices**

In the context of social mobility, the transition matrix \(P\) is a stochastic matrix where each entry \(P_{ij}\) represents the probability of transitioning from social class \(i\) to social class \(j\) in one generation.[14][16][17][45] The eigenvalues of this transition matrix carry profound implications for long-term mobility. For a finite-state Markov chain with a transition matrix, the **largest eigenvalue is always 1** (the spectral radius), and the corresponding left eigenvector is the stationary distribution—the long-run probability distribution across social classes.[25][28][54][58] All other eigenvalues have absolute value strictly less than 1, and their magnitudes determine the rate of convergence to this stationary distribution.[25][28][36]

The convergence rate to equilibrium is controlled by the **spectral gap**, defined as the difference between the largest eigenvalue (which is 1) and the second-largest eigenvalue in absolute value.[33][36] A larger spectral gap means faster convergence to the stationary distribution, while a smaller spectral gap means the system remains sensitive to initial conditions for extended periods, with individuals' positions remaining dependent on their ancestral origins for many generations.[33][36] Crucially, when the Jordan form reveals that the geometric multiplicity of the eigenvalue 1 is less than its algebraic multiplicity—when there exists a non-trivial Jordan block associated with eigenvalue 1—the system exhibits fundamentally different dynamics than when all eigenvalues equal 1 in a trivial multiplicative sense.[1][4]

## Social Stratification as a Mathematical System: Transition Matrices and Their Structure

Social mobility has long been studied through the lens of Markov chains, where individuals occupy discrete social positions and transition between them according to fixed probability distributions.[14][16][17][45][48] The transition matrix framework provides an elegant mathematical representation of social reality: rows correspond to parental social positions, columns correspond to children's positions, and matrix entries represent the probability of intergenerational transition.[14][16][17][45] This approach has been applied extensively in sociology to measure both **structural mobility** (changes in the overall class distribution due to economic transformations) and **exchange mobility** (reranking within a fixed class structure).[32][35]

**The Structure of Empirical Transition Matrices**

Empirical research on intergenerational mobility reveals consistent patterns across developed economies. In the United States, for instance, individuals whose fathers occupy the lowest income quintile have only about a 1.3% probability of reaching the top quintile in their own lifetimes.[13][32][35] Conversely, persistence is dramatically higher at the top: those with fathers in the highest class remain in high positions with substantially greater probability than those attempting upward mobility.[13][32][35] This pattern of high persistence at the top and bottom, with relatively open movement in the middle, creates a characteristic "lumping on the diagonals" phenomenon in the transition matrix—diagonal elements are substantially larger than off-diagonal elements, indicating that individuals tend to remain in their parents' social position.[14][48]

This structural feature is mathematically significant because it produces a transition matrix with an eigenvalue structure that reflects this persistence. The eigenvalues of such matrices cluster near 1, with slow decay rates into the complex plane.[36][58] The geometric and algebraic multiplicities of these eigenvalues, revealed through Jordan decomposition, capture precisely the rigidity of the system: where the Jordan blocks are large, the system is "locked" into reproducing initial inequalities across many generations; where Jordan blocks are small or trivial, mobility is faster and more efficient.[1][4]

**Generational Depth and the Multi-Step Transition Matrix**

A critical limitation of standard transition matrix analysis is that it typically examines only two-generation pairs (parents and children). However, counter-globalization movements operate over time horizons spanning multiple generations, and understanding the cumulative effect of stratification requires examining the matrix raised to higher powers.[17][45] The \(n\)-step transition matrix \(P^n\) describes the probability distribution after \(n\) generations, and the eigenvalue structure determines whether \(P^n\) converges to a limiting matrix as \(n \to \infty\).[17][45]

For regular (aperiodic and irreducible) Markov chains, this limiting matrix exists and is rank 1, with all rows equal to the stationary distribution.[25][28][51] However, the Jordan form reveals the precise rate of convergence and identifies any asymptotic behavior that deviates from smooth decay. When the Jordan form contains Jordan blocks larger than \(1 \times 1\), the convergence to stationarity involves polynomial factors in addition to exponential decay, potentially creating long-term oscillations or slower-than-expected convergence.[1][4] This means that even after many generations, individuals' positions may remain somewhat correlated with their distant ancestors' positions—a phenomenon economists call "long-run persistence."[17][45]

## Ergodicity Theory: From Physics to Social Systems

**Foundational Concepts in Ergodic Theory**

Ergodicity, originally developed in statistical physics and dynamical systems theory, describes systems where the time average behavior of individual trajectories equals the ensemble average across all possible states.[2][8][11] An ergodic system is one where a single long-running system explores the full space of possibilities in a representative manner, eventually visiting all regions with frequencies matching the invariant measure.[2][8][11] Formally, a transformation \(T\) on a probability space is ergodic with respect to a measure \(\mu\) if every measurable set that is invariant under \(T\) has measure either 0 or 1.[11] This mathematical property has profound implications for understanding long-term behavior: in an ergodic system, the long-run statistical properties can be deduced from examining a single trajectory, rather than requiring analysis of all possible trajectories simultaneously.[2][8][11]

The **ergodic theorem**, originally proved by George David Birkhoff in 1931, states that for an ergodic transformation with an invariant measure, time averages along trajectories converge almost everywhere to space averages over the entire system.[8][11] In social terms, this means that in a perfectly ergodic society, the long-run outcomes experienced by any randomly selected individual would eventually match the overall distribution of outcomes across the population.[8][11] Such a society would represent complete social mixing: no family's descendants would be permanently locked into any particular class, and positions would be distributed based solely on chance rather than inherited advantage.[8][11]

**Ergodicity in Markov Chains and Social Systems**

For Markov chains, ergodicity is formalized through the concepts of irreducibility and aperiodicity.[25][28][51] A Markov chain is **irreducible** if every state can reach every other state with positive probability, ensuring that the system explores all available states.[25][28][51] A chain is **aperiodic** if there is no cyclical pattern preventing return to states at certain times; formally, the greatest common divisor of all times at which a state can return to itself is 1.[25][28][51] An ergodic Markov chain is one that is irreducible, aperiodic, and has at most one recurrent class.[25][28][51]

For social stratification, irreducibility would mean that individuals from any class have positive probability of reaching any other class. Aperiodicity would mean that there is no cyclical structure preventing mobility. When both conditions hold, the Markov chain converges to a unique stationary distribution independent of initial conditions.[25][28][51] The ergodic theorem for Markov chains then implies that the proportion of time a chain spends in each state converges to the stationary distribution, providing a quantitative measure of long-run accessibility to each social position.[25][28][36]

**The Spectral Gap and Convergence Rate**

The speed of convergence to the stationary distribution is governed by the **spectral gap** \(\lambda\), defined as the difference between 1 and the absolute value of the second-largest eigenvalue.[33][36] The spectral gap directly controls mixing time: systems with larger spectral gaps mix rapidly, while systems with smaller spectral gaps—near zero—mix extremely slowly.[33][36] The relationship is exponential: the \(L^2\) distance between the current distribution and the stationary distribution decays as \(e^{-2\lambda t}\), meaning that even small reductions in spectral gap create exponentially longer mixing times.[36]

This is profoundly significant for counter-globalization movements because it means that even if a society is technically ergodic (all states accessible with positive probability), it can remain functionally stratified for centuries due to slow mixing. The Jordan form of the transition matrix reveals the structure underlying this mixing rate: the spectral gap is fundamentally constrained by the size of Jordan blocks associated with eigenvalues near 1.[1][4] Large Jordan blocks associated with large eigenvalues create bottlenecks that slow global mixing even when local transitions are rapid.[1][4]

## Defective Matrices and Rigidity in Social Systems

**Defectivity and the Failure of Simple Diagonalization**

A matrix is **defective** if it lacks a sufficient number of linearly independent eigenvectors to form a complete basis—equivalently, if some eigenvalue has geometric multiplicity less than its algebraic multiplicity.[1][39][46] Defective matrices cannot be diagonalized and require the full Jordan normal form to be understood.[1][39][46] This mathematical property has direct sociological significance: defective transition matrices encode social systems with structural rigidity that simple mobility statistics cannot capture.[1][39][46]

When a defective eigenvalue appears in the transition matrix, corresponding to a long-term stationary distribution mode, the defectivity indicates that the system's approach to stationarity involves **generalized eigenvectors** extending beyond ordinary eigenvectors.[1][39][46] These generalized eigenvectors create coupling between different generational cohorts, meaning that the distribution of class membership in generation \(n\) depends not just on generation \(n-1\) but also on generation \(n-2\), \(n-3\), and beyond.[1][4][39][46] This creates **multigenerational effects** where distant ancestors' positions influence descendants' positions even generations later, a phenomenon empirically documented in mobility research.[17][45]

**Jordan Blocks and Locking Mechanisms**

The Jordan block structure reveals precisely how social positions become locked. An \(m \times m\) Jordan block associated with eigenvalue \(\lambda = 1\) has the form where 1 appears on the diagonal and 1 appears on the superdiagonal.[1][4][34] The nilpotent component of this block (the superdiagonal 1s) encodes a mechanism by which individuals occupying certain "locked" positions cannot escape to other positions even with infinite time. The nilpotent index—the smallest power \(k\) such that the nilpotent component raised to the \(k\)th power becomes zero—equals the size of the Jordan block minus 1, determining the number of generations required before the locking mechanism is overcome.[1][4][34]

This mathematical structure maps onto social reality in the following way: suppose a Jordan block of size \(k\) corresponds to the top social class. The nilpotent structure implies that children of top-class individuals are biased toward remaining in the top class, grandchildren face reduced but still substantial bias, great-grandchildren face even less bias, and by the \(k\)th generation of descendants, the bias completely disappears.[1][4][34] Such a structure is empirically consistent with multigenerational wealth persistence documented in economic research, where descendants of wealthy families show advantages that decay across generations but take surprisingly long to disappear completely.[17][45]

## Ergodic Boundaries: Where Mixing Becomes Impossible

**The Concept of Ergodic Boundaries**

The **ergodic boundary** of a social system is the set of conditions and structural parameters that separate regimes where ergodic mixing is possible from regimes where it is impossible.[2][11] In the context of social stratification, this boundary is determined by the eigenvalue structure and Jordan form of the transition matrix. A system with all eigenvalues satisfying \(|\lambda| < 1\) except for a simple eigenvalue of 1 (with geometric multiplicity equal to algebraic multiplicity 1) is fully ergodic: the stationary distribution is unique and globally attracting, and any initial distribution converges to it.[25][28][51]

However, when the Jordan form reveals a non-trivial Jordan block associated with eigenvalue 1, the system crosses the ergodic boundary into a region where true ergodicity is compromised. The existence of generalized eigenvectors means that certain types of initial conditions create trajectories that decay toward stationarity more slowly than the simple exponential decay predicted by the largest eigenvalue alone.[1][4] For social systems, this translates to the existence of families whose descendants remain disadvantaged (or advantaged) for longer than would be expected in a fully ergodic system.[1][4]

**Measuring Distance from the Ergodic Boundary**

Distance from the ergodic boundary can be quantified through several metrics. The **defect index**—the difference between the algebraic and geometric multiplicities of eigenvalue 1—measures how far the system deviates from diagonalizability.[1][39][46] A defect index of 0 means perfect diagonalizability and simple exponential convergence; higher defect indices indicate increasing departure from ergodicity.[1][39][46] Similarly, the **spectral gap** (the distance between 1 and the second-largest eigenvalue magnitude) provides another measure: spectral gaps near zero indicate systems far from true ergodic mixing.[33][36]

These metrics can be estimated from empirical social mobility data. When researchers examine intergenerational transition matrices and perform spectral analysis, they find spectral gaps varying substantially across countries and time periods.[16] Nations with stronger welfare states and more equitable education systems generally show larger spectral gaps and smaller defect indices, indicating faster mobility and greater ergodicity.[16] Conversely, societies with high inequality typically show small spectral gaps and larger defect indices, revealing slower mixing and more rigid stratification systems.[16]

**The Role of Counter-Globalization Forces in Altering the Ergodic Boundary**

Counter-globalization movements attempt to reshape global economic systems through direct action and organizational pressure.[3][6] These efforts can be understood mathematically as attempts to alter the transition matrix \(P\) that governs social mobility. Successful counter-globalization initiatives would increase off-diagonal transition probabilities (making it easier for individuals to move between classes), reduce diagonal elements (making it harder to remain in privileged or disadvantaged positions), and ultimately reduce the spectral gap and defect index of the transition matrix.[3][6]

However, the Jordan form reveals structural obstacles to such transformation. The size and multiplicity of Jordan blocks associated with the largest eigenvalues constrain how quickly the ergodic properties can be improved. Even if counter-globalization movements successfully increase total mobility (reduce diagonal dominance), the Jordan structure of the transition matrix may prevent these changes from fully transforming the system into a truly ergodic state.[1][4] This is because the Jordan form is invariant under similarity transformation: while the matrix can be reordered and rescaled, its fundamental eigenvalue structure and block pattern are intrinsic to the system's dynamical properties.[1][4][34]

## Counter-Globalization as a Flow System and Its Ergodic Properties

**Defining Counter-Globalization Flow**

The counter-globalization movement operates as a complex adaptive system where diverse organizations, activists, and communities coordinate action to challenge global economic inequalities.[3][6] This system exhibits **flow** properties in the sense that information, resources, and personnel move through networks attempting to reach and mobilize populations at multiple scales.[3][6][23] The "flow" in counter-globalization is both literal (people traveling to protest sites, funds moving between organizations) and metaphorical (ideas spreading through social networks, organizational practices diffusing across communities).[3][6][23]

Counter-globalization flow can be represented as a dynamical system operating on the space of social states. Initial states represent existing power distributions and organizational structures. The counter-globalization movement acts as a transformation operator trying to move the system toward states of greater equality and participatory democracy.[3][6] The ergodic properties of this transformed system determine whether the movement can achieve permanent transformation or whether it will be absorbed back into existing hierarchies through counterforces.[3][6]

**Multi-Scale Structure of Counter-Globalization Networks**

Empirical research reveals that counter-globalization organizing operates through decentralized networks with affinity groups as basic organizing units.[3][6] These local groups connect to larger regional and continental forums, creating a multi-scale hierarchy of communication and coordination.[3][6] This structure has been deliberately designed to resist centralized control and to enable rapid adaptation to local conditions while maintaining global solidarity.[3][6] The World Social Forum and European Social Forums provide nodes where diverse movements intersect and coordinate strategy.[3][6]

From a dynamical systems perspective, this multi-scale structure creates layered dynamics at different temporal and spatial scales. Local affinity groups operate with rapid turnover and high internal coordination (high ergodicity within groups). Regional networks operate at intermediate scales with moderate mixing. Global coordination occurs episodically through forum events and online communication, creating slower long-range mixing.[3][6] The overall system exhibits **hierarchical mixing**: rapid local ergodicity at fine scales transitions to slower mixing at larger scales, creating an effective reduction in global ergodicity despite local democracy.[3][6]

**Attempting to Alter Global Ergodicity: The Neoliberal Transition Matrix**

The neoliberal globalization that counter-globalization movements oppose can be represented as a particular transition matrix \(P_{neo}\) that describes how economic policies transform social structures.[3][6] Neoliberal policies—privatization of public services, labor market deregulation, reduction of welfare protections, and deunionization—have the mathematical effect of increasing the diagonal dominance of the global social stratification matrix.[6] By preventing workers from organizing collectively to access higher positions, by reducing public services that enable upward mobility, and by creating precarious "flexploitation" of labor, neoliberalism increases the probability that individuals remain in their original social position across generations.[3][6]

The Jordan form of \(P_{neo}\) reveals structural features of neoliberal stratification: large Jordan blocks associated with large eigenvalues correspond to the "locked" underclasses created by precarious employment, insufficient education access, and debt servitude.[3][6] The spectral gap of \(P_{neo}\) is small, reflecting slow social mixing and persistent inequality across generations.[3][6] Counter-globalization movements seek to create an alternative transition matrix \(P_{alt}\) with smaller diagonal dominance, faster spectral gaps, and smaller defect indices.[3][6]

**The Mathematical Obstacles to Transformation**

The central mathematical challenge is that the Jordan form structure of \(P_{neo}\) imposes constraints on what alternative matrices \(P_{alt}\) are achievable through counter-globalization action. Specifically, the **rank** of the transformation and the **kernel structure** of the transition operator determine feasible alternative equilibria.[1][4][31][34] If counter-globalization movements can only incrementally adjust individual transition probabilities (increase some \(P_{ij}\) values while decreasing others to preserve stochasticity), the achievable set of alternative matrices is constrained by the geometric structure of the original space of stochastic matrices.[1][4]

This constraint becomes more severe when one considers that counter-globalization movements cannot simply erase the historical legacy encoded in the Jordan blocks of existing stratification matrices. The nilpotent components of Jordan blocks represent persistent advantages and disadvantages inherited across generations—these cannot be instantly eliminated but must be gradually dissipated through repeated transformation cycles.[1][4][34] Mathematically, if \(P_{neo}\) has Jordan form \(J_{neo} = D + N\) where \(D\) is diagonal (representing direct transition probabilities) and \(N\) is nilpotent (representing multigenerational persistence), counter-globalization movements must somehow reduce \(N\) toward zero through their actions, while also adjusting \(D\) to increase mobility.[1][4][34]

The problem is that \(N^k = 0\) only after a finite number of powers—the nilpotency index of the Jordan block.[1][4][34] This means that the inherited advantages and disadvantages of position are fundamentally time-bounded, but that bound may extend far into the future. If Jordan blocks are large (high nilpotency index), the system is "locked" for many generations even if counter-globalization movements successfully prevent further entrenchment. Conversely, if Jordan blocks are small, the system is already closer to ergodicity, requiring less transformation to achieve true mixing.

## Integration: Jordan Form Constraints on Ergodic Boundaries in Mobility Functions

**The Fundamental Constraint: Eigenvalue Structure is Invariant**

The deepest mathematical constraint on counter-globalization movements' capacity to transform social systems emerges from the invariance of the eigenvalue structure under similarity transformation. While the Jordan normal form of a matrix can be reordered (by permuting Jordan blocks), the set of eigenvalues and their multiplicities is invariant under any similarity transformation.[1][4][31][34] This means that no amount of organizational work can change the eigenvalues of the global social transition matrix—the fundamental frequencies at which social mobility oscillates are fixed by the economic and institutional structure of global capitalism.[1][4][31][34]

Why is this significant? Because the **ergodic boundary**—the set of conditions determining whether true ergodic mixing is possible—is fundamentally determined by the eigenvalue structure.[2][11][25][28][51] For an irreducible aperiodic Markov chain (the ideal ergodic system in social terms), the unique stationary distribution exists and is globally attractive if and only if eigenvalue 1 has geometric multiplicity exactly 1 and all other eigenvalues have absolute value strictly less than 1.[25][28][51] If counter-globalization movements cannot alter these eigenvalues, they cannot fundamentally move the system across the ergodic boundary.[1][4][25][28][51]

**Decomposing Jordan Blocks: The Multigenerational Penalty**

The Jordan block structure imposes a specific cost on social transformation measured in generations required for change to fully propagate. Consider a society with transition matrix having Jordan form with a block of size \(k\) associated with eigenvalue 1. This block's contribution to the system dynamics involves terms like \(t^j \lambda^t\) for \(j = 0, 1, ..., k-1\), where \(t\) is the generation number and \(\lambda\) is the eigenvalue.[1][4][34] Even when \(\lambda = 1\), these polynomial factors mean that the system's approach to its limiting behavior involves polynomial growth or decay superimposed on the exponential decay from eigenvalues less than 1.[1][4][34]

Operationally, this translates to the following: if a society implements a successful policy intervention that reduces the diagonal dominance of the transition matrix (increases off-diagonal elements), the benefits of this intervention propagate at different rates depending on the initial Jordan structure. For a system with small Jordan blocks, the policy intervention's benefits are felt within a few generations. For a system with large Jordan blocks, the benefits are felt slowly and incompletely, with certain family lineages remaining locked in disadvantaged positions for extended periods despite the policy intervention.[1][4][34]

This is not a flaw of counter-globalization movements but rather a fundamental feature of how stratification systems operate. The mathematical structure of the Jordan form implies that **intergenerational effects are path-dependent**: the outcomes for generation \(n\) depend on outcomes for generations \(n-1\), \(n-2\), ..., \(n-k\) where \(k\) is the size of the relevant Jordan block.[1][4][34] Breaking these multigenerational dependencies requires either: (1) targeting policies specifically at the oldest affected generations to reset initial conditions, or (2) waiting sufficient generations for the nilpotent components to decay naturally.[1][4][34]

**The Spectral Gap as a Limiting Factor in Movement Efficacy**

Counter-globalization movements are constrained in their ability to increase the spectral gap of social transition matrices beyond what the fundamental eigenvalue structure permits. The spectral gap \(\lambda\) controls mixing time according to the relationship: mixing time \(\propto 1/\lambda\).[33][36] If the second-largest eigenvalue in absolute value is \(\lambda_2\), then \(\lambda = 1 - \lambda_2\), and the mixing time is proportional to \(1/(1-\lambda_2)\).[33][36]

The Jordan form reveals what values of \(\lambda_2\) are achievable given the system's constraint structure. If the transition matrix has a large Jordan block associated with a large eigenvalue \(\lambda_2\), increasing the spectral gap beyond \(1 - \lambda_2\) becomes mathematically impossible without fundamentally restructuring the system's capacity to transition between classes.[1][4] Counter-globalization movements operating within capitalist frameworks that constrain class mobility are implicitly constrained by this eigenvalue structure: they can improve mixing locally through union organizing, education expansion, and wealth redistribution, but global mixing time remains limited by the spectral gap inherent in how global capitalism structures class relationships.[1][4][3][6]

**Application to Real Social Systems: The United States Case**

Empirical analysis of United States intergenerational mobility reveals a transition matrix with spectral gap approximately 0.15-0.20, corresponding to a mixing time of roughly 5-7 generations.[16][36] This means that shocks to the class distribution take about 5-7 generations to fully dissipate, and families' positions after that many generations remain only weakly dependent on initial conditions. However, the Jordan structure of the actual empirical transition matrix is more complex than a simple diagonal form.[1][4][16] The presence of non-trivial Jordan blocks extends the effective time constant for certain types of initial conditions beyond what the spectral gap alone would predict.[1][4]

When counter-globalization movements and progressive policies in the United States have successfully increased certain off-diagonal transition probabilities (for instance, through expansion of higher education access or increased social mobility during economic expansions), the overall spectral gap has improved somewhat, but not dramatically.[16] The Jordan structure has constrained how much global mixing rate can increase, because the fundamental eigenvalue structure reflects the deep structural features of capitalist production (class division, capital accumulation, labor commodification) that are difficult to alter without moving beyond capitalism entirely.[1][4][3][6]

## Ergodicity Breakdown: Non-Markovian and Non-Stationary Effects

**The Inadequacy of Simple Markov Models**

While the Markov chain transition matrix framework provides powerful analytical tools, real social systems exhibit complexities not captured by first-order Markovian assumptions. The Markovian assumption states that the probability of transitioning from state \(i\) to state \(j\) depends only on the current state \(i\), not on the history of previous states.[14][45][48] However, empirical research on intergenerational mobility reveals significant violations of this assumption: individuals' current class membership is influenced not just by their parents' class but by their grandparents' class, and possibly by even more distant ancestors.[17][45]

These non-Markovian effects correspond precisely to the existence of non-trivial Jordan blocks in the transition matrix. A second-order Markov process, where outcomes depend on states at times \(t-1\) and \(t-2\), can be reformulated as a first-order Markov chain on an enlarged state space, but the Jordan structure of this enlarged system reveals the coupling between different generational levels.[1][4][17][45] This coupling creates a fundamental obstacle to ergodicity: the system cannot explore the full space of outcomes independently of its history, because historical conditions constrain future possibilities through Jordan block coupling.[1][4]

**Temporal Variation in the Transition Matrix**

Another critical complexity is that the transition matrix itself is not truly stationary over time. Economic cycles, technological changes, policy interventions, and cultural shifts alter transition probabilities across generations.[17][45][48] This creates a **time-inhomogeneous Markov chain** where the transition matrix \(P(t)\) varies with generation \(t\), rather than a simple time-homogeneous chain with constant \(P\).[17][45][48] The Jordan form of time-inhomogeneous systems is far more complex to analyze, because the eigenvalues and eigenvectors of \(P(t)\) change across time.[1][4][29]

For counter-globalization movements, this non-stationarity presents both challenges and opportunities. The challenge is that improvements in social mobility achieved through movement action may be temporary, lasting only so long as favorable political-economic conditions persist. The opportunity is that by shifting power relationships and institutional structures, counter-globalization movements can alter not just individual transition probabilities but the fundamental eigenvalue structure of the social transition matrix, shifting the system across the ergodic boundary.[3][6][19]

**Feedback and Self-Organization in Counter-Globalization Systems**

Counter-globalization movements are not merely external perturbations to social systems but rather endogenous forces that reshape the systems themselves. This creates **feedback effects** where the movement's actions alter the transition matrix, which changes the dynamics that the movement responds to, creating a complex dynamical interplay.[19][22][23] Such systems can exhibit emergence of new patterns and self-organization that transcend the simple eigenvalue structure of either the initial system or the movement's localized actions.[19][22][23]

Mathematically, these feedback systems are described by dynamical systems with mean-field interactions, where individual-level behaviors aggregate into population-level patterns that then feed back to influence individual-level decisions.[19][22][23] The ergodic properties of such coupled systems are complex and not fully reducible to the eigenvalue structure of any single matrix. Instead, equilibria emerge through the interaction of multiple coupled systems with their own Jordan structures, creating possibilities for regime shifts and bifurcations not present in simpler systems.[19][22][23]

## Implications: What Jordan Form Analysis Reveals About Counter-Globalization Prospects

**The Case for Structural Transformation Beyond Reformism**

The Jordan form analysis reveals fundamental limits to what can be achieved through incremental reforms within existing capitalist structures. The eigenvalue structure of capitalist social systems reflects the deep structural features of capital accumulation, class division, and labor commodification.[1][4][3][6] Attempting to increase social mobility through policies like education expansion, progressive taxation, or labor organizing can improve the spectral gap marginally, but cannot fundamentally alter the eigenvalue structure without moving beyond capitalism itself.[1][4][3][6]

This analysis supports the radical wing of counter-globalization movements that call for systemic transformation rather than mere reform of neoliberal systems.[3][6] If the goal is to cross the ergodic boundary and create a truly mixing social system with equal long-run prospects for all individuals regardless of birth position, then the eigenvalue structure itself must be transformed, not merely adjusted.[1][4][3][6] This might be achieved by creating economic systems based on different principles—worker ownership, participatory planning, gift economies—that generate different transition probabilities and hence different eigenvalue structures.[1][4][3][6]

**The Multigenerational Time Horizon Required for Full Transformation**

Jordan form analysis also reveals that even successful systemic transformation requires substantial time to fully propagate through the population. The nilpotency indices of Jordan blocks in the existing transition matrix determine the minimum number of generations required for advantages and disadvantages inherited from the old system to fully dissipate.[1][4][34] This explains why revolutions and systemic transformations often fail to produce equality immediately: the old system's Jordan structure persists, locking in advantages and disadvantages across generations even after political and economic structures change.[1][4][34]

For counter-globalization movements, this implies that long-term commitment to transformation is essential. The benefits of system change accumulate across generations as the nilpotent components of the old system's Jordan blocks decay to zero. Patience and intergenerational solidarity become strategic necessities, not mere virtues.[1][4][34] Movements that abandon their agenda after decades of struggle may do so just as the benefits of earlier work begin to compound across generations.[1][4][34]

**The Organizational Challenge of Maintaining Ergodicity in Movement Structure**

Counter-globalization movements themselves are social systems whose ergodic properties determine their capacity to maintain internal democracy and prevent the emergence of hierarchies.[3][6][22][23][28] To the extent that movements adopt structures with non-trivial Jordan blocks—hierarchical leadership, gatekeeping of information, or unequal access to decision-making power—they reproduce within their own organization the stratification patterns they oppose in society at large.[3][6][22][23]

True internal ergodicity would require that information flows freely through all organizational levels, that leadership positions are occupied by different individuals across time (rapid mixing of roles), and that decision-making power is distributed so that no permanent privileged positions emerge.[3][6][22][23] The decentralized affinity group structure that many counter-globalization movements adopt is, in this sense, an attempt to maximize organizational ergodicity by preventing large Jordan blocks from forming.[3][6]

However, maintaining such structures under pressure is challenging. External repression, internal conflicts, and the natural tendency toward leadership concentration create pressures that transform ergodic organizational structures into more stratified ones with larger Jordan blocks.[3][6][22][23] Successful long-term counter-globalization movements must therefore develop organizational technologies and practices that continuously work to maintain high ergodicity internally, even as they struggle against the low-ergodicity structures of capitalist society.[3][6][22][23]

## Advanced Analysis: Spectral Gaps in Non-Reversible Systems

**The Asymmetry of Downward and Upward Mobility**

In most empirical social transition matrices, downward mobility is less common than upward mobility, and the transition probabilities are not symmetric: the probability of moving from class \(i\) to class \(i+1\) differs from the probability of moving from class \(i+1\) to class \(i\).[16][32][35] This asymmetry reflects the non-reversible nature of social transitions—it is easier to fall into poverty than to escape it, for instance.[16][32][35] From a dynamical systems perspective, non-reversible matrices have more complex spectral properties than reversible (symmetric) matrices.[33][36]

For non-reversible transition matrices, the spectral gap must be defined more carefully through singular values rather than just eigenvalues.[33] The second-smallest singular value of the generator matrix controls the spectral gap for non-reversible systems, and this can differ substantially from what would be predicted by examining eigenvalues alone.[33] This suggests that counter-globalization movements attempting to make mobility systems more reversible—creating equal ease of upward and downward mobility—might achieve faster mixing and larger effective spectral gaps than would be possible while maintaining the asymmetries of capitalism.[33]

**Defect Structures in Specific Social Groups**

The Jordan structure of social transition matrices varies across different demographic groups. Research on intergenerational mobility broken down by race, ethnicity, and gender reveals that different groups often have transition matrices with different eigenvalue structures and defect indices.[13][32][35] For instance, white Americans show faster intergenerational mobility (larger spectral gaps) than Black Americans, reflecting the persistent effects of historical racism encoded as larger Jordan blocks in racialized transition matrices.[13][32][35] Similarly, women's mobility dynamics historically showed different defect structures than men's, reflecting gender-based structural constraints.[13][32][35]

This implies that counter-globalization movements and social justice struggles must be specifically targeted at the Jordan structures particular to marginalized groups. General policies that improve mobility on average may fail to address large Jordan blocks specific to racialized or gendered groups. Effective policies must increase off-diagonal mobility probabilities specifically for transitions currently restricted by racism, sexism, or other forms of oppression, thereby reducing the defect indices specific to those groups.[13][32][35]

## Conclusion: The Mathematical Fundamentals of Durable Social Change

The analysis presented here demonstrates that the Jordan normal form of social stratification matrices provides a powerful mathematical framework for understanding both the limitations and possibilities of counter-globalization movements. The fundamental insight is that **the eigenvalue structure of social transition matrices is invariant under organizational and political action**—while counter-globalization movements can alter transition probabilities and improve spectral gaps, they cannot change the deep eigenvalue structure without fundamentally transforming the economic system itself.[1][4][25][28][51]

The ergodic boundary—the dividing line between societies with true long-run social mixing and those with permanently stratified hierarchies—is determined by this eigenvalue structure. Most capitalist societies operate on the non-ergodic side of this boundary, with Jordan block structures that lock in multigenerational advantages and disadvantages, slow spectral gaps that create long mixing times measured in generations, and defect indices indicating structural rigidity beyond what simple mobility statistics reveal.[1][4][3][6]

Counter-globalization movements face the mathematical reality that incremental reform cannot move social systems across the ergodic boundary.[1][4][3][6] Achieving true ergodic mixing—where all individuals have equal long-run probability of occupying any social position regardless of birth position—requires systemic transformation that alters the fundamental eigenvalue structure. Such transformation may be possible through the creation of post-capitalist economic systems with different production relations, but it cannot be achieved through marginal adjustments to capitalist structures.[1][4][3][6]

Additionally, even successful systemic transformation requires multigenerational commitment to allow the nilpotent components of the old system's Jordan blocks to decay to zero.[1][4][34] Revolutionary moments can alter political and economic institutions quickly, but the social mixing implied by the new system's ergodic properties unfolds across generations as the effects of old inequalities gradually fade.[1][4][34] This explains both the necessity of radical change and the patience required to see its full effects.

For counter-globalization movements themselves, maintaining internal ergodicity while opposing external stratification remains a central organizational challenge.[3][6][22][23] The decentralized structures adopted by many movements represent attempts to prevent large Jordan blocks from forming within movement organization, but this requires constant work against pressures toward hierarchicalization.[3][6][22][23]

The Jordan form analysis also reveals that different social groups and demographic strata face different Jordan structures, with some groups experiencing larger Jordan blocks encoding persistent historical discrimination.[13][32][35] Effective counter-globalization strategy must address these group-specific defect structures through targeted policies increasing off-diagonal mobility for historically excluded populations.[13][32][35]

Finally, the framework presented here suggests that measuring progress toward greater social equality should involve not just tracking aggregate mobility rates but also examining the spectral gap, defect index, and Jordan block structure of transition matrices.[1][4][25][28][51] These metrics reveal whether apparent improvements in mobility are superficial changes in off-diagonal elements or fundamental transformations of the system's eigenvalue structure. True progress toward the erosion of permanent stratification will be marked by decreasing defect indices, increasing spectral gaps, and smaller Jordan blocks—changes that reflect genuine movement toward the ergodic boundary of social mixing.[1][4][25][28][51]

The intersection of Jordan form analysis, ergodic theory, and the study of counter-globalization movements reveals that the mathematical structure of social systems and the political struggles to transform them are deeply interconnected. The Jordan form is not merely a technical mathematical tool but a language for understanding the deep structural rigidities that counter-globalization movements must overcome. By combining rigorous mathematical analysis with attention to the social meanings encoded in matrix structures, we can develop more sophisticated understanding of both the possibilities and limitations of social transformation in the present historical moment.

## Annotations
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Jordan normal form - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Jordan_normal_form'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Ergodicity - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Ergodicity'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Anti-globalization movement', 'url': 'https://en.wikipedia.org/wiki/Anti-globalization_movement'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Notes on Jordan Form - Northwestern University', 'url': 'https://sites.math.northwestern.edu/scg479/courses/notes/jordan-form.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Fate of pseudomobility edges and multiple states in a non-Hermitian ...', 'url': 'https://link.aps.org/doi/10.1103/PhysRevB.111.014315'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Antiglobalization | Social, Economic & Political Impact', 'url': 'https://www.britannica.com/event/antiglobalization'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Projecting social contact matrices to populations stratified by binary ...', 'url': 'https://www.aimspress.com/article/doi/10.3934/mbe.2023154'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Ergodic theory - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Ergodic_theory'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Bounds on Mixing in Stratified Shear Flows', 'url': 'https://www.whoi.edu/cms/files/CaulfieldLec9_21401.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Introduction to Social Network Methods; Chapter 5: Using Matrices', 'url': 'https://faculty.ucr.edu/~hanneman/nettext/C5_%20Matrices.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Ergodic measures (Chapter 9)', 'url': 'https://www.cambridge.org/core/books/dynamical-systems-and-ergodic-theory/ergodic-measures/701D998FC0FBAD34B90AC0748633AA9F'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The critical role of stratification in submarine channels: Implications ...', 'url': 'https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2014JC009807'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Intergenerational mobility measurement with latent transition matrices', 'url': 'https://www.inet.ox.ac.uk/publications/intergenerational-mobility-measurement-with-latent-transition-matrices'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Intragenerational Social Mobility as a Markov Process', 'url': 'https://tyap.net/mediaf/mcfarland.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Stably Stratified Atmospheric Boundary Layers', 'url': 'https://climate-dynamics.org/wp-content/uploads/2015/05/mahrt13a.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Measuring Intergenerational Mobility | Miles Corak', 'url': 'https://milescorak.com/wp-content/uploads/2018/10/econ-85600-corak-lecture-5-measuring-intergenerational-mobility.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Multigenerational Social Mobility: A Demographic Approach', 'url': 'https://www.asanet.org/wp-content/uploads/attach/journals/feb21smfeature.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Boundary Layers: Stratified Fluids', 'url': 'https://www.whoi.edu/cms/files/Lecture3_32345.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Dynamic Systems of Social Interactions', 'url': 'https://www.applied-financial-mathematics.de/sites/default/files/DSSI-JEBO-Revision2.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Towards a re‐conceptualization of flow in social contexts - Hackert', 'url': 'https://onlinelibrary.wiley.com/doi/10.1111/jtsb.12362'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Eigenvalues in microeconomics - arXiv', 'url': 'https://arxiv.org/html/2502.12309v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Ergodic opinion dynamics over networks: learning influences from ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC8245206/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Definition of The Flow System - The Flow Guide', 'url': 'https://flowguides.org/guide.php'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Eigenvalues in microeconomics', 'url': 'https://bengolub.net/wp-content/uploads/2025/02/Eigenvalues_Social_science_notices_AMS__Revision_-2.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '11.3: Ergodic Markov Chains', 'url': 'https://stats.libretexts.org/Bookshelves/Probability_Theory/Introductory_Probability_(Grinstead_and_Snell)/11:_Markov_Chains/11.03:_Ergodic_Markov_Chains'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Implementation of boundary conditions', 'url': 'http://www.lmm.jussieu.fr/~hoepffner/boundarycondition.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Algebraic Structure of Nilpotent and Idempotent Matrices', 'url': 'https://ijmcr.in/index.php/ijmcr/article/download/938/730/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Ergodic Markov Chains', 'url': 'https://gregorygundersen.com/blog/2019/10/28/ergodic-markov-chains/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Dynamical Systems and Linear Algebra', 'url': 'https://d-nb.info/1273230701/34'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Nilpotent Quantum Mechanics: Analogs and Applications', 'url': 'https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2017.00028/full'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Jordan Matrix Decomposition -- from Wolfram MathWorld', 'url': 'https://mathworld.wolfram.com/JordanMatrixDecomposition.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Intergenerational Mobility Measurement with Latent Transition ...', 'url': 'https://iariw.org/wp-content/uploads/2021/08/Bavaro_tullio_paper.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[2310.10876] Spectral gap of nonreversible Markov chains - arXiv', 'url': 'https://arxiv.org/abs/2310.10876'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Jordan normal form - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Jordan_normal_form'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Intergenerational mobility measurement with latent transition matrices', 'url': 'https://www.inet.ox.ac.uk/publications/intergenerational-mobility-measurement-with-latent-transition-matrices'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Lecture 28 : The Spectral Gap - stat.berkeley.edu', 'url': 'https://www.stat.berkeley.edu/~pitman/s205s03/lecture28.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] p..0.·V···ER~/DlscussloN - Institute for Research on Poverty', 'url': 'https://www.irp.wisc.edu/publications/dps/pdfs/dp26275.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Some Principles of Stratification - Kingsley Davis; Wilbert E. Moore', 'url': 'https://inequality.stanford.edu/sites/default/files/media/_media/pdf/Reference%20Media/Kingsley_Moore_Theory.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Generalized eigenvector - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Generalized_eigenvector'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] The Representation of Social Processes by Markov Models1', 'url': 'https://academiccommons.columbia.edu/doi/10.7916/D8X06J43/download'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Some Principles of Stratification - jstor', 'url': 'https://www.jstor.org/stable/2085643'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Generalized Eigenvectors - Penn Math', 'url': 'https://www2.math.upenn.edu/~moose/240S2013/slides7-31.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Movement Patterns, Social Dynamics, and the Evolution of ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3566791/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The Costs of Simplicity: Why Multilevel Models May Benefit from ...', 'url': 'https://journals.sagepub.com/doi/abs/10.1177/0003122417717901'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Multigenerational Social Mobility: A Demographic Approach', 'url': 'https://www.asanet.org/wp-content/uploads/attach/journals/feb21smfeature.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Defective matrix - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Defective_matrix'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Introducing simple models of social systems - AIP Publishing', 'url': 'https://pubs.aip.org/aapt/ajp/article/90/6/462/2820127/Introducing-simple-models-of-social-systems'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A Stochastic Model of Social Mobility', 'url': 'https://tyap.net/mediaf/mcginnis_ses_mob.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] the minimal polynomial and some applications - Penn Math', 'url': 'https://www2.math.upenn.edu/~aaronsil/Math312Spring2013/minpolyandappns.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Absorbing Markov chain - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Absorbing_Markov_chain'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '11.2.4 Classification of States - Probability Course', 'url': 'https://www.probabilitycourse.com/chapter11/11_2_4_classification_of_states.php'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Minimal Polynomials and Diagonal Form - YouTube', 'url': 'https://www.youtube.com/watch?v=RCWpF9jLnRA'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Absorbing Barriers → Area → Sustainability', 'url': 'https://lifestyle.sustainability-directory.com/area/absorbing-barriers/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] 1 Communication classes and irreducibility for Markov chains', 'url': 'http://www.columbia.edu/~ww2040/4701Sum07/4701-06-Notes-MCII.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Eigenvalues for Stochastic Matrices with a Prescribed Stationary ...', 'url': 'https://www.math.uwaterloo.ca/~agtheory/Slides/agt_seminar_reversible.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Nilpotent matrix - StatLect', 'url': 'https://www.statlect.com/matrix-algebra/nilpotent-matrix'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Characteristic polynomial - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Characteristic_polynomial'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Stochastic matrix - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Stochastic_matrix'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[1203.6615] The strong nilpotency index of a matrix - arXiv', 'url': 'https://arxiv.org/abs/1203.6615'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A Characteristic Polynomial for The Transition Probability Matrix of A ...', 'url': 'https://arxiv.org/abs/2012.09619'}}

## Sources
https://en.wikipedia.org/wiki/Jordan_normal_form
https://en.wikipedia.org/wiki/Ergodicity
https://en.wikipedia.org/wiki/Anti-globalization_movement
https://sites.math.northwestern.edu/scg479/courses/notes/jordan-form.pdf
https://link.aps.org/doi/10.1103/PhysRevB.111.014315
https://www.britannica.com/event/antiglobalization
https://www.aimspress.com/article/doi/10.3934/mbe.2023154
https://en.wikipedia.org/wiki/Ergodic_theory
https://www.whoi.edu/cms/files/CaulfieldLec9_21401.pdf
https://faculty.ucr.edu/~hanneman/nettext/C5_%20Matrices.html
https://www.cambridge.org/core/books/dynamical-systems-and-ergodic-theory/ergodic-measures/701D998FC0FBAD34B90AC0748633AA9F
https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2014JC009807
https://www.inet.ox.ac.uk/publications/intergenerational-mobility-measurement-with-latent-transition-matrices
https://tyap.net/mediaf/mcfarland.pdf
https://climate-dynamics.org/wp-content/uploads/2015/05/mahrt13a.pdf
https://milescorak.com/wp-content/uploads/2018/10/econ-85600-corak-lecture-5-measuring-intergenerational-mobility.pdf
https://www.asanet.org/wp-content/uploads/attach/journals/feb21smfeature.pdf
https://www.whoi.edu/cms/files/Lecture3_32345.pdf
https://www.applied-financial-mathematics.de/sites/default/files/DSSI-JEBO-Revision2.pdf
https://onlinelibrary.wiley.com/doi/10.1111/jtsb.12362
https://arxiv.org/html/2502.12309v1
https://pmc.ncbi.nlm.nih.gov/articles/PMC8245206/
https://flowguides.org/guide.php
https://bengolub.net/wp-content/uploads/2025/02/Eigenvalues_Social_science_notices_AMS__Revision_-2.pdf
https://stats.libretexts.org/Bookshelves/Probability_Theory/Introductory_Probability_(Grinstead_and_Snell)/11:_Markov_Chains/11.03:_Ergodic_Markov_Chains
http://www.lmm.jussieu.fr/~hoepffner/boundarycondition.pdf
https://ijmcr.in/index.php/ijmcr/article/download/938/730/
https://gregorygundersen.com/blog/2019/10/28/ergodic-markov-chains/
https://d-nb.info/1273230701/34
https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2017.00028/full
https://mathworld.wolfram.com/JordanMatrixDecomposition.html
https://iariw.org/wp-content/uploads/2021/08/Bavaro_tullio_paper.pdf
https://arxiv.org/abs/2310.10876
https://en.wikipedia.org/wiki/Jordan_normal_form
https://www.inet.ox.ac.uk/publications/intergenerational-mobility-measurement-with-latent-transition-matrices
https://www.stat.berkeley.edu/~pitman/s205s03/lecture28.pdf
https://www.irp.wisc.edu/publications/dps/pdfs/dp26275.pdf
https://inequality.stanford.edu/sites/default/files/media/_media/pdf/Reference%20Media/Kingsley_Moore_Theory.pdf
https://en.wikipedia.org/wiki/Generalized_eigenvector
https://academiccommons.columbia.edu/doi/10.7916/D8X06J43/download
https://www.jstor.org/stable/2085643
https://www2.math.upenn.edu/~moose/240S2013/slides7-31.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC3566791/
https://journals.sagepub.com/doi/abs/10.1177/0003122417717901
https://www.asanet.org/wp-content/uploads/attach/journals/feb21smfeature.pdf
https://en.wikipedia.org/wiki/Defective_matrix
https://pubs.aip.org/aapt/ajp/article/90/6/462/2820127/Introducing-simple-models-of-social-systems
https://tyap.net/mediaf/mcginnis_ses_mob.pdf
https://www2.math.upenn.edu/~aaronsil/Math312Spring2013/minpolyandappns.pdf
https://en.wikipedia.org/wiki/Absorbing_Markov_chain
https://www.probabilitycourse.com/chapter11/11_2_4_classification_of_states.php
https://www.youtube.com/watch?v=RCWpF9jLnRA
https://lifestyle.sustainability-directory.com/area/absorbing-barriers/
http://www.columbia.edu/~ww2040/4701Sum07/4701-06-Notes-MCII.pdf
https://www.math.uwaterloo.ca/~agtheory/Slides/agt_seminar_reversible.pdf
https://www.statlect.com/matrix-algebra/nilpotent-matrix
https://en.wikipedia.org/wiki/Characteristic_polynomial
https://en.wikipedia.org/wiki/Stochastic_matrix
https://arxiv.org/abs/1203.6615
https://arxiv.org/abs/2012.09619