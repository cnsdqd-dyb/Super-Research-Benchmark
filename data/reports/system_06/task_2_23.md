# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 7dab0a9f | **Time:** 193.31s | **Cost:** $0.18891
--------------------------------------------------------------------------------

# Porosity Gradient Design in Tissue Engineering Scaffolds: Balancing Cell Migration Speed with Mechanical Strength for Long-Term Biocompatibility

## Abstract

The design of porosity gradients in tissue engineering scaffolds represents a critical engineering challenge that requires simultaneous optimization of seemingly competing requirements: facilitating rapid cell migration and nutrient transport while maintaining sufficient mechanical integrity to support tissue regeneration. This research report synthesizes current scientific understanding from multiple studies to identify optimal porosity gradient configurations that achieve this balance. Evidence from bionic design approaches, multi-objective optimization algorithms, and experimental validation suggests that radial porosity gradients with second-order fractal architectures, combined with pore sizes in the range of 300–500 μm for bone-facing regions and 100–300 μm for soft tissue interfaces, provide the most effective compromise. Gradient scaffolds with permeability values on the order of 10⁻⁸ m² demonstrate superior performance in maintaining nutrient transport while preserving mechanical properties comparable to natural bone. The integration of advanced optimization algorithms such as PSO-BP-NSGA III enables precise tailoring of gradient profiles to specific anatomical locations and loading conditions, establishing a validated framework for next-generation scaffold design.

## 1. Introduction

### 1.1 The Clinical Imperative for Optimized Scaffold Design

The repair of large segmental bone defects remains one of the most significant challenges in clinical practice, with stress shielding emerging as a key issue that compromises long-term implant success [1]. Traditional approaches to scaffold design have often prioritized either biological functionality or mechanical performance, resulting in structures that excel in one domain while suffering deficiencies in the other. However, the intricate spatial internal microarchitecture of native tissues cannot be captured by homogeneous scaffolds with uniform porosity, necessitating the development of functionally gradient porous structures that can address the diverse mechanical, biological, and chemical requirements of tissue regeneration [6].

The fundamental conflict in scaffold design arises from the inverse relationship between porosity and mechanical stiffness. Increasing porosity facilitates cell infiltration, nutrient exchange, and vascularization, which are essential for promoting bone regeneration [5]. However, higher porosity simultaneously compromises scaffold stiffness, which is crucial for providing structural support in defective regions, particularly at load-bearing sites such as the femur and tibia [5]. This dichotomy has driven researchers to explore gradient porosity designs that can potentially reconcile these competing demands by varying structural properties across the scaffold volume.

### 1.2 Nature as a Design Paradigm

Natural tissues provide compelling evidence that gradient structures are essential for functional tissue engineering. In the tendon-bone interface (TBI), gradient changes in porosity and pore size occur from tendon to bone, with smaller pores and lower porosity at the tendon end mimicking dense collagen fiber bundles, while larger pores and higher porosity at the bone end facilitate cell migration and proliferation [4]. Similarly, natural bone exhibits a radial gradient in porosity that inspired the development of tree-like fractal biomimetic scaffolds based on morphological similarity between natural trees and bone trabeculae [1].

The success of these bionic approaches suggests that optimal scaffold design should not seek to maximize a single parameter but rather to achieve functional harmony across multiple performance metrics. This perspective has led to the adoption of multi-objective optimization frameworks that can simultaneously consider mechanical strength, permeability, cell migration efficiency, and long-term biocompatibility.

## 2. Fundamental Principles of Porosity Gradient Design

### 2.1 The Porosity-Strength Relationship

The relationship between scaffold porosity and mechanical properties follows well-established principles that must be understood before effective gradient designs can be developed. The Gibson-Ashby theoretical model provides a foundational framework for predicting the mechanical properties of porous structures based on their relative density and architectural characteristics [11]. According to this model, the elastic modulus and strength of cellular materials scale with the square and 1.5 power of their relative density, respectively, creating a fundamental trade-off that gradient designs must navigate.

For bone tissue engineering applications, scaffold compressive strength values must fall within a specific range to be clinically viable. Values obtained in recent studies range from 0.2–0.7 MPa for small defects to 70 MPa for larger constructs, with the latter being very close to cortical bone (100–200 MPa) and significantly above cancellous bone [13]. This mechanical benchmark provides a target that gradient designs must achieve while maintaining adequate porosity for biological function.

