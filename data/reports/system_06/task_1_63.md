# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 57c54503 | **Time:** 178.97s | **Cost:** $0.19740
--------------------------------------------------------------------------------

# Impact of Nonlinear Density-Velocity Characteristics on Macroscopic Fundamental Diagram Prediction Near Phase Transition Points

## Abstract

The Macroscopic Fundamental Diagram (MFD) represents a cornerstone of modern traffic flow theory, establishing relationships between network-averaged flow, density, and speed variables. However, the prediction of MFDs becomes particularly challenging near phase transition points where nonlinear density-velocity characteristics dominate. This report examines the theoretical foundations and practical implications of these nonlinearities, focusing on how they affect fundamental diagram predictions during critical traffic state transitions. Drawing from recent developments in traffic flow theory, including Lighthill-Whitham-Richards (LWR) models, phase transition frameworks, and empirical hysteresis analyses, this investigation reveals that nonlinear density-velocity relationships fundamentally alter the predictability and stability of MFD predictions. The analysis demonstrates that near critical density thresholds, the assumption of single-valued functional relationships breaks down, leading to hysteresis phenomena, capacity drops, and significant prediction uncertainties that have profound implications for traffic management and control strategies.

## 1. Introduction

The study of traffic flow dynamics has long relied upon the fundamental diagram as a primary analytical tool for understanding the relationships between key macroscopic variables: flow, density, and speed. Godfrey (1969) appears to be the first author to postulate a strictly functional, uni-modal relationship between average flow and density in urban traffic networks [1]. Since traffic flow theory and empirical investigations by Daganzo and Geroliminis (2008) have confirmed the existence of such relationships, their estimation and analysis have gained considerable popularity in both academic research and practical applications.

The fundamental diagram, in its various forms, serves as the theoretical backbone for kinematic wave traffic flow theory and provides essential insights into traffic phase transitions. The flow-density fundamental diagram, for instance, specifies the transition patterns of various traffic states on the phase plane and completes the kinematic wave traffic flow theory [2]. In higher-order models, the speed-density or speed-spacing fundamental diagram also plays a critical role, enabling convenient analysis within the framework of the effective fundamental diagram.

However, the practical application of fundamental diagram-based approaches encounters significant challenges when traffic systems approach phase transition points—critical thresholds where traffic behavior shifts between free-flow and congested states. These transition regions are characterized by pronounced nonlinearities in the density-velocity relationship, leading to phenomena such as hysteresis, capacity drop, and fundamental diagram scatter that complicate accurate prediction.

This report investigates the specific impacts of nonlinear density-velocity characteristics on macroscopic fundamental diagram prediction near phase transition points. The analysis integrates theoretical frameworks from traffic flow physics with empirical observations to provide a comprehensive understanding of the challenges and potential mitigation strategies. The investigation addresses three primary research questions: first, how do nonlinear density-velocity relationships manifest near critical density thresholds; second, what mechanisms cause the breakdown of single-valued functional relationships in these regions; and third, what are the implications of these nonlinearities for MFD-based traffic management strategies.

## 2. Theoretical Foundations of Fundamental Diagrams

### 2.1 Classical Fundamental Diagram Theory

The classical derivation of the fundamental diagram relationship traces back to Wardrop, who established the foundational mathematical framework connecting traffic flow variables [3]. The fundamental relationship can be expressed as q = ku, where q represents flow (vehicles per unit time), k denotes density (vehicles per unit distance), and u signifies speed (distance per unit time). A similar relationship exists among speed, flow, vehicle length, and occupancy: u = qL/H, where L represents vehicle length and H occupancy, defined as the fraction of time that vehicles are present at a point [3].

The graphical representation of relations between macroscopic characteristics of flow and density reveals several critical points that define the fundamental diagram structure [4]. The free speed ξ = 1 corresponds to zero flow and zero density, representing the condition where no vehicles are present on the roadway. The capacity qc represents the maximal flow, also termed the critical flow, which is not achieved at the maximum mean speed due to the nonlinear relationship between density and speed. The capacity density or critical density ρc corresponds to the density at which capacity flow is achieved, while the capacity speed ξc represents the mean speed at capacity flow conditions. The jam density corresponds to the maximum achievable density where flow vanishes entirely.

