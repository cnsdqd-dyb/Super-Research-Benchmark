# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** ceb97e64 | **Time:** 326.01s | **Cost:** $1.09698
--------------------------------------------------------------------------------

# Comprehensive Analysis of Ablative Thermal Protection System Designs for Coupled Aerodynamic Heating and Structural Thermal Stress

### Key Points
*   **3D Woven Architectures are Superior:** The research indicates that **3D Woven Thermal Protection Systems (TPS)**, specifically **HEEET (Heatshield for Extreme Entry Environment Technology)** and **3D-MAT (3-Dimensional Multifunctional Ablative Thermal Protection System)**, represent the current optimal design for handling the coupled field of aerodynamic heating and structural stress. Unlike legacy 2D laminates or honeycomb-filled resins, 3D weaving provides through-thickness reinforcement, eliminating delamination planes and allowing the material to carry significant structural loads while ablating.
*   **Structural-Ablative Integration:** 3D-MAT was explicitly developed to solve the coupled problem for the Orion spacecraft's compression pads, which must serve as both a load-bearing structural interface and a heat shield. This design demonstrates the highest capacity for managing simultaneous mechanical loading and thermal recession.
*   **Mitigation of Brittleness:** Traditional high-efficiency ablators like **PICA (Phenolic Impregnated Carbon Ablator)** are brittle and prone to cracking under structural deformation. The development of **Conformal PICA (C-PICA)** and **PICA-Flex**, which utilize flexible carbon felt substrates rather than rigid fiber forms, addresses the structural stress coupling by allowing the TPS to comply with the substructure's thermal expansion without failure.
*   **Legacy vs. Modern:** While the Apollo-era **Avcoat** (epoxy-novolac in fiberglass honeycomb) effectively manages char retention and prevents spallation through its honeycomb reinforcement, it is labor-intensive and less mass-efficient than modern woven solutions. The shift is toward automated 3D weaving and additive manufacturing to improve reliability and reduce the "touch labor" associated with legacy designs.

---

## 1. Introduction

The design of Thermal Protection Systems (TPS) for atmospheric reentry vehicles is one of the most demanding challenges in aerospace engineering. It requires a solution to a multiphysics problem where extreme aerodynamic heating interacts dynamically with the vehicle's structural mechanics. This interaction is defined as a **coupled field**: the aerodynamic flow generates heat (enthalpy) and pressure (mechanical load), which induces thermal expansion and degradation (ablation) in the TPS material. Simultaneously, the underlying structure deforms under inertial and aerodynamic loads, imposing strain on the TPS.

Historically, TPS design treated thermal and structural requirements as separate functions: the substructure carried the load, and the TPS managed the heat. However, as missions target more aggressive entry trajectories (e.g., Mars Sample Return, Venus probes) and seek greater mass efficiency, the coupling between these fields becomes critical. If a TPS material is an excellent insulator but too brittle to withstand the structural flexing of the aeroshell, it will fail catastrophically via cracking or delamination. Conversely, a mechanically robust material that conducts heat too readily will fail to protect the payload.

This report analyzes the state-of-the-art in ablative TPS design, focusing on materials and architectures that best handle this coupled environment. It contrasts legacy systems like Avcoat and PICA with emerging 3D woven technologies (HEEET, 3D-MAT) and flexible ablators, establishing why 3D architectures are currently the superior solution for coupled thermal-structural environments.

---

## 2. The Physics of the Coupled Field in Reentry

To understand why specific designs are superior, one must first understand the failure modes induced by the coupled environment.

### 2.1 Aerodynamic Heating and Ablation Mechanisms
During hypersonic entry, the vehicle's kinetic energy is converted into thermal energy within the shock layer. The heat flux ($q$) impinging on the surface can reach megawatts per square meter [cite: 1]. Ablative materials manage this energy through a sacrificial process involving:
1.  **Phase Change:** The polymer matrix undergoes pyrolysis, an endothermic reaction that absorbs heat.
2.  **Char Formation:** The material forms a carbonaceous char layer that radiates heat away from the surface.
3.  **Blowing/Blockage:** Pyrolysis gases are ejected into the boundary layer, thickening it and reducing convective heat transfer (the "blockage effect") [cite: 2, 3].

### 2.2 Structural Thermal Stress and Mechanical Erosion
The "coupled" aspect arises because the TPS is not a static insulator. It is a dynamic structural element subject to:
*   **Thermal Gradient Stress:** The outer surface may be at 2000°C while the bond line is at 200°C. This steep gradient causes differential thermal expansion, generating massive internal shear stresses [cite: 4].
*   **Pyrolysis Gas Pressure:** As the resin decomposes, internal gas pressure builds up. If the material's permeability is low, this pressure can exceed the material's tensile strength, causing "spallation" or explosive delamination [cite: 4, 5].
*   **Aerodynamic Shear:** The high-velocity flow exerts shear stress on the char layer. If the char is mechanically weak, it will be stripped away (mechanical erosion) faster than the chemical ablation rate, leading to rapid recession and potential vehicle failure [cite: 6, 7].
*   **Substructure Deformation:** The vehicle's backshell and heat shield structure flex under aerodynamic pressure. A rigid TPS bonded to a flexing structure experiences strain. If the TPS strain-to-failure is lower than the structure's deformation, the TPS will crack, creating a path for hot gas to penetrate to the bond line [cite: 8].

---

## 3. Legacy Architectures: Strengths and Limitations

The evolution of ablative TPS has been driven by the need to solve these coupled stress-heating problems.

### 3.1 Honeycomb-Reinforced Ablators (Avcoat)
**Avcoat 5026-39**, used on the Apollo Command Module and early Orion designs, represents the first successful attempt to engineer a material specifically for coupled mechanical and thermal loads.
*   **Design:** It consists of an epoxy-novolac resin filled with quartz fibers and phenolic microballoons, injected into a fiberglass honeycomb matrix [cite: 9, 10].
*   **Handling Coupled Fields:** The honeycomb is the critical structural element. It reinforces the weak char layer, preventing it from sloughing off under aerodynamic shear (spallation) [cite: 5]. It also arrests crack propagation; if thermal stress causes a crack, it stops at the cell wall rather than propagating through the entire shield.
*   **Limitations:** The manufacturing process is extremely labor-intensive. For Apollo, 360,000 honeycomb cells were filled by hand [cite: 9, 11]. Furthermore, the honeycomb structure is relatively heavy and difficult to scale for very large aeroshells without introducing seams. While effective at char retention, Avcoat is less mass-efficient than modern carbon-phenolic ablators.

### 3.2 Monolithic/Tiled Ablators (PICA)
**Phenolic Impregnated Carbon Ablator (PICA)**, developed by NASA Ames, revolutionized TPS by offering much lower density (~0.27 g/cm³) and higher thermal efficiency than Avcoat [cite: 3, 12].
*   **Design:** PICA uses a rigid carbon fiber preform (FiberForm) impregnated with phenolic resin.
*   **Handling Coupled Fields:** PICA excels at the thermal aspect but struggles with the structural coupling. It is inherently brittle with a very low strain-to-failure [cite: 8].
*   **The Tile Solution:** To prevent cracking due to substructure thermal expansion, PICA cannot be applied as a large monolith. It must be cut into small tiles with gaps between them [cite: 13, 14].
*   **The Gap Problem:** These gaps require complex fillers and careful design. If the vehicle flexes significantly, the gaps can open or close, crushing the tiles or allowing plasma flow-through. This necessitates a **Strain Isolation Pad (SIP)** between the PICA and the structure to mechanically decouple them [cite: 15]. This adds complexity and mass, and the gap fillers themselves are potential failure points [cite: 16].

---

## 4. The State-of-the-Art: 3D Woven Architectures

The current "best" design for handling coupled fields—where high heat flux meets high structural load or shear—is the **3D Woven Thermal Protection System**. This technology addresses the fundamental weakness of 2D laminates and brittle monoliths: the lack of through-thickness (Z-direction) reinforcement.

### 4.1 HEEET (Heatshield for Extreme Entry Environment Technology)
HEEET is explicitly designed to replace heritage Carbon Phenolic (which suffered from delamination) for extreme entry environments (e.g., Venus, Saturn) [cite: 17, 18].

#### 4.1.1 Design Architecture
HEEET utilizes a high-density carbon fiber outer layer woven directly into a lower-density insulating inner layer (blended carbon/phenolic yarn) [cite: 19, 20].
*   **Mechanical Interlock:** The layers are not glued; they are integrally woven together in 3D. This mechanical interlocking eliminates the plane of weakness found in dual-layer tiles or 2D laminates [cite: 17].
*   **Resin Infusion:** The woven preform is infused with phenolic resin to create the final composite.

