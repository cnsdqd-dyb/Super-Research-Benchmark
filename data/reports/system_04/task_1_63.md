# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 614cc5e2 | **Time:** 334.28s | **Cost:** $1.35585
--------------------------------------------------------------------------------

# The Impact of Nonlinear Density-Velocity Characteristics on Macroscopic Fundamental Diagram Prediction Near Phase Transition Points

### Key Points
*   **Nonlinearity Induced Instability:** The relationship between traffic density and velocity is inherently nonlinear, particularly near the critical density (phase transition point). This nonlinearity is the primary driver of macroscopic instability, leading to phenomena such as the "capacity drop," where the queue discharge rate is significantly lower than the free-flow capacity [cite: 1, 2].
*   **Hysteresis and Path Dependence:** Prediction accuracy near phase transitions is severely compromised by hysteresis loops. The Macroscopic Fundamental Diagram (MFD) is not a single-valued function in the congested regime; rather, the network production depends on the spatial distribution of congestion (inhomogeneity). This is often described as the "nucleation effect," where congestion concentrates around bottlenecks, reducing network performance during the loading phase compared to the unloading phase [cite: 3, 4].
*   **Bifurcation of Traffic States:** Near the critical density, the traffic system undergoes bifurcation, where the system can evolve into multiple distinct equilibrium states (e.g., congested vs. uncongested branches) based on minor perturbations or initial conditions. This makes deterministic prediction challenging and necessitates stochastic or multi-regime modeling approaches [cite: 5, 6].
*   **Metastability and Critical Perturbations:** Theoretical analyses reveal ranges of density where traffic flow is metastable. In these regions, small disturbances fade away, but perturbations exceeding a critical amplitude trigger a breakdown into congested phases. This nonlinear stability characteristic creates a "zone of uncertainty" for MFD prediction near the tip of the diagram [cite: 7, 8].
*   **Inhomogeneity as a Predictor:** To improve prediction accuracy near phase transitions, the standard 2D MFD (Flow vs. Density) is insufficient. Research advocates for a Generalized Macroscopic Fundamental Diagram (GMFD) that incorporates the spatial variance of density (inhomogeneity) as a third dimension, thereby resolving the scatter and hysteresis observed in empirical data [cite: 3, 9].

---

## 1. Introduction

The Macroscopic Fundamental Diagram (MFD) has emerged as a pivotal tool in traffic flow theory and network management. It postulates a crisp, low-scatter relationship between the average network density (accumulation) and the average network flow (production) or speed [cite: 5, 10]. While the MFD provides a robust framework for monitoring and controlling urban traffic under homogeneous conditions, its predictive capability degrades significantly near phase transition points—specifically, the critical density where traffic shifts from a stable free-flow state to an unstable congested state.

The core of this predictive challenge lies in the nonlinear characteristics of the density-velocity relationship. Unlike fluid dynamics where higher loads typically yield higher flows, traffic dynamics exhibit a fundamental breakdown where exceeding a critical load reduces performance [cite: 3]. This report provides an exhaustive analysis of how these nonlinearities manifest as capacity drops, hysteresis loops, and bifurcations, and how they impede the accurate prediction of network states.

### 1.1 The Ideal vs. The Real MFD
In an idealized scenario, the MFD is a concave, single-valued function. However, empirical and simulation-based research demonstrates that the congested branch of the MFD is often multi-valued and exhibits high scatter [cite: 1, 11]. This scatter is not merely measurement noise but a reflection of the underlying nonlinear dynamics and the spatial heterogeneity of traffic. The transition from free-flow to congestion is not a smooth curve but a complex phase transition characterized by discontinuities and path-dependence [cite: 2, 4].

### 1.2 Scope of Analysis
This report synthesizes findings on the nonlinear stability analysis of traffic flow, the "nucleation effect" of congestion, and the mathematical derivation of critical perturbation amplitudes. It explores how these microscopic and mesoscopic nonlinearities aggregate to form complex macroscopic patterns, necessitating advanced modeling techniques such as the Generalized MFD (GMFD) and volume-delay differential equations [cite: 9, 12].

---

## 2. Theoretical Foundations of Nonlinear Density-Velocity Relationships

The fundamental diagram is derived from the basic hydrodynamic relation $q = k \cdot u$, where $q$ is flow, $k$ is density, and $u$ is speed [cite: 2]. The nonlinearity of the $u(k)$ relationship is the mathematical root of phase transitions in traffic flow.

### 2.1 The Speed-Density Function
Empirical observations confirm that as density increases, speed decreases nonlinearly. At low densities, interactions between vehicles are rare, and speed remains near the free-flow velocity ($u_f$). As density approaches the critical value ($k_c$), vehicle interactions become frequent, leading to a rapid, nonlinear decay in speed.
Mathematical models, such as the logistic speed-density models, attempt to capture this behavior by introducing parameters that reflect the "goodness" of traffic and driver response times [cite: 13]. However, in the congested phase, the flux can hardly be approximated by a single-valued function of density due to the statistical variability of driver behaviors and the formation of local slowdowns, often referred to as "phantom traffic jams" [cite: 1].

### 2.2 Phase Transition Mechanisms
The transition from free-flow to congestion is a phase transition analogous to those in thermodynamics.
*   **Free Phase:** Below critical density, the flow is stable. Perturbations (e.g., a vehicle braking) are dampened and dissipate.
*   **Congested Phase:** Above critical density, the flow becomes unstable or metastable. Small perturbations can amplify, propagating upstream as shockwaves [cite: 14].
*   **The Critical Point:** The peak of the MFD represents the maximum network capacity. Prediction near this point is precarious because the system is sensitive to initial conditions. A slight increase in density can trigger a "collapse" into the congested regime, characterized by a sudden drop in flow [cite: 1, 2].

### 2.3 Mathematical Formulation of Instability
Macroscopic models often utilize partial differential equations (PDEs) to describe these dynamics. For instance, the Lighthill-Whitham-Richards (LWR) model uses a nonlinear density-velocity relationship yielding a quasi-linear first-order hyperbolic PDE [cite: 15, 16]. The stability of the numerical solutions to these PDEs (e.g., using the Lax-Friedrichs scheme) reveals that the nonlinear terms are responsible for the formation of shockwaves and discontinuous solutions, which correspond to the sudden phase transitions observed in real traffic [cite: 17, 18].

---

## 3. The Capacity Drop Phenomenon

One of the most significant impacts of nonlinear density-velocity characteristics on MFD prediction is the "capacity drop." This phenomenon refers to the observation that the discharge flow rate from a queue is lower than the capacity of the road before the queue formed [cite: 2].

### 3.1 Mechanism of Capacity Drop
The capacity drop creates a discontinuity in the fundamental diagram near the critical density.
*   **Free-Flow Capacity ($q_{c1}$):** The maximum flow achievable when approaching capacity from the uncongested side.
*   **Queue Discharge Capacity ($q_{c2}$):** The maximum flow achievable once congestion has set in.
Research indicates that $q_{c2}$ can be significantly lower than $q_{c1}$, creating a "reverse lambda" shape or a discontinuity in the MFD [cite: 2]. This drop is driven by the bounded acceleration of vehicles and the reaction times of drivers leaving a jam. Macroscopic models that fail to account for this nonlinearity will overestimate the network's performance once the phase transition occurs [cite: 19].

### 3.2 Impact on Prediction Accuracy
Standard MFD models that assume a continuous, concave curve (like a parabola or triangle) fail to predict the capacity drop. When the system hovers near the critical density, a predictive model might forecast a return to high flow, whereas the nonlinear reality dictates a drop to a lower efficiency state.
*   **Bifurcation at Capacity:** The system effectively faces a bifurcation point. Depending on whether a perturbation triggers the capacity drop, the system trajectory will diverge significantly. This has been modeled using modified Cell Transmission Models (CTM) that introduce a jam-density discharge flow rate as a distinct parameter [cite: 19].
*   **Empirical Evidence:** Studies on freeway merges and arterial networks confirm that this drop is not an artifact but a reproducible feature of the nonlinear interactions between density and velocity [cite: 19].

---

## 4. Hysteresis and the Nucleation Effect

While the capacity drop describes a reduction in maximum flow, **hysteresis** describes the path-dependence of the traffic state. The relationship between flow and density is different during the onset of congestion (loading) compared to the dissipation of congestion (unloading).

