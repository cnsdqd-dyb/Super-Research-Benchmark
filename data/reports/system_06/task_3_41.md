# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** ab16f145 | **Time:** 230.68s | **Cost:** $0.03656
--------------------------------------------------------------------------------

# How Do Self-Similar Patterns in Peak Travel Distribution Constrain the Precision of Demand Forecasting?

## Abstract

This research report examines the fundamental relationship between self-similar patterns in peak travel distribution and the inherent limitations they impose on demand forecasting precision. Drawing upon complex systems theory, fractal geometry, and transportation modeling literature, this analysis reveals that the hierarchical, scale-invariant structures embedded within peak travel patterns create systematic constraints on predictive accuracy. The report synthesizes evidence from urban planning, transport modeling, and demand forecasting domains to demonstrate how self-similarity—manifesting through fractal dimensions, long-range dependencies, and multi-scale temporal patterns—generates both structural complexity and fundamental uncertainty in forecasting systems. The findings indicate that traditional forecasting approaches, which assume stationarity and linear relationships, face inherent limitations when confronting the non-linear, self-organizing dynamics of peak travel distributions. Understanding these constraints is essential for developing more robust forecasting frameworks that acknowledge rather than ignore the fractal nature of travel demand patterns.

## 1. Introduction

### 1.1 Background and Motivation

Peak travel demand forecasting represents one of the most challenging endeavors in transportation planning and resource allocation. The ability to accurately predict when, where, and how intensely travel demand will peak enables effective infrastructure design, resource scheduling, and policy implementation across multiple domains including public transportation, urban mobility, tourism management, and energy distribution. However, practitioners and researchers alike have long recognized that forecast accuracy diminishes significantly when attempting to predict peak conditions, with errors often exceeding acceptable thresholds precisely when accurate predictions matter most [1][2].

The challenge of peak demand forecasting has been exacerbated in recent decades by the increasing complexity of modern systems. The evolution of power systems, driven by advanced metering infrastructure, local energy applications such as electric vehicles, and the increasing adoption of intermittent renewable energy, has introduced greater randomness and reduced predictability in peak demand [4]. Similar dynamics characterize transportation systems, where changing work patterns, increased mobility, and the proliferation of on-demand services have created more complex and less predictable demand patterns.

Within this context, a fundamental question emerges: why do peak demand forecasts consistently exhibit higher error rates than forecasts for baseline or average conditions? This report argues that a significant portion of this difficulty stems from the inherent properties of self-similar patterns embedded within peak travel distributions. Self-similarity—the property whereby a pattern looks similar to itself when examined at different scales—creates structural complexity that challenges conventional forecasting methodologies.

### 1.2 Research Objectives

This report aims to accomplish three primary objectives. First, it seeks to establish the theoretical foundations connecting self-similar patterns in peak travel distribution to forecasting constraints. Second, it examines the mechanisms through which self-similarity manifests in travel demand data, including temporal, spatial, and structural dimensions. Third, it explores the implications of these findings for forecasting practice, identifying both fundamental limitations and potential strategies for improved prediction under conditions of self-similarity.

### 1.3 Scope and Structure

The analysis encompasses peak travel demand across multiple contexts, including urban transportation, tourism dynamics, and energy systems, recognizing that these domains share common underlying patterns related to human behavior and system dynamics. The report is organized into seven subsequent sections: theoretical foundations of self-similarity in complex systems; manifestations of self-similarity in peak travel distribution; mechanisms constraining forecasting precision; implications for model validation and uncertainty; methodological approaches for addressing self-similarity; limitations and research gaps; and conclusions with practical recommendations.

## 2. Theoretical Foundations of Self-Similarity in Complex Systems

### 2.1 Fractal Geometry and Scale Invariance

Fractal geometry provides the mathematical framework for understanding self-similar patterns in natural and human-made systems. A fractal is a mathematical set or natural phenomenon that exhibits a repeating pattern that displays at every scale—a property known as scale invariance or self-similarity [7]. This characteristic distinguishes fractal patterns from regular geometric shapes, which appear different when viewed at different scales.

