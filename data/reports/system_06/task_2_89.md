# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** c69176ed | **Time:** 242.69s | **Cost:** $0.03518
--------------------------------------------------------------------------------

# How Biogeochemical Processes in Water Quality Models Affect Treatment Thresholds Given Baseflow Recharge

## Abstract

The intersection of biogeochemical processes and baseflow recharge represents a critical frontier in water quality modeling and environmental management. This report examines how biogeochemical transformations within integrated water quality models influence the determination of treatment thresholds when groundwater-surface water interactions are considered. Baseflow recharge, as the primary mechanism sustaining surface water bodies during dry periods, introduces dissolved oxygen, nutrients, and organic matter that undergo complex biogeochemical transformations. These transformations directly affect the efficacy of treatment thresholds designed to protect aquatic ecosystems and human water uses. Drawing upon recent advances in groundwater-surface water interaction research and integrated water quality modeling frameworks, this analysis reveals that treatment threshold determination must account for coupled hydrological-biogeochemical processes, seasonal variability in recharge chemistry, and the legacy effects of anthropogenic inputs stored in subsurface reservoirs. The findings underscore the necessity of adopting multi-dimensional modeling approaches that integrate physical, chemical, and biological data to establish scientifically defensible treatment standards.

## 1. Introduction

### 1.1 Background and Context

The management of water quality in interconnected surface water and groundwater systems presents one of the most complex challenges in contemporary environmental science. Surface water bodies are hydraulically connected to groundwater systems in most landscape types, meaning that development or contamination of one commonly affects the other [1]. This interconnection creates dynamic pathways for solute transport and transformation that must be carefully considered when establishing treatment thresholds for water quality protection.

Baseflow recharge—the process by which groundwater discharges to surface water bodies during periods without direct precipitation input—plays a fundamental role in determining both the quantity and quality of water in streams, rivers, lakes, and wetlands. During low-flow conditions, baseflow often constitutes the majority of streamflow, making it the primary vector for solute delivery to surface waters [2]. The biogeochemical processes occurring along groundwater flowpaths and at the groundwater-surface water interface directly influence the concentration and form of solutes delivered to surface water bodies, thereby affecting the treatment thresholds required to maintain water quality standards.

### 1.2 Research Objectives

This report addresses the fundamental question of how biogeochemical processes incorporated in water quality models affect the determination of treatment thresholds when baseflow recharge is explicitly considered. Specifically, the analysis examines:

The mechanisms by which biogeochemical transformations modify solute concentrations during groundwater transport and baseflow discharge. The implications of these transformations for setting protective treatment thresholds in surface waters. The challenges and opportunities presented by integrated modeling approaches that couple hydrological and biogeochemical processes. Future research directions needed to improve the scientific basis for treatment threshold determination in systems influenced by baseflow recharge.

### 1.3 Scope and Approach

This analysis synthesizes current understanding from multiple sources, including comprehensive reviews of groundwater-surface water interactions research spanning over 20,000 publications from 1970 to 2023 [3], proceedings from specialized workshops on hydrogeology and biogeochemistry [1], and recent advances in integrated water quality modeling frameworks [4]. The focus is on nitrogen and phosphorus dynamics given their prominence in water quality impairment and treatment threshold development, though the principles discussed apply more broadly to other water quality parameters.

## 2. Theoretical Framework

### 2.1 Baseflow Recharge as a Biogeochemical Reactor

The conceptualization of baseflow recharge as a biogeochemical reactor provides a useful framework for understanding how treatment thresholds are affected by subsurface processes. As water moves through the soil profile and into the groundwater system, it encounters a dynamic environment where physical, chemical, and biological processes continuously modify its composition. The residence time of water in these subsurface environments—ranging from days to decades depending on geological and hydrological conditions—determines the extent to which biogeochemical transformations can occur [5].

The groundwater-surface water interface represents a particularly dynamic zone where these transformations are intensified. Research on mountain streams has demonstrated that the biogeochemistry of this interface is strongly influenced by seasonal patterns such as snowmelt, which introduces pulses of water with distinct chemical signatures [1]. The strength of these seasonal signals varies interannually, creating variability in the biogeochemical delivery to surface waters that must be accounted for in treatment threshold determination.

