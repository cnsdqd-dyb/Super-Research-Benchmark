# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 40f9f7ca | **Time:** 159.55s | **Cost:** $0.03444
--------------------------------------------------------------------------------

# How is the Customer Grade Partition Boundary Determined in RFM Value Stratification?

## Abstract

Customer segmentation represents a fundamental pillar of modern marketing strategy, enabling organizations to allocate resources efficiently and tailor interventions to distinct consumer groups. The Recency, Frequency, and Monetary (RFM) analysis framework has emerged as a cornerstone methodology for categorizing customers based on their transactional behavior. However, the determination of partition boundaries—those critical thresholds that delineate customer grades—remains a nuanced process that significantly impacts segmentation quality and subsequent strategic decisions. This research report provides a comprehensive examination of the methodologies, algorithms, and practical considerations involved in establishing customer grade partition boundaries within RFM value stratification systems. Drawing upon contemporary clustering techniques, statistical optimization methods, and domain-specific adaptations, this analysis elucidates the theoretical foundations and practical implementations that enable organizations to construct robust, actionable customer tier frameworks.

## 1. Introduction

### 1.1 Background and Significance

The contemporary business landscape demands increasingly sophisticated approaches to customer relationship management. Organizations across diverse industries—from e-commerce and retail to financial services and subscription-based platforms—recognize that not all customers contribute equally to organizational success. This recognition has catalyzed the development of customer value-based segmentation methodologies, among which RFM analysis stands as a particularly influential framework [1].

RFM analysis operates on a deceptively simple premise: customers can be evaluated and categorized based on three quantifiable dimensions of their purchasing behavior. Recency measures how recently a customer has made a purchase, Frequency captures how often purchases occur within a defined period, and Monetary quantifies the total spending or average transaction value. By synthesizing these three dimensions into a unified scoring framework, organizations can construct a multidimensional view of customer value that transcends simplistic revenue-based rankings [2].

The transition from raw RFM scores to actionable customer grades—commonly manifested as tiers such as Platinum, Gold, Silver, Bronze, and Bad—requires the establishment of partition boundaries. These boundaries serve as the critical demarcation points that determine which customers belong to which grade, directly influencing marketing resource allocation, service prioritization, and retention strategies. The manner in which these boundaries are determined carries profound implications for segmentation effectiveness and business outcomes [3].

### 1.2 Research Objectives

This report aims to provide a thorough examination of the methodologies employed in determining customer grade partition boundaries within RFM value stratification systems. Specifically, the analysis addresses the statistical foundations underlying boundary determination, the algorithmic approaches that automate and optimize this process, and the practical considerations that guide implementation decisions. By synthesizing insights from academic research, industry practices, and technical documentation, this report offers a comprehensive perspective on the current state of boundary determination methodologies.

## 2. Theoretical Foundations of RFM Value Stratification

### 2.1 The RFM Framework

The RFM framework provides the conceptual architecture upon which customer grade partition boundaries are constructed. Each dimension contributes distinct information about customer behavior, and their combination yields a comprehensive assessment of customer value [4].

**Recency (R)** captures the temporal dimension of customer engagement, measuring the elapsed time since a customer's most recent transaction. The underlying assumption is that customers who have purchased more recently are more likely to respond to marketing initiatives, exhibit higher engagement levels, and maintain an ongoing relationship with the organization. In practice, lower recency values (fewer days since last purchase) are considered more favorable, necessitating inverse scoring approaches where shorter time intervals yield higher scores [5].

**Frequency (F)** quantifies the number of transactions or interactions within a specified temporal window. Customers who engage in frequent purchases demonstrate sustained interest and commitment to the brand, suggesting higher loyalty and potentially greater lifetime value. Unlike recency, frequency benefits from direct positive scoring, where higher transaction counts correspond to elevated scores [6].

**Monetary (M)** reflects the total spending or average transaction value associated with a customer. This dimension captures the revenue contribution directly attributable to each customer relationship. Higher monetary values indicate customers who invest more significantly in the organization's offerings, warranting preferential treatment and targeted retention efforts [7].

The synthesis of these three dimensions typically results in a composite RFM score, often represented as a three-digit code where each digit ranges from 1 to 5. A score of 555 represents the ideal customer (most recent, most frequent, highest spending), while 111 indicates the least valuable segment (least recent, least frequent, lowest spending). This 5×5×5 structure generates 125 possible score combinations, though practical segmentation often consolidates these into a smaller number of actionable tiers [8].