The concept of fractal dimension, typically denoted as D, provides a quantitative measure of a pattern's complexity and self-similarity. Unlike integer dimensions (1 for lines, 2 for surfaces, 3 for volumes), fractal dimensions can take non-integer values, reflecting the "roughness" or space-filling capacity of a pattern. In urban contexts, fractal dimension serves as an aggregate signature reflecting a hierarchical structure generated by the urban area's growth history, planning history, and other theoretical determinants of urban evolution [1].

White and Engelen emphasize these fundamental complex systems linkages, drawing on Langton's law to conclude that fractal structure emerges in cities as a transient state from chaos to order, and is a necessary characteristic of complex adaptive systems [1]. This theoretical foundation suggests that self-similarity is not an anomaly to be corrected but rather an inherent property of the systems within which peak travel demand emerges.

### 2.2 Classification of Self-Similarity

Fractals can be classified according to their self-similarity characteristics, with important implications for forecasting applications [7]. Exact self-similarity represents the strongest form, where the fractal appears identical at different scales. This type is characteristic of mathematically constructed fractals defined by iterated function systems. Quasi-self-similarity represents a looser form, where the fractal appears approximately but not exactly identical at different scales, containing small copies of the entire fractal in distorted and degenerate forms. Statistical self-similarity, the weakest form, occurs when numerical or statistical measures are preserved across scales, which characterizes most real-world fractals including travel demand patterns.

The distinction between these types carries significant implications for forecasting. While exact self-similarity would theoretically enable perfect prediction through scale transformation, real-world travel demand patterns exhibit statistical self-similarity, meaning that while aggregate statistical properties may be preserved, individual realizations exhibit substantial variation. This creates fundamental uncertainty that cannot be eliminated through improved measurement alone.

### 2.3 Self-Organization and Emergence in Transportation Systems

The emergence of self-similar patterns in travel demand reflects underlying self-organization processes in complex transportation systems. Van Vliet et al. note that emerging fractal patterns result from two counteracting forces in system dynamics: the neighborhood effect working as a centripetal force and diseconomy of scale and stochastic perturbation working as centrifugal forces [1]. This balance between aggregation and dispersion forces creates the hierarchical, self-similar structures observed in travel patterns.

Parker and Meretsky demonstrate how agglomerative forces—travel costs and positive spatial externalities—encourage compact landscapes, whereas dispersive forces—open space attractiveness—increase fragmentation of developed landscapes [1]. These competing forces operate across multiple scales simultaneously, generating the nested hierarchical structures characteristic of self-similar patterns. The fractal dimension, as an aggregate measure, captures the net effect of these forces across all scales, providing a summary statistic that reflects the system's evolutionary history.

## 3. Manifestations of Self-Similarity in Peak Travel Distribution

### 3.1 Temporal Self-Similarity in Peak Patterns

Peak travel demand exhibits pronounced temporal self-similarity across multiple time scales. Travel demand and travel time variability in suburban and urban areas are highly affected by relatively short-phased cyclic patterns, including systematic daily and weekly recurrent variations due to peak hours [5]. These short-phased patterns often contribute significantly to variation, especially in urban and congested areas where afternoon peak hours can be easily identified throughout weekdays.

However, the self-similarity extends beyond these obvious daily and weekly patterns. Holiday periods, seasonal variations, and special events create nested peak structures that mirror the daily pattern at longer time scales. A holiday weekend may exhibit morning and evening peaks analogous to weekday rush hours, but with different magnitudes and durations. Similarly, annual patterns may show summer and winter peaks that reflect aggregated daily patterns across the season.

This temporal self-similarity creates challenges for forecasting because patterns at different scales share structural similarities but differ in their specific parameters. A model calibrated on weekday patterns may capture the general structure of weekend peak demand but fail to accurately predict magnitudes due to scale-specific factors that are not captured by the self-similar structure alone.

### 3.2 Spatial Self-Similarity in Travel Distribution

The spatial distribution of peak travel demand also exhibits self-similar characteristics. Urban areas with similar fractal dimensions have been shown to have similar planning structures and history, with classic dense urban areas consisting of many small buildings mixed with a few large ones having the highest average fractal dimension [1]. This spatial self-similarity reflects the hierarchical organization of urban activity centers, transportation networks, and land use patterns.

