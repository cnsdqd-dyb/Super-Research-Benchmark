# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 6e9a588d | **Time:** 274.90s | **Cost:** $1.18665
--------------------------------------------------------------------------------

# Inventory Synchronization Strategies and Turnover Optimization via Inter-Product Demand Correlation Decomposition

**Key Points**
*   **Inventory Synchronization and Turnover:** Inventory synchronization strategies, particularly Joint Replenishment Problems (JRP), can significantly optimize inventory turnover rates by balancing ordering costs against holding costs. By coordinating the replenishment of multiple products, firms can reduce the aggregate inventory required to support a given service level, thereby decreasing the denominator in the turnover ratio [cite: 1, 2].
*   **Role of Demand Correlation:** Inter-product demand correlation is a critical, often overlooked factor. Positive correlation (complementary products) suggests synchronization is highly effective for cost reduction, while negative correlation (substitutable products) offers opportunities for risk pooling, which directly reduces safety stock requirements and boosts turnover [cite: 3, 4].
*   **Decomposition Techniques:** Two primary forms of decomposition facilitate this optimization:
    1.  **Spectral Decomposition (PCA/SVD):** These statistical techniques decompose the demand correlation matrix to separate signal from noise and identify latent demand drivers. This improves forecasting accuracy for sporadic or correlated demand, allowing for leaner inventory levels [cite: 5, 6, 7].
    2.  **Customer-Item Decomposition:** This control-theoretic approach breaks down complex multi-item stochastic inventory problems into single-unit subproblems. It is particularly effective in deriving optimal policies (e.g., state-dependent base-stock levels) in systems with correlated demand, ensuring that inventory is only held when the marginal benefit exceeds the cost [cite: 8].
*   **Optimization Mechanism:** By utilizing decomposition to accurately model the covariance structure of demand, firms can calculate precise safety stocks and joint reorder points. This minimizes "dead stock" (increasing efficiency) and prevents stockouts (maintaining sales volume), mathematically driving the inventory turnover ratio higher [cite: 9, 10].

---

## 1. Introduction

Inventory turnover, defined as the ratio of Cost of Goods Sold (COGS) to Average Inventory, serves as a fundamental barometer of supply chain efficiency and financial health [cite: 9, 11]. A high turnover rate implies that a firm is effectively converting working capital into revenue, minimizing the risks associated with obsolescence and holding costs. However, optimizing this metric is mathematically complex in multi-product environments where demand is uncertain and inter-related. Traditional inventory models often treat Stock Keeping Units (SKUs) as independent entities, an assumption that fails to capture the synergies and risks inherent in modern product portfolios [cite: 10, 12].

The query addresses a sophisticated intersection of operations research: the use of **inventory synchronization strategies**—specifically through the lens of **inter-product demand correlation decomposition**—to maximize turnover. This approach moves beyond simple Economic Order Quantity (EOQ) models to leverage the statistical structure of demand. By decomposing the correlation matrix of product demands (using techniques such as Principal Component Analysis or Singular Value Decomposition) and the control problem itself (via Customer-Item Decomposition), firms can theoretically achieve a "Pareto improvement": reducing average inventory levels without degrading service levels [cite: 5, 8].

This report provides an exhaustive analysis of these mechanisms. It explores how synchronization strategies like the Joint Replenishment Problem (JRP) interact with demand correlation, how decomposition methods isolate actionable signal from noise, and how these mathematical operations translate into higher inventory turnover rates.

## 2. Theoretical Foundations of Inventory Turnover and Synchronization

To understand how synchronization optimizes turnover, one must first establish the governing dynamics of the turnover metric and the mechanics of joint replenishment.

### 2.1 The Inventory Turnover Metric
The inventory turnover ratio ($IT$) is calculated as:
\[ IT = \frac{\text{Cost of Goods Sold (COGS)}}{\text{Average Inventory}} \]
To optimize (maximize) $IT$, a firm must either increase COGS (sales) or decrease Average Inventory, or preferably both [cite: 9, 13].
*   **Numerator (COGS):** Driven by demand fulfillment. Stockouts reduce COGS. Therefore, strategies must maintain high service levels.
*   **Denominator (Average Inventory):** Composed of Cycle Stock and Safety Stock.
    \[ \text{Avg Inv} = \frac{Q}{2} + SS \]
    Where $Q$ is the order quantity and $SS$ is the safety stock.

Synchronization strategies primarily target the **Average Inventory** component. By optimizing $Q$ through joint ordering (amortizing fixed costs) and optimizing $SS$ through correlation analysis (risk pooling), the denominator decreases, and turnover rises [cite: 2, 11].

### 2.2 Inventory Synchronization: The Joint Replenishment Problem (JRP)
Inventory synchronization involves coordinating the replenishment of multiple items to exploit economies of scale. The classic formulation is the Joint Replenishment Problem (JRP). In the JRP, a major setup cost ($S$) is incurred whenever an order is placed, regardless of the number of items, and a minor setup cost ($s_i$) is incurred for each specific item $i$ included in the order [cite: 2].

*   **Direct Grouping Strategy:** Products are grouped into sets that follow the same cycle time.
*   **Indirect Grouping Strategy:** Each product has a cycle time that is an integer multiple of a base cycle time [cite: 2].

**Impact on Turnover:**
JRP reduces the total ordering costs, which mathematically allows for smaller, more frequent replenishment of individual items compared to independent ordering (where the high major setup cost would force large batch sizes). Smaller batches ($Q$) reduce Cycle Stock ($Q/2$), thereby reducing Average Inventory and increasing Turnover [cite: 2, 14]. However, the effectiveness of JRP is heavily contingent on the **demand correlation** between items. If items are synchronized but their demands are negatively correlated, the firm may hold unnecessary stock of one item while waiting to order another [cite: 12].

## 3. Inter-Product Demand Correlation

The assumption of demand independence is a significant source of inefficiency in inventory management. Real-world demand is often correlated due to substitutability (negative correlation) or complementarity (positive correlation) [cite: 4, 10].

### 3.1 The Correlation Matrix
For a set of $n$ products, demand can be represented as a random vector $\mathbf{D} = (D_1, D_2, ..., D_n)$ with a covariance matrix $\Sigma$. The off-diagonal elements $\sigma_{ij}$ represent the covariance between product $i$ and product $j$.
*   **Positive Correlation ($\rho > 0$):** Items tend to be bought together (e.g., shampoo and conditioner). Synchronization is natural here; they should be replenished together.
*   **Negative Correlation ($\rho < 0$):** Items are substitutes (e.g., red vs. blue t-shirts). When demand for one is high, demand for the other is likely low.

### 3.2 Impact on Safety Stock and Turnover
The standard deviation of the aggregate demand during lead time ($\sigma_L$) for a pooled group of products is given by:
\[ \sigma_{pool} = \sqrt{\sum_{i} \sigma_i^2 + \sum_{i \neq j} \rho_{ij} \sigma_i \sigma_j} \]
*   **Positive Correlation Penalty:** If $\rho_{ij} > 0$, the aggregate variance increases. This requires *higher* safety stocks to maintain service levels, which suppresses inventory turnover [cite: 3].
*   **Negative Correlation Benefit (Risk Pooling):** If $\rho_{ij} < 0$, the aggregate variance decreases. The "peaks" of one product cancel out the "valleys" of another. This allows the firm to hold *less* total safety stock for the same aggregate service level, significantly boosting inventory turnover [cite: 4, 15].

Research on mergers and acquisitions confirms this phenomenon: firms with negatively correlated demand streams that merge and pool inventory realize significant improvements in inventory turnover compared to those with positively correlated demands [cite: 3, 4].

## 4. Decomposition Methodologies

To operationalize correlation data for optimization, "decomposition" is applied in two distinct ways: decomposing the *data* (to forecast and measure correlation) and decomposing the *control problem* (to manage complexity).

### 4.1 Spectral Decomposition of Demand (PCA/SVD)
High-dimensional demand data is often noisy. Spectral decomposition techniques like Principal Component Analysis (PCA) and Singular Value Decomposition (SVD) are used to decompose the demand correlation matrix into orthogonal (uncorrelated) components [cite: 5, 7].

#### 4.1.1 Mathematical Mechanism
PCA transforms the original correlated variables (SKU demands) into a new set of uncorrelated variables (Principal Components) that are linear combinations of the original variables.
\[ \mathbf{D} = \mathbf{W} \mathbf{P} \]
Where $\mathbf{P}$ are the principal components and $\mathbf{W}$ are the weights (loadings).
*   **Signal vs. Noise:** The first few components usually capture the majority of the variance (the "signal," such as seasonality or market trends), while the later components capture random noise. By reconstructing demand using only the leading components, firms can filter out noise [cite: 16, 17].
*   **Application to Turnover:**
    1.  **Noise Reduction:** SVD entropy approaches have been shown to improve predictive power in volatile markets [cite: 18]. Better predictions reduce the forecast error ($\sigma_\epsilon$), which is the primary driver of safety stock ($SS = z \cdot \sigma_\epsilon$). Lower $SS$ increases turnover.
    2.  **Clustering for JRP:** PCA loadings can identify which products share underlying demand drivers. Products with similar loadings on the first principal component are highly positively correlated and are ideal candidates for Joint Replenishment groups [cite: 5, 19].

#### 4.1.2 SVD in Sporadic Demand
For items with lumpy or sporadic demand (which typically have low turnover), SVD can be used to extract latent patterns that traditional time-series methods miss. This allows for tighter inventory control on slow-moving items, preventing the accumulation of obsolete stock that kills turnover rates [cite: 6, 20].

### 4.2 Customer-Item Decomposition
While PCA decomposes data, **Customer-Item Decomposition** is a method for solving the stochastic inventory control problem itself. It was pioneered to handle the "curse of dimensionality" in multi-item systems [cite: 8].

#### 4.2.1 The Approach
This method decomposes the complex multi-item problem into a series of single-unit subproblems. It tracks each unit of inventory and matches it to a specific future demand (the $k$-th unit ordered satisfies the $k$-th demand arrival).
*   **Cost Evaluation:** The expected cost for each unit is calculated based on holding costs (time spent in inventory) and backorder costs (time customer waits).
*   **Optimal Policy:** Research shows that for systems with correlated demand, the optimal policy derived via this decomposition is often a **state-dependent base-stock policy** [cite: 8, 21].

