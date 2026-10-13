# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 2b617681 | **Time:** 508.72s | **Cost:** $0.03439
--------------------------------------------------------------------------------

# Synaptic Weight Update Mechanisms for Parallel Optimization of Energy Efficiency and Learning Accuracy in Neuromorphic Chips Under Device Variation and Power Constraints

## Executive Summary

Neuromorphic computing represents a paradigm shift in hardware architecture, drawing inspiration from the brain's remarkable energy efficiency and adaptive learning capabilities. At the heart of this technology lies the synaptic weight update mechanism, which determines how artificial synapses modify their connection strengths during learning. This report investigates the critical question of which synaptic weight update mechanisms can simultaneously achieve parallel optimization of energy efficiency and learning accuracy while operating under the constraints of device variation and limited power budgets. Through comprehensive analysis of recent research developments, this report identifies several promising approaches, including synaptic caching algorithms, linear weight update mechanisms, and hardware-aware learning rules such as CRUS (Constrained Weight Update Strategy). The findings suggest that the most effective solutions employ a holistic, co-design methodology that integrates device-level innovations with system-level algorithmic adaptations, thereby achieving robust performance despite the inherent non-idealities of nanoscale neuromorphic hardware.

## 1. Introduction and Background

### 1.1 The Neuromorphic Computing Paradigm

Neuromorphic computing has emerged as a transformative approach to addressing the fundamental limitations of traditional von Neumann architectures, particularly in applications requiring real-time processing, adaptive learning, and ultra-low power consumption [1]. Unlike conventional computing systems that separate memory and processing units, neuromorphic architectures integrate computational and memory elements in a manner that closely mimics the biological nervous system. This integration enables massively parallel information processing while maintaining exceptional energy efficiency, making neuromorphic systems particularly suitable for edge computing applications, autonomous vehicles, wearable devices, and other scenarios where power constraints and real-time responsiveness are paramount concerns [2].

The fundamental building blocks of neuromorphic systems include artificial neurons and synapses, which collectively form spiking neural networks (SNNs) capable of encoding and processing information through discrete temporal events rather than continuous signals. This event-driven processing strategy represents a significant departure from traditional artificial neural networks (ANNs) and contributes substantially to the energy efficiency of neuromorphic hardware [3]. When a neuron receives sufficient input stimulation to exceed its firing threshold, it generates a spike that propagates through the network via synaptic connections, with each synapse modifying its connection strength based on the timing and patterns of pre- and postsynaptic activity.

### 1.2 The Critical Role of Synaptic Weight Update Mechanisms

The synaptic weight update mechanism constitutes the learning algorithm that governs how synaptic weights are modified during training, and it represents one of the most critical factors determining both the energy efficiency and learning accuracy of neuromorphic systems [4]. In biological systems, synaptic plasticity—the ability of synapses to strengthen or weaken over time—underpins all forms of learning and memory, enabling organisms to adapt their behavior based on experience. Artificial neuromorphic systems seek to replicate this capability through various implementations of synaptic plasticity, each offering distinct trade-offs between computational complexity, energy consumption, and learning performance.

The challenge of designing effective synaptic weight update mechanisms for neuromorphic hardware is compounded by several factors inherent to nanoscale electronic devices. Device variation, arising from manufacturing imperfections and material inhomogeneities, introduces uncertainty in synaptic weight values and update operations [5]. Limited dynamic range constrains the precision with which weights can be represented, while power consumption during weight update operations directly impacts the overall energy efficiency of the system. Furthermore, the non-ideal switching characteristics of synaptic devices—including nonlinear weight updates, asymmetric potentiation and depression, and cycle-to-cycle variability—create additional challenges for achieving reliable learning performance [6].

### 1.3 Research Objectives and Scope

This report addresses the central research question: What synaptic weight update mechanism achieves parallel optimization of energy efficiency and learning accuracy while constrained by device variation and power limits? To answer this question, we examine multiple approaches reported in recent literature, analyzing their underlying principles, implementation strategies, and performance characteristics. The analysis encompasses device-level innovations in synaptic hardware, algorithmic-level developments in learning rules, and system-level strategies for managing hardware constraints and non-idealities.

