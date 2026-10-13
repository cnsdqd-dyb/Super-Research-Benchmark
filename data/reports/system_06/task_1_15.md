# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 6f345a4b | **Time:** 356.52s | **Cost:** $0.12448
--------------------------------------------------------------------------------

# Aerodynamic Principles for Balancing Performance Parameters in Aero-Engine Compressor Design

## Abstract

The design of aero-engine compressors represents one of the most challenging multidisciplinary optimization problems in modern propulsion engineering. This report examines the aerodynamic principles that enable engineers to balance competing performance objectives: thrust-to-weight ratio, fuel efficiency, pressure ratio, and stall margins. Through analysis of contemporary research and development practices, this report identifies key design strategies including three-dimensional blade optimization techniques, variable geometry systems, and advanced control methodologies that collectively enable the achievement of optimal compressor performance across diverse operating conditions.

## 1. Introduction

The compressor subsystem of an aero-engine fundamentally determines the engine's overall performance characteristics, serving as the primary mechanism for increasing air pressure prior to combustion. The aerodynamic design of compressor components directly influences four critical performance parameters that often exist in tension with one another: thrust-to-weight ratio, fuel efficiency, pressure ratio capability, and stall margin [1][2]. Achieving an optimal balance among these parameters requires sophisticated application of aerodynamic principles combined with advanced optimization methodologies.

Modern aviation propulsion demands engines capable of operating efficiently across a wide range of flight conditions, from subsonic cruise to supersonic dash performance. This requirement has driven the development of Variable Cycle Engines (VCEs) that employ adaptive components to enable real-time optimization of engine parameters [6]. The fundamental challenge lies in the inherent trade-offs between these performance parameters, where improvements in one area often come at the expense of another. For instance, increasing pressure ratio typically enhances thermal efficiency and thrust output but simultaneously reduces the compressor's stable operating range, potentially compromising stall margins [9].

This report synthesizes current understanding of the aerodynamic principles and design methodologies that enable engineers to navigate these complex trade-offs. The analysis encompasses blade geometry optimization, variable geometry systems, computational optimization techniques, and control strategies that collectively provide the framework for achieving balanced compressor performance.

## 2. Fundamental Trade-offs in Compressor Design

### 2.1 The Competing Performance Objectives

Compressor aerodynamic design inherently involves compromises among pressure rise, flow capacity, efficiency, and stall margin [11]. The relationship between these parameters creates a multidimensional design space where optimization must carefully balance competing requirements. Higher pressure ratios contribute directly to improved thermal efficiency and specific thrust, enabling greater power density within a given engine envelope. However, the attainment of gains in pressure ratio is complicated by the concurrent requirements for high efficiency and wide operability [9].

As aerodynamic loading increases, losses tend to escalate, and the potential for flow breakdown and aerodynamic instability becomes substantially greater. For transonic compressor applications, rotor tip relative Mach numbers can vary from subsonic to highly supersonic values exceeding 1.6, conditions that can result in severe shock-related viscous losses [9]. This phenomenon illustrates the fundamental tension between追求 maximum pressure ratio capability and maintaining acceptable efficiency levels across the operating envelope.

The thrust-to-weight ratio consideration adds another dimension to this optimization challenge. Higher pressure ratios typically require additional compressor stages or more complex blade geometries, potentially increasing engine weight and complexity. Conversely, reducing stage count to minimize weight may compromise pressure ratio capability or require higher loading per stage, which can negatively impact efficiency and stall margin [3]. The design team must therefore navigate these interdependencies through careful selection of design variables and optimization constraints.

### 2.2 Stall Margin Considerations

Compressor stall represents a critical operational constraint that fundamentally limits the usable operating range of the engine. A compressor stall occurs when there is an imbalance between air flow supply and airflow demand, resulting in a pressure ratio incompatible with the engine RPM [12]. When this condition develops, smooth airflow is interrupted, creating turbulence and pressure fluctuations within the turbine section. These disturbances can cause the air flowing through the compressor to slow down or stagnate, sometimes resulting in reverse flow that can cause severe engine damage.

The stall margin—the difference between the operating line and the stall line—represents a key design parameter that must be carefully managed. Optimized levels of efficiency, flow, and pressure rise may need to be sacrificed to achieve satisfactory levels of stall margin [11]. This trade-off is particularly critical during transient engine operations, such as acceleration and deceleration, when the compressor is most susceptible to stall conditions. The design of variable stator settings, for example, can improve efficiency while potentially reducing the conventional stall margin, requiring careful analysis of the sensitivity of stall line position to changes in operating parameters [11].