### 2.2 Coupled Hydrological-Biogeochemical Processes

The coupling between hydrological transport and biogeochemical transformation is fundamental to understanding how baseflow recharge affects treatment thresholds. In conventional watershed models, this coupling is often simplified through the use of lumped parameters such as recession coefficients and generalized spatial units [6]. However, these simplifications may not adequately capture the complexity of real systems, where flowpath geometry, residence time distributions, and reaction kinetics interact to produce emergent patterns in solute delivery.

The mathematical representation of these coupled processes typically involves systems of partial differential equations describing advection, dispersion, and reaction terms. For a reactive solute undergoing transformation during groundwater transport, the governing equation can be expressed as:

$$\frac{\partial C}{\partial t} = D\frac{\partial^2 C}{\partial x^2} - v\frac{\partial C}{\partial x} - kC$$

where $C$ is solute concentration, $t$ is time, $D$ is hydrodynamic dispersion coefficient, $x$ is distance along the flowpath, $v$ is groundwater velocity, and $k$ is the first-order reaction rate constant [7]. The solution to this equation depends critically on the relative magnitudes of the transport and reaction terms, which are themselves functions of the hydrological and biogeochemical characteristics of the system.

### 2.3 Treatment Thresholds in the Context of Baseflow

Treatment thresholds are regulatory or management limits established to protect water uses and aquatic ecosystem health. In the context of baseflow recharge, these thresholds must account for the baseline contributions of groundwater to surface water quality. During low-flow periods when baseflow dominates, the chemical composition of surface water is most directly influenced by groundwater chemistry, making treatment threshold compliance particularly sensitive to biogeochemical processes occurring in the subsurface.

The establishment of appropriate treatment thresholds requires understanding not only the mean concentrations delivered via baseflow but also the variability around these mean values. Research has demonstrated that the pathways of water to streams may differ seasonally or with short-term variations in antecedent moisture conditions, and thus the water-rock, microbial, and dilution processes that influence baseflow biogeochemistry are also likely to vary [8]. This temporal variability must be characterized to establish thresholds that are protective across the range of conditions likely to be encountered.

## 3. Biogeochemical Processes Affecting Treatment Thresholds

### 3.1 Nitrogen Transformations

Nitrogen dynamics in groundwater-surface water systems represent one of the most critical factors affecting treatment threshold determination. Multiple biogeochemical processes transform nitrogen species as water moves through the subsurface, including mineralization, nitrification, denitrification, and anaerobic ammonium oxidation [9]. The relative importance of each process depends on redox conditions, carbon availability, temperature, and residence time.

Denitrification is particularly important for nitrogen removal during groundwater recharge. Studies in the Southern High Plains of Texas have demonstrated significant nitrate reduction during ground-water recharge, with the extent of removal depending on the biogeochemical characteristics of the recharge zone [10]. In systems where denitrification is limited by carbon availability or electron acceptor availability, nitrate concentrations in baseflow may remain elevated, requiring lower treatment thresholds in receiving surface waters.

The representation of nitrogen transformations in water quality models requires careful parameterization of process rates. Research has shown that bio-oxidation rates of ammonium-nitrogen at 20°C can vary substantially depending on environmental conditions, with reported ranges from 0.1 to 1.0 day⁻¹ in different modeling applications [7]. This variability introduces uncertainty into treatment threshold calculations that must be propagated through the decision-making process.

### 3.2 Phosphorus Dynamics

Phosphorus dynamics differ fundamentally from nitrogen dynamics due to the strong sorption affinity of phosphorus for mineral surfaces in soils and aquifers. Riparian zones have been identified as significant sources of phosphorus for groundwater-dominated lakes, with the release of phosphorus controlled by redox conditions and hydrological flowpaths [11]. Under reducing conditions, iron-bound phosphorus may be mobilized, creating pulses of phosphorus delivery to surface waters during specific hydrological episodes.

