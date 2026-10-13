# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 3b4d6edc | **Time:** 521.30s | **Cost:** $2.63497
--------------------------------------------------------------------------------

# Design of Flexible Transmission Mechanisms in Minimally Invasive Surgical Instruments: Balancing Precision, Rigidity, and Force Feedback

### Key Points
*   **The Fundamental Trade-off:** Minimally Invasive Surgery (MIS) instruments face a critical design conflict: they must be flexible to navigate tortuous anatomical paths safely but rigid to transmit sufficient force for tissue manipulation and provide accurate haptic feedback.
*   **Variable Stiffness Mechanisms (VSM):** Recent advancements in **fiber jamming** and **layer jamming** offer dynamic rigidity control. Fiber jamming, in particular, has demonstrated response times under 300 ms and high stiffness ratios, allowing instruments to switch between navigation (flexible) and operation (rigid) modes almost instantaneously.
*   **Transmission Dynamics:** Wire-wound flexible shafts utilize opposing layer windings to achieve high torsional stiffness (up to 100 times the sum of individual layers) while maintaining bending flexibility. However, internal friction and backlash remain significant challenges for precision.
*   **Force Estimation Strategies:** Due to size constraints preventing distal sensor placement, **model-based estimation** (using Cosserat rod theory or Neural Networks) and **visual-haptic fusion** are emerging as primary methods to restore force feedback without increasing instrument diameter.
*   **Backlash Compensation:** Hybrid control strategies combining feedforward friction models (e.g., LuGre, Capstan) with proximal sensing are essential to mitigate the non-linear hysteresis inherent in tendon-sheath and flexible shaft transmissions.

---

## 1. Introduction

The evolution of Minimally Invasive Surgery (MIS) and Robot-Assisted Minimally Invasive Surgery (RAMIS) has revolutionized medical interventions by reducing patient trauma, recovery time, and postoperative complications. However, the separation of the surgeon from the operating site via long, slender instruments introduces significant engineering challenges, primarily the loss of direct haptic feedback and the mechanical trade-off between instrument flexibility and rigidity [cite: 1, 2].

In open surgery, surgeons rely on palpation to diagnose tissue abnormalities and gauge the force required for suturing or dissection. In MIS, this direct connection is severed. The transmission mechanisms—whether tendon-driven, concentric tubes, or flexible rotary shafts—must convey motion from the surgeon’s hand (or robotic master console) to the distal tip inside the patient. Ideally, this transmission should be transparent, meaning the surgeon feels the exact interaction forces at the tip (force feedback) and the tip moves exactly as commanded (precision) [cite: 3, 4].

However, the requirement for flexibility to navigate anatomical pathways (e.g., the gastrointestinal tract or vasculature) inherently compromises the structural stiffness needed to transmit high forces and maintain precise positioning against tissue resistance [cite: 1, 5]. Flexible transmissions suffer from friction, backlash, and hysteresis, which degrade position accuracy and mask the subtle forces required for haptic feedback [cite: 6, 7].

This report provides an exhaustive analysis of the design strategies for flexible transmission mechanisms in MIS. It explores how advanced mechanical designs, such as variable stiffness actuators and optimized flexible shafts, can be integrated with computational force estimation algorithms to resolve the conflict between navigation flexibility and operational rigidity.

---

## 2. Mechanics of Flexible Transmission Systems

To design for optimal force feedback and precision, one must first understand the mechanical behavior of the primary transmission types used in MIS: Tendon-Sheath Mechanisms (TSM), Flexible Rotary Shafts, and Concentric Tube Robots (CTR).

### 2.1 Tendon-Sheath Mechanisms (TSM)

Tendon-sheath mechanisms are ubiquitous in flexible endoscopes and catheters due to their ability to transmit tension over long, tortuous paths while maintaining a low distal profile. However, they are plagued by non-linear friction and backlash, which are the primary antagonists to precision and force fidelity.

#### 2.1.1 Friction and Hysteresis
The transmission of force in a TSM is governed by the interaction between the tendon and its sheath. As the instrument bends to follow anatomical curves, the normal force between the tendon and sheath increases, leading to exponential friction losses described by the Capstan equation [cite: 8]. This friction results in a phenomenon where the tension applied at the proximal end is significantly different from the tension delivered at the distal tip.
*   **Hysteresis:** When the direction of motion reverses, the tendon must first overcome the static friction and slack before the distal tip moves. This creates a "dead zone" or backlash hysteresis, which can exceed 10 degrees in bending joints, severely degrading surgical performance [cite: 7].
*   **Non-linear Behavior:** The friction is not constant; it varies with the total curvature of the path, the tension load, and the velocity of movement. This makes linear control strategies ineffective for precise positioning or force estimation [cite: 6, 9].

#### 2.1.2 Backlash and Lost Motion
Backlash in TSMs arises from the clearance between the tendon and sheath and the elongation of the tendon under load. In long flexible instruments, this compliance results in "lost motion," where proximal actuation does not immediately translate to distal movement. Research indicates that reducing backlash hysteresis to below 10 degrees is critical for maintaining efficient performance in robotic endoscopic tasks [cite: 7].

### 2.2 Flexible Rotary Shafts

Flexible rotary shafts are designed to transmit torque around bends, making them ideal for drilling, reaming, or actuating distal mechanisms in MIS.

#### 2.2.1 Structural Composition and Torsional Stiffness
These shafts are constructed from layers of high-tensile wire wound over a central core. Crucially, each layer is wound in the opposite direction to the one below it.
*   **Dynamic Interference:** When torque is applied, the outer layer may contract while the inner layer expands (or vice versa, depending on rotation direction). This creates a dynamic interference or "locking" effect between layers.
*   **Stiffness Amplification:** This inter-layer interference results in a torsional stiffness that is approximately **100 times greater** than the sum of the stiffness of the individual layers acting alone [cite: 10]. This property is vital for MIS, as it allows the shaft to be flexible in bending (to navigate curves) while remaining rigid in torsion (to transmit precise rotational motion and torque).

#### 2.2.2 Directionality and Friction
The mechanical properties of flexible shafts are often direction-dependent. A shaft wound for clockwise torque transmission will possess higher stiffness and torque capacity in that direction. If rotated in the unwinding direction, the layers may separate, significantly reducing stiffness and increasing backlash [cite: 11]. Furthermore, internal friction between wire layers increases as the bend radius decreases, which can lead to heat generation and efficiency losses [cite: 10].

### 2.3 Concentric Tube Robots (CTR)

Concentric tube robots represent a different class of flexible transmission, relying on the elastic interaction of pre-curved superelastic (Nitinol) tubes nested within one another.

#### 2.3.1 Stiffness Interaction Modes
The shape of a CTR is determined by the relative rotation and translation of its constituent tubes. The interaction is governed by the bending and torsional stiffness of the tubes [cite: 12, 13].
*   **Dominating Stiffness Pair:** If one tube is significantly stiffer than the other, the robot conforms to the shape of the stiffer tube. This allows for a "follow-the-leader" deployment where a stiff outer tube guides a flexible inner tool [cite: 13, 14, 15].
*   **Balanced Stiffness Pair:** If the tubes have similar stiffness, their interaction creates a resultant curvature that is a vector sum of their individual pre-curvatures. This mode allows for continuous control of the tip's curvature by rotating the tubes relative to each other [cite: 16].

#### 2.3.2 Stability and Snapping
A major design challenge in CTRs is "snapping" instability. This occurs when the energy stored in the torsional twisting of the tubes is suddenly released, causing the robot to jump unpredictably from one configuration to another. This instability is dangerous in surgery as it can cause tissue damage. It is fundamentally caused by a high ratio of bending stiffness to torsional stiffness [cite: 17, 18].

---

## 3. Variable Stiffness Mechanisms (VSM) for Rigidity Control

To resolve the conflict between the need for flexibility during insertion and rigidity during operation, Variable Stiffness Mechanisms (VSM) have been developed. These allow the mechanical properties of the instrument to be tuned in real-time.

### 3.1 Jamming-Based Mechanisms

Jamming mechanisms rely on the transition of a material from a fluid-like state to a solid-like state upon the application of a vacuum or external pressure.

#### 3.1.1 Granular Jamming
This involves a membrane filled with granular media (e.g., beads). When a vacuum is applied, the particles interlock, increasing shear resistance and bending stiffness. While effective, granular jamming often requires significant volume changes and can be bulky, which is disadvantageous for the narrow workspaces of MIS [cite: 1, 19, 20].

#### 3.1.2 Layer (Laminar) Jamming
Layer jamming utilizes the friction between stacked sheets of material (e.g., paper, plastic, or steel). When the stack is compressed (usually via vacuum), the friction prevents the layers from sliding past one another, dramatically increasing bending stiffness.
*   **Performance:** Layer jamming can achieve high stiffness ratios (up to 1800:1 in specific configurations) and is more compact than granular jamming [cite: 20].
*   **Geometry:** It is particularly well-suited for tubular or flat designs and maintains a hollow lumen, allowing other instruments to pass through [cite: 21, 22].

#### 3.1.3 Fiber Jamming
Fiber jamming is a more recent development that offers distinct advantages for catheter-like instruments. It involves bundles of fibers that jam against each other under vacuum.
*   **Speed and Ratio:** Recent research has demonstrated fiber jamming catheters that can switch stiffness states in **under 300 ms** and achieve stiffness changes of up to 6.5 times (or even higher in optimized modules) [cite: 23, 24].
*   **Multi-directionality:** Unlike layer jamming, which is often anisotropic (stiff in one plane, flexible in another), fiber jamming can provide tunable stiffness in multiple bending directions, making it ideal for 3D navigation in the heart or vascular system [cite: 20, 23, 25].
*   **Clinical Relevance:** This rapid switching allows for "on-demand" rigidity. A catheter can be soft for safe navigation through fragile vessels and then instantly stiffened to provide a stable platform for ablation or tissue puncture [cite: 23].

### 3.2 Phase Change and Fluidic Mechanisms

