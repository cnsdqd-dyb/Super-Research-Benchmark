# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 4451bc48 | **Time:** 291.58s | **Cost:** $0.03562
--------------------------------------------------------------------------------

# The Role of Thermal Runaway Propagation Mechanisms in Designing Safety Redundancy for Lithium-Ion Battery Packs: Considerations of Electrolyte and Separator Stability

## Executive Summary

Thermal runaway propagation represents one of the most critical safety challenges in lithium-ion battery pack design, where the failure of a single cell can cascade through an entire energy storage system with potentially catastrophic consequences. This report examines the fundamental mechanisms underlying thermal runaway propagation and analyzes how understanding these mechanisms directly informs the design of comprehensive safety redundancy systems. The interplay between electrolyte stability and separator integrity emerges as a central consideration, as these components govern both the initiation and progression of thermal events within battery assemblies. By synthesizing current research on propagation pathways, material science advancements, and system-level mitigation strategies, this report provides a framework for understanding how safety redundancy can be engineered at multiple levels—from individual cell components to entire battery pack architectures.

The analysis reveals that effective safety redundancy requires a holistic design approach that addresses thermal, electrical, and mechanical failure modes simultaneously. Understanding the specific mechanisms by which thermal runaway propagates—from direct cell-to-cell conduction through interstitial materials to flame jet-induced heating from vented gases—enables engineers to implement targeted countermeasures at each potential pathway. The stability of electrolyte systems and separator materials under thermal stress conditions fundamentally determines the time available for detection and intervention, making material selection a critical factor in overall system safety design.

## 1. Introduction: The Critical Importance of Thermal Runaway Propagation in Battery Safety

The widespread adoption of lithium-ion batteries in electric vehicles and large-scale energy storage systems has brought unprecedented attention to safety considerations in battery pack design. Electric vehicle battery thermal incidents present a critical engineering challenge, with cell temperatures potentially escalating beyond 150°C during thermal runaway events [1]. When a single cell reaches this threshold, it can trigger a cascade of decomposition reactions, releasing gases at rates exceeding 2L/min per cell and generating heat that threatens adjacent cells in densely packed battery assemblies [1]. The fundamental challenge lies in detecting and containing thermal events at the individual cell level while maintaining the high energy density demands of modern electric vehicles.

Thermal runaway propagation refers to the phenomenon whereby a thermal event originating in one cell spreads to neighboring cells within a battery module or pack, potentially leading to catastrophic system-wide failure. An EV battery has many cells, connected in series and parallel, to increase voltage and range; when a single cell enters thermal runaway, the heat can be propagated from cell to cell throughout the battery pack, escalating the hazard until eventually all cells in the battery pack may fail, venting toxic and flammable gas mixtures [2]. Understanding the mechanisms that govern this propagation is essential for designing effective safety redundancy systems that can prevent localized failures from becoming system-wide disasters.

The design of the whole system—namely the battery pack, inter-cell connections, surrounds (including insulation, packing material, and casing), high voltage system, and the thermal and electrical management systems—is critical to ensuring each cell is operated within its safe parameters, thus mitigating cell failure and preventing cell-to-cell propagation of thermal runaway through the pack in the event that a cell does fail [2]. This holistic perspective recognizes that safety redundancy must be engineered at multiple levels simultaneously, from the molecular stability of electrolyte compositions to the architectural layout of battery modules within the pack enclosure.

## 2. Mechanisms of Thermal Runaway Propagation

### 2.1 The Sequential Stages of Thermal Runaway

Current research on lithium-ion battery thermal runaway typically divides the process into four sequential stages based on temperature thresholds [3]. Initially, when internal temperatures reach the decomposition point of the solid-electrolyte interface (SEI) or cathode-electrolyte interface (CEI), these surface layers break down, triggering exothermic reactions between the electrodes and the electrolyte that cause self-accelerating temperature increases [3]. This first stage represents the critical threshold where reversible operation transitions to irreversible degradation, and where early detection systems must identify anomalous conditions before the process becomes self-sustaining.

