# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 8b72ce8c | **Time:** 1660.48s | **Cost:** $0.20072
--------------------------------------------------------------------------------

# How Does the Spatiotemporal Distribution of OD Matrices Affect Capacity Allocation Under Different Density Gradients?

## Abstract

The relationship between origin-destination (OD) matrix distributions and transportation network capacity allocation represents a fundamental challenge in urban transportation planning. This report examines how the spatiotemporal characteristics of OD matrices interact with varying urban density gradients to influence capacity allocation decisions. Drawing from contemporary research in transportation network analysis, urban density modeling, and machine learning approaches to traffic prediction, this investigation reveals that OD matrix distributions exhibit complex, non-linear relationships with capacity allocation that are modulated by spatial density variations. The analysis demonstrates that density gradients fundamentally reshape both the magnitude and spatial distribution of travel demand, creating cascading effects on network capacity requirements. Key findings indicate that capacity allocation strategies must account for temporal heterogeneity in OD patterns, spatial non-stationarity in demand-supply relationships, and threshold effects that emerge at critical density levels. The integration of graph neural network approaches and spatiotemporal correlation modeling provides promising frameworks for capturing these intricate dynamics. This research contributes to the theoretical understanding of density-dependent capacity allocation and offers practical insights for transportation planners seeking to optimize network performance across diverse urban contexts.

## 1. Introduction

### 1.1 Background and Motivation

Transportation network capacity allocation constitutes one of the most consequential decisions in urban infrastructure planning, directly affecting mobility efficiency, economic productivity, and environmental sustainability. The complexity of this allocation problem stems fundamentally from the dynamic and heterogeneous nature of travel demand, which varies substantially across space, time, and urban density contexts. At the heart of understanding travel demand lies the origin-destination matrix, a fundamental construct that quantifies the volume of trips between all pairs of origins and destinations within a transportation network [1].

The four-step transportation planning process—encompassing trip generation, trip distribution, mode choice, and route choice—provides the traditional framework for analyzing travel demand patterns [1]. Within this framework, the OD matrix emerges from the distribution step, representing the aggregate result of individual travel decisions influenced by demographic factors, land use patterns, and transportation system characteristics. However, conventional approaches to OD matrix estimation and capacity allocation often treat these matrices as static entities, overlooking the rich spatiotemporal dynamics that characterize real-world urban mobility.

Contemporary research has increasingly recognized that OD matrices exhibit substantial temporal variation, with demand patterns shifting across time intervals ranging from hourly fluctuations during peak periods to longer-term variations spanning weeks, months, and seasonal cycles [2]. Similarly, the spatial distribution of OD flows demonstrates considerable heterogeneity, reflecting the underlying urban structure and density gradients that shape travel behavior. These observations motivate the central question of this report: how does the spatiotemporal distribution of OD matrices affect capacity allocation under different density gradients?

### 1.2 Research Objectives

This report pursues several interconnected objectives aimed at advancing the understanding of OD matrix dynamics and their implications for capacity allocation. First, it examines the theoretical foundations linking OD matrix characteristics to capacity allocation decisions, drawing from classical transportation network theory and contemporary advances in urban analytics. Second, it investigates how urban density gradients influence the spatial and temporal patterns of OD matrices, with particular attention to non-linear relationships and threshold effects. Third, it analyzes the methodological approaches developed for capturing spatiotemporal OD dynamics, including both traditional analytical techniques and emerging machine learning frameworks. Finally, it synthesizes these insights to identify key principles for density-responsive capacity allocation strategies.

### 1.3 Scope and Structure

The analysis presented herein focuses primarily on urban transportation contexts, where density gradients and spatiotemporal demand variations are most pronounced. The report is organized into seven subsequent sections. Section 2 reviews the theoretical foundations of OD matrix analysis and capacity allocation. Section 3 examines urban density modeling approaches and their implications for understanding demand patterns. Section 4 investigates the spatiotemporal dynamics of OD matrices. Section 5 analyzes capacity allocation under varying density conditions. Section 6 presents methodological approaches for integrated analysis. Section 7 offers conclusions and recommendations for practice and future research.

