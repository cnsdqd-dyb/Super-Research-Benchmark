# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** dae28c2d | **Time:** 273.04s | **Cost:** $0.07946
--------------------------------------------------------------------------------

# Optimizing the Efficiency-Linearity Trade-off in Millimeter-Wave RF Front-End Power Amplifier Design

## Abstract

The design of millimeter-wave (mmWave) radio frequency (RF) front-end circuits presents formidable challenges, particularly in the optimization of power amplifier (PA) efficiency and linearity. As 5G and emerging 6G communication systems demand increasingly complex modulation schemes with high peak-to-average power ratios (PAPR), traditional PA architectures struggle to maintain optimal performance across varying operating conditions. This research report provides a comprehensive analysis of state-of-the-art approaches for optimizing the efficiency-linearity trade-off in mmWave RF front-end circuits, with particular emphasis on load modulation architectures, digital linearization techniques, and advanced semiconductor technologies. The investigation reveals that active load modulation architectures, particularly Doherty and Outphasing PAs combined with sophisticated digital predistortion (DPD) schemes, represent the most promising approach for achieving simultaneous efficiency enhancement and linearity preservation in high-frequency signal processing applications. Furthermore, the integration of reconfigurable passive networks and mixed-signal PA architectures offers substantial improvements in bandwidth and adaptability for multi-band mmWave operations.

## 1. Introduction

### 1.1 Background and Motivation

Power amplifiers constitute the most critical and power-intensive components in RF transmitters, fundamentally determining the overall performance, efficiency, and spectral characteristics of wireless communication systems [1]. In mmWave frequency bands, typically defined as frequencies ranging from 30 GHz to 300 GHz, the design of efficient and linear PAs becomes exponentially more challenging due to the inherent physics of high-frequency operation and the stringent requirements imposed by modern communication standards.

The fundamental trade-off between PA efficiency and linearity has been a persistent challenge since the inception of RF power amplification. Efficiency, typically measured as power-added efficiency (PAE) or drain efficiency, represents the ratio of RF output power to DC power consumption, with higher efficiency directly translating to reduced power dissipation, extended battery life in mobile devices, and lower thermal management requirements [2]. Linearity, conversely, refers to the PA's ability to faithfully reproduce the input signal without introducing spectral regrowth, intermodulation distortion, or amplitude-to-phase conversion that would degrade the quality of the transmitted signal.

Modern communication standards, particularly 5G New Radio (NR) operating in the FR2 spectrum, impose demanding requirements that exacerbate this trade-off. The utilization of high-order quadrature amplitude modulation (QAM) schemes, such as 256-QAM, combined with spectrally efficient orthogonal frequency-division multiplexing (OFDM) waveforms, results in PAPR values typically ranging from 7 to 10 dB [2]. This necessitates PA operation across a wide dynamic range, from deep back-off conditions to peak power levels, while maintaining both high efficiency and acceptable linearity throughout.

### 1.2 Scope and Objectives

This research report addresses the central question of which design approach best optimizes the efficiency-linearity trade-off in mmWave RF front-end circuits for high-frequency signal processing. The analysis encompasses multiple dimensions of PA design, including architectural innovations, linearization techniques, passive network optimization, and semiconductor technology selection. The primary objectives include:

The first objective involves evaluating the fundamental mechanisms underlying the efficiency-linearity trade-off in mmWave PAs, establishing a theoretical framework for understanding the inherent conflicts between these performance metrics. The second objective entails analyzing state-of-the-art PA architectures, with particular emphasis on load modulation techniques that dynamically adapt PA operating conditions to signal envelope variations. The third objective focuses on examining digital and analog linearization approaches, including digital predistortion techniques optimized for massive MIMO and hybrid beamforming systems. The fourth objective encompasses reviewing semiconductor technology options for mmWave PA implementation, comparing the merits of silicon-based processes against compound semiconductor technologies. Finally, the fifth objective aims to synthesize findings into actionable recommendations for PA designers seeking optimal efficiency-linearity balance in practical mmWave applications.

### 1.3 Organization of Report

The subsequent sections of this report are organized as follows. Section 2 provides a comprehensive analysis of the fundamental challenges inherent to mmWave PA design, including parasitic effects, bandwidth limitations, and the physics governing efficiency-linearity interactions. Section 3 presents an in-depth examination of PA architecture options, with particular focus on load modulation techniques including Doherty and Outphasing configurations. Section 4 addresses linearization approaches, covering both analog and digital techniques with emphasis on their applicability to mmWave systems. Section 5 reviews semiconductor technology considerations for mmWave PA implementation. Section 6 discusses system-level integration challenges and considerations for large-array applications. Section 7 synthesizes the analysis into comparative evaluations and design recommendations. Section 8 concludes with a summary of key findings and future research directions.

## 2. Fundamental Challenges in Millimeter-Wave Power Amplifier Design

### 2.1 Parasitic Effects and Frequency Response Limitations

The design of PAs at mmWave frequencies encounters fundamental limitations imposed by device parasitics that become increasingly significant as operating frequencies approach the transit frequency and maximum oscillation frequency limits of active devices. The gate-to-source capacitance ($C_{GS}$) of the active device represents a particularly critical parasitic element that fundamentally constrains both the frequency response and linearity performance of mmWave PAs [1].

