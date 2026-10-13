# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 49d7118a | **Time:** 274.94s | **Cost:** $0.10061
--------------------------------------------------------------------------------

# Does Impedance Matching in Microgrid Control Affect Small-Signal Stability Under Distributed Power Fluctuations?

## Abstract

This research report investigates the relationship between impedance matching strategies in microgrid control systems and their impact on small-signal stability under conditions of distributed power fluctuations. The analysis draws upon contemporary research in power electronics, control theory, and microgrid stability assessment to provide a comprehensive examination of this critical topic. The findings reveal that impedance matching is not merely a passive design consideration but an active determinant of small-signal stability, particularly when constant power loads and renewable energy sources introduce dynamic variations in power injection. The report synthesizes impedance-based stability analysis methods, droop control mechanisms, and active damping strategies to establish a framework for understanding how impedance characteristics influence microgrid stability margins. Key findings indicate that improper impedance matching can lead to negative incremental resistance phenomena, Nyquist contour encirclements of the critical point, and potential system instability, while well-designed impedance coordination through virtual impedance injection and optimized droop coefficients can significantly enhance stability boundaries.

## 1. Introduction

### 1.1 Background and Motivation

The proliferation of distributed energy resources (DERs) integrated through power electronic converters has fundamentally transformed the architecture and operational paradigms of modern power systems. Microgrids, as localized energy systems capable of operating in both grid-connected and islanded modes, exemplify this transformation by incorporating renewable energy sources, energy storage systems, and diverse load types within a coordinated control framework [1]. However, the high penetration of inverter-based resources introduces complex stability challenges that differ substantially from those encountered in conventional power systems dominated by synchronous generators.

Small-signal stability represents a fundamental prerequisite for reliable microgrid operation, encompassing the system's ability to maintain synchronism and stable equilibrium following small disturbances [7]. Unlike large-scale power systems where stability is primarily governed by electromechanical dynamics, microgrid small-signal stability is heavily influenced by the interaction between power electronic converter controls, network impedances, and the dynamic characteristics of connected loads [9]. The distributed nature of power generation in microgrids, combined with the inherent variability of renewable energy sources, creates operating conditions where power fluctuations can excite unstable modes if impedance relationships are not properly managed.

### 1.2 Research Objective and Scope

This report addresses the central question of whether impedance matching in microgrid control affects small-signal stability under distributed power fluctuations. The investigation encompasses the theoretical foundations of impedance-based stability analysis, the mechanisms through which impedance mismatches manifest as stability issues, and the control strategies employed to mitigate adverse effects. The scope includes both AC and DC microgrid configurations, with particular attention to the role of constant power loads, droop-controlled inverters, and reactive power control modes in determining stability boundaries.

### 1.3 Report Structure

The subsequent sections of this report are organized as follows: Section 2 provides the theoretical foundations of impedance-based stability analysis, including the Nyquist stability criterion and its application to microgrid systems. Section 3 examines the specific mechanisms through which distributed power fluctuations interact with impedance characteristics to influence stability. Section 4 presents an analysis of control strategies that leverage impedance matching for stability enhancement. Section 5 discusses design guidelines and practical considerations, and Section 6 concludes with a summary of key findings and recommendations for future research.

## 2. Theoretical Foundations of Impedance-Based Stability Analysis

### 2.1 Impedance Characterization in Microgrid Systems

The impedance-based approach to stability analysis represents a powerful methodology for assessing the interaction between sources and loads in power electronic systems. In this framework, each component of the microgrid is characterized by its input and output impedances, transforming the complex multi-component system into a source-load interconnection that can be analyzed using established control theory principles [7]. The source impedance represents the equivalent impedance seen from the output terminals of a power source or converter, while the load impedance represents the impedance presented by downstream components to the source.

For microgrid systems, the impedance characterization must account for the multiple control loops inherent in modern power electronic converters. A typical grid-forming inverter, for instance, exhibits impedance characteristics that depend on the voltage control loop, current control loop, and any supplementary control functions such as droop control or virtual impedance injection [4]. The resulting impedance is not a fixed parameter but a function of frequency, operating point, and control parameters, necessitating frequency-domain analysis to capture the complete stability assessment.

