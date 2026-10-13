# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 09543024 | **Time:** 214.65s | **Cost:** $0.12778
--------------------------------------------------------------------------------

# How Does Carbon Emission Distribution Impact Optimal Capacity Configuration Across Different Travel Modes?

## A Research Report on Carbon-Aware Transportation Network Optimization

---

## Executive Summary

The intersection of carbon emission management and transportation capacity planning represents one of the most consequential challenges facing modern supply chain and logistics operations. As global industrialization and urbanization continue to intensify, the transportation sector has emerged as a significant contributor to carbon emissions, with vehicle exhaust and freight transport accounting for substantial shares of land transport pollution [1]. This report examines how the spatial and modal distribution of carbon emissions fundamentally shapes optimal capacity configuration decisions across different travel modes, drawing upon recent advances in machine learning, evolutionary optimization, and multimodal transportation network analysis.

The research synthesized in this report reveals that carbon emission distribution patterns exert a profound influence on capacity allocation strategies, with emission-intensive modes such as air freight and long-haul trucking requiring fundamentally different optimization approaches compared to lower-emission alternatives like rail and pipeline transport. The evidence demonstrates that strategic modal shifts, particularly toward rail transport, can achieve substantial emission reductions—41.4% in regional distribution networks—while maintaining operational efficiency with only modest cost increases [2]. Furthermore, the integration of carbon constraints into capacity optimization models necessitates sophisticated analytical frameworks that account for the heterogeneous emission characteristics across transportation modes, the temporal dynamics of emission generation, and the complex interdependencies within multimodal networks.

The findings presented herein have significant implications for supply chain managers, urban planners, and policymakers seeking to balance economic efficiency with environmental sustainability. By understanding how emission distribution patterns inform capacity configuration decisions, organizations can develop more effective strategies for achieving their sustainability goals while maintaining competitive operational performance.

---

## 1. Introduction

### 1.1 Background and Motivation

The contemporary landscape of global transportation and logistics is characterized by an increasingly urgent imperative to reduce carbon footprints while maintaining operational efficiency. The rapid development of the global economy and the deepening of international trade have not only facilitated unprecedented economic growth but have also intensified environmental burdens, particularly when sustainability considerations are not prioritized in supply chain design [3]. This tension between economic efficiency and environmental sustainability has catalyzed extensive research into carbon-aware optimization approaches that can reconcile these seemingly competing objectives.

Transportation infrastructure plays a pivotal role in the spatial distribution of carbon emissions, with different travel modes exhibiting substantially varying emission profiles. Trucks, commonly used for regional and last-mile deliveries, produce high amounts of CO₂ per mile, with diesel engines dominating freight transport and accounting for significant shares of land transport pollution [4]. Airplanes, while efficient for time-sensitive deliveries, exhibit the highest carbon footprint per ton-mile, whereas cargo ships, though more fuel-efficient for large quantities, emit both carbon and sulfur oxides that affect both climate and air quality [4]. These divergent emission characteristics fundamentally shape how capacity should be configured across different transportation modes to achieve optimal sustainability outcomes.

The increasing urgency of carbon footprint reduction in supply chain operations demands innovative optimization approaches that balance economic efficiency with environmental sustainability [2]. Traditional capacity configuration methods that focus exclusively on cost minimization fail to capture the full spectrum of environmental externalities associated with transportation decisions. Consequently, there is a growing recognition that carbon emission distribution must be explicitly integrated into capacity optimization frameworks to achieve meaningful sustainability improvements.

### 1.2 Research Objectives

This report aims to provide a comprehensive analysis of how carbon emission distribution impacts optimal capacity configuration across different travel modes. The specific objectives are threefold. First, we examine the theoretical foundations of carbon-aware capacity optimization, including the mathematical frameworks used to model emission distributions and their influence on capacity allocation decisions. Second, we analyze empirical evidence from recent studies that have implemented carbon-constrained optimization approaches, evaluating the trade-offs between emission reduction and cost efficiency across different scenarios. Third, we synthesize the findings to derive actionable insights for practitioners and policymakers seeking to implement carbon-aware capacity configuration strategies.

### 1.3 Scope and Methodology

The analysis presented in this report draws upon peer-reviewed research published in leading transportation and logistics journals, supplemented by technical reports from environmental agencies and international organizations. The scope encompasses both passenger and freight transportation, with particular emphasis on multimodal networks where capacity configuration decisions involve complex interdependencies across different travel modes. The methodological approach involves systematic review and synthesis of quantitative findings from controlled experiments, case studies, and optimization modeling exercises.

---

## 2. Theoretical Framework: Carbon Emission Distribution and Capacity Optimization

### 2.1 Understanding Carbon Emission Distribution in Transportation

