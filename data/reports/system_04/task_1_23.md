# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 8a92ed57 | **Time:** 459.78s | **Cost:** $1.34024
--------------------------------------------------------------------------------

# Balancing Explanatory Power and Overfitting in Multi-Factor Asset Pricing Models: The Role of Ridge Regression and Prediction Bias During Anomalies

### Key Points
*   **The Trade-off is Fundamental:** Multi-factor models face an inherent conflict between maximizing explanatory power (reducing bias) and minimizing overfitting (reducing variance). Ridge regression (L2 regularization) explicitly manages this by introducing a controlled bias to reduce estimation variance, theoretically lowering total prediction error [cite: 1, 2].
*   **Bias is Inherent but Not Necessarily Amplified:** Ridge regression is mathematically defined as a biased estimator. However, whether it "amplifies" prediction bias during anomalies depends on the nature of the anomaly. In high-noise environments, Ridge often stabilizes predictions better than OLS; however, during structural breaks where signal strength surges (e.g., high-volatility crashes), static Ridge penalties can suppress valid signals, leading to under-reaction and increased bias [cite: 3, 4].
*   **The "Factor Zoo" Context:** With over 400 identified factors, the risk of spurious correlation is high. Ridge regression is superior to OLS in this high-dimensional setting because it handles multicollinearity and low signal-to-noise ratios effectively, often outperforming variable selection methods like Lasso when signals are diffuse [cite: 5, 6].
*   **Dynamic Solutions are Required:** The "inevitability" of bias amplification during anomalies is mitigated by dynamic approaches. Rolling-window Ridge regression and "de-biased" estimators allow models to adapt to structural breaks, preventing the regularization parameter from enforcing obsolete constraints during market shifts [cite: 7, 8].

---

## 1. Introduction: The Dilemma of Modern Asset Pricing

The central challenge in modern empirical asset pricing is the tension between the proliferation of pricing factors—the so-called "Factor Zoo"—and the statistical reliability of the models built upon them. As researchers identify hundreds of potential predictors for stock returns, from momentum and value to complex accounting ratios, the risk of overfitting increases exponentially [cite: 9, 10]. A model that fits historical data perfectly (high explanatory power) often fails to generalize to new data (high overfitting risk), particularly during market anomalies or regime shifts.

Ridge regression, a form of Tikhonov regularization, has emerged as a standard econometric tool to address this instability. By imposing a penalty on the magnitude of regression coefficients, Ridge regression shrinks estimates toward zero, sacrificing in-sample unbiasedness for lower out-of-sample variance [cite: 11, 12]. The user’s query posits a critical investigation: does this intentional introduction of bias become detrimental during market anomalies? Specifically, does the regularization process "inevitably amplify" prediction bias when the market behaves atypically, or can it serve as a stabilizing force?

This report synthesizes extensive literature to argue that while Ridge regression introduces estimation bias by design, it does not inevitably amplify prediction bias during anomalies. Rather, its performance is contingent on the signal-to-noise ratio of the market environment and the adaptability of the regularization parameter. While static regularization can lead to underfitting during structural breaks, dynamic and de-biased Ridge methodologies offer robust mechanisms to balance explanatory power with the risks of the Factor Zoo [cite: 7, 13].

---

## 2. The Mechanics of Regularization in Asset Pricing

To understand the behavior of Ridge regression during anomalies, one must first establish the mathematical and theoretical underpinnings of the bias-variance trade-off in the context of financial data.

### 2.1 The Bias-Variance Trade-off
In predictive modeling, the mean squared error (MSE) of an estimator can be decomposed into three components: bias squared, variance, and irreducible error [cite: 14, 15].
*   **Bias** refers to the error introduced by approximating a real-world problem (which may be complex) with a simplified model. High bias typically leads to underfitting.
*   **Variance** refers to the model's sensitivity to fluctuations in the training set. High variance leads to overfitting, where the model captures noise as if it were signal [cite: 11, 16].

In the context of multi-factor asset pricing, Ordinary Least Squares (OLS) estimators are unbiased (assuming the Gauss-Markov assumptions hold) but often exhibit extremely high variance, especially when factors are highly correlated (multicollinearity) or when the number of factors ($p$) approaches the number of observations ($n$) [cite: 17, 18].

### 2.2 Ridge Regression (L2 Regularization)
Ridge regression modifies the OLS objective function by adding a penalty term proportional to the square of the magnitude of the coefficients. The objective function is minimized as follows:
\[ \hat{\beta}_{ridge} = \arg\min_{\beta} \left( ||y - X\beta||^2 + \lambda ||\beta||^2 \right) \]
Where $\lambda$ is the regularization parameter [cite: 11, 15].
*   **Shrinkage:** As $\lambda$ increases, coefficients are shrunk toward zero. This reduces the model's flexibility (increasing bias) but stabilizes the estimates (reducing variance) [cite: 2, 18].
*   **Multicollinearity Solution:** In the "Factor Zoo," many factors are economically or statistically redundant (e.g., different measures of value). OLS would assign large, unstable coefficients to these correlated variables. Ridge distributes the coefficient weights more evenly, preventing any single factor from dominating due to noise [cite: 15, 19].

### 2.3 Signal-to-Noise Ratio in Finance
Financial data is characterized by a notoriously low signal-to-noise ratio. Most movements in asset prices are attributable to noise (irreducible error) rather than predictable signal. In such environments, unbiased estimators like OLS often perform poorly because they "chase noise." Theoretical insights suggest that Ridge regression is superior in low signal-to-noise environments because the variance reduction it provides significantly outweighs the bias it introduces [cite: 6, 20].

---

## 3. The Factor Zoo and Overfitting Risk

The proliferation of factors has created a crisis of replicability in finance. With over 400 published anomalies, the dimensionality of the predictor space often exceeds the available time-series history for reliable estimation [cite: 5, 9].

### 3.1 The Curse of Dimensionality
When the number of predictors is large relative to the sample size, OLS models inevitably overfit. They identify spurious correlations that exist in the historical sample but vanish out-of-sample. This is the definition of overfitting risk in asset pricing [cite: 15, 21].
*   **Spurious Factors:** Many factors in the "Zoo" are likely noise. Including them in an unregularized model dilutes the predictive power of genuine factors [cite: 9].
*   **Parameter Uncertainty:** Even valid factors have uncertain betas (risk loadings). OLS ignores this uncertainty, leading to overly confident predictions that fail during market stress [cite: 22].

### 3.2 Ridge vs. Lasso in the Factor Zoo
While Lasso (L1 regularization) performs variable selection by setting some coefficients to exactly zero, Ridge keeps all variables but shrinks their impact. Research indicates that Ridge often outperforms Lasso in economic and financial forecasting.
*   **Diffuse Signals:** Financial predictive power is often spread across many weak predictors rather than concentrated in a few strong ones. Lasso tends to arbitrarily select one variable from a correlated group and drop the others, potentially losing information. Ridge retains the information from all correlated predictors, which is advantageous when signals are weak and diffuse [cite: 6, 23].
*   **Weak Signals:** Theoretical work shows that Ridge regression is superior for exploiting "weak signals" (covariates with small non-zero coefficients), whereas Lasso may fail to exceed a zero-benchmark in such scenarios [cite: 6].

---

## 4. Ridge Regression During Anomalies: Bias Amplification or Stabilization?

The core of the user's query concerns the behavior of Ridge regression during "anomalies"—periods of market stress, structural breaks, or extreme volatility (e.g., the 2008 financial crisis, the COVID-19 crash). Does the bias introduced by Ridge regression become a liability in these moments?

### 4.1 The Argument for Bias Amplification
The concern that Ridge regression "inevitably amplifies" prediction bias stems from the nature of shrinkage during structural breaks.
*   **Under-reaction to Structural Breaks:** If a market anomaly represents a fundamental shift in the data generating process (a structural break), the coefficients learned from the pre-break period are no longer valid. Ridge regression, by constraining coefficients to remain small (based on the penalty $\lambda$), may prevent the model from adapting quickly to the new regime. This results in "underfitting" the new reality, effectively amplifying prediction bias because the model is constrained from moving to the new optimal parameter values [cite: 24, 25].
*   **Indiscriminate Suppression:** In some contexts, high-frequency bands of data contain both noise and critical signals. Regularization techniques that indiscriminately suppress high-frequency components (to reduce variance) may inadvertently suppress the "alarm signals" of a coming crisis, interpreting them as noise. This leads to a spectral bias where the model fails to predict the anomaly [cite: 26].
*   **The "Gray Area" of Weak Signals:** During normal times, weak signals are indistinguishable from noise. Ridge suppresses them. If an anomaly causes these weak signals to suddenly become strong determinants of returns, a static Ridge model will miss this transition, leading to large prediction errors [cite: 6].

### 4.2 The Argument for Stabilization (Variance Reduction)
Conversely, a significant body of research suggests that Ridge regression reduces total error during anomalies by preventing overreaction.
*   **Noise Dampening:** Market anomalies are often accompanied by extreme volatility (noise). An unregularized OLS model will fit this noise, resulting in wild coefficient swings and catastrophic out-of-sample predictions. Ridge regression acts as a "gentle weight," keeping coefficients stable and preventing the model from chasing transient market panic [cite: 18].
*   **Rational Regularization:** Forecasters facing noisy signals rationally regularize their estimates. Even if this introduces bias, it is the "textbook prescription" for high-noise environments. Empirical evidence shows that Ridge regression often yields lower Mean Squared Forecast Error (MSFE) during crises compared to OLS because the reduction in variance dominates the increase in bias [cite: 4].
*   **Robustness to Outliers:** While Ridge is not robust to outliers in the same way as robust regression (e.g., Huber loss), the shrinkage prevents any single outlier from pulling the regression line too far, which is a common failure mode of OLS during crashes [cite: 15].

### 4.3 Empirical Evidence from Crises
Studies analyzing the performance of factor models during the 2008 crisis and the COVID-19 pandemic provide mixed but generally favorable results for regularization.
*   **Emerging vs. Developed Markets:** In comparisons of Fama-French models during COVID-19, adding more factors did not automatically improve reliability, suggesting that model complexity (without regularization) is a liability during crises [cite: 27, 28].
*   **Tail Risk Prediction:** Ridge regression has been successfully used to forecast tail risk and volatility during crises. By stabilizing the covariance matrix and coefficient estimates, Ridge allows for more consistent risk assessments than unregularized models, which may blow up due to ill-conditioning [cite: 3, 20].

---

## 5. Addressing the "Inevitability": Dynamic and De-Biased Approaches

The assertion that Ridge regression *inevitably* amplifies bias is challenged by advancements in dynamic modeling. The limitation lies not in the regularization itself, but in the application of *static* regularization parameters to *dynamic* markets.