## 3. Three-Dimensional Blade Optimization Techniques

### 3.1 Blade Lean and Sweep Principles

Three-dimensional blade design modifications, particularly blade lean and sweep, represent powerful tools for improving compressor performance across multiple parameters simultaneously. These geometric modifications alter the spanwise distribution of blade loading, thereby influencing secondary flow patterns, shock wave structures, and tip leakage flows in ways that can enhance both efficiency and stall margin [1][8].

Blade lean refers to the tangential displacement of the blade stacking line along the blade span, creating a non-axial orientation of the blade sections. Positive lean (leaning toward the pressure surface at the tip) and negative lean (leaning toward the suction surface at the tip) produce distinctly different flow field modifications. Research has demonstrated that leaned and swept blades can achieve higher efficiency, total pressure ratio, and stall margin compared to baseline radial blade configurations [8]. The key flow mechanism underlying these improvements involves the redistribution of spanwise and chordwise loading, which alters the radial pressure gradients that drive secondary flows.

The optimization of blade lean and sweep distributions has been successfully demonstrated for the NASA Rotor-67 blade, where entropy production was reduced by more than 16% compared to the baseline design [8]. The optimized configuration featured a lambda-shaped shock wave on the suction side, demonstrating how three-dimensional blade modifications can beneficially alter the shock structure in transonic compressors. This shock modification reduces shock-boundary layer interaction losses while simultaneously improving the stability margin of the compressor.

### 3.2 Shock Wave Management

In transonic and supersonic compressor stages, shock wave management represents a critical aspect of aerodynamic design. The interaction between shock waves and boundary layers can trigger flow separation, increasing losses and potentially initiating stall. Three-dimensional blade sweep shifts the shock wave position relative to the blade surface, typically moving the shock downstream along the blade span [1]. This downstream migration reduces the adverse pressure gradient experienced by the boundary layer, delaying separation and extending the stable operating range.

The effects of sweep on axial compressor performance have been extensively studied using numerical simulation of the NASA Rotor-37 with grooved casing treatments [1]. These studies demonstrated that carefully designed sweep distributions can significantly improve stall margin by modifying the tip leakage flow structure and reducing the strength of shock-boundary layer interactions. The grooved casing treatment works synergistically with blade sweep to enhance tip region flow control, providing additional stability margin.

Research by Biollo and Benini revealed that newly designed three-dimensional swept and leaned rotors achieve higher efficiency through modification of the shock wave structure [8]. The three-dimensional nature of the shock modification creates a more gradual pressure rise across the blade passage, reducing the tendency for boundary layer separation while maintaining high pressure ratio capability. This represents a fundamental principle: three-dimensional blade design enables the decoupling of spanwise loading distributions, allowing optimization of performance at multiple spanwise locations simultaneously.

### 3.3 Flow Separation Control

Blade lean has been identified as an effective mechanism for controlling flow separation on blade surfaces and improving turbomachinery performance [1]. The redistribution of loading associated with blade lean alters the pressure gradient distribution along the blade surface, potentially reducing the extent of separated flow regions. Cao et al. demonstrated that positive lean can increase radial secondary flow on the suction surface compared to linear blades, while simultaneously reducing the cross-passage pressure gradient that drives secondary flows [1].

The mechanism by which lean controls flow separation involves modification of the three-dimensional flow structure within the blade passage. By tilting the blade sections, lean changes the effective angle of attack distribution along the span, which in turn affects the development of the boundary layer. At locations where the boundary layer is prone to separation under baseline conditions, the lean-induced modification of the pressure field can provide a more favorable pressure gradient distribution, promoting attached flow and reducing losses.

## 4. Variable Geometry Systems

### 4.1 Variable Stator and Compressor Geometry

Variable geometry features in compressors provide a mechanism for adapting the compressor characteristics to match varying operating conditions, thereby enabling optimization across a wider operating envelope. Variable geometry requires an actuating mechanism capable of withstanding the high temperatures and thermal stresses typical of the compressor section, while remaining compact and lightweight for aero-engine application [6]. The implementation of variable geometry represents a significant engineering challenge but provides substantial performance benefits.

