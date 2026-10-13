# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 66f40c50 | **Time:** 2527.37s | **Cost:** $0.18540
--------------------------------------------------------------------------------

# Reconfiguration Algorithms for Adaptive Computing Architectures: Balancing Real-Time Response Speed with Resource Utilization

## Abstract

Adaptive computing architectures represent a paradigm shift in hardware design, enabling systems to dynamically reconfigure their computational resources in response to changing application requirements. This report examines the reconfiguration algorithms that enable such architectures to match hardware resources to applications in real-time while optimizing resource utilization. Through analysis of contemporary research in field-programmable gate array (FPGA) partial reconfiguration, runtime reconfiguration management, and heterogeneous system scheduling, this report identifies key algorithmic approaches including Time-Division Multiplexing (TDM) scheduling, context-aware task mapping, and dynamic partial reconfiguration (DPR) strategies. The findings reveal that effective reconfiguration algorithms must balance multiple competing objectives: minimizing reconfiguration latency, reducing power overhead, maximizing hardware utilization, and ensuring real-time responsiveness. The synthesis of these approaches provides a comprehensive understanding of the algorithmic foundations supporting next-generation adaptive computing systems.

## 1. Introduction

The exponential growth in computational demands across diverse application domains—from artificial intelligence and machine learning to edge computing and cyber-physical systems—has exposed fundamental limitations in traditional static hardware architectures. Conventional computing systems, designed with fixed hardware configurations, struggle to accommodate the varying computational requirements that characterize modern workloads. This mismatch between hardware capabilities and application demands has catalyzed significant research interest in adaptive computing architectures capable of runtime reconfiguration.

Adaptive computing systems represent a transformative approach to hardware design, wherein computational resources can be dynamically reconfigured to match the specific requirements of executing applications. Unlike traditional fixed-function hardware, these systems can modify their functional behavior at runtime, enabling unprecedented flexibility in resource allocation and utilization. The core challenge lies in developing reconfiguration algorithms that can effectively manage this dynamic adaptation while satisfying stringent real-time constraints and maximizing resource efficiency.

The significance of this research extends across multiple domains. In embedded AI applications, adaptive systems can adjust their computational resources based on workload characteristics, achieving substantial improvements in both performance and energy efficiency [1]. For real-time systems in aerospace and defense applications, runtime reconfiguration enables systems to adapt to changing operational requirements without service interruption [2]. In high-performance computing environments, adaptive resource management can optimize cache utilization and processing element allocation based on application behavior patterns [3].

This report synthesizes current research to address the central question: What reconfiguration algorithms enable adaptive computing architectures to dynamically match hardware to applications while balancing real-time response speed with resource utilization? The analysis encompasses FPGA-based partial reconfiguration techniques, runtime scheduling algorithms for heterogeneous systems, and co-design methodologies that integrate software adaptability with hardware reconfigurability.

## 2. Theoretical Foundations of Runtime Reconfiguration

### 2.1 Fundamental Concepts and Terminology

Runtime reconfiguration refers to the capability of a computing system to modify its hardware configuration during operation without halting system execution. This capability is particularly significant in Field-Programmable Gate Array (FPGA) based systems, where partial reconfiguration allows specific regions of the device to be reprogrammed while other regions continue operating [4]. The distinction between full and partial reconfiguration is fundamental: full reconfiguration requires halting all system operations and reloading the entire bitstream, whereas partial reconfiguration enables targeted modifications to specific hardware modules.

Dynamic Partial Reconfiguration (DPR) has emerged as the primary mechanism for implementing adaptive computing on modern FPGA platforms. DPR enables the time-sharing of physical resources to execute multiple design modules called run-time reconfiguration (RTR) modules [5]. This virtualization of FPGA resources allows a single physical device to host multiple hardware accelerators over time, dramatically improving resource utilization compared to static implementations.

The concept of Time-Division Multiplexing (TDM) in FPGA resource management was first introduced through partial reconfiguration technology [4]. TDM enables multiple hardware contexts to share the same physical resources by allocating distinct time slots for each configuration. This approach leads to several key benefits: more efficient resource utilization, shorter reconfiguration time compared to full reconfiguration, and lower static power dissipation. The TDM paradigm has proven particularly valuable in applications where multiple hardware functions are required but not simultaneously active.

### 2.2 Reconfiguration Granularity and Levels

