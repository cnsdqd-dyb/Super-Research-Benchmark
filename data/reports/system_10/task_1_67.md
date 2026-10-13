# Deep Research Report: perplexity/sonar-deep-research
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** c36dbb30 | **Time:** 129.79s | **Cost:** $1.17849
--------------------------------------------------------------------------------

# Base-Stock Policy Parameter Optimization and Demand Variation: A Comprehensive Analysis of Cost Minimization

This comprehensive report examines how base-stock policy parameter optimization systematically minimizes total inventory costs while accounting for demand variability measured through coefficients of variation. Research demonstrates that optimal base-stock levels balance opposing cost pressures through mathematical frameworks that explicitly incorporate demand volatility metrics, with studies showing that base-stock policies achieve cost performance within 1.5% of optimal solutions when demand-to-holding cost ratios are substantial, and that a 1% reduction in demand variance can generate 0.4% to 0.5% savings in safety stock investment.[1][13] The fundamental insight is that base-stock parameters—primarily the target inventory level or "order up-to" point—must be dynamically calibrated based on coefficient of variation values, lead time characteristics, and the specific cost structure of holding and shortage penalties, creating a quantitative bridge between demand predictability and economically efficient inventory positioning.

## Fundamentals of Base-Stock Policy Design and Operation

The base-stock policy represents one of the most fundamental and widely studied inventory control mechanisms in operations management, providing both theoretical elegance and practical implementation simplicity.[15] The policy operates through a straightforward decision rule: when inventory falls below a predetermined target level (the base-stock level, often denoted as S or R), the firm immediately orders sufficient units to bring inventory back to that target level.[6][15] This contrasts with alternative policies like the (R, Q) policy that prescribe both a reorder point and a fixed order quantity, or the (s, S) policy that employs two thresholds with fixed costs.[37]

Understanding the operational mechanics of base-stock policies requires distinguishing between inventory position and on-hand inventory levels.[25] Inventory position represents the total of on-hand inventory plus all outstanding orders, while on-hand inventory refers only to goods physically available for immediate sale or use.[25] The base-stock policy maintains the inventory position at a constant level S, meaning that if current on-hand inventory is less than S after fulfilling demand, an order is immediately placed for the difference.[6][15][25] This ensures a predictable and consistent flow through the system, with demand during the lead time being the critical variable determining whether actual stockouts occur.[15]

The elegance of base-stock policies stems from their proven optimality under specific but common conditions in inventory management.[37][58] When inventory systems face linear ordering costs (unit cost per item ordered) and no fixed setup costs, dynamic programming analysis reveals that the optimal policy exhibits a convex value function structure, which naturally leads to a base-stock formulation.[37][40][58] The proof of this optimality hinges on showing that the cost function is convex in the inventory position—a mathematical property that guarantees that ordering up to a single target level minimizes expected costs better than any alternative ordering strategy.[40][58]

The theoretical foundation for base-stock optimality extends to multi-period settings with stochastic demand.[17][37][40] In each period, the optimal ordering decision depends only on the current inventory position and the conditional distribution of future demands, not on the history of past demands or orders.[17][40] This property, known as the Markov property, allows decision-makers to focus exclusively on setting the appropriate target level S, dramatically simplifying computation relative to more complex policies that might require tracking multiple state variables.[17]

## Understanding Demand Variation and the Coefficient of Variation

Demand variability represents the central operational challenge in inventory management, as random fluctuations in customer demand create fundamental uncertainty about future needs.[2][19][20] The coefficient of variation (CoV) provides a normalized, dimensionless measure of this variability that enables comparisons across products with different absolute demand levels, different units of measurement, or different scales.[2][9][20][23] The CoV is calculated as the ratio of the standard deviation of demand to the mean demand, typically expressed as a percentage: CoV = (Standard Deviation / Mean) × 100.[2][20][23]

The power of the coefficient of variation lies in its ability to standardize variability measurement.[2][9][19][20][23] Consider a situation where one product experiences average monthly demand of 1,000 units with a standard deviation of 200, while a second product has average monthly demand of 100 units with a standard deviation of 50.[23] The first product has an absolute standard deviation four times larger than the second, yet both exhibit identical coefficients of variation of 20%.[2][23] For inventory management purposes, these products should be managed similarly despite their vastly different demand scales, and the CoV correctly identifies this equivalence in relative volatility.[2][23]

Practical inventory research reveals a critical threshold in CoV values at approximately 0.5.[2][9][23] Products with CoV below 0.5 are classified as having stable, predictable demand suitable for standard forecasting techniques and relatively simple inventory management approaches.[2][23] Products with CoV between 0.5 and 1.0 exhibit intermediate variability requiring more sophisticated planning, and products with CoV exceeding 1.0 demonstrate highly volatile or lumpy demand patterns that resist traditional forecasting and demand special management strategies.[2][9][23]

Demand variability originates from multiple sources, both external and internal to the organization.[19] External factors include seasonality (predictable variation tied to seasons, holidays, or weather), economic conditions (recessions or booms affecting spending), consumer preference shifts (trends in tastes or technology adoption), supply chain disruptions (shortages or transportation issues), and competitive actions (promotions or new product launches by competitors).[19] Internal factors stem from organizational decisions including promotional timing (artificial demand spikes from temporary discounts), new product introductions (creating uncertainty about initial adoption), sales force incentives (end-of-period pushes creating lumpy patterns), and pricing decisions.[19][23]

