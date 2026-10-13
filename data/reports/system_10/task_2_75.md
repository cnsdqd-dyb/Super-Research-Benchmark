# Deep Research Report: perplexity/sonar-deep-research
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** fc2c7213 | **Time:** 109.04s | **Cost:** $1.01718
--------------------------------------------------------------------------------

# Eigenvectors of Punishment Matrices and the Stability of Social Harmony Gradients in Restorative Justice Games

This comprehensive analysis explores the mathematical foundations underlying the relationship between punishment mechanisms in restorative justice frameworks and the stability of social harmony within game-theoretic models. Recent work integrating spectral graph theory, evolutionary game dynamics, and restorative justice principles reveals that the eigenvectors and eigenvalues of punishment matrices serve as critical determinants of equilibrium stability in social networks. The dominant eigenvector of a punishment matrix, combined with the spectral properties of the underlying network topology, fundamentally shapes whether social systems can achieve sustainable cooperative states or descend into cycles of escalating conflict. This report examines how the mathematical properties of punishment structures, when analyzed through the lens of linear stability theory and spectral network analysis, provide quantitative insights into the conditions necessary for stable social harmony gradients to emerge and persist in populations engaging in restorative justice practices.

## Restorative Justice as a Game-Theoretic Framework

### Foundational Principles of Restorative Justice

Restorative justice represents a paradigmatic shift from traditional retributive approaches to conflict resolution, emphasizing the restoration of relationships and repair of harm rather than punishment for its own sake[1][12][22]. At its core, restorative justice operates on the principle that when harmful behavior occurs, the focus should be on understanding the harm, identifying responsible parties, and determining how the affected community and individual can work together to repair the damage[9][12]. This philosophical framework creates a fundamentally different game-theoretic structure compared to traditional justice systems, as it introduces multiple stakeholders beyond the offender and victim—including community members, facilitators, and broader social networks[1][12][22].

The theoretical underpinnings of restorative justice emphasize several core values that fundamentally alter the mathematical properties of social interactions modeled through game theory[9][12]. These values include empathic understanding, recognition of harm and victim needs, support for restoration processes, accountability that focuses on understanding consequences rather than mere punishment, and community engagement in the resolution process[9]. When translated into mathematical models, these principles create a different objective function compared to retributive systems. Instead of maximizing individual payoff through competitive advantage, restorative justice games reward behaviors that restore relationships and minimize total system harm.

The integration of restorative justice principles into school discipline systems provides empirical evidence that these frameworks produce measurable outcomes distinct from traditional punitive approaches[44][55]. Schools implementing restorative practices saw decreases in misbehavior, substance abuse, and mental health challenges, while simultaneously improving academic achievement[44]. The mathematical implication is significant: restorative justice creates a different equilibrium landscape than pure competitive games, with multiple attractors corresponding to varying levels of cooperation and harmony[12].

### Restorative Justice Behavioral Learning Matrices

The practical implementation of restorative justice employs structured frameworks that can be represented as behavioral matrices, where different infractions and responses are systematically organized[1]. These matrices establish progressive disciplinary consequences that increase in severity while also increasing support mechanisms, creating a coupled system where punishment and intervention escalate together[1]. This coupled structure is mathematically crucial because it prevents the divergence between punishment severity and behavioral change capacity that characterizes many purely punitive systems.

The Raton Public Schools' Behavioral Learning Matrix exemplifies how these frameworks operate in practice[1]. For most behaviors, restorative practices guide students through reflective questions about what happened, what effects occurred, who bears responsibility, and how harm will be repaired[1]. These reflective processes create feedback mechanisms in the social system that enhance information flow about the consequences of behavioral choices. In game-theoretic terms, this improves the informational basis upon which individuals make strategic decisions, potentially moving the system toward more efficient equilibria.

## Punishment Matrices in Evolutionary Game Theory and Social Dynamics

### Mathematical Formulation of Punishment in Game Theory

Punishment in game-theoretic contexts can be formalized as a structured intervention in the payoff matrix that modifies the incentive landscape facing strategic agents[7][14][21][26][34][56]. A fundamental insight from evolutionary game theory is that pure punishment alone frequently fails to sustain cooperation in populations[7][14]. Rather, reputation effects—even arbitrarily small probabilities that one player knows another's punishment inclinations—create bifurcations in the dynamics that shift the population toward more cooperative states[7][14]. This finding establishes that the matrix structure itself must encode information about behavior and reputation to achieve stable cooperation.

The ultimatum game provides a canonical example where punishment matrices reveal this dynamic[7][14]. In this two-player game, one player proposes how to split a resource, and the other player can accept or reject the proposal. If rejected, both players receive nothing. Classical game theory predicts the proposer should offer the minimal positive amount, as any positive offer is better than nothing. However, empirical experiments show proposers typically offer close to half the resource, and responders often reject unfair offers despite the punishing consequence to themselves[7][21]. When this game is embedded in an evolutionary framework with reputation effects, the mathematics demonstrates that even small probabilities that cooperators believe they face punishers can create bifurcations driving toward the observed "social" outcome[7][14].

The mathematical formulation involves defining a payoff matrix \( M \) where entry \( M_{ij} \) represents the payoff to strategy \( i \) against strategy \( j \)[7]. For a public goods game with punishment, strategies can be coded to capture cooperation, defection, and punishment or non-punishment of defectors[7][14]. The replicator dynamics, which describe how the frequency of strategies changes over time proportional to their relative fitness, take the form:

\[\dot{x}_i = x_i(f_i - \bar{f})\]

