# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 7faf4bf6 | **Time:** 445.79s | **Cost:** $1.38603
--------------------------------------------------------------------------------

# Balancing Content Exposure Diversity with Conversion Goals in Recommendation Ranking

### Key Points
*   **The Fundamental Trade-off:** Recommendation systems face an inherent tension between **accuracy** (exploiting known user preferences to maximize immediate conversion) and **diversity** (exploring new content to prevent filter bubbles and ensure long-term retention).
*   **Algorithmic Solutions:** The primary mechanisms for balancing these goals occur during the **re-ranking phase**, utilizing algorithms like **Maximal Marginal Relevance (MMR)** and **Determinantal Point Processes (DPP)**. These methods introduce tunable parameters (e.g., $\lambda$ in MMR) to mathematically weigh relevance against dissimilarity.
*   **Long-term vs. Short-term Value:** While high diversity may reduce immediate Click-Through Rates (CTR), empirical research indicates it significantly reduces user churn and increases Customer Lifetime Value (CLTV) by preventing boredom and satisfying variety-seeking behaviors.
*   **Multi-Stakeholder Fairness:** Diversity is not merely a user-experience metric but a requirement for **provider fairness**. Ensuring exposure for niche or new content creators is essential for maintaining marketplace liquidity and preventing "rich-get-richer" feedback loops.
*   **Reinforcement Learning (RL):** Modern systems are moving away from greedy heuristics toward RL frameworks that optimize for long-term cumulative rewards, dynamically adjusting the diversity-relevance balance based on user context and session history.

---

## 1. Introduction

The architecture of modern recommender systems (RS) is dominated by the objective of maximizing utility, typically defined through immediate conversion metrics such as clicks, purchases, or watch time. However, a myopic focus on accuracy and immediate engagement often leads to the "accuracy-diversity dilemma" [cite: 1]. Systems that optimize purely for relevance tend to generate homogeneous recommendation lists, confining users within "filter bubbles" or "echo chambers" where they are exposed only to content that reinforces their existing preferences [cite: 2].

While high relevance drives short-term conversion, the lack of diversity can degrade the user experience over time, leading to fatigue, boredom, and eventual churn [cite: 3, 4]. Furthermore, in multi-sided marketplaces (e.g., Spotify, Amazon, YouTube), the recommendation ranking function serves as the primary allocation mechanism for attention. A lack of diversity results in **exposure bias**, where popular items receive disproportionate visibility while niche or new items (the "long tail") remain undiscovered, threatening the economic viability of content providers and the overall health of the platform ecosystem [cite: 4, 5].

This report provides an exhaustive analysis of how content exposure diversity is balanced with conversion goals. It examines the theoretical underpinnings of this trade-off, the specific algorithmic techniques used in re-ranking (MMR, DPP), the integration of diversity into Reinforcement Learning (RL) frameworks, and the critical role of diversity in ensuring multi-stakeholder fairness and long-term user retention.

---

## 2. The Theoretical Framework: Accuracy vs. Diversity

The challenge of balancing diversity and conversion is fundamentally a **Multi-Objective Optimization (MOO)** problem. The system must select a subset of items from a larger candidate pool to form a slate (a ranked list) that maximizes a utility function comprising conflicting objectives.

### 2.1 The Exploration-Exploitation Trade-off
In the context of recommendation ranking, "exploitation" refers to recommending items with the highest predicted probability of conversion (relevance). "Exploration" refers to recommending items with high uncertainty or high dissimilarity to past interactions to gather information about user preferences or to satisfy a user's desire for novelty [cite: 1, 6].

*   **Exploitation (Conversion Focus):** Relies on collaborative filtering (CF) or content-based signals to match users with items similar to their history. This maximizes immediate reward but suffers from diminishing returns as the user becomes saturated with similar content [cite: 7].
*   **Exploration (Diversity Focus):** Introduces variety to the slate. This may lower the aggregate predicted relevance score of the slate (potentially hurting short-term conversion) but increases the probability of serendipitous discovery and sustains long-term engagement [cite: 8, 9].

### 2.2 The Pareto Frontier
The relationship between accuracy and diversity is often visualized as a Pareto Frontier. A solution is Pareto optimal if no objective can be improved without degrading another.
*   **Pareto Efficiency:** In ranking, the goal is to find a ranking policy where diversity cannot be increased without a necessary drop in accuracy, and vice versa [cite: 10, 11].
*   **The "Wicked Problem":** Designing multi-objective rankers is described as a "dynamic wicked problem" because there is no single optimal solution; the ideal balance point shifts based on user intent (e.g., focused search vs. casual browsing) and temporal dynamics [cite: 10].

### 2.3 Types of Diversity
To balance diversity with conversion, one must first define the type of diversity being optimized:
1.  **Intra-List Diversity (ILD):** The dissimilarity between items within a single recommendation slate (e.g., a list of 10 movies). This is the most common target for re-ranking algorithms [cite: 6, 12].
2.  **Temporal Diversity:** The dissimilarity of recommendations shown to a user over time (e.g., ensuring today's feed is different from yesterday's) [cite: 13].
3.  **Aggregate (System-Level) Diversity:** The distribution of recommendations across the entire catalog and user base. This is closely tied to provider fairness and catalog coverage [cite: 2, 14].

---

## 3. Algorithmic Strategies for Balancing Diversity and Conversion

The most effective method for injecting diversity into recommendations without requiring a complete overhaul of the core prediction model is **Re-ranking**. In this multi-stage architecture, a candidate generation layer retrieves a broad set of relevant items, and a subsequent ranking layer scores them for relevance. The re-ranking phase then permutes this list to satisfy diversity constraints [cite: 13, 15, 16].

### 3.1 Maximal Marginal Relevance (MMR)
Introduced by Carbonell and Goldstein (1998), MMR is the foundational greedy algorithm for diversity-aware ranking. It explicitly quantifies the trade-off between relevance and novelty [cite: 17, 18].

#### 3.1.1 The MMR Formula
The MMR algorithm selects the next item to add to a slate $S$ from the set of candidate items $R$ by maximizing the following objective:

\[
MMR = \arg\max_{i \in R \setminus S} \left[ \lambda \cdot Sim_1(i, q) - (1 - \lambda) \cdot \max_{j \in S} Sim_2(i, j) \right]
\]

Where:
*   $Sim_1(i, q)$: The relevance score of item $i$ to the user/query $q$ (Conversion goal).
*   $Sim_2(i, j)$: The similarity between candidate item $i$ and an already selected item $j$ (Diversity penalty).
*   $\lambda$ (Lambda): A tunable parameter ($0 \le \lambda \le 1$) that controls the trade-off [cite: 17, 19, 20].

#### 3.1.2 Balancing Mechanism
*   **$\lambda = 1$:** Pure relevance ranking (Standard probability ranking principle). Maximizes conversion but minimizes diversity.
*   **$\lambda = 0$:** Pure diversity ranking. Selects items most dissimilar to those already chosen, ignoring relevance.
*   **$\lambda \approx 0.5 - 0.7$:** A typical "sweet spot" where the system selects highly relevant items but penalizes those that are near-duplicates of items already in the slate [cite: 19].

**Limitations:** MMR is a greedy approach. It makes locally optimal decisions at each step (selecting the next best item) but does not guarantee that the final set $S$ has the optimal global diversity-relevance balance [cite: 21, 22].

### 3.2 Determinantal Point Processes (DPP)
To overcome the greedy limitations of MMR, Determinantal Point Processes (DPP) have emerged as a state-of-the-art probabilistic framework for set selection. DPPs model the probability of selecting a subset of items based on the volume spanned by their feature vectors, naturally capturing both quality (magnitude) and diversity (orthogonality) [cite: 15, 21].

#### 3.2.1 The DPP Kernel Matrix
A DPP is parameterized by a positive semi-definite kernel matrix $L$. The probability of selecting a subset $Y$ is proportional to the determinant of the submatrix $L_Y$:
\[
P(Y) \propto \det(L_Y)
\]
The kernel $L$ is decomposed into quality and similarity:
\[
L_{ij} = q_i \cdot q_j \cdot S_{ij}
\]
*   $q_i$: The quality/relevance score of item $i$ (Conversion probability).
*   $S_{ij}$: The similarity between item $i$ and item $j$ ($S_{ii} = 1$).

#### 3.2.2 Balancing Mechanism
If two items $i$ and $j$ are perfectly similar ($S_{ij} \approx 1$), the determinant of the matrix involving both approaches zero, making it highly unlikely they will both be selected. This forces the system to choose items that are both high quality (high $q$) and dissimilar (low $S_{ij}$) [cite: 21].
*   **Parameter $\alpha$:** Similar to $\lambda$ in MMR, DPP implementations often introduce a hyperparameter $\alpha$ to weigh the contribution of the relevance score against the diversity kernel [cite: 15].
*   **Efficiency:** While finding the exact MAP (Maximum A Posteriori) set in DPP is NP-hard, **Fast Greedy MAP Inference** algorithms allow DPPs to be deployed in real-time industrial systems (e.g., YouTube, Hulu) with complexity reduced to $O(k^2 N)$ or $O(N)$ depending on implementation [cite: 15, 23].

