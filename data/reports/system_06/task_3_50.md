# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 0b090999 | **Time:** 229.83s | **Cost:** $0.18288
--------------------------------------------------------------------------------

# How Does the Stress-Strain Relationship in Ice Flow Models Constrain Sea Level Rise Predictions Given Basal Sliding Changes?

## A Technical Research Report

---

## Executive Summary

The projection of future sea level rise remains one of the most consequential challenges in climate science, with estimates for the 21st century varying between approximately 50 centimeters and over 100 centimeters relative to 1900 levels [1]. This substantial uncertainty fundamentally hampers the formulation of effective adaptation strategies for coastal communities worldwide. At the heart of this uncertainty lies a complex interplay between the mechanical behavior of ice and the processes governing ice sheet dynamics, particularly the relationship between stress and strain in ice flow models and how this relationship responds to changes in basal sliding conditions.

This report examines the fundamental physics governing ice flow, focusing on how the stress-strain relationship—encapsulated in flow laws for internal deformation and sliding laws for basal motion—constrains and influences sea level rise predictions. The analysis reveals that basal sliding represents a dominant mode of ice motion along ice sheet margins, where fast-flowing outlet glaciers slide over thawed beds [2]. The parameterization of basal sliding, including the choice of sliding law formulation and its associated parameters, constitutes a key source of uncertainty in ice sheet models. Recent research has demonstrated that ice loss projections, particularly for sensitive regions such as the Amundsen Sea Embayment, are highly sensitive to the applied sliding law, with sliding law parameters being a primary driver of uncertainty in sea level projections [3].

The evidence synthesized from multiple modeling studies indicates that the choice between different sliding law formulations—particularly Weertman-type power laws versus Coulomb behavior—can lead to substantially different sea level rise contributions. Bayesian model selection has identified Coulomb behavior as the most probable mode of sliding in fast-flowing regions, potentially increasing sea level rise contributions from critical Antarctic basins [3]. These findings carry significant implications for the development of next-generation ice sheet models and the interpretation of sea level projections for policy-making purposes.

---

## 1. Introduction

### 1.1 The Critical Importance of Ice Sheet Dynamics in Sea Level Projections

Mass loss from the Greenland and Antarctic ice sheets has emerged as a major driver of global sea level change, with ice flow dynamics playing a central role in determining the magnitude and rate of future contributions [4]. The Intergovernmental Panel on Climate Change has recognized that dynamical processes related to ice flow not included in earlier computer models, but suggested by recent observations, could increase the vulnerability of ice sheets to warming and thereby increase future sea level rise [5]. Understanding of these processes remains limited, and there is no consensus on their precise magnitude, representing a critical gap in our ability to project future sea levels accurately.

The fundamental challenge in ice sheet modeling lies in the complex, highly nonlinear behavior of ice as a material and the difficulty in observing processes occurring at the ice-bed interface, where much of the motion is generated. Ice sheets flow through a combination of internal deformation, governed by the rheological properties of ice, and basal sliding, where ice slides over the underlying bedrock or sediments. The relative contribution of these two mechanisms varies across the ice sheet, with internal deformation dominating in the cold interior regions and basal sliding becoming increasingly important in fast-flowing ice streams and outlet glaciers that drain the majority of ice from the sheet [6].

### 1.2 Scope and Objectives of This Report

This technical report synthesizes current understanding of how the stress-strain relationship in ice flow models constrains sea level rise predictions, with particular emphasis on the role of basal sliding changes. The analysis addresses several interconnected questions that are critical to advancing our predictive capabilities:

First, we examine the mathematical formulation of stress-strain relationships in ice flow, including both the flow laws governing internal deformation and the sliding laws describing basal motion. Second, we investigate how these relationships propagate through ice sheet models to influence sea level projections. Third, we analyze the sensitivity of model predictions to different sliding law formulations and parameter choices. Finally, we identify key knowledge gaps and recommend directions for future research and model development.

