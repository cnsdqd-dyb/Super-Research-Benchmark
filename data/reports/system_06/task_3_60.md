# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** db63c4e6 | **Time:** 283.52s | **Cost:** $0.03515
--------------------------------------------------------------------------------

# How Diffusion Resistance in Membrane Separation Affects CCS Energy Efficiency Curves

## Abstract

Membrane separation technology represents a promising pathway for carbon capture and storage (CCS) applications, offering a cost-effective alternative to conventional solvent-based capture methods. However, the energy efficiency of membrane-based CCS systems is fundamentally governed by the interplay between membrane transport properties and process operating conditions. This report examines how diffusion resistance—arising from the solution-diffusion mechanism governing gas transport through dense polymer membranes—influences the energy efficiency curves of CCS systems. Through analysis of membrane transport phenomena, process optimization studies, and techno-economic evaluations, this report elucidates the relationships between diffusion resistance, membrane area requirements, parasitic energy loads, and overall CCS performance. The findings indicate that diffusion resistance creates significant trade-offs between capital costs and operating expenses, manifesting as characteristic curves in energy efficiency analyses that must be carefully navigated during process design and membrane material selection.

## 1. Introduction

The imperative to mitigate anthropogenic carbon dioxide emissions has driven substantial research into carbon capture and storage technologies capable of integration with existing power generation infrastructure. Among the various capture approaches under development, membrane separation has emerged as a particularly promising technology due to its modular nature, potential for scalability, and absence of phase change or chemical regeneration requirements that characterize solvent-based systems [1]. The U.S. Department of Energy's advanced carbon dioxide capture research program has identified membrane technology as a key focus area, emphasizing the potential for more efficient membrane modules and process schemes to reduce pressure drop and increase driving force for CO₂ separation in harsh environments [1].

The fundamental appeal of membrane systems lies in their elegant separation principle, wherein differential permeation rates of gas species through a selective barrier enable compositional separation without the thermodynamic penalties associated with thermal regeneration cycles. However, realizing the full potential of membrane technology for post-combustion carbon capture requires careful consideration of the transport mechanisms governing species passage through the membrane matrix. The solution-diffusion model, which describes gas transport through dense polymeric membranes, identifies diffusion as a critical resistance term that directly influences both the required membrane area and the energy consumption of the separation process [2].

Understanding how diffusion resistance affects CCS energy efficiency curves is essential for several reasons. First, the energy penalty associated with carbon capture directly impacts the net power output of the host power plant, thereby affecting the economic viability of CCS deployment. Second, the relationship between membrane properties and energy consumption creates optimization challenges that must be addressed through systematic process design. Third, the trade-offs between membrane permeability, selectivity, and diffusion resistance have profound implications for the selection of appropriate membrane materials and process configurations. This report synthesizes current understanding of these relationships to provide a comprehensive analysis of how diffusion resistance influences the energy efficiency characteristics of membrane-based CCS systems.

## 2. Theoretical Framework: Solution-Diffusion Transport and Diffusion Resistance

### 2.1 Fundamentals of the Solution-Diffusion Model

Gas separation through dense polymeric membranes follows the solution-diffusion mechanism, wherein three sequential steps govern species transport: sorption at the feed-membrane interface, diffusion through the membrane matrix, and desorption at the permeate-membrane interface [2]. The permeate flux J of a gas species through the membrane can be expressed as:

$$J = \frac{P}{\ell} \Delta p = \frac{D \cdot S}{\ell} \Delta p$$

where P represents the permeability coefficient, D denotes the diffusion coefficient, S is the solubility coefficient, ℓ is the membrane thickness, and Δp is the partial pressure difference driving force across the membrane [2]. The permeability P itself represents the product of the diffusion coefficient D and the solubility coefficient S, reflecting the dual nature of gas transport through dense polymer membranes.

The diffusion coefficient D characterizes the mobility of gas molecules within the polymer matrix and is temperature-dependent according to an Arrhenius-type relationship:

$$D = D_0 \exp\left(-\frac{E_d}{RT}\right)$$

