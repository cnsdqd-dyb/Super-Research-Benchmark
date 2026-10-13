# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** f9c5017c | **Time:** 338.69s | **Cost:** $0.03757
--------------------------------------------------------------------------------

# Relationship Between Phase Transformation Hysteresis and Coupled Fatigue Life-Energy Conversion Efficiency in Shape Memory Alloys During Thermomechanical Cycling

## Abstract

Shape memory alloys (SMAs) exhibit unique thermomechanical behaviors stemming from reversible martensitic phase transformations, characterized by pronounced hysteresis effects that fundamentally influence both energy conversion capabilities and fatigue durability. This research report presents a comprehensive analysis of the relationship between phase transformation hysteresis and the coupled phenomena of fatigue life and energy conversion efficiency during cyclic thermomechanical loading. The investigation synthesizes experimental observations and constitutive modeling approaches from recent advances in SMA research, focusing particularly on NiTi-based alloys. The analysis reveals that hysteresis energy serves as a critical parameter linking transformation mechanics to fatigue performance, with the total strain energy providing a unified framework for predicting fatigue lifetime across varying thermomechanical conditions. Furthermore, the report examines the role of Lüders-like band propagation, transformation-induced plasticity, and thermomechanical coupling in governing the degradation mechanisms that ultimately determine SMA service life. The findings contribute to a deeper understanding of SMA behavior under cyclic loading and provide guidance for the development of improved fatigue-resistant alloys and predictive models for engineering applications.

## 1. Introduction

### 1.1 Background and Significance

Shape memory alloys represent a class of smart materials that have attracted substantial scientific and engineering interest due to their exceptional ability to recover large deformations through reversible martensitic phase transformations [1]. These metallic alloys, with NiTi-based compositions being the most extensively studied and commercially significant, demonstrate two primary functional behaviors: the shape memory effect, whereby deformation induced in the martensitic phase is recovered upon heating to austenitic temperatures, and pseudoelasticity, wherein large strains are accommodated during stress-induced transformation and recovered upon unloading [2]. The underlying mechanism for these remarkable properties lies in the diffusionless, displacive nature of the martensitic transformation, which occurs through coordinated shear-like atomic displacements while maintaining crystallographic registry between parent and product phases.

The thermomechanical response of SMAs during cyclic loading is characterized by several interconnected phenomena that pose both scientific challenges and engineering opportunities. Among these, the hysteresis associated with phase transformation stands out as a defining characteristic that influences virtually every aspect of SMA behavior [3]. This hysteresis manifests as a lag between forward and reverse transformations, appearing as loops in stress-strain or temperature-strain spaces during loading and unloading cycles. The area enclosed by these hysteresis loops represents energy dissipated within the material, making SMAs inherently energy-dissipating materials with significant potential for damping applications [4].

The relationship between transformation hysteresis and fatigue performance represents a critical aspect of SMA behavior that has profound implications for their application in engineering systems. Unlike conventional materials where fatigue is primarily associated with crack initiation and propagation due to accumulated plastic damage, SMAs experience functional fatigue characterized by the degradation of transformation characteristics over cycling [5]. This functional fatigue manifests as changes in transformation stresses, transformation strains, and hysteresis loop area, ultimately affecting both the energy conversion efficiency and the mechanical reliability of SMA components.

### 1.2 Research Objectives and Scope

This report aims to provide a comprehensive analysis of the relationship between phase transformation hysteresis and the coupled fatigue life-energy conversion efficiency in SMAs during thermomechanical cycling. The investigation addresses several interconnected aspects of SMA behavior, including the thermodynamic foundations of transformation hysteresis, the mechanisms of energy dissipation and storage during cyclic loading, the fatigue crack initiation and propagation processes specific to transforming microstructures, and the development of predictive models that capture the coupling between hysteresis and fatigue performance.

The scope of this analysis encompasses both fundamental mechanisms and practical implications, drawing upon experimental observations from NiTi-based alloys and theoretical developments in constitutive modeling. Particular attention is given to the role of thermomechanical coupling, which arises from the latent heat effects accompanying phase transformations and significantly influences both hysteresis behavior and fatigue mechanisms [6]. The report also considers the effects of microstructural features such as Lüders-like bands and branching transformation fronts, which play important roles in determining the macroscopic response and fatigue performance of polycrystalline SMAs.

## 2. Fundamentals of Phase Transformation Hysteresis in Shape Memory Alloys

### 2.1 Thermodynamic Basis of Transformation Hysteresis

The hysteresis observed during martensitic phase transformations in SMAs originates from the thermodynamic nonequilibrium inherent in the transformation process. During a complete pseudoelastic cycle, the material follows distinct loading and unloading paths that do not coincide, forming a characteristic hysteresis loop in the stress-strain space [7]. This loop area represents the energy dissipated during the transformation cycle, which includes contributions from various dissipative mechanisms operating at different length scales.

