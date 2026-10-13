# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 71294f68 | **Time:** 351.72s | **Cost:** $1.39537
--------------------------------------------------------------------------------

# Does the Venture Capital Allocation Algorithm of Financial Startups Optimize the Return-Diversification Balance, or Does the Markowitz Model's Covariance Estimation Exaggerate Tail Risk Prediction Errors?

### Key Points
*   **The Divergence of Theory and Reality:** Traditional Markowitz Mean-Variance Optimization (MVO) often fails in venture capital (VC) allocation because it assumes normal distributions of returns. VC returns follow a Power Law (Pareto distribution), where a tiny fraction of investments generate the vast majority of returns. Consequently, standard MVO tends to underestimate the potential of "home run" outliers while misinterpreting the risk of failure.
*   **The "Error Maximization" Enigma:** The Markowitz model is mathematically prone to "error maximization." It acts as a magnifying glass for estimation errors in input data. In VC, where data is sparse and noisy, this leads to unstable and extreme portfolio weights that do not reflect true risk-adjusted optimality.
*   **Volatility Laundering and Covariance:** Private market valuations are often "smoothed" due to infrequent pricing (appraisal-based valuations). This artificial smoothing suppresses observed volatility and correlation with public markets. When these "laundered" metrics are fed into MVO algorithms, the model exaggerates the diversification benefits, leading to dangerous over-allocations to illiquid assets.
*   **Algorithmic Evolution:** Financial startups and "Quant VCs" are increasingly abandoning pure MVO in favor of Machine Learning (ML) and robust optimization techniques (e.g., Conditional Value at Risk or CVaR). These newer algorithms attempt to model non-linear dependencies and fat tails directly, aiming to optimize the "batting average" and capture the Power Law rather than merely minimizing variance.

---

## 1. Introduction

The integration of algorithmic decision-making into venture capital (VC) and financial startups represents a collision between classical financial theory and the chaotic reality of private markets. The central tension lies between the elegant, equilibrium-based framework of Modern Portfolio Theory (MPT)—specifically the Markowitz Mean-Variance Optimization (MVO) model—and the skewed, heavy-tailed nature of startup returns.

The user’s query probes a critical systemic risk: whether the algorithms used by modern financial startups to allocate capital are genuinely optimizing the trade-off between risk and return, or if they are merely propagating the flaws of covariance estimation inherent in the Markowitz model. The evidence suggests that while MVO remains a foundational pedagogical tool, its direct application to venture capital is fraught with peril. The model’s reliance on historical covariance and normal distribution assumptions often leads to the exaggeration of diversification benefits (due to data smoothing) and the exacerbation of prediction errors (due to error maximization), failing to account for the "fat tails" that define venture success.

This report analyzes the mechanics of these algorithms, the statistical anomalies of venture capital returns, and the specific failures of covariance estimation in private markets.

---

## 2. The Markowitz Model: Theoretical Foundations and Venture Capital Incompatibility

### 2.1 The Mechanics of Mean-Variance Optimization (MVO)
Harry Markowitz’s Modern Portfolio Theory (MPT), introduced in 1952, revolutionized finance by quantifying the benefits of diversification. The core premise is that an investor can construct an "efficient frontier" of portfolios that maximize expected return for a given level of risk (defined as variance or standard deviation) [cite: 1, 2].

The mathematical backbone of this model relies on three primary inputs:
1.  **Expected Returns ($\mu$):** The anticipated future performance of assets.
2.  **Volatility ($\sigma$):** The standard deviation of returns, serving as a proxy for risk.
3.  **Covariance Matrix ($\Sigma$):** A measure of how asset returns move in relation to one another [cite: 3, 4].

In a frictionless market with normally distributed returns (Gaussian distribution), MVO mathematically guarantees an optimal return-diversification balance. By combining assets with imperfect correlations (covariance < 1), the aggregate portfolio risk is lower than the weighted average risk of the individual components [cite: 5, 6].

### 2.2 The Normality Assumption vs. The Power Law
The fundamental disconnect in applying MVO to venture capital is the distribution of returns. MVO assumes that asset returns are normally distributed—a "bell curve" where outcomes cluster around the mean, and extreme events (tails) are rare [cite: 1].

However, venture capital returns do not follow a normal distribution; they follow a **Power Law** (or Pareto distribution). In this environment:
*   **The Fat Tail Dominance:** A tiny percentage of investments (the "home runs" or "unicorns") generate the vast majority of the fund's total return. Research indicates that the top 10% of venture deals can generate 60-80% of all returns [cite: 7, 8].
*   **Asymmetry:** The most likely outcome for a single VC investment is a total loss (100% downside), while the upside is theoretically uncapped (1,000x or more). This extreme skewness violates the symmetry assumed by the variance measure in MVO [cite: 7, 9].
*   **The Failure of Variance as a Risk Metric:** In MVO, "risk" is defined as volatility (deviation from the mean). In VC, upside volatility is the *objective*, not a risk to be minimized. MVO penalizes the extreme upside volatility of a potential unicorn just as it penalizes downside volatility, leading to suboptimal allocations that shy away from the very assets required for venture success [cite: 7, 10].

### 2.3 The "Error Maximization" Enigma
The query asks if the model exaggerates prediction errors. The answer is a definitive yes, a phenomenon known in financial econometrics as "error maximization."

MVO algorithms are mathematically hypersensitive to inputs. They treat estimated parameters (expected returns and covariance) as if they were certain. However, these inputs are mere estimates with significant standard errors. The optimization process acts as an "error maximizer," aggressively allocating capital to assets with the most optimistic (and likely erroneous) return estimates or the most understated risk estimates [cite: 2, 11].

In the context of financial startups and VC:
*   **Sparse Data:** Startups lack the long historical price data required to calculate a robust covariance matrix.
*   **Noise Amplification:** When an algorithm runs MVO on noisy VC data, it tends to concentrate the portfolio in assets that appear statistically attractive due to measurement error rather than fundamental strength [cite: 12, 13].
*   **Instability:** Small changes in the input assumptions can lead to massive swings in the recommended portfolio weights, making the "optimal" portfolio practically unimplementable and theoretically suspect [cite: 1, 14].

---

## 3. Covariance Estimation and "Volatility Laundering"

A critical failure point in applying Markowitzian algorithms to private markets is the estimation of the covariance matrix. The user asks if this estimation exaggerates tail risk prediction errors. Research indicates that the specific mechanics of private market valuation lead to a phenomenon often called "volatility laundering," which causes algorithms to **underestimate** risk and **exaggerate** diversification benefits.

### 3.1 The Smoothing Effect
Unlike public stocks, which are priced continuously (mark-to-market), private assets like VC and private equity are valued infrequently (mark-to-model), often quarterly or annually. This appraisal-based valuation creates a "smoothing" effect where the reported returns lag behind true economic reality [cite: 15, 16].

*   **Autocorrelation:** Private asset returns exhibit high serial correlation (autocorrelation). If a startup's value drops in reality, the markdown might be spread over several quarters. This artificial smoothness dampens the calculated standard deviation [cite: 15, 17].
*   **Artificial Low Volatility:** Studies show that reported volatility for private equity and VC can be artificially suppressed by 40% to 60% due to smoothing. For example, early-stage VC volatility might be reported at 29%, but when "unsmoothed" to reflect true market risk, it jumps to 87% [cite: 15, 18].

### 3.2 Distortion of the Covariance Matrix
The Markowitz algorithm relies on the covariance matrix to find uncorrelated assets. Smoothing distorts this matrix in two ways:
1.  **Underestimated Correlation:** Because private valuations react slowly to market shocks, they appear mathematically uncorrelated with public markets in the short term. This is an illusion. In a true liquidity crisis, correlations often converge to 1 [cite: 5, 19].
2.  **Exaggerated Diversification:** When an MVO algorithm processes this smoothed data, it perceives the asset class as having "high return, low risk, and low correlation." Consequently, the algorithm allocates a disproportionately large weight to the asset class, believing it has found a "free lunch" of diversification [cite: 5].

### 3.3 The Impact on Tail Risk Prediction
Does this exaggerate tail risk prediction errors? **Yes, by masking them.**
*   **The False Sense of Security:** By using a covariance matrix derived from smoothed data, the algorithm predicts a much thinner "tail" (lower probability of extreme loss) than exists in reality. It effectively "launders" the tail risk out of the model [cite: 20, 21].
*   **The "Exaggeration" Mechanism:** The model exaggerates the *precision* of its risk prediction while simultaneously being massively wrong about the *magnitude* of the tail risk. When the "unsmoothing" of returns is performed (adjusting for lagged betas), Sharpe ratios for VC funds often plummet (e.g., from 0.62 to 0.28), revealing that the algorithm's initial optimization was based on a phantom risk profile [cite: 15, 18].

