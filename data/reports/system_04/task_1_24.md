# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 87d9100c | **Time:** 358.47s | **Cost:** $0.74979
--------------------------------------------------------------------------------

# The Efficiency-Tail Risk Trade-off in Value-at-Risk Models: Non-Stationarity, Window Selection, and Estimation Bias

### Key Points
*   **Inherent Trade-off:** Standard Value-at-Risk (VaR) models, particularly Historical Simulation (HS), do not inherently optimize the trade-off between computational efficiency and tail risk capture. Instead, they force a compromise where improving one often degrades the other.
*   **Window Selection Dilemma:** The selection of the historical window length creates a direct conflict between **bias** and **variance**. Short windows reduce bias by capturing recent market regimes (responsiveness) but increase variance due to small sample sizes. Long windows reduce variance but introduce significant bias by including "stale" data that no longer reflects current market dynamics [cite: 1, 2].
*   **Non-Stationarity and Bias:** Financial markets are non-stationary, characterized by changing means, variances, and correlations over time. Applying static window HS to non-stationary data leads to systematic estimation bias, as the model assumes the past distribution is identical to the future distribution [cite: 3, 4, 5].
*   **The "Ghost Effect":** A specific artifact of window-based HS is the "ghost effect," where a significant historical shock causes VaR to spike and remain elevated until the data point exits the window, at which point VaR drops artificially, regardless of the actual current risk environment [cite: 6, 7, 8].
*   **Optimization via Hybrid Models:** Research suggests that **Filtered Historical Simulation (FHS)** offers a superior optimization of this trade-off. By combining GARCH-based volatility filtering (to handle non-stationarity) with bootstrapping of standardized residuals (to capture non-normal tail risks), FHS mitigates the limitations of fixed-window HS [cite: 9, 10, 11].

---

## 1. Introduction

Value at Risk (VaR) remains the cornerstone of financial risk management, serving as the standard metric for quantifying the potential loss in value of a portfolio over a defined period for a given confidence interval. Despite its ubiquity, the calculation of VaR is fraught with a fundamental tension: the trade-off between **efficiency** (computational simplicity and responsiveness to recent data) and **tail risk capture** (the ability to accurately model extreme, rare events).

The user's query posits a critical dichotomy: does the model optimize this trade-off, or does the methodology itself—specifically the selection of the historical simulation window—introduce estimation bias? The weight of academic and empirical evidence suggests the latter. Standard Historical Simulation (HS), the most common method due to its ease of implementation and lack of distributional assumptions, suffers significantly under **non-stationary distributions**.

Financial time series are rarely stationary; they exhibit volatility clustering, structural breaks, and regime shifts [cite: 3, 12]. When a VaR model employs a fixed historical window (e.g., 250 days or 500 days) on non-stationary data, it implicitly assumes that the statistical properties of the past are identical to the immediate future. This assumption fails during regime changes, leading to **estimation bias**. A window that is too long dilutes the signal of rising volatility with calm historical data (underestimation of risk), while a window that is too short lacks sufficient data points to model the tail of the distribution accurately (high variance and instability) [cite: 1, 2].

This report provides an exhaustive analysis of these dynamics. It examines the mechanics of Historical Simulation, the statistical consequences of non-stationarity, the "ghost effects" caused by windowing, and the bias-variance trade-off. Furthermore, it evaluates advanced methodologies, such as Filtered Historical Simulation (FHS) and adaptive window techniques, which attempt to resolve these inherent conflicts.

---

## 2. The Mechanics of Historical Simulation and Window Selection

To understand the estimation bias in VaR, one must first deconstruct the mechanics of the Historical Simulation (HS) approach and the pivotal role of the lookback window.

### 2.1 The Historical Simulation Approach
Historical Simulation is a non-parametric method. Unlike the Variance-Covariance (Parametric) method, which assumes returns follow a specific distribution (typically Normal) and requires the estimation of a covariance matrix, HS relies entirely on empirical data [cite: 1, 13].

The process involves:
1.  Collecting a time series of actual historical returns for the assets in the portfolio over a specific window $N$ (e.g., the last 250 trading days).
2.  Applying these historical returns to the current portfolio weights to simulate a distribution of hypothetical Profit and Loss (P&L).
3.  Sorting the simulated P&L from worst to best.
4.  Identifying the quantile corresponding to the desired confidence level (e.g., the 5th percentile for 95% VaR) [cite: 14, 15].

The primary advantage of HS is its ability to capture **fat tails** (leptokurtosis) and non-linear dependencies (e.g., options) that parametric models often miss, provided these events occurred within the selected window [cite: 9, 16]. It does not assume normality, which is a critical feature given that financial returns are notoriously non-normal [cite: 7, 17].

### 2.2 The Critical Role of Window Size ($N$)
The parameter $N$ (the length of the historical window) is the single most significant variable in the HS methodology. It dictates the "memory" of the model.
*   **Long Windows ($N > 500$ days):** Include more data points, theoretically providing a denser distribution for tail estimation. However, they include distant history that may be irrelevant to current market conditions [cite: 2].
*   **Short Windows ($N < 250$ days):** Highly responsive to recent volatility but suffer from small sample size, making tail estimation statistically fragile. For a 1% VaR using 100 days of data, the estimate relies on a single observation (the worst day), leading to extreme variance [cite: 1].

The selection of $N$ is not merely a calibration detail; it determines the model's sensitivity to **non-stationarity**.

---

## 3. Non-Stationarity and Estimation Bias

The core failure of standard HS lies in its assumption of stationarity. A stochastic process is strictly stationary if its joint probability distribution does not change when shifted in time. However, financial time series are characterized by **non-stationarity**, specifically heteroskedasticity (time-varying variance) and structural breaks [cite: 3, 4].

### 3.1 The Stationarity Assumption vs. Reality
Standard HS weights every observation in the window $N$ equally ($w = 1/N$). This implies that a return observed 200 days ago is just as predictive of tomorrow's risk as a return observed yesterday [cite: 11, 18].
*   **Reality:** Financial markets exhibit "volatility clustering" (large changes tend to be followed by large changes).
*   **Consequence:** In a period of rapidly increasing volatility (e.g., the onset of the 2008 crisis or the COVID-19 pandemic), an HS model with a long window (e.g., 500 days) will be dominated by 480+ days of low-volatility data. The VaR estimate will be biased downward (underestimating risk) because the "stale" low-volatility data dilutes the signal from the recent high-volatility events [cite: 5, 9].

### 3.2 Estimation Bias in Non-Stationary Distributions
Research indicates that ignoring non-stationarity leads to biased estimates and non-normal sampling distributions, rendering standard inferential testing inappropriate [cite: 4].
*   **Downward Bias:** In small samples or during structural breaks where volatility rises, autoregressive processes (common in finance) often yield coefficients that are biased downward. Similarly, HS VaR will systematically lag behind the true risk level during the onset of a crisis [cite: 3, 19].
*   **Unit Roots and Random Walks:** Many financial variables exhibit unit root behavior (random walks), where shocks have permanent effects. Standard HS, by treating history as a mean-reverting or stationary pool of scenarios, fails to capture the "drifting" nature of these risks [cite: 3, 20].

### 3.3 The "Ghost Effect" (Shadow Effect)
A distinct manifestation of estimation bias in window-based HS is the "ghost effect" (also known as the echo effect).
*   **Mechanism:** Suppose a massive market crash occurs on Day $t$. The HS VaR immediately spikes (correctly reflecting higher risk). However, if the window length is $N=250$, exactly 251 days later, this extreme data point drops out of the rolling window.
*   **Artifact:** On Day $t+251$, the VaR will drop precipitously, purely because the data point expired, even if the current market environment remains risky. Conversely, if the market has calmed, the VaR remains artificially high for exactly $N$ days, "ghosting" the past event long after it has become irrelevant [cite: 6, 7, 8].
*   **Implication:** This creates a "sawtooth" pattern in risk estimates that is driven by the window selection rather than actual market dynamics, representing a clear failure to optimize the efficiency-accuracy trade-off [cite: 6].

---

## 4. The Bias-Variance Trade-off in Window Selection

The user's query asks if the model optimizes the trade-off. In statistical terms, this is the **Bias-Variance Trade-off**. Standard HS does not optimize this; it forces the risk manager to choose between high bias or high variance.

### 4.1 Theoretical Framework
*   **Bias:** The error introduced by approximating a real-world problem (which may be complex and time-varying) with a simplified model (which assumes stationarity over window $N$). Long windows have **High Bias** regarding the *current* regime because they average over multiple past regimes [cite: 21, 22].
*   **Variance:** The error introduced by sensitivity to small fluctuations in the training set. Short windows have **High Variance** because the VaR estimate changes drastically with the addition or removal of a single data point [cite: 21, 22].

### 4.2 The Trade-off in VaR Context
*   **Scenario A: Large Window (e.g., 1000 days)**
    *   *Variance:* Low. The estimate is stable day-to-day.
    *   *Bias:* High. It fails to react to structural breaks. In a crisis, it underestimates risk (Type II error). In a recovery, it overestimates risk (Type I error) [cite: 2, 23].
    *   *Tail Capture:* Theoretically better due to more data, but only if the tail events are distributed evenly over time, which they are not [cite: 1].

*   **Scenario B: Small Window (e.g., 100 days)**
    *   *Variance:* High. VaR estimates are volatile and noisy.
    *   *Bias:* Low. The model adapts quickly to new volatility levels.
    *   *Tail Capture:* Poor. With only 100 points, the 99% VaR is essentially the single worst observation. The uncertainty around this quantile estimation is massive [cite: 1].

### 4.3 Failure to Optimize
An "optimized" model would minimize total error (Bias² + Variance). However, fixed-window HS cannot do this because the optimal window length changes dynamically with market conditions.
*   In stable markets, a long window is optimal (low variance, low bias).
*   In transitioning markets, a short window is required to reduce bias.
*   Standard HS uses a static $N$, ensuring it is sub-optimal in at least one of these regimes [cite: 24, 25].

