# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** b7758222 | **Time:** 170.91s | **Cost:** $0.08377
--------------------------------------------------------------------------------

# The Impact of Asymmetric Transport Delay Distribution on Response Resilience of Inventory Allocation

## Abstract

This research report examines the relationship between asymmetric transport delay distributions and the response resilience of inventory allocation systems within contemporary supply chains. Drawing upon recent scholarly literature and industry analyses, this study investigates how skewed lead time distributions—characterized by extended tails and unpredictable disruption patterns—fundamentally alter the dynamics of inventory management and allocation decisions. The analysis reveals that asymmetric delay distributions create systemic vulnerabilities that traditional symmetric-focused inventory models fail to adequately address, necessitating the development of adaptive, real-time responsive systems capable of handling compounding disruption scenarios. The findings suggest that organizations must transition from static contingency planning toward dynamic, data-driven allocation strategies that account for the inherent asymmetry and variability present in modern global supply chain networks.

## 1. Introduction

The contemporary landscape of global supply chain management has undergone profound transformation in recent years, driven by an unprecedented convergence of disruptive events ranging from pandemic-related disruptions to geopolitical tensions and climate-induced delays. Traditional supply chain resilience strategies, which historically relied upon symmetric assumptions about delay distributions and predictable recovery patterns, have proven increasingly inadequate in addressing the complex, multi-node disruptions characterizing modern supply chain environments [1]. This inadequacy stems fundamentally from a critical oversight: the assumption that transport delays follow symmetric, well-behaved statistical distributions that can be modeled using conventional approaches.

Asymmetric transport delay distributions represent a significant departure from traditional modeling assumptions. Unlike symmetric distributions where deviations from the mean are equally likely in both directions, asymmetric distributions exhibit pronounced skewness, with extended tails representing rare but consequential delay events that can cascade throughout the supply network [3]. The presence of such asymmetry presents substantial challenges for inventory allocation, as standard optimization models built upon symmetric assumptions systematically underestimate the probability and impact of extreme delay scenarios. Research has demonstrated that limited numbers of products or routes are responsible for disproportionately large volumes of delays, creating concentration risks that traditional inventory models fail to capture adequately [3].

The automotive sector's experience during the 2021 semiconductor shortages provides compelling evidence of these dynamics. Automakers across Europe had anticipated chip-related disruptions to be short-lived, planning recovery based on typical contingency expectations grounded in symmetric delay assumptions. In reality, many factories faced weeks of unexpected downtime that far exceeded these forecasts, with entire production lines at major brands slowing or halting entirely [1]. This scenario demonstrates that even well-prepared contingency plans collapse when multiple supplier failures coincide and delay distributions exhibit significant asymmetry.

This report synthesizes current research and industry findings to provide a comprehensive analysis of how asymmetric transport delay distributions impact inventory allocation resilience. The investigation encompasses both the theoretical foundations of asymmetric delay modeling and the practical implications for supply chain practitioners seeking to enhance their organizations' adaptive capabilities.

## 2. Theoretical Framework: Understanding Asymmetric Delay Distributions

### 2.1 Statistical Characteristics of Asymmetric Transport Delays

Transport delay distributions in global supply chains rarely conform to the normal or symmetric distributions assumed in traditional inventory models. Instead, empirical evidence consistently reveals distributions with pronounced right-skewness, characterized by a concentration of relatively minor delays coupled with an extended right tail representing infrequent but severe disruption events [3]. This asymmetry has profound implications for risk assessment and inventory allocation decisions.

The mathematical characterization of asymmetric delay distributions requires moving beyond simple mean and variance metrics to incorporate higher-order moments that capture skewness and kurtosis. Let $L$ represent the transport delay random variable with probability density function $f(l)$. For asymmetric distributions, the relationship between mean ($\mu$), median ($m$), and mode ($mo$) deviates from the equality observed in symmetric distributions:

$$\mu > m > mo$$

for right-skewed distributions commonly observed in supply chain contexts. The presence of extended tails—formally captured through the tail index or through comparison of upper and lower tail decay rates—indicates that extreme delay events occur with non-negligible probability despite their infrequency.

