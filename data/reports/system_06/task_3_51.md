# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** ec1d3e92 | **Time:** 237.34s | **Cost:** $0.17263
--------------------------------------------------------------------------------

# Does Error Propagation in Cloud Microphysics Parameterization Limit Regional Climate Prediction Resolution?

## A Technical Analysis Report

---

## Executive Summary

Cloud microphysics parameterization represents one of the most significant sources of uncertainty in contemporary climate modeling systems. As regional climate models push toward higher spatial resolutions, the question of whether error propagation in microphysical parameterizations fundamentally limits prediction accuracy has become increasingly critical. This report synthesizes current understanding of error propagation mechanisms in cloud microphysics schemes and evaluates their implications for regional climate prediction at various spatial resolutions.

The evidence presented herein demonstrates that error propagation in cloud microphysics parameterization does indeed impose substantial constraints on regional climate prediction resolution. Unlike other model components where increased resolution can reduce uncertainty, microphysical parameterizations face inherent limitations stemming from incomplete physical understanding, numerical errors in process formulations, and the complex multi-scale nature of cloud processes. The analysis reveals that microphysics-related uncertainties may already constitute, or will soon constitute, the dominant source of prediction uncertainty even as other aspects of climate models steadily improve. This finding carries profound implications for the future development of regional climate prediction systems and highlights the urgent need for targeted research investments in cloud physics knowledge, observational capabilities, and novel parameterization approaches including physics-informed machine learning techniques.

---

## 1. Introduction

### 1.1 The Central Role of Cloud Microphysics in Climate Modeling

Atmospheric processes span an extraordinary range of spatial and temporal scales, from approximately $10^{-2}$ to $10^8$ meters and $10^{-1}$ to $10^8$ seconds [1]. Global and regional climate models cannot resolve these physical processes across all scales by construction. Unresolved processes are therefore represented through physical parameterization schemes that apply various assumptions and approximations to simplify complex phenomena. Among these parameterizations, cloud microphysics holds particular importance due to its direct influence on the hydrological cycle, radiative transfer, and atmospheric energy balance.

Cloud microphysics parameterizations calculate the formation, growth, and removal of liquid and solid water particles while capturing phase changes that significantly influence cloud lifetime, reflectivity, and precipitation efficiency [2]. The accurate representation of these processes is crucial for reliable climate projections, as microphysical uncertainties can propagate through model simulations to affect large-scale circulation patterns, precipitation distributions, and temperature projections. The sensitivity of simulated weather and climate to microphysics representation has grown so substantial that, given limited direct observational guidance and the absence of a benchmark model, microphysics representation has arguably become an impediment to reducing overall model uncertainty [3].

### 1.2 The Resolution Challenge in Regional Climate Prediction

Regional climate models have progressively increased their spatial resolution over recent decades, with contemporary systems routinely operating at grid spacings of 10-50 km and convection-permitting simulations approaching kilometer-scale resolution. This trend toward higher resolution reflects the expectation that finer grids will better resolve mesoscale phenomena, topographic effects, and precipitation patterns that are critical for regional climate assessments. However, this pursuit of higher resolution encounters a fundamental challenge when it comes to cloud microphysics parameterization.

Unlike convective parameterizations, which can potentially be eliminated or substantially simplified at convection-permitting resolutions, cloud microphysical parameterizations remain essential regardless of model resolution [4]. Even at kilometer-scale resolution, individual cloud-scale processes involving cloud droplet formation, collision-coalescence, ice crystal growth, and precipitation particle interactions occur at scales far below the model grid. Consequently, the parameterization of these processes—and the errors inherent in such parameterizations—persists as a source of uncertainty that cannot be simply "resolved away" through grid refinement.

### 1.3 Scope and Objectives of This Report

This report examines the mechanisms through which errors propagate through cloud microphysics parameterizations and evaluates whether this propagation fundamentally limits the effective resolution of regional climate predictions. The analysis synthesizes evidence from multiple sources including numerical error correction studies, machine learning parameterization development, sensitivity experiments with different microphysics schemes, and assessments of uncertainty contributions in regional climate simulations. The ultimate objective is to provide a comprehensive technical assessment that informs research priorities and investment decisions in climate modeling.