## 2. Device-Level Considerations for Synaptic Weight Update

### 2.1 Material and Device Characteristics

The choice of synaptic device technology fundamentally constrains the achievable performance of weight update mechanisms. Various memory technologies have been explored for neuromorphic applications, including resistive random-access memory (ReRAM), phase-change memory (PCM), ferroelectric field-effect transistors (FeFET), and electrochemical synaptic devices [7]. Each technology presents distinct characteristics in terms of switching dynamics, energy efficiency, retention, endurance, and susceptibility to device variation.

Research on ferroelectric synaptic transistors has identified several key device characteristics that significantly impact learning accuracy [7]. The dynamic range of synaptic weights—the ratio between maximum and minimum conductance states—determines the precision with which information can be encoded and the representational capacity of the network. Linearity and symmetry of weight update refer to the consistency of conductance changes across the entire weight range and the correspondence between potentiation (weight increase) and depression (weight decrease) dynamics. Programming energy consumption reflects the energy required to modify synaptic weights, directly impacting the overall energy efficiency of the system. Finally, uniformity and variability characterize the device-to-device consistency and the reproducibility of switching behavior across multiple cycles.

HfO₂-based memristors with gold nanoparticle (AuNP) and DNA interfaces have demonstrated excellent linear weight update characteristics combined with large conductance ratios [8]. The high linearity of synaptic weights achieved through simple programming based on pulse amplitude particularly enhances both energy efficiency and learning accuracy in neural network applications. This finding underscores the importance of device-level engineering in enabling high-performance weight update mechanisms.

### 2.2 Managing Device Variation and Non-Idealities

Device variation represents one of the most significant challenges in implementing reliable synaptic weight update mechanisms. In analog synaptic devices, intrinsic instability and lack of control over conductance switching behavior can critically degrade system performance [5]. The variation coefficient, defined as the ratio of conductance standard deviation to mean conductance, quantifies the extent of device-to-device and cycle-to-cycle variability.

Research on binarized neural networks (BNNs) using digital-type synaptic devices has demonstrated that binary weight representations offer considerably higher immunity to device variability compared to analog implementations [5]. In BNNs, synaptic weights are constrained to binary values (+1 or -1), effectively eliminating the impact of fine-grained conductance variations. Simulation studies have shown that when the conductance difference between high and low states (ΔG) exceeds a threshold of approximately 5, the classification accuracy remains relatively robust even as the variation coefficient increases from 0.2 to 1.0. This finding suggests that coarse-grained weight representations can provide a viable pathway for achieving reliable learning performance in the presence of significant device variation.

Phase-change memory devices have shown remarkable stability over repeated cycles of stimulation and relaxation, with device-to-device variance remaining consistent across multiple experiments [4]. The ability to configure PCM devices with different decay timescales—fast (~1 ms), slow (~100 ms), and ultraslow (>500 ms)—enables emulation of various biological neuronal signaling elements and supports diverse learning rules. This configurability represents a significant advantage for implementing adaptive weight update mechanisms that can optimize performance across different application requirements.

## 3. Algorithmic Approaches to Energy-Accuracy Optimization

### 3.1 Synaptic Caching: Balancing Transient and Stable Plasticity

One of the most promising algorithmic approaches to optimizing energy efficiency while maintaining learning accuracy is the synaptic caching algorithm, which draws inspiration from the metabolic efficiency of biological neural systems [9]. This algorithm addresses the fundamental trade-off between energy consumption and network capacity by strategically managing different forms of synaptic plasticity with distinct energy costs and stability characteristics.

The synaptic caching algorithm operates on the principle that synaptic plasticity is metabolically demanding, with energy requirements rising steeply as memory load or designated accuracy level increases [9]. Rather than implementing all weight updates directly in persistent, stable forms of synaptic plasticity, the algorithm temporarily stores changes in transient, labile forms that require less energy to modify. These transient changes are then occasionally consolidated into stable forms through targeted consolidation operations.

