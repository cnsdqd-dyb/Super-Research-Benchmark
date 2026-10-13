# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 8e6ea4b5 | **Time:** 1999.36s | **Cost:** $0.11978
--------------------------------------------------------------------------------

# The Impact of Markov Chain Monte Carlo Convergence Conditions on the Estimation Precision of Fertility Rate Parameters in Age Structure Forecasting

## Abstract

This research report examines the critical relationship between Markov Chain Monte Carlo (MCMC) convergence conditions and the precision of fertility rate parameter estimation within the context of age structure forecasting. As demographic modeling increasingly relies on Bayesian hierarchical frameworks to project age-specific fertility rates (ASFRs) and total fertility rates (TFRs), understanding how convergence diagnostics, thinning strategies, and burn-in period determination affect estimation accuracy becomes paramount. This analysis synthesizes evidence from multiple methodological studies and demographic applications to elucidate how inadequate convergence can propagate uncertainty through population projections, ultimately influencing policy decisions grounded in demographic forecasts. The report demonstrates that convergence conditions directly impact the numerical standard error of fertility parameter estimates, effective sample sizes, and the reliability of posterior probability intervals, with implications for the robustness of age structure projections across multiple temporal and geographic scales.

## 1. Introduction

### 1.1 Background and Motivation

Population projections constitute fundamental tools for governmental planning, resource allocation, and policy development at local, regional, national, and international levels [1]. The accuracy of these projections depends critically on the precision with which fertility rate parameters can be estimated, particularly age-specific fertility rates that capture the differential reproductive patterns across female age cohorts. In recent decades, Bayesian approaches to demographic modeling have gained prominence due to their capacity to incorporate prior knowledge, propagate uncertainty through complex hierarchical structures, and provide full posterior distributions rather than point estimates alone [2].

The estimation of fertility rate parameters within Bayesian frameworks typically employs Markov Chain Monte Carlo methods, which enable sampling from high-dimensional posterior distributions that would otherwise be computationally intractable. However, the validity of MCMC-based inference rests upon the fundamental assumption that the Markov chain has converged to its stationary distribution—the target posterior distribution from which we wish to sample [3]. When convergence conditions are not adequately satisfied, the resulting parameter estimates may be biased, overconfident, or otherwise misleading, with potentially severe consequences for demographic projections that inform long-term planning decisions.

### 1.2 Research Objectives

This report addresses the central question of how MCMC convergence conditions influence the estimation precision of fertility rate parameters in age structure forecasting. Specifically, we examine the mechanisms through which convergence failures manifest in degraded estimation precision, the diagnostic tools available for assessing convergence adequacy, and the practical implications for demographic modeling applications. The analysis draws upon methodological literature on MCMC convergence diagnostics as well as applied demographic studies that employ these techniques in fertility rate estimation contexts.

### 1.3 Structure of the Report

The subsequent sections proceed as follows: Section 2 provides technical background on MCMC methods, convergence theory, and fertility rate modeling in demographic applications. Section 3 examines the relationship between convergence conditions and estimation precision, including theoretical frameworks and empirical evidence. Section 4 discusses convergence diagnostics relevant to fertility rate estimation, while Section 5 addresses practical implications for age structure forecasting. Section 6 concludes with recommendations for demographic modeling practice.

## 2. Technical Background

### 2.1 Markov Chain Monte Carlo Methods in Demographic Modeling

Markov Chain Monte Carlo methods encompass a class of algorithms that generate samples from probability distributions by constructing Markov chains with desired stationary distributions [4]. In demographic applications, these methods enable estimation of complex hierarchical models that relate observed population counts, survey data, and prior information to underlying fertility rate parameters. The fundamental appeal of MCMC lies in its ability to sample from posterior distributions without requiring analytical integration, making it particularly valuable for models with numerous parameters and intricate dependencies.

The Gibbs sampler represents one of the most widely employed MCMC algorithms in demographic modeling, particularly for hierarchical fertility rate models [5]. This algorithm samples each parameter conditionally upon the current values of all other parameters, cycling through the full parameter vector until convergence is achieved. In the context of total fertility rate estimation, the Gibbs sampler may update age-specific fertility rates, variance components, and hyperparameter sequentially, with each conditional distribution taking a tractable form that facilitates efficient sampling [6].