### 2.2 The Need for Grade Partitioning

While the 125-cell RFM matrix provides granular customer insights, its complexity presents implementation challenges. Marketing teams require actionable categories that facilitate resource allocation and strategic planning. Customer grade partitioning addresses this need by establishing boundaries that group similar RFM combinations into coherent tiers [9].

The typical grade hierarchy—Platinum, Gold, Silver, Bronze, and Bad—represents a stratification from highest to lowest customer value. However, the specific boundaries that delineate these grades are not universally standardized. Organizations must determine where one grade ends and another begins, a decision that depends on multiple factors including business objectives, customer base characteristics, and strategic priorities [10].

The partition boundary determination process fundamentally shapes the composition of each grade. Boundaries positioned too aggressively may result in overly exclusive high-value tiers, while conservative boundaries may dilute the significance of premium grades. This balance requires careful consideration of both statistical properties and business implications [11].

## 3. Methodological Approaches to Boundary Determination

### 3.1 Quintile-Based Segmentation

The quintile-based approach represents one of the most widely adopted methodologies for establishing RFM partition boundaries. This method leverages the natural distribution of customer behavior by dividing the customer base into five equal groups based on each RFM dimension [12].

The implementation utilizes the NTILE window function in SQL or equivalent statistical operations in analytical platforms. For Recency scoring, customers are ordered by days since last purchase in descending order, with the most recent customers receiving the highest quintile (score of 5). For Frequency and Monetary dimensions, ascending order assigns higher scores to customers with greater frequency and spending [13].

The quintile approach offers several advantages for boundary determination. First, it ensures that each score level contains an equal proportion of customers, facilitating fair comparison and resource allocation. Second, it adapts automatically to the distribution characteristics of the underlying data, accommodating datasets with varying customer behavior patterns. Third, it provides interpretable boundaries that can be easily communicated across organizational stakeholders [14].

The resulting boundaries emerge from the data distribution itself rather than arbitrary thresholds. For example, if the 20th percentile of recency values (measured from most recent) falls at 45 days, customers with recency values below 45 days receive a score of 5, while those above receive progressively lower scores. This data-driven approach ensures that boundaries reflect actual customer behavior patterns rather than theoretical assumptions [15].

### 3.2 Custom Threshold Segmentation

Custom threshold segmentation represents an alternative approach where partition boundaries are defined based on domain expertise and business knowledge rather than purely statistical distributions. This methodology recognizes that optimal boundaries may depend on factors beyond raw data distributions, including strategic priorities, competitive positioning, and industry-specific considerations [16].

Under this approach, organizations establish explicit thresholds for each RFM dimension. For Recency, thresholds might define score 5 as purchases within the last month, score 4 as purchases 1-3 months ago, score 3 as purchases 3-6 months ago, score 2 as purchases 6-12 months ago, and score 1 as purchases exceeding 12 months. Similar threshold structures apply to Frequency and Monetary dimensions [17].

The specification of these thresholds requires careful consideration of business context. A luxury retailer and a coffee shop would establish vastly different monetary thresholds reflecting their distinct price points and customer spending patterns. Similarly, industries with different purchase cycles—subscription services versus retail, for instance—would define recency thresholds appropriate to their engagement patterns [18].

Custom threshold segmentation offers precision and alignment with specific business needs but requires significant domain expertise and iterative refinement. Organizations must validate that established thresholds meaningfully differentiate customer value and produce actionable segment sizes [19].

### 3.3 Weighted Composite Scoring

Weighted composite scoring introduces a layer of sophistication to boundary determination by assigning differential importance to each RFM dimension. Rather than treating R, F, and M as equally contributing to customer grade, this approach reflects the strategic priority of each dimension through weighted aggregation [20].

The weighted sum calculation takes the form:

$$
\text{RFM}_{\text{score}} = w_R \times R_{\text{score}} + w_F \times F_{\text{score}} + w_M \times M_{\text{score}}
$$

where $w_R$, $w_F$, and $w_M$ represent the weights assigned to each dimension, typically summing to 1.0 or 100%. An organization might assign Recency a weight of 50%, Frequency 30%, and Monetary 20%, reflecting a strategic emphasis on recent engagement over historical spending [21].

