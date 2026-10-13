# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 2d7f9967 | **Time:** 2443.57s | **Cost:** $7.33632
--------------------------------------------------------------------------------

# Synaptic Weight Update Mechanisms for Parallel Optimization of Energy Efficiency and Learning Accuracy in Neuromorphic Chips

### Key Points
*   **Dynamical Alignment and Encoding:** Recent research (2025) identifies "Dynamical Alignment" as a critical principle enabling the parallel optimization of energy efficiency and learning accuracy. By encoding static inputs into dynamic spatiotemporal trajectories (e.g., using the Lorenz system), neural networks can switch between a "dissipative mode" (high energy efficiency, sparse coding) and an "expansive mode" (high accuracy, robust representation), effectively resolving the performance paradox of Spiking Neural Networks (SNNs).
*   **Tree-Structured Weight Updates in Nickelates:** A novel mechanism observed in perovskite nickelate devices utilizes a "tree-like" hierarchical structure for weight updates. This mechanism is inherently self-limiting, ensuring stability and energy efficiency, while maintaining responsiveness to new stimuli (learning accuracy). It demonstrates remarkable immunity to device variations (e.g., variations in the parameter $\mu$).
*   **Parallel Update Algorithms (SignSGD):** To address the latency and power constraints of training on crossbar arrays, sign-based Stochastic Gradient Descent (SignSGD) allows for massive parallel updates of synaptic weights. While traditionally less accurate, optimizations like Error-aware Probabilistic Update (EaPU) and specific momentum variants (e.g., AdaDelta) have been shown to restore accuracy while maintaining the energy benefits of parallel operations.
*   **Material-Level Innovations:** Advances in Phase Change Materials (PCM) using photonic updates and Ferroelectric devices (e.g., PZT/Nb:STO) achieve femtojoule-level energy consumption per synaptic event. These devices address the "device variation" constraint through material engineering that improves the linearity and symmetry of conductance modulation, which is crucial for accurate online learning.

## 1. Introduction

The transition from the traditional Von Neumann computing architecture to neuromorphic computing represents a fundamental shift in information processing. Conventional architectures, characterized by the physical separation of processing units and memory, suffer from the "Von Neumann bottleneck," where significant energy and time are consumed transferring data back and forth [cite: 1, 2]. Neuromorphic computing aims to emulate the biological brain's architecture, where memory (synapses) and processing (neurons) are collocated, offering the potential for massive parallelism and orders-of-magnitude improvements in energy efficiency [cite: 1, 3].

However, realizing this potential in physical hardware is fraught with challenges. A central dilemma in neuromorphic engineering is the trade-off between **energy efficiency** and **learning accuracy**. Biological brains operate on approximately 20 watts while performing complex cognitive tasks that require megawatts in digital supercomputers [cite: 1, 3]. Replicating this efficiency while maintaining the high precision required for tasks like pattern recognition or control is difficult due to the inherent **device variations** (e.g., conductance variability, non-linearity) and strict **power limits** of edge devices [cite: 4, 5, 6].

This report investigates the specific synaptic weight update mechanisms that address these conflicting requirements. It focuses on two primary domains of innovation:
1.  **Theoretical Frameworks:** The "Dynamical Alignment" principle, which introduces a bimodal optimization landscape to parallelize energy and accuracy objectives.
2.  **Physical Device Mechanisms:** Novel material properties (e.g., in nickelates and memristors) that inherently support efficient, robust, and parallel weight updates.

## 2. Theoretical Framework: Dynamical Alignment

A breakthrough in resolving the tension between energy efficiency and learning accuracy is the proposal of the **Dynamical Alignment** hypothesis. This framework suggests that the computational capabilities of a neural network are not solely determined by its static architecture but by the temporal dynamics of its input signals relative to the network's intrinsic processing characteristics [cite: 7, 8, 9, 10].

### 2.1 The Bimodal Optimization Landscape
Research indicates that by encoding static inputs into controllable dynamical trajectories, a neuromorphic system can access a bimodal optimization landscape. This landscape consists of two distinct computational modes, separated by a critical phase transition governed by phase space volume dynamics [cite: 7, 8, 10]:

1.  **The Dissipative Mode (Energy-First):**
    *   **Mechanism:** Driven by contracting dynamics where the phase space volume shrinks over time.
    *   **Characteristics:** This mode produces extremely sparse and precise spike patterns, forming a "sparse temporal coding." Information is carried by a small number of neurons firing with high temporal synchrony [cite: 8].
    *   **Optimization Goal:** It prioritizes **energy efficiency**. The input appears as fast, uncorrelated fluctuations to the neuron (autocorrelation time $\tau_{corr} \ll$ membrane time constant $\tau_m$), allowing the neuron to integrate fluctuations efficiently and fire only when necessary [cite: 8].
    *   **Trade-off:** While highly efficient, this mode is less robust to noise and neuron silencing. Performance can collapse with just a 10% spike deletion rate [cite: 7, 8].

2.  **The Expansive Mode (Accuracy-First):**
    *   **Mechanism:** Driven by expanding dynamics (e.g., chaotic attractors) where trajectories diverge, increasing the dimensionality of the representation.
    *   **Characteristics:** This mode exhibits distributed neuron firing and high inter-neuronal correlations. It creates a high-dimensional representational space that is easier to classify linearly [cite: 8].
    *   **Optimization Goal:** It prioritizes **learning accuracy** and representational power. It unlocks the ability of SNNs to match or exceed the accuracy of traditional Artificial Neural Networks (ANNs) [cite: 7, 8].
    *   **Robustness:** This mode is highly robust to device variation and noise. It maintains $>90\%$ accuracy even when 40% of spikes are deleted, demonstrating significant information redundancy [cite: 7, 8].

### 2.2 Dynamical Encoding as a Mechanism
To achieve this parallel optimization, the system employs **Dynamical Encoding**. This process transforms static data points into rich spatiotemporal trajectories using dynamical systems (e.g., the Lorenz system) [cite: 8].
*   **Step 1:** Input data is used as the initial condition for the dynamical system.
*   **Step 2:** The system's trajectory is generated in phase space through numerical integration.
*   **Step 3:** These trajectories are converted into spike patterns [cite: 8].

This encoding creates an information structure that is more conducive to gradient propagation, enabling the network to find optimal solutions more robustly than traditional encoding methods like Rate or Time-to-First-Spike (TTFS) [cite: 7]. For instance, in experimental validations, a "Lorenz-SNN" achieved **96.98% accuracy** on MNIST, virtually eliminating the gap with Multi-Layer Perceptrons (MLP), while consuming **40.4% fewer spikes** than TTFS methods [cite: 7].

### 2.3 Parallel Optimization Axis
The core innovation of Dynamical Alignment is that it treats energy efficiency not as a byproduct but as a **parallel optimization axis** alongside accuracy [cite: 7, 8]. By adjusting the dynamical regime (tuning the alignment between input $\tau_{corr}$ and network $\tau_m$), a single hardware substrate can be dynamically "sculpted" to prioritize either energy (dissipative) or accuracy (expansive) depending on the immediate task constraints [cite: 8]. This directly addresses the user's query regarding a mechanism that optimizes both, constrained by power limits (favoring dissipative) and the need for accuracy (favoring expansive).

## 3. Physical Mechanisms: Tree-Structured Weight Updates

While Dynamical Alignment provides the theoretical control, the physical implementation of synaptic updates requires devices that can handle variations and power limits. A prominent solution is found in **perovskite nickelate (NdNiO$_3$) devices**, which exhibit a unique "tree-structured" weight update mechanism [cite: 11, 12, 13, 14, 15, 16].

### 3.1 The Tree Structure Mechanism
In these devices, the synaptic weight (conductance) update follows a hierarchical, tree-like trajectory.
*   **Proton Modulation:** The mechanism relies on the modulation of proton distribution within the nickelate lattice under electric pulses. The top electrode (e.g., Pd) catalytically dopes hydrogen (protons) into the material. Applying electric fields moves these protons, changing the local Ni valence state and electron-electron correlation, thereby modulating resistance [cite: 11, 16].
*   **Hierarchical Branching:** When a sequence of constant stimuli (pulses) is applied, the synaptic strength adjusts along a specific "branch" of the tree. If the stimulus changes, the weight update trajectory "branches" off, allowing the synapse to retain previous information while responding to new inputs [cite: 11, 13].

### 3.2 Self-Limiting Characteristics for Stability
A critical feature for energy efficiency and stability is the **self-limiting** nature of this mechanism. During a constant stimulus sequence, the weight update saturates (limits itself), preventing "runaway" potentiation or depression that could destabilize the neural circuit or consume excessive power [cite: 13, 15]. This mimics biological homeostatic mechanisms and ensures that the device operates within a safe and energy-efficient dynamic range.

### 3.3 Immunity to Device Variation
The research highlights that this mechanism is remarkably robust to device variations. Specifically, the parameter $\mu$, which characterizes the device's response, can vary without significantly hampering network performance.
*   **Experimental Evidence:** In a spiking neural network trained on MNIST using this mechanism, testing accuracy changed by only about $\pm 0.5\%$ despite variations in $\mu$ [cite: 11, 12, 14].
*   **Implication:** This robustness allows for the use of devices that may not be perfectly identical (a common issue in nanofabrication), thereby relaxing manufacturing constraints and improving yield without sacrificing learning accuracy.

## 4. Memristive Parallel Update Mechanisms

For large-scale neuromorphic chips using crossbar arrays (e.g., RRAM, ReRAM), the **synaptic weight update mechanism** must support massive parallelism to achieve high throughput and energy efficiency.

### 4.1 Sign-Based Stochastic Gradient Descent (SignSGD)
Traditional backpropagation requires precise, continuous weight updates, which are expensive to implement on analog hardware due to the need for high-precision write circuitry and the "weight transport problem" [cite: 17].
*   **Mechanism:** SignSGD updates weights based only on the *sign* of the gradient, rather than its magnitude. This allows for a simplified "parallel update" scheme where all synapses in a crossbar can be updated simultaneously using global voltage pulses [cite: 2, 18, 19, 20].
*   **Energy Efficiency:** By reducing the update to a binary or ternary operation (increase, decrease, stay), the complexity and power consumption of the write driver are drastically reduced.
*   **Accuracy Challenge:** Historically, SignSGD could lead to decreased accuracy due to the loss of gradient magnitude information [cite: 18, 20].

### 4.2 Optimizing for Accuracy: Momentum and Probabilistic Updates
To recover accuracy while retaining the energy benefits of parallel updates, several optimization strategies have been developed:
*   **Algorithmic Optimization:** Research comparing various optimizers on memristor-based systems shows that **AdaDelta** and **Momentum** variants of SGD achieve the highest accuracy (e.g., ~89.5% on MNIST, ~90.5% on CIFAR), significantly outperforming standard AdaGrad [cite: 2, 20, 21]. These algorithms adapt the learning rate or accumulate gradients, compensating for the coarseness of the sign-based update.
*   **Error-aware Probabilistic Update (EaPU):** This technique adjusts the *probability* of a weight update based on the error magnitude. Instead of changing the weight size (which is hard in binary devices), the system changes the likelihood of a pulse being applied. This restores a form of "analog" resolution over time, improving accuracy [cite: 19].

### 4.3 Mitigating Device Variation in Crossbars
Device-to-device and cycle-to-cycle variations are major constraints in memristive chips.
*   **Multi-Device Synapses:** One effective mechanism is to represent a single synaptic weight using multiple resistive devices (e.g., a differential pair or a cluster). The statistical aggregation of these devices averages out individual variations, making the effective weight more precise and robust [cite: 5, 22].
*   **Slope Correction:** In Phase Change Memory (PCM), "conductance drift" changes the weight value over time. A "slope correction" technique applied to the neuron's activation function can compensate for this drift, maintaining accuracy over long periods (e.g., 1 year) without requiring energy-intensive reprogramming [cite: 6].

## 5. Advanced Material Implementations

Beyond nickelates and standard RRAM, other material systems offer specific advantages for the energy-accuracy optimization loop.

