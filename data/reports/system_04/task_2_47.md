# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 52087e5a | **Time:** 356.41s | **Cost:** $1.80590
--------------------------------------------------------------------------------

# Survival Analysis in Churn Prediction: Balancing Timeliness, Feature Complexity, and Covariate Selection Strategies

### Key Points
*   **Survival Analysis vs. Binary Classification:** Unlike traditional binary classification (e.g., Logistic Regression) which predicts *if* a customer will churn, survival analysis predicts *when*, offering a dynamic view of customer retention and enabling timely interventions based on hazard rates [cite: 1, 2, 3].
*   **The Cox Model Trade-off:** The Cox Proportional Hazards (CPH) model is the industry standard for interpretability but relies on the Proportional Hazards (PH) assumption—that the effect of covariates remains constant over time. In churn contexts, this assumption is frequently violated (e.g., the impact of price sensitivity changes as tenure increases), potentially compromising long-term retention strategies if not corrected [cite: 4, 5].
*   **Covariate Selection Risks:** Improper covariate selection, particularly the omission of time-varying covariates (TVCs) or treating dynamic behaviors as static baseline variables, introduces significant bias. This "overadjustment" or "static bias" can mask early warning signs of churn, leading to retention strategies that are reactive rather than proactive [cite: 6, 7, 8].
*   **Complexity vs. Interpretability:** While machine learning approaches like DeepHit and Random Survival Forests (RSF) handle high feature complexity and non-linear interactions better than Cox models, they often lack the parameter interpretability required to design specific business interventions. Thus, a "compromise" exists where Cox models may sacrifice predictive raw accuracy for causal explainability [cite: 9, 10].

### Executive Summary
The application of survival analysis to customer churn prediction represents a significant methodological advancement over static classification techniques. By modeling the "time-to-event," organizations can balance the timeliness of predictions with the complexity of customer behavior. However, this balance is precarious. The reliance on the Cox Proportional Hazards model introduces specific vulnerabilities regarding covariate selection. Research indicates that when time-varying covariates—such as fluctuating usage patterns or customer sentiment—are excluded or modeled as static, the resulting hazard ratios may be biased. This compromises long-term retention strategies by failing to account for the evolving nature of customer risk. While advanced machine learning survival models address feature complexity and non-linearity, the Cox model remains dominant for its interpretability, provided that rigorous attention is paid to the Proportional Hazards assumption and the integration of time-dependent variables.

---

## 1. Introduction: The Paradigm Shift from "If" to "When" in Churn Prediction

Customer churn prediction has historically been treated as a binary classification problem: will a customer leave within a fixed window (e.g., the next 30 days)? While useful, this approach suffers from a fundamental limitation—it ignores the temporal dynamics of customer behavior and the censoring of data (customers who remain active are effectively invisible to the "churn" class in simple models) [cite: 1, 3].

Survival analysis, originating from biostatistics and reliability engineering, addresses these limitations by modeling the expected duration until an event occurs. In the context of churn, it answers not just *who* is at risk, but *when* that risk is highest [cite: 2, 11]. This shift allows businesses to calculate the Customer Lifetime Value (CLV) with greater precision and deploy retention resources at the specific moments when the "hazard" of churning spikes [cite: 3, 11].

However, the transition to survival analysis introduces new complexities. The mathematical frameworks, particularly the Cox Proportional Hazards model, require strict assumptions about how customer features (covariates) interact with time. The user's query highlights a critical tension: does the algorithm's ability to handle time (timeliness) come at the cost of adequately managing the complex, evolving nature of customer data (feature complexity)? Furthermore, does the process of selecting these covariates introduce biases that undermine the very long-term strategies the model is meant to support?

## 2. The Cox Proportional Hazards Model: Mechanics and Assumptions

To understand the trade-offs in churn prediction, one must first understand the dominant algorithm: the Cox Proportional Hazards (CPH) model.

### 2.1 The Hazard Function and Proportionality
The CPH model estimates the hazard rate \( h(t|X) \), which is the instantaneous probability of churn at time \( t \), given that the customer has survived up to that time. The model is defined as:
\[ h(t|X) = h_0(t) \exp(X\beta) \]
Where:
*   \( h_0(t) \) is the baseline hazard (the risk of churn over time for a customer with all covariates set to zero).
*   \( X \) represents the vector of covariates (features).
*   \( \beta \) represents the coefficients (weights) indicating the impact of each feature [cite: 3].

The critical component here is the **Proportional Hazards (PH) assumption**. It posits that the ratio of hazards between two individuals is constant over time [cite: 5, 10]. For example, if High-Spender A is half as likely to churn as Low-Spender B at month 1, the model assumes A is *still* half as likely to churn as B at month 24, regardless of changes in the baseline risk [cite: 4].

### 2.2 The Interpretability Advantage
The primary reason Cox models remain prevalent in churn prediction, despite the existence of more complex machine learning models, is interpretability. The coefficients \( \beta \) can be directly translated into Hazard Ratios. If the coefficient for "Service Calls" is positive, a business knows that an increase in service calls increases the instantaneous risk of churn by a specific factor [cite: 5]. This direct link between feature and risk is essential for designing retention strategies (e.g., "We must reduce service calls to lower churn risk").

## 3. The Tension: Timeliness vs. Feature Complexity

The user asks if the algorithm balances timeliness and feature complexity. The evidence suggests that while survival analysis excels at timeliness, the standard Cox model struggles with feature complexity, specifically regarding high-dimensional data and non-linear interactions.

### 3.1 Timeliness: The Strength of Survival Analysis
Survival analysis inherently prioritizes timeliness. By generating a survival curve \( S(t) \) and a hazard function \( h(t) \) for each customer, the model provides a temporal roadmap of risk [cite: 3, 12].
*   **Dynamic Risk Profiling:** Unlike logistic regression, which gives a single probability score, survival analysis reveals periods of "increasing, stable, or decreasing churn rates" [cite: 3].
*   **Censoring Handling:** It utilizes data from customers who are still active (right-censored), ensuring that the model learns from the entire customer base, not just those who have already failed. This improves the timeliness of predictions for newer cohorts [cite: 1, 10].

### 3.2 Feature Complexity: The Achilles' Heel
The standard Cox model faces significant challenges when dealing with the complexity of modern customer data:
*   **High Dimensionality:** When the number of covariates is large (e.g., hundreds of behavioral metrics), standard Cox models can overfit or fail to converge. Variable selection methods like LASSO (Least Absolute Shrinkage and Selection Operator) are often required to reduce complexity, but this reduction can discard subtle signals necessary for long-term prediction [cite: 13, 14, 15].
*   **Non-Linearity:** The standard Cox model assumes a log-linear relationship between covariates and the hazard. However, customer behavior is often non-linear (e.g., extremely low *and* extremely high usage might both indicate churn risk). Capturing these patterns requires complex feature engineering or advanced extensions that compromise the model's simplicity [cite: 9].

## 4. Covariate Selection and the Compromise of Long-Term Strategies

The core of the inquiry is whether covariate selection in Cox models compromises long-term retention. Research strongly suggests that **yes, improper covariate selection—specifically the treatment of dynamic variables as static—compromises long-term accuracy.**

### 4.1 The Static Covariate Fallacy
In many implementations, analysts take a snapshot of customer data at the time of subscription (baseline covariates) and use this to predict churn years into the future.
*   **The Problem:** Customer characteristics change. A customer who was "High Value" at signup may become "Low Engagement" by month 6.
*   **The Consequence:** The PH assumption is violated. The effect of the baseline variable "High Value" diminishes or reverses over time. If the model assumes this effect is constant (proportional), it will overestimate retention probability in the long term [cite: 16, 17].
*   **Example:** Research in dialysis survival (analogous to customer survival) showed that "underweight" was a risk factor in the short term, but "overweight" was a risk factor in the long term. A standard Cox model averaging these effects would fail to identify the correct risk factors for long-term survivors [cite: 16]. In churn, a discount might prevent churn in month 1 (negative coefficient) but be associated with bargain-hunters who churn in month 12 (positive coefficient).

### 4.2 Overadjustment and Endogeneity Bias
When selecting covariates, there is a risk of "overadjustment bias" if one controls for variables that are actually intermediate steps in the causal path to churn [cite: 8].
*   **Internal Covariates:** These are variables generated by the customer over time (e.g., "Recent Login Activity"). They are "internal" because they are tied to the customer's survival status [cite: 6, 18].
*   **The Compromise:** If a model excludes these time-varying internal covariates to satisfy the simplicity of a standard Cox model, it misses the immediate precursors to churn (the "disengagement" phase). Conversely, if it includes them without proper time-dependent modeling, it introduces bias because the covariate value depends on the customer not having churned yet [cite: 6, 19].

### 4.3 Variable Selection Methods (LASSO/Elastic Net)
To handle complexity, researchers use penalized regression (Cox-LASSO). While this selects the most predictive variables, it prioritizes "data fitting" over "causal validity" [cite: 14, 20].
*   **Instability:** The set of genes (or customer features) selected can vary wildly based on the sample, meaning the "key drivers" identified for strategy might be artifacts of the specific dataset rather than robust behavioral drivers [cite: 21].
*   **Compromise:** This instability makes it difficult to build a consistent long-term retention strategy, as the "most important" features keep shifting with every model retrain.

## 5. Time-Varying Covariates (TVCs): The Solution and Its Costs

To address the limitations of static covariate selection, the **Extended Cox Model** allows for Time-Varying Covariates (TVCs). This approach balances timeliness and complexity but introduces high computational and data costs.

### 5.1 The Necessity of TVCs in Churn
In churn prediction, the most predictive signals are often recent behavioral changes (e.g., a sudden drop in usage or a spike in support tickets).
*   **Dynamic Prediction:** TVCs allow the hazard rate to update as the customer's behavior changes. A customer is not assigned a single risk score at birth; their risk score evolves daily/monthly [cite: 3, 4].
*   **Violation Resolution:** Using TVCs resolves the violation of the Proportional Hazards assumption. Instead of assuming the effect of "Spend" is constant, the model evaluates "Current Spend" at each time point [cite: 4].