*   **Low Melting Point Alloys (LMPA):** These materials (e.g., Field's metal) are solid at body temperature but melt when heated. They offer extreme stiffness changes (rigid to fluid). However, the thermal activation and cooling processes are slow (often tens of seconds to minutes), limiting their use in dynamic surgical tasks [cite: 23, 26].
*   **Fluidic/Pneumatic Stiffening:** Pressurizing chambers within a flexible instrument can increase rigidity. While simple, this often leads to "ballooning" or expansion, which may be undesirable in confined anatomical spaces [cite: 1, 19].

### 3.3 Hybrid Designs
Combining transmission types can yield optimal results. For example, a tendon-driven manipulator can be integrated with a variable stiffness spine (using jamming or phase change materials). This allows the tendons to provide precise steering while the spine manages the overall structural rigidity [cite: 27].

---

## 4. Precision and Backlash Compensation

Achieving high precision in flexible instruments requires mitigating the inherent backlash and friction described in Section 2.

### 4.1 Mechanical Compensation Strategies

*   **Dual-Drive / Antagonistic Control:** Using two motors to drive a single joint (antagonistic pairs) allows for pre-tensioning. By maintaining a baseline tension in both tendons, the "slack" region is eliminated, ensuring that any motor movement results in immediate joint motion. This "counter-operating drive" method effectively cancels backlash [cite: 28, 29].
*   **Pre-tensioning Springs:** Incorporating pre-loading springs in the transmission chain can eliminate gaps in the assembly and maintain tension on cables, reducing the mechanical play that contributes to backlash [cite: 30].

### 4.2 Control-Based Compensation

*   **Friction Models:** Advanced friction models, such as the LuGre model or modified Capstan models, are used to predict the non-linear friction behavior based on the instrument's current configuration (curvature). These models feed into the control loop to add a compensatory torque, effectively canceling out the friction forces [cite: 6, 9, 31].
*   **Hysteresis Inversion:** By characterizing the hysteresis loop of the instrument (the difference between loading and unloading paths), controllers can apply an inverse model to linearize the output. This is crucial for ensuring that the surgeon's input motion maps linearly to the tip motion [cite: 7, 32].
*   **Time-Delay Estimation:** Some controllers use time-delay estimation techniques to approximate unknown dynamics and disturbances (like friction) from the previous time step, allowing for robust control without a perfect model [cite: 33, 34].

---

## 5. Force Feedback and Estimation Strategies

Restoring the sense of touch (haptics) is the ultimate goal of optimizing flexible transmissions. Since placing force sensors at the distal tip is often impossible due to size and sterilization constraints, indirect methods are required.

### 5.1 Distal Sensing (Direct Measurement)
While challenging, miniaturized sensors are being developed.
*   **Fiber Bragg Gratings (FBG):** Optical fibers inscribed with gratings can measure strain with extreme precision. They are immune to electromagnetic interference, biocompatible, and small enough to be embedded in catheter walls. FBGs can measure contact forces and shape simultaneously [cite: 35, 36].
*   **Vision-Based Tactile Sensors:** Small cameras embedded in a soft tip (e.g., GelSight) track the deformation of a gel layer to infer contact forces. While promising, these require a line of sight or internal illumination and significant processing power [cite: 37, 38, 39].

### 5.2 Proximal Sensing and Model-Based Estimation
This is the most common approach for current surgical robots. Sensors measure tension or torque at the *proximal* end (outside the patient), and algorithms estimate the *distal* force by subtracting friction and internal stiffness.
*   **Cosserat Rod Theory:** This mechanical modeling framework treats the instrument as a continuous elastic rod. By solving the equilibrium equations that account for internal elastic energy and external loads, the model can estimate the tip force based on the known shape and actuator inputs [cite: 40, 41, 42, 43].
*   **Neural Networks:** Deep learning models (e.g., Recurrent Neural Networks or MLPs) can be trained to map proximal inputs (motor current, position, tendon tension) to distal forces. These "black box" models can capture complex non-linearities (like friction and backlash) that are difficult to model analytically [cite: 36, 44, 45].
*   **Kinetostatic Modeling:** This involves solving the static force balance and kinematic constraints simultaneously. By incorporating a friction model (determining friction direction based on velocity), these models can estimate tip forces with errors reduced by over 45% compared to simple models [cite: 8, 46].

### 5.3 Visual-Haptic Fusion
Given the limitations of mechanical force feedback, "visual haptics" or sensory substitution is gaining traction.
*   **Concept:** Visual cues are used to convey force information. This can be direct (observing tissue deformation) or augmented (graphic overlays on the surgical monitor representing force levels).
*   **Efficacy:** Studies show that visual force feedback (VFF) can reduce suture breakage and peak applied forces, particularly for novice surgeons. It serves as a bridge, allowing the surgeon to "see" the force they cannot feel [cite: 47, 48].
*   **Fusion:** Combining visual data (tissue deformation tracked by cameras) with kinematic data (robot position) creates a robust force estimation system. The vision system estimates external force by analyzing tissue indentation, while the kinematic system cross-references this with the tool's stiffness [cite: 49, 50].

---

## 6. Design Optimization for Specific Applications

### 6.1 Optimizing Flexible Shafts for Precision
To balance precision and rigidity in rotary shafts:
*   **Winding Geometry:** The number of layers and the winding angle must be optimized. A "dynamic interference" design, where layers tighten against each other under load, maximizes torsional stiffness (up to 100x amplification) [cite: 10].
*   **Material Selection:** High-tensile steel or stainless steel is standard. For MRI compatibility or specific stiffness profiles, non-magnetic or composite materials may be used.
*   **Lubrication and Sheathing:** A liner (e.g., Teflon/PTFE) between the shaft and its casing reduces friction, which is critical for minimizing the "stick-slip" phenomenon that degrades haptic transparency [cite: 51].

### 6.2 Optimizing Concentric Tubes for Stability
*   **Patterning:** Laser-cutting anisotropic patterns (e.g., rhombuses) into the Nitinol tubes can adjust the ratio of bending to torsional stiffness. Optimizing this ratio is the key to preventing "snapping" instability while maintaining the desired workspace [cite: 17].
*   **Stiffness Matching:** Designing the tube set as a "Dominating Stiffness Pair" allows for predictable deployment, where the outer tube dictates the path and the inner tube performs the task [cite: 13, 14].

---

## 7. Conclusion

Designing flexible transmission mechanisms for MIS requires a multi-faceted approach that addresses the inherent mechanical contradictions of the field. The "Holy Grail" is a system that is compliant enough to reach deep anatomical targets without trauma, yet rigid enough to perform precise interventions with high-fidelity force feedback.

The research indicates that no single mechanism solves all problems. Instead, the optimal solution lies in **hybridization**:
1.  **Variable Stiffness:** Utilizing **fiber jamming** allows for instantaneous switching between navigation (flexible) and operation (rigid) modes, solving the fundamental rigidity trade-off [cite: 23, 24].
2.  **Advanced Transmission:** Employing **wire-wound shafts** with optimized layer interference provides the necessary torsional stiffness for rotary tools [cite: 10].
3.  **Computational Intelligence:** Overcoming friction and backlash requires **model-based compensation** (e.g., Cosserat or Neural Networks) combined with **proximal force sensing** to estimate distal interactions [cite: 40, 45].
4.  **Sensory Augmentation:** Integrating **visual-haptic fusion** ensures that even when mechanical feedback is imperfect, the surgeon receives reliable force information through augmented visual cues [cite: 47, 48].

By integrating these mechanical and computational strategies, engineers can design the next generation of surgical instruments that restore the surgeon's sense of touch and control, ultimately improving patient safety and surgical outcomes.

---

### References

*   **[cite: 1]** *Design of flexible surgical instruments balancing stiffness and precision*
*   **[cite: 52]** *Flexible Medical Devices: Review of Controllable Stiffness Solutions*
*   **[cite: 30]** *Design and Analysis of a Six-Degree-of-Freedom Handheld Microsurgical Instrument*
*   **[cite: 5]** *Design of a flexible shaft for minimally invasive surgery*
*   **[cite: 3]** *Improved Force Transmission of a Flexible Surgical Instrument*
*   **[cite: 44]** *Tendon-driven grasping force feedback mechanism for flexible surgical robots*
*   **[cite: 2]** *Role of force feedback in minimally invasive surgery*
*   **[cite: 4]** *Force feedback in robotic surgery: Assessment and design*
*   **[cite: 35]** *Development of a new flexible manipulator integrating contact force sensors*
*   **[cite: 19]** *Variable stiffness mechanisms for flexible medical devices*
*   **[cite: 26]** *Variable stiffness insertion tube for LESS surgery*
*   **[cite: 23]** *Variable stiffness catheter based on fiber jamming*
*   **[cite: 53]** *Laminar jamming for variable stiffness in robotics*
*   **[cite: 6]** *Motion Compensation of Tendon-Sheath Driven Continuum Manipulator*
*   **[cite: 9]** *Friction compensation techniques for tendon-driven robotic hands*
*   **[cite: 54]** *Force estimation for tendon-driven continuum robots*
*   **[cite: 55]** *Shape reconstruction and force estimation of soft robots*
*   **[cite: 40]** *Simultaneous shape and force estimation of tendon-driven soft robots*
*   **[cite: 41]** *Kinetostatic model for force estimation in soft robots*
*   **[cite: 45]** *Tip contact force sensing method based on recurrent neural network*
*   **[cite: 10]** *Flexible Rotary Shafts: Mechanical Design Guide*
*   **[cite: 7]** *Backlash hysteresis criteria of surgical tool bending joints*
*   **[cite: 56]** *Transmission backlash compensation for cable-pulley systems*
*   **[cite: 32]** *System performance in free space movements for system backlash*
*   **[cite: 28]** *Compensation of Backlash for Geared Drive Systems and Thrust Wires*
*   **[cite: 12]** *Concentric tube robots: Design and optimization*
*   **[cite: 42]** *Kinematics and Stiffness Modeling of Soft Robot With a Concentric Backbone*
*   **[cite: 17]** *Design Optimization for the Stability of Concentric Tube Robots*
*   **[cite: 13]** *Concentric Tube Robots: Domination and Balanced Stiffness Modes*
*   **[cite: 10]** *Flexible Rotary Shafts: Internal Friction and Design*
*   **[cite: 11]** *Design and selection of flexible shafts*
*   **[cite: 36]** *Haptic feedback for flexible endoscopic surgical robots*
*   **[cite: 57]** *Haptic Feedback and Force-Based Teleoperation in Surgical Robotics*
*   **[cite: 37]** *Vision-based multi-axis force sensing module*
*   **[cite: 27]** *Variable stiffness continuum robots: Clinical applications*
*   **[cite: 31]** *Friction observer for robots with joint torque sensing*
*   **[cite: 33]** *Adaptive friction compensation for robotic arms*
*   **[cite: 34]** *Tracking Control of Robot Manipulator with Friction Compensation*
*   **[cite: 18]** *Stability of concentric tube robots*
*   **[cite: 14]** *Concentric tube robots: Domination stiffness tube pair*
*   **[cite: 15]** *Tendon-actuated concentric tube mechanisms*
*   **[cite: 16]** *Concentric Tube Robots: Stiffness Pairs*
*   **[cite: 21]** *Layer jamming mechanism for minimally invasive surgery*
*   **[cite: 22]** *Scalable Variable Stiffness Revolute Joint based on Layer Jamming*
*   **[cite: 58]** *Layer Jamming Actuator for Tunable Stiffness*
*   **[cite: 20]** *Fiber jamming vs Layer jamming for soft robotics*
*   **[cite: 38]** *Vision-based tactile sensor for force estimation*
*   **[cite: 49]** *Visual Force Estimation During Teleoperation*
*   **[cite: 47]** *Effects of visual force feedback on tying surgical knots*
*   **[cite: 39]** *Vision-based tactile sensor system using deep learning*
*   **[cite: 8]** *Improved friction model for tendon-driven soft robotic devices*
*   **[cite: 43]** *Tendon-driven continuum robot model considering friction*
*   **[cite: 46]** *Comprehensive Control Method for Tendon-Sheath System*
*   **[cite: 59]** *Experimental determination of stiffness of umbilical cables*
*   **[cite: 51]** *Flexible shaft configuration and characteristics*
*   **[cite: 11]** *Design and selection of flexible shafts (Thonab)*
*   **[cite: 24]** *Rapidly tunable tensile stiffness via fiber jamming*
*   **[cite: 60]** *Stiffness-tunable soft actuator based on wire/fiber jamming*
*   **[cite: 10]** *Flexible Rotary Shafts: Torsional Stiffness*
*   **[cite: 48]** *Visual-haptic fusion for force sensing*
*   **[cite: 61]** *Artificial sensory neuron with visual-haptic fusion*
*   **[cite: 50]** *Finger contact sensing and visual-haptic fusion*
*   **[cite: 29]** *Counter-operating drives for backlash compensation*

**Sources:**
1. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBoMKRWoS2SotCla-xFACUn5fSyfaK_ehuVPwDOaq9QLy3WtssnXYEGri1d3QU6ni_7pcg27xSlm7xYIW8-0eKmzZtoNUmOZUp2IBHqIPqTnM_KloEPCO4Z1Ws)
2. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs5v2nY0eZk9LvN4GHDES9-DV-_5oRoR2jy80AX9Smatb-o92te_E-ZE89fLI3npRtsTWxLtaMsxYRJpccXY6Vz2xuNL7iMuva7D417iZ4hgT2QRQzD1idGkljJqAIM4Bb2_QOsI3J)
3. [asme.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUR8B4cGF4r9-4GPV8W23pPvk2Fr3vOztnsUndJ6RrNldAC1BTBB8sE_uDB4geSv_T-sMYfm6EqkCax9Cudd9VAqq89XmddkGbKSTU5mdEqLMfAXS1hgO1OA5Afs0THHfu7AVpan2RUIeMhAMkZuw_V0T8oLTTEp9uwxHsfVzFtdGZISKI5Z_l9GbDJdWiRgT7LNGz1J9FFuwY3xdNR98WI_j6KR55CptXCeI7xpj2tQbQ2V5ttMqcqQ==)
4. [tum.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVbyKT2FleOlHyko8bU0ifm5ozOydsy1sjRJbADYtey0SQLXG6ToJ26ayPJvWpJ5PQ74vdWpzLi8fefNUQym4NQoIwrZ-x3pHXy_El2fV7WtVyxHXCxM1GS4kqdY4TxBVY32xPXfB0VnI=)
5. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFf1zpfQmDMmU9w4zJDC07wn0BVp8BahvuzN4Rcy-OLauGdzDlE5_HvSSUT4ZrP2PpsM4a8CFU8mmag-uGJQMPTzMNB06by0mwZc4iaG2vRMSDHZR77eL8nPtndWXXx)
6. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-9wziRVORtXUllLgclJAl2BvNSpyPxoM4Gk83Mu_iVdY6D6Ql6q9JcosUE49LbeRNCNL_wyYzEnF7DpoavxXEvd51iAuj0LlgweusyT0_uFM263e44XhNygYcCqp6dvoaIUseg6aGK6MlGAYn75qJjV16bpnHUIZ3D3FUXLkmy9nZMXEsoZ_rw-r3SkpXJ9sVqn3vKLb4TLFtOWz7dkyzFH5b5uED7g8sbzpnFjLaeph1K4rx-MC3nmvkSZvfDvr_bA==)
7. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEntSfmDjPFtdudD5FR1hgnvM8stpB7h2aS8DOWYwbFPuWGqEE0DnjtOOP1OsND03f7ICq7NDO6E3dWZ4OGoeky0iaD_WpqvBJ0_EYbk0emrIrqTCJolsCFG1kBWf6qSw==)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgxPE8ZYw7O81yEmdeQ2ngP3KqGdPf5c8wJI-LYLjhTOM6VPAmYQRwc3voTa-laPPu4PN--AdDat3vZMrL5wo5BgmYoYw7mnI9emSmK4SrlbFG2twT0NwS8jCR5nBQ5gZ_avPgWu_qlUhhDMTFNMJo89Zc4qXLXREA4dU6dEWqdHpqojkTRBV2Eb99UVJszvwoybIvZ2J1o8yD0S-INHkJjBazeIhnj63IyOsxogCXJP99NwGjskKazsQTnOlZ0A==)
9. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3eDwbIoC2R6sx6uUtx7MtlHkL-nkAU2ktGXz0AaZwbUQ41YzmWPRT9psZlXMiWMiCa6U_XK25b-evIbJKjWO0hfEO52uiO41OSU1LdGU3vF9J_FJ8RPTK9qFXLqk-GwuyrwHSv6eLbLuIf0-Ns6Q1pTJq67rSGMXYqK-lPkfbur7UZOrlSuiuNLgM3UtWD2MmUhOR7Ns5HfDHjeXkZYqPwloXBK88l_nd)
10. [sswhiteaerospace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxQDBJBi97O8-rrGpqGkKER3vihePckVJblSzGcz9JBVASaAC-w4zxcAuqXFvdASlQmVnbBdJg1ApTwTDgGudjddwM4fZwGrPe2SaaE8-ixaGadXFqyfolBKpFXCU5bSWjXgHat6yS612JH01uaOHqarB3ZbiBKovhWjBfpeFoIlGELQZEve0WXNxm0apn4tp6Lg==)
11. [thonab.se](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6rT9lMsOxbqf3ewa3AxUHNCFdzWWt_fJHHL53buFjCzEAYa7Im79mQqZOZsM-4UHVTWNBWOSNIw-YqQr4dYAFOnCBwa0gAoOLhBTv2Zxm5XK0KvxagNup_KVDa4PXHBvIWUpciM7Jlj5y1BAW6rqygaPlFA==)
12. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGh_LnE5gUitW_ytNtWa1mWur_cJzxkZudk6FNIS-cO6I6cS0epCJ3MTUf20I3JH89kZAxDE0Peld9JVascxrJdomHOD-tpdTco7blH6pHBzwCQs3mYpMPVbYrOpPkAs3Ux5QJyGLAy)
13. [harvard.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFC-wGeB-hmO_9pot1A8vW55UC1gUS9Zhd266_PGL9KubLaH6bC4KtbOR8LJgnTufEjoj3pFrAa08qhyz6gTOBFk7itNxxs5jGZI5CAnAxb3HaVZu1yq8ybUVSCFXCn0fCPt3sO4P7PaZp0BM30e0k8nwiZPEFjbem4p-bqLFBBkPbVsbwF91c=)
14. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjW_b0dN2TcDeRqOOgutGnUJQ-gRu6bAqDs8XDcEXEHtjclFX3SZxCpTUloLYINEmOi3hp6RCyOFNYjxwu5aQ7eKU0B8MenuffkGPwDUWKToprzOUoeaxWmDTUtdXhlqMiCuFKkv0V)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1tjO2YRr8P2-PCPlgm0-P452HDUGf6oUk6dqvIcXXqPxerN2t2ZYWQKeUh7n8ziRQnXmG4hAaHc46r6rShsuAljV4ZhLcxbrhpBKQh6g-FXFjuHG6MYQKejwu8BHnHcflTLRKWEtm7YWot670uYOTG-Gjk-mdIemIl5vrJ-fq5PK9UQYbFN-6c8jEirHNfIEnACtYHtb-QwWLr8Yf8WiAk7WJJzKOUDSoKItRDO9uyOtawkxbbi0CRSIAOisXFQ==)
16. [opencontinuumrobotics.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyfO1lp4G4WzxPYDYO1kvG1-VqXqUsFHiu53GPs9Chs4RyZRmaGksuucNisMN0eruC1-laOjP3isV26q-2dM8N-U7An-8Hp3HaJIBcWi5gz36Autf3VVdk99ryIQ2eF40unMqVdFcOopVr-UfTOrQZabTAbZfXCklHQQ==)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHmliFaxQdALf2dTGBv7KLB0OIs9sNcUHoKSRrZBN5_yMYoOwcryye00a5PZ8OAXd3gT6sbii4poQblTDMlLmkVsLaXQHWBcp-LQgEXCJUWNiWw5OPPzWFYyzYPZsZi3NldJqZDDUrjE7xVDs98c-rUtJPoqqjQZo-m9bhbMa44Y2vhvSIezSPO1q5jgd4tQ8zqsRlDoBpi6qXT5H_ro5nfdsfcGWmdl8=)
18. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2pzspmqRK5cSIUuC97YMHMcFiF4wQV8ARlerWSQrdUe1U8F2UXJ8xS7658jfmyEVOGVF3B5u0ATqWxp7cFNzzJyFMVsnuqmv423Z2qKz6ypaki28oP6IM6O-w63d_Ea3k)
19. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5kxI2nqUsJp36B_TSvCMGPm8LslvGOTN5DchxQAxYUvs8OT5MNiywxmOMoPTGD2LlAMhFWjgdHtNFaBtVI3CuPjxy9xuqQX0FMQEZE9ATlkS1ovshInH0q8GW4fqu1EDikZxKbiSSmmK6TaZGQMW7EIxXnj8dzB7AmZaZXn66coK5wkaodw3cwHqLzmr99HSD)
20. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5pd-15tmRiVEr_ys1jc7_g1KlcRRQnaBv8wfcbxtaBNNDQ1hoqB4b59W32uEcvzQluRsqisiaYpygFjDFI7bi3TXwOfpI0MKqQ_XUF_bt1dANMwPpF4HR35ilGA==)
21. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtQV6ozQsmHMETq9YcHpMbGkA4eqR6A4Kbi8Nnz2yEGjAqaiDAITGdDAUKzZ6SFHL6iocYddT_81BMZG-YWCstWTeY6XBszzXk-TmEK76bQcoD3Dpxz_xMKUcXRvMXbVmF4o2FGsa1Cd3_ZQf0zloqBhjV8QiHKYleudBH_pCrxULlZtjqUer0F_wmx-Q6Kzr5shj1cn73znkfBnfzATEtNibcj2sEzbsy4NwWHIq_sID8zHwp54n5YqwnzF3sqoAgGi807-ISTKPb)
22. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXrSj4B1C__NPMPuKoW58WvYSm5iqu-bUkOivBZSfQq1nE-PR_9S9fIU1rfj76do_csW3BNOTapx_dRfrTCEEmh3BKncT53kXlz3n-am6JK-1Yxzr27cIdAmGftw1NsHcy)
23. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExB3qvqHdk0oC-eutn3tAinNyEIOluWBTy6TMPO7AClkNtWuPBy669oz55d43GAlGkpFqBOucj3ttu4SWXS7LjkCDBYldp3Pza4-PakTSFwTI0CDyGdEhGsaXir_gGC5VU)
24. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXZHVKY4l0pqN6Vtuh8mNB8ZQA9aRlbdgXtkW-8WNicpkwEXs2bdavVlTcD24mFf39ofyvIjKex4yAd0PAVdEAMw02MirttEAjj7-jRspVJVLs4YtX0MMlU-d3tGelloj126QxVkDphw==)
25. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLFLqPZsm9guFFz6z4MBIS7D0lQOSsc19o7ApLT34kBhAFIpmc_9YebEOaj1AjvkAXhkud0wrFSWnT4FlGUIXL1K7n_zJU7hIRNzCe5HBjLdEBKkd3GUV4-U6EgfRuy4ro)
26. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5R27HBBdjKjZ6vOHvtNVZHBJkGEeXV9QoOvgCu8sP-j23wZfRi8IcVpQRyoVu6fNEaasyQI2qHb4but803xigXMD-UZF8YZicGd8X8eSm7iat3tL_9ScXtNX7fbQE6A==)
27. [lincaolab.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtrdFsq6fMgSmqJCW9RjX52KHekYmPt74vfRwajXRIKcYySNUU_W1IB8y1z_igrCMAIzt_DgITp_Y0CWSGTNU9CncY-rn7FFR0nMEdpoJ6Rwe0Edu9Dav2ZiWoTakcWJXmObW3IlKReZpIT9Kr8kz2qYRNBfpA-RytyOhg)
28. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1Enda9sk9QqeX7yUDMHV83B8E5RLKqTWIeJzu-EZ5m-XjJQDBA9n1se_P5PFeQB7PD5kYB8gOIrxbSJyFDyCuFoIeqeaueDTtnNwsi055C0ppcM2LNguaupLdvZHoKlFHG4QW2KRbgCQUJ-CdQir3qZncjS58r5LVjSC52o9k2SpnZb73mnAoX17D5MhETZZkra7pxVeSnsHpPhsWc2_Ow5lrTvKQLJkbly5FLQyUfbzswMs3MiZZaayKpm9HoQh3XQ==)
29. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJPZXTQdVJLfQ6xcfZIoLACSOb9r6UOjxRzfngJVN5mpfoEshRaxgK57OAlMLd8_zwcrN8H0eIGbtWoye-xeTYlSs4G6d0pP3QFuHRV-JyMObUdCIQzM5RGNXnSVYaCLRApkeu2pTKGZo4S3kyesbJYiZ1_0UvBPyu9Nb3C9nP4shNyLidJ8wAwXGIRsXdQtmCyYck190Uip3CQn8lSDk0SUpkovaagmz2eVfxUQZvyetbXyC--xQ=)
30. [asme.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQ9yd1M6Ra8971t_IR-Qtle85wDvujVxc9W4gBgLEnW9Kkcp2v0btFczoWhRIoc1Rt4ne9vNb1b9E2mzcPCCBWTA7zIt1BjAuKETyxDH0ZzmsenuOUPxQiP-dFlOSE1QB2carX5SKS3-qJ9t3prxorXSBXbJp0R4NsK9R-b8wWGgz-JWw_5dji48XFZhF7FWGK9lKuDGF4kbKExmuZrH9SHg0froZ-E_wO2wlbklGVx65Oa28dSmCPxwNt)
31. [uniroma1.it](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOdJ_gA81pKdmrLhAy-MN_grMU2w95x6zUm0c_ucMFCgBzWGqzqgPlTA2u1VSsprNLrdnP-McVJv7BUch_-50-35RJjS-XQNlhU04c05zHIaUkZ50vY9nOtxMOsE0c_j1O6ZMSdhZ_Eg65M9R-SCmT5Q26SqFcNbYBm7E=)
32. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRsZWmqfbpfrCZgByDjEDMvXeyR8i2_Ritf3zmqdWzRgnigWWz0X87OINJ3-MYQ6lI4KOwa5NO3766KtnI4-9iC2nJBd7cDY-HQGehpo037Ysu-B0sWVONJThfK-70S8h-QD4zeFxCbOaScwycnPZR49cU4paQqJo8CiSLtJVuhT97AkdXaWCqZHjiZG6QmOjmoXXaeYtP7iMHoXTSZgv6-pITNCNOGy9C7AUTz5rKUHNdCVs=)
33. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6lUvB1au8xPuNnPMO1nOz3wA6_Rt56AFepZKIIKAnKm5qw4Rg80XBwWREycqv2SiIek-64KYUvsBUNqSnHgg_9jqwmyjXiS_yVlrE5OO8LFkIzGQTVnFfV_FE9mY=)
34. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoFuSzJWvXGtYFm4MqWV-aKBpRPhAxLKwlqkLAIMAmfcdIgDRJO69xKqLZq2DYDO1ke46pGDnO1WPsxU9VsG3bPBSxjJYUoC1yqcvs02IxmkjqYP9v3x6_gh3vHxVGh9KFmYrg2CQFxi5IyOQmyNw6G3_a6BT8IkGetiGhDQVb9WLkYEgckjqA8FzpakTPf2LH8vHJVTN5pToP7BtxhnLcvshOsScjNCtif47rrodHrUE_s5aeIrJOYWsIsZfuWbHNlk9i9XpPW8SYm96uunDgN51vo28NbVbCWq5hyQ_3JGdCjJcbtg==)
35. [brunel.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHj76p6F5d0vE3uV49xMKFxehthIaIFqXCm_ILAySTsZnfHyqxsWKiHGFp01giwshsvQ5GgiwBnUlkcriRwE-pT_5PSAVoROd0Y-PnOThnV4fUnahWKkO4aonUFtCIBVfleMeiBqD6MXErTqT4GeMLAS8S4DvQusqNPL7OqATbtHV4jmd4iRu59nmi0HKUd9L2i3P8wItx0P1ya-hFWTpDdqra0cfmK3vVG)
36. [lincaolab.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpm-HMBE6pRAoVcc40AIeKYXIjUdrx4uORk31UHjQLrSeZifj6Yr_Xu2n1Pk0mIYWYZ4m054CyyfbtgwYzSKhaoKgD5kqyULNwbWJluqOYkrXwgQkmwJccYWrJNdN-h6qy6T0Y9OTnF2rnaul-Sg90A3-Z0hrWgbJnN6ImQLz_xzN5pjgNs6YTJniwY8GbUYA=)
37. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDzhBq2goK4UN-HgSL2FjyyB2bWRVYXPHut54XUziS-Dm6I55nda0Y5zPEBsMy3UjbbK3PqMMV0BAF0XRlBvknMXKVWqLO4j0aDzLawloK5OS8rycsXQ==)
38. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5UHq27Z1sAhl3tOLzysuqvELhpOcKu29ng3ghYR6odkqPLfZFkBKb_pQUaSQd3g6NE-rgZx5y8f66zgTx_Q-DcwcAcQBB2ductzW9qUGk48lujyQguw==)
39. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmOOIEBZJt8tweWKKQA4J985cOkT_pkEUOlnekfPMbBwfBAK1LMYz4poRHyGMRxwjThE8b8FwCirIDrpCMWFDPiRdf7z5ppTCkMR1nS28IL5xRPMytE_Wb5wGssd-I)
40. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdM6khB14GDFSMqecTio16T1yUb6_UGjJ0bOL3f7shGvxkftQrkX3jANyv1IM1PvpEsh1MxclRGefAPT443atgMgRQpy-VGY-1iTztVShdFLZjnG8vj4g_qMYY3ndDqn0zTC4VQi5ynFoxN7vrjn3S4tFDV1DacuFQCdp2dCb9lsv7WncJggR0i7v06kpzO1O2mZCRu8XWlnX9-z_xJfGhFn_wAIrbi2snTdj8frcMh4ORLX4mfJWvSdlTm83ihBFuXeEvYg==)
41. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlVItX5PeN8Jrt4c-0IREojdUSXiPR454tzrMqIs3S19sYh9CPjQmCwkv7VwxVrtlCMRfNSR6YatF8aT6vuGuf7sYMEYXEKpxQQY8BcjlaJZx30FuiQTtgO0G9hmHZ-ICy9pyrqeaCfW-xlugu72Dz)
42. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSVD4_qU9iij1AUwKMIVhZ0chYAGfG9LgSA2vmQaAvP7M53yEaIfvbZ05vIIL8LhQ0DBICNWLCmUO6EB8-JPJmI6u4FJLfVcehxTRAQ4RLG4PXg0ot7OSpmaP0Eqhycaa5fItIRj0K56TGWTD8N3tgyIKNcjs4GCz_L4a6nmRMTeoNpq_stYdb4Ve0vphBPCkhSLsBOLdEm8lr4DDeBLPiN6jAFz7mveqcGo2H-_vxMmO66uvtQXow3NG4fRZe20KLSVBby64=)
43. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCk6WcyVmbjFyW6FQ7-_nIJ1HMAP2zcKzilcd_GP5gam0AhauvWNVfOL1-6QmcyRdkdZ1YPPahnmNWlQgElouR3huk25yTKaX5QHX4BCXw1McYgHfTsdjegbxgcZI=)
44. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPzKfNgTr2K9u1B0J9j1aUMXTXsCmW5iwXz02JqB6h6aKLjWsI_Bsyioc5I8EeSQJIuq6aXWkcViSBpxB6vSqgA3En3XKSvqH-9O_D2OoBCPegyxI7QzOVgNIzWg-iHg==)
45. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG416Sg6WZw3qYhp_qZt3kmT8GPquBWqPA1tOHUtnD3N3AEalJVqraYDN__8zPqY7VEcdpXnua81OD88_CF4mnWISI_2sWnp6DgcnZmYgEbyTsCn-I9f76KVYv5LnyKig==)
46. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrbgXnk7-kE97D6PpFoAnxmhRlaI1dHRJHzm3Yp5znllaoAV3XxvDj7mj2yzg7VX8UowserQwIGjlgYM372SxfQbpJlRS2T5FpX7w2DzTc_liKElTHMARktlOF0XhbtIR2XJAyYBUivAJixzw9aTCBfJbZAJWU6FqMvmmnRxfJTcd_-TjlU3KKreV_fpFp1SlDq0MlcMD4S2Z310WmGAnv1vQYMAQJE6_zwnPbR2i0e8VNxcrxw5HCKz-8sI8tnUPZLYeR9OCxAlIlp3ogNYhprY9TyTUyQstKuENgAp1FWnyzyk1oTAZKHkVo47cRcP6U4NZLfaOiaE8VzS8h9vG90yPqoM-ObwNHZRWuJQ==)
47. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAHmO1VKjvZJ8yqO0nCa0fr516nMiw7KxfzsTglWFQYx9GUhM0vWEAwdjAJeiiMQoLlb7ROvloI-6Id7HIQmkH03fmM0WLKwq-mkU1HWfKW4d5b3i6PzvuC1sNAD_P7KXYruEah6aw)
48. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEDFtUwPbhaFuhUwlVqzPEUOoTNgf0I1Vajt_BbP9Es2fSNNKwZ9O1G62U2ZrdA2QXLNI1agApj7o1XFH-TlWjiv17OLLXvinF3pPKcZtX5IHPpBShBKnh2o65KzHBgqSio4qDM74aSg==)
49. [case.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlPJAeuSorO_whLwG5jo3hgNSCdhX8LN04ZNovYXnmnsl5XeArKenomv86ualWUKNAfB5qIK9453HtZ64DWYxinQqZGacd2fivv6NDT2ixdyI3RVSxRidTgqNErzUwVh4EovA5zh90faAzT17hywUMtIpfGc_RzmnNVQSc-Tm2pie2hrSV40GuLzAX9sSYGwstaw==)
50. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpOdLKzIbBFAm_bxPqhAMaseFX9lkinhWOL3TyAKv9mVlp-qCPhcOOWzzIvWpAieMvH_m9l_VCYY5o0sZ3_qdTJpNJ1gNH-OIl7Uig7tc_i1uqhmxNqgLiq4rUw7Z2cPhf2_ODZYZDjqANXb-NY1CNFDaEfcbBMMn_DUqTzwTpHjhQQh-98DrIFECWygaU-Mwg0q7UysFDMT5mxfRA4-dCXA5xVyooGJonCPXNdsE4BAaq)
51. [sumflex.jp](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuQkK69UpBpH7OZxfIgBLYAUTAOcunjqmt_5Yfl-lVHDAXYHht9yPqc8xQLDoZxFp_99YkKTskJf1gxf9Jy96lJeym2-okbyNET5IblOwbg4wJarZMeW--I0z85R-KVWtM_qFfRe6JLIplGqzby9tR4v-Gc2uLW8C6daM=)
52. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXZFym5-wn_5WWIM1yepvw1k4y23MVw29_M9vc13UA9300xDKzryURncGWzNmfb0ry_DwFLerP-3hbBpvqJwZcfVMRw90ZtjpkOrXyN_KlAbNMr_BXyJOFYRZR9UzHQiMBPIFZ_AmuboKqZEw-DybsOlpa4rmXnLP64yWjS_lSe9hkdCy95bWh-6zUjO5lhsAXkTaMXbF0vHsl5i4o-Kxm04vWYwyZnyZ7uVhp)
53. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHU0ZJr3MvBY-9HxuE7bkNn1AK5Nqpjgc7b_PnjdrlI8nmmk0nTUAkh6Y0DhUGx1wfcM8SxCQzYR7D68wP5OF4W5tlwGCHtzc7LfJduidnHQdFPRzrfK2MON_14oA==)
54. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNX4UBTXwOP10bhaJG810f0YHdDXo2CVzy9quf3BZ2ah5GCZ_BI6IblH80FYqmK4rwK2RXvod83Rx6Yu2qlG7-4Kj-34CSTlYZpmFbS4TIeQqc0ufODHK2n5SrKaeUqDm6CYAzphDE)
55. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZGuMWo0nxRlwSdNsGbtIEmw0wLfFhO_dIUTOjGIhr8lvt4BJiRLRZR2IBxpZsPHACLfnqhbWbvjLtGgYNLvd1Coz5Ivk-dCGcGlQgy850lPy0lZMNZPtzvak-K_XCo8REVkYEKInHyXkL3CnPSFKhHlSuSA==)
56. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHvxpaoFT1UO78cLR9JFwA7knjjbLR0LeWBuZMaerkcNoiN_VyW-yCobpcYLZ59kWpnppQOAh3LSq4AuGFtqQbULbW03LQXnAHwiQpEj933KOUytCARyMV5RB79h2reFQ=)
57. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsg6eH3NfiL5uPFrMZaEz-xXY40LCKw07xebjrsDuUHCWMgPZTEERNg9AKbWLmtimdtV2R7yXv46TEO2J2WLoxlTPQffi8IwosL9jCpbyXHc8rodMx39yUSIEEgA5HyIbANlzYZjM6yRF6JUOxF0L1xMIvY13xwYs57TJl8qDkhGUgIA5fZbsnj2MeQAebWbFTTUzd8NTHm7h-dMK1iRDoyEkf3EjdVP96X1Y=)
58. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7h_bUsM0CGgm8_J1ujRNGQt-klU4lJbhgjj2Gs36t6nZ-R-gM61khfhJm6-CAHM7ZUx4Aob95VvD2R4yRb8BSlHW_VKT4fJHkVHc9f5rhNB-P4TVpSO3WR6U0qEXUJDSfJ-o-tq9eaGQnAmG-eibMf0Iqcv-rYMWjUJf08pzTFMy__EixtuoaQSsGzffIIZ_fnefhvTubrr4I5zmhH9sTn-U3A2l25gRmjn2JDiNNmaFP)
59. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVJNhAu3bk55hzIQ4f0LF0kWK7OQFPOPVUYOO7J_glVZ2lZNmLcxif8hTdgviwnnfmTFt3wqi1T4_MYL7EdFmDqTjv75y4LMGvcRlS61Rkm2C87SYnwSrBJwjLIu7EwLKZ6FaDfVabG6cIajVQUh-TKIpUzI44USRAIwoA5A8WPwEsrOurhj_zP8ei-gRc1-vAcY7KmJy5bHxUdcY9JMEcxFJ2tXFEeljUVr8Ghj4wMQLRGsd8Sr420-DugXOZCtOx)
60. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3Yn-w_k2N6wZI5l_VeyvUrV3gJM9WTHKit1tGijJj4k4CGWbc4UQrSYNg6-QhWqIIvkrXJ0TfC-fZsA3sLvmEMMcatwWyenHytHd7LaIIa58TXZcbCUswZcQKYlP5)
61. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9xQ_UL9lr4abdwWmKaQnEh6X1PsBYMcHBSpqFTkg7aCqKd4vIUzsMZYkVMcmRu9lgWZg9bYiWH8iHDzuh2tAIwkbf0HV93DxAX3U-9K0v51CkrjhKKmUrrcLI2PSWK7uP-icqRt6AuRqt)


