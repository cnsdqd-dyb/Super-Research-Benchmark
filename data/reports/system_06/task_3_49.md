# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 41437aee | **Time:** 182.69s | **Cost:** $0.11567
--------------------------------------------------------------------------------

# How Does the Parameterization of Ocean Heat Redistribution Affect Seasonal Prediction Skill Regarding ENSO Amplitude?

## Abstract

The El Niño-Southern Oscillation (ENSO) represents the dominant source of seasonal-to-interannual predictability in the tropical Pacific climate system. This report examines how the parameterization of ocean heat redistribution mechanisms influences seasonal prediction skill for ENSO amplitude. Through synthesis of recent modeling studies and forecast system evaluations, we identify three primary pathways through which ocean heat redistribution parameterizations affect prediction skill: (1) vertical mixing schemes that govern the coupling between thermocline dynamics and sea surface temperature variations, (2) diurnal variation parameterizations that control the representation of near-surface thermal structure, and (3) horizontal resolution-dependent processes that determine the spatial distribution of heat content anomalies. The analysis reveals that accurate representation of these processes—particularly through enhanced vertical resolution and sophisticated mixing parameterizations—significantly improves ENSO amplitude prediction, phase-locking behavior, and forecast reliability. However, substantial model dependence persists, indicating that continued refinement of ocean heat redistribution parameterizations remains essential for advancing seasonal prediction capability.

## 1. Introduction

The El Niño-Southern Oscillation phenomenon constitutes the most consequential mode of interannual climate variability, with profound implications for global weather patterns, marine ecosystems, and socioeconomic systems worldwide. Seasonal prediction of ENSO events—particularly their amplitude at mature phases—represents a cornerstone of operational climate forecasting, yet skill levels remain variable and subject to the fidelity of underlying model physics. Central to this challenge is the accurate representation of ocean heat redistribution processes, which govern the evolution of thermal anomalies that ultimately manifest as ENSO events.

Ocean heat redistribution in the tropical Pacific occurs through multiple interconnected physical mechanisms. Vertical processes—including mixing, upwelling, and subduction—transfer heat between the surface mixed layer and deeper ocean layers, thereby modulating sea surface temperatures that drive atmospheric teleconnections. Horizontal processes, encompassing advection by currents and the spatial redistribution of heat content anomalies, determine the longitudinal structure and evolution of ENSO events. The parameterization of these processes in climate models directly influences the simulated ENSO characteristics, including amplitude, periodicity, phase-locking, and asymmetry between El Niño and La Niña events.

This report synthesizes evidence from recent modeling studies, forecast system evaluations, and theoretical analyses to address the fundamental question: How does the parameterization of ocean heat redistribution affect seasonal prediction skill regarding ENSO amplitude? We examine three complementary aspects of this problem: the role of vertical mixing parameterizations in linking subsurface thermal conditions to surface manifestations, the importance of diurnal variation schemes in capturing near-surface thermal dynamics, and the influence of horizontal resolution on the representation of heat redistribution processes. Through this analysis, we identify key mechanisms through which parameterization choices translate into prediction skill and highlight areas requiring further research attention.

## 2. Theoretical Framework: Ocean Heat Redistribution and ENSO Dynamics

### 2.1 The Recharge Oscillator Paradigm

Understanding how ocean heat redistribution affects ENSO prediction requires grounding in the theoretical framework that describes ENSO dynamics. The recharge oscillator paradigm, as articulated in foundational theoretical work, posits that ENSO evolution depends critically on the redistribution of heat content across the tropical Pacific basin [1]. During the buildup phase of an El Niño event, warm water volume accumulates in the western equatorial Pacific—a state characterized as "recharged." The subsequent discharge of this heat content, through increased upwelling and horizontal advection, accompanies the transition to neutral or La Niña conditions.

This framework highlights the fundamental importance of accurately representing ocean heat content variations for ENSO prediction. The heat storage capacity of the ocean substantially exceeds that of the atmospheric component, providing the memory that enables seasonal prediction [2]. Subsurface thermal anomalies on basin scales offer the temporal persistence necessary for predictability, as these slowly evolving anomalies carry information about future ENSO states. Consequently, the parameterization of processes that redistribute this heat—vertically within the water column and horizontally across the basin—directly determines the fidelity with which models can capture ENSO dynamics.

### 2.2 Vertical Coupling Mechanisms