#### 4.1.2 Performance in Coupled Fields
*   **Delamination Resistance:** In traditional 2D tape-wrapped carbon phenolic (used on the Galileo probe), thermal shock and gas pressure can cause the layers to separate (delamination). HEEET's 3D weave prevents this, allowing it to survive heat fluxes >5000 W/cm² and high shear forces without losing structural integrity [cite: 18, 21].
*   **Mass Efficiency:** Because the insulation layer is integrally woven, HEEET eliminates the need for a separate adhesive bond line between the recession layer and the insulator. This results in a ~40% mass savings compared to heritage carbon phenolic systems [cite: 17, 20].
*   **Structural Robustness:** The 3D architecture provides higher shear strength and impact resistance than PICA, reducing the risk of handling damage or in-flight mechanical erosion [cite: 18].

### 4.2 3D-MAT (3-Dimensional Multifunctional Ablative TPS)
3D-MAT represents the pinnacle of **structural-ablative integration**. It was developed specifically to solve a critical failure mode in the Orion spacecraft's compression pads [cite: 22, 23].

#### 4.2.1 The Coupled Problem
The Orion compression pads connect the Crew Module to the Service Module. They must:
1.  Carry massive structural loads during launch and pyroshock separation (Structural requirement).
2.  Withstand the extreme heat of lunar return reentry (Thermal requirement).
Legacy 2D carbon-phenolic laminates used in early tests had low interlaminar strength and required metal shear inserts to carry the load. These inserts conducted heat, creating a thermal short circuit [cite: 22, 24].

#### 4.2.2 The 3D-MAT Solution
*   **Material:** Quartz yarns woven in a 3D orthogonal architecture, fully densified with cyanate ester resin [cite: 19, 22].
*   **Structural Capability:** The 3D weave provides exceptional interlaminar strength (shear and tension), allowing the material itself to serve as the primary load-bearing structure. It eliminates the need for metal inserts [cite: 24].
*   **Thermal Capability:** Quartz is a robust ablator. The material functions as a heat shield while carrying loads that would crush or delaminate standard PICA or Avcoat [cite: 23].
*   **Significance:** 3D-MAT proves that with 3D weaving, the TPS *can* be the structure, offering the ultimate solution to the coupled field problem for high-load points.

---

## 5. Flexible and Conformal Designs: Decoupling the Stress

While 3D weaving reinforces the material to *withstand* stress, another design philosophy seeks to *avoid* stress by making the material compliant.

### 5.1 Conformal PICA (C-PICA) and PICA-Flex
To address the brittleness of standard PICA, NASA developed variants using **carbon felt** substrates instead of the rigid FiberForm [cite: 15].
*   **Mechanism:** The felt substrate is inherently flexible (compliant). When impregnated with resin, it retains enough compliance to deform with the underlying substructure.
*   **Coupled Field Benefit:** This compliance eliminates the need for Strain Isolation Pads (SIP). The material can be bonded directly to the aeroshell. If the aeroshell expands thermally, C-PICA stretches rather than cracks [cite: 15].
*   **Application:** This is ideal for large-area heat shields where the primary structural load is carried by the backshell, and the TPS needs to accommodate that movement without adding the weight and complexity of tiles and gap fillers [cite: 15, 25].

---

## 6. Integrated Thermal Protection Systems (ITPS)

Moving beyond ablators, the concept of **Integrated TPS (ITPS)** aims to create a single structural panel that insulates and carries load, often using sandwich structures.

### 6.1 Corrugated Core Sandwich Structures
Research into C/SiC (Carbon-Silicon Carbide) sandwich panels with corrugated cores demonstrates a method to integrate functions [cite: 26].
*   **Design:** A load-bearing outer face sheet (CMC), a corrugated core for stiffness and insulation (often filled with fibrous insulation like Saffil), and an inner face sheet.
*   **Coupled Performance:** These systems are designed specifically for the coupled field. The corrugation allows for thermal expansion while maintaining high specific stiffness. However, these are typically non-ablative (reusable) and limited by the maximum operating temperature of the CMC material [cite: 26].
*   **Hybrid Ablative ITPS:** Recent studies propose embedding Phase Change Materials (PCMs) or ablative fillers into lattice-core sandwich structures to combine the load-bearing capacity of metal/composite sandwiches with the thermal management of ablation [cite: 1, 26].

---

## 7. Computational Modeling of Coupled Fields

The "best" design is often determined by the fidelity of the simulation tools used to validate it. The interaction between fluid dynamics and structural response requires **multiphysics coupling**.

### 7.1 Conjugate Heat Transfer (CHT) and Fluid-Structure Interaction (FSI)
Modern design relies on coupling CFD codes (like FLUENT or LAURA) with Finite Element Analysis (FEA) codes (like ABAQUS or LS-DYNA) [cite: 27, 28].
*   **Loose Coupling:** The CFD calculates heat flux and pressure; these are passed to the FEA solver to calculate thermal soak and structural deformation. The deformed mesh is passed back to CFD [cite: 28, 29].
*   **Mesh Movement Algorithms:** To accurately predict performance, the simulation must account for surface recession (ablation). As the TPS recedes, the shock layer shape changes, altering the heat flux. This dynamic feedback loop is critical for optimizing thickness and preventing structural burn-through [cite: 27].

### 7.2 Modeling Mechanical Erosion
Recent advancements include models that specifically calculate **mechanical erosion** (spallation) based on the shear stress at the wall. This allows designers to select materials (like HEEET) that have sufficient shear strength for specific trajectories, rather than applying large safety margins to weaker materials like PICA [cite: 4].

---

## 8. Comparative Analysis of Design Approaches

The following table summarizes how different TPS designs handle the coupled thermal-structural field.

| Feature | **PICA (Standard)** | **Avcoat (Honeycomb)** | **HEEET (3D Woven)** | **3D-MAT (Structural)** | **C-PICA (Flexible)** |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Primary Reinforcement** | Rigid Carbon FiberForm | Fiberglass Honeycomb | 3D Interlocked Weave | 3D Orthogonal Quartz Weave | Carbon Felt |
| **Structural Role** | Non-load bearing (Insulator) | Non-load bearing (Insulator) | Semi-structural (High Shear) | **Load Bearing (Structural)** | Compliant (Non-structural) |
| **Failure Mode** | Brittle Cracking / Spallation | Char Spallation (if unreinforced) | High Shear Strength | High Interlaminar Strength | High Strain-to-Failure |
| **Coupled Stress Handling**| Poor (Requires Tiles/SIP) | Good (Honeycomb stabilizes) | **Excellent (3D Interlock)** | **Superior (Structural Composite)** | Good (Compliant/Flexible) |
| **Mass Efficiency** | High | Moderate | **Very High** | Moderate (Dense) | High |
| **Manufacturing** | Machined Tiles | Hand/Gun Filled | Automated Weaving | Resin Transfer Molding | Impregnated Felt |

---

## 9. Conclusion

The thermal protection system design that best handles the coupled field of aerodynamic heating and structural thermal stress is the **3D Woven Composite**, specifically exemplified by **HEEET** for acreage applications and **3D-MAT** for high-load structural points.

*   **Why 3D Woven is Best:** It fundamentally alters the material's anisotropy. By introducing fibers in the Z-direction (through-thickness), it eliminates the delamination failure mode that plagues 2D laminates under thermal shock and mechanical load. It allows the TPS to function as a unified structural element rather than a fragile coating that must be isolated from the vehicle's structure.
*   **The Role of Compliance:** For applications where the TPS does not need to carry primary loads but must survive large substructure deformations, **Conformal PICA (C-PICA)** offers a superior alternative to rigid tiles by utilizing material compliance to decouple the thermal and structural fields.
*   **The Verdict:** While legacy systems like Avcoat and PICA have successful flight heritage, they rely on complex integration schemes (honeycombs, tiles, SIPs) to mitigate their structural weaknesses. 3D woven technologies solve the problem at the material architecture level, offering a robust, mass-efficient, and structurally integrated solution for the next generation of reentry vehicles.