The distinction between demand variability itself and forecast error variability carries profound implications for safety stock calculation and base-stock parameter setting.[12][22][31][35] When organizations rely on historical demand to set inventory targets, they explicitly measure demand variance and incorporate it directly into formulas.[12][22][31][35] However, when organizations employ forecasts to determine cycle stock levels, the relevant variability metric becomes forecast error—the difference between predicted and actual demand.[12][22][31][35] An improved forecasting process that generates predictions closer to realized values effectively reduces the variability term in safety stock calculations, demonstrating that forecast accuracy directly translates to inventory cost reduction.[9][12][22][32]

## Cost Components and the Economic Foundation of Parameter Optimization

The total cost structure in inventory systems comprises three distinct and competing elements: holding costs, ordering costs, and shortage costs.[7][30][34][41] These three cost categories create the fundamental economic tension that parameter optimization must resolve.[7][30][41] Understanding each component is essential for comprehending why base-stock parameters must be calibrated differently for products with varying demand variation characteristics.

Holding costs, also termed carrying costs or storage costs, represent the expenses incurred for maintaining inventory in warehouses or facilities.[7][41] These costs include explicit expenses such as warehouse facility rental or ownership, utilities, insurance premiums, labor for inventory management and handling, and shrinkage or loss from theft or deterioration.[7][41] They also include implicit or opportunity costs, representing the financial returns foregone by deploying capital in inventory rather than alternative investments.[7][41] Industry benchmarking suggests holding costs typically range from 20% to 35% of inventory value annually, with the rate depending heavily on the nature of products (perishable goods incur higher rates due to spoilage risk), the efficiency of facilities, and the opportunity cost of capital.[7][41]

The holding cost structure creates a direct incentive to minimize inventory levels.[7][30][41] Every additional unit held in inventory generates proportional holding costs that accumulate throughout the period the unit remains in stock.[7][41] For products with low holding cost percentages (such as high-value items with long shelf lives), maintaining higher inventory levels to protect against demand variability becomes economically justified.[7][30][41] Conversely, for products with high holding costs (such as perishable goods or items with rapid technological obsolescence), minimizing inventory becomes paramount, forcing organizations to accept higher shortage risk.[7][30][41]

Shortage costs or penalty costs represent the financial consequences of insufficient inventory when demand occurs.[30][34][41] These costs manifest differently depending on whether the inventory system operates under backorder assumptions (unfulfilled demand waits for replenishment) or lost-sales assumptions (unmet demand is permanently lost).[30][34][41] Under backorder assumptions, shortage costs include the cost of expedited ordering or production to replenish stock quickly, potentially at premium costs, plus potential customer dissatisfaction and relationship damage.[30][34][41] Under lost-sales assumptions, shortage costs equal the gross profit margin on unmet units, representing the direct revenue loss from inability to serve demand.[30][34][41]

The relationship between holding costs and shortage costs creates the economic rationale for base-stock parameter optimization.[30][34] When shortage costs substantially exceed holding costs (typical in most practical applications where the ratio exceeds 100:1), organizations should maintain relatively high base-stock levels to minimize the risk of costly stockouts.[24][30][34] When holding costs are proportionally higher relative to shortage costs, organizations should set more conservative base-stock levels, accepting higher stockout probabilities to minimize inventory investment.[30][34]

Ordering costs, the third component, represent expenses associated with placing and receiving orders.[30][34] These costs include administrative expenses for order processing, communication with suppliers, inspection and quality checking of received goods, and sometimes transportation costs.[30][34] Ordering costs per unit typically decrease with order quantity (fixed costs spread across more units), creating incentives to order in larger batches.[30][34] However, in base-stock policies with continuous or frequent review, ordering costs per order become a fixed expense that doesn't vary with the base-stock level itself, though lead times may be affected by ordering patterns.[30][34]

## The Mathematical Framework Connecting Demand Variation to Optimal Base-Stock Levels

The connection between demand variation and optimal base-stock parameters operates through a well-established mathematical framework rooted in dynamic programming and cost minimization.[40][44][58] The fundamental insight is that the base-stock level must be set sufficiently high to cover expected demand during the replenishment lead time plus an additional safety buffer proportional to demand variation.[15][25][44]

The optimal base-stock level formula for single-period contexts follows directly from the newsvendor model framework:[26][43][48]

\[ r^* + 1 = \theta + z\sigma \]

where \( \theta \) represents mean demand during the lead time, \( z \) is a critical fractile value determined by the cost ratio, and \( \sigma \) is the standard deviation of demand during the lead time.[15][26][44] The critical fractile value z satisfies the relationship:[15][26][44]

\[ G(r^* + 1) = \frac{b}{b + h} \]

where \( b \) represents the unit shortage cost and \( h \) represents the unit holding cost.[15][26][44] This formula reveals the precise mechanism by which cost parameters drive base-stock determination: the optimal service level (probability of not stockout) increases directly with shortage cost relative to total cost, and decreases with holding cost.[15][26][44]

The critical insight for demand variation is that the coefficient of variation influences the absolute magnitude of the safety stock buffer required:[9][31][32][50] When demand exhibits high variability (high standard deviation relative to mean demand), the term \( z\sigma \) becomes substantial, requiring substantially higher base-stock levels to maintain a constant service level probability.[9][31][32][50] Conversely, when demand is stable and predictable (low CoV), the standard deviation term is small, allowing lower base-stock levels while maintaining the same service level target.[9][31][32][50]

The total cost function for base-stock policies incorporates both holding and shortage costs as functions of the chosen base-stock level:[15][44][50]

\[ TC = h \cdot I(r) + b \cdot B(r) \]

where \( I(r) \) represents the expected on-hand inventory level given base-stock level r, and \( B(r) \) represents the expected backorder or shortage quantity.[15][44] The expected on-hand inventory under base-stock policy equals:[15][25][44]

\[ I(r) = r + 1 - \theta + B(r) \]

