# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** b5fa128f | **Time:** 482.15s | **Cost:** $0.03450
--------------------------------------------------------------------------------

# Ensuring Low Waveguide Loss in Silicon Photonics Under Manufacturing Variations and Temperature Drift: Methods for High-Bandwidth Optical Interconnects

## Abstract

Silicon photonics has emerged as the leading platform for high-bandwidth optical interconnects, leveraging CMOS-compatible fabrication processes to enable dense co-integration of electronics and photonics. However, the high refractive index contrast that enables compact device footprints simultaneously makes silicon photonic circuits highly sensitive to manufacturing process variations and temperature-induced drift. These variations manifest as optical phase errors, resonance wavelength shifts, and increased propagation losses that can severely degrade signal integrity in high-bandwidth applications. This report provides a comprehensive analysis of the methods employed to ensure that waveguide loss remains sufficiently low to maintain signal integrity, despite these challenging environmental and fabrication-induced perturbations. The discussion encompasses process-level solutions including advanced annealing techniques and refractive index trimming, design-based approaches such as waveguide geometry optimization and athermalization strategies, and system-level implementations including active thermal control and digital signal processing. By synthesizing insights from recent research across multiple institutions and fabrication platforms, this report offers a holistic perspective on the current state of the art and future directions for ensuring robust, low-loss operation of silicon photonic interconnects in production environments.

## 1. Introduction

The exponential growth in data center traffic and high-performance computing applications has driven unprecedented demand for optical interconnects capable of delivering terabit-per-second bandwidth with minimal power consumption. Silicon photonics has risen to meet this challenge, offering the promise of CMOS-foundry compatibility, mature fabrication infrastructure, and the ability to integrate photonic and electronic circuits on a single chip [1]. The silicon-on-insulator (SOI) platform, with its high refractive index contrast between silicon (n ≈ 3.45) and silicon dioxide (n ≈ 1.45), enables strong optical confinement that allows for dramatically compact waveguide structures with tight bending radii, facilitating the integration of complex photonic integrated circuits (PICs) within millimeter-scale footprints.

Despite these advantages, the very high index contrast that enables compact photonic circuits simultaneously renders them extremely sensitive to dimensional variations introduced during fabrication. Nanoscale variations in waveguide width and thickness—often on the order of a few nanometers—can introduce significant optical phase errors between identically designed components, leading to performance degradation in wavelength-division multiplexing (WDM) systems, resonant modulators, and filter structures [2]. Furthermore, silicon possesses a substantial thermo-optic coefficient (Δn/ΔT = 1.86 × 10⁻⁴ K⁻¹), meaning that temperature variations as small as a few degrees Celsius can induce refractive index changes on the order of 10⁻³, causing resonance wavelength shifts in sensitive components and altering propagation characteristics [3].

The propagation loss in silicon photonic waveguides represents a critical parameter that directly impacts the maximum achievable link length, power budget, and overall system reliability. For single-mode strip waveguides with widths of 400-500 nm fabricated on standard SOI substrates, baseline propagation losses typically range from 0.1 to 0.3 dB/mm at telecom wavelengths [3]. However, these losses can increase substantially under the combined influence of manufacturing variations and temperature drift, threatening signal integrity in high-bandwidth optical interconnect applications. This report examines the comprehensive array of methods—spanning fabrication processes, design strategies, and system-level techniques—that have been developed and deployed to maintain low waveguide loss under these challenging conditions.

## 2. Understanding the Sources of Loss and Variability

### 2.1 Manufacturing Process Variations

The fabrication of silicon photonic waveguides involves multiple lithography, etching, and deposition steps, each introducing variations that can impact optical performance. Contemporary silicon photonics processes typically employ 193 nm immersion lithography to produce both silicon and silicon nitride waveguides in 200-300 mm wafer formats, with photolithography achieving critical dimensions of approximately 100 nm [4]. However, the 6σ spread of both waveguide width and thickness variation within a wafer is typically in excess of 15 nm—an order of magnitude larger than the sub-nanometer variations that can significantly impact device performance in high-contrast waveguide systems [2].