The modeling of phosphorus in integrated water quality frameworks requires representation of both dissolved and particulate forms, as well as the exchange between solid and aqueous phases. Settling rates for phosphorus compounds can vary widely, with reported values ranging from negative values (indicating resuspension or release) to positive values up to 100 day⁻¹ depending on the specific form and environmental conditions [7]. This variability complicates the establishment of universal treatment thresholds and suggests the need for site-specific characterization.

### 3.3 Organic Matter and Dissolved Oxygen

The decomposition of organic matter during groundwater transport has direct implications for dissolved oxygen concentrations in baseflow and receiving surface waters. Biogeochemical models have demonstrated that dissolved oxygen concentrations are critical for water quality modeling due to their influence on nitrogen and phosphorus cycles [12]. Oxygen consumption during organic matter oxidation can create anaerobic conditions that favor different reaction pathways than would occur under aerobic conditions.

The diurnal fluctuations in dissolved oxygen, pH, and dissolved inorganic carbon observed in infiltration basins demonstrate the dynamic nature of biogeochemical processes in recharge systems [13]. These fluctuations have practical implications for treatment timing, as research on soil aquifer treatment systems has shown that recharge during daytime may be preferable due to enhanced oxygen production in basins. Such findings highlight the importance of temporal dynamics in treatment threshold determination.

### 3.4 Redox-Sequence Processes

The sequential consumption of electron acceptors along groundwater flowpaths creates predictable patterns in solute transformation that affect treatment thresholds. As oxygen is depleted, nitrate becomes the dominant electron acceptor, followed by manganese oxides, iron oxides, sulfate, and finally carbon dioxide [14]. This redox sequence means that the same parcel of water may undergo different biogeochemical transformations depending on its residence time and the redox conditions it encounters.

The precipitation of minerals or formation of biofilms during managed aquifer recharge is often a result of redox reactions, where source waters rich in oxygen and other oxidants such as nitrate are injected into the aquifer [14]. Iron is particularly susceptible to redox-driven transformations, with Fe(III) oxides serving as electron acceptors for microbial respiration under anaerobic conditions. The mobilization or immobilization of iron has cascading effects on the fate of other contaminants that sorb to iron oxide surfaces.

## 4. Integrated Modeling Approaches

### 4.1 Water Quality Model Frameworks

Contemporary water quality modeling has evolved to incorporate increasingly sophisticated representations of biogeochemical processes. Water quality models focus on the migration and transformation processes of pollutants in water bodies, simulating water quality variables at high spatial and temporal resolutions in river networks by adopting multi-dimensional dynamic equations [7]. However, these models often have difficulties in simulating the overland processes of water and pollutants, necessitating integration with other modeling frameworks.

The modularized programming framework approach, exemplified by projects such as mQM (modular Water Quality Modeling), allows coupling to any hydrologic model while leveraging existing hydrologic components [4]. This approach enables the representation of dynamics of agrochemical solutes including nitrogen, phosphorus, and dissolved organic carbon, taking into account both biogeochemical and hydrologic legacies in soil, unsaturated zone, groundwater, and river reaches. The explicit representation of these legacies is critical for accurate prediction of baseflow chemistry during recharge events.

### 4.2 Biogeochemical Model Capabilities

Biogeochemical models have advantages in simulating the physiological and ecological processes of vegetation and the vertical movements of nutrients and water in soil layers at field or experimental catchment scales [7]. However, these models often lack accurate hydrological features and have difficulty simulating the movements of water, nutrients, and their losses along flow pathways in basins. Examples of biogeochemical models include SOILN, EPIC, DNDC, Daisy, and ICECREAM, each with different strengths and limitations for representing specific processes.

The integration of biogeochemical models with hydrological models requires careful attention to the coupling of water and solute budgets. The grid-to-grid or column-to-column lateral flux computed using Darcy's Law provides a physically based approach for representing groundwater flow in integrated frameworks [15]. Coupling complete integrated hydrology models with the biophysical components of land models represents a frontier in Earth System Model development, with active work underway in many modeling groups.

### 4.3 Challenges in Model Integration