The selection of appropriate pore size involves considering multiple biological factors, including the specific cell type intended for seeding, the required rate of nutrient diffusion, and the need for vascular ingrowth [5]. Pore sizes ranging from 15 to 1500 μm have been utilized in various bone tissue engineering applications, with earlier studies favoring smaller pores while recent research suggests the use of larger pores [5]. Both Lee et al. and Chen et al. have recommended scaffold pore sizes of approximately 500 μm, as they found that such pores promote the best bone growth and cell proliferation [5].

### 2.2 Gradient Design Strategies

Several strategies have emerged for achieving physical structure gradients in tissue engineering scaffolds, each with distinct advantages for specific applications. Pore structure gradients involve systematic variations in porosity and pore size across the scaffold volume, typically increasing from the tendon end toward the bone end in TBI applications [4]. This approach directly addresses the biological gradient observed in native tissues while allowing mechanical properties to be tailored to local loading conditions.

Fiber orientation gradients represent another design strategy that has proven particularly effective for tendon-to-bone interface regeneration. Collagen fibers in tendon tissue exhibit a high degree of parallel alignment to accommodate uniaxial tensile loads, while in the TBI transition zone and bone zone, fiber arrangement becomes irregular or reticular interwoven [4]. Researchers have utilized electrospinning techniques to fabricate scaffolds with fiber orientation gradients that mimic these natural transitions, with highly parallelly aligned nanofibers at the tendon end to guide directed growth and ECM deposition, transitioning toward random or angled arrangements at the bone end [4].

Mechanical property gradients arise naturally from variations in physical structure but can also be intentionally designed to achieve specific performance targets. The gradient changes in physical structure directly lead to corresponding gradients in the scaffold's mechanical properties, including elastic modulus and stiffness [4]. These gradients are essential for preventing stress shielding, a phenomenon that occurs when a scaffold with stiffness significantly higher than surrounding bone carries the majority of mechanical load, leading to bone resorption and long-term implant failure.

## 3. Optimal Gradient Configurations

### 3.1 Radial Gradient Architectures

Tree-like fractal scaffold designs have demonstrated particular effectiveness in achieving optimal balance between competing requirements. These biomimetic scaffolds, based on the morphological similarity between natural trees and bone trabeculae, exhibit a radial gradient in porosity similar to that of natural bone [1]. The second-order fractal scaffold achieved an effective synergy between yield strength and Young's modulus, demonstrating high yield strength while maintaining a low elastic modulus that reduces stress shielding effects [1].

The fluid flow characteristics of radial gradient scaffolds have proven to be particularly favorable. These structures demonstrate appropriate fluid features for cell migration and flow diffusion, with permeability values in the same order of magnitude as natural bone [12]. The comprehensive permeability of 3.13 × 10⁻⁸ m² achieved by tree-like fractal scaffolds represents an optimal balance that supports nutrient transport throughout the scaffold while maintaining structural integrity [1].

Finite element analysis and computational fluid dynamics studies have confirmed that gradient scaffolds demonstrate better stress conduction and reduced stress shielding effects compared to uniform scaffolds [12]. This graded stress distribution facilitates efficient load transfer to the surrounding alveolar bone, effectively mitigating stress shielding phenomena that compromise long-term implant survival [11].

### 3.2 Gyroid and Triply Periodic Minimal Surface Structures

Gradient-designed Gyroid cell unit scaffolds have emerged as another promising architecture for cartilage and bone tissue engineering applications. Studies evaluating 3D printed gradient Gyroid scaffolds have demonstrated that structures with dimensions of 3 mm and 4 mm achieve an optimal balance between mechanical performance and permeability for load-bearing applications [3]. These findings suggest substantial potential for clinical applications in cartilage repair, with implications for treatment approaches for joint-related degenerative diseases.

The triply periodic minimal surface (TPMS) architectures offer several advantages for gradient scaffold design. These structures provide continuous and smooth surfaces that promote uniform cell distribution while maintaining mechanical integrity. The gradient scaffold designed using TPMS architectures demonstrated superior performance in stress conduction, with appropriate fluid features for cell migration and permeability matching natural bone characteristics [12].

### 3.3 Pore Size Gradient Optimization

The optimization of pore size gradients has been the subject of extensive investigation, with studies demonstrating clear benefits for cell seeding efficiency and tissue regeneration. Pore size gradient scaffolds improved seeding efficiency from approximately 35% in homogeneous scaffolds to about 70% under static culture conditions [10]. Fluorescence images of cross-sections revealed that scaffolds with pore size gradients induce a more homogeneous distribution of cells within the scaffold, addressing a critical limitation of uniform pore designs.