where the difference between the base-stock level and mean demand reflects the safety stock buffer, adjusted downward by expected shortages that consume inventory position.[15][25][44] The expected shortage quantity is calculated as:[15][44][50]

\[ B(r) = \int_{r+1}^{\infty} (x - r - 1)g(x)dx \]

where g(x) is the probability density function of demand during the lead time.[15][44][50]

The optimization principle states that the optimal base-stock level minimizes the total cost function by balancing the marginal holding cost against the marginal shortage cost:[15][44][58] Moving from r to r+1 adds one unit of expected holding cost and reduces expected shortage cost by the probability that demand exceeds the current level times the unit shortage cost.[15][44][58] The optimal point is reached when these marginal effects balance exactly.[15][44][58]

For normally distributed demand, the optimal base-stock level takes the practical form:[15][44][50]

\[ r^* + 1 = \theta + z \cdot \sigma \]

where z is the standard normal quantile satisfying \( \Phi(z) = \frac{b}{b + h} \].[15][44][50] This formula explicitly shows that required base-stock increases linearly with demand standard deviation—doubling the standard deviation requires increasing the base-stock level by an amount proportional to the coefficient of variation increase.[15][44][50]

## Coefficient of Variation as a Demand Variability Metric in Parameter Setting

The coefficient of variation provides crucial insight into how base-stock parameters should be adjusted across different products within an organization's portfolio.[2][9][23][32] Products with identical absolute standard deviations but different mean demands have different CoV values and should receive different inventory management approaches.[2][9][23] A product with mean demand of 1,000 units and standard deviation of 200 (CoV = 0.20) should be managed quite differently from a product with mean demand of 100 and standard deviation of 200 (CoV = 2.0), despite both having identical absolute variability.[2][9][23]

The empirical relationship between demand variance reduction and safety stock savings has been quantified through supply chain research, revealing the practical magnitude of CoV effects.[9][32] A 1% reduction in demand variance (achieved through improved forecasting) produces approximately 0.4% to 0.5% reduction in required safety stock investment.[9][32] For organizations with $100 million in inventory containing $25 million in safety stock, a 10% improvement in demand variance (achieved through better forecasting that reduces the variance of forecast errors) translates to approximately $1 million in safety stock reduction.[9][32] Given that typical demand planning projects cost substantially less than $1 million, the return on investment from improving forecasting accuracy becomes extraordinarily attractive.[9][32]

This relationship manifests because safety stock requirements depend on both the mean demand during lead time and the standard deviation of that demand:[9][31][32][50] Safety stock is calculated as \( SS = Z \cdot \sigma \) where Z is the service level factor and \( \sigma \) is demand standard deviation.[9][31][32][50] Products with high CoV (high relative variability) naturally require higher safety stock multiples to achieve equivalent service levels compared to low-CoV products.[9][23][32] An organization should therefore allocate sophisticated demand planning resources preferentially toward high-CoV products where forecast improvement generates the greatest absolute savings.[9][23][32]

The segmentation of products based on CoV combined with other dimensions creates the foundation for differentiated inventory management strategies.[23][24] High-volume products with low CoV (below 0.5) can be managed through simple forecasting models and lean inventory approaches, freeing management attention for more demanding categories.[2][23][24] High-CoV products receive more sophisticated forecasting attention, often employing machine learning models or causal forecasting approaches that can capture nonlinear patterns in demand drivers.[2][23][24] Very low-volume, high-CoV products may employ make-to-order or assemble-to-order strategies, effectively eliminating demand forecasting risk by creating inventory only after confirmed customer demand.[2][23][24]

## Lead Time Effects and Their Interaction with Demand Variation

The replenishment lead time—the duration between ordering and receiving inventory—plays a critical role in modulating how demand variation translates into required base-stock levels.[14][25][31][33][50] The interaction between lead time and demand variation is multiplicative rather than additive: long lead times with high demand variation create compounding risks requiring dramatically higher base-stock levels.[14][25][31][50]

The mathematical form of this relationship appears in the safety stock calculation: safety stock depends on standard deviation of demand during the lead time, which equals the single-period standard deviation multiplied by the square root of the lead time in periods.[31][50] If weekly demand has standard deviation of 50 units and lead time is 4 weeks, the standard deviation of lead time demand is \( 50 \times \sqrt{4} = 100 \) units.[31][50] This square-root relationship means that doubling the lead time increases required safety stock by only 41% (the square root of 2), not 100%, but the effect remains substantial.[31][50]

Lead time variability adds an additional layer of complexity beyond mean lead time length.[14][31][35][50] When suppliers deliver inconsistently, the actual lead time varies around its mean, forcing organizations to buffer against both the variability of demand during the mean lead time and the variability of the lead time itself.[14][31][35][50] The combined safety stock formula for both demand and lead time variability is:[31][50]

\[ SS = Z \times \sqrt{(\sigma_D^2 \times L) + (\sigma_{LT}^2 \times D_{avg}^2)} \]

where \( \sigma_D \) is demand standard deviation, L is mean lead time, \( \sigma_{LT} \) is lead time standard deviation, and \( D_{avg} \) is average demand.[31][50] Research on the relative impact of these two variability sources reveals that demand variability typically dominates, with effects approximately 10 times larger than lead time variability effects for typical supply chains.[31][50]

This finding has important implications for base-stock parameter optimization: organizations achieve greater cost reductions by investing in demand forecasting improvement (reducing \( \sigma_D \)) than by attempting to reduce lead time variability alone.[31][32][50] However, reducing mean lead time (different from reducing lead time variability) produces substantial benefits, as it reduces the total expected demand accumulated during the lead time, allowing lower base-stock levels without sacrificing service levels.[14][31][33][50]