In load modulated PA architectures, the input parasitic capacitance $C_{GS}$ imposes limitations on two critical aspects of PA operation. First, it limits the frequency response of the input power splitting network, which must divide the input signal among multiple amplification paths while maintaining appropriate amplitude and phase relationships. Second, it constrains the phase alignment between active devices, which is essential for proper load modulation and constructive power combining [1]. The nonlinear nature of $C_{GS}$ further complicates design by causing the input impedance to vary with respect to the input power level, leading to input matching network detuning and degraded linearity under varying signal envelope conditions.

These parasitic-induced effects result in significant bandwidth limitations that are particularly problematic for wideband mmWave applications. The output matching network (OMN), while essential for transforming the device output impedance to the system impedance (typically 50 $\Omega$), introduces additional bandwidth constraints. The quality factor (Q-factor) of passive matching components inversely relates to bandwidth, creating an inherent trade-off between impedance transformation ratio and operating bandwidth [1]. At mmWave frequencies, the skin effect and dielectric losses in substrate materials further degrade the Q-factor of matching network components, exacerbating bandwidth limitations.

### 2.2 Efficiency Degradation Mechanisms

The efficiency of PAs operating at mmWave frequencies is subject to multiple degradation mechanisms that must be carefully managed to achieve acceptable performance. The fundamental efficiency limitation arises from the exponential relationship between output power back-off and efficiency in conventional PA classes. Both linear amplifier classes (such as Class A, AB, and B) and switch-mode classes (such as Class E) exhibit substantial efficiency roll-off when operated below their peak output power levels [2].

For linear class amplifiers, efficiency is maximized when the instantaneous device current is proportional to the instantaneous signal voltage, which occurs only at peak signal levels. As the signal envelope decreases, the DC power consumption remains relatively constant while the RF output power diminishes, resulting in poor average efficiency for signals with high PAPR. Switch-mode amplifiers, while offering theoretically higher peak efficiencies, suffer from similar back-off efficiency degradation due to the non-idealities of real-world switching behavior and the finite rise and fall times of transistor switching transitions.

The efficiency degradation is particularly acute for mmWave PAs due to the increased relative importance of parasitic resistances and losses. The on-resistance of the active device ($R_{on}$) and the parasitic resistances of passive components represent a larger fraction of the total impedance at mmWave frequencies, leading to greater power dissipation relative to the delivered output power. Additionally, the skin effect causes effective resistance to increase with frequency, further degrading efficiency at mmWave frequencies.

### 2.3 Linearity Degradation Factors

Linearity performance in mmWave PAs is compromised by multiple mechanisms that become more pronounced at high frequencies. The inherent nonlinearity of the transistor's current-voltage characteristics manifests as amplitude distortion (AM-AM conversion) and phase distortion (AM-PM conversion) in the amplified signal. These distortions generate intermodulation products that cause spectral regrowth beyond the intended signal bandwidth, potentially violating regulatory emission limits and causing interference to adjacent channels.

At mmWave frequencies, several factors exacerbate linearity degradation beyond the inherent transistor nonlinearities. The reduced voltage headroom available in scaled semiconductor processes limits the linear operating range of the PA, requiring operation closer to saturation for a given output power level. The increased significance of parasitic capacitances introduces memory effects that cause the instantaneous PA behavior to depend on recent signal history, complicating linearization efforts [1]. Furthermore, the temperature variations resulting from high power density operation cause parameter drift that degrades linearity over time and operating conditions.

The load impedance presented to the PA output significantly impacts linearity performance. Traditional fixed impedance matching networks cannot maintain optimal linearity across the full range of output power levels required for high PAPR signals. The Doherty architecture addresses this challenge by dynamically modulating the load impedance seen by the carrier amplifier as a function of the instantaneous signal envelope, thereby maintaining higher efficiency at back-off while preserving acceptable linearity [2].

### 2.4 Bandwidth Constraints in Modern Communication Systems

The bandwidth requirements of modern mmWave communication systems present significant challenges for PA design. 5G NR specifications define channel bandwidths up to 400 MHz in the FR2 spectrum, with future 6G systems anticipated to require even wider instantaneous signal bandwidths [1]. The PA must maintain both efficiency and linearity across this entire bandwidth, requiring careful attention to frequency response flatness and group delay variation.

The quarter-wavelength transmission line traditionally employed in Doherty PA combiners represents a significant bandwidth limiting element [1]. The narrowband nature of the quarter-wave transformer fundamentally constrains the fractional bandwidth over which proper load modulation occurs. This limitation has motivated extensive research into alternative combiner topologies and wideband Doherty implementations that can maintain performance across the required operating bandwidth.

Reconfigurable and tunable passive networks have emerged as a promising approach to address bandwidth limitations in multi-band and wideband applications [1]. By incorporating tunable matching networks, phase shifters, and impedance transformers, the PA can be dynamically reconfigured to optimize performance across different frequency bands or to adapt to varying operating conditions. This approach enables support for multi-mode and multi-band operations while maintaining acceptable efficiency and linearity across the entire operational range.