#### 4.2.2 Optimization of Turnover
By using Customer-Item decomposition, the system can dynamically adjust base-stock levels ($S$) based on the current state of correlated demands. Unlike static policies that hold a fixed buffer, this dynamic approach reduces inventory when the probability of demand is low (based on cross-correlations), thereby reducing average inventory and increasing turnover [cite: 8, 22].

### 4.3 Expectation-Maximization (EM) for Censored Demand
A major barrier to optimizing turnover is that "true" demand is often unknown due to stockouts (censored data). If a firm only looks at sales data, they underestimate demand variance and correlation.
*   **The EM Algorithm:** This iterative method estimates the parameters of the underlying demand distribution (including the correlation matrix) from incomplete data. It alternates between estimating the missing data (Expectation) and optimizing the parameters (Maximization) [cite: 10, 23].
*   **Relevance:** Accurate estimation of the *inter-product demand correlation* (using EM) prevents the "spiral of death" where under-forecasting leads to lower stock, more stockouts, and even lower future forecasts. Correctly sizing inventory for *true* demand ensures sales (numerator) are maximized while inventory (denominator) is efficient [cite: 10, 24].

## 5. Optimization Strategies: Synthesizing Synchronization and Decomposition

The integration of these concepts leads to advanced strategies for optimizing turnover.

### 5.1 Correlation-Based Clustering for JRP
Traditional JRP groups items based on holding/ordering cost ratios. A superior strategy utilizes **Demand Correlation Pattern (DCP)** decomposition [cite: 25].
*   **Strategy:** Use PCA/SVD to identify clusters of items with high positive correlation.
*   **Execution:** Apply Joint Replenishment policies (e.g., Can-Order policies) specifically within these clusters.
*   **Outcome:** Since these items move together, synchronizing their orders minimizes the "residual" inventory held. If Item A and B are always bought together, ordering them together means they arrive and leave inventory together, keeping the average inventory low and turnover high [cite: 12, 26].

### 5.2 Risk-Pooling via Negative Correlation Exploitation
For items identified (via decomposition) as negatively correlated:
*   **Strategy:** Do *not* necessarily synchronize their orders to arrive at the same time if capacity is constrained, but *do* pool their safety stock calculations.
*   **Execution:** Use a "Portfolio Effect" logic. The safety stock for the aggregate group is less than the sum of individual safety stocks.
*   **Outcome:** The firm holds significantly less total safety stock. Research on mergers indicates that this effect is the primary driver of post-merger inventory turnover improvements [cite: 3, 4].

### 5.3 Dynamic State-Dependent Control
Using Customer-Item decomposition results:
*   **Strategy:** Implement $(s, c, d, S)$ policies where the reorder points depend on the inventory position of correlated items.
*   **Execution:** If Item A's demand is highly correlated with Item B, and Item B has a surplus, the system might delay ordering Item A (anticipating a slowdown) or expedite it (anticipating a spike), depending on the lead-time correlation structure [cite: 8, 27].
*   **Outcome:** This dynamic adjustment prevents the buildup of cycle stock during low-demand periods, directly improving the turnover ratio [cite: 27].

## 6. Algorithmic Implementation Framework

To implement these strategies, an academic or practitioner would follow this high-level algorithmic approach:

1.  **Data Collection & Cleaning:** Gather historical sales data. Use **Expectation-Maximization (EM)** to correct for censored demand (lost sales) and estimate the true demand covariance matrix [cite: 10, 23].
2.  **Decomposition & Feature Extraction:**
    *   Apply **SVD/PCA** to the covariance matrix to identify principal components (latent demand drivers) [cite: 5, 7].
    *   Separate signal (leading components) from noise (trailing components) to refine forecasts [cite: 16].
3.  **Clustering & Grouping:**
    *   Cluster SKUs based on their loadings in the principal components. Group positively correlated items for **Joint Replenishment** [cite: 19, 25].
    *   Identify negatively correlated pairs for **Risk Pooling** analysis [cite: 3].
4.  **Policy Optimization (Customer-Item Method):**
    *   For high-value or complex groups, use **Customer-Item Decomposition** to solve for optimal state-dependent base-stock levels [cite: 8].
    *   Calculate the optimal joint reorder points ($s$) and order-up-to levels ($S$).
5.  **Execution & Monitoring:**
    *   Execute the synchronized replenishment.
    *   Continuously monitor the **Inventory Turnover Ratio** ($COGS / Avg Inv$) as the key performance indicator (KPI) [cite: 9, 11].

## 7. Empirical Evidence and Case Studies

### 7.1 Mergers and Acquisitions (M&A)
Empirical studies on M&A provide the strongest evidence for the benefits of correlation-based optimization. Research analyzing 270 same-industry mergers found that inventory turnover improved significantly post-merger. Crucially, this improvement was "especially pronounced in deals where the demand of bidder and target firms are negatively correlated prior to the merger" [cite: 3, 4]. This validates the theoretical prediction that decomposing demand to find and exploit negative correlations reduces safety stock requirements.

### 7.2 Bike Sharing Systems (Spatial Correlation)
While not "inventory" in the retail sense, bike-sharing systems function as inventory networks where bikes are the stock. Research using **Demand Correlation Matrices** and **GCNN (Graph Convolutional Neural Networks)** to decompose demand patterns shows that accounting for spatial correlations (similar to inter-product correlation) significantly improves demand prediction and rebalancing (replenishment) efficiency [cite: 28, 29]. This leads to higher utilization rates (turnover) of the bikes.

### 7.3 Retail and Spare Parts
In spare parts management, where demand is lumpy, using **SVD** for forecasting has been shown to reduce forecasting error better than traditional methods. This allows for lower safety stocks without compromising service, directly improving the turnover of expensive, slow-moving parts [cite: 6]. Additionally, **PCA** has been used to characterize inventory profiles in multi-item/multi-supplier environments, identifying risk profiles that leverage inventory management for improved performance [cite: 5].

## 8. Challenges and Limitations

While theoretically robust, these strategies face practical hurdles:
*   **Computational Complexity:** The "curse of dimensionality" makes calculating optimal policies for many correlated items computationally expensive. While Customer-Item decomposition helps, it is still polynomial in complexity [cite: 8].
*   **Data Quality:** The success of SVD/PCA and EM algorithms depends heavily on the quality of historical data. Non-stationary demand (changing correlations over time) can render static decomposition models obsolete quickly [cite: 8].
*   **Parameter Sensitivity:** The benefits of JRP decrease if the correlation structure is misidentified. Treating negatively correlated items as a JRP group (synchronizing them) could actually *increase* costs by forcing orders when they aren't needed [cite: 12].

## 9. Conclusion

Inventory synchronization strategies can indeed optimize turnover rates, but their success is contingent upon the sophisticated handling of **inter-product demand correlation**. Simple synchronization (JRP) works best for positively correlated items, while risk pooling is the mechanism for negatively correlated items.

**Decomposition** is the mathematical key that unlocks these benefits. **Spectral decomposition (SVD/PCA)** cleans the data and identifies the correlation structure, allowing managers to group items correctly. **Customer-Item decomposition** solves the resulting complex control problems, providing dynamic policies that trim excess safety stock. By integrating these approaches, firms can achieve a state of "lean synchronization," minimizing the Average Inventory denominator while protecting the Sales numerator, thereby maximizing the Inventory Turnover Ratio.

## References

*   **[cite: 9]** Synder. (2023). *Tips for optimizing your inventory turnover rate*.
*   **[cite: 1]** Unisco. *Inventory synchronization techniques*.
*   **[cite: 11]** Ficommerce. (2026). *How to improve your inventory turnover ratio*.
*   **[cite: 8]** ResearchGate. *A Customer-Item Decomposition Approach to Stochastic Inventory Systems with Correlation*.
*   **[cite: 10]** ResearchGate. (2025). *Multivariate Customer Demand Modeling and Estimation from Censored Sales*.
*   **[cite: 3]** Yoksis. *Inventory Performance with Pooling: Evidence from Mergers and Acquisitions*.
*   **[cite: 2]** ResearchGate. (2017). *A systematic literature review on the joint replenishment problem solutions*.
*   **[cite: 12]** ResearchGate. *The Impact of Demand Correlation on Replenishment Policies*.
*   **[cite: 16]** MDPI. (2025). *Singular Spectrum Analysis for Demand Forecasting*.
*   **[cite: 5]** Repositorium UMinho. (2022). *Principal component analysis in inventory management*.
*   **[cite: 6]** IEOM Society. *Forecasting sporadic demand using Principal Component Analysis*.
*   **[cite: 8]** ResearchGate. *A Customer-Item Decomposition Approach*.
*   **[cite: 4]** ResearchGate. *Inventory Performance with Pooling: Evidence from Mergers and Acquisitions*.
*   **[cite: 7]** Statistics By Jim. *Principal Component Analysis*.
*   **[cite: 23]** ResearchGate. (2016). *An expectation-maximization method to estimate a rank-based choice model*.