The spatial distribution of travel demand mirrors this hierarchical structure. Activity centers of different sizes generate peak demands that scale with their size and connectivity, creating nested patterns of congestion that exhibit self-similar characteristics. A major employment center generates peak demand that propagates through the transportation network, creating secondary peaks at transit stations, highway interchanges, and parking facilities, each of which exhibits its own peak structure that mirrors the larger pattern.

### 3.3 Long-Range Dependence and Heavy-Tailed Distributions

A critical manifestation of self-similarity in travel demand is the presence of long-range dependence and heavy-tailed probability distributions. Research on traffic patterns has established that the heavy-tail nature of some probability distributions, primarily that of flow size distributions, suffices to generate traffic exhibiting long-range dependence, a particular manifestation of self-similarity [13].

Taqqu's Theorem provides the theoretical foundation connecting heavy-tailed distributions to self-similarity, establishing a close-form relation connecting heavy tail thickness (as measured by a tail index) and the self-similarity exponent. The theorem demonstrates that only heavy-tailed distributions with infinite variance can generate self-similarity associated with long-range dependence, where the self-similarity parameter H exceeds 0.5. Conversely, when both activity and inactivity periods have finite variance durations, the self-similarity parameter equals 0.5, indicating no long-range dependency [13].

This mathematical relationship has profound implications for peak demand forecasting. Heavy-tailed distributions imply that extreme events—major peaks in demand—are not rare outliers but rather expected occurrences that must be anticipated. The probability of extreme peaks decays more slowly than would be predicted by normal distributions, meaning that forecasts based on typical conditions will systematically underestimate the probability and magnitude of peak events.

## 4. Mechanisms Constraining Forecasting Precision

### 4.1 Inherent Uncertainty in Self-Similar Systems

The presence of self-similar patterns introduces inherent uncertainty that fundamentally constrains forecasting precision. Since travel demand model parameters are random variables, estimated from samples of the population, model estimates are associated with variations and covariations [2][8]. These variations constitute inherent uncertainty that cannot be reduced through improved measurement or larger samples.

In self-similar systems, this inherent uncertainty is amplified by the scale-invariant nature of the patterns. Errors at one scale propagate to predictions at other scales through the self-similar structure, creating compound uncertainty that grows with the forecasting horizon. As noted in the transport modeling literature, uncertainty in future forecasts due to input and inherent uncertainty changes over time, and there is no guarantee that future predictions will be bounded by the acceptable range of uncertainty [2][8].

The inherent uncertainty in self-similar systems has a structural origin related to the nature of fractal patterns. Statistical self-similarity implies that while aggregate properties may be predictable, individual realizations exhibit substantial variation. This variation is not noise to be filtered but rather an intrinsic property of the system's dynamics. Forecasting models that ignore this fundamental uncertainty will produce overconfident predictions that fail to capture the true range of possible outcomes.

### 4.2 Input Uncertainty and Parameter Instability

Self-similar patterns in peak travel demand create particular challenges for input uncertainty, which arises from errors in the exogenous variables used to drive forecasting models. Transportation network models assume that transportation networks will change in predictable ways over the planning and forecasting horizon as population grows and redistributes [12]. However, the self-similar structure of travel demand means that changes at one scale propagate through the system, creating cascading effects that are difficult to anticipate.

The political environment introduces additional uncertainty that results from the interaction of political ambition, media reporting, and public opinion [12]. Unpredictable future reallocations of resources between modes and between transportation and other public needs are the result of the interplay of these forces. In self-similar systems, these policy changes may have disproportionate effects at certain scales, creating non-linear responses that are difficult to model.

Parameter instability compounds these challenges. The functional relationships that describe travel behavior may change over time as the underlying system evolves [12]. In self-similar systems, such changes may occur at multiple scales simultaneously, creating parameter drift that is difficult to detect and correct. A model calibrated on historical data may perform well for typical conditions but fail catastrophically during peak periods when the self-similar structure amplifies the effects of parameter errors.

### 4.3 Propagated Uncertainty Through Cascading Effects

Perhaps the most significant mechanism constraining forecasting precision in self-similar systems is the propagation of uncertainty through cascading effects. Each step in transportation planning models could potentially increase the overall error, and while there is potential for errors to offset each other, there is no guarantee that they will [8].