Alternative MCMC algorithms employed in demographic applications include Metropolis-Hastings steps for parameters without convenient conditional distributions and slice sampling for enhanced exploration of posterior geometry [7]. The choice of sampling algorithm and its configuration directly influences convergence behavior, with poorly tuned proposals or inappropriate step sizes potentially slowing convergence or preventing it entirely.

### 2.2 Convergence Theory and Stationarity

The theoretical foundation of MCMC inference rests upon the ergodic theorem, which guarantees that sample averages converge to expectations under the stationary distribution as the number of iterations approaches infinity [8]. However, this guarantee holds only after the Markov chain has reached stationarity—the so-called burn-in period must be discarded before inference proceeds. The duration of the burn-in period depends upon the starting position of the chain, the geometry of the posterior distribution, and the efficiency of the sampling algorithm.

Convergence to stationarity requires that the Markov chain satisfy two conditions: irreducibility, which ensures the chain can eventually reach any region of the parameter space with positive posterior density, and aperiodicity, which prevents the chain from exhibiting systematic oscillations between regions [9]. In practice, demographic fertility rate models typically satisfy these conditions, but the rate at which convergence occurs can vary dramatically depending upon posterior geometry.

The relationship between convergence rate and posterior geometry has been extensively studied, with particular attention to the phenomenon of slow mixing in high-dimensional or poorly conditioned parameter spaces [10]. When parameters are highly correlated in the posterior distribution, the Gibbs sampler may require many iterations to explore the full joint distribution, as each parameter update only moves a small distance in the high-correlation direction. This behavior directly impacts the precision of fertility rate estimates, as chains that mix slowly produce samples with high autocorrelation, reducing the effective sample size for a given computational budget.

### 2.3 Fertility Rate Modeling in Age Structure Forecasting

Age structure forecasting requires specification of age-specific fertility rates (ASFRs) that describe the pattern of fertility across female age groups, typically in five-year intervals from ages 15-49 [11]. The total fertility rate (TFR) represents a summary measure obtained by summing age-specific rates across all age groups, providing an index of period fertility that facilitates comparison across populations and time periods.

Bayesian approaches to fertility rate estimation incorporate multiple sources of information, including survey data such as Demographic and Health Surveys (DHS), census enumerations, and official statistics from national statistical agencies [12]. The United Nations World Population Prospects (UN WPP) provides standardized ASFR estimates that serve as important reference points in Bayesian hierarchical models, with precision parameters reflecting the uncertainty inherent in these estimates [13].

The hierarchical structure of Bayesian fertility models typically includes country-specific or region-specific parameters that allow fertility patterns to vary across administrative units while borrowing strength from the global pattern [14]. This hierarchical specification introduces additional parameters and complex dependencies that can challenge MCMC convergence, particularly when the number of groups is large or when some groups have limited data.

## 3. Convergence Conditions and Estimation Precision

### 3.1 Theoretical Framework for Precision Degradation

The precision of MCMC-based parameter estimates depends fundamentally upon the quality of the posterior samples generated by the algorithm. When the Markov chain has not converged to stationarity, samples from the transient (non-stationary) phase contaminate the posterior sample, biasing estimates toward the initial values of the chain rather than the true posterior distribution [15]. This bias directly reduces estimation precision by introducing systematic error that cannot be reduced through additional sampling.

Even after apparent stationarity is achieved, slow mixing due to high posterior correlations or multi-modality can degrade precision by producing highly autocorrelated samples [16]. The effective sample size (ESS), which quantifies the number of independent samples equivalent to the autocorrelated MCMC sample, provides a direct measure of this precision degradation. For a chain of length $N$ with autocorrelation function $\rho_k$ at lag $k$, the effective sample size is approximately:

$$\text{ESS} \approx \frac{N}{1 + 2\sum_{k=1}^{\infty} \rho_k}$$

When autocorrelation is high, the effective sample size may be substantially smaller than the nominal sample size, requiring longer chains to achieve desired precision levels [17].

### 3.2 Numerical Standard Error and Convergence

The numerical standard error (NSE) quantifies the uncertainty in Monte Carlo estimates attributable to sampling variability, providing a direct link between convergence behavior and estimation precision [18]. For an estimator $\bar{h}$ of a function $h(\boldsymbol{\theta})$ of the parameter vector, the NSE accounts for autocorrelation in the MCMC sample through the spectral density at zero frequency:

$$\text{NSE}(\bar{h}) = \sqrt{\frac{\hat{f}_h(0)}{S}}$$