Once customers receive weighted composite scores, partition boundaries can be established using percentile-based thresholds. For example, the top 5% of customers by weighted score might receive Platinum designation, the following 15% Gold, the next 30% Silver, and the remaining 50% Bronze or below. This approach combines the statistical rigor of distribution-based boundaries with the strategic flexibility of weighted aggregation [22].

The selection of weights significantly impacts boundary placement and segment composition. Organizations must carefully evaluate which customer behaviors most strongly correlate with desired outcomes—whether retention, revenue growth, or advocacy—and calibrate weights accordingly [23].

## 4. Algorithmic Approaches to Boundary Optimization

### 4.1 K-Means Clustering and the Elbow Method

K-means clustering represents a powerful algorithmic approach to customer grade partition boundary determination. Rather than imposing predefined thresholds, this method allows the data itself to reveal natural groupings that correspond to meaningful customer segments [24].

The K-means algorithm partitions customers into K clusters by iteratively minimizing within-cluster variance. Each customer is assigned to the cluster whose centroid (mean) is nearest, where distance is typically measured using Euclidean distance in the normalized RFM feature space. The algorithm proceeds through alternating assignment and update steps until convergence [25].

The critical challenge in applying K-means to boundary determination lies in selecting the optimal number of clusters K. The Elbow Method addresses this challenge by evaluating the within-cluster sum of squares (WCSS), also known as inertia, across different values of K [26]:

$$
\text{WCSS} = \sum_{k=1}^{K} \sum_{c \in C_k} \|c - \mu_k\|^2
$$

where $C_k$ represents the set of customers in cluster $k$ and $\mu_k$ represents the centroid of cluster $k$.

The Elbow Method involves plotting WCSS against the number of clusters and identifying the "elbow point"—the value of K where the rate of decrease in WCSS sharply diminishes. This point represents the optimal balance between model complexity (more clusters) and explanatory power (lower WCSS). Beyond this point, additional clusters yield diminishing returns in terms of variance explained [27].

Research indicates that for customer segmentation applications, the Elbow Method typically suggests K values between 4 and 6, aligning well with common grade structures (Platinum, Gold, Silver, Bronze, Bad). The resulting cluster assignments then define the partition boundaries, with each cluster representing a distinct customer grade [28].

### 4.2 Expectation-Maximization Clustering

The Expectation-Maximization (EM) algorithm offers an alternative clustering approach that addresses certain limitations of K-means. While K-means assigns each customer to exactly one cluster, EM clustering calculates the probability that each customer belongs to each cluster, accommodating uncertainty in boundary assignments [29].

The EM algorithm iterates between two steps until convergence. In the Expectation step, the algorithm calculates the probability that each observation belongs to each class based on current parameter estimates. In the Maximization step, it updates the parameters of each class to maximize these probabilities. This process continues until the algorithm converges to a local optimum [30].

For customer grade partitioning, EM clustering provides probabilistic boundary assignments. A customer might have a 70% probability of belonging to the Platinum cluster and 30% probability of belonging to the Gold cluster, indicating boundary proximity. This probabilistic framework proves valuable for customers near partition boundaries, enabling nuanced treatment strategies [31].

### 4.3 Integration with Decision Tree Classification

Decision Tree classifiers offer a complementary approach to boundary determination by identifying the specific RFM thresholds that best separate customer segments. Trained on RFM data with cluster assignments as the target variable, Decision Trees automatically discover the decision rules that most effectively partition customers [32].

The resulting decision rules provide explicit, interpretable boundaries. For example, a Decision Tree might identify that customers with Recency ≤ 30 days, Frequency ≥ 5, and Monetary ≥ $500 belong to the Platinum segment, with clear boundary conditions for each dimension. This interpretability facilitates communication and validation of boundary decisions across organizational stakeholders [33].

## 5. Practical Implementation Considerations

### 5.1 Data Quality and Preprocessing

The accuracy and reliability of partition boundaries depend fundamentally on data quality. Organizations must address several data quality considerations before boundary determination [34].

**Duplicate transactions** can artificially inflate Frequency scores and distort Monetary calculations, leading to misplaced boundaries. Robust deduplication procedures must identify and consolidate duplicate records before analysis. **Incorrect monetary values** require validation against business rules and external data sources to ensure accuracy. **Inconsistent date formats** can compromise Recency calculations, necessitating standardization before scoring [35].

