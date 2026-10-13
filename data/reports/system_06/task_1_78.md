# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** e3f2b53d | **Time:** 279.98s | **Cost:** $0.14131
--------------------------------------------------------------------------------

# How Activation Energy Barriers Constrain Plastic Recycling Purity Control Given Molecular Weight Distribution

## Abstract

The pursuit of circular economy principles in polymer recycling faces fundamental thermodynamic and kinetic constraints that manifest through the interplay between activation energy barriers and molecular weight distribution. This report examines how the energy requirements for bond scission reactions, which vary significantly with polymer chain length and architecture, fundamentally limit the purity and quality achievable through both mechanical and chemical recycling pathways. The analysis reveals that activation energy barriers create inherent trade-offs between processing severity, molecular weight retention, and product purity, establishing critical boundaries for recycling technology development. Understanding these constraints is essential for designing effective recycling strategies and catalyst systems that can navigate the complex energy landscape of polymer degradation and reconstruction.

## 1. Introduction

The global plastic waste crisis has intensified focus on recycling technologies, yet the fundamental physicochemical constraints governing polymer reprocessing remain insufficiently understood in the context of circular economy implementation. Plastic recycling presents a multifaceted challenge that extends far beyond simple collection and reprocessing logistics, touching upon deep principles of polymer chemistry, thermodynamics, and reaction kinetics. The molecular weight distribution of polymeric materials represents a critical parameter that influences virtually every aspect of recycling efficacy, from mechanical property retention to the selectivity of chemical depolymerization pathways.

Activation energy barriers constitute the fundamental thermodynamic constraints that govern whether and how polymer chains can be selectively broken down or reformed during recycling processes. These energy barriers arise from the strength of chemical bonds within the polymer backbone and the specific reaction mechanisms through which bond cleavage occurs. The magnitude of these barriers determines the processing conditions required for recycling, the extent of side reactions that compete with desired transformations, and ultimately the purity and quality of recycled products. As the polymer community seeks to transition from linear to circular material flows, a rigorous understanding of how activation energy barriers interact with molecular weight distribution becomes paramount for technology development and process optimization.

This report synthesizes current understanding of activation energy barriers in polymer recycling contexts, examining how these energy constraints manifest across different recycling methodologies and polymer types. The analysis focuses particularly on how molecular weight distribution influences the energy landscape of polymer transformations and constrains the achievable purity in recycled materials. By examining the fundamental kinetics and thermodynamics governing polymer degradation and reconstruction, this report aims to provide a comprehensive framework for understanding the inherent limitations and opportunities in plastic recycling technology.

## 2. Fundamental Principles of Activation Energy in Polymer Systems

### 2.1 Thermodynamic Foundations of Bond Scission

The chemical bonds connecting monomer units in polymer chains represent the fundamental structural elements that must be manipulated during recycling processes. For carbon-carbon bonds, which constitute the primary linkages in commodity polymers such as polyethylene, polypropylene, and polystyrene, the bond dissociation energy provides a baseline reference for the minimum energy required to effect chain scission. The carbon-carbon single bond energy of approximately 348 kJ mol⁻¹ represents the theoretical minimum energy barrier for homolytic bond cleavage under idealized conditions [1]. However, the actual activation energy observed experimentally for polymer degradation processes frequently deviates substantially from this idealized value, reflecting the complex interplay of molecular architecture, chain conformation, and reaction environment.

The relationship between activation energy and reaction rate is governed by the Arrhenius equation, which expresses the rate constant k as a function of the activation energy barrier Eₐ, the gas constant R, and temperature T:

$$k = k_0 \exp\left(-\frac{E_a}{RT}\right)$$

where k₀ represents the pre-exponential factor that accounts for the frequency of molecular collisions and the orientation requirements for successful reaction [1]. This fundamental relationship establishes that even modest differences in activation energy translate into exponentially large differences in reaction rates at given temperatures, creating sharp thresholds for when specific degradation pathways become kinetically accessible.

### 2.2 Chain Length Dependence of Activation Energies

