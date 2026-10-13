# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 299c71da | **Time:** 106.48s | **Cost:** $0.11551
--------------------------------------------------------------------------------

# What Sets the Similarity Threshold for Substitute Recommendations in Shopping Basket Analysis?

## Abstract

This research report examines the fundamental question of how similarity thresholds are determined for substitute product recommendations within shopping basket analysis. The determination of appropriate similarity thresholds represents a critical challenge in recommendation system design, balancing the need for relevant suggestions against the risk of overwhelming users with irrelevant alternatives. Drawing upon established principles from market basket analysis, collaborative filtering methodologies, and contemporary e-commerce research, this report synthesizes the key factors that influence threshold selection, including product attribute weighting, category-specific considerations, clustering algorithm characteristics, and empirical optimization through A/B testing. The findings indicate that effective similarity thresholds emerge from a multifaceted approach that combines domain-specific attribute analysis, algorithmic considerations, and continuous performance evaluation through controlled experimentation.

## 1. Introduction

The landscape of e-commerce has been fundamentally transformed by recommendation systems, which leverage sophisticated algorithms to present users with products they are likely to purchase. Within this ecosystem, substitute recommendations occupy a particularly important niche, serving customers who seek alternatives to products they are currently viewing or have already added to their shopping baskets. Unlike complementary recommendations, which suggest products that work alongside a primary item, substitute recommendations identify products that can fulfill a similar function or purpose, thereby enabling comparison shopping and facilitating purchase decisions when the original item is unavailable, unsuitable, or competitively priced.

The effectiveness of substitute recommendations hinges critically on the similarity threshold—the boundary that determines which products are deemed sufficiently alike to be recommended as alternatives. Setting this threshold too high results in recommendations that are too narrow, potentially missing relevant alternatives that could satisfy customer needs. Conversely, setting the threshold too low produces recommendations that are too broad, including products that share only superficial similarities and failing to provide genuine value to the shopping experience. This fundamental tension between precision and recall defines much of the challenge in threshold determination.

Market basket analysis provides the foundational methodology for discovering relationships among products in transaction datasets. As described in the research literature, market basket analysis "methodically examines customer buying patterns to reveal correlations among various items in their shopping carts," with the primary aim of "ascertaining the things commonly bought together by customers" [1]. While traditional market basket analysis focuses primarily on complementary relationships—items purchased together—extending these techniques to identify substitutes requires careful consideration of what constitutes meaningful similarity in the context of product substitution.

The question of what sets the similarity threshold for substitute recommendations is therefore multidimensional, encompassing technical considerations of algorithm design, business considerations of customer experience, and empirical considerations of performance optimization. This report synthesizes insights from the academic literature and industry practices to provide a comprehensive understanding of the factors that influence threshold selection and the methodologies available for optimizing these critical parameters.

## 2. Theoretical Framework

### 2.1 Market Basket Analysis and Association Rule Mining

Market basket analysis employs association rule mining algorithms to discover interesting relationships between items in transaction datasets. Each transaction represents a customer's purchase, and the items within are analyzed to identify patterns of co-occurrence. The fundamental metrics used in association rule mining—support, confidence, and lift—provide the building blocks for understanding product relationships, though these metrics must be adapted when the goal shifts from identifying complementary products to identifying substitutes.

Support measures the frequency with which an itemset appears in transactions, while confidence measures the probability that item B is purchased given that item A has been purchased. Lift indicates the strength of association beyond what would be expected if the items were independent. For substitute recommendations, these traditional metrics must be supplemented with similarity measures that capture the degree of functional equivalence between products rather than their co-purchase behavior.

The Apriori algorithm represents a classic approach to association rule mining, generating frequent itemsets through iterative passes over the transaction database [2]. While effective for identifying complementary products, the Apriori framework requires extension when applied to substitution scenarios, where the goal is to identify products that compete for the same purchase decision rather than products that are purchased together.

### 2.2 The Nature of Substitute Products