**Sources:**
1. [unisco.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3rnrSrtlPt32jknr6ccg5MkTzjR6i_iIoclEeOnbnPjBH2AlnBw0JeOiD0-g_WXe2P7TDikNk5b3I1SGHFRrcv8wNJo1O509mh4QZ1PVfCTo3MmrTQzySent6nAbg7m88O07Hg5xEZ6t_cJV6Ew_U8w_luci-uqQr-sHMEajW4Ed3)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGydvlusV4dg47jXl6HPLPrl_LYMZBP1yeDGOtWoi3V16_H5MtFv1Neft_uU8SNFKuvEJN9sRvikveqTAihUb1uHENwfmWA62Dg82KUUIhwyfT_EslMCwDSkDUjYmVZFhKUUe6932b0-ChfgtczlSAr79S0JDX_xrX-XqrXd_q75UCguFruek8x5jxlsZG624sYAu9D-0v2XlX_6Fl5KhNnUTeZCNk7aOtkjpsS3DS4cZHuuQAuvFt_HK7KHZ6DLA==)
3. [bilkent.edu.tr](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGeLjing7mYQQuOe7ojL2Uoa4KakcfWadguuydvyuT2qCP2zXnvwNwV2VX9re6tyZQS0jsITj5CcUR6exve_qn66Hq_TwMMQNzXULrTHLsVVRXgflHYpw8yrSCwBDJhlQoxs7uuXEM-)
4. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRnP30DmE3LDhI-t7aYZB3YAw2PDiKpHOAoRC9mtGK4ViiOjKKc3IjrjWakODaDyq_7BNJ04b4ITDgvzvWxZbzRnxPE16C5iJ3bSe0nU41yeZLnWIPXJkzY56JoErH1LJnVK_zs5p2Bwqq0avLNVhdhhB7X8H41lQOTW6RYtviF3wogclXeAYLYXdYUGomB5DoUIr6z2jkOTV5VkxL3Z2u-bzif7tCKMFUKy-GW9QypdlX)
5. [uminho.pt](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRzcF03wO-emcaXwPbWhaYwF690Nq1lbd-Vts8yLMKuSWXsuk9y2TMue_W4-TcEkya5NlBvZ-Iy3RfSPM1ig8Upr747maMWLqv4OxKs1WnoWYNHMCfmJxyqi_i3-HUkMqZrgwkfcE9wNR0uOI-8GwP1hcvTaeKeJYjqijEE3KUxcfZF15JDDwioixPvlI=)
6. [ieomsociety.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7pYFys9Tc1eEwzO2-yQiSpXptZuDgx88kWRriUtz128n51lkyv3xwjTQXOgqyXUsonyNMKztHMiJHnriYLBXPTB4y06CjuUvFP0okh931srOa5MVURIbjwbq7Jbvpl0qLLpLLbl8OUQ1O0g==)
7. [statisticsbyjim.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFY6RaaTeNJ6yTtDWrKG97eaEbgpCxWAYlktauWQFeolvOMD6R8pp0VyrhDuonLEuGtbG2uQIziPItPoW0BPw-PpeCDLwrt5_2H5LDE6mXnxswCsB8xGDaoEAokhR3vYmm9LkFFpUEVT5l7uyOC920j591kWTKD)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEjqmZ99L2LM-iDBvmHM1MVVp9XSZnbaWKaYOMwIEMBHoNeLU85kFKdmRdwAR91Ll3pg0we83ZjYDKHrOu3XqKlAHXMSlMr7SIxx-zZhtfWZEH8-_i1PQzl5xLFWImYicBcUvkSsEQvyuqPK4sSGGX5A6YlVivXC8lTBnAKlKDuLDfXkTCMOLNeSZLLGnOhMIjqzWPFPxRlXraAITPiHpl85K8wWWCIotJAC9jnfSNClcXpTvMW1dsd5t8l47owAOC)
9. [synder.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHygFnMZmE2OYLdV96LC-ouW-vue31B89pKyibnS5YK_zsGs1fXmE5K-f6tHlxs79TiHf-bO4lf9l_2MMY8EGcUtw41cf0Cnhm1wOA7uBwff-41NXQH95uUGmx9G2_xyWMxrQI7RvQ-2-te5mcOhLBVvKLmTVy6UL1FEPDAbbNq)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYL9KHueawHOJiqsxfA7nbWjEomFpueoEzgIg2SIl-qTYPNo3XDvUvXCLxM08nqy-T-5Tc3hrxK8JDsajCu0rFSzxVVBDiZ-VNzZ19FY_tIQqN5-ZWrw4gj6RNaRQNp-8p3Df6ARZIsSB4gNq7cGVd1m8gfH_kcwpQAIw5n4HsJ_9K1KvRWgMjtyo9G-O6CH-WWYP60dlsryT-qxq3UyfO6-LmxyGGaq88AsfMRMsvY38=)
11. [ficommerce.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4ks3Jf_LePEvfhIvOYN3Y-GxM7WLecQoqDWzLZ9UG5_jKyjxowuPq_TVpKwJ_jw9EUgXq9URVFWJ_NrWOmUeazYmjSffCEsbVkvTohyuU5AxEFqpohQQpI_JeA2kHjEdAHTeV_GV8xwhw0LHMBnseY8IIJERGjofW4TYaxQ==)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqoCxB0BI0Y7BeR2EQKp8Zkyb8BFRbex9RLQC3FbaZp1LFS7F63n1S80NBpNU9Jb-W_ItQn4h9HnKECjXQXaHkITZxZtDkkmSzRibtawrgYo8SJd-OBV5LCdcwJg3FLsR3L7dRLZ48pLv92icqF-afmF2K_11rABGT_auUlbXS_tNoeW4tnyUC00zflpwLpiswDlnXXUkcklOHEVt2hBDtU_rZV_6sufc7zsJ6cAvOkKwTjSaiX3ZGtOhsapQ9ejQLq5QRraYArgtY3ptuHcDLOA2zxG-BDsjLNyiFVru1bYOK4PhXN6jZZCtMaK_HuOoQXg==)
13. [omneelab.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyQcyZBZK5CJg0oC9PXwbJKsc2LUSrz2Ya3W-hPHEstBWIBgKDH9FTwVuU4w16CBG-TdU_tQ_sxa5yfJqYYxPOyJIoyNVYmY7R9Kb7v15xhJpu7ejq1fN5ANHskmTvBJ2OkIHwQsibnoAT1cIXpnlh6uS6gw==)
14. [informs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGluk_qx-QYFyTc0-obkfMeFAHTuvtw-PzeQ_0Ef1Mh9BmVT5-HA0pflHcrqLxC37mVoiBcerXS9AhxlfkQmsoU55j8ozqri9aR1cpqS6J-YCDUtGCY2wkaER8sRsaQjEhi4xMFnkLL9SzU1MoQyxuy)
15. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGySq7qlll6_n-j_nTCGo5t03gqfe3T4J2LQ_O7mdRLW_JdFmuC9dk5nOO6jOno45hk1LOkfOc8lfTErRa15YdQg6xYHR_CiOVIP20VymhhjluLkO3VRnd3rHXSNu-A3C2ldiDG9j_ScCwN7uhtwSo-gcLB)
16. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNVlNhYpDMbN163tH6zlcRAgatLz3Ik-hI9VvCkWf6SUFY6uf_GI5bYEzWD3EOJlHCarREYrbP5V2nUwQxSthn-YDAj79Y41XQJY4TR1SLm4UwAs12X9xNh3NSR7uPnpI=)
17. [lu.se](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGl3lBcYdqU4DtksdCj_DZoeF5Ggssc0r7cGcowJntMOhjmeU6Vh4VIUivk8AjPgEpvN8koA_gmZR_XEJT0McfdXfOh8oGOtUreWNECTbIDH2bGnS_OpK-6oTcJSiauBNec0JQpdpOnpTxwv8t1A_IBKffn0Rnau0B-kw==)
18. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDP95Tqi0DdzcByQzjxzt-ptdlSZmVBeG7X5zdm66wmJJWH5pbfEt2WpA_rjC4Q06fvWFd6yCORKVerwgMqJhjJTuJJx6r3xaj5UAp-93L3jQKiT3r05j-ZRcESPaoGeEKcFnbQjzX)
19. [psecommunity.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYJfaxQkOtO9KtXwDdxCBODo5PlVoKF_jWdIIgRTVr3AMBRPrlQJP6lFj5TtKqXGYlnyjNvfXsFAzxbHhJPbdMa05OPmRSrodlMuQatHBOOUky2HlfOLIxx5QRcu3BM-iJV0ASKH3MQrT3TH_Em7qIZmmpveVuJ_ziAyzCxtsZZdfzKnUYKJ_eX6sElVBIsaee)
20. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaEF36OmwTraoRAl3TGJCdJ7IbWtvdp2u08RnQ47h-k-HCJRbqxcFeBAwEI3V9fXgcg5-a8F-Qj1p1QNYUyP3RK8ydCQDMYEa6aODvo7zxeOBrOWVeeOv2Z-lCuH_dCRpGIMLfyNe8rIYQEDNgLVFBX-gSRor_dT-wq8a5_StAp4Rw2lGceKI5tMzpIkcRZV-rW6PRwTMu3Q==)
21. [d-nb.info](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcF_P9Obs7FE-SnvmFlgKtsFTuZC4r1DjYwxsgbwnjEHIgcM6SnggdbiyBEEqKvR1S3IECNgWlt3Lss8hr6nO4IoALHbABNBdOTo5KW90BIa7YLcfo)
22. [uni-mannheim.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGv4ekVso3zl9oBktGvajR0LUP5HQsUhwI6J0PoKUM-qGdBLF2QEsuHTvkiSfQHTQUI0o8r49mZNweDy0nl7KORpBQ7-maBTE1I4clIL0NVLQ8ReOg44xeC1YqmLc9GAJR_INQt6UeP-iG9tikcQOQptfq-VapOmOMxhYh-RSz7et_h3RTOZxzFk2NOtDBG1KIqZFRx-sfwX-dXdGLA1qJgMXkfXX1UTXk5j4vOTb3hLKIQaHNTD2uLO-k_jXNDAUHEFIaHy-gGHZSmpgzaj7PUtrJgVkLB_9rnT6-SdFj_aIIIUaes6giXTOirk8P88CAZqLvvtZRwiuEgzVWKrsLSsnrm)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFR6r7gf0KdukKnRRpGcA4RRhImljwGUOEHpso3fvmHtGecQKLR7seFOsTRwSXG2yRr6Mlnyo2E-OyMD18YN6i6klPJtOEA-h3wnV2SSVOMdkdrRw0qjJAlDx38gmvq-SG_H7awk74OoH-NTriWjNEdMZ1hhDAHnKohky2jhQg-OlwhgvAhn4uHgIHuAT1CpIaK42cQK8GS7neianfRWSIeoN11-LggaI3b4FoYvhixr5UuKpMb1yldmJ4Y2Q==)
24. [informs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEw0cenJYLbkQY7fx39an6G8N5mM4nKlO3fWzZJ3KNTbRakWRc71804cEatzb0NQAWElTfouvmq2GxaqFWJ01Ma2fS4tCDsPMH67GlZAF8gkGBnMDHuC6_Y5Gn7CBiJ5RDCefbIgmGQVKQ91QipxGI=)
25. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyJBMe5_6WYWlI0Yjl7v2eIMuXRJOo37ZLMM9Gt8X-TxdqXdKd_rgjtYaQNo-mJSkfkkrgA3QNqYPsKID2kXbkLwcUybLzLgeWrOv8ZddcHJZpvHI9dFp307lXE3HJpFn_TobjvO5tBpBKUPFKtdR1kGL5iSx95lzxIwdICTRPRAcNyjs=)
26. [dvunified.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiFZiEJao3563Kch35Kzw0ztbGu237OcAftif_4lOuGUrjIbuuKX36QNhrTyDyxq5VyiPOYrUFI1VYlb_gYKdV-5AWSN-f821Y7ymrK5uL1uzSAvhhnoG6j5yZYjnSdnjXL9VgY5e3lOg=)
27. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwv4OWyDVuU5GBAYrJEtgop2QXXqOFpgnKtcRRtL-nGdwIwdkMNc9U7ouftJz6AiJ3KDkCdFOB-gFGKXIxyByIj5ALWFh0k5wofk2iItoPkFf40yKc4_tOv1PZziB429RuIoZVIBIzlyBJY38D8zJoF8g5)
28. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEICeebk6_ADArjOgTgx99tTg-k1fYuCccMofzDgMEdpgPvDt_-TNOaMm_-PoSqFzAkCq-TKa-YMyX7YfAgu4M0-Wcs5JjUumvJezLwgRTGDipc7qsxVAZlYdlPjRq9R6AaHYFS9wyMyHZ0vBiytdPQx9iEp7XnvV71LupOaWI6dRf-rgQF_z0PiNZrLhZW-S73M62MW21d22j5fHHVGKC6q4mfmdwKuoC1NLOeNzeX3oWgJQk1ZrwlxFmv7poLybNognEYXgdnVW1rKQ==)
29. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOceqbyk48Rkjria_6oslK2Fi7nrbySaU7o0hn6D4e9DLq-_y2tUWqTSKWhioe_QItpVe7FoBL8l53o1b06E4rJYspDOf-Dmsyys4WkGWezSurNAcNhsoxA_-RiD3w-eEekxlxELGtKI0roWogBwxog5oO_jIXmp3ZNZcnSOj5BAT2QuhgvS5o0O_cU9OkdavcwiHnAcDpdmCCAc09VMTvbMdsdA==)


