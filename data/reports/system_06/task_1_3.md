# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 0583f87d | **Time:** 510.76s | **Cost:** $0.03439
--------------------------------------------------------------------------------

# Design Constraints in Gate Length Scaling of FinFET Devices: Balancing Drive Current Enhancement and Leakage Current Suppression Amidst Quantum and Short-Channel Effects

## Abstract

The continued scaling of FinFET devices to sub-10nm technology nodes presents a fundamental conflict between enhancing drive current ($I_{ON}$) and suppressing leakage current ($I_{OFF}$). This research report examines the critical design constraints that must be balanced to manage this conflict, particularly in the presence of quantum mechanical effects and short-channel effects (SCEs). As gate lengths shrink below 10nm, phenomena including drain-induced barrier lowering (DIBL), subthreshold slope degradation, gate oxide tunneling, and source-to-drain tunneling become increasingly pronounced, threatening the efficiency gains that FinFET technology offers. This analysis explores the multifaceted design trade-offs involving gate structure engineering, channel design optimization, threshold voltage control, and source/drain engineering, while evaluating emerging materials and architectural innovations that enable continued scaling. The findings indicate that successful device optimization requires a holistic approach that considers electrostatic control, quantum confinement effects, and manufacturing process capabilities through design-technology co-optimization (DTCO) methodologies.

## 1. Introduction

The semiconductor industry has pursued relentless advancements in transistor technology to propel electronic devices into new realms of efficiency and performance. Conventional planar CMOS transistors have driven these advancements for decades, yet their limitations have become increasingly evident, especially when scaling down to sub-10nm technology nodes [1]. Issues such as short-channel effects, escalating leakage currents, and challenges in maintaining scalability have underscored the necessity for exploring alternative transistor architectures.

FinFET (Fin Field-Effect Transistor) technology has emerged as a pivotal innovation in response to these limitations. Distinguished by its three-dimensional fin-like structure, FinFETs offer superior electrostatic control over the channel region compared to their planar counterparts. The distinctive architecture features a thin vertical fin with the gate completely encircling the channel on three sides, enhancing channel control and resulting in better short-channel behavior and lower leakage power [2]. This three-dimensional configuration enables greater drive currents, lower operating voltages, and a considerable decrease in static leakage current, making FinFETs the preferred transistor technology for high-performance, power-efficient solutions in digital circuits.

However, as process nodes continue to shrink below 10nm, fundamental physical constraints become increasingly challenging to overcome. Quantum mechanical effects become more pronounced, exacerbating leakage issues through multiple mechanisms including subthreshold leakage, gate leakage, and band-to-band tunneling [3]. The semiconductor industry has established that a comprehensive understanding of these leakage pathways is essential for developing effective mitigation strategies. This report provides an in-depth analysis of the design constraints that must be balanced when scaling FinFET gate lengths, with particular focus on managing the inherent conflict between drive current enhancement and leakage current suppression.

## 2. Fundamentals of FinFET Operation and Scaling Dynamics

### 2.1 FinFET Architecture and Electrostatic Control

The FinFET's three-dimensional architecture represents a significant departure from traditional planar MOSFET designs. In a typical FinFET implementation, the channel is formed in a thin vertical silicon fin that extends above the substrate surface, with the gate electrode wrapping around three sides of this fin [4]. This multi-gate configuration provides superior electrostatic control over the channel, as the gate electric field can influence charge carriers from multiple directions rather than just from the top surface.

The effectiveness of this electrostatic control is quantified by the parameter $\lambda$, known as the natural length or screening length, which characterizes how effectively the gate controls the channel potential. For a FinFET, the natural length can be expressed as:

$$\lambda = \sqrt{\frac{\epsilon_{si} t_{ox} t_{fin}}{2\epsilon_{ox}}}$$

where $\epsilon_{si}$ and $\epsilon_{ox}$ are the permittivities of silicon and the gate oxide, respectively, $t_{ox}$ is the oxide thickness, and $t_{fin}$ is the fin thickness. A smaller natural length indicates better electrostatic control and improved immunity to short-channel effects. The three-sided gate wrapping in FinFETs effectively reduces $\lambda$ compared to single-gate planar devices, enabling further scaling while maintaining acceptable short-channel behavior.