## Advanced Parameter Optimization Techniques

Moving beyond the theoretical foundations, practical optimization of base-stock parameters in complex real-world scenarios often requires computational approaches that can handle the interaction of multiple constraints and objectives.[1][11][40][55] Single-period newsvendor frameworks and basic dynamic programming work well for relatively simple scenarios, but modern supply chains frequently exhibit characteristics such as multiple products, capacity constraints, setup costs, or non-stationary demand that complicate optimization.[1][40][54]

Stochastic approximation methods provide one approach for computing optimal base-stock levels when analytical solutions become intractable.[11][55] These methods operate by iteratively updating base-stock level estimates based on observed demand realizations, without requiring explicit knowledge of the underlying demand distribution.[11][55] The key advantage is computational feasibility: these methods can work directly with observed sample data rather than requiring estimation of complete demand distributions.[11][55] Research demonstrates that stochastic approximation methods, when initialized with reasonable starting values, converge to optimal base-stock levels within 10-40 iterations, even when starting from solutions with substantial optimality gaps.[11][55]

Simulation-based optimization approaches prove particularly valuable when system dynamics involve production capacity constraints, multiple echelons, or product interactions not captured by simple analytical models.[54] The optimization approach involves constructing a detailed simulation model reflecting actual supply chain operations, then using algorithms such as simulated annealing, genetic algorithms, or gradient-based search to identify base-stock parameter combinations that minimize total system cost while maintaining service level targets.[54] Research on multi-echelon systems found that optimization methods incorporating actual production constraints achieved 30.7% reductions in average inventory compared to standard industry approaches while simultaneously improving service levels from 88.4% to 96.3%.[54]

Capped base-stock policies represent an emerging class of policies that modify the standard approach by introducing an order cap—a maximum order quantity—alongside the traditional base-stock level parameter.[1] These policies prove valuable in lost-sales environments where demand exceeding inventory is permanently lost rather than back-ordered.[1] The theoretical contribution shows that capped base-stock policies converge exponentially rapidly toward constant-order policies as the base-stock level increases, providing a bridge between two traditionally distinct policy classes and revealing that optimal policies in highly uncertain environments often blend characteristics of multiple policy types.[1]

Machine learning and artificial intelligence approaches increasingly enable more sophisticated demand forecasting that directly improves base-stock optimization.[39][42] Modern machine learning models can capture nonlinear relationships and interactions between demand drivers that traditional statistical methods miss.[39][42] When integrated into closed-loop prediction-optimization frameworks, these models provide dynamic real-time adjustments to base-stock parameters that respond automatically to changing business conditions.[39][42] Research on equipment distribution systems found that AI-enabled demand forecasting combined with multi-objective inventory optimization reduced inventory redundancy to 9.42% and decreased stockouts by 35% compared to traditional approaches.[39]

## Practical Implementation: Translating Theory into Decision Rules

Despite the mathematical sophistication of base-stock theory, practical implementation requires translating optimal parameter calculations into clear decision rules that operations personnel can execute daily.[27][36][42] The standard approach involves calculating the reorder point—the inventory level that triggers a new order—as:[36]

\[ ROP = (Lead\ Time\ Demand) + Safety\ Stock \]

or more explicitly:[36]

\[ ROP = (L \times D_{avg}) + (Z \times \sigma_D \times \sqrt{L}) \]

where L is lead time in days or weeks, \( D_{avg} \) is average demand per day or week, Z is the service level factor, and \( \sigma_D \) is the standard deviation of demand per period.[36]

For implementation, organizations should calibrate the Z service level factor independently for product groups based on strategic importance, profit margin, or dollar volume.[12][22][31][35] High-value items or products critical to customer satisfaction should receive higher Z values (typically 1.65 for 95% service level or 2.33 for 98% service level).[12][22][31][35] Lower-value items or slow-movers can employ lower Z values (1.04 for 85% service level or 1.28 for 90% service level), reducing inventory investment on less important items.[12][22][31][35]

The practical challenge in implementation involves obtaining accurate estimates of the required input parameters: average demand, demand standard deviation, and lead time.[36][42] For mature products with stable demand patterns, historical demand data spanning at least 12-24 months provides reliable estimates.[36][42] For new products or products with demand under major structural change, organizations must either use proxy products with similar demand characteristics or explicitly account for uncertainty in the parameter estimates through higher safety factors.[36][42]

Organizations should implement periodic reviews of base-stock parameters—monthly reviews for volatile categories, quarterly for stable items—to ensure that parameters remain aligned with evolving business conditions.[42] These reviews should specifically examine whether actual service levels align with targets, whether inventory turnover rates have changed significantly, and whether external factors (new customers, product phase-outs, promotional calendars) suggest the need for parameter adjustments.[42] This adaptive approach prevents parameters from becoming stale and disconnected from current operations.[42]

Automation becomes essential for organizations managing thousands of SKUs across multiple locations, as manual parameter calculation and updating becomes impractical.[33][36][42] Inventory management software can automatically calculate base-stock parameters for each SKU based on historical demand data and configured service level targets, update these parameters on configurable schedules, and generate alerts when inventory approaches reorder points or when parameter changes exceed threshold values requiring supervisory review.[33][36][42]

## Optimization in Multi-Product and Multi-Echelon Systems

Real-world supply chains typically involve multiple products competing for limited resources, storage space, and capital, requiring base-stock optimization that accounts for these interactions.[1][4][16][54] Single-product optimization approaches that treat each item independently often produce suboptimal results for the total system because they ignore product interactions and resource constraints.[1][4][54]