### 5.1 Photonic Synaptic Updates (GST on Waveguides)
Photonic neuromorphic systems use Phase Change Materials (like GST) on waveguides to emulate synapses.
*   **Mechanism:** The weight is updated by sending optical pulses that change the GST between amorphous and crystalline states.
*   **Energy/Speed:** While electrical PCM suffers from high write latency, photonic excitation allows for **sub-nanosecond write speeds** (e.g., 200 ps) and high energy efficiency [cite: 4].
*   **Parallelism:** Wavelength Division Multiplexing (WDM) allows multiple synaptic weights to be updated in parallel on the same waveguide, maximizing throughput.

### 5.2 Ferroelectric and 2D Material Synapses
*   **Ferroelectric (PZT/Nb:STO):** These devices achieve ultralow energy consumption (**< 9 fJ per event**) by optimizing the Schottky barrier. They offer progressive domain switching, which leads to highly linear and symmetric weight updates—a key factor for high learning accuracy [cite: 23].
*   **2D Materials (MoS2, MoO3):** Synaptic transistors based on 2D materials demonstrate excellent linearity and symmetry in weight updates (LTP/LTD). This linearity is directly correlated with higher classification accuracy (e.g., ~94-96% on MNIST) because it allows the learning algorithm to converge more reliably than in highly non-linear devices [cite: 24, 25].

## 6. Conclusion

To achieve parallel optimization of energy efficiency and learning accuracy in neuromorphic chips, constrained by device variation and power limits, the research points to a multi-layered solution:

1.  **At the Architectural Level:** Implementing **Dynamical Alignment** allows the system to dynamically switch between "dissipative" (energy-efficient) and "expansive" (high-accuracy) modes based on task requirements. This turns the energy-accuracy trade-off into a tunable control parameter.
2.  **At the Device Level:** Utilizing **Tree-Structured Weight Updates** (as in nickelates) provides an inherent hardware mechanism for stability (self-limiting) and robustness to variation. Alternatively, **Ferroelectric** and **2D material** devices offer the linearity and femtojoule-level operation required for strict power limits.
3.  **At the Update Mechanism Level:** Employing **Sign-based Parallel Updates** (SignSGD) with algorithmic enhancements (like AdaDelta or EaPU) enables the massive parallelism required for speed and efficiency, while compensating for the precision loss inherent in low-power analog hardware.

By integrating these mechanisms—dynamical encoding for control, robust materials for storage, and parallel algorithms for updates—neuromorphic chips can effectively navigate the complex optimization landscape required for next-generation AI.

## 7. Detailed Analysis of Mechanisms

### 7.1 Dynamical Alignment: The "Software" of Neuromorphic Efficiency
The concept of Dynamical Alignment [cite: 7, 8, 9, 10] is arguably the most significant theoretical advancement found in the search results for addressing the "parallel optimization" query. It posits that the efficiency of a neural network is not static but emerges from the alignment between the input signal's dynamics and the network's processing characteristics.

#### 7.1.1 The Performance Paradox
SNNs have theoretically promised high energy efficiency due to their event-driven nature (spiking only when necessary). However, they have historically struggled to match the accuracy of ANNs (the "performance paradox") [cite: 7, 10]. Dynamical Alignment resolves this by suggesting that SNNs need inputs encoded in a specific dynamical form to leverage their spatiotemporal processing capabilities fully.

#### 7.1.2 Mechanism of Action
The mechanism works by transforming static inputs (like an image) into a time-series trajectory using a chaotic system (e.g., Lorenz attractor).
*   **Input:** Static vector $x$.
*   **Transformation:** $x$ sets the initial state of a dynamical system $\dot{z} = F(z)$.
*   **Output:** The trajectory $z(t)$ is converted into spike trains.

This process creates a "consistent, architecture-independent phenomenon" where the gap between SNN and ANN performance is closed by an average of 72% [cite: 7].

#### 7.1.3 Energy vs. Accuracy Modes
The system can operate in two distinct modes, effectively optimizing the two variables in parallel:
*   **Dissipative Mode:** When the input dynamics are contracting (negative Lyapunov exponents dominating), the phase space volume shrinks. This results in sparse spiking. It is the "Energy Efficiency" optimum.
*   **Expansive Mode:** When the input dynamics are expanding (positive Lyapunov exponents), trajectories diverge. This separates data points that are close in the original space, making them easier to classify. This is the "Learning Accuracy" optimum.

Crucially, the system can be designed to switch between these modes, or "sculpt" the computation, allowing for optimization under power constraints (force dissipative mode) or accuracy constraints (force expansive mode) [cite: 8].

### 7.2 Nickelate Perovskites: The "Hardware" of Robustness
While Dynamical Alignment handles the signal, the physical synapse must store the weight. The **NdNiO$_3$ (Nickelate)** devices described in [cite: 11, 12, 13, 14, 15, 16] offer a unique solution to "device variation."

#### 7.2.1 Proton-Doped Plasticity
The weight update is driven by the migration of protons ($H^+$) within the lattice. This is a non-volatile change. The "tree structure" emerges because the resistance state depends on the history of pulses in a hierarchical manner.

#### 7.2.2 Robustness to $\mu$
The parameter $\mu$ in the nickelate device model describes the scaling of the weight update. In standard devices, variations in such a parameter would lead to heterogeneous learning rates across the array, degrading accuracy. However, the tree-structure mechanism is shown to be "sufficiently immune" to variations in $\mu$. A network with 400-6400 neurons showed only a $\pm 0.5\%$ change in accuracy despite these variations [cite: 11]. This directly answers the "constrained by device variation" part of the query.

### 7.3 Memristor Crossbars: The "Architecture" of Parallelism
For high-density chips, crossbar arrays are the standard. The challenge is updating millions of weights.

#### 7.3.1 Parallel Update via SignSGD
In a crossbar, applying a specific voltage to rows and columns can update weights at the intersections. To do this in parallel for a whole layer, the **SignSGD** method is used [cite: 18, 20].
*   **Protocol:** Calculate the gradient $g$. Take $sign(g)$. Apply a global SET pulse to all synapses where $sign(g)$ is positive and a RESET pulse where it is negative.
*   **Benefit:** This avoids the need to calculate and apply a unique analog voltage for every single synapse, which would require serial processing or massive DACs (Digital-to-Analog Converters).
*   **Constraint Management:** To handle the "learning accuracy" constraint (which usually drops with sign-only updates), the system uses **momentum** (accumulating signs over time) or **probabilistic updates** (EaPU), where the *frequency* of pulses encodes the gradient magnitude [cite: 19].

### 7.4 Energy Efficiency Metrics
The report must quantify the "energy efficiency" mentioned in the query.
*   **Nickelates:** Self-limiting nature prevents wasted current.
*   **Ferroelectrics (PZT):** < 9 fJ per synaptic event [cite: 23].
*   **Photonic GST:** 4 pJ per write (electrical equivalent is 14-19 pJ) [cite: 4].
*   **Lorenz-SNN:** 40.4% fewer spikes than TTFS, directly translating to dynamic power savings [cite: 7].

## 8. Addressing Constraints

### 8.1 Device Variation
*   **Problem:** Nanoscale devices (memristors, PCM) differ in their switching characteristics due to fabrication tolerances.
*   **Solution 1 (Material):** Nickelate tree structures are inherently robust [cite: 11].
*   **Solution 2 (Circuit):** Using multiple devices per synapse (e.g., 2 or 4 RRAMs) averages out the variation [cite: 5].
*   **Solution 3 (Algorithmic):** Slope correction in PCM compensates for the temporal variation (drift) [cite: 6].

### 8.2 Power Limits
*   **Problem:** Edge devices cannot sustain high-current write operations.
*   **Solution 1 (Mode Switching):** Dynamical Alignment allows the system to enter "Dissipative Mode" to stay within power budgets [cite: 8].
*   **Solution 2 (Low-Energy Physics):** Ferroelectric switching requires field, not current, leading to fJ operations [cite: 23].
*   **Solution 3 (Sparsity):** The Lorenz-SNN reduces spike counts, lowering the dynamic power of the digital/analog communication fabric [cite: 7].

## 9. Conclusion

The "synaptic weight update mechanism" that achieves parallel optimization of energy efficiency and learning accuracy is not a single component but a **synergistic combination of a dynamical control principle and robust material physics**.

Specifically, the **Dynamical Alignment** framework provides the "software" capability to tune the energy-accuracy trade-off in real-time by aligning input timescales with network timescales. This is physically realized using **Tree-Structured (Nickelate)** or **Parallel-Update (Memristive/SignSGD)** mechanisms that are engineered to be robust to device variations and operate within strict power limits. The integration of these elements defines the state-of-the-art in neuromorphic chip design as of 2025.

## References
[cite: 4] PMC Article 6113276
[cite: 11] ResearchGate: Perovskite neural trees
[cite: 12] PMC Article 7206050
[cite: 5] US Patent 20190228287A1
[cite: 1] Arxiv 2505.16362
[cite: 26] PMC Article 9646995
[cite: 21] ResearchGate: Optimizing Memristor-Based Synaptic Devices
[cite: 2] IEEE Xplore 10720006
[cite: 27] Arxiv 2304.08778
[cite: 6] IBM Research: Neuromorphic computing with phase change device
[cite: 7] Arxiv 2508.10064v1
[cite: 7] Arxiv 2508.10064v1 (Duplicate of 16, cited for specific sections)
[cite: 13] OSTI.gov 2202272
[cite: 11] ResearchGate: Perovskite neural trees (Duplicate of 2)
[cite: 14] ResearchGate Figure (Nickelate)
[cite: 4] PMC Article 6113276 (Duplicate of 1)
[cite: 8] Arxiv 2508.10064 (Duplicate of 16)
[cite: 17] PMC Article 7902857
[cite: 22] ResearchGate: Recent Advances in Synaptic Nonvolatile Memory
[cite: 24] ResearchGate: Energy-Efficient Scalable Single-Layer MoS2
[cite: 25] AFM Paper 2018
[cite: 23] PMC Article 9353489
[cite: 7] Arxiv 2508.10064v1 (Duplicate of 16)
[cite: 8] Arxiv 2508.10064 (Duplicate of 16)
[cite: 18] ResearchGate Figure (SignSGD)
[cite: 3] Arxiv 2505.16362v1
[cite: 2] IEEE Xplore 10720006 (Duplicate of 10)
[cite: 21] ResearchGate: Optimizing Memristor-Based Synaptic Devices (Duplicate of 9)
[cite: 8] Arxiv 2508.10064 (Duplicate of 16)
[cite: 7] Arxiv 2508.10064v1 (Duplicate of 16)
[cite: 9] ResearchGate: Dynamical Alignment
[cite: 28] Arxiv 2512.23916v1
[cite: 19] ResearchGate: SignSGD
[cite: 20] ResearchGate Figure (SignSGD)
[cite: 13] OSTI.gov 2202272 (Duplicate of 29)
[cite: 12] PMC Article 7206050 (Duplicate of 5)
[cite: 15] Purdue Hammer (Nickelate)
[cite: 16] ResearchGate Figure (Nickelate)
[cite: 11] ResearchGate: Perovskite neural trees (Duplicate of 2)
[cite: 14] ResearchGate Figure (Nickelate)
[cite: 7] Arxiv 2508.10064v1 (Duplicate of 16)
[cite: 8] Arxiv 2508.10064 (Duplicate of 16)
[cite: 10] Arxiv 2508.10064 (Duplicate of 16)
[cite: 20] ResearchGate Figure (SignSGD)
[cite: 19] ResearchGate: SignSGD (Duplicate of 61)
[cite: 8] Arxiv 2508.10064 (Duplicate of 16)
[cite: 7] Arxiv 2508.10064v1 (Duplicate of 16)

