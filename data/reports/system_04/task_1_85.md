# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** bd5e40f4 | **Time:** 433.60s | **Cost:** $1.37519
--------------------------------------------------------------------------------

# Comprehensive Analysis of Similarity Threshold Determination in Substitute Recommendation Systems

### Key Points
*   **Multidimensional Determination:** The similarity threshold is rarely a single static number; it is a dynamic decision boundary determined by a convergence of attribute similarity (text/image), statistical co-occurrence metrics (Lift/Leverage), and business constraints (profit margins/inventory).
*   **Metric-Dependent Thresholds:** The nature of the threshold depends heavily on the underlying metric: Jaccard similarity often utilizes fixed empirical cutoffs (e.g., 0.5–0.7), while embedding-based methods (Cosine Similarity) and Market Basket Analysis (Lift < 1) require distribution-based or optimized thresholds to balance precision and recall.
*   **Machine Learning Optimization:** Modern systems increasingly treat the threshold as a hyperparameter tuned via supervised learning (e.g., maximizing F1-scores) or dynamic ranking models (e.g., Learning-to-Rank, Top-K approximation) rather than manual specification.
*   **Business Logic Integration:** Final thresholds are frequently adjusted by "post-processing" layers that incorporate real-time inventory levels, profit margins, and "cannibalization" risks, ensuring that a mathematically similar substitute is also economically viable.

---

## 1. Introduction

In the domain of retail analytics and e-commerce, the identification of substitute products is a critical function for managing out-of-stock (OOS) scenarios and optimizing inventory. Unlike complementary products, which are purchased together (e.g., chips and salsa), substitute products are mutually exclusive items that fulfill the same consumer need (e.g., two different brands of organic whole milk). The core challenge in automating substitute recommendations lies in defining the **similarity threshold**: the quantitative cutoff point that separates a valid substitute from an irrelevant item.

This report provides an exhaustive analysis of the factors and methodologies that set this threshold. It explores how thresholds are derived from mathematical similarity functions, statistical market basket analysis (MBA), machine learning optimization, and strategic business constraints.

## 2. Theoretical Foundations of Similarity Metrics

The determination of a threshold is intrinsically linked to the mathematical properties of the similarity metric employed. Different metrics distribute similarity scores differently, necessitating distinct strategies for setting cutoffs.

### 2.1 Attribute-Based Similarity and Jaccard Distance
For products defined by categorical attributes (e.g., "Gluten-Free," "Organic," "Brand Name"), the Jaccard similarity coefficient is a standard measure. It quantifies similarity as the size of the intersection of attribute sets divided by the size of the union.

\[
J(A, B) = \frac{|A \cap B|}{|A \cup B|}
\]

Research indicates that for multi-valued attributes in food retail, thresholds are often set empirically. For instance, a baseline approach may classify products as substitutes if the Jaccard distance of their names or attribute sets exceeds a fixed value, such as **0.5** or **0.7** [cite: 1, 2, 3].
*   **Threshold Behavior:** A threshold of 0.5 implies that products must share at least 50% of their defining attributes.
*   **Limitations:** Fixed thresholds in Jaccard similarity can be rigid. If a product has sparse attributes, a single mismatch can drop the score below the threshold, necessitating a lower, more lenient cutoff [cite: 1].

### 2.2 Vector Space Models and Cosine Similarity
In modern recommendation systems, products are often represented as dense vectors (embeddings) derived from textual descriptions (using BERT, Word2Vec) or images. Cosine similarity measures the cosine of the angle between two non-zero vectors, providing a value between -1 and 1.

\[
\text{similarity} = \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}
\]

*   **Threshold Setting:** Unlike Jaccard, cosine similarity thresholds are often determined by analyzing the distribution of scores across the entire catalog. A common approach is to set a threshold that captures the **Top-K** nearest neighbors or to use a percentile-based cutoff (e.g., the top 5% of similar pairs) [cite: 4, 5].
*   **Semantic Nuance:** Embeddings capture semantic relationships (e.g., "soda" vs. "pop"). However, they lack a "ground truth" for similarity, often requiring manual monitoring or visualization (e.g., 3D plots) to calibrate the threshold so that distinct categories (e.g., dog food vs. cat food) do not merge [cite: 6].

### 2.3 Numeric and Relative Difference
For numerical attributes (e.g., weight, volume, price), similarity is often calculated using relative difference.
*   **Binary Thresholding:** A simplistic approach sets the similarity to 1 if values are identical and 0 otherwise. This is often too strict for substitutes (e.g., 500g vs. 450g pasta) [cite: 1].
*   **Fuzzy Thresholding:** More sophisticated systems use a relative difference function, where a threshold (e.g., $\lambda$) determines the acceptable variance. For example, products might be considered similar if their weight differs by less than 10% [cite: 1].

## 3. Market Basket Analysis: The Role of Lift and Negative Association

Traditional Market Basket Analysis (MBA) focuses on finding items that co-occur (complements). However, identifying substitutes requires inverting this logic or looking for **structural equivalence**.

### 3.1 The "Negative Lift" Threshold
The **Lift** metric measures the strength of an association rule $A \Rightarrow B$.

\[
\text{Lift}(A \Rightarrow B) = \frac{\text{Support}(A \cup B)}{\text{Support}(A) \times \text{Support}(B)}
\]

*   **Lift > 1:** Indicates positive correlation (Complements).
*   **Lift = 1:** Indicates independence.
*   **Lift < 1:** Indicates negative correlation (Substitutes).

For substitute recommendations, the threshold is effectively **Lift < 1**. This signifies that the purchase of Product A *decreases* the likelihood of purchasing Product B, which is characteristic of substitutes (e.g., a customer buys Coke or Pepsi, but rarely both in the same transaction) [cite: 7, 8, 9, 10].
*   **Cannibalization Analysis:** Retailers use this "negative lift" threshold to identify products that cannibalize each other's sales. If the lift is significantly below 1, the system flags the items as potential substitutes [cite: 11, 12].