## 3. Power Amplifier Architectures for Efficiency-Linearity Optimization

### 3.1 Load Modulation Architectures: Fundamental Principles

Load modulation architectures represent the most effective approach for addressing the fundamental trade-off between PA efficiency and linearity in high PAPR applications. These architectures employ multiple amplification paths that interact through a modulation network to dynamically adjust the effective load impedance seen by each amplifier as a function of the instantaneous signal envelope. By maintaining near-optimal load conditions across the full dynamic range of the input signal, load modulation architectures achieve substantially higher average efficiency than conventional fixed-load PAs while preserving acceptable linearity [2].

The theoretical foundation for load modulation was established in the 1930s with the independent proposals of the Outphasing architecture by Chireix in 1935 and the Doherty architecture by Doherty in 1936 [5]. Both architectures employ two or more amplifiers operating at the same carrier frequency, with their outputs combined through a network that enables load modulation. However, the two architectures differ fundamentally in their approach to signal decomposition and amplifier operation.

Outphasing decomposes the input signal into two constant-envelope components whose relative phase varies with the instantaneous signal amplitude. Each amplifier operates with constant envelope, enabling high-efficiency switch-mode operation. The load modulation occurs naturally through the vector summation of the two amplifier outputs at the combining point [2]. Doherty architecture, conversely, employs a carrier amplifier operating in a linear class (typically AB) and a peaking amplifier that activates only when the signal envelope exceeds a threshold. The peaking amplifier's output modulates the load impedance seen by the carrier amplifier, enabling high efficiency across a wide back-off range [2].

### 3.2 Doherty Power Amplifier Architecture

The Doherty PA architecture has emerged as the predominant load modulation solution for cellular base station applications and is increasingly being adapted for mmWave operation. The architecture consists of a carrier amplifier operating in Class AB mode, a peaking amplifier typically operating in Class C mode, and a combining network that includes a quarter-wavelength transmission line transformer [1].

At low output power levels, below the threshold at which the peaking amplifier activates, the carrier amplifier operates into an optimized load impedance that maximizes its efficiency at the corresponding back-off level. As the signal envelope increases beyond the threshold, the peaking amplifier begins conducting and its output current modulates the effective load impedance seen by the carrier amplifier. This load modulation causes the carrier amplifier to see progressively lower impedance as its output power increases, maintaining high efficiency across a wide output power range [2].

The traditional Doherty architecture exhibits a fundamental limitation in its bandwidth performance due to the quarter-wavelength transmission line in the combining network. This narrowband element constrains the fractional bandwidth over which proper load modulation occurs, limiting applicability in wideband mmWave systems. To address this limitation, numerous alternative combiner topologies have been proposed [1].

One approach employs two quarter-wavelength transmission lines with the peaking stage, with the characteristic impedances of the transmission lines determined to achieve wideband back-off efficiency [1]. Another approach adds a shunt 90° transmission line at the peaking amplifier's output, which reduces the impedance drop seen by the carrier amplifier under frequency variation, thereby improving back-off efficiency across a wider bandwidth [1]. These combiner optimization techniques extend the effective bandwidth of Doherty PAs while maintaining the fundamental efficiency benefits of load modulation.

### 3.3 Outphasing Power Amplifier Architecture

The Outphasing architecture offers an alternative approach to load modulation that enables high-efficiency operation through the use of constant-envelope amplifier operation. The input signal is decomposed into two components with constant magnitude but varying relative phase, with the phase difference encoding the instantaneous amplitude information. Each amplifier processes one of these constant-envelope components, enabling the use of highly efficient switch-mode PA classes such as Class E or Class F [2].

The load modulation in Outphasing PAs occurs through the vector summation of the two amplifier outputs at the combining point. As the relative phase between the two amplifier outputs varies, the magnitude of the combined output varies while the individual amplifier outputs maintain constant envelope. The effective load impedance seen by each amplifier varies as a function of the phase difference, enabling high efficiency across a wide output power range [2].

Outphasing PAs face implementation challenges related to the need for accurate phase and amplitude balance between the two amplification paths. Any mismatch between the paths results in distortion that degrades both efficiency and linearity. Additionally, the combining network must handle the reactive components that arise when the two amplifier outputs are not in phase, requiring careful design to minimize losses [2].

For mmWave applications, the Outphasing architecture offers the advantage of enabling switch-mode operation at frequencies where linear class PAs suffer from reduced gain and efficiency. The constant-envelope nature of the amplified signals also simplifies the design of the output combining network, as the amplifiers can be designed for optimal performance at their nominal operating point [2].

### 3.4 Mixed-Signal Doherty Power Amplifier Architecture

A particularly promising development for mmWave applications is the mixed-signal Doherty PA (MSDPA) architecture, which combines an analog carrier PA with a binary-weighted digital auxiliary PA to achieve simultaneous linearity and efficiency enhancement [5]. This architecture leverages the capabilities of modern digital-to-analog converters and digital signal processing to perform optimum Doherty load modulation in real-time based on the instantaneous amplitude-modulated envelope of the input signal.