Understanding what constitutes a substitute product is essential for establishing appropriate similarity thresholds. According to economic principles, "a substitute product can replace another, since it typically has the same form, fit, and function as a preferred item" [3]. The substitutability between products exists along a spectrum, from perfect substitutes that are virtually indistinguishable to imperfect substitutes that share only some functional characteristics.

The relationship between substitute products has direct implications for demand dynamics. As noted in the economic literature, "there is a relationship between the demand schedules of substitute products. If the price of a product goes up, the demand for a substitute will tend to increase" [3]. This economic principle underscores why substitute recommendations are valuable to retailers: they capture customers who might otherwise abandon a purchase due to price concerns or unavailability.

For recommendation purposes, substitutes can be categorized along several dimensions. Close substitutes, such as different brands of the same product category, share nearly identical attributes and can serve as direct replacements. Broader substitutes, such as coffee and tea, fulfill the same underlying need (caffeination or hot beverage consumption) while differing substantially in form and characteristics. The appropriate similarity threshold must account for this spectrum of substitutability, potentially using different thresholds for different categories of products.

### 2.3 Recommendation System Approaches

Contemporary recommendation systems employ several fundamental approaches to generating product suggestions, each with distinct implications for similarity threshold determination.

Content-based filtering generates recommendations by evaluating the similarity of items based on their attributes and features. This method "utilizes features such as product attributes, descriptions, and user preferences to identify items that closely match those already in the user's cart" [4]. For substitute recommendations, content-based approaches examine product features to identify items that share sufficient characteristics to serve as viable alternatives. The similarity threshold in content-based systems is typically defined in terms of feature overlap or distance in a multidimensional attribute space.

Collaborative filtering recommends products by analyzing user-item interactions across the entire dataset. This method "identifies patterns and similarities in user behavior, such as purchase history or item ratings, to generate recommendations" [4]. For substitute recommendations, collaborative filtering can identify products that customers view or purchase as alternatives to each other, even when the products share few explicit attributes. The similarity threshold in collaborative systems reflects the strength of behavioral co-occurrence patterns.

Hybrid approaches combine content-based and collaborative methods, potentially offering the most robust framework for substitute recommendations. The integration of these approaches allows systems to leverage both explicit product attributes and implicit behavioral signals when determining substitutability.

## 3. Factors Influencing Similarity Thresholds

### 3.1 Product Attribute Weighting

The relative importance of different product attributes for determining substitutability varies significantly across product categories. Research on assortment optimization has demonstrated that "all attributes did not contribute equally to the notion of substitutability. In fact the key attribute for substitutability would vary based on the category in consideration" [5]. This observation has profound implications for threshold setting, as it suggests that a universal similarity threshold is unlikely to be optimal across all product categories.

Consider the example provided in the research literature: "among razors, the retailer carries products from the same brand but targeting different genders so one has to ensure that if the customer was looking for Venus razors, they are not recommended Gillette for men since both the products share the same brand name. Hence, the attribute gender is very important for this category" [5]. In this case, gender represents a critical attribute that must be weighted heavily in similarity calculations, and the similarity threshold must be set to ensure that products differing on this attribute are not recommended as substitutes.

Conversely, for categories where certain attributes are implicit or less relevant, the weighting scheme must be adjusted accordingly. This category-specific variation in attribute importance necessitates either category-specific thresholds or adaptive threshold mechanisms that adjust based on the product category under consideration.

### 3.2 Category Characteristics and Market Structure

The structure of the product category influences appropriate similarity thresholds in several ways. In categories with dense substitution possibilities—where many products compete for the same customer needs—lower similarity thresholds may be appropriate to surface the full range of alternatives. In sparse categories, where genuine substitutes are limited, higher thresholds may be necessary to ensure that recommended alternatives are meaningful.

The competitive dynamics within a category also matter. In monopolistic competition, where products are differentiated through branding or perceived quality differences, "companies are not price-takers, meaning demand is not highly sensitive to price" [3]. In such contexts, similarity thresholds must account for the fact that products may be imperfect substitutes due to utility differences that are not fully captured by product attributes.

