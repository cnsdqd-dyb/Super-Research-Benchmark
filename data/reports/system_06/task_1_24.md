# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** a60fac9d | **Time:** 191.57s | **Cost:** $0.03580
--------------------------------------------------------------------------------

# Does the VaR Calculation Model Optimize the Trade-Off Between Efficiency and Tail Risk Capture, or Does Historical Simulation Window Selection Lead to Estimation Bias Under Non-Stationary Distributions?

## Abstract

This research report examines a fundamental tension in Value-at-Risk (VaR) modeling: whether existing methodologies successfully balance computational efficiency with accurate tail risk capture, or whether the selection of historical simulation windows introduces systematic estimation bias when underlying return distributions exhibit non-stationary behavior. Drawing upon recent empirical studies and established theoretical frameworks, this analysis investigates the structural limitations of traditional VaR approaches, particularly Historical Simulation (HS), under conditions of market volatility, heteroskedasticity, and regime switching. The evidence suggests that static historical simulation methods suffer from inherent estimation bias stemming from inappropriate window calibration, with longer windows incorporating stale information from outdated market regimes while shorter windows exhibit excessive sensitivity to noise and outliers. Furthermore, the assumption of identically distributed returns within estimation windows proves problematic when return volatility is heteroskedastic—a characteristic prevalent in financial markets. This report concludes that achieving optimal trade-offs between efficiency and tail risk capture requires adaptive windowing techniques, volatility-adjusted methodologies such as Filtered Historical Simulation (FHS), or expectile-based frameworks that account for time-varying risk dynamics and asymmetric market behavior.

---

## 1. Introduction

### 1.1 Background and Motivation

Value-at-Risk remains one of the most widely adopted risk measurement tools in financial institutions, regulatory frameworks, and investment management practices. Despite its ubiquity, the methodology underlying VaR calculation continues to face significant challenges in accurately capturing tail risk—the potential for extreme losses that, while infrequent, can have catastrophic consequences for financial portfolios. The fundamental question this report addresses is whether current VaR calculation models successfully navigate the inherent trade-off between computational efficiency and robust tail risk estimation, or whether methodological choices—particularly regarding historical simulation window selection—introduce systematic biases that compromise risk assessment accuracy.

The importance of this inquiry extends beyond academic interest. Regulatory frameworks such as the Basel Accords and the Fundamental Review of the Trading Book (FRTB) mandate specific approaches to VaR calculation, with the European Banking Authority reporting that 58% of surveyed banks with approved internal models employ a one-year estimation period, while 42% utilize longer windows [7]. These choices have direct implications for capital adequacy requirements, risk management practices, and financial stability. Understanding whether these approaches optimize the efficiency-tail risk trade-off or introduce estimation bias is therefore critical for both practitioners and regulators.

### 1.2 Research Objectives

This report pursues three primary objectives. First, it examines the theoretical foundations and practical implementations of major VaR calculation methodologies, with particular emphasis on Historical Simulation and its variants. Second, it investigates how historical simulation window selection affects estimation accuracy under conditions of non-stationary return distributions, volatility clustering, and regime switching. Third, it evaluates emerging approaches—including Filtered Historical Simulation, GARCH-based methods, and expectile-based frameworks—that attempt to address the limitations of traditional VaR models.

### 1.3 Scope and Structure

The analysis that follows is organized into seven major sections. Section 2 provides a comprehensive review of VaR calculation methodologies, examining the theoretical underpinnings and practical implementations of Historical Simulation, parametric approaches, and Monte Carlo simulation. Section 3 analyzes the critical issue of historical simulation window selection and its implications for estimation bias. Section 4 investigates the challenges posed by non-stationary distributions, heteroskedasticity, and regime switching. Section 5 evaluates advanced methodologies designed to address these challenges, including Filtered Historical Simulation and expectile-based approaches. Section 6 presents empirical evidence from comparative studies of VaR model performance. Section 7 synthesizes the findings and offers conclusions regarding the optimization of the efficiency-tail risk trade-off.

---

## 2. Value-at-Risk Calculation Methodologies: A Comprehensive Review

