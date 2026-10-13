# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 01bd975d | **Time:** 388.58s | **Cost:** $1.38767
--------------------------------------------------------------------------------

# Optimizing Sentinel Surveillance: Balancing Early Warning Sensitivity and Resource Efficiency in ILI Monitoring

### Key Points
*   **Sentinel Surveillance Efficiency:** Sentinel systems optimize resources by monitoring a subset of the population (e.g., specific general practitioners or hospitals) rather than the entire population. Mathematical optimization models, such as the Maximal Coverage Model (MCM), demonstrate that strategic site selection can achieve equivalent population coverage with significantly fewer sites than voluntary networks, directly reducing resource consumption while maintaining sensitivity.
*   **Threshold Methodologies:** The Moving Epidemic Method (MEM) has emerged as a gold standard for establishing Influenza-Like Illness (ILI) thresholds. It offers a robust statistical framework that balances sensitivity (typically >80%) and specificity (>90%), minimizing false alarms that trigger costly public health responses.
*   **Cost-Benefit of Testing:** Resource consumption is optimized by limiting confirmatory laboratory testing to specific prevalence windows. Research indicates that rapid testing is most cost-beneficial when influenza prevalence is between 30% and 40%; outside this range, empiric treatment or no treatment is often more economically efficient.
*   **Predictive Integration:** Advanced machine learning models (e.g., XGBoost, SARIMA) and dynamic downscaling techniques allow systems to transition from reactive thresholds to proactive forecasting. These models integrate multi-source data (clinical, meteorological, digital) to predict epidemic onset weeks in advance, allowing for "just-in-time" resource allocation.
*   **Adaptive Systems:** Static thresholds often fail during atypical seasons (e.g., pandemics). Adaptive risk metrics and dynamic thresholds that update in real-time based on current transmission dynamics prevent system saturation and maintain relevance when historical baselines are disrupted.

---

## 1. Introduction

Infectious disease surveillance is the cornerstone of public health preparedness, yet it operates under a fundamental constraint: the tension between the need for rapid, sensitive detection of outbreaks and the finite resources available for monitoring and response. Sentinel surveillance systems, particularly those designed for Influenza-Like Illness (ILI), represent a strategic compromise. By collecting high-quality data from a limited number of selected sites, public health authorities aim to infer trends for the broader population without the prohibitive costs of universal surveillance.

The optimization of these systems is critical. A system that is too sensitive may generate frequent false positives, leading to "alarm fatigue," wasted stockpiles of antivirals, and unnecessary mobilization of emergency response teams. Conversely, a system that prioritizes resource conservation may set reporting thresholds too high, missing the early phase of an epidemic when interventions are most effective.

This report provides an exhaustive analysis of how sentinel surveillance systems optimize this trade-off. It examines the statistical methodologies for establishing reporting thresholds, specifically the Moving Epidemic Method (MEM) and the ALERT algorithm. It explores the mathematical frameworks used to "right-size" surveillance networks, such as Maximal Coverage Models (MCM). Furthermore, it investigates the integration of epidemic prediction models—ranging from autoregressive neural networks to dynamic downscaling—that allow for adaptive resource allocation. Finally, it presents a detailed cost-benefit analysis of confirmatory testing and the economic implications of surveillance design.

## 2. Establishing Epidemic Thresholds: The Statistical Foundation

The definition of an "epidemic" within a surveillance system is not merely biological but statistical. It relies on establishing a baseline of expected activity and determining a threshold above which activity is considered aberrant. The precision of this threshold determines the system's sensitivity (ability to detect true outbreaks) and specificity (ability to ignore background noise).

### 2.1 The Moving Epidemic Method (MEM)
The Moving Epidemic Method (MEM) has become the standard for influenza surveillance in Europe and is increasingly adopted globally. Unlike simple historical averages, MEM applies a complex statistical approach to historical data to define pre-epidemic, epidemic, and post-epidemic periods.

#### 2.1.1 Methodology and Calculation
MEM calculates the epidemic threshold based on the geometric mean of the incidence rates of the pre-epidemic period (usually the 30 highest weekly rates from non-epidemic periods of historical seasons) and their standard deviation. The method constructs a baseline curve and establishes intensity levels (low, medium, high, very high) [cite: 1, 2, 3].

The core advantage of MEM is its stability and adaptability. By using a cross-validation procedure—often leaving out one season at a time to test the model—MEM ensures that the threshold is robust against outliers. For example, in a study validating MEM in Hubei Province, China, the method was applied to virology data from 2010 to 2018. The study established specific thresholds for different age groups, finding a threshold of 15.42% for school-aged children, who are often the main transmitters [cite: 4].

#### 2.1.2 Sensitivity and Specificity Trade-offs
The primary metric for optimizing the trade-off between early warning and resource use in MEM is the balance between sensitivity and specificity. A study in Montenegro applying MEM to data from 2010–2018 demonstrated this balance effectively. The calculated pre-epidemic ILI threshold was 19.23 cases per 100,000 population. The model achieved a sensitivity of 89% and a specificity of 99% [cite: 5, 6, 7].

*   **High Specificity (99%):** This is crucial for resource conservation. It implies that the system rarely signals an epidemic when one is not occurring, preventing the waste of resources on false alarms.
*   **High Sensitivity (89%):** This ensures that the vast majority of true epidemic weeks are flagged, facilitating early intervention.

Similarly, a study in Tunisia applying MEM to nine seasons of data found a sensitivity of 85% and a specificity of 69% [cite: 8]. The variation in specificity between regions highlights the need for local calibration of the model parameters (such as the parameter $\delta$, which defines the minimum increment percentage used to find the optimum epidemic duration) to optimize the trade-off for local conditions [cite: 9].

### 2.2 The CDC Methodology
The United States Centers for Disease Control and Prevention (CDC) employs a slightly different statistical approach. The national baseline is developed by calculating the mean percentage of patient visits for ILI during non-influenza weeks for the most recent two seasons and adding two standard deviations. A "non-influenza week" is defined as a period where less than 2% of specimens test positive for influenza [cite: 1, 2].

This method is computationally simpler than MEM but relies heavily on the definition of "non-influenza weeks." If viral circulation is prolonged or if the definition of non-influenza weeks is not rigorous, the baseline may be artificially inflated, reducing sensitivity (raising the bar for an alert). Conversely, if the baseline is too low, the system may trigger alerts due to random noise or other respiratory pathogens (e.g., RSV, COVID-19), consuming resources on investigations that are not influenza-related [cite: 1].

### 2.3 The ALERT Algorithm
While MEM and CDC methods focus on regional or national thresholds, the Above Local Elevated Respiratory Illness Threshold (ALERT) algorithm is designed for community-level or hospital-level detection. This is critical for operational resource allocation, such as opening overflow wards or implementing staffing surges.

The ALERT algorithm uses a threshold-based approach to identify the transition from endemic to epidemic activity. In a study using data from hospitals in Baltimore and Denver, ALERT thresholds were designed to capture 90% of all cases. When applied prospectively, the algorithm successfully identified 71%–91% of all reported cases within the ALERT period [cite: 10].

The optimization here is explicit: users can tune the threshold based on their tolerance for false positives versus their need for capture.
*   **Lower Thresholds:** Result in longer "alert" durations and a higher percentage of cases captured (high sensitivity), but increase the likelihood of early false alarms (resource consumption).
*   **Higher Thresholds:** Reduce the duration of the alert period (saving resources) but risk missing the early phase of the epidemic curve [cite: 10].

### 2.4 Adaptive and Dynamic Thresholds
Static thresholds (like a fixed number of cases) can fail when the underlying dynamics of the disease change, such as during the emergence of a novel pandemic or when multiple respiratory viruses co-circulate.

Research into adaptive risk metrics suggests that thresholds should update in real-time. For example, a study on COVID-19 risk metrics proposed an adaptive method where thresholds for "high risk" designations were updated based on the evolving relationship between cases, hospitalizations, and mortality. This adaptive approach outperformed static metrics in predicting 3-week-ahead mortality and intensive care usage [cite: 11, 12].

In the context of influenza, dynamic thresholds are essential when historical data is disrupted. For instance, the COVID-19 pandemic suppressed influenza circulation for several years, rendering historical baselines (like the 5-year average) unreliable for predicting post-pandemic influenza seasons [cite: 13, 14]. Adaptive models that weigh recent data more heavily or use "nowcasting" techniques allow surveillance systems to remain sensitive without being triggered by the statistical anomalies of a post-pandemic recovery period.