where \( x_i \) is the frequency of strategy \( i \), \( f_i \) is the fitness of strategy \( i \), and \( \bar{f} \) is the average fitness across all strategies[7][14]. This equation reveals that strategies with above-average fitness increase in frequency, creating selection pressure that can drive populations toward cooperation if the punishment matrix is structured appropriately.

### Empirical Evidence on Punishment and Cooperation

Experimental and computational studies consistently demonstrate that punishment mechanisms, when combined with reputation, can stabilize cooperation in prisoner's dilemma games and public goods games[7][14][21][34][41][56]. A landmark study using evolutionary game theory showed that reputation effects combined with small probabilities of knowing others' punishment behavior can create stable cooperative states[7]. The key mathematical insight is that the bifurcation structure—the way equilibria change as parameters vary—fundamentally depends on the specific structure of the punishment matrix and how reputation information flows through the network.

Hybrid reward-punishment strategies have been shown to create even more stable cooperation than punishment alone, particularly in resource governance contexts[17]. When incentive budgets are allocated between reward and punishment mechanisms, the stability of sustainable cooperation depends critically on both the total incentive available and the ratio between rewards and punishments[17]. This finding suggests that the eigenvalue spectrum of the matrix representing the coupled reward-punishment system determines the basin of attraction for sustainable states.

### Network Structure and Punishment Effectiveness

The topology of the social network through which punishment information propagates fundamentally affects whether punishment mechanisms can stabilize cooperation[59]. In heterogeneous networks with central and peripheral nodes, punishment by central nodes (those with higher connectivity) spreads cooperation more effectively throughout the network than distributed punishment[59]. This network-dependent effect emerges because central nodes' decisions have disproportionate influence on neighboring agents' payoffs and thus on their strategic responses.

Computational simulations with multi-agent reinforcement learning agents playing games on networks reveal that direct punishment by an agent's own partner is more effective at promoting cooperation than third-party punishment from agents not directly involved in the interaction, particularly when combined with partner selection and reputation[56]. The mechanism operates through a process of cluster formation, where cooperative agents preferentially interact with each other, creating local regions of high cooperation that expand over time as defectors are punished and excluded from interactions with cooperative clusters[59].

## Eigenvalue Analysis and the Spectral Properties of Networks

### Spectral Graph Theory Foundations

Spectral graph theory provides mathematical tools for analyzing networks by examining the eigenvalues and eigenvectors of matrices associated with the network structure[15][25][28][39][54]. The two most fundamental matrices in spectral analysis are the adjacency matrix \( A \), where entry \( A_{ij} \) equals one if nodes \( i \) and \( j \) are connected and zero otherwise, and the Laplacian matrix \( L = D - A \), where \( D \) is the diagonal matrix of node degrees[15][25][28][39]. The eigenvalues of these matrices encode critical information about network properties including connectivity, clustering structure, and the capacity for information flow[15][25][28][39].

The largest eigenvalue (spectral radius) of the adjacency matrix is directly related to a network's connectivity and has implications for dynamical processes like epidemic spreading and information diffusion[15][25][28][39][54]. For a random graph with average degree \( \langle k \rangle \), the spectral radius scales approximately as \( \sqrt{\langle k \rangle} \) in sparse networks[15][25][28]. This relationship establishes a quantitative link between network structure (captured by degree distribution) and the dominant eigenvalue that controls many dynamical properties.

The Laplacian matrix's eigenvalues have different interpretations but equally important implications for dynamics on networks[15][25][28][39]. The smallest non-zero eigenvalue, called the algebraic connectivity or Fiedler eigenvalue, measures how well-connected the graph is[25][28][39]. A larger algebraic connectivity indicates faster convergence of diffusion processes and consensus formation on the network[25][28][39]. The eigenvector corresponding to this eigenvalue reveals the bipartition structure of the network—regions of nodes most distant from each other in terms of network structure.

### Spectral Properties of Weighted and Directed Networks

Punishment matrices in restorative justice games are typically represented as weighted networks where edge weights encode the strength or severity of punishment for specific violations[2][5][13][15]. For directed networks where punishment flows from punishers to offenders but not necessarily vice versa, spectral analysis becomes more complex[2][5][13]. The adjacency matrix of a directed graph is generally non-symmetric, requiring analysis of both right and left eigenvectors[2][5][13].

For a weighted directed network with adjacency matrix \( A \), the eigenvalue equation is:

\[A \mathbf{v} = \lambda \mathbf{v}\]

where \( \lambda \) is an eigenvalue and \( \mathbf{v} \) is a right eigenvector[2][13]. The right eigenvector represents the relative importance or "influence" of each node in a fashion proportional to the network's structure. Left eigenvectors, satisfying \( \mathbf{u}^T A = \lambda \mathbf{u}^T \), represent the "susceptibility" of each node to influences flowing through the network[2][13].

For directed networks, the leading eigenvalue (largest in absolute value) is particularly important for determining stability of dynamical systems, though the relationship is more subtle than for undirected networks[2][13][16]. A key result from the study of directed complex networks shows that network heterogeneity (variation in node degrees) is generally destabilizing, meaning that networks with more heterogeneous degree distributions tend to have larger spectral radii and thus exhibit greater instability[2]. This finding has profound implications for punishment systems: networks where punishment authority is concentrated in a few central nodes may be inherently less stable than those where punishment authority is distributed more evenly.

### Spectral Graph Theory Applied to Punishment Matrices

In the context of restorative justice games, a punishment matrix can be constructed where entry \( P_{ij} \) represents the severity of punishment that agent \( i \) will apply to agent \( j \) for a particular transgression[3][6][12][22]. This matrix encodes both the network structure (which pairs of agents interact) and the strength of punishment responses. The eigenvalue spectrum of the punishment matrix then reveals fundamental properties of how punishment effects propagate through the social system.