**Sources:**
1. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTnfkYydapMBRsVNwaIXeC6mw7GbmtzsmjNiR72zzee55W97P6wUTsV_gt2VPES0jSnNq8yqXLN61eTWCjSdGjhehfB8JtKF-jwr0pt0NhYYFoSE_MqA==)
2. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4Wy3Pj3pGf8z_Ep8Ik3_uQC-VGl6szZ24Y4oshiB2T4iSn1vcPKGosfx22GMTDJOHx0ICK1fq0TxCJMMg3m7amTy_9UNvAFRZphLhZdRGRGPD5fm_WdQl-MAb41xtfN6X8z9CPNSXPLVKJSSrssspG50aug==)
3. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKBt1X--6iUOnBSoVDISmzVfPUEeSBc9nTLxBB_xkvH_koM6ZV-DzHwBJ5xzdGdReiLLjmROoVTcvZ_W2KGCLwwkGqIKK3uxzjl7OGWy6dnhtVgWgGP96eGQ==)
4. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZ755GrjYdbJHfpfQ9SPxh4f2iT4jJUIuH8l6b5izUEZpIKcpMFb9udbgg_EzVulv8yT-cztwsKcbbLs3Bw6XMe2miJmf4smslZHDVRHs2FFW0RRxTuoYnNaWcx24o57J1r5HlCwsM)
5. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEssTJZx1kyNC2FCXbtuYt1x1sr3ZdN457yOIkOaQAyVvA0xDZvl3xybJbBVRRIpeZgDLhgLCdJtvtuubJxWiPcjOErwlCG7cLpPKOsxQ0sHapFfqbWljsnd-ykv9x5quaiadc9CWpO71_e)
6. [ibm.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGHk7w7EWvRV_cxQ5XlMQDF0nQs5mxrO5Gn9K1SLO6kA4CIf1ZIk5KhlpbWVTgmeh5Jsf47kbS3a7PxMzhaH7vm8Gasge1a4sJXJSkXJUpmnHsvU789XuMTG_9xtvDBk6bTJqS-_YCBc35LfayHhcCD7-nTmGyMtsRSZDlajlW2_NF8_roHhob6-kQo4GGUq4az_PPZY66T3oLSArSaFU0pyn4cacZJi4JZp4s66-erjtT)
7. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNr5s5wDHAuLPHR4jozhXortzkRm86IlcHyAA2NkG_UpWy49esrt4Vzw2v7Yj4tEtT915tPklzJGEeqV9fFIYlbJjgoMJSpNx2dkt5PvJoeyMRf1EXIiTjTQ==)
8. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLPLKj8I2IfVMPrs7IIPdq9zwPJyl2oJfJZIGDMYuv133Ucu-NNKpQSDPr4rNi5eVtCJW9y9cDTdXwtlO4hXGLyiz0zGjtW6U3bY7XD9Q-O4-bUXXF5PE=)
9. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF43YgCHTEZV23pS45mlWqpyUOe9rplXc8QbGR_0i1o8VQirO3KIWUym9C-pKSy3WR2CfM0cTKpwipBqRMtu_AQcAc2EN_1X-hpuiqiVDSgM4aRbCo7ypDTwDJGz3dTBw6YABriyTobWk2svcFN4vVlmBbU9dnkNvIDsTi9pyM35gmpzSbDOGIOCmuFzIo_9KdzN5q2frNJkkJLrgX-LwyHgaRapOVPWcs=)
10. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0HbhFI3L6juMHw7mVZRZfVhgVUUiz71yIqNwFO0lp8JSObRFl9Owb1EFLQABcXklzXUfLDX-7Ia1PCwHr-w9K6ngrV_ZXAb87c7sAsLq9LnuKSppG1A==)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFA2eR7Zg-oLQhxZpu7NZryeYeqSFYt1S2w6AP8fKm4wrWszMTSc2PKg7LUlqRJPLeK3i3w2aHAkTu6eafjX4TowNpGckof4uK6kcCzLt0iCvJ2ALCghRn8Ds-ymPL2yvlTEzUSjxQamYuMd93DZTE5D5B2o1LEiFfuuNkdh8G-QA==)
12. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmgTPW3dCE-ef0XtbKKq7iZhIxf5vr6o51k981O81KFHX0jZjGi9SxpSwNU9VQwJcdeAwmX_WcmQUs3N9cGswkzql9df7J1DuJZGu6B4GM-qC_vmJlMQu2Q1tlJ8zPf6xzovS7fJVV)
13. [osti.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFr2RHUuFmKf7MewFxRsilRYhN_5d4ezYr0JVVUHOdFl0tS9d43mIoCJUiQKEenoJjkqlvc0BF_gVUPfN-hEZ0cuZ3iTUXWgZYMD7Fy7SqmrNqI-zBwMXMriE-mqhXTIDs=)
14. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKZDqJEHjKuCAbGLKn3936h_oKtz93IJsgOKAb_r6puKZLLR8oiEjmlCKtNFBYgytRM6f9KkbOBcSLZHnQ0P8xCmn_KMHKrc0zz4g6i0wkgVUdC1zVzpGiVq5KFfnHhq-lQCyhTuK_DOIG2Va53VKKCNmGYNinCW2gb0dyx2qW7lOJf4EyNSXHLX9qxUOjvvivBjc5Ggnn8SkrjlV02S8ESrV-sc3shfyuD-H7iQjMACOM4perRW7njT96wb52P88=)
15. [purdue.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjiWwms_uWQu_SR_lBpj37fpjEtAQEWRdmxInEiX3CMqFEZnIEMrtPi3XseW2srYTQL7ksA7aPej52pnCtEak8ipVun_dlc2qWHz3B4okznIDaXU_z-1A4JMBcN8NPrH8yx9XKDvLfMYsi)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg_PaRFaSUv7_UPDLpPLeFhFJfVD2ogsTPaIssOYfYqJYGykoR9MqSjs8wRZyYeQafX7wEfUikYzzUcd7z2uaLFbrdphOEdlXQz_8cicRpgTY_xh5QA0EdF3BEnttjFrreR1oQrnB5DcT0HXN57Mt8cZ4eKtw0v7AqiSBWu2haBUZn3JAjSGmTST3v0P15bTMq5FC1sYPk7ll17jsoiYCfZaQZWriArQXkDPk2ibafcRi_Ulnxh80ooBYz1rT5DfDbQw==)
17. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9geWaz0NZJg9oAEjuXJN-DHk8f4yj1ph6GkPQ2OBlKKXfYyQuBW-9wiStdEalVA-mWlowJYFGSGzRG2iVu_4mfJllnjA5D37xy3rMtxhNpDkhAQdxz0lHsg3re_WzsvSWdL3N99-r)
18. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgWZhHJ6EJQHmfJEaI8FL-geOaR--y9tBuzfgTv7g_ZnkKk3kITT2lZ9I1Bakeui1AnRMI-W0nNRKe2UGFy-ESzXhc331m_lRXzvDed_BLQqko8A9X2OM0pENZ6JKnhv9HzXQwf2fYwnHmWjRhlGyWq_yMonUoTvJFLxIqrfs7-iTgSKGLq1dg_RIW60oFBhrHdgwsOYKt0zqoGixYVksqWglRuYeMQTE5iSckVH27TyKyGHP8kdyRn8Gp)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRc543v5rP4-_EFhAwzIoXvzo9uMUCo5mB3TF4CbocPi_3EM4-W2DKhdtrC_FTvaTc4BQOl2eIScFj6equ6PYSQiKp88O6JpMvzdmFo4nqiFfqULSk2b2mxVdc3lrb4RdqVx0VKrWli6ZMG2oE2A7nfMrZO9c2OZB2L865ywSfmj48N70mIt2TAdxnpruxf9s175aaPFLa2TEiZXxgb9tf)
20. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvU16ZZjielUPccGPDtbr5psOSeUGfonkkIXaWLFSIUlz7zT8uNFhYLWYuWZm4I3nDWa4IGq0jkUmY2eqkbme-O6nLNF04swvvo1PtCveHYA7COSasCjVcyjXvoHPR81j2c6iK7heNKLlxTIBkYJPm0gmq4c_OuM-nU7kWfPsxcLjFam5lzEnm0KgOs7-0iZsWzONEvyjd8bdvbJ3t3syCskape213LlZ6_KREYVUzokjrigzxrLkwQUWkhq66SxY=)
21. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGk9hosLjihIOLp1HScPv3m6aUW7qBxiCQUpbDibQ6C6q34JpkhUCb1Ki6VUu3-AmEZ-HKTR9ZkHFkAlyXuIsI8csjknf3gcFb1MFhtTo0VmsXldYioEdxOEihtl6HUb6N0iMMXRRKRLCcR-WoAvihAPHipoxIVE-rOSw_2M0klNozl7fAADuiMt6enFkQ83VQWhTFct3g5elndy_stIg0xS4C5W3W2J28bSZ5ztMZgYPCe6JiIP5TQDtaqr-lvjwLhN2c5ZrsEJKytrT3-FqixOcZ1nrhB7DaB18BSc-OXY6R9)
22. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxLNYMFNnzmRkl6ugWh_iEg3rYDGSY6L7Tk84kONsv6SqEOf9uRuR0D8O2xFgWmEPLZ6M7FW0iEQhew-hVxverPjGeB8wEr_icLu2XFccgNwrgwcsahMrl102_7YVBGwacCdW5isYhFFm_Mi_XPKZiyuys0m3_IF144SNPLZDTudIc3CapszpxAuc5xkpeK3AUIWDpP2MPBvZEM25FerbAeggiVyzoIaaFhbbQ2sEOABfTwtxq37fFEgg_HsZnbOC7RQdUUhTVImxpf1sFNGLryur3TkRs0P5mf6MxnofLdEZOucspmMAksOvTsetkvY5Jml2g0sFSuCa7wJy1Iuvs6RY=)
23. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHk1hnKNRj7V4Uy4zUzvpUlqR6-ZP0Gf8Uh4xEZrGHNQCDQj_1OHbWmN7KT4UUXHRpV07Z16VlwWBeH13O08ayJrbn-Rjr9iGg8E9UNYC3lEijyzgQ-Xi8x4ucEOSQEiv1FMBpCH802)
24. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElf6Vu_fuDg2LflXuu65dyE1waLXPDY9pcGej-Y_WUwkHVcD1st8aIJowbDwwkLwaSwVVQXqEmVBPx9rvHGjMKCmqy31aAJiVlz9Uips-jarnVhEjT053-9lo3jJFMuxjwS0dE8ikDk6eO3fXTSzvoQANg-6wKlIcOHPuHbireWmGOO0_lBHQ3QW_dmbt2yYg8LnaMTEwQNEJArphwHgiO7ZNqKZO9HmPwRIo8eHIQYWRtmTBwWaF9jLJm9HBeAw==)
25. [iphy.ac.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzMyy0UnwJpjytRtPWAWDNZTWGceWWucey4Pm3E-aIXou4b1wFdhP8wIpTFP62sHzlVthgY9Om-0q8O_JwUYxM2_IbGH85up_CPuJcwbw1gI9ycjVInwukhgKzsBeBhXf6PLe4__oIBZSdiDx4DLCW0JJfC3AW)
26. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeoFv7q3x2p6H8yGhBrZ_hCYE7zuQzDVSpJOAS87MwN_QYYAsn95rpczI65qA1Pab8fL-U2SMR__Axu9e1SezHXWFRVX1dihmVNrmL2j89Pb-ZH77o1tzRBViIBMwPQXqRsRIXNeew)
27. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwPWX8z5S7jCgXu5-JQXppUa_LjlOI31oEDhrSLYZuYTlG0a6ALGIdhQFRacnycdFQZ--Z0MokCASefuqDeJyoA0byhTlRr3TfWQVOgqy4PO5_Ex6PTA==)
28. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeI1rYsEErd1OZ9j7D4HNJ0EZtIbBJ07-5wOKJNglVjJN4Narhc11y9hlN1EMRzmmmZYsqsAw0gDgwB8c6xeJZP9VPeHWqeScUd8d4Uaag6v_mK6ERtGZ9IQ==)