Data normalization represents another critical preprocessing step. Min-max scaling ensures that all RFM features occupy similar ranges, typically between 0 and 1. This normalization prevents features with larger magnitudes from overshadowing others during clustering, enhancing model stability and boundary validity [36].

### 5.2 Dynamic Boundary Adjustment

Static boundaries may become suboptimal as customer behavior evolves, market conditions change, and business strategies shift. Dynamic segmentation approaches address this limitation by adjusting boundaries based on ongoing performance metrics and temporal factors [37].

Seasonal variations significantly impact RFM distributions and boundary validity. Holiday periods may compress recency values as purchase activity spikes, while promotional campaigns may temporarily inflate frequency and monetary metrics. Dynamic approaches account for these variations by establishing seasonal adjustment factors or recalibrating boundaries at regular intervals [38].

Real-time RFM analysis enables immediate boundary response to significant customer events. When a high-value customer exhibits early churn signals—such as reduced purchase frequency or extended recency—dynamic systems can trigger interventions before the customer crosses critical boundaries [39].

### 5.3 Industry-Specific Adaptations

Different industries exhibit distinct customer behavior patterns that necessitate adapted boundary determination approaches [40].

**E-commerce and retail** environments typically feature high transaction volumes and moderate average order values. Boundaries often emphasize frequency and recency to capture engaged shoppers, with monetary thresholds calibrated to product price points. **Subscription services** prioritize retention metrics, often weighting recency more heavily to identify churn risks early. **Financial services** incorporate additional dimensions such as account balance trends and product adoption rates alongside traditional RFM metrics [41].

The hospitality industry exemplifies sector-specific adaptation, where boundaries may incorporate visit frequency, average daily rates, and ancillary spending patterns. These industry-specific considerations ensure that partition boundaries reflect the unique value drivers within each business context [42].

## 6. Validation and Performance Measurement

### 6.1 Silhouette Score Analysis

The Silhouette Score provides a quantitative assessment of boundary quality by measuring how similar customers are to their assigned cluster compared to neighboring clusters. The score ranges from -1 to 1, with higher values indicating better-defined boundaries [43].

For customer grade partitioning, Silhouette Scores help validate that established boundaries meaningfully separate distinct customer behaviors. Low Silhouette Scores may indicate overlapping grade definitions or inappropriate boundary placements, suggesting the need for boundary recalibration [44].

Comparative analysis across different clustering algorithms—K-means, EM, hierarchical clustering—using Silhouette Scores enables organizations to select the boundary determination approach that best captures natural customer groupings [45].

### 6.2 Segment Profile Validation

Beyond statistical metrics, boundary validity requires validation against business expectations and customer characteristics. Radar charts and profile summaries comparing the average RFM values across segments provide visual validation of boundary appropriateness [46].

Effective boundaries should produce segments with clearly differentiated profiles. Platinum customers should exhibit significantly higher Recency, Frequency, and Monetary values than Gold customers, who in turn should exceed Silver customers, and so forth. Overlapping profiles suggest boundaries that fail to meaningfully differentiate customer grades [47].

Business context validation ensures that segment compositions align with strategic expectations. If the Platinum segment contains an unexpectedly large or small proportion of customers, boundaries may require adjustment to achieve desired resource allocation implications [48].

## 7. Advanced Techniques and Emerging Approaches

### 7.1 Enhanced RFM with Additional Dimensions

Contemporary approaches extend traditional RFM analysis by incorporating additional dimensions that capture complementary aspects of customer value. The Customer Change Rate (C), for example, measures the trend in customer purchase behavior, indicating whether customers are increasing or decreasing their engagement over time [49].

Enhanced RFM+C frameworks feed additional variables into clustering algorithms, producing boundaries that reflect both current value and trajectory. This approach enables identification of "rising stars" (moderate current value with positive trends) and "declining whales" (high current value with negative trends) that traditional RFM boundaries might misclassify [50].

### 7.2 Micro-Segmentation through Hierarchical Clustering

Hierarchical clustering enables multi-resolution boundary determination that accommodates both broad grade structures and fine-grained micro-segments. By constructing a hierarchy of customer groupings, organizations can drill down from high-level grades (Platinum, Gold, Silver) to increasingly specific segments within each grade [51].