As temperatures rise to the separator's melting point, its structural collapse induces internal short circuits, releasing significant heat and marking the transition to the second stage [3]. The separator plays a crucial role in this transition, as its failure mode determines whether internal shorting occurs gradually or catastrophically. Modern separator designs incorporate various mechanisms to delay or prevent this collapse, including ceramic coatings and thermally responsive materials that can halt ion transport before reaching critical temperatures.

This heat then intensifies electrode-electrolyte side reactions in the third stage, generating additional thermal energy that further elevates temperatures [3]. The cathode material undergoes continuous reversible embedding and de-embedding of ions during fast charging and discharging, indicating that the energy and power of the battery is largely determined by the cathode material [4]. The safety of cathode materials is crucial to the electrochemical performance and safety of batteries, attributed to the earlier occurrence of the reaction between the cathode and electrolyte compared to the decomposition reaction of the anode during thermal runaway [4]. Thermal stability can be enhanced by cutting off the chain reaction between cathode and electrolyte through element substitution and protective coating to mitigate thermal runaway in the battery [4].

### 2.2 Heat Transfer Pathways in Cell-to-Cell Propagation

Thermal runaway can spread from one cell to adjacent cells within a battery through a combination of conduction, convection, and radiation [5]. The propagation aspect refers to when that failure spreads to neighboring cells like a domino effect, caused by the heat coming from the failing cell spreading and overheating surrounding cells [6]. Heat and thermal distribution represent a major problem and a key topic in thermal runaway research, but electrical shorting problems can also occur through battery packs during thermal runaway events, leading to internal heating or current dumping from neighboring cells as they experience external short circuits [6].

Research has identified multiple mechanisms that can cause propagation once the initial cell fails [6]. These include thermal transfer through sidewall rupture directly facing onto other cells, release of hot flames through cell vents, and cell-to-cell conduction through interstitial materials [6]. Additionally, an array of electrical short-circuiting issues can result from thermal runaway, with multiple pathways and sources contributing to the propagation risk [6]. This complexity necessitates a multi-faceted approach to safety redundancy design that addresses each potential propagation mechanism.

Three typical modes of thermal runaway propagation have been abstracted from experimental results: high overall temperature, overheating of local area, and uneven thermal contact within battery packs [7]. The mechanisms of these modes are further discussed with the combination of computational models, revealing that high overall temperature, overheating of local area, and uneven thermal contact within battery packs are the three main reasons for hazardous thermal runaway propagation [7]. Moreover, ambient temperature, state of charge, and stacking form are three critical factors that determine the possibility and speed of propagation [7].

### 2.3 Propagation Time and Mitigation Windows

The propagation time determines the time available for mitigation, with studies measuring propagation between 123 seconds and 467 seconds under various test conditions [8]. Considering the increased size and complexity of battery systems, a better understanding of the impact of one cell on the system is essential. It has previously been demonstrated that one single cell failure in multiple battery configurations can generate sufficient heat to initiate thermal runaway in neighboring cells, which in a cascading manner can lead to catastrophic failures [8]. For this reason, battery module and pack safety systems are generally installed to prevent thermal runaway from propagating throughout the entire unit.

The early stages of thermal runaway, including the decomposition of the anode and separator, were considered in an electrochemical-thermal simulation of charge and discharge cycling [9]. The results showed that these decompositions could advance temperature and voltage profiles by 0.07°C over 20 cycles, aiding early prediction of thermal runaway in battery management systems [9]. This work introduces novel models to calculate mass losses, identify reactions, quantify heat release, and estimate thickness or volume reductions in battery components during thermal runaway [9].

## 3. The Critical Role of Electrolyte Stability

### 3.1 Electrolyte Decomposition Pathways

