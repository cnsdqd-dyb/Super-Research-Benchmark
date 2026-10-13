# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** b8790dae | **Time:** 515.25s | **Cost:** $2.00301
--------------------------------------------------------------------------------

# Comprehensive Analysis of Electrode Array Density in Neural Prostheses: Balancing Signal Resolution with Chronic Biocompatibility

### Executive Summary
The determination of an optimal electrode array density for neural prostheses represents a complex optimization problem governed by two opposing constraints: the physics of extracellular signal acquisition, which demands high spatial sampling to resolve individual neurons, and the biology of the foreign body response (FBR), which penalizes high-density intrusion with tissue encapsulation and neuronal death.

**Key Findings:**
*   **Signal Acquisition:** The effective recording radius of a microelectrode is approximately **50–100 $\mu$m** [cite: 1, 2]. To reliably detect and spike-sort neurons without "blind spots," inter-electrode spacing should ideally be **<40 $\mu$m** along a shank or **<100 $\mu$m** between shanks [cite: 3, 4].
*   **Tissue Tolerance:** Conventional rigid arrays (e.g., Utah arrays) utilize a **400 $\mu$m pitch** to preserve a bridge of healthy tissue between shanks, preventing the merger of glial scars [cite: 5]. Reducing pitch below **100–200 $\mu$m** in rigid "bed-of-nails" architectures significantly increases insertion trauma and vascular damage unless specific mitigation strategies (e.g., electro-sharpening, pneumatic insertion) are employed [cite: 1].
*   **The Optimization Zone:** Recent research suggests that the optimal balance for rigid penetrating arrays lies near a **100 $\mu$m pitch**, provided the electrode tips are electro-sharpened to mitigate compressive tissue strain [cite: 6, 7]. However, for long-term stability, ultra-flexible or "mesh" electronics that decouple the recording site density from the mechanical shank footprint offer the most promising path to high-density recording (e.g., **<20 $\mu$m site spacing**) without triggering chronic rejection [cite: 8, 9].

---

## 1. Introduction: The Density-Damage Trade-off in Brain-Computer Interfaces

The efficacy of intracortical brain-computer interfaces (BCIs) is fundamentally limited by the bandwidth of the neural interface. High-fidelity control of prosthetic devices requires the simultaneous recording of large populations of neurons with single-unit resolution. This demand drives the engineering trend toward High-Density Microelectrode Arrays (HDMEAs), which pack thousands of recording sites into small footprints [cite: 10]. However, the brain is a soft, viscoelastic tissue protected by a vigilant immune system. The insertion of high-density probes triggers a Foreign Body Response (FBR) that can degrade signal quality over time, leading to a "density-damage" trade-off.

The central engineering challenge is to maximize **Volumetric Efficiency**—defined as the number of independent recording channels per unit volume of displaced tissue [cite: 11]—while maintaining the biological viability of the neural microenvironment. This report analyzes the biophysical and biological constraints determining the optimal electrode density, examining the transition from sparse arrays (e.g., Utah arrays) to emerging ultra-high-density systems (e.g., Neuropixels, Paradromics, Neuralink).

---

## 2. Biophysical Constraints on Signal Acquisition

To determine the optimal density for signal acquisition, one must first define the spatial reach of a single electrode and the sampling requirements for isolating individual signal sources (neurons).

### 2.1 The Recording Radius and the "Blind Spot" Problem
Extracellular action potentials (spikes) attenuate rapidly with distance from the somatic source. The amplitude of a recorded spike generally follows an inverse distance relationship ($1/r$ to $1/r^2$), depending on the local conductivity and dipole characteristics.
*   **Effective Radius:** Empirical and modeling studies consistently identify the recording radius of a standard microelectrode to be approximately **50 to 100 $\mu$m** [cite: 1, 2, 12]. Beyond 100 $\mu$m, the signal-to-noise ratio (SNR) typically drops below the threshold required for reliable spike detection [cite: 2, 5].
*   **The Blind Spot:** In sparse arrays, such as the standard Utah array which features a **400 $\mu$m inter-shank pitch**, the recording zones of adjacent electrodes do not overlap. This leaves a "blind spot" of approximately 200–300 $\mu$m of unmonitored tissue between electrodes [cite: 5]. Consequently, sparse arrays sample only a small fraction (<1–10%) of the neurons within the implanted volume [cite: 2, 13].

### 2.2 Optimal Spacing for Spike Sorting
Merely detecting a spike is insufficient; BCIs must often distinguish between multiple neurons firing near the same electrode (spike sorting). High-density spacing allows a single neuron to be recorded on multiple adjacent channels ("oversampling"), which significantly improves sorting accuracy by providing spatial triangulation of the source.
*   **Oversampling Requirement:** Research indicates that to maximize spike sorting efficiency and neuron yield per channel, the optimal inter-electrode spacing is significantly smaller than the recording radius. A spacing of approximately **37 $\mu$m** has been identified as optimal for maximizing the number of well-isolated units in certain high-density configurations [cite: 3].
*   **Vertical vs. Horizontal Density:** Modern silicon probes (e.g., Neuropixels) achieve extremely high vertical density (e.g., **20 $\mu$m pitch**) along a single shank [cite: 14, 15]. This allows for excellent sorting of units along the depth of the cortex but does not address horizontal coverage. The challenge remains in scaling this density horizontally (shank-to-shank) without causing excessive tissue displacement.

### 2.3 Local Field Potentials (LFPs) vs. Spikes
If the goal is recording Local Field Potentials (LFPs) rather than single units, the density requirements are relaxed. LFPs represent the summed synaptic activity of larger populations and correlate over longer distances.
*   **LFP Spacing:** Studies on optimal spacing for electrocorticography (ECoG) and LFP suggest that signals remain highly correlated at sub-millimeter distances. However, to capture non-shared, high-frequency information, spacing as low as **0.6–1.25 mm** is recommended for surface arrays [cite: 16, 17]. For intracortical LFP, densities higher than 400 $\mu$m pitch may yield redundant data unless single-unit resolution is the goal.

---

## 3. Biological Constraints: Tissue Mechanics and the Foreign Body Response

Increasing electrode density inevitably increases the volume of abiotic material introduced into the brain. The biological response to this intrusion is the primary limiter of long-term BCI stability.

### 3.1 The "Bed-of-Nails" Effect and Insertion Trauma
A critical mechanical barrier to high-density arrays is the "bed-of-nails" effect. As the number of shanks increases and inter-shank spacing decreases, the brain tissue tends to dimple and compress under the array rather than being penetrated by the individual needles [cite: 1].
*   **Compression Damage:** This dimpling stores elastic energy in the tissue, which is released as high-velocity strain once the pia mater is punctured. This results in widespread cellular damage and vascular rupture [cite: 1, 18].
*   **Pitch Thresholds:** Standard blunt or planar arrays often struggle to penetrate without excessive force at pitches below **400 $\mu$m**. To achieve higher densities (e.g., **100 $\mu$m pitch**), specialized insertion strategies are required.
*   **Mitigation Strategies:**
    *   **Electro-sharpening:** Sharpening electrode tips (e.g., to <8 degrees) significantly reduces the insertion force and cellular damage, making **100 $\mu$m pitch** arrays viable [cite: 1, 6, 7].
    *   **High-Speed Insertion:** Pneumatic or ballistic insertion can overcome tissue viscoelasticity, reducing dimpling and BBB compromise compared to slow insertion [cite: 1].

### 3.2 The "Kill Zone" and Glial Scarring
Following insertion, the chronic FBR leads to the formation of a glial scar. Microglia and astrocytes encapsulate the electrode, insulating it electrically and chemically.
*   **The Kill Zone:** Histological studies consistently show a zone of reduced neuronal density extending **50–150 $\mu$m** from the electrode surface [cite: 1, 5, 19]. This "kill zone" is caused by mechanical mismatch, chronic inflammation, and neurotoxic factors released by activated microglia.
*   **Merging of Scars:** In sparse arrays (400 $\mu$m pitch), the 50–100 $\mu$m kill zones around adjacent shanks do not overlap, leaving a corridor of healthy tissue that supports the metabolic needs of the remaining neurons. In high-density arrays (e.g., <100–150 $\mu$m pitch), these zones may merge, creating a continuous block of scar tissue that isolates the array from the neural network and prevents nutrient diffusion [cite: 5, 10].

