# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** e8ee1932 | **Time:** 288.57s | **Cost:** $0.18962
--------------------------------------------------------------------------------

# Do Partition Coefficients in Solvent Extraction Affect the Economic Feasibility of Urban Mining Recovery?

## Abstract

Partition coefficients represent fundamental thermodynamic parameters that govern the efficiency and selectivity of solvent extraction processes in urban mining operations for rare earth element recovery. This research report examines the intricate relationship between partition coefficients—encompassing distribution ratios ($D$) and separation factors ($\beta$)—and the economic viability of urban mining recovery systems. Through analysis of the underlying physicochemical principles and their practical implications, this report demonstrates that partition coefficients exert a profound influence on multiple economic determinants, including capital expenditure requirements, operational costs, recovery yields, and process scalability. The findings indicate that favorable partition coefficients can substantially reduce the number of extraction stages required, minimize reagent consumption, and enhance overall process efficiency, thereby directly impacting the economic feasibility of urban mining ventures. Conversely, unfavorable partition coefficients necessitate more complex process designs, increased equipment investments, and higher operational expenditures, potentially rendering otherwise viable urban mining projects economically uncompetitive.

## 1. Introduction

### 1.1 Background and Context

The global imperative for sustainable resource management has elevated urban mining to a position of strategic importance in the contemporary materials economy. Unlike conventional mining operations that extract valuable elements from concentrated ore bodies typically containing 3-5% rare earth oxides, urban mining operations must collect dispersed materials across wide geographic areas where valuable elements exist in trace quantities [1]. This fundamental distinction creates unique technical and economic challenges that are intimately connected to the separation technologies employed, particularly solvent extraction (SX), which has emerged as the predominant method for rare earth element (REE) recovery from secondary sources.

Solvent extraction is a widely adopted separation technique in hydrometallurgy, particularly effective for the selective recovery of metals from complex aqueous solutions [2]. The technique exploits differences in the partitioning behavior of metal species between two immiscible phases—typically an organic extractant dissolved in a diluent and an aqueous feed solution containing the target metals. The efficiency and selectivity of this partitioning process are governed by partition coefficients, which quantify the distribution of metal species between the organic and aqueous phases at equilibrium.

### 1.2 Research Objective and Scope

This report addresses the central research question: Do partition coefficients in solvent extraction affect the economic feasibility of urban mining recovery? To answer this question comprehensively, we must examine the theoretical foundations of partition coefficients, their influence on process design and operational parameters, and their ultimate impact on the economic metrics that determine project viability. The analysis draws upon established principles of separation science and empirical evidence from urban mining applications, with particular emphasis on rare earth element recovery from electronic waste and other secondary resources.

The scope of this investigation encompasses the fundamental thermodynamic and kinetic factors governing partition coefficients, their mathematical representation and measurement, their role in determining separation efficiency, and the cascade of economic implications that arise from their values. By establishing these connections, this report provides a framework for understanding how optimization of partition coefficients can enhance the economic viability of urban mining operations.

## 2. Theoretical Framework: Partition Coefficients in Solvent Extraction

### 2.1 Fundamental Definitions and Principles

The partition coefficient, also known as the distribution ratio ($D$), represents the equilibrium ratio of the concentration of a solute in the organic phase to its concentration in the aqueous phase [3]. Mathematically, this relationship is expressed as:

$$D = \frac{[M]_{org}}{[M]_{aq}}$$

where $[M]_{org}$ denotes the concentration of metal $M$ in the organic phase and $[M]_{aq}$ represents its concentration in the aqueous phase at equilibrium. This parameter is fundamentally a thermodynamic quantity that reflects the relative affinity of the metal species for the organic extractant compared to the aqueous medium.

The distribution ratio is primarily dictated by the aqueous phase pH but also changes with REE concentrations in both the aqueous and organic phases [4]. This dependence creates a complex relationship between process conditions and partitioning behavior, requiring careful optimization of multiple parameters simultaneously. The pH dependence arises from the protonation equilibria of the extractant molecules and the hydrolysis equilibria of the metal ions, both of which influence the formation of extractable metal complexes.