### References
[cite: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

**Sources:**
1. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjZuER4HtPs2ucnB3wXMnd6IvzcwT2EamweOG1wR0m3ZO6CAPGznZEb2Wn_aGzeeRuaF5CzkfF_bNFiNO0TGem19aS3_OzJCPlvZnUGDTvyUptdURxHZ-5Wb6ESXnCqgpuOfA3v8zffb6QuFhYn0opd_am1cUMF_gGDD_qxyrzdxGn4w2tVZAsZTABU7quuWggWVXuqqbDQrEeF53fTVOy9OusnM2qQr_NxXFjlwA_SjRkOwq1lccZgMFybbVPpsZpByQLLgK_paqvg-Qm8rxTdSfIaSQ=)
2. [sjsu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDm7a6FuFFEm3pwy8DBY5fF594-qRdkiX27Tvik2m4jBbWMKtLDzs9jZUmwSUXgsNCaOvX93wBheBgFCKBqIUwQNlRkF8LkuiumpwQQ_WhBvtUZIEbkS5p_b_3AdyJdmfEaewJS834sPQmDNmB6weyuwL_uSSuIGzd)
3. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEartVCyKdDRid06b6C4Z-fLAWK5LGL-nE2qP4iqnr9YSuaCXdbck9_Z2GY4vYI8X45GzNsMvoCZTfDZzp8lO84uPhtvWCDTYOBObrzqMBQrTGehIuX6wVkg-ORNw_Fj2kjUfFJ)
4. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJopW3wW0a4MXctCW0VWIKyjEcHOBMZoL4G6Z9YkU0PSnnQSou9-vzbnZNErRhOvrcXnnJ5Qev-rf3e-7E8_KO58SN6YvZnsHGtf_8_sIvxkXp4UQ1vsZoEOTP5hMvg-1o3MUGQVHlcRGTZrU8Z4heJrqVQRdOn2aeA9_Unx9eosSiOcPffSM9-fV0N0y5SJ5XZ-It_SXjfbvyqR6Xe6gUqzwhSux976_Z4pnbc8Nn613LDKP5aiEBfeId)
5. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_5FKK9PsLnQaHeSSanvEwq_sjkl014_jmUtVBAg19sb5NjnpJ-l2NaoHyeBS9A91IuDQjFiZ4AEQ3xVuGVcFyl1PBs7zEZf6mzjtmMY5A21D1paMltxWpmGF8v2MgBkIKLYqVR750HDS7Mgj8z5L-E7wqrKSUXjtQ7p4BKlo=)
6. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAlh6Yu8SgD6KWiaZS2qVeGiBtRVxnpV0jF2uYJWhtl-rg-G8wAz88oOCKto1D6gHSmf-8XDod0V3tFOqKnZElYKh37JpmycoUR-AfWQw1znuj2okBTLuXPG041rD55OCm2trJ3hsFBiG_CNC9oZJa3YSlylaY3XNYjcg5XaM=)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjIbtO1VFSXU8C3eZydF1q6hKjBDYHt5bZh7sSYxjln7W_exOCK8BeQl3HDzbupDJ3NwvGSomlOh-AT2zX5PO5AdGEMXpGRXoj3QhZsbXAI5z1SRyYfgaY5ObZt6wje-PpzQmcCY8wBIu8vBLWgVxwevP2UK-M9ANvU4xfSO0TmsxRxmC4y85ZPnUp3mRlcY4X0IOq7G6g3HV5dukb8Xslqps=)
8. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwCMpCf1Jra8bUyeBmcnBB_A7WtzxqLU6NFa8__nBawCDtrcA7SmXbNKo2_1OaD8JKREmlDZo7jwB22BJCQU3PeLSNl_LppTDBepGlaZ6ZfrxxyLI4ygCRWay9-dJCg97SM0XloA==)
9. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEX3jDykzHVDIkr8zbR_5EmEl41PyiqXPvWmPXnbTAHpZDwWkesPdUrJ5CK38swDU09GZBGFCC_EOc-ElgGnXcUOPNJTfPQ-AT-PrgZ7zIZpLzxI9M6fsiJ1fDkmqCD5paGwgQGwshBdjSbi-aMXSHdwyzxXsHdGw36vPmyJeiDoDxoMARypgjXhrq9mbrOQplMopsx)
10. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsaWw3-LeYHMXUuW-c9Dek0J4hepmeczcWynD8Pl0QNrPOs59kE7rIjEl3-ewY_c2x6DOXVdmg1x_m02iXm7AVgSxTxxhjTaIo28NkKleFnw2xqqqSEOyoCIj1mlh-LqrIxmQDfYvUH80=)
11. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_1xXx0CNUmMmz-NO-4EYeAnQErPufpQvFf-B_sIAULfj1pnGeZQU7sEbkTS59zGGkY8eERZm_W7Xj5ay0wzitH7RYPOyp04abzmKLleqQrnVOEyTaMyUppxJ7Y6s8RstRbV7bgJ7L50YiW_cFhqU8TsUSvJMot5uRr-xbH-ljKMeonkkFLyFtOg==)
12. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKbtUmrHyUZD4wOps7zdNH2o96REvLVSFocY8n0z2bApfXE4dj68SymqpuyU2aUEoQ63OnSRJRODayYyWR9waAa3WZZQKWlsuU4Sn3-DOwbEATdyKoCRKD3zO4ql27VOI=)
13. [reddit.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0HKmjhTKAD2n8XQ5sq_fdXAFoQpKy5MOXKk657gLb0UUBRVDJs46iQW6xLl2QrmeG3OBBnJz7y6DI3cfzk4igwFRY8-CbZHcWNGmVtuxm9BXsUfA6OpGwjolsUVLtkseearWt8q08WwemHrlmbGjwAUhkx3g4kYKNtX0Lr3b4KUw=)
14. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTIUQt26CjQwf7XVIkTwLbI1poFyBIa02ECwHzlyL9ZAM6_LE7x28YZ0FnaBoWjKv_B7RReBu3KEAwhwL8_z1t5qb-jY74OOxIzem1U_0ZJEgeiLAzUlyuXMEUKV5KYlPQJ2UGZnMMzjyv9QSAwFqieSnj2Q7gcxJinKcSqs0=)
15. [usu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuS9THqZzkca73pKeuVRdvNmHRjBg5487SmspuhylGZdymMVMnSeevYyRZJtOCeLY6dA7EzFl_gcUx43-cLZMLqxVpTmsVmV29N_uSNPCLSQZPhCV0vvd3wqgABNTIvcp9yZToXm5M_9QOsp0ATTUDpLThWF1MyIaNlQ3G8P00HFNxTTv9)
16. [techbriefs.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECIHGft39kIuIHFR3y5mdOhKfNjNFl5zsi7kRxeZ-Ucdkt-JOqWi0eTkgzhs6BYTEIcnDieRVCM5cABvsjyBEerJKPRE9V0YkXYcyGr_BOpQZAXZ-qpJLrwfZGWdpc8bis1urlxksEdePrV71PvWNwoZJ4Irk2cTXKaQ==)
17. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBPKrMACt5Ihco8OHSe6E7_QZ8GE0kmbpzfN6U02X8603XOnndP5Rp5xorRIBGv0UjGf2nw_vMlNjXTn2A8fQPcCzu4u2tXGvTuy-L1JnrVGc7RcJE31y3G1EMARl63i0=)
18. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUK7KibYTPVMc_82hb96RMERL5IhP78kCWXcYFgOAj204bFHHTeU6utb9asE-rdGoZaIBXw-qvcLxeI5nacAu-1CGLcUP1qsRwdwWQX9beVkA1jZSCTgj7HLLXbar3OLc_34ApVN0hPJkitkpoK1d_WJBqH8c9_59ZafNNQgwMJXxpC08G-_XLhmGjQRLQz9JmRm_J115SojIffg8PeH-Xa32s5F_1yCEFS13IrQ60fi3QpY-IYvi5oH7zSMXWHy4=)
19. [techbriefs.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5HehkfZ1TYnFi9IoszoNcWWWp4sopzEDGW_N9RpQNTvmfHJL_o2MMVD8ixps9lO2rtmapjFaj8Ricv6lmh1yVz_FpdbLDAwHelIsUjEKlm5lj4ab-GVcIDoKxPQmCJd_QiMDG8C0pPnjGHxsMicNa2L8KNzskGEScoVXAn96-C9uxVFsNhzCKcqkfQQB2s9lbkw==)
20. [idtechex.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_TQOCS7866ycbzNs_uVsO96RgbdAVbTgP9T-NyRNTl803j9wika-u3Mzv95m8fL3cpo1FwQZSFc3XN0uLDZQGecycELdsh4fZ8aVMYUZyOO6yzs0cbRvMo45icvJ4CK_QCNwkzLZ0tgRq1HEXbk9cyNgMkgdv7IKPV8vBy0a4ipnFuDOAs9FOK4zNr-eD-G3Mzz7Dv3Znt2k0ya7LAKYNXh7CdK-HF2LYnB0=)
21. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPdh0DiuoSAt9YBH0TR5RabhLrxDXxKodm0NvXXb5WncJE2jA9_ZOat6o_dhcI9Ktq3jIHTEuUqciEgQX-99PFydgAKI47plYESDJgCTQuDdcJgc281AOam6J2YWZH2FaD3ZKt7aN4CKiuAZzMMSiaJKnUsVAG-K3el0iDg2w=)
22. [techbriefs.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFo4EDIqTBS5HiwUgf-cump64XnmM7Z82vuKttEW9_pMzzFvCUcjfsLoigQqNUOOitZFb5sOho1GGi6bsrsabRqoaclkgyLMCGdV5hdoya0O5KLJr8e0mTXFJxZaCfC7hMR5SKQttKZV2e5-t9gl6VATe_5wRFa8URTotk=)
23. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGbvEvhqrdXi-dX7bmfstbYxNGQsqwq73I92I7H5QMQtAYJmZ6PFnKr4iyt0AMOGe_kvubct998ODz47WuoqD7FdD-x0EVGKf4_OcLYRQDqCFcrB953Ybx-zZ9vm7omqY65cishUJKu4Ip6366EUf9p6lXkrw=)
24. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHS6jVpRNhHZuZNQCo6wkmFZC-EYGFQ0veDSoGy2vYygivpX28pCU3GcfYaYBo_34yAVQ-XqipkiOGVejDt9Yc6bjJZ4d1p-q9-NAgnQ1sgNU-2JcoSWBG5BaXIiOotmr8=)
25. [usra.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZEZzU18kItAxev15LpgbajgGvvcWQrZWlQpUbLKEpOCPacX8ENQLPNDWJqPTYaRGutQL_MPYnGEFYEPs7-uQjXfvR8a6I2xUDaMGKMOsF3pSd03BYdH-nOwG7Nv8SQ48hDk_sEbr41BG3HVwkqJrIbw==)
26. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFsJq7KZ-Qg7-1H3Zv3wpwJRgVUkAMHy0KoATx5wicawhV9CFTgpuyPUwTLYKO0JFbLC6Li0eAnrT7a1fJ9-N6d6jWy4TnGS_XmJm99J9fUkUSTV6L8t_4ZqXUCQ==)
27. [academia.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGw4OSv1Hs8uoWEkmdlwhmz9xNfdsEVsE4aoLaj-ySt3hTT5RKlYhTeUmLXo3XdY9jX3BysStbsOI-PXPzam2u38qnQtdpdF2peKitShAO03YusaTYYlEc1rY-M4gQ1XWTiroSsyil8rHT1kyU-5dqR5xQwz4Enn85TM-UpYSfxWFwPlpQSiTTR8CTYQ9ujpD5qq_E2RVTRuZQSHVA9RwPL9C5oltOyFJDx00mE3n4=)
28. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHAndSS30cDeTmyCcbhTU2mxXQze1LiqV_rzSLEeRtlNzdh5Bm7ubuZwHkTLikwlFaFD0d0YlDg1a8ltQkPQ6YKBoPXfoaN9_kiXqyQXJ5C7tUAP0tI3OvpPMPLVg1d58sNTDLd-mVYQU1HLz44XjLBJ_vlzRBVyssVz5J7zTncRmHwjKeKhHV8PwFqvr88OtIj0Z5g3oBhyMbvTDacC-5V2X1dYDcTqp4TB5lEQEy)
29. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG64D4xvuK0x94vk6xfVd5rHX-RRRfXUpk7WGgjyJwTn-TaB-_ebCwcMzHl0Y8Mr6QFijwwNDipLgunAAnAt49qqNlDtZ1w2exNCBuqcrlVOnkhf8BlnFWbhQeHOH0oj_ff-oMFNJ2DyNyv-2qfNLZi3l-RJgJPHibEoN5m57AuDD88ytrR-CQCRqiGKuTWDAmC2qx_cGoH80In5_OkjfxGTJJhVhTAJfysKj_dCDoVNUeuZzCai-kdT52H_1ZC6UiuwdK2gm-G0Q==)