### 5.2 The "Compromise" of TVCs
While TVCs improve accuracy, they complicate the analysis:
*   **Data Structure:** Data must be transformed into a "counting process" format (start-stop intervals), significantly increasing the size of the dataset and computational processing time [cite: 3, 18, 22].
*   **Prediction Difficulty:** To predict churn 12 months out using TVCs, one must *forecast* the values of those covariates for the next 12 months. If you cannot accurately predict a customer's future usage, you cannot use "future usage" as a covariate in a standard survival prediction model for long-term horizons [cite: 23].
*   **Strategic Ambiguity:** It becomes harder to say "Feature X causes churn" when Feature X is constantly changing. The strategy shifts from "Target customers with attribute X" to "Target customers *when* attribute X drops below Y" [cite: 16].

## 6. Machine Learning Alternatives: Accuracy vs. Explainability

Given the difficulties with Cox models (PH assumption, TVC complexity), Machine Learning (ML) survival models have emerged.

### 6.1 Random Survival Forests (RSF) and DeepHit
*   **Random Survival Forests:** These handle non-linear interactions and high-dimensional data automatically without the strict assumptions of Cox models. They have been shown to capture patterns in churn data better than Cox regression when non-linearities exist [cite: 9].
*   **DeepHit:** A deep learning approach that learns the distribution of survival times directly. It outperforms Cox models in complex datasets (e.g., competing risks) and does not require the PH assumption [cite: 10, 24].

### 6.2 The Trade-off
*   **Performance:** Studies show ML models (DeepHit, XGBoost) often achieve higher Concordance Indices (C-index) and better calibration than Cox models, especially in large datasets [cite: 10, 25].
*   **Interpretability Gap:** The "compromise" here is interpretability. A DeepHit model might predict churn time accurately, but it cannot easily tell a marketing manager *why* a specific cohort is at risk or what the Hazard Ratio of a specific intervention is [cite: 5, 10]. For long-term strategy, understanding the *mechanism* (provided by Cox) is often as valuable as the prediction itself.

## 7. Strategic Implications for Retention Strategies

The choice of algorithm and covariate selection method directly impacts business strategy.

### 7.1 Misleading Retention Allocations
If a Cox model is used with static covariates that violate the PH assumption, the model might flag "High Tenure" customers as "Safe" (based on historical averages) even if their recent behavior indicates high risk. This leads to under-investment in retaining valuable, long-term customers who are showing early signs of decay [cite: 4].

### 7.2 The "Timeliness" of Intervention
Survival analysis allows for **Time-Dependent ROC** analysis and dynamic risk stratification. Businesses can identify the specific month (e.g., Month 9) where the hazard spikes and implement an intervention at Month 8. This is a strategic advantage over binary models that simply flag "Churn Likely" without a temporal component [cite: 11, 26].

### 7.3 Balancing the Portfolio
To avoid compromising long-term strategy, organizations often use a hybrid approach:
1.  **Cox Models (with TVCs):** Used for *inference*—to identify which features are statistically significant drivers of churn risk [cite: 3, 5].
2.  **ML Models (RSF/DeepHit):** Used for *prediction*—to generate the most accurate individual risk scores for targeting [cite: 9, 10].

## 8. Conclusion

Does the survival analysis algorithm balance timeliness and feature complexity? **Yes, but with significant caveats.** Survival analysis inherently solves the timeliness problem by modeling time-to-event. However, the standard Cox model struggles with feature complexity.

Does covariate selection in Cox models compromise long-term retention strategies? **Yes, it frequently does.** The compromise occurs in two ways:
1.  **Assumption Violation:** By forcing dynamic customer behaviors into static covariates to fit the Proportional Hazards assumption, models produce biased hazard ratios that misinform long-term strategy [cite: 4].
2.  **Omission of Dynamics:** Omitting time-varying covariates to simplify the model leads to "overadjustment bias" or missed signals of disengagement, causing the model to fail exactly when it is needed most—in the long-term prediction of customer lifecycles [cite: 6, 7].

Therefore, while survival analysis is superior to binary classification for churn, the **Cox model specifically requires rigorous validation of the PH assumption and the inclusion of time-varying covariates** to avoid compromising long-term retention strategies. Without these adjustments, the model's "timeliness" is based on flawed "feature" assumptions.

## References
*   **[cite: 1]** Proove Intelligence. (n.d.). *Understanding customer churn with survival analysis*.
*   **[cite: 9]** Exploratory.io. (2021). *Cohort Analysis - Analyzing What Makes Customers Churn with Survival/Prediction Models*.
*   **[cite: 23]** Stack Exchange. (2011). *Survival model for predicting churn - time varying predictors*.
*   **[cite: 10]** Singh, K. (2024). *Survival-Based Predictive Analytics for Customer Churn*.
*   **[cite: 3]** RStudio Pubs. (n.d.). *Survival Analysis in Churn Prediction*.
*   **[cite: 2]** Fabi.ai. (2024). *Why use survival analysis for churn prediction*.
*   **[cite: 13]** PMC. (2024). *Robust variable selection approaches for the Cox model*.
*   **[cite: 6]** EuroIntervention. (2014). *Dealing with time-varying covariates in survival analysis*.
*   **[cite: 21]** Stack Exchange. (2019). *How to choose the best combination of covariates in Cox multiple regression*.
*   **[cite: 27]** arXiv. (2023). *Controlled Feature Selection using Knockoffs for the Cox Model*.
*   **[cite: 10]** Singh, K. (2024). *Evaluating Classical and Neural Network Models*.
*   **[cite: 25]** Kaggle. (2023). *Survival Models VS Machine Learning Models Benchmark*.
*   **[cite: 20]** PMC. (2016). *Comparison of variable selection methods for Cox models*.
*   **[cite: 5]** ResearchGate. (n.d.). *Customer Churn Analysis in Telecom Industry using Kaplan-Meier and Cox*.
*   **[cite: 4]** Medium. (2023). *Unpacking churn with survival models*.
*   **[cite: 23]** Stack Exchange. (2011). *Survival model for predicting churn - time varying predictors*.
*   **[cite: 19]** PMC. (2019). *Time-varying covariates in subdistribution hazard models*.
*   **[cite: 28]** GraphPad. (n.d.). *Survival Analysis Guide*.
*   **[cite: 12]** PMC. (n.d.). *Survival analysis in cardiovascular nursing*.
*   **[cite: 29]** Falcon Editing. (2023). *Survival Analysis: Understanding Time-to-Event Data*.
*   **[cite: 22]** YouTube. (2025). *Interpreting Time-dependent Covariates In Survival Analysis*.
*   **[cite: 16]** PubMed. (2008). *Survival analysis: time-dependent effects and time-varying risk factors*.
*   **[cite: 17]** ResearchGate. (2025). *Survival analysis: Time-dependent effects and time-varying risk factors*.
*   **[cite: 26]** BMJ Open Respiratory Research. (2026). *Prognostic significance of systemic inflammation in pulmonary embolism*.
*   **[cite: 14]** medRxiv. (2025). *Covariate selection in Cox-LASSO regression*.
*   **[cite: 15]** ResearchGate. (2023). *Variable Selection for Cox's Regression Model*.
*   **[cite: 9]** Exploratory.io. (2021). *Random Survival Forest vs Cox*.
*   **[cite: 5]** ResearchGate. (n.d.). *Impact of proportional hazards assumption*.
*   **[cite: 3]** RStudio Pubs. (n.d.). *Advantages of survival analysis in churn prediction*.
*   **[cite: 11]** CMI Research. (n.d.). *Churn Survival Analysis 101*.
*   **[cite: 4]** Medium. (2023). *Unpacking churn with survival models*.
*   **[cite: 18]** PMC. (2018). *Time-varying covariance in Cox regression*.
*   **[cite: 7]** PMC. (2022). *Bias in time-varying drug exposures*.
*   **[cite: 8]** PMC. (2024). *Overadjustment bias in PK/PD modeling*.
*   **[cite: 10]** DiVA Portal. (2024). *DeepHit vs Cox in Churn*.
*   **[cite: 24]** AAAI. (2018). *DeepHit: A Deep Learning Approach to Survival Analysis*.