Thermal stability of common electrolytes plays a significant role in lithium-ion battery safety [10]. The most widely used electrolyte for lithium-ion batteries is lithium hexafluorophosphate (LiPF6) salt dissolved in a mixture of alkyl carbonate solvents, including ethylene carbonate (a mandatory component for solid electrolyte interphase growth), dimethyl, diethyl, and ethyl-methyl carbonates [10]. Excellent ionic conductivity combined with electrochemical metastability against a range of electrode materials has made these electrolytes very attractive despite their known shortcomings in thermal stability [10].

Operating cells at temperatures above 70°C resulted in SEI and electrolyte decomposition [11]. Operando spectra collected during heating revealed EC ring-opening as the mechanism of thermal degradation, which resulted in permanent capacity loss [11]. EC thermal decomposition was identical in all cells tested, indicating a homogeneous decomposition reaction independent of electrode material or potential [11]. Thermal stability decreased with increased salt concentration indicating that decomposition is likely catalyzed by LiPF6 decomposition products [11].

Many investigations of the thermal decomposition of electrolytes have focused on rapid decomposition at high temperatures (150–350°C) using differential scanning calorimetry or accelerated rate calorimetry [10]. These measurements provide onset temperatures and reaction rates for SEI decomposition, electrolyte/electrode reactions, and separator failure [10]. However, DSC and ARC data are largely insensitive to electrolyte decomposition at temperatures below 150°C, and the low boiling points of common electrolytes can further complicate interpretation of results [10]. While ARC and DSC investigations are important for understanding the reactions occurring during the later stages of thermal runaway, all events must first undergo decomposition at lower temperatures in the liquid electrolyte [10].

### 3.2 Chemical Evolution and Gas Generation

The chemical evolution at cathode particle boundaries in lithium-ion batteries constitutes a critical factor determining thermal stability, particularly in high-voltage systems exceeding 4.3V [12]. Organic carbonate-based electrolytes employing lithium hexafluorophosphate as the conducting salt exhibit anodic decomposition above 4.7V, generating hydrofluoric acid through hydrolysis [12]. This HF generation accelerates transition metal dissolution from cathode surfaces, with Ni2+/Co2+ leaching rates increasing threefold at 60°C [12]. Concurrently, electrolyte decomposition forms a solid-electrolyte interphase layer with heterogeneous thickness distribution, exposing additional cathode surface area that exacerbates intragranular crack propagation [12].

When the gases vent from the cells they take with them small droplets of the organic solvents from the electrolyte, resulting in a white vapor cloud that may be mistaken for smoke or steam, and which could present an explosion risk [2]. The LEDC in the SEI will decompose to produce CO2 and C2H4 gas at temperatures above 50°C, thereby triggering thermal runaway [12]. The solid propionic lithium and Li2CO3 produced by decomposition will cause changes in the components of the SEI, leading to a decline in performance [12]. Therefore, inhibiting the decomposition of the SEI is crucial for battery safety [12].

### 3.3 Implications for Safety Redundancy Design

The decomposition pathways of electrolytes directly inform the design of safety redundancy systems by defining the temperature thresholds and reaction kinetics that must be managed. The gas generation rates exceeding 2L/min per cell during thermal runaway [1] necessitate robust venting systems that can safely redirect pressurized gases away from adjacent cells and critical system components. Additionally, the flammability of electrolyte vapor clouds requires consideration of explosion prevention measures in pack design, including gas detection systems and ventilation strategies.

Understanding that electrolyte decomposition begins at temperatures as low as 50°C [12] emphasizes the importance of thermal management systems that maintain cells well below these thresholds during normal operation. The catalytic effect of LiPF6 decomposition products on electrolyte stability [11] suggests that electrolyte additives or alternative salt formulations could improve overall system safety by raising the decomposition onset temperature or reducing the exothermicity of decomposition reactions.

## 4. Separator Stability and Thermal Shutdown Mechanisms

### 4.1 Separator Requirements and Failure Modes

