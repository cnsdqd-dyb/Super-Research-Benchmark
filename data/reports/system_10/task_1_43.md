# Deep Research Report: perplexity/sonar-deep-research
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 99009a83 | **Time:** 124.60s | **Cost:** $1.17885
--------------------------------------------------------------------------------

# The Impact of Markov Chain Monte Carlo Convergence Conditions on Fertility Rate Parameter Estimation Precision in Age Structure Forecasting

## Executive Summary

Markov Chain Monte Carlo (MCMC) methods have become foundational to Bayesian approaches for estimating fertility rates and projecting age-structured populations, yet the quality of these estimates is fundamentally dependent on the convergence properties of the underlying chains. This report examines how convergence conditions—including reversibility, ergodicity, and mixing properties—directly influence the precision of fertility rate parameter estimates used in demographic forecasting. The convergence assessment process, which relies on diagnostics such as the Gelman-Rubin potential scale reduction factor and effective sample size calculations, determines whether collected samples adequately represent the posterior distribution. Poor convergence leads to biased estimates and artificially narrow credible intervals, while adequate convergence ensures that parameter uncertainty is properly characterized. Through the integration of theoretical frameworks with practical demographic applications, this analysis demonstrates that MCMC convergence conditions are not merely technical concerns but critical determinants of forecast reliability for population projections. The relationship between convergence quality and estimation precision becomes particularly important when projecting fertility rates across multiple age groups simultaneously, where high-dimensional parameter spaces can create mixing challenges that substantially affect the validity of demographic predictions.

## Understanding Markov Chain Monte Carlo Convergence Conditions

### Fundamental Theoretical Foundations

The convergence of a Markov chain to its stationary distribution represents one of the most critical aspects of MCMC methodology in demographic applications. At its theoretical core, convergence requires that a Markov chain with transition kernel \(K\) satisfies specific mathematical conditions that guarantee it will eventually sample from the target posterior distribution.[1] The most commonly invoked condition for establishing Central Limit Theorem convergence in MCMC methods is **reversibility**, which is equivalent to the detailed balance condition.[1] The detailed balance condition states that a Markov chain satisfies reversibility if there exists a function \(f\) such that \(K(y, x)f(y) = K(x, y)f(x)\), meaning the probability flow from state \(x\) to state \(y\) equals the flow in the reverse direction when weighted by the stationary distribution.[1]

Beyond reversibility, establishing convergence requires several additional mathematical properties that work in concert. **Irreducibility** ensures that the chain can potentially reach any state from any other state, preventing the chain from becoming trapped in isolated regions of parameter space.[1] **Aperiodicity** guarantees that the chain does not get locked into cyclical patterns of state transitions that would prevent convergence to a unique stationary distribution.[1] These conditions, though sometimes restrictive in theory, are often easily satisfied in practical MCMC algorithms by introducing auxiliary variables or using symmetric proposal mechanisms.[1] The theoretical framework extends further to include the concept of **Harris recurrence**, which is necessary for establishing the Law of Large Numbers for MCMC estimates, and additional conditions such as geometric ergodicity may be required to ensure the Central Limit Theorem holds precisely.[1]

### Reversibility and Detailed Balance in Demographic Applications

The practical significance of reversibility becomes evident when considering how demographic parameters like fertility rates are estimated. In fertility projection models implemented through MCMC, such as those used by the United Nations World Population Prospects, the transition kernels governing how parameters are updated must satisfy detailed balance to ensure proper sampling from the posterior distribution of fertility parameters.[17] The double logistic function used to model fertility transitions during the demographic transition phase (Phase II) has multiple parameters—including the pace of decline and level parameters—that must be jointly estimated.[15][17] When these parameters are updated through MCMC, the reversibility condition ensures that the joint posterior distribution of all country-specific and global parameters is properly approximated.

In practice, reversibility is often implemented through symmetric proposal distributions. For instance, when updating fertility rate parameters in age-structured models, random walk proposals with symmetric innovations naturally satisfy the detailed balance condition.[17] However, the effectiveness of this approach depends on the scale of the proposal distribution; proposals that are too small lead to high autocorrelation and slow mixing, while proposals that are too large result in frequent rejection and wasted computational resources.[1] The interplay between reversibility requirements and practical proposal design directly impacts how efficiently the MCMC sampler explores the posterior distribution of fertility parameters, which in turn affects the precision of estimates for age-specific fertility rates across different demographic subpopulations.

### The Role of Irreducibility and Aperiodicity in High-Dimensional Fertility Models

Irreducibility becomes particularly important in high-dimensional fertility estimation problems where multiple age groups and countries must be estimated simultaneously. The Bayesian hierarchical models used for global fertility projection contain hundreds or thousands of parameters—including age-specific fertility parameters for each country across multiple time periods.[14][15][17] For the MCMC chain to properly explore this high-dimensional posterior space, it must be able to reach all regions of meaningful posterior probability. Irreducibility ensures that the chain is not confined to a subset of parameter space due to structural barriers in the model specification.[1]

Aperiodicity, while mathematically distinct from irreducibility, becomes critical when considering the update order of interdependent parameters in demographic models. In fertility estimation, parameters controlling the level of fertility are strongly correlated with those controlling the pace of fertility decline.[15][17] If the MCMC algorithm processes parameter updates in a strictly cyclical manner without variation, the chain could theoretically exhibit periodic behavior even if it visits all states. In practice, modern MCMC implementations in demographic applications—such as those used in the bayesTFR and bayesLife R packages—incorporate adaptive tuning and randomized update orderings that ensure aperiodicity is satisfied.[17][48][49]

## Convergence Diagnostics and Assessment Methods

### The Gelman-Rubin Potential Scale Reduction Factor