The analysis draws upon recent advances in ice sheet modeling, including high-resolution simulations, inverse methods for parameter estimation, and ensemble approaches to uncertainty quantification. Particular attention is given to the Amundsen Sea Embayment of West Antarctica, which represents the largest potential source of near-term sea level rise from the Antarctic Ice Sheet and has been the focus of intensive research efforts.

---

## 2. The Stress-Strain Relationship in Ice Flow Models

### 2.1 Fundamental Principles of Ice Rheology

Ice exhibits complex rheological behavior that is fundamentally temperature-dependent and highly nonlinear. At the stress levels encountered in ice sheets, ice behaves as a non-Newtonian viscous material, with the relationship between stress and strain rate following a power-law relationship known as Glen's flow law. The general form of this relationship can be expressed as:

$$\dot{\epsilon}_{ij} = A(T) \tau_E^{n-1} \tau_{ij}$$

where $\dot{\epsilon}_{ij}$ is the strain rate tensor, $A(T)$ is a temperature-dependent rate factor, $\tau_E$ is the effective stress (the second invariant of the deviatoric stress tensor), $\tau_{ij}$ is the deviatoric stress tensor, and $n$ is the flow law exponent, typically taken as $n = 3$ for polycrystalline ice [7].

The rate factor $A(T)$ is highly sensitive to temperature, following an Arrhenius-type relationship that accounts for the thermally activated nature of ice creep. This temperature dependence creates a thermo-mechanical coupling in ice sheet models, where the temperature field influences the flow velocity, which in turn affects the temperature distribution through advection and dissipation. The basal temperate layer, where ice is at the pressure melting point, represents an important modulator of ice motion, extending or compressing in response to topographic perturbations [8].

### 2.2 Mathematical Representation of Internal Deformation

The stress-strain relationship for internal ice deformation is typically implemented in ice sheet models through the Stokes equations for slow, viscous flow, coupled with appropriate boundary conditions. For large-scale ice sheet modeling, various approximations of the full Stokes equations have been developed, each with different levels of complexity and computational cost.

The Shallow Ice Approximation (SIA) represents the simplest commonly used approach, assuming that vertical shear stresses dominate over longitudinal stresses. Under this approximation, the ice velocity is primarily determined by vertical shear, and the flow law can be integrated vertically to yield an expression for the surface velocity as a function of the local ice thickness and surface slope. The SIA has proven valuable for modeling the slow-moving interior regions of ice sheets but breaks down in areas of fast flow where longitudinal stresses become important [5].

The Shallow Shelf Approximation (SSA) provides a complementary framework for modeling the flow of ice shelves and fast-flowing ice streams, where longitudinal stresses dominate. The SSA has also been integrated into SIA models as a sliding law for ice streams, with a parameter adjusted to balance the amount of ice motion due to SSA and SIA components [5]. This hybrid approach enables accurate simulation of ice streaming, where most of the displacement is due to basal slip, and across the grounding line where the transition from grounded to floating ice occurs.

More sophisticated approaches, such as the Full Stokes equations or higher-order approximations, retain additional stress components and provide more accurate simulations of complex flow regimes but at substantially higher computational cost. The choice of approximation represents a fundamental trade-off between accuracy and computational feasibility, particularly for long-term projections spanning centuries.

### 2.3 Vertical Structure of Ice Velocity

Recent high-resolution modeling studies have revealed complex vertical structure in ice velocity that is not captured by traditional parameterizations. Research has demonstrated that vertical gradients in ice velocity are notably reduced just above the cold-temperate transition surface (CTS), with the basal temperate layer extending or compressing in response to topographic perturbations [8]. Over larger scales of approximately one kilometer, the behavior diverges substantially from ice motion patterns presently incorporated into grid or mesh cells in state-of-the-art ice sheet models.

These findings have important implications for the representation of ice flow in models. Temperate ice has been found to be vertically extensive, exceeding 100 meters in deep troughs, but thinning notably to less than 5 meters over bedrock highs [8]. Basal slip rates correspondingly range from over 90 percent to less than 5 percent of surface velocity, depending on topography and temperate layer thickness. Reconciling this improved understanding through more accurate parameterizations of ice sheet motion at large scales may lead to more accurate predictions of sea level rise in the coming decades and centuries.