Variable stator settings enable optimization of the incidence angle at the rotor inlet across different operating speeds and flow conditions [11]. At low rotor speeds, variable stators can be positioned to maintain optimal incidence, preserving efficiency that would otherwise be lost due to off-design incidence angles. However, applying sensitivity factors that degrade the stall line for changes in the stator schedule can result in a loss in stall margin of 4% to 5% [11]. This illustrates the careful balance required when implementing variable geometry systems—the benefits in efficiency must be weighed against potential reductions in operating range.

The design of variable geometry compressor systems requires consideration of both the steady-state and dynamic characteristics of the variable mechanism. During the preliminary design phase, redefining both the stator and blade velocity diagrams can produce larger gains in efficiency for a given loss in stall margin [11]. This suggests that the optimization of variable geometry should be integrated into the overall compressor design process rather than treated as a post-design modification.

### 4.2 Variable Cycle Engine Concepts

Variable Cycle Engines (VCEs) represent an advanced approach to addressing the fundamental trade-offs in compressor design by enabling real-time adaptation of engine cycle parameters [6]. By adjusting bypass ratios, turbine operations, and compressor settings, VCEs offer flexibility that reduces the need for performance compromises across the mission profile. This approach is particularly valuable for military aircraft that must operate efficiently at subsonic speeds while providing the thrust necessary for supersonic flight.

The variable compression system in VCEs addresses the fundamental limitation that fan pressure ratio at the design point determines specific thrust and specific fuel consumption for the entire flight range in traditional engines [6]. In engines with multiple bypass ducts, the fan is divided into front and rear sections, with variable area mixers and nozzles used to control the fan pressure ratio. This enables efficient subsonic flight with low pressure ratios and high-thrust supersonic flight with high pressure ratios, effectively decoupling the traditional trade-off between efficiency and performance.

The implementation of VCE concepts requires sophisticated integration of multiple variable geometry systems, including variable compressor geometry, variable turbine geometry, and variable nozzle systems. While variable turbines can significantly impact engine cycles and offer benefits in terms of work and shaft-speed regulation between spools, they are not prioritized in aviation applications due to their complexity and the challenges of implementing variable geometry in the high-temperature turbine environment [6]. The thermal and mechanical demands of the turbine section, where components are subjected to high temperatures and thermal expansion, make variable turbine implementation particularly challenging.

### 4.3 Supersonic Airflow Management

For engines operating at supersonic flight speeds, intake design becomes critical to compressor performance. Variable-geometry inlets with adjustable ramps or centerbodies decelerate supersonic airflow to subsonic velocities before compressor entry, minimizing total pressure loss through shock wave management [2]. Diverterless supersonic inlets (DSI) use carefully contoured bump surfaces to compress and redirect boundary layer flow, eliminating complex bleed systems while reducing radar cross-section.

The management of supersonic airflow through the intake directly affects the conditions presented to the compressor inlet. Total pressure recovery at the compressor face determines the maximum achievable pressure ratio and efficiency of the compressor stage. Shock wave management in the intake therefore has direct implications for overall engine performance, including thrust-specific fuel consumption and stall margin. The optimization of intake geometry must be coordinated with compressor design to ensure compatible operating conditions across the flight envelope.

## 5. Advanced Optimization Methodologies

### 5.1 Multi-Objective Optimization Approaches

Modern compressor design increasingly employs sophisticated optimization methodologies that can simultaneously address multiple performance objectives. Optimization methods have been recognized as practical tools for improving the performance of turbomachinery, enabling systematic exploration of the design space to identify configurations that balance competing requirements [1]. These approaches typically combine computational fluid dynamics simulations with optimization algorithms to explore the relationships between design variables and performance metrics.

Research has demonstrated the application of genetic algorithm and neural network coupling for compressor performance optimization at multiple design points, including conditions close to the stall and choke regimes [1]. This multi-point optimization approach recognizes that a compressor must perform well across its entire operating envelope, not just at a single design point. The coupling of genetic algorithms with neural network surrogates enables efficient exploration of the design space while maintaining accuracy in performance prediction.

The optimization of blade lean and sweep for the NASA Rotor-67 axial compressor exemplifies this approach, where three-dimensional numerical simulation results showed good agreement with experimental data [1]. The blade stacking line was then modified to improve performance, demonstrating how optimization methods can guide design improvements while maintaining fidelity through validation against experimental measurements. This integration of simulation, optimization, and experimental validation represents the current state-of-the-art in compressor design methodology.

### 5.2 Robust Design Considerations