---

## 5. Tail Risk Capture vs. Efficiency

The second part of the user's query concerns the trade-off between efficiency and tail risk capture.

### 5.1 Computational vs. Statistical Efficiency
*   **Computational Efficiency:** HS is extremely efficient computationally. It requires no optimization routines (unlike GARCH) and no matrix inversion (unlike Parametric VaR). It is easy to explain to regulators and boards [cite: 16, 17].
*   **Statistical Efficiency:** HS is statistically *inefficient*. It discards information (all data outside window $N$) and uses the remaining data inefficiently (equal weighting). It requires a larger sample size to achieve the same accuracy as a correctly specified parametric model [cite: 26, 27].

### 5.2 Tail Risk Limitations
While HS is praised for not assuming normality, its ability to capture tail risk is strictly limited by the historical sample.
*   **The "Black Swan" Problem:** If a specific tail event (e.g., a pandemic-induced crash) has not occurred within the window $N$, HS assigns it a probability of zero. It cannot extrapolate beyond the minimum observed return [cite: 1, 16].
*   **Underestimation:** Empirical studies show that HS often underestimates tail risk during periods of high volatility because the window is "polluted" with low-volatility data from the pre-crisis period. For example, during the 2015-2024 NASDAQ analysis, HS showed poor adaptability to unknown extreme events compared to Monte Carlo simulations [cite: 28].
*   **Breach Frequencies:** Backtesting results often reveal that HS models have breach rates (exceptions) that far exceed the theoretical confidence levels (e.g., a 99% VaR breached 3% of the time) during volatile periods, indicating a failure to capture tail risk [cite: 25].

---

## 6. Optimizing the Trade-off: Advanced Approaches

Given that standard HS fails to optimize the trade-off, research points to several modifications that attempt to solve the bias-variance dilemma and the non-stationarity problem.

### 6.1 Weighted Historical Simulation (WHS)
To address the "ghost effect" and the equal-weighting bias, practitioners use Age-Weighted or Volatility-Weighted HS.
*   **Age-Weighting:** Assigns decay factors ($\lambda$) to past observations. Recent data gets higher weight. This reduces the "ghost effect" (data fades out rather than dropping off) and reduces bias toward recent regimes [cite: 7, 8].
*   **Volatility-Weighting:** Rescales historical returns based on current volatility. If current volatility is high, past returns are scaled up. This allows the model to use a long window (reducing variance) while remaining responsive to current conditions (reducing bias) [cite: 8].

### 6.2 Filtered Historical Simulation (FHS)
FHS is widely cited as the method that best optimizes the trade-off between efficiency and tail risk capture.
*   **Methodology:**
    1.  Fit a GARCH model to the historical data to estimate conditional volatility.
    2.  Standardize the historical returns by dividing them by their estimated volatility (creating "residuals"). These residuals are approximately i.i.d. and stationary.
    3.  Bootstrap these residuals to simulate future paths.
    4.  Re-scale the simulated residuals by the *current* forecasted volatility [cite: 9, 11].
*   **Optimization:**
    *   *Handles Non-Stationarity:* The GARCH filter removes the volatility clustering, making the data stationary (solving the bias problem) [cite: 27].
    *   *Captures Tail Risk:* By bootstrapping residuals, it retains the non-normal, fat-tailed nature of the empirical distribution (solving the normality assumption problem) [cite: 10].
    *   *Responsiveness:* Because it uses *current* volatility to re-scale, it reacts immediately to market shocks, avoiding the lag of standard HS [cite: 10, 11].
    *   *Empirical Superiority:* Studies show FHS provides breach rates much closer to theoretical targets (e.g., 4.89% for a 5% target) compared to standard HS (which can have breach rates >40% in crises) [cite: 10, 25].

### 6.3 Adaptive Window Techniques
Emerging research applies signal processing concepts (like Adaptive Short-Time Fourier Transforms) to VaR. These methods dynamically adjust the window length $N$ based on a bias-variance intersection calculation.
*   **Concept:** When the signal is stable, lengthen the window to reduce variance. When a structural break is detected (high bias), shorten the window to adapt [cite: 24, 29, 30].
*   **Application:** While computationally more intensive, adaptive windows explicitly target the optimization of the bias-variance trade-off, unlike fixed-window methods [cite: 31].

---

## 7. Empirical Evidence and Case Studies

### 7.1 The 2008 Financial Crisis
During the 2008 crisis, standard HS models failed catastrophically. Because the preceding years (2003-2007) were characterized by low volatility (the "Great Moderation"), long-window HS models had extremely low VaR estimates. When the crash hit, the "stale" data prevented the VaR from rising fast enough, leading to massive trading losses that exceeded risk limits [cite: 5, 19].

### 7.2 NASDAQ Analysis (2015-2024)
A comparative study of VaR methods on the NASDAQ index over a decade found that while HS is effective in stable periods, its accuracy degrades significantly during volatility. The study concluded that HS relies too heavily on the assumption that "past market behavior reflects future risks," causing poor adaptability to unknown extreme events compared to Monte Carlo or Variance-Covariance methods adjusted for fat tails [cite: 28].

### 7.3 Comparative Breach Analysis
In a rigorous backtest comparing HS, GARCH-Normal, and FHS:
*   **HS:** Showed "densely packed" breach indicators, implying structural failure. It failed to discriminate changing risk dynamics.
*   **FHS:** Yielded breach indicators that were sporadic and clustered only around extreme volatility, aligning with theoretical expectations. It successfully captured the "fat tails" without the lag of HS [cite: 10, 25].

---

## 8. Conclusion

The answer to the user's query is clear: **The standard VaR calculation model, specifically Historical Simulation, does not optimize the trade-off between efficiency and tail risk capture.** Instead, the selection of the historical simulation window leads to significant **estimation bias under non-stationary distributions**.

1.  **Failure of Optimization:** Standard HS forces a choice between the high variance of short windows and the high bias (and lag) of long windows. It lacks a mechanism to dynamically adjust to the non-stationary nature of financial markets.
2.  **Source of Bias:** The bias stems from the implicit assumption of stationarity. By treating old, low-volatility data as equally relevant to current high-volatility regimes, HS systematically underestimates risk during crises and overestimates it during recoveries.
3.  **Ghost Effects:** The fixed window creates artificial drops in risk estimates ("ghost effects") that confuse risk management signals.
4.  **The Solution:** To truly optimize the trade-off, one must move beyond simple HS. **Filtered Historical Simulation (FHS)** represents the most robust solution identified in the literature. It decouples the distributional shape (empirical residuals) from the volatility dynamics (GARCH), allowing for a model that is both highly responsive to non-stationary variance and capable of capturing extreme tail risks.

In summary, while Historical Simulation is computationally efficient, it is statistically flawed for non-stationary data. The window selection process is not an optimization but a rigid constraint that introduces unavoidable estimation errors. True optimization requires hybrid approaches that explicitly model the time-varying nature of market risk.

### References
[cite: 3] Parker, Reed College, "VaR estimation bias non-stationary distributions"
[cite: 4] Tandfonline, "Biased estimates and non-normal sampling distribution"
[cite: 16] Edda, "Understanding Value at Risk (VaR) Models"
[cite: 1] FasterCapital, "Historical Simulation Approach for VaR Estimation"
[cite: 6] Quant StackExchange, "Pros and cons of historical and Gaussian approaches"
[cite: 2] CryptoDataDownload, "Pros & Cons: VaR Lookback Window Length"
[cite: 28] ResearchGate, "Historical Simulation... for Market Risk Assessment From NASDAQ Index"
[cite: 21] Wikipedia, "Bias–variance tradeoff"
[cite: 7] Medium, "Historical Simulation Value-at-Risk Explained"
[cite: 19] Pritsker, "The Hidden Dangers of Historical Simulation"
[cite: 25] ResearchGate, "Comparative Evaluation of VaR Models"
[cite: 9] Stanford, "Filtered historical simulation"
[cite: 10] Arxiv, "Comparative Evaluation of VaR Models: HS, GARCH, FHS"
[cite: 11] Vineetv, "Filtered Historical Simulation (FHS)"
[cite: 8] Midhafin, "Non-parametric Approaches"
[cite: 5] ResearchGate, "The Hidden Dangers of Historical Simulation"
[cite: 25] ResearchGate, "Time Series of VaR Breach Indicators"