### 2.1 Foundational Concepts and Mathematical Framework

Value-at-Risk represents the maximum potential loss on a portfolio over a specified time horizon at a given confidence level. Mathematically, for a portfolio with return distribution $R_t$ at time $t$, the VaR at confidence level $\alpha$ is defined as:

$$\text{VaR}_{\alpha,t} = -\inf\{r \in \mathbb{R}: P(R_t \leq r) > \alpha\}$$

This formulation captures the $\alpha$-quantile of the return distribution, representing the loss level that will not be exceeded with probability $\alpha$. The choice of confidence level—typically 95%, 99%, or 99.9% depending on regulatory requirements and institutional risk appetite—directly affects the emphasis placed on tail risk capture versus computational efficiency [5].

The mathematical simplicity of this definition belies the substantial methodological challenges involved in accurately estimating the relevant quantile of the return distribution. As noted in the literature, "the VaR concept is very simple, its calculation is not easy" [10]. The difficulty arises from the need to model or estimate the entire return distribution, particularly its tail behavior, under conditions of uncertainty regarding the underlying data-generating process.

### 2.2 Historical Simulation: Principles and Implementation

Historical Simulation represents the most widely used non-parametric approach to VaR estimation, valued for its conceptual simplicity and minimal distributional assumptions. The method operates on the premise that historical patterns will repeat in the future, using observed returns during a specific past period to construct an empirical frequency distribution of potential profits and losses [4]. The VaR is then determined by selecting the appropriate quantile corresponding to the chosen confidence level from this empirical distribution.

The mathematical formulation of Historical Simulation VaR can be expressed as follows. Given a sequence of historical returns $\{r_{t-\tau}\}_{\tau=1}^{m}$ observed over a window of $m$ days, the VaR at confidence level $\alpha$ is:

$$\text{VaR}_{\alpha,t}^{\text{HS}} = -\text{percentile}\left(\{r_{t-\tau}\}_{\tau=1}^{m}, \alpha\right)$$

This approach offers several advantages that explain its popularity in practice. First, it makes no a priori assumptions about the distribution of asset returns, allowing it to capture empirical characteristics such as fat tails and volatility clustering without explicit modeling [4]. Second, it is straightforward to implement, requiring only the collection and sorting of historical return data. Third, it can be applied directly to any security or portfolio without the need for position mapping or factor decomposition.

However, the apparent simplicity of Historical Simulation masks significant methodological limitations that affect its ability to optimize the trade-off between efficiency and tail risk capture. The method implicitly assumes that "the distribution of past returns is a good and complete representation of expected future returns" [13]. In markets characterized by evolving risk dynamics, structural breaks, and non-stationary behavior, this assumption becomes increasingly problematic.

### 2.3 Parametric and Variance-Covariance Approaches

Parametric VaR methods, also known as variance-covariance or delta-normal approaches, assume that asset returns follow a specific probability distribution—typically the normal distribution—and estimate the required parameters from historical data. Under the assumption of normally distributed returns with mean $\mu$ and standard deviation $\sigma$, the VaR at confidence level $\alpha$ for a portfolio with value $V$ is:

$$\text{VaR}_{\alpha} = V \cdot (\mu + \sigma \cdot z_{\alpha})$$

where $z_{\alpha}$ is the $\alpha$-quantile of the standard normal distribution.

The parametric approach offers computational efficiency and analytical tractability, but its reliance on distributional assumptions introduces systematic bias when actual return distributions exhibit characteristics inconsistent with the assumed form. As documented extensively in the financial literature, "there is significant evidence that most return series show fatter tails" than the normal distribution predicts [11]. This phenomenon—known as leptokurtosis—means that parametric VaR models systematically underestimate the probability of extreme losses, compromising tail risk capture.

### 2.4 Monte Carlo Simulation

Monte Carlo simulation represents the most flexible VaR calculation methodology, generating thousands of hypothetical market scenarios by drawing from specified distributions of risk factors. Each simulated scenario produces a hypothetical portfolio loss distribution, from which the VaR is extracted as the $\alpha$-quantile [5]. The method can incorporate non-linear payoffs, fat-tailed distributions, stochastic volatilities, and complex dependency structures through copula modeling.