Multi-product optimization frameworks must explicitly model the trade-offs between different products.[1][4][54] A product with high demand variability and high shortage cost receives higher base-stock levels and consumes more warehousing space and working capital, leaving less available for other products.[1][4][54] The global optimization problem seeks to allocate limited resources—warehousing capacity, working capital, inventory management effort—across all products to minimize total system cost while achieving specified service levels for the product portfolio.[1][4][54]

Multi-echelon systems, where inventory exists at multiple levels (manufacturing facility, regional distribution centers, retail locations), introduce further complexity because decisions at one echelon affect others.[4][6][16] The echelon inventory concept proves valuable here: instead of managing inventory position at each echelon independently, organizations track total downstream inventory (including inventory at all subsequent echelons) to make more informed ordering decisions at upstream levels.[6][16] When a regional distribution center is adequately stocked, the manufacturing facility doesn't need to hold additional buffer inventory; when downstream facilities face stockout risk, the manufacturing facility should increase its base-stock level to provide better support.[6][16]

The asymptotic optimality results for base-stock policies with setup costs or capacity constraints provide theoretical guidance for complex scenarios.[4][8][16][54] These results establish that, in limiting regimes where certain parameters (such as setup times) grow very large, base-stock policies achieve optimal or near-optimal performance.[4][8][16][54] The practical value is that organizations can employ base-stock structures for optimization while incorporating additional constraints and complexities, with confidence that the resulting solutions will perform well even if not provably optimal.[4][8][16][54]

## Cost Minimization Performance and Comparative Analysis

Empirical and computational research comparing base-stock policies to alternative approaches consistently demonstrates their cost minimization effectiveness, particularly when demand-to-holding cost ratios are substantial.[13][24][28][47] When the unit shortage cost exceeds the unit holding cost by a ratio of 100:1 or greater—the typical case in most practical applications—the best base-stock policy achieves costs within 1.5% of the theoretical optimal cost.[13][24][47] This near-optimality performance justifies the widespread adoption of base-stock policies despite the existence of more complex alternative policies.[13][24][47]

The performance advantage of base-stock policies relative to simpler alternatives grows more pronounced as demand variability increases.[13][28] For stable, predictable demand (low CoV), even crude inventory rules of thumb may perform adequately, so the performance advantage of optimized base-stock parameters is modest.[13][28] For highly variable demand (high CoV), the difference between naively set parameters and optimally chosen parameters becomes substantial—sometimes representing 10-20% differences in total system cost.[13][28] This observation explains why CoV analysis is particularly valuable for identifying which products in a portfolio most urgently require sophisticated inventory management attention.[13][28]

Comparative analysis with dual-sourcing policies (where organizations can order from both fast and slow suppliers with different costs and lead times) reveals that under certain conditions, modified base-stock structures can approximate optimal performance.[1] The capped base-stock policy approaches a constant-order policy asymptotically, demonstrating that the two policies are not fundamentally distinct but rather represent different points on a spectrum of practical inventory control approaches.[1]

## Application to Demand Planning and Forecast Accuracy Improvement

The connection between base-stock parameter optimization and demand forecasting quality creates a powerful lever for improving supply chain performance.[9][12][22][32] Since base-stock levels depend directly on the standard deviation of forecast error (when forecasts are employed rather than historical demand), improving forecast accuracy directly reduces required inventory investment.[9][12][22][32]

Organizations should view their demand planning investment as directly generating returns through reduced base-stock parameter requirements.[9][32] If a demand planning initiative improves forecast accuracy such that forecast error standard deviation decreases by 10%, and if an organization maintains $25 million in safety stock inventory, the 0.4% to 0.5% safety stock reduction generates approximately $1 million in freed working capital or reduced inventory holding costs.[9][32] For complex product portfolios, the aggregate impact of forecast improvement across many items frequently exceeds $5-10 million in released working capital.[9][32]

This relationship explains why sophisticated demand planning approaches—including machine learning models, causal forecasting incorporating leading indicators, collaborative forecasting with customer input, and statistical techniques for handling demand seasonality and trends—generate positive financial returns despite their implementation costs.[39][42] Each percentage point of forecast improvement translates directly into percentage point reductions in required safety stock levels, making forecast improvement one of the highest-return supply chain investments available.[9][32][39][42]

Different demand patterns require different forecasting approaches to minimize variability in forecast errors, which then determines optimal base-stock levels.[2][23][24] High-volume, stable demand items (low CoV) can employ simple exponential smoothing or moving average methods, as these methods excel at extracting true demand signals from stable patterns.[2][23][24] Items with strong seasonality benefit from seasonal decomposition methods that separate trend, seasonal, and irregular components before forecasting each separately.[2][23][24] Items with low volume and sporadic demand (high CoV, lumpy demand) often cannot be forecast using standard time-series methods at all; instead, organizations may employ judgmental forecasting, causal models based on customer order pipelines or project pipelines, or simply employ make-to-order strategies to eliminate forecasting requirement entirely.[2][23][24]

## Conclusion: Synthesizing Theory and Practice for Optimal Supply Chain Decisions

Base-stock policy parameter optimization achieves cost minimization by systematically calibrating inventory target levels to match the specific characteristics of demand variability, supply lead times, and the cost structure of holding versus shortage penalties.[1][15][25][44] The coefficient of variation provides the essential metric for measuring demand variability in normalized form, enabling direct comparison across products with vastly different absolute demand levels.[2][9][20][23] The mathematical frameworks connecting CoV to optimal base-stock levels reveal that required inventory increases proportionally to demand standard deviation, creating a clear and quantifiable relationship between demand predictability and inventory investment requirements.[15][44][50]