Research has identified multiple levels of reconfiguration granularity, each offering distinct trade-offs between flexibility and overhead. At the system level, reconfiguration involves distributing application functionalities across heterogeneous architecture components including digital signal processors (DSPs), FPGAs, and general-purpose processors [6]. This level of reconfiguration addresses coarse-grained allocation decisions but typically operates on longer time scales.

Functional level reconfiguration represents the most commonly implemented approach for adaptive FPGA systems. At this level, partially runtime reconfigurable architectures based on FPGAs support partial dynamic runtime configuration, enabling flexible hardware adaptation [6]. A runtime reconfiguration manager controls, monitors, and executes the dynamic reconfiguration process, abstracting the complexity of bitstream manipulation from application developers.

At the logic and RTL level, fine-grained reconfiguration allows configuration at the bit level, providing maximum flexibility but with significant overhead. This level is architecture-dependent and does not typically support open methodologies, limiting its applicability to specific vendor ecosystems [6]. For most adaptive computing applications, functional level reconfiguration provides the optimal balance between flexibility and practical implementability.

### 2.3 Architectural Considerations

The implementation of runtime reconfiguration requires careful architectural design to minimize reconfiguration overhead while maximizing system flexibility. Modern approaches employ hierarchical management structures comprising Upper Management Units (UMU), Management Units (MU), Processing Units (PU), and Re-ordering Units (RU) [4]. This hierarchical organization enables distributed decision-making while maintaining coherent system-wide resource allocation.

Custom hardware-based runtime management implements reconfiguration control completely in hardware through custom state-machines and reconfiguration controllers [7]. These systems achieve high reconfiguration throughput by supporting direct memory access (DMA) transfer of bitstreams from external memory to the configuration interface. However, they generally employ simple adaptation algorithms due to the difficulty and resource requirements of implementing complex algorithms in hardware.

The trade-off between hardware and software-based reconfiguration management reflects fundamental architectural decisions in adaptive system design. Software-based approaches offer greater flexibility and easier implementation of complex scheduling algorithms but introduce additional latency. Hardware-based approaches minimize reconfiguration latency but constrain the sophistication of adaptation algorithms.

## 3. Reconfiguration Algorithms and Scheduling Strategies

### 3.1 Throughput-Aware Scheduling Algorithms

Effective reconfiguration scheduling must balance multiple competing objectives, with throughput optimization representing a primary concern for many applications. Throughput-aware scheduling algorithms prioritize maximizing the rate of task completion by minimizing idle time and maximizing parallel execution of reconfigurable hardware modules [4]. These algorithms typically employ predictive models to anticipate upcoming resource requirements and pre-load configurations before they are needed.

The scheduler routine for throughput-aware data processing implements a strategy that minimizes hardware context switching times while accounting for dynamic reconfiguration time overhead and extra power dissipation [4]. This approach recognizes that the cost of reconfiguration includes not only the direct time required for bitstream loading but also the energy consumed during the reconfiguration process. By carefully scheduling reconfiguration operations during natural idle periods, these algorithms can significantly improve overall system throughput.

Algorithm design for throughput optimization must consider the dependencies between tasks and the availability of required configurations. In systems executing multiple concurrent applications, the scheduler must allocate reconfigurable resources among competing demands while maintaining quality of service guarantees. This multi-dimensional optimization problem requires sophisticated scheduling policies that can adapt to changing workload characteristics.

### 3.2 Real-Time Response Optimization

For applications with stringent latency requirements, real-time response optimization takes precedence over throughput maximization. Real-time scheduling algorithms for adaptive computing must guarantee that reconfiguration operations complete within specified time bounds while maintaining system stability [4]. These algorithms typically employ priority-based scheduling with admission control to ensure that real-time constraints can be satisfied.

The scheduler for real-time applications with fast reaction requirements implements specialized logic to minimize response latency [4]. This approach involves maintaining frequently-used configurations in fast-access memory, pre-empting lower-priority reconfiguration operations when urgent requests arrive, and employing predictive pre-loading based on anticipated workload patterns. The challenge lies in balancing the need for rapid response with the overhead of maintaining multiple ready configurations.

Runtime reconfigurability, as demonstrated in systems like DRACS (Dynamic Reconfiguration for Adaptive Computing Systems), enables nearly instantaneous reconfiguration of system functions to operational needs [2]. This capability is achieved through careful co-design of reconfiguration controllers, configuration memory systems, and scheduling algorithms that minimize the critical path for reconfiguration operations.

### 3.3 Adaptive Task Mapping and Device Selection

