# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 2eeed531 | **Time:** 369.71s | **Cost:** $1.58382
--------------------------------------------------------------------------------

# The Rheological Constraints on Sea Level Rise: The Interplay of Stress-Strain Relationships and Basal Sliding in Ice Sheet Models

### Key Points
*   **Rheological Control:** The stress-strain relationship of ice, governed primarily by Glen’s Flow Law, acts as the fundamental "brake" on ice discharge when basal sliding increases. As friction at the bed decreases (e.g., due to meltwater), the ice sheet’s internal viscosity and resistance to stretching (longitudinal stress gradients) become the primary constraints on how fast ice can flow into the ocean.
*   **The Exponent Controversy ($n=3$ vs. $n=4$):** Standard glaciological models have long used a stress exponent of $n=3$. However, recent research indicates that in fast-flowing Antarctic ice streams dominated by dislocation creep, an exponent of $n=4$ may be more accurate. This higher nonlinearity implies that ice becomes significantly "softer" under high stress, potentially accelerating the response to buttressing loss and increasing sea level rise (SLR) projections beyond current consensus estimates.
*   **Basal Sliding vs. Internal Deformation:** In regions of rapid flow (ice streams), the basal boundary condition shifts from a "no-slip" to a frictional sliding regime. When the bed is slippery, the Shallow Ice Approximation (SIA)—which assumes flow is controlled by local basal drag—fails. Accurate predictions require Higher-Order or Full-Stokes models that account for membrane stresses (longitudinal and lateral drag), which transmit forces upstream and govern the rate of drawdown.
*   **Model Sensitivity:** The "coupling length"—the distance upstream that a perturbation at the grounding line is felt—is a function of the ice rheology. A higher stress exponent ($n$) alters this length scale, changing how rapidly inland ice thins in response to coastal changes. Consequently, uncertainties in the microscopic physics of ice deformation translate directly into multi-meter uncertainties in global sea level rise.

---

## 1. Introduction

The prediction of global sea level rise (SLR) in a warming climate is fundamentally a problem of continuum mechanics. While surface mass balance (snowfall minus melting) plays a role, the largest uncertainty in future sea level projections arises from the dynamic instability of the Antarctic and Greenland ice sheets—specifically, how fast ice flows from the interior into the ocean [cite: 1, 2]. This flow is resisted by two primary forces: friction at the base of the ice sheet (basal drag) and the internal viscous resistance of the ice itself (rheology).

The user’s query addresses the critical intersection of these two forces. When basal sliding changes—for instance, when subglacial hydrology lubricates the bed or when grounding lines retreat from stabilizing ridges—the basal drag decreases. In these scenarios, the ice sheet’s velocity is no longer limited by the bed, but by its own internal stiffness and its ability to transmit stress. Therefore, the mathematical description of how ice deforms under stress (the stress-strain relationship) becomes the governing constraint on discharge rates.

This report provides an exhaustive analysis of how the stress-strain relationship in ice flow models constrains SLR predictions. It examines the physics of Glen’s Flow Law, the implications of recent findings suggesting a revision of the flow law exponent, the mechanics of stress transmission in slippery ice streams, and the failure of simplified models to capture these dynamics.

---

## 2. The Physics of Ice Rheology: Glen’s Flow Law

To understand how ice flow constrains sea level rise, one must first define the constitutive equation that governs ice deformation. Glacier ice is treated as a non-Newtonian, viscous fluid. The relationship between the applied stress and the resulting deformation rate is non-linear, meaning the "viscosity" of ice changes depending on how hard it is pushed.

### 2.1 The Constitutive Equation
The standard mathematical description of ice rheology is **Glen’s Flow Law** (also known as the Glen-Nye Law), derived from laboratory experiments in the 1950s [cite: 3, 4, 5]. In its simplest scalar form for secondary creep, the law states:

\[ \dot{\epsilon} = A \tau^n \]

Where:
*   **$\dot{\epsilon}$** is the strain rate (how fast the ice deforms).
*   **$\tau$** is the deviatoric stress (the driving force, primarily shear stress).
*   **$A$** is the flow rate parameter (or fluidity), which depends on temperature, crystal fabric, grain size, and impurities.
*   **$n$** is the stress exponent, which determines the non-linearity of the flow [cite: 4].

### 2.2 The Significance of the Stress Exponent ($n$)
The exponent $n$ is the critical parameter defining the sensitivity of ice flow to changes in stress.
*   **Newtonian Fluid ($n=1$):** If ice were Newtonian, a doubling of stress would result in a doubling of flow speed.
*   **Non-Newtonian ($n > 1$):** Ice is "shear-thinning" (or pseudoplastic). As stress increases, the effective viscosity decreases, allowing the ice to flow disproportionately faster.
*   **The Canonical Value ($n=3$):** For decades, glaciologists have used $n=3$ as the standard value for ice sheet modeling [cite: 4, 6]. This value was empirically derived and has been sufficient for reproducing the geometry of slow-moving ice divides.

However, the value of $n$ is not a universal constant; it reflects the dominant microphysical mechanism of deformation.
*   **Diffusion Creep ($n \approx 1$):** Dominant at very low stresses and small grain sizes.
*   **Grain-Boundary Sliding ($n \approx 1.8$):** A mechanism where ice crystals slide past one another [cite: 7].
*   **Dislocation Creep ($n \approx 4$):** Dominant at high stresses typical of fast-flowing ice streams, where deformation occurs via the movement of dislocations within the crystal lattice [cite: 7, 8].

### 2.3 The "Stiffness" Constraint
The stress-strain relationship acts as a constraint on SLR because it dictates the "stiffness" of the ice. In regions where basal sliding is high (low basal friction), the ice stream is essentially pulled by gravity and restrained by its attachment to slower-moving ice at the margins and upstream.
*   If ice is **stiff** (low $A$, low $n$), it resists this pull, limiting discharge into the ocean.
*   If ice is **soft** (high $A$, high $n$), it stretches easily, allowing rapid acceleration and thinning, leading to faster SLR [cite: 8, 9].

Recent research has challenged the universality of $n=3$, suggesting that in the critical shear margins of Antarctic ice streams—the "brakes" of the ice sheet—the exponent is likely closer to $n=4$ [cite: 7, 8, 10]. This implies that ice streams are more sensitive to stress perturbations than previously modeled, potentially making current SLR predictions too conservative.

---

## 3. Basal Sliding: The Boundary Condition

The stress-strain relationship describes the *internal* deformation of the ice. However, the total flux of ice into the ocean is the sum of internal deformation and **basal sliding**.

### 3.1 Mechanisms of Basal Sliding
Basal sliding occurs when the ice is at the pressure-melting point. It is facilitated by:
1.  **Regelation:** Melting on the upstream side of bedrock obstacles and refreezing on the downstream side [cite: 4, 11].
2.  **Enhanced Creep:** Plastic deformation of ice around obstacles.
3.  **Cavitation:** Separation of ice from the bed due to high water pressure [cite: 11, 12].
4.  **Sediment Deformation:** In many Antarctic ice streams (e.g., Whillans Ice Stream), the ice rides on a layer of weak, water-saturated till that deforms like a viscous fluid [cite: 13, 14].

### 3.2 Friction Laws in Models
In numerical models, basal sliding is parameterized using a friction law that relates the basal shear stress ($\tau_b$) to the sliding velocity ($u_b$) and effective pressure ($N$):

*   **Weertman Law (Power Law):** $\tau_b = C u_b^m$. This assumes friction increases indefinitely with speed. It often fails to capture the behavior of fast-flowing streams where cavitation limits friction [cite: 12, 15].
*   **Coulomb Friction:** $\tau_b = \mu N$. Friction is proportional to the effective pressure (ice overburden minus water pressure). Once the yield stress is reached, the ice slides freely (plastic failure) [cite: 13, 14].
*   **Regularized Coulomb (Schoof) Law:** A hybrid approach that behaves like a power law at low speeds and a Coulomb law at high speeds. This is currently considered the most physically realistic for SLR simulations as it places an upper bound on basal drag [cite: 9, 12].

### 3.3 The Decoupling Effect
When basal sliding increases (e.g., due to ocean warming melting an ice shelf and reducing backstress, or subglacial lakes lubricating the bed), the basal shear stress ($\tau_b$) drops. In the extreme case of a floating ice shelf, $\tau_b = 0$.
**Crucially, when $\tau_b$ decreases, the gravitational driving stress ($\tau_d$) must be balanced by something else, or the ice will accelerate infinitely.** That "something else" is the internal stress within the ice body—specifically, the longitudinal and lateral resistive stresses. This is where the stress-strain relationship becomes the limiting factor [cite: 9, 16].

---

## 4. Stress Transmission: Longitudinal and Membrane Stresses

The core of the user's query lies in the mechanics of **stress transmission**. How does the rheology of the ice constrain flow when the bed is slippery?

### 4.1 The Force Balance Budget
The momentum balance for an ice stream can be simplified as:
\[ \tau_d = \tau_b + \frac{\partial}{\partial x} (2 H \bar{\nu} \frac{\partial u}{\partial x}) + \frac{\partial}{\partial y} (H \bar{\nu} \frac{\partial u}{\partial y}) \]
Where:
*   $\tau_d$ is the gravitational driving stress ($\rho g H \sin \alpha$).
*   $\tau_b$ is the basal drag.
*   The terms with derivatives represent the **longitudinal** and **lateral** stress gradients (often collectively called membrane stresses).
*   $\bar{\nu}$ is the effective viscosity, which is derived from Glen’s Law ($\nu \propto \dot{\epsilon}^{(1-n)/n}$).

### 4.2 The "Tug-of-War" Dynamics
When basal sliding changes (e.g., $\tau_b$ decreases):
1.  **Immediate Acceleration:** The driving stress initially exceeds the resistive forces, causing the ice to accelerate.
2.  **Activation of Membrane Stresses:** As the ice accelerates, the strain rates ($\frac{\partial u}{\partial x}$) increase. Because ice is viscous, this stretching generates a resistive stress (longitudinal stress gradient).
3.  **Rheological Constraint:** The magnitude of this resistive stress is determined by the ice viscosity.
    *   If $n$ is high (e.g., $n=4$), the viscosity drops rapidly as strain rate increases (shear thinning). The ice offers *less* resistance to stretching, allowing the acceleration to propagate further upstream and the velocity to reach higher peaks [cite: 8, 17].
    *   If $n$ is low, the ice remains "stiffer" effectively dampening the acceleration [cite: 9].

### 4.3 Longitudinal Stress Gradients
Longitudinal stress gradients are the "pushing and pulling" forces within the ice. In the accumulation zone, ice is pushed (compression); in the ablation zone or ice streams, it is pulled (extension) [cite: 4, 18].
In a fast-flowing ice stream, the basal drag is often negligible ($\tau_b \approx 0$). The flow is restrained primarily by lateral drag against the shear margins and the longitudinal tension transmitted from the buttressing ice shelf or sticky spots [cite: 16, 19].
The **stress-strain relationship** dictates how effectively these restraining forces are transmitted upstream. A "stiff" rheology transmits stress over long distances (long coupling length), meaning a perturbation at the grounding line is felt deep in the interior. A "soft" rheology might localize the strain, leading to extreme thinning near the coast but less immediate drawdown inland [cite: 16, 17].

