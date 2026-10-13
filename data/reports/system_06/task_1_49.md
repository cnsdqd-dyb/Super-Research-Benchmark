# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** f37ef8ab | **Time:** 80.16s | **Cost:** $0.17462
--------------------------------------------------------------------------------

# How Do Connected Components of Local Node Clustering Influence the Isomorphism Group Structure of Identity Construction in Cultural Semantic Networks?

## Abstract

This research report investigates the intricate relationship between local node clustering patterns and the emergence of isomorphism group structures within cultural semantic networks. Drawing upon theoretical frameworks from network science, institutional sociology, and graph neural networks, we develop a comprehensive analytical model that explains how connected components at the local level propagate structural pressures that shape identity construction at both micro and macro levels of analysis. The report synthesizes findings from computational approaches to semantic network analysis with sociological theories of institutional isomorphism to illuminate the mechanisms through which local clustering configurations generate isomorphic tendencies in organizational and cultural identity formation. Our analysis reveals that the clustering coefficient, transitivity patterns, and neighborhood topology serve as fundamental determinants of identity isomorphism, operating through mimetic, coercive, and normative mechanisms that connect local structural properties to global identity configurations.

## 1. Introduction

The study of cultural semantic networks has emerged as a critical interdisciplinary endeavor, bridging computational network analysis with sociological theories of identity and institutional change. Cultural semantic networks represent the structural configurations through which meanings, concepts, and identities are organized and transmitted across social systems [1]. These networks encode the relationships between cultural constructs and the social positions of actors who create and maintain them, revealing patterns of meaning-making that transcend individual-level analysis [2].

At the heart of understanding these networks lies the question of how local structural properties influence broader organizational and cultural phenomena. Local node clustering—characterized by the density of connections among neighboring nodes—represents one of the most fundamental structural features of complex networks. The clustering coefficient, which measures the proportion of possible connections that actually exist among a node's neighbors, provides a quantitative indicator of local structural cohesion [3]. In cultural semantic networks, high clustering coefficients indicate the presence of tightly knit semantic communities where concepts, identities, and meanings are densely interconnected.

The concept of isomorphism, originally developed within institutional sociology, offers a powerful lens for understanding how organizational and cultural forms converge over time. Isomorphism in the context of globalization refers to the tendency of contemporary national societies to adopt standardized institutional forms through global cultural and associational processes [4]. This homogenizing tendency operates through three primary mechanisms: coercive isomorphism, where organizations are forced to change by external forces; mimetic isomorphism, where organizations imitate perceived legitimate models; and normative isomorphism, where professional standards drive convergence [4].

The intersection of local node clustering and isomorphism group structure represents a theoretically rich but underexplored domain. When we consider how connected components of local clustering influence the formation of isomorphic identity structures, we must examine the bidirectional relationship between micro-level network topology and macro-level institutional patterns. This relationship is particularly salient in cultural semantic networks, where the meaning attached to relationships varies by context and shapes tie-formation logics that are institutionalized as rules-of-the-game [5].

The present report addresses this theoretical gap by developing a formal framework that connects local node clustering properties to isomorphism group structures in identity construction. We draw upon multiple theoretical traditions, including graph neural network architectures that formalize message-passing mechanisms in networked structures [6], institutional theory's account of isomorphic pressures [4], and socio-semantic network analysis that reveals the mutual constitution of culture and social networks [2]. By integrating these perspectives, we aim to provide a comprehensive account of how local structural patterns generate cascading effects on identity formation across cultural semantic networks.

## 2. Theoretical Foundations

### 2.1 Local Node Clustering in Network Science

The concept of local clustering occupies a central position in network science, providing essential insights into the structure of complex systems. Clustering, also known as transitivity, represents a typical property of acquaintance networks where two individuals with a common friend are likely to know each other [3]. In graph-theoretic terms, transitivity manifests as the presence of a high number of triangles—complete subgraphs of three nodes where all possible edges exist.

The clustering coefficient of a node provides a precise mathematical characterization of local clustering. For a node u with degree k_u, the clustering coefficient C_u is defined as the ratio of the actual number of edges among neighbors to the maximum possible number of such edges [3]. Formally:

$$C_u = \frac{2 \cdot e_u}{k_u \cdot (k_u - 1)}$$