Modern heterogeneous computing systems require algorithms that can dynamically select the optimal execution device for each task based on current system state and workload characteristics. TornadoVM exemplifies this approach, adapting execution during runtime to the heterogeneous device that best suits the input policy without requiring prior knowledge or performance models [8]. This runtime adaptation enables the system to respond to changing conditions that may not be predictable at design time.

The Aira system employs performance prediction models and resource allocation policies to perform CPU/GPU selection at runtime [8]. By combining analytical models with runtime measurements, Aira can make informed decisions about task placement that balance performance, energy consumption, and resource utilization. This model-based approach provides more consistent performance across varying workloads but requires accurate calibration of prediction models.

Machine learning techniques have been applied to the device selection problem, with approaches like those proposed by Hayashi et al. and Grewe et al. addressing the challenge through data-driven model construction [8]. These approaches can capture complex relationships between application characteristics and optimal device mapping that may not be apparent through analytical modeling. However, they require training data and may exhibit unpredictable behavior for novel workloads.

### 3.4 Cache and Resource Utilization Optimization

Adaptive systems must also manage lower-level resources such as cache memories and processing elements to maximize overall system efficiency. Research has characterized common patterns of cache utilization across applications and developed adaptive runtime schemes that automatically reconfigure cache resources based on application behavior [3]. These schemes can turn cache regions on or off to save energy and switch cache organization to streaming mode when appropriate.

The runtime reconfiguration of cache parameters involves identifying iterative patterns and reconfiguration units, then applying reconfiguration when measured attributes fall within specified thresholds [3]. This approach requires runtime monitoring of application behavior and collective decision-making across multiple processing elements to ensure consistent adaptation. The use of collective operations like Allreduce enables distributed determination of when reconfiguration is appropriate.

Resource utilization varies widely from application to application, with some workloads benefiting from aggressive parallel execution while others are memory-bandwidth limited [9]. Adaptive algorithms must recognize these patterns and configure hardware resources accordingly. This recognition may involve analyzing instruction mix, memory access patterns, and communication characteristics during execution.

## 4. FPGA-Specific Reconfiguration Techniques

### 4.1 Partial Reconfiguration Management

Partial reconfiguration enables implementation of adaptive hardware systems that can modify their behavior dynamically at the hardware level to adapt to operating conditions [7]. This capability is particularly important in applications where computational requirements exceed software capabilities but custom hardware would be too rigid. Software-defined radio (SDR) represents a canonical application domain where PR combines flexibility with hardware performance.

Runtime placement and configuration file manipulation techniques have been developed to overcome long tool chain runtimes associated with partial reconfiguration [7]. These approaches enable runtime placement and routing and bitstream manipulation to make implemented logic relocatable. However, practical success has been limited due to the heterogeneous architecture of modern FPGAs and the limited processing power of embedded processors typically employed for online manipulations.

The reconfiguration schedule in custom hardware-based systems is either pre-stored in internal memory or dynamically decided by state machines observing surroundings through sensors [7]. This approach achieves high reconfiguration throughput through DMA-supported bitstream transfer but offers limited flexibility due to the difficulty of implementing complex adaptation algorithms in hardware.

### 4.2 Dynamic Reconfiguration for Deep Learning Acceleration

FPGA-based acceleration of deep neural networks (DNNs) has emerged as a critical application domain for runtime reconfiguration. Research has demonstrated that dynamic reconfiguration can increase power and computing efficiency of both DNN models and hardware to meet application-specific requirements [10]. Achieved results show reductions in energy consumption and processing time of up to 53.8% and 36.5% respectively by switching to smaller models during execution.

The co-design methodology for CNN acceleration on FPGAs combines CNN architecture adaptability with dynamic partial reconfiguration of FPGA hardware [1]. This approach enables automated synthesis and runtime customization of hardware acceleration units, enhancing computational performance and reducing latency. The framework supports both fine-grained and coarse-grained hardware customizations that improve computation efficiency.

Runtime FPGA reconfiguration allows adaptation of CNNs and hyperparameters without full re-synthesis, dramatically reducing deployment time and costs [1]. This capability is particularly valuable in edge computing scenarios where operational requirements may change after deployment. The ability to update hardware configurations in the field enables continuous optimization of the hardware-software interface.

### 4.3 Edge Computing and Critical Systems

Edge AI acceleration for critical systems presents unique challenges for reconfiguration algorithms, including power constraints, radiation tolerance requirements, and the need for reliable AI processing [11]. FPGA and Coarse-Grained Reconfigurable Array (CGRA) technologies provide promising platforms for real-time and autonomous data processing in these demanding environments.