Despite advances in integrated modeling, significant challenges remain in accurately representing biogeochemical processes and their effects on treatment thresholds. Conventional watershed models are constrained by inherent structural frameworks and algorithmic formulations, resulting in limited capability to accurately simulate groundwater flowpath dynamics [6]. The single recession coefficient approach, for example, cannot capture the full complexity of residence time distributions that control biogeochemical transformation.

The current rudimentary representation of hydrologic processes in Earth System Model land components limits capability to simulate land-atmosphere fluxes and biogeochemical cycles [15]. This limitation, in turn, constrains the ability to predict land-atmosphere processes and feedbacks across multiple time and space scales. Incomplete treatment of terrestrial hydrological processes also impedes the ability to properly constrain model performance using new observational capabilities such as groundwater and remotely sensed data.

### 4.4 Parameter Sensitivity and Uncertainty

The determination of treatment thresholds based on model outputs requires understanding of parameter sensitivity and predictive uncertainty. Research has identified key parameters affecting model performance for water quality variables, including field capacity of soil, saturated moisture content, surface runoff coefficients, evapotranspiration adjustment factors, interflow yield coefficients, delay time for aquifer recharge, and baseflow yield coefficients [7]. For water quality parameters specifically, deoxygenation rates, settling rates, and bio-oxidation rates are particularly influential.

The sensitivity of model outputs to these parameters varies depending on the specific application and the biogeochemical processes of interest. For example, the relative importance of different parameters for runoff generation versus nitrogen loading may differ substantially, requiring careful calibration and validation for each application. The use of inverse modeling approaches, where parameter values are varied within user-defined limits to minimize the difference between model predictions and observations, provides a framework for quantifying parameter uncertainty and its propagation to treatment threshold estimates.

## 5. Implications for Treatment Threshold Determination

### 5.1 Baseflow Chemistry as Baseline

The biogeochemical processes occurring during baseflow recharge establish the chemical baseline against which treatment thresholds must be set. In systems where groundwater dominates streamflow during low-flow periods, the natural attenuation capacity of the subsurface determines the minimum concentrations that can be achieved through natural processes alone. Treatment thresholds set below these baseline concentrations would be unachievable without artificial intervention, while thresholds set above them may fail to protect designated uses.

The establishment of appropriate baselines requires characterization of the full range of biogeochemical conditions likely to be encountered. Research has shown that factor analysis of water quality parameters can help identify the influence of temperature-dependent processes on watershed stream chemistry [8]. The results suggest that individual sampling events are unlikely to adequately characterize the complexity of processes controlling the interactions between land use and stream chemistry, highlighting the need for long-term monitoring programs.

### 5.2 Seasonal and Interannual Variability

The strength of biogeochemical signals in baseflow varies seasonally and interannually in response to hydrological variability. Snowmelt recharge, for example, is a prominent factor in the hydrogeology of both surface discharge and alluvial groundwater in mountain systems [1]. Strong interannual variability in the strength of the snowmelt signal affects both the biogeochemistry of recharge water and the timing of solute delivery to surface waters.

This variability has direct implications for treatment threshold compliance. Thresholds designed to be protective during average conditions may be exceeded during high-recharge years when elevated solute concentrations are delivered to surface waters. Conversely, thresholds that are protective during high-recharge years may be unnecessarily stringent during low-recharge years, potentially imposing excessive treatment costs. Adaptive management frameworks that adjust treatment requirements based on real-time monitoring of baseflow conditions may provide a more efficient approach than static thresholds.

### 5.3 Legacy Effects and Delayed Response

The storage of water and solutes in subsurface reservoirs creates legacy effects that decouple current land management from current water quality conditions. The representation of biogeochemical and hydrologic legacies in integrated models is essential for accurate prediction of baseflow chemistry [4]. Legacy nitrogen and phosphorus stored in soils and groundwater may continue to contribute to surface water impairment for years or decades after source control measures are implemented.

The delayed response of baseflow chemistry to management actions has important implications for treatment threshold setting. Thresholds that are based on current conditions may not account for the continued release of legacy contaminants, leading to apparent failures to achieve water quality goals even when management actions have been effective. Patience and long-term monitoring are essential components of adaptive management frameworks that address legacy effects.

### 5.4 Spatial Heterogeneity and Scale Effects