The flexibility of Monte Carlo simulation comes at the cost of computational intensity and model risk. Users must correctly specify the stochastic processes governing risk factor dynamics, the marginal distributions of individual factors, and the dependence structure linking them. Misspecification at any of these levels can lead to biased VaR estimates. Recent research has proposed iterative optimization processes that adjust Monte Carlo simulations to accommodate recent shocks and incorporate the latest market conditions, with empirical validation showing improved reliability and consistency compared to simple Monte Carlo approaches [14].

---

## 3. Historical Simulation Window Selection and Estimation Bias

### 3.1 The Window Length Trade-Off

The selection of an appropriate historical window length represents one of the most consequential methodological decisions in Historical Simulation VaR estimation. This choice embodies a fundamental trade-off: longer windows incorporate more historical observations, potentially providing more stable quantile estimates, but risk including "stale information from outdated regimes" that may no longer be relevant to current market conditions [1]. Conversely, shorter windows respond more quickly to recent market developments but may be "too sensitive to noise and outliers," producing volatile VaR estimates that fail to distinguish between genuine risk signals and random fluctuations.

The European Banking Authority's benchmarking study reveals substantial heterogeneity in institutional practice, with 58% of surveyed banks employing a one-year estimation window and others utilizing lengthier periods [7]. The FRTB framework favors a one-year period, which can be shortened during times of stress but cannot be less than six months. These regulatory prescriptions reflect an attempt to balance the competing considerations of statistical stability and responsiveness, but they do not resolve the underlying tension.

### 3.2 Stale Information and Regime Persistence

When longer historical windows are employed, the resulting VaR estimates may reflect market conditions that are no longer representative of current risk dynamics. This phenomenon is particularly problematic during periods of regime change, when the statistical properties of return distributions undergo structural shifts. As noted in the literature, "if the underlying return distribution exhibits large fluctuations or abrupt structural shifts, then the assumption of a static historical distribution becomes invalid" [1].

The consequences of stale information are evident in the behavior of VaR breach indicators. Visual inspection of breach time series reveals that Historical Simulation methods exhibit "breach indicators densely packed across the entire sample period, with very few non-breach days," suggesting "extremely poor model calibration and almost no discrimination of market risk dynamics" [1]. The persistence of breaches indicates "structural failure in risk estimation" rather than random statistical fluctuations.

### 3.3 Noise Sensitivity and Outlier Reactivity

Shorter historical windows, while more responsive to recent market conditions, introduce their own estimation biases. With fewer observations, the empirical quantile estimate becomes more sensitive to individual extreme events, potentially producing VaR estimates that overreact to short-term volatility spikes. This noise sensitivity can lead to unstable risk estimates that complicate risk management and capital allocation decisions.

The problem is exacerbated by the presence of outliers in the historical sample. A single extreme loss event can dramatically shift the empirical quantile estimate when the window is small, creating VaR "bumps" that reflect dataset composition rather than genuine changes in risk [11]. As observations fall out of the dataset because they are "too far in the past," VaR estimates may shift drastically, indicating that "the model is not robust for changes in the dataset."

### 3.4 Rolling Window Implementation and Look-Ahead Bias

The standard approach to implementing Historical Simulation involves a rolling window mechanism, where model parameters are estimated using only historical data within a fixed-size window, and the resulting estimates are used to forecast VaR for the next trading day [8]. This approach "effectively mitigates estimation bias caused by look-ahead information" by "continuously discarding outdated observations and incorporating the most recent data."

However, the rolling window approach does not resolve the fundamental tension between window length and estimation accuracy. It merely relocates the methodological choice from a static parameter to a dynamic one. The optimal window length may itself be time-varying, with different regimes requiring different calibration. Static window selection, regardless of the specific length chosen, cannot adapt to changing market conditions without explicit regime detection mechanisms.

---

## 4. Non-Stationary Distributions and Time-Varying Risk Dynamics

