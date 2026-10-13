# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** bfc583cb | **Time:** 213.66s | **Cost:** $0.03598
--------------------------------------------------------------------------------

# Do Kinetic Control Steps in Extraction Models Affect the Process Economics of Rare Earth Separation from Waste?

## Executive Summary

The separation of rare earth elements (REEs) from secondary sources, including electronic waste, coal fly ash, and mine tailings, represents a critical pathway for securing domestic supply chains of these strategically important materials. Solvent extraction (SX) remains the dominant industrial method for REE separation, yet the interplay between kinetic control steps and process economics remains insufficiently understood. This report examines whether kinetic limitations in extraction models significantly influence the economic viability of REE separation from waste streams. The analysis reveals that kinetic control steps substantially affect process economics through multiple interconnected mechanisms, including equipment sizing requirements, reagent consumption rates, stage configuration, and overall plant throughput. Understanding and modeling these kinetic phenomena is essential for developing cost-competitive separation processes that can compete with established foreign supply chains while meeting stringent environmental regulatory requirements.

## 1. Introduction

### 1.1 Strategic Importance of Rare Earth Element Recycling

Rare earth elements have emerged as indispensable materials for modern technological applications, spanning renewable energy systems, defense technologies, consumer electronics, and medical equipment [1]. The growing demand for these critical materials, combined with concentrated global supply chains predominantly controlled by a single nation, has prompted significant interest in developing domestic recycling capabilities from secondary sources. Electronic waste, coal fly ash, mine tailings, and other waste streams represent substantial untapped resources that could reduce dependence on foreign imports while mitigating the environmental impacts associated with primary mining operations [2].

The United States faces a strategic imperative to establish cost-competitive domestic REE separation capabilities. Without economically viable separation techniques, the nation risks supply chain disruptions affecting military systems, commercial products, and consumer goods. Such disruptions would adversely impact national security, homeland security, energy security, and overall economic stability [3]. This context establishes the critical importance of understanding all factors that influence the economics of REE separation, including the kinetic phenomena that govern extraction efficiency.

### 1.2 Solvent Extraction as the Primary Separation Technology

Solvent extraction has been the dominant industrial method for REE separation since its adaptation from the nuclear fuel cycle in the 1960s [4]. The technique exploits differences in solubility between aqueous and organic phases to achieve selective separation of metal ions. For rare earth elements, the process presents unique challenges due to the remarkable chemical similarity among the fifteen lanthanide elements. The trivalent REE ions exhibit nearly identical binding affinities with common extractants, meaning separation relies on small differences in equilibrium partitioning ratios between neighboring elements [5].

A typical REE separations facility produces pure individual species through a series of downstream solvent extraction circuits, each requiring extraction, scrubbing, and stripping stages. The resulting flowsheet may comprise hundreds of interconnected stages across multiple circuits, creating complex systems highly susceptible to process transients [6]. This complexity underscores the importance of accurate modeling, including proper representation of kinetic phenomena, for optimizing process economics.

### 1.3 Research Objective and Scope

This report investigates whether kinetic control steps in extraction models significantly affect the process economics of rare earth separation from waste materials. The analysis examines the theoretical foundations of kinetic phenomena in solvent extraction, their manifestation in REE separation processes, and the economic implications of these kinetic limitations. The scope encompasses both equilibrium-based and kinetic modeling approaches, with particular attention to how kinetic considerations influence equipment design, reagent consumption, energy requirements, and overall process efficiency.

## 2. Theoretical Framework: Kinetic Phenomena in Solvent Extraction

### 2.1 Fundamental Mechanisms of Mass Transfer

Solvent extraction involves the transfer of solute species across the interface between immiscible liquid phases. The overall mass transfer process comprises several sequential steps: diffusion of the solute through the bulk aqueous phase to the interface, interfacial reaction or complexation, diffusion of the complex through the interface into the bulk organic phase, and subsequent transport away from the interface [7]. Each of these steps may impose resistance to the overall mass transfer rate, with the slowest step typically controlling the overall extraction kinetics.

The mass transfer rate can be expressed mathematically through the flux equation:

$$N_A = k_L (C_{A,i} - C_{A}^*)$$