### 3.3 Mechanical Mismatch and Micromotion
The stiffness mismatch between silicon/metal electrodes (~150 GPa) and brain tissue (~kPa) causes chronic trauma due to micromotion (breathing, vascular pulsation).
*   **Density Implication:** Higher density rigid arrays increase the total stiffness and mass of the implant, potentially exacerbating micromotion-induced damage. This necessitates a shift toward flexible materials or subcellular dimensions for high-density applications [cite: 9, 10, 20].

---

## 4. Comparative Analysis of Array Architectures

Different BCI architectures adopt distinct strategies to navigate the density-damage trade-off.

### 4.1 The Utah Array (Standard Density)
*   **Configuration:** 10x10 grid of silicon needles.
*   **Density:** **400 $\mu$m pitch** (inter-shank spacing).
*   **Rationale:** The 400 $\mu$m spacing was chosen to ensure that the "kill zones" of adjacent electrodes do not merge, preserving the viability of the tissue lattice [cite: 5, 21].
*   **Limitations:** Low volumetric efficiency; significant blind spots; rigid mechanics lead to chronic signal loss [cite: 5, 22].

### 4.2 Microwire Bundles (High Density - Paradromics)
*   **Configuration:** Bundles of fine microwires (gold/tungsten) bonded to a CMOS sensor.
*   **Density:** **100 $\mu$m pitch** (or greater).
*   **Strategy:** Paradromics utilizes **electro-sharpened tips** to mitigate the bed-of-nails effect, allowing for successful insertion at 100 $\mu$m pitch with reduced acute damage compared to blunt arrays [cite: 1, 6, 7].
*   **Outcome:** This approach achieves a higher sampling density, reducing blind spots while attempting to manage insertion trauma through tip geometry [cite: 7].

### 4.3 Flexible Threads (High Density - Neuralink)
*   **Configuration:** Polyimide thin-film threads inserted individually by a robot.
*   **Density:** High channel count (1024+), but density is defined by insertion sites.
*   **Strategy:** By inserting threads individually (or in small groups), the "bed-of-nails" effect is avoided. The flexibility of the threads reduces chronic micromotion damage, theoretically allowing for higher density without the chronic "kill zone" penalty of rigid shanks [cite: 23, 24].
*   **Risk:** Thread retraction and migration remain challenges [cite: 23, 25].

### 4.4 Mesh Electronics (Ultra-High Density / Bio-integrated)
*   **Configuration:** Macroporous mesh with subcellular feature sizes.
*   **Density:** High local density, but highly porous.
*   **Strategy:** The open structure allows neurons and glia to grow *through* the array, eliminating the continuous scar boundary. This architecture supports stable long-term recordings at single-neuron resolution, effectively bypassing the traditional density limits imposed by solid shanks [cite: 8, 9].

---

## 5. Optimization: Defining the "Optimal" Density

Based on the synthesized research, the "optimal" density is not a static number but a function of the probe's material properties and insertion mechanics.

### 5.1 For Rigid Probes (Silicon/Microwire)
*   **Optimal Pitch:** **100–150 $\mu$m**.
    *   *Reasoning:* A pitch of 100 $\mu$m is the lower limit for avoiding severe bed-of-nails compression during insertion (unless tips are ultra-sharp) [cite: 1]. It also approaches the limit where glial scars might begin to merge if the FBR is not mitigated [cite: 5].
    *   *Signal Benefit:* This spacing aligns well with the 50–100 $\mu$m recording radius, minimizing blind spots [cite: 2].

### 5.2 For Flexible/Laminar Probes
*   **Optimal Pitch:** **<50 $\mu$m (Vertical) / Variable (Horizontal)**.
    *   *Reasoning:* On a single shank (e.g., Neuropixels or Michigan probes), vertical sites can be packed extremely densely (20–40 $\mu$m) because they do not increase the shank's cross-section [cite: 14, 15].
    *   *Horizontal Spacing:* Inter-shank spacing for flexible probes can likely be tighter than rigid probes due to reduced chronic irritation, but insertion mechanics (buckling) become the limiting factor [cite: 10, 26].

### 5.3 Theoretical Optima
*   **Spike Sorting Efficiency:** Theoretical models and downsampling experiments suggest that an inter-electrode distance of **~37 $\mu$m** maximizes the efficiency of spike sorting (units per electrode) [cite: 3].
*   **Volumetric Efficiency:** To maximize the information extracted per unit of displaced tissue, the array should minimize the "dead space" of the shank. Technologies like the BISC (Bi-directional Interface via Stacked CMOS) aim for maximal volumetric efficiency by integrating processing, reducing the cabling bulk that often dictates density limits [cite: 11].

---

## 6. Conclusion

The optimal electrode array density for neural prostheses is a dynamic parameter that has shifted from the conservative **400 $\mu$m pitch** of the Utah array toward the **100 $\mu$m pitch** of modern high-density microwire arrays, and potentially down to **<40 $\mu$m** site spacing for next-generation flexible devices.

To balance high-resolution acquisition with minimal tissue damage:
1.  **Geometric Optimization:** For penetrating arrays, a pitch of **100 $\mu$m** appears to be the current "sweet spot" for maximizing yield without catastrophic tissue compression, *provided* that **electro-sharpened tips** and **high-speed insertion** are used [cite: 1, 6].
2.  **Material Optimization:** To sustain this density chronically, the mechanical mismatch must be minimized. Transitioning from rigid silicon to **flexible polymers** or **mesh architectures** allows for higher densities by reducing the chronic "kill zone" that necessitates wide spacing in rigid arrays [cite: 8, 9].
3.  **Sorting Optimization:** For the specific purpose of spike sorting, electrode sites should be spaced **~37 $\mu$m** apart to enable effective oversampling of single units [cite: 3].

**Final Recommendation:** Future neural prostheses should aim for an architecture that supports **<50 $\mu$m site spacing** (for sorting) distributed across shanks or threads spaced **100–200 $\mu$m** apart (to preserve tissue bridges), utilizing **flexible materials** and **sharpened geometries** to minimize the biological footprint of this high-density interface.

---

## 7. Detailed Analysis of Research Findings

### 7.1 Signal Acquisition Physics and Electrode Spacing
The fundamental goal of high-density arrays is to capture the activity of the maximum number of distinct neurons. The physics of extracellular recording dictates that the voltage signal $V$ decays with distance $r$ from the source.
*   **Decay Function:** The potential typically decays as $1/r$, but filtering and local tissue properties can steepen this to $1/r^2$.
*   **Detection Threshold:** A neuron is typically detectable only if it lies within a "listening sphere" of the electrode.
    *   *Source 28* estimates this radius at **~140 $\mu$m** under ideal conditions but notes that practical detection is often limited to **<100 $\mu$m**.
    *   *Source 29* is more conservative, estimating a radius of **50–100 $\mu$m** for reliable isolation.
    *   *Source 74* confirms that in Utah arrays (400 $\mu$m spacing), the 200 $\mu$m radius of "silence" between electrodes results in a massive loss of potential data.

**Table 1: Recording Radius vs. Array Pitch**

| Array Type | Pitch (Spacing) | Recording Radius | Coverage Status | Source |
| :--- | :--- | :--- | :--- | :--- |
| Utah Array | 400 $\mu$m | ~50–100 $\mu$m | Significant Blind Spots | [cite: 5] |
| Paradromics F$\mu$A | 100 $\mu$m | ~50–100 $\mu$m | Near-Continuous Coverage | [cite: 1, 7] |
| Neuropixels | ~20 $\mu$m (vertical) | ~50–100 $\mu$m | High Oversampling (Vertical) | [cite: 14, 15] |