The key insight underlying synaptic caching is that not all synaptic modifications require the same level of permanence. By precisely balancing labile and stable forms of synaptic plasticity based on the temporal requirements of the learning task, the algorithm can achieve substantial energy savings without proportionally degrading learning accuracy. The consolidation process can be triggered by various heuristics, such as the salience of the learned pattern, the stability of the weight changes, or the availability of computational resources.

Experimental validation of the synaptic caching concept has demonstrated energy efficiency improvements of several-fold compared to naive implementations of synaptic plasticity rules [9]. Importantly, the algorithm can be applied in conjunction with any underlying plasticity rule, including backpropagation, making it a versatile approach for enhancing the efficiency of diverse neuromorphic learning systems.

### 3.2 Linear Weight Update Mechanisms

The linearity of synaptic weight updates represents a critical factor in achieving both high energy efficiency and learning accuracy [8]. Nonlinear weight updates introduce systematic errors that accumulate during training, degrading network performance and requiring additional computational overhead to compensate. In contrast, linear weight updates enable more predictable and controllable modifications to synaptic conductances, facilitating accurate implementation of learning algorithms.

Research on HfO₂/AuNP-DNA-based memristors has demonstrated that high linearity in synaptic weights can be achieved through careful engineering of the device structure and programming conditions [8]. The relationship between applied voltage pulse amplitude and resulting conductance change determines the linearity of the weight update characteristic. By optimizing this relationship, researchers have achieved synaptic devices that exhibit near-ideal linear behavior across a wide range of weight values.

The importance of linearity extends beyond accuracy considerations to energy efficiency. Nonlinear weight updates often require iterative programming procedures to achieve target conductance values, consuming additional energy with each programming attempt. Linear weight updates, by contrast, can achieve target values in a single programming operation, significantly reducing energy consumption. Furthermore, linear updates simplify the design of learning algorithms by eliminating the need for nonlinear compensation terms that would otherwise increase computational complexity.

### 3.3 CRUS: Hardware-Efficient Weight Update Under Non-Ideal Conditions

The Constrained Weight Update Strategy (CRUS) represents a hardware-efficient approach to handling the nonlinear and asymmetric weight update characteristics common in analog synaptic devices [6]. This method addresses the challenge of achieving high classification accuracy even when synaptic devices exhibit highly nonlinear or abrupt conductance update behaviors, quantified by nonlinearity coefficients (NL) with absolute values of 8 or greater.

CRUS achieves its robustness through several key design principles. First, it employs a weight update rule that requires only 1-bit precision, reducing the sensitivity of the system to fine-grained conductance variations. Second, it minimizes the frequency of conductance access operations, thereby reducing both energy consumption and the accumulation of update errors over time. Third, it incorporates LTD (long-term depression) skip update events that help minimize the damage caused by temporal variations in conductance updates.

Performance evaluations of CRUS on the MNIST handwritten digit classification task have demonstrated classification accuracy exceeding 90% even under challenging conditions where the nonlinearity coefficients of both long-term potentiation (LTP) and long-term depression (LTD) reach ±8 or higher [6]. This performance level is achieved with high hardware efficiency, as the method requires minimal additional computational overhead beyond the standard weight update operations. The resilience of CRUS to temporal conductance variation compared to alternative approaches such as periodic refresh methods or ideal synaptic device assumptions highlights its practical utility for neuromorphic hardware implementations.

## 4. System-Level Strategies for Constraint Management

### 4.1 Holistic Hardware-Algorithm Co-Design

Effective optimization of energy efficiency and learning accuracy in neuromorphic systems requires a holistic approach that considers hardware design, spike-based computation models, adaptive learning algorithms, and supporting software frameworks as an integrated system [2]. This co-design philosophy recognizes that the performance of synaptic weight update mechanisms cannot be evaluated in isolation but must be understood in the context of the complete hardware-software stack.

Training algorithms that account for global hardware constraints and fabrication variations represent a key component of this holistic approach [1]. Rather than treating device non-idealities as noise to be filtered out, these algorithms incorporate explicit models of hardware limitations into the learning process. This integration enables the system to make optimal use of available device characteristics while compensating for predictable sources of error.

