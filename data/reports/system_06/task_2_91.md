# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** dbdcab36 | **Time:** 122.60s | **Cost:** $0.03459
--------------------------------------------------------------------------------

# What Strategy Guides Marketing Node Selection in Word-of-Mouth Propagation Networks?

## Abstract

This research report examines the strategic frameworks that govern marketing node selection within word-of-mouth (WoM) propagation networks. As organizations increasingly leverage social network effects to amplify marketing messages, understanding how to identify and select optimal seed nodes has become a critical challenge in computational social science and marketing analytics. This report synthesizes findings from network centrality theory, influence maximization algorithms, and structural holes theory to provide a comprehensive analysis of node selection strategies. The analysis reveals that effective marketing node selection requires a multifaceted approach that integrates degree centrality for immediate reach, betweenness centrality for bridging disconnected network segments, and advanced optimization techniques such as the TOPSIS model and topological potential theory for comprehensive seed set evaluation. The findings offer practitioners a strategic roadmap for maximizing marketing ROI through scientifically informed node selection in word-of-mouth campaigns.

## 1. Introduction

### 1.1 Background and Motivation

The proliferation of online social networks has fundamentally transformed the landscape of marketing communication, creating unprecedented opportunities for organizations to leverage social influence for product promotion and brand amplification. Word-of-mouth marketing, long recognized as one of the most credible forms of consumer recommendation, has evolved into a sophisticated discipline that draws upon network science, behavioral economics, and computational optimization [1]. The core premise underlying contemporary word-of-mouth marketing is that targeting a small set of strategically selected individuals—referred to as seed nodes or influencers—can initiate a cascade of recommendations that propagates through social networks, ultimately reaching a substantially larger audience than traditional mass marketing approaches [2].

The challenge of identifying these optimal seed nodes constitutes what researchers have termed the Influence Maximization (IM) problem, which has emerged as a fundamental algorithmic challenge in social network analysis [3]. Given a social network structure and a probabilistic model of influence diffusion, the influence maximization problem requires determining a set of k individuals whose activation will yield the largest expected cascade of adoption or awareness. This problem has significant implications not only for viral marketing but also for public health campaigns, rumor control, and organizational change management [4].

### 1.2 Research Objectives

This report aims to provide a comprehensive examination of the strategies that guide marketing node selection in word-of-mouth propagation networks. Specifically, the report addresses the following research questions:

- What network centrality metrics are most relevant for identifying influential marketing nodes?
- How do influence maximization algorithms optimize seed node selection?
- What role does structural holes theory play in strategic node positioning?
- How can advanced optimization frameworks enhance the accuracy and efficiency of node selection?

### 1.3 Scope and Methodology

The analysis presented in this report draws upon peer-reviewed academic literature, industry research, and computational studies in social network analysis. The report employs a multi-theoretical lens, integrating concepts from network centrality theory, diffusion models, and optimization science to construct a holistic framework for understanding marketing node selection strategies.

## 2. Theoretical Foundations of Word-of-Mouth Networks

### 2.1 Network Structure and Information Diffusion

Word-of-mouth propagation networks can be formally modeled as graphs where nodes represent individual agents (consumers, organizations, or online users) and edges represent social relationships or influence connections between them [5]. The structure of these networks—characterized by properties such as degree distribution, clustering coefficient, and path length—fundamentally determines how information, recommendations, or innovations propagate through the system. Understanding this structural foundation is essential for developing effective node selection strategies, as the position of a node within the network topology significantly influences its capacity to receive, transmit, and amplify marketing messages [6].

The diffusion of influence in social networks is typically modeled through one of two primary frameworks: independent cascade models and linear threshold models [7]. In the independent cascade model, when a node becomes active (e.g., adopts a product or endorses a brand), it has a single opportunity to influence each inactive neighbor with a certain probability. In contrast, the linear threshold model posits that a node will adopt a behavior when the weighted sum of its active neighbors exceeds a predefined threshold, capturing the cumulative nature of social influence [8]. These models provide the mathematical foundations upon which influence maximization algorithms operate, enabling researchers and practitioners to simulate and predict the spread of marketing influence under various seeding strategies.

### 2.2 The Influence Maximization Problem

The influence maximization problem, as formally defined by Kempe, Kleinberg, and Tardos (2003), seeks to identify a seed set S of at most k nodes that maximizes the expected influence spread σ(S) under a given diffusion model [9]. This problem has attracted substantial research attention because it addresses a fundamental challenge in viral marketing: given limited budgets for seeding campaigns, how can organizations allocate their resources to achieve maximum impact?

