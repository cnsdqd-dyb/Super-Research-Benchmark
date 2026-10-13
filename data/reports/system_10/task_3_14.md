# Deep Research Report: perplexity/sonar-deep-research
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 33debca9 | **Time:** 138.19s | **Cost:** $1.14195
--------------------------------------------------------------------------------

# Edge Weight Optimization and Markov Equilibrium in Migration Networks: A Comprehensive Analysis of Regional Population Distribution Dynamics

The optimization of edge weights in migration networks represents a critical mechanism through which regional population distributions converge to Markov equilibrium states, fundamentally shaping the long-term demographic structure of interconnected geographic regions. Recent advances in network theory and mathematical modeling demonstrate that when edge weights—representing migration costs, resistance distances, or flow efficiencies between locations—are systematically optimized, the resulting transition matrices governing population flows achieve equilibrium configurations wherein the stationary distribution of population becomes independent of initial conditions[7][15]. This report synthesizes current knowledge regarding how such optimization processes interact with Markov chain properties to establish stable, long-run population equilibria across spatially distributed regions.

## Theoretical Foundations of Migration Networks as Markov Systems

### Markov Chains and Migration Flow Modeling

The application of Markov chain theory to human migration represents one of the most elegant mathematical frameworks for understanding population redistribution across regions[10][55]. A Markov chain in the migration context consists of a finite set of geographic regions as states, with transition probabilities representing the proportion of individuals moving from one region to another during a specified time period[7][39]. The fundamental property of a Markov chain—that the future state depends only on the current state and not on historical paths—aligns remarkably well with migration decisions that are often made based on current conditions rather than past migration trajectories[55].

Consider a simple system with two regions: rural and urban areas. In the classic formulation, individuals transition between these states according to fixed probabilities that capture the attractiveness of each location[10]. The transition matrix \(P\) encodes these probabilities, where element \(p_{ij}\) represents the probability that an individual in region \(i\) moves to region \(j\) during one time period[39]. When this transition matrix is applied iteratively to an initial population distribution vector, it generates a sequence of population distributions over successive time periods. This mathematical structure provides a tractable method for analyzing how populations redistribute in response to location-specific factors such as employment opportunities, amenities, and migration costs[55].

The elegance of the Markov chain approach lies in its capacity to accommodate complex spatial interactions while remaining analytically solvable. A multi-stage network equilibrium model of human migration, which extends basic Markov theory to account for costs of migration and congestion effects, demonstrates that equilibrium conditions can be reformulated as variational inequality problems[7]. This theoretical advancement permits the incorporation of realistic features such as distance-dependent migration costs, population-dependent utilities at different locations, and constraints on migration flows, all while maintaining the mathematical tractability necessary for determining equilibrium configurations[7][56].

### Stationary Distributions and Equilibrium States

A central concept in Markov chain theory applicable to migration networks is the **stationary distribution**, also termed the equilibrium distribution[9][12]. A stationary distribution \(\pi\) is a probability vector that satisfies the equation \(\pi P = \pi\), where \(P\) is the transition matrix[9][42]. This equation embodies a profound principle: when a Markov chain is in its stationary distribution, the application of the transition matrix leaves the distribution unchanged[9]. In the migration context, this means that if the population is distributed across regions according to the stationary distribution, the flows predicted by the migration transition probabilities will maintain exactly this distribution in the subsequent time period[10][55].

For ergodic Markov chains—chains that are irreducible (all states are reachable from one another) and aperiodic (there is no fixed cycle length for returns to states)—a unique stationary distribution exists, and any initial population distribution converges to this stationary distribution as time progresses[9][39][42]. This convergence property is of paramount importance for understanding long-run demographic patterns, as it implies that regardless of the initial population configuration, the system will eventually settle into a characteristic distribution determined entirely by the transition matrix structure[9][42]. The speed of convergence depends on the second-largest eigenvalue of the transition matrix in absolute value; transition matrices with transition probabilities further from the eigenvalues determine faster convergence to equilibrium[42][60].

The stationary distribution has an elegant interpretation through eigenvalue theory: it is the left eigenvector of the transition matrix corresponding to eigenvalue \(\lambda = 1\), normalized so that its components sum to unity[39][42]. This mathematical property connects the probabilistic interpretation of migration flows to the algebraic structure of the transition matrix, allowing sophisticated analysis of how changes to the matrix structure affect the equilibrium distribution. Furthermore, the rate at which the n-step transition matrix \(P^n\) approaches the limiting form depends on the magnitudes of all eigenvalues besides unity; smaller second-largest eigenvalues correspond to faster convergence to the stationary distribution[42][60].

## Edge Weights as Fundamental Parameters in Migration Networks

### Definition and Interpretation of Edge Weights

In the context of migration networks, edge weights represent the quantified resistance, cost, or efficiency associated with population movement between geographic regions[14][20][23]. These weights are not arbitrary parameters but rather encode the fundamental friction that governs migration patterns across space. Edge weights may represent several distinct quantities, depending on the modeling framework employed: they can quantify monetary migration costs, travel distances that create friction against mobility, inverse frequencies of migration flows indicating established pathways, or effective resistances derived from electrical network analogies[14][20][22][23].

The interpretation of edge weights as **effective migration surfaces** provides particular insight into their role in determining population equilibrium[20][23]. When migration rates are estimated from genetic or demographic data using methods like Estimating Effective Migration Surfaces (EEMS), the resulting edge weights represent the historical rates of gene flow or population movement that, within an idealized stepping-stone model, produce the observed genetic dissimilarities or demographic patterns observed in actual data[20][23]. These effective migration rates differ fundamentally from actual historical migration rates; they represent the simplified rates that would generate equivalent population structure within a time-invariant equilibrium framework[20]. This distinction proves crucial for understanding that optimized edge weights in migration network models represent idealized rates that balance competing forces rather than direct observations of migration behavior.

A sophisticated approach to characterizing edge weights employs **resistance distance** theory, which draws analogies from electrical network analysis[14][22]. In this framework, each edge is assigned a conductance (the inverse of resistance), and the resistance distance between two nodes represents the effective resistance between those points if the network were an electrical circuit[22]. The resistance distance has profound mathematical properties: it is proportional to the average commute time of a random walk between two nodes in the network, and it accounts for all possible paths between nodes, not merely the shortest route[14][22]. This multi-path perspective makes resistance distance particularly appropriate for migration networks, where populations do not necessarily follow deterministic shortest paths but rather distribute themselves across multiple routes according to probabilistic factors[22].

### Effective Migration Surfaces and Spatial Heterogeneity