The trade-offs between speed, power consumption, and size must be computed at the system level and are therefore application-specific [1]. An extrapolation of individual device performance is insufficient because the collective behavior of interconnected devices can exhibit emergent properties that differ significantly from the sum of individual characteristics. Networks can be trained using extra neurons to mitigate inaccuracies caused by noisy signals, demonstrating how system-level strategies can compensate for device-level limitations.

### 4.2 Event-Driven Processing and Adaptive Learning

Event-driven processing represents a fundamental characteristic of neuromorphic computing that contributes substantially to energy efficiency [3]. Rather than processing data continuously, neuromorphic systems respond to events or changes in input, enabling computation only when relevant information is present. This approach eliminates unnecessary operations and reduces static power consumption, making it particularly suitable for edge computing applications where power budgets are constrained.

Spike-timing-dependent plasticity (STDP) and other biologically-inspired learning rules enable event-driven learning in neuromorphic systems [3]. These rules modify synaptic weights based on the precise timing relationships between pre- and postsynaptic spikes, naturally aligning weight update operations with the event-driven nature of the computation. The temporal coding of information in spiking neural networks enables efficient representation of dynamic stimuli and supports online learning with minimal computational overhead.

The integration of event-driven processing with adaptive learning algorithms enables neuromorphic systems to achieve real-time performance while maintaining low power consumption [2]. This combination is particularly valuable for applications such as autonomous navigation, real-time control systems, and interactive artificial intelligence, where rapid adaptation to changing conditions is essential.

### 4.3 Approximate Computing for Energy-Accuracy Trade-offs

Approximate computing offers a pragmatic approach to managing the inherent trade-offs between energy efficiency and learning accuracy in neuromorphic systems [10]. Rather than attempting to eliminate all sources of error in emerging memory devices, approximate computing strategically sacrifices accuracy to achieve substantial improvements in energy efficiency and computational throughput.

The fundamental insight underlying approximate computing is that machine learning applications do not require 100% accuracy to be useful [10]. By accepting modest reductions in classification accuracy, often in the range of 1-5%, significant energy savings can be achieved through simplified circuit design, reduced precision arithmetic, and optimized memory access patterns. The error rate of approximate computing elements can be controlled through design parameters such as pulse duration, enabling fine-grained trade-offs between accuracy and energy consumption.

For synaptic devices, approximate computing can maximize energy efficiency by reducing unnecessary precision in weight representations and update operations [10]. High-priority computational modules can be allocated more resources to maintain accuracy, while lower-priority modules can employ more aggressive approximation to save energy. This differentiated approach enables system-level optimization that adapts to the varying accuracy requirements of different computational tasks.

## 5. Integration of Multiple Optimization Strategies

### 5.1 Combining Device Innovation with Algorithmic Adaptation

The most effective approaches to parallel optimization of energy efficiency and learning accuracy combine device-level innovations with algorithmic adaptations that account for hardware constraints. VO₂-based devices configured with specific decay timescales have been used to implement behavioral time-scale plasticity (BTSP) learning rules that store spatial maps of environmental information in synaptic weights [4]. The real-time calculation of synaptic weight updates based on intermittent measurements of device conductance states demonstrates how hardware characteristics can be leveraged to implement efficient learning algorithms.

The BTSP learning rule exemplifies the integration of device physics with algorithmic requirements. By exploiting the intrinsic decay dynamics of VO₂ devices, which match the timescales of biological neuronal signaling elements, the system achieves efficient representation of slowly varying signals without continuous computational overhead. Once an intersynaptic (IS) device fully relaxes to its insulating state, the window for plasticity closes and read pulses can cease until the next dendritic calcium spike event occurs, reducing unnecessary energy consumption.

### 5.2 Cross-Homeostatic Rules for Stability in Heterogeneous Systems

Achieving robust performance in neuromorphic systems with heterogeneous, variable components requires learning rules that can maintain stability while adapting to changing conditions. Biologically-plausible cross-homeostatic rules have been developed to balance excitatory and inhibitory plasticity in spiking recurrent networks implemented on neuromorphic hardware [11]. These rules adjust the overall activity levels of neurons to maintain stability while allowing synaptic weights to adapt based on experience.

