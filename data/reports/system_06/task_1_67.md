# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** d5b51272 | **Time:** 163.20s | **Cost:** $0.20553
--------------------------------------------------------------------------------

# How Base-Stock Policy Parameter Optimization Minimizes Total Cost Relative to Demand Variation Coefficients

## A Technical Research Report

---

## Executive Summary

This research report examines the relationship between base-stock policy parameter optimization and demand variation coefficients in stochastic inventory systems. Base-stock policies represent one of the most fundamental and widely applied inventory control mechanisms in make-to-stock production environments, where the objective is to maintain inventory levels at predetermined target positions while minimizing the total costs associated with inventory holding and stockouts. The optimization of base-stock levels becomes particularly critical when demand exhibits stochastic variability, as the coefficient of variation serves as a key determinant of both the optimal policy parameters and the resulting cost performance.

The analysis reveals that increased demand variability, as measured by the coefficient of variation, systematically drives upward adjustments in optimal base-stock levels. This relationship emerges from the fundamental trade-off between inventory holding costs and backordering costs, where higher variability necessitates greater safety stock to achieve equivalent service levels. The research demonstrates that when demand inter-arrival distributions are ordered in a stochastic sense, increased arrival time variability leads to an augmentation of optimal base-stock levels and a corresponding increase in optimal inventory-related costs [1]. Furthermore, the coefficient of variation of demand during lead time and review periods serves as a critical indicator for determining the sensitivity of total costs to changes in various parameters, including lead time mean and variance [2].

This report synthesizes analytical findings, numerical evidence, and practical implications to provide a comprehensive understanding of how organizations can optimize base-stock policies to minimize total costs in the presence of demand uncertainty. The findings have significant implications for supply chain management, inventory planning, and operational decision-making in environments characterized by stochastic demand patterns.

---

## 1. Introduction

### 1.1 Background and Context

Inventory management under stochastic demand represents one of the most challenging problems in operations research and supply chain management. Organizations must balance the competing objectives of maintaining sufficient stock to meet customer demand while avoiding excessive inventory holdings that tie up capital and increase storage costs. This fundamental trade-off becomes particularly pronounced in make-to-stock production systems, where finished goods inventory serves as a buffer between production capacity and uncertain customer demand.

The base-stock policy has emerged as a canonical approach for managing inventory in such settings. Under this policy, the inventory position is continuously monitored, and orders are placed to bring the position up to a predetermined base-stock level whenever demand depletes the inventory below this threshold [3]. The elegance of the base-stock policy lies in its structural simplicity combined with its remarkable optimality properties across a wide range of inventory system configurations. Research has demonstrated that dynamic programming approaches yield optimal base-stock policies in numerous settings, including models with correlated demand and forecast evolution [4].

The optimization of base-stock policy parameters, particularly the determination of the optimal base-stock level, constitutes a central problem in inventory theory. When the objective is to minimize inventory holding and backordering costs, the optimization reduces to finding the base-stock level that balances these competing cost components [1]. The complexity of this optimization task varies significantly depending on the underlying modeling assumptions, ranging from closed-form analytical solutions in simple settings to computationally intensive simulation-based approaches in more complex environments.

### 1.2 Problem Statement

The central question addressed in this report concerns the relationship between base-stock policy parameter optimization and demand variation coefficients. Specifically, how does the coefficient of variation of demand influence the optimal base-stock level, and how does this relationship translate into effects on total inventory costs? Understanding this relationship is crucial for organizations seeking to implement effective inventory management strategies in the presence of demand uncertainty.

The coefficient of variation, defined as the ratio of the standard deviation to the mean of demand, provides a standardized measure of demand variability that enables comparison across different products, time periods, and organizational contexts. This metric plays a pivotal role in inventory optimization because it captures the relative variability of demand independent of the absolute demand level, making it particularly useful for characterizing the difficulty of inventory management across different product categories [5].

### 1.3 Research Objectives

This report pursues several interconnected objectives. First, it establishes the theoretical foundations of base-stock policy optimization in stochastic inventory systems. Second, it examines how demand variability, as measured by the coefficient of variation, affects the optimal base-stock level and the resulting cost performance. Third, it synthesizes numerical evidence from multiple sources to quantify these effects. Fourth, it derives practical implications for inventory management and supply chain optimization.

---