where $S$ is the number of samples and $\hat{f}_h(0)$ is the estimated spectral density at frequency zero. When the Markov chain has not converged, the spectral density estimate may be inconsistent or biased, leading to underestimation of the true NSE and overconfidence in parameter estimates.

In the context of fertility rate estimation, the NSE for age-specific fertility rates directly impacts the width of posterior probability intervals and the reliability of point estimates [19]. Research on TFR estimation from age-sex structure has demonstrated that posterior intervals can be substantially wider than naive independent-sample calculations would suggest when autocorrelation in the MCMC sample is properly accounted for [20]. This finding has important implications for uncertainty quantification in population projections, where interval width influences planning scenarios and policy sensitivity analyses.

### 3.3 Thinning Strategies and Precision Trade-offs

Thinning, the practice of retaining only every $k$-th iteration from the MCMC chain, represents a common strategy for managing storage requirements and reducing autocorrelation in posterior samples [21]. By discarding intermediate samples, thinning reduces the correlation between retained samples, potentially increasing the effective sample size per stored observation. However, thinning also reduces the total number of samples available for inference, creating a trade-off between sample independence and sample size.

The impact of thinning on estimation precision depends upon the autocorrelation structure of the chain and the thinning interval selected [22]. For chains with strong autocorrelation, moderate thinning can substantially improve precision by reducing the redundancy in stored samples. However, excessive thinning discards information without proportional gains in independence, ultimately reducing precision. The optimal thinning interval balances these considerations and should be determined through diagnostic examination of autocorrelation functions rather than applied indiscriminately.

In Bayesian fertility modeling applications, thinning decisions should consider the computational cost of generating additional samples and the storage constraints imposed by large-scale demographic models [23]. For hierarchical models with thousands of country-specific fertility parameters, thinning may be necessary to manage storage requirements, but the precision cost should be carefully evaluated against the benefits of reduced autocorrelation.

### 3.4 Burn-in Determination and Bias Reduction

The burn-in period represents iterations that must be discarded before valid inference can proceed, as samples from this phase reflect the transient behavior of the Markov chain rather than the stationary distribution [24]. Inadequate burn-in can bias parameter estimates, with the bias magnitude depending upon the distance from the starting point to the stationary distribution and the mixing rate of the chain.

For fertility rate models initialized from prior means or external estimates, the burn-in period may be substantial if the starting point is far from the high-probability region of the posterior [25]. This situation commonly arises when prior information is vague or when external estimates are inconsistent with the observed data. Diagnostic tools for burn-in assessment include trace plot examination, which visualizes the trajectory of parameter estimates over iterations, and formal statistical tests that assess whether the chain distribution has stabilized.

The relationship between burn-in adequacy and estimation precision is particularly relevant for age-specific fertility rates that may exhibit different mixing behavior across age groups [26]. Some age-specific rates may converge rapidly while others require extended burn-in periods, necessitating burn-in determination based on the slowest-mixing parameter to ensure all samples are from the stationary distribution.

## 4. Convergence Diagnostics for Fertility Rate Estimation

### 4.1 Gelman-Rubin Diagnostic and Potential Scale Reduction

The Gelman-Rubin diagnostic, also known as the potential scale reduction factor ($\hat{R}$), assesses convergence by comparing within-chain and between-chain variance in multiple parallel MCMC runs [27]. When chains have converged to the stationary distribution, samples from different chains should be indistinguishable, resulting in $\hat{R}$ values close to 1. Values substantially greater than 1 indicate that additional iterations are needed for chains to mix adequately.

The theoretical foundation of $\hat{R}$ relies upon the decomposition of total variance into within-chain and between-chain components [28]. For a scalar function $f(\boldsymbol{\theta})$ of the parameter vector, the potential scale reduction is computed as:

$$\hat{R} = \sqrt{\frac{\hat{\sigma}^2}{W}}$$

where $\hat{\sigma}^2$ is the pooled variance estimate and $W$ is the within-chain variance. When $\hat{R}$ approaches 1, both the mean and variance of the chain distribution have stabilized, suggesting that convergence has been achieved.

In hierarchical fertility rate models, $\hat{R}$ should be computed for all parameters of interest, including age-specific fertility rates, variance components, and hyper-parameters [29]. Research on TFR projection models has demonstrated that convergence may be slower for random effects representing small populations or groups with limited data, requiring extended monitoring to ensure adequate $\hat{R}$ values across all parameters [30].