### 5.1 Dynamic Ridge Regression and Rolling Windows
To prevent bias amplification during structural breaks, researchers employ dynamic Ridge regression.
*   **Rolling Windows:** By estimating the model over rolling windows (e.g., the last 60 months), the model gradually incorporates the new regime. While there is a lag (bias) immediately following the break, the rolling approach allows the coefficients to adjust. Ridge regression within these windows stabilizes the estimates when the sample size ($T$) is small relative to the number of factors ($N$) [cite: 8, 29].
*   **Time-Varying Parameters:** More sophisticated models allow betas and risk premia to vary over time. Dynamic asset pricing models using Ridge-like shrinkage (or kernel regressions) have been shown to yield smaller pricing errors than static Fama-MacBeth regressions, explicitly capturing the time-variation in risk premia during anomalies [cite: 13, 29].

### 5.2 De-Biased Ridge Estimators
Recent econometric innovations have introduced "de-biased" Ridge estimators.
*   **Iterative Bias Correction:** For high-dimensional data ($p > n$), standard Ridge estimators are biased. New iterative strategies can correct this bias effectively. These methods estimate the bias term and subtract it, allowing for valid hypothesis testing and confidence intervals even in high-dimensional settings. This directly counters the "inevitability" of bias, allowing researchers to retain the stability of Ridge while recovering unbiased estimates of the true parameters [cite: 7, 30, 31].
*   **Bias-Variance Optimization:** The choice of $\lambda$ is critical. Cross-validation is typically used to select $\lambda$. During an anomaly, the optimal $\lambda$ may change. Adaptive algorithms that update $\lambda$ in real-time can prevent the model from becoming overly constrained (high bias) when the market environment demands flexibility [cite: 2, 17].

### 5.3 Machine Learning Integration
Machine learning models, including Neural Networks and Random Forests, often incorporate L2 regularization (Ridge) as a component.
*   **Non-Linearity:** Neural networks with L2 regularization excel at capturing non-linear functions of weak signals, which linear Ridge regression might miss. This allows the model to detect complex anomaly patterns that a linear model would interpret as noise [cite: 6, 21].
*   **Double Descent:** In modern ML, the "bias-variance trade-off" is sometimes replaced by the "double descent" phenomenon, where highly over-parameterized models (with regularization) achieve low test error, challenging traditional intuitions about overfitting [cite: 16, 32].

---

## 6. Conclusion

The application of Ridge regression in multi-factor asset pricing models represents a calculated compromise, not a guaranteed flaw.

**Can multi-factor models balance explanatory power and overfitting?**
Yes. The use of regularization techniques like Ridge regression is essential to achieving this balance. By shrinking coefficients, Ridge regression allows researchers to utilize the rich information in the "Factor Zoo" without succumbing to the paralysis of multicollinearity or the error of overfitting. It effectively filters the signal from the noise in high-dimensional financial datasets [cite: 5, 9].

**Does Ridge regression inevitably amplify prediction bias during anomalies?**
No, "inevitably" is too strong. While Ridge regression *is* a biased estimator, this statistical bias often prevents the catastrophic prediction errors (variance) that unbiased estimators suffer during crises.
*   **Conditional Amplification:** Bias is amplified only if the model is static and the anomaly represents a structural break where previously "shrunk" signals become dominant drivers of returns. In this specific case, the regularization penalty prevents the model from reacting fast enough [cite: 24, 26].
*   **Mitigation:** This risk is effectively mitigated by using **dynamic Ridge regression** (rolling windows), **de-biased estimators**, and **adaptive regularization parameters**. These tools allow the model to adjust to the new market regime, ensuring that the bias remains a stabilizing force rather than a blinding blindfold [cite: 7, 8, 13].

In summary, Ridge regression is a powerful tool for taming the Factor Zoo. Its tendency to introduce bias is a feature, not a bug, designed to combat the far more dangerous enemy of variance in noisy financial markets. When implemented with dynamic adjustments, it balances explanatory power and overfitting risk more effectively than unregularized alternatives.

---

## 7. Comprehensive Reference List

*   **[cite: 1]** Infermatic.ai. (n.d.). *Impact of Regularization on Bias and Variance*.
*   **[cite: 17]** Bindel, D. (2019). *Bias-variance tradeoffs and regularization*. Cornell University.
*   **[cite: 14]** Towards Data Science. (2022). *Machine Learning: Bias-Variance Tradeoff and Regularization*.
*   **[cite: 33]** The Friendly Statistician. (2025). *How Does Regularization Affect Bias And Variance In Regression?* [Video].
*   **[cite: 11]** Cogxta. (n.d.). *Regularization and the Bias-Variance Trade-off in Machine Learning*.
*   **[cite: 2]** The Friendly Statistician. (2025). *How Does Ridge Regression Affect Bias And Variance?* [Video].
*   **[cite: 7]** ArXiv. (2024). *Optimal Bias-Correction and Valid Inference in High-Dimensional Ridge Regression*.
*   **[cite: 34]** MLFactor. (n.d.). *Chapter 3: Penalized Regression and Anomalies*.
*   **[cite: 18]** The Friendly Statistician. (2025). *How Does Ridge Regression Fix Unstable OLS Coefficients?* [Video].
*   **[cite: 15]** Simplified Zone. (2025). *Conquering Overfitting: The Power of Penalized Regression (Ridge & Lasso)*.
*   **[cite: 27]** Kostin, Runge, & Adams. (2021). *Analysis of Fama French Models during COVID-19*. MDPI.
*   **[cite: 28]** ResearchGate. (2022). *An Analysis and Comparison of Multi-Factor Asset Pricing Model Performance during Pandemic Situations*.
*   **[cite: 32]** Quantopian. (2025). *From Econometrics to Machine Learning: Transforming Empirical Asset Pricing* [Video].
*   **[cite: 22]** Journal of Finance. (2000). *Assessing Asset Pricing Anomalies*.
*   **[cite: 5]** EconStor. (2022). *Navigating the Factor Zoo*.
*   **[cite: 6]** Shen, Z., & Xiu, D. (2024). *Can Machines Learn Weak Signals?* BFI Working Paper.
*   **[cite: 20]** Stockholm School of Economics. (n.d.). *Return Prediction and Dimension Reduction*.
*   **[cite: 21]** Pelger, M. (2020). *Deep Learning in Asset Pricing*. University of Zurich.
*   **[cite: 35]** Medium. (2024). *Handbook of Anomaly Detection: Regularization*.
*   **[cite: 16]** IBM. (n.d.). *Bias-Variance Tradeoff*.
*   **[cite: 3]** AIMS Press. (2025). *Ridge Regression and Realized Volatility*.
*   **[cite: 24]** MDPI. (n.d.). *Market Crashes and Ridge Regression*.
*   **[cite: 25]** MDPI. (2024). *Forecasting Inflation with Ridge and Lasso*.
*   **[cite: 36]** Basu, S., & Michailidis, G. (2024). *A high-dimensional approach to measure connectivity in the financial sector*.
*   **[cite: 37]** Espinoza, N. (2023). *Why & How AIs Hallucinate*. Medium.
*   **[cite: 26]** OpenReview. (n.d.). *Spectral Bias and Noise Amplification*.
*   **[cite: 20]** Stockholm School of Economics. (n.d.). *Deep Learning vs. Ridge in Return Prediction*.
*   **[cite: 13]** Nagel, S., & Singleton, K. J. (2011). *Estimation and Evaluation of Conditional Asset Pricing Models*. New York Fed.
*   **[cite: 38]** Lazarus, E. (2022). *Dynamic Asset (Mis)Pricing: Build-up versus Resolution Anomalies*.
*   **[cite: 29]** ResearchGate. (2025). *Regression-Based Estimation of Dynamic Asset Pricing Models*.
*   **[cite: 39]** Van Binsbergen, J., et al. (2021). *Dynamic Asset Pricing Anomalies*.
*   **[cite: 18]** The Friendly Statistician. (2025). *Ridge Regression and Multicollinearity*.
*   **[cite: 9]** ResearchGate. (2026). *Taming the Factor Zoo: A Comprehensive Review*.
*   **[cite: 10]** Springer. (n.d.). *Multifactor Models and Machine Learning*.
*   **[cite: 40]** Zhu, R. (2024). *Ridge Regression and the Bias-Variance Trade-off*.
*   **[cite: 19]** The Friendly Statistician. (2025). *Why Use Ridge Regression Instead Of OLS?*.
*   **[cite: 30]** ArXiv. (2024). *Bias Correction Strategies in Ridge Regression*.
*   **[cite: 41]** Medium. (2024). *The Art of Balancing Bias and Variance with Ridge Regression*.
*   **[cite: 31]** ArXiv. (2024). *Optimal Bias-Correction in High-Dimensional Ridge Regression*.
*   **[cite: 12]** Wikipedia. (n.d.). *Ridge Regression*.
*   **[cite: 23]** UC Riverside. (2025). *Forecast Combination and Ridge Regression*.
*   **[cite: 8]** Insider Finance. (2024). *Adaptive Time Series Forecasting with Rolling Ridge Regression*.
*   **[cite: 29]** ResearchGate. (2025). *Dynamic Asset Pricing and Rolling Windows*.
*   **[cite: 4]** ArXiv. (2025). *Rational Regularization and Forecast Efficiency*.
*   **[cite: 6]** BFI. (2024). *Ridge Regression and Weak Signals*.

