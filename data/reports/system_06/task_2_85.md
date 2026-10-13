# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** fc913cac | **Time:** 353.90s | **Cost:** $0.14935
--------------------------------------------------------------------------------

# Does the Lagged Response of Soil-Vegetation Feedback Amplify Prediction Uncertainty in Global Carbon Budget Models?

## Abstract

Global carbon budget models rely on accurate representations of soil-vegetation interactions to project future climate trajectories and estimate remaining carbon budgets. However, the temporal lags inherent in soil-vegetation feedback mechanisms introduce substantial complexity into these projections. This report examines whether the lagged response of soil-vegetation feedback amplifies prediction uncertainty in global carbon budget models, synthesizing evidence from Earth system model intercomparisons, observational studies, and theoretical analyses. The evidence demonstrates that lagged soil-vegetation feedbacks indeed contribute significantly to prediction uncertainty, with complex models exhibiting uncertainties more than ten times larger than conventional approaches [1]. The interplay between microbial dynamics, rhizosphere priming effects, and climate variability creates cascading uncertainties that propagate through carbon cycle feedbacks [2]. Understanding these lagged responses is critical for constraining the largest source of uncertainty in future carbon cycle projections and improving the reliability of carbon budget estimates.

## 1. Introduction

The quantification of global carbon budgets represents one of the most consequential challenges in contemporary climate science. Remaining carbon budget estimates can vary by ±150 PgC due to uncertainties in historical warming levels, with an additional ±60 PgC uncertainty arising from geophysical responses to non-CO₂ emissions [3]. These substantial uncertainties fundamentally constrain our ability to establish greenhouse gas emission targets consistent with limiting global warming to specific thresholds. At the heart of this uncertainty lies the terrestrial carbon cycle, where soil-vegetation interactions play a pivotal role in determining whether terrestrial ecosystems act as carbon sinks or sources under changing climate conditions.

Soil-vegetation feedback encompasses a complex suite of processes through which plants influence soil carbon dynamics and, conversely, through which soil conditions affect vegetation productivity and distribution. These interactions operate across multiple temporal scales, from immediate physiological responses to decadal-scale soil carbon turnover processes. The lagged nature of many soil-vegetation feedbacks—particularly those involving soil organic matter decomposition, microbial community dynamics, and nutrient cycling—introduces substantial complexity into carbon budget projections. Understanding whether and how these lagged responses amplify prediction uncertainty is essential for improving model reliability and informing climate policy decisions.

The IPCC Sixth Assessment Report emphasizes that land carbon storage remains the largest source of uncertainty in future carbon cycle projections, with this uncertainty persisting across multiple generations of Earth system models [4]. This persistent uncertainty highlights the fundamental challenges inherent in representing soil-vegetation feedbacks and their temporal dynamics. The present report synthesizes current understanding of how lagged soil-vegetation feedbacks contribute to prediction uncertainty, examining evidence from model intercomparison projects, observational networks, and theoretical analyses of carbon cycle dynamics.

## 2. Theoretical Framework: Soil-Vegetation Feedback Mechanisms

### 2.1 Bidirectional Interactions in the Soil-Vegetation System

Soil-vegetation feedback operates through bidirectional interactions that connect plant productivity, litter inputs, and soil carbon decomposition. Plants influence soil carbon dynamics through the quantity and quality of organic matter inputs, including leaf litter, root exudates, and fine root turnover. Simultaneously, soil conditions—including moisture, temperature, nutrient availability, and microbial community composition—affect plant growth, phenology, and stress tolerance. These interactions create feedback loops that can either amplify or dampen carbon cycle responses to environmental perturbations.

The conventional Century-type model represents soil carbon decomposition using first-order kinetics with multiple pools characterized by different turnover times [1]. This approach, while computationally tractable, may inadequately capture the complex temporal dynamics arising from microbial interactions, physical protection mechanisms, and priming effects. More sophisticated representations, including vertically resolved models and microbial-explicit frameworks such as the Microbial-Mineral Carbon Stabilization (MIMICS) model, incorporate additional process complexity that better represents the mechanistic basis of soil carbon dynamics [1].