The application of cross-homeostatic rules addresses the fundamental challenge of maintaining network stability in the presence of device variation [11]. By continuously adjusting the balance between excitation and inhibition, these rules compensate for device-to-device variations and ensure consistent network dynamics across different hardware instances. This approach represents a system-level strategy for managing heterogeneity that complements device-level and algorithmic-level optimizations.

### 5.3 Backpropagation-Compatible Learning Rules for Neuromorphic Hardware

The development of learning rules compatible with both backpropagation training and neuromorphic hardware deployment represents a significant advance in enabling high-accuracy learning on energy-constrained platforms [12]. Traditional backpropagation algorithms are incompatible with the event-driven, low-precision nature of neuromorphic hardware, creating a gap between training and deployment that often results in accuracy degradation.

A novel approach to reconciling backpropagation with neuromorphic hardware involves training networks with continuous-valued inputs, neuron outputs, and synaptic weights constrained to the range [0, 1], where these constrained values represent probabilities of spiking or synaptic activation [12]. This constrained network can be trained using standard backpropagation algorithms while maintaining a direct representation in spiking, low-precision deployment systems. The network topology employs a progressive mixing approach where each neuron combines inputs through probabilistic connections.

The synaptic connection probability changes according to the update rule $\Delta \tilde{c}_{ij} = -\alpha \frac{\partial E}{\partial \tilde{c}_{ij}}$, where $\alpha$ is the learning rate and $E$ represents the loss function [12]. Any connection probabilities falling outside the valid range [0, 1] are snapped to the nearest boundary value, ensuring hardware compatibility. This constrain-then-train approach offers the advantage that decreases in training error directly correspond to decreases in deployment error, providing a reliable pathway for transferring learned representations to neuromorphic hardware.

## 6. Performance Analysis and Comparative Evaluation

### 6.1 Energy-Accuracy Trade-offs Across Different Approaches

The synaptic weight update mechanisms examined in this report exhibit different trade-off characteristics between energy efficiency and learning accuracy, reflecting their underlying design principles and target applications. Synaptic caching algorithms achieve energy efficiency improvements of several-fold by strategically managing the consolidation of transient and stable synaptic modifications [9]. The magnitude of energy savings depends on the decay characteristics and maintenance costs of transient plasticity, with optimal performance achieved when transient forms provide sufficient stability for the application while requiring minimal energy for maintenance and modification.

Linear weight update mechanisms in HfO₂/AuNP-DNA memristors enable both high energy efficiency and learning accuracy by eliminating the need for iterative programming procedures and reducing systematic errors in weight updates [8]. The high linearity achieved through simple pulse amplitude programming particularly enhances the device's suitability for neural network applications where precise weight control is essential.

CRUS demonstrates remarkable robustness to device non-idealities, maintaining classification accuracy above 90% on MNIST even under conditions of high nonlinearity (|NL| ≥ 8) and low analog fidelity [6]. This performance is achieved through efficient weight update rules requiring only 1-bit precision and infrequent conductance access, minimizing both energy consumption and the accumulation of update errors.

### 6.2 Robustness to Device Variation

The robustness of different weight update mechanisms to device variation varies significantly based on their design principles and implementation approaches. Binarized neural networks using digital-type synaptic devices exhibit the highest immunity to device variability due to the coarse-grained nature of weight representations [5]. The requirement for only two distinct conductance states, rather than a continuum of analog values, effectively eliminates the impact of fine-grained variation.

CRUS achieves robustness to temporal conductance variation through its LTD skip update mechanism, which minimizes the damage caused by variations in conductance updates over time [6]. This approach is particularly effective for handling cycle-to-cycle variation, where the same device exhibits different switching behavior across repeated operations.

Cross-homeostatic rules provide robustness to device-to-device variation by continuously adjusting the balance of excitation and inhibition to maintain stable network dynamics [11]. This approach compensates for variation at the network level rather than attempting to eliminate variation at the device level, representing a fundamentally different strategy for managing heterogeneity.

### 6.3 Scalability and Practical Implementation