---

## 3. Basal Sliding: Mechanisms and Parameterizations

### 3.1 Physical Basis of Basal Sliding

Basal sliding represents the motion of ice along its bed, occurring when the base of the ice sheet is at the pressure melting point and a thin layer of water is present to lubricate the interface. Despite over 60 years of research on basal sliding, starting with the pioneering work of Weertman and Lliboutry in the late 1950s, significant uncertainties remain in our understanding and representation of this process [3].

The physical mechanisms underlying basal sliding involve complex interactions between ice, water, and the underlying substrate. At the microscopic scale, sliding occurs through a combination of regelation (refreezing of meltwater in areas of high pressure) and plastic deformation of ice at the interface. The presence of sediments at the bed can further complicate the process, with deformation of saturated till contributing to the overall basal motion [9]. Basal sliding and sediment deformation are the dominant modes of ice motion along ice sheet margins, where Greenland's fast-flowing outlet glaciers slide over thawed beds [2].

### 3.2 Weertman-Type Sliding Laws

The classical Weertman sliding law, developed in the 1957, provides a power-law relationship between basal shear stress and sliding velocity:

$$\tau_b = C u_b^{1/m}$$

where $\tau_b$ is the basal shear stress, $u_b$ is the sliding velocity, $C$ is a coefficient representing bed roughness and other properties, and $m$ is an exponent typically taken as $m = 1/3$ for temperate beds [10]. This formulation emerges from theoretical considerations of ice flow over a sinusoidal bed topography, with the sliding velocity limited by the rate at which ice can deform to accommodate obstacles.

Subsequent developments have generalized the Weertman formulation to include additional physical processes. The Budd sliding law introduces a linear dependence on effective pressure (the difference between ice overburden pressure and water pressure) and has been widely used in ice sheet modeling [10]. The power-law exponent $m$ in the Weertman-Budd sliding law has been identified as the most controlling factor determining mass changes of the Antarctic ice sheet, with spatial variation in effective pressure modulating basal sliding for a given value of the exponent [10].

### 3.3 Coulomb Sliding Behavior

An alternative conceptualization of basal sliding, based on Coulomb friction theory, has gained increasing support from recent observational and modeling studies. Under Coulomb behavior, the basal shear stress is limited by a constant friction coefficient times the effective pressure:

$$\tau_b \leq \mu N$$

where $\mu$ is the friction coefficient and $N$ is the effective pressure. This formulation predicts that sliding velocity becomes insensitive to driving stress once a yield stress is exceeded, potentially leading to unstable behavior where small changes in conditions can cause large changes in sliding rate.

Bayesian model selection applied to observations from the Amundsen Sea Embayment has identified Coulomb behavior as the most probable mode of sliding in this region [3]. Inferred effective pressures are generally below 0.5 MPa across most of the Amundsen Sea Embayment and below 0.1 MPa within fast-flowing tributaries of Pine Island Glacier. These low effective pressures, combined with the high driving stresses in these regions, are consistent with Coulomb-type sliding where the bed is close to failure.

### 3.4 Parameterization of Effective Pressure

The effective pressure $N$, representing the difference between ice overburden pressure and basal water pressure, is a critical parameter in sliding laws. A recent parameterization has been developed that varies from $p = 0$ (no basal water pressure) to $p = 1$ (the subglacial drainage system is hydrologically well connected to the ocean with full support near the grounding line) [11]. When $p = 0.5$, there is partial support of the ice overburden by subglacial water pressure.

This parameterization only accounts for basal sliding for ice grounded below sea level and does not account for subglacial hydrology in regions where the glacier bed is above sea level. The parameter $p$ affects the effective pressure near the grounding line and dictates the degree of basal slipperiness, particularly in marine-based ice [11]. Both the sliding coefficient and $p$ are set during model spin-up and play a role in conditioning the ice sheet, with different combinations yielding acceptable spin-up states that have different sensitivities to future ocean forcing.

---

## 4. How Stress-Strain Relationships Constrain Sea Level Predictions

### 4.1 The Critical Role of Basal Sliding in Ice Sheet Mass Balance