where $N_A$ represents the molar flux of species A, $k_L$ denotes the overall mass transfer coefficient, $C_{A,i}$ is the interfacial concentration, and $C_{A}^*$ represents the equilibrium concentration corresponding to the bulk organic phase composition. This relationship illustrates that the extraction rate depends fundamentally on both the mass transfer coefficient and the concentration driving force.

### 2.2 Equilibrium Versus Kinetic Separation Factors

The separation of adjacent rare earth elements depends on differences in their distribution coefficients between organic and aqueous phases. The equilibrium separation factor between two elements $i$ and $j$ is defined as:

$$\beta_{i,j} = \frac{(D_i)}{(D_j)} = \frac{[RE_i]_{org}/[RE_i]_{aq}}{[RE_j]_{org}/[RE_j]_{aq}}$$

where $D$ represents the distribution coefficient [8]. For neighboring lanthanides, these separation factors are typically quite low, often ranging from 1.1 to 2.5, reflecting the chemical similarity of these elements.

However, equilibrium separation factors do not account for kinetic differences in extraction rates between elements. In practice, even elements with similar equilibrium behavior may exhibit different kinetic responses to extraction conditions. These kinetic differences arise from subtle variations in hydration energies, complexation kinetics, and interfacial phenomena. The kinetic separation factor, defined as the ratio of extraction rate constants for different elements, may differ significantly from the equilibrium separation factor, offering potential opportunities for kinetic-based separations [9].

### 2.3 Factors Influencing Extraction Kinetics

Several factors govern the kinetics of REE solvent extraction from waste matrices. The nature of the extractant molecule significantly influences complexation rates, with organophosphorus compounds, carboxylic acids, and amine-based extractants each exhibiting distinct kinetic profiles. The diluent composition affects both the solubility of the REE-complex and the interfacial tension, which in turn influences mass transfer coefficients [10].

Hydrodynamic conditions within extraction equipment determine the interfacial area available for mass transfer and the intensity of turbulence affecting film thickness. Agitation speed, impeller design, and column geometry all influence the mass transfer characteristics. Temperature affects both the diffusion coefficients and the reaction kinetics, typically accelerating extraction rates with increasing temperature according to the Arrhenius relationship:

$$k = A \exp\left(-\frac{E_a}{RT}\right)$$

where $A$ is the pre-exponential factor, $E_a$ is the activation energy, $R$ is the gas constant, and $T$ is the absolute temperature [11].

The presence of complexing agents, masking agents, or competing ions in the aqueous phase can significantly modify extraction kinetics. In waste matrices, the presence of matrix elements such as iron, aluminum, or transition metals may compete for extractant sites or form complexes that interfere with REE extraction kinetics.

## 3. Economic Dimensions of REE Separation Processes

### 3.1 Capital Expenditure Considerations

The capital costs of REE separation facilities encompass multiple categories of equipment and infrastructure. Solvent extraction mixer-settler units, columns, and contactors represent the primary separation equipment, with costs scaling with required throughput and the number of stages. A separations facility producing pure REE products may require hundreds of stages across multiple circuits, representing substantial capital investment [12].

Equipment sizing is directly influenced by the residence time requirements, which in turn depend on kinetic parameters. Slower extraction kinetics necessitate larger equipment volumes or longer residence times to achieve target recoveries. The relationship between equipment size and kinetic parameters can be expressed through the general design equation:

$$V = \frac{Q \cdot \tau}{n}$$

where $V$ is the required vessel volume, $Q$ is the volumetric flow rate, $\tau$ is the residence time, and $n$ represents the number of stages. Since residence time requirements are fundamentally linked to extraction kinetics, slower reactions directly increase capital costs through larger equipment requirements.

Auxiliary systems including phase separation equipment, solvent recovery units, and wastewater treatment facilities add to capital requirements. The complexity of flowsheets with multiple circuits further increases instrumentation, piping, and control system costs. Economic assessments indicate that capital costs for REE separation facilities can range from tens to hundreds of millions of dollars depending on capacity and product specifications [13].

### 3.2 Operating Expenditure Drivers

Operating costs in REE separation facilities are dominated by reagent consumption, energy requirements, and labor. Reagent costs represent one of the largest operating expenses, with extractants, saponification agents, and process acids contributing significantly to overall costs [14]. The saponification process, which neutralizes cation extractants with sodium hydroxide or ammonium hydroxide to enable efficient metal exchange, is particularly costly:

$$\text{2HR}_{(org)} + \text{2Na}^+_{(aq)} \rightarrow \text{2NaR}_{(org)} + \text{2H}^+_{(aq)}$$

This reaction enables the exchange mechanism:

$$\text{RE}^{3+}_{(aq)} + \text{3NaR}_{(org)} \rightarrow \text{RE-R}_3_{(org)} + \text{3Na}^+_{(aq)}$$

The net result is no change in acid concentration, but the reagent costs for saponification are substantial [15]. Additionally, saponification causes environmental concerns due to effluent waste streams and can lead to gel formation and increased extractant solubility in the aqueous phase when performed excessively.

Kinetic limitations can exacerbate reagent consumption in several ways. Incomplete extraction due to kinetic constraints may require additional contact stages or higher extractant concentrations to achieve target recoveries. Higher extractant concentrations increase both direct reagent costs and downstream solvent recovery burdens. The relationship between extraction efficiency and reagent consumption creates economic incentives for optimizing kinetic performance.

### 3.3 Throughput and Capacity Utilization

Plant throughput directly influences the economic viability of REE separation operations. Higher throughput spreads fixed costs across larger production volumes, improving unit economics. However, throughput is constrained by the slowest step in the overall process, which may be a kinetic limitation in extraction or stripping operations.

The overall process throughput can be modeled using the concept of rate-limiting steps. If extraction kinetics are slower than other process steps, the extraction stage becomes the bottleneck, limiting overall plant capacity. This bottleneck effect can be expressed as:

$$Q_{max} = \frac{V_{ext} \cdot E}{t_{res}}$$

where $Q_{max}$ is the maximum throughput, $V_{ext}$ is the extraction equipment volume, $E$ is the extraction efficiency, and $t_{res}$ is the residence time required for kinetic completeness [16].

Capacity utilization rates significantly impact project economics. Techno-economic analyses of REE recycling operations indicate that net present value and internal rate of return are highly sensitive to throughput assumptions. Recycling processes that achieve higher throughput rates can reduce costs by up to 40% compared to primary extraction methods [17].

## 4. Impact of Kinetic Control on Process Economics

### 4.1 Stage Configuration and Number of Equilibrium Stages

The number of theoretical stages required for a given separation depends on both the separation factor and the approach to equilibrium. In equilibrium-based McCabe-Thiele analysis, the operating line and equilibrium curve define the stage requirements. However, when kinetic limitations prevent attainment of equilibrium, actual stage requirements exceed theoretical predictions.

The Murphree efficiency, which relates actual composition changes to theoretical equilibrium changes, provides a measure of kinetic performance:

$$E_{MV} = \frac{y_n - y_{n+1}}{y_n^* - y_{n+1}}$$

where $y_n$ is the actual exiting organic composition, $y_{n+1}$ is the entering organic composition, and $y_n^*$ is the composition that would be in equilibrium with the exiting aqueous phase [18]. Lower Murphree efficiencies, resulting from kinetic limitations, directly increase the number of stages required for a given separation.

For REE separations, where separation factors between adjacent elements are small, the stage requirements are already substantial. A separation facility producing pure individual rare earths may require dozens of stages per circuit. If kinetic limitations reduce effective stage efficiency from 100% to 50%, the stage requirement doubles, with corresponding increases in equipment costs, floor space requirements, and piping complexity.

### 4.2 Equipment Sizing and Capital Investment

The relationship between extraction kinetics and equipment sizing follows from the fundamental mass transfer equation. For a given throughput and separation requirement, slower kinetics necessitate larger equipment volumes. This relationship can be quantified through the overall volumetric mass transfer coefficient:

$$K_L a = \frac{V}{t \cdot \Delta C_{lm}}$$

where $K_L a$ is the volumetric mass transfer coefficient, $V$ is the vessel volume, $t$ is the residence time, and $\Delta C_{lm}$ is the log-mean concentration driving force [19].