The optimization principle—balancing marginal holding costs against marginal shortage costs—translates into practical decision rules for setting reorder points and base-stock levels that can be computed efficiently even for organizations managing tens of thousands of distinct products.[11][30][36][40][55] The near-optimality of well-designed base-stock policies (typically within 1.5% of theoretical optimal cost) justifies their widespread adoption despite the theoretical possibility of more complex alternatives.[13][24][47] The performance advantage becomes most pronounced for products with high demand variation, where optimized parameters can generate 10-20% cost improvements relative to crude approximations.[13][28]

Practical implementation of base-stock optimization requires accurate estimation of input parameters (demand mean and standard deviation, lead time duration), periodic review and updating of parameters to maintain alignment with evolving conditions, and often technology-enabled automation for organizations managing large product portfolios.[36][42] The segmentation of products based on coefficient of variation combined with ABC classification enables differentiated inventory management strategies that allocate sophisticated planning effort toward highest-impact items while employing simpler approaches for lower-priority products.[2][9][23][24]

The recognition that demand forecast improvement directly reduces base-stock parameter requirements—generating approximately 0.4% to 0.5% safety stock reduction for each 1% improvement in forecast accuracy—creates strong financial justification for investing in advanced demand planning capabilities including machine learning models and causal forecasting approaches.[9][32][39] This relationship establishes demand planning, base-stock optimization, and inventory cost minimization as interconnected components of an integrated supply chain strategy rather than isolated functional activities.[9][32][39][42]

Organizations seeking to minimize inventory costs while maintaining service levels should employ this comprehensive framework: measure demand variability using coefficient of variation metrics, segment products based on both CoV and value, set base-stock parameters using formulas explicitly incorporating demand variability and cost ratios, invest in demand forecasting improvement particularly for high-CoV products, and employ periodic reviews and automated systems to maintain parameters aligned with evolving conditions.[1][9][31][36][42] This systematic approach transforms inventory management from art and intuition into science and quantifiable decision-making, unlocking substantial opportunities for improving financial performance through working capital optimization.