## 2. Theoretical Foundations of OD Matrix Analysis and Capacity Allocation

### 2.1 Fundamentals of OD Matrix Representation

The OD matrix represents a fundamental data structure in transportation analysis, encoding the volume of travel demand between all origin-destination pairs within a defined study area. Mathematically, an OD matrix $F$ of dimension $N \times N$ contains elements $F_{i,j}$ representing the number of trips originating from zone $i$ and terminating at zone $j$ during a specified time period [3]. This representation provides the essential input for traffic assignment procedures that distribute demand across the network infrastructure.

The estimation of OD matrices has traditionally relied on the four-step planning process, where trip generation produces total trip ends for each zone, trip distribution allocates these ends to destination zones based on impedance functions, and subsequent steps determine mode choice and route assignment [1]. However, this sequential approach has been increasingly supplemented by direct estimation techniques that leverage observed traffic counts, sensor data, and emerging data sources such as mobile phone records and smart card transactions [2].

Contemporary OD estimation methodologies recognize the inherent uncertainty in demand estimates and employ probabilistic frameworks to characterize this uncertainty. The work of Osorio and colleagues has developed metamodel formulations that efficiently approximate the mapping between travel demand and link performance, enabling tractable estimation even for large-scale networks [2]. These approaches incorporate prior or seed matrices—typically derived from census data or simpler static models—that capture plausible travel demand patterns for the calibration period. The scalar weight factors in these formulations define the trade-off between fitting observed data and maintaining consistency with prior information.

### 2.2 Capacity Allocation in Transportation Networks

Capacity allocation encompasses the decisions regarding how transportation infrastructure resources—road lanes, transit vehicles, signal timing, and other operational parameters—should be distributed across the network to serve travel demand effectively. The fundamental challenge arises from the potential mismatch between demand and supply, particularly during peak periods when demand may exceed available capacity [1].

Traffic assignment models provide the analytical framework for understanding how OD demand translates into link flows and capacity requirements. User equilibrium assignment, the most widely applied framework, assumes that travelers select routes to minimize their individual travel costs, resulting in a state where no traveler can reduce their cost by unilaterally changing routes. The classical Wardrop equilibrium principle states that routes used in equilibrium must have equal and minimum cost, while unused routes have higher cost [1].

The introduction of capacity constraints into traffic assignment creates significant analytical challenges. When demand for a link exceeds its capacity, the resulting congestion propagates upstream rather than affecting the constrained link itself [1]. This phenomenon, illustrated in Figure 1.7 of the source material, has profound implications for capacity allocation: improving a bottleneck link may not reduce congestion on upstream links, and capacity expansions may attract additional demand that partially or fully offsets the initial benefit.

### 2.3 Sensitivity Analysis Framework

Understanding how changes in OD matrices affect capacity allocation requires systematic sensitivity analysis. The sensitivity of link flows and travel costs to perturbations in OD demand provides essential information for both planning decisions and real-time operations. Changes to the OD matrix represent one of the primary sources of sensitivity in transportation network models [1].

The sensitivity of network performance metrics to OD variations can be characterized through derivative-based approaches that compute how link flows change with respect to OD demand. These sensitivities enable planners to identify critical OD pairs whose demand variations have disproportionate effects on network performance. Furthermore, sensitivity analysis supports the network design problem, where infrastructure investments are optimized to maximize network performance under demand uncertainty [1].

The relationship between OD changes and capacity requirements exhibits important structural properties. For small demand perturbations, linear approximations based on sensitivity derivatives provide accurate predictions of flow changes. However, for larger perturbations—particularly those that cause links to approach or exceed capacity—the non-linear nature of link performance functions becomes significant, and higher-order effects must be considered.

## 3. Urban Density Gradients and Their Modeling