### 2.2 Drive Current Enhancement Mechanisms

The drive current $I_{ON}$ in a FinFET device is determined by the charge carriers in the channel and their velocity under the influence of the longitudinal electric field. In the saturation region, the drive current can be approximated as:

$$I_{ON} = \frac{1}{2} \mu C_{ox} \frac{W}{L} (V_{GS} - V_{th})^2 (1 + \lambda V_{DS})$$

where $\mu$ is the carrier mobility, $C_{ox}$ is the gate oxide capacitance per unit area, $W$ is the effective channel width, $L$ is the gate length, $V_{GS}$ is the gate-source voltage, $V_{th}$ is the threshold voltage, and $\lambda$ is the channel length modulation parameter [5].

Enhancing drive current in scaled FinFETs involves several strategies. Increasing the effective channel width through multiple fin configurations directly scales $I_{ON}$, though this comes at the cost of increased area consumption. Reducing the gate length $L$ improves $I_{ON}$ according to the $1/L$ dependence, but this reduction simultaneously exacerbates short-channel effects that increase leakage. Optimizing the fin height and thickness affects both the electrostatic control and the current-carrying capability, requiring careful balance to prevent volume inversion effects and maintain acceptable subthreshold characteristics.

### 2.3 Leakage Current Mechanisms

Leakage current in FinFETs manifests through multiple mechanisms that become increasingly problematic as gate lengths are scaled down. The primary leakage components include:

**Subthreshold Leakage ($I_{sub}$):** This component flows between the source and drain when the transistor is in the OFF state ($V_{GS} < V_{th}$). The subthreshold current is exponentially dependent on the applied gate voltage and is characterized by the subthreshold swing (SS):

$$SS = \frac{dV_{GS}}{d(\log_{10} I_{DS})} = \frac{kT}{q} \ln(10) \left(1 + \frac{C_{dep}}{C_{ox}}\right)$$

where $k$ is Boltzmann's constant, $T$ is temperature, $q$ is the elementary charge, and $C_{dep}$ is the depletion capacitance. Ideally, SS approaches the thermal limit of 60 mV/decade at room temperature, but short-channel effects cause significant degradation [6].

**Gate Oxide Tunneling Leakage ($I_{gate}$):** As gate oxide thicknesses approach atomic scales, electrons can tunnel directly through the oxide barrier via Fowler-Nordheim tunneling or direct tunneling mechanisms. The gate leakage current density $J_{ox}$ can be approximated using the Fowler-Nordheim equation:

$$J_{ox} = \frac{q^3 E_{ox}^2}{8\pi h \phi_{ox}} \exp\left(-\frac{8\pi\sqrt{2m^*}\phi_{ox}^{3/2}}{3qhE_{ox}}\right)$$

where $E_{ox}$ is the electric field across the oxide, $h$ is Planck's constant, $m^*$ is the effective electron mass in the oxide, and $\phi_{ox}$ is the barrier height [7].

**Source-to-Drain Tunneling ($I_{SD}$):** In ultra-short channel devices, quantum mechanical tunneling directly across the channel from source to drain becomes significant. This phenomenon is particularly problematic in devices with channel lengths below 10nm, where the width of the potential barrier becomes comparable to the electron wavelength [8].

**Gate-Induced Drain Leakage (GIDL):** This effect occurs in the drain-gate overlap region under high reverse bias, where band-to-band tunneling generates electron-hole pairs that contribute to leakage current.

## 3. Short-Channel Effects in Scaled FinFETs

### 3.1 Threshold Voltage Roll-Off

As gate lengths decrease, the threshold voltage $V_{th}$ of the transistor decreases due to the increasing influence of the drain voltage on the channel potential. This phenomenon, known as threshold voltage roll-off, directly impacts both drive current and leakage. The threshold voltage reduction can be modeled as:

$$\Delta V_{th} = V_{th}(L) - V_{th}(L_{long}) \approx \frac{a}{L^n}$$

where $L$ is the gate length, $L_{long}$ is a reference long-channel length, and $a$ and $n$ are technology-dependent parameters [9]. The roll-off effect becomes more pronounced as $L$ approaches the natural length $\lambda$, eventually making it impossible to turn the device off completely.

### 3.2 Drain-Induced Barrier Lowering (DIBL)

DIBL represents another critical short-channel effect where the drain voltage reduces the potential barrier between the source and channel, facilitating electron injection even when the gate voltage is below threshold. The DIBL coefficient $\eta$ is defined as:

$$\eta = -\frac{\Delta V_{th}}{\Delta V_{DS}}$$

Higher DIBL coefficients indicate greater susceptibility to this effect. In scaled FinFETs, DIBL contributes to both increased subthreshold leakage and reduced output resistance, degrading the voltage gain of analog applications [10].

### 3.3 Subthreshold Slope Degradation

The subthreshold slope SS represents the gate voltage required to change the subthreshold current by one decade. In ideal long-channel devices, SS approaches the thermal limit of 60 mV/decade. However, short-channel effects cause significant degradation, with SS values increasing to 80-100 mV/decade or higher in aggressively scaled devices. This degradation directly impacts the $I_{ON}/I_{OFF}$ ratio, as a higher SS means more gate voltage swing is required to switch between states, increasing dynamic power consumption while potentially increasing OFF-state leakage.

### 3.4 Impact of Fin Dimensions on Short-Channel Effects

The fin geometry plays a crucial role in determining the severity of short-channel effects. Decreasing the fin width $t_{fin}$ is effective in reducing short-channel effects; however, this comes with the trade-off of potential performance degradation [11]. This degradation is attributed to the increase in parasitic drain/source resistance, resulting in a reduction of drive current and transconductance of the device. Additionally, the higher concentration of subthreshold leakage current at the corners of the fin due to these dimensional changes is called the "corner effect."

Furthermore, smaller fin widths impede the easy flow of heat, leading to an increase in device temperature. Elevated temperatures exacerbate all leakage mechanisms, creating a positive feedback loop that can significantly impact circuit reliability. The solution to this problem involves manufacturing FinFETs with more curved and rounded fin profiles, which reduce corner effects while maintaining thermal management capabilities.

## 4. Quantum Mechanical Effects in Ultra-Scaled FinFETs

### 4.1 Quantum Confinement

As FinFET dimensions approach the nanometer scale, quantum confinement effects become significant. Quantum confinement varies the band structure and density of states (DOS) of the channel material, affecting both carrier transport and tunneling phenomena [12]. In ultra-thin silicon channels, the quantization of energy levels perpendicular to the transport direction creates subbands with different effective masses, altering the density of states and carrier distribution.

The quantum confinement effect can be analyzed by solving the 1D Schrödinger equation for the confinement potential. For a triangular well approximation at the Si/SiO₂ interface, the ground state energy is:

$$E_0 = \left(\frac{\hbar^2}{2m^*}\right)^{1/3} \left(\frac{3\pi q E_{ox}}{2\epsilon_{si}}\right)^{2/3}$$

This energy quantization shifts the threshold voltage and reduces the inversion charge density for a given gate voltage, effectively reducing drive current while simultaneously affecting leakage characteristics [13].

### 4.2 Gate Oxide Tunneling

With gate oxide thicknesses approaching 1nm and below, direct tunneling through the oxide barrier becomes a significant source of gate leakage current. The gate leakage through tunneling mechanisms has emerged as a critical concern, with electrons able to penetrate the ultra-thin gate dielectric despite improvements in high-k materials [3]. The tunneling probability can be estimated using the WKB approximation:

$$T \approx \exp\left(-\frac{2}{\hbar}\int_{x_1}^{x_2}\sqrt{2m^*(V(x)-E)}dx\right)$$