**Sources:**
1. [prooveintelligence.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAK_HF2hA1sJoOr-XRwWLmfUyyhg99zDf3kfSJW1Mmk-xBHKpM_QdyOAakMGdIGNy2itPwLP9JN-qaoDN1glzIIYd1OG7OT3K_I916WfiEeqNYrQeBv46hNh_o_KgQJuS_yEjuuBN9grzF2dBtB1HInu7P_uaoAcQmT3ooxRM7qNnqrpcI8DmD7XIfZc7p-kLXfw==)
2. [fabi.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8h3VylLsMVz9uNdoflQ0-0ge_cxeR_J1MwlCde_hB6paQtA4HIhF9YrXfkiMJz3ivxA_0owp1alVJagZ54cWRyj_2-w2OanNXiv38f8pq_Y8PwRlWml7-YPP50ySORtCz1uwilWuqFGIdWzfe37cd9ZDGyqNdMi7EPvLg7-MD7gn3vpeGkHp42fSrVvuVL2zrEDetAw==)
3. [amazonaws.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHemG3Om-6wMSQj9tH8CDbacQgTwJ2cmq_2e8sMSSy0zHhJzqFU1Pyl8xCUtNMJc_U1fa4PrDHr_DIi0WDBTufQeRoxODf3VtQrcjJuSOmvaYgjpmS6pDf_OmO66a5iKduVdorrm9-5j4OtBFq8r5aQ5Eudyv9mBOIA1quob2Nbxi-1eDqvZFA7iYtNIe0xw==)
4. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHx2Iqto76lJEEoUnamVVI23ll0FLwHc-9N32Suyzih1F_w8QK3esmrCsCpNI5ZeQE0WgDxAG54vBoTo6gSLvAZ-O5vyIrnnVQDRuF2dx-NhrFdiIh_Vy2HZRPYODuEqGt0YiDykaZFQsLoLqWwuiPZIDyxVU0YeDrpUC7lJxD8XZZePuW5CsNOCHTN2vmhs9kFuikw)
5. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBdzaJ4fYSgeUQSerHSuGcpR99yOWyYoPqO7PjyTO8ymvGMJlkgQB1QrnxNzOoSiwaOjQOP2McXfpoBrKw8UWebS_a3hMqJTE3_Fhve6_a2wrNmxIpO0dWoJ-VjZ4YB33dZd_v_6iAXMu0ZX9dQV_E5PAIL-4ryt_nKdqXiBmfCNlwHI9B4e4vz7kPUAhQ3lAlW_He4AAk2QTpkkrwcSTQ7XGGW0EI5D86kIMOE5w6ykI6u0k90bCPwUSUuurDC-XY1YgKHhCrGk8G6Q==)
6. [pcronline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGd9Izqh-cYLDIj4WAVLuYJbvspAysTwmbOsOFsJRR8OM6n0bxDkSzuWZEAebrYK-KfBreptj5cCGr5RnSZ2FMgVWmtM4HIfZID47iAGYG_angokJSzqd4lKzN6FxEKwwXhRQ-4brR5Tt7rkgVyyRfnM04OvMIRtsuXMmSC4O6ePxM9TGe3uFGR8dVzm950eW3NPNZ_mzm73MB7kewpYsdT3LuBD6i3TMNlXl1KcPdYEupYDCbmMnMnpg-PicZeHIL98wWbyDwhlul-K1v70tkpXuHgz4ymnfUHKBJPWjs=)
7. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDvAk9R5F8FxWry1FPV_GMiQU0eRod5CxlwhIwmUxjW2bUEt3x3gIofOcAOnV0l18Iy3wbrO3DyQmNrxG9NkV7r1Gdgx4j-AV1ff_6jONH88_6e3PdM5atomQsSdu1Zhk32gfZbSW3)
8. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSRqr77SuDZhUKdP8Ewo_t4TuG1NP1bkC-Ugb8ANdwU7fkJhjyomxcSFOQa9RL8jI8DUKi5OTbbB68f-SiRr_bvW05X_UdbLDuUoKc4BNQdAXW3rGg7Xk96WzdDj6vq0G9Zji-DHwsDQ==)
9. [exploratory.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZxUGYYRURQAamKhdXIV5rWievVCmYXXvl5xqiZ5Vu0xh28TYVo_Fk6DRYAg_TFcEyzGg3EQJwpC1psPfchCJ6_M6Sao7OlstrPgSNaRki_D75a9WeHFr5xv6A8i8SquMBPFK5U398EDPbRkhs8SQvbCYTGWmYxByypepZJeSOMj9wKy7Dig==)
10. [diva-portal.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTtws1BUhN3j6Pv2PTcsAtfpLP5ui-71X1ExihDGtqZwde3qO9uF8f1aEogd7VFvI_V2beV3xSXrfIGzaZve4gbZV8D-1PGwKRyeqn-5_2MkDUVMay3jzsRVMxMBCHJId0QFisolpaG3xhcNRC5Rqedr6ECbNspQ==)
11. [cmiresearch.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnnNPnYwDsIg6b8SBtqMoutA3Y6x2LQGug6zIaq0YdjOXG3K1F4VO5KgN1LX8gFjPmTbyX_jQR22xd7t3xTiIKR_2exPQxTcB0X4i3U6BmVXEpqkX0We4qZe6J6h3dovFiogoguAV1d65cd-C5N4k8jqgdfVYHYCg=)
12. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7IbqBgSkw9kvu5hqC2pvoCnaXBK5w2xgH4KkWoIDdpPbvGwyeVLRZiBYlL1DdnqJ23t5_dNAfTtSywQn0ua62g4RZNhBezBwt3NHwxBqdkfxK22hDq1o8zWB8Wzvo0Nd3wtJcK_1ULA==)
13. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHefQIOAZSwWtk4_1tQLQGuZ5dkjLEcO3VyFxdQsdl5GdrunzbmPef0yKIUQhmBC7B9vHsikcM9v1TiS3hfmjDBYkRDhVznC_5vvlj4pnkA6AEVd9o51eoUCrsCwrfGYOr-HRb8N_KZMg==)
14. [medrxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQnVbzncRWvOwE5jO1LHAAkmoVWOPhzNRK9m5UU_uW4lmmE6LP-0sumD2GyPxLjdYXm-3avdaraq_FS3NqnIHKDK7M7eHC2xZeO-Ukro5uP6QmFG_8V9QsktQtIlmo3wgsXfh-wFg61BDa-BCPdNJqgFf-m3KdGSeTsOg08gA=)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpCJZq-b6-GDNYI8Nuz1IqHGYqpDS6GHtk0pm3N2WyzAPrDkE38erK9RBz_WmNtutJePc4jI_J1j8K882Oo0T0jSgRJkvVSo8kfOXFrX9Xs5I8BzJXR0zBERm-hPbije3NN09OOTR7V8DM8Onn2YVMg1YIVaqQ5PzjNhbwRGP4dAIfAydNIHY7nw7aZejj8dxsTPycx7GasjAvN3dli_PBHznwAgaSoG-O0BIGjL-ItgIqXvrTkn3I)
16. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaJQdQScxlFKuBDq3bhPmZYzTM468kdnBpgojlDRNlvUlE9lLWjAJE6N9SwrYZxXkh9vWnlieLTpJVRv95E73UrNeIPA10GUBtesE4s2lh_n60SpTjzPtwtzove9LKig==)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRfqBWCvoL9AqYpR_0Q-0w2OGzfD05bR5Q5R1hNyI7Gd3dUCG721H5iQOSVpdnfFsTLfKZNYzYs9Zd3Z8-oKc3UzockCOaQy4chkY9WUDJ2AXSkNHgcuE6YDtVzpMm2RUgytHVbjCu_vOC7_dGZqFLe-YE4cyFsxVyoyPzoQ2w4FpZlaUe38xyqf8qcnZ_3nex0d6RHLsQLAEO1ClM9k2cOnVeLLNwsCopZ_Pgsgg=)
18. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9Ah4VFJBSWqi7hJcnUTBx7WrD2ovZzs3SjGX8giX8_i7bvmiP2jbg4by1kT7Zn5gu86SRoDvtLvMs3Ayk7MygSpPIRFibyNaApZecLucrDVourYofq_6SU3KSgt4nVfEr2dnQUVGn)
19. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKUoKqCybCb_SmzE6Kx2IJ5XuvzI2sgQHOVyn63ipYIv_-6Loj1tU2FwxGYciU7eBu8GvG58x9mypFvjHAXwhlSe7fHR7IExmJ5gJtFE_kMKiu02zgfWBIxVSfIUvvZUlg3DswqY1M)
20. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQ_NLoFAlvbkIwLnojiFrhFPXHRdcT1uLrUsHIjI2uSJ1XLqpCVjavfT1CWT0knsOikI9y1llwzkYB6BNgJ0R0dNBnx_kCwewidVXXDJcY1H8-p_gDUMiPb-EcE9TpWEzv27cZxf4j)
21. [stackexchange.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0f87_GlxSj62HgLnMia1UBNuASJ-JoxhVOSZoPURAUG-pfD-mhoQL2isyjyJLuZL1IJzzkZ_5Vb5yAQ1nyDsR4iMVHnDIgivdTyyLIV1pD-fwpcewVfn7wud3kTUwkoJItLZFz1OPAL56xep0qA_uQdTHcpVGrryArlCQBUeMNvWG3EzzG9llS4QHzpbSCO8bT_5ITBUNhKiuTO8-4f-vy2HlCueSjnM7Yc7lbK4jLg8d)
22. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2MyvmszPhat3jQgfcwcUXt6r54JGhoEPjcvaAatLb7KUAA3cvtNtMLtr8V-5v9Do2HIhqMh4MNPE2NcbcgmUOGYSSOmwTKt-wmE0Hqfb37X5Uh4C5Zd6ENtqnkm3JvDdI)
23. [stackexchange.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzP4s5RvutZykuSbBtITj19ZkcytCPm4owRHGBYeSeSY4z6tWLDC3MgiCO9qkSP8E_lzO6zryuihcM9FVDVnCNyXVgu56kxa995iATeH7wVtI_ajaDGHCA25N32jwwdnINImHa68wPmNBut65HrjF6fG5lN8dVYqOsMr6YbVZcKZxzJXl0xeANPGMOVg502oEJtfVNsizJBviARbtDK125)
24. [ucla.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGH3hAMqgKg8Sr1QXk_XuJxG-R2ClzoJ_BPUm8-Ssm8OX5BRZErdWbY17YNHQZ_LqDcqCD15vA2oWmOyeYVDl5zTn2UaT5p2m0izbhWll1vhwUi3bpByklqvEmDlCpIMB7avuHwbP_TFRG0KUsx)
25. [kaggle.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEKs-JrOCwnp9SG3zJITT_-ddrkCGiIEKI89j8lXl5kuIhQZeA5XRg2rvsoTRtZtICb1rlDMi3iWp774n59gu4VFLH_gvZNEIRfwzGDoxTLCpGum8YNwbknphN_bBeI6Mop5nUyzXJF2_spUGsTkMWCJgQUXa4ZaYKPMtDAky7SsWQFsiKAbrNzuKBMQ==)
26. [bmj.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfq0pFTggNNNjlRCYuh806HmtkJHn3j6ZdKsJgVQGXH9yAvUKOin7wXUv0sKQAUP_BmnFnvvIcFK1ShoCVnGyLT0aDwihzvMqu0yHeHxYCQ9YV0kfzxFyKJGn6ymL-Pb9QMPqJM2MZCPQ=)
27. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfQGSBrc5cuJun4bIhs4NjP3fLmMxiQJytZTy1GpYNzAMTmaET9K3wo6krnUD3PmIthNfuTqziOlVYyZTotVMrRHZaUurnDM9H2jjNskHlXzF_t8bWKA==)
28. [graphpad.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzx50KU6bhmo0Zzxx-T9ImXwWz0JF_muR9RxV2W2X87qQRHP_719qK6dcqu3sanj0I29LX_nk2mZnEefiVIuS6cD1SRP6HBtZc2-XnNSTK-bQ2iElJ54QOJgIwGltGbt-QGcP_m9UF)
29. [falconediting.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYC88BMUkW4rqXIiYbPqYQdyx-thbz5oYJPYq90ZSwXHYw0EcXj-H-HO0IK8jxgoxYhCzEa2bKCmAT4Da2Fr5UvPcavmMd78TJhU2fJRBE6PaHcX0gzKL0CUv0Q938TL5-07UMqtKmE0ZfbfcvtS4QCpol2okAIqw2KhiuGT_0mIIBsmtXnvfx0G-q_Xku7i6yoPqAIMmx)