The concept of effective migration surfaces extends beyond simple edge weights to capture spatial variation in migration propensity across geographic space[20][23]. In the EEMS framework, each node (representing a geographic location or subpopulation) is assigned a diversity parameter, and each edge receives a migration rate parameter[20][23]. The edge weights are then parameterized as the average of the migration parameters of the two nodes they connect, introducing a smooth spatial structure to migration intensity[23]. This parameterization encodes a crucial insight: migration barriers and corridors are not uniformly distributed but rather form coherent geographic patterns reflecting underlying economic, cultural, and physical geographic structures[20][23].

The estimation of effective migration surfaces reveals that certain regions experience systematically higher or lower migration rates than would be predicted by distance alone[20]. For example, coastal populations may exhibit greater genetic similarity at given distances than inland populations, reflecting historical maritime trade and communication networks[20]. Similarly, migrations constrained by mountain ranges or other geographic barriers show reduced gene flow across the barrier compared to regions without such physical constraints[20]. These spatial patterns in effective migration reflect the accumulated historical effects of differential accessibility and attractiveness across landscapes[20].

The visual representation of effective migration surfaces provides powerful insights into migration network structure[20][23]. When edge weights are interpolated across geographic space to produce continuous migration surface maps, they reveal the existence of distinct migration corridors, barriers to migration, and hubs of high migration activity[20]. Such visualizations demonstrate that migration networks exhibit inherent spatial organization, with certain pathways featuring systematically lower resistance to movement and others acting as demographic boundaries[20]. Understanding these spatial patterns in edge weights proves essential for predicting how changes to particular migration corridors affect the overall equilibrium distribution.

## Mathematical Formulation of Migration Equilibrium with Network Structure

### Network Equilibrium Conditions and Population Distribution

The mathematical framework for migration equilibrium accommodates both the spatial structure of the network and the behavioral responses of migrants to location-specific utilities and migration costs[7][56]. In its most general formulation, a migration equilibrium specifies a population distribution across locations and a corresponding set of migration flows such that no individual or group has an incentive to alter their location choice given prevailing conditions[56]. This definition parallels the Nash equilibrium concept in game theory, adapted to the context of population distribution[7][56].

The equilibrium conditions can be formally expressed as follows[7][56]. Let \(u_i^k\) denote the utility associated with location \(i\) for an individual of class \(k\) (where classes might represent demographic or socioeconomic categories), and let \(c_{ij}^{kl}\) represent the cost of migration from location \(i\) to location \(j\) for individuals transitioning between class \(k\) and class \(l\)[56]. At equilibrium, individuals choose locations that maximize their net benefit, defined as utility gained minus migration costs incurred[56]. This implies that at equilibrium, the utility at the location chosen must be at least as large as the utility available at any other location, accounting for migration costs[56].

The variational inequality formulation of migration equilibrium provides a mathematically elegant statement of these conditions[7][56]. For a migration equilibrium with migration costs, a population distribution \(p^*\) and flow pattern \(f^*\) satisfy equilibrium if and only if they satisfy:

\[\langle -u(p^*) + c(f^*), (p - p^*, f - f^*) \rangle \geq 0 \text{ for all feasible } (p, f)\][7][56]

This variational inequality simultaneously encodes the conditions that flows must conserve population (no nodes create or destroy individuals) and that individuals respond optimally to utilities and costs[56]. The existence of solutions to such variational inequalities is guaranteed under continuity assumptions on the utility and cost functions, while uniqueness follows under monotonicity conditions (utilities decrease with congestion; costs increase with flow)[7][56].

### Connection Between Edge Weights and Transition Probabilities

The fundamental relationship between edge weights in the network representation and the transition probabilities in the corresponding Markov chain provides the crucial link between network optimization and equilibrium analysis[10][11][55]. In the simplest formulation, transition probabilities can be derived directly from edge weights through a gravity model specification[11][29]. According to this approach, the probability of migration from location \(i\) to location \(j\) depends on the "attraction" or utility at location \(j\) relative to other destinations, discounted by the friction or cost of migration represented by the edge weight[11][29].

A commonly employed gravity model specifies that the expected flow from location \(i\) to location \(j\) is proportional to the product of populations at these locations divided by a distance or cost function raised to some power[29]. When applied to transition probabilities, this becomes:

\[P_{ij} \propto \frac{A_j}{d_{ij}^\alpha}\]

where \(A_j\) represents the attractiveness or utility of location \(j\), \(d_{ij}\) represents the distance or edge weight between locations, and \(\alpha\) is an empirically estimated elasticity parameter[29]. The edge weights thus enter the transition probabilities inversely: higher edge weights (greater migration friction) reduce the probability of moving between locations, while lower edge weights (easier movement pathways) increase transition probabilities[11][29].

More sophisticated formulations recognize that edge weights may themselves be optimized to match observed migration patterns[14][23]. In the EEMS framework, edge weights are adjusted so that the genetic or demographic distances predicted by the model, computed using resistance distances over the weighted network, match observed distances in actual data[14][23]. This optimization approach recognizes that migration networks exhibit complex structure not capturable by simple distance decay functions; certain pathways demonstrate consistently higher migration propensity than others even after accounting for geographic distance[14][23].

### Graph Laplacian Properties and Network Dynamics

The **graph Laplacian** emerges as a fundamental mathematical object connecting edge weights to network dynamics and equilibrium properties[18][39][41][42]. For a weighted network with edge weights represented in the adjacency matrix \(A\), the Laplacian matrix \(L\) is defined as \(L = D - A\), where \(D\) is the diagonal matrix of node degrees (the sum of edge weights incident to each node)[39][42]. The eigenvalue spectrum of the Laplacian encodes crucial information about the network's structural properties and dynamics[39][41].

The smallest eigenvalue of the Laplacian is always zero, with corresponding eigenvector equal to the vector of all ones; this reflects the basic conservation law that the sum of migration flows entering any node must equal the sum leaving (for a closed system)[39][42]. The second-smallest eigenvalue, termed the algebraic connectivity, measures how well-connected the network is; higher algebraic connectivity indicates a more tightly connected network with more effective mixing of populations[39][41][42][60]. The magnitude of this second eigenvalue directly governs the rate of convergence to equilibrium: networks with higher algebraic connectivity converge to their stationary distributions faster[39][42].

The eigenvalue spectrum of the Laplacian also connects to the spectral properties of the transition matrix[39][42][60]. For a transition matrix derived from a weighted network, the eigenvalues of the associated Laplacian determine the temporal behavior of the system: the gap between the largest eigenvalue (unity) and the second-largest eigenvalue controls how quickly the system approaches its stationary distribution[39][42][60]. This mathematical relationship reveals that optimization of edge weights to increase network connectivity directly accelerates convergence to the equilibrium population distribution[39][42].