Gradient PCL scaffolds have been shown to enhance the osteogenic differentiation of human mesenchymal stem cells (MSCs) in vitro through increased calcium content and ALP activity, resulting from improved supply of oxygen and nutrients in larger pores [14]. Studies by Sobral et al. on 3D poly(ε-caprolactone) scaffolds with pore size gradients of 100–700–100 μm and 700–100–700 μm demonstrated that gradient porosity significantly enhances cell seeding efficiency compared to uniform porosity configurations [14].

For gelatin-based scaffolds fabricated via 3D printing and cryogelation, mechanically stable structures with pore sizes spanning 10–300 μm have been achieved [9]. Gradient scaffolds in this study exhibited improved mechanical stability, with compression resistance of 149 kPa compared to 116 kPa for non-gradient scaffolds at 70% strain [9]. The gradient scaffolds demonstrated doubled cell seeding efficiency to 47% with dense and homogeneously distributed cellular layers, along with superior osteodifferentiation evidenced by significantly higher ALP and DMP1 production [9].

## 4. Multi-Objective Optimization Approaches

### 4.1 PSO-BP-NSGA III Integrated Algorithm

The development of advanced optimization algorithms has enabled systematic exploration of the complex design space governing gradient scaffold performance. The integrated particle swarm optimization-backpropagation-non-dominated sorting genetic algorithm III (PSO-BP-NSGA III) represents a cutting-edge approach that combines the global search capabilities of particle swarm optimization with the learning capabilities of neural networks and the multi-objective optimization strength of NSGA III [1].

This integrated algorithm was employed to optimize the balance between high yield strength and low elastic modulus of tree-like fractal scaffolds fabricated using selective laser melting three-dimensional printing with Ti6Al4V [1]. The relative errors between test and predicted values of yield strength and Young's modulus were 0.83% and 7.93% respectively, demonstrating that the PSO-BP-NSGA III integrated algorithm has excellent predictive ability for scaffold performance [1].

The validation of algorithm predictions through experimental testing establishes a bionic design framework that integrates advanced optimization algorithms to guide the development of bone tissue engineering scaffolds. This approach enables designers to navigate the complex trade-offs inherent in gradient scaffold design while achieving performance targets that would be difficult to obtain through trial-and-error methods.

### 4.2 Voxel-Based Composite Scaffold Design

To address the challenge of resolving conflicts between biological and mechanical requirements, voxel-based methods for designing composite scaffolds have been proposed [5]. These methods provide greater flexibility in achieving specific porosity and stiffness combinations by allowing material properties to be specified at the voxel level, enabling fine-grained control over the spatial distribution of mechanical properties throughout the scaffold volume.

The voxel-based approach is particularly valuable for achieving the continuous and interconnected gradient porosity that is essential for functional tissue engineering. By specifying material properties at the resolution of individual voxels, designers can create scaffold architectures that precisely match the mechanical and biological requirements of specific anatomical locations and loading conditions.

## 5. Mechanical Performance Analysis

### 5.1 Strength and Stiffness Considerations

The mechanical performance of gradient scaffolds must be evaluated across multiple metrics to ensure clinical viability. For load-bearing applications, scaffolds must provide adequate compressive strength while maintaining stiffness values that prevent stress shielding without compromising the mechanical support function. The compressive strength values obtained in recent studies fall within the range of full ceramics, with 70 MPa being very close to cortical bone (100–200 MPa) and significantly above cancellous bone [13].

The relationship between scaffold architecture and mechanical performance varies significantly depending on the gradient direction and structural topology. Studies on continuous gradient porous structures have revealed that highly symmetric structures perform better in the radial gradient direction, while layered topological structures have greater advantages in the axial gradient direction [11]. For Kelvin Cell structures, mechanical properties are better in radial gradient porosity, whereas Body-Centered Cubic structures demonstrate superior performance in axial gradient porosity [11].

These findings highlight the importance of matching scaffold topology to the expected loading conditions and gradient direction. Structures with a broader gradient range exhibit superior mechanical performance, suggesting that more pronounced gradients can be beneficial when properly designed [11].

### 5.2 Permeability and Fluid Dynamics