For practical separation applications, the separation factor ($\beta$) provides a more relevant metric than the individual distribution ratios. The separation factor between two extracting species A and B is defined as the ratio of their distribution ratios:

$$\beta_{A/B} = \frac{D_A}{D_B}$$

This parameter serves as a measure of the relative selectivity that the ligand exhibits for extracting one species over another [5]. High separation factors indicate a higher degree of separation between the two species, which directly translates to more efficient separation processes. The separation factor is frequently used as the primary optimization target in solvent extraction circuit design because it captures the essential selectivity requirement for effective separation.

### 2.2 Thermodynamic and Kinetic Considerations

The partition coefficient is governed by the chemical affinity between the metal species and the extractant [6]. This affinity arises from the formation of coordination complexes between the metal ions and the extractant molecules, with the stability of these complexes determining the magnitude of the distribution ratio. For rare earth elements, the similar chemical properties make distinguishing and separating between them particularly challenging [7], which directly impacts the achievable separation factors.

The equilibrium constants represent the only model parameters that need to be experimentally determined to enable the simulation of a whole REE separation circuit [8]. These parameters are obtained from standard batch extraction tests conducted with separatory funnels, and robust estimation methods have been developed to estimate equilibrium constants from these tests. The relative amplitudes of these values are consistent with the separation factors provided in the literature despite the variability often observed in reported separation factors.

It is essential to recognize that distribution ratio and separation factor data are nothing more than ratios of equilibrium concentrations [9]. This mathematical nature has important practical implications: an extraction occurring at a high organic-to-aqueous (O/A) phase ratio may quantitatively extract a given species, but the value of the distribution ratio may appear low due to the dilution of the extracted species in the larger organic phase volume. Therefore, interpretation of partition coefficient data must account for the specific operating conditions under which they were measured.

### 2.3 Mathematical Modeling and Simulation

The majority of available solvent extraction models use experimentally obtained distribution data in combination with thermodynamic modeling to predict distribution coefficients for solute partitioning [10]. One primary drawback to these models is that they are based on steady-state material balances and therefore are only capable of predicting the steady-state concentration profiles for given operating conditions.

The general chemical engineering mathematical approach to conceive a solvent extraction plant has historically been based on the McCabe-Thiele diagram, an approach that is not adapted to multiple element extraction as is the case of REE separation [11]. The first publications to have proposed a mathematical method to simulate REE separation date back to the 1980s, and most documented simulation methods use separation factors as the model parameters for the simulation.

Empirical correlations for the distribution ratio are utilized in models to allow it to change as feed concentration changes, effectively changing the distribution ratio over time during the approach to steady state [12]. This dynamic behavior must be accounted for in process design to ensure that the actual operating conditions will achieve the expected separation performance.

## 3. Impact of Partition Coefficients on Process Design and Efficiency

### 3.1 Number of Extraction Stages and Circuit Complexity

The magnitude of partition coefficients directly determines the number of extraction stages required to achieve a target recovery or separation efficiency. In counter-current extraction systems, higher distribution ratios generally enable fewer stages to achieve the same degree of extraction, while lower distribution ratios necessitate additional stages or higher phase ratios to achieve comparable recovery.

For scandium recovery from uranium ores, the observed order of recovery was Th > Ti > Zr > Hf > Sc > U > Sc, which resulted in the separation of scandium from Th, Ti, Zr, and Hf after 3–15 steps of counter-current back extraction [13]. The most significant drawback of this procedure is the extensive use of HF acids, which poses a threat to the environment. This example illustrates how unfavorable partition coefficients between similar elements necessitate multiple separation stages, increasing both capital and operational costs.