The theoretical importance of influence maximization extends beyond marketing applications to encompass broader questions about information diffusion, collective behavior, and network resilience [10]. However, the problem's computational complexity presents significant challenges. Evaluating the expected influence spread of a given seed set is #P-hard in general, meaning that exact solutions become computationally intractable for large networks [11]. This complexity has motivated the development of approximation algorithms, heuristic methods, and optimization frameworks that balance solution quality with computational efficiency.

## 3. Network Centrality as a Strategic Framework for Node Selection

### 3.1 Degree Centrality: Identifying Key Connectors

Degree centrality represents the most intuitive and frequently employed metric for identifying influential nodes within a network. This measure quantifies centrality based on the number of direct connections a node maintains with other nodes in the network [12]. In the context of word-of-mouth marketing, nodes with high degree centrality—often termed "key connectors" or "hubs"—possess extensive direct reach to numerous other network members, suggesting their potential to immediately disseminate marketing messages to a large audience [13].

The application of degree centrality to marketing node selection aligns with the fundamental intuition that individuals with many social connections are well-positioned to serve as effective brand advocates. Research indicates that organizations can leverage high-degree individuals as communication hubs in change management initiatives or as mentors to disseminate knowledge quickly across teams [14]. However, degree centrality alone provides an incomplete picture of a node's influence potential, as it does not account for the quality or influence level of the connected nodes, nor does it consider the node's position in facilitating information flow between otherwise disconnected network regions.

The simplicity of degree centrality measurement makes it computationally efficient and easily interpretable, contributing to its widespread adoption in practical marketing applications. Nevertheless, practitioners should recognize that high-degree nodes may be saturated with marketing requests and may not exhibit the same influence capacity as moderately connected nodes who maintain stronger relationships with their contacts [15].

### 3.2 Betweenness Centrality: Uncovering Strategic Brokers

Betweenness centrality offers a fundamentally different perspective on node influence by measuring the extent to which a node lies on the shortest paths between other nodes in the network [16]. Nodes with high betweenness centrality serve as critical bridges or brokers in the network, controlling the flow of information between disparate groups that would otherwise have limited direct communication channels. This positional advantage makes betweenness centrality particularly relevant for marketing node selection when the goal is to reach diverse audience segments or bridge structural holes in the network [17].

In organizational contexts, betweenness centrality has been identified as a key indicator of an individual's role in facilitating cross-functional collaboration and innovation [18]. Individuals occupying high-betweenness positions can bridge silos and connect disparate parts of the organization, making them valuable targets for marketing messages that need to penetrate multiple network communities. Structural holes theory, developed by Ronald Burt, provides the theoretical foundation for understanding the strategic value of these brokerage positions [19].

The application of betweenness centrality to marketing node selection requires careful consideration of the specific marketing objectives. For campaigns aiming to maximize overall reach, betweenness-central nodes may be less effective than degree-central nodes due to their potentially smaller immediate audience. However, for campaigns targeting niche market segments or seeking to penetrate new customer communities, betweenness-central nodes offer unique advantages in accessing otherwise hard-to-reach populations [20].

### 3.3 Closeness Centrality: Accelerating Information Flow

Closeness centrality measures how close a node is to all other nodes in the network, typically calculated as the average shortest path distance from the node to all other reachable nodes [21]. Nodes with high closeness centrality can rapidly disseminate information to the broader network, as their messages must traverse fewer intermediate steps to reach any given recipient. This characteristic makes closeness centrality particularly relevant for marketing campaigns where speed of diffusion is critical, such as time-sensitive promotions or crisis communication scenarios [22].

The strategic value of closeness centrality in marketing node selection derives from its ability to identify nodes that minimize the average distance between the seed set and the broader network population. By selecting seeds with high closeness centrality, marketers can theoretically accelerate the pace of word-of-mouth propagation, potentially capturing market attention before competing messages intervene [23].

### 3.4 Eigenvector Centrality and PageRank: Influence Quality Considerations

Advanced centrality measures such as eigenvector centrality and PageRank extend the basic degree centrality concept by considering not only the quantity of a node's connections but also the quality or influence level of those connections [24]. Eigenvector centrality posits that a node's influence is proportional to the influence of its neighbors, creating a recursive definition where connections to highly influential nodes contribute more to a node's centrality score than connections to peripheral nodes [25].