---

## 2. Understanding Error Propagation in Cloud Microphysics Parameterizations

### 2.1 Sources of Uncertainty in Microphysical Process Representations

Cloud microphysics schemes face two fundamental challenges that generate substantial uncertainty in model predictions. The first challenge concerns how to represent the population of cloud and precipitation particles given the impossibility of simulating all particles individually even within a small cloud [3]. Bulk-type parameterizations predict moments of hydrometeor size distributions, typically using assumptions about particle size distributions and mass-dimensional relationships that introduce systematic biases. The second challenge involves uncertainties in microphysical process rates owing to critical gaps in cloud physics knowledge, particularly regarding ice-phase processes.

These uncertainties are especially pronounced for ice-phase processes including vapor diffusional growth, melting, and aggregation (the sticking and collection of ice particles) [3]. The complicated and intricate shapes of atmospheric ice particles introduce enormous complexity into process rate calculations. Laboratory experimentation provides a critical means to quantify individual microphysical process rates in controlled settings, yet there has been an apparent decline in laboratory work over recent decades relative to other research areas in cloud physics. This gap in fundamental process understanding directly translates into parameterization uncertainty that propagates through climate simulations.

### 2.2 Mechanisms of Error Propagation

Error propagation in cloud microphysics parameterizations operates through multiple interconnected mechanisms. Direct error propagation occurs when uncertainties in microphysical process rates directly affect predicted hydrometeor distributions, which then influence radiative transfer calculations, latent heating profiles, and surface precipitation. The cascading nature of cloud processes means that errors in one parameterization component can amplify through feedback mechanisms.

Consider the example of ice cloud parameterization. Errors in the relationship between cloud-ice mixing ratio and number concentration can significantly affect the simulated cloud ice content, which in turn influences the radiative properties of ice clouds and the latent heat release associated with ice-phase processes [5]. Research has demonstrated that numerical errors intrinsic to the description of cloud-ice characteristics in microphysics schemes such as the WDM6 scheme can produce regional climate impacts comparable to those from changes in fundamental cloud-ice shape assumptions [5]. This finding illustrates how seemingly technical numerical errors can propagate to affect large-scale circulation patterns such as the Western North Pacific High in regional monsoon simulations.

The buffered behavior of the climate system sometimes moderates the direct translation of microphysical errors into large-scale forecast errors [4]. However, this buffering is neither complete nor reliable across all situations. For regional climate predictions focusing on specific metrics such as surface precipitation distribution and variability, microphysics-related uncertainties can dominate the error budget, particularly for phenomena involving deep convection, frontal systems, and orographic precipitation.

### 2.3 Scale Dependence of Error Propagation

The propagation of microphysical errors exhibits complex scale dependence that challenges simple generalizations about resolution effects. At coarse resolutions where convective parameterizations are active, microphysical errors interact with convective parameterization errors in ways that can either amplify or dampen total prediction uncertainty. At convection-permitting resolutions where explicit grid-scale precipitation is predicted, microphysical errors become more directly coupled to resolved dynamics but may also interact more strongly with planetary boundary layer and turbulence parameterizations.

High-resolution regional climate simulations have demonstrated substantial sensitivity to cloud microphysics scheme selection. Studies examining wintertime precipitation in mountainous regions found that different bulk microphysics parameterizations produced widely varying snowfall predictions even when all other model components were held constant [6]. The sensitivity extended to interactions with planetary boundary layer schemes, land surface schemes, and radiative transfer schemes, indicating that microphysical errors propagate through multiple pathways to affect regional climate predictions.

---

## 3. Resolution Limitations and the Persistence of Microphysical Uncertainty

### 3.1 The Fundamental Limitation of Grid Refinement

A critical distinction exists between parameterizations that can be progressively simplified or eliminated through increased model resolution and those that cannot. Convective parameterizations represent the former category—at convection-permitting resolutions of approximately 4 km or finer, the explicit simulation of deep convection becomes feasible and convective parameterizations can be modified or removed. Cloud microphysics parameterizations represent the latter category [4].