Among convergence diagnostics, the **Gelman-Rubin potential scale reduction factor**, denoted as \(\hat{R}\), has emerged as the most widely adopted metric in demographic applications.[1][21][26] This diagnostic evaluates MCMC convergence by comparing the variance of samples within individual chains to the variance across all chains pooled together.[21] The mathematical formulation expresses \(\hat{R}\) as the ratio of an estimated variance to the within-chain variance: \(\hat{R} = \sqrt{\frac{\widehat{\text{var}}^{+}(\theta|y)}{W}}\), where the numerator combines within-chain variance weighted by a factor of \((N-1)/N\) and between-chain variance weighted by \(1/N\).[21]

If all chains have converged to the same stationary distribution, the between-chain and within-chain variances should be approximately equal, and thus \(\hat{R}\) should approach unity.[1][21] In practice, a value of \(\hat{R} < 1.1\) is conventionally taken as evidence of adequate convergence.[1][21] Higher values indicate that the chains are still exploring different regions of the parameter space and have not yet reached convergence.[1] For fertility rate estimation, this means that if the Gelman-Rubin diagnostic for age-specific fertility rate parameters exceeds 1.1, the collected samples do not yet adequately represent the posterior distribution and additional MCMC iterations are required.

The advantage of the Gelman-Rubin diagnostic lies in its ability to detect non-stationarity by comparing multiple chains initialized from overdispersed starting values.[1][21] This design feature proves particularly valuable in detecting chains that become "stuck" in narrow regions of parameter space—a problem that can occur when estimating fertility parameters in countries with unusual demographic histories or sparse data.[15] However, the statistic has known limitations. Recent developments have introduced modifications to address concerns about its behavior with multimodal posteriors and its sensitivity to chain initialization.[4][7][26] The **split-\(\hat{R}\)** variant addresses non-stationarity by splitting each chain into two halves before computing the diagnostic, providing additional sensitivity to slow convergence.[21]

### Alternative Convergence Diagnostics

Beyond the Gelman-Rubin statistic, several other convergence diagnostics provide complementary information about MCMC performance in demographic applications.[1][7][20] **Visual trace plots** of parameters over iterations reveal whether chains are mixing well by displaying how parameter values change across iterations.[20][22] For fertility rate parameters, trace plots should show relatively stable oscillation around a central value without trends, drifts, or sudden jumps that would indicate inadequate mixing or convergence failure.[20] The autocorrelation structure visible in trace plots provides intuitive evidence of mixing quality—chains with high autocorrelation at many lags indicate that consecutive samples are highly dependent, reducing the effective information content of the chain.[1][9]

**Raftery-Lewis diagnostics** provide quantitative estimates of the number of iterations required to estimate specific quantiles (such as the 2.5th and 97.5th percentiles needed for credible intervals) to a specified level of accuracy.[20] This diagnostic is particularly relevant for fertility projection applications where credible intervals around projected fertility rates directly inform policy decisions.[1] The diagnostic works by analyzing autocorrelation in the chain and estimating the "thinning factor" needed to achieve approximately independent samples—information directly applicable to deciding how many iterations must be collected after convergence.[20]

The emergence of machine learning-based convergence diagnostics represents a recent methodological advance.[7] These approaches use classification algorithms to distinguish between samples that adequately represent the posterior and those from the warmup phase, potentially providing more nuanced convergence assessment than traditional statistics.[7] Such methods can incorporate information from the joint sampling distribution of multiple parameters simultaneously, which may be particularly valuable for age-structured fertility models where parameters are correlated across ages.[7]

### Assessing Convergence in the Many-Short-Chains Regime

Recent computational advances have enabled a paradigm shift in MCMC practice, where researchers run hundreds or thousands of short chains in parallel rather than a few long chains.[4][26] This "many-short-chains regime" becomes feasible through GPU acceleration and parallel computing infrastructure.[4][26] For large-scale demographic applications like the UN's World Population Prospects, which requires fertility projection for all countries simultaneously, this approach offers significant computational advantages.[26]

However, the many-short-chains regime presents unique convergence assessment challenges. The standard Gelman-Rubin diagnostic must be recalibrated when individual chains are very short.[4][26] A chain of length one sampling iteration after convergence represents an extreme case where almost all information comes from the number of chains rather than chain length.[26] In this setting, detecting bias from incomplete warmup becomes critical, and modified versions of the Gelman-Rubin diagnostic that account for "persistent variance" from initialization effects have been proposed.[4][26] This development proves particularly important for fertility estimation where the dimension of parameter space is high and chains initialized in poor regions could introduce systematic bias even if the final sample appears well-mixed.[26]

## Effective Sample Size and Parameter Estimation Precision

### Autocorrelation and Effective Sample Size Calculations

The precision of MCMC-based fertility rate estimates is not simply determined by the number of samples collected; rather, it depends critically on the **effective sample size (ESS)**, which accounts for autocorrelation within chains.[9][12] MCMC methods produce autocorrelated samples as successive draws from the Markov chain are statistically dependent, meaning each new sample adds less fresh information than an independent draw would contribute.[1][9] The effective sample size is defined through the autocorrelation structure: \(N_{\text{eff}} = \frac{N}{1 + 2\sum_{t=1}^{\infty} \rho_t}\), where \(N\) is the total number of samples and \(\rho_t\) is the autocorrelation at lag \(t\).[9]

In an ideal scenario with no autocorrelation, \(\rho_k = 0\) and thus \(N_{\text{eff}} \approx N\), meaning all collected samples contain independent information.[1][9] Conversely, in a poorly mixing chain with strong autocorrelation, \(N_{\text{eff}}\) can be substantially smaller than \(N\).[1][9] Monitoring the ESS for each parameter represents a practical method to gauge how much autocorrelation is present; a low ESS indicates that many more iterations may be needed to achieve a desired effective sample of independent draws for reliably estimating fertility parameters.[1][9]