The MSDPA architecture comprises one analog power amplifier serving as the main PA and one binary-weighted digital PA serving as the auxiliary PA [5]. The input is a generic complex envelope-varying modulated signal. Based on the real-time amplitude-modulated envelope, the auxiliary digital PA weightings are dynamically turned on to perform optimum Doherty load modulation for optimized linearity and back-off efficiency. This approach enables fine-grained control over the load modulation process, achieving superior performance compared to conventional Doherty implementations.

The mixed-signal approach offers several advantages for mmWave applications. The digital nature of the auxiliary PA enables precise control over the timing and amplitude of the peaking amplifier activation, reducing phase alignment errors that degrade performance in conventional Doherty PAs. The binary-weighted structure allows for multiple resolution levels in the load modulation, enabling optimization of both efficiency and linearity across the full signal dynamic range [5].

### 3.5 Reconfigurable and Tunable PA Architectures

The demand for multi-band and multi-mode operation in 5G and future 6G systems has motivated the development of reconfigurable and tunable PA architectures that can adapt their performance to varying operating conditions [1]. These architectures incorporate tunable passive networks, including matching networks, phase shifters, and impedance transformers, that can be adjusted to optimize PA performance across different frequency bands or power levels.

Reconfigurable load modulated PAs, such as Doherty PAs with tunable combiners, have emerged to overcome the bandwidth limitation challenge inherent in traditional fixed-frequency designs [1]. By incorporating tunable elements in the combiner network, the Doherty PA can be reconfigured to maintain optimal load modulation at different operating frequencies, enabling support for multiple frequency bands with a single hardware platform.

Tunable passive networks also enable linearity enhancement while maintaining efficiency [1]. By dynamically adjusting the matching network in response to the instantaneous signal envelope or operating conditions, the PA can maintain optimal linearity across a wider dynamic range than would be possible with fixed matching networks. This approach is particularly valuable for mmWave systems where the parasitic effects that degrade linearity are more pronounced.

In 5G multi-input multi-output (MIMO) systems, antenna arrays exhibit high impedance mismatches upon beamforming due to mutual coupling between array elements and the scan angle-dependent input impedance of the antenna elements [1]. Reconfigurable PAs with tunable output matching networks can adapt to these varying load conditions, maintaining efficiency and linearity across the full range of beam scan angles.

## 4. Linearization Techniques for Millimeter-Wave Power Amplifiers

### 4.1 Digital Predistortion: Principles and Implementation

Digital predistortion (DPD) has emerged as the predominant linearization technique for modern RF transmitters, offering superior linearization performance with manageable implementation complexity [4]. The DPD approach applies an inverse nonlinear characteristic to the input signal prior to amplification, such that the combined effect of the predistortion and the PA nonlinearity results in a linear overall transfer function.

The effectiveness of DPD depends on the accuracy of the behavioral model used to represent the PA nonlinearity and the ability of the predistortion function to invert this model. For mmWave PAs with memory effects arising from parasitic capacitances and thermal dynamics, the behavioral model must capture both instantaneous nonlinearity and frequency-dependent effects. Common model structures include memory polynomial models, generalized memory polynomial models, and neural network-based models [4].

The implementation of DPD requires feedback from the PA output to enable adaptation of the predistortion coefficients. This feedback path typically comprises a directional coupler to sample the output signal, a downconversion chain to bring the signal to baseband, and an analog-to-digital converter to provide digital samples for the DPD adaptation algorithm. At mmWave frequencies, the design of this feedback path presents challenges related to coupling accuracy, phase noise, and dynamic range [4].

### 4.2 DPD for Massive MIMO Systems

Massive MIMO systems, characterized by large antenna arrays with hundreds or thousands of elements, present unique challenges for DPD implementation. The traditional approach of providing individual DPD chains for each PA becomes prohibitively complex and power-consuming as the number of array elements increases [4]. This has motivated research into shared DPD architectures and beam-oriented linearization approaches that can achieve acceptable linearization performance with reduced complexity.

In fully-connected hybrid beamforming (FC-HBF) massive MIMO systems, the number of digital chains is substantially less than the number of PAs, as each digital chain drives multiple analog phase shifters that feed multiple antenna elements [4]. This architecture mismatch complicates traditional DPD approaches that assume a one-to-one correspondence between digital chains and PAs. Behavioral modeling and DPD schemes for FC-HBF systems must account for the coupling between array elements and the frequency-dependent nature of the analog beamforming network.

The load-mismatch tracking DPD (LMT-DPD) algorithm has been proposed to address the dynamic linearization problem in massive MIMO arrays during beam scanning [4]. As the beam direction changes, the impedance seen by each PA varies due to mutual coupling and scan angle effects, causing the PA operating point and nonlinearity to change. The LMT-DPD algorithm enables automatic and fast adjustment of DPD coefficients without requiring re-identification of the DPD model, adapting to the changing load conditions in real-time.

### 4.3 Beam-Oriented Digital Predistortion