The primary sources of manufacturing-induced loss and variability include sidewall roughness from etching processes, thickness variations in the silicon device layer, variations in buried oxide (BOX) cladding thickness, and film stress-induced distortions. Sidewall roughness is particularly critical because scattering from the core-cladding interface represents the dominant loss mechanism in high-index-contrast waveguides. The roughness amplitude directly correlates with propagation loss, and even sub-nanometer variations in surface smoothness can measurably affect loss characteristics [5]. Etch control in terms of width, depth, and sidewall angle is therefore critical to propagation loss, with final etch depth variations in silicon typically ranging from 2.5-3.3 nm [4].

Film stress represents another significant concern, particularly for thick cladding layers required in low-index waveguide designs. For cladding thicknesses exceeding 20 µm to achieve mode matching with single-mode fibers, film stress induces wafer bowing that can complicate subsequent lithography steps and introduce geometric distortions [4]. The relationship between film stress and wafer bow is described by the Stoney equation, which quantifies the curvature induced by stress in thin films deposited on substrates.

### 2.2 Temperature-Induced Effects

Temperature variations impact silicon photonic waveguides through multiple mechanisms, with the thermo-optic effect being the most significant. The large thermo-optic coefficient of silicon means that temperature changes directly alter the refractive index of the waveguide core, affecting phase relationships in interferometric structures, shifting resonance wavelengths in resonant components, and modifying propagation constants [3]. Experimental results have demonstrated that a 7°C temperature change in a 500 µm long silicon device can result in a 180° phase shift and a refractive index change of approximately 1.3 × 10⁻³ [3].

Beyond the thermo-optic effect, temperature variations can exacerbate loss mechanisms through several secondary effects. Thermal expansion mismatches between different materials in the waveguide stack can induce mechanical stress that modifies the effective index through the photoelastic effect. Temperature-dependent absorption in the cladding materials can increase propagation loss at elevated temperatures. Furthermore, thermal gradients across a chip can create non-uniform index variations that distort optical wavefronts and degrade the performance of complex photonic circuits.

The combined impact of manufacturing variations and temperature drift is particularly severe in resonant structures such as microring resonators (MRRs) and Mach-Zehnder interferometers (MZIs). In WDM systems employing cascaded MRR structures, wavelength misalignment between channels due to fabrication errors and temperature variations represents a critical issue that can lead to channel crosstalk and data errors [6]. Similarly, resonant cavity modulators exhibit sensitivity to both fabrication errors and temperature variations, requiring sophisticated thermal management strategies to maintain stable operation.

## 3. Process-Level Solutions for Loss Reduction

### 3.1 Hydrogen Thermal Annealing

Among the most effective process-level techniques for reducing waveguide loss, hydrogen thermal annealing has demonstrated remarkable capability in smoothing silicon waveguide sidewalls and reducing optical propagation losses. Research has shown that hydrogen annealing treatment applied after waveguide patterning can reduce sidewall roughness down to 0.25 nm (1σ) while maintaining rectangular strip waveguide geometries [5]. The resulting optical losses measured at telecom wavelengths were less than 1 dB/cm for waveguides with dimensions larger than 350 nm, representing among the lowest losses reported for standard SOI waveguides.

The mechanism underlying hydrogen annealing's effectiveness involves the high surface mobility of silicon atoms at elevated temperatures in hydrogen ambient, which enables surface diffusion that smooths asperities created during the etching process. Studies have demonstrated that increasing annealing duration allows greater roughness reduction and consequently lower optical propagation losses. After 8 minutes of annealing, an average 52% loss reduction was obtained compared to rib patterning without any annealing, resulting in approximately 0.6 dB/cm losses for critical dimensions of 300-400 nm [5].

However, careful consideration must be given to the annealing conditions and waveguide geometry. For rib waveguides, the silicon reflow during H₂ anneal can lead to the formation of a foot at the bottom of the structure and rounding of the top, requiring a compromise between low losses and conservation of the intended waveguide geometry [5]. Additionally, hydrogen can cause absorption in certain waveguide configurations, necessitating careful process optimization for specific applications.

### 3.2 Refractive Index Trimming Techniques

Manufacturing variations in waveguide dimensions translate directly into variations in the effective modal index, leading to phase errors that accumulate across photonic circuits. Refractive index trimming represents a powerful approach to post-fabrication correction of these variations, enabling reduction of variability across devices and correspondingly reducing the required active tuning ranges for compensation [1]. Multiple methods of refractive index trimming have been demonstrated across various photonic platforms, each with distinct advantages and limitations.