Separators have excellent mechanical strength and thermal stability in order to avoid thermal runaway in the battery [13]. Preparing a separator that meets multiple requirements is still a challenge [13]. The separator has to halt ion transport before temperature runs away, representing a critical safety component that can either mitigate or accelerate thermal propagation depending on its design and thermal response characteristics.

A porous composite membrane based on para-aramid nanofibers with the introduction of polyethylene oxide was successfully prepared by electrostatic spinning, and the cell of ANFs/PEO diaphragm showed better electrochemical performance than Celgard 2400 diaphragm [13]. Separation via heat treatment possesses preferable mechanical strength (tensile strength reaches 41.52 MPa) and remarkable thermal stability (almost no thermal contraction at 200°C for 1 h) [13]. In the future, high porosity, good flexibility, and excellent thermal stability will be key requirements for advanced separator designs [13].

### 4.2 Advanced Separator Technologies

A roll-to-roll coating of high-surface-area zeolite creates a zeolite-integrated separator coating that is electronically insulating and highly wettable; its pores adsorb water, dissolved metals and even pre-loaded flame retardants [1]. To shorten shutdown time, a ceramic-backed polyolefin film can be dusted with phase-change particles, yielding a phase-change assisted shutdown separator [1]. Around 130°C the particles melt, soak up heat and flow into the pores, blocking ion transport before the base polymer shrinks [1]. Where ultra-thin cells demand extra robustness, a stacked alumina sheet plus an amphiphilic nanofiber mesh provides a multi-layer ceramic-nanofiber separator that resists puncture [1].

These advanced separator technologies represent direct applications of thermal runaway propagation understanding to safety redundancy design. By incorporating materials that respond to temperature increases by blocking ion transport, these separators create an inherent safety mechanism that can halt the electrochemical processes driving thermal runaway before temperatures reach critical levels. The phase-change materials absorb thermal energy during their phase transition, providing both a thermal buffer and a physical barrier to further reaction.

### 4.3 Integration with Safety Redundancy Systems

The separator's role in safety redundancy extends beyond its intrinsic thermal response properties. By delaying or preventing internal short circuits during thermal events, advanced separators extend the time window available for detection systems to identify anomalous conditions and for cooling or isolation systems to intervene. This extended window is critical for system-level safety redundancy, as it allows multiple independent safety mechanisms to activate in sequence rather than requiring instantaneous response.

The mechanical strength requirements identified for advanced separators [13] also relate to safety redundancy by ensuring that separators maintain integrity under conditions of cell swelling and pressure buildup that precede thermal runaway. A separator that maintains its structural integrity prevents direct contact between electrodes that could create low-resistance internal short circuits, thereby preventing one of the primary initiation mechanisms for thermal runaway.

## 5. Designing Safety Redundancy Based on Propagation Understanding

### 5.1 Multi-Layer Safety Architecture

The complexity of thermal runaway propagation mechanisms necessitates a multi-layer safety architecture that addresses each potential pathway and failure mode. Implementing robust safety measures is essential to prevent hazards associated with lithium-ion batteries, including thermal runaway, toxic gas release, and electrical faults [14]. Hazard mitigation analysis requires a thorough evaluation of potential failure modes, such as overheating or short circuits, to identify vulnerabilities and implement preventive measures [14].

Battery module and pack safety systems are generally installed to prevent thermal runaway from propagating throughout the entire unit [8]. Failure tests and increased understanding of thermal runaway propagation is crucial for several reasons, not only to improve safety designs, but also for performance optimization, minimizing environmental damage and cost reduction [8]. It is also essential that governmental safety standards and regulations reflect the current understanding of propagation mechanisms [8].

A comprehensive safety redundancy system should include multiple independent layers of protection, each capable of detecting or responding to thermal anomalies at different stages of propagation. These layers might include intrinsic cell-level safety features (such as thermal shutdown separators and electrolyte additives), module-level thermal barriers, pack-level cooling and isolation systems, and vehicle-level emergency response systems. The design of each layer should be informed by the specific propagation mechanisms it is intended to address.