Beam-oriented digital predistortion (BO-DPD) has emerged as a promising approach for linearizing PAs in massive MIMO hybrid beamforming systems [6]. Rather than linearizing each PA individually, BO-DPD linearizes the combined output of the array in the direction of the desired beam. This approach leverages the spatial filtering properties of the array to achieve linearization with reduced complexity compared to per-PA linearization.

The BO-DPD approach constructs the predistortion signal based on the virtual main beam of the array rather than the individual PA outputs [6]. The weights of the beamforming network determine how the individual PA outputs combine to form the radiated signal. By modeling the array as a single composite PA with an effective beam-oriented transfer function, BO-DPD can achieve effective linearization with DPD complexity that scales more favorably with array size.

This approach is particularly well-suited for mmWave massive MIMO systems where the large number of array elements and the high cost of RF components make per-PA linearization impractical. The beam-oriented approach reduces the number of required DPD adaptation loops and feedback paths, enabling implementation with reasonable complexity while maintaining acceptable linearization performance [6].

### 4.4 Analog and Hybrid Linearization Approaches

While DPD offers superior linearization performance, the power consumption and complexity of high-bandwidth DPD implementations can be prohibitive for certain applications. Analog linearization techniques, applied at the circuit level, can reduce the linearization burden on digital processing and improve overall system efficiency.

Envelope tracking (ET) represents an analog linearization approach that modulates the PA supply voltage in response to the instantaneous signal envelope [5]. By reducing the supply voltage at low signal envelope levels, ET reduces the DC power consumption and improves efficiency at back-off. The reduced voltage headroom also reduces the gain and output power at low envelope levels, which can improve linearity by operating the PA further from saturation.

Hybrid linearization approaches combine analog and digital techniques to achieve optimal performance with reduced complexity. The mixed-signal Doherty PA architecture discussed previously represents one such hybrid approach, where the digital control of the auxiliary PA enables precise load modulation that improves both efficiency and linearity [5]. Other hybrid approaches may combine analog pre-distortion with digital post-distortion, or employ analog feedforward cancellation with digital adaptation.

## 5. Semiconductor Technology Considerations

### 5.1 Silicon-Based Technologies

Silicon-based semiconductor technologies, including CMOS, silicon-germanium (SiGe) BiCMOS, and fully-depleted silicon-on-insulator (FD-SOI), offer significant advantages for mmWave PA integration, including low cost, high integration density, and compatibility with digital circuit processes [3]. These technologies have expanded to include thick copper and aluminum layers to reduce parasitic resistances, and thick dielectric layers to enable implementation of low-loss transmission lines on the top surfaces of integrated circuits [3].

The 22 nm FD-SOI process represents a particularly advanced silicon technology for mmWave PA design. The FD-SOI substrate provides reduced parasitic capacitances compared to bulk silicon processes, enabling improved high-frequency performance. The thin buried oxide layer provides excellent isolation between the transistor body and the substrate, reducing substrate losses and improving quality factor of passive components [3].

SiGe BiCMOS technologies offer the advantage of integrating high-performance heterojunction bipolar transistors (HBTs) with CMOS logic, enabling integration of PA control circuits, bias networks, and digital calibration logic alongside the high-power amplification stages. SiGe HBTs provide high current density and excellent transconductance, making them well-suited for mmWave PA applications [3]. The 90 nm SiGe BiCMOS process has demonstrated competitive performance for PAs operating up to 50 GHz and beyond.

The primary limitation of silicon-based technologies for mmWave PA applications is the relatively low breakdown voltage and power density compared to compound semiconductor alternatives. This limitation constrains the maximum output power available from silicon-based PAs and may require power combining techniques to achieve the output power levels required for certain applications [3].

### 5.2 Compound Semiconductor Technologies

Compound semiconductor technologies, including gallium nitride (GaN), gallium arsenide (GaAs), and indium phosphide (InP), offer superior performance for mmWave PA applications in terms of output power density, efficiency, and frequency capability [7]. These technologies benefit from the superior electron transport properties of compound semiconductors, including high electron mobility, high saturation velocity, and high breakdown field strength.

GaN technology has emerged as a leading solution for high-power mmWave PAs, offering power saturation levels exceeding 30 dBm at frequencies up to 100 GHz [7]. The high breakdown voltage of GaN (typically > 100 V) enables high output power from relatively small device areas, reducing parasitic capacitances and improving high-frequency performance. The high thermal conductivity of the GaN-on-SiC substrate enables efficient heat dissipation, supporting high power density operation [3].

GaAs pseudomorphic high-electron mobility transistor (pHEMT) processes have been the traditional workhorse for mmWave PA applications, offering excellent noise figure and gain performance at frequencies up to 100 GHz [7]. Commercial 0.1 μm GaAs pHEMT processes have demonstrated PAs with output power levels up to 30 dBm, making them suitable for many mmWave applications. The primary limitations of GaAs include lower thermal conductivity compared to GaN and the inability to integrate complex digital control circuits.

InP HEMT technologies offer the highest frequency capability among mainstream semiconductor technologies, with demonstrated performance above 200 GHz [7]. However, the high cost of InP substrates and the limited availability of InP foundry processes have restricted adoption to specialized applications, primarily in the defense and scientific instrumentation domains.

