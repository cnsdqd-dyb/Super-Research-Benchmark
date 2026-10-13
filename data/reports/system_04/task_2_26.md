# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 920b8ae0 | **Time:** 399.51s | **Cost:** $1.94731
--------------------------------------------------------------------------------

# Tribological Optimization in Artificial Joints: Managing the Competition Between Lubrication Film Formation and Wear Particle Generation

### Key Points
*   **The Central Conflict:** The longevity of artificial joints is fundamentally limited by a tribological competition: the struggle to maintain a continuous lubrication film (which protects surfaces) against the inevitable generation of wear particles during mixed or boundary lubrication regimes (which causes osteolysis and aseptic loosening).
*   **Primary Strategy 1: Biomimetic Hydration Lubrication (MPC Polymers):** The most clinically successful strategy for resolving this competition is the application of zwitterionic polymer brushes, specifically Poly(2-methacryloyloxyethyl phosphorylcholine) (PMPC). This approach mimics the hydration mechanism of natural cartilage, attracting a robust water shell that provides superlubricity (CoF < 0.01) and suppresses protein adsorption, thereby preventing the contact that generates wear particles.
*   **Primary Strategy 2: Surface Texturing (Micro-dimples):** A geometric strategy involves laser-texturing micro-dimples onto bearing surfaces. These dimples manage the competition by acting as reservoirs for lubricant (enhancing film formation via hydrodynamic lift) and as traps for wear debris (removing abrasive third bodies from the contact interface). However, this requires precise optimization to avoid turbulence or stress concentrations.
*   **Synergistic Future:** Emerging research points toward "chemical-structural coupling," where surface texturing is combined with solid lubricants or biomimetic coatings to maximize film stability while actively managing any debris generated.

---

## 1. Introduction: The Tribological Paradox of Joint Replacement

The clinical success of total joint arthroplasty (TJA), particularly in hip and knee replacements, is currently compromised by a finite lifespan of the prosthetic components, typically ranging from 15 to 25 years [cite: 1, 2]. While this duration is sufficient for elderly patients, it is increasingly inadequate for younger, more active patients who face the risk of revision surgery. The primary mechanism of failure is not acute mechanical fracture, but a chronic biological reaction to tribological failure: **aseptic loosening** induced by wear particles [cite: 1, 3, 4].

The design of artificial joints faces a fundamental tribological competition. On one side is **lubrication film formation**, the hydrodynamic or elastohydrodynamic process that separates bearing surfaces and prevents damage. On the other side is **wear particle generation**, which occurs when the lubrication film breaks down, leading to asperity contact, adhesion, and abrasion [cite: 5, 6]. In natural joints, articular cartilage and synovial fluid cooperate to maintain fluid-film lubrication even under high loads, resulting in near-zero wear. Artificial joints, however, often operate in the **mixed lubrication regime**, where the film thickness is insufficient to fully separate the surfaces, leading to a constant "competition" between the protective fluid and the destructive solid-solid contact [cite: 1, 7, 8].

This report provides an exhaustive analysis of the strategies employed to optimize durability and biocompatibility by managing this competition. It focuses on two dominant approaches: **Biomimetic Hydration Lubrication**, which seeks to enhance film formation through surface chemistry (specifically MPC polymers), and **Surface Texturing**, which seeks to manage wear particles and enhance hydrodynamic pressure through surface geometry.

---

## 2. The Tribological Landscape of Artificial Joints

To understand the strategies for optimization, one must first characterize the environment in which this competition takes place.

### 2.1 Lubrication Regimes and the Stribeck Curve
The performance of artificial joints is governed by the Stribeck curve, which relates the coefficient of friction (CoF) to the Hersey number (viscosity × speed / load).
*   **Fluid-Film Lubrication:** Ideally, joints would operate here, where a thick film fully separates surfaces. Natural joints achieve this via hydration lubrication [cite: 9, 10].
*   **Boundary Lubrication:** At low speeds (e.g., gait initiation) or high loads, the film collapses, and load is carried by surface asperities. This is where the majority of wear particles are generated [cite: 5, 11].
*   **Mixed Lubrication:** Most artificial joints operate in this regime, a transitional state where both fluid pressure and asperity contact carry the load [cite: 1, 5].

The "competition" is most fierce in the mixed regime. If the design promotes film formation (shifting right on the Stribeck curve), wear is minimized. If wear particles are generated, they act as third-body abrasives, further destabilizing the film and accelerating wear in a feedback loop [cite: 12, 13].

### 2.2 The Biological Consequence: Osteolysis
The generation of wear particles is not merely a mechanical issue; it is a biological catastrophe. Polyethylene (PE) particles, in particular, trigger an immune response. Macrophages phagocytose these particles and release pro-inflammatory cytokines (TNF-α, IL-1, IL-6), which stimulate osteoclasts to resorb bone [cite: 1, 4, 14]. This leads to periprosthetic osteolysis, the loosening of the implant, and eventual failure. Therefore, the strategy for durability is inextricably linked to biocompatibility: **to optimize biocompatibility, one must minimize the tribological generation of wear debris** [cite: 1, 2].

---

## 3. Strategy I: Biomimetic Hydration Lubrication (The Chemical Approach)

The most prominent and clinically validated strategy to resolve the competition in favor of film formation is **Biomimetic Hydration Lubrication**. This approach seeks to replicate the surface properties of articular cartilage using synthetic polymers.

### 3.1 The Inspiration: Articular Cartilage
Natural cartilage exhibits extremely low friction (CoF 0.001–0.02) due to the "hydration lubrication" mechanism [cite: 9, 15]. The surface of cartilage is lined with phospholipids (like phosphatidylcholine) that attract a hydration shell of water molecules. These water molecules are tightly bound to the charged headgroups, supporting high loads without being squeezed out, yet they remain fluid enough to shear easily, providing lubrication [cite: 10, 16].

### 3.2 The Solution: MPC Polymers (PMPC)
Researchers, notably Ishihara and colleagues, developed a synthetic analogue: **2-methacryloyloxyethyl phosphorylcholine (MPC)**. This molecule contains a phospholipid polar group identical to that found in cell membranes [cite: 14, 17, 18].

#### 3.2.1 Mechanism of Action
When MPC is grafted onto the surface of polyethylene (specifically cross-linked polyethylene, CLPE) or metals, it forms a polymer brush layer (PMPC).
1.  **Hydration Shell Formation:** The zwitterionic nature of the phosphorylcholine group attracts a significant amount of water, creating a nanometer-scale hydrated layer [cite: 9, 17, 19].
2.  **Repulsion:** This hydrated layer acts as a physical and energetic barrier. It repels proteins (preventing adsorption and denaturation) and separates the articulating surfaces [cite: 9, 16].
3.  **Friction Reduction:** The water molecules act as a lubricant, reducing the CoF to levels comparable to natural cartilage (< 0.01), even under high loads [cite: 15, 16, 20].

#### 3.2.2 Managing the Competition
PMPC grafting fundamentally alters the competition by **preventing wear particle generation at the source**.
*   **Wear Reduction:** In hip joint simulator tests, PMPC-grafted liners demonstrated a dramatic reduction in wear. While standard CLPE liners showed typical wear rates, PMPC-grafted liners showed **up to 99% reduction in wear**, often resulting in no detectable gravimetric wear after millions of cycles [cite: 4, 14, 19].
*   **Biocompatibility:** Beyond wear reduction, the MPC polymer is biologically inert. It suppresses protein adsorption and cell adhesion, which further reduces the inflammatory potential if any particles were to be generated [cite: 17, 21, 22].

### 3.3 Clinical Implementation: The "Aquala" Liner
The most notable commercial application of this strategy is the **Aquala** technology developed by Kyocera in collaboration with the University of Tokyo [cite: 19, 23].
*   **Technology:** It features a nanometer-scale PMPC layer grafted onto a highly cross-linked polyethylene liner.
*   **Performance:** Clinical and laboratory data suggest that this technology effectively eliminates the trade-off between stability and wear, potentially offering a "lifetime" implant [cite: 19, 23]. The surface mimics the "weeping lubrication" of cartilage, ensuring that a lubrication film is maintained even when the joint is stationary or moving slowly [cite: 19].

---

## 4. Strategy II: Surface Texturing (The Geometric Approach)

While MPC polymers address surface chemistry, **Surface Texturing** addresses the physical geometry of the bearing interface. This strategy involves creating micro-scale features (dimples, grooves, or pits) on the hard bearing surface (metal or ceramic) to actively manage the fluid dynamics and debris transport.

### 4.1 Mechanisms of Optimization
Surface texturing manages the competition between film formation and wear generation through three distinct mechanisms [cite: 12, 24, 25, 26]:

1.  **Hydrodynamic Lift (Enhancing Film Formation):**
    *   As lubricant flows over a micro-dimple, the divergence and convergence of the flow create a pressure differential. The pressure drop at the inlet is smaller than the pressure build-up at the outlet (due to cavitation or inertia), resulting in a net positive hydrodynamic lift [cite: 27, 28, 29].
    *   *Result:* This additional lift increases the film thickness, separating the asperities and pushing the system from mixed lubrication toward full fluid-film lubrication [cite: 1, 26].

2.  **Debris Trapping (Managing Wear Generation):**
    *   In the event that wear particles are generated (or enter from the environment), micro-dimples act as traps. They capture abrasive debris, removing it from the contact interface [cite: 5, 12, 25, 30].
    *   *Result:* This prevents "third-body abrasion," where loose particles plough through the softer polyethylene liner, accelerating wear. By sequestering the particles, the texturing breaks the cycle of wear generation [cite: 31, 32].

3.  **Lubricant Reservoirs (Secondary Lubrication):**
    *   The dimples retain synovial fluid. Under conditions of starvation or motion reversal (where entrainment velocity drops to zero), these reservoirs supply lubricant to the interface, maintaining the film when it would otherwise collapse [cite: 24, 25, 33].

### 4.2 The "Competition" Within Texturing
Unlike MPC grafting, which is almost universally beneficial, surface texturing introduces its own internal competition that must be managed. Texturing is not inherently good; it is only effective if optimized [cite: 6, 13].

*   **The Negative Effects:**
    *   **Contact Area Reduction:** Dimples reduce the nominal contact area, which can increase the contact pressure on the remaining surface. If the pressure becomes too high, it can accelerate wear [cite: 6, 32].
    *   **Vortex Flow and Debris Release:** While dimples trap debris, the hydrodynamic turbulence (vortex flow) within the dimple can sometimes lift the particles back out into the contact zone, potentially increasing wear rates [cite: 13].
    *   **Asperity Cutting:** If the edges of the dimples are sharp or raised (bulging from laser processing), they can act as cutting edges, shaving the softer counter-surface [cite: 6].

### 4.3 Optimization Parameters
To win this competition, specific geometric parameters must be tuned:
*   **Dimple Diameter and Depth:** Research indicates that specific aspect ratios (depth-to-diameter) are critical. For example, small dimples (e.g., 5 µm diameter) with specific densities (e.g., 5-15%) have been shown to be most effective in hip joints [cite: 24, 26].
*   **Area Density:** A density that is too high leads to excessive pressure; too low provides insufficient lift. Densities around 10-20% are often cited as optimal [cite: 24, 34].
*   **Shape:** Circular dimples, elliptical shapes, and bio-inspired patterns (like shark skin or shell textures) have been investigated. Elliptical dimples arranged vertically can provide maximum bearing capacity [cite: 35].

---

## 5. Synergistic Strategies: Chemical-Structural Coupling

The most advanced research suggests that managing the competition requires combining both strategies. This is referred to as **Chemical-Structural Coupling** [cite: 36, 37].

### 5.1 Concept
This approach combines the geometric benefits of texturing (lift and trapping) with the chemical benefits of solid lubricants or biomimetic coatings.
*   **Example:** A titanium alloy surface might be laser-textured with biomimetic "wavy" patterns (inspired by shells) and then filled or coated with a solid lubricant (like SnAgCu-WS2) or a soft polymer [cite: 37].
*   **Mechanism:** The texture provides the reservoir and mechanical trap, while the coating/lubricant provides the low-shear interface and prevents the texture edges from damaging the counter-surface. This "coupling" improves durability under extreme conditions where either strategy alone might fail [cite: 36].

### 5.2 Hydrogels and "Weeping" Lubrication
Another hybrid strategy involves using **hydrogels** that structurally mimic the porous nature of cartilage.
*   **Mechanism:** These materials can release water/lubricant under pressure ("weeping lubrication") and re-absorb it when unloaded, dynamically managing the lubrication film [cite: 38, 39].
*   **Challenge:** While tribologically superior, hydrogels often lack the mechanical strength (fracture toughness) required for long-term load bearing in hips and knees, leading to research into fiber-reinforced or double-network hydrogels [cite: 39].

---

## 6. Material-Specific Considerations

The strategy for managing lubrication vs. wear differs based on the material pairing.