The distinction between perfect and imperfect substitutes has practical implications for recommendation design. Perfect substitutes, such as "gasoline from a gas station on one corner" that is "virtually indistinguishable from gasoline sold by another station on the opposite corner" [3], require very high similarity thresholds to ensure that recommendations are meaningful. Imperfect substitutes, such as generic versus brand-name medications that are "nearly indistinguishable chemically, but... not perfect substitutes due to the utility consumers may get—or believe they get—from purchasing a brand name" [3], require more nuanced threshold setting that accounts for perceived as well as actual differences.

### 3.3 User Behavior and Shopping Context

The effectiveness of substitute recommendations depends on understanding the context in which customers seek alternatives. Product detail page views "reveal specific product interest even before cart addition. The sequence and duration of these views provide context about the shopping journey. A visitor who examines multiple similar products signals comparison shopping, suggesting alternative recommendations might be effective" [6].

This behavioral signal suggests that similarity thresholds should be calibrated not only to product characteristics but also to the stage of the shopping journey. Customers in active comparison mode may benefit from broader recommendations that span a wider similarity range, while customers who have already committed to a product may prefer more focused suggestions that offer alternatives only when the primary option is unavailable or unsuitable.

The distinction between comparison shopping and complementary shopping is crucial for recommendation placement and threshold setting. Alternative product recommendations "serve an important function for comparison shoppers. These 'you might also like' or 'similar products' sections help customers explore options within the same category" [6]. For these recommendations to be effective, they must balance the need to present genuine alternatives against the risk of overwhelming customers with too many choices.

### 3.4 Clustering Algorithm Characteristics

The choice of clustering algorithm for identifying substitute products has direct implications for threshold determination. Research comparing clustering approaches for grocery shopping optimization found that "affinity propagation emerges as the more suitable clustering algorithm due to its compatibility with distance-based clustering and its effectiveness in handling sparse matrices" [7]. Affinity propagation "excels in scenarios where pairwise connections among items are limited, making it well suited for optimizing grocery shopping lists with potentially sparse relationships between products."

In contrast, "agglomerative clustering can be adapted for grocery shopping optimization by appropriately setting distance thresholds" [7], but it "is more reliant on dense graphs to perform optimally." This suggests that the appropriate similarity threshold depends on the underlying clustering approach, with affinity propagation potentially tolerating lower similarity thresholds due to its ability to handle sparse relationships, while agglomerative clustering may require higher thresholds to ensure meaningful cluster formation.

The research also notes that "affinity propagation tends to shine when dealing with larger shopping lists due to its ability to handle sparse matrices effectively, making it a robust choice for comprehensive grocery shopping optimization. Conversely, agglomerative clustering exhibits better performance with smaller lists by setting appropriate distance thresholds, capitalizing on the strength of dense graphs" [7]. This observation suggests that dynamic threshold strategies, which adjust based on the size and density of the product set under consideration, may outperform static threshold approaches.

## 4. Optimization Strategies

### 4.1 A/B Testing Methodologies

A/B testing provides the empirical foundation for optimizing similarity thresholds in production recommendation systems. As described in the literature, "A/B testing is a statistical method used to compare two versions (A and B) of a web page, product feature, or machine learning model to determine which one performs better on a specific metric" [8]. For substitute recommendations, A/B testing allows practitioners to evaluate different threshold configurations against real user behavior, moving beyond theoretical considerations to empirically grounded optimization.

The application of A/B testing to recommendation pod optimization has been demonstrated in practice. For example, one e-commerce platform tested different orders of recommendation pods, comparing "Compare similar products first (control)" against "'You may also like' first (proposed variant B)" and "'Use it with' first (proposed variant C)" [9]. While this particular test focused on pod placement rather than similarity thresholds, the methodology is directly applicable to threshold optimization.