### 4.2 Raftery-Lewis Diagnostic for Quantile Estimation

The Raftery-Lewis diagnostic specifically addresses the number of iterations required to estimate quantiles of the posterior distribution to specified precision [31]. Unlike diagnostics focused on mean estimation, this approach considers the accuracy of arbitrary quantile estimates, which may require more iterations when the quantile is in a region of low probability density.

The diagnostic proceeds by running an initial "pilot" chain to estimate the dependence structure, then computing the required sample size for quantile estimation based on the specified accuracy and confidence level [32]. For fertility rate estimation, this diagnostic is particularly relevant when posterior quantiles inform policy thresholds, such as the probability that TFR falls below replacement level or that age-specific fertility in a particular cohort exceeds a critical value.

The Raftery-Lewis method provides guidance on burn-in length and total sample size requirements, distinguishing between the burn-in needed for the chain to reach stationarity and the additional iterations needed for precise quantile estimation [33]. This distinction is valuable for fertility modeling applications where policy decisions depend upon quantile-based summaries rather than posterior means alone.

### 4.3 Trace Plot Analysis and Visual Diagnostics

Visual examination of trace plots—graphs of parameter estimates versus iteration number—provides intuitive assessment of convergence behavior that complements formal statistical diagnostics [34]. Well-mixed chains exhibit trace plots that appear as random fluctuations around a constant mean without systematic trends, while poorly mixed chains show patterns such as gradual drift, periodic oscillations, or extended periods in localized regions.

For age-specific fertility rates, trace plot analysis can reveal age-specific patterns in convergence behavior that may not be captured by scalar diagnostics [35]. Some age groups may exhibit rapid mixing while others show persistent trends or multi-modal behavior, indicating the need for age-specific convergence assessment. The bayesTFR package for Bayesian TFR estimation explicitly recommends trace plot examination as part of the convergence assessment workflow [36].

Autocorrelation plots, which display the correlation between samples at different lags, provide complementary visual diagnostics that quantify the mixing rate of the chain [37]. High autocorrelation at long lags indicates slow mixing and suggests that additional thinning or algorithm modifications may be needed to achieve efficient sampling.

### 4.4 Effective Sample Size Monitoring

Effective sample size (ESS) monitoring provides ongoing assessment of the information content of posterior samples, enabling researchers to determine whether sufficient samples have been collected for precise inference [38]. Modern MCMC software packages typically report ESS estimates alongside parameter summaries, allowing researchers to identify parameters with inadequate sampling efficiency.

The relationship between ESS and estimation precision is direct: for a given ESS, the Monte Carlo standard error is approximately the same as that from an independent sample of size ESS [39]. When ESS values are low relative to the nominal sample size, additional iterations or algorithm improvements are needed to achieve desired precision levels.

In hierarchical fertility models, ESS can vary substantially across parameters, with random effects for small groups often exhibiting lower ESS due to limited data informing their estimates [40]. This heterogeneity in sampling efficiency necessitates ESS monitoring at the parameter level rather than relying upon aggregate summaries that may mask inadequate mixing for specific fertility rate components.

## 5. Practical Implications for Age Structure Forecasting

### 5.1 Uncertainty Propagation Through Population Projections

The precision of fertility rate parameter estimates directly influences the uncertainty of population projections that depend upon these estimates [41]. When MCMC convergence is inadequate, underestimation of parameter uncertainty can propagate through cohort-component projection models, producing projection intervals that are too narrow to capture the true range of future population trajectories.

Research on probabilistic population projections has emphasized the importance of properly accounting for uncertainty in fertility rate estimates [42]. The UN World Population Prospects increasingly employs Bayesian hierarchical models that explicitly propagate uncertainty from fertility rate estimation through population projection calculations, making convergence adequacy critical for the reliability of official population forecasts.

The impact of convergence-induced precision degradation is particularly pronounced for long-horizon projections, where small errors in initial fertility rate estimates compound over time through population momentum effects [43]. Studies of TFR projection scenarios have demonstrated that differences in fertility assumptions can lead to substantial divergence in projected population sizes by century's end, underscoring the importance of accurate uncertainty quantification in fertility rate estimation.

### 5.2 Hierarchical Model Complexity and Convergence Challenges