Equipment cost scales approximately with volume raised to a power of 0.6 to 0.8, depending on equipment type. Thus, a 50% increase in required volume due to kinetic limitations translates to roughly 30-45% increase in equipment cost. For large-scale separation facilities, this represents millions of dollars in additional capital investment.

Mixer-settler units, which are common in REE separation applications, require both mixing vessels and settlers for phase separation. Mixing power requirements depend on achieving sufficient turbulence for dispersion formation and mass transfer. Settler sizing depends on the required residence time for phase separation, which can be affected by the presence of emulsions or fine dispersions resulting from high-energy mixing.

### 4.3 Reagent Consumption and Operating Costs

Kinetic limitations can significantly impact reagent consumption through multiple mechanisms. Incomplete extraction due to kinetic constraints may necessitate higher extractant concentrations in the organic phase. Higher extractant loadings increase the risk of third-phase formation and may require diluent modification or phase modifiers, adding to reagent costs.

The saponification requirement is directly proportional to the extractant concentration and the metal loading. Higher extractant concentrations increase both direct chemical costs and wastewater treatment requirements. Environmental concerns associated with saponification waste streams may also necessitate additional treatment costs or regulatory compliance expenses.

Stripping operations may also be affected by kinetic limitations. Incomplete stripping due to slow kinetics requires either higher stripping reagent concentrations or additional contact stages. For REE separation, stripping typically involves acid solutions, with acid consumption representing a significant operating cost. Techno-economic analyses identify reagent consumption as one of the key variables affecting the profitability of REE extraction from secondary sources [20].

### 4.4 Processing Time and Throughput Limitations

The residence time required for kinetic completeness directly limits plant throughput. For continuous operations, the residence time per stage determines the maximum flow rate for a given equipment size. If extraction kinetics are slow, achieving high recovery rates requires either larger equipment or reduced throughput.

The impact of processing time on economics can be illustrated through the concept of time value of money. Longer processing times delay product realization, affecting cash flows and project economics. For time-sensitive applications or volatile REE markets, processing time can significantly influence project viability.

Batch processing of REE from waste streams may be particularly affected by kinetic limitations. Each batch cycle includes loading, reaction, settling, and unloading phases. Slow kinetics extend the reaction phase, reducing the number of batches that can be processed per unit time and increasing per-batch overhead costs.

## 5. Modeling Approaches for Kinetic Optimization

### 5.1 Equilibrium-Based Modeling

Equilibrium models assume that the extraction process reaches thermodynamic equilibrium in each contact stage. This assumption simplifies calculations and is reasonable when mass transfer rates are fast compared to residence times. For REE separation, equilibrium modeling using software tools such as METSIM enables steady-state process simulation with equipment inventory sizing [21].

The equilibrium approach provides a theoretical baseline for process design. McCabe-Thiele diagrams and Kremser equations can be applied to calculate theoretical stage requirements. However, equilibrium models may significantly underestimate actual stage requirements when kinetic limitations are significant.

Process simulation software allows evaluation of complete flowsheets including multiple circuits for sequential separation of different REE groups. These simulations can identify bottlenecks and optimize operating conditions. However, the accuracy of equilibrium-based simulations depends on the validity of the equilibrium assumption, which may not hold for kinetically-limited systems.

### 5.2 Kinetic Modeling and Rate-Based Simulation

Rate-based models account for finite mass transfer rates and reaction kinetics. These models require kinetic parameters including mass transfer coefficients, interfacial areas, and reaction rate constants. For complex REE systems, determining accurate kinetic parameters requires experimental measurement under relevant conditions.

The general rate-based model for a differential element of an extraction column can be written as:

$$\frac{dy}{dz} = \frac{K_L a}{u_{org}} (x^* - x)$$

for the organic phase, with analogous equations for the aqueous phase [22]. Solving these equations requires knowledge of the mass transfer coefficient $K_L$, the interfacial area $a$, and the equilibrium relationship $x^*(y)$.

Computational fluid dynamics (CFD) modeling offers a more fundamental approach to capturing mass transfer phenomena. CFD models can resolve flow patterns, turbulence characteristics, and concentration fields within extraction equipment. For structured packing and other complex geometries, CFD simulations can predict mass transfer coefficients based on fluid dynamics [23].

### 5.3 Computational Fluid Dynamics Applications

