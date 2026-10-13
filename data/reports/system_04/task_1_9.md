# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** ccaedb8b | **Time:** 288.10s | **Cost:** $0.77693
--------------------------------------------------------------------------------

# Implementing Synaptic Plasticity in Neuromorphic Computing: Balancing Energy Efficiency, Computational Expressiveness, and Physical Constraints

### Key Points
*   **Imbalanced Plasticity for Sparsity:** Implementing learning rules where synaptic depression is slightly stronger than potentiation naturally induces connectivity sparsity (L1 regularization). This mimics biological energy conservation strategies found in the cerebellum and reduces hardware power consumption by maximizing the number of "silent" or zero-weight synapses without sacrificing information storage capacity.
*   **Synaptic Caching and Hierarchical Plasticity:** To mitigate the high energy cost of constant memory consolidation, systems can employ "synaptic caching." This involves using metabolically cheap, transient plasticity (Short-Term Plasticity or STP) for initial storage and only consolidating to expensive, persistent forms (Long-Term Plasticity or LTP) when a threshold is met. This hierarchy balances rapid adaptability with long-term retention.
*   **Three-Factor Learning Rules:** To achieve computational expressiveness beyond simple Hebbian association, hardware must implement three-factor rules (pre-synaptic activity, post-synaptic activity, and a modulatory signal like reward or error). This enables reinforcement learning and solves the "credit assignment" problem in spiking networks, often utilizing "eligibility traces" to bridge the temporal gap between neural activity and feedback.
*   **Embracing Device Non-Idealities:** Physical limitations of memristors, such as variability and stochasticity, can be leveraged rather than suppressed. Stochastic switching can implement probabilistic learning rules that prevent overfitting and improve generalization. Furthermore, heterosynaptic plasticity mechanisms (normalization) are essential to stabilize network dynamics against the runaway positive feedback loops inherent in Hebbian learning on imperfect hardware.

---

## 1. Introduction

The transition from von Neumann architectures to neuromorphic computing represents a fundamental shift in information processing, moving from centralized, sequential logic to distributed, event-driven parallel processing. A critical component of this paradigm is **synaptic plasticity**—the ability of connections between artificial neurons to change strength over time. While biological brains achieve remarkable computational expressiveness with a power budget of approximately 20 watts [cite: 1, 2], replicating this efficiency in silicon while maintaining the ability to solve complex tasks remains a formidable challenge.

The implementation of synaptic plasticity in hardware faces a trilemma: it must be **energy-efficient** (minimizing power per synaptic operation), **computationally expressive** (capable of learning complex temporal and spatial patterns), and robust to **physical device limitations** (such as variability, low precision, and conductance drift).

This report analyzes how recent research addresses this trilemma. It explores bio-inspired mechanisms like imbalanced plasticity and synaptic caching that optimize energy use, algorithmic innovations like three-factor learning rules that enhance expressiveness, and hardware-software co-design strategies that mitigate or exploit the non-idealities of emerging memory devices.

---

## 2. Theoretical Frameworks for Energy-Efficient Plasticity

To balance energy and expressiveness, neuromorphic engineers look to the metabolic constraints that shaped the evolution of the biological brain. Two primary theoretical frameworks have emerged: the induction of sparsity through imbalanced plasticity and the reduction of consolidation costs through synaptic caching.

### 2.1 Imbalanced Plasticity and Sparse Connectivity
In biological systems, synaptic transmission dominates energy consumption. Consequently, evolutionary pressure has favored sparse coding and sparse connectivity, ensuring that only a fraction of synapses are active at any given time. Research indicates that this sparsity can be engineered into neuromorphic systems through specific plasticity rules.

**The Mechanism of Imbalance:**
Standard Hebbian learning often leads to dense connectivity matrices which are computationally expensive to update and store. However, studies show that when synaptic potentiation (strengthening) and depression (weakening) are balanced according to mean presynaptic activity, information storage is maximized. Crucially, introducing an **imbalance towards depression**—where the weakening of synapses is slightly more aggressive than their strengthening—acts as a regularizing constraint on the synaptic weight vector [cite: 3, 4].

**Computational and Energetic Implications:**
*   **L1 Regularization:** This imbalance mathematically corresponds to imposing an L1-norm constraint on the weights, a technique well-known in machine learning to induce sparsity (driving many weights to exactly zero) [cite: 3, 4].
*   **Silent Synapses:** In hardware, a "zero-weight" synapse effectively disconnects, halting the flow of spikes and eliminating dynamic power consumption for that connection. Research suggests that an imbalance towards depression can result in a configuration where approximately 50% or more of synapses are silent, mimicking the high fraction of silent synapses observed in the cerebellum [cite: 3, 5].
*   **Performance Retention:** Remarkably, this aggressive pruning does not significantly degrade computational performance. The network maintains high information capacity per non-zero synapse, thereby boosting "memory efficiency" [cite: 4].

For neuromorphic hardware, implementing imbalanced plasticity rules offers a direct pathway to energy efficiency. By biasing the learning circuits (e.g., in memristor crossbars) to favor Reset (depression) over Set (potentiation) operations, the system naturally evolves toward a sparse, low-power state without requiring complex, post-hoc pruning algorithms.

### 2.2 Synaptic Caching: Decoupling Transient and Persistent Storage
Learning is metabolically expensive. In biology, the formation of long-term memory (LTM) requires protein synthesis, which consumes significant energy. Conversely, transient memory (Short-Term Plasticity or STP) relies on temporary biochemical changes and is metabolically cheap.

**The Synaptic Caching Algorithm:**
To optimize energy, neuromorphic systems can implement "synaptic caching." This algorithm distributes learning across transient and persistent forms of plasticity. Weight updates are initially stored in a labile, transient state (the "cache"). Only when these transient changes accumulate to cross a specific threshold are they consolidated into a persistent, stable weight [cite: 6, 7].

**Hardware Relevance:**
*   **Reduced Write Operations:** In non-volatile memory (NVM) devices like Phase-Change Memory (PCM) or Resistive RAM (RRAM), the "write" operation is the most energy-intensive and damaging process (limiting endurance). Synaptic caching reduces the frequency of these expensive writes.
*   **Hierarchical Implementation:** A hardware architecture can utilize a small, volatile capacitor or SRAM buffer to represent the "transient" weight (low energy, high speed) and a non-volatile memristor for the "persistent" weight. The system only triggers a high-energy programming pulse to the memristor when the capacitor's charge exceeds a threshold [cite: 8].
*   **Efficiency Gains:** Models suggest that synaptic caching can boost energy efficiency manifold (up to 10-fold) compared to naive implementations where every learning event triggers a persistent weight update [cite: 9, 10]. This approach aligns with the "synaptic tagging and capture" hypothesis in neuroscience, providing a bio-plausible blueprint for managing memory hierarchies in silicon [cite: 9, 10].

---

## 3. Enhancing Computational Expressiveness: Advanced Learning Rules

While energy efficiency is paramount, the system must remain computationally expressive. Simple Pairwise Spike-Timing-Dependent Plasticity (STDP)—where a synapse changes based solely on the timing of pre- and post-synaptic spikes—is often insufficient for complex tasks like supervised classification or reinforcement learning.

### 3.1 Three-Factor Learning Rules
To enable supervised and reinforcement learning in spiking neural networks (SNNs), "three-factor" learning rules are essential. These rules extend the local Hebbian update (Factors 1 and 2) with a third, global signal (Factor 3) representing reward, error, or novelty [cite: 11, 12, 13].

**The Credit Assignment Problem:**
In a temporal stream of data, a reward may arrive significantly later than the neural activity that caused it. Standard STDP cannot bridge this gap. Three-factor rules solve this by introducing **eligibility traces**.
*   **Eligibility Traces:** When a pre- and post-synaptic spike pair occurs, instead of immediately updating the weight, the synapse sets a "flag" or eligibility trace. This trace decays over time. If a global reward signal (the third factor) arrives while the trace is active, the weight is updated [cite: 12, 14].
*   **Hardware Implementation:** In neuromorphic processors like Intel’s Loihi or the BrainScaleS system, eligibility traces are implemented as local state variables within the synapse or plasticity processing unit. For example, the BrainScaleS-2 system uses calcium-based plasticity rules where calcium transients act as the eligibility trace, bridging the timescale between millisecond spikes and second-long behavioral feedback [cite: 15, 16].

**Event-Based Three-Factor Local Plasticity (ETLP):**
Recent work proposes ETLP, which uses pre-synaptic spike traces, post-synaptic membrane voltage, and a third factor (projected labels) to enable online learning without global error backpropagation. This method respects the locality constraints of neuromorphic hardware (where memory and compute are co-localized) while achieving accuracy competitive with Back-Propagation Through Time (BPTT) [cite: 11, 17].

### 3.2 Heterosynaptic Plasticity and Normalization
A major limitation of Hebbian (homosynaptic) plasticity is positive feedback: strong synapses cause more firing, which leads to further strengthening, eventually saturating the weights (runaway dynamics). This reduces computational expressiveness by degrading the network's ability to discriminate patterns.

**The Role of Heterosynaptic Plasticity:**
Heterosynaptic plasticity involves changes at synapses that were *not* active during the induction of plasticity. It serves as a homeostatic mechanism, often implementing **weight normalization** [cite: 18, 19].
*   **Competition:** If one synapse strengthens, heterosynaptic rules can induce depression in neighboring synapses to keep the total synaptic weight of the neuron constant [cite: 20, 21].
*   **Stability:** This mechanism prevents runaway dynamics and ensures that neurons remain sensitive to input variations. In hardware, this can be implemented via local circuitry that monitors the total current or weight sum and applies a global scaling factor or subtractive inhibition to the synaptic row [cite: 22].
*   **Expressiveness:** By enforcing competition, heterosynaptic plasticity prevents a single strong feature from dominating the neuron's response, forcing the neuron to learn more diverse and informative representations [cite: 23, 24].

---

## 4. Addressing Physical Device Limitations

The physical realization of these plasticity rules relies on devices like memristors (RRAM, PCM, Ferroelectric Tunnel Junctions). However, these devices are imperfect. They suffer from variability, stochasticity, and limited precision.

### 4.1 Mitigating and Exploiting Variability
Device-to-device and cycle-to-cycle variability are often viewed as defects. However, in the context of bio-inspired computing, they can be managed or even utilized.

**Weight Variation-Aware Training (WVAT):**
To handle the inherent variability of nano-scale devices, researchers have developed training methods that explicitly account for weight perturbations. WVAT trains the network to find a "flat" minimum in the loss landscape, where the system is robust to the noise introduced by the hardware. This approach has been shown to reduce accuracy degradation significantly (e.g., maintaining >85% accuracy on CIFAR-10 despite hardware noise) [cite: 25].

