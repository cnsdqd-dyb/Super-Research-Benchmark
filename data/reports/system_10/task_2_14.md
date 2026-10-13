# Deep Research Report: perplexity/sonar-deep-research
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** edb7cd6a | **Time:** 109.43s | **Cost:** $1.08346
--------------------------------------------------------------------------------

# Load Scheduling Algorithms for Hybrid GPU-CPU Architectures: Balancing Computational Throughput with Energy Efficiency

## Executive Summary

The design and implementation of efficient load scheduling algorithms for hybrid GPU-CPU architectures represents one of the most critical challenges in modern heterogeneous computing systems. This comprehensive analysis examines the various approaches to scheduling computational tasks across heterogeneous processing elements while simultaneously optimizing both computational throughput and energy efficiency metrics. The key finding emerging from current research is that no single universally optimal algorithm exists; rather, the most effective approach depends on specific system characteristics, workload patterns, and optimization priorities. Advanced scheduling frameworks such as HybriMoE demonstrate that dynamic, adaptive scheduling strategies incorporating real-time workload monitoring and cache management can achieve significant performance improvements, with speedups ranging from 1.33× to 1.70× across different execution phases compared to traditional approaches[1]. Energy-aware scheduling methodologies combined with Dynamic Voltage and Frequency Scaling (DVFS) techniques can reduce energy consumption by up to 68% while maintaining throughput constraints, though this requires sophisticated modeling of power consumption characteristics across heterogeneous processors[9][13]. The optimal solution for most practical scenarios involves hybrid approaches that combine load-aware scheduling decisions with adaptive resource management, incorporating feedback mechanisms to respond to runtime variations in workload and system conditions.

## Fundamentals of Hybrid GPU-CPU Computing Architectures

### Understanding Heterogeneous Computing Systems

Heterogeneous computing refers to systems that utilize multiple different types of processors or cores operating together to achieve superior performance or energy efficiency[3]. Unlike homogeneous systems where all processors possess identical capabilities, heterogeneous architectures strategically combine different processing elements to exploit their specialized strengths. Graphics Processing Units (GPUs) excel at data-parallel computations with high arithmetic intensity, capable of providing order-of-magnitude improvements in computing power and memory bandwidth compared to traditional CPUs[57]. However, CPUs maintain advantages in sequential task execution, complex branching logic, and handling traditional operating system responsibilities. When properly orchestrated through effective load scheduling, hybrid CPU-GPU systems can deliver performance improvements of 21% to 23% with simultaneous energy savings, demonstrating the fundamental advantage of heterogeneous architectures over homogeneous alternatives[3].

The integration of heterogeneous computing into practical systems has accelerated dramatically with the proliferation of GPU computing in scientific and industrial applications. Supercomputing facilities and commercial data centers have embraced GPU acceleration as a core component of their computational infrastructure. For instance, the Titan supercomputer at Oak Ridge National Laboratory deployed 18,688 NVIDIA GPUs to achieve 17.59 petaflops of raw computing power, while major cloud service providers including Amazon, Microsoft, Alibaba, and others now offer hybrid CPU-GPU computing as standard cloud services[57]. This widespread adoption underscores the critical importance of developing efficient scheduling strategies that can maximize the utilization of these expensive and power-hungry resources.

### Characteristics and Performance Asymmetries

Hybrid GPU-CPU systems present unique challenges that distinguish them from homogeneous computing environments. The fundamental performance asymmetry between CPUs and GPUs requires sophisticated scheduling decisions that account for task characteristics and resource capabilities. A GPU may be exceptionally efficient at executing compute-intensive workloads with substantial parallelism but may be completely inappropriate for sequential tasks with irregular control flow. Similarly, a CPU can efficiently handle tasks with complex branching patterns and low arithmetic intensity but would waste substantial power executing embarrassingly parallel computations that could be far more efficiently executed on GPU hardware[4].

The performance heterogeneity extends beyond mere computational speed differences to encompass memory hierarchies, communication patterns, and power consumption profiles. Each processing element operates under different performance and power characteristics. GPUs feature wide memory bandwidth and specialized cache hierarchies optimized for streaming data access patterns, while CPUs maintain sophisticated caching mechanisms designed for workloads with temporal and spatial locality. The energy consumption characteristics differ substantially as well; while GPUs can deliver extraordinary peak performance per watt on well-matched workloads, they continue consuming significant power even when partially utilized. A single NVIDIA DGX-1 GPU server consumes up to 3,200 watts of electricity, with 75 percent dedicated to its eight GPUs alone, making energy efficiency a paramount concern for large-scale deployments[57].

### Memory and Communication Overheads

A critical consideration often overlooked in naive scheduling approaches is the cost of data movement between CPU and GPU memory domains. These disjoint memory spaces require explicit data transfers that consume bandwidth and introduce latency. Scheduling decisions must account not only for computation time but also for the overhead of transferring input data to GPU memory and retrieving results back to the CPU. Work-stealing approaches for GPU-accelerated systems demonstrate the importance of this consideration, showing that managing data movement between CPU and GPU memory domains is as critical as scheduling computation itself[7]. In some scenarios, the communication overhead can eliminate or even reverse the performance advantage that would otherwise accrue from executing a task on a GPU.

## Overview of Scheduling Approaches in Heterogeneous Systems

### Traditional Scheduling Algorithms

The classical approaches to task scheduling in heterogeneous computing environments include well-established heuristics such as the Heterogeneous Earliest Finish Time (HEFT) algorithm, Min-Min, Max-Min, and Round-Robin strategies[14][22]. The HEFT algorithm operates by computing upward rank values for each task based on average execution times and communication costs, then iteratively assigning tasks to the processor that minimizes the earliest finish time using an insertion-based approach[14][17]. This approach has proven effective for static scheduling scenarios where all tasks are known in advance and can be represented as directed acyclic graphs. HEFT achieves significant performance advantages over simpler approaches and remains widely referenced in scheduling literature.

