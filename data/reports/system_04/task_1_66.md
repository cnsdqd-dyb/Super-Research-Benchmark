# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** a286c602 | **Time:** 398.46s | **Cost:** $1.50426
--------------------------------------------------------------------------------

# The Markov Chain Character of Activity Sequences and Prediction Reliability Under Changing Socioeconomic Attributes

### Key Points
*   **Reliability of Markov Models:** Research indicates that Markov chain models can achieve high prediction reliability for activity sequences, with some studies reporting an RMSE as low as 0.008 for neighborhood socioeconomic transitions and $R^2$ values up to 0.99 for routine daily patterns (e.g., Home-Work-Home).
*   **The "Memoryless" Debate:** While critics argue that the Markov property (where future states depend only on the current state) oversimplifies complex human behaviors by ignoring long-term history, empirical evidence suggests that for many aggregate applications, Markovian predictions are statistically comparable to those utilizing full historical data.
*   **Socioeconomic Influence:** Socioeconomic attributes are critical determinants of transition probabilities. Models that fail to segment populations based on attributes (e.g., income, employment status) suffer from reduced accuracy. Integrating socioeconomic data via clustering or hybrid machine learning approaches (e.g., Random Forest combined with Markov Chains) significantly enhances model fidelity.
*   **Handling Changing Attributes:** Markov chains are particularly valuable for counterfactual analysis, allowing researchers to simulate how changes in socioeconomic attributes (such as gentrification or policy shifts) alter future activity landscapes by manipulating transition matrices, although they struggle to predict the emergence of entirely new, undefined states.

---

## 1. Introduction

The modeling of activity sequences—whether representing the daily movements of individuals or the longitudinal evolution of urban neighborhoods—is a cornerstone of modern transportation planning, urban geography, and kinetic theory applied to social systems. A dominant methodological framework for these analyses is the Markov chain, a stochastic process predicated on the assumption that the probability of transitioning to a future state depends solely on the current state, independent of the sequence of events that preceded it [cite: 1]. This "memoryless" property offers computational elegance and mathematical tractability, yet it raises significant questions regarding its fidelity in representing the complex, historically contingent nature of human behavior and socioeconomic evolution.

The reliability of these predictions becomes particularly salient when socioeconomic attributes are introduced as dynamic variables. Socioeconomic status (SES) acts as a powerful constraint and driver of activity patterns; a high-income individual’s daily activity chain differs fundamentally from that of a low-income student, just as a gentrifying neighborhood follows a different trajectory than a stable industrial zone [cite: 2, 3]. Consequently, the intersection of the Markov chain character (the mathematical structure) and changing socioeconomic attributes (the contextual variables) forms a critical area of inquiry.

This report evaluates whether the Markov chain character of activity sequences compromises or supports prediction reliability in the context of changing socioeconomic attributes. It synthesizes evidence from urban neighborhood evolution studies, individual travel behavior modeling, and kinetic theories of active particles to determine the robustness of these models.

## 2. The Markov Chain Character in Activity Sequence Modeling

### 2.1 The Markov Property and the "Memoryless" Assumption
At the core of the Markov chain approach is the Markov property, which posits that the future is independent of the past, given the present. In the context of activity sequencing, this implies that the decision to undertake the next activity (e.g., going to a restaurant) depends only on the current activity (e.g., being at work) and not on the sequence of activities performed earlier in the day [cite: 1].

This assumption is theoretically contentious in social sciences. Critics argue that human activity is teleological and path-dependent; an individual’s decision to return home is often dictated by the cumulative duration of time spent out or specific sequences completed earlier (e.g., a "life project" or daily agenda) rather than just their immediate location [cite: 4]. Sequence analysis advocates suggest that Markov models miss the generative processes that produce trajectories, potentially leading to unstable results sensitive to algorithmic specifications [cite: 4, 5].

However, empirical applications often contradict the theoretical limitations. Studies validating Markov models for neighborhood change found that predictions based solely on the present state were "often just as good as the ones considering the full history of the process" [cite: 4]. This suggests that while the generative mechanism of human behavior is complex, the statistical regularities of transitions at an aggregate level are sufficiently captured by the Markov property for accurate forecasting.

### 2.2 First-Order vs. Higher-Order and Hidden Markov Models
To mitigate the limitations of the memoryless assumption, researchers often employ variations of the standard chain:
*   **First-Order Markov Chains:** These rely strictly on the current state ($t$). They are computationally efficient and have been shown to predict neighborhood socioeconomic transitions with high accuracy (RMSE of 0.008) [cite: 4].
*   **Higher-Order Markov Chains:** These incorporate $n$ previous states to determine the next transition. While theoretically more robust, they increase computational complexity. Research in drought prediction, for example, suggests that second-order chains are necessary to capture persistence, a concept transferable to activity "bouts" in human behavior [cite: 6, 7].
*   **Hidden Markov Models (HMM):** HMMs assume that the observed sequence (e.g., GPS location data) is generated by underlying, unobservable states (e.g., "shopping" or "working" purposes). HMMs are particularly effective in inferring activity types from sparse data, such as smart card records, where the socioeconomic intent of a trip is not explicitly labeled [cite: 2, 8].

### 2.3 Applicability to Categorical Time Series
Markov chains are uniquely improved for handling categorical time-series data, which is the standard format for activity sequences (e.g., Home $\to$ Work $\to$ Shop) [cite: 8, 9]. Unlike continuous variable models, Markov chains naturally map the discrete state space of human activities. This capability allows for the simulation of activity status at each time step, capturing the stochasticity inherent in human behavior that deterministic models often fail to represent [cite: 8].

## 3. The Influence of Socioeconomic Attributes

Socioeconomic attributes are not merely background variables; they fundamentally shape the transition matrices that drive Markov processes. The reliability of a Markov model is therefore contingent on how well it accounts for the heterogeneity of the population's socioeconomic characteristics.

### 3.1 Heterogeneity in Transition Probabilities
The probability of transitioning from one activity to another is highly correlated with socioeconomic attributes such as income, employment status, and household structure.
*   **Income and Mobility:** Populations with higher socioeconomic levels typically exhibit larger mobility ranges and more diverse activity chains compared to lower-income groups [cite: 2].
*   **Role-Based Patterns:** Workers, students, and non-workers have distinct transition probabilities. For instance, the sequence "Home-Work-Home" is highly predictable for employed individuals ($R^2 = 0.99$), whereas students exhibit different, though still predictable, patterns like "Home-Education-Home" ($R^2 = 0.90$) [cite: 3, 10].

