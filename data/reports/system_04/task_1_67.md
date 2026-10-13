# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 3c550782 | **Time:** 358.59s | **Cost:** $1.39200
--------------------------------------------------------------------------------

# How Base-Stock Policy Parameter Optimization Minimizes Total Cost Relative to Demand Variation Coefficients

### Key Points
*   **Base-Stock Optimization Mechanism:** The base-stock policy (often denoted as $S$ or $S-1, S$) minimizes total cost by balancing the expected cost of holding excess inventory against the expected cost of backorders or lost sales. The optimal level $S^*$ is found where the marginal cost of adding one unit of inventory equals the marginal reduction in expected shortage costs.
*   **Role of Coefficient of Variation (CV):** The Coefficient of Variation ($CV = \sigma/\mu$) serves as a normalized measure of demand uncertainty. Research indicates that as CV increases, the "first term" of the safety stock equation (driven by demand variability) becomes the dominant factor in total inventory investment, often accounting for over 80% of safety stock in high-volatility scenarios.
*   **Cost Sensitivity:** The relationship between total cost and demand variation is significant. Empirical studies suggest that a 1% reduction in demand variance can yield approximately a 0.4% to 0.5% reduction in safety stock requirements, thereby lowering total holding costs while maintaining service levels.
*   **Complexity in Non-Standard Models:** In systems with lost sales (rather than backorders) or compound demand distributions, the optimal base-stock level is highly sensitive to CV. High variability in these contexts exacerbates the risk of irreversible lost sales, often necessitating simulation-based metaheuristics to locate the cost-minimizing $S^*$ because traditional mean-based approximations fail.

---

## 1. Introduction to Base-Stock Policy and Cost Minimization

The continuous-review base-stock policy is a fundamental inventory control mechanism used extensively in supply chain management. Under this policy, the inventory position is monitored continuously, and a replenishment order is placed immediately whenever the inventory position drops below a specific base-stock level, denoted as $S$ [cite: 1, 2]. The primary objective of optimizing this parameter $S$ is to minimize the long-run expected total cost, which typically comprises holding costs, shortage costs (backorder or lost sales penalties), and occasionally ordering costs [cite: 1, 3].

### 1.1 The Total Cost Function
The mathematical foundation of base-stock optimization relies on a convex cost function. The total expected cost per unit of time, $TC(S)$, is generally expressed as the sum of expected holding costs and expected shortage costs.
\[ TC(S) = h \cdot E[I^+(S)] + b \cdot E[I^-(S)] \]
Where:
*   $h$ is the holding cost per unit per time unit.
*   $b$ is the backorder cost per unit per time unit.
*   $E[I^+(S)]$ is the expected on-hand inventory.
*   $E[I^-(S)]$ is the expected backorder level [cite: 3, 4].

The optimization process seeks to identify the scalar $S^*$ that minimizes this function. In standard models (e.g., Newsvendor-type frameworks applied to continuous review), this minimum is found where the cumulative distribution function (CDF) of demand during lead time equals a critical ratio, typically $\frac{b}{h+b}$ [cite: 3, 4].

### 1.2 The Challenge of Demand Variation
While the cost parameters ($h$ and $b$) determine the *target service level*, the actual magnitude of $S^*$ required to achieve that target is dictated by the stochastic nature of demand. The Coefficient of Variation (CV), defined as the ratio of the standard deviation of demand to the mean demand ($CV = \sigma / \mu$), is the critical metric for assessing this variability [cite: 5]. The optimization of $S$ must essentially "buffer" against this variability. Consequently, the total cost at optimality is intrinsically linked to the CV; as the "noise" in demand (CV) increases, the system must carry more expensive safety stock to minimize the total cost function effectively [cite: 6].

---

## 2. The Coefficient of Variation (CV) in Demand Modeling

### 2.1 Definition and Statistical Significance
The Coefficient of Variation provides a normalized measure of dispersion, allowing for the comparison of variability across different products or time periods regardless of the mean demand volume [cite: 5].
\[ CV = \frac{\sigma}{\mu} \times 100\% \]
In inventory modeling, CV is pivotal for segmentation. Products with low CV (e.g., $\le 0.5$) are considered stable and predictable, whereas products with high CV (e.g., $> 0.5$) exhibit "lumpy" or erratic demand patterns [cite: 6].

### 2.2 CV as a Driver of Inventory Classification
The magnitude of CV directly influences the choice of forecasting models and inventory policies. Low CV items can often be managed with simple mean-based approximations. However, high CV items require sophisticated probabilistic models because the "tail" risks of the demand distribution—where stockouts occur—are much fatter. Research indicates that in high CV scenarios, the variance of demand becomes the primary driver of safety stock levels, overshadowing the influence of the mean demand [cite: 6].

---

## 3. Analytical Relationship Between CV and Optimal Base-Stock Levels

The optimization of the base-stock parameter $S$ can be decomposed into two components: the cycle stock (covering mean demand during lead time) and the safety stock (buffering against variability).
\[ S^* = \mu_L + SS \]
Where $\mu_L$ is the expected demand during lead time and $SS$ is the safety stock.

### 3.1 The Safety Stock Formulation
For normally distributed demand, the safety stock required to minimize costs (by achieving the optimal service level implied by the $b/h$ ratio) is calculated as:
\[ SS = Z \cdot \sigma_D \cdot \sqrt{L} \]
Where:
*   $Z$ is the safety factor corresponding to the optimal service level.
*   $\sigma_D$ is the standard deviation of demand per period.
*   $L$ is the lead time [cite: 7, 8].

Since $\sigma_D = CV \cdot \mu_D$, the equation can be rewritten to explicitly show the dependency on CV:
\[ SS = Z \cdot (CV \cdot \mu_D) \cdot \sqrt{L} \]

### 3.2 Dominance of the "First Term"
Research analyzing the composition of safety stock reveals that the total inventory buffer is derived from two sources of variability: demand variability and lead time variability. The general formula for combined uncertainty is:
\[ SS = Z \sqrt{L\sigma_D^2 + \mu_D^2\sigma_L^2} \]
In this context, the term containing $\sigma_D$ (and thus CV) is often referred to as the "first term." Empirical studies on consumer packaged goods (CPG) and industrial parts demonstrate that as CV increases, this first term accounts for an increasing percentage of the total safety stock—often exceeding 80% for low CV items and dominating even more for high CV items [cite: 6].

This implies that parameter optimization for $S^*$ is essentially an exercise in scaling the base stock linearly with the standard deviation of demand. Therefore, if the mean demand is constant, $S^*$ (and the associated holding cost) increases linearly with the Coefficient of Variation [cite: 9, 10].

---

## 4. Cost Sensitivity to Demand Variation

The minimization of total cost is achieved by setting $S$ such that the marginal cost of holding inventory equals the marginal cost of a shortage. However, the *value* of that minimum total cost is highly sensitive to the CV.

### 4.1 Impact on Holding and Shortage Costs
As the Coefficient of Variation increases, the probability density function (PDF) of demand spreads out. To maintain the same optimal protection level against stockouts (which is determined solely by the cost parameters $h$ and $b$), the optimizer must increase $S$.
*   **Holding Cost:** Increases because the optimal base-stock level $S^*$ rises to accommodate the wider demand distribution.
*   **Shortage Cost:** In an optimized system, the expected shortage cost is balanced against holding costs. However, with higher variability, the absolute number of expected backorders for a *sub-optimal* $S$ would skyrocket. By optimizing $S$ upward, the system converts potential shortage costs into realized holding costs [cite: 1, 4].