### 3.1 Classical Density Functions

Urban density—the concentration of population, employment, or activity within urban space—constitutes a primary determinant of travel demand patterns. The spatial distribution of density across urban areas creates characteristic gradients that shape both the magnitude and spatial structure of OD matrices. Understanding these gradients requires appropriate mathematical models that capture the distance decay of density from urban centers.

The negative exponential function, originally introduced by Clark, provides the most widely applied model for urban density gradients [4]. This function takes the form:

$$\rho(r) = \rho_0 e^{-\mu r} = \rho_0 e^{-r/r_0}$$

where $\rho(r)$ represents the density at distance $r$ from the city center, $\rho_0$ is the central density, $\mu$ is the density decay coefficient, and $r_0$ is the characteristic decay distance [4]. This formulation captures the intuitive observation that density typically decreases with distance from urban cores, though the rate of decrease varies across cities and over time.

The exponential density model implies that travel demand generated at different locations will vary systematically with their position in the density gradient. Areas of high density near urban centers generate substantial trip production and attraction, while lower-density suburban areas produce fewer trips per unit area but may generate longer-distance journeys. These variations in trip generation characteristics directly affect the structure of OD matrices.

### 3.2 Density and Travel Behavior Relationships

Research on the built environment and travel behavior has established robust relationships between density and travel outcomes. Studies employing the "5D" framework—encompassing density, diversity, design, destination accessibility, and distance to transit—have consistently found that higher density is associated with reduced automobile dependence and increased use of sustainable transportation modes [5][6].

The relationship between density and travel outcomes, however, is not uniformly linear. Recent investigations using advanced machine learning techniques have revealed non-linear patterns and threshold effects that complicate simple density-travel relationships [5]. For automobile travel, increasing origin density initially reduces excess travel distance, indicating improved accessibility and shorter trips in moderately dense areas. However, at very high densities, excess travel distance begins to rise, likely due to congestion, limited parking, and network inefficiencies [5].

For public transit users, excess travel distance generally declines as density increases, reaching a minimum at moderate to high density levels before potentially increasing in extremely dense environments [5]. This pattern reflects the efficiency gains from dense, transit-oriented networks, where higher density supports more frequent service and shorter access distances. The sensitivity of transit users to density variations highlights the importance of density gradients for mode-specific capacity allocation.

### 3.3 Spatiotemporal Density Dynamics

Urban density is not static but exhibits both short-term fluctuations and long-term evolution. Short-term density variations occur as populations move through urban space during daily activity patterns—residents commuting to work, shoppers visiting commercial areas, and visitors accessing entertainment venues. These movements create dynamic density patterns that differ substantially from residential or employment-based density measures [4].

Grid-based time series approaches have been developed to capture the full spatiotemporal dynamics of population fluctuations [4]. Rather than representing population at a single time point, these methods track how population changes across both space and time, revealing patterns of concentration and dispersal that characterize urban activity rhythms. The temporal evolution of density patterns directly influences the temporal structure of OD matrices, with peak demand periods corresponding to times and locations of maximum activity concentration.

The relationship between population fluctuations and points of interest (POI) density demonstrates stronger urban allometry than the relationship with residential population density [4]. This finding suggests that activity-based density measures may better capture the demand-generating characteristics of urban locations than residential-based measures. For capacity allocation purposes, understanding the relationship between different density conceptualizations and travel demand enables more accurate demand forecasting.

## 4. Spatiotemporal Dynamics of OD Matrices

### 4.1 Temporal Heterogeneity in OD Patterns

OD matrices exhibit substantial temporal variation across multiple time scales. At the shortest scales, demand fluctuates within hours as travelers respond to time-varying conditions and schedule their activities. Daily patterns show characteristic peaks during morning and evening commute periods, with midday and off-peak periods exhibiting different demand structures. Weekly patterns distinguish weekday from weekend travel, while longer-term variations capture seasonal effects and trends [2].