### 6.1 Metal-on-Polyethylene (MoP)
*   **Challenge:** The softer PE wears down, generating millions of sub-micron particles.
*   **Optimization:** **MPC grafting (Aquala)** is the gold standard here. It effectively turns the PE surface into a cartilage-like super-lubricated surface, preventing the adhesion that tears particles loose [cite: 19, 40]. Texturing the metal head is risky because it can abrade the PE if not perfectly smooth [cite: 1].

### 6.2 Ceramic-on-Ceramic (CoC)
*   **Challenge:** Very low wear, but susceptible to "squeaking" (stick-slip friction due to lack of lubrication) and brittle fracture.
*   **Optimization:** **Surface Texturing** is highly relevant here. Micro-dimples on ceramic surfaces can improve lubricant retention, preventing the dry contact that causes squeaking [cite: 12, 41]. The hardness of ceramic allows for texturing without the risk of the edges deforming.

### 6.3 Metal-on-Metal (MoM)
*   **Challenge:** Generates metal ions and debris, leading to metallosis. (Largely abandoned in clinical practice due to these issues).
*   **Optimization:** Research has shown that larger femoral heads and specific clearances promote fluid film lubrication, but the biological risks of metal ions remain too high. Texturing has been explored to reduce friction but has not salvaged this class of implants [cite: 1, 42].

---

## 7. The Role of Synovial Fluid Components

The competition is also influenced by the biological environment. Synovial fluid contains proteins (albumin, globulin), hyaluronic acid (HA), and phospholipids [cite: 1, 7].
*   **Protein Aggregation:** Proteins can aggregate and form a "sludge" or solid film. While sometimes protective, this can also increase friction in MoM joints [cite: 43].
*   **Biomimetic Synergy:** Strategies like MPC grafting are designed to work *with* these components. The hydration shell repels the proteins (preventing the formation of a high-friction protein layer) while utilizing the water content of the synovial fluid for lubrication [cite: 9, 16].
*   **Viscosupplementation:** Injecting HA is a temporary strategy to improve the viscosity of the lubricant, aiding film formation, but it does not permanently alter the implant mechanics [cite: 44].

---

## 8. Future Directions and Challenges

### 8.1 Personalized Tribology
Research indicates that synovial fluid composition varies between patients (e.g., healthy vs. osteoarthritic). Future designs may need to be optimized for the specific biological fluid environment of the patient, potentially using "smart" surfaces that adapt to pH or protein concentration changes [cite: 41, 45].

### 8.2 Durability of the Modification
A critical question for surface coatings (like MPC) and textures is: **Will they last 20+ years?**
*   **MPC Durability:** Studies on the Aquala liner suggest the graft is stable and durable, with simulator tests equivalent to decades of use showing maintained hydrophilicity and low wear [cite: 19, 40].
*   **Texture Durability:** Textures on metal can wear down over time. However, since they are usually applied to the harder counter-face (metal/ceramic), they are relatively stable. The concern is whether they will eventually fill with debris and lose effectiveness [cite: 46].

### 8.3 Manufacturing Complexity
Creating nanometer-scale grafts or precise micro-textures adds cost and complexity to manufacturing. Laser texturing (femtosecond lasers) offers high precision but requires careful control to avoid thermal damage or burr formation [cite: 47, 48].

---

## 9. Conclusion

In the tribological design of artificial joints, the strategy that best optimizes durability and biocompatibility is the **decoupling of the bearing surfaces through enhanced fluid-film lubrication**.