### 2.2 Temporal Lag Characteristics in Soil-Vegetation Feedbacks

The temporal structure of soil-vegetation feedbacks exhibits considerable heterogeneity across different processes and scales. Soil carbon turnover times (τs), defined as the ratio of mean soil carbon stocks to heterotrophic respiration (τs = Cs/Rh), vary from years to decades depending on soil type, climate, and vegetation characteristics [5]. This inherent temporal lag between carbon input and release creates substantial inertia in the soil carbon system, meaning that current soil carbon stocks reflect environmental conditions from previous decades or even centuries.

The lagged response of soil carbon to environmental changes has been demonstrated through long-term experimental manipulations. In a seven-year soil warming study at the Harvard Forest, warming-induced soil carbon losses totaled 13.0 Mg·C·ha⁻¹, while concurrent vegetation carbon gains amounted to 7.0 Mg·C·ha⁻¹ [6]. The net carbon loss over the study period demonstrates that soil carbon losses initially exceeded vegetation gains, though the annual net losses decreased over time as plant carbon storage increased. This temporal asymmetry in response magnitudes and timescales exemplifies the complexity introduced by lagged feedbacks.

Rhizosphere priming effects represent another source of temporal lag in soil-vegetation interactions. The priming effect, whereby root activity stimulates soil organic matter decomposition, operates through microbial activation and nutrient mobilization processes that unfold over weeks to months [2]. Recent modeling studies incorporating Michaelis-Menten functions to represent priming effects have demonstrated that this mechanism could induce an additional 40 PgC loss from northern soils by 2100 under intermediate emission scenarios [2]. The temporal dynamics of priming effects—requiring sufficient root respiration to trigger microbial activity and subsequent nutrient release—introduce lagged responses that complicate carbon budget projections.

## 3. Sources of Uncertainty in Carbon Budget Models

### 3.1 Parameter Uncertainty

Parameter uncertainty arises from imprecise estimates of the values characterizing soil carbon decomposition rates, vegetation productivity responses, and feedback strengths. In agroecosystem models, soil organic carbon stock data serve as key inputs for quantifying cropland carbon budgets and soil carbon credits [7]. However, substantial discrepancies exist between widely used SOC stock datasets. The Rapid Carbon Assessment dataset (RaCA) and Gridded Soil Survey Geographic Database (gSSURGO) exhibit a relative difference of 48.0% for 0–30 cm SOC stock in the U.S. Midwest, quantified using Normalized Root Mean Square Error [7].

The propagation of SOC stock uncertainty through carbon budget calculations depends critically on the specific application. When comparing cover crop versus no cover crop scenarios, the uncertainty of calculated soil carbon credits induced by initial SOC% uncertainty was less than 4% for 90% of cases [7]. However, both simulated ΔSOC and its uncertainty were negatively correlated with initial SOC%, while ΔSOC uncertainty was positively correlated with air temperature [7]. These correlations indicate that parameter uncertainties interact with environmental conditions to produce spatially heterogeneous uncertainty patterns.

Monte Carlo simulation analyses have demonstrated that soil carbon parameters are most influential in contributing to overall carbon budget uncertainty due to the relative size of the soil carbon pool [8]. A reduction by one-half in the range of soil carbon parameters was required to achieve approximately the same effect on uncertainty reduction as more modest changes in other parameter categories [8]. The importance index, which aggregates the effects of parameter uncertainties on intermediate carbon pools, consistently identifies soil carbon as the dominant uncertainty source across multiple years of projection.

### 3.2 Structural Uncertainty

Structural uncertainty arises from differences in model formulation, including the representation of processes, pool structures, and mathematical formulations. This form of uncertainty is particularly relevant for soil-vegetation feedbacks, where alternative model structures can represent the same underlying processes using different assumptions and levels of complexity. The most important short-term goal in Earth system modeling should be to represent theoretical uncertainty in soil carbon decomposition and formation processes through different underlying model structures [9].