Electron beam irradiation has been employed to modify the refractive index of silicon waveguides with high spatial precision, enabling targeted trimming of individual components. Ion implantation offers similar capabilities, with the ability to tune the magnitude and depth of index modification by controlling ion species, dose, and energy [1]. Optical irradiation methods have demonstrated index changes through photochemical processes, while thermal treatment can modify both the silicon core and surrounding cladding materials.

Among these approaches, local thermal annealing of ion-implanted waveguides and sputter-deposited silica (SiO) cladding represent notable exceptions that maintain compatibility with trimming of packaged dies [1]. Research has demonstrated that thermal treatment of PECVD SiO cladding at temperatures of 350-450°C can induce significant changes in the SiOH peak associated with the deposited oxide, with corresponding changes in refractive index. Fourier-transform infrared (FTIR) spectroscopy measurements revealed little to no change in peaks associated with silicon nitride, but significant changes in the SiOH peak, leading to the hypothesis that modal effective index trimming stems from composition and corresponding index changes in the PECVD SiO waveguide cladding [1]. Prior studies of thin film SiO thermal annealing report reductions in refractive index for temperatures below 600°C, consistent with these observations.

### 3.3 Advanced Deposition and Annealing Processes

For silicon nitride waveguides, which offer advantages including better optical power handling, lower thermal sensitivity, and increased robustness to dimensional variations compared to silicon waveguides, specialized deposition and annealing processes are critical for achieving ultra-low losses [7]. Thick core nitride waveguide designs, which are essential for nonlinear optical photonics, can achieve losses as low as 0.4 dB/m and resonator quality factors as high as 67 million when fabricated with appropriate processes [7]. However, these typically require annealing temperatures of 1050°C and structures for stress mitigation as well as chemical-mechanical polishing (CMP).

Research efforts to reduce the processing temperature of thick nitride waveguides have focused on deuterated silicon nitride to lower losses in the nitride core, though these approaches have not addressed lowering the deuterated oxide cladding losses [7]. The development of uniform anneal-free waveguide fabrication processes for both thin and thick structures remains a significant challenge, as heterogeneous and monolithic integration of nitride photonics with materials that cannot withstand high annealing temperatures is inhibited by incompatibility with high-temperature nitride growth and high-temperature post-oxide cladding annealing processes.

Post-deposition annealing is generally desirable to remove hydrogen impurities and densify the oxide cladding, with the specific annealing process requiring optimization based on the waveguide confinement requirements and the thermal budget constraints of the overall process flow [4]. For very thick claddings, film stress-induced wafer bowing must be managed, potentially through deposition of compensating films on the wafer backside.

## 4. Design-Based Approaches to Loss Mitigation

### 4.1 Waveguide Geometry Optimization

One of the most effective ways to reduce propagation loss through design is by utilizing wider waveguides, which reduces the modal overlap with the sidewall interfaces where roughness-induced scattering occurs [4]. This approach can be effective up to a certain point, beyond which the waveguide becomes multimode and other properties such as minimum bending radius begin to degrade. The relationship between waveguide width and sidewall roughness-induced loss demonstrates that wider waveguides exhibit lower scattering losses for a given roughness amplitude, making width optimization a powerful design tool.

For typical single-mode strip waveguides with 220 nm height and 450 nm width, propagation losses can be maintained below 0.01 dB/90° for bending radii of 5 µm in the TE polarization [4]. However, the loss increases exponentially as the bending radius decreases, requiring careful trade-offs between circuit compactness and loss budget. Waveguide crossings, which are necessary for complex routing in large-scale PICs, require optimized tapers with slowly varying widths compared to the mode evolution to avoid reflections and generation of higher order modes. For optimized taper waveguide crossings fabricated in standard CMOS-compatible 300 mm foundry processes, insertion loss for TE mode at 1550 nm can be approximately 0.2 dB after considering the impact of manufacturing variations, with crosstalk levels of -56 dB [4].

Partially etched rib waveguides offer reduced sensitivity to performance degradation as a function of waveguide geometry compared to fully etched strip waveguides [8]. The modal overlap of the fundamental mode does not vary strongly with waveguide width for partially etched waveguides, and most of the mode is contained in the slab region where no sidewall interfaces exist. This geometric characteristic results in less variation in excess loss under radiation exposure and potentially under other perturbation sources.

### 4.2 Athermalization Strategies