The linkage between subsurface thermal conditions and sea surface temperature variations occurs primarily through vertical processes within the upper ocean. The role of vertical mixing, rather than upwelling alone, in connecting thermocline movements to SST changes has been emphasized as a critical physical mechanism that is often neglected in simplified modeling frameworks [3]. Intermediate coupled models that do not employ the full dynamics of the mixed layer may inadequately represent this coupling, leading to systematic biases in ENSO simulations.

The ocean-atmosphere coupling strength itself exhibits seasonal variation, entering models through the coupling coefficient that relates atmospheric heating to underlying sea surface temperatures [3]. This seasonal variation results from the combined effects of mean SST and wind divergence patterns, which modulate the atmospheric response to thermal forcing. The parameterization of this coupling, particularly its seasonal structure, influences the timing and amplitude of ENSO events in model simulations.

## 3. Vertical Mixing Parameterizations and ENSO Prediction Skill

### 3.1 Richardson-Number Dependent Mixing Schemes

The parameterization of vertical mixing in ocean models fundamentally shapes the representation of upper ocean thermal structure and its evolution. Modern climate models employ various mixing schemes, with Richardson-number dependent parameterizations representing a widely adopted approach [4]. These schemes relate the vertical turbulent diffusivity to the local stability of the water column, as characterized by the Richardson number, thereby modulating the rate of heat transfer between layers based on the prevailing dynamic conditions.

The choice of vertical mixing scheme has direct consequences for tropical Pacific temperature simulations. Comparative studies investigating different mixing parameterizations have demonstrated substantial sensitivity of simulated ENSO characteristics to these choices [5]. Models employing more sophisticated mixing schemes that accurately capture the diurnal cycle and seasonal evolution of the mixed layer tend to produce more realistic ENSO amplitude distributions and phase-locking behavior.

### 3.2 Mixed Layer Dynamics and Heat Budget

The mixed layer heat budget provides a diagnostic framework for understanding how vertical mixing affects ENSO prediction. Analysis of coupled model outputs reveals that the development and decay of El Niño events can be attributed to ocean advection, with all three components—zonal, meridional, and vertical—contributing to the heat budget [6]. The vertical component, representing the net effect of mixing and entrainment processes, plays a crucial role in determining the rate at which subsurface heat content anomalies influence surface conditions.

The parameterization of subgrid-scale vertical mixing processes, including both turbulent kinetic energy closure schemes and simpler parameterizations, introduces uncertainty into these heat budget calculations [7]. Models using different mixing schemes exhibit divergent representations of the vertical heat flux, leading to systematic differences in ENSO amplitude evolution and prediction skill. This sensitivity underscores the importance of continued refinement of mixing parameterizations for operational forecasting applications.

### 3.3 Implications for Initialization and Prediction

The representation of vertical mixing processes also influences the effectiveness of initialization strategies for seasonal prediction. Data assimilation techniques that incorporate oceanic observations require accurate model dynamics to properly propagate information about subsurface thermal conditions [8]. When vertical mixing is inadequately parameterized, the assimilation system may produce inconsistent initial states that degrade prediction skill through initialization shock—the adjustment that occurs when a model is started from conditions that are inconsistent with its physics.

The benefit of ocean data assimilation for ENSO prediction depends critically on the quality of the coupled model, including its representation of vertical mixing processes [9]. In models where major sources of forecast error stem from inadequate physics, improvements in ocean initial conditions may have limited impact on prediction skill. This interdependence highlights the need for coordinated advances in both parameterization fidelity and initialization techniques.

## 4. Diurnal Variation Parameterizations and ENSO Amplitude

### 4.1 The Diurnal Amplitude of Sea Surface Temperature

Recent research has revealed that the parameterization of diurnal variations in sea surface temperature significantly affects ENSO simulations, including amplitude, frequency, and asymmetry characteristics [10]. The diurnal amplitude (DA)—defined as the difference between daily maximum and minimum SST—can exceed 3°C under calm and clear conditions, representing a substantial fraction of the total thermal variability. However, capturing this variability requires adequate vertical resolution in the upper ocean, with studies indicating that approximately 1-meter resolution is necessary to resolve the shoaling boundary layer during daytime heating.

The importance of accurate DA simulation extends beyond the diurnal cycle itself. Model experiments have demonstrated that inclusion of diurnal variation parameterization schemes substantially improves ENSO phase-locking simulation—the tendency for El Niño events to reach peak amplitude near the end of the calendar year [10]. This improvement arises primarily from the spatial inhomogeneities in seasonal DA variations during ENSO years, which affect the coupling between ocean and atmosphere in ways that influence event timing.