### 4.2 The "1% Variance Reduction" Heuristic
A critical finding in inventory optimization research is the quantitative relationship between variance reduction and cost savings. Analysis of safety stock sensitivity suggests that a 1% decrease in demand variance (which lowers the CV) results in a 0.4% to 0.5% reduction in required safety stock [cite: 6].
For a company with substantial inventory investment, this is non-trivial. For instance, if \$25 million is tied up in safety stock, a 10% reduction in demand variance (achieved, perhaps, through better forecasting that reduces the effective CV) could release approximately \$1 million in working capital [cite: 6]. This demonstrates that total cost minimization is not just about finding $S^*$ for a *given* CV, but also about actively reducing the CV itself.

### 4.3 Non-Linearity of Service Level Costs
While the relationship between $S^*$ and $\sigma$ (and thus CV) is linear for a fixed Z-score, the relationship between the Z-score and the cost is non-linear. As the target service level approaches 100%, the required safety stock grows exponentially. Therefore, if a high CV forces a system to operate in the "tail" of the distribution, slight inaccuracies in parameter optimization can lead to massive cost inefficiencies [cite: 7].

---

## 5. Optimization Under Complexity: Lost Sales and Compound Demand

Standard analytical models often assume backordering and normal demand. However, real-world scenarios frequently involve "Lost Sales" (where demand not immediately satisfied is lost forever) and "Compound Demand" (erratic batch sizes).

### 5.1 Lost Sales vs. Backorders
In lost sales models, the optimization of $S$ is more complex because the cost of a stockout includes not just a penalty but the loss of the profit margin and potential future market share [cite: 2, 11].
*   **Sensitivity to CV:** Research indicates that optimal base-stock levels in lost sales systems are highly sensitive to demand variability. Unlike backorder systems where demand is merely delayed, lost sales represent an irreversible economic loss. Consequently, as CV rises, the optimal policy often dictates a disproportionately higher $S^*$ to avoid the "death spiral" of frequent stockouts [cite: 11].
*   **Intractability:** Analytical solutions for continuous-review lost-sales models with high CV are often intractable. The objective function may not be strictly convex or may be too complex to differentiate [cite: 2, 12].

### 5.2 Simulation-Based Metaheuristics
To minimize total cost in these high-CV, complex environments, researchers employ simulation-optimization frameworks. These methods integrate discrete-event simulation with metaheuristics (e.g., genetic algorithms or search procedures).
*   **Mechanism:** The simulation evaluates the total cost for a candidate $S$ under stochastic conditions (incorporating the specific CV). The metaheuristic then iteratively adjusts $S$ based on the feedback to converge on a near-optimal solution [cite: 2, 12].
*   **Findings:** These studies confirm that traditional heuristics (like those derived from simple EOQ or normal approximations) perform poorly when CV is high. Simulation-based optimization can identify $S^*$ levels that significantly outperform mean-based rules, preventing costly under-stocking in volatile markets [cite: 2, 12].

---

## 6. Lead Time and Demand Variability Interactions

The optimization of base-stock parameters cannot view demand variability in isolation; it interacts heavily with lead time ($L$).

### 6.1 Combined Variance
The total variance faced by the inventory system during a replenishment cycle is a function of both demand variance and lead time variance.
\[ \sigma_{Total}^2 = L\sigma_D^2 + \mu_D^2\sigma_L^2 \]
Optimization minimizes total cost by buffering against this combined variance. High demand CV ($\sigma_D$) amplifies the impact of lead time length ($L$). Conversely, high lead time variability ($\sigma_L$) amplifies the impact of mean demand [cite: 8, 10].

### 6.2 Strategic Trade-offs
Research highlights that demand variability ($\sigma_D$) is often the dominant influence on safety stock requirements, with its effect being significantly larger than that of lead time variability in many practical scenarios (sometimes by a factor of 10) [cite: 10].
*   **Optimization Insight:** To minimize total cost, it is often more effective to invest in reducing demand uncertainty (lowering CV via forecasting) than to marginally reduce lead time variability, although both are beneficial.
*   **Linear Decrease with Lead Time:** While the relationship with CV is driven by the standard deviation, the relationship between optimal cost and *lead time length* is often described as linear. Reducing the lead time duration ($L$) linearly decreases the period over which the CV acts, thereby reducing $S^*$ and Total Cost [cite: 9].

---

## 7. Managerial Implications and Strategic Adjustments

### 7.1 Inventory Segmentation
Given the strong influence of CV on optimal costs, firms should not apply a "one-size-fits-all" service level target.
*   **High CV Items:** These require sophisticated planning. The optimal $S$ will be high relative to the mean. Managers might accept a lower service level for these items to cap the total cost, or use "Make-to-Order" strategies if the CV is too high to support a base-stock policy economically [cite: 5].
*   **Low CV Items:** These can be managed with leaner inventories and higher service level targets because the marginal cost of protection is lower [cite: 5].

### 7.2 Forecasting as Cost Reduction
Since the "demand variation" used in safety stock formulas is actually the variance of the *forecast error*, improving forecast accuracy directly reduces the effective CV. The "1% variance reduction" rule suggests that investments in predictive analytics (e.g., Machine Learning) yield high ROI by lowering the $S^*$ required to minimize total cost [cite: 6].

---

## Conclusion

Base-stock policy parameter optimization minimizes total cost by identifying the specific inventory level $S^*$ that equilibrates the marginal costs of holding inventory and stockouts. The Coefficient of Variation (CV) acts as a primary scaling factor in this optimization. A higher CV necessitates a larger safety buffer to maintain the optimal service level, thereby increasing the minimum achievable total cost.

The relationship is characterized by the dominance of demand variability in the safety stock calculation, where the variance of demand often constitutes the majority of the safety stock requirement. Advanced optimization techniques, particularly simulation-based metaheuristics, are essential when high CV is combined with lost sales or stochastic lead times, as they capture the non-linear penalties of stockouts that simplified models miss. Ultimately, minimizing total cost in the presence of demand variation requires a dual approach: mathematically optimizing $S$ for the current CV, and operationally working to reduce the CV through improved forecasting and supply chain stability.

## References
[cite: 1] Scribd. (n.d.). Base stock policy.
[cite: 2] ResearchGate. (2026). Optimizing Base-Stock Levels in Continuous-Review Inventory Models...
[cite: 4] UTDallas. (n.d.). Basestock Model.
[cite: 13] Scialert. (2009). [Title regarding base stock policy optimization].
[cite: 12] ResearchGate. (2026). Optimizing Base-Stock Levels... [Duplicate/Related to 2].
[cite: 5] Inteli-chain. (n.d.). Coefficient of Variation (CoV) in Demand Planning.
[cite: 9] ResearchGate. (2004). The Value of Advance Demand Information...
[cite: 14] NUS. (2017). [Paper on Brownian inventory models].
[cite: 6] Arkieva. (2021). Coefficient of Variation Safety Stock Decisions.
[cite: 3] Wikipedia. (n.d.). Base stock model.
[cite: 15] IESE. (n.d.). [Paper on multi-echelon inventory].
[cite: 4] UTDallas. (n.d.). Basestock Model [Duplicate of 3].
[cite: 5] Inteli-chain. (n.d.). Coefficient of Variation... [Duplicate of 6].
[cite: 6] Arkieva. (2021). [Duplicate of 13].
[cite: 11] ResearchGate. (2026). Optimizing Base Stock Policies with Stochastic Lead Times...
[cite: 16] Formplus. (2021). Coefficient of Variation.
[cite: 9] ResearchGate. (2004). [Duplicate of 7].
[cite: 15] IESE. (n.d.). [Duplicate of 16].
[cite: 5] Inteli-chain. (n.d.). [Duplicate of 6].
[cite: 6] Arkieva. (2021). [Duplicate of 13].
[cite: 10] MIT. (n.d.). King_SafetyStock.pdf.
[cite: 7] ASCM. (n.d.). Safety Stock: A Contingency Plan...
[cite: 8] ISM. (2025). How to Calculate Safety Stock.
[cite: 6] Arkieva. (2021). [Duplicate of 13].
[cite: 2] ResearchGate. (2026). [Duplicate of 2].