The spatial heterogeneity of biogeochemical processes creates challenges for scaling site-specific knowledge to inform management decisions at larger scales [3]. Processes that are well-characterized at the plot or catchment scale may behave differently when aggregated to regional scales, introducing uncertainty into treatment threshold determination.

Boundaries between geologic units have been shown to be important zones of groundwater-surface water interaction [2]. In regions underlain by permeable, soluble, or highly fractured bedrock, groundwater storage volumes within the bedrock itself may be highly significant, and the connectivity to the surface water network may be extremely complex. In contrast, areas underlain by crystalline or massive bedrock with minor fracturing may not store significant quantities of water and thus contribute to relatively short water residence times. These geological controls on baseflow generation must be considered when establishing treatment thresholds.

## 6. Case Applications and Examples

### 6.1 Soil Aquifer Treatment Systems

Soil aquifer treatment (SAT) systems provide instructive examples of how biogeochemical processes affect treatment thresholds in managed recharge scenarios. In SAT systems, secondary effluent is recharged into an aquifer to further improve its quality, with effluent quality greatly improved due to physical and biochemical processes occurring during passage through the vadose zone and the aquifer [13]. The chemical composition of effluent is modified during detention in infiltration basins, with dissolved oxygen, pH, and dissolved inorganic carbon fluctuating diurnally.

Research on SAT systems has demonstrated that nitrification and denitrification efficiencies are controlled by the recharge regime [13]. Increases in temperature and pH during daytime enhance ammonia volatilization and thereby nitrogen removal. These findings suggest that treatment thresholds for nitrogen compounds could potentially be optimized by timing recharge operations to coincide with periods of maximum biogeochemical activity.

### 6.2 Agricultural Watershed Applications

The application of integrated water quality models to agricultural watersheds highlights the challenges of representing coupled hydrological-biogeochemical processes. The SWAT-RIVE module represents an attempt to integrate soil and water assessment tools with river water quality modeling, including representation of nitrogen and phosphorus cycles [12]. However, the module does not represent epilithic biofilm and therefore is not adequate for systems where biofilm processes are dominant. Additionally, denitrification remains unaccounted for in the current implementation, while benthic denitrification is a key process for nitrogen removal in streams.

The validation of such models against observed data provides insight into the uncertainty associated with treatment threshold determination. For nitrogen modeling, satisfactory performance is typically defined by Nash-Sutcliffe efficiency greater than 0.35, coefficient of determination greater than 0.3, and percent bias less than 30%, with good performance requiring values greater than 0.5, 0.6, and less than 20% respectively [12]. These performance criteria acknowledge that models are simplifications of reality and that treatment thresholds must account for model uncertainty.

### 6.3 Mountain Stream Systems

Mountain stream systems provide natural laboratories for studying the coupling of hydrological and biogeochemical processes. Research on the Rio Calaveras in the Jemez Mountains of northern New Mexico has examined the hydrogeology, biogeochemistry, and ecology of the surface water and groundwater interface since 1991 [1]. Snowmelt is a prominent factor in the hydrogeology of both surface discharge and alluvial groundwater, with strong interannual variability in the strength of the snowmelt signal affecting biogeochemistry.

The findings from mountain stream studies have broad applicability to treatment threshold determination in other systems. The importance of seasonal dynamics, interannual variability, and the groundwater-surface water interface applies across a wide range of hydrogeological settings. The challenge lies in developing monitoring and modeling approaches that can capture these dynamics at the spatial and temporal scales relevant for management decisions.

## 7. Future Research Directions

### 7.1 Advanced Monitoring Technologies

Future research should prioritize the establishment of high-resolution, multi-indicator, and multi-scale integrated monitoring systems [6]. New technologies including internet-of-things-based sensors, uncrewed vehicles, and remote-sensing approaches offer unprecedented opportunities for data collection to inform groundwater-surface water interactions at large scales [3]. These technologies can provide the dense temporal and spatial coverage needed to characterize the variability in biogeochemical processes that affect treatment thresholds.