## 2. Theoretical Framework

### 2.1 Base-Stock Policy Fundamentals

The base-stock policy, also known as the order-up-to policy, represents a continuous review inventory control mechanism where the inventory position is maintained at a constant target level. Let $S$ denote the base-stock level, which represents the order-up-to position. Under this policy, whenever a demand event occurs, an order is placed to immediately replenish the inventory position back to level $S$ [6]. This mechanism ensures that the inventory position remains constant over time, with actual inventory levels fluctuating based on the relationship between demand arrivals and production completions.

In a single-item, single-stage production/inventory system operating in make-to-stock mode, the base-stock policy drives inventories toward a predetermined target level [1]. The policy can be formally characterized as follows: if the inventory position at the beginning of period $t$ is denoted by $x_t$, and the optimal base-stock level for that period is $R(f_t)$, where $f_t$ represents the available information set, then the optimal action is to order up to $R(f_t)$ whenever $x_t < R(f_t)$ and to order nothing otherwise [4]. This structure ensures that the inventory position is maintained at or above the target level while minimizing ordering costs.

The base-stock policy is particularly well-suited for environments with stochastic demand because it automatically adapts to demand realizations by triggering replenishment orders in response to demand occurrences. The policy's simplicity facilitates implementation and monitoring while its optimality properties ensure cost-effective inventory management under appropriate conditions.

### 2.2 Cost Structure in Inventory Systems

The total cost in base-stock controlled inventory systems comprises several components that must be balanced to achieve optimal performance. The primary cost elements include inventory holding costs, backordering or stockout costs, and in some cases, ordering or setup costs. The structure of these costs and their relative magnitudes significantly influence the optimal base-stock level.

The inventory holding cost, typically denoted by $h$, represents the cost of maintaining one unit of inventory over a specified time period. This cost encompasses storage expenses, capital carrying costs, insurance premiums, and obsolescence risks. The backordering cost, often denoted by $b$ or $\pi$, represents the cost associated with unmet demand, including lost sales, customer goodwill erosion, and emergency fulfillment expenses. The trade-off between these cost components forms the foundation of base-stock optimization.

The total cost function for a base-stock controlled system can be expressed as:

$$TC(S) = h \cdot E[I(S)] + b \cdot E[B(S)]$$

where $E[I(S)]$ represents the expected inventory level and $E[B(S)]$ represents the expected backorder level under base-stock level $S$. The optimal base-stock level $S^*$ minimizes this total cost function, balancing the increasing holding cost component against the decreasing backorder cost component as $S$ increases.

Research has extended this basic cost structure to incorporate more sophisticated objectives. For instance, studies have examined the minimization of total cost Conditional Value-at-Risk (CVaR) in make-to-stock systems, developing approximations for optimal base-stock levels under risk-averse objectives [7]. This extension recognizes that decision-makers may be concerned not only with expected costs but also with the distribution of potential cost outcomes, particularly the tail risks associated with high-cost scenarios.

### 2.3 Demand Variability and the Coefficient of Variation

The coefficient of variation (CoV) provides a standardized measure of dispersion that enables meaningful comparisons of variability across different contexts. For demand during a specified time period, the coefficient of variation is defined as:

$$CoV_D = \frac{\sigma_D}{\mu_D}$$

where $\sigma_D$ represents the standard deviation of demand and $\mu_D$ represents the mean demand. This dimensionless ratio expresses variability as a proportion of the mean, facilitating comparisons between products or time periods with different average demand levels.

The coefficient of variation plays a crucial role in inventory optimization because it captures the relative uncertainty in demand that directly impacts safety stock requirements. Higher coefficients of variation indicate greater demand uncertainty, which necessitates larger safety stocks to maintain specified service levels. Research has demonstrated that the coefficient of variation of demand during lead time and review periods serves as a useful indicator for determining whether total cost is more sensitive to changes in lead time mean or lead time variance [2].

The relationship between coefficient of variation and inventory costs operates through the safety stock mechanism. Safety stock, which represents the inventory buffer maintained to protect against demand variability, is proportional to the standard deviation of demand during the replenishment lead time. When demand variability increases, as reflected in a higher coefficient of variation, the required safety stock increases proportionally, leading to higher holding costs. However, inadequate safety stock results in increased stockout costs, creating the fundamental trade-off that base-stock optimization seeks to resolve.