Min-Min and Max-Min algorithms represent alternative heuristic approaches that operate by identifying task-processor pairs with minimum completion time (Min-Min) or maximum completion time (Max-Min) and prioritizing these selections appropriately[22]. These algorithms are computationally efficient but may suffer from poor load balancing in certain scenarios. Round-Robin scheduling distributes tasks uniformly across available resources regardless of their computational characteristics, making it appropriate only for situations where all processors possess equivalent capabilities and all tasks have similar execution requirements.

A key limitation of these traditional approaches is their inability to adapt to runtime variations in system conditions, workload patterns, or task characteristics. They typically assume static system configurations and unchanging task properties. In modern heterogeneous systems with dynamic workloads and variable system conditions, these static approaches often deliver suboptimal performance[11].

### Dynamic and Adaptive Approaches

Contemporary scheduling research increasingly focuses on dynamic and adaptive methodologies that can respond to runtime conditions. These approaches employ real-time monitoring of system state and workload characteristics, using this information to make continuous scheduling adjustments[5][25]. The distinction between static and dynamic scheduling becomes particularly important in heterogeneous environments where task-processor affinity can vary dramatically based on the specific characteristics of individual tasks and current system conditions.

Feedback-based control approaches represent a theoretically grounded methodology for designing adaptive schedulers. These frameworks map performance control requirements from real-time systems to feedback control theory, establishing dynamic models of system behavior and developing performance analyses that guarantee satisfaction of transient and steady-state performance specifications[48]. This control-theoretic approach provides more rigorous foundations compared to ad-hoc adaptive scheduling methods, enabling systematic design of scheduler algorithms with established analytical methods from control theory.

Machine learning approaches have emerged as increasingly effective tools for scheduling in heterogeneous systems. By training neural networks on historical execution data, these approaches can predict optimal task-processor assignments with significant speedup improvements. Research combining Deep Neural Networks with genetic algorithms demonstrates that while a neural network may not fully reproduce the optimization performance of genetic algorithms, it can reduce scheduling time by approximately 50 percent while maintaining competitive scheduling quality[11]. Prediction models for GPU execution times similarly show promise, though they require careful handling of uncertainty and potential underprediction errors[37].

## Energy Efficiency Considerations in Scheduling

### Dynamic Voltage and Frequency Scaling

Dynamic Voltage and Frequency Scaling (DVFS) represents one of the most effective techniques for reducing energy consumption in computing systems while maintaining performance constraints. DVFS exploits the mathematical relationship where dynamic power consumption follows a relationship of approximately \(P \propto CV^2f\), where C is effective capacitance, V is supply voltage, and f is clock frequency[13]. By reducing frequency, the voltage can be correspondingly reduced, leading to nearly quadratic reductions in dynamic power with voltage and linear reductions with frequency. This relationship creates a powerful opportunity for energy reduction, though it introduces trade-offs because reducing frequency generally increases task execution time[13].

The application of DVFS in heterogeneous computing requires consideration of several factors. First, many practical processors only support discrete frequency levels rather than continuous frequency scaling, which constrains optimization opportunities. Second, the relationship between frequency and voltage may not be convex, meaning that optimal solutions might require selecting only one or two neighboring frequency levels rather than allowing arbitrary frequency selection[13]. Third, different applications respond differently to frequency scaling; some applications experience superlinear increases in execution time when frequency is reduced, while others maintain nearly linear relationships[18].

Temperature-aware and application-dependent voltage and frequency scaling (T-DVFS and A-DVFS) represent sophisticated extensions of basic DVFS that improve energy efficiency by incorporating temperature and application-specific characteristics into scaling decisions[18]. Experimental results demonstrate that intelligent DVFS application can improve GPU power efficiency by 37 to 48 percent over default settings when combined with appropriate temperature management and application-specific tuning[18]. Energy reductions of up to 68 percent have been achieved for throughput-constrained streaming applications through periodic scheduling frameworks that allow applications to switch execution between energy-efficient operating modes[9].

### Power Consumption Models and Measurements

Effective energy-aware scheduling requires accurate models of power consumption across different operating conditions. Power consumption in modern processors exhibits complex behavior that depends not only on frequency and voltage but also on temperature, utilization patterns, and resource contention. Dynamic power consumption (related to active computation) dominates in many scenarios, but static power consumption (leakage) becomes increasingly important as transistor sizes shrink. Moreover, the relationship between utilization level and power consumption is non-trivial; partially utilized GPUs continue consuming substantial power even when processing fewer operations than their full capacity[2].

Power models that account for these complexities enable more accurate scheduling decisions. A runtime scheduling algorithm such as sBEET (Balancing Energy Efficiency and Timeliness) uses generic power models to capture the characteristics of dynamic and idle power consumption, then makes scheduling decisions about computing resource partitioning based on predicted energy consumption[2]. Through this approach, systems can achieve 13 percent reduction in deadline misses under overload conditions while simultaneously achieving 15 to 21 percent lower energy consumption when task sets are schedulable[2].

The relationship between spatial multitasking and energy consumption presents an important subtlety often overlooked in scheduling design. While spatial multitasking (allowing multiple kernels to execute simultaneously on a GPU) improves real-time performance by reducing idle waiting time, it can paradoxically increase energy consumption by reducing the total time that computing units remain completely idle[2]. This highlights the fundamental tension between different optimization objectives and demonstrates why effective scheduling often requires careful trade-off analysis.

### Energy-Efficient Load Balancing Methodologies