Research examining supply chain delays has specifically identified the presence of distributions with extended tails, suggesting that a limited number of products or routes are responsible for disproportionately large delay volumes [3]. This concentration phenomenon compounds the challenges of asymmetric modeling, as the tail events are not merely statistical abstractions but represent identifiable concentration risks within the supply network. The practical implication is that inventory allocation strategies must account for the possibility of simultaneous, correlated delay events affecting multiple high-risk routes or products.

### 2.2 The Failure of Traditional Optimization Under Asymmetry

Mathematical optimization in supply chain contexts traditionally relies upon objective functions and constraints that assume well-behaved, symmetric delay distributions [5]. The basic optimization framework involves an objective function $f(x)$ representing the output to be maximized or minimized, with variables $x$ representing controllable inputs. When delay distributions are asymmetric, the fundamental assumptions underlying these optimization models become problematic.

Traditional inventory optimization models typically minimize expected costs subject to service level constraints, with costs calculated based on expected holding costs, shortage costs, and ordering costs. Under symmetric delay assumptions, these expectations can be computed using standard formulas that converge appropriately as more data becomes available. However, when delay distributions exhibit significant asymmetry, the expected value becomes increasingly dominated by tail events, and the variance of cost estimates increases substantially [8].

The challenge is compounded by the distinction between static and dynamic optimization problems [5]. Static problems assume fixed delay distributions that do not change over time, while dynamic problems require continual adjustments as new information becomes available. Asymmetric delay distributions are inherently dynamic, as the parameters governing the distribution may shift in response to changing global conditions, regulatory environments, and network configurations. This dynamism means that optimization solutions derived under static assumptions rapidly become suboptimal as the underlying distribution evolves.

Furthermore, the distinction between deterministic and stochastic problems becomes critical in asymmetric contexts [5]. Deterministic models assume specific causes produce specific effects, while stochastic models incorporate randomness and probability. Asymmetric delay distributions are fundamentally stochastic phenomena, requiring probabilistic treatment that accounts for the non-negligible probability of extreme events. Traditional deterministic models systematically underestimate the true cost of delay risk by failing to adequately weight tail events.

## 3. Impact Mechanisms: How Asymmetry Degrades Resilience

### 3.1 Bullwhip Effect Amplification

Asymmetric transport delay distributions significantly amplify the bullwhip effect in supply chains, wherein small fluctuations in demand or supply propagate with increasing magnitude through successive echelons of the supply network. Research has documented that lead time variability—particularly when characterized by asymmetric distributions—substantially increases the bullwhip effect compared to equivalent levels of symmetric variability [8].

The mechanism of amplification operates through the information distortion created by asymmetric delays. When upstream echelons experience delay distributions with extended right tails, downstream echelons receive delayed and distorted demand signals. The asymmetry means that positive demand shocks (requiring increased inventory) are more likely to encounter severe delays than negative demand shocks (requiring decreased inventory), creating a systematic bias toward over-ordering and inventory accumulation. This bias is reinforced when organizations attempt to buffer against delay uncertainty by increasing safety stock levels, thereby exacerbating the bullwhip effect through their own protective responses.

The optimization of inventory policies under asymmetric delay conditions requires consideration of both the mean and variance of lead time distributions, with research demonstrating that performance measures depend much more on the means of on-time and off-time distributions than on their specific types [8]. However, this finding must be qualified by the recognition that asymmetric distributions create situations where the "on-time" and "off-time" states themselves have fundamentally different distributional properties, violating the assumptions underlying many analytical results.

### 3.2 Service Level Degradation

Asymmetric delay distributions systematically degrade service level performance in inventory allocation systems. Research examining the relationship between lead time variability and fulfillment rates has established robust associations between delay characteristics and inventory outcomes, with asymmetric variability creating more severe service level impacts than equivalent symmetric variability [3].