**Stochasticity as a Feature:**
The stochastic nature of memristor switching (probabilistic rather than deterministic updates) can be leveraged to implement stochastic learning rules.
*   **Probabilistic STDP:** Instead of precisely changing a weight by a small amount $\delta w$, the hardware can switch a binary synapse with probability $P$. Over time and across an ensemble, this approximates high-precision learning [cite: 26, 27].
*   **Regularization:** Noise in the synaptic update acts as a regularizer, preventing overfitting and helping the network escape local minima during learning [cite: 28, 29].

### 4.2 Low-Precision Computing
Traditional deep learning relies on 32-bit floating-point numbers. Neuromorphic hardware often relies on low-precision (1-bit to 4-bit) weights to maximize density and minimize energy.

**Binary and Ternary Synapses:**
Research demonstrates that high accuracy (e.g., >99% on MNIST) is achievable with binary (1-bit) or ternary weights if the network is sufficiently sparse or if ensemble methods are used [cite: 26, 30].
*   **Probabilistic Training:** One effective strategy is to train a network using continuous probabilities and then sample these probabilities to deploy binary weights onto the chip. This "ensemble of sampled networks" approach allows low-precision hardware to approximate the performance of high-precision software [cite: 26, 27].
*   **Energy Gains:** The use of 1-bit synapses eliminates the need for complex Digital-to-Analog Converters (DACs) and reduces memory bandwidth, leading to orders-of-magnitude energy savings compared to GPU implementations [cite: 31, 32].

### 4.3 Conductance Drift and Reliability
Phase-Change Memory (PCM) devices suffer from conductance drift, where the programmed weight changes over time as the amorphous material relaxes.
*   **Slope Correction:** To combat this, researchers have developed "slope correction" techniques that adjust the reading or activation function over time to compensate for the predictable drift trajectory of the device [cite: 33].
*   **Periodic Re-consolidation:** Similar to the synaptic caching concept, the system can periodically read drifting weights and "refresh" them, or use drift-resilient encoding schemes [cite: 33].

---

## 5. Bridging Short-Term and Long-Term Dynamics in Hardware

A key aspect of expressiveness is the ability to process information across multiple timescales. This requires hardware that can transition between Short-Term Plasticity (STP) and Long-Term Plasticity (LTP).

### 5.1 Pulse-Based Modulation of Plasticity
In memristive devices, the transition from STP to LTP can be controlled by the characteristics of the programming pulses.
*   **Pulse Width and Frequency:** Short, infrequent pulses may cause temporary conductance changes (STP) due to charge trapping or temporary ion migration. Longer, higher-amplitude, or high-frequency pulse trains can drive ions into stable lattice positions or form robust filaments, resulting in non-volatile changes (LTP) [cite: 34, 35].
*   **Bio-Mimicry:** This behavior mimics the biological transition where repeated stimulation leads to permanent synaptic strengthening. For example, in $HfO_x/ZnO$ bilayers or $Mo_2C/MoS_2$ devices, increasing the pulse width or reducing the interval between pulses (simulating high-frequency firing) successfully transitions the device from a volatile STP state to a non-volatile LTP state [cite: 34, 35].

### 5.2 Synaptic Tagging and Capture (STC) in Silicon
The STC hypothesis explains how weak events can be consolidated if they occur near strong events.
*   **Hardware Implementation:** The BrainScaleS-2 system implements STC by using a "tag" variable (based on calcium accumulation) that decays over time. If a "capture" signal (representing protein synthesis) is triggered by strong activity, synapses with active tags are consolidated. This allows the hardware to associate events separated by significant time windows, enhancing its ability to learn temporal correlations [cite: 15, 16, 36].

---

## 6. Co-Design Strategies

The successful implementation of these mechanisms requires a tight co-design of algorithms and hardware.

*   **Hardware-Aware Algorithms:** Algorithms must be designed with the specific constraints of the hardware in mind (e.g., local learning rules like ETLP that do not require global error signals) [cite: 11, 37].
*   **Device-Algorithm Matching:** The choice of material (e.g., Ferroelectric vs. PCM) dictates the available plasticity rules. Ferroelectric Tunnel Junctions (FTJs), for instance, offer linear symmetric switching which is beneficial for online learning, while PCM's abrupt reset behavior requires specific architectural adaptations like "2-PCM" synapses (using two devices per synapse to represent positive and negative weights) [cite: 33, 38].
*   **Surrogate Gradients:** To train SNNs despite the non-differentiable nature of spikes, "surrogate gradient" methods are used during offline training to optimize weights that are then deployed to the hardware. This allows the expressiveness of backpropagation to be combined with the efficiency of spiking hardware [cite: 11, 39].

---

## 7. Conclusion

Balancing energy efficiency with computational expressiveness in neuromorphic computing requires a multi-layered approach that embraces physical constraints rather than fighting them.

1.  **Efficiency** is achieved through **imbalanced plasticity** (inducing sparsity) and **synaptic caching** (minimizing expensive memory writes).
2.  **Expressiveness** is enhanced by **three-factor learning rules** (enabling reinforcement learning) and **heterosynaptic plasticity** (ensuring stability and competition).
3.  **Physical Limitations** are addressed by exploiting **stochasticity** for probabilistic learning, using **low-precision** ensembles, and modulating **pulse dynamics** to emulate the transition from short-term to long-term memory.

By integrating these biological principles with advanced materials science and algorithmic innovation, neuromorphic systems can move closer to the brain's unparalleled efficiency and adaptability.

---

## 8. Detailed Analysis of Plasticity Mechanisms

### 8.1 Imbalanced Plasticity: The Path to Energy-Efficient Sparsity
The concept of imbalanced plasticity is central to achieving energy efficiency. In biological brains, specifically the cerebellum, a high fraction of synapses are "silent" or possess zero weight. This is not a defect but a feature optimized for energy conservation.

**Theoretical Underpinnings:**
Research by Sacramento et al. [cite: 3, 4] demonstrates that information storage in a perceptron is maximized when potentiation and depression are balanced. However, by shifting this balance slightly towards depression, the network is forced to select only the most critical correlations to maintain as active synapses.
*   **Mathematical Formulation:** The learning rule can be viewed as minimizing an error function subject to a constraint on the sum of absolute weights ($\sum |w_i|$). This is equivalent to L1 regularization (Lasso), which is mathematically proven to induce sparsity.
*   **Energy Savings:** In neuromorphic hardware, a silent synapse implies no switching events and no current flow. If 50-80% of synapses are silenced via imbalanced plasticity, the dynamic power consumption of the crossbar array drops proportionally. This allows the system to operate within a tight thermal envelope, crucial for edge computing and implantable devices [cite: 3, 5].

### 8.2 Synaptic Caching: Optimizing the Metabolic Cost of Learning
The "Synaptic Caching" hypothesis posits that the brain minimizes the metabolic cost of learning by decoupling the *acquisition* of information from its *consolidation*.

**Algorithmic Implementation:**
*   **Transient Weights ($W_t$):** Rapidly changing, volatile, low-energy cost. In hardware, this could be charge on a capacitor or the state of a volatile selector.
*   **Persistent Weights ($W_p$):** Slowly changing, non-volatile, high-energy cost. In hardware, this is the resistive state of the memristor (RRAM/PCM).
*   **The Update Rule:** $\Delta W_t$ accumulates with every learning event. $W_p$ is updated only if $|W_t| > \theta$ (threshold). After update, $W_t$ is reset.
*   **Impact:** This filters out noise (small, random fluctuations in $W_t$ never trigger a $W_p$ update) and batches significant updates. Li & van Rossum showed this can reduce the energy cost of plasticity by orders of magnitude without compromising the final learned accuracy [cite: 6, 7, 10].

### 8.3 Heterosynaptic Plasticity: The Stabilizing Force
While homosynaptic (Hebbian) plasticity ("fire together, wire together") drives association, it is inherently unstable. Without regulation, weights would grow indefinitely (in simulation) or saturate to the maximum conductance state (in hardware), destroying the information content.

**Hardware Realization of Normalization:**
Heterosynaptic plasticity provides the necessary negative feedback.
*   **Mechanism:** When a specific synapse is potentiated, a regulatory signal is broadcast to other synapses on the same neuron (or dendritic branch) to induce a small amount of depression.
*   **Circuitry:** In a memristor crossbar, this can be implemented by monitoring the total current output of a column (neuron). If the current exceeds a target, a global "depression" pulse can be applied to the entire column, slightly reducing the conductance of all memristors. This effectively normalizes the weight vector, keeping the neuron in its sensitive dynamic range [cite: 18, 20, 22].
*   **Computational Benefit:** This competition forces the neuron to be selective. Instead of responding to *all* inputs, it specializes in specific patterns, increasing the "expressiveness" and distinctiveness of the features learned by the network [cite: 19, 23].

---

## 9. Hardware Constraints and Solutions

### 9.1 The Memristor: A Synaptic mimic with Non-Idealities
Memristors (Resistive RAM, Phase Change Memory, etc.) are the leading candidates for artificial synapses due to their ability to store information as resistance, enabling in-memory computing. However, they differ from ideal theoretical synapses.

**Non-Idealities:**
1.  **Variability:** No two devices are identical. The voltage required to switch a device varies, and the resulting resistance state has a spread [cite: 40, 41].
2.  **Non-Linearity:** The change in conductance is often not linear with respect to the number of pulses. Potentiation might be abrupt, while depression is gradual (or vice versa) [cite: 33, 42].
3.  **Limited Precision:** While floating-point simulation assumes infinite precision, real devices might only reliably distinguish 4 to 16 states (2-4 bits) [cite: 30, 43].

**Solutions:**
*   **Stochastic Rounding:** To handle limited precision, updates that are smaller than the minimum step size of the device are not discarded. Instead, they are implemented probabilistically. If a calculated update is 0.3 of a step, the device is switched with a 30% probability. Over time, the expected value of the weight matches the high-precision target [cite: 15, 43].
*   **2-Device Synapses:** To handle asymmetry (e.g., abrupt set, gradual reset), a single synapse can be represented by two memristors working in differential mode ($G_{synapse} = G_1 - G_2$). One device handles potentiation (by increasing $G_1$) and the other depression (by increasing $G_2$), or one is used for the positive part of the weight and the other for the negative [cite: 33, 44].

### 9.2 Low-Precision and Binary Weights
The constraint of low precision is not merely a hurdle but an avenue for extreme efficiency.
*   **TrueNorth and Binary Crossbars:** IBM's TrueNorth chip utilizes binary synapses (active or inactive). Research shows that by training a network to learn continuous probabilities and then sampling them to create binary crossbars, performance on MNIST can reach 99.42% with an ensemble of 64 networks, or 92.7% with a single network at a minuscule energy cost of 0.268 µJ per image [cite: 26, 27, 32].
*   **Expressiveness via Ensembles:** The loss of expressiveness in a single binary network is compensated by running multiple small, efficient networks in parallel (ensembles). This trade-off favors energy efficiency while recovering high accuracy [cite: 26, 32].