The temporal correlation of network performance metrics presents particular challenges for dynamic OD estimation. Unlike static models that consider a single time interval, dynamic OD calibration must account for how demand in one period influences conditions in subsequent periods through congestion accumulation and dissipation [2]. The analytical network models developed for static contexts do not capture this temporal evolution, necessitating more sophisticated dynamic formulations.

Research on metro ridership has documented significant temporal heterogeneity in travel patterns. Ridership patterns vary across years, with individual stations showing consistent high-ridership levels while others fluctuate with urban development and service changes [6]. The number of entrances, floor-area ratio (FAR), and employment density emerge as consistently influential factors, while other built environment factors exhibit temporal variations in importance [6]. These findings underscore the dynamic nature of OD patterns and the need for capacity allocation strategies that can adapt to temporal changes.

### 4.2 Spatial Structure of OD Flows

The spatial distribution of OD flows reflects the underlying urban structure and the spatial organization of activities. OD matrices naturally exhibit block structures, with strong flows between adjacent or nearby zones and weaker flows between distant locations. The distance decay of OD flows follows patterns consistent with the negative exponential density model, though the specific parameters may differ from residential density decay [4].

Graph-based representations have proven effective for capturing the spatial structure of OD networks. Transportation networks can be modeled as graphs $G = (V, E)$, where $V$ represents nodes (intersections, zones, or stations) and $E$ represents edges (road segments or transit links) [7]. OD matrices represent weighted directed graphs, where the weight of edge $(i, j)$ corresponds to the flow $F_{i,j}$ from origin $i$ to destination $j$ [3].

The spatial dependencies among network elements create challenges for traditional analytical approaches but opportunities for graph-based machine learning methods. Graph neural networks (GNNs) can capture how traffic behavior at one location influences others, providing richer representations of network-wide conditions than localized analyses [7]. These approaches recognize that effective capacity allocation must consider the topology of the transportation network and the spatial propagation of demand effects.

### 4.3 Integrated Spatiotemporal Modeling

The full complexity of OD dynamics requires integrated spatiotemporal models that capture both spatial dependencies and temporal evolution. Deep learning frameworks combining graph convolution with temporal convolution have demonstrated effectiveness in capturing these dynamics [7]. Spatiotemporal graph convolutional networks (STGCN) represent one such architecture, combining spatial dependencies among network links with temporal dynamics in traffic patterns.

The Dual-Branch Spatial-Temporal Network (DBSTNet) represents a recent advance in OD demand forecasting that models pick-up and drop-off patterns via transposed OD matrices [8]. This approach employs independent branches to separately capture spatial-temporal features, developing multi-hop spatial-hierarchical temporal blocks that leverage polynomial-based graph convolutions to extract long-range spatial dependencies. Similar approaches using bidirectional demand trend modeling modules jointly learn demand evolution from both origin and destination perspectives [9].

Line-based Network Graph Aggregation (LNGA) provides another framework for approximating OD matrices while ensuring flow constraints and traffic assignment consistency [7]. The introduction of regularization terms in these formulations helps ensure that estimated OD matrices exhibit narrow variations, improving robustness and practical applicability. These methodological advances enable more accurate representation of spatiotemporal OD dynamics for capacity allocation purposes.

## 5. Capacity Allocation Under Density Gradients

### 5.1 Density-Dependent Demand Patterns

The relationship between urban density gradients and OD matrix characteristics creates density-dependent demand patterns that fundamentally shape capacity requirements. High-density areas generate substantial trip production and attraction, creating concentrated demand that may overwhelm local capacity even when average network conditions appear adequate. Conversely, low-density areas generate more dispersed demand that may be efficiently served with lower per-area capacity but potentially longer travel distances.

The non-linear relationship between density and travel outcomes has direct implications for capacity allocation. At moderate density levels, increasing density improves accessibility and reduces average trip lengths, potentially reducing capacity requirements per trip. However, at very high densities, congestion effects dominate, increasing travel times and potentially requiring capacity expansion to maintain performance levels [5]. This non-linearity means that capacity allocation strategies must consider not just absolute density levels but the position of specific locations within the density-performance curve.