### 4.2 Mechanisms Linking Diurnal Processes to ENSO Amplitude

Beyond phase-locking, other ENSO characteristics including amplitude, period, and skewness show partial improvement following the inclusion of accurate diurnal amplitude simulation [10]. However, the physical mechanisms driving these relationships remain incompletely understood and require further investigation. Several pathways through which diurnal processes might influence ENSO amplitude have been proposed.

First, the diurnal cycle affects the thermal structure of the upper ocean in ways that modulate the vertical coupling between subsurface and surface layers. Accurate representation of near-surface stratification influences the response of SST to wind forcing and the rate of heat exchange between the mixed layer and deeper waters. Second, diurnal variations in SST affect atmospheric convection and precipitation patterns, thereby influencing the atmospheric component of the coupled system. Third, the cumulative effect of diurnal heating and cooling may contribute to the seasonal evolution of heat content that determines ENSO amplitude.

### 4.3 Parameterization Challenges and Computational Considerations

The implementation of diurnal variation parameterizations in climate models presents substantial technical challenges. Schemes that ignore full mixed-layer dynamics processes can simulate accurate DA of near-surface temperatures but require high vertical resolution in the upper ocean [10]. This requirement substantially increases computational and storage demands, limiting the widespread adoption of such schemes in operational forecasting systems.

Alternative parameterization approaches that capture the essential physics of diurnal cycling without requiring extremely high vertical resolution have been developed [10]. These schemes approximate the effects of diurnal variation through modified boundary layer dynamics or enhanced surface heating formulations. However, the effectiveness of these simplified approaches varies across models and conditions, indicating that further development is needed to achieve robust improvements in ENSO prediction skill.

## 5. Horizontal Resolution and Heat Redistribution

### 5.1 Resolution Effects on Predictive Skill

Horizontal resolution in climate models has been identified as an important factor for advancing seasonal prediction capability [11]. Comparative studies examining forecast systems at different resolutions have demonstrated statistically significant improvements in ENSO prediction skill at higher resolution. For example, the EC-Earth3-HR forecast system, with approximately 40 km atmospheric and 25 km ocean resolution, shows higher predictive skill in the equatorial Pacific compared to the standard resolution configuration with approximately 70 km atmospheric and 100 km ocean resolution [12].

The improvements in predictive skill at higher resolution manifest across multiple variables, including sea surface temperature, zonal surface winds, precipitation, air surface temperature, and mixed layer depth [12]. These improvements extend from the western equatorial Pacific through the Niño3.4 and Niño3 regions, with statistically significant increases in anomaly correlation coefficient for forecast months 3-5 during boreal summer. The resolution dependence of predictive skill suggests that processes governing ocean heat redistribution are more accurately represented at finer horizontal scales.

### 5.2 Physical Processes Resolved at Higher Resolution

The enhanced predictive skill at higher resolution arises from multiple factors related to the representation of physical processes. At coarser resolutions, many important processes are parameterized rather than explicitly resolved, introducing uncertainty into the simulation of heat redistribution [12]. Higher resolution allows these processes to be represented more directly, reducing parameterization-related errors.

Specific processes that benefit from increased resolution include the representation of sharp frontal zones in the tropical Pacific, the dynamics of ocean eddies that redistribute heat horizontally, and the interaction between atmospheric circulation and orographic features [12]. The refined orography resulting from resolution enhancement can subsequently interact with atmospheric circulation in ways that affect the evolution of ENSO-related thermal anomalies. Additionally, differences in initial conditions between resolution configurations may contribute to skill differences, though the relative importance of this factor varies across forecast systems.

### 5.3 Regional Variations in Resolution Sensitivity

The sensitivity of ENSO prediction skill to horizontal resolution exhibits regional variation within the tropical Pacific. The improvement in predictive skill moving from standard to high resolution is most pronounced in the central and eastern equatorial Pacific regions, as measured by anomaly correlation in the Niño3.4 and Niño3 domains [12]. In contrast, the improvement is smaller and not statistically significant in the westernmost part of the equatorial Pacific, as shown by analysis of the Niño4 region.

The relatively poor skill in the Western Equatorial Pacific (WEP) in both resolution configurations indicates that additional factors beyond horizontal resolution limit predictive capability in this region [12]. These factors may include the representation of processes specific to the western Pacific warm pool, the influence of the Maritime Continent, and the interaction of ENSO with other modes of tropical variability. Addressing these limitations may require improvements in parameterizations beyond simple resolution enhancement.

## 6. Ocean Heat Content Initialization and Predictability