Comparative analyses of soil carbon decomposition models with distinct structures reveal substantial divergence in projected responses to climate change. Both the vertically resolved model and the microbial-explicit model project much greater uncertainties to climate change than the conventional soil carbon model, with both positive and negative C-climate feedbacks, whereas the conventional model consistently predicts positive soil C-climate feedback [1]. The uncertainties in the vertically resolved model or MIMICS are more than ten times larger than that in the conventional model, demonstrating that increased model complexity does not necessarily reduce prediction uncertainty [1].

This counterintuitive result—where more parameters and explicit dynamics lead to larger prediction uncertainty—highlights the fundamental challenge of representing soil-vegetation feedbacks. Complex models capture additional processes but also introduce additional degrees of freedom that can amplify uncertainty propagation. The larger uncertainty in complex models suggests the need to strike a balance between model complexity and the need to include diverse model structures to forecast soil carbon dynamics with high confidence [1].

### 3.3 Observational Uncertainty and Data Limitations

Observational uncertainty encompasses errors in measurement, sampling, and spatial representation of soil carbon stocks and fluxes. The International Soil Moisture Network and similar synthesis efforts provide quality-controlled databases for calibration and validation, but models do relatively well in capturing large-scale variability while poorly reproducing observed patterns at scales of hundreds of kilometers and smaller [10]. This scale-dependent performance introduces uncertainty that propagates through carbon budget calculations.

Data-driven parameter ensembles derived from assimilating re-gridded global soil carbon data, such as those from the Harmonized World Soil Database and the Northern Circumpolar Soil Carbon Database, assume that soil carbon content was at steady state [11]. The probability inversion using Markov Chain Monte Carlo techniques is effective in constraining targeted parameters, but the underlying steady-state assumption may not hold under changing climate conditions [11]. This temporal mismatch between observational data and model requirements introduces additional uncertainty into carbon budget projections.

## 4. Evidence for Lagged Feedback Amplification of Uncertainty

### 4.1 Multi-Model Ensemble Evidence

Earth system model intercomparison projects provide compelling evidence that lagged soil-vegetation feedbacks contribute substantially to prediction uncertainty. The CMIP6 and CMIP5 model generations exhibit substantial variation in their representation of soil carbon dynamics and associated controls [5]. Evaluation using multiple methods—including coefficients of variation, spatial standard deviations, spatial Pearson correlation coefficients, and root mean square errors—reveals that spatial soil carbon distributions and their controls differ substantially across models [5].

The nonlinear feedback parameters among advanced Earth system models show large uncertainty, ranging from 0.2–9.6% for β and 0.8–45% for γ [12]. This wide range suggests substantial structural uncertainty in how models represent carbon cycle feedbacks, including the lagged responses of soil-vegetation interactions. The IPCC assessment notes that there is still low confidence on the relative roles and importance of ocean and terrestrial carbon processes on TCRE variability and uncertainty on centennial time scales [3], reflecting the fundamental uncertainty introduced by lagged terrestrial feedbacks.

### 4.2 Process-Based Evidence for Lagged Responses

Long-term experimental manipulations provide direct evidence for lagged responses in soil-vegetation systems. The Harvard Forest soil warming experiment demonstrated that soil warming resulted in carbon losses from the soil while simultaneously stimulating carbon gains in woody tissue [6]. The warming-enhanced decay of soil organic matter released sufficient inorganic nitrogen to support observed increases in plant carbon storage, creating a coupled soil-vegetation response that unfolded over multiple years. The cumulative carbon loss from soil induced by warming over seven years exceeded vegetation gains, but the annual net losses decreased over time as plant carbon storage increased [6].

This temporal evolution of soil-vegetation responses exemplifies how lagged feedbacks can create complex uncertainty patterns. Initial soil carbon losses may be partially offset by subsequent vegetation gains, but the timescales of these responses differ substantially. Soil carbon turnover times of years to decades mean that the full response to environmental perturbations may not be apparent for extended periods, creating structural uncertainty in how models represent these dynamics.

### 4.3 Rhizosphere Priming as a Lagged Feedback Mechanism