## 3. Optimizing Surveillance Network Design

The physical configuration of the sentinel network—how many sites, where they are located, and whom they serve—is the primary determinant of fixed resource consumption. A network with too many sites wastes money; a network with too few or poorly placed sites lacks sensitivity and representativeness.

### 3.1 Maximal Coverage Models (MCM)
The Maximal Coverage Model (MCM) is a mathematical optimization approach used to select sentinel sites. The objective is to maximize the number of people living within a specified distance (e.g., 20 miles) of a sentinel site, given a fixed number of sites (or fixed budget).

A landmark study in Iowa compared the existing voluntary network of 22 sentinel providers against an optimized network designed using MCM. The results were striking:
*   **Efficiency:** The existing 22 sites covered 56% of the population. An MCM-optimized network could achieve the *same* 56% coverage with only 10 sites [cite: 15, 16].
*   **Enhanced Coverage:** Using the same number of sites (22) but placing them optimally would increase population coverage to over 75%, adding nearly 600,000 residents to the surveillance catchment area [cite: 15].

This demonstrates that resource consumption (the cost of running 22 sites) can yield significantly higher sensitivity (75% vs 56% coverage) simply through mathematical optimization of site placement. Alternatively, the system could reduce resource consumption by closing 12 sites while maintaining the status quo of sensitivity.

### 3.2 K-Median and Greedy Algorithms
While MCM focuses on coverage radius, the K-Median model minimizes the total distance traveled by the population to the nearest sentinel site. This approach is particularly useful for ensuring accessibility and representativeness in rural areas.

Furthermore, "greedy algorithms" are used to sequentially select sites that provide the maximum marginal gain in information. In the context of detecting outbreaks on a network (e.g., a contact network), studies have shown that selecting "sentinels" based on their centrality or contact frequency can drastically reduce the time to detection. For example, monitoring the "friends of randomly selected individuals" (who tend to be more central/connected) allows for earlier detection of contagious outbreaks than monitoring random individuals [cite: 17, 18].

### 3.3 Temporal and Spatial Optimization
Surveillance needs are not static; they vary over time and space.
*   **Temporal Optimization:** Research suggests that sampling frequency can be traded off against the number of sites. In scenarios with slow-moving outbreaks (e.g., certain livestock diseases), visiting fewer sites more frequently may be more cost-effective. However, for rapidly spreading respiratory viruses like influenza, spatial coverage is often prioritized [cite: 19].
*   **Spatial Prediction:** Frameworks like the Disease Surveillance Informatics Optimization and Simulation (DIOS) allow planners to select sites that maximize the spatial prediction of disease prevalence at *unmonitored* sites. This allows the system to infer the status of the entire region based on a sparse, resource-efficient network [cite: 20, 21].

### 3.4 Sample Size and "Right-Sizing"
The concept of "right-sizing" surveillance involves determining the minimum number of specimens required to achieve specific confidence intervals. For virologic surveillance, a threshold of 10% prevalence is often used as a benchmark for situational awareness. The Association of Public Health Laboratories (APHL) and CDC have developed calculators to determine sample sizes that ensure adequate confidence in detecting novel viruses or antiviral resistance without over-testing [cite: 22]. This statistical "right-sizing" prevents the resource drain of testing thousands of negative samples during low-prevalence periods.

## 4. Epidemic Prediction and Forecasting Models

While thresholds detect an epidemic *after* it has crossed a line, prediction models aim to forecast the crossing of that line, allowing for preemptive resource allocation. This shift from reactive to proactive surveillance is a key optimization strategy.

### 4.1 Machine Learning Approaches (XGBoost, SARIMA)
Advanced statistical and machine learning models are increasingly replacing or augmenting traditional regression models.
*   **XGBoost:** This gradient boosting algorithm has shown superior performance in forecasting influenza incidence. A study using WHO FluID data from 32 countries showed that XGBoost models reduced the mean absolute error by 62% for 4-week ahead predictions compared to null models [cite: 23]. By treating incidence as an ordinal variable (e.g., low, medium, high), XGBoost simplifies the prediction task into actionable categories for public health officials.
*   **Ensemble Models:** No single model performs best in all contexts. During the COVID-19 pandemic, when historical patterns were disrupted, simple exponential smoothing models often outperformed complex neural networks. However, ensemble models (combining multiple forecasts) consistently provided stable and reliable predictions, mitigating the risk of relying on a single, potentially failing model [cite: 13, 14].

### 4.2 Dynamic Downscaling
Public health decisions often require daily data, but sentinel systems typically report weekly. "Dynamic downscaling" is a numerical procedure that fuses weekly confirmed case data with daily syndromic data (e.g., emergency department chief complaints) to estimate daily incidence.
*   **Mechanism:** A study in Michigan used Bayesian dynamic downscaling to provide one-day and seven-day forecasts. By utilizing the strong correlation (0.81) between ED constitutional complaints and influenza rates, the model could interpolate daily fluctuations that weekly reports missed [cite: 24].
*   **Optimization:** This allows health departments to detect fast-growing transmission chains days earlier than the official weekly report would allow, optimizing the timing of interventions without increasing the frequency of formal reporting (which would consume more resources).

### 4.3 Integrating Digital Surveillance (Search and Social Data)
Digital surveillance (infodemiology) offers a low-marginal-cost data stream to enhance sensitivity.
*   **Search Queries:** Models integrating Baidu or Google search indices with traditional ILI data have shown the ability to anticipate epidemics by 1–3 weeks. For instance, the ARGO (AutoRegression with GOogle search data) model reduces forecasting error by 20–35% compared to autoregressive models alone [cite: 25, 26].
*   **Resource Implication:** These data sources are essentially free to the public health agency (once the pipeline is built), providing a high-sensitivity signal that can trigger targeted, resource-intensive investigation only when necessary. However, reliance solely on these can lead to false positives (as seen with Google Flu Trends), so they are best used as part of a hybrid system [cite: 27, 28].

## 5. Resource Consumption and Cost-Benefit Analysis

The ultimate metric for optimization is economic: does the cost of the surveillance and subsequent intervention justify the health benefits?

### 5.1 The Economics of Confirmatory Testing
A critical decision in sentinel surveillance is when to perform expensive PCR or culture tests versus relying on clinical diagnosis (syndromic surveillance).
*   **The 30-40% Window:** Cost-benefit analyses have identified a specific prevalence window where rapid testing is economically viable. For neuraminidase inhibitors, testing is most cost-beneficial when influenza prevalence is between 30% and 40%.
    *   **Below 30%:** The Positive Predictive Value (PPV) is low; testing yields too many false positives or negatives relative to the risk, and "no treatment" or watchful waiting is often preferred.
    *   **Above 40%:** The pre-test probability is so high that empiric treatment (treating based on symptoms without a test) is more cost-effective than testing. Testing in this scenario consumes resources to confirm what is already statistically probable [cite: 29].
*   **Point-of-Care Testing (POCT):** A study in Hong Kong elderly patients showed that while POCT increased upfront costs, it reduced hospitalization rates (1.38% vs 2.85%) and mortality. The Incremental Cost-Effectiveness Ratio (ICER) was ~$29,582 per QALY saved, which was deemed cost-effective [cite: 30].

### 5.2 The Cost of False Positives
Optimizing for high sensitivity often leads to false positives. In a low-prevalence environment (e.g., the 2020-2021 flu season suppressed by COVID measures), rapid antigen tests showed a high rate of false positives (100% in one cluster of 22 cases). This resulted in unnecessary antiviral use and isolation protocols, highlighting the resource drain of maintaining high-sensitivity thresholds during non-epidemic periods [cite: 31].
*   **Optimization Strategy:** To mitigate this, protocols often require confirmatory molecular testing for "first detections" or when prevalence is low, switching to syndromic monitoring once the epidemic is established [cite: 32].

### 5.3 Sentinel vs. Population-Based Costs
Sentinel surveillance is inherently a cost-reduction strategy. It utilizes 1-5% of physicians to estimate national trends. While it cannot calculate precise incidence rates (due to denominator uncertainty), it provides the necessary trend data for 90% of public health decisions at a fraction of the cost of population-based registries. The trade-off is a lack of representativeness, particularly in rural or underserved areas, which MCM optimization attempts to correct [cite: 33, 34, 35].

## 6. Conclusion

Sentinel surveillance systems optimize the trade-off between early warning sensitivity and resource consumption through a multi-layered approach involving statistical rigor, network design, and economic stratification.