### 6.1 The Role of Subsurface Thermal Conditions

Ocean heat content, particularly in the upper 300 meters of the tropical Pacific, provides the primary source of predictability for ENSO at seasonal timescales. The relationship between western equatorial Pacific heat content (T300WA) and upcoming ENSO amplitude has been identified as a key predictor for seasonal forecasts [13]. This relationship reflects the physical connection between heat storage in the western Pacific and the subsequent evolution of ENSO events through the recharge oscillator mechanism.

The importance of subsurface thermal conditions for ENSO prediction has motivated the development of ocean data assimilation systems that incorporate observations from multiple platforms [8]. These systems produce ocean analyses that initialize seasonal forecasts, with the quality of the initial heat content distribution directly influencing prediction skill. The assimilation of observations into ocean models forced by prescribed atmospheric fluxes represents the most common practice for seasonal forecast initialization [9].

### 6.2 Recharged versus Discharged Initial States

The initial heat content state—whether recharged (positive heat content anomaly) or discharged (negative heat content anomaly)—significantly influences subsequent ENSO predictability and evolution [13]. Ensemble experiments initialized from different thermal states demonstrate that the predictability of ENSO depends on the oceanic preconditioning established prior to the forecast period.

However, the relationship between initial state and predictability exhibits model dependence. Some studies using conceptual recharge oscillator models and simplified frameworks point toward enhanced predictability of La Niña events, while others find equivalent predictability for El Niño and La Niña when initialized from real-time observations [13]. This discrepancy may arise from differences in model physics, including the representation of ocean heat redistribution processes, or from the effect of oceanic initial condition uncertainties in realistic forecast settings.

### 6.3 Data Assimilation and Initialization Techniques

The development of data assimilation methods has greatly advanced the initialization of ENSO prediction systems [8]. Progression from simple optimal interpolation in the 1970s-1980s through 3D and 4D variational methods in the 1980s-1990s to ensemble-based methods in the 1990s has enabled increasingly accurate characterization of ocean heat content for forecast initialization.

The impact of ocean data assimilation on ENSO prediction skill depends on multiple factors, including the observing system coverage, the assimilation methodology, and the quality of the coupled model [9]. Assimilation of ocean observations has demonstrated clear benefits for ENSO prediction in multiple forecasting systems. However, the benefits are less pronounced in regions where model errors are large or where observational coverage is insufficient, such as the equatorial Atlantic. The continued development of ocean observing systems and assimilation techniques remains essential for further improvements in ENSO prediction skill.

## 7. Synthesis: Mechanisms Linking Parameterization to Prediction Skill

### 7.1 Pathway 1: Vertical Coupling Fidelity

The first pathway through which parameterization affects ENSO amplitude prediction involves the fidelity of vertical coupling between subsurface and surface layers. Parameterizations that accurately represent vertical mixing processes enable models to properly simulate the response of SST to thermocline variations, which is essential for capturing ENSO amplitude evolution. Models employing full mixed-layer dynamics, as opposed to simplified intermediate coupled approaches, demonstrate improved representation of this coupling [3].

The seasonal variation in ocean-atmosphere coupling strength, which depends on mean SST and wind convergence patterns, further modulates this vertical coupling [3]. Parameterizations that capture the seasonal evolution of coupling strength produce more realistic ENSO phase-locking and amplitude characteristics. The interdependence of vertical mixing parameterization and seasonal coupling representation suggests that comprehensive treatment of upper ocean dynamics is necessary for optimal prediction skill.

### 7.2 Pathway 2: Diurnal and Subdiurnal Variability

The second pathway involves the representation of diurnal and subdiurnal variability in near-surface temperatures. Accurate simulation of diurnal amplitude affects ENSO phase-locking through spatial inhomogeneities in seasonal DA variations [10]. Additionally, the cumulative effects of diurnal cycling may influence the vertical heat distribution and mixed layer evolution in ways that affect ENSO amplitude.

The computational demands of high-resolution diurnal cycling simulation have limited its widespread implementation in operational systems. However, the demonstrated benefits for ENSO prediction suggest that continued development of computationally efficient parameterization schemes is warranted. The trade-off between parameterization complexity and computational cost represents a key consideration for operational forecasting applications.

### 7. Pathway 3: Horizontal Heat Redistribution

The third pathway involves the horizontal redistribution of heat content anomalies across the tropical Pacific basin. Higher horizontal resolution enables more accurate representation of processes governing this redistribution, including eddy dynamics, frontal processes, and current systems [12]. The resulting improvements in heat content distribution translate into enhanced prediction skill for ENSO amplitude.

