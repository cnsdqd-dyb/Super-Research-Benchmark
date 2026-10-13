# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 396acf99 | **Time:** 334.96s | **Cost:** $0.99388
--------------------------------------------------------------------------------

# Optimization of Logical Depth and Precision in Quantum Computing Simulators via Gate Operation Fidelity

### Key Points
*   **The Fidelity-Depth Scaling Law:** Research indicates a fundamental scaling law where the optimal circuit depth ($D_{opt}$) in digital quantum simulation is proportional to $1/\log(1/F)$, where $F$ is the gate fidelity. This relationship defines the "sweet spot" where the trade-off between algorithmic discretization error (which decreases with depth) and hardware-induced decoherence (which increases with depth) is minimized.
*   **Coherence Time as a Hard Constraint:** While error correction can extend effective lifetimes, physical coherence times ($T_1, T_2$) impose a ceiling on the number of operations possible within a logical cycle. In trapped ion systems, long coherence times allow for deeper circuits despite slower gate speeds, whereas superconducting systems require faster gates to outrun rapid decoherence.
*   **The Precision-Resource Trade-off:** Increasing algorithmic precision (e.g., through finer Trotterization steps) necessitates greater circuit depth. However, without sufficient gate fidelity (typically $>99.9\%$ for fault tolerance), the noise accumulation from additional gates negates the theoretical precision gains.
*   **Logical Layer Abstraction:** In the fault-tolerant regime, optimization shifts from physical gate counts to "logical depth," determined by the code distance required to suppress errors. Higher physical gate fidelity allows for smaller code distances, significantly reducing the qubit overhead and latency for logical operations.

### Executive Summary
The optimization of logical depth and precision in quantum computing simulators is governed by a complex interplay between gate operation fidelity, coherence time, and the chosen error correction scheme. Current research suggests that for any given hardware fidelity, there exists a distinct "fidelity sweet spot" or optimal circuit depth. Pushing beyond this depth introduces more noise than the algorithmic precision it gains. In the Noisy Intermediate-Scale Quantum (NISQ) era, this optimization is often managed via adaptive Trotterization and noise-aware compilation. As the field transitions to Fault-Tolerant Quantum Computing (FTQC), the focus shifts to minimizing the "logical depth factor" by improving physical gate fidelities to lower the necessary overhead of quantum error correction (QEC) codes.

---

## 1. Introduction

The quest to realize practical quantum simulation—using a controllable quantum system to simulate the dynamics of another complex quantum system—rests on the ability to balance two opposing forces: algorithmic precision and physical noise. Digital Quantum Simulation (DQS) approximates continuous time evolution through discrete gate operations (Trotterization). To achieve high precision, the time steps must be infinitesimally small, leading to deep quantum circuits with high gate counts. However, real-world quantum hardware is plagued by finite coherence times and imperfect gate operations.

This report provides an exhaustive analysis of how gate operation fidelity determines the optimization of logical depth and precision. It synthesizes data from superconducting circuits, trapped ions, and neutral atom platforms to establish the theoretical and practical bounds of quantum simulation. We explore the transition from physical circuit depth optimization in the NISQ era to logical depth optimization in the error-corrected era, highlighting the critical role of fidelity in defining the "break-even" points for quantum advantage.

## 2. The Physics of Fidelity and Circuit Depth

The fundamental constraint in quantum circuit design is that the probability of a successful computation decays exponentially with circuit depth in the absence of error correction. Understanding the quantitative relationship between gate fidelity and achievable depth is the first step in optimization.

### 2.1 The Scaling Law of Optimal Depth
Research into digital quantum simulation, particularly for Nuclear Magnetic Resonance (NMR) and molecular dynamics, has identified a critical scaling law. The resolution and precision of a simulation are limited by the competition between the Trotter error (algorithmic artifact) and the decoherence rate (hardware limitation).

At any given value of the average gate fidelity $F$, there is an optimal circuit depth $D_{opt}$ that maximizes the fidelity of the simulation outcome. This relationship is described as:
\[ D_{opt} \sim \frac{1}{\log(1/F)} \]
This scaling arises because the total error $\epsilon_{total}$ is roughly the sum of the algorithmic error $\epsilon_{alg}$ (which scales inversely with depth, e.g., $\sim 1/D$ for first-order Trotterization) and the hardware error $\epsilon_{hw}$ (which scales linearly or exponentially with depth depending on the noise model, $\sim D(1-F)$).

*   **Algorithmic Error:** Decreases as the number of Trotter steps increases (deeper circuit), as the discrete evolution better approximates the continuous Hamiltonian [cite: 1, 2].
*   **Hardware Error:** Increases as the number of gates increases due to the accumulation of gate infidelities and decoherence over time [cite: 1, 3].

The "sweet spot" occurs where the rate of improvement in algorithmic precision is exactly matched by the rate of degradation due to noise. For example, in trapped ion experiments simulating NMR spectra, researchers observed a $1/\sqrt{D}$ scaling in resolution up to a critical depth, after which decoherence dominated [cite: 2, 4].

### 2.2 Gate Fidelity Thresholds
The magnitude of $F$ determines the ceiling for logical complexity.
*   **99.9% (Three Nines):** This is widely considered the entry threshold for effective Quantum Error Correction (QEC). At this level, surface codes can begin to suppress logical errors, though with high overhead. In the NISQ regime, this fidelity allows for circuits with depths in the range of hundreds of operations before the signal-to-noise ratio becomes unmanageable [cite: 5, 6].
*   **99.99% (Four Nines):** Fidelity at this level allows for circuits with hundreds of qubits and significantly greater depth. It reduces the overhead for QEC, allowing for smaller code distances to achieve the same logical error rate [cite: 5].
*   **99.999% (Five Nines):** This is the target for robust fault tolerance, enabling circuits to reach the threshold for thousands of operations and significantly reducing the physical-to-logical qubit ratio [cite: 5, 6].

Recent breakthroughs, such as Oxford's demonstration of single-qubit gate error rates below $1 \times 10^{-7}$ (fidelity > 99.9999%), suggest that physical error rates can be pushed low enough to drastically reduce the infrastructure required for error correction [cite: 6].

### 2.3 Coherence Time Constraints ($T_1$ and $T_2$)
Gate fidelity is intrinsically linked to coherence time. A gate operation takes a finite amount of time $t_g$. The fidelity is limited by the ratio of the gate time to the coherence time ($T_2$).
\[ F \approx 1 - \frac{t_g}{T_2} - \epsilon_{control} \]
where $\epsilon_{control}$ represents coherent control errors (e.g., calibration, crosstalk).

*   **Trapped Ions:** Exhibit extremely long coherence times (seconds to minutes) but have slower gate speeds (microseconds). This allows for deep circuits in the time domain, but the total execution time can be significant [cite: 7, 8].
*   **Superconducting Qubits:** Have short coherence times (microseconds) but very fast gate speeds (nanoseconds). The optimization here focuses on squeezing as many operations as possible into the short coherence window [cite: 6, 9].

The optimization of logical depth requires maximizing the number of gates per coherence time interval. This is why "gate operation fidelity" is a compound metric involving both the precision of the control pulse and the speed of the operation relative to decoherence [cite: 10, 11].

## 3. Digital Quantum Simulation (DQS): The Precision-Depth Trade-off

Digital Quantum Simulation relies on decomposing a unitary evolution operator $U(t) = e^{-iHt}$ into a sequence of elementary gates. The standard approach is Trotterization (product formulas).

### 3.1 Trotterization and Error Bounds
For a Hamiltonian $H = \sum H_k$ consisting of non-commuting terms, the first-order Trotter formula approximates the evolution as:
\[ e^{-iHt} \approx \left( \prod e^{-iH_k \tau} \right)^N \]
where $\tau = t/N$ is the Trotter step size and $N$ is the number of steps (circuit depth).

*   **Discretization Error:** Scales as $O(\tau^2)$ or $O(t^2/N)$. To reduce this error, one must increase $N$ (depth) [cite: 12, 13].
*   **Gate Error:** Scales with the total number of gates, which is proportional to $N$.

Research indicates that DQS is more robust than worst-case bounds suggest. Phenomena such as **quantum localization** can constrain the propagation of errors for local observables, meaning that DQS with comparatively large Trotter steps (shallower circuits) can still retain controlled errors [cite: 13]. This finding is crucial for optimization, as it suggests that simulators can operate with lower logical depth than previously thought necessary.

### 3.2 Adaptive Trotterization
To optimize the trade-off between depth and precision, **adaptive Trotterization** algorithms have been developed. Instead of a fixed step size $\tau$, these algorithms adjust the step size dynamically based on the time-dependence of the Hamiltonian or the local error estimates [cite: 12, 14].

*   **Mechanism:** By using piecewise conserved quantities (e.g., energy or energy variance) to estimate errors, the algorithm maximizes the step size $\delta t$ while keeping the error within a pre-set tolerance.
*   **Benefit:** This minimizes the circuit depth required for a target accuracy, directly addressing the gate imperfection constraints of NISQ devices [cite: 15, 16].
*   **Result:** Adaptive schemes have been shown to outperform fixed-step Trotter algorithms, providing a superior fidelity-depth trade-off [cite: 17].