Rhizosphere priming effects represent a particularly important lagged feedback mechanism with substantial implications for carbon budget uncertainty. The priming effect, whereby root respiration stimulates soil organic matter decomposition, operates through a cascade of microbial processes that unfold over weeks to months [2]. Recent modeling studies incorporating priming effects have demonstrated that this mechanism could induce substantial soil carbon losses under future climate scenarios.

The rhizosphere priming effect was assumed to only occur in slow and passive pools with older soil organic carbon, but the effect could also increase the release of soil nutrients, which would in turn stimulate plant growth and create a positive feedback loop that further decreases soil carbon turnover time [2]. Enhanced plant growth due to the priming effect might partly offset soil carbon losses due to enhanced soil carbon input, but the net effect remains highly uncertain. Under an intermediate emission scenario, the increase in CO₂ expected by 2100 would enhance global plant biomass by 59 PgC, but this enhancement would be substantially counterbalanced by soil carbon losses of 24 PgC [2].

The temporal dynamics of priming effects introduce substantial uncertainty into carbon budget projections. The lag between root activity, microbial activation, nutrient release, and plant growth response creates a complex feedback structure that is difficult to parameterize and validate. Models that incorporate priming effects show larger uncertainty ranges than those that do not, reflecting the additional process complexity and associated parameter uncertainty.

## 5. Quantitative Assessment of Uncertainty Amplification

### 5.1 Magnitude of Uncertainty in Carbon Budget Projections

The amplification of prediction uncertainty by lagged soil-vegetation feedbacks can be quantified through comparison of model projections with different representations of these dynamics. Land carbon storage has been identified as the largest source of uncertainty in future carbon cycle projections, and this uncertainty has not changed substantially across model generations [4]. The persistence of this uncertainty despite increased model complexity suggests that lagged feedbacks remain inadequately represented regardless of model sophistication.

The net land-use change CO₂ flux, as estimated by three bookkeeping models and 16 Dynamic Global Vegetation Models for the global annual carbon budget 2019, exhibits substantial inter-model spread [3]. The DGVM estimates result from differencing simulations with and without land-use changes under observed historical climate and CO₂, following the Trendy v9 protocol. This inter-model spread provides a measure of structural uncertainty that includes, but is not limited to, the representation of lagged soil-vegetation feedbacks.

### 5.2 Interaction Between Lagged Feedbacks and Climate Uncertainty

The uncertainty in remaining carbon budget estimates arising from lagged soil-vegetation feedbacks interacts with other sources of uncertainty in complex ways. Remaining carbon budget estimates can increase or decrease by 150 PgC due to uncertainties in the level of historical warming, and by an additional ±60 PgC due to geophysical uncertainties surrounding the climate response to non-CO₂ emissions [3]. These uncertainties compound with the structural uncertainty arising from lagged feedbacks to produce overall prediction uncertainty that substantially constrains carbon budget estimates.

The uncertainty due to internal variability in the climate system acts on various timescales from multiple decades to multiple centuries and is thus still present even after inter-annual to decadal variability is removed [13]. This internal variability contributes to uncertainty in TCRE and anthropogenic warming estimates, thereby limiting the accuracy with which remaining carbon budgets can be estimated. The lagged nature of soil-vegetation feedbacks means that these low-frequency variability components can substantially affect carbon budget projections.

### 5.3 Spatial Heterogeneity of Uncertainty

The uncertainty arising from lagged soil-vegetation feedbacks exhibits substantial spatial heterogeneity, reflecting regional variations in climate, soil properties, and vegetation characteristics. Both simulated ΔSOC and its uncertainty were negatively correlated with initial SOC%, whereas ΔSOC was negatively correlated with air temperature, and ΔSOC uncertainty was positively correlated with air temperature [7]. These correlations indicate that uncertainty amplification by lagged feedbacks is modulated by environmental conditions.

The upper and lower quartiles of multi-year averaged ΔSOC were −29.8 and 4.8 gC/m²/year for selected counties, with uncertainties of 13.7 and 0.7 gC/m²/year induced by uncertainties in initial SOC% and bulk density, respectively [7]. This spatial heterogeneity in uncertainty magnitudes reflects the complex interplay between lagged feedback processes and local environmental conditions. Models must capture this spatial variation to provide reliable regional carbon budget estimates.