For demographic applications estimating fertility rates by age group, the ESS typically differs across parameters.[9][12] Age-specific fertility parameters for young reproductive ages may have different autocorrelation properties than parameters for older ages due to differences in data availability and prior information.[2][8][14] Some parameters may achieve reasonable ESS values relatively quickly, while others require substantially longer chains. This heterogeneity necessitates monitoring ESS separately for each fertility parameter rather than relying on a single summary statistic.[9]

### Relationship Between Convergence Quality and Parameter Precision

The connection between convergence conditions and parameter precision operates through multiple mechanisms. First, convergence affects the bias of estimates. If an MCMC chain has not adequately converged before samples are collected, the early samples will reflect the influence of initial parameter values rather than the true posterior distribution.[4][22][26] This initialization bias directly translates into biased fertility rate estimates, potentially leading to systematically wrong population projections.[4] The warm-up or burn-in phase exists precisely to allow chains to forget their initialization and approach the stationary distribution, but determining the appropriate length requires convergence assessment.[19][22]

Second, convergence quality impacts the accuracy of credible intervals—the primary measure of uncertainty in Bayesian demographic inference. Poor convergence leads to artificially narrow credible intervals because the sampler explores insufficient portions of the posterior distribution, underestimating true parameter uncertainty.[1][7] This underestimation of uncertainty proves particularly problematic for fertility rate projections where decision-makers rely on credible intervals to characterize uncertainty in future population structures.[15][51] A fertility projection with credible intervals that are too narrow provides false confidence that future fertility is more predictable than it actually is.

Third, convergence affects the effective sample size and therefore the Monte Carlo error of estimates. For a given total number of iterations, poor convergence (high autocorrelation) reduces the effective sample size, which directly increases the standard error of all posterior estimates, including fertility rate parameters.[9] This larger Monte Carlo error translates into wider confidence intervals around estimates and reduced precision in characterizing the posterior distribution of fertility parameters.[9][12]

### Thinning and Sample Efficiency

The practice of collecting every \(k\)-th iteration from an MCMC chain (thinning) demonstrates the practical importance of autocorrelation and effective sample size. Stan Reference Manual documentation notes that generating 10,000 draws after convergence by saving all of them produces the same sample consisting of one thousand draws as generating 1,000 draws after convergence and saving every tenth draw, yet the second approach can produce a higher effective sample size.[9] This counterintuitive result occurs because thinning reduces autocorrelation in the retained samples.[9] When autocorrelation is substantial, the effective autocorrelation \(\rho_t\) in a thinned sequence becomes \(\rho_{10t}\) from the unthinned sequence, reducing the sum of autocorrelations and thus increasing effective sample size.[9]

For fertility rate estimation using MCMC, this principle has practical implications. Rather than running longer chains and saving every sample, researchers might achieve better precision by running longer chains and applying selective thinning to reduce autocorrelation.[9] The optimal thinning strategy depends on the specific autocorrelation properties of fertility parameters being estimated, which vary across age groups and countries.[17][49]

## Fertility Rate Estimation within Bayesian MCMC Frameworks

### Bayesian Hierarchical Models for Total and Age-Specific Fertility Rates

The estimation of fertility rates using Bayesian MCMC methods relies fundamentally on hierarchical model structures that share information across countries, time periods, and age groups while allowing for country-specific variations.[8][14][15][17] The World Population Prospects employs a Bayesian hierarchical model (BHM) to estimate annual age-specific fertility rates (ASFR) by five-year age groups from age 10 to 54 for all countries since 1950.[14][35] This model has three fundamental phases: pre-transition (Phase I, high stable fertility), transition (Phase II, declining fertility), and post-transition (Phase III, low fluctuating fertility).[15][17][49]

During Phase II, fertility decline is modeled as a random walk with drift, where the drift term follows a double logistic function of fertility level.[15][17][49] The model can be written as:

\[d_{c,t} = d(\theta_c, \lambda_c, \tau_c, f_{c,t}) = \begin{cases} g(\theta_c, f_{c,t}) & \text{if } f_{c,t} > 1 \\ 0 & \text{otherwise} \end{cases}\][17]

where \(d_c\) is the maximum possible pace of decline and other parameters describe the country-specific fertility transition characteristics.[17] The parameters of this decline function must be estimated jointly for all countries using MCMC, creating a high-dimensional estimation problem where convergence becomes technically challenging.

A crucial aspect of these hierarchical models is the "borrowing of strength" across countries—information from countries with abundant fertility data helps constrain estimates in countries with sparse or unreliable data.[8][14][15][35] This pooling of information through hierarchical priors is implemented through a "world distribution" of fertility parameters.[15][49] The concentration of the hierarchical prior (how much information is borrowed) is itself estimated from data, adding another parameter that must converge.[15][49]

### Convergence Challenges in Fertility Estimation

The MCMC estimation of fertility parameters presents specific convergence challenges beyond those encountered in simpler statistical models. First, the high dimensionality of the problem—with country-specific parameters, global hyperparameters, and age-specific fertility patterns all requiring simultaneous estimation—creates a complex posterior landscape with many local modes and ridges.[14][15][49] When fertility data for a specific country and age group are sparse, the posterior becomes dominated by the hierarchical prior, which can lead to weak identifiability of country-specific parameters.[2][8][14]

Second, fertility parameters exhibit strong correlations that complicate mixing. The level of fertility (measured by the total fertility rate) is negatively correlated with the pace of fertility decline in the double logistic model—countries with higher fertility tend to have higher decline rates, and this correlation must be properly captured by the MCMC sampler.[15][17] Such correlations increase autocorrelation in chains and reduce effective sample size, requiring longer chains or algorithmic improvements to achieve convergence.[1][17]

Third, missing or imputed data is common in fertility estimation, particularly for historical periods and countries with incomplete vital registration systems.[14][35] The need to estimate both the parameters of the fertility model and values of missing data points further expands the dimensionality of the MCMC sampling problem. Modern implementations address this through hierarchical models that explicitly model data quality and measurement error, but this adds additional parameters requiring convergence assessment.[14][35]