where $V(x)$ is the potential barrier profile and $E$ is the electron energy. For ultra-thin oxides, this tunneling probability becomes substantial even at moderate electric fields, contributing significantly to total power consumption.

### 4.3 Source-to-Drain Tunneling

By scaling channel length, the width of the potential barrier reduces, making it possible for carriers to penetrate through the barrier via quantum tunneling. This effect in the OFF-state increases the leakage current and makes it harder to turn off the device [14]. Tunneling current percentage over the whole OFF-current increases with gate scaling. With source-to-drain tunneling, the gate voltage needs to be lower to make the barrier taller in order to keep the OFF-current at acceptable levels, leading to higher subthreshold swing. Higher SS degrades device performance and creates a fundamental trade-off between leakage suppression and switching speed.

### 4.4 Quantum Transport Considerations

At gate lengths below 10nm, the semiclassical drift-diffusion model becomes inadequate for accurate device simulation. Quantum transport effects, including phase coherence and discrete energy levels, must be considered. The calculated ON-current trend with quantum transport tools and compact model-based calculations show significant differences due to three major effects: short-channel effects, source-to-drain tunneling, and quantum confinement [14]. This necessitates sophisticated CAD tools that can capture all essential physics accurately for reliable device design.

## 5. Design Constraints and Balancing Act

### 5.1 The Fundamental Trade-Off

The core challenge in FinFET scaling lies in balancing two seemingly contradictory objectives: maximizing drive current $I_{ON}$ while minimizing leakage current $I_{OFF}$. These objectives are fundamentally linked through the device physics:

- **Drive Current Enhancement:** Requires shorter gate lengths, higher electric fields, and optimized channel geometry to maximize carrier injection and velocity.

- **Leakage Suppression:** Requires longer effective channels, lower electric fields in the OFF-state, and robust electrostatic control to prevent unintended carrier flow.

The $I_{ON}/I_{OFF}$ ratio serves as the key figure of merit, with industry targets typically requiring ratios of $10^9$ or higher for low-power applications [15]. Achieving this ratio in aggressively scaled devices requires careful optimization of multiple design parameters.

### 5.2 Gate Length Scaling Constraints

The minimum gate length $L_{min}$ is constrained by several factors:

1. **Electrostatic Integrity:** The natural length $\lambda$ must be sufficiently small compared to $L$ to maintain acceptable short-channel effects. Typically, $L > 4\lambda$ is required for adequate control.

2. **DIBL Constraint:** The DIBL coefficient must remain below a threshold (typically < 100 mV/V) to maintain acceptable output resistance and subthreshold characteristics.

3. **Tunneling Limit:** Source-to-drain tunneling must be kept below a specified fraction of the total OFF-current, typically requiring $L > 5-7$ nm for silicon channels.

4. **Manufacturing Variability:** Random dopant fluctuations and line-edge roughness must be accounted for, requiring design margins that effectively increase the minimum usable gate length.

### 5.3 Fin Dimension Optimization

The fin width $t_{fin}$ and height $H_{fin}$ present their own optimization challenges:

- **Fin Width:** Narrower fins improve electrostatic control and reduce short-channel effects but increase parasitic resistance and reduce drive current. The optimal fin width typically ranges from 5-8 nm for sub-10nm nodes.

- **Fin Height:** Taller fins increase the effective channel width and drive current but make the fin more susceptible to mechanical instability and increase the aspect ratio, complicating fabrication.

- **Fin Pitch:** The spacing between fins affects density and parasitic capacitance, with tighter pitches enabling higher density but increased cross-talk and manufacturing challenges.

### 5.4 Gate Oxide and Dielectric Engineering

The gate dielectric stack represents a critical optimization point. Deploying high-k dielectric materials in the narrow channel length of FinFET devices is essential for enhancing efficiency and minimizing short-channel effects [11]. The industry has focused on designing FinFETs using innovative dielectric materials, including Al₂O₃, SiO₂, HfO₂, Si₃N₄, ZrO₂, TiO₂, Y₂O₃, Ta₂O₅, and LaZrO₂, which reduce gate leakage current.