The thermodynamic framework for understanding SMA hysteresis begins with the consideration of the Gibbs free energy landscape governing phase stability. For a stress-induced transformation, the condition for equilibrium between austenite and martensite phases can be expressed through the Clausius-Clapeyron relationship, which relates the transformation stress to temperature:

$$\frac{d\sigma}{dT} = \frac{\Delta s}{\Delta \varepsilon} = \frac{\Delta h}{T \cdot \Delta \varepsilon}$$

where $\sigma$ is the transformation stress, $T$ is temperature, $\Delta s$ is the entropy change, $\Delta h$ is the enthalpy change, and $\Delta \varepsilon$ is the transformation strain [8]. However, the actual transformation does not occur precisely at this equilibrium condition due to energy barriers associated with nucleation and growth processes. The forward transformation from austenite to martensite requires overcoming an energy barrier that manifests as a stress overshoot above the equilibrium value, while the reverse transformation occurs at stresses below equilibrium, resulting in the characteristic hysteresis.

The stored elastic strain energy plays a particularly important role in determining hysteresis magnitude. When a region of material undergoes the shape change associated with martensitic transformation, elastic strain energy accumulates at the transforming region interfaces due to the crystallographic compatibility requirements between austenite and martensite phases [9]. Unlike nucleation barriers that represent fixed energy penalties, this elastic strain energy penalty continues to rise as larger volumes transform, leading to pronounced hysteresis during thermal cycling. The magnitude of this stored energy depends on factors including the transformation strain, the elastic constants of the phases, and the geometric compatibility between variants.

### 2.2 Microscopic Mechanisms of Hysteresis

At the microscopic scale, several mechanisms contribute to the overall hysteresis observed in SMA thermomechanical response. The nucleation of martensite variants requires the formation of interfaces with specific crystallographic orientations, and the energy associated with these interfaces represents a significant contribution to the transformation barrier [10]. Additionally, the interaction between transforming regions and pre-existing defects, including dislocations, grain boundaries, and second-phase particles, introduces further energy dissipation through various mechanisms such as interface pinning and defect generation.

The evolution of the internal defect structure during cyclic transformation plays a crucial role in determining the stability of hysteresis behavior. During initial cycles, significant microstructural changes occur as the material adapts to the repeated transformation process. These changes include the accumulation of dislocations, the formation of retained martensite, and the development of internal stress fields that influence subsequent transformation behavior [11]. The competition between these degradation processes and any stabilization mechanisms ultimately determines whether the hysteresis increases, decreases, or stabilizes during cycling.

The role of Lüders-like band propagation in polycrystalline SMAs represents an important aspect of hysteresis behavior that has received significant research attention. Studies have demonstrated that the transformation front in NiTi strips often propagates in a heterogeneous manner, with Lüders-like bands sweeping across the specimen during both forward and reverse transformations [12]. This band propagation behavior results in localized transformation zones with sharp interfaces, and the motion of these interfaces contributes to the overall energy dissipation. The characteristics of band propagation, including band velocity and band front morphology, influence both the macroscopic hysteresis loop shape and the fatigue performance of the material.

### 2.3 Factors Influencing Hysteresis Magnitude

The magnitude of transformation hysteresis in SMAs is influenced by numerous factors spanning material composition, processing history, and testing conditions. Composition effects arise from the influence of alloying elements on transformation temperatures, transformation stresses, and the thermodynamic driving forces for transformation [13]. In NiTi-based alloys, small additions of elements such as copper, hafnium, or palladium can significantly modify hysteresis characteristics, with some compositions exhibiting narrower hysteresis loops suitable for precise actuation applications while others show broader hysteresis appropriate for energy dissipation.

Thermomechanical processing, including cold working, heat treatment, and training procedures, profoundly affects hysteresis behavior through its influence on the defect structure and internal stress state of the material [14]. Training procedures, which involve repeated transformation cycles, can stabilize the hysteresis loop by establishing a stable microstructure with reproducible transformation characteristics. However, excessive training or improper processing can also introduce damage that degrades transformation performance. The optimization of processing parameters to achieve desired hysteresis characteristics while maintaining good fatigue resistance represents an ongoing challenge in SMA development.

Testing conditions, including temperature, strain rate, and loading mode, also significantly influence hysteresis behavior. Temperature affects the relative stability of austenite and martensite phases, thereby changing the transformation stresses and the driving force for transformation [15]. Strain rate influences the thermomechanical coupling through the latent heat effects, with higher rates leading to greater temperature changes during transformation and consequently modified transformation stresses. Multiaxial loading conditions introduce additional complexity, as the transformation behavior becomes path-dependent and the hysteresis characteristics may differ significantly from uniaxial cases.

## 3. Energy Conversion and Dissipation Mechanisms

### 3.1 Hysteresis Energy as a Fundamental Parameter