## Annotations
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Technical Note—Understanding the Performance of Capped Base ...', 'url': 'https://pubsonline.informs.org/doi/10.1287/opre.2020.2019'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Coefficient of Variation (CoV) in Demand Planning: A Key Metric for ...', 'url': 'https://inteli-chain.com/coefficient-of-variation-cov-in-demand-planning-a-key-metric-for-success/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Analyzing Variability, Cost, and Responsiveness of Base-Stock ...', 'url': 'https://www.tandfonline.com/doi/abs/10.1080/0740817X.2014.999897'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Asymptotic Optimality of Base-Stock Policies with Idle Times for ...', 'url': 'http://www.columbia.edu/~jd2736/publication/Base_stock.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Optimizing Stock Strategies with Demand Variability Analysis', 'url': 'https://demanddriventech.com/blog/managing-demand-variability'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Base Stock Policy - DSpace@MIT', 'url': 'https://dspace.mit.edu/bitstream/handle/1721.1/39423/2-853Fall-2002/NR/rdonlyres/Mechanical-Engineering/2-853Manufacturing-Systems-I--Analytical-Methods-and-Flow-ModelsFall2002/0472BED3-CEB2-47E1-B273-B1E003E05AFE/0/lecture_12.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'How to Reduce Holding Costs with Stock Optimization', 'url': 'https://www.inventory-planner.com/understanding-holding-costs-and-how-to-minimize-them-with-stock-optimization/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Asymptotic Optimality of Base-Stock Policies with Idle Times for ...', 'url': 'http://www.columbia.edu/~jd2736/publication/Base_stock.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Using Coefficient of Variation to Drive Safety Stock Related Decisions', 'url': 'https://blog.arkieva.com/coefficient-of-variation-safety-stock-decisions/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Inventory Control Models: Different Types and Applications | Nest Egg', 'url': 'https://nestegg.cloud/blog/inventory-control-models-different-types-and-applications/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Using Stochastic Approximation Methods to Compute Optimal Base ...', 'url': 'https://people.orie.cornell.edu/huseyin/publications/base_stock.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Calculate Inventory with Precision — Even Amid Variability - ASCM', 'url': 'https://www.ascm.org/ascm-insights/safety-stock-a-contingency-plan-to-keep-supply-chains-flying-high/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] An Adaptive Algorithm for Finding the Optimal Base-Stock Policy in ...', 'url': 'http://faculty.marshall.usc.edu/Paat-Rusmevichientong/psfiles/Adaptive-LostSale.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The Effect of Leadtime Uncertainty in a Simple Stochastic Inventory ...', 'url': 'https://pubsonline.informs.org/doi/10.1287/mnsc.40.5.603'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Base stock model - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Base_stock_model'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Asymptotic Optimality of Base-Stock Policies with Idle Times for ...', 'url': 'http://www.columbia.edu/~jd2736/publication/Base_stock.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Approximation Algorithms for Stochastic Inventory Control Models', 'url': 'https://people.orie.cornell.edu/shmoys/pdf/stoch-inv.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Inventory models: stock optimisation for efficient logistics operations', 'url': 'https://www.mecalux.com/blog/inventory-models'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Demand Variability: Causes & How to Manage It - Intuendi', 'url': 'https://intuendi.com/demand-variability/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Coefficient of Variation (CoV) in Demand Planning: A Key Metric for ...', 'url': 'https://inteli-chain.com/coefficient-of-variation-cov-in-demand-planning-a-key-metric-for-success/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Optimality of Base-Stock Policy Under Unknown General Demand ...', 'url': 'https://journals.sagepub.com/doi/10.1177/10591478251345135'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Calculate Inventory with Precision — Even Amid Variability - ASCM', 'url': 'https://www.ascm.org/ascm-insights/safety-stock-a-contingency-plan-to-keep-supply-chains-flying-high/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Inventory Policy in Supply Chains requires CoV for SKUs', 'url': 'https://www.learnaboutlogistics.com/inventory-policy-in-supply-chains-requires-cov-for-skus/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] An Adaptive Algorithm for Finding the Optimal Base-Stock Policy in ...', 'url': 'http://faculty.marshall.usc.edu/Paat-Rusmevichientong/psfiles/Adaptive-LostSale.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Basestock policy', 'url': 'https://www.utdallas.edu/~metin/Or6302/Folios/ombasestock.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Newsvendor model - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Newsvendor_model'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Top 3 Most Common Inventory Control Policies - Smart Software', 'url': 'https://smartcorp.com/inventory-control/inventory-control-policies-software/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] An Adaptive Algorithm for Finding the Optimal Base-Stock Policy in ...', 'url': 'http://faculty.marshall.usc.edu/Paat-Rusmevichientong/psfiles/Adaptive-LostSale.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Newsvendor Model', 'url': 'https://www.utdallas.edu/~metin/Or6302/Folios/omnewsvendor.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'What is stock optimization?: Methods, challenges, benefits & more', 'url': 'https://www.digitalsense.ai/blog/what-is-inventory-optimization'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Understanding safety stock and mastering its equations - MIT', 'url': 'https://web.mit.edu/2.810/www/files/readings/King_SafetyStock.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Using Coefficient of Variation to Drive Safety Stock Related Decisions', 'url': 'https://blog.arkieva.com/coefficient-of-variation-safety-stock-decisions/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Reorder Point – What Is It? | Formulas and Examples - Slimstock', 'url': 'https://www.slimstock.com/blog/reorder-point/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'How to calculate safety stock using standard deviation - Netstock', 'url': 'https://www.netstock.com/blog/safety-stock-meaning-formula-how-to-calculate/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Calculate Inventory with Precision — Even Amid Variability - ASCM', 'url': 'https://www.ascm.org/ascm-insights/safety-stock-a-contingency-plan-to-keep-supply-chains-flying-high/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Understanding the Reorder Point Formula in Inventory Management', 'url': 'https://www.netstock.com/blog/reorder-point-formula/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Stochastic Inventory Control', 'url': 'https://www.professeurs.polymtl.ca/jerome.le-ny/teaching/DP_fall09/notes/lec3_inventoryControl.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Basestock policy', 'url': 'https://www.utdallas.edu/~metin/Or6302/Folios/ombasestock.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Demand forecasting and inventory optimization of distribution ... - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC12626329/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] COMPUTING PROVABLY NEAR-OPTIMAL POLICIES FOR ...', 'url': 'https://mitsloan.mit.edu/shared/ods/documents?PublicationDocumentID=7654'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Inventory Holding Costs Guide: Formula + Free Calculator - ShipBob', 'url': 'https://www.shipbob.com/inventory-kpis/holding-costs/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Forecast Update Frequency for Inventory Models - ToolsGroup', 'url': 'https://www.toolsgroup.com/blog/forecast-update-frequency-inventory-models/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Newsvendor model - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Newsvendor_model'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Base stock model - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Base_stock_model'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Underage vs Overage Cost: Optimizing Inventory Costs - Fundbox', 'url': 'https://fundbox.com/blog/optimize-inventory-costs/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Newsvendor Networks: Inventory Management and Capacity ...', 'url': 'https://www.kellogg.northwestern.edu/faculty/vanmieghem/htm/pubs/VanMieghem_Rudi_2002_Newsnet_MSOM.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] An Adaptive Algorithm for Finding the Optimal Base-Stock Policy in ...', 'url': 'http://faculty.marshall.usc.edu/Paat-Rusmevichientong/psfiles/Adaptive-LostSale.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Stochastic Inventory Control - Course Web Pages', 'url': 'https://courses.ie.bilkent.edu.tr/ie375/wp-content/uploads/sites/7/2020/04/Stochastic-Inventory-I.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Optimizing Inventory to Respond to Demand Variability', 'url': 'https://www.supplychainbrain.com/articles/15723-optimizing-inventory-to-respond-to-demand-variability'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Understanding safety stock and mastering its equations - MIT', 'url': 'https://web.mit.edu/2.810/www/files/readings/King_SafetyStock.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Sensitivity Analysis Made Easy with Coefficient of Variation', 'url': 'https://fastercapital.com/content/Sensitivity-Analysis-Made-Easy-with-Coefficient-of-Variation.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Managing Inventory Variability in Demand - Accelera', 'url': 'https://www.accelera.io/blog/fluctuating-inventory-levels-managing-variability-in-stock-and-demand'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'How to calculate safety stock using standard deviation - Netstock', 'url': 'https://www.netstock.com/blog/safety-stock-meaning-formula-how-to-calculate/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Master Thesis Optimizing the base stock levels in a multi-echelon ...', 'url': 'https://essay.utwente.nl/96172/7/vanEkeris_MA_BMS.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Using Stochastic Approximation Methods to Compute Optimal Base ...', 'url': 'https://people.orie.cornell.edu/huseyin/publications/base_stock.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[1905.04337] Learning in structured MDPs with convex cost functions', 'url': 'https://arxiv.org/abs/1905.04337'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Inventory management metrics to handle demand volatility', 'url': 'https://www.phocassoftware.com/resources/blog/inventory-management-metrics-to-handle-demand-volatility'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] COMPUTING PROVABLY NEAR-OPTIMAL POLICIES FOR ...', 'url': 'https://mitsloan.mit.edu/shared/ods/documents?PublicationDocumentID=7654'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] On the convexity of the cost function for the (Q,R) inventory model', 'url': 'https://core.ac.uk/download/pdf/213958790.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'How to set safety stock levels for volatile demand items - EOXS', 'url': 'https://eoxs.com/new_blog/how-to-set-safety-stock-levels-for-volatile-demand-items/'}}