Research on excess travel distance—the difference between actual travel distance and the minimum possible distance—provides insight into how density affects capacity requirements. For car trips, increasing origin density initially reduces excess travel distance, indicating improved route efficiency in moderately dense areas. However, at very high densities, excess travel distance rises due to congestion, limited parking, and network inefficiencies [5]. For public transit, excess travel distance declines significantly as density increases, reaching a minimum at moderate levels before potentially increasing in hyper-dense environments [5].

### 5.2 Spatial Non-Stationarity in Capacity Effects

The effects of capacity allocation on network performance exhibit spatial non-stationarity, meaning that identical capacity investments may produce different effects depending on their location within the urban density gradient. Capacity expansions in high-density, high-demand areas may generate substantial benefits by relieving bottlenecks that constrain overall network throughput. Similar expansions in lower-density areas may have minimal effects if demand is insufficient to utilize the additional capacity.

The phenomenon of congestion upstream of bottlenecks has particular relevance for understanding spatial non-stationarity in capacity effects. When demand for a link exceeds capacity, congestion develops on upstream links rather than on the constrained link itself [1]. This spatial separation between the capacity constraint and its effects means that capacity allocation decisions must consider the broader network context, not just local conditions. A capacity expansion at a bottleneck may reduce upstream congestion, but the benefits depend on the spatial distribution of demand and the network topology.

Network capacity models have been developed to assess the capacity flexibility and reliability of transportation networks under varying demand patterns [10]. These models recognize that network capacity is not a fixed property but depends on the spatial and temporal distribution of demand. The O-D cost decreases as network capacity increases, but this relationship is modulated by the structure of OD demand and the network topology [10].

### 5.3 Temporal Dynamics of Capacity Utilization

Capacity utilization varies temporally as OD patterns shift throughout the day, week, and year. Peak period demand creates capacity constraints that may be absent during off-peak periods, leading to temporal mismatches between supply and demand. Effective capacity allocation must account for these temporal dynamics, either through flexible capacity that can be reallocated across time periods or through infrastructure investments sized to accommodate peak demand.

The temporal correlation of network performance metrics creates challenges for capacity allocation under dynamic OD conditions. Demand in one time period influences conditions in subsequent periods through congestion accumulation and dissipation [2]. This temporal dependence means that capacity allocation decisions made for one period affect conditions in other periods, requiring integrated temporal analysis rather than independent period-by-period optimization.

Traffic resilience provides an important perspective on capacity allocation under varying demand conditions. Research has examined whether transportation networks are configured for maximum traffic resilience, presenting capacity allocation optimization problems with resilience maximization as the objective [11]. These approaches consider how capacity should be allocated—through lane allocations on two-way roads and traffic signal timing—to maximize network performance under both normal and disrupted conditions.

## 6. Methodological Approaches for Integrated Analysis

### 6.1 Traditional Analytical Methods

Classical transportation network analysis provides a foundation for understanding OD matrix effects on capacity allocation. Sensitivity analysis methods compute how link flows and travel costs change with respect to OD demand perturbations, enabling identification of critical demand variations that most affect network performance [1]. These methods rely on derivative-based calculations that exploit the mathematical structure of traffic assignment models.

The four-step planning process, while criticized for its sequential structure and static assumptions, remains the dominant framework for long-term transportation planning. Within this framework, OD matrix estimation combines trip generation and distribution models to produce demand forecasts that inform capacity allocation decisions [1]. The integration of land use and transportation models within this framework enables consideration of how density gradients affect both trip generation and distribution.

Network design optimization formulations seek to identify capacity investments that maximize network performance subject to budget constraints. These formulations may consider capacity expansion on existing links, addition of new links, or operational improvements that increase effective capacity [1]. The objective function typically incorporates user equilibrium travel costs, with constraints ensuring that investments stay within available resources.