This hierarchical approach proves particularly valuable for organizations seeking to balance strategic simplicity (few broad tiers) with operational precision (numerous actionable micro-segments). Boundaries at each level of the hierarchy serve different purposes, from resource allocation to campaign targeting [52].

### 7.3 Machine Learning Integration

Advanced machine learning approaches increasingly complement traditional boundary determination methods. Gradient boosting algorithms and neural networks can identify non-linear boundary patterns that escape simpler statistical methods, particularly in datasets with complex customer behavior distributions [53].

However, the interpretability trade-off associated with complex models requires careful consideration. While a neural network might identify optimal boundaries in a mathematical sense, the resulting boundaries may lack the transparency needed for organizational adoption and stakeholder communication [54].

## 8. Conclusion

The determination of customer grade partition boundaries in RFM value stratification represents a multifaceted challenge that sits at the intersection of statistical methodology, algorithmic optimization, and business strategy. This comprehensive examination has revealed that effective boundary determination requires careful consideration of multiple complementary approaches [55].

Quintile-based segmentation provides a statistically grounded foundation that adapts to data distributions, while custom threshold segmentation enables alignment with domain expertise and strategic priorities. Weighted composite scoring introduces strategic flexibility by reflecting differential dimension importance. Algorithmic approaches—particularly K-means clustering with the Elbow Method and Expectation-Maximization clustering—allow data-driven boundary discovery that reveals natural customer groupings [56].

The practical implementation of boundary determination demands attention to data quality, preprocessing rigor, and dynamic adjustment mechanisms. Industry-specific adaptations ensure that boundaries reflect the unique value drivers within each business context, while validation techniques including Silhouette Score analysis and segment profile validation confirm boundary effectiveness [57].

As organizations increasingly recognize customer segmentation as a strategic capability, the sophistication of boundary determination methodologies continues to advance. The integration of additional dimensions, hierarchical clustering for multi-resolution segmentation, and machine learning for complex pattern recognition represents the frontier of boundary determination practice [58].

The optimal approach to customer grade partition boundary determination likely combines multiple methodologies—leveraging the statistical rigor of clustering algorithms, the strategic flexibility of weighted scoring, and the interpretability of decision tree rules. By thoughtfully integrating these approaches within the context of specific business objectives and customer base characteristics, organizations can establish boundaries that meaningfully differentiate customer grades and enable effective, targeted customer relationship management [59].

---

## References

[1] Akande et al., "Customer Segmentation Strategy Combining RFM Analysis and K-Means Clustering," Ceddi Journal of Information System and Technology (JST), 2024, 3(1): 14–25.

[2] Express Analytics, "RFM Analysis for Customer Segmentation," Express Analytics Blog, 2024.

[3] Clevertap, "RFM Analysis," Clevertap Blog, 2024.

[4] Uju Emmanuella, "The Complete RFM Analysis Guide," Medium, 2024.

[5] Shirvaron, "Customer Segmentation Implementing the RFM Model with SQL," Medium, 2024.

[6] Harsh1995hg, "Beyond Top Spenders: The Complete Guide to RFM Customer Segmentation with SQL," Medium, 2024.

[7] Radhityan, "Understanding RFM Analysis for Effective Marketing," Medium, 2024.

[8] Bloomreach, "RFM Segmentation," Bloomreach Documentation, 2024.

[9] Smartico, "Guide to RFM Modeling," Smartico Blog, 2024.

[10] Research.abo.fi, "Segmenting Retail Customers with Enhanced RFM Data using a Hybrid Regression-Clustering Method," Åbo Akademi University Research Publications, 2024.

[11] arXiv, "Customer Segmentation Problem Analysis," arXiv preprint arXiv:2505.08136, 2025.

[12] Lezhnina & Kismihók, "Cluster Validation Methods," 2022.

[13] Onumanyi et al., "Optimal Cluster Number Determination," 2022.

[14] Mouton et al., "Cluster Quantity Assessment," 2020.

[15] Anitha & Patil, "RFM Clustering Outcomes," 2022.

[16] Hu et al., "Customer Segmentation Strategy," 2020.

[17] Hu et al., "RFM Analysis Extensions," 2023.

[18] Express Analytics, "RFM Analysis in Different Industries," 2024.

[19] Express Analytics, "Measuring RFM Analysis Success," 2024.

