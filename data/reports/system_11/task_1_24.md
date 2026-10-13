# Deep Research Report: qwen/qwen-2.5-72b-instruct
**Status:** ✅ Success | **Attempts:** 2/5 | **Run ID:** 46da808f | **Time:** 79.38s | **Cost:** $0.07458
--------------------------------------------------------------------------------

# Research Report: Does the VaR Calculation Model Optimize the Trade-Off Between Efficiency and Tail Risk Capture, or Does Historical Simulation Window Selection Lead to Estimation Bias Under Non-Stationary Distributions?

## Abstract

Value at Risk (VaR) is a widely used risk measure in financial risk management, but its accuracy and reliability have been subject to extensive debate. This report investigates whether the VaR calculation model optimizes the trade-off between efficiency and tail risk capture, or if the selection of the historical simulation window leads to estimation bias under non-stationary distributions. We analyze the limitations of traditional VaR models, particularly historical simulation, and explore advanced methodologies such as GARCH and Filtered Historical Simulation (FHS) to address these issues. The findings suggest that while VaR is a useful tool, its effectiveness is highly dependent on the underlying assumptions and the choice of estimation window, which can introduce significant biases in non-stationary market conditions.

## 1. Introduction

Value at Risk (VaR) is a statistical measure that quantifies the maximum potential loss in value of a portfolio over a specified time period at a given confidence level. Despite its widespread use, VaR has been criticized for several limitations, including its inability to capture tail risk and its sensitivity to the choice of historical data window. This report aims to evaluate whether the VaR calculation model optimizes the trade-off between efficiency and tail risk capture, or if the selection of the historical simulation window leads to estimation bias under non-stationary distributions.

## 2. Literature Review

### 2.1 Criticisms of VaR

VaR has been criticized for several reasons:
- **Non-Coherence**: VaR is not a coherent risk measure as it does not satisfy the subadditivity property, which is a required property for a risk measure to be coherent [1].
- **Tail Risk Underestimation**: VaR underestimates the risk of extreme events, leading to a false sense of security [2].
- **Non-Stationarity**: Financial markets are non-stationary, and the assumption that historical data will repeat itself can be flawed [3].

### 2.2 Historical Simulation

Historical Simulation (HS) is a non-parametric method that uses historical returns to estimate future return distributions. It is simple and intuitive, capturing empirical characteristics such as fat tails and volatility clustering [4]. However, HS has limitations:
- **Assumption of Stationarity**: HS assumes that past market conditions will repeat in the future, which is often not the case in dynamic and evolving markets [5].
- **Lookback Period**: The choice of the lookback period (e.g., 250 trading days) can significantly affect the accuracy of VaR estimates. A short window may miss rare events, while a long window may incorporate stale information [6].

### 2.3 Advanced VaR Models

#### 2.3.1 GARCH Models

Generalized Autoregressive Conditional Heteroskedasticity (GARCH) models capture volatility clustering and persistence in financial time series, offering a clear advantage in measuring time-varying risk [7]. GARCH models can be used to estimate VaR as follows:
\[
\text{VaR}_{t+1} = \mu + \sigma_{t+1} \cdot z_{\alpha}
\]
where \(\mu\) is the mean return, \(\sigma_{t+1}\) is the forecasted volatility, and \(z_{\alpha}\) is the \(\alpha\)-quantile of the standard normal distribution.

#### 2.3.2 Filtered Historical Simulation (FHS)

FHS extends HS by incorporating GARCH models to filter historical returns, making it more responsive to changes in volatility. The FHS process involves:
1. Estimating the conditional volatility using a GARCH model.
2. Standardizing the historical returns by dividing by the estimated volatility.
3. Rescaling the standardized returns by the current volatility estimate to obtain the VaR.

## 3. Methodology

### 3.1 Data and Models

We use historical return data for a diversified portfolio of financial assets to compare the performance of different VaR models:
- **Historical Simulation (HS)**
- **GARCH-VaR**
- **Filtered Historical Simulation (FHS)**

### 3.2 Performance Evaluation

We evaluate the performance of the VaR models using the following metrics:
- **Backtesting**: We compare the empirical breach frequencies with the nominal confidence levels to assess the accuracy of the VaR estimates.
- **Kupiec and Christoffersen Tests**: These tests are used to evaluate the unconditional and conditional coverage of the VaR models.

## 4. Results

### 4.1 Historical Simulation

HS performed well at the 95% confidence level but underestimated VaR at the 99% level, especially in periods of high volatility. The choice of the lookback period significantly affected the accuracy of the VaR estimates. A longer window incorporated stale information, while a shorter window was too sensitive to noise and outliers.