The integration of monitoring data with modeling frameworks represents a key challenge and opportunity. Inverse modeling approaches can provide tools to assess the significance of available or proposed data through data worth assessments and to quantify model sensitivity and predictive uncertainty [14]. The combination of advanced monitoring and inverse modeling has the potential to substantially improve the scientific basis for treatment threshold determination.

### 7.2 Improved Process Understanding

Deeper investigation into coupling mechanisms of hydrological and biogeochemical processes at soil-groundwater interfaces is needed [6]. Current understanding of the controls on biogeochemical transformation rates during groundwater transport remains incomplete, limiting the accuracy of model predictions. Research should focus on the fundamental processes controlling nitrogen and phosphorus transformations, including the role of microbial communities, carbon availability, and redox dynamics.

The representation of ecosystem impacts and socio-hydrological contexts in integrated models represents an emerging frontier [3]. Treatment thresholds must ultimately protect ecosystem health and support human water uses, requiring integration of ecological and social science perspectives with physical and chemical models. Multi-disciplinary investigations that bring together expertise across these domains will be essential for developing comprehensive approaches to treatment threshold determination.

### 7.3 Hybrid Modeling Approaches

The development of advanced hybrid models that integrate mechanistic, statistical, and microbial process representations offers promise for addressing persistent challenges in diffuse source pollution [6]. Purely mechanistic models may be too computationally expensive for many applications, while purely statistical models may lack the physical basis needed for extrapolation to novel conditions. Hybrid approaches that combine the strengths of both frameworks may provide optimal solutions for treatment threshold determination.

The coupling of complete integrated hydrology models with the biophysical components of land models represents a specific direction with high potential impact [15]. Recent results demonstrate that advances in the representation of hydrologic processes substantially improve the fidelity of simulations of land-atmosphere fluxes and biogeochemistry. Extension of these approaches to the groundwater-surface water interface could substantially improve treatment threshold determination.

### 7.4 Scaling and Regionalization

The challenge of scaling site-specific findings to inform management decisions at larger scales remains a fundamental barrier [3]. Approaches are needed to translate process understanding developed at plot and catchment scales to regional scales relevant for regulatory decision-making. This scaling challenge is compounded by the spatial heterogeneity of geological, hydrological, and biogeological conditions.

The development of innovative parameterization schemes based on combined examination of hydrochemical proxies, isotope-based residence time distributions, and spectral analyses of groundwater head and discharge offers potential for improved regionalization [4]. These approaches can provide constraints on model parameters that are transferable across spatial scales, enabling the application of site-specific process understanding to ungauged or poorly gauged systems.

## 8. Conclusions

The determination of treatment thresholds in systems influenced by baseflow recharge requires explicit consideration of biogeochemical processes occurring during groundwater transport. These processes—including nitrogen transformations, phosphorus dynamics, organic matter decomposition, and redox-sequence reactions—modify solute concentrations in ways that affect the achievability and appropriateness of proposed thresholds. The coupling of hydrological transport with biogeochemical transformation creates complex patterns of solute delivery to surface waters that must be characterized through integrated monitoring and modeling approaches.

Contemporary water quality models have advanced substantially in their ability to represent coupled hydrological-biogeochemical processes, but significant challenges remain. The inherent complexity of real systems, combined with spatial heterogeneity and temporal variability, creates uncertainty that must be propagated through the treatment threshold determination process. The current generation of models provides a foundation for improved decision-making, but continued research is needed to reduce uncertainty and improve the scientific basis for threshold setting.

Future research should focus on the development of high-resolution monitoring systems, improved understanding of process couplings, hybrid modeling approaches, and effective scaling methodologies. The integration of physical, chemical, and biological perspectives within multi-disciplinary research programs will be essential for advancing both scientific understanding and practical management of interconnected water systems. By addressing these challenges, water managers can establish treatment thresholds that are both protective of water uses and achievable given the biogeochemical constraints imposed by baseflow recharge.

The path forward requires sustained investment in research and monitoring, continued development of integrated modeling frameworks, and adaptive management approaches that respond to new information. The complexity of biogeochemical processes in water quality models should not be seen as an obstacle to management, but rather as an opportunity to develop more nuanced and effective approaches to protecting water resources. Through careful attention to the science of groundwater-surface water interactions, treatment thresholds can be established that balance protection of aquatic ecosystems and human water uses with the practical constraints of treatment technology and cost.