### 4.1 Heteroskedasticity and the Identically Distributed Assumption

A fundamental assumption underlying many VaR estimation methods is that returns within the estimation window are identically distributed. This assumption is violated when return volatility is heteroskedastic—characterized by periods of high volatility followed by periods of calm, a phenomenon known as volatility clustering that is "often observed in financial returns" [12]. When volatility is time-varying, the unconditional distribution of returns within a historical window may be a mixture of distributions corresponding to different volatility states, complicating quantile estimation.

The implications for Historical Simulation are particularly severe. The method implicitly assumes that the empirical distribution of past returns accurately represents the distribution of future returns. When the data-generating process is heteroskedastic, this assumption fails because the relative frequency of high-volatility observations in the historical sample may not match their probability of occurrence in the future. During periods of elevated volatility, Historical Simulation VaR estimates based on windows that include insufficient high-volatility observations will systematically underestimate tail risk.

### 4.2 Structural Non-Stationarity and Regime Switching

Financial markets frequently exhibit structural non-stationarity, with the parameters of return distributions undergoing discrete shifts in response to economic events, policy changes, or financial crises. These regime switches create fundamental challenges for VaR estimation methods that rely on historical data to infer future risk characteristics.

Recent research employing regime-switching analysis has identified "distinct market regimes with different risk characteristics," demonstrating that "the ability of expectile models to capture these regime-dependent patterns represents a significant advancement over static approaches" [3]. Static VaR models, including traditional Historical Simulation, cannot adapt to regime changes without explicit mechanisms for regime detection and model switching.

The failure of Historical Simulation to account for structural non-stationarity is reflected in its poor backtesting performance during crisis periods. Studies comparing VaR methodologies across different market conditions find that Historical Simulation "may lead to poor backtesting results," with breach rates significantly exceeding the expected level during volatile periods [7]. This systematic underperformance suggests that the limitations of Historical Simulation "may not only stem from model bias or estimation error, but also from deeper issues such as structural non-stationarity, volatility clustering, and inappropriate window calibration" [1].

### 4.3 Asymmetric Volatility and Tail Behavior

Financial markets commonly exhibit asymmetric volatility dynamics, where downward price movements are associated with higher subsequent volatility than upward movements of equivalent magnitude. This leverage effect violates the symmetry assumptions implicit in many VaR models and creates challenges for accurate tail risk estimation.

Traditional symmetric VaR models "fail to capture the asymmetric nature of tail risk," particularly during periods "when markets experience sharp declines followed by gradual recoveries" [3]. The expectile framework, with its "inherent sensitivity to tail magnitudes," provides more accurate risk assessment in these conditions by weighting losses above the expectile more heavily than equivalent gains below it. This asymmetric treatment better reflects the empirical reality of financial markets, where downside risk carries different implications than upside potential.

---

## 5. Advanced Methodologies for Improved Tail Risk Capture

### 5.1 Filtered Historical Simulation

Filtered Historical Simulation (FHS) represents one of the most significant advances in VaR methodology, addressing the limitations of plain Historical Simulation by explicitly modeling time-varying volatility. The approach involves two stages: first, filtering historical returns through a volatility model (typically GARCH) to obtain standardized residuals; second, bootstrapping these residuals to generate simulated returns that reflect current volatility conditions [7].

The mathematical formulation of FHS involves scaling historical returns according to a revolatile and devolatile process:

$$\tilde{r}_t = \frac{\sigma_T}{\sigma_t} r_t, \quad 1 \leq t \leq T$$

where $\sigma_T$ is the most recent forecast of volatility and $\sigma_t$ is the volatility estimate for date $t$ [7]. This transformation adjusts historical observations to reflect current market conditions, effectively removing stale information about past volatility levels while preserving the empirical distribution of standardized returns.

Empirical evidence strongly supports the superiority of FHS over plain Historical Simulation. Research comparing multiple VaR methodologies concludes that "FHS is more accurate than both plain historical simulation and BRW [Bootstrapped Ranked Weighted] estimators" [7]. The approach "accounts for volatility changes" and "is the most robust to the choice of data window length," addressing both major sources of estimation bias in traditional Historical Simulation.