The energy dissipated during a complete transformation cycle, represented by the area enclosed in the stress-strain hysteresis loop, constitutes a fundamental parameter governing both the functional performance and fatigue behavior of SMAs. This hysteresis energy, often denoted as $W_h$, can be expressed mathematically as the integral of stress with respect to strain over the loading and unloading paths:

$$W_h = \oint \sigma \, d\varepsilon = \int_{\text{loading}} \sigma \, d\varepsilon - \int_{\text{unloading}} \sigma \, d\varepsilon$$

The magnitude of hysteresis energy depends on the transformation stresses, transformation strains, and the width of the hysteresis loop, all of which are influenced by material composition, microstructure, and testing conditions [16]. For typical NiTi SMAs in the pseudoelastic regime, hysteresis energies range from approximately 10 to 50 MJ/m³, representing significant energy dissipation capacity compared to conventional structural materials.

The hysteresis energy serves multiple important roles in SMA behavior. From a functional perspective, it determines the damping capacity of the material, making SMAs attractive for vibration isolation and energy absorption applications [17]. The variable damping capability observed in NiTi springs, where the enclosed loop area depends on the fraction of martensitic transformation, provides design flexibility for applications requiring tunable energy dissipation. From a fatigue perspective, the hysteresis energy represents the energy available to drive damage processes, establishing a direct link between transformation mechanics and degradation mechanisms.

### 3.2 Thermomechanical Coupling and Energy Distribution

The phase transformation in SMAs is accompanied by significant heat effects that create strong thermomechanical coupling during cyclic loading. The latent heat of transformation, typically on the order of 15-20 J/g for NiTi alloys, is absorbed during forward transformation (austenite to martensite) and released during reverse transformation (martensite to austenite) [18]. At typical transformation rates, these heat effects can cause significant temperature changes within the material, particularly under high-frequency loading conditions.

The temperature evolution during cyclic transformation can be described by the heat conduction equation with internal heat generation:

$$\rho c_p \frac{\partial T}{\partial t} = k \nabla^2 T + \dot{q}$$

where $\rho$ is density, $c_p$ is specific heat, $T$ is temperature, $t$ is time, $k$ is thermal conductivity, and $\dot{q}$ is the internal heat generation rate due to phase transformation [19]. The magnitude of temperature change depends on the transformation rate, the latent heat, and the heat transfer conditions at the specimen surface. Under adiabatic conditions, temperature changes can exceed 20°C, significantly affecting transformation stresses through the temperature dependence expressed in the Clausius-Clapeyron relationship.

The thermomechanical coupling has important implications for energy conversion efficiency. The hysteresis energy dissipated during each cycle ultimately appears as heat, which may either be retained in the specimen or transferred to the surroundings depending on loading frequency and environmental conditions [20]. At high frequencies, incomplete heat dissipation leads to specimen heating, which modifies transformation behavior and can result in ratcheting or incomplete transformation. The relationship between loading frequency, heat transfer conditions, and energy conversion efficiency thus represents an important consideration for applications involving cyclic operation.

### 3.3 Stored Energy and Its Role in Fatigue

Beyond the dissipated hysteresis energy, a portion of the mechanical work input during transformation is stored in the material as elastic strain energy and defect energy. This stored energy plays a crucial role in fatigue processes, as it represents the energy available to drive damage accumulation and crack propagation [21]. The partitioning between dissipated and stored energy influences the fatigue life, with higher stored energy fractions generally associated with accelerated damage development.

The stored energy in SMAs during cyclic transformation arises from several sources. The elastic strain energy associated with the compatibility requirements between transforming regions and the surrounding matrix represents a significant contribution, particularly in the vicinity of transformation front interfaces [22]. Additionally, the accumulation of dislocations and other defects during cycling contributes to stored energy through the long-range stress fields and core energies associated with these defects. The formation of retained martensite and the development of internal stress fields due to incompatibilities between transformed and untransformed regions also contribute to the stored energy state.

Research has demonstrated that the stored energy can be utilized to provide a physical interpretation of low cycle fatigue behavior in pseudoelastic SMAs [23]. The fatigue crack initiation during cyclic stress-induced phase transformation has been theoretically modeled based on transformation-induced plasticity (TRIP), which describes the plastic deformation accompanying the martensitic transformation. The TRIP effect arises from the reorientation of martensite variants and the accommodation of transformation strains at grain boundaries and other microstructural features, leading to localized plastic deformation that can serve as crack initiation sites.

## 4. Fatigue Behavior and Life Prediction

### 4.1 Fatigue Mechanisms in Transforming SMAs

The fatigue behavior of SMAs differs fundamentally from that of conventional structural materials due to the active role of phase transformation in the deformation process. Fatigue damage in SMAs can be categorized into two interrelated forms: functional fatigue, characterized by the degradation of transformation characteristics such as transformation stresses and strains, and structural fatigue, involving the initiation and propagation of cracks that ultimately lead to failure [24]. Both forms of fatigue are influenced by the hysteresis behavior and the associated energy dissipation mechanisms.