The service level degradation mechanism operates through several interconnected pathways. First, the extended right tail of asymmetric delay distributions creates a non-negligible probability of extremely long delays that exhaust conventional safety stock buffers. While these extreme events may be rare, their impact on service levels is disproportionate to their probability because they affect multiple orders simultaneously and create cascading backorders. Second, the asymmetry means that the relationship between safety stock levels and service levels becomes non-linear, with diminishing returns to safety stock investment occurring at lower levels than would be predicted under symmetric assumptions.

The presence of asymmetry also complicates the determination of appropriate service level targets. Traditional approaches assume that service level requirements can be specified independently of the underlying delay distribution, with safety stock calculated to achieve the target service level given the distribution's parameters. Under asymmetric conditions, the relationship between safety stock and service level becomes distribution-dependent in ways that may not be transparent to practitioners, leading to systematic underestimation of required safety stock levels.

### 3.3 Allocation Inefficiency and Stockout Concentration

Asymmetric delay distributions create systematic inefficiencies in inventory allocation across multiple stocking locations or echelons. When delay distributions are asymmetric, the optimal allocation of limited inventory resources shifts away from the proportional allocation implied by symmetric models toward allocations that provide greater protection against tail events [9].

The inefficiency manifests through the concentration of stockout risk in specific locations or time periods. Under asymmetric delay conditions, delays tend to cluster around particular routes, products, or time periods, creating localized shortages even when aggregate inventory levels appear adequate. This concentration effect is particularly pronounced when organizations employ common suppliers or transportation modes across multiple product lines, as asymmetric delays affecting a shared resource simultaneously impact multiple inventory positions.

Research on inventory management for products with asymmetric cost structures has demonstrated that traditional approaches failing to account for asymmetry can result in total cost increases of over 45% and service level decreases exceeding 17% compared to asymmetric-aware approaches [9]. These findings underscore the practical significance of asymmetry in inventory allocation decisions and highlight the potential for substantial performance improvements through asymmetry-aware modeling.

## 4. Adaptive Response Mechanisms

### 4.1 Real-Time Visibility and Dynamic Reallocation

The limitations of static contingency planning in addressing asymmetric delay distributions have prompted organizations to develop adaptive supply chain capabilities centered on real-time visibility and automated decision-making [1]. These adaptive systems detect regulatory risks, congestion, and quality issues across transportation corridors, enabling networks to re-route shipments, reassign carriers, and ensure cross-border compliance within hours rather than the days required by traditional planning processes.

The value of real-time visibility in addressing asymmetric delays stems from its ability to detect emerging delay patterns before they fully materialize. Asymmetric delay distributions are characterized by precursory signals—early indicators of developing disruptions that, if detected and acted upon promptly, can substantially mitigate the ultimate impact. Real-time visibility systems that monitor transportation status, border conditions, and carrier performance can identify these precursory signals and trigger proactive reallocation of inventory before delays become severe.

Dynamic reallocation capabilities complement visibility by enabling rapid response to detected delay patterns. When asymmetric delays begin to materialize along particular routes, systems with dynamic reallocation capability can shift pending orders to alternative routes or sources, rebalance inventory across locations, and adjust production schedules to account for revised arrival times. This dynamic capability is essential because the asymmetric nature of delays means that static allocation plans rapidly become suboptimal as delay patterns evolve.

### 4.2 Optimization Under Uncertainty

Addressing asymmetric delay distributions requires optimization approaches that explicitly account for distributional asymmetry rather than relying on symmetric approximations. Multi-stage stochastic programming approaches have been developed to model the effect of disruptions on supply chain capacity while incorporating asymmetric delay distributions [8]. These approaches recognize that the optimal inventory allocation strategy depends on the specific characteristics of the delay distribution, not merely its mean and variance.

The development of risk-measurement policies that account for asymmetric risk profiles represents a significant advance in this area. Rather than optimizing solely for expected cost minimization, these approaches incorporate risk measures such as value-at-risk or conditional value-at-risk that explicitly weight tail events according to their severity. Computational results demonstrate that such approaches yield more resilient network configurations than expected-cost minimization alone, particularly when delay distributions exhibit pronounced asymmetry [8].

