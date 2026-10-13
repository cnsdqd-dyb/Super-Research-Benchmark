# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 362976f1 | **Time:** 332.19s | **Cost:** $1.48599
--------------------------------------------------------------------------------

# Optimal Porosity Gradient Designs for Balancing Cell Migration and Mechanical Strength in Tissue Engineering Scaffolds

### Key Points
*   **Radial Gradient Architecture:** The optimal design for balancing mechanical strength with cell migration is a **radial porosity gradient**, specifically one that mimics the natural structure of long bones (biomimetic). This configuration typically features a **dense outer shell** (low porosity) to bear mechanical loads and a **highly porous inner core** (high porosity) to facilitate nutrient transport and cell migration.
*   **The "Reverse" Gradient Advantage:** Recent research identifies the "reverse radial gradient" (where porosity decreases from the center to the periphery) as superior in yield strength and load-bearing capacity compared to uniform or axial gradients. This structure effectively minimizes stress shielding while maintaining a biologically favorable core.
*   **Pore Size "Goldilocks" Zone:** A gradient that transitions from smaller pores (~100 $\mu$m) to larger pores (300–600 $\mu$m) addresses the conflict between initial cell attachment (favored by small pores) and long-term migration/vascularization (favored by large pores).
*   **Gyroid/TPMS Structures:** Triply Periodic Minimal Surface (TPMS) architectures, particularly the **Gyroid** sheet structure, provide the best mathematical geometry for these gradients, offering superior permeability and stress distribution compared to traditional strut-based lattices.

---

## 1. Introduction

The central challenge in designing scaffolds for tissue engineering, particularly for bone regeneration, lies in resolving the inherent conflict between biological functionality and mechanical integrity. A scaffold must be sufficiently porous to allow for cell migration, vascularization, and nutrient diffusion, yet sufficiently dense to withstand physiological loads and prevent mechanical failure [cite: 1, 2]. This dichotomy is often described as the "permeability-strength trade-off" [cite: 3, 4].

Uniform scaffolds, which possess a homogeneous pore size and porosity throughout, often fail to resolve this conflict. High-porosity uniform scaffolds facilitate rapid cell migration but lack the yield strength required for load-bearing applications, leading to potential implant failure. Conversely, low-porosity scaffolds offer high mechanical strength but restrict oxygen diffusion and cell infiltration, often resulting in a necrotic core [cite: 5, 6].

To address these limitations, functionally graded scaffolds (FGS) have emerged as a superior alternative. By spatially varying porosity and pore size, these scaffolds can be tailored to mimic the hierarchical architecture of natural tissue. This report provides an exhaustive analysis of porosity gradient designs, identifying the **radial gradient**—specifically the dense-shell/porous-core configuration based on Triply Periodic Minimal Surface (TPMS) architectures—as the optimal design for balancing cell migration speed with mechanical strength to ensure long-term biocompatibility.

## 2. The Mechanobiology of Porosity: Migration vs. Strength

Understanding the optimal gradient requires first dissecting the individual requirements of cell migration and mechanical stability, and how they relate to pore geometry.

### 2.1. Cell Migration and Pore Size Dynamics
Cell migration is a critical determinant of scaffold success. For tissue regeneration to occur, cells (such as mesenchymal stem cells or osteoblasts) must penetrate the scaffold's interior rather than merely lining the periphery.

*   **The Confinement Effect:** Research indicates that pore size significantly influences migration speed. In very small pores (<100 $\mu$m), cell migration is often limited by physical confinement and the need for proteolytic remodeling of the matrix [cite: 7]. While small pores provide high specific surface area for initial cell attachment [cite: 8, 9], they can restrict the speed of infiltration and limit the diffusion of oxygen, leading to hypoxia in the scaffold center [cite: 5].
*   **The Optimal Range for Migration:** Larger pores (typically >300 $\mu$m) reduce steric hindrance, allowing for faster cell migration and better vascularization [cite: 10, 11]. Studies have shown that cell migration speed increases with pore size up to a certain threshold, as the open space allows for unimpeded movement and better nutrient supply [cite: 12, 13]. However, if pores become too large (e.g., >800-1000 $\mu$m), the specific surface area available for cell adhesion drops, potentially slowing down the overall rate of tissue formation despite high permeability [cite: 8].
*   **Gradient-Driven Migration:** Cells are sensitive to structural gradients. Gradients in pore size can induce **durotaxis** (migration based on stiffness gradients) and **haptotaxis** (migration based on adhesive surface area gradients). A scaffold that transitions from small to large pores can effectively "guide" cells deep into the construct [cite: 14, 15].

