# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** d73da41e | **Time:** 345.91s | **Cost:** $1.39164
--------------------------------------------------------------------------------

# The Fractal Constraint: How Self-Similar Patterns in Peak Travel Distribution Limit Demand Forecasting Precision

### Key Points
*   **Fundamental Incompatibility with Standard Models:** Self-similar traffic patterns, characterized by Long-Range Dependence (LRD) and heavy-tailed distributions, fundamentally violate the assumptions of memorylessness and finite variance inherent in traditional Poisson and Markovian forecasting models.
*   **The "Joseph Effect" and "Noah Effect":** The precision of forecasting is constrained by two fractal phenomena: the Joseph Effect (persistence of trends) and the Noah Effect (infinite variance/extreme volatility). These ensure that "bursts" of demand occur across all time scales, preventing the smoothing of peaks through aggregation.
*   **Theoretical Limits of Precision:** Research indicates a theoretical upper bound to predictability in self-similar systems. While the structure of traffic is highly correlated (predictable), the magnitude of peaks follows power-law distributions that make point-accuracy impossible, necessitating probabilistic or interval-based forecasting.
*   **Computational Trade-offs:** Capturing self-similarity requires modeling "infinite history," which is computationally intractable. Approximations (like truncated LRD or deep learning attention mechanisms) introduce inevitable precision errors, creating a trade-off between computational feasibility and fractal fidelity.
*   **The Predictability Paradox:** As forecasting models become more complex to account for fractal resilience, they often become less interpretable and more sensitive to initial conditions, leading to a paradox where increased model sophistication does not linearly translate to reduced forecast error during extreme peak events.

---

## 1. Introduction: The Fractal Nature of Travel Demand

The precision of demand forecasting in transportation and network traffic is fundamentally constrained by the statistical nature of the demand itself. Traditional forecasting methodologies have historically relied on the Central Limit Theorem and assumptions of stationarity, presuming that as data is aggregated over time, traffic patterns smooth out and variance stabilizes. However, a convergence of research across physical transportation, digital networks, and supply chain logistics demonstrates that peak travel distributions exhibit **self-similarity**—a fractal property where traffic burstiness is preserved across time scales [cite: 1, 2, 3].

This report analyzes how self-similar patterns impose hard constraints on the precision of demand forecasting. Unlike short-memory processes (e.g., Poisson arrivals), where the past rapidly becomes irrelevant, self-similar processes display Long-Range Dependence (LRD). This implies that traffic spikes are not isolated outliers but part of a structured, persistent pattern of volatility that defies standard smoothing techniques [cite: 4, 5, 6]. Consequently, the "precision" of a forecast cannot be defined simply by minimizing mean squared error, as the variance in these systems may be theoretically infinite [cite: 3, 7].

We explore these constraints through the lenses of statistical theory (the Hurst exponent and heavy tails), computational limits (the inability to process infinite history), and the "Predictability Paradox," where the very nature of bursty traffic renders high-precision point forecasting mathematically impossible for peak events [cite: 8, 9].

---

## 2. Theoretical Foundations of Self-Similarity and LRD

To understand the constraints on forecasting precision, one must first define the statistical environment of peak travel. The literature consistently identifies two primary components of self-similar traffic that disrupt conventional modeling: the **Joseph Effect** and the **Noah Effect**.

### 2.1 The Joseph Effect: Long-Range Dependence (LRD)
The Joseph Effect, named by Mandelbrot after the biblical seven years of plenty and seven years of famine, refers to the tendency of persistent trends to exist in time series data [cite: 10, 11, 12]. In the context of travel demand, this means that periods of high traffic are likely to be followed by further high traffic, and this correlation decays so slowly that it is mathematically considered non-summable.

*   **Statistical Definition:** A process is considered to have LRD if its autocorrelation function decays according to a power law, rather than exponentially. This implies that the current state of traffic is influenced by events that occurred significantly far in the past [cite: 4, 5].
*   **Implication for Precision:** Traditional models like ARIMA (Autoregressive Integrated Moving Average) assume that correlations drop off quickly (Short-Range Dependence). When applied to LRD traffic, these models underestimate the duration and intensity of peak periods because they fail to account for the "memory" of the system. The precision of the forecast degrades as the prediction horizon extends because the model assumes the system will revert to the mean faster than it actually does [cite: 5, 13].

### 2.2 The Noah Effect: Infinite Variance and Heavy Tails
The Noah Effect refers to the high variability and the presence of extreme values (disasters or deluges) that exceed what is predicted by a normal (Gaussian) distribution [cite: 6, 10, 14].

*   **Heavy-Tailed Distributions:** Peak travel demand often follows heavy-tailed distributions (e.g., Pareto, Log-Normal, or Burr distributions) rather than Gaussian distributions. In these distributions, the probability of extreme events (massive traffic jams, sudden surges in network packets) decays slowly [cite: 15, 16, 17].
*   **Constraint on Precision:** In a heavy-tailed distribution, the second moment (variance) can be infinite. Standard forecasting metrics like Root Mean Square Error (RMSE) rely on the existence of a finite variance to be meaningful. When variance is infinite or extremely large, the "precision" of a point forecast becomes volatile and unreliable. A model might have low average error but fail catastrophically during the peaks that matter most [cite: 3, 7].

### 2.3 The Hurst Exponent as a Measure of Constraint
The degree of self-similarity is quantified by the Hurst exponent ($H$).
*   **$0.5 < H < 1$:** Indicates a persistent, self-similar process. The closer $H$ is to 1, the stronger the LRD and the "burstier" the traffic [cite: 5, 12, 18, 19].
*   **$H = 0.5$:** Indicates a random walk (Brownian motion) with no memory.
*   **Constraint:** Research indicates that real-world traffic traces often exhibit $H$ values between 0.7 and 0.9 [cite: 5, 12]. This high degree of self-similarity implies that "bursts" exist at every time scale—from milliseconds to hours. There is no "smoothing scale" where the traffic becomes uniform. Therefore, forecasting precision is constrained because there is no stable "average" state to converge upon during peak periods [cite: 6, 20, 21].

---

## 3. Constraints Imposed by Distributional Characteristics

The distributional shape of peak travel demand creates specific barriers to accuracy. The assumption of normality is the "original sin" of many legacy forecasting systems, leading to systematic underestimation of risk and resource requirements.

### 3.1 The Failure of Poisson and Gaussian Models
Traditional traffic engineering (e.g., Erlang formulas in telecommunications or standard capacity planning in highways) often assumes Poisson arrival processes. Poisson processes are "memoryless" and their variance equals their mean.
*   **The Burstiness Gap:** Self-similar traffic is "bursty" at all scales. A Poisson model might predict a peak demand of $X$, but the actual fractal nature of the traffic allows for peaks of $10X$ or $100X$ with non-negligible probability [cite: 3, 20].
*   **Forecasting Error:** Studies show that Poisson models seriously underestimate the burstiness of traffic. When demand is modeled as Poisson, the forecast assumes that peaks will smooth out over longer intervals. In reality, self-similar traffic maintains its burstiness even when aggregated, leading to significant forecasting errors and resource under-provisioning [cite: 3, 20].

### 3.2 Heavy-Tailed Constraints in Physical and Digital Systems
The constraint of heavy tails is observed across diverse domains, reinforcing its universality.
*   **Airport Ground Support:** Research into airport ground support equipment (e.g., potable water trucks) demonstrates that service durations follow heavy-tailed distributions (specifically Stable or Burr distributions) rather than normal distributions. Using heavy-tailed models reduced estimation errors by 13% to 25% compared to conventional methods [cite: 15, 22, 23]. This explicitly quantifies the "precision penalty" of ignoring self-similarity: a quarter of the forecast accuracy is lost by assuming normality.
*   **Network Traffic:** In LEO satellite networks and industrial IoT, traffic exhibits high nonlinearity and burstiness. Linear models fail to capture these multi-scale characteristics, leading to error increases of 40–60% during burst scenarios [cite: 24]. The "infinite variance syndrome" means that standard confidence intervals are too narrow, giving a false sense of precision [cite: 3].

### 3.3 The Aggregation Fallacy
A common technique to improve forecasting precision is aggregation (e.g., forecasting daily totals instead of hourly peaks).
*   **Fractal Resistance:** Self-similarity implies scale invariance. Unlike white noise, which smooths out as you aggregate it, self-similar traffic retains its variability across scales [cite: 6, 21].
*   **Constraint:** This means that "zooming out" does not necessarily yield a more precise deterministic forecast for peak capacity planning. The "Joseph Effect" ensures that high-demand days cluster together, preventing the law of large numbers from stabilizing the forecast as quickly as expected [cite: 6, 10].

---

## 4. Computational and Algorithmic Constraints

Even if the theoretical distributions are understood, the practical implementation of forecasting models for self-similar traffic faces severe computational constraints. Precision is often sacrificed for computational feasibility.

### 4.1 The "Infinite History" Problem
To perfectly forecast a process with Long-Range Dependence, a model theoretically requires the entire history of the time series, as the autocorrelation function decays non-negligibly over infinite time.
*   **Practical Limitation:** Infinite history is impossible to store or process in real-time systems. Forecasting models must truncate the history (finite memory).
*   **Precision Trade-off:** Truncating the history eliminates the oldest correlations, which, in an LRD process, still contain relevant information about the current state. This truncation introduces an unavoidable error floor. Research suggests that while simple Minimum Mean Square Error (MMSE) predictors can achieve accuracy within 5% of complex fractional predictors, they still cannot capture the full fractal dynamic [cite: 5].