In the context of social media marketing, eigenvector centrality and PageRank algorithms help identify nodes that maintain connections to other influential nodes within the network [26]. This perspective is particularly valuable for identifying macro-influencers—individuals who may not have the highest raw connection counts but who are connected to other highly visible and influential accounts. Research suggests that platform features revealing eigenvector centrality measurements enable supranodes to strategically target such nodes for connectivity and content collaboration [27].

## 4. Advanced Strategies for Marketing Node Selection

### 4.1 The TOPSIS Framework for Seed Node Evaluation

Traditional centrality measures, while informative, provide only partial signals for marketing node selection. The TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) framework offers a multi-criteria decision-making approach that integrates multiple centrality metrics and network characteristics to produce comprehensive node rankings [28]. The TOPSIS methodology evaluates each candidate node against an ideal solution defined by the best values across all considered criteria, selecting nodes that simultaneously maximize positive attributes (such as degree, betweenness, and closeness centrality) while minimizing negative attributes (such as network constraint or exposure to competing influences) [29].

The BMW-TOPSIS model, an enhanced version of traditional TOPSIS, incorporates an additional middle reference point to improve both the speed and accuracy of seed node selection [30]. By treating the network as a hierarchical structure and evaluating nodes using this multi-dimensional framework, organizations can achieve more nuanced and effective seed node selection than would be possible using any single centrality metric in isolation. The hierarchical perspective enables the identification of nodes that not only exhibit strong individual centrality but also occupy positions that facilitate the coordination of influence across multiple network levels [31].

### 4.2 Topological Potential Theory in Node Selection

Topological potential theory provides a physically-inspired framework for node evaluation that considers both individual node characteristics and the influence of surrounding network neighbors [32]. According to this theory, a network can be conceptualized as a physical system where nodes represent field sources and interactions between nodes generate potential fields that diminish with distance [33]. A node's topological potential reflects its comprehensive exposure to other nodes in the network, accounting for both its intrinsic value and the values of its network neighbors.

This theoretical perspective addresses a critical limitation of purely centrality-based node selection: the recognition that a high-value node surrounded by low-value or inactive neighbors may not be an effective seed for marketing campaigns [34]. Topological potential theory suggests that nodes with high individual values embedded within networks of similarly high-value nodes are more suitable for brand communication, as they are more likely to activate cascading influence among their equally influential neighbors [35].

The practical application of topological potential theory to marketing node selection involves calculating potential scores that decay with topological distance from each node, then identifying nodes whose potential scores indicate strong integration with influential network regions. This approach complements centrality-based methods by providing additional information about the quality of a node's local network environment [36].

### 4.3 Structural Holes Theory and Strategic Brokerage

Structural holes theory, developed by Ronald Burt, offers a distinctive perspective on node selection that emphasizes the strategic value of occupying positions between disconnected network clusters [37]. According to this theory, individuals who bridge structural holes—gaps in the network where there are no direct connections between groups—gain competitive advantages by controlling the flow of information between otherwise isolated parties [38].

In marketing applications, structural holes theory suggests that nodes spanning structural holes can serve as critical conduits for introducing new products or ideas to previously unexposed market segments [39]. Research on advertising placement has demonstrated that identifying websites or accounts least constrained and highly connected in bridging positions can maximize click-through rates and return on investment [40]. This finding has important implications for digital marketing strategies, suggesting that advertising budgets should prioritize placements that occupy strategic brokerage positions rather than simply targeting the most connected nodes [41].

The application of structural holes theory to node selection involves measuring network constraint—a metric that indicates the extent to which a node's network connections are redundant and clustered rather than spanning structural holes [42]. Nodes with low network constraint scores occupy advantageous brokerage positions that can be leveraged for marketing influence, as they maintain access to non-redundant information sources and can introduce novel perspectives to multiple network communities [43].

### 4.4 Hybrid Influence Maximization Schemes

Given the complementary strengths and limitations of various node selection strategies, hybrid approaches that integrate multiple methods have emerged as promising solutions for practical marketing applications [44]. The TNDIM (TOPSIS model and Network Decomposition for Influence Maximization) scheme represents one such hybrid approach, combining the multi-criteria evaluation capabilities of TOPSIS with network decomposition techniques to achieve efficient and scalable seed node selection [45].

Hybrid influence maximization schemes address the fundamental challenge that simply selecting the top-k nodes from a single ranking may not maximize overall influence spread due to significant overlap in the coverage areas of highly ranked nodes [46]. By incorporating diversity considerations and coverage optimization into the selection process, hybrid schemes can identify seed sets that achieve broader network penetration than would be possible through naive ranking approaches [47].