### 3.3 The Fidelity "Sweet Spot"
Recent studies on transmon qubit systems have revealed a "fidelity sweet spot" that emerges even under strong noise. This sweet spot represents an optimal circuit configuration where the interplay between the specific initial state (e.g., those with favorable symmetry) and the circuit depth yields maximal fidelity [cite: 18, 19]. Machine learning frameworks are now being employed to predict the position of these sweet spots, enabling automated optimization of circuit durations for specific device configurations [cite: 18].

## 4. Quantum Error Correction and Logical Depth

As hardware scales beyond the NISQ era, the definition of "fidelity" and "depth" shifts from physical qubits to logical qubits.

### 4.1 Physical-to-Logical Transition
In Fault-Tolerant Quantum Computing (FTQC), information is encoded in logical qubits consisting of many physical qubits. The **logical error rate** ($P_L$) is suppressed exponentially with the **code distance** ($d$) provided the physical error rate ($p$) is below a threshold ($p_{th}$):
\[ P_L \propto \left( \frac{p}{p_{th}} \right)^{\frac{d+1}{2}} \]

*   **Gate Fidelity as a Determinant:** The physical gate fidelity determines $p$. If $p$ is significantly lower than $p_{th}$ (i.e., high fidelity), a smaller code distance $d$ is required to achieve a target logical error rate [cite: 6, 20].
*   **Overhead Reduction:** A smaller $d$ means fewer physical qubits and, crucially, faster logical gate operations (since logical gate time often scales with $d$). Therefore, improving physical gate fidelity directly optimizes logical depth by reducing the QEC overhead [cite: 21, 22].

### 4.2 Optimal Code Distance
There is a trade-off in choosing the code distance.
*   **Too Small:** Logical errors are not sufficiently suppressed.
*   **Too Large:** The logical cycle time increases, and the number of physical components (and thus potential failure points) increases.
*   **Optimization:** Tools like "MITS" (reverse engineering for STIM) automatically determine the optimal QEC settings (code distance, number of rounds) based on the specific noise model and gate fidelity of the hardware [cite: 20]. This ensures the surface code operates within the hardware's constraints without unnecessary overhead.

### 4.3 Logical Depth and "QuOps"
New metrics are emerging to quantify the power of error-corrected systems.
*   **Logical Depth:** The number of logical operations a computer can perform before a failure. This depends on the logical error rate.
*   **MegaQuOp:** A proposed metric defined as (Number of Logical Qubits) $\times$ (Logical Depth). Achieving a "MegaQuOp" requires high physical fidelities to support the necessary logical depth [cite: 23].
*   **Resource Estimation:** Tools like the Azure Quantum Resource Estimator calculate the "logical depth factor." If the physical gate error rate is high, the system requires more "magic state distillation" factories to produce high-fidelity logical T-gates, which increases the physical footprint and runtime [cite: 24, 25].

## 5. Hardware-Specific Optimization Strategies

Different quantum platforms require distinct optimization strategies based on their specific fidelity-coherence profiles.

### 5.1 Trapped Ions (e.g., IonQ, Quantinuum)
*   **Characteristics:** High connectivity (all-to-all in chains), long coherence times, high gate fidelity ($>99.9\%$), but slow gate speeds [cite: 7, 26].
*   **Optimization:** Because gates are slow, the "depth" in terms of time is the bottleneck. Optimization focuses on reducing the absolute gate count and leveraging all-to-all connectivity to avoid SWAP gates (which are costly in depth and fidelity) [cite: 7].
*   **Fidelity Impact:** High fidelity allows for very deep logical circuits. IonQ reports that 99.99% fidelity enables circuits with hundreds of qubits, while 99.999% pushes this to thousands [cite: 5].

### 5.2 Superconducting Circuits (e.g., IBM, Google)
*   **Characteristics:** Fast gates, fixed coupling (nearest-neighbor), lower coherence times, lower connectivity [cite: 27, 28].
*   **Optimization:** The primary constraint is decoherence. Circuits must be executed quickly. Optimization relies heavily on **SWAP minimization** and **dynamical decoupling** to preserve coherence during idle times [cite: 8, 29].
*   **Fidelity Impact:** Gate fidelity is often limited by crosstalk and leakage. Improving fidelity here involves advanced pulse shaping (e.g., DRAG pulses) and tunable couplers to turn off interactions when not needed [cite: 30, 31].

### 5.3 Geometric and Holonomic Gates
To further optimize fidelity, researchers are exploring **geometric quantum gates**. Unlike dynamic gates, which depend on the precise duration and amplitude of control fields (and are thus susceptible to control errors), geometric gates depend on the global geometric properties of the evolution path [cite: 11, 32].
*   **Nonadiabatic Geometric Quantum Computation (NGQC):** This approach combines the robustness of geometric phases with the speed of nonadiabatic evolution. It has shown promise in enhancing gate fidelity and robustness against local noise, potentially offering a better optimization path for logical depth than standard dynamical gates [cite: 32].

## 6. Algorithmic and Compilation Optimization

Beyond hardware, the optimization of logical depth occurs at the compiler level.

### 6.1 Circuit Compilation and Routing
Mapping a logical circuit to physical hardware requires respecting connectivity constraints.
*   **SWAP Overhead:** On limited-connectivity devices (like superconducting grids), interacting distant qubits requires chains of SWAP gates. Each SWAP adds 3 CNOTs, significantly increasing depth and error.
*   **Optimization:** Heuristic algorithms (e.g., SABRE) and exact solvers are used to find the qubit mapping that minimizes the SWAP count and overall circuit depth [cite: 29, 33].
*   **Fidelity-Aware Routing:** Advanced compilers use calibration data (current gate fidelities) to route signals through the "quietest" (highest fidelity) qubits and links, effectively optimizing the circuit's success probability [cite: 27, 29].

### 6.2 Rewrite Rules and Resynthesis
Compilers like Quartz and TASO use automated theorem proving and cost-based backtracking to optimize circuits.
*   **Rewrite Rules:** Local transformations (e.g., merging adjacent rotation gates) that reduce gate count.
*   **Resynthesis:** Replacing a subcircuit with a functionally equivalent but more efficient version (e.g., one with fewer two-qubit gates). This is critical because two-qubit gates usually have much lower fidelity than single-qubit gates [cite: 34, 35].

### 6.3 Error Mitigation vs. Correction
In the NISQ era, **Quantum Error Mitigation (QEM)** is used to artificially boost precision without full correction.
*   **Zero-Noise Extrapolation (ZNE):** Runs the circuit at different noise levels (by stretching pulses) and extrapolates to the zero-noise limit. This trades runtime (more runs) for precision [cite: 36].
*   **Probabilistic Error Cancellation:** Characterizes the noise model and applies inverse noise maps. This requires high sampling overhead but can recover unbiased expectation values [cite: 29].

## 7. Conclusion

The optimization of logical depth and precision in quantum computing simulators is not a static problem but a dynamic equation solved by maximizing the ratio of **Gate Fidelity** to **Error Accumulation Rate**.

1.  **Fidelity is the Ceiling:** The achievable logical depth is strictly bounded by physical gate fidelity. The scaling law $D_{opt} \sim 1/\log(1/F)$ dictates that incremental improvements in fidelity yield exponential returns in the complexity of simulatable problems.
2.  **Coherence is the Timer:** Coherence time sets the hard limit on physical circuit duration. Optimization strategies must compress the logical operations into this window, favoring faster gates or architectures with longer memory (like ions).
3.  **QEC is the Multiplier:** In the fault-tolerant era, high physical fidelity acts as a lever, reducing the code distance required for logical qubits. This reduction in overhead (fewer physical qubits per logical qubit) is the most effective way to optimize logical depth and computational power.
4.  **Adaptive Precision:** For digital quantum simulation, the rigid Trotter steps of the past are being replaced by adaptive algorithms that sense the local error landscape, adjusting circuit depth dynamically to stay within the "fidelity sweet spot."

Ultimately, the determinant of optimization is the **fidelity-to-overhead ratio**. Whether through better hardware (higher $F$), smarter software (Adaptive Trotterization), or more efficient encoding (LDPC/Surface codes), the goal remains the same: to execute the deepest possible logical circuit before the noise floor obscures the quantum signal.

## 8. References