### 3.2 Structural Equivalence in Networks
Since substitutes rarely appear in the same basket, direct co-occurrence data is sparse. Network analysis uses **structural equivalence** to set thresholds. Two products are structurally equivalent if they share the same set of neighbors (i.e., they are bought with the same complementary items).
*   **Thresholding Strategy:** Instead of a simple co-occurrence threshold, the system calculates the similarity of the *neighborhoods* of two products. A threshold is applied to this second-order similarity (e.g., Cosine similarity of the neighbor vectors) to identify substitutes [cite: 13, 14, 15].

## 4. Machine Learning and Optimization Approaches

In advanced systems, the similarity threshold is not a manually chosen heuristic but a learned parameter or a dynamic output of a model.

### 4.1 Supervised Learning and Hyperparameter Tuning
The threshold can be treated as a hyperparameter in a supervised learning problem.
*   **Objective Function:** The optimal threshold is found by maximizing a performance metric such as **F1-Score**, **Accuracy**, or **AUC** (Area Under the Curve) on a validation dataset [cite: 1, 16, 17].
*   **Grid Search:** Researchers perform grid searches over potential threshold values (e.g., 0.05 to 0.95) to find the "sweet spot" that balances Precision (relevance of substitutes) and Recall (quantity of substitutes found) [cite: 18].
*   **Classification Models:** Algorithms like Random Forest or Support Vector Machines (SVM) can implicitly learn non-linear thresholds by training on labeled pairs of "substitute" vs. "non-substitute" items [cite: 1].

### 4.2 Dynamic and Adaptive Thresholds (K-Adapt)
Fixed thresholds fail when user preferences or product densities vary (e.g., a "strict" threshold might work for common items like milk but return zero results for niche items like vegan gluten-free cookies).
*   **K-Adapt Framework:** Recent research proposes frameworks like **K-Adapt**, which dynamically determine the prediction set size (Top-K) for each user or product query. Instead of a global threshold, the system learns a calibrated threshold based on user utility metrics and risk control, ensuring that the number of recommendations adapts to the certainty of the model [cite: 19].
*   **Differentiable Top-K:** Techniques like **DFTopK** allow the Top-K selection process (typically non-differentiable) to be trained end-to-end within deep learning models. This allows the "thresholding" logic to be optimized via gradient descent during model training [cite: 20, 21].

### 4.3 The Instacart Case Study
Instacart's approach to substitute recommendations illustrates a hybrid system where thresholds are applied at multiple stages [cite: 22, 23]:
1.  **Candidate Generation (Heuristic Thresholds):** Initial candidates are retrieved using heuristics like **Levenshtein distance** (text similarity) and taxonomy matching. A loose threshold is applied here to ensure high recall (capturing 95% of potential replacements).
2.  **Ranking (Learned Scores):** A deep learning model (Siamese network/Two-tower architecture) scores the candidates based on features like price difference, brand affinity, and dietary labels.
3.  **Final Decision (Probability Threshold):** The model outputs a probability score (e.g., 0.653). A final threshold determines if the item is shown to the user. This threshold is calibrated based on offline metrics (AUC, Log-loss) and online A/B testing (user acceptance rates).

## 5. Business and Operational Constraints

While mathematical similarity is the starting point, business rules often dictate the final effective threshold.

### 5.1 Profitability and Margin Management
Patented systems describe methods where the similarity threshold is adjusted based on financial outcomes.
*   **Margin-Based Filtering:** A system may identify a group of substitutes using a similarity score threshold (e.g., cosine similarity > X). However, this list is further filtered to prioritize items with higher profit margins or those where a discount can be negotiated [cite: 24, 25].
*   **Dynamic Pricing:** The threshold for what constitutes a "viable" substitute may shift based on the price elasticity of the product. If a substitute is too expensive (e.g., >20% price hike), it may be rejected regardless of attribute similarity [cite: 11, 26].

### 5.2 Inventory and Availability
The "threshold" is effectively infinite if an item is out of stock. Real-time systems integrate inventory data to dynamically filter the list of substitutes.
*   **Availability Constraints:** Recommendations are strictly limited to items currently available in the specific store location. This binary constraint acts as a hard filter that overrides similarity scores [cite: 27, 28].

### 5.3 The Precision-Recall Trade-off in Retail
Retailers must balance the risk of showing a bad substitute (low precision) against the risk of showing nothing (low recall).
*   **High Threshold (Conservative):** High precision, low recall. Used for sensitive categories (e.g., baby formula, medication) where an incorrect substitute is unacceptable.
*   **Low Threshold (Aggressive):** Low precision, high recall. Used for generic categories (e.g., paper towels) where users are more flexible.
*   **Tuning:** The threshold is often adjusted empirically to maximize "conversion" (the user accepts the substitute) while minimizing "rejection" or bad customer experience [cite: 16, 29, 30].

## 6. Summary of Threshold Determination Methods

The following table summarizes the primary methods for setting similarity thresholds as identified in the research:

| Method | Metric Used | Threshold Determination Logic | Typical Application |
| :--- | :--- | :--- | :--- |
| **Heuristic / Rule-Based** | Jaccard, Levenshtein | Fixed values (e.g., 0.5, 0.7) based on domain expertise. | Baseline models, simple attribute matching [cite: 1, 2]. |
| **Distributional** | Cosine Similarity | Percentile-based (e.g., Top 5%) or Top-K neighbors. | Embedding-based retrieval, vector search [cite: 4, 5]. |
| **Market Basket Analysis** | Lift, Confidence | Lift < 1 (Substitutes) or Lift > 1 (Complements). | Transaction mining, cannibalization analysis [cite: 7, 8]. |
| **Supervised Learning** | Probability Score | Optimized to maximize F1-Score, AUC, or Accuracy. | Advanced recommender systems (e.g., Instacart) [cite: 18, 22]. |
| **Network Analysis** | Structural Equivalence | Similarity of neighbor vectors (second-order). | Identifying substitutes in sparse transaction data [cite: 13, 15]. |
| **Business Logic** | Margin, Price | Adjusted dynamically to maximize profit or clear inventory. | Retail management systems, dynamic pricing [cite: 24, 25]. |

## 7. Conclusion