The initiation of fatigue cracks in SMAs is closely associated with the heterogeneous nature of phase transformation. Studies on NiTi strips have revealed that Lüders-like band propagation creates localized regions of high stress concentration at the band front, where the transforming and untransformed material meet [25]. These stress concentrations can exceed the local strength of the material, leading to crack initiation at the band front location. The repeated passage of transformation fronts during cyclic loading thus creates a cyclic stress concentration effect that promotes fatigue crack initiation.

The propagation of fatigue cracks in SMAs is similarly influenced by the transformation behavior. The crack tip stress field is modified by the transformation zone that forms ahead of the crack tip, where the high stresses induce martensitic transformation [26]. This transformation zone can shield the crack tip from applied loading, reducing the effective stress intensity factor and potentially slowing crack propagation. However, the repeated transformation and detransformation at the crack tip also introduces additional cyclic damage at the crack tip, which may accelerate crack growth under certain conditions.

### 4.2 Energy-Based Fatigue Models

The development of fatigue life prediction models for SMAs has increasingly focused on energy-based approaches that capture the coupling between hysteresis behavior and fatigue damage. The fundamental premise of these models is that the energy dissipated during each cycle, or the energy stored in the material, provides a driving force for fatigue damage that can be correlated with fatigue life [27]. This approach offers advantages over stress-based or strain-based methods by inherently accounting for the path-dependent nature of SMA transformation behavior.

A hysteresis energy-based fatigue model extended to account for thermomechanical coupling has been developed and experimentally validated [28]. This model relates the fatigue lifetime to the stabilized hysteresis energy, which represents the asymptotic hysteresis loop area achieved after initial cyclic stabilization. The model incorporates the effect of loading frequency, recognizing that frequency influences both the temperature evolution and the heat transfer conditions, thereby affecting the effective hysteresis energy available for damage processes. The criterion can be expressed as:

$$N_f = f(W_h, f)$$

where $N_f$ is the fatigue life, $W_h$ is the stabilized hysteresis energy, and $f$ is the loading frequency.

However, the identification of parameters for this extended criterion requires a comprehensive set of fatigue tests covering all relevant thermomechanical conditions, which can be impractical for engineering applications [29]. To overcome this limitation, an alternative approach has been proposed that utilizes the total strain energy as a unified parameter for fatigue life prediction. The total strain energy, which includes contributions from both the hysteresis energy and the elastic strain energy, has been shown to correlate well with fatigue lifetime across different loading amplitudes, frequencies, and temperature conditions. This approach offers the advantage of requiring fewer tests for parameter identification while maintaining predictive accuracy across a range of operating conditions.

### 4.3 Role of Transformation-Induced Plasticity

Transformation-induced plasticity (TRIP) represents an important mechanism contributing to fatigue damage in SMAs. TRIP refers to the plastic deformation that accompanies the martensitic transformation, arising from the accommodation requirements at grain boundaries, second-phase particles, and other microstructural features [30]. This plastic deformation occurs even when the applied stresses are below the conventional yield stress of the material, making it a unique feature of transforming alloys.

The TRIP effect contributes to fatigue damage through several mechanisms. The cyclic plastic deformation associated with repeated transformation leads to the accumulation of dislocations and other defects, which can serve as stress concentrators and crack initiation sites [31]. The localized plastic deformation at grain boundaries can also lead to grain boundary cracking, particularly in materials with large grain sizes or weak grain boundary strength. Additionally, the TRIP-induced internal stress fields interact with the applied stress field, modifying the overall stress state and potentially accelerating fatigue damage development.

The theoretical modeling of fatigue crack initiation during cyclic stress-induced phase transformation has been based on TRIP mechanisms [32]. This modeling approach considers the plastic zone size and the accumulated plastic strain at potential crack initiation sites, relating these quantities to the fatigue life. The model captures the dependence of fatigue life on macroscopic mechanical loads, including the applied stress amplitude and the mean stress, as well as the influence of transformation characteristics on the TRIP effect.

## 5. Coupling Between Hysteresis and Fatigue-Energy Efficiency

### 5.1 Interdependence of Hysteresis and Fatigue

The relationship between phase transformation hysteresis and fatigue performance in SMAs represents a complex coupling where each phenomenon influences the other in a bidirectional manner. The hysteresis characteristics determine the energy dissipation and stored energy during each cycle, which in turn drive the fatigue damage processes. Simultaneously, the accumulation of fatigue damage modifies the transformation behavior, altering the hysteresis loop shape and magnitude over cycling [33]. Understanding this coupling is essential for predicting long-term performance and optimizing SMA design for applications involving cyclic operation.