---

## 4. Tail Risk and the Failure of Normal Distributions

The user's query specifically references "tail risk prediction errors." In venture capital, the tail *is* the curve. The failure of standard algorithms to account for this leads to systematic misallocation.

### 4.1 Fat Tails and Kurtosis
Standard MVO assumes a kurtosis (measure of tailedness) of 3 (normal distribution). Venture capital return distributions exhibit "fat tails" (excess kurtosis), meaning extreme events occur far more frequently than a normal distribution predicts [cite: 1, 22].
*   **Left Tail (Downside):** The risk of total loss is high (50%+ of startups fail), creating a truncated left tail [cite: 7].
*   **Right Tail (Upside):** The potential for 100x returns creates a massive right skew.

### 4.2 Underestimation vs. Exaggeration
There is a nuance in the user's question regarding whether the model "exaggerates" errors.
*   **Underestimation of Frequency:** Standard MVO *underestimates* the frequency of tail events. It assigns a near-zero probability to events that happen regularly in VC (both total wipeouts and massive unicorns) [cite: 23, 24].
*   **Exaggeration of Safety:** By underestimating the tails, the model *exaggerates* the safety and stability of the portfolio.
*   **Exaggeration of Sensitivity:** As noted in the "Error Maximization" section, the model *exaggerates* the impact of small estimation errors. If the covariance matrix is slightly off (which it always is in VC), the model might aggressively overweight a specific sector, exposing the portfolio to idiosyncratic tail risks that the diversification was supposed to eliminate [cite: 11, 12].

### 4.3 The Power Law Imperative
In a Power Law environment, the "average" is meaningless because it is skewed by the outliers. A "diversified" portfolio in the Markowitz sense (e.g., 15 assets to remove idiosyncratic risk) is insufficient in VC. To capture the Power Law tail, a portfolio must be large enough (indexing) to statistically guarantee hitting a winner. Research suggests VC portfolios need 50-80+ investments to reliably capture the outlier, whereas MVO might suggest a concentrated portfolio based on false covariance data [cite: 7, 25].

---

## 5. Algorithmic Innovations: How Financial Startups are Responding

Recognizing the failures of the Markowitz model in the VC context, financial startups and "Quant VCs" are developing new algorithmic approaches. These represent the "optimization" side of the user's query.

### 5.1 From Mean-Variance to Mean-CVaR
To address the tail risk blindness of MVO, advanced algorithms are shifting toward **Conditional Value at Risk (CVaR)** or Expected Shortfall optimization.
*   **Mechanism:** Unlike Variance (which treats upside and downside deviation equally), CVaR focuses specifically on the left tail (the worst-case losses). It optimizes the portfolio to minimize the expected loss *given* that a tail event occurs [cite: 24, 26, 27].
*   **Application:** This allows algorithms to construct portfolios that are robust to the high failure rates of startups while still seeking the upside skew [cite: 24].

### 5.2 Machine Learning and Predictive Analytics
Financial startups are replacing the static inputs of MVO with dynamic Machine Learning (ML) models.
*   **Non-Linearity:** ML algorithms (e.g., Neural Networks, Random Forests) can model non-linear relationships and regime changes that linear covariance matrices miss [cite: 1, 28, 29].
*   **Alternative Data:** Instead of relying solely on price history (which is non-existent for early-stage startups), these algorithms analyze "alternative data" such as GitHub commits, web traffic, founder backgrounds, and hiring velocity to predict success probabilities [cite: 30, 31, 32].
*   **Regime Switching:** ML models can adapt to changing market correlations (e.g., during a crash when all correlations go to 1), whereas standard MVO assumes static correlations [cite: 29, 33].

### 5.3 Robust Optimization and Shrinkage
To combat "error maximization," algorithms use **Shrinkage Estimators** (e.g., Ledoit-Wolf).
*   **Concept:** These methods "shrink" the noisy sample covariance matrix toward a structured target (like a constant correlation model). This reduces the impact of estimation errors and prevents the algorithm from making extreme bets based on noise [cite: 12, 34, 35].
*   **Result:** This produces more stable portfolios that are less sensitive to the "garbage in, garbage out" problem of VC data [cite: 36].

---

## 6. Synthesis: Does the Algorithm Optimize or Exaggerate?

The answer to the user's query is not binary; it depends on *which* algorithm is being used.

### 6.1 The Failure of Naive Algorithms
If a financial startup uses a "naive" Markowitz implementation (standard MVO with historical sample covariance) for VC allocation:
*   **It does NOT optimize the return-diversification balance.** It optimizes a *fiction* based on smoothed returns.
*   **It DOES exaggerate tail risk prediction errors.** It does so by:
    1.  **Masking the Tail:** Underestimating the probability of extreme events due to normality assumptions [cite: 23].
    2.  **Amplifying Noise:** Maximizing the impact of estimation errors in the covariance matrix [cite: 11].
    3.  **Laundering Volatility:** Interpreting smoothed valuations as low risk, leading to dangerous over-concentration in illiquid assets [cite: 5, 15].

### 6.2 The Promise of Modern "Quant VC" Algorithms
If the startup utilizes state-of-the-art techniques (ML, CVaR, Robust Optimization):
*   **It attempts to optimize the Power Law.** By focusing on "batting average" and outlier capture rather than variance minimization, these algorithms align better with the economic reality of VC [cite: 7, 32].
*   **It mitigates prediction errors.** Through shrinkage and robust estimators, these models dampen the noise inherent in private market data [cite: 35].

### 6.3 The "Batting Average" vs. "Home Run" Debate
A critical finding in the research is that even sophisticated algorithms struggle with the "Power Law" nature of VC. Some research suggests that "indexing" (buying the whole haystack to find the needle) is superior to algorithmic selection because the uncertainty of the outlier is irreducible [cite: 7, 25]. However, other data suggests that ML models can improve the "batting average" (identifying viable companies) even if they cannot perfectly predict the magnitude of the "home run" [cite: 32, 37].

---

## 7. Conclusion

The venture capital allocation algorithms of financial startups exist on a spectrum. Those relying on the traditional Markowitz model with standard covariance estimation are demonstrably flawed. They do not optimize the return-diversification balance; rather, they engage in "volatility laundering," accepting smoothed returns as truth and consequently underestimating tail risk while exaggerating the precision of their allocations. The "error maximization" property of the Markowitz model ensures that the noise in venture capital data—sparse, infrequent, and subjective—is amplified into fragile portfolio constructions.

However, the next generation of financial algorithms is moving beyond Markowitz. By incorporating Machine Learning to handle non-linearities, adopting CVaR to manage fat tails, and utilizing robust covariance estimators to dampen error maximization, these newer systems are beginning to align with the Power Law reality of venture capital. Ultimately, while the Markowitz model's covariance estimation does exaggerate prediction errors in this context, the industry's trajectory is toward models that explicitly reject the Gaussian assumptions that cause these errors.

### Summary Table: Markowitz vs. Venture Capital Reality

| Feature | Markowitz Model (MVO) Assumption | Venture Capital Reality | Consequence of Mismatch |
| :--- | :--- | :--- | :--- |
| **Distribution** | Normal (Bell Curve) | Power Law (Pareto) | Underestimation of outliers (upside) and failure rates (downside). |
| **Risk Metric** | Variance (Volatility) | Permanent Loss / Missed Outlier | "Safe" portfolios miss the winners required for fund return. |
| **Covariance** | Static, Observable | Dynamic, Smoothed (Lagged) | "Volatility Laundering" leads to over-allocation to illiquid assets. |
| **Input Sensitivity**| High (Error Maximization) | High (Noisy/Sparse Data) | Extreme, unstable portfolio weights based on noise. |
| **Diversification** | Uncorrelated Assets reduce Variance | "Indexing" to catch the Outlier | MVO may suggest concentration; VC requires broad exposure (50+ bets). |