The similarity threshold for substitute recommendations is not a singular, universal constant. It is a **composite parameter** derived from the interplay of data characteristics (sparsity, dimensionality), algorithm choice (Jaccard vs. Embeddings), and business objectives (profit vs. customer satisfaction).

While basic systems may rely on static thresholds (e.g., Jaccard > 0.5), state-of-the-art implementations like those at Instacart and Amazon utilize **dynamic, learned thresholds**. These are optimized via deep learning to maximize the probability of user acceptance, constrained by hard business rules regarding inventory and price. The evolution of this field is moving toward **differentiable ranking** and **adaptive K** methods, where the system autonomously determines the optimal number and quality of substitutes to present for every unique query, effectively removing the need for manual threshold tuning.

**Sources:**
1. [diva-portal.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_iMa_Nwd2X_h3AOeMnbgbiolL8JUJCqtw-qTiNvx7f5jk3Ei2hntT-Vt6qKj4WjMeTT-KdwmtUtGX1I7Vd6fNP5EGU6osqnVemrAKeOKqGG4s_IreBIS_8B5MMXXDWs1CTjNam0-rubntLHY4sk1Ix-G8FQ==)
2. [plos.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4_RWeYcJYRBbxU0BvDpV1kO8RBCF2Xxrm-aqYmM6xpwVVivh69wn2eYST_k4VrBTw1sG6iPEtTi1PpVqFQ1OP56yea8horGSX1PUdB9h_yTaqzzTANHGPNhDYcYYjcbQcgir3tWXcdv2IdTDShVys0KMYSAzPG_cKTZ3hF7kU)
3. [ibm.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpVlll3twjmOynye2SaZJtgh7kpgINuXSlMueAeLbwRd1K-GyIs-2rFXUx7atW_F4ctxKDliEuXRznRsBTCynIy9O0SQjUP8yImueXA6xfHv_D7lp9J2fanDx9EBkkw2O9PmU8RRO-IRMwPbF0)
4. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkfv9HkiP7g0mcLr_4oHkq0tJaU2BCrSyu_EsD5W2IAl25G2urYDYv5ghcJVKMPbXSN7a5-aXc00g6srQ37FgTeA81U8tNnREDYSBgjqJwVU59rEn2JpJE4zeaghtespqiqpnCPDtlmAIBzdAKyDz_S4Cm35WGUeSmxLP2xZW1tj03kRIQp7ClZa-VXvOxeZW5uA==)
5. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHn89zrSW2_TSolKa4B3mxnOLhL3RW-sNTGrLUJOnkSMjBKYOMjJzBp5er_6DtFmziPvApTzobOEnSOQ5je2FiTkHiNruPlFuoDJc6daNfoplLGVXro3HnrAPHfsJFKF2XLLzC8vqTeCnYdyxLzmKNunLByTCgmAJzeV2VwfNKwdKZzhsLo4GmdeatIbMi8)
6. [dunnhumby.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHSyTAEPgAZahAb19X8yYWYtdFwMPyjGK6pYwYz_Lgbp6fBvi9AlJteXeriz1dxfQ3CNDXC7nDumFptIWqHKqprHj_o_c7lTtX74bMOJBueoWHHUlKBDl6-Xz_ZnYgPahL51DSVigJfvwsMSc8-ZpTuGdNz7mH4Xmj5EbX-dvQKhd2CymBhELFdAvv-UQXaiIH3roVmrK6jIMCa1wYJ_wcmJJD6UHYfbzf26bMNp4PSujlFA==)
7. [streamlit.app](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFL5123QW_oxH2wqq3vXQ7voHztjLdDvdAH6y7THcJOJzYJbKAmUJsW2F-DQifkK-4CDbK3rmmk62hokbN913L5a6xEiIwrAyJm2ysjsDyHm6RHGEwhApzwbg_j0lMW4VBoi77c_iV4FKc=)
8. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqhRGr23jVpzMPL_Jya_sr02L_qbZJBNkpW1MUJGp8kNVqA8nUNnrvu-UnrQs-mKwHu66XcpsbIsebaIv0YGFPJcBmlmWR5CY2BlmZlJPlenz8_c2117gxbCVqRPcuL4L-supGNK1SoShc_844SlzoPoB6Uk7Bvt8H5R_w5tITKDfZ_CXUZ0Cx368c6FAbBexGJzQnDC5bZV5AEk5AXK7W8Nswm8g1gTwzxcvA3wD4-uS2CU_Zf4aDNBkpSEg=)
9. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElklRGIwU5U6mpYi076ItqNMry8GaWT4CnfiYqpHoAa1_Hln7iIM4B8tSoC3SOkiiWqXcG6v_uoMLqAbydUEcKutIrKei5X0Ws_LAXB9fIyq_yxoNKRvC7o2Aezvimxh8PPFk5zW8aZQ2aut40)
10. [turing.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVXD1Qh8bohG-4GNoTGfTiKm3biKGKF5VSid-nilWLs5fvjLXEKl5kmYNaHmpIspkvgZHrQPwFWAQXhs-65Y3LM6vP-3dQFjvUXMhj__FF-PevaPDOPkRqOQvxsCWaw7uZ_bN1jQE=)
11. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzNgzw4aABYvSgrbBkfNGEd4HicTakJMXHWEW283FhOjpFRdqChdWDzJMe8NvElGTk6ImTGeMX43Z5Vfyc9KKdj7ERK5UgNJHFAijRIsi-Ybbwe9uFfi4gS5DUy5IbDhbOxdhjd6ll81cf)
12. [billigence.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnPKRkHVuNNIL_Q_9mIzgUNm8LSB8pL0gjGMGy15nPmk5CSC0sYMs5sa--n24ioenyJsVfWEeNNvm1kAuyyEk7_iu87DLOuo0Y6g0cTpMlzmExkisoM8TArNr4_ZOIwkidR1NfcgAL2Ds539d_7CbwmpMZkG-wh8u5RJrTATw=)
13. [unu-merit.nl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlRc4Q0BT3DWB_wf7mS6D95oI7GT8hRK0Yp8hFRTe8NXirB0-TC0yWsc5_jHRnRxZ6ZIRxb8ZtNQV4p-_z-J4SuvgcTfvPyXnks_d9AX0Q3Dr8KQKAMJQfmkT5Wf_vkeXRlp25o4zrlwTRvDfs799Wmw==)
14. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOMZYqzW4qH63hGu43hXxt7W4WMozNwTdaJ7JhPC3-CSkfc6p2YXsBQDijhy5-XmN9Bu3e4DfgLdIBWhY6y-jb1MV4XGxzVVmsRe4S_qwjst4oHIy9zJJC4NwKuoIXJyCzGqNFYkPZF9zH6hqNdxl6K0RGvU1ppDrJF0DCu4fdo7HC1TQh3qH1H316gIRkMbP0IlLJv-61TKb5vWdCTKw7DdF40aNgVOPKMk78fUphN-2kk0XF)
15. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbcuqWn_yhShqXOnd2IN7yA-F9GEv3uKQ3VLFZ0CRnejG7W5dFOd70tHVDcCvXp5nifPAawHEj_b-FZRi0qbSzglZIQnE8LirJ50POuxqndt932zvdmnlabtFuT-37Ynqx4ljN2hnhemXCj9TLQvxYFOQ6vIJTOz0=)
16. [stackexchange.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETkM8W3uEgpq2058NUa_59dl3Lr_7J3eTWJgro_rOKLOoLoKj1OC6HJe9cYkTa-LukTS-droou6BahroO4aPtrsCjkqSseO2dBOpPastQiC8CujWB01rtpmEyL9GjK9ltvKBIjv1e6et64xdU16-X30uJVgdJQGzHpCY3t5i3I4AjI88d6VhqqrC0=)
17. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEX-2_2vC9s39Zrxh1JK94SpUbBm0WdIFo98VXxHieMHdQrSoA4s3C3Jz2k-mUhO0iSi3huCDBauhgIqgRUQfNWCdhY6fkehfgeSg5Q0da1o7PxVw0ROmvmWIKVALYLSM2GFGqeCc10UmQI1pPOpDjV2Xcrilp53lb-CQlxlJmhyWcyNPvt2eBKpOecv0995q6xFgnG2Gk=)
18. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFDMW6TYAspbAxpxp9gJLMfRjMyo13Gys4lFck2jAMRnGAZ4qK5gJ_SNw3V47YU8fqS9WTQAcfFz4lYurw5n-xd1_9g_HGJI_LbPGwRzlitesw8fO698HlYTfdnJ_Juw==)
19. [openreview.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPZWRSitiPbJRvksevabGr0ggJAqUXcqp_I19I5XjHrUVa9Z2jja-ZREmmZJFpBEIinbMC07QeqbYFCWqybsoOY4XFPw-gfiEikArfkATgJk1HLZm6fu7i9MDgL7dAiT4=)
20. [themoonlight.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfJ21AJYC22OK-SI8REYrZPNeh17WrftscAsxuZ6aV9wsQHDabBLBV82CEvx5uycmsMAAoxoY6q2YDlpXOrIzFlcIDJdzB0fIZx_1JU2fNHy2yY2vRG8jq-u0vyPfkU-YxDgjVRZ4O0HlrLMw7YDWJt5rY-23_F6lwm4l_unZ153OK8jtvm-ZwzMz5gp0O9RIyG7g3fUuGdBNQfoZ-fg==)
21. [emergentmind.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG62rm76Oklj63CfNes64JQ_27hGx1FLFofm7yByn6pBJ6rGXQZZEGfB-eGYKI6aLcA02jSDrCGMhOdiksiYpKON4NDqWlWoOYydKWr_YFq7kVulJ21RYLQzJNDgroVvyNV5QOY4uiIowBCZY6jJcJRs6lXFEl2OM0=)
22. [instacart.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEen1TgxzZaCmPhsxe1DdBb8d85Dr75bi8td2KMte59z6qrQGIL9mSyzarUqGh0pXSJ2UH3DYPzh_K3s-aEglP2z-0ZxXpA2eIKS8b_GGhtF02c_66pzW5voE4rV72gmMhHwFLLsy-2E0-9ftIq9-YHI_9L4xWiOkBudZgodaKsmIF7b-Bxs9QBHBMrkPsTLxDmnHqtrKSejGyTo4bo7_COaGEnPuXK4eb922CsHswQ48injQ==)
23. [datatinkerer.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHu5QwqIcMnRP5da3KslQZzzv8Ge7woQbVLx33lkqftx0leQqwXtRLl52pL2ewB_ihNAfNYmsn3yZDIPaRYNtI69635aOe-4Jx_R0vLjPc-8hg7txNz3UycNY0nfRxl7gCDNdN5KxCDhk7upyH7UiRPbfPdya28zwIpvM-lt6za)
24. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkVm1IInpx_-TsvgLeSuIMLiguSMwht2frUEWQvArYcmpoMBrWsbtk63cCJRdzwsjBuHVD4cd8UIz68kaq2QG4uMmG_IOAJzGJwukwLhgD9KuCG8G3Ucwj48nQ2sXlPfXKc4EQij9P-8NG)
25. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuhbxHaWLb4AKTHa4TScsFV20qiV0cFOU5t5PuBUY_cZ2_AYTnwJAOOsgSquWFsMubC9q_uNIDHKS_20yp7HnEGs_HEBzA9ZlVJFEdosw-O5e3dRplO9nYU1lC_3jitxNL-KRCithp)
26. [towardsdatascience.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_KE-07z7RjLv-DRynyEMlNpF-rn58a-73iCrz_UpQI9gIn8sH7KwvtWkkaFiLmFYW9wBd4jj5RfQ56sEcH2xSpWld6N4pLADCp47dTcL0EjGbLjxmFg8uAN7vnjt3UhKY3Z6HhKaPUx7_qK218rj02TH3Udv-edmGKUJnWO_gU4zBVcAhrjHMMIWImA1LkhfQVQ2JHgvzTbsMz7Dvqsk=)
27. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYocezHSR9epI8zvLW1ursj5zGXt4Ce8479Obvd5wTSZ2HkNL5wBJhnZr40ptzKMX38k4WUwtsZIxB63ceAU7ILtAXhEh00rPXJtJrdkWzPXMZVG7IBH6h82kvAUK7fsw2G3-eFQVEGva0)
28. [instacart.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAIW0lNErd2W32iXSE1UtB03bi3G0zMQKIw4Q6hcHr5n1QDWSb_yyYABqMaEa39qlYpV_xJag-B2U0ItMw0mP6dyr81oXN9TleIysEozdazk_K6SgJ1OQbLigFDypINsgfMN7dOcck_fN_7D8pBdN4nnUhbo8=)
29. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKmdctkcUdP6_cbzCXVt_RgmnT_S-6ooNBOIoVNl_x9llrONaMplCHK0u1cCM1U-8GrKYIcSK9Ol9lgY4a-mO2fvVuxSDIF4SDrHAPtKVXDdtzE-BBqnngEL5FXxjPSj3dnCfe3tVTVimFbJ7MHRjnz6MLxDU1meorpDD4IWjpMFWLTLI6MTo=)
30. [apxml.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmMeLftNvNHOU6j8OzSEi3czcIL2BkSMjR1mqzmptwuDpmDcCHo5cMEFnmm9jBitibhr5VBFOYetU27FICvc91sP6iG2-JqRxMiEZl2fp7m6lLFyOwFwbn18I0-Z3vCnbeYUsCkLj5MaMdOJuLJZU3KE7mSxri34fjhxmJT2V2_T3lW8W1ez38MIign8P9ijkDQ51r5H_bHZ9RS7rzX-PGOc15Y6n5w63EveBLEoU=)