A crucial finding in polymer degradation science is that activation energy for chain scission depends significantly on the degree of polymerization, particularly for shorter chains. Studies on polyethylene random scission have revealed activation energy values ranging from approximately 251 kJ mol⁻¹ for chains containing 100 repeat units to 305 kJ mol⁻¹ for chains consisting of only five repeat units [1]. This chain length dependence reflects the differential stability of polymer chains as a function of their molecular weight, with shorter chains exhibiting lower activation barriers due to reduced stabilization of the transition state and altered thermodynamic driving forces for bond cleavage.

Molecular dynamics modeling has provided additional insight into the relationship between chain length and scission kinetics. These simulations demonstrate an acceleration of scission reactions with increasing chain length up to a degree of polymerization of approximately five, after which this effect saturates for longer chains [1]. The saturation behavior suggests that the chain length dependence of activation energy becomes negligible beyond a certain molecular weight threshold, which has important implications for understanding the degradation behavior of high molecular weight polymers typical of commodity plastic applications.

The practical consequence of this chain length dependence is that the molecular weight distribution of a polymer sample inherently determines the distribution of activation energies present within the material. A polydisperse polymer, characterized by a broad molecular weight distribution, will exhibit a corresponding distribution of activation energies for bond scission reactions. This heterogeneity in activation barriers complicates the design of recycling processes that must operate under conditions selective for specific molecular weight fractions.

### 2.3 Activation Energy for Mass Loss Kinetics

Beyond the fundamental bond scission events, the overall activation energy for mass loss during polymer degradation represents an experimentally accessible parameter that integrates multiple elementary processes. For polyethylene degradation, activation energies for mass loss have been reported within the range of 150-250 kJ mol⁻¹, depending on the specific experimental conditions and the conversion level at which measurements are made [1]. This range reflects the complexity of polymer degradation, which involves not only bond scission but also the diffusion and volatilization of lower molecular weight fragments.

The conversion-dependent nature of the activation energy for mass loss indicates that the degradation mechanism evolves as the reaction proceeds. Initial stages of degradation may be dominated by scission of weaker bonds or chain ends, while later stages involve more stable backbone segments. This temporal evolution of the rate-limiting step has direct implications for recycling process design, as optimal conditions may change throughout the processing timeline.

## 3. Mechanical Recycling Constraints from Activation Energy Barriers

### 3.1 Thermomechanical Degradation During Reprocessing

Mechanical recycling, which involves physical reprocessing of polymer materials through melting and reshaping, is fundamentally limited by the thermomechanical degradation that occurs during processing. The elevated temperatures required to melt polymers and enable flow through processing equipment inevitably approach the temperature regime where thermal degradation becomes kinetically accessible. For polystyrene processing, temperatures around 205°C are typically employed during extrusion and regranulation, yet these conditions can induce material degradation manifested as discoloration (yellowing) and formation of toxic low-molecular-weight degradation products including styrene, benzaldehyde, and ethylbenzene [2].

The formation of these low molecular weight products reflects the competition between chain scission reactions that generate volatile fragments and the cross-linking reactions that can lead to gel formation. The relative rates of these competing pathways depend on the specific polymer structure, processing conditions, and the presence of additives or contaminants. For polypropylene, which contains tertiary carbons that stabilize radical intermediates, the degradation behavior is particularly complex, with chain scission and cross-linking occurring simultaneously in a competitive manner [3].

Molecular weight distribution measurements following multiple extrusion cycles reveal characteristic patterns of degradation. Studies on polypropylene have demonstrated that chain scission occurs preferentially near the middle portions of macromolecules, consistent with the Bueche theory for mechanical degradation [3]. The molecular weight and polydispersity reduction observed during recycling reflects the cumulative effect of chain scission events that progressively fragment the polymer distribution toward lower molecular weights.

### 3.2 Temperature-Dependent Degradation Regimes

Detailed investigation of polypropylene degradation during multiple extrusion cycles has identified three distinct temperature regimes with different degradation behaviors [3]. At temperatures between the melt temperature and approximately 230°C, no appreciable degradation occurs, suggesting that the activation energy barrier for significant chain scission is not overcome under these conditions. This observation defines a processing window where mechanical recycling can be conducted with minimal molecular weight degradation.

However, between 230°C and 250°C, a rapid increase in chain scission rate occurs with rising temperature, indicating that this temperature range encompasses the activation energy threshold for significant degradation. The exponential sensitivity of degradation rate to temperature in this regime creates practical challenges for process control, as small temperature excursions can result in substantial changes to the molecular weight distribution of the recycled material.