### 2.2. Mechanical Strength and Stress Shielding
The mechanical requirement for a scaffold is twofold: it must be strong enough to support loads (yield strength) and its stiffness (Young's modulus) must match that of the host tissue to prevent stress shielding.

*   **The Porosity-Strength Inverse Relationship:** Mechanical properties, particularly compressive strength and elastic modulus, follow a power-law relationship with relative density. As porosity increases, mechanical strength decreases exponentially [cite: 3, 4]. A uniform scaffold with 80-90% porosity (ideal for biology) often has an elastic modulus far below that of cortical bone, risking structural collapse.
*   **Stress Shielding:** If an implant is too stiff (e.g., solid titanium), it absorbs the mechanical load that should be transmitted to the surrounding bone. This lack of mechanical stimulation causes the bone to resorb, a phenomenon known as stress shielding [cite: 1, 16]. Porous scaffolds reduce the effective modulus of the material. The goal is to achieve a modulus in the range of human bone (10–30 GPa for cortical, 0.05–0.5 GPa for trabecular) [cite: 3, 17].

## 3. Radial Gradient Architectures: The Optimal Design

Research overwhelmingly points to **radial gradient architectures** as the most effective design for balancing these competing needs. This design mimics the natural structure of long bones, which consist of a dense outer cortical shell and a porous inner trabecular core.

### 3.1. The "Reverse" Radial Gradient (Dense Shell / Porous Core)
In the context of additive manufacturing and scaffold design, terminology can vary. Some studies define a "forward" gradient as increasing porosity from center to edge, while others define it based on the manufacturing build direction. However, the functional consensus is that a **dense outer shell with a porous inner core** is superior.

*   **Mechanical Superiority:** A study on Gyroid-based Zn-2Mg scaffolds explicitly compared uniform, axial, and radial gradients. The results demonstrated that **radial gradient scaffolds** possessed the highest equivalent Young's modulus and exceptional load-bearing capacity compared to axial or uniform designs of the same average porosity [cite: 3, 18]. Specifically, the "reverse radial gradient" (defined in the study as porosity decreasing from the center to the edge, i.e., a denser shell) exhibited superior yield strength [cite: 3, 18].
*   **Mechanism of Action:** The dense outer layer acts as a structural shield, bearing the majority of the compressive and torsional loads, similar to cortical bone. This protects the more fragile, high-porosity core from mechanical failure [cite: 19, 20]. This configuration allows the scaffold to maintain a high overall average porosity (beneficial for biology) without sacrificing structural integrity.
*   **Stress Distribution:** Finite Element Analysis (FEA) shows that radial gradients distribute stress more evenly and effectively transfer load to the surrounding bone, thereby mitigating stress shielding more effectively than uniform structures [cite: 1, 21].

### 3.2. Biological Performance of the Porous Core
While the shell provides strength, the core is designed for speed.

*   **Enhanced Infiltration:** The inner core, characterized by high porosity (often 70-90%) and larger pore sizes (300-600 $\mu$m), facilitates rapid cell migration and nutrient transport [cite: 3, 5]. This prevents the formation of a necrotic center, a common failure mode in large uniform scaffolds [cite: 6].
*   **Vascularization:** The larger pores in the core are essential for angiogenesis. Vascular ingrowth requires pore sizes generally greater than 300 $\mu$m to allow capillary formation. A radial gradient ensures that once vessels penetrate the shell (which must have sufficient permeability, typically >100 $\mu$m), they can expand rapidly within the core [cite: 11, 22].
*   **Toxicity Mitigation:** Interestingly, one study on biodegradable Zn-2Mg scaffolds noted that "forward" radial gradients (lower porosity in the center, higher at the edge) showed lower toxicity in vitro [cite: 3]. This suggests that for biodegradable metals, the degradation rate (which is surface-area dependent) must be balanced. However, for non-toxic or slowly degrading materials (like Ti-6Al-4V or PCL), the dense-shell/porous-core remains the mechanical standard.

### 3.3. Comparison with Axial Gradients
Axial gradients (porosity changing from top to bottom) are specifically useful for **osteochondral interfaces** (cartilage-to-bone transitions) where the tissue type changes [cite: 1, 23]. However, for segmental bone defects or load-bearing implants, axial gradients often create weak points. If a scaffold has a high-porosity layer at one end, mechanical failure will likely initiate there under compressive load [cite: 24]. Radial gradients avoid this by maintaining a continuous structural column (the shell) along the load-bearing axis.

## 4. Structural Unit Geometry: The Role of TPMS

The geometric shape of the pores within the gradient is as important as the gradient itself. **Triply Periodic Minimal Surfaces (TPMS)**, such as Gyroid, Diamond, and Primitive structures, have outperformed traditional strut-based (lattice) designs.

### 4.1. The Gyroid Advantage
The Gyroid structure is frequently cited as the optimal unit cell for gradient scaffolds.

*   **Permeability vs. Strength:** Gyroid structures offer a bi-continuous geometry that separates space into two intertwined labyrinths. This provides high permeability for fluid flow (and thus cell migration) even at lower porosities compared to discrete strut lattices [cite: 1, 4].
*   **Curvature and Cell Attachment:** The mean curvature of TPMS surfaces (zero mean curvature) mimics the geometry of natural trabecular bone. This curvature has been shown to be favorable for cell attachment and proliferation [cite: 1].
*   **Stress Concentration:** Unlike strut-based lattices which have sharp nodal connections that act as stress concentrators, TPMS structures have smooth transitions. This results in better fatigue resistance and energy absorption [cite: 1, 25].
*   **Gradient Connectivity:** TPMS equations allow for the generation of continuous gradients without structural discontinuities. A radial gradient can be mathematically generated where the wall thickness of the Gyroid smoothly varies from thick (edge) to thin (center), ensuring no weak interfaces exist between layers [cite: 4, 26].

## 5. Optimal Pore Size Distribution for Long-Term Biocompatibility

To ensure long-term biocompatibility, the scaffold must support not just initial migration, but sustained tissue health and integration.

### 5.1. The Gradient Range
Research suggests the optimal gradient should span specific pore size ranges:
*   **Outer Shell (Cortical Mimicry):** Pore sizes of **100–300 $\mu$m** with lower porosity (e.g., 30-50%). This range is sufficient to allow initial cell ingress and nutrient diffusion but small enough to maximize mechanical stiffness and surface area for osteoblast attachment [cite: 8, 16, 23].
*   **Inner Core (Cancellous Mimicry):** Pore sizes of **300–800 $\mu$m** with high porosity (e.g., 70-90%). This range maximizes permeability, allowing for rapid vascularization and unrestricted cell migration to the center [cite: 5, 11, 16].

### 5.2. Balancing Degradation and Regeneration
For biodegradable scaffolds (e.g., Magnesium or Zinc alloys, Polymers), the porosity gradient also dictates the degradation profile.
*   **Degradation Control:** A highly porous core degrades faster than a dense shell. This is advantageous because as the new bone forms (typically growing from the periphery inwards or via vascular channels), the core clears space for the new tissue while the shell maintains mechanical stability until the remodeling is complete [cite: 27, 28].
*   **Toxicity Management:** In biodegradable metals, rapid degradation can release ions (e.g., Mg2+, Zn2+) at cytotoxic levels. A gradient design allows for modulation of the surface-area-to-volume ratio, thereby controlling the ion release rate to remain within the therapeutic window [cite: 3, 27].

## 6. Material-Specific Considerations

### 6.1. Biodegradable Metals (Zn, Mg)
Recent studies on **Zn-2Mg** scaffolds highlight the efficacy of radial gradients. The "reverse" radial gradient (dense shell) provided the best yield strength, crucial for load-bearing bone defects. The Gyroid structure in these metals provided a modulus (approx. 3-10 GPa) that closely matches trabecular bone, significantly reducing stress shielding compared to solid implants [cite: 3, 27].

### 6.2. Titanium Alloys (Ti-6Al-4V)
For permanent implants, the focus is on osseointegration and fatigue life. Radial gradients in Titanium scaffolds fabricated via Selective Laser Melting (SLM) have shown to effectively lower the elastic modulus of the implant surface to match bone (preventing resorption) while keeping a solid core for screw fixation or high-load transmission [cite: 4, 6, 19].

### 6.3. Polymeric Scaffolds (PCL, PLGA)
In polymers, which are inherently weaker than metals, the dense shell is even more critical for structural integrity. Studies using PCL microspheres showed that "moderately porous" gradients (balancing 200-600 $\mu$m pores) supported better cell survival and mineralization than highly porous uniform scaffolds which collapsed, or low porosity ones which caused necrosis [cite: 5].

## 7. Conclusion

The porosity gradient design that best balances cell migration speed with mechanical strength is a **biomimetic radial gradient** based on **TPMS (Gyroid) architectures**.

Specifically, the optimal configuration is a **"reverse" radial gradient** characterized by:
1.  **A Dense Outer Shell:** Porosity ~30-50%, pore size 100-300 $\mu$m. This ensures mechanical load bearing, matches cortical bone stiffness to prevent stress shielding, and provides high surface area for initial cell attachment.
2.  **A Highly Porous Inner Core:** Porosity ~70-90%, pore size 300-600+ $\mu$m. This facilitates rapid cell migration to the scaffold center, ensures adequate nutrient/waste transport to prevent necrosis, and supports robust vascularization.
3.  **Continuous Transition:** Achieved via TPMS math (e.g., Gyroid), eliminating stress concentrations at interfaces.

This design leverages the "dense shell" to satisfy the mechanical strength requirement and the "porous core" to satisfy the cell migration and biological transport requirement, thereby ensuring long-term biocompatibility through sustained tissue integration and vascular survival.

## References
[cite: 1] PMC10704082
[cite: 25] IJB.1263
[cite: 5] PMC5802344
[cite: 22] PMC11588461
[cite: 10] PMC7407612
[cite: 17] PMC6388715
[cite: 14] PMC3363018
[cite: 3] MDPI 1996-1944/18/18/4399
[cite: 16] PMC5510170
[cite: 8] PMC2958613
[cite: 7] Royal Society 20180225
[cite: 12] ResearchGate 6540965
[cite: 9] ResearchGate 385838156
[cite: 29] PMC4790631
[cite: 3] MDPI 1996-1944/18/18/4399
[cite: 26] ResearchGate 332649304
[cite: 18] PMC12471331
[cite: 21] ResearchGate 385134114
[cite: 19] ResearchGate 351121359
[cite: 30] MDPI 1422-0067/23/9/4533
[cite: 13] PMC4846637
[cite: 11] Frontiers 10.3389/fbioe.2024.1444986
[cite: 31] PMC3826579
[cite: 23] PMC11814525
[cite: 1] PMC10704082
[cite: 6] RSC c8ra04815k
[cite: 32] ResearchGate 329383544
[cite: 2] Hollister SJ, Nat Mater
[cite: 15] PMC8126827
[cite: 24] IPPT o6740
[cite: 3] MDPI 1996-1944/18/18/4399
[cite: 27] PMC10837348
[cite: 28] SemanticScholar f9d3a717
[cite: 4] MDPI 1996-1944/13/11/2589
[cite: 33] PubMed 34909694
[cite: 34] EurekAlert 1060855
[cite: 35] Elsevier Pure 3d-printable-bone
[cite: 23] PMC11814525
[cite: 20] MDPI 2079-6412/14/1/65
[cite: 36] ResearchGate 377134467
[cite: 37] bioRxiv 10.64898
[cite: 18] PMC12471331
[cite: 38] ResearchGate 354628509
[cite: 39] ResearchGate 47700069

**Sources:**
1. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnNPQMU_BI9tQST68_wovrqctsVbPhIzUMahIElJay8F3MwKMVBBZ5YzA2MpfyWR-gOklZm-K3AYTreuw13161OIkEqt125ImGaikgA3l2AQHTeQHT1WOxb5jT_TZ1q240FgJFlHjE)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFa9J-b6U-cBdpnbFnlQCvuj1lu_U-_tcSzVnui9cPzeQKffaqAhzWd1oOFKvNz1wK3WKXEkcmeRKMnuGzakLBcx7P3K7J2fqH8Tgvy8J3Sr6i35Kidby8XtvbZfOMT4cyLtLHYCmWFUu8QQr6iKFdff96avPLOeS6YpjQ_qD1WhXc2I5XaQC998REK1nAK5WHAtaJfn_7TZmnsAaO09gInG4wX8r0HMxM-HNPbxgQhaEaFKJPFEt1mfP03T4xgSbndMTe9cq8HRJyRXP4YphXPWSQ56AFKrC8ganZHNM03z7wAP91oDAgM-Gf5afzzxleY)
3. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHACxA0yRRxG3FaX2dzFUj02oHeyO7xNyguGBJ_5EszCQ5pnfRCIV_4uZXyAtZx_4pEtEvwMFKFyhUbZPMAYt5s2eru4lkTW-c63-ZBHupxU03aTcQ4ym0Li32KtZdR)
4. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCgJCXw9W_xzXjiMvPpKkDJYmVO6ULsKYLMPYHKWvjIgkzAU89xMw590kQJ_52bEDhQmvoN5rEJUfZHc_A7rmf9SCpaY0fM5wZ4xjKqFwfU6HmtUsNKOkqNW33NxYI)
5. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnjaJL4dg-Uyi10hU0yMKljYYRHQyCpZjZFupioqT2ZpUrldUNzXh1M-zfpxQd9eQorwovtyjXHyAU6LRr3mfXsMMGCiu1sCrOI2eH_TzzmjJbGR05b00YexM3ZamwOGfCqIleZ20=)
6. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGE0mSBID0h-zpt_U5eUP1JMBtDOU2ixjCrAzQOgl188V7KOEqaLbW4IQDqMwg7uBoA2LOTVdqkzw8G31hQML7zNXiOm--WTn_i1yEKS9pHltumjfMNvY1jIfzd047UyWvm9_EnIyL1QJYrdmTELS_3_Hc9)
7. [royalsocietypublishing.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFimfYFsm-VfFbnf6I2xrL2DEyB-yxM6Ewha8lG7xh5SeFUIr4IvlfzBqlh8yh2Q2t7wAPXK3M_53zctDTOzZPzSQcOz9VXr_0jAGo7ayMYDUPJAUn16pAlawfxRHy-l6knkw3XLTkmBDn6izMvoFUAMRXHW5IzEX-j6JztqGCHp9jkFWHICIb79_0sP6s0iPTM9GT6tyRC-fDwJMevdXiw6v-aESMbTdIpYYP9FiNI)
8. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3jtNYXgYsyNZ2MkEbcX0g27_-kM2HTcq5Hi4o3iVFwk71TIefQ_16MhamlNSq0af-8MW-UKvpO9mHN-Z8KtoExF25OUnUHr4Y6R8GWD2xzj0iTJMCbuGdNO5DA02WCZxNMzcNGSM=)
9. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFMGJTFQf36d4Cjn7EpXJgbK1BSj7_nX8rxKpm1uIiMQMCW_9sVU413-lyMQ9iTAVFI4jpw6AlhKUSQLNR_6KHBqUWsFOLZZA03VQI8JdC6NOwynlpFcvo72IdEIDeEn-Hp4Q4ZKv20g-L2fVDq25rfm4W42iefnNyGVkLyRGI5oTBbvNfcGwCq0e8Ybi0jivzTB1Trn32RhZBvo1aG4YtORzVciCZGeuAwGMUIi4IQ9WOWjIY9wdRqy7lGzajUsTuNg==)
10. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuyAnSfgyhB4wbdzexR0YdaZ3Y7WrTvgCSthPDr-qc-MATumMuWeaVOQ8S4hhRedujQODaFhJYwXsZJBkT-Hz-eVvysWLySakRq7Ph-aVFUW_aXo0LQRwHBR-WUUWKuI0eTB7EpZI=)
11. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqk9jaPkQ8qL6Qp56DeTtRTZTkSUORCR5eIA3XwG5f3Kv4GDZP1tX1jMXCypq79zmUeiO9MXMsj-cwna0eFFu_cuyhaw2Oay9K6G4YJqkDdar3qz7XOF8twN317dpzgw7qc9iHXNpvar1hwtOkPw176Spgc9eGKqLODLZ-UAt6NUKMxMXjWCukbIKyr04pAv69idk1WH7OlZHtJBzE2yAiEtnr)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWdPeULhKACEKdE7V589FDmg0akb30AFbWwcpJin83Z4vV6NH04z5NjcpvrARXS3DRNeXQ2JKJ8u1qcsV6mu-eAR3AvaG68Cobm0Hy1ZK0KX3DBeI7tJ8vhRWypmGz0wFR8P2gBDdxqKpCIFQx604CbGLsCNhJkO_nHLlNvnymJmMg7-a_lAZFgcXGnTK5Wuj7I6RwRVfMencmr2bZW2ZzTd2UZi1mm4gso_jLh1VwV2eO95bbYEw3niEStzCV2ms2I6aOD_LmEsw95mV3YdA=)
13. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFisOpYiGY72Ry6xKghhHrG4ynVFwcZ872fBZ8pNOEL5k62hPihmFnaV2aACcsMWhmlOdmmHYwCYwTjPWORX8M7NDCqhegN2WBgsHD8vOz0XobggIJ33EVGRrEOwbAoFb8yWZFuJHQ=)
14. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGf-2xjyFuU2DtP4E_oobb9ss1OACvZbDeOjVIx-ko8iSZQpxJA4yXTARXEjtZNAcQEVPT2R7hZR-nQIQOrj-7eRZJ-s0bN0Mt87S67acYPBZCBUmbJv2fIr0vflgkxA0cIIhSwziY=)
15. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEr4TjKmWvvIRGlQ9R_slC4bs-BFVcD-fiVPDQA3slrpxYBjk56bcsTYn0sxUHOOqrJz71bLNqNPWm4k19COhRAlQ9ffLLqIcLns8tliLkwUd-nJ_kaIq4s8Cu-fgyYVh8mNDxOAic=)
16. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwP6mxuxx6VhSHLZYHYkR20GbPI69HTq2lh3vwqetsKUge6EHL_XGlwDhxStPensOSwejq6einaqd0j4YSv2wjEzV-hE4n6VG9qLAHD7fINUDfDKijr4pJ7RqIXwMzXVtopQeMtxU=)
17. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFB6BQmdnEVqGMsXYO90XqUlHcGPn3RNEUWY-dD2G-9AsNllArxyOTwI-KcpsM0C1AdpgrGusT7vIRdFolM_wknUOBf0fwn3Av_JseNRDGS2VsU88aS0cWA42K52xYrV8bEqNAzErQ=)
18. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuKNMhhqG1vjwFR7zjM88Ex5RUQESAYqvom2w5avyncee28tjbgLAeTAHu66O2sMqEyagevNIYmJAvBOPGMBJ2lvXjPw9Z5370TNghDcoaIT0Twn5aJlRQMcqh3tUFus_SqMA7vph8)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZ_siJg8eV2WhKiOqEyM2k8a_4Ueek0dGckQS4uvU0C_AUL3ja0hD57x3M2iJzwzWmEYDIy54T4cNCpXjk8rK8AhGptcyLeu64FkSXctaPdbmAB3Wy792o3JVxsLR3yTRp60YAJ2DhahP7tmAGW1YXOIhkkOasVdX9UkR6reU7NddV2XvZcZJjPHC8yM51hKWUmXlbVCxWdpYI09gQElaD34oJrmLP69Dl39a3m8qoU91jVxqBubt0xU6IF2j_bu2vqmishFvKP0SaVBZ8SHEOHKNbJxSbht-_NCgqh5f44NtiSEHSkNI=)
20. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELqmhhF8KF3RjXiRRz45ZB3_LVRPm5cx6B-FaMDawvLks8xGxJPalRXEFYp62Do2c837y8E6ZR2Ns5p9J2OZzRb-xXwgedxSE-t7SSzbdxZcFLlO_sEQB7jP5T)
21. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2h3lKPhyicJDQWorW_yQYj711ppx4tWhccc2gFf7AwSC37TYuyxW-pC__OYWszK1J2IeodkWQBGzDZ5fSgsC6QQisc2IOxbJ6VPuQ5tb5HXx-ecFP5XTLEUejA4-x2qUgFZ5uBp3ODO5IdiKjqJBibedOU9DIWlyMXIoHJ6bAB7uoiQjfFsjuWa_TeQX2i9W6twnbex8r90U9UanMKod6EEWb0emrLpzYFjC37Wb_tZp-d6JAfGLbgGH9NG_bB770eT9R_1OIPAspyiSZwzb0MLL8y0l0zzFFiO4XNFjiSu47xGOIqmOBRCzG588RYVmXw47tLoeglxP74q_Y2duXgbs65D1lNK0sZ_5-5NE3uIP3Fht9fYKblbDdrm7d)
22. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkC4HqdJp54YKWOukzUyoMgH7a7O-NOG-R-KZ-Ojr803yueVQ_7JEVxEGs0cZoWhGCDviCqiadJ_7R9oSjdtoN2b41hbql0gCEsncOoHvaatE6CaEWAkq76BW_0e5udr66BeA1Ek47)
23. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0K8OIPrrMgUE8COxDFW5Z3RLSFxvdrxZnVPJwPDSqHvNsMJSUDaajlGlVu7uYq3OCX0Sr5wZiyHwHEPMW_A6GgrAB2QG3_Y74-8ouCSb6sDvz8XiUiTuGilmQXwEHHyRxZg5OqAzD)
24. [pan.pl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKm5avFrOLwhrk-f1YxLmCl29Q0QbBvwD05G774psMu0ITNsbaO1R6GftRIQ4YJjEc83krjma9Lzn0hjR_SMDHxp_a-8KljjrWVsO7s5nLoNDDSfU7bzutmuiD7OzhK8w=)
25. [accscience.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8Sf11K2BynTpugd28F9Vq8tmGBgLevgXJp3p6dbKSCMoyWCIE4gKo2rthOwSpbhUVLRKafQclBXlA9UbdAHOI50ZKvlj9VPJwNqM61ieA0VN_-dULEbURAGldCLuO94vAY7OZPOF_OUg9URATjg==)
26. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSnrPW8onPZ9aG5KhUCjT1BYEixhVVs_Yf686ju_AnUx5Z_FNlP2HP0DAY3QUWTtfidf79yfwzd-nyDF5aySRWzpv47EnHc0ri6aCoozbjN5UtQTxvr7hKNOCEwawH6JP-de5f-Prgpe-cGmVusJqT1kpCrW9M3r43KQXI9bi5-zkfvWhbToM8E9e3NoFvLPHmrWYd1qGSZkbcX0gHQdPHhnyYJEvgfetLQGvL6jp1cr03Jw==)
27. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQ6QTKhfLMcbM1ZFZGem0D-HYS3VhjX_jPTU-fqADNGGCI8_jllGe0y1V6wk-Rv6Ey84TQuV9-Rf_Kr-Kbx1I-Wcuz-_OtnFWTG7RNAuToESUjaIop8E7L0XYOBqA6aC_vEbzFHyQa)
28. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhdrNas64Y-NEpZrtpQnKyrVYBQdGT933QMM68a2Oz_WA2i9-KPDFMd6KOOUcGoZsVt4H7fOCLq9mH31iELAhasq0cW00obTMIWs-QYNOr9CbrF-YOYXVar0iwbnDTAnEHKQQbfDmhH5pCP2qTxk1vrWxtN4beSdYzWSm2VfnHJ8VkaA==)
29. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpcpO2KexLf2G56YuLx-ELSybQa38X2pb-njCaEv89kbOhcHm4q1nFF9rClHNbGdpVkYC0vqBuZU30vV46eU5Fa8mgYsVc3CZtucyVE8_oRhwd71N9G7ffX7tg7QUCkCWPrXu1L7k=)
30. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFx6B1NhtvEHt28_zyCUGuI12RtAnIATcswaTBeQYYsfchaxqTClWgbCFCt6LHQlq3vcvQ-s_y3CXLJH5PA7AgBwNu_iaKkk_MB6G-pBmK56qw2zbvJIBONKZ96-t8=)
31. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzAVAWCpo22tS6lilHtXfw-GaoYztyc-UQvewScU3ThoIBwMGTlGWN_OLqD9dogQg-pcFk0EobJ326CjmfFPoIGYtEw_h1UGXp1AtaEzdjeAOkKz8Uif_MWHwc0q_ZK44bdnN5wgI=)
32. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4Kr3OC4SuvFeGB16WywmSavjxryzM6vEq1vNLxYSX7QOYvV2I8-TjzfMWbftphYDcU9JpyG_rDndiopRvAcLmMV-fLtSCXu6RGTkWWa0HUKRLSbiZeKAN7npKtL8hRLA6nOd5myc90RarWsR5jP4ipDFIu6MPCitAYF9EkypBBBoffFdEAD9_VSzPMLV4DlDFZK909-d0olkA_cELC0haxndeyMoMakWtc6ub2QM44e0npodYD3tcZBgpFA3SS--FGkezSLs75oWk)
33. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYtAL9sFbRIGGUOKDNtAYJlmTqlzxGeTvTP2IHBIBeuU-XVbdQ-9GT4lmqXxWb8ljlkhArvOZCqwcT-yTUW_eEKw6X49XGV4PaCEiUxFs2-DJsAEtwr9VMoO-lL-Qk)
34. [eurekalert.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-VwpgS4xFbjvmQMl8AcImkfcCdpFQWDxRLmmbrYm_llCW8MMpP8VyiSl5lqc4RsAQCNsqDXXAYREitpHh2XCbGRnlMp1cFORHtvphlP-laxgC1IIo8_UHr3I_5_ySr3eM5FSPDQ==)
35. [elsevierpure.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELC2k07vJVKG4JUHSlgs5OjIdjmkvxL8lAP3qW6AvsuVLYAAcYhdkW-ium5mmBY7n5ZvUueB2jtF0exwNLkRrxrAMtfIZjjGdpCaabfBmW5ChLn6mgEwMyL7nVQ6C1Ev1D0T6YGIHD066NdvY3E-pM1DfRAciplk67F2NLlZ6HKFcfdJ3pHyg5HBRSmn3lVvrfp-kNjW62qLaqo8koda7SK5pSuas=)
36. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEys_yNT2hLOsQAXkksxKykYGK8eVIXzlsfcMHVeV1rOx1VO4s-bOFl2l3TrK5xnRqzzir2AcchFdDYt-7jk57WOb6k_EIBdUQU5IknyrD3nkABHZtG5HAwarhtL_YXg7jj0DGWCRzhcxDc3mmoaBOqO4c-B8KZQZq9Z6U1YeIggG5Z9-QOD7GFzkvwQxMWg-08TBCq8bgZWgtEIXvGiwQcnykmf2fN7MgpDvRMCSgCyfZK8vJ4q2kL-rutdC2DeTMgfkjgkOcPatkw0GLmxDupT_1gLB1wBCxXeQ==)
37. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEUZQKSnLo9_qkcj3r6ibW-h_cnmQmJv4WHJenS-GCN6UjcE-r0LdODQqqQyS2yaWF_qIkbcok-TdprrP6vriafusHCgW0eA65MRygZeiG3Vyr9EdsF_8t6F99jl8G9Jk4g4V0akNzRzFSbC9G71KwJfjqlAXsKZv6BQ==)
38. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIQqJbGgH0cEkCTlP49dxZwvdh1i6AltorjYnCYD4zSgFqAnhseJvgvEcqNacwAeaTLnqGxKKZuEeNWWGWix2cDLc9idztbWzseT6RRN3evrZdI5f93ZMjWXE552t0r3M14BsbsUhZQNuAYjNv6ka5Gv1fFl76fgb0q9tH7p_q9g-FxMIU5EofWPYoj7KTZsqZx2vaTYPp9RdA3GS4UNzkRYXaDLL8zehMOD8D9nXPbUsE4khJYzOdx5cDEmU=)
39. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLo9Jji6FBd851QK92Zk5JT1epF-bTGpZAhrlOq2OfF-AED1d5z1NkeE0Ft1aPN02gBDS_8C7lyV7-hrzQZRvKT4UNTziRqrbORIrKsLjjwX5Gn7c6NAjPM2kjGrVyG-eYWGcQdQpyjMjpMsPev5neRcmFdNDmfXqXqEW9b77qQloy-VkhFKr9b-y7ViZQuT72krWybgrF56gMQOPJfqTwFRO-LrN2DdDhI3bAmIn6vgfZBUD7luxdF8sxiZ1ePRWUXmLT5RC9bzjVR48mml4sd2i6-b6-3DZJTNAsyyP6NL2nqXXatLqoyRc8Nn0-Rcy05AzD-xdSl6erOe1UnHPzPQ==)