*   **[cite: 5]** *Plotting the impact of fidelity on circuit depth...* (Reddit/IonQ, 2025).
*   **[cite: 27]** *Validation experiments for our fidelity model...* (arXiv, 2024).
*   **[cite: 6]** *Oxford qubit gate error...* (PostQuantum, 2025).
*   **[cite: 10]** *Quantum error correction is a crucial step...* (Frontiers in Physics, 2022).
*   **[cite: 33]** *Quantum circuit optimization...* (arXiv, 2024).
*   **[cite: 34]** *Quartz: A Quantum Circuit Superoptimizer...* (CMU, 2022).
*   **[cite: 35]** *GUOQ: A Stochastic Algorithm...* (ASPLOS, 2025).
*   **[cite: 7]** *IonQ Forte System...* (IonQ, 2025).
*   **[cite: 11]** *Geometric phases and quantum gates...* (Frontiers of Physics, 2026).
*   **[cite: 8]** *Trapped ion systems...* (Uni-Hannover).
*   **[cite: 32]** *Geometric quantum gates...* (arXiv, 2025).
*   **[cite: 9]** *DiVincenzo prerequisites...* (JKPS, 2018).
*   **[cite: 21]** *To implement fault-tolerant codes...* (SIQEW, 2024).
*   **[cite: 30]** *Optimisation of diamond quantum processors...* (ResearchGate, 2020).
*   **[cite: 1]** *Optimal circuit depth...* (NSF, 2021).
*   **[cite: 18]** *Fidelity sweet spot in transmon qubit rings...* (arXiv, 2025).
*   **[cite: 12]** *Adaptive Trotterization...* (Pure MPG, 2024).
*   **[cite: 13]** *A many-body localization phenomenon...* (PMC, 2019).
*   **[cite: 24]** *The Quantum Platforms Briefing...* (Medium, 2025).
*   **[cite: 25]** *Azure Quantum Resource Estimator...* (Microsoft, 2025).
*   **[cite: 20]** *Optimizing Quantum Error Correction...* (PMC, 2025).
*   **[cite: 22]** *Compiling the surface code...* (arXiv, 2024).
*   **[cite: 37]** *Erasure conversion...* (Jason Chadwick, 2025).
*   **[cite: 26]** *IonQ Aria...* (IonQ).
*   **[cite: 32]** *Geometric phases...* (arXiv, 2025).
*   **[cite: 19]** *Hyperbolic Lattices...* (ResearchGate, 2025).
*   **[cite: 2]** *Simulations of NMR...* (Science Advances, 2025).
*   **[cite: 1]** *Comparison of FID...* (NSF, 2021).
*   **[cite: 14]** *Adaptive Trotterization...* (arXiv, 2023).
*   **[cite: 15]** *Digital quantum simulation relies on Trotterization...* (D-NB, 2024).
*   **[cite: 36]** *Improved Accuracy for Trotter Simulations...* (OSTI).
*   **[cite: 23]** *Introducing Riverlane's QEC Roadmap...* (Riverlane, 2024).
*   **[cite: 29]** *Noise Mitigation Part 2...* (YouTube/Qiskit, 2023).