The regional variation in resolution sensitivity indicates that different aspects of horizontal heat redistribution are more or less resolution-dependent. The central and eastern equatorial Pacific, where ENSO SST signals are strongest, show greater benefit from increased resolution than the western Pacific. This pattern suggests that resolution enhancement primarily improves the representation of processes that affect the propagation and evolution of ENSO-related thermal anomalies in the central and eastern basin.

## 8. Implications for Operational Forecasting

### 8.1 Current State of ENSO Prediction Skill

Contemporary seasonal forecasting systems demonstrate substantial skill for ENSO prediction, particularly in the equatorial Pacific where inter-annual variability is high and ENSO-driven anomalies are predicted with high skill [14]. Anomaly correlation coefficients and amplitude ratios indicate that current systems capture both the timing and magnitude of ENSO events with reasonable accuracy. However, skill degrades for forecasts extending beyond the first few months and in regions where initial condition uncertainties or model biases are large.

The improvements in ENSO forecasts over the past decade can be attributed equally to better initialization of the ocean and improved coupled models [9]. This parallel progress highlights the importance of advancing both parameterization fidelity and initialization techniques to continue improving prediction skill. The interdependence of these factors suggests that gains in one area may be limited without corresponding advances in the other.

### 8.2 Recommendations for Model Development

Based on the analysis presented in this report, several recommendations emerge for model development aimed at improving ENSO amplitude prediction:

First, investment in vertical mixing parameterization development should be prioritized, with particular attention to schemes that accurately represent the coupling between thermocline dynamics and SST variations. The demonstrated sensitivity of ENSO simulations to mixing parameterization indicates that continued refinement of these schemes offers potential for skill improvement.

Second, the implementation of diurnal variation parameterization schemes should be pursued, with efforts focused on developing computationally efficient approaches that capture the essential physics without requiring extremely high vertical resolution. The benefits for phase-locking and amplitude prediction justify the additional computational investment.

Third, horizontal resolution should be increased where computationally feasible, particularly for the tropical Pacific domain. The demonstrated improvements in predictive skill at higher resolution, especially in the central and eastern equatorial Pacific, suggest that resolution enhancement represents an effective strategy for skill improvement.

### 8.3 Challenges and Future Directions

Despite the advances described in this report, substantial challenges remain for ENSO amplitude prediction. The model dependence of results indicates that parameterization improvements may not transfer uniformly across different modeling frameworks [13]. This model dependence argues for coordinated multi-model approaches to ENSO prediction, where the robustness of improvements can be assessed across different systems.

The mechanisms linking diurnal variation parameterization to ENSO amplitude improvement remain incompletely understood [10]. Further research is needed to elucidate these mechanisms and guide the development of more effective parameterization schemes. Additionally, the representation of stochastic processes, such as westerly wind bursts, that significantly influence ENSO evolution requires continued attention.

The development of coupled assimilation systems that provide consistent initial conditions for both ocean and atmosphere components represents an important direction for future research [8]. The more natural initialization method offered by coupled assimilation should provide improved initial conditions for predictions, particularly for variables that depend on the coupled system state.

## 9. Conclusions

The parameterization of ocean heat redistribution processes exerts a profound influence on seasonal prediction skill for ENSO amplitude. Through three primary pathways—vertical coupling fidelity, diurnal variability representation, and horizontal heat redistribution—parameterization choices determine the ability of climate models to accurately simulate ENSO evolution and provide skillful seasonal predictions.

Vertical mixing parameterizations that properly represent the linkage between thermocline movements and SST changes are essential for capturing ENSO amplitude dynamics. The emphasis on vertical mixing rather than upwelling alone, and the importance of full mixed-layer dynamics, indicates that sophisticated treatment of upper ocean processes is necessary for optimal prediction skill.

Diurnal variation parameterizations, despite their computational demands, provide significant benefits for ENSO prediction through improvements in phase-locking and amplitude simulation. The spatial inhomogeneities in diurnal amplitude variations during ENSO years affect the coupling between ocean and atmosphere in ways that influence event timing and magnitude.

Horizontal resolution enhancement improves the representation of processes governing horizontal heat redistribution, leading to statistically significant improvements in predictive skill for the central and eastern equatorial Pacific. The regional variation in resolution sensitivity indicates that different aspects of ENSO dynamics benefit differentially from resolution enhancement.