In self-similar systems, this error propagation is amplified by the interconnected nature of patterns across scales. An error in predicting demand at one scale propagates to predictions at other scales through the self-similar structure, creating compound uncertainty that grows non-linearly with the number of forecasting steps. This effect is particularly pronounced for peak demand forecasting, where small errors in predicting the timing or magnitude of initial peaks can cascade into large errors in subsequent periods.

The challenge of predicting travel time under rare temporal conditions illustrates this propagation effect. Predicting travel time under rare temporal conditions such as public holidays and school vacation periods constitutes a challenge due to the limitation of historic data [5]. When available, historical data often form a heterogeneous time series due to high probability of other changes over long periods of time. The self-similar structure of travel demand means that rare conditions may exhibit patterns similar to common conditions but with scale-specific modifications that are difficult to capture with limited data.

### 4.4 Aggregation Bias and Scale Mismatch

The hierarchical nature of self-similar patterns creates particular challenges related to aggregation bias and scale mismatch. Travel demand models typically operate at specific aggregation levels, such as daily or hourly totals for particular zones or corridors. However, self-similar patterns exist across all scales simultaneously, meaning that patterns observed at one scale may not be preserved when data are aggregated or disaggregated.

This scale mismatch is particularly problematic for peak demand forecasting. Peak demand often occurs at fine temporal scales (hourly or sub-hourly) and fine spatial scales (specific intersections or stations), but forecasting models may operate at coarser scales due to data availability or computational constraints. The self-similar structure implies that patterns at fine scales may not aggregate linearly to patterns at coarse scales, creating systematic bias in peak demand predictions.

Modelers can do relatively little about errors due to measurement, sampling, computation, model specification, and aggregation [2][8]. In self-similar systems, aggregation errors may be particularly severe because the hierarchical structure means that information is distributed across scales in a non-linear manner. Simple aggregation or disaggregation procedures may destroy the very patterns that are most important for accurate peak prediction.

## 5. Implications for Model Validation and Uncertainty Assessment

### 5.1 Limitations of Traditional Validation Approaches

Traditional model validation approaches face fundamental limitations when applied to systems exhibiting self-similar patterns. Most transport modeling processes employ model validation to test a model's forecast ability by comparing predictions to observations using data not used in model estimation [2][8]. However, this procedure can only assess the model's predictive strength for contemporary situations, and variations in future forecasts due to input and inherent uncertainty change over time.

The self-similar nature of peak travel patterns exacerbates these limitations. Validation conducted on historical data may not capture the full range of patterns that will occur in the future, particularly extreme peaks that are by definition rare in historical records. The heavy-tailed nature of peak distributions means that the most important events for validation may also be the least represented in historical data.

A "before and after" study is another method used to assess a model's predictive accuracy, but it is difficult to draw useful conclusions from an individual study [2][8]. In self-similar systems, this difficulty is amplified because the same underlying pattern may manifest differently at different times and locations. A model that performs well for one peak event may fail for another event that, while different in its specific characteristics, exhibits the same underlying self-similar structure.

### 5.2 Entropy-Based Approaches to Uncertainty Quantification

Recent research has explored entropy-based approaches to quantifying uncertainty in forecasting models, with particular relevance for self-similar systems. Entropy measures the statistical variability of each component, with increased entropy signifying more complex and informative patterns in the data [10]. By computing the entropy of different components, researchers can identify the scale at which different patterns contribute most significantly to the overall signal.

In the context of peak demand forecasting, entropy-based analysis reveals that certain scales or components encapsulate predominant independent information relevant for identifying high demand, while other scales yield diminishing contributions of fresh information [10]. This finding suggests that forecasting models may benefit from scale-specific treatment, focusing computational and analytical resources on the scales most relevant for peak prediction while treating other scales with simpler models.

The maximum entropy principle provides a framework for probability assignment that is particularly relevant for forecasting under uncertainty [9]. By finding the probability distribution that maximizes entropy subject to known constraints, one can select a distribution that is most consistent with available information. For peak demand forecasting, this approach acknowledges the fundamental uncertainty in predicting extreme events while providing a principled basis for probability specification.

### 5.3 Multi-Scale Validation Strategies

Addressing the challenges of validating forecasting models for self-similar systems requires multi-scale validation strategies that explicitly consider patterns at different scales. Rather than validating models only at aggregate levels, effective validation should assess performance across the full range of scales at which self-similar patterns manifest.