---

## 5. Model Hierarchies: Why the Stress-Strain Model Matters

The ability of a computer model to predict SLR depends entirely on whether its mathematical equations include the terms for longitudinal stress transmission.

### 5.1 Shallow Ice Approximation (SIA)
The SIA is the simplest model, assuming that the gravitational driving stress is balanced *locally* by basal drag ($\tau_d = \tau_b$). It neglects longitudinal and lateral stress gradients [cite: 20, 21].
*   **Failure Mode:** In the SIA, if basal sliding increases (friction drops), the model predicts infinite or unrealistic velocities because there is no mechanism (like membrane stress) to hold the ice back.
*   **Constraint:** The SIA cannot simulate ice streams or the stress-strain constraint requested in the query. It is valid only for slow-moving, frozen-bed interiors [cite: 22, 23].

### 5.2 Shallow Shelf Approximation (SSA) / Shelfy-Stream
The SSA assumes that basal drag is low and that flow is dominated by longitudinal and lateral stresses. This approximation explicitly includes the stress-strain relationship (viscosity) in the momentum balance [cite: 24, 25].
*   **Relevance:** This is the standard for modeling fast-flowing ice streams (e.g., Pine Island, Thwaites).
*   **Constraint:** In SSA models, the SLR prediction is directly sensitive to the choice of $A$ and $n$ in Glen’s Law. Changing $n$ from 3 to 4 in an SSA model fundamentally alters the calculated discharge for a given geometry [cite: 8, 26].

### 5.3 Full Stokes Models
These solve the complete set of stress equations without approximation. They capture vertical shear (neglected in SSA) and longitudinal stress (neglected in SIA).
*   **Findings:** Comparisons show that while SSA is good for ice shelves, Full Stokes is required to accurately capture the "transition zone" near the grounding line where both basal shear and longitudinal stresses are active. The rheological constraint is most complex here [cite: 20, 23, 25].

---

## 6. Implications for Sea Level Rise Predictions

The interaction between basal sliding changes and the stress-strain relationship leads to several critical implications for SLR forecasts.

### 6.1 Sensitivity to the Stress Exponent ($n$)
Recent studies have highlighted that the choice of $n$ is a major source of uncertainty.
*   **The $n=4$ Hypothesis:** Research by Millstein et al. (MIT) and others suggests that in high-stress areas (shear margins, grounding lines), dislocation creep dominates, and $n=4$ is more appropriate than $n=3$ [cite: 5, 8, 10].
*   **Impact on SLR:** Using $n=4$ makes the ice "softer" at high stresses. Models using $n=4$ predict **faster** ice acceleration and **more rapid** sea level rise following a loss of buttressing (e.g., ice shelf collapse) compared to models using $n=3$. The ice cannot "hold itself back" as effectively [cite: 8, 26].
*   **Quantification:** One study found that using $n=4$ instead of $n=3$ could significantly accelerate the projected mass loss from the Amundsen Sea Embayment, the most vulnerable sector of West Antarctica [cite: 26].

### 6.2 Buttressing and Instability
"Buttressing" refers to the backpressure exerted by ice shelves. When an ice shelf thins or collapses, this backpressure is removed.
*   **Rheological Response:** The grounded ice upstream must accelerate to re-establish force balance. The rate of this acceleration is constrained by the ice viscosity.
*   **Marine Ice Sheet Instability (MISI):** This instability occurs on retrograde bed slopes. The timescale of MISI—how fast the collapse occurs—is governed by the stress-strain law. A highly non-linear rheology ($n=4$) facilitates rapid stretching and thinning, potentially shortening the timescale of collapse from centuries to decades [cite: 8, 27, 28].

### 6.3 The Role of Basal Lubrication
As climate change increases surface melt, water may reach the bed, increasing basal sliding.
*   **Constraint:** If the bed becomes slippery, the ice stream speeds up until the increased strain rates generate enough internal viscous resistance (membrane stress) to balance gravity.
*   **Prediction:** If models overestimate ice stiffness (e.g., by using too low an $A$ or $n$), they will underestimate the discharge resulting from this lubrication. Conversely, if they underestimate stiffness, they will predict runaway collapse too early [cite: 9, 12].

---

## 7. Recent Advances and Controversies

### 7.1 Dislocation Creep vs. Grain Boundary Sliding
While $n=3$ is standard, and $n=4$ is proposed for fast flow, some research suggests $n \approx 1.8$ (grain boundary sliding) might be relevant in specific regimes [cite: 7]. A unified flow law that transitions between these mechanisms based on stress and grain size is the frontier of modeling [cite: 7, 29].

### 7.2 Temperate Ice Rheology
A recent study (2025) indicated that *temperate* glacier ice (at the melting point) might flow with an exponent closer to $n=1$ (Newtonian) rather than $n=3$ or $4$ [cite: 3].
*   **Implication:** If true for specific glaciers, this would mean they are *less* sensitive to stress changes than currently modeled, potentially leading to *lower* SLR contributions from these specific temperate glaciers. However, this finding stands in contrast to the Antarctic (cold ice) context where $n=4$ is the concern for massive SLR [cite: 3].

### 7.3 Spatially Varying Rheology
Inversion techniques now allow modelers to infer the rheology ($A$ and basal friction) from satellite velocity data. These inversions show that "stiffness" is not constant but varies spatially due to damage (crevasses) and temperature [cite: 15, 30]. Damaged ice in shear margins is softer, effectively decoupling the ice stream from the walls and accelerating flow [cite: 15].

---

## 8. Conclusion

The stress-strain relationship is the "viscous damper" of the ice sheet system. In the context of sea level rise, it acts as the final line of defense against gravity when the stabilizing forces of basal friction and ice shelf buttressing are removed.

Current research suggests that this damper may be weaker than previously thought. The shift in understanding from a stress exponent of $n=3$ to $n=4$ in fast-flowing regions implies that Antarctic ice streams are more rheologically sensitive to stress perturbations. Consequently, when basal sliding increases—whether through subglacial lubrication or grounding line retreat—the ice may accelerate and thin more rapidly than traditional models predict.

To constrain SLR predictions effectively, models must:
1.  Move beyond the Shallow Ice Approximation to include longitudinal stress gradients (SSA or Full Stokes).
2.  Adopt physically based friction laws (Regularized Coulomb) that account for cavitation.
3.  Implement spatially varying stress exponents ($n$) that reflect the dominant creep mechanisms (dislocation vs. diffusion) in different parts of the ice sheet.

Failure to account for these rheological nuances likely leads to a systematic bias in SLR projections, with the weight of recent evidence pointing toward a potential underestimation of mass loss rates from the West Antarctic Ice Sheet.

---

## References

*   **[cite: 3]** ScitechDaily (2025). "Glacier Experts Uncover Critical Flaw in Sea Level Rise Predictions." (Discusses $n=1$ for temperate ice).
*   **[cite: 1]** IPCC SROCC Chapter 4. "Sea Level Rise and Implications."
*   **[cite: 4, 18]** AntarcticGlaciers.org. "Glacier Flow II: Stress and Strain."
*   **[cite: 5, 31]** MIT News/WeForum (2022). "Study: Ice flow is more sensitive to stress than previously thought." (Discusses $n=4$).
*   **[cite: 13]** "The impact of spatially varying ice sheet basal conditions on sliding."
*   **[cite: 26]** ResearchGate. "Increasing the Glen-Nye Power-Law Exponent Accelerates Ice-Loss Projections."
*   **[cite: 7, 8, 29]** Ranganathan & Minchew (2024). "A modified viscous flow law for natural glacier ice." (PNAS).
*   **[cite: 9, 32]** McArthur et al. (2023). "Basal conditions of Denman Glacier." (The Cryosphere).
*   **[cite: 20]** "Glacier flow modelling: A comparison of the Shallow Ice Approximation and the full-Stokes solution."
*   **[cite: 17]** "Nonlinear longitudinal stress coupling in glacier and ice sheet flow."
*   **[cite: 16]** "The role of membrane-like stresses in determining the stability... of the Antarctic ice sheets."
*   **[cite: 12]** Joughin et al. (2019). "Regularized Coulomb Friction."
*   **[cite: 6, 10]** "Refinement of the fluidity parameter range with a stress exponent of four."