---

## 10. Future Directions: Material-Algorithm Co-Evolution

The future of neuromorphic computing lies in the deep integration of material properties with learning algorithms.

*   **Organic and 2D Materials:** Emerging research into organic small molecules and 2D materials (like $MoS_2$) shows promise for flexible, tunable plasticity. These materials can exhibit intrinsic STP-to-LTP transitions and linear conductance modulation, potentially overcoming the limitations of filamentary RRAM [cite: 35, 45, 46].
*   **Ferroelectric Devices:** Ferroelectric Tunnel Junctions (FTJs) offer distinct advantages such as linearity and symmetry in switching, which are critical for online learning algorithms that assume symmetric updates. They also provide ultra-low power operation due to field-driven (rather than current-driven) switching [cite: 38].
*   **Neuromorphic-Enhanced Edge AI:** The combination of local, three-factor learning rules (like ETLP) with energy-efficient hardware is poised to enable "always-on" learning in edge devices (wearables, IoT). This allows devices to adapt to new users or environments continuously without needing connection to a cloud server [cite: 11, 29, 37].

In conclusion, the implementation of synaptic plasticity in neuromorphic hardware is a complex optimization problem. By mimicking biological strategies like sparsity and caching, and by developing algorithms that are robust to the stochastic nature of physical matter, researchers are forging a path toward computing systems that rival the brain in both efficiency and capability.