## Sources
https://pubsonline.informs.org/doi/10.1287/opre.2020.2019
https://inteli-chain.com/coefficient-of-variation-cov-in-demand-planning-a-key-metric-for-success/
https://www.tandfonline.com/doi/abs/10.1080/0740817X.2014.999897
http://www.columbia.edu/~jd2736/publication/Base_stock.pdf
https://demanddriventech.com/blog/managing-demand-variability
https://dspace.mit.edu/bitstream/handle/1721.1/39423/2-853Fall-2002/NR/rdonlyres/Mechanical-Engineering/2-853Manufacturing-Systems-I--Analytical-Methods-and-Flow-ModelsFall2002/0472BED3-CEB2-47E1-B273-B1E003E05AFE/0/lecture_12.pdf
https://www.inventory-planner.com/understanding-holding-costs-and-how-to-minimize-them-with-stock-optimization/
http://www.columbia.edu/~jd2736/publication/Base_stock.pdf
https://blog.arkieva.com/coefficient-of-variation-safety-stock-decisions/
https://nestegg.cloud/blog/inventory-control-models-different-types-and-applications/
https://people.orie.cornell.edu/huseyin/publications/base_stock.pdf
https://www.ascm.org/ascm-insights/safety-stock-a-contingency-plan-to-keep-supply-chains-flying-high/
http://faculty.marshall.usc.edu/Paat-Rusmevichientong/psfiles/Adaptive-LostSale.pdf
https://pubsonline.informs.org/doi/10.1287/mnsc.40.5.603
https://en.wikipedia.org/wiki/Base_stock_model
http://www.columbia.edu/~jd2736/publication/Base_stock.pdf
https://people.orie.cornell.edu/shmoys/pdf/stoch-inv.pdf
https://www.mecalux.com/blog/inventory-models
https://intuendi.com/demand-variability/
https://inteli-chain.com/coefficient-of-variation-cov-in-demand-planning-a-key-metric-for-success/
https://journals.sagepub.com/doi/10.1177/10591478251345135
https://www.ascm.org/ascm-insights/safety-stock-a-contingency-plan-to-keep-supply-chains-flying-high/
https://www.learnaboutlogistics.com/inventory-policy-in-supply-chains-requires-cov-for-skus/
http://faculty.marshall.usc.edu/Paat-Rusmevichientong/psfiles/Adaptive-LostSale.pdf
https://www.utdallas.edu/~metin/Or6302/Folios/ombasestock.pdf
https://en.wikipedia.org/wiki/Newsvendor_model
https://smartcorp.com/inventory-control/inventory-control-policies-software/
http://faculty.marshall.usc.edu/Paat-Rusmevichientong/psfiles/Adaptive-LostSale.pdf
https://www.utdallas.edu/~metin/Or6302/Folios/omnewsvendor.pdf
https://www.digitalsense.ai/blog/what-is-inventory-optimization
https://web.mit.edu/2.810/www/files/readings/King_SafetyStock.pdf
https://blog.arkieva.com/coefficient-of-variation-safety-stock-decisions/
https://www.slimstock.com/blog/reorder-point/
https://www.netstock.com/blog/safety-stock-meaning-formula-how-to-calculate/
https://www.ascm.org/ascm-insights/safety-stock-a-contingency-plan-to-keep-supply-chains-flying-high/
https://www.netstock.com/blog/reorder-point-formula/
https://www.professeurs.polymtl.ca/jerome.le-ny/teaching/DP_fall09/notes/lec3_inventoryControl.pdf
https://www.utdallas.edu/~metin/Or6302/Folios/ombasestock.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC12626329/
https://mitsloan.mit.edu/shared/ods/documents?PublicationDocumentID=7654
https://www.shipbob.com/inventory-kpis/holding-costs/
https://www.toolsgroup.com/blog/forecast-update-frequency-inventory-models/
https://en.wikipedia.org/wiki/Newsvendor_model
https://en.wikipedia.org/wiki/Base_stock_model
https://fundbox.com/blog/optimize-inventory-costs/
https://www.kellogg.northwestern.edu/faculty/vanmieghem/htm/pubs/VanMieghem_Rudi_2002_Newsnet_MSOM.pdf
http://faculty.marshall.usc.edu/Paat-Rusmevichientong/psfiles/Adaptive-LostSale.pdf
https://courses.ie.bilkent.edu.tr/ie375/wp-content/uploads/sites/7/2020/04/Stochastic-Inventory-I.pdf
https://www.supplychainbrain.com/articles/15723-optimizing-inventory-to-respond-to-demand-variability
https://web.mit.edu/2.810/www/files/readings/King_SafetyStock.pdf
https://fastercapital.com/content/Sensitivity-Analysis-Made-Easy-with-Coefficient-of-Variation.html
https://www.accelera.io/blog/fluctuating-inventory-levels-managing-variability-in-stock-and-demand
https://www.netstock.com/blog/safety-stock-meaning-formula-how-to-calculate/
https://essay.utwente.nl/96172/7/vanEkeris_MA_BMS.pdf
https://people.orie.cornell.edu/huseyin/publications/base_stock.pdf
https://arxiv.org/abs/1905.04337
https://www.phocassoftware.com/resources/blog/inventory-management-metrics-to-handle-demand-volatility
https://mitsloan.mit.edu/shared/ods/documents?PublicationDocumentID=7654
https://core.ac.uk/download/pdf/213958790.pdf
https://eoxs.com/new_blog/how-to-set-safety-stock-levels-for-volatile-demand-items/