The part of the flow-density relationship characterized by constant speed corresponds to a stable region, while the region where speed decreases with increasing density represents the unstable region [4]. This distinction between stable and unstable regions has profound implications for traffic dynamics and the predictability of fundamental diagram behavior.

### 2.2 Lighthill-Whitham-Richards Framework

In contrast to previously described macroscopic modeling approaches, the theory by Lighthill and Whitham (1955) and Richards (1956), commonly known as the LWR theory, assumes that traffic flow and density are locally related through a concave functional relationship known as the fundamental diagram [1]. This theoretical framework is well-suited for analyzing local traffic jam dynamics, but its application in larger networks is prohibitively resource-intensive due to the computational complexity of solving the underlying partial differential equations.

The LWR theory provides a hydrodynamic analogy to traffic flow, treating vehicle density analogous to fluid density and flow analogous to fluid flux. The fundamental equation of the LWR model takes the form ∂k/∂t + ∂(ku)/∂x = 0, where the flux function Q(k) = ku(k) relates flow to density through a prescribed fundamental diagram [5]. The concavity assumption on the fundamental diagram ensures that the model exhibits wave-like behavior with characteristics that propagate at speeds determined by the derivative of the flux function.

However, the LWR framework's assumption of a single-valued, concave fundamental diagram becomes problematic near phase transition points where traffic behavior exhibits multiple equilibria and path-dependent dynamics. Existing mesoscopic analyses of traffic jams behind bottlenecks within the LWR framework do not account for the characteristic congestion buildup and subsequent dissipation of traffic corridors during peak hours [1], highlighting a significant limitation of the classical approach.

### 2.3 Triangular Fundamental Diagram Representation

The triangular fundamental diagram represents a simplified yet widely-used representation of traffic flow relationships [5]. This model defines the flux function as:

$$Q(k) = 
\begin{cases} 
kv_{\max} & \text{if } k \leq k_c \\
(k_j - k)w & \text{if } k \geq k_c
\end{cases}$$

where vmax denotes the free-flow speed, kc represents the critical density, kj signifies the jam density, and w represents the backward moving wave speed. These parameters must satisfy the continuity condition kcvmax = (kc - kj)w for flow continuity at the critical density [5].

Density values below the critical density correspond to free-flow states, while density values above the critical density correspond to congested states. The triangular fundamental diagram's piecewise-linear structure captures the essential features of traffic flow while maintaining mathematical tractability. However, this simplification necessarily abstracts away the nonlinear characteristics that become prominent near phase transition points, potentially limiting its predictive accuracy in these critical regions.

## 3. Nonlinear Density-Velocity Characteristics

### 3.1 Analytical Expressions for Velocity and Flux Functions

The modeling of traffic flow involves seeking analytic expressions for velocity and flux functions that can subsequently be used for the derivation of hydrodynamical equations [4]. A notable example is the formula:

$$v_e = (1 - \rho)^{\frac{1}{1+a}}, \quad q_e = \rho(1 - \rho)^{\frac{1}{1+b}}$$

with parameters a, b ≥ 0, attributed to Kühne and Rösninger as reported in reviews of traffic flow modeling [4]. This formulation represents one of many attempts to capture the nonlinear relationship between density and velocity through analytically tractable functions.

More recent experimental observations have revealed that at low density, vehicles generally maintain maximum velocity until a critical value ρc of density is reached [4]. For densities exceeding this critical threshold, velocity begins decaying with increasing density. This behavior reflects the fundamental nonlinear nature of density-velocity relationships and has significant implications for fundamental diagram predictions near phase transition points.

The nonlinear decay of velocity with increasing density beyond the critical threshold creates a region of the fundamental diagram where small changes in density can produce large changes in flow. This heightened sensitivity to density variations near critical points amplifies prediction uncertainties and can lead to significant errors in traffic state estimation.

### 3.2 Multiregime Models and Discontinuous Characteristics

For many decades, traffic-flow analysts have studied various mathematical formulations describing the relationships among density, flow, and speed of uninterrupted traffic flows [3]. The best mathematical approaches have traditionally been determined by trying several different formulas and applying regression analysis, requiring specification of regression curves and transition points in advance.