### 5.2 GARCH-Based Approaches

Generalized Autoregressive Conditional Heteroskedasticity (GARCH) models explicitly capture time-varying volatility, providing a parametric framework for modeling the dynamic structure of financial return distributions. When combined with appropriate distributional assumptions for standardized residuals, GARCH models can produce VaR estimates that adapt to changing market conditions.

However, GARCH-based VaR estimation faces its own challenges. The common assumption that standardized residuals follow a normal distribution leads to "structural underestimation of tail risk" [1]. Visual inspection of breach indicators for GARCH + Normal methods reveals that "breaches under this method appear more evenly spread over time compared to HS, their overall frequency remains significantly higher than the expected 5% threshold," indicating persistent tail risk underestimation.

The solution involves combining GARCH volatility modeling with fat-tailed distributions for the standardized residuals. As documented in the literature, "the asymmetric GARCH model under both a normal and a Student's t-distribution of returns" allows for the leverage effect while capturing the fat tails characteristic of financial returns [12]. The t-distribution provides sufficient flexibility to model excess kurtosis without the computational complexity of more elaborate alternatives.

### 5.3 Extreme Value Theory Approaches

Extreme Value Theory (EVT) provides a rigorous statistical framework for modeling the tails of return distributions, focusing directly on the extreme observations that determine VaR estimates. Two primary approaches have been developed: the block maxima method, which models the distribution of maximum losses over fixed periods, and the peaks-over-threshold (POT) method, which models losses exceeding a specified threshold.

Research comparing VaR methodologies finds that "the combination of either the block maxima method or the POT method with traditional time series modelling, into what we call conditional EVT, does the best job both in tranquil and volatile periods" [2]. This superior performance reflects EVT's focus on tail behavior rather than the entire distribution, allowing more efficient use of limited extreme observations.

The integration of EVT with GARCH modeling—known as GARCH-EVT—provides a comprehensive framework that captures both time-varying volatility and fat-tailed return distributions. Recent applications to green asset markets demonstrate that "GARCH–EVT–VaR models based on normal and t-distributions" effectively capture tail risk in diverse asset classes [8].

### 5.4 Expectile-Based Risk Measures

Expectile-based risk measures, including the Expected Value-at-Risk (EVaR), represent an emerging approach that addresses limitations of traditional VaR by incorporating asymmetric weighting of tail outcomes. Unlike VaR, which considers only the quantile threshold, expectiles average all observations beyond the threshold, providing coherent risk measures that are more sensitive to tail magnitude.

Empirical validation during the extreme volatility of March 2020, "when the FTSE 100 experienced daily moves exceeding 10%," demonstrates that "the EVaR model provided more timely and accurate risk warnings" compared to traditional VaR models, which "either failed to capture the magnitude of tail risk or over-reacted to short-term volatility spikes" [3]. The "superior performance of expectile-based methods is particularly evident during periods of asymmetric volatility," where traditional symmetric VaR models fail to capture the differential treatment of gains and losses.

The comparative analysis reveals "substantial improvements across all confidence levels, with particularly pronounced benefits for extreme tail events (99% confidence level)" [3]. This enhanced performance at extreme quantiles suggests that expectile-based methods may be particularly valuable for regulatory capital calculation and risk management during periods of market stress.

---

## 6. Empirical Evidence from Comparative Studies

### 6.1 Backtesting Framework and Evaluation Criteria

Rigorous evaluation of VaR model performance requires systematic backtesting procedures that compare predicted VaR estimates with realized outcomes. The Kupiec test (Proportion of Failures test) and Christoffersen test (Conditional Coverage test) represent the standard statistical framework for evaluating VaR forecast accuracy, testing whether the frequency and clustering of VaR breaches are consistent with the specified confidence level [8].

Backtesting should be conducted not only under normal market conditions but also during stressed periods, as "the backtesting requirement should not thus be dismissed and (internally) assessed over a stressed period, on top of day to day monitoring, in order to assess the resilience of a risk model" [7]. This comprehensive approach reveals model weaknesses that may be masked during tranquil periods but become critical during market stress.