The追求 of optimal compressor performance must be balanced against the need for robust designs that tolerate manufacturing variations and operating condition changes. Robust design approaches recognize that the best global optimum may not represent the optimal engineering solution if it is sensitive to small changes in shape or operating conditions [4]. Design searches that seek to balance absolute performance and robustness become particularly challenging when the response of the geometry to changes in design variables is abrupt.

The mathematics of shapes relevant to aerodynamic design has evolved to address these challenges, with new curve and surface models equipped with design variables that enable intuitive shape changes [4]. These parameterization approaches must provide sufficient flexibility to explore the design space while maintaining smoothness and predictability in the response. The selection of appropriate design variables and constraints significantly influences the effectiveness of the optimization process and the practical utility of the resulting designs.

A clear trade-off between system efficiency, mass-flow range, and robustness has been identified in compressor design optimization [10]. Higher nominal compressor mass-flows, corresponding to increased nominal power, can decrease the hypervolume of feasible manufacturing deviations. This finding suggests the existence of an optimal operating point that balances performance requirements against manufacturing tolerances and operational variability.

### 5.3 Collaborative and Multidisciplinary Optimization

The design of aero-engine compressors inherently involves interactions between multiple engineering disciplines, including aerodynamics, structures, heat transfer, and controls. Multidisciplinary optimization frameworks have been developed to address these interactions, enabling concurrent optimization of design variables across disciplines [5][7]. These approaches recognize that optimal solutions often lie at the intersection of discipline-specific optima, requiring integrated analysis and optimization.

The cycle selection process for engine design begins with consideration of the engine design point, using past experience to establish a starting point for an iterative process [5]. Leading cycle parameters, flows, efficiencies, and temperatures are chosen, with corresponding geometry generated by component areas. Component geometry is allied to component performance, but overall layout and envelope considerations, together with component interactions, force compromises that must be navigated through iterative refinement.

The mechanical architecture of the engine is heavily influenced by mass considerations and life-cycle cost, with resultant decisions concerning compressor variable geometry, disc-blade fixing, bearing arrangements, parts count, and shaft rotation [5]. This illustrates how compressor design decisions propagate through the entire engine system, requiring consideration of factors beyond pure aerodynamic performance. The integration of these considerations into the optimization process ensures that resulting designs are not only aerodynamically optimal but also practical for manufacture, assembly, and maintenance throughout the engine lifecycle.

## 6. Control System Integration

### 6.1 Full Authority Digital Engine Control

Full Authority Digital Engine Control (FADEC) systems have revolutionized engine control by eliminating hydromechanical linkages and providing microsecond-level authority over fuel flow, variable geometry positioning, and afterburner staging [2]. Dual-channel redundant processors monitor hundreds of engine parameters continuously, executing closed-loop control laws that adapt to changing atmospheric conditions, aircraft maneuvering loads, and pilot throttle commands. This capability enables real-time optimization of compressor operating conditions within the constraints established by the mechanical design.

The integration of advanced control strategies with compressor design enables operation closer to performance limits while maintaining adequate margins for stability and durability. Real-time fuel flow, air ratio, and afterburner optimization provide the control authority necessary to manage the complex interactions between compressor, combustor, and turbine components [2]. The response time and adaptability enabled by FADEC systems directly impact combat effectiveness and safety in military applications.

### 6.2 Predictive and Adaptive Control

The evolution of artificial intelligence and machine learning technologies has enabled new approaches to engine control that can anticipate operating conditions and proactively adjust engine parameters. AI-based predictive tuning represents an emerging capability that can further enhance the balance between performance and operability [2]. By analyzing patterns in operating data and predicting upcoming conditions, these systems can pre-position variable geometry elements and adjust fuel schedules to optimize performance for anticipated mission phases.

The integration of predictive control with compressor design requires consideration of the control system during the initial design phase. Any engine model that exists at such an early stage in the design process is preliminary by definition and may contain assumptions and omissions in steady-state or dynamic modeling [5]. Variable geometry features are not always well understood in the early stages of design in terms of the relationship between geometry setting and thermodynamic effect. The development of accurate models that capture these relationships is essential for effective implementation of advanced control strategies.

## 7. Design Space Exploration and Trade-off Analysis

### 7.1 Parametric Design Studies

Systematic parametric studies provide essential insight into the relationships between design variables and performance metrics, enabling informed decision-making during the design process. A parametric study conducted to define an optimum axial-flow high-pressure ratio compressor for commercial subsonic transport service investigated compressors with 18:1 pressure ratio and 6 to 12 stages [3]. A matrix of 49 compressors was developed using statistical techniques, enabling systematic exploration of the design space.