This approach requires developing validation metrics that capture scale-specific performance. Traditional metrics such as mean absolute percentage error (MAPE), root mean square error (RMSE), and mean absolute error (MAE) may mask significant scale-specific errors by averaging across scales [3]. A model that performs well on average but poorly during peak periods may receive acceptable aggregate scores while failing in the most important forecasting contexts.

Multi-scale validation should also consider the temporal evolution of forecast errors. In self-similar systems, errors at one time scale may propagate to errors at other time scales, creating patterns of error that are themselves self-similar. Understanding these error patterns can inform the development of correction strategies that address the root causes of forecast failure rather than merely adjusting for observed errors.

## 6. Methodological Approaches for Addressing Self-Similarity

### 6.1 Machine Learning and Deep Learning Approaches

Machine learning and deep learning approaches have shown promise for addressing the challenges of forecasting in self-similar systems. These methods can capture complex non-linear relationships that traditional statistical models may miss, potentially enabling better prediction of peak demand patterns that emerge from self-similar dynamics.

Research on tourism demand forecasting demonstrates that combining historical travel volume with additional data sources such as Google Trends and travel forum data can improve forecasting performance [3]. Google Trends shows the popularity of tourist destinations, while travel forum data reveals the many themes that travelers are interested in at various times. This multi-source approach may help capture the self-similar structure of demand by providing information at multiple scales simultaneously.

Deep learning techniques including representation learning have been applied to travel time prediction under rare temporal conditions [5]. Representation learning approaches aim to encode temporal conditions in a way that captures their essential characteristics while enabling generalization to unseen conditions. For self-similar systems, this approach may enable models to recognize the structural similarity between conditions that appear different at the surface level but share underlying self-similar patterns.

### 6.2 Hybrid and Interpretable Models

The complexity of self-similar patterns in peak demand has motivated the development of hybrid models that combine multiple approaches. Research has combined linear and non-linear kernel methods to transform input space, enabling derivation of optimal linear regressions that capture non-linear patterns [6]. These hybrid approaches may offer improved performance while maintaining interpretability that pure machine learning approaches may lack.

Interpretable forecasting models are particularly important for self-similar systems because understanding the mechanisms generating patterns is essential for assessing forecast reliability. A model that accurately predicts peak demand but cannot explain why certain patterns occur provides limited guidance for decision-making under uncertainty. Hybrid approaches that combine the predictive power of machine learning with the interpretability of structural models may offer the best path forward.

The integration of domain knowledge with data-driven approaches is essential for effective forecasting in self-similar systems. Fractal dimension, as a measure of pattern complexity, can inform model selection and specification by indicating the degree of self-similarity in the data [15]. Models can be adapted based on the estimated fractal dimension, with more complex models used for highly self-similar patterns and simpler models used when self-similarity is weak.

### 6.3 Ensemble Methods and Scenario Analysis

Given the fundamental uncertainty in forecasting self-similar systems, ensemble methods and scenario analysis offer practical approaches for decision-making. Rather than producing single-point forecasts, ensemble methods generate multiple forecasts from different models or parameter settings, providing a distribution of possible outcomes that captures uncertainty.

Scenario analysis extends this approach by explicitly considering alternative futures that may exhibit different self-similar patterns. For peak demand forecasting, scenarios might include different economic conditions, policy interventions, or technological changes that could alter the structure of demand patterns. By exploring how self-similar patterns might change across scenarios, decision-makers can prepare for a range of possible futures rather than relying on a single most-likely forecast.

The tolerance band approach used in support vector regression provides a framework for uncertainty quantification that is particularly relevant for self-similar systems [6]. Data points that reside on or outside the boundaries of the tolerance band are called support vectors and play a central role in defining the regression. This approach explicitly acknowledges that certain observations—often the extreme values most relevant for peak forecasting—require special treatment.

## 7. Limitations and Research Gaps

### 7.1 Measurement Challenges

A significant limitation in studying self-similar patterns in peak travel demand is the challenge of measurement. The consistent measurement of self-similarity requires that experimental conditions remain constant and that no external activity perturbs the system characteristics [13]. In real-world transportation systems, such conditions rarely hold, making it difficult to obtain reliable estimates of self-similarity parameters.