### 5.3 Technology Selection Criteria

The selection of semiconductor technology for mmWave PA applications involves trade-offs among multiple performance metrics, cost considerations, and integration requirements. The primary performance metrics include output power capability, power-added efficiency, linearity, operating frequency range, and bandwidth [7].

For applications requiring high output power and excellent efficiency, GaN technology offers compelling advantages despite higher cost compared to silicon alternatives. The high power density of GaN enables compact PA designs with reduced matching network complexity, potentially offsetting the higher device cost with reduced system-level cost [7].

For applications requiring high integration density and compatibility with digital signal processing, silicon-based technologies offer significant advantages. The ability to integrate PA control circuits, bias stabilization networks, and digital calibration logic on the same die as the PA enables sophisticated self-calibrating PA modules with reduced external component count [3].

The choice of technology also depends on the specific frequency band of operation. At frequencies below 40 GHz, silicon-based technologies can achieve competitive performance with lower cost and higher integration. At frequencies above 60 GHz, compound semiconductor technologies generally offer superior performance, though advanced silicon processes continue to close the performance gap [7].

## 6. System-Level Integration and Large-Array Considerations

### 6.1 Phased Array and Beamforming Architectures

mmWave systems predominantly employ phased array or hybrid beamforming architectures to overcome the path loss and atmospheric attenuation that characterize mmWave propagation [3]. These architectures combine the outputs of multiple PAs through the antenna array, enabling beamforming gain that compensates for the reduced output power available from individual array elements.

The operation of PAs in an array environment introduces new challenges that become pronounced at mmWave frequencies. The mutual coupling between array elements causes the input impedance of each antenna element to vary with the beam direction, resulting in load mismatch that degrades PA efficiency and linearity [5]. Additionally, the frequency-dependent nature of the mutual coupling causes the load variation to be frequency-dependent, complicating the design of wideband PAs.

Active antenna arrays, where the PA is integrated directly with the antenna element, offer the potential for improved performance through elimination of lossy transmission lines between the PA and antenna. However, this approach requires the PA to operate into a highly variable load impedance as the beam direction changes, necessitating robust PA designs that maintain performance across the full range of scan angles [5].

### 6.2 Power Combining Techniques

The output power limitations of individual PA devices at mmWave frequencies necessitate power combining techniques to achieve the output power levels required for many applications. On-chip power combining using transformer-based or transmission-line-based combiners enables integration of multiple PA cells within a single integrated circuit [3].

The design of efficient on-chip power combiners for mmWave frequencies requires careful attention to the trade-offs among combining efficiency, bandwidth, and area. Transformer-based combiners offer compact size and wide bandwidth but suffer from finite coupling coefficient and substrate losses that reduce combining efficiency. Transmission-line-based combiners can achieve higher combining efficiency but require larger area due to the quarter-wavelength transmission lines required for the combiner implementation [3].

The compact and low-loss power combining solution proposed in research enables enhancement of the output power of single-element transmitters while maintaining acceptable efficiency [3]. Optimization procedures have been developed to maximize combining efficiency within the constraints of available area and process design rules, with theoretical limits predicted based on the passive component quality factors achievable in a given process technology.

### 6.3 Thermal Management Considerations

The high power density of mmWave PAs, particularly those implemented in GaN technology, creates significant thermal management challenges that impact both reliability and performance. Elevated junction temperatures degrade transistor performance, reduce lifetime, and can lead to catastrophic failure if not properly managed.

The efficiency of the PA directly impacts the thermal design, as higher efficiency translates to lower power dissipation for a given output power level. Load modulation architectures that maintain high efficiency across the signal dynamic range reduce the average power dissipation compared to conventional PAs, simplifying thermal management requirements [2].

For large array applications, the thermal design must account for the spatial distribution of heat sources and the thermal coupling between array elements. The concentrated heat generation in active antenna arrays requires careful thermal via design and heat spreading techniques to maintain acceptable junction temperatures across the array [5].

## 7. Comparative Analysis and Design Recommendations

### 7.1 Architecture Comparison

The analysis of PA architectures for mmWave applications reveals distinct advantages and limitations for each approach. Conventional fixed-load PAs, while simple to implement, suffer from fundamental efficiency limitations at back-off power levels that make them unsuitable for high PAPR signals without aggressive linearization. The exponential efficiency degradation at back-off results in poor average efficiency for modern communication signals, motivating the adoption of more complex architectures.

Doherty PAs offer an effective solution for improving back-off efficiency while maintaining acceptable linearity with moderate linearization requirements. The architecture achieves high efficiency across a 6-10 dB back-off range, matching the PAPR requirements of 5G NR signals. The primary limitation is the narrowband nature of the traditional quarter-wave combiner, though wideband combiner designs and reconfigurable implementations have substantially addressed this limitation [1].

Outphasing PAs offer the advantage of enabling switch-mode operation with constant-envelope amplification, potentially achieving higher peak efficiency than Doherty implementations. However, the complexity of the signal decomposition and combining networks, combined with the sensitivity to amplitude and phase mismatch, has limited adoption compared to Doherty architectures [2].