1.  **Statistical Optimization:** By employing the **Moving Epidemic Method (MEM)**, systems achieve a high specificity (99%), ensuring that scarce response resources are not wasted on false alarms, while maintaining sufficient sensitivity (~89%) to detect true outbreaks.
2.  **Structural Optimization:** **Maximal Coverage Models (MCM)** allow public health authorities to reduce the number of sentinel sites by >50% without sacrificing population coverage, or to drastically improve coverage without increasing the budget.
3.  **Operational Optimization:** Economic analyses dictate that expensive confirmatory testing should be restricted to specific prevalence windows (e.g., **30-40%**) or high-risk populations (elderly), relying on empiric treatment or syndromic data outside these bounds.
4.  **Predictive Optimization:** The integration of **machine learning forecasting** and **dynamic downscaling** transforms surveillance from a reactive tool to a proactive one, allowing for the temporal allocation of resources (e.g., staffing, stockpiles) weeks before the peak demand occurs.

Future optimization lies in the adaptive integration of these components—creating systems where thresholds dynamically adjust based on real-time prediction models, and where sentinel sites are fluidly re-tasked based on the changing spatial dynamics of the pathogen.

## 7. References

*   **[cite: 36]** Epidemic prediction models and resource allocation in war.
*   **[cite: 1]** CDC FluView Overview and Threshold Methodology.
*   **[cite: 2]** Methodology used by the USA CDC for ILI and MEM.
*   **[cite: 33]** Sentinel surveillance resource utilization and limitations.
*   **[cite: 5]** MEM performance in Montenegro (Sensitivity/Specificity).
*   **[cite: 10]** The ALERT Algorithm for triggering interventions.
*   **[cite: 13]** Forecasting ILI during COVID-19 using ensemble models.
*   **[cite: 37]** XGBoost for ordinal influenza forecasting.
*   **[cite: 24]** Dynamic downscaling for daily influenza estimates.
*   **[cite: 38]** Optimizing surveillance sites for respiratory disease forecasting.
*   **[cite: 15]** Optimizing sentinel provider locations in Iowa (MCM).
*   **[cite: 29]** Cost-benefit analysis of rapid testing vs. empiric treatment.
*   **[cite: 27]** Google Flu Trends and the problem of false positives.
*   **[cite: 11]** Adaptive risk metrics for COVID-19.
*   **[cite: 22]** Right-sizing virologic surveillance sample sizes.
*   **[cite: 3]** Establishing epidemic thresholds by MEM in Europe.
*   **[cite: 16]** Computational framework for sizing sentinel networks.
*   **[cite: 4]** MEM thresholds for age-specific groups in China.
*   **[cite: 30]** Cost-effectiveness of POCT in Hong Kong elderly.
*   **[cite: 23]** XGBoost forecasting of influenza incidence.