The competition between lubrication film formation and wear particle generation is best managed by:
1.  **Biomimetic Chemistry (The Leader):** Grafting **MPC polymers** (as seen in Kyocera's Aquala) is currently the most effective method. It utilizes the body's own water to create a hydration shell, reducing friction to near-zero levels and effectively stopping wear particle generation at the source. This directly addresses the biocompatibility limit (osteolysis) by eliminating the trigger (debris).
2.  **Geometric Engineering (The Support):** **Surface texturing** (micro-dimples) serves as a powerful auxiliary strategy, particularly for hard-on-hard bearings or to provide secondary lubrication safety nets. It manages the competition by physically trapping any debris that *is* generated and generating hydrodynamic lift to enforce film formation.

The convergence of these fields—where biomimetic chemistry meets precision surface engineering—represents the future of the "lifetime" artificial joint.

---

## 10. References

*   **[cite: 1]** *Lubrication, Wear and Tribological Performance of Artificial Joints* (Source 1, 28, 38, 46)
*   **[cite: 49]** *The Crucial Role of Lubrication in Joint Replacement Design* (Source 2)
*   **[cite: 3]** *Advances of Wear Reduction of Artificial Joints* (Source 3)
*   **[cite: 43]** *Tribology of Hip Implants* (Source 4, 73)
*   **[cite: 11]** *Bio-inspired Low Wear and Durable Lubrication* (Source 5)
*   **[cite: 17]** *MPC Polymer Surface Modification* (Source 6, 78)
*   **[cite: 18]** *MPC Grafting on UHMWPE* (Source 7)
*   **[cite: 21]** *Antibacterial and Biocompatible MPC Coatings* (Source 8)
*   **[cite: 14]** *Biocompatible Polymers Designed by Nature* (Source 9, 79)
*   **[cite: 15]** *Effects of Structure of MPC Polymer on Durability* (Source 10)
*   **[cite: 9]** *Biomimetic Hydration Lubrication* (Source 11, 60, 62)
*   **[cite: 20]** *Hydration Lubrication by Polyelectrolyte Brushes* (Source 12)
*   **[cite: 10]** *Hydration Lubrication Paradigm* (Source 14)
*   **[cite: 41]** *Effect of Synovial Fluid Variation on Tribology* (Source 16)
*   **[cite: 7]** *Lubrication Mechanisms in Total Knee Replacements* (Source 20, 25, 42)
*   **[cite: 5]** *Mixed Lubrication Modelling* (Source 29)
*   **[cite: 24]** *Surface Texturing for Friction Reduction* (Source 30)
*   **[cite: 1]** *Surface Texturing in Hip Implants* (Source 38)
*   **[cite: 12]** *Micro-dimples in Artificial Hip Joints* (Source 43)
*   **[cite: 35]** *Texture Morphology on Titanium Alloy* (Source 44)
*   **[cite: 25]** *Micro-dimples and DLC Coating* (Source 47)
*   **[cite: 6]** *Friction Size-Effect and Texturing* (Source 51)
*   **[cite: 32]** *Particle Size Effects on Texturing Efficiency* (Source 52)
*   **[cite: 36]** *Biomimetic Lubrication Strategies Review* (Source 54, 85)
*   **[cite: 26]** *Surface Texturing Optimization* (Source 64)
*   **[cite: 28]** *Hydrodynamic Lubrication of Microdimple Textured Surface* (Source 67)
*   **[cite: 16]** *Highly Lubricated Polymer Interfaces* (Source 77)
*   **[cite: 4]** *PMPC Grafting and Wear Reduction* (Source 79)
*   **[cite: 13]** *Surface Texturing and Coating Combination* (Source 95)
*   **[cite: 19]** *Kyocera Aquala Technology Award* (Source 105)
*   **[cite: 23]** *Aquala Hip Wins Tech Award* (Source 110)
*   **[cite: 40]** *Clinical Results of Aquala Liner* (Source 112)

**Sources:**
1. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK8xzsQ8j8u7PnQ7RmxqLoWecE7E_7lbTSwL-8bAEoYikFVO0pSmA8FmSKzsVd4Imh8ibWnFkXJM1fKusttMj_P89q0bsr26ad2ymLTr6m8AKff8il8gcktLdXKdI=)
2. [whiterose.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEph0-bLtpQiddTZ5-EgTtwKvtTUZndQWGK0ai-rCEuAOyW9Q1_fJQXOVhNQDYfGKs8B-W6KnQ95ks22muZGG52ankGi2QZ894kZZ56z2aMSdNgF6EK0oZDMCRzRMJ93Lc7NF9xZXADLMxNv-uPaPvMkt_awHiNme_F30kchIkQemAYw3JYwiVqTT2CuT22EWD5LoEqzmQ2k6yLdxffI4h-3HTWn07M5SNHxOwtFo8q6CmXx04G-cyjgtrexyprzdYE7Ht1MNLHZkQwLPA99e8_YrfDxp8P1TtIbYCC)
3. [core.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEX68WDnJ3GKoW-cpfw0rdJbkn8rV72OtPrYwnR1HazUFKHUDS0llIlC79ThIHK6r01RvgNBQtwMgPFZvS8vvhCSp2_DlJX7PlMd4WNt-DNchUj2KkexDJCN5Jj_6-aHY_RvQ==)
4. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfIyYu-bmJSONZ6wa4IL5eDhirP5DDZ0QyEghhzG211UlkoXCSpwOrgB2yR-2suSDlwc30ghTZ3wH2-uUMw3zSiKagmzFL_xWPX4KGhsbtA31QIj9AuQaZBwBMbvjb)
5. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbLghkI0ztgUocVns5V517Tk0JM_EiBPN8ApdQLbM7AI1almqc8lhxmXHvs45XP6xJyMWFtw-8CIjurGzMLsbZeMnHxzXZNu0VMIw1Jm652SXOL7m2O2cRL-U_VTxdGSygBfZZjBuGEsr4fxNcOXDr-g65LPx6JytGMhg2zcNaL2P2L8JLJ-2XWAdTzntA0ldjRxreWxhfaSGjEaMw7A==)
6. [ntu.edu.sg](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuPzPyb2guZhMmHJvfTz3booaHDudiXn0ZMonHkXaTC3lYAWCht9H40qtauUWLgMf698p5SfPsR6r3AtOb68K7riU-Fs5NdzDR15fTF6q9pqALcEfUceVskmL4GR2RWelpIwgtmoVgcEMZ_dHXoxljExXu6y5Yl9dg7HZV4qtefS0yuXRrp9EUIGCb-ZqCgZ6C8w==)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1J_gcwb-jrFsc5AYz7NEZ0EEI_g-08rml7pdlQOHexmei1KQb0wucTBIyJi42GC0e3CdHsdMAlkx-w0GzwU0E-r2OSUdbTIzg70PYXk78SkKtMb5mq05XOFJqwXWdXjSFkBBf2V5yd664gTaHdue45ibnsdWyICqW3aqRZxlI4C7EjwRdYqsOQY-383QiHDGguMEDAYLXx4LVNxGXKRkAu8Uwn83kBU2I6bD1kDgcDQDPBvKseK3_JsIPPqaRIOYGoZ9CaQNI_0lOQJOTBLd9qAIr6Z6xLY6_q_x5)
8. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOBKfpYf7klvFyNOB5JwUIiDSmg5ghJIgJ98hKDhvdJpACTJ4RQ0xpFrbk2DImNbuY0NAIu9plym0snGGA7hISC2rXJMHCDIGRFamJtFLuewPxPbyBFgxzgOykVL0=)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8K-6SdPRNGlx9tAlZ2NuDjh1vCpZDogu5rWJEqefgE4lcHtX3sLHsRONCKh3Odiby0XWvrpWScNp6WSHkspW5wX1Ng9Q-oQXsxGS-RP2xjju6xAm6hlQ9TqCBcXqH)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFElkDCIHUvqpY_C1ijieuy0H4wS7W9wnKiCmS_K7EByvrMfU2z40pKtjLB0a3xSr2T039CeVPX83Iladrd-qUX2kmErYJbPWl6tvdsSTNQNsi4YUJW1rPc-Mg1R-pnxHynu7qnhHLyEwr5Q1QBbyQgNhtwlrb4r5m3HBiHpw==)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPoiS6-pvBZ092rjLs6f2Pq5NDUcpKQrTtxxwmH_bksodRyLtUYzd4ayAI-DkcegkZV5epImUP7LS6rip6TqsRPMFAxuEEC4g5wyAXu3rSFz9rrVMy-NW3gCpYcmy_GOzNSwp-trRxT6JwQPtMrg3mIDMNGzkURBq1xj-R5rs807DsHFl0bcNGw0VPhwG9feYy-KlNgNyHQk30bNoW4UTuMNaqjMvkqdYTws_weYetvCB7KJQnWx2FSNIrT1wI_m2NNTWj7GhUu6nCAC7Nn4SIeIicmOuNXhJwytLVTA==)
12. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0uYuuU8J1m3TDQPLMdQaLfU67R0Abeg2TZCvGCRfQKUJdyCZyILm0Yes7MAg2zOl1oQ3XW5bZe7pb_jSKtQKLmxJaVQqEfswtJ85q2je9EcpBSdK6jrXjWK5YbM0wSKHdqYwpjJhNqYmqDb0y4LDA6hougf6-yNToYs-jxmWA1x6M5Q==)
13. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpIhkXHDBRrl5rJ38-gbubAHHgZtyvEI2nPCVUrPGwWswUApSiBSiVg3VLwvKR7G1jmJ1mRzE1kJaHV6npTj6KAfndqYgDR51kTw_NuMVyu3a-csY4q67gz_qJldHMtalR6hhZtpI=)
14. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfkteLzEx1DXk_U5uWUtluzWku_KsQYFjmC9MKdkofdkF-SYjBD7pu5-aeOKQ9qttSXrhGwJAlfsT5XmdQYe9enZIoL7y-xT2hMwObC_gO7N-gE7QVOWYIGyr7xmGGVA8Il0c9b9nAgjBhDEobUK8Z9lJGut1OtJqYRs2nsl84LGOukxMxVYdLC6qptdvnDoZPo19JryW__js-x_cMohlSUV2KnAE8l5SADIgpbKoLujZgyF4tEdw05_nnBtrMjmsByg==)
15. [niph.go.jp](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFx-tLEfu5eoSeMhw2moj7KO9s1NspzWdxNAhpOBBUxfg_kJHawFcuxxyjFTREiRfoxdcwlc-03nNhxg_HaFrzo9aRtuvJlB74HKa2FJmktptZayWvRswquYvqHWhcIEIIOyYmFMLXMg92FzHqnfdPi5NbO4Iom7IC1JHqUD9P00lbmXKfWT3mSd6U=)
16. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfYwzlPBMUmiuAf7yx24lDY23olNYI7jhc1teg4jspASOfd3owj2cLxSpZAlQQyjCNSxzPdfiT5OebAEmKTzzi4r_knzkTEtpOIqExDk61aAyB9amaJ5e1T_jwrO-W8qw6Sxy79rQq)
17. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHprrnzStcrKLSDhS_OXD-WaV30WQ_PWhdlC5iAfvgMTt-2I-LmUZ-Ac9TXkawNk4Hadp7E6YNt2Ei36zpxdMevnIGeoebJnX1zDdTgL1ndDD1dldxn7Tqp0BPn9YYv-PDQLzGi5QcP)
18. [worldscientific.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuzjCZeK6NRvFUc9lzyKtp7WTeYJrGRprwl5o3wH82nLYdxJuJ5lNQuTT4Qgk6ctlnzBb-S73uAPuHJWwpGyDf5ZlAGOPITc3bgdQifcY2YDZqltqoqNiSgBlqsNZ47UsWzWpCo-WnHPNuSQ9705EELgVwgb-l)
19. [kyocera.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETtLDIhE_McKjhPEYT08srjuC7yXHGMmbqaLqp1LQIiMkx9VqIcHorXo5qJScvqBkDXVIgglEkpfZggctBLeqxJqT9v3x1KnjRS55RyAMIKgTAMob7eMIkG7PlmxLWo12CvHeKeZXG0yazrQ==)
20. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpXucEhyfgsDRfkfzHjwOCuansQGZQUnmzIozQj1pC4874tmqeMP_SsxI0wBwPBjOyErsD1FPX6IF0pp0sgwP-yxgUzMDIJ9ZY9j-urzP7L6qkE01q6gx-1Q0DC8c-Ql5adVT6zU457A==)
21. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgRXiQnz9a6i6iZ1riBef5fLRbHsrXqJlAaBJj6kUX8RtJCaWn-SLpmPgC0chbLsNtkSdHIks3hR6rdO2rO6ZaK5fgC7vSvqcT68T1K1361qV8rEPWev2JMhTPmaSE0RpJhsH9ohM=)
22. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQET_Av-FQPgNisF6ExnmzACHxMCglHY2xBw_eebt077UEaCzGuhh_oLrK-Qq0fvJAAWZTzBIPaZ11lerOP-Ng-215G0TcPCTX8CqGwBumrOASWOjHjKjVJzwcBDxFd05TVFzUINiI-dYE5HPugnXNdNTVxq117lrKfBoEzoFVYYBo46H0zw6hrj7JpxoW6TtRsl6_virCr16cn3kS9v7jqKKEY4TIBWq-GBBiD6moLwuKWeKJfGrhBHcxeMFjrrjTIzFuFSV7XqMYpRnWOD)
23. [ryortho.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESa6grsgjfcUjT4Wm5J3mAx1uKN-8vKreTGLHJhhHItVZicpEIhO39GYc0IXCDG48_LqOOwgWjnvCRwnHa1RUvuzNg2wrRsBxeGlIe7aW2G7zDKdCQC5YZ9QGUNud6j5ZeRqnfGbF73AiO3SX4jn0owUYd84NXb1zwBRtrGbdpHA==)
24. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtpe3VDgYnS8W7ISsuSn58x5dlDqUQod9fPqlYTUanfj7eSTbhx352bYO-Tc7R93Yw_HcVimtu2i7aUVeMs-UpRERZFWDWBaZZSLYIH_K2VkjbGgYA4J-J22F99hQ=)
25. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpk_XF1Bza4fGHRCJAFJlKcP4fvfQ_0lfqpW2h3VtnSpilb6hoGTmXJ5ZpBsfwHNZGZFFdye0u9XoVPZLfoZtOGxLCHJgm3ak9Ay8IbCoucRULsJaALyKstCZvYRepPxm5HEw2Jn4=)
26. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGo9uDfeL8CH1XPK00sLi3gYu3p8eqDJqYUPyp1VZUmSOX5Bzf-odgXriQpfTjZQQsXXTXbfHleQR7ZUzCaT9C6Ss9Dg0KqC5mBvcG-ZXJsgRvIxJthfKJXY41Cg==)
27. [soton.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGD_vDJkjXX70gUsIpAdU4MN0KG4DMIkbzC0D7eaRc8R7woc5Lt_Fj3cMCh1eDnWZWJ2_QQkB1UFjZx0QfM87Rb_anm9ykK9ujHpzzK3HfxQfUTMj3mir3KYsVjJ9w7VU5VUdBLblTCtiavlypRt4Oj62MEz949dH2lE2_Tel4819RiWPnJQ3lYsrPNaUsAFJGwttQlbeFPl3DF2SbGjbLyrX3EPnO2R6MBZhHvm0jvHWib-oo=)
28. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGjP347VogiSeiIEQt2dn_ZmXivhXmdVSHUKLWcmgIufGEuaRefnO0Hf05rmZICzjFocyo6t7V_xLMvwYOkJKAY4HQBrZ1uR1BVk7-3pP_HYtCFW7aUX_Zf39TPRjZuVxVQM6ZOtt20Zx40qQnFjJ5hjFbtIjlU9zBATQPnqju5VrEAY5zV7CoA9OF5E9SrkRX-SGoV7FGFGeZEymXkNyMMAarmot3d4Hbda0uGKJiBGDw4SrjBuGvEyEge4U=)
29. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmJy_VHBJVV0j74cWPVtkvLTWE1MhToe-nz4FiOe9xK4yTztckj3Sa2REbzYvraG6lICBjIGUhm70cqVnsrWzz6kXWUgPVvcdTybB8DOu9VKFsoF2VM8SyZPyXH8529tLqvO5w--iITTuptqBzEG3nQ_HtKT2TaLozRzem23RM9Svg2k6f2e5hhpPXU6XMKFOeo_Lq1Nox_yy8buw2Ur5GjS12D-yWarVX2OsO5HQr9b8pS96N-hUI7Nor168uh4GErpbS9x2ECkB7EUzI5Leg3mE2nkg=)
30. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHP4vFcFaS5O5_BrjJd71Ophk2OzlDoIDP7yNdurZXEVy-9TUGCG-UVYiTzas9HKFXXPHBiWZzo0jgAyalEeRncHdYw7-3a7NRXnJ64obSgE-UMVJK4V-fdaae_U-bCSLZdAZIXOQ8t)
31. [scribd.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHv5g6t_u4UwtUBx_xmR9CXE2e_EOHZYqXUjceKmIqJVMgukBZ2I2eGfAtxm_VX1Axy7cSdXkNlFTD2Z0ILmjfnVR2E4wAP9SGDw2JAOr1oGLgC_m-mHnuhN_3g-GCuHlK4Si2ltS1Cp5HXYs2nOkc9zdMr86ikEGKBRzn8rAuHd1Aa8L5uga9mbfjFuur0H8h2nGUw83jJoOoY6cHh_Rkqp4D3XLt8pY1zvh7q6iA4J-TjkA1KyvVhbgBvPMeCk7lCZEcVPm6zsJNOwUUIwL-xptUHQXVM14Jfw==)
32. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpdFJk-vFvt9WPaoEf3eUWVnGohcTGtuKuZodQiE4Awj2jLCAjZn-ut5g20M6JebihnxU_wJQMIPwi-L7gKeJ2BXJnjhVF94ahXKrjCAXv4E4EbM4K-gTqD2fmFQbBfhHZizMw6MlScC-IHLYbPhXAeShRGcA4lVqxmpMBfO8BkkEEPIGBSR4apdRamLPCJgEmMaqB3W72Ni4El_tefvjCGWOWrgN0e9vbLUiPnPI_OKoUzHEKqQ==)
33. [lancashire.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEhRqoMkF0Yt9TRbZZ7ODvUIloKbjqGR2kNa5LdWaKtNPtP4JsYxAIae-gkAMUqTo5Y8ygIoIJ1EJnB50OtfzO32lpoPNWgwo6S-LW0YfOG_g4VdA13UEHGp0mNFxZ8BGX7ndh_yflhcTDoD8PuxC7ULkytfZKFdEinLhJ1aw6dkQ=)
34. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZG9lkYzETRg9PcjCwiJN0MacfQqNgHREH475Ezvg4sQvw-QrzlsrZ_5E5eZgTAbPOWxTpPhAfRhdF6TwP6K_QAL4EkEwQMVAKLX4Uhx459UWPM_ukVXwsver7zijomscTDyFsV-8UZzwZcpLHe68BeBpS)
35. [scientific.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGn24x2_KrMrbyq_C_eIwwyHfGXgkcs6OHIY_D4WGKXCmoBU8YE1ncZN3FIaycheDwOcC88g5O4f5bkHNKrKvN03ViwIS4_pSGQJaHnVmI9WFBHu9tJXmVcaqU=)
36. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVcR4p4BPQCtn37-iLZfcNf5Uf64JcPUOzgcIEjSO1diOD18fuJ-w8uM_DJhkNpRT6oDr8LilLPqGF8TiHnpjPtRoh8Z6YtEiA_HtjiUibapYfXcdbFWnPGCBQNn8=)
37. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqKQWHa1SKkWlnDRGVx2nLugDY6PAI_5WGh3FpDH_Bejlhinz_rEvBHhQx68uIUFpd4_EFsdpzYLm-Ay3U3rkFQK1Ejk4w0SX-2lMliFfHZvk78MXtOCQaliOxnxmL_mWeVnn-E9_qER5Nw2ryGF1Hk444kAGoH7kg1ZD1zBjJYQvEkCxWT0tzXjDSehbSKrXBVtzN-D6ec9M9SSvJlg0OhaQB5aXj4Opw9MFLsm5wP4V8V0NzEuwzBrtjZndE2W4CIKhK1F_yZCyNurzMQKZJ2rfKInHMMlNHBe2f)
38. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvBzgBxCbB5xKycdnbMFgzCXxm_4Fg4yEFdS62-Vz1VsmULnFmE1Qujre-ywkWEgQ_r1YCQcIXo7GBd6i1CkZxX2XQH9Ss578dHbCHCEdWdmo-uRtziSmE22st8gNLrBpe27OGvZgRLHZufS0tyW6cKCtJTRc4tEcoQlO3ngDCCAqDtsoKrL_C3AGlSxq2XZBZiDrI9mLa4ErUUi-O0hLQXpDGNU9MaXKVOZ0huvWF2cevp9_HalfCPyXhLUFRrD4J)
39. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGW3YHBJqN1Qqy6yI-yksnZ98P64Z_YJ-nYTL4A1oNCYZvYRsz2Q8_TgsrGc8s529RwfDs9y4Mtc0GBR0Xv-iJ0tKerBE2u-E2stfXVwLQ1Tho7QosAP5QJm1av)
40. [niph.go.jp](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHB1UbRw0mnLtB-yWcIbxjaHEzR9TBSYDD0g7E8QkSt9LnfrXeEKOroJ3TEawPy2Ut3lz8gRDQiGmPATRpSSd_hUMFG02vjAiUg4X7kmTgmz1It-EXnoh33_d_U1PhgQRCnHw3G-Cnb7S4v7IfNQmKgE8zm7epc-kCCL7o_2nka85dUBGjp_laV6KI=)
41. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrRq_I-KVMKKflWfvLlJudEGRhC30DiQF9pRApubTTEF1kis7pslkxe2RIKbpGRV3yeTYDaNGYOGxVXmfuBppU00bATEMEkWGuk3tx7rTjL1SJoMjPD4CBSBr9uOHiVsps4jH-CAxpMouisfe9fUsQC3ePHABQdQ==)
42. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGtEVSot8lEYZFWjablFkDQmahbWti1tIDbnQonPTOUUvRRtD8VsJwpw5az55FxRGXfiM7Rkcng5E2KQIogU02dmv3XmcCixd6xoy0DHKjNcw63Y_4NXav7FJjrEoPoDWQ2xYdS-I=)
43. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkgAt-zeLn60q5v5C1kLzMeCP6lpQYu9kgfI0qNyZEonR_nktl-IDRYigkX3GtA_LBrlq0Pz4J0nCP7-M1r0MtVYHVAbPcgtI_QFuqqGKEF3OgZQCzpERDXEq8Iswi4n-vzX7ZC_0=)
44. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrB7HKiszqAIsM7tbWfJsEdCSfWujQwBwQFOP6M8bTulD66hCPD6T6DFQZgU5ZvIbFO0G-pWV-PcSsA34I5E-ctHfoN2a1bm9UH8BffCnVDoM_6zT-O8sH3FmRRDWPgjuFlwrkNsvXM2qo84soQUCaSb5rvnO8Tgy0ZhAdi1vTcg==)
45. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEedXG6Zvk_tf2x3S3R7EBGMravPZoOnLag9ZkXWXXi06PhLQP3tl_a3pKxRy6aEBvYQgX8hSWbq751ugXpSPbhDa-RBVBEEgCuR9gxaP5BS9ln17X2s80CidVEdMDWZ9f9LdMMec8=)
46. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDUVFsDCnY0fOvL4CLIqcaYkPg3eAPNjHCQytd_c2HqmKbuvReQ6arBS11RlKDphuu6nfBmdoqyDjWSmcRCs-1vLqAt_iEON9_ANvPFE-irmLAmwwep0VQQwwIbnSf-3PTyFUkEevsxCxpcKSRWR5V4HqP5T5_9rBdiC9573JvUhGOYVB1Z6JLU4Um2rKlGrSy14zq22cZFpZCnqPEDhSbzHce6Oq45eptLUMHhphOp83JWF1LurCZVOidp59YZxTaCf1aYjdHZp2ttEGcSALzM7t9onfM)
47. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxrws9afwXY11XbvbkCoxUmbJvNE2DT9Qg4VKBdijKuVrR3Zod2GCTU3xaCzsUg7LuDk8fGxKp47Lwz-LW7DN9pEHWIwb6DHiKRqBZN3epG6WADckXrW2wGbNZZQsg9N-vo8EzTtQ=)
48. [sensofar.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsaFwYhhfNUH0hA2HRVjC5AFq1YG3raM7_RJW0S6A_gXspIGJaO9C_DruH_qZEneav2fisYLyywnJ_eY0foXtn_h2vc7BNp4M2NtarQ53Eevfh8mLiWlC5YEliVc8PuZd0yPbi8vDBQmpeJbszl-IaCo3Vj7pWQR8Q8NoV)
49. [biotrib.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTCJcxgLH3XNBxUnBVc59Ne7l4E45SSrYj7kKQ-zTvLX6rANHSSPQjKFAluqQsctABl6RnfJcMhKl--8hm4xQB_w5rVfXqyv2mTboIW6oVMpNYgY59YoMPZCH1dI644ISZ81KpFuwwRYkABbC1eexMTwhSb3EE60UaNhBcUKAwN411Nbk=)