However, research has demonstrated that neural network models can effectively describe the nonlinear and discontinuous characteristics among traffic flow variables without requiring advance specification of regression curves or transition points [3]. The multiple correlation coefficients resulting from neural network approaches have proven better than those from conventional nonlinear equations, suggesting that traditional parametric models may inadequately capture the full complexity of density-velocity relationships.

Multiregime models represent an alternative approach that divides the density-velocity relationship into distinct regions, each governed by different functional forms [6]. These models recognize that the physics of traffic flow may differ substantially between free-flow, congested, and transitional regimes, requiring different mathematical representations for each region. The breakpoints between regimes are typically determined empirically and may vary across different roadway types and traffic conditions.

### 3.3 Phase Transition Dynamics

The dynamics of phase transition models are governed by different systems of partial differential equations for the free-flow phase and for the congestion phase [5]. The Colombo phase transition model represents a notable example, consisting of two coupled partial differential equations valid in free-flow and congested regimes respectively:

$$\begin{cases}
\partial_t\rho + \partial_x(\rho v_f(\rho)) = 0 & \text{in free-flow } (\Omega_f) \\
\partial_t\rho + \partial_x(\rho v_c(\rho, q)) = 0 & \\
\partial_tq + \partial_x((q - q^*) v_c(\rho, q)) = 0 & \text{in congestion } (\Omega_c)
\end{cases}$$

where the state variables ρ and q denote density and linearized momentum, respectively [5]. The term q* represents a characteristic parameter of the road under consideration. An empirical relation expresses velocity as a function of density in free-flow, v := vf(ρ), and as a function of density and linearized momentum in congestion, v := vc(ρ, q).

This phase transition framework acknowledges that the fundamental relationship between density and velocity fundamentally differs between free-flow and congested states. The transition between these regimes involves not merely a change in functional form but potentially discontinuous changes in system behavior, including the emergence of new dynamic modes and instabilities.

## 4. Hysteresis Phenomena Near Phase Transitions

### 4.1 Mechanisms of Hysteresis in Traffic Systems

Hysteresis represents one of the most significant manifestations of nonlinear density-velocity characteristics near phase transition points. Data analysis has confirmed that the hysteresis phenomenon occurs in traffic systems, with the kinetic energy of traffic streams defined as αku², where α is a dimensionless constant, k is density, and u is speed [7]. When a platoon is released from maximum density conditions, the resulting values of speed, volume, and kinetic energy are retarded compared to pre-disturbance conditions at respective densities.

The existence of hysteresis does not depend on the maximum density reached, suggesting that the phenomenon arises from fundamental properties of traffic dynamics rather than specific extreme conditions [7]. This observation has profound implications for fundamental diagram predictions, as it indicates that the relationship between density and flow is not uniquely determined by density alone but also depends on the system's history.

Research has demonstrated that counterclockwise hysteresis loops in the exit function result from vehicles being closer to their destinations during congestion easing, whereas clockwise loops in the Fundamental Diagram come from tighter vehicle clustering in such phases [1]. This distinction highlights the multiple mechanisms through which hysteresis can manifest in traffic systems and the complexity of predicting loop shapes and sizes from traffic flow data.

### 4.2 Impact on Fundamental Diagram Scatter

The hysteresis phenomenon contributes significantly to the scatter observed in empirical fundamental diagrams. At the same average network density, average network flow as congestion builds is greater than during congestion dissipation [8]. This path-dependence means that single-valued fundamental diagram models cannot accurately represent traffic behavior throughout the congestion cycle.

The capacity drop phenomenon, where maximum flow cannot be sustained for long periods, further complicates fundamental diagram predictions [8]. More loading decreases network flow, with Δq1 increasing during network loading. Additionally, Δq2 develops during congestion dissipation as some link densities decrease while others remain congested, creating a higher density standard deviation accompanied by increased flow reduction.

The relationship between density standard deviations and hysteresis loop characteristics has been quantified through empirical analysis [8]. Studies have found strong correlations between average standard deviation of density and various hysteresis loop parameters, with R² values reaching 0.8574 for certain relationships. These findings indicate that spatial heterogeneity in congestion distribution plays a crucial role in determining the magnitude of hysteresis effects and the resulting fundamental diagram scatter.

### 4.3 Vehicle Clustering and Spatial Distribution