Even at kilometer-scale resolution, the characteristic scales of key microphysical processes remain subgrid. Cloud droplet activation occurs at scales of micrometers to millimeters. Collision and coalescence processes involve interactions between individual particles. Ice crystal nucleation depends on aerosol distributions and supersaturation fluctuations at scales far below the model grid. Consequently, microphysics parameterizations remain necessary regardless of how finely the model grid is refined, and the uncertainties inherent in these parameterizations persist as a source of prediction error.

This fundamental limitation has profound implications for the pursuit of higher resolution in regional climate prediction. While increased resolution can improve the representation of dynamical processes and large-scale flow features, it cannot eliminate microphysical uncertainty. In fact, as other sources of uncertainty are progressively reduced through improved parameterizations, increased resolution, and better initial conditions, microphysical uncertainty may become relatively more dominant in the prediction error budget.

### 3.2 Implications for Regional Climate Prediction Resolution

The persistence of microphysical uncertainty at all model resolutions suggests that there may be practical limits to the useful resolution of regional climate predictions. These limits are determined not by computational capabilities but by the fundamental uncertainty in representing microphysical processes. If microphysical errors propagate to affect regional climate metrics at the scales of interest, then simply increasing grid resolution without addressing microphysical uncertainty may yield diminishing returns.

Evidence from regional climate modeling studies supports this perspective. Research examining high-resolution sensitivity studies over the Alpine region found that while increased resolution improved some aspects of precipitation simulation, systematic biases related to microphysical process representation remained significant across resolutions [1]. The error characteristics of high-resolution regional climate models showed persistent biases that could not be attributed solely to large-scale driving data or dynamical downscaling errors, suggesting substantial contributions from physics parameterizations including microphysics.

For predictions of the next decade, internal variability accounts for 40-60% of total prediction uncertainty in most regions [7]. While reducing internal variability through improved initialization can contribute to uncertainty reduction, model uncertainty—including microphysical uncertainty—remains a dominant contribution for predictions of the fourth decade ahead over almost all regions. This pattern suggests that investments in reducing microphysical uncertainty may yield substantial benefits for long-term regional climate predictions, potentially more so than continued resolution increases alone.

### 3.3 The Utility of High-Resolution Simulations for Parameterization Development

The persistence of microphysical uncertainty also affects the utility of high-resolution simulations for developing parameterizations intended for coarser resolution models. Large eddy simulations (LES) and convection-permitting models can resolve some aspects of cloud and precipitation processes that are parameterized in climate models. However, the translation of insights from these high-resolution simulations to improved coarser-resolution parameterizations is complicated by the fundamental differences in scale and dynamics between the simulation and target application.

High-resolution simulations that resolve vertical motion and mixing more accurately can provide valuable training data for machine learning parameterizations that emulate the effects of unresolved dynamics on microphysics [2]. However, the differences in scale, boundary conditions, and dynamics between high-resolution simulations and climate model applications can complicate this translation. The challenge lies not only in capturing the statistical relationships between resolved variables and microphysical tendencies but also in ensuring that these relationships remain valid across the range of conditions encountered in climate simulations.

---

## 4. Numerical Errors in Microphysics Schemes

### 4.1 Origins and Characteristics of Numerical Errors

Beyond the fundamental uncertainties in physical process representations, cloud microphysics parameterizations are subject to numerical errors arising from the discretization of continuous equations and the approximations inherent in computational implementations. These numerical errors can be subtle and may not be immediately apparent from inspection of the code or standard testing procedures.

Research examining the WDM6 microphysics scheme identified numerical errors originating from the diagnosed ice number concentration, which is a function of the cloud-ice mixing ratio [5]. The cloud-ice shape assumption of single bullets introduced systematic biases into the relationships between cloud microphysics characteristics. By rederiving these relationships, researchers were able to remove numerical errors intrinsic to the description of cloud-ice characteristics in the original scheme. The corrections led to significant improvements in regional climate simulations, including better capture of monsoon rain band distributions and more realistic representations of large-scale circulation features.