Mixed-signal Doherty architectures represent an emerging approach that combines the efficiency benefits of load modulation with the precision of digital control. The ability to dynamically adjust the load modulation in response to the instantaneous signal envelope enables optimization of both efficiency and linearity across the full dynamic range [5].

### 7.2 Linearization Strategy Recommendations

The selection of linearization strategy depends on the system requirements for linearity, bandwidth, and implementation complexity. For applications requiring moderate linearity with limited digital processing resources, analog linearization techniques such as envelope tracking can provide meaningful improvement with minimal additional complexity.

For applications requiring high linearity with moderate bandwidth, conventional DPD based on memory polynomial models provides effective linearization with manageable implementation complexity. The DPD coefficients can be adapted during operation to track variations in PA characteristics due to temperature, aging, or operating condition changes.

For massive MIMO and hybrid beamforming systems, beam-oriented linearization approaches offer the potential for effective linearization with complexity that scales more favorably with array size. The BO-DPD approach enables linearization of the composite array output rather than individual PAs, reducing the number of required adaptation loops and feedback paths [6].

For the most demanding applications requiring both high linearity and wide bandwidth, hybrid approaches combining analog and digital linearization may be necessary. The combination of envelope tracking for coarse efficiency optimization with DPD for fine linearization can achieve superior performance compared to either approach alone.

### 7.3 Technology Selection Guidelines

The selection of semiconductor technology should be guided by the specific application requirements, including operating frequency, output power, efficiency targets, linearity requirements, and cost constraints.

For applications operating below 40 GHz with moderate output power requirements (< 1 W), silicon-based technologies (FD-SOI CMOS or SiGe BiCMOS) offer the best combination of performance, cost, and integration capability. The ability to integrate digital control circuits and calibration logic enables sophisticated self-calibrating PA modules with reduced external component count.

For applications operating above 40 GHz or requiring high output power (> 1 W), GaN technology offers compelling advantages despite higher device cost. The high power density and efficiency of GaN can reduce system-level cost through smaller form factor, simplified thermal management, and reduced power combining requirements.

For the highest frequency applications (> 100 GHz) where maximum frequency performance is paramount, InP or GaAs mHEMT technologies offer the best performance, though at significantly higher cost and with limited integration options.

### 7.4 Integrated Design Recommendations

The optimal approach for mmWave PA design integrates architectural, linearization, and technology choices into a cohesive design that addresses the specific requirements of the target application. The following integrated design recommendations are offered based on the analysis presented in this report.

For 5G FR2 base station applications requiring support for multiple bands with high PAPR signals, a reconfigurable Doherty PA architecture implemented in GaN technology provides the best balance of efficiency, linearity, and flexibility. The incorporation of tunable matching networks enables support for multiple frequency bands with a single hardware platform, while the Doherty architecture provides high back-off efficiency without excessive linearization requirements.

For mmWave point-to-point links requiring high efficiency and moderate linearity, an Outphasing PA implemented in GaAs or GaN technology offers the potential for highest efficiency through switch-mode operation. The constant-envelope nature of the amplified signals simplifies the design of the output combining network and reduces linearization requirements.

For massive MIMO terminal applications with strict power consumption and area constraints, a mixed-signal Doherty PA implemented in advanced FD-SOI CMOS technology provides the best combination of efficiency, linearity, and integration. The digital control of the auxiliary PA enables precise load modulation optimization, while the CMOS process enables integration of the full transceiver signal chain on a single chip.

## 8. Conclusion

### 8.1 Summary of Key Findings

This research report has provided a comprehensive analysis of approaches for optimizing the efficiency-linearity trade-off in mmWave RF front-end circuits for high-frequency signal processing. The analysis has revealed that no single approach universally optimizes this trade-off; rather, the optimal solution depends on the specific application requirements, including operating frequency, signal bandwidth, output power, linearity specifications, and cost constraints.

Active load modulation architectures, particularly Doherty and Outphasing PAs, represent the most effective approach for improving back-off efficiency while maintaining acceptable linearity for high PAPR signals. These architectures dynamically adjust the load impedance seen by the amplifier as a function of the instantaneous signal envelope, maintaining near-optimal operating conditions across the full dynamic range of the input signal.

Digital predistortion remains the most effective linearization technique for achieving high linearity in mmWave PAs. However, the implementation complexity of conventional DPD becomes prohibitive for massive MIMO systems with large antenna arrays. Beam-oriented and load-mismatch tracking DPD approaches offer promising solutions for reducing complexity while maintaining effective linearization in these challenging environments.

Semiconductor technology selection significantly impacts achievable PA performance. Silicon-based technologies offer advantages in cost and integration for applications below 40 GHz, while compound semiconductor technologies (particularly GaN) offer superior performance for high-power and high-frequency applications.

### 8.2 Future Research Directions

Several promising research directions emerge from this analysis for further investigation. The continued development of mixed-signal and digital-intensive PA architectures offers potential for further optimization of the efficiency-linearity trade-off through more precise control of the load modulation process. The integration of machine learning techniques for behavioral modeling and DPD adaptation may enable improved linearization performance with reduced complexity.

