# Deep Research Report: qwen/qwen-2.5-72b-instruct
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 23d92a4a | **Time:** 67.09s | **Cost:** $0.07469
--------------------------------------------------------------------------------

# Research Report: What Sets the Similarity Threshold for Substitute Recommendations in Shopping Basket Analysis?

## Abstract
This report delves into the methodologies and metrics used to set the similarity threshold for substitute recommendations in shopping basket analysis. By leveraging large-scale shopping cart data, we explore how conditional probabilities, association scores, and similarity metrics are employed to identify substitutable items. The report also discusses the implications of these methods on recommendation accuracy and user satisfaction in e-commerce settings.

## 1. Introduction
In the realm of e-commerce, the ability to recommend substitute products when a desired item is out of stock is crucial for maintaining customer satisfaction and driving sales. Shopping basket analysis, a subset of market basket analysis, focuses on identifying patterns in customer purchases to recommend items that are likely to be substitutable. This report examines the key metrics and techniques used to set the similarity threshold for substitute recommendations, ensuring that the recommended items are indeed suitable replacements.

## 2. Methodology
### 2.1 Conditional Probability
The conditional probability of choosing an item given another item is in the basket is a fundamental metric in shopping basket analysis. For items \( c \) and \( c' \), the conditional probability \( P(k|c) \) and \( P(k|c') \) are used to estimate the substitutability of \( c \) and \( c' \). The substitution score \( S(c, c') \) is defined as:

\[
S(c, c') = 1 - \left| P(k|c) - P(k|c') \right|
\]

The more similar the probabilities, the higher the substitution score, indicating a higher degree of substitutability [1].

### 2.2 Association Score
The association score (AS) is another critical metric used to identify substitutable products. It is defined as:

\[
AS(A \rightarrow B) = \frac{P(A \cap B)}{P(A)P(B)}
\]

Where:
- \( P(A \cap B) \) is the probability that both items \( A \) and \( B \) are purchased together.
- \( P(A) \) and \( P(B) \) are the individual probabilities of purchasing items \( A \) and \( B \), respectively.

If \( AS(A \rightarrow B) > 1 \), it indicates that the presence of item \( B \) increases the likelihood of purchasing item \( A \), suggesting substitutability [2].

### 2.3 Similarity Metrics
Various similarity metrics are used to measure the similarity between items or users. Common metrics include:

- **Cosine Similarity**: Measures the cosine of the angle between two vectors. It is defined as:

\[
\text{cosine\_similarity}(A, B) = \frac{A \cdot B}{\|A\| \|B\|}
\]

- **Jaccard Similarity**: Measures the ratio of the size of the intersection to the size of the union of two sets. It is defined as:

\[
\text{Jaccard\_similarity}(A, B) = \frac{|A \cap B|}{|A \cup B|}
\]

- **Pearson Correlation**: Measures the linear correlation between two variables. It is defined as:

\[
\text{pearson\_correlation}(A, B) = \frac{\sum (A_i - \bar{A})(B_i - \bar{B})}{\sqrt{\sum (A_i - \bar{A})^2} \sqrt{\sum (B_i - \bar{B})^2}}
\]

### 2.4 Reinforcement Learning
Reinforcement learning (RL) is a dynamic approach that adjusts recommendations based on user interactions. RL-based recommendation engines optimize recommendations by continuously learning from user feedback, making them highly adaptive to changing user preferences [3].

## 3. Application in E-Commerce
### 3.1 Substitution Policies
Effective substitution policies are crucial in post-purchase stock-out (PP-OOS) scenarios. Online grocery retailers often suggest substitutions based on past purchase records, which have been shown to increase acceptance rates. The category differentiation (horizontal vs. vertical) also plays a significant role in determining the dominant attribute matching policy. For example, matching on flavor is more effective in horizontally differentiated categories, while brand matching is more suitable for vertically differentiated categories [4].

### 3.2 Personalization and User Engagement
Personalization techniques, such as user-based and item-based collaborative filtering, enhance the relevance of recommendations. By combining these techniques with content-based filtering, e-commerce platforms can provide more accurate and diverse recommendations. Contextual factors, such as user location, time of day, and device type, further refine the recommendation process, ensuring that the suggested items are highly relevant to the user's current context [5].

## 4. Case Studies and Empirical Results
### 4.1 Performance of Similarity Metrics
An empirical study comparing different similarity metrics in recommender systems found that Cosine Similarity and Jaccard Similarity performed better than other metrics for both RMSE and MAE. The Jaccard Coefficient, in particular, showed the lowest RMSE and MAE values, indicating its high accuracy in predicting user-item ratings [6].

### 4.2 Market Basket Analysis
Market basket analysis has been successfully applied to identify substitutable products in various e-commerce settings. For instance, a study on shoe sizes used market basket analysis to recommend the correct size for a desired product, taking into account the variations in size conventions across different brands [7].

## 5. Conclusion
The similarity threshold for substitute recommendations in shopping basket analysis is set using a combination of conditional probabilities, association scores, and similarity metrics. These methods ensure that the recommended items are highly substitutable, enhancing user satisfaction and driving sales. Future research should focus on integrating advanced machine learning techniques, such as reinforcement learning, to further optimize the recommendation process and improve the overall user experience.