### 6.2 Machine Learning and Deep Learning Approaches

Machine learning methods have increasingly been applied to OD matrix estimation and capacity allocation, offering capabilities for capturing complex non-linear relationships that traditional methods may miss. Extended Kalman Filter (EKF) approaches have found extensive application in OD estimation problems, providing a framework for recursive estimation that accounts for observation noise and model uncertainty [7].

Graph neural network approaches have demonstrated particular promise for transportation applications, recognizing the natural graph structure of transportation networks. Line Graph Convolutional Networks (L-GCN) transform line graphs to capture spatial-temporal OD flows from link information [7]. Spatiotemporal Graph Convolutional Networks (STGCN) combine graph convolution with temporal convolution to capture both spatial dependencies and temporal dynamics [7].

The XGBoost algorithm has been employed for modeling complex non-linear relationships between built environment factors and travel outcomes [5]. Unlike linear models that assume predetermined functional forms, XGBoost flexibly models intricate dependencies through ensemble decision trees, where each successive tree corrects the errors of its predecessors. This approach has revealed non-linear and threshold effects in density-travel relationships that simpler models would miss.

Deep learning approaches for OD demand forecasting have achieved substantial accuracy improvements over traditional methods. Models achieving over 85% accuracy in OD matrix prediction have been developed, with architectures including Multi-hop Spatial-Hierarchical Temporal blocks that leverage polynomial-based graph convolutions [8]. These advances enable more accurate representation of spatiotemporal OD dynamics for capacity allocation applications.

### 6.3 Hybrid and Integrated Frameworks

The complexity of spatiotemporal OD dynamics and their effects on capacity allocation has motivated hybrid frameworks that combine multiple methodological approaches. Simulation-based optimization algorithms have been developed for dynamic large-scale urban transportation problems, integrating analytical network models with simulation to capture complex network dynamics [2].

Prior OD matrices play an important role in estimation frameworks, capturing plausible demand patterns for calibration periods [2]. The weight factors in these formulations define trade-offs between fitting observed data and maintaining consistency with prior information, enabling incorporation of multiple data sources and uncertainty quantification.

Generative approaches for OD matrix modeling represent an emerging direction, leveraging advanced diffusion-based graph generation models to generate realistic OD matrices conditioned on urban characteristics [3]. These approaches can capture universal and distinct mobility patterns at the city level, potentially enabling transfer of insights across urban contexts.

## 7. Implications for Practice and Policy

### 7.1 Principles for Density-Responsive Capacity Allocation

The analysis presented in this report suggests several principles for capacity allocation that responds effectively to spatiotemporal OD dynamics and density gradients. First, capacity allocation should consider the position of network elements within urban density gradients, recognizing that identical investments may produce different effects depending on location. High-density areas with concentrated demand may warrant greater capacity investment per unit area than lower-density areas, though the non-linear relationship between density and performance must be considered.

Second, capacity allocation strategies should account for temporal heterogeneity in OD patterns. Peak period demand creates capacity constraints that may be addressed through infrastructure expansion, demand management, or operational improvements. The temporal correlation of network conditions means that capacity allocation decisions should consider effects across multiple time periods, not just the immediate period of investment.

Third, the threshold effects and non-linear relationships between density and travel outcomes suggest that capacity allocation should be guided by detailed analysis of local conditions rather than generic standards. What constitutes adequate capacity depends on the specific density context, the mode mix, and the network topology. Blanket capacity standards may under- or over-allocate resources relative to actual requirements.

### 7.2 Data and Modeling Requirements

Effective density-responsive capacity allocation requires data and modeling capabilities that capture spatiotemporal OD dynamics. Traditional OD estimation approaches based on household surveys and traffic counts provide valuable but infrequent snapshots of demand patterns. Emerging data sources—smart card transactions, mobile phone records, and connected vehicle data—offer opportunities for more frequent and granular demand estimation.