---

## 3. Base-Stock Policy Optimization

### 3.1 Mathematical Formulation

The optimization of base-stock policy parameters involves finding the base-stock level $S$ that minimizes the expected total cost of inventory management. The mathematical formulation begins with the definition of the cost function and proceeds through the identification of optimality conditions.

Consider a make-to-stock queue with general demand arrival times operated according to a base-stock policy [1]. Let $\lambda$ denote the demand arrival rate and $\rho$ represent the utilization parameter. The cost function incorporates both inventory holding costs and backordering costs, with the optimal base-stock level balancing these competing considerations.

The optimization problem can be formally stated as:

$$\min_S \left\{ h \cdot E[I(S)] + b \cdot E[B(S)] \right\}$$

where the expectations are taken with respect to the demand distribution. The optimality condition for this problem is given by the well-known newsvendor fractile solution:

$$F(S^*) = \frac{b}{b + h}$$

where $F(\cdot)$ represents the cumulative distribution function of demand during the replenishment lead time. This condition states that the optimal base-stock level corresponds to the fractile of the lead-time demand distribution determined by the critical ratio $\frac{b}{b + h}$.

However, this analytical solution applies primarily to simplified settings. In more complex environments characterized by capacitated production, general demand arrival processes, or multi-echelon structures, the optimization must account for additional factors that influence the cost function. Research has shown that in capacitated production settings, the optimal base-stock level depends not only on the cost parameters and demand distribution but also on the production capacity utilization [7].

### 3.2 Optimization Approaches

The optimization of base-stock policy parameters can be approached through several methodologies, each with distinct advantages and limitations depending on the complexity of the underlying system model.

**Analytical Optimization**: In certain simplified settings, closed-form solutions for optimal base-stock levels can be derived. These analytical solutions provide valuable insights into the structure of optimal policies and the relationships between parameters. For instance, in systems with Poisson demand and exponential production times, the optimal base-stock level can be expressed in terms of the system parameters and cost ratios [1]. However, analytical solutions are generally available only for restricted classes of demand and production distributions.

**Numerical Optimization**: When analytical solutions are unavailable, numerical methods can be employed to find optimal or near-optimal base-stock levels. These methods include gradient-based optimization algorithms, grid search procedures, and specialized techniques for stochastic systems. Numerical optimization enables the exploration of optimal policies in more complex settings while providing quantitative results that can guide practical implementation [1].

**Simulation-Optimization**: For highly complex systems where neither analytical nor standard numerical methods are feasible, simulation-optimization approaches combine simulation models with optimization algorithms to identify optimal or approximately optimal policies. Recent research has demonstrated the effectiveness of Monte Carlo Simulation with grid search and Bayesian optimization for inventory management under stochastic demand [8]. These approaches enable the evaluation of different inventory policies, including both periodic review (p, Q) and continuous review (r, Q) configurations, and can identify the optimal reorder quantities that maximize profit while minimizing stockout risks and excessive inventory holdings.

The choice among these approaches depends on several factors, including the complexity of the demand and production processes, the availability of computational resources, and the required precision of the solution. In practice, hybrid approaches that combine analytical insights with numerical refinement often prove most effective.

### 3.3 Structural Properties of Optimal Policies

Research has established important structural properties of optimal base-stock policies that facilitate their implementation and optimization. One of the most significant findings is that optimal base-stock policies exhibit monotonicity properties: the optimal base-stock level is non-decreasing in the cost of stockouts relative to holding costs and non-increasing in the production capacity utilization [1].

In dynamic settings with evolving information, the optimal base-stock policy maintains its fundamental structure while adapting to changing conditions. Dynamic programming analysis has revealed that the optimal policy takes the form of a state-dependent base-stock policy, where the optimal target level in each period is determined by the conditional distribution of future demands given available information [4]. This structure simplifies implementation by reducing the optimization to a series of single-period problems, each requiring the determination of an optimal base-stock level based on current information.

The optimality of base-stock policies has been proven in numerous settings, including models with correlated demand and forecast evolution [4]. This broad applicability underscores the fundamental nature of base-stock policies as optimal solutions to inventory management problems under uncertainty.

---

## 4. Impact of Demand Variation Coefficients on Optimization

### 4.1 Theoretical Relationship Between Variability and Optimal Base-Stock Levels