In the second circuit for scandium refinement, the obtained concentration of scandium was refined to high purity of 99.9% using a counter-current circuit with three extraction stages and three rounds of scrubbing [14]. Scrubbing and stripping were carried out using two different solutions containing 0.35 mol/L and 1 mol/L of HCl, respectively. This example demonstrates that favorable partition coefficients can enable high-purity recovery with a relatively small number of stages, reducing equipment requirements and operational complexity.

### 3.2 Selectivity and Separation Efficiency

The separation factor between target metals and impurities is a critical determinant of product purity and recovery efficiency. High separation factors enable cleaner separations with fewer stages and lower impurity carryover, while low separation factors result in impure products that require additional purification steps or result in yield losses.

The mixture of 10% P204 and 5% TBP in kerosene achieved extraction efficiency of scandium approximately 99% [15]. This high efficiency is attributed to favorable partition coefficients and good selectivity of the extractant system. The ability to achieve near-quantitative extraction in a single stage or limited stages significantly reduces the capital and operating costs compared to systems requiring multiple extraction passes.

Solvent extraction facilitates the achievement of elevated purity in rare earth fractions [16]. The method's implementation enables the production of high-purity products that meet stringent specification requirements for advanced applications. However, to acquire high-purity scandium products, precise flow-chart procedures must be used, increasing the cost of both capital and operational equipment [17]. This underscores the trade-off between product purity requirements and economic feasibility.

### 3.3 Reagent Consumption and Operating Costs

The partition coefficient directly influences reagent consumption in solvent extraction circuits. Higher distribution ratios generally require lower extractant concentrations to achieve target loadings, reducing the cost of extractant makeup and losses. Conversely, systems with low distribution ratios may require higher extractant concentrations or larger organic phase volumes, increasing both capital and operating costs.

The distribution ratio is primarily dictated by the aqueous phase pH but also changes with REE concentrations in the aqueous and organic phases [18]. This relationship necessitates careful control of process conditions to maintain optimal partitioning behavior throughout the extraction circuit. The strong dependence on pH requires an acid material balance to be maintained, which adds complexity to process control and increases chemical consumption.

Compared with the primary extraction of REEs from ores, the recovery of REEs via technospheric or urban mining has the advantage that there are no thorium issues and that the composition of the obtained REE concentrate is less complex [19]. This compositional advantage can translate to more favorable partition coefficients and reduced separation challenges, potentially lowering processing costs compared to primary ore processing.

## 4. Economic Implications of Partition Coefficients in Urban Mining

### 4.1 Capital Expenditure Considerations

The capital investment required for urban mining facilities encompasses substantial upfront investments across multiple specialized systems [20]. The number and complexity of these systems are directly influenced by the partition coefficients of the target metals in the chosen extraction system. Favorable partition coefficients enable simpler process flowsheets with fewer extraction stages, smaller equipment sizes, and reduced auxiliary systems, resulting in lower capital expenditure requirements.

One can anticipate that the effort and financial investment for the piloting of a circuit consisting of 1000 units may rapidly discourage motivated REE orebody promoters [21]. This difficulty to pilot REE-SX separation circuits justifies the use of mathematical simulation to design a separation plant. The simulation approach allows optimization of process conditions to maximize partition coefficients and minimize equipment requirements, thereby reducing capital costs.

The fundamental economics of urban mining differ dramatically from conventional mining operations [22]. Unlike primary producers with concentrated ore bodies, urban mining operations must process materials where valuable elements exist in trace quantities. This reality places even greater importance on achieving favorable partition coefficients to ensure that the recovery process remains economically viable despite the low feed grades.

### 4.2 Operational Expenditure and Process Efficiency

Operational costs in solvent extraction circuits are dominated by reagent consumption, energy requirements, and labor costs. Partition coefficients influence all three of these cost components through their effects on process efficiency and equipment sizing.

Solvent extraction offers high selectivity, efficiency, and scalability, making it a crucial component of sustainable and economically viable metal recovery strategies in urban mining [23]. The efficiency gains achievable with favorable partition coefficients directly translate to reduced reagent consumption, lower energy requirements for mixing and phase separation, and decreased labor requirements for process monitoring and control.