### 4.2 Complexity of Long-Memory Models
Models designed to handle LRD, such as Fractional ARIMA (FARIMA) or Fractional Brownian Motion (fBm) models, are computationally expensive.
*   **Computational Cost:** Fitting parameters for self-similar models (like the Hurst exponent) is time-consuming and difficult to perform online [cite: 4, 5].
*   **Resource Constraints:** In resource-constrained environments like Industrial IoT gateways or onboard satellite processors, the $O(n^2)$ complexity of advanced models (like Transformers with full self-attention) is prohibitive. This forces the use of lightweight approximations (e.g., linear models or sparse attention), which inherently limit the precision of capturing complex, non-linear self-similar patterns [cite: 24].

### 4.3 Deep Learning and Attention Mechanisms
Recent advancements use Deep Learning, specifically Transformers and LSTMs (Long Short-Term Memory networks), to address LRD.
*   **Attention as a Solution:** Attention mechanisms allow models to focus on distant past events, theoretically mimicking LRD capture [cite: 25, 26].
*   **The Constraint:** While these models outperform traditional statistics, they still struggle with the "Predictability Paradox." As models become complex enough to capture fractal patterns, they become "black boxes," making it difficult to distinguish between a genuine structural forecast and overfitting to noise. Furthermore, standard loss functions (like MSE) may not align with the heavy-tailed nature of the data, penalizing the model for missing a peak that was statistically probable but temporally unpredictable [cite: 8, 9].

---

## 5. The Predictability Paradox and Uncertainty

A critical finding in the literature is that self-similar traffic possesses a duality: it is structurally predictable (due to correlations) but magnitude-unpredictable (due to heavy tails).

### 5.1 High Predictability vs. Low Precision
Research using entropy analysis on traffic flows indicates a high theoretical predictability (up to 83-93%) of user mobility patterns [cite: 27, 28].
*   **The Paradox:** While we can predict *that* a user will move or *that* traffic will be heavy (high predictability of state), the exact magnitude of the peak (the "Noah Effect") remains elusive. The heavy tail means the peak could be 100 units or 10,000 units with similar probabilities.
*   **Constraint:** This creates a ceiling on *precision* (exact value prediction) even if *accuracy* (trend prediction) is high. The forecast might correctly identify a peak period but fail to predict the catastrophic extent of the demand [cite: 28].

### 5.2 The Predictability-Resilience Paradox
In algorithmic environments, a paradox emerges: to make systems resilient to the burstiness of self-similar traffic, algorithms must be dynamic and adaptive. However, this adaptivity makes the system's output less predictable [cite: 8].
*   **Feedback Loops:** In traffic assignment and routing, user responses to forecasts (e.g., avoiding a predicted jam) alter the demand pattern. In a self-similar system, these perturbations can cascade (Butterfly Effect), rendering the initial high-precision forecast obsolete the moment it is acted upon [cite: 29].

---

## 6. Methodological Responses and Their Limits

Given these constraints, researchers have developed specific methodologies to mitigate the loss of precision, though none can fully eliminate the fractal uncertainty.

### 6.1 Fractal-Fuzzy and Hybrid Approaches
To handle the non-linearity and ambiguity of peak demand, hybrid models combining fractal theory with fuzzy logic have been proposed.
*   **Performance:** These models select features based on fractal dimensions to improve processing speed and accuracy, showing promise in electricity and travel demand [cite: 1].
*   **Limit:** They rely on the assumption that the fractal dimension remains stable, which may not hold during regime shifts (e.g., post-pandemic travel patterns) [cite: 30, 31].

### 6.2 Probabilistic and Interval Forecasting
Acknowledging that point forecasting is constrained by infinite variance, the field is moving toward probabilistic forecasting.
*   **Shift in Precision Definition:** Instead of predicting "500 cars," models predict a probability distribution (e.g., "95% chance of 400-800 cars"). This accounts for the heavy tail by widening the confidence interval [cite: 32, 33, 34].
*   **Conformal Prediction:** Techniques like conformal prediction provide rigorous error bounds that are valid regardless of the underlying distribution, offering a way to quantify the lack of precision inherent in self-similar systems [cite: 34].

### 6.3 Decomposition and Multi-Scale Modeling
Recognizing that self-similarity manifests differently at different scales, decomposition methods (e.g., Wavelet transforms, Empirical Mode Decomposition) are used.
*   **Mechanism:** These separate the signal into high-frequency (bursty) and low-frequency (trend) components. The trend is forecasted with standard models, while the bursty component requires specialized heavy-tailed models [cite: 7, 24, 31, 35].
*   **Constraint:** Reassembling these components introduces phase errors, and the "bursty" component remains inherently difficult to predict with high precision due to its stochastic nature [cite: 35].

---

## 7. Conclusion

Self-similar patterns in peak travel distribution constrain demand forecasting precision by invalidating the statistical laws that underpin traditional forecasting. The **Joseph Effect** ensures that errors accumulate rather than cancel out over time, while the **Noah Effect** introduces extreme values that defy minimization by standard error metrics.

The precision of demand forecasting in this context is not merely limited by data quality or algorithm power, but by the **mathematical properties of the traffic itself**. When variance is infinite and dependence is long-range, "exact" forecasting is a theoretical impossibility. The constraints manifest as:
1.  **Statistical Constraints:** Inability to use Gaussian-based confidence intervals or standard error minimization.
2.  **Computational Constraints:** Inability to process the "infinite history" required to fully resolve LRD.
3.  **Epistemological Constraints:** The Predictability Paradox, where the structure of the traffic allows prediction of trends but the heavy tails prevent precision regarding magnitudes.

Future advancements lie not in trying to force self-similar traffic into linear models, but in adopting **fractal-aware** architectures (like Fractal-Fuzzy systems or LRD-aware Transformers) and shifting the goal from precise point forecasting to robust **probabilistic risk assessment** that explicitly models the heavy tails of demand.

---

## 8. Detailed Analysis of Research Findings

### 8.1 The Impact of Self-Similarity on Forecasting Error
Research explicitly links the Hurst exponent to forecasting error. High Hurst values (indicating strong self-similarity) correlate with higher forecasting errors in traditional models because these models anticipate a "return to mean" that does not occur.
*   **Study Evidence:** In tourism demand, using the Hurst exponent to select predictive keywords improved forecasting ability, suggesting that acknowledging the fractal nature of the data is a prerequisite for precision [cite: 36].
*   **Network Traffic:** In satellite networks, self-similarity analysis combined with LSTM models significantly reduced Root Mean Squared Error (RMSE) compared to models that ignored the fractal property, yet the error remained non-negligible due to the inherent volatility [cite: 19].

### 8.2 The Role of "Event Shocks" and Non-Stationarity
Self-similar processes are often non-stationary (or stationary only in a specific fractal sense). External shocks (e.g., pandemics, policy changes) can alter the fractal dimension or the scaling parameters.
*   **Constraint:** Models trained on one regime of self-similarity may fail catastrophically if the Hurst exponent shifts. For example, COVID-19 introduced "event shocks" that distorted passenger volume forecasts, requiring models that can adapt to abrupt structural changes rather than relying solely on historical fractal patterns [cite: 30].
*   **Post-Pandemic Tails:** Research on Airbnb bookings showed that post-pandemic stay lengths became *more* heavy-tailed. Models anchored to 2019 assumptions (lighter tails) systematically under-predicted demand for long stays, highlighting how evolving fractal properties constrain precision [cite: 17].

### 8.3 Average vs. Peak Constraints
A recurring theme is the discrepancy between average and peak behavior in self-similar systems.
*   **Resource Provisioning:** In network dimensioning, reserving bandwidth based on average traffic leads to degradation during peaks (due to bursts), while reserving based on peaks leads to waste. This "Average vs. Peak" dilemma is a direct result of self-similarity, where the ratio between peak and average does not converge to a stable constant as it would in Poisson traffic [cite: 20, 37, 38].
*   **Implication:** Forecasting precision is constrained because a model optimized for the "average" (which is statistically easier) will inherently fail to capture the "peak" (which is fractally bursty).

### 8.4 Domain-Specific Nuances
*   **Urban Traffic:** The predictability of urban traffic is bounded. While entropy measures suggest high potential predictability, the actual realization of this is limited by the complexity of driver behavior and the non-linear interactions of congestion, which exhibit self-organized criticality [cite: 28].
*   **Industrial IoT:** The trade-off between model complexity and deployability is stark. High-precision fractal models (like Transformers) are too heavy for edge gateways, forcing the use of lighter, less precise models that struggle with multi-scale burstiness [cite: 24].

### 8.5 Summary of Constraints
| Constraint Type | Source Mechanism | Impact on Precision |
| :--- | :--- | :--- |
| **Statistical** | Heavy Tails (Noah Effect) | Infinite variance makes point forecasts unreliable; standard error metrics fail. |
| **Temporal** | Long-Range Dependence (Joseph Effect) | History never fully "decays"; truncation of data leads to information loss. |
| **Computational** | Fractal Complexity | Accurate models ($O(n^2)$) are too slow for real-time; fast models are too simple. |
| **Structural** | Scale Invariance | Aggregation does not smooth the data; bursts persist at all time scales. |

This comprehensive analysis confirms that self-similar patterns impose a hard ceiling on the precision of demand forecasting, necessitating a paradigm shift from deterministic precision to probabilistic risk management.