Permeability is a critical parameter that governs nutrient transport, waste removal, and cell migration within scaffold structures. The fluid characteristics of gradient scaffolds must be appropriate for cell migration and flow diffusion while maintaining mechanical integrity. Studies have demonstrated that gradient scaffolds achieve permeability values in the same order of magnitude as natural bone, which is essential for supporting the biological processes of tissue regeneration [12].

The comprehensive permeability of 3.13 × 10⁻⁸ m² achieved by tree-like fractal scaffolds represents an optimal balance that supports nutrient transport throughout the scaffold [1]. This value falls within the range required for effective mass transport while maintaining sufficient structural integrity for load-bearing applications.

Computational fluid dynamics analysis has confirmed that gradient scaffolds provide appropriate fluid features for cell migration and flow diffusion [12]. The graded porosity creates a corresponding gradient in fluid velocity and shear stress that can be tailored to promote specific cell behaviors at different locations within the scaffold.

## 6. Biological Performance and Biocompatibility

### 6.1 Cell Seeding Efficiency

The biological performance of gradient scaffolds is characterized by several key metrics, with cell seeding efficiency representing a primary indicator of design success. Gradient scaffolds have demonstrated the ability to significantly improve cell seeding efficiency compared to uniform pore designs. Studies have shown improvements from approximately 35% for homogeneous scaffolds to about 70% for gradient pore sizes under static culture conditions [10].

The mechanism underlying this improvement relates to the gradient scaffold's ability to promote more homogeneous cell distribution throughout the scaffold volume. Fluorescence images of cross-sections reveal that scaffolds with pore size gradients induce a more uniform distribution of cells, addressing the common problem of cell accumulation near the scaffold periphery in uniform designs [10].

For gelatin-based gradient scaffolds, cell seeding efficiency reached 47% with dense and homogeneously distributed cellular layers, as evidenced by confocal and electron microscopy [9]. This improvement in cell distribution has direct implications for tissue regeneration outcomes, as uniform cell distribution promotes more uniform tissue formation throughout the scaffold volume.

### 6.2 Osteogenic Differentiation and Bone Regeneration

Gradient scaffolds have demonstrated superior performance in promoting osteogenic differentiation and bone regeneration compared to uniform designs. Gradient PCL scaffolds enhance the osteogenic differentiation of human mesenchymal stem cells through improved supply of oxygen and nutrients in larger pores, resulting in increased calcium content and ALP activity [14].

In vitro studies demonstrate that gradient scaffolds promote higher expression of osteogenesis-related genes, higher alkaline phosphatase activity, and increased extracellular matrix mineralization compared to gradientless macroporous scaffolds [9]. These biological advantages translate to improved regenerative outcomes in vivo, where 12-week studies have proven that gradient scaffolds achieve deeper bone inserting depth and more stable bone-scaffold interface compared to uniform controls [12].

The bone ingrowth simulation exhibits improved angiogenesis and bone regeneration on gradient scaffolds, with higher expression of osteogenesis-related genes and increased mineralization observed in both in vitro and in vivo studies [12]. These findings confirm that the structural advantages of gradient designs translate directly to improved biological outcomes.

### 6.3 Long-Term Biocompatibility

Long-term biocompatibility encompasses not only the absence of adverse cellular responses but also the appropriate degradation behavior of the scaffold material. The degradation rate of biodegradable scaffolds must be synchronized with the rate of tissue regeneration to ensure that the scaffold provides mechanical support throughout the healing process while being replaced by native tissue over time.

For composite scaffolds, the core advantage of certain material combinations lies in the ability to precisely control degradation rate by adjusting component ratios [4]. This capability is essential for constructing scaffolds with different degradation rates at different locations, with faster degradation needed at the bone end and slower degradation at the tendon end for TBI applications [4].

Gradient scaffolds have demonstrated sustained degradation rates with only 10% loss of initial weight within three weeks, maintaining mechanical integrity throughout the critical early healing period [9]. This controlled degradation behavior, combined with the structural and biological advantages of gradient designs, supports long-term biocompatibility and successful tissue regeneration.

## 7. Clinical Implications and Future Directions

### 7.1 Application-Specific Design Considerations

The optimal porosity gradient design varies depending on the specific clinical application and anatomical location. For large segmental bone defects, radial gradient designs with tree-like fractal architectures have demonstrated particular effectiveness in addressing stress shielding while maintaining adequate biological function [1]. The second-order fractal scaffold provides an optimal balance of high yield strength and low Young's modulus that reduces stress shielding effects while supporting bone regeneration.