The computational requirements for spatiotemporal OD analysis and capacity optimization can be substantial, particularly for large urban networks. Metamodel approaches that approximate complex network models with simpler analytical formulations can reduce computational burdens while maintaining accuracy [2]. These approaches enable practical application of sensitivity analysis and optimization methods that would otherwise be infeasible.

Model integration represents an ongoing challenge, as different modeling approaches capture different aspects of OD dynamics and capacity effects. Frameworks that combine traditional analytical methods with machine learning approaches may offer the most comprehensive capabilities, leveraging the interpretability of classical methods and the flexibility of data-driven approaches.

### 7.3 Future Research Directions

Several research directions emerge from this analysis as promising for advancing understanding of OD matrix effects on capacity allocation. First, the development of dynamic network capacity models that explicitly account for spatiotemporal OD variations would enable more accurate assessment of capacity requirements under realistic demand conditions. Current capacity models often assume static demand patterns, limiting their applicability to dynamic contexts.

Second, research on the transferability of density-OD-capacity relationships across urban contexts would support planning in cities with limited local data. The universal and distinct mobility patterns identified in recent work suggest that some relationships may generalize across cities while others are context-specific [3]. Systematic comparison across urban contexts could identify which relationships are universal and which require local calibration.

Third, the integration of land use and transportation models with machine learning approaches offers opportunities for capturing the co-evolution of density patterns and transportation systems. As cities develop and change, both density gradients and OD patterns evolve, requiring capacity allocation strategies that can adapt to these changes.

## 8. Conclusion

This report has examined the complex relationships between spatiotemporal OD matrix distributions and capacity allocation under varying urban density gradients. The analysis reveals that these relationships are characterized by non-linear dynamics, threshold effects, and spatial non-stationarity that challenge traditional planning approaches.

The key findings can be summarized as follows. Urban density gradients fundamentally shape the spatial structure of OD matrices, with trip generation and distribution patterns varying systematically with distance from urban centers. The negative exponential density model provides a parsimonious representation of these gradients, though actual patterns may deviate from this idealized form. The relationship between density and travel outcomes is non-linear, with moderate densities often producing optimal accessibility while very high densities may increase congestion and travel times.

Spatiotemporal OD dynamics add additional complexity to capacity allocation. OD patterns vary substantially across time scales from hours to years, with temporal correlations that create challenges for dynamic estimation and prediction. Spatial dependencies among network elements mean that capacity effects propagate across the network, often in non-intuitive ways such as upstream congestion propagation from bottlenecks.

Methodological advances in machine learning and deep learning, particularly graph neural network approaches, offer promising capabilities for capturing spatiotemporal OD dynamics. These methods can represent complex spatial dependencies and temporal evolution that traditional analytical methods struggle to capture. However, integration with classical transportation planning frameworks remains an active area of development.

For practice, the analysis suggests that effective capacity allocation requires consideration of local density contexts, temporal demand patterns, and network topology. Generic capacity standards may be inadequate for addressing the specific requirements of different urban locations. Data-driven approaches that leverage emerging sources of demand information can support more responsive capacity allocation, though computational and integration challenges remain.

The spatiotemporal distribution of OD matrices and their interaction with density gradients represents a rich area for continued research. As cities continue to grow and evolve, understanding these relationships becomes increasingly important for sustainable transportation planning. The methodological tools for addressing these challenges continue to advance, offering hope for more effective and efficient capacity allocation in urban transportation systems.

## References

[1] Boyles, S. D. Transportation Network Analysis. https://sboyles.github.io/book082.pdf

[2] Osorio, C. Dynamic OD Calibration for Urban Transportation Networks. https://web.mit.edu/osorioc/www/papers/osoDynamicOD.pdf

[3] ICLR 2025 Proceedings. Large-Scale Commuting OD Matrix Generation via Diffusion Models. https://proceedings.iclr.cc/paper_files/paper/2025/file/efccec15378fba34be92d814a38e89ac-Paper-Conference.pdf