The spectral radius of the punishment matrix determines whether punishment effects amplify or dampen as they propagate through the network[10][15][37]. If the spectral radius is greater than one, small initial perturbations in punishment behavior can grow exponentially, potentially leading to runaway cycles of retaliation. Conversely, if the spectral radius is less than one, punishment effects naturally dissipate over time, creating stable bounds on conflict escalation[10][37]. This mathematical criterion provides a quantitative stability condition that can be checked before implementing punishment systems in restorative justice contexts.

The eigenvector corresponding to the largest eigenvalue, called the dominant eigenvector, reveals the spatial pattern of how punishment effects are most strongly amplified[10][15][37]. Nodes with large components in the dominant eigenvector experience punishment effects that amplify most efficiently through the network structure. In restorative justice systems, this suggests that central nodes (those with many connections) are critical control points: their punishment behavior can either stabilize or destabilize the entire system depending on whether their behavior follows the restorative justice principles encoded in the system design.

## Stability Analysis of Dynamical Systems on Social Networks

### Linear Stability Analysis and the Jacobian Matrix

When a social system can be described by continuous-time dynamics, its stability properties near equilibrium states can be analyzed through linear stability analysis[52][46][49]. Given a system of differential equations:

\[\frac{d\mathbf{x}}{dt} = \mathbf{F}(\mathbf{x})\]

equilibrium points satisfy \( \mathbf{F}(\mathbf{x}^*) = 0 \)[52][46][49]. The stability of an equilibrium point \( \mathbf{x}^* \) is determined by the eigenvalues of the Jacobian matrix \( J \), defined as:

\[J_{ij} = \frac{\partial F_i}{\partial x_j}\bigg|_{\mathbf{x}^*}\]

If all eigenvalues of \( J \) have negative real parts, the equilibrium is stable (attracting). If any eigenvalue has positive real part, the equilibrium is unstable (repelling)[52][46][49].

For dynamical systems defined on networks, where the dynamics at each node depend on its own state and the states of its neighbors, the Jacobian matrix inherits structure from both the dynamics and the network topology[52][46][13][16][37]. For a general class of networked dynamical systems belonging to the Barzel-Barabási family, the Jacobian takes the form:

\[J_{ii} = a_i, \quad J_{ij} = A_{ij} b_i c_j\]

where \( A \) is the adjacency matrix of the network and \( a, b, c \) are vectors derived from the specific dynamical model[16][37]. This structure reveals that the network's eigenvalue spectrum directly controls the Jacobian's eigenvalue spectrum, establishing a direct link between network topology and system stability.

### Spectral Stability Criteria for Network Dynamics

A remarkable result from recent analysis of stability in large dynamical systems on directed graphs is that stability depends critically on the spectral radius of the network adjacency matrix[13][15][16][37]. For systems with sufficiently large size, the linear stability transition occurs at a critical point where the largest eigenvalue of the system's Jacobian equals zero[13][16]. This transition typically depends on the leading eigenvalue of the network matrix and the parameters of the local dynamics at each node[13][16].

For systems on random directed graphs with heterogeneous degree distributions, the surprising result emerges that infinitely large systems can remain stable even when the degree distribution has unbounded support—a property that does not hold for undirected networks[13]. However, the phase transition between stable and unstable regimes exhibits universal features depending only on the mean degree and degree correlation coefficients[13]. This universality suggests that restorative justice systems might achieve stability across diverse network structures if designed according to universal principles related to mean punishment intensity and correlation structure.

### Origins of Instability: Localization and Delocalization

A crucial insight from recent spectral analysis of networked dynamical systems is that instability can originate from very different spatial locations depending on system parameters[16][37]. In some regimes, instability originates in high-degree (hub) nodes, while in others it originates in low-degree nodes, and in still other regimes it occurs everywhere simultaneously[16][37]. The critical determinant is whether the leading eigenvector of the Jacobian is localized on particular nodes or delocalized across the network[16][37].

For restorative justice systems, this finding has important implications: the nodes (individuals or communities) most responsible for system instability depend on the specific parameters of the punishment and restoration mechanisms. A punishment regime designed assuming instability would originate in hub nodes might fail if the actual system parameters place instability at peripheral nodes or distributed throughout the network.

## Social Harmony Gradients and Their Mathematical Representation

### Defining Harmony in Social Systems

The concept of social harmony can be mathematically formulated as a state space where the system has certain desired properties related to cooperation, fairness, and mutual satisfaction[57]. A basic mathematical equation for expressing harmony degree is:

\[HD = a_i - b_j\]

where \( a \) represents the uniform degree (how much agreement exists), \( b \) is the difference degree (amount of disagreement), \( i \) is the harmony coefficient, and \( j \) is the disharmony coefficient[57]. This formulation captures the intuition that harmony emerges from balancing uniformity (agreement on goals and norms) with tolerance for difference (acknowledgment that not all individuals think identically).

In network terms, a harmony gradient would represent how the degree of social harmony varies spatially across the network—some regions might exhibit high cooperation and low conflict (high harmony), while others exhibit low cooperation and high conflict (low harmony)[57]. The stability of these harmony gradients determines whether the system can maintain regional variation in social states or whether gradients inevitably dissipate, leading to uniform states.

### Gradient Flows and Dissonance Functions

Structural balance theory, which studies how signed networks (networks with positive and negative edges representing friendships and antagonisms) evolve, provides a framework for understanding how harmony gradients stabilize[27][23]. Heider's axioms state that balanced configurations should satisfy: a friend of a friend is a friend, an enemy of a friend is an enemy, a friend of an enemy is an enemy, and an enemy of an enemy is a friend[27][23].