Given the substantial thermo-optic coefficient of silicon, athermalization represents a critical design requirement for silicon photonic filters and other components requiring stable operation across temperature ranges. A hybrid strip-slot waveguide introduced into one arm of an MZI structure has demonstrated athermalization with temperature-dependent wavelength shift of -5 pm/K and insertion loss of 0.4 dB with a device footprint of 170 µm × 580 µm [6]. This approach leverages the opposite thermo-optic coefficients of different waveguide geometries to achieve net zero temperature dependence.

Passive temperature compensation techniques can maintain resonant wavelength stability without active power consumption, though the mode field distribution must be carefully designed to achieve the desired compensation [6]. These approaches are particularly attractive for applications where power consumption and system complexity must be minimized. The design of athermal waveguides requires detailed consideration of the thermo-optic coefficients of all materials in the waveguide stack, including the core, cladding, and substrate materials.

### 4.3 Robust Design Against Variations

The sensitivity of silicon photonic circuits to minute variations in fabricated geometries necessitates design approaches that maximize robustness to process variations. Adjoint-based optimization methods have been developed to efficiently search through the full space of fabricable devices, enabling the design of photonic devices with previously unattainable fabrication robustness [9]. These computational design approaches can identify device geometries that maintain performance despite expected variations in critical dimensions.

For wavelength filtering circuits, the variability of critical process steps such as waveguide width and height must be considered during the design phase. Ignoring the impact of process variation could lead to circuit failure even when active tuning capabilities are available in the platform [2]. For instance, a tunable beam coupler implemented as a balanced Mach-Zehnder interferometer with phase tuners in the arms can only tune over the full range of 0-100% power coupling if the static beam splitters at the inputs provide sufficient accuracy. Design margins must therefore account for the expected range of process variations across the manufacturing technology node being utilized.

## 5. System-Level Thermal Management

### 5.1 Active Thermal Control

Integrated heater and thermal control circuits represent the most widely deployed approach for managing temperature drift in silicon photonic systems. By implementing localized heating elements and feedback control loops, the temperature of sensitive components can be actively stabilized despite ambient temperature variations or thermal gradients across the chip [6]. This approach is particularly effective for resonant components such as microring modulators and filters, where resonance wavelength stability is critical for proper operation.

The design of heater architecture for thermal control of silicon photonics circuits requires careful consideration of thermal efficiency, crosstalk between adjacent heaters, and power consumption. Comparison of different heater architectures has demonstrated trade-offs between these parameters, with some designs offering lower power consumption at the cost of increased thermal crosstalk, and vice versa [3]. For high-density PICs with many thermally tunable elements, minimizing thermal crosstalk is essential to prevent unintended tuning of adjacent components.

The thermo-optic phase shifter, which leverages the temperature-dependent refractive index of silicon to achieve phase modulation, represents a key building block for thermal control systems. Efficient, compact, and low-loss thermo-optic phase shifters in silicon have been demonstrated with optimized designs that maximize the phase shift per unit length while minimizing insertion loss and power consumption [3]. These phase shifters serve both as tuning elements and as components in more complex thermal management systems.

### 5.2 Wavelength Locking Techniques

For WDM systems employing cascaded microring resonator structures, wavelength misalignment between channels due to fabrication errors and temperature variations represents a critical challenge. Wavelength locking methods can be utilized to align the wavelengths, though at the cost of increased device complexity [6]. These techniques typically involve monitoring the output of resonant components and adjusting heating elements to maintain alignment with the desired wavelength channels.

The implementation of wavelength locking requires additional photodetectors, control electronics, and feedback algorithms, adding complexity and power consumption to the overall system. However, for applications requiring high reliability and predictable performance, the added complexity is often justified by the improved system margin and reduced sensitivity to environmental variations. Digital implementations of wavelength locking algorithms can provide adaptive compensation for both static fabrication variations and dynamic temperature fluctuations.

### 5.3 Digital Signal Processing Compensation

Digital signal processing (DSP) has emerged as a powerful tool for compensating for impairments in high-speed optical interconnect systems, including those arising from manufacturing variations and temperature drift [6]. With post-filter and maximum likelihood sequence detection (MLSD), single-lane bit rates of 200 Gb/s (80 Gbaud) PAM-6 have been achieved based on Mach-Zehnder modulators with electro-optic bandwidth of 22.5 GHz [6]. These DSP techniques can compensate for channel impairments including frequency response variations, phase noise, and timing errors that may result from imperfect photonic components.