Above 250°C, the number of chain scissions reaches a plateau where further temperature increases do not accelerate degradation. This saturation behavior suggests that the rate-limiting step transitions from bond scission to some other process, possibly the diffusion of reactive intermediates or the availability of susceptible bond sites. The existence of this plateau has important implications for high-temperature processing, as it indicates that aggressive processing conditions may not necessarily accelerate degradation beyond a certain point.

### 3.3 Molecular Weight Distribution Evolution During Recycling

The molecular weight distribution of recycled polymers evolves characteristically during mechanical recycling, with the pattern of evolution depending on the specific polymer and processing conditions. For polyethylene terephthalate (PET), consecutive processing cycles induce systematic changes in molecular weight, rheological properties, thermal behavior, and mechanical characteristics [4]. These variations are interconnected through the fundamental relationships between molecular structure and material properties, creating cascading effects that propagate through the material hierarchy.

The connectivity of molecular and material property variations during recycling cycles presents a fundamental challenge for quality control in mechanical recycling. As molecular weight decreases and molecular weight distribution broadens during reprocessing, the resulting materials exhibit altered flow behavior, reduced mechanical strength, and modified thermal properties. These changes limit the applications for which recycled materials can be used and contribute to the phenomenon of downcycling, where recycled products are of lower quality than their virgin counterparts.

The downcycling trajectory of mechanically recycled plastics reflects the cumulative effect of molecular weight degradation. Materials that enter the recycling stream with degraded molecular weight distributions cannot be fully restored to virgin-like properties through mechanical reprocessing alone. The activation energy barriers that govern thermal degradation ensure that any reprocessing at elevated temperatures will cause some degree of additional chain scission, progressively shifting the molecular weight distribution toward lower values with each recycling generation.

## 4. Chemical Recycling and Activation Energy Constraints

### 4.1 Overcoming Energetic Barriers Through Catalysis

Chemical recycling offers the potential to overcome the activation energy barriers that constrain mechanical recycling by employing catalysts or reagents specifically designed to lower the energy requirements for bond cleavage. The fundamental challenge lies in developing catalytic systems that can selectively break down polymer chains into desired products while minimizing unwanted side reactions. Robust, recyclable catalysts operating under conditions that overcome the refractory properties of plastics are needed, while avoiding long-lived intermediates such as radicals that lead to cross-linking or uncontrolled chain cleavage [5].

The design of effective catalysts for polymer depolymerization requires detailed understanding of the activation energy landscape for the target reaction. For many polymer systems, the activation energy for random chain scission via homolytic cleavage is prohibitively high for practical processing, necessitating alternative reaction pathways with lower energy barriers. Catalytic systems can provide these lower-energy pathways by stabilizing transition states or by enabling heterolytic cleavage mechanisms that differ fundamentally from the homolytic processes dominant in thermal degradation.

### 4.2 End-Group Effects on Depolymerization Kinetics

A particularly important finding in chemical recycling research is that the presence of reactive end-groups can substantially lower the activation energy barrier for depolymerization. For polymers prepared by controlled polymerization methods, the ω chain-ends that enable controlled synthesis can often be leveraged to initiate depolymerization at temperatures substantially lower than those required for random chain scission [6]. This phenomenon reflects the lower energy pathway available when depolymerization proceeds through depropagation from chain ends rather than random backbone cleavage.

The thermodynamic equilibrium between monomer and polymer involves only active polymer chains, meaning that for a presynthesized polymer to depolymerize, chains must first be transformed to an active state [6]. For conventional polymers with terminated chain ends, this activation requires sufficient energy for random chain scission to occur. However, polymers synthesized by controlled methods such as reversible-deactivation radical polymerization (RDRP) techniques retain reactive chain ends that can directly initiate depropagation without the high-energy random scission step.

The extent of depolymerization achievable through end-group initiated pathways depends critically on end-group fidelity during the depolymerization process. Studies have demonstrated that loss of end-group fidelity inhibits depolymerization, as the reactive sites necessary for initiating the low-energy depropagation pathway are lost [6]. This finding establishes a direct connection between synthesis conditions, molecular weight distribution characteristics, and depolymerization behavior.