## Annotations
Annotation(end_index=2155, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBoMKRWoS2SotCla-xFACUn5fSyfaK_ehuVPwDOaq9QLy3WtssnXYEGri1d3QU6ni_7pcg27xSlm7xYIW8-0eKmzZtoNUmOZUp2IBHqIPqTnM_KloEPCO4Z1Ws', start_index=2143)
Annotation(end_index=2155, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs5v2nY0eZk9LvN4GHDES9-DV-_5oRoR2jy80AX9Smatb-o92te_E-ZE89fLI3npRtsTWxLtaMsxYRJpccXY6Vz2xuNL7iMuva7D417iZ4hgT2QRQzD1idGkljJqAIM4Bb2_QOsI3J', start_index=2143)
Annotation(end_index=2741, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUR8B4cGF4r9-4GPV8W23pPvk2Fr3vOztnsUndJ6RrNldAC1BTBB8sE_uDB4geSv_T-sMYfm6EqkCax9Cudd9VAqq89XmddkGbKSTU5mdEqLMfAXS1hgO1OA5Afs0THHfu7AVpan2RUIeMhAMkZuw_V0T8oLTTEp9uwxHsfVzFtdGZISKI5Z_l9GbDJdWiRgT7LNGz1J9FFuwY3xdNR98WI_j6KR55CptXCeI7xpj2tQbQ2V5ttMqcqQ==', start_index=2729)
Annotation(end_index=2741, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVbyKT2FleOlHyko8bU0ifm5ozOydsy1sjRJbADYtey0SQLXG6ToJ26ayPJvWpJ5PQ74vdWpzLi8fefNUQym4NQoIwrZ-x3pHXy_El2fV7WtVyxHXCxM1GS4kqdY4TxBVY32xPXfB0VnI=', start_index=2729)
Annotation(end_index=3017, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBoMKRWoS2SotCla-xFACUn5fSyfaK_ehuVPwDOaq9QLy3WtssnXYEGri1d3QU6ni_7pcg27xSlm7xYIW8-0eKmzZtoNUmOZUp2IBHqIPqTnM_KloEPCO4Z1Ws', start_index=3005)
Annotation(end_index=3017, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFf1zpfQmDMmU9w4zJDC07wn0BVp8BahvuzN4Rcy-OLauGdzDlE5_HvSSUT4ZrP2PpsM4a8CFU8mmag-uGJQMPTzMNB06by0mwZc4iaG2vRMSDHZR77eL8nPtndWXXx', start_index=3005)
Annotation(end_index=3190, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEntSfmDjPFtdudD5FR1hgnvM8stpB7h2aS8DOWYwbFPuWGqEE0DnjtOOP1OsND03f7ICq7NDO6E3dWZ4OGoeky0iaD_WpqvBJ0_EYbk0emrIrqTCJolsCFG1kBWf6qSw==', start_index=3178)
Annotation(end_index=3190, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-9wziRVORtXUllLgclJAl2BvNSpyPxoM4Gk83Mu_iVdY6D6Ql6q9JcosUE49LbeRNCNL_wyYzEnF7DpoavxXEvd51iAuj0LlgweusyT0_uFM263e44XhNygYcCqp6dvoaIUseg6aGK6MlGAYn75qJjV16bpnHUIZ3D3FUXLkmy9nZMXEsoZ_rw-r3SkpXJ9sVqn3vKLb4TLFtOWz7dkyzFH5b5uED7g8sbzpnFjLaeph1K4rx-MC3nmvkSZvfDvr_bA==', start_index=3178)
Annotation(end_index=4546, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgxPE8ZYw7O81yEmdeQ2ngP3KqGdPf5c8wJI-LYLjhTOM6VPAmYQRwc3voTa-laPPu4PN--AdDat3vZMrL5wo5BgmYoYw7mnI9emSmK4SrlbFG2twT0NwS8jCR5nBQ5gZ_avPgWu_qlUhhDMTFNMJo89Zc4qXLXREA4dU6dEWqdHpqojkTRBV2Eb99UVJszvwoybIvZ2J1o8yD0S-INHkJjBazeIhnj63IyOsxogCXJP99NwGjskKazsQTnOlZ0A==', start_index=4537)
Annotation(end_index=5001, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEntSfmDjPFtdudD5FR1hgnvM8stpB7h2aS8DOWYwbFPuWGqEE0DnjtOOP1OsND03f7ICq7NDO6E3dWZ4OGoeky0iaD_WpqvBJ0_EYbk0emrIrqTCJolsCFG1kBWf6qSw==', start_index=4992)
Annotation(end_index=5263, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-9wziRVORtXUllLgclJAl2BvNSpyPxoM4Gk83Mu_iVdY6D6Ql6q9JcosUE49LbeRNCNL_wyYzEnF7DpoavxXEvd51iAuj0LlgweusyT0_uFM263e44XhNygYcCqp6dvoaIUseg6aGK6MlGAYn75qJjV16bpnHUIZ3D3FUXLkmy9nZMXEsoZ_rw-r3SkpXJ9sVqn3vKLb4TLFtOWz7dkyzFH5b5uED7g8sbzpnFjLaeph1K4rx-MC3nmvkSZvfDvr_bA==', start_index=5251)
Annotation(end_index=5263, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3eDwbIoC2R6sx6uUtx7MtlHkL-nkAU2ktGXz0AaZwbUQ41YzmWPRT9psZlXMiWMiCa6U_XK25b-evIbJKjWO0hfEO52uiO41OSU1LdGU3vF9J_FJ8RPTK9qFXLqk-GwuyrwHSv6eLbLuIf0-Ns6Q1pTJq67rSGMXYqK-lPkfbur7UZOrlSuiuNLgM3UtWD2MmUhOR7Ns5HfDHjeXkZYqPwloXBK88l_nd', start_index=5251)
Annotation(end_index=5728, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEntSfmDjPFtdudD5FR1hgnvM8stpB7h2aS8DOWYwbFPuWGqEE0DnjtOOP1OsND03f7ICq7NDO6E3dWZ4OGoeky0iaD_WpqvBJ0_EYbk0emrIrqTCJolsCFG1kBWf6qSw==', start_index=5719)
Annotation(end_index=6591, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxQDBJBi97O8-rrGpqGkKER3vihePckVJblSzGcz9JBVASaAC-w4zxcAuqXFvdASlQmVnbBdJg1ApTwTDgGudjddwM4fZwGrPe2SaaE8-ixaGadXFqyfolBKpFXCU5bSWjXgHat6yS612JH01uaOHqarB3ZbiBKovhWjBfpeFoIlGELQZEve0WXNxm0apn4tp6Lg==', start_index=6581)
Annotation(end_index=7144, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6rT9lMsOxbqf3ewa3AxUHNCFdzWWt_fJHHL53buFjCzEAYa7Im79mQqZOZsM-4UHVTWNBWOSNIw-YqQr4dYAFOnCBwa0gAoOLhBTv2Zxm5XK0KvxagNup_KVDa4PXHBvIWUpciM7Jlj5y1BAW6rqygaPlFA==', start_index=7134)
Annotation(end_index=7303, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxQDBJBi97O8-rrGpqGkKER3vihePckVJblSzGcz9JBVASaAC-w4zxcAuqXFvdASlQmVnbBdJg1ApTwTDgGudjddwM4fZwGrPe2SaaE8-ixaGadXFqyfolBKpFXCU5bSWjXgHat6yS612JH01uaOHqarB3ZbiBKovhWjBfpeFoIlGELQZEve0WXNxm0apn4tp6Lg==', start_index=7293)
Annotation(end_index=7760, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFC-wGeB-hmO_9pot1A8vW55UC1gUS9Zhd266_PGL9KubLaH6bC4KtbOR8LJgnTufEjoj3pFrAa08qhyz6gTOBFk7itNxxs5jGZI5CAnAxb3HaVZu1yq8ybUVSCFXCn0fCPt3sO4P7PaZp0BM30e0k8nwiZPEFjbem4p-bqLFBBkPbVsbwF91c=', start_index=7746)
Annotation(end_index=7760, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGh_LnE5gUitW_ytNtWa1mWur_cJzxkZudk6FNIS-cO6I6cS0epCJ3MTUf20I3JH89kZAxDE0Peld9JVascxrJdomHOD-tpdTco7blH6pHBzwCQs3mYpMPVbYrOpPkAs3Ux5QJyGLAy', start_index=7746)
Annotation(end_index=8024, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1tjO2YRr8P2-PCPlgm0-P452HDUGf6oUk6dqvIcXXqPxerN2t2ZYWQKeUh7n8ziRQnXmG4hAaHc46r6rShsuAljV4ZhLcxbrhpBKQh6g-FXFjuHG6MYQKejwu8BHnHcflTLRKWEtm7YWot670uYOTG-Gjk-mdIemIl5vrJ-fq5PK9UQYbFN-6c8jEirHNfIEnACtYHtb-QwWLr8Yf8WiAk7WJJzKOUDSoKItRDO9uyOtawkxbbi0CRSIAOisXFQ==', start_index=8006)
Annotation(end_index=8024, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFC-wGeB-hmO_9pot1A8vW55UC1gUS9Zhd266_PGL9KubLaH6bC4KtbOR8LJgnTufEjoj3pFrAa08qhyz6gTOBFk7itNxxs5jGZI5CAnAxb3HaVZu1yq8ybUVSCFXCn0fCPt3sO4P7PaZp0BM30e0k8nwiZPEFjbem4p-bqLFBBkPbVsbwF91c=', start_index=8006)
Annotation(end_index=8024, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjW_b0dN2TcDeRqOOgutGnUJQ-gRu6bAqDs8XDcEXEHtjclFX3SZxCpTUloLYINEmOi3hp6RCyOFNYjxwu5aQ7eKU0B8MenuffkGPwDUWKToprzOUoeaxWmDTUtdXhlqMiCuFKkv0V', start_index=8006)
Annotation(end_index=8319, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyfO1lp4G4WzxPYDYO1kvG1-VqXqUsFHiu53GPs9Chs4RyZRmaGksuucNisMN0eruC1-laOjP3isV26q-2dM8N-U7An-8Hp3HaJIBcWi5gz36Autf3VVdk99ryIQ2eF40unMqVdFcOopVr-UfTOrQZabTAbZfXCklHQQ==', start_index=8309)
Annotation(end_index=8760, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2pzspmqRK5cSIUuC97YMHMcFiF4wQV8ARlerWSQrdUe1U8F2UXJ8xS7658jfmyEVOGVF3B5u0ATqWxp7cFNzzJyFMVsnuqmv423Z2qKz6ypaki28oP6IM6O-w63d_Ea3k', start_index=8746)
Annotation(end_index=8760, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHmliFaxQdALf2dTGBv7KLB0OIs9sNcUHoKSRrZBN5_yMYoOwcryye00a5PZ8OAXd3gT6sbii4poQblTDMlLmkVsLaXQHWBcp-LQgEXCJUWNiWw5OPPzWFYyzYPZsZi3NldJqZDDUrjE7xVDs98c-rUtJPoqqjQZo-m9bhbMa44Y2vhvSIezSPO1q5jgd4tQ8zqsRlDoBpi6qXT5H_ro5nfdsfcGWmdl8=', start_index=8746)
Annotation(end_index=9635, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5pd-15tmRiVEr_ys1jc7_g1KlcRRQnaBv8wfcbxtaBNNDQ1hoqB4b59W32uEcvzQluRsqisiaYpygFjDFI7bi3TXwOfpI0MKqQ_XUF_bt1dANMwPpF4HR35ilGA==', start_index=9618)
Annotation(end_index=9635, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBoMKRWoS2SotCla-xFACUn5fSyfaK_ehuVPwDOaq9QLy3WtssnXYEGri1d3QU6ni_7pcg27xSlm7xYIW8-0eKmzZtoNUmOZUp2IBHqIPqTnM_KloEPCO4Z1Ws', start_index=9618)
Annotation(end_index=9635, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5kxI2nqUsJp36B_TSvCMGPm8LslvGOTN5DchxQAxYUvs8OT5MNiywxmOMoPTGD2LlAMhFWjgdHtNFaBtVI3CuPjxy9xuqQX0FMQEZE9ATlkS1ovshInH0q8GW4fqu1EDikZxKbiSSmmK6TaZGQMW7EIxXnj8dzB7AmZaZXn66coK5wkaodw3cwHqLzmr99HSD', start_index=9618)
Annotation(end_index=10099, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5pd-15tmRiVEr_ys1jc7_g1KlcRRQnaBv8wfcbxtaBNNDQ1hoqB4b59W32uEcvzQluRsqisiaYpygFjDFI7bi3TXwOfpI0MKqQ_XUF_bt1dANMwPpF4HR35ilGA==', start_index=10089)
Annotation(end_index=10265, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtQV6ozQsmHMETq9YcHpMbGkA4eqR6A4Kbi8Nnz2yEGjAqaiDAITGdDAUKzZ6SFHL6iocYddT_81BMZG-YWCstWTeY6XBszzXk-TmEK76bQcoD3Dpxz_xMKUcXRvMXbVmF4o2FGsa1Cd3_ZQf0zloqBhjV8QiHKYleudBH_pCrxULlZtjqUer0F_wmx-Q6Kzr5shj1cn73znkfBnfzATEtNibcj2sEzbsy4NwWHIq_sID8zHwp54n5YqwnzF3sqoAgGi807-ISTKPb', start_index=10251)
Annotation(end_index=10265, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXrSj4B1C__NPMPuKoW58WvYSm5iqu-bUkOivBZSfQq1nE-PR_9S9fIU1rfj76do_csW3BNOTapx_dRfrTCEEmh3BKncT53kXlz3n-am6JK-1Yxzr27cIdAmGftw1NsHcy', start_index=10251)
Annotation(end_index=10707, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExB3qvqHdk0oC-eutn3tAinNyEIOluWBTy6TMPO7AClkNtWuPBy669oz55d43GAlGkpFqBOucj3ttu4SWXS7LjkCDBYldp3Pza4-PakTSFwTI0CDyGdEhGsaXir_gGC5VU', start_index=10693)
Annotation(end_index=10707, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXZHVKY4l0pqN6Vtuh8mNB8ZQA9aRlbdgXtkW-8WNicpkwEXs2bdavVlTcD24mFf39ofyvIjKex4yAd0PAVdEAMw02MirttEAjj7-jRspVJVLs4YtX0MMlU-d3tGelloj126QxVkDphw==', start_index=10693)
Annotation(end_index=10991, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExB3qvqHdk0oC-eutn3tAinNyEIOluWBTy6TMPO7AClkNtWuPBy669oz55d43GAlGkpFqBOucj3ttu4SWXS7LjkCDBYldp3Pza4-PakTSFwTI0CDyGdEhGsaXir_gGC5VU', start_index=10973)
Annotation(end_index=10991, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5pd-15tmRiVEr_ys1jc7_g1KlcRRQnaBv8wfcbxtaBNNDQ1hoqB4b59W32uEcvzQluRsqisiaYpygFjDFI7bi3TXwOfpI0MKqQ_XUF_bt1dANMwPpF4HR35ilGA==', start_index=10973)
Annotation(end_index=10991, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLFLqPZsm9guFFz6z4MBIS7D0lQOSsc19o7ApLT34kBhAFIpmc_9YebEOaj1AjvkAXhkud0wrFSWnT4FlGUIXL1K7n_zJU7hIRNzCe5HBjLdEBKkd3GUV4-U6EgfRuy4ro', start_index=10973)
Annotation(end_index=11242, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExB3qvqHdk0oC-eutn3tAinNyEIOluWBTy6TMPO7AClkNtWuPBy669oz55d43GAlGkpFqBOucj3ttu4SWXS7LjkCDBYldp3Pza4-PakTSFwTI0CDyGdEhGsaXir_gGC5VU', start_index=11232)
Annotation(end_index=11634, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExB3qvqHdk0oC-eutn3tAinNyEIOluWBTy6TMPO7AClkNtWuPBy669oz55d43GAlGkpFqBOucj3ttu4SWXS7LjkCDBYldp3Pza4-PakTSFwTI0CDyGdEhGsaXir_gGC5VU', start_index=11620)
Annotation(end_index=11634, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5R27HBBdjKjZ6vOHvtNVZHBJkGEeXV9QoOvgCu8sP-j23wZfRi8IcVpQRyoVu6fNEaasyQI2qHb4but803xigXMD-UZF8YZicGd8X8eSm7iat3tL_9ScXtNX7fbQE6A==', start_index=11620)
Annotation(end_index=11877, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBoMKRWoS2SotCla-xFACUn5fSyfaK_ehuVPwDOaq9QLy3WtssnXYEGri1d3QU6ni_7pcg27xSlm7xYIW8-0eKmzZtoNUmOZUp2IBHqIPqTnM_KloEPCO4Z1Ws', start_index=11864)
Annotation(end_index=11877, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5kxI2nqUsJp36B_TSvCMGPm8LslvGOTN5DchxQAxYUvs8OT5MNiywxmOMoPTGD2LlAMhFWjgdHtNFaBtVI3CuPjxy9xuqQX0FMQEZE9ATlkS1ovshInH0q8GW4fqu1EDikZxKbiSSmmK6TaZGQMW7EIxXnj8dzB7AmZaZXn66coK5wkaodw3cwHqLzmr99HSD', start_index=11864)
Annotation(end_index=12211, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtrdFsq6fMgSmqJCW9RjX52KHekYmPt74vfRwajXRIKcYySNUU_W1IB8y1z_igrCMAIzt_DgITp_Y0CWSGTNU9CncY-rn7FFR0nMEdpoJ6Rwe0Edu9Dav2ZiWoTakcWJXmObW3IlKReZpIT9Kr8kz2qYRNBfpA-RytyOhg', start_index=12201)
Annotation(end_index=12801, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJPZXTQdVJLfQ6xcfZIoLACSOb9r6UOjxRzfngJVN5mpfoEshRaxgK57OAlMLd8_zwcrN8H0eIGbtWoye-xeTYlSs4G6d0pP3QFuHRV-JyMObUdCIQzM5RGNXnSVYaCLRApkeu2pTKGZo4S3kyesbJYiZ1_0UvBPyu9Nb3C9nP4shNyLidJ8wAwXGIRsXdQtmCyYck190Uip3CQn8lSDk0SUpkovaagmz2eVfxUQZvyetbXyC--xQ=', start_index=12787)
Annotation(end_index=12801, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1Enda9sk9QqeX7yUDMHV83B8E5RLKqTWIeJzu-EZ5m-XjJQDBA9n1se_P5PFeQB7PD5kYB8gOIrxbSJyFDyCuFoIeqeaueDTtnNwsi055C0ppcM2LNguaupLdvZHoKlFHG4QW2KRbgCQUJ-CdQir3qZncjS58r5LVjSC52o9k2SpnZb73mnAoX17D5MhETZZkra7pxVeSnsHpPhsWc2_Ow5lrTvKQLJkbly5FLQyUfbzswMs3MiZZaayKpm9HoQh3XQ==', start_index=12787)
Annotation(end_index=13030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQ9yd1M6Ra8971t_IR-Qtle85wDvujVxc9W4gBgLEnW9Kkcp2v0btFczoWhRIoc1Rt4ne9vNb1b9E2mzcPCCBWTA7zIt1BjAuKETyxDH0ZzmsenuOUPxQiP-dFlOSE1QB2carX5SKS3-qJ9t3prxorXSBXbJp0R4NsK9R-b8wWGgz-JWw_5dji48XFZhF7FWGK9lKuDGF4kbKExmuZrH9SHg0froZ-E_wO2wlbklGVx65Oa28dSmCPxwNt', start_index=13020)
Annotation(end_index=13418, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-9wziRVORtXUllLgclJAl2BvNSpyPxoM4Gk83Mu_iVdY6D6Ql6q9JcosUE49LbeRNCNL_wyYzEnF7DpoavxXEvd51iAuj0LlgweusyT0_uFM263e44XhNygYcCqp6dvoaIUseg6aGK6MlGAYn75qJjV16bpnHUIZ3D3FUXLkmy9nZMXEsoZ_rw-r3SkpXJ9sVqn3vKLb4TLFtOWz7dkyzFH5b5uED7g8sbzpnFjLaeph1K4rx-MC3nmvkSZvfDvr_bA==', start_index=13402)
Annotation(end_index=13418, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOdJ_gA81pKdmrLhAy-MN_grMU2w95x6zUm0c_ucMFCgBzWGqzqgPlTA2u1VSsprNLrdnP-McVJv7BUch_-50-35RJjS-XQNlhU04c05zHIaUkZ50vY9nOtxMOsE0c_j1O6ZMSdhZ_Eg65M9R-SCmT5Q26SqFcNbYBm7E=', start_index=13402)
Annotation(end_index=13418, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3eDwbIoC2R6sx6uUtx7MtlHkL-nkAU2ktGXz0AaZwbUQ41YzmWPRT9psZlXMiWMiCa6U_XK25b-evIbJKjWO0hfEO52uiO41OSU1LdGU3vF9J_FJ8RPTK9qFXLqk-GwuyrwHSv6eLbLuIf0-Ns6Q1pTJq67rSGMXYqK-lPkfbur7UZOrlSuiuNLgM3UtWD2MmUhOR7Ns5HfDHjeXkZYqPwloXBK88l_nd', start_index=13402)
Annotation(end_index=13730, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEntSfmDjPFtdudD5FR1hgnvM8stpB7h2aS8DOWYwbFPuWGqEE0DnjtOOP1OsND03f7ICq7NDO6E3dWZ4OGoeky0iaD_WpqvBJ0_EYbk0emrIrqTCJolsCFG1kBWf6qSw==', start_index=13717)
Annotation(end_index=13730, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRsZWmqfbpfrCZgByDjEDMvXeyR8i2_Ritf3zmqdWzRgnigWWz0X87OINJ3-MYQ6lI4KOwa5NO3766KtnI4-9iC2nJBd7cDY-HQGehpo037Ysu-B0sWVONJThfK-70S8h-QD4zeFxCbOaScwycnPZR49cU4paQqJo8CiSLtJVuhT97AkdXaWCqZHjiZG6QmOjmoXXaeYtP7iMHoXTSZgv6-pITNCNOGy9C7AUTz5rKUHNdCVs=', start_index=13717)
Annotation(end_index=13977, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6lUvB1au8xPuNnPMO1nOz3wA6_Rt56AFepZKIIKAnKm5qw4Rg80XBwWREycqv2SiIek-64KYUvsBUNqSnHgg_9jqwmyjXiS_yVlrE5OO8LFkIzGQTVnFfV_FE9mY=', start_index=13963)
Annotation(end_index=13977, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoFuSzJWvXGtYFm4MqWV-aKBpRPhAxLKwlqkLAIMAmfcdIgDRJO69xKqLZq2DYDO1ke46pGDnO1WPsxU9VsG3bPBSxjJYUoC1yqcvs02IxmkjqYP9v3x6_gh3vHxVGh9KFmYrg2CQFxi5IyOQmyNw6G3_a6BT8IkGetiGhDQVb9WLkYEgckjqA8FzpakTPf2LH8vHJVTN5pToP7BtxhnLcvshOsScjNCtif47rrodHrUE_s5aeIrJOYWsIsZfuWbHNlk9i9XpPW8SYm96uunDgN51vo28NbVbCWq5hyQ_3JGdCjJcbtg==', start_index=13963)
Annotation(end_index=14681, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpm-HMBE6pRAoVcc40AIeKYXIjUdrx4uORk31UHjQLrSeZifj6Yr_Xu2n1Pk0mIYWYZ4m054CyyfbtgwYzSKhaoKgD5kqyULNwbWJluqOYkrXwgQkmwJccYWrJNdN-h6qy6T0Y9OTnF2rnaul-Sg90A3-Z0hrWgbJnN6ImQLz_xzN5pjgNs6YTJniwY8GbUYA=', start_index=14667)
Annotation(end_index=14681, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHj76p6F5d0vE3uV49xMKFxehthIaIFqXCm_ILAySTsZnfHyqxsWKiHGFp01giwshsvQ5GgiwBnUlkcriRwE-pT_5PSAVoROd0Y-PnOThnV4fUnahWKkO4aonUFtCIBVfleMeiBqD6MXErTqT4GeMLAS8S4DvQusqNPL7OqATbtHV4jmd4iRu59nmi0HKUd9L2i3P8wItx0P1ya-hFWTpDdqra0cfmK3vVG', start_index=14667)
Annotation(end_index=14960, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDzhBq2goK4UN-HgSL2FjyyB2bWRVYXPHut54XUziS-Dm6I55nda0Y5zPEBsMy3UjbbK3PqMMV0BAF0XRlBvknMXKVWqLO4j0aDzLawloK5OS8rycsXQ==', start_index=14942)
Annotation(end_index=14960, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmOOIEBZJt8tweWKKQA4J985cOkT_pkEUOlnekfPMbBwfBAK1LMYz4poRHyGMRxwjThE8b8FwCirIDrpCMWFDPiRdf7z5ppTCkMR1nS28IL5xRPMytE_Wb5wGssd-I', start_index=14942)
Annotation(end_index=14960, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5UHq27Z1sAhl3tOLzysuqvELhpOcKu29ng3ghYR6odkqPLfZFkBKb_pQUaSQd3g6NE-rgZx5y8f66zgTx_Q-DcwcAcQBB2ductzW9qUGk48lujyQguw==', start_index=14942)
Annotation(end_index=15564, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCk6WcyVmbjFyW6FQ7-_nIJ1HMAP2zcKzilcd_GP5gam0AhauvWNVfOL1-6QmcyRdkdZ1YPPahnmNWlQgElouR3huk25yTKaX5QHX4BCXw1McYgHfTsdjegbxgcZI=', start_index=15542)
Annotation(end_index=15564, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdM6khB14GDFSMqecTio16T1yUb6_UGjJ0bOL3f7shGvxkftQrkX3jANyv1IM1PvpEsh1MxclRGefAPT443atgMgRQpy-VGY-1iTztVShdFLZjnG8vj4g_qMYY3ndDqn0zTC4VQi5ynFoxN7vrjn3S4tFDV1DacuFQCdp2dCb9lsv7WncJggR0i7v06kpzO1O2mZCRu8XWlnX9-z_xJfGhFn_wAIrbi2snTdj8frcMh4ORLX4mfJWvSdlTm83ihBFuXeEvYg==', start_index=15542)
Annotation(end_index=15564, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlVItX5PeN8Jrt4c-0IREojdUSXiPR454tzrMqIs3S19sYh9CPjQmCwkv7VwxVrtlCMRfNSR6YatF8aT6vuGuf7sYMEYXEKpxQQY8BcjlaJZx30FuiQTtgO0G9hmHZ-ICy9pyrqeaCfW-xlugu72Dz', start_index=15542)
Annotation(end_index=15564, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSVD4_qU9iij1AUwKMIVhZ0chYAGfG9LgSA2vmQaAvP7M53yEaIfvbZ05vIIL8LhQ0DBICNWLCmUO6EB8-JPJmI6u4FJLfVcehxTRAQ4RLG4PXg0ot7OSpmaP0Eqhycaa5fItIRj0K56TGWTD8N3tgyIKNcjs4GCz_L4a6nmRMTeoNpq_stYdb4Ve0vphBPCkhSLsBOLdEm8lr4DDeBLPiN6jAFz7mveqcGo2H-_vxMmO66uvtQXow3NG4fRZe20KLSVBby64=', start_index=15542)
Annotation(end_index=15901, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPzKfNgTr2K9u1B0J9j1aUMXTXsCmW5iwXz02JqB6h6aKLjWsI_Bsyioc5I8EeSQJIuq6aXWkcViSBpxB6vSqgA3En3XKSvqH-9O_D2OoBCPegyxI7QzOVgNIzWg-iHg==', start_index=15883)
Annotation(end_index=15901, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG416Sg6WZw3qYhp_qZt3kmT8GPquBWqPA1tOHUtnD3N3AEalJVqraYDN__8zPqY7VEcdpXnua81OD88_CF4mnWISI_2sWnp6DgcnZmYgEbyTsCn-I9f76KVYv5LnyKig==', start_index=15883)
Annotation(end_index=15901, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpm-HMBE6pRAoVcc40AIeKYXIjUdrx4uORk31UHjQLrSeZifj6Yr_Xu2n1Pk0mIYWYZ4m054CyyfbtgwYzSKhaoKgD5kqyULNwbWJluqOYkrXwgQkmwJccYWrJNdN-h6qy6T0Y9OTnF2rnaul-Sg90A3-Z0hrWgbJnN6ImQLz_xzN5pjgNs6YTJniwY8GbUYA=', start_index=15883)
Annotation(end_index=16217, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrbgXnk7-kE97D6PpFoAnxmhRlaI1dHRJHzm3Yp5znllaoAV3XxvDj7mj2yzg7VX8UowserQwIGjlgYM372SxfQbpJlRS2T5FpX7w2DzTc_liKElTHMARktlOF0XhbtIR2XJAyYBUivAJixzw9aTCBfJbZAJWU6FqMvmmnRxfJTcd_-TjlU3KKreV_fpFp1SlDq0MlcMD4S2Z310WmGAnv1vQYMAQJE6_zwnPbR2i0e8VNxcrxw5HCKz-8sI8tnUPZLYeR9OCxAlIlp3ogNYhprY9TyTUyQstKuENgAp1FWnyzyk1oTAZKHkVo47cRcP6U4NZLfaOiaE8VzS8h9vG90yPqoM-ObwNHZRWuJQ==', start_index=16204)
Annotation(end_index=16217, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgxPE8ZYw7O81yEmdeQ2ngP3KqGdPf5c8wJI-LYLjhTOM6VPAmYQRwc3voTa-laPPu4PN--AdDat3vZMrL5wo5BgmYoYw7mnI9emSmK4SrlbFG2twT0NwS8jCR5nBQ5gZ_avPgWu_qlUhhDMTFNMJo89Zc4qXLXREA4dU6dEWqdHpqojkTRBV2Eb99UVJszvwoybIvZ2J1o8yD0S-INHkJjBazeIhnj63IyOsxogCXJP99NwGjskKazsQTnOlZ0A==', start_index=16204)
Annotation(end_index=16807, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAHmO1VKjvZJ8yqO0nCa0fr516nMiw7KxfzsTglWFQYx9GUhM0vWEAwdjAJeiiMQoLlb7ROvloI-6Id7HIQmkH03fmM0WLKwq-mkU1HWfKW4d5b3i6PzvuC1sNAD_P7KXYruEah6aw', start_index=16793)
Annotation(end_index=16807, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEDFtUwPbhaFuhUwlVqzPEUOoTNgf0I1Vajt_BbP9Es2fSNNKwZ9O1G62U2ZrdA2QXLNI1agApj7o1XFH-TlWjiv17OLLXvinF3pPKcZtX5IHPpBShBKnh2o65KzHBgqSio4qDM74aSg==', start_index=16793)
Annotation(end_index=17131, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpOdLKzIbBFAm_bxPqhAMaseFX9lkinhWOL3TyAKv9mVlp-qCPhcOOWzzIvWpAieMvH_m9l_VCYY5o0sZ3_qdTJpNJ1gNH-OIl7Uig7tc_i1uqhmxNqgLiq4rUw7Z2cPhf2_ODZYZDjqANXb-NY1CNFDaEfcbBMMn_DUqTzwTpHjhQQh-98DrIFECWygaU-Mwg0q7UysFDMT5mxfRA4-dCXA5xVyooGJonCPXNdsE4BAaq', start_index=17117)
Annotation(end_index=17131, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlPJAeuSorO_whLwG5jo3hgNSCdhX8LN04ZNovYXnmnsl5XeArKenomv86ualWUKNAfB5qIK9453HtZ64DWYxinQqZGacd2fivv6NDT2ixdyI3RVSxRidTgqNErzUwVh4EovA5zh90faAzT17hywUMtIpfGc_RzmnNVQSc-Tm2pie2hrSV40GuLzAX9sSYGwstaw==', start_index=17117)
Annotation(end_index=17533, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxQDBJBi97O8-rrGpqGkKER3vihePckVJblSzGcz9JBVASaAC-w4zxcAuqXFvdASlQmVnbBdJg1ApTwTDgGudjddwM4fZwGrPe2SaaE8-ixaGadXFqyfolBKpFXCU5bSWjXgHat6yS612JH01uaOHqarB3ZbiBKovhWjBfpeFoIlGELQZEve0WXNxm0apn4tp6Lg==', start_index=17523)
Annotation(end_index=17936, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuQkK69UpBpH7OZxfIgBLYAUTAOcunjqmt_5Yfl-lVHDAXYHht9yPqc8xQLDoZxFp_99YkKTskJf1gxf9Jy96lJeym2-okbyNET5IblOwbg4wJarZMeW--I0z85R-KVWtM_qFfRe6JLIplGqzby9tR4v-Gc2uLW8C6daM=', start_index=17926)
Annotation(end_index=18261, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHmliFaxQdALf2dTGBv7KLB0OIs9sNcUHoKSRrZBN5_yMYoOwcryye00a5PZ8OAXd3gT6sbii4poQblTDMlLmkVsLaXQHWBcp-LQgEXCJUWNiWw5OPPzWFYyzYPZsZi3NldJqZDDUrjE7xVDs98c-rUtJPoqqjQZo-m9bhbMa44Y2vhvSIezSPO1q5jgd4tQ8zqsRlDoBpi6qXT5H_ro5nfdsfcGWmdl8=', start_index=18251)
Annotation(end_index=18472, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFC-wGeB-hmO_9pot1A8vW55UC1gUS9Zhd266_PGL9KubLaH6bC4KtbOR8LJgnTufEjoj3pFrAa08qhyz6gTOBFk7itNxxs5jGZI5CAnAxb3HaVZu1yq8ybUVSCFXCn0fCPt3sO4P7PaZp0BM30e0k8nwiZPEFjbem4p-bqLFBBkPbVsbwF91c=', start_index=18458)
Annotation(end_index=18472, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjW_b0dN2TcDeRqOOgutGnUJQ-gRu6bAqDs8XDcEXEHtjclFX3SZxCpTUloLYINEmOi3hp6RCyOFNYjxwu5aQ7eKU0B8MenuffkGPwDUWKToprzOUoeaxWmDTUtdXhlqMiCuFKkv0V', start_index=18458)
Annotation(end_index=19173, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExB3qvqHdk0oC-eutn3tAinNyEIOluWBTy6TMPO7AClkNtWuPBy669oz55d43GAlGkpFqBOucj3ttu4SWXS7LjkCDBYldp3Pza4-PakTSFwTI0CDyGdEhGsaXir_gGC5VU', start_index=19159)
Annotation(end_index=19173, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXZHVKY4l0pqN6Vtuh8mNB8ZQA9aRlbdgXtkW-8WNicpkwEXs2bdavVlTcD24mFf39ofyvIjKex4yAd0PAVdEAMw02MirttEAjj7-jRspVJVLs4YtX0MMlU-d3tGelloj126QxVkDphw==', start_index=19159)
Annotation(end_index=19342, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxQDBJBi97O8-rrGpqGkKER3vihePckVJblSzGcz9JBVASaAC-w4zxcAuqXFvdASlQmVnbBdJg1ApTwTDgGudjddwM4fZwGrPe2SaaE8-ixaGadXFqyfolBKpFXCU5bSWjXgHat6yS612JH01uaOHqarB3ZbiBKovhWjBfpeFoIlGELQZEve0WXNxm0apn4tp6Lg==', start_index=19332)
Annotation(end_index=19574, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdM6khB14GDFSMqecTio16T1yUb6_UGjJ0bOL3f7shGvxkftQrkX3jANyv1IM1PvpEsh1MxclRGefAPT443atgMgRQpy-VGY-1iTztVShdFLZjnG8vj4g_qMYY3ndDqn0zTC4VQi5ynFoxN7vrjn3S4tFDV1DacuFQCdp2dCb9lsv7WncJggR0i7v06kpzO1O2mZCRu8XWlnX9-z_xJfGhFn_wAIrbi2snTdj8frcMh4ORLX4mfJWvSdlTm83ihBFuXeEvYg==', start_index=19560)
Annotation(end_index=19574, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG416Sg6WZw3qYhp_qZt3kmT8GPquBWqPA1tOHUtnD3N3AEalJVqraYDN__8zPqY7VEcdpXnua81OD88_CF4mnWISI_2sWnp6DgcnZmYgEbyTsCn-I9f76KVYv5LnyKig==', start_index=19560)
Annotation(end_index=19792, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAHmO1VKjvZJ8yqO0nCa0fr516nMiw7KxfzsTglWFQYx9GUhM0vWEAwdjAJeiiMQoLlb7ROvloI-6Id7HIQmkH03fmM0WLKwq-mkU1HWfKW4d5b3i6PzvuC1sNAD_P7KXYruEah6aw', start_index=19778)
Annotation(end_index=19792, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEDFtUwPbhaFuhUwlVqzPEUOoTNgf0I1Vajt_BbP9Es2fSNNKwZ9O1G62U2ZrdA2QXLNI1agApj7o1XFH-TlWjiv17OLLXvinF3pPKcZtX5IHPpBShBKnh2o65KzHBgqSio4qDM74aSg==', start_index=19778)
Annotation(end_index=20073, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBoMKRWoS2SotCla-xFACUn5fSyfaK_ehuVPwDOaq9QLy3WtssnXYEGri1d3QU6ni_7pcg27xSlm7xYIW8-0eKmzZtoNUmOZUp2IBHqIPqTnM_KloEPCO4Z1Ws', start_index=20064)
Annotation(end_index=20168, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXZFym5-wn_5WWIM1yepvw1k4y23MVw29_M9vc13UA9300xDKzryURncGWzNmfb0ry_DwFLerP-3hbBpvqJwZcfVMRw90ZtjpkOrXyN_KlAbNMr_BXyJOFYRZR9UzHQiMBPIFZ_AmuboKqZEw-DybsOlpa4rmXnLP64yWjS_lSe9hkdCy95bWh-6zUjO5lhsAXkTaMXbF0vHsl5i4o-Kxm04vWYwyZnyZ7uVhp', start_index=20158)
Annotation(end_index=20258, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQ9yd1M6Ra8971t_IR-Qtle85wDvujVxc9W4gBgLEnW9Kkcp2v0btFczoWhRIoc1Rt4ne9vNb1b9E2mzcPCCBWTA7zIt1BjAuKETyxDH0ZzmsenuOUPxQiP-dFlOSE1QB2carX5SKS3-qJ9t3prxorXSBXbJp0R4NsK9R-b8wWGgz-JWw_5dji48XFZhF7FWGK9lKuDGF4kbKExmuZrH9SHg0froZ-E_wO2wlbklGVx65Oa28dSmCPxwNt', start_index=20248)
Annotation(end_index=20359, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFf1zpfQmDMmU9w4zJDC07wn0BVp8BahvuzN4Rcy-OLauGdzDlE5_HvSSUT4ZrP2PpsM4a8CFU8mmag-uGJQMPTzMNB06by0mwZc4iaG2vRMSDHZR77eL8nPtndWXXx', start_index=20350)
Annotation(end_index=20437, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUR8B4cGF4r9-4GPV8W23pPvk2Fr3vOztnsUndJ6RrNldAC1BTBB8sE_uDB4geSv_T-sMYfm6EqkCax9Cudd9VAqq89XmddkGbKSTU5mdEqLMfAXS1hgO1OA5Afs0THHfu7AVpan2RUIeMhAMkZuw_V0T8oLTTEp9uwxHsfVzFtdGZISKI5Z_l9GbDJdWiRgT7LNGz1J9FFuwY3xdNR98WI_j6KR55CptXCeI7xpj2tQbQ2V5ttMqcqQ==', start_index=20428)
Annotation(end_index=20520, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPzKfNgTr2K9u1B0J9j1aUMXTXsCmW5iwXz02JqB6h6aKLjWsI_Bsyioc5I8EeSQJIuq6aXWkcViSBpxB6vSqgA3En3XKSvqH-9O_D2OoBCPegyxI7QzOVgNIzWg-iHg==', start_index=20510)
Annotation(end_index=20617, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs5v2nY0eZk9LvN4GHDES9-DV-_5oRoR2jy80AX9Smatb-o92te_E-ZE89fLI3npRtsTWxLtaMsxYRJpccXY6Vz2xuNL7iMuva7D417iZ4hgT2QRQzD1idGkljJqAIM4Bb2_QOsI3J', start_index=20608)
Annotation(end_index=20690, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVbyKT2FleOlHyko8bU0ifm5ozOydsy1sjRJbADYtey0SQLXG6ToJ26ayPJvWpJ5PQ74vdWpzLi8fefNUQym4NQoIwrZ-x3pHXy_El2fV7WtVyxHXCxM1GS4kqdY4TxBVY32xPXfB0VnI=', start_index=20681)
Annotation(end_index=20768, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHj76p6F5d0vE3uV49xMKFxehthIaIFqXCm_ILAySTsZnfHyqxsWKiHGFp01giwshsvQ5GgiwBnUlkcriRwE-pT_5PSAVoROd0Y-PnOThnV4fUnahWKkO4aonUFtCIBVfleMeiBqD6MXErTqT4GeMLAS8S4DvQusqNPL7OqATbtHV4jmd4iRu59nmi0HKUd9L2i3P8wItx0P1ya-hFWTpDdqra0cfmK3vVG', start_index=20758)
Annotation(end_index=20865, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5kxI2nqUsJp36B_TSvCMGPm8LslvGOTN5DchxQAxYUvs8OT5MNiywxmOMoPTGD2LlAMhFWjgdHtNFaBtVI3CuPjxy9xuqQX0FMQEZE9ATlkS1ovshInH0q8GW4fqu1EDikZxKbiSSmmK6TaZGQMW7EIxXnj8dzB7AmZaZXn66coK5wkaodw3cwHqLzmr99HSD', start_index=20855)
Annotation(end_index=20945, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5R27HBBdjKjZ6vOHvtNVZHBJkGEeXV9QoOvgCu8sP-j23wZfRi8IcVpQRyoVu6fNEaasyQI2qHb4but803xigXMD-UZF8YZicGd8X8eSm7iat3tL_9ScXtNX7fbQE6A==', start_index=20935)
Annotation(end_index=21017, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExB3qvqHdk0oC-eutn3tAinNyEIOluWBTy6TMPO7AClkNtWuPBy669oz55d43GAlGkpFqBOucj3ttu4SWXS7LjkCDBYldp3Pza4-PakTSFwTI0CDyGdEhGsaXir_gGC5VU', start_index=21007)
Annotation(end_index=21089, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHU0ZJr3MvBY-9HxuE7bkNn1AK5Nqpjgc7b_PnjdrlI8nmmk0nTUAkh6Y0DhUGx1wfcM8SxCQzYR7D68wP5OF4W5tlwGCHtzc7LfJduidnHQdFPRzrfK2MON_14oA==', start_index=21079)
Annotation(end_index=21160, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-9wziRVORtXUllLgclJAl2BvNSpyPxoM4Gk83Mu_iVdY6D6Ql6q9JcosUE49LbeRNCNL_wyYzEnF7DpoavxXEvd51iAuj0LlgweusyT0_uFM263e44XhNygYcCqp6dvoaIUseg6aGK6MlGAYn75qJjV16bpnHUIZ3D3FUXLkmy9nZMXEsoZ_rw-r3SkpXJ9sVqn3vKLb4TLFtOWz7dkyzFH5b5uED7g8sbzpnFjLaeph1K4rx-MC3nmvkSZvfDvr_bA==', start_index=21151)
Annotation(end_index=21246, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3eDwbIoC2R6sx6uUtx7MtlHkL-nkAU2ktGXz0AaZwbUQ41YzmWPRT9psZlXMiWMiCa6U_XK25b-evIbJKjWO0hfEO52uiO41OSU1LdGU3vF9J_FJ8RPTK9qFXLqk-GwuyrwHSv6eLbLuIf0-Ns6Q1pTJq67rSGMXYqK-lPkfbur7UZOrlSuiuNLgM3UtWD2MmUhOR7Ns5HfDHjeXkZYqPwloXBK88l_nd', start_index=21237)
Annotation(end_index=21332, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNX4UBTXwOP10bhaJG810f0YHdDXo2CVzy9quf3BZ2ah5GCZ_BI6IblH80FYqmK4rwK2RXvod83Rx6Yu2qlG7-4Kj-34CSTlYZpmFbS4TIeQqc0ufODHK2n5SrKaeUqDm6CYAzphDE', start_index=21322)
Annotation(end_index=21405, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZGuMWo0nxRlwSdNsGbtIEmw0wLfFhO_dIUTOjGIhr8lvt4BJiRLRZR2IBxpZsPHACLfnqhbWbvjLtGgYNLvd1Coz5Ivk-dCGcGlQgy850lPy0lZMNZPtzvak-K_XCo8REVkYEKInHyXkL3CnPSFKhHlSuSA==', start_index=21395)
Annotation(end_index=21483, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdM6khB14GDFSMqecTio16T1yUb6_UGjJ0bOL3f7shGvxkftQrkX3jANyv1IM1PvpEsh1MxclRGefAPT443atgMgRQpy-VGY-1iTztVShdFLZjnG8vj4g_qMYY3ndDqn0zTC4VQi5ynFoxN7vrjn3S4tFDV1DacuFQCdp2dCb9lsv7WncJggR0i7v06kpzO1O2mZCRu8XWlnX9-z_xJfGhFn_wAIrbi2snTdj8frcMh4ORLX4mfJWvSdlTm83ihBFuXeEvYg==', start_index=21473)
Annotation(end_index=21573, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlVItX5PeN8Jrt4c-0IREojdUSXiPR454tzrMqIs3S19sYh9CPjQmCwkv7VwxVrtlCMRfNSR6YatF8aT6vuGuf7sYMEYXEKpxQQY8BcjlaJZx30FuiQTtgO0G9hmHZ-ICy9pyrqeaCfW-xlugu72Dz', start_index=21563)
Annotation(end_index=21649, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG416Sg6WZw3qYhp_qZt3kmT8GPquBWqPA1tOHUtnD3N3AEalJVqraYDN__8zPqY7VEcdpXnua81OD88_CF4mnWISI_2sWnp6DgcnZmYgEbyTsCn-I9f76KVYv5LnyKig==', start_index=21639)
Annotation(end_index=21737, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxQDBJBi97O8-rrGpqGkKER3vihePckVJblSzGcz9JBVASaAC-w4zxcAuqXFvdASlQmVnbBdJg1ApTwTDgGudjddwM4fZwGrPe2SaaE8-ixaGadXFqyfolBKpFXCU5bSWjXgHat6yS612JH01uaOHqarB3ZbiBKovhWjBfpeFoIlGELQZEve0WXNxm0apn4tp6Lg==', start_index=21727)
Annotation(end_index=21805, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEntSfmDjPFtdudD5FR1hgnvM8stpB7h2aS8DOWYwbFPuWGqEE0DnjtOOP1OsND03f7ICq7NDO6E3dWZ4OGoeky0iaD_WpqvBJ0_EYbk0emrIrqTCJolsCFG1kBWf6qSw==', start_index=21796)
Annotation(end_index=21887, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHvxpaoFT1UO78cLR9JFwA7knjjbLR0LeWBuZMaerkcNoiN_VyW-yCobpcYLZ59kWpnppQOAh3LSq4AuGFtqQbULbW03LQXnAHwiQpEj933KOUytCARyMV5RB79h2reFQ=', start_index=21877)
Annotation(end_index=21968, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRsZWmqfbpfrCZgByDjEDMvXeyR8i2_Ritf3zmqdWzRgnigWWz0X87OINJ3-MYQ6lI4KOwa5NO3766KtnI4-9iC2nJBd7cDY-HQGehpo037Ysu-B0sWVONJThfK-70S8h-QD4zeFxCbOaScwycnPZR49cU4paQqJo8CiSLtJVuhT97AkdXaWCqZHjiZG6QmOjmoXXaeYtP7iMHoXTSZgv6-pITNCNOGy9C7AUTz5rKUHNdCVs=', start_index=21958)
Annotation(end_index=22052, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1Enda9sk9QqeX7yUDMHV83B8E5RLKqTWIeJzu-EZ5m-XjJQDBA9n1se_P5PFeQB7PD5kYB8gOIrxbSJyFDyCuFoIeqeaueDTtnNwsi055C0ppcM2LNguaupLdvZHoKlFHG4QW2KRbgCQUJ-CdQir3qZncjS58r5LVjSC52o9k2SpnZb73mnAoX17D5MhETZZkra7pxVeSnsHpPhsWc2_Ow5lrTvKQLJkbly5FLQyUfbzswMs3MiZZaayKpm9HoQh3XQ==', start_index=22042)
Annotation(end_index=22140, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGh_LnE5gUitW_ytNtWa1mWur_cJzxkZudk6FNIS-cO6I6cS0epCJ3MTUf20I3JH89kZAxDE0Peld9JVascxrJdomHOD-tpdTco7blH6pHBzwCQs3mYpMPVbYrOpPkAs3Ux5QJyGLAy', start_index=22130)
Annotation(end_index=22209, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSVD4_qU9iij1AUwKMIVhZ0chYAGfG9LgSA2vmQaAvP7M53yEaIfvbZ05vIIL8LhQ0DBICNWLCmUO6EB8-JPJmI6u4FJLfVcehxTRAQ4RLG4PXg0ot7OSpmaP0Eqhycaa5fItIRj0K56TGWTD8N3tgyIKNcjs4GCz_L4a6nmRMTeoNpq_stYdb4Ve0vphBPCkhSLsBOLdEm8lr4DDeBLPiN6jAFz7mveqcGo2H-_vxMmO66uvtQXow3NG4fRZe20KLSVBby64=', start_index=22199)
Annotation(end_index=22305, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHmliFaxQdALf2dTGBv7KLB0OIs9sNcUHoKSRrZBN5_yMYoOwcryye00a5PZ8OAXd3gT6sbii4poQblTDMlLmkVsLaXQHWBcp-LQgEXCJUWNiWw5OPPzWFYyzYPZsZi3NldJqZDDUrjE7xVDs98c-rUtJPoqqjQZo-m9bhbMa44Y2vhvSIezSPO1q5jgd4tQ8zqsRlDoBpi6qXT5H_ro5nfdsfcGWmdl8=', start_index=22295)
Annotation(end_index=22390, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFC-wGeB-hmO_9pot1A8vW55UC1gUS9Zhd266_PGL9KubLaH6bC4KtbOR8LJgnTufEjoj3pFrAa08qhyz6gTOBFk7itNxxs5jGZI5CAnAxb3HaVZu1yq8ybUVSCFXCn0fCPt3sO4P7PaZp0BM30e0k8nwiZPEFjbem4p-bqLFBBkPbVsbwF91c=', start_index=22380)
Annotation(end_index=22475, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxQDBJBi97O8-rrGpqGkKER3vihePckVJblSzGcz9JBVASaAC-w4zxcAuqXFvdASlQmVnbBdJg1ApTwTDgGudjddwM4fZwGrPe2SaaE8-ixaGadXFqyfolBKpFXCU5bSWjXgHat6yS612JH01uaOHqarB3ZbiBKovhWjBfpeFoIlGELQZEve0WXNxm0apn4tp6Lg==', start_index=22465)
Annotation(end_index=22549, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6rT9lMsOxbqf3ewa3AxUHNCFdzWWt_fJHHL53buFjCzEAYa7Im79mQqZOZsM-4UHVTWNBWOSNIw-YqQr4dYAFOnCBwa0gAoOLhBTv2Zxm5XK0KvxagNup_KVDa4PXHBvIWUpciM7Jlj5y1BAW6rqygaPlFA==', start_index=22539)
Annotation(end_index=22610, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpm-HMBE6pRAoVcc40AIeKYXIjUdrx4uORk31UHjQLrSeZifj6Yr_Xu2n1Pk0mIYWYZ4m054CyyfbtgwYzSKhaoKgD5kqyULNwbWJluqOYkrXwgQkmwJccYWrJNdN-h6qy6T0Y9OTnF2rnaul-Sg90A3-Z0hrWgbJnN6ImQLz_xzN5pjgNs6YTJniwY8GbUYA=', start_index=22600)
Annotation(end_index=22687, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsg6eH3NfiL5uPFrMZaEz-xXY40LCKw07xebjrsDuUHCWMgPZTEERNg9AKbWLmtimdtV2R7yXv46TEO2J2WLoxlTPQffi8IwosL9jCpbyXHc8rodMx39yUSIEEgA5HyIbANlzYZjM6yRF6JUOxF0L1xMIvY13xwYs57TJl8qDkhGUgIA5fZbsnj2MeQAebWbFTTUzd8NTHm7h-dMK1iRDoyEkf3EjdVP96X1Y=', start_index=22677)
Annotation(end_index=22775, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDzhBq2goK4UN-HgSL2FjyyB2bWRVYXPHut54XUziS-Dm6I55nda0Y5zPEBsMy3UjbbK3PqMMV0BAF0XRlBvknMXKVWqLO4j0aDzLawloK5OS8rycsXQ==', start_index=22765)
Annotation(end_index=22841, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtrdFsq6fMgSmqJCW9RjX52KHekYmPt74vfRwajXRIKcYySNUU_W1IB8y1z_igrCMAIzt_DgITp_Y0CWSGTNU9CncY-rn7FFR0nMEdpoJ6Rwe0Edu9Dav2ZiWoTakcWJXmObW3IlKReZpIT9Kr8kz2qYRNBfpA-RytyOhg', start_index=22831)
Annotation(end_index=22921, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOdJ_gA81pKdmrLhAy-MN_grMU2w95x6zUm0c_ucMFCgBzWGqzqgPlTA2u1VSsprNLrdnP-McVJv7BUch_-50-35RJjS-XQNlhU04c05zHIaUkZ50vY9nOtxMOsE0c_j1O6ZMSdhZ_Eg65M9R-SCmT5Q26SqFcNbYBm7E=', start_index=22911)
Annotation(end_index=22997, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6lUvB1au8xPuNnPMO1nOz3wA6_Rt56AFepZKIIKAnKm5qw4Rg80XBwWREycqv2SiIek-64KYUvsBUNqSnHgg_9jqwmyjXiS_yVlrE5OO8LFkIzGQTVnFfV_FE9mY=', start_index=22987)
Annotation(end_index=23066, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoFuSzJWvXGtYFm4MqWV-aKBpRPhAxLKwlqkLAIMAmfcdIgDRJO69xKqLZq2DYDO1ke46pGDnO1WPsxU9VsG3bPBSxjJYUoC1yqcvs02IxmkjqYP9v3x6_gh3vHxVGh9KFmYrg2CQFxi5IyOQmyNw6G3_a6BT8IkGetiGhDQVb9WLkYEgckjqA8FzpakTPf2LH8vHJVTN5pToP7BtxhnLcvshOsScjNCtif47rrodHrUE_s5aeIrJOYWsIsZfuWbHNlk9i9XpPW8SYm96uunDgN51vo28NbVbCWq5hyQ_3JGdCjJcbtg==', start_index=23056)
Annotation(end_index=23152, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2pzspmqRK5cSIUuC97YMHMcFiF4wQV8ARlerWSQrdUe1U8F2UXJ8xS7658jfmyEVOGVF3B5u0ATqWxp7cFNzzJyFMVsnuqmv423Z2qKz6ypaki28oP6IM6O-w63d_Ea3k', start_index=23142)
Annotation(end_index=23209, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjW_b0dN2TcDeRqOOgutGnUJQ-gRu6bAqDs8XDcEXEHtjclFX3SZxCpTUloLYINEmOi3hp6RCyOFNYjxwu5aQ7eKU0B8MenuffkGPwDUWKToprzOUoeaxWmDTUtdXhlqMiCuFKkv0V', start_index=23199)
Annotation(end_index=23285, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1tjO2YRr8P2-PCPlgm0-P452HDUGf6oUk6dqvIcXXqPxerN2t2ZYWQKeUh7n8ziRQnXmG4hAaHc46r6rShsuAljV4ZhLcxbrhpBKQh6g-FXFjuHG6MYQKejwu8BHnHcflTLRKWEtm7YWot670uYOTG-Gjk-mdIemIl5vrJ-fq5PK9UQYbFN-6c8jEirHNfIEnACtYHtb-QwWLr8Yf8WiAk7WJJzKOUDSoKItRDO9uyOtawkxbbi0CRSIAOisXFQ==', start_index=23275)
Annotation(end_index=23349, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyfO1lp4G4WzxPYDYO1kvG1-VqXqUsFHiu53GPs9Chs4RyZRmaGksuucNisMN0eruC1-laOjP3isV26q-2dM8N-U7An-8Hp3HaJIBcWi5gz36Autf3VVdk99ryIQ2eF40unMqVdFcOopVr-UfTOrQZabTAbZfXCklHQQ==', start_index=23339)
Annotation(end_index=23410, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtQV6ozQsmHMETq9YcHpMbGkA4eqR6A4Kbi8Nnz2yEGjAqaiDAITGdDAUKzZ6SFHL6iocYddT_81BMZG-YWCstWTeY6XBszzXk-TmEK76bQcoD3Dpxz_xMKUcXRvMXbVmF4o2FGsa1Cd3_ZQf0zloqBhjV8QiHKYleudBH_pCrxULlZtjqUer0F_wmx-Q6Kzr5shj1cn73znkfBnfzATEtNibcj2sEzbsy4NwWHIq_sID8zHwp54n5YqwnzF3sqoAgGi807-ISTKPb', start_index=23400)
Annotation(end_index=23486, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXrSj4B1C__NPMPuKoW58WvYSm5iqu-bUkOivBZSfQq1nE-PR_9S9fIU1rfj76do_csW3BNOTapx_dRfrTCEEmh3BKncT53kXlz3n-am6JK-1Yxzr27cIdAmGftw1NsHcy', start_index=23476)
Annotation(end_index=23573, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7h_bUsM0CGgm8_J1ujRNGQt-klU4lJbhgjj2Gs36t6nZ-R-gM61khfhJm6-CAHM7ZUx4Aob95VvD2R4yRb8BSlHW_VKT4fJHkVHc9f5rhNB-P4TVpSO3WR6U0qEXUJDSfJ-o-tq9eaGQnAmG-eibMf0Iqcv-rYMWjUJf08pzTFMy__EixtuoaQSsGzffIIZ_fnefhvTubrr4I5zmhH9sTn-U3A2l25gRmjn2JDiNNmaFP', start_index=23563)
Annotation(end_index=23639, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5pd-15tmRiVEr_ys1jc7_g1KlcRRQnaBv8wfcbxtaBNNDQ1hoqB4b59W32uEcvzQluRsqisiaYpygFjDFI7bi3TXwOfpI0MKqQ_XUF_bt1dANMwPpF4HR35ilGA==', start_index=23629)
Annotation(end_index=23709, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5UHq27Z1sAhl3tOLzysuqvELhpOcKu29ng3ghYR6odkqPLfZFkBKb_pQUaSQd3g6NE-rgZx5y8f66zgTx_Q-DcwcAcQBB2ductzW9qUGk48lujyQguw==', start_index=23699)
Annotation(end_index=23779, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlPJAeuSorO_whLwG5jo3hgNSCdhX8LN04ZNovYXnmnsl5XeArKenomv86ualWUKNAfB5qIK9453HtZ64DWYxinQqZGacd2fivv6NDT2ixdyI3RVSxRidTgqNErzUwVh4EovA5zh90faAzT17hywUMtIpfGc_RzmnNVQSc-Tm2pie2hrSV40GuLzAX9sSYGwstaw==', start_index=23769)
Annotation(end_index=23845, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAHmO1VKjvZJ8yqO0nCa0fr516nMiw7KxfzsTglWFQYx9GUhM0vWEAwdjAJeiiMQoLlb7ROvloI-6Id7HIQmkH03fmM0WLKwq-mkU1HWfKW4d5b3i6PzvuC1sNAD_P7KXYruEah6aw', start_index=23835)
Annotation(end_index=23923, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmOOIEBZJt8tweWKKQA4J985cOkT_pkEUOlnekfPMbBwfBAK1LMYz4poRHyGMRxwjThE8b8FwCirIDrpCMWFDPiRdf7z5ppTCkMR1nS28IL5xRPMytE_Wb5wGssd-I', start_index=23913)
Annotation(end_index=23998, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgxPE8ZYw7O81yEmdeQ2ngP3KqGdPf5c8wJI-LYLjhTOM6VPAmYQRwc3voTa-laPPu4PN--AdDat3vZMrL5wo5BgmYoYw7mnI9emSmK4SrlbFG2twT0NwS8jCR5nBQ5gZ_avPgWu_qlUhhDMTFNMJo89Zc4qXLXREA4dU6dEWqdHpqojkTRBV2Eb99UVJszvwoybIvZ2J1o8yD0S-INHkJjBazeIhnj63IyOsxogCXJP99NwGjskKazsQTnOlZ0A==', start_index=23989)
Annotation(end_index=24082, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCk6WcyVmbjFyW6FQ7-_nIJ1HMAP2zcKzilcd_GP5gam0AhauvWNVfOL1-6QmcyRdkdZ1YPPahnmNWlQgElouR3huk25yTKaX5QHX4BCXw1McYgHfTsdjegbxgcZI=', start_index=24072)
Annotation(end_index=24160, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrbgXnk7-kE97D6PpFoAnxmhRlaI1dHRJHzm3Yp5znllaoAV3XxvDj7mj2yzg7VX8UowserQwIGjlgYM372SxfQbpJlRS2T5FpX7w2DzTc_liKElTHMARktlOF0XhbtIR2XJAyYBUivAJixzw9aTCBfJbZAJWU6FqMvmmnRxfJTcd_-TjlU3KKreV_fpFp1SlDq0MlcMD4S2Z310WmGAnv1vQYMAQJE6_zwnPbR2i0e8VNxcrxw5HCKz-8sI8tnUPZLYeR9OCxAlIlp3ogNYhprY9TyTUyQstKuENgAp1FWnyzyk1oTAZKHkVo47cRcP6U4NZLfaOiaE8VzS8h9vG90yPqoM-ObwNHZRWuJQ==', start_index=24150)
Annotation(end_index=24235, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVJNhAu3bk55hzIQ4f0LF0kWK7OQFPOPVUYOO7J_glVZ2lZNmLcxif8hTdgviwnnfmTFt3wqi1T4_MYL7EdFmDqTjv75y4LMGvcRlS61Rkm2C87SYnwSrBJwjLIu7EwLKZ6FaDfVabG6cIajVQUh-TKIpUzI44USRAIwoA5A8WPwEsrOurhj_zP8ei-gRc1-vAcY7KmJy5bHxUdcY9JMEcxFJ2tXFEeljUVr8Ghj4wMQLRGsd8Sr420-DugXOZCtOx', start_index=24225)
Annotation(end_index=24316, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuQkK69UpBpH7OZxfIgBLYAUTAOcunjqmt_5Yfl-lVHDAXYHht9yPqc8xQLDoZxFp_99YkKTskJf1gxf9Jy96lJeym2-okbyNET5IblOwbg4wJarZMeW--I0z85R-KVWtM_qFfRe6JLIplGqzby9tR4v-Gc2uLW8C6daM=', start_index=24306)
Annotation(end_index=24386, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6rT9lMsOxbqf3ewa3AxUHNCFdzWWt_fJHHL53buFjCzEAYa7Im79mQqZOZsM-4UHVTWNBWOSNIw-YqQr4dYAFOnCBwa0gAoOLhBTv2Zxm5XK0KvxagNup_KVDa4PXHBvIWUpciM7Jlj5y1BAW6rqygaPlFA==', start_index=24376)
Annotation(end_index=24456, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXZHVKY4l0pqN6Vtuh8mNB8ZQA9aRlbdgXtkW-8WNicpkwEXs2bdavVlTcD24mFf39ofyvIjKex4yAd0PAVdEAMw02MirttEAjj7-jRspVJVLs4YtX0MMlU-d3tGelloj126QxVkDphw==', start_index=24446)
Annotation(end_index=24529, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3Yn-w_k2N6wZI5l_VeyvUrV3gJM9WTHKit1tGijJj4k4CGWbc4UQrSYNg6-QhWqIIvkrXJ0TfC-fZsA3sLvmEMMcatwWyenHytHd7LaIIa58TXZcbCUswZcQKYlP5', start_index=24519)
Annotation(end_index=24610, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxQDBJBi97O8-rrGpqGkKER3vihePckVJblSzGcz9JBVASaAC-w4zxcAuqXFvdASlQmVnbBdJg1ApTwTDgGudjddwM4fZwGrPe2SaaE8-ixaGadXFqyfolBKpFXCU5bSWjXgHat6yS612JH01uaOHqarB3ZbiBKovhWjBfpeFoIlGELQZEve0WXNxm0apn4tp6Lg==', start_index=24600)
Annotation(end_index=24675, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEDFtUwPbhaFuhUwlVqzPEUOoTNgf0I1Vajt_BbP9Es2fSNNKwZ9O1G62U2ZrdA2QXLNI1agApj7o1XFH-TlWjiv17OLLXvinF3pPKcZtX5IHPpBShBKnh2o65KzHBgqSio4qDM74aSg==', start_index=24665)
Annotation(end_index=24735, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9xQ_UL9lr4abdwWmKaQnEh6X1PsBYMcHBSpqFTkg7aCqKd4vIUzsMZYkVMcmRu9lgWZg9bYiWH8iHDzuh2tAIwkbf0HV93DxAX3U-9K0v51CkrjhKKmUrrcLI2PSWK7uP-icqRt6AuRqt', start_index=24725)
Annotation(end_index=24808, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpOdLKzIbBFAm_bxPqhAMaseFX9lkinhWOL3TyAKv9mVlp-qCPhcOOWzzIvWpAieMvH_m9l_VCYY5o0sZ3_qdTJpNJ1gNH-OIl7Uig7tc_i1uqhmxNqgLiq4rUw7Z2cPhf2_ODZYZDjqANXb-NY1CNFDaEfcbBMMn_DUqTzwTpHjhQQh-98DrIFECWygaU-Mwg0q7UysFDMT5mxfRA4-dCXA5xVyooGJonCPXNdsE4BAaq', start_index=24798)
Annotation(end_index=24877, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJPZXTQdVJLfQ6xcfZIoLACSOb9r6UOjxRzfngJVN5mpfoEshRaxgK57OAlMLd8_zwcrN8H0eIGbtWoye-xeTYlSs4G6d0pP3QFuHRV-JyMObUdCIQzM5RGNXnSVYaCLRApkeu2pTKGZo4S3kyesbJYiZ1_0UvBPyu9Nb3C9nP4shNyLidJ8wAwXGIRsXdQtmCyYck190Uip3CQn8lSDk0SUpkovaagmz2eVfxUQZvyetbXyC--xQ=', start_index=24867)

## Sources