A/B testing provides several advantages for threshold optimization. First, it "provides empirical data that can help make decisions that improve user experience, increase revenue, enhance performance, and drive product development based on actual user behavior rather than assumptions" [8]. Second, it enables "clear insights into which model performs better for a specific task" [8], allowing direct comparison of different threshold configurations. Third, it supports "fine-tuning the model to enhance user satisfaction and engagement" [8], facilitating iterative improvement of recommendation quality.

### 4.2 Precision-Recall Trade-offs

The fundamental trade-off between precision and recall defines much of the challenge in setting similarity thresholds for substitute recommendations. Precision measures the proportion of recommended items that are relevant, while recall measures the proportion of relevant items that are recommended. As noted in the recommendation systems literature, "precision and recall often pull in opposite directions, creating a balancing act that defines much of recommendation system design. Improving one usually means sacrificing the other; a classic inverse relationship that can be tricky to manage" [10].

For substitute recommendations, this trade-off manifests directly in threshold selection. Higher similarity thresholds increase precision by ensuring that only highly similar products are recommended, but decrease recall by excluding borderline cases that might be relevant to some users. Lower thresholds increase recall by casting a wider net, but decrease precision by including products that may not serve as genuine substitutes.

The appropriate balance between precision and recall depends on the specific application context. "Different applications demand different balances" [10], and substitute recommendations are no exception. In categories where incorrect recommendations carry high costs—either in terms of customer frustration or lost sales—higher precision may be preferred, even at the cost of lower recall. In categories with many potential substitutes and low cost for incorrect recommendations, higher recall may be more valuable.

The precision-recall curve provides a tool for visualizing this trade-off across different threshold values. "To understand performance across different classification thresholds, you can plot a precision-recall curve. This graph shows how precision and recall trade off as you adjust the confidence level for recommending items" [10]. Higher curves, "closer to the top-right corner, indicate a model with better overall performance" [10], and the area under this curve (AUC-PR) provides a single-number summary of overall recommendation quality.

The F1 score, which "combines precision and recall as their harmonic mean" [10], offers a balanced metric for threshold optimization when no single dimension is prioritized. However, in practice, business metrics such as conversion rate, average order value, or revenue per session may provide more actionable objectives for threshold optimization.

### 4.3 Dynamic Threshold Strategies

Static similarity thresholds may be suboptimal because the appropriate threshold varies based on product characteristics, user context, and category structure. Dynamic threshold strategies, which adjust the threshold based on contextual factors, offer a potential solution to this limitation.

Research on clustering algorithms suggests that "an intriguing approach would involve a dynamic strategy that leverages both algorithms based on the size of the shopping list" [7]. While this observation specifically addresses algorithm selection, the same logic applies to threshold setting: different contexts may warrant different threshold values.

Several factors could inform dynamic threshold adjustment. Product category could trigger category-specific thresholds that reflect the typical density of substitutes in that category. User behavior signals, such as the duration of product page views or the number of products examined, could indicate whether the user is in comparison mode and therefore receptive to broader recommendations. Business constraints, such as inventory levels or promotional priorities, could influence thresholds to favor in-stock items or promoted products.

The implementation of dynamic thresholds requires careful consideration of interpretability and debugging. Static thresholds are straightforward to analyze and adjust, while dynamic thresholds may produce unexpected results in edge cases. A practical approach might begin with static thresholds optimized through A/B testing, then gradually introduce dynamic adjustments as confidence in the underlying model grows.

## 5. Practical Implementation Considerations

### 5.1 Attribute Extraction and Representation

The quality of substitute recommendations depends fundamentally on the quality of product attribute representation. Content-based recommendation approaches "utilize features such as product attributes, descriptions, and user preferences to identify items that closely match those already in the user's cart" [4]. For substitute recommendations, these features must capture the dimensions along which products can substitute for each other.

Product attributes for substitution may include functional attributes (what the product does), form attributes (what the product is), performance attributes (how well the product performs), and aesthetic attributes (how the product looks). The relative importance of these attribute categories varies by product type, reinforcing the need for category-specific threshold considerations.