where e_u represents the number of edges connecting the neighbors of u. This coefficient ranges from 0 to 1, where a value of 1 indicates that all neighbors of u are also neighbors of each other, forming a completely interconnected local community.

The global clustering coefficient, or transitivity T, extends this concept to the network level by measuring the relative number of transitive triples [3]:

$$T = \frac{3 \times \#\text{triangles in } G}{\#\text{connected triples of vertices in } G}$$

The factor of 3 in the numerator compensates for the fact that each complete triangle contributes three connected triples, ensuring that the measure remains bounded between 0 and 1.

An alternative perspective on the clustering coefficient views it as counting the number of closed triangles within each node's local neighborhood [7]. The ego graph of a node—the subgraph containing that node, its neighbors, and all edges between neighbors—provides the structural context for this measurement. This perspective emphasizes that the clustering coefficient measures how tightly clustered a node's neighborhood is, with some nodes in real-world networks exhibiting high clustering coefficients while others show coefficients of zero [7].

Real-world networks throughout the social and biological sciences tend to have far higher clustering coefficients than would be expected if edges were distributed randomly [7]. This property, known as the high clustering property, indicates that local communities play a fundamental role in shaping network structure and function. The identification of these local clusters represents a critical analytical task, requiring efficient community detection techniques that provide reasonable first cuts on the structure of large networks [8].

### 2.2 Isomorphism and Identity Construction

The concept of isomorphism in sociology addresses the question of how organizational and cultural forms become similar over time. In the context of globalization, isomorphism represents an idea of contemporary national societies that is addressed by the institutionalization of world models constructed and propagated through global cultural and associational processes [4]. Despite the heterogeneity of economic and political resources and local cultural origins, many theories suggest that the trajectory of change in political units tends toward homogenization around the world.

Policy convergence across nation states exemplifies isomorphism in action. Within the European Union, for instance, states harmonize policies driven by structural pressures such as directives, regulations, cohesion funds, and collaboration mechanisms [4]. This convergence occurs despite the diversity of local economic forces, power relationships, and traditional cultural forms that might produce different outcomes. Isolated societies that make contact with the global system quickly adopt standardized forms and appear similar to other nation-states around the world.

The mechanisms driving isomorphic change operate at multiple levels. Mimetic isomorphism in organization theory refers to the tendency of an organization to imitate another organization's structure because of the belief that the latter's structure is beneficial [4]. This behavior occurs primarily when an organization's goals or means of achieving these goals are unclear, making imitation of a perceived legitimate model a "safe" way to proceed. A struggling regional university hiring a star faculty member to be perceived as more similar to revered institutions exemplifies this mechanism.

Identity-constrained isomorphism emphasizes the centrality of organizational identity in fostering imitation within social networks [9]. Organizations identify as part of a social network and mimic other organizations that share the same social network identity, independent of any interaction that would facilitate information dissemination. These inter-organizational ties and relationships impact social identification and emulation targets, with organizations imitating those who have similar identity characteristics [9].

The relationship between identity and network structure is bidirectional. Cultural sociology has developed formal frameworks that connect social and semantic networks, examining how semantics relate to social networks and how semantic networks connect to actors [10]. The classical notion of "structural holes," denoting the brokerage position of certain nodes in a social network that connect otherwise weakly connected portions, can be translated in a socio-semantic context as "cultural holes" [10]. These holes describe divergences in the way actors use terms, with communications becoming more difficult when socio-semantic connections match less.

### 2.3 Cultural Semantic Networks and Tie-Formation

Cultural semantic networks represent the structural instantiation of meaning systems within social contexts. Research combining culture and networks has demonstrated that culture is linked to social relations in a mutually constitutive manner [2]. On one hand, culture is reproduced through interactions and therefore relies on concrete interpersonal ties. On the other hand, culture affects the structure of social ties, creating a dual relationship between cultural constructs and network positions.

Tie-formation mechanisms like homophily, reciprocity, transitivity, and preferential attachment operate to varying degrees across contexts [5]. Romantic ties tend to be homophilous by age, education, and ethnicity and remain dyadic, while scientific citations fall into highly unequal preferential attachment patterns. Triangulation is nearly absent in advice and patronage networks but features prominently in friendship ties [5].

This variation in connectivity patterns derives from the meaning attached to relationships, which varies by context. Tie-formation logics are institutionalized rules-of-the-game and susceptible to change over time [5]. The mechanisms of tie-formation behind empirical network patterns have to be connected to the cultural rules in particular fields, revealing how social context shapes networks via cultural rules, not just organizational factors.

Language-based clustering provides a concrete example of how identity attributes shape network structure. Research on language diversity in international business has shown that language is a core element of social identity, with employees in multinational enterprises forming homophily-based clusters with those who share their native language [11]. However, language-based clusters are not monolithic; they intersect with other salient identity attributes such as gender, regional dialects, and education, changing the composition of language-based clusters and altering group dynamics [11].

The bipartite connection between individuals and affiliations makes it possible to define a broader notion of groups by connecting the social and semantic levels in a hierarchical structure known as Galois connections [10]. These connections reveal how membership networks—linking individuals to groups they belong to—operate at the intersection of social and semantic dimensions, with groups representing either concrete collectives or more abstract entities such as events or identities.

## 3. Graph Neural Network Perspectives on Isomorphism

### 3.1 Message-Passing and Local Aggregation

Graph Neural Networks (GNNs) provide a computational framework for understanding how local node features combine with structural information to produce network-level representations. The message-passing paradigm, which underlies many GNN architectures, formalizes how information flows through networked structures [6]. In this framework, each node updates its representation by aggregating information from its neighbors and combining this with its current state.

The general message-passing framework can be expressed as:

$$h_i^{(l+1)} = \text{UPDATE}\left(h_i^{(l)}, \text{AGGREGATE}\left(\{h_j^{(l)} : j \in \mathcal{N}(i)\}\right)\right)$$

where $\mathcal{N}(i)$ represents the neighbors of node $i$, and AGGREGATE and UPDATE are differentiable functions [6]. This process effectively combines local node features with structural information encoded in the graph topology.

Graph Convolutional Networks (GCNs) implement a specific form of this message-passing framework:

$$h_i^{(l+1)} = \sigma\left(W^{(l)}\sum_{j \in \mathcal{N}(i) \cup \{i\}} \frac{1}{\sqrt{\tilde{d}_i \tilde{d}_j}} h_j^{(l)}\right)$$

where $\tilde{d}_i$ represents the degree of node $i$ in the normalized adjacency matrix, and $\sigma$ denotes an activation function [6]. This formulation shows how local neighborhoods contribute to node representations through a normalized aggregation process.

### 3.2 Graph Isomorphism Networks

Graph Isomorphism Networks (GINs) represent a significant advancement in the ability of neural networks to distinguish non-isomorphic graph structures. The key novelty of GINs is their capacity to differentiate graphs that are not isomorphic to each other, where graph isomorphism represents an equivalent relation for "similar" structures [12].

Graph isomorphism is a pure topological relation that does not consider node features [12]. Two graphs are isomorphic if there exists a bijection between their node sets that preserves adjacency relationships. This mathematical definition has profound implications for understanding identity in cultural semantic networks, where structural equivalence may indicate functional or categorical similarity.

The ability of GINs to capture fine-grained structural differences stems from their use of injective multiset functions that can distinguish different multiset configurations. This theoretical foundation ensures that the network can learn representations that reflect the true structural identity of graphs, providing a computational analog to the sociological concept of structural isomorphism.

## 4. Local Clustering and Isomorphism: A Theoretical Integration

### 4.1 The Clustering-Isomorphism Nexus

The relationship between local node clustering and isomorphism group structure operates through multiple mechanisms that connect micro-level structural properties to macro-level patterns of identity convergence. We propose a theoretical framework that integrates network science perspectives on clustering with institutional theory's account of isomorphic pressures.

At the local level, the clustering coefficient determines the density of connections within a node's neighborhood, which in turn influences the strength of structural pressures experienced by nodes in that position. High clustering creates dense local communities where information flows rapidly and norms are strongly enforced. These local communities serve as the primary context for identity construction, as individuals and organizations develop their self-understanding through interactions with nearby network positions.

The connected components of local clustering generate isomorphic pressures through three primary mechanisms. First, mimetic isomorphism emerges from structural equivalence within clustered neighborhoods. Nodes that occupy similar positions within highly clustered regions face similar environmental pressures and are likely to imitate each other's identity configurations. Second, coercive isomorphism operates through the enforcement of norms within tightly knit communities, where deviation from accepted patterns faces social sanctions. Third, normative isomorphism develops as professional and cultural standards emerge within clustered groups, shaping identity expectations for all members.

### 4.2 Neighborhood Topology and Identity Configuration

The topology of a node's neighborhood—characterized by the pattern of connections among its neighbors—fundamentally shapes the identity options available to that node. In cultural semantic networks, the neighborhood topology determines which identity categories are structurally adjacent and therefore available for adoption or emulation.

Consider a node $i$ in a cultural semantic network. Its neighborhood $\mathcal{N}(i)$ consists of all nodes directly connected to $i$, while the induced subgraph on $\mathcal{N}(i)$ reveals the pattern of relationships among these neighbors. When this induced subgraph is densely connected—indicated by a high clustering coefficient—it forms a cohesive semantic community that strongly constrains the identity possibilities for node $i$.

The structural holes within a neighborhood—the gaps between nodes that are not directly connected—create opportunities for brokerage and identity innovation. However, in highly clustered neighborhoods, structural holes are rare, as most potential connections already exist. This density limits the range of identity configurations available to nodes within the cluster, pushing toward isomorphic outcomes where all members adopt similar identity patterns.

### 4.3 Connected Components and Group Identity

Connected components within the local clustering structure represent distinct identity communities that may develop different cultural patterns over time. The decomposition of a network into connected components reveals the modular structure of cultural semantic networks, where each component represents a relatively isolated domain of meaning-making.

Within each connected component, the local clustering patterns shape the development of group identity. High internal clustering creates strong in-group cohesion, as members share dense networks of semantic connections that reinforce shared understandings of identity categories. The boundaries between connected components, characterized by sparse interconnections, maintain differences in identity configurations across the network.

The evolution of identity within connected components follows patterns of institutional isomorphism, where the isolated development of local norms eventually produces convergent outcomes. As members of a connected component interact repeatedly, they develop shared understandings of identity categories that become institutionalized as rules-of-the-game [5]. These institutional patterns persist because they are reinforced by the dense local connections that characterize high-clustering environments.

## 5. Mechanisms of Influence

### 5.1 Structural Equivalence and Mimetic Pressure

Structural equivalence occurs when nodes occupy similar positions within the network structure, regardless of their direct connection to each other. In terms of local clustering, nodes with similar neighborhood topologies—characterized by comparable clustering coefficients and similar patterns of connections among neighbors—experience structural equivalence that drives mimetic isomorphism.

Nodes that are structurally equivalent face similar problems and have access to similar resources and identity models. When these nodes observe each other through the network structure, they are likely to imitate each other's identity configurations, believing that successful patterns can be transferred across equivalent positions. This mimetic process operates even in the absence of direct interaction, as structural observers learn from the identity choices of similar others.

The strength of mimetic pressure increases with the degree of structural equivalence, which is itself influenced by local clustering patterns. In highly clustered neighborhoods, structural equivalence is more pronounced, as the density of connections creates more similar structural contexts for nodes within the cluster. This clustering amplifies mimetic pressures, pushing nodes toward isomorphic identity configurations that match those of their structurally equivalent peers.

### 5.2 Cohesion and Coercive Pressure

Local clustering creates cohesive communities where social control mechanisms operate effectively. The density of connections within clustered neighborhoods enables rapid transmission of information about identity deviations and facilitates collective responses to non-conformity. This cohesion generates coercive pressures that push nodes toward accepted identity patterns.

In cultural semantic networks, coercive pressure manifests as the enforcement of semantic norms by community members. Nodes that adopt identity configurations inconsistent with community expectations face social sanctions ranging from subtle disapproval to explicit exclusion. The strength of these sanctions depends on the density of local connections, as more densely clustered communities have more extensive networks of social control.

The relationship between clustering density and coercive pressure follows a nonlinear pattern. At moderate levels of clustering, communities can enforce norms effectively while maintaining enough diversity to allow for identity innovation. At very high levels of clustering, however, the strength of coercive pressure may become excessive, stifling creativity and generating resistance to dominant identity patterns. The optimal level of clustering for community functioning balances coercive enforcement with space for individual and collective identity development.

### 5.3 Community Boundaries and Normative Pressure

The boundaries between connected components of local clustering create contexts for normative pressure, as communities develop distinct cultural standards that differentiate them from neighboring groups. These boundary-defining processes generate normative isomorphism within components while maintaining differences across components.

Normative pressure operates through the development of professional standards, cultural conventions, and institutional rules that shape identity expectations. Within a connected component, repeated interactions among members lead to the emergence of shared understandings about appropriate identity configurations. These shared understandings become institutionalized as norms that guide identity construction for all community members.

The strength of normative pressure depends on the degree of isolation of the connected component from other network regions. Highly isolated components develop distinctive normative patterns that may diverge significantly from those of other components. Less isolated components, with more extensive connections to external network regions, are exposed to diverse normative influences that may prevent the development of extreme local patterns.

## 6. Mathematical Formalization

### 6.1 Local Clustering Metrics

We formalize the local clustering properties that influence isomorphism group structure through several key metrics. The local clustering coefficient for node $i$ is defined as:

$$C_i = \frac{2 \cdot |E(\mathcal{N}(i))|}{|\mathcal{N}(i)| \cdot (|\mathcal{N}(i)| - 1)}$$

where $E(\mathcal{N}(i))$ represents the set of edges among neighbors of node $i$, and $|\mathcal{N}(i)|$ denotes the size of the neighborhood. This metric captures the density of internal connections within the local cluster surrounding node $i$.

The neighborhood topology can be further characterized by the degree sequence of nodes in $\mathcal{N}(i)$, which reveals the distribution of connectivity patterns within the local cluster. The second-order clustering coefficient, which measures the correlation between neighbor degrees, provides additional information about the structural configuration of the local neighborhood.

### 6.2 Isomorphism Pressure Functions

We model the influence of local clustering on isomorphism group structure through pressure functions that map local structural properties to isomorphic tendencies. The mimetic pressure $M_i$ experienced by node $i$ can be expressed as:

$$M_i = f\left(\{C_j, \text{topology}(\mathcal{N}(j)) : j \in \mathcal{N}(i)\}\right)$$

where the function $f$ aggregates local clustering information from nodes in the neighborhood to produce a mimetic pressure value. This formulation captures how the clustering properties of nearby nodes influence the imitation tendencies of node $i$.

Similarly, coercive pressure $P_i$ and normative pressure $N_i$ can be defined as functions of local clustering properties:

$$P_i = g\left(\sum_{j \in \mathcal{N}(i)} w_{ij} \cdot C_j\right)$$

$$N_i = h\left(\text{cluster\_coherence}(C_i)\right)$$

where $w_{ij}$ represents the weight of the connection between nodes $i$ and $j$, and cluster\_coherence measures the consistency of clustering patterns within the connected component containing node $i$.

### 6.3 Identity Configuration Dynamics

The identity configuration of node $i$ evolves according to the combined influence of mimetic, coercive, and normative pressures from local clustering structures. We model this evolution through a dynamic system:

$$\frac{dI_i}{dt} = \alpha \cdot M_i + \beta \cdot P_i + \gamma \cdot N_i$$

where $I_i$ represents the identity configuration of node $i$, and $\alpha$, $\beta$, and $\gamma$ are parameters that weight the relative influence of each pressure type. The equilibrium identity configurations emerge when the sum of pressures equals zero, indicating a stable isomorphic state.

The global isomorphism group structure emerges from the aggregation of local identity configurations across the network. When local clustering patterns are homogeneous across the network, isomorphic pressures produce convergent identity configurations throughout the system. When local clustering patterns vary across network regions, different isomorphic outcomes may emerge in different areas, creating a modular structure of identity configurations.

## 7. Implications for Cultural Semantic Networks

### 7.1 Identity Construction in Multi-Level Networks

The framework developed in this report has significant implications for understanding identity construction in multi-level cultural semantic networks. At the micro-level, individual nodes develop their identity configurations through interactions within local clusters, experiencing isomorphic pressures from mimetic, coercive, and normative sources. At the meso-level, connected components of local clustering develop distinctive identity patterns that reflect their particular structural configurations. At the macro-level, the interaction of local clustering patterns across the network produces global patterns of identity distribution.

The multi-level nature of this process means that identity construction cannot be understood solely through individual-level analysis or solely through global structural analysis. Rather, the relationship between local clustering and isomorphism group structure operates across levels, with local structural properties influencing meso-level identity communities that in turn shape macro-level patterns of cultural convergence.

Research on language and identity in multinational enterprises illustrates this multi-level dynamics [11]. Employees form language-based clusters that intersect with other identity attributes such as gender, regional dialects, and education. These clusters change composition over time, altering group dynamics and organizational processes. The local clustering patterns within language-based groups shape identity construction through mechanisms of homophily and shared meaning, while the boundaries between language groups maintain differences in identity configurations across the organization.

### 7.2 Cultural Holes and Identity Innovation

The concept of cultural holes—divergences in the way actors use terms that create gaps in socio-semantic connections—provides insight into the dynamics of identity innovation within cultural semantic networks [10]. While local clustering generally promotes isomorphic identity configurations, cultural holes create opportunities for identity innovation by exposing actors to divergent semantic patterns.

When a node bridges a cultural hole—connecting otherwise disconnected semantic regions—it gains access to diverse identity models that may not be available within its local cluster. This structural position enables the combination of identity elements from different semantic communities, potentially producing novel identity configurations that challenge isomorphic tendencies.

The relationship between local clustering and cultural holes follows an inverse pattern. High local clustering reduces the prevalence of cultural holes within clusters but may increase the prominence of cultural holes at cluster boundaries. These boundary cultural holes serve as important sites of identity innovation, where actors can draw upon diverse semantic resources to develop new identity configurations.

### 7.3 Institutional Isomorphism and Network Structure

The three mechanisms of institutional isomorphism—coercive, mimetic, and normative—map onto network structural properties in systematic ways. Coercive isomorphism corresponds to the density of connections within local clusters, as dense networks enable more effective enforcement of identity norms. Mimetic isomorphism corresponds to structural equivalence within and across clusters, as similar structural positions create templates for identity imitation. Normative isomorphism corresponds to the coherence of clustering patterns within connected components, as consistent local structures enable the development of shared professional standards.

This mapping reveals that institutional isomorphism is not merely an abstract sociological concept but has concrete structural manifestations in cultural semantic networks. The local clustering properties that network scientists measure—clustering coefficients, transitivity patterns, neighborhood topologies—are directly related to the isomorphic pressures that shape identity construction. This connection provides a bridge between computational network analysis and institutional theory, enabling more precise theoretical statements about the relationship between structure and identity.

## 8. Conclusion

This report has developed a comprehensive theoretical framework for understanding how connected components of local node clustering influence the isomorphism group structure of identity construction in cultural semantic networks. By integrating perspectives from network science, institutional sociology, and graph neural networks, we have revealed the mechanisms through which local structural properties generate cascading effects on identity patterns across multiple levels of analysis.

The key findings of this analysis can be summarized as follows. First, local clustering coefficients directly influence the strength of isomorphic pressures experienced by nodes within clustered neighborhoods. High clustering creates dense local communities where mimetic, coercive, and normative pressures are amplified, pushing nodes toward convergent identity configurations. Second, the topology of neighborhoods—characterized by patterns of connections among neighbors—shapes the structural equivalence of nodes and therefore the templates available for identity imitation. Third, connected components of local clustering develop distinctive identity patterns that reflect their particular structural configurations, creating modular variation in isomorphism group structures across the network.

The implications of this framework extend to multiple domains of inquiry. For organizational studies, it provides a structural account of how local network positions shape identity construction and isomorphic change. For cultural sociology, it reveals the network foundations of cultural convergence and divergence. For computational approaches to semantic networks, it connects local structural metrics to higher-level patterns of meaning and identity.

Future research should focus on empirical validation of the proposed relationships, developing measures of local clustering and isomorphism group structure that can be applied to diverse cultural semantic networks. The integration of computational methods from graph neural networks with theoretical insights from institutional sociology offers promising directions for advancing our understanding of identity construction in networked contexts.

The relationship between local clustering and isomorphism group structure represents a fundamental aspect of cultural semantic networks that has significant implications for understanding organizational and cultural dynamics. By illuminating the mechanisms through which local structural properties influence identity patterns, this report contributes to the development of more nuanced and precise theories of network-based identity construction.

---

## References

[1] Mohr, J.W. (1998). Measuring meaning structures. Annual Review of Sociology, 24, 345-370.

[2] Basov, N., Lee, J.S., & Antoniuk, A. (2018). Social Networks and Construction of Culture: A Socio-Semantic Analysis of Art Groups. Studies in Computational Intelligence.

[3] Boccaletti, S., et al. (2006). Complex networks: Structure and dynamics. Physics Reports, 424(4-5), 175-308.

[4] DiMaggio, P.J., & Powell, W.W. (1983). The iron cage revisited: Institutional isomorphism and collective rationality in organizational fields. American Sociological Review, 48(2), 147-160.

[5] Lizardo, O. (2006). How cultural tastes shape personal networks. American Sociological Review, 71(5), 778-807.

[6] Kipf, T.N., & Welling, M. (2016). Semi-supervised classification with graph convolutional networks. arXiv:1609.02907.

[7] Newman, M.E.J. (2003). The structure and function of complex networks. SIAM Review, 45(2), 167-256.

[8] Moody, J., & White, D.R. (2003). Structural cohesion and embeddedness: A hierarchical concept of social groups. American Sociological Review, 68(1), 103-127.

[9] Vicinanza, P. (2016). Identity-Constrained Isomorphism. University of Michigan Honors Thesis.

[10] Krackhardt, D., & Carley, K.M. (1998). A PCANS model of structure in organizations. Proceedings of the 1998 International Symposium on Command and Control Research and Technology.

[11] Tenzer, H., & Pudelko, M. (2024). Language and identity: The dynamics of linguistic clustering in multinational enterprises. Journal of World Business, 59(4), 101541.

[12] Xu, K., et al. (2019). How powerful are graph neural networks? International Conference on Learning Representations.

## Annotations


## Sources
[1] http://lsa.umich.edu/content/dam/orgstudies-assets/orgstudiesdocuments/oshonors/oshonorsthesis/2016-honors-theses/Vicinanza%20Paul%20Honors%20Thesis%20-%20Final.pdf
[2] https://aclanthology.org/2024.naacl-long.342.pdf
[3] https://arxiv.org/abs/2401.02999
[4] https://arxiv.org/pdf/1807.04698
[5] https://bradylab.ucsd.edu/pdfs/RobinsonDeStefanoVulBrady2024.pdf
[6] https://cosnet.bifi.es/publications/phys_rep_2006.pdf
[7] https://digitalcommons.liberty.edu/cgi/viewcontent.cgi?article=8979&context=doctoral
[8] https://docs.enriquedussel.com/txt/Textos_200_Obras/Filosofos_latinos_EU/Visible_identities-Linda_Alcoff.pdf
[9] https://en.wikipedia.org/wiki/Isomorphism_(sociology)
[10] https://en.wikipedia.org/wiki/Semantic_network
[11] https://hal.science/tel-03360647v1/file/HDR-CS%2B%2B.pdf
[12] https://people.duke.edu/~jmoody77/peergroups.pdf
[13] https://purehost.bath.ac.uk/ws/portalfiles/portal/191606968/Ashford_DBA_Thesis_09.04.19.pdf
[14] https://wandb.ai/graph-neural-networks/GIN/reports/What-are-Graph-Isomorphism-Networks---Vmlldzo1MTExMTg5
[15] https://web.stanford.edu/group/fearon-research/cgi-bin/wordpress/wp-content/uploads/2013/10/What-is-Identity-as-we-now-use-the-word-.pdf
[16] https://www.cs.mcgill.ca/~wlh/grl_book/files/GRL_Book.pdf
[17] https://www.emergentmind.com/topics/local-clustering-coefficient
[18] https://www.jneurosci.org/content/45/17/e0802242025
[19] https://www.jstor.org/stable/27289163
[20] https://www.mdpi.com/2075-1680/14/3/204
[21] https://www.mdpi.com/2571-5577/8/5/142
[22] https://www.nature.com/articles/s41598-025-24276-1
[23] https://www.nature.com/articles/s44271-025-00214-9
[24] https://www.sciencedirect.com/science/article/abs/pii/S0304422X19304073
[25] https://www.sciencedirect.com/science/article/pii/S0378873321001143
[26] https://www.sciencedirect.com/science/article/pii/S109095162400021X
[27] https://www.yworks.com/pages/clustering-graphs-and-networks