### 7.2 The "Bed-of-Nails" Effect and Insertion Mechanics
A major finding in recent literature is the quantification of the "bed-of-nails" effect for high-density arrays.
*   **Mechanism:** When the spacing between shanks is reduced, the brain tissue acts as a continuous elastic surface rather than discrete entry points. The force required to penetrate increases, causing the brain to depress (dimple) significantly before puncture occurs.
*   **Consequences:** Deep dimpling stretches the tissue, rupturing capillaries and neurons far from the insertion site.
*   **Solution:** *Source 2* and *Source 13* demonstrate that **electro-sharpening** microwires (creating a pencil-like tip <8 degrees) allows arrays with **100 $\mu$m pitch** to penetrate with minimal dimpling, whereas blunt or angled tips at the same density cause severe damage. This suggests that **100 $\mu$m** is a viable density *only if* tip geometry is optimized.

### 7.3 Chronic Stability and the Glial Scar
The long-term stability of the interface depends on the chronic FBR.
*   **Neuronal Die-off:** *Source 71* (a rare primate study) found a **63% reduction** in neuron density within the immediate vicinity of Utah array shanks after >500 days.
*   **Scar Merging:** *Source 1* and *Source 71* discuss the risk of scar merging. If the "kill zone" is ~100 $\mu$m, then electrodes spaced 200 $\mu$m apart might have their scar tissues touch, effectively walling off the entire array. This supports the historical use of 400 $\mu$m spacing for rigid arrays but highlights the need for smaller, less traumatic shanks (like threads or mesh) to enable higher densities safely.

### 7.4 Emerging High-Density Architectures
*   **Paradromics:** Uses a **100 $\mu$m pitch** with electro-sharpened tips. Their data [cite: 1] claims this density is achievable with reduced acute damage compared to standard blunt arrays.
*   **Neuralink:** Uses flexible threads. While the exact pitch can vary, the flexibility allows the threads to move with the brain, reducing the chronic strain that drives the "kill zone," theoretically permitting higher densities [cite: 24].
*   **Mesh Electronics:** *Source 7* describes mesh probes that have **macroporous** structures. The "density" here is high in terms of channel count, but the *material* density is low. This allows cells to integrate *through* the device, preventing the formation of a continuous scar and allowing stable recording for months.

### 7.5 Optimal Spacing for Spike Sorting
*   *Source 98* explicitly investigates the relationship between spacing and sorting efficiency. It concludes that **37 $\mu$m** is an optimal inter-electrode distance.
    *   **Why?** At this distance, a single spike is visible on multiple channels with sufficient amplitude variation to allow precise triangulation.
    *   **Trade-off:** Spacing closer than 37 $\mu$m yields redundant data (diminishing returns), while spacing much larger (e.g., >100 $\mu$m) prevents the oversampling necessary for resolving overlapping spikes.

---

## 8. Synthesis and Recommendations

The "optimal" density is a function of the specific BCI application:

1.  **For Maximum Unit Yield (Research/High-Bandwidth BCI):**
    *   **Density:** High (Pitch ~100 $\mu$m; Site Spacing ~30–40 $\mu$m).
    *   **Requirement:** Must use **flexible** or **electro-sharpened** probes to avoid the bed-of-nails effect and chronic scarring.
    *   **Technology:** Neuropixels (acute/short-term), Paradromics (high-density rigid), Neuralink (flexible).

2.  **For Long-Term Stability (Clinical Implants):**
    *   **Density:** Moderate (Pitch ~200–400 $\mu$m) *OR* Ultra-High (Mesh/Flexible).
    *   **Requirement:** Must avoid scar merging. Rigid arrays should stick to 400 $\mu$m. Flexible arrays can push to higher densities.
    *   **Technology:** Utah Array (current standard), Mesh Electronics (future standard).

**Final Conclusion:** The field is moving away from the 400 $\mu$m limit of the Utah array. Evidence supports **100 $\mu$m** as a viable high-density standard for penetrating arrays, provided that insertion trauma is managed via sharp tip geometry and high-speed insertion. For surface-level (LFP) decoding, sub-millimeter spacing (**0.6–1.2 mm**) is sufficient. The ultimate convergence of high resolution and stability lies in **flexible, cellular-scale** architectures that can support high-density sites without triggering the mechanical FBR.