## References
1. Tickr. (2023). Identifying Substitutable Goods Using Large-Scale Shopping Cart Basket Data. Retrieved from https://tickr.com/identifying-substitutable-goods-using-large-scale-shopping-cart-basket-data/
2. Combinatorial Press. (2023). Optimisation of e-commerce Personalised Recommendation Algorithms Driven by Neural Network Models. Retrieved from https://combinatorialpress.com/article/jcmcc/Volume%20127/Volume%20127a/Optimisation%20of%20e-commerce%20personalised%20recommendation%20algorithms%20driven%20by%20neural%20network%20models.pdf
3. Lumen Alta. (2023). 7 Machine Learning Algorithms for Recommendation Engines. Retrieved from https://lumenalta.com/insights/7-machine-learning-algorithms-for-recommendation-engines
4. ScienceDirect. (2023). "Sorry, the product you ordered is out of stock": Effects of Substitution Policy in Online Grocery Retailing. Retrieved from https://www.sciencedirect.com/science/article/pii/S002243592200046X
5. IRJET. (2023). Analysing the Performance of Recommendation System Using Different Similarity Metrics. Retrieved from https://www.irjet.net/archives/V10/i4/IRJET-V10I485.pdf
6. Amazon Science. (2023). Recommending Product Sizes to Customers. Retrieved from https://assets.amazon.science/e0/1f/f6eff24d42858edc71ab97d8d7e8/recommending-product-sizes-to-customers.pdf
7. Medium. (2023). High Performance and Reliable Market Basket Analysis Using Item-to-Item Collaborative Filtering. Retrieved from https://sirlcern3.medium.com/high-performance-and-reliable-market-basket-analysis-using-item-to-item-collaborative-filtering-81e24cbf40d2

## Annotations


## Sources
[1] https://arxiv.org/pdf/2108.05891
[2] https://assets.amazon.science/e0/1f/f6eff24d42858edc71ab97d8d7e8/recommending-product-sizes-to-customers.pdf
[3] https://combinatorialpress.com/article/jcmcc/Volume%20127/Volume%20127a/Optimisation%20of%20e-commerce%20personalised%20recommendation%20algorithms%20driven%20by%20neural%20network%20models.pdf
[4] https://datascience.stackexchange.com/questions/5121/applications-and-differences-for-jaccard-similarity-and-cosine-similarity
[5] https://docs.acquia.com/customer-data-platform/market-basket-analysis
[6] https://eajournals.org/wp-content/uploads/sites/21/2025/05/AI-Powered-Recommendation-Engines.pdf
[7] https://ecyang.medium.com/similar-product-recommendations-data-to-deployment-970a085bafce
[8] https://hal.science/hal-04182275v1/document
[9] https://ijfans.org/uploads/paper/377e3169c159ea4b8b3a77e68aa47494.pdf
[10] https://ijireeice.com/wp-content/uploads/2025/03/IJIREEICE.2025.13309.pdf
[11] https://lumenalta.com/insights/7-machine-learning-algorithms-for-recommendation-engines
[12] https://medium.com/@anicomanesh/evolution-of-recommendation-algorithms-part-i-fundamentals-and-classical-recommendation-bb1c0bce78a9
[13] https://medium.com/beyond-the-build/deep-dive-into-content-based-recommender-systems-unveiling-the-power-of-attribute-based-48d27fc98812
[14] https://pdfs.semanticscholar.org/ae0a/02d661716af3451b7e73bda12692a208856c.pdf
[15] https://scispace.com/pdf/product-matching-lessons-and-recommendations-from-a-real-51qyozuu3s.pdf
[16] https://sirlcern3.medium.com/high-performance-and-reliable-market-basket-analysis-using-item-to-item-collaborative-filtering-81e24cbf40d2
[17] https://site.warrington.ufl.edu/kumar/files/2023/07/How-do-recomemndations-help-consumer-search-products.pdf
[18] https://tickr.com/identifying-substitutable-goods-using-large-scale-shopping-cart-basket-data/
[19] https://www.amazon.science/the-history-of-amazons-recommendation-algorithm
[20] https://www.baeldung.com/cs/amazon-recommendation-system
[21] https://www.bloomreach.com/en/blog/ecommerce-product-recommendation-engine
[22] https://www.irjet.net/archives/V10/i4/IRJET-V10I485.pdf
[23] https://www.mlgworkshop.org/2020/papers/MLG2020_paper_7.pdf
[24] https://www.nature.com/articles/s41598-025-02593-9
[25] https://www.sciencedirect.com/science/article/pii/S002243592200046X
[26] https://www.sciencedirect.com/topics/computer-science/market-basket-analysis
[27] https://www.scitepress.org/Papers/2023/121355/121355.pdf
[28] https://www.shaped.ai/blog/ai-powered-recommendation-engines
[29] https://www.vldb.org/pvldb/vol9/p636-mann.pdf