The relationship between demand variability and optimal base-stock levels represents a fundamental result in inventory theory. When demand inter-arrival distributions are ordered in a stochastic sense, increased arrival time variability leads to an augmentation of optimal base-stock levels [1]. This relationship emerges from the increased uncertainty associated with more variable demand, which necessitates larger inventory buffers to maintain equivalent service levels.

The theoretical foundation for this relationship rests on the convexity of the cost function with respect to the base-stock level. As variability increases, the cost function becomes steeper in the region around the optimal base-stock level, meaning that deviations from the optimal level result in larger cost penalties. This increased sensitivity to suboptimal base-stock levels drives organizations to maintain higher inventory positions when facing more variable demand.

The coefficient of variation serves as the key metric linking demand variability to inventory optimization. Research has demonstrated that the fill rate approximation performs better when the coefficient of variation of demand during lead time and review periods decreases [9]. This finding indicates that lower variability simplifies the optimization problem and improves the accuracy of analytical approximations, while higher variability introduces greater complexity and uncertainty into the optimization process.

### 4.2 Quantification of Variability Effects

The effects of demand variability on optimal base-stock levels and costs can be quantified through both analytical relationships and numerical examples. Analytical results establish the directional relationships, while numerical investigations provide precise magnitudes for specific parameter configurations.

In make-to-stock queue settings, the optimal base-stock level $S^*$ increases with demand variability in a manner that can be characterized through the properties of the underlying demand distribution. When demand inter-arrival times exhibit increased variability, as measured by the coefficient of variation, the optimal base-stock level must be raised to compensate for the greater uncertainty in demand timing and magnitude [1].

The increase in optimal base-stock levels translates directly into higher inventory-related costs. Research has shown that increased arrival time variability leads to a corresponding increase in optimal inventory holding and backordering costs [1]. This cost escalation occurs because higher base-stock levels increase average inventory holdings while the increased variability also affects the distribution of inventory positions and backorder levels.

The total cost variance also exhibits interesting behavior with respect to base-stock level optimization. Research has established that as the base-stock level increases, the asymptotic growth rate of total cost variance first decreases and then increases, tending toward a limit [7]. This non-monotonic relationship suggests the existence of a finite optimal base-stock level that balances not only expected costs but also cost variability, a consideration that becomes particularly relevant for risk-averse decision-makers.

### 4.3 Interaction with Lead Time Variability

The effects of demand variability on base-stock optimization interact significantly with lead time variability, creating a complex landscape of影响因素. Research has demonstrated that both lead time mean and lead time variance influence total costs through their combined effect on the standard deviation of demand during lead time [2].

The total cost function can be expressed to highlight the separate contributions of demand variability and lead time variability:

$$TC = \frac{AD}{Q} + \frac{Qh}{2} + h \cdot k \cdot \sigma_X + \frac{k \cdot \sigma_X^2}{Q}$$

where the terms represent ordering costs, cycle stock holding costs, safety stock holding costs, and the interaction between safety stock and order quantity, respectively [2]. In this formulation, $\sigma_X$ represents the standard deviation of demand during lead time, which depends on both demand variability and lead time variability.

The coefficient of variation of demand, denoted as $\delta_D = \sigma_D / \mu_D$, serves as a useful indicator for determining whether total cost is more sensitive to changes in lead time mean or lead time variance [2]. When the demand coefficient of variation is high, demand variability dominates the cost structure, and organizations should focus their improvement efforts on demand forecasting and variability reduction. Conversely, when the demand coefficient of variation is low, lead time management becomes relatively more important for cost minimization.

---

## 5. Numerical Evidence and Case Studies

### 5.1 Simulation Studies

Numerical investigations provide concrete evidence for the theoretical relationships between demand variability, optimal base-stock levels, and costs. Simulation studies have examined a wide range of parameter configurations to quantify these effects and validate analytical predictions.

Research involving 108 problem instances with different parameter values has found that optimal base-stock levels can be identified through simulation, with the results confirming the theoretical predictions regarding the effects of variability [7]. These simulation durations are representative of practical circumstances where total cost can be evaluated quarterly or annually, providing relevance for real-world implementation.