**Sources:**
1. [ipcc.ch](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1KWz_7A0aSfBrjtMVJscg_A_RjU16qddc0t4FbFo5N7R6RaufUw8X0I_hVYhyfZcC87AuycFZQ3GEhK124jbZQHC9eWHjQpWC_mzGNSlXTIXGzKyASxlnV7bgeam8oSHkn4uiLADMJwxp0sPRy3UjLrUeWI0DkbuydvWN8H_86oYuIkZMzWXJnjP1ty-ivou19whqKDzDCS5CIfpg0KLYVnFok7j7B0FtcEr0YNw_)
2. [cpom.org.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFv-MzQQoQWbzui6brn9Ff_aFCp9y3baOZu6A5yDjDVY4Hy97xEkgL9k6yUX0ocD-iFCxWriq61VYN06NT-6X13MmGnYtCsMxHYabaTswdtKVcPxL9xF25qLGfd5QIMFMKzU3XAKvQ4gRm_idL8FCXXbHRduw0V62kaNW2-15X14ev4qgW_xU2J)
3. [scitechdaily.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKFyqS5Tti7nTgFN3zSut__vyWhwC3MD4HaU8xJHy1VzEuasp5vGGj81doLvRBTo59gL_FxEyT0f6GforIVdeSy89Lh3FJ4oPlF9URpEHH4cMtPdegVpTIqDcKPR2WBNbIpBoLbr3Cy7OfJ7Ny5krnvwq8HNHGt2Zy0fl1sy1XiYMzb9D9atYcef8OMmsxW8YjesI=)
4. [antarcticglaciers.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTNwqpoFusBrFqTyStAYAQMX0ecNOPoPkVdQwF_dxEPrdYcEqSQ5cvdxiO-1RKiPoqz9fVdABnIDQdpnvoDwZPPZAAoY8Hq38m12GObggnZWaLd2sCU91D44uvFJegJ5nij2a88DFTQruX4tHHAJ3ItV3ifFA3SRFWQGXsxNEf2sKh5POPp7ABoRikDiE99GxVjFLJw2hd6B6JOQ==)
5. [weforum.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRL_1U7kHKKRN5Hfop6lIbPWTkFKNDbny9RJYPg-Bqce-6-5yz8WIo1Y-OyaTU37xSmrJImwkq2324jrfbmQ4FxGQfPGffmJT_nTdZZsbUdwH-XJM1L-DWBv6BPixjMUEYvkEoqwM1Q5qYQxG5YKiTWns1TCXgX3upjs0vpoUJAXfUpQ_k5rGu5XPr1RmC9-0xC9pz4GYLn2Ocn2v_cbGvAw==)
6. [copernicus.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgUGBcoF5AJgP_DeKiyAMxo4tMbxNhNqV65MZ_GyN64N3_6kQCiUaFNMWgs5A-V1_B7TmagT1TSm8v-gTKyYEAUM0-jj4ISltoer08lIR4mmRgDSnAnw-LQf6c7GMLlgAjnObdZBKHY_QWT8MWq2RdXn7otIjaocfVN_pQdE7qnPzQ42C6qq5aV6gy4Hoj8_1q)
7. [mit.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPa-X2xC90hQ-vXbn0iYwddFnefoEFl9lACu8-KfFgDHIfSZ3Lyw7gx_Rq476PaEYRFxtztV0h9bHVahNZSnBaab8uibZEEY7Ryh3UUSj18KION1CafMwGcCocWvpA949Dn0EqGaKnuUYjS3NBc6mQGsLLoGHaFI_Pxin35lcbL027YsBB-tjgxXl-Wzs0frUmAVT1tNShhGLbi3z2FIkvJEQQMucyykIV430f8iwpInyZQmyMXwK0L0S6viFk-iIHoYxXThH47dl4YrxXUVqYzv72_VinfPz7mIsYYOTXwTgRqkOcDSLBG51gPBZ1hEkxIyB0Y5yzFJ13rUA=)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9f_OzzAkMOw3GSAYUl6W8OztQKjf75lGHXRiXwwT76epGXYSQhf2jKEAL4XU6xyLx1jjPUw3f42uEHdtf23AXI3BEbhDglUnre1QrZgf2TWBar6JXm9wHLJ2GLgKDqKQkjjs4huwOfbrbpXJmDYvjI_QB0wQiTUMxbkU3LRpIUREpFekexV0Hbr913QC4wkKE1BDONs1rke5up8eJacUjLw3LRVmjkVMAauJJ5bYzgMVQHMYv5AXvT8fKTEgGH6a-CSMEMA==)
9. [copernicus.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIovdo1pt58VyYVy20stJP3KM0Bp4DShkMbd3Qp0efAdjzNycOkZamxZvPDm5D9KGUhc_E1pKE2Kn3V8YiNYBdOSbIt_6-hfW99JP8xGF1wTpxzfi-Bwesyb2FxFaR550C2YCVqqVOcprGF7Pr4dGcM1-DiRHuNN4n)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEL5ktRwVURrQQ51DTE-b7_jUlXDDLiUNZOw3xSiovgauNbnh65jemJyKQVxxk-WmIPCYT1AvH7aHkHV8TT3OjQLnTsLRVaYSI2avImpsnBSaitYtYG9F58ulOwXAagcJFeXu_iTwZZKbxrBoEDyMdXXisbXDX4J9cr3HG2ngJsRtDkTHHzKrWkgWSGl2CNHJkVTQxl8U1lMaaqt-BPZwkreWWN-amDRNmxi6OnZa055XzqM8mEB2bnZtySiEBj2hCYQctqgfwdthe2kArrpdw6hWEXc8KZPg6HC-nR_GKneYlW-n7_2VLQ-Chnv6AX)
11. [antarcticglaciers.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG41OKyhUbtnA_-9FNe-LpMY7ZYNMyMLbMp46DAKJMoAqUmJn_nRljp43_DwuNGzty-LFUPlkpIEa_GkGa4ZPPMqq08zGw-VcXfYQnQNDVDkOcRtsA0QhjCkZb2shYa5dE9clWZ1Z85YtXboOSro7MNOfYVcbSQMcAnt4atJWg6Hg79QKomZA==)
12. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5TZTWgU6whIYKrIB6gRt5sV_JD-NROCkzoT-bcidoXqFrMslawpirqtrWCgiDq88speBDbP82_V0xQVY2Ny3AyK-W86PwXuzfC-np1tgxYFsnnHQa2ySy_evNevdwVyVPkx_NVD8c)
13. [geomar.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7GYoi2I8D0vAVv4e0tiEoFqTxfYcc2Nr6nuCFn8SiVOm9attos-NVwDKJ0l9uNbTgokWVFD3LToBhEB3IX2wwOGA05k7UsAU_5u31vVFCEM3LvZD0atWONbWuwk3rg-uaS9AKcACojrobbUZX50VnFIoGT5aMGciBwfDcgNxpUl-xxAN5KOm2rVQ0h3W-cCeB_BEcwJMHBGk07ZydInm_06XT70vIB1ohg2SJQRTxUAq1PiWm0p-RyAU=)
14. [core.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMqz-h9tCp4VBf8recVvTEsth-qomJFln-JvA6RXznBN7FjRoqGhxh-e5xHU2N3i9-vFZifjAf3bdx3TeAMS87_Ijd7TkwNAMifBbKHxZdXAfCWRqamNBlpxYKAUghnrawtos=)
15. [cambridge.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGw1IL4X0UV2kZiyboERXZH6e5K01HBj2au3DZm4J8bIr4mo--DymfszhEgqvoPBmAgwPQC8JeUoThmICYhOfPwmUKIG7_H3EkTfVhboJyOqLXypJpt4rWL0J3jewiDHLMDxMTX8HKcTlBDbSnet8ABRNprVjaUSpvi1aEQyF4I9fUci3TlB-UKNIOYNJ04yksw1_6Uh7VYIP4HYBs1I0pnzll4Fg_z-By3byAKLxRvR8h3MPHqzfbdinAWRKzCjVy6xyO85BLEfYRAvz77GmsM7ZGw7IqnNBB5frqND80rAj_Nkb1dQXGjGszrkOxpR1RpjV1O)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVicaWeivtACeK5CjSaaEGcXst2EAShBCev7tyDRk5uLvun-7-Oeo60cN0Sz3Uwh4ykooy2JYz4FAhoe2nNt2ZodnfSl1Y8-Y396bTq8-MdRM8wQ4UwajJ4gOfA4Q-43xrEBRM1oswtY6iFCchfl6AcOQQJ7lGtXqeTOkXyBfFYDBedVhEatSTCMP2aEmexMPzXIe__HTWE0pRR9NhPx6wNcLKO6LCM9G38UJMnmSvwcJbj9wd3mpHnUa4kurhKH0VWru_jucU5_k3tZqpXtKgquN9uhBS-L88IChgMb4sKQWbcY4VtCics0Emek8Ha2RXzoAtJeqSBHGK0w==)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmwNLgIu7SpCOuLRHLaY6cMhfYKyiaOcr9bIEQzj71VZHe14NDl7w2sxK0qy0oo8HOSCVcwwLmywzNtXjayBFf2OCXRQNi1lExbOzttNeU-kN9vh-H5yBl3kW7a0rTBMGnucuuEJDg0GWYlJJlH8uMpPB3rmHIkbsac48KIrc68tferad37Axoc71evmISjp_RDIMU34dmngk6KqhgD2wl_jTzCfqZLl1Ne6siWw==)
18. [antarcticglaciers.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCIVNbB33u6YTHKzBL2I45aFXk_NRVWg5JewxWy-yGMXFnir6Tk2643IXkZ3ELDd4Y74m8BSnGDPjNv-z-yEBzUIT-Tu1eHT83G55kZijnMABvGXfEkBG8zPP-Iiumry-V5So3-KQqEQPbsL_bGwiqYbP4jwq6xPlU0AVAgJPfCq9izPdEDu_TTAzatyo=)
19. [uchicago.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFS3jazFyjIIIVIA_xTEj2mTHGe6qmXV3aBUcNBsK-a-NLIvmaGiL0gq1bmQ0gB4mxdX08lQLp-JrJQ8Caag1c4Mz1brJ-Vp2Vbdb3UUI6m8uzI5ZRlHmdZrzAtGe0GLjQaDa2mnS64vUfckMc=)
20. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYMJout3HGtk-qQt3kCBsI4vVXhoOzybSCt5NGsKv_arMY3_gnq-WKHzBVvkYVtryP4-SIf1HtyzzMZBrsDtgd8uq5PKlTIf1S1VrWdGR9CG3621DB9RtdVKwTUXBXzB_B9GIXyY--93rmEJXGftU9e7f0bOp7MHOKijqQb6vgWujMkHI9RAhli5fJHd6a3wKXxxe8MmNngzG24BPgQSHf6LK1OJlA36u5YoOl6_h6PcNXZARZzcNjE0EJVyrX_Mcyfa0H4JCCez6u4A==)
21. [copernicus.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbJbdztJ1Iclg5CKAkhPHGU03errc6zDFQqYH3T9MkvmK2FWvfEDge8cwahdL-SdgAQsMRrIS9NlOjDpm5Udy6uAT3pzD-6lWoMHY-oRHYHf9rWScHn6shDjGoa8U72yelOsLameqtFkJO1888inF44KoIcE2U3mrtOiWToQ==)
22. [antarcticglaciers.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF960icuG8jm5HhmM334rqthcYe_UPF1sX7wms_nh7E8-uDSTbO4oZbw6lrP1xJemxqT7cJAPZLEKRzQSDSMwkszrRTOZEomMiThFZfUrDvop9kE2RmHWy3sXFWx7P0G04hexxlqsVo52LMImLGzU74ZHvvYKj7_mxOXnGzPT3eOoOYkSPTSbvRRcEPD4Mk6ZCBeBCGKjErCZxchXr_C7y9FgLKpP0z6AEaK_sLgtSBxA==)
23. [harvard.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQESfbywzBY5QHhrN8xy-8kES0i7tyMsubH3E8pf-5ETuNC9qhuM0J5BLfS7lBpcCdMAKfIhQPN9vk0VQyl7JRZCnufHrTgULzyxIdwsnO7l6lGEf1hJlscyuddzrIh590Gy-TZiX1xhsw3CYyX5-Qn8GFO8avanDUsLR-qzN7yVGlAH4ote_3NHZtS6mTX1VmzvIlIk3wdn7UKgGB0Y1b8gXVCueCICxxqSuJCq8vDtlv1B6gFsfyaKHozZNcDFOHSxm9--o=)
24. [cambridge.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGB17W0OFN9t4tt4Nax3wa1DbuDIOOwY6Z0V8BwMTD3XIYFi1_lJxNKftoEE9nPSvHD_f80BHQXTMbqGemlk7UW4TkDEELVsm2_vHGEhcWFVZpMY2TMPYIyDIM9Sf2KJhd6VkUlo5SWFYsu9fMuraC5uEUHhqF48ZL48bZi-VH-RKTfMbqRGHJCYb-3u3QMoi9dYA-5bS4JTBtk3Rh94Wr6Yzq5zoZfYluYF-f3I9NvjQJhO9vGU_LW0KYZ2qL2l-4O_Xd3F7xkfSl1ZcHVZb_IcWdrzw_JwIEeO2EQ)
25. [copernicus.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmiZLYU8bmAkfkcLgSC4RptJnA_VLqet3GGKIpAhj6ovfz3gbX0_m4vQTajxCGyesNBibxsk-iqxlSXIx_NgGL-yQ3wAz6NkeIetADeLuEYV2tCjblAlQgnFw4bo-ynJuI9AzSCjKcC8U4MS3IkdoZuqnm2V-VtFw=)
26. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsgavGmZDXRI9Zk9IRT2GInGSo6z2f366RJ2bo6pRJ8WiCg1KVRf1z3vIGym6VDU0Gqar8YPdfrLTuzFVjS-tcRKgBAGp0QOFRg4HGkrXqUca4GmfAOLJebN-Wn7fP3YcFqPrd5pc0tpbf6tmUEnU_h_lDPLb2px6b4_Ntv0VeNe0-xZzAcrWdmbah5QGVAkfckEgYQAT8Q0hg4v3RrW7mk8hk3sJ6ZUg491DwY8eO97Sn1M0YPpfO5R4YGt_xPQkE3LSo9eCwWdVuS_JWs6Lyn-LuVBNV-fqMoLA1nVsmTYIMZZ8=)
27. [copernicus.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEG9a3Y9q5zbzfNd04xakzgkEE0w6_0HglVM2yP5udvADx7uFQI6JwGaZ4IdwdDgA_5evkWcIqF-5T0en65d-CyBva8RW_8gtEEy3NVYUC20jVwdLEraQCvfVMmvEnmKJrFfQF3-nU335KMBCyk56sta1QYHgk=)
28. [royalsocietypublishing.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZvB5r-gn45OG0NQJyM-8qJfxWVMLzZXbGuWdGrhs5dM1qaNSi-QFF_XIizUPiLq9d1h2KeJ12c8D-xELfLHQYccYimbe-vYQDwtiedh5z0HlOv40-cr_Mtr8RT7ed7xI3MwRdF8GMqUK7ltcQlulJ-go7H3xRiy92x5JAQ1_y3Eauq5hFIJaNTFtITW049tN91q1S5SeXiVMCDBTGZcSa)
29. [pnas.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzTpCGO8PshnMnsX5HGhGdRDIhL_5cydL_20OZXmSkqc2tkzVwmYABDvS_dyVekR6NUqj6cLhSQOwa7tDarQ6UJqMKdy4JgMw_IsLVTMWFaxV8mxhV6w0NGm8176LJ2Sfxt_2ernQ=)
30. [cambridge.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJyGGHN4wvO3TFsdt7sYPBGgLqPnrlktn_ZA-0S0bys0E3OLoUrp4fktRqmhD3XC0pHxmkSxTLuPMQF1dgDEAgICHf1LlSoQxWYxXkTKDJ-l_uhYCHLNy1hrqWk5dt-c_G5TpDvAGYJD6Oo8bwtl8Jx11V_DIkzo4GzfdL2kfAN8kFlZfsWSu9SVjZ9pnRS7qWd1brUzRiH556q89sdQmNpeK42LTwhZ9szU4nGxhkrpRnWRau-Uk2Ulpb4HOFP0hpAjifF4rgIswm8qIJIovwW4OjcnwOEpLHXRrrwMtB4tuA5dEg9G0CyQGHilLLbglSvqBYITG-L8yRlIFkMIMFRN2wWcBDsdDmrRuhPfy7ATxC)
31. [eurekalert.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_zS72vaW-R3nejP7F5S1zW04_TrS7K_ZNfM2paj0RVRhzGbnRPUWXK8-Ce3dt2nsc4cLnvOOsuYdV4CPSJuXoq6rlYk9GsiGhyVoOsihF-WcQg4LLFWQL3e4zTehaQrHgrbr32A==)
32. [copernicus.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcnziE7i2xWRQvfqQ0oELoeLWL76K7jFU7VW2sj08PsryT9YuzGsF3qmKv15KLQ9L6Vh2RGHRaviTb8b9u_oDvJBzX-M470gRolt5tA9fcUi1qte_ZH_uSw6pQtSdQtHShi0ZQz18=)