## Edge Weight Optimization Mechanisms and Algorithmic Approaches

### Optimization for Cost Minimization and Flow Efficiency

The optimization of edge weights in migration networks frequently follows cost-minimization principles derived from operations research and network flow theory[31][34]. The **minimum-cost flow problem** represents a fundamental optimization framework applicable to migration networks: given a network with capacities on edges and costs per unit flow, find the flow pattern that meets specified demands while minimizing total cost[31][34]. In the migration context, this translates to determining flow patterns that satisfy constraints on population conservation while minimizing total migration costs[31][34].

The minimum-cost flow problem can be formally stated as follows[31]. Given a directed graph with nodes \(V\) and edges \(E\), where each edge \((u,v)\) has capacity \(c(u,v)\), cost \(a(u,v)\), and flow \(f(u,v)\), the objective is to minimize:

\[\text{Cost} = \sum_{(u,v) \in E} f(u,v) \cdot a(u,v)\]

subject to capacity constraints \(f(u,v) \leq c(u,v)\) and flow conservation constraints at each node[31]. For migration networks, the "cost" might represent expected migration distance, economic transaction costs, or psychological costs of separation from origin communities, while "flow" represents population movement[31].

One powerful algorithmic approach to solving minimum-cost flow problems is the **cycle-canceling algorithm**, which starts with any feasible flow and iteratively improves it by identifying and removing negative-cost cycles[31]. Another important approach employs the **network simplex algorithm**, which combines properties of the simplex method for linear programming with the special structure of network problems[31]. These algorithms guarantee convergence to optimal solutions while remaining computationally efficient even for large networks[31].

The application of cost-minimization approaches to migration networks reveals that optimized edge weights often differ substantially from raw distance metrics[1][11]. When deep reinforcement learning techniques are applied to optimize edge computing migration (conceptually similar to optimizing physical migration networks), the resulting optimization schemes demonstrate dramatically reduced energy consumption and waiting times compared to simpler selection algorithms[1]. Similarly, in geographic migration contexts, optimizing migration corridors to minimize overall movement costs subject to population distribution constraints reveals that equilibrium populations concentrate in locations that balance accessibility with space for congestion effects[25][26][28].

### Effective Resistance Optimization and Network Topology

An alternative optimization approach leverages the concept of **effective resistance** from electrical network theory[14][22][23]. In this framework, the goal is to adjust edge weights (conductances in the electrical analogy) so that resistance distances between pairs of nodes match observed demographic or genetic distances in actual populations[14][23]. The FEEMS (Fast Estimating Effective Migration Surfaces) method employs this approach, using a Gaussian approximation to the likelihood that observed genetic differences would occur under a hypothesized migration model with specified edge weights[23].

The optimization of edge weights to minimize the discrepancy between predicted and observed resistance distances yields several important insights[14][23]. First, the resulting edge weights exhibit spatial smoothness, with neighboring edges assigned similar weights; this reflects the reality that migration barriers and corridors extend continuously across space rather than appearing as isolated features[14][23]. Second, the optimized weights reveal previously unrecognized migration corridors of systematically low resistance (high migration propensity) and barriers of high resistance[14][20]. Third, the computational efficiency of this optimization approach permits application to very large geographic regions with thousands of nodes, making it practical for continental-scale migration analysis[23].

The mathematical principle underlying resistance distance optimization connects to random walk theory on networks[22][23][60]. The resistance distance between two nodes equals the commute time expected for a random walk beginning at one node and traveling until it reaches the other node and returns to the starting point[22]. Minimizing resistance distances between pairs of nodes is thus equivalent to optimizing the network structure to facilitate rapid mixing—the property that populations distributed across the network equilibrate quickly to a uniform distribution via random movement[22][23][60].

### Spectral Methods for Network Optimization

**Spectral methods** for network analysis and optimization employ the eigenvalue spectrum and eigenvectors of graph matrices to characterize and optimize network properties[41][42][60]. The spectral analysis approach recognizes that the dynamics of processes on networks, including population migration, depend fundamentally on the eigenvalue spectrum of the underlying graph Laplacian[39][41][42][60].

A particularly important insight from spectral analysis concerns the relationship between network structure and convergence to equilibrium[41][42][60]. For any ergodic Markov chain, convergence to the stationary distribution follows a rate governed by the spectral gap—the difference between the largest eigenvalue (unity) and the second-largest eigenvalue[39][42][60]. Networks with larger spectral gaps converge to equilibrium faster[39][42][60]. This insight immediately suggests an optimization objective: adjust edge weights to maximize the spectral gap of the resulting transition matrix, thereby accelerating convergence to the equilibrium population distribution[39][42][60].

The spectral properties of random networks follow universal patterns characterized by **random matrix theory**[41]. For many types of networks—including random graphs, scale-free networks, and small-world networks—the eigenvalue fluctuations of the Laplacian follow Gaussian orthogonal ensemble (GOE) statistics, suggesting a deep universality in how network structure relates to dynamics[41]. However, the specific eigenvalues and eigenvectors differ based on the detailed connection structure, permitting optimization of the network to achieve desired spectral properties[41].

## Convergence Dynamics and the Relationship to Population Equilibrium

### Rates of Convergence to Equilibrium Distribution

The convergence of population distributions to their Markov equilibrium state exhibits temporal dynamics that depend critically on the eigenvalue structure of the transition matrix and, equivalently, on the spectral properties of the underlying migration network[42][60]. For an ergodic Markov chain, the rate of convergence to the stationary distribution \(\pi\) follows:

\[\|P^n - E[\pi]\| \sim \lambda_2^n\]

where \(\lambda_2\) is the second-largest eigenvalue of the transition matrix in absolute value, and \(E[\pi]\) denotes the matrix with each row equal to \(\pi\)[42][60]. This relationship implies exponential convergence with rate determined by \(\lambda_2\); when \(\lambda_2\) is close to unity, convergence is slow, while smaller values of \(\lambda_2\) produce rapid convergence[42][60].

Crucially, the second-largest eigenvalue depends directly on the edge weights in the migration network[39][42][60]. Networks with edge weights configured to create more balanced connectivity—avoiding extreme differences in node degrees and ensuring multiple pathways between regions—exhibit larger spectral gaps and thus faster convergence[42][60]. Edge weight optimization that increases connectivity therefore produces not only more efficient equilibrium states but also faster temporal adjustment to these equilibrium states[42][60].