**Sources:**
1. [nsf.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFn1S0-Tbu_0RzFG-VQyI11fo66xRYfMr0iZZ2bmRSNyZ3W_DbCR-YP7jevfgN--UxaUHGk-I_GZZOKRCroxIPp6N1Kt_wzKIPl8LXdVjPop98O3igbHKVwn9JuJXftTw==)
2. [duke.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCEi8nF6bUcprMtdr0IvRqK0PdYouQZ0TDmSN34PXF-wPYgLYFREpoAkdMC0VUS8jSYc9vVIcLoQjvxRzSfCZyUFKH9hhx0y7wvgg4jm1MMJQ0ZWb5jJG9zPK0zOiAzEIHJvZIe1GAXYlO3W59dQ==)
3. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHizUYC1_wxHpLZ6-yctHNU8V4jo2ETykEhO20Pq4eoT0Vg__YIxd_GAmWdZ1EFAtPUkDYZzfrXbMy_boQHBDzYIHBPOyUe1CTcqhr6SjOiskCUZFQ-TrWdONcnxmANhjFBtWBKUZ5TRPNVHFEGcqYmbcynBpS_J1I9ejJXHoKKyXoyFSH06w1vMyvz6pJzOc6j9fgVA==)
4. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcIOnQzNTnybjSOWhXFDVoiXErWN1O1ZG9khVPARTHNIDG4r31qbeP4I-JmvJdPeeDGK3TKiHCdpiYDWou-f6mHc6GroHUsnEUeoCj02ZRQJhOYdDEPX-f5pg4kelJkHatEjBMtDPoPY-t8_Dpaq0rh5jr9q0fOHMr1sSB-05kSg5xmldH-kmhFFuwrDYsFWEO75acCQ==)
5. [reddit.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6GPPJCbpWqa4MM6TatM6DCGKa3ttW3A7URwajfMlPbP0Ew1ueSZhGeNbPi6JmbJBeq0S9d-G10w0516DrSdVpjxDOl_mE5hou9_5ua6NgGwyiP6cZSX7YyxLhfLVWRfYrUKQLUi_gVi463Qjb3Ew3Kbpjz3_ZF9cqCYXzz_XKc_ZU5XT7ZKTwLnKGQv8Oqmi46NW-ZA==)
6. [postquantum.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEU8P5syFj4DJT_uZh6wEBTYkcPNPgGcRvKEQUr-U8ZXCu6Nl-ZGggX2zr9OHOlKiSJEjwFrNWHOR-fqow9C48roEguGv0YvrKOunbTEN55FxT-0zDmYyvPtGkTF9Wx7chA6WrF6v_HrZ_VtKfRhjyMPypsoSsx)
7. [ionq.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9udxaKMNXYXn1lkc_wSxFDi0xQIqTFLm0Ta4xfhNTno4s1uA76wWkKQLIe1Os3x93Rd5VzACRd4v2ec81Z3eTsJWGsO6mDGoVgUlCsengGuHSQIVRDQJy983Ea6KpBg==)
8. [uni-hannover.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGnuyZItl1P5utrnHitHOxwv2hosJYjq_BvQV6qItl-eLng0-GXG3-R3zxD6f2cOE1pwDpr_wg7eBcvICGvjiyz_soSHmfIC_VC8DvxaMtGGphdUShkbSL1sV7LnFg3q_8csiqU2hBuNs9mNI_5QLAsTgDeNqBpHAY5rJgqvT2sSiEOI-MJlphz3c=)
9. [kaist.ac.kr](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjDLUC4qjEDWXLZ1Tcxe-RW5o59Rj3QFvJUgZyHsxmunIb1L8acpEhgr5doU-jVsY8mkEKLQQkqLj_XdXR6_BYJcL87ud9Gmpvhs6y0TS8asty0nxYIF-qZB-LeWTVqHdfkDYyrdRJAvM0Qg==)
10. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzQOdctY-awUs4vYQWsOPn3osl0y3yqj5b8OZJhfc5NzCl04E_06olPfg68pHk6Hza5nk2z8usMNDfW_4UNZNJrfqDzbApfBFXo8wk3eNDQFjI5D8pvqaT2MAEXJVm0wq5T-nRXadDKBkAhPuvcrg9BPquymwSgyIYSsoDJBnw6p3JkViAz80=)
11. [hep.com.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOvIf0BH4jkrhAy2F2tQ_RgymaF0oU_JEFYetrRKn7ljMsfFAHESGo6bK4kpwVHn_-AkcgZdcoOKz0uKtCuqJuYP89jCVaGGPQVSc1aGQBBZM8TMVeJoOX7skdqx8zWT0jKDj3VOt501YvCaEl16dtQlar7SiNeuoc)
12. [mpg.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfM8uxzoqRIp8t-2Q-JEE2q898YExXlZYhbiPnSqCWYH2-oi1y7heSiMKm6L5Z9uU4kLOZ0T5EeS-r2F1K_1-2FPN84ydboOHyVQljFOpbqphAXgf3myKSktwPefm2H9a0iQDImf5P8L7JgxCtPEGUCZGcURG-exYJGfUyKg9ggPpYPEh9tu74S21H)
13. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIcqMRj-0sHFz6pMKAkiUaA6bQxP3bQ_zu7v12bZeXZfp4PPlH6r9MuTKezfvMqze9f_S0uQHCGWTOXPPPlWXHcH4-fqNjEUMxCVoCLkjCpj9olwkjFs2HP2wVzfradLctlxt9CtY=)
14. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7w-ymH_3xdbTfgCWl83yhCWMy2quF5Z8U1q4G_tYCera1EcxkKhggtMynTeHIDT2L67TwqifjJOfNrVp-uHg-ZRmjEpwSaJKcJ79CsT2yemv4O_Am)
15. [d-nb.info](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFY2VfTopZJn5k0Guyx2Bk5E3aweKnIJ0s4UVhrXBcoSXKnYAVgNwmPdbpaHeP8XmEDX2PHpLvkaX3H3YdHABmICOTmImEcc_0h5f-xiXmkhy5cO8=)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTjD_rtu4J3uyS9am-2zksfKo1A3JtLzZITkOknRO7UskcLr37j7NER4ID180NT9NjBAtJCx_Reg_DL7-vYcUgC1qvHvGL5Fx-Uar9qmTi_bFFURCY75iRqocq6meBOO7yhuShe2nZJPtJyEwORkF61arK1MXpA7cpUmVvMt1ILrQtWQQSXF2CHvO5ZCXOwpyzYbBpfP8p4_QdYsYlO3XR0Ck125hVmk_ICZOusnOCSHdLCl8o3q458HxDQh34gRm-RTjOcD3UfOAEiyDguIOk4ClRCtIf)
17. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6XdBUeWt11wZsQbdsJJbX7hYXFQRvpCksW8gv0peAe_CGtymYnGlEztIHHsNJqEMckWbMp2i7uGLWHBGE2Hq8QV2dFO6uNyrGOWsYx3MPCgXrthMqNqwB)
18. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELOT8c1b_AuYPr5u-3Zjo47wbCmxWJ-tOZw3WPgqIQP07xkn_6_ruLabUP1y1WLZljthnc-OmF7RrfD5kxl03gd_dVCI7dvS1cGnO2XRIqVCjRayKn1BEN)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFv5zPSmKqsvoGa_sljrY8ynZu3nocoiWW2NG5FSCsjSApILzMn7uvnboeIK2VHqXWoVCqdyhs3XaQiUcTLH8bT2EZkDLvGRJ8lJzsmpe8SMF_iusvYNbMpXiJTMVSZ0BwrVKedlQtCIWRHQM578cw5bP3qTfedAb0jny5x-a8Dv5-nP73KtKGksr39KbkvpoVmA5nAixpuiZT0jl6Dzg==)
20. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgGilkzUgB7CI5PiBwVBNZTOEVeRAvV1Wg04l1cnxilyjhoWy-emufGBjJXXvn6B3kWHkomSUxK-cD0HkOCpE11KMqdnU-yY98StRB7U5UA9SY8tNHELPbuz1PtOqXHJtVZ7_huWFZ)
21. [siqew2024.ch](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENWQ7RHDhJYRxZhHtvk6Wbo0dgiWA17COJ2jaLxw1ynvcllr74zrjLr412T3eq62L_ZAglWv0Yc1eDeax_PEmihht-PFO4rnafweQFW5IVkWF1u2kOltl1hb5aZK7yqltBYt7hqbE0IkYeh4aoto5ANvqS4NJ3rBynUSUE3BBwqt4hd-A=)
22. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEC8RP0j2NElFtRPT7DWMeCFf-AKf4WZsWMemOSJBwuzIFXZ8AxS0ppPTfmDKS-3FFsULXWMegDjf55kFYXEpMo73bAeaxguau6DtIQ2xRPOOX1xbSZFYRp)
23. [riverlane.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvmQU76PTCHzMBiHmqMKzNi4spQvXOoFrXAid5rUd2iOoAAByBTMUsdBXRWlDy9_0kZKsLlNNxHBnuKb-p2pBhyK-9zlFl-ZsNZLteYnf-ompWCDTpU6EvzrYxj2svxyZjDuFLGSXlYGWXjq1Q2NyL7IK1lzMSrP3pjLMOYajOmYTm4kFyj3TlIQVR5g==)
24. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN5xLG9-z9IKvBvUU9RPptdfjFuy1xSupT5fMSJvSZ9eXu5Aco9cZtPIE7ab5jugOq26-H2tCCrbPgZqkiQPUezGkhmkT875_0YzfON4i-ZwgcUJnTmUL44QDR7x8K3R-w0AOXpQRzDYsqZJDBEWULAX3Rt7Wixna8l-L8rVoMtuK8xmG-N86-QkTEKNYCi-y5kBzQ)
25. [microsoft.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHO-Nwx_AUHMqnxwQIIeO5PUNAU3gBnCJue1jL1m78Cc7a-B29qaXnlOKy0MxRcUXOfVNsBUVOLSWn8pVgZ_sOLz9pC3d61EyExOopHyZntBNdN7Zx5VPyHVUFL-vkLJO1r83m5ycwJLy1olVhNLrBjZqfJkUPQfaUUkNy77Ne17cY=)
26. [ionq.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWMTLM0yDrnqLhMJkqFprVSDNaNAkzZFXQAOOYelVaj9LbIEuzBoNYvEa0QW0d6n0NlMiO9MLh2fZmTvw3efxytEv_UDtFNE9YG3FVhYRyVPfiuHGW8fd_uCUr8frV)
27. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2BK-IEDS6eLsgvrulr8atiQVpKPl2suy-F0UTXWcZFoyMCwq5YOcC8wpeOAmJh2bJdFg6iH0zfeduD6EiT1VpEuzK2RRF5AW4VOH-q8rWLGwIDCBX-qFy)
28. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEi75lFWmBJQOeRm248U2TDFKaSQonYtAbVj_Wm1PHuwFAfDKXayuIdu06IWGzfneh_iOzsB70KmiRjzkaOvwtrvYxIjwT5KdiyUfPzTV2Ui4xmMO7WIGd9leePNLeKY0pr2aY2Ma_Lk3TlSxxamyLsmfurhpZj8hETsI17hwH2rqUIe9osT3u0QVCuiKWTXNTB97esLl8pxTkI9yWG7aUAM309Hiq_GMcEo6l8J1seL5ciXpYQBUdSwSAuorAU)
29. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYqZ58xVg_aVxKd-Y71GlAdivRqfoaXrS2-TauhlPm4gOc-p7cdybOL0v5J3XmgNMdxpTMBzTsVK-GPzpGmwEjlHDPhE5COdIScVk63wf9y-7EvgCoDBjo43MWbVwEuso=)
30. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZI229xdCkv4D0B-gWxPDcrvbrLcVt4V1XzBA6t-2RKTdj1RpLPype9RKODN2d1gyAnaqbpJzj_LgEHXr-DilQCTqTA3y0aweVRx-QmHjpUAArI0t0dF9fBOAC8f0DsXSRuOpO9ivuMxYXmocARtPBW29yAuPjnhZRcOQzXVunwqJTg1bF57lSU5TSxl8nxBzkfw==)
31. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHo-TG6h-PKi6e5r9D_dv1Q6GDWq413smc1tpSpDz4CSnLNE9pAGJ-5YKSrFT9l0GhLYZgg28s6eTs2xGdIscFFXj76w8ElrS3aCxylzepVpzPE-1-6Akyldhpwjvu1oQ965XC962iyZsYBJ78EOfKpzO_YVjQRAxhUIg1aHjdosmesUO6e6de-bgq4cOYJoeU66eid8UW8AGFR5QrSujsldufxCnlktMEIv3VXEA_sPZhuDw==)
32. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyU56C0ecGZ78rso77-7og6-5Qwc25M42CKRDJZ-4hotyRlPRhofnkDmp808gWVY_CBl7UVdC8kHnTxrwufqwS5snFd_LJG3iwhuE_X1NXYhCiy34I)
33. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYTiAJib1HqGIEM9wPweJiMpl71gPzy4qIjqvBSk4wpYfbSG-hnY6edJoQMWDzZ1zPnTzXTlBP1YwpSF_cbDF9TVXkjAEuP54Csaaa7tkInd8-jsG_)
34. [cmu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTYX9FvH_rtCguUYKJYUZPL9BcJbkCXveddEKqbWGrl9Q6Pbae16jaWwI8_-THzXdDUj1YeDvSsPt5pQQoe0WJznerRUnzzXiz8Un7h7w24N20xMR-K9qoeSnxgdI15oxAk61bU1gtWmwQHOlAPQ==)
35. [wisc.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdBffSQZ8PHrI9Tqm6zDOnhJdqZfWVJLZZIg2xms9GErWLO-19K66DGHv64234MKK8RcXDYPB_GyGB9k6s-livhbH__IkdYP3Gt_Du2RKPIR1yYS7XwqFRCN3h-2lAbi4lhqkKxJdo)
36. [osti.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPemyV18QUmOZEbG04xahTWXL8XUUJdQyPf9msCI0XOIxjnuSevD6x94FRayAMydealcwht1-1A2k4YOqbb25Jt1Y8RYBbZGoeZ8zhxodMMlRZwUVuIvwjaVFh7TpjUSqy4HF17g==)
37. [jason-chadwick.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE81bp6bFxb_nPi4UB6yUvLOcm1vxEiQbSlJXCV7te198C0a3FYzGxaZj4WjwO0owk_w1JSi0hp3j_uHd1EEkM_wWt3wIVnwzBU7jafWlztcu6dv2gBgVde6AYvv3YaP4C9LLJ9V1UBy_TjD0fLpRnSOGlTydnqkHcmx4A=)