The impacts of these numerical errors on simulated regional climate were substantial. The correction to WDM6 produced a significant reduction in cloud ice, which in turn strengthened the Western North Pacific High [5]. Sensitivity experiments revealed that the impacts of existing numerical errors on simulated monsoon circulation were comparable in magnitude to the impacts of changes in fundamental cloud-ice shape assumptions. This finding demonstrates that numerical errors in microphysics schemes can propagate to affect climate-scale phenomena with magnitudes similar to those from physical uncertainty.

### 4.2 Error Propagation Through Process Interactions

Numerical errors in microphysics schemes propagate through the complex network of process interactions that characterize cloud-climate feedbacks. Cloud microphysics processes are tightly coupled through mass and number conservation equations, phase change rates, and radiative transfer calculations. An error in one process equation can cascade through the system to affect multiple output variables and feedback pathways.

The equations for cloud microphysics processes affected by numerical errors involve complex interactions between cloud water, rain, cloud ice, snow, and graupel species [5]. Changes to the characteristic diameter relationships for one hydrometeor type affect collection rates, conversion rates, and sedimentation velocities throughout the scheme. These changes then influence the vertical distribution of hydrometeors, which affects radiative heating profiles and latent heating rates, ultimately impacting large-scale dynamics and circulation patterns.

The propagation of numerical errors through these pathways means that identifying and correcting such errors requires comprehensive understanding of the entire microphysics scheme and its interactions with other model components. Simple fixes to individual process equations may introduce new errors or disrupt carefully tuned balances within the scheme. This complexity contributes to the challenge of improving microphysics parameterizations and suggests that systematic approaches to error identification and correction are needed.

### 4.3 Implications for Regional Climate Model Accuracy

The demonstration that numerical errors in microphysics schemes can produce regional climate impacts of substantial magnitude has important implications for regional climate modeling. If errors of this magnitude exist in widely used microphysics schemes, then regional climate simulations may be systematically biased in ways that cannot be attributed to large-scale forcing errors or initial condition uncertainties.

The correction of numerical errors in the WDM6 scheme improved the model's performance in capturing the observed distribution of the monsoon rain band [5]. This improvement demonstrates that addressing numerical errors in microphysics schemes can yield tangible benefits for regional climate prediction skill. However, the identification of such errors requires careful analysis and often depends on access to high-resolution observational data for validation. The lack of direct observational guidance for many microphysical quantities complicates the identification and quantification of numerical errors.

---

## 5. Machine Learning Approaches to Mitigate Error Propagation

### 5.1 Physics-Informed Machine Learning for Microphysics Parameterization

The development of machine learning-based parameterizations for cloud microphysics represents a promising approach to reducing error propagation in climate models. These approaches leverage high-resolution simulation data to learn relationships between resolved variables and microphysical tendencies that can be applied in coarser-resolution climate models. The goal is to capture the effects of unresolved dynamics on microphysical processes in ways that traditional parameterizations may not achieve.

Research has developed a cloud microphysics parameterization for the ICON model based on physics-informed machine learning [2]. By training the ML model on high-resolution simulation data generated with a one-moment cloud microphysics scheme including a complex graupel scheme, the approach enhances the representation of cloud microphysics in Earth system models compared to traditional parameterization schemes. The ML approach specifically considers the influence of high-resolution dynamics that are not resolved in coarse Earth system models, enabling the parameterization to capture some of these effects even when applied to coarse-scale models.

The ML approach combines a microphysics trigger classifier and a regression model [2]. The trigger classifier identifies grid cells where changes due to microphysical processes are significant, while the regression model predicts the magnitude of these changes based on high-resolution simulation data. This architecture allows the parameterization to adapt to local conditions rather than applying uniform process rates across the model domain.

### 5.2 Learning from High-Resolution Simulations

A key advantage of machine learning approaches is their ability to learn complex, nonlinear relationships from high-resolution simulation data that may be difficult to parameterize using traditional approaches. High-resolution simulations that resolve cloud-scale dynamics can provide training data that captures the statistical relationships between resolved variables and microphysical tendencies under a wide range of conditions.