The impedance of photovoltaic (PV) inverters has been shown to vary significantly depending on the reactive power control mode employed [1]. Under different control modes, the inverter output impedance exhibits distinct characteristics in the D-Q reference frame, with the volt-var droop mode presenting particular challenges from a stability perspective. Research has demonstrated that when a PV inverter operates under volt-var droop mode, the eigenvalue loci can encircle the critical (-1, j0) point on the Nyquist plot, indicating instability according to the Generalized Nyquist Criterion (GNC) [1]. This finding underscores the importance of considering control mode selection as an integral part of impedance matching strategy.

### 2.2 The Nyquist Stability Criterion in Microgrid Applications

The Nyquist stability criterion provides the theoretical foundation for impedance-based stability assessment by relating the encirclements of the critical point in the Nyquist plot to the number of unstable poles in the closed-loop system [2]. For a microgrid interconnection, the loop gain is typically defined as the ratio of the source output impedance to the load input impedance, expressed as $L(s) = Z_{out}(s)/Z_{in}(s)$. If the Nyquist contour of $L(s)$ does not enclose the (-1, j0) point, and given that the source and load impedances contain no right-half-plane (RHP) poles, the interconnected system is deemed stable [2].

The application of the Nyquist criterion to microgrid systems requires careful consideration of the multi-input multi-output (MIMO) nature of the interconnection. The Generalized Nyquist Criterion extends the single-loop analysis to MIMO systems by examining the characteristic loci of the return ratio matrix [1]. This approach is particularly relevant for microgrids with multiple inverter-based sources operating in parallel, where the interaction between multiple control loops can give rise to complex stability phenomena that cannot be captured by single-loop analysis alone.

The Bode plot analysis complements the Nyquist assessment by providing frequency-domain insight into impedance magnitudes and phases. Comparative Bode plots of PV inverter impedance under different control modes reveal significant variations in both magnitude and phase characteristics, particularly in the frequency range where potential interactions with grid impedance may occur [1]. The phase relationship between source and load impedances determines whether the net impedance appears inductive or capacitive at various frequencies, directly influencing the stability margins of the system.

### 2.3 Small-Signal Modeling for Stability Assessment

The small-signal stability analysis of microgrids relies on linearized models that capture the system dynamics around a specific operating point. For droop-controlled inverters, the small-signal model can be derived by perturbing the nonlinear power equations and control relationships [5]. The resulting state-space representation enables eigenvalue analysis, which identifies the natural modes of the system and their damping characteristics.

The small-signal model of a typical DC microgrid with droop-controlled interfacing converters can be expressed through the relationship between capacitor voltage, inductor current, and power references [5]. Perturbing the steady-state equations yields expressions that relate small-signal variations in voltage and current to the droop coefficients and filter parameters. The derived transfer functions reveal how the equivalent output impedance of parallel-connected converters depends on the controller parameters and the virtual impedance introduced through the control loops.

Research has established that the small-signal stability of microgrids depends critically on the relationship between droop gains and line parameters [4]. Specifically, the stability of frequency droop control has been shown to depend on the X/R ratio of the transmission lines, with resistive-dominated networks (low X/R ratios) presenting different stability characteristics than reactance-dominated networks [4]. This dependence highlights the importance of considering network impedance characteristics when designing droop control parameters for microgrid stability.

## 3. Impact of Distributed Power Fluctuations on Stability

### 3.1 Constant Power Loads and Negative Impedance Characteristics

Constant power loads (CPLs) represent one of the most significant sources of instability in microgrid systems, particularly in DC microgrids where tightly regulated power converters present negative incremental resistance to the source [3]. Unlike passive loads that exhibit positive impedance characteristics, CPLs maintain constant power consumption regardless of voltage variations, resulting in an impedance that decreases as voltage increases. This negative impedance characteristic can destabilize the system by counteracting the natural damping provided by source impedances and filter components.

The instability mechanism arising from CPLs has been extensively documented in the literature [3][8]. When a CPL is connected to a DC bus through an input filter, the negative impedance of the load can interact with the filter inductance and capacitance to produce oscillatory modes. If the net damping of these modes becomes negative, the system exhibits growing oscillations that can lead to voltage collapse or equipment damage. The stability boundary depends on the relative magnitudes of the CPL negative impedance and the source impedance, with higher source impedance generally providing better damping but at the cost of increased voltage regulation challenges.

The behavioral characteristics of CPLs have been mapped onto generalized models that enable systematic stability analysis [8]. By abstracting the nonlinear CPL behavior into an equivalent negative resistance, the stability assessment can be performed using linear techniques such as eigenvalue analysis or impedance-based methods. The derived stability conditions provide design guidelines for ensuring that the system remains stable across the expected operating range of power fluctuations.