**Sources:**
1. [fastercapital.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHM9CG6dVHaGLqIv5GGtS2ybZ_yfouIIY-V9re2aRhMu8CYgaj6O_XncEdEhMGfXbG0cKs52SOJy7_znbBN18b8QJUf-DNGQN5IBa6UoDfvr1gQecuZrH86538g1NAM8tbe7TUnpXjye5R5VhHbD2_-pQom-KNYwe4NlqQkcLIpJTHmFLR8fH9VXxgzMs1c-Q==)
2. [cryptodatadownload.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzvieGvM3Xvc7NE7_sqywZD3tVJ1QF-Gbqf_k_YX4rhELJynC34PkZrNKGALH068mJM9exPHezNuod9KsoM4jdIiY3xYrkd1j3dcf4B9U4T5xbiqWkgeMlJ_YOLbOAB3eQ-OCl5sX-aUNipyNWL2QONs1Hm5mbgbc7TYlJxzFaYoHUF2mBuKBMAw==)
3. [reed.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCAL57RbUWM0MlR3nZ8ShFCa7x1qI9KhH0INheCX0XL4mF-_awaORBTCMrWciPx0uxDy0VbSv1irgvFdJQon1-1rULf7xAQVhW9UX34uw-KrjWlUoAi_zstNRqpCcBXWSrE1ZxXovc9ziES-bR0SdmpT2Ag4M=)
4. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFac01RDXINwG-NenAiRRQQkFjpyv7m3vObbLDUeqRhmxmgfFrdC_iV05ckN-uF3C2xDxWKChvzAJdjeK4PHKvkzaF6J2g9nEpboQzWyQ4nljojyvCa9d-XodCeRmiKga3y2e1xJDLJrNkE9hAShp14OyMdKNpBCnQ=)
5. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1s-4nzVhDXDiZ9d0PmRedHDAr0UuyLyCGzjJyeI5-3gheQuWUlcWgWvy7GeerWA54D3vQpe7BSWSx0nQ_tsDtVkMlXmtwmZQvXYtagI4IFbZDDLiBdQRPI3Vo2NpXBmJeCmaMOMuYlBCNtqJIIsZD6VGTc48WhOOp7Q8lHC-P3jlhjYoiQUQuqx9r8HB1gvTEdc8c)
6. [stackexchange.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwutK40jYn2DtBJtMpn6ZuEe2qeBrX_l0knQb5H9ZonCoz4Yjzcb4z13SzXwIpTfIOC6WYP2fmRhFZSLfD-jktJvynAb3ktYC8mm0KgQGOOq9qBt6g3eAd7oSycRhHgIF9ONkXR5jUq8tff1nSfRguBRAIZwpoKzdnVILyBc4viyykr9mdxdV-PhxDpSTUcNpkrCEJ4xClPJRmgQBFvkm4G_OlLpHGP4tHLahK)
7. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1PZ2DJ4O7KjxjG9BaW8-QUNwMZCCQPNdAJN_JVg7Am5LcOFe9gHNu1xLyrMpSEO_YMliFq09jx9TfPY0nUzr2CkMmQEI3XF6jUzqntj7WqpnmBMASAORjddhi5pcHpJ2PyqhVkb5yWO4gqC_ICXbW7IbYD0wOvaCLyUuqWdOzHGPTtYACdBvGwBPXyxHJwS9zVX6RUhlYCZu3pRNWwmVS)
8. [midhafin.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR0tnEpM-Ogsk-5D1ihaN51qio9gCZgB8Uij11HTp05AVnxrG1_gA61Pqx4LzNlcmJ6ll9Ts7Wee-ZaFd9LjYOz8V3JxgJ6Q85KQ6MdL54q7TJrys2_9jS6ACkSm-rojDe-sAqSsMMnhs0kZmL6Kw=)
9. [stanford.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEUFQXuGdu-gCznckSUTcoLfHapT5BbQlgNi3n37Z-tWmsa0IQ76xUljbM4UB_B6sZ_yjf7Nt32QTgY5sJtbyKPvNMnrP-PxEcKn3UOmb488eDsyGrxb6fiwOM_9JqGi8ewZNNkkPEkppL16YzAJcdE9TQTPbPSqvYo3Yo)
10. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG51wqLTwzrrigi5C3BJZvB7bpuQBsOwa0nR9LoXkEocnBm3hzrAGSlhRBx4LpfJ5Hwg5yraFheCI32FTfbaE-secPX-xrw6UXU8b5MH-AZm7m6qrxdGqoc7A==)
11. [wordpress.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_CQ1wgZ4HvEYJ6kchT4Vp8JJy3JFoqPaeAG-C4AmUe-ciLY2Jy3wcQIoinh6tx2jRM6WnFP43YLAyQ0WYLxodwyn0LOglYfvlTSBs5vq5sCAsHboldSnxA65AZLlshl0vb2k=)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3Ft1KwRH6HPcmsFpUbXDSqeIm52StEZ43VFcMJbugbypwUwusnDHIxePJN3po5WDnoXuJf9usQRgAMu3IhZX_efJCUwueMsVZl8n1TIWt9pbsbJbZU_cYlRsMV82FL6zzvUdu5eKPUDtsc2J5kCm0E-ihV4sWah8PxKw0xjyuISXXwWXCTkAiIPbAqlmajGA6M-CYoVAgIhY4vN1AEzL5n9N6_O0rXrZVkVLnDoqC4YBsn8gSwT6V0oEz0H5KJSQ=)
13. [analystprep.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2lycQRvu4GfXcsyZlpqtRGVIJNDahMj6eZY452QZGU0Z77G8jXRyXCrdxmrF6fajk-vzIG1s-9YCTURfvqx00cpiPurqN-jXbcmA6nPyDt-sCcSJXAgKvgJKAEAuSQ3MZu-Py0WgLV6plH5Hr0RvGtVnoGpcuLGh3n5bsSla4wEB3CZMiAVY86uJtny_r8CseIcSftTxIJ0pd6rHDfhOXP918Lh5ON2QHTOGwZIdunW14A0BQdT8q2_-0ZVKh5dZu7fX-1R66pJKvTqWjIEwkuA00kwqyIQ3pZ0LjO3g=)
14. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGNpHtwqnKnyXyqzfz9uFm0-JmxNo5rOy5bUddPbUxA5aGr2V9SbFpJ5DoS5ruk_uTS8NZc_lTLqJ8OYgRsFqTSPRnIvjj7Z6LA7ATsN2NMXZLLbU0xL7wKklNWo518G2A)
15. [simtrade.fr](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErNx75AXIl-W8xJKY6sszQNdn7LBKL8nZhWA9kU9nLkrRpSZs08d17XSoAI4O97RojNcUWwwjlyyFVYkGuVWUXYBh5Md11MLTeC-1I4G9rph-WYfHb6tNXm28EuBQzL32PPvqbQFEd5WVKv5hhXG3iFCRhyAtzs_GdmDT96_c=)
16. [edda.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQES0RkljYPwaNmI2uPI5PDMOxnE27L8KAOnbSRLBcpTL0CUE_EcHe_-4EdTZ5QZHLbkXn7SXTYvqoS9FdiqMNz77nPCNTvL8NoMi46yqa4zLDp0aLtOSftheFeFebuNsrkuJmb3W9KqjXBc3bsywXhD_-uiVuzr1hEEYH5p4Q==)
17. [analystprep.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKdIhwd1bL4yXfE-RoXwl3n4vI7zeIpkbSCVbaLoIV1fyuwqAQ7lKEXTSM0Ewn5KiWpi2_x1DX1D9exACixfrIHoiG09Q5ihvB7Z84Kdvp46fw6LE2BDP5LROWrSxgYZKz8uRfQ8IwflDQPNLQbFY2XGFK-ZYHi1N2xxak-57YVFYD4ZgqhQjsaimxkN9P3qJWTNnSng==)
18. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEo_JX8R-V6CyibttIW2oLafcvXmQfHLKk_qByV1YxrZxVROp1BLXh2Y_xsN2O_qFEHzmznOWwXnFB3N7W6P4k9Qi1zGSajNb0ZzpZnjkei_AIVP2lQ1whlsUXtyDzNKMc7Q3g27bF0iCfHeMXkDdn2u6ve)
19. [usp.br](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGy7xBhcDC-A_BeHHw_wsuHp7Wcd1ascW9UJqfJ6RpXi78bDDLF3a_LZs6BCwroDW-r2FKrGY4gwWwCQ6nh1zlRneL8BsXulrTuQBc0ETBlugeFYAyGWdEPRLOf8ziEULYFiLCdlRfQQdw=)
20. [stackexchange.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFi4nX7JOQ-y2NbFqiH964q0286Lx42lWo86onRDvoax8EUc6L8ump8rJpJNizxz5Ds4zyI4zt0_43513JCNObZGdbjKotpzTy8-c9wPULVL-QxB_kWFAGVM7V6z3R7VLP-fIi3vNE_hrEWFUaV-LxcibHeXtesSxiogsFkG7PpTHssvTuzg04LT9HmnuMCwElXirnad6zo2m-rkY68hHJQM7aJ2s1CmujoI74yoxVL_Vrd8_OTNmMN)
21. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCUFj3PiK6A9uvnbIBoUAGPpD8ny9KoopOI0DnZEUjpj3WzxxuPPT0vP08MPnd3IARkBHe_Gpw0I2JKayOC-ffkUASKeEZfcNjNrOwW3uhs8JqI8fMQAGXyvAzD2emfEdEXk1JoryMx8M_9pVTMskJdBQ=)
22. [ibm.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDx2n4TnkoVMJW1tvCL5bP-DNyanlPynNqOBdIermFUI8mff7AK25zr-omHASHxsAHcHCFVdW31nV0JNxOTiTxw_ikOdqTyaRcESE0ci_LPIbMTG5h9MFBmCezn4b1d_uT-ivUjppvAsYrPfqA)
23. [cam.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHv4mBcNMPbnHEiRFljuwk16Kk3SzDwIXilwa7PO_QlU2ol76rgM9OVCDtrhAvgyFqcJASrwvd2sLgnGldmOmPrcodT4hyAs_E-lORKq6nfzUumZdvowM0IOQRNgMqN8aJmO2-h0h1ilIbuWv9f6x2rUoqNUGLr3A0v0S88JUjxAMD6v30wDzhdCPO2uSjQlg==)
24. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjTQ4DlntmKl5RhyjmqjDHsLMYGeiXlz2U928B23z5OwxU25tmlFYeIn9LXhpWh5A9m9XOX05ey_CsK1Gp1DnD-WINWBuGXmnCWdKkH3DaDgJtfUM59z4tbK08tVjSp-Tvz1o36vruiBzyaK5xFP7DgrkM9Ajv9ZD303EfV3CdJ_RW3YvrzjKjGwwfHQWZb-p8Ln2OfuWOcqb33gruuND25wJP99XmbsYPsFjvIbaFJW5VX03Fs-qGGCvO_73E)
25. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyLugR-97dGguuyr5DdZyK0b_TtKEiTuyiOQivh0pcCMXeLBUSAcoq92tPCFwV9nhI3Xn4JXdnQOd6-5GlWuzS-BLQYVGKxMhaVsOCJUqFIFRoVYXbJhuG3Zy5oEj3DPZpX_w9RmM0QI2oIYNDH_TzgjI6hmIut4FvWnSgpX262DBOgZGcLmybWk3FjZVJ32b8-fxGw9ZYCa-P5aPrw1Xjkxx6GIp4PSdXAXDVNTUFfNzP5qMVwJo2mCfG7DaJgjOT5b7aeIRJ1aqtox9viJgVpRod7khsKsoRZhjNnKLi)
26. [core.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEf1PTx_XHTHAkl7jR_Iis7tXuOz8ztxNfWpJRCZ56hJxHIIQA5nCNNZOTMyETJjSRN9kRG0AS8Q8wlEhNGtS8M2_WFTSyUzpo5AiPn3dU-kX9fBABLiBNb5NZpfeRikMy2WYI=)
27. [efmaefm.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHirjg39KmtEgXhgN5SJS2n2xRI1e8lvJHJ5DQvTLiDXG0il__hdzR-6x5sYZv7R6TchuMPA0sFmMydtQ96Rj7ieOv2wjQHll7R0oM_ql_dLSpbrOAckeQSQ6Wth84FNWzbGFRA6wssag-406nAf08TA3_URW17-GdlMj0b2GyfyA00HsUfi26s42zXV4ln4Q==)
28. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0q14I7OHoc6J4YzcuMzkVol9j7Ra_dzMQOIfv5XRuAd0AVJQ6XNASwvN9ldx9YhG6YBqQj0svpN7JhiHePPhJDHxtWQByjZtPsBQ4rRpPeVYd14yBQYtr8jc0By0s1tdyfc8cI_bGn-2CPBB9_qtSIcCI1b1o6SRwsaOSmnIEOuYcegnI3oSM4NppOqjDADLMZHEuFw9CEG_N16qmezObLlzJEFOeJhrIC0YnLMqkfAwG939-q_9etYbMaCEe2UGNkC0aGgLFxYpzyR_o4QV61__CHB1DkxynRg8V65k-eRSpwGABJTk08FrYieo=)
29. [ucg.ac.me](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmCk36H7e-qejzl4W2PrvIeMOmof1Z-ztfz5FTx8Uj_IhSj6vgxhJ0q1FrbfHrlk8bdk62SyA27vkIsdsZYuVnqzRc2KUy7HEY2LvyvtiXY4QLboTqy_oneA==)
30. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVH6uYzAyjLcL9f5DRXwUT_0cibbtCbH11j3HMwPKUNCYkZVvsE82jRiMR9a_ceJ0ljk34SvEEW1cuRFvKdm7bmM74y-xSKHYD5QmyLGV78yVYmjUCVQ==)
31. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDsXXmk9yb1gxGqP5bSHVhHEWYPTWe_eQ3Bt2xaSUvFtaHQc7S2tGA-braw41b_iESvAh5H2XpQc4Nvu3f0Y2HpGPY1Q7OsBhBzND_8-IdkVJewDUmUxtrNnK5q4RZ)