### 5.2 Thermal Barriers and Propagation Suppression

By adding phase-change materials, heat pipes, or other cooling technologies, as well as insulating the battery cell's inner case, the heat transfer rate in battery cells can be slowed to arrest or delay thermal runaway propagation [5]. Experimental and computational studies underscore the efficacy of materials like aerogels, ceramic fibers, and phase-change composites, as well as active cooling methods such as liquid cooling and heat pipes, in suppressing thermal runaway propagation [15].

Implementing techniques like employing thermal insulating substances, boosting contact resistance, and upgrading monitoring systems for battery thermal management can significantly reduce the occurrence of thermal failures by identifying areas prone to overheating [16]. The heating position and cell spacing in thermal propagation within battery modules represent critical design parameters that influence propagation likelihood and speed [16]. The bottom end under 20 mm width is the most vulnerable position to thermal runaway, but the vertical-20 mm position did not initiate thermal runaway within the initial 15.83 minutes [16].

### 5.3 Electrical Isolation and Current Management

Enhancing thermal safety in lithium-ion battery packs through parallel cell current dumping mitigation represents an important aspect of safety redundancy design [17]. During thermal runaway events, electrical shorting problems can occur through battery packs, leading to internal heating or current dumping from neighboring cells as they experience external short circuits [6]. Safety redundancy must therefore address both thermal and electrical propagation mechanisms simultaneously.

Electrical isolation strategies include fuse elements that disconnect failing cells from the electrical circuit, contactors that can isolate entire modules or sub-packs, and battery management systems that can actively balance loads to prevent overstressing healthy cells during failure events. The coordination between thermal and electrical isolation systems is critical, as the timing and sequence of isolation actions can significantly influence propagation outcomes.

## 6. System-Level Design Implications

### 6.1 Module Architecture and Pack Layout

The battery housing and module architectures enhancing thermal containment represent critical elements of safety redundancy design [1]. The spatial arrangement of cells within modules and modules within packs directly influences thermal propagation pathways and the effectiveness of containment strategies. Higher numbers of cells increase the chance of fire propagation, making the architectural layout particularly important in large-format battery systems [5].

Location and spacing requirements for lithium-ion battery storage systems include areas with adequate ventilation and spacing to prevent overheating [14]. NFPA mandates a minimum clearance between battery units to reduce the risk of fire propagation [14]. These requirements reflect the understanding that thermal propagation can be suppressed through proper spacing and ventilation design, which allows heat dissipation and prevents the accumulation of thermal energy that could trigger cascading failures.

### 6.2 Venting, Pressure Relief, and Gas Management

Venting, pressure relief and gas flow management systems represent essential components of safety redundancy that directly address the gas generation and release mechanisms during thermal runaway [1]. When the gases vent from the cells they take with them small droplets of the organic solvents from the electrolyte, resulting in a white vapor cloud that may be mistaken for smoke or steam, and which could present an explosion risk [2]. Proper venting design must direct these gases away from adjacent cells and ignition sources while maintaining structural integrity of the pack enclosure.

For energy storage systems, the global combustible concentrations have to be limited at or below 25% of the lower flammability limit after thermal runaway, required by NFPA 69 [18]. These standards and regulations aim to mitigate the risk of thermal runaway by mandating a series of design parameters and safety features [18]. Gas detection systems can provide early warning of venting events, allowing emergency response systems to activate before thermal runaway propagates to additional cells.

### 6.3 Emergency Response and Fire Suppression

Emergency coolant discharge and fire suppression mechanisms represent the final layer of safety redundancy, designed to contain and extinguish thermal events that have progressed beyond the capability of earlier intervention layers [1]. The efficacy and environmental consequences of lithium-ion battery fire extinguishing systems represent active areas of research [2]. Understanding the specific combustion characteristics of electrolyte materials and the thermal decomposition products is essential for designing effective suppression strategies.