## Annotations
Annotation(end_index=5095, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFn1S0-Tbu_0RzFG-VQyI11fo66xRYfMr0iZZ2bmRSNyZ3W_DbCR-YP7jevfgN--UxaUHGk-I_GZZOKRCroxIPp6N1Kt_wzKIPl8LXdVjPop98O3igbHKVwn9JuJXftTw==', start_index=5083)
Annotation(end_index=5095, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCEi8nF6bUcprMtdr0IvRqK0PdYouQZ0TDmSN34PXF-wPYgLYFREpoAkdMC0VUS8jSYc9vVIcLoQjvxRzSfCZyUFKH9hhx0y7wvgg4jm1MMJQ0ZWb5jJG9zPK0zOiAzEIHJvZIe1GAXYlO3W59dQ==', start_index=5083)
Annotation(end_index=5247, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFn1S0-Tbu_0RzFG-VQyI11fo66xRYfMr0iZZ2bmRSNyZ3W_DbCR-YP7jevfgN--UxaUHGk-I_GZZOKRCroxIPp6N1Kt_wzKIPl8LXdVjPop98O3igbHKVwn9JuJXftTw==', start_index=5235)
Annotation(end_index=5247, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHizUYC1_wxHpLZ6-yctHNU8V4jo2ETykEhO20Pq4eoT0Vg__YIxd_GAmWdZ1EFAtPUkDYZzfrXbMy_boQHBDzYIHBPOyUe1CTcqhr6SjOiskCUZFQ-TrWdONcnxmANhjFBtWBKUZ5TRPNVHFEGcqYmbcynBpS_J1I9ejJXHoKKyXoyFSH06w1vMyvz6pJzOc6j9fgVA==', start_index=5235)
Annotation(end_index=5581, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCEi8nF6bUcprMtdr0IvRqK0PdYouQZ0TDmSN34PXF-wPYgLYFREpoAkdMC0VUS8jSYc9vVIcLoQjvxRzSfCZyUFKH9hhx0y7wvgg4jm1MMJQ0ZWb5jJG9zPK0zOiAzEIHJvZIe1GAXYlO3W59dQ==', start_index=5569)
Annotation(end_index=5581, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcIOnQzNTnybjSOWhXFDVoiXErWN1O1ZG9khVPARTHNIDG4r31qbeP4I-JmvJdPeeDGK3TKiHCdpiYDWou-f6mHc6GroHUsnEUeoCj02ZRQJhOYdDEPX-f5pg4kelJkHatEjBMtDPoPY-t8_Dpaq0rh5jr9q0fOHMr1sSB-05kSg5xmldH-kmhFFuwrDYsFWEO75acCQ==', start_index=5569)
Annotation(end_index=6071, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6GPPJCbpWqa4MM6TatM6DCGKa3ttW3A7URwajfMlPbP0Ew1ueSZhGeNbPi6JmbJBeq0S9d-G10w0516DrSdVpjxDOl_mE5hou9_5ua6NgGwyiP6cZSX7YyxLhfLVWRfYrUKQLUi_gVi463Qjb3Ew3Kbpjz3_ZF9cqCYXzz_XKc_ZU5XT7ZKTwLnKGQv8Oqmi46NW-ZA==', start_index=6059)
Annotation(end_index=6071, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEU8P5syFj4DJT_uZh6wEBTYkcPNPgGcRvKEQUr-U8ZXCu6Nl-ZGggX2zr9OHOlKiSJEjwFrNWHOR-fqow9C48roEguGv0YvrKOunbTEN55FxT-0zDmYyvPtGkTF9Wx7chA6WrF6v_HrZ_VtKfRhjyMPypsoSsx', start_index=6059)
Annotation(end_index=6319, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6GPPJCbpWqa4MM6TatM6DCGKa3ttW3A7URwajfMlPbP0Ew1ueSZhGeNbPi6JmbJBeq0S9d-G10w0516DrSdVpjxDOl_mE5hou9_5ua6NgGwyiP6cZSX7YyxLhfLVWRfYrUKQLUi_gVi463Qjb3Ew3Kbpjz3_ZF9cqCYXzz_XKc_ZU5XT7ZKTwLnKGQv8Oqmi46NW-ZA==', start_index=6310)
Annotation(end_index=6542, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6GPPJCbpWqa4MM6TatM6DCGKa3ttW3A7URwajfMlPbP0Ew1ueSZhGeNbPi6JmbJBeq0S9d-G10w0516DrSdVpjxDOl_mE5hou9_5ua6NgGwyiP6cZSX7YyxLhfLVWRfYrUKQLUi_gVi463Qjb3Ew3Kbpjz3_ZF9cqCYXzz_XKc_ZU5XT7ZKTwLnKGQv8Oqmi46NW-ZA==', start_index=6530)
Annotation(end_index=6542, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEU8P5syFj4DJT_uZh6wEBTYkcPNPgGcRvKEQUr-U8ZXCu6Nl-ZGggX2zr9OHOlKiSJEjwFrNWHOR-fqow9C48roEguGv0YvrKOunbTEN55FxT-0zDmYyvPtGkTF9Wx7chA6WrF6v_HrZ_VtKfRhjyMPypsoSsx', start_index=6530)
Annotation(end_index=6818, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEU8P5syFj4DJT_uZh6wEBTYkcPNPgGcRvKEQUr-U8ZXCu6Nl-ZGggX2zr9OHOlKiSJEjwFrNWHOR-fqow9C48roEguGv0YvrKOunbTEN55FxT-0zDmYyvPtGkTF9Wx7chA6WrF6v_HrZ_VtKfRhjyMPypsoSsx', start_index=6809)
Annotation(end_index=7458, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGnuyZItl1P5utrnHitHOxwv2hosJYjq_BvQV6qItl-eLng0-GXG3-R3zxD6f2cOE1pwDpr_wg7eBcvICGvjiyz_soSHmfIC_VC8DvxaMtGGphdUShkbSL1sV7LnFg3q_8csiqU2hBuNs9mNI_5QLAsTgDeNqBpHAY5rJgqvT2sSiEOI-MJlphz3c=', start_index=7446)
Annotation(end_index=7458, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9udxaKMNXYXn1lkc_wSxFDi0xQIqTFLm0Ta4xfhNTno4s1uA76wWkKQLIe1Os3x93Rd5VzACRd4v2ec81Z3eTsJWGsO6mDGoVgUlCsengGuHSQIVRDQJy983Ea6KpBg==', start_index=7446)
Annotation(end_index=7693, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEU8P5syFj4DJT_uZh6wEBTYkcPNPgGcRvKEQUr-U8ZXCu6Nl-ZGggX2zr9OHOlKiSJEjwFrNWHOR-fqow9C48roEguGv0YvrKOunbTEN55FxT-0zDmYyvPtGkTF9Wx7chA6WrF6v_HrZ_VtKfRhjyMPypsoSsx', start_index=7681)
Annotation(end_index=7693, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjDLUC4qjEDWXLZ1Tcxe-RW5o59Rj3QFvJUgZyHsxmunIb1L8acpEhgr5doU-jVsY8mkEKLQQkqLj_XdXR6_BYJcL87ud9Gmpvhs6y0TS8asty0nxYIF-qZB-LeWTVqHdfkDYyrdRJAvM0Qg==', start_index=7681)
Annotation(end_index=7977, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzQOdctY-awUs4vYQWsOPn3osl0y3yqj5b8OZJhfc5NzCl04E_06olPfg68pHk6Hza5nk2z8usMNDfW_4UNZNJrfqDzbApfBFXo8wk3eNDQFjI5D8pvqaT2MAEXJVm0wq5T-nRXadDKBkAhPuvcrg9BPquymwSgyIYSsoDJBnw6p3JkViAz80=', start_index=7963)
Annotation(end_index=7977, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOvIf0BH4jkrhAy2F2tQ_RgymaF0oU_JEFYetrRKn7ljMsfFAHESGo6bK4kpwVHn_-AkcgZdcoOKz0uKtCuqJuYP89jCVaGGPQVSc1aGQBBZM8TMVeJoOX7skdqx8zWT0jKDj3VOt501YvCaEl16dtQlar7SiNeuoc', start_index=7963)
Annotation(end_index=8703, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIcqMRj-0sHFz6pMKAkiUaA6bQxP3bQ_zu7v12bZeXZfp4PPlH6r9MuTKezfvMqze9f_S0uQHCGWTOXPPPlWXHcH4-fqNjEUMxCVoCLkjCpj9olwkjFs2HP2wVzfradLctlxt9CtY=', start_index=8689)
Annotation(end_index=8703, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfM8uxzoqRIp8t-2Q-JEE2q898YExXlZYhbiPnSqCWYH2-oi1y7heSiMKm6L5Z9uU4kLOZ0T5EeS-r2F1K_1-2FPN84ydboOHyVQljFOpbqphAXgf3myKSktwPefm2H9a0iQDImf5P8L7JgxCtPEGUCZGcURG-exYJGfUyKg9ggPpYPEh9tu74S21H', start_index=8689)
Annotation(end_index=9098, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIcqMRj-0sHFz6pMKAkiUaA6bQxP3bQ_zu7v12bZeXZfp4PPlH6r9MuTKezfvMqze9f_S0uQHCGWTOXPPPlWXHcH4-fqNjEUMxCVoCLkjCpj9olwkjFs2HP2wVzfradLctlxt9CtY=', start_index=9088)
Annotation(end_index=9571, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7w-ymH_3xdbTfgCWl83yhCWMy2quF5Z8U1q4G_tYCera1EcxkKhggtMynTeHIDT2L67TwqifjJOfNrVp-uHg-ZRmjEpwSaJKcJ79CsT2yemv4O_Am', start_index=9557)
Annotation(end_index=9571, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfM8uxzoqRIp8t-2Q-JEE2q898YExXlZYhbiPnSqCWYH2-oi1y7heSiMKm6L5Z9uU4kLOZ0T5EeS-r2F1K_1-2FPN84ydboOHyVQljFOpbqphAXgf3myKSktwPefm2H9a0iQDImf5P8L7JgxCtPEGUCZGcURG-exYJGfUyKg9ggPpYPEh9tu74S21H', start_index=9557)
Annotation(end_index=9954, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFY2VfTopZJn5k0Guyx2Bk5E3aweKnIJ0s4UVhrXBcoSXKnYAVgNwmPdbpaHeP8XmEDX2PHpLvkaX3H3YdHABmICOTmImEcc_0h5f-xiXmkhy5cO8=', start_index=9940)
Annotation(end_index=9954, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTjD_rtu4J3uyS9am-2zksfKo1A3JtLzZITkOknRO7UskcLr37j7NER4ID180NT9NjBAtJCx_Reg_DL7-vYcUgC1qvHvGL5Fx-Uar9qmTi_bFFURCY75iRqocq6meBOO7yhuShe2nZJPtJyEwORkF61arK1MXpA7cpUmVvMt1ILrQtWQQSXF2CHvO5ZCXOwpyzYbBpfP8p4_QdYsYlO3XR0Ck125hVmk_ICZOusnOCSHdLCl8o3q458HxDQh34gRm-RTjOcD3UfOAEiyDguIOk4ClRCtIf', start_index=9940)
Annotation(end_index=10106, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6XdBUeWt11wZsQbdsJJbX7hYXFQRvpCksW8gv0peAe_CGtymYnGlEztIHHsNJqEMckWbMp2i7uGLWHBGE2Hq8QV2dFO6uNyrGOWsYx3MPCgXrthMqNqwB', start_index=10096)
Annotation(end_index=10473, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELOT8c1b_AuYPr5u-3Zjo47wbCmxWJ-tOZw3WPgqIQP07xkn_6_ruLabUP1y1WLZljthnc-OmF7RrfD5kxl03gd_dVCI7dvS1cGnO2XRIqVCjRayKn1BEN', start_index=10459)
Annotation(end_index=10473, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFv5zPSmKqsvoGa_sljrY8ynZu3nocoiWW2NG5FSCsjSApILzMn7uvnboeIK2VHqXWoVCqdyhs3XaQiUcTLH8bT2EZkDLvGRJ8lJzsmpe8SMF_iusvYNbMpXiJTMVSZ0BwrVKedlQtCIWRHQM578cw5bP3qTfedAb0jny5x-a8Dv5-nP73KtKGksr39KbkvpoVmA5nAixpuiZT0jl6Dzg==', start_index=10459)
Annotation(end_index=10670, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELOT8c1b_AuYPr5u-3Zjo47wbCmxWJ-tOZw3WPgqIQP07xkn_6_ruLabUP1y1WLZljthnc-OmF7RrfD5kxl03gd_dVCI7dvS1cGnO2XRIqVCjRayKn1BEN', start_index=10660)
Annotation(end_index=11489, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEU8P5syFj4DJT_uZh6wEBTYkcPNPgGcRvKEQUr-U8ZXCu6Nl-ZGggX2zr9OHOlKiSJEjwFrNWHOR-fqow9C48roEguGv0YvrKOunbTEN55FxT-0zDmYyvPtGkTF9Wx7chA6WrF6v_HrZ_VtKfRhjyMPypsoSsx', start_index=11476)
Annotation(end_index=11489, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgGilkzUgB7CI5PiBwVBNZTOEVeRAvV1Wg04l1cnxilyjhoWy-emufGBjJXXvn6B3kWHkomSUxK-cD0HkOCpE11KMqdnU-yY98StRB7U5UA9SY8tNHELPbuz1PtOqXHJtVZ7_huWFZ', start_index=11476)
Annotation(end_index=11777, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEC8RP0j2NElFtRPT7DWMeCFf-AKf4WZsWMemOSJBwuzIFXZ8AxS0ppPTfmDKS-3FFsULXWMegDjf55kFYXEpMo73bAeaxguau6DtIQ2xRPOOX1xbSZFYRp', start_index=11763)
Annotation(end_index=11777, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENWQ7RHDhJYRxZhHtvk6Wbo0dgiWA17COJ2jaLxw1ynvcllr74zrjLr412T3eq62L_ZAglWv0Yc1eDeax_PEmihht-PFO4rnafweQFW5IVkWF1u2kOltl1hb5aZK7yqltBYt7hqbE0IkYeh4aoto5ANvqS4NJ3rBynUSUE3BBwqt4hd-A=', start_index=11763)
Annotation(end_index=12299, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgGilkzUgB7CI5PiBwVBNZTOEVeRAvV1Wg04l1cnxilyjhoWy-emufGBjJXXvn6B3kWHkomSUxK-cD0HkOCpE11KMqdnU-yY98StRB7U5UA9SY8tNHELPbuz1PtOqXHJtVZ7_huWFZ', start_index=12289)
Annotation(end_index=12857, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvmQU76PTCHzMBiHmqMKzNi4spQvXOoFrXAid5rUd2iOoAAByBTMUsdBXRWlDy9_0kZKsLlNNxHBnuKb-p2pBhyK-9zlFl-ZsNZLteYnf-ompWCDTpU6EvzrYxj2svxyZjDuFLGSXlYGWXjq1Q2NyL7IK1lzMSrP3pjLMOYajOmYTm4kFyj3TlIQVR5g==', start_index=12847)
Annotation(end_index=13184, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN5xLG9-z9IKvBvUU9RPptdfjFuy1xSupT5fMSJvSZ9eXu5Aco9cZtPIE7ab5jugOq26-H2tCCrbPgZqkiQPUezGkhmkT875_0YzfON4i-ZwgcUJnTmUL44QDR7x8K3R-w0AOXpQRzDYsqZJDBEWULAX3Rt7Wixna8l-L8rVoMtuK8xmG-N86-QkTEKNYCi-y5kBzQ', start_index=13170)
Annotation(end_index=13184, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHO-Nwx_AUHMqnxwQIIeO5PUNAU3gBnCJue1jL1m78Cc7a-B29qaXnlOKy0MxRcUXOfVNsBUVOLSWn8pVgZ_sOLz9pC3d61EyExOopHyZntBNdN7Zx5VPyHVUFL-vkLJO1r83m5ycwJLy1olVhNLrBjZqfJkUPQfaUUkNy77Ne17cY=', start_index=13170)
Annotation(end_index=13560, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWMTLM0yDrnqLhMJkqFprVSDNaNAkzZFXQAOOYelVaj9LbIEuzBoNYvEa0QW0d6n0NlMiO9MLh2fZmTvw3efxytEv_UDtFNE9YG3FVhYRyVPfiuHGW8fd_uCUr8frV', start_index=13547)
Annotation(end_index=13560, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9udxaKMNXYXn1lkc_wSxFDi0xQIqTFLm0Ta4xfhNTno4s1uA76wWkKQLIe1Os3x93Rd5VzACRd4v2ec81Z3eTsJWGsO6mDGoVgUlCsengGuHSQIVRDQJy983Ea6KpBg==', start_index=13547)
Annotation(end_index=13822, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9udxaKMNXYXn1lkc_wSxFDi0xQIqTFLm0Ta4xfhNTno4s1uA76wWkKQLIe1Os3x93Rd5VzACRd4v2ec81Z3eTsJWGsO6mDGoVgUlCsengGuHSQIVRDQJy983Ea6KpBg==', start_index=13813)
Annotation(end_index=14026, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6GPPJCbpWqa4MM6TatM6DCGKa3ttW3A7URwajfMlPbP0Ew1ueSZhGeNbPi6JmbJBeq0S9d-G10w0516DrSdVpjxDOl_mE5hou9_5ua6NgGwyiP6cZSX7YyxLhfLVWRfYrUKQLUi_gVi463Qjb3Ew3Kbpjz3_ZF9cqCYXzz_XKc_ZU5XT7ZKTwLnKGQv8Oqmi46NW-ZA==', start_index=14017)
Annotation(end_index=14210, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEi75lFWmBJQOeRm248U2TDFKaSQonYtAbVj_Wm1PHuwFAfDKXayuIdu06IWGzfneh_iOzsB70KmiRjzkaOvwtrvYxIjwT5KdiyUfPzTV2Ui4xmMO7WIGd9leePNLeKY0pr2aY2Ma_Lk3TlSxxamyLsmfurhpZj8hETsI17hwH2rqUIe9osT3u0QVCuiKWTXNTB97esLl8pxTkI9yWG7aUAM309Hiq_GMcEo6l8J1seL5ciXpYQBUdSwSAuorAU', start_index=14196)
Annotation(end_index=14210, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2BK-IEDS6eLsgvrulr8atiQVpKPl2suy-F0UTXWcZFoyMCwq5YOcC8wpeOAmJh2bJdFg6iH0zfeduD6EiT1VpEuzK2RRF5AW4VOH-q8rWLGwIDCBX-qFy', start_index=14196)
Annotation(end_index=14443, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGnuyZItl1P5utrnHitHOxwv2hosJYjq_BvQV6qItl-eLng0-GXG3-R3zxD6f2cOE1pwDpr_wg7eBcvICGvjiyz_soSHmfIC_VC8DvxaMtGGphdUShkbSL1sV7LnFg3q_8csiqU2hBuNs9mNI_5QLAsTgDeNqBpHAY5rJgqvT2sSiEOI-MJlphz3c=', start_index=14430)
Annotation(end_index=14443, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYqZ58xVg_aVxKd-Y71GlAdivRqfoaXrS2-TauhlPm4gOc-p7cdybOL0v5J3XmgNMdxpTMBzTsVK-GPzpGmwEjlHDPhE5COdIScVk63wf9y-7EvgCoDBjo43MWbVwEuso=', start_index=14430)
Annotation(end_index=14679, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZI229xdCkv4D0B-gWxPDcrvbrLcVt4V1XzBA6t-2RKTdj1RpLPype9RKODN2d1gyAnaqbpJzj_LgEHXr-DilQCTqTA3y0aweVRx-QmHjpUAArI0t0dF9fBOAC8f0DsXSRuOpO9ivuMxYXmocARtPBW29yAuPjnhZRcOQzXVunwqJTg1bF57lSU5TSxl8nxBzkfw==', start_index=14665)
Annotation(end_index=14679, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHo-TG6h-PKi6e5r9D_dv1Q6GDWq413smc1tpSpDz4CSnLNE9pAGJ-5YKSrFT9l0GhLYZgg28s6eTs2xGdIscFFXj76w8ElrS3aCxylzepVpzPE-1-6Akyldhpwjvu1oQ965XC962iyZsYBJ78EOfKpzO_YVjQRAxhUIg1aHjdosmesUO6e6de-bgq4cOYJoeU66eid8UW8AGFR5QrSujsldufxCnlktMEIv3VXEA_sPZhuDw==', start_index=14665)
Annotation(end_index=15036, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOvIf0BH4jkrhAy2F2tQ_RgymaF0oU_JEFYetrRKn7ljMsfFAHESGo6bK4kpwVHn_-AkcgZdcoOKz0uKtCuqJuYP89jCVaGGPQVSc1aGQBBZM8TMVeJoOX7skdqx8zWT0jKDj3VOt501YvCaEl16dtQlar7SiNeuoc', start_index=15022)
Annotation(end_index=15036, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyU56C0ecGZ78rso77-7og6-5Qwc25M42CKRDJZ-4hotyRlPRhofnkDmp808gWVY_CBl7UVdC8kHnTxrwufqwS5snFd_LJG3iwhuE_X1NXYhCiy34I', start_index=15022)
Annotation(end_index=15387, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyU56C0ecGZ78rso77-7og6-5Qwc25M42CKRDJZ-4hotyRlPRhofnkDmp808gWVY_CBl7UVdC8kHnTxrwufqwS5snFd_LJG3iwhuE_X1NXYhCiy34I', start_index=15377)
Annotation(end_index=16042, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYTiAJib1HqGIEM9wPweJiMpl71gPzy4qIjqvBSk4wpYfbSG-hnY6edJoQMWDzZ1zPnTzXTlBP1YwpSF_cbDF9TVXkjAEuP54Csaaa7tkInd8-jsG_', start_index=16028)
Annotation(end_index=16042, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYqZ58xVg_aVxKd-Y71GlAdivRqfoaXrS2-TauhlPm4gOc-p7cdybOL0v5J3XmgNMdxpTMBzTsVK-GPzpGmwEjlHDPhE5COdIScVk63wf9y-7EvgCoDBjo43MWbVwEuso=', start_index=16028)
Annotation(end_index=16290, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2BK-IEDS6eLsgvrulr8atiQVpKPl2suy-F0UTXWcZFoyMCwq5YOcC8wpeOAmJh2bJdFg6iH0zfeduD6EiT1VpEuzK2RRF5AW4VOH-q8rWLGwIDCBX-qFy', start_index=16276)
Annotation(end_index=16290, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYqZ58xVg_aVxKd-Y71GlAdivRqfoaXrS2-TauhlPm4gOc-p7cdybOL0v5J3XmgNMdxpTMBzTsVK-GPzpGmwEjlHDPhE5COdIScVk63wf9y-7EvgCoDBjo43MWbVwEuso=', start_index=16276)
Annotation(end_index=16805, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdBffSQZ8PHrI9Tqm6zDOnhJdqZfWVJLZZIg2xms9GErWLO-19K66DGHv64234MKK8RcXDYPB_GyGB9k6s-livhbH__IkdYP3Gt_Du2RKPIR1yYS7XwqFRCN3h-2lAbi4lhqkKxJdo', start_index=16791)
Annotation(end_index=16805, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTYX9FvH_rtCguUYKJYUZPL9BcJbkCXveddEKqbWGrl9Q6Pbae16jaWwI8_-THzXdDUj1YeDvSsPt5pQQoe0WJznerRUnzzXiz8Un7h7w24N20xMR-K9qoeSnxgdI15oxAk61bU1gtWmwQHOlAPQ==', start_index=16791)
Annotation(end_index=17169, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPemyV18QUmOZEbG04xahTWXL8XUUJdQyPf9msCI0XOIxjnuSevD6x94FRayAMydealcwht1-1A2k4YOqbb25Jt1Y8RYBbZGoeZ8zhxodMMlRZwUVuIvwjaVFh7TpjUSqy4HF17g==', start_index=17159)
Annotation(end_index=17366, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYqZ58xVg_aVxKd-Y71GlAdivRqfoaXrS2-TauhlPm4gOc-p7cdybOL0v5J3XmgNMdxpTMBzTsVK-GPzpGmwEjlHDPhE5COdIScVk63wf9y-7EvgCoDBjo43MWbVwEuso=', start_index=17356)
Annotation(end_index=19056, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6GPPJCbpWqa4MM6TatM6DCGKa3ttW3A7URwajfMlPbP0Ew1ueSZhGeNbPi6JmbJBeq0S9d-G10w0516DrSdVpjxDOl_mE5hou9_5ua6NgGwyiP6cZSX7YyxLhfLVWRfYrUKQLUi_gVi463Qjb3Ew3Kbpjz3_ZF9cqCYXzz_XKc_ZU5XT7ZKTwLnKGQv8Oqmi46NW-ZA==', start_index=19047)
Annotation(end_index=19150, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2BK-IEDS6eLsgvrulr8atiQVpKPl2suy-F0UTXWcZFoyMCwq5YOcC8wpeOAmJh2bJdFg6iH0zfeduD6EiT1VpEuzK2RRF5AW4VOH-q8rWLGwIDCBX-qFy', start_index=19140)
Annotation(end_index=19234, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEU8P5syFj4DJT_uZh6wEBTYkcPNPgGcRvKEQUr-U8ZXCu6Nl-ZGggX2zr9OHOlKiSJEjwFrNWHOR-fqow9C48roEguGv0YvrKOunbTEN55FxT-0zDmYyvPtGkTF9Wx7chA6WrF6v_HrZ_VtKfRhjyMPypsoSsx', start_index=19225)
Annotation(end_index=19303, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzQOdctY-awUs4vYQWsOPn3osl0y3yqj5b8OZJhfc5NzCl04E_06olPfg68pHk6Hza5nk2z8usMNDfW_4UNZNJrfqDzbApfBFXo8wk3eNDQFjI5D8pvqaT2MAEXJVm0wq5T-nRXadDKBkAhPuvcrg9BPquymwSgyIYSsoDJBnw6p3JkViAz80=', start_index=19293)
Annotation(end_index=19400, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYTiAJib1HqGIEM9wPweJiMpl71gPzy4qIjqvBSk4wpYfbSG-hnY6edJoQMWDzZ1zPnTzXTlBP1YwpSF_cbDF9TVXkjAEuP54Csaaa7tkInd8-jsG_', start_index=19390)
Annotation(end_index=19468, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTYX9FvH_rtCguUYKJYUZPL9BcJbkCXveddEKqbWGrl9Q6Pbae16jaWwI8_-THzXdDUj1YeDvSsPt5pQQoe0WJznerRUnzzXiz8Un7h7w24N20xMR-K9qoeSnxgdI15oxAk61bU1gtWmwQHOlAPQ==', start_index=19458)
Annotation(end_index=19546, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdBffSQZ8PHrI9Tqm6zDOnhJdqZfWVJLZZIg2xms9GErWLO-19K66DGHv64234MKK8RcXDYPB_GyGB9k6s-livhbH__IkdYP3Gt_Du2RKPIR1yYS7XwqFRCN3h-2lAbi4lhqkKxJdo', start_index=19536)
Annotation(end_index=19614, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9udxaKMNXYXn1lkc_wSxFDi0xQIqTFLm0Ta4xfhNTno4s1uA76wWkKQLIe1Os3x93Rd5VzACRd4v2ec81Z3eTsJWGsO6mDGoVgUlCsengGuHSQIVRDQJy983Ea6KpBg==', start_index=19605)
Annotation(end_index=19670, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOvIf0BH4jkrhAy2F2tQ_RgymaF0oU_JEFYetrRKn7ljMsfFAHESGo6bK4kpwVHn_-AkcgZdcoOKz0uKtCuqJuYP89jCVaGGPQVSc1aGQBBZM8TMVeJoOX7skdqx8zWT0jKDj3VOt501YvCaEl16dtQlar7SiNeuoc', start_index=19660)
Annotation(end_index=19758, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGnuyZItl1P5utrnHitHOxwv2hosJYjq_BvQV6qItl-eLng0-GXG3-R3zxD6f2cOE1pwDpr_wg7eBcvICGvjiyz_soSHmfIC_VC8DvxaMtGGphdUShkbSL1sV7LnFg3q_8csiqU2hBuNs9mNI_5QLAsTgDeNqBpHAY5rJgqvT2sSiEOI-MJlphz3c=', start_index=19749)
Annotation(end_index=19818, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyU56C0ecGZ78rso77-7og6-5Qwc25M42CKRDJZ-4hotyRlPRhofnkDmp808gWVY_CBl7UVdC8kHnTxrwufqwS5snFd_LJG3iwhuE_X1NXYhCiy34I', start_index=19808)
Annotation(end_index=19880, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjDLUC4qjEDWXLZ1Tcxe-RW5o59Rj3QFvJUgZyHsxmunIb1L8acpEhgr5doU-jVsY8mkEKLQQkqLj_XdXR6_BYJcL87ud9Gmpvhs6y0TS8asty0nxYIF-qZB-LeWTVqHdfkDYyrdRJAvM0Qg==', start_index=19871)
Annotation(end_index=19943, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENWQ7RHDhJYRxZhHtvk6Wbo0dgiWA17COJ2jaLxw1ynvcllr74zrjLr412T3eq62L_ZAglWv0Yc1eDeax_PEmihht-PFO4rnafweQFW5IVkWF1u2kOltl1hb5aZK7yqltBYt7hqbE0IkYeh4aoto5ANvqS4NJ3rBynUSUE3BBwqt4hd-A=', start_index=19933)
Annotation(end_index=20016, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZI229xdCkv4D0B-gWxPDcrvbrLcVt4V1XzBA6t-2RKTdj1RpLPype9RKODN2d1gyAnaqbpJzj_LgEHXr-DilQCTqTA3y0aweVRx-QmHjpUAArI0t0dF9fBOAC8f0DsXSRuOpO9ivuMxYXmocARtPBW29yAuPjnhZRcOQzXVunwqJTg1bF57lSU5TSxl8nxBzkfw==', start_index=20006)
Annotation(end_index=20104, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFn1S0-Tbu_0RzFG-VQyI11fo66xRYfMr0iZZ2bmRSNyZ3W_DbCR-YP7jevfgN--UxaUHGk-I_GZZOKRCroxIPp6N1Kt_wzKIPl8LXdVjPop98O3igbHKVwn9JuJXftTw==', start_index=20095)
Annotation(end_index=20163, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELOT8c1b_AuYPr5u-3Zjo47wbCmxWJ-tOZw3WPgqIQP07xkn_6_ruLabUP1y1WLZljthnc-OmF7RrfD5kxl03gd_dVCI7dvS1cGnO2XRIqVCjRayKn1BEN', start_index=20153)
Annotation(end_index=20246, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfM8uxzoqRIp8t-2Q-JEE2q898YExXlZYhbiPnSqCWYH2-oi1y7heSiMKm6L5Z9uU4kLOZ0T5EeS-r2F1K_1-2FPN84ydboOHyVQljFOpbqphAXgf3myKSktwPefm2H9a0iQDImf5P8L7JgxCtPEGUCZGcURG-exYJGfUyKg9ggPpYPEh9tu74S21H', start_index=20236)
Annotation(end_index=20312, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIcqMRj-0sHFz6pMKAkiUaA6bQxP3bQ_zu7v12bZeXZfp4PPlH6r9MuTKezfvMqze9f_S0uQHCGWTOXPPPlWXHcH4-fqNjEUMxCVoCLkjCpj9olwkjFs2HP2wVzfradLctlxt9CtY=', start_index=20302)
Annotation(end_index=20385, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN5xLG9-z9IKvBvUU9RPptdfjFuy1xSupT5fMSJvSZ9eXu5Aco9cZtPIE7ab5jugOq26-H2tCCrbPgZqkiQPUezGkhmkT875_0YzfON4i-ZwgcUJnTmUL44QDR7x8K3R-w0AOXpQRzDYsqZJDBEWULAX3Rt7Wixna8l-L8rVoMtuK8xmG-N86-QkTEKNYCi-y5kBzQ', start_index=20375)
Annotation(end_index=20456, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHO-Nwx_AUHMqnxwQIIeO5PUNAU3gBnCJue1jL1m78Cc7a-B29qaXnlOKy0MxRcUXOfVNsBUVOLSWn8pVgZ_sOLz9pC3d61EyExOopHyZntBNdN7Zx5VPyHVUFL-vkLJO1r83m5ycwJLy1olVhNLrBjZqfJkUPQfaUUkNy77Ne17cY=', start_index=20446)
Annotation(end_index=20532, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgGilkzUgB7CI5PiBwVBNZTOEVeRAvV1Wg04l1cnxilyjhoWy-emufGBjJXXvn6B3kWHkomSUxK-cD0HkOCpE11KMqdnU-yY98StRB7U5UA9SY8tNHELPbuz1PtOqXHJtVZ7_huWFZ', start_index=20522)
Annotation(end_index=20605, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEC8RP0j2NElFtRPT7DWMeCFf-AKf4WZsWMemOSJBwuzIFXZ8AxS0ppPTfmDKS-3FFsULXWMegDjf55kFYXEpMo73bAeaxguau6DtIQ2xRPOOX1xbSZFYRp', start_index=20595)
Annotation(end_index=20671, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE81bp6bFxb_nPi4UB6yUvLOcm1vxEiQbSlJXCV7te198C0a3FYzGxaZj4WjwO0owk_w1JSi0hp3j_uHd1EEkM_wWt3wIVnwzBU7jafWlztcu6dv2gBgVde6AYvv3YaP4C9LLJ9V1UBy_TjD0fLpRnSOGlTydnqkHcmx4A=', start_index=20661)
Annotation(end_index=20738, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWMTLM0yDrnqLhMJkqFprVSDNaNAkzZFXQAOOYelVaj9LbIEuzBoNYvEa0QW0d6n0NlMiO9MLh2fZmTvw3efxytEv_UDtFNE9YG3FVhYRyVPfiuHGW8fd_uCUr8frV', start_index=20728)
Annotation(end_index=20780, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyU56C0ecGZ78rso77-7og6-5Qwc25M42CKRDJZ-4hotyRlPRhofnkDmp808gWVY_CBl7UVdC8kHnTxrwufqwS5snFd_LJG3iwhuE_X1NXYhCiy34I', start_index=20770)
Annotation(end_index=20836, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFv5zPSmKqsvoGa_sljrY8ynZu3nocoiWW2NG5FSCsjSApILzMn7uvnboeIK2VHqXWoVCqdyhs3XaQiUcTLH8bT2EZkDLvGRJ8lJzsmpe8SMF_iusvYNbMpXiJTMVSZ0BwrVKedlQtCIWRHQM578cw5bP3qTfedAb0jny5x-a8Dv5-nP73KtKGksr39KbkvpoVmA5nAixpuiZT0jl6Dzg==', start_index=20826)
Annotation(end_index=20901, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCEi8nF6bUcprMtdr0IvRqK0PdYouQZ0TDmSN34PXF-wPYgLYFREpoAkdMC0VUS8jSYc9vVIcLoQjvxRzSfCZyUFKH9hhx0y7wvgg4jm1MMJQ0ZWb5jJG9zPK0zOiAzEIHJvZIe1GAXYlO3W59dQ==', start_index=20892)
Annotation(end_index=20969, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFn1S0-Tbu_0RzFG-VQyI11fo66xRYfMr0iZZ2bmRSNyZ3W_DbCR-YP7jevfgN--UxaUHGk-I_GZZOKRCroxIPp6N1Kt_wzKIPl8LXdVjPop98O3igbHKVwn9JuJXftTw==', start_index=20960)
Annotation(end_index=21024, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7w-ymH_3xdbTfgCWl83yhCWMy2quF5Z8U1q4G_tYCera1EcxkKhggtMynTeHIDT2L67TwqifjJOfNrVp-uHg-ZRmjEpwSaJKcJ79CsT2yemv4O_Am', start_index=21014)
Annotation(end_index=21087, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFY2VfTopZJn5k0Guyx2Bk5E3aweKnIJ0s4UVhrXBcoSXKnYAVgNwmPdbpaHeP8XmEDX2PHpLvkaX3H3YdHABmICOTmImEcc_0h5f-xiXmkhy5cO8=', start_index=21077)
Annotation(end_index=21177, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPemyV18QUmOZEbG04xahTWXL8XUUJdQyPf9msCI0XOIxjnuSevD6x94FRayAMydealcwht1-1A2k4YOqbb25Jt1Y8RYBbZGoeZ8zhxodMMlRZwUVuIvwjaVFh7TpjUSqy4HF17g==', start_index=21167)
Annotation(end_index=21251, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvmQU76PTCHzMBiHmqMKzNi4spQvXOoFrXAid5rUd2iOoAAByBTMUsdBXRWlDy9_0kZKsLlNNxHBnuKb-p2pBhyK-9zlFl-ZsNZLteYnf-ompWCDTpU6EvzrYxj2svxyZjDuFLGSXlYGWXjq1Q2NyL7IK1lzMSrP3pjLMOYajOmYTm4kFyj3TlIQVR5g==', start_index=21241)
Annotation(end_index=21330, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYqZ58xVg_aVxKd-Y71GlAdivRqfoaXrS2-TauhlPm4gOc-p7cdybOL0v5J3XmgNMdxpTMBzTsVK-GPzpGmwEjlHDPhE5COdIScVk63wf9y-7EvgCoDBjo43MWbVwEuso=', start_index=21320)

## Sources