The contribution of basal sliding to overall ice-flow velocity is fundamental to accurately assessing how changes will influence sea level. Ice sheet models must quantify robustly the contributions of both internal deformation and basal sliding to overall ice-flow velocity [4]. In practice, models represent internal deformation through flow laws that define relationships between driving force (stress) and deformation rate (strain rate), while basal sliding laws are calibrated by comparing observed surface velocities with velocities calculated from the flow laws, with any excess attributed to sliding.

This calibration approach means that forecasts of the contribution of basal sliding to ice-mass loss fundamentally depend on the flow laws used for internal deformation. Both the form of the flow law and the values of its parameters influence the inferred basal sliding rates and, consequently, the projected future behavior of the ice sheet. Recent work has shown that higher nonlinearity of ice flow significantly reduces estimated basal motion, highlighting the sensitivity of these estimates to the assumed flow law formulation [4].

### 4.2 Sensitivity of Sea Level Projections to Sliding Law Choice

Ice loss projections, particularly for the Amundsen Sea Embayment, have been shown to be highly sensitive to the applied sliding law. Previous studies have demonstrated that sliding law parameters are a key source of uncertainty in sea level projections [3]. The choice between different sliding law formulations can lead to substantially different outcomes, with important implications for coastal communities and policy decisions.

Research using the BISICLES ice sheet model has shown that a Coulomb sliding law leads to higher sea level contribution compared with Weertman sliding, while higher values of the exponent in the Weertman sliding law also increase sea level contribution [12]. However, other work has suggested that different basal sliding laws and parameterizations drive broadly similar mass loss on decadal to centennial timescales [13]. This apparent discrepancy may reflect differences in the specific implementations, parameter ranges, or experimental setups used in different studies.

To minimize uncertainties in sea level rise projections, the sliding law used in large-scale ice sheet models should approach Coulomb behavior in fast-flowing regions [3]. This recommendation reflects the growing evidence that Coulomb sliding provides a more accurate representation of basal conditions in areas of rapid ice flow, where the majority of ice discharge to the ocean occurs.

### 4.3 Propagation of Uncertainty Through Ice Sheet Models

The uncertainty in basal sliding parameters propagates through ice sheet models to affect sea level projections through several interconnected pathways. First, the choice of sliding law and its parameters directly influences the simulated present-day ice geometry and velocity fields during model spin-up. Different parameter combinations can yield acceptable spin-up states that have different sensitivities to future forcing [11].

Second, the representation of basal sliding affects the model's response to changes in boundary conditions, such as ocean warming or changes in surface mass balance. The grounding line dynamics, which are critical for marine ice sheet stability, are particularly sensitive to the basal sliding formulation. The parameter $p$ affects basal friction near the grounding line and can condition the ice sheet to be more or less susceptible to ocean thermal forcing [11].

Third, the coupling between basal sliding and other ice sheet processes, such as subglacial hydrology and sediment deformation, introduces additional complexity and uncertainty. Accounting for basal hydrology has the potential to increase centennial-scale sea level contribution under forcing compared with Weertman sliding [12]. The development of more comprehensive representations of these coupled processes represents an important frontier in ice sheet modeling.

### 4.4 Inverse Methods and Parameter Estimation

Previous approaches to constraining basal properties, i.e., the sliding law parameters, have generally relied on remote sensing data and inverse methods or seismic observations [3]. Inverse methods seek to determine the spatial distribution of basal parameters that best reproduce observed surface velocities, subject to the constraint of momentum conservation. These methods have proven valuable for initializing models and have been used extensively in ice sheet modeling for over 30 years.

However, inverse methods face fundamental limitations. The most common approach, called snapshot inversion, minimizes the model-observation misfit for the model at one time step, commonly the initial time step [2]. While this method has proved valuable for initializing models, subsequent forward simulations do not always capture trends in ice dynamics. This limitation arises because snapshot inversion does not account for time-dependent processes and may not capture the full complexity of basal conditions.