### 4.3 Kinetic Barriers in Polyester and Polycarbonate Depolymerization

Quantitative studies of activation energy barriers for polymer depolymerization have revealed systematic relationships between polymer structure and recycling kinetics. For polyesters with different linker lengths, the kinetic barriers as assessed by transition-state free-energy differences show characteristic patterns [7]. The 6-atom polyester series exhibits activation enthalpies ranging from 62 to 96 kJ mol⁻¹, while the 7-atom series shows values from 71 to 81 kJ mol⁻¹, with corresponding free energy barriers of 102-118 kJ mol⁻¹ and 118-132 kJ mol⁻¹ respectively [7].

Polycarbonates present a contrasting case, with midchain-substituted variants showing lower activation barriers than unsubstituted analogues. For example, polycarbonate PC-6b exhibits an activation enthalpy of 88 kJ mol⁻¹ compared to 96 kJ mol⁻¹ for PC-6a, a difference attributed to increased torsional strain in the substituted polymer that raises the ground-state energy and decreases the enthalpy cost for intramolecular cyclization [7]. This structure-reactivity relationship demonstrates how subtle changes in polymer architecture can significantly influence the energy landscape for depolymerization.

The rate constants for depolymerization span several orders of magnitude depending on polymer structure, ranging from approximately 0.65 × 10⁻⁴ mol⁻¹ s⁻¹ dm³ for the slowest systems to 5500 × 10⁻⁴ mol⁻¹ s⁻¹ dm³ for the fastest [7]. This enormous range in reaction rates reflects the fundamental influence of activation energy barriers on process feasibility and has direct implications for the design of industrial chemical recycling processes.

### 4.4 Competing Pathways and Selectivity Challenges

The activation energy landscape for polymer degradation typically contains multiple competing pathways that lead to different products with different molecular weights. Chain scission can occur through random backbone cleavage, chain-end depropagation, or chain-centered fragmentation, each with its own characteristic activation energy [8]. The relative rates of these pathways determine the molecular weight distribution of degradation products and the selectivity of the recycling process.

For solvent-swelling induced main-chain scission, the mechanism stands apart from classical chain degradation reactions as it is caused by chain-internal mechanical stress rather than external forces or chemical attack [8]. The activation barrier for this mechanical scission pathway differs from that for thermal or chemical degradation, creating opportunities for selective processing under conditions where specific pathways are favored.

The presence of radical trapping agents can suppress certain degradation pathways while leaving others unaffected, providing mechanistic insight into the reaction network. Studies have shown that in the presence of radical traps, no depolymerization occurs through pathways that generate radical intermediates, while polar pathways may still proceed if their activation barriers are sufficiently low [8]. This selectivity in pathway suppression highlights the complex interplay of activation energies governing polymer degradation.

## 5. Molecular Weight Distribution as a Constraining Factor

### 5.1 Polydispersity Effects on Processing

The molecular weight distribution of polymer feeds represents a critical variable that influences activation energy barriers and recycling outcomes. A broad molecular weight distribution, characterized by high polydispersity index, implies a corresponding distribution of activation energies for bond scission reactions. This heterogeneity complicates process design, as conditions optimized for one molecular weight fraction may be suboptimal or even detrimental for others.

During mechanical recycling, the molecular weight distribution evolves in characteristic ways that depend on the relative rates of chain scission for chains of different lengths. If shorter chains degrade preferentially, the distribution may narrow during processing; if longer chains are more susceptible, the distribution may broaden. Understanding these dynamics requires detailed knowledge of how activation energy depends on chain length and how this dependence translates into differential reaction rates.

The practical consequence of polydispersity effects is that recycled polymer batches exhibit variable processing behavior and product quality. The molecular weight distribution of incoming waste materials varies depending on the history of the material, including the number of prior processing cycles, the specific conditions of previous use, and the presence of additives or contaminants. This variability propagates through recycling processes, creating challenges for quality control and product specification.

### 5.2 Low Molecular Weight Fraction Behavior

The low molecular weight fraction of polymer materials presents unique challenges and opportunities in recycling contexts. Low-molecular-weight products generated during degradation can be purified and reused as chemical feedstock, replacing raw materials in polymerization processes [2]. This pathway, sometimes termed "Ressource Life-Cycle," represents a form of chemical recycling that bypasses the limitations of mechanical reprocessing by converting polymers to their constituent monomers or oligomers.