The integration of machine learning methods with optimization frameworks offers additional promise for handling asymmetric delay distributions. Research has demonstrated that machine learning approaches can improve the precision of predictive models, particularly in complex situations involving extensive datasets with significant variability [3]. These methods can identify non-linear relationships between delay indicators and outcomes that traditional statistical approaches may miss, enabling more accurate characterization of asymmetric delay distributions and their impacts.

### 4.3 Strategic Buffer Stock Optimization

The recognition that asymmetric delay distributions require enhanced protection against tail events has renewed attention to strategic buffer stock optimization. While lean inventory approaches remain appropriate for stable conditions, today's volatile environment necessitates strategic buffer stock for critical items to mitigate the risk of stockouts caused by unpredictable lead times and transportation disruptions [10].

The optimization of buffer stock levels under asymmetric delay conditions requires moving beyond simple service level targets to incorporate the full distributional characteristics of delays. Research indicates that effective buffer stock optimization should consider the specific shape of the delay distribution, including its skewness and tail characteristics, rather than relying solely on mean and variance [8]. This approach ensures that buffer stocks are calibrated to provide adequate protection against the specific delay risks facing the organization rather than the average risks implied by symmetric models.

The classification of inventory using approaches such as ABC analysis enables differentiated buffer stock strategies that allocate protection resources efficiently across product portfolios [10]. Class A items representing the critical 20% of inventory value typically warrant the most rigorous protection against asymmetric delays, while less critical items may be adequately served by simpler periodic review approaches. This differentiated approach ensures that limited buffer stock resources are deployed where they provide the greatest resilience benefit.

## 5. Mitigation Strategies and Implementation Considerations

### 5.1 Supply Chain Diversification

Supply chain diversification represents a fundamental strategy for mitigating the impact of asymmetric delay distributions on inventory allocation resilience. By reducing dependence on any single supplier, carrier, or transportation route, organizations decrease the probability that asymmetric delays affecting a particular node will simultaneously impact multiple inventory positions [4].

The implementation of diversification strategies requires careful consideration of the correlation structure of delay distributions across potential alternatives. Simply adding additional suppliers or routes is insufficient if the delay distributions across these alternatives are highly correlated, as asymmetric delays affecting the primary supplier may simultaneously affect backup options. Effective diversification requires identification of alternatives with low delay correlation, which may involve geographic diversification, modal diversification, or sourcing from suppliers operating in different regulatory or environmental contexts.

The coordination of diversified supply chains introduces additional complexity that must be managed through enhanced collaboration and information sharing [6]. Success in today's environment depends on the ability to think of vendors and suppliers as collaborators, with businesses at every step along the supply chain working together to address issues of availability, timing, and cost. This collaborative approach enables more effective utilization of diversified supply chain configurations, as information about delay conditions across multiple alternatives can be shared and acted upon in real time.

### 5.2 Lead Time Policy Optimization

The optimization of lead time policies represents a critical lever for enhancing resilience to asymmetric delay distributions. Research has demonstrated that lead time policies significantly impact supply chain performance under stochastic and asymmetric conditions [8]. Organizations can reduce the responsiveness risk inherent in asymmetric delays by implementing policies that provide greater control over lead time variability.

Lead time policy optimization may involve multiple mechanisms, including the establishment of preferred carrier programs with guaranteed service levels, the implementation of expedited shipping options for critical items, and the negotiation of flexible lead time contracts that provide suppliers with greater scheduling flexibility. Each of these mechanisms reduces the effective asymmetry of the delay distribution by truncating the right tail or reducing its probability mass.

The coordination of lead time policies across supply chain echelons is essential for achieving optimal resilience benefits. Research on supply chain coordination with controllable lead time has demonstrated that coordination mechanisms can significantly improve system-wide performance compared to independently optimized echelon-level policies [8]. This coordination is particularly important when delay distributions exhibit asymmetry, as uncoordinated policies may inadvertently create bottlenecks that concentrate delay risk at particular echelons.

### 5.3 Information Visualization and Risk Understanding

The literature consistently identifies information visualization and risk understanding as critical factors contributing to supply chain resilience in the face of asymmetric delays [2]. The complexity of asymmetric delay distributions makes intuitive understanding difficult, necessitating visualization tools that can effectively communicate the nature and implications of distributional asymmetry.

