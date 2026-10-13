# Deep Research Report: deepseek/deepseek-r1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 6afff050 | **Time:** 133.83s | **Cost:** $0.10641
--------------------------------------------------------------------------------

## Research Report: Attribution Weight Determination in Purchase Conversion Models  

**Prepared by:** Senior Technical Analyst  
**Date:** October 26, 2023  

---

### 1. Introduction  
Attribution weighting quantifies the contribution of each marketing touchpoint to conversion outcomes. In multi-touch attribution (MTA), weights distribute credit across interactions in complex customer journeys. This report examines methodologies for determining attribution weights, categorizing them into **rule-based** and **data-driven** approaches, based on industry practices and technical literature.  

---

### 2. Rule-Based Attribution Models  
Rule-based models assign fixed weights using deterministic heuristics. Weights are predefined and do not adapt to data patterns.  

#### 2.1 Common Rule-Based Frameworks:  
- **Position-Based (e.g., U-Shaped, W-Shaped, Z-Shaped):**  
  - **Z-shaped attribution** allocates 22.5% each to first touch, lead creation, opportunity creation, and conversion, with 10% distributed to intermediate touchpoints [3].  
  - **U-shaped** assigns 40% to first and last touchpoints, 20% to middle interactions [3].  
- **Time-Decay:** Weights increase exponentially near conversion.  
- **Linear:** Equal weight to all touchpoints.  

#### 2.2 Weight Assignment Rationale:  
- **Business heuristics** prioritize touchpoints deemed strategically significant (e.g., first/last touch for awareness/closing).  
- Custom adjustments incorporate **engagement quality** (e.g., webinar attendance > ad click) [2].  
- **Limitations:** Fails to capture nonlinear journey dynamics or hidden correlations [2][6].  

---

### 3. Data-Driven Attribution Models  
Data-driven models use statistical methods to derive weights from observed conversion paths. Weights reflect empirical impact.  

#### 3.1 Core Methodologies:  
- **Shapley Value (Cooperative Game Theory):**  
  Computes the average marginal contribution of a touchpoint across all possible channel combinations:  
  \[
  \phi_i = \frac{1}{|\mathcal{N}|!} \sum_{R} \left( v(P_i^R \cup \{i\}) - v(P_i^R) \right)
  \]  
  where \(v(S)\) is the conversion probability of subset \(S\), and \(R\) is all permutations of touchpoints [7][9].  
  - **Advantages:** Fairly distributes credit; handles synergy between channels.  
  - **Requirements:** ≥500 conversions/month for reliability [10].  

- **Markov Chains:**  
  Models customer journeys as state sequences. Weight is determined by the **removal effect**:  
  \[
  \text{Weight}_i = 1 - \frac{P(\text{conversion without touchpoint } i)}{P(\text{conversion})}
  \]  
  where \(P\) is path conversion probability [7][8].  
  - **Use Case:** Identifies critical transition points in nonlinear journeys [8].  

- **Fractional/Incremental Attribution:**  
  - **Fractional:** Assigns partial credit via regression/ML on historical paths [3].  
  - **Incremental:** Measures lift from a touchpoint using A/B tests (e.g., conversion rate with/without exposure) [5][11].  

#### 3.2 Machine Learning Enhancements:  
- **Algorithms:** Logistic regression, LASSO (for sparse data), ensemble methods [4], deep learning (LSTM/transformers for non-linear paths) [10].  
- **Training:** Uses features like time-to-conversion, interaction depth, and creative type [9].  
- **Counterfactual Analysis:** Compares real outcomes against simulated paths missing specific touchpoints [9][12].  

---

### 4. Critical Implementation Considerations  

#### 4.1 Data Requirements:  
- **Comprehensive Tracking:** Capture online/offline touchpoints (e.g., UTMs, CRM logs, call tracking) [2][6].  
- **Key Data Points:** Timestamp, engagement depth, content type, channel, account/contact linkage [6].  
- **Sparse Data Mitigation:**  
  - **Entropy-weighted k-means** or **LASSO** prioritize predictive sparse variables [4].  
  - Minimum conversion thresholds (e.g., 400–600/month) ensure model stability [10].  

#### 4.2 Model Selection Criteria:  
- **Journey Complexity:**  
  - Short cycles: Rule-based (last-touch).  
  - B2B/long cycles: Data-driven (Shapley, Markov) or Z-shaped [3][10].  