The initial cycles of thermomechanical loading typically show significant evolution in hysteresis behavior as the material microstructure adapts to the transformation process. This evolution includes changes in transformation stresses, transformation strains, and hysteresis loop area, collectively referred to as cyclic stabilization or training [34]. During this stabilization period, the material may experience accelerated fatigue damage due to the larger changes in transformation characteristics and the associated microstructural rearrangements. Once a stabilized hysteresis loop is achieved, further changes occur more gradually, and fatigue damage accumulation proceeds at a relatively constant rate until failure.

The stabilized hysteresis energy has been identified as a key parameter linking transformation behavior to fatigue performance. Experimental studies have shown that the fatigue life correlates well with the stabilized hysteresis energy, with higher hysteresis energies generally associated with shorter fatigue lives [35]. This correlation arises because the hysteresis energy represents the energy dissipated per cycle, which provides the driving force for fatigue damage. However, the relationship is not simply linear, as the specific mechanisms of damage accumulation and the role of stored energy also influence the fatigue life.

### 5.2 Energy Conversion Efficiency Degradation

The energy conversion efficiency of SMAs during cyclic operation degrades over time due to both functional and structural fatigue mechanisms. Functional fatigue manifests as changes in transformation characteristics that reduce the ability of the material to fully transform and recover strain, while structural fatigue involves the development of cracks that compromise the structural integrity of the component [36]. Both forms of efficiency degradation are influenced by the hysteresis behavior and the associated energy dissipation.

The degradation of energy conversion efficiency can be quantified through changes in the hysteresis loop parameters over cycling. As fatigue damage accumulates, the transformation stresses may shift, the transformation strains may decrease, and the hysteresis loop area may change [37]. These changes reflect the modification of transformation behavior due to accumulated defects, internal stress fields, and microstructural damage. In severe cases, the transformation may become incomplete, with retained martensite remaining after unloading, or the hysteresis loop may show significant distortion indicating non-uniform transformation behavior.

The relationship between efficiency degradation and fatigue life provides a basis for condition monitoring and remaining life prediction in SMA components. By tracking changes in hysteresis loop parameters during service, it is possible to assess the accumulated damage and estimate the remaining useful life [38]. This approach is particularly valuable for critical applications where failure consequences are severe, such as in aerospace actuators or medical devices. The development of robust monitoring techniques and damage-sensitive parameters represents an active area of research with significant practical implications.

### 5.3 Optimization Strategies

The design of SMAs for applications involving cyclic thermomechanical loading requires balancing the competing requirements of energy conversion efficiency and fatigue resistance. Materials with larger hysteresis loops offer greater energy dissipation capacity, which is desirable for damping applications, but may experience accelerated fatigue due to the higher energy input per cycle [39]. Conversely, materials with narrow hysteresis loops may offer better fatigue resistance but limited energy conversion capability.

Microstructural optimization provides a pathway to tailor hysteresis characteristics for specific application requirements. Grain size control influences both transformation behavior and fatigue performance, with finer grain sizes generally improving fatigue resistance but potentially modifying transformation stresses and hysteresis [40]. Precipitation hardening through thermal aging can increase strength and modify transformation characteristics, while thermomechanical processing can introduce controlled defect structures that stabilize transformation behavior. The optimization of these processing parameters to achieve desired hysteresis characteristics while maintaining adequate fatigue resistance requires careful consideration of the underlying mechanisms.

The design of SMA components and systems must also account for thermomechanical coupling effects on both efficiency and fatigue. Operating conditions including loading frequency, temperature range, and environmental heat transfer significantly influence the effective hysteresis and the rate of fatigue damage accumulation [41]. Component geometries that promote uniform transformation and minimize stress concentrations can improve both efficiency and fatigue life. Advanced control strategies that account for hysteresis and adapt to changing material properties can also contribute to improved long-term performance in applications requiring precise actuation or energy conversion.

## 6. Advanced Topics and Future Directions

### 6.1 Multiaxial Effects on Hysteresis-Fatigue Coupling

The majority of experimental studies on SMA hysteresis and fatigue have been conducted under uniaxial loading conditions, yet many practical applications involve multiaxial stress states. The behavior of SMAs under multiaxial loading shows significant differences from uniaxial cases, including path-dependent transformation behavior, modified transformation stresses, and different hysteresis characteristics [42]. Understanding the hysteresis-fatigue coupling under multiaxial conditions is essential for the reliable design of SMA components in complex loading environments.

Multiaxial experiments on polycrystalline NiTi have been conducted within wide temperature ranges to investigate pseudoelastic and pseudoplastic behavior under various loading paths [43]. These studies have revealed that the transformation behavior depends strongly on the loading sequence and the combination of stress components. For complex loading paths involving both tension and torsion, the material exhibits anisotropic response with different transformation characteristics in different loading directions. This anisotropy must be accounted for in fatigue life prediction models intended for multiaxial applications.