## Annotations
Annotation(end_index=451, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAK_HF2hA1sJoOr-XRwWLmfUyyhg99zDf3kfSJW1Mmk-xBHKpM_QdyOAakMGdIGNy2itPwLP9JN-qaoDN1glzIIYd1OG7OT3K_I916WfiEeqNYrQeBv46hNh_o_KgQJuS_yEjuuBN9grzF2dBtB1HInu7P_uaoAcQmT3ooxRM7qNnqrpcI8DmD7XIfZc7p-kLXfw==', start_index=436)
Annotation(end_index=451, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHemG3Om-6wMSQj9tH8CDbacQgTwJ2cmq_2e8sMSSy0zHhJzqFU1Pyl8xCUtNMJc_U1fa4PrDHr_DIi0WDBTufQeRoxODf3VtQrcjJuSOmvaYgjpmS6pDf_OmO66a5iKduVdorrm9-5j4OtBFq8r5aQ5Eudyv9mBOIA1quob2Nbxi-1eDqvZFA7iYtNIe0xw==', start_index=436)
Annotation(end_index=451, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8h3VylLsMVz9uNdoflQ0-0ge_cxeR_J1MwlCde_hB6paQtA4HIhF9YrXfkiMJz3ivxA_0owp1alVJagZ54cWRyj_2-w2OanNXiv38f8pq_Y8PwRlWml7-YPP50ySORtCz1uwilWuqFGIdWzfe37cd9ZDGyqNdMi7EPvLg7-MD7gn3vpeGkHp42fSrVvuVL2zrEDetAw==', start_index=436)
Annotation(end_index=900, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBdzaJ4fYSgeUQSerHSuGcpR99yOWyYoPqO7PjyTO8ymvGMJlkgQB1QrnxNzOoSiwaOjQOP2McXfpoBrKw8UWebS_a3hMqJTE3_Fhve6_a2wrNmxIpO0dWoJ-VjZ4YB33dZd_v_6iAXMu0ZX9dQV_E5PAIL-4ryt_nKdqXiBmfCNlwHI9B4e4vz7kPUAhQ3lAlW_He4AAk2QTpkkrwcSTQ7XGGW0EI5D86kIMOE5w6ykI6u0k90bCPwUSUuurDC-XY1YgKHhCrGk8G6Q==', start_index=888)
Annotation(end_index=900, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHx2Iqto76lJEEoUnamVVI23ll0FLwHc-9N32Suyzih1F_w8QK3esmrCsCpNI5ZeQE0WgDxAG54vBoTo6gSLvAZ-O5vyIrnnVQDRuF2dx-NhrFdiIh_Vy2HZRPYODuEqGt0YiDykaZFQsLoLqWwuiPZIDyxVU0YeDrpUC7lJxD8XZZePuW5CsNOCHTN2vmhs9kFuikw', start_index=888)
Annotation(end_index=1281, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDvAk9R5F8FxWry1FPV_GMiQU0eRod5CxlwhIwmUxjW2bUEt3x3gIofOcAOnV0l18Iy3wbrO3DyQmNrxG9NkV7r1Gdgx4j-AV1ff_6jONH88_6e3PdM5atomQsSdu1Zhk32gfZbSW3', start_index=1266)
Annotation(end_index=1281, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSRqr77SuDZhUKdP8Ewo_t4TuG1NP1bkC-Ugb8ANdwU7fkJhjyomxcSFOQa9RL8jI8DUKi5OTbbB68f-SiRr_bvW05X_UdbLDuUoKc4BNQdAXW3rGg7Xk96WzdDj6vq0G9Zji-DHwsDQ==', start_index=1266)
Annotation(end_index=1281, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGd9Izqh-cYLDIj4WAVLuYJbvspAysTwmbOsOFsJRR8OM6n0bxDkSzuWZEAebrYK-KfBreptj5cCGr5RnSZ2FMgVWmtM4HIfZID47iAGYG_angokJSzqd4lKzN6FxEKwwXhRQ-4brR5Tt7rkgVyyRfnM04OvMIRtsuXMmSC4O6ePxM9TGe3uFGR8dVzm950eW3NPNZ_mzm73MB7kewpYsdT3LuBD6i3TMNlXl1KcPdYEupYDCbmMnMnpg-PicZeHIL98wWbyDwhlul-K1v70tkpXuHgz4ymnfUHKBJPWjs=', start_index=1266)
Annotation(end_index=1709, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTtws1BUhN3j6Pv2PTcsAtfpLP5ui-71X1ExihDGtqZwde3qO9uF8f1aEogd7VFvI_V2beV3xSXrfIGzaZve4gbZV8D-1PGwKRyeqn-5_2MkDUVMay3jzsRVMxMBCHJId0QFisolpaG3xhcNRC5Rqedr6ECbNspQ==', start_index=1696)
Annotation(end_index=1709, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZxUGYYRURQAamKhdXIV5rWievVCmYXXvl5xqiZ5Vu0xh28TYVo_Fk6DRYAg_TFcEyzGg3EQJwpC1psPfchCJ6_M6Sao7OlstrPgSNaRki_D75a9WeHFr5xv6A8i8SquMBPFK5U398EDPbRkhs8SQvbCYTGWmYxByypepZJeSOMj9wKy7Dig==', start_index=1696)
Annotation(end_index=3263, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAK_HF2hA1sJoOr-XRwWLmfUyyhg99zDf3kfSJW1Mmk-xBHKpM_QdyOAakMGdIGNy2itPwLP9JN-qaoDN1glzIIYd1OG7OT3K_I916WfiEeqNYrQeBv46hNh_o_KgQJuS_yEjuuBN9grzF2dBtB1HInu7P_uaoAcQmT3ooxRM7qNnqrpcI8DmD7XIfZc7p-kLXfw==', start_index=3251)
Annotation(end_index=3263, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHemG3Om-6wMSQj9tH8CDbacQgTwJ2cmq_2e8sMSSy0zHhJzqFU1Pyl8xCUtNMJc_U1fa4PrDHr_DIi0WDBTufQeRoxODf3VtQrcjJuSOmvaYgjpmS6pDf_OmO66a5iKduVdorrm9-5j4OtBFq8r5aQ5Eudyv9mBOIA1quob2Nbxi-1eDqvZFA7iYtNIe0xw==', start_index=3251)
Annotation(end_index=3538, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnnNPnYwDsIg6b8SBtqMoutA3Y6x2LQGug6zIaq0YdjOXG3K1F4VO5KgN1LX8gFjPmTbyX_jQR22xd7t3xTiIKR_2exPQxTcB0X4i3U6BmVXEpqkX0We4qZe6J6h3dovFiogoguAV1d65cd-C5N4k8jqgdfVYHYCg=', start_index=3525)
Annotation(end_index=3538, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8h3VylLsMVz9uNdoflQ0-0ge_cxeR_J1MwlCde_hB6paQtA4HIhF9YrXfkiMJz3ivxA_0owp1alVJagZ54cWRyj_2-w2OanNXiv38f8pq_Y8PwRlWml7-YPP50ySORtCz1uwilWuqFGIdWzfe37cd9ZDGyqNdMi7EPvLg7-MD7gn3vpeGkHp42fSrVvuVL2zrEDetAw==', start_index=3525)
Annotation(end_index=3744, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHemG3Om-6wMSQj9tH8CDbacQgTwJ2cmq_2e8sMSSy0zHhJzqFU1Pyl8xCUtNMJc_U1fa4PrDHr_DIi0WDBTufQeRoxODf3VtQrcjJuSOmvaYgjpmS6pDf_OmO66a5iKduVdorrm9-5j4OtBFq8r5aQ5Eudyv9mBOIA1quob2Nbxi-1eDqvZFA7iYtNIe0xw==', start_index=3731)
Annotation(end_index=3744, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnnNPnYwDsIg6b8SBtqMoutA3Y6x2LQGug6zIaq0YdjOXG3K1F4VO5KgN1LX8gFjPmTbyX_jQR22xd7t3xTiIKR_2exPQxTcB0X4i3U6BmVXEpqkX0We4qZe6J6h3dovFiogoguAV1d65cd-C5N4k8jqgdfVYHYCg=', start_index=3731)
Annotation(end_index=5133, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHemG3Om-6wMSQj9tH8CDbacQgTwJ2cmq_2e8sMSSy0zHhJzqFU1Pyl8xCUtNMJc_U1fa4PrDHr_DIi0WDBTufQeRoxODf3VtQrcjJuSOmvaYgjpmS6pDf_OmO66a5iKduVdorrm9-5j4OtBFq8r5aQ5Eudyv9mBOIA1quob2Nbxi-1eDqvZFA7iYtNIe0xw==', start_index=5124)
Annotation(end_index=5308, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBdzaJ4fYSgeUQSerHSuGcpR99yOWyYoPqO7PjyTO8ymvGMJlkgQB1QrnxNzOoSiwaOjQOP2McXfpoBrKw8UWebS_a3hMqJTE3_Fhve6_a2wrNmxIpO0dWoJ-VjZ4YB33dZd_v_6iAXMu0ZX9dQV_E5PAIL-4ryt_nKdqXiBmfCNlwHI9B4e4vz7kPUAhQ3lAlW_He4AAk2QTpkkrwcSTQ7XGGW0EI5D86kIMOE5w6ykI6u0k90bCPwUSUuurDC-XY1YgKHhCrGk8G6Q==', start_index=5295)
Annotation(end_index=5308, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTtws1BUhN3j6Pv2PTcsAtfpLP5ui-71X1ExihDGtqZwde3qO9uF8f1aEogd7VFvI_V2beV3xSXrfIGzaZve4gbZV8D-1PGwKRyeqn-5_2MkDUVMay3jzsRVMxMBCHJId0QFisolpaG3xhcNRC5Rqedr6ECbNspQ==', start_index=5295)
Annotation(end_index=5522, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHx2Iqto76lJEEoUnamVVI23ll0FLwHc-9N32Suyzih1F_w8QK3esmrCsCpNI5ZeQE0WgDxAG54vBoTo6gSLvAZ-O5vyIrnnVQDRuF2dx-NhrFdiIh_Vy2HZRPYODuEqGt0YiDykaZFQsLoLqWwuiPZIDyxVU0YeDrpUC7lJxD8XZZePuW5CsNOCHTN2vmhs9kFuikw', start_index=5513)
Annotation(end_index=5967, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBdzaJ4fYSgeUQSerHSuGcpR99yOWyYoPqO7PjyTO8ymvGMJlkgQB1QrnxNzOoSiwaOjQOP2McXfpoBrKw8UWebS_a3hMqJTE3_Fhve6_a2wrNmxIpO0dWoJ-VjZ4YB33dZd_v_6iAXMu0ZX9dQV_E5PAIL-4ryt_nKdqXiBmfCNlwHI9B4e4vz7kPUAhQ3lAlW_He4AAk2QTpkkrwcSTQ7XGGW0EI5D86kIMOE5w6ykI6u0k90bCPwUSUuurDC-XY1YgKHhCrGk8G6Q==', start_index=5958)
Annotation(end_index=6715, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7IbqBgSkw9kvu5hqC2pvoCnaXBK5w2xgH4KkWoIDdpPbvGwyeVLRZiBYlL1DdnqJ23t5_dNAfTtSywQn0ua62g4RZNhBezBwt3NHwxBqdkfxK22hDq1o8zWB8Wzvo0Nd3wtJcK_1ULA==', start_index=6702)
Annotation(end_index=6715, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHemG3Om-6wMSQj9tH8CDbacQgTwJ2cmq_2e8sMSSy0zHhJzqFU1Pyl8xCUtNMJc_U1fa4PrDHr_DIi0WDBTufQeRoxODf3VtQrcjJuSOmvaYgjpmS6pDf_OmO66a5iKduVdorrm9-5j4OtBFq8r5aQ5Eudyv9mBOIA1quob2Nbxi-1eDqvZFA7iYtNIe0xw==', start_index=6702)
Annotation(end_index=6911, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHemG3Om-6wMSQj9tH8CDbacQgTwJ2cmq_2e8sMSSy0zHhJzqFU1Pyl8xCUtNMJc_U1fa4PrDHr_DIi0WDBTufQeRoxODf3VtQrcjJuSOmvaYgjpmS6pDf_OmO66a5iKduVdorrm9-5j4OtBFq8r5aQ5Eudyv9mBOIA1quob2Nbxi-1eDqvZFA7iYtNIe0xw==', start_index=6902)
Annotation(end_index=7189, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAK_HF2hA1sJoOr-XRwWLmfUyyhg99zDf3kfSJW1Mmk-xBHKpM_QdyOAakMGdIGNy2itPwLP9JN-qaoDN1glzIIYd1OG7OT3K_I916WfiEeqNYrQeBv46hNh_o_KgQJuS_yEjuuBN9grzF2dBtB1HInu7P_uaoAcQmT3ooxRM7qNnqrpcI8DmD7XIfZc7p-kLXfw==', start_index=7176)
Annotation(end_index=7189, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTtws1BUhN3j6Pv2PTcsAtfpLP5ui-71X1ExihDGtqZwde3qO9uF8f1aEogd7VFvI_V2beV3xSXrfIGzaZve4gbZV8D-1PGwKRyeqn-5_2MkDUVMay3jzsRVMxMBCHJId0QFisolpaG3xhcNRC5Rqedr6ECbNspQ==', start_index=7176)
Annotation(end_index=7738, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQnVbzncRWvOwE5jO1LHAAkmoVWOPhzNRK9m5UU_uW4lmmE6LP-0sumD2GyPxLjdYXm-3avdaraq_FS3NqnIHKDK7M7eHC2xZeO-Ukro5uP6QmFG_8V9QsktQtIlmo3wgsXfh-wFg61BDa-BCPdNJqgFf-m3KdGSeTsOg08gA=', start_index=7720)
Annotation(end_index=7738, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHefQIOAZSwWtk4_1tQLQGuZ5dkjLEcO3VyFxdQsdl5GdrunzbmPef0yKIUQhmBC7B9vHsikcM9v1TiS3hfmjDBYkRDhVznC_5vvlj4pnkA6AEVd9o51eoUCrsCwrfGYOr-HRb8N_KZMg==', start_index=7720)
Annotation(end_index=7738, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpCJZq-b6-GDNYI8Nuz1IqHGYqpDS6GHtk0pm3N2WyzAPrDkE38erK9RBz_WmNtutJePc4jI_J1j8K882Oo0T0jSgRJkvVSo8kfOXFrX9Xs5I8BzJXR0zBERm-hPbije3NN09OOTR7V8DM8Onn2YVMg1YIVaqQ5PzjNhbwRGP4dAIfAydNIHY7nw7aZejj8dxsTPycx7GasjAvN3dli_PBHznwAgaSoG-O0BIGjL-ItgIqXvrTkn3I', start_index=7720)
Annotation(end_index=8116, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZxUGYYRURQAamKhdXIV5rWievVCmYXXvl5xqiZ5Vu0xh28TYVo_Fk6DRYAg_TFcEyzGg3EQJwpC1psPfchCJ6_M6Sao7OlstrPgSNaRki_D75a9WeHFr5xv6A8i8SquMBPFK5U398EDPbRkhs8SQvbCYTGWmYxByypepZJeSOMj9wKy7Dig==', start_index=8107)
Annotation(end_index=9073, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRfqBWCvoL9AqYpR_0Q-0w2OGzfD05bR5Q5R1hNyI7Gd3dUCG721H5iQOSVpdnfFsTLfKZNYzYs9Zd3Z8-oKc3UzockCOaQy4chkY9WUDJ2AXSkNHgcuE6YDtVzpMm2RUgytHVbjCu_vOC7_dGZqFLe-YE4cyFsxVyoyPzoQ2w4FpZlaUe38xyqf8qcnZ_3nex0d6RHLsQLAEO1ClM9k2cOnVeLLNwsCopZ_Pgsgg=', start_index=9059)
Annotation(end_index=9073, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaJQdQScxlFKuBDq3bhPmZYzTM468kdnBpgojlDRNlvUlE9lLWjAJE6N9SwrYZxXkh9vWnlieLTpJVRv95E73UrNeIPA10GUBtesE4s2lh_n60SpTjzPtwtzove9LKig==', start_index=9059)
Annotation(end_index=9398, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaJQdQScxlFKuBDq3bhPmZYzTM468kdnBpgojlDRNlvUlE9lLWjAJE6N9SwrYZxXkh9vWnlieLTpJVRv95E73UrNeIPA10GUBtesE4s2lh_n60SpTjzPtwtzove9LKig==', start_index=9388)
Annotation(end_index=9777, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSRqr77SuDZhUKdP8Ewo_t4TuG1NP1bkC-Ugb8ANdwU7fkJhjyomxcSFOQa9RL8jI8DUKi5OTbbB68f-SiRr_bvW05X_UdbLDuUoKc4BNQdAXW3rGg7Xk96WzdDj6vq0G9Zji-DHwsDQ==', start_index=9768)
Annotation(end_index=9986, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9Ah4VFJBSWqi7hJcnUTBx7WrD2ovZzs3SjGX8giX8_i7bvmiP2jbg4by1kT7Zn5gu86SRoDvtLvMs3Ayk7MygSpPIRFibyNaApZecLucrDVourYofq_6SU3KSgt4nVfEr2dnQUVGn', start_index=9973)
Annotation(end_index=9986, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGd9Izqh-cYLDIj4WAVLuYJbvspAysTwmbOsOFsJRR8OM6n0bxDkSzuWZEAebrYK-KfBreptj5cCGr5RnSZ2FMgVWmtM4HIfZID47iAGYG_angokJSzqd4lKzN6FxEKwwXhRQ-4brR5Tt7rkgVyyRfnM04OvMIRtsuXMmSC4O6ePxM9TGe3uFGR8dVzm950eW3NPNZ_mzm73MB7kewpYsdT3LuBD6i3TMNlXl1KcPdYEupYDCbmMnMnpg-PicZeHIL98wWbyDwhlul-K1v70tkpXuHgz4ymnfUHKBJPWjs=', start_index=9973)
Annotation(end_index=10374, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKUoKqCybCb_SmzE6Kx2IJ5XuvzI2sgQHOVyn63ipYIv_-6Loj1tU2FwxGYciU7eBu8GvG58x9mypFvjHAXwhlSe7fHR7IExmJ5gJtFE_kMKiu02zgfWBIxVSfIUvvZUlg3DswqY1M', start_index=10361)
Annotation(end_index=10374, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGd9Izqh-cYLDIj4WAVLuYJbvspAysTwmbOsOFsJRR8OM6n0bxDkSzuWZEAebrYK-KfBreptj5cCGr5RnSZ2FMgVWmtM4HIfZID47iAGYG_angokJSzqd4lKzN6FxEKwwXhRQ-4brR5Tt7rkgVyyRfnM04OvMIRtsuXMmSC4O6ePxM9TGe3uFGR8dVzm950eW3NPNZ_mzm73MB7kewpYsdT3LuBD6i3TMNlXl1KcPdYEupYDCbmMnMnpg-PicZeHIL98wWbyDwhlul-K1v70tkpXuHgz4ymnfUHKBJPWjs=', start_index=10361)
Annotation(end_index=10621, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQnVbzncRWvOwE5jO1LHAAkmoVWOPhzNRK9m5UU_uW4lmmE6LP-0sumD2GyPxLjdYXm-3avdaraq_FS3NqnIHKDK7M7eHC2xZeO-Ukro5uP6QmFG_8V9QsktQtIlmo3wgsXfh-wFg61BDa-BCPdNJqgFf-m3KdGSeTsOg08gA=', start_index=10607)
Annotation(end_index=10621, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQ_NLoFAlvbkIwLnojiFrhFPXHRdcT1uLrUsHIjI2uSJ1XLqpCVjavfT1CWT0knsOikI9y1llwzkYB6BNgJ0R0dNBnx_kCwewidVXXDJcY1H8-p_gDUMiPb-EcE9TpWEzv27cZxf4j', start_index=10607)
Annotation(end_index=10871, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0f87_GlxSj62HgLnMia1UBNuASJ-JoxhVOSZoPURAUG-pfD-mhoQL2isyjyJLuZL1IJzzkZ_5Vb5yAQ1nyDsR4iMVHnDIgivdTyyLIV1pD-fwpcewVfn7wud3kTUwkoJItLZFz1OPAL56xep0qA_uQdTHcpVGrryArlCQBUeMNvWG3EzzG9llS4QHzpbSCO8bT_5ITBUNhKiuTO8-4f-vy2HlCueSjnM7Yc7lbK4jLg8d', start_index=10861)
Annotation(end_index=11744, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHemG3Om-6wMSQj9tH8CDbacQgTwJ2cmq_2e8sMSSy0zHhJzqFU1Pyl8xCUtNMJc_U1fa4PrDHr_DIi0WDBTufQeRoxODf3VtQrcjJuSOmvaYgjpmS6pDf_OmO66a5iKduVdorrm9-5j4OtBFq8r5aQ5Eudyv9mBOIA1quob2Nbxi-1eDqvZFA7iYtNIe0xw==', start_index=11732)
Annotation(end_index=11744, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHx2Iqto76lJEEoUnamVVI23ll0FLwHc-9N32Suyzih1F_w8QK3esmrCsCpNI5ZeQE0WgDxAG54vBoTo6gSLvAZ-O5vyIrnnVQDRuF2dx-NhrFdiIh_Vy2HZRPYODuEqGt0YiDykaZFQsLoLqWwuiPZIDyxVU0YeDrpUC7lJxD8XZZePuW5CsNOCHTN2vmhs9kFuikw', start_index=11732)
Annotation(end_index=11969, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHx2Iqto76lJEEoUnamVVI23ll0FLwHc-9N32Suyzih1F_w8QK3esmrCsCpNI5ZeQE0WgDxAG54vBoTo6gSLvAZ-O5vyIrnnVQDRuF2dx-NhrFdiIh_Vy2HZRPYODuEqGt0YiDykaZFQsLoLqWwuiPZIDyxVU0YeDrpUC7lJxD8XZZePuW5CsNOCHTN2vmhs9kFuikw', start_index=11960)
Annotation(end_index=12270, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9Ah4VFJBSWqi7hJcnUTBx7WrD2ovZzs3SjGX8giX8_i7bvmiP2jbg4by1kT7Zn5gu86SRoDvtLvMs3Ayk7MygSpPIRFibyNaApZecLucrDVourYofq_6SU3KSgt4nVfEr2dnQUVGn', start_index=12253)
Annotation(end_index=12270, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHemG3Om-6wMSQj9tH8CDbacQgTwJ2cmq_2e8sMSSy0zHhJzqFU1Pyl8xCUtNMJc_U1fa4PrDHr_DIi0WDBTufQeRoxODf3VtQrcjJuSOmvaYgjpmS6pDf_OmO66a5iKduVdorrm9-5j4OtBFq8r5aQ5Eudyv9mBOIA1quob2Nbxi-1eDqvZFA7iYtNIe0xw==', start_index=12253)
Annotation(end_index=12270, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2MyvmszPhat3jQgfcwcUXt6r54JGhoEPjcvaAatLb7KUAA3cvtNtMLtr8V-5v9Do2HIhqMh4MNPE2NcbcgmUOGYSSOmwTKt-wmE0Hqfb37X5Uh4C5Zd6ENtqnkm3JvDdI', start_index=12253)
Annotation(end_index=12599, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzP4s5RvutZykuSbBtITj19ZkcytCPm4owRHGBYeSeSY4z6tWLDC3MgiCO9qkSP8E_lzO6zryuihcM9FVDVnCNyXVgu56kxa995iATeH7wVtI_ajaDGHCA25N32jwwdnINImHa68wPmNBut65HrjF6fG5lN8dVYqOsMr6YbVZcKZxzJXl0xeANPGMOVg502oEJtfVNsizJBviARbtDK125', start_index=12589)
Annotation(end_index=12845, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaJQdQScxlFKuBDq3bhPmZYzTM468kdnBpgojlDRNlvUlE9lLWjAJE6N9SwrYZxXkh9vWnlieLTpJVRv95E73UrNeIPA10GUBtesE4s2lh_n60SpTjzPtwtzove9LKig==', start_index=12835)
Annotation(end_index=13363, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZxUGYYRURQAamKhdXIV5rWievVCmYXXvl5xqiZ5Vu0xh28TYVo_Fk6DRYAg_TFcEyzGg3EQJwpC1psPfchCJ6_M6Sao7OlstrPgSNaRki_D75a9WeHFr5xv6A8i8SquMBPFK5U398EDPbRkhs8SQvbCYTGWmYxByypepZJeSOMj9wKy7Dig==', start_index=13354)
Annotation(end_index=13587, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTtws1BUhN3j6Pv2PTcsAtfpLP5ui-71X1ExihDGtqZwde3qO9uF8f1aEogd7VFvI_V2beV3xSXrfIGzaZve4gbZV8D-1PGwKRyeqn-5_2MkDUVMay3jzsRVMxMBCHJId0QFisolpaG3xhcNRC5Rqedr6ECbNspQ==', start_index=13573)
Annotation(end_index=13587, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGH3hAMqgKg8Sr1QXk_XuJxG-R2ClzoJ_BPUm8-Ssm8OX5BRZErdWbY17YNHQZ_LqDcqCD15vA2oWmOyeYVDl5zTn2UaT5p2m0izbhWll1vhwUi3bpByklqvEmDlCpIMB7avuHwbP_TFRG0KUsx', start_index=13573)
Annotation(end_index=13809, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTtws1BUhN3j6Pv2PTcsAtfpLP5ui-71X1ExihDGtqZwde3qO9uF8f1aEogd7VFvI_V2beV3xSXrfIGzaZve4gbZV8D-1PGwKRyeqn-5_2MkDUVMay3jzsRVMxMBCHJId0QFisolpaG3xhcNRC5Rqedr6ECbNspQ==', start_index=13795)
Annotation(end_index=13809, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEKs-JrOCwnp9SG3zJITT_-ddrkCGiIEKI89j8lXl5kuIhQZeA5XRg2rvsoTRtZtICb1rlDMi3iWp774n59gu4VFLH_gvZNEIRfwzGDoxTLCpGum8YNwbknphN_bBeI6Mop5nUyzXJF2_spUGsTkMWCJgQUXa4ZaYKPMtDAky7SsWQFsiKAbrNzuKBMQ==', start_index=13795)
Annotation(end_index=14086, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBdzaJ4fYSgeUQSerHSuGcpR99yOWyYoPqO7PjyTO8ymvGMJlkgQB1QrnxNzOoSiwaOjQOP2McXfpoBrKw8UWebS_a3hMqJTE3_Fhve6_a2wrNmxIpO0dWoJ-VjZ4YB33dZd_v_6iAXMu0ZX9dQV_E5PAIL-4ryt_nKdqXiBmfCNlwHI9B4e4vz7kPUAhQ3lAlW_He4AAk2QTpkkrwcSTQ7XGGW0EI5D86kIMOE5w6ykI6u0k90bCPwUSUuurDC-XY1YgKHhCrGk8G6Q==', start_index=14073)
Annotation(end_index=14086, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTtws1BUhN3j6Pv2PTcsAtfpLP5ui-71X1ExihDGtqZwde3qO9uF8f1aEogd7VFvI_V2beV3xSXrfIGzaZve4gbZV8D-1PGwKRyeqn-5_2MkDUVMay3jzsRVMxMBCHJId0QFisolpaG3xhcNRC5Rqedr6ECbNspQ==', start_index=14073)
Annotation(end_index=14731, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHx2Iqto76lJEEoUnamVVI23ll0FLwHc-9N32Suyzih1F_w8QK3esmrCsCpNI5ZeQE0WgDxAG54vBoTo6gSLvAZ-O5vyIrnnVQDRuF2dx-NhrFdiIh_Vy2HZRPYODuEqGt0YiDykaZFQsLoLqWwuiPZIDyxVU0YeDrpUC7lJxD8XZZePuW5CsNOCHTN2vmhs9kFuikw', start_index=14722)
Annotation(end_index=15118, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfq0pFTggNNNjlRCYuh806HmtkJHn3j6ZdKsJgVQGXH9yAvUKOin7wXUv0sKQAUP_BmnFnvvIcFK1ShoCVnGyLT0aDwihzvMqu0yHeHxYCQ9YV0kfzxFyKJGn6ymL-Pb9QMPqJM2MZCPQ=', start_index=15104)
Annotation(end_index=15118, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnnNPnYwDsIg6b8SBtqMoutA3Y6x2LQGug6zIaq0YdjOXG3K1F4VO5KgN1LX8gFjPmTbyX_jQR22xd7t3xTiIKR_2exPQxTcB0X4i3U6BmVXEpqkX0We4qZe6J6h3dovFiogoguAV1d65cd-C5N4k8jqgdfVYHYCg=', start_index=15104)
Annotation(end_index=15384, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBdzaJ4fYSgeUQSerHSuGcpR99yOWyYoPqO7PjyTO8ymvGMJlkgQB1QrnxNzOoSiwaOjQOP2McXfpoBrKw8UWebS_a3hMqJTE3_Fhve6_a2wrNmxIpO0dWoJ-VjZ4YB33dZd_v_6iAXMu0ZX9dQV_E5PAIL-4ryt_nKdqXiBmfCNlwHI9B4e4vz7kPUAhQ3lAlW_He4AAk2QTpkkrwcSTQ7XGGW0EI5D86kIMOE5w6ykI6u0k90bCPwUSUuurDC-XY1YgKHhCrGk8G6Q==', start_index=15372)
Annotation(end_index=15384, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHemG3Om-6wMSQj9tH8CDbacQgTwJ2cmq_2e8sMSSy0zHhJzqFU1Pyl8xCUtNMJc_U1fa4PrDHr_DIi0WDBTufQeRoxODf3VtQrcjJuSOmvaYgjpmS6pDf_OmO66a5iKduVdorrm9-5j4OtBFq8r5aQ5Eudyv9mBOIA1quob2Nbxi-1eDqvZFA7iYtNIe0xw==', start_index=15372)
Annotation(end_index=15523, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTtws1BUhN3j6Pv2PTcsAtfpLP5ui-71X1ExihDGtqZwde3qO9uF8f1aEogd7VFvI_V2beV3xSXrfIGzaZve4gbZV8D-1PGwKRyeqn-5_2MkDUVMay3jzsRVMxMBCHJId0QFisolpaG3xhcNRC5Rqedr6ECbNspQ==', start_index=15510)
Annotation(end_index=15523, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZxUGYYRURQAamKhdXIV5rWievVCmYXXvl5xqiZ5Vu0xh28TYVo_Fk6DRYAg_TFcEyzGg3EQJwpC1psPfchCJ6_M6Sao7OlstrPgSNaRki_D75a9WeHFr5xv6A8i8SquMBPFK5U398EDPbRkhs8SQvbCYTGWmYxByypepZJeSOMj9wKy7Dig==', start_index=15510)
Annotation(end_index=16177, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHx2Iqto76lJEEoUnamVVI23ll0FLwHc-9N32Suyzih1F_w8QK3esmrCsCpNI5ZeQE0WgDxAG54vBoTo6gSLvAZ-O5vyIrnnVQDRuF2dx-NhrFdiIh_Vy2HZRPYODuEqGt0YiDykaZFQsLoLqWwuiPZIDyxVU0YeDrpUC7lJxD8XZZePuW5CsNOCHTN2vmhs9kFuikw', start_index=16168)
Annotation(end_index=16453, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDvAk9R5F8FxWry1FPV_GMiQU0eRod5CxlwhIwmUxjW2bUEt3x3gIofOcAOnV0l18Iy3wbrO3DyQmNrxG9NkV7r1Gdgx4j-AV1ff_6jONH88_6e3PdM5atomQsSdu1Zhk32gfZbSW3', start_index=16441)
Annotation(end_index=16453, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGd9Izqh-cYLDIj4WAVLuYJbvspAysTwmbOsOFsJRR8OM6n0bxDkSzuWZEAebrYK-KfBreptj5cCGr5RnSZ2FMgVWmtM4HIfZID47iAGYG_angokJSzqd4lKzN6FxEKwwXhRQ-4brR5Tt7rkgVyyRfnM04OvMIRtsuXMmSC4O6ePxM9TGe3uFGR8dVzm950eW3NPNZ_mzm73MB7kewpYsdT3LuBD6i3TMNlXl1KcPdYEupYDCbmMnMnpg-PicZeHIL98wWbyDwhlul-K1v70tkpXuHgz4ymnfUHKBJPWjs=', start_index=16441)
Annotation(end_index=16843, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAK_HF2hA1sJoOr-XRwWLmfUyyhg99zDf3kfSJW1Mmk-xBHKpM_QdyOAakMGdIGNy2itPwLP9JN-qaoDN1glzIIYd1OG7OT3K_I916WfiEeqNYrQeBv46hNh_o_KgQJuS_yEjuuBN9grzF2dBtB1HInu7P_uaoAcQmT3ooxRM7qNnqrpcI8DmD7XIfZc7p-kLXfw==', start_index=16834)
Annotation(end_index=16945, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZxUGYYRURQAamKhdXIV5rWievVCmYXXvl5xqiZ5Vu0xh28TYVo_Fk6DRYAg_TFcEyzGg3EQJwpC1psPfchCJ6_M6Sao7OlstrPgSNaRki_D75a9WeHFr5xv6A8i8SquMBPFK5U398EDPbRkhs8SQvbCYTGWmYxByypepZJeSOMj9wKy7Dig==', start_index=16936)
Annotation(end_index=17078, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzP4s5RvutZykuSbBtITj19ZkcytCPm4owRHGBYeSeSY4z6tWLDC3MgiCO9qkSP8E_lzO6zryuihcM9FVDVnCNyXVgu56kxa995iATeH7wVtI_ajaDGHCA25N32jwwdnINImHa68wPmNBut65HrjF6fG5lN8dVYqOsMr6YbVZcKZxzJXl0xeANPGMOVg502oEJtfVNsizJBviARbtDK125', start_index=17068)
Annotation(end_index=17186, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTtws1BUhN3j6Pv2PTcsAtfpLP5ui-71X1ExihDGtqZwde3qO9uF8f1aEogd7VFvI_V2beV3xSXrfIGzaZve4gbZV8D-1PGwKRyeqn-5_2MkDUVMay3jzsRVMxMBCHJId0QFisolpaG3xhcNRC5Rqedr6ECbNspQ==', start_index=17176)
Annotation(end_index=17280, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHemG3Om-6wMSQj9tH8CDbacQgTwJ2cmq_2e8sMSSy0zHhJzqFU1Pyl8xCUtNMJc_U1fa4PrDHr_DIi0WDBTufQeRoxODf3VtQrcjJuSOmvaYgjpmS6pDf_OmO66a5iKduVdorrm9-5j4OtBFq8r5aQ5Eudyv9mBOIA1quob2Nbxi-1eDqvZFA7iYtNIe0xw==', start_index=17271)
Annotation(end_index=17361, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8h3VylLsMVz9uNdoflQ0-0ge_cxeR_J1MwlCde_hB6paQtA4HIhF9YrXfkiMJz3ivxA_0owp1alVJagZ54cWRyj_2-w2OanNXiv38f8pq_Y8PwRlWml7-YPP50ySORtCz1uwilWuqFGIdWzfe37cd9ZDGyqNdMi7EPvLg7-MD7gn3vpeGkHp42fSrVvuVL2zrEDetAw==', start_index=17352)
Annotation(end_index=17447, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHefQIOAZSwWtk4_1tQLQGuZ5dkjLEcO3VyFxdQsdl5GdrunzbmPef0yKIUQhmBC7B9vHsikcM9v1TiS3hfmjDBYkRDhVznC_5vvlj4pnkA6AEVd9o51eoUCrsCwrfGYOr-HRb8N_KZMg==', start_index=17437)
Annotation(end_index=17536, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGd9Izqh-cYLDIj4WAVLuYJbvspAysTwmbOsOFsJRR8OM6n0bxDkSzuWZEAebrYK-KfBreptj5cCGr5RnSZ2FMgVWmtM4HIfZID47iAGYG_angokJSzqd4lKzN6FxEKwwXhRQ-4brR5Tt7rkgVyyRfnM04OvMIRtsuXMmSC4O6ePxM9TGe3uFGR8dVzm950eW3NPNZ_mzm73MB7kewpYsdT3LuBD6i3TMNlXl1KcPdYEupYDCbmMnMnpg-PicZeHIL98wWbyDwhlul-K1v70tkpXuHgz4ymnfUHKBJPWjs=', start_index=17527)
Annotation(end_index=17642, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0f87_GlxSj62HgLnMia1UBNuASJ-JoxhVOSZoPURAUG-pfD-mhoQL2isyjyJLuZL1IJzzkZ_5Vb5yAQ1nyDsR4iMVHnDIgivdTyyLIV1pD-fwpcewVfn7wud3kTUwkoJItLZFz1OPAL56xep0qA_uQdTHcpVGrryArlCQBUeMNvWG3EzzG9llS4QHzpbSCO8bT_5ITBUNhKiuTO8-4f-vy2HlCueSjnM7Yc7lbK4jLg8d', start_index=17632)
Annotation(end_index=17764, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfQGSBrc5cuJun4bIhs4NjP3fLmMxiQJytZTy1GpYNzAMTmaET9K3wo6krnUD3PmIthNfuTqziOlVYyZTotVMrRHZaUurnDM9H2jjNskHlXzF_t8bWKA==', start_index=17754)
Annotation(end_index=17864, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTtws1BUhN3j6Pv2PTcsAtfpLP5ui-71X1ExihDGtqZwde3qO9uF8f1aEogd7VFvI_V2beV3xSXrfIGzaZve4gbZV8D-1PGwKRyeqn-5_2MkDUVMay3jzsRVMxMBCHJId0QFisolpaG3xhcNRC5Rqedr6ECbNspQ==', start_index=17854)
Annotation(end_index=17951, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEKs-JrOCwnp9SG3zJITT_-ddrkCGiIEKI89j8lXl5kuIhQZeA5XRg2rvsoTRtZtICb1rlDMi3iWp774n59gu4VFLH_gvZNEIRfwzGDoxTLCpGum8YNwbknphN_bBeI6Mop5nUyzXJF2_spUGsTkMWCJgQUXa4ZaYKPMtDAky7SsWQFsiKAbrNzuKBMQ==', start_index=17941)
Annotation(end_index=18042, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQ_NLoFAlvbkIwLnojiFrhFPXHRdcT1uLrUsHIjI2uSJ1XLqpCVjavfT1CWT0knsOikI9y1llwzkYB6BNgJ0R0dNBnx_kCwewidVXXDJcY1H8-p_gDUMiPb-EcE9TpWEzv27cZxf4j', start_index=18032)
Annotation(end_index=18132, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBdzaJ4fYSgeUQSerHSuGcpR99yOWyYoPqO7PjyTO8ymvGMJlkgQB1QrnxNzOoSiwaOjQOP2McXfpoBrKw8UWebS_a3hMqJTE3_Fhve6_a2wrNmxIpO0dWoJ-VjZ4YB33dZd_v_6iAXMu0ZX9dQV_E5PAIL-4ryt_nKdqXiBmfCNlwHI9B4e4vz7kPUAhQ3lAlW_He4AAk2QTpkkrwcSTQ7XGGW0EI5D86kIMOE5w6ykI6u0k90bCPwUSUuurDC-XY1YgKHhCrGk8G6Q==', start_index=18123)
Annotation(end_index=18246, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHx2Iqto76lJEEoUnamVVI23ll0FLwHc-9N32Suyzih1F_w8QK3esmrCsCpNI5ZeQE0WgDxAG54vBoTo6gSLvAZ-O5vyIrnnVQDRuF2dx-NhrFdiIh_Vy2HZRPYODuEqGt0YiDykaZFQsLoLqWwuiPZIDyxVU0YeDrpUC7lJxD8XZZePuW5CsNOCHTN2vmhs9kFuikw', start_index=18237)
Annotation(end_index=18321, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzP4s5RvutZykuSbBtITj19ZkcytCPm4owRHGBYeSeSY4z6tWLDC3MgiCO9qkSP8E_lzO6zryuihcM9FVDVnCNyXVgu56kxa995iATeH7wVtI_ajaDGHCA25N32jwwdnINImHa68wPmNBut65HrjF6fG5lN8dVYqOsMr6YbVZcKZxzJXl0xeANPGMOVg502oEJtfVNsizJBviARbtDK125', start_index=18311)
Annotation(end_index=18429, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKUoKqCybCb_SmzE6Kx2IJ5XuvzI2sgQHOVyn63ipYIv_-6Loj1tU2FwxGYciU7eBu8GvG58x9mypFvjHAXwhlSe7fHR7IExmJ5gJtFE_kMKiu02zgfWBIxVSfIUvvZUlg3DswqY1M', start_index=18419)
Annotation(end_index=18521, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzx50KU6bhmo0Zzxx-T9ImXwWz0JF_muR9RxV2W2X87qQRHP_719qK6dcqu3sanj0I29LX_nk2mZnEefiVIuS6cD1SRP6HBtZc2-XnNSTK-bQ2iElJ54QOJgIwGltGbt-QGcP_m9UF', start_index=18511)
Annotation(end_index=18585, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7IbqBgSkw9kvu5hqC2pvoCnaXBK5w2xgH4KkWoIDdpPbvGwyeVLRZiBYlL1DdnqJ23t5_dNAfTtSywQn0ua62g4RZNhBezBwt3NHwxBqdkfxK22hDq1o8zWB8Wzvo0Nd3wtJcK_1ULA==', start_index=18575)
Annotation(end_index=18664, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYC88BMUkW4rqXIiYbPqYQdyx-thbz5oYJPYq90ZSwXHYw0EcXj-H-HO0IK8jxgoxYhCzEa2bKCmAT4Da2Fr5UvPcavmMd78TJhU2fJRBE6PaHcX0gzKL0CUv0Q938TL5-07UMqtKmE0ZfbfcvtS4QCpol2okAIqw2KhiuGT_0mIIBsmtXnvfx0G-q_Xku7i6yoPqAIMmx', start_index=18654)
Annotation(end_index=18762, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2MyvmszPhat3jQgfcwcUXt6r54JGhoEPjcvaAatLb7KUAA3cvtNtMLtr8V-5v9Do2HIhqMh4MNPE2NcbcgmUOGYSSOmwTKt-wmE0Hqfb37X5Uh4C5Zd6ENtqnkm3JvDdI', start_index=18752)
Annotation(end_index=18861, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaJQdQScxlFKuBDq3bhPmZYzTM468kdnBpgojlDRNlvUlE9lLWjAJE6N9SwrYZxXkh9vWnlieLTpJVRv95E73UrNeIPA10GUBtesE4s2lh_n60SpTjzPtwtzove9LKig==', start_index=18851)
Annotation(end_index=18971, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRfqBWCvoL9AqYpR_0Q-0w2OGzfD05bR5Q5R1hNyI7Gd3dUCG721H5iQOSVpdnfFsTLfKZNYzYs9Zd3Z8-oKc3UzockCOaQy4chkY9WUDJ2AXSkNHgcuE6YDtVzpMm2RUgytHVbjCu_vOC7_dGZqFLe-YE4cyFsxVyoyPzoQ2w4FpZlaUe38xyqf8qcnZ_3nex0d6RHLsQLAEO1ClM9k2cOnVeLLNwsCopZ_Pgsgg=', start_index=18961)
Annotation(end_index=19087, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfq0pFTggNNNjlRCYuh806HmtkJHn3j6ZdKsJgVQGXH9yAvUKOin7wXUv0sKQAUP_BmnFnvvIcFK1ShoCVnGyLT0aDwihzvMqu0yHeHxYCQ9YV0kfzxFyKJGn6ymL-Pb9QMPqJM2MZCPQ=', start_index=19077)
Annotation(end_index=19219, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQnVbzncRWvOwE5jO1LHAAkmoVWOPhzNRK9m5UU_uW4lmmE6LP-0sumD2GyPxLjdYXm-3avdaraq_FS3NqnIHKDK7M7eHC2xZeO-Ukro5uP6QmFG_8V9QsktQtIlmo3wgsXfh-wFg61BDa-BCPdNJqgFf-m3KdGSeTsOg08gA=', start_index=19209)
Annotation(end_index=19302, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpCJZq-b6-GDNYI8Nuz1IqHGYqpDS6GHtk0pm3N2WyzAPrDkE38erK9RBz_WmNtutJePc4jI_J1j8K882Oo0T0jSgRJkvVSo8kfOXFrX9Xs5I8BzJXR0zBERm-hPbije3NN09OOTR7V8DM8Onn2YVMg1YIVaqQ5PzjNhbwRGP4dAIfAydNIHY7nw7aZejj8dxsTPycx7GasjAvN3dli_PBHznwAgaSoG-O0BIGjL-ItgIqXvrTkn3I', start_index=19292)
Annotation(end_index=19391, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZxUGYYRURQAamKhdXIV5rWievVCmYXXvl5xqiZ5Vu0xh28TYVo_Fk6DRYAg_TFcEyzGg3EQJwpC1psPfchCJ6_M6Sao7OlstrPgSNaRki_D75a9WeHFr5xv6A8i8SquMBPFK5U398EDPbRkhs8SQvbCYTGWmYxByypepZJeSOMj9wKy7Dig==', start_index=19382)
Annotation(end_index=19466, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBdzaJ4fYSgeUQSerHSuGcpR99yOWyYoPqO7PjyTO8ymvGMJlkgQB1QrnxNzOoSiwaOjQOP2McXfpoBrKw8UWebS_a3hMqJTE3_Fhve6_a2wrNmxIpO0dWoJ-VjZ4YB33dZd_v_6iAXMu0ZX9dQV_E5PAIL-4ryt_nKdqXiBmfCNlwHI9B4e4vz7kPUAhQ3lAlW_He4AAk2QTpkkrwcSTQ7XGGW0EI5D86kIMOE5w6ykI6u0k90bCPwUSUuurDC-XY1YgKHhCrGk8G6Q==', start_index=19457)
Annotation(end_index=19551, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHemG3Om-6wMSQj9tH8CDbacQgTwJ2cmq_2e8sMSSy0zHhJzqFU1Pyl8xCUtNMJc_U1fa4PrDHr_DIi0WDBTufQeRoxODf3VtQrcjJuSOmvaYgjpmS6pDf_OmO66a5iKduVdorrm9-5j4OtBFq8r5aQ5Eudyv9mBOIA1quob2Nbxi-1eDqvZFA7iYtNIe0xw==', start_index=19542)
Annotation(end_index=19647, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnnNPnYwDsIg6b8SBtqMoutA3Y6x2LQGug6zIaq0YdjOXG3K1F4VO5KgN1LX8gFjPmTbyX_jQR22xd7t3xTiIKR_2exPQxTcB0X4i3U6BmVXEpqkX0We4qZe6J6h3dovFiogoguAV1d65cd-C5N4k8jqgdfVYHYCg=', start_index=19637)
Annotation(end_index=19718, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHx2Iqto76lJEEoUnamVVI23ll0FLwHc-9N32Suyzih1F_w8QK3esmrCsCpNI5ZeQE0WgDxAG54vBoTo6gSLvAZ-O5vyIrnnVQDRuF2dx-NhrFdiIh_Vy2HZRPYODuEqGt0YiDykaZFQsLoLqWwuiPZIDyxVU0YeDrpUC7lJxD8XZZePuW5CsNOCHTN2vmhs9kFuikw', start_index=19709)
Annotation(end_index=19793, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9Ah4VFJBSWqi7hJcnUTBx7WrD2ovZzs3SjGX8giX8_i7bvmiP2jbg4by1kT7Zn5gu86SRoDvtLvMs3Ayk7MygSpPIRFibyNaApZecLucrDVourYofq_6SU3KSgt4nVfEr2dnQUVGn', start_index=19783)
Annotation(end_index=19869, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDvAk9R5F8FxWry1FPV_GMiQU0eRod5CxlwhIwmUxjW2bUEt3x3gIofOcAOnV0l18Iy3wbrO3DyQmNrxG9NkV7r1Gdgx4j-AV1ff_6jONH88_6e3PdM5atomQsSdu1Zhk32gfZbSW3', start_index=19860)
Annotation(end_index=19939, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSRqr77SuDZhUKdP8Ewo_t4TuG1NP1bkC-Ugb8ANdwU7fkJhjyomxcSFOQa9RL8jI8DUKi5OTbbB68f-SiRr_bvW05X_UdbLDuUoKc4BNQdAXW3rGg7Xk96WzdDj6vq0G9Zji-DHwsDQ==', start_index=19930)
Annotation(end_index=20012, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTtws1BUhN3j6Pv2PTcsAtfpLP5ui-71X1ExihDGtqZwde3qO9uF8f1aEogd7VFvI_V2beV3xSXrfIGzaZve4gbZV8D-1PGwKRyeqn-5_2MkDUVMay3jzsRVMxMBCHJId0QFisolpaG3xhcNRC5Rqedr6ECbNspQ==', start_index=20002)
Annotation(end_index=20079, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGH3hAMqgKg8Sr1QXk_XuJxG-R2ClzoJ_BPUm8-Ssm8OX5BRZErdWbY17YNHQZ_LqDcqCD15vA2oWmOyeYVDl5zTn2UaT5p2m0izbhWll1vhwUi3bpByklqvEmDlCpIMB7avuHwbP_TFRG0KUsx', start_index=20069)

## Sources