**Sources:**
1. [infermatic.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEt1kzClYjDiCLRub9lRLHCYoiEg79ZVcGlfBRYpFS0-CkPMUUGl1A5VCO9QyXPThPfWV6hztXoUgiVdvuD24qocVyxPuA6AVih65RLfDxpHshIAPDaRKZDvy4o2hy8j1PjoG78Hm754h_73csqfl_8GSB8O8vP5IoYBMBLeJKUdYl25zWQZy0CBUIGZkuhRxzXumuNmtdIEVIaPbum4yEB61wCkWe8ZmNMiRYKURvCmWrzD1_xufDNTEKScPhiL-lvcWLw)
2. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDvKRQe5i30D6s0M8yZtQzCKtRv0mcy4dQMQSTYIzCdqdhd_rGT7tZRm1hhaRWxeFxm8wMJUE1PXuTcHQd9FFFreLzY61ZIjK7zU96WVxOprJlcGrMl8qKxf6OiRT6srE=)
3. [aimspress.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpoXV8EkGwmT9SITRS6m-GIKBwMVDNfOXPWaE5DO1JaDqzDA4wlQZMZVO_GjszNXRrzaPt466uv-YUnPRMaqHaiX0Hei1UZRZPmjcOqykgNmWAU3h7uXscKbQW24gpf1o4wwKBVYb9GtriusimgQZKicTCJVLf-DOH2FjeKsE=)
4. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-_fGDGtfVKIHb2bu8hdUBEkkP0XE3vYr6Z1MCxEDWwcEH3P2AeMZ-gdzbw099PPmW-ugdEWDKNjytkrhFUp6yYKZS_pqD-M1ybr_QVy48qYp6n83s)
5. [econstor.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvstHmGl7x5WbvY19Xyv4_7HtKdBuTkXDWuCUZ3MaDS8p-mx3tjH1MJpFHw4j3qPhWLiBgVNFOlantX_XsXg--6jrcKYoewmwldmj5Dd0_VcAuqOSFlIdCZxrtonIv0d6zMz_a1RQhKr_lo0VAAni49zgzJEE6V1Qv5bpd)
6. [uchicago.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzeqp1EZ_omw2RMRuI30B-3cXt8jpwpb7KhvkB9S75ZUqLFPbQlhgo-Dw46vhiIT2UX3oihhXtzAGfbpqTWhgDo0wvmMYqDep7hqTpofJO7gqASRqUF4ApWumHdlitRcy6BOyFADprcEweNi0v02Km6S7H0rdx1Int6Gs=)
7. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUeyA3h85GqUNFPt9L-tFSEk_ICqgps9ppcmclSjnUeE1P2Y_xyj0OJkw-3ax2986kFe-yNbrJxMxyumEwV6GemUFp7lhh5lnLYNmqKFwtLuTHEhx4)
8. [insiderfinance.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyXY_y-C_GO6No6GobscQiRSDjShUWyCB8yki2QxyJfgAgPLq627Z5LboNDHYaYgz5Yo5UiIE8HXXu5HkLT5Jef03RrYAAkMt3R5dKE79ZHwkrcq2JTvKZLmNhAPrkSjaLqfHnOcP6hmwCsr0pSbSE8tcXM9oVZj8dg3nlc_kUIiCoKNC1CR--lRTwkyAOCgGKMjLtX9MHzqN3tQ1k7x4=)
9. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbb0etVF0-RIDogAYGcdqROSTSlog7e-iCMzrYUneocL5aNz6TIPndSCefUwkUKn9HxGj8jhsWOgUJmEAzGeLE9tcnF1F4KlTfzDA1dYLaFMBT-kt6Gy0zI99P15P4flnrHslwKht8Z_Qbia3mlIyzajAo_HSI48v-DE_gAJKfSRmXQ1avHTf9ymYCURnx_I89mXO3lV1-U_v3Sb-HhbgauhLsHgIR2G5J3zdARd2v0AY66UKteq5LhKN_8GYLqGBYKbqK8y3oCPUiIRg846msmM7seha7brr2G3lnwhI=)
10. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2pbXrd6-gbeYlGjUrPAF-OLBs5MCj_wg0kk-omVDlk8X_tMen7HS0k83x1MPTlozp_vaPUeNN7SeUEZa7GESZHcckehR7NL1cwsv4QPcmiPrbOOV7nVth1WgI697qU11StfrSN0C8bg5YbLCXgXO0qKQ=)
11. [cogxta.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExSmxNSkZTQoKCjpBBA4rQYjCO8scihwM-bt9-0n3WOBVeNlg63AsNbnpWCyMhNJy4tSDgcfvfXj-dafhUCDWSMEIsmD-CE-24iOsyevfOxTwvCgluWMpkrNzBw-DHNqjxUkIjbd_F5mgK6kzaxfTFHltIZuA90p30DP1JuO6E1AKZBXry8loeyIG1G1zVXfA=)
12. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESb45kjQoKZs21-FtUzMm_EzKsds1cqdyQxdXww6DsJlgRX5t0ZBdGX_QK-eVkz0UE-cTbjHOTR-Saq1kJmsrDcfBC23uFglcbq_zssywrUydfsAoCLk1KIEGc55XJW21xa_Y=)
13. [newyorkfed.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE39i18IX4CrxNidl3_QnlLwP0R4qthmfXPX4mdpkHbI_iTwJTOqPBpLf-LkpwJTL617EDukXJQQpoivT8Hq0BMaHHQ7KHSNVL9HP3PWsCxenrVB6S09hw5EOiAv8QuTlkoA0Fy4HhEuvwvtn-b7J_L6nWwOcqg21TDN0RIxhagtR_HtQ==)
14. [towardsdatascience.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpFWrS30l6FphabGq6CGI-Xh-vE7TenOtKBWfA-enFs7EjZTa8kVHZnGLdV6TwqQosVg46fMn_4ntmVviEPYRQK-K0bzVwktN0WhI16vMYT5-1oHNFcwcUEHdCgSBTJPKbVSX_WQxh3MQCrRaNV2Ufgx4k_8cu_Tct8xyNowebekvuFzCNNZkDPP9y_jh3-iaKYWeNjTgK23ut0-U=)
15. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGb7o-w2-hi5Uv6aTeobTbj9AeN-lnoeKGXxdBXMdp4Tc9jLiazTxe6uSCRtyIJngo0bjK_-T2POuChobW-r02Dln5N8r02WRBWeh_Ftjf83fJluuagSOjvP6bIC-4eBzBxPa5BsYgHIfxi5ljcO0QKZHbQn2zXR7wNWxxaHCRZl5RH5PRRN8Qi-JHLetcj6VrziBrNlb5ak-rZDTcss48NrKyiczKaeU9J0O5ylXuA)
16. [ibm.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbKm6vMTPLVpmR0L_okArADg2zbnHUt1oAPsowBWRU9VvPrSWoOJJgZMBJEOSfFeWqnqbf9Xd6Ve_ruL9Z7n07mkZPupzX8lW3lx54I6CoOJyfHRITHk51O7VccoAg-EjDPKqL3l7WoYkHeXI=)
17. [cornell.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHZykpVCOmXvoF8KA7dRy6QCmQ1uwVW8b_kEBieT9eynkW8ILJdgzCOKIkelE69CxorQ8k0jdSf49TQhePpFP7V65HkF5oAGTiwOofZKWCSWSex_p30s8YEy0MbydIHkqnb8j6s_PJRb9M-3ZXzMFU36izv7jkW2GzmGJ2lLM=)
18. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6GvWKtPdCxGcHm-gZjyehTj8Iy7e_MnFWYw1xh5ihoXO8b2PlImzYbLWraEnSDTXp4XR9_yofcxtBPFaIfdjoOxyognNeo75-jraG2Cna8IoNklJysl-lggYvpAwH2ds=)
19. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEC3oz_RWNMXYsB_nI5OMZUrPzeHNGHvCME2fT5UTpM1D2ape8h1OoasiQAIlzvbU_DQud8jW-OdEtquuLeNvijI67vM7OaMQjlqFDFrLvpBAzzNpSmA5Lrt3m4nGZKzK0=)
20. [hhs.se](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9w79MscHp5h5HrHE7XOMm69puJYVCQk_uiJcWDqDbdGZktjBF79LdE5Up23tbQn4XaAwnQLwFaTLvc3uEGO3XDuQ6fyp4FKkJ4B2mrEKQVPgNDg36YDurzL_ehuXuh8aGfA==)
21. [uzh.ch](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTtw5qhcyqpA5GbM7JGnidCKD6QapOqUO7ojnkezwBYBkJHWvMKgTKW4BhEp7BigQjWGsKXH2QmxWWmyC_cDvtR7YcN-Ei617WuQFBsbPouS20DHQBzNL1Nu10WhF1XaH3h0ECZZJ8eA49uQkmxiB-m5QCoAoQS-dQpW8nvLeD08ubT_SygRG3P4q8g0IeSlRMJe4yJGxqf0VWBA==)
22. [efinance.org.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEesM21hTJRbWhwuzxq3xLs1WS9Ia79t-u28BIQzGd1FFxgf5RNI6-ocNGcLbfz_6joB81nMPvOZZUpEiBebD-i0oeq4hFKFVIvU26auTOwN0nzP4KSmglBAJE-8YPwTEv4zD6gEZkSxnpzN9Zbu3jlwIhd0N7JHLq9_d3jYA==)
23. [ucr.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETSh_eCN6LZkTYSNDme1phmEHFBhamK9aAzETim6vOyj2wiwGmwRGY9tLDmD7M_HK3aYW79R-bHY9LjTZ6CN-Tq0YCv8ro1QlTu3_XHMYC8qNjKJATQUNEdOVHMRUjUn0u8ajkB4caoSrP)
24. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMKHfi-JRtZb2z2F7nv3qNsyC6f2Sd1GreYeSLW3bAwbM4ETKl12XuqB9wp93aFPN4eLU2z43zWYtc-ADTVljkPFq_QeluJKGYhJZ4IV2PLTr87Rrrvn5qMiV44g==)
25. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCjTvpXauxqsDvqnj_W8ljBOCwRwjaXCP6Sy2p8pK6bkbh7Z5dXQEhaLal_Vt_CTLtCyMiEFxJwTlYzbENbuT6tOmvLIw1yrXXpe_g-BbIsS69TXOoj6dgNF0=)
26. [openreview.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAYrlhpuRAAgJ9u9LBI_sCGjKjlw42DF-v8Y3IUehQ_VXXrgry2qliwkoti8sa-9BHwzADFgNZw4ZxET-VvZldAGeEwKcu2-9-xMBntcv_K1PNmiJDNlzX3iRBQK1jSwEj8ZR0OMee19rw6aCIKkjSX-oLSPFxqExp-8y9)
27. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmOZMji_BwJfS4nC6tgoSmtICB_ioCbEGNbyFHu0FCuleIsU2YveBWQMrhoAesRRr_5hfSsD7S55nKm1WUtnTPV3oFBgBpxk3PF7RjgZblARbhvCJmeC4mmox8wQ==)
28. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmrLU7itm4rU7K-Qaq9-ceeWpKSIcmW7uaXA4gzzQnBCgLwyD1rCbixmWz-RslRhATutn0SBvTuJhssMj-mNuNC1tmHL-D2eLgAnEA9dHEcCiOtLhXPyXdXV3vpUe-IfdPOPVnqVyS03KPCfNeS7PmxcbLwO8-QX4mmXjOekhiwaRpLzvOrm1R-sT_1aXV4CnjBOdRQtcEh2egjKA8ppLmEB7SIlogvcbSZMhrX8y9DjzBwIH1OyFgXS33_JdotREKT5mQb-3Kq_2-zGUId8nDvvbYklxvEVUrrKiTFEWyqDBu-dL4H-BZ5hGRINV5VKE=)
29. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGICXat3kn6-DLQonuuTNHZ2CSXoWEfYE7bYHM1hH8ihpo4ZgrtDv1TeYgVmw0cif7QEe0YCoerzq0VuInmzcpVYT4zllBSBGookB5OEicpVJ4OwTRGEMpU0J1-jAumnl26G0Lwd7coeeqMlNQKEg2reJRYLLQ6JC4LIvMqNrrl7SfC3r2OVbPO8gl8dad-H9KjcHXJ96gYRt3A-6wetE9rL2hA)
30. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnsHnYHGsDZl7iWsOM463bRX9OQZ9Kbf5Az8Qz6bQasl0lELKBqOnxJhwDcLLnpBSP1cUj-_5_HyFEllxm-Te_7-jgvx5kAAx0flhsWMJfLyoWk6DZgV7p)
31. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfJhLH4MLu1kXbRyDbcXD00ZM3KaUJQls813z6w8wm11xy3zQ_hxVKhc-4BitlhBc6Tbbg_8GHopefzawAzi4wZzrCS7cAUD0yVO_uflMoYTVYoCQF)
32. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfTAj6kN_FkiEpj7O27rz6GI6k6j8SZnWHzEVxlRbas-6jIbvN1YmsgbM3kYgUlAsRvYrOa69-lxNl9cFh7UzJOT9hWJ_5AgPWYRemMgMAspq3wIcxwnQ_KEfg7cjmuxE=)
33. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3HyO3cLXMpfdyJzgmYQVz_t3YHowGPtD-nBoX9kIzGUX4wYrKcSUWLkjUQ35ksix4D8Pv5tZQAUj0yqlXBU_eSVA3g_VN3TkKbzwl-q9WalnQZx798_Sn-haxg4bt-ns=)
34. [mlfactor.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjR_KEIV8U9krcRHpb0kZSDCpUQ2KK-vpXZ2-P9PfwXv24dIyQEkScKQGBTUmiaZs5zmKRxmkwnOXVYJL_7lS6c9lp-nKu40V6J7WeARACEezjEcDTBtNk)
35. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFancGSoA2DDdFjqkrLc_V38EH0CW3wtX7t1uXdPulycM_JmcTzgDbPcSvn1sV8e1G1w8vu5hlv0x9xrd5gAWGYNT70A3UMSU31K8zG_4en1GxYNF6yM-zNrTk_AXoCRIAKt_K2uvJyzFoH8dHUACOv3GKJmjRVEBPjhcc4CsAXfm--uqOFHTa2to2bRHylnozllA==)
36. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_s95IE3U7tV_oPCUK8kkX9hsag75M5OUo2geuGqE0pwWhLflL8hXoWQwaXGZA3L_lflvWG39nZQhqvnr1ks_v_00fWwKXvYQwDuW4We7eKcZuh0QZKKn4oZsnKQUDTCFA3pS-kfe5UBOBXwKIjb1_rf2TzQFlZjQkYC_9DwGaAW6_pYePimVO9SZEBMD_cFVHZgznTH819dEKvs8a8EycG6h_zbSZkxBUPP_KQMKdwCIOvg==)
37. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9b3fF7I3jiorfSJStmBqTIxIe1jxGng-izMFodZkzLK03gs-Hg1tEuNTgIgNe1Rbk3dQ0qI5U0qZRUQ1tDlPAVYBfjQOeXpkiy-Um6QFXpPojbk1etE6dbinxfojFFmu7sl_0UWtXnB_DrypvJkYJ6rJcTjW1FnqitgYzKg==)
38. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGA_YfFJ3GLeM71g2YlSR7rSOtbJLU7O4fwfvSp4ROQsjohWVGdkutXxQGbfBNnE9oRfjv-hba86uqI3LqHI-JhSDMC40vPdTSVpdP-5cld5n7yulGMg6qyqHearJJJ6y0gKjkJ12iU7bS9dGoxhAwQL4khGnZfrX8xyPjH1xie_T_b)
39. [fraconference.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtTOX8RTyUiGTVM_iH-oizL2FJpfvqSUHzBSDWrwd3fjtFib4npDhRR05KeT1jhSPcJfdxhNqF8ESh6cZoMuO_wXJEij4bjOFB1k7qZa8OTWP_HMPJxBiXKhdHlwJL89UWgwbqMtGL4YiErKG8_pjTk0lb32va2_K7ZlUvAnyd6fBYYMF9G0JU)
40. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhXYvLAujp3XnaLp2crN_QU8509sy9_VObfX5u9Q4RfWZlrrXlOAF9TDLLDqthoLS-ebjcz0boEiqdCDft3pObz_tV79zNgFb2veVe1NAqt8jyClkYSzxa4jAR3bXwX71b8u_0kmgWs-KITsO04jQ=)
41. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHIT_3RL2VkyT-YbXTHQOs-vVN19B5E8E4LOPK_Ja9lEXj6dSXcl3yLooi4nvzyKFDSk_8KUzPHt9Jw8Uciw-IJdJZlBSSO1b2Yye3TBnE3moG2x6RWqFRFIi_ltDQKgEkAhZz3QsQx0_cKmreg1aPUHA_IBHIwkZ_msn1gLbACATYY4icu_LwLpbOmJrfMzIQrcuaW-L8E-9Lzh5hvdcORw==)