- **Business Goals:** Align with objectives (e.g., awareness vs. conversion optimization) [1][2].  
- **Computational Cost:** Shapley values scale exponentially with touchpoints; Markov chains require path probability matrices [7][10].  

#### 4.3 Validation & Optimization:  
- **Incrementality Testing:** Validate weights via geo-based or audience-split RCTs [5][11].  
- **Synthetic Controls:** Algorithmically weight unexposed segments to estimate true lift [11].  
- **Continuous Refinement:** Recalibrate weights quarterly using new journey data [1][6].  

---

### 5. Conclusion  
Attribution weights are determined via:  
1. **Rule-based heuristics** for simplicity and strategic alignment.  
2. **Data-driven algorithms** (Shapley, Markov, ML) for accuracy in complex journeys.  
3. **Empirical validation** through incrementality testing.  

**Recommendations:**  
- Use data-driven models for journeys with >8 touchpoints and diverse channels.  
- Combine rule-based frameworks for interpretability with algorithmic refinements.  
- Address data sparsity via LASSO/entropy-weighting and enforce minimum conversion volumes.  
- Validate weights quarterly using RCTs or synthetic controls.  

Future work should explore transformer-based models for non-linear path analysis [10] and privacy-preserving federated learning for offline data integration.  

---  
**Citations:**  
[1] Salesforce (Multi-Touch Attribution Best Practices)  
[2] Hockeystack (Attribution Models)  
[3] Triple Whale (Z-Shaped Attribution)  
[4] University of Colorado (Sparse Data Techniques)  
[5] Measured (Incrementality Guide)  
[6] Hockeystack (Attribution Measurement)  
[7] Statsig (Shapley/Markov Attribution)  
[8] Google Analytics (Data-Driven Attribution)  
[9] Lebesgue (Shapley Value)  
[10] Madgicx (Advanced ML Models)  
[11] Appier (Incrementality Methodologies)  
[12] Rotman School of Management (Rule-Based Limitations)

## Annotations


## Sources
[1] https://arxiv.org/pdf/1804.05327
[2] https://arxiv.org/pdf/2302.06075
[3] https://business.adobe.com/blog/basics/marketing-attribution
[4] https://developers.google.com/ads-data-hub/guides/shapley
[5] https://haus.io/article/meta-incrementality-testing
[6] https://improvado.io/blog/marketing-attribution-models
[7] https://info.measured.com/hubfs/Incrementality%20Measurement%20for%20Marketers%20Guide.pdf
[8] https://lebesgue.io/marketing-attribution/attribution-modeling-methods-a-comprehensive-guide
[9] https://madgicx.com/blog/advanced-machine-learning-models-for-attribution-modeling
[10] https://medium.com/@bhaskarammu/a-machine-learning-approach-to-marketing-attribution-601ca22ac8bd
[11] https://medium.com/@xiaotingkuangcu/machine-learning-based-multi-touch-attribution-models-f95e45f7ab0f
[12] https://support.google.com/analytics/answer/10596866?hl=en
[13] https://www-2.rotman.utoronto.ca/userfiles/brownbags/operations/files/paper_Raghav_Singal.pdf
[14] https://www.appier.com/en/blog/the-incrementality-imperative-a-comparative-analysis-of-measurement-tools
[15] https://www.colorado.edu/business/ms-programs/ms-blog/2023/01/24/data-analytics-best-practices-machiene-learning-sparse-data
[16] https://www.hockeystack.com/blog-posts/different-attribution-models
[17] https://www.hockeystack.com/blog-posts/how-to-measure-marketing-attribution
[18] https://www.leewayhertz.com/ai-powered-dynamic-pricing-solution/
[19] https://www.mdpi.com/2079-9292/9/11/1822
[20] https://www.northbeam.io/blog/introducing-incrementality-by-northbeam-automated-lift-testing-you-can-trust
[21] https://www.owox.com/blog/articles/marketing-attribution-models
[22] https://www.reform.app/blog/what-is-a-machine-learning-attribution-model
[23] https://www.revsure.ai/resources/whitepapers/the-state-of-b2b-marketing-attribution-2025
[24] https://www.salesforce.com/marketing/multi-touch-attribution/
[25] https://www.sentic.io/blog/maximizing-marketing-roi-with-attribution-modelling
[26] https://www.statsig.com/blog/marketing-attribution-models-tech-survey
[27] https://www.triplewhale.com/blog/multi-touch-attribution-models