CGRA systems offer a flexible platform for hardware acceleration that can suit a wide variety of applications, especially in machine learning, digital signal processing, and computer vision [11]. The reconfigurable nature of CGRAs enables adaptation to workloads that change frequently and require varying degrees of computational intensity. Integration of CGRAs with RISC-V processors provides increased throughput, decreased latency, and increased energy efficiency.

The design of Application-Specific Integrated Circuits (ASICs) for specific neural network accelerators is not sustainable due to the diverse and evolving nature of AI applications [11]. Future hardware platforms must balance high performance with adaptability, supporting various AI models and the ability to update and reconfigure as mission requirements change. This balance is achieved through sophisticated reconfiguration algorithms that optimize resource allocation in real-time.

## 5. System Integration and Implementation Frameworks

### 5.1 Runtime System Architecture

The runtime system in adaptive computing environments orchestrates the control system that manages resource allocation and reconfiguration scheduling. In HPC environments, the runtime system mediates communication and provides parallel services such as message passing in MPI [3]. This management capability, combined with application persistence, empowers the runtime system to provide important features including load balancing, fault tolerance, efficient parallel I/O, and power management.

Adaptive runtime systems manage Sequential Execution Blocks (SEBs), defined as sequential computations between two communication calls [3]. After identifying iterative patterns and reconfiguration units, the runtime system ensures that iterations and their SEBs are consistent across different processors. This consistency is achieved through gathering characteristic information about SEB execution, including execution time, instruction-based samples, and key performance counters.

The integration of reconfiguration management with runtime system services enables sophisticated adaptation strategies that would not be possible with standalone reconfiguration controllers. By leveraging the runtime system's visibility into application behavior and communication patterns, reconfiguration decisions can be made with greater context awareness.

### 5.2 API Extensions and Programming Models

The DRACS program expanded the existing SLAAC application programming interface to include runtime reconfiguration capabilities [2]. These extensions include host-driven and data-driven reconfiguration, allowing both user-level and system-level control of configurations under software control. Current API extensions provide support for defining virtual configurations and managing the reconfiguration process.

TornadoVM demonstrates a compiler and runtime system approach that allows automatic instrumentation of existing parallel and heterogeneous code to select the best mapping device [8]. The system uses performance prediction models and resource allocation policies to perform device selection at runtime. TornadoVM bytecodes are totally hardware agnostic, allowing easy shipping between different machines and hardware configurations.

The HPVM compiler, runtime system, and virtual instruction set provides similar capabilities for targeting different heterogeneous systems [8]. The virtual instruction set concept enables hardware-agnostic program representation while supporting task reconfiguration capabilities. This approach simplifies the development of portable adaptive applications.

### 5.3 Design Automation and Synthesis

Modern frameworks integrate various tools to manage the design flow from high-level architecture modeling to low-level hardware generation [11]. The mapper and scheduler components utilize Integer Linear Programming (ILP) to allocate application Data-Flow Graph (DFG) nodes to CGRA resources, with topological search ensuring precise synchronization. Auxiliary hardware modules, including configuration and schedule controllers, are auto-generated to enhance dynamic reconfiguration and operational accuracy.

Design Space Exploration (DSE) algorithms play a crucial role in identifying optimal configurations for adaptive systems [11]. These algorithms iteratively search the configuration space to find parameter settings that optimize application metrics. The automation of configuration selection and hardware deployment enables developers to concentrate on higher-level design decisions while ensuring optimal runtime behavior.

The automation of hardware deployment for neural networks involves multiple steps including model compression, quantization, and configuration selection [11]. Simulation results are saved into tables used during the DSE phase, which selects quantized configurations based on application metrics. This automated approach reduces the semantic gap between application requirements and hardware implementation.

## 6. Performance Analysis and Optimization Trade-offs

### 6.1 Reconfiguration Latency Considerations

Reconfiguration latency represents a major drawback of runtime reconfiguration on commercial devices and must be considered during hardware/software partitioning [6]. The objective is to obtain near-optimal scheduling of tasks in time over a heterogeneous architecture, balancing the benefits of reconfiguration against the time and energy costs of performing reconfiguration operations.

The general rule for minimizing reconfiguration overhead is to minimize hardware context switching times while accounting for dynamic reconfiguration time overhead and extra power dissipation [4]. This optimization requires accurate models of reconfiguration time and energy consumption for different configuration sizes and memory hierarchies. Predictive pre-loading can mask reconfiguration latency by initiating reconfiguration before a configuration is actually needed.