The equivalent oxide thickness (EOT) must be minimized to maintain electrostatic control, but this reduction increases direct tunneling. High-k dielectrics like HfO₂ (k ≈ 25) allow physical thickness scaling while maintaining acceptable EOT, reducing gate leakage compared to SiO₂ at the same EOT [16]. However, even with high-k materials, direct tunneling occurs due to the reduction in the gate oxide layer thickness, necessitating careful optimization of the dielectric stack.

### 5.5 Threshold Voltage Control Methods

Threshold voltage $V_{th}$ control is essential for managing the $I_{ON}/I_{OFF}$ trade-off. Multiple approaches exist:

1. **Work Function Engineering:** Using metal gates with appropriate work functions enables $V_{th}$ tuning without heavy channel doping, reducing random dopant fluctuations.

2. **Channel Doping:** Retrograde doping profiles can create ground-plane effects that improve short-channel behavior, but random dopant fluctuations become problematic at atomic scales.

3. **Gate Stack Optimization:** The combination of high-k dielectrics and metal gates allows precise $V_{th}$ control through dipole formation at the interface.

4. **Body Biasing:** Applying bias to the substrate or body terminal can modulate $V_{th}$ dynamically, enabling adaptive power management in circuits.

### 5.6 Spacer Engineering

The gate spacer dimensions significantly impact device performance. Decreasing the spacer length brings the source and drain regions closer to the gate, which can improve short-channel control and enhance the $I_{ON}/I_{OFF}$ ratio [17]. A narrower spacer reduces the distance between the gate and the lightly doped drain extension regions, allowing the gate to better suppress leakage and enhance drive current. However, excessive reduction in spacer length can lead to parasitic capacitance increase and short-channel effects, which may eventually impair performance. Moderate spacer length scaling can therefore increase $I_{ON}/I_{OFF}$.

Studies on wavy FinFET structures have compared various spacer materials such as SiO₂, Si₃N₄, and HfO₂, finding that HfO₂ spacers deliver significant leakage reduction and improved performance [17]. The S³-FinFET with optimized spacer configuration achieves significantly higher $I_{ON}/I_{OFF}$ ratio, improved drive current, and markedly reduced DIBL and SS values.

## 6. Advanced Mitigation Strategies

### 6.1 Gate Structure Modifications

Various modifications to the gate structure of FinFET devices can significantly reduce leakage current. These include using high-k gate dielectric materials, metal gate electrodes, and optimized gate length designs [3]. Gate engineering techniques such as work function tuning and gate stack optimization help control threshold voltage and minimize gate-induced drain leakage (GIDL), resulting in improved device performance and power efficiency.

Negative capacitance FinFETs (NC-FinFETs) represent an emerging approach that uses ferroelectric materials in the gate stack to achieve sub-60 mV/dec subthreshold swing without the $I_{ON}$ penalty traditionally associated with steep-slope devices [15]. Current research in NC-FinFET focuses on material engineering of the ferroelectric layer such as doped HfO₂, PZT, and BaTiO₃ to balance scalability, polarization strength, and CMOS compatibility. Compared with conventional FinFETs, the proposed 10 nm PZT NC-FinFET achieves a lower subthreshold swing of 30.5-55.5 mV/dec while maintaining the same $I_{ON}/I_{OFF}$ ratio.

### 6.2 Source/Drain Engineering Techniques

Source and drain engineering plays a crucial role in managing leakage while maintaining drive current. Key approaches include:

**Selective Epitaxial Growth:** This technique repairs the fin outer surface and can reduce parasitic resistance while maintaining junction abruptness [11].

**Junction Profile Engineering:** Optimized doping profiles in the source/drain extensions minimize electric field peaks that contribute to GIDL and band-to-band tunneling.

**Stress Engineering:** Applying tensile or compressive stress in the channel enhances carrier mobility, allowing lower $V_{DD}$ for the same $I_{ON}$, which indirectly reduces leakage.

### 6.3 Channel Design and Material Innovations

Channel design optimization involves both geometric and material considerations:

**Heterojunction Channels:** Using III-V compound semiconductors like InGaAs and GaSb, with their high carrier mobility and tunable band gaps, offers compelling advantages for high-performance logic applications [18]. These materials naturally suppress short-channel effects and reduce direct source-to-drain tunneling, though integration challenges with silicon substrates remain.

**Strained Silicon:** Applying mechanical strain to the silicon channel modifies the band structure, increasing carrier mobility and enabling higher drive currents at reduced voltages.

**Ultra-Thin Body Structures:** Silicon-on-insulator (SOI) FinFETs and fully depleted devices reduce parasitic capacitance and improve short-channel behavior by eliminating the body contact.

### 6.4 Advanced Isolation Techniques

Isolation between adjacent devices becomes increasingly critical at high densities. Shallow trench isolation (STI) must be optimized to minimize stress-induced effects on adjacent fins while preventing leakage through the isolation oxide. For sub-10nm nodes, advanced isolation schemes including air gaps and high-aspect-ratio contacts are being developed to manage parasitic capacitance and leakage.

### 6.5 Design-Technology Co-Optimization (DTCO)

The close interaction of process capabilities requires that the circuit and physical design architecture be comprehended—this is classical Design Technology Co-optimization (DTCO) [19]. DTCO has become increasingly important as technology nodes advance, requiring collaboration between process engineers and circuit designers from the earliest stages of development.

Key DTCO considerations include:

- Memory transistor design must anticipate required read and write assists and their impact on area
- Denser cell libraries restrict possible cell configurations
- Complex cells with breaks are better assembled by automated place-and-route tools
- Flexible sizing and placement with multiple cells must be considered
- At all points in the design process, the anticipated physical design has to be understood
- Parasitic extraction tools must calculate the parasitics of moving cuts and dummy metals

## 7. Future Outlook and Emerging Technologies

### 7.1 Gate-All-Around (GAA) Transistors

The industry's shift from planar to three-dimensional structures is already underway. FinFETs have successfully enabled scaling down to 7 nm, offering improved subthreshold slope and reduced leakage by wrapping the surrounding the channel with the gate on three sides [18]. Gate-all-around (GAA) transistors, including nanosheet and nanowire configurations, provide even greater electrostatic control by wrapping the gate completely around the channel. GAA architectures offer superior electrostatic control, increased effective gate length, and reduced short-channel effects, representing the natural evolution beyond FinFETs for sub-5nm nodes.

### 7.2 Vertical Transistor Architectures

Vertical transistor architectures represent an alternative approach to continued scaling, where the current flows vertically rather than horizontally. This orientation allows for increased device density without aggressive lateral scaling and can provide improved electrostatic control through the gate-all-around configuration.

### 7.3 Computational Challenges and Requirements

As channel lengths go below 10nm, high source-to-drain tunneling current in the OFF-state becomes significant. To capture tunneling effects accurately, sophisticated CAD tools are required [14]. Due to these reasons, device characteristics for advanced technology nodes must be calculated with quantum transport tools that capture all essential physics accurately. The computational requirements for accurate device simulation continue to increase as quantum effects become more pronounced.

### 7.4 Thermal Management Considerations

Thermal management becomes increasingly critical as device dimensions shrink. Higher power densities and reduced heat dissipation pathways in scaled FinFETs lead to elevated operating temperatures. Since leakage currents have positive temperature coefficients, thermal runaway can occur if heat is not adequately removed. Advanced thermal management strategies including improved heat spreading layers, optimized fin geometries, and thermal-aware circuit design are essential for reliable operation.

## 8. Conclusion

The scaling of FinFET gate lengths to sub-10nm dimensions presents a complex optimization challenge that requires balancing multiple, sometimes conflicting, design constraints. The fundamental conflict between drive current enhancement and leakage current suppression is mediated by a combination of short-channel effects and quantum mechanical phenomena that become increasingly pronounced at atomic scales.