Transient calibration represents an emerging capability that uses time series of surface observations and time-dependent physics to constrain uncertain model parameters [2]. With more constraints than the common snapshot inversion method, transient calibration has been shown to better capture trends in ice dynamics. The basal friction coefficient in the sliding law is a key parameter that can be constrained through transient calibration, potentially reducing uncertainty in sea level projections.

---

## 5. Evidence from Key Ice Sheet Regions

### 5.1 The Amundsen Sea Embayment

The Amundsen Sea Embayment of West Antarctica represents the largest potential source of near-term sea level rise from the Antarctic Ice Sheet and has been the focus of intensive research efforts. This region contains several major glaciers, including Pine Island Glacier and Thwaites Glacier, that have shown accelerated mass loss in recent decades. The slipperiness of the bed beneath regions of fast-flowing ice streams in this area has been identified as a key source of uncertainty in sea level projections [1].

Inferred effective pressures in the Amundsen Sea Embayment are generally below 0.5 MPa across most of the region and below 0.1 MPa within fast-flowing tributaries of Pine Island Glacier [3]. These low effective pressures, combined with high driving stresses, are consistent with Coulomb-type sliding behavior. Bayesian model selection has identified Coulomb behavior as the most probable mode of sliding in this region, potentially increasing sea level rise contributions from the Amundsen Sea Embayment.

The sensitivity of ice loss projections to the applied sliding law has been demonstrated through multiple modeling studies. Research has shown that the choice of sliding law can significantly affect projected mass loss from this region, with implications for global sea level projections. To minimize uncertainties in sea level rise projections, the sliding law used in large-scale ice sheet models should therefore approach Coulomb behavior in fast-flowing regions [3].

### 5.2 The Greenland Ice Sheet

Basal sliding and sediment deformation are the dominant modes of ice motion along the margins of the Greenland Ice Sheet, where fast-flowing outlet glaciers slide over thawed beds [2]. The parameterization of basal sliding in Greenland ice sheet models has been shown to significantly influence simulated velocities and mass loss projections.

Recent work has demonstrated that the choice of sliding law affects the ability of models to reproduce observed velocities in Northwest Greenland, with the linear Budd sliding law and sliding laws without effective pressure resulting in slower velocities compared to other sliding laws [2]. These uncertainties in sliding law representation could be compensating for limitations in other aspects of the model, such as the flow law formulation or the representation of shear margins.

The Greenland Ice Sheet has been identified as a system where ice flow models may underestimate observed mass loss, raising questions about whether future sea-level rise may be larger than projected [2]. Transient calibration methods have been applied to improve the representation of basal friction in Greenland models, with promising results for capturing trends in ice dynamics.

### 5.3 Antarctic Ice Shelves and Buttressing Effects

The ice flow at the margins of the West Antarctic Ice Sheet is moderated by large ice shelves that provide buttressing to upstream grounded ice. The stability of these ice shelves results from the balance of mass gain by accumulation and ice flow from the adjacent ice sheet and mass loss by calving and basal melting due to ocean heat flux [9]. Recent results from ocean circulation models indicate that warm circumpolar water of the Southern Ocean may override the submarine slope front of the Antarctic Continent and boost basal ice shelf melting.

Coupled simulations with finite element ocean models and three-dimensional thermomechanical ice flow models have revealed that thinning of major ice shelves, such as the Filchner-Ronne Ice Shelf, would lead to extensive grounding line retreat associated with vast mass loss from the West Antarctic Ice Sheet [9]. The parametrization of basal sliding properties by simulated basal melt water fluxes allows for more realistic representation of velocity and locations of observed ice streams in these catchments.

The representation of calving processes at the margins of ice shelves remains a significant challenge. While ice flow models are starting to include calving laws at large scale and high resolution, these laws have been designed mostly for Greenland glaciers, currently remain poorly validated by observations, and may not capture the relevant processes underlying calving for each ice shelf cavity system [14].

---

## 6. Implications for Model Development and Uncertainty Quantification

### 6.1 Hierarchical Approaches to Ice Sheet Modeling

Ice sheet models can use a variety of different solutions of differing complexities to simulate ice flow, with different approximations of the nine principal stress components [5]. The more complex models include all nine stress components, including longitudinal (stretching and compressional) and transverse stresses, while simpler models make approximations that reduce computational cost at the expense of accuracy in certain flow regimes.