## Annotations
Annotation(end_index=4091, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjZuER4HtPs2ucnB3wXMnd6IvzcwT2EamweOG1wR0m3ZO6CAPGznZEb2Wn_aGzeeRuaF5CzkfF_bNFiNO0TGem19aS3_OzJCPlvZnUGDTvyUptdURxHZ-5Wb6ESXnCqgpuOfA3v8zffb6QuFhYn0opd_am1cUMF_gGDD_qxyrzdxGn4w2tVZAsZTABU7quuWggWVXuqqbDQrEeF53fTVOy9OusnM2qQr_NxXFjlwA_SjRkOwq1lccZgMFybbVPpsZpByQLLgK_paqvg-Qm8rxTdSfIaSQ=', start_index=4082)
Annotation(end_index=4555, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEartVCyKdDRid06b6C4Z-fLAWK5LGL-nE2qP4iqnr9YSuaCXdbck9_Z2GY4vYI8X45GzNsMvoCZTfDZzp8lO84uPhtvWCDTYOBObrzqMBQrTGehIuX6wVkg-ORNw_Fj2kjUfFJ', start_index=4543)
Annotation(end_index=4555, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDm7a6FuFFEm3pwy8DBY5fF594-qRdkiX27Tvik2m4jBbWMKtLDzs9jZUmwSUXgsNCaOvX93wBheBgFCKBqIUwQNlRkF8LkuiumpwQQ_WhBvtUZIEbkS5p_b_3AdyJdmfEaewJS834sPQmDNmB6weyuwL_uSSuIGzd', start_index=4543)
Annotation(end_index=4947, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJopW3wW0a4MXctCW0VWIKyjEcHOBMZoL4G6Z9YkU0PSnnQSou9-vzbnZNErRhOvrcXnnJ5Qev-rf3e-7E8_KO58SN6YvZnsHGtf_8_sIvxkXp4UQ1vsZoEOTP5hMvg-1o3MUGQVHlcRGTZrU8Z4heJrqVQRdOn2aeA9_Unx9eosSiOcPffSM9-fV0N0y5SJ5XZ-It_SXjfbvyqR6Xe6gUqzwhSux976_Z4pnbc8Nn613LDKP5aiEBfeId', start_index=4938)
Annotation(end_index=5195, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJopW3wW0a4MXctCW0VWIKyjEcHOBMZoL4G6Z9YkU0PSnnQSou9-vzbnZNErRhOvrcXnnJ5Qev-rf3e-7E8_KO58SN6YvZnsHGtf_8_sIvxkXp4UQ1vsZoEOTP5hMvg-1o3MUGQVHlcRGTZrU8Z4heJrqVQRdOn2aeA9_Unx9eosSiOcPffSM9-fV0N0y5SJ5XZ-It_SXjfbvyqR6Xe6gUqzwhSux976_Z4pnbc8Nn613LDKP5aiEBfeId', start_index=5183)
Annotation(end_index=5195, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_5FKK9PsLnQaHeSSanvEwq_sjkl014_jmUtVBAg19sb5NjnpJ-l2NaoHyeBS9A91IuDQjFiZ4AEQ3xVuGVcFyl1PBs7zEZf6mzjtmMY5A21D1paMltxWpmGF8v2MgBkIKLYqVR750HDS7Mgj8z5L-E7wqrKSUXjtQ7p4BKlo=', start_index=5183)
Annotation(end_index=5475, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjIbtO1VFSXU8C3eZydF1q6hKjBDYHt5bZh7sSYxjln7W_exOCK8BeQl3HDzbupDJ3NwvGSomlOh-AT2zX5PO5AdGEMXpGRXoj3QhZsbXAI5z1SRyYfgaY5ObZt6wje-PpzQmcCY8wBIu8vBLWgVxwevP2UK-M9ANvU4xfSO0TmsxRxmC4y85ZPnUp3mRlcY4X0IOq7G6g3HV5dukb8Xslqps=', start_index=5463)
Annotation(end_index=5475, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAlh6Yu8SgD6KWiaZS2qVeGiBtRVxnpV0jF2uYJWhtl-rg-G8wAz88oOCKto1D6gHSmf-8XDod0V3tFOqKnZElYKh37JpmycoUR-AfWQw1znuj2okBTLuXPG041rD55OCm2trJ3hsFBiG_CNC9oZJa3YSlylaY3XNYjcg5XaM=', start_index=5463)
Annotation(end_index=5815, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwCMpCf1Jra8bUyeBmcnBB_A7WtzxqLU6NFa8__nBawCDtrcA7SmXbNKo2_1OaD8JKREmlDZo7jwB22BJCQU3PeLSNl_LppTDBepGlaZ6ZfrxxyLI4ygCRWay9-dJCg97SM0XloA==', start_index=5806)
Annotation(end_index=6394, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEX3jDykzHVDIkr8zbR_5EmEl41PyiqXPvWmPXnbTAHpZDwWkesPdUrJ5CK38swDU09GZBGFCC_EOc-ElgGnXcUOPNJTfPQ-AT-PrgZ7zIZpLzxI9M6fsiJ1fDkmqCD5paGwgQGwshBdjSbi-aMXSHdwyzxXsHdGw36vPmyJeiDoDxoMARypgjXhrq9mbrOQplMopsx', start_index=6381)
Annotation(end_index=6394, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsaWw3-LeYHMXUuW-c9Dek0J4hepmeczcWynD8Pl0QNrPOs59kE7rIjEl3-ewY_c2x6DOXVdmg1x_m02iXm7AVgSxTxxhjTaIo28NkKleFnw2xqqqSEOyoCIj1mlh-LqrIxmQDfYvUH80=', start_index=6381)
Annotation(end_index=6593, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_5FKK9PsLnQaHeSSanvEwq_sjkl014_jmUtVBAg19sb5NjnpJ-l2NaoHyeBS9A91IuDQjFiZ4AEQ3xVuGVcFyl1PBs7zEZf6mzjtmMY5A21D1paMltxWpmGF8v2MgBkIKLYqVR750HDS7Mgj8z5L-E7wqrKSUXjtQ7p4BKlo=', start_index=6584)
Annotation(end_index=6887, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEX3jDykzHVDIkr8zbR_5EmEl41PyiqXPvWmPXnbTAHpZDwWkesPdUrJ5CK38swDU09GZBGFCC_EOc-ElgGnXcUOPNJTfPQ-AT-PrgZ7zIZpLzxI9M6fsiJ1fDkmqCD5paGwgQGwshBdjSbi-aMXSHdwyzxXsHdGw36vPmyJeiDoDxoMARypgjXhrq9mbrOQplMopsx', start_index=6874)
Annotation(end_index=6887, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_1xXx0CNUmMmz-NO-4EYeAnQErPufpQvFf-B_sIAULfj1pnGeZQU7sEbkTS59zGGkY8eERZm_W7Xj5ay0wzitH7RYPOyp04abzmKLleqQrnVOEyTaMyUppxJ7Y6s8RstRbV7bgJ7L50YiW_cFhqU8TsUSvJMot5uRr-xbH-ljKMeonkkFLyFtOg==', start_index=6874)
Annotation(end_index=7359, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEartVCyKdDRid06b6C4Z-fLAWK5LGL-nE2qP4iqnr9YSuaCXdbck9_Z2GY4vYI8X45GzNsMvoCZTfDZzp8lO84uPhtvWCDTYOBObrzqMBQrTGehIuX6wVkg-ORNw_Fj2kjUfFJ', start_index=7346)
Annotation(end_index=7359, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKbtUmrHyUZD4wOps7zdNH2o96REvLVSFocY8n0z2bApfXE4dj68SymqpuyU2aUEoQ63OnSRJRODayYyWR9waAa3WZZQKWlsuU4Sn3-DOwbEATdyKoCRKD3zO4ql27VOI=', start_index=7346)
Annotation(end_index=7640, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwCMpCf1Jra8bUyeBmcnBB_A7WtzxqLU6NFa8__nBawCDtrcA7SmXbNKo2_1OaD8JKREmlDZo7jwB22BJCQU3PeLSNl_LppTDBepGlaZ6ZfrxxyLI4ygCRWay9-dJCg97SM0XloA==', start_index=7631)
Annotation(end_index=7841, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0HKmjhTKAD2n8XQ5sq_fdXAFoQpKy5MOXKk657gLb0UUBRVDJs46iQW6xLl2QrmeG3OBBnJz7y6DI3cfzk4igwFRY8-CbZHcWNGmVtuxm9BXsUfA6OpGwjolsUVLtkseearWt8q08WwemHrlmbGjwAUhkx3g4kYKNtX0Lr3b4KUw=', start_index=7827)
Annotation(end_index=7841, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTIUQt26CjQwf7XVIkTwLbI1poFyBIa02ECwHzlyL9ZAM6_LE7x28YZ0FnaBoWjKv_B7RReBu3KEAwhwL8_z1t5qb-jY74OOxIzem1U_0ZJEgeiLAzUlyuXMEUKV5KYlPQJ2UGZnMMzjyv9QSAwFqieSnj2Q7gcxJinKcSqs0=', start_index=7827)
Annotation(end_index=8166, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuS9THqZzkca73pKeuVRdvNmHRjBg5487SmspuhylGZdymMVMnSeevYyRZJtOCeLY6dA7EzFl_gcUx43-cLZMLqxVpTmsVmV29N_uSNPCLSQZPhCV0vvd3wqgABNTIvcp9yZToXm5M_9QOsp0ATTUDpLThWF1MyIaNlQ3G8P00HFNxTTv9', start_index=8156)
Annotation(end_index=8269, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECIHGft39kIuIHFR3y5mdOhKfNjNFl5zsi7kRxeZ-Ucdkt-JOqWi0eTkgzhs6BYTEIcnDieRVCM5cABvsjyBEerJKPRE9V0YkXYcyGr_BOpQZAXZ-qpJLrwfZGWdpc8bis1urlxksEdePrV71PvWNwoZJ4Irk2cTXKaQ==', start_index=8259)
Annotation(end_index=8876, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBPKrMACt5Ihco8OHSe6E7_QZ8GE0kmbpzfN6U02X8603XOnndP5Rp5xorRIBGv0UjGf2nw_vMlNjXTn2A8fQPcCzu4u2tXGvTuy-L1JnrVGc7RcJE31y3G1EMARl63i0=', start_index=8862)
Annotation(end_index=8876, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUK7KibYTPVMc_82hb96RMERL5IhP78kCWXcYFgOAj204bFHHTeU6utb9asE-rdGoZaIBXw-qvcLxeI5nacAu-1CGLcUP1qsRwdwWQX9beVkA1jZSCTgj7HLLXbar3OLc_34ApVN0hPJkitkpoK1d_WJBqH8c9_59ZafNNQgwMJXxpC08G-_XLhmGjQRLQz9JmRm_J115SojIffg8PeH-Xa32s5F_1yCEFS13IrQ60fi3QpY-IYvi5oH7zSMXWHy4=', start_index=8862)
Annotation(end_index=9069, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_TQOCS7866ycbzNs_uVsO96RgbdAVbTgP9T-NyRNTl803j9wika-u3Mzv95m8fL3cpo1FwQZSFc3XN0uLDZQGecycELdsh4fZ8aVMYUZyOO6yzs0cbRvMo45icvJ4CK_QCNwkzLZ0tgRq1HEXbk9cyNgMkgdv7IKPV8vBy0a4ipnFuDOAs9FOK4zNr-eD-G3Mzz7Dv3Znt2k0ya7LAKYNXh7CdK-HF2LYnB0=', start_index=9055)
Annotation(end_index=9069, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5HehkfZ1TYnFi9IoszoNcWWWp4sopzEDGW_N9RpQNTvmfHJL_o2MMVD8ixps9lO2rtmapjFaj8Ricv6lmh1yVz_FpdbLDAwHelIsUjEKlm5lj4ab-GVcIDoKxPQmCJd_QiMDG8C0pPnjGHxsMicNa2L8KNzskGEScoVXAn96-C9uxVFsNhzCKcqkfQQB2s9lbkw==', start_index=9055)
Annotation(end_index=9283, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBPKrMACt5Ihco8OHSe6E7_QZ8GE0kmbpzfN6U02X8603XOnndP5Rp5xorRIBGv0UjGf2nw_vMlNjXTn2A8fQPcCzu4u2tXGvTuy-L1JnrVGc7RcJE31y3G1EMARl63i0=', start_index=9273)
Annotation(end_index=9772, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPdh0DiuoSAt9YBH0TR5RabhLrxDXxKodm0NvXXb5WncJE2jA9_ZOat6o_dhcI9Ktq3jIHTEuUqciEgQX-99PFydgAKI47plYESDJgCTQuDdcJgc281AOam6J2YWZH2FaD3ZKt7aN4CKiuAZzMMSiaJKnUsVAG-K3el0iDg2w=', start_index=9758)
Annotation(end_index=9772, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUK7KibYTPVMc_82hb96RMERL5IhP78kCWXcYFgOAj204bFHHTeU6utb9asE-rdGoZaIBXw-qvcLxeI5nacAu-1CGLcUP1qsRwdwWQX9beVkA1jZSCTgj7HLLXbar3OLc_34ApVN0hPJkitkpoK1d_WJBqH8c9_59ZafNNQgwMJXxpC08G-_XLhmGjQRLQz9JmRm_J115SojIffg8PeH-Xa32s5F_1yCEFS13IrQ60fi3QpY-IYvi5oH7zSMXWHy4=', start_index=9758)
Annotation(end_index=10051, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBPKrMACt5Ihco8OHSe6E7_QZ8GE0kmbpzfN6U02X8603XOnndP5Rp5xorRIBGv0UjGf2nw_vMlNjXTn2A8fQPcCzu4u2tXGvTuy-L1JnrVGc7RcJE31y3G1EMARl63i0=', start_index=10037)
Annotation(end_index=10051, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_TQOCS7866ycbzNs_uVsO96RgbdAVbTgP9T-NyRNTl803j9wika-u3Mzv95m8fL3cpo1FwQZSFc3XN0uLDZQGecycELdsh4fZ8aVMYUZyOO6yzs0cbRvMo45icvJ4CK_QCNwkzLZ0tgRq1HEXbk9cyNgMkgdv7IKPV8vBy0a4ipnFuDOAs9FOK4zNr-eD-G3Mzz7Dv3Znt2k0ya7LAKYNXh7CdK-HF2LYnB0=', start_index=10037)
Annotation(end_index=10247, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUK7KibYTPVMc_82hb96RMERL5IhP78kCWXcYFgOAj204bFHHTeU6utb9asE-rdGoZaIBXw-qvcLxeI5nacAu-1CGLcUP1qsRwdwWQX9beVkA1jZSCTgj7HLLXbar3OLc_34ApVN0hPJkitkpoK1d_WJBqH8c9_59ZafNNQgwMJXxpC08G-_XLhmGjQRLQz9JmRm_J115SojIffg8PeH-Xa32s5F_1yCEFS13IrQ60fi3QpY-IYvi5oH7zSMXWHy4=', start_index=10237)
Annotation(end_index=10501, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGbvEvhqrdXi-dX7bmfstbYxNGQsqwq73I92I7H5QMQtAYJmZ6PFnKr4iyt0AMOGe_kvubct998ODz47WuoqD7FdD-x0EVGKf4_OcLYRQDqCFcrB953Ybx-zZ9vm7omqY65cishUJKu4Ip6366EUf9p6lXkrw=', start_index=10487)
Annotation(end_index=10501, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFo4EDIqTBS5HiwUgf-cump64XnmM7Z82vuKttEW9_pMzzFvCUcjfsLoigQqNUOOitZFb5sOho1GGi6bsrsabRqoaclkgyLMCGdV5hdoya0O5KLJr8e0mTXFJxZaCfC7hMR5SKQttKZV2e5-t9gl6VATe_5wRFa8URTotk=', start_index=10487)
Annotation(end_index=11013, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFo4EDIqTBS5HiwUgf-cump64XnmM7Z82vuKttEW9_pMzzFvCUcjfsLoigQqNUOOitZFb5sOho1GGi6bsrsabRqoaclkgyLMCGdV5hdoya0O5KLJr8e0mTXFJxZaCfC7hMR5SKQttKZV2e5-t9gl6VATe_5wRFa8URTotk=', start_index=10999)
Annotation(end_index=11013, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHS6jVpRNhHZuZNQCo6wkmFZC-EYGFQ0veDSoGy2vYygivpX28pCU3GcfYaYBo_34yAVQ-XqipkiOGVejDt9Yc6bjJZ4d1p-q9-NAgnQ1sgNU-2JcoSWBG5BaXIiOotmr8=', start_index=10999)
Annotation(end_index=11172, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFo4EDIqTBS5HiwUgf-cump64XnmM7Z82vuKttEW9_pMzzFvCUcjfsLoigQqNUOOitZFb5sOho1GGi6bsrsabRqoaclkgyLMCGdV5hdoya0O5KLJr8e0mTXFJxZaCfC7hMR5SKQttKZV2e5-t9gl6VATe_5wRFa8URTotk=', start_index=11158)
Annotation(end_index=11172, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5HehkfZ1TYnFi9IoszoNcWWWp4sopzEDGW_N9RpQNTvmfHJL_o2MMVD8ixps9lO2rtmapjFaj8Ricv6lmh1yVz_FpdbLDAwHelIsUjEKlm5lj4ab-GVcIDoKxPQmCJd_QiMDG8C0pPnjGHxsMicNa2L8KNzskGEScoVXAn96-C9uxVFsNhzCKcqkfQQB2s9lbkw==', start_index=11158)
Annotation(end_index=11410, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHS6jVpRNhHZuZNQCo6wkmFZC-EYGFQ0veDSoGy2vYygivpX28pCU3GcfYaYBo_34yAVQ-XqipkiOGVejDt9Yc6bjJZ4d1p-q9-NAgnQ1sgNU-2JcoSWBG5BaXIiOotmr8=', start_index=11400)
Annotation(end_index=11594, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGbvEvhqrdXi-dX7bmfstbYxNGQsqwq73I92I7H5QMQtAYJmZ6PFnKr4iyt0AMOGe_kvubct998ODz47WuoqD7FdD-x0EVGKf4_OcLYRQDqCFcrB953Ybx-zZ9vm7omqY65cishUJKu4Ip6366EUf9p6lXkrw=', start_index=11584)
Annotation(end_index=12173, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuS9THqZzkca73pKeuVRdvNmHRjBg5487SmspuhylGZdymMVMnSeevYyRZJtOCeLY6dA7EzFl_gcUx43-cLZMLqxVpTmsVmV29N_uSNPCLSQZPhCV0vvd3wqgABNTIvcp9yZToXm5M_9QOsp0ATTUDpLThWF1MyIaNlQ3G8P00HFNxTTv9', start_index=12163)
Annotation(end_index=12587, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuS9THqZzkca73pKeuVRdvNmHRjBg5487SmspuhylGZdymMVMnSeevYyRZJtOCeLY6dA7EzFl_gcUx43-cLZMLqxVpTmsVmV29N_uSNPCLSQZPhCV0vvd3wqgABNTIvcp9yZToXm5M_9QOsp0ATTUDpLThWF1MyIaNlQ3G8P00HFNxTTv9', start_index=12577)
Annotation(end_index=12842, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZEZzU18kItAxev15LpgbajgGvvcWQrZWlQpUbLKEpOCPacX8ENQLPNDWJqPTYaRGutQL_MPYnGEFYEPs7-uQjXfvR8a6I2xUDaMGKMOsF3pSd03BYdH-nOwG7Nv8SQ48hDk_sEbr41BG3HVwkqJrIbw==', start_index=12828)
Annotation(end_index=12842, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuS9THqZzkca73pKeuVRdvNmHRjBg5487SmspuhylGZdymMVMnSeevYyRZJtOCeLY6dA7EzFl_gcUx43-cLZMLqxVpTmsVmV29N_uSNPCLSQZPhCV0vvd3wqgABNTIvcp9yZToXm5M_9QOsp0ATTUDpLThWF1MyIaNlQ3G8P00HFNxTTv9', start_index=12828)
Annotation(end_index=13257, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFsJq7KZ-Qg7-1H3Zv3wpwJRgVUkAMHy0KoATx5wicawhV9CFTgpuyPUwTLYKO0JFbLC6Li0eAnrT7a1fJ9-N6d6jWy4TnGS_XmJm99J9fUkUSTV6L8t_4ZqXUCQ==', start_index=13247)
Annotation(end_index=13750, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFsJq7KZ-Qg7-1H3Zv3wpwJRgVUkAMHy0KoATx5wicawhV9CFTgpuyPUwTLYKO0JFbLC6Li0eAnrT7a1fJ9-N6d6jWy4TnGS_XmJm99J9fUkUSTV6L8t_4ZqXUCQ==', start_index=13740)
Annotation(end_index=14023, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFsJq7KZ-Qg7-1H3Zv3wpwJRgVUkAMHy0KoATx5wicawhV9CFTgpuyPUwTLYKO0JFbLC6Li0eAnrT7a1fJ9-N6d6jWy4TnGS_XmJm99J9fUkUSTV6L8t_4ZqXUCQ==', start_index=14010)
Annotation(end_index=14023, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjZuER4HtPs2ucnB3wXMnd6IvzcwT2EamweOG1wR0m3ZO6CAPGznZEb2Wn_aGzeeRuaF5CzkfF_bNFiNO0TGem19aS3_OzJCPlvZnUGDTvyUptdURxHZ-5Wb6ESXnCqgpuOfA3v8zffb6QuFhYn0opd_am1cUMF_gGDD_qxyrzdxGn4w2tVZAsZTABU7quuWggWVXuqqbDQrEeF53fTVOy9OusnM2qQr_NxXFjlwA_SjRkOwq1lccZgMFybbVPpsZpByQLLgK_paqvg-Qm8rxTdSfIaSQ=', start_index=14010)
Annotation(end_index=14500, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHAndSS30cDeTmyCcbhTU2mxXQze1LiqV_rzSLEeRtlNzdh5Bm7ubuZwHkTLikwlFaFD0d0YlDg1a8ltQkPQ6YKBoPXfoaN9_kiXqyQXJ5C7tUAP0tI3OvpPMPLVg1d58sNTDLd-mVYQU1HLz44XjLBJ_vlzRBVyssVz5J7zTncRmHwjKeKhHV8PwFqvr88OtIj0Z5g3oBhyMbvTDacC-5V2X1dYDcTqp4TB5lEQEy', start_index=14486)
Annotation(end_index=14500, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGw4OSv1Hs8uoWEkmdlwhmz9xNfdsEVsE4aoLaj-ySt3hTT5RKlYhTeUmLXo3XdY9jX3BysStbsOI-PXPzam2u38qnQtdpdF2peKitShAO03YusaTYYlEc1rY-M4gQ1XWTiroSsyil8rHT1kyU-5dqR5xQwz4Enn85TM-UpYSfxWFwPlpQSiTTR8CTYQ9ujpD5qq_E2RVTRuZQSHVA9RwPL9C5oltOyFJDx00mE3n4=', start_index=14486)
Annotation(end_index=14712, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHAndSS30cDeTmyCcbhTU2mxXQze1LiqV_rzSLEeRtlNzdh5Bm7ubuZwHkTLikwlFaFD0d0YlDg1a8ltQkPQ6YKBoPXfoaN9_kiXqyQXJ5C7tUAP0tI3OvpPMPLVg1d58sNTDLd-mVYQU1HLz44XjLBJ_vlzRBVyssVz5J7zTncRmHwjKeKhHV8PwFqvr88OtIj0Z5g3oBhyMbvTDacC-5V2X1dYDcTqp4TB5lEQEy', start_index=14698)
Annotation(end_index=14712, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG64D4xvuK0x94vk6xfVd5rHX-RRRfXUpk7WGgjyJwTn-TaB-_ebCwcMzHl0Y8Mr6QFijwwNDipLgunAAnAt49qqNlDtZ1w2exNCBuqcrlVOnkhf8BlnFWbhQeHOH0oj_ff-oMFNJ2DyNyv-2qfNLZi3l-RJgJPHibEoN5m57AuDD88ytrR-CQCRqiGKuTWDAmC2qx_cGoH80In5_OkjfxGTJJhVhTAJfysKj_dCDoVNUeuZzCai-kdT52H_1ZC6UiuwdK2gm-G0Q==', start_index=14698)
Annotation(end_index=15033, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGw4OSv1Hs8uoWEkmdlwhmz9xNfdsEVsE4aoLaj-ySt3hTT5RKlYhTeUmLXo3XdY9jX3BysStbsOI-PXPzam2u38qnQtdpdF2peKitShAO03YusaTYYlEc1rY-M4gQ1XWTiroSsyil8rHT1kyU-5dqR5xQwz4Enn85TM-UpYSfxWFwPlpQSiTTR8CTYQ9ujpD5qq_E2RVTRuZQSHVA9RwPL9C5oltOyFJDx00mE3n4=', start_index=15023)
Annotation(end_index=15409, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJopW3wW0a4MXctCW0VWIKyjEcHOBMZoL4G6Z9YkU0PSnnQSou9-vzbnZNErRhOvrcXnnJ5Qev-rf3e-7E8_KO58SN6YvZnsHGtf_8_sIvxkXp4UQ1vsZoEOTP5hMvg-1o3MUGQVHlcRGTZrU8Z4heJrqVQRdOn2aeA9_Unx9eosSiOcPffSM9-fV0N0y5SJ5XZ-It_SXjfbvyqR6Xe6gUqzwhSux976_Z4pnbc8Nn613LDKP5aiEBfeId', start_index=15400)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBPKrMACt5Ihco8OHSe6E7_QZ8GE0kmbpzfN6U02X8603XOnndP5Rp5xorRIBGv0UjGf2nw_vMlNjXTn2A8fQPcCzu4u2tXGvTuy-L1JnrVGc7RcJE31y3G1EMARl63i0=', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECIHGft39kIuIHFR3y5mdOhKfNjNFl5zsi7kRxeZ-Ucdkt-JOqWi0eTkgzhs6BYTEIcnDieRVCM5cABvsjyBEerJKPRE9V0YkXYcyGr_BOpQZAXZ-qpJLrwfZGWdpc8bis1urlxksEdePrV71PvWNwoZJ4Irk2cTXKaQ==', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJopW3wW0a4MXctCW0VWIKyjEcHOBMZoL4G6Z9YkU0PSnnQSou9-vzbnZNErRhOvrcXnnJ5Qev-rf3e-7E8_KO58SN6YvZnsHGtf_8_sIvxkXp4UQ1vsZoEOTP5hMvg-1o3MUGQVHlcRGTZrU8Z4heJrqVQRdOn2aeA9_Unx9eosSiOcPffSM9-fV0N0y5SJ5XZ-It_SXjfbvyqR6Xe6gUqzwhSux976_Z4pnbc8Nn613LDKP5aiEBfeId', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPdh0DiuoSAt9YBH0TR5RabhLrxDXxKodm0NvXXb5WncJE2jA9_ZOat6o_dhcI9Ktq3jIHTEuUqciEgQX-99PFydgAKI47plYESDJgCTQuDdcJgc281AOam6J2YWZH2FaD3ZKt7aN4CKiuAZzMMSiaJKnUsVAG-K3el0iDg2w=', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEX3jDykzHVDIkr8zbR_5EmEl41PyiqXPvWmPXnbTAHpZDwWkesPdUrJ5CK38swDU09GZBGFCC_EOc-ElgGnXcUOPNJTfPQ-AT-PrgZ7zIZpLzxI9M6fsiJ1fDkmqCD5paGwgQGwshBdjSbi-aMXSHdwyzxXsHdGw36vPmyJeiDoDxoMARypgjXhrq9mbrOQplMopsx', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_1xXx0CNUmMmz-NO-4EYeAnQErPufpQvFf-B_sIAULfj1pnGeZQU7sEbkTS59zGGkY8eERZm_W7Xj5ay0wzitH7RYPOyp04abzmKLleqQrnVOEyTaMyUppxJ7Y6s8RstRbV7bgJ7L50YiW_cFhqU8TsUSvJMot5uRr-xbH-ljKMeonkkFLyFtOg==', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEartVCyKdDRid06b6C4Z-fLAWK5LGL-nE2qP4iqnr9YSuaCXdbck9_Z2GY4vYI8X45GzNsMvoCZTfDZzp8lO84uPhtvWCDTYOBObrzqMBQrTGehIuX6wVkg-ORNw_Fj2kjUfFJ', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjIbtO1VFSXU8C3eZydF1q6hKjBDYHt5bZh7sSYxjln7W_exOCK8BeQl3HDzbupDJ3NwvGSomlOh-AT2zX5PO5AdGEMXpGRXoj3QhZsbXAI5z1SRyYfgaY5ObZt6wje-PpzQmcCY8wBIu8vBLWgVxwevP2UK-M9ANvU4xfSO0TmsxRxmC4y85ZPnUp3mRlcY4X0IOq7G6g3HV5dukb8Xslqps=', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0HKmjhTKAD2n8XQ5sq_fdXAFoQpKy5MOXKk657gLb0UUBRVDJs46iQW6xLl2QrmeG3OBBnJz7y6DI3cfzk4igwFRY8-CbZHcWNGmVtuxm9BXsUfA6OpGwjolsUVLtkseearWt8q08WwemHrlmbGjwAUhkx3g4kYKNtX0Lr3b4KUw=', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFsJq7KZ-Qg7-1H3Zv3wpwJRgVUkAMHy0KoATx5wicawhV9CFTgpuyPUwTLYKO0JFbLC6Li0eAnrT7a1fJ9-N6d6jWy4TnGS_XmJm99J9fUkUSTV6L8t_4ZqXUCQ==', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGbvEvhqrdXi-dX7bmfstbYxNGQsqwq73I92I7H5QMQtAYJmZ6PFnKr4iyt0AMOGe_kvubct998ODz47WuoqD7FdD-x0EVGKf4_OcLYRQDqCFcrB953Ybx-zZ9vm7omqY65cishUJKu4Ip6366EUf9p6lXkrw=', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHAndSS30cDeTmyCcbhTU2mxXQze1LiqV_rzSLEeRtlNzdh5Bm7ubuZwHkTLikwlFaFD0d0YlDg1a8ltQkPQ6YKBoPXfoaN9_kiXqyQXJ5C7tUAP0tI3OvpPMPLVg1d58sNTDLd-mVYQU1HLz44XjLBJ_vlzRBVyssVz5J7zTncRmHwjKeKhHV8PwFqvr88OtIj0Z5g3oBhyMbvTDacC-5V2X1dYDcTqp4TB5lEQEy', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZEZzU18kItAxev15LpgbajgGvvcWQrZWlQpUbLKEpOCPacX8ENQLPNDWJqPTYaRGutQL_MPYnGEFYEPs7-uQjXfvR8a6I2xUDaMGKMOsF3pSd03BYdH-nOwG7Nv8SQ48hDk_sEbr41BG3HVwkqJrIbw==', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_TQOCS7866ycbzNs_uVsO96RgbdAVbTgP9T-NyRNTl803j9wika-u3Mzv95m8fL3cpo1FwQZSFc3XN0uLDZQGecycELdsh4fZ8aVMYUZyOO6yzs0cbRvMo45icvJ4CK_QCNwkzLZ0tgRq1HEXbk9cyNgMkgdv7IKPV8vBy0a4ipnFuDOAs9FOK4zNr-eD-G3Mzz7Dv3Znt2k0ya7LAKYNXh7CdK-HF2LYnB0=', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjZuER4HtPs2ucnB3wXMnd6IvzcwT2EamweOG1wR0m3ZO6CAPGznZEb2Wn_aGzeeRuaF5CzkfF_bNFiNO0TGem19aS3_OzJCPlvZnUGDTvyUptdURxHZ-5Wb6ESXnCqgpuOfA3v8zffb6QuFhYn0opd_am1cUMF_gGDD_qxyrzdxGn4w2tVZAsZTABU7quuWggWVXuqqbDQrEeF53fTVOy9OusnM2qQr_NxXFjlwA_SjRkOwq1lccZgMFybbVPpsZpByQLLgK_paqvg-Qm8rxTdSfIaSQ=', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFo4EDIqTBS5HiwUgf-cump64XnmM7Z82vuKttEW9_pMzzFvCUcjfsLoigQqNUOOitZFb5sOho1GGi6bsrsabRqoaclkgyLMCGdV5hdoya0O5KLJr8e0mTXFJxZaCfC7hMR5SKQttKZV2e5-t9gl6VATe_5wRFa8URTotk=', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuS9THqZzkca73pKeuVRdvNmHRjBg5487SmspuhylGZdymMVMnSeevYyRZJtOCeLY6dA7EzFl_gcUx43-cLZMLqxVpTmsVmV29N_uSNPCLSQZPhCV0vvd3wqgABNTIvcp9yZToXm5M_9QOsp0ATTUDpLThWF1MyIaNlQ3G8P00HFNxTTv9', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwCMpCf1Jra8bUyeBmcnBB_A7WtzxqLU6NFa8__nBawCDtrcA7SmXbNKo2_1OaD8JKREmlDZo7jwB22BJCQU3PeLSNl_LppTDBepGlaZ6ZfrxxyLI4ygCRWay9-dJCg97SM0XloA==', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG64D4xvuK0x94vk6xfVd5rHX-RRRfXUpk7WGgjyJwTn-TaB-_ebCwcMzHl0Y8Mr6QFijwwNDipLgunAAnAt49qqNlDtZ1w2exNCBuqcrlVOnkhf8BlnFWbhQeHOH0oj_ff-oMFNJ2DyNyv-2qfNLZi3l-RJgJPHibEoN5m57AuDD88ytrR-CQCRqiGKuTWDAmC2qx_cGoH80In5_OkjfxGTJJhVhTAJfysKj_dCDoVNUeuZzCai-kdT52H_1ZC6UiuwdK2gm-G0Q==', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDm7a6FuFFEm3pwy8DBY5fF594-qRdkiX27Tvik2m4jBbWMKtLDzs9jZUmwSUXgsNCaOvX93wBheBgFCKBqIUwQNlRkF8LkuiumpwQQ_WhBvtUZIEbkS5p_b_3AdyJdmfEaewJS834sPQmDNmB6weyuwL_uSSuIGzd', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTIUQt26CjQwf7XVIkTwLbI1poFyBIa02ECwHzlyL9ZAM6_LE7x28YZ0FnaBoWjKv_B7RReBu3KEAwhwL8_z1t5qb-jY74OOxIzem1U_0ZJEgeiLAzUlyuXMEUKV5KYlPQJ2UGZnMMzjyv9QSAwFqieSnj2Q7gcxJinKcSqs0=', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsaWw3-LeYHMXUuW-c9Dek0J4hepmeczcWynD8Pl0QNrPOs59kE7rIjEl3-ewY_c2x6DOXVdmg1x_m02iXm7AVgSxTxxhjTaIo28NkKleFnw2xqqqSEOyoCIj1mlh-LqrIxmQDfYvUH80=', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGw4OSv1Hs8uoWEkmdlwhmz9xNfdsEVsE4aoLaj-ySt3hTT5RKlYhTeUmLXo3XdY9jX3BysStbsOI-PXPzam2u38qnQtdpdF2peKitShAO03YusaTYYlEc1rY-M4gQ1XWTiroSsyil8rHT1kyU-5dqR5xQwz4Enn85TM-UpYSfxWFwPlpQSiTTR8CTYQ9ujpD5qq_E2RVTRuZQSHVA9RwPL9C5oltOyFJDx00mE3n4=', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5HehkfZ1TYnFi9IoszoNcWWWp4sopzEDGW_N9RpQNTvmfHJL_o2MMVD8ixps9lO2rtmapjFaj8Ricv6lmh1yVz_FpdbLDAwHelIsUjEKlm5lj4ab-GVcIDoKxPQmCJd_QiMDG8C0pPnjGHxsMicNa2L8KNzskGEScoVXAn96-C9uxVFsNhzCKcqkfQQB2s9lbkw==', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAlh6Yu8SgD6KWiaZS2qVeGiBtRVxnpV0jF2uYJWhtl-rg-G8wAz88oOCKto1D6gHSmf-8XDod0V3tFOqKnZElYKh37JpmycoUR-AfWQw1znuj2okBTLuXPG041rD55OCm2trJ3hsFBiG_CNC9oZJa3YSlylaY3XNYjcg5XaM=', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKbtUmrHyUZD4wOps7zdNH2o96REvLVSFocY8n0z2bApfXE4dj68SymqpuyU2aUEoQ63OnSRJRODayYyWR9waAa3WZZQKWlsuU4Sn3-DOwbEATdyKoCRKD3zO4ql27VOI=', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHS6jVpRNhHZuZNQCo6wkmFZC-EYGFQ0veDSoGy2vYygivpX28pCU3GcfYaYBo_34yAVQ-XqipkiOGVejDt9Yc6bjJZ4d1p-q9-NAgnQ1sgNU-2JcoSWBG5BaXIiOotmr8=', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUK7KibYTPVMc_82hb96RMERL5IhP78kCWXcYFgOAj204bFHHTeU6utb9asE-rdGoZaIBXw-qvcLxeI5nacAu-1CGLcUP1qsRwdwWQX9beVkA1jZSCTgj7HLLXbar3OLc_34ApVN0hPJkitkpoK1d_WJBqH8c9_59ZafNNQgwMJXxpC08G-_XLhmGjQRLQz9JmRm_J115SojIffg8PeH-Xa32s5F_1yCEFS13IrQ60fi3QpY-IYvi5oH7zSMXWHy4=', start_index=18030)
Annotation(end_index=18143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_5FKK9PsLnQaHeSSanvEwq_sjkl014_jmUtVBAg19sb5NjnpJ-l2NaoHyeBS9A91IuDQjFiZ4AEQ3xVuGVcFyl1PBs7zEZf6mzjtmMY5A21D1paMltxWpmGF8v2MgBkIKLYqVR750HDS7Mgj8z5L-E7wqrKSUXjtQ7p4BKlo=', start_index=18030)

## Sources