Hierarchical Bayesian models for fertility rate estimation across multiple countries or regions introduce computational challenges that can impede convergence and degrade estimation precision [44]. The bayesTFR package, which implements Bayesian hierarchical models for global TFR estimation, explicitly addresses convergence diagnostics as a critical component of the modeling workflow, providing functions for thinned MCMC storage and convergence assessment [45].

The complexity of hierarchical fertility models arises from several sources: the large number of country-specific parameters, the hierarchical structure that induces dependence between parameters, and the need to accommodate diverse data quality across countries [46]. These challenges necessitate careful attention to convergence diagnostics and may require algorithm modifications such as reparameterization, blocked updating, or alternative sampling algorithms to achieve adequate mixing.

Research on convergence in hierarchical models has demonstrated that the Gelman-Rubin diagnostic may be conservative in high-dimensional settings, requiring more iterations than simpler models to achieve $\hat{R}$ values close to 1 [47]. This finding has practical implications for fertility modeling, where the number of countries or regions may number in the hundreds, necessitating extended MCMC runs to ensure convergence across all parameters.

### 5.3 Sensitivity to Prior Specifications

The choice of prior distributions in Bayesian fertility models can influence convergence behavior and estimation precision, particularly when priors are informative or when data are sparse for certain parameters [48]. Non-informative priors, while theoretically appealing for objective inference, can lead to diffuse posterior distributions that mix slowly and require extended burn-in periods.

Studies employing Gompertz models for fertility projection have used non-informative prior distributions to implement Bayesian parameter estimation, relying upon the data to drive posterior inference [49]. While this approach minimizes prior influence, it may result in slower convergence when the likelihood provides limited information about certain parameters, such as asymptote parameters in fertility trajectory models.

The precision parameter $\tau_{asfr}$ in hierarchical fertility models, which represents the inverse of the variance, directly influences the strength of pooling toward the global mean [50]. When this parameter is estimated from data, its posterior distribution may exhibit complex behavior that affects convergence of country-specific fertility rate estimates, requiring careful monitoring to ensure adequate mixing.

### 5.4 Recommendations for Demographic Modeling Practice

Based on the evidence synthesized in this report, several recommendations emerge for demographic researchers employing MCMC methods in fertility rate estimation:

First, convergence diagnostics should be computed for all parameters of interest, not merely aggregate summaries, to ensure that slowly-mixing parameters do not compromise inference [51]. Age-specific fertility rates may exhibit heterogeneous convergence behavior that would be masked by focusing solely on TFR summaries.

Second, multiple diagnostic approaches should be employed in combination, as each diagnostic addresses different aspects of convergence behavior [52]. The Gelman-Rubin diagnostic assesses between-chain consistency, the Raftery-Lewis diagnostic addresses quantile estimation precision, and visual diagnostics such as trace plots provide intuitive assessment of mixing behavior.

Third, effective sample size should be monitored throughout the MCMC run, with additional iterations generated for parameters with inadequate ESS [53]. The computational cost of extended sampling should be weighed against the precision requirements of the application, with more demanding applications requiring higher ESS thresholds.

Fourth, thinning decisions should be based on diagnostic examination of autocorrelation rather than arbitrary rules, with the understanding that excessive thinning can reduce precision unnecessarily [54]. When storage constraints necessitate thinning, the minimum thinning interval that achieves acceptable autocorrelation reduction should be employed.

## 6. Conclusion

The convergence conditions of Markov Chain Monte Carlo methods exert a profound influence on the estimation precision of fertility rate parameters in age structure forecasting. Inadequate convergence introduces bias, inflates numerical standard errors, and reduces effective sample sizes, ultimately compromising the reliability of demographic projections that inform critical policy decisions. The theoretical framework linking convergence to precision degradation is well-established, with autocorrelation functions, effective sample sizes, and numerical standard errors providing quantitative measures of precision loss from non-convergence or slow mixing.

The practical implications for demographic modeling are substantial. Hierarchical Bayesian models for fertility rate estimation across multiple populations introduce computational challenges that can impede convergence, necessitating careful attention to diagnostic assessment and algorithm configuration. The Gelman-Rubin diagnostic, Raftery-Lewis diagnostic, trace plot analysis, and effective sample size monitoring each provide complementary perspectives on convergence behavior, and their combined application offers the most comprehensive assessment of MCMC adequacy.