### Impact of Convergence on Fertility Projection Uncertainty

The quality of MCMC convergence directly affects the probabilistic projections of future fertility rates that form the basis for population projections. The UN's World Population Prospects produces projections with 80-percent and 95-percent prediction intervals derived from the posterior predictive distribution of fertility rates.[15][51] These intervals are obtained by simulating trajectories from the posterior distribution of the fertility transition parameters and propagating uncertainty through projection equations.[15][49][51]

If MCMC chains have not adequately converged before drawing samples for prediction, the resulting prediction intervals underestimate true uncertainty because the posterior distribution has not been fully characterized.[4][7][58][59] Conversely, if chains exhibit high autocorrelation and the effective sample size remains small, prediction intervals may be artificially wide because the effective posterior sample is insufficient to estimate probability distributions accurately.[9] Neither extreme—underestimated or overestimated uncertainty—is acceptable for informing demographic policy decisions that affect billions of people.[15][51]

## Age-Structured Population Models and Demographic Forecasting

### Integration of Fertility Parameters into Cohort Component Models

Fertility rate parameters estimated through MCMC form essential inputs to age-structured population projection models, particularly the cohort component method (CCM), also known as the Leslie matrix approach.[6][15][25][51] The cohort component method projects populations forward by age group using the fundamental demographic balancing equation:

\[\text{Population}_{a,t+n} = \text{Population}_{a,t} \times \text{Survival}_{a,t} + \text{Births}_{t} \times \text{Survival}_{0,t} + \text{Migration}_{a,t}\][6][25][51]

Births in the population are directly proportional to the number of women of reproductive age multiplied by age-specific fertility rates. Therefore, uncertainty in estimated fertility rate parameters translates directly into uncertainty in projected births and, cascading through the demographic balancing equation, into uncertainty about the entire future age structure of the population.[6][25][51]

The precision of age-specific fertility rate parameters becomes particularly critical when disaggregating projections by age groups. A five-year age group structure (ages 0-4, 5-9, ..., 75+) or single-year age groups requires that fertility parameters be estimated separately for each age interval.[6][14][35] If an MCMC chain has inadequately converged for age-specific parameters, the age pattern of fertility may be distorted, leading to projections that incorrectly estimate births to women at specific ages and thus misallocate births across the age structure.[14][35]

### Small Area Population Forecasting and Hierarchical Structure

When extending fertility-based population projections to small areas (counties, districts, municipalities), the convergence requirements become even more stringent.[3][32][34] Small area population forecasting faces the challenge of sparse data—many administrative areas have relatively few births recorded in available data sources, particularly when disaggregating by age and sex.[3][32][34] The hierarchical Bayesian approach addresses this by borrowing strength from larger areas, but the estimation of area-specific deviations from national patterns requires MCMC sampling in increasingly high-dimensional spaces.[3][32][34]

For instance, estimating fertility rates for 155 countries disaggregated by sex and age group simultaneously requires MCMC sampling in a parameter space with thousands of dimensions.[34] Convergence assessment becomes computationally intensive and technically challenging at this scale.[34] The Gelman-Rubin diagnostic must be computed for each parameter, and researchers must ensure that convergence is achieved not just for marginal parameters but for functions of parameters (such as the total fertility rate summed across ages).[21]

### Validation of Age-Structured Projections

Assessing whether MCMC convergence has been adequate requires comparing projected outcomes against observed data in validation exercises.[3][15][38][50][51][57] These validation studies fit models to historical data truncated at some point in time and assess predictive accuracy for the held-out future period.[38][50][51][57] Studies evaluating Bayesian fertility projection models have found that when MCMC chains have adequately converged, prediction intervals achieve close to nominal coverage—meaning that 95-percent prediction intervals contain true future values approximately 95 percent of the time.[15][51][57][58][59]

Conversely, when convergence is inadequate, prediction interval coverage deteriorates substantially.[58][59] A study accounting for uncertainty about past fertility values found that previous methods, which did not account for past estimation uncertainty, achieved prediction interval coverage considerably below nominal levels; implementing improved convergence assessment and hierarchical modeling to account for data uncertainty substantially improved coverage to near-nominal levels.[58][59] This demonstrates that convergence quality has measurable, quantifiable impacts on forecast reliability.

## Practical Implementation: Achieving Adequate Convergence in Demographic MCMC

### Warm-Up Versus Burn-In Conceptualization

Modern MCMC implementations, particularly in Hamiltonian Monte Carlo algorithms like those in Stan, distinguish between "warm-up" and "burn-in" phases, a distinction with important implications for convergence assessment.[19][22][26] In older terminology, "burn-in" referred to iterations discarded before sampling, motivated by an analogy to industrial stress-testing.[19] However, in contemporary MCMC software like Stan, the warm-up phase serves multiple purposes beyond simple convergence to stationarity.[19][22]

During warm-up, the MCMC algorithm tunes parameters that control its behavior—such as the mass matrix (metric) and step size (integration discretization interval) in Hamiltonian methods.[19] This adaptation improves the sampler's efficiency but means that warm-up samples are not drawn from the target posterior distribution and should not be included in inference.[19][22] After warm-up concludes and adaptation ceases, additional iterations (sometimes called the "post-adaptation warm-up") are recommended before collecting inference samples to ensure the chain has settled into typical set (the high probability mass region) after adaptation.[19][22]

This distinction becomes important for understanding convergence requirements in fertility estimation. The burn-in period needed depends not just on convergence to the invariant distribution but on convergence to the region where adaptation will occur effectively.[19][22] In Bayesian fertility models with complex hierarchical structures, this may require more iterations than convergence diagnostics alone would suggest.[17][49]

### Automatic Tuning and Convergence Assessment