The analysis of trade factors and partial derivatives enables evaluation of the sensitivity of performance metrics to changes in individual design parameters [3]. Trade factors established for each engine characteristic—including thrust-specific fuel consumption, weight, price, dimensions, and maintenance cost—provide quantitative measures of the interdependencies between design choices. These factors enable rapid assessment of the impact of proposed design changes on overall engine performance, supporting informed decision-making during the iterative design process.

### 7.2 Flow-Path Optimization

The selection of flow-path shape significantly influences compressor performance, with constant-diameter casing providing the best balance between high pressure ratio and good efficiency in many applications [9]. Because of the need to limit exit rim speed, the casing diameter is often reduced at the aft end of the compressor, with a discharge Mach number of approximately 0.35 assumed based on considerations of matching with downstream stages.

Stage efficiency is refined by balancing stage reaction, inlet swirl, solidity, aspect ratio, and axial velocity diffusion [9]. Orchestrating all these parameters results in an overall total-pressure ratio of 12:1 at a rotor corrected tip speed of 1477 ft/s, with average aspect ratios of 0.8 for rotors and 1.0 for stators. These design choices reflect the careful balancing of competing requirements that characterizes modern compressor design.

The anticipated aerodynamic technology advancements suggest potential for substantial expansion of the design space in the direction of higher work coefficients and stage total-pressure ratio [9]. Maximum dividends occur when both high loading and high tip speed are selected, but this combination requires careful attention to maintaining acceptable efficiency and operability. The evolutionary approach employs advancements in simulation techniques to refine traditional design concepts in pursuit of higher efficiencies at increased aerodynamic loading levels, while the revolutionary approach attempts to explore unconventional concepts for increased pressure ratio, higher efficiencies, and wider operability.

## 8. Conclusion

The aerodynamic design of aero-engine compressors requires sophisticated application of fundamental principles to balance the inherently competing objectives of thrust-to-weight ratio, fuel efficiency, pressure ratio, and stall margin. Three-dimensional blade optimization techniques, particularly blade lean and sweep, provide powerful mechanisms for simultaneously improving multiple performance parameters by beneficially modifying shock structures, controlling flow separation, and redistributing spanwise loading.

Variable geometry systems, including variable stators and variable cycle engine concepts, enable adaptation of compressor characteristics to changing operating conditions, extending the useful operating envelope and reducing the need for performance compromises at specific operating points. The integration of advanced control systems through FADEC and predictive control strategies provides the real-time optimization authority necessary to operate compressors close to their performance limits while maintaining adequate stability margins.

Modern optimization methodologies, including multi-objective optimization, robust design approaches, and multidisciplinary optimization frameworks, enable systematic exploration of the complex design space defined by compressor performance requirements. The coupling of computational fluid dynamics with genetic algorithms and neural networks provides efficient tools for identifying optimal configurations that balance competing objectives across the operating envelope.

The fundamental principle underlying successful compressor design is the recognition that performance parameters are interconnected through the underlying fluid dynamics, and improvements in one area can often enable or facilitate improvements in others. By understanding and exploiting these relationships through careful application of aerodynamic principles, engineers can achieve compressor designs that meet the demanding requirements of modern aviation propulsion systems.

## References

[1] Heidarian Shahri, M., Madadi, A., and Boroomand, M. (2023). "Three-Dimensional Optimization of Blade Lean and Sweep for an Axial Compressor to Improve the Engine Performance." *Journal of Applied Fluid Mechanics*, Vol. 16, No. 11, pp. 2206-2218.

[2] BQPSIM. (2024). "Military Jet Engine Optimization." Available at: https://www.bqpsim.com/articles/military-jet-engine-optimization

[3] NASA. (1976). "Parametric Study of Optimum Axial-Flow High-Pressure Ratio Compressors." NASA Technical Report, NASA Lewis Research Center.

[4] Sobester, A. "Aircraft Aerodynamic Design: Geometry and Optimization." Available at: https://www.rexresearch1.com/AeroEngineeringLibrary/AircraftAerodynamicDesignGeometryOptimization.pdf

[5] DTIC. (2002). "Advanced Life Cycle Optimization and Analysis Facility (ALOAF) for Turbine Engines." Available at: https://apps.dtic.mil/sti/pdfs/ADA403085.pdf