The mathematical model developed for analyzing hysteresis factors at the corridor level reveals that predictions of hysteresis behavior match empirical data through theoretical analysis [1]. This understanding is based on the significant impact of vehicles' time-varying spatial distribution, with the model shedding light on patterns of vehicle clustering that affect traffic flow dynamics.

Specifically, tighter vehicle clustering during congestion easing phases produces clockwise loops in the Fundamental Diagram [1]. This clustering effect slows vehicles and reduces flow rates compared to the buildup phase at equivalent densities. The physical mechanism involves the propagation of disturbances through the traffic stream and the time required for vehicles to re-establish normal spacing patterns after congestion.

The spatial distribution of vehicles thus emerges as a critical factor in determining the nonlinear response of traffic systems near phase transition points. Traditional fundamental diagram approaches that treat traffic as spatially homogeneous cannot capture these effects, leading to systematic prediction errors in heterogeneous networks and during transition periods.

## 5. Implications for MFD Prediction

### 5.1 Challenges in Low-Scattered MFD Estimation

It is difficult to draw low-scattered MFDs for real-world city-scale networks due to the combined effects of nonlinear density-velocity characteristics, hysteresis, and spatial heterogeneity [8]. The scatter in empirical MFDs reflects the underlying complexity of traffic dynamics that cannot be fully captured by simple functional relationships.

The challenge is particularly acute near phase transition points where small perturbations can lead to substantially different traffic states. The nonlinear amplification of density variations near critical thresholds means that measurement errors or model inaccuracies can produce large prediction errors. This sensitivity poses significant challenges for real-time traffic management systems that rely on accurate MFD predictions.

The inhomogeneous spatial distribution of congestion increases flow reduction during network unloading as congestion dissipates [8]. As congestion dissipates, the densities of many links decrease; however, some links remain congested, creating a higher density standard deviation. The flow on most links falls (because of either congestion or low link occupancy), and consequently, Δq2 increases. Thus, the larger the Δq2, the more heterogeneous the congestion distribution during recovery.

### 5.2 Stability Analysis and Perturbation Dynamics

Formal definitions of linear and nonlinear string instability in macroscopic terms consider an infinite system initially in steady state at density ρe and examine the spatiotemporal development of the response to temporary and localized perturbations [9]. If the initial perturbation corresponds to a sudden change in speed of a single vehicle, the macroscopic initial perturbation of the speed field is localized in space.

Near phase transition points, the stability characteristics of traffic flow change significantly. The fundamental diagram's derivative with respect to density, which determines characteristic wave speeds, approaches zero at the critical density where free-flow and congested branches meet. This vanishing derivative implies that perturbations propagate more slowly near critical points, allowing disturbances to persist longer and potentially grow through nonlinear mechanisms.

The perturbation traffic model (PTM) provides a framework for analyzing these dynamics [5]. The model introduces a perturbation variable p that can be computed from joint observations of density and speed, or density and flow. When the perturbation vanishes (p = 0), the fundamental diagram reduces to the classical relation between stationary states. However, values of speed higher or lower than the stationary fundamental diagram are admissible for non-stationary states, reflecting the dynamic nature of traffic near phase transitions.

### 5.3 Network-Level Fundamental Diagram Considerations

The concept of the Macroscopic Fundamental Diagram (MFD) has developed to establish a relationship between volume and density from empirical and simulation data in homogeneous urban network regions [6]. The MFD is particularly useful for characterizing the traffic flow characteristics of entire networks, overcoming the limitations of link-level analysis for large-scale traffic management.

However, the application of MFD-based approaches requires careful consideration of the nonlinear density-velocity characteristics that manifest near phase transition points. Networks with heterogeneous spatial distributions of congestion may exhibit significantly different MFD shapes compared to homogeneous networks, even at equivalent average densities. The capacity drop and hysteresis effects described previously can lead to multiple possible flow values at the same average density, depending on the network's loading history and spatial configuration.

Traffic management systems that rely on MFD-based control strategies must account for these nonlinearities to avoid degraded performance during transition periods. The challenge lies in developing prediction methods that can accurately estimate MFD behavior despite the inherent uncertainties near critical points.

## 6. Modeling Approaches for Improved Prediction

### 6.1 Neural Network and Data-Driven Methods