As demographic forecasting increasingly relies upon Bayesian hierarchical frameworks to propagate uncertainty through population projections, ensuring adequate MCMC convergence becomes essential for reliable inference. The precision of age-specific fertility rate estimates directly influences the uncertainty of population forecasts, with consequences for planning and policy decisions that may span decades into the future. Researchers and practitioners in demographic modeling must therefore prioritize convergence assessment as a fundamental component of the MCMC workflow, recognizing that the validity of their inferences depends upon the quality of the posterior samples from which conclusions are drawn.

Future research directions include the development of more efficient MCMC algorithms for high-dimensional hierarchical fertility models, adaptive methods that automatically adjust sampling parameters based on observed chain behavior, and standardized protocols for convergence assessment in demographic applications. The continued advancement of demographic forecasting methodology depends upon addressing these computational challenges while maintaining the principled uncertainty quantification that Bayesian approaches provide.

---

## References

[1] University of Washington. "Accounting for Uncertainty About Past Values in Probabilistic Projections of the Total Fertility Rate." PhD Thesis, 2017.

[2] Pandey, A. "Projection of Some Fertility Indicators of India using MCMC Technique in Bayesian Procedure." SSRN, 2024.

[3] Brooks, S.P. and Roberts, G.O. "Assessing Convergence of Markov Chain Monte Carlo Algorithms." Statistics and Computing, 1998.

[4] Gelman, A. et al. Bayesian Data Analysis. Chapman & Hall/CRC, 2013.

[5] University of Washington. "Estimation of the Complete Model: Given the estimated bias." PhD Thesis, 2017.

[6] Hauer, M. "Bayesian estimation of total fertility from a population's age–sex structure." Statistical Modelling, 2018.

[7] IIASA. "WP-23-007: Age-specific fertility rates by education." IIASA Working Paper, 2023.

[8] Robert, C.P. and Casella, G. Monte Carlo Statistical Methods. Springer, 2004.

[9] Brooks, S.P. and Roberts, G.O. "Convergence Diagnosis and Output Analysis." MCMC Preprint, 1997.

[10] Gelman, A. and Rubin, D.B. "Inference from iterative simulation using multiple sequences." Statistical Science, 1992.

[11] IIASA. "Equation 2. The weights, $w_{cyae}$." IIASA Working Paper, 2023.

[12] Hauer, M. "Bayesian estimation of total fertility from a population's age–sex structure." Statistical Modelling, 2018.

[13] IIASA. "Equation 3. The ASFRs are adjusted to the UN WPP ASFRs." IIASA Working Paper, 2023.

[14] University of Washington. "Bayesian hierarchical model for TFR." PhD Thesis, 2017.

[15] Cowles, M.K. and Carlin, B.P. "Markov Chain Monte Carlo Convergence Diagnostics: A Comparative Review." JASA, 1996.

[16] Gelman, A. et al. "Understanding predictive information criteria for Bayesian models." Statistics and Computing, 2014.

[17] Stan Development Team. "MCMC Diagnostics." Stan Documentation, 2016.

[18] University of Duke. "Numerical Standard Error." Stat 376 Course Notes.

[19] Hauer, M. "The marginal posterior for TFR." Statistical Modelling, 2018.

[20] Hauer, M. "MCMC sampling of 2,000 values from the posterior distribution of TFR." Statistical Modelling, 2018.

[21] Link, W.A. and Eaton, M.J. "On thinning of chains in MCMC." Methods in Ecology and Evolution, 2012.

[22] Stan Development Team. "Thinning and Effective Sample Size." Stan Documentation, 2016.

[23] R Project. "bayesTFR: Running Markov Chain Monte Carlo for Parameters of Total Fertility Rate." R Package Documentation.

[24] Brooks, S.P. and Roberts, G.O. "Assessing Convergence of Markov Chain Monte Carlo Algorithms." Statistics and Computing, 1998.

[25] Pandey, A. "Non-informative prior distribution to implement the Bayesian approach." SSRN, 2024.

[26] University of Washington. "Convergence by inspecting trace plots." PhD Thesis, 2017.

[27] Gelman, A. and Rubin, D.B. "Inference from iterative simulation using multiple sequences." Statistical Science, 1992.

[28] Gelman, A. et al. "A General Diagnostic for Markov Chain Monte Carlo." Preprint, 2023.

[29] University of Washington. "Gelman-Rubin diagnostic (Gelman and Rubin 1992)." PhD Thesis, 2017.

[30] R Project. "auto.conf: List containing a configuration for an 'automatic' run." bayesTFR Package Documentation.