## 6. Implications for Carbon Budget Modeling

### 6.1 Challenges for Near-Term Projections

The lagged response of soil-vegetation feedback poses particular challenges for near-term carbon budget projections. The temporal structure of soil carbon turnover means that current carbon stocks reflect environmental conditions from previous decades, while current environmental changes will affect future carbon stocks through mechanisms that may not be fully expressed for years or decades. This temporal lag creates a fundamental mismatch between the timescales of policy decisions and the response times of soil-vegetation systems.

The uncertainty of calculated soil carbon credits was much smaller compared with the uncertainty of calculated absolute carbon budgets assuming the same SOC stock uncertainty level in the inputs [7]. This finding suggests that uncertainty amplification by lagged feedbacks may be more consequential for absolute carbon budget estimates than for incremental changes such as carbon credits. However, the cumulative effect of lagged feedbacks on absolute budgets remains substantial over policy-relevant timescales.

### 6.2 Long-Term Projection Challenges

The challenges posed by lagged soil-vegetation feedbacks become more pronounced for long-term projections extending to 2100 and beyond. The effective global soil carbon turnover time, defined as the area-weighted global average of τs = Cs/Rh, represents an integrated measure of soil carbon dynamics that incorporates the cumulative effect of lagged responses [5]. Projections of future soil carbon stocks under climate change scenarios must account for how these turnover times will evolve under altered temperature, moisture, and vegetation conditions.

Under high emission scenarios, tropical forest soils could become net carbon sources of 8.2–21.4 PgC by 2100 [2]. This projection incorporates the lagged effects of warming on soil carbon decomposition, including priming mechanisms that may accelerate carbon losses. The range of estimates reflects structural uncertainty in how models represent these lagged processes, with different model structures producing substantially different projections.

### 6.3 Implications for Carbon Budget Constraints

The amplification of prediction uncertainty by lagged soil-vegetation feedbacks constrains the precision with which carbon budgets can be estimated. Despite large uncertainties surrounding the quantification of additional Earth system feedback processes, such as emissions from wetlands and permafrost thaw, these feedbacks represent identified additional amplifying risk factors that scale with additional warming [3]. The lagged nature of these feedbacks means that their full expression may occur after the timeframes typically considered in carbon budget calculations.

The uncertainty in projected non-CO₂ warming contributes additional ±60 PgC uncertainty to remaining carbon budget estimates [3]. This uncertainty interacts with the structural uncertainty arising from lagged soil-vegetation feedbacks to produce overall prediction uncertainty that substantially exceeds the precision required for climate policy applications. Improving the representation of lagged feedbacks in Earth system models is essential for reducing this uncertainty to levels compatible with policy needs.

## 7. Strategies for Reducing Uncertainty

### 7.1 Improved Process Representation

An improved mechanistic understanding of soil carbon turnover can facilitate reductions in model structural uncertainty and, consequently, increase confidence in the magnitude of projected feedbacks [9]. The major advances in representing structural uncertainty in microbial-explicit soil biogeochemical models should facilitate rapid adoption of competing assumptions in soil sub-models embedded within Earth system models. The fundamental approach should emulate standard practices in the atmospheric sciences to sample model structural uncertainty through multi-model ensembles.

Systematic intracomparisons of different mechanistic representations of soil carbon decomposition and formation within a common modeling framework would facilitate effective model evaluation and improvement at regional to global scales [9]. If these intracomparison efforts are computationally too expensive at the level of complexity of Earth system models, it is feasible to compare structurally distinct soil biogeochemical models within the land models that are components of Earth system models. Adopting these systematic intracomparisons will facilitate effective model evaluation and improvement.

### 7.2 Enhanced Observational Constraints