The approach of learning from more detailed microphysics parameterizations using superdroplet box models offers another avenue for improvement [2]. These methods aim to enhance the representation of cloud microphysics and reduce biases in coarse-resolution Earth system models through detailed high-resolution simulations. However, switching from superdroplet box models to global climate simulations introduces challenges related to scale differences, boundary conditions, and dynamics between box models and Earth system models.

The computational requirements of ML-based parameterizations differ significantly from classical parameterizations typically used in Earth system models [2]. This adds technical complexity when implementing such models, particularly for operational systems where computational efficiency is paramount. The Fortran-Python bridges required to couple ML parameterizations to climate models written in Fortran pose significant technical challenges, including potential instabilities in simulation runs and the need for model retuning.

### 5.3 Potential Benefits and Limitations

Machine learning-based microphysics parameterizations offer the potential to enhance climate model accuracy by better representing the influence of highly resolved dynamics on cloud microphysical processes [2]. More accurate and robust climate projections are essential for informed decision-making and risk assessment in addressing the global warming crisis. The ML approach bridges a gap by indirectly learning the effects of unresolved dynamics on microphysics from high-resolution simulations, enabling the parameterization to capture some of these effects even when applied to coarse-scale models.

However, significant challenges remain. The ML-based microphysics parameterization has not yet been coupled to ICON in a full Earth system model implementation [2]. Implementing it in a global climate model will be crucial for fully assessing potential benefits and impacts on climate projections. This step poses significant technical challenges that are the subject of ongoing effort. Furthermore, the generalizability of ML parameterizations trained on limited simulation data to conditions outside the training distribution remains an open question.

Future improvements could focus on utilizing even higher-resolution data, such as those from large eddy simulations, which resolve vertical motion and mixing even more accurately [2]. Such advancements could further reduce biases and enhance the physical accuracy of ML-based parameterizations for cloud microphysics. However, the fundamental uncertainties in cloud physics knowledge that affect traditional parameterizations will also affect ML approaches trained on simulation data that incorporates these uncertainties.

---

## 6. Implications for Regional Climate Prediction

### 6.1 Dominant Source of Uncertainty

For modeling that involves clouds or precipitation, microphysics is, or will soon become, a dominant source of uncertainty even as other aspects are steadily improved, such as increasing model resolution [3]. This conclusion has profound implications for regional climate prediction. As dynamical core improvements, increased resolution, and better initial condition specification progressively reduce other sources of uncertainty, microphysical uncertainty will become relatively more important in the prediction error budget.

The recognition that microphysics uncertainty may limit prediction skill even at high resolutions challenges the paradigm of pursuing ever-finer model grids as the primary strategy for improving regional climate predictions. While resolution increases remain valuable for resolving dynamical processes and topographic effects, they cannot address the fundamental uncertainty in representing cloud microphysical processes. A more balanced approach that invests in reducing microphysical uncertainty alongside resolution increases may yield greater overall improvements in prediction skill.

### 6.2 Limits to Uncertainty Reduction

An important question concerns whether there are fundamental limits to the potential for narrowing uncertainty in regional climate predictions. The evidence suggests that such limits may exist but that there is currently no evidence that these limits have been reached [7]. The potential to narrow uncertainty is real, and the need is urgent given the importance of climate projections for societal decision-making.

However, acknowledging that progress in climate science may sometimes broaden rather than narrow uncertainty—as occurred with improved understanding of carbon cycle feedbacks—is not a reason to avoid focused attention on the requirement and opportunities to narrow uncertainty [7]. Indeed, this requirement should be a major focus of climate science because of its importance to society. The identification of microphysics as a dominant source of uncertainty provides a clear target for research investments that could yield substantial benefits for prediction skill.

### 6.3 Research Priorities

To continue advancing models into the future will require confronting the microphysics uncertainty problem head on [3]. This confrontation must proceed along multiple fronts. Increased support for laboratory work is needed to address major gaps in cloud physics knowledge and to provide data for developing physically based parameterizations. Laboratory experimentation provides a direct way to quantify individual microphysical process rates in controlled settings and represents a critical part of advancing cloud physics knowledge.