The integration of solvent extraction in urban mining not only enhances the efficiency of metal recovery but also significantly contributes to environmental protection and economic sustainability [24]. Compared to traditional mining and smelting practices, this method offers a cleaner, more targeted, and resource-efficient approach to managing the growing burden of electronic waste. The environmental benefits translate to economic benefits through reduced waste treatment costs, lower regulatory compliance costs, and improved community relations.

### 4.3 Recovery Yields and Revenue Generation

The ultimate economic viability of urban mining operations depends on the recovery yields achieved for valuable metals. Partition coefficients directly determine the maximum achievable recovery for a given number of extraction stages and phase ratio. Higher distribution ratios enable higher recoveries for a given equipment configuration, while lower distribution ratios result in metal losses to the raffinate stream.

For instance, a study on the extraction of REEs from NdFeB magnets found that increasing the pressure from 15 MPa to 25 MPa at a constant temperature of 60°C enhanced the extraction efficiency from 70% to 95% [25]. While this example relates to supercritical fluid extraction rather than conventional solvent extraction, the principle is analogous: optimization of process conditions to improve partition coefficients directly enhances recovery yields and economic returns.

The economic potential of urban mining is substantial—one ton of mobile phone circuit boards may contain more gold than a ton of gold ore [26]. Solvent extraction allows for the recovery of these high-value elements at a fraction of the cost of traditional mining. However, realizing this potential requires extractant systems with favorable partition coefficients that enable efficient recovery from the complex matrices present in electronic waste.

### 4.4 Product Purity and Market Value

The purity of recovered products directly impacts their market value and, consequently, the economic viability of urban mining operations. Partition coefficients determine the selectivity of the separation process and therefore the achievable product purity. High separation factors between the target metal and impurities enable production of high-purity products that command premium prices in the market.

Since scandium and other REEs have chemical properties that are very similar, it is difficult to distinguish and separate between them [27]. This similarity necessitates extractant systems with carefully optimized partition coefficients to achieve the selectivity required for high-purity product recovery. The additional processing steps required to achieve high purity increase operational costs, but the premium prices for high-purity products often justify these additional expenses.

High-purity Sc can be prepared by multi-step counter current extractive treatment of Sc concentrate with TIAP (tri-iso-amyl phosphate) [28]. This example demonstrates that achieving high product purity requires multiple separation stages, with the number of stages determined by the separation factors achievable with the extractant system. Extractant systems with higher selectivity (higher separation factors) can achieve the same purity target with fewer stages, reducing processing costs.

## 5. Challenges and Optimization Strategies

### 5.1 Technical Challenges in Urban Mining

Despite its potential, the variability observed in recovery rates underscores significant technical and logistical challenges in urban mining [29]. These challenges include optimizing pre-processing techniques, improving collection and sorting systems, and advancing recycling technologies to enhance efficiency and minimize material losses. The partition coefficients achievable in solvent extraction systems are influenced by the composition of the feed solution, which in turn depends on the effectiveness of pre-processing and leaching operations.

Existing recycling infrastructure optimizes for bulk materials like steel, aluminum, and copper that comprise 80% of electronic waste by mass, while critical elements representing less than 1% by mass receive minimal attention despite their strategic importance [30]. This design mismatch explains why global rare earth recycling rates remain below 1% despite growing awareness of supply chain vulnerabilities. Addressing this mismatch requires development of solvent extraction systems with partition coefficients optimized for the low concentrations and complex matrices characteristic of urban mining feeds.

Collection systems compound this problem by capturing only 22.8% of available electronic devices globally [31]. The limited availability of feed material constrains the scale of urban mining operations and makes it difficult to achieve the economies of scale that would improve economic viability. For urban mining to become economically competitive, processes must be designed to achieve acceptable returns at the scales enabled by available feed material, which places additional importance on process efficiency as determined by partition coefficients.