The dynamics of achieving structural balance can be modeled as gradient flow of a dissonance function \( E \), which measures how severely Heider's axioms are violated[27][23]. The gradient flow equations take the form:

\[\frac{dx_{ij}}{dt} = -\frac{\partial E}{\partial x_{ij}}\]

where \( x_{ij} \) represents the signed relationship between agents \( i \) and \( j \)[27][23]. This formulation guarantees that the system evolves to minimize dissonance—to maximize harmony—over time[27][23]. The critical points of the dissonance function represent equilibrium configurations where no gradient flow occurs[27][23].

### Stability of Harmony Equilibria

Harmony equilibria in social networks can be stable or unstable in the Lyapunov sense[46][49][52]. A harmony state is stable if small perturbations to the social relationships do not cause the system to diverge from the harmonious configuration[46][49][52]. Mathematically, if \( \mathbf{x}^* \) represents a harmony equilibrium and \( \mathbf{x}(t) = \mathbf{x}^* + \delta\mathbf{x}(t) \) is a nearby trajectory, stability requires that \( |\delta\mathbf{x}(t)| \to 0 \) as \( t \to \infty \)[46][49][52].

The stability of harmony equilibria depends critically on the eigenvalue spectrum of the Jacobian of the system dynamics near the equilibrium[16][37][46][49][52]. For systems where harmony is maintained by punishment of norm violations, the eigenvalues of the punishment matrix's Jacobian directly determine whether small departures from harmony amplify or decay. If the spectral radius (largest eigenvalue magnitude) is less than one, perturbations decay exponentially, and the harmony state is stable. If any eigenvalue has magnitude greater than one, the state is unstable[46][49][52].

## The Relationship Between Punishment Mechanisms and Network Stability

### Coupling Between Punishment and Cooperation

A fundamental insight from evolutionary game theory combined with network analysis is that punishment and cooperation form a coupled dynamical system where neither can be understood in isolation[3][7][14][17][21][34][41][56][59]. The stability of cooperation depends on whether punishment is sufficiently strong to deter defection but not so strong that it creates cycles of escalating conflict[17][34][41]. Similarly, the sustainability of punishment (whether punishers continue to incur costs to punish) depends on whether cooperation emerges and generates payoffs that reward cooperation[7][14][21][56][59].

In game-theoretic terms, this coupling is captured by the spectral properties of the joint punishment-cooperation matrix[3][7][14][17][34]. If we define a matrix \( M \) where entry \( M_{ij} \) encodes both the cooperation level and punishment intensity in the interaction between agents \( i \) and \( j \), then the eigenvalue spectrum of this coupled matrix determines overall system stability. For restorative justice systems, this coupling is explicit: restoration efforts increase cooperation capacity while simultaneously constraining punishment to levels proportional to harm caused, creating an integrated system rather than separate punishment and cooperation mechanisms.

### Costly Punishment and Reputation Effects

Costly punishment—where the punisher incurs a cost to punish a violator—creates a critical tension in game-theoretic models[7][14][21][26][56][59]. Why would rational self-interested agents pay a cost to punish others? The mathematical resolution involves reputation: if agents know that others will punish free-riders, this knowledge (captured as an arbitrarily small probability that cooperators believe they face punishers) can create bifurcations in the replicator dynamics[7][14]. These bifurcations shift the stable equilibrium from universal defection to universal cooperation[7][14].

The bifurcation structure reveals that reputation creates a separatrix—a boundary in the state space separating the basin of attraction of the defective equilibrium from the cooperative equilibrium[7][14]. The dominance of each basin depends sensitively on both the punishment parameters and the probability of reputation information[7][14]. This sensitivity implies that effective restorative justice systems must carefully calibrate not only punishment severity but also the transparency and reliability of information about who punishes violations.

### Network Topology and Punishment Distribution

The topology of the punishment network—which agents can punish whom—fundamentally affects whether costly punishment can stabilize cooperation[10][38][59]. In well-mixed populations where every agent can potentially punish every other agent, costly punishment often fails because punishers are diluted among many potential targets[38][59]. However, in structured populations where punishment is limited to neighbors in a social network, punishment can create clusters of cooperators that are more successful than surrounding defectors, allowing cooperation to invade and stabilize[38][59].