where D₀ is a pre-exponential factor, E_d is the activation energy for diffusion, R is the gas constant, and T is the absolute temperature [2]. This temperature dependence has significant implications for CCS applications, as the operating temperature of flue gas streams from coal-fired power plants can substantially influence diffusion rates and thereby affect membrane performance.

### 2.2 Diffusion Resistance as a Limiting Factor

The concept of diffusion resistance emerges from the transport framework as the inverse of the diffusion coefficient, scaled by membrane thickness. In practical terms, higher diffusion resistance requires either increased membrane area to achieve a target separation or higher driving forces (achieved through compression or vacuum) to maintain flux rates. The dimensionless groups developed for analyzing electrochemical CO₂ separation systems provide useful analogies for understanding diffusion resistance in membrane systems [3]. The parameter γ_mt, representing the ratio of the electrochemical reaction rate to the mass transport rate in the boundary layer, has a direct analog in membrane systems where the ratio of permeation rate to diffusion capacity determines concentration polarization effects and overall mass transfer resistance [3].

When diffusion resistance is significant relative to the overall mass transfer driving force, concentration gradients develop across the membrane thickness, and the effective flux falls below the theoretical maximum predicted by ideal solution-diffusion behavior. This phenomenon becomes particularly important in high-flux applications where the permeate side concentration may build up, creating back-diffusion effects that reduce the net driving force. Studies have shown that at low values of γ_mt (much less than unity), mass transport rates are high relative to the driving force, and species concentrations at the membrane surface remain similar to bulk values [3]. However, as γ_mt increases, the slowing of transport processes becomes significant, and diffusion resistance begins to dominate the overall mass transfer behavior.

### 2.3 Relationship to Membrane Permeance and Selectivity

The membrane CO₂ permeance, defined as the permeability divided by membrane thickness (P/ℓ), represents the practical figure of merit for membrane performance in CCS applications. Research has assumed membranes can be fabricated with effective thicknesses of 0.1 μm, enabling high permeance values that reduce the required membrane area for a given separation task [4]. However, the relationship between permeance and selectivity is governed by the well-known Robeson upper bound, which describes an inverse correlation between permeability (or permeance) and selectivity for polymer membranes [4].

This trade-off has profound implications for diffusion resistance. Materials with higher diffusion coefficients (lower diffusion resistance) typically exhibit reduced selectivity, while highly selective materials often possess lower diffusion coefficients that increase diffusion resistance. The Robeson plot for CO₂ and N₂ separation illustrates this relationship, showing that increasing CO₂ permeability generally leads to a concomitant decrease in CO₂/N₂ selectivity [4]. In the context of carbon capture applications, this trade-off reflects a fundamental compromise between total membrane area requirements (capital cost) and energy requirements (operating cost), both of which are influenced by diffusion resistance.

## 3. Impact of Diffusion Resistance on CCS Energy Efficiency

### 3.1 Energy Penalty Framework

The energy penalty associated with CCS represents the fraction of fuel input that must be dedicated to capture activities rather than useful power production. For membrane-based systems, this penalty arises primarily from the work required to create the pressure differential driving force across the membrane and to compress the permeate stream to conditions suitable for transport and storage. The energy penalty f₁ can be expressed as:

$$f_1 = \frac{E_S}{E_H}$$

where E_S represents the energy required for CCS activities and E_H is the total fuel energy input [5]. If the fuel quantity is fixed, the energy penalty manifests as a reduction in the plant's power output. The new power output per unit fuel becomes:

$$W_e = \eta_{pp}E_H(1 - f_1)$$

where η_pp represents the power plant efficiency [5].

Diffusion resistance affects the energy penalty through its influence on the required pressure ratio between feed and permeate streams. Higher diffusion resistance necessitates either increased membrane area or higher pressure differentials to achieve target separation performance. Studies have demonstrated that the capture cost decreases significantly as the inlet CO₂ molar fraction increases, a trend explained by the simultaneous reduction in both membrane area and energy demand [6]. For inlet CO₂ molar fractions ranging from 0.20 to 0.30, capture costs decreased from $73.13/t-CO₂ to $45.69/t-CO₂, while energy demand dropped from 284.5 kWh/t-CO₂ to 182.8 kWh/t-CO₂ [6].

### 3.2 Parasitic Loads and Compression Energy