**Sources:**
1. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEikn5f59uil7G-hqfQRbkmWrVdzuZIYs_5Fq5aUQZZgfTW34ndKFGQZ5gj_dITMn8yNsvin3q56aqEvHVJRkf-fdBFCyUEkgatuJSp9HFRj_dIONoME1RtrTkliWLI5pqv6CK5jZr8c-I8te9jhrvxy4Ymh6CBsLmvLx-TXlebjO_cqdbHp8g-IyhOGa7NSD7sV68EG1uteDvI3uQ9aWBxoApTQlzV9Co085RlGLK7IW-37g==)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFd6lONZKt26AhVIuyg3rkwyIQVAMRvJyQASiwk1Y6a2_q2tOUMbimBh-61iOF5db2aEr5R5HJn-4_dVGvbwYrkixQKANj7hf5TQkosmx9b51MNB9Tb5eU7xYvhKJbXVm5t0FMK11BZlwZGkFTiVUpybRzpkQ_yNRRwIBdtb6jX9H7GZZeK6acrePcD3J4CEBMxMYwhsW7QPWbS-UnB_l5zP5aQNmy7qk7OZjkMF_Eqfg35XL2pPzr9NOQr6w==)
3. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGG1i7KLgWKMzXzGOQ2WKkctn_p6KxYpi6J72T_hhIj_vgfoLGvrIlXAk6MyTjj4PQ2fT61SMRhVUXKeJOZ_hVEgpg1dbiQh2nC_FUA0y5L51sGL-ic3IrM5sozM6YsmCXZBeJbZEufwgmhlcohSzfaYwLaxLLpGdEHWKyNxTOncwvuw5zHhMqfkyriPE56JSHSAg7sykmdRPBfhBhF)
4. [scholaris.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2mZwBFRJkraPP3_hgpQs8D6cAmWtsEGGXfEHHtM_sfYDSKogVwj5Li-mPUWhTxGFsACmeYPiGYs73XSschgO7WAABgsrmTpSOj-seM-G7FkQhwfvjZsFp5fPV7MWP6qkxTqxZTQSgMLZ1jW81zUGcStdS-P-ILaGeCAR5tQufch84G2GKGJizMRB7GA==)
5. [uwaterloo.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBumi1ZUDGtTspXYqXucXcjpiEdbgJ6YVEcUANRPVkeA55bajFOiRcYzhr_s26th4yuu-SE57jnkdGPfMNC_UCgemWaV-Hq-iJd2Yw2m4b9IkNGaDTHfWvK8KE8Kl7GaW_zCkNKWnw1VsA6J-wrix0bVQ7)
6. [northwestern.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFT4NjJIJCAdZKyPzL9XB6I7ZMy5G852MAYT5xothbme4AztlgrE9hOpWvvDDToP0Sdg9pOc3I25zt7yEhLVQpZpGZZDfbpgC_cVrZMssOJgIXbt2KFWedpa5Ad_9enl7HGkm2QX-T0HqeLWpUf210LdS_93W52pHrXCu8MKk8wcVmNLmU=)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG22AB7VXefbSW4jX0p7iyCOMrpc2P9m7HhZ1CJYmyVQxy-hcGgHnVEdQmT-kXUvwb5oMhtzQa3zRiCFQyXIQ2bydxxOCIrbTd7KjpGdygP_NEelNpL_Ogi0MbBCPPyk1JCz-FxTQxnLgtYMQ-QAme_2yv5pNr1CQA_E5G_5cbsphR8_YaGwh9rXsqkOix7njJ0479C5GLMOgQEUZnYOzfJ)
8. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0AuRS48Wyceo_cRyrr1tqXIhQsxtSbc4E4eBdUEiKmXH2OQ6jm1RFAAItPCCT-4-EuXZOEadSY8B0HzKPQZ76EmhlQx5g-zgc5owN97Kg_-BhYFG4tQdR3uHCtcOL86ympIUlsnitgAvqE19UvdqBhKok526DXYiCHrvbDI7LviMjaK52AnUTIAidC20oT6lppPVFmlFlnlu9)
9. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPDW9zrlrxGZgi6twWi988iGoQwqhLku-4jwkWdtMh9NgWQxwebSi4bl0l6QR7Ry5V9bH08aPhH5Se8895Z9FpT4uM-KbV1Iz_gJNw843YlA6LdY_BWgiyJQ==)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEneLZPSqTeFjM3loL6YRTCWE5mvk5owvCjdZI6y30urkw_O4Gi96SyFrt3px8SsATFW-obCmBIUm6lS5QaJnEtjO6cCx7T9Wlc9WP0WIrognwWNWGuaR2cQike4FAdWg9jaWsgdF_S7HFH0GGTYQ2OgWMSQQsI1no9AhQuQYhK6s48dok_NEi-40AxHlu0aBjkPq1aNcvyOvT8nrFD_QfjheYuCIQ=)
11. [nkorolko.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQQaZjEQlc-uTKB3DqZtpOg1f32DLZmF8_H7_vV8t4-ypreYtF6QTxtM4zrq1KLVunCBefVe-MyV5Yj8JCq7nvkMgw3fMdWQhTQff2ReuTk783ULQhsQt3Z2dWx5dZJg==)
12. [huji.ac.il](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKrJKUHR_WDur_cUJra2oCfPDsLzjlzmtLjEh5m85tUGn63RNPKpmJdlC6sYItG8fuA4EREwbqrWdQkkzGm3bZd0GrrR_Q1r1PfwspXgsCukIj0gJwX0sOXEbJPwGXm3jw6SWIMjFdc9fLj7yCq5w=)
13. [scholaris.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxIUJPkWL8TJ5r6N8hrcOlPJYhkNYF4sFUtGLUy6QPzIm0rD1kGnQCLikgB-nDBQb7xbD8KiP_xXblyliCmAxFSQjYOva2IucWHTcJ-jZlIFgibtgmMDp4E3M_4kSrc48sxNxr9EKBWREQUzPvPZ0Mv4uMNqSuSiiwJ5JEMXu4d3R1BYy4diD-LB58TyA82XMgNk84B0lZkcJkJQ==)
14. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEljgPjn2qnmMrhrsTuV8-uoqY-74JxFpRIAievagJPhayPyBp8ZqvE3xLzIH7dXmCVTLXlILxuYDy13mk6Hza0i4rlSRxBADbCRksH8oqHd5T2V8qNhKZ3XbEbR9MtYXiE7CYubzzlwWuQeA8rMWwQj_OZV0rjGyzfo-BeGdMEGZxjJRgC18e4yot-P4Q_uSB1ASMscxlrUb028vUI_n2H8cwm7bSYab9Xs2M2x9cI9Sc=)
15. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE66_wRWSIGgEFvFTVwFn60uLVIW43N5iSyxDhPD2eoOXUQ-yRvEOUQXjTT9oTxdfMjOmYfI38_DnK21OmNZrjvCyq53NPxzz7Cy7WYHA1MMxrIXXX_huRFCO4A5Ro=)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTmI7JWrHolWi9u2wPycohvBX9GBOdhck-iDxNHLXuON8gOG4gsg0U47ZQov4JjxUljDlAlQD9rPvKwCCWOpVhiE4mpjCVKn9WIW1IsIGI1Dj9_RAq9AcAN4pc8psPNBkMM2EudrhlIo_kS3dl0sMBivIBCiHH0f8st0Q8di48_zX8y6XG1qpP3IODsPbHulWPMEOSLPcmMC4UZFrfvpCMfKGTL2Wh5I-_a9EnzRNZuN2QIgO8MJUU5OllE6LnucZC7EA_GfZhUGRRGuL0WqM6bdsbLXev_4AR6UI41xbc)
17. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHg3oxiL1ZhSw2COlw0XSDSvTeRA4SrMFSR6bXlepiCt_kfRy4_Bm01E_j6oCLWAGBfUIoyuQHnMqlhoVLSeyFPmxyc2F3kT4JoDJ6fHLe0MeTKBhN8ITQJ0Q==)
18. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGa3uHoxuETNdknC7yozyi9J5YXcnIO0JX7W8kmwEpb5NftBqU_oMM41CSTTxn186kI8pVazGeB7Nnvz5Gpp5enfBYKkSPnlIaWyRUE035x5y9eFb_Usg==)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHr_9rKI1C7EXTebF2bsP2DIVwXR9vg6hvHhXqRtogFICKyRCYCRuH7cP22LCDk-oqrtaoC63_sPyt2mxFLrFkA4JXLyw4hgyKAZRdmf80Xt_jgD_H0G_t8t0mT9raKcDdsX3FpaTzSllW6eEOhItChkUtihBfA2L2VjD8TeUJlK7yug0lHJKKuNUoVITww5INgtarqGYZGHVArWCPCFjAzcStelkPGzV7qZKkHouaP3Eg=)
20. [accc.gov.au](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwQ7d__hCtIfKs8WGHXc8xa80-rKHuZHXIYP6k-PddgJFo2U0LF5MpqD_YB9j0MIhxCF-R3jMvyZ2x6tz_7kgqrzcnapJ_HfgKDn55OUvhneONKuDd9rCFBFG9u5tTOWFxx67Vv_yJmQvqHpoHr05mZAynHb8a4MKVgRX2-Fx260tDwIt1wKx4EkZYNVvi_FRKr-59UnCtmunf4P4GpOSGu_GT_A28hu6QR2iVQt_quHDgLfxiO1bxq2SCqfbCq1X1_zjd)
21. [purdue.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkSe-BLyVydDavaXlveJJQl3DIXVVRGhj4Z6zQBIlghmnFvvs4l-S9xpyxrxzHzmJuFVst9KlzJIplckdcBQ5EerNdZLji3ZDVFriGAL88r3hd0dniRSNIlWacIktC1yOD26yu2Q==)
22. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEzR1lHzinVuuU8DIK6mtJLalVXGsSdUYJU6tAhUTPbT7jxBLaWMf53n1_Cqott_A-wRzGeYtIVMEhwdbRGAaLhxVPjcMvGAdjPW-xkzdRwi50GFkD26jhsZijADGfYVtL3zYlahq8ql1suNzgS9st_05zFpHjBEqFEeOFwtlu28gSAvFKu1zJtmlUr6ocVcZXKMRZJhYTXsQsMLJxLLgYmGMocWVq9uVdQ3DR3goH3dZSYQ_v1KhCo6lOw-4vVOApbp85eF2_NRPy338dge2NN37KrjDBIWky3_5EdabBTgNn5VAcSXVnWMCutXO4BZ0g7Fw=)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2pQVNc8T95Iw6oVRu9F16fqnokfF62qj8rQpAcrKFgJghs9zBnYPv77ITdnG5S5ch4Iu_wILSt9_yqTCuSWJxfjE0eHjEefOCrxAQJy5Io6JgQs1UlIdTNAOAj_ETE7haoGj8VEIVKIJfiVOKaD1SadvAqFnJHTSzj8-_j17a22awWGh1M1X-BspWhsrHIVR4L8cxpI6hXmMVMP_5w3uO6Y_NR6l_)
24. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGF6iQwKWucOBnqGs2cn5k-s5ycozhYmFeq6JoTu6aHcNKmSZvunuaEZWDCTePcMHhC6F0W2FoElhGH7vm9o_lRhexcZ_inXhX6clIn7dYEIS7wBtAredDlJuGKeM=)
25. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6wmu4K3j6GavZHSFDIG7aFksiRD6JVGCZ9hyFvJ4mjtAkWdF9hzJhIOgFfxJCURZeCA0U8QkCf8u9zIZlH0o3rIYjQXG4s73eScEvLOcWuMK0Qok6mHvNzDbPaac=)
26. [tangent-h2020.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlpnMvE36Kcbb3_QT4kVnHuzcrvp-XwGwY1qkjOwNLnuAWhiGCm1ImpxdywYeX0z-D3Kgq3bHweq90hiO2iReZjM7TDihTak_rbuWiRlG84NyKo4zs6MUPRF_xDC-HoFppV3mShOjoJ3iKR-CW-F-lPcr--yJGX2fLfxPW-rRqlcM8QbYvCIsW-Pj4hMlClPG_kEeSP5DkqHWtlblc_hfEWMwfUxntsFSD2F1Su0A98tuLX-DExyK0PbMfTm8HIVG_YRl9XfuTf3BA3d1rOw==)
27. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgFVOnzq1e9L0omoIyDetRyOUVsVq2DQ1bDfov0rswe-3_K7ywyvQlZhr6u3mp0360miNkHhNzUwQV4rYhmJKLyrTcopiLFLxw2cRCo3dEc-yyIGWIWig8OGBgMsM=)
28. [plos.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOk9KB_tMnH_fEHwpCd4_i7LlSoLK1QLlmLptztReDa0Svk_UDUxdeCHUCg_mw0UWvfGcDSPXeFtw6P_G4wYPM0iNnRtBJ-159X8H0LnWv5AYNy2fbihWrxKuqjJW8UgYbJmtibych_73NsrUrEsiyDbK4HpfE4zrexCzt_gHP)
29. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFm3Ls5ZUuFwEM3Mjbtb4Y77nHPzegXMLPWG9FAs8V3-9PcU6UfeT2Y5-gMgcnJqMuaH112GvmstW1CM-tl-SW7SLtal7MOvHPSM9rRXe_Ni9Xl-jHuSr7NalzqL6fVQq92SfmIzRx6HDI5kkirvmUPbldW52BK4EAvLVBxhFuxj_o1dHrHizO_VZ5f1Sb-7e2O0PdQMt6KDZn9tzXfjwkA2ewHXpu8hor-0aTlERF--8OiBQU418uyuNjH_VdQmw6JNxXwEHEveeCbFNcsKALrXpyDRHNTXMkz5Ij0JtsRxIJtOy7QdJgGn6G19BP1a51piV1ddgPm941QuEF7Gj6r4fEaZ-UennEJdPD0AswuHEBw3tTY28NH8QhKH-E4av1tjM_eJtqf-eSw8fvbwYnJIJoELm5IWUAkX_LAovP4bA6s9bBQDTovgg==)
30. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyqLdSJ8-wsYR4KIVbL99QH8PZKm3K04XCm4foBADZE1b0RoKejDwB2cPs3rv4BVl8G5sAmy3n5KygndKJhO7H-TQi2DGciJB0XeNxb6VVaNIi0qAfb4mM1C8k)
31. [science.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG293hrct7ePJCsV8xVTWbM0IFKSD6Ky0vdwO-PeFvlHj4sBJvphA5FOxThRup7OmjpEYz64CJZR-i_ZjcayasJuzr_VG7UzkcB5sPF5HLx7QdEhxkEukYEN1NTmd2gxVuFyUD50VbdFn4b_1pV9QIftA==)
32. [griddynamics.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRFRwqUNaFU-6tC2hiVcWpRzsGFNin6cYk7TwGl_ic_RWXXfjE1u5Sb45QqT93GyQm0YG8-TBxBe5TMl3j9TM4pCA3SFgQyy9hVyh8Nww3PBvMKuvM7zO_R98XoNQRgAp0vDh8L5aniXKApPevOMEVuuP8YmbHykPy-fX1tjr4qZiClA==)
33. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGz-6efU8GEhAzqvrw3pypsAIQcv-7swjFYEEi2-Df78Drv1UC_JR06TSq7g3zIhd5wr-EvwObJBW9W28BC_ZbmGfeQ-lqEvkwMK-xTItaX40k_LR_8PQ9vULFnOac7cYJsZPa9t4spA3XbMXII3njZFYJmErk1ydw_p50aXyTykfRW5UkuIKFhcPw0Flk7zM1Ks88kzf_NXbc=)
34. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhkfVyo2Zqdz6ioO7Ndm8Ux_Ffsy4-PHPOCh5IPmVgfILlsMRw3QxlEiOfLX1hNOvcs5oKzFtpgxoV29GYHgwyHq-uFNsYkTmx-W_I75BhyoB6lLOmCw26HhW_yonf3imK)
35. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3iau6kO9sGWZg_3swII4FT6tcdSc7nWe6ilw9gt0Xpr_cAKzwOe-X2inb4h7WxPPPDjxLKAft161qyNJzA-hU3MGLoI5lISpHJgBAvuh5NqNS2HrHh8HQbrvMm-Ee2R4UWuxaw5LYw0W_jqDCpk7x6tzF4im40nC2M28eu21FU4L93wcs0YIDpDj7d_HjtEko5NdjgmAwz_fClhrnDkIsQe7gszpCY__IbHt5nz7WNA==)
36. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTssqcxQN6mFr_qaLDHUvqhIADmrAo0edBhLQnMBQWcYJwNrz96rkRu6lAQLCdsW9Lea6mOuWVgKwDbavtc0uuKceqNK3kWaWh08wDmLO9DEPYtx5goVM06o7wT8u2K0hqdFBJrKucPs7FN6zH_WjKMxQH4vMyLuUyqRxyAhs9ef6l_3ohMCVOE6zUtZXvSg7QXa2wMKu75cagBsSh)
37. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnm42fL_WgIocfRkJiq7lx8s8HysEq_DuYQlxgaY1xLw7wyWgAwWKpIpPyLpSoqOKCkKNEMea_4S-Zpb4HpfNE7ZAR2xqsxJbgsWaCbx6wM8VAAa419ZtRRob9qmZZ4LQAUxnkaHP4_bWjDT-HrwQY0KBOLTsaAjbXcJsj2oJ-mIqKN7JFGoRjmGBjBnt1n0Py_F62tNU=)
38. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAs4xCa3yW4HZVFiq-Y1fFJdQkY34BsIRcjBEp4WC8AANJY7StjgSatAS9-TcO43ntdQ7MOJ9jc5WJeBzrvlxJOL2ZL5G3NxFrwZcWrlb-Hsg2S_vrUijIWPLldOEs9cJrLq37u2Wl7xtqDXTq7wVkERt-GnB4vx0mBU-gx69-6Qy0q2j2te611BkdK_VeFXy87xVF4eHPb6t72NfX1jvwIoYSxD4bIhH6DhEOMYxHvvCWxQbzk2cEqyHuwZQ0ip15FixnfPzgm1o8P0YEt4xuAJvxFhguVGCzO6_bXhXYpXG5dZV6)