Successful FinFET design requires holistic optimization across multiple domains: gate structure engineering using high-k dielectrics and metal gates, fin dimension optimization for electrostatic control, threshold voltage tuning through work function engineering, source/drain engineering for reduced parasitics, and spacer optimization for improved $I_{ON}/I_{OFF}$ ratios. The emergence of negative capacitance FinFETs and gate-all-around architectures offers promising pathways for continued scaling beyond the limitations of current FinFET implementations.

Design-technology co-optimization has become essential, requiring close collaboration between process development and circuit design teams from the earliest stages. As the semiconductor industry approaches the physical limits of silicon-based devices, innovations in materials, device architectures, and design methodologies will be crucial for maintaining the pace of progress that has driven the digital revolution.

The findings of this analysis indicate that while significant challenges remain, the continued evolution of FinFET technology through advanced engineering techniques and novel device architectures provides a viable pathway for high-performance, power-efficient electronics at future technology nodes. The key to success lies in recognizing and managing the inherent trade-offs through systematic optimization and innovative solutions that address both the symptoms and root causes of leakage and performance degradation in ultra-scaled devices.

## References

[1] Vixra.org, "FinFET Technology for Sub-10nm Nodes," 2024.

[2] Research Gate, "Leakage-Delay Tradeoff in FinFET Logic Circuits: A Comparative Analysis With Bulk Technology."

[3] PatSnap, "How To Reduce Leakage Current In FinFET Devices," 2025.

[4] MDPI Electronics, "Radiation Effects in FinFET Technology," 2025.

[5] ASU Elsevier Pure, "Design with Sub-10nm FinFET Technologies," 2017.

[6] PMC, "FinFET Materials and Design Optimization," 2024.

[7] ScienceDirect, "Gate Engineering Solutions for Short Channel Effects," 2025.

[8] Nature Scientific Reports, "NC-FinFET Performance Analysis," 2025.

[9] Purdue University, "Quantum Transport in Scaled FinFETs," 2014.

[10] PMC, "Spacer Engineering for FinFET Performance," 2024.

[11] PMC, "Corner Effects in Scaled FinFETs," 2024.

[12] Journal of Physics and Applications, "Quantum Tunneling in Scaled Devices," 2024.

[13] ASU Scholarship, "Compact Modeling of Double-Gate MOSFETs."

[14] Purdue University, "Source-to-Drain Tunneling in Nano-scale Devices," 2014.

[15] Nature Scientific Reports, "Negative Capacitance FinFETs," 2025.

[16] ScienceDirect, "High-K Dielectric Materials for FinFETs," 2025.

[17] PMC, "S3-FinFET Spacer Configuration," 2024.

[18] Journal of Physics and Applications, "Advanced Transistor Architectures," 2024.

[19] ASU Elsevier Pure, "Design Technology Co-optimization," 2017.

## Annotations


## Sources
[1] https://asu.elsevierpure.com/en/publications/design-with-sub-10-nm-finfet-technologies/
[2] https://engineering.purdue.edu/gekcogrp/publications/theses/PhD_17_2014_Mehdi_Salmani_Jelodar_thesis.pdf
[3] https://escholarship.org/content/qt37383183/qt37383183.pdf
[4] https://eureka.patsnap.com/report-how-to-reduce-leakage-current-in-finfet-devices
[5] https://pmc.ncbi.nlm.nih.gov/articles/PMC11509352/
[6] https://pmc.ncbi.nlm.nih.gov/articles/PMC12388639/
[7] https://vixra.org/pdf/2401.0029v1.pdf
[8] https://www.mdpi.com/2079-9292/14/15/2937
[9] https://www.nature.com/articles/s41598-025-19866-y
[10] https://www.physicsjournal.in/archives/2024/vol6issue1/PartB/7-1-47-600.pdf
[11] https://www.researchgate.net/publication/224439682_Leakage-Delay_Tradeoff_in_FinFET_Logic_Circuits_A_Comparative_Analysis_With_Bulk_Technology
[12] https://www.sciencedirect.com/science/article/abs/pii/S0026269216302427
[13] https://www.sciencedirect.com/science/article/pii/S2772671125000415