Runtime reconfiguration managers must balance the desire to maintain many ready configurations against the memory and energy costs of storing these configurations. Configuration compression and incremental reconfiguration techniques can reduce the effective reconfiguration time by transmitting only the differences between configurations.

### 6.2 Power and Energy Optimization

Power consumption during reconfiguration includes both the static power of the configuration memory and the dynamic power consumed during bitstream loading. Research has demonstrated that TDM-based resource management leads to lower static power dissipation compared to static allocation of dedicated resources [4]. This reduction occurs because unused resources can be powered down when not allocated to active configurations.

The energy consumption of adaptive systems depends on the frequency and granularity of reconfiguration operations. Fine-grained reconfiguration enables more precise resource allocation but may incur higher overhead per reconfiguration operation. Coarse-grained reconfiguration reduces overhead but may result in less optimal resource utilization. The optimal balance depends on application characteristics and operational requirements.

Dynamic voltage and frequency scaling can be combined with reconfiguration to further optimize energy consumption. By adjusting both the configuration and the operating parameters of reconfigurable resources, adaptive systems can achieve energy efficiency close to that of dedicated hardware while maintaining flexibility.

### 6.3 Resource Utilization Efficiency

The utilization of reconfigurable resources varies significantly depending on the scheduling policy and application characteristics. Scheduling policies have direct effects on system performance and should be optimized according to specific application requirements such as throughput or reaction latency [4]. One-size-fits-all approaches rarely achieve optimal utilization across diverse workloads.

Resource management on reconfigurable devices enables load-balancing of multi-task processing through sophisticated allocation models [4]. These models must consider the heterogeneous nature of reconfigurable resources, where different regions may have different capabilities and reconfiguration characteristics. Hierarchical management structures help coordinate allocation across multiple resource types.

The complicated hardware architecture consisting of hierarchical management units makes implementation challenging and impractical without appropriate abstraction [4]. Effective resource management requires clear interfaces between management levels and well-defined protocols for resource allocation and deallocation.

## 7. Emerging Trends and Future Directions

### 7.1 Co-Design Methodologies

End-to-end co-design methodologies that integrate software adaptability with FPGA hardware reconfigurability represent a significant advance in adaptive system design [1]. These methodologies enable automated synthesis and runtime customization of hardware acceleration units, reducing the development effort while improving system performance. The co-design approach recognizes that optimal adaptive systems require coordinated design of hardware and software components.

The integration of high-level synthesis tools with runtime reconfiguration management enables automatic generation of reconfigurable accelerators from abstract specifications. This automation reduces the expertise required to develop adaptive systems and enables rapid exploration of design alternatives. The resulting systems can adapt to changing requirements without manual intervention in the hardware design.

### 7.2 Machine Learning Integration

Machine learning techniques are increasingly being applied to reconfiguration decision-making, enabling data-driven optimization of resource allocation [8]. These approaches can capture complex relationships between application characteristics and optimal configurations that may not be expressible through analytical models. The challenge lies in ensuring that learned policies generalize to novel workloads and operating conditions.

Reinforcement learning approaches to reconfiguration scheduling show promise for optimizing long-term system performance. By learning from the outcomes of past reconfiguration decisions, these systems can develop policies that improve over time. However, the exploration required for learning may be unacceptable in safety-critical applications where poor configurations could cause system failures.

### 7.3 Heterogeneous System Integration

The integration of multiple reconfigurable technologies—including FPGAs, CGRAs, and specialized accelerators—presents new challenges for reconfiguration algorithms [11]. Coordinating reconfiguration across heterogeneous resources requires sophisticated management architectures that can abstract the differences between resource types while optimizing overall system performance.

RISC-V processors integrated with CGRAs provide a flexible platform for heterogeneous computing that combines general-purpose computation with reconfigurable acceleration [11]. The open-source nature of RISC-V enables tight integration between processor and accelerator design, facilitating the development of coordinated reconfiguration strategies.

## 8. Conclusion

The reconfiguration algorithms enabling adaptive computing architectures to dynamically match hardware to applications represent a convergence of scheduling theory, hardware design, and runtime system architecture. Through the synthesis of partial reconfiguration technology, runtime scheduling algorithms, and co-design methodologies, these systems achieve a balance between real-time response speed and resource utilization that would be impossible with static hardware configurations.