The interaction between network structure and convergence dynamics becomes particularly complex in systems with multiple time scales, such as those incorporating both labor mobility and capital investment dynamics[28]. A dynamic spatial general equilibrium model incorporating forward-looking capital accumulation alongside worker migration demonstrates that convergence to long-run equilibrium exhibits nonmonotonic regional dynamics: initial immediate effects of productivity shocks differ substantially from long-run effects as capital stocks adjust[28]. Edge weights representing migration costs interact with capital depreciation and investment rates to produce complex transition dynamics; regions initially receiving worker inflows may later experience outflows as capital accumulation increases congestion costs[28].

### Interaction Between Multiple Driving Forces

In comprehensive models of population redistribution incorporating multiple mechanisms—cost of living, political environment, urbanization level, and racial demographics—edge weights and network structure interact with these exogenous factors to determine equilibrium outcomes[27]. A network model of United States inter-county migration employing valued exponential-family random graph models reveals that migration flows exhibit substantial network-level interdependencies; the flow from county A to county B correlates with flows from other origins to the same destination and with reverse flows from B to A[27]. These dependencies reflect social network effects and information cascades that amplify through the migration network[27].

The optimization of edge weights in such complex networks must therefore account for these interdependencies[27]. A simple approach that independently optimizes edge weights for each pair of locations while ignoring network-wide dependencies will mischaracterize equilibrium outcomes[27]. Instead, sophisticated optimization recognizes that populations respond to the expected utility at destinations adjusted for migration costs, and that these expected utilities depend on the full distribution of population across all locations in the network[27].

### Heterogeneity in Migration Propensities and Effective Populations

**Effective population size** concepts from genetics provide useful parallels for understanding how edge weight optimization translates to effective migration propensity[20][23]. Just as effective population size may differ substantially from census size due to variations in reproduction rates, effective migration rates inferred from population genetic data may differ from actual historical migration rates due to variation in reproductive success and settlement patterns[20].

This distinction proves important for understanding the relationship between optimized edge weights and actual observed migration flows[20][23]. Edge weights optimized to match observed genetic or demographic structure represent idealized rates that would generate equivalent patterns within a simplified equilibrium model[20][23]. The actual migration rates producing these patterns may have varied over time, incorporated directional biases, or involved complex temporal dynamics[20][23]. The optimization process effectively filters out these complexities, retaining only the information necessary to characterize equilibrium population structure[20][23].

The interaction between effective migration propensities and network topology becomes crucial when considering how perturbations to the network affect equilibrium outcomes[39][42][60]. Removing or degrading edges with high optimized weights has disproportionate effects on convergence rates and equilibrium distributions, as these edges often correspond to critical pathways in the network that facilitate mixing between otherwise distant regions[39][42][60]. Conversely, optimizing edges currently representing bottlenecks can dramatically accelerate population equilibration[39][42][60].

## Empirical Manifestations of Edge Weight Effects on Population Equilibrium

### Network Structure and Empirical Migration Patterns

Empirical analysis of migration networks reveals striking evidence that edge weights optimize to match geographic and economic realities[30][35][50]. The global migration network during 1960-2015 exhibits hierarchical core-periphery structure, with developed nations forming an interconnected core receiving migrants from peripheral regions[30]. This core-periphery structure emerges not as an exogenously imposed constraint but rather as an equilibrium outcome of edge weight optimization subject to economic disparities and policy constraints[30][25][26].

Countries classified as high-income by the World Bank attract 67% of global migrants despite comprising only 15% of the world population, demonstrating the powerful pulling effect of destination-specific utilities[35]. Furthermore, high-income countries send 33% of global migrants despite representing only 19% of the world population, indicating that migrants tend to originate from wealthier countries with resources enabling long-distance movement[35]. These patterns reflect the equilibrium outcome of edge weights adjusted for both destination attractiveness and origin capacity to generate migrants; edge weights incorporating both migration costs and destination utilities determine the stable population distribution[35].

**Gravity models** of migration, which specify that bilateral flows depend on origin and destination sizes and the distance or cost between them, represent the most widely employed empirical framework for characterizing edge weights[29][26]. The consistency of gravity model specifications across diverse migration contexts—international migration, internal migration within countries, inter-county migration—suggests that a universal principle governs edge weight optimization: populations distribute themselves across space such that marginal migrants are indifferent between origins and destinations, accounting for costs[29][26].

### Regional Variations in Effective Migration Surfaces

Detailed analysis of internal migration in diverse geographic contexts reveals substantial heterogeneity in edge weights across space[8][27][28]. Internal migration in Turkey exhibits geographically bounded communities with well-defined migration routes, consistent with edge weight optimization creating distinct regional subsystems[8]. The hierarchical community structure identified through network analysis demonstrates that cities cluster into groups whose members exchange migrants at substantially higher rates than they exchange with cities in other groups[8]. This community structure emerges from edge weight patterns reflecting proximity, economic complementarity, and transportation infrastructure[8].

Similarly, analysis of internal migration in the United States reveals persistent core-periphery structure at the county level, with large metropolitan areas functioning as migration hubs attracting workers from surrounding rural areas[27]. The edge weights characterizing these migration patterns incorporate both geographic distance and relative economic opportunity; counties with greater wage differentials relative to destinations experience lower edge weights (higher migration propensity) than geographic distance alone would predict[27][28]. Edge weight optimization thus reflects the equilibration of perceived opportunity differences, not merely spatial friction[27][28].

The **California Exodus**—the recent net outmigration from California to other states—illustrates how changes in location-specific utilities propagate through optimized edge weight networks to alter equilibrium population distributions[27]. Increases in housing costs and taxes in California effectively raise edge weights for outbound migration by increasing the cost differential between California and alternative destinations[27]. As these edge weights increase, the stationary distribution of the migration system shifts, with less population concentrated in California and more distributed to lower-cost alternatives[27]. Remarkably, network models incorporating endogenous feedback mechanisms predict that this redistribution occurs through multiple pathways, not simply direct migration from California to the most obvious alternatives but rather cascading redistribution throughout the national migration network[27].

### Mathematical Signatures of Edge Weight Optimization in Real Data

The empirical identification of edge weight optimization in real migration data requires examining whether observed flow patterns match the predictions of optimized network models[14][23][35]. The FEEMS optimization approach, when applied to gray wolf genetic data sampled across North America, reconstructs known geographic features: the Rocky Mountains and Sierra Nevada appear as barriers to gene flow (high resistance), while coastal regions and river valleys appear as corridors of enhanced gene flow (low resistance)[23]. This correspondence between optimized edge weights and known geographic features provides strong evidence that the optimization procedure recovers meaningful network structure from data[23].