If a Markov model aggregates these distinct groups into a single transition matrix, prediction reliability suffers due to the averaging of divergent behaviors. Conversely, when models segment populations based on socioeconomic attributes (e.g., using geodemographic segmentation), the predictive power increases significantly [cite: 4].

### 3.2 Clustering and Segmentation Approaches
To address heterogeneity, advanced methodologies employ a two-step process:
1.  **Clustering:** Individuals or neighborhoods are classified into distinct groups based on socioeconomic attributes (e.g., "recreation-shopping-oriented" vs. "schooling-drop-off-oriented" patterns) [cite: 9, 11].
2.  **Markov Modeling:** A separate Markov chain is estimated for each cluster. This approach allows the model to capture the specific generative processes relevant to each socioeconomic group.

For example, a study in Toronto classified neighborhoods into a hierarchy of socioeconomic types before applying Markov models. This hierarchical approach allowed researchers to predict the future distribution of neighborhood types with exceptional accuracy, validating the model's power when socioeconomic context is explicitly integrated [cite: 4].

### 3.3 Dynamic Socioeconomic Changes
A critical challenge is modeling *changing* socioeconomic attributes—situations where the attributes themselves evolve over time (e.g., a person gets a job, or a neighborhood gentrifies).
*   **Non-Stationarity:** Standard Markov chains often assume stationary transition probabilities (probabilities do not change over time) [cite: 1]. However, changing socioeconomic conditions imply non-stationarity.
*   **Kinetic Theory Integration:** Advanced theoretical frameworks, such as the Kinetic Theory for Active Particles, generalize Markov chains to allow transition matrices to undergo stochastic variations. This accounts for interactions with the "external world," such as economic shocks or policy changes, making the models more applicable to dynamic socioeconomic problems [cite: 1].

## 4. Prediction Reliability: Empirical Evidence

The ultimate test of the Markov chain character's suitability is the empirical reliability of its predictions. The research results provide quantitative evidence of high performance when models are correctly specified.

### 4.1 Quantitative Accuracy Metrics
*   **Neighborhood Evolution:** In the study of Toronto's neighborhood changes, Markov models predicted the final distribution of neighborhood types with an average Root Mean Square Error (RMSE) of **0.008** [cite: 4]. This extremely low error rate demonstrates that the Markov character, despite its theoretical simplicity, captures the inertia and transition dynamics of urban socio-spatial structure effectively.
*   **Individual Activity Patterns:** For individual daily schedules, models incorporating socioeconomic attributes have achieved high replication accuracy. Specific routine sequences like "Home-Work-Home" are predicted with an $R^2$ of **0.99** for workers [cite: 3, 10]. Even for more variable groups like students, accuracy remains high ($R^2 = 0.90$) [cite: 3].
*   **General Schedule Replication:** Random Forest models combined with activity sequencing have shown sequence replication accuracy of up to **77%** to **82%** for 24-hour schedules [cite: 3, 12].

### 4.2 Stability and Robustness
Critics have suggested that sequence analysis results can be unstable and sensitive to algorithms [cite: 4]. However, the validation of Markov models in longitudinal studies shows that the predominant temporal pattern is continuity—neighborhoods and individuals tend to reproduce their states over time [cite: 4, 13]. The Markov model's ability to capture this continuity contributes to its high reliability.

Furthermore, comparisons between Markov models and those considering the full history of a process often reveal that the Markovian predictions are "just as good" [cite: 4, 13]. This finding supports the "sufficiency" of the current state for prediction in many practical contexts, rendering the additional computational burden of history-dependent models unnecessary for certain applications.

### 4.3 Limitations in Reliability
Despite these successes, reliability is not absolute.
*   **Emergence of New States:** A significant drawback of Markov chains is their inability to predict the emergence of entirely new types of neighborhoods or activities that were not present in the initial state space [cite: 4]. If socioeconomic changes lead to a novel form of urban living or a new class of employment activity, a standard Markov model cannot anticipate it.
*   **Infrequent Activities:** While routine patterns (work, school) are predicted well, infrequent activities (e.g., medical visits, rare leisure) are harder to capture with simple Markov chains, often requiring hybrid approaches [cite: 8].

## 5. Methodological Integrations: Enhancing Reliability

To overcome the limitations of the basic Markov character and fully leverage socioeconomic data, researchers have developed hybrid and integrated methodologies.

### 5.1 Hybrid Machine Learning Models
Recent advancements combine Markov chains with machine learning algorithms to better incorporate socioeconomic attributes.
*   **Random Forest + Markov:** Studies have used Random Forest models to predict activity patterns based on socio-demographic characteristics, achieving high accuracy in replicating activity agendas [cite: 12]. The Random Forest component handles the complex, non-linear relationships between SES and activity choices, while the sequencing aspect handles the temporal progression.
*   **Mixture Models:** Markov-chain-based mixture models cluster daily activity chains into distinct patterns (e.g., "recreation-shopping-oriented"). This allows for the identification of generative processes that differ by socioeconomic group, improving the granularity of predictions [cite: 9, 11].

### 5.2 Spatial Markov Chains
Activity sequences do not occur in a vacuum; they are spatially embedded. Spatial Markov chains add a spatial component to the process, allowing the transition probabilities of a neighborhood to depend on the character of nearby neighborhoods [cite: 4]. This integration uncovers the extent to which socioeconomic change is contagious or spatially dependent, significantly refining prediction reliability in urban contexts.

### 5.3 Kinetic Theory and Active Particles
At a theoretical level, the Kinetic Theory for Active Particles re-interprets Boltzmann equations using Markov chains to model large systems (human populations). This approach explicitly introduces parameters for "interactions" and "external force fields" (socioeconomic constraints), providing a rigorous mathematical foundation for how individual stochastic behaviors aggregate into reliable macroscopic predictions [cite: 1].

## 6. Counterfactual Analysis and Scenario Planning

One of the strongest arguments for the reliability and utility of Markov models in this domain is their capacity for counterfactual analysis.

### 6.1 Simulating Policy and Preference Changes
Markov chains allow researchers to modify transition probabilities or initial state distributions to simulate hypothetical scenarios.
*   **Policy Impact:** Researchers can ask, "How would the city evolve if the probability of transitioning from 'low-income' to 'gentrified' were reduced by 10% due to housing policy?" [cite: 4].
*   **Socioeconomic Shifts:** Models can simulate the trajectory of a city under different socioeconomic futures (e.g., an aging population or a shift in workforce composition).