The key algorithmic approaches identified in this report include Time-Division Multiplexing scheduling for efficient resource sharing, context-aware task mapping for heterogeneous device selection, and dynamic partial reconfiguration for FPGA-based adaptation. These approaches are unified by common principles: minimizing reconfiguration overhead through careful scheduling, maintaining multiple ready configurations to reduce latency, and adapting resource allocation based on runtime measurements of application behavior.

The performance of adaptive systems depends critically on the sophistication of their reconfiguration algorithms. Throughput-aware scheduling maximizes task completion rates for batch processing workloads, while real-time response optimization ensures timely adaptation for latency-sensitive applications. Cache and resource utilization optimization enables fine-grained adaptation to application behavior patterns, improving efficiency across diverse workloads.

Future research directions include the integration of machine learning techniques for data-driven optimization, the development of unified frameworks for heterogeneous reconfigurable systems, and the extension of co-design methodologies to encompass the complete hardware-software stack. As computational demands continue to grow and application requirements become more diverse, adaptive computing architectures enabled by sophisticated reconfiguration algorithms will become increasingly essential.

The findings of this report demonstrate that effective reconfiguration algorithms must balance multiple competing objectives: minimizing reconfiguration latency, reducing power overhead, maximizing hardware utilization, and ensuring real-time responsiveness. No single algorithm optimizes all these objectives simultaneously; rather, practical systems must select and combine approaches based on application requirements and operational constraints. The continued advancement of reconfiguration algorithms will be crucial to realizing the full potential of adaptive computing architectures in next-generation computing systems.

## References

[1] Future Generation Computer Systems, "Dynamic FPGA reconfiguration for scalable embedded artificial intelligence (AI): A co-design methodology for convolutional neural networks (CNN) acceleration," Volume 169, August 2025.

[2] DARPA, "Dynamic Reconfiguration for Adaptive Computing Systems (DRACS) program," Defense Technical Information Center, ADA408401.

[3] University of Illinois, "Adaptive Runtime Reconfiguration Schemes for HPC Platforms," IACOMA Research Group, 2014.

[4] Ming Liu, "Thesis Outline and Author's Contributions," KTH Royal Institute of Technology, https://people.kth.se/~mingliu/publications/phd_thesis.pdf.

[5] ScienceDirect, "Computing platforms for next-generation cyber–physical systems," 2024, Heliyon.

[6] UCI, "Runtime Reconfiguration Management for Heterogeneous Systems," IPDPS 2006.

[7] University of Warwick, "FPGA Dynamic Partial Reconfiguration Methods," WRAP Research Repository, 2018.

[8] JJ Fumero et al., "TornadoVM: Dynamic Reconfiguration for Heterogeneous Systems," VEE 2019.

[9] Cornell University, "Runtime Reconfiguration and Processor Efficiency," CSL Research.

[10] ARCS Lab, "Flexible Hardware Accelerator Framework for Deep Learning on FPGA-based Edge Computing," 2023.

[11] University of Pisa, "Edge AI Acceleration for Critical Systems: from FPGA Hardware to CGRA Technology," River Publishers, 2024.

## Annotations


## Sources
[1] https://aha.stanford.edu/sites/g/files/sbiybj20066/files/media/file/aha-retreat-2023_lightning-talks_web_sep2023_0.pdf
[2] https://apps.dtic.mil/sti/pdfs/ADA374632.pdf
[3] https://apps.dtic.mil/sti/tr/pdf/ADA408401.pdf
[4] https://balancezhai.github.io/files/ARCS_Lu.pdf
[5] https://iacoma.cs.uiuc.edu/iacoma-papers/sc14.pdf
[6] https://jjfumero.github.io/files/VEE2019_Fumero_Preprint.pdf
[7] https://people.kth.se/~mingliu/publications/phd_thesis.pdf
[8] https://repositorio-aberto.up.pt/bitstream/10216/169828/2/744535.pdf
[9] https://space.pitt.edu/sites/default/files/2024-10/TRETS09_G7.pdf
[10] https://wrap.warwick.ac.uk/100301/7/WRAP-FPGA-dynamic-partial-reconfiguration-methods-Fahmy-2018.pdf
[11] https://www.cecs.uci.edu/~papers/ipdps06/pdfs/20-RAW-paper-1.pdf
[12] https://www.csl.cornell.edu/~albonesi/research/papers/rtr.ps
[13] https://www.riverpublishers.com/downloadchapter.php?file=RP_9788743808831C6.pdf
[14] https://www.sciencedirect.com/science/article/abs/pii/S0141933118300802
[15] https://www.sciencedirect.com/science/article/pii/S0167739X2500072X