**Sources:**
1. [scribd.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0kMecCzfucjdPY8Q2D87A_xXLjV24ZklHVSNs_0sq-WxEcigr26AASL40fRNDHhmSwsbyjo__Lgxv87nXaHr1dz0kmkp7VNIzjyqAhJfTq2pmZjJH4ts2TTdSJZwd1p0KEeoxZs_Bh5hrhHO1tcIUybBcJA==)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1e7Zqz-dJ1VkxNuNmyJRnZfUjudse4dS2UPbLSXudNzBaOEjIvfn4EF-xJ7npwAOeu1rFgypipoiul7hIi1z5cntQPTKUuOyOusoYButtzV53ggH2PSxY3U-Un9Ng-dTpt4X-CZLLssFcrfYiyxwv4B7Pux3k4XHu14mZkDw_uPISDbf86Rc1AVm458_jjbtXIIo5hrqI-UiWk4SDpIAI1K9VimqC5zkgCxVUevRyy3DCwpk0vyyatinm7sKTScPv5wExYxqaSB7D5U834Bh6h0YOSsJ1W6_jMpNZyPbAoBss3i2aFT1MuEXpfM1OUmAfImqHFh_O7nZbM9CNxURozkYvqFNi1CFuIENA_W-A97nAcyUkDvY=)
3. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQlzQ3fT4GvTS7FkGK6DAF1ipLGp8FFBKd-7TYy_a7p_83aNKpg09ExHrHRvgEGyVJsonZeCc_XouArMtkx1oiSKHTDqpDlmeB0cI2_S09qTubxKzYYdYkkrL5OgdslJkpYT2G)
4. [utdallas.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXFU8R2gutUy5_-xUJF_goE5WiPQqQoxcCw0UZG93uBklhZAtQ4IXzBRIcLEMYOGx53W5ZqZHzrZWpxpoUyc8_ScjmGHuhSYjgR_C9jKqPJ7rk06wg6r0jRjlDDREOgITgvXdz3c8Hi8t9xBDYmhwfcd_O)
5. [inteli-chain.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlft6gfPLIViVP7Ck3ZGjCPeaG2WtVQNonMsf-IEpzd2o1hy2ny6CImZE7sL8ilIX0o2Tne99Fle34vVhKY6S1C73ozecHAkulYKJSd_KyKsDgmephCkhWdvKr04NS_BK7-WOgZi3SXCJnJEX0c3A_gPt_n3LBAbraJ0iMvzngsk_Wfmhr14ZFrpJWTBx7qr2nQbZUiyFA7w==)
6. [arkieva.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZ82BzVjcRy2UlP3VfaA59CJU7GVz3h_cZzKZqL9rDLTeolXa1e8qFa8V9MTDr2E6wjxzfYkWy95xAQjZt8S4VgMNz6MzhOkVCs5ZxKs9c_6sVLE5G-A_KmQgUJrbQqX4Haqgoo_lE2SXEVZA3FddEFJILBfMbjD8Alg8OOvxe)
7. [ascm.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGocsleNDhTgY_IHHuRWA6-WJRVvHPe8-M-9OC6EYsAPMraRN2vPiBshrgDheGwZtWzMkDaMLpKKab5hIuItXMC0c5mYRvroCE-SQz7L_VBEtPD2bxQEP-8KZyKQPTnXd8xYCOY1B3vdQEQdvpMiKyPpKLBIGHaD61dAyuqhfDGYXfX9SXEMjR4eNUpUnAGOwH0zetXOX4JXczSw==)
8. [ism.ws](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUmfCq6QQDIK4xFu1UQDv5GCN2MSfRA4PwkKA3SiN2wKMUzl7P6Fo1x0TGZ2zkFKp83Lg_59HBTpP2l67C1EbiexkdE6rYebuMB11pM97w0Fx1TX8twwpOW2Z9ZQ0GLQlB-otKpk_fWZNJK0L9ikuxjw==)
9. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFIDFAbA2VDj-ZpivLsL6duPIJlyPnFxIyynAfC8_nZGYaZznadTmloyFYlgVZ477cUCOqaC3vYCivmkdHvHp7l1AnORd4M5unn0QFn_CarE_ayDBpgbXyOux3VS3hBxuyKjtQKdXQ_-gT93ijjKTXriRqTXeqc1q-LSXpbqaWIL3Lv8e3Z5en1_p98Y9esNABER06D3zVIAF5lCn6gYAupYQCh_g0CxqKJjQUr3F0S1HOc8-hKVmVtA==)
10. [mit.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESy-OO5dBEzIPlFZxjmZJNKqg59DoM1wYmhYuTkoQpd-49tbH-P8FPtMXrFJvNrnrhZAz7wZJGQ5jS5KxhhfT-zhGKhK2CJn7ADjeARlkV7AYy9n6u8onBqTZkX3qIatXx8RsVLwO7Vi3o5OPcpHlyPM_U81pX-g==)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIz8GTMH4GeUsmlqIq74GSO1LLN9CNtM-lC9s7HGD1iR0ANle-24q6gJynane84DLo7_EXm2i8G_gpJUwX_E47ETjcEzxDnztM_zH2lSf61jhpUClQhXubOozJU3mf1mydoA0Sik2rCEFJiL376Swr_PGW06LPugtwZz5fG5f7HMLRQ21T6L8aE3L6_epJiHL3bbJ5neCKRPw53_9XxFuQ1ST8UrvA8oV7IPB-VdvLjvtaydTh5twPpDBvk_OE5jYp-B_kvO4OghX-ZXH4OoENyQaUjhxDiw==)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuvf11ZsWP9ds-VTu4v-6EmZHt0sCoU_P2-KB0VNZNGZm9Aw_aY6-jeqicC1_tZIYLTfSC_n2pmzuObpA8aXjY5j7BZ5eUuQAbLDZA87eJZiX_FZLl9pX5wDOvGNRnr3_QfCKZHwQ2iwgdbZDq78910UtJdi9uqnLYE6vgmVDk8pbwn5CPfjn_wSUze6YH_suNHglJ6a8pwZCpo6kQ49axS5LO8NRuepys6WWxL3TFmTyhGl74CF48LQ7GxAzJv7lzWmBLnCVsMjKWtd1FyZRitLFYwXiePKsFcyUfIEtxQYaAN6Q_dD9ClwB2lUPEInw8U5NsAVXlaRbl-ni0iW8-9hv8wqSTRjRIpRYLxhgZ-5gDxxxDkrI=)
13. [scialert.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHk73GOWuuHSNLi3jdRBD0riAQeUVcdsmGNQCCjc5rlAQ2Vb6FEWhCUXY_dHR_VFIpkWPIf00goX7RtVMchIDnPimj7eJ0BvF90MI3llrdHe5kz2OxRWFQMNFmrZnGvh9iPfm8dLQX8nvc=)
14. [nus.edu.sg](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFK9W8phsDDxxf_EA9hjNr4yknPKY4-mIO2GDy3aq5HVfx52KMTSoPPbw7ELK1gOFLNXbNEUkYXwDMb_Ol10IFz_A8Tcdi6B6G3Z690X-P8a9W-mITRCnTTY3nroG2ElnMqVUayG4GLS7XxXe8XVY4VZkMkJreNtUynA4FnsqY3rYS_)
15. [iese.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqXpoKp5lkwx5mOhfiKtZnfsPEU0rt2V86GkTMKFlqFJSCeyOVB9gOiUxFS0jV4USrRO1FubtPSBYNMCotzlvgt3QFm308dt7QAyMNlDaGyGBhMJ6Tc0tvroyx4KJzp6gijvjgAzFJuMzhikQ=)
16. [formpl.us](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzhWqTOwiVZdR7Iog_JnolhYq_B3GECQMacP9cUPqCDUExJ6OA3cXIZvlgca8ce9XRCL1ACe9e2wkn0_1diduE6f4iPMPQ9sZWpa6hvVwEPuyLU_3dLJgpRtjpNU64ly508PtT5tc=)