Monte Carlo Simulation combined with optimization techniques has demonstrated the effectiveness of grid search and Bayesian optimization for inventory management under stochastic demand [8]. Studies comparing periodic review (p, Q) and continuous review (r, Q) inventory policies have found that the (r, Q) policy significantly increases expected profit compared to the (p, Q) policy. This improvement results from the dynamic nature of the continuous review policy, which manages inventory levels based on daily demand and lead time considerations.

The integration of random and conditional sampling techniques in simulation studies has highlighted critical periods of high demand and their impact on optimal inventory policies [8]. These findings emphasize the importance of understanding demand patterns beyond simple variability measures, including the temporal distribution of demand spikes and their implications for inventory positioning.

### 5.2 Empirical Findings

Empirical studies in industrial settings have validated the theoretical relationships between demand variability and inventory performance. Research examining inventory management practices across multiple materials has found that applying optimized stock management models resulted in a 33% cost reduction for the components analyzed [5].

The interaction between product value and demand variability influences the choice of optimal inventory policy. Studies have found that items with low variability (AX items in XYZ analysis) perform better with continuous review Q-models because the required safety stock is lower but sufficient to achieve high service levels [5]. These items require continuous monitoring to provide stock replenishment when needed, avoiding both stockouts and excess inventory.

The coefficient of variation serves as the basis for classifying demand patterns into categories such as steady, variable, erratic, irregular, lumpy, or dead [10]. Each pattern implies different inventory management tactics and actions by supply chain managers. This classification enables organizations to tailor their base-stock optimization approaches to the specific characteristics of different product categories, recognizing that the optimal base-stock level depends not only on aggregate variability measures but also on the underlying demand pattern structure.

### 5.3 Sensitivity Analysis

Sensitivity analysis of optimal base-stock levels against parameter value changes provides valuable insights for inventory planning and management. Research has examined how optimal base-stock levels respond to changes in stockout costs, capacity utilization, and other system parameters [7].

The findings offer strategic directions for management by informing the connections between stockout cost, capacity utilization, and inventory level in the context of inventory planning. Managers can benefit from understanding how changes in one parameter affect the optimal base-stock level and total costs, enabling more informed decision-making regarding inventory investments and service level commitments.

The trade-off between profit and risk should be considered when deciding which optimization method to use. While Bayesian optimization may offer marginal improvement in expected profit compared to grid search, it may also represent a potentially riskier inventory management strategy [8]. This trade-off highlights the importance of considering the full distribution of outcomes, not just expected values, when optimizing base-stock policies under uncertainty.

---

## 6. Managerial Implications

### 6.1 Strategic Inventory Planning

The research findings have significant implications for strategic inventory planning in organizations facing stochastic demand. The positive relationship between demand variability and optimal base-stock levels implies that organizations experiencing highly variable demand must maintain higher inventory investments to achieve equivalent service levels. This relationship should inform budgeting decisions, warehouse capacity planning, and working capital allocation for inventory.

The coefficient of variation provides a useful metric for prioritizing improvement efforts. When the demand coefficient of variation is high, organizations should focus on demand forecasting improvements and variability reduction initiatives. When the coefficient is low, efforts may be more productively directed toward lead time reduction and reliability improvements. This prioritization ensures that improvement resources are allocated to the factors that most significantly impact inventory costs.

The research also highlights the importance of considering cost variability, not just expected costs, in inventory optimization. For risk-averse decision-makers, the optimal base-stock level may differ from the level that minimizes expected costs alone. Understanding the relationship between base-stock levels and cost variance enables organizations to select policies that appropriately balance expected costs against the risk of adverse outcomes.

### 6.2 Policy Selection and Implementation

The choice between different inventory policies should be informed by the characteristics of demand variability. For items with low variability, continuous review policies such as (r, Q) may provide superior performance due to their dynamic response to demand realizations [8]. For items with higher variability, periodic review policies may be more appropriate given their simpler implementation requirements and adequate performance under uncertainty.

The implementation of base-stock policies requires careful attention to the accuracy of demand forecasting and the estimation of variability parameters. The performance of optimized base-stock levels depends critically on the quality of input data and the appropriateness of distributional assumptions. Organizations should invest in demand sensing capabilities and statistical methods that provide reliable estimates of demand variability.