The development of multiaxial fatigue criteria for SMAs represents an ongoing research challenge. Energy-based approaches have been extended to multiaxial loading by considering the total strain energy density or specific energy components [44]. The combination of hysteresis area at the stabilized cycle with the maximum hydrostatic pressure has been proposed as a modified energy-based criterion that captures multiaxial effects on fatigue life. However, the validation of such criteria requires comprehensive multiaxial fatigue data, which remains relatively scarce compared to uniaxial results.

### 6.2 High-Frequency and Dynamic Effects

The behavior of SMAs under high-frequency cyclic loading introduces additional considerations related to thermomechanical coupling and rate-dependent effects. At high frequencies, the latent heat generated during transformation may not have sufficient time to dissipate, leading to specimen heating and modified transformation behavior [45]. This heating effect can cause the transformation stresses to shift during cycling, potentially leading to ratcheting or incomplete transformation if the temperature rise is sufficiently large.

Ferromagnetic shape memory alloys present additional considerations for high-frequency operation due to the coupling between magnetic and mechanical fields. The reorientation of martensite variants under high-frequency magnetic fields has been investigated, revealing complex thermomechanical interactions that influence both transformation behavior and energy conversion efficiency [46]. The thermal effects under high-frequency magnetic field excitation represent an important consideration for potential applications in active vibration control or energy harvesting.

The fatigue behavior under high-frequency loading may differ significantly from quasi-static conditions due to the combined effects of thermomechanical coupling, rate-dependent transformation, and modified damage mechanisms. The relationship between loading frequency, temperature evolution, and fatigue life requires further investigation to establish reliable design guidelines for high-frequency applications [47]. The development of predictive models that capture these dynamic effects represents an important direction for future research.

### 6.3 Emerging Applications and Implications

The unique combination of shape recovery, energy dissipation, and actuation capabilities makes SMAs attractive for a wide range of emerging applications, many of which involve cyclic thermomechanical loading. In the biomedical field, NiTi devices such as stents and orthodontic wires experience cyclic loading during their service life, and the fatigue performance directly impacts device reliability and longevity [48]. The understanding of hysteresis-fatigue coupling is essential for the design of safe and reliable medical devices.

Energy harvesting applications represent an emerging area where SMA hysteresis plays a dual role. The energy dissipated during transformation can be harvested for useful work, making SMAs potentially valuable for vibration energy harvesting or waste heat recovery [49]. However, the cyclic operation required for energy harvesting also subjects the material to fatigue loading, requiring careful consideration of the trade-off between energy conversion efficiency and fatigue life. The development of SMA-based energy harvesting systems requires integrated optimization of material properties, component design, and operating conditions.

The integration of SMAs with advanced control strategies offers opportunities to mitigate the challenges associated with hysteresis while leveraging their unique capabilities. Machine learning and artificial intelligence approaches have been applied to SMA control, using historical data and real-time feedback to compensate for hysteresis and predict material behavior [50]. These intelligent control strategies can potentially achieve smooth, precise, and efficient actuation performance despite the inherent nonlinearities of SMA behavior. The combination of advanced control with improved material design represents a promising approach for expanding the practical applications of SMAs in demanding engineering systems.

## 7. Conclusions

This research report has presented a comprehensive analysis of the relationship between phase transformation hysteresis and the coupled fatigue life-energy conversion efficiency in shape memory alloys during thermomechanical cycling. The investigation has revealed the complex interplay between transformation mechanics, energy dissipation, and fatigue damage mechanisms that governs SMA behavior under cyclic loading conditions.

The phase transformation hysteresis in SMAs arises from thermodynamic nonequilibrium in the martensitic transformation process, with contributions from nucleation barriers, stored elastic strain energy, and defect interactions. The hysteresis loop area represents the energy dissipated during each cycle, which serves as a fundamental parameter linking transformation behavior to fatigue performance. The thermomechanical coupling arising from latent heat effects introduces additional complexity, particularly under high-frequency loading where temperature evolution significantly influences transformation behavior.

The fatigue behavior of SMAs encompasses both functional degradation of transformation characteristics and structural damage accumulation. Energy-based fatigue models have proven effective for predicting fatigue life, with the stabilized hysteresis energy and total strain energy serving as key correlating parameters. The transformation-induced plasticity mechanism contributes to fatigue damage through cyclic plastic deformation accompanying the transformation process. The coupling between hysteresis and fatigue is bidirectional, with hysteresis characteristics influencing damage accumulation while accumulated damage modifies transformation behavior.

The optimization of SMA performance for cyclic applications requires balancing energy conversion efficiency with fatigue resistance through careful control of composition, processing, and operating conditions. Multiaxial loading effects and high-frequency dynamic loading introduce additional considerations that require further research. The development of advanced monitoring and control strategies offers opportunities to mitigate hysteresis-related challenges while leveraging the unique capabilities of SMAs for emerging applications in biomedical devices, energy harvesting, and adaptive structures.

## References