The bayesTFR R package, widely used for fertility projections including by the United Nations, implements automatic convergence assessment through periodic diagnostics during the MCMC run.[17][48][49] Rather than specifying a fixed number of iterations in advance, researchers can set the algorithm to automatically determine when convergence criteria are satisfied and terminate the chain.[17][48][49] This approach addresses the challenge of determining appropriate run length, which varies depending on model complexity, data characteristics, and prior specification.[17][48][49]

The automatic convergence assessment in bayesTFR computes the Gelman-Rubin diagnostic periodically during MCMC sampling for all parameters simultaneously.[17][48][49] When all parameters achieve \(\hat{R} < 1.1\), the algorithm transitions from burn-in to production sampling.[17][48][49] The number of production iterations is specified in advance and represents the samples retained for posterior inference and prediction.[17][48][49] This semi-automatic approach balances computational efficiency with convergence assurance—practitioners are protected from the worst case of insufficient convergence while avoiding unnecessary additional iterations once convergence is achieved.[17][48][49]

### Computational Advances: GPU Acceleration and Parallel Chains

Recent computational developments have transformed practical convergence assessment approaches through GPU acceleration enabling the many-short-chains regime.[4][26][45] Rather than running a few long MCMC chains sequentially, practitioners can now run hundreds or thousands of short chains in parallel.[4][26] While each individual chain must still complete a warmup phase, the ability to run chains simultaneously means the total wall-clock time for obtaining a large posterior sample can be substantially reduced.[4][26]

This paradigm shift affects convergence assessment in important ways. With many parallel chains, the Gelman-Rubin diagnostic becomes more powerful for detecting divergent chains, as differences between chains become apparent even with short individual chain lengths.[4][26][45] Conversely, the challenge of detecting initialization bias within individual chains increases when chains are very short, necessitating careful attention to post-warmup convergence and the presence of persistent variance from initialization effects.[4][26]

For large-scale fertility estimation projects, this computational advance enables practical implementation of larger hierarchical models with finer geographic resolution. Studies of genomic prediction models implementing this approach found that automatically tunable burn-in with multiple parallel chains provided accurate and cost-effective computation for complex Bayesian models, suggesting the approach would generalize to demographic applications.[45]

### Model Reparameterization and Algorithmic Improvements

When standard MCMC implementations achieve poor convergence for fertility parameters, reparameterization and algorithmic improvements can dramatically improve performance.[29][31][37] Reparameterizing the fertility decline function to use transformed parameters rather than raw parameters often dramatically improves convergence.[17][49] For example, using log-transformed versions of fertility pace parameters that are naturally positive can reduce correlation structures in the posterior and improve mixing.[17][49]

Another algorithmic improvement involves the order of parameter updates within the Gibbs sampler.[31][37] Some updating schemes naturally lead to better mixing than others; updating highly correlated parameters jointly rather than separately often substantially reduces autocorrelation.[31] The bayesTFR package uses carefully designed update orderings and adaptive covariance matrices for Metropolis-Hastings steps to improve convergence in the complex fertility transition model.[17][48][49]

Slice sampling, implemented in the bayesTFR package for updating the total fertility rate in post-transition Phase III, represents another algorithmic choice designed to improve convergence.[49] Slice sampling can handle complex posterior shapes better than standard Metropolis-Hastings, leading to better mixing and higher acceptance rates without requiring manual tuning of proposal variances.[49]

## Synthesis: Linking Convergence to Forecast Accuracy

### Empirical Evidence from Demographic Validation Studies

Multiple validation studies comparing Bayesian demographic projections to subsequent actual outcomes provide empirical evidence connecting MCMC convergence quality to forecast accuracy.[15][51][56][57][58][59] A foundational study evaluating the Bayesian probabilistic population projection method fit models to data from 1950-1990 and projected to 2010, comparing predictions against actual observed values.[51] The results demonstrated that when MCMC convergence was properly assessed using multiple chains with careful monitoring of the Gelman-Rubin diagnostic, prediction intervals were reasonably well calibrated—the 80-percent prediction intervals contained true values approximately 80 percent of the time.[51]

Studies that extended this work by accounting for uncertainty about past fertility values found that improving MCMC implementation through better convergence assessment significantly improved prediction interval coverage.[58][59] The extension from the standard bayesTFR model to one accounting for past estimation uncertainty required longer MCMC chains and more careful convergence assessment, but the result was improved probabilistic calibration of predictions.[58][59] This demonstrates that investing additional computational resources in more rigorous convergence assessment yields tangible improvements in forecast reliability.

For age-structured population forecasts, a study comparing different small area population forecasting methods found that approaches explicitly accounting for demographic uncertainty through MCMC sampling produced more accurate predictions than deterministic methods.[3][57] The accuracy advantage depended critically on adequate MCMC convergence, as chains that had not adequately converged produced biased forecasts.[3][57] This finding generalizes across multiple demographic contexts: small area population forecasting, species population dynamics modeling, and international migration projections all benefit from rigorous convergence assessment when MCMC methods are employed.[3][28][41][57]

### Policy Implications and Decision-Making Under Demographic Uncertainty

The implications of MCMC convergence quality extend beyond technical statistical concerns to directly affect policy decisions based on demographic forecasts. Population projections inform decisions about infrastructure investment, education system planning, healthcare capacity, and pension system design.[15][51] When fertility rate projections include credible intervals that underestimate true uncertainty due to inadequate MCMC convergence, policymakers may make decisions based on a false sense of confidence in future demographic trends.[15][51]

Conversely, prediction intervals that are artificially wide due to inefficient MCMC sampling (high autocorrelation, low effective sample size) can lead policymakers to over-prepare for demographic variability.[9][12] The goal of rigorous convergence assessment is neither to overstate nor understate uncertainty, but to characterize it accurately.[1][15][51]