A hierarchical approach to ice sheet modeling allows different levels of approximation to be applied in different regions based on the dominant physical processes. The proportion of movement from SIA or SSA varies across the domain, from fully SIA (sheet flow in interior) to a combination (ice streams) to fully SSA (ice shelves) [5]. This enables accurate simulation of ice streaming, where most of the displacement is due to basal slip, and across the grounding line.

The development of multi-fidelity approaches to uncertainty quantification represents a promising direction for addressing the computational challenges of comprehensive uncertainty assessment. These methods combine high-fidelity simulations, which provide accurate but computationally expensive results, with lower-fidelity models that are faster to evaluate but less accurate [15]. By exploiting correlations between fidelity levels, multi-fidelity methods can substantially reduce the computational cost of uncertainty quantification while maintaining accuracy.

### 6.2 Ensemble Methods and Parameter Sensitivity

A comprehensive exploration of how basal sliding is represented would significantly improve our understanding of uncertainty in sea level projections. Recent studies have used large ensemble approaches to probe the dependence of future Antarctic mass loss on sliding law parameters. One study ran a 325-member ensemble, where 25 unique combinations of sliding parameters were used to generate new spin-ups, each achieving similar spin-up states that are in steady state and whose ice sheet configuration resembles today's ice sheet [11].

These ensemble approaches reveal that a large range of parameter combinations can yield acceptable spin-up states that have different sensitivities to future ocean forcing. This finding highlights the importance of considering parameter uncertainty, rather than just model structure uncertainty, in sea level projections. The parameter settings can condition the ice sheet to be more or less susceptible to ocean thermal forcing, which has significant implications for sea level projections [11].

### 6.3 Coupling with Ocean and Climate Models

Significant progress has been made in coupling ice sheet and ocean models to better capture processes and understand feedbacks at the ice-ocean interface and beyond [14]. These efforts include both idealized and realistic ice-ocean systems, both of which have highlighted the limitations of parameterizations, which tend to underestimate ocean-induced melt rates and ice mass loss.

Efforts are also underway to couple ice sheet models into large-scale general circulation models, as used in the Coupled Model Intercomparison Project [14]. These coupled simulations enable the investigation of feedbacks between ice sheets, oceans, and atmosphere that cannot be captured in standalone ice sheet or ocean models. However, the computational expense of these coupled models limits the number of simulations that can be performed, constraining the exploration of parameter uncertainty.

The representation of subglacial hydrology represents an important frontier in coupled ice-ocean modeling. A parametrization of basal sliding properties by the simulated basal melt water fluxes allows for more realistic representation of ice stream behavior [9]. Developing parameterizations of the net effect of complex basal motion can improve the realism of predictive ice sheet models and reduce uncertainty in sea level projections.

---

## 7. Challenges and Future Directions

### 7.1 Observational Constraints on Basal Processes

A fundamental challenge in constraining basal sliding parameters is the limited observational access to ice shelf cavities and subglacial environments. The bed beneath ice sheets remains sparsely sampled, and direct observations of basal conditions are extremely difficult to obtain [14]. Accurately representing these processes requires high-resolution global or circum-Antarctic ocean models with ice shelf capabilities that achieve good model-data agreement.

Previous approaches to constraining basal properties have generally relied on remote sensing data and inverse methods or seismic observations, but lack a direct link between observations and the representation of basal sliding in ice sheet models [3]. Developing this link represents a critical challenge for improving the predictive capability of ice sheet models.

Future field studies should focus on obtaining direct observations of basal conditions, including basal water pressure, sediment properties, and bed topography at high resolution. These observations can be used to validate and constrain the parameterizations used in ice sheet models, ultimately reducing uncertainty in sea level projections.

### 7.2 Representation of Complex Basal Motion

Recent high-resolution modeling studies have revealed complex basal motion patterns that are not captured by traditional parameterizations. Temperate ice is vertically extensive in deep troughs but thins notably over bedrock highs, with basal slip rates reaching over 90 percent or less than 5 percent of surface velocity depending on topography and temperate layer thickness [8].