The relationship between membrane properties and parasitic loads represents a critical aspect of CCS energy efficiency. While increasing CO₂ membrane permeability results in significant savings in capital cost by reducing required membrane area, it comes with the trade-off of lower CO₂/N₂ selectivity, which eventually results in larger plant parasitic loads [4]. This relationship creates characteristic curves in energy efficiency analyses, where improvements in one performance metric necessarily degrade another.

The operating pressures of membrane stages are optimized to minimize the levelized cost of electricity (LCOE) while achieving target capture rates [4]. Membrane CO₂/N₂ selectivity is varied over a broad range encompassing values considered by membrane technology developers, while membrane CO₂ permeability is varied with selectivity according to the variation anticipated by the upper bound of the Robeson plot for CO₂ and N₂ [4]. The optimization space of membrane properties and operating conditions is scanned globally to determine the process design that minimizes LCOE, revealing the complex interplay between diffusion resistance, selectivity, and energy consumption.

### 3.3 Vacuum Versus Compression Configurations

The choice between vacuum pump and compressor configurations for the permeate side has significant implications for energy efficiency and is directly influenced by diffusion resistance characteristics. At a fixed pressure ratio, vacuum pumps offered lower energy use compared to compressors, although they required larger membrane areas [7]. This observation favors high-permeance membranes (lower diffusion resistance) for vacuum configurations and high-selectivity membranes for compressor-based systems [7].

For biogas upgrading applications, which typically operate at 3–7 bar, the permeate side can remain at atmospheric pressure, eliminating the need for vacuum pumps [7]. However, post-combustion flue gas applications present different challenges, as the low CO₂ partial pressure in flue gas necessitates either significant compression of the feed stream or application of vacuum to the permeate side to create an adequate driving force. The flue gas must be kept at atmospheric pressure and the concentrated CO₂ stream kept under vacuum (approximately three pounds per square inch) conditions for effective separation [8].

## 4. Trade-off Relationships and the Robeson Upper Bound

### 4.1 The Permeability-Selectivity Trade-off

The fundamental trade-off between membrane permeability and selectivity arises from the solution-diffusion mechanism governing gas transport through dense polymers. More permeable polymers are generally less selective and vice versa, a relationship that has been extensively documented in the membrane science literature [2]. The CO₂/N₂ selectivity for most types of polymeric membrane materials is less than 50 to 70, while CO₂ permeability varies substantially even within the same type of membrane material [2].

This trade-off has direct implications for diffusion resistance. Materials with higher diffusion coefficients (lower diffusion resistance) typically exhibit larger free volume fractions that reduce their ability to discriminate between gas species based on size, thereby decreasing selectivity. Conversely, highly selective materials often possess tighter polymer structures that increase diffusion resistance while providing superior separation performance. The challenge for membrane developers is to identify materials that approach the Robeson upper bound while maintaining adequate stability in the harsh environments encountered in CCS applications.

### 4.2 Implications for Multi-Stage Configurations

The optimization of multi-stage hybrid membrane processes for post-combustion CO₂ capture requires systematic evaluation of several design variables on LCOE [4]. The trade-off relationship between CO₂/N₂ selectivity and the feed-to-permeate operating pressure ratio must be balanced against the relationship between permeability and membrane area requirements. Multi-stage configurations offer opportunities to optimize these trade-offs by distributing separation tasks across multiple membrane units with different property requirements.

Research has demonstrated that membranes with high permeance reduce the required membrane area, while high selectivity improves CO₂ purity and decreases energy consumption [7]. For the four heavy industry-representative cases studied, membranes with selectivities above approximately 30 have essentially the same economics, suggesting that further improvements in selectivity beyond this threshold provide diminishing returns [9]. When the permeance of CO is above 1000 GPU and the selectivity is between 20 and 30, membrane systems can achieve low capture costs ($20 to $55 per ton) and high energy efficiencies (150 to 500 kWh per ton) [9].

### 4.3 Economic Optimization and Energy Efficiency Curves

The economic optimization of membrane-based CCS systems reveals characteristic relationships between membrane properties, process configuration, and energy efficiency. The objective function typically minimizes capture cost, defined as:

$$C_{capCost} = (\phi + \psi) \cdot CAPEX + OPEX + MREP$$

where CAPEX represents capital expenditure, OPEX represents operating expenditure, and MREP represents membrane replacement costs, all normalized by the CO₂ capture rate [6]. This formulation captures the trade-offs between capital costs (influenced by membrane area) and operating costs (influenced by energy consumption), both of which are affected by diffusion resistance.

The dimensionless feed flow and retentate recovery are associated with the capital cost and energy requirement, respectively [6]. Analysis of multi-stage membrane systems reveals that different stages may utilize different membrane materials optimized for their specific separation tasks, allowing partial decoupling of the permeability-selectivity trade-off across the overall process. This approach can reduce the impact of diffusion resistance on overall energy efficiency by matching membrane properties to the requirements of each separation stage.

## 5. Process Configuration Effects on Energy Efficiency

### 5.1 Single-Stage Versus Multi-Stage Configurations

The configuration of membrane separation systems significantly influences how diffusion resistance affects overall energy efficiency. Single-stage configurations are simpler but often require extreme operating conditions to achieve high capture rates, leading to elevated energy consumption. Multi-stage configurations offer improved flexibility but introduce additional complexity in terms of inter-stage compression requirements and overall process optimization.

Preliminary calculations have shown that the carbon capture energy requirement can be sufficiently reduced in a two-stage process [8]. In the first stage, CO₂ is removed from flue gas by evacuation; in the second stage, remaining CO₂ is removed using an air sweep such that the 90 percent capture target is met [8]. This configuration reduces the diffusion resistance impact by distributing the separation load across two stages with different driving force requirements.

### 5.2 Flow Configuration and Mass Transfer

The flow configuration within membrane modules affects the effective mass transfer coefficients and thereby influences the impact of diffusion resistance on system performance. Cross-flow and countercurrent-sweep stages have been analyzed with the aim of reducing both energy consumption and membrane area [10]. Different process configurations analyzed include cross-flow stages based on 2-D models capable of predicting separation through spiral-wound permeators, which provide more accurate predictions of mass transfer behavior than simplified 1-D models [10].

The comparison of different modeling approaches—constant overall mass transfer coefficient, 1-D resistance in series, 1-D and 2-D convection-diffusion models—reveals that the membrane mass transfer coefficient serves as the primary adjustable parameter governing prediction accuracy [10]. Higher-fidelity models that account for concentration polarization and boundary layer effects provide more accurate predictions of how diffusion resistance influences overall system performance, enabling better optimization of process design.

### 5.3 Integration with Power Plant Cycles

The integration of membrane-based carbon capture with power plant cycles introduces additional considerations for energy efficiency. For non-temperature-swing separation systems such as membranes, waste heat is not directly useful because the separation work constitutes a parasitic load on the power plant turbine [5]. The energy required for membrane-based separation therefore directly reduces the net power output available for electricity generation.

The energy penalty for post-combustion capture and storage of pulverized coal power plant CO₂ has been estimated by several different studies, with estimates differing between studies by nearly a factor of four [5]. Analysis of the relationships governing energy penalties provides insight into that spread as well as into future CCS development. The reviewed studies of pulverized coal retrofits include only small amounts of waste heat recovery, with associated second law efficiencies between 43% and 77%, indicating turbine efficiencies of approximately 40%–60% [5].

## 6. Material Considerations and Diffusion Resistance

### 6.1 Polymer Membrane Materials

Polymer-based membranes remain the only commercially viable type for CO₂ removal from flue gas, with materials including cellulose acetate, polyimides, polysulfone, and polycarbonates [11]. The performance of these materials depends on their stability in the environment of the real process, as exposure to gases such as CO₂, water vapor, and H₂S may result in plasticization and mechanical fouling that effectively increases diffusion resistance over time [11].

The poor thermal stability of polymeric membranes at operating temperatures above 100°C represents a significant limitation for post-combustion applications [11]. Only polybenzimidazole has been examined at the temperature range of 300–700°C for syngas purification, with the greatest performance in H₂ permeability and H₂/CO₂ selectivity observed between 200 and 270°C [11]. This peak performance relates to the increasing diffusivity of the smaller H₂ molecule as temperature increases, demonstrating the temperature dependence of diffusion coefficients.