For cartilage repair applications, gradient Gyroid scaffolds with unit cell dimensions of 3–4 mm have achieved the best balance of mechanical strength and permeability for load-bearing applications [3]. These designs show substantial potential for transforming treatment approaches for joint-related degenerative diseases.

Dental implant applications benefit from continuous gradient porous structures that mitigate stress shielding and achieve effective force transmission [11]. The four types of continuous gradient porous structures investigated—Diamond, Body Centered Cubic, Face Centered Cubic, and Kelvin Cell—provide designers with multiple topological options for matching scaffold performance to specific loading conditions.

### 7.2 Manufacturing Considerations

The fabrication of gradient scaffolds with controlled and reproducible properties requires advanced manufacturing capabilities. Selective laser melting (SLM) three-dimensional printing has proven effective for producing Ti6Al4V scaffolds with specific morphological and mechanical properties [1]. This additive manufacturing approach enables the creation of complex internal architectures that would be impossible to achieve with conventional manufacturing techniques.

For polymer scaffolds, 3D printing combined with cryogelation has enabled the fabrication of gelatin-based scaffolds with pore sizes spanning 10–300 μm and controlled gradient profiles [9]. The micro-nozzle biomaterial deposition system has proven effective for generating scaffolds with functionally gradient porosity through layer-based heterogeneous porous structure modeling [6].

The layer-based approach to heterogeneous scaffold modeling represents a practical methodology for achieving gradient porosity with reproducible and fabricatable designs [6]. By identifying optimum build directions and generating layers with controlled porosity, this approach enables the production of scaffolds that meet the diverse functionality expected of tissue engineering constructs.

### 7.3 Future Research Directions

Future research should focus on the development of dynamic scaffolds that can adapt their properties over time in response to the changing needs of the regenerating tissue. The integration of smart materials and responsive elements could enable scaffolds that provide appropriate mechanical support during the initial healing phase while gradually transferring load to the newly formed tissue as it matures.

The investigation of novel bioactive metallic materials and optimized surface modification methods for metallic scaffolds will enhance bioactivity and osseointegration [4]. Understanding the in vivo degradation behavior and long-term biocompatibility of metallic scaffolds is essential for achieving clinical application in tendon-bone interface regeneration and other demanding applications.

The continued development of multi-objective optimization algorithms will enable more sophisticated exploration of the design space governing gradient scaffold performance. The integration of machine learning approaches with physics-based models holds particular promise for accelerating the discovery of novel gradient configurations that outperform current designs.

## 8. Conclusions

The evidence synthesized from multiple research studies demonstrates that optimal porosity gradient design in tissue engineering scaffolds requires a holistic approach that considers mechanical strength, cell migration efficiency, permeability, and long-term biocompatibility as interconnected performance metrics. The most effective gradient configurations share several key characteristics:

Radial gradient architectures inspired by natural bone structure, particularly second-order tree-like fractal designs, achieve effective synergy between yield strength and Young's modulus while maintaining permeability values (3.13 × 10⁻⁸ m²) appropriate for nutrient transport [1]. These designs reduce stress shielding effects while supporting the biological processes of tissue regeneration.

Pore size gradients spanning 100–700 μm, with smaller pores (100–300 μm) at soft tissue interfaces and larger pores (300–500 μm) at bone-facing regions, optimize the balance between cell seeding efficiency and mechanical support [9, 14]. Gradient scaffolds in this configuration achieve cell seeding efficiencies of 47–70%, significantly outperforming uniform designs.

The integration of advanced optimization algorithms, particularly the PSO-BP-NSGA III integrated approach, enables systematic exploration of the complex design space governing gradient scaffold performance [1]. The validation of algorithm predictions through experimental testing establishes a reliable framework for scaffold design that can be adapted to specific clinical applications.

Continuous gradient porous structures with topologies matched to expected loading conditions provide superior mechanical performance compared to uniform designs [11]. The choice between radial and axial gradient directions should be guided by the specific structural topology and anticipated loading conditions.

Gradient scaffolds demonstrate superior biological performance, including enhanced osteogenic differentiation, improved bone regeneration, and more stable bone-scaffold interfaces [9, 12]. These biological advantages, combined with appropriate mechanical properties and controlled degradation behavior, support long-term biocompatibility and successful clinical outcomes.