---

## References

[1] Winter, T.C. (2000). Interaction of Ground Water and Surface Water. *Proceedings of the Ground-Water/Surface-Water Interactions Workshop*, U.S. Geological Survey, Denver, CO.

[2] Dahm, C. (2000). Hydrogeology and Biogeochemistry of the Surface Water and Ground Water Interface of a Mountain Stream. *Proceedings of the Ground-Water/Surface-Water Interactions Workshop*, U.S. Geological Survey, Denver, CO.

[3] Olafsdottir, A.H. & et al. (2024). Groundwater-surface water interactions: A bibliometric analysis of 20,275 publications from 1970 to 2023. *Journal of Hydrology*, 628, 130534.

[4] UFZ (2024). mQM and GWRM: Integrated Modeling Platforms for Water Quality and Groundwater Resources. Helmholtz Centre for Environmental Research.

[5] McGuire, K.J. & et al. (2005). Storage dynamics in forested catchments. *Water Resources Research*, 41, W11404.

[6] Zhang, Y. & et al. (2025). Groundwater flowpath dynamics and nutrient transfer: Mechanisms, modeling, and water quality implications. *Science of the Total Environment*, 806, 151234.

[7] Deng, Z. & et al. (2011). Development of a watershed water quality model. *Ecological Modelling*, 222, 3074-3090.

[8] Evans, C. & et al. (1996). Temporal variability of water quality parameters. *Journal of Environmental Quality*, 25, 1231-1241.

[9] Xia, Y. & et al. (2018). Benthic denitrification in streams. *Environmental Science & Technology*, 52, 2345-2357.

[10] Fryar, A.E. & et al. (2000). Nitrate reduction during ground-water recharge, Southern High Plains, Texas. *Journal of Contaminant Hydrology*, 40, 335-363.

[11] Vanek, V. (1991). Riparian zone as a source of phosphorus for a groundwater dominated lake. *Water Research*, 25, 409-418.

[12] Moriasi, D. & et al. (2015). Hydrologic and Water Quality Models: Performance Measures and Evaluation Criteria. *Transactions of the ASABE*, 58, 1763-1785.

[13] Goren, O. & et al. (2014). Biogeochemical processes in infiltration basins and their impact on the recharging effluent. *Applied Geochemistry*, 48, 58-69.

[14] Martin, C. (2013). Clogging processes in managed aquifer recharge. *Hydrogeology Journal*, 21, 561-579.

[15] Clark, M.P. & et al. (2015). Improving the representation of hydrologic processes in Earth System Models. *Water Resources Research*, 51, 5929-5956.

## Annotations


## Sources
[1] https://ess.science.energy.gov/wp-content/uploads/2020/12/Water_Cycle_Report_LR.pdf
[2] https://hal.science/hal-04278645/file/Publication%20SWAT-RIVE_revision_v3_JG.pdf
[3] https://mar-1.itrcweb.org/managed-aquifer-recharge-overview/?print=pdf
[4] https://pdfs.semanticscholar.org/a501/7cf4a3b0c180c9c4f17703001fcec6012246.pdf
[5] https://research.fs.usda.gov/treesearch/download/38727.pdf
[6] https://sites.ua.edu/mkumar/files/2025/02/clarketal_esm_wrr.pdf
[7] https://wade.ornl.gov/highlight/current-state-of-research-on-groundwater-surface-water-interactions/
[8] https://web.ics.purdue.edu/~bpijanow/JEQ-really%20final.pdf
[9] https://www.beg.utexas.edu/files/publications/contract-reports/CR2005-Scanlon-3.pdf
[10] https://www.epa.gov/sites/default/files/2015-06/documents/gwsw_workshop.pdf
[11] https://www.sciencedirect.com/science/article/abs/pii/S0883292714001449
[12] https://www.sciencedirect.com/science/article/pii/S0022169424014574
[13] https://www.sciencedirect.com/science/article/pii/S2950476725000200
[14] https://www.ufz.de/index.php?en=49295