## Annotations
Annotation(end_index=830, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzvieGvM3Xvc7NE7_sqywZD3tVJ1QF-Gbqf_k_YX4rhELJynC34PkZrNKGALH068mJM9exPHezNuod9KsoM4jdIiY3xYrkd1j3dcf4B9U4T5xbiqWkgeMlJ_YOLbOAB3eQ-OCl5sX-aUNipyNWL2QONs1Hm5mbgbc7TYlJxzFaYoHUF2mBuKBMAw==', start_index=818)
Annotation(end_index=830, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHM9CG6dVHaGLqIv5GGtS2ybZ_yfouIIY-V9re2aRhMu8CYgaj6O_XncEdEhMGfXbG0cKs52SOJy7_znbBN18b8QJUf-DNGQN5IBa6UoDfvr1gQecuZrH86538g1NAM8tbe7TUnpXjye5R5VhHbD2_-pQom-KNYwe4NlqQkcLIpJTHmFLR8fH9VXxgzMs1c-Q==', start_index=818)
Annotation(end_index=1161, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1s-4nzVhDXDiZ9d0PmRedHDAr0UuyLyCGzjJyeI5-3gheQuWUlcWgWvy7GeerWA54D3vQpe7BSWSx0nQ_tsDtVkMlXmtwmZQvXYtagI4IFbZDDLiBdQRPI3Vo2NpXBmJeCmaMOMuYlBCNtqJIIsZD6VGTc48WhOOp7Q8lHC-P3jlhjYoiQUQuqx9r8HB1gvTEdc8c', start_index=1146)
Annotation(end_index=1161, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCAL57RbUWM0MlR3nZ8ShFCa7x1qI9KhH0INheCX0XL4mF-_awaORBTCMrWciPx0uxDy0VbSv1irgvFdJQon1-1rULf7xAQVhW9UX34uw-KrjWlUoAi_zstNRqpCcBXWSrE1ZxXovc9ziES-bR0SdmpT2Ag4M=', start_index=1146)
Annotation(end_index=1161, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFac01RDXINwG-NenAiRRQQkFjpyv7m3vObbLDUeqRhmxmgfFrdC_iV05ckN-uF3C2xDxWKChvzAJdjeK4PHKvkzaF6J2g9nEpboQzWyQ4nljojyvCa9d-XodCeRmiKga3y2e1xJDLJrNkE9hAShp14OyMdKNpBCnQ=', start_index=1146)
Annotation(end_index=1473, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwutK40jYn2DtBJtMpn6ZuEe2qeBrX_l0knQb5H9ZonCoz4Yjzcb4z13SzXwIpTfIOC6WYP2fmRhFZSLfD-jktJvynAb3ktYC8mm0KgQGOOq9qBt6g3eAd7oSycRhHgIF9ONkXR5jUq8tff1nSfRguBRAIZwpoKzdnVILyBc4viyykr9mdxdV-PhxDpSTUcNpkrCEJ4xClPJRmgQBFvkm4G_OlLpHGP4tHLahK', start_index=1458)
Annotation(end_index=1473, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1PZ2DJ4O7KjxjG9BaW8-QUNwMZCCQPNdAJN_JVg7Am5LcOFe9gHNu1xLyrMpSEO_YMliFq09jx9TfPY0nUzr2CkMmQEI3XF6jUzqntj7WqpnmBMASAORjddhi5pcHpJ2PyqhVkb5yWO4gqC_ICXbW7IbYD0wOvaCLyUuqWdOzHGPTtYACdBvGwBPXyxHJwS9zVX6RUhlYCZu3pRNWwmVS', start_index=1458)
Annotation(end_index=1473, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR0tnEpM-Ogsk-5D1ihaN51qio9gCZgB8Uij11HTp05AVnxrG1_gA61Pqx4LzNlcmJ6ll9Ts7Wee-ZaFd9LjYOz8V3JxgJ6Q85KQ6MdL54q7TJrys2_9jS6ACkSm-rojDe-sAqSsMMnhs0kZmL6Kw=', start_index=1458)
Annotation(end_index=1851, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEUFQXuGdu-gCznckSUTcoLfHapT5BbQlgNi3n37Z-tWmsa0IQ76xUljbM4UB_B6sZ_yjf7Nt32QTgY5sJtbyKPvNMnrP-PxEcKn3UOmb488eDsyGrxb6fiwOM_9JqGi8ewZNNkkPEkppL16YzAJcdE9TQTPbPSqvYo3Yo', start_index=1834)
Annotation(end_index=1851, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_CQ1wgZ4HvEYJ6kchT4Vp8JJy3JFoqPaeAG-C4AmUe-ciLY2Jy3wcQIoinh6tx2jRM6WnFP43YLAyQ0WYLxodwyn0LOglYfvlTSBs5vq5sCAsHboldSnxA65AZLlshl0vb2k=', start_index=1834)
Annotation(end_index=1851, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG51wqLTwzrrigi5C3BJZvB7bpuQBsOwa0nR9LoXkEocnBm3hzrAGSlhRBx4LpfJ5Hwg5yraFheCI32FTfbaE-secPX-xrw6UXU8b5MH-AZm7m6qrxdGqoc7A==', start_index=1834)
Annotation(end_index=2969, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3Ft1KwRH6HPcmsFpUbXDSqeIm52StEZ43VFcMJbugbypwUwusnDHIxePJN3po5WDnoXuJf9usQRgAMu3IhZX_efJCUwueMsVZl8n1TIWt9pbsbJbZU_cYlRsMV82FL6zzvUdu5eKPUDtsc2J5kCm0E-ihV4sWah8PxKw0xjyuISXXwWXCTkAiIPbAqlmajGA6M-CYoVAgIhY4vN1AEzL5n9N6_O0rXrZVkVLnDoqC4YBsn8gSwT6V0oEz0H5KJSQ=', start_index=2956)
Annotation(end_index=2969, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCAL57RbUWM0MlR3nZ8ShFCa7x1qI9KhH0INheCX0XL4mF-_awaORBTCMrWciPx0uxDy0VbSv1irgvFdJQon1-1rULf7xAQVhW9UX34uw-KrjWlUoAi_zstNRqpCcBXWSrE1ZxXovc9ziES-bR0SdmpT2Ag4M=', start_index=2956)
Annotation(end_index=3531, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzvieGvM3Xvc7NE7_sqywZD3tVJ1QF-Gbqf_k_YX4rhELJynC34PkZrNKGALH068mJM9exPHezNuod9KsoM4jdIiY3xYrkd1j3dcf4B9U4T5xbiqWkgeMlJ_YOLbOAB3eQ-OCl5sX-aUNipyNWL2QONs1Hm5mbgbc7TYlJxzFaYoHUF2mBuKBMAw==', start_index=3519)
Annotation(end_index=3531, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHM9CG6dVHaGLqIv5GGtS2ybZ_yfouIIY-V9re2aRhMu8CYgaj6O_XncEdEhMGfXbG0cKs52SOJy7_znbBN18b8QJUf-DNGQN5IBa6UoDfvr1gQecuZrH86538g1NAM8tbe7TUnpXjye5R5VhHbD2_-pQom-KNYwe4NlqQkcLIpJTHmFLR8fH9VXxgzMs1c-Q==', start_index=3519)
Annotation(end_index=4515, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2lycQRvu4GfXcsyZlpqtRGVIJNDahMj6eZY452QZGU0Z77G8jXRyXCrdxmrF6fajk-vzIG1s-9YCTURfvqx00cpiPurqN-jXbcmA6nPyDt-sCcSJXAgKvgJKAEAuSQ3MZu-Py0WgLV6plH5Hr0RvGtVnoGpcuLGh3n5bsSla4wEB3CZMiAVY86uJtny_r8CseIcSftTxIJ0pd6rHDfhOXP918Lh5ON2QHTOGwZIdunW14A0BQdT8q2_-0ZVKh5dZu7fX-1R66pJKvTqWjIEwkuA00kwqyIQ3pZ0LjO3g=', start_index=4502)
Annotation(end_index=4515, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHM9CG6dVHaGLqIv5GGtS2ybZ_yfouIIY-V9re2aRhMu8CYgaj6O_XncEdEhMGfXbG0cKs52SOJy7_znbBN18b8QJUf-DNGQN5IBa6UoDfvr1gQecuZrH86538g1NAM8tbe7TUnpXjye5R5VhHbD2_-pQom-KNYwe4NlqQkcLIpJTHmFLR8fH9VXxgzMs1c-Q==', start_index=4502)
Annotation(end_index=5007, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErNx75AXIl-W8xJKY6sszQNdn7LBKL8nZhWA9kU9nLkrRpSZs08d17XSoAI4O97RojNcUWwwjlyyFVYkGuVWUXYBh5Md11MLTeC-1I4G9rph-WYfHb6tNXm28EuBQzL32PPvqbQFEd5WVKv5hhXG3iFCRhyAtzs_GdmDT96_c=', start_index=4993)
Annotation(end_index=5007, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGNpHtwqnKnyXyqzfz9uFm0-JmxNo5rOy5bUddPbUxA5aGr2V9SbFpJ5DoS5ruk_uTS8NZc_lTLqJ8OYgRsFqTSPRnIvjj7Z6LA7ATsN2NMXZLLbU0xL7wKklNWo518G2A', start_index=4993)
Annotation(end_index=5244, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQES0RkljYPwaNmI2uPI5PDMOxnE27L8KAOnbSRLBcpTL0CUE_EcHe_-4EdTZ5QZHLbkXn7SXTYvqoS9FdiqMNz77nPCNTvL8NoMi46yqa4zLDp0aLtOSftheFeFebuNsrkuJmb3W9KqjXBc3bsywXhD_-uiVuzr1hEEYH5p4Q==', start_index=5231)
Annotation(end_index=5244, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEUFQXuGdu-gCznckSUTcoLfHapT5BbQlgNi3n37Z-tWmsa0IQ76xUljbM4UB_B6sZ_yjf7Nt32QTgY5sJtbyKPvNMnrP-PxEcKn3UOmb488eDsyGrxb6fiwOM_9JqGi8ewZNNkkPEkppL16YzAJcdE9TQTPbPSqvYo3Yo', start_index=5231)
Annotation(end_index=5373, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1PZ2DJ4O7KjxjG9BaW8-QUNwMZCCQPNdAJN_JVg7Am5LcOFe9gHNu1xLyrMpSEO_YMliFq09jx9TfPY0nUzr2CkMmQEI3XF6jUzqntj7WqpnmBMASAORjddhi5pcHpJ2PyqhVkb5yWO4gqC_ICXbW7IbYD0wOvaCLyUuqWdOzHGPTtYACdBvGwBPXyxHJwS9zVX6RUhlYCZu3pRNWwmVS', start_index=5360)
Annotation(end_index=5373, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKdIhwd1bL4yXfE-RoXwl3n4vI7zeIpkbSCVbaLoIV1fyuwqAQ7lKEXTSM0Ewn5KiWpi2_x1DX1D9exACixfrIHoiG09Q5ihvB7Z84Kdvp46fw6LE2BDP5LROWrSxgYZKz8uRfQ8IwflDQPNLQbFY2XGFK-ZYHi1N2xxak-57YVFYD4ZgqhQjsaimxkN9P3qJWTNnSng==', start_index=5360)
Annotation(end_index=5812, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzvieGvM3Xvc7NE7_sqywZD3tVJ1QF-Gbqf_k_YX4rhELJynC34PkZrNKGALH068mJM9exPHezNuod9KsoM4jdIiY3xYrkd1j3dcf4B9U4T5xbiqWkgeMlJ_YOLbOAB3eQ-OCl5sX-aUNipyNWL2QONs1Hm5mbgbc7TYlJxzFaYoHUF2mBuKBMAw==', start_index=5803)
Annotation(end_index=6109, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHM9CG6dVHaGLqIv5GGtS2ybZ_yfouIIY-V9re2aRhMu8CYgaj6O_XncEdEhMGfXbG0cKs52SOJy7_znbBN18b8QJUf-DNGQN5IBa6UoDfvr1gQecuZrH86538g1NAM8tbe7TUnpXjye5R5VhHbD2_-pQom-KNYwe4NlqQkcLIpJTHmFLR8fH9VXxgzMs1c-Q==', start_index=6100)
Annotation(end_index=6638, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCAL57RbUWM0MlR3nZ8ShFCa7x1qI9KhH0INheCX0XL4mF-_awaORBTCMrWciPx0uxDy0VbSv1irgvFdJQon1-1rULf7xAQVhW9UX34uw-KrjWlUoAi_zstNRqpCcBXWSrE1ZxXovc9ziES-bR0SdmpT2Ag4M=', start_index=6626)
Annotation(end_index=6638, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFac01RDXINwG-NenAiRRQQkFjpyv7m3vObbLDUeqRhmxmgfFrdC_iV05ckN-uF3C2xDxWKChvzAJdjeK4PHKvkzaF6J2g9nEpboQzWyQ4nljojyvCa9d-XodCeRmiKga3y2e1xJDLJrNkE9hAShp14OyMdKNpBCnQ=', start_index=6626)
Annotation(end_index=6901, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEo_JX8R-V6CyibttIW2oLafcvXmQfHLKk_qByV1YxrZxVROp1BLXh2Y_xsN2O_qFEHzmznOWwXnFB3N7W6P4k9Qi1zGSajNb0ZzpZnjkei_AIVP2lQ1whlsUXtyDzNKMc7Q3g27bF0iCfHeMXkDdn2u6ve', start_index=6887)
Annotation(end_index=6901, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_CQ1wgZ4HvEYJ6kchT4Vp8JJy3JFoqPaeAG-C4AmUe-ciLY2Jy3wcQIoinh6tx2jRM6WnFP43YLAyQ0WYLxodwyn0LOglYfvlTSBs5vq5sCAsHboldSnxA65AZLlshl0vb2k=', start_index=6887)
Annotation(end_index=7430, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1s-4nzVhDXDiZ9d0PmRedHDAr0UuyLyCGzjJyeI5-3gheQuWUlcWgWvy7GeerWA54D3vQpe7BSWSx0nQ_tsDtVkMlXmtwmZQvXYtagI4IFbZDDLiBdQRPI3Vo2NpXBmJeCmaMOMuYlBCNtqJIIsZD6VGTc48WhOOp7Q8lHC-P3jlhjYoiQUQuqx9r8HB1gvTEdc8c', start_index=7418)
Annotation(end_index=7430, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEUFQXuGdu-gCznckSUTcoLfHapT5BbQlgNi3n37Z-tWmsa0IQ76xUljbM4UB_B6sZ_yjf7Nt32QTgY5sJtbyKPvNMnrP-PxEcKn3UOmb488eDsyGrxb6fiwOM_9JqGi8ewZNNkkPEkppL16YzAJcdE9TQTPbPSqvYo3Yo', start_index=7418)
Annotation(end_index=7666, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFac01RDXINwG-NenAiRRQQkFjpyv7m3vObbLDUeqRhmxmgfFrdC_iV05ckN-uF3C2xDxWKChvzAJdjeK4PHKvkzaF6J2g9nEpboQzWyQ4nljojyvCa9d-XodCeRmiKga3y2e1xJDLJrNkE9hAShp14OyMdKNpBCnQ=', start_index=7657)
Annotation(end_index=7967, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCAL57RbUWM0MlR3nZ8ShFCa7x1qI9KhH0INheCX0XL4mF-_awaORBTCMrWciPx0uxDy0VbSv1irgvFdJQon1-1rULf7xAQVhW9UX34uw-KrjWlUoAi_zstNRqpCcBXWSrE1ZxXovc9ziES-bR0SdmpT2Ag4M=', start_index=7954)
Annotation(end_index=7967, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGy7xBhcDC-A_BeHHw_wsuHp7Wcd1ascW9UJqfJ6RpXi78bDDLF3a_LZs6BCwroDW-r2FKrGY4gwWwCQ6nh1zlRneL8BsXulrTuQBc0ETBlugeFYAyGWdEPRLOf8ziEULYFiLCdlRfQQdw=', start_index=7954)
Annotation(end_index=8264, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCAL57RbUWM0MlR3nZ8ShFCa7x1qI9KhH0INheCX0XL4mF-_awaORBTCMrWciPx0uxDy0VbSv1irgvFdJQon1-1rULf7xAQVhW9UX34uw-KrjWlUoAi_zstNRqpCcBXWSrE1ZxXovc9ziES-bR0SdmpT2Ag4M=', start_index=8251)
Annotation(end_index=8264, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFi4nX7JOQ-y2NbFqiH964q0286Lx42lWo86onRDvoax8EUc6L8ump8rJpJNizxz5Ds4zyI4zt0_43513JCNObZGdbjKotpzTy8-c9wPULVL-QxB_kWFAGVM7V6z3R7VLP-fIi3vNE_hrEWFUaV-LxcibHeXtesSxiogsFkG7PpTHssvTuzg04LT9HmnuMCwElXirnad6zo2m-rkY68hHJQM7aJ2s1CmujoI74yoxVL_Vrd8_OTNmMN', start_index=8251)
Annotation(end_index=9017, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwutK40jYn2DtBJtMpn6ZuEe2qeBrX_l0knQb5H9ZonCoz4Yjzcb4z13SzXwIpTfIOC6WYP2fmRhFZSLfD-jktJvynAb3ktYC8mm0KgQGOOq9qBt6g3eAd7oSycRhHgIF9ONkXR5jUq8tff1nSfRguBRAIZwpoKzdnVILyBc4viyykr9mdxdV-PhxDpSTUcNpkrCEJ4xClPJRmgQBFvkm4G_OlLpHGP4tHLahK', start_index=9002)
Annotation(end_index=9017, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1PZ2DJ4O7KjxjG9BaW8-QUNwMZCCQPNdAJN_JVg7Am5LcOFe9gHNu1xLyrMpSEO_YMliFq09jx9TfPY0nUzr2CkMmQEI3XF6jUzqntj7WqpnmBMASAORjddhi5pcHpJ2PyqhVkb5yWO4gqC_ICXbW7IbYD0wOvaCLyUuqWdOzHGPTtYACdBvGwBPXyxHJwS9zVX6RUhlYCZu3pRNWwmVS', start_index=9002)
Annotation(end_index=9017, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR0tnEpM-Ogsk-5D1ihaN51qio9gCZgB8Uij11HTp05AVnxrG1_gA61Pqx4LzNlcmJ6ll9Ts7Wee-ZaFd9LjYOz8V3JxgJ6Q85KQ6MdL54q7TJrys2_9jS6ACkSm-rojDe-sAqSsMMnhs0kZmL6Kw=', start_index=9002)
Annotation(end_index=9251, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwutK40jYn2DtBJtMpn6ZuEe2qeBrX_l0knQb5H9ZonCoz4Yjzcb4z13SzXwIpTfIOC6WYP2fmRhFZSLfD-jktJvynAb3ktYC8mm0KgQGOOq9qBt6g3eAd7oSycRhHgIF9ONkXR5jUq8tff1nSfRguBRAIZwpoKzdnVILyBc4viyykr9mdxdV-PhxDpSTUcNpkrCEJ4xClPJRmgQBFvkm4G_OlLpHGP4tHLahK', start_index=9242)
Annotation(end_index=9885, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDx2n4TnkoVMJW1tvCL5bP-DNyanlPynNqOBdIermFUI8mff7AK25zr-omHASHxsAHcHCFVdW31nV0JNxOTiTxw_ikOdqTyaRcESE0ci_LPIbMTG5h9MFBmCezn4b1d_uT-ivUjppvAsYrPfqA', start_index=9871)
Annotation(end_index=9885, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCUFj3PiK6A9uvnbIBoUAGPpD8ny9KoopOI0DnZEUjpj3WzxxuPPT0vP08MPnd3IARkBHe_Gpw0I2JKayOC-ffkUASKeEZfcNjNrOwW3uhs8JqI8fMQAGXyvAzD2emfEdEXk1JoryMx8M_9pVTMskJdBQ=', start_index=9871)
Annotation(end_index=10132, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDx2n4TnkoVMJW1tvCL5bP-DNyanlPynNqOBdIermFUI8mff7AK25zr-omHASHxsAHcHCFVdW31nV0JNxOTiTxw_ikOdqTyaRcESE0ci_LPIbMTG5h9MFBmCezn4b1d_uT-ivUjppvAsYrPfqA', start_index=10118)
Annotation(end_index=10132, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCUFj3PiK6A9uvnbIBoUAGPpD8ny9KoopOI0DnZEUjpj3WzxxuPPT0vP08MPnd3IARkBHe_Gpw0I2JKayOC-ffkUASKeEZfcNjNrOwW3uhs8JqI8fMQAGXyvAzD2emfEdEXk1JoryMx8M_9pVTMskJdBQ=', start_index=10118)
Annotation(end_index=10463, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzvieGvM3Xvc7NE7_sqywZD3tVJ1QF-Gbqf_k_YX4rhELJynC34PkZrNKGALH068mJM9exPHezNuod9KsoM4jdIiY3xYrkd1j3dcf4B9U4T5xbiqWkgeMlJ_YOLbOAB3eQ-OCl5sX-aUNipyNWL2QONs1Hm5mbgbc7TYlJxzFaYoHUF2mBuKBMAw==', start_index=10450)
Annotation(end_index=10463, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHv4mBcNMPbnHEiRFljuwk16Kk3SzDwIXilwa7PO_QlU2ol76rgM9OVCDtrhAvgyFqcJASrwvd2sLgnGldmOmPrcodT4hyAs_E-lORKq6nfzUumZdvowM0IOQRNgMqN8aJmO2-h0h1ilIbuWv9f6x2rUoqNUGLr3A0v0S88JUjxAMD6v30wDzhdCPO2uSjQlg==', start_index=10450)
Annotation(end_index=10618, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHM9CG6dVHaGLqIv5GGtS2ybZ_yfouIIY-V9re2aRhMu8CYgaj6O_XncEdEhMGfXbG0cKs52SOJy7_znbBN18b8QJUf-DNGQN5IBa6UoDfvr1gQecuZrH86538g1NAM8tbe7TUnpXjye5R5VhHbD2_-pQom-KNYwe4NlqQkcLIpJTHmFLR8fH9VXxgzMs1c-Q==', start_index=10609)
Annotation(end_index=10984, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHM9CG6dVHaGLqIv5GGtS2ybZ_yfouIIY-V9re2aRhMu8CYgaj6O_XncEdEhMGfXbG0cKs52SOJy7_znbBN18b8QJUf-DNGQN5IBa6UoDfvr1gQecuZrH86538g1NAM8tbe7TUnpXjye5R5VhHbD2_-pQom-KNYwe4NlqQkcLIpJTHmFLR8fH9VXxgzMs1c-Q==', start_index=10975)
Annotation(end_index=11458, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjTQ4DlntmKl5RhyjmqjDHsLMYGeiXlz2U928B23z5OwxU25tmlFYeIn9LXhpWh5A9m9XOX05ey_CsK1Gp1DnD-WINWBuGXmnCWdKkH3DaDgJtfUM59z4tbK08tVjSp-Tvz1o36vruiBzyaK5xFP7DgrkM9Ajv9ZD303EfV3CdJ_RW3YvrzjKjGwwfHQWZb-p8Ln2OfuWOcqb33gruuND25wJP99XmbsYPsFjvIbaFJW5VX03Fs-qGGCvO_73E', start_index=11444)
Annotation(end_index=11458, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyLugR-97dGguuyr5DdZyK0b_TtKEiTuyiOQivh0pcCMXeLBUSAcoq92tPCFwV9nhI3Xn4JXdnQOd6-5GlWuzS-BLQYVGKxMhaVsOCJUqFIFRoVYXbJhuG3Zy5oEj3DPZpX_w9RmM0QI2oIYNDH_TzgjI6hmIut4FvWnSgpX262DBOgZGcLmybWk3FjZVJ32b8-fxGw9ZYCa-P5aPrw1Xjkxx6GIp4PSdXAXDVNTUFfNzP5qMVwJo2mCfG7DaJgjOT5b7aeIRJ1aqtox9viJgVpRod7khsKsoRZhjNnKLi', start_index=11444)
Annotation(end_index=11896, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQES0RkljYPwaNmI2uPI5PDMOxnE27L8KAOnbSRLBcpTL0CUE_EcHe_-4EdTZ5QZHLbkXn7SXTYvqoS9FdiqMNz77nPCNTvL8NoMi46yqa4zLDp0aLtOSftheFeFebuNsrkuJmb3W9KqjXBc3bsywXhD_-uiVuzr1hEEYH5p4Q==', start_index=11882)
Annotation(end_index=11896, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKdIhwd1bL4yXfE-RoXwl3n4vI7zeIpkbSCVbaLoIV1fyuwqAQ7lKEXTSM0Ewn5KiWpi2_x1DX1D9exACixfrIHoiG09Q5ihvB7Z84Kdvp46fw6LE2BDP5LROWrSxgYZKz8uRfQ8IwflDQPNLQbFY2XGFK-ZYHi1N2xxak-57YVFYD4ZgqhQjsaimxkN9P3qJWTNnSng==', start_index=11882)
Annotation(end_index=12198, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEf1PTx_XHTHAkl7jR_Iis7tXuOz8ztxNfWpJRCZ56hJxHIIQA5nCNNZOTMyETJjSRN9kRG0AS8Q8wlEhNGtS8M2_WFTSyUzpo5AiPn3dU-kX9fBABLiBNb5NZpfeRikMy2WYI=', start_index=12184)
Annotation(end_index=12198, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHirjg39KmtEgXhgN5SJS2n2xRI1e8lvJHJ5DQvTLiDXG0il__hdzR-6x5sYZv7R6TchuMPA0sFmMydtQ96Rj7ieOv2wjQHll7R0oM_ql_dLSpbrOAckeQSQ6Wth84FNWzbGFRA6wssag-406nAf08TA3_URW17-GdlMj0b2GyfyA00HsUfi26s42zXV4ln4Q==', start_index=12184)
Annotation(end_index=12597, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQES0RkljYPwaNmI2uPI5PDMOxnE27L8KAOnbSRLBcpTL0CUE_EcHe_-4EdTZ5QZHLbkXn7SXTYvqoS9FdiqMNz77nPCNTvL8NoMi46yqa4zLDp0aLtOSftheFeFebuNsrkuJmb3W9KqjXBc3bsywXhD_-uiVuzr1hEEYH5p4Q==', start_index=12584)
Annotation(end_index=12597, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHM9CG6dVHaGLqIv5GGtS2ybZ_yfouIIY-V9re2aRhMu8CYgaj6O_XncEdEhMGfXbG0cKs52SOJy7_znbBN18b8QJUf-DNGQN5IBa6UoDfvr1gQecuZrH86538g1NAM8tbe7TUnpXjye5R5VhHbD2_-pQom-KNYwe4NlqQkcLIpJTHmFLR8fH9VXxgzMs1c-Q==', start_index=12584)
Annotation(end_index=12957, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0q14I7OHoc6J4YzcuMzkVol9j7Ra_dzMQOIfv5XRuAd0AVJQ6XNASwvN9ldx9YhG6YBqQj0svpN7JhiHePPhJDHxtWQByjZtPsBQ4rRpPeVYd14yBQYtr8jc0By0s1tdyfc8cI_bGn-2CPBB9_qtSIcCI1b1o6SRwsaOSmnIEOuYcegnI3oSM4NppOqjDADLMZHEuFw9CEG_N16qmezObLlzJEFOeJhrIC0YnLMqkfAwG939-q_9etYbMaCEe2UGNkC0aGgLFxYpzyR_o4QV61__CHB1DkxynRg8V65k-eRSpwGABJTk08FrYieo=', start_index=12947)
Annotation(end_index=13235, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyLugR-97dGguuyr5DdZyK0b_TtKEiTuyiOQivh0pcCMXeLBUSAcoq92tPCFwV9nhI3Xn4JXdnQOd6-5GlWuzS-BLQYVGKxMhaVsOCJUqFIFRoVYXbJhuG3Zy5oEj3DPZpX_w9RmM0QI2oIYNDH_TzgjI6hmIut4FvWnSgpX262DBOgZGcLmybWk3FjZVJ32b8-fxGw9ZYCa-P5aPrw1Xjkxx6GIp4PSdXAXDVNTUFfNzP5qMVwJo2mCfG7DaJgjOT5b7aeIRJ1aqtox9viJgVpRod7khsKsoRZhjNnKLi', start_index=13225)
Annotation(end_index=13875, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1PZ2DJ4O7KjxjG9BaW8-QUNwMZCCQPNdAJN_JVg7Am5LcOFe9gHNu1xLyrMpSEO_YMliFq09jx9TfPY0nUzr2CkMmQEI3XF6jUzqntj7WqpnmBMASAORjddhi5pcHpJ2PyqhVkb5yWO4gqC_ICXbW7IbYD0wOvaCLyUuqWdOzHGPTtYACdBvGwBPXyxHJwS9zVX6RUhlYCZu3pRNWwmVS', start_index=13863)
Annotation(end_index=13875, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR0tnEpM-Ogsk-5D1ihaN51qio9gCZgB8Uij11HTp05AVnxrG1_gA61Pqx4LzNlcmJ6ll9Ts7Wee-ZaFd9LjYOz8V3JxgJ6Q85KQ6MdL54q7TJrys2_9jS6ACkSm-rojDe-sAqSsMMnhs0kZmL6Kw=', start_index=13863)
Annotation(end_index=14160, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR0tnEpM-Ogsk-5D1ihaN51qio9gCZgB8Uij11HTp05AVnxrG1_gA61Pqx4LzNlcmJ6ll9Ts7Wee-ZaFd9LjYOz8V3JxgJ6Q85KQ6MdL54q7TJrys2_9jS6ACkSm-rojDe-sAqSsMMnhs0kZmL6Kw=', start_index=14151)
Annotation(end_index=14748, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEUFQXuGdu-gCznckSUTcoLfHapT5BbQlgNi3n37Z-tWmsa0IQ76xUljbM4UB_B6sZ_yjf7Nt32QTgY5sJtbyKPvNMnrP-PxEcKn3UOmb488eDsyGrxb6fiwOM_9JqGi8ewZNNkkPEkppL16YzAJcdE9TQTPbPSqvYo3Yo', start_index=14735)
Annotation(end_index=14748, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_CQ1wgZ4HvEYJ6kchT4Vp8JJy3JFoqPaeAG-C4AmUe-ciLY2Jy3wcQIoinh6tx2jRM6WnFP43YLAyQ0WYLxodwyn0LOglYfvlTSBs5vq5sCAsHboldSnxA65AZLlshl0vb2k=', start_index=14735)
Annotation(end_index=14924, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHirjg39KmtEgXhgN5SJS2n2xRI1e8lvJHJ5DQvTLiDXG0il__hdzR-6x5sYZv7R6TchuMPA0sFmMydtQ96Rj7ieOv2wjQHll7R0oM_ql_dLSpbrOAckeQSQ6Wth84FNWzbGFRA6wssag-406nAf08TA3_URW17-GdlMj0b2GyfyA00HsUfi26s42zXV4ln4Q==', start_index=14914)
Annotation(end_index=15112, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG51wqLTwzrrigi5C3BJZvB7bpuQBsOwa0nR9LoXkEocnBm3hzrAGSlhRBx4LpfJ5Hwg5yraFheCI32FTfbaE-secPX-xrw6UXU8b5MH-AZm7m6qrxdGqoc7A==', start_index=15102)
Annotation(end_index=15276, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_CQ1wgZ4HvEYJ6kchT4Vp8JJy3JFoqPaeAG-C4AmUe-ciLY2Jy3wcQIoinh6tx2jRM6WnFP43YLAyQ0WYLxodwyn0LOglYfvlTSBs5vq5sCAsHboldSnxA65AZLlshl0vb2k=', start_index=15262)
Annotation(end_index=15276, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG51wqLTwzrrigi5C3BJZvB7bpuQBsOwa0nR9LoXkEocnBm3hzrAGSlhRBx4LpfJ5Hwg5yraFheCI32FTfbaE-secPX-xrw6UXU8b5MH-AZm7m6qrxdGqoc7A==', start_index=15262)
Annotation(end_index=15498, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG51wqLTwzrrigi5C3BJZvB7bpuQBsOwa0nR9LoXkEocnBm3hzrAGSlhRBx4LpfJ5Hwg5yraFheCI32FTfbaE-secPX-xrw6UXU8b5MH-AZm7m6qrxdGqoc7A==', start_index=15484)
Annotation(end_index=15498, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyLugR-97dGguuyr5DdZyK0b_TtKEiTuyiOQivh0pcCMXeLBUSAcoq92tPCFwV9nhI3Xn4JXdnQOd6-5GlWuzS-BLQYVGKxMhaVsOCJUqFIFRoVYXbJhuG3Zy5oEj3DPZpX_w9RmM0QI2oIYNDH_TzgjI6hmIut4FvWnSgpX262DBOgZGcLmybWk3FjZVJ32b8-fxGw9ZYCa-P5aPrw1Xjkxx6GIp4PSdXAXDVNTUFfNzP5qMVwJo2mCfG7DaJgjOT5b7aeIRJ1aqtox9viJgVpRod7khsKsoRZhjNnKLi', start_index=15484)
Annotation(end_index=15928, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmCk36H7e-qejzl4W2PrvIeMOmof1Z-ztfz5FTx8Uj_IhSj6vgxhJ0q1FrbfHrlk8bdk62SyA27vkIsdsZYuVnqzRc2KUy7HEY2LvyvtiXY4QLboTqy_oneA==', start_index=15910)
Annotation(end_index=15928, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjTQ4DlntmKl5RhyjmqjDHsLMYGeiXlz2U928B23z5OwxU25tmlFYeIn9LXhpWh5A9m9XOX05ey_CsK1Gp1DnD-WINWBuGXmnCWdKkH3DaDgJtfUM59z4tbK08tVjSp-Tvz1o36vruiBzyaK5xFP7DgrkM9Ajv9ZD303EfV3CdJ_RW3YvrzjKjGwwfHQWZb-p8Ln2OfuWOcqb33gruuND25wJP99XmbsYPsFjvIbaFJW5VX03Fs-qGGCvO_73E', start_index=15910)
Annotation(end_index=15928, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVH6uYzAyjLcL9f5DRXwUT_0cibbtCbH11j3HMwPKUNCYkZVvsE82jRiMR9a_ceJ0ljk34SvEEW1cuRFvKdm7bmM74y-xSKHYD5QmyLGV78yVYmjUCVQ==', start_index=15910)
Annotation(end_index=16111, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDsXXmk9yb1gxGqP5bSHVhHEWYPTWe_eQ3Bt2xaSUvFtaHQc7S2tGA-braw41b_iESvAh5H2XpQc4Nvu3f0Y2HpGPY1Q7OsBhBzND_8-IdkVJewDUmUxtrNnK5q4RZ', start_index=16101)
Annotation(end_index=16575, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1s-4nzVhDXDiZ9d0PmRedHDAr0UuyLyCGzjJyeI5-3gheQuWUlcWgWvy7GeerWA54D3vQpe7BSWSx0nQ_tsDtVkMlXmtwmZQvXYtagI4IFbZDDLiBdQRPI3Vo2NpXBmJeCmaMOMuYlBCNtqJIIsZD6VGTc48WhOOp7Q8lHC-P3jlhjYoiQUQuqx9r8HB1gvTEdc8c', start_index=16562)
Annotation(end_index=16575, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGy7xBhcDC-A_BeHHw_wsuHp7Wcd1ascW9UJqfJ6RpXi78bDDLF3a_LZs6BCwroDW-r2FKrGY4gwWwCQ6nh1zlRneL8BsXulrTuQBc0ETBlugeFYAyGWdEPRLOf8ziEULYFiLCdlRfQQdw=', start_index=16562)
Annotation(end_index=17046, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0q14I7OHoc6J4YzcuMzkVol9j7Ra_dzMQOIfv5XRuAd0AVJQ6XNASwvN9ldx9YhG6YBqQj0svpN7JhiHePPhJDHxtWQByjZtPsBQ4rRpPeVYd14yBQYtr8jc0By0s1tdyfc8cI_bGn-2CPBB9_qtSIcCI1b1o6SRwsaOSmnIEOuYcegnI3oSM4NppOqjDADLMZHEuFw9CEG_N16qmezObLlzJEFOeJhrIC0YnLMqkfAwG939-q_9etYbMaCEe2UGNkC0aGgLFxYpzyR_o4QV61__CHB1DkxynRg8V65k-eRSpwGABJTk08FrYieo=', start_index=17036)
Annotation(end_index=17500, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG51wqLTwzrrigi5C3BJZvB7bpuQBsOwa0nR9LoXkEocnBm3hzrAGSlhRBx4LpfJ5Hwg5yraFheCI32FTfbaE-secPX-xrw6UXU8b5MH-AZm7m6qrxdGqoc7A==', start_index=17486)
Annotation(end_index=17500, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyLugR-97dGguuyr5DdZyK0b_TtKEiTuyiOQivh0pcCMXeLBUSAcoq92tPCFwV9nhI3Xn4JXdnQOd6-5GlWuzS-BLQYVGKxMhaVsOCJUqFIFRoVYXbJhuG3Zy5oEj3DPZpX_w9RmM0QI2oIYNDH_TzgjI6hmIut4FvWnSgpX262DBOgZGcLmybWk3FjZVJ32b8-fxGw9ZYCa-P5aPrw1Xjkxx6GIp4PSdXAXDVNTUFfNzP5qMVwJo2mCfG7DaJgjOT5b7aeIRJ1aqtox9viJgVpRod7khsKsoRZhjNnKLi', start_index=17486)
Annotation(end_index=19299, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCAL57RbUWM0MlR3nZ8ShFCa7x1qI9KhH0INheCX0XL4mF-_awaORBTCMrWciPx0uxDy0VbSv1irgvFdJQon1-1rULf7xAQVhW9UX34uw-KrjWlUoAi_zstNRqpCcBXWSrE1ZxXovc9ziES-bR0SdmpT2Ag4M=', start_index=19290)
Annotation(end_index=19382, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFac01RDXINwG-NenAiRRQQkFjpyv7m3vObbLDUeqRhmxmgfFrdC_iV05ckN-uF3C2xDxWKChvzAJdjeK4PHKvkzaF6J2g9nEpboQzWyQ4nljojyvCa9d-XodCeRmiKga3y2e1xJDLJrNkE9hAShp14OyMdKNpBCnQ=', start_index=19373)
Annotation(end_index=19462, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQES0RkljYPwaNmI2uPI5PDMOxnE27L8KAOnbSRLBcpTL0CUE_EcHe_-4EdTZ5QZHLbkXn7SXTYvqoS9FdiqMNz77nPCNTvL8NoMi46yqa4zLDp0aLtOSftheFeFebuNsrkuJmb3W9KqjXBc3bsywXhD_-uiVuzr1hEEYH5p4Q==', start_index=19452)
Annotation(end_index=19521, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHM9CG6dVHaGLqIv5GGtS2ybZ_yfouIIY-V9re2aRhMu8CYgaj6O_XncEdEhMGfXbG0cKs52SOJy7_znbBN18b8QJUf-DNGQN5IBa6UoDfvr1gQecuZrH86538g1NAM8tbe7TUnpXjye5R5VhHbD2_-pQom-KNYwe4NlqQkcLIpJTHmFLR8fH9VXxgzMs1c-Q==', start_index=19512)
Annotation(end_index=19598, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwutK40jYn2DtBJtMpn6ZuEe2qeBrX_l0knQb5H9ZonCoz4Yjzcb4z13SzXwIpTfIOC6WYP2fmRhFZSLfD-jktJvynAb3ktYC8mm0KgQGOOq9qBt6g3eAd7oSycRhHgIF9ONkXR5jUq8tff1nSfRguBRAIZwpoKzdnVILyBc4viyykr9mdxdV-PhxDpSTUcNpkrCEJ4xClPJRmgQBFvkm4G_OlLpHGP4tHLahK', start_index=19589)
Annotation(end_index=19683, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzvieGvM3Xvc7NE7_sqywZD3tVJ1QF-Gbqf_k_YX4rhELJynC34PkZrNKGALH068mJM9exPHezNuod9KsoM4jdIiY3xYrkd1j3dcf4B9U4T5xbiqWkgeMlJ_YOLbOAB3eQ-OCl5sX-aUNipyNWL2QONs1Hm5mbgbc7TYlJxzFaYoHUF2mBuKBMAw==', start_index=19674)
Annotation(end_index=19756, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0q14I7OHoc6J4YzcuMzkVol9j7Ra_dzMQOIfv5XRuAd0AVJQ6XNASwvN9ldx9YhG6YBqQj0svpN7JhiHePPhJDHxtWQByjZtPsBQ4rRpPeVYd14yBQYtr8jc0By0s1tdyfc8cI_bGn-2CPBB9_qtSIcCI1b1o6SRwsaOSmnIEOuYcegnI3oSM4NppOqjDADLMZHEuFw9CEG_N16qmezObLlzJEFOeJhrIC0YnLMqkfAwG939-q_9etYbMaCEe2UGNkC0aGgLFxYpzyR_o4QV61__CHB1DkxynRg8V65k-eRSpwGABJTk08FrYieo=', start_index=19746)
Annotation(end_index=19853, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCUFj3PiK6A9uvnbIBoUAGPpD8ny9KoopOI0DnZEUjpj3WzxxuPPT0vP08MPnd3IARkBHe_Gpw0I2JKayOC-ffkUASKeEZfcNjNrOwW3uhs8JqI8fMQAGXyvAzD2emfEdEXk1JoryMx8M_9pVTMskJdBQ=', start_index=19843)
Annotation(end_index=19901, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1PZ2DJ4O7KjxjG9BaW8-QUNwMZCCQPNdAJN_JVg7Am5LcOFe9gHNu1xLyrMpSEO_YMliFq09jx9TfPY0nUzr2CkMmQEI3XF6jUzqntj7WqpnmBMASAORjddhi5pcHpJ2PyqhVkb5yWO4gqC_ICXbW7IbYD0wOvaCLyUuqWdOzHGPTtYACdBvGwBPXyxHJwS9zVX6RUhlYCZu3pRNWwmVS', start_index=19892)
Annotation(end_index=19968, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGy7xBhcDC-A_BeHHw_wsuHp7Wcd1ascW9UJqfJ6RpXi78bDDLF3a_LZs6BCwroDW-r2FKrGY4gwWwCQ6nh1zlRneL8BsXulrTuQBc0ETBlugeFYAyGWdEPRLOf8ziEULYFiLCdlRfQQdw=', start_index=19958)
Annotation(end_index=20035, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyLugR-97dGguuyr5DdZyK0b_TtKEiTuyiOQivh0pcCMXeLBUSAcoq92tPCFwV9nhI3Xn4JXdnQOd6-5GlWuzS-BLQYVGKxMhaVsOCJUqFIFRoVYXbJhuG3Zy5oEj3DPZpX_w9RmM0QI2oIYNDH_TzgjI6hmIut4FvWnSgpX262DBOgZGcLmybWk3FjZVJ32b8-fxGw9ZYCa-P5aPrw1Xjkxx6GIp4PSdXAXDVNTUFfNzP5qMVwJo2mCfG7DaJgjOT5b7aeIRJ1aqtox9viJgVpRod7khsKsoRZhjNnKLi', start_index=20025)
Annotation(end_index=20098, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEUFQXuGdu-gCznckSUTcoLfHapT5BbQlgNi3n37Z-tWmsa0IQ76xUljbM4UB_B6sZ_yjf7Nt32QTgY5sJtbyKPvNMnrP-PxEcKn3UOmb488eDsyGrxb6fiwOM_9JqGi8ewZNNkkPEkppL16YzAJcdE9TQTPbPSqvYo3Yo', start_index=20089)
Annotation(end_index=20152, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG51wqLTwzrrigi5C3BJZvB7bpuQBsOwa0nR9LoXkEocnBm3hzrAGSlhRBx4LpfJ5Hwg5yraFheCI32FTfbaE-secPX-xrw6UXU8b5MH-AZm7m6qrxdGqoc7A==', start_index=20142)
Annotation(end_index=20225, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_CQ1wgZ4HvEYJ6kchT4Vp8JJy3JFoqPaeAG-C4AmUe-ciLY2Jy3wcQIoinh6tx2jRM6WnFP43YLAyQ0WYLxodwyn0LOglYfvlTSBs5vq5sCAsHboldSnxA65AZLlshl0vb2k=', start_index=20215)
Annotation(end_index=20283, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR0tnEpM-Ogsk-5D1ihaN51qio9gCZgB8Uij11HTp05AVnxrG1_gA61Pqx4LzNlcmJ6ll9Ts7Wee-ZaFd9LjYOz8V3JxgJ6Q85KQ6MdL54q7TJrys2_9jS6ACkSm-rojDe-sAqSsMMnhs0kZmL6Kw=', start_index=20274)
Annotation(end_index=20331, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1s-4nzVhDXDiZ9d0PmRedHDAr0UuyLyCGzjJyeI5-3gheQuWUlcWgWvy7GeerWA54D3vQpe7BSWSx0nQ_tsDtVkMlXmtwmZQvXYtagI4IFbZDDLiBdQRPI3Vo2NpXBmJeCmaMOMuYlBCNtqJIIsZD6VGTc48WhOOp7Q8lHC-P3jlhjYoiQUQuqx9r8HB1gvTEdc8c', start_index=20322)
Annotation(end_index=20402, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyLugR-97dGguuyr5DdZyK0b_TtKEiTuyiOQivh0pcCMXeLBUSAcoq92tPCFwV9nhI3Xn4JXdnQOd6-5GlWuzS-BLQYVGKxMhaVsOCJUqFIFRoVYXbJhuG3Zy5oEj3DPZpX_w9RmM0QI2oIYNDH_TzgjI6hmIut4FvWnSgpX262DBOgZGcLmybWk3FjZVJ32b8-fxGw9ZYCa-P5aPrw1Xjkxx6GIp4PSdXAXDVNTUFfNzP5qMVwJo2mCfG7DaJgjOT5b7aeIRJ1aqtox9viJgVpRod7khsKsoRZhjNnKLi', start_index=20392)

## Sources