### 6.2 Comparative Performance Across Market Regimes

Empirical studies comparing VaR methodologies across different market regimes reveal substantial variation in model performance. During stable periods, simpler methods such as Historical Simulation may perform adequately, but their limitations become apparent during volatile periods when accurate tail risk capture is most critical.

Research examining VaR performance across different asset classes finds that "the parametric VaR with a random walk specification was the most accurate" for euro exchange rate forecasting, underscoring "the importance of aligning model selection with asset-specific characteristics" [8]. Similarly, "range-based GARCH models with bounded M-estimators" have been shown to "outperform traditional models during periods of market stress" [8], suggesting that volatility specification significantly affects tail risk capture.

The performance hierarchy among VaR methods is not uniform across all market conditions. Studies comparing historical simulation, Monte Carlo simulation, parametric methods, and extreme value theory find that "among the methodologies developed initially, no approach appeared to perform better than the others" when evaluated across all conditions [10]. However, when evaluated separately during tranquil and volatile periods, EVT-based methods demonstrate superior performance in both regimes [2].

### 6.3 Window Length Sensitivity Analysis

The sensitivity of VaR estimates to window length selection has been systematically investigated through empirical studies. Research comparing plain historical VaR based on rolling windows of different lengths reveals that "plain historical simulation may lead to poor backtesting results" when window calibration is inappropriate for current market conditions [7].

Filtered Historical Simulation demonstrates greater robustness to window length selection compared to plain Historical Simulation. The FHS approach "is the most robust to the choice of data window length" because the volatility filtering stage adjusts for changes in market conditions regardless of the historical period from which observations are drawn [7]. This robustness property has important practical implications, as it reduces the sensitivity of VaR estimates to what is ultimately an arbitrary methodological choice.

---

## 7. Synthesis and Conclusions

### 7.1 The Efficiency-Tail Risk Trade-Off: A Critical Assessment

The evidence synthesized in this report suggests that traditional VaR calculation models, particularly Historical Simulation, do not optimally balance efficiency and tail risk capture when applied to financial markets exhibiting non-stationary behavior. The fundamental limitation lies not in the concept of VaR itself but in the methodological choices required for practical implementation.

Historical Simulation's efficiency advantage—computational simplicity and minimal distributional assumptions—comes at the cost of systematic estimation bias under non-stationary conditions. The method's reliance on static historical distributions fails to account for time-varying volatility, regime switching, and structural breaks that characterize actual financial markets. The window selection problem embodies this trade-off: longer windows sacrifice responsiveness to current conditions, while shorter windows sacrifice statistical stability.

### 7.2 Estimation Bias from Window Selection

The historical simulation window selection problem leads to estimation bias through multiple mechanisms. Stale information from outdated market regimes contaminates VaR estimates when longer windows are employed, while noise sensitivity and outlier reactivity distort estimates when shorter windows are used. Neither extreme optimizes the efficiency-tail risk trade-off; instead, both introduce systematic biases that compromise risk assessment accuracy.

The bias is particularly severe during regime transitions, when the statistical properties of return distributions undergo structural shifts. Static Historical Simulation cannot detect or adapt to these changes, resulting in VaR estimates that reflect historical rather than current risk conditions. The consequence is systematic underestimation of tail risk during volatile periods, when accurate risk assessment is most critical.

### 7.3 Recommendations for Improved Practice

Based on the evidence presented, several recommendations emerge for practitioners seeking to improve VaR estimation accuracy while maintaining computational feasibility. First, Filtered Historical Simulation should be preferred over plain Historical Simulation due to its explicit treatment of time-varying volatility and greater robustness to window length selection. Second, GARCH-based approaches with fat-tailed distributions for standardized residuals provide a parametric framework that captures both volatility clustering and excess kurtosis. Third, expectile-based measures offer advantages for capturing asymmetric tail risk and may provide more timely warnings during market stress.