## Annotations
Annotation(end_index=2050, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0kMecCzfucjdPY8Q2D87A_xXLjV24ZklHVSNs_0sq-WxEcigr26AASL40fRNDHhmSwsbyjo__Lgxv87nXaHr1dz0kmkp7VNIzjyqAhJfTq2pmZjJH4ts2TTdSJZwd1p0KEeoxZs_Bh5hrhHO1tcIUybBcJA==', start_index=2038)
Annotation(end_index=2050, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1e7Zqz-dJ1VkxNuNmyJRnZfUjudse4dS2UPbLSXudNzBaOEjIvfn4EF-xJ7npwAOeu1rFgypipoiul7hIi1z5cntQPTKUuOyOusoYButtzV53ggH2PSxY3U-Un9Ng-dTpt4X-CZLLssFcrfYiyxwv4B7Pux3k4XHu14mZkDw_uPISDbf86Rc1AVm458_jjbtXIIo5hrqI-UiWk4SDpIAI1K9VimqC5zkgCxVUevRyy3DCwpk0vyyatinm7sKTScPv5wExYxqaSB7D5U834Bh6h0YOSsJ1W6_jMpNZyPbAoBss3i2aFT1MuEXpfM1OUmAfImqHFh_O7nZbM9CNxURozkYvqFNi1CFuIENA_W-A97nAcyUkDvY=', start_index=2038)
Annotation(end_index=2293, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0kMecCzfucjdPY8Q2D87A_xXLjV24ZklHVSNs_0sq-WxEcigr26AASL40fRNDHhmSwsbyjo__Lgxv87nXaHr1dz0kmkp7VNIzjyqAhJfTq2pmZjJH4ts2TTdSJZwd1p0KEeoxZs_Bh5hrhHO1tcIUybBcJA==', start_index=2281)
Annotation(end_index=2293, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQlzQ3fT4GvTS7FkGK6DAF1ipLGp8FFBKd-7TYy_a7p_83aNKpg09ExHrHRvgEGyVJsonZeCc_XouArMtkx1oiSKHTDqpDlmeB0cI2_S09qTubxKzYYdYkkrL5OgdslJkpYT2G', start_index=2281)
Annotation(end_index=2833, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXFU8R2gutUy5_-xUJF_goE5WiPQqQoxcCw0UZG93uBklhZAtQ4IXzBRIcLEMYOGx53W5ZqZHzrZWpxpoUyc8_ScjmGHuhSYjgR_C9jKqPJ7rk06wg6r0jRjlDDREOgITgvXdz3c8Hi8t9xBDYmhwfcd_O', start_index=2821)
Annotation(end_index=2833, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQlzQ3fT4GvTS7FkGK6DAF1ipLGp8FFBKd-7TYy_a7p_83aNKpg09ExHrHRvgEGyVJsonZeCc_XouArMtkx1oiSKHTDqpDlmeB0cI2_S09qTubxKzYYdYkkrL5OgdslJkpYT2G', start_index=2821)
Annotation(end_index=3171, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXFU8R2gutUy5_-xUJF_goE5WiPQqQoxcCw0UZG93uBklhZAtQ4IXzBRIcLEMYOGx53W5ZqZHzrZWpxpoUyc8_ScjmGHuhSYjgR_C9jKqPJ7rk06wg6r0jRjlDDREOgITgvXdz3c8Hi8t9xBDYmhwfcd_O', start_index=3159)
Annotation(end_index=3171, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQlzQ3fT4GvTS7FkGK6DAF1ipLGp8FFBKd-7TYy_a7p_83aNKpg09ExHrHRvgEGyVJsonZeCc_XouArMtkx1oiSKHTDqpDlmeB0cI2_S09qTubxKzYYdYkkrL5OgdslJkpYT2G', start_index=3159)
Annotation(end_index=3601, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlft6gfPLIViVP7Ck3ZGjCPeaG2WtVQNonMsf-IEpzd2o1hy2ny6CImZE7sL8ilIX0o2Tne99Fle34vVhKY6S1C73ozecHAkulYKJSd_KyKsDgmephCkhWdvKr04NS_BK7-WOgZi3SXCJnJEX0c3A_gPt_n3LBAbraJ0iMvzngsk_Wfmhr14ZFrpJWTBx7qr2nQbZUiyFA7w==', start_index=3592)
Annotation(end_index=3905, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZ82BzVjcRy2UlP3VfaA59CJU7GVz3h_cZzKZqL9rDLTeolXa1e8qFa8V9MTDr2E6wjxzfYkWy95xAQjZt8S4VgMNz6MzhOkVCs5ZxKs9c_6sVLE5G-A_KmQgUJrbQqX4Haqgoo_lE2SXEVZA3FddEFJILBfMbjD8Alg8OOvxe', start_index=3896)
Annotation(end_index=4226, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlft6gfPLIViVP7Ck3ZGjCPeaG2WtVQNonMsf-IEpzd2o1hy2ny6CImZE7sL8ilIX0o2Tne99Fle34vVhKY6S1C73ozecHAkulYKJSd_KyKsDgmephCkhWdvKr04NS_BK7-WOgZi3SXCJnJEX0c3A_gPt_n3LBAbraJ0iMvzngsk_Wfmhr14ZFrpJWTBx7qr2nQbZUiyFA7w==', start_index=4217)
Annotation(end_index=4502, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZ82BzVjcRy2UlP3VfaA59CJU7GVz3h_cZzKZqL9rDLTeolXa1e8qFa8V9MTDr2E6wjxzfYkWy95xAQjZt8S4VgMNz6MzhOkVCs5ZxKs9c_6sVLE5G-A_KmQgUJrbQqX4Haqgoo_lE2SXEVZA3FddEFJILBfMbjD8Alg8OOvxe', start_index=4493)
Annotation(end_index=5063, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZ82BzVjcRy2UlP3VfaA59CJU7GVz3h_cZzKZqL9rDLTeolXa1e8qFa8V9MTDr2E6wjxzfYkWy95xAQjZt8S4VgMNz6MzhOkVCs5ZxKs9c_6sVLE5G-A_KmQgUJrbQqX4Haqgoo_lE2SXEVZA3FddEFJILBfMbjD8Alg8OOvxe', start_index=5054)
Annotation(end_index=5872, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGocsleNDhTgY_IHHuRWA6-WJRVvHPe8-M-9OC6EYsAPMraRN2vPiBshrgDheGwZtWzMkDaMLpKKab5hIuItXMC0c5mYRvroCE-SQz7L_VBEtPD2bxQEP-8KZyKQPTnXd8xYCOY1B3vdQEQdvpMiKyPpKLBIGHaD61dAyuqhfDGYXfX9SXEMjR4eNUpUnAGOwH0zetXOX4JXczSw==', start_index=5860)
Annotation(end_index=5872, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUmfCq6QQDIK4xFu1UQDv5GCN2MSfRA4PwkKA3SiN2wKMUzl7P6Fo1x0TGZ2zkFKp83Lg_59HBTpP2l67C1EbiexkdE6rYebuMB11pM97w0Fx1TX8twwpOW2Z9ZQ0GLQlB-otKpk_fWZNJK0L9ikuxjw==', start_index=5860)
Annotation(end_index=6734, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZ82BzVjcRy2UlP3VfaA59CJU7GVz3h_cZzKZqL9rDLTeolXa1e8qFa8V9MTDr2E6wjxzfYkWy95xAQjZt8S4VgMNz6MzhOkVCs5ZxKs9c_6sVLE5G-A_KmQgUJrbQqX4Haqgoo_lE2SXEVZA3FddEFJILBfMbjD8Alg8OOvxe', start_index=6725)
Annotation(end_index=7038, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESy-OO5dBEzIPlFZxjmZJNKqg59DoM1wYmhYuTkoQpd-49tbH-P8FPtMXrFJvNrnrhZAz7wZJGQ5jS5KxhhfT-zhGKhK2CJn7ADjeARlkV7AYy9n6u8onBqTZkX3qIatXx8RsVLwO7Vi3o5OPcpHlyPM_U81pX-g==', start_index=7025)
Annotation(end_index=7038, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFIDFAbA2VDj-ZpivLsL6duPIJlyPnFxIyynAfC8_nZGYaZznadTmloyFYlgVZ477cUCOqaC3vYCivmkdHvHp7l1AnORd4M5unn0QFn_CarE_ayDBpgbXyOux3VS3hBxuyKjtQKdXQ_-gT93ijjKTXriRqTXeqc1q-LSXpbqaWIL3Lv8e3Z5en1_p98Y9esNABER06D3zVIAF5lCn6gYAupYQCh_g0CxqKJjQUr3F0S1HOc8-hKVmVtA==', start_index=7025)
Annotation(end_index=8094, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXFU8R2gutUy5_-xUJF_goE5WiPQqQoxcCw0UZG93uBklhZAtQ4IXzBRIcLEMYOGx53W5ZqZHzrZWpxpoUyc8_ScjmGHuhSYjgR_C9jKqPJ7rk06wg6r0jRjlDDREOgITgvXdz3c8Hi8t9xBDYmhwfcd_O', start_index=8082)
Annotation(end_index=8094, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0kMecCzfucjdPY8Q2D87A_xXLjV24ZklHVSNs_0sq-WxEcigr26AASL40fRNDHhmSwsbyjo__Lgxv87nXaHr1dz0kmkp7VNIzjyqAhJfTq2pmZjJH4ts2TTdSJZwd1p0KEeoxZs_Bh5hrhHO1tcIUybBcJA==', start_index=8082)
Annotation(end_index=8451, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZ82BzVjcRy2UlP3VfaA59CJU7GVz3h_cZzKZqL9rDLTeolXa1e8qFa8V9MTDr2E6wjxzfYkWy95xAQjZt8S4VgMNz6MzhOkVCs5ZxKs9c_6sVLE5G-A_KmQgUJrbQqX4Haqgoo_lE2SXEVZA3FddEFJILBfMbjD8Alg8OOvxe', start_index=8442)
Annotation(end_index=8766, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZ82BzVjcRy2UlP3VfaA59CJU7GVz3h_cZzKZqL9rDLTeolXa1e8qFa8V9MTDr2E6wjxzfYkWy95xAQjZt8S4VgMNz6MzhOkVCs5ZxKs9c_6sVLE5G-A_KmQgUJrbQqX4Haqgoo_lE2SXEVZA3FddEFJILBfMbjD8Alg8OOvxe', start_index=8757)
Annotation(end_index=9392, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGocsleNDhTgY_IHHuRWA6-WJRVvHPe8-M-9OC6EYsAPMraRN2vPiBshrgDheGwZtWzMkDaMLpKKab5hIuItXMC0c5mYRvroCE-SQz7L_VBEtPD2bxQEP-8KZyKQPTnXd8xYCOY1B3vdQEQdvpMiKyPpKLBIGHaD61dAyuqhfDGYXfX9SXEMjR4eNUpUnAGOwH0zetXOX4JXczSw==', start_index=9383)
Annotation(end_index=9942, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIz8GTMH4GeUsmlqIq74GSO1LLN9CNtM-lC9s7HGD1iR0ANle-24q6gJynane84DLo7_EXm2i8G_gpJUwX_E47ETjcEzxDnztM_zH2lSf61jhpUClQhXubOozJU3mf1mydoA0Sik2rCEFJiL376Swr_PGW06LPugtwZz5fG5f7HMLRQ21T6L8aE3L6_epJiHL3bbJ5neCKRPw53_9XxFuQ1ST8UrvA8oV7IPB-VdvLjvtaydTh5twPpDBvk_OE5jYp-B_kvO4OghX-ZXH4OoENyQaUjhxDiw==', start_index=9929)
Annotation(end_index=9942, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1e7Zqz-dJ1VkxNuNmyJRnZfUjudse4dS2UPbLSXudNzBaOEjIvfn4EF-xJ7npwAOeu1rFgypipoiul7hIi1z5cntQPTKUuOyOusoYButtzV53ggH2PSxY3U-Un9Ng-dTpt4X-CZLLssFcrfYiyxwv4B7Pux3k4XHu14mZkDw_uPISDbf86Rc1AVm458_jjbtXIIo5hrqI-UiWk4SDpIAI1K9VimqC5zkgCxVUevRyy3DCwpk0vyyatinm7sKTScPv5wExYxqaSB7D5U834Bh6h0YOSsJ1W6_jMpNZyPbAoBss3i2aFT1MuEXpfM1OUmAfImqHFh_O7nZbM9CNxURozkYvqFNi1CFuIENA_W-A97nAcyUkDvY=', start_index=9929)
Annotation(end_index=10351, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIz8GTMH4GeUsmlqIq74GSO1LLN9CNtM-lC9s7HGD1iR0ANle-24q6gJynane84DLo7_EXm2i8G_gpJUwX_E47ETjcEzxDnztM_zH2lSf61jhpUClQhXubOozJU3mf1mydoA0Sik2rCEFJiL376Swr_PGW06LPugtwZz5fG5f7HMLRQ21T6L8aE3L6_epJiHL3bbJ5neCKRPw53_9XxFuQ1ST8UrvA8oV7IPB-VdvLjvtaydTh5twPpDBvk_OE5jYp-B_kvO4OghX-ZXH4OoENyQaUjhxDiw==', start_index=10341)
Annotation(end_index=10576, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuvf11ZsWP9ds-VTu4v-6EmZHt0sCoU_P2-KB0VNZNGZm9Aw_aY6-jeqicC1_tZIYLTfSC_n2pmzuObpA8aXjY5j7BZ5eUuQAbLDZA87eJZiX_FZLl9pX5wDOvGNRnr3_QfCKZHwQ2iwgdbZDq78910UtJdi9uqnLYE6vgmVDk8pbwn5CPfjn_wSUze6YH_suNHglJ6a8pwZCpo6kQ49axS5LO8NRuepys6WWxL3TFmTyhGl74CF48LQ7GxAzJv7lzWmBLnCVsMjKWtd1FyZRitLFYwXiePKsFcyUfIEtxQYaAN6Q_dD9ClwB2lUPEInw8U5NsAVXlaRbl-ni0iW8-9hv8wqSTRjRIpRYLxhgZ-5gDxxxDkrI=', start_index=10563)
Annotation(end_index=10576, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1e7Zqz-dJ1VkxNuNmyJRnZfUjudse4dS2UPbLSXudNzBaOEjIvfn4EF-xJ7npwAOeu1rFgypipoiul7hIi1z5cntQPTKUuOyOusoYButtzV53ggH2PSxY3U-Un9Ng-dTpt4X-CZLLssFcrfYiyxwv4B7Pux3k4XHu14mZkDw_uPISDbf86Rc1AVm458_jjbtXIIo5hrqI-UiWk4SDpIAI1K9VimqC5zkgCxVUevRyy3DCwpk0vyyatinm7sKTScPv5wExYxqaSB7D5U834Bh6h0YOSsJ1W6_jMpNZyPbAoBss3i2aFT1MuEXpfM1OUmAfImqHFh_O7nZbM9CNxURozkYvqFNi1CFuIENA_W-A97nAcyUkDvY=', start_index=10563)
Annotation(end_index=11117, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuvf11ZsWP9ds-VTu4v-6EmZHt0sCoU_P2-KB0VNZNGZm9Aw_aY6-jeqicC1_tZIYLTfSC_n2pmzuObpA8aXjY5j7BZ5eUuQAbLDZA87eJZiX_FZLl9pX5wDOvGNRnr3_QfCKZHwQ2iwgdbZDq78910UtJdi9uqnLYE6vgmVDk8pbwn5CPfjn_wSUze6YH_suNHglJ6a8pwZCpo6kQ49axS5LO8NRuepys6WWxL3TFmTyhGl74CF48LQ7GxAzJv7lzWmBLnCVsMjKWtd1FyZRitLFYwXiePKsFcyUfIEtxQYaAN6Q_dD9ClwB2lUPEInw8U5NsAVXlaRbl-ni0iW8-9hv8wqSTRjRIpRYLxhgZ-5gDxxxDkrI=', start_index=11104)
Annotation(end_index=11117, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1e7Zqz-dJ1VkxNuNmyJRnZfUjudse4dS2UPbLSXudNzBaOEjIvfn4EF-xJ7npwAOeu1rFgypipoiul7hIi1z5cntQPTKUuOyOusoYButtzV53ggH2PSxY3U-Un9Ng-dTpt4X-CZLLssFcrfYiyxwv4B7Pux3k4XHu14mZkDw_uPISDbf86Rc1AVm458_jjbtXIIo5hrqI-UiWk4SDpIAI1K9VimqC5zkgCxVUevRyy3DCwpk0vyyatinm7sKTScPv5wExYxqaSB7D5U834Bh6h0YOSsJ1W6_jMpNZyPbAoBss3i2aFT1MuEXpfM1OUmAfImqHFh_O7nZbM9CNxURozkYvqFNi1CFuIENA_W-A97nAcyUkDvY=', start_index=11104)
Annotation(end_index=11451, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuvf11ZsWP9ds-VTu4v-6EmZHt0sCoU_P2-KB0VNZNGZm9Aw_aY6-jeqicC1_tZIYLTfSC_n2pmzuObpA8aXjY5j7BZ5eUuQAbLDZA87eJZiX_FZLl9pX5wDOvGNRnr3_QfCKZHwQ2iwgdbZDq78910UtJdi9uqnLYE6vgmVDk8pbwn5CPfjn_wSUze6YH_suNHglJ6a8pwZCpo6kQ49axS5LO8NRuepys6WWxL3TFmTyhGl74CF48LQ7GxAzJv7lzWmBLnCVsMjKWtd1FyZRitLFYwXiePKsFcyUfIEtxQYaAN6Q_dD9ClwB2lUPEInw8U5NsAVXlaRbl-ni0iW8-9hv8wqSTRjRIpRYLxhgZ-5gDxxxDkrI=', start_index=11438)
Annotation(end_index=11451, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1e7Zqz-dJ1VkxNuNmyJRnZfUjudse4dS2UPbLSXudNzBaOEjIvfn4EF-xJ7npwAOeu1rFgypipoiul7hIi1z5cntQPTKUuOyOusoYButtzV53ggH2PSxY3U-Un9Ng-dTpt4X-CZLLssFcrfYiyxwv4B7Pux3k4XHu14mZkDw_uPISDbf86Rc1AVm458_jjbtXIIo5hrqI-UiWk4SDpIAI1K9VimqC5zkgCxVUevRyy3DCwpk0vyyatinm7sKTScPv5wExYxqaSB7D5U834Bh6h0YOSsJ1W6_jMpNZyPbAoBss3i2aFT1MuEXpfM1OUmAfImqHFh_O7nZbM9CNxURozkYvqFNi1CFuIENA_W-A97nAcyUkDvY=', start_index=11438)
Annotation(end_index=12122, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESy-OO5dBEzIPlFZxjmZJNKqg59DoM1wYmhYuTkoQpd-49tbH-P8FPtMXrFJvNrnrhZAz7wZJGQ5jS5KxhhfT-zhGKhK2CJn7ADjeARlkV7AYy9n6u8onBqTZkX3qIatXx8RsVLwO7Vi3o5OPcpHlyPM_U81pX-g==', start_index=12109)
Annotation(end_index=12122, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUmfCq6QQDIK4xFu1UQDv5GCN2MSfRA4PwkKA3SiN2wKMUzl7P6Fo1x0TGZ2zkFKp83Lg_59HBTpP2l67C1EbiexkdE6rYebuMB11pM97w0Fx1TX8twwpOW2Z9ZQ0GLQlB-otKpk_fWZNJK0L9ikuxjw==', start_index=12109)
Annotation(end_index=12419, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESy-OO5dBEzIPlFZxjmZJNKqg59DoM1wYmhYuTkoQpd-49tbH-P8FPtMXrFJvNrnrhZAz7wZJGQ5jS5KxhhfT-zhGKhK2CJn7ADjeARlkV7AYy9n6u8onBqTZkX3qIatXx8RsVLwO7Vi3o5OPcpHlyPM_U81pX-g==', start_index=12409)
Annotation(end_index=12990, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFIDFAbA2VDj-ZpivLsL6duPIJlyPnFxIyynAfC8_nZGYaZznadTmloyFYlgVZ477cUCOqaC3vYCivmkdHvHp7l1AnORd4M5unn0QFn_CarE_ayDBpgbXyOux3VS3hBxuyKjtQKdXQ_-gT93ijjKTXriRqTXeqc1q-LSXpbqaWIL3Lv8e3Z5en1_p98Y9esNABER06D3zVIAF5lCn6gYAupYQCh_g0CxqKJjQUr3F0S1HOc8-hKVmVtA==', start_index=12981)
Annotation(end_index=13508, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlft6gfPLIViVP7Ck3ZGjCPeaG2WtVQNonMsf-IEpzd2o1hy2ny6CImZE7sL8ilIX0o2Tne99Fle34vVhKY6S1C73ozecHAkulYKJSd_KyKsDgmephCkhWdvKr04NS_BK7-WOgZi3SXCJnJEX0c3A_gPt_n3LBAbraJ0iMvzngsk_Wfmhr14ZFrpJWTBx7qr2nQbZUiyFA7w==', start_index=13499)
Annotation(end_index=13668, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlft6gfPLIViVP7Ck3ZGjCPeaG2WtVQNonMsf-IEpzd2o1hy2ny6CImZE7sL8ilIX0o2Tne99Fle34vVhKY6S1C73ozecHAkulYKJSd_KyKsDgmephCkhWdvKr04NS_BK7-WOgZi3SXCJnJEX0c3A_gPt_n3LBAbraJ0iMvzngsk_Wfmhr14ZFrpJWTBx7qr2nQbZUiyFA7w==', start_index=13659)
Annotation(end_index=14067, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZ82BzVjcRy2UlP3VfaA59CJU7GVz3h_cZzKZqL9rDLTeolXa1e8qFa8V9MTDr2E6wjxzfYkWy95xAQjZt8S4VgMNz6MzhOkVCs5ZxKs9c_6sVLE5G-A_KmQgUJrbQqX4Haqgoo_lE2SXEVZA3FddEFJILBfMbjD8Alg8OOvxe', start_index=14058)
Annotation(end_index=15219, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0kMecCzfucjdPY8Q2D87A_xXLjV24ZklHVSNs_0sq-WxEcigr26AASL40fRNDHhmSwsbyjo__Lgxv87nXaHr1dz0kmkp7VNIzjyqAhJfTq2pmZjJH4ts2TTdSJZwd1p0KEeoxZs_Bh5hrhHO1tcIUybBcJA==', start_index=15210)
Annotation(end_index=15264, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1e7Zqz-dJ1VkxNuNmyJRnZfUjudse4dS2UPbLSXudNzBaOEjIvfn4EF-xJ7npwAOeu1rFgypipoiul7hIi1z5cntQPTKUuOyOusoYButtzV53ggH2PSxY3U-Un9Ng-dTpt4X-CZLLssFcrfYiyxwv4B7Pux3k4XHu14mZkDw_uPISDbf86Rc1AVm458_jjbtXIIo5hrqI-UiWk4SDpIAI1K9VimqC5zkgCxVUevRyy3DCwpk0vyyatinm7sKTScPv5wExYxqaSB7D5U834Bh6h0YOSsJ1W6_jMpNZyPbAoBss3i2aFT1MuEXpfM1OUmAfImqHFh_O7nZbM9CNxURozkYvqFNi1CFuIENA_W-A97nAcyUkDvY=', start_index=15255)
Annotation(end_index=15366, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXFU8R2gutUy5_-xUJF_goE5WiPQqQoxcCw0UZG93uBklhZAtQ4IXzBRIcLEMYOGx53W5ZqZHzrZWpxpoUyc8_ScjmGHuhSYjgR_C9jKqPJ7rk06wg6r0jRjlDDREOgITgvXdz3c8Hi8t9xBDYmhwfcd_O', start_index=15357)
Annotation(end_index=15412, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHk73GOWuuHSNLi3jdRBD0riAQeUVcdsmGNQCCjc5rlAQ2Vb6FEWhCUXY_dHR_VFIpkWPIf00goX7RtVMchIDnPimj7eJ0BvF90MI3llrdHe5kz2OxRWFQMNFmrZnGvh9iPfm8dLQX8nvc=', start_index=15402)
Annotation(end_index=15491, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuvf11ZsWP9ds-VTu4v-6EmZHt0sCoU_P2-KB0VNZNGZm9Aw_aY6-jeqicC1_tZIYLTfSC_n2pmzuObpA8aXjY5j7BZ5eUuQAbLDZA87eJZiX_FZLl9pX5wDOvGNRnr3_QfCKZHwQ2iwgdbZDq78910UtJdi9uqnLYE6vgmVDk8pbwn5CPfjn_wSUze6YH_suNHglJ6a8pwZCpo6kQ49axS5LO8NRuepys6WWxL3TFmTyhGl74CF48LQ7GxAzJv7lzWmBLnCVsMjKWtd1FyZRitLFYwXiePKsFcyUfIEtxQYaAN6Q_dD9ClwB2lUPEInw8U5NsAVXlaRbl-ni0iW8-9hv8wqSTRjRIpRYLxhgZ-5gDxxxDkrI=', start_index=15481)
Annotation(end_index=15581, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlft6gfPLIViVP7Ck3ZGjCPeaG2WtVQNonMsf-IEpzd2o1hy2ny6CImZE7sL8ilIX0o2Tne99Fle34vVhKY6S1C73ozecHAkulYKJSd_KyKsDgmephCkhWdvKr04NS_BK7-WOgZi3SXCJnJEX0c3A_gPt_n3LBAbraJ0iMvzngsk_Wfmhr14ZFrpJWTBx7qr2nQbZUiyFA7w==', start_index=15572)
Annotation(end_index=15664, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFIDFAbA2VDj-ZpivLsL6duPIJlyPnFxIyynAfC8_nZGYaZznadTmloyFYlgVZ477cUCOqaC3vYCivmkdHvHp7l1AnORd4M5unn0QFn_CarE_ayDBpgbXyOux3VS3hBxuyKjtQKdXQ_-gT93ijjKTXriRqTXeqc1q-LSXpbqaWIL3Lv8e3Z5en1_p98Y9esNABER06D3zVIAF5lCn6gYAupYQCh_g0CxqKJjQUr3F0S1HOc8-hKVmVtA==', start_index=15655)
Annotation(end_index=15740, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFK9W8phsDDxxf_EA9hjNr4yknPKY4-mIO2GDy3aq5HVfx52KMTSoPPbw7ELK1gOFLNXbNEUkYXwDMb_Ol10IFz_A8Tcdi6B6G3Z690X-P8a9W-mITRCnTTY3nroG2ElnMqVUayG4GLS7XxXe8XVY4VZkMkJreNtUynA4FnsqY3rYS_', start_index=15730)
Annotation(end_index=15801, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZ82BzVjcRy2UlP3VfaA59CJU7GVz3h_cZzKZqL9rDLTeolXa1e8qFa8V9MTDr2E6wjxzfYkWy95xAQjZt8S4VgMNz6MzhOkVCs5ZxKs9c_6sVLE5G-A_KmQgUJrbQqX4Haqgoo_lE2SXEVZA3FddEFJILBfMbjD8Alg8OOvxe', start_index=15792)
Annotation(end_index=15877, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQlzQ3fT4GvTS7FkGK6DAF1ipLGp8FFBKd-7TYy_a7p_83aNKpg09ExHrHRvgEGyVJsonZeCc_XouArMtkx1oiSKHTDqpDlmeB0cI2_S09qTubxKzYYdYkkrL5OgdslJkpYT2G', start_index=15868)
Annotation(end_index=15925, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqXpoKp5lkwx5mOhfiKtZnfsPEU0rt2V86GkTMKFlqFJSCeyOVB9gOiUxFS0jV4USrRO1FubtPSBYNMCotzlvgt3QFm308dt7QAyMNlDaGyGBhMJ6Tc0tvroyx4KJzp6gijvjgAzFJuMzhikQ=', start_index=15915)
Annotation(end_index=15985, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXFU8R2gutUy5_-xUJF_goE5WiPQqQoxcCw0UZG93uBklhZAtQ4IXzBRIcLEMYOGx53W5ZqZHzrZWpxpoUyc8_ScjmGHuhSYjgR_C9jKqPJ7rk06wg6r0jRjlDDREOgITgvXdz3c8Hi8t9xBDYmhwfcd_O', start_index=15976)
Annotation(end_index=16047, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlft6gfPLIViVP7Ck3ZGjCPeaG2WtVQNonMsf-IEpzd2o1hy2ny6CImZE7sL8ilIX0o2Tne99Fle34vVhKY6S1C73ozecHAkulYKJSd_KyKsDgmephCkhWdvKr04NS_BK7-WOgZi3SXCJnJEX0c3A_gPt_n3LBAbraJ0iMvzngsk_Wfmhr14ZFrpJWTBx7qr2nQbZUiyFA7w==', start_index=16038)
Annotation(end_index=16125, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZ82BzVjcRy2UlP3VfaA59CJU7GVz3h_cZzKZqL9rDLTeolXa1e8qFa8V9MTDr2E6wjxzfYkWy95xAQjZt8S4VgMNz6MzhOkVCs5ZxKs9c_6sVLE5G-A_KmQgUJrbQqX4Haqgoo_lE2SXEVZA3FddEFJILBfMbjD8Alg8OOvxe', start_index=16116)
Annotation(end_index=16172, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIz8GTMH4GeUsmlqIq74GSO1LLN9CNtM-lC9s7HGD1iR0ANle-24q6gJynane84DLo7_EXm2i8G_gpJUwX_E47ETjcEzxDnztM_zH2lSf61jhpUClQhXubOozJU3mf1mydoA0Sik2rCEFJiL376Swr_PGW06LPugtwZz5fG5f7HMLRQ21T6L8aE3L6_epJiHL3bbJ5neCKRPw53_9XxFuQ1ST8UrvA8oV7IPB-VdvLjvtaydTh5twPpDBvk_OE5jYp-B_kvO4OghX-ZXH4OoENyQaUjhxDiw==', start_index=16162)
Annotation(end_index=16266, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzhWqTOwiVZdR7Iog_JnolhYq_B3GECQMacP9cUPqCDUExJ6OA3cXIZvlgca8ce9XRCL1ACe9e2wkn0_1diduE6f4iPMPQ9sZWpa6hvVwEPuyLU_3dLJgpRtjpNU64ly508PtT5tc=', start_index=16256)
Annotation(end_index=16320, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFIDFAbA2VDj-ZpivLsL6duPIJlyPnFxIyynAfC8_nZGYaZznadTmloyFYlgVZ477cUCOqaC3vYCivmkdHvHp7l1AnORd4M5unn0QFn_CarE_ayDBpgbXyOux3VS3hBxuyKjtQKdXQ_-gT93ijjKTXriRqTXeqc1q-LSXpbqaWIL3Lv8e3Z5en1_p98Y9esNABER06D3zVIAF5lCn6gYAupYQCh_g0CxqKJjQUr3F0S1HOc8-hKVmVtA==', start_index=16311)
Annotation(end_index=16371, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqXpoKp5lkwx5mOhfiKtZnfsPEU0rt2V86GkTMKFlqFJSCeyOVB9gOiUxFS0jV4USrRO1FubtPSBYNMCotzlvgt3QFm308dt7QAyMNlDaGyGBhMJ6Tc0tvroyx4KJzp6gijvjgAzFJuMzhikQ=', start_index=16361)
Annotation(end_index=16414, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlft6gfPLIViVP7Ck3ZGjCPeaG2WtVQNonMsf-IEpzd2o1hy2ny6CImZE7sL8ilIX0o2Tne99Fle34vVhKY6S1C73ozecHAkulYKJSd_KyKsDgmephCkhWdvKr04NS_BK7-WOgZi3SXCJnJEX0c3A_gPt_n3LBAbraJ0iMvzngsk_Wfmhr14ZFrpJWTBx7qr2nQbZUiyFA7w==', start_index=16405)
Annotation(end_index=16464, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZ82BzVjcRy2UlP3VfaA59CJU7GVz3h_cZzKZqL9rDLTeolXa1e8qFa8V9MTDr2E6wjxzfYkWy95xAQjZt8S4VgMNz6MzhOkVCs5ZxKs9c_6sVLE5G-A_KmQgUJrbQqX4Haqgoo_lE2SXEVZA3FddEFJILBfMbjD8Alg8OOvxe', start_index=16455)
Annotation(end_index=16511, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESy-OO5dBEzIPlFZxjmZJNKqg59DoM1wYmhYuTkoQpd-49tbH-P8FPtMXrFJvNrnrhZAz7wZJGQ5jS5KxhhfT-zhGKhK2CJn7ADjeARlkV7AYy9n6u8onBqTZkX3qIatXx8RsVLwO7Vi3o5OPcpHlyPM_U81pX-g==', start_index=16501)
Annotation(end_index=16556, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGocsleNDhTgY_IHHuRWA6-WJRVvHPe8-M-9OC6EYsAPMraRN2vPiBshrgDheGwZtWzMkDaMLpKKab5hIuItXMC0c5mYRvroCE-SQz7L_VBEtPD2bxQEP-8KZyKQPTnXd8xYCOY1B3vdQEQdvpMiKyPpKLBIGHaD61dAyuqhfDGYXfX9SXEMjR4eNUpUnAGOwH0zetXOX4JXczSw==', start_index=16547)
Annotation(end_index=16616, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUmfCq6QQDIK4xFu1UQDv5GCN2MSfRA4PwkKA3SiN2wKMUzl7P6Fo1x0TGZ2zkFKp83Lg_59HBTpP2l67C1EbiexkdE6rYebuMB11pM97w0Fx1TX8twwpOW2Z9ZQ0GLQlB-otKpk_fWZNJK0L9ikuxjw==', start_index=16607)
Annotation(end_index=16670, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZ82BzVjcRy2UlP3VfaA59CJU7GVz3h_cZzKZqL9rDLTeolXa1e8qFa8V9MTDr2E6wjxzfYkWy95xAQjZt8S4VgMNz6MzhOkVCs5ZxKs9c_6sVLE5G-A_KmQgUJrbQqX4Haqgoo_lE2SXEVZA3FddEFJILBfMbjD8Alg8OOvxe', start_index=16661)
Annotation(end_index=16716, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1e7Zqz-dJ1VkxNuNmyJRnZfUjudse4dS2UPbLSXudNzBaOEjIvfn4EF-xJ7npwAOeu1rFgypipoiul7hIi1z5cntQPTKUuOyOusoYButtzV53ggH2PSxY3U-Un9Ng-dTpt4X-CZLLssFcrfYiyxwv4B7Pux3k4XHu14mZkDw_uPISDbf86Rc1AVm458_jjbtXIIo5hrqI-UiWk4SDpIAI1K9VimqC5zkgCxVUevRyy3DCwpk0vyyatinm7sKTScPv5wExYxqaSB7D5U834Bh6h0YOSsJ1W6_jMpNZyPbAoBss3i2aFT1MuEXpfM1OUmAfImqHFh_O7nZbM9CNxURozkYvqFNi1CFuIENA_W-A97nAcyUkDvY=', start_index=16707)

## Sources