Beyond structured attributes, unstructured text such as product descriptions can provide valuable signals for substitutability. Natural language processing techniques can extract semantic features from descriptions, enabling similarity calculations that capture functional equivalence even when products use different terminology to describe the same capabilities.

### 5.2 Similarity Metric Selection

The choice of similarity metric determines how product attributes are translated into similarity scores, which are then compared against the threshold to generate recommendations. Common similarity metrics include cosine similarity, Euclidean distance, Jaccard similarity, and more sophisticated measures designed for specific data types.

Traditional similarity metrics in collaborative filtering "may lead to unreasonable similarity between users or items" [11] when applied without consideration of the specific characteristics of the recommendation domain. For substitute recommendations, the metric should capture functional equivalence rather than mere attribute overlap. Products that share different attributes but serve the same purpose may be better substitutes than products that share many attributes but serve different purposes.

Zhang's metric, used in market basket analysis for measuring association strength, provides one approach to capturing non-obvious relationships [2]. The metric is computed as:

$$
\text{Zhang's Metric} = \frac{\text{support}(X \cap Y) - \text{support}(X)\text{support}(Y)}{\max\{\text{support}(X \cap Y)(1 - \text{support}(X)), \text{support}(X)(\text{support}(Y) - \text{support}(X \cap Y))\}}
$$

This metric captures the degree to which the co-occurrence of items exceeds what would be expected by chance, potentially identifying substitute relationships where customers view or purchase one item in lieu of another.

### 5.3 Evaluation and Continuous Improvement

The optimization of similarity thresholds is not a one-time exercise but an ongoing process of measurement, analysis, and refinement. A/B testing provides the primary mechanism for this continuous improvement, allowing practitioners to test threshold changes against baseline performance and quantify the impact on business metrics.

Beyond A/B testing, offline evaluation metrics can provide rapid feedback during development. Precision, recall, and F1 score can be computed on held-out transaction data, allowing comparison of different threshold configurations without the time and resource requirements of live testing. However, offline metrics may not fully capture the complexity of user behavior, making online testing essential for final validation.

The research literature emphasizes that "A/B testing tells you how effective these pods are relative to your standard recommendations" [9], suggesting that threshold optimization should be conducted in the context of the broader recommendation strategy. Changes to similarity thresholds may interact with other aspects of the recommendation system, including the selection of candidate products, the ordering of recommendations, and the visual presentation of results.

## 6. Conclusion

The similarity threshold for substitute recommendations in shopping basket analysis emerges from the intersection of multiple considerations, including product attribute analysis, category-specific dynamics, user behavior patterns, and algorithmic characteristics. Rather than a single universal threshold, effective recommendation systems employ nuanced approaches that account for the multidimensional nature of product substitutability.

The evidence suggests that successful threshold determination requires attention to several key factors. First, attribute weighting must reflect category-specific importance, as "the key attribute for substitutability would vary based on the category in consideration" [5]. Second, the clustering approach influences appropriate threshold values, with affinity propagation and agglomerative clustering exhibiting different performance characteristics across list sizes and densities [7]. Third, A/B testing provides essential empirical validation, enabling optimization based on actual user behavior rather than theoretical considerations [8].

The precision-recall trade-off remains a fundamental constraint in threshold selection, requiring practitioners to balance the cost of missed recommendations against the cost of irrelevant suggestions. Dynamic threshold strategies that adjust based on context offer potential advantages over static approaches, though they introduce additional complexity in implementation and interpretation.

As e-commerce continues to evolve, the importance of effective substitute recommendations will only increase. Customers increasingly expect to find relevant alternatives when browsing products, and retailers benefit from capturing comparison shopping behavior that might otherwise result in abandoned purchases. The thoughtful determination of similarity thresholds, grounded in both theoretical understanding and empirical optimization, represents a critical capability for recommendation systems seeking to deliver value to both customers and businesses.

Future research directions include the development of automated threshold optimization techniques, the integration of real-time behavioral signals into dynamic threshold adjustment, and the exploration of deep learning approaches that may learn optimal similarity boundaries directly from data. The fundamental question of what sets the similarity threshold will continue to require careful attention as recommendation systems become more sophisticated and as customer expectations continue to rise.

---

## References

[1] Acadlore. (2024). Market Basket Analysis. *Journal of Scientific Agriculture*, 4(2).

[2] Medium. (2023). Market Basket Analysis: Apriori Algorithm Using Zhang's Metric.

[3] Investopedia. (2025). What Is a Substitute? *Investopedia*.

[4] IIETA. (2024). Product Recommendation Systems. *Journal of Software*.

[5] MLG Workshop. (2020). Assortment Optimization with Product Substitution. *Proceedings of the MLG Workshop*.

[6] Nacelle. (2024). Product Recommendations: AI-Driven Strategies for E-commerce Growth.

[7] MDPI. (2024). Clustering Algorithms for Grocery Shopping Optimization. *Future Internet*, 16(8).

[8] Medium. (2023). Demystifying A/B Testing in Machine Learning.

[9] Constructor. (2025). A/B Testing Strategies to Drive More Revenue Through Recommendations.

[10] Shaped. (2024). Relevancy, Precision, and Recall in Recommendation Systems.

[11] Core. (2015). Similarity Metrics in Recommendation Systems. *PhD Thesis*.

## Annotations


## Sources
[1] https://arxiv.org/html/2507.02643v1
[2] https://arxiv.org/pdf/2403.18536
[3] https://constructor.com/blog/ab-testing-strategies-to-drive-more-revenue-through-recommendations
[4] https://core.ac.uk/download/pdf/38107215.pdf
[5] https://link.springer.com/article/10.1007/s10660-019-09352-9
[6] https://medium.com/@iuyasik/market-basket-analysis-apriori-algorithm-using-zhangs-metric-708406fc5dfc
[7] https://medium.com/@weidagang/demystifying-a-b-testing-in-machine-learning-a923fe07018d
[8] https://medium.com/headspace-engineering/mindful-experimentation-evaluate-recommendation-system-performance-using-a-b-testing-at-headspace-3c8c05d0ae3b
[9] https://nacelle.com/blog/product-recommendations-ai-driven-strategies-for-ecommerce-growth
[10] https://neptune.ai/blog/recommender-systems-metrics
[11] https://norma.ncirl.ie/5171/1/harikrishnankannan.pdf
[12] https://site.warrington.ufl.edu/kumar/files/2023/07/How-do-recomemndations-help-consumer-search-products.pdf
[13] https://tech.instacart.com/how-instacart-uses-machine-learning-to-suggest-replacements-for-out-of-stock-products-8f80d03bb5af
[14] https://towardsai.net/p/l/market-basket-analysis-for-retail-growth
[15] https://www.acadlore.com/article/JOSA/2024_2_2/josa020201
[16] https://www.analyticsvidhya.com/blog/2021/10/a-comprehensive-guide-on-market-basket-analysis/
[17] https://www.applexus.com/blogs/market-basket-analysis-in-retail-and-cpg-analytics-to-increase-revenue
[18] https://www.businessperspectives.org/images/pdf/applications/publishing/templates/article/assets/19781/IM_2024_01_Ahmed.pdf
[19] https://www.charuaggarwal.net/sim.pdf
[20] https://www.cs.umd.edu/~samir/498/schafer01ecommerce.pdf
[21] https://www.evidentlyai.com/ranking-metrics/precision-recall-at-k
[22] https://www.iieta.org/download/file/fid/140187
[23] https://www.investopedia.com/terms/s/substitute.asp
[24] https://www.mdpi.com/1999-5903/16/8/277
[25] https://www.mlgworkshop.org/2020/papers/MLG2020_paper_7.pdf
[26] https://www.shaped.ai/blog/relevancy-precision-and-recall
[27] https://www.statsig.com/perspectives/ab-testing-recommender-systems
[28] https://www.techscience.com/jbd/v4n1/47664/html
[29] https://www.turing.com/kb/market-basket-analysis