Similarly, Facebook-based estimates of international migration flows exhibit correlation patterns consistent with edge weight optimization reflecting both distance and bilateral relationship strength[35]. Regions with strong social ties despite geographic distance show migration patterns inconsistent with simple distance decay, instead exhibiting lower effective edge weights (higher migration propensity) due to social network effects that facilitate movement[35]. The optimization of edge weights to match observed migration flows therefore effectively incorporates social capital and network effects that simple gravity models neglect[35].

## Establishing the Markov Equilibrium State Through Optimal Network Design

### Theoretical Conditions for Equilibrium Existence and Uniqueness

The existence and uniqueness of Markov equilibrium states in migration networks depends critically on the mathematical properties of the transition matrix derived from edge weights[7][39][56]. For finite-state ergodic Markov chains—chains with the property that all states are mutually reachable (irreducibility) and the expected return time to any state is finite (positive recurrence)—a unique stationary distribution always exists[39][42][60]. Furthermore, the distribution of the system converges to this stationary distribution regardless of initial conditions[39][42][60].

These fundamental theoretical results imply that properly configured edge weights always yield a well-defined Markov equilibrium state[39][42][60]. The practical question becomes: how should edge weights be configured to achieve a desired equilibrium state? This inverse problem—specifying edge weights that produce a target stationary distribution—admits a solution under mild conditions[15]. Given a target stationary distribution representing desired long-run population shares, linear programming methods can determine a sparse perturbation to the transition matrix that achieves this target while retaining as much of the original structure as possible[15].

The variational inequality framework provides the most general mathematical setting for establishing existence and uniqueness of migration equilibrium[7][56]. Under the assumption of continuous and strictly monotone utility and migration cost functions—implying that utilities decrease with population congestion and costs increase with migration flow—a unique migration equilibrium exists[7][56]. The strict monotonicity condition encodes the economically sensible assumption that migration flows respond to congestion effects and diminishing returns[7][56].

### Design of Edge Weights for Target Equilibrium States

In practical applications of migration network models, a central design question concerns how to adjust edge weights to achieve specific equilibrium outcomes[1][31][34]. For instance, regional development agencies may seek to design migration corridors (optimize edge weights) to encourage population growth in declining regions while managing depopulation of congested areas[1]. This design problem reduces to choosing edge weights such that the resulting transition matrix produces an equilibrium distribution concentrating population in desired locations[1].

The deep reinforcement learning approach to computing migration optimization demonstrates that intelligent algorithms can discover near-optimal edge weight configurations that minimize migration costs while maintaining high service quality[1]. When applied to edge computing migration (a computational analog of physical migration), deep reinforcement learning algorithms achieve convergence in approximately 16-19 iterations to edge weight configurations minimizing total energy consumption while maintaining acceptable service levels[1]. This rapid convergence reflects the efficiency of learned optimization strategies relative to traditional heuristic approaches[1].

For human migration networks, analogous principles suggest that edge weights can be systematically adjusted through policy interventions affecting migration costs and location utilities[26][27][28]. Infrastructure investments that reduce travel times between regions effectively lower edge weights by reducing migration costs[47]. Tax policies and regulations affecting location utilities directly influence the utility components of the transition matrix, thereby shifting the equilibrium population distribution[27]. Housing policy affecting the relative costs of living in different regions impacts edge weights for both interstate and intra-state migration[27].

### Variational Inequality Formulations for Edge Weight Optimization

The variational inequality framework provides a mathematically sophisticated approach to simultaneously determining edge weights and equilibrium populations[7][56]. Rather than separately specifying edge weights and then computing the resulting equilibrium, the variational inequality formulation integrates these decisions, seeking a migration equilibrium that satisfies both population conservation and individual optimization simultaneously[7][56].

The fundamental variational inequality for migration equilibrium with migration costs states[7][56]: A population and migration flow pattern \((p^*, f^*)\) satisfies migration equilibrium conditions if and only if

\[\langle -u(p^*), p - p^* \rangle + \langle c(f^*), f - f^* \rangle \geq 0\]

for all feasible alternative population and flow patterns \((p, f)\)[7][56]. This inequality simultaneously encodes that no individual benefits from relocating (the first term) and that no inefficiency exists in the network flow (the second term)[7][56].

Solving this variational inequality yields not only the equilibrium populations and flows but also implicitly determines the edge weights that rationalize these equilibrium outcomes[56]. An interesting result from variational inequality theory is that if the utility and cost functions satisfy natural monotonicity conditions (utilities decrease with congestion, costs increase with flow), then the equilibrium is unique[7][56]. This uniqueness guarantees that there exists a single edge weight configuration producing any given target equilibrium, eliminating ambiguity about appropriate policy directions[7][56].

## Advanced Topics: Multiple Timescales and Complex Dynamics

### Dynamic Spatial Equilibrium with Capital Accumulation

More sophisticated models incorporating temporal dynamics beyond simple Markov processes reveal complex interactions between edge weights and population equilibrium across multiple timescales[28]. A dynamic spatial general equilibrium model incorporating forward-looking capital accumulation alongside discrete-choice migration demonstrates that convergence to long-run equilibrium exhibits substantial nonmonotonic dynamics, with intermediate-run outcomes differing markedly from both short-run and long-run effects[28].

The key insight from dynamic equilibrium models is that edge weights representing migration costs interact with capital stock dynamics across locations[28]. When a negative productivity shock hits a region, workers immediately begin migrating away in response to reduced employment opportunities, but capital stocks adjust gradually through depreciation and reduced investment[28]. This creates complex dynamics wherein initially, neighboring regions receive large population inflows (due to low migration costs to nearby alternatives), but later experience outflows as capital accumulation from population inflows increases congestion costs, making once-attractive regions less appealing[28].

These findings imply that optimization of edge weights based on steady-state considerations may prove inappropriate for regions undergoing substantial structural changes[28]. Instead, dynamic optimization approaches accounting for forward-looking expectations and capital dynamics become necessary for predicting and managing population redistribution in response to large shocks[28]. Edge weights that appear optimal for steady-state equilibrium may generate undesirable transition dynamics if capital adjustment lags population migration[28].

### Heterogeneous Agents and Class-Specific Migration