The advantage of DSP-based compensation is that it operates on the electrical signals after photodetection, requiring no modifications to the photonic hardware. However, DSP can only compensate for impairments that manifest as predictable, deterministic distortions in the received signal; random variations and noise cannot be compensated through signal processing alone. Therefore, DSP-based approaches are most effective when used in conjunction with hardware-based methods that minimize the fundamental sources of impairment.

## 6. Material and Platform Considerations

### 6.1 Silicon Nitride Integration

The integration of silicon nitride (SiN) waveguides in silicon photonics platforms has become commonplace, owing to the better optical power handling, lower thermal sensitivity, and increased robustness to dimensional variations of SiN compared to Si waveguides [1]. Silicon nitride waveguides can achieve extremely low losses of 0.1 dB/m, making them attractive for long-distance propagation within chips and for applications requiring ultra-high quality factors [3].

The development of platforms that combine silicon and silicon nitride waveguides enables optimization of different circuit sections for their specific requirements. Silicon waveguides can be used for active modulation and detection, while silicon nitride waveguides can be employed for low-loss routing and high-Q resonant structures. However, the integration of these materials requires careful consideration of their different processing requirements, particularly the high temperatures required for low-loss silicon nitride deposition and annealing.

### 6.2 Cladding Material Optimization

The choice of cladding materials and their processing significantly impacts waveguide loss characteristics. PECVD-deposited silicon dioxide claddings require post-deposition annealing to densify the film and reduce hydrogen content, which can otherwise contribute to absorption losses. The annealing process also affects the refractive index of the cladding, which in turn affects the optical confinement and loss characteristics of the waveguide [1].

For applications requiring very low losses, LPCVD SiO₂ claddings may be preferred, though these typically require CMP to achieve smooth surfaces [4]. The roughness of the top and bottom surfaces of the waveguide can contribute to scattering losses, particularly for waveguides with weak vertical confinement. Some deposition methods produce surfaces with measurable roughness that can be improved through CMP processing.

## 7. Emerging Approaches and Future Directions

### 7.1 Anneal-Free Fabrication Processes

A major transformation in silicon nitride photonics is needed, where the ultra-low loss and wafer-scale CMOS foundry compatible processes of thin nitride structures and nonlinear properties of thick waveguide structures are maintained while adding the heterogeneous functionality of optical gain, high-speed modulation, electronics, and engineered thermal properties [7]. At the same time, a uniform anneal-free waveguide fabrication process for both thin and thick structures is required to enable integration with materials that cannot withstand high-temperature processing.

Research efforts are exploring alternative deposition and processing approaches that can achieve low-loss waveguides without the traditional high-temperature annealing steps. These include novel precursor materials for chemical vapor deposition, optimized plasma processing conditions, and post-deposition treatments that can achieve film densification at lower temperatures. The development of such processes would enable heterogeneous integration of silicon photonics with materials such as compound semiconductors, ferroelectrics, and organic materials that are incompatible with high-temperature processing.

### 7.2 Advanced Surface Smoothing Techniques

Beyond hydrogen annealing, multiple methods exist or are under development to reduce the sidewall roughness of silicon waveguides. Cycles of oxidation and oxide removal can smooth sidewalls through the preferential oxidation of surface asperities, though this approach must be carefully controlled to avoid excessive dimensional changes [4]. Photoresist reflow techniques can smooth features before the etching transfer, reducing the roughness that would otherwise be imprinted on the silicon waveguide sidewalls.

The combination of multiple smoothing techniques may offer superior results compared to any single approach. For example, resist reflow followed by hydrogen annealing can address roughness at multiple length scales, achieving smoother sidewalls than either technique alone. The optimization of these multi-step processes requires careful consideration of their impact on other aspects of the fabrication flow, including critical dimension control and overlay accuracy.

### 7.3 Machine Learning for Process Optimization

The increasing complexity of silicon photonic circuits and the tight tolerances required for high-performance operation are driving the adoption of machine learning approaches for process optimization and variation compensation. These methods can identify correlations between process parameters and device performance that may not be apparent through traditional design of experiments approaches.