The relationship between convergence quality and policy relevance becomes particularly salient for fertility projections in high-fertility countries undergoing rapid demographic change. Countries in Sub-Saharan Africa have experienced fertility declines that vary substantially across regions and population subgroups, requiring finely-tuned MCMC algorithms that properly capture heterogeneity in fertility transition parameters.[8][15][51][58] Fertility projections that fail to adequately estimate the uncertainty in these transitions due to convergence problems could lead to substantial forecast errors with major policy consequences.[15][51]

### Benchmarking and Best Practices

Evidence-based benchmarks for adequate MCMC performance in demographic applications have emerged from extensive validation research and methodological development. The widely adopted standard that \(\hat{R} < 1.1\) for all parameters represents a practical threshold that balances the need for convergence assurance with computational efficiency.[1][15][21] However, this threshold should be understood as a guideline rather than an absolute requirement—some applications may require more stringent convergence criteria, while others with less stringent requirements might use slightly higher thresholds.[21]

For effective sample size, practical guidance suggests that the ESS divided by total iterations (the thinning factor) should exceed 0.1, meaning effective sample size should be at least 10 percent of the total number of iterations collected after convergence.[9] Many applications in demographic forecasting find that achieving ESS equivalent to 1000-5000 independent samples is sufficient for accurate estimation of fertility parameters and their uncertainty.[15][17][49]

When running multiple MCMC chains, best practices recommend initializing chains from overdispersed starting values that are more variable than the target posterior distribution.[22][26] This initialization strategy ensures that divergent chains will be detected by convergence diagnostics; if all chains happen to converge to the same region despite starting from dispersed initial values, this provides strong evidence of genuine convergence rather than chains being trapped in local modes.[22][26]

Post-convergence diagnostics should include both visual inspection of trace plots and quantitative diagnostics, with attention to whether all estimated parameters achieve satisfactory convergence values.[20][21] Parameters controlling the age pattern of fertility may converge at different rates than those controlling the overall level of fertility, requiring that convergence assessment not focus exclusively on summary statistics like total fertility rates.[14][21][35]

## Conclusion

The convergence conditions of Markov Chain Monte Carlo methods represent far more than a technical consideration in demographic inference; they fundamentally determine the reliability and usefulness of fertility rate parameter estimates for age-structured population forecasting. The theoretical requirements for convergence—including reversibility, ergodicity, irreducibility, and aperiodicity—create a mathematical foundation ensuring that MCMC samples eventually represent the target posterior distribution.[1] However, achieving these conditions in practice for complex hierarchical models of fertility requires careful attention to algorithm design, initialization strategies, and continuous convergence assessment.

The precision of fertility rate parameter estimates depends critically on both the convergence of MCMC chains to their stationary distributions and the efficiency with which those chains explore the posterior space, as reflected in effective sample size calculations.[9] Poor convergence introduces bias into estimates, artificially narrows credible intervals, and produces prediction intervals that fail to achieve nominal coverage when compared to subsequent observed demographic outcomes.[4][7][58][59] Empirical validation studies demonstrate that rigorously assessed convergence leads to demographic forecasts that accurately characterize uncertainty, while inadequate convergence produces systematically miscalibrated predictions.[15][51][58][59]

For age-structured population forecasting, the challenge becomes more acute because fertility parameters must be estimated by age group (and often by country, region, and other demographic subgroups) simultaneously, creating high-dimensional MCMC sampling problems.[14][15][35] The correlation structure of fertility parameters—where level and pace of fertility decline are correlated across countries, and age-specific patterns show strong dependencies—naturally leads to high autocorrelation in MCMC chains.[1][15][17] Achieving adequate convergence in these settings requires careful consideration of proposal distributions, parameter transformations, update orderings, and the total number of iterations needed to characterize the posterior distribution accurately.

Recent computational advances, including GPU acceleration enabling the many-short-chains regime, have transformed practical approaches to convergence assessment while introducing new challenges for detecting initialization bias with short individual chains.[4][26] Modern demographic forecasting tools like the bayesTFR R package implement semi-automatic convergence assessment that provides practitioners with protection against insufficient convergence while maintaining computational efficiency.[17][48][49]

The impact of MCMC convergence quality on fertility parameter precision ultimately propagates through to the reliability of population forecasts that inform major policy decisions affecting billions of people.[15][51] Populations from policy makers' perspective rely on accurate characterization of demographic uncertainty, particularly for long-term forecasts where small differences in fertility assumptions create dramatic divergence in projected populations.[15][51] Investment in rigorous convergence assessment, careful algorithm design, and validation against subsequent observed outcomes yields improvements in forecast reliability that justify the additional computational and analytical effort required. Future developments in MCMC methodology—including advances in scaling to even higher dimensional problems, improvements to convergence diagnostics, and refinements to hierarchical model structures—will continue to enhance the precision and reliability of demographic forecasts based on fertility parameter estimation.