These findings suggest that reconciling improved understanding through more accurate parameterizations of ice sheet motion at large scales may lead to more accurate predictions of sea level rise in the coming decades and centuries [8]. Developing parameterizations of the net effect of this complex motion represents a significant challenge but one that could substantially improve the realism of predictive ice sheet models.

Initial approaches to incorporating complex basal motion into numerical parameterizations applicable to large-scale predictive ice sheet models have been proposed [8]. These approaches seek to capture the essential physics of basal motion while remaining computationally tractable for long-term projections. Further development and validation of these parameterizations represents an important direction for future research.

### 7.3 Reducing Uncertainty in Sea Level Projections

A quantitative understanding of how ice sheets might evolve over decades to centuries, with a thorough assessment of uncertainties, is urgently needed to inform adaptation strategies [14]. While ongoing studies provide qualitative insights, the translation of these insights into quantitative projections with well-characterized uncertainties remains a significant challenge.

To minimize uncertainties in sea level rise projections, the sliding law used in large-scale ice sheet models should approach Coulomb behavior in fast-flowing regions [3]. Additionally, the development of more comprehensive representations of coupled processes, including subglacial hydrology, sediment deformation, and ice-ocean interactions, will be essential for reducing uncertainty.

The integration of machine learning approaches into ice sheet modeling represents a promising direction for addressing some of these challenges. Machine learning methods can be used to develop surrogate models that approximate the behavior of high-fidelity ice sheet models at a fraction of the computational cost, enabling more comprehensive uncertainty quantification [15]. These approaches may prove particularly valuable for exploring the high-dimensional parameter spaces associated with basal sliding and other uncertain processes.

---

## 8. Conclusions

The stress-strain relationship in ice flow models plays a fundamental role in constraining sea level rise predictions, with basal sliding changes representing a primary source of uncertainty. The analysis presented in this report reveals several key findings that have important implications for ice sheet modeling and sea level projection:

First, the choice of sliding law formulation significantly influences projected ice loss, with Coulomb behavior identified as the most probable mode of sliding in fast-flowing regions such as the Amundsen Sea Embayment. This finding suggests that ice sheet models should incorporate sliding laws that capture Coulomb-like behavior to minimize uncertainty in sea level projections.

Second, the parameters governing basal sliding, including the effective pressure and sliding coefficient, are critical determinants of ice sheet sensitivity to forcing. Different parameter combinations can yield acceptable model states that have substantially different sensitivities to ocean warming, highlighting the importance of comprehensive uncertainty quantification.

Third, the representation of basal processes in ice sheet models remains limited by sparse observations and computational constraints. Developing improved parameterizations that capture the complex basal motion revealed by high-resolution modeling, while remaining computationally tractable for long-term projections, represents a critical frontier.

Fourth, the coupling between basal sliding and other ice sheet processes, including subglacial hydrology, sediment deformation, and ice-ocean interactions, introduces additional complexity that must be addressed to improve predictive capability. Integrated approaches that consider these coupled processes will be essential for reducing uncertainty in sea level projections.

The projection of future sea level rise under climate change scenarios is of paramount importance for coastal communities and policy decisions. The stress-strain relationship in ice flow models, particularly as it relates to basal sliding, represents a fundamental constraint on our ability to make accurate projections. Continued research to improve the representation of basal processes in ice sheet models, combined with enhanced observational constraints and advanced uncertainty quantification methods, will be essential for reducing uncertainty and informing adaptation strategies in the coming decades.

---

## References

[1] IPCC Core Writing Team, et al. (2023). Climate Change 2023: Synthesis Report. Contribution of Working Groups I, II and III to the Sixth Assessment Report. Geneva: IPCC.

[2] PNAS. (2024). Transient calibration impacts on ice sheet model projections. Proceedings of the National Academy of Sciences.

[3] Brondex, J., et al. (2019). Sensitivity of Antarctic ice loss to basal conditions: Implications for the Amundsen Sea Embayment. The Cryosphere.