### 3.2 Renewable Energy Variability and Impedance Interactions

The inherent variability of renewable energy sources introduces time-varying power injection that can excite stability issues in microgrid systems. Solar photovoltaic systems, in particular, exhibit power output variations due to cloud transients, temperature changes, and irradiance fluctuations. These variations manifest as disturbances at the DC bus of grid-connected inverters, propagating through the control system and potentially affecting the AC-side impedance characteristics.

Research on PV inverter stability has revealed that the reactive power control mode significantly influences the impedance characteristics under fluctuating power conditions [1]. The volt-var droop mode, while providing voltage support capabilities, can lead to stability issues when the PV inverter interacts with weak grid conditions. The Nyquist analysis demonstrates that under this control mode, the eigenvalue loci can encircle the critical point, indicating potential instability [1]. This finding is particularly relevant for distribution systems with high PV penetration, where the aggregate effect of multiple inverters operating in volt-var mode can create system-wide stability concerns.

The interaction between PV inverter impedance and grid impedance forms a critical determinant of stability under fluctuating conditions. When the grid impedance is significant relative to the inverter output impedance (weak grid conditions), the effective loop gain increases, potentially reducing stability margins [2]. The time constant of the control system plays a crucial role in determining whether the constant power behavior exhibits positive or negative resistivity at the oscillation frequency, with improper time constant selection leading to unstable operation [2].

### 3.3 Distributed Generation Fluctuations and Multi-Converter Interactions

Microgrids typically contain multiple distributed generation units operating in parallel, each contributing to the overall power balance while interacting through the common network. The distributed nature of generation means that power fluctuations from any single source propagate through the network, affecting voltage profiles and potentially exciting unstable interactions with other converters. The impedance matching between converters and the network determines the degree of interaction and the resulting stability characteristics.

The parallel operation of interfacing converters in DC microgrids introduces additional complexity to the stability analysis [5]. When multiple converters share the load current, the equivalent output impedance seen by the load is the parallel combination of individual converter impedances. The small-signal analysis reveals that the combined impedance depends on the droop coefficients, controller parameters, and virtual impedance settings of each converter. The interaction between converters through the droop control mechanism can either enhance or degrade stability depending on the parameter coordination.

Research on multi-agent stabilization systems has proposed methods for coordinating multiple converters to maintain stability during power fluctuations [3]. The approach involves modifying CPL set-points during power variations and optimizing the effect of each stabilizing agent on system stability. The objective function defined for agent design ensures that the collective action of converters provides adequate damping across the expected operating range. This coordinated approach represents an advancement over decentralized control strategies that may not adequately account for multi-converter interactions.

## 4. Impedance Matching Strategies for Stability Enhancement

### 4.1 Droop Control and Virtual Impedance Design

Droop control represents the primary decentralized control strategy for power sharing among parallel converters in microgrids. By establishing a relationship between power output and frequency (for active power) or voltage and reactive power (for reactive power), droop control enables autonomous operation without high-speed communication links. However, the basic droop control mechanism can lead to stability issues if the droop coefficients are not properly coordinated with the network impedance characteristics.

The small-signal stability analysis of droop-controlled microgrids has established relationships between droop gains and stability boundaries [4][9]. For frequency droop control, the stability depends on the X/R ratio of the lines connecting inverters, with optimal droop coefficients varying depending on whether the network is reactance-dominated or resistance-dominated. In systems with low X/R ratios (resistive networks), the traditional P-ω droop may not provide adequate decoupling, necessitating modified droop characteristics or supplementary control actions.

Virtual impedance injection has emerged as a powerful technique for shaping the output impedance of converters to achieve desired stability characteristics [5]. By synthesizing a virtual impedance through the control system, designers can modify the effective impedance seen by the load without adding physical components. The virtual impedance can be designed to provide positive damping at frequencies where instability might otherwise occur, counteracting the negative impedance effects of CPLs or weak grid conditions.

The design of virtual impedance-based stabilizers involves perturbing the control equations and deriving the resulting impedance expressions [5]. The analysis shows that the virtual impedance appears in series with the physical impedance in the equivalent circuit model, allowing the designer to adjust both resistance and reactance components. For DC microgrids, the virtual impedance design has been shown to enable stable operation with CPLs by ensuring that the total impedance exhibits positive resistivity at the oscillation frequency [8].