[20] Uju Emmanuella, "RFM Scoring System Setup," 2024.

[21] Shirvaron, "Weighted RFM Scoring," 2024.

[22] Harsh1995hg, "RFM Segment Assignment," 2024.

[23] Radhityan, "Normalization of RFM Data," 2024.

[24] arXiv, "K-Means Clustering in Customer Segmentation," 2025.

[25] Express Analytics, "K-Means Clustering for Customer Segmentation," 2024.

[26] Radhityan, "K-Means Clustering with Elbow Method," 2024.

[27] Akande et al., "Elbow Curve Approach," 2024.

[28] Lezhnina & Kismihók, "Explained Variance Against Number of Clusters," 2022.

[29] Research.abo.fi, "EM Clustering Algorithm," 2024.

[30] Research.abo.fi, "Expectation-Maximization Steps," 2024.

[31] Express Analytics, "GMM Clusters and Probabilistic Assignment," 2024.

[32] Express Analytics, "Decision Tree Classifier for RFM," 2024.

[33] Express Analytics, "Probability Trees for RFM Analysis," 2024.

[34] Express Analytics, "Data Quality Considerations," 2024.

[35] Uju Emmanuella, "Privacy Considerations in RFM," 2024.

[36] Radhityan, "Min-Max Scaling for RFM," 2024.

[37] Express Analytics, "Dynamic Segmentation," 2024.

[38] Express Analytics, "Seasonal Variations in RFM," 2024.

[39] Uju Emmanuella, "Real-Time RFM Analysis," 2024.

[40] Express Analytics, "RFM Analysis in Different Industries," 2024.

[41] Uju Emmanuella, "RFM Applications by Industry," 2024.

[42] Express Analytics, "Industry-Specific RFM Applications," 2024.

[43] Express Analytics, "Model Evaluation and Comparison," 2024.

[44] Express Analytics, "GMM Silhouette Score," 2024.

[45] Express Analytics, "Clustering Algorithm Comparison," 2024.

[46] Express Analytics, "Radar Chart of Customer Profiles," 2024.

[47] Akande et al., "Segment Distribution Analysis," 2024.

[48] Akande et al., "Mean Value per RFM Segment," 2024.

[49] Research.abo.fi, "Customer Change Rate (C) Variable," 2024.

[50] Research.abo.fi, "Enhanced RFM with Trend Analysis," 2024.

[51] Express Analytics, "Hierarchical Clustering Approaches," 2024.

[52] Smartico, "Micro-Segmentation with RFM," 2024.

[53] Express Analytics, "Advanced RFM Analysis Techniques," 2024.

[54] Express Analytics, "Implementation Challenges," 2024.

[55] Akande et al., "Customer Segmentation Framework," 2024.

[56] Uju Emmanuella, "Step-by-Step RFM Implementation," 2024.

[57] Express Analytics, "Best Practices for RFM Analysis," 2024.

[58] Smartico, "Beyond Basic RFM: Advanced Implementation," 2024.

[59] Uju Emmanuella, "RFM vs. Other Segmentation Methods," 2024.

## Annotations


## Sources
[1] https://arxiv.org/pdf/2505.08136
[2] https://clevertap.com/blog/rfm-analysis/
[3] https://documentation.bloomreach.com/engagement/docs/rfm-segmentation
[4] https://journal.ceddi.id/index.php/jst/article/download/81/49
[5] https://medium.com/@UjuEmmanuella/the-complete-rfm-analysis-guide-how-to-boost-marketing-roi-by-targeting-your-most-valuable-53a4bdfe7c89
[6] https://medium.com/@harsh1995hg/beyond-top-spenders-the-complete-guide-to-rfm-customer-segmentation-with-sql-27ec1925962b
[7] https://medium.com/@radhityan/understanding-rfm-analysis-for-effective-marketing-c21bc1e3b6bb
[8] https://medium.com/@shirvaron/customer-segmentation-implementing-the-rfm-model-with-sql-8d07fd990d32
[9] https://research.abo.fi/ws/files/25261378/Segmenting%20Retail%20Customers%20with%20Enhanced%20RFM%20Data%20using%20a%20Hybrid%20RegressionClustering%20Method.pdf
[10] https://www.expressanalytics.com/blog/rfm-analysis-customer-segmentation
[11] https://www.smartico.ai/blog-post/guide-rfm-modeling