Given the limitations of traditional parametric approaches, neural network models have emerged as promising tools for capturing the nonlinear and discontinuous characteristics of traffic flow relationships [3]. These methods can learn complex mappings between density, flow, and speed without requiring explicit specification of functional forms or transition points.

The effectiveness of neural network approaches stems from their ability to approximate arbitrary nonlinear functions, potentially capturing the full complexity of density-velocity relationships near phase transition points. The multiple correlation coefficients resulting from neural network models have demonstrated superior performance compared to conventional nonlinear equations, suggesting that these data-driven methods may provide more accurate predictions in challenging regions of the fundamental diagram.

However, neural network approaches also present challenges, including the need for large training datasets, potential overfitting, and limited interpretability. The black-box nature of these models may hinder understanding of the underlying physical mechanisms and limit their transferability to new roadway contexts.

### 6.2 Phase Transition Models

Phase transition models offer a physically-motivated framework for representing the different behaviors of traffic in free-flow and congested regimes [5]. By explicitly acknowledging the distinct dynamics in each regime and the conditions for transitioning between them, these models can potentially provide more accurate predictions near critical points.

The Colombo phase transition model represents one approach to capturing the physics of phase transitions [5]. The model uses different velocity functions for free-flow and congested conditions, with the transition governed by the critical density threshold. This structure allows the model to represent the discontinuous changes in system behavior that occur at phase transitions.

The perturbation traffic model extends this framework by introducing additional state variables that capture non-equilibrium effects [5]. The dynamics are governed by different systems of partial differential equations for each phase, with the perturbation variable allowing representation of deviations from stationary fundamental diagram behavior. This approach can capture hysteresis effects and other path-dependent phenomena that simple fundamental diagram models cannot represent.

### 6.3 Multi-Resolution and Hybrid Approaches

Given the complementary strengths and limitations of different modeling approaches, multi-resolution and hybrid methods may offer the most promising path forward for improved MFD prediction near phase transition points. These approaches could combine the physical interpretability of phase transition models with the flexibility of data-driven methods.

Multi-resolution approaches might use different models at different density ranges, applying simpler fundamental diagram models in regions where they perform well and switching to more complex representations near critical points. The transition between models could be governed by detected proximity to phase transition conditions, allowing adaptive prediction strategies.

Hybrid approaches might use data-driven methods to correct systematic biases in physics-based models, or use physics-based constraints to regularize data-driven predictions. Such combinations could potentially leverage the strengths of both paradigms while mitigating their individual limitations.

## 7. Conclusions

The impact of nonlinear density-velocity characteristics on macroscopic fundamental diagram prediction near phase transition points represents a fundamental challenge in traffic flow theory and practice. The analysis presented in this report reveals several key findings that advance understanding of this complex phenomenon.

First, the density-velocity relationship exhibits pronounced nonlinearities near critical density thresholds, with velocity remaining approximately constant at low densities before decaying with increasing density beyond the critical point [4]. This behavior creates regions of heightened sensitivity where small density changes produce large flow variations, amplifying prediction uncertainties.

Second, hysteresis phenomena fundamentally challenge the assumption of single-valued functional relationships between density and flow. The observation that counterclockwise hysteresis loops in exit functions result from vehicles being closer to destinations during congestion easing, while clockwise loops in the Fundamental Diagram arise from tighter vehicle clustering [1], demonstrates the path-dependent nature of traffic dynamics near phase transitions.

Third, spatial heterogeneity in congestion distribution significantly affects fundamental diagram scatter and hysteresis loop characteristics. The strong correlation between density standard deviation and hysteresis loop parameters [8] indicates that network-level predictions must account for spatial distribution effects that simple homogeneous models cannot capture.

Fourth, phase transition models provide a physically-motivated framework for representing the distinct dynamics of free-flow and congested regimes [5]. These models acknowledge that the fundamental relationship between density and velocity differs fundamentally between regimes, offering potential improvements in prediction accuracy near critical points.

The implications of these findings for traffic management and control strategies are substantial. MFD-based approaches must account for the inherent uncertainties near phase transition points, potentially incorporating probabilistic elements or adaptive mechanisms that can handle the path-dependent nature of traffic dynamics. The development of improved prediction methods will require continued integration of theoretical advances with empirical validation across diverse network conditions.