Load balancing in heterogeneous environments requires special attention to power efficiency considerations. Traditional load balancing approaches focus primarily on distributing computational load evenly across resources to minimize completion time. Energy-efficient load balancing additionally considers the power consumption characteristics of different nodes and the power efficiency of different resource allocations. A workload distribution and balancing methodology designed for heterogeneous systems accounts for the throughput sustainable by different compute nodes and their respective power efficiency characteristics[56]. For example, a hardware accelerator might provide exceptional power efficiency and thus should receive more workload allocation than less efficient general-purpose processors, even if it cannot complete more total work.

The optimization of power-efficient load balancing often involves determining frequency scaling levels that enable processors to meet throughput requirements while minimizing overall power consumption. When a system faces a throughput constraint, the workload should be distributed among heterogeneous nodes such that the overall power consumed is minimized while meeting the specified throughput target[56]. This requires solving a complex optimization problem that simultaneously considers task allocation, processor frequencies, and communication costs.

## Comprehensive Analysis of Hybrid Scheduling Frameworks

### HybriMoE: Dynamic CPU-GPU Scheduling for Expert Systems

Recent research has produced sophisticated hybrid CPU-GPU scheduling frameworks specifically designed for modern machine learning inference workloads. HybriMoE represents a state-of-the-art approach to hybrid CPU-GPU scheduling that addresses the unique challenges posed by Mixture of Experts (MoE) architectures[1]. These architectures introduce particular scheduling challenges because expert activation patterns are highly unstable and unpredictable, making fixed mapping strategies inherently inefficient. HybriMoE introduces multiple innovations: a dynamic intra-layer scheduling strategy that balances workloads across CPU and GPU based on runtime observations, an impact-driven inter-layer prefetching algorithm that anticipates expert access patterns, and a score-based caching algorithm to mitigate the effects of expert activation instability[1].

The key innovation of HybriMoE lies in its recognition that static CPU-GPU work partitioning cannot accommodate the highly variable nature of expert activation in MoE models. Instead, the framework employs dynamic scheduling that continuously adapts the CPU-GPU workload split based on runtime measurements. The dynamic intra-layer scheduling strategy monitors which experts are activated and adjusts the distribution of expert processing between CPU and GPU to maintain balanced utilization. This adaptive approach achieves average speedups of 1.33× in the prefill stage and 1.70× in the decode stage compared to state-of-the-art hybrid MoE inference frameworks[1].

The prefetching algorithm employed by HybriMoE demonstrates the importance of managing data movement between CPU and GPU memory domains. By predicting which experts will be needed in subsequent layers based on current layer activation patterns, the framework can initiate data transfers in advance, hiding much of the communication overhead. The score-based caching algorithm prioritizes keeping frequently accessed experts cached near processing elements, reducing the penalty of repeatedly transferring the same data.

### Work-Stealing and Dynamic Load Balancing

Work-stealing represents an alternative paradigm to centralized scheduling that proves particularly effective for heterogeneous GPU-CPU systems. In work-stealing approaches, rather than a central scheduler making all assignment decisions, individual processing elements that become idle actively pull work from queues, with the ability to steal work from other processors' queues when their local work is exhausted[10][7]. This pull-based approach offers several advantages over traditional push-based load balancing: it automatically adapts to heterogeneity in processor capabilities, naturally incorporates data locality considerations, and reduces the overhead of centralized scheduling decisions[10].

The Scioto-ACC work-stealing framework for GPU-accelerated parallel programs demonstrates how this approach can be extended to hybrid CPU-GPU systems[7]. An accelerator-aware work-stealing algorithm performs scalable, receiver-initiated dynamic load balancing while accounting for the impact of task distribution and data movement overheads. The framework maintains queues where both CPU-friendly and GPU-friendly tasks can reside, with each processor type pulling work from different ends of the queue. When the CPU is idle, it dequeues tasks from one end of the queue and executes them on the CPU. Similarly, when the GPU becomes idle, it takes tasks from the other end of the queue and executes them on the GPU. This double-ended queue strategy proves particularly effective because it enables tasks to be executed where they achieve better performance.

The work-stealing approach also provides flexibility in handling tasks with varying CPU-GPU suitability. Through selective single-ended GPU-steal strategies, the system can determine execution time ratios on CPU versus GPU and preferentially assign tasks to the processing element where they will complete faster. Experimental results demonstrate that double-ended queue strategies and selective single-ended GPU-steal strategies consistently outperform simpler alternatives, achieving superior performance through intelligent work distribution[7].

### Interference-Aware Scheduling and Performance Isolation

When multiple tasks execute concurrently on shared GPU resources, they invariably experience resource contention and interference. This interference can severely compromise the performance predictability that many applications require. Modern GPU scheduling frameworks must account for these interference effects when making colocation decisions[38][21]. Understanding the sources of interference—including compute resource contention, memory bandwidth competition, cache conflicts, and register file pressure—enables more intelligent scheduling that minimizes negative performance interactions.

GPU scheduling should operate at fine granularity levels, making decisions per kernel or per thread block rather than at coarse task granularity, to avoid head-of-line blocking where a long-running resource-intensive kernel prevents other work from executing[38]. When kernels must execute concurrently, restricting them to separate Streaming Multiprocessors (SMs) helps eliminate certain types of interference but cannot prevent contention for shared resources like L2 cache and memory bandwidth. The relationship between occupancy and performance proves complex; kernels with lower occupancy may actually achieve better performance when coexecuting with other kernels because they leave more resources available for the colocating workload[38].

Performance isolation mechanisms available in modern GPUs include NVIDIA's Multi-Process Service (MPS), Multi-Instance GPU (MIG), and emerging technologies like Green Contexts[44]. MPS allows multiple processes to share GPU resources but provides limited isolation guarantees and leaves applications vulnerable to interference. MIG achieves hardware-level isolation by partitioning GPUs into independent instances with dedicated resources, providing strong isolation at the cost of reduced flexibility. Green Contexts represent an emerging middle ground, offering temporal isolation through time-slicing mechanisms[44]. The choice among these mechanisms depends on specific application requirements, with safety-critical applications preferring strong isolation mechanisms even at some cost to utilization, while throughput-oriented applications might accept weaker isolation to maximize overall system throughput.