## Annotations
Annotation(end_index=534, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEt1kzClYjDiCLRub9lRLHCYoiEg79ZVcGlfBRYpFS0-CkPMUUGl1A5VCO9QyXPThPfWV6hztXoUgiVdvuD24qocVyxPuA6AVih65RLfDxpHshIAPDaRKZDvy4o2hy8j1PjoG78Hm754h_73csqfl_8GSB8O8vP5IoYBMBLeJKUdYl25zWQZy0CBUIGZkuhRxzXumuNmtdIEVIaPbum4yEB61wCkWe8ZmNMiRYKURvCmWrzD1_xufDNTEKScPhiL-lvcWLw', start_index=522)
Annotation(end_index=534, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDvKRQe5i30D6s0M8yZtQzCKtRv0mcy4dQMQSTYIzCdqdhd_rGT7tZRm1hhaRWxeFxm8wMJUE1PXuTcHQd9FFFreLzY61ZIjK7zU96WVxOprJlcGrMl8qKxf6OiRT6srE=', start_index=522)
Annotation(end_index=1045, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-_fGDGtfVKIHb2bu8hdUBEkkP0XE3vYr6Z1MCxEDWwcEH3P2AeMZ-gdzbw099PPmW-ugdEWDKNjytkrhFUp6yYKZS_pqD-M1ybr_QVy48qYp6n83s', start_index=1033)
Annotation(end_index=1045, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpoXV8EkGwmT9SITRS6m-GIKBwMVDNfOXPWaE5DO1JaDqzDA4wlQZMZVO_GjszNXRrzaPt466uv-YUnPRMaqHaiX0Hei1UZRZPmjcOqykgNmWAU3h7uXscKbQW24gpf1o4wwKBVYb9GtriusimgQZKicTCJVLf-DOH2FjeKsE=', start_index=1033)
Annotation(end_index=1402, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvstHmGl7x5WbvY19Xyv4_7HtKdBuTkXDWuCUZ3MaDS8p-mx3tjH1MJpFHw4j3qPhWLiBgVNFOlantX_XsXg--6jrcKYoewmwldmj5Dd0_VcAuqOSFlIdCZxrtonIv0d6zMz_a1RQhKr_lo0VAAni49zgzJEE6V1Qv5bpd', start_index=1390)
Annotation(end_index=1402, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzeqp1EZ_omw2RMRuI30B-3cXt8jpwpb7KhvkB9S75ZUqLFPbQlhgo-Dw46vhiIT2UX3oihhXtzAGfbpqTWhgDo0wvmMYqDep7hqTpofJO7gqASRqUF4ApWumHdlitRcy6BOyFADprcEweNi0v02Km6S7H0rdx1Int6Gs=', start_index=1390)
Annotation(end_index=1751, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyXY_y-C_GO6No6GobscQiRSDjShUWyCB8yki2QxyJfgAgPLq627Z5LboNDHYaYgz5Yo5UiIE8HXXu5HkLT5Jef03RrYAAkMt3R5dKE79ZHwkrcq2JTvKZLmNhAPrkSjaLqfHnOcP6hmwCsr0pSbSE8tcXM9oVZj8dg3nlc_kUIiCoKNC1CR--lRTwkyAOCgGKMjLtX9MHzqN3tQ1k7x4=', start_index=1739)
Annotation(end_index=1751, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUeyA3h85GqUNFPt9L-tFSEk_ICqgps9ppcmclSjnUeE1P2Y_xyj0OJkw-3ax2986kFe-yNbrJxMxyumEwV6GemUFp7lhh5lnLYNmqKFwtLuTHEhx4', start_index=1739)
Annotation(end_index=2217, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2pbXrd6-gbeYlGjUrPAF-OLBs5MCj_wg0kk-omVDlk8X_tMen7HS0k83x1MPTlozp_vaPUeNN7SeUEZa7GESZHcckehR7NL1cwsv4QPcmiPrbOOV7nVth1WgI697qU11StfrSN0C8bg5YbLCXgXO0qKQ=', start_index=2204)
Annotation(end_index=2217, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbb0etVF0-RIDogAYGcdqROSTSlog7e-iCMzrYUneocL5aNz6TIPndSCefUwkUKn9HxGj8jhsWOgUJmEAzGeLE9tcnF1F4KlTfzDA1dYLaFMBT-kt6Gy0zI99P15P4flnrHslwKht8Z_Qbia3mlIyzajAo_HSI48v-DE_gAJKfSRmXQ1avHTf9ymYCURnx_I89mXO3lV1-U_v3Sb-HhbgauhLsHgIR2G5J3zdARd2v0AY66UKteq5LhKN_8GYLqGBYKbqK8y3oCPUiIRg846msmM7seha7brr2G3lnwhI=', start_index=2204)
Annotation(end_index=2729, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESb45kjQoKZs21-FtUzMm_EzKsds1cqdyQxdXww6DsJlgRX5t0ZBdGX_QK-eVkz0UE-cTbjHOTR-Saq1kJmsrDcfBC23uFglcbq_zssywrUydfsAoCLk1KIEGc55XJW21xa_Y=', start_index=2715)
Annotation(end_index=2729, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExSmxNSkZTQoKCjpBBA4rQYjCO8scihwM-bt9-0n3WOBVeNlg63AsNbnpWCyMhNJy4tSDgcfvfXj-dafhUCDWSMEIsmD-CE-24iOsyevfOxTwvCgluWMpkrNzBw-DHNqjxUkIjbd_F5mgK6kzaxfTFHltIZuA90p30DP1JuO6E1AKZBXry8loeyIG1G1zVXfA=', start_index=2715)
Annotation(end_index=3582, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE39i18IX4CrxNidl3_QnlLwP0R4qthmfXPX4mdpkHbI_iTwJTOqPBpLf-LkpwJTL617EDukXJQQpoivT8Hq0BMaHHQ7KHSNVL9HP3PWsCxenrVB6S09hw5EOiAv8QuTlkoA0Fy4HhEuvwvtn-b7J_L6nWwOcqg21TDN0RIxhagtR_HtQ==', start_index=3569)
Annotation(end_index=3582, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUeyA3h85GqUNFPt9L-tFSEk_ICqgps9ppcmclSjnUeE1P2Y_xyj0OJkw-3ax2986kFe-yNbrJxMxyumEwV6GemUFp7lhh5lnLYNmqKFwtLuTHEhx4', start_index=3569)
Annotation(end_index=4055, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGb7o-w2-hi5Uv6aTeobTbj9AeN-lnoeKGXxdBXMdp4Tc9jLiazTxe6uSCRtyIJngo0bjK_-T2POuChobW-r02Dln5N8r02WRBWeh_Ftjf83fJluuagSOjvP6bIC-4eBzBxPa5BsYgHIfxi5ljcO0QKZHbQn2zXR7wNWxxaHCRZl5RH5PRRN8Qi-JHLetcj6VrziBrNlb5ak-rZDTcss48NrKyiczKaeU9J0O5ylXuA', start_index=4041)
Annotation(end_index=4055, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpFWrS30l6FphabGq6CGI-Xh-vE7TenOtKBWfA-enFs7EjZTa8kVHZnGLdV6TwqQosVg46fMn_4ntmVviEPYRQK-K0bzVwktN0WhI16vMYT5-1oHNFcwcUEHdCgSBTJPKbVSX_WQxh3MQCrRaNV2Ufgx4k_8cu_Tct8xyNowebekvuFzCNNZkDPP9y_jh3-iaKYWeNjTgK23ut0-U=', start_index=4041)
Annotation(end_index=4420, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExSmxNSkZTQoKCjpBBA4rQYjCO8scihwM-bt9-0n3WOBVeNlg63AsNbnpWCyMhNJy4tSDgcfvfXj-dafhUCDWSMEIsmD-CE-24iOsyevfOxTwvCgluWMpkrNzBw-DHNqjxUkIjbd_F5mgK6kzaxfTFHltIZuA90p30DP1JuO6E1AKZBXry8loeyIG1G1zVXfA=', start_index=4406)
Annotation(end_index=4420, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbKm6vMTPLVpmR0L_okArADg2zbnHUt1oAPsowBWRU9VvPrSWoOJJgZMBJEOSfFeWqnqbf9Xd6Ve_ruL9Z7n07mkZPupzX8lW3lx54I6CoOJyfHRITHk51O7VccoAg-EjDPKqL3l7WoYkHeXI=', start_index=4406)
Annotation(end_index=4770, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6GvWKtPdCxGcHm-gZjyehTj8Iy7e_MnFWYw1xh5ihoXO8b2PlImzYbLWraEnSDTXp4XR9_yofcxtBPFaIfdjoOxyognNeo75-jraG2Cna8IoNklJysl-lggYvpAwH2ds=', start_index=4756)
Annotation(end_index=4770, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHZykpVCOmXvoF8KA7dRy6QCmQ1uwVW8b_kEBieT9eynkW8ILJdgzCOKIkelE69CxorQ8k0jdSf49TQhePpFP7V65HkF5oAGTiwOofZKWCSWSex_p30s8YEy0MbydIHkqnb8j6s_PJRb9M-3ZXzMFU36izv7jkW2GzmGJ2lLM=', start_index=4756)
Annotation(end_index=5170, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExSmxNSkZTQoKCjpBBA4rQYjCO8scihwM-bt9-0n3WOBVeNlg63AsNbnpWCyMhNJy4tSDgcfvfXj-dafhUCDWSMEIsmD-CE-24iOsyevfOxTwvCgluWMpkrNzBw-DHNqjxUkIjbd_F5mgK6kzaxfTFHltIZuA90p30DP1JuO6E1AKZBXry8loeyIG1G1zVXfA=', start_index=5156)
Annotation(end_index=5170, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGb7o-w2-hi5Uv6aTeobTbj9AeN-lnoeKGXxdBXMdp4Tc9jLiazTxe6uSCRtyIJngo0bjK_-T2POuChobW-r02Dln5N8r02WRBWeh_Ftjf83fJluuagSOjvP6bIC-4eBzBxPa5BsYgHIfxi5ljcO0QKZHbQn2zXR7wNWxxaHCRZl5RH5PRRN8Qi-JHLetcj6VrziBrNlb5ak-rZDTcss48NrKyiczKaeU9J0O5ylXuA', start_index=5156)
Annotation(end_index=5369, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6GvWKtPdCxGcHm-gZjyehTj8Iy7e_MnFWYw1xh5ihoXO8b2PlImzYbLWraEnSDTXp4XR9_yofcxtBPFaIfdjoOxyognNeo75-jraG2Cna8IoNklJysl-lggYvpAwH2ds=', start_index=5356)
Annotation(end_index=5369, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDvKRQe5i30D6s0M8yZtQzCKtRv0mcy4dQMQSTYIzCdqdhd_rGT7tZRm1hhaRWxeFxm8wMJUE1PXuTcHQd9FFFreLzY61ZIjK7zU96WVxOprJlcGrMl8qKxf6OiRT6srE=', start_index=5356)
Annotation(end_index=5726, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEC3oz_RWNMXYsB_nI5OMZUrPzeHNGHvCME2fT5UTpM1D2ape8h1OoasiQAIlzvbU_DQud8jW-OdEtquuLeNvijI67vM7OaMQjlqFDFrLvpBAzzNpSmA5Lrt3m4nGZKzK0=', start_index=5712)
Annotation(end_index=5726, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGb7o-w2-hi5Uv6aTeobTbj9AeN-lnoeKGXxdBXMdp4Tc9jLiazTxe6uSCRtyIJngo0bjK_-T2POuChobW-r02Dln5N8r02WRBWeh_Ftjf83fJluuagSOjvP6bIC-4eBzBxPa5BsYgHIfxi5ljcO0QKZHbQn2zXR7wNWxxaHCRZl5RH5PRRN8Qi-JHLetcj6VrziBrNlb5ak-rZDTcss48NrKyiczKaeU9J0O5ylXuA', start_index=5712)
Annotation(end_index=6257, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9w79MscHp5h5HrHE7XOMm69puJYVCQk_uiJcWDqDbdGZktjBF79LdE5Up23tbQn4XaAwnQLwFaTLvc3uEGO3XDuQ6fyp4FKkJ4B2mrEKQVPgNDg36YDurzL_ehuXuh8aGfA==', start_index=6244)
Annotation(end_index=6257, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzeqp1EZ_omw2RMRuI30B-3cXt8jpwpb7KhvkB9S75ZUqLFPbQlhgo-Dw46vhiIT2UX3oihhXtzAGfbpqTWhgDo0wvmMYqDep7hqTpofJO7gqASRqUF4ApWumHdlitRcy6BOyFADprcEweNi0v02Km6S7H0rdx1Int6Gs=', start_index=6244)
Annotation(end_index=6548, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvstHmGl7x5WbvY19Xyv4_7HtKdBuTkXDWuCUZ3MaDS8p-mx3tjH1MJpFHw4j3qPhWLiBgVNFOlantX_XsXg--6jrcKYoewmwldmj5Dd0_VcAuqOSFlIdCZxrtonIv0d6zMz_a1RQhKr_lo0VAAni49zgzJEE6V1Qv5bpd', start_index=6536)
Annotation(end_index=6548, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbb0etVF0-RIDogAYGcdqROSTSlog7e-iCMzrYUneocL5aNz6TIPndSCefUwkUKn9HxGj8jhsWOgUJmEAzGeLE9tcnF1F4KlTfzDA1dYLaFMBT-kt6Gy0zI99P15P4flnrHslwKht8Z_Qbia3mlIyzajAo_HSI48v-DE_gAJKfSRmXQ1avHTf9ymYCURnx_I89mXO3lV1-U_v3Sb-HhbgauhLsHgIR2G5J3zdARd2v0AY66UKteq5LhKN_8GYLqGBYKbqK8y3oCPUiIRg846msmM7seha7brr2G3lnwhI=', start_index=6536)
Annotation(end_index=6858, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTtw5qhcyqpA5GbM7JGnidCKD6QapOqUO7ojnkezwBYBkJHWvMKgTKW4BhEp7BigQjWGsKXH2QmxWWmyC_cDvtR7YcN-Ei617WuQFBsbPouS20DHQBzNL1Nu10WhF1XaH3h0ECZZJ8eA49uQkmxiB-m5QCoAoQS-dQpW8nvLeD08ubT_SygRG3P4q8g0IeSlRMJe4yJGxqf0VWBA==', start_index=6844)
Annotation(end_index=6858, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGb7o-w2-hi5Uv6aTeobTbj9AeN-lnoeKGXxdBXMdp4Tc9jLiazTxe6uSCRtyIJngo0bjK_-T2POuChobW-r02Dln5N8r02WRBWeh_Ftjf83fJluuagSOjvP6bIC-4eBzBxPa5BsYgHIfxi5ljcO0QKZHbQn2zXR7wNWxxaHCRZl5RH5PRRN8Qi-JHLetcj6VrziBrNlb5ak-rZDTcss48NrKyiczKaeU9J0O5ylXuA', start_index=6844)
Annotation(end_index=7028, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbb0etVF0-RIDogAYGcdqROSTSlog7e-iCMzrYUneocL5aNz6TIPndSCefUwkUKn9HxGj8jhsWOgUJmEAzGeLE9tcnF1F4KlTfzDA1dYLaFMBT-kt6Gy0zI99P15P4flnrHslwKht8Z_Qbia3mlIyzajAo_HSI48v-DE_gAJKfSRmXQ1avHTf9ymYCURnx_I89mXO3lV1-U_v3Sb-HhbgauhLsHgIR2G5J3zdARd2v0AY66UKteq5LhKN_8GYLqGBYKbqK8y3oCPUiIRg846msmM7seha7brr2G3lnwhI=', start_index=7019)
Annotation(end_index=7229, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEesM21hTJRbWhwuzxq3xLs1WS9Ia79t-u28BIQzGd1FFxgf5RNI6-ocNGcLbfz_6joB81nMPvOZZUpEiBebD-i0oeq4hFKFVIvU26auTOwN0nzP4KSmglBAJE-8YPwTEv4zD6gEZkSxnpzN9Zbu3jlwIhd0N7JHLq9_d3jYA==', start_index=7219)
Annotation(end_index=7923, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETSh_eCN6LZkTYSNDme1phmEHFBhamK9aAzETim6vOyj2wiwGmwRGY9tLDmD7M_HK3aYW79R-bHY9LjTZ6CN-Tq0YCv8ro1QlTu3_XHMYC8qNjKJATQUNEdOVHMRUjUn0u8ajkB4caoSrP', start_index=7910)
Annotation(end_index=7923, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzeqp1EZ_omw2RMRuI30B-3cXt8jpwpb7KhvkB9S75ZUqLFPbQlhgo-Dw46vhiIT2UX3oihhXtzAGfbpqTWhgDo0wvmMYqDep7hqTpofJO7gqASRqUF4ApWumHdlitRcy6BOyFADprcEweNi0v02Km6S7H0rdx1Int6Gs=', start_index=7910)
Annotation(end_index=8158, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzeqp1EZ_omw2RMRuI30B-3cXt8jpwpb7KhvkB9S75ZUqLFPbQlhgo-Dw46vhiIT2UX3oihhXtzAGfbpqTWhgDo0wvmMYqDep7hqTpofJO7gqASRqUF4ApWumHdlitRcy6BOyFADprcEweNi0v02Km6S7H0rdx1Int6Gs=', start_index=8149)
Annotation(end_index=9283, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCjTvpXauxqsDvqnj_W8ljBOCwRwjaXCP6Sy2p8pK6bkbh7Z5dXQEhaLal_Vt_CTLtCyMiEFxJwTlYzbENbuT6tOmvLIw1yrXXpe_g-BbIsS69TXOoj6dgNF0=', start_index=9269)
Annotation(end_index=9283, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMKHfi-JRtZb2z2F7nv3qNsyC6f2Sd1GreYeSLW3bAwbM4ETKl12XuqB9wp93aFPN4eLU2z43zWYtc-ADTVljkPFq_QeluJKGYhJZ4IV2PLTr87Rrrvn5qMiV44g==', start_index=9269)
Annotation(end_index=9693, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAYrlhpuRAAgJ9u9LBI_sCGjKjlw42DF-v8Y3IUehQ_VXXrgry2qliwkoti8sa-9BHwzADFgNZw4ZxET-VvZldAGeEwKcu2-9-xMBntcv_K1PNmiJDNlzX3iRBQK1jSwEj8ZR0OMee19rw6aCIKkjSX-oLSPFxqExp-8y9', start_index=9683)
Annotation(end_index=10010, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzeqp1EZ_omw2RMRuI30B-3cXt8jpwpb7KhvkB9S75ZUqLFPbQlhgo-Dw46vhiIT2UX3oihhXtzAGfbpqTWhgDo0wvmMYqDep7hqTpofJO7gqASRqUF4ApWumHdlitRcy6BOyFADprcEweNi0v02Km6S7H0rdx1Int6Gs=', start_index=10001)
Annotation(end_index=10579, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6GvWKtPdCxGcHm-gZjyehTj8Iy7e_MnFWYw1xh5ihoXO8b2PlImzYbLWraEnSDTXp4XR9_yofcxtBPFaIfdjoOxyognNeo75-jraG2Cna8IoNklJysl-lggYvpAwH2ds=', start_index=10569)
Annotation(end_index=10984, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-_fGDGtfVKIHb2bu8hdUBEkkP0XE3vYr6Z1MCxEDWwcEH3P2AeMZ-gdzbw099PPmW-ugdEWDKNjytkrhFUp6yYKZS_pqD-M1ybr_QVy48qYp6n83s', start_index=10975)
Annotation(end_index=11260, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGb7o-w2-hi5Uv6aTeobTbj9AeN-lnoeKGXxdBXMdp4Tc9jLiazTxe6uSCRtyIJngo0bjK_-T2POuChobW-r02Dln5N8r02WRBWeh_Ftjf83fJluuagSOjvP6bIC-4eBzBxPa5BsYgHIfxi5ljcO0QKZHbQn2zXR7wNWxxaHCRZl5RH5PRRN8Qi-JHLetcj6VrziBrNlb5ak-rZDTcss48NrKyiczKaeU9J0O5ylXuA', start_index=11250)
Annotation(end_index=11726, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmrLU7itm4rU7K-Qaq9-ceeWpKSIcmW7uaXA4gzzQnBCgLwyD1rCbixmWz-RslRhATutn0SBvTuJhssMj-mNuNC1tmHL-D2eLgAnEA9dHEcCiOtLhXPyXdXV3vpUe-IfdPOPVnqVyS03KPCfNeS7PmxcbLwO8-QX4mmXjOekhiwaRpLzvOrm1R-sT_1aXV4CnjBOdRQtcEh2egjKA8ppLmEB7SIlogvcbSZMhrX8y9DjzBwIH1OyFgXS33_JdotREKT5mQb-3Kq_2-zGUId8nDvvbYklxvEVUrrKiTFEWyqDBu-dL4H-BZ5hGRINV5VKE=', start_index=11712)
Annotation(end_index=11726, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmOZMji_BwJfS4nC6tgoSmtICB_ioCbEGNbyFHu0FCuleIsU2YveBWQMrhoAesRRr_5hfSsD7S55nKm1WUtnTPV3oFBgBpxk3PF7RjgZblARbhvCJmeC4mmox8wQ==', start_index=11712)
Annotation(end_index=12050, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9w79MscHp5h5HrHE7XOMm69puJYVCQk_uiJcWDqDbdGZktjBF79LdE5Up23tbQn4XaAwnQLwFaTLvc3uEGO3XDuQ6fyp4FKkJ4B2mrEKQVPgNDg36YDurzL_ehuXuh8aGfA==', start_index=12037)
Annotation(end_index=12050, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpoXV8EkGwmT9SITRS6m-GIKBwMVDNfOXPWaE5DO1JaDqzDA4wlQZMZVO_GjszNXRrzaPt466uv-YUnPRMaqHaiX0Hei1UZRZPmjcOqykgNmWAU3h7uXscKbQW24gpf1o4wwKBVYb9GtriusimgQZKicTCJVLf-DOH2FjeKsE=', start_index=12037)
Annotation(end_index=12953, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyXY_y-C_GO6No6GobscQiRSDjShUWyCB8yki2QxyJfgAgPLq627Z5LboNDHYaYgz5Yo5UiIE8HXXu5HkLT5Jef03RrYAAkMt3R5dKE79ZHwkrcq2JTvKZLmNhAPrkSjaLqfHnOcP6hmwCsr0pSbSE8tcXM9oVZj8dg3nlc_kUIiCoKNC1CR--lRTwkyAOCgGKMjLtX9MHzqN3tQ1k7x4=', start_index=12940)
Annotation(end_index=12953, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGICXat3kn6-DLQonuuTNHZ2CSXoWEfYE7bYHM1hH8ihpo4ZgrtDv1TeYgVmw0cif7QEe0YCoerzq0VuInmzcpVYT4zllBSBGookB5OEicpVJ4OwTRGEMpU0J1-jAumnl26G0Lwd7coeeqMlNQKEg2reJRYLLQ6JC4LIvMqNrrl7SfC3r2OVbPO8gl8dad-H9KjcHXJ96gYRt3A-6wetE9rL2hA', start_index=12940)
Annotation(end_index=13313, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE39i18IX4CrxNidl3_QnlLwP0R4qthmfXPX4mdpkHbI_iTwJTOqPBpLf-LkpwJTL617EDukXJQQpoivT8Hq0BMaHHQ7KHSNVL9HP3PWsCxenrVB6S09hw5EOiAv8QuTlkoA0Fy4HhEuvwvtn-b7J_L6nWwOcqg21TDN0RIxhagtR_HtQ==', start_index=13299)
Annotation(end_index=13313, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGICXat3kn6-DLQonuuTNHZ2CSXoWEfYE7bYHM1hH8ihpo4ZgrtDv1TeYgVmw0cif7QEe0YCoerzq0VuInmzcpVYT4zllBSBGookB5OEicpVJ4OwTRGEMpU0J1-jAumnl26G0Lwd7coeeqMlNQKEg2reJRYLLQ6JC4LIvMqNrrl7SfC3r2OVbPO8gl8dad-H9KjcHXJ96gYRt3A-6wetE9rL2hA', start_index=13299)
Annotation(end_index=13932, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfJhLH4MLu1kXbRyDbcXD00ZM3KaUJQls813z6w8wm11xy3zQ_hxVKhc-4BitlhBc6Tbbg_8GHopefzawAzi4wZzrCS7cAUD0yVO_uflMoYTVYoCQF', start_index=13915)
Annotation(end_index=13932, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnsHnYHGsDZl7iWsOM463bRX9OQZ9Kbf5Az8Qz6bQasl0lELKBqOnxJhwDcLLnpBSP1cUj-_5_HyFEllxm-Te_7-jgvx5kAAx0flhsWMJfLyoWk6DZgV7p', start_index=13915)
Annotation(end_index=13932, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUeyA3h85GqUNFPt9L-tFSEk_ICqgps9ppcmclSjnUeE1P2Y_xyj0OJkw-3ax2986kFe-yNbrJxMxyumEwV6GemUFp7lhh5lnLYNmqKFwtLuTHEhx4', start_index=13915)
Annotation(end_index=14299, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHZykpVCOmXvoF8KA7dRy6QCmQ1uwVW8b_kEBieT9eynkW8ILJdgzCOKIkelE69CxorQ8k0jdSf49TQhePpFP7V65HkF5oAGTiwOofZKWCSWSex_p30s8YEy0MbydIHkqnb8j6s_PJRb9M-3ZXzMFU36izv7jkW2GzmGJ2lLM=', start_index=14286)
Annotation(end_index=14299, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDvKRQe5i30D6s0M8yZtQzCKtRv0mcy4dQMQSTYIzCdqdhd_rGT7tZRm1hhaRWxeFxm8wMJUE1PXuTcHQd9FFFreLzY61ZIjK7zU96WVxOprJlcGrMl8qKxf6OiRT6srE=', start_index=14286)
Annotation(end_index=14746, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTtw5qhcyqpA5GbM7JGnidCKD6QapOqUO7ojnkezwBYBkJHWvMKgTKW4BhEp7BigQjWGsKXH2QmxWWmyC_cDvtR7YcN-Ei617WuQFBsbPouS20DHQBzNL1Nu10WhF1XaH3h0ECZZJ8eA49uQkmxiB-m5QCoAoQS-dQpW8nvLeD08ubT_SygRG3P4q8g0IeSlRMJe4yJGxqf0VWBA==', start_index=14733)
Annotation(end_index=14746, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzeqp1EZ_omw2RMRuI30B-3cXt8jpwpb7KhvkB9S75ZUqLFPbQlhgo-Dw46vhiIT2UX3oihhXtzAGfbpqTWhgDo0wvmMYqDep7hqTpofJO7gqASRqUF4ApWumHdlitRcy6BOyFADprcEweNi0v02Km6S7H0rdx1Int6Gs=', start_index=14733)
Annotation(end_index=15026, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbKm6vMTPLVpmR0L_okArADg2zbnHUt1oAPsowBWRU9VvPrSWoOJJgZMBJEOSfFeWqnqbf9Xd6Ve_ruL9Z7n07mkZPupzX8lW3lx54I6CoOJyfHRITHk51O7VccoAg-EjDPKqL3l7WoYkHeXI=', start_index=15012)
Annotation(end_index=15026, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfTAj6kN_FkiEpj7O27rz6GI6k6j8SZnWHzEVxlRbas-6jIbvN1YmsgbM3kYgUlAsRvYrOa69-lxNl9cFh7UzJOT9hWJ_5AgPWYRemMgMAspq3wIcxwnQ_KEfg7cjmuxE=', start_index=15012)
Annotation(end_index=15661, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvstHmGl7x5WbvY19Xyv4_7HtKdBuTkXDWuCUZ3MaDS8p-mx3tjH1MJpFHw4j3qPhWLiBgVNFOlantX_XsXg--6jrcKYoewmwldmj5Dd0_VcAuqOSFlIdCZxrtonIv0d6zMz_a1RQhKr_lo0VAAni49zgzJEE6V1Qv5bpd', start_index=15649)
Annotation(end_index=15661, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbb0etVF0-RIDogAYGcdqROSTSlog7e-iCMzrYUneocL5aNz6TIPndSCefUwkUKn9HxGj8jhsWOgUJmEAzGeLE9tcnF1F4KlTfzDA1dYLaFMBT-kt6Gy0zI99P15P4flnrHslwKht8Z_Qbia3mlIyzajAo_HSI48v-DE_gAJKfSRmXQ1avHTf9ymYCURnx_I89mXO3lV1-U_v3Sb-HhbgauhLsHgIR2G5J3zdARd2v0AY66UKteq5LhKN_8GYLqGBYKbqK8y3oCPUiIRg846msmM7seha7brr2G3lnwhI=', start_index=15649)
Annotation(end_index=16259, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAYrlhpuRAAgJ9u9LBI_sCGjKjlw42DF-v8Y3IUehQ_VXXrgry2qliwkoti8sa-9BHwzADFgNZw4ZxET-VvZldAGeEwKcu2-9-xMBntcv_K1PNmiJDNlzX3iRBQK1jSwEj8ZR0OMee19rw6aCIKkjSX-oLSPFxqExp-8y9', start_index=16245)
Annotation(end_index=16259, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMKHfi-JRtZb2z2F7nv3qNsyC6f2Sd1GreYeSLW3bAwbM4ETKl12XuqB9wp93aFPN4eLU2z43zWYtc-ADTVljkPFq_QeluJKGYhJZ4IV2PLTr87Rrrvn5qMiV44g==', start_index=16245)
Annotation(end_index=16607, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE39i18IX4CrxNidl3_QnlLwP0R4qthmfXPX4mdpkHbI_iTwJTOqPBpLf-LkpwJTL617EDukXJQQpoivT8Hq0BMaHHQ7KHSNVL9HP3PWsCxenrVB6S09hw5EOiAv8QuTlkoA0Fy4HhEuvwvtn-b7J_L6nWwOcqg21TDN0RIxhagtR_HtQ==', start_index=16591)
Annotation(end_index=16607, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyXY_y-C_GO6No6GobscQiRSDjShUWyCB8yki2QxyJfgAgPLq627Z5LboNDHYaYgz5Yo5UiIE8HXXu5HkLT5Jef03RrYAAkMt3R5dKE79ZHwkrcq2JTvKZLmNhAPrkSjaLqfHnOcP6hmwCsr0pSbSE8tcXM9oVZj8dg3nlc_kUIiCoKNC1CR--lRTwkyAOCgGKMjLtX9MHzqN3tQ1k7x4=', start_index=16591)
Annotation(end_index=16607, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUeyA3h85GqUNFPt9L-tFSEk_ICqgps9ppcmclSjnUeE1P2Y_xyj0OJkw-3ax2986kFe-yNbrJxMxyumEwV6GemUFp7lhh5lnLYNmqKFwtLuTHEhx4', start_index=16591)
Annotation(end_index=17030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEt1kzClYjDiCLRub9lRLHCYoiEg79ZVcGlfBRYpFS0-CkPMUUGl1A5VCO9QyXPThPfWV6hztXoUgiVdvuD24qocVyxPuA6AVih65RLfDxpHshIAPDaRKZDvy4o2hy8j1PjoG78Hm754h_73csqfl_8GSB8O8vP5IoYBMBLeJKUdYl25zWQZy0CBUIGZkuhRxzXumuNmtdIEVIaPbum4yEB61wCkWe8ZmNMiRYKURvCmWrzD1_xufDNTEKScPhiL-lvcWLw', start_index=17021)
Annotation(end_index=17121, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHZykpVCOmXvoF8KA7dRy6QCmQ1uwVW8b_kEBieT9eynkW8ILJdgzCOKIkelE69CxorQ8k0jdSf49TQhePpFP7V65HkF5oAGTiwOofZKWCSWSex_p30s8YEy0MbydIHkqnb8j6s_PJRb9M-3ZXzMFU36izv7jkW2GzmGJ2lLM=', start_index=17111)
Annotation(end_index=17225, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpFWrS30l6FphabGq6CGI-Xh-vE7TenOtKBWfA-enFs7EjZTa8kVHZnGLdV6TwqQosVg46fMn_4ntmVviEPYRQK-K0bzVwktN0WhI16vMYT5-1oHNFcwcUEHdCgSBTJPKbVSX_WQxh3MQCrRaNV2Ufgx4k_8cu_Tct8xyNowebekvuFzCNNZkDPP9y_jh3-iaKYWeNjTgK23ut0-U=', start_index=17215)
Annotation(end_index=17337, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3HyO3cLXMpfdyJzgmYQVz_t3YHowGPtD-nBoX9kIzGUX4wYrKcSUWLkjUQ35ksix4D8Pv5tZQAUj0yqlXBU_eSVA3g_VN3TkKbzwl-q9WalnQZx798_Sn-haxg4bt-ns=', start_index=17327)
Annotation(end_index=17466, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExSmxNSkZTQoKCjpBBA4rQYjCO8scihwM-bt9-0n3WOBVeNlg63AsNbnpWCyMhNJy4tSDgcfvfXj-dafhUCDWSMEIsmD-CE-24iOsyevfOxTwvCgluWMpkrNzBw-DHNqjxUkIjbd_F5mgK6kzaxfTFHltIZuA90p30DP1JuO6E1AKZBXry8loeyIG1G1zVXfA=', start_index=17456)
Annotation(end_index=17570, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDvKRQe5i30D6s0M8yZtQzCKtRv0mcy4dQMQSTYIzCdqdhd_rGT7tZRm1hhaRWxeFxm8wMJUE1PXuTcHQd9FFFreLzY61ZIjK7zU96WVxOprJlcGrMl8qKxf6OiRT6srE=', start_index=17561)
Annotation(end_index=17686, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUeyA3h85GqUNFPt9L-tFSEk_ICqgps9ppcmclSjnUeE1P2Y_xyj0OJkw-3ax2986kFe-yNbrJxMxyumEwV6GemUFp7lhh5lnLYNmqKFwtLuTHEhx4', start_index=17677)
Annotation(end_index=17804, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjR_KEIV8U9krcRHpb0kZSDCpUQ2KK-vpXZ2-P9PfwXv24dIyQEkScKQGBTUmiaZs5zmKRxmkwnOXVYJL_7lS6c9lp-nKu40V6J7WeARACEezjEcDTBtNk', start_index=17794)
Annotation(end_index=17890, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6GvWKtPdCxGcHm-gZjyehTj8Iy7e_MnFWYw1xh5ihoXO8b2PlImzYbLWraEnSDTXp4XR9_yofcxtBPFaIfdjoOxyognNeo75-jraG2Cna8IoNklJysl-lggYvpAwH2ds=', start_index=17880)
Annotation(end_index=18012, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGb7o-w2-hi5Uv6aTeobTbj9AeN-lnoeKGXxdBXMdp4Tc9jLiazTxe6uSCRtyIJngo0bjK_-T2POuChobW-r02Dln5N8r02WRBWeh_Ftjf83fJluuagSOjvP6bIC-4eBzBxPa5BsYgHIfxi5ljcO0QKZHbQn2zXR7wNWxxaHCRZl5RH5PRRN8Qi-JHLetcj6VrziBrNlb5ak-rZDTcss48NrKyiczKaeU9J0O5ylXuA', start_index=18002)
Annotation(end_index=18133, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmOZMji_BwJfS4nC6tgoSmtICB_ioCbEGNbyFHu0FCuleIsU2YveBWQMrhoAesRRr_5hfSsD7S55nKm1WUtnTPV3oFBgBpxk3PF7RjgZblARbhvCJmeC4mmox8wQ==', start_index=18123)
Annotation(end_index=18240, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmrLU7itm4rU7K-Qaq9-ceeWpKSIcmW7uaXA4gzzQnBCgLwyD1rCbixmWz-RslRhATutn0SBvTuJhssMj-mNuNC1tmHL-D2eLgAnEA9dHEcCiOtLhXPyXdXV3vpUe-IfdPOPVnqVyS03KPCfNeS7PmxcbLwO8-QX4mmXjOekhiwaRpLzvOrm1R-sT_1aXV4CnjBOdRQtcEh2egjKA8ppLmEB7SIlogvcbSZMhrX8y9DjzBwIH1OyFgXS33_JdotREKT5mQb-3Kq_2-zGUId8nDvvbYklxvEVUrrKiTFEWyqDBu-dL4H-BZ5hGRINV5VKE=', start_index=18230)
Annotation(end_index=18386, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfTAj6kN_FkiEpj7O27rz6GI6k6j8SZnWHzEVxlRbas-6jIbvN1YmsgbM3kYgUlAsRvYrOa69-lxNl9cFh7UzJOT9hWJ_5AgPWYRemMgMAspq3wIcxwnQ_KEfg7cjmuxE=', start_index=18376)
Annotation(end_index=18512, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEesM21hTJRbWhwuzxq3xLs1WS9Ia79t-u28BIQzGd1FFxgf5RNI6-ocNGcLbfz_6joB81nMPvOZZUpEiBebD-i0oeq4hFKFVIvU26auTOwN0nzP4KSmglBAJE-8YPwTEv4zD6gEZkSxnpzN9Zbu3jlwIhd0N7JHLq9_d3jYA==', start_index=18502)
Annotation(end_index=18595, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvstHmGl7x5WbvY19Xyv4_7HtKdBuTkXDWuCUZ3MaDS8p-mx3tjH1MJpFHw4j3qPhWLiBgVNFOlantX_XsXg--6jrcKYoewmwldmj5Dd0_VcAuqOSFlIdCZxrtonIv0d6zMz_a1RQhKr_lo0VAAni49zgzJEE6V1Qv5bpd', start_index=18586)
Annotation(end_index=18660, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzeqp1EZ_omw2RMRuI30B-3cXt8jpwpb7KhvkB9S75ZUqLFPbQlhgo-Dw46vhiIT2UX3oihhXtzAGfbpqTWhgDo0wvmMYqDep7hqTpofJO7gqASRqUF4ApWumHdlitRcy6BOyFADprcEweNi0v02Km6S7H0rdx1Int6Gs=', start_index=18651)
Annotation(end_index=18761, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9w79MscHp5h5HrHE7XOMm69puJYVCQk_uiJcWDqDbdGZktjBF79LdE5Up23tbQn4XaAwnQLwFaTLvc3uEGO3XDuQ6fyp4FKkJ4B2mrEKQVPgNDg36YDurzL_ehuXuh8aGfA==', start_index=18751)
Annotation(end_index=18864, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTtw5qhcyqpA5GbM7JGnidCKD6QapOqUO7ojnkezwBYBkJHWvMKgTKW4BhEp7BigQjWGsKXH2QmxWWmyC_cDvtR7YcN-Ei617WuQFBsbPouS20DHQBzNL1Nu10WhF1XaH3h0ECZZJ8eA49uQkmxiB-m5QCoAoQS-dQpW8nvLeD08ubT_SygRG3P4q8g0IeSlRMJe4yJGxqf0VWBA==', start_index=18854)
Annotation(end_index=18958, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFancGSoA2DDdFjqkrLc_V38EH0CW3wtX7t1uXdPulycM_JmcTzgDbPcSvn1sV8e1G1w8vu5hlv0x9xrd5gAWGYNT70A3UMSU31K8zG_4en1GxYNF6yM-zNrTk_AXoCRIAKt_K2uvJyzFoH8dHUACOv3GKJmjRVEBPjhcc4CsAXfm--uqOFHTa2to2bRHylnozllA==', start_index=18948)
Annotation(end_index=19042, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbKm6vMTPLVpmR0L_okArADg2zbnHUt1oAPsowBWRU9VvPrSWoOJJgZMBJEOSfFeWqnqbf9Xd6Ve_ruL9Z7n07mkZPupzX8lW3lx54I6CoOJyfHRITHk51O7VccoAg-EjDPKqL3l7WoYkHeXI=', start_index=19032)
Annotation(end_index=19099, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpoXV8EkGwmT9SITRS6m-GIKBwMVDNfOXPWaE5DO1JaDqzDA4wlQZMZVO_GjszNXRrzaPt466uv-YUnPRMaqHaiX0Hei1UZRZPmjcOqykgNmWAU3h7uXscKbQW24gpf1o4wwKBVYb9GtriusimgQZKicTCJVLf-DOH2FjeKsE=', start_index=19090)
Annotation(end_index=19182, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMKHfi-JRtZb2z2F7nv3qNsyC6f2Sd1GreYeSLW3bAwbM4ETKl12XuqB9wp93aFPN4eLU2z43zWYtc-ADTVljkPFq_QeluJKGYhJZ4IV2PLTr87Rrrvn5qMiV44g==', start_index=19172)
Annotation(end_index=19254, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCjTvpXauxqsDvqnj_W8ljBOCwRwjaXCP6Sy2p8pK6bkbh7Z5dXQEhaLal_Vt_CTLtCyMiEFxJwTlYzbENbuT6tOmvLIw1yrXXpe_g-BbIsS69TXOoj6dgNF0=', start_index=19244)
Annotation(end_index=19333, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_s95IE3U7tV_oPCUK8kkX9hsag75M5OUo2geuGqE0pwWhLflL8hXoWQwaXGZA3L_lflvWG39nZQhqvnr1ks_v_00fWwKXvYQwDuW4We7eKcZuh0QZKKn4oZsnKQUDTCFA3pS-kfe5UBOBXwKIjb1_rf2TzQFlZjQkYC_9DwGaAW6_pYePimVO9SZEBMD_cFVHZgznTH819dEKvs8a8EycG6h_zbSZkxBUPP_KQMKdwCIOvg==', start_index=19323)
Annotation(end_index=19467, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9b3fF7I3jiorfSJStmBqTIxIe1jxGng-izMFodZkzLK03gs-Hg1tEuNTgIgNe1Rbk3dQ0qI5U0qZRUQ1tDlPAVYBfjQOeXpkiy-Um6QFXpPojbk1etE6dbinxfojFFmu7sl_0UWtXnB_DrypvJkYJ6rJcTjW1FnqitgYzKg==', start_index=19457)
Annotation(end_index=19544, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAYrlhpuRAAgJ9u9LBI_sCGjKjlw42DF-v8Y3IUehQ_VXXrgry2qliwkoti8sa-9BHwzADFgNZw4ZxET-VvZldAGeEwKcu2-9-xMBntcv_K1PNmiJDNlzX3iRBQK1jSwEj8ZR0OMee19rw6aCIKkjSX-oLSPFxqExp-8y9', start_index=19534)
Annotation(end_index=19624, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9w79MscHp5h5HrHE7XOMm69puJYVCQk_uiJcWDqDbdGZktjBF79LdE5Up23tbQn4XaAwnQLwFaTLvc3uEGO3XDuQ6fyp4FKkJ4B2mrEKQVPgNDg36YDurzL_ehuXuh8aGfA==', start_index=19614)
Annotation(end_index=19730, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE39i18IX4CrxNidl3_QnlLwP0R4qthmfXPX4mdpkHbI_iTwJTOqPBpLf-LkpwJTL617EDukXJQQpoivT8Hq0BMaHHQ7KHSNVL9HP3PWsCxenrVB6S09hw5EOiAv8QuTlkoA0Fy4HhEuvwvtn-b7J_L6nWwOcqg21TDN0RIxhagtR_HtQ==', start_index=19720)
Annotation(end_index=19866, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGA_YfFJ3GLeM71g2YlSR7rSOtbJLU7O4fwfvSp4ROQsjohWVGdkutXxQGbfBNnE9oRfjv-hba86uqI3LqHI-JhSDMC40vPdTSVpdP-5cld5n7yulGMg6qyqHearJJJ6y0gKjkJ12iU7bS9dGoxhAwQL4khGnZfrX8xyPjH1xie_T_b', start_index=19856)
Annotation(end_index=19973, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGICXat3kn6-DLQonuuTNHZ2CSXoWEfYE7bYHM1hH8ihpo4ZgrtDv1TeYgVmw0cif7QEe0YCoerzq0VuInmzcpVYT4zllBSBGookB5OEicpVJ4OwTRGEMpU0J1-jAumnl26G0Lwd7coeeqMlNQKEg2reJRYLLQ6JC4LIvMqNrrl7SfC3r2OVbPO8gl8dad-H9KjcHXJ96gYRt3A-6wetE9rL2hA', start_index=19963)
Annotation(end_index=20077, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtTOX8RTyUiGTVM_iH-oizL2FJpfvqSUHzBSDWrwd3fjtFib4npDhRR05KeT1jhSPcJfdxhNqF8ESh6cZoMuO_wXJEij4bjOFB1k7qZa8OTWP_HMPJxBiXKhdHlwJL89UWgwbqMtGL4YiErKG8_pjTk0lb32va2_K7ZlUvAnyd6fBYYMF9G0JU', start_index=20067)
Annotation(end_index=20166, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6GvWKtPdCxGcHm-gZjyehTj8Iy7e_MnFWYw1xh5ihoXO8b2PlImzYbLWraEnSDTXp4XR9_yofcxtBPFaIfdjoOxyognNeo75-jraG2Cna8IoNklJysl-lggYvpAwH2ds=', start_index=20156)
Annotation(end_index=20261, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbb0etVF0-RIDogAYGcdqROSTSlog7e-iCMzrYUneocL5aNz6TIPndSCefUwkUKn9HxGj8jhsWOgUJmEAzGeLE9tcnF1F4KlTfzDA1dYLaFMBT-kt6Gy0zI99P15P4flnrHslwKht8Z_Qbia3mlIyzajAo_HSI48v-DE_gAJKfSRmXQ1avHTf9ymYCURnx_I89mXO3lV1-U_v3Sb-HhbgauhLsHgIR2G5J3zdARd2v0AY66UKteq5LhKN_8GYLqGBYKbqK8y3oCPUiIRg846msmM7seha7brr2G3lnwhI=', start_index=20252)
Annotation(end_index=20351, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2pbXrd6-gbeYlGjUrPAF-OLBs5MCj_wg0kk-omVDlk8X_tMen7HS0k83x1MPTlozp_vaPUeNN7SeUEZa7GESZHcckehR7NL1cwsv4QPcmiPrbOOV7nVth1WgI697qU11StfrSN0C8bg5YbLCXgXO0qKQ=', start_index=20341)
Annotation(end_index=20431, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhXYvLAujp3XnaLp2crN_QU8509sy9_VObfX5u9Q4RfWZlrrXlOAF9TDLLDqthoLS-ebjcz0boEiqdCDft3pObz_tV79zNgFb2veVe1NAqt8jyClkYSzxa4jAR3bXwX71b8u_0kmgWs-KITsO04jQ=', start_index=20421)
Annotation(end_index=20518, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEC3oz_RWNMXYsB_nI5OMZUrPzeHNGHvCME2fT5UTpM1D2ape8h1OoasiQAIlzvbU_DQud8jW-OdEtquuLeNvijI67vM7OaMQjlqFDFrLvpBAzzNpSmA5Lrt3m4nGZKzK0=', start_index=20508)
Annotation(end_index=20616, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnsHnYHGsDZl7iWsOM463bRX9OQZ9Kbf5Az8Qz6bQasl0lELKBqOnxJhwDcLLnpBSP1cUj-_5_HyFEllxm-Te_7-jgvx5kAAx0flhsWMJfLyoWk6DZgV7p', start_index=20606)
Annotation(end_index=20700, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHIT_3RL2VkyT-YbXTHQOs-vVN19B5E8E4LOPK_Ja9lEXj6dSXcl3yLooi4nvzyKFDSk_8KUzPHt9Jw8Uciw-IJdJZlBSSO1b2Yye3TBnE3moG2x6RWqFRFIi_ltDQKgEkAhZz3QsQx0_cKmreg1aPUHA_IBHIwkZ_msn1gLbACATYY4icu_LwLpbOmJrfMzIQrcuaW-L8E-9Lzh5hvdcORw==', start_index=20690)
Annotation(end_index=20799, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfJhLH4MLu1kXbRyDbcXD00ZM3KaUJQls813z6w8wm11xy3zQ_hxVKhc-4BitlhBc6Tbbg_8GHopefzawAzi4wZzrCS7cAUD0yVO_uflMoYTVYoCQF', start_index=20789)
Annotation(end_index=20897, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESb45kjQoKZs21-FtUzMm_EzKsds1cqdyQxdXww6DsJlgRX5t0ZBdGX_QK-eVkz0UE-cTbjHOTR-Saq1kJmsrDcfBC23uFglcbq_zssywrUydfsAoCLk1KIEGc55XJW21xa_Y=', start_index=20887)
Annotation(end_index=20955, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETSh_eCN6LZkTYSNDme1phmEHFBhamK9aAzETim6vOyj2wiwGmwRGY9tLDmD7M_HK3aYW79R-bHY9LjTZ6CN-Tq0YCv8ro1QlTu3_XHMYC8qNjKJATQUNEdOVHMRUjUn0u8ajkB4caoSrP', start_index=20945)
Annotation(end_index=21040, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyXY_y-C_GO6No6GobscQiRSDjShUWyCB8yki2QxyJfgAgPLq627Z5LboNDHYaYgz5Yo5UiIE8HXXu5HkLT5Jef03RrYAAkMt3R5dKE79ZHwkrcq2JTvKZLmNhAPrkSjaLqfHnOcP6hmwCsr0pSbSE8tcXM9oVZj8dg3nlc_kUIiCoKNC1CR--lRTwkyAOCgGKMjLtX9MHzqN3tQ1k7x4=', start_index=21031)
Annotation(end_index=21150, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGICXat3kn6-DLQonuuTNHZ2CSXoWEfYE7bYHM1hH8ihpo4ZgrtDv1TeYgVmw0cif7QEe0YCoerzq0VuInmzcpVYT4zllBSBGookB5OEicpVJ4OwTRGEMpU0J1-jAumnl26G0Lwd7coeeqMlNQKEg2reJRYLLQ6JC4LIvMqNrrl7SfC3r2OVbPO8gl8dad-H9KjcHXJ96gYRt3A-6wetE9rL2hA', start_index=21140)
Annotation(end_index=21235, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-_fGDGtfVKIHb2bu8hdUBEkkP0XE3vYr6Z1MCxEDWwcEH3P2AeMZ-gdzbw099PPmW-ugdEWDKNjytkrhFUp6yYKZS_pqD-M1ybr_QVy48qYp6n83s', start_index=21226)
Annotation(end_index=21319, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzeqp1EZ_omw2RMRuI30B-3cXt8jpwpb7KhvkB9S75ZUqLFPbQlhgo-Dw46vhiIT2UX3oihhXtzAGfbpqTWhgDo0wvmMYqDep7hqTpofJO7gqASRqUF4ApWumHdlitRcy6BOyFADprcEweNi0v02Km6S7H0rdx1Int6Gs=', start_index=21310)

## Sources