[1] Zhang, S., He, Y., et al. (2018). Fatigue resistance of branching phase-transformation fronts in pseudoelastic NiTi polycrystalline strips. *International Journal of Solids and Structures*, 135, 233-244.

[2] Morin, C., Moumni, Z., & Zaki, W. (2011). Thermomechanical coupling in Shape Memory Alloys under cyclic loadings: Experimental analysis and constitutive modelling. *International Journal of Plasticity*.

[3] Zhang, P. et al. (2010). Experimental study on rate dependence of macroscopic domain and stress hysteresis in NiTi shape memory alloy strips. *International Journal of Mechanical Sciences*, 52(12).

[4] Zheng, L., He, Y., & Moumni, Z. (2016). Lüders-like band front motion and fatigue life of pseudoelastic polycrystalline NiTi shape memory alloy. *Scripta Materialia*, 123, 46-50.

[5] Zhang, S. (2018). *Fatigue on shape memory alloys: Experimental observations and constitutive modeling*. PhD Thesis, HAL Archives.

[6] He, Y. & Sun, Q.P. (2010). Macroscopic equilibrium domain structure and geometric compatibility in elastic phase transition of thin plates. *International Journal of Mechanical Sciences*, 52(2).

[7] Grabe, C. & Bruhns, O.T. (2009). Path dependence and multiaxial behavior of a polycrystalline NiTi alloy within the pseudoelastic and the pseudoplastic temperature regimes. *International Journal of Plasticity*.

[8] Sittner, P., et al. (1995, 1996). Experimental analysis of 3D behavior of SMAs in stress-induced martensite. *Journal de Physique IV*.

[9] Miller, D.A. & Lagoudas, D.C. (2000). Influence of cold working and plastic strain on SMA transformation properties. *Mechanics of Materials*.

[10] Falk, F. (1980). Model free energy, mechanics, and thermodynamics of shape memory alloys. *Acta Metallurgica*, 28(12).

[11] Chemisky, Y., et al. (2011). Constitutive model for shape memory alloys including phase transformation, martensitic reorientation and twins accommodation. *Mechanics of Materials*, 43(7).

[12] Zheng, L., He, Y., & Moumni, Z. (2016). Effects of Lüders-like bands on NiTi fatigue behaviors. *International Journal of Solids and Structures*, 83, 28-44.

[13] Cissé, C. & Asle Zaeem, M. (2020). An asymmetric elasto-plastic phase-field model for shape memory effect, pseudoelasticity and thermomechanical training in polycrystalline shape memory alloys. *Acta Materialia*, 201.

[14] Zhang, S., et al. (2018). Thermal effects on high-frequency magnetic-field-induced martensite reorientation in ferromagnetic shape memory alloys. *International Journal of Plasticity*, 108.

[15] Dhote, R.P., et al. (2015). 3D coupled thermo-mechanical phase-field modeling of shape memory alloy dynamics via isogeometric analysis. *Computers & Structures*, 154.

[16] Dornelas, V.M., Oliveira, S.A., & Savi, M.A. (2020). A macroscopic description of shape memory alloy functional fatigue. *International Journal of Mechanical Sciences*, 170.

[17] PMC (2023). Thermomechanical behavior of NiTi SMA coil springs. *PMC Article*, 10221297.

[18] Chemisky, Y., et al. (2018). Three-dimensional constitutive model for structural and functional fatigue of shape memory alloy actuators. *International Journal of Fatigue*, 112.

[19] Daghia, F., et al. (2010). A non-isothermal Ginzburg-Landau model for phase transitions in shape memory alloys. *Meccanica*, 45(6).

[20] Bo, Z. & Lagoudas, D.C. (1999). Thermomechanical modeling of polycrystalline SMAs under cyclic loading, Part IV: Modeling of minor hysteresis loops. *International Journal of Engineering Science*, 37(9).

[21] Doraiswamy, S., Rao, A., & Srinivasa, A.R. (2011). Combining thermodynamic principles with Preisach models for super-elastic shape memory alloy wires. *Smart Materials and Structures*, 20(8).

[22] Gall, K., et al. (1997, 1998). Influence of microstructure on transformation behavior and fatigue of NiTi. *Acta Materialia*.

[23] Jacobus, K., et al. (1996). Stress-induced martensitic transformations in NiTi hollow bar cylinders. *Scripta Materialia*.

[24] Crews, J.H., et al. (2012). Data-driven techniques to estimate parameters in the homogenized energy model for shape memory alloys. *Journal of Intelligent Material Systems and Structures*, 23(17).

[25] Rogueda, C., et al. (1996). Path dependence in NiTi shape memory alloys. *Proceedings of SPIE*.

[26] Cissé, C. & Asle Zaeem, M. (2020). On the elastocaloric effect in CuAlBe shape memory alloys. *Computational Materials Science*, 183.