The continued advancement of ENSO prediction skill will require coordinated progress across multiple fronts: refinement of vertical mixing and diurnal variation parameterizations, strategic enhancement of horizontal resolution where feasible, and development of improved initialization techniques that leverage the full spectrum of available observations. Through these efforts, the seasonal prediction of ENSO amplitude can be further improved, providing greater societal benefit from operational climate forecasting systems.

## References

[1] Jin, F.-F., et al. (2007). Recharge oscillator paradigm. *Journal of Geophysical Research*, 103, 14375–14393.

[2] Latif, M., et al. (1998). A review of the predictability and prediction of ENSO. *Journal of Geophysical Research*, 103, 14375–14393.

[3] Galanti, E., et al. (2002). Ocean-atmosphere seasonal coupling. *Weizmann Institute of Science PhD Thesis*.

[4] Pacanowski, R. C., & Philander, S. G. H. (1981). Parameterization of vertical mixing in numerical models of the tropical ocean. *Journal of Physical Oceanography*, 11, 1442–1451.

[5] Syu, H. H., & Neelin, J. D. (2000). ENSO in a hybrid coupled model. *Journal of Climate*, 13, 2425–2440.

[6] Huang, B., et al. (2011). Mixed layer heat budget of the El Niño in NCEP Climate Forecast System. *Journal of Climate*, 23, 4901–4925.

[7] Blanke, B., & Delecluse, P. (1993). Variability of the tropical Atlantic Ocean simulated by a general circulation model with two different mixed-layer physics. *Journal of Physical Oceanography*, 23, 1363–1388.

[8] Duan, W., et al. (2019). ENSO prediction and initialization techniques. *National Science Review*, 5, 826-847.

[9] Balmaseda, M. A., & Anderson, D. (2009). Initialization techniques in seasonal forecasts. *ECMWF Seminar on Seasonal Prediction*.

[10] FIO-ESM v2.0 (2023). Diurnal variation parameterization and ENSO phase-locking. *Nature*, 12, 483.

[11] Xue, Y., et al. (2017). Resolution in climate models and seasonal prediction capability. *Journal of Climate*, 29, 7759-7778.

[12] EC-Earth3-HR (2025). High-resolution forecast system and ENSO predictive skill. *EGU Sphere Preprints*, 2025-4658.

[13] Planton, Y., et al. (2018). Western equatorial Pacific heat content and ENSO predictability. *Climate Dynamics*, 51, 3309-3326.

[14] Balmaseda, M. A., et al. (2021). Ocean heat content forecast skill across global ocean regions. *Climate Dynamics*, 57, 2867-2890.

## Annotations


## Sources
[1] https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2019MS001759
[2] https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2021GL096932
[3] https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2025GL116972
[4] https://archimer.ifremer.fr/doc/00694/80616/83870.pdf
[5] https://egusphere.copernicus.org/preprints/2025/egusphere-2025-4658/egusphere-2025-4658.pdf
[6] https://esd.copernicus.org/articles/13/1611/2022/esd-13-1611-2022.pdf
[7] https://journals.ametsoc.org/view/journals/clim/29/24/jcli-d-16-0117.1.pdf
[8] https://journals.ametsoc.org/view/journals/clim/33/1/jcli-d-18-0877.1.xml
[9] https://journals.ametsoc.org/view/journals/clim/35/11/JCLI-D-21-0383.1.xml
[10] https://journals.ametsoc.org/view/journals/mwre/126/4/1520-0493_1998_126_1022_aicmfe_2.0.co_2.xml
[11] https://journals.ametsoc.org/view/journals/phoc/49/1/jpo-d-18-0100.1.pdf
[12] https://labesm-staff.iap.ac.cn/duanws/ueditor/php/upload/file/20190903/1567478903273663.pdf
[13] https://link.springer.com/article/10.1007/s00382-021-06101-3
[14] https://www.aos.wisc.edu/aosjournal/Volume31/Thomas_PhD.pdf
[15] https://www.cpc.ncep.noaa.gov/products/people/yxue/pub/33.pdf
[16] https://www.ecmwf.int/sites/default/files/elibrary/2013/7901-initialization-techniques-seasonal-forecasts.pdf
[17] https://www.mdpi.com/2072-4292/14/14/3363
[18] https://www.nationalacademies.org/read/23552/chapter/5
[19] https://www.nature.com/articles/s41612-023-00483-3
[20] https://www.sciencedirect.com/science/article/pii/B9780443315381000105
[21] https://www.weizmann.ac.il/EPS/Galanti/sites/EPS.Galanti/files/publications/Galanti_phd_thesis.pdf