## Annotations
Annotation(end_index=3197, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpVlll3twjmOynye2SaZJtgh7kpgINuXSlMueAeLbwRd1K-GyIs-2rFXUx7atW_F4ctxKDliEuXRznRsBTCynIy9O0SQjUP8yImueXA6xfHv_D7lp9J2fanDx9EBkkw2O9PmU8RRO-IRMwPbF0', start_index=3182)
Annotation(end_index=3197, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_iMa_Nwd2X_h3AOeMnbgbiolL8JUJCqtw-qTiNvx7f5jk3Ei2hntT-Vt6qKj4WjMeTT-KdwmtUtGX1I7Vd6fNP5EGU6osqnVemrAKeOKqGG4s_IreBIS_8B5MMXXDWs1CTjNam0-rubntLHY4sk1Ix-G8FQ==', start_index=3182)
Annotation(end_index=3197, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4_RWeYcJYRBbxU0BvDpV1kO8RBCF2Xxrm-aqYmM6xpwVVivh69wn2eYST_k4VrBTw1sG6iPEtTi1PpVqFQ1OP56yea8horGSX1PUdB9h_yTaqzzTANHGPNhDYcYYjcbQcgir3tWXcdv2IdTDShVys0KMYSAzPG_cKTZ3hF7kU', start_index=3182)
Annotation(end_index=3542, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_iMa_Nwd2X_h3AOeMnbgbiolL8JUJCqtw-qTiNvx7f5jk3Ei2hntT-Vt6qKj4WjMeTT-KdwmtUtGX1I7Vd6fNP5EGU6osqnVemrAKeOKqGG4s_IreBIS_8B5MMXXDWs1CTjNam0-rubntLHY4sk1Ix-G8FQ==', start_index=3533)
Annotation(end_index=4314, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkfv9HkiP7g0mcLr_4oHkq0tJaU2BCrSyu_EsD5W2IAl25G2urYDYv5ghcJVKMPbXSN7a5-aXc00g6srQ37FgTeA81U8tNnREDYSBgjqJwVU59rEn2JpJE4zeaghtespqiqpnCPDtlmAIBzdAKyDz_S4Cm35WGUeSmxLP2xZW1tj03kRIQp7ClZa-VXvOxeZW5uA==', start_index=4302)
Annotation(end_index=4314, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHn89zrSW2_TSolKa4B3mxnOLhL3RW-sNTGrLUJOnkSMjBKYOMjJzBp5er_6DtFmziPvApTzobOEnSOQ5je2FiTkHiNruPlFuoDJc6daNfoplLGVXro3HnrAPHfsJFKF2XLLzC8vqTeCnYdyxLzmKNunLByTCgmAJzeV2VwfNKwdKZzhsLo4GmdeatIbMi8', start_index=4302)
Annotation(end_index=4636, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHSyTAEPgAZahAb19X8yYWYtdFwMPyjGK6pYwYz_Lgbp6fBvi9AlJteXeriz1dxfQ3CNDXC7nDumFptIWqHKqprHj_o_c7lTtX74bMOJBueoWHHUlKBDl6-Xz_ZnYgPahL51DSVigJfvwsMSc8-ZpTuGdNz7mH4Xmj5EbX-dvQKhd2CymBhELFdAvv-UQXaiIH3roVmrK6jIMCa1wYJ_wcmJJD6UHYfbzf26bMNp4PSujlFA==', start_index=4627)
Annotation(end_index=4988, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_iMa_Nwd2X_h3AOeMnbgbiolL8JUJCqtw-qTiNvx7f5jk3Ei2hntT-Vt6qKj4WjMeTT-KdwmtUtGX1I7Vd6fNP5EGU6osqnVemrAKeOKqGG4s_IreBIS_8B5MMXXDWs1CTjNam0-rubntLHY4sk1Ix-G8FQ==', start_index=4979)
Annotation(end_index=5253, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_iMa_Nwd2X_h3AOeMnbgbiolL8JUJCqtw-qTiNvx7f5jk3Ei2hntT-Vt6qKj4WjMeTT-KdwmtUtGX1I7Vd6fNP5EGU6osqnVemrAKeOKqGG4s_IreBIS_8B5MMXXDWs1CTjNam0-rubntLHY4sk1Ix-G8FQ==', start_index=5244)
Annotation(end_index=6249, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElklRGIwU5U6mpYi076ItqNMry8GaWT4CnfiYqpHoAa1_Hln7iIM4B8tSoC3SOkiiWqXcG6v_uoMLqAbydUEcKutIrKei5X0Ws_LAXB9fIyq_yxoNKRvC7o2Aezvimxh8PPFk5zW8aZQ2aut40', start_index=6230)
Annotation(end_index=6249, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFL5123QW_oxH2wqq3vXQ7voHztjLdDvdAH6y7THcJOJzYJbKAmUJsW2F-DQifkK-4CDbK3rmmk62hokbN913L5a6xEiIwrAyJm2ysjsDyHm6RHGEwhApzwbg_j0lMW4VBoi77c_iV4FKc=', start_index=6230)
Annotation(end_index=6249, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqhRGr23jVpzMPL_Jya_sr02L_qbZJBNkpW1MUJGp8kNVqA8nUNnrvu-UnrQs-mKwHu66XcpsbIsebaIv0YGFPJcBmlmWR5CY2BlmZlJPlenz8_c2117gxbCVqRPcuL4L-supGNK1SoShc_844SlzoPoB6Uk7Bvt8H5R_w5tITKDfZ_CXUZ0Cx368c6FAbBexGJzQnDC5bZV5AEk5AXK7W8Nswm8g1gTwzxcvA3wD4-uS2CU_Zf4aDNBkpSEg=', start_index=6230)
Annotation(end_index=6249, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVXD1Qh8bohG-4GNoTGfTiKm3biKGKF5VSid-nilWLs5fvjLXEKl5kmYNaHmpIspkvgZHrQPwFWAQXhs-65Y3LM6vP-3dQFjvUXMhj__FF-PevaPDOPkRqOQvxsCWaw7uZ_bN1jQE=', start_index=6230)
Annotation(end_index=6492, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnPKRkHVuNNIL_Q_9mIzgUNm8LSB8pL0gjGMGy15nPmk5CSC0sYMs5sa--n24ioenyJsVfWEeNNvm1kAuyyEk7_iu87DLOuo0Y6g0cTpMlzmExkisoM8TArNr4_ZOIwkidR1NfcgAL2Ds539d_7CbwmpMZkG-wh8u5RJrTATw=', start_index=6478)
Annotation(end_index=6492, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzNgzw4aABYvSgrbBkfNGEd4HicTakJMXHWEW283FhOjpFRdqChdWDzJMe8NvElGTk6ImTGeMX43Z5Vfyc9KKdj7ERK5UgNJHFAijRIsi-Ybbwe9uFfi4gS5DUy5IbDhbOxdhjd6ll81cf', start_index=6478)
Annotation(end_index=7135, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbcuqWn_yhShqXOnd2IN7yA-F9GEv3uKQ3VLFZ0CRnejG7W5dFOd70tHVDcCvXp5nifPAawHEj_b-FZRi0qbSzglZIQnE8LirJ50POuxqndt932zvdmnlabtFuT-37Ynqx4ljN2hnhemXCj9TLQvxYFOQ6vIJTOz0=', start_index=7117)
Annotation(end_index=7135, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOMZYqzW4qH63hGu43hXxt7W4WMozNwTdaJ7JhPC3-CSkfc6p2YXsBQDijhy5-XmN9Bu3e4DfgLdIBWhY6y-jb1MV4XGxzVVmsRe4S_qwjst4oHIy9zJJC4NwKuoIXJyCzGqNFYkPZF9zH6hqNdxl6K0RGvU1ppDrJF0DCu4fdo7HC1TQh3qH1H316gIRkMbP0IlLJv-61TKb5vWdCTKw7DdF40aNgVOPKMk78fUphN-2kk0XF', start_index=7117)
Annotation(end_index=7135, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlRc4Q0BT3DWB_wf7mS6D95oI7GT8hRK0Yp8hFRTe8NXirB0-TC0yWsc5_jHRnRxZ6ZIRxb8ZtNQV4p-_z-J4SuvgcTfvPyXnks_d9AX0Q3Dr8KQKAMJQfmkT5Wf_vkeXRlp25o4zrlwTRvDfs799Wmw==', start_index=7117)
Annotation(end_index=7670, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETkM8W3uEgpq2058NUa_59dl3Lr_7J3eTWJgro_rOKLOoLoKj1OC6HJe9cYkTa-LukTS-droou6BahroO4aPtrsCjkqSseO2dBOpPastQiC8CujWB01rtpmEyL9GjK9ltvKBIjv1e6et64xdU16-X30uJVgdJQGzHpCY3t5i3I4AjI88d6VhqqrC0=', start_index=7653)
Annotation(end_index=7670, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEX-2_2vC9s39Zrxh1JK94SpUbBm0WdIFo98VXxHieMHdQrSoA4s3C3Jz2k-mUhO0iSi3huCDBauhgIqgRUQfNWCdhY6fkehfgeSg5Q0da1o7PxVw0ROmvmWIKVALYLSM2GFGqeCc10UmQI1pPOpDjV2Xcrilp53lb-CQlxlJmhyWcyNPvt2eBKpOecv0995q6xFgnG2Gk=', start_index=7653)
Annotation(end_index=7670, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_iMa_Nwd2X_h3AOeMnbgbiolL8JUJCqtw-qTiNvx7f5jk3Ei2hntT-Vt6qKj4WjMeTT-KdwmtUtGX1I7Vd6fNP5EGU6osqnVemrAKeOKqGG4s_IreBIS_8B5MMXXDWs1CTjNam0-rubntLHY4sk1Ix-G8FQ==', start_index=7653)
Annotation(end_index=7909, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFDMW6TYAspbAxpxp9gJLMfRjMyo13Gys4lFck2jAMRnGAZ4qK5gJ_SNw3V47YU8fqS9WTQAcfFz4lYurw5n-xd1_9g_HGJI_LbPGwRzlitesw8fO698HlYTfdnJ_Juw==', start_index=7899)
Annotation(end_index=8129, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_iMa_Nwd2X_h3AOeMnbgbiolL8JUJCqtw-qTiNvx7f5jk3Ei2hntT-Vt6qKj4WjMeTT-KdwmtUtGX1I7Vd6fNP5EGU6osqnVemrAKeOKqGG4s_IreBIS_8B5MMXXDWs1CTjNam0-rubntLHY4sk1Ix-G8FQ==', start_index=8120)
Annotation(end_index=8775, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPZWRSitiPbJRvksevabGr0ggJAqUXcqp_I19I5XjHrUVa9Z2jja-ZREmmZJFpBEIinbMC07QeqbYFCWqybsoOY4XFPw-gfiEikArfkATgJk1HLZm6fu7i9MDgL7dAiT4=', start_index=8765)
Annotation(end_index=9063, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfJ21AJYC22OK-SI8REYrZPNeh17WrftscAsxuZ6aV9wsQHDabBLBV82CEvx5uycmsMAAoxoY6q2YDlpXOrIzFlcIDJdzB0fIZx_1JU2fNHy2yY2vRG8jq-u0vyPfkU-YxDgjVRZ4O0HlrLMw7YDWJt5rY-23_F6lwm4l_unZ153OK8jtvm-ZwzMz5gp0O9RIyG7g3fUuGdBNQfoZ-fg==', start_index=9049)
Annotation(end_index=9063, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG62rm76Oklj63CfNes64JQ_27hGx1FLFofm7yByn6pBJ6rGXQZZEGfB-eGYKI6aLcA02jSDrCGMhOdiksiYpKON4NDqWlWoOYydKWr_YFq7kVulJ21RYLQzJNDgroVvyNV5QOY4uiIowBCZY6jJcJRs6lXFEl2OM0=', start_index=9049)
Annotation(end_index=9240, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEen1TgxzZaCmPhsxe1DdBb8d85Dr75bi8td2KMte59z6qrQGIL9mSyzarUqGh0pXSJ2UH3DYPzh_K3s-aEglP2z-0ZxXpA2eIKS8b_GGhtF02c_66pzW5voE4rV72gmMhHwFLLsy-2E0-9ftIq9-YHI_9L4xWiOkBudZgodaKsmIF7b-Bxs9QBHBMrkPsTLxDmnHqtrKSejGyTo4bo7_COaGEnPuXK4eb922CsHswQ48injQ==', start_index=9226)
Annotation(end_index=9240, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHu5QwqIcMnRP5da3KslQZzzv8Ge7woQbVLx33lkqftx0leQqwXtRLl52pL2ewB_ihNAfNYmsn3yZDIPaRYNtI69635aOe-4Jx_R0vLjPc-8hg7txNz3UycNY0nfRxl7gCDNdN5KxCDhk7upyH7UiRPbfPdya28zwIpvM-lt6za', start_index=9226)
Annotation(end_index=10589, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuhbxHaWLb4AKTHa4TScsFV20qiV0cFOU5t5PuBUY_cZ2_AYTnwJAOOsgSquWFsMubC9q_uNIDHKS_20yp7HnEGs_HEBzA9ZlVJFEdosw-O5e3dRplO9nYU1lC_3jitxNL-KRCithp', start_index=10575)
Annotation(end_index=10589, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkVm1IInpx_-TsvgLeSuIMLiguSMwht2frUEWQvArYcmpoMBrWsbtk63cCJRdzwsjBuHVD4cd8UIz68kaq2QG4uMmG_IOAJzGJwukwLhgD9KuCG8G3Ucwj48nQ2sXlPfXKc4EQij9P-8NG', start_index=10575)
Annotation(end_index=10855, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_KE-07z7RjLv-DRynyEMlNpF-rn58a-73iCrz_UpQI9gIn8sH7KwvtWkkaFiLmFYW9wBd4jj5RfQ56sEcH2xSpWld6N4pLADCp47dTcL0EjGbLjxmFg8uAN7vnjt3UhKY3Z6HhKaPUx7_qK218rj02TH3Udv-edmGKUJnWO_gU4zBVcAhrjHMMIWImA1LkhfQVQ2JHgvzTbsMz7Dvqsk=', start_index=10841)
Annotation(end_index=10855, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzNgzw4aABYvSgrbBkfNGEd4HicTakJMXHWEW283FhOjpFRdqChdWDzJMe8NvElGTk6ImTGeMX43Z5Vfyc9KKdj7ERK5UgNJHFAijRIsi-Ybbwe9uFfi4gS5DUy5IbDhbOxdhjd6ll81cf', start_index=10841)
Annotation(end_index=11275, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAIW0lNErd2W32iXSE1UtB03bi3G0zMQKIw4Q6hcHr5n1QDWSb_yyYABqMaEa39qlYpV_xJag-B2U0ItMw0mP6dyr81oXN9TleIysEozdazk_K6SgJ1OQbLigFDypINsgfMN7dOcck_fN_7D8pBdN4nnUhbo8=', start_index=11261)
Annotation(end_index=11275, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYocezHSR9epI8zvLW1ursj5zGXt4Ce8479Obvd5wTSZ2HkNL5wBJhnZr40ptzKMX38k4WUwtsZIxB63ceAU7ILtAXhEh00rPXJtJrdkWzPXMZVG7IBH6h82kvAUK7fsw2G3-eFQVEGva0', start_index=11261)
Annotation(end_index=11967, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKmdctkcUdP6_cbzCXVt_RgmnT_S-6ooNBOIoVNl_x9llrONaMplCHK0u1cCM1U-8GrKYIcSK9Ol9lgY4a-mO2fvVuxSDIF4SDrHAPtKVXDdtzE-BBqnngEL5FXxjPSj3dnCfe3tVTVimFbJ7MHRjnz6MLxDU1meorpDD4IWjpMFWLTLI6MTo=', start_index=11949)
Annotation(end_index=11967, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETkM8W3uEgpq2058NUa_59dl3Lr_7J3eTWJgro_rOKLOoLoKj1OC6HJe9cYkTa-LukTS-droou6BahroO4aPtrsCjkqSseO2dBOpPastQiC8CujWB01rtpmEyL9GjK9ltvKBIjv1e6et64xdU16-X30uJVgdJQGzHpCY3t5i3I4AjI88d6VhqqrC0=', start_index=11949)
Annotation(end_index=11967, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmMeLftNvNHOU6j8OzSEi3czcIL2BkSMjR1mqzmptwuDpmDcCHo5cMEFnmm9jBitibhr5VBFOYetU27FICvc91sP6iG2-JqRxMiEZl2fp7m6lLFyOwFwbn18I0-Z3vCnbeYUsCkLj5MaMdOJuLJZU3KE7mSxri34fjhxmJT2V2_T3lW8W1ez38MIign8P9ijkDQ51r5H_bHZ9RS7rzX-PGOc15Y6n5w63EveBLEoU=', start_index=11949)
Annotation(end_index=12414, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_iMa_Nwd2X_h3AOeMnbgbiolL8JUJCqtw-qTiNvx7f5jk3Ei2hntT-Vt6qKj4WjMeTT-KdwmtUtGX1I7Vd6fNP5EGU6osqnVemrAKeOKqGG4s_IreBIS_8B5MMXXDWs1CTjNam0-rubntLHY4sk1Ix-G8FQ==', start_index=12402)
Annotation(end_index=12414, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4_RWeYcJYRBbxU0BvDpV1kO8RBCF2Xxrm-aqYmM6xpwVVivh69wn2eYST_k4VrBTw1sG6iPEtTi1PpVqFQ1OP56yea8horGSX1PUdB9h_yTaqzzTANHGPNhDYcYYjcbQcgir3tWXcdv2IdTDShVys0KMYSAzPG_cKTZ3hF7kU', start_index=12402)
Annotation(end_index=12568, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkfv9HkiP7g0mcLr_4oHkq0tJaU2BCrSyu_EsD5W2IAl25G2urYDYv5ghcJVKMPbXSN7a5-aXc00g6srQ37FgTeA81U8tNnREDYSBgjqJwVU59rEn2JpJE4zeaghtespqiqpnCPDtlmAIBzdAKyDz_S4Cm35WGUeSmxLP2xZW1tj03kRIQp7ClZa-VXvOxeZW5uA==', start_index=12556)
Annotation(end_index=12568, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHn89zrSW2_TSolKa4B3mxnOLhL3RW-sNTGrLUJOnkSMjBKYOMjJzBp5er_6DtFmziPvApTzobOEnSOQ5je2FiTkHiNruPlFuoDJc6daNfoplLGVXro3HnrAPHfsJFKF2XLLzC8vqTeCnYdyxLzmKNunLByTCgmAJzeV2VwfNKwdKZzhsLo4GmdeatIbMi8', start_index=12556)
Annotation(end_index=12731, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFL5123QW_oxH2wqq3vXQ7voHztjLdDvdAH6y7THcJOJzYJbKAmUJsW2F-DQifkK-4CDbK3rmmk62hokbN913L5a6xEiIwrAyJm2ysjsDyHm6RHGEwhApzwbg_j0lMW4VBoi77c_iV4FKc=', start_index=12719)
Annotation(end_index=12731, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqhRGr23jVpzMPL_Jya_sr02L_qbZJBNkpW1MUJGp8kNVqA8nUNnrvu-UnrQs-mKwHu66XcpsbIsebaIv0YGFPJcBmlmWR5CY2BlmZlJPlenz8_c2117gxbCVqRPcuL4L-supGNK1SoShc_844SlzoPoB6Uk7Bvt8H5R_w5tITKDfZ_CXUZ0Cx368c6FAbBexGJzQnDC5bZV5AEk5AXK7W8Nswm8g1gTwzxcvA3wD4-uS2CU_Zf4aDNBkpSEg=', start_index=12719)
Annotation(end_index=12896, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEen1TgxzZaCmPhsxe1DdBb8d85Dr75bi8td2KMte59z6qrQGIL9mSyzarUqGh0pXSJ2UH3DYPzh_K3s-aEglP2z-0ZxXpA2eIKS8b_GGhtF02c_66pzW5voE4rV72gmMhHwFLLsy-2E0-9ftIq9-YHI_9L4xWiOkBudZgodaKsmIF7b-Bxs9QBHBMrkPsTLxDmnHqtrKSejGyTo4bo7_COaGEnPuXK4eb922CsHswQ48injQ==', start_index=12882)
Annotation(end_index=12896, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFDMW6TYAspbAxpxp9gJLMfRjMyo13Gys4lFck2jAMRnGAZ4qK5gJ_SNw3V47YU8fqS9WTQAcfFz4lYurw5n-xd1_9g_HGJI_LbPGwRzlitesw8fO698HlYTfdnJ_Juw==', start_index=12882)
Annotation(end_index=13064, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbcuqWn_yhShqXOnd2IN7yA-F9GEv3uKQ3VLFZ0CRnejG7W5dFOd70tHVDcCvXp5nifPAawHEj_b-FZRi0qbSzglZIQnE8LirJ50POuxqndt932zvdmnlabtFuT-37Ynqx4ljN2hnhemXCj9TLQvxYFOQ6vIJTOz0=', start_index=13050)
Annotation(end_index=13064, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlRc4Q0BT3DWB_wf7mS6D95oI7GT8hRK0Yp8hFRTe8NXirB0-TC0yWsc5_jHRnRxZ6ZIRxb8ZtNQV4p-_z-J4SuvgcTfvPyXnks_d9AX0Q3Dr8KQKAMJQfmkT5Wf_vkeXRlp25o4zrlwTRvDfs799Wmw==', start_index=13050)
Annotation(end_index=13226, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuhbxHaWLb4AKTHa4TScsFV20qiV0cFOU5t5PuBUY_cZ2_AYTnwJAOOsgSquWFsMubC9q_uNIDHKS_20yp7HnEGs_HEBzA9ZlVJFEdosw-O5e3dRplO9nYU1lC_3jitxNL-KRCithp', start_index=13212)
Annotation(end_index=13226, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkVm1IInpx_-TsvgLeSuIMLiguSMwht2frUEWQvArYcmpoMBrWsbtk63cCJRdzwsjBuHVD4cd8UIz68kaq2QG4uMmG_IOAJzGJwukwLhgD9KuCG8G3Ucwj48nQ2sXlPfXKc4EQij9P-8NG', start_index=13212)

## Sources