The integration of base-stock policies with broader supply chain planning systems requires coordination across multiple functional areas. Production scheduling, procurement, and distribution decisions must align with inventory policies to achieve system-wide optimization. The structural properties of optimal base-stock policies, including their monotonicity and adaptability, facilitate this integration by providing clear targets for inventory positioning.

### 6.3 Performance Measurement and Continuous Improvement

Organizations should establish performance measurement systems that track both inventory levels and service outcomes relative to optimized base-stock targets. Deviations from optimal base-stock levels indicate either implementation problems or changes in underlying demand characteristics that require policy adjustment.

The coefficient of variation should be monitored over time to detect changes in demand patterns that may necessitate policy updates. Significant increases in variability should trigger reviews of safety stock levels and service level commitments. Conversely, reductions in variability may enable inventory reductions without sacrificing service levels.

Continuous improvement initiatives should focus on the factors that most significantly impact inventory costs given the organization's specific demand characteristics. For many organizations, demand variability represents the dominant cost driver, making demand forecasting improvement and variability reduction high-priority initiatives. For others, lead time management may offer greater improvement potential.

---

## 7. Conclusions and Future Research Directions

### 7.1 Summary of Key Findings

This research report has examined the relationship between base-stock policy parameter optimization and demand variation coefficients in stochastic inventory systems. The analysis has established several key findings that advance understanding of inventory management under uncertainty.

First, base-stock policies represent optimal or near-optimal inventory control mechanisms across a wide range of settings, from simple single-item systems to complex multi-echelon networks. The structural simplicity of these policies facilitates implementation while their theoretical foundations ensure cost-effective inventory management.

Second, demand variability, as measured by the coefficient of variation, has a systematic and predictable effect on optimal base-stock levels. Increased variability necessitates higher base-stock levels to maintain equivalent service levels, with the magnitude of this effect depending on the specific cost parameters and demand characteristics of the system.

Third, the relationship between variability and costs operates through multiple channels, including direct effects on safety stock requirements and indirect effects on cost variance and risk exposure. Organizations must consider both expected costs and cost variability when optimizing base-stock policies under uncertainty.

Fourth, the coefficient of variation serves as a useful indicator for prioritizing improvement efforts and selecting appropriate inventory policies. Organizations can leverage this metric to classify products, allocate resources, and guide strategic decisions regarding inventory investment.

### 7.2 Limitations and Scope

This analysis has focused primarily on single-item, single-stage inventory systems, with extensions to multi-echelon settings where applicable. The relationships established in this report may require modification when applied to more complex systems with multiple products, multiple echelons, or supply chain interdependencies.

The analysis has assumed that demand variability can be characterized through standard distributional assumptions and the coefficient of variation. In practice, demand patterns may exhibit characteristics such as seasonality, trends, or autocorrelation that are not fully captured by simple variability measures. Organizations should complement the analytical framework presented here with demand pattern analysis appropriate to their specific contexts.

The optimization approaches discussed include analytical, numerical, and simulation-based methods, each with distinct requirements and limitations. The applicability of specific approaches depends on the complexity of the system model, the availability of computational resources, and the precision requirements of the application.

### 7.3 Directions for Future Research

Several directions for future research emerge from this analysis. First, the development of more sophisticated models that capture the full complexity of demand patterns, including non-stationarity, seasonality, and demand shocks, would enhance the practical relevance of base-stock optimization research.

Second, the integration of machine learning and advanced forecasting methods with inventory optimization represents a promising research frontier. As organizations accumulate larger volumes of demand data and develop more sophisticated analytical capabilities, the opportunity to leverage these capabilities for improved inventory management continues to expand.

Third, the extension of base-stock optimization to supply chain contexts with multiple stakeholders, conflicting objectives, and information asymmetry would address important practical challenges. Research in this direction would help organizations optimize inventory positions across complex supply networks while managing the inherent tensions between local optimization and system-wide performance.

Fourth, the development of robust optimization approaches that perform well under parameter uncertainty would enhance the practical applicability of base-stock optimization. While this report has focused on optimization under known demand distributions, in practice, organizations face uncertainty about the true demand distribution and its parameters.

Finally, the empirical validation of theoretical findings across diverse industry contexts would strengthen the practical relevance of inventory optimization research. While this report has cited empirical studies, continued efforts to bridge theoretical advances and practical implementation would accelerate the adoption of best practices in inventory management.

---

## References