### 5.2 Optimization of Partition Coefficients

Advances in extractant chemistry have enabled development of systems with improved partition coefficients for specific metal separations. The addition of tri-n-butyl phosphate (TBP) as a co-solvent improved the extraction of REEs from fluorescent lamp phosphors, achieving recovery rates of up to 98% [32]. This example demonstrates how extractant optimization can significantly improve partition coefficients and, consequently, process efficiency and economics.

The optimization of process parameters, such as pressure, temperature, and extraction time, is crucial for achieving high REE recovery rates and purity [33]. For solvent extraction systems, analogous parameters include extractant concentration, diluent composition, phase ratio, pH, and temperature. Optimization of these parameters to maximize partition coefficients and separation factors is essential for achieving economically viable recovery rates.

Despite the promising potential of solvent extraction for REE recovery from e-waste, challenges remain in terms of process optimization and scaling up for industrial applications [34]. Future research should focus on investigating the extraction mechanisms, developing novel co-solvents and chelating agents, and designing continuous-flow solvent extraction systems for large-scale REE recovery from various e-waste streams.

### 5.3 Integration with Circular Economy Principles

Urban mining is closely related to circular economy principles and plays a crucial role in efficient waste management and resource conservation [35]. By enabling the reuse of metals, solvent extraction supports the circular economy model—recovered metals can re-enter the manufacturing cycle, reducing the demand for virgin ore extraction and associated ecological damage. The economic viability of urban mining is therefore not only a matter of direct profitability but also of broader societal benefits that may be captured through policy mechanisms.

The balance problem explains why even for countries with large primary rare-earth resources, such as China, recycling of REEs is becoming an issue [36]. Mining of REE ores for specific elements like neodymium also produces large amounts of other lanthanides that need to be sold. Recycling of neodymium means that less REE ores need to be mined to meet the global demand for this metal. Urban mining can help address this balance problem by providing sources of specific REEs without the co-production of unwanted elements.

The integrated implementation of measures to enhance the efficiency of REE recovery will contribute to reducing environmental impacts and ultimately promoting the sustainable utilization of REEs from e-waste [37]. By improving partition coefficients and process efficiency, urban mining operations can achieve the economic viability necessary to scale up and contribute meaningfully to circular economy objectives.

## 6. Case Studies and Practical Applications

### 6.1 Scandium Recovery from Secondary Sources

The recovery of scandium from secondary sources provides an instructive case study for examining the relationship between partition coefficients and economic feasibility. Scandium is less common than lanthanum or cerium, and its recovery from primary ores is often economically challenging due to low concentrations and complex processing requirements [38]. Urban mining of scandium from secondary sources may offer economic advantages if suitable extraction technologies can be developed.

High-purity Sc can be prepared by multi-step counter current extractive treatment of Sc concentrate with TIAP [39]. The extraction of Sc from acidic solutions using organo-phosphoric acid reagents was selective [40]. These examples demonstrate that extractant systems with appropriate partition coefficients can enable efficient scandium recovery, though the multi-step nature of the process increases costs.

For the time being, China is the world's leading exporter of rare earths, and some scandium is recovered during the rare earth-processing process [41]. This co-production model benefits from favorable partition coefficients that enable simultaneous recovery of multiple REEs, spreading the processing costs across multiple product streams and improving overall economics.

### 6.2 Rare Earth Magnet Recycling

Rare earth magnets, particularly those based on neodymium-iron-boron (NdFeB) and samarium-cobalt (SmCo) alloys, represent a significant target for urban mining due to their high REE content and growing end-of-life volumes. The recovery of REEs via urban mining has the advantage that the composition of the obtained REE concentrate is less complex compared to primary ore processing [42].

Compared with primary extraction of REEs from ores, the recovery of REEs via technospheric or urban mining has the advantage that there are no thorium issues [43]. This eliminates the need for thorium separation and associated processing steps, simplifying the solvent extraction circuit and reducing costs. The simplified composition of urban mining feeds may also result in more favorable partition coefficients by reducing competition from matrix elements.