## Scheduling Algorithms Optimizing Throughput and Energy Efficiency

### Multi-Objective Optimization Approaches

Many practical scheduling problems in heterogeneous systems require balancing multiple competing objectives: minimizing makespan (total completion time), reducing energy consumption, meeting deadline constraints, ensuring fairness, and maximizing resource utilization. Multi-objective optimization approaches address this complexity by finding scheduling solutions that Pareto-optimally balance different objectives—that is, finding solutions where improving one objective would necessarily require degrading another[28].

The Multi-Objective Discrete Particle Swarm Optimization (MODPSO) algorithm combined with Dynamic Voltage and Frequency Scaling represents a sophisticated approach to multi-objective workflow scheduling in cloud environments[28]. This algorithm iteratively searches for scheduling solutions that simultaneously minimize makespan, reduce energy consumption, and maintain acceptable cost levels. Experimental results demonstrate that compared to the HEFT algorithm, MODPSO improves makespan by 0.05 percent, cost by 9.93 percent, and energy consumption by 26.40 percent for synthetic workflow instances. These improvements demonstrate the potential of sophisticated optimization techniques compared to simpler greedy approaches[28].

The energy-efficient makespan cost-aware scheduling (EMCS) algorithm represents another multi-objective approach designed for cloud-fog-based IoT applications[51]. Using evolutionary strategies to optimize execution time, cost, and energy consumption simultaneously, EMCS achieves 67.1 percent better makespan compared to cost makespan-aware scheduling (CMaS), 62.4 percent lower cost compared to CMaS, and 11.55 percent lower energy consumption compared to CMaS[51]. These results underscore the potential of evolutionary algorithms to address complex multi-objective optimization problems in heterogeneous scheduling.

### Fairness-Aware Scheduling

While throughput and energy efficiency represent important metrics, fairness considerations also matter significantly, particularly in multi-user systems or when executing heterogeneous workloads with different characteristics. Fairness-aware scheduling approaches aim to ensure that no individual task or user experiences severe performance degradation relative to others, even while optimizing for system-wide metrics[53]. In heterogeneous multi-core systems with different core types (big and small cores), fairness-aware scheduling must balance the tendency of big cores to be monopolized by compute-intensive threads against the need to ensure all threads receive reasonable performance.

The equal-progress scheduling approach ensures that each thread makes approximately equal progress over time, preventing starvation of threads assigned to less powerful core types[53]. Experimental results demonstrate that equal-progress scheduling improves performance by 32 percent on average for heterogeneous multi-threaded workloads while achieving fairness levels of 86 percent compared to only 56 percent fairness for pinned scheduling approaches. For multi-program workloads, fairness-aware scheduling achieves 21 percent throughput improvement over pinned scheduling while maintaining comparable throughput to throughput-optimized scheduling that ignores fairness considerations[53].

This demonstrates an important principle: fairness-aware scheduling often proves superior to approaches that pursue throughput optimization at the expense of fairness. When different workloads experience highly disparate performance on heterogeneous resources, unfair allocation that concentrates all work on the most capable resources often reduces overall throughput because less capable resources become idle. More balanced allocation maintains higher overall resource utilization even though individual tasks may not achieve their best possible performance[53].

### Adaptive Real-Time Scheduling with Feedback Control

Feedback Control real-time Scheduling (FCS) frameworks apply control theory principles to design adaptive scheduling algorithms that can satisfy performance specifications in dynamic and unpredictable environments[48]. Rather than relying on ad-hoc tuning iterations, control theory provides systematic design methodologies for achieving desired dynamic response characteristics. The FCS framework maps performance control requirements from real-time systems to feedback control theory, establishing dynamic models of system behavior and developing scheduling algorithms with proven performance guarantees.

This approach recognizes that in unpredictable environments where task CPU utilization varies over time and is not known in advance, static scheduling approaches necessarily prove inadequate. A feedback control loop continuously monitors actual system performance relative to target performance specifications, computing control inputs that adjust scheduler behavior to drive the system toward desired performance levels. The control design methodology establishes dynamic models of the real-time system, applies control theory methods to develop controller parameters, and provides mathematical analyses proving that the resulting controller satisfies system performance specifications.

Adaptive real-time scheduling algorithms can incorporate DVFS mechanisms as a control input, adjusting processor frequency to maintain desired performance levels while optimizing energy consumption. By treating frequency scaling as a feedback control variable, the system can maintain specified performance targets while adapting to runtime changes in workload characteristics and environmental conditions. This provides more principled approaches to energy management compared to reactive frequency scaling schemes that lack performance guarantees[45].

## Trade-offs Between Throughput and Energy Efficiency

### Fundamental Performance-Energy Trade-offs

The relationship between computational throughput and energy efficiency is inherently complex and often contradictory. Maximizing raw computational throughput typically requires running processors at high frequency and full utilization, which maximizes energy consumption. Conversely, minimizing energy consumption often requires reducing frequency and allowing processors to enter low-power states, which reduces throughput. The Energy-Delay Product (EDP) metric provides one common approach to quantifying this trade-off, measuring the product of energy consumption and execution time. Many optimization approaches target specific points on the Pareto frontier of possible throughput-energy trade-offs rather than pursuing either objective to its logical extreme.

The distinction between dynamic and static power consumption introduces additional complexity to this trade-off analysis. Dynamic power consumption scales with frequency and voltage and represents the dominant source of power consumption in many scenarios. Reducing frequency through DVFS directly reduces dynamic power consumption. However, static power consumption due to leakage currents does not decrease proportionally to frequency reduction, meaning that the relative importance of static power increases at lower frequencies. This introduces a "sweet spot" frequency where total power consumption reaches a minimum, typically occurring at somewhat reduced frequency compared to maximum frequency operation[18].