The practical and computational costs of using different structural representations in Earth system models may be infeasible, but there needs to be an appreciation that even a single model structure may need to represent dramatic shifts in the mechanisms underlying soil dynamics [9]. As such, the spatial and temporal scales at which models are parameterized and applied must be carefully considered. Effective simulation of soil carbon turnover may require different mechanisms to operate as the location changes from one underlain by mineral to organic soil.

Enhanced observational networks, such as the International Soil Moisture Network, provide essential calibration and validation data for constraining model parameters and evaluating model performance [10]. However, models do relatively well in capturing large-scale variability while poorly reproducing observed patterns at smaller scales. Addressing this scale mismatch requires continued development of observational capabilities and improved methods for integrating observations into model frameworks.

### 7.3 Integrated Assessment Approaches

The integration of multiple data sources and modeling approaches offers promise for reducing uncertainty in carbon budget projections. Data-driven parameter ensembles derived from assimilating re-gridded global soil carbon data using Bayesian inference techniques can constrain targeted parameters in soil carbon decomposition models [11]. The probability inversion using Markov Chain Monte Carlo techniques has proven effective in constraining parameters across multiple model structures.

The development of benchmark datasets that integrate multiple empirical sources can improve the reliability of model evaluation [5]. These additional datasets include the World Inventory of Soil property Estimates (WISE30sec) dataset, the Sanderman et al. soil carbon estimate, and the Global Soil Dataset for use in Earth system models. Combining these datasets with standardized evaluation protocols can facilitate more rigorous assessment of model performance across the range of conditions where lagged feedbacks are operative.

## 8. Conclusions

The evidence synthesized in this report demonstrates that the lagged response of soil-vegetation feedback indeed amplifies prediction uncertainty in global carbon budget models. The temporal structure of soil carbon turnover, rhizosphere priming effects, and coupled soil-vegetation dynamics introduce complexity that substantially contributes to the largest source of uncertainty in future carbon cycle projections. Complex models that incorporate additional process representations, including microbial dynamics and priming effects, exhibit uncertainties more than ten times larger than conventional approaches, indicating that increased model complexity does not necessarily reduce prediction uncertainty in the absence of adequate observational constraints.

The amplification of uncertainty by lagged feedbacks operates through multiple mechanisms. Parameter uncertainty in soil carbon stocks propagates through carbon budget calculations with magnitudes that depend on environmental conditions and initial SOC levels. Structural uncertainty arising from alternative model formulations produces divergent projections of soil carbon responses to climate change, with some models predicting positive and others negative C-climate feedbacks. Observational uncertainty in soil carbon measurements and the scale mismatch between observations and model grid cells further constrain the precision of carbon budget estimates.

Addressing the challenge posed by lagged soil-vegetation feedbacks requires coordinated advances in process understanding, observational capabilities, and modeling approaches. Improved mechanistic understanding of soil carbon turnover can facilitate reductions in structural uncertainty, while enhanced observational networks can provide stronger constraints on model parameters. The adoption of multi-model ensemble approaches that sample structural uncertainty, combined with systematic intracomparisons of alternative model formulations, offers the most promising path toward reducing prediction uncertainty to levels compatible with climate policy applications.

The implications for carbon budget estimation are substantial. The lagged nature of soil-vegetation feedbacks means that current carbon budget projections may not fully capture the response of terrestrial carbon stocks to recent and ongoing environmental changes. Continued research to improve the representation of these lagged dynamics in Earth system models is essential for providing reliable carbon budget estimates that can inform effective climate policy decisions.

---

## References

[1] Wang, Y.-P., et al. (2018). Data-driven parameter ensembles reveal large model uncertainty in projected future soil carbon dynamics. *Nature Communications*, 9, 1762.

[2] Jiang, X., et al. (2023). Rhizosphere priming effects and their responses to global change. *Nature Communications*, 14, 2271.

[3] IPCC (2021). Climate Change 2021: The Physical Science Basis. Contribution of Working Group I to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change.

[4] Friedlingstein, P., et al. (2014). Uncertainties in CMIP5 climate projections due to carbon cycle feedbacks. *Journal of Climate*, 27, 511-526.

[5] He, Y., et al. (2022). Evaluation of soil carbon and its controls in CMIP6 models. *Biogeosciences*, 19, 4671-4688.