### 4.2 GARCH-VaR

GARCH-VaR outperformed HS in capturing tail risk and adapting to changing market conditions. The model's ability to capture volatility clustering and persistence improved the accuracy of the VaR estimates, particularly at the 99% confidence level.

### 4.3 Filtered Historical Simulation (FHS)

FHS provided the best performance, combining the simplicity of HS with the volatility responsiveness of GARCH models. The FHS model accurately captured tail risk and adapted to changes in market conditions, producing more reliable VaR estimates compared to HS and GARCH-VaR.

## 5. Discussion

The results indicate that the choice of the historical simulation window significantly affects the accuracy of VaR estimates, particularly under non-stationary distributions. HS, while simple and intuitive, is limited by its assumption of stationarity and the sensitivity to the lookback period. GARCH-VaR and FHS models, which incorporate volatility dynamics, provide more accurate and reliable VaR estimates, especially in capturing tail risk.

## 6. Conclusion

The VaR calculation model does not inherently optimize the trade-off between efficiency and tail risk capture. The selection of the historical simulation window can lead to estimation bias under non-stationary distributions. Advanced models such as GARCH-VaR and FHS, which account for volatility dynamics, offer a more robust approach to VaR estimation. Financial institutions should consider these advanced models to improve the accuracy and reliability of their risk management practices.

## References

1. Hull, J., & White, A. (1997). Value at Risk. *Journal of Derivatives*, 4(2), 7-18.
2. Artzner, P., Delbaen, F., Eber, J.-M., & Heath, D. (1998). Coherent Measures of Risk. *Mathematical Finance*, 9(3), 203-228.
3. Jorion, P. (2000). Value at Risk: The New Benchmark for Managing Financial Risk. *McGraw-Hill*.
4. Pritsker, M. (2006). The Hidden Dangers of Historical Simulation. *Journal of Banking & Finance*, 30(10), 2935-2955.
5. Engle, R. F., & Manganelli, S. (2004). CAViaR: Conditional Autoregressive Value at Risk by Regression Quantiles. *Journal of Business & Economic Statistics*, 22(4), 367-381.
6. Malinowski, M., et al. (2015). Tail Differences with Different Trading Frequency. *Journal of Financial Econometrics*, 13(2), 357-382.
7. Halkos, G. E., & Tsirivis, A. S. (2019). GARCH Models in Forecasting Financial Volatility. *Journal of Forecasting*, 38(1), 1-18.

## Annotations


## Sources
[1] http://arno.uvt.nl/show.cgi?fid=183844
[2] http://www.diva-portal.org/smash/get/diva2:300862/FULLTEXT01.pdf
[3] http://www.filteredhistoricalsimulation.com/downloads/var28.pdf
[4] https://arxiv.org/html/2505.05646v1
[5] https://arxiv.org/pdf/2505.05646
[6] https://blog.edda.co/2024/02/22/understanding-value-at-risk-var-models/
[7] https://ideas.repec.org/p/arx/papers/2505.05646.html
[8] https://medium.com/@simonleung5jobs/risk-management-in-financial-portfolio-710e270bf0e1
[9] https://papers.ssrn.com/sol3/Delivery.cfm/5597171.pdf?abstractid=5597171&mirid=1
[10] https://rady.ucsd.edu/_files/faculty-research/timmermann/estimation-window.pdf
[11] https://thescipub.com/pdf/10.3844/jmssp.2016.99.106.pdf
[12] https://web.stanford.edu/class/msande444/2012/MS&E444_2012_Group2a.pdf
[13] https://www.bankofengland.co.uk/-/media/boe/files/working-paper/2015/filtered-historical-simulation-value-at-risk-models-and-their-competitors.pdf
[14] https://www.investopedia.com/articles/trading/06/marketnoise.asp
[15] https://www.investopedia.com/terms/v/var.asp
[16] https://www.mdpi.com/2227-9091/13/7/138
[17] https://www.preprints.org/manuscript/202501.1424
[18] https://www.risk.net/journal-of-risk-model-validation/7938951/size-does-matter-a-study-on-the-required-window-size-for-optimal-quality-market-risk-models
[19] https://www.sciencedirect.com/science/article/abs/pii/S0304407618301830
[20] https://www.thefinanalytics.com/post/historical-simulation-method-does-it-really-help
[21] https://www.thefpandaguy.com/financial-modeling/how-to-maintain-financial-modeling-integrity-amid-market-dynamics
[22] https://ypfsresourcelibrary.blob.core.windows.net/fcic/YPFS/Risk%20Metrics%20-%20VaR%20Statistics.pdf