### 6.2 Advanced Membrane Architectures

Novel thin-film composite polymer membranes have been developed to address the limitations of homogeneous polymer membranes [2]. These architectures typically feature a thin selective layer supported on a porous substrate, enabling reduction of the effective membrane thickness while maintaining mechanical integrity. The reduction in effective thickness directly reduces diffusion resistance by decreasing the diffusion path length, enabling higher flux rates without sacrificing selectivity.

Contaminant resistance represents another important consideration for membrane materials in CCS applications. Phosphazene-based membranes have been tested and found resistant to contaminant species such as oxygen, nitrogen oxide, sulfur dioxide, and moisture present in coal flue gas [8]. Fly ash particulate removal is required as pretreatment, and membrane replacement is estimated at approximately four years for commercial systems [8]. These practical considerations affect the long-term effective diffusion resistance of membrane systems, as fouling and degradation can increase resistance over the operational lifetime.

### 6.3 Inorganic and Hybrid Membranes

For applications involving syngas from coal gasification, which is released at much higher temperatures (250–400°C) and pressures (20–50 bar), the use of metallic membranes that can withstand such harsh conditions becomes necessary [7]. These inorganic membranes often exhibit different transport mechanisms than polymeric membranes, with molecular sieving and surface diffusion playing more prominent roles.

Pure Pd material membranes are susceptible to poisoning by sulphur compounds present in coal-derived syngas, requiring integration of sulphur resistant membrane materials [12]. Novel Pd-alloy H₂ membrane materials of higher sulphur tolerance have been developed, along with high temperature sorbent-based hydrogen sulphide removal technology that reduces process exergy loss and unlocks the potential of Pd membranes in integrated gasification combined cycle (IGCC)-CCS applications [12]. These technologies in combination enable Pd membrane advancement into broader coal pre-combustion CO₂ capture applications, with potential to reduce capture energy penalty by nearly 40% compared to state-of-the-art Selexol technology [12].

## 7. Quantitative Relationships Between Diffusion Resistance and Energy Efficiency

### 7.1 Membrane Area and Energy Demand Correlations

The relationship between membrane area and energy demand provides insight into how diffusion resistance affects CCS efficiency curves. As inlet CO₂ molar fraction increases from 0.20 to 0.30, membrane area requirements decrease from 371,880 m² to 193,536 m², while energy demand decreases from 284.5 kWh/t-CO₂ to 182.8 kWh/t-CO₂ [6]. This simultaneous reduction reflects the decreased importance of diffusion resistance at higher CO₂ concentrations, where the driving force for permeation is naturally higher.

The capture cost decreases significantly across this range, from $73.13/t-CO₂ at 0.20 inlet CO₂ molar fraction to $45.69/t-CO₂ at 0.30 [6]. These relationships demonstrate that diffusion resistance effects are not uniform across all operating conditions but vary depending on the feed composition and target separation requirements. Process optimization must therefore consider the specific application context when evaluating membrane system performance.

### 7.2 Operating Pressure Optimization

The optimization of feed and permeate pressures over ranges encompassing values proposed by membrane technology developers reveals the complex relationships between operating conditions and energy efficiency [4]. Higher feed pressures increase the driving force for permeation but require compression energy, while lower permeate pressures (achieved through vacuum) enhance the driving force but require vacuum pump energy.

The balance between these competing effects creates characteristic efficiency curves with optima at specific pressure combinations. For a given membrane material with fixed diffusion resistance characteristics, there exists an optimal pressure ratio that minimizes total energy consumption while achieving target capture rates. Deviations from this optimum in either direction increase the energy penalty, either through excessive compression requirements or through the need for larger membrane areas to compensate for reduced driving forces.

### 7.3 Recovery and Purity Trade-offs

The relationships between CO₂ recovery, CO₂ purity, and energy consumption reflect the fundamental trade-offs imposed by diffusion resistance. Higher recovery rates require either larger membrane areas or more extreme operating conditions, both of which increase energy consumption. Similarly, higher purity requirements increase the separation difficulty, effectively increasing the diffusion resistance penalty for a given membrane material.