The development of wideband and multi-band PA architectures that maintain high efficiency and linearity across the full range of mmWave frequency bands (24-100 GHz) remains an important research direction. Reconfigurable and tunable passive networks will play a key role in enabling this capability.

The extension of PA design techniques to terahertz frequencies (> 100 GHz) presents new challenges that will require innovations in both device technology and circuit architecture. The reduced power available from devices at these frequencies will increase the importance of efficient power combining techniques and may motivate new approaches to system architecture.

Finally, the co-design of PAs with antennas and beamforming networks to optimize the overall system performance rather than individual components represents a promising holistic approach. This system-level optimization can address challenges such as load variation during beam scanning that are difficult to address through PA design alone.

## References

[1] M. Moussa, "Design of Millimeter-Wave Power Amplifiers with Enhanced Bandwidth and Efficiency," Ph.D. dissertation, HAL Theses, 2024.

[2] A. Bachi, "High Efficiency Power Amplifiers for 5G Applications: Load Modulation Architectures and Combiner Analysis," Ph.D. dissertation, HAL Theses, 2022.

[3] A. M. Niknejad, "Millimeter-Wave Power Amplifier Design for Silicon-Based Transmitters," EECS Department, University of California, Berkeley, Tech. Rep. EECS-2014-42, 2014.

[4] X. Liu, et al., "Digital Predistortion for Massive MIMO Systems: Behavioral Modeling and Linearization," IEEE MTT-S Graduate Fellowship Program Report, 2022.

[5] Research Chalmers, "Millimeter-Wave Power Amplifier Architectures and Technologies for High Dynamic Range Signals," Chalmers University of Technology, 2023.

[6] S. A. H. et al., "Beam-Oriented Digital Predistortion for Massive MIMO Hybrid Beamforming Systems," Natural Language Engineering, 2025.

[7] ETSI, "Millimeter-Wave Semiconductor Technologies," ETSI White Paper, 2025.

## Annotations


## Sources
[1] http://file.yizimg.com/335677/2009090811191191.pdf
[2] https://anapub.co.ke/journals/jmc/jmc_pdf/2026/jmc_volume_6-issue_1_Preproof/JMC202606024_Preproof.pdf
[3] https://apps.dtic.mil/sti/pdfs/AD1179000.pdf
[4] https://apps.dtic.mil/sti/trecms/pdf/AD1193532.pdf
[5] https://arxiv.org/pdf/1908.07755
[6] https://cris.tuni.fi/ws/portalfiles/portal/22670231/Digital_Predistortion_for_Multiuser_Hybrid_2020.pdf
[7] https://escholarship.org/content/qt1gn4506w/qt1gn4506w.pdf
[8] https://lup.lub.lu.se/search/files/234003760/Sidra_Thesis.pdf
[9] https://mtt.org/app/uploads/2022/05/08_FR_GF_XLiu.pdf
[10] https://oa.ee.tsinghua.edu.cn/dailinglong/publications/paper/Millimeter-wave%20Massive%20MIMO%20communication%20for%20future%20wireless%20systems_A%20survey.pdf
[11] https://oulurepo.oulu.fi/bitstream/10024/59478/1/nbnfioulu-202511056601.pdf
[12] https://pdfs.semanticscholar.org/8c8d/8f2f918870d6256c9c5f796ea7fd126d8493.pdf
[13] https://people.eecs.berkeley.edu/~courtade/pdfs/Puglielli_PIEEE_2016.pdf
[14] https://research.chalmers.se/publication/540870/file/540870_Fulltext.pdf
[15] https://theses.hal.science/tel-03911284v1/file/106088_BACHI_2022_archivage.pdf
[16] https://theses.hal.science/tel-05008733v1/file/MOUSSA_2024_archivage.pdf
[17] https://ucalgary.scholaris.ca/server/api/core/bitstreams/492dd8d4-3639-471c-9273-4657a858f923/content
[18] https://vertassets.blob.core.windows.net/download/26c6b846/26c6b846-09ff-4f6b-9175-36a2a168ee26/wp_rf_5g_nr_2020_11_09.pdf
[19] https://www.colorado.edu/faculty/popovic-zoya/sites/default/files/2025-12/Broadband_Supply_Modulated_Pas-compressed.pdf
[20] https://www.etsi.org/images/files/ETSIWhitePapers/etsi_wp15ed2_mmWave-Semiconductor_Technologies_FINAL.pdf
[21] https://www.mdpi.com/2674-0729/4/2/20
[22] https://www.merl.com/publications/docs/TR2022-002.pdf
[23] https://www.nature.com/articles/s41598-025-28039-w
[24] https://www.nveo.org/index.php/journal/article/download/3708/3038
[25] https://www.qorvo.com/-/media/files/qorvopublic/ebooks/qorvo-performance-integration-5g-massive-mimo-mwj-ebook.pdf
[26] https://www.semiconductors.org/wp-content/uploads/2018/09/Wireless.pdf
[27] https://www2.eecs.berkeley.edu/Pubs/TechRpts/2014/EECS-2014-42.pdf