Effective visualization of asymmetric delay distributions requires presentation of distributional shape beyond simple summary statistics. Box plots, density plots, and cumulative distribution function representations enable practitioners to直观地理解 the skewness and tail characteristics that drive resilience impacts [3]. These visualizations support better decision-making by making abstract distributional properties concrete and comparable across different routes, products, or time periods.

The understanding and dealing with risks associated with asymmetric delays requires not only visualization but also analytical frameworks that connect delay characteristics to operational impacts [2]. Organizations that develop such frameworks—mapping delay distributions to inventory requirements, service level projections, and cost implications—position themselves to make more informed decisions about resilience investments and operational responses.

## 6. Case Analysis: Compound Disruption Scenarios

### 6.1 The COVID-19 Pandemic and Asymmetric Delay Dynamics

The COVID-19 pandemic provides a compelling case study of asymmetric delay dynamics in practice. The pandemic caused widespread disruptions including lockdowns, factory closures, labor shortages, and transportation bottlenecks that affected supply chains across electronics, automotive, and consumer goods sectors [4]. The asymmetric nature of these disruptions—affecting some routes and products severely while leaving others relatively untouched—created challenges that static contingency plans were fundamentally unable to address.

The pandemic's impact on transport delays was characterized by extreme asymmetry. While some transportation lanes experienced severe, extended delays, others remained relatively functional. Organizations with visibility and adaptive capabilities were able to shift operations toward less-affected lanes, while those relying on static plans found themselves trapped in severely disrupted routes. The extended duration of the pandemic's impact—far exceeding typical contingency planning horizons—further underscored the inadequacy of symmetric delay assumptions that implicitly assumed disruptions would be short-lived.

The pandemic also demonstrated the compounding effect of multiple simultaneous disruptions on asymmetric delay distributions. When multiple disruption events coincide, the resulting delay distribution exhibits even greater asymmetry than any individual disruption would produce, with the combined effect dominated by the worst-case scenarios from each individual disruption. This compounding effect explains why even well-prepared contingency plans collapsed when multiple supplier failures coincided during the pandemic [1].

### 6.2 The Suez Canal Blockage: A Natural Experiment in Asymmetric Delay

The six-day blockage of the Suez Canal in March 2021 provided a natural experiment in asymmetric delay dynamics [4]. The blockage caused a massive ship traffic jam and delays in the delivery of goods worldwide, with the impact highly asymmetric across products, origins, and destinations.

Products and companies with supply chains heavily dependent on the Suez route experienced extreme delays that far exceeded typical contingency expectations, while those with alternative routing options experienced relatively modest impacts. This asymmetry highlighted the importance of route diversification and the dangers of concentration risk in transportation networks. Organizations that had invested in visibility and alternative routing capabilities were able to adapt relatively quickly, while those with limited visibility and no established alternatives faced extended disruptions.

The Suez Canal blockage also demonstrated the cascading nature of asymmetric delays through supply networks. Delays at the canal propagated backward through supply chains, affecting production schedules, inventory positions, and downstream deliveries in complex patterns that were difficult to predict using traditional planning tools. The extended tail of the delay distribution—representing the most severely affected shipments—created backlogs that took weeks to clear even after the canal reopened.

## 7. Implications for Practice

### 7.1 Assessment of Delay Distribution Asymmetry

Organizations seeking to enhance resilience to asymmetric delays should begin with systematic assessment of their current delay distributions. This assessment should move beyond calculation of mean and variance to characterize the full distributional shape, including skewness measures and tail behavior. The presence of significant asymmetry should trigger enhanced attention to tail risk protection and adaptive response capabilities.

The assessment should examine delay distributions at multiple levels of granularity, including overall network delays, route-specific delays, product-specific delays, and time-period-specific delays. Asymmetry may be present at some levels of aggregation while absent at others, and understanding this heterogeneity enables more targeted resilience investments. For example, overall network delays may appear relatively symmetric while specific high-risk routes exhibit pronounced asymmetry requiring specialized protection strategies.