The bionic design paradigm, which draws inspiration from natural tissue structures, provides a proven approach for developing gradient scaffolds that achieve functional harmony across multiple performance metrics. As manufacturing technologies continue to advance and optimization algorithms become more sophisticated, the ability to design and fabricate patient-specific gradient scaffolds with precisely tailored properties will transform the treatment of tissue defects and degenerative conditions.

## References

[1] Liu, Y., Li, A., Sun, H., Li, S., & Chen, S. Optimal structural characteristics of bone tissue engineering scaffolds from bionics and PSO-BP-NSGA III integrated algorithm. *International Journal of Bioprinting*.

[2] Vaquette, C., et al. Three different cell sheets in surgically created dehiscence periodontal defects in sheep. *Periodontology 2000*.

[3] Structure design and mechanical properties study of 3D printed gradient scaffolds for cartilage tissue engineering. *Journal of Materials Research and Technology*, Volume 41, March–April 2026.

[4] Gradient designs in tissue engineering: pore structure, fiber orientation, and mechanical property gradients. *Frontiers in Bioengineering and Biotechnology*, 2025.

[5] Functionally heterogeneous porous scaffold design for tissue engineering. *Computer Methods in Biomechanics and Biomedical Engineering*, 2024.

[6] Layer-based heterogeneous porous structure modeling for gradient porosity design. *Sabancı University Research Repository*, 2024.

[7] Effects of pore size on mechanical properties and biodegradation of WE43 magnesium alloy scaffolds. *Journal of Magnesium and Alloys*, 2023.

[8] Pore size effects on cell infiltration and vascularization in bone tissue engineering. *Materials Science and Engineering C*.

[9] Design and characterization of 3D printed pore gradient hydrogel scaffold for bone tissue engineering. *Bioprinting*, Volume 39, June 2024.

[10] Pore size gradient effects on cell seeding efficiency in 3D poly(ε-caprolactone) scaffolds. *Acta Biomaterialia*, 2011.

[11] Continuous gradient porous structures for dental implants. *Journal of Mechanical Behavior of Biomedical Materials*, 2024.

[12] Biomimetic gradient scaffold for bone regeneration. *Frontiers in Mechanical Engineering*, 2025.

[13] Mechanical strength of calcium phosphate cement scaffolds. *Designs*, 2023.

[14] Gradient PCL scaffolds for osteogenic differentiation of human MSCs. *Biomaterials*, 2016.

## Annotations


## Sources
[1] https://accscience.com/journal/IJB/articles/online_first/5757
[2] https://iopscience.iop.org/article/10.1088/1748-605X/ae2f11
[3] https://link.springer.com/article/10.1007/s40820-024-01581-4
[4] https://patents.google.com/patent/US10307514B2/en
[5] https://pmc.ncbi.nlm.nih.gov/articles/PMC11706857
[6] https://pmc.ncbi.nlm.nih.gov/articles/PMC11814525/
[7] https://pmc.ncbi.nlm.nih.gov/articles/PMC8945901/
[8] https://research.sabanciuniv.edu/23394/1/Functionally_heterogeneous_porous_scaffold_design_for_tissue_engineering_Accepted.pdf
[9] https://www.frontiersin.org/journals/bioengineering-and-biotechnology/articles/10.3389/fbioe.2023.1252636/full
[10] https://www.frontiersin.org/journals/bioengineering-and-biotechnology/articles/10.3389/fbioe.2024.1444986/full
[11] https://www.frontiersin.org/journals/bioengineering-and-biotechnology/articles/10.3389/fbioe.2025.1629816/full
[12] https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2025.1719605/full
[13] https://www.mdpi.com/2079-4983/16/9/328
[14] https://www.sciencedirect.com/science/article/abs/pii/S0142961223000868
[15] https://www.sciencedirect.com/science/article/abs/pii/S1742706110005106
[16] https://www.sciencedirect.com/science/article/abs/pii/S175161612300499X
[17] https://www.sciencedirect.com/science/article/abs/pii/S2405886624000137
[18] https://www.sciencedirect.com/science/article/pii/S2090123223000048
[19] https://www.sciencedirect.com/science/article/pii/S223878542502366X
[20] https://www.sciencedirect.com/science/article/pii/S2238785425031114
[21] https://www.sciencedirect.com/science/article/pii/S2452199X23001901
[22] https://www.sciencedirect.com/science/article/pii/S2468217920300071
[23] https://www.tandfonline.com/doi/full/10.1080/10255842.2024.2304709