**Sources:**
1. [shs-conferences.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkPShfwRoNCN8dLO-KxMphN6C_wCo-G3KDw12y54IjzH47Q5vkplEvgZIX2U6TVCJ1msi-LzEj_Ut1WgzVfPXulFy7_WdO4fEPVuy9T7kbpZ55c95BpFq_vrM2c9SuhR5JQmsXHeq-TNOMTr_nP6MPsaf61NBwgeM0tihUpvEqZESyduclhWEWIcTsZnCl)
2. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGshA2z2eTq98l1PzjOlRGmPdPlsOwgBeUGAZlBknwCzKFUe8uoneECGT-OYsiMw-hzzPo8e9nS1a9LWvsu-rWnVh0iyqF3hkgAmvJmKZoFarf86ZF4hAhlTw7q-MvZJZJ3qZI=)
3. [bcpublication.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHCz6_OLcNqzDU-O_Ms90OnkFVzQc0s83AQyN0ygQ_NEdT6uk4_89ZG5Ken64PyRUuAVdj56V3yh9h56jGf2GCnJenofmu_XzQWh8Jn-5Sbf1rigK4whdPf3AdyBAfd1U7pwYkVdGwMX2lZfYZYWbt0FaQGX3pV4eL5-Ou)
4. [freedomadvisors.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAZsEkv3m6EJ5nqTIM6p3pFABz19IN7jOkIl5mtEZKPH9isk7flgZzFkb-nUOB7C5gAgSr3PQG4s-axZFF582oUnD9R676SLmAhN8nOHmPy0Q44etMWvijc850CarlNP3FyeMLCTABLj8kUxkcBompttfQz14lKYTG7nOQha43Yw1ZFjmZd8dfOg==)
5. [pwlcapital.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaRon65or8ld5meG9UXJgmU1c7PlSrg_IBPEpc749W20066ZYGcl4G4KmkbuQaLJwE0AI0pinkdFsrWwaDy1MCGiyPlIcwYWOYkC8i7-M9HRUS-UUd1ORAvtMt_AbbyqoEEwYYkxsRLnLhSPiF2G_Rr86_4TXZ-6ap4iKDMWpZ)
6. [portagon.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGhrYyuXlgM8tX6rDrUijgcBVuQ1OWD6jdGA9Ytxs0fr3betAzViXf7-yz-1DdsQzl20HTf5YZc3xOJw9lWL_p0DgHPA0mlA9EGSRQgonsQNFRNjZkEUhUUufpZpaSmSwKrL2GXXQWHEdB-HiJDqKKTf1GDqj9uLZiVwNjaI-9h4HgK1rihV6O7BiRwQarf)
7. [skalata.vc](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMPX2gRVW7WgoDbo2NAg7zQPHNjJ6uHlJlAX_DOOpeMB5hwo8Am3DdbzKRZJXZfGv2L4TrbTtYv6LDfu8Nrq4g_fyVLeESMI8r8euQ2qY7hKcqOMcPz4Txu2N_9qjweqf5d9zP0AUs6QiWyNSiiv2oBNoupR2A0MEsO3kF1RgDGfq9IKLC6J9KhKGep2LD5dc9HBL8NJXZfsSQew0RJs0=)
8. [taghash.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8oeODrgoYzjNZ-bMJ_9KHIOYY9CF5F9yyoe-eUTQ9zSQj1NYwGTNKLI9Ve3Vub0jeZZM8MnatDlR_FMFnKKcCJg5XGF8inwuZBbPMmfMIaEAGIE5N9WiOEDMZ26S76Q1q2-P2bv_lNcPEu5sCyo6V0EG0B1_8tNXkRoCs6Fjvfw2BQLL6CllI2xmhh1b9zY4WnDdVyT-9bPP8)
9. [substack.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy2Nfwt5JYILKLBJTl1xKOOOyB83iqBH3186rylfHwlSrKv6bc7r1NQGAzRCY4p8J0BVRk2yroEssEEWFnOnxz4nn2iF6P5bUtDzdr2IkmKLsSkdPqkAwVMOUa7oskestV0dQ17oCGTEIW3w2rjw3lEC5lUZTXDDYf2li5ZGM=)
10. [stanford.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6OnNX16bk4PGA2ncdOGk6ybFY_8U-W9GzT4qdbtI-UkdPEMzCd2nKIm_rAx9E0-ss90nBBdnU0hgaCViUGz6AUn-ne0MOZNICxyDQil4uXbsBYJNLUiH0qM_Ft8rE3N4-YpLwDstYI_31EIPK)
11. [stackexchange.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIE5NFugfPmPqn6-z0hvcx0t1UqKH7W0JrLcGuaaKbgs_SInnhfqCrn48uapc9pJ0rDwxg8J7bkMUTdCePV0XbTlnIbdm54E3qOeZ6qV1KHtNNgpDI-JW8eyNwtesDmLkfBGzXOuul1guvNCUIxnvyf3VW0OvzKwsHQLAUV6s1arvQC2pFdn8yp8wYIZ-n6CpR3Wj3y7SNVe0a_KQdtkI=)
12. [mosek.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL8jK5u7jZ3PeVr7jsreXY1giH-GflBo3YzHcyA9JeXX6omIod-V5tFkoxgp6EtObnEfqJT35_Q6inD9Ww5w_cYjLqAim2i0swlpQ7vQYVWwi4SsR7kVEnzL12XSphty9LjjoYXQNA_deMY-o4omCFH6ZSmA==)
13. [cmu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2OFSvy4giJK8ZPhY-BSDbWY-ffBWPOpiYoiKkueJXmB48xmDM-B6wyuG3KWT5keIpnBnReH71O1kMNfFOBKuF5uDQRruhwNqQdhO31tCLqWo5CFAQW5mik78hLh-egu4rq-O4VVCnQYzYHVZkHhZWnTnQNM8=)
14. [uni-muenchen.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIfkGbP-tXfYkCv6f-_v3bRIi4_4LBw6KzYSk3Fy3wBaMmJ-aec_jsOhrODubvMjFtn9GX8fLiRvTHeEK0lmpnWK81kAHUSRxXL4Phjt5WtjNmPIWTiGtKctu0BMeB3bmV4VOspvBBHnCPs78swtRkFlZpBjyc1iSujHaJjOl91pW7pjP_xFSDhUcc_W03eQLwoxcUwDWAvl_-OTncIMLYHTOUfvMVKFnIdNX-hDL0)
15. [interactivebrokers.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE14_X-jewWhdB1mGeU3MfVdK5pFFbplZTDar4l0Euzae5BkI0vzfSqbgr0a3s_BcaJnGz4Le5vNt9ukshD3XCKgiTHlDA009nI0O1_2wOY3H4bulvI1tKQxZifpo3uZ4IWZ2pbwx8g9bDBKzH9WdoUEG2cceqPZ5FTXPAiaAHAzNa-Lx4gJGiUIbnWfAkQjaMW_3t-dgqPcdU-KVkyVQZi6zWFEj2PePwZh7Xy4Fmy)
16. [institutionalinvestor.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzguILvhf3TH4OngMK2sjCTS9KtjC2VCOsU44jMPXeR9BQk3ZAcxQ6tIwr2qLBsgJ2R7jlQwM4mFSeuDLNDqvG46v6A89PciFkNulr0XTzsPWJM4cksEI_fNCg-xMIN3HX21nbiDPxHMtoACfMD2oSJmPwExWJ1jlNNgE-dgfn9dofnN-vvtE6lkRjPz8668aGbFQFZL-BsjEbwWNnNXqmPjYRUnRoVKfglFdA30I4uMuoRH-qt3XXPQ5S07eAoGpuxkQerI6knV8Nc89OkpF9GzYR)
17. [portfoliooptimizer.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiO87ueltYlNJ0Lu9ZSr3e1IdNWnuc75rdYr_16Pebj7eZQ7opDhKQHHf5tskjWIlgVHnWBRqm806avkT8ws14DapsDQywkN51luM8h5v-5iioS0T1eEVZJlU3wYYOdKVDJrEv1K6h7qo2TZCfs5sBLuNbdu08OFyjGtKAw-h3CUCaslM2QI1RG1uKx7ICLyy27ejWjII1gLTaKGwuaOYgWh-t)
18. [alphaarchitect.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXyzcm0zfk3EObVwar_kZCThJfKlxxZg-Ob8eiMgpk1t33piSUupGLF3CiHQKx-bRTaSyv01ZrLmZCGGTd0Z-3D_4iNPKSw0VczEIvXGLhhPgcd1ceWgP0o7WiMaEKfdxCar4r4Vk0)
19. [commonfund.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7Awr7h9lGX47_CS6YnDqQnXei1fnPxL0Yj-z27KWiaIuY-m3DtQQJn_n7g0kzoKd3flHlkOt-gOPmOWvVl2T3PKlIZ_9R4JJXYTo7DQwRW6SpTja5I7ktGrxwkXFGXK6DXHw18pUydfLKPN8N6xgpwmX2Wd_3ToO9WLP22voJJ95GF__EMPeapgPfi1o3Pc8XN6coePqk2mjz3fBGgIlUdjm_Uifu)
20. [pimco.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHa3xbXp53DwXwKhWLzT8pp1yH3dczT8TFPX5jW6SU8kXCt-LG9D8fs3_rr6nVEFobHwzW8ezkYyB3fS9m8D0B4bjSEn1QYov0X_5sy_alGxhl_brP-IdYtqpuKOlLWQn1TpoRhYOO0reXUTapOS-AJLQ==)
21. [troweprice.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzQYVKx_RE6-7aWu9M5GE8K5x9J3elF16o0UZc6pPoMzgngobyyMRtQBTQrn4pfFeMmmQJjQh4sriBpe-ljiq8IS9MYlVj_jX-OyxMsYKWR-Z6j3Qo6ezq8WsOQh2V-lyjndmletjxG6qpZJ3ynWsDy0yUT88s5p-CYVJC5aQ2l2WNNhZuKRARl7dXnf5e-8N9T1fON7HpSXOGxHcKI2Q=)
22. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEC0_2v-M9cweRuktfDg-L1FeJWJ56wpQEpW1vVq7tbJEy8QaFyi31kzx-Qn4LrmiI3agDZuj7kTDSeR_gy4jWHiKAm7dqXjwJkjCrcNLjkmDmqqsCzOHHJ8cWM4dVE2FZu)
23. [cam.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF1isQPKQ8iW9Zr3ti-AswsdHk24SUNWxi8f4C9fnQePICMn5Ju00oaIOHpHjfq-uk6pC6HujaXZe4CGZKn77NFbrrXg9WDf7S1zH3PGmkj11uCU6LOW6RVUgB1fzDf2jbuITzoMIFjHSxZkLQxSJwHDJoEvhTIsPDBtsRP46KxiA==)
24. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDTH5S_NAW6LjqINZRtErN_j3q9N5jHpuWBptUkKQkRAFtSOy06ufSferRhdzeP32ajcPMZet9uQxD0NDHPt2LV-Xsc_Gx173AMZ_q76mqC7dpHX0Gh966zQ==)
25. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCgFGKCIsZArexUaMB6seuLfDUl8PGj552m127J1ZyBOcGA22ykQlZBCqmmOzFX1mTa3O806ou7KUjNhr-jUa5ehB-b2sTeKfHB_LAguFGzjomwDrE_Kbt-BGjyKquVFTgAjJ478Nf0He9lWFwdPukmQ-Ooxv6baJOmZ0HEZyPbja3NTTjC4hZ9b21rHsbh3OsDsmFb4D5aSJNf76ZiM0vQ9nTdWjd3jMgpvRE_Suf)
26. [vu.lt](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsPTwqLbEI1vBHaDk0xqHnvDVKErxmPpovG1E_BlNSCzqSQuzd9FilpTtzpXTidO4MCAPgywW1mTiVUM5Q9xr_MHz7QYk8oSLUp3lQoR8RtArAZRDcx3gJ5pVpldSL5wn__Dol0N770OPFWqIS_cdtwlx8T-wz)
27. [elifesciences.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrb8EBiBPtd-LqIfVN8pC5p1A9HuZW4c0BSBp0o2Rv8ihBvQlUOcDWPIogKDa4DgT317tV4ctWZtkDecT3qi7xBp7uV3uqgV39Ie_desGFlmbzDxrclsaEYehKRV8Cew==)
28. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-9Ii0bLQedEBnC9APx9NuAbnrOTUcH0zsubh73qDG9v1lOy8EItSyG6rIjOegb2AjEMPFP_Sw31d2fiasRc0ZyA4QG_kT9gz2gs1or84yGuMsvl-wcEueNIQwdEWt-LE9HjWvfe2-UUhV7KwNy6dqEQN_RYt_OWlBo7NvjhKHmJ2e_yErb2Z6EqNw0wtSJ171lT5A3PXg_u0bJBOqKLvlSRuyYjnIFKTe30lSjA0Coc_5mFIGs9dkXMPWq63N-PBDtMJwjnXL8q3pPQLZ-Qexgcp6)
29. [cfainstitute.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxALvJpm8SLVj0dQVXmHGQnbxa1Nkp6WxBM7_8rOuNfuWBcJpulLLKJaNn6TZmA53mc7rDRtfgOTc6zJtCtcK3iKnW89VQtwbw0HmGu4e5Lyi0rFN0dZLpbyle75jx3H3-wGbrz5lJvDlc29ZHp2a-YBSJRbsLxyyzOfD22SLysinAkkTmZ61tK9moQJ4HNwXn7o-CMOTdtaNGzb3a1wDKM6BMVwndHrZrqKIU93pRsI_y8NmlM2vp-wBAQFza)
30. [forbes.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnq93vG9mTf9tjlVnPkgbgp0h8YFwBHe0GK4lq6oIz7fh9ekYelz9p3VbCKhMW6sVLE7j37Wvztqea7WuZ9s6pM_uqTWXQyzOSjD5eWzHDdY51z9KLtIP990VwgJDGGasqkNTkFSUmPVDpSid09hK2_Oc9emmlTNRFFRuE3VQMTu3owy6X8qqzRUnMYGisPgsflP0vOk7R4kgLvdBEEhw49bsGOezYnJRRtMawPw==)
31. [stanford.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUuFCgk58LFeAy2RWUuTqfR-h7nk7IMWqbxptzBVoVZD-fnavr29oZizKx_RJQumbQSskbV4P_ceW48RogjZYUE-xR24GYRAzbaF8gqrvsTlm5y0y-aawxSpwZryhRHLn3nu7OeY_Oy68pIktPir9RZgXWX4bgeg==)
32. [imperial.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYsn-h6m-mgaxr8I_ZkzkfxpzKzYyUSF09TR5TVz8dDr-ocXKkqIlD6RZe1pJtN27GhDrlg_HcY_DPZ8VRFpOVsHiVwuM4pSXzxO14nIpui4v4keXOU7MyNBx9k8uGuhoqVT9G7UDg3hMgHZ1UBFpzE6eWks08YjGpWy5ZreEDvrlQOpa4LY9fuAp1lDhDo5Z8TnhfH-f7rTiDtnaYk8dRktif5TLn7PjfzpceVhQ0zm2yGphp1DjRHm2TOsma_Ei3jQbWzkrRjW7y60w=)
33. [causalens.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEW9fJ5WwPADsPBdCVFx8QMkIhpM89pp3Kdx78KFvWFz28O_yxmcfEqGdg5xjpFVBLcpKlKR0_8Qh6km3IIvGifUVWr1hzXVW9aL-61JmqgfB9zaaUNaR0oWXU37dKmpIJFhh2lzufuCAfHMVXLfdRfGlpyDDpum_l5OV-2q1gKqEwrOyG8LbKvkz-9id1nIppSsadsOCfSKjzzFg==)
34. [reading.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQ7BoCq4DRqJ4xSp6Mi6r1zFLcIcHYARqrJgDCuXPR9sbmTRBwFH_rOJBQvFXRc5YT8O8WIYJGT8GLqEGgMf6QNeGdAet90yDPbnqX6ovKQIDqUoFu9S80YPAo1RCOZPEKQmMZE0Kq7acxQWMZLnEWQoO4)
35. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCDcH3n-mfavSZmOaosiuN7PE4xSnlBO08Zn8HH2BBmXwc8sBahopXPoEUYcRCjKD-M2Vv_GWTMRmeZeG_iKr0ChA9lcQqT3W-yryIn2OrrWAXI71Y6GI=)
36. [diva-portal.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwIrkjjmibx3-o_8_XkJr3ZZ9J9SgtrGQgn0lNbOBTNYlGbKcoSrmobBZ9Xs6r7FbNQxN_z3BFbZlrueQMvONkXDwVfRSCugwyVE67d-hmFh0mgvFva6hfKg2iSFSU72NRzTdTjiSrB8aJbu8EbDV1qxZyHoAARIM=)
37. [bipventures.vc](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvkYwClSeOG2T9Zw2fxghOvXufxjoW_HBYKdd07BWB7ODv0EUOGLc5NHdSFrnCYvPyMVIiW7-GGsdpb1iZNxunyG5r_WpaD6FYNwUg-fjXw2hiXIhbkScX1-IBYlVnByNt6iKnTfT6H3exJpWVVIAuKHYnBk0ecxNk6SB9HGtlYnJ3kATdiICc5h_zgLwj7w==)