Spatial multitasking on GPUs presents a particularly interesting example of throughput-energy trade-offs. While executing multiple kernels concurrently on a GPU can improve real-time performance by reducing queuing delays and improving overall resource utilization, it simultaneously increases energy consumption by reducing the time that computing units remain completely idle[2]. A GPU with partially utilized kernels still consumes nearly the same power as when fully utilized; only when all computing units can be powered down are substantial power savings achieved. This demonstrates that improving throughput and improving energy efficiency can work against each other in some scenarios, requiring careful engineering to achieve acceptable compromises.

### Energy Efficiency Metrics and Measurement

Quantifying energy efficiency requires careful selection of appropriate metrics. Power Usage Effectiveness (PUE), defined as total facility energy consumption divided by IT equipment energy consumption, measures the efficiency of cooling and infrastructure but does not address the efficiency of computation itself[12]. For evaluating computational efficiency, metrics such as performance-per-watt, which measures useful computational output divided by power consumed, provide more relevant assessments. The Carbon Usage Effectiveness (CUE) metric extends this further by measuring carbon emissions relative to energy consumed by IT equipment, helping quantify environmental impact[12].

Data center energy consumption metrics extend beyond simple power measurement to include energy reuse through waste heat recovery, renewable energy factors, and tracking of on-site generation[12]. The Energy Reuse Effectiveness (ERE) metric quantifies how effectively a data center reuses energy, calculated by multiplying PUE with the Energy Reuse Factor (the ratio of reused energy to total energy consumed). Comprehensive energy assessment requires tracking energy consumption of IT equipment, supporting infrastructure, cooling systems, and power delivery mechanisms[12].

For specific devices and applications, performance-per-watt measurements should account for the specific workloads being executed, recognizing that energy efficiency varies dramatically across different applications. A single GPU might achieve excellent efficiency on some workloads while showing poor efficiency on others. Proper benchmarking requires executing representative workloads and carefully measuring actual energy consumption across the full range of utilization levels and operating conditions.

## Practical Implementation Considerations

### Scheduling Framework Design

Implementing effective scheduling frameworks for hybrid GPU-CPU systems requires careful consideration of several architectural decisions. The scheduler must continuously monitor system state including processor utilization, memory bandwidth consumption, and thermal conditions. This monitoring overhead itself consumes resources and must be minimized to avoid dominating the runtime scheduling decision computation. The decision granularity significantly impacts both scheduling quality and overhead; making scheduling decisions at very fine granularities (per thread block) enables more precise optimization but incurs higher overhead, while coarse-grained decisions (per task) reduce overhead but miss optimization opportunities[38].

The scheduler must also manage the complexity of predicting task execution time and resource requirements. Many modern applications exhibit execution behavior that depends on input data characteristics, making offline execution time prediction impossible. Runtime profiling and prediction models can help, but these themselves incur overhead and introduce prediction uncertainty. Machine learning models trained on historical execution data can improve prediction accuracy, but require careful handling of distribution shift when new applications or input characteristics appear[37].

Integration with existing operating system and runtime stacks presents additional complexity. Most modern GPU systems include GPU drivers that handle low-level resource management, typically through mechanisms like CUDA streams or OpenCL command queues. A practical scheduling framework must work within these driver constraints while achieving scheduling objectives. Some optimization opportunities require modifications to GPU drivers or operating systems, which limits the solutions that can be deployed without requiring specialized hardware or privileged modifications[47].

### Empirical Performance Evaluation

Evaluating scheduling approaches requires comprehensive experimental methodology that tests performance across diverse workloads and system configurations. Microbenchmarks that isolate specific performance characteristics enable detailed analysis of individual optimization mechanisms. Real applications provide ground truth evaluation but introduce complexity and variation that can obscure the impact of specific algorithmic improvements. A complete evaluation should include both types of benchmarks[4].

Speedup measurements compare the wall-clock execution time of the optimized approach with baseline implementations, quantifying the practical benefit. Speedup measurements must be interpreted carefully, accounting for measurement variation and ensuring that timing measurements accurately reflect actual system behavior rather than artifacts of measurement methodology. A speedup of 1.33× to 1.70× represents meaningful improvement (33 to 70 percent faster execution) but recognizes that no approach can universally achieve dramatic speedups[1].

Energy consumption measurements require instrumenting systems with accurate power measurement hardware or accessing built-in power measurement capabilities. For GPUs, power measurement might come from integrated power monitors on the GPU itself or through externally monitored current draw. Measurement uncertainty in power consumption can be substantial, and reported energy savings of 10 to 30 percent represent meaningful improvements given typical measurement uncertainties[2][28].

## Future Directions and Emerging Approaches

### Machine Learning-Based Scheduling

Machine learning approaches to scheduling represent an increasingly important research direction, leveraging historical execution data to train models that predict optimal scheduling decisions or predict task execution times under different scheduling conditions. Deep Neural Networks combined with genetic algorithms demonstrate potential to accelerate scheduling computation while maintaining scheduling quality[11]. However, these approaches introduce new challenges including generalization to new applications not seen during training, handling of distribution shift as workload patterns change, and providing performance guarantees or bounds on degradation.

Uncertainty-aware prediction approaches address the reality that machine learning models produce predictions with inherent uncertainty. By scaling predicted completion times by coefficients that account for prediction uncertainty, systems can ensure that tasks complete within predicted time bounds, maintaining schedule feasibility even when predictions include errors[37]. This represents an important step toward making machine learning-based scheduling practical for systems with strict performance requirements.

### Heterogeneous System Architecture Evolution