**Sources:**
1. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc4RGD7BJQR1nBgDRnQZL1O_WCLzQUXzIhuq_eOI2n4OR5cOIvznf_QaQfgXFeXt5uZmW7ZnRNDfiYc2IWS_OZMMqKqFtu1_pxsjL4Aeev3H3PQ_TPhdr_C_9CJGe4CBRcJpVpfT9rWrqbBJYu45FhlAFTLgM7xWSJWg==)
2. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGf5UyMl4dqi9_kKKX9ftwMYQvJqnuouAqAbCfLwXBfCaCnAP7R3iScNUyJbYLj6m-PYC_CwlEZ4X9sftvJN8Wa-8RDCQaMvr0kSRFIJpIRrA1jtyrbCTdBRn70w5ttGEwZU_G1qxRu)
3. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHRWAxuYZoL0iIcDb_EQOaZTpv3xDmzlIgng24bDZ_bu1RvupH27O3Y2EFwdQ1k_iUE7eCdNsb0FEQt96PVxFKlI3OAXrZoApb-Obh2xXdjBh4gpjLw1temoNRe8zih3FToA2xvktytLF9EqYZ1f2GhA==)
4. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGgWnzLpcmXVzl483V1fIrYhABQ_EDEO7R1B8Zlc5agts-iKPzvKsgZJDNUppqb_3-O-q_UvBwNb5iJpRy3Z5_aIPO-FaOKZyzZQSTT9q7ZPM4uQ50PJj7zwjgb3azAdYhSf8XJk8tMrt829rADrfHfBMDInJCVGUWZD8Fwn4XnhX3b19bwrSFGZaOnGXQPFO_SOrPRI6F21VZb_jWHXm5A23paY05u96AIonVkF-l2R538WKByqi6LqhXuzsYe1c=)
5. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrfZCuqbPOD-H7TQVsCf8eVqpl9ToGxsaACTcjDus_SDAQ2Xm5yhNm4vCJSWczrat0iyrkTamoAWSwK4LWA1ioTV4I4vrerbw95o1S_gw2GM0eOhHy4DE2xf2aGzPuOLYJlrPmNyWx)
6. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvJSHSnC5Dbogd0LQ1uToIEdYlGf6rcRXq0jsJzFFe28Nl3DM37JWCjHn633sZRKx1aQ_sArepeooUM8YWk3vQFQILdYk-9FvSYVWhjypeL1XgvxVVaBoSBF2c-DSbOT2GevgUlZCuW7g0wga0_qM55BnQ37BPtk12NTI=)
7. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7AojUMR5NUHAK-5s536DCP3YTHV5TitEQEvaRE3rnGhiykdCm7V_fTxNkCx8xzUgI1G_0tO-l72_IihRCE2YYweD5WlJoQ667jdyPaw6xDZsLecjqIxaocfpsr7kNP15seiZlI8eXQk7VL16WVkpG9ZHQ5elDSa4mcg==)
8. [pnas.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfd5H68VYwd5i39Yh3rbICbIqJElTOoDnz9Ct-P0XeoeI1Blx1h3MAHb--4HXGByOy0oZtfp-z5a_SluuwkCCXYaqcWEBpaSOdPS5ntJ3h3CNJee1IxyJs3aBslTyYrnKtMwTnR4U=)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFn6GtztfaWC3o5Gs-qDFRrjkbRJyaSE-qkmRQS1GWeQQ-Z50HVfFH6Cn9sAulm2yW1oK3ht68_C0UfHHSeY6INVa9SQoKlHmscZb5SEqfVFjX9NG0lVokXQEK1dZ02Y5Q5cIUKfVaG)
10. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_iWfa_wSwNsrDTf1S6yMA-jL4TacukMl50XazyhNfsxvXM-VVgEoLRscxftMFkQiQx-L1cMle5PH58e1ehSXndYyHGI-dmyTcZdjmvQ6Cm7cwsCFjoo33ZLSwwYOUs7GhXaSgOB7mSg==)
11. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbsLhCnd1XGD-sAz2bmJGHDSDH0VbmKjHJaV3xWOafTgobAxnMl-auE0SfB53Na8VqRGcVtYqIY2K2AaCpZwKsrD-RP2AoNXiWS9WYifc_McSzcFuNGh-OjkF2tyrBBIf0eRDocgapCg==)
12. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGY9XG4lmDiEerCNWAJaFo4xE6vmtxFLLW27pYikWyCWbYa7JLrbyeLJrOHGVmdjyr2tqh1geoOiTjWexzPDLe4pONXxmhCqkVk-RIEWejv6b9rnJurg9NngYWJoQou9qnNuvhb3zGEvwUIxA==)
13. [physiology.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIS8iXxgWjSpdDcKTeyS2ueux95TAC_iZ97oMsdACwJc7l3Et505QK8rLJxq7o3NwNU90dhtnAI4pFgCsLzbnFzJ73Ig5LCO3WVWrEysSgm28V3RQRwoxz-NxdZ193G48Q89zRJSUEzvbfG4J9tD--zFGhVg==)
14. [ucl.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfht8M8unG_msD4uo59jq4PbPqWZTm0dru4Ensvc9cXOwN1IIYOKoebWKb6cXikBRlN_57hrkqeGjtLmndQe099ycR5X_Aj65rQD9fDAmTs-80ElOG-R9P7_xEpbU-QDWRmp8f9heNZMdLD3QLyJqMR9dpTYVk5OSajxWt6MowwJI4lVw6FJen-iT-7JdBGxgWuejWkAg=)
15. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7kEFcLGt37trOZfTOytbOqzSB9QFBpA8GL3jJzWtTDa93Ec6RKB2ZQuev8Xm1H8TbOwUs3Agrloh-BnG89nuNLpm7jF3FdOU0PZ9VOyy5rA7m7R7Ax20HcRYdJo2T0gNP82J-o5CUyQPYANoAF07je5Y3efZW58MwAQ==)
16. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJifKvBYBC2eP6q6M_00UBsq5h8g3f96trjuknsoXzxLe3LM40V6bi1tAgsXzXNfHh1y18K2aZnsuf_AS69vspdCYs-cfziVoVlNw616DWdR3Lu8d7zj0Ug1t-PzsvUJTzNuKd2kRF)
17. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEWoPe8kB-DRrVi-1J3XM_5C_1_2sYCuaIoLuihdwflcAYmGlKcFNOxA6sVez-JXgEaJGAyqVus7notWyPhXxPx_mNQjd8T8Zz6dxWZHZhn4gKuHMmVO3H94myng-5lDv-TDbYxathaA==)
18. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFz55Cfrp37dWqMCPQEDrKYiabH31n7mJXlqznoba5aNXp9jgn6OJjDQGeCurhByQDajiAcdr7ACYHOKvbdCy1a1TIBrxFtHN3FwA8KSJqYHKZr4n9ksuRudelkJ_po3SzaBQ9SS7tv9WQSLP3ptenJVXk-ToMbpcP9RiXtOCgNQrfxH2vxUB6dB-ZTDJuMIxtmqreb7Ogv8HbJ7r-ZSrj71VpchxK6rGY63Bu1z4449vmgLzGhI3p0n6JT2lBJUFflTebwFmQ09G90I3Z2SnCw-1SsRCEkeO5uBA==)
19. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHop0L9AByU_w1dBYlUTdwG9R_dYcIdibH9nR7xIo2oYe1i0wDAB_HFiV7GAyYFcuFAC1mUg7UNum0qRtUrpK3gPlXWnxa1iJmNqrOzXC-Lp4T3w4QqNQXPKWkoIuL1Pmwg-xOsmT4)
20. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTpHCHoR_lRM674SEHcP2F21N2ucpQsWNE3NgxTiJ5OLMYEqEXm_6x10ci4NgXrAZIstFMl_Hb75xxH_9yWGDmVeSaL7Jyx26hKDrerz5N8ZuFq409eMk33q1KYc2x111iTVZ3cHaA)
21. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0X2ckIXvsK7MrSyo_u4wdsGSmVoSA41P5Rn2D1MQwlN-6hU98QVT27nyFZO9lX4WECCVOopLrKKRlOX-aRcRq76qzcJD6h8xtgInJcjizzbLyx57J3pgzeHjRyis6H_flE9zWE0CGcM9y8kvBD3r5YyHmf8n_YF5czCVS13uDe-XvdIAJyggc_n34oBfo17Ve)
22. [blackrockneurotech.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFGDYWinMc2AOp1mdRHuckjd97fuoOjXUw9Wj8nbith1qfnyVA0Zqzx_gR7x5_W6IP5Ny8jMWKcUp4zk8-hk5NS7mL2-Z2RAbHNDQY2zZeuVsVqgX4uqpkdgUZCv9AhcIx_aBNIKR_pbQ=)
23. [republicworld.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBgQYSV-TkjAF3swpPMhgqYaz5OIHuHSa3rIavgJ3zpy4Ake6cLeQenxcabgD8PCf_h4ECdjod8iKctOJInMMQG7mCSgjxLIIdNj_JIBChJbS3eTRU1JfSFJrV6pU5E6R64oglYLRxPlfNE2gihwSrvRIgXnUGBdaY8L_kPeGTul0XqCSfVP9XMn95015WkFZku5mzrAk1KeTdevOlFXTO)
24. [neuralink.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsO44ZulwqQOVj9r3Nj2IKj7mdqv7DikB7CM8r90L_s3e-SVLuKc-Vc3JalRJphf_fAMprMv_WicrxA39zrK_87U9kCnNcdFD8mMPnVHm8NgDy3POHe3-Kzg1KFUjQDeWSGz_YOt2QVqWHm9wsaWuHygwsVZcN)
25. [forbes.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfBbfhx9H5oXHj5sD6ZmMbJ8T_By52PUXmJYfVRxlXbW3hD6JNDbKhs-Gi_KPeIzNDKDcpGp_5P4AZmS7xm1d0hjmznaFqfajS5tGnqK75eV9moNW5lN4dpkYD3_a331QfuKt1FU0rX64FNU5QiYXfqysp4ZdW1KcDc0OZCQkaacZNJfMfP2nkh8uCYjqdPYxAO8soLlYDQ6S82XuMkdfI2TS8glne2Po=)
26. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjRi5WNtQfJsS2sYL_1_fztEJNcUmqtQ4w2ZiNDAYPUwNUOdI5SJUDKHDYDeof9yzRfuiNwEuz6usUJrqTMudHacWaWwMiSowUURQ4DBX5aLLdqIeWO5cS1tcDaFjMyi7bbJj88jyB)