## Annotations
Annotation(end_index=2408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTnfkYydapMBRsVNwaIXeC6mw7GbmtzsmjNiR72zzee55W97P6wUTsV_gt2VPES0jSnNq8yqXLN61eTWCjSdGjhehfB8JtKF-jwr0pt0NhYYFoSE_MqA==', start_index=2396)
Annotation(end_index=2408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4Wy3Pj3pGf8z_Ep8Ik3_uQC-VGl6szZ24Y4oshiB2T4iSn1vcPKGosfx22GMTDJOHx0ICK1fq0TxCJMMg3m7amTy_9UNvAFRZphLhZdRGRGPD5fm_WdQl-MAb41xtfN6X8z9CPNSXPLVKJSSrssspG50aug==', start_index=2396)
Annotation(end_index=2668, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKBt1X--6iUOnBSoVDISmzVfPUEeSBc9nTLxBB_xkvH_koM6ZV-DzHwBJ5xzdGdReiLLjmROoVTcvZ_W2KGCLwwkGqIKK3uxzjl7OGWy6dnhtVgWgGP96eGQ==', start_index=2656)
Annotation(end_index=2668, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTnfkYydapMBRsVNwaIXeC6mw7GbmtzsmjNiR72zzee55W97P6wUTsV_gt2VPES0jSnNq8yqXLN61eTWCjSdGjhehfB8JtKF-jwr0pt0NhYYFoSE_MqA==', start_index=2656)
Annotation(end_index=3028, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKBt1X--6iUOnBSoVDISmzVfPUEeSBc9nTLxBB_xkvH_koM6ZV-DzHwBJ5xzdGdReiLLjmROoVTcvZ_W2KGCLwwkGqIKK3uxzjl7OGWy6dnhtVgWgGP96eGQ==', start_index=3016)
Annotation(end_index=3028, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTnfkYydapMBRsVNwaIXeC6mw7GbmtzsmjNiR72zzee55W97P6wUTsV_gt2VPES0jSnNq8yqXLN61eTWCjSdGjhehfB8JtKF-jwr0pt0NhYYFoSE_MqA==', start_index=3016)
Annotation(end_index=3311, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGHk7w7EWvRV_cxQ5XlMQDF0nQs5mxrO5Gn9K1SLO6kA4CIf1ZIk5KhlpbWVTgmeh5Jsf47kbS3a7PxMzhaH7vm8Gasge1a4sJXJSkXJUpmnHsvU789XuMTG_9xtvDBk6bTJqS-_YCBc35LfayHhcCD7-nTmGyMtsRSZDlajlW2_NF8_roHhob6-kQo4GGUq4az_PPZY66T3oLSArSaFU0pyn4cacZJi4JZp4s66-erjtT', start_index=3296)
Annotation(end_index=3311, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEssTJZx1kyNC2FCXbtuYt1x1sr3ZdN457yOIkOaQAyVvA0xDZvl3xybJbBVRRIpeZgDLhgLCdJtvtuubJxWiPcjOErwlCG7cLpPKOsxQ0sHapFfqbWljsnd-ykv9x5quaiadc9CWpO71_e', start_index=3296)
Annotation(end_index=3311, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZ755GrjYdbJHfpfQ9SPxh4f2iT4jJUIuH8l6b5izUEZpIKcpMFb9udbgg_EzVulv8yT-cztwsKcbbLs3Bw6XMe2miJmf4smslZHDVRHs2FFW0RRxTuoYnNaWcx24o57J1r5HlCwsM', start_index=3296)
Annotation(end_index=4280, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0HbhFI3L6juMHw7mVZRZfVhgVUUiz71yIqNwFO0lp8JSObRFl9Owb1EFLQABcXklzXUfLDX-7Ia1PCwHr-w9K6ngrV_ZXAb87c7sAsLq9LnuKSppG1A==', start_index=4261)
Annotation(end_index=4280, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF43YgCHTEZV23pS45mlWqpyUOe9rplXc8QbGR_0i1o8VQirO3KIWUym9C-pKSy3WR2CfM0cTKpwipBqRMtu_AQcAc2EN_1X-hpuiqiVDSgM4aRbCo7ypDTwDJGz3dTBw6YABriyTobWk2svcFN4vVlmBbU9dnkNvIDsTi9pyM35gmpzSbDOGIOCmuFzIo_9KdzN5q2frNJkkJLrgX-LwyHgaRapOVPWcs=', start_index=4261)
Annotation(end_index=4280, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLPLKj8I2IfVMPrs7IIPdq9zwPJyl2oJfJZIGDMYuv133Ucu-NNKpQSDPr4rNi5eVtCJW9y9cDTdXwtlO4hXGLyiz0zGjtW6U3bY7XD9Q-O4-bUXXF5PE=', start_index=4261)
Annotation(end_index=4280, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNr5s5wDHAuLPHR4jozhXortzkRm86IlcHyAA2NkG_UpWy49esrt4Vzw2v7Yj4tEtT915tPklzJGEeqV9fFIYlbJjgoMJSpNx2dkt5PvJoeyMRf1EXIiTjTQ==', start_index=4261)
Annotation(end_index=4643, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0HbhFI3L6juMHw7mVZRZfVhgVUUiz71yIqNwFO0lp8JSObRFl9Owb1EFLQABcXklzXUfLDX-7Ia1PCwHr-w9K6ngrV_ZXAb87c7sAsLq9LnuKSppG1A==', start_index=4627)
Annotation(end_index=4643, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLPLKj8I2IfVMPrs7IIPdq9zwPJyl2oJfJZIGDMYuv133Ucu-NNKpQSDPr4rNi5eVtCJW9y9cDTdXwtlO4hXGLyiz0zGjtW6U3bY7XD9Q-O4-bUXXF5PE=', start_index=4627)
Annotation(end_index=4643, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNr5s5wDHAuLPHR4jozhXortzkRm86IlcHyAA2NkG_UpWy49esrt4Vzw2v7Yj4tEtT915tPklzJGEeqV9fFIYlbJjgoMJSpNx2dkt5PvJoeyMRf1EXIiTjTQ==', start_index=4627)
Annotation(end_index=5019, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLPLKj8I2IfVMPrs7IIPdq9zwPJyl2oJfJZIGDMYuv133Ucu-NNKpQSDPr4rNi5eVtCJW9y9cDTdXwtlO4hXGLyiz0zGjtW6U3bY7XD9Q-O4-bUXXF5PE=', start_index=5010)
Annotation(end_index=5327, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLPLKj8I2IfVMPrs7IIPdq9zwPJyl2oJfJZIGDMYuv133Ucu-NNKpQSDPr4rNi5eVtCJW9y9cDTdXwtlO4hXGLyiz0zGjtW6U3bY7XD9Q-O4-bUXXF5PE=', start_index=5318)
Annotation(end_index=5505, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLPLKj8I2IfVMPrs7IIPdq9zwPJyl2oJfJZIGDMYuv133Ucu-NNKpQSDPr4rNi5eVtCJW9y9cDTdXwtlO4hXGLyiz0zGjtW6U3bY7XD9Q-O4-bUXXF5PE=', start_index=5493)
Annotation(end_index=5505, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNr5s5wDHAuLPHR4jozhXortzkRm86IlcHyAA2NkG_UpWy49esrt4Vzw2v7Yj4tEtT915tPklzJGEeqV9fFIYlbJjgoMJSpNx2dkt5PvJoeyMRf1EXIiTjTQ==', start_index=5493)
Annotation(end_index=5923, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLPLKj8I2IfVMPrs7IIPdq9zwPJyl2oJfJZIGDMYuv133Ucu-NNKpQSDPr4rNi5eVtCJW9y9cDTdXwtlO4hXGLyiz0zGjtW6U3bY7XD9Q-O4-bUXXF5PE=', start_index=5914)
Annotation(end_index=6145, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLPLKj8I2IfVMPrs7IIPdq9zwPJyl2oJfJZIGDMYuv133Ucu-NNKpQSDPr4rNi5eVtCJW9y9cDTdXwtlO4hXGLyiz0zGjtW6U3bY7XD9Q-O4-bUXXF5PE=', start_index=6133)
Annotation(end_index=6145, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNr5s5wDHAuLPHR4jozhXortzkRm86IlcHyAA2NkG_UpWy49esrt4Vzw2v7Yj4tEtT915tPklzJGEeqV9fFIYlbJjgoMJSpNx2dkt5PvJoeyMRf1EXIiTjTQ==', start_index=6133)
Annotation(end_index=6357, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLPLKj8I2IfVMPrs7IIPdq9zwPJyl2oJfJZIGDMYuv133Ucu-NNKpQSDPr4rNi5eVtCJW9y9cDTdXwtlO4hXGLyiz0zGjtW6U3bY7XD9Q-O4-bUXXF5PE=', start_index=6345)
Annotation(end_index=6357, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNr5s5wDHAuLPHR4jozhXortzkRm86IlcHyAA2NkG_UpWy49esrt4Vzw2v7Yj4tEtT915tPklzJGEeqV9fFIYlbJjgoMJSpNx2dkt5PvJoeyMRf1EXIiTjTQ==', start_index=6345)
Annotation(end_index=6624, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLPLKj8I2IfVMPrs7IIPdq9zwPJyl2oJfJZIGDMYuv133Ucu-NNKpQSDPr4rNi5eVtCJW9y9cDTdXwtlO4hXGLyiz0zGjtW6U3bY7XD9Q-O4-bUXXF5PE=', start_index=6615)
Annotation(end_index=6889, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLPLKj8I2IfVMPrs7IIPdq9zwPJyl2oJfJZIGDMYuv133Ucu-NNKpQSDPr4rNi5eVtCJW9y9cDTdXwtlO4hXGLyiz0zGjtW6U3bY7XD9Q-O4-bUXXF5PE=', start_index=6880)
Annotation(end_index=7131, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNr5s5wDHAuLPHR4jozhXortzkRm86IlcHyAA2NkG_UpWy49esrt4Vzw2v7Yj4tEtT915tPklzJGEeqV9fFIYlbJjgoMJSpNx2dkt5PvJoeyMRf1EXIiTjTQ==', start_index=7122)
Annotation(end_index=7362, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNr5s5wDHAuLPHR4jozhXortzkRm86IlcHyAA2NkG_UpWy49esrt4Vzw2v7Yj4tEtT915tPklzJGEeqV9fFIYlbJjgoMJSpNx2dkt5PvJoeyMRf1EXIiTjTQ==', start_index=7353)
Annotation(end_index=7569, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLPLKj8I2IfVMPrs7IIPdq9zwPJyl2oJfJZIGDMYuv133Ucu-NNKpQSDPr4rNi5eVtCJW9y9cDTdXwtlO4hXGLyiz0zGjtW6U3bY7XD9Q-O4-bUXXF5PE=', start_index=7557)
Annotation(end_index=7569, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNr5s5wDHAuLPHR4jozhXortzkRm86IlcHyAA2NkG_UpWy49esrt4Vzw2v7Yj4tEtT915tPklzJGEeqV9fFIYlbJjgoMJSpNx2dkt5PvJoeyMRf1EXIiTjTQ==', start_index=7557)
Annotation(end_index=7855, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLPLKj8I2IfVMPrs7IIPdq9zwPJyl2oJfJZIGDMYuv133Ucu-NNKpQSDPr4rNi5eVtCJW9y9cDTdXwtlO4hXGLyiz0zGjtW6U3bY7XD9Q-O4-bUXXF5PE=', start_index=7846)
Annotation(end_index=8444, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFA2eR7Zg-oLQhxZpu7NZryeYeqSFYt1S2w6AP8fKm4wrWszMTSc2PKg7LUlqRJPLeK3i3w2aHAkTu6eafjX4TowNpGckof4uK6kcCzLt0iCvJ2ALCghRn8Ds-ymPL2yvlTEzUSjxQamYuMd93DZTE5D5B2o1LEiFfuuNkdh8G-QA==', start_index=8414)
Annotation(end_index=8444, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg_PaRFaSUv7_UPDLpPLeFhFJfVD2ogsTPaIssOYfYqJYGykoR9MqSjs8wRZyYeQafX7wEfUikYzzUcd7z2uaLFbrdphOEdlXQz_8cicRpgTY_xh5QA0EdF3BEnttjFrreR1oQrnB5DcT0HXN57Mt8cZ4eKtw0v7AqiSBWu2haBUZn3JAjSGmTST3v0P15bTMq5FC1sYPk7ll17jsoiYCfZaQZWriArQXkDPk2ibafcRi_Ulnxh80ooBYz1rT5DfDbQw==', start_index=8414)
Annotation(end_index=8444, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFr2RHUuFmKf7MewFxRsilRYhN_5d4ezYr0JVVUHOdFl0tS9d43mIoCJUiQKEenoJjkqlvc0BF_gVUPfN-hEZ0cuZ3iTUXWgZYMD7Fy7SqmrNqI-zBwMXMriE-mqhXTIDs=', start_index=8414)
Annotation(end_index=8444, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjiWwms_uWQu_SR_lBpj37fpjEtAQEWRdmxInEiX3CMqFEZnIEMrtPi3XseW2srYTQL7ksA7aPej52pnCtEak8ipVun_dlc2qWHz3B4okznIDaXU_z-1A4JMBcN8NPrH8yx9XKDvLfMYsi', start_index=8414)
Annotation(end_index=8444, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKZDqJEHjKuCAbGLKn3936h_oKtz93IJsgOKAb_r6puKZLLR8oiEjmlCKtNFBYgytRM6f9KkbOBcSLZHnQ0P8xCmn_KMHKrc0zz4g6i0wkgVUdC1zVzpGiVq5KFfnHhq-lQCyhTuK_DOIG2Va53VKKCNmGYNinCW2gb0dyx2qW7lOJf4EyNSXHLX9qxUOjvvivBjc5Ggnn8SkrjlV02S8ESrV-sc3shfyuD-H7iQjMACOM4perRW7njT96wb52P88=', start_index=8414)
Annotation(end_index=8444, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmgTPW3dCE-ef0XtbKKq7iZhIxf5vr6o51k981O81KFHX0jZjGi9SxpSwNU9VQwJcdeAwmX_WcmQUs3N9cGswkzql9df7J1DuJZGu6B4GM-qC_vmJlMQu2Q1tlJ8zPf6xzovS7fJVV', start_index=8414)
Annotation(end_index=8978, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFA2eR7Zg-oLQhxZpu7NZryeYeqSFYt1S2w6AP8fKm4wrWszMTSc2PKg7LUlqRJPLeK3i3w2aHAkTu6eafjX4TowNpGckof4uK6kcCzLt0iCvJ2ALCghRn8Ds-ymPL2yvlTEzUSjxQamYuMd93DZTE5D5B2o1LEiFfuuNkdh8G-QA==', start_index=8964)
Annotation(end_index=8978, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg_PaRFaSUv7_UPDLpPLeFhFJfVD2ogsTPaIssOYfYqJYGykoR9MqSjs8wRZyYeQafX7wEfUikYzzUcd7z2uaLFbrdphOEdlXQz_8cicRpgTY_xh5QA0EdF3BEnttjFrreR1oQrnB5DcT0HXN57Mt8cZ4eKtw0v7AqiSBWu2haBUZn3JAjSGmTST3v0P15bTMq5FC1sYPk7ll17jsoiYCfZaQZWriArQXkDPk2ibafcRi_Ulnxh80ooBYz1rT5DfDbQw==', start_index=8964)
Annotation(end_index=9305, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFA2eR7Zg-oLQhxZpu7NZryeYeqSFYt1S2w6AP8fKm4wrWszMTSc2PKg7LUlqRJPLeK3i3w2aHAkTu6eafjX4TowNpGckof4uK6kcCzLt0iCvJ2ALCghRn8Ds-ymPL2yvlTEzUSjxQamYuMd93DZTE5D5B2o1LEiFfuuNkdh8G-QA==', start_index=9291)
Annotation(end_index=9305, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFr2RHUuFmKf7MewFxRsilRYhN_5d4ezYr0JVVUHOdFl0tS9d43mIoCJUiQKEenoJjkqlvc0BF_gVUPfN-hEZ0cuZ3iTUXWgZYMD7Fy7SqmrNqI-zBwMXMriE-mqhXTIDs=', start_index=9291)
Annotation(end_index=9679, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFr2RHUuFmKf7MewFxRsilRYhN_5d4ezYr0JVVUHOdFl0tS9d43mIoCJUiQKEenoJjkqlvc0BF_gVUPfN-hEZ0cuZ3iTUXWgZYMD7Fy7SqmrNqI-zBwMXMriE-mqhXTIDs=', start_index=9665)
Annotation(end_index=9679, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjiWwms_uWQu_SR_lBpj37fpjEtAQEWRdmxInEiX3CMqFEZnIEMrtPi3XseW2srYTQL7ksA7aPej52pnCtEak8ipVun_dlc2qWHz3B4okznIDaXU_z-1A4JMBcN8NPrH8yx9XKDvLfMYsi', start_index=9665)
Annotation(end_index=10274, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFA2eR7Zg-oLQhxZpu7NZryeYeqSFYt1S2w6AP8fKm4wrWszMTSc2PKg7LUlqRJPLeK3i3w2aHAkTu6eafjX4TowNpGckof4uK6kcCzLt0iCvJ2ALCghRn8Ds-ymPL2yvlTEzUSjxQamYuMd93DZTE5D5B2o1LEiFfuuNkdh8G-QA==', start_index=10256)
Annotation(end_index=10274, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKZDqJEHjKuCAbGLKn3936h_oKtz93IJsgOKAb_r6puKZLLR8oiEjmlCKtNFBYgytRM6f9KkbOBcSLZHnQ0P8xCmn_KMHKrc0zz4g6i0wkgVUdC1zVzpGiVq5KFfnHhq-lQCyhTuK_DOIG2Va53VKKCNmGYNinCW2gb0dyx2qW7lOJf4EyNSXHLX9qxUOjvvivBjc5Ggnn8SkrjlV02S8ESrV-sc3shfyuD-H7iQjMACOM4perRW7njT96wb52P88=', start_index=10256)
Annotation(end_index=10274, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmgTPW3dCE-ef0XtbKKq7iZhIxf5vr6o51k981O81KFHX0jZjGi9SxpSwNU9VQwJcdeAwmX_WcmQUs3N9cGswkzql9df7J1DuJZGu6B4GM-qC_vmJlMQu2Q1tlJ8zPf6xzovS7fJVV', start_index=10256)
Annotation(end_index=11045, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9geWaz0NZJg9oAEjuXJN-DHk8f4yj1ph6GkPQ2OBlKKXfYyQuBW-9wiStdEalVA-mWlowJYFGSGzRG2iVu_4mfJllnjA5D37xy3rMtxhNpDkhAQdxz0lHsg3re_WzsvSWdL3N99-r', start_index=11035)
Annotation(end_index=11325, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvU16ZZjielUPccGPDtbr5psOSeUGfonkkIXaWLFSIUlz7zT8uNFhYLWYuWZm4I3nDWa4IGq0jkUmY2eqkbme-O6nLNF04swvvo1PtCveHYA7COSasCjVcyjXvoHPR81j2c6iK7heNKLlxTIBkYJPm0gmq4c_OuM-nU7kWfPsxcLjFam5lzEnm0KgOs7-0iZsWzONEvyjd8bdvbJ3t3syCskape213LlZ6_KREYVUzokjrigzxrLkwQUWkhq66SxY=', start_index=11304)
Annotation(end_index=11325, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4Wy3Pj3pGf8z_Ep8Ik3_uQC-VGl6szZ24Y4oshiB2T4iSn1vcPKGosfx22GMTDJOHx0ICK1fq0TxCJMMg3m7amTy_9UNvAFRZphLhZdRGRGPD5fm_WdQl-MAb41xtfN6X8z9CPNSXPLVKJSSrssspG50aug==', start_index=11304)
Annotation(end_index=11325, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRc543v5rP4-_EFhAwzIoXvzo9uMUCo5mB3TF4CbocPi_3EM4-W2DKhdtrC_FTvaTc4BQOl2eIScFj6equ6PYSQiKp88O6JpMvzdmFo4nqiFfqULSk2b2mxVdc3lrb4RdqVx0VKrWli6ZMG2oE2A7nfMrZO9c2OZB2L865ywSfmj48N70mIt2TAdxnpruxf9s175aaPFLa2TEiZXxgb9tf', start_index=11304)
Annotation(end_index=11325, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgWZhHJ6EJQHmfJEaI8FL-geOaR--y9tBuzfgTv7g_ZnkKk3kITT2lZ9I1Bakeui1AnRMI-W0nNRKe2UGFy-ESzXhc331m_lRXzvDed_BLQqko8A9X2OM0pENZ6JKnhv9HzXQwf2fYwnHmWjRhlGyWq_yMonUoTvJFLxIqrfs7-iTgSKGLq1dg_RIW60oFBhrHdgwsOYKt0zqoGixYVksqWglRuYeMQTE5iSckVH27TyKyGHP8kdyRn8Gp', start_index=11304)
Annotation(end_index=11667, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvU16ZZjielUPccGPDtbr5psOSeUGfonkkIXaWLFSIUlz7zT8uNFhYLWYuWZm4I3nDWa4IGq0jkUmY2eqkbme-O6nLNF04swvvo1PtCveHYA7COSasCjVcyjXvoHPR81j2c6iK7heNKLlxTIBkYJPm0gmq4c_OuM-nU7kWfPsxcLjFam5lzEnm0KgOs7-0iZsWzONEvyjd8bdvbJ3t3syCskape213LlZ6_KREYVUzokjrigzxrLkwQUWkhq66SxY=', start_index=11653)
Annotation(end_index=11667, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgWZhHJ6EJQHmfJEaI8FL-geOaR--y9tBuzfgTv7g_ZnkKk3kITT2lZ9I1Bakeui1AnRMI-W0nNRKe2UGFy-ESzXhc331m_lRXzvDed_BLQqko8A9X2OM0pENZ6JKnhv9HzXQwf2fYwnHmWjRhlGyWq_yMonUoTvJFLxIqrfs7-iTgSKGLq1dg_RIW60oFBhrHdgwsOYKt0zqoGixYVksqWglRuYeMQTE5iSckVH27TyKyGHP8kdyRn8Gp', start_index=11653)
Annotation(end_index=12157, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvU16ZZjielUPccGPDtbr5psOSeUGfonkkIXaWLFSIUlz7zT8uNFhYLWYuWZm4I3nDWa4IGq0jkUmY2eqkbme-O6nLNF04swvvo1PtCveHYA7COSasCjVcyjXvoHPR81j2c6iK7heNKLlxTIBkYJPm0gmq4c_OuM-nU7kWfPsxcLjFam5lzEnm0KgOs7-0iZsWzONEvyjd8bdvbJ3t3syCskape213LlZ6_KREYVUzokjrigzxrLkwQUWkhq66SxY=', start_index=12140)
Annotation(end_index=12157, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGk9hosLjihIOLp1HScPv3m6aUW7qBxiCQUpbDibQ6C6q34JpkhUCb1Ki6VUu3-AmEZ-HKTR9ZkHFkAlyXuIsI8csjknf3gcFb1MFhtTo0VmsXldYioEdxOEihtl6HUb6N0iMMXRRKRLCcR-WoAvihAPHipoxIVE-rOSw_2M0klNozl7fAADuiMt6enFkQ83VQWhTFct3g5elndy_stIg0xS4C5W3W2J28bSZ5ztMZgYPCe6JiIP5TQDtaqr-lvjwLhN2c5ZrsEJKytrT3-FqixOcZ1nrhB7DaB18BSc-OXY6R9', start_index=12140)
Annotation(end_index=12157, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4Wy3Pj3pGf8z_Ep8Ik3_uQC-VGl6szZ24Y4oshiB2T4iSn1vcPKGosfx22GMTDJOHx0ICK1fq0TxCJMMg3m7amTy_9UNvAFRZphLhZdRGRGPD5fm_WdQl-MAb41xtfN6X8z9CPNSXPLVKJSSrssspG50aug==', start_index=12140)
Annotation(end_index=12637, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRc543v5rP4-_EFhAwzIoXvzo9uMUCo5mB3TF4CbocPi_3EM4-W2DKhdtrC_FTvaTc4BQOl2eIScFj6equ6PYSQiKp88O6JpMvzdmFo4nqiFfqULSk2b2mxVdc3lrb4RdqVx0VKrWli6ZMG2oE2A7nfMrZO9c2OZB2L865ywSfmj48N70mIt2TAdxnpruxf9s175aaPFLa2TEiZXxgb9tf', start_index=12627)
Annotation(end_index=13096, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEssTJZx1kyNC2FCXbtuYt1x1sr3ZdN457yOIkOaQAyVvA0xDZvl3xybJbBVRRIpeZgDLhgLCdJtvtuubJxWiPcjOErwlCG7cLpPKOsxQ0sHapFfqbWljsnd-ykv9x5quaiadc9CWpO71_e', start_index=13083)
Annotation(end_index=13096, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxLNYMFNnzmRkl6ugWh_iEg3rYDGSY6L7Tk84kONsv6SqEOf9uRuR0D8O2xFgWmEPLZ6M7FW0iEQhew-hVxverPjGeB8wEr_icLu2XFccgNwrgwcsahMrl102_7YVBGwacCdW5isYhFFm_Mi_XPKZiyuys0m3_IF144SNPLZDTudIc3CapszpxAuc5xkpeK3AUIWDpP2MPBvZEM25FerbAeggiVyzoIaaFhbbQ2sEOABfTwtxq37fFEgg_HsZnbOC7RQdUUhTVImxpf1sFNGLryur3TkRs0P5mf6MxnofLdEZOucspmMAksOvTsetkvY5Jml2g0sFSuCa7wJy1Iuvs6RY=', start_index=13083)
Annotation(end_index=13428, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGHk7w7EWvRV_cxQ5XlMQDF0nQs5mxrO5Gn9K1SLO6kA4CIf1ZIk5KhlpbWVTgmeh5Jsf47kbS3a7PxMzhaH7vm8Gasge1a4sJXJSkXJUpmnHsvU789XuMTG_9xtvDBk6bTJqS-_YCBc35LfayHhcCD7-nTmGyMtsRSZDlajlW2_NF8_roHhob6-kQo4GGUq4az_PPZY66T3oLSArSaFU0pyn4cacZJi4JZp4s66-erjtT', start_index=13419)
Annotation(end_index=14078, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZ755GrjYdbJHfpfQ9SPxh4f2iT4jJUIuH8l6b5izUEZpIKcpMFb9udbgg_EzVulv8yT-cztwsKcbbLs3Bw6XMe2miJmf4smslZHDVRHs2FFW0RRxTuoYnNaWcx24o57J1r5HlCwsM', start_index=14069)
Annotation(end_index=14589, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHk1hnKNRj7V4Uy4zUzvpUlqR6-ZP0Gf8Uh4xEZrGHNQCDQj_1OHbWmN7KT4UUXHRpV07Z16VlwWBeH13O08ayJrbn-Rjr9iGg8E9UNYC3lEijyzgQ-Xi8x4ucEOSQEiv1FMBpCH802', start_index=14579)
Annotation(end_index=14957, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElf6Vu_fuDg2LflXuu65dyE1waLXPDY9pcGej-Y_WUwkHVcD1st8aIJowbDwwkLwaSwVVQXqEmVBPx9rvHGjMKCmqy31aAJiVlz9Uips-jarnVhEjT053-9lo3jJFMuxjwS0dE8ikDk6eO3fXTSzvoQANg-6wKlIcOHPuHbireWmGOO0_lBHQ3QW_dmbt2yYg8LnaMTEwQNEJArphwHgiO7ZNqKZO9HmPwRIo8eHIQYWRtmTBwWaF9jLJm9HBeAw==', start_index=14943)
Annotation(end_index=14957, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzMyy0UnwJpjytRtPWAWDNZTWGceWWucey4Pm3E-aIXou4b1wFdhP8wIpTFP62sHzlVthgY9Om-0q8O_JwUYxM2_IbGH85up_CPuJcwbw1gI9ycjVInwukhgKzsBeBhXf6PLe4__oIBZSdiDx4DLCW0JJfC3AW', start_index=14943)
Annotation(end_index=16515, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0HbhFI3L6juMHw7mVZRZfVhgVUUiz71yIqNwFO0lp8JSObRFl9Owb1EFLQABcXklzXUfLDX-7Ia1PCwHr-w9K6ngrV_ZXAb87c7sAsLq9LnuKSppG1A==', start_index=16496)
Annotation(end_index=16515, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF43YgCHTEZV23pS45mlWqpyUOe9rplXc8QbGR_0i1o8VQirO3KIWUym9C-pKSy3WR2CfM0cTKpwipBqRMtu_AQcAc2EN_1X-hpuiqiVDSgM4aRbCo7ypDTwDJGz3dTBw6YABriyTobWk2svcFN4vVlmBbU9dnkNvIDsTi9pyM35gmpzSbDOGIOCmuFzIo_9KdzN5q2frNJkkJLrgX-LwyHgaRapOVPWcs=', start_index=16496)
Annotation(end_index=16515, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLPLKj8I2IfVMPrs7IIPdq9zwPJyl2oJfJZIGDMYuv133Ucu-NNKpQSDPr4rNi5eVtCJW9y9cDTdXwtlO4hXGLyiz0zGjtW6U3bY7XD9Q-O4-bUXXF5PE=', start_index=16496)
Annotation(end_index=16515, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNr5s5wDHAuLPHR4jozhXortzkRm86IlcHyAA2NkG_UpWy49esrt4Vzw2v7Yj4tEtT915tPklzJGEeqV9fFIYlbJjgoMJSpNx2dkt5PvJoeyMRf1EXIiTjTQ==', start_index=16496)
Annotation(end_index=17097, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0HbhFI3L6juMHw7mVZRZfVhgVUUiz71yIqNwFO0lp8JSObRFl9Owb1EFLQABcXklzXUfLDX-7Ia1PCwHr-w9K6ngrV_ZXAb87c7sAsLq9LnuKSppG1A==', start_index=17084)
Annotation(end_index=17097, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNr5s5wDHAuLPHR4jozhXortzkRm86IlcHyAA2NkG_UpWy49esrt4Vzw2v7Yj4tEtT915tPklzJGEeqV9fFIYlbJjgoMJSpNx2dkt5PvJoeyMRf1EXIiTjTQ==', start_index=17084)
Annotation(end_index=17802, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNr5s5wDHAuLPHR4jozhXortzkRm86IlcHyAA2NkG_UpWy49esrt4Vzw2v7Yj4tEtT915tPklzJGEeqV9fFIYlbJjgoMJSpNx2dkt5PvJoeyMRf1EXIiTjTQ==', start_index=17793)
Annotation(end_index=18636, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLPLKj8I2IfVMPrs7IIPdq9zwPJyl2oJfJZIGDMYuv133Ucu-NNKpQSDPr4rNi5eVtCJW9y9cDTdXwtlO4hXGLyiz0zGjtW6U3bY7XD9Q-O4-bUXXF5PE=', start_index=18627)
Annotation(end_index=18870, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFA2eR7Zg-oLQhxZpu7NZryeYeqSFYt1S2w6AP8fKm4wrWszMTSc2PKg7LUlqRJPLeK3i3w2aHAkTu6eafjX4TowNpGckof4uK6kcCzLt0iCvJ2ALCghRn8Ds-ymPL2yvlTEzUSjxQamYuMd93DZTE5D5B2o1LEiFfuuNkdh8G-QA==', start_index=18840)
Annotation(end_index=18870, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg_PaRFaSUv7_UPDLpPLeFhFJfVD2ogsTPaIssOYfYqJYGykoR9MqSjs8wRZyYeQafX7wEfUikYzzUcd7z2uaLFbrdphOEdlXQz_8cicRpgTY_xh5QA0EdF3BEnttjFrreR1oQrnB5DcT0HXN57Mt8cZ4eKtw0v7AqiSBWu2haBUZn3JAjSGmTST3v0P15bTMq5FC1sYPk7ll17jsoiYCfZaQZWriArQXkDPk2ibafcRi_Ulnxh80ooBYz1rT5DfDbQw==', start_index=18840)
Annotation(end_index=18870, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFr2RHUuFmKf7MewFxRsilRYhN_5d4ezYr0JVVUHOdFl0tS9d43mIoCJUiQKEenoJjkqlvc0BF_gVUPfN-hEZ0cuZ3iTUXWgZYMD7Fy7SqmrNqI-zBwMXMriE-mqhXTIDs=', start_index=18840)
Annotation(end_index=18870, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjiWwms_uWQu_SR_lBpj37fpjEtAQEWRdmxInEiX3CMqFEZnIEMrtPi3XseW2srYTQL7ksA7aPej52pnCtEak8ipVun_dlc2qWHz3B4okznIDaXU_z-1A4JMBcN8NPrH8yx9XKDvLfMYsi', start_index=18840)
Annotation(end_index=18870, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKZDqJEHjKuCAbGLKn3936h_oKtz93IJsgOKAb_r6puKZLLR8oiEjmlCKtNFBYgytRM6f9KkbOBcSLZHnQ0P8xCmn_KMHKrc0zz4g6i0wkgVUdC1zVzpGiVq5KFfnHhq-lQCyhTuK_DOIG2Va53VKKCNmGYNinCW2gb0dyx2qW7lOJf4EyNSXHLX9qxUOjvvivBjc5Ggnn8SkrjlV02S8ESrV-sc3shfyuD-H7iQjMACOM4perRW7njT96wb52P88=', start_index=18840)
Annotation(end_index=18870, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmgTPW3dCE-ef0XtbKKq7iZhIxf5vr6o51k981O81KFHX0jZjGi9SxpSwNU9VQwJcdeAwmX_WcmQUs3N9cGswkzql9df7J1DuJZGu6B4GM-qC_vmJlMQu2Q1tlJ8zPf6xzovS7fJVV', start_index=18840)
Annotation(end_index=19656, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFA2eR7Zg-oLQhxZpu7NZryeYeqSFYt1S2w6AP8fKm4wrWszMTSc2PKg7LUlqRJPLeK3i3w2aHAkTu6eafjX4TowNpGckof4uK6kcCzLt0iCvJ2ALCghRn8Ds-ymPL2yvlTEzUSjxQamYuMd93DZTE5D5B2o1LEiFfuuNkdh8G-QA==', start_index=19646)
Annotation(end_index=20137, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvU16ZZjielUPccGPDtbr5psOSeUGfonkkIXaWLFSIUlz7zT8uNFhYLWYuWZm4I3nDWa4IGq0jkUmY2eqkbme-O6nLNF04swvvo1PtCveHYA7COSasCjVcyjXvoHPR81j2c6iK7heNKLlxTIBkYJPm0gmq4c_OuM-nU7kWfPsxcLjFam5lzEnm0KgOs7-0iZsWzONEvyjd8bdvbJ3t3syCskape213LlZ6_KREYVUzokjrigzxrLkwQUWkhq66SxY=', start_index=20123)
Annotation(end_index=20137, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgWZhHJ6EJQHmfJEaI8FL-geOaR--y9tBuzfgTv7g_ZnkKk3kITT2lZ9I1Bakeui1AnRMI-W0nNRKe2UGFy-ESzXhc331m_lRXzvDed_BLQqko8A9X2OM0pENZ6JKnhv9HzXQwf2fYwnHmWjRhlGyWq_yMonUoTvJFLxIqrfs7-iTgSKGLq1dg_RIW60oFBhrHdgwsOYKt0zqoGixYVksqWglRuYeMQTE5iSckVH27TyKyGHP8kdyRn8Gp', start_index=20123)
Annotation(end_index=20799, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRc543v5rP4-_EFhAwzIoXvzo9uMUCo5mB3TF4CbocPi_3EM4-W2DKhdtrC_FTvaTc4BQOl2eIScFj6equ6PYSQiKp88O6JpMvzdmFo4nqiFfqULSk2b2mxVdc3lrb4RdqVx0VKrWli6ZMG2oE2A7nfMrZO9c2OZB2L865ywSfmj48N70mIt2TAdxnpruxf9s175aaPFLa2TEiZXxgb9tf', start_index=20789)
Annotation(end_index=21041, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHk1hnKNRj7V4Uy4zUzvpUlqR6-ZP0Gf8Uh4xEZrGHNQCDQj_1OHbWmN7KT4UUXHRpV07Z16VlwWBeH13O08ayJrbn-Rjr9iGg8E9UNYC3lEijyzgQ-Xi8x4ucEOSQEiv1FMBpCH802', start_index=21031)
Annotation(end_index=21125, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZ755GrjYdbJHfpfQ9SPxh4f2iT4jJUIuH8l6b5izUEZpIKcpMFb9udbgg_EzVulv8yT-cztwsKcbbLs3Bw6XMe2miJmf4smslZHDVRHs2FFW0RRxTuoYnNaWcx24o57J1r5HlCwsM', start_index=21116)
Annotation(end_index=21232, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNr5s5wDHAuLPHR4jozhXortzkRm86IlcHyAA2NkG_UpWy49esrt4Vzw2v7Yj4tEtT915tPklzJGEeqV9fFIYlbJjgoMJSpNx2dkt5PvJoeyMRf1EXIiTjTQ==', start_index=21223)
Annotation(end_index=21505, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFA2eR7Zg-oLQhxZpu7NZryeYeqSFYt1S2w6AP8fKm4wrWszMTSc2PKg7LUlqRJPLeK3i3w2aHAkTu6eafjX4TowNpGckof4uK6kcCzLt0iCvJ2ALCghRn8Ds-ymPL2yvlTEzUSjxQamYuMd93DZTE5D5B2o1LEiFfuuNkdh8G-QA==', start_index=21495)
Annotation(end_index=21629, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEssTJZx1kyNC2FCXbtuYt1x1sr3ZdN457yOIkOaQAyVvA0xDZvl3xybJbBVRRIpeZgDLhgLCdJtvtuubJxWiPcjOErwlCG7cLpPKOsxQ0sHapFfqbWljsnd-ykv9x5quaiadc9CWpO71_e', start_index=21620)
Annotation(end_index=21745, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGHk7w7EWvRV_cxQ5XlMQDF0nQs5mxrO5Gn9K1SLO6kA4CIf1ZIk5KhlpbWVTgmeh5Jsf47kbS3a7PxMzhaH7vm8Gasge1a4sJXJSkXJUpmnHsvU789XuMTG_9xtvDBk6bTJqS-_YCBc35LfayHhcCD7-nTmGyMtsRSZDlajlW2_NF8_roHhob6-kQo4GGUq4az_PPZY66T3oLSArSaFU0pyn4cacZJi4JZp4s66-erjtT', start_index=21736)
Annotation(end_index=21986, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLPLKj8I2IfVMPrs7IIPdq9zwPJyl2oJfJZIGDMYuv133Ucu-NNKpQSDPr4rNi5eVtCJW9y9cDTdXwtlO4hXGLyiz0zGjtW6U3bY7XD9Q-O4-bUXXF5PE=', start_index=21977)
Annotation(end_index=22117, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHk1hnKNRj7V4Uy4zUzvpUlqR6-ZP0Gf8Uh4xEZrGHNQCDQj_1OHbWmN7KT4UUXHRpV07Z16VlwWBeH13O08ayJrbn-Rjr9iGg8E9UNYC3lEijyzgQ-Xi8x4ucEOSQEiv1FMBpCH802', start_index=22107)
Annotation(end_index=22266, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNr5s5wDHAuLPHR4jozhXortzkRm86IlcHyAA2NkG_UpWy49esrt4Vzw2v7Yj4tEtT915tPklzJGEeqV9fFIYlbJjgoMJSpNx2dkt5PvJoeyMRf1EXIiTjTQ==', start_index=22257)
Annotation(end_index=23062, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZ755GrjYdbJHfpfQ9SPxh4f2iT4jJUIuH8l6b5izUEZpIKcpMFb9udbgg_EzVulv8yT-cztwsKcbbLs3Bw6XMe2miJmf4smslZHDVRHs2FFW0RRxTuoYnNaWcx24o57J1r5HlCwsM', start_index=23053)
Annotation(end_index=23093, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFA2eR7Zg-oLQhxZpu7NZryeYeqSFYt1S2w6AP8fKm4wrWszMTSc2PKg7LUlqRJPLeK3i3w2aHAkTu6eafjX4TowNpGckof4uK6kcCzLt0iCvJ2ALCghRn8Ds-ymPL2yvlTEzUSjxQamYuMd93DZTE5D5B2o1LEiFfuuNkdh8G-QA==', start_index=23083)
Annotation(end_index=23142, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmgTPW3dCE-ef0XtbKKq7iZhIxf5vr6o51k981O81KFHX0jZjGi9SxpSwNU9VQwJcdeAwmX_WcmQUs3N9cGswkzql9df7J1DuJZGu6B4GM-qC_vmJlMQu2Q1tlJ8zPf6xzovS7fJVV', start_index=23132)
Annotation(end_index=23172, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEssTJZx1kyNC2FCXbtuYt1x1sr3ZdN457yOIkOaQAyVvA0xDZvl3xybJbBVRRIpeZgDLhgLCdJtvtuubJxWiPcjOErwlCG7cLpPKOsxQ0sHapFfqbWljsnd-ykv9x5quaiadc9CWpO71_e', start_index=23163)
Annotation(end_index=23206, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTnfkYydapMBRsVNwaIXeC6mw7GbmtzsmjNiR72zzee55W97P6wUTsV_gt2VPES0jSnNq8yqXLN61eTWCjSdGjhehfB8JtKF-jwr0pt0NhYYFoSE_MqA==', start_index=23197)
Annotation(end_index=23234, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeoFv7q3x2p6H8yGhBrZ_hCYE7zuQzDVSpJOAS87MwN_QYYAsn95rpczI65qA1Pab8fL-U2SMR__Axu9e1SezHXWFRVX1dihmVNrmL2j89Pb-ZH77o1tzRBViIBMwPQXqRsRIXNeew', start_index=23224)
Annotation(end_index=23265, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGk9hosLjihIOLp1HScPv3m6aUW7qBxiCQUpbDibQ6C6q34JpkhUCb1Ki6VUu3-AmEZ-HKTR9ZkHFkAlyXuIsI8csjknf3gcFb1MFhtTo0VmsXldYioEdxOEihtl6HUb6N0iMMXRRKRLCcR-WoAvihAPHipoxIVE-rOSw_2M0klNozl7fAADuiMt6enFkQ83VQWhTFct3g5elndy_stIg0xS4C5W3W2J28bSZ5ztMZgYPCe6JiIP5TQDtaqr-lvjwLhN2c5ZrsEJKytrT3-FqixOcZ1nrhB7DaB18BSc-OXY6R9', start_index=23255)
Annotation(end_index=23333, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4Wy3Pj3pGf8z_Ep8Ik3_uQC-VGl6szZ24Y4oshiB2T4iSn1vcPKGosfx22GMTDJOHx0ICK1fq0TxCJMMg3m7amTy_9UNvAFRZphLhZdRGRGPD5fm_WdQl-MAb41xtfN6X8z9CPNSXPLVKJSSrssspG50aug==', start_index=23324)
Annotation(end_index=23365, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwPWX8z5S7jCgXu5-JQXppUa_LjlOI31oEDhrSLYZuYTlG0a6ALGIdhQFRacnycdFQZ--Z0MokCASefuqDeJyoA0byhTlRr3TfWQVOgqy4PO5_Ex6PTA==', start_index=23355)
Annotation(end_index=23392, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGHk7w7EWvRV_cxQ5XlMQDF0nQs5mxrO5Gn9K1SLO6kA4CIf1ZIk5KhlpbWVTgmeh5Jsf47kbS3a7PxMzhaH7vm8Gasge1a4sJXJSkXJUpmnHsvU789XuMTG_9xtvDBk6bTJqS-_YCBc35LfayHhcCD7-nTmGyMtsRSZDlajlW2_NF8_roHhob6-kQo4GGUq4az_PPZY66T3oLSArSaFU0pyn4cacZJi4JZp4s66-erjtT', start_index=23383)
Annotation(end_index=23464, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNr5s5wDHAuLPHR4jozhXortzkRm86IlcHyAA2NkG_UpWy49esrt4Vzw2v7Yj4tEtT915tPklzJGEeqV9fFIYlbJjgoMJSpNx2dkt5PvJoeyMRf1EXIiTjTQ==', start_index=23455)
Annotation(end_index=23493, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNr5s5wDHAuLPHR4jozhXortzkRm86IlcHyAA2NkG_UpWy49esrt4Vzw2v7Yj4tEtT915tPklzJGEeqV9fFIYlbJjgoMJSpNx2dkt5PvJoeyMRf1EXIiTjTQ==', start_index=23484)
Annotation(end_index=23570, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFr2RHUuFmKf7MewFxRsilRYhN_5d4ezYr0JVVUHOdFl0tS9d43mIoCJUiQKEenoJjkqlvc0BF_gVUPfN-hEZ0cuZ3iTUXWgZYMD7Fy7SqmrNqI-zBwMXMriE-mqhXTIDs=', start_index=23560)
Annotation(end_index=23598, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFA2eR7Zg-oLQhxZpu7NZryeYeqSFYt1S2w6AP8fKm4wrWszMTSc2PKg7LUlqRJPLeK3i3w2aHAkTu6eafjX4TowNpGckof4uK6kcCzLt0iCvJ2ALCghRn8Ds-ymPL2yvlTEzUSjxQamYuMd93DZTE5D5B2o1LEiFfuuNkdh8G-QA==', start_index=23588)
Annotation(end_index=23664, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKZDqJEHjKuCAbGLKn3936h_oKtz93IJsgOKAb_r6puKZLLR8oiEjmlCKtNFBYgytRM6f9KkbOBcSLZHnQ0P8xCmn_KMHKrc0zz4g6i0wkgVUdC1zVzpGiVq5KFfnHhq-lQCyhTuK_DOIG2Va53VKKCNmGYNinCW2gb0dyx2qW7lOJf4EyNSXHLX9qxUOjvvivBjc5Ggnn8SkrjlV02S8ESrV-sc3shfyuD-H7iQjMACOM4perRW7njT96wb52P88=', start_index=23654)
Annotation(end_index=23706, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZ755GrjYdbJHfpfQ9SPxh4f2iT4jJUIuH8l6b5izUEZpIKcpMFb9udbgg_EzVulv8yT-cztwsKcbbLs3Bw6XMe2miJmf4smslZHDVRHs2FFW0RRxTuoYnNaWcx24o57J1r5HlCwsM', start_index=23697)
Annotation(end_index=23753, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLPLKj8I2IfVMPrs7IIPdq9zwPJyl2oJfJZIGDMYuv133Ucu-NNKpQSDPr4rNi5eVtCJW9y9cDTdXwtlO4hXGLyiz0zGjtW6U3bY7XD9Q-O4-bUXXF5PE=', start_index=23744)
Annotation(end_index=23799, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9geWaz0NZJg9oAEjuXJN-DHk8f4yj1ph6GkPQ2OBlKKXfYyQuBW-9wiStdEalVA-mWlowJYFGSGzRG2iVu_4mfJllnjA5D37xy3rMtxhNpDkhAQdxz0lHsg3re_WzsvSWdL3N99-r', start_index=23789)
Annotation(end_index=23830, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxLNYMFNnzmRkl6ugWh_iEg3rYDGSY6L7Tk84kONsv6SqEOf9uRuR0D8O2xFgWmEPLZ6M7FW0iEQhew-hVxverPjGeB8wEr_icLu2XFccgNwrgwcsahMrl102_7YVBGwacCdW5isYhFFm_Mi_XPKZiyuys0m3_IF144SNPLZDTudIc3CapszpxAuc5xkpeK3AUIWDpP2MPBvZEM25FerbAeggiVyzoIaaFhbbQ2sEOABfTwtxq37fFEgg_HsZnbOC7RQdUUhTVImxpf1sFNGLryur3TkRs0P5mf6MxnofLdEZOucspmMAksOvTsetkvY5Jml2g0sFSuCa7wJy1Iuvs6RY=', start_index=23820)
Annotation(end_index=23902, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElf6Vu_fuDg2LflXuu65dyE1waLXPDY9pcGej-Y_WUwkHVcD1st8aIJowbDwwkLwaSwVVQXqEmVBPx9rvHGjMKCmqy31aAJiVlz9Uips-jarnVhEjT053-9lo3jJFMuxjwS0dE8ikDk6eO3fXTSzvoQANg-6wKlIcOHPuHbireWmGOO0_lBHQ3QW_dmbt2yYg8LnaMTEwQNEJArphwHgiO7ZNqKZO9HmPwRIo8eHIQYWRtmTBwWaF9jLJm9HBeAw==', start_index=23892)
Annotation(end_index=23971, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzMyy0UnwJpjytRtPWAWDNZTWGceWWucey4Pm3E-aIXou4b1wFdhP8wIpTFP62sHzlVthgY9Om-0q8O_JwUYxM2_IbGH85up_CPuJcwbw1gI9ycjVInwukhgKzsBeBhXf6PLe4__oIBZSdiDx4DLCW0JJfC3AW', start_index=23961)
Annotation(end_index=23997, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHk1hnKNRj7V4Uy4zUzvpUlqR6-ZP0Gf8Uh4xEZrGHNQCDQj_1OHbWmN7KT4UUXHRpV07Z16VlwWBeH13O08ayJrbn-Rjr9iGg8E9UNYC3lEijyzgQ-Xi8x4ucEOSQEiv1FMBpCH802', start_index=23987)
Annotation(end_index=24027, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNr5s5wDHAuLPHR4jozhXortzkRm86IlcHyAA2NkG_UpWy49esrt4Vzw2v7Yj4tEtT915tPklzJGEeqV9fFIYlbJjgoMJSpNx2dkt5PvJoeyMRf1EXIiTjTQ==', start_index=24018)
Annotation(end_index=24074, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLPLKj8I2IfVMPrs7IIPdq9zwPJyl2oJfJZIGDMYuv133Ucu-NNKpQSDPr4rNi5eVtCJW9y9cDTdXwtlO4hXGLyiz0zGjtW6U3bY7XD9Q-O4-bUXXF5PE=', start_index=24065)
Annotation(end_index=24120, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgWZhHJ6EJQHmfJEaI8FL-geOaR--y9tBuzfgTv7g_ZnkKk3kITT2lZ9I1Bakeui1AnRMI-W0nNRKe2UGFy-ESzXhc331m_lRXzvDed_BLQqko8A9X2OM0pENZ6JKnhv9HzXQwf2fYwnHmWjRhlGyWq_yMonUoTvJFLxIqrfs7-iTgSKGLq1dg_RIW60oFBhrHdgwsOYKt0zqoGixYVksqWglRuYeMQTE5iSckVH27TyKyGHP8kdyRn8Gp', start_index=24110)
Annotation(end_index=24160, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKBt1X--6iUOnBSoVDISmzVfPUEeSBc9nTLxBB_xkvH_koM6ZV-DzHwBJ5xzdGdReiLLjmROoVTcvZ_W2KGCLwwkGqIKK3uxzjl7OGWy6dnhtVgWgGP96eGQ==', start_index=24151)
Annotation(end_index=24189, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4Wy3Pj3pGf8z_Ep8Ik3_uQC-VGl6szZ24Y4oshiB2T4iSn1vcPKGosfx22GMTDJOHx0ICK1fq0TxCJMMg3m7amTy_9UNvAFRZphLhZdRGRGPD5fm_WdQl-MAb41xtfN6X8z9CPNSXPLVKJSSrssspG50aug==', start_index=24180)
Annotation(end_index=24239, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGk9hosLjihIOLp1HScPv3m6aUW7qBxiCQUpbDibQ6C6q34JpkhUCb1Ki6VUu3-AmEZ-HKTR9ZkHFkAlyXuIsI8csjknf3gcFb1MFhtTo0VmsXldYioEdxOEihtl6HUb6N0iMMXRRKRLCcR-WoAvihAPHipoxIVE-rOSw_2M0klNozl7fAADuiMt6enFkQ83VQWhTFct3g5elndy_stIg0xS4C5W3W2J28bSZ5ztMZgYPCe6JiIP5TQDtaqr-lvjwLhN2c5ZrsEJKytrT3-FqixOcZ1nrhB7DaB18BSc-OXY6R9', start_index=24229)
Annotation(end_index=24324, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLPLKj8I2IfVMPrs7IIPdq9zwPJyl2oJfJZIGDMYuv133Ucu-NNKpQSDPr4rNi5eVtCJW9y9cDTdXwtlO4hXGLyiz0zGjtW6U3bY7XD9Q-O4-bUXXF5PE=', start_index=24315)
Annotation(end_index=24369, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNr5s5wDHAuLPHR4jozhXortzkRm86IlcHyAA2NkG_UpWy49esrt4Vzw2v7Yj4tEtT915tPklzJGEeqV9fFIYlbJjgoMJSpNx2dkt5PvJoeyMRf1EXIiTjTQ==', start_index=24360)
Annotation(end_index=24416, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF43YgCHTEZV23pS45mlWqpyUOe9rplXc8QbGR_0i1o8VQirO3KIWUym9C-pKSy3WR2CfM0cTKpwipBqRMtu_AQcAc2EN_1X-hpuiqiVDSgM4aRbCo7ypDTwDJGz3dTBw6YABriyTobWk2svcFN4vVlmBbU9dnkNvIDsTi9pyM35gmpzSbDOGIOCmuFzIo_9KdzN5q2frNJkkJLrgX-LwyHgaRapOVPWcs=', start_index=24407)
Annotation(end_index=24461, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeI1rYsEErd1OZ9j7D4HNJ0EZtIbBJ07-5wOKJNglVjJN4Narhc11y9hlN1EMRzmmmZYsqsAw0gDgwB8c6xeJZP9VPeHWqeScUd8d4Uaag6v_mK6ERtGZ9IQ==', start_index=24451)
Annotation(end_index=24491, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRc543v5rP4-_EFhAwzIoXvzo9uMUCo5mB3TF4CbocPi_3EM4-W2DKhdtrC_FTvaTc4BQOl2eIScFj6equ6PYSQiKp88O6JpMvzdmFo4nqiFfqULSk2b2mxVdc3lrb4RdqVx0VKrWli6ZMG2oE2A7nfMrZO9c2OZB2L865ywSfmj48N70mIt2TAdxnpruxf9s175aaPFLa2TEiZXxgb9tf', start_index=24481)
Annotation(end_index=24524, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvU16ZZjielUPccGPDtbr5psOSeUGfonkkIXaWLFSIUlz7zT8uNFhYLWYuWZm4I3nDWa4IGq0jkUmY2eqkbme-O6nLNF04swvvo1PtCveHYA7COSasCjVcyjXvoHPR81j2c6iK7heNKLlxTIBkYJPm0gmq4c_OuM-nU7kWfPsxcLjFam5lzEnm0KgOs7-0iZsWzONEvyjd8bdvbJ3t3syCskape213LlZ6_KREYVUzokjrigzxrLkwQUWkhq66SxY=', start_index=24514)
Annotation(end_index=24565, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFr2RHUuFmKf7MewFxRsilRYhN_5d4ezYr0JVVUHOdFl0tS9d43mIoCJUiQKEenoJjkqlvc0BF_gVUPfN-hEZ0cuZ3iTUXWgZYMD7Fy7SqmrNqI-zBwMXMriE-mqhXTIDs=', start_index=24555)
Annotation(end_index=24611, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmgTPW3dCE-ef0XtbKKq7iZhIxf5vr6o51k981O81KFHX0jZjGi9SxpSwNU9VQwJcdeAwmX_WcmQUs3N9cGswkzql9df7J1DuJZGu6B4GM-qC_vmJlMQu2Q1tlJ8zPf6xzovS7fJVV', start_index=24601)
Annotation(end_index=24659, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjiWwms_uWQu_SR_lBpj37fpjEtAQEWRdmxInEiX3CMqFEZnIEMrtPi3XseW2srYTQL7ksA7aPej52pnCtEak8ipVun_dlc2qWHz3B4okznIDaXU_z-1A4JMBcN8NPrH8yx9XKDvLfMYsi', start_index=24649)
Annotation(end_index=24696, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg_PaRFaSUv7_UPDLpPLeFhFJfVD2ogsTPaIssOYfYqJYGykoR9MqSjs8wRZyYeQafX7wEfUikYzzUcd7z2uaLFbrdphOEdlXQz_8cicRpgTY_xh5QA0EdF3BEnttjFrreR1oQrnB5DcT0HXN57Mt8cZ4eKtw0v7AqiSBWu2haBUZn3JAjSGmTST3v0P15bTMq5FC1sYPk7ll17jsoiYCfZaQZWriArQXkDPk2ibafcRi_Ulnxh80ooBYz1rT5DfDbQw==', start_index=24686)
Annotation(end_index=24739, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFA2eR7Zg-oLQhxZpu7NZryeYeqSFYt1S2w6AP8fKm4wrWszMTSc2PKg7LUlqRJPLeK3i3w2aHAkTu6eafjX4TowNpGckof4uK6kcCzLt0iCvJ2ALCghRn8Ds-ymPL2yvlTEzUSjxQamYuMd93DZTE5D5B2o1LEiFfuuNkdh8G-QA==', start_index=24729)
Annotation(end_index=24805, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKZDqJEHjKuCAbGLKn3936h_oKtz93IJsgOKAb_r6puKZLLR8oiEjmlCKtNFBYgytRM6f9KkbOBcSLZHnQ0P8xCmn_KMHKrc0zz4g6i0wkgVUdC1zVzpGiVq5KFfnHhq-lQCyhTuK_DOIG2Va53VKKCNmGYNinCW2gb0dyx2qW7lOJf4EyNSXHLX9qxUOjvvivBjc5Ggnn8SkrjlV02S8ESrV-sc3shfyuD-H7iQjMACOM4perRW7njT96wb52P88=', start_index=24795)
Annotation(end_index=24847, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNr5s5wDHAuLPHR4jozhXortzkRm86IlcHyAA2NkG_UpWy49esrt4Vzw2v7Yj4tEtT915tPklzJGEeqV9fFIYlbJjgoMJSpNx2dkt5PvJoeyMRf1EXIiTjTQ==', start_index=24838)
Annotation(end_index=24894, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLPLKj8I2IfVMPrs7IIPdq9zwPJyl2oJfJZIGDMYuv133Ucu-NNKpQSDPr4rNi5eVtCJW9y9cDTdXwtlO4hXGLyiz0zGjtW6U3bY7XD9Q-O4-bUXXF5PE=', start_index=24885)
Annotation(end_index=24940, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0HbhFI3L6juMHw7mVZRZfVhgVUUiz71yIqNwFO0lp8JSObRFl9Owb1EFLQABcXklzXUfLDX-7Ia1PCwHr-w9K6ngrV_ZXAb87c7sAsLq9LnuKSppG1A==', start_index=24930)
Annotation(end_index=24986, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvU16ZZjielUPccGPDtbr5psOSeUGfonkkIXaWLFSIUlz7zT8uNFhYLWYuWZm4I3nDWa4IGq0jkUmY2eqkbme-O6nLNF04swvvo1PtCveHYA7COSasCjVcyjXvoHPR81j2c6iK7heNKLlxTIBkYJPm0gmq4c_OuM-nU7kWfPsxcLjFam5lzEnm0KgOs7-0iZsWzONEvyjd8bdvbJ3t3syCskape213LlZ6_KREYVUzokjrigzxrLkwQUWkhq66SxY=', start_index=24976)
Annotation(end_index=25027, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRc543v5rP4-_EFhAwzIoXvzo9uMUCo5mB3TF4CbocPi_3EM4-W2DKhdtrC_FTvaTc4BQOl2eIScFj6equ6PYSQiKp88O6JpMvzdmFo4nqiFfqULSk2b2mxVdc3lrb4RdqVx0VKrWli6ZMG2oE2A7nfMrZO9c2OZB2L865ywSfmj48N70mIt2TAdxnpruxf9s175aaPFLa2TEiZXxgb9tf', start_index=25017)
Annotation(end_index=25077, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLPLKj8I2IfVMPrs7IIPdq9zwPJyl2oJfJZIGDMYuv133Ucu-NNKpQSDPr4rNi5eVtCJW9y9cDTdXwtlO4hXGLyiz0zGjtW6U3bY7XD9Q-O4-bUXXF5PE=', start_index=25068)
Annotation(end_index=25122, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNr5s5wDHAuLPHR4jozhXortzkRm86IlcHyAA2NkG_UpWy49esrt4Vzw2v7Yj4tEtT915tPklzJGEeqV9fFIYlbJjgoMJSpNx2dkt5PvJoeyMRf1EXIiTjTQ==', start_index=25113)

## Sources