### 3.3 Sliding Window Approaches
For infinite feeds (e.g., TikTok, Instagram Reels), calculating diversity against the entire history of the session is computationally prohibitive and may be undesirable (users' interests drift).
*   **Sliding Window MMR/DPP:** Diversity is calculated only against the last $K$ items in the slate or session. This ensures local diversity (no back-to-back duplicates) while allowing the system to drift into new topics over time [cite: 17, 24].

### 3.4 Personalized Diversification
Not all users value diversity equally. Some users ("specialists") prefer narrow recommendations, while others ("generalists") prefer variety.
*   **Adaptive Weights:** Advanced systems use contextual bandits or user profiling to dynamically adjust the diversity parameter ($\lambda$ or $\alpha$) for each user. For example, a user with high entropy in their consumption history might receive a lower $\lambda$ (more diversity), while a focused user receives a higher $\lambda$ [cite: 15, 25, 26, 27].
*   **User Perception:** Research indicates users perceive diversity non-linearly. They prefer metadata-based diversity (e.g., different genres) over latent feature diversity. Algorithms that align diversity metrics with user-perceivable attributes (e.g., Genre, Artist) tend to balance satisfaction and conversion better than those using abstract embeddings [cite: 28].

---

## 4. Reinforcement Learning: Optimizing for Long-Term Goals

Traditional re-ranking (MMR/DPP) often treats diversity as a constraint on immediate relevance. However, Reinforcement Learning (RL) reframes the problem: diversity is a strategic action taken to maximize **long-term cumulative reward** [cite: 6, 29, 30].

### 4.1 The RL Formulation
In an RL-based recommender:
*   **Agent:** The recommender system.
*   **Environment:** The user.
*   **Action:** The slate of recommended items.
*   **Reward:** A combination of immediate feedback (click/conversion) and long-term signals (retention, return frequency).

### 4.2 Reward Engineering for Diversity
To balance conversion and diversity, the reward function $R$ is often a weighted sum:
\[
R_{total} = w_1 \cdot R_{click} + w_2 \cdot R_{diversity} + w_3 \cdot R_{fairness}
\]
*   **Exploration as Reward:** The agent receives a reward for exploring new parts of the item space, even if the immediate click probability is lower. This incentivizes the agent to learn user preferences in uncertain regions [cite: 31, 32].
*   **Surrogate Metrics:** Since long-term retention is sparse and delayed, RL systems use surrogate rewards—short-term behaviors that correlate with long-term retention (e.g., diversity of consumption, depth of consumption) [cite: 11, 33].

### 4.3 Contextual Bandits
Contextual bandits are a specific class of RL used for adaptive balancing.
*   **Mechanism:** The bandit observes the user context and selects an arm (recommendation strategy). Some arms might be "Exploit" (high relevance), others "Explore" (high diversity).
*   **Learning:** The bandit learns which context requires diversity. For example, if a user repeatedly ignores recommendations from the "Exploit" arm, the bandit learns to switch to "Explore" to recover engagement [cite: 34, 35, 36].

---

## 5. Multi-Stakeholder Fairness and Ecosystem Health

Balancing diversity is not solely about user conversion; it is critical for the supply-side health of the marketplace.

### 5.1 Provider Fairness and Exposure
In two-sided marketplaces, the platform must ensure **provider fairness**—that items from different providers (or groups of providers) receive fair exposure [cite: 2, 14].
*   **The "Rich-Get-Richer" Effect:** Relevance-only ranking creates feedback loops where popular items get more exposure, leading to more interaction data, leading to even higher predicted relevance. This marginalizes niche providers [cite: 12, 37, 38].
*   **Provider Churn:** If niche content creators do not receive sufficient exposure (conversion), they may leave the platform. This reduction in supply diversity eventually harms the user experience (catalog shrinkage) [cite: 5, 39, 40].

### 5.2 Constraints and Regularization
To balance this, systems implement **Fairness-Aware Re-ranking**:
*   **Exposure Constraints:** Algorithms like **Fairness-Aware Re-ranking (FAR)** or **P-MMF (Provider Max-min Fairness)** impose constraints ensuring that the exposure of protected groups (e.g., new providers) meets a minimum threshold relative to non-protected groups [cite: 38, 41].
*   **Optimization:** This is often modeled as a constrained optimization problem: Maximize Relevance subject to Diversity $\ge$ Threshold. Since this is NP-hard, heuristics or convex relaxations (e.g., Birkhoff-von Neumann decomposition) are used [cite: 2, 14].

---

## 6. Metrics and Evaluation

Evaluating the balance between diversity and conversion requires a suite of conflicting metrics.

### 6.1 Accuracy/Conversion Metrics
*   **NDCG (Normalized Discounted Cumulative Gain):** Measures the quality of ranking, heavily weighting highly relevant items at the top.
*   **CTR (Click-Through Rate):** The ratio of clicks to impressions.
*   **CVR (Conversion Rate):** The ratio of transactions to clicks.

### 6.2 Diversity Metrics
*   **ILD (Intra-List Diversity):** The average pairwise distance (e.g., Cosine distance, Hamming distance) between all items in a slate [cite: 8, 26].
    \[
    ILD = \frac{1}{|S|(|S|-1)} \sum_{i \in S} \sum_{j \in S, j \neq i} dist(i, j)
    \]
*   **Entropy:** Measures the distribution of items across categories (e.g., genres). Higher entropy indicates a more uniform distribution [cite: 8, 27].
*   **Catalog Coverage:** The percentage of unique items in the catalog recommended to users over a specific period. High coverage indicates the system is effectively utilizing the "long tail" [cite: 2, 8].

### 6.3 Trade-off Metrics
*   **$\alpha$-NDCG:** A variant of NDCG that penalizes redundancy. If a user has already seen/consumed a subtopic, subsequent items from that subtopic contribute less to the score [cite: 42, 43].
*   **Pareto Frontier Analysis:** Plotting Accuracy vs. Diversity for different parameter values ($\lambda$) to identify the optimal operating curve [cite: 10, 21].

---

## 7. Empirical Impact on Business Goals

Research and industry case studies demonstrate that while diversity may incur a short-term cost, it drives long-term value.

### 7.1 The "Diversity Dip" and Recovery
Implementing diversity re-ranking (e.g., increasing $\lambda$ for diversity) often causes an initial dip in aggregate CTR because users are presented with less immediately familiar options. However, studies show that over time (e.g., 4-6 weeks), engagement stabilizes or increases as users discover new interests [cite: 8].

### 7.2 Churn Reduction
A study on a large digital content distributor found that as the number of product categories recommended increased (higher diversity), the likelihood of customer churn "strikingly decreased," even after controlling for the number of products. Recommending diverse products was estimated to save the company ~7.5% of annual revenue by preventing churn [cite: 3, 9].

### 7.3 Headspace Health Case Study
A real-world implementation of diversity re-ranking at Headspace Health showed:
*   **Rarity Improvement:** +562% to +765% (massive increase in long-tail exposure).
*   **Entropy Improvement:** +19% to +22%.
*   **Content Starts:** +2.26% (proving that diversity did not hurt, but actually helped, engagement) [cite: 8].

---

## 8. Conclusion

Balancing content exposure diversity with conversion goals is a sophisticated optimization challenge that has evolved from simple heuristic re-ranking to complex, multi-objective reinforcement learning.

1.  **Re-ranking is the Control Point:** Algorithms like **MMR** and **DPP** provide the most direct control over this balance, allowing operators to tune the "diversity penalty" applied to similar items.
2.  **Diversity is a Long-Term Investment:** While relevance drives the next click, diversity drives the next visit. By sacrificing marginal relevance in the short term, platforms cultivate broader user interests and prevent the stagnation that leads to churn.
3.  **Fairness is a Structural Necessity:** Beyond user preference, diversity is the mechanism by which platforms ensure provider viability. Without algorithmic intervention to boost exposure diversity, marketplaces risk collapsing into "superstar" economies that alienate the majority of content creators.

Future systems will likely rely increasingly on **Personalized DPPs** and **RL-based policies** that do not use a static diversity parameter, but rather learn the optimal diversity tolerance for each user in real-time, maximizing the area under the curve for both user satisfaction and ecosystem health.

### References
[cite: 2] Multi-objective optimization and filter bubbles.
[cite: 10, 11] Pareto efficiency and wicked problems in ranking.
[cite: 1, 6] Accuracy-diversity trade-off and exploration-exploitation.
[cite: 17, 19] Maximal Marginal Relevance (MMR) mechanics.
[cite: 15] Determinantal Point Processes (DPP) and Fast Greedy MAP.
[cite: 4, 5] Ecosystem health and provider fairness.
[cite: 8] Real-world impact of diversity on metrics (Headspace case study).
[cite: 21] Geometric intuition of DPPs vs. MMR.
[cite: 29, 31] Reinforcement learning for long-term engagement.
[cite: 14, 41] Provider fairness constraints and optimization.
[cite: 26, 27] Adaptive/Personalized diversity based on user entropy.
[cite: 3, 9] Impact of diversity on churn and retention.
[cite: 18, 20] Foundational MMR papers.

**Sources:**
1. [milvus.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZLNXuCDK2LI669s_sFrAcl-PJLtvLDffTztZfU-1Tg_36GpmoP5bUgAB9P8mK11DC-WX8F1mNyPNpeYGHCJLq0yiQmMpYgQybyX3lX38gVJOU5WCdJ9FGCdOqG36DKHlGz5PYdfVEtR6EA-iHGW6Wi-8kYd4U0BVDeT2qOMmIN6CtBeIsvJaC34pmP23vCPlIeIe3-3-JW3jxXOfR7WO4xOTgf1YiAg==)
2. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEm3TpdxG6jpkUno6zl8tTEoF851F6mLbEAOrFudAPzlL8HXkzK6kKsgd4wiLkK0AgnnmwSpHQ5eClwlunNU-UwXoUZYxyJsIwPNVXXLJ5UsM4L8Bo5KQwOnw==)
3. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGiiMlAscLpJ0dxDLM-O86PFkOAKS0Sn0iwDfEYiYWjN4J7g4M_RF4fLGePDYT_KQhhGB4dmt5S-LSeV-N1xC0W78i0KqzNKin4aEEcErtEmC-Ip7I_29lr1slzID5VyBN7Knq4iK-z6jINuZuKLZ7VJlBcNgRk1UVtmWQX0JbJThQlVRwBEhOhrhu4ILGI4wnffq9__if2ShUGHGBdqCW9kisdjnF5RtmSE10lD8JvXrp5o8G5H1KOfH-BrZ-sCAMglhXb_bOwL1_mATOsYBo=)
4. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGz9IYmnJDbTCmqSwiEWv3oK1N-v-wk6IJ887fqQUyaPPZWQ556IVAj5_QSn8iE6bF1YdskZvk6xGPWp9R76o6HaZ8PNwOJ-u7ufJEPbnCuBm2HLfhKuQ==)
5. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjZlBJLqDb3Ih7YdIttmGYGLs2y5jsk2k6pZu9LP7yJGWDAghaf74j9lFvJlAtpW8k4pqF877W3qchmZmrVvqtH45qE-m6vrKOIA8Q-iV-7Djb7Fsk6gJP_rlXDiRRTNTPhKH72KmhY3YHE5hjVRAJnAlWFYdzgEjxcfxpgP_6Gg7DCBYxvKSqBhhXtXoQA_q1kjpFx4wxp3U9DLEiR8x60DT04q73FuxVptv6tKO-ieMTBpIudsu7ms-3)
6. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHGkqOodawyqx4K0L88O-GEroMY0TmSavUccTvQmFvv7aphUV29tRd8BZjHnnNpigPjiDXBxLOcSHf2YmiT3KVaaWaSJ8Oc_y6jmVzlHpztgxiXOfMPxqEYDgxBngh2wOCfIGW2bAeuYCCG7eF-EOcIHPrB9i5NpsVwSvUAwrYJHJoShy0G7MdMZUy23oP3mqhGa-mDVX1-mIkjp8zNv0hkckYhNy-vjC8FSbNmw==)
7. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvEmHNGwnIy1rrdPg8KPViDSVgOq8qbNyMZ6kVRjGTHPvQg0nAcF3_hjt7KMUuoSKtw954r1W7-8C3bk2eIn_8YbFny6IewT1ojkPYNgM22mUeSfSuKg-DAk4csW_hmWaxc2k-PQc=)
8. [towardsdatascience.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEGt26x2FKxDEoeUz3tyQe9xw_8NhiiwbbjYK-mpIXRa8HdN6UGYJoU14IzKZ5GpsaMGRKgbWiHjY6mujh3Hiv6VyaMCSnzG1vbhexXX6d7GCIyZwbcHR1YfXtEZmLtp5iW9ocQdhnJmbkAbxJZGkcKa4QETydcQ-IjYZafGADtDqwlVZzj0T6RN0y0QOr4HL2_Gf0aPOjoTyrs27WLdXYqlNpfLV-M1pTDA==)
9. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgz0zjIGTFw_XVT44jWsHm1GVftptj0WruefcH6-c94OOuxESvqhdYQKJbOeoXqfAXBrRWMGg2jXSd0_AC-9hZ9UocNy8wTExwAs9WKGWc1jEK58ydpBxi9KEPLuXT7yjm7Cjyg-FviRkQ0Lw3pCa01Foc5WRq9kpaVS8ln4TFcol8tqJDs89aAW3MFSGCNaUInnJnvnAH64_SYDLJj6yPT2dKLE9tbfGDqoMzdqPflJIv31-xX94qlTBNwMIrIaHayVqncyyUoqKhXml32e72dk6NMlg=)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnSVGSgX0xHKExNLwxhzsSEezeQTU1x_XdaRZ9VDlZkekC_fKbLzWJZaRoS_ycmmiaA4rFgI8Y7tv0efZ-avTQgaSiKUti15UGZI6Cs5wmhIcxHTaX3_xXw0XK6khhqDwRKwBUJymft4pNFxaOXvziZzFuimT47ZQOBTY_Qi_-nBwQyzq5kcKHJmvAh0CKc52X2evY9R9njlrtKzJkuCs=)
11. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1WogzdY99yfr967y0EmkLG12QdP8GsSvG_29guJuFQ_VbnFKGj43wSCH-juzAoy7GbothTTVHyoSk1V4l0ja4zZb15wPTJw82IOvrMvJ-2sJpHLM1ig4tipLxhq62zTiEV6jldIqPkJitBg8Cu5zfIbmDmn3EmSaluc23lg8AIFVd4X_6AqriDq2IgQ==)
12. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHv2N9sQY5QnHqBxNMZIVZA1KtnOpMeQQ-sDP6dSO2lv44T38AJY0wAHONz6D1bwjrocVM-zTznDU9pqwVqBKNj2sX9afyQaqQKQUWzu9PWepWn7ESAXs02mOzDl13Kdh73CiI3LUM74g0ba_pm7KlYiCwG7itDU9iXwJbHitbpF2ZKFQNDFD0xP2jZK54Ew84pRoCjg3Rz1YYkYpJlCIgmU3kvI3nDIlC3Le9Feu9e_6FXEeBSgdiPYX-adr3JLyWhHBAzEw==)
13. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-0vGbfE1GkFCR2q5sIsrw5S3f9zq7WYtdL5JmEOzfrqlz6RQuE1UvEVbZqLm0Q6dP8A5eCDLDubmmKkGVMtWuTNi10r2rlvXK5SchS-FWZ5p1J9nNplkLBz_oinGYn9ofh1Hggw5L8Kya4WqwSnTq3hFNXpq4nrM3hTGAzOC0ZczW)
14. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnsljJm7xcVnB9rXcNqxLfFGRFxcqMhUSLWp3i-8ZUZ54ghbHgu8WzUTbThjDANJF1nn4qZqCEQrlR4-Ew5ga7f85OoopVmO9FG78ktYMoWaCs8jjA8hv_5vJU2FA8Og==)
15. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHozhB0ifX1tpvDzfcaK9u78KupiiF2Vj5C6_tBIUaclhHuo2yWS-m4w4fCUXvF264x7p9OVb6YpldbD2323FUgMGrNn59z6IwOsnSKKww2b26hdXitVsYntZ9rAcjmIsraWMffqp_VCSdA_hi7CE-Mtv0=)
16. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6bBM-VmV7v955YVQLl2WQ8O3imm-n-m9qyw-46v9W5LaiBPX8FdkJd0ZURJP6tktMlSmVaoCJGMw-iGkRTwW0d8x_9eqRL3EKa7mQ--_396VccOAVTG10ZqcgnNC31KdIkZYTVB-VBgEbV_eORboaU3GTSLfThyWRBOQ9NRig9R15mANSTGZoai0lZtndjMi3NSjW919rhvIdepmvQ_Mkcd2SFa1CrQ0D_a1ZLWA=)
17. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKR4Ug7Rl0vKLEC6dbPHi5LVxs2zmsvLWLLYkQsJ6kVeAoT3FL4pKuh6B0e9VALK29Huj-MP0dXgjqNvL35GTmJA13iJ7c0BaCktldGwS7UZ92cF_A4QSVmDVVkwbpzs0nwLWM5dc3tdC8I18vYE-fSlBr4zPHxGgfJ3XAJeFAJnvCR_ZwGM4amE6IzQtvcp7CzugtlG595JgHgYwQvRxbbTundSg2V3Iz74JU4g6c)
18. [aclanthology.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcipvERZPFgi7mBixkiZYO2n7KJ7My4tvQ4ezXvQziSdLwWYM4yYVyH18MKz4HONy0_8Y_p6f2FiwqC8QJqMs57Pve3nij2zMc23EG_JDwHi0WfP7TGGrVVMP8)
19. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHD_vKZoUowDf038c0B3fYFTa5JL4o31QV6Kr4GjqXcsXqDKxc3E4BwyLLblFqMDsRYsUuiIkXiy8L4vmPcesUEI6fM6WMR5g1HbucyA1rQOQXF8I-ICmIgBwo8xTMWXDOcOlB8WmYO_k0tYGwNWsZg6pIpaueQYEqjp6RazXXvcvCWqH0kyr2FqF5PRMuTXs3ekdDx-iQww84xm0IlTyPl3La-6fo4fM26)
20. [cmu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGCxI-O-8bMQKa6jXQFuwoUFDOgNk1XLijEXuWGWf2BMY3tgLUhX8Q6MU1f1bVb52tghxHua-5p_GrfIg3KsggGZ-4fggoYp-7v2Mk5jqG0gdm8F2kCh-qSqqF55Oct2T1kpE9rtKiZ5Gen8QFdmvUCpAdyNrJxKVaLGO6C03oo6ssoPD724D7)
21. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkMHMf5iCpZ6W9uUM3Jr417EVqFdqY-N0zSryZEzqtR9gNBEGuVfxdRCxe-sAWzVO7qpQU-Fxa9uy3d8cKFy-wlp4H5DdWGx3uagdSebPiYwMjYS1M29dPxBNif2QfKAQCL7J28mVLinOqa0c_-U2LRr64nLa4IwrgHbsKuooHmioXEpQ4Jrst1Z-sbDqBK-7PnlhirdBDtcR1sJfUw1D3FNL4-yMua99rcCP9)
22. [jgillenw.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdxR7pMH7wCZaXpnfQ_Pkx4duFdxRk4YatNKp0UY-6KFUaDRzt6xpxdf2eyJZ_a-_B9JO-sF680j0KXTp1OtpLkV5zYeZUZyUNIgTUwVWjf9Q-VXBXtAI=)
23. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCF25ubYBqCCH0VK6JJVhK47iOrcvp1liimwRXlXFDTWhe6WyOMH5kwrlKqmDPSyuNipTC_wDExmLdC36lUnIYVayohz1-Ri9N9FsLzPxo4twwCxL4-lXHYd_qmrgYtl-3YOGjRmKe4gd5PoTV0E-EPNs4bA==)
24. [substack.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTHaW_lyl0lvb7tgSR72Wb05ztq5m9nFOYQkwgeYTG74A2_cDibP-eWULyxOzTEsmF7OJSwF9ccVp3a5Mz5vauiJHNJuc-oOsrAWCk9fU8par7RC_SKPAWV1OpdLycETaPP81jVh2zEgAk0zJOXscSG5sHoTQrtdFC)
25. [ruizhang.info](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuDOeZYZfsJ8mGRrF-hAPgPQZEBmFU95DNycSMdbg2ZJxE3HtzFHWMgmGdGrNXYpm5f8vLrdO6lfoINNGzBStFOKcTiqF5Er1Xe2Vjf3rZJ94ZX2vvwcIRkZJVsGWaYYzvDmbe3vEGSxFhdU1vqdkbFsJnEizjEjNMU3pWJUqN16lZbulLZjPPaY2ReQ9FD2DbBuCblF2Uifg-9M1O_2y9DZ9M6aTMj0lNOh2atcIR5L2a1-NaK21gvSw11fCTt40=)
26. [poliba.it](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGO76NVeW67ukxHYM0I2MNd7GSucFud9VwWtzlmB-bKej1lE3tBOeNcJmIdX752t0WV9jEejqVq8rGNrpGI_kLZqmoQbuTbGeGqwKJe9ZgCAjSVPuzaSbHrfcgVq-nL5mD2hZ4hbTOQiXc6mvtC3m65E9ZfyMTaBc4Nw0uXd0cEQhLq3Z_52kRp7tijpFAGQdYo1G1rj7wdpt3N8ck1yrQkoJwaHTXx3f1_cTAr2hg34oiubQ==)
27. [cnr.it](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErmJs2lMMiB43m5jpIoCSyisGalMRcl5P_Hc7QO0qqTKgBfldw2nwF-y002Fonxodoq35ncs_ki1SJ4ZhUwAzRaAor69Vk-8YiOO5g1JJRtnbMQ4psSzxre19yYp9RC3u7dTQeVbtCzBQYJ4fxe5HcdAHODKWjgA==)
28. [ludovicoboratto.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyaF0YpR8By1BRj0UN7h09vTs-bau4TKcwWGjweqyHrlX11aj9TFjKDlbW7dAsgAbzsZD2fGoJsh0T9aRm8n22pZ1M35mH3bFcmwWPSPmrmKvqzGYEdRDVGT0bHHsVPSFLu1xv6t34o7eRRJaWny7Sc9wNQFTKZ8ElV7Yjlec2KNyrD7I_pvmDVWtc)
29. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFG-RD77TgEdMz4qg-JP0SWSvXYmHgNpegd21NRoY0pIy-tKvkR3JLsPGbE6TJeGlom0t-Ub0njXq2GSe0DGrVDe78Yy1oQySn5jA7Q4qNfph6NoB3CTB1dr7soXSwYjLlAWyWnUF6yUB5EZXxNtAtDwL9xBSlFrR1xspCt85lJTBXYsnZI3tuaVK-LT-Et9fLzCUXmVC8FwrJGECtSty8kxEsoT3gJUElX8XWSrhfUXBSUUB7UusN_Lyp66g==)
30. [applyingml.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXutS4lTy5WUeocsX_0LyUm8zVwkQSmi06c972KchgUEJhI2XL3w_8Py4tR6oPJN6h-aPSxTiEXgdlV5Kug43FD_Nalw_trkMcQ_bfbNrzt5AJFKKWLgciAZ63o9K3BIVPFbpJQw==)
31. [aaai.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFT2RLUdysOANh_eRPhEG4KhDlMljjpKz2RsW4_RA3PFrdRW24WQ-25XcGOd3DfILm1txOUnSPvztNsBBuQlmvs-zYWPmVkI_inf4smh0YJNBAwPxUHsKujF0FtpVe5FkqdWG88aikJOhAvjCZMixSJ9pfZtg==)
32. [geeksforgeeks.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAGwnnOsX5zZQkd4FKMA5v7a11ivCdIr3fscu4mFWwKYnpxVdkvx0jNrZux_SAjAesZbE2b0DNRGD1KGjgFCWRf7X37yPKxYIfMnCCbqGGpgaNuCiDCE5d6lbIuwMFDL-4IcHZR4R4uIUPZ0FFZFDAoM6jDarw0gTCxNFazWoMZNTcS-LzhdKSRdWNNM2-Shii5JHHWYNJjttKo_bz)
33. [research.google](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGTAKU-gjd41pfvid6cjk8ezY_ezTzJIzRtASUxCYJ8-JeXcev3vLZMJTBJ6F4apgQOTEHDAjjOoc8A-A0p57CB4H4iTz2-0L5R-SsIoth4cihhimJeTab3QRGGiOprNltgp7yX_sWkynTMcQLgymYWu0livpRzz7ZReSLGhHoeqD2fgVdqURfSwymJweYLCIw0g==)
34. [aaai.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGki0LRoRUyS8YQTQ0rhr3aCrOJ3xuHZcx3OetUGGAWHuiABySNPJt5ljyDrWyVhrz8rSo08LkAgf6wEERVVjIaLU7KD9JCmz4wu9x0UXv4m6f3w6fnPtQvgpnYLjuek8B1lxNiICIW-kfrtVVqjAYkpMQ=)
35. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFpGvUMWa_mJQGYnDPaBqh4gltG4K0V7mZrYQCMfpQxzlE3S-f_6I37H3bZRi8B_YbAC8JFy8_r5wE2rILbpwBA8UHm67T6NkQjvWhRE78h3Mbzu-BRmX3fLan3OtOeG7iw5f6KGgvxCFS4Wso45eHaZyObZnAEE86cuicvqq-mC_VcC3BLiDcRA9I95B-hzu-4dEDdcdIwtmcbqhbcEzbDPrh)
36. [substack.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFEjrHqxmNzAtw89-NjVUCJ3bhVYZj4YWz3QgAUDUkxUPEY-1nleFVx5mOLy16LIaJUQJn2TMxvNHRVZjI6ZNFl-qsrGtWgyimUmTpjTQ4DTjVmSmBfK96_0rqlmHgzTzFf3dzS4SjWQ02843bb_AY064B__yYJ9w=)
37. [lawfaremedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGa1k6dwxbms_ctSvHkIWIh7_F3Imaolrt1QeI1KIFZAliVQEvI36_hRNiqWQmloshVy-nC3ElY10PgfXxONRP3ROdoiupL_l5Ry0W9qe54CAHbmwwgBZF72wKf2WAQumK4KbK7O1JB87SDOAWFqFBK8tUvsusiFtvbxXKcQi5r1jyV0nVgcFeqHtloBhRNVlzTXB_Nnmyx)
38. [recombee.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkxgHjMD48uEU-voEaN0hXJbSenVjXA-Qds-tQFTMH2hk_27oR02e6XTy0tL41Wu8BxRXXRocI5FT2jc0jRqOLm8aKaJxElHQrUtxt6NVw5qzF1xKJux2TrOXIIwZN6ZlkMhCeU9nMdVt7YSaXulFMoNb5JQF5-tXHfG2Vo__VguNP5tmSkOS_hnVZ7I3EdYHvoo-a1Jc-Nrc=)
39. [hbs.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyNd0rl2rYIrgcKud1mU-9xRR7czFnRW0HCNexVEMNzcXmKS6EdFBUFG8YF1RYPbTujm4WoxxNxw8yYxbVpp8VOC3Blk2MTvOGiheDjhyeU-KUi71o6QapGgNVTNfMKELpI0nXbe25YxyEkKJNn7dznnI1QHNbQp8bZt948UVYtL11gowpgA==)
40. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPXg5B3qGKNG9NQNOjnYOx0BpURJSLNi6H9CUE6GHvxbhXEWraCnu0c9tS9MXNq-bvoHp1TGhNqcuDZEidkEjoN2O5sS7LyZTnL1SMf-F_4yog5oouWdbdiZmAETvlTLx8pghXJh1TVEaaz48pqTtZztahlaU=)
41. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4dfuU9mSLZKB-7X4nU8sqwWf3T9Epvko9nKMgTF3W8w0aL-UDsl3xlAraE3uHeXn5G8S5VXJG4Tec3OoR6nvU7ufVcAY-kd8Eo6dkELiwT-_4hhFT9lOypw==)
42. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4LwqY9bthHldbYW4RalgIEXO8Vpp2rrf9wGNnhjF11I-UXdrLkKsSNv01EJx8FjOiXUIvC8x_6HM61eF77UfEz1h8NTRyjka49PJalPRc2y5VZwM50GXTmQ==)
43. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHW4zTMqx6YB5RhV066BG-PBd4Tmz2IEBRIFMY0GH7j6M5XB2GJsGCGMEitkvl0SufdhiS2-CaAph_gnT5kANHr6VPOmS_qlxHeR88q6pOsJUS3bpPozFqkwFqUsbGEhRp38u0c_JwrSOi_7WLo305u_0wvfO_baoB9ChgjlS87lUzKebFUBxX_x8t0eBMwl81o0FnRsRtObG0AH5V4RSMTxenTUB0sVWs3EsYkEA_27R8MJjRjsrK0FlztPJ0UDiSKivunAo11Csdv38fP5CMfVGh_Mw==)