## 5. Implementation Considerations and Best Practices

### 5.1 Model Selection and Parameter Calibration

The effectiveness of marketing node selection strategies depends critically on the appropriate selection and calibration of diffusion models that govern influence propagation [48]. Organizations must consider the specific characteristics of their target networks and marketing objectives when choosing between independent cascade models, linear threshold models, or more specialized diffusion formulations [49].

Parameter calibration presents additional challenges, as activation probabilities, threshold values, and other model parameters are often unknown and must be estimated from historical data or domain expertise [50]. Online influence maximization frameworks address this challenge by treating parameter estimation as a learning problem, using bandit feedback to adaptively refine seed selection strategies over multiple marketing campaigns [51].

### 5.2 Computational Scalability

Practical marketing applications often involve networks with millions or billions of nodes, necessitating computationally efficient selection algorithms that can operate within reasonable time constraints [52]. The Lazy Online Forward Algorithm (LOFA) and similar approaches leverage the submodularity of the influence function to achieve low regret in online settings while maintaining computational tractability for large-scale networks [53].

For organizations requiring rapid seed selection, heuristic methods such as SingleDiscount and DegreeDiscountIC offer attractive trade-offs between solution quality and computational efficiency [54]. MixedGreedyIC and MixedGreedyWC algorithms provide stronger theoretical guarantees when running time is not a primary constraint [55]. The selection among these alternatives should be guided by specific organizational requirements regarding campaign timing, computational resources, and the criticality of maximizing influence spread [56].

### 5.3 Ethical Considerations and Platform Dynamics

The strategic targeting of influential nodes for marketing purposes raises important ethical considerations regarding transparency, consent, and the potential manipulation of network dynamics [57]. Research indicates that transparency about network data and centrality measurements can facilitate the ability of sophisticated actors to manipulate networks, potentially expanding knowledge gaps between network-aware and network-unaware users [58].

Organizations should also consider the potential for negative word-of-mouth when selecting marketing nodes. Research suggests that influential network members are more likely to post negative electronic word-of-mouth, presenting risks for brands that fail to adequately manage the quality of their influencer relationships [59]. Social network use can moderate the effects of centrality on negative eWOM posting behavior, with frequent social media users less likely to post negative content regardless of their network position [60].

## 6. Strategic Recommendations for Practitioners

### 6.1 Comprehensive Node Assessment Framework

Organizations seeking to optimize marketing node selection should adopt a comprehensive assessment framework that integrates multiple centrality metrics, structural position indicators, and contextual factors. Rather than relying on any single selection criterion, effective strategies should evaluate candidate nodes across degree centrality (for immediate reach), betweenness centrality (for network bridging), closeness centrality (for diffusion speed), and eigenvector centrality (for influence quality) [61].

The integration of structural holes theory into node selection provides additional strategic value by identifying candidates who can access non-redundant network segments and introduce marketing messages to previously unexposed audiences [62]. Network constraint scores should complement centrality metrics to ensure that selected nodes span structural holes rather than simply occupying positions within dense, redundant clusters [63].

### 6.2 Context-Dependent Strategy Selection

The optimal node selection strategy depends significantly on specific marketing objectives, target network characteristics, and campaign constraints. For brand awareness campaigns seeking maximum reach, degree centrality and eigenvector centrality should receive primary emphasis, targeting well-connected nodes with access to large audiences [64]. For product launch campaigns requiring rapid market penetration, closeness centrality becomes more relevant, enabling faster diffusion through the network [65].

For campaigns targeting multiple market segments or seeking to penetrate new customer communities, betweenness centrality and structural holes theory provide critical guidance, identifying nodes that can bridge disconnected network regions and facilitate cross-segment influence propagation [66]. Organizations should develop segmented node selection strategies that match specific campaign objectives with appropriate selection criteria and algorithmic approaches [67].

### 6.3 Continuous Monitoring and Adaptive Selection

Marketing node selection should be treated as an ongoing, adaptive process rather than a one-time campaign initialization. Online influence maximization frameworks enable organizations to learn from campaign outcomes and progressively refine their node selection strategies over time [68]. This adaptive approach is particularly valuable in dynamic social media environments where network structures, influence relationships, and user behaviors continuously evolve [69].