However, the presence of low molecular weight species also creates purity concerns, particularly for applications with stringent material specifications. The formation of toxic low-molecular-weight degradation products such as styrene, benzaldehyde, and ethylbenzene during polystyrene processing demonstrates how activation energy barriers for side reactions can generate contaminants that limit the usability of recycled materials [2]. These low molecular weight impurities may be difficult to separate from the bulk polymer and can compromise material safety and performance.

The activation energy for formation of low molecular weight fragments depends on the specific chemical reactions involved and the molecular structure of the polymer. For polymers with weak links in the backbone or susceptible side groups, the barriers for generating low molecular weight products may be substantially lower than for random backbone scission, leading to preferential formation of specific contaminants.

### 5.3 High Molecular Weight Fraction Constraints

At the opposite end of the molecular weight distribution, high molecular weight fractions present different constraints for recycling processes. Very long chains may exhibit different degradation behavior than shorter chains due to entropic effects, chain entanglement, and the statistical distribution of weak points along the chain. The activation energy for scission of very long chains may approach the theoretical limit set by the bond dissociation energy, requiring more severe conditions for depolymerization.

The presence of high molecular weight fractions in recycled materials can be beneficial for mechanical properties but problematic for chemical recycling processes. High molecular weight polymers may be resistant to complete depolymerization, leading to residual material that must be separated and disposed of or processed further. The energy barriers for complete depolymerization of high molecular weight fractions may be substantially higher than for mid-range molecular weights, creating thermodynamic constraints on recycling efficiency.

## 6. Integrated Perspectives on Purity Control

### 6.1 Trade-offs Between Processing Severity and Product Quality

The relationship between activation energy barriers and molecular weight distribution creates fundamental trade-offs in recycling process design. More severe processing conditions, characterized by higher temperatures or more aggressive chemical environments, can overcome higher activation energy barriers and achieve more complete depolymerization or cleaning of contaminated materials. However, these severe conditions also promote side reactions that generate impurities, degrade molecular weight, and compromise product quality.

Conversely, milder processing conditions preserve molecular weight and minimize side reactions but may not overcome the activation energy barriers necessary for removing certain contaminants or achieving complete depolymerization. The optimal processing strategy must balance these competing considerations, selecting conditions that achieve the required transformation while minimizing unwanted effects.

For mechanical recycling, this trade-off manifests as the choice between processing temperatures that minimize degradation while still enabling adequate flow and mixing for product formation. For chemical recycling, the trade-off involves selecting catalysts and conditions that selectively lower activation barriers for desired reactions without promoting competing degradation pathways.

### 6.2 Energy Requirements and Environmental Considerations

The activation energy barriers for polymer degradation translate directly into energy requirements for recycling processes. Breaking down long-chain polymers using heat or chemical reactions is often significantly more energy-intensive than mechanical recycling through melting and reforming [9]. If the energy required to overcome activation barriers is derived from fossil fuels, the process contributes to greenhouse gas emissions that may offset environmental benefits aimed at by diverting plastic from landfills or incineration.

The energy intensity of chemical recycling depends critically on the activation energy landscape for the target polymer and the efficiency of catalytic or reagent systems in lowering effective barriers. Processes that require temperatures high enough to overcome high activation barriers without catalytic assistance will be particularly energy-intensive, while catalytic systems that provide lower-energy pathways can substantially reduce energy requirements.

The environmental footprint of recycling processes is therefore heavily dependent on the relationship between activation energy barriers, molecular weight distribution, and processing conditions. A comprehensive assessment of recycling technology must consider not only the technical feasibility of achieving desired transformations but also the energy implications of the activation energy barriers involved.

### 6.3 Implications for Circular Economy Development

The activation energy constraints on plastic recycling have profound implications for the development of circular economy approaches. The fundamental thermodynamic and kinetic limitations ensure that perfect recycling, in which materials are recovered with identical properties to virgin inputs, is not achievable through current technologies. Each recycling cycle imposes some degree of molecular weight degradation and property loss that cannot be fully reversed.