## Annotations
Annotation(end_index=3705, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkPShfwRoNCN8dLO-KxMphN6C_wCo-G3KDw12y54IjzH47Q5vkplEvgZIX2U6TVCJ1msi-LzEj_Ut1WgzVfPXulFy7_WdO4fEPVuy9T7kbpZ55c95BpFq_vrM2c9SuhR5JQmsXHeq-TNOMTr_nP6MPsaf61NBwgeM0tihUpvEqZESyduclhWEWIcTsZnCl', start_index=3693)
Annotation(end_index=3705, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGshA2z2eTq98l1PzjOlRGmPdPlsOwgBeUGAZlBknwCzKFUe8uoneECGT-OYsiMw-hzzPo8e9nS1a9LWvsu-rWnVh0iyqF3hkgAmvJmKZoFarf86ZF4hAhlTw7q-MvZJZJ3qZI=', start_index=3693)
Annotation(end_index=4068, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAZsEkv3m6EJ5nqTIM6p3pFABz19IN7jOkIl5mtEZKPH9isk7flgZzFkb-nUOB7C5gAgSr3PQG4s-axZFF582oUnD9R676SLmAhN8nOHmPy0Q44etMWvijc850CarlNP3FyeMLCTABLj8kUxkcBompttfQz14lKYTG7nOQha43Yw1ZFjmZd8dfOg==', start_index=4056)
Annotation(end_index=4068, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHCz6_OLcNqzDU-O_Ms90OnkFVzQc0s83AQyN0ygQ_NEdT6uk4_89ZG5Ken64PyRUuAVdj56V3yh9h56jGf2GCnJenofmu_XzQWh8Jn-5Sbf1rigK4whdPf3AdyBAfd1U7pwYkVdGwMX2lZfYZYWbt0FaQGX3pV4eL5-Ou', start_index=4056)
Annotation(end_index=4404, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaRon65or8ld5meG9UXJgmU1c7PlSrg_IBPEpc749W20066ZYGcl4G4KmkbuQaLJwE0AI0pinkdFsrWwaDy1MCGiyPlIcwYWOYkC8i7-M9HRUS-UUd1ORAvtMt_AbbyqoEEwYYkxsRLnLhSPiF2G_Rr86_4TXZ-6ap4iKDMWpZ', start_index=4392)
Annotation(end_index=4404, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGhrYyuXlgM8tX6rDrUijgcBVuQ1OWD6jdGA9Ytxs0fr3betAzViXf7-yz-1DdsQzl20HTf5YZc3xOJw9lWL_p0DgHPA0mlA9EGSRQgonsQNFRNjZkEUhUUufpZpaSmSwKrL2GXXQWHEdB-HiJDqKKTf1GDqj9uLZiVwNjaI-9h4HgK1rihV6O7BiRwQarf', start_index=4392)
Annotation(end_index=4710, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkPShfwRoNCN8dLO-KxMphN6C_wCo-G3KDw12y54IjzH47Q5vkplEvgZIX2U6TVCJ1msi-LzEj_Ut1WgzVfPXulFy7_WdO4fEPVuy9T7kbpZ55c95BpFq_vrM2c9SuhR5JQmsXHeq-TNOMTr_nP6MPsaf61NBwgeM0tihUpvEqZESyduclhWEWIcTsZnCl', start_index=4701)
Annotation(end_index=5110, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMPX2gRVW7WgoDbo2NAg7zQPHNjJ6uHlJlAX_DOOpeMB5hwo8Am3DdbzKRZJXZfGv2L4TrbTtYv6LDfu8Nrq4g_fyVLeESMI8r8euQ2qY7hKcqOMcPz4Txu2N_9qjweqf5d9zP0AUs6QiWyNSiiv2oBNoupR2A0MEsO3kF1RgDGfq9IKLC6J9KhKGep2LD5dc9HBL8NJXZfsSQew0RJs0=', start_index=5098)
Annotation(end_index=5110, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8oeODrgoYzjNZ-bMJ_9KHIOYY9CF5F9yyoe-eUTQ9zSQj1NYwGTNKLI9Ve3Vub0jeZZM8MnatDlR_FMFnKKcCJg5XGF8inwuZBbPMmfMIaEAGIE5N9WiOEDMZ26S76Q1q2-P2bv_lNcPEu5sCyo6V0EG0B1_8tNXkRoCs6Fjvfw2BQLL6CllI2xmhh1b9zY4WnDdVyT-9bPP8', start_index=5098)
Annotation(end_index=5371, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMPX2gRVW7WgoDbo2NAg7zQPHNjJ6uHlJlAX_DOOpeMB5hwo8Am3DdbzKRZJXZfGv2L4TrbTtYv6LDfu8Nrq4g_fyVLeESMI8r8euQ2qY7hKcqOMcPz4Txu2N_9qjweqf5d9zP0AUs6QiWyNSiiv2oBNoupR2A0MEsO3kF1RgDGfq9IKLC6J9KhKGep2LD5dc9HBL8NJXZfsSQew0RJs0=', start_index=5359)
Annotation(end_index=5371, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy2Nfwt5JYILKLBJTl1xKOOOyB83iqBH3186rylfHwlSrKv6bc7r1NQGAzRCY4p8J0BVRk2yroEssEEWFnOnxz4nn2iF6P5bUtDzdr2IkmKLsSkdPqkAwVMOUa7oskestV0dQ17oCGTEIW3w2rjw3lEC5lUZTXDDYf2li5ZGM=', start_index=5359)
Annotation(end_index=5783, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMPX2gRVW7WgoDbo2NAg7zQPHNjJ6uHlJlAX_DOOpeMB5hwo8Am3DdbzKRZJXZfGv2L4TrbTtYv6LDfu8Nrq4g_fyVLeESMI8r8euQ2qY7hKcqOMcPz4Txu2N_9qjweqf5d9zP0AUs6QiWyNSiiv2oBNoupR2A0MEsO3kF1RgDGfq9IKLC6J9KhKGep2LD5dc9HBL8NJXZfsSQew0RJs0=', start_index=5770)
Annotation(end_index=5783, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6OnNX16bk4PGA2ncdOGk6ybFY_8U-W9GzT4qdbtI-UkdPEMzCd2nKIm_rAx9E0-ss90nBBdnU0hgaCViUGz6AUn-ne0MOZNICxyDQil4uXbsBYJNLUiH0qM_Ft8rE3N4-YpLwDstYI_31EIPK', start_index=5770)
Annotation(end_index=6428, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIE5NFugfPmPqn6-z0hvcx0t1UqKH7W0JrLcGuaaKbgs_SInnhfqCrn48uapc9pJ0rDwxg8J7bkMUTdCePV0XbTlnIbdm54E3qOeZ6qV1KHtNNgpDI-JW8eyNwtesDmLkfBGzXOuul1guvNCUIxnvyf3VW0OvzKwsHQLAUV6s1arvQC2pFdn8yp8wYIZ-n6CpR3Wj3y7SNVe0a_KQdtkI=', start_index=6415)
Annotation(end_index=6428, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGshA2z2eTq98l1PzjOlRGmPdPlsOwgBeUGAZlBknwCzKFUe8uoneECGT-OYsiMw-hzzPo8e9nS1a9LWvsu-rWnVh0iyqF3hkgAmvJmKZoFarf86ZF4hAhlTw7q-MvZJZJ3qZI=', start_index=6415)
Annotation(end_index=6823, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2OFSvy4giJK8ZPhY-BSDbWY-ffBWPOpiYoiKkueJXmB48xmDM-B6wyuG3KWT5keIpnBnReH71O1kMNfFOBKuF5uDQRruhwNqQdhO31tCLqWo5CFAQW5mik78hLh-egu4rq-O4VVCnQYzYHVZkHhZWnTnQNM8=', start_index=6809)
Annotation(end_index=6823, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL8jK5u7jZ3PeVr7jsreXY1giH-GflBo3YzHcyA9JeXX6omIod-V5tFkoxgp6EtObnEfqJT35_Q6inD9Ww5w_cYjLqAim2i0swlpQ7vQYVWwi4SsR7kVEnzL12XSphty9LjjoYXQNA_deMY-o4omCFH6ZSmA==', start_index=6809)
Annotation(end_index=7048, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIfkGbP-tXfYkCv6f-_v3bRIi4_4LBw6KzYSk3Fy3wBaMmJ-aec_jsOhrODubvMjFtn9GX8fLiRvTHeEK0lmpnWK81kAHUSRxXL4Phjt5WtjNmPIWTiGtKctu0BMeB3bmV4VOspvBBHnCPs78swtRkFlZpBjyc1iSujHaJjOl91pW7pjP_xFSDhUcc_W03eQLwoxcUwDWAvl_-OTncIMLYHTOUfvMVKFnIdNX-hDL0', start_index=7035)
Annotation(end_index=7048, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkPShfwRoNCN8dLO-KxMphN6C_wCo-G3KDw12y54IjzH47Q5vkplEvgZIX2U6TVCJ1msi-LzEj_Ut1WgzVfPXulFy7_WdO4fEPVuy9T7kbpZ55c95BpFq_vrM2c9SuhR5JQmsXHeq-TNOMTr_nP6MPsaf61NBwgeM0tihUpvEqZESyduclhWEWIcTsZnCl', start_index=7035)
Annotation(end_index=7886, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE14_X-jewWhdB1mGeU3MfVdK5pFFbplZTDar4l0Euzae5BkI0vzfSqbgr0a3s_BcaJnGz4Le5vNt9ukshD3XCKgiTHlDA009nI0O1_2wOY3H4bulvI1tKQxZifpo3uZ4IWZ2pbwx8g9bDBKzH9WdoUEG2cceqPZ5FTXPAiaAHAzNa-Lx4gJGiUIbnWfAkQjaMW_3t-dgqPcdU-KVkyVQZi6zWFEj2PePwZh7Xy4Fmy', start_index=7872)
Annotation(end_index=7886, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzguILvhf3TH4OngMK2sjCTS9KtjC2VCOsU44jMPXeR9BQk3ZAcxQ6tIwr2qLBsgJ2R7jlQwM4mFSeuDLNDqvG46v6A89PciFkNulr0XTzsPWJM4cksEI_fNCg-xMIN3HX21nbiDPxHMtoACfMD2oSJmPwExWJ1jlNNgE-dgfn9dofnN-vvtE6lkRjPz8668aGbFQFZL-BsjEbwWNnNXqmPjYRUnRoVKfglFdA30I4uMuoRH-qt3XXPQ5S07eAoGpuxkQerI6knV8Nc89OkpF9GzYR', start_index=7872)
Annotation(end_index=8161, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE14_X-jewWhdB1mGeU3MfVdK5pFFbplZTDar4l0Euzae5BkI0vzfSqbgr0a3s_BcaJnGz4Le5vNt9ukshD3XCKgiTHlDA009nI0O1_2wOY3H4bulvI1tKQxZifpo3uZ4IWZ2pbwx8g9bDBKzH9WdoUEG2cceqPZ5FTXPAiaAHAzNa-Lx4gJGiUIbnWfAkQjaMW_3t-dgqPcdU-KVkyVQZi6zWFEj2PePwZh7Xy4Fmy', start_index=8147)
Annotation(end_index=8161, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiO87ueltYlNJ0Lu9ZSr3e1IdNWnuc75rdYr_16Pebj7eZQ7opDhKQHHf5tskjWIlgVHnWBRqm806avkT8ws14DapsDQywkN51luM8h5v-5iioS0T1eEVZJlU3wYYOdKVDJrEv1K6h7qo2TZCfs5sBLuNbdu08OFyjGtKAw-h3CUCaslM2QI1RG1uKx7ICLyy27ejWjII1gLTaKGwuaOYgWh-t', start_index=8147)
Annotation(end_index=8471, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE14_X-jewWhdB1mGeU3MfVdK5pFFbplZTDar4l0Euzae5BkI0vzfSqbgr0a3s_BcaJnGz4Le5vNt9ukshD3XCKgiTHlDA009nI0O1_2wOY3H4bulvI1tKQxZifpo3uZ4IWZ2pbwx8g9bDBKzH9WdoUEG2cceqPZ5FTXPAiaAHAzNa-Lx4gJGiUIbnWfAkQjaMW_3t-dgqPcdU-KVkyVQZi6zWFEj2PePwZh7Xy4Fmy', start_index=8457)
Annotation(end_index=8471, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXyzcm0zfk3EObVwar_kZCThJfKlxxZg-Ob8eiMgpk1t33piSUupGLF3CiHQKx-bRTaSyv01ZrLmZCGGTd0Z-3D_4iNPKSw0VczEIvXGLhhPgcd1ceWgP0o7WiMaEKfdxCar4r4Vk0', start_index=8457)
Annotation(end_index=8915, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaRon65or8ld5meG9UXJgmU1c7PlSrg_IBPEpc749W20066ZYGcl4G4KmkbuQaLJwE0AI0pinkdFsrWwaDy1MCGiyPlIcwYWOYkC8i7-M9HRUS-UUd1ORAvtMt_AbbyqoEEwYYkxsRLnLhSPiF2G_Rr86_4TXZ-6ap4iKDMWpZ', start_index=8902)
Annotation(end_index=8915, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7Awr7h9lGX47_CS6YnDqQnXei1fnPxL0Yj-z27KWiaIuY-m3DtQQJn_n7g0kzoKd3flHlkOt-gOPmOWvVl2T3PKlIZ_9R4JJXYTo7DQwRW6SpTja5I7ktGrxwkXFGXK6DXHw18pUydfLKPN8N6xgpwmX2Wd_3ToO9WLP22voJJ95GF__EMPeapgPfi1o3Pc8XN6coePqk2mjz3fBGgIlUdjm_Uifu', start_index=8902)
Annotation(end_index=9249, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaRon65or8ld5meG9UXJgmU1c7PlSrg_IBPEpc749W20066ZYGcl4G4KmkbuQaLJwE0AI0pinkdFsrWwaDy1MCGiyPlIcwYWOYkC8i7-M9HRUS-UUd1ORAvtMt_AbbyqoEEwYYkxsRLnLhSPiF2G_Rr86_4TXZ-6ap4iKDMWpZ', start_index=9240)
Annotation(end_index=9641, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzQYVKx_RE6-7aWu9M5GE8K5x9J3elF16o0UZc6pPoMzgngobyyMRtQBTQrn4pfFeMmmQJjQh4sriBpe-ljiq8IS9MYlVj_jX-OyxMsYKWR-Z6j3Qo6ezq8WsOQh2V-lyjndmletjxG6qpZJ3ynWsDy0yUT88s5p-CYVJC5aQ2l2WNNhZuKRARl7dXnf5e-8N9T1fON7HpSXOGxHcKI2Q=', start_index=9627)
Annotation(end_index=9641, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHa3xbXp53DwXwKhWLzT8pp1yH3dczT8TFPX5jW6SU8kXCt-LG9D8fs3_rr6nVEFobHwzW8ezkYyB3fS9m8D0B4bjSEn1QYov0X_5sy_alGxhl_brP-IdYtqpuKOlLWQn1TpoRhYOO0reXUTapOS-AJLQ==', start_index=9627)
Annotation(end_index=10072, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE14_X-jewWhdB1mGeU3MfVdK5pFFbplZTDar4l0Euzae5BkI0vzfSqbgr0a3s_BcaJnGz4Le5vNt9ukshD3XCKgiTHlDA009nI0O1_2wOY3H4bulvI1tKQxZifpo3uZ4IWZ2pbwx8g9bDBKzH9WdoUEG2cceqPZ5FTXPAiaAHAzNa-Lx4gJGiUIbnWfAkQjaMW_3t-dgqPcdU-KVkyVQZi6zWFEj2PePwZh7Xy4Fmy', start_index=10058)
Annotation(end_index=10072, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXyzcm0zfk3EObVwar_kZCThJfKlxxZg-Ob8eiMgpk1t33piSUupGLF3CiHQKx-bRTaSyv01ZrLmZCGGTd0Z-3D_4iNPKSw0VczEIvXGLhhPgcd1ceWgP0o7WiMaEKfdxCar4r4Vk0', start_index=10058)
Annotation(end_index=10634, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEC0_2v-M9cweRuktfDg-L1FeJWJ56wpQEpW1vVq7tbJEy8QaFyi31kzx-Qn4LrmiI3agDZuj7kTDSeR_gy4jWHiKAm7dqXjwJkjCrcNLjkmDmqqsCzOHHJ8cWM4dVE2FZu', start_index=10621)
Annotation(end_index=10634, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkPShfwRoNCN8dLO-KxMphN6C_wCo-G3KDw12y54IjzH47Q5vkplEvgZIX2U6TVCJ1msi-LzEj_Ut1WgzVfPXulFy7_WdO4fEPVuy9T7kbpZ55c95BpFq_vrM2c9SuhR5JQmsXHeq-TNOMTr_nP6MPsaf61NBwgeM0tihUpvEqZESyduclhWEWIcTsZnCl', start_index=10621)
Annotation(end_index=10762, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMPX2gRVW7WgoDbo2NAg7zQPHNjJ6uHlJlAX_DOOpeMB5hwo8Am3DdbzKRZJXZfGv2L4TrbTtYv6LDfu8Nrq4g_fyVLeESMI8r8euQ2qY7hKcqOMcPz4Txu2N_9qjweqf5d9zP0AUs6QiWyNSiiv2oBNoupR2A0MEsO3kF1RgDGfq9IKLC6J9KhKGep2LD5dc9HBL8NJXZfsSQew0RJs0=', start_index=10753)
Annotation(end_index=11215, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF1isQPKQ8iW9Zr3ti-AswsdHk24SUNWxi8f4C9fnQePICMn5Ju00oaIOHpHjfq-uk6pC6HujaXZe4CGZKn77NFbrrXg9WDf7S1zH3PGmkj11uCU6LOW6RVUgB1fzDf2jbuITzoMIFjHSxZkLQxSJwHDJoEvhTIsPDBtsRP46KxiA==', start_index=11201)
Annotation(end_index=11215, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDTH5S_NAW6LjqINZRtErN_j3q9N5jHpuWBptUkKQkRAFtSOy06ufSferRhdzeP32ajcPMZet9uQxD0NDHPt2LV-Xsc_Gx173AMZ_q76mqC7dpHX0Gh966zQ==', start_index=11201)
Annotation(end_index=11736, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIE5NFugfPmPqn6-z0hvcx0t1UqKH7W0JrLcGuaaKbgs_SInnhfqCrn48uapc9pJ0rDwxg8J7bkMUTdCePV0XbTlnIbdm54E3qOeZ6qV1KHtNNgpDI-JW8eyNwtesDmLkfBGzXOuul1guvNCUIxnvyf3VW0OvzKwsHQLAUV6s1arvQC2pFdn8yp8wYIZ-n6CpR3Wj3y7SNVe0a_KQdtkI=', start_index=11722)
Annotation(end_index=11736, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL8jK5u7jZ3PeVr7jsreXY1giH-GflBo3YzHcyA9JeXX6omIod-V5tFkoxgp6EtObnEfqJT35_Q6inD9Ww5w_cYjLqAim2i0swlpQ7vQYVWwi4SsR7kVEnzL12XSphty9LjjoYXQNA_deMY-o4omCFH6ZSmA==', start_index=11722)
Annotation(end_index=12290, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMPX2gRVW7WgoDbo2NAg7zQPHNjJ6uHlJlAX_DOOpeMB5hwo8Am3DdbzKRZJXZfGv2L4TrbTtYv6LDfu8Nrq4g_fyVLeESMI8r8euQ2qY7hKcqOMcPz4Txu2N_9qjweqf5d9zP0AUs6QiWyNSiiv2oBNoupR2A0MEsO3kF1RgDGfq9IKLC6J9KhKGep2LD5dc9HBL8NJXZfsSQew0RJs0=', start_index=12277)
Annotation(end_index=12290, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCgFGKCIsZArexUaMB6seuLfDUl8PGj552m127J1ZyBOcGA22ykQlZBCqmmOzFX1mTa3O806ou7KUjNhr-jUa5ehB-b2sTeKfHB_LAguFGzjomwDrE_Kbt-BGjyKquVFTgAjJ478Nf0He9lWFwdPukmQ-Ooxv6baJOmZ0HEZyPbja3NTTjC4hZ9b21rHsbh3OsDsmFb4D5aSJNf76ZiM0vQ9nTdWjd3jMgpvRE_Suf', start_index=12277)
Annotation(end_index=13036, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsPTwqLbEI1vBHaDk0xqHnvDVKErxmPpovG1E_BlNSCzqSQuzd9FilpTtzpXTidO4MCAPgywW1mTiVUM5Q9xr_MHz7QYk8oSLUp3lQoR8RtArAZRDcx3gJ5pVpldSL5wn__Dol0N770OPFWqIS_cdtwlx8T-wz', start_index=13018)
Annotation(end_index=13036, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDTH5S_NAW6LjqINZRtErN_j3q9N5jHpuWBptUkKQkRAFtSOy06ufSferRhdzeP32ajcPMZet9uQxD0NDHPt2LV-Xsc_Gx173AMZ_q76mqC7dpHX0Gh966zQ==', start_index=13018)
Annotation(end_index=13036, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrb8EBiBPtd-LqIfVN8pC5p1A9HuZW4c0BSBp0o2Rv8ihBvQlUOcDWPIogKDa4DgT317tV4ctWZtkDecT3qi7xBp7uV3uqgV39Ie_desGFlmbzDxrclsaEYehKRV8Cew==', start_index=13018)
Annotation(end_index=13206, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDTH5S_NAW6LjqINZRtErN_j3q9N5jHpuWBptUkKQkRAFtSOy06ufSferRhdzeP32ajcPMZet9uQxD0NDHPt2LV-Xsc_Gx173AMZ_q76mqC7dpHX0Gh966zQ==', start_index=13196)
Annotation(end_index=13545, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-9Ii0bLQedEBnC9APx9NuAbnrOTUcH0zsubh73qDG9v1lOy8EItSyG6rIjOegb2AjEMPFP_Sw31d2fiasRc0ZyA4QG_kT9gz2gs1or84yGuMsvl-wcEueNIQwdEWt-LE9HjWvfe2-UUhV7KwNy6dqEQN_RYt_OWlBo7NvjhKHmJ2e_yErb2Z6EqNw0wtSJ171lT5A3PXg_u0bJBOqKLvlSRuyYjnIFKTe30lSjA0Coc_5mFIGs9dkXMPWq63N-PBDtMJwjnXL8q3pPQLZ-Qexgcp6', start_index=13528)
Annotation(end_index=13545, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkPShfwRoNCN8dLO-KxMphN6C_wCo-G3KDw12y54IjzH47Q5vkplEvgZIX2U6TVCJ1msi-LzEj_Ut1WgzVfPXulFy7_WdO4fEPVuy9T7kbpZ55c95BpFq_vrM2c9SuhR5JQmsXHeq-TNOMTr_nP6MPsaf61NBwgeM0tihUpvEqZESyduclhWEWIcTsZnCl', start_index=13528)
Annotation(end_index=13545, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxALvJpm8SLVj0dQVXmHGQnbxa1Nkp6WxBM7_8rOuNfuWBcJpulLLKJaNn6TZmA53mc7rDRtfgOTc6zJtCtcK3iKnW89VQtwbw0HmGu4e5Lyi0rFN0dZLpbyle75jx3H3-wGbrz5lJvDlc29ZHp2a-YBSJRbsLxyyzOfD22SLysinAkkTmZ61tK9moQJ4HNwXn7o-CMOTdtaNGzb3a1wDKM6BMVwndHrZrqKIU93pRsI_y8NmlM2vp-wBAQFza', start_index=13528)
Annotation(end_index=13839, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYsn-h6m-mgaxr8I_ZkzkfxpzKzYyUSF09TR5TVz8dDr-ocXKkqIlD6RZe1pJtN27GhDrlg_HcY_DPZ8VRFpOVsHiVwuM4pSXzxO14nIpui4v4keXOU7MyNBx9k8uGuhoqVT9G7UDg3hMgHZ1UBFpzE6eWks08YjGpWy5ZreEDvrlQOpa4LY9fuAp1lDhDo5Z8TnhfH-f7rTiDtnaYk8dRktif5TLn7PjfzpceVhQ0zm2yGphp1DjRHm2TOsma_Ei3jQbWzkrRjW7y60w=', start_index=13821)
Annotation(end_index=13839, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUuFCgk58LFeAy2RWUuTqfR-h7nk7IMWqbxptzBVoVZD-fnavr29oZizKx_RJQumbQSskbV4P_ceW48RogjZYUE-xR24GYRAzbaF8gqrvsTlm5y0y-aawxSpwZryhRHLn3nu7OeY_Oy68pIktPir9RZgXWX4bgeg==', start_index=13821)
Annotation(end_index=13839, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnq93vG9mTf9tjlVnPkgbgp0h8YFwBHe0GK4lq6oIz7fh9ekYelz9p3VbCKhMW6sVLE7j37Wvztqea7WuZ9s6pM_uqTWXQyzOSjD5eWzHDdY51z9KLtIP990VwgJDGGasqkNTkFSUmPVDpSid09hK2_Oc9emmlTNRFFRuE3VQMTu3owy6X8qqzRUnMYGisPgsflP0vOk7R4kgLvdBEEhw49bsGOezYnJRRtMawPw==', start_index=13821)
Annotation(end_index=14036, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEW9fJ5WwPADsPBdCVFx8QMkIhpM89pp3Kdx78KFvWFz28O_yxmcfEqGdg5xjpFVBLcpKlKR0_8Qh6km3IIvGifUVWr1hzXVW9aL-61JmqgfB9zaaUNaR0oWXU37dKmpIJFhh2lzufuCAfHMVXLfdRfGlpyDDpum_l5OV-2q1gKqEwrOyG8LbKvkz-9id1nIppSsadsOCfSKjzzFg==', start_index=14022)
Annotation(end_index=14036, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxALvJpm8SLVj0dQVXmHGQnbxa1Nkp6WxBM7_8rOuNfuWBcJpulLLKJaNn6TZmA53mc7rDRtfgOTc6zJtCtcK3iKnW89VQtwbw0HmGu4e5Lyi0rFN0dZLpbyle75jx3H3-wGbrz5lJvDlc29ZHp2a-YBSJRbsLxyyzOfD22SLysinAkkTmZ61tK9moQJ4HNwXn7o-CMOTdtaNGzb3a1wDKM6BMVwndHrZrqKIU93pRsI_y8NmlM2vp-wBAQFza', start_index=14022)
Annotation(end_index=14443, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQ7BoCq4DRqJ4xSp6Mi6r1zFLcIcHYARqrJgDCuXPR9sbmTRBwFH_rOJBQvFXRc5YT8O8WIYJGT8GLqEGgMf6QNeGdAet90yDPbnqX6ovKQIDqUoFu9S80YPAo1RCOZPEKQmMZE0Kq7acxQWMZLnEWQoO4', start_index=14425)
Annotation(end_index=14443, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCDcH3n-mfavSZmOaosiuN7PE4xSnlBO08Zn8HH2BBmXwc8sBahopXPoEUYcRCjKD-M2Vv_GWTMRmeZeG_iKr0ChA9lcQqT3W-yryIn2OrrWAXI71Y6GI=', start_index=14425)
Annotation(end_index=14443, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL8jK5u7jZ3PeVr7jsreXY1giH-GflBo3YzHcyA9JeXX6omIod-V5tFkoxgp6EtObnEfqJT35_Q6inD9Ww5w_cYjLqAim2i0swlpQ7vQYVWwi4SsR7kVEnzL12XSphty9LjjoYXQNA_deMY-o4omCFH6ZSmA==', start_index=14425)
Annotation(end_index=14584, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwIrkjjmibx3-o_8_XkJr3ZZ9J9SgtrGQgn0lNbOBTNYlGbKcoSrmobBZ9Xs6r7FbNQxN_z3BFbZlrueQMvONkXDwVfRSCugwyVE67d-hmFh0mgvFva6hfKg2iSFSU72NRzTdTjiSrB8aJbu8EbDV1qxZyHoAARIM=', start_index=14574)
Annotation(end_index=15225, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF1isQPKQ8iW9Zr3ti-AswsdHk24SUNWxi8f4C9fnQePICMn5Ju00oaIOHpHjfq-uk6pC6HujaXZe4CGZKn77NFbrrXg9WDf7S1zH3PGmkj11uCU6LOW6RVUgB1fzDf2jbuITzoMIFjHSxZkLQxSJwHDJoEvhTIsPDBtsRP46KxiA==', start_index=15215)
Annotation(end_index=15335, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIE5NFugfPmPqn6-z0hvcx0t1UqKH7W0JrLcGuaaKbgs_SInnhfqCrn48uapc9pJ0rDwxg8J7bkMUTdCePV0XbTlnIbdm54E3qOeZ6qV1KHtNNgpDI-JW8eyNwtesDmLkfBGzXOuul1guvNCUIxnvyf3VW0OvzKwsHQLAUV6s1arvQC2pFdn8yp8wYIZ-n6CpR3Wj3y7SNVe0a_KQdtkI=', start_index=15325)
Annotation(end_index=15490, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE14_X-jewWhdB1mGeU3MfVdK5pFFbplZTDar4l0Euzae5BkI0vzfSqbgr0a3s_BcaJnGz4Le5vNt9ukshD3XCKgiTHlDA009nI0O1_2wOY3H4bulvI1tKQxZifpo3uZ4IWZ2pbwx8g9bDBKzH9WdoUEG2cceqPZ5FTXPAiaAHAzNa-Lx4gJGiUIbnWfAkQjaMW_3t-dgqPcdU-KVkyVQZi6zWFEj2PePwZh7Xy4Fmy', start_index=15477)
Annotation(end_index=15490, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaRon65or8ld5meG9UXJgmU1c7PlSrg_IBPEpc749W20066ZYGcl4G4KmkbuQaLJwE0AI0pinkdFsrWwaDy1MCGiyPlIcwYWOYkC8i7-M9HRUS-UUd1ORAvtMt_AbbyqoEEwYYkxsRLnLhSPiF2G_Rr86_4TXZ-6ap4iKDMWpZ', start_index=15477)
Annotation(end_index=15840, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMPX2gRVW7WgoDbo2NAg7zQPHNjJ6uHlJlAX_DOOpeMB5hwo8Am3DdbzKRZJXZfGv2L4TrbTtYv6LDfu8Nrq4g_fyVLeESMI8r8euQ2qY7hKcqOMcPz4Txu2N_9qjweqf5d9zP0AUs6QiWyNSiiv2oBNoupR2A0MEsO3kF1RgDGfq9IKLC6J9KhKGep2LD5dc9HBL8NJXZfsSQew0RJs0=', start_index=15827)
Annotation(end_index=15840, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYsn-h6m-mgaxr8I_ZkzkfxpzKzYyUSF09TR5TVz8dDr-ocXKkqIlD6RZe1pJtN27GhDrlg_HcY_DPZ8VRFpOVsHiVwuM4pSXzxO14nIpui4v4keXOU7MyNBx9k8uGuhoqVT9G7UDg3hMgHZ1UBFpzE6eWks08YjGpWy5ZreEDvrlQOpa4LY9fuAp1lDhDo5Z8TnhfH-f7rTiDtnaYk8dRktif5TLn7PjfzpceVhQ0zm2yGphp1DjRHm2TOsma_Ei3jQbWzkrRjW7y60w=', start_index=15827)
Annotation(end_index=15995, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCDcH3n-mfavSZmOaosiuN7PE4xSnlBO08Zn8HH2BBmXwc8sBahopXPoEUYcRCjKD-M2Vv_GWTMRmeZeG_iKr0ChA9lcQqT3W-yryIn2OrrWAXI71Y6GI=', start_index=15985)
Annotation(end_index=16357, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMPX2gRVW7WgoDbo2NAg7zQPHNjJ6uHlJlAX_DOOpeMB5hwo8Am3DdbzKRZJXZfGv2L4TrbTtYv6LDfu8Nrq4g_fyVLeESMI8r8euQ2qY7hKcqOMcPz4Txu2N_9qjweqf5d9zP0AUs6QiWyNSiiv2oBNoupR2A0MEsO3kF1RgDGfq9IKLC6J9KhKGep2LD5dc9HBL8NJXZfsSQew0RJs0=', start_index=16344)
Annotation(end_index=16357, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCgFGKCIsZArexUaMB6seuLfDUl8PGj552m127J1ZyBOcGA22ykQlZBCqmmOzFX1mTa3O806ou7KUjNhr-jUa5ehB-b2sTeKfHB_LAguFGzjomwDrE_Kbt-BGjyKquVFTgAjJ478Nf0He9lWFwdPukmQ-Ooxv6baJOmZ0HEZyPbja3NTTjC4hZ9b21rHsbh3OsDsmFb4D5aSJNf76ZiM0vQ9nTdWjd3jMgpvRE_Suf', start_index=16344)
Annotation(end_index=16552, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvkYwClSeOG2T9Zw2fxghOvXufxjoW_HBYKdd07BWB7ODv0EUOGLc5NHdSFrnCYvPyMVIiW7-GGsdpb1iZNxunyG5r_WpaD6FYNwUg-fjXw2hiXIhbkScX1-IBYlVnByNt6iKnTfT6H3exJpWVVIAuKHYnBk0ecxNk6SB9HGtlYnJ3kATdiICc5h_zgLwj7w==', start_index=16538)
Annotation(end_index=16552, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYsn-h6m-mgaxr8I_ZkzkfxpzKzYyUSF09TR5TVz8dDr-ocXKkqIlD6RZe1pJtN27GhDrlg_HcY_DPZ8VRFpOVsHiVwuM4pSXzxO14nIpui4v4keXOU7MyNBx9k8uGuhoqVT9G7UDg3hMgHZ1UBFpzE6eWks08YjGpWy5ZreEDvrlQOpa4LY9fuAp1lDhDo5Z8TnhfH-f7rTiDtnaYk8dRktif5TLn7PjfzpceVhQ0zm2yGphp1DjRHm2TOsma_Ei3jQbWzkrRjW7y60w=', start_index=16538)

## Sources