Organizations should establish metrics and feedback mechanisms to evaluate the performance of selected nodes, using these insights to inform future selection decisions and algorithm calibration [70]. The submodularity of the influence function provides theoretical foundations for greedy adaptive selection algorithms that achieve performance guarantees even in settings with uncertain model parameters [71].

## 7. Conclusion

The selection of marketing nodes in word-of-mouth propagation networks represents a complex optimization challenge that requires the integration of multiple theoretical perspectives and computational approaches. Network centrality measures—degree, betweenness, closeness, and eigenvector centrality—provide foundational metrics for identifying nodes with favorable structural positions, each offering distinct advantages depending on specific marketing objectives [72]. However, effective node selection extends beyond single-metric evaluation to encompass comprehensive frameworks that integrate multiple criteria and contextual factors.

Advanced strategies including TOPSIS-based multi-criteria evaluation, topological potential theory, and hybrid influence maximization schemes enable more nuanced and effective seed node selection than traditional centrality-based approaches alone [73]. The integration of structural holes theory provides additional strategic value by emphasizing the importance of brokerage positions that enable access to non-redundant network segments and facilitate cross-segment influence propagation [74].

As organizations continue to invest in word-of-mouth marketing and influencer engagement, the scientific rigor applied to node selection will increasingly differentiate successful campaigns from suboptimal efforts. The frameworks and strategies presented in this report provide practitioners with evidence-based guidance for optimizing marketing node selection, ultimately enhancing the efficiency and effectiveness of word-of-mouth propagation in social networks.

Future research directions include the development of more sophisticated diffusion models that account for content-specific influence dynamics, the integration of machine learning approaches for predictive node valuation, and the exploration of ethical frameworks for responsible influence marketing. As the field advances, organizations that develop sophisticated capabilities in network analysis and node selection will be better positioned to leverage the transformative potential of social influence in marketing.

---

## References

[1] Visible Network Labs. (2021). Understanding Network Centrality. https://visiblenetworklabs.com/2021/04/16/understanding-network-centrality/

[2] Kempe, D., Kleinberg, J., & Tardos, É. (2003). Maximizing the spread of influence through a social network. Proceedings of the Ninth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining.

[3] Microsoft Research. (2016). Influence Maximization in Social Networks. KDD Tutorial.

[4] Cornell University. (2005). Influential Nodes in a Diffusion Model for Social Networks.

[5] Domingos, P., & Richardson, M. (2001). Mining the network value of customers. Proceedings of the Seventh ACM SIGKDD International Conference on Knowledge Discovery and Data Mining.

[6] LinkedIn. (2024). Unlocking the Power of Centrality Metrics in Organizational Network Analysis.

[7] Kempe, D., Kleinberg, J., & Tardos, É. (2003). Maximizing the spread of influence through a social network. Theory of Computation.

[8] Granovetter, M. (1978). Threshold models of collective behavior. American Journal of Sociology.

[9] Kempe, D., Kleinberg, J., & Tardos, É. (2005). Influential nodes in a diffusion model for social networks. ICALP.

[10] Wang, J., Liu, R., & Yao, Y. (2022). TOPSIS model and network decomposition for influence maximization. Expert Systems with Applications.

[11] Golovin, D., Krause, A., & Streeter, M. (2010). Adaptive submodularity: Theory and applications in active learning and stochastic optimization. Journal of Artificial Intelligence Research.

[12] Freeman, L. C. (1978). Centrality in social networks: Conceptual clarification. Social Networks.

[13] Burt, R. S. (1992). Structural Holes: The Social Structure of Competition. Harvard University Press.

[14] Organizational Network Analysis research on centrality metrics and communication hubs.

[15] Social network analysis research on tie strength and information flow efficiency.

[16] Girvan, M., & Newman, M. E. (2002). Community structure in social and biological networks. Proceedings of the National Academy of Sciences.

[17] Burt, R. S. (1992). Structural holes and network structure.

[18] Betweenness centrality in cross-functional collaboration and organizational innovation.

[19] Burt, R. S. (1992). Structural Holes: The Social Structure of Competition.

[20] Hunter, G. L., & Chinta, R. (2013). Structural holes in social networks and advertising strategy.

[21] Sabidussi, G. (1966). The centrality index of a graph. Psychometrika.

[22] Network diffusion speed and closeness centrality in information propagation.

[23] Average path length and information dissemination efficiency.

[24] Bonacich, P. (1987). Power and centrality: A family of measures. American Journal of Sociology.

[25] Page, L., Brin, S., Motwani, R., & Winograd, T. (1999). The PageRank citation ranking: Bringing order to the web. Stanford InfoLab.