### 4.1 The Nucleation Effect
The primary driver of hysteresis in the MFD is the "nucleation effect" [cite: 3, 4].
*   **Loading Phase:** As vehicles enter the network, congestion does not spread uniformly. Instead, it "nucleates" or concentrates around specific bottlenecks. The rest of the network may remain relatively free-flowing. This allows the network to maintain a higher average flow for a given average density.
*   **Unloading Phase:** As demand decreases, the congestion that has formed takes time to dissipate. The high-density pockets (nuclei) persist and may even spread (spillback) before clearing. This results in a highly inhomogeneous distribution of density.
*   **Impact on Flow:** Due to the concavity of the fundamental diagram (Jensen's inequality), a heterogeneous distribution of density yields a lower average flow than a homogeneous distribution with the same average density [cite: 20]. Consequently, the unloading branch of the MFD typically lies *below* the loading branch, forming a clockwise hysteresis loop [cite: 21, 22].

### 4.2 Generalized Macroscopic Fundamental Diagram (GMFD)
To address the prediction errors caused by hysteresis, researchers have proposed the GMFD.
*   **3D Relationship:** The GMFD posits that network production ($P$) is a continuous function of both accumulation ($A$) and the spatial inhomogeneity of density ($\sigma$): $P = f(A, \sigma)$ [cite: 3, 9].
*   **Resolving Scatter:** By including inhomogeneity as a variable, the scatter observed in the 2D MFD can be explained. The "noise" is actually a projection of the 3D surface onto the 2D plane.
*   **Predictive Power:** The GMFD allows for accurate prediction even during phase transitions. If the model knows the current level of inhomogeneity (which spikes during phase transitions), it can predict the lower flow rates associated with the hysteresis loop [cite: 4].

### 4.3 Types of Hysteresis Loops
*   **Clockwise Loops:** The most common form, observed when congestion is more evenly distributed during the loading phase than the unloading phase [cite: 21].
*   **Counter-Clockwise Loops:** Can occur in specific metrics like trip completion rates or under specific network topologies where congestion clears rapidly from the periphery [cite: 21].
*   **Determinants:** The shape and direction of the loop are determined by the network topology, control strategies, and the "fragile-robust-antifragile" nature of the traffic dynamics [cite: 23].

---

## 5. Stability Analysis and Metastability

The prediction of traffic states near phase transitions is further complicated by the phenomenon of metastability. Nonlinear stability analysis reveals that there are density ranges where the traffic state is neither purely stable nor purely unstable.

### 5.1 Critical Perturbation Amplitudes
Analytical investigations into traffic flow models (e.g., the optimal velocity model) identify specific critical densities ($\rho_{c1}, \rho_{c2}, \dots$) [cite: 7].
*   **Linearly Unstable Regime:** In some density ranges, any perturbation, no matter how small, will grow and cause a breakdown.
*   **Metastable Regime:** In other ranges (typically near the phase transition), the flow is stable against small perturbations but unstable against large ones.
*   **Critical Amplitude:** There exists a critical amplitude $\Delta \rho_c$. If a disturbance $\Delta \rho < \Delta \rho_c$, the flow recovers. If $\Delta \rho > \Delta \rho_c$, a traffic jam forms [cite: 7, 8].

### 5.2 Implications for MFD Prediction
This metastability implies that the MFD is not deterministic near the critical density.
*   **Probabilistic Nature:** A specific density value does not guarantee a specific flow rate. The outcome depends on the magnitude of external disturbances (e.g., a truck changing lanes, a brief distraction).
*   **Zone of Uncertainty:** Prediction models must account for this "zone of uncertainty" where the system can flip between free-flow and congested states stochastically. This is often modeled using stochastic differential equations or by defining the MFD as an envelope of possible states rather than a single line [cite: 11].

### 5.3 Bifurcation Theory
The transition between these states can be mathematically described as a bifurcation.
*   **Saddle-Node and Pitchfork Bifurcations:** As control parameters (like driver reaction time or density) change, the number and stability of equilibrium points change. For example, a stable equilibrium (free flow) might split into a stable (jammed) and unstable state [cite: 24, 25].
*   **AM/PM Bifurcation:** Empirical studies have detected bifurcations in the MFD shape itself, where the network exhibits different patterns during the morning (AM) and evening (PM) peaks. This is attributed to different driver behaviors (route choice efficiency) and demand patterns, effectively creating two different MFDs for the same network [cite: 6, 26].

---

## 6. Methodological Approaches to Improving Prediction

Given the impacts of nonlinearity, hysteresis, and instability, researchers have developed advanced methodologies to improve MFD prediction accuracy near phase transitions.

### 6.1 Data Fusion and Observability
Accurate prediction requires accurate estimation of the current state. Traditional loop detectors often fail to capture the spatial average density required for MFDs, leading to bias [cite: 12].
*   **Volume-Delay MFD (MFD-VD):** A new model derives a first-order, nonlinear implicit ODE relating network accumulation to the average congestion index (delay). This model utilizes data from License Plate Cameras (LPC) and Road Congestion Indices (RCI) [cite: 12].
*   **Observability-Invariant Property:** A crucial theoretical finding is that the ratio of traffic volume to the critical volume (at the MFD peak) is independent of the penetration rate of the sensors. This allows for robust estimation of the phase transition point even with partial data [cite: 12].

### 6.2 The Enveloping MFD
To handle the high scatter caused by nonlinear dynamics, some researchers propose modeling the "Enveloping MFD." Instead of fitting a curve through the mean of the scatter, this approach identifies the upper boundary of the flow-density points. This represents the maximum potential performance of the network and serves as a more stable target for control strategies [cite: 11].

### 6.3 Machine Learning and Nonlinear Approximation
Given the complexity of the analytical functions required to describe these nonlinearities, data-driven approaches are gaining traction.
*   **Neural Networks:** Multi-layer perceptrons (MLP) and other neural network architectures are used to capture the nonlinear interactions between density, speed, and viscosity (in fluid analogies) or flow. These models can learn the shape of the hysteresis loops and the capacity drop from historical data without requiring explicit physical derivation [cite: 27, 28].
*   **Graph Attention Networks:** Advanced models integrate network topology with traffic data to estimate individual link speeds and aggregate them into a more accurate network-wide state, overcoming the limitations of assuming homogeneity [cite: 29].

---

## 7. Conclusion

The impact of nonlinear density-velocity characteristics on MFD prediction near phase transition points is profound and multifaceted. The nonlinearity is not merely a statistical nuisance but the physical engine driving **capacity drops**, **hysteresis loops**, and **bifurcations**.

1.  **Predictive Uncertainty:** Near the critical density, the assumption of a one-to-one mapping between density and flow breaks down. The system becomes metastable, where the future state depends heavily on the magnitude of perturbations and the spatial distribution of density (nucleation).
2.  **Necessity of Higher-Order Models:** Simple 2D MFDs are insufficient for precise control near phase transitions. The inclusion of inhomogeneity (GMFD) or the use of history-dependent models (hysteresis tracking) is essential to reduce prediction error.
3.  **Control Implications:** Traffic management strategies (e.g., gating, perimeter control) must be designed to be robust against these nonlinearities. They should aim to keep the network slightly below the critical density to avoid the risk of triggering the capacity drop or entering the metastable regime where recovery is difficult due to hysteresis.

In summary, the "crisp" MFD is a useful approximation for stable regimes, but accurate prediction near phase transitions requires a rigorous accounting of the nonlinear, dynamic, and spatially heterogeneous nature of traffic flow.

---

## References

*   **[cite: 5]** Impact of nonlinear density-velocity characteristics on macroscopic fundamental diagram prediction near phase transition points.
*   **[cite: 3]** Generalized Macroscopic Fundamental Diagram: A continuous function of density and spatial inhomogeneity.
*   **[cite: 12]** Macroscopic fundamental diagram with volume-delay relationship: model derivation and empirical validation.
*   **[cite: 1]** Kinetic models of traffic flow and phase transitions.
*   **[cite: 2]** Fundamental diagrams: Capacity drop and queue discharge.
*   **[cite: 14]** Macroscopic fundamental diagrams for railway systems.
*   **[cite: 10]** Fundamental diagram of traffic flow: Basic statements and relationships.
*   **[cite: 23]** Mapping MFD regions to fragile-robust-antifragile spectrum.
*   **[cite: 19]** Experimental observations of capacity drop phenomena in freeway merges.
*   **[cite: 7]** Analytical Calculation of Critical Perturbation Amplitudes and Critical Densities.
*   **[cite: 8]** Nonlinear stability analysis of traffic flow models.
*   **[cite: 21]** Hysteresis patterns in Macroscopic Fundamental Diagrams.
*   **[cite: 22]** Relationship between inhomogeneous vehicle distribution and hysteresis loops.
*   **[cite: 30]** Impacts of driver relaxation and anticipation on traffic hysteresis.
*   **[cite: 13]** Modeling of speed-density relationship based on logistic curve.
*   **[cite: 15]** Finite difference scheme for macroscopic traffic flow model with nonlinear density-velocity.
*   **[cite: 17]** Numerical Simulation of Multilane Traffic Flow Model.
*   **[cite: 18]** Analysis and Simulation of Vehicle Velocity Density Function.
*   **[cite: 16]** Analytical and grid-free solutions to the LWR traffic flow model.
*   **[cite: 31]** Bifurcation structures in large populations of active rotators.
*   **[cite: 24]** Bifurcation diagrams and qualitative behavior changes.
*   **[cite: 32]** Two-Dimensional Bifurcation Diagram and phase changes.
*   **[cite: 25]** Bifurcation and Criticality in nonequilibrium systems.
*   **[cite: 11]** Modeling the Enveloping Macroscopic Fundamental Diagram.
*   **[cite: 29]** Deep learning for traffic speed estimation and prediction.
*   **[cite: 27]** Accurate prediction of density and viscosity using data-driven modeling.
*   **[cite: 28]** Support vector regression for nonlinear system modeling.
*   **[cite: 20]** Macroscopic Fundamental Diagram: Aggregation and scatter.
*   **[cite: 12]** Macroscopic fundamental diagram with volume-delay relationship (MFD-VD).
*   **[cite: 4]** The nucleation effect and Generalized MFD.
*   **[cite: 9]** Two dimensional generalization of the MFD and nucleation effect.
*   **[cite: 33]** Routing strategies based on Generalized MFD.
*   **[cite: 6]** Bifurcation in MFD: AM vs PM patterns.
*   **[cite: 26]** Empirical evaluation of influential factors on bifurcation in MFDs.
*   **[cite: 16]** Analytical solutions to LWR model with nonlinear density-velocity.
*   **[cite: 20]** Chapter 11: Macroscopic Fundamental Diagram and inhomogeneity.

**Sources:**
1. [unito.it](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3XdJCL6GFu4D41jtTDCwPopAkRZpSwvWcqWJons7Y2CTeeTDrKDZD77yAk0RXUDeWf9IKLfVxSi3eW4o6QZVtoAMonxDwF9gfSl_ECQY9i9hXkOUtAIUBCLeK4GfWk4T95ZbX7gtTaETSKmXnpjm9TAoZowM3wpuUx8Q_rpkbnEqkClNFzP4=)
2. [tudelft.nl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqP5XYiMrSYLtbXXLfj1hpPb1K3vjQuZLtMLs5ckAtXpcWI7_j-wyUHus_rVLs4Tqqi6AXSjYMxx4wNmnkzyq2D-NIaPzAlncPJAKoL4ws6oCtES83gFNfF8Y9qCOGZJpVe_SyIwyIzPWo0HASV-_kFNUkOFhzcW7dBSKORAeN2i8XFQ==)
3. [victorknoop.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgRIf_oxthAWjkaxSSBR2ZBufY2wInoDknktUGNcS01yPM-xK6riuiHYVOJJ41zd5mdTns1Yn4JyCxh4SZjgxDNn5DX5Z3O9Sz1Wu2BOnhQsCpR5OrP_zKErWDmmOJKjlrqDO_gzCiD4wkchvG)
4. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYNgExg7Ppg2sKKD3ZFaSNMTYkOuJZR210CQ6bMJHP82KrtAyBw7EJMMhpxPoC6APi_0xMDl4ZkNS8BhihbRxZHPfjriJu6MqunS0iSoJeIQ230vLsNQKowflxjL9eUoIZc5Bp_X8YeCzyiqOcA52kSYRJKL_CXOKOdJnTeNcarA47eP-rGFczSt0EM97zbQcbuHNpctNmJwIASOcxXUpDuBXoOwZsbCubt98=)
5. [uhasselt.be](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEF1Pxt6zbVPp-O43hICVsB5qqbCABNGZxi0jlJVQLPhG81Se4bhckgcLJb_9DQEXrWcl1AiCO6fkf3Gz-UedKRi2dm73VSRreKh-N_piqGcAio3T-AMUldIrH96cxp8BxmQ02UuxY_M8B3g2m5O3Ykfz16O0GSvLiMvw==)
6. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEp0z3OLIiXhXRUkpObJ8vsmD2VR-7kVCssUPrDxdEFTFkTqvpeteLZ38u-lcQxZtFuwysjfkGFZWOWEJbKUr59OGljaL8FoofBHVJgsOUEbdDxGREE3DJmieCO8Kd6)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_C4OSd2Ya7QRbeNoehdlUKuNZ280QTpF4Ywhu5nMxVFfkU_LLkRl1rjzaoJdBP-TXAWwdncQZ2etlCKTgAIrv89w_N86zZUm5xzxJNS3KrwOv_XUoJ67OTXUAHfkUBImlX1SGPdpfGsPpX535sOZu2rYkaVCnkkksTi2F4S-b4W4g1lh8Y_dY5txeMmS2wzNEpMSLHbpGoVupztmqMA5WnWpwUk8_5gOZrRxImEXChTCimpJty2NZ9FcwxnD1ph-i5-Z1b2L4ZAS5bCca3oPNELfK6EtVbo7ong4eGs_KMR1WvVhb-YXuZ-bK5WnZ3ux082vOO9WKzguiwA==)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZWWHr9PzaPlUId2nzirIL4iXrIPti6iHxpTvfUcXlmhAdVGZFSSSQZj-akhA1Q7IohxhNi3y_HbighzrSvY8Md7THFKPIXkfNyIvpScWs9p9NrqtXwTICkX8PZ7-gl3opC6KIL1ZDKAdeHJ-EIw73aI97vpXDTchKQeitd-HSTZeyxG84Si6V64uRLZs6K4LGHgbcFvyzLMVPXhCzmWM2AwWcPQy-0CfKAvaQLDENc8r16wIPsODsAKcmc42E_to7tZ9vRceNbCFxF5LlaUL_oLfSzMo8krxgQjLid9_7W7LybDamV8GUfLSMrv6Gmb6wSc5h-jqzjjESdA==)
9. [victorknoop.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHn-Tjc4GkHYuSJ73E1C53H1hgVuaRD0eA4nejBAgZ48qXLciqkVgXtzVKuL00rMfkV9dENHmT9k6GOZnJrKJ7-tM04UPYcExBUlh1QCZ971-6uTNCp6jBTbnj51wni6NWMkYVSV0oQ7gCPin0bnrvgkQ==)
10. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZwIjqnC_CK1L3uIglo2vzmz3kx9_gJSm86fFY_ypyY3i-wCRTEKAUQvyzS6l8jl81zHMHUuc61r2_wZTHotGatJTsvKNbjMIWMtXmMRxCj6B52_dMprN9PoSk0C9xicWtSXUUdYw70eUyDduFQwaLdPU5hSKp2w==)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEl-w_ikbbS27lYJXeHBgksxJ41ralt9bxeRDF0y0txABCu8ZOQ8hMQ51JNK8XuR1H0ZjGP58sOIU6NbW4_i8ky9DOGPvfNqyOgBDpoGTnKcsRpwWLi-sk5WoMtwJQXLSiE5wgj_wyDn2sO8I3vn8ORdMsJCgQxcjK4cgufzJaEH5UBgB82xmNVl6kegk5S5UjPBCaLVhvq)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-6kq-btUDX_SFGRqIdbCoZmfTppYpJd46iU5LP-g5RIgZI20mzTIjt7BS7GwjXbwnny4YvB-UBcFK7ihEIZqM8m4HZGzoOuKHYCZDgV_K_1KDHbcEAJBkzJAeulnokL9GzNQDFXLMNuKutXt-Z4FgtpXzP5TlhSn3tdZF9Qb4abogqKOpX7nLhAAf_LzlTMQvc5vWlAgOuay6l_5Fq6JvgBpqG8K90TdghrQeWsFKji7gHRk-V5s790qQrUOPbkdLsUp8U_fEBnggjx2l5TntOwHt4kDTTWKuO2292Xclm-WemSKH-w==)
13. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4NMa0kzofSEYAZ5gCzZirKPY9jKRGa1Uwdns7A6q43QD093_flhsw9-kplIGCFx4bUczxwXr91UEHTsoBAoCmuqkpggE8ipabnHjYL_C1ng5eI6p6KFOhUdLlWsS4cknYkU9uydOY7NvwdT2o2n_9Rw6m62-yKV5N6XpomJwdM_SfyibbfgMzCBkhCtg_bBWhB6KcdAeagR85GZKn26NMngM_tnhep1SGY4WgQe5pnx8nlQJZKGLD)
14. [dlr.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsS-V4PzgyEsKVNJgKZn4AWZ96Pl6KeHh2muGyco8uY0dK4pMRv_0oE_K5g9NH2ZLQKL4w9geD_YnKKd_2vkKb6UZvbqlZlwwc_YXIXZ7598yuFBfbXw1cLFqkmzmIXNZOyNAshmXWgOSKkS_-ZG77m8ZYSH-MCMZF-rA-e1eq7TGZCmU=)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGU3oGNXcloYb1e6rI1vzUI-d9vmMcr_lFScXLcVjuHW_iZh929LIuPGfBWSOSJGFwIcKh8gl5RVW_v47RxgJgDhK49Cv7261V04o3uVegvrs826-_iv5D529xSiFXeV6JpxTwtMGgwGgenbs-5CFdJ6Amvxe4GkwdwBr1vjSWGfU7TPVxm7n5r885s7z44kcRFhJpUJRyH3H81D97lJ1SNEPnEPTXMLDS-BwTy7Pt6JyfjeE9l-6zY9lIDd8bHGQPCNk9XtVDdXpR1fSYLUyC2fJ_gIbl7QpRXvW5M)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHa5E3v1JyRv7swx9hWoCVPg9UB8O3RE9N-2Umx3BNtm15u-6uPqRPO99hF7E7Q9OcYRg0MFyKBmpsjW41RZQfjM5MDuTUXm2EAIxAjz16JfpSrC8PKoyhjao28Ap8CA5TVqEa3Y3BqO7OMOG1yd7wsegbFaFeJqY-LOwx8RPvudMGhZ1LoqpVCZFbb_QpZFtA902cozWfPHinAh6PZa7LoIalQ7qovbJoxAdAWuUhWBuq06emwh5KVIIieDlX59V5Z)
17. [banglajol.info](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_cnXW-TAxZ2X3zQr1k3jhwm8nIT_ZWkQ9dpchFzHtc2wvSyh8sGB6tLpFQ-Lwo6mJbs9qbSprE8hus10hfruV2mnVK4xlPhg_kGGq1R3pz_hmMOuN7IU3blaJIN0xlQPt8U0GsCWOOitnq6wqz12dR6HqDWDaqfN1)
18. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnV0WI4ixbetgQmTKYOlyXqO43MRISmS5JBs2pcDyFn3lMcRmRRHm8CfcXLW2gfzJyx5p2k1Zy1lFb3QqCpCxmIFqhp-SUGx7yNwjoYcXhrN0CBsxBiwDw3SZM24aQfdQgq4b0d23lwqSO7sQ8tEiNm46KtL6RRjgtq5Iiq_1mNpzStUfx0kWP83c5eYcQ09aY3aA-1owmFrJSF84zrMUecR4mnbxD_Cqr8Yf4QYQYzP1dN6yv8ci2n_fMmUU=)
19. [escholarship.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9Kz299JN0V_ZqCpFHHmXe7h0AWD8hzKBphTe3yS5FgNKT6226wPUShgROuYXfpnH68OZAoNakGNbR6E-BF8tT2xyO6G2omka4oXce0KZZmubI3LlcGoSze5sd-d1_LxB0wU9l9FMc3A6jXFYHTsDz)
20. [tudelft.nl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUkeyj9gcHFgCfqPYSKXYryTP4pPAWivTP8pyLNh75BxrXp99EtDu3H-nQji5pMGgesE7pA4CrLlt4Szy5n02WoP9xy1MXmBzZbfpVKxawqKyCUUzeJiOCZbC__M-LUUDjuqI9g56PMRHcQ7IgLE9FQfoTbZEfYDIYvv8UiluEnJbdC-WKqgiBwZ6PEIs=)
21. [psu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpsiRebTKij8GJE8zu_YjJh5fpKl0OKthchaFCBPsMngCgV8IxqM88zvTyW54z3J-XuUDMxPVb7JUk5oFPZn_lzATPu1l0EJp-_TQtbnFADWUt386HWThCgKyIP0rpGi1WwimNwn4=)
22. [epfl.ch](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7m5zh6VkH-JTjwhJnLfcVF4Xu3-ISasC5C0Te_R2xcDtw3eTygkC7BUmSB93BDOS6dBIBKX3a-_QZAePZCwSuQ1o-iEu34rLXVtBSVgdJ-1Vwb6nMeyZuMLvmdB6QIF1b2cQcyIrBBjB5_1U3zaJlH9aEByQesIhAg5JmXE4=)
23. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0CH5t68qOdkLwoV5thtl-A0ZEicrC9_WQV3zO9bpUvB6ZwA_1qaiJjqQ5diptKbEJcpFeAHLrpfMwSL0M_iyCW2tw_7RHWnLr668lr_WniVCsUHSqzg==)
24. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEOUtgQj4m0kpUI8syKAQLcjReUriZMvEnBRQhXvECZyWqTDqgGzph1mZtPdqio82hgKYbG2-lCjZWoh5k1Lgep2nTuotFAmrVL0iD4Imvu6-h4o_LKxZqkEQAqlZJVuPzL)
25. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdRsz-0QeIDKNu7DA2qiVO5S8Ts8iET8ftQxogQuoSjf4DiAWxmTb4PPuKSpK-DoXaiR8umowIvdGXbKvCdo_gGueb-U12icbvEHp1mKG-PycixKjrew==)
26. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPWDpIxy98leEqt9lhw5WduQWBlSSJQhUTiqLYZoQHTHojh3jYXp2gRE9kSWxwYZfqao2n16Xei1cMWANevenE33S9RmNMJ07gX4TPnY9tV5kt3wLypxXPYSopkPxai8pKqsUrrz6ikfwB0u8bQ0pMgSw-tBFzpKedhH805rGYIvDq6G9qt6EiVKzba5dcBADdZEzsQXZmmsAXEBE8x9bN3pZNYfIolGEZNxzwhG7qex7oJ7fEr0spcg==)
27. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTVrF6vw1j91mSBxblg6gNPPOl_e6cgkjrV11jTYS94Ev6LRrEFDyhhXT4TfuEWroailkhKTWf-TV7WiNG5lIocWUi0sKOwBtKlQsigAVozR9Ckio36r9ZCk7FaFWKsACiKIuFcWX19_yQcRenIwHKf5ob9fDLak0vmBqujF0A3ouZRjFUKSnrRphImnGnFnpRZ5A12kdzXisiWvUGU86aWkruQyKzPlH5o4FZcLaOATqXUIGSYBvKDAcbig_hnHflk8NdLKe1zkUabl643ChQid-BmXZG5z4EHQoT76cmhzgTjGTPdM7dkiDwqnCgaz0ALg==)
28. [kaust.edu.sa](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFU7ZUexIo7LXjzjvVAdV5KHCY8TRo2vPtg07L7pKnKPgw92IIsJhKkNkGCjTih-VZnOXXY1-JF5Eu6QDzU6-ardhbXRnGNqUOPZn2ZamVXWVFQrOSvC0hj5gm86hfk5b3foL6Zas2BOsglgKkt8CF8c-zOzpW8KWPPl65L8VDcMdmVbWnmfk_18CTip47X)
29. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_UviSsJ61XvCq0mYyuMJLtcKJl7zGOtb2tvhTB8tEfJm1XaF5dJ3GAHWfOrZeLEPdMHIQbUwilrCone2UMMRoPgIA9Vetq_R9Xk5s_3lVf5NkuUfEbjM=)
30. [ucdavis.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxlNfo21NIRCDcIbf-9BN83H6I3CudrAl8Z2ToeLlrr3Mf5uWWmy7UmAd17fnsEG7RBapexzxtLnyO2idFM4faToyuy4ZUZQHuy1SIJjncbhNtNRE4oAheO2LR5pzv9hF3WDlUE2h_jt4GqXTrv3AT)
31. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGUgmNvGsxN2NtPSEYNLlOflXl0yXEDy3_iXjN6Pd4cMXrzH3lAcXMdGBzSrTCHoii5pqWFCmhYGdNS_MOKueUA6NO3F2Wi1LWjx_SJuBrIzgiX6Jq_-kazaAIeI_WgCnTbwbz4-rfnhnXh5_FUVcOSAJlKI10Qmv_D5USv-b8JuFxsOCVso0I58eNvWkMrZN43epP4b3-DKhAttfrxo8g8_75QAqDOmbTGliYzq5ifKxCpAjnENOwt4PWosC6_D5BSgJvxR3d1Fk6l-ioTg7nE-GHJtroZ_ic6xiN)
32. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXtErc5Cl6cz2K95N8A0Iak92mPmT1MPjgddmrOjs9GWXLCgbZJNBAhbijuqJMHK6PZVf2mqnFvh3JLGun8Srmqch2dZ9uOh0ZU4yW2rWWed0GiqeGdeAxjK1B4P_nz8bfQ8jAZRYDrMB7J2JtmapoBZWkK91nL03Azd40wkeUlZM458VNPAq1EUGehkgz2D_VLP0LuoU_GCn9K0pDj4zhqZ9JzVl1lArU1RkCTl3aiKwQkTmUEocngkf7Rfo=)
33. [victorknoop.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAPzoaH8O4fxV7PNWVRpdwZsrIQAV_VHgocGs6wDqytT03hunyxITIFIh5Y4pdjfTop6bSKeUZrTr_X76J2CTG-opCigxrlN-xE-81Aga7RxfBtlq4hnsPEpfU1ED28AHu4Tz4gPHqfojhkVl_UEOMDA==)