More complex migration models incorporate heterogeneity in migrant types, recognizing that different demographic and socioeconomic groups exhibit different propensities to migrate and respond differently to migration costs and location utilities[26][56]. A theory-consistent gravity equation for interregional migration developed in the context of unemployment explicitly models how search intensities vary across origin-destination pairs based on social network connectivity[26]. This approach reveals that edge weights implicitly incorporate bilateral search network effects, permitting certain origins to access employment opportunities in distant destinations more effectively than geographic distance alone predicts[26].

The inclusion of class-specific heterogeneity in edge weights permits more nuanced analysis of how population redistribution differentially affects demographic groups[56]. A multiclass migration equilibrium model allowing for class transformations (such as changes in skill level or occupational status during migration) demonstrates that individuals selecting destinations that maximize net utility (utility gain minus migration cost) may transition into different socioeconomic classes following migration[56]. Edge weights optimized for aggregate population flow may mask substantial heterogeneity in how different groups respond, with implications for understanding inequality and social stratification in spatial equilibrium[56].

## Synthesis and Implications for Regional Population Management

### Unified Framework Connecting Edge Weights to Equilibrium

The cumulative evidence from diverse research traditions—network analysis, Markov chain theory, economic geography, and operations research—points toward a unified framework wherein edge weight optimization and Markov equilibrium are inextricably linked[7][39][42][56]. Edge weights encode the fundamental friction governing population movement between regions, entering the transition matrix through gravity model specifications or inverse cost relationships[11][29]. Optimization of these weights—whether through cost minimization, resistance distance fitting, or variational inequality methods—adjusts the transition matrix structure, thereby altering the eigenvalue spectrum and, consequently, the stationary distribution representing long-run equilibrium[39][42][60].

The eigenvalue spectrum itself provides crucial information about both equilibrium and dynamics[39][42][60]. The left eigenvector corresponding to eigenvalue unity constitutes the stationary distribution[39][42][42], while the second-largest eigenvalue determines convergence rate[42][60]. Optimization of edge weights that increases the algebraic connectivity of the migration network—bringing more distant regions into effective connection—simultaneously increases the spectral gap, thereby accelerating convergence to equilibrium while potentially altering the equilibrium distribution itself[39][42][60].

This interconnection between structure and dynamics reveals why edge weight optimization proves so consequential for regional population management[1][28][34]. Small changes to edge weights governing critical migration corridors can produce large shifts in both equilibrium populations and convergence rates, with profound implications for regional development and demographic sustainability[27][28].

### Policy Implications and Practical Applications

The framework connecting edge weights to Markov equilibrium suggests several practical policy levers for managing regional population distribution[26][27][28][34]. First, direct investment in migration cost reduction—through transportation infrastructure, communication technology, or information dissemination—effectively reduces edge weights, making movement between regions easier[47]. Such investments accelerate the system's convergence toward equilibrium while potentially altering the equilibrium itself by making peripheral regions more accessible to migrants[47].

Second, location utility enhancement through policy interventions—such as place-based economic development, amenity improvements, or preferential taxation—affects the equilibrium distribution by increasing the attractiveness of targeted locations[25][26][28]. Such interventions effectively lower edge weights for migration toward designated target regions, concentrating population there in the long-run equilibrium[26][28].

Third, the temporal dynamics of adjustment suggest that policymakers must distinguish between immediate migration responses (determined largely by current migration costs) and long-run equilibrium outcomes (incorporating capital accumulation and changing location utilities)[28]. Edge weights optimized for steady-state equilibrium may not account for transitional instability or inequality arising from population disequilibrium during adjustment periods[28].

Fourth, recognition of network-wide interdependencies in migration flows suggests that local optimization of individual migration corridors may prove counterproductive in network-wide contexts[27]. The interdependencies reflected in valued graph models reveal that reducing migration costs on one corridor may indirectly affect migration flows on distant corridors through complex network effects[27]. Systematic network-level optimization rather than piecemeal corridor adjustment better achieves desired regional outcomes[27].

## Conclusion

The optimization of edge weights in migration networks plays a fundamental role in determining the Markov equilibrium state of regional population distribution, operating through mechanisms that connect local network structure to global population dynamics. Edge weights—representing migration costs, geographic friction, and accessibility differences—enter the transition matrix of the migration system, thereby governing the stationary distribution representing long-run population equilibrium. Optimization of these weights through cost minimization, resistance distance fitting, or variational inequality methods produces more efficient, better-connected networks that achieve population equilibrium rapidly while concentrating populations in locations that maximize aggregate utility subject to distance frictions[1][7][39][42][56].

The eigenvalue spectrum of the network's transition matrix or Laplacian provides a unified mathematical framework connecting edge weight optimization to both equilibrium outcomes and convergence dynamics[39][42][60]. Higher-quality edge weight optimization—increasing the algebraic connectivity of the migration network—produces larger spectral gaps that accelerate convergence to the equilibrium distribution while potentially altering the equilibrium itself to reflect more integrated regional systems[39][42][60]. This dual effect of edge weight optimization on both dynamics and equilibrium distinguishes it as a crucial policy lever for regional population management[27][28].

The practical implications extend beyond theoretical understanding to concrete policy applications[26][27][28][34]. Infrastructure investments, economic development policies, and regulatory frameworks all function, in essence, by adjusting the effective edge weights in migration networks, thereby shifting both equilibrium population distributions and the speed of adjustment toward those equilibria[27][28]. Sophisticated policymaking requires recognition that these mechanisms operate through the mathematical structure of network-based Markov systems, enabling systematic analysis of how targeted interventions propagate through migration networks to produce regional outcomes[27][28][34].

Future research should focus on integrating dynamic optimization approaches that account for forward-looking behavior and capital accumulation alongside pure network optimization, developing methods for heterogeneous-agent migration networks that capture class-specific responses to edge weight changes, and applying spectral analysis techniques to empirical migration networks to identify critical edges whose optimization would most efficiently shift regional equilibrium outcomes[28][56]. The convergence of network science, Markov chain theory, and economic geography represented in this research agenda promises to substantially advance understanding of how regions distribute themselves across space and how strategic intervention in migration networks can reshape demographic futures[7][39][42][56].