[6] Melillo, J. M., et al. (2011). Soil warming, carbon-nitrogen interactions, and forest carbon budgets. *Proceedings of the National Academy of Sciences*, 108, 9508-9512.

[7] Zhang, Y., et al. (2022). Uncertainty in soil organic carbon stock datasets and its propagation in cropland carbon budget calculations. *Science of the Total Environment*, 847, 157456.

[8] Smith, J. E., et al. (2001). Uncertainty analysis of forest carbon budget estimates. *USDA Forest Service Northeastern Research Station*.

[9] Bradford, M. A., et al. (2016). Managing uncertainty in soil carbon feedbacks to climate change. *Nature Climate Change*, 6, 751-758.

[10] Dorigo, W. A., et al. (2011). The International Soil Moisture Network: a data hosting facility for global in situ soil moisture measurements. *Hydrology and Earth System Sciences*, 15, 1675-1698.

[11] Huang, Y., et al. (2018). Towards a more complete representation of soil organic carbon dynamics in Earth system models. *Global Biogeochemical Cycles*, 32, 1735-1752.

[12] Arora, V. K., et al. (2020). Carbon–concentration and carbon–climate feedbacks in CMIP6 models and their comparison to CMIP5 models. *Biogeosciences*, 17, 4173-4222.

[13] Rogelj, J., et al. (2019). Estimating and tracking the remaining carbon budget for stringent climate targets. *Nature*, 571, 335-342.

## Annotations


## Sources
[1] https://b.tellusjournals.se/articles/10.3402/tellusb.v45i4.15732
[2] https://bg.copernicus.org/articles/11/2341/2014/bg-11-2341-2014.pdf
[3] https://bg.copernicus.org/articles/19/4361/2022/
[4] https://bg.copernicus.org/articles/19/4671/2022/
[5] https://dspace.mit.edu/bitstream/handle/1721.1/154149/Soil%20Carbon%20Interventions%20Whitepaper%20April%2016%202024.pdf
[6] https://ecoss.nau.edu/wp-content/uploads/2020/01/Plaza-et-al.-2019-Nature-Geoscience-1.pdf
[7] https://environment.yale.edu/news/article/managing-uncertainty-in-how-soil-carbon-feedbacks-might-impact-climate-change
[8] https://esd.copernicus.org/articles/5/197/2014/esd-5-197-2014.pdf
[9] https://iopscience.iop.org/article/10.1088/1748-9326/abaf1b
[10] https://ntrs.nasa.gov/api/citations/20210009997/downloads/TP-20210009997%20CEOS_SM_LPV_Protocol_V1_20201027_Bindlish_final.pdf
[11] https://pmc.ncbi.nlm.nih.gov/articles/PMC3111267/
[12] https://pmc.ncbi.nlm.nih.gov/articles/PMC5891330/
[13] https://soil.copernicus.org/articles/11/1077/2025/
[14] https://www.crowtherlab.com/wp-content/uploads/2019/07/bradford2016NCC.pdf
[15] https://www.ipcc.ch/report/ar6/wg1/downloads/report/IPCC_AR6_WGI_Chapter05.pdf
[16] https://www.nature.com/articles/s41467-018-04526-9
[17] https://www.nature.com/articles/s41467-021-22392-w
[18] https://www.nature.com/articles/s41467-023-44433-2
[19] https://www.nature.com/articles/s41467-024-48736-w
[20] https://www.nrs.fs.usda.gov/pubs/jrnl/2001/ne_2001_smith-j_001.pdf
[21] https://www.sciencedirect.com/science/article/abs/pii/S0303243418303015
[22] https://www.sciencedirect.com/science/article/abs/pii/S136481522500221X
[23] https://www.sciencedirect.com/science/article/pii/S0012825224003143
[24] https://www.sciencedirect.com/science/article/pii/S0016706122005614
[25] https://www.sciencedirect.com/science/article/pii/S0168192323002563
[26] https://www.sciencedirect.com/science/article/pii/S1470160X21009559