### 6.2 Empirical Demonstration of Complexity
These counterfactual scenarios have empirically demonstrated urban complexity: small initial changes in transition probabilities can reverberate throughout the system, leading to vastly different long-term outcomes [cite: 4]. The reliability of the Markov model in this context is not just about point prediction, but about reliably capturing the *sensitivity* of the system to socioeconomic variables.

## 7. Conclusion

The research overwhelmingly suggests that the Markov chain character of activity sequences does **not** inherently compromise prediction reliability; in fact, when appropriately adapted to account for socioeconomic attributes, it supports highly accurate and robust predictions.

While the "memoryless" assumption is a theoretical simplification, empirical validation shows that Markov models can predict neighborhood evolution with negligible error (RMSE 0.008) and replicate routine individual schedules with high fidelity ($R^2 \approx 0.99$). The key to this reliability lies in the integration of socioeconomic data. Models that treat populations as homogeneous fail to capture the diverse generative processes of activity; however, models that segment populations, employ spatial dependencies, or utilize hybrid machine learning techniques successfully bridge the gap between stochastic simplicity and social complexity.

Therefore, the Markov chain remains a reliable and powerful tool for predicting activity sequences, provided that the changing socioeconomic attributes are explicitly modeled as drivers of the transition probabilities or state spaces.

## References
[cite: 1] Bellomo, N., & Outada, N. (2024). *Mathematics*, 12(10), 1571.
[cite: 4] Silver, D., & Adler, P. (2021). *Complexity*, 2021.
[cite: 8] *Characterizing activity sequences using Profile Hidden Markov Models*. (2025). ResearchGate.
[cite: 2] *Sustainability*, 10(11), 4178. (2018).
[cite: 9] *Journal of Transport Geography*, 130. (2026).
[cite: 3] *Transportation*, 47. (2020).
[cite: 12] *Transportation Research Part C*, 121. (2021).
[cite: 10] *Transportation*, 47. (2020).
[cite: 1] *Mathematics*, 12(10), 1571. (2024).
[cite: 6] *International Journal of Climatology*, 34. (2014).
[cite: 4] *PLOS ONE*, 16(1). (2021).
[cite: 8] *Travel Behaviour and Society*, 24. (2021).
[cite: 11] *Travel Behaviour and Society*, 24. (2021).
[cite: 13] *PLOS ONE*, 16(1). (2021).
[cite: 5] *Geographical Analysis*, 51. (2019).
[cite: 4] *PLOS ONE*, 16(1). (2021).

**Sources:**
1. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmaUSRSRSPya4DIK03ivfa09s1YzirYuB0D06VdPPKKtZTwUqiwdJ_erXgE9PrASXWNceyJJjTYQIFQ7OqhHO4ycmo1l_a2W3hJ5qzXeMON5IGeVYwgSg_x-waLndRFw==)
2. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoib3TQIjGCDR2IEsCah7IPLXIXgMcU9XZWb41VrxjD9f3nQWQPICikvbwkV_LiKzT24HN8p5TbE9t1JEkYYQ07wusOhgEC1P0Mstwf6SrpSd830AJF_ZVu2MGca2qCA==)
3. [d-nb.info](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-phy8vSBklxQbYpb2GFLXWvcAD_xWhraTGuQB7BUNlaQPRjOjJX-72TMqHxE9KcaaJ35SKd11BbaPKYoLMP0RD-cHGuX9vTf0j2IAXNm5qTJrqNyO)
4. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa8wUYIIrjDNA6jrV_dzZ4s7QNPjw7Q8xTKaD4G_o7eMjOuXYa_5PnVMNY_KeHlcjWaN2grk-l_BL7op0zm254GqKlvGVL9xMCh40FWW2kboFPdOY849hm62Innq5MgteNl4fjqA_x)
5. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2y_AOtS_kPVFklegmqg-QVsrrV91EvX3uK9e4TstaMQde8SJKPldNlK-8PoVOlEjhHsF6GfkvM1Ca7O_l8_O0p4AAZ_F2CbTeTdplCFnFiiIjg_v1L3i-0yGFxoF6svhqGxXCoPwzarkYfKJJYZPvOlI6X1hhCaErJvXkUKaPnunPEgD1-8gWP_2SM0NORDu1mvDXVmQ8V1R_u8GjD8w_U9aDPDJztf9h8dFCCG-JZ6u32gtb6EvzkM-XOY0MRrL0-w==)
6. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIXHLuF8VNBEzC2k5-LnrFdBAQY7-gRtZsn7XGg6_kO2_YAReG5mw8E5nDYoYJ1Y8quKtW-QsliXDF7fka2rG6-vGWU1UQQau_QO6sMoSRLKe4bTt2HW8LksX8UjPxFRac2UQklVsdeo3OyeVH2pXJ-j1TD8RtFhyLbc7zQGbkqFG9z9EZrK5MI1KveQ8Y_3iyh1NGAEc-UGq1tUUYSmX2PyqcVEsqIHvReh353EBNSchav0qx3adfPdVV8eR_dTPJRrVuTIYLkX966Fajb7ujNTEbISbza-7GpdB1GwHKACDWU8lvj9K7EsWEqrjWgc6RTP5M748VEAmFMLW6BVcYYQ==)
7. [conicet.gov.ar](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEulzRkfpVuF0-TGNXo5qnbct6qg5va_yJFWqViJ8Kq-mnBdkTaF3oQvcVBbjFXlywnQti5EQ_Q6X4-d1_yxWyuKwBMkEfvaVI_fM3KFXCJthO2FWGf0rkCcfBLKOv2GT6lDAu5SYkgOHLZs4094iYGaq7cLZfmA10rhJ6pRQ-ZQw9LXZCO_uPG-KYoCgBziJ3X5sfjal1OCMtc3syitbNrCQ==)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUinqzMqFD6P4vjHuZ1Tsa8vQWriTDXE5_U8c_nUdLB-GXEdN3bdGfLwgLdxpx2BkPZxcVY890abXEc5hKxu6JdoaaPURnuYAK_I0WJGuggrjoacm4yhL_yoO5BcASnkZXhhyT00pluOmATLT6VuW8IiQwVzNjS7w6ZwPcU6ARwqOpFWFpZdCXTJ1K6jh7-IrlLhjqFtkW9sp-1LTg99wd_wON6FDdavgTIj_34A==)
9. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIWo5zsBXUfyMldbBA0_cFi03_w6fiE5nAZpscwmHHfbYErgnhHCFhjj3FSmoan7y4yL4nkbs1lpjqr4Of2dYFe1Vwd9Xg5N5M7zlByNmpEaiE3Gy_3-Yb0DYy_Dm2OPPu4ocOqMITGax8IkWFq8k8edGFDPJwnKryp8s49i6jR_zbpbY=)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8Aw8vvUCqJc0T37cDJl49cRgPryqZd5eph1Q3feQL7IVtenIhDEC37rLVxikiOWK4nYsoq7ErPZjVA9WaLJ8QakY6B4_nCMhgYjfsQ0zdMCMmeQslDRpjwSFesvPp9Dr-SCCBpndB6d3UmjIThgNsc8pgW9_aGapUnQ-qA6hSAgjcQ1cOQd2kFCQtmlmydJqvkApQ3N06TKML3WAeh1bedaIhyI6V2bZJgJpcoSU2j05Or54ekYWBkOS7KaiwbpG4PITgTDfqOkLEgHUIGjZ3whYhcL5XCrNERh82zorKUo3OLF5EDXgDyJtkvDfKnPkxgUXbvQNpAuHpobbE)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpZEtzYn5eDsCIptFFDF7VYE4y-XatMMk8upWPORy7TpEX1E0jSYV0Naopb2wFR1CiYqQoVd1AfVEccGhyA4hhXnq2knTxpRLpAjzuIlKV7fioCf539E9TbA4mOCrW4VvRGAd_hpxLuUGyc-mUB_FN9TxS8Ju66wzZRMuwAJRrlA75duPG8dTbQ_S_-mxnniJxQL7bZP29UJqJXZRcK1trRJkUAovvVy7CqEvJJzo6AqjIL2UCa5s1VoiHGw0n6O6eH-jzg0JsSuLjeP9Ip0rrVtGPyM5FmAWoRg==)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEblAZIfWis6CU9yYgGFMJBIZZogug-RHqnXHFphVC-3_zgFeSlim532grRSA01gD5qD9utQE754l6fUmxd85eISqQbHlpLaxTD1elPtz1SVRRrof477I8X4UcYkfjO1T7yXLAVC6Lxr5emGlooz4OTk_WnPcD5j9La7-NNSI2eJCbbmy2q13n8tKHt16N5o-m9Mu4k5KNgvSZcFkGZ9lm-3Lu18IgzkRonylsvEgC6u6FyKEMRN72E8Rqr)
13. [plos.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE35jsJdZE954ga_FU8xjtGoOJh0TW_9i8_IeRpJSN6Sc059tNuKoaYb7AzGgR4IJCdoYvxxmAD-YAioJiypF1VEI39ksYC0j-qsvcF67Ng_x0ACE0CE8_wX2XnkYb1RSEqlqmzCqP5MJJAuql2FQhSdIkOK8LfdknevMHjaYnD)