The other, less prevalent type of rare earth magnets are based upon samarium-cobalt alloys, which possess a high coercivity, good corrosion resistance, and excellent thermal stability [44]. These magnets may contain admixtures of different transition metals, such as Fe, Zr, and Cu. The presence of these transition metals necessitates extractant systems with sufficient selectivity to achieve high-purity REE recovery, highlighting the importance of partition coefficient optimization.

### 6.3 Electronic Waste Processing

Electronic waste represents a growing urban mining target due to its high content of valuable metals and increasing generation rates. Currently, less than 5% of rare earth elements are recovered from e-waste globally, and the EU's ambitious target of 50% recovery of critical metals highlights the need for improved recovery technologies [45].

In the context of e-waste recycling, solvent extraction plays a crucial role in isolating target metals from complex mixtures [46]. The partition coefficients of REEs in solvent extraction systems determine the efficiency with which these metals can be separated from the complex matrix of electronic waste. Optimization of partition coefficients is essential for achieving the recovery rates necessary to make urban mining economically viable.

By extracting valuable metals from discarded electronics, solvent extraction minimizes the volume of waste destined for landfills and incineration [47]. This directly reduces the risk of leaching heavy metals such as lead, mercury, and cadmium into soil and groundwater. The environmental benefits of urban mining complement the economic benefits by reducing external costs associated with waste disposal and primary resource extraction.

## 7. Conclusions and Future Perspectives

### 7.1 Summary of Findings

This analysis has demonstrated that partition coefficients in solvent extraction exert a profound influence on the economic feasibility of urban mining recovery operations. The key findings can be summarized as follows:

First, partition coefficients directly determine the number of extraction stages required to achieve target recovery and purity levels. Higher distribution ratios and separation factors enable simpler process flowsheets with fewer stages, reducing both capital and operational expenditure requirements. The relationship between partition coefficients and stage requirements is fundamental to process design and has cascading effects on all aspects of economic viability.

Second, the selectivity achievable in solvent extraction circuits, as quantified by separation factors, directly impacts product purity and yield. High separation factors enable production of high-purity products that command premium prices while minimizing yield losses to impurity streams. The economic value captured from product sales depends critically on the partition coefficients of the extraction system.

Third, reagent consumption and operating costs are strongly influenced by partition coefficients. Systems with favorable partitioning behavior require lower extractant concentrations and smaller phase ratios to achieve target loadings, reducing chemical costs and waste generation. The ongoing costs of operation are a primary determinant of project economics and are directly linked to partition coefficient optimization.

Fourth, the complexity of urban mining feeds, with their low concentrations of target metals and complex matrices, places particular importance on achieving favorable partition coefficients. Unlike primary ore processing, where high feed grades can compensate for suboptimal separation efficiency, urban mining requires highly efficient extraction to achieve acceptable economics.

### 7.2 Implications for Practice

The findings of this analysis have several important implications for practitioners in the urban mining field. Process design should begin with careful characterization of partition coefficients for the specific feed materials and extractant systems under consideration. The investment in thorough characterization pays dividends through optimized process design and reduced operational costs.

Extractant selection should prioritize systems with high selectivity (separation factors) for the target metals over impurities, even if this requires trade-offs in distribution ratio. The ability to achieve high purity with fewer stages often provides greater economic benefit than high distribution ratios that require complex multi-stage circuits.

Process optimization should focus on maximizing partition coefficients through careful control of pH, temperature, extractant concentration, and phase ratio. The strong dependence of partition coefficients on these parameters creates opportunities for optimization that can significantly improve process economics.

### 7.3 Future Research Directions

Future research should focus on developing novel extractant systems with improved partition coefficients for urban mining applications. The unique characteristics of urban mining feeds—low metal concentrations, complex matrices, and variable composition—require extractant systems specifically designed for these challenges.