## Annotations
Annotation(end_index=2502, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEikn5f59uil7G-hqfQRbkmWrVdzuZIYs_5Fq5aUQZZgfTW34ndKFGQZ5gj_dITMn8yNsvin3q56aqEvHVJRkf-fdBFCyUEkgatuJSp9HFRj_dIONoME1RtrTkliWLI5pqv6CK5jZr8c-I8te9jhrvxy4Ymh6CBsLmvLx-TXlebjO_cqdbHp8g-IyhOGa7NSD7sV68EG1uteDvI3uQ9aWBxoApTQlzV9Co085RlGLK7IW-37g==', start_index=2487)
Annotation(end_index=2502, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFd6lONZKt26AhVIuyg3rkwyIQVAMRvJyQASiwk1Y6a2_q2tOUMbimBh-61iOF5db2aEr5R5HJn-4_dVGvbwYrkixQKANj7hf5TQkosmx9b51MNB9Tb5eU7xYvhKJbXVm5t0FMK11BZlwZGkFTiVUpybRzpkQ_yNRRwIBdtb6jX9H7GZZeK6acrePcD3J4CEBMxMYwhsW7QPWbS-UnB_l5zP5aQNmy7qk7OZjkMF_Eqfg35XL2pPzr9NOQr6w==', start_index=2487)
Annotation(end_index=2502, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGG1i7KLgWKMzXzGOQ2WKkctn_p6KxYpi6J72T_hhIj_vgfoLGvrIlXAk6MyTjj4PQ2fT61SMRhVUXKeJOZ_hVEgpg1dbiQh2nC_FUA0y5L51sGL-ic3IrM5sozM6YsmCXZBeJbZEufwgmhlcohSzfaYwLaxLLpGdEHWKyNxTOncwvuw5zHhMqfkyriPE56JSHSAg7sykmdRPBfhBhF', start_index=2487)
Annotation(end_index=2950, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBumi1ZUDGtTspXYqXucXcjpiEdbgJ6YVEcUANRPVkeA55bajFOiRcYzhr_s26th4yuu-SE57jnkdGPfMNC_UCgemWaV-Hq-iJd2Yw2m4b9IkNGaDTHfWvK8KE8Kl7GaW_zCkNKWnw1VsA6J-wrix0bVQ7', start_index=2935)
Annotation(end_index=2950, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFT4NjJIJCAdZKyPzL9XB6I7ZMy5G852MAYT5xothbme4AztlgrE9hOpWvvDDToP0Sdg9pOc3I25zt7yEhLVQpZpGZZDfbpgC_cVrZMssOJgIXbt2KFWedpa5Ad_9enl7HGkm2QX-T0HqeLWpUf210LdS_93W52pHrXCu8MKk8wcVmNLmU=', start_index=2935)
Annotation(end_index=2950, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2mZwBFRJkraPP3_hgpQs8D6cAmWtsEGGXfEHHtM_sfYDSKogVwj5Li-mPUWhTxGFsACmeYPiGYs73XSschgO7WAABgsrmTpSOj-seM-G7FkQhwfvjZsFp5fPV7MWP6qkxTqxZTQSgMLZ1jW81zUGcStdS-P-ILaGeCAR5tQufch84G2GKGJizMRB7GA==', start_index=2935)
Annotation(end_index=3130, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG22AB7VXefbSW4jX0p7iyCOMrpc2P9m7HhZ1CJYmyVQxy-hcGgHnVEdQmT-kXUvwb5oMhtzQa3zRiCFQyXIQ2bydxxOCIrbTd7KjpGdygP_NEelNpL_Ogi0MbBCPPyk1JCz-FxTQxnLgtYMQ-QAme_2yv5pNr1CQA_E5G_5cbsphR8_YaGwh9rXsqkOix7njJ0479C5GLMOgQEUZnYOzfJ', start_index=3118)
Annotation(end_index=3130, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGG1i7KLgWKMzXzGOQ2WKkctn_p6KxYpi6J72T_hhIj_vgfoLGvrIlXAk6MyTjj4PQ2fT61SMRhVUXKeJOZ_hVEgpg1dbiQh2nC_FUA0y5L51sGL-ic3IrM5sozM6YsmCXZBeJbZEufwgmhlcohSzfaYwLaxLLpGdEHWKyNxTOncwvuw5zHhMqfkyriPE56JSHSAg7sykmdRPBfhBhF', start_index=3118)
Annotation(end_index=3476, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0AuRS48Wyceo_cRyrr1tqXIhQsxtSbc4E4eBdUEiKmXH2OQ6jm1RFAAItPCCT-4-EuXZOEadSY8B0HzKPQZ76EmhlQx5g-zgc5owN97Kg_-BhYFG4tQdR3uHCtcOL86ympIUlsnitgAvqE19UvdqBhKok526DXYiCHrvbDI7LviMjaK52AnUTIAidC20oT6lppPVFmlFlnlu9', start_index=3464)
Annotation(end_index=3476, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPDW9zrlrxGZgi6twWi988iGoQwqhLku-4jwkWdtMh9NgWQxwebSi4bl0l6QR7Ry5V9bH08aPhH5Se8895Z9FpT4uM-KbV1Iz_gJNw843YlA6LdY_BWgiyJQ==', start_index=3464)
Annotation(end_index=4087, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQQaZjEQlc-uTKB3DqZtpOg1f32DLZmF8_H7_vV8t4-ypreYtF6QTxtM4zrq1KLVunCBefVe-MyV5Yj8JCq7nvkMgw3fMdWQhTQff2ReuTk783ULQhsQt3Z2dWx5dZJg==', start_index=4069)
Annotation(end_index=4087, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEneLZPSqTeFjM3loL6YRTCWE5mvk5owvCjdZI6y30urkw_O4Gi96SyFrt3px8SsATFW-obCmBIUm6lS5QaJnEtjO6cCx7T9Wlc9WP0WIrognwWNWGuaR2cQike4FAdWg9jaWsgdF_S7HFH0GGTYQ2OgWMSQQsI1no9AhQuQYhK6s48dok_NEi-40AxHlu0aBjkPq1aNcvyOvT8nrFD_QfjheYuCIQ=', start_index=4069)
Annotation(end_index=4087, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKrJKUHR_WDur_cUJra2oCfPDsLzjlzmtLjEh5m85tUGn63RNPKpmJdlC6sYItG8fuA4EREwbqrWdQkkzGm3bZd0GrrR_Q1r1PfwspXgsCukIj0gJwX0sOXEbJPwGXm3jw6SWIMjFdc9fLj7yCq5w=', start_index=4069)
Annotation(end_index=4590, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBumi1ZUDGtTspXYqXucXcjpiEdbgJ6YVEcUANRPVkeA55bajFOiRcYzhr_s26th4yuu-SE57jnkdGPfMNC_UCgemWaV-Hq-iJd2Yw2m4b9IkNGaDTHfWvK8KE8Kl7GaW_zCkNKWnw1VsA6J-wrix0bVQ7', start_index=4578)
Annotation(end_index=4590, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2mZwBFRJkraPP3_hgpQs8D6cAmWtsEGGXfEHHtM_sfYDSKogVwj5Li-mPUWhTxGFsACmeYPiGYs73XSschgO7WAABgsrmTpSOj-seM-G7FkQhwfvjZsFp5fPV7MWP6qkxTqxZTQSgMLZ1jW81zUGcStdS-P-ILaGeCAR5tQufch84G2GKGJizMRB7GA==', start_index=4578)
Annotation(end_index=5104, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBumi1ZUDGtTspXYqXucXcjpiEdbgJ6YVEcUANRPVkeA55bajFOiRcYzhr_s26th4yuu-SE57jnkdGPfMNC_UCgemWaV-Hq-iJd2Yw2m4b9IkNGaDTHfWvK8KE8Kl7GaW_zCkNKWnw1VsA6J-wrix0bVQ7', start_index=5091)
Annotation(end_index=5104, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxIUJPkWL8TJ5r6N8hrcOlPJYhkNYF4sFUtGLUy6QPzIm0rD1kGnQCLikgB-nDBQb7xbD8KiP_xXblyliCmAxFSQjYOva2IucWHTcJ-jZlIFgibtgmMDp4E3M_4kSrc48sxNxr9EKBWREQUzPvPZ0Mv4uMNqSuSiiwJ5JEMXu4d3R1BYy4diD-LB58TyA82XMgNk84B0lZkcJkJQ==', start_index=5091)
Annotation(end_index=5354, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEljgPjn2qnmMrhrsTuV8-uoqY-74JxFpRIAievagJPhayPyBp8ZqvE3xLzIH7dXmCVTLXlILxuYDy13mk6Hza0i4rlSRxBADbCRksH8oqHd5T2V8qNhKZ3XbEbR9MtYXiE7CYubzzlwWuQeA8rMWwQj_OZV0rjGyzfo-BeGdMEGZxjJRgC18e4yot-P4Q_uSB1ASMscxlrUb028vUI_n2H8cwm7bSYab9Xs2M2x9cI9Sc=', start_index=5337)
Annotation(end_index=5354, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEneLZPSqTeFjM3loL6YRTCWE5mvk5owvCjdZI6y30urkw_O4Gi96SyFrt3px8SsATFW-obCmBIUm6lS5QaJnEtjO6cCx7T9Wlc9WP0WIrognwWNWGuaR2cQike4FAdWg9jaWsgdF_S7HFH0GGTYQ2OgWMSQQsI1no9AhQuQYhK6s48dok_NEi-40AxHlu0aBjkPq1aNcvyOvT8nrFD_QfjheYuCIQ=', start_index=5337)
Annotation(end_index=5354, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFT4NjJIJCAdZKyPzL9XB6I7ZMy5G852MAYT5xothbme4AztlgrE9hOpWvvDDToP0Sdg9pOc3I25zt7yEhLVQpZpGZZDfbpgC_cVrZMssOJgIXbt2KFWedpa5Ad_9enl7HGkm2QX-T0HqeLWpUf210LdS_93W52pHrXCu8MKk8wcVmNLmU=', start_index=5337)
Annotation(end_index=5686, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE66_wRWSIGgEFvFTVwFn60uLVIW43N5iSyxDhPD2eoOXUQ-yRvEOUQXjTT9oTxdfMjOmYfI38_DnK21OmNZrjvCyq53NPxzz7Cy7WYHA1MMxrIXXX_huRFCO4A5Ro=', start_index=5668)
Annotation(end_index=5686, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTmI7JWrHolWi9u2wPycohvBX9GBOdhck-iDxNHLXuON8gOG4gsg0U47ZQov4JjxUljDlAlQD9rPvKwCCWOpVhiE4mpjCVKn9WIW1IsIGI1Dj9_RAq9AcAN4pc8psPNBkMM2EudrhlIo_kS3dl0sMBivIBCiHH0f8st0Q8di48_zX8y6XG1qpP3IODsPbHulWPMEOSLPcmMC4UZFrfvpCMfKGTL2Wh5I-_a9EnzRNZuN2QIgO8MJUU5OllE6LnucZC7EA_GfZhUGRRGuL0WqM6bdsbLXev_4AR6UI41xbc', start_index=5668)
Annotation(end_index=5686, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHg3oxiL1ZhSw2COlw0XSDSvTeRA4SrMFSR6bXlepiCt_kfRy4_Bm01E_j6oCLWAGBfUIoyuQHnMqlhoVLSeyFPmxyc2F3kT4JoDJ6fHLe0MeTKBhN8ITQJ0Q==', start_index=5668)
Annotation(end_index=6148, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG22AB7VXefbSW4jX0p7iyCOMrpc2P9m7HhZ1CJYmyVQxy-hcGgHnVEdQmT-kXUvwb5oMhtzQa3zRiCFQyXIQ2bydxxOCIrbTd7KjpGdygP_NEelNpL_Ogi0MbBCPPyk1JCz-FxTQxnLgtYMQ-QAme_2yv5pNr1CQA_E5G_5cbsphR8_YaGwh9rXsqkOix7njJ0479C5GLMOgQEUZnYOzfJ', start_index=6136)
Annotation(end_index=6148, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGG1i7KLgWKMzXzGOQ2WKkctn_p6KxYpi6J72T_hhIj_vgfoLGvrIlXAk6MyTjj4PQ2fT61SMRhVUXKeJOZ_hVEgpg1dbiQh2nC_FUA0y5L51sGL-ic3IrM5sozM6YsmCXZBeJbZEufwgmhlcohSzfaYwLaxLLpGdEHWKyNxTOncwvuw5zHhMqfkyriPE56JSHSAg7sykmdRPBfhBhF', start_index=6136)
Annotation(end_index=6444, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBumi1ZUDGtTspXYqXucXcjpiEdbgJ6YVEcUANRPVkeA55bajFOiRcYzhr_s26th4yuu-SE57jnkdGPfMNC_UCgemWaV-Hq-iJd2Yw2m4b9IkNGaDTHfWvK8KE8Kl7GaW_zCkNKWnw1VsA6J-wrix0bVQ7', start_index=6423)
Annotation(end_index=6444, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKrJKUHR_WDur_cUJra2oCfPDsLzjlzmtLjEh5m85tUGn63RNPKpmJdlC6sYItG8fuA4EREwbqrWdQkkzGm3bZd0GrrR_Q1r1PfwspXgsCukIj0gJwX0sOXEbJPwGXm3jw6SWIMjFdc9fLj7yCq5w=', start_index=6423)
Annotation(end_index=6444, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGa3uHoxuETNdknC7yozyi9J5YXcnIO0JX7W8kmwEpb5NftBqU_oMM41CSTTxn186kI8pVazGeB7Nnvz5Gpp5enfBYKkSPnlIaWyRUE035x5y9eFb_Usg==', start_index=6423)
Annotation(end_index=6444, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHr_9rKI1C7EXTebF2bsP2DIVwXR9vg6hvHhXqRtogFICKyRCYCRuH7cP22LCDk-oqrtaoC63_sPyt2mxFLrFkA4JXLyw4hgyKAZRdmf80Xt_jgD_H0G_t8t0mT9raKcDdsX3FpaTzSllW6eEOhItChkUtihBfA2L2VjD8TeUJlK7yug0lHJKKuNUoVITww5INgtarqGYZGHVArWCPCFjAzcStelkPGzV7qZKkHouaP3Eg=', start_index=6423)
Annotation(end_index=6651, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBumi1ZUDGtTspXYqXucXcjpiEdbgJ6YVEcUANRPVkeA55bajFOiRcYzhr_s26th4yuu-SE57jnkdGPfMNC_UCgemWaV-Hq-iJd2Yw2m4b9IkNGaDTHfWvK8KE8Kl7GaW_zCkNKWnw1VsA6J-wrix0bVQ7', start_index=6638)
Annotation(end_index=6651, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKrJKUHR_WDur_cUJra2oCfPDsLzjlzmtLjEh5m85tUGn63RNPKpmJdlC6sYItG8fuA4EREwbqrWdQkkzGm3bZd0GrrR_Q1r1PfwspXgsCukIj0gJwX0sOXEbJPwGXm3jw6SWIMjFdc9fLj7yCq5w=', start_index=6638)
Annotation(end_index=6977, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwQ7d__hCtIfKs8WGHXc8xa80-rKHuZHXIYP6k-PddgJFo2U0LF5MpqD_YB9j0MIhxCF-R3jMvyZ2x6tz_7kgqrzcnapJ_HfgKDn55OUvhneONKuDd9rCFBFG9u5tTOWFxx67Vv_yJmQvqHpoHr05mZAynHb8a4MKVgRX2-Fx260tDwIt1wKx4EkZYNVvi_FRKr-59UnCtmunf4P4GpOSGu_GT_A28hu6QR2iVQt_quHDgLfxiO1bxq2SCqfbCq1X1_zjd', start_index=6960)
Annotation(end_index=6977, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFT4NjJIJCAdZKyPzL9XB6I7ZMy5G852MAYT5xothbme4AztlgrE9hOpWvvDDToP0Sdg9pOc3I25zt7yEhLVQpZpGZZDfbpgC_cVrZMssOJgIXbt2KFWedpa5Ad_9enl7HGkm2QX-T0HqeLWpUf210LdS_93W52pHrXCu8MKk8wcVmNLmU=', start_index=6960)
Annotation(end_index=6977, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkSe-BLyVydDavaXlveJJQl3DIXVVRGhj4Z6zQBIlghmnFvvs4l-S9xpyxrxzHzmJuFVst9KlzJIplckdcBQ5EerNdZLji3ZDVFriGAL88r3hd0dniRSNIlWacIktC1yOD26yu2Q==', start_index=6960)
Annotation(end_index=7831, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwQ7d__hCtIfKs8WGHXc8xa80-rKHuZHXIYP6k-PddgJFo2U0LF5MpqD_YB9j0MIhxCF-R3jMvyZ2x6tz_7kgqrzcnapJ_HfgKDn55OUvhneONKuDd9rCFBFG9u5tTOWFxx67Vv_yJmQvqHpoHr05mZAynHb8a4MKVgRX2-Fx260tDwIt1wKx4EkZYNVvi_FRKr-59UnCtmunf4P4GpOSGu_GT_A28hu6QR2iVQt_quHDgLfxiO1bxq2SCqfbCq1X1_zjd', start_index=7818)
Annotation(end_index=7831, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGG1i7KLgWKMzXzGOQ2WKkctn_p6KxYpi6J72T_hhIj_vgfoLGvrIlXAk6MyTjj4PQ2fT61SMRhVUXKeJOZ_hVEgpg1dbiQh2nC_FUA0y5L51sGL-ic3IrM5sozM6YsmCXZBeJbZEufwgmhlcohSzfaYwLaxLLpGdEHWKyNxTOncwvuw5zHhMqfkyriPE56JSHSAg7sykmdRPBfhBhF', start_index=7818)
Annotation(end_index=8217, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwQ7d__hCtIfKs8WGHXc8xa80-rKHuZHXIYP6k-PddgJFo2U0LF5MpqD_YB9j0MIhxCF-R3jMvyZ2x6tz_7kgqrzcnapJ_HfgKDn55OUvhneONKuDd9rCFBFG9u5tTOWFxx67Vv_yJmQvqHpoHr05mZAynHb8a4MKVgRX2-Fx260tDwIt1wKx4EkZYNVvi_FRKr-59UnCtmunf4P4GpOSGu_GT_A28hu6QR2iVQt_quHDgLfxiO1bxq2SCqfbCq1X1_zjd', start_index=8204)
Annotation(end_index=8217, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGG1i7KLgWKMzXzGOQ2WKkctn_p6KxYpi6J72T_hhIj_vgfoLGvrIlXAk6MyTjj4PQ2fT61SMRhVUXKeJOZ_hVEgpg1dbiQh2nC_FUA0y5L51sGL-ic3IrM5sozM6YsmCXZBeJbZEufwgmhlcohSzfaYwLaxLLpGdEHWKyNxTOncwvuw5zHhMqfkyriPE56JSHSAg7sykmdRPBfhBhF', start_index=8204)
Annotation(end_index=8754, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE66_wRWSIGgEFvFTVwFn60uLVIW43N5iSyxDhPD2eoOXUQ-yRvEOUQXjTT9oTxdfMjOmYfI38_DnK21OmNZrjvCyq53NPxzz7Cy7WYHA1MMxrIXXX_huRFCO4A5Ro=', start_index=8736)
Annotation(end_index=8754, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2pQVNc8T95Iw6oVRu9F16fqnokfF62qj8rQpAcrKFgJghs9zBnYPv77ITdnG5S5ch4Iu_wILSt9_yqTCuSWJxfjE0eHjEefOCrxAQJy5Io6JgQs1UlIdTNAOAj_ETE7haoGj8VEIVKIJfiVOKaD1SadvAqFnJHTSzj8-_j17a22awWGh1M1X-BspWhsrHIVR4L8cxpI6hXmMVMP_5w3uO6Y_NR6l_', start_index=8736)
Annotation(end_index=8754, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEzR1lHzinVuuU8DIK6mtJLalVXGsSdUYJU6tAhUTPbT7jxBLaWMf53n1_Cqott_A-wRzGeYtIVMEhwdbRGAaLhxVPjcMvGAdjPW-xkzdRwi50GFkD26jhsZijADGfYVtL3zYlahq8ql1suNzgS9st_05zFpHjBEqFEeOFwtlu28gSAvFKu1zJtmlUr6ocVcZXKMRZJhYTXsQsMLJxLLgYmGMocWVq9uVdQ3DR3goH3dZSYQ_v1KhCo6lOw-4vVOApbp85eF2_NRPy338dge2NN37KrjDBIWky3_5EdabBTgNn5VAcSXVnWMCutXO4BZ0g7Fw=', start_index=8736)
Annotation(end_index=9161, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGF6iQwKWucOBnqGs2cn5k-s5ycozhYmFeq6JoTu6aHcNKmSZvunuaEZWDCTePcMHhC6F0W2FoElhGH7vm9o_lRhexcZ_inXhX6clIn7dYEIS7wBtAredDlJuGKeM=', start_index=9151)
Annotation(end_index=9296, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGG1i7KLgWKMzXzGOQ2WKkctn_p6KxYpi6J72T_hhIj_vgfoLGvrIlXAk6MyTjj4PQ2fT61SMRhVUXKeJOZ_hVEgpg1dbiQh2nC_FUA0y5L51sGL-ic3IrM5sozM6YsmCXZBeJbZEufwgmhlcohSzfaYwLaxLLpGdEHWKyNxTOncwvuw5zHhMqfkyriPE56JSHSAg7sykmdRPBfhBhF', start_index=9287)
Annotation(end_index=9657, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFT4NjJIJCAdZKyPzL9XB6I7ZMy5G852MAYT5xothbme4AztlgrE9hOpWvvDDToP0Sdg9pOc3I25zt7yEhLVQpZpGZZDfbpgC_cVrZMssOJgIXbt2KFWedpa5Ad_9enl7HGkm2QX-T0HqeLWpUf210LdS_93W52pHrXCu8MKk8wcVmNLmU=', start_index=9644)
Annotation(end_index=9657, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkSe-BLyVydDavaXlveJJQl3DIXVVRGhj4Z6zQBIlghmnFvvs4l-S9xpyxrxzHzmJuFVst9KlzJIplckdcBQ5EerNdZLji3ZDVFriGAL88r3hd0dniRSNIlWacIktC1yOD26yu2Q==', start_index=9644)
Annotation(end_index=9972, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEneLZPSqTeFjM3loL6YRTCWE5mvk5owvCjdZI6y30urkw_O4Gi96SyFrt3px8SsATFW-obCmBIUm6lS5QaJnEtjO6cCx7T9Wlc9WP0WIrognwWNWGuaR2cQike4FAdWg9jaWsgdF_S7HFH0GGTYQ2OgWMSQQsI1no9AhQuQYhK6s48dok_NEi-40AxHlu0aBjkPq1aNcvyOvT8nrFD_QfjheYuCIQ=', start_index=9959)
Annotation(end_index=9972, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFT4NjJIJCAdZKyPzL9XB6I7ZMy5G852MAYT5xothbme4AztlgrE9hOpWvvDDToP0Sdg9pOc3I25zt7yEhLVQpZpGZZDfbpgC_cVrZMssOJgIXbt2KFWedpa5Ad_9enl7HGkm2QX-T0HqeLWpUf210LdS_93W52pHrXCu8MKk8wcVmNLmU=', start_index=9959)
Annotation(end_index=11103, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBumi1ZUDGtTspXYqXucXcjpiEdbgJ6YVEcUANRPVkeA55bajFOiRcYzhr_s26th4yuu-SE57jnkdGPfMNC_UCgemWaV-Hq-iJd2Yw2m4b9IkNGaDTHfWvK8KE8Kl7GaW_zCkNKWnw1VsA6J-wrix0bVQ7', start_index=11094)
Annotation(end_index=11446, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBumi1ZUDGtTspXYqXucXcjpiEdbgJ6YVEcUANRPVkeA55bajFOiRcYzhr_s26th4yuu-SE57jnkdGPfMNC_UCgemWaV-Hq-iJd2Yw2m4b9IkNGaDTHfWvK8KE8Kl7GaW_zCkNKWnw1VsA6J-wrix0bVQ7', start_index=11434)
Annotation(end_index=11446, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2mZwBFRJkraPP3_hgpQs8D6cAmWtsEGGXfEHHtM_sfYDSKogVwj5Li-mPUWhTxGFsACmeYPiGYs73XSschgO7WAABgsrmTpSOj-seM-G7FkQhwfvjZsFp5fPV7MWP6qkxTqxZTQSgMLZ1jW81zUGcStdS-P-ILaGeCAR5tQufch84G2GKGJizMRB7GA==', start_index=11434)
Annotation(end_index=11876, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGF6iQwKWucOBnqGs2cn5k-s5ycozhYmFeq6JoTu6aHcNKmSZvunuaEZWDCTePcMHhC6F0W2FoElhGH7vm9o_lRhexcZ_inXhX6clIn7dYEIS7wBtAredDlJuGKeM=', start_index=11866)
Annotation(end_index=12202, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlpnMvE36Kcbb3_QT4kVnHuzcrvp-XwGwY1qkjOwNLnuAWhiGCm1ImpxdywYeX0z-D3Kgq3bHweq90hiO2iReZjM7TDihTak_rbuWiRlG84NyKo4zs6MUPRF_xDC-HoFppV3mShOjoJ3iKR-CW-F-lPcr--yJGX2fLfxPW-rRqlcM8QbYvCIsW-Pj4hMlClPG_kEeSP5DkqHWtlblc_hfEWMwfUxntsFSD2F1Su0A98tuLX-DExyK0PbMfTm8HIVG_YRl9XfuTf3BA3d1rOw==', start_index=12188)
Annotation(end_index=12202, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6wmu4K3j6GavZHSFDIG7aFksiRD6JVGCZ9hyFvJ4mjtAkWdF9hzJhIOgFfxJCURZeCA0U8QkCf8u9zIZlH0o3rIYjQXG4s73eScEvLOcWuMK0Qok6mHvNzDbPaac=', start_index=12188)
Annotation(end_index=12741, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0AuRS48Wyceo_cRyrr1tqXIhQsxtSbc4E4eBdUEiKmXH2OQ6jm1RFAAItPCCT-4-EuXZOEadSY8B0HzKPQZ76EmhlQx5g-zgc5owN97Kg_-BhYFG4tQdR3uHCtcOL86ympIUlsnitgAvqE19UvdqBhKok526DXYiCHrvbDI7LviMjaK52AnUTIAidC20oT6lppPVFmlFlnlu9', start_index=12729)
Annotation(end_index=12741, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPDW9zrlrxGZgi6twWi988iGoQwqhLku-4jwkWdtMh9NgWQxwebSi4bl0l6QR7Ry5V9bH08aPhH5Se8895Z9FpT4uM-KbV1Iz_gJNw843YlA6LdY_BWgiyJQ==', start_index=12729)
Annotation(end_index=13184, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgFVOnzq1e9L0omoIyDetRyOUVsVq2DQ1bDfov0rswe-3_K7ywyvQlZhr6u3mp0360miNkHhNzUwQV4rYhmJKLyrTcopiLFLxw2cRCo3dEc-yyIGWIWig8OGBgMsM=', start_index=13170)
Annotation(end_index=13184, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOk9KB_tMnH_fEHwpCd4_i7LlSoLK1QLlmLptztReDa0Svk_UDUxdeCHUCg_mw0UWvfGcDSPXeFtw6P_G4wYPM0iNnRtBJ-159X8H0LnWv5AYNy2fbihWrxKuqjJW8UgYbJmtibych_73NsrUrEsiyDbK4HpfE4zrexCzt_gHP', start_index=13170)
Annotation(end_index=13728, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOk9KB_tMnH_fEHwpCd4_i7LlSoLK1QLlmLptztReDa0Svk_UDUxdeCHUCg_mw0UWvfGcDSPXeFtw6P_G4wYPM0iNnRtBJ-159X8H0LnWv5AYNy2fbihWrxKuqjJW8UgYbJmtibych_73NsrUrEsiyDbK4HpfE4zrexCzt_gHP', start_index=13718)
Annotation(end_index=14012, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0AuRS48Wyceo_cRyrr1tqXIhQsxtSbc4E4eBdUEiKmXH2OQ6jm1RFAAItPCCT-4-EuXZOEadSY8B0HzKPQZ76EmhlQx5g-zgc5owN97Kg_-BhYFG4tQdR3uHCtcOL86ympIUlsnitgAvqE19UvdqBhKok526DXYiCHrvbDI7LviMjaK52AnUTIAidC20oT6lppPVFmlFlnlu9', start_index=14003)
Annotation(end_index=14331, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFm3Ls5ZUuFwEM3Mjbtb4Y77nHPzegXMLPWG9FAs8V3-9PcU6UfeT2Y5-gMgcnJqMuaH112GvmstW1CM-tl-SW7SLtal7MOvHPSM9rRXe_Ni9Xl-jHuSr7NalzqL6fVQq92SfmIzRx6HDI5kkirvmUPbldW52BK4EAvLVBxhFuxj_o1dHrHizO_VZ5f1Sb-7e2O0PdQMt6KDZn9tzXfjwkA2ewHXpu8hor-0aTlERF--8OiBQU418uyuNjH_VdQmw6JNxXwEHEveeCbFNcsKALrXpyDRHNTXMkz5Ij0JtsRxIJtOy7QdJgGn6G19BP1a51piV1ddgPm941QuEF7Gj6r4fEaZ-UennEJdPD0AswuHEBw3tTY28NH8QhKH-E4av1tjM_eJtqf-eSw8fvbwYnJIJoELm5IWUAkX_LAovP4bA6s9bBQDTovgg==', start_index=14321)
Annotation(end_index=14912, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEikn5f59uil7G-hqfQRbkmWrVdzuZIYs_5Fq5aUQZZgfTW34ndKFGQZ5gj_dITMn8yNsvin3q56aqEvHVJRkf-fdBFCyUEkgatuJSp9HFRj_dIONoME1RtrTkliWLI5pqv6CK5jZr8c-I8te9jhrvxy4Ymh6CBsLmvLx-TXlebjO_cqdbHp8g-IyhOGa7NSD7sV68EG1uteDvI3uQ9aWBxoApTQlzV9Co085RlGLK7IW-37g==', start_index=14903)
Annotation(end_index=15092, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG293hrct7ePJCsV8xVTWbM0IFKSD6Ky0vdwO-PeFvlHj4sBJvphA5FOxThRup7OmjpEYz64CJZR-i_ZjcayasJuzr_VG7UzkcB5sPF5HLx7QdEhxkEukYEN1NTmd2gxVuFyUD50VbdFn4b_1pV9QIftA==', start_index=15078)
Annotation(end_index=15092, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyqLdSJ8-wsYR4KIVbL99QH8PZKm3K04XCm4foBADZE1b0RoKejDwB2cPs3rv4BVl8G5sAmy3n5KygndKJhO7H-TQi2DGciJB0XeNxb6VVaNIi0qAfb4mM1C8k', start_index=15078)
Annotation(end_index=15510, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhkfVyo2Zqdz6ioO7Ndm8Ux_Ffsy4-PHPOCh5IPmVgfILlsMRw3QxlEiOfLX1hNOvcs5oKzFtpgxoV29GYHgwyHq-uFNsYkTmx-W_I75BhyoB6lLOmCw26HhW_yonf3imK', start_index=15492)
Annotation(end_index=15510, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRFRwqUNaFU-6tC2hiVcWpRzsGFNin6cYk7TwGl_ic_RWXXfjE1u5Sb45QqT93GyQm0YG8-TBxBe5TMl3j9TM4pCA3SFgQyy9hVyh8Nww3PBvMKuvM7zO_R98XoNQRgAp0vDh8L5aniXKApPevOMEVuuP8YmbHykPy-fX1tjr4qZiClA==', start_index=15492)
Annotation(end_index=15510, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGz-6efU8GEhAzqvrw3pypsAIQcv-7swjFYEEi2-Df78Drv1UC_JR06TSq7g3zIhd5wr-EvwObJBW9W28BC_ZbmGfeQ-lqEvkwMK-xTItaX40k_LR_8PQ9vULFnOac7cYJsZPa9t4spA3XbMXII3njZFYJmErk1ydw_p50aXyTykfRW5UkuIKFhcPw0Flk7zM1Ks88kzf_NXbc=', start_index=15492)
Annotation(end_index=15759, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhkfVyo2Zqdz6ioO7Ndm8Ux_Ffsy4-PHPOCh5IPmVgfILlsMRw3QxlEiOfLX1hNOvcs5oKzFtpgxoV29GYHgwyHq-uFNsYkTmx-W_I75BhyoB6lLOmCw26HhW_yonf3imK', start_index=15749)
Annotation(end_index=16221, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGF6iQwKWucOBnqGs2cn5k-s5ycozhYmFeq6JoTu6aHcNKmSZvunuaEZWDCTePcMHhC6F0W2FoElhGH7vm9o_lRhexcZ_inXhX6clIn7dYEIS7wBtAredDlJuGKeM=', start_index=16200)
Annotation(end_index=16221, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG22AB7VXefbSW4jX0p7iyCOMrpc2P9m7HhZ1CJYmyVQxy-hcGgHnVEdQmT-kXUvwb5oMhtzQa3zRiCFQyXIQ2bydxxOCIrbTd7KjpGdygP_NEelNpL_Ogi0MbBCPPyk1JCz-FxTQxnLgtYMQ-QAme_2yv5pNr1CQA_E5G_5cbsphR8_YaGwh9rXsqkOix7njJ0479C5GLMOgQEUZnYOzfJ', start_index=16200)
Annotation(end_index=16221, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG293hrct7ePJCsV8xVTWbM0IFKSD6Ky0vdwO-PeFvlHj4sBJvphA5FOxThRup7OmjpEYz64CJZR-i_ZjcayasJuzr_VG7UzkcB5sPF5HLx7QdEhxkEukYEN1NTmd2gxVuFyUD50VbdFn4b_1pV9QIftA==', start_index=16200)
Annotation(end_index=16221, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3iau6kO9sGWZg_3swII4FT6tcdSc7nWe6ilw9gt0Xpr_cAKzwOe-X2inb4h7WxPPPDjxLKAft161qyNJzA-hU3MGLoI5lISpHJgBAvuh5NqNS2HrHh8HQbrvMm-Ee2R4UWuxaw5LYw0W_jqDCpk7x6tzF4im40nC2M28eu21FU4L93wcs0YIDpDj7d_HjtEko5NdjgmAwz_fClhrnDkIsQe7gszpCY__IbHt5nz7WNA==', start_index=16200)
Annotation(end_index=16424, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3iau6kO9sGWZg_3swII4FT6tcdSc7nWe6ilw9gt0Xpr_cAKzwOe-X2inb4h7WxPPPDjxLKAft161qyNJzA-hU3MGLoI5lISpHJgBAvuh5NqNS2HrHh8HQbrvMm-Ee2R4UWuxaw5LYw0W_jqDCpk7x6tzF4im40nC2M28eu21FU4L93wcs0YIDpDj7d_HjtEko5NdjgmAwz_fClhrnDkIsQe7gszpCY__IbHt5nz7WNA==', start_index=16414)
Annotation(end_index=18467, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTssqcxQN6mFr_qaLDHUvqhIADmrAo0edBhLQnMBQWcYJwNrz96rkRu6lAQLCdsW9Lea6mOuWVgKwDbavtc0uuKceqNK3kWaWh08wDmLO9DEPYtx5goVM06o7wT8u2K0hqdFBJrKucPs7FN6zH_WjKMxQH4vMyLuUyqRxyAhs9ef6l_3ohMCVOE6zUtZXvSg7QXa2wMKu75cagBsSh', start_index=18457)
Annotation(end_index=18754, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHr_9rKI1C7EXTebF2bsP2DIVwXR9vg6hvHhXqRtogFICKyRCYCRuH7cP22LCDk-oqrtaoC63_sPyt2mxFLrFkA4JXLyw4hgyKAZRdmf80Xt_jgD_H0G_t8t0mT9raKcDdsX3FpaTzSllW6eEOhItChkUtihBfA2L2VjD8TeUJlK7yug0lHJKKuNUoVITww5INgtarqGYZGHVArWCPCFjAzcStelkPGzV7qZKkHouaP3Eg=', start_index=18744)
Annotation(end_index=19364, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyqLdSJ8-wsYR4KIVbL99QH8PZKm3K04XCm4foBADZE1b0RoKejDwB2cPs3rv4BVl8G5sAmy3n5KygndKJhO7H-TQi2DGciJB0XeNxb6VVaNIi0qAfb4mM1C8k', start_index=19354)
Annotation(end_index=19671, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHg3oxiL1ZhSw2COlw0XSDSvTeRA4SrMFSR6bXlepiCt_kfRy4_Bm01E_j6oCLWAGBfUIoyuQHnMqlhoVLSeyFPmxyc2F3kT4JoDJ6fHLe0MeTKBhN8ITQJ0Q==', start_index=19661)
Annotation(end_index=20206, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnm42fL_WgIocfRkJiq7lx8s8HysEq_DuYQlxgaY1xLw7wyWgAwWKpIpPyLpSoqOKCkKNEMea_4S-Zpb4HpfNE7ZAR2xqsxJbgsWaCbx6wM8VAAa419ZtRRob9qmZZ4LQAUxnkaHP4_bWjDT-HrwQY0KBOLTsaAjbXcJsj2oJ-mIqKN7JFGoRjmGBjBnt1n0Py_F62tNU=', start_index=20188)
Annotation(end_index=20206, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwQ7d__hCtIfKs8WGHXc8xa80-rKHuZHXIYP6k-PddgJFo2U0LF5MpqD_YB9j0MIhxCF-R3jMvyZ2x6tz_7kgqrzcnapJ_HfgKDn55OUvhneONKuDd9rCFBFG9u5tTOWFxx67Vv_yJmQvqHpoHr05mZAynHb8a4MKVgRX2-Fx260tDwIt1wKx4EkZYNVvi_FRKr-59UnCtmunf4P4GpOSGu_GT_A28hu6QR2iVQt_quHDgLfxiO1bxq2SCqfbCq1X1_zjd', start_index=20188)
Annotation(end_index=20206, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAs4xCa3yW4HZVFiq-Y1fFJdQkY34BsIRcjBEp4WC8AANJY7StjgSatAS9-TcO43ntdQ7MOJ9jc5WJeBzrvlxJOL2ZL5G3NxFrwZcWrlb-Hsg2S_vrUijIWPLldOEs9cJrLq37u2Wl7xtqDXTq7wVkERt-GnB4vx0mBU-gx69-6Qy0q2j2te611BkdK_VeFXy87xVF4eHPb6t72NfX1jvwIoYSxD4bIhH6DhEOMYxHvvCWxQbzk2cEqyHuwZQ0ip15FixnfPzgm1o8P0YEt4xuAJvxFhguVGCzO6_bXhXYpXG5dZV6', start_index=20188)
Annotation(end_index=20757, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOk9KB_tMnH_fEHwpCd4_i7LlSoLK1QLlmLptztReDa0Svk_UDUxdeCHUCg_mw0UWvfGcDSPXeFtw6P_G4wYPM0iNnRtBJ-159X8H0LnWv5AYNy2fbihWrxKuqjJW8UgYbJmtibych_73NsrUrEsiyDbK4HpfE4zrexCzt_gHP', start_index=20747)
Annotation(end_index=21033, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGF6iQwKWucOBnqGs2cn5k-s5ycozhYmFeq6JoTu6aHcNKmSZvunuaEZWDCTePcMHhC6F0W2FoElhGH7vm9o_lRhexcZ_inXhX6clIn7dYEIS7wBtAredDlJuGKeM=', start_index=21023)

## Sources