Analysis of multi-stage membrane systems reveals stage-specific performance characteristics. For a three-stage system, membrane areas of 30,849 m², 107,800 m², and 54,887 m² were reported for stages M1, M2, and M3, respectively [6]. Inlet CO₂ molar fractions varied from 0.70 in the first stage to 0.15 in the third stage, with corresponding CO₂ purities of 0.90, 0.70, and 0.42 [6]. These variations reflect the decreasing driving force and increasing separation difficulty as the process progresses, demonstrating how diffusion resistance effects compound across multiple stages.

## 8. Implications for CCS System Design

### 8.1 Design Optimization Strategies

The optimization of membrane-based CO₂ capture processes requires careful consideration of emission source characteristics to minimize energy consumption [7]. Systematic understanding of process-performance relationships across different industrial streams enables identification of optimal membrane configurations for specific applications. The trade-offs between membrane properties and operating conditions must be balanced against economic considerations to achieve cost-effective carbon capture.

Process optimization is essential for maximizing both performance and energy efficiency [7]. The global optimization of membrane properties and operating conditions determines the process design that minimizes LCOE, requiring consideration of the full range of design variables and their interactions. This approach reveals that the impact of diffusion resistance on energy efficiency cannot be evaluated in isolation but must be considered as part of the overall system optimization problem.

### 8.2 Technology Development Priorities

The development of highly efficient materials for carbon capture and storage represents a critical research priority, including both adsorption and membrane technologies [10]. The synthesis and scale-up of sufficiently selective and permeable membranes remains the primary research challenge for membrane-based CCS [8]. Advances in membrane materials that push the Robeson upper bound while maintaining stability in harsh environments would significantly improve the energy efficiency of membrane-based capture systems.

Cost reductions in membrane manufacturing may reduce capital cost and lower LCOE, making membrane-based capture more economically competitive [4]. The development of scalable, low-cost membrane platforms such as hollow fiber supports represents an important advance toward commercial viability [8]. These technological developments, combined with improved process design and optimization, will determine the ultimate role of membrane technology in CCS deployment strategies.

### 8.3 Integration with Overall CCS Systems

The integration of membrane separation with compression, transport, and storage components of CCS systems introduces additional considerations for energy efficiency. Each of the CCS steps requires work, and the fuel requirement for performing this work constitutes the CCS energy penalty [5]. Membrane systems that minimize separation energy consumption contribute to reduced overall CCS energy penalties, but must be evaluated in the context of complete CCS chains.

Integration of hydrogen-selective membranes into natural gas combined cycle-CCS processes has been shown to reduce capture energy penalty by 15% and cost of CO₂ avoided by 7% compared to state-of-the-art methyl diethanolamine (MDEA) technology [12]. Similar benefits are anticipated for post-combustion applications as membrane technology matures and process integration strategies improve.

## 9. Conclusions

Diffusion resistance in membrane separation fundamentally affects CCS energy efficiency curves through its influence on membrane area requirements, operating pressure ratios, and parasitic energy loads. The solution-diffusion mechanism governing gas transport through dense polymer membranes creates inherent trade-offs between permeability and selectivity that manifest as characteristic curves in energy efficiency analyses. Higher diffusion resistance necessitates either increased membrane area (capital cost impact) or higher pressure differentials (operating cost impact), with the optimal balance depending on specific application requirements and economic constraints.

The Robeson upper bound relationship between permeability and selectivity represents a fundamental constraint that must be navigated during membrane material selection and process design. Multi-stage configurations offer opportunities to partially decouple this trade-off by distributing separation tasks across multiple membrane units with different property requirements. The optimization of operating conditions—including feed pressure, permeate pressure, and stage configurations—enables minimization of energy consumption for given membrane properties, while advances in membrane materials that approach or exceed the Robeson upper bound offer pathways to improved overall efficiency.

The energy penalty associated with membrane-based carbon capture directly impacts the net power output of host facilities and therefore the economic viability of CCS deployment. Understanding the relationships between diffusion resistance and energy efficiency is essential for process designers, membrane developers, and policy makers seeking to optimize CCS system performance. Continued research into membrane materials, process configurations, and system integration strategies will further improve the energy efficiency of membrane-based carbon capture, advancing the deployment of this promising technology toward commercial viability.