## Annotations
Annotation(end_index=1896, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZLNXuCDK2LI669s_sFrAcl-PJLtvLDffTztZfU-1Tg_36GpmoP5bUgAB9P8mK11DC-WX8F1mNyPNpeYGHCJLq0yiQmMpYgQybyX3lX38gVJOU5WCdJ9FGCdOqG36DKHlGz5PYdfVEtR6EA-iHGW6Wi-8kYd4U0BVDeT2qOMmIN6CtBeIsvJaC34pmP23vCPlIeIe3-3-JW3jxXOfR7WO4xOTgf1YiAg==', start_index=1887)
Annotation(end_index=2142, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEm3TpdxG6jpkUno6zl8tTEoF851F6mLbEAOrFudAPzlL8HXkzK6kKsgd4wiLkK0AgnnmwSpHQ5eClwlunNU-UwXoUZYxyJsIwPNVXXLJ5UsM4L8Bo5KQwOnw==', start_index=2133)
Annotation(end_index=2321, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGiiMlAscLpJ0dxDLM-O86PFkOAKS0Sn0iwDfEYiYWjN4J7g4M_RF4fLGePDYT_KQhhGB4dmt5S-LSeV-N1xC0W78i0KqzNKin4aEEcErtEmC-Ip7I_29lr1slzID5VyBN7Knq4iK-z6jINuZuKLZ7VJlBcNgRk1UVtmWQX0JbJThQlVRwBEhOhrhu4ILGI4wnffq9__if2ShUGHGBdqCW9kisdjnF5RtmSE10lD8JvXrp5o8G5H1KOfH-BrZ-sCAMglhXb_bOwL1_mATOsYBo=', start_index=2309)
Annotation(end_index=2321, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGz9IYmnJDbTCmqSwiEWv3oK1N-v-wk6IJ887fqQUyaPPZWQ556IVAj5_QSn8iE6bF1YdskZvk6xGPWp9R76o6HaZ8PNwOJ-u7ufJEPbnCuBm2HLfhKuQ==', start_index=2309)
Annotation(end_index=2779, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjZlBJLqDb3Ih7YdIttmGYGLs2y5jsk2k6pZu9LP7yJGWDAghaf74j9lFvJlAtpW8k4pqF877W3qchmZmrVvqtH45qE-m6vrKOIA8Q-iV-7Djb7Fsk6gJP_rlXDiRRTNTPhKH72KmhY3YHE5hjVRAJnAlWFYdzgEjxcfxpgP_6Gg7DCBYxvKSqBhhXtXoQA_q1kjpFx4wxp3U9DLEiR8x60DT04q73FuxVptv6tKO-ieMTBpIudsu7ms-3', start_index=2767)
Annotation(end_index=2779, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGz9IYmnJDbTCmqSwiEWv3oK1N-v-wk6IJ887fqQUyaPPZWQ556IVAj5_QSn8iE6bF1YdskZvk6xGPWp9R76o6HaZ8PNwOJ-u7ufJEPbnCuBm2HLfhKuQ==', start_index=2767)
Annotation(end_index=3961, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZLNXuCDK2LI669s_sFrAcl-PJLtvLDffTztZfU-1Tg_36GpmoP5bUgAB9P8mK11DC-WX8F1mNyPNpeYGHCJLq0yiQmMpYgQybyX3lX38gVJOU5WCdJ9FGCdOqG36DKHlGz5PYdfVEtR6EA-iHGW6Wi-8kYd4U0BVDeT2qOMmIN6CtBeIsvJaC34pmP23vCPlIeIe3-3-JW3jxXOfR7WO4xOTgf1YiAg==', start_index=3949)
Annotation(end_index=3961, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHGkqOodawyqx4K0L88O-GEroMY0TmSavUccTvQmFvv7aphUV29tRd8BZjHnnNpigPjiDXBxLOcSHf2YmiT3KVaaWaSJ8Oc_y6jmVzlHpztgxiXOfMPxqEYDgxBngh2wOCfIGW2bAeuYCCG7eF-EOcIHPrB9i5NpsVwSvUAwrYJHJoShy0G7MdMZUy23oP3mqhGa-mDVX1-mIkjp8zNv0hkckYhNy-vjC8FSbNmw==', start_index=3949)
Annotation(end_index=4250, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvEmHNGwnIy1rrdPg8KPViDSVgOq8qbNyMZ6kVRjGTHPvQg0nAcF3_hjt7KMUuoSKtw954r1W7-8C3bk2eIn_8YbFny6IewT1ojkPYNgM22mUeSfSuKg-DAk4csW_hmWaxc2k-PQc=', start_index=4241)
Annotation(end_index=4539, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEGt26x2FKxDEoeUz3tyQe9xw_8NhiiwbbjYK-mpIXRa8HdN6UGYJoU14IzKZ5GpsaMGRKgbWiHjY6mujh3Hiv6VyaMCSnzG1vbhexXX6d7GCIyZwbcHR1YfXtEZmLtp5iW9ocQdhnJmbkAbxJZGkcKa4QETydcQ-IjYZafGADtDqwlVZzj0T6RN0y0QOr4HL2_Gf0aPOjoTyrs27WLdXYqlNpfLV-M1pTDA==', start_index=4527)
Annotation(end_index=4539, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgz0zjIGTFw_XVT44jWsHm1GVftptj0WruefcH6-c94OOuxESvqhdYQKJbOeoXqfAXBrRWMGg2jXSd0_AC-9hZ9UocNy8wTExwAs9WKGWc1jEK58ydpBxi9KEPLuXT7yjm7Cjyg-FviRkQ0Lw3pCa01Foc5WRq9kpaVS8ln4TFcol8tqJDs89aAW3MFSGCNaUInnJnvnAH64_SYDLJj6yPT2dKLE9tbfGDqoMzdqPflJIv31-xX94qlTBNwMIrIaHayVqncyyUoqKhXml32e72dk6NMlg=', start_index=4527)
Annotation(end_index=4927, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnSVGSgX0xHKExNLwxhzsSEezeQTU1x_XdaRZ9VDlZkekC_fKbLzWJZaRoS_ycmmiaA4rFgI8Y7tv0efZ-avTQgaSiKUti15UGZI6Cs5wmhIcxHTaX3_xXw0XK6khhqDwRKwBUJymft4pNFxaOXvziZzFuimT47ZQOBTY_Qi_-nBwQyzq5kcKHJmvAh0CKc52X2evY9R9njlrtKzJkuCs=', start_index=4913)
Annotation(end_index=4927, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1WogzdY99yfr967y0EmkLG12QdP8GsSvG_29guJuFQ_VbnFKGj43wSCH-juzAoy7GbothTTVHyoSk1V4l0ja4zZb15wPTJw82IOvrMvJ-2sJpHLM1ig4tipLxhq62zTiEV6jldIqPkJitBg8Cu5zfIbmDmn3EmSaluc23lg8AIFVd4X_6AqriDq2IgQ==', start_index=4913)
Annotation(end_index=5208, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnSVGSgX0xHKExNLwxhzsSEezeQTU1x_XdaRZ9VDlZkekC_fKbLzWJZaRoS_ycmmiaA4rFgI8Y7tv0efZ-avTQgaSiKUti15UGZI6Cs5wmhIcxHTaX3_xXw0XK6khhqDwRKwBUJymft4pNFxaOXvziZzFuimT47ZQOBTY_Qi_-nBwQyzq5kcKHJmvAh0CKc52X2evY9R9njlrtKzJkuCs=', start_index=5198)
Annotation(end_index=5541, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHGkqOodawyqx4K0L88O-GEroMY0TmSavUccTvQmFvv7aphUV29tRd8BZjHnnNpigPjiDXBxLOcSHf2YmiT3KVaaWaSJ8Oc_y6jmVzlHpztgxiXOfMPxqEYDgxBngh2wOCfIGW2bAeuYCCG7eF-EOcIHPrB9i5NpsVwSvUAwrYJHJoShy0G7MdMZUy23oP3mqhGa-mDVX1-mIkjp8zNv0hkckYhNy-vjC8FSbNmw==', start_index=5528)
Annotation(end_index=5541, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHv2N9sQY5QnHqBxNMZIVZA1KtnOpMeQQ-sDP6dSO2lv44T38AJY0wAHONz6D1bwjrocVM-zTznDU9pqwVqBKNj2sX9afyQaqQKQUWzu9PWepWn7ESAXs02mOzDl13Kdh73CiI3LUM74g0ba_pm7KlYiCwG7itDU9iXwJbHitbpF2ZKFQNDFD0xP2jZK54Ew84pRoCjg3Rz1YYkYpJlCIgmU3kvI3nDIlC3Le9Feu9e_6FXEeBSgdiPYX-adr3JLyWhHBAzEw==', start_index=5528)
Annotation(end_index=5704, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-0vGbfE1GkFCR2q5sIsrw5S3f9zq7WYtdL5JmEOzfrqlz6RQuE1UvEVbZqLm0Q6dP8A5eCDLDubmmKkGVMtWuTNi10r2rlvXK5SchS-FWZ5p1J9nNplkLBz_oinGYn9ofh1Hggw5L8Kya4WqwSnTq3hFNXpq4nrM3hTGAzOC0ZczW', start_index=5694)
Annotation(end_index=5903, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEm3TpdxG6jpkUno6zl8tTEoF851F6mLbEAOrFudAPzlL8HXkzK6kKsgd4wiLkK0AgnnmwSpHQ5eClwlunNU-UwXoUZYxyJsIwPNVXXLJ5UsM4L8Bo5KQwOnw==', start_index=5890)
Annotation(end_index=5903, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnsljJm7xcVnB9rXcNqxLfFGRFxcqMhUSLWp3i-8ZUZ54ghbHgu8WzUTbThjDANJF1nn4qZqCEQrlR4-Ew5ga7f85OoopVmO9FG78ktYMoWaCs8jjA8hv_5vJU2FA8Og==', start_index=5890)
Annotation(end_index=6395, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6bBM-VmV7v955YVQLl2WQ8O3imm-n-m9qyw-46v9W5LaiBPX8FdkJd0ZURJP6tktMlSmVaoCJGMw-iGkRTwW0d8x_9eqRL3EKa7mQ--_396VccOAVTG10ZqcgnNC31KdIkZYTVB-VBgEbV_eORboaU3GTSLfThyWRBOQ9NRig9R15mANSTGZoai0lZtndjMi3NSjW919rhvIdepmvQ_Mkcd2SFa1CrQ0D_a1ZLWA=', start_index=6377)
Annotation(end_index=6395, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-0vGbfE1GkFCR2q5sIsrw5S3f9zq7WYtdL5JmEOzfrqlz6RQuE1UvEVbZqLm0Q6dP8A5eCDLDubmmKkGVMtWuTNi10r2rlvXK5SchS-FWZ5p1J9nNplkLBz_oinGYn9ofh1Hggw5L8Kya4WqwSnTq3hFNXpq4nrM3hTGAzOC0ZczW', start_index=6377)
Annotation(end_index=6395, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHozhB0ifX1tpvDzfcaK9u78KupiiF2Vj5C6_tBIUaclhHuo2yWS-m4w4fCUXvF264x7p9OVb6YpldbD2323FUgMGrNn59z6IwOsnSKKww2b26hdXitVsYntZ9rAcjmIsraWMffqp_VCSdA_hi7CE-Mtv0=', start_index=6377)
Annotation(end_index=6638, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKR4Ug7Rl0vKLEC6dbPHi5LVxs2zmsvLWLLYkQsJ6kVeAoT3FL4pKuh6B0e9VALK29Huj-MP0dXgjqNvL35GTmJA13iJ7c0BaCktldGwS7UZ92cF_A4QSVmDVVkwbpzs0nwLWM5dc3tdC8I18vYE-fSlBr4zPHxGgfJ3XAJeFAJnvCR_ZwGM4amE6IzQtvcp7CzugtlG595JgHgYwQvRxbbTundSg2V3Iz74JU4g6c', start_index=6624)
Annotation(end_index=6638, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcipvERZPFgi7mBixkiZYO2n7KJ7My4tvQ4ezXvQziSdLwWYM4yYVyH18MKz4HONy0_8Y_p6f2FiwqC8QJqMs57Pve3nij2zMc23EG_JDwHi0WfP7TGGrVVMP8', start_index=6624)
Annotation(end_index=7268, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKR4Ug7Rl0vKLEC6dbPHi5LVxs2zmsvLWLLYkQsJ6kVeAoT3FL4pKuh6B0e9VALK29Huj-MP0dXgjqNvL35GTmJA13iJ7c0BaCktldGwS7UZ92cF_A4QSVmDVVkwbpzs0nwLWM5dc3tdC8I18vYE-fSlBr4zPHxGgfJ3XAJeFAJnvCR_ZwGM4amE6IzQtvcp7CzugtlG595JgHgYwQvRxbbTundSg2V3Iz74JU4g6c', start_index=7250)
Annotation(end_index=7268, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHD_vKZoUowDf038c0B3fYFTa5JL4o31QV6Kr4GjqXcsXqDKxc3E4BwyLLblFqMDsRYsUuiIkXiy8L4vmPcesUEI6fM6WMR5g1HbucyA1rQOQXF8I-ICmIgBwo8xTMWXDOcOlB8WmYO_k0tYGwNWsZg6pIpaueQYEqjp6RazXXvcvCWqH0kyr2FqF5PRMuTXs3ekdDx-iQww84xm0IlTyPl3La-6fo4fM26', start_index=7250)
Annotation(end_index=7268, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGCxI-O-8bMQKa6jXQFuwoUFDOgNk1XLijEXuWGWf2BMY3tgLUhX8Q6MU1f1bVb52tghxHua-5p_GrfIg3KsggGZ-4fggoYp-7v2Mk5jqG0gdm8F2kCh-qSqqF55Oct2T1kpE9rtKiZ5Gen8QFdmvUCpAdyNrJxKVaLGO6C03oo6ssoPD724D7', start_index=7250)
Annotation(end_index=7750, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHD_vKZoUowDf038c0B3fYFTa5JL4o31QV6Kr4GjqXcsXqDKxc3E4BwyLLblFqMDsRYsUuiIkXiy8L4vmPcesUEI6fM6WMR5g1HbucyA1rQOQXF8I-ICmIgBwo8xTMWXDOcOlB8WmYO_k0tYGwNWsZg6pIpaueQYEqjp6RazXXvcvCWqH0kyr2FqF5PRMuTXs3ekdDx-iQww84xm0IlTyPl3La-6fo4fM26', start_index=7740)
Annotation(end_index=7986, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdxR7pMH7wCZaXpnfQ_Pkx4duFdxRk4YatNKp0UY-6KFUaDRzt6xpxdf2eyJZ_a-_B9JO-sF680j0KXTp1OtpLkV5zYeZUZyUNIgTUwVWjf9Q-VXBXtAI=', start_index=7972)
Annotation(end_index=7986, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkMHMf5iCpZ6W9uUM3Jr417EVqFdqY-N0zSryZEzqtR9gNBEGuVfxdRCxe-sAWzVO7qpQU-Fxa9uy3d8cKFy-wlp4H5DdWGx3uagdSebPiYwMjYS1M29dPxBNif2QfKAQCL7J28mVLinOqa0c_-U2LRr64nLa4IwrgHbsKuooHmioXEpQ4Jrst1Z-sbDqBK-7PnlhirdBDtcR1sJfUw1D3FNL4-yMua99rcCP9', start_index=7972)
Annotation(end_index=8391, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkMHMf5iCpZ6W9uUM3Jr417EVqFdqY-N0zSryZEzqtR9gNBEGuVfxdRCxe-sAWzVO7qpQU-Fxa9uy3d8cKFy-wlp4H5DdWGx3uagdSebPiYwMjYS1M29dPxBNif2QfKAQCL7J28mVLinOqa0c_-U2LRr64nLa4IwrgHbsKuooHmioXEpQ4Jrst1Z-sbDqBK-7PnlhirdBDtcR1sJfUw1D3FNL4-yMua99rcCP9', start_index=8377)
Annotation(end_index=8391, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHozhB0ifX1tpvDzfcaK9u78KupiiF2Vj5C6_tBIUaclhHuo2yWS-m4w4fCUXvF264x7p9OVb6YpldbD2323FUgMGrNn59z6IwOsnSKKww2b26hdXitVsYntZ9rAcjmIsraWMffqp_VCSdA_hi7CE-Mtv0=', start_index=8377)
Annotation(end_index=9213, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkMHMf5iCpZ6W9uUM3Jr417EVqFdqY-N0zSryZEzqtR9gNBEGuVfxdRCxe-sAWzVO7qpQU-Fxa9uy3d8cKFy-wlp4H5DdWGx3uagdSebPiYwMjYS1M29dPxBNif2QfKAQCL7J28mVLinOqa0c_-U2LRr64nLa4IwrgHbsKuooHmioXEpQ4Jrst1Z-sbDqBK-7PnlhirdBDtcR1sJfUw1D3FNL4-yMua99rcCP9', start_index=9203)
Annotation(end_index=9422, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHozhB0ifX1tpvDzfcaK9u78KupiiF2Vj5C6_tBIUaclhHuo2yWS-m4w4fCUXvF264x7p9OVb6YpldbD2323FUgMGrNn59z6IwOsnSKKww2b26hdXitVsYntZ9rAcjmIsraWMffqp_VCSdA_hi7CE-Mtv0=', start_index=9412)
Annotation(end_index=9729, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCF25ubYBqCCH0VK6JJVhK47iOrcvp1liimwRXlXFDTWhe6WyOMH5kwrlKqmDPSyuNipTC_wDExmLdC36lUnIYVayohz1-Ri9N9FsLzPxo4twwCxL4-lXHYd_qmrgYtl-3YOGjRmKe4gd5PoTV0E-EPNs4bA==', start_index=9715)
Annotation(end_index=9729, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHozhB0ifX1tpvDzfcaK9u78KupiiF2Vj5C6_tBIUaclhHuo2yWS-m4w4fCUXvF264x7p9OVb6YpldbD2323FUgMGrNn59z6IwOsnSKKww2b26hdXitVsYntZ9rAcjmIsraWMffqp_VCSdA_hi7CE-Mtv0=', start_index=9715)
Annotation(end_index=10208, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKR4Ug7Rl0vKLEC6dbPHi5LVxs2zmsvLWLLYkQsJ6kVeAoT3FL4pKuh6B0e9VALK29Huj-MP0dXgjqNvL35GTmJA13iJ7c0BaCktldGwS7UZ92cF_A4QSVmDVVkwbpzs0nwLWM5dc3tdC8I18vYE-fSlBr4zPHxGgfJ3XAJeFAJnvCR_ZwGM4amE6IzQtvcp7CzugtlG595JgHgYwQvRxbbTundSg2V3Iz74JU4g6c', start_index=10194)
Annotation(end_index=10208, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTHaW_lyl0lvb7tgSR72Wb05ztq5m9nFOYQkwgeYTG74A2_cDibP-eWULyxOzTEsmF7OJSwF9ccVp3a5Mz5vauiJHNJuc-oOsrAWCk9fU8par7RC_SKPAWV1OpdLycETaPP81jVh2zEgAk0zJOXscSG5sHoTQrtdFC', start_index=10194)
Annotation(end_index=10747, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErmJs2lMMiB43m5jpIoCSyisGalMRcl5P_Hc7QO0qqTKgBfldw2nwF-y002Fonxodoq35ncs_ki1SJ4ZhUwAzRaAor69Vk-8YiOO5g1JJRtnbMQ4psSzxre19yYp9RC3u7dTQeVbtCzBQYJ4fxe5HcdAHODKWjgA==', start_index=10725)
Annotation(end_index=10747, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGO76NVeW67ukxHYM0I2MNd7GSucFud9VwWtzlmB-bKej1lE3tBOeNcJmIdX752t0WV9jEejqVq8rGNrpGI_kLZqmoQbuTbGeGqwKJe9ZgCAjSVPuzaSbHrfcgVq-nL5mD2hZ4hbTOQiXc6mvtC3m65E9ZfyMTaBc4Nw0uXd0cEQhLq3Z_52kRp7tijpFAGQdYo1G1rj7wdpt3N8ck1yrQkoJwaHTXx3f1_cTAr2hg34oiubQ==', start_index=10725)
Annotation(end_index=10747, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHozhB0ifX1tpvDzfcaK9u78KupiiF2Vj5C6_tBIUaclhHuo2yWS-m4w4fCUXvF264x7p9OVb6YpldbD2323FUgMGrNn59z6IwOsnSKKww2b26hdXitVsYntZ9rAcjmIsraWMffqp_VCSdA_hi7CE-Mtv0=', start_index=10725)
Annotation(end_index=10747, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuDOeZYZfsJ8mGRrF-hAPgPQZEBmFU95DNycSMdbg2ZJxE3HtzFHWMgmGdGrNXYpm5f8vLrdO6lfoINNGzBStFOKcTiqF5Er1Xe2Vjf3rZJ94ZX2vvwcIRkZJVsGWaYYzvDmbe3vEGSxFhdU1vqdkbFsJnEizjEjNMU3pWJUqN16lZbulLZjPPaY2ReQ9FD2DbBuCblF2Uifg-9M1O_2y9DZ9M6aTMj0lNOh2atcIR5L2a1-NaK21gvSw11fCTt40=', start_index=10725)
Annotation(end_index=11118, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyaF0YpR8By1BRj0UN7h09vTs-bau4TKcwWGjweqyHrlX11aj9TFjKDlbW7dAsgAbzsZD2fGoJsh0T9aRm8n22pZ1M35mH3bFcmwWPSPmrmKvqzGYEdRDVGT0bHHsVPSFLu1xv6t34o7eRRJaWny7Sc9wNQFTKZ8ElV7Yjlec2KNyrD7I_pvmDVWtc', start_index=11108)
Annotation(end_index=11442, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFG-RD77TgEdMz4qg-JP0SWSvXYmHgNpegd21NRoY0pIy-tKvkR3JLsPGbE6TJeGlom0t-Ub0njXq2GSe0DGrVDe78Yy1oQySn5jA7Q4qNfph6NoB3CTB1dr7soXSwYjLlAWyWnUF6yUB5EZXxNtAtDwL9xBSlFrR1xspCt85lJTBXYsnZI3tuaVK-LT-Et9fLzCUXmVC8FwrJGECtSty8kxEsoT3gJUElX8XWSrhfUXBSUUB7UusN_Lyp66g==', start_index=11425)
Annotation(end_index=11442, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHGkqOodawyqx4K0L88O-GEroMY0TmSavUccTvQmFvv7aphUV29tRd8BZjHnnNpigPjiDXBxLOcSHf2YmiT3KVaaWaSJ8Oc_y6jmVzlHpztgxiXOfMPxqEYDgxBngh2wOCfIGW2bAeuYCCG7eF-EOcIHPrB9i5NpsVwSvUAwrYJHJoShy0G7MdMZUy23oP3mqhGa-mDVX1-mIkjp8zNv0hkckYhNy-vjC8FSbNmw==', start_index=11425)
Annotation(end_index=11442, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXutS4lTy5WUeocsX_0LyUm8zVwkQSmi06c972KchgUEJhI2XL3w_8Py4tR6oPJN6h-aPSxTiEXgdlV5Kug43FD_Nalw_trkMcQ_bfbNrzt5AJFKKWLgciAZ63o9K3BIVPFbpJQw==', start_index=11425)
Annotation(end_index=12200, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFT2RLUdysOANh_eRPhEG4KhDlMljjpKz2RsW4_RA3PFrdRW24WQ-25XcGOd3DfILm1txOUnSPvztNsBBuQlmvs-zYWPmVkI_inf4smh0YJNBAwPxUHsKujF0FtpVe5FkqdWG88aikJOhAvjCZMixSJ9pfZtg==', start_index=12186)
Annotation(end_index=12200, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAGwnnOsX5zZQkd4FKMA5v7a11ivCdIr3fscu4mFWwKYnpxVdkvx0jNrZux_SAjAesZbE2b0DNRGD1KGjgFCWRf7X37yPKxYIfMnCCbqGGpgaNuCiDCE5d6lbIuwMFDL-4IcHZR4R4uIUPZ0FFZFDAoM6jDarw0gTCxNFazWoMZNTcS-LzhdKSRdWNNM2-Shii5JHHWYNJjttKo_bz', start_index=12186)
Annotation(end_index=12443, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGTAKU-gjd41pfvid6cjk8ezY_ezTzJIzRtASUxCYJ8-JeXcev3vLZMJTBJ6F4apgQOTEHDAjjOoc8A-A0p57CB4H4iTz2-0L5R-SsIoth4cihhimJeTab3QRGGiOprNltgp7yX_sWkynTMcQLgymYWu0livpRzz7ZReSLGhHoeqD2fgVdqURfSwymJweYLCIw0g==', start_index=12429)
Annotation(end_index=12443, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1WogzdY99yfr967y0EmkLG12QdP8GsSvG_29guJuFQ_VbnFKGj43wSCH-juzAoy7GbothTTVHyoSk1V4l0ja4zZb15wPTJw82IOvrMvJ-2sJpHLM1ig4tipLxhq62zTiEV6jldIqPkJitBg8Cu5zfIbmDmn3EmSaluc23lg8AIFVd4X_6AqriDq2IgQ==', start_index=12429)
Annotation(end_index=12965, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFEjrHqxmNzAtw89-NjVUCJ3bhVYZj4YWz3QgAUDUkxUPEY-1nleFVx5mOLy16LIaJUQJn2TMxvNHRVZjI6ZNFl-qsrGtWgyimUmTpjTQ4DTjVmSmBfK96_0rqlmHgzTzFf3dzS4SjWQ02843bb_AY064B__yYJ9w=', start_index=12947)
Annotation(end_index=12965, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFpGvUMWa_mJQGYnDPaBqh4gltG4K0V7mZrYQCMfpQxzlE3S-f_6I37H3bZRi8B_YbAC8JFy8_r5wE2rILbpwBA8UHm67T6NkQjvWhRE78h3Mbzu-BRmX3fLan3OtOeG7iw5f6KGgvxCFS4Wso45eHaZyObZnAEE86cuicvqq-mC_VcC3BLiDcRA9I95B-hzu-4dEDdcdIwtmcbqhbcEzbDPrh', start_index=12947)
Annotation(end_index=12965, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGki0LRoRUyS8YQTQ0rhr3aCrOJ3xuHZcx3OetUGGAWHuiABySNPJt5ljyDrWyVhrz8rSo08LkAgf6wEERVVjIaLU7KD9JCmz4wu9x0UXv4m6f3w6fnPtQvgpnYLjuek8B1lxNiICIW-kfrtVVqjAYkpMQ=', start_index=12947)
Annotation(end_index=13359, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEm3TpdxG6jpkUno6zl8tTEoF851F6mLbEAOrFudAPzlL8HXkzK6kKsgd4wiLkK0AgnnmwSpHQ5eClwlunNU-UwXoUZYxyJsIwPNVXXLJ5UsM4L8Bo5KQwOnw==', start_index=13346)
Annotation(end_index=13359, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnsljJm7xcVnB9rXcNqxLfFGRFxcqMhUSLWp3i-8ZUZ54ghbHgu8WzUTbThjDANJF1nn4qZqCEQrlR4-Ew5ga7f85OoopVmO9FG78ktYMoWaCs8jjA8hv_5vJU2FA8Og==', start_index=13346)
Annotation(end_index=13614, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkxgHjMD48uEU-voEaN0hXJbSenVjXA-Qds-tQFTMH2hk_27oR02e6XTy0tL41Wu8BxRXXRocI5FT2jc0jRqOLm8aKaJxElHQrUtxt6NVw5qzF1xKJux2TrOXIIwZN6ZlkMhCeU9nMdVt7YSaXulFMoNb5JQF5-tXHfG2Vo__VguNP5tmSkOS_hnVZ7I3EdYHvoo-a1Jc-Nrc=', start_index=13596)
Annotation(end_index=13614, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGa1k6dwxbms_ctSvHkIWIh7_F3Imaolrt1QeI1KIFZAliVQEvI36_hRNiqWQmloshVy-nC3ElY10PgfXxONRP3ROdoiupL_l5Ry0W9qe54CAHbmwwgBZF72wKf2WAQumK4KbK7O1JB87SDOAWFqFBK8tUvsusiFtvbxXKcQi5r1jyV0nVgcFeqHtloBhRNVlzTXB_Nnmyx', start_index=13596)
Annotation(end_index=13614, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHv2N9sQY5QnHqBxNMZIVZA1KtnOpMeQQ-sDP6dSO2lv44T38AJY0wAHONz6D1bwjrocVM-zTznDU9pqwVqBKNj2sX9afyQaqQKQUWzu9PWepWn7ESAXs02mOzDl13Kdh73CiI3LUM74g0ba_pm7KlYiCwG7itDU9iXwJbHitbpF2ZKFQNDFD0xP2jZK54Ew84pRoCjg3Rz1YYkYpJlCIgmU3kvI3nDIlC3Le9Feu9e_6FXEeBSgdiPYX-adr3JLyWhHBAzEw==', start_index=13596)
Annotation(end_index=13853, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPXg5B3qGKNG9NQNOjnYOx0BpURJSLNi6H9CUE6GHvxbhXEWraCnu0c9tS9MXNq-bvoHp1TGhNqcuDZEidkEjoN2O5sS7LyZTnL1SMf-F_4yog5oouWdbdiZmAETvlTLx8pghXJh1TVEaaz48pqTtZztahlaU=', start_index=13836)
Annotation(end_index=13853, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyNd0rl2rYIrgcKud1mU-9xRR7czFnRW0HCNexVEMNzcXmKS6EdFBUFG8YF1RYPbTujm4WoxxNxw8yYxbVpp8VOC3Blk2MTvOGiheDjhyeU-KUi71o6QapGgNVTNfMKELpI0nXbe25YxyEkKJNn7dznnI1QHNbQp8bZt948UVYtL11gowpgA==', start_index=13836)
Annotation(end_index=13853, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjZlBJLqDb3Ih7YdIttmGYGLs2y5jsk2k6pZu9LP7yJGWDAghaf74j9lFvJlAtpW8k4pqF877W3qchmZmrVvqtH45qE-m6vrKOIA8Q-iV-7Djb7Fsk6gJP_rlXDiRRTNTPhKH72KmhY3YHE5hjVRAJnAlWFYdzgEjxcfxpgP_6Gg7DCBYxvKSqBhhXtXoQA_q1kjpFx4wxp3U9DLEiR8x60DT04q73FuxVptv6tKO-ieMTBpIudsu7ms-3', start_index=13836)
Annotation(end_index=14245, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkxgHjMD48uEU-voEaN0hXJbSenVjXA-Qds-tQFTMH2hk_27oR02e6XTy0tL41Wu8BxRXXRocI5FT2jc0jRqOLm8aKaJxElHQrUtxt6NVw5qzF1xKJux2TrOXIIwZN6ZlkMhCeU9nMdVt7YSaXulFMoNb5JQF5-tXHfG2Vo__VguNP5tmSkOS_hnVZ7I3EdYHvoo-a1Jc-Nrc=', start_index=14231)
Annotation(end_index=14245, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4dfuU9mSLZKB-7X4nU8sqwWf3T9Epvko9nKMgTF3W8w0aL-UDsl3xlAraE3uHeXn5G8S5VXJG4Tec3OoR6nvU7ufVcAY-kd8Eo6dkELiwT-_4hhFT9lOypw==', start_index=14231)
Annotation(end_index=14508, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEm3TpdxG6jpkUno6zl8tTEoF851F6mLbEAOrFudAPzlL8HXkzK6kKsgd4wiLkK0AgnnmwSpHQ5eClwlunNU-UwXoUZYxyJsIwPNVXXLJ5UsM4L8Bo5KQwOnw==', start_index=14495)
Annotation(end_index=14508, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnsljJm7xcVnB9rXcNqxLfFGRFxcqMhUSLWp3i-8ZUZ54ghbHgu8WzUTbThjDANJF1nn4qZqCEQrlR4-Ew5ga7f85OoopVmO9FG78ktYMoWaCs8jjA8hv_5vJU2FA8Og==', start_index=14495)
Annotation(end_index=15134, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEGt26x2FKxDEoeUz3tyQe9xw_8NhiiwbbjYK-mpIXRa8HdN6UGYJoU14IzKZ5GpsaMGRKgbWiHjY6mujh3Hiv6VyaMCSnzG1vbhexXX6d7GCIyZwbcHR1YfXtEZmLtp5iW9ocQdhnJmbkAbxJZGkcKa4QETydcQ-IjYZafGADtDqwlVZzj0T6RN0y0QOr4HL2_Gf0aPOjoTyrs27WLdXYqlNpfLV-M1pTDA==', start_index=15121)
Annotation(end_index=15134, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGO76NVeW67ukxHYM0I2MNd7GSucFud9VwWtzlmB-bKej1lE3tBOeNcJmIdX752t0WV9jEejqVq8rGNrpGI_kLZqmoQbuTbGeGqwKJe9ZgCAjSVPuzaSbHrfcgVq-nL5mD2hZ4hbTOQiXc6mvtC3m65E9ZfyMTaBc4Nw0uXd0cEQhLq3Z_52kRp7tijpFAGQdYo1G1rj7wdpt3N8ck1yrQkoJwaHTXx3f1_cTAr2hg34oiubQ==', start_index=15121)
Annotation(end_index=15384, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEGt26x2FKxDEoeUz3tyQe9xw_8NhiiwbbjYK-mpIXRa8HdN6UGYJoU14IzKZ5GpsaMGRKgbWiHjY6mujh3Hiv6VyaMCSnzG1vbhexXX6d7GCIyZwbcHR1YfXtEZmLtp5iW9ocQdhnJmbkAbxJZGkcKa4QETydcQ-IjYZafGADtDqwlVZzj0T6RN0y0QOr4HL2_Gf0aPOjoTyrs27WLdXYqlNpfLV-M1pTDA==', start_index=15371)
Annotation(end_index=15384, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErmJs2lMMiB43m5jpIoCSyisGalMRcl5P_Hc7QO0qqTKgBfldw2nwF-y002Fonxodoq35ncs_ki1SJ4ZhUwAzRaAor69Vk-8YiOO5g1JJRtnbMQ4psSzxre19yYp9RC3u7dTQeVbtCzBQYJ4fxe5HcdAHODKWjgA==', start_index=15371)
Annotation(end_index=15591, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEGt26x2FKxDEoeUz3tyQe9xw_8NhiiwbbjYK-mpIXRa8HdN6UGYJoU14IzKZ5GpsaMGRKgbWiHjY6mujh3Hiv6VyaMCSnzG1vbhexXX6d7GCIyZwbcHR1YfXtEZmLtp5iW9ocQdhnJmbkAbxJZGkcKa4QETydcQ-IjYZafGADtDqwlVZzj0T6RN0y0QOr4HL2_Gf0aPOjoTyrs27WLdXYqlNpfLV-M1pTDA==', start_index=15579)
Annotation(end_index=15591, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEm3TpdxG6jpkUno6zl8tTEoF851F6mLbEAOrFudAPzlL8HXkzK6kKsgd4wiLkK0AgnnmwSpHQ5eClwlunNU-UwXoUZYxyJsIwPNVXXLJ5UsM4L8Bo5KQwOnw==', start_index=15579)
Annotation(end_index=15815, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4LwqY9bthHldbYW4RalgIEXO8Vpp2rrf9wGNnhjF11I-UXdrLkKsSNv01EJx8FjOiXUIvC8x_6HM61eF77UfEz1h8NTRyjka49PJalPRc2y5VZwM50GXTmQ==', start_index=15801)
Annotation(end_index=15815, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHW4zTMqx6YB5RhV066BG-PBd4Tmz2IEBRIFMY0GH7j6M5XB2GJsGCGMEitkvl0SufdhiS2-CaAph_gnT5kANHr6VPOmS_qlxHeR88q6pOsJUS3bpPozFqkwFqUsbGEhRp38u0c_JwrSOi_7WLo305u_0wvfO_baoB9ChgjlS87lUzKebFUBxX_x8t0eBMwl81o0FnRsRtObG0AH5V4RSMTxenTUB0sVWs3EsYkEA_27R8MJjRjsrK0FlztPJ0UDiSKivunAo11Csdv38fP5CMfVGh_Mw==', start_index=15801)
Annotation(end_index=15980, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnSVGSgX0xHKExNLwxhzsSEezeQTU1x_XdaRZ9VDlZkekC_fKbLzWJZaRoS_ycmmiaA4rFgI8Y7tv0efZ-avTQgaSiKUti15UGZI6Cs5wmhIcxHTaX3_xXw0XK6khhqDwRKwBUJymft4pNFxaOXvziZzFuimT47ZQOBTY_Qi_-nBwQyzq5kcKHJmvAh0CKc52X2evY9R9njlrtKzJkuCs=', start_index=15966)
Annotation(end_index=15980, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkMHMf5iCpZ6W9uUM3Jr417EVqFdqY-N0zSryZEzqtR9gNBEGuVfxdRCxe-sAWzVO7qpQU-Fxa9uy3d8cKFy-wlp4H5DdWGx3uagdSebPiYwMjYS1M29dPxBNif2QfKAQCL7J28mVLinOqa0c_-U2LRr64nLa4IwrgHbsKuooHmioXEpQ4Jrst1Z-sbDqBK-7PnlhirdBDtcR1sJfUw1D3FNL4-yMua99rcCP9', start_index=15966)
Annotation(end_index=16518, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEGt26x2FKxDEoeUz3tyQe9xw_8NhiiwbbjYK-mpIXRa8HdN6UGYJoU14IzKZ5GpsaMGRKgbWiHjY6mujh3Hiv6VyaMCSnzG1vbhexXX6d7GCIyZwbcHR1YfXtEZmLtp5iW9ocQdhnJmbkAbxJZGkcKa4QETydcQ-IjYZafGADtDqwlVZzj0T6RN0y0QOr4HL2_Gf0aPOjoTyrs27WLdXYqlNpfLV-M1pTDA==', start_index=16509)
Annotation(end_index=16909, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgz0zjIGTFw_XVT44jWsHm1GVftptj0WruefcH6-c94OOuxESvqhdYQKJbOeoXqfAXBrRWMGg2jXSd0_AC-9hZ9UocNy8wTExwAs9WKGWc1jEK58ydpBxi9KEPLuXT7yjm7Cjyg-FviRkQ0Lw3pCa01Foc5WRq9kpaVS8ln4TFcol8tqJDs89aAW3MFSGCNaUInnJnvnAH64_SYDLJj6yPT2dKLE9tbfGDqoMzdqPflJIv31-xX94qlTBNwMIrIaHayVqncyyUoqKhXml32e72dk6NMlg=', start_index=16897)
Annotation(end_index=16909, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGiiMlAscLpJ0dxDLM-O86PFkOAKS0Sn0iwDfEYiYWjN4J7g4M_RF4fLGePDYT_KQhhGB4dmt5S-LSeV-N1xC0W78i0KqzNKin4aEEcErtEmC-Ip7I_29lr1slzID5VyBN7Knq4iK-z6jINuZuKLZ7VJlBcNgRk1UVtmWQX0JbJThQlVRwBEhOhrhu4ILGI4wnffq9__if2ShUGHGBdqCW9kisdjnF5RtmSE10lD8JvXrp5o8G5H1KOfH-BrZ-sCAMglhXb_bOwL1_mATOsYBo=', start_index=16897)
Annotation(end_index=17267, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEGt26x2FKxDEoeUz3tyQe9xw_8NhiiwbbjYK-mpIXRa8HdN6UGYJoU14IzKZ5GpsaMGRKgbWiHjY6mujh3Hiv6VyaMCSnzG1vbhexXX6d7GCIyZwbcHR1YfXtEZmLtp5iW9ocQdhnJmbkAbxJZGkcKa4QETydcQ-IjYZafGADtDqwlVZzj0T6RN0y0QOr4HL2_Gf0aPOjoTyrs27WLdXYqlNpfLV-M1pTDA==', start_index=17258)
Annotation(end_index=18600, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEm3TpdxG6jpkUno6zl8tTEoF851F6mLbEAOrFudAPzlL8HXkzK6kKsgd4wiLkK0AgnnmwSpHQ5eClwlunNU-UwXoUZYxyJsIwPNVXXLJ5UsM4L8Bo5KQwOnw==', start_index=18591)
Annotation(end_index=18664, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnSVGSgX0xHKExNLwxhzsSEezeQTU1x_XdaRZ9VDlZkekC_fKbLzWJZaRoS_ycmmiaA4rFgI8Y7tv0efZ-avTQgaSiKUti15UGZI6Cs5wmhIcxHTaX3_xXw0XK6khhqDwRKwBUJymft4pNFxaOXvziZzFuimT47ZQOBTY_Qi_-nBwQyzq5kcKHJmvAh0CKc52X2evY9R9njlrtKzJkuCs=', start_index=18650)
Annotation(end_index=18664, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1WogzdY99yfr967y0EmkLG12QdP8GsSvG_29guJuFQ_VbnFKGj43wSCH-juzAoy7GbothTTVHyoSk1V4l0ja4zZb15wPTJw82IOvrMvJ-2sJpHLM1ig4tipLxhq62zTiEV6jldIqPkJitBg8Cu5zfIbmDmn3EmSaluc23lg8AIFVd4X_6AqriDq2IgQ==', start_index=18650)
Annotation(end_index=18727, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZLNXuCDK2LI669s_sFrAcl-PJLtvLDffTztZfU-1Tg_36GpmoP5bUgAB9P8mK11DC-WX8F1mNyPNpeYGHCJLq0yiQmMpYgQybyX3lX38gVJOU5WCdJ9FGCdOqG36DKHlGz5PYdfVEtR6EA-iHGW6Wi-8kYd4U0BVDeT2qOMmIN6CtBeIsvJaC34pmP23vCPlIeIe3-3-JW3jxXOfR7WO4xOTgf1YiAg==', start_index=18715)
Annotation(end_index=18727, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHGkqOodawyqx4K0L88O-GEroMY0TmSavUccTvQmFvv7aphUV29tRd8BZjHnnNpigPjiDXBxLOcSHf2YmiT3KVaaWaSJ8Oc_y6jmVzlHpztgxiXOfMPxqEYDgxBngh2wOCfIGW2bAeuYCCG7eF-EOcIHPrB9i5NpsVwSvUAwrYJHJoShy0G7MdMZUy23oP3mqhGa-mDVX1-mIkjp8zNv0hkckYhNy-vjC8FSbNmw==', start_index=18715)
Annotation(end_index=18801, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKR4Ug7Rl0vKLEC6dbPHi5LVxs2zmsvLWLLYkQsJ6kVeAoT3FL4pKuh6B0e9VALK29Huj-MP0dXgjqNvL35GTmJA13iJ7c0BaCktldGwS7UZ92cF_A4QSVmDVVkwbpzs0nwLWM5dc3tdC8I18vYE-fSlBr4zPHxGgfJ3XAJeFAJnvCR_ZwGM4amE6IzQtvcp7CzugtlG595JgHgYwQvRxbbTundSg2V3Iz74JU4g6c', start_index=18787)
Annotation(end_index=18801, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHD_vKZoUowDf038c0B3fYFTa5JL4o31QV6Kr4GjqXcsXqDKxc3E4BwyLLblFqMDsRYsUuiIkXiy8L4vmPcesUEI6fM6WMR5g1HbucyA1rQOQXF8I-ICmIgBwo8xTMWXDOcOlB8WmYO_k0tYGwNWsZg6pIpaueQYEqjp6RazXXvcvCWqH0kyr2FqF5PRMuTXs3ekdDx-iQww84xm0IlTyPl3La-6fo4fM26', start_index=18787)
Annotation(end_index=18856, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHozhB0ifX1tpvDzfcaK9u78KupiiF2Vj5C6_tBIUaclhHuo2yWS-m4w4fCUXvF264x7p9OVb6YpldbD2323FUgMGrNn59z6IwOsnSKKww2b26hdXitVsYntZ9rAcjmIsraWMffqp_VCSdA_hi7CE-Mtv0=', start_index=18846)
Annotation(end_index=18926, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjZlBJLqDb3Ih7YdIttmGYGLs2y5jsk2k6pZu9LP7yJGWDAghaf74j9lFvJlAtpW8k4pqF877W3qchmZmrVvqtH45qE-m6vrKOIA8Q-iV-7Djb7Fsk6gJP_rlXDiRRTNTPhKH72KmhY3YHE5hjVRAJnAlWFYdzgEjxcfxpgP_6Gg7DCBYxvKSqBhhXtXoQA_q1kjpFx4wxp3U9DLEiR8x60DT04q73FuxVptv6tKO-ieMTBpIudsu7ms-3', start_index=18914)
Annotation(end_index=18926, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGz9IYmnJDbTCmqSwiEWv3oK1N-v-wk6IJ887fqQUyaPPZWQ556IVAj5_QSn8iE6bF1YdskZvk6xGPWp9R76o6HaZ8PNwOJ-u7ufJEPbnCuBm2HLfhKuQ==', start_index=18914)
Annotation(end_index=18976, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEGt26x2FKxDEoeUz3tyQe9xw_8NhiiwbbjYK-mpIXRa8HdN6UGYJoU14IzKZ5GpsaMGRKgbWiHjY6mujh3Hiv6VyaMCSnzG1vbhexXX6d7GCIyZwbcHR1YfXtEZmLtp5iW9ocQdhnJmbkAbxJZGkcKa4QETydcQ-IjYZafGADtDqwlVZzj0T6RN0y0QOr4HL2_Gf0aPOjoTyrs27WLdXYqlNpfLV-M1pTDA==', start_index=18967)
Annotation(end_index=19053, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkMHMf5iCpZ6W9uUM3Jr417EVqFdqY-N0zSryZEzqtR9gNBEGuVfxdRCxe-sAWzVO7qpQU-Fxa9uy3d8cKFy-wlp4H5DdWGx3uagdSebPiYwMjYS1M29dPxBNif2QfKAQCL7J28mVLinOqa0c_-U2LRr64nLa4IwrgHbsKuooHmioXEpQ4Jrst1Z-sbDqBK-7PnlhirdBDtcR1sJfUw1D3FNL4-yMua99rcCP9', start_index=19043)
Annotation(end_index=19105, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFG-RD77TgEdMz4qg-JP0SWSvXYmHgNpegd21NRoY0pIy-tKvkR3JLsPGbE6TJeGlom0t-Ub0njXq2GSe0DGrVDe78Yy1oQySn5jA7Q4qNfph6NoB3CTB1dr7soXSwYjLlAWyWnUF6yUB5EZXxNtAtDwL9xBSlFrR1xspCt85lJTBXYsnZI3tuaVK-LT-Et9fLzCUXmVC8FwrJGECtSty8kxEsoT3gJUElX8XWSrhfUXBSUUB7UusN_Lyp66g==', start_index=19091)
Annotation(end_index=19105, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFT2RLUdysOANh_eRPhEG4KhDlMljjpKz2RsW4_RA3PFrdRW24WQ-25XcGOd3DfILm1txOUnSPvztNsBBuQlmvs-zYWPmVkI_inf4smh0YJNBAwPxUHsKujF0FtpVe5FkqdWG88aikJOhAvjCZMixSJ9pfZtg==', start_index=19091)
Annotation(end_index=19169, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnsljJm7xcVnB9rXcNqxLfFGRFxcqMhUSLWp3i-8ZUZ54ghbHgu8WzUTbThjDANJF1nn4qZqCEQrlR4-Ew5ga7f85OoopVmO9FG78ktYMoWaCs8jjA8hv_5vJU2FA8Og==', start_index=19155)
Annotation(end_index=19169, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4dfuU9mSLZKB-7X4nU8sqwWf3T9Epvko9nKMgTF3W8w0aL-UDsl3xlAraE3uHeXn5G8S5VXJG4Tec3OoR6nvU7ufVcAY-kd8Eo6dkELiwT-_4hhFT9lOypw==', start_index=19155)
Annotation(end_index=19232, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErmJs2lMMiB43m5jpIoCSyisGalMRcl5P_Hc7QO0qqTKgBfldw2nwF-y002Fonxodoq35ncs_ki1SJ4ZhUwAzRaAor69Vk-8YiOO5g1JJRtnbMQ4psSzxre19yYp9RC3u7dTQeVbtCzBQYJ4fxe5HcdAHODKWjgA==', start_index=19218)
Annotation(end_index=19232, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGO76NVeW67ukxHYM0I2MNd7GSucFud9VwWtzlmB-bKej1lE3tBOeNcJmIdX752t0WV9jEejqVq8rGNrpGI_kLZqmoQbuTbGeGqwKJe9ZgCAjSVPuzaSbHrfcgVq-nL5mD2hZ4hbTOQiXc6mvtC3m65E9ZfyMTaBc4Nw0uXd0cEQhLq3Z_52kRp7tijpFAGQdYo1G1rj7wdpt3N8ck1yrQkoJwaHTXx3f1_cTAr2hg34oiubQ==', start_index=19218)
Annotation(end_index=19300, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgz0zjIGTFw_XVT44jWsHm1GVftptj0WruefcH6-c94OOuxESvqhdYQKJbOeoXqfAXBrRWMGg2jXSd0_AC-9hZ9UocNy8wTExwAs9WKGWc1jEK58ydpBxi9KEPLuXT7yjm7Cjyg-FviRkQ0Lw3pCa01Foc5WRq9kpaVS8ln4TFcol8tqJDs89aAW3MFSGCNaUInnJnvnAH64_SYDLJj6yPT2dKLE9tbfGDqoMzdqPflJIv31-xX94qlTBNwMIrIaHayVqncyyUoqKhXml32e72dk6NMlg=', start_index=19288)
Annotation(end_index=19300, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGiiMlAscLpJ0dxDLM-O86PFkOAKS0Sn0iwDfEYiYWjN4J7g4M_RF4fLGePDYT_KQhhGB4dmt5S-LSeV-N1xC0W78i0KqzNKin4aEEcErtEmC-Ip7I_29lr1slzID5VyBN7Knq4iK-z6jINuZuKLZ7VJlBcNgRk1UVtmWQX0JbJThQlVRwBEhOhrhu4ILGI4wnffq9__if2ShUGHGBdqCW9kisdjnF5RtmSE10lD8JvXrp5o8G5H1KOfH-BrZ-sCAMglhXb_bOwL1_mATOsYBo=', start_index=19288)
Annotation(end_index=19359, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGCxI-O-8bMQKa6jXQFuwoUFDOgNk1XLijEXuWGWf2BMY3tgLUhX8Q6MU1f1bVb52tghxHua-5p_GrfIg3KsggGZ-4fggoYp-7v2Mk5jqG0gdm8F2kCh-qSqqF55Oct2T1kpE9rtKiZ5Gen8QFdmvUCpAdyNrJxKVaLGO6C03oo6ssoPD724D7', start_index=19345)
Annotation(end_index=19359, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcipvERZPFgi7mBixkiZYO2n7KJ7My4tvQ4ezXvQziSdLwWYM4yYVyH18MKz4HONy0_8Y_p6f2FiwqC8QJqMs57Pve3nij2zMc23EG_JDwHi0WfP7TGGrVVMP8', start_index=19345)

## Sources