## Annotations
Annotation(end_index=2172, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmaUSRSRSPya4DIK03ivfa09s1YzirYuB0D06VdPPKKtZTwUqiwdJ_erXgE9PrASXWNceyJJjTYQIFQ7OqhHO4ycmo1l_a2W3hJ5qzXeMON5IGeVYwgSg_x-waLndRFw==', start_index=2163)
Annotation(end_index=2867, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-phy8vSBklxQbYpb2GFLXWvcAD_xWhraTGuQB7BUNlaQPRjOjJX-72TMqHxE9KcaaJ35SKd11BbaPKYoLMP0RD-cHGuX9vTf0j2IAXNm5qTJrqNyO', start_index=2855)
Annotation(end_index=2867, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoib3TQIjGCDR2IEsCah7IPLXIXgMcU9XZWb41VrxjD9f3nQWQPICikvbwkV_LiKzT24HN8p5TbE9t1JEkYYQ07wusOhgEC1P0Mstwf6SrpSd830AJF_ZVu2MGca2qCA==', start_index=2855)
Annotation(end_index=3960, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmaUSRSRSPya4DIK03ivfa09s1YzirYuB0D06VdPPKKtZTwUqiwdJ_erXgE9PrASXWNceyJJjTYQIFQ7OqhHO4ycmo1l_a2W3hJ5qzXeMON5IGeVYwgSg_x-waLndRFw==', start_index=3951)
Annotation(end_index=4335, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa8wUYIIrjDNA6jrV_dzZ4s7QNPjw7Q8xTKaD4G_o7eMjOuXYa_5PnVMNY_KeHlcjWaN2grk-l_BL7op0zm254GqKlvGVL9xMCh40FWW2kboFPdOY849hm62Innq5MgteNl4fjqA_x', start_index=4326)
Annotation(end_index=4541, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa8wUYIIrjDNA6jrV_dzZ4s7QNPjw7Q8xTKaD4G_o7eMjOuXYa_5PnVMNY_KeHlcjWaN2grk-l_BL7op0zm254GqKlvGVL9xMCh40FWW2kboFPdOY849hm62Innq5MgteNl4fjqA_x', start_index=4529)
Annotation(end_index=4541, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2y_AOtS_kPVFklegmqg-QVsrrV91EvX3uK9e4TstaMQde8SJKPldNlK-8PoVOlEjhHsF6GfkvM1Ca7O_l8_O0p4AAZ_F2CbTeTdplCFnFiiIjg_v1L3i-0yGFxoF6svhqGxXCoPwzarkYfKJJYZPvOlI6X1hhCaErJvXkUKaPnunPEgD1-8gWP_2SM0NORDu1mvDXVmQ8V1R_u8GjD8w_U9aDPDJztf9h8dFCCG-JZ6u32gtb6EvzkM-XOY0MRrL0-w==', start_index=4529)
Annotation(end_index=4827, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa8wUYIIrjDNA6jrV_dzZ4s7QNPjw7Q8xTKaD4G_o7eMjOuXYa_5PnVMNY_KeHlcjWaN2grk-l_BL7op0zm254GqKlvGVL9xMCh40FWW2kboFPdOY849hm62Innq5MgteNl4fjqA_x', start_index=4818)
Annotation(end_index=5462, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa8wUYIIrjDNA6jrV_dzZ4s7QNPjw7Q8xTKaD4G_o7eMjOuXYa_5PnVMNY_KeHlcjWaN2grk-l_BL7op0zm254GqKlvGVL9xMCh40FWW2kboFPdOY849hm62Innq5MgteNl4fjqA_x', start_index=5453)
Annotation(end_index=5835, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEulzRkfpVuF0-TGNXo5qnbct6qg5va_yJFWqViJ8Kq-mnBdkTaF3oQvcVBbjFXlywnQti5EQ_Q6X4-d1_yxWyuKwBMkEfvaVI_fM3KFXCJthO2FWGf0rkCcfBLKOv2GT6lDAu5SYkgOHLZs4094iYGaq7cLZfmA10rhJ6pRQ-ZQw9LXZCO_uPG-KYoCgBziJ3X5sfjal1OCMtc3syitbNrCQ==', start_index=5823)
Annotation(end_index=5835, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIXHLuF8VNBEzC2k5-LnrFdBAQY7-gRtZsn7XGg6_kO2_YAReG5mw8E5nDYoYJ1Y8quKtW-QsliXDF7fka2rG6-vGWU1UQQau_QO6sMoSRLKe4bTt2HW8LksX8UjPxFRac2UQklVsdeo3OyeVH2pXJ-j1TD8RtFhyLbc7zQGbkqFG9z9EZrK5MI1KveQ8Y_3iyh1NGAEc-UGq1tUUYSmX2PyqcVEsqIHvReh353EBNSchav0qx3adfPdVV8eR_dTPJRrVuTIYLkX966Fajb7ujNTEbISbza-7GpdB1GwHKACDWU8lvj9K7EsWEqrjWgc6RTP5M748VEAmFMLW6BVcYYQ==', start_index=5823)
Annotation(end_index=6213, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUinqzMqFD6P4vjHuZ1Tsa8vQWriTDXE5_U8c_nUdLB-GXEdN3bdGfLwgLdxpx2BkPZxcVY890abXEc5hKxu6JdoaaPURnuYAK_I0WJGuggrjoacm4yhL_yoO5BcASnkZXhhyT00pluOmATLT6VuW8IiQwVzNjS7w6ZwPcU6ARwqOpFWFpZdCXTJ1K6jh7-IrlLhjqFtkW9sp-1LTg99wd_wON6FDdavgTIj_34A==', start_index=6201)
Annotation(end_index=6213, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoib3TQIjGCDR2IEsCah7IPLXIXgMcU9XZWb41VrxjD9f3nQWQPICikvbwkV_LiKzT24HN8p5TbE9t1JEkYYQ07wusOhgEC1P0Mstwf6SrpSd830AJF_ZVu2MGca2qCA==', start_index=6201)
Annotation(end_index=6443, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUinqzMqFD6P4vjHuZ1Tsa8vQWriTDXE5_U8c_nUdLB-GXEdN3bdGfLwgLdxpx2BkPZxcVY890abXEc5hKxu6JdoaaPURnuYAK_I0WJGuggrjoacm4yhL_yoO5BcASnkZXhhyT00pluOmATLT6VuW8IiQwVzNjS7w6ZwPcU6ARwqOpFWFpZdCXTJ1K6jh7-IrlLhjqFtkW9sp-1LTg99wd_wON6FDdavgTIj_34A==', start_index=6431)
Annotation(end_index=6443, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIWo5zsBXUfyMldbBA0_cFi03_w6fiE5nAZpscwmHHfbYErgnhHCFhjj3FSmoan7y4yL4nkbs1lpjqr4Of2dYFe1Vwd9Xg5N5M7zlByNmpEaiE3Gy_3-Yb0DYy_Dm2OPPu4ocOqMITGax8IkWFq8k8edGFDPJwnKryp8s49i6jR_zbpbY=', start_index=6431)
Annotation(end_index=6748, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUinqzMqFD6P4vjHuZ1Tsa8vQWriTDXE5_U8c_nUdLB-GXEdN3bdGfLwgLdxpx2BkPZxcVY890abXEc5hKxu6JdoaaPURnuYAK_I0WJGuggrjoacm4yhL_yoO5BcASnkZXhhyT00pluOmATLT6VuW8IiQwVzNjS7w6ZwPcU6ARwqOpFWFpZdCXTJ1K6jh7-IrlLhjqFtkW9sp-1LTg99wd_wON6FDdavgTIj_34A==', start_index=6739)
Annotation(end_index=7508, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoib3TQIjGCDR2IEsCah7IPLXIXgMcU9XZWb41VrxjD9f3nQWQPICikvbwkV_LiKzT24HN8p5TbE9t1JEkYYQ07wusOhgEC1P0Mstwf6SrpSd830AJF_ZVu2MGca2qCA==', start_index=7499)
Annotation(end_index=7847, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-phy8vSBklxQbYpb2GFLXWvcAD_xWhraTGuQB7BUNlaQPRjOjJX-72TMqHxE9KcaaJ35SKd11BbaPKYoLMP0RD-cHGuX9vTf0j2IAXNm5qTJrqNyO', start_index=7834)
Annotation(end_index=7847, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8Aw8vvUCqJc0T37cDJl49cRgPryqZd5eph1Q3feQL7IVtenIhDEC37rLVxikiOWK4nYsoq7ErPZjVA9WaLJ8QakY6B4_nCMhgYjfsQ0zdMCMmeQslDRpjwSFesvPp9Dr-SCCBpndB6d3UmjIThgNsc8pgW9_aGapUnQ-qA6hSAgjcQ1cOQd2kFCQtmlmydJqvkApQ3N06TKML3WAeh1bedaIhyI6V2bZJgJpcoSU2j05Or54ekYWBkOS7KaiwbpG4PITgTDfqOkLEgHUIGjZ3whYhcL5XCrNERh82zorKUo3OLF5EDXgDyJtkvDfKnPkxgUXbvQNpAuHpobbE', start_index=7834)
Annotation(end_index=8185, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa8wUYIIrjDNA6jrV_dzZ4s7QNPjw7Q8xTKaD4G_o7eMjOuXYa_5PnVMNY_KeHlcjWaN2grk-l_BL7op0zm254GqKlvGVL9xMCh40FWW2kboFPdOY849hm62Innq5MgteNl4fjqA_x', start_index=8176)
Annotation(end_index=8525, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIWo5zsBXUfyMldbBA0_cFi03_w6fiE5nAZpscwmHHfbYErgnhHCFhjj3FSmoan7y4yL4nkbs1lpjqr4Of2dYFe1Vwd9Xg5N5M7zlByNmpEaiE3Gy_3-Yb0DYy_Dm2OPPu4ocOqMITGax8IkWFq8k8edGFDPJwnKryp8s49i6jR_zbpbY=', start_index=8512)
Annotation(end_index=8525, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpZEtzYn5eDsCIptFFDF7VYE4y-XatMMk8upWPORy7TpEX1E0jSYV0Naopb2wFR1CiYqQoVd1AfVEccGhyA4hhXnq2knTxpRLpAjzuIlKV7fioCf539E9TbA4mOCrW4VvRGAd_hpxLuUGyc-mUB_FN9TxS8Ju66wzZRMuwAJRrlA75duPG8dTbQ_S_-mxnniJxQL7bZP29UJqJXZRcK1trRJkUAovvVy7CqEvJJzo6AqjIL2UCa5s1VoiHGw0n6O6eH-jzg0JsSuLjeP9Ip0rrVtGPyM5FmAWoRg==', start_index=8512)
Annotation(end_index=9071, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa8wUYIIrjDNA6jrV_dzZ4s7QNPjw7Q8xTKaD4G_o7eMjOuXYa_5PnVMNY_KeHlcjWaN2grk-l_BL7op0zm254GqKlvGVL9xMCh40FWW2kboFPdOY849hm62Innq5MgteNl4fjqA_x', start_index=9062)
Annotation(end_index=9449, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmaUSRSRSPya4DIK03ivfa09s1YzirYuB0D06VdPPKKtZTwUqiwdJ_erXgE9PrASXWNceyJJjTYQIFQ7OqhHO4ycmo1l_a2W3hJ5qzXeMON5IGeVYwgSg_x-waLndRFw==', start_index=9440)
Annotation(end_index=9902, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmaUSRSRSPya4DIK03ivfa09s1YzirYuB0D06VdPPKKtZTwUqiwdJ_erXgE9PrASXWNceyJJjTYQIFQ7OqhHO4ycmo1l_a2W3hJ5qzXeMON5IGeVYwgSg_x-waLndRFw==', start_index=9893)
Annotation(end_index=10430, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa8wUYIIrjDNA6jrV_dzZ4s7QNPjw7Q8xTKaD4G_o7eMjOuXYa_5PnVMNY_KeHlcjWaN2grk-l_BL7op0zm254GqKlvGVL9xMCh40FWW2kboFPdOY849hm62Innq5MgteNl4fjqA_x', start_index=10421)
Annotation(end_index=10900, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-phy8vSBklxQbYpb2GFLXWvcAD_xWhraTGuQB7BUNlaQPRjOjJX-72TMqHxE9KcaaJ35SKd11BbaPKYoLMP0RD-cHGuX9vTf0j2IAXNm5qTJrqNyO', start_index=10887)
Annotation(end_index=10900, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8Aw8vvUCqJc0T37cDJl49cRgPryqZd5eph1Q3feQL7IVtenIhDEC37rLVxikiOWK4nYsoq7ErPZjVA9WaLJ8QakY6B4_nCMhgYjfsQ0zdMCMmeQslDRpjwSFesvPp9Dr-SCCBpndB6d3UmjIThgNsc8pgW9_aGapUnQ-qA6hSAgjcQ1cOQd2kFCQtmlmydJqvkApQ3N06TKML3WAeh1bedaIhyI6V2bZJgJpcoSU2j05Or54ekYWBkOS7KaiwbpG4PITgTDfqOkLEgHUIGjZ3whYhcL5XCrNERh82zorKUo3OLF5EDXgDyJtkvDfKnPkxgUXbvQNpAuHpobbE', start_index=10887)
Annotation(end_index=10993, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-phy8vSBklxQbYpb2GFLXWvcAD_xWhraTGuQB7BUNlaQPRjOjJX-72TMqHxE9KcaaJ35SKd11BbaPKYoLMP0RD-cHGuX9vTf0j2IAXNm5qTJrqNyO', start_index=10984)
Annotation(end_index=11192, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-phy8vSBklxQbYpb2GFLXWvcAD_xWhraTGuQB7BUNlaQPRjOjJX-72TMqHxE9KcaaJ35SKd11BbaPKYoLMP0RD-cHGuX9vTf0j2IAXNm5qTJrqNyO', start_index=11179)
Annotation(end_index=11192, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEblAZIfWis6CU9yYgGFMJBIZZogug-RHqnXHFphVC-3_zgFeSlim532grRSA01gD5qD9utQE754l6fUmxd85eISqQbHlpLaxTD1elPtz1SVRRrof477I8X4UcYkfjO1T7yXLAVC6Lxr5emGlooz4OTk_WnPcD5j9La7-NNSI2eJCbbmy2q13n8tKHt16N5o-m9Mu4k5KNgvSZcFkGZ9lm-3Lu18IgzkRonylsvEgC6u6FyKEMRN72E8Rqr', start_index=11179)
Annotation(end_index=11335, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa8wUYIIrjDNA6jrV_dzZ4s7QNPjw7Q8xTKaD4G_o7eMjOuXYa_5PnVMNY_KeHlcjWaN2grk-l_BL7op0zm254GqKlvGVL9xMCh40FWW2kboFPdOY849hm62Innq5MgteNl4fjqA_x', start_index=11326)
Annotation(end_index=11546, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE35jsJdZE954ga_FU8xjtGoOJh0TW_9i8_IeRpJSN6Sc059tNuKoaYb7AzGgR4IJCdoYvxxmAD-YAioJiypF1VEI39ksYC0j-qsvcF67Ng_x0ACE0CE8_wX2XnkYb1RSEqlqmzCqP5MJJAuql2FQhSdIkOK8LfdknevMHjaYnD', start_index=11533)
Annotation(end_index=11546, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa8wUYIIrjDNA6jrV_dzZ4s7QNPjw7Q8xTKaD4G_o7eMjOuXYa_5PnVMNY_KeHlcjWaN2grk-l_BL7op0zm254GqKlvGVL9xMCh40FWW2kboFPdOY849hm62Innq5MgteNl4fjqA_x', start_index=11533)
Annotation(end_index=11815, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE35jsJdZE954ga_FU8xjtGoOJh0TW_9i8_IeRpJSN6Sc059tNuKoaYb7AzGgR4IJCdoYvxxmAD-YAioJiypF1VEI39ksYC0j-qsvcF67Ng_x0ACE0CE8_wX2XnkYb1RSEqlqmzCqP5MJJAuql2FQhSdIkOK8LfdknevMHjaYnD', start_index=11802)
Annotation(end_index=11815, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa8wUYIIrjDNA6jrV_dzZ4s7QNPjw7Q8xTKaD4G_o7eMjOuXYa_5PnVMNY_KeHlcjWaN2grk-l_BL7op0zm254GqKlvGVL9xMCh40FWW2kboFPdOY849hm62Innq5MgteNl4fjqA_x', start_index=11802)
Annotation(end_index=12351, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa8wUYIIrjDNA6jrV_dzZ4s7QNPjw7Q8xTKaD4G_o7eMjOuXYa_5PnVMNY_KeHlcjWaN2grk-l_BL7op0zm254GqKlvGVL9xMCh40FWW2kboFPdOY849hm62Innq5MgteNl4fjqA_x', start_index=12342)
Annotation(end_index=12740, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUinqzMqFD6P4vjHuZ1Tsa8vQWriTDXE5_U8c_nUdLB-GXEdN3bdGfLwgLdxpx2BkPZxcVY890abXEc5hKxu6JdoaaPURnuYAK_I0WJGuggrjoacm4yhL_yoO5BcASnkZXhhyT00pluOmATLT6VuW8IiQwVzNjS7w6ZwPcU6ARwqOpFWFpZdCXTJ1K6jh7-IrlLhjqFtkW9sp-1LTg99wd_wON6FDdavgTIj_34A==', start_index=12731)
Annotation(end_index=13335, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEblAZIfWis6CU9yYgGFMJBIZZogug-RHqnXHFphVC-3_zgFeSlim532grRSA01gD5qD9utQE754l6fUmxd85eISqQbHlpLaxTD1elPtz1SVRRrof477I8X4UcYkfjO1T7yXLAVC6Lxr5emGlooz4OTk_WnPcD5j9La7-NNSI2eJCbbmy2q13n8tKHt16N5o-m9Mu4k5KNgvSZcFkGZ9lm-3Lu18IgzkRonylsvEgC6u6FyKEMRN72E8Rqr', start_index=13325)
Annotation(end_index=13807, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIWo5zsBXUfyMldbBA0_cFi03_w6fiE5nAZpscwmHHfbYErgnhHCFhjj3FSmoan7y4yL4nkbs1lpjqr4Of2dYFe1Vwd9Xg5N5M7zlByNmpEaiE3Gy_3-Yb0DYy_Dm2OPPu4ocOqMITGax8IkWFq8k8edGFDPJwnKryp8s49i6jR_zbpbY=', start_index=13794)
Annotation(end_index=13807, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpZEtzYn5eDsCIptFFDF7VYE4y-XatMMk8upWPORy7TpEX1E0jSYV0Naopb2wFR1CiYqQoVd1AfVEccGhyA4hhXnq2knTxpRLpAjzuIlKV7fioCf539E9TbA4mOCrW4VvRGAd_hpxLuUGyc-mUB_FN9TxS8Ju66wzZRMuwAJRrlA75duPG8dTbQ_S_-mxnniJxQL7bZP29UJqJXZRcK1trRJkUAovvVy7CqEvJJzo6AqjIL2UCa5s1VoiHGw0n6O6eH-jzg0JsSuLjeP9Ip0rrVtGPyM5FmAWoRg==', start_index=13794)
Annotation(end_index=14092, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa8wUYIIrjDNA6jrV_dzZ4s7QNPjw7Q8xTKaD4G_o7eMjOuXYa_5PnVMNY_KeHlcjWaN2grk-l_BL7op0zm254GqKlvGVL9xMCh40FWW2kboFPdOY849hm62Innq5MgteNl4fjqA_x', start_index=14083)
Annotation(end_index=14736, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmaUSRSRSPya4DIK03ivfa09s1YzirYuB0D06VdPPKKtZTwUqiwdJ_erXgE9PrASXWNceyJJjTYQIFQ7OqhHO4ycmo1l_a2W3hJ5qzXeMON5IGeVYwgSg_x-waLndRFw==', start_index=14727)
Annotation(end_index=15312, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa8wUYIIrjDNA6jrV_dzZ4s7QNPjw7Q8xTKaD4G_o7eMjOuXYa_5PnVMNY_KeHlcjWaN2grk-l_BL7op0zm254GqKlvGVL9xMCh40FWW2kboFPdOY849hm62Innq5MgteNl4fjqA_x', start_index=15303)
Annotation(end_index=15763, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa8wUYIIrjDNA6jrV_dzZ4s7QNPjw7Q8xTKaD4G_o7eMjOuXYa_5PnVMNY_KeHlcjWaN2grk-l_BL7op0zm254GqKlvGVL9xMCh40FWW2kboFPdOY849hm62Innq5MgteNl4fjqA_x', start_index=15754)
Annotation(end_index=17148, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmaUSRSRSPya4DIK03ivfa09s1YzirYuB0D06VdPPKKtZTwUqiwdJ_erXgE9PrASXWNceyJJjTYQIFQ7OqhHO4ycmo1l_a2W3hJ5qzXeMON5IGeVYwgSg_x-waLndRFw==', start_index=17139)
Annotation(end_index=17221, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa8wUYIIrjDNA6jrV_dzZ4s7QNPjw7Q8xTKaD4G_o7eMjOuXYa_5PnVMNY_KeHlcjWaN2grk-l_BL7op0zm254GqKlvGVL9xMCh40FWW2kboFPdOY849hm62Innq5MgteNl4fjqA_x', start_index=17212)
Annotation(end_index=17283, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUinqzMqFD6P4vjHuZ1Tsa8vQWriTDXE5_U8c_nUdLB-GXEdN3bdGfLwgLdxpx2BkPZxcVY890abXEc5hKxu6JdoaaPURnuYAK_I0WJGuggrjoacm4yhL_yoO5BcASnkZXhhyT00pluOmATLT6VuW8IiQwVzNjS7w6ZwPcU6ARwqOpFWFpZdCXTJ1K6jh7-IrlLhjqFtkW9sp-1LTg99wd_wON6FDdavgTIj_34A==', start_index=17274)
Annotation(end_index=17387, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoib3TQIjGCDR2IEsCah7IPLXIXgMcU9XZWb41VrxjD9f3nQWQPICikvbwkV_LiKzT24HN8p5TbE9t1JEkYYQ07wusOhgEC1P0Mstwf6SrpSd830AJF_ZVu2MGca2qCA==', start_index=17378)
Annotation(end_index=17437, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIWo5zsBXUfyMldbBA0_cFi03_w6fiE5nAZpscwmHHfbYErgnhHCFhjj3FSmoan7y4yL4nkbs1lpjqr4Of2dYFe1Vwd9Xg5N5M7zlByNmpEaiE3Gy_3-Yb0DYy_Dm2OPPu4ocOqMITGax8IkWFq8k8edGFDPJwnKryp8s49i6jR_zbpbY=', start_index=17428)
Annotation(end_index=17494, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-phy8vSBklxQbYpb2GFLXWvcAD_xWhraTGuQB7BUNlaQPRjOjJX-72TMqHxE9KcaaJ35SKd11BbaPKYoLMP0RD-cHGuX9vTf0j2IAXNm5qTJrqNyO', start_index=17485)
Annotation(end_index=17535, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEblAZIfWis6CU9yYgGFMJBIZZogug-RHqnXHFphVC-3_zgFeSlim532grRSA01gD5qD9utQE754l6fUmxd85eISqQbHlpLaxTD1elPtz1SVRRrof477I8X4UcYkfjO1T7yXLAVC6Lxr5emGlooz4OTk_WnPcD5j9La7-NNSI2eJCbbmy2q13n8tKHt16N5o-m9Mu4k5KNgvSZcFkGZ9lm-3Lu18IgzkRonylsvEgC6u6FyKEMRN72E8Rqr', start_index=17525)
Annotation(end_index=17593, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8Aw8vvUCqJc0T37cDJl49cRgPryqZd5eph1Q3feQL7IVtenIhDEC37rLVxikiOWK4nYsoq7ErPZjVA9WaLJ8QakY6B4_nCMhgYjfsQ0zdMCMmeQslDRpjwSFesvPp9Dr-SCCBpndB6d3UmjIThgNsc8pgW9_aGapUnQ-qA6hSAgjcQ1cOQd2kFCQtmlmydJqvkApQ3N06TKML3WAeh1bedaIhyI6V2bZJgJpcoSU2j05Or54ekYWBkOS7KaiwbpG4PITgTDfqOkLEgHUIGjZ3whYhcL5XCrNERh82zorKUo3OLF5EDXgDyJtkvDfKnPkxgUXbvQNpAuHpobbE', start_index=17583)
Annotation(end_index=17633, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmaUSRSRSPya4DIK03ivfa09s1YzirYuB0D06VdPPKKtZTwUqiwdJ_erXgE9PrASXWNceyJJjTYQIFQ7OqhHO4ycmo1l_a2W3hJ5qzXeMON5IGeVYwgSg_x-waLndRFw==', start_index=17624)
Annotation(end_index=17680, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIXHLuF8VNBEzC2k5-LnrFdBAQY7-gRtZsn7XGg6_kO2_YAReG5mw8E5nDYoYJ1Y8quKtW-QsliXDF7fka2rG6-vGWU1UQQau_QO6sMoSRLKe4bTt2HW8LksX8UjPxFRac2UQklVsdeo3OyeVH2pXJ-j1TD8RtFhyLbc7zQGbkqFG9z9EZrK5MI1KveQ8Y_3iyh1NGAEc-UGq1tUUYSmX2PyqcVEsqIHvReh353EBNSchav0qx3adfPdVV8eR_dTPJRrVuTIYLkX966Fajb7ujNTEbISbza-7GpdB1GwHKACDWU8lvj9K7EsWEqrjWgc6RTP5M748VEAmFMLW6BVcYYQ==', start_index=17671)
Annotation(end_index=17742, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa8wUYIIrjDNA6jrV_dzZ4s7QNPjw7Q8xTKaD4G_o7eMjOuXYa_5PnVMNY_KeHlcjWaN2grk-l_BL7op0zm254GqKlvGVL9xMCh40FWW2kboFPdOY849hm62Innq5MgteNl4fjqA_x', start_index=17733)
Annotation(end_index=17779, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUinqzMqFD6P4vjHuZ1Tsa8vQWriTDXE5_U8c_nUdLB-GXEdN3bdGfLwgLdxpx2BkPZxcVY890abXEc5hKxu6JdoaaPURnuYAK_I0WJGuggrjoacm4yhL_yoO5BcASnkZXhhyT00pluOmATLT6VuW8IiQwVzNjS7w6ZwPcU6ARwqOpFWFpZdCXTJ1K6jh7-IrlLhjqFtkW9sp-1LTg99wd_wON6FDdavgTIj_34A==', start_index=17770)
Annotation(end_index=17834, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpZEtzYn5eDsCIptFFDF7VYE4y-XatMMk8upWPORy7TpEX1E0jSYV0Naopb2wFR1CiYqQoVd1AfVEccGhyA4hhXnq2knTxpRLpAjzuIlKV7fioCf539E9TbA4mOCrW4VvRGAd_hpxLuUGyc-mUB_FN9TxS8Ju66wzZRMuwAJRrlA75duPG8dTbQ_S_-mxnniJxQL7bZP29UJqJXZRcK1trRJkUAovvVy7CqEvJJzo6AqjIL2UCa5s1VoiHGw0n6O6eH-jzg0JsSuLjeP9Ip0rrVtGPyM5FmAWoRg==', start_index=17824)
Annotation(end_index=17889, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE35jsJdZE954ga_FU8xjtGoOJh0TW_9i8_IeRpJSN6Sc059tNuKoaYb7AzGgR4IJCdoYvxxmAD-YAioJiypF1VEI39ksYC0j-qsvcF67Ng_x0ACE0CE8_wX2XnkYb1RSEqlqmzCqP5MJJAuql2FQhSdIkOK8LfdknevMHjaYnD', start_index=17879)
Annotation(end_index=17926, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2y_AOtS_kPVFklegmqg-QVsrrV91EvX3uK9e4TstaMQde8SJKPldNlK-8PoVOlEjhHsF6GfkvM1Ca7O_l8_O0p4AAZ_F2CbTeTdplCFnFiiIjg_v1L3i-0yGFxoF6svhqGxXCoPwzarkYfKJJYZPvOlI6X1hhCaErJvXkUKaPnunPEgD1-8gWP_2SM0NORDu1mvDXVmQ8V1R_u8GjD8w_U9aDPDJztf9h8dFCCG-JZ6u32gtb6EvzkM-XOY0MRrL0-w==', start_index=17917)
Annotation(end_index=17973, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa8wUYIIrjDNA6jrV_dzZ4s7QNPjw7Q8xTKaD4G_o7eMjOuXYa_5PnVMNY_KeHlcjWaN2grk-l_BL7op0zm254GqKlvGVL9xMCh40FWW2kboFPdOY849hm62Innq5MgteNl4fjqA_x', start_index=17964)

## Sources