The mathematical mechanism involves the interaction between two network properties: the degree distribution (how many neighbors each agent has) and the clustering coefficient (how many of an agent's neighbors are connected to each other)[11][33][38][39][51]. Networks with high clustering facilitate punishment of norm violators because gossip about violations spreads efficiently through highly connected local groups[11][33][38]. Conversely, networks with low clustering but high degree (small-world networks) can be unstable because information about who should be punished does not reach all neighbors with sufficient reliability[11][33][38].

### Spectral Control of Punishment Effectiveness

Recent work on functional control of network dynamics using designed Laplacian spectra demonstrates that network dynamics can be precisely controlled by engineering the spectral properties of the network matrix[15][28]. By designing weighted edges (connection strengths) in a network to achieve a desired Laplacian spectrum, one can create networks exhibiting specific dynamical behaviors including localization, pattern formation, or convergence to consensus states[15][28].

For restorative justice systems, this principle suggests that punishment effectiveness can be enhanced by designing the social network's punishment structure to achieve specific spectral properties. For instance, if analysis reveals that stability requires the spectral radius of the punishment matrix to be below a certain threshold, punishment weights can be scaled systematically to achieve this goal while preserving the network's connection pattern[15][28].

## Eigenvectors as Determinants of Stability

### Dominant Eigenvector and System Response

The dominant eigenvector (eigenvector corresponding to the largest eigenvalue) of the punishment matrix reveals the spatial pattern to which the system evolves most readily[10][15][25][37][39][54]. When the punishment system receives a small perturbation, the system's response is initially governed by all eigenvectors, but over time, components along eigenvectors corresponding to larger eigenvalues amplify while components along eigenvectors corresponding to smaller eigenvalues decay[10][15][37][39][46][49].

For a punishment matrix \( P \) with eigenvalues ordered as \( |\lambda_1| > |\lambda_2| > \ldots > |\lambda_n| \) and corresponding eigenvectors \( \mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n \), the long-term response to a perturbation \( \delta \mathbf{x}_0 \) evolves approximately as:

\[\delta \mathbf{x}(t) \approx (\mathbf{v}_1^T \delta \mathbf{x}_0) e^{\lambda_1 t} \mathbf{v}_1\]

This equation reveals that if \( \lambda_1 < 0 \), the perturbation decays exponentially; if \( \lambda_1 > 0 \), it grows exponentially. The eigenvector \( \mathbf{v}_1 \) shows which spatial pattern of punishment (or response to punishment) grows fastest[10][15][37].

In restorative justice contexts, this means analyzing the dominant eigenvector can reveal which communities or social groups are most susceptible to escalating punishment cycles if the system drifts from its intended design. Nodes with large components in the dominant eigenvector are those whose punishment patterns will most strongly amplify perturbations[10][15][37].

### Bipartiteness and Alternating Dynamics

For certain network structures, particularly bipartite networks where nodes can be partitioned into two groups with connections only between groups but not within them, the eigenvalue spectrum has special structure[25][28]. Bipartite graphs have eigenvalues that come in pairs: if \( \lambda \) is an eigenvalue, then \( -\lambda \) is also an eigenvalue[25][28].

This bipartite structure creates alternating dynamics where odd and even iterations evolve differently[25][28]. In social contexts, bipartite structure might arise when society is divided into two opposing groups with intense interactions between groups but weak interactions within groups[25][28][33][36]. Under such conditions, punishment dynamics can create oscillating conflicts where the two groups repeatedly escalate retaliation against each other[25][28][33][36]. The presence of both \( \lambda \) and \( -\lambda \) eigenvalues mathematically guarantees these oscillations are inherent to the network structure rather than accidental features of the punishment parameters[25][28].

Restorative justice systems in polarized communities must contend with this mathematical constraint: if the underlying social network is strongly bipartite, the system is mathematically predisposed toward oscillating cycles rather than stable harmony. Breaking the bipartite structure by creating cross-cutting ties between the opposed groups is thus a fundamental structural intervention, not merely a social preference[25][28][33][36].

### Spectral Gaps and Basin of Attraction

The spectral gap—the difference between the largest and second-largest eigenvalue of the Laplacian matrix—determines how quickly consensus or synchronization can be achieved in networked systems[15][25][28][39]. A large spectral gap indicates fast convergence to consensus, while a small spectral gap indicates slow, fragile consensus that is easily disrupted[15][25][28][39].

For restorative justice systems, this principle implies that systems with large spectral gaps can more readily achieve widespread acceptance of restorative norms and mutual agreements about harmony restoration[15][25][28][39]. Conversely, systems with small spectral gaps may struggle to propagate consensus about justice outcomes throughout the entire community, leading to persistent disagreement about whether harmony has been restored[15][25][28][39].

The spectral gap also relates to the size of the basin of attraction around stable equilibria[15][25][28][39]. Systems with large spectral gaps have larger basins of attraction, meaning they can recover from larger perturbations and still return to the desired harmony state[15][25][28][39]. This robustness property is critical for real-world restorative justice applications where unpredictable events constantly perturb the system.

## Empirical Applications and Practical Implications

### School-Based Restorative Justice Systems

Empirical research on school-based restorative justice demonstrates that these systems can be effectively designed and implemented in ways that reduce conflict and improve outcomes across multiple dimensions[44][55][58]. Schools implementing restorative practices saw substantial improvements in academic achievement, reductions in suspension rates (with disproportionately large benefits for Black and Latino students), and decreases in school-wide misbehavior and substance abuse[44][55].

The empirical data reveals that the effectiveness of restorative practices depends on pervasive integration throughout the school rather than isolated programs[44][55]. This finding aligns with the mathematical prediction that network-level properties (mean degree, spectral radius) determine outcomes more than local properties alone[15][25][38][39]. When restorative practices are distributed throughout the network of school relationships rather than concentrated in isolated programs, they create the network-level effects necessary for systemic change.

Oakland Unified School District's experience exemplifies this principle: their district-wide adoption of restorative justice practices led to an 87 percent reduction in suspensions and elimination of violence within two years at their initial pilot school[55]. The rapid and dramatic change in outcomes suggests that once the school network reached a critical configuration aligned with restorative justice principles, stability shifted to the cooperative equilibrium with self-reinforcing dynamics supporting that state.

### Community Conflict Resolution Networks

Network analysis of conflict and its resolution in broader community contexts reveals that the spatial structure of relationships determines which communities develop intractable conflicts[33][36]. Communities organized as dense clusters with weak inter-cluster connections develop persistent factional conflicts because their internal network structure is bipartite, creating the mathematical conditions for oscillating conflict[33][36].

Conversely, communities that develop cross-cutting ties and overlapping group memberships exhibit greater stability in cooperation and more successful conflict resolution[33][36]. These communities have network properties that break bipartiteness and increase the spectral gap, mathematically facilitating rapid convergence to consensus about justice outcomes[33][36].

Restorative justice practices applied in such network contexts benefit from understanding these structural constraints. Interventions that explicitly create bridging ties between previously separated groups alter the spectral properties of the network, making stable cooperation mathematically more likely[33][36].

## Conclusion

The mathematical analysis of restorative justice games through the lens of spectral graph theory and dynamical systems stability reveals that the eigenvalues and eigenvectors of punishment matrices serve as fundamental determinants of whether social harmony can be achieved and maintained. The spectral radius of the punishment matrix must remain below one for small perturbations to stability to decay rather than grow. The dominant eigenvector reveals which spatial patterns of punishment response most readily amplify, identifying critical nodes and communities whose behavior is most consequential for system stability. The spectral gap of the underlying social network determines how rapidly consensus about justice outcomes can spread and how robustly the system resists perturbation.

The integration of these mathematical insights with restorative justice principles suggests several key design principles for stable systems. First, punishment severity should be carefully calibrated so that the spectral radius of the punishment matrix remains bounded below one, preventing escalating conflict cycles. Second, reputation information about who will punish violations must flow efficiently through the network, requiring high algebraic connectivity or large spectral gap. Third, the punishment network should not be bipartite, as bipartite structure mathematically ensures oscillating cycles of retaliation. Fourth, punishment authority should be somewhat distributed rather than concentrated, as concentrated authority creates spectral heterogeneity that is mathematically destabilizing.

Empirical research on school-based and community-based restorative justice systems confirms these mathematical predictions: systems that become distributed throughout social networks, that integrate reputation mechanisms effectively, and that break polarized social structures achieve stable cooperation and sustained improvements in outcomes. The eigenvectors and eigenvalues that emerge from the mathematical analysis thus serve not as abstract curiosities but as concrete guides for designing justice systems that achieve stability and harmony.

The path forward for restorative justice involves increasingly sophisticated integration of network science and dynamical systems analysis into system design and implementation. As communities and organizations seek to implement restorative practices, analysis of the spectral properties of their social networks can reveal critical vulnerabilities and opportunities for intervention. The mathematics of eigenvalues and eigenvectors provides a rigorous language for communicating about these structural properties and predicting how system modifications will affect stability. By grounding restorative justice implementation in this mathematical framework, practitioners can move beyond trial-and-error approaches toward principled designs that leverage the mathematical structure of social networks to support stable social harmony.

## Annotations
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Behavior Learning Matrix - raton public schools', 'url': 'https://www.ratonschools.com/uploads/1/3/0/3/130384604/behavior_learning_matrix.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Eigenvalue spectra and stability of directed complex networks', 'url': 'https://link.aps.org/doi/10.1103/PhysRevE.106.064302'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The Beautiful Game Theory - using mathematics to resolve human ...', 'url': 'https://projects.research-and-innovation.ec.europa.eu/en/horizon-magazine/beautiful-game-theory-using-mathematics-resolve-human-conflicts'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Creative Restorative Justice Games', 'url': 'https://www.euforumrj.org/creative-restorative-justice-games'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Dynamics and Stability of Social and Economic Networks', 'url': 'https://gaduh.hosted.uark.edu/papers/CarrilloGaduh%20-%202021%20-%20Dynamics%20and%20Stability%20of%20Social%20and%20Economic%20Networks.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Alternative Criminal Justice Systems: A Game Theoretic Analysis', 'url': 'https://lgfellowship.rutgers.edu/research/additional-research-projects/research-project/251-alternative-criminal-justice-systems-a-game-theoretic-analysis'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Reward and punishment | PNAS', 'url': 'https://www.pnas.org/doi/10.1073/pnas.161155698'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': "Stability in social networks - Dunbar's number", 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11040248/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] The Restorative Justice Attitudes Scale: Development and Initial ...', 'url': 'https://www.apa.org/education-career/ce/restorative-justice.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Largest Laplacian eigenvalue predicts the emergence of costly ...', 'url': 'https://link.aps.org/doi/10.1103/PhysRevE.80.066101'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Graph concepts and measures | Social Network Analysis for ...', 'url': 'https://eehh-stanford.github.io/SNA-workshop/graphs.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Justifying Restorative Justice: A Theoretical Justification for the Use ...', 'url': 'https://www.iirp.edu/images/pdf/justifyingrj.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Linear stability analysis of large dynamical systems on random ...', 'url': 'https://link.aps.org/doi/10.1103/PhysRevResearch.2.033313'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Reward and punishment | PNAS', 'url': 'https://www.pnas.org/doi/10.1073/pnas.161155698'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Functional Control of Network Dynamics Using Designed Laplacian ...', 'url': 'https://link.aps.org/doi/10.1103/PhysRevX.8.041043'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Origins of Instability in Dynamical Systems on Undirected Networks', 'url': 'https://arxiv.org/pdf/2512.09765.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Hybrid reward-punishment in feedback-evolving game for common ...', 'url': 'https://link.aps.org/doi/10.1103/PhysRevE.110.034301'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[1406.3387] The Interplay Between Dynamics and Networks - arXiv', 'url': 'https://arxiv.org/abs/1406.3387'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Toward a Restorative Math Pedagogy - PDXScholar', 'url': 'https://pdxscholar.library.pdx.edu/cgi/viewcontent.cgi?article=1310&context=nwjte'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Evaluating Cognitive Social Capital - Diva-portal.org', 'url': 'http://www.diva-portal.org/smash/get/diva2:1150103/FULLTEXT01.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Game theory and reciprocity in some extensive form experimental ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC24109/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Restorative Justice and Responsive Regulation - John Braithwaite', 'url': 'http://johnbraithwaite.com/wp-content/uploads/2019/02/Restorative-Justice-and-Responsive-regulation-book.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Structural Balance via Gradient Flows Over Signed Graphs', 'url': 'https://www.semanticscholar.org/paper/Structural-Balance-via-Gradient-Flows-Over-Signed-Cisneros-Velarde-Friedkin/5eb2bfe4bccef2ce287944381c9c0bc0b600164b'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': "Cooperation in the Prisoner's Dilemma Game Based on the Second ...", 'url': 'https://www.jasss.org/12/4/7.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Spectral Properties of Graphs: Insights into Eigenvalues and Graph ...', 'url': 'https://garph.co.uk/IJARIE/June2018/ijarie-indrani.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Mathematical Models and the Experimental Analysis of Behavior - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC1472627/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Structural Balance via Gradient Flows Over Signed Graphs', 'url': 'https://escholarship.org/content/qt8bm719kp/qt8bm719kp_noSplash_730efa1275d103227c316da9da2259f0.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Lectures on Spectral Graph Theory Fan R. K. Chung', 'url': 'https://fanchung.ucsd.edu/research/cbms.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Neural Mechanisms of Decision Making Under Risk of Punishment ...', 'url': 'https://wires.onlinelibrary.wiley.com/doi/abs/10.1002/wcs.70012'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Fixed‐Time Stable Gradient Flows for Optimal Adaptive Control of ...', 'url': 'https://onlinelibrary.wiley.com/doi/10.1155/2024/5241035'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'How Evolutionary Dynamics Affects Network Reciprocity in ... - JASSS', 'url': 'https://www.jasss.org/18/2/22.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Toward a Restorative Math Pedagogy - PDXScholar', 'url': 'https://pdxscholar.library.pdx.edu/cgi/viewcontent.cgi?article=1310&context=nwjte'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Network Thinking in Peace and Conflict Studies - NSUWorks', 'url': 'https://nsuworks.nova.edu/cgi/viewcontent.cgi?article=1045&context=pcs'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Cooperation and evolutionary dynamics in the public goods game ...', 'url': 'https://pubmed.ncbi.nlm.nih.gov/21843530/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Using a restorative approach to heal and learn from adverse events', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9327844/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Conflict Events-Data and Network Analysis: A Case Study of ...', 'url': 'https://wiki.santafe.edu/images/f/f1/Sf_csss06_meier_et_al.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Origins of instability in dynamical systems on undirected networks', 'url': 'https://journals.aps.org/pre/abstract/10.1103/g2mp-bkhf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Network-based criterion for the success of cooperation in an ...', 'url': 'https://link.aps.org/doi/10.1103/PhysRevE.86.026113'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Spectral Graph Theory and Social Networks', 'url': 'https://ijercse.com/article/10%20May%202024%20IJERCSE.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Power system steady-state stability and the load-flow Jacobian', 'url': 'https://home.engineering.iastate.edu/~jdm/ee554/pai_sauer_sing_jacobian.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Evolutionary dynamics in state-feedback public goods games with ...', 'url': 'https://pubs.aip.org/aip/cha/article/35/4/043138/3344488/Evolutionary-dynamics-in-state-feedback-public'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Multilayer networks: metrics and spectral properties - Cosnet', 'url': 'https://cosnet.bifi.es/wp-content/uploads/2016/03/CFRM01.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Stablility of Fixed Point of a Dynamical System - Aditya M. Deshpande', 'url': 'https://adipandas.github.io/posts/2020/02/stable-unstable-fixed-point/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Fostering Belonging, Transforming Schools: The Impact of ...', 'url': 'https://learningpolicyinstitute.org/product/impact-restorative-practices-brief'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Targeting influence in a harmonic opinion model - arXiv', 'url': 'https://arxiv.org/html/2407.00213v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Stability theory - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Stability_theory'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'How to Evaluate Social Impacts of Restorative Justice', 'url': 'https://www.euforumrj.org/how-evaluate-social-impacts-restorative-justice'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Targeting Influence in a Harmonic Opinion Model - ACM Digital Library', 'url': 'https://dl.acm.org/doi/abs/10.1137/24M1697013'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Stability Theory for Nonlinear Systems', 'url': 'https://www.diag.uniroma1.it/oriolo/amr/material/stability.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Chapter 7 Evolutionary Game Theory - Cornell: Computer Science', 'url': 'https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch07.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Structural robustness and vulnerability of networks - arXiv', 'url': 'https://arxiv.org/html/2409.07498v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '7.5: Linear Stability Analysis of Nonlinear Dynamical Systems', 'url': 'https://math.libretexts.org/Bookshelves/Scientific_Computing_Simulations_and_Modeling/Introduction_to_the_Modeling_and_Analysis_of_Complex_Systems_(Sayama)/07:_ContinuousTime_Models_II__Analysis/7.05:_Linear_Stability_Analysis_of_Nonlinear_Dynamical_Systems'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Evolutionary game theory - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Evolutionary_game_theory'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Estimating and increasing the structural robustness of a network', 'url': 'https://onlinelibrary.wiley.com/doi/full/10.1002/nla.2418'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Toward a Restorative Math Pedagogy - PDXScholar', 'url': 'https://pdxscholar.library.pdx.edu/cgi/viewcontent.cgi?article=1310&context=nwjte'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Investigating the Impact of Direct Punishment on the Emergence of ...', 'url': 'https://arxiv.org/html/2301.08278v3'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Description and Application of a Mathematical Method for the ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC4488008/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Reducing Math Anxiety - Restorative Practices', 'url': 'https://www.iirp.edu/news/reducing-math-anxiety-utilizing-restorative-practices-approaches'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Oxytocin and the Punitive Hub—Dynamic Spread of Cooperation in ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9337605/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] The Mathematics of Harmony', 'url': 'https://www.mi.sanu.ac.rs/vismath/stakhov2013new/origins.pdf'}}

## Sources
https://www.ratonschools.com/uploads/1/3/0/3/130384604/behavior_learning_matrix.pdf
https://link.aps.org/doi/10.1103/PhysRevE.106.064302
https://projects.research-and-innovation.ec.europa.eu/en/horizon-magazine/beautiful-game-theory-using-mathematics-resolve-human-conflicts
https://www.euforumrj.org/creative-restorative-justice-games
https://gaduh.hosted.uark.edu/papers/CarrilloGaduh%20-%202021%20-%20Dynamics%20and%20Stability%20of%20Social%20and%20Economic%20Networks.pdf
https://lgfellowship.rutgers.edu/research/additional-research-projects/research-project/251-alternative-criminal-justice-systems-a-game-theoretic-analysis
https://www.pnas.org/doi/10.1073/pnas.161155698
https://pmc.ncbi.nlm.nih.gov/articles/PMC11040248/
https://www.apa.org/education-career/ce/restorative-justice.pdf
https://link.aps.org/doi/10.1103/PhysRevE.80.066101
https://eehh-stanford.github.io/SNA-workshop/graphs.html
https://www.iirp.edu/images/pdf/justifyingrj.pdf
https://link.aps.org/doi/10.1103/PhysRevResearch.2.033313
https://www.pnas.org/doi/10.1073/pnas.161155698
https://link.aps.org/doi/10.1103/PhysRevX.8.041043
https://arxiv.org/pdf/2512.09765.pdf
https://link.aps.org/doi/10.1103/PhysRevE.110.034301
https://arxiv.org/abs/1406.3387
https://pdxscholar.library.pdx.edu/cgi/viewcontent.cgi?article=1310&context=nwjte
http://www.diva-portal.org/smash/get/diva2:1150103/FULLTEXT01.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC24109/
http://johnbraithwaite.com/wp-content/uploads/2019/02/Restorative-Justice-and-Responsive-regulation-book.pdf
https://www.semanticscholar.org/paper/Structural-Balance-via-Gradient-Flows-Over-Signed-Cisneros-Velarde-Friedkin/5eb2bfe4bccef2ce287944381c9c0bc0b600164b
https://www.jasss.org/12/4/7.html
https://garph.co.uk/IJARIE/June2018/ijarie-indrani.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC1472627/
https://escholarship.org/content/qt8bm719kp/qt8bm719kp_noSplash_730efa1275d103227c316da9da2259f0.pdf
https://fanchung.ucsd.edu/research/cbms.pdf
https://wires.onlinelibrary.wiley.com/doi/abs/10.1002/wcs.70012
https://onlinelibrary.wiley.com/doi/10.1155/2024/5241035
https://www.jasss.org/18/2/22.html
https://pdxscholar.library.pdx.edu/cgi/viewcontent.cgi?article=1310&context=nwjte
https://nsuworks.nova.edu/cgi/viewcontent.cgi?article=1045&context=pcs
https://pubmed.ncbi.nlm.nih.gov/21843530/
https://pmc.ncbi.nlm.nih.gov/articles/PMC9327844/
https://wiki.santafe.edu/images/f/f1/Sf_csss06_meier_et_al.pdf
https://journals.aps.org/pre/abstract/10.1103/g2mp-bkhf
https://link.aps.org/doi/10.1103/PhysRevE.86.026113
https://ijercse.com/article/10%20May%202024%20IJERCSE.pdf
https://home.engineering.iastate.edu/~jdm/ee554/pai_sauer_sing_jacobian.pdf
https://pubs.aip.org/aip/cha/article/35/4/043138/3344488/Evolutionary-dynamics-in-state-feedback-public
https://cosnet.bifi.es/wp-content/uploads/2016/03/CFRM01.pdf
https://adipandas.github.io/posts/2020/02/stable-unstable-fixed-point/
https://learningpolicyinstitute.org/product/impact-restorative-practices-brief
https://arxiv.org/html/2407.00213v1
https://en.wikipedia.org/wiki/Stability_theory
https://www.euforumrj.org/how-evaluate-social-impacts-restorative-justice
https://dl.acm.org/doi/abs/10.1137/24M1697013
https://www.diag.uniroma1.it/oriolo/amr/material/stability.pdf
https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch07.pdf
https://arxiv.org/html/2409.07498v1
https://math.libretexts.org/Bookshelves/Scientific_Computing_Simulations_and_Modeling/Introduction_to_the_Modeling_and_Analysis_of_Complex_Systems_(Sayama)/07:_ContinuousTime_Models_II__Analysis/7.05:_Linear_Stability_Analysis_of_Nonlinear_Dynamical_Systems
https://en.wikipedia.org/wiki/Evolutionary_game_theory
https://onlinelibrary.wiley.com/doi/full/10.1002/nla.2418
https://pdxscholar.library.pdx.edu/cgi/viewcontent.cgi?article=1310&context=nwjte
https://arxiv.org/html/2301.08278v3
https://pmc.ncbi.nlm.nih.gov/articles/PMC4488008/
https://www.iirp.edu/news/reducing-math-anxiety-utilizing-restorative-practices-approaches
https://pmc.ncbi.nlm.nih.gov/articles/PMC9337605/
https://www.mi.sanu.ac.rs/vismath/stakhov2013new/origins.pdf