GPU and accelerator architectures continue evolving rapidly, with new capabilities and performance characteristics emerging regularly. NVIDIA's introduction of Multi-Instance GPU (MIG) technology enables finer-grained resource partitioning and isolation, opening new opportunities for scheduling flexibility. ARM-based GPUs and custom AI accelerators introduce additional diversity to heterogeneous systems. Scheduling frameworks must adapt to these architectural changes while remaining compatible with multiple generations of hardware.

The proliferation of specialized accelerators for specific tasks (cryptographic accelerators, video encoders, neural network inference engines) increases system heterogeneity dramatically. Scheduling frameworks designed for just CPU-GPU pairs may prove inadequate for systems with dozens of different accelerator types, each with unique characteristics, capabilities, and power consumption profiles. Developing scheduling techniques that scale to manage extreme heterogeneity represents an open research challenge.

### Energy-Aware Infrastructure and Demand Response

Future improvements in scheduling efficiency will likely come from closer integration with infrastructure-level energy management and potentially demand-responsive pricing. Data centers that can respond to grid conditions and energy prices in real-time might shift computation to periods when renewable energy is abundant or when energy prices are lower. Scheduling frameworks that incorporate this infrastructure-level information could achieve energy reductions beyond what optimized local scheduling alone can provide.

Temperature-aware scheduling that considers thermal conditions throughout the data center represents another emerging direction. Rather than treating temperature merely as a constraint to avoid thermal damage, sophisticated scheduling might shift computation to cooler regions of data centers or manage the temporal distribution of high-power tasks to smooth thermal and cooling requirements.

## Conclusion

The challenge of scheduling computational tasks in hybrid GPU-CPU architectures while balancing throughput and energy efficiency admits no universally optimal solution. The most effective approach depends on specific system characteristics, workload patterns, optimization priorities, and application requirements. Advanced scheduling frameworks such as HybriMoE demonstrate that dynamic, adaptive approaches incorporating real-time monitoring and intelligent resource management can achieve significant performance improvements over static approaches. Energy-aware scheduling methodologies combined with DVFS provide powerful tools for reducing energy consumption while maintaining throughput constraints, though their application requires sophisticated modeling of power consumption characteristics.

The optimal solution for most practical scenarios involves hybrid approaches that combine multiple techniques: load-aware scheduling decisions that account for processor heterogeneity, adaptive resource management that responds to runtime variations, feedback mechanisms that continuously adjust scheduler behavior, and careful trade-off analysis that balances competing objectives. Future scheduling systems will likely incorporate machine learning techniques for prediction and optimization, while remaining cognizant of the need to provide performance guarantees and maintain compatibility with diverse hardware configurations.

For practitioners implementing scheduling systems, the current state of research suggests several practical recommendations. First, invest in accurate modeling of task execution time and resource requirements specific to your system and workloads, recognizing that general models often prove inadequate. Second, implement dynamic scheduling that continuously adapts to runtime conditions rather than relying solely on static approaches. Third, carefully monitor both throughput and energy consumption metrics specific to your application requirements, avoiding the tendency to optimize for single metrics at the expense of others. Fourth, consider the overhead of scheduling decisions and monitoring, recognizing that highly sophisticated scheduling that incurs excessive overhead may provide no practical benefit compared to simpler approaches. Finally, remain flexible and prepared to evolve scheduling strategies as hardware capabilities and workload patterns change.

The field of heterogeneous system scheduling remains actively evolving, with new techniques, architectures, and applications continually emerging. The fundamental challenge of coordinating diverse processing elements toward efficient execution of heterogeneous workloads will remain relevant for the foreseeable future, continuing to motivate research into more sophisticated, adaptive, and efficient scheduling approaches.