**Sources:**
1. [cdc.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeFeX2I_acv8nWl2jvyq30h9wLNi9fCJZzkyknIsH9FvKtBH6ch4iJOdhJHKyYPuEd9IIDPgrLGFJnCchjc4IN0y2qjvEx3KlTI8K-4gxhMAHdzPkSnIEMV6fbDiJF6NGsmFNBPQ==)
2. [ictp-saifr.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWUX9GxmSHb6TAdrglPeZfW2cQn1OtCFlPxGsO2uNHbUBUQU7PTs-_dYHGAlyeuih3I50lCwOtH-II-G56p48VMsHdgq7QVkbiHcIIWvaAVQlOnNSFVimNH4rlzgUJled0R91yVgZPsG4hQKjvmqHogQlXoxzD4cr-rBJN)
3. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpr03fHoHOSIi2qk1XEg1z_7QGiFegi1CRrmwZrdWd5NIjqtlMyOfYU7wDnOCw9OKRXoQAeVTXEirlKtNxgZwe8XljYunLh0PL4mSDyuBgEAVWgw92prf84MCNBQm8ndIfuANdqcukYlj7gOvpS0bybI-trZHJPNCNjIBy4HSU1Ni_Ar7Oa9lypVh_wbCW1CpZ2pSeYvCoELfsdbC09ck5vIimOhlTHhw2onMwBYo0cWTDCfZKskr4kNFugnDrDKenKQhbXXEZNpE=)
4. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUdgdKGgFJC9PPvve6iKGJNOSHvMyVSgiurgCODE8IOPY-G9hEt8YWMhgzLzD4M2qQe8IrzbUAlzR9CHZOunKeR7_Jsk80dPSxIuW6dRwrqsxRHvWRIvBVQWFJvg_r)
5. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHy8vDnokn4BdjS6bWYyGWl1jN_AMAeNomoUszeTn-bcOjAyKTFhfCFlCVShvR4LyumAElXKfyE0TnufrkvQYAy506a3fJJP-dUuF4UhNa9em586nDINyanmMvQnpVorTdqXeyi-CdR)
6. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfSYiGphZujJWeUNJEy1i0FVt6xRph5YmCM1rx9yDYN7I4xnoIcTrf9CWuV2nN7zUlTJYdOP3bOicj6NYC9zuOIfqs5BJyFfkm-EwttE6NUkT8FNakQPFrThNUDSi6WtY0EF_b75pk_ZvfaJ-AG4CZhdhWc5o9gLuCOw8SWarO_r50sICh3fJHhWLAKjvU6MpZaUc28RYfMMUo-tpIPQrH2FcDi_yeHXA9DAo_30zGMhk9I-uDQld-PKbc57sazWoFHuNFO-_m-xE1LIBovUfWDyjX9VTrJLp4MGfQqwn7CwdOY9NnfgwveQ26uvdDOGdTYJGl8vFyy4yMSRaIJUBokiar1m_cMA==)
7. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLbvHyfhy18hyCX491ixXVzsw5vQdm74A8Y9oWrlPGeP3zG74kwrna8ocKXGz2F_s2nZrgpi-bzq-nzFTuHJ0-GkjkHc_iGI2UtNlCgRjC-ehNQhuHHDtO7RUFNbiXcQ==)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4IBXMBF2v0hqoLg5Z3fkarvAJyCn5TXLgUqyxjPEqHjQ1bL16bAIZRdBHI4wkakf645xKxT2_5xqBbPgjhs0owucXEWgc0SEBXtZ_X40pKA2telazL7Qq0OaLrey84b3c35jgpL-FSumRlm0S1nNnpgrdYCPGa6OLXEioRMRqTA7ang70XSjfp3tiVqwM9CG5yN8odRgNMz6IcXsNDRRKjyPTW32GzvN46mwOpVCjDN34BwjEoGwh-B_AuyDPkhrWLou3wdNC0SZSYHCucTEdobYQ0znbUiRin3AMJDvk0Mw-JkCTej6GCDgv7eZ1XTv6fBa_cnCxzwaiGURFaq1lxUrS_251-_2UZw==)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAtgCCNwcSpqClXFn_huFnDQPI1ACSFqi_P_-_mmnjXwOlBfyU6xM-qZrd5eDM6mVIYo_e85cUv1Eri8euf39d6GB5ey41eIa8KH2gf9jsDqmvuXJi3rG3qUWwgu8XTwHbJM957u2v)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUgJLuNee0nclCbrTCk6hfplz61Bgrn2ZW65sc1njs5y6F3gtAz4mUa7uwGrd9Q9D0XKVQaDUyiTPQqVevTvcgQVOpXaUhb_rWUuOEaABSTKAjwy4u_woYr0TCKPgAhg4G1XbIMGnhcq1QVJL_trrd9_aJXmdS2VUMlt60lH0c_XdZygI8nmrzouZd2w38pe3cVda_ScH1DugbHs6hIAb8J0Lm)
11. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5rC6oFa-e2rhIr-AgTHuG1svu6zoYjq8INKXGr7VKx4ZsoTUnlzUUJ86zm3UeiEi1n7GzEnBYRMooMHWHEQihIablOR_q3b7LeaQ33rS7MVzFKHgpj-eg2cGQ3DdKGt9kYKSFH5OQ-w==)
12. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFf89X_VvoQOi5Xue2oT-xgj6nwkv9Ql3-U2vBC7X0yrslrIOz6aATO95fGDopyv52AKk1M3vUc7nDk-cfG8T8X_Tr51VcHahRHU1HihdOBJpRCgLawssiXh29wuyPu3sMxxB19lTIj)
13. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKNMgmOa3gBDJrJ7Q1u-zQsLSJsan4i5WaMZ5zThR5z00hxBwoAfzSQ-hR_GXc5CueT3LxwmdsNtKM9e_oS9aACeUFtwqXdmrrkUCR0bR376dtw1WBbeRhtqRaaXydC41-DHLoEzW-gwmPM4KNrJyfMEmv3Q5ZtLo4QduZbYi1C3I88Q4DeTptePKVHwHhgihx2DU-zOFyZ3nbi0OLhwkyQ9mcuOOQbHv_zSlr)
14. [medrxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcYba7ZpfuHwSU2FW-N9uomENk5FfAT_aR9u4R4lxZMq53pvpsEGq8nEo2sfsWbt9dBFcrVRi14eWkM9u3YrI-guritkTc1MzJBxN0zJ4LB4T7tvSZ3LQIfAjMEbmpvsJFIuz022EVZiIfEY2w2rAtH9xaU1gsVGNk4gWNeA==)
15. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_DO3nPwKaBA_wlbu7xwD4HLIQZPKRguyjQcmFKi4GQk9qDtDOtRlmqJOw95fM71A1FxHU49vSHJXaW0AKDPoAOFrK_6jddfWMrcwnzTKIblyLo0D-bVIvksnXWRC5hQ==)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvgbZPoIabZ1gTnJLcyltR1YZpd7Oafk2T92WNFZhgD2S4uWkjK404QXYixvrF4Bd2a1x-fQM6Q6njrTpvYa-6ebIHTpX8ukcWDJs_GiuugWsURFQKT9YJc12vLeOQG56T9oX2ZcPS5dmuS5xJxrkQjVJbFkQjhq0Cp8SrWiTdc2Ka_BvK2adPFjXQJzervPKmdTiw8YU3rkbV7L5L5lNdd14_3Y2TbqK4FN8yH5ySdKiHATZtkQSKx1rfYJuN)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpryhPI66AgTnkgn9d3drFB-HBcvxqH_0QiqWLTp8bXRExlLt2aa34zebQIXVxRegXHd7_t0eZcAmt3lmIF8rUQVw-c0UOzswyRLpzzEtdS42RgTXUQ4y0ubJ5iWeMiXLAh5gSSRf2A-2_MMjLjwIAUCObkaWEgka-kTjfgubi5LftNLbJBzhzcl4wjhbdCfoc-dt1vne_EfvX2yTSFOwhJPMjYc4LnW-ZtQ==)
18. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQm50G8Vnmry-RV0Bg8EpOGe6f6RhOT5JQ4ClwpJkIocOtXOrnLjk2zOF_o4iBInEH-LlCAhu7KvAvhxjYZtfnSNZBuDV3oquew4Lh7dAStyMguR9C1vrc6Xc5DyWNRsJnMvhNOMSq)
19. [royalsocietypublishing.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5Q3OnvuYHoN4gNucRjAM6PDbHuUrmECTn0-5ZHVmSayBo_fZTHfvO7VCVNIWQFn8ioYhEvncfDMLUBITifGdAsj5IvwEwjT1WV3xHPsXWTpecSKQe8EyfiWSFP40xjvxedbx6QOMLAhBcd4o_n_kx2RgHF78nOr5XL9771lKhTUvDSQlENWf3hRFCA_SgCiV0UtNcylbGMIBPSq0gM_Q70SsRzLwcXo0=)
20. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoiRVBwLF4MFR8TwwEqCxQNAM2MyHFETnM4cqSHiNapathIsn6y3GRrmR34VaNMqPrSKdBxA7DZ0NH1V0bsOleDfO67r81Rqb5dm4_fjkdco5w6IQ4naspcgskxzLNKSgR-0xlnAAZ)
21. [medrxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE30_SrNgf3xVhNChzQaQzoC0SImZflZeXYYO65omSeG8YbhYvc9ILzTOkPhAkt2iKrDMiHaBkCCLGHoNc9obcsyMvqLqlD7jdipDeL0EvaJyXsvayyIhySzIUlpJeirWSuZmEG5b5McSf8nVsA3t81N1-_)
22. [aphl.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHs5sgna-bj4eL9yzhPyc55hcpzp0-KPhkSEkiAyAN1l9yX3exNVg9HaZFdc62YrUwHUpjJ6xDcvsmOGPjJp-vl5jDezRl2R3YK1QkLPr8mlnyigZ7oe3t9Lf3Ul3HRKivvYX8_lLNtWy4diVeATxH9JTm113RUToZMrG4KT2jjVrWKm5xzD7Th-qKKuP1wuEVhAJcKA_lyyVI-oukammStBtB584AxLmejFZ8bVppeil6KQLX9gAV_Oe2s7d6iu82WUN0xJD81lpQ)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMATDWA10Hoje7QWv1Q8CNX3NiN25F0zAfms3yDoWENll-5OqJH0F-1prN5fu_CkxVzfaXRrM4i5MJCjP4ocKY8XnVMfi_K3wCG9AxUh7nkfsBZfu7HeC-fV_FJ-q40AB0Xr12aUTWrEm-wgN9YnlFeP8A4yMc-od1PZJnC7or5oyAuLPTVkltY1G3Bmlm0H3oF1AlwHpJcM7Sl3s7l4KWTclh9GXeJjErTFvzEfi-fE2wHIqGgpw=)
24. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcb-_adHFaWckRW8b3S4ez1OkNnAi2Fk79Po0GHMuh3vwDmVg2pmYF9p_lODBfO-8wWqlJ_BlTvewb17_4zMonknJUKyiyDX29HOZQqoJptKngYdrIjftrZYKmQbFGz8zYK72AexNn)
25. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHILlV4RiPzCeFAkBCbHJcp_ATHYukq0lMbkZTtxzVlcDMpjz2jylY_0sRcysf9OyFQTqvcWaE9IYS8m-eL6YY0lSXtgJksk6npO7ocAThAJD6I5RXn0lzUt1nZffWJUwC1vlK8hoELCKEWG6yy434TAXHCwKS_zD-2xt6w0y3CGCi9vjdjJSwvCXZaih4WHUZngJHV4NMmh0ijskMGURV3-iqVBubo4_KjbEfAX7o8vTCZbBV5lEYukQ==)
26. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIGGxPnLG3BPTfGM0K5JsPp5oBw3Z3VSs04TqYzuiayOZRMJ7q4dUNr-bng0byD9aSM83foadyUSWTTb7xvmPWhyxg9RuATF_QY5p8vZQw0S1btMQoP54XSU4883hGx6BSda0Xm85H4A==)
27. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpCyy-a5Qumq-B6ntXfW72ya5KgiLi9eEVJ8RN1isQokuhwhPsWcV5BoVGIKY4C5L_mCnqoAHLVxBxLCg3DAne2guwH7pzYHtwvAN8_ggQCkBb442Lgq_WSGkyARmzO5k-YmIEaIUi)
28. [plos.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0i43XIjQ9X6nKmL4Wfm8u6g_bXfwtFZHhsHMRKq3yLBoky-73_6OwD65-WKPduwybJkxBHR7_I7yNn79NoBajWouriB9K6s8oK71KvmnEJ3FE6dxEwyEWph0JPW0jg27_UuRucZ94F1Ng1A_Dip_UKMBG7QIMHYtMe5Z7-uNMcYfeZfY=)
29. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-UKfnNr52sNxwRpoW7zpAAqrGZxFewKYvITwS1j707DGG0dd9C63n1vkzo__nHVBHw49_96D18jqwscxNhCPzJmJmZ08lcpC-iFY0QarVJv9aydzSeHMd-qDidXXoiw==)
30. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6CCbqHx2sWm3tzSRkfxasUFQJ5yxOsKTOecVLYBHb2I115R_UA1_rZFcBG9C01WQQ-OLWvBY_QkYrnj97-leZHJzMWHJJiCkALORNSwfnFmzAqwMsJ9VWXPfot5TKu2ElrFLPitb0zBjefi1P60_swT-GXrkrdMmGPAJxZuklNfSdBL9AUxUakUGJGQHkww2m9jS5zDIo7uBHbAZGXAnTJVPdniv9gF0UxD4oNLV9kORDy-bUQ7eICIIo_3UFoNeHPofkpfrfBZ_SjJHMOcJD2pczhAVQDE7xx_4ddqxVGOVWjHQ=)
31. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCm7JEdQPAxGxQtU7hByNdpTWBdg-PfsFr0MV8ii13x41Q5jrNMjjzHXvRIl-s08qPOYHdtteiyAd7JEaMXcs-rqG2UMIhBaQA1suVgDD-DS_dnvsagzW4JfJPyNqvnqFiYoHqzyZ_)
32. [cdc.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyUZKGhatWqXbEd6ZB1j31fQ4105JtY07R-xWf2Yib5mD3dbKQmeV1POmw_v6ewt3cmd8wgD3oh5FuC54zAN67-CTHJHH0K7gW5VU251CE64yj3qKQ4cLS5B4VtfRIELh3S_HQaViioM-0m0zhgE-jYnPVt-EG2JJ6z8eVKgnQuLk1TBZOmuPeP9z4lWM4q4Mwi_mRVtAaF88Gj5TR20PHYLtnYSygR2vT)
33. [nipn-nutrition-platforms.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3Md2pEL0vGiSTaPH146JA4RK3d0xSKjTR5rfhlH9s8HDiET-xPU_cXeo4GXXjzfNs5MA3vY0H9F4-Uj5tQ1KGNOTHnY8SZwAno6DCPD8KXhT164E8jIE9ZWUzJK2uacMPiSI3dx7X0I5Ec9edZotGM2GqB2annvrL7ieT2vaRvsrh_D_uDNjKKHHGxQQ=)
34. [europa.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRyd-vDUEiBHygbqUyTP9MzBp4LYGD0JbAD4hQbKSjXnrEuwh29e6287DypTIuX6EsI4cX-enmS_91lwiCgkev1ZOVjY17BNw1v8v_yfu2NCNYJcfdfxUbqqezxUGiNls2RrKrEPPki7YaimhNExVgSzm6ltaz7XAtTWMSiF8y0ZpjMUMR5zi5XJAPrsrEFOhLVJ-0NxJZHzGZireRBxA4)
35. [who.int](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECCswZ8dheJRUNzhSAcTbJKT2y7ScPAGysJRl8II0oZzaGClEyCQFAiEbXSgqM9fWjHPZdMxMxStgrk7VJlm-5TwtBNsuDqitkFVEWch5PKtBWVjXoum6AxOxCJcwqd9OKWas_MuT2blAeJ0VHBjnHnlkXogObKYf4YJjCE6tV)
36. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfnGsQRWY2odq77wab-eGvJR3D_HzW-W-N2ZMsx0wHWbaSVVD6mLom2IibCA-Kj-aQ3Sg_r-41gWwFA_w_I1HoFcvoF48m9_WeIxuQuCth150syDOvablkWh9_GOsgnRtUC736lARIVg==)
37. [wellcomeopenresearch.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMJwJGmM8779klY7m-v0r6HWOf40W4TUaCtbm04B-3iGY19igdQtmmXtRVw3XCrxKegXUwtYZtJREkSJna8M8snO1AE6oLPyMC-fQMxJxQ8vOLHvMsVzocaEi_YW9IksCx9sQe)
38. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeDJ_gPYjoGmqPMEaXyT5fiD1X_1_Xhuoy_q6YyZ0jxvlRa-E2WwaK2V6J6FCOTACon2wJO4r_yvj9YyMnfJlPJaWMMtqBSDqib6NSyl9z3WukoxU_mCNpmJOqvrDZNSk4b3aOWrM9)