[4] Nature Communications. Urban density scaling of population fluctuations. https://www.nature.com/articles/s41467-025-58286-4

[5] Scientific Reports. Built environment factors and excess travel distance in medium-sized cities. https://www.nature.com/articles/s41598-025-17878-2

[6] Information Technology and Innovation Foundation. Metro ridership and built environment factors. https://academic.oup.com/iti/article/doi/10.1093/iti/liae023/7931050

[7] Taylor & Francis Online. Deep learning approaches for OD estimation. https://www.tandfonline.com/doi/full/10.1080/23249935.2026.2616045

[8] Alexandria Engineering Journal. DBSTNet for taxi OD demand prediction. https://www.sciencedirect.com/science/article/pii/S1110016825008464

[9] ScienceDirect. DSTCN for OD demand forecasting. https://www.sciencedirect.com/science/article/pii/S095741742503711X

[10] Springer. Network capacity models and OD cost relationships. https://link.springer.com/article/10.1007/s11116-021-10208-1

[11] EPFL TRC-30. Traffic resilience and capacity allocation optimization. https://trc-30.epfl.ch/wp-content/uploads/2024/09/TRC-30_paper_189.pdf

## Annotations


## Sources
[1] http://www.sciencedirect.com/science/article/pii/S1110016825008464
[2] https://academic.oup.com/iti/article/doi/10.1093/iti/liae023/7931050
[3] https://arxiv.org/html/2407.15823v3
[4] https://arxiv.org/html/2503.24237v1
[5] https://bayen.berkeley.edu/sites/default/files/dissertation_yiling_phd.pdf
[6] https://docs.aimsun.com/next/22.0.1/UsersManual/TransportPlanningAndDemandAnalysisModelsAndAlgorithms.html
[7] https://escholarship.org/content/qt1nw754s6/qt1nw754s6.pdf
[8] https://fi.ee.tsinghua.edu.cn/~dingjingtao/papers/ODGenBench.pdf
[9] https://journal-buildingscities.org/articles/10.5334/bc.125
[10] https://lexparsimon.github.io/pdfs/PhD_Thesis_Gevorg_Yeghikyan_Corrected.pdf
[11] https://link.springer.com/article/10.1007/s11116-021-10208-1
[12] https://link.springer.com/article/10.1007/s42421-025-00124-6
[13] https://orca.cardiff.ac.uk/id/eprint/144683/3/s41598-021-97208-4.pdf
[14] https://pmc.ncbi.nlm.nih.gov/articles/PMC12671825/
[15] https://proceedings.iclr.cc/paper_files/paper/2025/file/efccec15378fba34be92d814a38e89ac-Paper-Conference.pdf
[16] https://sboyles.github.io/book082.pdf
[17] https://sumo.dlr.de/pdf/2025/pre-print-2628.pdf
[18] https://tfresource.org/topics/Temporal_data.html
[19] https://trc-30.epfl.ch/wp-content/uploads/2024/09/TRC-30_paper_189.pdf
[20] https://web.mit.edu/osorioc/www/papers/osoDynamicOD.pdf
[21] https://www.frontiersin.org/journals/sustainable-cities/articles/10.3389/frsc.2025.1681723/full
[22] https://www.ijcai.org/proceedings/2025/0372.pdf
[23] https://www.mdpi.com/2073-445X/14/6/1232
[24] https://www.mdpi.com/2076-3417/15/22/12156
[25] https://www.nature.com/articles/s41467-025-58286-4
[26] https://www.nature.com/articles/s41598-025-17878-2
[27] https://www.sciencedirect.com/science/article/pii/S095741742503711X
[28] https://www.tandfonline.com/doi/full/10.1080/23249935.2026.2616045
[29] https://www.tn.gov/content/dam/tn/tdot/research/final-reports/2023-final-reports-and-summaries/RES2023-17%20-%20AI-Engine%20-%20TMS%20-%20%20Final%20Report-Approved.pdf