**Sources:**
1. [humanbrainproject.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIbhXnCOcCFcGfXwRHN-fSxLWPH7k8Arg9dYuJRcV1RObiI1xaeoLg7cS5MiRnSSmaABWbS1DkQIDDsdgpbkzNrM6btXlb9p77fih3cEBmzmRaA-QDoj8J18HkDtiJD97zKbWwexuyyJWKVIZWL4MgKJ74dyoy6zNnC34GUHpiMaG1TVpI7gc7yJAjMFPvixI3nA-udgC5X095-XKkMYvqbId0YlSuezH6UPBDkClIFw==)
2. [sciencedaily.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgW0IRYCoEBYlyiTnp7pFLtTNxAvSfbTAdbS9qkwS6cGGh2XesP2MfzrYZ5_zcjBdL6bdbuRHWNZpiYW88Xoygv7sD0uf3X3NJjocIonGv6SQEeOJhhJZ9Xelj2vOpiYz75MO7wOCPqAm4zI8GdctRCyCZMg==)
3. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEELT7EIbHMndQatlVBbDZfmjd7cgowCz9y29bpjVAQ_bdWvHm6biExTqP0bHi7EUT4rNLtPbnaCOCiFKARYbR-Ydt2f9bv06Hc6VlzZ6J0wnh1WKrDL1gcWCe0wSlXGw==)
4. [plos.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESrecQHALu_ewsBCrqvP0v7l3BF9GmLPmRC4oPw7vbBqpJbDMGo3oDCWpD2E7h-AIYk8JTLfi1sCbmI6rb-srH0ac_pIwmbOu1jJ5UtuU65CRRavo1PEa3fLD5_jNGyZ_5B8hwSllRUqaIw8xeJMPku_I4xF6SNEpnobSfYapST6q_CbE=)
5. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtZjV_hDC_n89iPngrLIeeTVHgt2QC3XsfbenI7CjiteN94AmS6Ae7qoriYuLmUYmhvyfGqQ00uMFKqTHmXPQSTXuhGN2AWQ0nxA4VWSjlRYtdWveKSRtnb6WUlsKEWKgklAGG0e9G)
6. [elifesciences.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1YQuhdGVQpnCKkHBOx-ItBfOUCFc97IoWfwsq_laPdhsRO28F9i4_HjpVKT4jhyaXK76XTq62D7a8Boqz6oU6hg9lXfd9y5woDKjJPzKo7BjlKZES2UdBJaEYxAMnSqQ=)
7. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXKROzqIt1mHnDbEVhkEWvzTOGLA7wCrmBi9eHzVst4dAD-CGzn7T1GHcIn7Diis786TWCwG0MKNm9lzK4a_yIOfpM77hO6eOgiThLZX0-eHso9cflXIbnyDJcx6pcPMLtJG0SsKNkcQ==)
8. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBqFCuJKKARt0EU73jeIfZW-EKRAnGIhU1jbYj2aydQfOlFzZHHBXh4qk7OII8MY_d8pw0CIYwHw_2GGPKaORHeLm9QXijQWQOmAqv4RxmaYNF2o0kt9FJYoM2etiuGDlBxhipsKW3)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfqFXBWDIfu6suGh2vAV7uFGl9dad6VZbHKPYdXyl0EtTRraccPlwyKCTh5I983pegAMsk-6s9Xqw04-t8Rfio2C1fbfymdtKar0IO6Oadls1QpFAJUhnG1GU59yP0Jw==)
10. [elifesciences.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmUeO0X1s0Yk87arnS2R1hqDGFsXIeDVrbSREfOweTlR0CDH4aRD55FMBFzNSxgCEToWM-qJ_Oj_sFTo8cfSU-fHHmesWRQd461nlYmL3Ge2yNuk7Jvj-7X3AKNty8)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpuiSQzrJ_ircKub7VTPvV5IQZ7M0e1ivAuTJAXuQg0hnx91Y4ZlW-yLikBvwuraOBBXIlg_KrohKgsd2YtZi-7SeZgoBlbQlT6KdFrrI4WFUuQ-7zMM60xA8OzQYPYJznSKH0AFJkpDBruUQ3QMH4m8SZ4_5Mt6lCU2pkV0kmPW8d64avRpvN-MQLKZgwB7tL23y0PDjrjOB2OTUHEYvryWTFKM31sk4rFphORLZ22EOH501JNz_IokHlpz3wkvYMiFHqai2wFf2mWy-DR9KweNdvqlFEv5gfdvqMeFVYmFI=)
12. [emergentmind.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4wM17XGr1VvxXQ3s5khg_cJMgix-NOAxRPtShgJCJx1zl1YqIVYN00fQHqmx1sLo5tp1RO3mekX_5M4_sfWiI_g-6NPUpZllqPJxJvHB7tyh08DbMRq8hqbdWdANc2DoKV_QoiZ8OR51Gd8NsTeE8EPkioic=)
13. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6trATjtAatKOHStSqqkOfVfKNU1pe0yzIdOAJAdpfI4fMH4kiZSUu53PCrHb-MgU_N-tt3Jl_tvIzG5ZMqMd0Cx6kP7NeQ56UH3Z_zXf15f5V5e7D0g==)
14. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHo4Dt66pmMg0YLBCWQuDmVm8gv7HM2Cug7gz6a41-62OWYW_LXidbT7bUY8NikHs0IcWBb9iZwKLG7xU7tuGPBvj40AoNywYEd979f7FUA4azZ5nE5L6T6Ncd1BxyRfmRFlAntv3VI)
15. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfWKWguFHRhLzL8GGozZsx8iKO0KZJK0OybVHgTburqI_2OSkgnf3sAvcuxTg62wP7Q-idty8m3FM98Q6R53Vv1XY9gK_XrwCFH54pS8NEOWTXPm3k_kQhiYuKnVvtsOdwVTK8)
16. [emergentmind.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtHLwO7-3uzY1S5xS7HFygYW0Id_9ZH8tXmVTMRG-4KI1hE0PhEn_MeNUt_5RXfND2jc8c6X5oi37cnci6Stjs4zJhVwQN-enoVYvlLWK62F6Tfb8tQ1kSJQrxW1ZIZA5lyxPKGJQoA6b7LeTkDttWmD9hiO4-)
17. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLJo8aWVyaChhOe_QSexobaxLt7n3eblSbc3z5Ou7hjvtvG7JPu36uro_8N6eb06P3w4y-yvZwn9jn241z1daLnPYMSopbyUkVOLiWFk7kRHryZEPANQ==)
18. [core.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF46lguNwB9NnVmXiqHOOBXi_DWHBnazrpA5wmQwoHDikcqZ3ekX_VCFxUDiXP6A8hFBSJl0TjW0pTAuPdrW51QqVa5Nx9Xqjehd6KEk8UDGAY3NyZGn_WlE2VaQonAnKoklQ==)
19. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzkni7B4iUleXrwFoRObSeFHGNrf4bJ3ju2EMzGobK2_VgSdk3vK7oRvhYeF7912q25K4PEU5-J8-5NwHHMOhpKCuZZb8T-exnN_CoNtFiWpkOKUWHT5xDHi52PZBZk_49EzPlZbtx)
20. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_bPhYRGh-vwoWPbj1_hcdw-b_erHbL_qiSplZxaNwSzKBYr6PZTGB1C8dvLSaCtSk5GWllQpxj8RCGdQIxt-5a6wtJbT78gQiXfXucRuGdAsFDuat70vdyWLSCK-wCihUg4q2NNfiJbXGV1P21GvQSdKcWNwJ4COI1K73bNxT91KfXDkl07qqVLg-WPnODxSK)
21. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7IMVoOVIWxUmcYrLp12_TYn8q-ogEuQMx1wbT2ZDdnDTHS1tzZxZSK9pIjHCP1OsT-7h8hGKrp_GFsTpwxJAuZ9yZlF2n5Aooq-mZ8Vp-9PrYNwajHuUFywMygizo0UhXIDhOdkdYsuDHbdAc)
22. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAjkTvv1REHomou2nbHJnnzN4I3GydJPgfVNKqrjLxK85OFB9EOL0atZG-KbI4PwPQ13qoy5ws8lesOkYRf7HvMNqINX4xyMiVYbMODUpTXUAAnutpYw==)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNZ5oMHnDhvKNts8neMVMPPX3oEI3Ndrx3Hu6DcXXi7Zt_39qfaceYCbtpDfC4KgngKHXrlWnKR0M_0QTMcmU1wdFk0Wsi4xiRL-22K4AkMXZeJUWAm2xFvE33kKZPtY9HEUr2RIqQ7fuNEvnlVpmHIPXlOhWykALdWiwG7BersMuUE8g2OIbIp_u4Ol9HCZONbtv8ROUxVH_meD16q9Sc-saMe1YHm6rrBGiDCXE3CYxhI7zeslEqpOTjv9H0OEVyYhM=)
24. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwYXdxizEcqgmAvWjQF_ge3z5FP-nt_F2HIBexfC5r54ZGDoe_dl2f1dA1-yT1SAC8hct_MENClYkcgrnOCU97AsBibb4_OAKmGy7LFvgwdY2PlDd1EOQGar67BduQEcwQM1mR1K7c_pEOEYMiMoahQgIglmkxEC7bbRZEeeipo82mEmfpybW5S7wKnqe04B_jPZAgRcQFV2kAUNRjcLC1xA==)
25. [openreview.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-QucNrSBYw9bOCfTQqXXGszH1S1W8PasVO8WviOqYxtPfeS7nGpGfScDddcv_Dh7C8aIVytYkB5z0vyfCn13NDaZi4DVwnoVcbrC5ZUPihKJP0g3X4jj3FyL3Mk2Xes-y)
26. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmj18nUReMvY0GoGYOwbv4ROW2nDF3R4rZyULdyq8uijsXeF6I6dBJEn_AsQOvVC7dkAE-9b2alVEH26zt9fABo2rdx8z8qC8hs_xUwL9uZBsV9aLN-A==)
27. [neurips.cc](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFf5ewby-8i7au1qrbRY8IB93iQUzRU5dkamOywIkUCnQ0z5nVzKTqVhGqD8P1v1d21udogC_WapAGOw0SvDrEDC-8UFUsVP1eBJvnda1cFhCIXRxKXHUdix5YPtN9oIwNIFLXxi7fGElM62xHa8kkMpzawyJKE0a4AHrU6Qh1ReMjHNVD6tikPDA-KXxLtD58S85g8FGi3u_4=)
28. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuiTB50xJRGQV2CCyE2KGN_gi2mw_RWBozGBICcdPJ5sC51MEB_PUlUmtcZKGktlxbBiol4I3V_uy8f8_OYuyXAlfnx0NPO6DvL8shHvRagAIUwDuZipP2H79eiI5pg13OLeIB3hD2)
29. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcRGKo7lbA3r-QNvwk9LJwMUMP8cJAXI-MczBY5pqLLwMJKdGKFsdLScnoGhi_LgF9qDKvahlVqkMffD4ICeVOx83k-W8ctVYlRJD8rmT15QihG04W5Q==)
30. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRTHvzbc-I9J9srsw1_zLE5A-lJFJshhGqJfrVUmrBrZxuxz4iAM1iDcw1qjGNrHQDilgVhyoQ5zmwsDqahip3Ckvm-APxXednELkvWdWgMw4MmiqTOA==)
31. [mit.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeAs2vLPGineDisvvPzrtrB4y5aPeQ5xRG7h68GXs5yozhMrh4aoM98djoNDmsUdxdaYdPTFYSzjPFKKxCmlIeugOWkQTtF_1mqImOTxMbm8x3FZDGRTxtK9aWf5Ad7kg_BAPIod03v55JpRHUCwxatDtX-lkNirG6EDTBcxxwc47iF6do_x51PDPXuCH6echnnHs=)
32. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFug0NNIJz_2INuhPRjNbQmweGNXfnXVegV3zEkTPMAqOmOp6k_A12hJBTZ7dQeDViVoinTp7srowZnGv90VD7L_oBd3CVvRXL629YXK1OOY0IxemgwWS5ys1-G0IrQDQgs-NDL754ezMf54fH0tPcrccFy3-SIF4Wk52MzLBJEMHkEC0YWzxvdVPx8RbuKPo_vDECRGvM1jsIim3F0_9LycUzRiW7SlTQzCa1bJixcyv1wiZluTb5QVqQ8BTYOYwYEkw54YtlePYebvHGf8eHQxJSbfzvUoRbv8xc2HA==)
33. [ibm.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaSN_TYrkLLZDk5_x7q4NwMoQEl8YQcIxS-vmDT4zJg_1k-O3UnN1FEzt1hx0ieInmaxUN0sRkuXG769f87ppL1hLuvfEhDK_KOjBVblgnfTRwyjiMC2lUOSXgNxAVHr8WDw2dkUhlg1vx4WgkPnrpgwzxwBGPsY7gYKVCHpXiSN2ome5crdqmdzTJU9rX59hVunhDWT2jBzCPOrFpDINe7eCybPAM9S8kZlEx2HMEwyHx)
34. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZ6jyWC3nUXQwrcG9TrlWJlwK4UqVdgz_L2KL4qA74PnNNcEkqKPrldBEl9pYGjgcqCo6pjiMe_jWbFLEa5GxAFgBO6f0vmngFeFRGTyglGAIvkDYSO74m0rhMMEMMbErD8k-8IrrX_57_ObVQqkPq9IEbXp5u1FEEp9bCuoyQ4TldCN9mxpGZVD5mKhwvSzh1JT9zV26mSbnN3VrXaxsxIiQHYhvFlXr_qLwsQXtJZIZAIXwTBV7N4CMVdeDy)
35. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLWDSdgex-XihR5fl-DHID9dfqwujXr4lKYAuRW1V7Kf2M-OFsGK_fRxzmJP9lXAVvm7NgbsCo8K0E81N3BShcNcNFOQ5jZfFP11nJbbfmRJ2zACU4fVEjoPjMpNENT-cxOLgV06rGWKH0Ig-_zmsCAunDbYVhsCH7UbVgDGID50b1Wmgmbn6Y3BqS-v9eZrkTriDX2uVWT3R6J83BFZhq5gbYTko8bY1OTQ2bPY4RsY5h2oTse72W)
36. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTK3SJzWEiuHyN8zNxUvL1hKrzKyhNK8SztVulCoPfiUUYQwuU9-mmXpRNfUvxrPyLxkkmm_zfMcceoeBE_qucb417XMBQlVgfvxIQ4XPqIPBbmppMakf44ILOXD7Tnc7ycH3tMVv5)
37. [purdue.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWO-dhxlUfbi90Ff1c_PZGJ6X5pMPKH3ZbQEFoqrIp2lBZowJXKLrOVyhxacKIUeS1mBQ8Z9Phjit5lO821dbtiZzPtpi4S0Gp-5W_YOnX87oxI31DP8KmpWsMYjxQILpXFWG-yEw2DAt9pl2sepPoWUQCwO44MRTERXLZVbFvcM43NMRI8hxKBZyI2_Om7n8cX-T80ku1H2Dmwa67G8upyTvpAERCmS7HEQMIfeQrPCmZEDJZHpYkiiyeuh5e-fabkR1k0sqmQi00EMiD9rdBcefYZj450qlRXMADKhTIbZ4=)
38. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGl_jljUvdBtSdWZFsek3Sa6287fHWVyA7cqIabAHLbIn0FkAzb9XLHBBPvBoUlLcyyi2zUYikihBt_okJndBsNHMXTRWc4F-_v1M6leytEv2ICaSr9-SP7Ndkkxocec5_O7JOW0_bnAeKgVyyD-hgvYsXAQXNvHpqqazxFat8qxtaVyoR5Yny8Y4taKtwQZeDnJbiEou8PrWrFKG5-JNpHTr5gyPLpw3z2nG3OFiyfhxPXwPnDqqgd7TUdhtc=)
39. [epapers2.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeZ6SssXd6AvNxVEJfc_Khj0SwIDmSF2NL5CzbWXpzv8JEdMNKrI76iRp1cebvRhWIrrp4ZLCZ-rhC0acZ0GWMMi_gIqKQF-lY7nui7xtBZdVSH87SsbLAiun2lemqMwZgvkCRL5GKfHHiCDIfIAeQVH4izdEYGkc=)
40. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAqilk5gxJvF4wXbtjtcmG_VWr1_Z460U_tlwjD7FKP2Pcs3qxegETrUWUltkrsPTMCVSNwe9LkkNBO3A3TwzlcafC--IoPc_0EWxrbJKJixfbIjq382SvELDhtw==)
41. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMCJru6-SPjNtiVzLf72Fx6jCnidLwgssfy1PYqXrz1xgwFALZWwOo_YajgfwUlu7eNaIJp9RayVB474iFmc8PWMUkzKcapHvZT461gUg9APS9wApexTgoDlSFsZCmRgVUw4ejeekN)
42. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6P3bjmsSY9heMIRrXLBAtSQLYRCOBVnXR3YHbICCxep77Neu8x66Xw1N0Nr94ZNe4MI5sUk6XhGfiz7ajgZPoJTzZ-lm5HzgpRiyxCZF6RyUO2rY5a_f8F0Lu12ibkc_LQpMN0s98Xx4dLsU7K-T1Q085HOPCM7g=)
43. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3meIABq72tUfri2oSmjM_vvu0ef7A0TViX6S_H5cf5qcRGF1zmItZ2Vbsi2pfxSfnnw9PXyLEKPiU0Kgn6XHDj8U4g1dK-2HRoqtaR2nhghEFFLDj)
44. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXXIRJnhdA2Y_S90yOa7LPIydIuw1o8v0NoTFk1kPS7gIR4iaWzf8DFWeVaOB7kpTV5XXjbp4XxSUIkYQt5ZvDPO3tAZk3IH99e_-Dvak2ENBgMB9rWlUNPrLU6Uk4WTs-3h1ihP_sTg==)
45. [advancedsciencenews.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGe_pVhfkRqtn9jRIh3NRzqOPvu8_I1E7n_-7B_it0r_toAlBW33SHEIWkkYzUSOwrDXMP_z8A_wqyRP61nChYTL2KOtjPiyh_P9HBC4sRPxUHx_AoRoqqaMeEt9n104T90MNP3igCxpofIi0WgQgL7XugXlJrgst93XFG7q6VnOCh3G8Q8LvyHqPjIPifkpu0wk-FKK9Srtw==)
46. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEe55QvdGjffO1e4V94AYKa9dALs44ofQ44zTcBkQv3LJSy1LyKKfDhR9Cet_6pqlgsVdLncuHMM0TT4CGtPLrhqT-AyxCqtJlZa96kwh0r8NjxqIe2bLKZTg-KsNXL48b6UaYPDZhDE_WlHiSY6csDkSL21lkklT4PFdTRM2t3gNSLzyyAhwc02nOZxEZyZhWdl9bK9R6qzwG4625rRYmiATIXNKEBePvnk8Ape4ba18xBpNhhabY4RURJg==)