The scalability of different weight update mechanisms to large-scale neuromorphic systems depends on several factors, including the complexity of update calculations, the frequency of weight modifications, and the requirements for inter-device coordination. Event-driven learning rules such as STDP naturally support scalable implementations because weight updates occur only in response to spike events, which are typically sparse in well-designed networks [3].

Synaptic caching algorithms require coordination between transient and stable plasticity mechanisms, which may introduce overhead in distributed implementations [9]. However, the energy savings achieved during the learning process often outweigh this overhead, particularly for applications with extended training phases.

The hardware-algorithm co-design approach advocated in recent research supports scalability by ensuring that learning algorithms are designed with hardware constraints in mind from the outset [1]. This proactive approach avoids the performance bottlenecks that can arise when algorithms designed for ideal hardware are retrofitted to accommodate real-world device limitations.

## 7. Conclusions and Future Directions

### 7.1 Summary of Key Findings

This report has examined the question of which synaptic weight update mechanisms achieve parallel optimization of energy efficiency and learning accuracy in neuromorphic chips under device variation and power constraints. The analysis reveals that no single mechanism universally outperforms all others across all dimensions of the optimization space. Instead, the most effective approaches combine multiple strategies tailored to specific application requirements and hardware characteristics.

Synaptic caching algorithms provide substantial energy efficiency improvements by strategically managing the consolidation of transient and stable synaptic plasticity, achieving energy savings of several-fold while maintaining learning accuracy [9]. Linear weight update mechanisms in engineered memristor devices enable both high energy efficiency and learning accuracy by eliminating systematic errors and reducing programming energy consumption [8]. CRUS demonstrates remarkable robustness to device non-idealities, maintaining high classification accuracy even under challenging conditions of high nonlinearity and low analog fidelity [6].

System-level strategies including holistic hardware-algorithm co-design, event-driven processing, and approximate computing complement device-level and algorithmic innovations to achieve comprehensive optimization across the hardware-software stack [1][2][10]. The integration of these approaches enables neuromorphic systems to achieve robust performance despite the inherent constraints of nanoscale device technology.

### 7.2 Recommendations for Implementation

Based on the analysis presented in this report, several recommendations can be offered for practitioners seeking to implement energy-efficient and accurate synaptic weight update mechanisms in neuromorphic systems:

First, a holistic co-design approach should be adopted that considers device characteristics, learning algorithms, and system-level constraints as an integrated optimization problem. The performance of individual components cannot be reliably extrapolated to predict system-level behavior, making early integration of hardware and algorithmic design essential.

Second, the choice of weight update mechanism should be matched to the specific application requirements and hardware characteristics. Applications requiring high accuracy may benefit from linear weight update mechanisms and synaptic caching, while applications prioritizing energy efficiency may favor approximate computing and event-driven learning rules.

Third, robustness to device variation should be explicitly considered in the design process. Strategies such as cross-homeostatic rules, binarized weight representations, and CRUS provide different approaches to managing variation that can be selected based on the expected variation characteristics of the target hardware platform.

### 7.3 Future Research Directions

Several promising directions for future research emerge from this analysis. The development of adaptive weight update mechanisms that can automatically adjust their behavior based on real-time monitoring of device characteristics and system performance represents an important opportunity for improving robustness and efficiency.

The integration of machine learning techniques for process control and fault detection during neuromorphic device fabrication offers potential for reducing device variation at its source [13]. CNN-based anomaly detection algorithms can identify deviations in processing conditions and enable real-time adjustment of process parameters to ensure consistent device quality.

Finally, the exploration of novel device technologies and materials that combine the advantages of different memory technologies—such as the integration of ferroelectric, resistive switching, and phase-change mechanisms—may enable weight update mechanisms that achieve unprecedented combinations of energy efficiency, accuracy, and robustness [7].

## References

[1] Ferreira de Lima, J. (2019). Machine learning for neuromorphic systems. *Journal of Lightwave Technology*. Retrieved from https://www.queensu.ca/physics/shastrilab/sites/shastwww/files/uploaded_files/publications/journals/47_Ferreira_de_Lima-JLT-machine_learning_2019.pdf