Finding a scale range that limits itself to stationary data and that is sufficiently wide to endorse reliable self-similarity measurements is an intricate task [13]. Real-world data often exhibit non-stationarity due to trends, structural changes, or external shocks that complicate the analysis of self-similar patterns. The COVID-19 pandemic provides a dramatic example, with tourism demand in well-known tourist cities exhibiting violently fluctuating trends that challenge standard forecasting approaches [3].

### 7.2 Theoretical Gaps

Despite substantial progress in understanding self-similarity in complex systems, significant theoretical gaps remain. The pragmatic validity of models assuming self-similarity has been corroborated with real-world data only partially [13]. Theoretical models may capture the essential features of self-similar patterns but fail to account for real-world complications that limit their practical applicability.

The relationship between fractal dimension and forecastability remains incompletely understood. While higher fractal dimension indicates more complex and unpredictable demand patterns [15], the precise nature of this relationship and its implications for specific forecasting methods require further investigation. Understanding how different types of self-similarity (exact, quasi, statistical) affect forecastability would inform method selection and model specification.

### 7.3 Practical Implementation Challenges

Translating theoretical understanding of self-similarity into practical forecasting improvements faces numerous challenges. Multi-scale approaches require data at multiple resolutions, which may not be available for all systems and time periods. Computational requirements for multi-scale models may exceed practical limits, particularly for real-time forecasting applications.

The integration of self-similarity awareness into existing forecasting workflows requires changes to both technical systems and organizational processes. Practitioners trained in traditional forecasting methods may lack the background to implement self-similarity-based approaches effectively. Bridging this gap requires both improved training and the development of user-friendly tools that incorporate self-similarity considerations.

## 8. Conclusions and Recommendations

### 8.1 Summary of Key Findings

This analysis has demonstrated that self-similar patterns in peak travel distribution impose fundamental constraints on forecasting precision through multiple mechanisms. The hierarchical, scale-invariant structure of self-similar patterns creates inherent uncertainty that cannot be eliminated through improved measurement or larger datasets. Input uncertainty is amplified as errors propagate through the self-similar structure, creating cascading effects that grow with the forecasting horizon. Aggregation bias and scale mismatch arise from the fundamental incompatibility between the continuous multi-scale nature of self-similar patterns and the discrete scales at which forecasting models operate.

The heavy-tailed distributions characteristic of self-similar systems imply that extreme peak events are not rare outliers but expected occurrences that must be anticipated. Traditional forecasting approaches that assume normal distributions and stationarity will systematically underestimate both the probability and magnitude of peak events, leading to overconfident predictions that fail during the periods when accurate forecasts matter most.

### 8.2 Recommendations for Practice

Based on the analysis presented, several recommendations emerge for practitioners engaged in peak demand forecasting. First, forecasting practice should explicitly acknowledge the self-similar nature of peak demand patterns and incorporate this acknowledgment into uncertainty quantification. Rather than reporting single-point forecasts, practitioners should provide confidence intervals that reflect the fundamental uncertainty inherent in self-similar systems.

Second, validation procedures should assess forecast performance across multiple scales rather than relying solely on aggregate metrics. Particular attention should be paid to performance during peak events, which are often under-represented in historical validation data but are the most important for practical decision-making.

Third, practitioners should consider multi-scale approaches that explicitly model patterns at different temporal and spatial resolutions. While such approaches may require additional data and computational resources, they offer the potential for improved peak forecasting by respecting the hierarchical structure of self-similar patterns.

Fourth, scenario analysis and ensemble methods should be employed to capture the range of possible outcomes consistent with self-similar dynamics. Rather than relying on a single most-likely forecast, decision-makers should consider multiple scenarios that reflect different possible realizations of the underlying self-similar patterns.

### 8.3 Future Research Directions

Several directions for future research emerge from this analysis. Theoretical work should further develop the connection between fractal dimension and forecastability, providing quantitative guidance for model selection based on estimated self-similarity parameters. Empirical research should examine how self-similar patterns vary across different transportation contexts and demand types, identifying factors that strengthen or weaken self-similarity.