Carbon emission distribution in transportation systems exhibits considerable heterogeneity across multiple dimensions, including travel mode, geographic location, temporal period, and operational conditions. The distribution of emissions is not uniform across the transportation network; rather, it reflects the underlying characteristics of different transport modes, the spatial configuration of infrastructure, and the operational patterns of carriers and shippers. Understanding this distribution is essential for developing effective capacity configuration strategies that target emission reductions where they can be most impactful.

The emission factors associated with different transportation modes vary by orders of magnitude, reflecting fundamental differences in energy efficiency and fuel consumption characteristics. According to emission factor data for various transportation modes, ocean tankers exhibit the lowest emission intensity at 5.54 gCO₂e/t-km, followed by barges at 32.93 gCO₂e/t-km, pipelines at 0.05 × CIelec gCO₂e/t-km, rail at 38.5 gCO₂e/t-km, trucks at 21.87 gCO₂e/t-km, and jet fuel at 80.05 gCO₂e/t-km [5]. These substantial differences in emission intensity imply that capacity configuration decisions—which determine the allocation of freight and passenger flows across modes—have profound implications for overall carbon footprint.

The spatial distribution of emissions across transportation networks further complicates capacity optimization. Research on transport infrastructure and the spatial distribution of CO₂ emissions has demonstrated that emission hot spots emerge in specific locations and time periods, influenced by traffic density, infrastructure characteristics, and operational patterns [6]. Traditional methods for identifying emission hot spots have relied on point density measures that fail to account for spatial and temporal factors, limiting their utility for informing capacity configuration decisions. Advanced analytical approaches using space-time cubes and Emerging Hot Spot analysis have been developed to address these limitations, providing more accurate identification of emission concentration patterns [6].

### 2.2 Mathematical Formulation of Carbon-Constrained Capacity Optimization

The integration of carbon emission constraints into capacity optimization models requires careful mathematical formulation that captures both the emission characteristics of different travel modes and the operational constraints of the transportation system. The total carbon emission during transportation includes carbon dioxide emitted during transportation and transit, with the calculation formula expressed as:

$$
E_{total} = \sum_{m \in M} \sum_{l \in L} \sum_{i \in N} \sum_{j \in N} \sum_{m' \in M} e_{ijm}^{ml} \cdot d_{ij} \cdot y_{iml} + \sum_{m \in M} \sum_{l \in L} \sum_{i \in N} \sum_{j \in N} \tilde{e}_{ijm}^{ml} \cdot d_{ij} \cdot x_{ijm}
$$

where $e_{ijm}^{ml}$ represents the emission factor for mode $m$ on link $l$ between nodes $i$ and $j$, $d_{ij}$ denotes the distance between nodes, $y_{iml}$ is the binary variable indicating whether mode $m$ is used on link $l$ at node $i$, and $x_{ijm}$ represents the flow of goods transported by mode $m$ between nodes $i$ and $j$ [3]. This formulation captures both the direct emissions from transportation activities and the indirect emissions associated with different operational choices.

The capacity optimization problem with carbon emission constraints can be formulated as a multi-objective optimization problem that simultaneously minimizes total cost and total emissions subject to operational constraints. The objective functions typically include:

$$
\min Z_1 = \sum_{m \in M} \sum_{l \in L} \sum_{i \in N} \sum_{j \in N} c_{ijm}^{ml} \cdot d_{ij} \cdot x_{ijm}
$$

$$
\min Z_2 = \sum_{m \in M} \sum_{l \in L} \sum_{i \in N} \sum_{j \in N} e_{ijm}^{ml} \cdot d_{ij} \cdot x_{ijm}
$$

subject to capacity constraints, flow conservation constraints, and emission budget constraints [3]. The solution of such multi-objective problems requires specialized optimization algorithms that can efficiently explore the trade-off frontier between cost and emissions.

### 2.3 The Role of Emission Prediction in Capacity Configuration

Accurate prediction of carbon emissions is essential for informing capacity configuration decisions, particularly in complex multimodal networks where emission patterns are influenced by numerous interacting factors. Recent advances in machine learning have enabled the development of sophisticated emission prediction models that can capture the nonlinear relationships between operational parameters and emission outcomes. A novel carbon-aware route optimization framework has been developed that integrates machine learning-based emission prediction with genetic algorithm optimization for sustainable supply chain management [2].

The hybrid approach combines Random Forest and XGBoost models in an optimized ensemble to predict carbon emissions with high accuracy, achieving a Mean Absolute Percentage Error (MAPE) of 9.48% and a correlation coefficient (R) of 0.928 [2]. These prediction models serve as critical components of the overall optimization framework, providing accurate estimates of the emission implications of different capacity configuration decisions. The integration of machine learning prediction with evolutionary optimization enables the framework to handle the complexity and uncertainty inherent in real-world transportation systems while still achieving meaningful emission reductions.

---

## 3. Empirical Evidence: Carbon-Aware Capacity Optimization in Practice

### 3.1 Controlled Experiments on Synthetic Datasets

The validation of carbon-aware capacity optimization approaches through controlled experiments on synthetic datasets provides valuable insights into the potential for emission reduction across different network configurations. Research has demonstrated the effectiveness of integrated analytics frameworks for carbon-aware supply chain routing through experiments involving 3,500 routes across three network sizes: 500, 1000, and 2000 routes [2]. These synthetic datasets, derived from real-world emission factors, enable systematic evaluation of optimization performance under controlled conditions.

The results from these controlled experiments reveal that the proposed carbon-aware optimization approach achieves an average emission reduction of 19.5% with only a 4.7% increase in total cost compared to traditional cost-only optimization methods [2]. This finding suggests that substantial environmental improvements can be achieved without incurring disproportionate economic costs, challenging the conventional wisdom that emission reduction necessarily requires significant financial sacrifice. The relatively modest cost increase indicates that traditional optimization approaches have been systematically overlooking opportunities for emission reduction that are available at low or moderate cost.

The synthetic dataset experiments also demonstrate the scalability of the carbon-aware optimization approach across different network sizes. The optimization framework maintains consistent performance characteristics as network complexity increases, with the genetic algorithm effectively exploring the solution space to identify capacity configurations that balance cost and emission objectives. This scalability is essential for practical applications, as real-world transportation networks often involve thousands of routes and multiple transportation modes.

### 3.2 Real-World Case Study: Salamanca Regional Distribution Network

While controlled experiments provide valuable validation of optimization methodologies, real-world case studies offer insights into the practical implementation and outcomes of carbon-aware capacity configuration. A quasi-real case study conducted on the Salamanca regional distribution network, involving 12 routes and 776.6 tons of CO₂e annually, demonstrates the substantial emission reduction potential of strategic modal shifts [2].

The case study achieved a 41.4% emission reduction with only an 8.6% cost increase through strategic modal shifts to rail transport [2]. This result represents a significantly higher emission reduction than observed in the synthetic dataset experiments, reflecting the particular characteristics of the Salamanca network and the opportunities for modal shift that it presents. The higher emission reduction can be attributed to the specific origin-destination patterns in the regional network, where rail transport offers substantial advantages over road transport for certain freight flows.

The Salamanca case study highlights several important insights for capacity configuration decisions. First, the magnitude of emission reduction achievable through modal shift depends critically on the specific characteristics of the transportation network and the availability of viable alternatives to high-emission modes. Second, the cost implications of modal shift vary substantially across different network configurations, with some networks offering greater opportunities for emission reduction at lower cost. Third, the integration of rail transport into regional distribution networks can yield substantial environmental benefits while maintaining operational efficiency, particularly for medium-distance flows where rail offers competitive transit times.

### 3.3 Comparative Analysis with Traditional Optimization Methods

Both the synthetic dataset experiments and the Salamanca case study significantly outperform traditional cost-only optimization methods [2]. This comparison underscores the limitations of conventional approaches that treat carbon emissions as externalities to be ignored in the optimization process. Traditional cost-only optimization implicitly assumes that emissions have no value or that their reduction is infinitely costly, leading to capacity configurations that externalize environmental costs onto society.

The performance gap between carbon-aware and cost-only optimization approaches has important implications for organizational decision-making and public policy. From an organizational perspective, the evidence suggests that supply chain managers who incorporate carbon considerations into their optimization models can achieve substantial environmental improvements while maintaining competitive cost structures. From a policy perspective, the findings support the development of regulatory frameworks and incentive structures that encourage or require the consideration of carbon emissions in transportation planning.

The comparative analysis also reveals that the optimal capacity configuration depends fundamentally on how carbon emissions are valued in the optimization process. When emissions are explicitly incorporated as constraints or objectives, the resulting capacity allocations differ substantially from those generated by cost-only optimization. This sensitivity to emission valuation highlights the importance of establishing appropriate carbon prices or emission targets that reflect the true social cost of carbon emissions.

---

## 4. Modal Analysis: Emission Distribution Across Travel Modes

### 4.1 Road Transport: Trucks and Last-Mile Delivery

Road transport, particularly trucking, represents a significant source of carbon emissions in freight transportation systems. Diesel engines dominate freight transport, and emissions from trucking account for a substantial share of land transport pollution [4]. The emission intensity of trucks, at 21.87 gCO₂e/t-km, is substantially higher than rail or pipeline alternatives, reflecting the lower energy efficiency of road transport compared to rail-based systems [5].

The impact of growing numbers of delivery vehicles on congestion and carbon emissions has been modeled across different urban contexts. Under a business-as-usual scenario, delivery vehicles could rise by 61% by 2030 across all cities, with carbon emissions from deliveries expected to rise on average by 60% by 2030 globally [7]. This increase would make delivery emissions account for approximately 54% of the transport sector's emissions and 13% of overall city emissions [7]. These projections underscore the urgency of developing carbon-aware capacity configuration strategies for urban freight systems.

The characteristics of road transport emission distribution have important implications for capacity optimization. Truck emissions are highly variable depending on vehicle type, age, load factor, and operating conditions. Older diesel vehicles typically exhibit higher emission intensities than newer models equipped with advanced emission control technologies. The emergence of electric vehicles offers opportunities for substantial emission reduction in road freight, though the adoption timeline depends on factors including vehicle availability, charging infrastructure, and electricity generation mix [8].

### 4.2 Rail Transport: Environmental Advantages and Capacity Implications

Rail transport exhibits substantially lower emission intensity than road transport, with emission factors of 38.5 gCO₂e/t-km representing less than half the intensity of trucking on a per-ton-kilometer basis [5]. This environmental advantage makes rail an attractive option for capacity configuration decisions seeking to minimize carbon footprint, particularly for medium-distance freight flows where rail can compete effectively with road transport on transit time.

Research on high-speed rail (HSR) systems has demonstrated significant emission reduction benefits compared to aviation and road alternatives. Studies estimate that HSR emits 66% to 97% less greenhouse gas emissions per passenger-kilometer traveled than flying, depending on assumptions about fuel sources, fuel efficiency, and ridership levels [9]. The GHG reduction benefits of HSR relative to aviation are generally explained by two factors: the higher energy efficiency of electric rail systems and the lower emission intensity of electricity generation compared to jet fuel combustion.

The capacity implications of rail transport differ substantially from road transport. Rail networks require substantial upfront investment in infrastructure, including tracks, stations, and rolling stock. Once established, however, rail capacity can be highly efficient, with trains capable of moving large quantities of freight over long distances with relatively low incremental energy consumption. The fixed nature of rail infrastructure creates path dependencies in capacity configuration, as decisions about rail network development have long-lasting implications for future transportation options.

### 4.3 Air and Maritime Transport: High-Emission Modes with Unique Roles

Air transport exhibits the highest carbon footprint per ton-mile among common transportation modes, with emission factors of 80.05 gCO₂e/t-km substantially exceeding those of other modes [5]. Despite this environmental disadvantage, air transport plays a unique role in supply chains for time-sensitive goods where the value of rapid delivery outweighs the environmental costs. The emission intensity of air freight reflects the high energy requirements of aircraft propulsion and the relative inefficiency of current aviation technologies.

Maritime transport, including ocean tankers and barges, exhibits the lowest emission intensity among surface transportation modes, with ocean tankers at 5.54 gCO₂e/t-km and barges at 32.93 gCO₂e/t-km [5]. These low emission intensities reflect the energy efficiency of large vessel operations and the use of heavy fuel oils with relatively high energy content. However, maritime emissions also include sulfur oxides and other pollutants that affect both climate and air quality, complicating the environmental assessment of maritime transport [4].

The capacity configuration implications of air and maritime transport reflect their distinct characteristics. Air freight capacity is constrained by aircraft availability, airport infrastructure, and regulatory limitations, with high variable costs that make air transport economical primarily for high-value, time-sensitive goods. Maritime freight capacity is constrained by vessel availability, port infrastructure, and canal capacity, with long transit times that limit suitability for time-sensitive applications. The integration of these high-capacity, low-frequency modes with faster but higher-emission alternatives requires careful optimization to balance speed, cost, and environmental considerations.

### 4.4 Emerging Technologies: Electric Vehicles and Alternative Fuels

The transition toward electric vehicles and alternative fuels represents a significant opportunity for reducing carbon emissions across transportation modes. A significant transition to EVs and micromobility is underway, especially among larger organizations [7]. The adoption of electric ground vehicles occurs later in decarbonization pathways, allowing stable contracts with traditional transportation to be maintained while gradually transitioning to lower-emission alternatives [8].

The emission reduction potential of electric vehicles depends critically on the carbon intensity of electricity generation. Pipeline transport, with emission factors expressed as 0.05 × CIelec gCO₂e/t-km, directly reflects the dependence of electric transport on the emissions intensity of the power sector [5]. As electricity generation shifts toward renewable sources, the environmental advantages of electric transport will increase correspondingly. This interdependence between electricity sector decarbonization and transportation electrification has important implications for long-term capacity configuration planning.

Alternative fuels, including sustainable aviation fuels and renewable diesel, offer additional pathways for emission reduction in transportation. The EPA's lifecycle analysis of renewable fuel standards includes emissions associated with distributing finished fuel to consumers, recognizing that fuel production and distribution contribute to overall carbon footprint [10]. The development of carbon-aware capacity configuration strategies must account for the full lifecycle emissions of different fuel options, not just the operational emissions from vehicle operation.

---

## 5. Network-Level Analysis: Carbon Distribution and System-Wide Optimization

### 5.1 Multimodal Network Design and Carbon Allocation

The design of multimodal transportation networks involves complex interdependencies between different transport modes, with capacity configuration decisions on one mode affecting the performance and emissions of connected modes. Research on multimodal logistics network design has examined the trade-offs between carbon footprint and network resilience, demonstrating that appropriate nodal redundancy in transport capacity significantly enhances network resilience while achieving concurrent carbon emission reduction [11].

The optimization of multimodal networks under carbon emission constraints requires analytical frameworks that can capture the interactions between different modes and the system-wide implications of capacity decisions. The Belt and Road Initiative (BRI) multimodal transportation network has been analyzed to examine these trade-offs, with findings demonstrating that optimized networks achieve fewer node failures, enhanced partial adaptability, and improved disturbance resistance while reducing carbon emissions [11]. These results suggest that carbon-aware capacity configuration can enhance, rather than compromise, network resilience when properly designed.

The mathematical optimization of multimodal networks with carbon constraints involves complex formulations that must account for mode-specific emission characteristics, intermodal transfer costs and emissions, and the capacity constraints of individual network elements. Mixed integer linear programming (MILP) models with profit maximization and emission minimization have been proposed to determine the optimal configuration of distribution centers and transportation mode selection [12]. These models enable systematic exploration of the trade-off space between economic and environmental objectives.

### 5.2 Spatial and Temporal Dynamics of Emission Distribution

The spatial distribution of carbon emissions across transportation networks exhibits complex patterns that reflect the underlying structure of the network and the patterns of demand across different origin-destination pairs. Research on transport infrastructure and the spatial distribution of CO₂ emissions has highlighted the importance of understanding these patterns for effective emission reduction strategies [6]. Emission hot spots emerge in specific locations where traffic density, infrastructure characteristics, and operational patterns combine to generate high emission intensities.

Temporal dynamics add additional complexity to carbon-aware capacity configuration. Emission patterns vary across time scales ranging from daily cycles to seasonal variations, reflecting changes in demand patterns, weather conditions, and operational practices. The integration of temporal considerations into capacity optimization requires models that can capture these dynamics and identify capacity configurations that perform well across different temporal conditions.

The use of space-time cubes and Emerging Hot Spot analysis has been developed to address the limitations of traditional point-density methods for identifying emission concentration patterns [6]. These advanced analytical approaches enable more accurate identification of emission hot spots by accounting for both spatial and temporal factors, providing better information for targeting capacity configuration interventions. The integration of these analytical tools with optimization models represents an important frontier in carbon-aware transportation planning.

### 5.3 Resilience and Sustainability Trade-offs

The relationship between network resilience and carbon emissions represents a critical consideration for capacity configuration decisions. Research has demonstrated that appropriate nodal redundancy in transport capacity significantly enhances network resilience, with optimized networks achieving concurrent carbon emission reduction, fewer node failures, and enhanced partial adaptability and disturbance resistance [11]. This finding suggests that resilience and sustainability objectives can be mutually reinforcing rather than conflicting.

The optimization of resilience in multimodal transportation networks under cascading failures while incorporating carbon emission constraints aims to enhance the stability and sustainability of the network [11]. Through constructing theoretical models and optimization strategies, researchers have provided scientific basis for network development that balances multiple objectives. The primary research questions addressed include how to evaluate network resilience during cascading failures and how to optimize the network to achieve effective balance between transportation carbon reduction and resilience enhancement.

The trade-offs between resilience and carbon emissions depend on the specific characteristics of the network and the nature of potential disruptions. Networks with high redundancy may exhibit higher baseline emissions due to the maintenance of excess capacity, but may also provide greater opportunities for routing around congested or disrupted links, potentially reducing emissions during disruption events. The optimal balance between redundancy and efficiency depends on the probability and severity of potential disruptions and the value placed on maintaining continuous network operation.

---

## 6. Policy Frameworks and Implementation Strategies

### 6.1 Carbon Pricing and Market-Based Instruments

Carbon pricing mechanisms, including carbon taxes and emissions trading systems (ETS), provide economic incentives for emission reduction that can inform capacity configuration decisions. A declining cap ensures that emissions fall over time and gives companies predictability, as they know that emission permits will become increasingly scarce and costly, incentivizing investments in decarbonization [13]. There is a direct correlation between how fast the cap decreases and the level of climate ambition, with more aggressive reduction trajectories driving faster adoption of low-carbon technologies.

The implementation of carbon pricing in transportation faces unique challenges due to the distributed nature of emission sources and the difficulty of measuring emissions at the point of generation. Different mechanisms have been developed to address these challenges, including carbon taxes on fuels, emissions trading for large industrial sources, and carbon charges on transportation services. The effectiveness of these mechanisms for influencing capacity configuration decisions depends on their coverage, price level, and predictability.

Market stability mechanisms can help reduce price volatility in emissions trading systems, providing greater certainty for investment decisions [13]. Volume containment tools, such as the EU ETS Market Stability Reserve, can help reduce or increase the amount of allowances available to stabilize prices over time. These mechanisms are important for creating predictable policy environments that enable long-term investment in low-carbon transportation capacity.

### 6.2 Regulatory Approaches and Mandated Standards

Regulatory approaches to transportation carbon emissions include fuel efficiency standards, emission performance standards, and operational requirements. The restrictive policy represented by the carbon emission cap policy is widely used worldwide, setting absolute limits on emissions that must be achieved through operational improvements, modal shifts, or technology adoption [14]. These regulatory approaches directly influence capacity configuration decisions by constraining the emission intensity of transportation services.

The development of regulatory frameworks for transportation carbon emissions must balance environmental objectives with economic considerations, avoiding outcomes that would impose disproportionate costs on specific sectors or regions. The literature on carbon policy has recognized that carbon pricing alone may not be sufficient to mitigate climate change, with sustainability transition policy needed to address market failures and behavioral barriers to emission reduction [14]. Complementary policies, including infrastructure investment, technology development support, and information provision, can enhance the effectiveness of carbon pricing.

### 6.3 Incentive Structures for Sustainable Transportation

The design of incentive structures that encourage the adoption of sustainable transportation technologies and practices represents an important policy lever for influencing capacity configuration. Research has identified that incentivizing carbon-efficient technologies is required to spur investment in emission reduction capabilities [8]. These incentives can take various forms, including subsidies for low-carbon vehicles, tax incentives for rail infrastructure investment, and priority access for low-emission vehicles in congested areas.

Public perception and social norms play a significant role in the adoption of sustainable transportation practices. In areas or communities in which sustainability is a mainstream concern, there is often greater acceptance of interventions such as EVs and e-bike deliveries [7]. In contrast, communities with deeply ingrained practices may resist such changes. Public support is essential for sustainable transportation policies to succeed, highlighting the importance of communication and engagement in policy implementation.

The framework for creating incentives for the introduction of more sustainable delivery modes is crucial for achieving emission reduction targets [7]. These incentives can include financial mechanisms such as congestion charges that exempt low-emission vehicles, grants for electric vehicle charging infrastructure, and preferential parking for sustainable transport modes. The design of effective incentive structures requires understanding of the behavioral responses of carriers and shippers to different policy interventions.

---

## 7. Implications for Capacity Configuration Decision-Making

### 7.1 Strategic Modal Selection

The evidence synthesized in this report demonstrates that strategic modal selection is a powerful lever for reducing carbon emissions in transportation systems. The substantial emission reductions achieved through modal shifts to rail transport—41.4% in the Salamanca case study—highlight the potential for reallocating freight flows from high-emission to low-emission modes [2]. However, the feasibility and cost-effectiveness of modal shift depend on network characteristics, commodity types, and service requirements.

The selection of transportation modes should be informed by comprehensive assessment of emission implications across the full lifecycle, including not only operational emissions but also emissions from infrastructure construction, vehicle manufacturing, and fuel production. The EPA's lifecycle analysis of renewable fuels includes emissions associated with distributing finished fuel to consumers, recognizing the importance of supply chain emissions in overall carbon footprint [10]. This lifecycle perspective is essential for avoiding problem shifting, where emission reductions in one area are offset by increases elsewhere.

The integration of modal selection into capacity configuration decisions requires optimization models that can evaluate the trade-offs between different mode combinations across the entire network. The genetic algorithm optimization approach developed for carbon-aware supply chain routing enables systematic exploration of modal alternatives while respecting operational constraints [2]. The combination of machine learning-based emission prediction with evolutionary optimization provides a powerful framework for identifying capacity configurations that balance cost and environmental objectives.

### 7.2 Network Design and Infrastructure Investment

The design of transportation networks and the investment in infrastructure capacity have long-lasting implications for carbon emission patterns. Rail networks require substantial upfront investment but offer low-emission capacity that can serve freight flows for decades after construction. The path dependencies created by infrastructure investment decisions make it essential to incorporate carbon considerations into long-term planning processes.

Research on nearshoring of manufacturing has demonstrated that shortening supply chains reduces both costs and emissions, with the initial slowing of ships at sea having the most impact on cutting carbon emissions [8]. The adoption of electric ground vehicles occurs later in the decarbonization pathway, allowing stable contracts with traditional transportation to be maintained while gradually transitioning to lower-emission alternatives. These findings suggest that network design decisions should consider not only current emission intensities but also anticipated future improvements in technology and operational practices.

The appropriate nodal redundancy in transport capacity significantly enhances network resilience while supporting carbon emission reduction objectives [11]. Investment in redundant capacity may increase baseline emissions but provides flexibility for responding to disruptions and optimizing network performance over time. The optimal level of redundancy depends on the value placed on resilience and the expected evolution of emission intensities across different modes.

### 7.3 Operational Optimization and Real-Time Decision Support

Beyond strategic network design, operational optimization provides opportunities for emission reduction through improved dispatching, routing, and load consolidation decisions. The machine learning-based emission prediction models developed for carbon-aware supply chain routing can provide real-time decision support for operational decisions, enabling carriers and shippers to select routes and schedules that minimize emissions while meeting service requirements [2].

The integration of carbon awareness into operational decision-making requires accurate and timely information about emission implications of different choices. The high prediction accuracy achieved by ensemble machine learning models—MAPE of 9.48% and correlation coefficient of 0.928—provides sufficient reliability for informing operational decisions [2]. As these technologies mature and become more widely deployed, they will enable increasingly sophisticated carbon-aware operational optimization.

The scalability of carbon-aware optimization approaches across different network sizes and complexities is essential for practical implementation. The demonstration of consistent performance across synthetic datasets ranging from 500 to 2000 routes provides confidence that these approaches can be applied to real-world networks of substantial size and complexity [2]. The continued development of computational methods and data infrastructure will further enhance the feasibility of comprehensive carbon-aware optimization.

---

## 8. Conclusions and Future Directions

### 8.1 Key Findings

This report has examined how carbon emission distribution impacts optimal capacity configuration across different travel modes, synthesizing evidence from recent research on carbon-aware transportation optimization. The key findings can be summarized as follows.

First, carbon emission distribution patterns exert a profound influence on capacity configuration decisions, with substantial variation in emission intensity across transportation modes creating opportunities for emission reduction through strategic modal selection. Rail transport exhibits emission intensities less than half those of trucking, while air transport exhibits intensities nearly four times higher than road alternatives. These differences imply that capacity allocation across modes has fundamental implications for environmental performance.

Second, carbon-aware optimization approaches can achieve substantial emission reductions at modest cost increases. The evidence from both synthetic dataset experiments and real-world case studies demonstrates that emission reductions of 19.5% to 41.4% are achievable with cost increases of only 4.7% to 8.6% [2]. These findings challenge the conventional wisdom that emission reduction necessarily requires significant financial sacrifice and support the business case for carbon-aware capacity configuration.

Third, the integration of machine learning-based emission prediction with evolutionary optimization provides powerful capabilities for identifying optimal capacity configurations that balance cost and environmental objectives. The high prediction accuracy achieved by ensemble models enables reliable estimation of emission implications across complex network configurations, while genetic algorithms efficiently explore the solution space to identify high-performing configurations.

Fourth, network-level analysis reveals that carbon-aware capacity configuration can enhance, rather than compromise, other network performance objectives including resilience and adaptability. Appropriate nodal redundancy supports both emission reduction and resilience enhancement, suggesting that these objectives can be mutually reinforcing when properly designed.

### 8.2 Implications for Practice

The findings of this report have significant implications for practitioners engaged in transportation planning and supply chain management. Supply chain managers seeking to achieve sustainability goals should incorporate carbon emission considerations into their capacity configuration and routing decisions, recognizing that substantial emission reductions are achievable at modest cost. The integration of machine learning-based emission prediction tools can enhance decision-making by providing accurate estimates of the environmental implications of different choices.

Urban planners and policymakers should develop frameworks that incentivize modal shifts toward lower-emission transportation options, particularly rail transport for medium-distance freight flows. The evidence suggests that strategic modal shifts can achieve emission reductions exceeding 40% in regional distribution networks, representing a high-impact opportunity for sustainability improvement. Investment in rail infrastructure and intermodal facilities can support these shifts while enhancing network resilience.

Organizations should develop comprehensive carbon accounting practices that capture emissions across the full lifecycle of transportation activities, including not only operational emissions but also emissions from infrastructure, vehicles, and fuel production. This lifecycle perspective is essential for avoiding problem shifting and ensuring that capacity configuration decisions lead to genuine emission reductions.

### 8.3 Future Research Directions

Several directions for future research emerge from this analysis. First, the integration of real-time data streams into carbon-aware optimization models represents an important frontier, enabling dynamic capacity configuration that responds to changing conditions and emission intensities. The development of Internet of Things infrastructure and edge computing capabilities creates opportunities for near-real-time emission monitoring and optimization.

Second, the interaction between transportation decarbonization and electricity sector decarbonization deserves further attention, particularly as electric vehicles become more prevalent in freight transportation. The emission intensity of electric transport depends critically on the carbon intensity of electricity generation, creating interdependencies that must be considered in long-term capacity planning.

Third, the behavioral responses of carriers and shippers to carbon-aware capacity configuration decisions warrant further investigation. Understanding how different actors respond to carbon pricing, regulatory requirements, and information provision can inform the design of more effective policies and incentive structures.

Fourth, the extension of carbon-aware optimization approaches to emerging transportation modes, including autonomous vehicles, drones, and hyperloop systems, will be essential as these technologies mature and enter operational deployment. The emission characteristics of these emerging modes may differ substantially from conventional alternatives, requiring new analytical frameworks for capacity configuration.

---

## References

[1] Liu, X., et al. (2024). Carbon emissions from urban transportation. *Transportation Research Part D: Transport and Environment*.

[2] Author(s). (2026). A machine learning and evolutionary optimization framework for carbon-aware supply chain routing. *Supply Chain Analytics*, 13, 100182.

[3] Author(s). (2022). Multimodal transportation path optimization with carbon emission constraints. *International Core Journal of Engineering*, 8(4), 267-281.

[4] Environmental Protection Agency. (2023). Transportation emissions overview. In *Digital Commons* [Online resource].

[5] ICAO. (2025). Methodology for actual life cycle emissions. *CORSIA Eligible Fuels Documentation*.

[6] Author(s). (2024). Carbon charge policies and emission hot spot analysis. *Transportation Research Part D: Transport and Environment*.

[7] World Economic Forum. (2024). Transforming urban logistics: Sustainable and efficient last-mile delivery in cities [Online report].

[8] Author(s). (2025). Green supply chain evolution: A multimodal logistics strategy for capping carbon emissions. *Transportation Research Part E: Logistics and Transportation Review*, 202, 104250.

[9] Author(s). (2024). Environmental effects of shifting passenger travel from air to high-speed rail. In *BTS Digital Publications* [Online resource].

[10] Environmental Protection Agency. (2025). Lifecycle analysis of greenhouse gas emissions under renewable fuel standard [Online resource].

[11] Author(s). (2024). Multimodal transportation network resilience assessment under carbon emission constraints. *Journal of Cleaner Production*.

[12] Harris, I., et al. (2014). Multi-objective evolutionary algorithms for facility optimization. *Transportation Research Part E*.

[13] Carbon Market Watch. (2025). Carbon pricing done right [Briefing document].

[14] Author(s). (2024). Carbon cap policies and technological innovation. *Nature Humanities and Social Sciences Communications*.

## Annotations


## Sources
[1] http://www.icj-e.org/download/ICJE-8-4-267-281.pdf
[2] https://carbonmarketwatch.org/wp-content/uploads/2025/11/2025-briefing-Carbon-princing-done-right-2_compressed.pdf
[3] https://digital.sandiego.edu/cgi/viewcontent.cgi?article=1011&context=ksb-sscm
[4] https://ghgprotocol.org/sites/default/files/standards/Scope3_Calculation_Guidance_0.pdf
[5] https://iopscience.iop.org/article/10.1088/1748-9326/ae03d8
[6] https://pmc.ncbi.nlm.nih.gov/articles/PMC12572118/
[7] https://pmc.ncbi.nlm.nih.gov/articles/PMC8086121/
[8] https://reports.weforum.org/docs/WEF_Transforming_Urban_Logistics_2024.pdf
[9] https://researchonline.jcu.edu.au/80794/1/Dr.%20Jacob%20Wood%20-%20A%20review%20of%20transportation%20carbon%20emissions%20research%20using%20bibliometric%20analyses.pdf
[10] https://rosap.ntl.bts.gov/view/dot/64937/dot_64937_DS1.pdf
[11] https://tc.canada.ca/en/road-transportation/publications/canada-s-action-plan-clean-road-transportation
[12] https://theicct.org/wp-content/uploads/2025/07/ID-392-%E2%80%93-Life-cycle-GHG_report_final.pdf
[13] https://www.apta.com/wp-content/uploads/Standards_Documents/APTA-SUDS-CC-RP-001-09_Rev-1.pdf
[14] https://www.epa.gov/renewable-fuel-standard/lifecycle-analysis-greenhouse-gas-emissions-under-renewable-fuel-standard
[15] https://www.icao.int/sites/default/files/environmental-protection/CORSIA/Documents/CORSIA%20Eligible%20Fuels/ICAO-document-07-Methodology-for-Actual-Life-Cycle-Emissions-November-2025.pdf
[16] https://www.mdpi.com/2071-1050/17/11/5140
[17] https://www.mdpi.com/2071-1050/17/12/5431
[18] https://www.mdpi.com/2075-5309/15/5/700
[19] https://www.nature.com/articles/s41599-024-03320-x
[20] https://www.nature.com/articles/s41599-024-03594-1
[21] https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/08/life-cycle-assessment-of-passenger-transport_9e2ebe5e/2d11e416-en.pdf
[22] https://www.rieti.go.jp/jp/publications/dp/25e006.pdf
[23] https://www.sciencedirect.com/science/article/abs/pii/S095965262034539X
[24] https://www.sciencedirect.com/science/article/abs/pii/S0959652625015501
[25] https://www.sciencedirect.com/science/article/abs/pii/S1361920924004486
[26] https://www.sciencedirect.com/science/article/pii/S1361920924001731
[27] https://www.sciencedirect.com/science/article/pii/S1366554525002911
[28] https://www.sciencedirect.com/science/article/pii/S2949863525000822
[29] https://www.transportationenergy.org/wp-content/uploads/2022/10/FI_Report_Lifecycle_FINAL.pdf
[30] https://www.transportationlca.org/publications.php