### 7.2 Investment Priorities for Asymmetric Delay Resilience

Based on the analysis presented in this report, organizations should prioritize investments in several areas to enhance resilience to asymmetric delay distributions. First, real-time visibility capabilities enable early detection of developing delays and provide the information foundation for adaptive response. Second, dynamic allocation systems enable rapid reallocation of inventory in response to detected delay patterns, moving beyond static allocation plans toward continuous optimization. Third, buffer stock optimization should account for distributional asymmetry, ensuring that protection levels are calibrated to actual delay risks rather than symmetric approximations.

The relative priority of these investments should be determined based on the specific characteristics of the organization's supply chain and the degree of asymmetry present in current delay distributions. Organizations with highly asymmetric delay distributions should prioritize tail risk protection through enhanced buffer stocks and diversification, while those with moderate asymmetry may achieve greater benefit from visibility and dynamic response capabilities.

### 7.3 Organizational and Process Considerations

Technical capabilities must be supported by appropriate organizational structures and processes to achieve full resilience benefits. The shift from static to adaptive supply chain management requires changes in decision-making authority, information sharing practices, and performance measurement systems [6]. Organizations must empower personnel to make rapid allocation decisions based on real-time information, rather than requiring approval through hierarchical processes that introduce delays incompatible with the speed of asymmetric disruption dynamics.

Collaboration with supply chain partners is essential for effective response to asymmetric delays [6]. Information sharing about delay conditions, capacity availability, and alternative options enables coordinated responses that are more effective than independent actions. Organizations should establish collaborative relationships with key suppliers and logistics partners that facilitate rapid information exchange and coordinated decision-making.

## 8. Conclusion

Asymmetric transport delay distributions represent a fundamental challenge for inventory allocation resilience in contemporary supply chains. The extended tails and skewed characteristics of these distributions create risks that traditional symmetric-focused inventory models systematically underestimate, leading to inadequate protection against tail events and degraded service level performance. The compounding nature of modern disruptions—wherein multiple asymmetric delay events coincide—further amplifies these risks, rendering static contingency plans increasingly inadequate.

The evidence examined in this report supports several key conclusions. First, organizations must develop capabilities to characterize and model asymmetric delay distributions, moving beyond mean and variance to capture distributional shape and tail behavior. Second, adaptive systems incorporating real-time visibility and dynamic allocation capabilities are essential for responding effectively to asymmetric delays, as static plans cannot accommodate the rapid evolution of delay patterns. Third, strategic investments in buffer stock optimization, supply chain diversification, and lead time policy management should be calibrated to the specific asymmetry characteristics of the organization's delay distributions.

The transition from traditional resilience strategies to adaptive supply chain management represents a fundamental shift in approach that extends beyond tactical adjustments to encompass organizational capabilities, collaborative relationships, and decision-making processes. Organizations that successfully make this transition will be positioned to maintain operational continuity and service level performance even in the face of severe, asymmetric disruptions that overwhelm competitors relying on traditional approaches.

The future of supply chain resilience lies in systems that can detect constraints, reallocate in real time, and continuously adapt to evolving conditions [1]. As asymmetric delay distributions become increasingly prevalent in the global supply chain environment, the development of such adaptive capabilities will transition from competitive advantage to operational necessity.

---

## References

[1] SCMR. (2024). Stop Planning for Disruptions Start Building Adaptive Supply Chains. *Supply Chain Management Review*. https://www.scmr.com/article/stop-planning-for-disruptions-start-building-adaptive-supply-chains

[2] WSEAS. (2024). Supply Chain Risk Analysis and Prefabricated Building Supply Chain Resilience. *WSEAS Transactions on Business and Economics*. https://wseas.com/journals/bae/2024/e305107-2788.pdf

[3] ETASR. (2024). Quantitative Examination of Supply Chain Delays, Lead Times, and Inventory Management. *Engineering, Technology & Applied Science Research*. https://etasr.com/index.php/ETASR/article/download/7834/3886/31472