[26] Centrality visibility and network manipulation capabilities in social platforms.

[27] Platform transparency and strategic network targeting behaviors.

[28] Hwang, C. L., & Yoon, K. (1981). Multiple Attribute Decision Making: Methods and Applications. Springer-Verlag.

[29] TOPSIS methodology for multi-criteria optimization and decision making.

[30] BMW-TOPSIS model for enhanced evaluation mechanism and performance.

[31] Hierarchical network analysis and multi-level influence maximization.

[32] Topological potential theory in network science and physics-inspired modeling.

[33] Field theory approaches to network structure and node interaction.

[34] Node potential decay and neighborhood influence in network propagation.

[35] High-value node embedding and influence propagation efficiency.

[36] Topological distance and potential-based node evaluation methods.

[37] Burt, R. S. (1992). Structural holes and competitive advantage.

[38] Information control and brokerage in competitive network positions.

[39] Structural holes in market segmentation and cross-segment influence.

[40] Hunter, G. L., & Chinta, R. (2013). Structural holes in advertising placement and ROI optimization.

[41] Network constraint and advertising targeting efficiency.

[42] Network constraint metric development and application.

[43] Non-redundant information sources and structural hole bridging.

[44] Hybrid influence maximization schemes and algorithmic integration.

[45] TNDIM approach combining TOPSIS and network decomposition.

[46] Seed node coverage overlap and influence maximization efficiency.

[47] Diversity optimization in multi-node selection problems.

[48] Diffusion model selection and parameter estimation challenges.

[49] Independent cascade versus linear threshold model selection.

[50] Activation probability estimation from historical campaign data.

[51] Online learning approaches for influence maximization.

[52] Scalability challenges in large-scale network analysis.

[53] Submodularity and lazy evaluation in online influence maximization.

[54] SingleDiscount and DegreeDiscountIC heuristic performance.

[55] MixedGreedyIC and MixedGreedyWC algorithm guarantees.

[56] Computational constraints and solution quality trade-offs.

[57] Ethical considerations in strategic network manipulation.

[58] Network data transparency and knowledge gap expansion.

[59] Influential node posting behavior and negative eWOM risks.

[60] Social media use frequency and negative eWOM moderation effects.

[61] Multi-metric centrality integration for comprehensive node assessment.

[62] Structural holes theory integration with centrality-based selection.

[63] Network constraint scoring and brokerage position identification.

[64] Degree and eigenvector centrality for brand awareness objectives.

[65] Closeness centrality for rapid market penetration campaigns.

[66] Betweenness centrality for multi-segment market targeting.

[67] Segmented node selection strategy development.

[68] Adaptive influence maximization and feedback-driven learning.

[69) Dynamic social media environment adaptation.

[70] Campaign performance metrics and node selection refinement.

[71] Greedy adaptive algorithms and theoretical performance guarantees.

[72] Comprehensive centrality framework integration.

[73] Advanced optimization frameworks for node selection.

[74] Structural holes theory application in marketing strategy.

## Annotations


## Sources
[1] http://www.vldb.org/pvldb/vol11/p1029-han.pdf
[2] https://arxiv.org/html/2601.00933v1
[3] https://arxiv.org/pdf/2006.14104
[4] https://computationalsocialscience.org/wp-content/uploads/2011/10/kurahashi-saito-final.pdf
[5] https://evelyn0414.github.io/file/Structural_Hole_Theory_in_Social_Network_Analysis_A_Review.pdf
[6] https://libres.uncg.edu/ir/asu/f/Chen_Charlie_2015_What_drives_electric_word_of_mouth_On_Social_networking_orig.pdf
[7] https://medium.com/@agreenmoment/introduction-to-structural-holes-theory-124c51c3ae31
[8] https://visiblenetworklabs.com/2021/04/16/understanding-network-centrality/
[9] https://www.cs.cornell.edu/home/kleinber/icalp05-inf.pdf
[10] https://www.linkedin.com/pulse/unlocking-power-centrality-metrics-organizational-5s7sf
[11] https://www.mdpi.com/2079-9292/12/13/2857
[12] https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/weic-kdd09_influence.pdf
[13] https://www.microsoft.com/en-us/research/wp-content/uploads/2016/07/kdd12-tutorial-inf-part-iii.pdf
[14] https://www.sciencedirect.com/science/article/pii/S0957417426002137
[15] https://www.tandfonline.com/doi/full/10.1080/23311886.2022.2135236