## Annotations
Annotation(end_index=579, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGydvlusV4dg47jXl6HPLPrl_LYMZBP1yeDGOtWoi3V16_H5MtFv1Neft_uU8SNFKuvEJN9sRvikveqTAihUb1uHENwfmWA62Dg82KUUIhwyfT_EslMCwDSkDUjYmVZFhKUUe6932b0-ChfgtczlSAr79S0JDX_xrX-XqrXd_q75UCguFruek8x5jxlsZG624sYAu9D-0v2XlX_6Fl5KhNnUTeZCNk7aOtkjpsS3DS4cZHuuQAuvFt_HK7KHZ6DLA==', start_index=567)
Annotation(end_index=579, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3rnrSrtlPt32jknr6ccg5MkTzjR6i_iIoclEeOnbnPjBH2AlnBw0JeOiD0-g_WXe2P7TDikNk5b3I1SGHFRrcv8wNJo1O509mh4QZ1PVfCTo3MmrTQzySent6nAbg7m88O07Hg5xEZ6t_cJV6Ew_U8w_luci-uqQr-sHMEajW4Ed3', start_index=567)
Annotation(end_index=973, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRnP30DmE3LDhI-t7aYZB3YAw2PDiKpHOAoRC9mtGK4ViiOjKKc3IjrjWakODaDyq_7BNJ04b4ITDgvzvWxZbzRnxPE16C5iJ3bSe0nU41yeZLnWIPXJkzY56JoErH1LJnVK_zs5p2Bwqq0avLNVhdhhB7X8H41lQOTW6RYtviF3wogclXeAYLYXdYUGomB5DoUIr6z2jkOTV5VkxL3Z2u-bzif7tCKMFUKy-GW9QypdlX', start_index=961)
Annotation(end_index=973, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGeLjing7mYQQuOe7ojL2Uoa4KakcfWadguuydvyuT2qCP2zXnvwNwV2VX9re6tyZQS0jsITj5CcUR6exve_qn66Hq_TwMMQNzXULrTHLsVVRXgflHYpw8yrSCwBDJhlQoxs7uuXEM-', start_index=961)
Annotation(end_index=1377, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRzcF03wO-emcaXwPbWhaYwF690Nq1lbd-Vts8yLMKuSWXsuk9y2TMue_W4-TcEkya5NlBvZ-Iy3RfSPM1ig8Upr747maMWLqv4OxKs1WnoWYNHMCfmJxyqi_i3-HUkMqZrgwkfcE9wNR0uOI-8GwP1hcvTaeKeJYjqijEE3KUxcfZF15JDDwioixPvlI=', start_index=1362)
Annotation(end_index=1377, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFY6RaaTeNJ6yTtDWrKG97eaEbgpCxWAYlktauWQFeolvOMD6R8pp0VyrhDuonLEuGtbG2uQIziPItPoW0BPw-PpeCDLwrt5_2H5LDE6mXnxswCsB8xGDaoEAokhR3vYmm9LkFFpUEVT5l7uyOC920j591kWTKD', start_index=1362)
Annotation(end_index=1377, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7pYFys9Tc1eEwzO2-yQiSpXptZuDgx88kWRriUtz128n51lkyv3xwjTQXOgqyXUsonyNMKztHMiJHnriYLBXPTB4y06CjuUvFP0okh931srOa5MVURIbjwbq7Jbvpl0qLLpLLbl8OUQ1O0g==', start_index=1362)
Annotation(end_index=1767, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEjqmZ99L2LM-iDBvmHM1MVVp9XSZnbaWKaYOMwIEMBHoNeLU85kFKdmRdwAR91Ll3pg0we83ZjYDKHrOu3XqKlAHXMSlMr7SIxx-zZhtfWZEH8-_i1PQzl5xLFWImYicBcUvkSsEQvyuqPK4sSGGX5A6YlVivXC8lTBnAKlKDuLDfXkTCMOLNeSZLLGnOhMIjqzWPFPxRlXraAITPiHpl85K8wWWCIotJAC9jnfSNClcXpTvMW1dsd5t8l47owAOC', start_index=1758)
Annotation(end_index=2127, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYL9KHueawHOJiqsxfA7nbWjEomFpueoEzgIg2SIl-qTYPNo3XDvUvXCLxM08nqy-T-5Tc3hrxK8JDsajCu0rFSzxVVBDiZ-VNzZ19FY_tIQqN5-ZWrw4gj6RNaRQNp-8p3Df6ARZIsSB4gNq7cGVd1m8gfH_kcwpQAIw5n4HsJ_9K1KvRWgMjtyo9G-O6CH-WWYP60dlsryT-qxq3UyfO6-LmxyGGaq88AsfMRMsvY38=', start_index=2114)
Annotation(end_index=2127, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHygFnMZmE2OYLdV96LC-ouW-vue31B89pKyibnS5YK_zsGs1fXmE5K-f6tHlxs79TiHf-bO4lf9l_2MMY8EGcUtw41cf0Cnhm1wOA7uBwff-41NXQH95uUGmx9G2_xyWMxrQI7RvQ-2-te5mcOhLBVvKLmTVy6UL1FEPDAbbNq', start_index=2114)
Annotation(end_index=2342, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4ks3Jf_LePEvfhIvOYN3Y-GxM7WLecQoqDWzLZ9UG5_jKyjxowuPq_TVpKwJ_jw9EUgXq9URVFWJ_NrWOmUeazYmjSffCEsbVkvTohyuU5AxEFqpohQQpI_JeA2kHjEdAHTeV_GV8xwhw0LHMBnseY8IIJERGjofW4TYaxQ==', start_index=2329)
Annotation(end_index=2342, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHygFnMZmE2OYLdV96LC-ouW-vue31B89pKyibnS5YK_zsGs1fXmE5K-f6tHlxs79TiHf-bO4lf9l_2MMY8EGcUtw41cf0Cnhm1wOA7uBwff-41NXQH95uUGmx9G2_xyWMxrQI7RvQ-2-te5mcOhLBVvKLmTVy6UL1FEPDAbbNq', start_index=2329)
Annotation(end_index=2848, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqoCxB0BI0Y7BeR2EQKp8Zkyb8BFRbex9RLQC3FbaZp1LFS7F63n1S80NBpNU9Jb-W_ItQn4h9HnKECjXQXaHkITZxZtDkkmSzRibtawrgYo8SJd-OBV5LCdcwJg3FLsR3L7dRLZ48pLv92icqF-afmF2K_11rABGT_auUlbXS_tNoeW4tnyUC00zflpwLpiswDlnXXUkcklOHEVt2hBDtU_rZV_6sufc7zsJ6cAvOkKwTjSaiX3ZGtOhsapQ9ejQLq5QRraYArgtY3ptuHcDLOA2zxG-BDsjLNyiFVru1bYOK4PhXN6jZZCtMaK_HuOoQXg==', start_index=2834)
Annotation(end_index=2848, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYL9KHueawHOJiqsxfA7nbWjEomFpueoEzgIg2SIl-qTYPNo3XDvUvXCLxM08nqy-T-5Tc3hrxK8JDsajCu0rFSzxVVBDiZ-VNzZ19FY_tIQqN5-ZWrw4gj6RNaRQNp-8p3Df6ARZIsSB4gNq7cGVd1m8gfH_kcwpQAIw5n4HsJ_9K1KvRWgMjtyo9G-O6CH-WWYP60dlsryT-qxq3UyfO6-LmxyGGaq88AsfMRMsvY38=', start_index=2834)
Annotation(end_index=3552, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRzcF03wO-emcaXwPbWhaYwF690Nq1lbd-Vts8yLMKuSWXsuk9y2TMue_W4-TcEkya5NlBvZ-Iy3RfSPM1ig8Upr747maMWLqv4OxKs1WnoWYNHMCfmJxyqi_i3-HUkMqZrgwkfcE9wNR0uOI-8GwP1hcvTaeKeJYjqijEE3KUxcfZF15JDDwioixPvlI=', start_index=3540)
Annotation(end_index=3552, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEjqmZ99L2LM-iDBvmHM1MVVp9XSZnbaWKaYOMwIEMBHoNeLU85kFKdmRdwAR91Ll3pg0we83ZjYDKHrOu3XqKlAHXMSlMr7SIxx-zZhtfWZEH8-_i1PQzl5xLFWImYicBcUvkSsEQvyuqPK4sSGGX5A6YlVivXC8lTBnAKlKDuLDfXkTCMOLNeSZLLGnOhMIjqzWPFPxRlXraAITPiHpl85K8wWWCIotJAC9jnfSNClcXpTvMW1dsd5t8l47owAOC', start_index=3540)
Annotation(end_index=4434, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyQcyZBZK5CJg0oC9PXwbJKsc2LUSrz2Ya3W-hPHEstBWIBgKDH9FTwVuU4w16CBG-TdU_tQ_sxa5yfJqYYxPOyJIoyNVYmY7R9Kb7v15xhJpu7ejq1fN5ANHskmTvBJ2OkIHwQsibnoAT1cIXpnlh6uS6gw==', start_index=4421)
Annotation(end_index=4434, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHygFnMZmE2OYLdV96LC-ouW-vue31B89pKyibnS5YK_zsGs1fXmE5K-f6tHlxs79TiHf-bO4lf9l_2MMY8EGcUtw41cf0Cnhm1wOA7uBwff-41NXQH95uUGmx9G2_xyWMxrQI7RvQ-2-te5mcOhLBVvKLmTVy6UL1FEPDAbbNq', start_index=4421)
Annotation(end_index=5037, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4ks3Jf_LePEvfhIvOYN3Y-GxM7WLecQoqDWzLZ9UG5_jKyjxowuPq_TVpKwJ_jw9EUgXq9URVFWJ_NrWOmUeazYmjSffCEsbVkvTohyuU5AxEFqpohQQpI_JeA2kHjEdAHTeV_GV8xwhw0LHMBnseY8IIJERGjofW4TYaxQ==', start_index=5024)
Annotation(end_index=5037, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGydvlusV4dg47jXl6HPLPrl_LYMZBP1yeDGOtWoi3V16_H5MtFv1Neft_uU8SNFKuvEJN9sRvikveqTAihUb1uHENwfmWA62Dg82KUUIhwyfT_EslMCwDSkDUjYmVZFhKUUe6932b0-ChfgtczlSAr79S0JDX_xrX-XqrXd_q75UCguFruek8x5jxlsZG624sYAu9D-0v2XlX_6Fl5KhNnUTeZCNk7aOtkjpsS3DS4cZHuuQAuvFt_HK7KHZ6DLA==', start_index=5024)
Annotation(end_index=5508, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGydvlusV4dg47jXl6HPLPrl_LYMZBP1yeDGOtWoi3V16_H5MtFv1Neft_uU8SNFKuvEJN9sRvikveqTAihUb1uHENwfmWA62Dg82KUUIhwyfT_EslMCwDSkDUjYmVZFhKUUe6932b0-ChfgtczlSAr79S0JDX_xrX-XqrXd_q75UCguFruek8x5jxlsZG624sYAu9D-0v2XlX_6Fl5KhNnUTeZCNk7aOtkjpsS3DS4cZHuuQAuvFt_HK7KHZ6DLA==', start_index=5499)
Annotation(end_index=5733, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGydvlusV4dg47jXl6HPLPrl_LYMZBP1yeDGOtWoi3V16_H5MtFv1Neft_uU8SNFKuvEJN9sRvikveqTAihUb1uHENwfmWA62Dg82KUUIhwyfT_EslMCwDSkDUjYmVZFhKUUe6932b0-ChfgtczlSAr79S0JDX_xrX-XqrXd_q75UCguFruek8x5jxlsZG624sYAu9D-0v2XlX_6Fl5KhNnUTeZCNk7aOtkjpsS3DS4cZHuuQAuvFt_HK7KHZ6DLA==', start_index=5724)
Annotation(end_index=6107, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGluk_qx-QYFyTc0-obkfMeFAHTuvtw-PzeQ_0Ef1Mh9BmVT5-HA0pflHcrqLxC37mVoiBcerXS9AhxlfkQmsoU55j8ozqri9aR1cpqS6J-YCDUtGCY2wkaER8sRsaQjEhi4xMFnkLL9SzU1MoQyxuy', start_index=6094)
Annotation(end_index=6107, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGydvlusV4dg47jXl6HPLPrl_LYMZBP1yeDGOtWoi3V16_H5MtFv1Neft_uU8SNFKuvEJN9sRvikveqTAihUb1uHENwfmWA62Dg82KUUIhwyfT_EslMCwDSkDUjYmVZFhKUUe6932b0-ChfgtczlSAr79S0JDX_xrX-XqrXd_q75UCguFruek8x5jxlsZG624sYAu9D-0v2XlX_6Fl5KhNnUTeZCNk7aOtkjpsS3DS4cZHuuQAuvFt_HK7KHZ6DLA==', start_index=6094)
Annotation(end_index=6370, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqoCxB0BI0Y7BeR2EQKp8Zkyb8BFRbex9RLQC3FbaZp1LFS7F63n1S80NBpNU9Jb-W_ItQn4h9HnKECjXQXaHkITZxZtDkkmSzRibtawrgYo8SJd-OBV5LCdcwJg3FLsR3L7dRLZ48pLv92icqF-afmF2K_11rABGT_auUlbXS_tNoeW4tnyUC00zflpwLpiswDlnXXUkcklOHEVt2hBDtU_rZV_6sufc7zsJ6cAvOkKwTjSaiX3ZGtOhsapQ9ejQLq5QRraYArgtY3ptuHcDLOA2zxG-BDsjLNyiFVru1bYOK4PhXN6jZZCtMaK_HuOoQXg==', start_index=6360)
Annotation(end_index=6656, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRnP30DmE3LDhI-t7aYZB3YAw2PDiKpHOAoRC9mtGK4ViiOjKKc3IjrjWakODaDyq_7BNJ04b4ITDgvzvWxZbzRnxPE16C5iJ3bSe0nU41yeZLnWIPXJkzY56JoErH1LJnVK_zs5p2Bwqq0avLNVhdhhB7X8H41lQOTW6RYtviF3wogclXeAYLYXdYUGomB5DoUIr6z2jkOTV5VkxL3Z2u-bzif7tCKMFUKy-GW9QypdlX', start_index=6643)
Annotation(end_index=6656, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYL9KHueawHOJiqsxfA7nbWjEomFpueoEzgIg2SIl-qTYPNo3XDvUvXCLxM08nqy-T-5Tc3hrxK8JDsajCu0rFSzxVVBDiZ-VNzZ19FY_tIQqN5-ZWrw4gj6RNaRQNp-8p3Df6ARZIsSB4gNq7cGVd1m8gfH_kcwpQAIw5n4HsJ_9K1KvRWgMjtyo9G-O6CH-WWYP60dlsryT-qxq3UyfO6-LmxyGGaq88AsfMRMsvY38=', start_index=6643)
Annotation(end_index=7738, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGeLjing7mYQQuOe7ojL2Uoa4KakcfWadguuydvyuT2qCP2zXnvwNwV2VX9re6tyZQS0jsITj5CcUR6exve_qn66Hq_TwMMQNzXULrTHLsVVRXgflHYpw8yrSCwBDJhlQoxs7uuXEM-', start_index=7729)
Annotation(end_index=8059, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRnP30DmE3LDhI-t7aYZB3YAw2PDiKpHOAoRC9mtGK4ViiOjKKc3IjrjWakODaDyq_7BNJ04b4ITDgvzvWxZbzRnxPE16C5iJ3bSe0nU41yeZLnWIPXJkzY56JoErH1LJnVK_zs5p2Bwqq0avLNVhdhhB7X8H41lQOTW6RYtviF3wogclXeAYLYXdYUGomB5DoUIr6z2jkOTV5VkxL3Z2u-bzif7tCKMFUKy-GW9QypdlX', start_index=8046)
Annotation(end_index=8059, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGySq7qlll6_n-j_nTCGo5t03gqfe3T4J2LQ_O7mdRLW_JdFmuC9dk5nOO6jOno45hk1LOkfOc8lfTErRa15YdQg6xYHR_CiOVIP20VymhhjluLkO3VRnd3rHXSNu-A3C2ldiDG9j_ScCwN7uhtwSo-gcLB', start_index=8046)
Annotation(end_index=8323, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRnP30DmE3LDhI-t7aYZB3YAw2PDiKpHOAoRC9mtGK4ViiOjKKc3IjrjWakODaDyq_7BNJ04b4ITDgvzvWxZbzRnxPE16C5iJ3bSe0nU41yeZLnWIPXJkzY56JoErH1LJnVK_zs5p2Bwqq0avLNVhdhhB7X8H41lQOTW6RYtviF3wogclXeAYLYXdYUGomB5DoUIr6z2jkOTV5VkxL3Z2u-bzif7tCKMFUKy-GW9QypdlX', start_index=8311)
Annotation(end_index=8323, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGeLjing7mYQQuOe7ojL2Uoa4KakcfWadguuydvyuT2qCP2zXnvwNwV2VX9re6tyZQS0jsITj5CcUR6exve_qn66Hq_TwMMQNzXULrTHLsVVRXgflHYpw8yrSCwBDJhlQoxs7uuXEM-', start_index=8311)
Annotation(end_index=8902, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRzcF03wO-emcaXwPbWhaYwF690Nq1lbd-Vts8yLMKuSWXsuk9y2TMue_W4-TcEkya5NlBvZ-Iy3RfSPM1ig8Upr747maMWLqv4OxKs1WnoWYNHMCfmJxyqi_i3-HUkMqZrgwkfcE9wNR0uOI-8GwP1hcvTaeKeJYjqijEE3KUxcfZF15JDDwioixPvlI=', start_index=8890)
Annotation(end_index=8902, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFY6RaaTeNJ6yTtDWrKG97eaEbgpCxWAYlktauWQFeolvOMD6R8pp0VyrhDuonLEuGtbG2uQIziPItPoW0BPw-PpeCDLwrt5_2H5LDE6mXnxswCsB8xGDaoEAokhR3vYmm9LkFFpUEVT5l7uyOC920j591kWTKD', start_index=8890)
Annotation(end_index=9556, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNVlNhYpDMbN163tH6zlcRAgatLz3Ik-hI9VvCkWf6SUFY6uf_GI5bYEzWD3EOJlHCarREYrbP5V2nUwQxSthn-YDAj79Y41XQJY4TR1SLm4UwAs12X9xNh3NSR7uPnpI=', start_index=9542)
Annotation(end_index=9556, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGl3lBcYdqU4DtksdCj_DZoeF5Ggssc0r7cGcowJntMOhjmeU6Vh4VIUivk8AjPgEpvN8koA_gmZR_XEJT0McfdXfOh8oGOtUreWNECTbIDH2bGnS_OpK-6oTcJSiauBNec0JQpdpOnpTxwv8t1A_IBKffn0Rnau0B-kw==', start_index=9542)
Annotation(end_index=9717, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDP95Tqi0DdzcByQzjxzt-ptdlSZmVBeG7X5zdm66wmJJWH5pbfEt2WpA_rjC4Q06fvWFd6yCORKVerwgMqJhjJTuJJx6r3xaj5UAp-93L3jQKiT3r05j-ZRcESPaoGeEKcFnbQjzX', start_index=9707)
Annotation(end_index=10166, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYJfaxQkOtO9KtXwDdxCBODo5PlVoKF_jWdIIgRTVr3AMBRPrlQJP6lFj5TtKqXGYlnyjNvfXsFAzxbHhJPbdMa05OPmRSrodlMuQatHBOOUky2HlfOLIxx5QRcu3BM-iJV0ASKH3MQrT3TH_Em7qIZmmpveVuJ_ziAyzCxtsZZdfzKnUYKJ_eX6sElVBIsaee', start_index=10153)
Annotation(end_index=10166, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRzcF03wO-emcaXwPbWhaYwF690Nq1lbd-Vts8yLMKuSWXsuk9y2TMue_W4-TcEkya5NlBvZ-Iy3RfSPM1ig8Upr747maMWLqv4OxKs1WnoWYNHMCfmJxyqi_i3-HUkMqZrgwkfcE9wNR0uOI-8GwP1hcvTaeKeJYjqijEE3KUxcfZF15JDDwioixPvlI=', start_index=10153)
Annotation(end_index=10515, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaEF36OmwTraoRAl3TGJCdJ7IbWtvdp2u08RnQ47h-k-HCJRbqxcFeBAwEI3V9fXgcg5-a8F-Qj1p1QNYUyP3RK8ydCQDMYEa6aODvo7zxeOBrOWVeeOv2Z-lCuH_dCRpGIMLfyNe8rIYQEDNgLVFBX-gSRor_dT-wq8a5_StAp4Rw2lGceKI5tMzpIkcRZV-rW6PRwTMu3Q==', start_index=10502)
Annotation(end_index=10515, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7pYFys9Tc1eEwzO2-yQiSpXptZuDgx88kWRriUtz128n51lkyv3xwjTQXOgqyXUsonyNMKztHMiJHnriYLBXPTB4y06CjuUvFP0okh931srOa5MVURIbjwbq7Jbvpl0qLLpLLbl8OUQ1O0g==', start_index=10502)
Annotation(end_index=10774, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEjqmZ99L2LM-iDBvmHM1MVVp9XSZnbaWKaYOMwIEMBHoNeLU85kFKdmRdwAR91Ll3pg0we83ZjYDKHrOu3XqKlAHXMSlMr7SIxx-zZhtfWZEH8-_i1PQzl5xLFWImYicBcUvkSsEQvyuqPK4sSGGX5A6YlVivXC8lTBnAKlKDuLDfXkTCMOLNeSZLLGnOhMIjqzWPFPxRlXraAITPiHpl85K8wWWCIotJAC9jnfSNClcXpTvMW1dsd5t8l47owAOC', start_index=10765)
Annotation(end_index=11391, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEjqmZ99L2LM-iDBvmHM1MVVp9XSZnbaWKaYOMwIEMBHoNeLU85kFKdmRdwAR91Ll3pg0we83ZjYDKHrOu3XqKlAHXMSlMr7SIxx-zZhtfWZEH8-_i1PQzl5xLFWImYicBcUvkSsEQvyuqPK4sSGGX5A6YlVivXC8lTBnAKlKDuLDfXkTCMOLNeSZLLGnOhMIjqzWPFPxRlXraAITPiHpl85K8wWWCIotJAC9jnfSNClcXpTvMW1dsd5t8l47owAOC', start_index=11378)
Annotation(end_index=11391, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcF_P9Obs7FE-SnvmFlgKtsFTuZC4r1DjYwxsgbwnjEHIgcM6SnggdbiyBEEqKvR1S3IECNgWlt3Lss8hr6nO4IoALHbABNBdOTo5KW90BIa7YLcfo', start_index=11378)
Annotation(end_index=11806, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGv4ekVso3zl9oBktGvajR0LUP5HQsUhwI6J0PoKUM-qGdBLF2QEsuHTvkiSfQHTQUI0o8r49mZNweDy0nl7KORpBQ7-maBTE1I4clIL0NVLQ8ReOg44xeC1YqmLc9GAJR_INQt6UeP-iG9tikcQOQptfq-VapOmOMxhYh-RSz7et_h3RTOZxzFk2NOtDBG1KIqZFRx-sfwX-dXdGLA1qJgMXkfXX1UTXk5j4vOTb3hLKIQaHNTD2uLO-k_jXNDAUHEFIaHy-gGHZSmpgzaj7PUtrJgVkLB_9rnT6-SdFj_aIIIUaes6giXTOirk8P88CAZqLvvtZRwiuEgzVWKrsLSsnrm', start_index=11793)
Annotation(end_index=11806, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEjqmZ99L2LM-iDBvmHM1MVVp9XSZnbaWKaYOMwIEMBHoNeLU85kFKdmRdwAR91Ll3pg0we83ZjYDKHrOu3XqKlAHXMSlMr7SIxx-zZhtfWZEH8-_i1PQzl5xLFWImYicBcUvkSsEQvyuqPK4sSGGX5A6YlVivXC8lTBnAKlKDuLDfXkTCMOLNeSZLLGnOhMIjqzWPFPxRlXraAITPiHpl85K8wWWCIotJAC9jnfSNClcXpTvMW1dsd5t8l47owAOC', start_index=11793)
Annotation(end_index=12358, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFR6r7gf0KdukKnRRpGcA4RRhImljwGUOEHpso3fvmHtGecQKLR7seFOsTRwSXG2yRr6Mlnyo2E-OyMD18YN6i6klPJtOEA-h3wnV2SSVOMdkdrRw0qjJAlDx38gmvq-SG_H7awk74OoH-NTriWjNEdMZ1hhDAHnKohky2jhQg-OlwhgvAhn4uHgIHuAT1CpIaK42cQK8GS7neianfRWSIeoN11-LggaI3b4FoYvhixr5UuKpMb1yldmJ4Y2Q==', start_index=12344)
Annotation(end_index=12358, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYL9KHueawHOJiqsxfA7nbWjEomFpueoEzgIg2SIl-qTYPNo3XDvUvXCLxM08nqy-T-5Tc3hrxK8JDsajCu0rFSzxVVBDiZ-VNzZ19FY_tIQqN5-ZWrw4gj6RNaRQNp-8p3Df6ARZIsSB4gNq7cGVd1m8gfH_kcwpQAIw5n4HsJ_9K1KvRWgMjtyo9G-O6CH-WWYP60dlsryT-qxq3UyfO6-LmxyGGaq88AsfMRMsvY38=', start_index=12344)
Annotation(end_index=12720, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEw0cenJYLbkQY7fx39an6G8N5mM4nKlO3fWzZJ3KNTbRakWRc71804cEatzb0NQAWElTfouvmq2GxaqFWJ01Ma2fS4tCDsPMH67GlZAF8gkGBnMDHuC6_Y5Gn7CBiJ5RDCefbIgmGQVKQ91QipxGI=', start_index=12706)
Annotation(end_index=12720, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYL9KHueawHOJiqsxfA7nbWjEomFpueoEzgIg2SIl-qTYPNo3XDvUvXCLxM08nqy-T-5Tc3hrxK8JDsajCu0rFSzxVVBDiZ-VNzZ19FY_tIQqN5-ZWrw4gj6RNaRQNp-8p3Df6ARZIsSB4gNq7cGVd1m8gfH_kcwpQAIw5n4HsJ_9K1KvRWgMjtyo9G-O6CH-WWYP60dlsryT-qxq3UyfO6-LmxyGGaq88AsfMRMsvY38=', start_index=12706)
Annotation(end_index=13094, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyJBMe5_6WYWlI0Yjl7v2eIMuXRJOo37ZLMM9Gt8X-TxdqXdKd_rgjtYaQNo-mJSkfkkrgA3QNqYPsKID2kXbkLwcUybLzLgeWrOv8ZddcHJZpvHI9dFp307lXE3HJpFn_TobjvO5tBpBKUPFKtdR1kGL5iSx95lzxIwdICTRPRAcNyjs=', start_index=13084)
Annotation(end_index=13604, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiFZiEJao3563Kch35Kzw0ztbGu237OcAftif_4lOuGUrjIbuuKX36QNhrTyDyxq5VyiPOYrUFI1VYlb_gYKdV-5AWSN-f821Y7ymrK5uL1uzSAvhhnoG6j5yZYjnSdnjXL9VgY5e3lOg=', start_index=13590)
Annotation(end_index=13604, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqoCxB0BI0Y7BeR2EQKp8Zkyb8BFRbex9RLQC3FbaZp1LFS7F63n1S80NBpNU9Jb-W_ItQn4h9HnKECjXQXaHkITZxZtDkkmSzRibtawrgYo8SJd-OBV5LCdcwJg3FLsR3L7dRLZ48pLv92icqF-afmF2K_11rABGT_auUlbXS_tNoeW4tnyUC00zflpwLpiswDlnXXUkcklOHEVt2hBDtU_rZV_6sufc7zsJ6cAvOkKwTjSaiX3ZGtOhsapQ9ejQLq5QRraYArgtY3ptuHcDLOA2zxG-BDsjLNyiFVru1bYOK4PhXN6jZZCtMaK_HuOoQXg==', start_index=13590)
Annotation(end_index=14240, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRnP30DmE3LDhI-t7aYZB3YAw2PDiKpHOAoRC9mtGK4ViiOjKKc3IjrjWakODaDyq_7BNJ04b4ITDgvzvWxZbzRnxPE16C5iJ3bSe0nU41yeZLnWIPXJkzY56JoErH1LJnVK_zs5p2Bwqq0avLNVhdhhB7X8H41lQOTW6RYtviF3wogclXeAYLYXdYUGomB5DoUIr6z2jkOTV5VkxL3Z2u-bzif7tCKMFUKy-GW9QypdlX', start_index=14228)
Annotation(end_index=14240, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGeLjing7mYQQuOe7ojL2Uoa4KakcfWadguuydvyuT2qCP2zXnvwNwV2VX9re6tyZQS0jsITj5CcUR6exve_qn66Hq_TwMMQNzXULrTHLsVVRXgflHYpw8yrSCwBDJhlQoxs7uuXEM-', start_index=14228)
Annotation(end_index=14721, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwv4OWyDVuU5GBAYrJEtgop2QXXqOFpgnKtcRRtL-nGdwIwdkMNc9U7ouftJz6AiJ3KDkCdFOB-gFGKXIxyByIj5ALWFh0k5wofk2iItoPkFf40yKc4_tOv1PZziB429RuIoZVIBIzlyBJY38D8zJoF8g5', start_index=14708)
Annotation(end_index=14721, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEjqmZ99L2LM-iDBvmHM1MVVp9XSZnbaWKaYOMwIEMBHoNeLU85kFKdmRdwAR91Ll3pg0we83ZjYDKHrOu3XqKlAHXMSlMr7SIxx-zZhtfWZEH8-_i1PQzl5xLFWImYicBcUvkSsEQvyuqPK4sSGGX5A6YlVivXC8lTBnAKlKDuLDfXkTCMOLNeSZLLGnOhMIjqzWPFPxRlXraAITPiHpl85K8wWWCIotJAC9jnfSNClcXpTvMW1dsd5t8l47owAOC', start_index=14708)
Annotation(end_index=14875, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwv4OWyDVuU5GBAYrJEtgop2QXXqOFpgnKtcRRtL-nGdwIwdkMNc9U7ouftJz6AiJ3KDkCdFOB-gFGKXIxyByIj5ALWFh0k5wofk2iItoPkFf40yKc4_tOv1PZziB429RuIoZVIBIzlyBJY38D8zJoF8g5', start_index=14865)
Annotation(end_index=15242, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFR6r7gf0KdukKnRRpGcA4RRhImljwGUOEHpso3fvmHtGecQKLR7seFOsTRwSXG2yRr6Mlnyo2E-OyMD18YN6i6klPJtOEA-h3wnV2SSVOMdkdrRw0qjJAlDx38gmvq-SG_H7awk74OoH-NTriWjNEdMZ1hhDAHnKohky2jhQg-OlwhgvAhn4uHgIHuAT1CpIaK42cQK8GS7neianfRWSIeoN11-LggaI3b4FoYvhixr5UuKpMb1yldmJ4Y2Q==', start_index=15228)
Annotation(end_index=15242, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYL9KHueawHOJiqsxfA7nbWjEomFpueoEzgIg2SIl-qTYPNo3XDvUvXCLxM08nqy-T-5Tc3hrxK8JDsajCu0rFSzxVVBDiZ-VNzZ19FY_tIQqN5-ZWrw4gj6RNaRQNp-8p3Df6ARZIsSB4gNq7cGVd1m8gfH_kcwpQAIw5n4HsJ_9K1KvRWgMjtyo9G-O6CH-WWYP60dlsryT-qxq3UyfO6-LmxyGGaq88AsfMRMsvY38=', start_index=15228)
Annotation(end_index=15408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRzcF03wO-emcaXwPbWhaYwF690Nq1lbd-Vts8yLMKuSWXsuk9y2TMue_W4-TcEkya5NlBvZ-Iy3RfSPM1ig8Upr747maMWLqv4OxKs1WnoWYNHMCfmJxyqi_i3-HUkMqZrgwkfcE9wNR0uOI-8GwP1hcvTaeKeJYjqijEE3KUxcfZF15JDDwioixPvlI=', start_index=15396)
Annotation(end_index=15408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFY6RaaTeNJ6yTtDWrKG97eaEbgpCxWAYlktauWQFeolvOMD6R8pp0VyrhDuonLEuGtbG2uQIziPItPoW0BPw-PpeCDLwrt5_2H5LDE6mXnxswCsB8xGDaoEAokhR3vYmm9LkFFpUEVT5l7uyOC920j591kWTKD', start_index=15396)
Annotation(end_index=15518, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNVlNhYpDMbN163tH6zlcRAgatLz3Ik-hI9VvCkWf6SUFY6uf_GI5bYEzWD3EOJlHCarREYrbP5V2nUwQxSthn-YDAj79Y41XQJY4TR1SLm4UwAs12X9xNh3NSR7uPnpI=', start_index=15508)
Annotation(end_index=15701, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYJfaxQkOtO9KtXwDdxCBODo5PlVoKF_jWdIIgRTVr3AMBRPrlQJP6lFj5TtKqXGYlnyjNvfXsFAzxbHhJPbdMa05OPmRSrodlMuQatHBOOUky2HlfOLIxx5QRcu3BM-iJV0ASKH3MQrT3TH_Em7qIZmmpveVuJ_ziAyzCxtsZZdfzKnUYKJ_eX6sElVBIsaee', start_index=15687)
Annotation(end_index=15701, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyJBMe5_6WYWlI0Yjl7v2eIMuXRJOo37ZLMM9Gt8X-TxdqXdKd_rgjtYaQNo-mJSkfkkrgA3QNqYPsKID2kXbkLwcUybLzLgeWrOv8ZddcHJZpvHI9dFp307lXE3HJpFn_TobjvO5tBpBKUPFKtdR1kGL5iSx95lzxIwdICTRPRAcNyjs=', start_index=15687)
Annotation(end_index=15787, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGeLjing7mYQQuOe7ojL2Uoa4KakcfWadguuydvyuT2qCP2zXnvwNwV2VX9re6tyZQS0jsITj5CcUR6exve_qn66Hq_TwMMQNzXULrTHLsVVRXgflHYpw8yrSCwBDJhlQoxs7uuXEM-', start_index=15778)
Annotation(end_index=15983, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEjqmZ99L2LM-iDBvmHM1MVVp9XSZnbaWKaYOMwIEMBHoNeLU85kFKdmRdwAR91Ll3pg0we83ZjYDKHrOu3XqKlAHXMSlMr7SIxx-zZhtfWZEH8-_i1PQzl5xLFWImYicBcUvkSsEQvyuqPK4sSGGX5A6YlVivXC8lTBnAKlKDuLDfXkTCMOLNeSZLLGnOhMIjqzWPFPxRlXraAITPiHpl85K8wWWCIotJAC9jnfSNClcXpTvMW1dsd5t8l47owAOC', start_index=15974)
Annotation(end_index=16285, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4ks3Jf_LePEvfhIvOYN3Y-GxM7WLecQoqDWzLZ9UG5_jKyjxowuPq_TVpKwJ_jw9EUgXq9URVFWJ_NrWOmUeazYmjSffCEsbVkvTohyuU5AxEFqpohQQpI_JeA2kHjEdAHTeV_GV8xwhw0LHMBnseY8IIJERGjofW4TYaxQ==', start_index=16272)
Annotation(end_index=16285, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHygFnMZmE2OYLdV96LC-ouW-vue31B89pKyibnS5YK_zsGs1fXmE5K-f6tHlxs79TiHf-bO4lf9l_2MMY8EGcUtw41cf0Cnhm1wOA7uBwff-41NXQH95uUGmx9G2_xyWMxrQI7RvQ-2-te5mcOhLBVvKLmTVy6UL1FEPDAbbNq', start_index=16272)
Annotation(end_index=16756, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRnP30DmE3LDhI-t7aYZB3YAw2PDiKpHOAoRC9mtGK4ViiOjKKc3IjrjWakODaDyq_7BNJ04b4ITDgvzvWxZbzRnxPE16C5iJ3bSe0nU41yeZLnWIPXJkzY56JoErH1LJnVK_zs5p2Bwqq0avLNVhdhhB7X8H41lQOTW6RYtviF3wogclXeAYLYXdYUGomB5DoUIr6z2jkOTV5VkxL3Z2u-bzif7tCKMFUKy-GW9QypdlX', start_index=16744)
Annotation(end_index=16756, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGeLjing7mYQQuOe7ojL2Uoa4KakcfWadguuydvyuT2qCP2zXnvwNwV2VX9re6tyZQS0jsITj5CcUR6exve_qn66Hq_TwMMQNzXULrTHLsVVRXgflHYpw8yrSCwBDJhlQoxs7uuXEM-', start_index=16744)
Annotation(end_index=17386, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEICeebk6_ADArjOgTgx99tTg-k1fYuCccMofzDgMEdpgPvDt_-TNOaMm_-PoSqFzAkCq-TKa-YMyX7YfAgu4M0-Wcs5JjUumvJezLwgRTGDipc7qsxVAZlYdlPjRq9R6AaHYFS9wyMyHZ0vBiytdPQx9iEp7XnvV71LupOaWI6dRf-rgQF_z0PiNZrLhZW-S73M62MW21d22j5fHHVGKC6q4mfmdwKuoC1NLOeNzeX3oWgJQk1ZrwlxFmv7poLybNognEYXgdnVW1rKQ==', start_index=17372)
Annotation(end_index=17386, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOceqbyk48Rkjria_6oslK2Fi7nrbySaU7o0hn6D4e9DLq-_y2tUWqTSKWhioe_QItpVe7FoBL8l53o1b06E4rJYspDOf-Dmsyys4WkGWezSurNAcNhsoxA_-RiD3w-eEekxlxELGtKI0roWogBwxog5oO_jIXmp3ZNZcnSOj5BAT2QuhgvS5o0O_cU9OkdavcwiHnAcDpdmCCAc09VMTvbMdsdA==', start_index=17372)
Annotation(end_index=17779, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7pYFys9Tc1eEwzO2-yQiSpXptZuDgx88kWRriUtz128n51lkyv3xwjTQXOgqyXUsonyNMKztHMiJHnriYLBXPTB4y06CjuUvFP0okh931srOa5MVURIbjwbq7Jbvpl0qLLpLLbl8OUQ1O0g==', start_index=17770)
Annotation(end_index=17990, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRzcF03wO-emcaXwPbWhaYwF690Nq1lbd-Vts8yLMKuSWXsuk9y2TMue_W4-TcEkya5NlBvZ-Iy3RfSPM1ig8Upr747maMWLqv4OxKs1WnoWYNHMCfmJxyqi_i3-HUkMqZrgwkfcE9wNR0uOI-8GwP1hcvTaeKeJYjqijEE3KUxcfZF15JDDwioixPvlI=', start_index=17981)
Annotation(end_index=18335, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEjqmZ99L2LM-iDBvmHM1MVVp9XSZnbaWKaYOMwIEMBHoNeLU85kFKdmRdwAR91Ll3pg0we83ZjYDKHrOu3XqKlAHXMSlMr7SIxx-zZhtfWZEH8-_i1PQzl5xLFWImYicBcUvkSsEQvyuqPK4sSGGX5A6YlVivXC8lTBnAKlKDuLDfXkTCMOLNeSZLLGnOhMIjqzWPFPxRlXraAITPiHpl85K8wWWCIotJAC9jnfSNClcXpTvMW1dsd5t8l47owAOC', start_index=18326)
Annotation(end_index=18572, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEjqmZ99L2LM-iDBvmHM1MVVp9XSZnbaWKaYOMwIEMBHoNeLU85kFKdmRdwAR91Ll3pg0we83ZjYDKHrOu3XqKlAHXMSlMr7SIxx-zZhtfWZEH8-_i1PQzl5xLFWImYicBcUvkSsEQvyuqPK4sSGGX5A6YlVivXC8lTBnAKlKDuLDfXkTCMOLNeSZLLGnOhMIjqzWPFPxRlXraAITPiHpl85K8wWWCIotJAC9jnfSNClcXpTvMW1dsd5t8l47owAOC', start_index=18563)
Annotation(end_index=18838, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqoCxB0BI0Y7BeR2EQKp8Zkyb8BFRbex9RLQC3FbaZp1LFS7F63n1S80NBpNU9Jb-W_ItQn4h9HnKECjXQXaHkITZxZtDkkmSzRibtawrgYo8SJd-OBV5LCdcwJg3FLsR3L7dRLZ48pLv92icqF-afmF2K_11rABGT_auUlbXS_tNoeW4tnyUC00zflpwLpiswDlnXXUkcklOHEVt2hBDtU_rZV_6sufc7zsJ6cAvOkKwTjSaiX3ZGtOhsapQ9ejQLq5QRraYArgtY3ptuHcDLOA2zxG-BDsjLNyiFVru1bYOK4PhXN6jZZCtMaK_HuOoQXg==', start_index=18828)
Annotation(end_index=19776, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHygFnMZmE2OYLdV96LC-ouW-vue31B89pKyibnS5YK_zsGs1fXmE5K-f6tHlxs79TiHf-bO4lf9l_2MMY8EGcUtw41cf0Cnhm1wOA7uBwff-41NXQH95uUGmx9G2_xyWMxrQI7RvQ-2-te5mcOhLBVvKLmTVy6UL1FEPDAbbNq', start_index=19767)
Annotation(end_index=19862, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3rnrSrtlPt32jknr6ccg5MkTzjR6i_iIoclEeOnbnPjBH2AlnBw0JeOiD0-g_WXe2P7TDikNk5b3I1SGHFRrcv8wNJo1O509mh4QZ1PVfCTo3MmrTQzySent6nAbg7m88O07Hg5xEZ6t_cJV6Ew_U8w_luci-uqQr-sHMEajW4Ed3', start_index=19853)
Annotation(end_index=19929, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4ks3Jf_LePEvfhIvOYN3Y-GxM7WLecQoqDWzLZ9UG5_jKyjxowuPq_TVpKwJ_jw9EUgXq9URVFWJ_NrWOmUeazYmjSffCEsbVkvTohyuU5AxEFqpohQQpI_JeA2kHjEdAHTeV_GV8xwhw0LHMBnseY8IIJERGjofW4TYaxQ==', start_index=19919)
Annotation(end_index=20015, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEjqmZ99L2LM-iDBvmHM1MVVp9XSZnbaWKaYOMwIEMBHoNeLU85kFKdmRdwAR91Ll3pg0we83ZjYDKHrOu3XqKlAHXMSlMr7SIxx-zZhtfWZEH8-_i1PQzl5xLFWImYicBcUvkSsEQvyuqPK4sSGGX5A6YlVivXC8lTBnAKlKDuLDfXkTCMOLNeSZLLGnOhMIjqzWPFPxRlXraAITPiHpl85K8wWWCIotJAC9jnfSNClcXpTvMW1dsd5t8l47owAOC', start_index=20006)
Annotation(end_index=20139, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYL9KHueawHOJiqsxfA7nbWjEomFpueoEzgIg2SIl-qTYPNo3XDvUvXCLxM08nqy-T-5Tc3hrxK8JDsajCu0rFSzxVVBDiZ-VNzZ19FY_tIQqN5-ZWrw4gj6RNaRQNp-8p3Df6ARZIsSB4gNq7cGVd1m8gfH_kcwpQAIw5n4HsJ_9K1KvRWgMjtyo9G-O6CH-WWYP60dlsryT-qxq3UyfO6-LmxyGGaq88AsfMRMsvY38=', start_index=20129)
Annotation(end_index=20255, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGeLjing7mYQQuOe7ojL2Uoa4KakcfWadguuydvyuT2qCP2zXnvwNwV2VX9re6tyZQS0jsITj5CcUR6exve_qn66Hq_TwMMQNzXULrTHLsVVRXgflHYpw8yrSCwBDJhlQoxs7uuXEM-', start_index=20246)
Annotation(end_index=20359, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGydvlusV4dg47jXl6HPLPrl_LYMZBP1yeDGOtWoi3V16_H5MtFv1Neft_uU8SNFKuvEJN9sRvikveqTAihUb1uHENwfmWA62Dg82KUUIhwyfT_EslMCwDSkDUjYmVZFhKUUe6932b0-ChfgtczlSAr79S0JDX_xrX-XqrXd_q75UCguFruek8x5jxlsZG624sYAu9D-0v2XlX_6Fl5KhNnUTeZCNk7aOtkjpsS3DS4cZHuuQAuvFt_HK7KHZ6DLA==', start_index=20350)
Annotation(end_index=20479, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqoCxB0BI0Y7BeR2EQKp8Zkyb8BFRbex9RLQC3FbaZp1LFS7F63n1S80NBpNU9Jb-W_ItQn4h9HnKECjXQXaHkITZxZtDkkmSzRibtawrgYo8SJd-OBV5LCdcwJg3FLsR3L7dRLZ48pLv92icqF-afmF2K_11rABGT_auUlbXS_tNoeW4tnyUC00zflpwLpiswDlnXXUkcklOHEVt2hBDtU_rZV_6sufc7zsJ6cAvOkKwTjSaiX3ZGtOhsapQ9ejQLq5QRraYArgtY3ptuHcDLOA2zxG-BDsjLNyiFVru1bYOK4PhXN6jZZCtMaK_HuOoQXg==', start_index=20469)
Annotation(end_index=20574, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNVlNhYpDMbN163tH6zlcRAgatLz3Ik-hI9VvCkWf6SUFY6uf_GI5bYEzWD3EOJlHCarREYrbP5V2nUwQxSthn-YDAj79Y41XQJY4TR1SLm4UwAs12X9xNh3NSR7uPnpI=', start_index=20564)
Annotation(end_index=20659, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRzcF03wO-emcaXwPbWhaYwF690Nq1lbd-Vts8yLMKuSWXsuk9y2TMue_W4-TcEkya5NlBvZ-Iy3RfSPM1ig8Upr747maMWLqv4OxKs1WnoWYNHMCfmJxyqi_i3-HUkMqZrgwkfcE9wNR0uOI-8GwP1hcvTaeKeJYjqijEE3KUxcfZF15JDDwioixPvlI=', start_index=20650)
Annotation(end_index=20762, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7pYFys9Tc1eEwzO2-yQiSpXptZuDgx88kWRriUtz128n51lkyv3xwjTQXOgqyXUsonyNMKztHMiJHnriYLBXPTB4y06CjuUvFP0okh931srOa5MVURIbjwbq7Jbvpl0qLLpLLbl8OUQ1O0g==', start_index=20753)
Annotation(end_index=20860, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEjqmZ99L2LM-iDBvmHM1MVVp9XSZnbaWKaYOMwIEMBHoNeLU85kFKdmRdwAR91Ll3pg0we83ZjYDKHrOu3XqKlAHXMSlMr7SIxx-zZhtfWZEH8-_i1PQzl5xLFWImYicBcUvkSsEQvyuqPK4sSGGX5A6YlVivXC8lTBnAKlKDuLDfXkTCMOLNeSZLLGnOhMIjqzWPFPxRlXraAITPiHpl85K8wWWCIotJAC9jnfSNClcXpTvMW1dsd5t8l47owAOC', start_index=20851)
Annotation(end_index=20934, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRnP30DmE3LDhI-t7aYZB3YAw2PDiKpHOAoRC9mtGK4ViiOjKKc3IjrjWakODaDyq_7BNJ04b4ITDgvzvWxZbzRnxPE16C5iJ3bSe0nU41yeZLnWIPXJkzY56JoErH1LJnVK_zs5p2Bwqq0avLNVhdhhB7X8H41lQOTW6RYtviF3wogclXeAYLYXdYUGomB5DoUIr6z2jkOTV5VkxL3Z2u-bzif7tCKMFUKy-GW9QypdlX', start_index=20925)
Annotation(end_index=21044, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFY6RaaTeNJ6yTtDWrKG97eaEbgpCxWAYlktauWQFeolvOMD6R8pp0VyrhDuonLEuGtbG2uQIziPItPoW0BPw-PpeCDLwrt5_2H5LDE6mXnxswCsB8xGDaoEAokhR3vYmm9LkFFpUEVT5l7uyOC920j591kWTKD', start_index=21035)
Annotation(end_index=21114, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFR6r7gf0KdukKnRRpGcA4RRhImljwGUOEHpso3fvmHtGecQKLR7seFOsTRwSXG2yRr6Mlnyo2E-OyMD18YN6i6klPJtOEA-h3wnV2SSVOMdkdrRw0qjJAlDx38gmvq-SG_H7awk74OoH-NTriWjNEdMZ1hhDAHnKohky2jhQg-OlwhgvAhn4uHgIHuAT1CpIaK42cQK8GS7neianfRWSIeoN11-LggaI3b4FoYvhixr5UuKpMb1yldmJ4Y2Q==', start_index=21104)

## Sources