## Annotations
Annotation(end_index=4896, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWUX9GxmSHb6TAdrglPeZfW2cQn1OtCFlPxGsO2uNHbUBUQU7PTs-_dYHGAlyeuih3I50lCwOtH-II-G56p48VMsHdgq7QVkbiHcIIWvaAVQlOnNSFVimNH4rlzgUJled0R91yVgZPsG4hQKjvmqHogQlXoxzD4cr-rBJN', start_index=4881)
Annotation(end_index=4896, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpr03fHoHOSIi2qk1XEg1z_7QGiFegi1CRrmwZrdWd5NIjqtlMyOfYU7wDnOCw9OKRXoQAeVTXEirlKtNxgZwe8XljYunLh0PL4mSDyuBgEAVWgw92prf84MCNBQm8ndIfuANdqcukYlj7gOvpS0bybI-trZHJPNCNjIBy4HSU1Ni_Ar7Oa9lypVh_wbCW1CpZ2pSeYvCoELfsdbC09ck5vIimOhlTHhw2onMwBYo0cWTDCfZKskr4kNFugnDrDKenKQhbXXEZNpE=', start_index=4881)
Annotation(end_index=4896, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeFeX2I_acv8nWl2jvyq30h9wLNi9fCJZzkyknIsH9FvKtBH6ch4iJOdhJHKyYPuEd9IIDPgrLGFJnCchjc4IN0y2qjvEx3KlTI8K-4gxhMAHdzPkSnIEMV6fbDiJF6NGsmFNBPQ==', start_index=4881)
Annotation(end_index=5411, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUdgdKGgFJC9PPvve6iKGJNOSHvMyVSgiurgCODE8IOPY-G9hEt8YWMhgzLzD4M2qQe8IrzbUAlzR9CHZOunKeR7_Jsk80dPSxIuW6dRwrqsxRHvWRIvBVQWFJvg_r', start_index=5402)
Annotation(end_index=5871, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfSYiGphZujJWeUNJEy1i0FVt6xRph5YmCM1rx9yDYN7I4xnoIcTrf9CWuV2nN7zUlTJYdOP3bOicj6NYC9zuOIfqs5BJyFfkm-EwttE6NUkT8FNakQPFrThNUDSi6WtY0EF_b75pk_ZvfaJ-AG4CZhdhWc5o9gLuCOw8SWarO_r50sICh3fJHhWLAKjvU6MpZaUc28RYfMMUo-tpIPQrH2FcDi_yeHXA9DAo_30zGMhk9I-uDQld-PKbc57sazWoFHuNFO-_m-xE1LIBovUfWDyjX9VTrJLp4MGfQqwn7CwdOY9NnfgwveQ26uvdDOGdTYJGl8vFyy4yMSRaIJUBokiar1m_cMA==', start_index=5856)
Annotation(end_index=5871, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLbvHyfhy18hyCX491ixXVzsw5vQdm74A8Y9oWrlPGeP3zG74kwrna8ocKXGz2F_s2nZrgpi-bzq-nzFTuHJ0-GkjkHc_iGI2UtNlCgRjC-ehNQhuHHDtO7RUFNbiXcQ==', start_index=5856)
Annotation(end_index=5871, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHy8vDnokn4BdjS6bWYyGWl1jN_AMAeNomoUszeTn-bcOjAyKTFhfCFlCVShvR4LyumAElXKfyE0TnufrkvQYAy506a3fJJP-dUuF4UhNa9em586nDINyanmMvQnpVorTdqXeyi-CdR', start_index=5856)
Annotation(end_index=6347, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4IBXMBF2v0hqoLg5Z3fkarvAJyCn5TXLgUqyxjPEqHjQ1bL16bAIZRdBHI4wkakf645xKxT2_5xqBbPgjhs0owucXEWgc0SEBXtZ_X40pKA2telazL7Qq0OaLrey84b3c35jgpL-FSumRlm0S1nNnpgrdYCPGa6OLXEioRMRqTA7ang70XSjfp3tiVqwM9CG5yN8odRgNMz6IcXsNDRRKjyPTW32GzvN46mwOpVCjDN34BwjEoGwh-B_AuyDPkhrWLou3wdNC0SZSYHCucTEdobYQ0znbUiRin3AMJDvk0Mw-JkCTej6GCDgv7eZ1XTv6fBa_cnCxzwaiGURFaq1lxUrS_251-_2UZw==', start_index=6338)
Annotation(end_index=6640, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAtgCCNwcSpqClXFn_huFnDQPI1ACSFqi_P_-_mmnjXwOlBfyU6xM-qZrd5eDM6mVIYo_e85cUv1Eri8euf39d6GB5ey41eIa8KH2gf9jsDqmvuXJi3rG3qUWwgu8XTwHbJM957u2v', start_index=6631)
Annotation(end_index=7098, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWUX9GxmSHb6TAdrglPeZfW2cQn1OtCFlPxGsO2uNHbUBUQU7PTs-_dYHGAlyeuih3I50lCwOtH-II-G56p48VMsHdgq7QVkbiHcIIWvaAVQlOnNSFVimNH4rlzgUJled0R91yVgZPsG4hQKjvmqHogQlXoxzD4cr-rBJN', start_index=7086)
Annotation(end_index=7098, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeFeX2I_acv8nWl2jvyq30h9wLNi9fCJZzkyknIsH9FvKtBH6ch4iJOdhJHKyYPuEd9IIDPgrLGFJnCchjc4IN0y2qjvEx3KlTI8K-4gxhMAHdzPkSnIEMV6fbDiJF6NGsmFNBPQ==', start_index=7086)
Annotation(end_index=7625, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeFeX2I_acv8nWl2jvyq30h9wLNi9fCJZzkyknIsH9FvKtBH6ch4iJOdhJHKyYPuEd9IIDPgrLGFJnCchjc4IN0y2qjvEx3KlTI8K-4gxhMAHdzPkSnIEMV6fbDiJF6NGsmFNBPQ==', start_index=7616)
Annotation(end_index=8345, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUgJLuNee0nclCbrTCk6hfplz61Bgrn2ZW65sc1njs5y6F3gtAz4mUa7uwGrd9Q9D0XKVQaDUyiTPQqVevTvcgQVOpXaUhb_rWUuOEaABSTKAjwy4u_woYr0TCKPgAhg4G1XbIMGnhcq1QVJL_trrd9_aJXmdS2VUMlt60lH0c_XdZygI8nmrzouZd2w38pe3cVda_ScH1DugbHs6hIAb8J0Lm', start_index=8335)
Annotation(end_index=8836, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUgJLuNee0nclCbrTCk6hfplz61Bgrn2ZW65sc1njs5y6F3gtAz4mUa7uwGrd9Q9D0XKVQaDUyiTPQqVevTvcgQVOpXaUhb_rWUuOEaABSTKAjwy4u_woYr0TCKPgAhg4G1XbIMGnhcq1QVJL_trrd9_aJXmdS2VUMlt60lH0c_XdZygI8nmrzouZd2w38pe3cVda_ScH1DugbHs6hIAb8J0Lm', start_index=8826)
Annotation(end_index=9522, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFf89X_VvoQOi5Xue2oT-xgj6nwkv9Ql3-U2vBC7X0yrslrIOz6aATO95fGDopyv52AKk1M3vUc7nDk-cfG8T8X_Tr51VcHahRHU1HihdOBJpRCgLawssiXh29wuyPu3sMxxB19lTIj', start_index=9508)
Annotation(end_index=9522, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5rC6oFa-e2rhIr-AgTHuG1svu6zoYjq8INKXGr7VKx4ZsoTUnlzUUJ86zm3UeiEi1n7GzEnBYRMooMHWHEQihIablOR_q3b7LeaQ33rS7MVzFKHgpj-eg2cGQ3DdKGt9kYKSFH5OQ-w==', start_index=9508)
Annotation(end_index=9839, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKNMgmOa3gBDJrJ7Q1u-zQsLSJsan4i5WaMZ5zThR5z00hxBwoAfzSQ-hR_GXc5CueT3LxwmdsNtKM9e_oS9aACeUFtwqXdmrrkUCR0bR376dtw1WBbeRhtqRaaXydC41-DHLoEzW-gwmPM4KNrJyfMEmv3Q5ZtLo4QduZbYi1C3I88Q4DeTptePKVHwHhgihx2DU-zOFyZ3nbi0OLhwkyQ9mcuOOQbHv_zSlr', start_index=9825)
Annotation(end_index=9839, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcYba7ZpfuHwSU2FW-N9uomENk5FfAT_aR9u4R4lxZMq53pvpsEGq8nEo2sfsWbt9dBFcrVRi14eWkM9u3YrI-guritkTc1MzJBxN0zJ4LB4T7tvSZ3LQIfAjMEbmpvsJFIuz022EVZiIfEY2w2rAtH9xaU1gsVGNk4gWNeA==', start_index=9825)
Annotation(end_index=11062, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_DO3nPwKaBA_wlbu7xwD4HLIQZPKRguyjQcmFKi4GQk9qDtDOtRlmqJOw95fM71A1FxHU49vSHJXaW0AKDPoAOFrK_6jddfWMrcwnzTKIblyLo0D-bVIvksnXWRC5hQ==', start_index=11048)
Annotation(end_index=11062, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvgbZPoIabZ1gTnJLcyltR1YZpd7Oafk2T92WNFZhgD2S4uWkjK404QXYixvrF4Bd2a1x-fQM6Q6njrTpvYa-6ebIHTpX8ukcWDJs_GiuugWsURFQKT9YJc12vLeOQG56T9oX2ZcPS5dmuS5xJxrkQjVJbFkQjhq0Cp8SrWiTdc2Ka_BvK2adPFjXQJzervPKmdTiw8YU3rkbV7L5L5lNdd14_3Y2TbqK4FN8yH5ySdKiHATZtkQSKx1rfYJuN', start_index=11048)
Annotation(end_index=11279, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_DO3nPwKaBA_wlbu7xwD4HLIQZPKRguyjQcmFKi4GQk9qDtDOtRlmqJOw95fM71A1FxHU49vSHJXaW0AKDPoAOFrK_6jddfWMrcwnzTKIblyLo0D-bVIvksnXWRC5hQ==', start_index=11269)
Annotation(end_index=12454, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpryhPI66AgTnkgn9d3drFB-HBcvxqH_0QiqWLTp8bXRExlLt2aa34zebQIXVxRegXHd7_t0eZcAmt3lmIF8rUQVw-c0UOzswyRLpzzEtdS42RgTXUQ4y0ubJ5iWeMiXLAh5gSSRf2A-2_MMjLjwIAUCObkaWEgka-kTjfgubi5LftNLbJBzhzcl4wjhbdCfoc-dt1vne_EfvX2yTSFOwhJPMjYc4LnW-ZtQ==', start_index=12440)
Annotation(end_index=12454, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQm50G8Vnmry-RV0Bg8EpOGe6f6RhOT5JQ4ClwpJkIocOtXOrnLjk2zOF_o4iBInEH-LlCAhu7KvAvhxjYZtfnSNZBuDV3oquew4Lh7dAStyMguR9C1vrc6Xc5DyWNRsJnMvhNOMSq', start_index=12440)
Annotation(end_index=12941, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5Q3OnvuYHoN4gNucRjAM6PDbHuUrmECTn0-5ZHVmSayBo_fZTHfvO7VCVNIWQFn8ioYhEvncfDMLUBITifGdAsj5IvwEwjT1WV3xHPsXWTpecSKQe8EyfiWSFP40xjvxedbx6QOMLAhBcd4o_n_kx2RgHF78nOr5XL9771lKhTUvDSQlENWf3hRFCA_SgCiV0UtNcylbGMIBPSq0gM_Q70SsRzLwcXo0=', start_index=12931)
Annotation(end_index=13297, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE30_SrNgf3xVhNChzQaQzoC0SImZflZeXYYO65omSeG8YbhYvc9ILzTOkPhAkt2iKrDMiHaBkCCLGHoNc9obcsyMvqLqlD7jdipDeL0EvaJyXsvayyIhySzIUlpJeirWSuZmEG5b5McSf8nVsA3t81N1-_', start_index=13283)
Annotation(end_index=13297, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoiRVBwLF4MFR8TwwEqCxQNAM2MyHFETnM4cqSHiNapathIsn6y3GRrmR34VaNMqPrSKdBxA7DZ0NH1V0bsOleDfO67r81Rqb5dm4_fjkdco5w6IQ4naspcgskxzLNKSgR-0xlnAAZ', start_index=13283)
Annotation(end_index=13828, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHs5sgna-bj4eL9yzhPyc55hcpzp0-KPhkSEkiAyAN1l9yX3exNVg9HaZFdc62YrUwHUpjJ6xDcvsmOGPjJp-vl5jDezRl2R3YK1QkLPr8mlnyigZ7oe3t9Lf3Ul3HRKivvYX8_lLNtWy4diVeATxH9JTm113RUToZMrG4KT2jjVrWKm5xzD7Th-qKKuP1wuEVhAJcKA_lyyVI-oukammStBtB584AxLmejFZ8bVppeil6KQLX9gAV_Oe2s7d6iu82WUN0xJD81lpQ', start_index=13818)
Annotation(end_index=14738, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMATDWA10Hoje7QWv1Q8CNX3NiN25F0zAfms3yDoWENll-5OqJH0F-1prN5fu_CkxVzfaXRrM4i5MJCjP4ocKY8XnVMfi_K3wCG9AxUh7nkfsBZfu7HeC-fV_FJ-q40AB0Xr12aUTWrEm-wgN9YnlFeP8A4yMc-od1PZJnC7or5oyAuLPTVkltY1G3Bmlm0H3oF1AlwHpJcM7Sl3s7l4KWTclh9GXeJjErTFvzEfi-fE2wHIqGgpw=', start_index=14728)
Annotation(end_index=15325, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKNMgmOa3gBDJrJ7Q1u-zQsLSJsan4i5WaMZ5zThR5z00hxBwoAfzSQ-hR_GXc5CueT3LxwmdsNtKM9e_oS9aACeUFtwqXdmrrkUCR0bR376dtw1WBbeRhtqRaaXydC41-DHLoEzW-gwmPM4KNrJyfMEmv3Q5ZtLo4QduZbYi1C3I88Q4DeTptePKVHwHhgihx2DU-zOFyZ3nbi0OLhwkyQ9mcuOOQbHv_zSlr', start_index=15311)
Annotation(end_index=15325, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcYba7ZpfuHwSU2FW-N9uomENk5FfAT_aR9u4R4lxZMq53pvpsEGq8nEo2sfsWbt9dBFcrVRi14eWkM9u3YrI-guritkTc1MzJBxN0zJ4LB4T7tvSZ3LQIfAjMEbmpvsJFIuz022EVZiIfEY2w2rAtH9xaU1gsVGNk4gWNeA==', start_index=15311)
Annotation(end_index=15940, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcb-_adHFaWckRW8b3S4ez1OkNnAi2Fk79Po0GHMuh3vwDmVg2pmYF9p_lODBfO-8wWqlJ_BlTvewb17_4zMonknJUKyiyDX29HOZQqoJptKngYdrIjftrZYKmQbFGz8zYK72AexNn', start_index=15930)
Annotation(end_index=16718, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIGGxPnLG3BPTfGM0K5JsPp5oBw3Z3VSs04TqYzuiayOZRMJ7q4dUNr-bng0byD9aSM83foadyUSWTTb7xvmPWhyxg9RuATF_QY5p8vZQw0S1btMQoP54XSU4883hGx6BSda0Xm85H4A==', start_index=16704)
Annotation(end_index=16718, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHILlV4RiPzCeFAkBCbHJcp_ATHYukq0lMbkZTtxzVlcDMpjz2jylY_0sRcysf9OyFQTqvcWaE9IYS8m-eL6YY0lSXtgJksk6npO7ocAThAJD6I5RXn0lzUt1nZffWJUwC1vlK8hoELCKEWG6yy434TAXHCwKS_zD-2xt6w0y3CGCi9vjdjJSwvCXZaih4WHUZngJHV4NMmh0ijskMGURV3-iqVBubo4_KjbEfAX7o8vTCZbBV5lEYukQ==', start_index=16704)
Annotation(end_index=17124, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0i43XIjQ9X6nKmL4Wfm8u6g_bXfwtFZHhsHMRKq3yLBoky-73_6OwD65-WKPduwybJkxBHR7_I7yNn79NoBajWouriB9K6s8oK71KvmnEJ3FE6dxEwyEWph0JPW0jg27_UuRucZ94F1Ng1A_Dip_UKMBG7QIMHYtMe5Z7-uNMcYfeZfY=', start_index=17110)
Annotation(end_index=17124, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpCyy-a5Qumq-B6ntXfW72ya5KgiLi9eEVJ8RN1isQokuhwhPsWcV5BoVGIKY4C5L_mCnqoAHLVxBxLCg3DAne2guwH7pzYHtwvAN8_ggQCkBb442Lgq_WSGkyARmzO5k-YmIEaIUi', start_index=17110)
Annotation(end_index=18245, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-UKfnNr52sNxwRpoW7zpAAqrGZxFewKYvITwS1j707DGG0dd9C63n1vkzo__nHVBHw49_96D18jqwscxNhCPzJmJmZ08lcpC-iFY0QarVJv9aydzSeHMd-qDidXXoiw==', start_index=18235)
Annotation(end_index=18555, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6CCbqHx2sWm3tzSRkfxasUFQJ5yxOsKTOecVLYBHb2I115R_UA1_rZFcBG9C01WQQ-OLWvBY_QkYrnj97-leZHJzMWHJJiCkALORNSwfnFmzAqwMsJ9VWXPfot5TKu2ElrFLPitb0zBjefi1P60_swT-GXrkrdMmGPAJxZuklNfSdBL9AUxUakUGJGQHkww2m9jS5zDIo7uBHbAZGXAnTJVPdniv9gF0UxD4oNLV9kORDy-bUQ7eICIIo_3UFoNeHPofkpfrfBZ_SjJHMOcJD2pczhAVQDE7xx_4ddqxVGOVWjHQ=', start_index=18545)
Annotation(end_index=19027, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCm7JEdQPAxGxQtU7hByNdpTWBdg-PfsFr0MV8ii13x41Q5jrNMjjzHXvRIl-s08qPOYHdtteiyAd7JEaMXcs-rqG2UMIhBaQA1suVgDD-DS_dnvsagzW4JfJPyNqvnqFiYoHqzyZ_', start_index=19017)
Annotation(end_index=19260, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyUZKGhatWqXbEd6ZB1j31fQ4105JtY07R-xWf2Yib5mD3dbKQmeV1POmw_v6ewt3cmd8wgD3oh5FuC54zAN67-CTHJHH0K7gW5VU251CE64yj3qKQ4cLS5B4VtfRIELh3S_HQaViioM-0m0zhgE-jYnPVt-EG2JJ6z8eVKgnQuLk1TBZOmuPeP9z4lWM4q4Mwi_mRVtAaF88Gj5TR20PHYLtnYSygR2vT', start_index=19250)
Annotation(end_index=19796, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECCswZ8dheJRUNzhSAcTbJKT2y7ScPAGysJRl8II0oZzaGClEyCQFAiEbXSgqM9fWjHPZdMxMxStgrk7VJlm-5TwtBNsuDqitkFVEWch5PKtBWVjXoum6AxOxCJcwqd9OKWas_MuT2blAeJ0VHBjnHnlkXogObKYf4YJjCE6tV', start_index=19778)
Annotation(end_index=19796, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3Md2pEL0vGiSTaPH146JA4RK3d0xSKjTR5rfhlH9s8HDiET-xPU_cXeo4GXXjzfNs5MA3vY0H9F4-Uj5tQ1KGNOTHnY8SZwAno6DCPD8KXhT164E8jIE9ZWUzJK2uacMPiSI3dx7X0I5Ec9edZotGM2GqB2annvrL7ieT2vaRvsrh_D_uDNjKKHHGxQQ=', start_index=19778)
Annotation(end_index=19796, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRyd-vDUEiBHygbqUyTP9MzBp4LYGD0JbAD4hQbKSjXnrEuwh29e6287DypTIuX6EsI4cX-enmS_91lwiCgkev1ZOVjY17BNw1v8v_yfu2NCNYJcfdfxUbqqezxUGiNls2RrKrEPPki7YaimhNExVgSzm6ltaz7XAtTWMSiF8y0ZpjMUMR5zi5XJAPrsrEFOhLVJ-0NxJZHzGZireRBxA4', start_index=19778)
Annotation(end_index=21434, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfnGsQRWY2odq77wab-eGvJR3D_HzW-W-N2ZMsx0wHWbaSVVD6mLom2IibCA-Kj-aQ3Sg_r-41gWwFA_w_I1HoFcvoF48m9_WeIxuQuCth150syDOvablkWh9_GOsgnRtUC736lARIVg==', start_index=21424)
Annotation(end_index=21511, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeFeX2I_acv8nWl2jvyq30h9wLNi9fCJZzkyknIsH9FvKtBH6ch4iJOdhJHKyYPuEd9IIDPgrLGFJnCchjc4IN0y2qjvEx3KlTI8K-4gxhMAHdzPkSnIEMV6fbDiJF6NGsmFNBPQ==', start_index=21502)
Annotation(end_index=21577, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWUX9GxmSHb6TAdrglPeZfW2cQn1OtCFlPxGsO2uNHbUBUQU7PTs-_dYHGAlyeuih3I50lCwOtH-II-G56p48VMsHdgq7QVkbiHcIIWvaAVQlOnNSFVimNH4rlzgUJled0R91yVgZPsG4hQKjvmqHogQlXoxzD4cr-rBJN', start_index=21568)
Annotation(end_index=21645, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3Md2pEL0vGiSTaPH146JA4RK3d0xSKjTR5rfhlH9s8HDiET-xPU_cXeo4GXXjzfNs5MA3vY0H9F4-Uj5tQ1KGNOTHnY8SZwAno6DCPD8KXhT164E8jIE9ZWUzJK2uacMPiSI3dx7X0I5Ec9edZotGM2GqB2annvrL7ieT2vaRvsrh_D_uDNjKKHHGxQQ=', start_index=21635)
Annotation(end_index=21723, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHy8vDnokn4BdjS6bWYyGWl1jN_AMAeNomoUszeTn-bcOjAyKTFhfCFlCVShvR4LyumAElXKfyE0TnufrkvQYAy506a3fJJP-dUuF4UhNa9em586nDINyanmMvQnpVorTdqXeyi-CdR', start_index=21714)
Annotation(end_index=21799, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUgJLuNee0nclCbrTCk6hfplz61Bgrn2ZW65sc1njs5y6F3gtAz4mUa7uwGrd9Q9D0XKVQaDUyiTPQqVevTvcgQVOpXaUhb_rWUuOEaABSTKAjwy4u_woYr0TCKPgAhg4G1XbIMGnhcq1QVJL_trrd9_aJXmdS2VUMlt60lH0c_XdZygI8nmrzouZd2w38pe3cVda_ScH1DugbHs6hIAb8J0Lm', start_index=21789)
Annotation(end_index=21868, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKNMgmOa3gBDJrJ7Q1u-zQsLSJsan4i5WaMZ5zThR5z00hxBwoAfzSQ-hR_GXc5CueT3LxwmdsNtKM9e_oS9aACeUFtwqXdmrrkUCR0bR376dtw1WBbeRhtqRaaXydC41-DHLoEzW-gwmPM4KNrJyfMEmv3Q5ZtLo4QduZbYi1C3I88Q4DeTptePKVHwHhgihx2DU-zOFyZ3nbi0OLhwkyQ9mcuOOQbHv_zSlr', start_index=21858)
Annotation(end_index=21942, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMJwJGmM8779klY7m-v0r6HWOf40W4TUaCtbm04B-3iGY19igdQtmmXtRVw3XCrxKegXUwtYZtJREkSJna8M8snO1AE6oLPyMC-fQMxJxQ8vOLHvMsVzocaEi_YW9IksCx9sQe', start_index=21932)
Annotation(end_index=22004, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcb-_adHFaWckRW8b3S4ez1OkNnAi2Fk79Po0GHMuh3vwDmVg2pmYF9p_lODBfO-8wWqlJ_BlTvewb17_4zMonknJUKyiyDX29HOZQqoJptKngYdrIjftrZYKmQbFGz8zYK72AexNn', start_index=21994)
Annotation(end_index=22074, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeDJ_gPYjoGmqPMEaXyT5fiD1X_1_Xhuoy_q6YyZ0jxvlRa-E2WwaK2V6J6FCOTACon2wJO4r_yvj9YyMnfJlPJaWMMtqBSDqib6NSyl9z3WukoxU_mCNpmJOqvrDZNSk4b3aOWrM9', start_index=22064)
Annotation(end_index=22160, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_DO3nPwKaBA_wlbu7xwD4HLIQZPKRguyjQcmFKi4GQk9qDtDOtRlmqJOw95fM71A1FxHU49vSHJXaW0AKDPoAOFrK_6jddfWMrcwnzTKIblyLo0D-bVIvksnXWRC5hQ==', start_index=22150)
Annotation(end_index=22233, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-UKfnNr52sNxwRpoW7zpAAqrGZxFewKYvITwS1j707DGG0dd9C63n1vkzo__nHVBHw49_96D18jqwscxNhCPzJmJmZ08lcpC-iFY0QarVJv9aydzSeHMd-qDidXXoiw==', start_index=22223)
Annotation(end_index=22314, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpCyy-a5Qumq-B6ntXfW72ya5KgiLi9eEVJ8RN1isQokuhwhPsWcV5BoVGIKY4C5L_mCnqoAHLVxBxLCg3DAne2guwH7pzYHtwvAN8_ggQCkBb442Lgq_WSGkyARmzO5k-YmIEaIUi', start_index=22304)
Annotation(end_index=22387, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5rC6oFa-e2rhIr-AgTHuG1svu6zoYjq8INKXGr7VKx4ZsoTUnlzUUJ86zm3UeiEi1n7GzEnBYRMooMHWHEQihIablOR_q3b7LeaQ33rS7MVzFKHgpj-eg2cGQ3DdKGt9kYKSFH5OQ-w==', start_index=22377)
Annotation(end_index=22442, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHs5sgna-bj4eL9yzhPyc55hcpzp0-KPhkSEkiAyAN1l9yX3exNVg9HaZFdc62YrUwHUpjJ6xDcvsmOGPjJp-vl5jDezRl2R3YK1QkLPr8mlnyigZ7oe3t9Lf3Ul3HRKivvYX8_lLNtWy4diVeATxH9JTm113RUToZMrG4KT2jjVrWKm5xzD7Th-qKKuP1wuEVhAJcKA_lyyVI-oukammStBtB584AxLmejFZ8bVppeil6KQLX9gAV_Oe2s7d6iu82WUN0xJD81lpQ', start_index=22432)
Annotation(end_index=22510, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpr03fHoHOSIi2qk1XEg1z_7QGiFegi1CRrmwZrdWd5NIjqtlMyOfYU7wDnOCw9OKRXoQAeVTXEirlKtNxgZwe8XljYunLh0PL4mSDyuBgEAVWgw92prf84MCNBQm8ndIfuANdqcukYlj7gOvpS0bybI-trZHJPNCNjIBy4HSU1Ni_Ar7Oa9lypVh_wbCW1CpZ2pSeYvCoELfsdbC09ck5vIimOhlTHhw2onMwBYo0cWTDCfZKskr4kNFugnDrDKenKQhbXXEZNpE=', start_index=22501)
Annotation(end_index=22580, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvgbZPoIabZ1gTnJLcyltR1YZpd7Oafk2T92WNFZhgD2S4uWkjK404QXYixvrF4Bd2a1x-fQM6Q6njrTpvYa-6ebIHTpX8ukcWDJs_GiuugWsURFQKT9YJc12vLeOQG56T9oX2ZcPS5dmuS5xJxrkQjVJbFkQjhq0Cp8SrWiTdc2Ka_BvK2adPFjXQJzervPKmdTiw8YU3rkbV7L5L5lNdd14_3Y2TbqK4FN8yH5ySdKiHATZtkQSKx1rfYJuN', start_index=22570)
Annotation(end_index=22652, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUdgdKGgFJC9PPvve6iKGJNOSHvMyVSgiurgCODE8IOPY-G9hEt8YWMhgzLzD4M2qQe8IrzbUAlzR9CHZOunKeR7_Jsk80dPSxIuW6dRwrqsxRHvWRIvBVQWFJvg_r', start_index=22643)
Annotation(end_index=22720, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6CCbqHx2sWm3tzSRkfxasUFQJ5yxOsKTOecVLYBHb2I115R_UA1_rZFcBG9C01WQQ-OLWvBY_QkYrnj97-leZHJzMWHJJiCkALORNSwfnFmzAqwMsJ9VWXPfot5TKu2ElrFLPitb0zBjefi1P60_swT-GXrkrdMmGPAJxZuklNfSdBL9AUxUakUGJGQHkww2m9jS5zDIo7uBHbAZGXAnTJVPdniv9gF0UxD4oNLV9kORDy-bUQ7eICIIo_3UFoNeHPofkpfrfBZ_SjJHMOcJD2pczhAVQDE7xx_4ddqxVGOVWjHQ=', start_index=22710)
Annotation(end_index=22788, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMATDWA10Hoje7QWv1Q8CNX3NiN25F0zAfms3yDoWENll-5OqJH0F-1prN5fu_CkxVzfaXRrM4i5MJCjP4ocKY8XnVMfi_K3wCG9AxUh7nkfsBZfu7HeC-fV_FJ-q40AB0Xr12aUTWrEm-wgN9YnlFeP8A4yMc-od1PZJnC7or5oyAuLPTVkltY1G3Bmlm0H3oF1AlwHpJcM7Sl3s7l4KWTclh9GXeJjErTFvzEfi-fE2wHIqGgpw=', start_index=22778)

## Sources