Machine learning models trained on fabrication and measurement data can predict the performance of devices before fabrication, enabling more efficient design iterations. They can also be used to develop compensation strategies that account for systematic variations across wafers or batches. As the volume of data from high-volume manufacturing increases, machine learning approaches will become increasingly powerful for optimizing process parameters and reducing variability.

## 8. Conclusion

Maintaining low waveguide loss in silicon photonics under manufacturing process variations and temperature drift requires a multi-faceted approach encompassing process-level solutions, design strategies, and system-level techniques. Hydrogen thermal annealing has emerged as a highly effective method for reducing sidewall roughness and achieving propagation losses below 1 dB/cm in standard SOI waveguides. Refractive index trimming techniques enable post-fabrication correction of variations, though many approaches require additional processing steps that may not be compatible with packaged dies.

Design-based approaches including waveguide geometry optimization, athermalization strategies, and robust design against variations provide inherent resilience to perturbations without requiring active intervention. For applications requiring the highest performance, active thermal control through integrated heaters and feedback systems provides precise stabilization of temperature-sensitive components. Digital signal processing offers powerful compensation capabilities for residual impairments that propagate through the optical link.

The continued evolution of silicon photonics toward larger-scale integration and higher bandwidths will further emphasize the importance of these loss mitigation techniques. The development of anneal-free fabrication processes, advanced surface smoothing methods, and machine learning-based optimization approaches represents promising directions for future research. By combining advances in these multiple domains, the photonics community can continue to push the boundaries of what is achievable in high-bandwidth optical interconnects while maintaining the signal integrity essential for reliable operation in data center and high-performance computing applications.

The path forward requires continued collaboration between process engineers, device designers, and system architects to ensure that solutions developed at one level are compatible with constraints and requirements at other levels. As silicon photonics matures into a high-volume manufacturing technology, the standardization of best practices for loss mitigation will become increasingly important for ensuring consistent performance across different fabrication facilities and technology generations.

---

## References

[1] Optica Publishing Group, "Refractive index trimming methods in silicon photonics," *Optics Express*, vol. 33, no. 21, pp. 43542-43556, 2025.

[2] ACS Photonics, "Fabrication process variations in silicon photonics platforms," *ACS Photonics*, 2022.

[3] MDPI Nanomaterials, "Silicon photonics for optical interconnects: Thermo-optic effects and waveguide characteristics," *Nanomaterials*, vol. 12, no. 3, p. 485, 2022.

[4] University of California Berkeley, "Fabrication techniques for silicon photonics MEMS switches," *EECS Technical Report*, EECS-2021-234, 2021.

[5] C. Bellegarde, et al., "Impact of hydrogen thermal annealing on silicon rib waveguide losses," *HAL Grenoble*, 2018.

[6] Photonics Research, "Silicon photonic filters and modulators for high-speed interconnects," *Photonics Research*, vol. 10, no. 9, 2022.

[7] Nature Communications, "Silicon nitride photonics: Bridging thin and thick film platforms," *Nature Communications*, 2024.

[8] DTIC, "Gamma radiation effects on silicon photonic waveguides," *Defense Technical Information Center*, AD1075231.

[9] Stanford University, "Automated design of silicon photonic devices using adjoint optimization," *J. Piggott Thesis*.

## Annotations


## Sources
[1] http://web.stanford.edu/group/nqp/jv_files/thesis/piggott_thesis.pdf
[2] https://apps.dtic.mil/sti/tr/pdf/AD1075231.pdf
[3] https://hal.univ-grenoble-alpes.fr/hal-01942725v1/file/Bellegarde2018.pdf
[4] https://opg.optica.org/abstract.cfm?uri=oe-18-14-14474
[5] https://opg.optica.org/oe/abstract.cfm?uri=oe-33-21-43542
[6] https://pubs.acs.org/doi/10.1021/acsphotonics.2c01194
[7] https://www.intechopen.com/online-first/1224995
[8] https://www.mdpi.com/2079-4991/12/3/485
[9] https://www.nature.com/articles/s41377-024-01503-4
[10] https://www.nature.com/articles/s41467-024-44750-0
[11] https://www.researching.cn/ArticlePdf/m00072/2022/10/9/A106.pdf
[12] https://www.sciencedirect.com/topics/engineering/silicon-waveguide
[13] https://www2.eecs.berkeley.edu/Pubs/TechRpts/2021/EECS-2021-234.pdf