Considering the low pressure for air transport, the battery packs shall be stored in a low-pressure environment of 11.6 kPa for at least 6 hours according to UN T 38.3 [18]. These requirements reflect the understanding that battery safety must consider the full range of environmental conditions that may be encountered during transportation and operation.

## 7. Detection, Monitoring, and Predictive Systems

### 7.1 Sensor-Driven Early Detection

Sensor-driven early detection and diagnostic technologies represent critical components of safety redundancy that enable intervention before thermal runaway progresses to propagation [1]. Use of advanced battery management systems to monitor voltage, temperature, and state of charge in real-time allows detection of anomalies and triggering of protective actions [14]. The effectiveness of these systems depends on the placement and sensitivity of sensors, as well as the algorithms used to interpret sensor data and distinguish normal operating variations from incipient failure conditions.

Developing methods to instrument cells to measure internal temperature and pressure during failure represents an important research direction [2]. Internal measurements provide more direct indicators of thermal runaway onset than external temperature sensors, which may lag behind actual cell conditions due to thermal inertia and heat dissipation. However, integrating internal sensors while maintaining cell reliability and manufacturing cost targets presents significant engineering challenges.

### 7.2 Predictive Modeling and Machine Learning

Thermal runaway models play a crucial role in different stages of lithium-ion batteries, covering design, operation, reuse, and accident scenarios [18]. As computational techniques have advanced, new research and applications based on thermal runaway simulation techniques have rapidly emerged in industrial circles [18]. These models enable designers to evaluate the effectiveness of safety redundancy measures before physical prototypes are constructed, reducing development time and cost while improving safety assurance.

Machine learning prediction approaches have emerged as promising tools for thermal runaway detection and prevention [15]. By analyzing patterns in battery operation data, machine learning algorithms can identify subtle precursors to thermal runaway that may not be apparent through traditional threshold-based monitoring. The integration of predictive models with real-time monitoring systems represents a key direction for advancing battery safety capabilities.

### 7.3 Integration with Battery Management Systems

The early stages of thermal runaway, including the decomposition of the anode and separator, were considered in an electrochemical-thermal simulation of charge and discharge cycling using PyBaMM solver [9]. The results showed that these decompositions could advance temperature and voltage profiles by 0.07°C over 20 cycles, aiding early prediction of thermal runaway in battery management systems [9]. This demonstrates how fundamental understanding of decomposition mechanisms can be translated into practical detection capabilities within battery management systems.

Battery management systems must coordinate across multiple safety layers, from cell-level protection circuits to pack-level thermal management systems. The design of these systems requires careful consideration of response times, false positive rates, and the interactions between different safety mechanisms. A thermal alarm signal of 5 minutes is required in EVs before any passenger compartment hazard caused by thermal runaway propagation [18], establishing a performance requirement that safety systems must meet.

## 8. Regulatory Framework and Standards

### 8.1 International Safety Standards

To ensure the sufficient safety quality of lithium-ion batteries available on the market, numerous safety requirements have been established by business assessment standards and national compulsory testing regulations, including GB 38031-2020, UL 2580-2020, GTR 20, and UN ECE R100 [18]. These standards reflect the accumulated understanding of thermal runaway propagation mechanisms and establish minimum safety requirements that battery designs must meet.

Consensus and industry standards programs include the National Fire Protection Association NFPA 855 Standard for the Installation of Stationary Energy Storage Systems, the International Electrotechnical Commission IEC 62281 Safety of Primary and Secondary Lithium Cells and Batteries During Transport, and Underwriters Laboratories UL 2054 Standard for Household and Commercial Batteries [19]. Compliance with these standards provides a baseline level of safety assurance, though the rapidly evolving understanding of thermal runaway mechanisms may require standards to be updated more frequently than traditional development cycles allow.

### 8.2 Implications for Safety Redundancy Design