## Annotations
Annotation(end_index=2003, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEph0-bLtpQiddTZ5-EgTtwKvtTUZndQWGK0ai-rCEuAOyW9Q1_fJQXOVhNQDYfGKs8B-W6KnQ95ks22muZGG52ankGi2QZ894kZZ56z2aMSdNgF6EK0oZDMCRzRMJ93Lc7NF9xZXADLMxNv-uPaPvMkt_awHiNme_F30kchIkQemAYw3JYwiVqTT2CuT22EWD5LoEqzmQ2k6yLdxffI4h-3HTWn07M5SNHxOwtFo8q6CmXx04G-cyjgtrexyprzdYE7Ht1MNLHZkQwLPA99e8_YrfDxp8P1TtIbYCC', start_index=1991)
Annotation(end_index=2003, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK8xzsQ8j8u7PnQ7RmxqLoWecE7E_7lbTSwL-8bAEoYikFVO0pSmA8FmSKzsVd4Imh8ibWnFkXJM1fKusttMj_P89q0bsr26ad2ymLTr6m8AKff8il8gcktLdXKdI=', start_index=1991)
Annotation(end_index=2353, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEX68WDnJ3GKoW-cpfw0rdJbkn8rV72OtPrYwnR1HazUFKHUDS0llIlC79ThIHK6r01RvgNBQtwMgPFZvS8vvhCSp2_DlJX7PlMd4WNt-DNchUj2KkexDJCN5Jj_6-aHY_RvQ==', start_index=2338)
Annotation(end_index=2353, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfIyYu-bmJSONZ6wa4IL5eDhirP5DDZ0QyEghhzG211UlkoXCSpwOrgB2yR-2suSDlwc30ghTZ3wH2-uUMw3zSiKagmzFL_xWPX4KGhsbtA31QIj9AuQaZBwBMbvjb', start_index=2338)
Annotation(end_index=2353, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK8xzsQ8j8u7PnQ7RmxqLoWecE7E_7lbTSwL-8bAEoYikFVO0pSmA8FmSKzsVd4Imh8ibWnFkXJM1fKusttMj_P89q0bsr26ad2ymLTr6m8AKff8il8gcktLdXKdI=', start_index=2338)
Annotation(end_index=2748, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbLghkI0ztgUocVns5V517Tk0JM_EiBPN8ApdQLbM7AI1almqc8lhxmXHvs45XP6xJyMWFtw-8CIjurGzMLsbZeMnHxzXZNu0VMIw1Jm652SXOL7m2O2cRL-U_VTxdGSygBfZZjBuGEsr4fxNcOXDr-g65LPx6JytGMhg2zcNaL2P2L8JLJ-2XWAdTzntA0ldjRxreWxhfaSGjEaMw7A==', start_index=2736)
Annotation(end_index=2748, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuPzPyb2guZhMmHJvfTz3booaHDudiXn0ZMonHkXaTC3lYAWCht9H40qtauUWLgMf698p5SfPsR6r3AtOb68K7riU-Fs5NdzDR15fTF6q9pqALcEfUceVskmL4GR2RWelpIwgtmoVgcEMZ_dHXoxljExXu6y5Yl9dg7HZV4qtefS0yuXRrp9EUIGCb-ZqCgZ6C8w==', start_index=2736)
Annotation(end_index=3177, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1J_gcwb-jrFsc5AYz7NEZ0EEI_g-08rml7pdlQOHexmei1KQb0wucTBIyJi42GC0e3CdHsdMAlkx-w0GzwU0E-r2OSUdbTIzg70PYXk78SkKtMb5mq05XOFJqwXWdXjSFkBBf2V5yd664gTaHdue45ibnsdWyICqW3aqRZxlI4C7EjwRdYqsOQY-383QiHDGguMEDAYLXx4LVNxGXKRkAu8Uwn83kBU2I6bD1kDgcDQDPBvKseK3_JsIPPqaRIOYGoZ9CaQNI_0lOQJOTBLd9qAIr6Z6xLY6_q_x5', start_index=3162)
Annotation(end_index=3177, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOBKfpYf7klvFyNOB5JwUIiDSmg5ghJIgJ98hKDhvdJpACTJ4RQ0xpFrbk2DImNbuY0NAIu9plym0snGGA7hISC2rXJMHCDIGRFamJtFLuewPxPbyBFgxzgOykVL0=', start_index=3162)
Annotation(end_index=3177, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK8xzsQ8j8u7PnQ7RmxqLoWecE7E_7lbTSwL-8bAEoYikFVO0pSmA8FmSKzsVd4Imh8ibWnFkXJM1fKusttMj_P89q0bsr26ad2ymLTr6m8AKff8il8gcktLdXKdI=', start_index=3162)
Annotation(end_index=4212, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8K-6SdPRNGlx9tAlZ2NuDjh1vCpZDogu5rWJEqefgE4lcHtX3sLHsRONCKh3Odiby0XWvrpWScNp6WSHkspW5wX1Ng9Q-oQXsxGS-RP2xjju6xAm6hlQ9TqCBcXqH', start_index=4199)
Annotation(end_index=4212, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFElkDCIHUvqpY_C1ijieuy0H4wS7W9wnKiCmS_K7EByvrMfU2z40pKtjLB0a3xSr2T039CeVPX83Iladrd-qUX2kmErYJbPWl6tvdsSTNQNsi4YUJW1rPc-Mg1R-pnxHynu7qnhHLyEwr5Q1QBbyQgNhtwlrb4r5m3HBiHpw==', start_index=4199)
Annotation(end_index=4432, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbLghkI0ztgUocVns5V517Tk0JM_EiBPN8ApdQLbM7AI1almqc8lhxmXHvs45XP6xJyMWFtw-8CIjurGzMLsbZeMnHxzXZNu0VMIw1Jm652SXOL7m2O2cRL-U_VTxdGSygBfZZjBuGEsr4fxNcOXDr-g65LPx6JytGMhg2zcNaL2P2L8JLJ-2XWAdTzntA0ldjRxreWxhfaSGjEaMw7A==', start_index=4419)
Annotation(end_index=4432, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPoiS6-pvBZ092rjLs6f2Pq5NDUcpKQrTtxxwmH_bksodRyLtUYzd4ayAI-DkcegkZV5epImUP7LS6rip6TqsRPMFAxuEEC4g5wyAXu3rSFz9rrVMy-NW3gCpYcmy_GOzNSwp-trRxT6JwQPtMrg3mIDMNGzkURBq1xj-R5rs807DsHFl0bcNGw0VPhwG9feYy-KlNgNyHQk30bNoW4UTuMNaqjMvkqdYTws_weYetvCB7KJQnWx2FSNIrT1wI_m2NNTWj7GhUu6nCAC7Nn4SIeIicmOuNXhJwytLVTA==', start_index=4419)
Annotation(end_index=4603, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbLghkI0ztgUocVns5V517Tk0JM_EiBPN8ApdQLbM7AI1almqc8lhxmXHvs45XP6xJyMWFtw-8CIjurGzMLsbZeMnHxzXZNu0VMIw1Jm652SXOL7m2O2cRL-U_VTxdGSygBfZZjBuGEsr4fxNcOXDr-g65LPx6JytGMhg2zcNaL2P2L8JLJ-2XWAdTzntA0ldjRxreWxhfaSGjEaMw7A==', start_index=4591)
Annotation(end_index=4603, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK8xzsQ8j8u7PnQ7RmxqLoWecE7E_7lbTSwL-8bAEoYikFVO0pSmA8FmSKzsVd4Imh8ibWnFkXJM1fKusttMj_P89q0bsr26ad2ymLTr6m8AKff8il8gcktLdXKdI=', start_index=4591)
Annotation(end_index=4910, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpIhkXHDBRrl5rJ38-gbubAHHgZtyvEI2nPCVUrPGwWswUApSiBSiVg3VLwvKR7G1jmJ1mRzE1kJaHV6npTj6KAfndqYgDR51kTw_NuMVyu3a-csY4q67gz_qJldHMtalR6hhZtpI=', start_index=4896)
Annotation(end_index=4910, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0uYuuU8J1m3TDQPLMdQaLfU67R0Abeg2TZCvGCRfQKUJdyCZyILm0Yes7MAg2zOl1oQ3XW5bZe7pb_jSKtQKLmxJaVQqEfswtJ85q2je9EcpBSdK6jrXjWK5YbM0wSKHdqYwpjJhNqYmqDb0y4LDA6hougf6-yNToYs-jxmWA1x6M5Q==', start_index=4896)
Annotation(end_index=5291, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfkteLzEx1DXk_U5uWUtluzWku_KsQYFjmC9MKdkofdkF-SYjBD7pu5-aeOKQ9qttSXrhGwJAlfsT5XmdQYe9enZIoL7y-xT2hMwObC_gO7N-gE7QVOWYIGyr7xmGGVA8Il0c9b9nAgjBhDEobUK8Z9lJGut1OtJqYRs2nsl84LGOukxMxVYdLC6qptdvnDoZPo19JryW__js-x_cMohlSUV2KnAE8l5SADIgpbKoLujZgyF4tEdw05_nnBtrMjmsByg==', start_index=5275)
Annotation(end_index=5291, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfIyYu-bmJSONZ6wa4IL5eDhirP5DDZ0QyEghhzG211UlkoXCSpwOrgB2yR-2suSDlwc30ghTZ3wH2-uUMw3zSiKagmzFL_xWPX4KGhsbtA31QIj9AuQaZBwBMbvjb', start_index=5275)
Annotation(end_index=5291, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK8xzsQ8j8u7PnQ7RmxqLoWecE7E_7lbTSwL-8bAEoYikFVO0pSmA8FmSKzsVd4Imh8ibWnFkXJM1fKusttMj_P89q0bsr26ad2ymLTr6m8AKff8il8gcktLdXKdI=', start_index=5275)
Annotation(end_index=5576, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEph0-bLtpQiddTZ5-EgTtwKvtTUZndQWGK0ai-rCEuAOyW9Q1_fJQXOVhNQDYfGKs8B-W6KnQ95ks22muZGG52ankGi2QZ894kZZ56z2aMSdNgF6EK0oZDMCRzRMJ93Lc7NF9xZXADLMxNv-uPaPvMkt_awHiNme_F30kchIkQemAYw3JYwiVqTT2CuT22EWD5LoEqzmQ2k6yLdxffI4h-3HTWn07M5SNHxOwtFo8q6CmXx04G-cyjgtrexyprzdYE7Ht1MNLHZkQwLPA99e8_YrfDxp8P1TtIbYCC', start_index=5564)
Annotation(end_index=5576, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK8xzsQ8j8u7PnQ7RmxqLoWecE7E_7lbTSwL-8bAEoYikFVO0pSmA8FmSKzsVd4Imh8ibWnFkXJM1fKusttMj_P89q0bsr26ad2ymLTr6m8AKff8il8gcktLdXKdI=', start_index=5564)
Annotation(end_index=6086, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8K-6SdPRNGlx9tAlZ2NuDjh1vCpZDogu5rWJEqefgE4lcHtX3sLHsRONCKh3Odiby0XWvrpWScNp6WSHkspW5wX1Ng9Q-oQXsxGS-RP2xjju6xAm6hlQ9TqCBcXqH', start_index=6073)
Annotation(end_index=6086, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFx-tLEfu5eoSeMhw2moj7KO9s1NspzWdxNAhpOBBUxfg_kJHawFcuxxyjFTREiRfoxdcwlc-03nNhxg_HaFrzo9aRtuvJlB74HKa2FJmktptZayWvRswquYvqHWhcIEIIOyYmFMLXMg92FzHqnfdPi5NbO4Iom7IC1JHqUD9P00lbmXKfWT3mSd6U=', start_index=6073)
Annotation(end_index=6418, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFElkDCIHUvqpY_C1ijieuy0H4wS7W9wnKiCmS_K7EByvrMfU2z40pKtjLB0a3xSr2T039CeVPX83Iladrd-qUX2kmErYJbPWl6tvdsSTNQNsi4YUJW1rPc-Mg1R-pnxHynu7qnhHLyEwr5Q1QBbyQgNhtwlrb4r5m3HBiHpw==', start_index=6404)
Annotation(end_index=6418, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfYwzlPBMUmiuAf7yx24lDY23olNYI7jhc1teg4jspASOfd3owj2cLxSpZAlQQyjCNSxzPdfiT5OebAEmKTzzi4r_knzkTEtpOIqExDk61aAyB9amaJ5e1T_jwrO-W8qw6Sxy79rQq', start_index=6404)
Annotation(end_index=6703, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfkteLzEx1DXk_U5uWUtluzWku_KsQYFjmC9MKdkofdkF-SYjBD7pu5-aeOKQ9qttSXrhGwJAlfsT5XmdQYe9enZIoL7y-xT2hMwObC_gO7N-gE7QVOWYIGyr7xmGGVA8Il0c9b9nAgjBhDEobUK8Z9lJGut1OtJqYRs2nsl84LGOukxMxVYdLC6qptdvnDoZPo19JryW__js-x_cMohlSUV2KnAE8l5SADIgpbKoLujZgyF4tEdw05_nnBtrMjmsByg==', start_index=6685)
Annotation(end_index=6703, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHprrnzStcrKLSDhS_OXD-WaV30WQ_PWhdlC5iAfvgMTt-2I-LmUZ-Ac9TXkawNk4Hadp7E6YNt2Ei36zpxdMevnIGeoebJnX1zDdTgL1ndDD1dldxn7Tqp0BPn9YYv-PDQLzGi5QcP', start_index=6685)
Annotation(end_index=6703, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuzjCZeK6NRvFUc9lzyKtp7WTeYJrGRprwl5o3wH82nLYdxJuJ5lNQuTT4Qgk6ctlnzBb-S73uAPuHJWwpGyDf5ZlAGOPITc3bgdQifcY2YDZqltqoqNiSgBlqsNZ47UsWzWpCo-WnHPNuSQ9705EELgVwgb-l', start_index=6685)
Annotation(end_index=7076, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETtLDIhE_McKjhPEYT08srjuC7yXHGMmbqaLqp1LQIiMkx9VqIcHorXo5qJScvqBkDXVIgglEkpfZggctBLeqxJqT9v3x1KnjRS55RyAMIKgTAMob7eMIkG7PlmxLWo12CvHeKeZXG0yazrQ==', start_index=7059)
Annotation(end_index=7076, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8K-6SdPRNGlx9tAlZ2NuDjh1vCpZDogu5rWJEqefgE4lcHtX3sLHsRONCKh3Odiby0XWvrpWScNp6WSHkspW5wX1Ng9Q-oQXsxGS-RP2xjju6xAm6hlQ9TqCBcXqH', start_index=7059)
Annotation(end_index=7076, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHprrnzStcrKLSDhS_OXD-WaV30WQ_PWhdlC5iAfvgMTt-2I-LmUZ-Ac9TXkawNk4Hadp7E6YNt2Ei36zpxdMevnIGeoebJnX1zDdTgL1ndDD1dldxn7Tqp0BPn9YYv-PDQLzGi5QcP', start_index=7059)
Annotation(end_index=7272, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8K-6SdPRNGlx9tAlZ2NuDjh1vCpZDogu5rWJEqefgE4lcHtX3sLHsRONCKh3Odiby0XWvrpWScNp6WSHkspW5wX1Ng9Q-oQXsxGS-RP2xjju6xAm6hlQ9TqCBcXqH', start_index=7259)
Annotation(end_index=7272, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfYwzlPBMUmiuAf7yx24lDY23olNYI7jhc1teg4jspASOfd3owj2cLxSpZAlQQyjCNSxzPdfiT5OebAEmKTzzi4r_knzkTEtpOIqExDk61aAyB9amaJ5e1T_jwrO-W8qw6Sxy79rQq', start_index=7259)
Annotation(end_index=7451, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpXucEhyfgsDRfkfzHjwOCuansQGZQUnmzIozQj1pC4874tmqeMP_SsxI0wBwPBjOyErsD1FPX6IF0pp0sgwP-yxgUzMDIJ9ZY9j-urzP7L6qkE01q6gx-1Q0DC8c-Ql5adVT6zU457A==', start_index=7433)
Annotation(end_index=7451, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFx-tLEfu5eoSeMhw2moj7KO9s1NspzWdxNAhpOBBUxfg_kJHawFcuxxyjFTREiRfoxdcwlc-03nNhxg_HaFrzo9aRtuvJlB74HKa2FJmktptZayWvRswquYvqHWhcIEIIOyYmFMLXMg92FzHqnfdPi5NbO4Iom7IC1JHqUD9P00lbmXKfWT3mSd6U=', start_index=7433)
Annotation(end_index=7451, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfYwzlPBMUmiuAf7yx24lDY23olNYI7jhc1teg4jspASOfd3owj2cLxSpZAlQQyjCNSxzPdfiT5OebAEmKTzzi4r_knzkTEtpOIqExDk61aAyB9amaJ5e1T_jwrO-W8qw6Sxy79rQq', start_index=7433)
Annotation(end_index=7922, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETtLDIhE_McKjhPEYT08srjuC7yXHGMmbqaLqp1LQIiMkx9VqIcHorXo5qJScvqBkDXVIgglEkpfZggctBLeqxJqT9v3x1KnjRS55RyAMIKgTAMob7eMIkG7PlmxLWo12CvHeKeZXG0yazrQ==', start_index=7905)
Annotation(end_index=7922, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfkteLzEx1DXk_U5uWUtluzWku_KsQYFjmC9MKdkofdkF-SYjBD7pu5-aeOKQ9qttSXrhGwJAlfsT5XmdQYe9enZIoL7y-xT2hMwObC_gO7N-gE7QVOWYIGyr7xmGGVA8Il0c9b9nAgjBhDEobUK8Z9lJGut1OtJqYRs2nsl84LGOukxMxVYdLC6qptdvnDoZPo19JryW__js-x_cMohlSUV2KnAE8l5SADIgpbKoLujZgyF4tEdw05_nnBtrMjmsByg==', start_index=7905)
Annotation(end_index=7922, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfIyYu-bmJSONZ6wa4IL5eDhirP5DDZ0QyEghhzG211UlkoXCSpwOrgB2yR-2suSDlwc30ghTZ3wH2-uUMw3zSiKagmzFL_xWPX4KGhsbtA31QIj9AuQaZBwBMbvjb', start_index=7905)
Annotation(end_index=8169, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQET_Av-FQPgNisF6ExnmzACHxMCglHY2xBw_eebt077UEaCzGuhh_oLrK-Qq0fvJAAWZTzBIPaZ11lerOP-Ng-215G0TcPCTX8CqGwBumrOASWOjHjKjVJzwcBDxFd05TVFzUINiI-dYE5HPugnXNdNTVxq117lrKfBoEzoFVYYBo46H0zw6hrj7JpxoW6TtRsl6_virCr16cn3kS9v7jqKKEY4TIBWq-GBBiD6moLwuKWeKJfGrhBHcxeMFjrrjTIzFuFSV7XqMYpRnWOD', start_index=8151)
Annotation(end_index=8169, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgRXiQnz9a6i6iZ1riBef5fLRbHsrXqJlAaBJj6kUX8RtJCaWn-SLpmPgC0chbLsNtkSdHIks3hR6rdO2rO6ZaK5fgC7vSvqcT68T1K1361qV8rEPWev2JMhTPmaSE0RpJhsH9ohM=', start_index=8151)
Annotation(end_index=8169, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHprrnzStcrKLSDhS_OXD-WaV30WQ_PWhdlC5iAfvgMTt-2I-LmUZ-Ac9TXkawNk4Hadp7E6YNt2Ei36zpxdMevnIGeoebJnX1zDdTgL1ndDD1dldxn7Tqp0BPn9YYv-PDQLzGi5QcP', start_index=8151)
Annotation(end_index=8391, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESa6grsgjfcUjT4Wm5J3mAx1uKN-8vKreTGLHJhhHItVZicpEIhO39GYc0IXCDG48_LqOOwgWjnvCRwnHa1RUvuzNg2wrRsBxeGlIe7aW2G7zDKdCQC5YZ9QGUNud6j5ZeRqnfGbF73AiO3SX4jn0owUYd84NXb1zwBRtrGbdpHA==', start_index=8377)
Annotation(end_index=8391, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETtLDIhE_McKjhPEYT08srjuC7yXHGMmbqaLqp1LQIiMkx9VqIcHorXo5qJScvqBkDXVIgglEkpfZggctBLeqxJqT9v3x1KnjRS55RyAMIKgTAMob7eMIkG7PlmxLWo12CvHeKeZXG0yazrQ==', start_index=8377)
Annotation(end_index=8709, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESa6grsgjfcUjT4Wm5J3mAx1uKN-8vKreTGLHJhhHItVZicpEIhO39GYc0IXCDG48_LqOOwgWjnvCRwnHa1RUvuzNg2wrRsBxeGlIe7aW2G7zDKdCQC5YZ9QGUNud6j5ZeRqnfGbF73AiO3SX4jn0owUYd84NXb1zwBRtrGbdpHA==', start_index=8695)
Annotation(end_index=8709, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETtLDIhE_McKjhPEYT08srjuC7yXHGMmbqaLqp1LQIiMkx9VqIcHorXo5qJScvqBkDXVIgglEkpfZggctBLeqxJqT9v3x1KnjRS55RyAMIKgTAMob7eMIkG7PlmxLWo12CvHeKeZXG0yazrQ==', start_index=8695)
Annotation(end_index=8878, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETtLDIhE_McKjhPEYT08srjuC7yXHGMmbqaLqp1LQIiMkx9VqIcHorXo5qJScvqBkDXVIgglEkpfZggctBLeqxJqT9v3x1KnjRS55RyAMIKgTAMob7eMIkG7PlmxLWo12CvHeKeZXG0yazrQ==', start_index=8868)
Annotation(end_index=9440, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGo9uDfeL8CH1XPK00sLi3gYu3p8eqDJqYUPyp1VZUmSOX5Bzf-odgXriQpfTjZQQsXXTXbfHleQR7ZUzCaT9C6Ss9Dg0KqC5mBvcG-ZXJsgRvIxJthfKJXY41Cg==', start_index=9418)
Annotation(end_index=9440, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtpe3VDgYnS8W7ISsuSn58x5dlDqUQod9fPqlYTUanfj7eSTbhx352bYO-Tc7R93Yw_HcVimtu2i7aUVeMs-UpRERZFWDWBaZZSLYIH_K2VkjbGgYA4J-J22F99hQ=', start_index=9418)
Annotation(end_index=9440, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0uYuuU8J1m3TDQPLMdQaLfU67R0Abeg2TZCvGCRfQKUJdyCZyILm0Yes7MAg2zOl1oQ3XW5bZe7pb_jSKtQKLmxJaVQqEfswtJ85q2je9EcpBSdK6jrXjWK5YbM0wSKHdqYwpjJhNqYmqDb0y4LDA6hougf6-yNToYs-jxmWA1x6M5Q==', start_index=9418)
Annotation(end_index=9440, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpk_XF1Bza4fGHRCJAFJlKcP4fvfQ_0lfqpW2h3VtnSpilb6hoGTmXJ5ZpBsfwHNZGZFFdye0u9XoVPZLfoZtOGxLCHJgm3ak9Ay8IbCoucRULsJaALyKstCZvYRepPxm5HEw2Jn4=', start_index=9418)
Annotation(end_index=9799, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGD_vDJkjXX70gUsIpAdU4MN0KG4DMIkbzC0D7eaRc8R7woc5Lt_Fj3cMCh1eDnWZWJ2_QQkB1UFjZx0QfM87Rb_anm9ykK9ujHpzzK3HfxQfUTMj3mir3KYsVjJ9w7VU5VUdBLblTCtiavlypRt4Oj62MEz949dH2lE2_Tel4819RiWPnJQ3lYsrPNaUsAFJGwttQlbeFPl3DF2SbGjbLyrX3EPnO2R6MBZhHvm0jvHWib-oo=', start_index=9781)
Annotation(end_index=9799, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGjP347VogiSeiIEQt2dn_ZmXivhXmdVSHUKLWcmgIufGEuaRefnO0Hf05rmZICzjFocyo6t7V_xLMvwYOkJKAY4HQBrZ1uR1BVk7-3pP_HYtCFW7aUX_Zf39TPRjZuVxVQM6ZOtt20Zx40qQnFjJ5hjFbtIjlU9zBATQPnqju5VrEAY5zV7CoA9OF5E9SrkRX-SGoV7FGFGeZEymXkNyMMAarmot3d4Hbda0uGKJiBGDw4SrjBuGvEyEge4U=', start_index=9781)
Annotation(end_index=9799, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmJy_VHBJVV0j74cWPVtkvLTWE1MhToe-nz4FiOe9xK4yTztckj3Sa2REbzYvraG6lICBjIGUhm70cqVnsrWzz6kXWUgPVvcdTybB8DOu9VKFsoF2VM8SyZPyXH8529tLqvO5w--iITTuptqBzEG3nQ_HtKT2TaLozRzem23RM9Svg2k6f2e5hhpPXU6XMKFOeo_Lq1Nox_yy8buw2Ur5GjS12D-yWarVX2OsO5HQr9b8pS96N-hUI7Nor168uh4GErpbS9x2ECkB7EUzI5Leg3mE2nkg=', start_index=9781)
Annotation(end_index=9990, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGo9uDfeL8CH1XPK00sLi3gYu3p8eqDJqYUPyp1VZUmSOX5Bzf-odgXriQpfTjZQQsXXTXbfHleQR7ZUzCaT9C6Ss9Dg0KqC5mBvcG-ZXJsgRvIxJthfKJXY41Cg==', start_index=9977)
Annotation(end_index=9990, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK8xzsQ8j8u7PnQ7RmxqLoWecE7E_7lbTSwL-8bAEoYikFVO0pSmA8FmSKzsVd4Imh8ibWnFkXJM1fKusttMj_P89q0bsr26ad2ymLTr6m8AKff8il8gcktLdXKdI=', start_index=9977)
Annotation(end_index=10251, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbLghkI0ztgUocVns5V517Tk0JM_EiBPN8ApdQLbM7AI1almqc8lhxmXHvs45XP6xJyMWFtw-8CIjurGzMLsbZeMnHxzXZNu0VMIw1Jm652SXOL7m2O2cRL-U_VTxdGSygBfZZjBuGEsr4fxNcOXDr-g65LPx6JytGMhg2zcNaL2P2L8JLJ-2XWAdTzntA0ldjRxreWxhfaSGjEaMw7A==', start_index=10230)
Annotation(end_index=10251, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0uYuuU8J1m3TDQPLMdQaLfU67R0Abeg2TZCvGCRfQKUJdyCZyILm0Yes7MAg2zOl1oQ3XW5bZe7pb_jSKtQKLmxJaVQqEfswtJ85q2je9EcpBSdK6jrXjWK5YbM0wSKHdqYwpjJhNqYmqDb0y4LDA6hougf6-yNToYs-jxmWA1x6M5Q==', start_index=10230)
Annotation(end_index=10251, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpk_XF1Bza4fGHRCJAFJlKcP4fvfQ_0lfqpW2h3VtnSpilb6hoGTmXJ5ZpBsfwHNZGZFFdye0u9XoVPZLfoZtOGxLCHJgm3ak9Ay8IbCoucRULsJaALyKstCZvYRepPxm5HEw2Jn4=', start_index=10230)
Annotation(end_index=10251, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHP4vFcFaS5O5_BrjJd71Ophk2OzlDoIDP7yNdurZXEVy-9TUGCG-UVYiTzas9HKFXXPHBiWZzo0jgAyalEeRncHdYw7-3a7NRXnJ64obSgE-UMVJK4V-fdaae_U-bCSLZdAZIXOQ8t', start_index=10230)
Annotation(end_index=10490, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHv5g6t_u4UwtUBx_xmR9CXE2e_EOHZYqXUjceKmIqJVMgukBZ2I2eGfAtxm_VX1Axy7cSdXkNlFTD2Z0ILmjfnVR2E4wAP9SGDw2JAOr1oGLgC_m-mHnuhN_3g-GCuHlK4Si2ltS1Cp5HXYs2nOkc9zdMr86ikEGKBRzn8rAuHd1Aa8L5uga9mbfjFuur0H8h2nGUw83jJoOoY6cHh_Rkqp4D3XLt8pY1zvh7q6iA4J-TjkA1KyvVhbgBvPMeCk7lCZEcVPm6zsJNOwUUIwL-xptUHQXVM14Jfw==', start_index=10476)
Annotation(end_index=10490, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpdFJk-vFvt9WPaoEf3eUWVnGohcTGtuKuZodQiE4Awj2jLCAjZn-ut5g20M6JebihnxU_wJQMIPwi-L7gKeJ2BXJnjhVF94ahXKrjCAXv4E4EbM4K-gTqD2fmFQbBfhHZizMw6MlScC-IHLYbPhXAeShRGcA4lVqxmpMBfO8BkkEEPIGBSR4apdRamLPCJgEmMaqB3W72Ni4El_tefvjCGWOWrgN0e9vbLUiPnPI_OKoUzHEKqQ==', start_index=10476)
Annotation(end_index=10808, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtpe3VDgYnS8W7ISsuSn58x5dlDqUQod9fPqlYTUanfj7eSTbhx352bYO-Tc7R93Yw_HcVimtu2i7aUVeMs-UpRERZFWDWBaZZSLYIH_K2VkjbGgYA4J-J22F99hQ=', start_index=10790)
Annotation(end_index=10808, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpk_XF1Bza4fGHRCJAFJlKcP4fvfQ_0lfqpW2h3VtnSpilb6hoGTmXJ5ZpBsfwHNZGZFFdye0u9XoVPZLfoZtOGxLCHJgm3ak9Ay8IbCoucRULsJaALyKstCZvYRepPxm5HEw2Jn4=', start_index=10790)
Annotation(end_index=10808, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEhRqoMkF0Yt9TRbZZ7ODvUIloKbjqGR2kNa5LdWaKtNPtP4JsYxAIae-gkAMUqTo5Y8ygIoIJ1EJnB50OtfzO32lpoPNWgwo6S-LW0YfOG_g4VdA13UEHGp0mNFxZ8BGX7ndh_yflhcTDoD8PuxC7ULkytfZKFdEinLhJ1aw6dkQ=', start_index=10790)
Annotation(end_index=11076, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpIhkXHDBRrl5rJ38-gbubAHHgZtyvEI2nPCVUrPGwWswUApSiBSiVg3VLwvKR7G1jmJ1mRzE1kJaHV6npTj6KAfndqYgDR51kTw_NuMVyu3a-csY4q67gz_qJldHMtalR6hhZtpI=', start_index=11063)
Annotation(end_index=11076, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuPzPyb2guZhMmHJvfTz3booaHDudiXn0ZMonHkXaTC3lYAWCht9H40qtauUWLgMf698p5SfPsR6r3AtOb68K7riU-Fs5NdzDR15fTF6q9pqALcEfUceVskmL4GR2RWelpIwgtmoVgcEMZ_dHXoxljExXu6y5Yl9dg7HZV4qtefS0yuXRrp9EUIGCb-ZqCgZ6C8w==', start_index=11063)
Annotation(end_index=11322, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuPzPyb2guZhMmHJvfTz3booaHDudiXn0ZMonHkXaTC3lYAWCht9H40qtauUWLgMf698p5SfPsR6r3AtOb68K7riU-Fs5NdzDR15fTF6q9pqALcEfUceVskmL4GR2RWelpIwgtmoVgcEMZ_dHXoxljExXu6y5Yl9dg7HZV4qtefS0yuXRrp9EUIGCb-ZqCgZ6C8w==', start_index=11309)
Annotation(end_index=11322, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpdFJk-vFvt9WPaoEf3eUWVnGohcTGtuKuZodQiE4Awj2jLCAjZn-ut5g20M6JebihnxU_wJQMIPwi-L7gKeJ2BXJnjhVF94ahXKrjCAXv4E4EbM4K-gTqD2fmFQbBfhHZizMw6MlScC-IHLYbPhXAeShRGcA4lVqxmpMBfO8BkkEEPIGBSR4apdRamLPCJgEmMaqB3W72Ni4El_tefvjCGWOWrgN0e9vbLUiPnPI_OKoUzHEKqQ==', start_index=11309)
Annotation(end_index=11564, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpIhkXHDBRrl5rJ38-gbubAHHgZtyvEI2nPCVUrPGwWswUApSiBSiVg3VLwvKR7G1jmJ1mRzE1kJaHV6npTj6KAfndqYgDR51kTw_NuMVyu3a-csY4q67gz_qJldHMtalR6hhZtpI=', start_index=11554)
Annotation(end_index=11752, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuPzPyb2guZhMmHJvfTz3booaHDudiXn0ZMonHkXaTC3lYAWCht9H40qtauUWLgMf698p5SfPsR6r3AtOb68K7riU-Fs5NdzDR15fTF6q9pqALcEfUceVskmL4GR2RWelpIwgtmoVgcEMZ_dHXoxljExXu6y5Yl9dg7HZV4qtefS0yuXRrp9EUIGCb-ZqCgZ6C8w==', start_index=11743)
Annotation(end_index=12126, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGo9uDfeL8CH1XPK00sLi3gYu3p8eqDJqYUPyp1VZUmSOX5Bzf-odgXriQpfTjZQQsXXTXbfHleQR7ZUzCaT9C6Ss9Dg0KqC5mBvcG-ZXJsgRvIxJthfKJXY41Cg==', start_index=12112)
Annotation(end_index=12126, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtpe3VDgYnS8W7ISsuSn58x5dlDqUQod9fPqlYTUanfj7eSTbhx352bYO-Tc7R93Yw_HcVimtu2i7aUVeMs-UpRERZFWDWBaZZSLYIH_K2VkjbGgYA4J-J22F99hQ=', start_index=12112)
Annotation(end_index=12307, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZG9lkYzETRg9PcjCwiJN0MacfQqNgHREH475Ezvg4sQvw-QrzlsrZ_5E5eZgTAbPOWxTpPhAfRhdF6TwP6K_QAL4EkEwQMVAKLX4Uhx459UWPM_ukVXwsver7zijomscTDyFsV-8UZzwZcpLHe68BeBpS', start_index=12293)
Annotation(end_index=12307, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtpe3VDgYnS8W7ISsuSn58x5dlDqUQod9fPqlYTUanfj7eSTbhx352bYO-Tc7R93Yw_HcVimtu2i7aUVeMs-UpRERZFWDWBaZZSLYIH_K2VkjbGgYA4J-J22F99hQ=', start_index=12293)
Annotation(end_index=12533, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGn24x2_KrMrbyq_C_eIwwyHfGXgkcs6OHIY_D4WGKXCmoBU8YE1ncZN3FIaycheDwOcC88g5O4f5bkHNKrKvN03ViwIS4_pSGQJaHnVmI9WFBHu9tJXmVcaqU=', start_index=12523)
Annotation(end_index=12773, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqKQWHa1SKkWlnDRGVx2nLugDY6PAI_5WGh3FpDH_Bejlhinz_rEvBHhQx68uIUFpd4_EFsdpzYLm-Ay3U3rkFQK1Ejk4w0SX-2lMliFfHZvk78MXtOCQaliOxnxmL_mWeVnn-E9_qER5Nw2ryGF1Hk444kAGoH7kg1ZD1zBjJYQvEkCxWT0tzXjDSehbSKrXBVtzN-D6ec9M9SSvJlg0OhaQB5aXj4Opw9MFLsm5wP4V8V0NzEuwzBrtjZndE2W4CIKhK1F_yZCyNurzMQKZJ2rfKInHMMlNHBe2f', start_index=12759)
Annotation(end_index=12773, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVcR4p4BPQCtn37-iLZfcNf5Uf64JcPUOzgcIEjSO1diOD18fuJ-w8uM_DJhkNpRT6oDr8LilLPqGF8TiHnpjPtRoh8Z6YtEiA_HtjiUibapYfXcdbFWnPGCBQNn8=', start_index=12759)
Annotation(end_index=13156, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqKQWHa1SKkWlnDRGVx2nLugDY6PAI_5WGh3FpDH_Bejlhinz_rEvBHhQx68uIUFpd4_EFsdpzYLm-Ay3U3rkFQK1Ejk4w0SX-2lMliFfHZvk78MXtOCQaliOxnxmL_mWeVnn-E9_qER5Nw2ryGF1Hk444kAGoH7kg1ZD1zBjJYQvEkCxWT0tzXjDSehbSKrXBVtzN-D6ec9M9SSvJlg0OhaQB5aXj4Opw9MFLsm5wP4V8V0NzEuwzBrtjZndE2W4CIKhK1F_yZCyNurzMQKZJ2rfKInHMMlNHBe2f', start_index=13146)
Annotation(end_index=13470, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVcR4p4BPQCtn37-iLZfcNf5Uf64JcPUOzgcIEjSO1diOD18fuJ-w8uM_DJhkNpRT6oDr8LilLPqGF8TiHnpjPtRoh8Z6YtEiA_HtjiUibapYfXcdbFWnPGCBQNn8=', start_index=13460)
Annotation(end_index=13816, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvBzgBxCbB5xKycdnbMFgzCXxm_4Fg4yEFdS62-Vz1VsmULnFmE1Qujre-ywkWEgQ_r1YCQcIXo7GBd6i1CkZxX2XQH9Ss578dHbCHCEdWdmo-uRtziSmE22st8gNLrBpe27OGvZgRLHZufS0tyW6cKCtJTRc4tEcoQlO3ngDCCAqDtsoKrL_C3AGlSxq2XZBZiDrI9mLa4ErUUi-O0hLQXpDGNU9MaXKVOZ0huvWF2cevp9_HalfCPyXhLUFRrD4J', start_index=13802)
Annotation(end_index=13816, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGW3YHBJqN1Qqy6yI-yksnZ98P64Z_YJ-nYTL4A1oNCYZvYRsz2Q8_TgsrGc8s529RwfDs9y4Mtc0GBR0Xv-iJ0tKerBE2u-E2stfXVwLQ1Tho7QosAP5QJm1av', start_index=13802)
Annotation(end_index=14069, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGW3YHBJqN1Qqy6yI-yksnZ98P64Z_YJ-nYTL4A1oNCYZvYRsz2Q8_TgsrGc8s529RwfDs9y4Mtc0GBR0Xv-iJ0tKerBE2u-E2stfXVwLQ1Tho7QosAP5QJm1av', start_index=14059)
Annotation(end_index=14554, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETtLDIhE_McKjhPEYT08srjuC7yXHGMmbqaLqp1LQIiMkx9VqIcHorXo5qJScvqBkDXVIgglEkpfZggctBLeqxJqT9v3x1KnjRS55RyAMIKgTAMob7eMIkG7PlmxLWo12CvHeKeZXG0yazrQ==', start_index=14540)
Annotation(end_index=14554, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHB1UbRw0mnLtB-yWcIbxjaHEzR9TBSYDD0g7E8QkSt9LnfrXeEKOroJ3TEawPy2Ut3lz8gRDQiGmPATRpSSd_hUMFG02vjAiUg4X7kmTgmz1It-EXnoh33_d_U1PhgQRCnHw3G-Cnb7S4v7IfNQmKgE8zm7epc-kCCL7o_2nka85dUBGjp_laV6KI=', start_index=14540)
Annotation(end_index=14652, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK8xzsQ8j8u7PnQ7RmxqLoWecE7E_7lbTSwL-8bAEoYikFVO0pSmA8FmSKzsVd4Imh8ibWnFkXJM1fKusttMj_P89q0bsr26ad2ymLTr6m8AKff8il8gcktLdXKdI=', start_index=14643)
Annotation(end_index=15023, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0uYuuU8J1m3TDQPLMdQaLfU67R0Abeg2TZCvGCRfQKUJdyCZyILm0Yes7MAg2zOl1oQ3XW5bZe7pb_jSKtQKLmxJaVQqEfswtJ85q2je9EcpBSdK6jrXjWK5YbM0wSKHdqYwpjJhNqYmqDb0y4LDA6hougf6-yNToYs-jxmWA1x6M5Q==', start_index=15009)
Annotation(end_index=15023, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrRq_I-KVMKKflWfvLlJudEGRhC30DiQF9pRApubTTEF1kis7pslkxe2RIKbpGRV3yeTYDaNGYOGxVXmfuBppU00bATEMEkWGuk3tx7rTjL1SJoMjPD4CBSBr9uOHiVsps4jH-CAxpMouisfe9fUsQC3ePHABQdQ==', start_index=15009)
Annotation(end_index=15561, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGtEVSot8lEYZFWjablFkDQmahbWti1tIDbnQonPTOUUvRRtD8VsJwpw5az55FxRGXfiM7Rkcng5E2KQIogU02dmv3XmcCixd6xoy0DHKjNcw63Y_4NXav7FJjrEoPoDWQ2xYdS-I=', start_index=15548)
Annotation(end_index=15561, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK8xzsQ8j8u7PnQ7RmxqLoWecE7E_7lbTSwL-8bAEoYikFVO0pSmA8FmSKzsVd4Imh8ibWnFkXJM1fKusttMj_P89q0bsr26ad2ymLTr6m8AKff8il8gcktLdXKdI=', start_index=15548)
Annotation(end_index=15786, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1J_gcwb-jrFsc5AYz7NEZ0EEI_g-08rml7pdlQOHexmei1KQb0wucTBIyJi42GC0e3CdHsdMAlkx-w0GzwU0E-r2OSUdbTIzg70PYXk78SkKtMb5mq05XOFJqwXWdXjSFkBBf2V5yd664gTaHdue45ibnsdWyICqW3aqRZxlI4C7EjwRdYqsOQY-383QiHDGguMEDAYLXx4LVNxGXKRkAu8Uwn83kBU2I6bD1kDgcDQDPBvKseK3_JsIPPqaRIOYGoZ9CaQNI_0lOQJOTBLd9qAIr6Z6xLY6_q_x5', start_index=15774)
Annotation(end_index=15786, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK8xzsQ8j8u7PnQ7RmxqLoWecE7E_7lbTSwL-8bAEoYikFVO0pSmA8FmSKzsVd4Imh8ibWnFkXJM1fKusttMj_P89q0bsr26ad2ymLTr6m8AKff8il8gcktLdXKdI=', start_index=15774)
Annotation(end_index=15959, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkgAt-zeLn60q5v5C1kLzMeCP6lpQYu9kgfI0qNyZEonR_nktl-IDRYigkX3GtA_LBrlq0Pz4J0nCP7-M1r0MtVYHVAbPcgtI_QFuqqGKEF3OgZQCzpERDXEq8Iswi4n-vzX7ZC_0=', start_index=15949)
Annotation(end_index=16249, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8K-6SdPRNGlx9tAlZ2NuDjh1vCpZDogu5rWJEqefgE4lcHtX3sLHsRONCKh3Odiby0XWvrpWScNp6WSHkspW5wX1Ng9Q-oQXsxGS-RP2xjju6xAm6hlQ9TqCBcXqH', start_index=16236)
Annotation(end_index=16249, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfYwzlPBMUmiuAf7yx24lDY23olNYI7jhc1teg4jspASOfd3owj2cLxSpZAlQQyjCNSxzPdfiT5OebAEmKTzzi4r_knzkTEtpOIqExDk61aAyB9amaJ5e1T_jwrO-W8qw6Sxy79rQq', start_index=16236)
Annotation(end_index=16450, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrB7HKiszqAIsM7tbWfJsEdCSfWujQwBwQFOP6M8bTulD66hCPD6T6DFQZgU5ZvIbFO0G-pWV-PcSsA34I5E-ctHfoN2a1bm9UH8BffCnVDoM_6zT-O8sH3FmRRDWPgjuFlwrkNsvXM2qo84soQUCaSb5rvnO8Tgy0ZhAdi1vTcg==', start_index=16440)
Annotation(end_index=16841, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEedXG6Zvk_tf2x3S3R7EBGMravPZoOnLag9ZkXWXXi06PhLQP3tl_a3pKxRy6aEBvYQgX8hSWbq751ugXpSPbhDa-RBVBEEgCuR9gxaP5BS9ln17X2s80CidVEdMDWZ9f9LdMMec8=', start_index=16827)
Annotation(end_index=16841, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrRq_I-KVMKKflWfvLlJudEGRhC30DiQF9pRApubTTEF1kis7pslkxe2RIKbpGRV3yeTYDaNGYOGxVXmfuBppU00bATEMEkWGuk3tx7rTjL1SJoMjPD4CBSBr9uOHiVsps4jH-CAxpMouisfe9fUsQC3ePHABQdQ==', start_index=16827)
Annotation(end_index=17186, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETtLDIhE_McKjhPEYT08srjuC7yXHGMmbqaLqp1LQIiMkx9VqIcHorXo5qJScvqBkDXVIgglEkpfZggctBLeqxJqT9v3x1KnjRS55RyAMIKgTAMob7eMIkG7PlmxLWo12CvHeKeZXG0yazrQ==', start_index=17172)
Annotation(end_index=17186, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHB1UbRw0mnLtB-yWcIbxjaHEzR9TBSYDD0g7E8QkSt9LnfrXeEKOroJ3TEawPy2Ut3lz8gRDQiGmPATRpSSd_hUMFG02vjAiUg4X7kmTgmz1It-EXnoh33_d_U1PhgQRCnHw3G-Cnb7S4v7IfNQmKgE8zm7epc-kCCL7o_2nka85dUBGjp_laV6KI=', start_index=17172)
Annotation(end_index=17465, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDUVFsDCnY0fOvL4CLIqcaYkPg3eAPNjHCQytd_c2HqmKbuvReQ6arBS11RlKDphuu6nfBmdoqyDjWSmcRCs-1vLqAt_iEON9_ANvPFE-irmLAmwwep0VQQwwIbnSf-3PTyFUkEevsxCxpcKSRWR5V4HqP5T5_9rBdiC9573JvUhGOYVB1Z6JLU4Um2rKlGrSy14zq22cZFpZCnqPEDhSbzHce6Oq45eptLUMHhphOp83JWF1LurCZVOidp59YZxTaCf1aYjdHZp2ttEGcSALzM7t9onfM', start_index=17455)
Annotation(end_index=17746, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxrws9afwXY11XbvbkCoxUmbJvNE2DT9Qg4VKBdijKuVrR3Zod2GCTU3xaCzsUg7LuDk8fGxKp47Lwz-LW7DN9pEHWIwb6DHiKRqBZN3epG6WADckXrW2wGbNZZQsg9N-vo8EzTtQ=', start_index=17732)
Annotation(end_index=17746, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsaFwYhhfNUH0hA2HRVjC5AFq1YG3raM7_RJW0S6A_gXspIGJaO9C_DruH_qZEneav2fisYLyywnJ_eY0foXtn_h2vc7BNp4M2NtarQ53Eevfh8mLiWlC5YEliVc8PuZd0yPbi8vDBQmpeJbszl-IaCo3Vj7pWQR8Q8NoV', start_index=17732)
Annotation(end_index=19030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK8xzsQ8j8u7PnQ7RmxqLoWecE7E_7lbTSwL-8bAEoYikFVO0pSmA8FmSKzsVd4Imh8ibWnFkXJM1fKusttMj_P89q0bsr26ad2ymLTr6m8AKff8il8gcktLdXKdI=', start_index=19021)
Annotation(end_index=19142, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTCJcxgLH3XNBxUnBVc59Ne7l4E45SSrYj7kKQ-zTvLX6rANHSSPQjKFAluqQsctABl6RnfJcMhKl--8hm4xQB_w5rVfXqyv2mTboIW6oVMpNYgY59YoMPZCH1dI644ISZ81KpFuwwRYkABbC1eexMTwhSb3EE60UaNhBcUKAwN411Nbk=', start_index=19132)
Annotation(end_index=19233, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEX68WDnJ3GKoW-cpfw0rdJbkn8rV72OtPrYwnR1HazUFKHUDS0llIlC79ThIHK6r01RvgNBQtwMgPFZvS8vvhCSp2_DlJX7PlMd4WNt-DNchUj2KkexDJCN5Jj_6-aHY_RvQ==', start_index=19224)
Annotation(end_index=19313, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkgAt-zeLn60q5v5C1kLzMeCP6lpQYu9kgfI0qNyZEonR_nktl-IDRYigkX3GtA_LBrlq0Pz4J0nCP7-M1r0MtVYHVAbPcgtI_QFuqqGKEF3OgZQCzpERDXEq8Iswi4n-vzX7ZC_0=', start_index=19303)
Annotation(end_index=19375, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPoiS6-pvBZ092rjLs6f2Pq5NDUcpKQrTtxxwmH_bksodRyLtUYzd4ayAI-DkcegkZV5epImUP7LS6rip6TqsRPMFAxuEEC4g5wyAXu3rSFz9rrVMy-NW3gCpYcmy_GOzNSwp-trRxT6JwQPtMrg3mIDMNGzkURBq1xj-R5rs807DsHFl0bcNGw0VPhwG9feYy-KlNgNyHQk30bNoW4UTuMNaqjMvkqdYTws_weYetvCB7KJQnWx2FSNIrT1wI_m2NNTWj7GhUu6nCAC7Nn4SIeIicmOuNXhJwytLVTA==', start_index=19365)
Annotation(end_index=19453, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHprrnzStcrKLSDhS_OXD-WaV30WQ_PWhdlC5iAfvgMTt-2I-LmUZ-Ac9TXkawNk4Hadp7E6YNt2Ei36zpxdMevnIGeoebJnX1zDdTgL1ndDD1dldxn7Tqp0BPn9YYv-PDQLzGi5QcP', start_index=19443)
Annotation(end_index=19522, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuzjCZeK6NRvFUc9lzyKtp7WTeYJrGRprwl5o3wH82nLYdxJuJ5lNQuTT4Qgk6ctlnzBb-S73uAPuHJWwpGyDf5ZlAGOPITc3bgdQifcY2YDZqltqoqNiSgBlqsNZ47UsWzWpCo-WnHPNuSQ9705EELgVwgb-l', start_index=19512)
Annotation(end_index=19577, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgRXiQnz9a6i6iZ1riBef5fLRbHsrXqJlAaBJj6kUX8RtJCaWn-SLpmPgC0chbLsNtkSdHIks3hR6rdO2rO6ZaK5fgC7vSvqcT68T1K1361qV8rEPWev2JMhTPmaSE0RpJhsH9ohM=', start_index=19567)
Annotation(end_index=19654, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfkteLzEx1DXk_U5uWUtluzWku_KsQYFjmC9MKdkofdkF-SYjBD7pu5-aeOKQ9qttSXrhGwJAlfsT5XmdQYe9enZIoL7y-xT2hMwObC_gO7N-gE7QVOWYIGyr7xmGGVA8Il0c9b9nAgjBhDEobUK8Z9lJGut1OtJqYRs2nsl84LGOukxMxVYdLC6qptdvnDoZPo19JryW__js-x_cMohlSUV2KnAE8l5SADIgpbKoLujZgyF4tEdw05_nnBtrMjmsByg==', start_index=19644)
Annotation(end_index=19732, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFx-tLEfu5eoSeMhw2moj7KO9s1NspzWdxNAhpOBBUxfg_kJHawFcuxxyjFTREiRfoxdcwlc-03nNhxg_HaFrzo9aRtuvJlB74HKa2FJmktptZayWvRswquYvqHWhcIEIIOyYmFMLXMg92FzHqnfdPi5NbO4Iom7IC1JHqUD9P00lbmXKfWT3mSd6U=', start_index=19722)
Annotation(end_index=19814, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8K-6SdPRNGlx9tAlZ2NuDjh1vCpZDogu5rWJEqefgE4lcHtX3sLHsRONCKh3Odiby0XWvrpWScNp6WSHkspW5wX1Ng9Q-oQXsxGS-RP2xjju6xAm6hlQ9TqCBcXqH', start_index=19805)
Annotation(end_index=19888, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpXucEhyfgsDRfkfzHjwOCuansQGZQUnmzIozQj1pC4874tmqeMP_SsxI0wBwPBjOyErsD1FPX6IF0pp0sgwP-yxgUzMDIJ9ZY9j-urzP7L6qkE01q6gx-1Q0DC8c-Ql5adVT6zU457A==', start_index=19878)
Annotation(end_index=19970, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFElkDCIHUvqpY_C1ijieuy0H4wS7W9wnKiCmS_K7EByvrMfU2z40pKtjLB0a3xSr2T039CeVPX83Iladrd-qUX2kmErYJbPWl6tvdsSTNQNsi4YUJW1rPc-Mg1R-pnxHynu7qnhHLyEwr5Q1QBbyQgNhtwlrb4r5m3HBiHpw==', start_index=19960)
Annotation(end_index=20034, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrRq_I-KVMKKflWfvLlJudEGRhC30DiQF9pRApubTTEF1kis7pslkxe2RIKbpGRV3yeTYDaNGYOGxVXmfuBppU00bATEMEkWGuk3tx7rTjL1SJoMjPD4CBSBr9uOHiVsps4jH-CAxpMouisfe9fUsQC3ePHABQdQ==', start_index=20024)
Annotation(end_index=20114, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1J_gcwb-jrFsc5AYz7NEZ0EEI_g-08rml7pdlQOHexmei1KQb0wucTBIyJi42GC0e3CdHsdMAlkx-w0GzwU0E-r2OSUdbTIzg70PYXk78SkKtMb5mq05XOFJqwXWdXjSFkBBf2V5yd664gTaHdue45ibnsdWyICqW3aqRZxlI4C7EjwRdYqsOQY-383QiHDGguMEDAYLXx4LVNxGXKRkAu8Uwn83kBU2I6bD1kDgcDQDPBvKseK3_JsIPPqaRIOYGoZ9CaQNI_0lOQJOTBLd9qAIr6Z6xLY6_q_x5', start_index=20105)
Annotation(end_index=20204, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbLghkI0ztgUocVns5V517Tk0JM_EiBPN8ApdQLbM7AI1almqc8lhxmXHvs45XP6xJyMWFtw-8CIjurGzMLsbZeMnHxzXZNu0VMIw1Jm652SXOL7m2O2cRL-U_VTxdGSygBfZZjBuGEsr4fxNcOXDr-g65LPx6JytGMhg2zcNaL2P2L8JLJ-2XWAdTzntA0ldjRxreWxhfaSGjEaMw7A==', start_index=20195)
Annotation(end_index=20265, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtpe3VDgYnS8W7ISsuSn58x5dlDqUQod9fPqlYTUanfj7eSTbhx352bYO-Tc7R93Yw_HcVimtu2i7aUVeMs-UpRERZFWDWBaZZSLYIH_K2VkjbGgYA4J-J22F99hQ=', start_index=20255)
Annotation(end_index=20338, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK8xzsQ8j8u7PnQ7RmxqLoWecE7E_7lbTSwL-8bAEoYikFVO0pSmA8FmSKzsVd4Imh8ibWnFkXJM1fKusttMj_P89q0bsr26ad2ymLTr6m8AKff8il8gcktLdXKdI=', start_index=20329)
Annotation(end_index=20405, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0uYuuU8J1m3TDQPLMdQaLfU67R0Abeg2TZCvGCRfQKUJdyCZyILm0Yes7MAg2zOl1oQ3XW5bZe7pb_jSKtQKLmxJaVQqEfswtJ85q2je9EcpBSdK6jrXjWK5YbM0wSKHdqYwpjJhNqYmqDb0y4LDA6hougf6-yNToYs-jxmWA1x6M5Q==', start_index=20395)
Annotation(end_index=20477, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGn24x2_KrMrbyq_C_eIwwyHfGXgkcs6OHIY_D4WGKXCmoBU8YE1ncZN3FIaycheDwOcC88g5O4f5bkHNKrKvN03ViwIS4_pSGQJaHnVmI9WFBHu9tJXmVcaqU=', start_index=20467)
Annotation(end_index=20547, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpk_XF1Bza4fGHRCJAFJlKcP4fvfQ_0lfqpW2h3VtnSpilb6hoGTmXJ5ZpBsfwHNZGZFFdye0u9XoVPZLfoZtOGxLCHJgm3ak9Ay8IbCoucRULsJaALyKstCZvYRepPxm5HEw2Jn4=', start_index=20537)
Annotation(end_index=20609, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuPzPyb2guZhMmHJvfTz3booaHDudiXn0ZMonHkXaTC3lYAWCht9H40qtauUWLgMf698p5SfPsR6r3AtOb68K7riU-Fs5NdzDR15fTF6q9pqALcEfUceVskmL4GR2RWelpIwgtmoVgcEMZ_dHXoxljExXu6y5Yl9dg7HZV4qtefS0yuXRrp9EUIGCb-ZqCgZ6C8w==', start_index=20600)
Annotation(end_index=20677, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpdFJk-vFvt9WPaoEf3eUWVnGohcTGtuKuZodQiE4Awj2jLCAjZn-ut5g20M6JebihnxU_wJQMIPwi-L7gKeJ2BXJnjhVF94ahXKrjCAXv4E4EbM4K-gTqD2fmFQbBfhHZizMw6MlScC-IHLYbPhXAeShRGcA4lVqxmpMBfO8BkkEEPIGBSR4apdRamLPCJgEmMaqB3W72Ni4El_tefvjCGWOWrgN0e9vbLUiPnPI_OKoUzHEKqQ==', start_index=20667)
Annotation(end_index=20756, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVcR4p4BPQCtn37-iLZfcNf5Uf64JcPUOzgcIEjSO1diOD18fuJ-w8uM_DJhkNpRT6oDr8LilLPqGF8TiHnpjPtRoh8Z6YtEiA_HtjiUibapYfXcdbFWnPGCBQNn8=', start_index=20746)
Annotation(end_index=20834, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGo9uDfeL8CH1XPK00sLi3gYu3p8eqDJqYUPyp1VZUmSOX5Bzf-odgXriQpfTjZQQsXXTXbfHleQR7ZUzCaT9C6Ss9Dg0KqC5mBvcG-ZXJsgRvIxJthfKJXY41Cg==', start_index=20824)
Annotation(end_index=20898, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGjP347VogiSeiIEQt2dn_ZmXivhXmdVSHUKLWcmgIufGEuaRefnO0Hf05rmZICzjFocyo6t7V_xLMvwYOkJKAY4HQBrZ1uR1BVk7-3pP_HYtCFW7aUX_Zf39TPRjZuVxVQM6ZOtt20Zx40qQnFjJ5hjFbtIjlU9zBATQPnqju5VrEAY5zV7CoA9OF5E9SrkRX-SGoV7FGFGeZEymXkNyMMAarmot3d4Hbda0uGKJiBGDw4SrjBuGvEyEge4U=', start_index=20888)
Annotation(end_index=20988, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfYwzlPBMUmiuAf7yx24lDY23olNYI7jhc1teg4jspASOfd3owj2cLxSpZAlQQyjCNSxzPdfiT5OebAEmKTzzi4r_knzkTEtpOIqExDk61aAyB9amaJ5e1T_jwrO-W8qw6Sxy79rQq', start_index=20978)
Annotation(end_index=21057, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfIyYu-bmJSONZ6wa4IL5eDhirP5DDZ0QyEghhzG211UlkoXCSpwOrgB2yR-2suSDlwc30ghTZ3wH2-uUMw3zSiKagmzFL_xWPX4KGhsbtA31QIj9AuQaZBwBMbvjb', start_index=21048)
Annotation(end_index=21123, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpIhkXHDBRrl5rJ38-gbubAHHgZtyvEI2nPCVUrPGwWswUApSiBSiVg3VLwvKR7G1jmJ1mRzE1kJaHV6npTj6KAfndqYgDR51kTw_NuMVyu3a-csY4q67gz_qJldHMtalR6hhZtpI=', start_index=21113)
Annotation(end_index=21198, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETtLDIhE_McKjhPEYT08srjuC7yXHGMmbqaLqp1LQIiMkx9VqIcHorXo5qJScvqBkDXVIgglEkpfZggctBLeqxJqT9v3x1KnjRS55RyAMIKgTAMob7eMIkG7PlmxLWo12CvHeKeZXG0yazrQ==', start_index=21188)
Annotation(end_index=21264, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESa6grsgjfcUjT4Wm5J3mAx1uKN-8vKreTGLHJhhHItVZicpEIhO39GYc0IXCDG48_LqOOwgWjnvCRwnHa1RUvuzNg2wrRsBxeGlIe7aW2G7zDKdCQC5YZ9QGUNud6j5ZeRqnfGbF73AiO3SX4jn0owUYd84NXb1zwBRtrGbdpHA==', start_index=21254)
Annotation(end_index=21325, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHB1UbRw0mnLtB-yWcIbxjaHEzR9TBSYDD0g7E8QkSt9LnfrXeEKOroJ3TEawPy2Ut3lz8gRDQiGmPATRpSSd_hUMFG02vjAiUg4X7kmTgmz1It-EXnoh33_d_U1PhgQRCnHw3G-Cnb7S4v7IfNQmKgE8zm7epc-kCCL7o_2nka85dUBGjp_laV6KI=', start_index=21315)

## Sources