[1] Research on GI/M/1 make-to-stock queues examining the effects of variability on optimal base-stock levels and costs, demonstrating that increased demand arrival time variability leads to augmentation of optimal base-stock levels and increased inventory-related costs.

[2] Analysis of total inventory cost sensitivity to demand and supply variation, establishing that the coefficient of variation of demand serves as a useful indicator for determining whether total cost is more sensitive to changes in lead time mean or lead time variance.

[3] Study of capacitated single-echelon base-stock policies establishing rules for system operation based on inventory levels, with the base-stock level indicating the ideal inventory position in a given period.

[4] Dynamic programming analysis demonstrating the optimality of state-dependent base-stock policies in inventory systems, including models with correlated demand and forecast evolution.

[5] Empirical study demonstrating that applying optimized stock management models resulted in a 33% cost reduction, with findings consistent across different product categories based on value and demand variability interactions.

[6] Research on discrete demand distributions in inventory systems, including analysis of compound Poisson demand and the relationship between base-stock policies and order-up-to mechanisms.

[7] Investigation of optimal base-stock levels under total cost CVaR minimization in make-to-stock systems, developing approximations for optimal base-stock levels and examining cost variance behavior.

[8] Comprehensive study on inventory management under stochastic demand using Monte Carlo Simulation with grid search and Bayesian optimization, comparing periodic review (p, Q) and continuous review (r, Q) policies.

[9] Analysis of fill rate approximation in general review single-stage systems, demonstrating that approximation performance improves when the coefficient of variation of demand during lead time and review periods decreases.

[10] Framework for demand pattern classification using coefficient of variation, categorizing demand as steady, variable, erratic, irregular, lumpy, or dead to guide inventory management tactics.

## Annotations


## Sources
[1] http://www.columbia.edu/~gmg2/4000/pdfold/lec10.pdf
[2] https://arxiv.org/html/2505.08673v1
[3] https://arxiv.org/pdf/2406.19425
[4] https://business.columbia.edu/sites/default/files-efs/pubfiles/4057/stochastic_inventory.pdf
[5] https://cdn.vanderbilt.edu/vu-web/owen/files/publications/FangLeadtimepprOmega.pdf
[6] https://dspace.mit.edu/bitstream/handle/1721.1/156876/10696_2024_Article_9562.pdf?sequence=1&isAllowed=y
[7] https://egon.cheme.cmu.edu/Papers/Garcia_Herreros_Optimizing_inventory_policies.pdf
[8] https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=case1087418721&disposition=inline
[9] https://irep.ntu.ac.uk/id/eprint/53586/1/Henry%20SOO%202025.pdf
[10] https://lup.lub.lu.se/student-papers/record/9162352/file/9162354.pdf
[11] https://mysite.ku.edu.tr/fkaraesmen/wp-content/uploads/sites/130/2021/09/WK_06.pdf
[12] https://people.orie.cornell.edu/huseyin/publications/base_stock.pdf
[13] https://people.orie.cornell.edu/shmoys/stoch-inv.pdf
[14] https://www.aimsciences.org/article/doi/10.3934/jimo.2020148
[15] https://www.cise.ufl.edu/~arunava/papers/msom-inventory-pooling-informal.pdf
[16] https://www.cwi.nl/documents/199637/Inventory_Management_2017-12-06.pdf
[17] https://www.digitalsense.ai/blog/what-is-inventory-optimization
[18] https://www.ime.unicamp.br/~andreani/MS515/capitulo12.pdf
[19] https://www.jhuapl.edu/spsa/pdf-spsa/schwartz_etal_automatica06.pdf
[20] https://www.learnaboutlogistics.com/inventory-policy-in-supply-chains-requires-cov-for-skus/
[21] https://www.mdpi.com/2079-8954/12/7/260
[22] https://www.mdpi.com/2227-7390/10/7/1142
[23] https://www.mdpi.com/2305-6290/9/4/170
[24] https://www.quora.com/Given-imperfect-data-and-non-normal-demand-distributions-how-would-you-go-about-setting-Multi-Echelon-Safety-Stock-levels
[25] https://www.sciencedirect.com/science/article/abs/pii/S0305054813001019
[26] https://www.sciencedirect.com/science/article/abs/pii/S0377221703009238
[27] https://www.sciencedirect.com/science/article/abs/pii/S0377221716302041