Regulatory requirements establish minimum performance criteria that safety redundancy systems must meet, but the specific mechanisms by which those requirements are met are often left to designer discretion. This approach allows innovation in safety system design while ensuring that all commercial products meet a common baseline of safety performance. Understanding the propagation mechanisms that underlie these standards enables designers to implement safety redundancy more efficiently and effectively.

The requirement for a 5-minute warning before passenger compartment hazards [18] establishes a specific timing requirement that safety systems must satisfy. This requirement directly reflects the understanding of thermal runaway propagation dynamics—the time required for a localized cell failure to propagate to the point where it threatens passenger safety. Designing safety redundancy to meet this requirement requires consideration of detection time, response time, and the propagation time under various failure scenarios.

## 9. Future Directions and Emerging Technologies

### 9.1 Solid-State and Advanced Electrolyte Systems

Different chemistries can have vastly different mechanisms and thresholds behind what happens with thermal runaway [6]. The removal of liquid aprotic volatile electrolytes and transition to lithium metal is being pursued as a potentially safer alternative, though thermal runaway and propagation can still occur and has occurred in field applications [6]. A recent example is the Paris Balore electric bus fire, which employed solid state or semi-solid state polymer electrolyte with lithium anode and LFP cathode, yet still experienced thermal runaway [6].

These observations underscore that while advanced electrolyte systems may raise the thresholds for thermal runaway initiation, they do not eliminate the need for comprehensive safety redundancy design. The propagation mechanisms may differ between liquid and solid electrolyte systems, requiring different approaches to detection and mitigation. Research into solid-state battery safety must therefore continue to address propagation mechanisms even as it pursues the benefits of improved energy density and reduced flammability.

### 9.2 Advanced Materials and Composites

The development of advanced thermal barrier materials represents an active area of research with significant implications for safety redundancy design. Materials like aerogels, ceramic fibers, and phase-change composites have demonstrated efficacy in suppressing thermal runaway propagation [15]. Challenges in scalability, cost, and standardization are critically analyzed, with recommendations for interdisciplinary collaboration to advance these technologies toward commercial implementation [15].

The integration of multiple safety functions into single material systems represents an emerging design approach. For example, separators that combine thermal shutdown functionality with flame retardant storage [1] or structural components that provide both mechanical support and thermal insulation demonstrate how understanding of propagation mechanisms can guide multifunctional material design.

### 9.3 Second-Life and Aged Battery Considerations

How ageing influences the stability and safety of lithium-ion batteries in second life applications, for example energy storage systems, represents an important research question [2]. Aged batteries may have degraded safety margins due to SEI growth, lithium plating, or other degradation mechanisms that alter their thermal behavior. Safety redundancy designs must therefore consider not only new battery behavior but also the evolution of safety characteristics over the battery lifetime.

The impact of failure in confined spaces, such as underground car parks, also requires further investigation [2]. The accumulation of vented gases and the constraints on emergency response in such environments may alter propagation dynamics and require modified safety approaches. Understanding these context-dependent factors is essential for designing safety redundancy that performs reliably across the full range of operating conditions.

## 10. Conclusion

The thermal runaway propagation mechanism plays a fundamental role in designing safety redundancy for lithium-ion battery packs, with electrolyte and separator stability serving as critical determinants of both propagation likelihood and the time available for intervention. Understanding that thermal runaway can spread through conduction, convection, and radiation pathways [5], potentially generating sufficient heat to initiate cascading failures across entire battery systems [8], provides the foundation for designing effective multi-layer safety architectures.

The stability of electrolyte systems under thermal stress defines the temperature thresholds and reaction kinetics that safety systems must manage, while separator integrity determines whether internal short circuits occur gradually or catastrophically. Advanced separator technologies incorporating phase-change materials, ceramic coatings, and nanofiber structures demonstrate how fundamental understanding of thermal behavior can be translated into intrinsic safety features [1]. Similarly, electrolyte additives and alternative formulations offer opportunities to raise decomposition onset temperatures and reduce the exothermicity of decomposition reactions.