Mathematical modeling and simulation capabilities should be enhanced to better predict partition coefficient behavior under the dynamic conditions encountered in urban mining operations. Current models based on steady-state material balances may not adequately capture the transient behavior that occurs during start-up, shutdown, and feed composition variations.

Integration of solvent extraction with upstream and downstream processes should be optimized to maximize overall process efficiency. The partition coefficients achievable in solvent extraction are influenced by feed composition, which depends on the effectiveness of pre-processing and leaching operations.

Finally, life cycle assessment and economic analysis should be integrated with technical optimization to ensure that improvements in partition coefficients translate to genuine improvements in sustainability and economic viability. The ultimate goal is to develop urban mining processes that are both economically competitive and environmentally sustainable.

## References

[1] Discovery Alert. "Urban Mining Challenges: Separation Technologies 2025." 2025.

[2] Online Scientifics Research. "Revolutionizing Urban Mining: Solvent Extraction for Sustainable Metal Recovery from Electronic Waste." 2024.

[3] University of Idaho. "Mathematical Model for Solvent Extraction." ETD Document.

[4] PMC. "Solvent Extraction of Scandium and Rare Earth Elements." PMC8999471.

[5] University of Idaho. "Separation Factor Definition." ETD Document.

[6] Online Scientifics Research. "Partition Coefficients and Distribution Ratios." 2024.

[7] PMC. "Challenges in REE Separation Due to Similar Chemical Properties." PMC8999471.

[8] MDPI. "Equilibrium Constants for REE Separation." Processes, 2024.

[9] University of Idaho. "Interpretation of Distribution Ratio Data." ETD Document.

[10] University of Idaho. "Solvent Extraction Modeling Approaches." ETD Document.

[11] MDPI. "McCabe-Thiele Method Limitations for REE Separation." Processes, 2024.

[12] University of Idaho. "Dynamic Distribution Ratio Correlations." ETD Document.

[13] PMC. "Scandium Recovery from Uranium Ores: Multi-step Extraction." PMC8999471.

[14] PMC. "High-Purity Scandium Refinement Circuit." PMC8999471.

[15] PMC. "P204 and TBP Extraction Efficiency for Scandium." PMC8999471.

[16] University of Saskatchewan. "Superior Purity Levels in SX." Harvest Repository.

[17] PMC. "Cost Implications of Precise Flow-Chart Procedures." PMC8999471.

[18] PMC. "pH Dependence of Distribution Ratios." PMC8999471.

[19] Solvomet. "REE Recovery via Urban Mining: Advantages." JCLEPRO Publication.

[20] Discovery Alert. "Capital Investment in Urban Mining Facilities." 2025.

[21] MDPI. "Pilot Plant Challenges for REE-SX Circuits." Processes, 2024.

[22] Discovery Alert. "Fundamental Economics of Urban Mining." 2025.

[23] Online Scientifics Research. "Solvent Extraction for Sustainable Urban Mining." 2024.

[24] Online Scientifics Research. "Environmental and Economic Impacts of SX." 2024.

[25] PMC. "Pressure Effects on REE Extraction Efficiency." PMC11477848.

[26] Online Scientifics Research. "Economic Potential of Urban Mining." 2024.

[27] PMC. "Chemical Similarity Challenges in REE Separation." PMC8999471.

[28] PMC. "TIAP for High-Purity Scandium Preparation." PMC8999471.

[29] SDEWES. "Technical Challenges in Urban Mining." JSDNAREMA.

[30] Discovery Alert. "Recycling Infrastructure Limitations." 2025.

[31] Discovery Alert. "Global E-Waste Collection Rates." 2025.

[32] PMC. "TBP Co-Solvent for REE Extraction." PMC11477848.

[33] PMC. "Process Parameter Optimization for REE Recovery." PMC11477848.

[34] PMC. "Future Research Directions for SFE." PMC11477848.

[35] SDEWES. "Urban Mining and Circular Economy Principles." JSDNAREMA.

[36] Solvomet. "REE Balance Problem and Recycling." JCLEPRO Publication.