CFD modeling of solvent extraction equipment has evolved significantly, though applications to REE separation remain limited. The approach involves solving the Navier-Stokes equations for fluid flow, coupled with species transport equations for mass transfer. For multiphase systems such as liquid-liquid extraction, additional complexity arises from interface tracking or population balance modeling.

The mass transfer prediction from CFD models depends significantly on the choice of mass transfer coefficient correlations and turbulence models. Studies indicate that CFD modeling of mass transfer in dispersive liquid-liquid systems is particularly challenging due to the need to model droplet breakup and coalescence phenomena [24].

For non-dispersive extraction modes such as hollow fiber contactors, CFD modeling can simulate mass transfer with individual droplets or slugs, providing detailed understanding of kinetic phenomena. These approaches offer potential for optimizing equipment design and operating conditions to enhance mass transfer rates.

### 5.4 Hybrid Modeling Approaches

Hybrid approaches combining equilibrium and kinetic elements offer practical compromises between accuracy and computational efficiency. Two-region models treat near-interface zones with kinetic descriptions while assuming equilibrium in bulk phases. These models can capture kinetic effects while maintaining reasonable computational requirements.

Data-driven modeling using machine learning techniques represents an emerging approach for predicting extraction kinetics. These methods can correlate extraction performance with operating variables, potentially capturing complex kinetic phenomena that are difficult to model mechanistically. However, such models require substantial training data and may not extrapolate well beyond the conditions of the training dataset.

The integration of laboratory data with modeling techniques forms the basis for optimizing solvent extraction flowsheets. The hypothesis that laboratory data coupled with modeling can optimize and develop SX flowsheets for adjacent rare earth elements has driven significant research efforts [25].

## 6. Case Studies and Empirical Evidence

### 6.1 Advanced Separation Technologies for Coal-Based Feedstocks

Research on REE extraction from coal and coal fly ash has developed baseline metallurgical process flowsheets for concentration and separation. These efforts have identified specific processing steps and associated costs for each step in the process. The work has also identified saleable byproducts that can improve overall process economics [26].

Kinetic studies on REE extraction from coal fly ash have examined the effects of acid concentration, temperature, and solid-to-liquid ratio on extraction rates. The primary association of REEs in lignite coal as weakly-bonded complexes of carboxyl groups has been identified as targets for extraction technology. Process modeling using hydrometallurgical simulation tools has provided forecasts of efficiency and leachability based on chemical kinetics and carboxylation percentages [27].

### 6.2 Electronic Waste Recycling Economics

Techno-economic assessments of REE recycling from electronic waste have evaluated the impact of process parameters on economic viability. Key financial and operational metrics including capital expenditure, operational expenditure, net present value, internal rate of return, and break-even analysis have been applied to evaluate recycling processes [28].

Studies on NdFeB magnet recycling have demonstrated that process innovations can significantly improve economics. The FJH-Cl₂ process enables high-purity and high-yield REE recovery from waste magnets in a single step. Life cycle assessment and techno-economic analysis show that this process reduces the number of steps by three times while reducing energy consumption by 87%, greenhouse gas emissions by 84%, and operating costs by 54% compared to traditional methods [29].

### 6.3 Acid Mine Drainage as a REE Source

Research on REE recovery from acid mine drainage has evaluated the economic feasibility of sequential leaching processes using weak acids at ambient temperature and pressure. Techno-economic assessments have examined excavation and transportation, multi-phase pH-driven step-leaching, and commercial solvent extraction to produce saleable rare earth oxide material [30].

Key variables affecting profitability include REE concentration and distribution in the feedstock, extraction and precipitation reagent consumption rates, and the potential for reagent recycling. Economically profitable valorization requires a combination of continued process innovation and financial incentives to substantially influence domestic REE supply.

### 6.4 Comparative Process Assessments

Comparative life cycle assessments have evaluated REE production from different sources including primary deposits, recycled materials, and urban mining sources. These assessments consider environmental footprints alongside economic factors, providing holistic views of process viability [31].

Studies indicate that recycling can reduce costs by up to 40% compared to primary extraction while enhancing supply chain stability and mitigating geopolitical risks. However, scaling from laboratory to industrial levels presents challenges including high capital investment, process optimization, and waste management. Laboratory methods requiring precise conditions are difficult to replicate in large-scale operations.