## Annotations
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[2504.05897] HybriMoE: Hybrid CPU-GPU Scheduling and Cache ...', 'url': 'https://arxiv.org/abs/2504.05897'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Balancing Energy Efficiency and Real-Time Performance in GPU ...', 'url': 'https://par.nsf.gov/servlets/purl/10316388'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Heterogeneous computing - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Heterogeneous_computing'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Hybrid CPU-GPU scheduling and execution of tree traversals', 'url': 'https://engineering.purdue.edu/~milind/docs/ics16a.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Balancing Performance and Power Efficiency in Modern GPU ...', 'url': 'https://www.scitepress.org/Papers/2025/135879/135879.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Optimal load balancing for heterogeneous clusters', 'url': 'https://www.pace.cs.stonybrook.edu/heterogeneous-lb.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Work stealing for GPU-accelerated parallel programs in a global ...', 'url': 'https://pavanbalaji.github.io/pubs/2016/ccpe/ccpe16.ga_gpu.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Evaluation of Task Scheduling Algorithms in Heterogeneous ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC8433676/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Energy-Efficient Scheduling of Throughput-Constrained Streaming ...', 'url': 'https://liacs.leidenuniv.nl/~stefanovtp/pdf/SAMOS_17.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Work Stealing: Load-balancing for compute-heavy tasks', 'url': 'https://stack.convex.dev/work-stealing'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Task Scheduling for Heterogeneous Systems Using a Hybrid Deep ...', 'url': 'https://www.scitepress.org/Papers/2024/135108/135108.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Best Data Center Metrics for Performance & Efficiency - DartPoints', 'url': 'https://dartpoints.com/blog/best-data-center-metrics-for-performance-efficiency/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Dynamic Voltage/Frequency Scaling - Emergent Mind', 'url': 'https://www.emergentmind.com/topics/dynamic-voltage-frequency-scaling-dvfs'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Heterogeneous Earliest Finish Time Algorithm (HEFT) - YouTube', 'url': 'https://www.youtube.com/watch?v=ZSXo9WZg8Vk'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Performance-Per-Watt Optimization with Variable Operating Voltage', 'url': 'https://www.synopsys.com/implementation-and-signoff/physical-implementation/fusion-compiler/variable-voltage-optimization-technique.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'What is dynamic voltage and frequency scaling (DVFS) - TechTarget', 'url': 'https://www.techtarget.com/whatis/definition/dynamic-voltage-and-frequency-scaling-DVFS'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'HEFT-Scheduling Algorithm - GitHub', 'url': 'https://github.com/hackerkid/HEFT-Scheduling'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[1407.8116] Optimizing performance per watt on GPUs in High ...', 'url': 'https://arxiv.org/abs/1407.8116'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'HAMM: A Hybrid Algorithm of Min-Min and Max-Min Task ... - SSRN', 'url': 'https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3922243'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '11 Load Balancing Metrics You Need to Measure and Why It Matters', 'url': 'https://www.arraynetworks.com/load-balancer-important-metrics-impacting-performance'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'ML Inference Scheduling with Predictable Latency - arXiv', 'url': 'https://arxiv.org/html/2512.18725v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A Min-Min Max-Min Selective Algorithm for Grid Task Scheduling', 'url': 'https://www.semanticscholar.org/paper/A-Min-Min-Max-Min-Selective-Algorithm-for-Grid-Task-Etminani-Naghibzadeh/d2e4b0333e07d4ab24a072cc88b5435100c61db3'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '6 Load Balancing Metrics to Monitor - Serverion', 'url': 'https://www.serverion.com/uncategorized/6-load-balancing-metrics-to-monitor/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'CoreTuner: Predicting and Scheduling Framework for Optimizing the ...', 'url': 'https://dl.acm.org/doi/10.1145/3754598.3754634'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Energy-Aware Scheduling: Definition, Examples, and Applications', 'url': 'https://www.graphapp.ai/engineering-glossary/cloud-computing/energy-aware-scheduling'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Abstract I. INTRODUCTION II. SYSTEM MODEL - Purdue Engineering', 'url': 'https://engineering.purdue.edu/~ee695n/protected/project1_sol.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'GPU and CPU Particle Swarm Optimization (PSO) Repository - GitHub', 'url': 'https://github.com/mohammad95labbaf/Parallel-PSO-GPU-CPU'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Multi-Objective Approach for Energy-Aware Workflow Scheduling in ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3835373/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Analyzing the Performance of Greedy Maximal Scheduling via Local ...', 'url': 'https://web.math.princeton.edu/~mchudnov/lpconf.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] GPU Parallelization for Particle Swarm Optimization Algorithms - arXiv', 'url': 'https://arxiv.org/pdf/2205.01313.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Asymptotic Analysis of an Algorithm for Balanced Parallel Processor ...', 'url': 'https://epubs.siam.org/doi/10.1137/0221007'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Energy-efficient Load-balanced Heterogeneous Mobile Cloud', 'url': 'https://calhoun.nps.edu/server/api/core/bitstreams/374bf913-c8ee-425e-8a17-6415a0353e91/content'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A Survey of Real-time Scheduling on Accelerator-based ... - arXiv', 'url': 'https://arxiv.org/html/2505.11970v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'On the Asymptotic Optimality of Multiprocessor Scheduling ...', 'url': 'https://pubsonline.informs.org/doi/10.1287/ijoc.7.2.201'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Heterogeneous Energy-aware Load Balancing for Industry 4.0 and ...', 'url': 'https://dl.acm.org/doi/full/10.1145/3543859'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Real-time, Work-conserving GPU Scheduling for Concurrent DNN ...', 'url': 'https://dl.acm.org/doi/10.1145/3768622'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Task Completion Time Prediction Scaled by Machine Learning ...', 'url': 'https://dl.ifip.org/db/conf/cnsm/cnsm2024/1571066160.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Understanding GPU Resource Interference One Level Deeper', 'url': 'https://anakli.inf.ethz.ch/papers/gpu_interference_socc25.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Load Balancing Algorithms and Techniques - Kemp Technologies', 'url': 'https://kemptechnologies.com/load-balancer/load-balancing-algorithms-techniques'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Predicting Job Idle Time before Execution using Machine Learning', 'url': 'https://indico.cern.ch/event/1167965/contributions/5003402/attachments/2494438/4284031/USCMS%20Francisco.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Interference-driven resource management for GPU-based ...', 'url': 'https://dl.acm.org/doi/10.1145/2287076.2287091'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Load-Balancing-Aware Scheduling Algorithm - Emergent Mind', 'url': 'https://www.emergentmind.com/topics/load-balancing-aware-scheduling-algorithm'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Online Energy‐Aware Scheduling for Deadline‐Constrained ...', 'url': 'https://onlinelibrary.wiley.com/doi/10.1155/2024/2122895'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Peformance Isolation for Inference Processes in Edge GPU Systems', 'url': 'https://arxiv.org/html/2601.07600v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Adaptive Real-Time Scheduling Algorithms for Embedded Systems', 'url': 'https://arxiv.org/abs/2512.21364'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'DASH: Deadline-Aware High-Performance Memory Scheduler for ...', 'url': 'https://dl.acm.org/doi/abs/10.1145/2847255'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Efficient Performance-Aware GPU Sharing with Compatibility and ...', 'url': 'https://www.usenix.org/system/files/atc25-zhang-shulai.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Feedback Control Real-Time Scheduling: Framework, Modeling ...', 'url': 'https://www.cs.virginia.edu/~stankovic/psfiles/rtsj.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Lyapunov stability - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Lyapunov_stability'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Lucky scheduling for energy-efficient heterogeneous multi-core ...', 'url': 'https://www.usenix.org/system/files/conference/hotpower12/hotpower12-final34.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] EMCS: An Energy-Efficient Makespan Cost-Aware Scheduling ...', 'url': 'https://www.diva-portal.org/smash/get/diva2:1716659/FULLTEXT01.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Ch. 9 - Lyapunov Analysis - Underactuated Robotics', 'url': 'http://underactuated.mit.edu/lyapunov.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Fairness-Aware Scheduling on Single-ISA Heterogeneous Multi-Cores', 'url': 'https://users.elis.ugent.be/~leeckhou/papers/pact13.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Power-Aware Scheduling for Makespan and Flow - Knox College', 'url': 'http://faculty.knox.edu/dbunde/pubs/poweraware-j.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Work-Conserving Distributed Schedulers for Terabit Routers', 'url': 'https://www.arl.wustl.edu/~jon.turner/pubs/2004/sigcomm04.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Power-Efficient Load-Balancing on Heterogeneous Computing ...', 'url': 'https://www.date-conference.com/proceedings-archive/2016/pdf/0898.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Energy-efficient Task Scheduling for CPU-GPU Hybrid Clusters ...', 'url': 'http://www.comp.hkbu.edu.hk/v1/proj/sre/2018/xc/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Work-conserving scheduler - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Work-conserving_scheduler'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Load Balancing Strategies in Heterogeneous Environments - SUAS', 'url': 'https://www.suaspress.org/ojs/index.php/JCTAM/article/download/v1n2a02/v1n2a02/126'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'ONLINE SCHEDULING OF MIXED CPU-GPU JOBS', 'url': 'https://www.worldscientific.com/doi/10.1142/S0129054114500312'}}