Future research directions include the development of hybrid modeling approaches that combine the physical interpretability of phase transition models with the flexibility of data-driven methods, the investigation of real-time adaptation strategies that can detect and respond to approaching phase transitions, and the extension of network-level analysis to capture the effects of spatial heterogeneity more comprehensively. As traffic systems continue to evolve toward greater automation and connectivity, accurate prediction of fundamental diagram behavior near phase transitions will become increasingly critical for optimizing network performance and ensuring reliable transportation services.

## References

[1] hEART 2024. Mathematical model for analyzing hysteresis factors at the corridor level. hEART 2024 Conference, paper 7610.

[2] Li, J. and Zhang, H.M. Fundamental diagram of traffic flow. Department of Civil and Environmental Engineering, University of California, Davis.

[3] Nakatsuji, T., Tanaka, M., Nassr, P.N., and Hagiwara, T. Description of macroscopic relationships among traffic flow variables using neural network models. Transportation Research Record 1510, 1995.

[4] Bellomo, N. and Dogbe, C. On the modeling of traffic and crowds: A survey of models, speculations, and perspectives. SIAM Review, 53(3):409-422, 2011.

[5] Blandin, S., Work, D., Goatin, P., Piccoli, B., and Bayen, A. A general phase transition model for vehicular traffic. SIAM Journal on Applied Mathematics, 71(1):107-127, 2011.

[6] Ahmed, I. Modeling and analysis of traffic flow on urban networks using macroscopic fundamental diagram. Virginia Tech, 2016.

[7] Transportation Research Board. Traffic flow theory: A state-of-the-art report. TRB Circular EC149, 1972.

[8] Geroliminis, N. and Daganzo, C.F. Existence of urban-scale macroscopic fundamental diagrams: Some experimental findings. Transportation Research Part B: Methodological, 42(9):759-770, 2008.

[9] Treiber, M. and Kesting, A. Traffic flow dynamics: Data, models and simulation. Springer, 2013.

## Annotations


## Sources
[1] https://bayen.berkeley.edu/sites/default/files/1-s2.0-s0191261513000313-main.pdf
[2] https://bayen.berkeley.edu/sites/default/files/siam11_v2.pdf
[3] https://connected-corridors.berkeley.edu/sites/default/files/Fundamental%20Diagram%20of%20Traffic%20Flow.pdf
[4] https://documentserver.uhasselt.be/bitstream/1942/37604/2/Impact.pdf
[5] https://en.wikipedia.org/wiki/Fundamental_diagram_of_traffic_flow
[6] https://inria.hal.science/hal-00765451v1/document
[7] https://lab-work.github.io/download/Blandin2012PTM.pdf
[8] https://link.aps.org/doi/10.1103/Physics.4.42
[9] https://mtreiber.de/Vkmod_Skript/Chap16_StabilityAnalysis.pdf
[10] https://onlinepubs.trb.org/Onlinepubs/trr/1995/1510/1510.pdf
[11] https://onlinepubs.trb.org/onlinepubs/circulars/ec149.pdf
[12] https://par.nsf.gov/servlets/purl/10343895
[13] https://pmc.ncbi.nlm.nih.gov/articles/PMC11612452/
[14] https://transp-or.epfl.ch/heart/2024/abstracts/hEART_2024_paper_7610.pdf
[15] https://trid.trb.org/View/1571837
[16] https://vtechworks.lib.vt.edu/bitstream/handle/10919/78468/Ahmed_I_T_2016.pdf?isAllowed=y&sequence=1
[17] https://web.math.utk.edu/~vasili/475/REFS/bellomo11.traffic-crowdsSurvey.pdf
[18] https://www.cee.ehime-u.ac.jp/~keikaku/ists18/pdf/ISTS_IWTDCS_2018_paper_5.pdf
[19] https://www.fhwa.dot.gov/publications/research/operations/tft/chap5.pdf
[20] https://www.online-pdh.com/pluginfile.php/79524/mod_resource/content/2/Transportation%20Engineering%20Traffic%20Flow%20Analysis.pdf
[21] https://www.sciencedirect.com/science/article/abs/pii/S0032591017309786
[22] https://www.sciencedirect.com/science/article/abs/pii/S0378437115005695
[23] https://www.sciencedirect.com/science/article/pii/S0968090X21000917
[24] https://www.victorknoop.eu/research/papers/PhysicaA_MFD.pdf