Effective safety redundancy requires a holistic design approach that addresses thermal, electrical, and mechanical failure modes simultaneously [6]. The multiple mechanisms that can cause propagation—including direct thermal transfer, flame jet heating, and electrical short-circuiting—necessitate correspondingly diverse mitigation strategies [6]. Battery management systems must integrate detection, prediction, and response capabilities across multiple time scales, from real-time monitoring to predictive algorithms that identify incipient failures before they escalate.

The regulatory framework established through standards such as NFPA 855, IEC 62281, and various national requirements [14][19] reflects the accumulated understanding of propagation mechanisms and establishes minimum safety performance criteria. However, the rapidly evolving nature of battery technology requires continuous refinement of both scientific understanding and safety standards to ensure that safety redundancy designs remain effective as battery chemistries and architectures continue to advance.

Future research directions including solid-state electrolytes, advanced thermal barrier materials, and machine learning-based prediction systems offer promising opportunities to enhance safety redundancy capabilities. However, the fundamental importance of understanding propagation mechanisms will persist regardless of the specific technologies employed, as effective safety design requires knowing not only what might fail but how failures can spread through interconnected systems.

---

## References

[1] https://xray.greyb.com/ev-battery/prevent-thermal-runaway-in-ev-battery

[2] https://www.faraday.ac.uk/wp-content/uploads/2023/07/Faraday_Insights_17_July2023_FINAL.pdf

[3] https://www.mdpi.com/1996-1073/18/16/4240

[4] https://www.mdpi.com/2571-6255/8/6/223

[5] https://www.sciencedirect.com/science/article/abs/pii/S2352152X23002918

[6] https://www.youtube.com/watch?v=JjsZEKsxRlM

[7] https://iopscience.iop.org/article/10.1149/MA2019-01/6/591

[8] https://docs.nrel.gov/docs/fy24osti/87353.pdf

[9] https://www.sciencedirect.com/science/article/pii/S0378775324019785

[10] https://iopscience.iop.org/article/10.1149/2.1051816jes

[11] https://pubs.acs.org/doi/10.1149/2.1051816jes

[12] https://www.mdpi.com/1996-1073/18/16/4240

[13] https://www.mdpi.com/2571-6255/8/6/223

[14] https://www.large-battery.com/blog/nfpa-855-lithium-battery-safety-standards/

[15] https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5282610

[16] https://www.nature.com/articles/s41598-025-07824-7

[17] https://www.sciencedirect.com/science/article/pii/S0306261920318761

[18] https://pmc.ncbi.nlm.nih.gov/articles/PMC11089405/

[19] https://www.osha.gov/sites/default/files/publications/OSHA4480.pdf

## Annotations


## Sources
[1] https://docs.nrel.gov/docs/fy24osti/87353.pdf
[2] https://iopscience.iop.org/article/10.1149/2.1051816jes
[3] https://iopscience.iop.org/article/10.1149/MA2019-01/6/591
[4] https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5282610
[5] https://pmc.ncbi.nlm.nih.gov/articles/PMC11089405/
[6] https://www.faraday.ac.uk/wp-content/uploads/2023/07/Faraday_Insights_17_July2023_FINAL.pdf
[7] https://www.large-battery.com/blog/nfpa-855-lithium-battery-safety-standards/
[8] https://www.mdpi.com/1996-1073/18/16/4240
[9] https://www.mdpi.com/2571-6255/8/6/223
[10] https://www.nature.com/articles/s41598-025-07824-7
[11] https://www.osha.gov/sites/default/files/publications/OSHA4480.pdf
[12] https://www.sciencedirect.com/science/article/abs/pii/S2352152X23002918
[13] https://www.sciencedirect.com/science/article/pii/S0378775324019785
[14] https://www.youtube.com/watch?v=JjsZEKsxRlM
[15] https://xray.greyb.com/ev-battery/prevent-thermal-runaway-in-ev-battery