## Annotations
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Machine Learning Computing Migration and Management Based on ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9484943/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Bounding the Equilibrium Distribution of Markov Population Models', 'url': 'https://arxiv.org/pdf/1007.3130.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Modelling Human Migration on Networks Using Partial Differential ...', 'url': 'https://www.hescor-project.com/2025/07/23/modelling-human-migration-on-networks-using-partial-differential-equations/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] MoDEMS: Optimizing Edge Computing Migrations for User Mobility', 'url': 'https://research.ece.cmu.edu/lions/Papers/MoDEMS_INFOCOM.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Bounding the Equilibrium Distribution of Markov Population Models', 'url': 'https://ui.adsabs.harvard.edu/abs/2010arXiv1007.3130D/abstract'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Structure and Dynamic of Global Population Migration Network - arXiv', 'url': 'https://arxiv.org/abs/2006.02208'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Using Markov Chains To Model Human Migration in a Network ...', 'url': 'https://supernet.isenberg.umass.edu/articles/JPANF.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Investigating internal migration with network analysis and latent ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9540093/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Stationary Distributions of Markov Chains', 'url': 'https://brilliant.org/wiki/stationary-distributions/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Math 309: Linear Algebra', 'url': 'https://users.math.msu.edu/users/richins/teaching/309/Slides1.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A Stochastic Population Model Utilizing Regional Transportation ...', 'url': 'https://www.geocomputation.org/2005/Meyer.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '11.3.2 Stationary and Limiting Distributions - Probability Course', 'url': 'https://www.probabilitycourse.com/chapter11/11_3_2_stationary_and_limiting_distributions.php'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Emergence of Complex Network Topologies from Flow-Weighted ...', 'url': 'https://link.aps.org/doi/10.1103/PhysRevX.14.021050'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Fast and flexible estimation of effective migration surfaces - PMC', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC8324296/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Driving Markov Chains to Desired Equilibria via Linear Programming', 'url': 'https://faculty.ucmerced.edu/hbhat/asilomar19final.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] CMSC 451: Lecture 12 Network Flows: Basic Concepts', 'url': 'https://www.cs.umd.edu/class/spring2025/cmsc451-0101/Lects/lect12-flow-basics.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Stability of nonlinear population systems with individual scale and ...', 'url': 'https://aimspress.com/article/doi/10.3934/math.2023006'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Improving the Convergence of Markov Chains via Permutations and ...', 'url': 'https://onlinelibrary.wiley.com/doi/full/10.1002/rsa.70016'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Resistance distance, closeness, and betweenness - UNIUD', 'url': 'http://users.dimi.uniud.it/~massimo.franceschet/ns/plugandplay/biblio/currentflow.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Visualizing spatial population structure with estimated effective ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC4696895/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Degree distributions in optimized directed network models', 'url': 'https://link.aps.org/doi/10.1103/PhysRevE.111.044308'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Resistance Distances in Directed Graphs: Definitions, Properties ...', 'url': 'https://arxiv.org/pdf/2302.04114.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Fast and flexible estimation of effective migration surfaces | eLife', 'url': 'https://elifesciences.org/articles/61927'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Prediction Equilibrium for Dynamic Network Flows', 'url': 'https://www.jmlr.org/papers/volume24/22-1446/22-1446.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Populations in Spatial Equilibrium - Patrick Farrell', 'url': 'https://www.patrickwfarrell.com/files/ef_pise.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Migration Gravity, Networks, and Unemployment', 'url': 'https://www.ub.edu/aqr/workshop/2021/wp-content/uploads/2021/2Chau.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'California Exodus? A Network Model of Population Redistribution in ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11164555/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Dynamic Spatial General Equilibrium - Princeton University', 'url': 'https://www.princeton.edu/~reddings/papers/SSTD_Paper.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] The Gravity Model James E. Anderson Working Paper 16576 - NBER', 'url': 'https://www.nber.org/system/files/working_papers/w16576/w16576.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Structure and Dynamic of Global Population Migration Network - 2020', 'url': 'https://onlinelibrary.wiley.com/doi/10.1155/2020/4359023'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Minimum-cost flow problem - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Minimum-cost_flow_problem'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Estimating and Conditional Forecasting Bilateral Migration Flows ...', 'url': 'https://pure.iiasa.ac.at/id/eprint/20773/1/aparicio-castro-et-al-2025-estimating-and-conditional-forecasting-bilateral-migration-flows-between-south-america-and.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] The Price of Stability for Network Design with Fair Cost Allocation', 'url': 'https://www.cs.cornell.edu/~eva/fairgame.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Minimum Cost Flow Problem Explained Network Optimization Guide', 'url': 'https://www.youtube.com/watch?v=8b_Lxvy1lIc'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Measuring global migration flows using online data - PNAS', 'url': 'https://www.pnas.org/doi/10.1073/pnas.2409418122'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] The Best of Both Worlds in Network Population Games - NeurIPS', 'url': 'https://proceedings.neurips.cc/paper_files/paper/2023/file/f39931608cdc52d7d9f8ba7003af9136-Paper-Conference.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Spectral analysis of networks with latent space dynamics and signs', 'url': 'https://onlinelibrary.wiley.com/doi/10.1002/sta4.381'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Dynamics of a susceptible-infected-recovered model on complex ...', 'url': 'https://link.aps.org/doi/10.1103/PhysRevE.110.024304'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'MARKOV PROCESSES', 'url': 'https://www.math.drexel.edu/~jwd25/LM_SPRING_07/lectures/Markov.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Spectral analysis and slow spreading dynamics on complex networks', 'url': 'https://link.aps.org/doi/10.1103/PhysRevE.88.032109'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Random matrix analysis of network Laplacians - MPG.PuRe', 'url': 'https://pure.mpg.de/rest/items/item_2220781/component/file_2220780/content'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] 6.262 Lecture 8: Markov eigenvalues and eigenvectors', 'url': 'https://ocw.mit.edu/courses/6-262-discrete-stochastic-processes-spring-2011/4c926d96cd76ee6427d207d0cc08b841_MIT6_262S11_lec08.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] (R2108) Global Asymptotic Stability Analysis of Discrete Time ...', 'url': 'https://digitalcommons.pvamu.edu/cgi/viewcontent.cgi?article=2117&context=aam'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Cost. Versus Time Equilibrium over a - Network', 'url': 'https://onlinepubs.trb.org/Onlinepubs/trr/1994/1443/1443-010.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Percolation in networks composed of connectivity and dependency ...', 'url': 'https://link.aps.org/doi/10.1103/PhysRevE.83.051127'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'ASYMPTOTIC BEHAVIOR OF SOME INTERACTIVE POPULATION ...', 'url': 'https://projecteuclid.org/journals/annals-of-applied-probability/volume-7/issue-4/Asymptotic-behavior-of-some-interactive-population-flow-models/10.1214/aoap/1043862413.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Evaluating Transport Improvements in Spatial Equilibrium', 'url': 'http://www.princeton.edu/~reddings/papers/TE_Paper.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Percolation transition in entangled granular networks - PMC', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC12738784/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] PUSH PULL MIGRATION LAWS - Guido Dorigo* and Waldo Tobler', 'url': 'https://people.geog.ucsb.edu/~tobler/publications/pdf_docs/Push-Pull-migration-laws.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Networks and Models with Heterogeneous Population Structure in ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC7123232/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The Architecture of Connectivity: A Key to Network Vulnerability ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9111940/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Migration Equilibrium', 'url': 'https://supernet.isenberg.umass.edu/austria_lectures/fmigsli.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Heterogeneity in Migration Network Effects Across Cultures', 'url': 'https://bibliothek.wzb.eu/pdf/2021/vi21-102.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Migration efficiency sustains connectivity across agroecological ...', 'url': 'https://esajournals.onlinelibrary.wiley.com/doi/10.1002/ecs2.3543'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A Markovian Analysis Of Migration Differentials', 'url': 'http://www.asasrms.org/Proceedings/y1966/A%20Markovian%20Analysis%20Of%20Migration%20Differentials.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Migration Equilibrium', 'url': 'https://supernet.isenberg.umass.edu/austria_lectures/fmigsli.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] TIONS TO LAPLACIAN SYSTEMS OF EQUATIONS', 'url': 'https://www.cse.iitd.ac.in/~bagchi/AAP_version3_A_Stochastic_Process_on_a_Network_with_Connections_to_Laplacian_Systems_of_Equations.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Stochastic evolution model for international migration | PLOS One', 'url': 'https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0332886'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Refugee migration networks and regulations: a multiclass, multipath ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC7371840'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A Tutorial on the Spectral Theory of Markov Chains - arXiv', 'url': 'https://arxiv.org/pdf/2207.02296.pdf'}}