## Annotations
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Markov chain Monte Carlo - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Markov_chain_Monte_Carlo'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A novel approach for estimating fertility rates in finite populations ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10810359/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Methods for Small Area Population Forecasts: State-of-the-Art ... - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC8365292/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Assessing the convergence of Markov chain Monte Carlo when ...', 'url': 'https://sites.stat.columbia.edu/gelman/research/published/nestedRhat.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Forecasting Births Using a Three- Parameter Model', 'url': 'https://www.humanfertility.org/File/GetDocument/Docs/Symposium/McDonald_Kippen.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Chapter 14: Forecasting Population Size and Age Structure', 'url': 'https://ecampusontario.pressbooks.pub/demographyandeconomics/chapter/chapter-14-forecasting-population-size-and-age-structure/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A Robust MCMC Convergence Diagnostic with Uncertainty Using ...', 'url': 'https://projecteuclid.org/journals/bayesian-analysis/advance-publication/R--A-Robust-MCMC-Convergence-Diagnostic-with-Uncertainty-Using/10.1214/20-BA1252.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'BAYESIAN PROJECTIONS OF TOTAL FERTILITY RATE ... - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11439461/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '16.4 Effective Sample Size | Stan Reference Manual', 'url': 'https://mc-stan.org/docs/2_21/reference-manual/effective-sample-size-section.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Quantifying uncertainty in transdimensional Markov chain Monte ...', 'url': 'https://cran.r-project.org/web/packages/MCMCprecision/vignettes/Heck_2018_Statistics_and_Computing.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Bayesian Forecasting of Cohort Fertility', 'url': 'https://www.humanfertility.org/File/GetDocument/Docs/Symposium/Schmertmann%20et%20al.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'What is Effective Sample Size? - Displayr', 'url': 'https://www.displayr.com/what-is-effective-sample-size/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Forecasting Fertility using Parametric Mixture Models - arXiv', 'url': 'https://arxiv.org/pdf/1909.09545.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Estimating age-specific fertility rate in the World Population Prospects', 'url': 'https://www.un.org/development/desa/pd/sites/www.un.org.development.desa.pd/files/undesa_pd_2023_technical-paper_asfr.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Bayesian Population Projections for the United Nations - PMC - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC4196216/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A novel approach for estimating fertility rates in finite populations ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10810359/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'bayesTFR: An R Package for Probabilistic Projections of the Total ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5096741/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Bayesian probabilistic population projections for all countries - PNAS', 'url': 'https://www.pnas.org/doi/10.1073/pnas.1211452109'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Burn-in for MCMC, why we prefer the term warm-up', 'url': 'https://statmodeling.stat.columbia.edu/2017/12/15/burn-vs-warm-iterative-simulation-algorithms/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] MCMC Diagnostics - MyWeb', 'url': 'https://myweb.uiowa.edu/pbreheny/uk/teaching/701/notes/3-5.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '15.3 Notation for samples, chains, and draws - Stan Reference Manual', 'url': 'https://mc-stan.org/docs/2_18/reference-manual/notation-for-samples-chains-and-draws.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A Brief Explanation of MCMC Sampling', 'url': 'https://hschuett.github.io/BayesForAccountingResearch/mcmc.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Statistical evaluation of parameters estimating autocorrelation and ...', 'url': 'https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/j.2041-210x.2012.00195.x'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] General Methods for Monitoring Convergence of Iterative Simulations', 'url': 'https://sites.stat.columbia.edu/gelman/research/published/brooksgelman2.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Bayesian reconstruction of two‐sex populations by age: estimating ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC4657758/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Assessing the convergence of Markov chain Monte Carlo ... - arXiv', 'url': 'https://arxiv.org/html/2110.13017v5'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Hierarchical Bayesian Integrated Modeling of Age- and Sex ... - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC12559060/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] using bayesian models to forecast international arrivals and ...', 'url': 'https://ojs.victoria.ac.nz/LEW/article/download/3672/3488/0'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Customizing MCMC methods for hierarchical models using ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC7069319/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'When should plant population models include age structure? - Chu', 'url': 'https://besjournals.onlinelibrary.wiley.com/doi/10.1111/1365-2745.12212'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A Bayesian multi-dimensional couple-based latent risk model ... - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC8048129/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A Bayesian Model to Estimate Male and Female Fertility Patterns at ...', 'url': 'https://epc2024.eaps.nl/uploads/240918'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Hierarchical Bayesian Integrated Modeling of Age- and Sex ... - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC12559060/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Flexible Bayesian Modelling of Age-Specific Counts in Many ... - arXiv', 'url': 'https://arxiv.org/pdf/2401.08247.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Estimating age-specific fertility rate in the World Population Prospects', 'url': 'https://www.un.org/development/desa/pd/sites/www.un.org.development.desa.pd/files/undesa_pd_2023_technical-paper_asfr.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Age-structured Jolly-Seber model expands inference and improves ...', 'url': 'https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0252748'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] MCMC Sampler Convergence Rates for Hierarchical Normal Linear ...', 'url': 'https://stat.duke.edu/~scs/Courses/Stat376/Papers/ConvergeRates/HierarchicalNormalConvergence.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Integrating uncertainty in time series population forecasts', 'url': 'https://www.demographic-research.org/volumes/vol29/43/29-43.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'MCMC Credible Interval Estimation', 'url': 'https://kramlinger.github.io/intro-mcmc/credible_intervals.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Simultaneous Estimation of Mixing Rates and Genetic Drift Under ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC1569702/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Quantifying demographic uncertainty: Bayesian methods for integral ...', 'url': 'https://esajournals.onlinelibrary.wiley.com/doi/10.1890/15-1526.1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] An Introduction to MCMC methods and Bayesian Statistics', 'url': 'https://dam.ukdataservice.ac.uk/media/307220/presentation4.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Bayesian reconstruction of two‐sex populations by age', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC4657758/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Three new methodologies for calculating the effective ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11577712/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Fast genomic prediction of breeding values using parallel ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5751823/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Projection of some Fertility Indicators of India using MCMC ...', 'url': 'https://papers.ssrn.com/sol3/Delivery.cfm/4880986.pdf?abstractid=4880986&mirid=1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Effective sample size: A measure of individual uncertainty ...', 'url': 'https://onlinelibrary.wiley.com/doi/full/10.1002/sim.10018'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Help for package bayesTFR', 'url': 'https://cran.r-project.org/web/packages/bayesTFR/refman/bayesTFR.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Probabilistic Estimation and Projection of the Annual Total Fertility ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11514362/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Integrating uncertainty in time series population forecasts', 'url': 'https://www.demographic-research.org/volumes/vol29/43/29-43.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Bayesian Population Projections for the United Nations - PMC - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC4196216/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Projection of some Fertility Indicators of India using MCMC ... - SSRN', 'url': 'https://papers.ssrn.com/sol3/Delivery.cfm/4880986.pdf?abstractid=4880986&mirid=1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Reconstructing Past Populations With Uncertainty From ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3613971/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': "[PDF] Bayesian estimation of total fertility from a population's age–sex ...", 'url': 'https://mathewhauer.github.io/papers/2018-StatisticalModelling.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A novel approach for estimating fertility rates in finite populations ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10810359/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Bayesian probabilistic population projections for all countries - PNAS', 'url': 'https://www.pnas.org/doi/10.1073/pnas.1211452109'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A modeling approach to forecast local demographic trends in ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11610681/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Accounting for Uncertainty About Past Values In Probabilistic ...', 'url': 'https://csss.uw.edu/files/working-papers/2018/wp159.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Accounting for Uncertainty About Past Values In Probabilistic ... - arXiv', 'url': 'https://arxiv.org/pdf/1806.01513.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A modeling approach to forecast local demographic trends in ...', 'url': 'https://esajournals.onlinelibrary.wiley.com/doi/10.1002/ecy.4459'}}