## Annotations
Annotation(end_index=713, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGf5UyMl4dqi9_kKKX9ftwMYQvJqnuouAqAbCfLwXBfCaCnAP7R3iScNUyJbYLj6m-PYC_CwlEZ4X9sftvJN8Wa-8RDCQaMvr0kSRFIJpIRrA1jtyrbCTdBRn70w5ttGEwZU_G1qxRu', start_index=701)
Annotation(end_index=713, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc4RGD7BJQR1nBgDRnQZL1O_WCLzQUXzIhuq_eOI2n4OR5cOIvznf_QaQfgXFeXt5uZmW7ZnRNDfiYc2IWS_OZMMqKqFtu1_pxsjL4Aeev3H3PQ_TPhdr_C_9CJGe4CBRcJpVpfT9rWrqbBJYu45FhlAFTLgM7xWSJWg==', start_index=701)
Annotation(end_index=897, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHRWAxuYZoL0iIcDb_EQOaZTpv3xDmzlIgng24bDZ_bu1RvupH27O3Y2EFwdQ1k_iUE7eCdNsb0FEQt96PVxFKlI3OAXrZoApb-Obh2xXdjBh4gpjLw1temoNRe8zih3FToA2xvktytLF9EqYZ1f2GhA==', start_index=885)
Annotation(end_index=897, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGgWnzLpcmXVzl483V1fIrYhABQ_EDEO7R1B8Zlc5agts-iKPzvKsgZJDNUppqb_3-O-q_UvBwNb5iJpRy3Z5_aIPO-FaOKZyzZQSTT9q7ZPM4uQ50PJj7zwjgb3azAdYhSf8XJk8tMrt829rADrfHfBMDInJCVGUWZD8Fwn4XnhX3b19bwrSFGZaOnGXQPFO_SOrPRI6F21VZb_jWHXm5A23paY05u96AIonVkF-l2R538WKByqi6LqhXuzsYe1c=', start_index=885)
Annotation(end_index=1103, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrfZCuqbPOD-H7TQVsCf8eVqpl9ToGxsaACTcjDus_SDAQ2Xm5yhNm4vCJSWczrat0iyrkTamoAWSwK4LWA1ioTV4I4vrerbw95o1S_gw2GM0eOhHy4DE2xf2aGzPuOLYJlrPmNyWx', start_index=1094)
Annotation(end_index=1354, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc4RGD7BJQR1nBgDRnQZL1O_WCLzQUXzIhuq_eOI2n4OR5cOIvznf_QaQfgXFeXt5uZmW7ZnRNDfiYc2IWS_OZMMqKqFtu1_pxsjL4Aeev3H3PQ_TPhdr_C_9CJGe4CBRcJpVpfT9rWrqbBJYu45FhlAFTLgM7xWSJWg==', start_index=1345)
Annotation(end_index=1600, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7AojUMR5NUHAK-5s536DCP3YTHV5TitEQEvaRE3rnGhiykdCm7V_fTxNkCx8xzUgI1G_0tO-l72_IihRCE2YYweD5WlJoQ667jdyPaw6xDZsLecjqIxaocfpsr7kNP15seiZlI8eXQk7VL16WVkpG9ZHQ5elDSa4mcg==', start_index=1588)
Annotation(end_index=1600, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvJSHSnC5Dbogd0LQ1uToIEdYlGf6rcRXq0jsJzFFe28Nl3DM37JWCjHn633sZRKx1aQ_sArepeooUM8YWk3vQFQILdYk-9FvSYVWhjypeL1XgvxVVaBoSBF2c-DSbOT2GevgUlZCuW7g0wga0_qM55BnQ37BPtk12NTI=', start_index=1588)
Annotation(end_index=1891, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfd5H68VYwd5i39Yh3rbICbIqJElTOoDnz9Ct-P0XeoeI1Blx1h3MAHb--4HXGByOy0oZtfp-z5a_SluuwkCCXYaqcWEBpaSOdPS5ntJ3h3CNJee1IxyJs3aBslTyYrnKtMwTnR4U=', start_index=1879)
Annotation(end_index=1891, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFn6GtztfaWC3o5Gs-qDFRrjkbRJyaSE-qkmRQS1GWeQQ-Z50HVfFH6Cn9sAulm2yW1oK3ht68_C0UfHHSeY6INVa9SQoKlHmscZb5SEqfVFjX9NG0lVokXQEK1dZ02Y5Q5cIUKfVaG', start_index=1879)
Annotation(end_index=2414, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_iWfa_wSwNsrDTf1S6yMA-jL4TacukMl50XazyhNfsxvXM-VVgEoLRscxftMFkQiQx-L1cMle5PH58e1ehSXndYyHGI-dmyTcZdjmvQ6Cm7cwsCFjoo33ZLSwwYOUs7GhXaSgOB7mSg==', start_index=2404)
Annotation(end_index=2845, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbsLhCnd1XGD-sAz2bmJGHDSDH0VbmKjHJaV3xWOafTgobAxnMl-auE0SfB53Na8VqRGcVtYqIY2K2AaCpZwKsrD-RP2AoNXiWS9WYifc_McSzcFuNGh-OjkF2tyrBBIf0eRDocgapCg==', start_index=2835)
Annotation(end_index=3949, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGY9XG4lmDiEerCNWAJaFo4xE6vmtxFLLW27pYikWyCWbYa7JLrbyeLJrOHGVmdjyr2tqh1geoOiTjWexzPDLe4pONXxmhCqkVk-RIEWejv6b9rnJurg9NngYWJoQou9qnNuvhb3zGEvwUIxA==', start_index=3933)
Annotation(end_index=3949, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGf5UyMl4dqi9_kKKX9ftwMYQvJqnuouAqAbCfLwXBfCaCnAP7R3iScNUyJbYLj6m-PYC_CwlEZ4X9sftvJN8Wa-8RDCQaMvr0kSRFIJpIRrA1jtyrbCTdBRn70w5ttGEwZU_G1qxRu', start_index=3933)
Annotation(end_index=3949, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc4RGD7BJQR1nBgDRnQZL1O_WCLzQUXzIhuq_eOI2n4OR5cOIvznf_QaQfgXFeXt5uZmW7ZnRNDfiYc2IWS_OZMMqKqFtu1_pxsjL4Aeev3H3PQ_TPhdr_C_9CJGe4CBRcJpVpfT9rWrqbBJYu45FhlAFTLgM7xWSJWg==', start_index=3933)
Annotation(end_index=4088, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrfZCuqbPOD-H7TQVsCf8eVqpl9ToGxsaACTcjDus_SDAQ2Xm5yhNm4vCJSWczrat0iyrkTamoAWSwK4LWA1ioTV4I4vrerbw95o1S_gw2GM0eOhHy4DE2xf2aGzPuOLYJlrPmNyWx', start_index=4076)
Annotation(end_index=4088, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGf5UyMl4dqi9_kKKX9ftwMYQvJqnuouAqAbCfLwXBfCaCnAP7R3iScNUyJbYLj6m-PYC_CwlEZ4X9sftvJN8Wa-8RDCQaMvr0kSRFIJpIRrA1jtyrbCTdBRn70w5ttGEwZU_G1qxRu', start_index=4076)
Annotation(end_index=4385, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrfZCuqbPOD-H7TQVsCf8eVqpl9ToGxsaACTcjDus_SDAQ2Xm5yhNm4vCJSWczrat0iyrkTamoAWSwK4LWA1ioTV4I4vrerbw95o1S_gw2GM0eOhHy4DE2xf2aGzPuOLYJlrPmNyWx', start_index=4376)
Annotation(end_index=4511, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIS8iXxgWjSpdDcKTeyS2ueux95TAC_iZ97oMsdACwJc7l3Et505QK8rLJxq7o3NwNU90dhtnAI4pFgCsLzbnFzJ73Ig5LCO3WVWrEysSgm28V3RQRwoxz-NxdZ193G48Q89zRJSUEzvbfG4J9tD--zFGhVg==', start_index=4498)
Annotation(end_index=4511, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGf5UyMl4dqi9_kKKX9ftwMYQvJqnuouAqAbCfLwXBfCaCnAP7R3iScNUyJbYLj6m-PYC_CwlEZ4X9sftvJN8Wa-8RDCQaMvr0kSRFIJpIRrA1jtyrbCTdBRn70w5ttGEwZU_G1qxRu', start_index=4498)
Annotation(end_index=5284, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHRWAxuYZoL0iIcDb_EQOaZTpv3xDmzlIgng24bDZ_bu1RvupH27O3Y2EFwdQ1k_iUE7eCdNsb0FEQt96PVxFKlI3OAXrZoApb-Obh2xXdjBh4gpjLw1temoNRe8zih3FToA2xvktytLF9EqYZ1f2GhA==', start_index=5275)
Annotation(end_index=5472, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7kEFcLGt37trOZfTOytbOqzSB9QFBpA8GL3jJzWtTDa93Ec6RKB2ZQuev8Xm1H8TbOwUs3Agrloh-BnG89nuNLpm7jF3FdOU0PZ9VOyy5rA7m7R7Ax20HcRYdJo2T0gNP82J-o5CUyQPYANoAF07je5Y3efZW58MwAQ==', start_index=5458)
Annotation(end_index=5472, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfht8M8unG_msD4uo59jq4PbPqWZTm0dru4Ensvc9cXOwN1IIYOKoebWKb6cXikBRlN_57hrkqeGjtLmndQe099ycR5X_Aj65rQD9fDAmTs-80ElOG-R9P7_xEpbU-QDWRmp8f9heNZMdLD3QLyJqMR9dpTYVk5OSajxWt6MowwJI4lVw6FJen-iT-7JdBGxgWuejWkAg=', start_index=5458)
Annotation(end_index=6291, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEWoPe8kB-DRrVi-1J3XM_5C_1_2sYCuaIoLuihdwflcAYmGlKcFNOxA6sVez-JXgEaJGAyqVus7notWyPhXxPx_mNQjd8T8Zz6dxWZHZhn4gKuHMmVO3H94myng-5lDv-TDbYxathaA==', start_index=6277)
Annotation(end_index=6291, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJifKvBYBC2eP6q6M_00UBsq5h8g3f96trjuknsoXzxLe3LM40V6bi1tAgsXzXNfHh1y18K2aZnsuf_AS69vspdCYs-cfziVoVlNw616DWdR3Lu8d7zj0Ug1t-PzsvUJTzNuKd2kRF', start_index=6277)
Annotation(end_index=7042, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc4RGD7BJQR1nBgDRnQZL1O_WCLzQUXzIhuq_eOI2n4OR5cOIvznf_QaQfgXFeXt5uZmW7ZnRNDfiYc2IWS_OZMMqKqFtu1_pxsjL4Aeev3H3PQ_TPhdr_C_9CJGe4CBRcJpVpfT9rWrqbBJYu45FhlAFTLgM7xWSJWg==', start_index=7033)
Annotation(end_index=7275, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFz55Cfrp37dWqMCPQEDrKYiabH31n7mJXlqznoba5aNXp9jgn6OJjDQGeCurhByQDajiAcdr7ACYHOKvbdCy1a1TIBrxFtHN3FwA8KSJqYHKZr4n9ksuRudelkJ_po3SzaBQ9SS7tv9WQSLP3ptenJVXk-ToMbpcP9RiXtOCgNQrfxH2vxUB6dB-ZTDJuMIxtmqreb7Ogv8HbJ7r-ZSrj71VpchxK6rGY63Bu1z4449vmgLzGhI3p0n6JT2lBJUFflTebwFmQ09G90I3Z2SnCw-1SsRCEkeO5uBA==', start_index=7262)
Annotation(end_index=7275, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc4RGD7BJQR1nBgDRnQZL1O_WCLzQUXzIhuq_eOI2n4OR5cOIvznf_QaQfgXFeXt5uZmW7ZnRNDfiYc2IWS_OZMMqKqFtu1_pxsjL4Aeev3H3PQ_TPhdr_C_9CJGe4CBRcJpVpfT9rWrqbBJYu45FhlAFTLgM7xWSJWg==', start_index=7262)
Annotation(end_index=7756, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7AojUMR5NUHAK-5s536DCP3YTHV5TitEQEvaRE3rnGhiykdCm7V_fTxNkCx8xzUgI1G_0tO-l72_IihRCE2YYweD5WlJoQ667jdyPaw6xDZsLecjqIxaocfpsr7kNP15seiZlI8eXQk7VL16WVkpG9ZHQ5elDSa4mcg==', start_index=7741)
Annotation(end_index=7756, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvJSHSnC5Dbogd0LQ1uToIEdYlGf6rcRXq0jsJzFFe28Nl3DM37JWCjHn633sZRKx1aQ_sArepeooUM8YWk3vQFQILdYk-9FvSYVWhjypeL1XgvxVVaBoSBF2c-DSbOT2GevgUlZCuW7g0wga0_qM55BnQ37BPtk12NTI=', start_index=7741)
Annotation(end_index=7756, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc4RGD7BJQR1nBgDRnQZL1O_WCLzQUXzIhuq_eOI2n4OR5cOIvznf_QaQfgXFeXt5uZmW7ZnRNDfiYc2IWS_OZMMqKqFtu1_pxsjL4Aeev3H3PQ_TPhdr_C_9CJGe4CBRcJpVpfT9rWrqbBJYu45FhlAFTLgM7xWSJWg==', start_index=7741)
Annotation(end_index=7935, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc4RGD7BJQR1nBgDRnQZL1O_WCLzQUXzIhuq_eOI2n4OR5cOIvznf_QaQfgXFeXt5uZmW7ZnRNDfiYc2IWS_OZMMqKqFtu1_pxsjL4Aeev3H3PQ_TPhdr_C_9CJGe4CBRcJpVpfT9rWrqbBJYu45FhlAFTLgM7xWSJWg==', start_index=7926)
Annotation(end_index=8323, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrfZCuqbPOD-H7TQVsCf8eVqpl9ToGxsaACTcjDus_SDAQ2Xm5yhNm4vCJSWczrat0iyrkTamoAWSwK4LWA1ioTV4I4vrerbw95o1S_gw2GM0eOhHy4DE2xf2aGzPuOLYJlrPmNyWx', start_index=8307)
Annotation(end_index=8323, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHop0L9AByU_w1dBYlUTdwG9R_dYcIdibH9nR7xIo2oYe1i0wDAB_HFiV7GAyYFcuFAC1mUg7UNum0qRtUrpK3gPlXWnxa1iJmNqrOzXC-Lp4T3w4QqNQXPKWkoIuL1Pmwg-xOsmT4', start_index=8307)
Annotation(end_index=8323, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc4RGD7BJQR1nBgDRnQZL1O_WCLzQUXzIhuq_eOI2n4OR5cOIvznf_QaQfgXFeXt5uZmW7ZnRNDfiYc2IWS_OZMMqKqFtu1_pxsjL4Aeev3H3PQ_TPhdr_C_9CJGe4CBRcJpVpfT9rWrqbBJYu45FhlAFTLgM7xWSJWg==', start_index=8307)
Annotation(end_index=8899, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrfZCuqbPOD-H7TQVsCf8eVqpl9ToGxsaACTcjDus_SDAQ2Xm5yhNm4vCJSWczrat0iyrkTamoAWSwK4LWA1ioTV4I4vrerbw95o1S_gw2GM0eOhHy4DE2xf2aGzPuOLYJlrPmNyWx', start_index=8886)
Annotation(end_index=8899, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_iWfa_wSwNsrDTf1S6yMA-jL4TacukMl50XazyhNfsxvXM-VVgEoLRscxftMFkQiQx-L1cMle5PH58e1ehSXndYyHGI-dmyTcZdjmvQ6Cm7cwsCFjoo33ZLSwwYOUs7GhXaSgOB7mSg==', start_index=8886)
Annotation(end_index=9400, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFn6GtztfaWC3o5Gs-qDFRrjkbRJyaSE-qkmRQS1GWeQQ-Z50HVfFH6Cn9sAulm2yW1oK3ht68_C0UfHHSeY6INVa9SQoKlHmscZb5SEqfVFjX9NG0lVokXQEK1dZ02Y5Q5cIUKfVaG', start_index=9383)
Annotation(end_index=9400, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_iWfa_wSwNsrDTf1S6yMA-jL4TacukMl50XazyhNfsxvXM-VVgEoLRscxftMFkQiQx-L1cMle5PH58e1ehSXndYyHGI-dmyTcZdjmvQ6Cm7cwsCFjoo33ZLSwwYOUs7GhXaSgOB7mSg==', start_index=9383)
Annotation(end_index=9400, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTpHCHoR_lRM674SEHcP2F21N2ucpQsWNE3NgxTiJ5OLMYEqEXm_6x10ci4NgXrAZIstFMl_Hb75xxH_9yWGDmVeSaL7Jyx26hKDrerz5N8ZuFq409eMk33q1KYc2x111iTVZ3cHaA', start_index=9383)
Annotation(end_index=9895, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrfZCuqbPOD-H7TQVsCf8eVqpl9ToGxsaACTcjDus_SDAQ2Xm5yhNm4vCJSWczrat0iyrkTamoAWSwK4LWA1ioTV4I4vrerbw95o1S_gw2GM0eOhHy4DE2xf2aGzPuOLYJlrPmNyWx', start_index=9882)
Annotation(end_index=9895, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0X2ckIXvsK7MrSyo_u4wdsGSmVoSA41P5Rn2D1MQwlN-6hU98QVT27nyFZO9lX4WECCVOopLrKKRlOX-aRcRq76qzcJD6h8xtgInJcjizzbLyx57J3pgzeHjRyis6H_flE9zWE0CGcM9y8kvBD3r5YyHmf8n_YF5czCVS13uDe-XvdIAJyggc_n34oBfo17Ve', start_index=9882)
Annotation(end_index=10027, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFGDYWinMc2AOp1mdRHuckjd97fuoOjXUw9Wj8nbith1qfnyVA0Zqzx_gR7x5_W6IP5Ny8jMWKcUp4zk8-hk5NS7mL2-Z2RAbHNDQY2zZeuVsVqgX4uqpkdgUZCv9AhcIx_aBNIKR_pbQ=', start_index=10014)
Annotation(end_index=10027, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrfZCuqbPOD-H7TQVsCf8eVqpl9ToGxsaACTcjDus_SDAQ2Xm5yhNm4vCJSWczrat0iyrkTamoAWSwK4LWA1ioTV4I4vrerbw95o1S_gw2GM0eOhHy4DE2xf2aGzPuOLYJlrPmNyWx', start_index=10014)
Annotation(end_index=10451, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7AojUMR5NUHAK-5s536DCP3YTHV5TitEQEvaRE3rnGhiykdCm7V_fTxNkCx8xzUgI1G_0tO-l72_IihRCE2YYweD5WlJoQ667jdyPaw6xDZsLecjqIxaocfpsr7kNP15seiZlI8eXQk7VL16WVkpG9ZHQ5elDSa4mcg==', start_index=10436)
Annotation(end_index=10451, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvJSHSnC5Dbogd0LQ1uToIEdYlGf6rcRXq0jsJzFFe28Nl3DM37JWCjHn633sZRKx1aQ_sArepeooUM8YWk3vQFQILdYk-9FvSYVWhjypeL1XgvxVVaBoSBF2c-DSbOT2GevgUlZCuW7g0wga0_qM55BnQ37BPtk12NTI=', start_index=10436)
Annotation(end_index=10451, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc4RGD7BJQR1nBgDRnQZL1O_WCLzQUXzIhuq_eOI2n4OR5cOIvznf_QaQfgXFeXt5uZmW7ZnRNDfiYc2IWS_OZMMqKqFtu1_pxsjL4Aeev3H3PQ_TPhdr_C_9CJGe4CBRcJpVpfT9rWrqbBJYu45FhlAFTLgM7xWSJWg==', start_index=10436)
Annotation(end_index=10615, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7AojUMR5NUHAK-5s536DCP3YTHV5TitEQEvaRE3rnGhiykdCm7V_fTxNkCx8xzUgI1G_0tO-l72_IihRCE2YYweD5WlJoQ667jdyPaw6xDZsLecjqIxaocfpsr7kNP15seiZlI8eXQk7VL16WVkpG9ZHQ5elDSa4mcg==', start_index=10606)
Annotation(end_index=11134, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsO44ZulwqQOVj9r3Nj2IKj7mdqv7DikB7CM8r90L_s3e-SVLuKc-Vc3JalRJphf_fAMprMv_WicrxA39zrK_87U9kCnNcdFD8mMPnVHm8NgDy3POHe3-Kzg1KFUjQDeWSGz_YOt2QVqWHm9wsaWuHygwsVZcN', start_index=11120)
Annotation(end_index=11134, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBgQYSV-TkjAF3swpPMhgqYaz5OIHuHSa3rIavgJ3zpy4Ake6cLeQenxcabgD8PCf_h4ECdjod8iKctOJInMMQG7mCSgjxLIIdNj_JIBChJbS3eTRU1JfSFJrV6pU5E6R64oglYLRxPlfNE2gihwSrvRIgXnUGBdaY8L_kPeGTul0XqCSfVP9XMn95015WkFZku5mzrAk1KeTdevOlFXTO', start_index=11120)
Annotation(end_index=11214, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfBbfhx9H5oXHj5sD6ZmMbJ8T_By52PUXmJYfVRxlXbW3hD6JNDbKhs-Gi_KPeIzNDKDcpGp_5P4AZmS7xm1d0hjmznaFqfajS5tGnqK75eV9moNW5lN4dpkYD3_a331QfuKt1FU0rX64FNU5QiYXfqysp4ZdW1KcDc0OZCQkaacZNJfMfP2nkh8uCYjqdPYxAO8soLlYDQ6S82XuMkdfI2TS8glne2Po=', start_index=11200)
Annotation(end_index=11214, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBgQYSV-TkjAF3swpPMhgqYaz5OIHuHSa3rIavgJ3zpy4Ake6cLeQenxcabgD8PCf_h4ECdjod8iKctOJInMMQG7mCSgjxLIIdNj_JIBChJbS3eTRU1JfSFJrV6pU5E6R64oglYLRxPlfNE2gihwSrvRIgXnUGBdaY8L_kPeGTul0XqCSfVP9XMn95015WkFZku5mzrAk1KeTdevOlFXTO', start_index=11200)
Annotation(end_index=11713, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfd5H68VYwd5i39Yh3rbICbIqJElTOoDnz9Ct-P0XeoeI1Blx1h3MAHb--4HXGByOy0oZtfp-z5a_SluuwkCCXYaqcWEBpaSOdPS5ntJ3h3CNJee1IxyJs3aBslTyYrnKtMwTnR4U=', start_index=11701)
Annotation(end_index=11713, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFn6GtztfaWC3o5Gs-qDFRrjkbRJyaSE-qkmRQS1GWeQQ-Z50HVfFH6Cn9sAulm2yW1oK3ht68_C0UfHHSeY6INVa9SQoKlHmscZb5SEqfVFjX9NG0lVokXQEK1dZ02Y5Q5cIUKfVaG', start_index=11701)
Annotation(end_index=12182, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc4RGD7BJQR1nBgDRnQZL1O_WCLzQUXzIhuq_eOI2n4OR5cOIvznf_QaQfgXFeXt5uZmW7ZnRNDfiYc2IWS_OZMMqKqFtu1_pxsjL4Aeev3H3PQ_TPhdr_C_9CJGe4CBRcJpVpfT9rWrqbBJYu45FhlAFTLgM7xWSJWg==', start_index=12173)
Annotation(end_index=12289, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrfZCuqbPOD-H7TQVsCf8eVqpl9ToGxsaACTcjDus_SDAQ2Xm5yhNm4vCJSWczrat0iyrkTamoAWSwK4LWA1ioTV4I4vrerbw95o1S_gw2GM0eOhHy4DE2xf2aGzPuOLYJlrPmNyWx', start_index=12280)
Annotation(end_index=12417, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGf5UyMl4dqi9_kKKX9ftwMYQvJqnuouAqAbCfLwXBfCaCnAP7R3iScNUyJbYLj6m-PYC_CwlEZ4X9sftvJN8Wa-8RDCQaMvr0kSRFIJpIRrA1jtyrbCTdBRn70w5ttGEwZU_G1qxRu', start_index=12408)
Annotation(end_index=12742, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7kEFcLGt37trOZfTOytbOqzSB9QFBpA8GL3jJzWtTDa93Ec6RKB2ZQuev8Xm1H8TbOwUs3Agrloh-BnG89nuNLpm7jF3FdOU0PZ9VOyy5rA7m7R7Ax20HcRYdJo2T0gNP82J-o5CUyQPYANoAF07je5Y3efZW58MwAQ==', start_index=12728)
Annotation(end_index=12742, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfht8M8unG_msD4uo59jq4PbPqWZTm0dru4Ensvc9cXOwN1IIYOKoebWKb6cXikBRlN_57hrkqeGjtLmndQe099ycR5X_Aj65rQD9fDAmTs-80ElOG-R9P7_xEpbU-QDWRmp8f9heNZMdLD3QLyJqMR9dpTYVk5OSajxWt6MowwJI4lVw6FJen-iT-7JdBGxgWuejWkAg=', start_index=12728)
Annotation(end_index=12965, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_iWfa_wSwNsrDTf1S6yMA-jL4TacukMl50XazyhNfsxvXM-VVgEoLRscxftMFkQiQx-L1cMle5PH58e1ehSXndYyHGI-dmyTcZdjmvQ6Cm7cwsCFjoo33ZLSwwYOUs7GhXaSgOB7mSg==', start_index=12951)
Annotation(end_index=12965, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjRi5WNtQfJsS2sYL_1_fztEJNcUmqtQ4w2ZiNDAYPUwNUOdI5SJUDKHDYDeof9yzRfuiNwEuz6usUJrqTMudHacWaWwMiSowUURQ4DBX5aLLdqIeWO5cS1tcDaFjMyi7bbJj88jyB', start_index=12951)
Annotation(end_index=13209, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHRWAxuYZoL0iIcDb_EQOaZTpv3xDmzlIgng24bDZ_bu1RvupH27O3Y2EFwdQ1k_iUE7eCdNsb0FEQt96PVxFKlI3OAXrZoApb-Obh2xXdjBh4gpjLw1temoNRe8zih3FToA2xvktytLF9EqYZ1f2GhA==', start_index=13200)
Annotation(end_index=13574, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbsLhCnd1XGD-sAz2bmJGHDSDH0VbmKjHJaV3xWOafTgobAxnMl-auE0SfB53Na8VqRGcVtYqIY2K2AaCpZwKsrD-RP2AoNXiWS9WYifc_McSzcFuNGh-OjkF2tyrBBIf0eRDocgapCg==', start_index=13564)
Annotation(end_index=14266, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvJSHSnC5Dbogd0LQ1uToIEdYlGf6rcRXq0jsJzFFe28Nl3DM37JWCjHn633sZRKx1aQ_sArepeooUM8YWk3vQFQILdYk-9FvSYVWhjypeL1XgvxVVaBoSBF2c-DSbOT2GevgUlZCuW7g0wga0_qM55BnQ37BPtk12NTI=', start_index=14254)
Annotation(end_index=14266, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc4RGD7BJQR1nBgDRnQZL1O_WCLzQUXzIhuq_eOI2n4OR5cOIvznf_QaQfgXFeXt5uZmW7ZnRNDfiYc2IWS_OZMMqKqFtu1_pxsjL4Aeev3H3PQ_TPhdr_C_9CJGe4CBRcJpVpfT9rWrqbBJYu45FhlAFTLgM7xWSJWg==', start_index=14254)
Annotation(end_index=14586, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfd5H68VYwd5i39Yh3rbICbIqJElTOoDnz9Ct-P0XeoeI1Blx1h3MAHb--4HXGByOy0oZtfp-z5a_SluuwkCCXYaqcWEBpaSOdPS5ntJ3h3CNJee1IxyJs3aBslTyYrnKtMwTnR4U=', start_index=14574)
Annotation(end_index=14586, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFn6GtztfaWC3o5Gs-qDFRrjkbRJyaSE-qkmRQS1GWeQQ-Z50HVfFH6Cn9sAulm2yW1oK3ht68_C0UfHHSeY6INVa9SQoKlHmscZb5SEqfVFjX9NG0lVokXQEK1dZ02Y5Q5cIUKfVaG', start_index=14574)
Annotation(end_index=14773, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHRWAxuYZoL0iIcDb_EQOaZTpv3xDmzlIgng24bDZ_bu1RvupH27O3Y2EFwdQ1k_iUE7eCdNsb0FEQt96PVxFKlI3OAXrZoApb-Obh2xXdjBh4gpjLw1temoNRe8zih3FToA2xvktytLF9EqYZ1f2GhA==', start_index=14764)
Annotation(end_index=16428, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrfZCuqbPOD-H7TQVsCf8eVqpl9ToGxsaACTcjDus_SDAQ2Xm5yhNm4vCJSWczrat0iyrkTamoAWSwK4LWA1ioTV4I4vrerbw95o1S_gw2GM0eOhHy4DE2xf2aGzPuOLYJlrPmNyWx', start_index=16419)
Annotation(end_index=16526, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7AojUMR5NUHAK-5s536DCP3YTHV5TitEQEvaRE3rnGhiykdCm7V_fTxNkCx8xzUgI1G_0tO-l72_IihRCE2YYweD5WlJoQ667jdyPaw6xDZsLecjqIxaocfpsr7kNP15seiZlI8eXQk7VL16WVkpG9ZHQ5elDSa4mcg==', start_index=16514)
Annotation(end_index=16526, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc4RGD7BJQR1nBgDRnQZL1O_WCLzQUXzIhuq_eOI2n4OR5cOIvznf_QaQfgXFeXt5uZmW7ZnRNDfiYc2IWS_OZMMqKqFtu1_pxsjL4Aeev3H3PQ_TPhdr_C_9CJGe4CBRcJpVpfT9rWrqbBJYu45FhlAFTLgM7xWSJWg==', start_index=16514)
Annotation(end_index=16633, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7kEFcLGt37trOZfTOytbOqzSB9QFBpA8GL3jJzWtTDa93Ec6RKB2ZQuev8Xm1H8TbOwUs3Agrloh-BnG89nuNLpm7jF3FdOU0PZ9VOyy5rA7m7R7Ax20HcRYdJo2T0gNP82J-o5CUyQPYANoAF07je5Y3efZW58MwAQ==', start_index=16619)
Annotation(end_index=16633, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfht8M8unG_msD4uo59jq4PbPqWZTm0dru4Ensvc9cXOwN1IIYOKoebWKb6cXikBRlN_57hrkqeGjtLmndQe099ycR5X_Aj65rQD9fDAmTs-80ElOG-R9P7_xEpbU-QDWRmp8f9heNZMdLD3QLyJqMR9dpTYVk5OSajxWt6MowwJI4lVw6FJen-iT-7JdBGxgWuejWkAg=', start_index=16619)
Annotation(end_index=18430, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHc4RGD7BJQR1nBgDRnQZL1O_WCLzQUXzIhuq_eOI2n4OR5cOIvznf_QaQfgXFeXt5uZmW7ZnRNDfiYc2IWS_OZMMqKqFtu1_pxsjL4Aeev3H3PQ_TPhdr_C_9CJGe4CBRcJpVpfT9rWrqbBJYu45FhlAFTLgM7xWSJWg==', start_index=18421)
Annotation(end_index=18768, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsO44ZulwqQOVj9r3Nj2IKj7mdqv7DikB7CM8r90L_s3e-SVLuKc-Vc3JalRJphf_fAMprMv_WicrxA39zrK_87U9kCnNcdFD8mMPnVHm8NgDy3POHe3-Kzg1KFUjQDeWSGz_YOt2QVqWHm9wsaWuHygwsVZcN', start_index=18758)

## Sources