[4] Infor. (2024). Strategies to Mitigate Supply Chain Disruptions. *Infor Blog Series*. https://www.infor.com/blog/strategies-to-mitigate-supply-chain-disruptions

[5] Stanford University. (2024). Mathematical Optimization in the Real World. *Stanford SI12 K12 Optimization Materials*. https://web.stanford.edu/group/sisl/k12/optimization/MO-unit1-pdfs/1.1optimization.pdf

[6] CohnReznick. (2024). 8 Strategies for Supply Chain Resilience. *CohnReznick Insights*. https://www.cohnreznick.com/insights/8-strategies-supply-chain-resilience

[7] ScienceDirect. (2024). Multi-Period Supply Chain Network Design with Stochastic Demands and Disruptions. *Computers & Operations Research*. https://www.sciencedirect.com/science/article/abs/pii/S0305054816301608

[8] ScienceDirect. (2025). Supply Chain Coordination with Controllable Lead Time and Asymmetric Information. *European Journal of Operational Research*. https://www.sciencedirect.com/science/article/pii/S0377221712002063

[9] IJIETAP. (2024). Asymmetrical Cost Structures in Inventory Management for Perishable Products. *International Journal of Industrial Engineering: Theory, Applications and Practice*. https://ijietap.journals.publicknowledgeproject.org/ijietap/index.php/ijie/article/view/10035

[10] Performance SC. (2024). 5 Pillars for End-to-End Supply Chain Resilience Strategies. *Performance Supply Chain Management*. https://performansc.com/news/5-pillars-for-end-to-end-supply-chain-resilience-strategies/

## Annotations


## Sources
[1] https://engineering.lehigh.edu/sites/engineering.lehigh.edu/files/_DEPARTMENTS/ise/pdf/tech-papers/12/12W_005.pdf
[2] https://eprints.whiterose.ac.uk/id/eprint/2557/1/ITS2091-User_equilibrium_traffic_network.pdf
[3] https://etasr.com/index.php/ETASR/article/download/7834/3886/31472
[4] https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=toledo1321426327&disposition=inline
[5] https://hal-emse.ccsd.cnrs.fr/emse-00881470v1/document
[6] https://ijietap.journals.publicknowledgeproject.org/ijietap/index.php/ijie/article/view/10035
[7] https://link.springer.com/article/10.1007/s40171-025-00458-8
[8] https://performansc.com/news/5-pillars-for-end-to-end-supply-chain-resilience-strategies/
[9] https://pmc.ncbi.nlm.nih.gov/articles/PMC10793953/
[10] https://scholarworks.waldenu.edu/cgi/viewcontent.cgi?article=19336&context=dissertations
[11] https://web.stanford.edu/group/sisl/k12/optimization/MO-unit1-pdfs/1.1optimization.pdf
[12] https://wseas.com/journals/bae/2024/e305107-2788.pdf
[13] https://www.britannica.com/science/optimization
[14] https://www.cohnreznick.com/insights/8-strategies-supply-chain-resilience
[15] https://www.iajournals.org/articles/iajpscm_v2_i2_179_205.pdf
[16] https://www.infor.com/blog/strategies-to-mitigate-supply-chain-disruptions
[17] https://www.l2l.com/blog/supply-chain-resilience-strategies
[18] https://www.merriam-webster.com/dictionary/optimization
[19] https://www.rairo-ro.org/articles/ro/pdf/2021/01/ro190171.pdf
[20] https://www.sciencedirect.com/org/science/article/pii/S1040162825000035
[21] https://www.sciencedirect.com/science/article/abs/pii/S0925527316301608
[22] https://www.sciencedirect.com/science/article/abs/pii/S0925527317303225
[23] https://www.sciencedirect.com/science/article/pii/S0022199623000740
[24] https://www.sciencedirect.com/science/article/pii/S2667325824003108
[25] https://www.scmr.com/article/stop-planning-for-disruptions-start-building-adaptive-supply-chains
[26] https://www.tandfonline.com/doi/full/10.1080/00207543.2025.2543493
[27] https://www.zhihu.com/question/27047110?sort=created
[28] https://www.zhihu.com/question/425102812