Sustained support for new airborne and ground-based instrument development and next-generation instruments in space is also essential [3]. Field data are needed to evaluate and constrain microphysics schemes in regional and global models. The lack of direct observational guidance for many microphysical quantities represents a fundamental limitation that can only be addressed through improved observational capabilities.

The development of novel parameterization approaches, including physics-informed machine learning techniques, represents another important research priority. These approaches offer the potential to better represent the effects of unresolved dynamics on microphysical processes and to reduce error propagation in climate models. However, substantial technical challenges remain in implementing these approaches in operational climate models and in ensuring their robustness across the range of conditions encountered in climate simulations.

---

## 7. Challenges and Future Directions

### 7.1 Bridging Scale Gaps

A fundamental challenge in cloud microphysics parameterization concerns the enormous gap between the scales of individual microphysical processes and the scales resolved by climate models. Cloud droplets form and grow through processes occurring at micrometer scales over timescales of seconds to minutes. These processes must be represented in climate models operating at grid spacings of kilometers to hundreds of kilometers and time steps of minutes to hours. The statistical representation of microphysical processes across these scale gaps introduces inherent uncertainties that cannot be eliminated through model refinement alone.

The scale gap also affects the translation of insights from process studies to improved parameterizations. Large eddy simulations and convection-permitting models can resolve some cloud-scale dynamics but cannot fully capture the spectrum of scales involved in cloud microphysical processes. The differences in scale, boundary conditions, and dynamics between these high-resolution simulations and climate model applications complicate the development of improved parameterizations.

### 7.2 Computational Constraints

Cloud microphysics parameterizations must balance physical realism against computational cost. Schemes in operational models are strongly constrained by their computational budget [3]. Greater flexibility in representing cloud microphysics using detailed bulk schemes has to be balanced by the increased computational cost. As computing power has increased dramatically over time, schemes in operational weather and climate models have progressively incorporated more complexity, including explicit prognostic treatment of multiple hydrometeor species.

However, computational constraints remain significant, particularly for climate simulations that must span decades to centuries of simulated time. The development of efficient parameterizations that capture essential physics while remaining computationally tractable represents an ongoing challenge. Machine learning approaches offer potential computational advantages once trained, but the training process itself requires substantial computational resources, and the inference process must be sufficiently efficient for operational use.

### 7.3 Physical Understanding Gaps

Despite decades of research, important gaps remain in the physical understanding of many cloud processes and their interactions that influence weather and climate [3]. Some processes are known or suspected to be important in clouds but are currently neglected or treated very crudely in parameterizations. This has motivated increases in complexity and sophistication in process models, but observations are often inadequate to provide the details necessary to characterize these processes quantitatively.

The ice phase presents particular challenges due to the complicated and intricate shapes of atmospheric ice particles [3]. Uncertainties in ice-phase processes including vapor diffusional growth, melting, and aggregation remain large. These uncertainties propagate through cloud-climate feedbacks to affect large-scale climate predictions. Addressing these understanding gaps requires sustained investment in fundamental cloud physics research, including laboratory studies, field observations, and theoretical development.

---

## 8. Conclusions

The analysis presented in this report demonstrates that error propagation in cloud microphysics parameterization does indeed limit regional climate prediction resolution in meaningful and significant ways. Unlike other model components where increased resolution can reduce uncertainty, microphysical parameterizations face inherent limitations that cannot be overcome through grid refinement alone. The fundamental challenges include incomplete physical understanding of cloud processes, numerical errors in process formulations, and the persistent scale gap between microphysical processes and climate model grids.

The evidence indicates that microphysics is, or will soon become, a dominant source of uncertainty in regional climate predictions involving clouds or precipitation. This dominance persists even as other aspects of climate models steadily improve through increased resolution, better initial conditions, and improved parameterizations of other physical processes. The recognition of microphysics as a limiting factor for prediction skill has important implications for research priorities and resource allocation in climate science.

Addressing the microphysics uncertainty challenge requires a multi-faceted approach. Fundamental research to fill gaps in cloud physics knowledge remains essential, including laboratory studies of microphysical process rates and field observations to constrain parameterizations. The development of novel parameterization approaches, including physics-informed machine learning techniques, offers promise for better representing the effects of unresolved dynamics on microphysical processes. However, substantial technical challenges remain in implementing these approaches in operational climate models.