## Annotations
Annotation(end_index=2433, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFv-MzQQoQWbzui6brn9Ff_aFCp9y3baOZu6A5yDjDVY4Hy97xEkgL9k6yUX0ocD-iFCxWriq61VYN06NT-6X13MmGnYtCsMxHYabaTswdtKVcPxL9xF25qLGfd5QIMFMKzU3XAKvQ4gRm_idL8FCXXbHRduw0V62kaNW2-15X14ev4qgW_xU2J', start_index=2421)
Annotation(end_index=2433, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1KWz_7A0aSfBrjtMVJscg_A_RjU16qddc0t4FbFo5N7R6RaufUw8X0I_hVYhyfZcC87AuycFZQ3GEhK124jbZQHC9eWHjQpWC_mzGNSlXTIXGzKyASxlnV7bgeam8oSHkn4uiLADMJwxp0sPRy3UjLrUeWI0DkbuydvWN8H_86oYuIkZMzWXJnjP1ty-ivou19whqKDzDCS5CIfpg0KLYVnFok7j7B0FtcEr0YNw_', start_index=2421)
Annotation(end_index=4171, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKFyqS5Tti7nTgFN3zSut__vyWhwC3MD4HaU8xJHy1VzEuasp5vGGj81doLvRBTo59gL_FxEyT0f6GforIVdeSy89Lh3FJ4oPlF9URpEHH4cMtPdegVpTIqDcKPR2WBNbIpBoLbr3Cy7OfJ7Ny5krnvwq8HNHGt2Zy0fl1sy1XiYMzb9D9atYcef8OMmsxW8YjesI=', start_index=4156)
Annotation(end_index=4171, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTNwqpoFusBrFqTyStAYAQMX0ecNOPoPkVdQwF_dxEPrdYcEqSQ5cvdxiO-1RKiPoqz9fVdABnIDQdpnvoDwZPPZAAoY8Hq38m12GObggnZWaLd2sCU91D44uvFJegJ5nij2a88DFTQruX4tHHAJ3ItV3ifFA3SRFWQGXsxNEf2sKh5POPp7ABoRikDiE99GxVjFLJw2hd6B6JOQ==', start_index=4156)
Annotation(end_index=4171, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRL_1U7kHKKRN5Hfop6lIbPWTkFKNDbny9RJYPg-Bqce-6-5yz8WIo1Y-OyaTU37xSmrJImwkq2324jrfbmQ4FxGQfPGffmJT_nTdZZsbUdwH-XJM1L-DWBv6BPixjMUEYvkEoqwM1Q5qYQxG5YKiTWns1TCXgX3upjs0vpoUJAXfUpQ_k5rGu5XPr1RmC9-0xC9pz4GYLn2Ocn2v_cbGvAw==', start_index=4156)
Annotation(end_index=4656, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTNwqpoFusBrFqTyStAYAQMX0ecNOPoPkVdQwF_dxEPrdYcEqSQ5cvdxiO-1RKiPoqz9fVdABnIDQdpnvoDwZPPZAAoY8Hq38m12GObggnZWaLd2sCU91D44uvFJegJ5nij2a88DFTQruX4tHHAJ3ItV3ifFA3SRFWQGXsxNEf2sKh5POPp7ABoRikDiE99GxVjFLJw2hd6B6JOQ==', start_index=4647)
Annotation(end_index=5256, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgUGBcoF5AJgP_DeKiyAMxo4tMbxNhNqV65MZ_GyN64N3_6kQCiUaFNMWgs5A-V1_B7TmagT1TSm8v-gTKyYEAUM0-jj4ISltoer08lIR4mmRgDSnAnw-LQf6c7GMLlgAjnObdZBKHY_QWT8MWq2RdXn7otIjaocfVN_pQdE7qnPzQ42C6qq5aV6gy4Hoj8_1q', start_index=5244)
Annotation(end_index=5256, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTNwqpoFusBrFqTyStAYAQMX0ecNOPoPkVdQwF_dxEPrdYcEqSQ5cvdxiO-1RKiPoqz9fVdABnIDQdpnvoDwZPPZAAoY8Hq38m12GObggnZWaLd2sCU91D44uvFJegJ5nij2a88DFTQruX4tHHAJ3ItV3ifFA3SRFWQGXsxNEf2sKh5POPp7ABoRikDiE99GxVjFLJw2hd6B6JOQ==', start_index=5244)
Annotation(end_index=5702, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPa-X2xC90hQ-vXbn0iYwddFnefoEFl9lACu8-KfFgDHIfSZ3Lyw7gx_Rq476PaEYRFxtztV0h9bHVahNZSnBaab8uibZEEY7Ryh3UUSj18KION1CafMwGcCocWvpA949Dn0EqGaKnuUYjS3NBc6mQGsLLoGHaFI_Pxin35lcbL027YsBB-tjgxXl-Wzs0frUmAVT1tNShhGLbi3z2FIkvJEQQMucyykIV430f8iwpInyZQmyMXwK0L0S6viFk-iIHoYxXThH47dl4YrxXUVqYzv72_VinfPz7mIsYYOTXwTgRqkOcDSLBG51gPBZ1hEkxIyB0Y5yzFJ13rUA=', start_index=5693)
Annotation(end_index=5907, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9f_OzzAkMOw3GSAYUl6W8OztQKjf75lGHXRiXwwT76epGXYSQhf2jKEAL4XU6xyLx1jjPUw3f42uEHdtf23AXI3BEbhDglUnre1QrZgf2TWBar6JXm9wHLJ2GLgKDqKQkjjs4huwOfbrbpXJmDYvjI_QB0wQiTUMxbkU3LRpIUREpFekexV0Hbr913QC4wkKE1BDONs1rke5up8eJacUjLw3LRVmjkVMAauJJ5bYzgMVQHMYv5AXvT8fKTEgGH6a-CSMEMA==', start_index=5895)
Annotation(end_index=5907, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPa-X2xC90hQ-vXbn0iYwddFnefoEFl9lACu8-KfFgDHIfSZ3Lyw7gx_Rq476PaEYRFxtztV0h9bHVahNZSnBaab8uibZEEY7Ryh3UUSj18KION1CafMwGcCocWvpA949Dn0EqGaKnuUYjS3NBc6mQGsLLoGHaFI_Pxin35lcbL027YsBB-tjgxXl-Wzs0frUmAVT1tNShhGLbi3z2FIkvJEQQMucyykIV430f8iwpInyZQmyMXwK0L0S6viFk-iIHoYxXThH47dl4YrxXUVqYzv72_VinfPz7mIsYYOTXwTgRqkOcDSLBG51gPBZ1hEkxIyB0Y5yzFJ13rUA=', start_index=5895)
Annotation(end_index=6487, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9f_OzzAkMOw3GSAYUl6W8OztQKjf75lGHXRiXwwT76epGXYSQhf2jKEAL4XU6xyLx1jjPUw3f42uEHdtf23AXI3BEbhDglUnre1QrZgf2TWBar6JXm9wHLJ2GLgKDqKQkjjs4huwOfbrbpXJmDYvjI_QB0wQiTUMxbkU3LRpIUREpFekexV0Hbr913QC4wkKE1BDONs1rke5up8eJacUjLw3LRVmjkVMAauJJ5bYzgMVQHMYv5AXvT8fKTEgGH6a-CSMEMA==', start_index=6475)
Annotation(end_index=6487, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIovdo1pt58VyYVy20stJP3KM0Bp4DShkMbd3Qp0efAdjzNycOkZamxZvPDm5D9KGUhc_E1pKE2Kn3V8YiNYBdOSbIt_6-hfW99JP8xGF1wTpxzfi-Bwesyb2FxFaR550C2YCVqqVOcprGF7Pr4dGcM1-DiRHuNN4n', start_index=6475)
Annotation(end_index=6708, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9f_OzzAkMOw3GSAYUl6W8OztQKjf75lGHXRiXwwT76epGXYSQhf2jKEAL4XU6xyLx1jjPUw3f42uEHdtf23AXI3BEbhDglUnre1QrZgf2TWBar6JXm9wHLJ2GLgKDqKQkjjs4huwOfbrbpXJmDYvjI_QB0wQiTUMxbkU3LRpIUREpFekexV0Hbr913QC4wkKE1BDONs1rke5up8eJacUjLw3LRVmjkVMAauJJ5bYzgMVQHMYv5AXvT8fKTEgGH6a-CSMEMA==', start_index=6692)
Annotation(end_index=6708, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEL5ktRwVURrQQ51DTE-b7_jUlXDDLiUNZOw3xSiovgauNbnh65jemJyKQVxxk-WmIPCYT1AvH7aHkHV8TT3OjQLnTsLRVaYSI2avImpsnBSaitYtYG9F58ulOwXAagcJFeXu_iTwZZKbxrBoEDyMdXXisbXDX4J9cr3HG2ngJsRtDkTHHzKrWkgWSGl2CNHJkVTQxl8U1lMaaqt-BPZwkreWWN-amDRNmxi6OnZa055XzqM8mEB2bnZtySiEBj2hCYQctqgfwdthe2kArrpdw6hWEXc8KZPg6HC-nR_GKneYlW-n7_2VLQ-Chnv6AX', start_index=6692)
Annotation(end_index=6708, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPa-X2xC90hQ-vXbn0iYwddFnefoEFl9lACu8-KfFgDHIfSZ3Lyw7gx_Rq476PaEYRFxtztV0h9bHVahNZSnBaab8uibZEEY7Ryh3UUSj18KION1CafMwGcCocWvpA949Dn0EqGaKnuUYjS3NBc6mQGsLLoGHaFI_Pxin35lcbL027YsBB-tjgxXl-Wzs0frUmAVT1tNShhGLbi3z2FIkvJEQQMucyykIV430f8iwpInyZQmyMXwK0L0S6viFk-iIHoYxXThH47dl4YrxXUVqYzv72_VinfPz7mIsYYOTXwTgRqkOcDSLBG51gPBZ1hEkxIyB0Y5yzFJ13rUA=', start_index=6692)
Annotation(end_index=7352, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTNwqpoFusBrFqTyStAYAQMX0ecNOPoPkVdQwF_dxEPrdYcEqSQ5cvdxiO-1RKiPoqz9fVdABnIDQdpnvoDwZPPZAAoY8Hq38m12GObggnZWaLd2sCU91D44uvFJegJ5nij2a88DFTQruX4tHHAJ3ItV3ifFA3SRFWQGXsxNEf2sKh5POPp7ABoRikDiE99GxVjFLJw2hd6B6JOQ==', start_index=7339)
Annotation(end_index=7352, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG41OKyhUbtnA_-9FNe-LpMY7ZYNMyMLbMp46DAKJMoAqUmJn_nRljp43_DwuNGzty-LFUPlkpIEa_GkGa4ZPPMqq08zGw-VcXfYQnQNDVDkOcRtsA0QhjCkZb2shYa5dE9clWZ1Z85YtXboOSro7MNOfYVcbSQMcAnt4atJWg6Hg79QKomZA==', start_index=7339)
Annotation(end_index=7515, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG41OKyhUbtnA_-9FNe-LpMY7ZYNMyMLbMp46DAKJMoAqUmJn_nRljp43_DwuNGzty-LFUPlkpIEa_GkGa4ZPPMqq08zGw-VcXfYQnQNDVDkOcRtsA0QhjCkZb2shYa5dE9clWZ1Z85YtXboOSro7MNOfYVcbSQMcAnt4atJWg6Hg79QKomZA==', start_index=7501)
Annotation(end_index=7515, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5TZTWgU6whIYKrIB6gRt5sV_JD-NROCkzoT-bcidoXqFrMslawpirqtrWCgiDq88speBDbP82_V0xQVY2Ny3AyK-W86PwXuzfC-np1tgxYFsnnHQa2ySy_evNevdwVyVPkx_NVD8c', start_index=7501)
Annotation(end_index=7709, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7GYoi2I8D0vAVv4e0tiEoFqTxfYcc2Nr6nuCFn8SiVOm9attos-NVwDKJ0l9uNbTgokWVFD3LToBhEB3IX2wwOGA05k7UsAU_5u31vVFCEM3LvZD0atWONbWuwk3rg-uaS9AKcACojrobbUZX50VnFIoGT5aMGciBwfDcgNxpUl-xxAN5KOm2rVQ0h3W-cCeB_BEcwJMHBGk07ZydInm_06XT70vIB1ohg2SJQRTxUAq1PiWm0p-RyAU=', start_index=7695)
Annotation(end_index=7709, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMqz-h9tCp4VBf8recVvTEsth-qomJFln-JvA6RXznBN7FjRoqGhxh-e5xHU2N3i9-vFZifjAf3bdx3TeAMS87_Ijd7TkwNAMifBbKHxZdXAfCWRqamNBlpxYKAUghnrawtos=', start_index=7695)
Annotation(end_index=8148, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGw1IL4X0UV2kZiyboERXZH6e5K01HBj2au3DZm4J8bIr4mo--DymfszhEgqvoPBmAgwPQC8JeUoThmICYhOfPwmUKIG7_H3EkTfVhboJyOqLXypJpt4rWL0J3jewiDHLMDxMTX8HKcTlBDbSnet8ABRNprVjaUSpvi1aEQyF4I9fUci3TlB-UKNIOYNJ04yksw1_6Uh7VYIP4HYBs1I0pnzll4Fg_z-By3byAKLxRvR8h3MPHqzfbdinAWRKzCjVy6xyO85BLEfYRAvz77GmsM7ZGw7IqnNBB5frqND80rAj_Nkb1dQXGjGszrkOxpR1RpjV1O', start_index=8134)
Annotation(end_index=8148, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5TZTWgU6whIYKrIB6gRt5sV_JD-NROCkzoT-bcidoXqFrMslawpirqtrWCgiDq88speBDbP82_V0xQVY2Ny3AyK-W86PwXuzfC-np1tgxYFsnnHQa2ySy_evNevdwVyVPkx_NVD8c', start_index=8134)
Annotation(end_index=8372, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7GYoi2I8D0vAVv4e0tiEoFqTxfYcc2Nr6nuCFn8SiVOm9attos-NVwDKJ0l9uNbTgokWVFD3LToBhEB3IX2wwOGA05k7UsAU_5u31vVFCEM3LvZD0atWONbWuwk3rg-uaS9AKcACojrobbUZX50VnFIoGT5aMGciBwfDcgNxpUl-xxAN5KOm2rVQ0h3W-cCeB_BEcwJMHBGk07ZydInm_06XT70vIB1ohg2SJQRTxUAq1PiWm0p-RyAU=', start_index=8358)
Annotation(end_index=8372, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMqz-h9tCp4VBf8recVvTEsth-qomJFln-JvA6RXznBN7FjRoqGhxh-e5xHU2N3i9-vFZifjAf3bdx3TeAMS87_Ijd7TkwNAMifBbKHxZdXAfCWRqamNBlpxYKAUghnrawtos=', start_index=8358)
Annotation(end_index=8646, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIovdo1pt58VyYVy20stJP3KM0Bp4DShkMbd3Qp0efAdjzNycOkZamxZvPDm5D9KGUhc_E1pKE2Kn3V8YiNYBdOSbIt_6-hfW99JP8xGF1wTpxzfi-Bwesyb2FxFaR550C2YCVqqVOcprGF7Pr4dGcM1-DiRHuNN4n', start_index=8633)
Annotation(end_index=8646, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5TZTWgU6whIYKrIB6gRt5sV_JD-NROCkzoT-bcidoXqFrMslawpirqtrWCgiDq88speBDbP82_V0xQVY2Ny3AyK-W86PwXuzfC-np1tgxYFsnnHQa2ySy_evNevdwVyVPkx_NVD8c', start_index=8633)
Annotation(end_index=9299, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIovdo1pt58VyYVy20stJP3KM0Bp4DShkMbd3Qp0efAdjzNycOkZamxZvPDm5D9KGUhc_E1pKE2Kn3V8YiNYBdOSbIt_6-hfW99JP8xGF1wTpxzfi-Bwesyb2FxFaR550C2YCVqqVOcprGF7Pr4dGcM1-DiRHuNN4n', start_index=9286)
Annotation(end_index=9299, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVicaWeivtACeK5CjSaaEGcXst2EAShBCev7tyDRk5uLvun-7-Oeo60cN0Sz3Uwh4ykooy2JYz4FAhoe2nNt2ZodnfSl1Y8-Y396bTq8-MdRM8wQ4UwajJ4gOfA4Q-43xrEBRM1oswtY6iFCchfl6AcOQQJ7lGtXqeTOkXyBfFYDBedVhEatSTCMP2aEmexMPzXIe__HTWE0pRR9NhPx6wNcLKO6LCM9G38UJMnmSvwcJbj9wd3mpHnUa4kurhKH0VWru_jucU5_k3tZqpXtKgquN9uhBS-L88IChgMb4sKQWbcY4VtCics0Emek8Ha2RXzoAtJeqSBHGK0w==', start_index=9286)
Annotation(end_index=10978, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9f_OzzAkMOw3GSAYUl6W8OztQKjf75lGHXRiXwwT76epGXYSQhf2jKEAL4XU6xyLx1jjPUw3f42uEHdtf23AXI3BEbhDglUnre1QrZgf2TWBar6JXm9wHLJ2GLgKDqKQkjjs4huwOfbrbpXJmDYvjI_QB0wQiTUMxbkU3LRpIUREpFekexV0Hbr913QC4wkKE1BDONs1rke5up8eJacUjLw3LRVmjkVMAauJJ5bYzgMVQHMYv5AXvT8fKTEgGH6a-CSMEMA==', start_index=10965)
Annotation(end_index=10978, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmwNLgIu7SpCOuLRHLaY6cMhfYKyiaOcr9bIEQzj71VZHe14NDl7w2sxK0qy0oo8HOSCVcwwLmywzNtXjayBFf2OCXRQNi1lExbOzttNeU-kN9vh-H5yBl3kW7a0rTBMGnucuuEJDg0GWYlJJlH8uMpPB3rmHIkbsac48KIrc68tferad37Axoc71evmISjp_RDIMU34dmngk6KqhgD2wl_jTzCfqZLl1Ne6siWw==', start_index=10965)
Annotation(end_index=11077, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIovdo1pt58VyYVy20stJP3KM0Bp4DShkMbd3Qp0efAdjzNycOkZamxZvPDm5D9KGUhc_E1pKE2Kn3V8YiNYBdOSbIt_6-hfW99JP8xGF1wTpxzfi-Bwesyb2FxFaR550C2YCVqqVOcprGF7Pr4dGcM1-DiRHuNN4n', start_index=11068)
Annotation(end_index=11331, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTNwqpoFusBrFqTyStAYAQMX0ecNOPoPkVdQwF_dxEPrdYcEqSQ5cvdxiO-1RKiPoqz9fVdABnIDQdpnvoDwZPPZAAoY8Hq38m12GObggnZWaLd2sCU91D44uvFJegJ5nij2a88DFTQruX4tHHAJ3ItV3ifFA3SRFWQGXsxNEf2sKh5POPp7ABoRikDiE99GxVjFLJw2hd6B6JOQ==', start_index=11318)
Annotation(end_index=11331, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCIVNbB33u6YTHKzBL2I45aFXk_NRVWg5JewxWy-yGMXFnir6Tk2643IXkZ3ELDd4Y74m8BSnGDPjNv-z-yEBzUIT-Tu1eHT83G55kZijnMABvGXfEkBG8zPP-Iiumry-V5So3-KQqEQPbsL_bGwiqYbP4jwq6xPlU0AVAgJPfCq9izPdEDu_TTAzatyo=', start_index=11318)
Annotation(end_index=11597, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFS3jazFyjIIIVIA_xTEj2mTHGe6qmXV3aBUcNBsK-a-NLIvmaGiL0gq1bmQ0gB4mxdX08lQLp-JrJQ8Caag1c4Mz1brJ-Vp2Vbdb3UUI6m8uzI5ZRlHmdZrzAtGe0GLjQaDa2mnS64vUfckMc=', start_index=11583)
Annotation(end_index=11597, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVicaWeivtACeK5CjSaaEGcXst2EAShBCev7tyDRk5uLvun-7-Oeo60cN0Sz3Uwh4ykooy2JYz4FAhoe2nNt2ZodnfSl1Y8-Y396bTq8-MdRM8wQ4UwajJ4gOfA4Q-43xrEBRM1oswtY6iFCchfl6AcOQQJ7lGtXqeTOkXyBfFYDBedVhEatSTCMP2aEmexMPzXIe__HTWE0pRR9NhPx6wNcLKO6LCM9G38UJMnmSvwcJbj9wd3mpHnUa4kurhKH0VWru_jucU5_k3tZqpXtKgquN9uhBS-L88IChgMb4sKQWbcY4VtCics0Emek8Ha2RXzoAtJeqSBHGK0w==', start_index=11583)
Annotation(end_index=12002, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmwNLgIu7SpCOuLRHLaY6cMhfYKyiaOcr9bIEQzj71VZHe14NDl7w2sxK0qy0oo8HOSCVcwwLmywzNtXjayBFf2OCXRQNi1lExbOzttNeU-kN9vh-H5yBl3kW7a0rTBMGnucuuEJDg0GWYlJJlH8uMpPB3rmHIkbsac48KIrc68tferad37Axoc71evmISjp_RDIMU34dmngk6KqhgD2wl_jTzCfqZLl1Ne6siWw==', start_index=11988)
Annotation(end_index=12002, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVicaWeivtACeK5CjSaaEGcXst2EAShBCev7tyDRk5uLvun-7-Oeo60cN0Sz3Uwh4ykooy2JYz4FAhoe2nNt2ZodnfSl1Y8-Y396bTq8-MdRM8wQ4UwajJ4gOfA4Q-43xrEBRM1oswtY6iFCchfl6AcOQQJ7lGtXqeTOkXyBfFYDBedVhEatSTCMP2aEmexMPzXIe__HTWE0pRR9NhPx6wNcLKO6LCM9G38UJMnmSvwcJbj9wd3mpHnUa4kurhKH0VWru_jucU5_k3tZqpXtKgquN9uhBS-L88IChgMb4sKQWbcY4VtCics0Emek8Ha2RXzoAtJeqSBHGK0w==', start_index=11988)
Annotation(end_index=12474, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYMJout3HGtk-qQt3kCBsI4vVXhoOzybSCt5NGsKv_arMY3_gnq-WKHzBVvkYVtryP4-SIf1HtyzzMZBrsDtgd8uq5PKlTIf1S1VrWdGR9CG3621DB9RtdVKwTUXBXzB_B9GIXyY--93rmEJXGftU9e7f0bOp7MHOKijqQb6vgWujMkHI9RAhli5fJHd6a3wKXxxe8MmNngzG24BPgQSHf6LK1OJlA36u5YoOl6_h6PcNXZARZzcNjE0EJVyrX_Mcyfa0H4JCCez6u4A==', start_index=12460)
Annotation(end_index=12474, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbJbdztJ1Iclg5CKAkhPHGU03errc6zDFQqYH3T9MkvmK2FWvfEDge8cwahdL-SdgAQsMRrIS9NlOjDpm5Udy6uAT3pzD-6lWoMHY-oRHYHf9rWScHn6shDjGoa8U72yelOsLameqtFkJO1888inF44KoIcE2U3mrtOiWToQ==', start_index=12460)
Annotation(end_index=12865, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF960icuG8jm5HhmM334rqthcYe_UPF1sX7wms_nh7E8-uDSTbO4oZbw6lrP1xJemxqT7cJAPZLEKRzQSDSMwkszrRTOZEomMiThFZfUrDvop9kE2RmHWy3sXFWx7P0G04hexxlqsVo52LMImLGzU74ZHvvYKj7_mxOXnGzPT3eOoOYkSPTSbvRRcEPD4Mk6ZCBeBCGKjErCZxchXr_C7y9FgLKpP0z6AEaK_sLgtSBxA==', start_index=12851)
Annotation(end_index=12865, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQESfbywzBY5QHhrN8xy-8kES0i7tyMsubH3E8pf-5ETuNC9qhuM0J5BLfS7lBpcCdMAKfIhQPN9vk0VQyl7JRZCnufHrTgULzyxIdwsnO7l6lGEf1hJlscyuddzrIh590Gy-TZiX1xhsw3CYyX5-Qn8GFO8avanDUsLR-qzN7yVGlAH4ote_3NHZtS6mTX1VmzvIlIk3wdn7UKgGB0Y1b8gXVCueCICxxqSuJCq8vDtlv1B6gFsfyaKHozZNcDFOHSxm9--o=', start_index=12851)
Annotation(end_index=13150, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmiZLYU8bmAkfkcLgSC4RptJnA_VLqet3GGKIpAhj6ovfz3gbX0_m4vQTajxCGyesNBibxsk-iqxlSXIx_NgGL-yQ3wAz6NkeIetADeLuEYV2tCjblAlQgnFw4bo-ynJuI9AzSCjKcC8U4MS3IkdoZuqnm2V-VtFw=', start_index=13136)
Annotation(end_index=13150, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGB17W0OFN9t4tt4Nax3wa1DbuDIOOwY6Z0V8BwMTD3XIYFi1_lJxNKftoEE9nPSvHD_f80BHQXTMbqGemlk7UW4TkDEELVsm2_vHGEhcWFVZpMY2TMPYIyDIM9Sf2KJhd6VkUlo5SWFYsu9fMuraC5uEUHhqF48ZL48bZi-VH-RKTfMbqRGHJCYb-3u3QMoi9dYA-5bS4JTBtk3Rh94Wr6Yzq5zoZfYluYF-f3I9NvjQJhO9vGU_LW0KYZ2qL2l-4O_Xd3F7xkfSl1ZcHVZb_IcWdrzw_JwIEeO2EQ', start_index=13136)
Annotation(end_index=13504, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9f_OzzAkMOw3GSAYUl6W8OztQKjf75lGHXRiXwwT76epGXYSQhf2jKEAL4XU6xyLx1jjPUw3f42uEHdtf23AXI3BEbhDglUnre1QrZgf2TWBar6JXm9wHLJ2GLgKDqKQkjjs4huwOfbrbpXJmDYvjI_QB0wQiTUMxbkU3LRpIUREpFekexV0Hbr913QC4wkKE1BDONs1rke5up8eJacUjLw3LRVmjkVMAauJJ5bYzgMVQHMYv5AXvT8fKTEgGH6a-CSMEMA==', start_index=13491)
Annotation(end_index=13504, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsgavGmZDXRI9Zk9IRT2GInGSo6z2f366RJ2bo6pRJ8WiCg1KVRf1z3vIGym6VDU0Gqar8YPdfrLTuzFVjS-tcRKgBAGp0QOFRg4HGkrXqUca4GmfAOLJebN-Wn7fP3YcFqPrd5pc0tpbf6tmUEnU_h_lDPLb2px6b4_Ntv0VeNe0-xZzAcrWdmbah5QGVAkfckEgYQAT8Q0hg4v3RrW7mk8hk3sJ6ZUg491DwY8eO97Sn1M0YPpfO5R4YGt_xPQkE3LSo9eCwWdVuS_JWs6Lyn-LuVBNV-fqMoLA1nVsmTYIMZZ8=', start_index=13491)
Annotation(end_index=13991, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYMJout3HGtk-qQt3kCBsI4vVXhoOzybSCt5NGsKv_arMY3_gnq-WKHzBVvkYVtryP4-SIf1HtyzzMZBrsDtgd8uq5PKlTIf1S1VrWdGR9CG3621DB9RtdVKwTUXBXzB_B9GIXyY--93rmEJXGftU9e7f0bOp7MHOKijqQb6vgWujMkHI9RAhli5fJHd6a3wKXxxe8MmNngzG24BPgQSHf6LK1OJlA36u5YoOl6_h6PcNXZARZzcNjE0EJVyrX_Mcyfa0H4JCCez6u4A==', start_index=13973)
Annotation(end_index=13991, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmiZLYU8bmAkfkcLgSC4RptJnA_VLqet3GGKIpAhj6ovfz3gbX0_m4vQTajxCGyesNBibxsk-iqxlSXIx_NgGL-yQ3wAz6NkeIetADeLuEYV2tCjblAlQgnFw4bo-ynJuI9AzSCjKcC8U4MS3IkdoZuqnm2V-VtFw=', start_index=13973)
Annotation(end_index=13991, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQESfbywzBY5QHhrN8xy-8kES0i7tyMsubH3E8pf-5ETuNC9qhuM0J5BLfS7lBpcCdMAKfIhQPN9vk0VQyl7JRZCnufHrTgULzyxIdwsnO7l6lGEf1hJlscyuddzrIh590Gy-TZiX1xhsw3CYyX5-Qn8GFO8avanDUsLR-qzN7yVGlAH4ote_3NHZtS6mTX1VmzvIlIk3wdn7UKgGB0Y1b8gXVCueCICxxqSuJCq8vDtlv1B6gFsfyaKHozZNcDFOHSxm9--o=', start_index=13973)
Annotation(end_index=14559, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9f_OzzAkMOw3GSAYUl6W8OztQKjf75lGHXRiXwwT76epGXYSQhf2jKEAL4XU6xyLx1jjPUw3f42uEHdtf23AXI3BEbhDglUnre1QrZgf2TWBar6JXm9wHLJ2GLgKDqKQkjjs4huwOfbrbpXJmDYvjI_QB0wQiTUMxbkU3LRpIUREpFekexV0Hbr913QC4wkKE1BDONs1rke5up8eJacUjLw3LRVmjkVMAauJJ5bYzgMVQHMYv5AXvT8fKTEgGH6a-CSMEMA==', start_index=14543)
Annotation(end_index=14559, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEL5ktRwVURrQQ51DTE-b7_jUlXDDLiUNZOw3xSiovgauNbnh65jemJyKQVxxk-WmIPCYT1AvH7aHkHV8TT3OjQLnTsLRVaYSI2avImpsnBSaitYtYG9F58ulOwXAagcJFeXu_iTwZZKbxrBoEDyMdXXisbXDX4J9cr3HG2ngJsRtDkTHHzKrWkgWSGl2CNHJkVTQxl8U1lMaaqt-BPZwkreWWN-amDRNmxi6OnZa055XzqM8mEB2bnZtySiEBj2hCYQctqgfwdthe2kArrpdw6hWEXc8KZPg6HC-nR_GKneYlW-n7_2VLQ-Chnv6AX', start_index=14543)
Annotation(end_index=14559, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRL_1U7kHKKRN5Hfop6lIbPWTkFKNDbny9RJYPg-Bqce-6-5yz8WIo1Y-OyaTU37xSmrJImwkq2324jrfbmQ4FxGQfPGffmJT_nTdZZsbUdwH-XJM1L-DWBv6BPixjMUEYvkEoqwM1Q5qYQxG5YKiTWns1TCXgX3upjs0vpoUJAXfUpQ_k5rGu5XPr1RmC9-0xC9pz4GYLn2Ocn2v_cbGvAw==', start_index=14543)
Annotation(end_index=14879, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9f_OzzAkMOw3GSAYUl6W8OztQKjf75lGHXRiXwwT76epGXYSQhf2jKEAL4XU6xyLx1jjPUw3f42uEHdtf23AXI3BEbhDglUnre1QrZgf2TWBar6JXm9wHLJ2GLgKDqKQkjjs4huwOfbrbpXJmDYvjI_QB0wQiTUMxbkU3LRpIUREpFekexV0Hbr913QC4wkKE1BDONs1rke5up8eJacUjLw3LRVmjkVMAauJJ5bYzgMVQHMYv5AXvT8fKTEgGH6a-CSMEMA==', start_index=14866)
Annotation(end_index=14879, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsgavGmZDXRI9Zk9IRT2GInGSo6z2f366RJ2bo6pRJ8WiCg1KVRf1z3vIGym6VDU0Gqar8YPdfrLTuzFVjS-tcRKgBAGp0QOFRg4HGkrXqUca4GmfAOLJebN-Wn7fP3YcFqPrd5pc0tpbf6tmUEnU_h_lDPLb2px6b4_Ntv0VeNe0-xZzAcrWdmbah5QGVAkfckEgYQAT8Q0hg4v3RrW7mk8hk3sJ6ZUg491DwY8eO97Sn1M0YPpfO5R4YGt_xPQkE3LSo9eCwWdVuS_JWs6Lyn-LuVBNV-fqMoLA1nVsmTYIMZZ8=', start_index=14866)
Annotation(end_index=15099, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsgavGmZDXRI9Zk9IRT2GInGSo6z2f366RJ2bo6pRJ8WiCg1KVRf1z3vIGym6VDU0Gqar8YPdfrLTuzFVjS-tcRKgBAGp0QOFRg4HGkrXqUca4GmfAOLJebN-Wn7fP3YcFqPrd5pc0tpbf6tmUEnU_h_lDPLb2px6b4_Ntv0VeNe0-xZzAcrWdmbah5QGVAkfckEgYQAT8Q0hg4v3RrW7mk8hk3sJ6ZUg491DwY8eO97Sn1M0YPpfO5R4YGt_xPQkE3LSo9eCwWdVuS_JWs6Lyn-LuVBNV-fqMoLA1nVsmTYIMZZ8=', start_index=15089)
Annotation(end_index=15801, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9f_OzzAkMOw3GSAYUl6W8OztQKjf75lGHXRiXwwT76epGXYSQhf2jKEAL4XU6xyLx1jjPUw3f42uEHdtf23AXI3BEbhDglUnre1QrZgf2TWBar6JXm9wHLJ2GLgKDqKQkjjs4huwOfbrbpXJmDYvjI_QB0wQiTUMxbkU3LRpIUREpFekexV0Hbr913QC4wkKE1BDONs1rke5up8eJacUjLw3LRVmjkVMAauJJ5bYzgMVQHMYv5AXvT8fKTEgGH6a-CSMEMA==', start_index=15784)
Annotation(end_index=15801, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEG9a3Y9q5zbzfNd04xakzgkEE0w6_0HglVM2yP5udvADx7uFQI6JwGaZ4IdwdDgA_5evkWcIqF-5T0en65d-CyBva8RW_8gtEEy3NVYUC20jVwdLEraQCvfVMmvEnmKJrFfQF3-nU335KMBCyk56sta1QYHgk=', start_index=15784)
Annotation(end_index=15801, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZvB5r-gn45OG0NQJyM-8qJfxWVMLzZXbGuWdGrhs5dM1qaNSi-QFF_XIizUPiLq9d1h2KeJ12c8D-xELfLHQYccYimbe-vYQDwtiedh5z0HlOv40-cr_Mtr8RT7ed7xI3MwRdF8GMqUK7ltcQlulJ-go7H3xRiy92x5JAQ1_y3Eauq5hFIJaNTFtITW049tN91q1S5SeXiVMCDBTGZcSa', start_index=15784)
Annotation(end_index=16395, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIovdo1pt58VyYVy20stJP3KM0Bp4DShkMbd3Qp0efAdjzNycOkZamxZvPDm5D9KGUhc_E1pKE2Kn3V8YiNYBdOSbIt_6-hfW99JP8xGF1wTpxzfi-Bwesyb2FxFaR550C2YCVqqVOcprGF7Pr4dGcM1-DiRHuNN4n', start_index=16382)
Annotation(end_index=16395, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5TZTWgU6whIYKrIB6gRt5sV_JD-NROCkzoT-bcidoXqFrMslawpirqtrWCgiDq88speBDbP82_V0xQVY2Ny3AyK-W86PwXuzfC-np1tgxYFsnnHQa2ySy_evNevdwVyVPkx_NVD8c', start_index=16382)
Annotation(end_index=16670, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPa-X2xC90hQ-vXbn0iYwddFnefoEFl9lACu8-KfFgDHIfSZ3Lyw7gx_Rq476PaEYRFxtztV0h9bHVahNZSnBaab8uibZEEY7Ryh3UUSj18KION1CafMwGcCocWvpA949Dn0EqGaKnuUYjS3NBc6mQGsLLoGHaFI_Pxin35lcbL027YsBB-tjgxXl-Wzs0frUmAVT1tNShhGLbi3z2FIkvJEQQMucyykIV430f8iwpInyZQmyMXwK0L0S6viFk-iIHoYxXThH47dl4YrxXUVqYzv72_VinfPz7mIsYYOTXwTgRqkOcDSLBG51gPBZ1hEkxIyB0Y5yzFJ13rUA=', start_index=16661)
Annotation(end_index=16805, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzTpCGO8PshnMnsX5HGhGdRDIhL_5cydL_20OZXmSkqc2tkzVwmYABDvS_dyVekR6NUqj6cLhSQOwa7tDarQ6UJqMKdy4JgMw_IsLVTMWFaxV8mxhV6w0NGm8176LJ2Sfxt_2ernQ=', start_index=16792)
Annotation(end_index=16805, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPa-X2xC90hQ-vXbn0iYwddFnefoEFl9lACu8-KfFgDHIfSZ3Lyw7gx_Rq476PaEYRFxtztV0h9bHVahNZSnBaab8uibZEEY7Ryh3UUSj18KION1CafMwGcCocWvpA949Dn0EqGaKnuUYjS3NBc6mQGsLLoGHaFI_Pxin35lcbL027YsBB-tjgxXl-Wzs0frUmAVT1tNShhGLbi3z2FIkvJEQQMucyykIV430f8iwpInyZQmyMXwK0L0S6viFk-iIHoYxXThH47dl4YrxXUVqYzv72_VinfPz7mIsYYOTXwTgRqkOcDSLBG51gPBZ1hEkxIyB0Y5yzFJ13rUA=', start_index=16792)
Annotation(end_index=17013, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKFyqS5Tti7nTgFN3zSut__vyWhwC3MD4HaU8xJHy1VzEuasp5vGGj81doLvRBTo59gL_FxEyT0f6GforIVdeSy89Lh3FJ4oPlF9URpEHH4cMtPdegVpTIqDcKPR2WBNbIpBoLbr3Cy7OfJ7Ny5krnvwq8HNHGt2Zy0fl1sy1XiYMzb9D9atYcef8OMmsxW8YjesI=', start_index=17004)
Annotation(end_index=17369, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKFyqS5Tti7nTgFN3zSut__vyWhwC3MD4HaU8xJHy1VzEuasp5vGGj81doLvRBTo59gL_FxEyT0f6GforIVdeSy89Lh3FJ4oPlF9URpEHH4cMtPdegVpTIqDcKPR2WBNbIpBoLbr3Cy7OfJ7Ny5krnvwq8HNHGt2Zy0fl1sy1XiYMzb9D9atYcef8OMmsxW8YjesI=', start_index=17360)
Annotation(end_index=17656, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGw1IL4X0UV2kZiyboERXZH6e5K01HBj2au3DZm4J8bIr4mo--DymfszhEgqvoPBmAgwPQC8JeUoThmICYhOfPwmUKIG7_H3EkTfVhboJyOqLXypJpt4rWL0J3jewiDHLMDxMTX8HKcTlBDbSnet8ABRNprVjaUSpvi1aEQyF4I9fUci3TlB-UKNIOYNJ04yksw1_6Uh7VYIP4HYBs1I0pnzll4Fg_z-By3byAKLxRvR8h3MPHqzfbdinAWRKzCjVy6xyO85BLEfYRAvz77GmsM7ZGw7IqnNBB5frqND80rAj_Nkb1dQXGjGszrkOxpR1RpjV1O', start_index=17642)
Annotation(end_index=17656, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJyGGHN4wvO3TFsdt7sYPBGgLqPnrlktn_ZA-0S0bys0E3OLoUrp4fktRqmhD3XC0pHxmkSxTLuPMQF1dgDEAgICHf1LlSoQxWYxXkTKDJ-l_uhYCHLNy1hrqWk5dt-c_G5TpDvAGYJD6Oo8bwtl8Jx11V_DIkzo4GzfdL2kfAN8kFlZfsWSu9SVjZ9pnRS7qWd1brUzRiH556q89sdQmNpeK42LTwhZ9szU4nGxhkrpRnWRau-Uk2Ulpb4HOFP0hpAjifF4rgIswm8qIJIovwW4OjcnwOEpLHXRrrwMtB4tuA5dEg9G0CyQGHilLLbglSvqBYITG-L8yRlIFkMIMFRN2wWcBDsdDmrRuhPfy7ATxC', start_index=17642)
Annotation(end_index=17783, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGw1IL4X0UV2kZiyboERXZH6e5K01HBj2au3DZm4J8bIr4mo--DymfszhEgqvoPBmAgwPQC8JeUoThmICYhOfPwmUKIG7_H3EkTfVhboJyOqLXypJpt4rWL0J3jewiDHLMDxMTX8HKcTlBDbSnet8ABRNprVjaUSpvi1aEQyF4I9fUci3TlB-UKNIOYNJ04yksw1_6Uh7VYIP4HYBs1I0pnzll4Fg_z-By3byAKLxRvR8h3MPHqzfbdinAWRKzCjVy6xyO85BLEfYRAvz77GmsM7ZGw7IqnNBB5frqND80rAj_Nkb1dQXGjGszrkOxpR1RpjV1O', start_index=17773)
Annotation(end_index=19212, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKFyqS5Tti7nTgFN3zSut__vyWhwC3MD4HaU8xJHy1VzEuasp5vGGj81doLvRBTo59gL_FxEyT0f6GforIVdeSy89Lh3FJ4oPlF9URpEHH4cMtPdegVpTIqDcKPR2WBNbIpBoLbr3Cy7OfJ7Ny5krnvwq8HNHGt2Zy0fl1sy1XiYMzb9D9atYcef8OMmsxW8YjesI=', start_index=19203)
Annotation(end_index=19359, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1KWz_7A0aSfBrjtMVJscg_A_RjU16qddc0t4FbFo5N7R6RaufUw8X0I_hVYhyfZcC87AuycFZQ3GEhK124jbZQHC9eWHjQpWC_mzGNSlXTIXGzKyASxlnV7bgeam8oSHkn4uiLADMJwxp0sPRy3UjLrUeWI0DkbuydvWN8H_86oYuIkZMzWXJnjP1ty-ivou19whqKDzDCS5CIfpg0KLYVnFok7j7B0FtcEr0YNw_', start_index=19350)
Annotation(end_index=19438, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTNwqpoFusBrFqTyStAYAQMX0ecNOPoPkVdQwF_dxEPrdYcEqSQ5cvdxiO-1RKiPoqz9fVdABnIDQdpnvoDwZPPZAAoY8Hq38m12GObggnZWaLd2sCU91D44uvFJegJ5nij2a88DFTQruX4tHHAJ3ItV3ifFA3SRFWQGXsxNEf2sKh5POPp7ABoRikDiE99GxVjFLJw2hd6B6JOQ==', start_index=19425)
Annotation(end_index=19438, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCIVNbB33u6YTHKzBL2I45aFXk_NRVWg5JewxWy-yGMXFnir6Tk2643IXkZ3ELDd4Y74m8BSnGDPjNv-z-yEBzUIT-Tu1eHT83G55kZijnMABvGXfEkBG8zPP-Iiumry-V5So3-KQqEQPbsL_bGwiqYbP4jwq6xPlU0AVAgJPfCq9izPdEDu_TTAzatyo=', start_index=19425)
Annotation(end_index=19521, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRL_1U7kHKKRN5Hfop6lIbPWTkFKNDbny9RJYPg-Bqce-6-5yz8WIo1Y-OyaTU37xSmrJImwkq2324jrfbmQ4FxGQfPGffmJT_nTdZZsbUdwH-XJM1L-DWBv6BPixjMUEYvkEoqwM1Q5qYQxG5YKiTWns1TCXgX3upjs0vpoUJAXfUpQ_k5rGu5XPr1RmC9-0xC9pz4GYLn2Ocn2v_cbGvAw==', start_index=19508)
Annotation(end_index=19521, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_zS72vaW-R3nejP7F5S1zW04_TrS7K_ZNfM2paj0RVRhzGbnRPUWXK8-Ce3dt2nsc4cLnvOOsuYdV4CPSJuXoq6rlYk9GsiGhyVoOsihF-WcQg4LLFWQL3e4zTehaQrHgrbr32A==', start_index=19508)
Annotation(end_index=19655, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7GYoi2I8D0vAVv4e0tiEoFqTxfYcc2Nr6nuCFn8SiVOm9attos-NVwDKJ0l9uNbTgokWVFD3LToBhEB3IX2wwOGA05k7UsAU_5u31vVFCEM3LvZD0atWONbWuwk3rg-uaS9AKcACojrobbUZX50VnFIoGT5aMGciBwfDcgNxpUl-xxAN5KOm2rVQ0h3W-cCeB_BEcwJMHBGk07ZydInm_06XT70vIB1ohg2SJQRTxUAq1PiWm0p-RyAU=', start_index=19645)
Annotation(end_index=19747, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsgavGmZDXRI9Zk9IRT2GInGSo6z2f366RJ2bo6pRJ8WiCg1KVRf1z3vIGym6VDU0Gqar8YPdfrLTuzFVjS-tcRKgBAGp0QOFRg4HGkrXqUca4GmfAOLJebN-Wn7fP3YcFqPrd5pc0tpbf6tmUEnU_h_lDPLb2px6b4_Ntv0VeNe0-xZzAcrWdmbah5QGVAkfckEgYQAT8Q0hg4v3RrW7mk8hk3sJ6ZUg491DwY8eO97Sn1M0YPpfO5R4YGt_xPQkE3LSo9eCwWdVuS_JWs6Lyn-LuVBNV-fqMoLA1nVsmTYIMZZ8=', start_index=19737)
Annotation(end_index=19865, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9f_OzzAkMOw3GSAYUl6W8OztQKjf75lGHXRiXwwT76epGXYSQhf2jKEAL4XU6xyLx1jjPUw3f42uEHdtf23AXI3BEbhDglUnre1QrZgf2TWBar6JXm9wHLJ2GLgKDqKQkjjs4huwOfbrbpXJmDYvjI_QB0wQiTUMxbkU3LRpIUREpFekexV0Hbr913QC4wkKE1BDONs1rke5up8eJacUjLw3LRVmjkVMAauJJ5bYzgMVQHMYv5AXvT8fKTEgGH6a-CSMEMA==', start_index=19849)
Annotation(end_index=19865, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzTpCGO8PshnMnsX5HGhGdRDIhL_5cydL_20OZXmSkqc2tkzVwmYABDvS_dyVekR6NUqj6cLhSQOwa7tDarQ6UJqMKdy4JgMw_IsLVTMWFaxV8mxhV6w0NGm8176LJ2Sfxt_2ernQ=', start_index=19849)
Annotation(end_index=19865, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPa-X2xC90hQ-vXbn0iYwddFnefoEFl9lACu8-KfFgDHIfSZ3Lyw7gx_Rq476PaEYRFxtztV0h9bHVahNZSnBaab8uibZEEY7Ryh3UUSj18KION1CafMwGcCocWvpA949Dn0EqGaKnuUYjS3NBc6mQGsLLoGHaFI_Pxin35lcbL027YsBB-tjgxXl-Wzs0frUmAVT1tNShhGLbi3z2FIkvJEQQMucyykIV430f8iwpInyZQmyMXwK0L0S6viFk-iIHoYxXThH47dl4YrxXUVqYzv72_VinfPz7mIsYYOTXwTgRqkOcDSLBG51gPBZ1hEkxIyB0Y5yzFJ13rUA=', start_index=19849)
Annotation(end_index=19980, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcnziE7i2xWRQvfqQ0oELoeLWL76K7jFU7VW2sj08PsryT9YuzGsF3qmKv15KLQ9L6Vh2RGHRaviTb8b9u_oDvJBzX-M470gRolt5tA9fcUi1qte_ZH_uSw6pQtSdQtHShi0ZQz18=', start_index=19967)
Annotation(end_index=19980, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIovdo1pt58VyYVy20stJP3KM0Bp4DShkMbd3Qp0efAdjzNycOkZamxZvPDm5D9KGUhc_E1pKE2Kn3V8YiNYBdOSbIt_6-hfW99JP8xGF1wTpxzfi-Bwesyb2FxFaR550C2YCVqqVOcprGF7Pr4dGcM1-DiRHuNN4n', start_index=19967)
Annotation(end_index=20079, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYMJout3HGtk-qQt3kCBsI4vVXhoOzybSCt5NGsKv_arMY3_gnq-WKHzBVvkYVtryP4-SIf1HtyzzMZBrsDtgd8uq5PKlTIf1S1VrWdGR9CG3621DB9RtdVKwTUXBXzB_B9GIXyY--93rmEJXGftU9e7f0bOp7MHOKijqQb6vgWujMkHI9RAhli5fJHd6a3wKXxxe8MmNngzG24BPgQSHf6LK1OJlA36u5YoOl6_h6PcNXZARZzcNjE0EJVyrX_Mcyfa0H4JCCez6u4A==', start_index=20069)
Annotation(end_index=20200, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmwNLgIu7SpCOuLRHLaY6cMhfYKyiaOcr9bIEQzj71VZHe14NDl7w2sxK0qy0oo8HOSCVcwwLmywzNtXjayBFf2OCXRQNi1lExbOzttNeU-kN9vh-H5yBl3kW7a0rTBMGnucuuEJDg0GWYlJJlH8uMpPB3rmHIkbsac48KIrc68tferad37Axoc71evmISjp_RDIMU34dmngk6KqhgD2wl_jTzCfqZLl1Ne6siWw==', start_index=20190)
Annotation(end_index=20291, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVicaWeivtACeK5CjSaaEGcXst2EAShBCev7tyDRk5uLvun-7-Oeo60cN0Sz3Uwh4ykooy2JYz4FAhoe2nNt2ZodnfSl1Y8-Y396bTq8-MdRM8wQ4UwajJ4gOfA4Q-43xrEBRM1oswtY6iFCchfl6AcOQQJ7lGtXqeTOkXyBfFYDBedVhEatSTCMP2aEmexMPzXIe__HTWE0pRR9NhPx6wNcLKO6LCM9G38UJMnmSvwcJbj9wd3mpHnUa4kurhKH0VWru_jucU5_k3tZqpXtKgquN9uhBS-L88IChgMb4sKQWbcY4VtCics0Emek8Ha2RXzoAtJeqSBHGK0w==', start_index=20281)
Annotation(end_index=20408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5TZTWgU6whIYKrIB6gRt5sV_JD-NROCkzoT-bcidoXqFrMslawpirqtrWCgiDq88speBDbP82_V0xQVY2Ny3AyK-W86PwXuzfC-np1tgxYFsnnHQa2ySy_evNevdwVyVPkx_NVD8c', start_index=20398)
Annotation(end_index=20485, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEL5ktRwVURrQQ51DTE-b7_jUlXDDLiUNZOw3xSiovgauNbnh65jemJyKQVxxk-WmIPCYT1AvH7aHkHV8TT3OjQLnTsLRVaYSI2avImpsnBSaitYtYG9F58ulOwXAagcJFeXu_iTwZZKbxrBoEDyMdXXisbXDX4J9cr3HG2ngJsRtDkTHHzKrWkgWSGl2CNHJkVTQxl8U1lMaaqt-BPZwkreWWN-amDRNmxi6OnZa055XzqM8mEB2bnZtySiEBj2hCYQctqgfwdthe2kArrpdw6hWEXc8KZPg6HC-nR_GKneYlW-n7_2VLQ-Chnv6AX', start_index=20472)
Annotation(end_index=20485, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgUGBcoF5AJgP_DeKiyAMxo4tMbxNhNqV65MZ_GyN64N3_6kQCiUaFNMWgs5A-V1_B7TmagT1TSm8v-gTKyYEAUM0-jj4ISltoer08lIR4mmRgDSnAnw-LQf6c7GMLlgAjnObdZBKHY_QWT8MWq2RdXn7otIjaocfVN_pQdE7qnPzQ42C6qq5aV6gy4Hoj8_1q', start_index=20472)

## Sources