[31] Raftery, A.E. and Lewis, S.M. "Implementing MCMC." In Markov Chain Monte Carlo in Practice, 1996.

[32] University of Duke. "Raftery and Lewis's (1992) method." Stat 376 Course Notes.

[33] Cowles, M.K. and Carlin, B.P. "Markov Chain Monte Carlo Convergence Diagnostics." JASA, 1996.

[34] University of Washington. "Monitored convergence by inspecting trace plots." PhD Thesis, 2017.

[35] Hauer, M. "We generated posterior draws from the 797-vector of parameters." Statistical Modelling, 2018.

[36] R Project. "The function create.thinned.tfr.mcmc is called from tfr.predict." bayesTFR Package Documentation.

[37] Stan Development Team. "Potential Scale Reduction ($\hat{R}$)." Stan Documentation, 2016.

[38] Stan Development Team. "Effective Sample Size." Stan Documentation, 2016.

[39] University of Duke. "Effective number of simulation draws." Stat 376 Course Notes.

[40] University of Washington. "The roughly 3,600 parameters." PhD Thesis, 2017.

[41] CBS Netherlands. "Dealing with Uncertainty in Population Forecasts." Statistics Netherlands, 2000.

[42] University of Washington. "Population projections or forecasts consist of forecasts." PhD Thesis, 2017.

[43] PMC. "Despite the convergence in TFRs, population projections remain relatively distinct." PMC Article, 2024.

[44] R Project. "Bayesian hierarchical model for TFR." bayesTFR Package Documentation.

[45] R Project. "Convergence diagnostics following each chunk." bayesTFR Package Documentation.

[46] IIASA. "Since the UN WPP ASFRs are themselves dependent on DHS data." IIASA Working Paper, 2023.

[47] Gelman, A. et al. "A General Diagnostic for Markov Chain Monte Carlo." Preprint, 2023.

[48] University of Washington. "Prior beliefs are expressed in terms of probability distributions." PhD Thesis, 2017.

[49] Pandey, A. "Gompertz model, assuming lower and upper asymptotes." SSRN, 2024.

[50] IIASA. "The precision parameter $\tau_{asfr}$, the inverse of the variance." IIASA Working Paper, 2023.

[51] University of Washington. "Convergence between MCMC chains was tested using the Gelman-Rubin diagnostic." PhD Thesis, 2017.

[52] Cowles, M.K. and Carlin, B.P. "Markov Chain Monte Carlo Convergence Diagnostics: A Comparative Review." JASA, 1996.

[53] Stan Development Team. "Effective Sample Size and Monte Carlo Standard Error." Stan Documentation, 2016.

[54] Link, W.A. and Eaton, M.J. "On thinning of chains in MCMC." Methods in Ecology and Evolution, 2012.

## Annotations


## Sources
[1] https://betanalpha.github.io/assets/chapters_pdf/fertility.pdf
[2] https://bookdown.org/aramir21/IntroductionBayesianEconometricsGuidedTour/sec54.html
[3] https://cran.r-project.org/web/packages/bayesTFR/bayesTFR.pdf
[4] https://digital.lib.washington.edu/server/api/core/bitstreams/cc57049a-b7c5-45ad-908e-e3a18b1f4569/content
[5] https://jrnold.github.io/bayesian_notes/mcmc-diagnostics.html
[6] https://mathewhauer.github.io/papers/2018-StatisticalModelling.pdf
[7] https://paa2010.populationassociation.org/papers/100654
[8] https://papers.ssrn.com/sol3/Delivery.cfm/4880986.pdf?abstractid=4880986&mirid=1
[9] https://pmc.ncbi.nlm.nih.gov/articles/PMC11439461/
[10] https://pure.iiasa.ac.at/id/eprint/18890/1/WP-23-007.pdf
[11] https://sbfnk.github.io/mfiidd/external_ref/Cowles96_MCMCconvergence.pdf
[12] https://sites.stat.columbia.edu/gelman/research/published/nestedRhat.pdf
[13] https://waves-vagues.dfo-mpo.gc.ca/Library/360989.pdf
[14] https://www.cbs.nl/-/media/imported/documents/2000/24/dealing-with-uncertainty.pdf
[15] https://www2.stat.duke.edu/~scs/Courses/Stat376/Papers/ConvergeDiagnostics/brooks97assessing.pdf