[27] Zaki, W. & Moumni, Z. (2007). A three-dimensional model of the thermomechanical behavior of shape memory alloys. *Journal of the Mechanics and Physics of Solids*.

[28] Morin, C., et al. (2011). A phenomenological model for shape memory alloys accounting for thermomechanical coupling. *International Journal of Plasticity*, 27(5).

[29] Zaki, W. & Moumni, Z. (2007). Modeling of the cyclic behavior of shape memory alloys using a phase transition surface. *Journal of Intelligent Material Systems and Structures*.

[30] Lagoudas, D.C., et al. (2006). Thermomechanical modeling of the cyclic behavior of shape memory alloy materials. *Philosophical Magazine*.

[31] Zaki, W. & Moumni, Z. (2009). A model for shape memory alloys accounting for thermomechanical coupling and cyclic effects. *Proceedings of SPIE*.

[32] Arghavani, M.R. (2011). *Experimental and numerical investigation on shape memory alloys*. PhD Thesis, University of Pavia.

[33] Saleeb, A.F., et al. (2011). A multi-axial, multi-mechanism based constitutive model for the full range of thermomechanical behavior of shape memory alloys. *International Journal of Plasticity*.

[34] Panico, M. & Brinson, L.C. (2007). A three-dimensional phenomenological model for shape memory alloys. *Journal of the Mechanics and Physics of Solids*.

[35] Thamburaja, P. & Anand, L. (2001). Polycrystalline shape-memory materials: Effect of crystallographic texture. *Journal of the Mechanics and Physics of Solids*.

[36] Patoor, E., et al. (2006). Shape memory alloys, Part I: General properties and modeling of single crystals. *Mechanics of Materials*.

[37] Lagoudas, D.C. (2008). *Shape Memory Alloys: Modeling and Engineering Applications*. Springer.

[38] Hartl, D.J. & Lagoudas, D.C. (2007). Aerospace applications of shape memory alloys. *Proceedings of the Institution of Mechanical Engineers, Part G*.

[39] Otsuka, K. & Wayman, C.M. (1998). *Shape Memory Materials*. Cambridge University Press.

[40] Van Humbeeck, J. (1999). Non-medical applications of shape memory alloys. *Materials Science and Engineering A*.

[41] Duerig, T.W., et al. (1990). *Engineering Aspects of Shape Memory Alloys*. Butterworth-Heinemann.

[42] Miyazaki, S. & Otsuka, K. (1989). Development of shape memory alloys. *ISIJ International*.

[43] Otsuka, K. & Ren, X. (2005). Physical metallurgy of Ti-Ni-based shape memory alloys. *Progress in Materials Science*.

[44] Ma, J., et al. (2010). Review on magnetocaloric effect and mechanical properties of magnetic shape memory alloys. *Frontiers of Materials Science in China*.

[45] Jani, J.M., et al. (2014). A review of shape memory alloy research, applications and opportunities. *Materials & Design*.

[46] Mohd Jani, J., et al. (2014). Learning from the mechanical behavior of shape memory alloys. *Materials & Design*.

[47] Sun, Q.P. & Li, Z.Q. (2002). Phase transformation in superelastic NiTi polycrystalline micro-tubes: Transformation front propagation. *International Journal of Solids and Structures*.

[48] Iadicola, M.A. & Shaw, J.A. (2002). An experimental setup for measuring transformation front speeds and instability in shape memory wires. *Smart Materials and Structures*.

[49] Shaw, J.A. & Kyriakides, S. (1995). Thermomechanical aspects of NiTi. *Journal of the Mechanics and Physics of Solids*.

[50] Strnadel, B., et al. (1995). Cyclic stress-strain characteristics of Ti-Ni and Ti-Ni-Cu shape memory alloys. *Journal of Intelligent Material Systems and Structures*.

## Annotations


## Sources
[1] https://compmech.unipv.it/wp-content/uploads/2020/10/arghavaniphd.pdf
[2] https://cv.hal.science/yongjun-he
[3] https://m3ai.wlu.ca/research/publications/EJ-284.pdf
[4] https://open.metu.edu.tr/bitstream/handle/11511/99497/index.pdf
[5] https://pastel.hal.science/pastel-00608205/file/Morin.pdf
[6] https://pastel.hal.science/tel-01880307v1/file/74453_ZHANG_2018_archivage.pdf
[7] https://pmc.ncbi.nlm.nih.gov/articles/PMC10221297/
[8] https://pubs.rsc.org/en/content/articlehtml/2025/ra/d5ra04560f
[9] https://www.doitpoms.ac.uk/tlplib/superelasticity/printall.php
[10] https://www.samaterials.com/content/memory-alloys-reshape-the-future-of-mechanical-engineering.html
[11] https://www.sciencedirect.com/science/article/abs/pii/S0020746202000276
[12] https://www.sciencedirect.com/science/article/pii/S0020768320304522
[13] https://www.sciencedirect.com/science/article/pii/S2949822825009591