### 4.2 Active Damping Methods

Active damping methods provide an alternative to passive impedance modification by using feedback control to introduce damping effects without physical resistors. These methods are particularly attractive for microgrid applications because they avoid the power losses associated with passive damping while offering flexibility in adapting to changing operating conditions [2]. The active damping approach injects a stabilizing current component that modifies the effective impedance seen by the source.

The distinction between passive and active damping methods lies in the implementation approach and resulting system characteristics [2]. Passive damping methods enhance stability margins by adding actual passive devices such as resistors or RC circuits, but these additions result in continuous power losses and reduced efficiency. Active damping methods, in contrast, achieve similar damping effects through control algorithms that modify the converter behavior, eliminating the need for additional passive components while maintaining high efficiency.

Research on active damping for grid-connected converters has demonstrated the importance of time constant selection in achieving stable operation [2]. The control system must ensure that the constant power unit impedance exhibits positive resistivity near the oscillation frequency. When the time constant is too small to meet this condition, the system exhibits unstable behavior characterized by growing oscillations in voltage and current. The active damping design must therefore carefully consider the frequency range of potential instabilities and adjust the control parameters accordingly.

The dual-current control strategy represents an advanced active damping approach that provides enhanced stability margins for grid-connected inverters with LCL filters [2]. By incorporating additional control loops, this strategy can actively damp the resonance modes of the LCL filter while maintaining good dynamic response characteristics. The approach has been validated through both simulation and experimental results, demonstrating its effectiveness in improving stability under various operating conditions.

### 4.3 Impedance Coordination in Multi-Converter Systems

The coordination of impedance characteristics among multiple converters in a microgrid requires careful attention to both the individual converter designs and their interactions through the network. The aggregate impedance seen by any load or source depends on the parallel or series combination of impedances from all connected converters, creating a complex interdependence that must be analyzed for stability assessment.

The small-signal model of parallel converter systems reveals that the combined output impedance depends on the sum of individual converter contributions [5]. By discretizing the transfer functions and analyzing the dominant modes, designers can identify the critical parameters that influence stability. The analysis shows that the total impedance can be expressed in terms of the individual controller parameters and droop coefficients, enabling systematic design of the coordinated system.

The fault-tolerant multi-agent stabilization system (MASS) represents a comprehensive approach to impedance coordination in microgrids [3]. This method ensures robust stability even when converters are suddenly shut down or the microgrid undergoes reconfiguration. The approach modifies CPL set-points during power fluctuations and optimizes the effect of each stabilizing agent through a defined objective function. The resulting design provides coordinated impedance shaping across the entire system, enhancing stability margins under adverse conditions.

## 5. Design Guidelines and Practical Considerations

### 5.1 Stability-Oriented Design Methodology

The design of microgrid control systems for small-signal stability requires a systematic methodology that considers impedance characteristics from the initial design stages. The first step involves characterizing the impedance of all sources and loads across the frequency range of interest, identifying potential interaction frequencies where instability might occur. This characterization should account for the operating point dependence of impedance, as converter impedance can vary significantly with power level and control mode.

The impedance matching design should aim to ensure that the source output impedance and load input impedance satisfy the Nyquist stability criterion across the expected operating range. For systems with CPLs, this requires that the source impedance provides sufficient positive damping to counteract the negative impedance of the loads [8]. The design guidelines derived from sensitivity analysis can inform decisions regarding converter location, reactive power control mode selection, and droop coefficient coordination.

The optimization of controller parameters for stability represents a critical aspect of the design methodology. Research has demonstrated that microgrids dominated by power electronic converters exhibit high small-signal stability when controllers are well-designed and all relevant parameters are optimized [7]. The optimization process should consider the trade-offs between stability margins, dynamic response speed, and power sharing accuracy, as these objectives can conflict with each other.

### 5.2 Control Mode Selection Considerations

The selection of reactive power control mode for inverters significantly impacts the impedance characteristics and resulting stability margins. Comparative studies of different control modes have revealed that the volt-var droop mode can lead to stability issues under certain conditions, while other modes may provide more favorable impedance characteristics [1]. The choice of control mode should therefore consider both the voltage regulation objectives and the stability implications.

For PV inverter integration, the IEEE 1547 standard requires reactive power control capability, increasing the complexity of inverter control while providing opportunities for grid support [1]. However, the additional control functions must be designed carefully to avoid stability issues. The analysis shows that different reactive power control modes result in distinctly different impedance characteristics, with implications for the stability of the interconnection with the distribution system.