This reality suggests that circular economy strategies for plastics must incorporate both mechanical and chemical recycling pathways in an integrated manner. Mechanical recycling can preserve value for materials that have not undergone significant degradation, while chemical recycling provides a pathway for recovering chemical value from materials that have degraded beyond the point where mechanical reprocessing is viable. The "Waste" path, which removes materials from the cycle through landfilling or incineration, must be minimized through strategic deployment of both recycling approaches [2].

The development of new catalytic systems and processing technologies that more effectively navigate activation energy landscapes represents a critical research priority. Advances in understanding how polymer structure influences activation barriers, how molecular weight distribution affects process selectivity, and how catalysts can provide lower-energy reaction pathways will enable the development of more efficient and sustainable recycling technologies.

## 7. Conclusions

The analysis presented in this report demonstrates that activation energy barriers fundamentally constrain plastic recycling purity control through their interaction with molecular weight distribution. The energy required to break chemical bonds in polymer chains varies with chain length, molecular architecture, and reaction mechanism, creating complex energy landscapes that limit the selectivity and efficiency of recycling processes. These constraints manifest across both mechanical and chemical recycling pathways, though in different ways and with different practical implications.

For mechanical recycling, activation energy barriers define processing windows within which thermal degradation can be minimized while still enabling material flow and reshaping. The temperature-dependent nature of degradation rates creates narrow optimal processing ranges, and the cumulative effect of chain scission during multiple recycling cycles progressively degrades molecular weight and material properties. The molecular weight distribution of recycled materials evolves characteristically during processing, with the pattern of evolution depending on the specific polymer and conditions.

For chemical recycling, activation energy barriers determine the feasibility and selectivity of depolymerization pathways. The discovery that reactive end-groups can lower activation barriers for depolymerization opens opportunities for more efficient recycling of polymers synthesized by controlled methods. However, the competing pathways available in complex polymer systems create selectivity challenges that complicate product purification.

The molecular weight distribution of polymer feeds and products represents a critical variable that influences activation energy barriers and recycling outcomes. The polydispersity of real polymer materials implies a distribution of activation energies that complicates process design and creates variability in recycling outcomes. Understanding and managing this relationship between molecular weight distribution and activation energy is essential for advancing recycling technology.

Moving forward, the development of more effective recycling technologies will require continued research into the fundamental relationships between polymer structure, activation energy barriers, and reaction pathways. Advances in catalyst design, process optimization, and quality control strategies must be grounded in a rigorous understanding of these fundamental constraints. Only through such understanding can the plastic recycling community develop technologies capable of establishing truly circular material flows for polymeric materials.

## References

[1] Activation energy values for polyethylene random scission range from approximately 251 kJ mol⁻¹ for chains with 100 repeat units to 305 kJ mol⁻¹ for chains with 5 repeat units, compared to the carbon-carbon bond energy of approximately 348 kJ mol⁻¹. Molecular dynamics modeling shows acceleration of scission with increasing chain length up to degree of polymerization of five, with saturation for longer chains. Activation energy for mass loss during degradation is reported within the range of 150-250 kJ mol⁻¹.

[2] Mechanical recycling processes often result in mixed plastic unsuitable for food packaging reuse, leading to downcycling applications. Low-molecular-weight products can be purified and reused as chemical feedstock through chemical recycling. Polystyrene recycling involves extrusion at around 205°C, where local overheating can cause degradation, discoloration, and formation of toxic low-molecular-weight products like styrene, benzaldehyde, and ethylbenzene.

[3] Polypropylene degradation during multiple extrusion cycles shows chain scission as the dominant degradation reaction. Molecular weight distribution curves suggest chain scissions occur near the middle of macromolecules. Three temperature regimes are observed: no appreciable degradation between melt temperature and 230°C, rapid increase in chain scissions from 230-250°C, and plateau in scission rate above 250°C.

[4] PET mechanical recycling feasibility requires acknowledgment of chemical and material property variations during consecutive processing cycles. Molecular variations influence rheological, thermal, and mechanical properties, necessitating improved assessment linking molecular and material scales for effective recycling strategy development.

[5] Chemical upcycling requires catalysts or reagents to overcome refractory physical and chemical properties of plastics while avoiding long-lived intermediates like radicals that cause cross-linking or uncontrolled chain cleavage. Chain scission reactions may occur spontaneously in the melt phase during mechanical recycling or as side reactions in two-electron processes.