## Sources
https://arxiv.org/abs/2504.05897
https://par.nsf.gov/servlets/purl/10316388
https://en.wikipedia.org/wiki/Heterogeneous_computing
https://engineering.purdue.edu/~milind/docs/ics16a.pdf
https://www.scitepress.org/Papers/2025/135879/135879.pdf
https://www.pace.cs.stonybrook.edu/heterogeneous-lb.html
https://pavanbalaji.github.io/pubs/2016/ccpe/ccpe16.ga_gpu.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC8433676/
https://liacs.leidenuniv.nl/~stefanovtp/pdf/SAMOS_17.pdf
https://stack.convex.dev/work-stealing
https://www.scitepress.org/Papers/2024/135108/135108.pdf
https://dartpoints.com/blog/best-data-center-metrics-for-performance-efficiency/
https://www.emergentmind.com/topics/dynamic-voltage-frequency-scaling-dvfs
https://www.youtube.com/watch?v=ZSXo9WZg8Vk
https://www.synopsys.com/implementation-and-signoff/physical-implementation/fusion-compiler/variable-voltage-optimization-technique.html
https://www.techtarget.com/whatis/definition/dynamic-voltage-and-frequency-scaling-DVFS
https://github.com/hackerkid/HEFT-Scheduling
https://arxiv.org/abs/1407.8116
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3922243
https://www.arraynetworks.com/load-balancer-important-metrics-impacting-performance
https://arxiv.org/html/2512.18725v1
https://www.semanticscholar.org/paper/A-Min-Min-Max-Min-Selective-Algorithm-for-Grid-Task-Etminani-Naghibzadeh/d2e4b0333e07d4ab24a072cc88b5435100c61db3
https://www.serverion.com/uncategorized/6-load-balancing-metrics-to-monitor/
https://dl.acm.org/doi/10.1145/3754598.3754634
https://www.graphapp.ai/engineering-glossary/cloud-computing/energy-aware-scheduling
https://engineering.purdue.edu/~ee695n/protected/project1_sol.pdf
https://github.com/mohammad95labbaf/Parallel-PSO-GPU-CPU
https://pmc.ncbi.nlm.nih.gov/articles/PMC3835373/
https://web.math.princeton.edu/~mchudnov/lpconf.pdf
https://arxiv.org/pdf/2205.01313.pdf
https://epubs.siam.org/doi/10.1137/0221007
https://calhoun.nps.edu/server/api/core/bitstreams/374bf913-c8ee-425e-8a17-6415a0353e91/content
https://arxiv.org/html/2505.11970v1
https://pubsonline.informs.org/doi/10.1287/ijoc.7.2.201
https://dl.acm.org/doi/full/10.1145/3543859
https://dl.acm.org/doi/10.1145/3768622
https://dl.ifip.org/db/conf/cnsm/cnsm2024/1571066160.pdf
https://anakli.inf.ethz.ch/papers/gpu_interference_socc25.pdf
https://kemptechnologies.com/load-balancer/load-balancing-algorithms-techniques
https://indico.cern.ch/event/1167965/contributions/5003402/attachments/2494438/4284031/USCMS%20Francisco.pdf
https://dl.acm.org/doi/10.1145/2287076.2287091
https://www.emergentmind.com/topics/load-balancing-aware-scheduling-algorithm
https://onlinelibrary.wiley.com/doi/10.1155/2024/2122895
https://arxiv.org/html/2601.07600v1
https://arxiv.org/abs/2512.21364
https://dl.acm.org/doi/abs/10.1145/2847255
https://www.usenix.org/system/files/atc25-zhang-shulai.pdf
https://www.cs.virginia.edu/~stankovic/psfiles/rtsj.pdf
https://en.wikipedia.org/wiki/Lyapunov_stability
https://www.usenix.org/system/files/conference/hotpower12/hotpower12-final34.pdf
https://www.diva-portal.org/smash/get/diva2:1716659/FULLTEXT01.pdf
http://underactuated.mit.edu/lyapunov.html
https://users.elis.ugent.be/~leeckhou/papers/pact13.pdf
http://faculty.knox.edu/dbunde/pubs/poweraware-j.pdf
https://www.arl.wustl.edu/~jon.turner/pubs/2004/sigcomm04.pdf
https://www.date-conference.com/proceedings-archive/2016/pdf/0898.pdf
http://www.comp.hkbu.edu.hk/v1/proj/sre/2018/xc/
https://en.wikipedia.org/wiki/Work-conserving_scheduler
https://www.suaspress.org/ojs/index.php/JCTAM/article/download/v1n2a02/v1n2a02/126
https://www.worldscientific.com/doi/10.1142/S0129054114500312