The coordination of control modes among multiple inverters in a microgrid requires attention to potential interactions. When multiple inverters operate in the same control mode, their combined impedance characteristics may differ significantly from a single inverter, potentially affecting stability boundaries. The design should consider the aggregate effect of all inverters and ensure that the combined system satisfies stability criteria.

### 5.3 Network Parameter Considerations

The impedance characteristics of the distribution network play a crucial role in determining microgrid stability. Unlike transmission systems where lines are primarily reactance-dominated, distribution systems often exhibit significant resistance, resulting in low X/R ratios that affect droop control performance and stability boundaries [4]. The design must account for these impedance characteristics when selecting control parameters.

The sensitivity analysis of PV integration has shown that the impact on voltage profile and system stability depends on the location of inverters and the network topology [1]. The sensitivity matrices developed for stability assessment are related to system topology and impedance, providing guidance for optimal inverter placement. The analysis reveals that system power loss follows a U-shaped trajectory as PV inverter capacity increases, with the optimal size depending on specific system characteristics.

For meshed network configurations, the impedance-based stability analysis must consider the complex interconnection paths between sources and loads. The generalized Nyquist criterion provides a framework for analyzing MIMO systems with multiple interconnection paths, enabling the identification of potential stability issues arising from network topology [1]. The design guidelines derived from such analysis can inform both controller design and network planning decisions.

## 6. Conclusion

### 6.1 Summary of Key Findings

This research report has examined the relationship between impedance matching in microgrid control and small-signal stability under distributed power fluctuations. The analysis reveals that impedance matching is indeed a critical determinant of small-signal stability, with improper matching capable of inducing instability through several mechanisms. The negative incremental resistance characteristic of constant power loads, when combined with inadequate source impedance damping, can lead to unstable oscillatory behavior. Similarly, the interaction between converter control modes and network impedance can produce eigenvalue loci that encircle the critical point on the Nyquist plot, indicating instability according to the Generalized Nyquist Criterion.

The findings demonstrate that distributed power fluctuations from renewable energy sources and variable loads create operating conditions where impedance interactions become particularly significant. The variability of PV power output, combined with different reactive power control modes, can shift the impedance characteristics of inverters into ranges that compromise stability margins. The time constant selection for control systems must ensure positive resistivity at oscillation frequencies, with improper selection leading to unstable operation.

The report also highlights the effectiveness of impedance matching strategies for stability enhancement. Droop control parameter coordination, virtual impedance injection, and active damping methods provide mechanisms for shaping impedance characteristics to achieve desired stability margins. The coordinated control approaches, including multi-agent stabilization systems, offer enhanced robustness compared to decentralized strategies by accounting for multi-converter interactions.

### 6.2 Recommendations for Practice

Based on the analysis presented, several recommendations can be offered for practitioners designing microgrid control systems. First, impedance characterization should be performed across the full frequency range of interest for all sources and loads, accounting for operating point dependence and control mode effects. This characterization provides the foundation for stability assessment and impedance matching design.

Second, the design of droop coefficients and virtual impedance should consider the network X/R ratio and the specific stability boundaries for the system configuration. The optimization of these parameters should balance stability requirements with power sharing accuracy and dynamic response objectives. Third, active damping methods should be considered as alternatives to passive damping to avoid efficiency penalties while achieving desired stability margins.

Fourth, the coordination of control modes among multiple converters should be analyzed using MIMO stability criteria to identify potential interaction issues. The aggregate effect of multiple converters operating in parallel can significantly affect stability boundaries compared to single-converter analysis. Finally, the ongoing monitoring of impedance characteristics during operation can provide early warning of potential stability issues as operating conditions change.

### 6.3 Future Research Directions

Several areas warrant further investigation to advance the understanding of impedance matching effects on microgrid stability. The development of real-time impedance estimation methods could enable adaptive impedance matching that adjusts to changing operating conditions, potentially improving stability margins across a wider operating range. The integration of machine learning techniques for stability prediction and control optimization represents an emerging research direction with significant potential.

The extension of impedance-based stability analysis to hybrid AC-DC microgrids and multi-bus configurations presents additional challenges that require further research. The interaction between AC and DC subsystems through interlinking converters creates complex impedance networks that may require enhanced analytical methods. The consideration of communication delays in distributed control systems also introduces additional dynamics that affect stability and require careful analysis.