[6] DLR. (2023). "Variable Cycle Engines for Next-Generation Propulsion Technology." German Aerospace Center. Available at: https://elib.dlr.de/215466/1/DLR_published.pdf

[7] NASA. (2000). "Multidisciplinary Design Optimization System for a Supersonic Natural Laminar Flow Aircraft Concept." NASA Technical Report.

[8] JAFM. (2023). "Effects of Blade Lean on Transonic Compressor Performance." *Journal of Applied Fluid Mechanics*. Available at: https://www.jafmonline.net/article_1907_19e6402ce4a378593be8e0e431d19b83.pdf

[9] NASA. (2003). "Advanced Compressor Design Concepts for High Efficiency and Wide Operability." NASA Technical Report, NASA Glenn Research Center.

[10] Massoudi, S., Picard, C., and Schiffmann, J. (2024). "An Integrated Approach to Designing Robust Gas-Bearing Supported Turbocompressors Through Surrogate Modeling and Constrained All-At-Once Multi-Objective Optimization." *ASME Journal of Mechanical Design*, Vol. 146, No. 12.

[11] MIT. (2002). "Optimizing Compressor Component Performance." Available at: https://dspace.mit.edu/bitstream/handle/1721.1/36437/30822304-MIT.pdf

[12] Skybrary. (2024). "Compressor Stall." Available at: https://skybrary.aero/articles/compressor-stall

## Annotations


## Sources
[1] https://aiaa.org/wp-content/uploads/2024/12/1stplaceundergradenginedesign.pdf
[2] https://apps.dtic.mil/sti/pdfs/ADA403085.pdf
[3] https://asmedigitalcollection.asme.org/mechanicaldesign/article/146/12/121706/1201239/An-Integrated-Approach-to-Designing-Robust-Gas
[4] https://asmedigitalcollection.asme.org/turbomachinery/article/146/4/041004/1170171/Optimization-of-Three-Dimensional-Blade-and
[5] https://dspace.mit.edu/bitstream/handle/1721.1/36437/30822304-MIT.pdf?sequence=2
[6] https://elib.dlr.de/215466/1/DLR_published.pdf
[7] https://journal.gpps.global/Design-optimization-of-a-multi-stage-axial-compressor-using-throughflow-and-a-database,109834,0,2.html
[8] https://kth.diva-portal.org/smash/get/diva2:1903035/FULLTEXT01.pdf
[9] https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=910065TW.TXT
[10] https://ntrs.nasa.gov/api/citations/19760025103/downloads/19760025103.pdf
[11] https://ntrs.nasa.gov/api/citations/19770013161/downloads/19770013161.pdf
[12] https://ntrs.nasa.gov/api/citations/19790014913/downloads/19790014913.pdf
[13] https://ntrs.nasa.gov/api/citations/19890015744/downloads/19890015744.pdf
[14] https://ntrs.nasa.gov/api/citations/20000002998/downloads/20000002998.pdf
[15] https://ntrs.nasa.gov/api/citations/20030014624/downloads/20030014624.pdf
[16] https://ntrs.nasa.gov/api/citations/20050185247/downloads/20050185247.pdf
[17] https://papers.ssrn.com/sol3/Delivery.cfm/f9201502-801b-4cba-81c0-dae522d68034-MECA.pdf?abstractid=5350815&mirid=1
[18] https://skybrary.aero/articles/compressor-stall
[19] https://www.asme.org/topics-resources/content/turbine-fuel-efficiency-fitting-a-pitch
[20] https://www.bqpsim.com/articles/military-jet-engine-optimization
[21] https://www.jafmonline.net/article_1907_19e6402ce4a378593be8e0e431d19b83.pdf
[22] https://www.jafmonline.net/article_2297_16bb57a3ae59be3ae633b1acae658524.pdf
[23] https://www.linkedin.com/posts/nourbadad_variable-stator-vane-vsv-system-optimizing-activity-7397985958303854593-YRKA
[24] https://www.nal.res.in/themes/stark/cfdimgs/FullPaper/P18-Design%20and%20CFD%20Analysis%20of%20a%20Multi%20Stage%20Axial%20Flow%20Compressor.pdf
[25] https://www.rexresearch1.com/AeroEngineeringLibrary/AircraftAerodynamicDesignGeometryOptimization.pdf
[26] https://www.sciencedirect.com/science/article/abs/pii/S0360544216318825
[27] https://www.sciencedirect.com/science/article/abs/pii/S0376042112000528
[28] https://www.sciencedirect.com/science/article/pii/S2212540X15000656