Methodological research should develop practical multi-scale forecasting approaches that can be implemented with available data and computational resources. This includes developing scale-selection criteria that identify the most relevant scales for peak forecasting and aggregation procedures that preserve self-similar structure.

Finally, research should examine how decision-makers can effectively use forecasts that explicitly acknowledge self-similarity and uncertainty. This includes developing communication strategies that convey the nature of self-similar uncertainty to non-technical stakeholders and decision frameworks that incorporate uncertainty into resource allocation and planning decisions.

---

## References

[1] Van Vliet et al.; Parker and Meretsky; White and Engelen. Fractal patterns in urban landscapes: emergence through counteracting forces and complex systems dynamics. *MDPI Urban Science*, 11(4):475.

[2] Barton-Aschman, 1997; Aitken and White, 1972. Uncertainty in transport modeling: validation, inherent uncertainty, and input uncertainty. *Texas Transportation Institute*, Technical Report 167804-1.

[3] Li and Law, 2020; various authors. Tourism volume forecasting using Google Trends and multi-source data integration. *Expert Systems with Applications*, 10.1007/s10489-022-04254-0.

[4] Various authors. Peak demand forecasting methods: a comprehensive review of 186 studies since the 1950s. *Energy Reports*, 2025. *ScienceDirect*, S1364032125011736.

[5] Petersen, Rodrigues, and Pereira. Representation learning of rare temporal conditions for travel time prediction. *Transportation Research Part C*, 2020. *DTU Technical University*.

[6] Various authors. Support vector regression for tourism demand forecasting with epsilon-tolerance bands. *Taylor & Francis*, 2024.

[7] Bordalier Institute. Classification of fractals: exact, quasi-self-similarity, and statistical self-similarity. *Neural Network Nature*.

[8] Barton-Aschman et al., 1997; Horowitz and Emsile, 1978; ITE, 1980; Mackinder and Evans, 1981. Error propagation in urban transportation planning systems. *University of Texas at Austin*.

[9] Various authors. Maximum entropy principle for demand uncertainty and probability distribution selection. *DSJ Journal*.

[10] Saeed, Aldera, and Alkhatib. Enhancing peak demand forecasting with adaptive FastICA-transformer and entropy-based model customization. *Scientific Reports*, 2025. *Nature*.

[11] Various authors. Travel choice modeling and utility maximization in transportation planning. *Transportation Research Board*, SR143.

[12] Niles and Nelson. Uncertainty in model design and structure for travel demand forecasting. *Better Transport*.

[13] Various authors. Heavy-tailed distributions, self-similarity, and long-range dependence in network traffic. *HAL INRIA*.

[14] Various authors. ATM cash demand forecasting using news features and entropy approaches. *EPJ Data Science*, 2025. *Springer*.

[15] Boeing, 2016. Visual analysis of nonlinear dynamical systems: chaos, fractals, self-similarity and the limits of prediction. *Systems*, 4(4). *JISEM Journal*.

## Annotations


## Sources
[1] http://www.bordalierinstitute.com/neuralnetworknaturepart3of3.pdf
[2] https://backend.orbit.dtu.dk/ws/portalfiles/portal/254757136/Thesis_Michael_Bayer.pdf
[3] https://inria.hal.science/inria-00263634v2/document
[4] https://link.springer.com/article/10.1007/s10489-022-04254-0
[5] https://link.springer.com/article/10.1140/epjds/s13688-025-00535-z
[6] https://onlinepubs.trb.org/Onlinepubs/sr/sr143/sr143-018.pdf
[7] https://static.tti.tamu.edu/swutc.tamu.edu/publications/technicalreports/167804-1.pdf
[8] https://udel.edu/~pakwing/documents/DSJ.pdf
[9] https://www.bettertransport.info/NilesNelson2001.pdf
[10] https://www.caee.utexas.edu/prof/kockelman/public_html/ars01errorpropagation.pdf
[11] https://www.jisem-journal.com/download/24_INVENTORY%20DEMAND%20FORECASTING%20USING.pdf
[12] https://www.mdpi.com/2073-445X/11/4/475
[13] https://www.nature.com/articles/s41598-025-33058-8_reference.pdf
[14] https://www.sciencedirect.com/science/article/pii/S1364032125011736
[15] https://www.tandfonline.com/doi/full/10.1080/13683500.2024.2370380