Finally, the validation of theoretical findings through hardware-in-the-loop testing and field demonstrations remains essential for translating research advances into practical implementations. The gap between analytical results and real-world performance must be addressed through comprehensive testing programs that account for component tolerances, measurement errors, and unmodeled dynamics.

## References

[1] Tang, Y. (2021). PV Inverter Impedances in D-Q Frame under Different Q Control Modes. *Virginia Tech Works*, 10919/111227.

[2] Guan, Y. et al. (2018). The dual-current control strategy of grid-connected inverter with LCL filter. *IEEE Transactions on Power Electronics*, 34(6), 5940-5952.

[3] Hosseinipour, A. & Hojabri, H. (2020). Small-signal stability analysis and active damping control of DC microgrids integrated with distributed electric springs. *IEEE Transactions on Smart Grid*, 11(5), 3737-3747.

[4] Dynamic phasor modeling and stability analysis of microgrids. *Wisconsin Library*, 1711.dl/SZVOA23R3UJKO9A.

[5] Xiaonan, L. et al. (2014). DC microgrid droop control based on multi-converter. *ECCE 2014*, vbn.aau.dk.

[6] Mitra, J. et al. Voltage dip mitigation using DG in a microgrid. *Michigan State University*, egr.msu.edu.

[7] Eberlein, S. (2021). Stability analysis of medium voltage microgrids. *University of Stuttgart*, ieh.uni-stuttgart.de.

[8] Zhu, X. & Meng, X. (2020). Stability analysis and active damping control of DC microgrid. *High Voltage Technology*, 46(5), 1670-1681.

[9] PNNL-30066. (2020). Small-signal stability constraints in networked microgrid design. *Pacific Northwest National Laboratory*.

## Annotations


## Sources
[1] https://asset.library.wisc.edu/1711.dl/SZVOA23R3UJKO9A/R/file-3c713.pdf
[2] https://cdn.misoenergy.org/Power%20System%20Analysis%20&%20Planning%20Report631170.pdf
[3] https://onlinelibrary.wiley.com/journal/16136829?msockid=0d242dd36ecc6bf5166a3b3f6f546a25
[4] https://per.mit.edu/wp-content/uploads/2016/09/cpCOMPEL16_Belk-Inam-Grid-Stability-online-post.pdf
[5] https://upcommons.upc.edu/bitstreams/460718c9-e215-4677-aa6b-77cad5903c95/download
[6] https://vbn.aau.dk/ws/files/204359710/20140624_Final_ECCE2014_Xiaonan_Lu.pdf
[7] https://vbn.aau.dk/ws/files/255745154/Review_on_Control_of_DC_Microgrids.pdf
[8] https://vbn.aau.dk/ws/files/255996890/FINAL_VERSION.pdf
[9] https://vtechworks.lib.vt.edu/bitstream/handle/10919/111227/Tang_Y_D_2021.pdf
[10] https://www.adelaide.edu.au/press/ua/media/477/uap-small-signal-ebook.pdf
[11] https://www.egr.msu.edu/~mitraj/research/pubs/jour/ipinnimo-mitra_epsr_voltage_dip.pdf
[12] https://www.ieh.uni-stuttgart.de/dokumente/dissertationen/2021_Dissertation_Langfassung_Eberlein.pdf
[13] https://www.linkedin.com/posts/prof-ahmed-al-durra-47b3126b_robust-distributed-secondary-control-for-activity-7364917867093340160-gCAl
[14] https://www.nature.com/articles/s41598-025-14523-w
[15] https://www.nature.com/articles/s41598-025-32695-3_reference.pdf
[16] https://www.nrel.gov/docs/fy23osti/84000.pdf
[17] https://www.pnnl.gov/main/publications/external/technical_reports/PNNL-30066.pdf
[18] https://www.sciencedirect.com/science/article/abs/pii/S0005109817306386
[19] https://www.sciencedirect.com/science/article/abs/pii/S0378779623007897
[20] https://www.sciencedirect.com/science/article/pii/S2352467721000060
[21] https://www.sciencedirect.com/science/article/pii/S2352484725008972
[22] https://www.sciencedirect.com/science/article/pii/S2590123024020425
[23] https://www.sciopen.com/article/10.62756/jmsi.1674-8042.2024053?issn=1674-8042
[24] https://www.stet-review.org/articles/stet/full_html/2024/01/stet20240116/stet20240116.html