## Annotations
Annotation(end_index=1935, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFa9J-b6U-cBdpnbFnlQCvuj1lu_U-_tcSzVnui9cPzeQKffaqAhzWd1oOFKvNz1wK3WKXEkcmeRKMnuGzakLBcx7P3K7J2fqH8Tgvy8J3Sr6i35Kidby8XtvbZfOMT4cyLtLHYCmWFUu8QQr6iKFdff96avPLOeS6YpjQ_qD1WhXc2I5XaQC998REK1nAK5WHAtaJfn_7TZmnsAaO09gInG4wX8r0HMxM-HNPbxgQhaEaFKJPFEt1mfP03T4xgSbndMTe9cq8HRJyRXP4YphXPWSQ56AFKrC8ganZHNM03z7wAP91oDAgM-Gf5afzzxleY', start_index=1923)
Annotation(end_index=1935, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnNPQMU_BI9tQST68_wovrqctsVbPhIzUMahIElJay8F3MwKMVBBZ5YzA2MpfyWR-gOklZm-K3AYTreuw13161OIkEqt125ImGaikgA3l2AQHTeQHT1WOxb5jT_TZ1q240FgJFlHjE', start_index=1923)
Annotation(end_index=2024, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCgJCXw9W_xzXjiMvPpKkDJYmVO6ULsKYLMPYHKWvjIgkzAU89xMw590kQJ_52bEDhQmvoN5rEJUfZHc_A7rmf9SCpaY0fM5wZ4xjKqFwfU6HmtUsNKOkqNW33NxYI', start_index=2012)
Annotation(end_index=2024, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHACxA0yRRxG3FaX2dzFUj02oHeyO7xNyguGBJ_5EszCQ5pnfRCIV_4uZXyAtZx_4pEtEvwMFKFyhUbZPMAYt5s2eru4lkTW-c63-ZBHupxU03aTcQ4ym0Li32KtZdR', start_index=2012)
Annotation(end_index=2482, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnjaJL4dg-Uyi10hU0yMKljYYRHQyCpZjZFupioqT2ZpUrldUNzXh1M-zfpxQd9eQorwovtyjXHyAU6LRr3mfXsMMGCiu1sCrOI2eH_TzzmjJbGR05b00YexM3ZamwOGfCqIleZ20=', start_index=2470)
Annotation(end_index=2482, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGE0mSBID0h-zpt_U5eUP1JMBtDOU2ixjCrAzQOgl188V7KOEqaLbW4IQDqMwg7uBoA2LOTVdqkzw8G31hQML7zNXiOm--WTn_i1yEKS9pHltumjfMNvY1jIfzd047UyWvm9_EnIyL1QJYrdmTELS_3_Hc9', start_index=2470)
Annotation(end_index=3852, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFimfYFsm-VfFbnf6I2xrL2DEyB-yxM6Ewha8lG7xh5SeFUIr4IvlfzBqlh8yh2Q2t7wAPXK3M_53zctDTOzZPzSQcOz9VXr_0jAGo7ayMYDUPJAUn16pAlawfxRHy-l6knkw3XLTkmBDn6izMvoFUAMRXHW5IzEX-j6JztqGCHp9jkFWHICIb79_0sP6s0iPTM9GT6tyRC-fDwJMevdXiw6v-aESMbTdIpYYP9FiNI', start_index=3843)
Annotation(end_index=3947, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3jtNYXgYsyNZ2MkEbcX0g27_-kM2HTcq5Hi4o3iVFwk71TIefQ_16MhamlNSq0af-8MW-UKvpO9mHN-Z8KtoExF25OUnUHr4Y6R8GWD2xzj0iTJMCbuGdNO5DA02WCZxNMzcNGSM=', start_index=3935)
Annotation(end_index=3947, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFMGJTFQf36d4Cjn7EpXJgbK1BSj7_nX8rxKpm1uIiMQMCW_9sVU413-lyMQ9iTAVFI4jpw6AlhKUSQLNR_6KHBqUWsFOLZZA03VQI8JdC6NOwynlpFcvo72IdEIDeEn-Hp4Q4ZKv20g-L2fVDq25rfm4W42iefnNyGVkLyRGI5oTBbvNfcGwCq0e8Ybi0jivzTB1Trn32RhZBvo1aG4YtORzVciCZGeuAwGMUIi4IQ9WOWjIY9wdRqy7lGzajUsTuNg==', start_index=3935)
Annotation(end_index=4079, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnjaJL4dg-Uyi10hU0yMKljYYRHQyCpZjZFupioqT2ZpUrldUNzXh1M-zfpxQd9eQorwovtyjXHyAU6LRr3mfXsMMGCiu1sCrOI2eH_TzzmjJbGR05b00YexM3ZamwOGfCqIleZ20=', start_index=4070)
Annotation(end_index=4260, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuyAnSfgyhB4wbdzexR0YdaZ3Y7WrTvgCSthPDr-qc-MATumMuWeaVOQ8S4hhRedujQODaFhJYwXsZJBkT-Hz-eVvysWLySakRq7Ph-aVFUW_aXo0LQRwHBR-WUUWKuI0eTB7EpZI=', start_index=4246)
Annotation(end_index=4260, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqk9jaPkQ8qL6Qp56DeTtRTZTkSUORCR5eIA3XwG5f3Kv4GDZP1tX1jMXCypq79zmUeiO9MXMsj-cwna0eFFu_cuyhaw2Oay9K6G4YJqkDdar3qz7XOF8twN317dpzgw7qc9iHXNpvar1hwtOkPw176Spgc9eGKqLODLZ-UAt6NUKMxMXjWCukbIKyr04pAv69idk1WH7OlZHtJBzE2yAiEtnr', start_index=4246)
Annotation(end_index=4448, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWdPeULhKACEKdE7V589FDmg0akb30AFbWwcpJin83Z4vV6NH04z5NjcpvrARXS3DRNeXQ2JKJ8u1qcsV6mu-eAR3AvaG68Cobm0Hy1ZK0KX3DBeI7tJ8vhRWypmGz0wFR8P2gBDdxqKpCIFQx604CbGLsCNhJkO_nHLlNvnymJmMg7-a_lAZFgcXGnTK5Wuj7I6RwRVfMencmr2bZW2ZzTd2UZi1mm4gso_jLh1VwV2eO95bbYEw3niEStzCV2ms2I6aOD_LmEsw95mV3YdA=', start_index=4434)
Annotation(end_index=4448, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFisOpYiGY72Ry6xKghhHrG4ynVFwcZ872fBZ8pNOEL5k62hPihmFnaV2aACcsMWhmlOdmmHYwCYwTjPWORX8M7NDCqhegN2WBgsHD8vOz0XobggIJ33EVGRrEOwbAoFb8yWZFuJHQ=', start_index=4434)
Annotation(end_index=4669, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3jtNYXgYsyNZ2MkEbcX0g27_-kM2HTcq5Hi4o3iVFwk71TIefQ_16MhamlNSq0af-8MW-UKvpO9mHN-Z8KtoExF25OUnUHr4Y6R8GWD2xzj0iTJMCbuGdNO5DA02WCZxNMzcNGSM=', start_index=4660)
Annotation(end_index=5035, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEr4TjKmWvvIRGlQ9R_slC4bs-BFVcD-fiVPDQA3slrpxYBjk56bcsTYn0sxUHOOqrJz71bLNqNPWm4k19COhRAlQ9ffLLqIcLns8tliLkwUd-nJ_kaIq4s8Cu-fgyYVh8mNDxOAic=', start_index=5021)
Annotation(end_index=5035, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGf-2xjyFuU2DtP4E_oobb9ss1OACvZbDeOjVIx-ko8iSZQpxJA4yXTARXEjtZNAcQEVPT2R7hZR-nQIQOrj-7eRZJ-s0bN0Mt87S67acYPBZCBUmbJv2fIr0vflgkxA0cIIhSwziY=', start_index=5021)
Annotation(end_index=5566, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCgJCXw9W_xzXjiMvPpKkDJYmVO6ULsKYLMPYHKWvjIgkzAU89xMw590kQJ_52bEDhQmvoN5rEJUfZHc_A7rmf9SCpaY0fM5wZ4xjKqFwfU6HmtUsNKOkqNW33NxYI', start_index=5554)
Annotation(end_index=5566, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHACxA0yRRxG3FaX2dzFUj02oHeyO7xNyguGBJ_5EszCQ5pnfRCIV_4uZXyAtZx_4pEtEvwMFKFyhUbZPMAYt5s2eru4lkTW-c63-ZBHupxU03aTcQ4ym0Li32KtZdR', start_index=5554)
Annotation(end_index=5994, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnNPQMU_BI9tQST68_wovrqctsVbPhIzUMahIElJay8F3MwKMVBBZ5YzA2MpfyWR-gOklZm-K3AYTreuw13161OIkEqt125ImGaikgA3l2AQHTeQHT1WOxb5jT_TZ1q240FgJFlHjE', start_index=5981)
Annotation(end_index=5994, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwP6mxuxx6VhSHLZYHYkR20GbPI69HTq2lh3vwqetsKUge6EHL_XGlwDhxStPensOSwejq6einaqd0j4YSv2wjEzV-hE4n6VG9qLAHD7fINUDfDKijr4pJ7RqIXwMzXVtopQeMtxU=', start_index=5981)
Annotation(end_index=6190, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFB6BQmdnEVqGMsXYO90XqUlHcGPn3RNEUWY-dD2G-9AsNllArxyOTwI-KcpsM0C1AdpgrGusT7vIRdFolM_wknUOBf0fwn3Av_JseNRDGS2VsU88aS0cWA42K52xYrV8bEqNAzErQ=', start_index=6177)
Annotation(end_index=6190, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHACxA0yRRxG3FaX2dzFUj02oHeyO7xNyguGBJ_5EszCQ5pnfRCIV_4uZXyAtZx_4pEtEvwMFKFyhUbZPMAYt5s2eru4lkTW-c63-ZBHupxU03aTcQ4ym0Li32KtZdR', start_index=6177)
Annotation(end_index=7288, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuKNMhhqG1vjwFR7zjM88Ex5RUQESAYqvom2w5avyncee28tjbgLAeTAHu66O2sMqEyagevNIYmJAvBOPGMBJ2lvXjPw9Z5370TNghDcoaIT0Twn5aJlRQMcqh3tUFus_SqMA7vph8', start_index=7275)
Annotation(end_index=7288, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHACxA0yRRxG3FaX2dzFUj02oHeyO7xNyguGBJ_5EszCQ5pnfRCIV_4uZXyAtZx_4pEtEvwMFKFyhUbZPMAYt5s2eru4lkTW-c63-ZBHupxU03aTcQ4ym0Li32KtZdR', start_index=7275)
Annotation(end_index=7477, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuKNMhhqG1vjwFR7zjM88Ex5RUQESAYqvom2w5avyncee28tjbgLAeTAHu66O2sMqEyagevNIYmJAvBOPGMBJ2lvXjPw9Z5370TNghDcoaIT0Twn5aJlRQMcqh3tUFus_SqMA7vph8', start_index=7464)
Annotation(end_index=7477, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHACxA0yRRxG3FaX2dzFUj02oHeyO7xNyguGBJ_5EszCQ5pnfRCIV_4uZXyAtZx_4pEtEvwMFKFyhUbZPMAYt5s2eru4lkTW-c63-ZBHupxU03aTcQ4ym0Li32KtZdR', start_index=7464)
Annotation(end_index=7735, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELqmhhF8KF3RjXiRRz45ZB3_LVRPm5cx6B-FaMDawvLks8xGxJPalRXEFYp62Do2c837y8E6ZR2Ns5p9J2OZzRb-xXwgedxSE-t7SSzbdxZcFLlO_sEQB7jP5T', start_index=7721)
Annotation(end_index=7735, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZ_siJg8eV2WhKiOqEyM2k8a_4Ueek0dGckQS4uvU0C_AUL3ja0hD57x3M2iJzwzWmEYDIy54T4cNCpXjk8rK8AhGptcyLeu64FkSXctaPdbmAB3Wy792o3JVxsLR3yTRp60YAJ2DhahP7tmAGW1YXOIhkkOasVdX9UkR6reU7NddV2XvZcZJjPHC8yM51hKWUmXlbVCxWdpYI09gQElaD34oJrmLP69Dl39a3m8qoU91jVxqBubt0xU6IF2j_bu2vqmishFvKP0SaVBZ8SHEOHKNbJxSbht-_NCgqh5f44NtiSEHSkNI=', start_index=7721)
Annotation(end_index=8149, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2h3lKPhyicJDQWorW_yQYj711ppx4tWhccc2gFf7AwSC37TYuyxW-pC__OYWszK1J2IeodkWQBGzDZ5fSgsC6QQisc2IOxbJ6VPuQ5tb5HXx-ecFP5XTLEUejA4-x2qUgFZ5uBp3ODO5IdiKjqJBibedOU9DIWlyMXIoHJ6bAB7uoiQjfFsjuWa_TeQX2i9W6twnbex8r90U9UanMKod6EEWb0emrLpzYFjC37Wb_tZp-d6JAfGLbgGH9NG_bB770eT9R_1OIPAspyiSZwzb0MLL8y0l0zzFFiO4XNFjiSu47xGOIqmOBRCzG588RYVmXw47tLoeglxP74q_Y2duXgbs65D1lNK0sZ_5-5NE3uIP3Fht9fYKblbDdrm7d', start_index=8136)
Annotation(end_index=8149, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnNPQMU_BI9tQST68_wovrqctsVbPhIzUMahIElJay8F3MwKMVBBZ5YzA2MpfyWR-gOklZm-K3AYTreuw13161OIkEqt125ImGaikgA3l2AQHTeQHT1WOxb5jT_TZ1q240FgJFlHjE', start_index=8136)
Annotation(end_index=8472, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnjaJL4dg-Uyi10hU0yMKljYYRHQyCpZjZFupioqT2ZpUrldUNzXh1M-zfpxQd9eQorwovtyjXHyAU6LRr3mfXsMMGCiu1sCrOI2eH_TzzmjJbGR05b00YexM3ZamwOGfCqIleZ20=', start_index=8460)
Annotation(end_index=8472, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHACxA0yRRxG3FaX2dzFUj02oHeyO7xNyguGBJ_5EszCQ5pnfRCIV_4uZXyAtZx_4pEtEvwMFKFyhUbZPMAYt5s2eru4lkTW-c63-ZBHupxU03aTcQ4ym0Li32KtZdR', start_index=8460)
Annotation(end_index=8582, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGE0mSBID0h-zpt_U5eUP1JMBtDOU2ixjCrAzQOgl188V7KOEqaLbW4IQDqMwg7uBoA2LOTVdqkzw8G31hQML7zNXiOm--WTn_i1yEKS9pHltumjfMNvY1jIfzd047UyWvm9_EnIyL1QJYrdmTELS_3_Hc9', start_index=8573)
Annotation(end_index=8956, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkC4HqdJp54YKWOukzUyoMgH7a7O-NOG-R-KZ-Ojr803yueVQ_7JEVxEGs0cZoWhGCDviCqiadJ_7R9oSjdtoN2b41hbql0gCEsncOoHvaatE6CaEWAkq76BW_0e5udr66BeA1Ek47', start_index=8942)
Annotation(end_index=8956, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqk9jaPkQ8qL6Qp56DeTtRTZTkSUORCR5eIA3XwG5f3Kv4GDZP1tX1jMXCypq79zmUeiO9MXMsj-cwna0eFFu_cuyhaw2Oay9K6G4YJqkDdar3qz7XOF8twN317dpzgw7qc9iHXNpvar1hwtOkPw176Spgc9eGKqLODLZ-UAt6NUKMxMXjWCukbIKyr04pAv69idk1WH7OlZHtJBzE2yAiEtnr', start_index=8942)
Annotation(end_index=9175, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHACxA0yRRxG3FaX2dzFUj02oHeyO7xNyguGBJ_5EszCQ5pnfRCIV_4uZXyAtZx_4pEtEvwMFKFyhUbZPMAYt5s2eru4lkTW-c63-ZBHupxU03aTcQ4ym0Li32KtZdR', start_index=9166)
Annotation(end_index=9663, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnNPQMU_BI9tQST68_wovrqctsVbPhIzUMahIElJay8F3MwKMVBBZ5YzA2MpfyWR-gOklZm-K3AYTreuw13161OIkEqt125ImGaikgA3l2AQHTeQHT1WOxb5jT_TZ1q240FgJFlHjE', start_index=9650)
Annotation(end_index=9663, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0K8OIPrrMgUE8COxDFW5Z3RLSFxvdrxZnVPJwPDSqHvNsMJSUDaajlGlVu7uYq3OCX0Sr5wZiyHwHEPMW_A6GgrAB2QG3_Y74-8ouCSb6sDvz8XiUiTuGilmQXwEHHyRxZg5OqAzD', start_index=9650)
Annotation(end_index=9900, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKm5avFrOLwhrk-f1YxLmCl29Q0QbBvwD05G774psMu0ITNsbaO1R6GftRIQ4YJjEc83krjma9Lzn0hjR_SMDHxp_a-8KljjrWVsO7s5nLoNDDSfU7bzutmuiD7OzhK8w=', start_index=9890)
Annotation(end_index=10724, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnNPQMU_BI9tQST68_wovrqctsVbPhIzUMahIElJay8F3MwKMVBBZ5YzA2MpfyWR-gOklZm-K3AYTreuw13161OIkEqt125ImGaikgA3l2AQHTeQHT1WOxb5jT_TZ1q240FgJFlHjE', start_index=10712)
Annotation(end_index=10724, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCgJCXw9W_xzXjiMvPpKkDJYmVO6ULsKYLMPYHKWvjIgkzAU89xMw590kQJ_52bEDhQmvoN5rEJUfZHc_A7rmf9SCpaY0fM5wZ4xjKqFwfU6HmtUsNKOkqNW33NxYI', start_index=10712)
Annotation(end_index=10964, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnNPQMU_BI9tQST68_wovrqctsVbPhIzUMahIElJay8F3MwKMVBBZ5YzA2MpfyWR-gOklZm-K3AYTreuw13161OIkEqt125ImGaikgA3l2AQHTeQHT1WOxb5jT_TZ1q240FgJFlHjE', start_index=10955)
Annotation(end_index=11211, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnNPQMU_BI9tQST68_wovrqctsVbPhIzUMahIElJay8F3MwKMVBBZ5YzA2MpfyWR-gOklZm-K3AYTreuw13161OIkEqt125ImGaikgA3l2AQHTeQHT1WOxb5jT_TZ1q240FgJFlHjE', start_index=11198)
Annotation(end_index=11211, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8Sf11K2BynTpugd28F9Vq8tmGBgLevgXJp3p6dbKSCMoyWCIE4gKo2rthOwSpbhUVLRKafQclBXlA9UbdAHOI50ZKvlj9VPJwNqM61ieA0VN_-dULEbURAGldCLuO94vAY7OZPOF_OUg9URATjg==', start_index=11198)
Annotation(end_index=11547, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCgJCXw9W_xzXjiMvPpKkDJYmVO6ULsKYLMPYHKWvjIgkzAU89xMw590kQJ_52bEDhQmvoN5rEJUfZHc_A7rmf9SCpaY0fM5wZ4xjKqFwfU6HmtUsNKOkqNW33NxYI', start_index=11534)
Annotation(end_index=11547, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSnrPW8onPZ9aG5KhUCjT1BYEixhVVs_Yf686ju_AnUx5Z_FNlP2HP0DAY3QUWTtfidf79yfwzd-nyDF5aySRWzpv47EnHc0ri6aCoozbjN5UtQTxvr7hKNOCEwawH6JP-de5f-Prgpe-cGmVusJqT1kpCrW9M3r43KQXI9bi5-zkfvWhbToM8E9e3NoFvLPHmrWYd1qGSZkbcX0gHQdPHhnyYJEvgfetLQGvL6jp1cr03Jw==', start_index=11534)
Annotation(end_index=12162, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwP6mxuxx6VhSHLZYHYkR20GbPI69HTq2lh3vwqetsKUge6EHL_XGlwDhxStPensOSwejq6einaqd0j4YSv2wjEzV-hE4n6VG9qLAHD7fINUDfDKijr4pJ7RqIXwMzXVtopQeMtxU=', start_index=12145)
Annotation(end_index=12162, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0K8OIPrrMgUE8COxDFW5Z3RLSFxvdrxZnVPJwPDSqHvNsMJSUDaajlGlVu7uYq3OCX0Sr5wZiyHwHEPMW_A6GgrAB2QG3_Y74-8ouCSb6sDvz8XiUiTuGilmQXwEHHyRxZg5OqAzD', start_index=12145)
Annotation(end_index=12162, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3jtNYXgYsyNZ2MkEbcX0g27_-kM2HTcq5Hi4o3iVFwk71TIefQ_16MhamlNSq0af-8MW-UKvpO9mHN-Z8KtoExF25OUnUHr4Y6R8GWD2xzj0iTJMCbuGdNO5DA02WCZxNMzcNGSM=', start_index=12145)
Annotation(end_index=12408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnjaJL4dg-Uyi10hU0yMKljYYRHQyCpZjZFupioqT2ZpUrldUNzXh1M-zfpxQd9eQorwovtyjXHyAU6LRr3mfXsMMGCiu1sCrOI2eH_TzzmjJbGR05b00YexM3ZamwOGfCqIleZ20=', start_index=12391)
Annotation(end_index=12408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqk9jaPkQ8qL6Qp56DeTtRTZTkSUORCR5eIA3XwG5f3Kv4GDZP1tX1jMXCypq79zmUeiO9MXMsj-cwna0eFFu_cuyhaw2Oay9K6G4YJqkDdar3qz7XOF8twN317dpzgw7qc9iHXNpvar1hwtOkPw176Spgc9eGKqLODLZ-UAt6NUKMxMXjWCukbIKyr04pAv69idk1WH7OlZHtJBzE2yAiEtnr', start_index=12391)
Annotation(end_index=12408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwP6mxuxx6VhSHLZYHYkR20GbPI69HTq2lh3vwqetsKUge6EHL_XGlwDhxStPensOSwejq6einaqd0j4YSv2wjEzV-hE4n6VG9qLAHD7fINUDfDKijr4pJ7RqIXwMzXVtopQeMtxU=', start_index=12391)
Annotation(end_index=12937, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQ6QTKhfLMcbM1ZFZGem0D-HYS3VhjX_jPTU-fqADNGGCI8_jllGe0y1V6wk-Rv6Ey84TQuV9-Rf_Kr-Kbx1I-Wcuz-_OtnFWTG7RNAuToESUjaIop8E7L0XYOBqA6aC_vEbzFHyQa', start_index=12923)
Annotation(end_index=12937, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhdrNas64Y-NEpZrtpQnKyrVYBQdGT933QMM68a2Oz_WA2i9-KPDFMd6KOOUcGoZsVt4H7fOCLq9mH31iELAhasq0cW00obTMIWs-QYNOr9CbrF-YOYXVar0iwbnDTAnEHKQQbfDmhH5pCP2qTxk1vrWxtN4beSdYzWSm2VfnHJ8VkaA==', start_index=12923)
Annotation(end_index=13239, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQ6QTKhfLMcbM1ZFZGem0D-HYS3VhjX_jPTU-fqADNGGCI8_jllGe0y1V6wk-Rv6Ey84TQuV9-Rf_Kr-Kbx1I-Wcuz-_OtnFWTG7RNAuToESUjaIop8E7L0XYOBqA6aC_vEbzFHyQa', start_index=13226)
Annotation(end_index=13239, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHACxA0yRRxG3FaX2dzFUj02oHeyO7xNyguGBJ_5EszCQ5pnfRCIV_4uZXyAtZx_4pEtEvwMFKFyhUbZPMAYt5s2eru4lkTW-c63-ZBHupxU03aTcQ4ym0Li32KtZdR', start_index=13226)
Annotation(end_index=13714, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQ6QTKhfLMcbM1ZFZGem0D-HYS3VhjX_jPTU-fqADNGGCI8_jllGe0y1V6wk-Rv6Ey84TQuV9-Rf_Kr-Kbx1I-Wcuz-_OtnFWTG7RNAuToESUjaIop8E7L0XYOBqA6aC_vEbzFHyQa', start_index=13701)
Annotation(end_index=13714, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHACxA0yRRxG3FaX2dzFUj02oHeyO7xNyguGBJ_5EszCQ5pnfRCIV_4uZXyAtZx_4pEtEvwMFKFyhUbZPMAYt5s2eru4lkTW-c63-ZBHupxU03aTcQ4ym0Li32KtZdR', start_index=13701)
Annotation(end_index=14114, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCgJCXw9W_xzXjiMvPpKkDJYmVO6ULsKYLMPYHKWvjIgkzAU89xMw590kQJ_52bEDhQmvoN5rEJUfZHc_A7rmf9SCpaY0fM5wZ4xjKqFwfU6HmtUsNKOkqNW33NxYI', start_index=14098)
Annotation(end_index=14114, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGE0mSBID0h-zpt_U5eUP1JMBtDOU2ixjCrAzQOgl188V7KOEqaLbW4IQDqMwg7uBoA2LOTVdqkzw8G31hQML7zNXiOm--WTn_i1yEKS9pHltumjfMNvY1jIfzd047UyWvm9_EnIyL1QJYrdmTELS_3_Hc9', start_index=14098)
Annotation(end_index=14114, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZ_siJg8eV2WhKiOqEyM2k8a_4Ueek0dGckQS4uvU0C_AUL3ja0hD57x3M2iJzwzWmEYDIy54T4cNCpXjk8rK8AhGptcyLeu64FkSXctaPdbmAB3Wy792o3JVxsLR3yTRp60YAJ2DhahP7tmAGW1YXOIhkkOasVdX9UkR6reU7NddV2XvZcZJjPHC8yM51hKWUmXlbVCxWdpYI09gQElaD34oJrmLP69Dl39a3m8qoU91jVxqBubt0xU6IF2j_bu2vqmishFvKP0SaVBZ8SHEOHKNbJxSbht-_NCgqh5f44NtiSEHSkNI=', start_index=14098)
Annotation(end_index=14538, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnjaJL4dg-Uyi10hU0yMKljYYRHQyCpZjZFupioqT2ZpUrldUNzXh1M-zfpxQd9eQorwovtyjXHyAU6LRr3mfXsMMGCiu1sCrOI2eH_TzzmjJbGR05b00YexM3ZamwOGfCqIleZ20=', start_index=14529)
Annotation(end_index=15725, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnNPQMU_BI9tQST68_wovrqctsVbPhIzUMahIElJay8F3MwKMVBBZ5YzA2MpfyWR-gOklZm-K3AYTreuw13161OIkEqt125ImGaikgA3l2AQHTeQHT1WOxb5jT_TZ1q240FgJFlHjE', start_index=15716)
Annotation(end_index=15748, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8Sf11K2BynTpugd28F9Vq8tmGBgLevgXJp3p6dbKSCMoyWCIE4gKo2rthOwSpbhUVLRKafQclBXlA9UbdAHOI50ZKvlj9VPJwNqM61ieA0VN_-dULEbURAGldCLuO94vAY7OZPOF_OUg9URATjg==', start_index=15738)
Annotation(end_index=15767, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnjaJL4dg-Uyi10hU0yMKljYYRHQyCpZjZFupioqT2ZpUrldUNzXh1M-zfpxQd9eQorwovtyjXHyAU6LRr3mfXsMMGCiu1sCrOI2eH_TzzmjJbGR05b00YexM3ZamwOGfCqIleZ20=', start_index=15758)
Annotation(end_index=15789, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkC4HqdJp54YKWOukzUyoMgH7a7O-NOG-R-KZ-Ojr803yueVQ_7JEVxEGs0cZoWhGCDviCqiadJ_7R9oSjdtoN2b41hbql0gCEsncOoHvaatE6CaEWAkq76BW_0e5udr66BeA1Ek47', start_index=15779)
Annotation(end_index=15812, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuyAnSfgyhB4wbdzexR0YdaZ3Y7WrTvgCSthPDr-qc-MATumMuWeaVOQ8S4hhRedujQODaFhJYwXsZJBkT-Hz-eVvysWLySakRq7Ph-aVFUW_aXo0LQRwHBR-WUUWKuI0eTB7EpZI=', start_index=15802)
Annotation(end_index=15834, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFB6BQmdnEVqGMsXYO90XqUlHcGPn3RNEUWY-dD2G-9AsNllArxyOTwI-KcpsM0C1AdpgrGusT7vIRdFolM_wknUOBf0fwn3Av_JseNRDGS2VsU88aS0cWA42K52xYrV8bEqNAzErQ=', start_index=15824)
Annotation(end_index=15856, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGf-2xjyFuU2DtP4E_oobb9ss1OACvZbDeOjVIx-ko8iSZQpxJA4yXTARXEjtZNAcQEVPT2R7hZR-nQIQOrj-7eRZJ-s0bN0Mt87S67acYPBZCBUmbJv2fIr0vflgkxA0cIIhSwziY=', start_index=15846)
Annotation(end_index=15877, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHACxA0yRRxG3FaX2dzFUj02oHeyO7xNyguGBJ_5EszCQ5pnfRCIV_4uZXyAtZx_4pEtEvwMFKFyhUbZPMAYt5s2eru4lkTW-c63-ZBHupxU03aTcQ4ym0Li32KtZdR', start_index=15868)
Annotation(end_index=15914, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwP6mxuxx6VhSHLZYHYkR20GbPI69HTq2lh3vwqetsKUge6EHL_XGlwDhxStPensOSwejq6einaqd0j4YSv2wjEzV-hE4n6VG9qLAHD7fINUDfDKijr4pJ7RqIXwMzXVtopQeMtxU=', start_index=15904)
Annotation(end_index=15935, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3jtNYXgYsyNZ2MkEbcX0g27_-kM2HTcq5Hi4o3iVFwk71TIefQ_16MhamlNSq0af-8MW-UKvpO9mHN-Z8KtoExF25OUnUHr4Y6R8GWD2xzj0iTJMCbuGdNO5DA02WCZxNMzcNGSM=', start_index=15926)
Annotation(end_index=15956, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFimfYFsm-VfFbnf6I2xrL2DEyB-yxM6Ewha8lG7xh5SeFUIr4IvlfzBqlh8yh2Q2t7wAPXK3M_53zctDTOzZPzSQcOz9VXr_0jAGo7ayMYDUPJAUn16pAlawfxRHy-l6knkw3XLTkmBDn6izMvoFUAMRXHW5IzEX-j6JztqGCHp9jkFWHICIb79_0sP6s0iPTM9GT6tyRC-fDwJMevdXiw6v-aESMbTdIpYYP9FiNI', start_index=15947)
Annotation(end_index=15990, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWdPeULhKACEKdE7V589FDmg0akb30AFbWwcpJin83Z4vV6NH04z5NjcpvrARXS3DRNeXQ2JKJ8u1qcsV6mu-eAR3AvaG68Cobm0Hy1ZK0KX3DBeI7tJ8vhRWypmGz0wFR8P2gBDdxqKpCIFQx604CbGLsCNhJkO_nHLlNvnymJmMg7-a_lAZFgcXGnTK5Wuj7I6RwRVfMencmr2bZW2ZzTd2UZi1mm4gso_jLh1VwV2eO95bbYEw3niEStzCV2ms2I6aOD_LmEsw95mV3YdA=', start_index=15980)
Annotation(end_index=16021, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFMGJTFQf36d4Cjn7EpXJgbK1BSj7_nX8rxKpm1uIiMQMCW_9sVU413-lyMQ9iTAVFI4jpw6AlhKUSQLNR_6KHBqUWsFOLZZA03VQI8JdC6NOwynlpFcvo72IdEIDeEn-Hp4Q4ZKv20g-L2fVDq25rfm4W42iefnNyGVkLyRGI5oTBbvNfcGwCq0e8Ybi0jivzTB1Trn32RhZBvo1aG4YtORzVciCZGeuAwGMUIi4IQ9WOWjIY9wdRqy7lGzajUsTuNg==', start_index=16012)
Annotation(end_index=16055, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpcpO2KexLf2G56YuLx-ELSybQa38X2pb-njCaEv89kbOhcHm4q1nFF9rClHNbGdpVkYC0vqBuZU30vV46eU5Fa8mgYsVc3CZtucyVE8_oRhwd71N9G7ffX7tg7QUCkCWPrXu1L7k=', start_index=16045)
Annotation(end_index=16076, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHACxA0yRRxG3FaX2dzFUj02oHeyO7xNyguGBJ_5EszCQ5pnfRCIV_4uZXyAtZx_4pEtEvwMFKFyhUbZPMAYt5s2eru4lkTW-c63-ZBHupxU03aTcQ4ym0Li32KtZdR', start_index=16067)
Annotation(end_index=16113, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSnrPW8onPZ9aG5KhUCjT1BYEixhVVs_Yf686ju_AnUx5Z_FNlP2HP0DAY3QUWTtfidf79yfwzd-nyDF5aySRWzpv47EnHc0ri6aCoozbjN5UtQTxvr7hKNOCEwawH6JP-de5f-Prgpe-cGmVusJqT1kpCrW9M3r43KQXI9bi5-zkfvWhbToM8E9e3NoFvLPHmrWYd1qGSZkbcX0gHQdPHhnyYJEvgfetLQGvL6jp1cr03Jw==', start_index=16103)
Annotation(end_index=16147, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuKNMhhqG1vjwFR7zjM88Ex5RUQESAYqvom2w5avyncee28tjbgLAeTAHu66O2sMqEyagevNIYmJAvBOPGMBJ2lvXjPw9Z5370TNghDcoaIT0Twn5aJlRQMcqh3tUFus_SqMA7vph8', start_index=16137)
Annotation(end_index=16170, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2h3lKPhyicJDQWorW_yQYj711ppx4tWhccc2gFf7AwSC37TYuyxW-pC__OYWszK1J2IeodkWQBGzDZ5fSgsC6QQisc2IOxbJ6VPuQ5tb5HXx-ecFP5XTLEUejA4-x2qUgFZ5uBp3ODO5IdiKjqJBibedOU9DIWlyMXIoHJ6bAB7uoiQjfFsjuWa_TeQX2i9W6twnbex8r90U9UanMKod6EEWb0emrLpzYFjC37Wb_tZp-d6JAfGLbgGH9NG_bB770eT9R_1OIPAspyiSZwzb0MLL8y0l0zzFFiO4XNFjiSu47xGOIqmOBRCzG588RYVmXw47tLoeglxP74q_Y2duXgbs65D1lNK0sZ_5-5NE3uIP3Fht9fYKblbDdrm7d', start_index=16160)
Annotation(end_index=16204, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZ_siJg8eV2WhKiOqEyM2k8a_4Ueek0dGckQS4uvU0C_AUL3ja0hD57x3M2iJzwzWmEYDIy54T4cNCpXjk8rK8AhGptcyLeu64FkSXctaPdbmAB3Wy792o3JVxsLR3yTRp60YAJ2DhahP7tmAGW1YXOIhkkOasVdX9UkR6reU7NddV2XvZcZJjPHC8yM51hKWUmXlbVCxWdpYI09gQElaD34oJrmLP69Dl39a3m8qoU91jVxqBubt0xU6IF2j_bu2vqmishFvKP0SaVBZ8SHEOHKNbJxSbht-_NCgqh5f44NtiSEHSkNI=', start_index=16194)
Annotation(end_index=16238, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFx6B1NhtvEHt28_zyCUGuI12RtAnIATcswaTBeQYYsfchaxqTClWgbCFCt6LHQlq3vcvQ-s_y3CXLJH5PA7AgBwNu_iaKkk_MB6G-pBmK56qw2zbvJIBONKZ96-t8=', start_index=16228)
Annotation(end_index=16274, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFisOpYiGY72Ry6xKghhHrG4ynVFwcZ872fBZ8pNOEL5k62hPihmFnaV2aACcsMWhmlOdmmHYwCYwTjPWORX8M7NDCqhegN2WBgsHD8vOz0XobggIJ33EVGRrEOwbAoFb8yWZFuJHQ=', start_index=16264)
Annotation(end_index=16296, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqk9jaPkQ8qL6Qp56DeTtRTZTkSUORCR5eIA3XwG5f3Kv4GDZP1tX1jMXCypq79zmUeiO9MXMsj-cwna0eFFu_cuyhaw2Oay9K6G4YJqkDdar3qz7XOF8twN317dpzgw7qc9iHXNpvar1hwtOkPw176Spgc9eGKqLODLZ-UAt6NUKMxMXjWCukbIKyr04pAv69idk1WH7OlZHtJBzE2yAiEtnr', start_index=16286)
Annotation(end_index=16344, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzAVAWCpo22tS6lilHtXfw-GaoYztyc-UQvewScU3ThoIBwMGTlGWN_OLqD9dogQg-pcFk0EobJ326CjmfFPoIGYtEw_h1UGXp1AtaEzdjeAOkKz8Uif_MWHwc0q_ZK44bdnN5wgI=', start_index=16334)
Annotation(end_index=16366, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0K8OIPrrMgUE8COxDFW5Z3RLSFxvdrxZnVPJwPDSqHvNsMJSUDaajlGlVu7uYq3OCX0Sr5wZiyHwHEPMW_A6GgrAB2QG3_Y74-8ouCSb6sDvz8XiUiTuGilmQXwEHHyRxZg5OqAzD', start_index=16356)
Annotation(end_index=16388, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnNPQMU_BI9tQST68_wovrqctsVbPhIzUMahIElJay8F3MwKMVBBZ5YzA2MpfyWR-gOklZm-K3AYTreuw13161OIkEqt125ImGaikgA3l2AQHTeQHT1WOxb5jT_TZ1q240FgJFlHjE', start_index=16379)
Annotation(end_index=16410, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGE0mSBID0h-zpt_U5eUP1JMBtDOU2ixjCrAzQOgl188V7KOEqaLbW4IQDqMwg7uBoA2LOTVdqkzw8G31hQML7zNXiOm--WTn_i1yEKS9pHltumjfMNvY1jIfzd047UyWvm9_EnIyL1QJYrdmTELS_3_Hc9', start_index=16401)
Annotation(end_index=16436, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4Kr3OC4SuvFeGB16WywmSavjxryzM6vEq1vNLxYSX7QOYvV2I8-TjzfMWbftphYDcU9JpyG_rDndiopRvAcLmMV-fLtSCXu6RGTkWWa0HUKRLSbiZeKAN7npKtL8hRLA6nOd5myc90RarWsR5jP4ipDFIu6MPCitAYF9EkypBBBoffFdEAD9_VSzPMLV4DlDFZK909-d0olkA_cELC0haxndeyMoMakWtc6ub2QM44e0npodYD3tcZBgpFA3SS--FGkezSLs75oWk', start_index=16426)
Annotation(end_index=16469, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFa9J-b6U-cBdpnbFnlQCvuj1lu_U-_tcSzVnui9cPzeQKffaqAhzWd1oOFKvNz1wK3WKXEkcmeRKMnuGzakLBcx7P3K7J2fqH8Tgvy8J3Sr6i35Kidby8XtvbZfOMT4cyLtLHYCmWFUu8QQr6iKFdff96avPLOeS6YpjQ_qD1WhXc2I5XaQC998REK1nAK5WHAtaJfn_7TZmnsAaO09gInG4wX8r0HMxM-HNPbxgQhaEaFKJPFEt1mfP03T4xgSbndMTe9cq8HRJyRXP4YphXPWSQ56AFKrC8ganZHNM03z7wAP91oDAgM-Gf5afzzxleY', start_index=16460)
Annotation(end_index=16504, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEr4TjKmWvvIRGlQ9R_slC4bs-BFVcD-fiVPDQA3slrpxYBjk56bcsTYn0sxUHOOqrJz71bLNqNPWm4k19COhRAlQ9ffLLqIcLns8tliLkwUd-nJ_kaIq4s8Cu-fgyYVh8mNDxOAic=', start_index=16494)
Annotation(end_index=16526, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKm5avFrOLwhrk-f1YxLmCl29Q0QbBvwD05G774psMu0ITNsbaO1R6GftRIQ4YJjEc83krjma9Lzn0hjR_SMDHxp_a-8KljjrWVsO7s5nLoNDDSfU7bzutmuiD7OzhK8w=', start_index=16516)
Annotation(end_index=16547, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHACxA0yRRxG3FaX2dzFUj02oHeyO7xNyguGBJ_5EszCQ5pnfRCIV_4uZXyAtZx_4pEtEvwMFKFyhUbZPMAYt5s2eru4lkTW-c63-ZBHupxU03aTcQ4ym0Li32KtZdR', start_index=16538)
Annotation(end_index=16584, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQ6QTKhfLMcbM1ZFZGem0D-HYS3VhjX_jPTU-fqADNGGCI8_jllGe0y1V6wk-Rv6Ey84TQuV9-Rf_Kr-Kbx1I-Wcuz-_OtnFWTG7RNAuToESUjaIop8E7L0XYOBqA6aC_vEbzFHyQa', start_index=16574)
Annotation(end_index=16607, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhdrNas64Y-NEpZrtpQnKyrVYBQdGT933QMM68a2Oz_WA2i9-KPDFMd6KOOUcGoZsVt4H7fOCLq9mH31iELAhasq0cW00obTMIWs-QYNOr9CbrF-YOYXVar0iwbnDTAnEHKQQbfDmhH5pCP2qTxk1vrWxtN4beSdYzWSm2VfnHJ8VkaA==', start_index=16597)
Annotation(end_index=16642, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCgJCXw9W_xzXjiMvPpKkDJYmVO6ULsKYLMPYHKWvjIgkzAU89xMw590kQJ_52bEDhQmvoN5rEJUfZHc_A7rmf9SCpaY0fM5wZ4xjKqFwfU6HmtUsNKOkqNW33NxYI', start_index=16633)
Annotation(end_index=16679, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYtAL9sFbRIGGUOKDNtAYJlmTqlzxGeTvTP2IHBIBeuU-XVbdQ-9GT4lmqXxWb8ljlkhArvOZCqwcT-yTUW_eEKw6X49XGV4PaCEiUxFs2-DJsAEtwr9VMoO-lL-Qk', start_index=16669)
Annotation(end_index=16706, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-VwpgS4xFbjvmQMl8AcImkfcCdpFQWDxRLmmbrYm_llCW8MMpP8VyiSl5lqc4RsAQCNsqDXXAYREitpHh2XCbGRnlMp1cFORHtvphlP-laxgC1IIo8_UHr3I_5_ySr3eM5FSPDQ==', start_index=16696)
Annotation(end_index=16736, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELC2k07vJVKG4JUHSlgs5OjIdjmkvxL8lAP3qW6AvsuVLYAAcYhdkW-ium5mmBY7n5ZvUueB2jtF0exwNLkRrxrAMtfIZjjGdpCaabfBmW5ChLn6mgEwMyL7nVQ6C1Ev1D0T6YGIHD066NdvY3E-pM1DfRAciplk67F2NLlZ6HKFcfdJ3pHyg5HBRSmn3lVvrfp-kNjW62qLaqo8koda7SK5pSuas=', start_index=16726)
Annotation(end_index=16779, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0K8OIPrrMgUE8COxDFW5Z3RLSFxvdrxZnVPJwPDSqHvNsMJSUDaajlGlVu7uYq3OCX0Sr5wZiyHwHEPMW_A6GgrAB2QG3_Y74-8ouCSb6sDvz8XiUiTuGilmQXwEHHyRxZg5OqAzD', start_index=16769)
Annotation(end_index=16802, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELqmhhF8KF3RjXiRRz45ZB3_LVRPm5cx6B-FaMDawvLks8xGxJPalRXEFYp62Do2c837y8E6ZR2Ns5p9J2OZzRb-xXwgedxSE-t7SSzbdxZcFLlO_sEQB7jP5T', start_index=16792)
Annotation(end_index=16836, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEys_yNT2hLOsQAXkksxKykYGK8eVIXzlsfcMHVeV1rOx1VO4s-bOFl2l3TrK5xnRqzzir2AcchFdDYt-7jk57WOb6k_EIBdUQU5IknyrD3nkABHZtG5HAwarhtL_YXg7jj0DGWCRzhcxDc3mmoaBOqO4c-B8KZQZq9Z6U1YeIggG5Z9-QOD7GFzkvwQxMWg-08TBCq8bgZWgtEIXvGiwQcnykmf2fN7MgpDvRMCSgCyfZK8vJ4q2kL-rutdC2DeTMgfkjgkOcPatkw0GLmxDupT_1gLB1wBCxXeQ==', start_index=16826)
Annotation(end_index=16870, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEUZQKSnLo9_qkcj3r6ibW-h_cnmQmJv4WHJenS-GCN6UjcE-r0LdODQqqQyS2yaWF_qIkbcok-TdprrP6vriafusHCgW0eA65MRygZeiG3Vyr9EdsF_8t6F99jl8G9Jk4g4V0akNzRzFSbC9G71KwJfjqlAXsKZv6BQ==', start_index=16860)
Annotation(end_index=16898, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuKNMhhqG1vjwFR7zjM88Ex5RUQESAYqvom2w5avyncee28tjbgLAeTAHu66O2sMqEyagevNIYmJAvBOPGMBJ2lvXjPw9Z5370TNghDcoaIT0Twn5aJlRQMcqh3tUFus_SqMA7vph8', start_index=16888)
Annotation(end_index=16921, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIQqJbGgH0cEkCTlP49dxZwvdh1i6AltorjYnCYD4zSgFqAnhseJvgvEcqNacwAeaTLnqGxKKZuEeNWWGWix2cDLc9idztbWzseT6RRN3evrZdI5f93ZMjWXE552t0r3M14BsbsUhZQNuAYjNv6ka5Gv1fFl76fgb0q9tH7p_q9g-FxMIU5EofWPYoj7KTZsqZx2vaTYPp9RdA3GS4UNzkRYXaDLL8zehMOD8D9nXPbUsE4khJYzOdx5cDEmU=', start_index=16911)
Annotation(end_index=16955, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLo9Jji6FBd851QK92Zk5JT1epF-bTGpZAhrlOq2OfF-AED1d5z1NkeE0Ft1aPN02gBDS_8C7lyV7-hrzQZRvKT4UNTziRqrbORIrKsLjjwX5Gn7c6NAjPM2kjGrVyG-eYWGcQdQpyjMjpMsPev5neRcmFdNDmfXqXqEW9b77qQloy-VkhFKr9b-y7ViZQuT72krWybgrF56gMQOPJfqTwFRO-LrN2DdDhI3bAmIn6vgfZBUD7luxdF8sxiZ1ePRWUXmLT5RC9bzjVR48mml4sd2i6-b6-3DZJTNAsyyP6NL2nqXXatLqoyRc8Nn0-Rcy05AzD-xdSl6erOe1UnHPzPQ==', start_index=16945)

## Sources