## Annotations
Annotation(end_index=548, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3XdJCL6GFu4D41jtTDCwPopAkRZpSwvWcqWJons7Y2CTeeTDrKDZD77yAk0RXUDeWf9IKLfVxSi3eW4o6QZVtoAMonxDwF9gfSl_ECQY9i9hXkOUtAIUBCLeK4GfWk4T95ZbX7gtTaETSKmXnpjm9TAoZowM3wpuUx8Q_rpkbnEqkClNFzP4=', start_index=536)
Annotation(end_index=548, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqP5XYiMrSYLtbXXLfj1hpPb1K3vjQuZLtMLs5ckAtXpcWI7_j-wyUHus_rVLs4Tqqi6AXSjYMxx4wNmnkzyq2D-NIaPzAlncPJAKoL4ws6oCtES83gFNfF8Y9qCOGZJpVe_SyIwyIzPWo0HASV-_kFNUkOFhzcW7dBSKORAeN2i8XFQ==', start_index=536)
Annotation(end_index=1075, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYNgExg7Ppg2sKKD3ZFaSNMTYkOuJZR210CQ6bMJHP82KrtAyBw7EJMMhpxPoC6APi_0xMDl4ZkNS8BhihbRxZHPfjriJu6MqunS0iSoJeIQ230vLsNQKowflxjL9eUoIZc5Bp_X8YeCzyiqOcA52kSYRJKL_CXOKOdJnTeNcarA47eP-rGFczSt0EM97zbQcbuHNpctNmJwIASOcxXUpDuBXoOwZsbCubt98=', start_index=1063)
Annotation(end_index=1075, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgRIf_oxthAWjkaxSSBR2ZBufY2wInoDknktUGNcS01yPM-xK6riuiHYVOJJ41zd5mdTns1Yn4JyCxh4SZjgxDNn5DX5Z3O9Sz1Wu2BOnhQsCpR5OrP_zKErWDmmOJKjlrqDO_gzCiD4wkchvG', start_index=1063)
Annotation(end_index=1474, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEF1Pxt6zbVPp-O43hICVsB5qqbCABNGZxi0jlJVQLPhG81Se4bhckgcLJb_9DQEXrWcl1AiCO6fkf3Gz-UedKRi2dm73VSRreKh-N_piqGcAio3T-AMUldIrH96cxp8BxmQ02UuxY_M8B3g2m5O3Ykfz16O0GSvLiMvw==', start_index=1462)
Annotation(end_index=1474, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEp0z3OLIiXhXRUkpObJ8vsmD2VR-7kVCssUPrDxdEFTFkTqvpeteLZ38u-lcQxZtFuwysjfkGFZWOWEJbKUr59OGljaL8FoofBHVJgsOUEbdDxGREE3DJmieCO8Kd6', start_index=1462)
Annotation(end_index=1877, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZWWHr9PzaPlUId2nzirIL4iXrIPti6iHxpTvfUcXlmhAdVGZFSSSQZj-akhA1Q7IohxhNi3y_HbighzrSvY8Md7THFKPIXkfNyIvpScWs9p9NrqtXwTICkX8PZ7-gl3opC6KIL1ZDKAdeHJ-EIw73aI97vpXDTchKQeitd-HSTZeyxG84Si6V64uRLZs6K4LGHgbcFvyzLMVPXhCzmWM2AwWcPQy-0CfKAvaQLDENc8r16wIPsODsAKcmc42E_to7tZ9vRceNbCFxF5LlaUL_oLfSzMo8krxgQjLid9_7W7LybDamV8GUfLSMrv6Gmb6wSc5h-jqzjjESdA==', start_index=1865)
Annotation(end_index=1877, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_C4OSd2Ya7QRbeNoehdlUKuNZ280QTpF4Ywhu5nMxVFfkU_LLkRl1rjzaoJdBP-TXAWwdncQZ2etlCKTgAIrv89w_N86zZUm5xzxJNS3KrwOv_XUoJ67OTXUAHfkUBImlX1SGPdpfGsPpX535sOZu2rYkaVCnkkksTi2F4S-b4W4g1lh8Y_dY5txeMmS2wzNEpMSLHbpGoVupztmqMA5WnWpwUk8_5gOZrRxImEXChTCimpJty2NZ9FcwxnD1ph-i5-Z1b2L4ZAS5bCca3oPNELfK6EtVbo7ong4eGs_KMR1WvVhb-YXuZ-bK5WnZ3ux082vOO9WKzguiwA==', start_index=1865)
Annotation(end_index=2276, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgRIf_oxthAWjkaxSSBR2ZBufY2wInoDknktUGNcS01yPM-xK6riuiHYVOJJ41zd5mdTns1Yn4JyCxh4SZjgxDNn5DX5Z3O9Sz1Wu2BOnhQsCpR5OrP_zKErWDmmOJKjlrqDO_gzCiD4wkchvG', start_index=2264)
Annotation(end_index=2276, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHn-Tjc4GkHYuSJ73E1C53H1hgVuaRD0eA4nejBAgZ48qXLciqkVgXtzVKuL00rMfkV9dENHmT9k6GOZnJrKJ7-tM04UPYcExBUlh1QCZ971-6uTNCp6jBTbnj51wni6NWMkYVSV0oQ7gCPin0bnrvgkQ==', start_index=2264)
Annotation(end_index=2586, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEF1Pxt6zbVPp-O43hICVsB5qqbCABNGZxi0jlJVQLPhG81Se4bhckgcLJb_9DQEXrWcl1AiCO6fkf3Gz-UedKRi2dm73VSRreKh-N_piqGcAio3T-AMUldIrH96cxp8BxmQ02UuxY_M8B3g2m5O3Ykfz16O0GSvLiMvw==', start_index=2573)
Annotation(end_index=2586, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZwIjqnC_CK1L3uIglo2vzmz3kx9_gJSm86fFY_ypyY3i-wCRTEKAUQvyzS6l8jl81zHMHUuc61r2_wZTHotGatJTsvKNbjMIWMtXmMRxCj6B52_dMprN9PoSk0C9xicWtSXUUdYw70eUyDduFQwaLdPU5hSKp2w==', start_index=2573)
Annotation(end_index=3199, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgRIf_oxthAWjkaxSSBR2ZBufY2wInoDknktUGNcS01yPM-xK6riuiHYVOJJ41zd5mdTns1Yn4JyCxh4SZjgxDNn5DX5Z3O9Sz1Wu2BOnhQsCpR5OrP_zKErWDmmOJKjlrqDO_gzCiD4wkchvG', start_index=3190)
Annotation(end_index=3668, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEl-w_ikbbS27lYJXeHBgksxJ41ralt9bxeRDF0y0txABCu8ZOQ8hMQ51JNK8XuR1H0ZjGP58sOIU6NbW4_i8ky9DOGPvfNqyOgBDpoGTnKcsRpwWLi-sk5WoMtwJQXLSiE5wgj_wyDn2sO8I3vn8ORdMsJCgQxcjK4cgufzJaEH5UBgB82xmNVl6kegk5S5UjPBCaLVhvq', start_index=3655)
Annotation(end_index=3668, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3XdJCL6GFu4D41jtTDCwPopAkRZpSwvWcqWJons7Y2CTeeTDrKDZD77yAk0RXUDeWf9IKLfVxSi3eW4o6QZVtoAMonxDwF9gfSl_ECQY9i9hXkOUtAIUBCLeK4GfWk4T95ZbX7gtTaETSKmXnpjm9TAoZowM3wpuUx8Q_rpkbnEqkClNFzP4=', start_index=3655)
Annotation(end_index=3973, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYNgExg7Ppg2sKKD3ZFaSNMTYkOuJZR210CQ6bMJHP82KrtAyBw7EJMMhpxPoC6APi_0xMDl4ZkNS8BhihbRxZHPfjriJu6MqunS0iSoJeIQ230vLsNQKowflxjL9eUoIZc5Bp_X8YeCzyiqOcA52kSYRJKL_CXOKOdJnTeNcarA47eP-rGFczSt0EM97zbQcbuHNpctNmJwIASOcxXUpDuBXoOwZsbCubt98=', start_index=3961)
Annotation(end_index=3973, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqP5XYiMrSYLtbXXLfj1hpPb1K3vjQuZLtMLs5ckAtXpcWI7_j-wyUHus_rVLs4Tqqi6AXSjYMxx4wNmnkzyq2D-NIaPzAlncPJAKoL4ws6oCtES83gFNfF8Y9qCOGZJpVe_SyIwyIzPWo0HASV-_kFNUkOFhzcW7dBSKORAeN2i8XFQ==', start_index=3961)
Annotation(end_index=4439, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-6kq-btUDX_SFGRqIdbCoZmfTppYpJd46iU5LP-g5RIgZI20mzTIjt7BS7GwjXbwnny4YvB-UBcFK7ihEIZqM8m4HZGzoOuKHYCZDgV_K_1KDHbcEAJBkzJAeulnokL9GzNQDFXLMNuKutXt-Z4FgtpXzP5TlhSn3tdZF9Qb4abogqKOpX7nLhAAf_LzlTMQvc5vWlAgOuay6l_5Fq6JvgBpqG8K90TdghrQeWsFKji7gHRk-V5s790qQrUOPbkdLsUp8U_fEBnggjx2l5TntOwHt4kDTTWKuO2292Xclm-WemSKH-w==', start_index=4426)
Annotation(end_index=4439, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHn-Tjc4GkHYuSJ73E1C53H1hgVuaRD0eA4nejBAgZ48qXLciqkVgXtzVKuL00rMfkV9dENHmT9k6GOZnJrKJ7-tM04UPYcExBUlh1QCZ971-6uTNCp6jBTbnj51wni6NWMkYVSV0oQ7gCPin0bnrvgkQ==', start_index=4426)
Annotation(end_index=4672, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqP5XYiMrSYLtbXXLfj1hpPb1K3vjQuZLtMLs5ckAtXpcWI7_j-wyUHus_rVLs4Tqqi6AXSjYMxx4wNmnkzyq2D-NIaPzAlncPJAKoL4ws6oCtES83gFNfF8Y9qCOGZJpVe_SyIwyIzPWo0HASV-_kFNUkOFhzcW7dBSKORAeN2i8XFQ==', start_index=4663)
Annotation(end_index=5349, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4NMa0kzofSEYAZ5gCzZirKPY9jKRGa1Uwdns7A6q43QD093_flhsw9-kplIGCFx4bUczxwXr91UEHTsoBAoCmuqkpggE8ipabnHjYL_C1ng5eI6p6KFOhUdLlWsS4cknYkU9uydOY7NvwdT2o2n_9Rw6m62-yKV5N6XpomJwdM_SfyibbfgMzCBkhCtg_bBWhB6KcdAeagR85GZKn26NMngM_tnhep1SGY4WgQe5pnx8nlQJZKGLD', start_index=5339)
Annotation(end_index=5605, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3XdJCL6GFu4D41jtTDCwPopAkRZpSwvWcqWJons7Y2CTeeTDrKDZD77yAk0RXUDeWf9IKLfVxSi3eW4o6QZVtoAMonxDwF9gfSl_ECQY9i9hXkOUtAIUBCLeK4GfWk4T95ZbX7gtTaETSKmXnpjm9TAoZowM3wpuUx8Q_rpkbnEqkClNFzP4=', start_index=5596)
Annotation(end_index=6048, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsS-V4PzgyEsKVNJgKZn4AWZ96Pl6KeHh2muGyco8uY0dK4pMRv_0oE_K5g9NH2ZLQKL4w9geD_YnKKd_2vkKb6UZvbqlZlwwc_YXIXZ7598yuFBfbXw1cLFqkmzmIXNZOyNAshmXWgOSKkS_-ZG77m8ZYSH-MCMZF-rA-e1eq7TGZCmU=', start_index=6038)
Annotation(end_index=6367, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3XdJCL6GFu4D41jtTDCwPopAkRZpSwvWcqWJons7Y2CTeeTDrKDZD77yAk0RXUDeWf9IKLfVxSi3eW4o6QZVtoAMonxDwF9gfSl_ECQY9i9hXkOUtAIUBCLeK4GfWk4T95ZbX7gtTaETSKmXnpjm9TAoZowM3wpuUx8Q_rpkbnEqkClNFzP4=', start_index=6355)
Annotation(end_index=6367, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqP5XYiMrSYLtbXXLfj1hpPb1K3vjQuZLtMLs5ckAtXpcWI7_j-wyUHus_rVLs4Tqqi6AXSjYMxx4wNmnkzyq2D-NIaPzAlncPJAKoL4ws6oCtES83gFNfF8Y9qCOGZJpVe_SyIwyIzPWo0HASV-_kFNUkOFhzcW7dBSKORAeN2i8XFQ==', start_index=6355)
Annotation(end_index=6686, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGU3oGNXcloYb1e6rI1vzUI-d9vmMcr_lFScXLcVjuHW_iZh929LIuPGfBWSOSJGFwIcKh8gl5RVW_v47RxgJgDhK49Cv7261V04o3uVegvrs826-_iv5D529xSiFXeV6JpxTwtMGgwGgenbs-5CFdJ6Amvxe4GkwdwBr1vjSWGfU7TPVxm7n5r885s7z44kcRFhJpUJRyH3H81D97lJ1SNEPnEPTXMLDS-BwTy7Pt6JyfjeE9l-6zY9lIDd8bHGQPCNk9XtVDdXpR1fSYLUyC2fJ_gIbl7QpRXvW5M', start_index=6672)
Annotation(end_index=6686, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHa5E3v1JyRv7swx9hWoCVPg9UB8O3RE9N-2Umx3BNtm15u-6uPqRPO99hF7E7Q9OcYRg0MFyKBmpsjW41RZQfjM5MDuTUXm2EAIxAjz16JfpSrC8PKoyhjao28Ap8CA5TVqEa3Y3BqO7OMOG1yd7wsegbFaFeJqY-LOwx8RPvudMGhZ1LoqpVCZFbb_QpZFtA902cozWfPHinAh6PZa7LoIalQ7qovbJoxAdAWuUhWBuq06emwh5KVIIieDlX59V5Z', start_index=6672)
Annotation(end_index=6981, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_cnXW-TAxZ2X3zQr1k3jhwm8nIT_ZWkQ9dpchFzHtc2wvSyh8sGB6tLpFQ-Lwo6mJbs9qbSprE8hus10hfruV2mnVK4xlPhg_kGGq1R3pz_hmMOuN7IU3blaJIN0xlQPt8U0GsCWOOitnq6wqz12dR6HqDWDaqfN1', start_index=6967)
Annotation(end_index=6981, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnV0WI4ixbetgQmTKYOlyXqO43MRISmS5JBs2pcDyFn3lMcRmRRHm8CfcXLW2gfzJyx5p2k1Zy1lFb3QqCpCxmIFqhp-SUGx7yNwjoYcXhrN0CBsxBiwDw3SZM24aQfdQgq4b0d23lwqSO7sQ8tEiNm46KtL6RRjgtq5Iiq_1mNpzStUfx0kWP83c5eYcQ09aY3aA-1owmFrJSF84zrMUecR4mnbxD_Cqr8Yf4QYQYzP1dN6yv8ci2n_fMmUU=', start_index=6967)
Annotation(end_index=7305, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqP5XYiMrSYLtbXXLfj1hpPb1K3vjQuZLtMLs5ckAtXpcWI7_j-wyUHus_rVLs4Tqqi6AXSjYMxx4wNmnkzyq2D-NIaPzAlncPJAKoL4ws6oCtES83gFNfF8Y9qCOGZJpVe_SyIwyIzPWo0HASV-_kFNUkOFhzcW7dBSKORAeN2i8XFQ==', start_index=7296)
Annotation(end_index=7808, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqP5XYiMrSYLtbXXLfj1hpPb1K3vjQuZLtMLs5ckAtXpcWI7_j-wyUHus_rVLs4Tqqi6AXSjYMxx4wNmnkzyq2D-NIaPzAlncPJAKoL4ws6oCtES83gFNfF8Y9qCOGZJpVe_SyIwyIzPWo0HASV-_kFNUkOFhzcW7dBSKORAeN2i8XFQ==', start_index=7799)
Annotation(end_index=8068, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9Kz299JN0V_ZqCpFHHmXe7h0AWD8hzKBphTe3yS5FgNKT6226wPUShgROuYXfpnH68OZAoNakGNbR6E-BF8tT2xyO6G2omka4oXce0KZZmubI3LlcGoSze5sd-d1_LxB0wU9l9FMc3A6jXFYHTsDz', start_index=8058)
Annotation(end_index=8764, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9Kz299JN0V_ZqCpFHHmXe7h0AWD8hzKBphTe3yS5FgNKT6226wPUShgROuYXfpnH68OZAoNakGNbR6E-BF8tT2xyO6G2omka4oXce0KZZmubI3LlcGoSze5sd-d1_LxB0wU9l9FMc3A6jXFYHTsDz', start_index=8754)
Annotation(end_index=8980, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9Kz299JN0V_ZqCpFHHmXe7h0AWD8hzKBphTe3yS5FgNKT6226wPUShgROuYXfpnH68OZAoNakGNbR6E-BF8tT2xyO6G2omka4oXce0KZZmubI3LlcGoSze5sd-d1_LxB0wU9l9FMc3A6jXFYHTsDz', start_index=8970)
Annotation(end_index=9427, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYNgExg7Ppg2sKKD3ZFaSNMTYkOuJZR210CQ6bMJHP82KrtAyBw7EJMMhpxPoC6APi_0xMDl4ZkNS8BhihbRxZHPfjriJu6MqunS0iSoJeIQ230vLsNQKowflxjL9eUoIZc5Bp_X8YeCzyiqOcA52kSYRJKL_CXOKOdJnTeNcarA47eP-rGFczSt0EM97zbQcbuHNpctNmJwIASOcxXUpDuBXoOwZsbCubt98=', start_index=9415)
Annotation(end_index=9427, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgRIf_oxthAWjkaxSSBR2ZBufY2wInoDknktUGNcS01yPM-xK6riuiHYVOJJ41zd5mdTns1Yn4JyCxh4SZjgxDNn5DX5Z3O9Sz1Wu2BOnhQsCpR5OrP_zKErWDmmOJKjlrqDO_gzCiD4wkchvG', start_index=9415)
Annotation(end_index=10229, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUkeyj9gcHFgCfqPYSKXYryTP4pPAWivTP8pyLNh75BxrXp99EtDu3H-nQji5pMGgesE7pA4CrLlt4Szy5n02WoP9xy1MXmBzZbfpVKxawqKyCUUzeJiOCZbC__M-LUUDjuqI9g56PMRHcQ7IgLE9FQfoTbZEfYDIYvv8UiluEnJbdC-WKqgiBwZ6PEIs=', start_index=10219)
Annotation(end_index=10370, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7m5zh6VkH-JTjwhJnLfcVF4Xu3-ISasC5C0Te_R2xcDtw3eTygkC7BUmSB93BDOS6dBIBKX3a-_QZAePZCwSuQ1o-iEu34rLXVtBSVgdJ-1Vwb6nMeyZuMLvmdB6QIF1b2cQcyIrBBjB5_1U3zaJlH9aEByQesIhAg5JmXE4=', start_index=10356)
Annotation(end_index=10370, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpsiRebTKij8GJE8zu_YjJh5fpKl0OKthchaFCBPsMngCgV8IxqM88zvTyW54z3J-XuUDMxPVb7JUk5oFPZn_lzATPu1l0EJp-_TQtbnFADWUt386HWThCgKyIP0rpGi1WwimNwn4=', start_index=10356)
Annotation(end_index=10730, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgRIf_oxthAWjkaxSSBR2ZBufY2wInoDknktUGNcS01yPM-xK6riuiHYVOJJ41zd5mdTns1Yn4JyCxh4SZjgxDNn5DX5Z3O9Sz1Wu2BOnhQsCpR5OrP_zKErWDmmOJKjlrqDO_gzCiD4wkchvG', start_index=10718)
Annotation(end_index=10730, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHn-Tjc4GkHYuSJ73E1C53H1hgVuaRD0eA4nejBAgZ48qXLciqkVgXtzVKuL00rMfkV9dENHmT9k6GOZnJrKJ7-tM04UPYcExBUlh1QCZ971-6uTNCp6jBTbnj51wni6NWMkYVSV0oQ7gCPin0bnrvgkQ==', start_index=10718)
Annotation(end_index=11201, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYNgExg7Ppg2sKKD3ZFaSNMTYkOuJZR210CQ6bMJHP82KrtAyBw7EJMMhpxPoC6APi_0xMDl4ZkNS8BhihbRxZHPfjriJu6MqunS0iSoJeIQ230vLsNQKowflxjL9eUoIZc5Bp_X8YeCzyiqOcA52kSYRJKL_CXOKOdJnTeNcarA47eP-rGFczSt0EM97zbQcbuHNpctNmJwIASOcxXUpDuBXoOwZsbCubt98=', start_index=11192)
Annotation(end_index=11397, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpsiRebTKij8GJE8zu_YjJh5fpKl0OKthchaFCBPsMngCgV8IxqM88zvTyW54z3J-XuUDMxPVb7JUk5oFPZn_lzATPu1l0EJp-_TQtbnFADWUt386HWThCgKyIP0rpGi1WwimNwn4=', start_index=11387)
Annotation(end_index=11587, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpsiRebTKij8GJE8zu_YjJh5fpKl0OKthchaFCBPsMngCgV8IxqM88zvTyW54z3J-XuUDMxPVb7JUk5oFPZn_lzATPu1l0EJp-_TQtbnFADWUt386HWThCgKyIP0rpGi1WwimNwn4=', start_index=11577)
Annotation(end_index=11785, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0CH5t68qOdkLwoV5thtl-A0ZEicrC9_WQV3zO9bpUvB6ZwA_1qaiJjqQ5diptKbEJcpFeAHLrpfMwSL0M_iyCW2tw_7RHWnLr668lr_WniVCsUHSqzg==', start_index=11775)
Annotation(end_index=12295, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_C4OSd2Ya7QRbeNoehdlUKuNZ280QTpF4Ywhu5nMxVFfkU_LLkRl1rjzaoJdBP-TXAWwdncQZ2etlCKTgAIrv89w_N86zZUm5xzxJNS3KrwOv_XUoJ67OTXUAHfkUBImlX1SGPdpfGsPpX535sOZu2rYkaVCnkkksTi2F4S-b4W4g1lh8Y_dY5txeMmS2wzNEpMSLHbpGoVupztmqMA5WnWpwUk8_5gOZrRxImEXChTCimpJty2NZ9FcwxnD1ph-i5-Z1b2L4ZAS5bCca3oPNELfK6EtVbo7ong4eGs_KMR1WvVhb-YXuZ-bK5WnZ3ux082vOO9WKzguiwA==', start_index=12286)
Annotation(end_index=12801, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZWWHr9PzaPlUId2nzirIL4iXrIPti6iHxpTvfUcXlmhAdVGZFSSSQZj-akhA1Q7IohxhNi3y_HbighzrSvY8Md7THFKPIXkfNyIvpScWs9p9NrqtXwTICkX8PZ7-gl3opC6KIL1ZDKAdeHJ-EIw73aI97vpXDTchKQeitd-HSTZeyxG84Si6V64uRLZs6K4LGHgbcFvyzLMVPXhCzmWM2AwWcPQy-0CfKAvaQLDENc8r16wIPsODsAKcmc42E_to7tZ9vRceNbCFxF5LlaUL_oLfSzMo8krxgQjLid9_7W7LybDamV8GUfLSMrv6Gmb6wSc5h-jqzjjESdA==', start_index=12789)
Annotation(end_index=12801, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_C4OSd2Ya7QRbeNoehdlUKuNZ280QTpF4Ywhu5nMxVFfkU_LLkRl1rjzaoJdBP-TXAWwdncQZ2etlCKTgAIrv89w_N86zZUm5xzxJNS3KrwOv_XUoJ67OTXUAHfkUBImlX1SGPdpfGsPpX535sOZu2rYkaVCnkkksTi2F4S-b4W4g1lh8Y_dY5txeMmS2wzNEpMSLHbpGoVupztmqMA5WnWpwUk8_5gOZrRxImEXChTCimpJty2NZ9FcwxnD1ph-i5-Z1b2L4ZAS5bCca3oPNELfK6EtVbo7ong4eGs_KMR1WvVhb-YXuZ-bK5WnZ3ux082vOO9WKzguiwA==', start_index=12789)
Annotation(end_index=13470, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEl-w_ikbbS27lYJXeHBgksxJ41ralt9bxeRDF0y0txABCu8ZOQ8hMQ51JNK8XuR1H0ZjGP58sOIU6NbW4_i8ky9DOGPvfNqyOgBDpoGTnKcsRpwWLi-sk5WoMtwJQXLSiE5wgj_wyDn2sO8I3vn8ORdMsJCgQxcjK4cgufzJaEH5UBgB82xmNVl6kegk5S5UjPBCaLVhvq', start_index=13460)
Annotation(end_index=13872, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEOUtgQj4m0kpUI8syKAQLcjReUriZMvEnBRQhXvECZyWqTDqgGzph1mZtPdqio82hgKYbG2-lCjZWoh5k1Lgep2nTuotFAmrVL0iD4Imvu6-h4o_LKxZqkEQAqlZJVuPzL', start_index=13858)
Annotation(end_index=13872, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdRsz-0QeIDKNu7DA2qiVO5S8Ts8iET8ftQxogQuoSjf4DiAWxmTb4PPuKSpK-DoXaiR8umowIvdGXbKvCdo_gGueb-U12icbvEHp1mKG-PycixKjrew==', start_index=13858)
Annotation(end_index=14235, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEp0z3OLIiXhXRUkpObJ8vsmD2VR-7kVCssUPrDxdEFTFkTqvpeteLZ38u-lcQxZtFuwysjfkGFZWOWEJbKUr59OGljaL8FoofBHVJgsOUEbdDxGREE3DJmieCO8Kd6', start_index=14222)
Annotation(end_index=14235, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPWDpIxy98leEqt9lhw5WduQWBlSSJQhUTiqLYZoQHTHojh3jYXp2gRE9kSWxwYZfqao2n16Xei1cMWANevenE33S9RmNMJ07gX4TPnY9tV5kt3wLypxXPYSopkPxai8pKqsUrrz6ikfwB0u8bQ0pMgSw-tBFzpKedhH805rGYIvDq6G9qt6EiVKzba5dcBADdZEzsQXZmmsAXEBE8x9bN3pZNYfIolGEZNxzwhG7qex7oJ7fEr0spcg==', start_index=14222)
Annotation(end_index=14705, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-6kq-btUDX_SFGRqIdbCoZmfTppYpJd46iU5LP-g5RIgZI20mzTIjt7BS7GwjXbwnny4YvB-UBcFK7ihEIZqM8m4HZGzoOuKHYCZDgV_K_1KDHbcEAJBkzJAeulnokL9GzNQDFXLMNuKutXt-Z4FgtpXzP5TlhSn3tdZF9Qb4abogqKOpX7nLhAAf_LzlTMQvc5vWlAgOuay6l_5Fq6JvgBpqG8K90TdghrQeWsFKji7gHRk-V5s790qQrUOPbkdLsUp8U_fEBnggjx2l5TntOwHt4kDTTWKuO2292Xclm-WemSKH-w==', start_index=14695)
Annotation(end_index=14973, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-6kq-btUDX_SFGRqIdbCoZmfTppYpJd46iU5LP-g5RIgZI20mzTIjt7BS7GwjXbwnny4YvB-UBcFK7ihEIZqM8m4HZGzoOuKHYCZDgV_K_1KDHbcEAJBkzJAeulnokL9GzNQDFXLMNuKutXt-Z4FgtpXzP5TlhSn3tdZF9Qb4abogqKOpX7nLhAAf_LzlTMQvc5vWlAgOuay6l_5Fq6JvgBpqG8K90TdghrQeWsFKji7gHRk-V5s790qQrUOPbkdLsUp8U_fEBnggjx2l5TntOwHt4kDTTWKuO2292Xclm-WemSKH-w==', start_index=14963)
Annotation(end_index=15276, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-6kq-btUDX_SFGRqIdbCoZmfTppYpJd46iU5LP-g5RIgZI20mzTIjt7BS7GwjXbwnny4YvB-UBcFK7ihEIZqM8m4HZGzoOuKHYCZDgV_K_1KDHbcEAJBkzJAeulnokL9GzNQDFXLMNuKutXt-Z4FgtpXzP5TlhSn3tdZF9Qb4abogqKOpX7nLhAAf_LzlTMQvc5vWlAgOuay6l_5Fq6JvgBpqG8K90TdghrQeWsFKji7gHRk-V5s790qQrUOPbkdLsUp8U_fEBnggjx2l5TntOwHt4kDTTWKuO2292Xclm-WemSKH-w==', start_index=15266)
Annotation(end_index=15684, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEl-w_ikbbS27lYJXeHBgksxJ41ralt9bxeRDF0y0txABCu8ZOQ8hMQ51JNK8XuR1H0ZjGP58sOIU6NbW4_i8ky9DOGPvfNqyOgBDpoGTnKcsRpwWLi-sk5WoMtwJQXLSiE5wgj_wyDn2sO8I3vn8ORdMsJCgQxcjK4cgufzJaEH5UBgB82xmNVl6kegk5S5UjPBCaLVhvq', start_index=15674)
Annotation(end_index=16247, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFU7ZUexIo7LXjzjvVAdV5KHCY8TRo2vPtg07L7pKnKPgw92IIsJhKkNkGCjTih-VZnOXXY1-JF5Eu6QDzU6-ardhbXRnGNqUOPZn2ZamVXWVFQrOSvC0hj5gm86hfk5b3foL6Zas2BOsglgKkt8CF8c-zOzpW8KWPPl65L8VDcMdmVbWnmfk_18CTip47X', start_index=16233)
Annotation(end_index=16247, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTVrF6vw1j91mSBxblg6gNPPOl_e6cgkjrV11jTYS94Ev6LRrEFDyhhXT4TfuEWroailkhKTWf-TV7WiNG5lIocWUi0sKOwBtKlQsigAVozR9Ckio36r9ZCk7FaFWKsACiKIuFcWX19_yQcRenIwHKf5ob9fDLak0vmBqujF0A3ouZRjFUKSnrRphImnGnFnpRZ5A12kdzXisiWvUGU86aWkruQyKzPlH5o4FZcLaOATqXUIGSYBvKDAcbig_hnHflk8NdLKe1zkUabl643ChQid-BmXZG5z4EHQoT76cmhzgTjGTPdM7dkiDwqnCgaz0ALg==', start_index=16233)
Annotation(end_index=16500, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_UviSsJ61XvCq0mYyuMJLtcKJl7zGOtb2tvhTB8tEfJm1XaF5dJ3GAHWfOrZeLEPdMHIQbUwilrCone2UMMRoPgIA9Vetq_R9Xk5s_3lVf5NkuUfEbjM=', start_index=16490)
Annotation(end_index=17988, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEF1Pxt6zbVPp-O43hICVsB5qqbCABNGZxi0jlJVQLPhG81Se4bhckgcLJb_9DQEXrWcl1AiCO6fkf3Gz-UedKRi2dm73VSRreKh-N_piqGcAio3T-AMUldIrH96cxp8BxmQ02UuxY_M8B3g2m5O3Ykfz16O0GSvLiMvw==', start_index=17979)
Annotation(end_index=18135, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgRIf_oxthAWjkaxSSBR2ZBufY2wInoDknktUGNcS01yPM-xK6riuiHYVOJJ41zd5mdTns1Yn4JyCxh4SZjgxDNn5DX5Z3O9Sz1Wu2BOnhQsCpR5OrP_zKErWDmmOJKjlrqDO_gzCiD4wkchvG', start_index=18126)
Annotation(end_index=18259, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-6kq-btUDX_SFGRqIdbCoZmfTppYpJd46iU5LP-g5RIgZI20mzTIjt7BS7GwjXbwnny4YvB-UBcFK7ihEIZqM8m4HZGzoOuKHYCZDgV_K_1KDHbcEAJBkzJAeulnokL9GzNQDFXLMNuKutXt-Z4FgtpXzP5TlhSn3tdZF9Qb4abogqKOpX7nLhAAf_LzlTMQvc5vWlAgOuay6l_5Fq6JvgBpqG8K90TdghrQeWsFKji7gHRk-V5s790qQrUOPbkdLsUp8U_fEBnggjx2l5TntOwHt4kDTTWKuO2292Xclm-WemSKH-w==', start_index=18249)
Annotation(end_index=18384, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3XdJCL6GFu4D41jtTDCwPopAkRZpSwvWcqWJons7Y2CTeeTDrKDZD77yAk0RXUDeWf9IKLfVxSi3eW4o6QZVtoAMonxDwF9gfSl_ECQY9i9hXkOUtAIUBCLeK4GfWk4T95ZbX7gtTaETSKmXnpjm9TAoZowM3wpuUx8Q_rpkbnEqkClNFzP4=', start_index=18375)
Annotation(end_index=18456, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqP5XYiMrSYLtbXXLfj1hpPb1K3vjQuZLtMLs5ckAtXpcWI7_j-wyUHus_rVLs4Tqqi6AXSjYMxx4wNmnkzyq2D-NIaPzAlncPJAKoL4ws6oCtES83gFNfF8Y9qCOGZJpVe_SyIwyIzPWo0HASV-_kFNUkOFhzcW7dBSKORAeN2i8XFQ==', start_index=18447)
Annotation(end_index=18532, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsS-V4PzgyEsKVNJgKZn4AWZ96Pl6KeHh2muGyco8uY0dK4pMRv_0oE_K5g9NH2ZLQKL4w9geD_YnKKd_2vkKb6UZvbqlZlwwc_YXIXZ7598yuFBfbXw1cLFqkmzmIXNZOyNAshmXWgOSKkS_-ZG77m8ZYSH-MCMZF-rA-e1eq7TGZCmU=', start_index=18522)
Annotation(end_index=18605, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZwIjqnC_CK1L3uIglo2vzmz3kx9_gJSm86fFY_ypyY3i-wCRTEKAUQvyzS6l8jl81zHMHUuc61r2_wZTHotGatJTsvKNbjMIWMtXmMRxCj6B52_dMprN9PoSk0C9xicWtSXUUdYw70eUyDduFQwaLdPU5hSKp2w==', start_index=18595)
Annotation(end_index=18697, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0CH5t68qOdkLwoV5thtl-A0ZEicrC9_WQV3zO9bpUvB6ZwA_1qaiJjqQ5diptKbEJcpFeAHLrpfMwSL0M_iyCW2tw_7RHWnLr668lr_WniVCsUHSqzg==', start_index=18687)
Annotation(end_index=18776, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9Kz299JN0V_ZqCpFHHmXe7h0AWD8hzKBphTe3yS5FgNKT6226wPUShgROuYXfpnH68OZAoNakGNbR6E-BF8tT2xyO6G2omka4oXce0KZZmubI3LlcGoSze5sd-d1_LxB0wU9l9FMc3A6jXFYHTsDz', start_index=18766)
Annotation(end_index=18866, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_C4OSd2Ya7QRbeNoehdlUKuNZ280QTpF4Ywhu5nMxVFfkU_LLkRl1rjzaoJdBP-TXAWwdncQZ2etlCKTgAIrv89w_N86zZUm5xzxJNS3KrwOv_XUoJ67OTXUAHfkUBImlX1SGPdpfGsPpX535sOZu2rYkaVCnkkksTi2F4S-b4W4g1lh8Y_dY5txeMmS2wzNEpMSLHbpGoVupztmqMA5WnWpwUk8_5gOZrRxImEXChTCimpJty2NZ9FcwxnD1ph-i5-Z1b2L4ZAS5bCca3oPNELfK6EtVbo7ong4eGs_KMR1WvVhb-YXuZ-bK5WnZ3ux082vOO9WKzguiwA==', start_index=18857)
Annotation(end_index=18967, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZWWHr9PzaPlUId2nzirIL4iXrIPti6iHxpTvfUcXlmhAdVGZFSSSQZj-akhA1Q7IohxhNi3y_HbighzrSvY8Md7THFKPIXkfNyIvpScWs9p9NrqtXwTICkX8PZ7-gl3opC6KIL1ZDKAdeHJ-EIw73aI97vpXDTchKQeitd-HSTZeyxG84Si6V64uRLZs6K4LGHgbcFvyzLMVPXhCzmWM2AwWcPQy-0CfKAvaQLDENc8r16wIPsODsAKcmc42E_to7tZ9vRceNbCFxF5LlaUL_oLfSzMo8krxgQjLid9_7W7LybDamV8GUfLSMrv6Gmb6wSc5h-jqzjjESdA==', start_index=18958)
Annotation(end_index=19039, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpsiRebTKij8GJE8zu_YjJh5fpKl0OKthchaFCBPsMngCgV8IxqM88zvTyW54z3J-XuUDMxPVb7JUk5oFPZn_lzATPu1l0EJp-_TQtbnFADWUt386HWThCgKyIP0rpGi1WwimNwn4=', start_index=19029)
Annotation(end_index=19115, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7m5zh6VkH-JTjwhJnLfcVF4Xu3-ISasC5C0Te_R2xcDtw3eTygkC7BUmSB93BDOS6dBIBKX3a-_QZAePZCwSuQ1o-iEu34rLXVtBSVgdJ-1Vwb6nMeyZuMLvmdB6QIF1b2cQcyIrBBjB5_1U3zaJlH9aEByQesIhAg5JmXE4=', start_index=19105)
Annotation(end_index=19212, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxlNfo21NIRCDcIbf-9BN83H6I3CudrAl8Z2ToeLlrr3Mf5uWWmy7UmAd17fnsEG7RBapexzxtLnyO2idFM4faToyuy4ZUZQHuy1SIJjncbhNtNRE4oAheO2LR5pzv9hF3WDlUE2h_jt4GqXTrv3AT', start_index=19202)
Annotation(end_index=19300, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4NMa0kzofSEYAZ5gCzZirKPY9jKRGa1Uwdns7A6q43QD093_flhsw9-kplIGCFx4bUczxwXr91UEHTsoBAoCmuqkpggE8ipabnHjYL_C1ng5eI6p6KFOhUdLlWsS4cknYkU9uydOY7NvwdT2o2n_9Rw6m62-yKV5N6XpomJwdM_SfyibbfgMzCBkhCtg_bBWhB6KcdAeagR85GZKn26NMngM_tnhep1SGY4WgQe5pnx8nlQJZKGLD', start_index=19290)
Annotation(end_index=19383, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGU3oGNXcloYb1e6rI1vzUI-d9vmMcr_lFScXLcVjuHW_iZh929LIuPGfBWSOSJGFwIcKh8gl5RVW_v47RxgJgDhK49Cv7261V04o3uVegvrs826-_iv5D529xSiFXeV6JpxTwtMGgwGgenbs-5CFdJ6Amvxe4GkwdwBr1vjSWGfU7TPVxm7n5r885s7z44kcRFhJpUJRyH3H81D97lJ1SNEPnEPTXMLDS-BwTy7Pt6JyfjeE9l-6zY9lIDd8bHGQPCNk9XtVDdXpR1fSYLUyC2fJ_gIbl7QpRXvW5M', start_index=19373)
Annotation(end_index=19495, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_cnXW-TAxZ2X3zQr1k3jhwm8nIT_ZWkQ9dpchFzHtc2wvSyh8sGB6tLpFQ-Lwo6mJbs9qbSprE8hus10hfruV2mnVK4xlPhg_kGGq1R3pz_hmMOuN7IU3blaJIN0xlQPt8U0GsCWOOitnq6wqz12dR6HqDWDaqfN1', start_index=19485)
Annotation(end_index=19568, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnV0WI4ixbetgQmTKYOlyXqO43MRISmS5JBs2pcDyFn3lMcRmRRHm8CfcXLW2gfzJyx5p2k1Zy1lFb3QqCpCxmIFqhp-SUGx7yNwjoYcXhrN0CBsxBiwDw3SZM24aQfdQgq4b0d23lwqSO7sQ8tEiNm46KtL6RRjgtq5Iiq_1mNpzStUfx0kWP83c5eYcQ09aY3aA-1owmFrJSF84zrMUecR4mnbxD_Cqr8Yf4QYQYzP1dN6yv8ci2n_fMmUU=', start_index=19558)
Annotation(end_index=19649, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHa5E3v1JyRv7swx9hWoCVPg9UB8O3RE9N-2Umx3BNtm15u-6uPqRPO99hF7E7Q9OcYRg0MFyKBmpsjW41RZQfjM5MDuTUXm2EAIxAjz16JfpSrC8PKoyhjao28Ap8CA5TVqEa3Y3BqO7OMOG1yd7wsegbFaFeJqY-LOwx8RPvudMGhZ1LoqpVCZFbb_QpZFtA902cozWfPHinAh6PZa7LoIalQ7qovbJoxAdAWuUhWBuq06emwh5KVIIieDlX59V5Z', start_index=19639)
Annotation(end_index=19734, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGUgmNvGsxN2NtPSEYNLlOflXl0yXEDy3_iXjN6Pd4cMXrzH3lAcXMdGBzSrTCHoii5pqWFCmhYGdNS_MOKueUA6NO3F2Wi1LWjx_SJuBrIzgiX6Jq_-kazaAIeI_WgCnTbwbz4-rfnhnXh5_FUVcOSAJlKI10Qmv_D5USv-b8JuFxsOCVso0I58eNvWkMrZN43epP4b3-DKhAttfrxo8g8_75QAqDOmbTGliYzq5ifKxCpAjnENOwt4PWosC6_D5BSgJvxR3d1Fk6l-ioTg7nE-GHJtroZ_ic6xiN', start_index=19724)
Annotation(end_index=19817, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEOUtgQj4m0kpUI8syKAQLcjReUriZMvEnBRQhXvECZyWqTDqgGzph1mZtPdqio82hgKYbG2-lCjZWoh5k1Lgep2nTuotFAmrVL0iD4Imvu6-h4o_LKxZqkEQAqlZJVuPzL', start_index=19807)
Annotation(end_index=19891, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXtErc5Cl6cz2K95N8A0Iak92mPmT1MPjgddmrOjs9GWXLCgbZJNBAhbijuqJMHK6PZVf2mqnFvh3JLGun8Srmqch2dZ9uOh0ZU4yW2rWWed0GiqeGdeAxjK1B4P_nz8bfQ8jAZRYDrMB7J2JtmapoBZWkK91nL03Azd40wkeUlZM458VNPAq1EUGehkgz2D_VLP0LuoU_GCn9K0pDj4zhqZ9JzVl1lArU1RkCTl3aiKwQkTmUEocngkf7Rfo=', start_index=19881)
Annotation(end_index=19965, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdRsz-0QeIDKNu7DA2qiVO5S8Ts8iET8ftQxogQuoSjf4DiAWxmTb4PPuKSpK-DoXaiR8umowIvdGXbKvCdo_gGueb-U12icbvEHp1mKG-PycixKjrew==', start_index=19955)
Annotation(end_index=20039, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEl-w_ikbbS27lYJXeHBgksxJ41ralt9bxeRDF0y0txABCu8ZOQ8hMQ51JNK8XuR1H0ZjGP58sOIU6NbW4_i8ky9DOGPvfNqyOgBDpoGTnKcsRpwWLi-sk5WoMtwJQXLSiE5wgj_wyDn2sO8I3vn8ORdMsJCgQxcjK4cgufzJaEH5UBgB82xmNVl6kegk5S5UjPBCaLVhvq', start_index=20029)
Annotation(end_index=20115, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_UviSsJ61XvCq0mYyuMJLtcKJl7zGOtb2tvhTB8tEfJm1XaF5dJ3GAHWfOrZeLEPdMHIQbUwilrCone2UMMRoPgIA9Vetq_R9Xk5s_3lVf5NkuUfEbjM=', start_index=20105)
Annotation(end_index=20193, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTVrF6vw1j91mSBxblg6gNPPOl_e6cgkjrV11jTYS94Ev6LRrEFDyhhXT4TfuEWroailkhKTWf-TV7WiNG5lIocWUi0sKOwBtKlQsigAVozR9Ckio36r9ZCk7FaFWKsACiKIuFcWX19_yQcRenIwHKf5ob9fDLak0vmBqujF0A3ouZRjFUKSnrRphImnGnFnpRZ5A12kdzXisiWvUGU86aWkruQyKzPlH5o4FZcLaOATqXUIGSYBvKDAcbig_hnHflk8NdLKe1zkUabl643ChQid-BmXZG5z4EHQoT76cmhzgTjGTPdM7dkiDwqnCgaz0ALg==', start_index=20183)
Annotation(end_index=20285, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFU7ZUexIo7LXjzjvVAdV5KHCY8TRo2vPtg07L7pKnKPgw92IIsJhKkNkGCjTih-VZnOXXY1-JF5Eu6QDzU6-ardhbXRnGNqUOPZn2ZamVXWVFQrOSvC0hj5gm86hfk5b3foL6Zas2BOsglgKkt8CF8c-zOzpW8KWPPl65L8VDcMdmVbWnmfk_18CTip47X', start_index=20275)
Annotation(end_index=20361, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUkeyj9gcHFgCfqPYSKXYryTP4pPAWivTP8pyLNh75BxrXp99EtDu3H-nQji5pMGgesE7pA4CrLlt4Szy5n02WoP9xy1MXmBzZbfpVKxawqKyCUUzeJiOCZbC__M-LUUDjuqI9g56PMRHcQ7IgLE9FQfoTbZEfYDIYvv8UiluEnJbdC-WKqgiBwZ6PEIs=', start_index=20351)
Annotation(end_index=20438, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-6kq-btUDX_SFGRqIdbCoZmfTppYpJd46iU5LP-g5RIgZI20mzTIjt7BS7GwjXbwnny4YvB-UBcFK7ihEIZqM8m4HZGzoOuKHYCZDgV_K_1KDHbcEAJBkzJAeulnokL9GzNQDFXLMNuKutXt-Z4FgtpXzP5TlhSn3tdZF9Qb4abogqKOpX7nLhAAf_LzlTMQvc5vWlAgOuay6l_5Fq6JvgBpqG8K90TdghrQeWsFKji7gHRk-V5s790qQrUOPbkdLsUp8U_fEBnggjx2l5TntOwHt4kDTTWKuO2292Xclm-WemSKH-w==', start_index=20428)
Annotation(end_index=20529, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYNgExg7Ppg2sKKD3ZFaSNMTYkOuJZR210CQ6bMJHP82KrtAyBw7EJMMhpxPoC6APi_0xMDl4ZkNS8BhihbRxZHPfjriJu6MqunS0iSoJeIQ230vLsNQKowflxjL9eUoIZc5Bp_X8YeCzyiqOcA52kSYRJKL_CXOKOdJnTeNcarA47eP-rGFczSt0EM97zbQcbuHNpctNmJwIASOcxXUpDuBXoOwZsbCubt98=', start_index=20520)
Annotation(end_index=20590, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHn-Tjc4GkHYuSJ73E1C53H1hgVuaRD0eA4nejBAgZ48qXLciqkVgXtzVKuL00rMfkV9dENHmT9k6GOZnJrKJ7-tM04UPYcExBUlh1QCZ971-6uTNCp6jBTbnj51wni6NWMkYVSV0oQ7gCPin0bnrvgkQ==', start_index=20581)
Annotation(end_index=20674, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAPzoaH8O4fxV7PNWVRpdwZsrIQAV_VHgocGs6wDqytT03hunyxITIFIh5Y4pdjfTop6bSKeUZrTr_X76J2CTG-opCigxrlN-xE-81Aga7RxfBtlq4hnsPEpfU1ED28AHu4Tz4gPHqfojhkVl_UEOMDA==', start_index=20664)
Annotation(end_index=20737, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEp0z3OLIiXhXRUkpObJ8vsmD2VR-7kVCssUPrDxdEFTFkTqvpeteLZ38u-lcQxZtFuwysjfkGFZWOWEJbKUr59OGljaL8FoofBHVJgsOUEbdDxGREE3DJmieCO8Kd6', start_index=20728)
Annotation(end_index=20795, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPWDpIxy98leEqt9lhw5WduQWBlSSJQhUTiqLYZoQHTHojh3jYXp2gRE9kSWxwYZfqao2n16Xei1cMWANevenE33S9RmNMJ07gX4TPnY9tV5kt3wLypxXPYSopkPxai8pKqsUrrz6ikfwB0u8bQ0pMgSw-tBFzpKedhH805rGYIvDq6G9qt6EiVKzba5dcBADdZEzsQXZmmsAXEBE8x9bN3pZNYfIolGEZNxzwhG7qex7oJ7fEr0spcg==', start_index=20785)
Annotation(end_index=20882, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHa5E3v1JyRv7swx9hWoCVPg9UB8O3RE9N-2Umx3BNtm15u-6uPqRPO99hF7E7Q9OcYRg0MFyKBmpsjW41RZQfjM5MDuTUXm2EAIxAjz16JfpSrC8PKoyhjao28Ap8CA5TVqEa3Y3BqO7OMOG1yd7wsegbFaFeJqY-LOwx8RPvudMGhZ1LoqpVCZFbb_QpZFtA902cozWfPHinAh6PZa7LoIalQ7qovbJoxAdAWuUhWBuq06emwh5KVIIieDlX59V5Z', start_index=20872)
Annotation(end_index=20968, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUkeyj9gcHFgCfqPYSKXYryTP4pPAWivTP8pyLNh75BxrXp99EtDu3H-nQji5pMGgesE7pA4CrLlt4Szy5n02WoP9xy1MXmBzZbfpVKxawqKyCUUzeJiOCZbC__M-LUUDjuqI9g56PMRHcQ7IgLE9FQfoTbZEfYDIYvv8UiluEnJbdC-WKqgiBwZ6PEIs=', start_index=20958)

## Sources