## Annotations
Annotation(end_index=2500, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIbhXnCOcCFcGfXwRHN-fSxLWPH7k8Arg9dYuJRcV1RObiI1xaeoLg7cS5MiRnSSmaABWbS1DkQIDDsdgpbkzNrM6btXlb9p77fih3cEBmzmRaA-QDoj8J18HkDtiJD97zKbWwexuyyJWKVIZWL4MgKJ74dyoy6zNnC34GUHpiMaG1TVpI7gc7yJAjMFPvixI3nA-udgC5X095-XKkMYvqbId0YlSuezH6UPBDkClIFw==', start_index=2488)
Annotation(end_index=2500, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgW0IRYCoEBYlyiTnp7pFLtTNxAvSfbTAdbS9qkwS6cGGh2XesP2MfzrYZ5_zcjBdL6bdbuRHWNZpiYW88Xoygv7sD0uf3X3NJjocIonGv6SQEeOJhhJZ9Xelj2vOpiYz75MO7wOCPqAm4zI8GdctRCyCZMg==', start_index=2488)
Annotation(end_index=4710, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEELT7EIbHMndQatlVBbDZfmjd7cgowCz9y29bpjVAQ_bdWvHm6biExTqP0bHi7EUT4rNLtPbnaCOCiFKARYbR-Ydt2f9bv06Hc6VlzZ6J0wnh1WKrDL1gcWCe0wSlXGw==', start_index=4698)
Annotation(end_index=4710, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESrecQHALu_ewsBCrqvP0v7l3BF9GmLPmRC4oPw7vbBqpJbDMGo3oDCWpD2E7h-AIYk8JTLfi1sCbmI6rb-srH0ac_pIwmbOu1jJ5UtuU65CRRavo1PEa3fLD5_jNGyZ_5B8hwSllRUqaIw8xeJMPku_I4xF6SNEpnobSfYapST6q_CbE=', start_index=4698)
Annotation(end_index=4991, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEELT7EIbHMndQatlVBbDZfmjd7cgowCz9y29bpjVAQ_bdWvHm6biExTqP0bHi7EUT4rNLtPbnaCOCiFKARYbR-Ydt2f9bv06Hc6VlzZ6J0wnh1WKrDL1gcWCe0wSlXGw==', start_index=4979)
Annotation(end_index=4991, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESrecQHALu_ewsBCrqvP0v7l3BF9GmLPmRC4oPw7vbBqpJbDMGo3oDCWpD2E7h-AIYk8JTLfi1sCbmI6rb-srH0ac_pIwmbOu1jJ5UtuU65CRRavo1PEa3fLD5_jNGyZ_5B8hwSllRUqaIw8xeJMPku_I4xF6SNEpnobSfYapST6q_CbE=', start_index=4979)
Annotation(end_index=5397, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEELT7EIbHMndQatlVBbDZfmjd7cgowCz9y29bpjVAQ_bdWvHm6biExTqP0bHi7EUT4rNLtPbnaCOCiFKARYbR-Ydt2f9bv06Hc6VlzZ6J0wnh1WKrDL1gcWCe0wSlXGw==', start_index=5385)
Annotation(end_index=5397, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtZjV_hDC_n89iPngrLIeeTVHgt2QC3XsfbenI7CjiteN94AmS6Ae7qoriYuLmUYmhvyfGqQ00uMFKqTHmXPQSTXuhGN2AWQ0nxA4VWSjlRYtdWveKSRtnb6WUlsKEWKgklAGG0e9G', start_index=5385)
Annotation(end_index=5640, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESrecQHALu_ewsBCrqvP0v7l3BF9GmLPmRC4oPw7vbBqpJbDMGo3oDCWpD2E7h-AIYk8JTLfi1sCbmI6rb-srH0ac_pIwmbOu1jJ5UtuU65CRRavo1PEa3fLD5_jNGyZ_5B8hwSllRUqaIw8xeJMPku_I4xF6SNEpnobSfYapST6q_CbE=', start_index=5631)
Annotation(end_index=6777, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1YQuhdGVQpnCKkHBOx-ItBfOUCFc97IoWfwsq_laPdhsRO28F9i4_HjpVKT4jhyaXK76XTq62D7a8Boqz6oU6hg9lXfd9y5woDKjJPzKo7BjlKZES2UdBJaEYxAMnSqQ=', start_index=6765)
Annotation(end_index=6777, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXKROzqIt1mHnDbEVhkEWvzTOGLA7wCrmBi9eHzVst4dAD-CGzn7T1GHcIn7Diis786TWCwG0MKNm9lzK4a_yIOfpM77hO6eOgiThLZX0-eHso9cflXIbnyDJcx6pcPMLtJG0SsKNkcQ==', start_index=6765)
Annotation(end_index=7457, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBqFCuJKKARt0EU73jeIfZW-EKRAnGIhU1jbYj2aydQfOlFzZHHBXh4qk7OII8MY_d8pw0CIYwHw_2GGPKaORHeLm9QXijQWQOmAqv4RxmaYNF2o0kt9FJYoM2etiuGDlBxhipsKW3', start_index=7448)
Annotation(end_index=7685, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfqFXBWDIfu6suGh2vAV7uFGl9dad6VZbHKPYdXyl0EtTRraccPlwyKCTh5I983pegAMsk-6s9Xqw04-t8Rfio2C1fbfymdtKar0IO6Oadls1QpFAJUhnG1GU59yP0Jw==', start_index=7672)
Annotation(end_index=7685, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmUeO0X1s0Yk87arnS2R1hqDGFsXIeDVrbSREfOweTlR0CDH4aRD55FMBFzNSxgCEToWM-qJ_Oj_sFTo8cfSU-fHHmesWRQd461nlYmL3Ge2yNuk7Jvj-7X3AKNty8', start_index=7672)
Annotation(end_index=7868, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfqFXBWDIfu6suGh2vAV7uFGl9dad6VZbHKPYdXyl0EtTRraccPlwyKCTh5I983pegAMsk-6s9Xqw04-t8Rfio2C1fbfymdtKar0IO6Oadls1QpFAJUhnG1GU59yP0Jw==', start_index=7855)
Annotation(end_index=7868, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmUeO0X1s0Yk87arnS2R1hqDGFsXIeDVrbSREfOweTlR0CDH4aRD55FMBFzNSxgCEToWM-qJ_Oj_sFTo8cfSU-fHHmesWRQd461nlYmL3Ge2yNuk7Jvj-7X3AKNty8', start_index=7855)
Annotation(end_index=8602, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4wM17XGr1VvxXQ3s5khg_cJMgix-NOAxRPtShgJCJx1zl1YqIVYN00fQHqmx1sLo5tp1RO3mekX_5M4_sfWiI_g-6NPUpZllqPJxJvHB7tyh08DbMRq8hqbdWdANc2DoKV_QoiZ8OR51Gd8NsTeE8EPkioic=', start_index=8584)
Annotation(end_index=8602, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6trATjtAatKOHStSqqkOfVfKNU1pe0yzIdOAJAdpfI4fMH4kiZSUu53PCrHb-MgU_N-tt3Jl_tvIzG5ZMqMd0Cx6kP7NeQ56UH3Z_zXf15f5V5e7D0g==', start_index=8584)
Annotation(end_index=8602, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpuiSQzrJ_ircKub7VTPvV5IQZ7M0e1ivAuTJAXuQg0hnx91Y4ZlW-yLikBvwuraOBBXIlg_KrohKgsd2YtZi-7SeZgoBlbQlT6KdFrrI4WFUuQ-7zMM60xA8OzQYPYJznSKH0AFJkpDBruUQ3QMH4m8SZ4_5Mt6lCU2pkV0kmPW8d64avRpvN-MQLKZgwB7tL23y0PDjrjOB2OTUHEYvryWTFKM31sk4rFphORLZ22EOH501JNz_IokHlpz3wkvYMiFHqai2wFf2mWy-DR9KweNdvqlFEv5gfdvqMeFVYmFI=', start_index=8584)
Annotation(end_index=9172, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4wM17XGr1VvxXQ3s5khg_cJMgix-NOAxRPtShgJCJx1zl1YqIVYN00fQHqmx1sLo5tp1RO3mekX_5M4_sfWiI_g-6NPUpZllqPJxJvHB7tyh08DbMRq8hqbdWdANc2DoKV_QoiZ8OR51Gd8NsTeE8EPkioic=', start_index=9158)
Annotation(end_index=9172, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHo4Dt66pmMg0YLBCWQuDmVm8gv7HM2Cug7gz6a41-62OWYW_LXidbT7bUY8NikHs0IcWBb9iZwKLG7xU7tuGPBvj40AoNywYEd979f7FUA4azZ5nE5L6T6Ncd1BxyRfmRFlAntv3VI', start_index=9158)
Annotation(end_index=9621, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfWKWguFHRhLzL8GGozZsx8iKO0KZJK0OybVHgTburqI_2OSkgnf3sAvcuxTg62wP7Q-idty8m3FM98Q6R53Vv1XY9gK_XrwCFH54pS8NEOWTXPm3k_kQhiYuKnVvtsOdwVTK8', start_index=9607)
Annotation(end_index=9621, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtHLwO7-3uzY1S5xS7HFygYW0Id_9ZH8tXmVTMRG-4KI1hE0PhEn_MeNUt_5RXfND2jc8c6X5oi37cnci6Stjs4zJhVwQN-enoVYvlLWK62F6Tfb8tQ1kSJQrxW1ZIZA5lyxPKGJQoA6b7LeTkDttWmD9hiO4-', start_index=9607)
Annotation(end_index=10085, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLJo8aWVyaChhOe_QSexobaxLt7n3eblSbc3z5Ou7hjvtvG7JPu36uro_8N6eb06P3w4y-yvZwn9jn241z1daLnPYMSopbyUkVOLiWFk7kRHryZEPANQ==', start_index=10071)
Annotation(end_index=10085, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpuiSQzrJ_ircKub7VTPvV5IQZ7M0e1ivAuTJAXuQg0hnx91Y4ZlW-yLikBvwuraOBBXIlg_KrohKgsd2YtZi-7SeZgoBlbQlT6KdFrrI4WFUuQ-7zMM60xA8OzQYPYJznSKH0AFJkpDBruUQ3QMH4m8SZ4_5Mt6lCU2pkV0kmPW8d64avRpvN-MQLKZgwB7tL23y0PDjrjOB2OTUHEYvryWTFKM31sk4rFphORLZ22EOH501JNz_IokHlpz3wkvYMiFHqai2wFf2mWy-DR9KweNdvqlFEv5gfdvqMeFVYmFI=', start_index=10071)
Annotation(end_index=10702, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzkni7B4iUleXrwFoRObSeFHGNrf4bJ3ju2EMzGobK2_VgSdk3vK7oRvhYeF7912q25K4PEU5-J8-5NwHHMOhpKCuZZb8T-exnN_CoNtFiWpkOKUWHT5xDHi52PZBZk_49EzPlZbtx', start_index=10688)
Annotation(end_index=10702, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF46lguNwB9NnVmXiqHOOBXi_DWHBnazrpA5wmQwoHDikcqZ3ekX_VCFxUDiXP6A8hFBSJl0TjW0pTAuPdrW51QqVa5Nx9Xqjehd6KEk8UDGAY3NyZGn_WlE2VaQonAnKoklQ==', start_index=10688)
Annotation(end_index=10891, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7IMVoOVIWxUmcYrLp12_TYn8q-ogEuQMx1wbT2ZDdnDTHS1tzZxZSK9pIjHCP1OsT-7h8hGKrp_GFsTpwxJAuZ9yZlF2n5Aooq-mZ8Vp-9PrYNwajHuUFywMygizo0UhXIDhOdkdYsuDHbdAc', start_index=10877)
Annotation(end_index=10891, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_bPhYRGh-vwoWPbj1_hcdw-b_erHbL_qiSplZxaNwSzKBYr6PZTGB1C8dvLSaCtSk5GWllQpxj8RCGdQIxt-5a6wtJbT78gQiXfXucRuGdAsFDuat70vdyWLSCK-wCihUg4q2NNfiJbXGV1P21GvQSdKcWNwJ4COI1K73bNxT91KfXDkl07qqVLg-WPnODxSK', start_index=10877)
Annotation(end_index=11211, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAjkTvv1REHomou2nbHJnnzN4I3GydJPgfVNKqrjLxK85OFB9EOL0atZG-KbI4PwPQ13qoy5ws8lesOkYRf7HvMNqINX4xyMiVYbMODUpTXUAAnutpYw==', start_index=11201)
Annotation(end_index=11448, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwYXdxizEcqgmAvWjQF_ge3z5FP-nt_F2HIBexfC5r54ZGDoe_dl2f1dA1-yT1SAC8hct_MENClYkcgrnOCU97AsBibb4_OAKmGy7LFvgwdY2PlDd1EOQGar67BduQEcwQM1mR1K7c_pEOEYMiMoahQgIglmkxEC7bbRZEeeipo82mEmfpybW5S7wKnqe04B_jPZAgRcQFV2kAUNRjcLC1xA==', start_index=11434)
Annotation(end_index=11448, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNZ5oMHnDhvKNts8neMVMPPX3oEI3Ndrx3Hu6DcXXi7Zt_39qfaceYCbtpDfC4KgngKHXrlWnKR0M_0QTMcmU1wdFk0Wsi4xiRL-22K4AkMXZeJUWAm2xFvE33kKZPtY9HEUr2RIqQ7fuNEvnlVpmHIPXlOhWykALdWiwG7BersMuUE8g2OIbIp_u4Ol9HCZONbtv8ROUxVH_meD16q9Sc-saMe1YHm6rrBGiDCXE3CYxhI7zeslEqpOTjv9H0OEVyYhM=', start_index=11434)
Annotation(end_index=12441, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-QucNrSBYw9bOCfTQqXXGszH1S1W8PasVO8WviOqYxtPfeS7nGpGfScDddcv_Dh7C8aIVytYkB5z0vyfCn13NDaZi4DVwnoVcbrC5ZUPihKJP0g3X4jj3FyL3Mk2Xes-y', start_index=12431)
Annotation(end_index=12878, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFf5ewby-8i7au1qrbRY8IB93iQUzRU5dkamOywIkUCnQ0z5nVzKTqVhGqD8P1v1d21udogC_WapAGOw0SvDrEDC-8UFUsVP1eBJvnda1cFhCIXRxKXHUdix5YPtN9oIwNIFLXxi7fGElM62xHa8kkMpzawyJKE0a4AHrU6Qh1ReMjHNVD6tikPDA-KXxLtD58S85g8FGi3u_4=', start_index=12864)
Annotation(end_index=12878, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmj18nUReMvY0GoGYOwbv4ROW2nDF3R4rZyULdyq8uijsXeF6I6dBJEn_AsQOvVC7dkAE-9b2alVEH26zt9fABo2rdx8z8qC8hs_xUwL9uZBsV9aLN-A==', start_index=12864)
Annotation(end_index=13053, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcRGKo7lbA3r-QNvwk9LJwMUMP8cJAXI-MczBY5pqLLwMJKdGKFsdLScnoGhi_LgF9qDKvahlVqkMffD4ICeVOx83k-W8ctVYlRJD8rmT15QihG04W5Q==', start_index=13039)
Annotation(end_index=13053, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuiTB50xJRGQV2CCyE2KGN_gi2mw_RWBozGBICcdPJ5sC51MEB_PUlUmtcZKGktlxbBiol4I3V_uy8f8_OYuyXAlfnx0NPO6DvL8shHvRagAIUwDuZipP2H79eiI5pg13OLeIB3hD2', start_index=13039)
Annotation(end_index=13507, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRTHvzbc-I9J9srsw1_zLE5A-lJFJshhGqJfrVUmrBrZxuxz4iAM1iDcw1qjGNrHQDilgVhyoQ5zmwsDqahip3Ckvm-APxXednELkvWdWgMw4MmiqTOA==', start_index=13493)
Annotation(end_index=13507, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmj18nUReMvY0GoGYOwbv4ROW2nDF3R4rZyULdyq8uijsXeF6I6dBJEn_AsQOvVC7dkAE-9b2alVEH26zt9fABo2rdx8z8qC8hs_xUwL9uZBsV9aLN-A==', start_index=13493)
Annotation(end_index=13840, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFf5ewby-8i7au1qrbRY8IB93iQUzRU5dkamOywIkUCnQ0z5nVzKTqVhGqD8P1v1d21udogC_WapAGOw0SvDrEDC-8UFUsVP1eBJvnda1cFhCIXRxKXHUdix5YPtN9oIwNIFLXxi7fGElM62xHa8kkMpzawyJKE0a4AHrU6Qh1ReMjHNVD6tikPDA-KXxLtD58S85g8FGi3u_4=', start_index=13826)
Annotation(end_index=13840, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmj18nUReMvY0GoGYOwbv4ROW2nDF3R4rZyULdyq8uijsXeF6I6dBJEn_AsQOvVC7dkAE-9b2alVEH26zt9fABo2rdx8z8qC8hs_xUwL9uZBsV9aLN-A==', start_index=13826)
Annotation(end_index=14080, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFug0NNIJz_2INuhPRjNbQmweGNXfnXVegV3zEkTPMAqOmOp6k_A12hJBTZ7dQeDViVoinTp7srowZnGv90VD7L_oBd3CVvRXL629YXK1OOY0IxemgwWS5ys1-G0IrQDQgs-NDL754ezMf54fH0tPcrccFy3-SIF4Wk52MzLBJEMHkEC0YWzxvdVPx8RbuKPo_vDECRGvM1jsIim3F0_9LycUzRiW7SlTQzCa1bJixcyv1wiZluTb5QVqQ8BTYOYwYEkw54YtlePYebvHGf8eHQxJSbfzvUoRbv8xc2HA==', start_index=14066)
Annotation(end_index=14080, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeAs2vLPGineDisvvPzrtrB4y5aPeQ5xRG7h68GXs5yozhMrh4aoM98djoNDmsUdxdaYdPTFYSzjPFKKxCmlIeugOWkQTtF_1mqImOTxMbm8x3FZDGRTxtK9aWf5Ad7kg_BAPIod03v55JpRHUCwxatDtX-lkNirG6EDTBcxxwc47iF6do_x51PDPXuCH6echnnHs=', start_index=14066)
Annotation(end_index=14502, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaSN_TYrkLLZDk5_x7q4NwMoQEl8YQcIxS-vmDT4zJg_1k-O3UnN1FEzt1hx0ieInmaxUN0sRkuXG769f87ppL1hLuvfEhDK_KOjBVblgnfTRwyjiMC2lUOSXgNxAVHr8WDw2dkUhlg1vx4WgkPnrpgwzxwBGPsY7gYKVCHpXiSN2ome5crdqmdzTJU9rX59hVunhDWT2jBzCPOrFpDINe7eCybPAM9S8kZlEx2HMEwyHx', start_index=14492)
Annotation(end_index=14700, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaSN_TYrkLLZDk5_x7q4NwMoQEl8YQcIxS-vmDT4zJg_1k-O3UnN1FEzt1hx0ieInmaxUN0sRkuXG769f87ppL1hLuvfEhDK_KOjBVblgnfTRwyjiMC2lUOSXgNxAVHr8WDw2dkUhlg1vx4WgkPnrpgwzxwBGPsY7gYKVCHpXiSN2ome5crdqmdzTJU9rX59hVunhDWT2jBzCPOrFpDINe7eCybPAM9S8kZlEx2HMEwyHx', start_index=14690)
Annotation(end_index=15485, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLWDSdgex-XihR5fl-DHID9dfqwujXr4lKYAuRW1V7Kf2M-OFsGK_fRxzmJP9lXAVvm7NgbsCo8K0E81N3BShcNcNFOQ5jZfFP11nJbbfmRJ2zACU4fVEjoPjMpNENT-cxOLgV06rGWKH0Ig-_zmsCAunDbYVhsCH7UbVgDGID50b1Wmgmbn6Y3BqS-v9eZrkTriDX2uVWT3R6J83BFZhq5gbYTko8bY1OTQ2bPY4RsY5h2oTse72W', start_index=15471)
Annotation(end_index=15485, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZ6jyWC3nUXQwrcG9TrlWJlwK4UqVdgz_L2KL4qA74PnNNcEkqKPrldBEl9pYGjgcqCo6pjiMe_jWbFLEa5GxAFgBO6f0vmngFeFRGTyglGAIvkDYSO74m0rhMMEMMbErD8k-8IrrX_57_ObVQqkPq9IEbXp5u1FEEp9bCuoyQ4TldCN9mxpGZVD5mKhwvSzh1JT9zV26mSbnN3VrXaxsxIiQHYhvFlXr_qLwsQXtJZIZAIXwTBV7N4CMVdeDy', start_index=15471)
Annotation(end_index=15894, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLWDSdgex-XihR5fl-DHID9dfqwujXr4lKYAuRW1V7Kf2M-OFsGK_fRxzmJP9lXAVvm7NgbsCo8K0E81N3BShcNcNFOQ5jZfFP11nJbbfmRJ2zACU4fVEjoPjMpNENT-cxOLgV06rGWKH0Ig-_zmsCAunDbYVhsCH7UbVgDGID50b1Wmgmbn6Y3BqS-v9eZrkTriDX2uVWT3R6J83BFZhq5gbYTko8bY1OTQ2bPY4RsY5h2oTse72W', start_index=15880)
Annotation(end_index=15894, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZ6jyWC3nUXQwrcG9TrlWJlwK4UqVdgz_L2KL4qA74PnNNcEkqKPrldBEl9pYGjgcqCo6pjiMe_jWbFLEa5GxAFgBO6f0vmngFeFRGTyglGAIvkDYSO74m0rhMMEMMbErD8k-8IrrX_57_ObVQqkPq9IEbXp5u1FEEp9bCuoyQ4TldCN9mxpGZVD5mKhwvSzh1JT9zV26mSbnN3VrXaxsxIiQHYhvFlXr_qLwsQXtJZIZAIXwTBV7N4CMVdeDy', start_index=15880)
Annotation(end_index=16490, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfWKWguFHRhLzL8GGozZsx8iKO0KZJK0OybVHgTburqI_2OSkgnf3sAvcuxTg62wP7Q-idty8m3FM98Q6R53Vv1XY9gK_XrwCFH54pS8NEOWTXPm3k_kQhiYuKnVvtsOdwVTK8', start_index=16472)
Annotation(end_index=16490, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtHLwO7-3uzY1S5xS7HFygYW0Id_9ZH8tXmVTMRG-4KI1hE0PhEn_MeNUt_5RXfND2jc8c6X5oi37cnci6Stjs4zJhVwQN-enoVYvlLWK62F6Tfb8tQ1kSJQrxW1ZIZA5lyxPKGJQoA6b7LeTkDttWmD9hiO4-', start_index=16472)
Annotation(end_index=16490, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTK3SJzWEiuHyN8zNxUvL1hKrzKyhNK8SztVulCoPfiUUYQwuU9-mmXpRNfUvxrPyLxkkmm_zfMcceoeBE_qucb417XMBQlVgfvxIQ4XPqIPBbmppMakf44ILOXD7Tnc7ycH3tMVv5', start_index=16472)
Annotation(end_index=16843, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWO-dhxlUfbi90Ff1c_PZGJ6X5pMPKH3ZbQEFoqrIp2lBZowJXKLrOVyhxacKIUeS1mBQ8Z9Phjit5lO821dbtiZzPtpi4S0Gp-5W_YOnX87oxI31DP8KmpWsMYjxQILpXFWG-yEw2DAt9pl2sepPoWUQCwO44MRTERXLZVbFvcM43NMRI8hxKBZyI2_Om7n8cX-T80ku1H2Dmwa67G8upyTvpAERCmS7HEQMIfeQrPCmZEDJZHpYkiiyeuh5e-fabkR1k0sqmQi00EMiD9rdBcefYZj450qlRXMADKhTIbZ4=', start_index=16829)
Annotation(end_index=16843, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpuiSQzrJ_ircKub7VTPvV5IQZ7M0e1ivAuTJAXuQg0hnx91Y4ZlW-yLikBvwuraOBBXIlg_KrohKgsd2YtZi-7SeZgoBlbQlT6KdFrrI4WFUuQ-7zMM60xA8OzQYPYJznSKH0AFJkpDBruUQ3QMH4m8SZ4_5Mt6lCU2pkV0kmPW8d64avRpvN-MQLKZgwB7tL23y0PDjrjOB2OTUHEYvryWTFKM31sk4rFphORLZ22EOH501JNz_IokHlpz3wkvYMiFHqai2wFf2mWy-DR9KweNdvqlFEv5gfdvqMeFVYmFI=', start_index=16829)
Annotation(end_index=17290, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaSN_TYrkLLZDk5_x7q4NwMoQEl8YQcIxS-vmDT4zJg_1k-O3UnN1FEzt1hx0ieInmaxUN0sRkuXG769f87ppL1hLuvfEhDK_KOjBVblgnfTRwyjiMC2lUOSXgNxAVHr8WDw2dkUhlg1vx4WgkPnrpgwzxwBGPsY7gYKVCHpXiSN2ome5crdqmdzTJU9rX59hVunhDWT2jBzCPOrFpDINe7eCybPAM9S8kZlEx2HMEwyHx', start_index=17276)
Annotation(end_index=17290, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGl_jljUvdBtSdWZFsek3Sa6287fHWVyA7cqIabAHLbIn0FkAzb9XLHBBPvBoUlLcyyi2zUYikihBt_okJndBsNHMXTRWc4F-_v1M6leytEv2ICaSr9-SP7Ndkkxocec5_O7JOW0_bnAeKgVyyD-hgvYsXAQXNvHpqqazxFat8qxtaVyoR5Yny8Y4taKtwQZeDnJbiEou8PrWrFKG5-JNpHTr5gyPLpw3z2nG3OFiyfhxPXwPnDqqgd7TUdhtc=', start_index=17276)
Annotation(end_index=17625, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeZ6SssXd6AvNxVEJfc_Khj0SwIDmSF2NL5CzbWXpzv8JEdMNKrI76iRp1cebvRhWIrrp4ZLCZ-rhC0acZ0GWMMi_gIqKQF-lY7nui7xtBZdVSH87SsbLAiun2lemqMwZgvkCRL5GKfHHiCDIfIAeQVH4izdEYGkc=', start_index=17611)
Annotation(end_index=17625, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpuiSQzrJ_ircKub7VTPvV5IQZ7M0e1ivAuTJAXuQg0hnx91Y4ZlW-yLikBvwuraOBBXIlg_KrohKgsd2YtZi-7SeZgoBlbQlT6KdFrrI4WFUuQ-7zMM60xA8OzQYPYJznSKH0AFJkpDBruUQ3QMH4m8SZ4_5Mt6lCU2pkV0kmPW8d64avRpvN-MQLKZgwB7tL23y0PDjrjOB2OTUHEYvryWTFKM31sk4rFphORLZ22EOH501JNz_IokHlpz3wkvYMiFHqai2wFf2mWy-DR9KweNdvqlFEv5gfdvqMeFVYmFI=', start_index=17611)
Annotation(end_index=19058, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEELT7EIbHMndQatlVBbDZfmjd7cgowCz9y29bpjVAQ_bdWvHm6biExTqP0bHi7EUT4rNLtPbnaCOCiFKARYbR-Ydt2f9bv06Hc6VlzZ6J0wnh1WKrDL1gcWCe0wSlXGw==', start_index=19046)
Annotation(end_index=19058, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESrecQHALu_ewsBCrqvP0v7l3BF9GmLPmRC4oPw7vbBqpJbDMGo3oDCWpD2E7h-AIYk8JTLfi1sCbmI6rb-srH0ac_pIwmbOu1jJ5UtuU65CRRavo1PEa3fLD5_jNGyZ_5B8hwSllRUqaIw8xeJMPku_I4xF6SNEpnobSfYapST6q_CbE=', start_index=19046)
Annotation(end_index=19987, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEELT7EIbHMndQatlVBbDZfmjd7cgowCz9y29bpjVAQ_bdWvHm6biExTqP0bHi7EUT4rNLtPbnaCOCiFKARYbR-Ydt2f9bv06Hc6VlzZ6J0wnh1WKrDL1gcWCe0wSlXGw==', start_index=19975)
Annotation(end_index=19987, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtZjV_hDC_n89iPngrLIeeTVHgt2QC3XsfbenI7CjiteN94AmS6Ae7qoriYuLmUYmhvyfGqQ00uMFKqTHmXPQSTXuhGN2AWQ0nxA4VWSjlRYtdWveKSRtnb6WUlsKEWKgklAGG0e9G', start_index=19975)
Annotation(end_index=21039, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1YQuhdGVQpnCKkHBOx-ItBfOUCFc97IoWfwsq_laPdhsRO28F9i4_HjpVKT4jhyaXK76XTq62D7a8Boqz6oU6hg9lXfd9y5woDKjJPzKo7BjlKZES2UdBJaEYxAMnSqQ=', start_index=21023)
Annotation(end_index=21039, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXKROzqIt1mHnDbEVhkEWvzTOGLA7wCrmBi9eHzVst4dAD-CGzn7T1GHcIn7Diis786TWCwG0MKNm9lzK4a_yIOfpM77hO6eOgiThLZX0-eHso9cflXIbnyDJcx6pcPMLtJG0SsKNkcQ==', start_index=21023)
Annotation(end_index=21039, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmUeO0X1s0Yk87arnS2R1hqDGFsXIeDVrbSREfOweTlR0CDH4aRD55FMBFzNSxgCEToWM-qJ_Oj_sFTo8cfSU-fHHmesWRQd461nlYmL3Ge2yNuk7Jvj-7X3AKNty8', start_index=21023)
Annotation(end_index=22081, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF46lguNwB9NnVmXiqHOOBXi_DWHBnazrpA5wmQwoHDikcqZ3ekX_VCFxUDiXP6A8hFBSJl0TjW0pTAuPdrW51QqVa5Nx9Xqjehd6KEk8UDGAY3NyZGn_WlE2VaQonAnKoklQ==', start_index=22063)
Annotation(end_index=22081, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAjkTvv1REHomou2nbHJnnzN4I3GydJPgfVNKqrjLxK85OFB9EOL0atZG-KbI4PwPQ13qoy5ws8lesOkYRf7HvMNqINX4xyMiVYbMODUpTXUAAnutpYw==', start_index=22063)
Annotation(end_index=22081, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_bPhYRGh-vwoWPbj1_hcdw-b_erHbL_qiSplZxaNwSzKBYr6PZTGB1C8dvLSaCtSk5GWllQpxj8RCGdQIxt-5a6wtJbT78gQiXfXucRuGdAsFDuat70vdyWLSCK-wCihUg4q2NNfiJbXGV1P21GvQSdKcWNwJ4COI1K73bNxT91KfXDkl07qqVLg-WPnODxSK', start_index=22063)
Annotation(end_index=22347, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzkni7B4iUleXrwFoRObSeFHGNrf4bJ3ju2EMzGobK2_VgSdk3vK7oRvhYeF7912q25K4PEU5-J8-5NwHHMOhpKCuZZb8T-exnN_CoNtFiWpkOKUWHT5xDHi52PZBZk_49EzPlZbtx', start_index=22333)
Annotation(end_index=22347, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNZ5oMHnDhvKNts8neMVMPPX3oEI3Ndrx3Hu6DcXXi7Zt_39qfaceYCbtpDfC4KgngKHXrlWnKR0M_0QTMcmU1wdFk0Wsi4xiRL-22K4AkMXZeJUWAm2xFvE33kKZPtY9HEUr2RIqQ7fuNEvnlVpmHIPXlOhWykALdWiwG7BersMuUE8g2OIbIp_u4Ol9HCZONbtv8ROUxVH_meD16q9Sc-saMe1YHm6rrBGiDCXE3CYxhI7zeslEqpOTjv9H0OEVyYhM=', start_index=22333)
Annotation(end_index=22885, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAqilk5gxJvF4wXbtjtcmG_VWr1_Z460U_tlwjD7FKP2Pcs3qxegETrUWUltkrsPTMCVSNwe9LkkNBO3A3TwzlcafC--IoPc_0EWxrbJKJixfbIjq382SvELDhtw==', start_index=22871)
Annotation(end_index=22885, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMCJru6-SPjNtiVzLf72Fx6jCnidLwgssfy1PYqXrz1xgwFALZWwOo_YajgfwUlu7eNaIJp9RayVB474iFmc8PWMUkzKcapHvZT461gUg9APS9wApexTgoDlSFsZCmRgVUw4ejeekN', start_index=22871)
Annotation(end_index=23082, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaSN_TYrkLLZDk5_x7q4NwMoQEl8YQcIxS-vmDT4zJg_1k-O3UnN1FEzt1hx0ieInmaxUN0sRkuXG769f87ppL1hLuvfEhDK_KOjBVblgnfTRwyjiMC2lUOSXgNxAVHr8WDw2dkUhlg1vx4WgkPnrpgwzxwBGPsY7gYKVCHpXiSN2ome5crdqmdzTJU9rX59hVunhDWT2jBzCPOrFpDINe7eCybPAM9S8kZlEx2HMEwyHx', start_index=23068)
Annotation(end_index=23082, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6P3bjmsSY9heMIRrXLBAtSQLYRCOBVnXR3YHbICCxep77Neu8x66Xw1N0Nr94ZNe4MI5sUk6XhGfiz7ajgZPoJTzZ-lm5HzgpRiyxCZF6RyUO2rY5a_f8F0Lu12ibkc_LQpMN0s98Xx4dLsU7K-T1Q085HOPCM7g=', start_index=23068)
Annotation(end_index=23256, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3meIABq72tUfri2oSmjM_vvu0ef7A0TViX6S_H5cf5qcRGF1zmItZ2Vbsi2pfxSfnnw9PXyLEKPiU0Kgn6XHDj8U4g1dK-2HRoqtaR2nhghEFFLDj', start_index=23242)
Annotation(end_index=23256, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRTHvzbc-I9J9srsw1_zLE5A-lJFJshhGqJfrVUmrBrZxuxz4iAM1iDcw1qjGNrHQDilgVhyoQ5zmwsDqahip3Ckvm-APxXednELkvWdWgMw4MmiqTOA==', start_index=23242)
Annotation(end_index=23646, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfWKWguFHRhLzL8GGozZsx8iKO0KZJK0OybVHgTburqI_2OSkgnf3sAvcuxTg62wP7Q-idty8m3FM98Q6R53Vv1XY9gK_XrwCFH54pS8NEOWTXPm3k_kQhiYuKnVvtsOdwVTK8', start_index=23632)
Annotation(end_index=23646, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3meIABq72tUfri2oSmjM_vvu0ef7A0TViX6S_H5cf5qcRGF1zmItZ2Vbsi2pfxSfnnw9PXyLEKPiU0Kgn6XHDj8U4g1dK-2HRoqtaR2nhghEFFLDj', start_index=23632)
Annotation(end_index=24040, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXXIRJnhdA2Y_S90yOa7LPIydIuw1o8v0NoTFk1kPS7gIR4iaWzf8DFWeVaOB7kpTV5XXjbp4XxSUIkYQt5ZvDPO3tAZk3IH99e_-Dvak2ENBgMB9rWlUNPrLU6Uk4WTs-3h1ihP_sTg==', start_index=24026)
Annotation(end_index=24040, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGaSN_TYrkLLZDk5_x7q4NwMoQEl8YQcIxS-vmDT4zJg_1k-O3UnN1FEzt1hx0ieInmaxUN0sRkuXG769f87ppL1hLuvfEhDK_KOjBVblgnfTRwyjiMC2lUOSXgNxAVHr8WDw2dkUhlg1vx4WgkPnrpgwzxwBGPsY7gYKVCHpXiSN2ome5crdqmdzTJU9rX59hVunhDWT2jBzCPOrFpDINe7eCybPAM9S8kZlEx2HMEwyHx', start_index=24026)
Annotation(end_index=24582, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFf5ewby-8i7au1qrbRY8IB93iQUzRU5dkamOywIkUCnQ0z5nVzKTqVhGqD8P1v1d21udogC_WapAGOw0SvDrEDC-8UFUsVP1eBJvnda1cFhCIXRxKXHUdix5YPtN9oIwNIFLXxi7fGElM62xHa8kkMpzawyJKE0a4AHrU6Qh1ReMjHNVD6tikPDA-KXxLtD58S85g8FGi3u_4=', start_index=24564)
Annotation(end_index=24582, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFug0NNIJz_2INuhPRjNbQmweGNXfnXVegV3zEkTPMAqOmOp6k_A12hJBTZ7dQeDViVoinTp7srowZnGv90VD7L_oBd3CVvRXL629YXK1OOY0IxemgwWS5ys1-G0IrQDQgs-NDL754ezMf54fH0tPcrccFy3-SIF4Wk52MzLBJEMHkEC0YWzxvdVPx8RbuKPo_vDECRGvM1jsIim3F0_9LycUzRiW7SlTQzCa1bJixcyv1wiZluTb5QVqQ8BTYOYwYEkw54YtlePYebvHGf8eHQxJSbfzvUoRbv8xc2HA==', start_index=24564)
Annotation(end_index=24582, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmj18nUReMvY0GoGYOwbv4ROW2nDF3R4rZyULdyq8uijsXeF6I6dBJEn_AsQOvVC7dkAE-9b2alVEH26zt9fABo2rdx8z8qC8hs_xUwL9uZBsV9aLN-A==', start_index=24564)
Annotation(end_index=24847, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFug0NNIJz_2INuhPRjNbQmweGNXfnXVegV3zEkTPMAqOmOp6k_A12hJBTZ7dQeDViVoinTp7srowZnGv90VD7L_oBd3CVvRXL629YXK1OOY0IxemgwWS5ys1-G0IrQDQgs-NDL754ezMf54fH0tPcrccFy3-SIF4Wk52MzLBJEMHkEC0YWzxvdVPx8RbuKPo_vDECRGvM1jsIim3F0_9LycUzRiW7SlTQzCa1bJixcyv1wiZluTb5QVqQ8BTYOYwYEkw54YtlePYebvHGf8eHQxJSbfzvUoRbv8xc2HA==', start_index=24833)
Annotation(end_index=24847, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmj18nUReMvY0GoGYOwbv4ROW2nDF3R4rZyULdyq8uijsXeF6I6dBJEn_AsQOvVC7dkAE-9b2alVEH26zt9fABo2rdx8z8qC8hs_xUwL9uZBsV9aLN-A==', start_index=24833)
Annotation(end_index=25364, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLWDSdgex-XihR5fl-DHID9dfqwujXr4lKYAuRW1V7Kf2M-OFsGK_fRxzmJP9lXAVvm7NgbsCo8K0E81N3BShcNcNFOQ5jZfFP11nJbbfmRJ2zACU4fVEjoPjMpNENT-cxOLgV06rGWKH0Ig-_zmsCAunDbYVhsCH7UbVgDGID50b1Wmgmbn6Y3BqS-v9eZrkTriDX2uVWT3R6J83BFZhq5gbYTko8bY1OTQ2bPY4RsY5h2oTse72W', start_index=25346)
Annotation(end_index=25364, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGe_pVhfkRqtn9jRIh3NRzqOPvu8_I1E7n_-7B_it0r_toAlBW33SHEIWkkYzUSOwrDXMP_z8A_wqyRP61nChYTL2KOtjPiyh_P9HBC4sRPxUHx_AoRoqqaMeEt9n104T90MNP3igCxpofIi0WgQgL7XugXlJrgst93XFG7q6VnOCh3G8Q8LvyHqPjIPifkpu0wk-FKK9Srtw==', start_index=25346)
Annotation(end_index=25364, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEe55QvdGjffO1e4V94AYKa9dALs44ofQ44zTcBkQv3LJSy1LyKKfDhR9Cet_6pqlgsVdLncuHMM0TT4CGtPLrhqT-AyxCqtJlZa96kwh0r8NjxqIe2bLKZTg-KsNXL48b6UaYPDZhDE_WlHiSY6csDkSL21lkklT4PFdTRM2t3gNSLzyyAhwc02nOZxEZyZhWdl9bK9R6qzwG4625rRYmiATIXNKEBePvnk8Ape4ba18xBpNhhabY4RURJg==', start_index=25346)
Annotation(end_index=25700, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGl_jljUvdBtSdWZFsek3Sa6287fHWVyA7cqIabAHLbIn0FkAzb9XLHBBPvBoUlLcyyi2zUYikihBt_okJndBsNHMXTRWc4F-_v1M6leytEv2ICaSr9-SP7Ndkkxocec5_O7JOW0_bnAeKgVyyD-hgvYsXAQXNvHpqqazxFat8qxtaVyoR5Yny8Y4taKtwQZeDnJbiEou8PrWrFKG5-JNpHTr5gyPLpw3z2nG3OFiyfhxPXwPnDqqgd7TUdhtc=', start_index=25690)
Annotation(end_index=26047, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWO-dhxlUfbi90Ff1c_PZGJ6X5pMPKH3ZbQEFoqrIp2lBZowJXKLrOVyhxacKIUeS1mBQ8Z9Phjit5lO821dbtiZzPtpi4S0Gp-5W_YOnX87oxI31DP8KmpWsMYjxQILpXFWG-yEw2DAt9pl2sepPoWUQCwO44MRTERXLZVbFvcM43NMRI8hxKBZyI2_Om7n8cX-T80ku1H2Dmwa67G8upyTvpAERCmS7HEQMIfeQrPCmZEDJZHpYkiiyeuh5e-fabkR1k0sqmQi00EMiD9rdBcefYZj450qlRXMADKhTIbZ4=', start_index=26029)
Annotation(end_index=26047, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcRGKo7lbA3r-QNvwk9LJwMUMP8cJAXI-MczBY5pqLLwMJKdGKFsdLScnoGhi_LgF9qDKvahlVqkMffD4ICeVOx83k-W8ctVYlRJD8rmT15QihG04W5Q==', start_index=26029)
Annotation(end_index=26047, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpuiSQzrJ_ircKub7VTPvV5IQZ7M0e1ivAuTJAXuQg0hnx91Y4ZlW-yLikBvwuraOBBXIlg_KrohKgsd2YtZi-7SeZgoBlbQlT6KdFrrI4WFUuQ-7zMM60xA8OzQYPYJznSKH0AFJkpDBruUQ3QMH4m8SZ4_5Mt6lCU2pkV0kmPW8d64avRpvN-MQLKZgwB7tL23y0PDjrjOB2OTUHEYvryWTFKM31sk4rFphORLZ22EOH501JNz_IokHlpz3wkvYMiFHqai2wFf2mWy-DR9KweNdvqlFEv5gfdvqMeFVYmFI=', start_index=26029)

## Sources