For regulatory purposes, the evidence supports frameworks that allow flexibility in methodology selection based on asset class characteristics and market conditions. The FRTB's one-year window prescription represents a reasonable default but may benefit from supplementary approaches during periods of elevated volatility. Adaptive windowing techniques that adjust calibration based on detected regime changes offer promise for addressing the limitations of static approaches.

### 7.4 Future Research Directions

Several avenues for future research emerge from this analysis. The development of real-time risk monitoring systems that "balance accuracy with computational efficiency whilst providing timely risk warnings during rapidly evolving market conditions" represents an important practical challenge [3]. The investigation of expectile-based risk measures for alternative assets, including cryptocurrencies, commodities, and structured products, would extend the applicability of improved frameworks to markets that "often exhibit extreme tail behaviour" [3].

Additionally, the integration of machine learning techniques with traditional econometric approaches may provide new methods for regime detection and adaptive model selection. The goal remains the development of VaR methodologies that successfully navigate the inherent trade-off between computational efficiency and robust tail risk capture, providing accurate risk assessment across diverse market conditions without sacrificing practical implementability.

---

## References

[1] arXiv:2505.05646 - Analysis of Historical Simulation VaR limitations under volatile market regimes and structural non-stationarity.

[2] ScienceDirect (S1057521904000110) - Evaluation of EVT-based models for tail risk modeling and VaR estimation across tranquil and volatile periods.

[3] arXiv:2507.13391 - Expectile-based risk measures and EVaR framework for enhanced tail risk capture during market stress.

[4] ARNO UVT (183844) - Historical Simulation methodology and limitations in emerging markets with non-standard return characteristics.

[5] The Fin Analytics - Comprehensive review of VaR calculation methodologies, assumptions, and limitations.

[6] MDPI (2227-9091/13/7/138) - Advances in tail risk measurement methodologies and comparative VaR model performance.

[7] HAL (hal-03679434) - VaR backtesting, EWMA models, and Filtered Historical Simulation robustness analysis.

[8] MDPI (2227-9091/13/7/138) - Rolling window VaR estimation and AR-EGARCH-EVT model performance evaluation.

[9] YouTube/Nuttle - Practical VaR calculation methodologies including historical simulation implementation.

[10] Elsevier (A comprehensive review of Value-at-Risk methodologies) - Comparative evaluation of initial VaR methodologies.

[11] Stanford MS&E444 (2012) - Monte Carlo VaR implementation and historical simulation limitations.

[12] ScienceDirect (S0378475412001218) - Comparison of VaR methodologies including extreme value theory approaches.

[13] NYU Stern (pages.stern.nyu.edu/~adamodar/pdfiles/papers/VAR.pdf) - Historical simulation weighting schemes and distributional assumptions.

[14] ScienceDirect (S1544612309000154) - Monte Carlo VaR optimization through iterative adjustment for recent market shocks.

## Annotations


## Sources
[1] http://arno.uvt.nl/show.cgi?fid=183844
[2] http://modelosfinanceiros.com.br/assets/documentos/backtesting_of_a_monte_carlo_value_at_risk.pdf
[3] https://arxiv.org/html/2507.13391v1
[4] https://arxiv.org/pdf/2505.05646
[5] https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/VAR.pdf
[6] https://paris1.hal.science/hal-03679434/document
[7] https://web.stanford.edu/class/msande444/2012/MS&E444_2012_Group2a.pdf
[8] https://www.elsevier.es/en-revista-the-spanish-review-financial-economics-332-articulo-a-comprehensive-review-value-at-S217312681300017X?redirectNew=true
[9] https://www.mdpi.com/2227-9091/13/7/138
[10] https://www.sciencedirect.com/science/article/abs/pii/S0378475412001218
[11] https://www.sciencedirect.com/science/article/abs/pii/S1057521904000110
[12] https://www.sciencedirect.com/science/article/abs/pii/S1544612309000154
[13] https://www.thefinanalytics.com/post/value-at-risk-for-risk-professionals-methodologies-computation-and-practical-applications
[14] https://www.youtube.com/watch?v=ThIYsyKXHds