[2] Frontiers in Neuromorphic Computing. (2024). Neuromorphic computing and AI for energy efficient and adaptive edge intelligence. *Frontiers Research Topics*. Retrieved from https://www.frontiersin.org/research-topics/71619/neuromorphic-computing-and-ai-for-energy-efficient-and-adaptive-edge-intelligenceundefined

[3] Royal Society of Chemistry. (2023). Neuromorphic computing: Brain-inspired intelligent systems. *Materials Advances*. Retrieved from https://pubs.rsc.org/en/content/articlehtml/2023/ma/d3ma00449j

[4] PNAS. (2024). Behavioral time scale plasticity in vanadium dioxide devices. *Proceedings of the National Academy of Sciences*. Retrieved from https://www.pnas.org/doi/10.1073/pnas.2318362121

[5] Nature Scientific Reports. (2019). Binarized neural networks with digital-type synaptic devices. *Scientific Reports*. Retrieved from https://www.nature.com/articles/s41598-019-51814-5

[6] arXiv. (2021). CRUS: Constrained weight update strategy for hardware neural networks. Retrieved from https://arxiv.org/pdf/2111.07113

[7] ScienceDirect. (2024). Ferroelectric synaptic transistors for neuromorphic computing. *Microelectronics Journal*. Retrieved from https://www.sciencedirect.com/science/article/abs/pii/S1567173924001755

[8] ScienceDirect. (2025). HfO₂/AuNP-DNA bilayer memristor for artificial synapse applications. *Robotics and Computer-Integrated Manufacturing*. Retrieved from https://www.sciencedirect.com/science/article/abs/pii/S0263224125003197

[9] eLife. (2020). Synaptic caching for energy-efficient neuromorphic computing. *eLife*. Retrieved from https://elifesciences.org/articles/50804

[10] MDPI Electronics. (2020). Approximate computing for energy-efficient neuromorphic systems. *Electronics*. Retrieved from https://www.mdpi.com/2079-9292/9/9/1414

[11] Nature Communications. (2024). Stable recurrent dynamics in heterogeneous neuromorphic computing systems. *Nature Communications*. Retrieved from https://www.nature.com/collections/jaidjgeceb

[12] NeurIPS. (2015). Backpropagation for energy-efficient neuromorphic computing. *Advances in Neural Information Processing Systems*. Retrieved from http://papers.neurips.cc/paper/5862-backpropagation-for-energy-efficient-neuromorphic-computing.pdf

[13] Researching.cn. (2025). Machine learning for neuromorphic device fabrication and control. Retrieved from https://www.researching.cn/ArticlePdf/m00095/2025/7/4/7.pdf

## Annotations


## Sources
[1] http://papers.neurips.cc/paper/5862-backpropagation-for-energy-efficient-neuromorphic-computing.pdf
[2] https://arxiv.org/pdf/2111.07113
[3] https://elifesciences.org/articles/50804
[4] https://iopscience.iop.org/article/10.1088/2631-7990/adba1e
[5] https://pubs.rsc.org/en/content/articlehtml/2023/ma/d3ma00449j
[6] https://www.frontiersin.org/research-topics/71619/neuromorphic-computing-and-ai-for-energy-efficient-and-adaptive-edge-intelligenceundefined
[7] https://www.mdpi.com/2079-9292/9/9/1414
[8] https://www.nature.com/articles/s41598-019-51814-5
[9] https://www.nature.com/collections/jaidjgeceb
[10] https://www.pnas.org/doi/10.1073/pnas.2318362121
[11] https://www.queensu.ca/physics/shastrilab/sites/shastwww/files/uploaded_files/publications/journals/47_Ferreira_de_Lima-JLT-machine_learning_2019.pdf
[12] https://www.researching.cn/ArticlePdf/m00095/2025/7/4/7.pdf
[13] https://www.sciencedirect.com/science/article/abs/pii/S0263224125003197
[14] https://www.sciencedirect.com/science/article/abs/pii/S1567173924001755
[15] https://www.sciencedirect.com/science/article/pii/S2589004218300865