[37] PMC. "Integrated Implementation for Sustainable REE Recovery." PMC11477848.

[38] Solvomet. "Scandium Rarity and Recovery Challenges." JCLEPRO Publication.

[39] PMC. "Multi-Step TIAP Extraction for Scandium." PMC8999471.

[40] PMC. "Organo-Phosphoric Acid Reagents for Sc Extraction." PMC8999471.

[41] PMC. "China's Role in Scandium Recovery." PMC8999471.

[42] Solvomet. "Advantages of Urban Mining for REE Recovery." JCLEPRO Publication.

[43] Solvomet. "Thorium-Free Urban Mining Advantage." JCLEPRO Publication.

[44] Solvomet. "Samarium-Cobalt Magnet Characteristics." JCLEPRO Publication.

[45] Core Consultants Group. "Global REE Recovery Rates from E-Waste." 2024.

[46] Online Scientifics Research. "Solvent Extraction in E-Waste Recycling." 2024.

[47] Online Scientifics Research. "Environmental Benefits of Urban Mining." 2024.

## Annotations


## Sources
[1] https://discoveryalert.com.au/urban-mining-2025-materials-recovery-challenges/
[2] https://discoveryalert.com.au/urban-mining-challenges-separation-technologies-2025/
[3] https://harvest.usask.ca/server/api/core/bitstreams/be39f663-7c89-4a16-8781-4853a601a783/content
[4] https://netl.doe.gov/sites/default/files/2019-05/2019_Annual_Reports/Wednesday/REE/7%20-%2020190410_0100C_FE0031526_NETL.pdf
[5] https://objects.lib.uidaho.edu/etd/pdf/Lyon_idaho_0089N_10815.pdf
[6] https://pmc.ncbi.nlm.nih.gov/articles/PMC11477848/
[7] https://pmc.ncbi.nlm.nih.gov/articles/PMC8999471/
[8] https://pubs.acs.org/doi/full/10.1021/acsenvironau.5c00175
[9] https://soar.wichita.edu/server/api/core/bitstreams/70402035-3552-4aa3-afb2-c630f9d5b4c7/content
[10] https://solvomet.eu/wp-content/uploads/2017/05/JCLEPRO_Binnemans_REE_Recycling_May2013.pdf
[11] https://www.coreconsultantsgroup.com/the-future-of-urban-mining-extracting-rare-earths-and-critical-metals-from-e-waste/
[12] https://www.epa.gov/sites/default/files/2015-05/documents/402-r-99-004a.pdf
[13] https://www.iosrjournals.org/iosr-jbb/papers/Volume%2011,%20Issue%204/Ser-1/H1104016169.pdf
[14] https://www.mdpi.com/2075-163X/13/6/714
[15] https://www.mdpi.com/2076-3417/15/20/10949
[16] https://www.mdpi.com/2227-9717/12/6/1235
[17] https://www.mdpi.com/2297-8739/12/2/52
[18] https://www.nanosteelco.com/top-10-recent-advances-in-rare-earth-metal-processing-you-should-know/
[19] https://www.onlinescientificsresearch.com/articles/revolutionizing-urban-mining-solvent-extraction-for-sustainable--metal-recovery-from-electronic-waste.pdf
[20] https://www.osti.gov/servlets/purl/2583807
[21] https://www.sciencedirect.com/science/article/abs/pii/S1226086X2400282X
[22] https://www.sciencedirect.com/science/article/abs/pii/S2213343725056544
[23] https://www.sciencedirect.com/science/article/am/pii/S1364032121002100
[24] https://www.sciencedirect.com/science/article/pii/S0892687513003452
[25] https://www.sciencedirect.com/science/article/pii/S1618866724000608
[26] https://www.sciencedirect.com/science/article/pii/S2213343724008996
[27] https://www.sciencedirect.com/science/article/pii/S2589004221003424
[28] https://www.sdewes.org/jsdnarema/pid1.0551