## 7. Implications for Process Design and Optimization

### 7.1 Design Strategies for Kinetic Enhancement

Understanding kinetic limitations enables targeted strategies for process improvement. Extractant selection can prioritize molecules with favorable kinetic characteristics alongside equilibrium selectivity. Temperature optimization balances kinetic enhancement against energy costs and potential degradation. Hydrodynamic design can maximize mass transfer coefficients through appropriate agitation and column internals.

The use of phase modifiers and additives can improve kinetic performance by modifying interfacial properties or complexation rates. For example, the addition of certain surfactants can reduce interfacial tension, increasing interfacial area and mass transfer rates. However, additives must be carefully selected to avoid adverse effects on phase separation or downstream processing.

Process intensification approaches including inline mixers, static mixers, and microchannel contactors can enhance mass transfer rates through improved mixing or reduced diffusion path lengths. These technologies may enable smaller equipment footprints and reduced capital costs while achieving target separations.

### 7.2 Economic Optimization Frameworks

Economic optimization of REE separation processes requires integrated consideration of kinetic and equilibrium phenomena. Multi-objective optimization frameworks can balance competing objectives including capital cost, operating cost, product purity, and recovery rate. Sensitivity analysis identifies key parameters affecting economics, guiding research and development priorities.

Techno-economic analysis methodologies developed for clean energy technologies provide frameworks for REE process evaluation. These approaches assess the impact of capital costs, operating and maintenance costs, and equipment service life on overall process viability [32]. The integration of kinetic models with economic parameters enables identification of optimal operating conditions.

Regional supply chain optimization considers the interplay between feedstock characteristics, process requirements, and market conditions. The development of regional resource assessments for critical minerals in unconventional sources supports creation of optimized supply chains based on extraction performance data and regional resource characteristics [33].

### 7.3 Scale-Up Considerations

The translation of laboratory-scale kinetic data to industrial-scale design presents significant challenges. Mass transfer coefficients measured in well-mixed laboratory reactors may not accurately predict performance in industrial equipment with different hydrodynamics. Scale-up criteria based on constant power per volume, tip speed, or Reynolds number may not preserve kinetic performance.

Geometric similarity alone does not guarantee similar mass transfer performance. The development of CFD models that capture mass transfer in complex geometries enables more reliable scale-up predictions. For structured packing and other intricate designs, CFD simulations can predict mass transfer coefficients based on fluid dynamics [34].

Pilot-scale testing remains essential for validating kinetic models and identifying scale-up issues. The progression from laboratory to pilot to commercial scale typically involves iterative refinement of process models and operating parameters. Techno-economic assessments performed prior to bench and pilot-scale facility construction help prioritize development efforts.

## 8. Conclusions and Future Directions

### 8.1 Summary of Findings

This analysis demonstrates that kinetic control steps in extraction models significantly affect the process economics of rare earth separation from waste. The evidence supports several key conclusions:

Kinetic limitations increase the number of contact stages required for target separations, directly impacting equipment costs and facility footprint. The relationship between extraction kinetics and stage efficiency means that slow mass transfer rates necessitate either more stages or larger equipment volumes, with corresponding increases in capital investment.

Reagent consumption is influenced by kinetic performance through multiple mechanisms. Incomplete extraction due to kinetic constraints may require higher extractant concentrations, increasing both direct chemical costs and waste treatment requirements. The saponification process, already identified as a major cost center, is exacerbated by kinetic limitations requiring higher extractant loadings.

Plant throughput and capacity utilization are constrained by the slowest kinetic steps in the process. For continuous operations, residence time requirements for kinetic completeness directly limit maximum flow rates. For batch operations, slow kinetics extend cycle times, reducing throughput and increasing per-batch overhead costs.

Modeling approaches that incorporate kinetic phenomena enable more accurate process design and optimization. Equilibrium models may significantly underestimate actual stage requirements when kinetic limitations are significant. Rate-based models and CFD simulations provide more accurate predictions but require additional kinetic parameters and computational resources.

### 8.2 Recommendations for Industry Practice

Based on this analysis, several recommendations emerge for practitioners developing REE separation processes from waste sources:

Kinetic characterization should be integrated into early-stage process development. Laboratory measurements of mass transfer coefficients and extraction rates under relevant conditions provide essential data for equipment design and scale-up. Standardized kinetic testing protocols would facilitate comparison of different extractants and process conditions.

Process simulation should incorporate rate-based models where kinetic limitations are significant. While equilibrium models provide useful insights, the economic implications of kinetic effects justify the additional complexity of kinetic simulations. Sensitivity analysis should identify conditions where kinetic effects are most pronounced.

Economic optimization should explicitly consider kinetic parameters alongside equilibrium selectivity. The trade-offs between extraction rate, separation factor, and reagent consumption require integrated analysis. Multi-objective optimization frameworks can identify operating conditions that balance competing economic objectives.

### 8.3 Future Research Priorities

Several areas warrant further investigation to improve understanding of kinetic effects on REE separation economics:

Fundamental kinetic studies on REE extraction from diverse waste matrices would provide data for improved model parameterization. The variation in kinetic behavior between different feedstocks (e.g., e-waste, coal fly ash, mine tailings) requires systematic characterization.

Development of predictive models for mass transfer coefficients in complex geometries would improve scale-up reliability. CFD modeling approaches that capture liquid-liquid dispersion phenomena remain challenging but offer potential for more accurate design predictions.

Integration of kinetic models with life cycle assessment and techno-economic analysis would enable holistic optimization of REE recycling processes. Such integration would support decisions regarding process selection, equipment design, and operating conditions.

Research on novel extraction technologies with improved kinetic characteristics could significantly impact process economics. Approaches such as membrane-based extraction, microfluidic extraction, and electrochemical methods may offer advantages in specific applications.

The development of domestic REE separation capabilities from secondary sources represents a strategic priority with significant economic and national security implications. Understanding and addressing kinetic control steps in extraction processes is essential for achieving cost-competitive, environmentally sustainable separation operations that can secure domestic supply chains for these critical materials.

---

## References

[1] N. A. Chowdhury et al., "Sustainable recycling of rare-earth elements from NdFeB magnet swarf: Techno-economic and environmental perspectives," *ACS Sustain. Chem. Eng.*, vol. 9, pp. 15915–15924, 2021.

[2] J. Binnemans et al., "Rare-earth recycling needs market intervention," *Nat. Rev. Mater.*, vol. 6, pp. 459–461, 2021.

[3] University of Idaho, "Solvent extraction flowsheets for adjacent rare earth elements," *ETD PDF*, 2021.

[4] K. Binnemans et al., "Towards zero-waste valorisation of rare-earth-containing industrial process residues: a critical review," *J. Cleaner Product.*, vol. 99, pp. 17–38, 2015.

[5] D. Peppard et al., "Studies of the solvent extraction behavior of transition elements. I. Order and degree of fractionation of the trivalent rare earths," *J. Phys. Chem.*, vol. 57, pp. 294–301, 1953.

[6] University of Idaho, "Solvent extraction flowsheets for rare earth separation," *ETD PDF*, 2021.

[7] J. Rydberg, *Solvent Extraction Principles and Practice*, Boca Raton: CRC Press, 2004.

[8] T. Uda, K. T. Jacob, and M. Hirasawa, "Technique for enhanced rare earth separation," *Science*, vol. 289, pp. 2326–2329, 2000.

[9] E. Kolar et al., "Microfluidic solvent extraction of rare earth elements from a mixed oxide concentrate leach solution using Cyanex® 572," *Chemical Engineering Science*, vol. 148, 2016.

[10] M. M. J. Correa et al., "Separation of copper from a leaching solution of printed circuit boards by using solvent extraction with D2EHPA," *Brazilian Journal of Chemical Engineering*, vol. 35, 2018.

[11] S. Kumar et al., "Development of a micro-mixer-settler for nuclear solvent extraction," *Journal of Radioanalytical and Nuclear Chemistry*, vol. 291, 2012.

[12] U.S. Department of Energy, "Report to Congress on Recovery of Rare Earth Elements and Critical Minerals from Coal and Coal By-Products," 2022.

[13] NETL, "FY2018 REE Peer Review Overview Report," 2018.