The path forward requires acknowledging that continued advances in regional climate prediction will depend not only on increasing model resolution but also on reducing the fundamental uncertainty in cloud microphysics representation. Investments in cloud physics research, observational capabilities, and innovative parameterization approaches should be prioritized alongside resolution increases. Only through comprehensive attention to the microphysics challenge can regional climate prediction achieve its full potential for informing societal adaptation to climate change.

---

## References

[1] Suklitsch, M., Gobiet, A., Truhetz, H., Awan, N. K., Göttel, H., and Jacob, D. (2010). Error characteristics of high resolution regional climate models over the Alpine area. Climate Dynamics.

[2] Physics-Informed Machine Learning Parameterization for Cloud Microphysics in ICON. Environmental Data Science, Cambridge University Press.

[3] Morrison, H., et al. (2024). Challenges and opportunities for advancing cloud microphysics parameterization. OpenSky University of Colorado.

[4] Seifert, A. (2011). Uncertainty and complexity in cloud microphysics. European Centre for Medium-Range Weather Forecasts.

[5] Hong, S., et al. (2009). Numerical errors in cloud ice microphysics of WDM6 scheme. Regional climate simulation study using WRF over East Asian region.

[6] Liu, C., Ikeda, K., Thompson, G., Rasmussen, R., and Dudhia, J. (2011). High-resolution simulations of wintertime precipitation in the Colorado Headwaters region: Sensitivity to physics parameterizations. National Center for Atmospheric Research.

[7] Hawkins, E. and Sutton, R. (2009). The potential to narrow uncertainty in regional climate predictions. Bulletin of the American Meteorological Society.

## Annotations


## Sources
[1] https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2025MS005341
[2] https://archive.ipcc.ch/pdf/supporting-material/gcos-117.pdf
[3] https://egusphere.copernicus.org/preprints/2025/egusphere-2025-4401/egusphere-2025-4401.pdf
[4] https://egusphere.copernicus.org/preprints/2025/egusphere-2025-5803/egusphere-2025-5803.pdf
[5] https://elib.dlr.de/216101/1/a-physics-informed-machine-learning-parameterization-for-cloud-microphysics-in-icon.pdf
[6] https://journals.ametsoc.org/view/journals/clim/24/12/2011jcli3674.1.xml
[7] https://journals.ametsoc.org/view/journals/mwre/150/11/MWR-D-22-0057.1.xml
[8] https://opensky.ucar.edu/system/files/2024-08/26186.pdf
[9] https://opensky.ucar.edu/system/files/2024-08/articles_12090.pdf
[10] https://opensky.ucar.edu/system/files/2024-08/articles_23626.pdf
[11] https://opensky.ucar.edu/system/files/2024-08/articles_26571.pdf
[12] https://paos.colorado.edu/~whan/ATOC4800_5000/Spring_2017/Materials/Hawkins_sutton.pdf
[13] https://pmc.ncbi.nlm.nih.gov/articles/PMC7507216/
[14] https://science.osti.gov/-/media/ber/pdf/community-resources/2023/Atmospheric_System_Research_LES_Workshop_Report_Sept23.pdf
[15] https://tellusjournal.org/articles/10.3402/tellusa.v67.26678
[16] https://www.atmos.washington.edu/MG/PDFs/JAMES18_Feng-etal_StructEvolMCS.pdf
[17] https://www.cambridge.org/core/journals/environmental-data-science/article/physicsinformed-machine-learning-parameterization-for-cloud-microphysics-in-icon/9EEF4A2B900F09D65475E62A3390C177
[18] https://www.ecmwf.int/sites/default/files/elibrary/2011/12166-uncertainty-and-complexity-cloud-microphysics.pdf
[19] https://www.osti.gov/pages/biblio/1959539
[20] https://www.osti.gov/pages/servlets/purl/1959539
[21] https://www.osti.gov/servlets/purl/1959539
[22] https://www2.mmm.ucar.edu/wrf/users/physics/phys_refs/CU_PHYS/Multiscale_KF.pdf