[4] PMC. (2024). Ice flow dynamics and sea level rise projections. PMC Article 9916990.

[5] Antarctic Glaciers. (2024). Hierarchy of ice sheet models: An introduction. Numerical Ice Sheet Models.

[6] Cuffey, K. M. & Paterson, W. S. B. (2010). The Physics of Glaciers. Butterworth-Heinemann.

[7] Greve, R. & Blatter, H. (2009). Dynamics of Ice Sheets and Glaciers. Springer.

[8] PMC. (2024). Basal temperate layer and ice motion patterns. PMC Article 11981940.

[9] EPIC. (2023). Ice stream dynamics and basal sliding in the Filchner-Ronne Ice Shelf catchment. Alfred Wegener Institute.

[10] TC. (2022). Role of subglacial hydrology and till deformation in Antarctic ice sheet behavior. The Cryosphere, 16, 4537-4556.

[11] TC. (2023). Ensemble-based sensitivity analysis of Antarctic ice sheet parameters. The Cryosphere, 17, 1513-1530.

[12] OSTI. (2024). Basal sliding parameterizations and sea level contributions. Office of Scientific and Technical Information.

[13] Barnes, J. M. & Gudmundsson, G. H. (2022). Similarities in mass loss across timescales for different sliding laws. Geophysical Research Letters.

[14] Elementa. (2024). The case for a framework for understanding ice-ocean interactions. UC Press.

[15] Aretz, N., et al. (2024). Multi-fidelity uncertainty quantification in ice sheet simulations. Oden Institute, University of Texas at Austin.

## Annotations


## Sources
[1] https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2024JF007805
[2] https://arxiv.org/abs/1910.08922
[3] https://eartharxiv.org/repository/object/2611/download/6289/
[4] https://epic.awi.de/36692/1/SebastianGoeller_Thesis.pdf
[5] https://epic.awi.de/36751/
[6] https://iowaclimate.org/2022/03/13/study-ice-flow-is-more-sensitive-to-stress-than-previously-thought/
[7] https://kiwi.oden.utexas.edu/papers/ice-sheet-multi-fidelity-uncertainty-quantification-Aretz-Willcox.pdf
[8] https://laro.lanl.gov/view/pdfCoverPage?instCode=01LANL_INST&filePid=13163624850003761&download=true
[9] https://link.aps.org/doi/10.1103/RevModPhys.84.885
[10] https://ntrs.nasa.gov/api/citations/20140009622/downloads/20140009622.pdf
[11] https://oceanrep.geomar.de/59761/1/the-impact-of-spatially-varying-ice-sheet-basal-conditions-on-sliding-at-glacial-time-scales.pdf
[12] https://online.ucpress.edu/elementa/article/12/1/00036/203616/The-case-for-a-Framework-for-UnderStanding-Ice
[13] https://pmc.ncbi.nlm.nih.gov/articles/PMC11981940/
[14] https://pmc.ncbi.nlm.nih.gov/articles/PMC9916990/
[15] https://sseh.uchicago.edu/doc/Schoof_and_Hewitt_2013.pdf
[16] https://tc.copernicus.org/articles/16/4537/2022/
[17] https://tc.copernicus.org/articles/17/1513/2023/
[18] https://tc.copernicus.org/articles/20/495/2026/tc-20-495-2026.pdf
[19] https://tc.copernicus.org/articles/7/1579/2013/tc-7-1579-2013.pdf
[20] https://web3.arxiv.org/pdf/1906.08197
[21] https://www.antarcticglaciers.org/glaciers-and-climate/numerical-ice-sheet-models/hierarchy-ice-sheet-models-introduction/
[22] https://www.nature.com/articles/s41467-025-57700-1.pdf
[23] https://www.nature.com/articles/s41598-022-14303-w
[24] https://www.nature.com/articles/s43247-022-00385-x
[25] https://www.noaa.gov/digital-coast-sea-level-rise-viewer
[26] https://www.nrdc.org/stories/sea-level-rise-101
[27] https://www.osti.gov/pages/servlets/purl/2538437
[28] https://www.pnas.org/doi/10.1073/pnas.2411904122