## Sources
https://en.wikipedia.org/wiki/Markov_chain_Monte_Carlo
https://pmc.ncbi.nlm.nih.gov/articles/PMC10810359/
https://pmc.ncbi.nlm.nih.gov/articles/PMC8365292/
https://sites.stat.columbia.edu/gelman/research/published/nestedRhat.pdf
https://www.humanfertility.org/File/GetDocument/Docs/Symposium/McDonald_Kippen.pdf
https://ecampusontario.pressbooks.pub/demographyandeconomics/chapter/chapter-14-forecasting-population-size-and-age-structure/
https://projecteuclid.org/journals/bayesian-analysis/advance-publication/R--A-Robust-MCMC-Convergence-Diagnostic-with-Uncertainty-Using/10.1214/20-BA1252.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC11439461/
https://mc-stan.org/docs/2_21/reference-manual/effective-sample-size-section.html
https://cran.r-project.org/web/packages/MCMCprecision/vignettes/Heck_2018_Statistics_and_Computing.pdf
https://www.humanfertility.org/File/GetDocument/Docs/Symposium/Schmertmann%20et%20al.pdf
https://www.displayr.com/what-is-effective-sample-size/
https://arxiv.org/pdf/1909.09545.pdf
https://www.un.org/development/desa/pd/sites/www.un.org.development.desa.pd/files/undesa_pd_2023_technical-paper_asfr.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC4196216/
https://pmc.ncbi.nlm.nih.gov/articles/PMC10810359/
https://pmc.ncbi.nlm.nih.gov/articles/PMC5096741/
https://www.pnas.org/doi/10.1073/pnas.1211452109
https://statmodeling.stat.columbia.edu/2017/12/15/burn-vs-warm-iterative-simulation-algorithms/
https://myweb.uiowa.edu/pbreheny/uk/teaching/701/notes/3-5.pdf
https://mc-stan.org/docs/2_18/reference-manual/notation-for-samples-chains-and-draws.html
https://hschuett.github.io/BayesForAccountingResearch/mcmc.html
https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/j.2041-210x.2012.00195.x
https://sites.stat.columbia.edu/gelman/research/published/brooksgelman2.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC4657758/
https://arxiv.org/html/2110.13017v5
https://pmc.ncbi.nlm.nih.gov/articles/PMC12559060/
https://ojs.victoria.ac.nz/LEW/article/download/3672/3488/0
https://pmc.ncbi.nlm.nih.gov/articles/PMC7069319/
https://besjournals.onlinelibrary.wiley.com/doi/10.1111/1365-2745.12212
https://pmc.ncbi.nlm.nih.gov/articles/PMC8048129/
https://epc2024.eaps.nl/uploads/240918
https://pmc.ncbi.nlm.nih.gov/articles/PMC12559060/
https://arxiv.org/pdf/2401.08247.pdf
https://www.un.org/development/desa/pd/sites/www.un.org.development.desa.pd/files/undesa_pd_2023_technical-paper_asfr.pdf
https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0252748
https://stat.duke.edu/~scs/Courses/Stat376/Papers/ConvergeRates/HierarchicalNormalConvergence.pdf
https://www.demographic-research.org/volumes/vol29/43/29-43.pdf
https://kramlinger.github.io/intro-mcmc/credible_intervals.html
https://pmc.ncbi.nlm.nih.gov/articles/PMC1569702/
https://esajournals.onlinelibrary.wiley.com/doi/10.1890/15-1526.1
https://dam.ukdataservice.ac.uk/media/307220/presentation4.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC4657758/
https://pmc.ncbi.nlm.nih.gov/articles/PMC11577712/
https://pmc.ncbi.nlm.nih.gov/articles/PMC5751823/
https://papers.ssrn.com/sol3/Delivery.cfm/4880986.pdf?abstractid=4880986&mirid=1
https://onlinelibrary.wiley.com/doi/full/10.1002/sim.10018
https://cran.r-project.org/web/packages/bayesTFR/refman/bayesTFR.html
https://pmc.ncbi.nlm.nih.gov/articles/PMC11514362/
https://www.demographic-research.org/volumes/vol29/43/29-43.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC4196216/
https://papers.ssrn.com/sol3/Delivery.cfm/4880986.pdf?abstractid=4880986&mirid=1
https://pmc.ncbi.nlm.nih.gov/articles/PMC3613971/
https://mathewhauer.github.io/papers/2018-StatisticalModelling.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC10810359/
https://www.pnas.org/doi/10.1073/pnas.1211452109
https://pmc.ncbi.nlm.nih.gov/articles/PMC11610681/
https://csss.uw.edu/files/working-papers/2018/wp159.pdf
https://arxiv.org/pdf/1806.01513.pdf
https://esajournals.onlinelibrary.wiley.com/doi/10.1002/ecy.4459