[6] For depolymerization, polymers must first be transformed to an active state for depropagation to occur. Polymers from controlled polymerization methods retain reactive chain ends that can initiate depropagation at lower temperatures than random chain scission. The extent of depolymerization is inhibited by loss of end-group fidelity during the process.

[7] Kinetic barriers for polyester depolymerization show activation enthalpies ranging from 62-96 kJ mol⁻¹ for 6-atom linkers and 71-81 kJ mol⁻¹ for 7-atom linkers, with corresponding free energy barriers of 102-132 kJ mol⁻¹. Polycarbonates with midchain substitution show lower barriers due to increased torsional strain raising ground-state energy.

[8] Solvent-swelling induced main-chain scission is caused by chain-internal mechanical stress, distinct from classical degradation. The mechanism involves chain-centered fragmentation similar to sonication-induced degradation. Radical pathways can be suppressed by trapping agents, while polar pathways may still proceed depending on activation barriers.

[9] Chemical recycling energy requirements for breaking down long-chain polymers are often significantly higher than mechanical recycling. The environmental footprint depends heavily on energy source and conversion process efficiency. High temperatures needed to overcome activation barriers can promote unwanted side reactions such as homolysis.

## Annotations


## Sources
[1] http://kinampark.com/T-Polymers/files/All%20References/Vogt%202021%2C%20Why%20is%20Recycling%20of%20Postconsumer%20Plastics%20so%20Challenging.pdf
[2] http://www.ijsit.com/admin/ijsit_files/INFLUENCE%20OF%20THE%20REPROCESSING%20CYCLES%20ON%20THE%20PROPERTIES%20OF%20POLYPROPYLENE_IJSIT_12.3.8.pdf
[3] https://cdn.intechopen.com/pdfs/32560/InTech-Recent_advances_in_the_chemical_recycling_of_polymers_pp_ps_ldpe_hdpe_pvc_pc_nylon_pmma_.pdf
[4] https://digitalcommons.library.uab.edu/etd-collection/405/
[5] https://dr.lib.iastate.edu/bitstreams/5994a5f7-ef8f-4f05-b595-c68404ea1668/download
[6] https://eprints.whiterose.ac.uk/id/eprint/228769/1/mcguire-et-al-2025-the-science-of-polymer-chemical-recycling-catalysis-uncovering-kinetic-and-thermodynamic-linear-free.pdf
[7] https://iopscience.iop.org/article/10.1088/2515-7639/ad5c06
[8] https://link.springer.com/article/10.1186/s44147-025-00799-2
[9] https://open.clemson.edu/cgi/viewcontent.cgi?article=5632&context=all_theses
[10] https://pmc.ncbi.nlm.nih.gov/articles/PMC12648417/
[11] https://pollution.sustainability-directory.com/question/what-are-the-main-challenges-of-chemical-recycling/
[12] https://pubs.acs.org/doi/10.1021/acsengineeringau.3c00056
[13] https://pubs.acs.org/doi/10.1021/acssuschemeng.4c02551
[14] https://pubs.acs.org/doi/10.1021/jacs.3c00589
[15] https://pubs.rsc.org/en/content/articlehtml/2019/sc/c9sc01639b
[16] https://pubs.rsc.org/en/content/articlehtml/2024/gc/d3gc04215d
[17] https://rex.libraries.wsu.edu/view/pdfCoverPage?instCode=01ALLIANCE_WSU&filePid=13366054160001842&download=true
[18] https://science.osti.gov/-/media/bes/pdf/reports/2020/Chemical_Upcycling_Polymers.pdf
[19] https://verso.uidaho.edu/view/pdfCoverPage?instCode=01ALLIANCE_UID&filePid=13308638010001851&download=true
[20] https://www.mdpi.com/1420-3049/28/5/2344
[21] https://www.mdpi.com/2073-4360/17/22/2991
[22] https://www.nature.com/articles/s41467-024-50702-5
[23] https://www.sciencedirect.com/org/science/article/pii/S2753812524002866
[24] https://www.sciencedirect.com/science/article/abs/pii/S014139102100063X
[25] https://www.sciencedirect.com/science/article/abs/pii/S0141391096002339