## Sources
https://pmc.ncbi.nlm.nih.gov/articles/PMC9484943/
https://arxiv.org/pdf/1007.3130.pdf
https://www.hescor-project.com/2025/07/23/modelling-human-migration-on-networks-using-partial-differential-equations/
https://research.ece.cmu.edu/lions/Papers/MoDEMS_INFOCOM.pdf
https://ui.adsabs.harvard.edu/abs/2010arXiv1007.3130D/abstract
https://arxiv.org/abs/2006.02208
https://supernet.isenberg.umass.edu/articles/JPANF.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC9540093/
https://brilliant.org/wiki/stationary-distributions/
https://users.math.msu.edu/users/richins/teaching/309/Slides1.pdf
https://www.geocomputation.org/2005/Meyer.pdf
https://www.probabilitycourse.com/chapter11/11_3_2_stationary_and_limiting_distributions.php
https://link.aps.org/doi/10.1103/PhysRevX.14.021050
https://pmc.ncbi.nlm.nih.gov/articles/PMC8324296/
https://faculty.ucmerced.edu/hbhat/asilomar19final.pdf
https://www.cs.umd.edu/class/spring2025/cmsc451-0101/Lects/lect12-flow-basics.pdf
https://aimspress.com/article/doi/10.3934/math.2023006
https://onlinelibrary.wiley.com/doi/full/10.1002/rsa.70016
http://users.dimi.uniud.it/~massimo.franceschet/ns/plugandplay/biblio/currentflow.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC4696895/
https://link.aps.org/doi/10.1103/PhysRevE.111.044308
https://arxiv.org/pdf/2302.04114.pdf
https://elifesciences.org/articles/61927
https://www.jmlr.org/papers/volume24/22-1446/22-1446.pdf
https://www.patrickwfarrell.com/files/ef_pise.pdf
https://www.ub.edu/aqr/workshop/2021/wp-content/uploads/2021/2Chau.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC11164555/
https://www.princeton.edu/~reddings/papers/SSTD_Paper.pdf
https://www.nber.org/system/files/working_papers/w16576/w16576.pdf
https://onlinelibrary.wiley.com/doi/10.1155/2020/4359023
https://en.wikipedia.org/wiki/Minimum-cost_flow_problem
https://pure.iiasa.ac.at/id/eprint/20773/1/aparicio-castro-et-al-2025-estimating-and-conditional-forecasting-bilateral-migration-flows-between-south-america-and.pdf
https://www.cs.cornell.edu/~eva/fairgame.pdf
https://www.youtube.com/watch?v=8b_Lxvy1lIc
https://www.pnas.org/doi/10.1073/pnas.2409418122
https://proceedings.neurips.cc/paper_files/paper/2023/file/f39931608cdc52d7d9f8ba7003af9136-Paper-Conference.pdf
https://onlinelibrary.wiley.com/doi/10.1002/sta4.381
https://link.aps.org/doi/10.1103/PhysRevE.110.024304
https://www.math.drexel.edu/~jwd25/LM_SPRING_07/lectures/Markov.html
https://link.aps.org/doi/10.1103/PhysRevE.88.032109
https://pure.mpg.de/rest/items/item_2220781/component/file_2220780/content
https://ocw.mit.edu/courses/6-262-discrete-stochastic-processes-spring-2011/4c926d96cd76ee6427d207d0cc08b841_MIT6_262S11_lec08.pdf
https://digitalcommons.pvamu.edu/cgi/viewcontent.cgi?article=2117&context=aam
https://onlinepubs.trb.org/Onlinepubs/trr/1994/1443/1443-010.pdf
https://link.aps.org/doi/10.1103/PhysRevE.83.051127
https://projecteuclid.org/journals/annals-of-applied-probability/volume-7/issue-4/Asymptotic-behavior-of-some-interactive-population-flow-models/10.1214/aoap/1043862413.pdf
http://www.princeton.edu/~reddings/papers/TE_Paper.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC12738784/
https://people.geog.ucsb.edu/~tobler/publications/pdf_docs/Push-Pull-migration-laws.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC7123232/
https://pmc.ncbi.nlm.nih.gov/articles/PMC9111940/
https://supernet.isenberg.umass.edu/austria_lectures/fmigsli.pdf
https://bibliothek.wzb.eu/pdf/2021/vi21-102.pdf
https://esajournals.onlinelibrary.wiley.com/doi/10.1002/ecs2.3543
http://www.asasrms.org/Proceedings/y1966/A%20Markovian%20Analysis%20Of%20Migration%20Differentials.pdf
https://supernet.isenberg.umass.edu/austria_lectures/fmigsli.pdf
https://www.cse.iitd.ac.in/~bagchi/AAP_version3_A_Stochastic_Process_on_a_Network_with_Connections_to_Laplacian_Systems_of_Equations.pdf
https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0332886
https://pmc.ncbi.nlm.nih.gov/articles/PMC7371840
https://arxiv.org/pdf/2207.02296.pdf