## References

[1] U.S. Department of Energy National Energy Technology Laboratory, "Advanced Process Modeling and Experimentation," Program 149, https://netl.doe.gov/sites/default/files/netl-file/Program-149_0.pdf.

[2] University of Wyoming Institute for Energy Conversion and Management, "Membrane Technology Report," September 2012, https://www.uwyo.edu/iecm/_bfiles/documentation/201209_iecmtd_memb-tech-report.pdf.

[3] ChemRxiv, "Insights into Energetic Penalties in Electrochemical CO₂ Separation Systems," https://chemrxiv.org/engage/api-gateway/chemrxiv/assets/orp/resource/item/663e0b3c418a5379b0ee6312/original/insights-into-energetic-penalties-in-electrochemical-co2-separation-systems.pdf.

[4] Roussanaly et al., "Optimization of Multi-Stage Hybrid Membrane Processes for Post-Combustion CO₂ Capture," 2016, https://www.sciencedirect.com/science/article/abs/pii/S1750583616308799.

[5] Harvard University, "Energy Penalty Analysis for Carbon Capture and Storage," https://dash.harvard.edu/bitstreams/7312037d-225f-6bd4-e053-0100007fdf3b/download.

[6] U.S. Department of Energy Office of Scientific and Technical Information, "Optimal Design of Multi-Stage Membrane Process for Carbon Capture," https://www.osti.gov/servlets/purl/2402978.

[7] B.T. Low et al., "Effects of Membrane Material Properties and Process Variables Under Post-Combustion Conditions," https://pmc.ncbi.nlm.nih.gov/articles/PMC12298987/.

[8] U.S. Department of Energy National Energy Technology Laboratory, "Post-Combustion Membranes Technology Update," May 2013, https://netl.doe.gov/sites/default/files/2017-12/CO2-Capture-Tech-Update-2013-Post-Combustion-Membranes.pdf.

[9] Elsevier, "Membrane Systems for Heavy Industry Decarbonization," 2023, https://www.sciencedirect.com/science/article/pii/S2772656823000866.

[10] Elsevier, "Multi-Stage Membrane Configurations for Carbon Capture," 2023, Journal of Cleaner Production, https://www.sciencedirect.com/science/article/abs/pii/S073519332100289X.

[11] U.S. Environmental Protection Agency, "Membrane Separation Technology in Carbon Capture," https://downloads.regulations.gov/EPA-HQ-OAR-2023-0072-0057/attachment_22.pdf.

[12] European Commission, "Hydrogen Membrane Development for IGCC-CCS," CORDIS Project ID 241342, https://cordis.europa.eu/project/id/241342/reporting.

## Annotations


## Sources
[1] https://chemrxiv.org/engage/api-gateway/chemrxiv/assets/orp/resource/item/663e0b3c418a5379b0ee6312/original/insights-into-energetic-penalties-in-electrochemical-co2-separation-systems.pdf
[2] https://cordis.europa.eu/project/id/241342/reporting
[3] https://dash.harvard.edu/bitstreams/7312037d-225f-6bd4-e053-0100007fdf3b/download
[4] https://downloads.regulations.gov/EPA-HQ-OAR-2023-0072-0057/attachment_22.pdf
[5] https://netl.doe.gov/sites/default/files/2017-12/CO2-Capture-Tech-Update-2013-Post-Combustion-Membranes.pdf
[6] https://netl.doe.gov/sites/default/files/netl-file/Program-149_0.pdf
[7] https://pmc.ncbi.nlm.nih.gov/articles/PMC12298987/
[8] https://pubs.rsc.org/en/content/articlehtml/2018/ee/c7ee02342a
[9] https://www.osti.gov/servlets/purl/2402978
[10] https://www.sciencedirect.com/science/article/abs/pii/S073519332100289X
[11] https://www.sciencedirect.com/science/article/abs/pii/S1750583616308799
[12] https://www.sciencedirect.com/science/article/pii/S2772656823000866
[13] https://www.uwyo.edu/iecm/_bfiles/documentation/201209_iecmtd_memb-tech-report.pdf