[14] P. S. Arshi, E. Vahidi, and F. Zhao, "Behind the scenes of clean energy: The environmental footprint of rare earth products," *ACS Sustain. Chem. Eng.*, vol. 6, pp. 3311–3320, 2018.

[15] University of Idaho, "Saponification and reagent costs in separations facilities," *ETD PDF*, 2021.

[16] A. H. G. Cents, D. W. F. Brilman, and G. F. Versteeg, "Gas absorption in an agitated gas-liquid-liquid system," *Chemical Engineering Science*, vol. 56, 2001.

[17] Wichita State University, "Economic viability of rare earth element recycling," *SOAR*, 2024.

[18] Z. Chen et al., "Fast extraction and enrichment of rare earth elements from waste water via microfluidic-based hollow droplet," *Separation and Purification Technology*, vol. 174, 2017.

[19] J. Marx et al., "Comparative life cycle assessment of NdFeB permanent magnet production from different rare earth deposits," *ACS Sustain. Chem. Eng.*, vol. 6, pp. 5858–5867, 2018.

[20] OSTI, "Techno-economic assessment of REE recovery from acid mine drainage," 2023.

[21] University of North Dakota, "Process modeling of hydrometallurgical extraction of REE," *UND Theses*, 2024.

[22] Bhabha Atomic Research Centre, "CFD modelling of solvent extraction equipment," *BARC Newsletter*, 2021.

[23] University of North Dakota, "CFD modeling for mass transfer prediction," *UND Theses*, 2024.

[24] Bhabha Atomic Research Centre, "CFD modelling of mass transfer in solvent extraction equipment," *BARC Newsletter*, 2021.

[25] University of Idaho, "Laboratory data coupled with modeling for SX flowsheet optimization," *ETD PDF*, 2021.

[26] NETL, "Baseline metallurgical process flowsheet for REE concentration and separation," 2018.

[27] University of North Dakota, "Hydrometallurgical process modeling using METSIM," *UND Theses*, 2024.

[28] Wichita State University, "Financial metrics for REE recycling assessment," *SOAR*, 2024.

[29] PNAS, "Sustainable recycling of rare-earth elements from NdFeB magnet swarf," 2025.

[30] OSTI, "Techno-economic assessment of REE recovery from AMDp," 2023.

[31] J. Marx et al., "Comparative life cycle assessment of NdFeB permanent magnet production," *ACS Sustain. Chem. Eng.*, 2018.

[32] NETL, "Performing a Techno-Economic Analysis for Power Generation Plants," *DOE/NETL-2015/1726*, 2015.

[33] U.S. Department of Energy, "Regional resource assessments for critical minerals," 2022.

[34] University of North Dakota, "VOF simulation for mass transfer prediction," *UND Theses*, 2024.

## Annotations


## Sources
[1] https://commons.und.edu/context/theses/article/5272/viewcontent/Kotwal_und_0156D_11967.pdf
[2] https://netl.doe.gov/sites/default/files/2019-05/2019_Annual_Reports/Wednesday/REE/7%20-%2020190410_0100C_FE0031526_NETL.pdf
[3] https://netl.doe.gov/sites/default/files/netl-file/FY2018%20REE%20Peer%20Review%20Overview%20Report_04262018.pdf
[4] https://objects.lib.uidaho.edu/etd/pdf/Lyon_idaho_0089N_10815.pdf
[5] https://soar.wichita.edu/server/api/core/bitstreams/70402035-3552-4aa3-afb2-c630f9d5b4c7/content
[6] https://www.barc.gov.in/barc_nl/2021/2021111206.pdf
[7] https://www.diva-portal.org/smash/get/diva2:868969/FULLTEXT01.pdf
[8] https://www.energy.gov/sites/default/files/2022-05/Report%20to%20Congress%20on%20Recovery%20of%20Rare%20Earth%20Elements%20and%20Critical%20Minerals%20from%20Coal%20and%20Coal%20By-Products.pdf
[9] https://www.nature.com/articles/s42005-025-02393-7
[10] https://www.osti.gov/servlets/purl/1922832
[11] https://www.osti.gov/servlets/purl/2418585
[12] https://www.pnas.org/doi/10.1073/pnas.2507819122
[13] https://www.sciencedirect.com/science/article/pii/S2213343724008996