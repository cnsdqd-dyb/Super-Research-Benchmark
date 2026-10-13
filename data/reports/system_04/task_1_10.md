# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 49179051 | **Time:** 470.99s | **Cost:** $2.06114
--------------------------------------------------------------------------------

# Optimizing Nanomedicine Stability and Permeability: The Role of Size Distribution in the Serum Protein-Cell Uptake Competitive Landscape

### Key Points
*   **Polydispersity Compromises Predictability:** A Polydispersity Index (PDI) > 0.3 results in heterogeneous protein corona compositions within a single formulation, causing erratic biodistribution where fractions of the dose are cleared rapidly while others fail to penetrate target tissues.
*   **The Vroman Effect and Curvature:** Nanoparticle curvature, dictated by size, fundamentally alters protein adsorption kinetics (Vroman effect). Smaller particles (<50 nm) with high curvature often resist the unfolding of adsorbed proteins, potentially reducing opsonization compared to larger, flatter surfaces.
*   **Dysopsonin Recruitment:** Controlling size distribution is essential for selectively recruiting dysopsonins (e.g., Albumin, Apolipoprotein E) which act as "Trojan horses" for targeted delivery (e.g., crossing the Blood-Brain Barrier or targeting hepatocytes), while minimizing opsonin (IgG, Complement) adsorption.
*   **The Permeability-Retention Trade-off:** Monodisperse particles in the 50–100 nm range optimize the trade-off between deep tumor penetration (requiring small size) and avoidance of renal/hepatic clearance (requiring larger size), maximizing the Enhanced Permeability and Retention (EPR) effect.

### Executive Summary
The clinical translation of nanomedicines is frequently hindered by the discrepancy between their "synthetic identity" (physicochemical properties ex vivo) and their "biological identity" (behavior in physiological fluids). Central to this disconnect is the formation of the protein corona—a dynamic layer of serum proteins that adsorbs onto nanoparticles immediately upon intravenous administration. This report analyzes how controlling the size distribution (polydispersity) of nanocarriers optimizes targeted delivery. It explores the competitive kinetics between serum protein adsorption and cellular uptake, demonstrating that narrow size distributions are critical for engineering predictable biological identities. By manipulating size and curvature, researchers can influence the Vroman effect to favor dysopsonin adsorption, thereby enhancing stability, prolonging circulation, and optimizing permeability across biological barriers.

---

## 1. Introduction: The Synthetic versus Biological Identity of Nanomedicines

The efficacy of nanomedicines—ranging from liposomes and lipid nanoparticles (LNPs) to polymeric and metallic nanocarriers—relies on their ability to navigate the complex biological environment to reach specific pathological sites. However, a fundamental challenge persists: the physicochemical properties engineered in the laboratory (synthetic identity) are instantly modified upon contact with biological fluids, creating a new "biological identity" defined largely by the protein corona [cite: 1, 2, 3].

### 1.1 The Criticality of Size Distribution and Polydispersity
While mean particle size is a standard characterization metric, the breadth of the size distribution, quantified by the Polydispersity Index (PDI), is equally critical yet often underappreciated. A PDI value below 0.3 is generally considered necessary to ensure a monodisperse population suitable for clinical applications [cite: 4, 5, 6].

In polydisperse systems (high PDI), the particle population contains significant fractions of both undersized and oversized particles. This heterogeneity leads to inconsistent biological fates:
*   **Undersized fraction (<10 nm):** Subject to rapid renal clearance via glomerular filtration [cite: 7, 8].
*   **Oversized fraction (>200 nm):** Prone to rapid opsonization and sequestration by the Mononuclear Phagocyte System (MPS) in the liver and spleen [cite: 9, 10].
*   **Target fraction (10–200 nm):** The optimal range for exploiting the Enhanced Permeability and Retention (EPR) effect and balancing circulation time with cellular uptake [cite: 11, 12].

Therefore, controlling size distribution is not merely a manufacturing quality control step but a biological necessity to ensure that the entire administered dose behaves uniformly regarding protein adsorption and cellular interaction [cite: 4, 13].

### 1.2 The Competition: Adsorption vs. Uptake
The fate of a nanoparticle is determined by a kinetic race between the adsorption of serum proteins (which can trigger clearance or facilitate targeting) and the recognition/uptake by target cells. High-affinity proteins (opsonins) mark particles for immune clearance, while dysopsonins can prolong circulation [cite: 14, 15]. Simultaneously, the protein corona can shield targeting ligands, reducing specific uptake, or conversely, provide new receptor-binding motifs (e.g., ApoE targeting LDL receptors) [cite: 16, 17]. Optimizing this balance requires precise control over the nanoparticle surface curvature and total surface area, both of which are functions of particle size and distribution [cite: 1, 18].

---

## 2. The Physics of Protein Corona Formation and Nanoparticle Curvature

The formation of the protein corona is a thermodynamic and kinetic process governed by the energy landscape of the nanoparticle surface. The size of the nanoparticle dictates its surface curvature, which fundamentally influences which proteins adsorb, how much they unfold, and their orientation.

### 2.1 The Vroman Effect and Competitive Adsorption
Protein adsorption is dynamic. The **Vroman effect** describes the temporal evolution of the corona composition, where highly abundant, small, and mobile proteins (e.g., albumin) initially adsorb to the surface but are subsequently displaced by less abundant proteins with higher binding affinities (e.g., fibrinogen, immunoglobulins, apolipoproteins) [cite: 19, 20, 21].

*   **Kinetics of Displacement:** The rate of this displacement is influenced by the nanoparticle size. Larger particles provide flatter surfaces (lower curvature), allowing larger proteins like fibrinogen to spread and maximize van der Waals interactions, accelerating the displacement of albumin [cite: 22, 23].
*   **Impact of Polydispersity:** In a polydisperse formulation, the Vroman effect occurs at different rates on particles of different sizes. Small particles may retain an albumin-rich (dysopsonin) corona longer due to steric constraints preventing large opsonins from binding, while larger aggregates in the same mixture rapidly acquire a fibrinogen-rich (opsonin) corona [cite: 24, 25]. This results in a "heterogeneous biological identity" where the therapeutic efficacy is inconsistent across the particle population [cite: 26].

### 2.2 Surface Curvature and Protein Conformation
The curvature of the nanoparticle surface acts as a geometric filter for protein adsorption.
*   **Steric Hindrance on High Curvature:** On small nanoparticles (<50 nm), the high surface curvature limits the contact area available for large proteins. This reduces the entropic gain from protein unfolding (denaturation). Consequently, proteins adsorbed on small, highly curved particles often retain their native conformation ("soft" corona) more effectively than those on larger, flatter particles [cite: 18, 27].
*   **Denaturation and Immunogenicity:** On larger particles (>100 nm), proteins can spread and denature, exposing cryptic epitopes that may trigger immune responses or complement activation. For example, albumin adsorbed on flat surfaces or large particles is more likely to undergo conformational changes that promote macrophage recognition, whereas albumin on small particles remains "stealthy" [cite: 27].
*   **PEGylation Efficiency:** The effectiveness of Polyethylene Glycol (PEG) grafting—a standard strategy to reduce protein adsorption—is also size-dependent. On smaller particles, the high curvature increases the volume available for the distal ends of PEG chains (V_PEG), reducing steric crowding and potentially allowing more protein penetration unless grafting density is extremely high [cite: 1].

### 2.3 Heterogeneity in Corona Composition
Research indicates that even with identical surface chemistry, nanoparticles of different sizes recruit different protein coronas.
*   **Case Study (Polystyrene):** A study comparing 50 nm and 100 nm polystyrene particles showed that while they shared ~70% of corona proteins, significant fractions were unique to specific sizes. The 100 nm particles adsorbed more unique proteins related to complement activation compared to the 50 nm counterparts [cite: 3, 24].
*   **Implication for PDI:** If a formulation has a high PDI (e.g., mixing 50 nm and 100 nm particles), the "biological identity" is a complex mixture. The 100 nm fraction may trigger rapid immune clearance, while the 50 nm fraction circulates. This unpredictability complicates dosing and toxicity profiles [cite: 13, 26].

---

## 3. Opsonins vs. Dysopsonins: Engineering the "Trojan Horse"

The composition of the protein corona determines whether the nanoparticle is flagged for clearance (opsonization) or allowed to circulate (dysopsonization). Controlling size distribution is a primary lever for shifting this balance.

### 3.1 The Opsonins: IgG and Complement
Opsonins are proteins that facilitate phagocytosis. The most prominent are Immunoglobulins (IgG) and Complement factors (e.g., C3b).
*   **Size Dependence:** Larger particles generally adsorb more IgG and Complement proteins due to increased surface area and lower curvature, which supports the multi-point binding required for these large protein complexes [cite: 15, 28].
*   **Clearance Mechanism:** Opsonized particles are recognized by Fc receptors and Complement receptors on macrophages (Kupffer cells in the liver), leading to rapid removal from the blood [cite: 29, 30].

### 3.2 The Dysopsonins: Albumin and Apolipoproteins
Dysopsonins promote circulation or specific uptake by non-phagocytic cells.
*   **Albumin:** The most abundant plasma protein. An albumin-rich corona can mask the particle, preventing the binding of opsonins and reducing macrophage uptake. This is often referred to as the "don't eat me" signal [cite: 28, 31, 32].
    *   *Optimization:* Small nanoparticles (<50 nm) tend to enrich albumin in their corona relative to larger particles due to the Vroman effect and curvature constraints that disfavor larger opsonins [cite: 14].
*   **Apolipoproteins (ApoE):** Crucial for lipid-based carriers. ApoE adsorbs onto LNPs and facilitates uptake by hepatocytes via the Low-Density Lipoprotein (LDL) receptor. This "Trojan Horse" mechanism is the basis for the efficacy of FDA-approved siRNA therapies (e.g., Onpattro) [cite: 16, 17, 33].
    *   *Size Dependence:* The adsorption of ApoE is highly sensitive to particle size and lipid composition. Studies suggest that LNPs in the 50–100 nm range optimally recruit ApoE while avoiding excessive complement activation [cite: 16, 34].

### 3.3 Competitive Displacement Strategies
Recent molecular dynamics simulations and experimental data suggest that pre-coating or engineering particles to preferentially bind dysopsonins can displace opsonins.
*   **Albumin vs. IgG:** On Graphene Oxide and silica nanoparticles, albumin has been shown to displace IgG or prevent its binding if the particle size and surface chemistry are optimized. High lateral diffusion of albumin on the surface allows it to form a stable, protective monolayer [cite: 14, 35].
*   **Strategic PDI Control:** By maintaining a narrow size distribution (PDI < 0.1), manufacturers can ensure that the surface curvature across the entire population favors the adsorption of dysopsonins (like ApoE or Albumin) over opsonins, thereby stabilizing the drug delivery system in vivo [cite: 4, 6].

---

## 4. Cellular Uptake and Ligand Shielding

The interaction between nanoparticles and target cells is the culmination of the delivery process. This interaction is heavily modulated by the protein corona, which can shield synthetic targeting ligands.

### 4.1 Ligand Shielding by the Corona
Active targeting relies on conjugating ligands (antibodies, peptides) to the nanoparticle surface. However, the protein corona can physically cover these ligands, rendering them ineffective—a phenomenon known as **ligand shielding**.
*   **Mechanism:** The corona thickness (often 10–20 nm) can exceed the length of the targeting ligand, preventing interaction with the cell receptor [cite: 17, 36, 37].
*   **Size Influence:** Ligand shielding is more pronounced on larger particles where the corona is denser and more complex. On smaller particles with high curvature, the "soft" corona may be more permeable or less dense, potentially allowing ligands to remain accessible [cite: 18, 36].
*   **Trojan Horse as an Alternative:** Because ligand shielding is so prevalent, modern nanomedicine often relies on the corona itself for targeting (e.g., recruiting endogenous ApoE to target liver cells) rather than fighting against it [cite: 37, 38].

### 4.2 Thermodynamic Models of Cellular Uptake
Cellular uptake is an energy-dependent process (endocytosis) governed by the interplay between membrane bending energy and receptor-ligand binding energy.
*   **The 50 nm Optimum:** Theoretical and experimental studies consistently identify ~50 nm as the optimal diameter for receptor-mediated endocytosis.
    *   *Physics:* Particles <30 nm often fail to drive the membrane wrapping process because the free energy released by receptor binding is insufficient to overcome the bending rigidity of the cell membrane. Particles >60 nm require the recruitment of too many receptors, depleting the local membrane supply and stalling uptake [cite: 9, 39].
*   **Impact of Polydispersity:** A polydisperse formulation with a mean size of 50 nm but a high PDI will contain many particles outside this optimal window. The <30 nm fraction may bind but not enter (blocking receptors), while the >100 nm fraction may be shunted toward phagocytosis rather than specific endocytosis [cite: 9, 13].

### 4.3 Endocytic Pathways and Size
The size of the nanoparticle determines the portal of entry into the cell:
*   **Clathrin-mediated Endocytosis:** Primary pathway for particles ~100-150 nm.
*   **Caveolae-mediated Endocytosis:** Often favored by smaller particles (20–100 nm) and specific surface chemistries.
*   **Macropinocytosis/Phagocytosis:** Dominant for larger aggregates (>200-500 nm) [cite: 39, 40].
*   **Consistency Requirement:** To target a specific intracellular compartment (e.g., escaping the endosome for cytosolic delivery), the uptake pathway must be consistent. A narrow size distribution ensures that the majority of the dose enters via the intended pathway, optimizing drug release kinetics [cite: 41, 42].

---

## 5. Permeability, Stability, and the EPR Effect

Once in the bloodstream, nanomedicines must remain stable against aggregation and permeate into the target tissue (often tumors).

### 5.1 Stability and Aggregation
Protein adsorption can induce aggregation, drastically altering the size distribution in vivo.
*   **Bridging Flocculation:** Proteins like fibrinogen can bridge multiple nanoparticles, forming large clusters. A 50 nm particle can rapidly become part of a 500 nm aggregate.
*   **Consequences:** These aggregates lose their ability to penetrate tumors and are immediately cleared by the MPS.
*   **Role of PDI:** Initial polydispersity exacerbates this instability. The presence of large particles can act as nucleation sites for further aggregation. Monodisperse, sterically stabilized (e.g., PEGylated) particles are more resistant to protein-induced aggregation [cite: 6, 43, 44].

### 5.2 The Enhanced Permeability and Retention (EPR) Effect
The EPR effect relies on the leaky vasculature of tumors (pores 200 nm to 2 µm) and impaired lymphatic drainage. However, the EPR effect is highly heterogeneous and size-dependent.
*   **Penetration vs. Retention:**
    *   *Small particles (<50 nm):* Penetrate deep into the tumor stroma and extracellular matrix (ECM) but may diffuse back out or be cleared rapidly by the kidneys [cite: 11].
    *   *Large particles (>100 nm):* Extravasate but remain trapped in the perivascular space (collagen matrix), failing to reach the tumor core [cite: 45, 46].
*   **The "Goldilocks" Zone:** The consensus for optimal EPR utilization is monodisperse particles in the **50–100 nm** range. This size is large enough to avoid renal clearance (>10 nm) and ensure retention, but small enough to penetrate the ECM [cite: 7, 12, 47].
*   **Multistage Systems:** To overcome the penetration-retention paradox, some systems are designed to shrink. A 100 nm particle (stable in blood) extravasates and then degrades into 10 nm particles (penetrating) within the tumor microenvironment [cite: 45]. This sophisticated engineering requires precise control over the initial size distribution.

---

## 6. Strategies for Optimization

To optimize stability and permeability amidst the protein-cell competition, the following strategies regarding size distribution are supported by the literature:

### 6.1 Strict Control of PDI (<0.2)
Achieving a PDI < 0.2 (and ideally < 0.1) is paramount. This ensures:
*   **Uniform Corona:** The entire dose recruits a similar protein profile (e.g., ApoE-rich), ensuring predictable targeting [cite: 4, 6].
*   **Consistent Clearance:** Avoids the "rapid clearance" fractions (renal <10 nm, MPS >200 nm) [cite: 5].
*   **Manufacturing Techniques:** Utilization of advanced microfluidics (e.g., NanoAssemblr) or digestive ripening techniques allows for the production of LNPs and metallic nanoparticles with extremely narrow size distributions [cite: 44, 48].

### 6.2 Tuning Curvature for Dysopsonin Recruitment
*   **Size Selection:** Engineering particles in the 50–80 nm range appears optimal for recruiting albumin and ApoE while minimizing fibrinogen/complement activation [cite: 16, 49].
*   **Surface Modification:** Coupling size control with surface chemistry (e.g., PEG density) allows for the "tuning" of the Vroman effect. On 50 nm particles, optimizing PEG density can selectively permit the binding of small dysopsonins while sterically blocking large opsonins [cite: 1].

### 6.3 Pre-coating (Artificial Corona)
Instead of relying on the random adsorption of serum proteins, particles can be pre-coated with dysopsonins (e.g., Albumin or ApoE) during manufacturing.
*   **Stability:** This "artificial corona" stabilizes the particle size and prevents the adsorption of opsonins upon injection [cite: 31, 34, 50].
*   **Targeting:** Pre-coating with ApoE has been shown to enhance uptake by brain endothelial cells (crossing the BBB) and hepatocytes [cite: 34, 51].

---

## 7. Conclusion

The optimization of nanomedicine carriers is not merely a matter of chemical composition but of precise physical engineering. The size distribution of the carrier dictates the thermodynamic and kinetic landscape of the protein corona formation. A narrow size distribution (low PDI) is the prerequisite for a predictable biological identity.

By controlling size and curvature, researchers can manipulate the **Vroman effect** to favor the adsorption of dysopsonins (Albumin, ApoE) over opsonins (IgG, Complement). This selective recruitment stabilizes the nanoparticle in the bloodstream, prevents macrophage clearance, and facilitates targeted delivery via "Trojan horse" mechanisms. Furthermore, maintaining a monodisperse population in the 50–100 nm range optimizes the trade-off between deep tissue permeability and systemic retention, maximizing the therapeutic index. Thus, the rigorous control of polydispersity is a critical design parameter for stabilizing nanomedicines against the competitive pressures of the biological environment.

### References
[cite: 13] An analytical approach for quantifying the impact of polydispersity on nanoparticle targeting and biological fate.
[cite: 52] Impact of Particle Size and Polydispersity Index on the Clinical Applications of Lipidic Nanocarrier Systems.
[cite: 40] Competition between serum protein adsorption and cell uptake nanoparticles size.
[cite: 1] Nanoparticle Size and Surface Chemistry Determine Serum Protein Adsorption and Macrophage Uptake.
[cite: 2] Nanoparticle size and surface chemistry determine serum protein adsorption and macrophage uptake.
[cite: 11] Nanoparticle size effect on EPR effect and mononuclear phagocyte system clearance.
[cite: 47] Barriers to the delivery of nano-sized drugs.
[cite: 9] Nanoparticle size effect on EPR effect and mononuclear phagocyte system clearance.
[cite: 45] EPR-effect Utilizing size-dependent nanoparticle delivery to solid tumors.
[cite: 29] Nanoparticle size effect on EPR effect and mononuclear phagocyte system clearance.
[cite: 50] Effect of nanoparticle size distribution on protein corona and cell uptake.
[cite: 53] Effect of nanoparticle size distribution on protein corona and cell uptake.
[cite: 24] Nanoparticle size and surface properties determine the protein corona with possible implications for biological impacts.
[cite: 26] Effect of nanoparticle polydispersity index on protein corona heterogeneity.
[cite: 25] Effect of nanoparticle polydispersity index on protein corona heterogeneity.
[cite: 49] Effect of nanoparticle polydispersity index on protein corona heterogeneity.
[cite: 36] How nanoparticle size distribution affects ligand shielding by protein corona.
[cite: 18] How nanoparticle size distribution affects ligand shielding by protein corona.
[cite: 43] How nanoparticle size distribution affects ligand shielding by protein corona.
[cite: 4] Narrow size distribution importance for targeted nanomedicine delivery consistency.
[cite: 5] Role of particle size in translational research of nanomedicines.
[cite: 10] Narrow size distribution importance for targeted nanomedicine delivery consistency.
[cite: 54] Heterogeneous protein corona formation on polydisperse nanoparticles.
[cite: 55] Polydispersity influence on EPR effect and tumor penetration heterogeneity.
[cite: 11] Polydispersity influence on EPR effect and tumor penetration heterogeneity.
[cite: 46] Polydispersity influence on EPR effect and tumor penetration heterogeneity.
[cite: 56] Effect of nanoparticle size on Apolipoprotein E adsorption.
[cite: 27] Effect of nanoparticle size on Apolipoprotein E adsorption.
[cite: 34] Effect of nanoparticle size on Apolipoprotein E adsorption.
[cite: 16] Effect of nanoparticle size on Apolipoprotein E adsorption.
[cite: 19] How size distribution affects Vroman effect kinetics.
[cite: 20] How size distribution affects Vroman effect kinetics.
[cite: 14] Nanoparticle size dependent adsorption of dysopsonins vs opsonins.
[cite: 35] Nanoparticle size dependent adsorption of dysopsonins vs opsonins.
[cite: 15] Nanoparticle size dependent adsorption of dysopsonins vs opsonins.
[cite: 28] Optimal nanoparticle size for albumin dysopsonin corona.
[cite: 31] Optimal nanoparticle size for albumin dysopsonin corona.
[cite: 17] Protein corona ligand shielding ApoE targeting LDL receptor Trojan horse.
[cite: 37] Protein corona ligand shielding ApoE targeting LDL receptor Trojan horse.
[cite: 33] Protein corona ligand shielding ApoE targeting LDL receptor Trojan horse.
[cite: 57] Nanoparticle protein corona hydrodynamic diameter increase cellular uptake threshold.
[cite: 3] Nanoparticle size distribution PDI protein corona heterogeneity biological identity.
[cite: 7] Nanomedicine size 50-200 nm EPR effect renal clearance MPS clearance.
[cite: 12] Nanomedicine size 50-200 nm EPR effect renal clearance MPS clearance.
[cite: 8] Imaging Nano-Bio Interactions in the Kidney Toward a Better Understanding of Nanoparticle Clearance.
[cite: 58] Nanomedicine size 50-200 nm EPR effect renal clearance MPS clearance.
[cite: 59] Nanoparticle size curvature Vroman effect albumin ApoE opsonin adsorption.
[cite: 1] Nanoparticle size curvature Vroman effect albumin ApoE opsonin adsorption.
[cite: 34] Effect of nanoparticle size on ApoE adsorption efficiency.
[cite: 21] Nanoparticle curvature effect albumin vs IgG adsorption Vroman effect.
[cite: 22] Nanoparticle curvature effect albumin vs IgG adsorption Vroman effect.
[cite: 23] Nanoparticle curvature effect albumin vs IgG adsorption Vroman effect.
[cite: 32] Nanoparticle curvature effect albumin vs IgG adsorption Vroman effect.
[cite: 48] Nanoparticle size distribution control optimizing delivery stability permeability competition.
[cite: 6] Nanoparticle size distribution control optimizing delivery stability permeability competition.
[cite: 42] Factors determining the stability size distribution and cellular accumulation.
[cite: 26] Impact of nanoparticle PDI on protein corona heterogeneity and biodistribution.
[cite: 14] Nanoparticle size effect on opsonin vs dysopsonin adsorption ratio.
[cite: 30] Nanoparticle size effect on opsonin vs dysopsonin adsorption ratio.
[cite: 44] "PDI < 0.3" nanomedicine protein corona homogeneity.
[cite: 60] Nanoparticle curvature effect on fibrinogen vs albumin adsorption contact area.
[cite: 27] Nanoparticle curvature effect on fibrinogen vs albumin adsorption contact area.
[cite: 39] Mechanism of dysopsonin enrichment on small nanoparticles.

**Sources:**
1. [utoronto.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmuxbH1NYqbRGm3rU9WD6WfIg2lT7QdC_F3FlZ7l9VMIeUYlEyxzK8B1Nnb26k3J4ta7PDhxf3Q8pzCDaCuN2DMozDg1ikM8gkj5zI6Bnhaix8Ph2hxMp8Kpk0yjjQNYHjGb_m1UWGqXTcdT6sf66BjhAyFdgqi1gUo0Wa3XTL)
2. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZGopu1ibDVDgXTkh5OknBTQ-GggMsCianaeWMU90G3YE3sq7ypl6jWAJ3lCtu5C1OOLZkHtdjGhuDqM91ccIL-uf7qPk1lWKhmKlcQVnq0fXA4AS-ouZERbuN7yC_6mN7O-8_uTWwN9C3766wiirFGW4A5u6GbCX4_zXefRe7Ljs2pMD9_JIhgn_eBT09z8EeYUnv_uP26VRYfgyDcOFwqBz3pUeKheSZZ5mr36Vgbl5lg75enQRyCATplnDKVNtO42Gf)
3. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDcTCzZJSHMZp4epV5HXFBF70JCHbjAJgW4NPb7D2ju82KlYJsf-c_nrSidr5n7zRAJ1w2_R1sVJShJ1g2UJ5QyOIEItDjLbxLKg6pRCiW_-xtBnrYESeJH3TYiqLNokZprnmyk39d)
4. [diversatechnologies.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN8xLTb6qJX1nVq1dhNFiz-NvSPQolNBWc4tONU9w72eBh_Uif6Q6dWLIVBodENBw5efK7aVzktRDSGZkodTRzpyCD0-4MJhev9ckoY_EW6EYJ24PNazjhm7DxsYRrb4eqv4QcVtB5zxWiHVeO1GTiiPeF_-7yrTcS05HQGqjc)
5. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqiLUCHSXYuOxmkTE7UytkCKrm5NPvFw4Ra-RK1AFYdodYpOwq2KTb8gpm1wW3T7caV1ul0dZLPPpj-wI_Vlu0OxJnPhv5qpvC_zVSVhM-6NKbI5eDwia-8e9DDFcsnusewEoyUUIV0XBAU_5tVB7ryXCnh2_yaxroS_xebRsbtPLz3teVEFO0E9vOdC5MUjoAqs1SHaLC2kp94OBUAcBgdKbQtKoou8d5KqwLtLj3Usp0FZyXVXYChOfYci1AyfJa0Tdk1Zajjh_mrakXQm69fi2cLYOMPOEyDsvLqEHyIfxQV7BmuA==)
6. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRlSgan1HljMfnhy-2cwGO7bTARW3fBsVTj81VONpaHkVt11zykgaLsqJ45pw6CAXjytXx2WlRL9_2ZMQjXJgZ8xFZBXbxV0tu9HMp0-i2WJMmOHN3UutSxLbQxbp4f_0d6YElt1rJ-w==)
7. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGh_gHcbf4J7HWcI1weD_ietlz7aA_363NMKSyR4E3piPl7IrEoJtbmrCUcGbE3H4b6-dymDVPLaq-RmUzGWbGQW9GpqyBKC1TwOAbi7rKQ6eu0c-B4_4mVn5CJfG7On2nb8SKmVg==)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNG3cGE05CAjjCYZwMSwukbAgiCfwPrinhfMLRH1DepuAoAvtwXi3DzgfMdzUdVW_Muu-kDMXaUp-_25lM0Q8O23hQVeHYlFoCWPDE_HNSXWaaNZSkdw2Vhe1_FXn7_t_56dZUCiLZ_eC_PGK54_AwtUG9mj958FyGB9OpyREfPRA7a9k6m6BqWdGpJ3A5_wrdKuAzEPw2nMoi_wKQJXssOJtFQF0mVpuuWL-7TQhuJMJXJgcPD_otpR1KRad80hciIh14_NHutmwIID8k)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqMsmZmzUhqJRpq_R7i48zJpPuqhO8Qkyt1H6rBDpq5pDmthThglUsNz5Kp7Ljp2kVs_SOoaa7QMV6yAt-h7r0VXd9rhJ9e01swV8Fs2ZEAxPpbvUXrmInBu7KSLvdmi90CBcbpO6G)
10. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVkDWZL2ye83tGCbO3kDYW2v5upbEQXtic9rNXLFFDdR5IIJM25QaT71TUptKfhoq82OZc1ZQjwn2jpvfX9Xw3RSryQ-f72B5Fe3R0YXVFDd4sTsNAs7cV2BmyxVVGLiT9aEDAsRxD)
11. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNeXP98Y1_qpgHzwwb9mJYAJ80ZGHI_K9nFTKHgUoivuf94AEAfI9lOjznb0AGVhPLvrwpeT2kF7gP9KHZY9uwtYh7uSntRO_N_yLJkmokGPnkiO2OdJEdndXS4WhBfAPEpBlknMdZ)
12. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqV8DtIj4-MnrsmndhRavm8uPkJEuUe8QUaN-c9eE0rvpYZHvRPKGU4GxyyCZz7RYqccVpH5DzxmtJqGteNXt4wlQzNKBX6e6o1rgN37zIhuVq6pVFhAJ5hwBflYICvy71GM9n72JOh1KQ5IjvYGlf86y3Zj1A0Ey1AFOg8cAJI7Bfg-AIEfCU_Quf5zV2ww==)
13. [royalsocietypublishing.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDZ_OznrJ7OCrGdpbvINLJmdn60pfgWfKEF1zA5AWpxNMkiGzZgp5KAbWhu1NSHRp445Yw676qjTt4J0w6ABymXMgRzjYRoizxOMBe9MaFLgOsXObl3sFGSOZUqwswNAB3N9DkNke24fG0vK2c5LWcNl8ndMf6DGFeGthEaJq1jX2TCgu9CIFM9yHf7ccIjlBmcyAJAsjJ06QbI0LHuheGqTqpPnhZ)
14. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHe3jWqaIH4etzHCUumhcP1imBtxzYZU1zyO1NybGMABPF6N_y-ehbE1mb0lXLfdMiZhe160mgQ9-5u1oJ97222knuY5Q-XjFvQ44dWhXdovDe9JZflzO1xn1VHKa419BKwdbAFomA58u0W7ybGqLyA8mubvuVganVSeSmYciaiYGx2E9skKm85Nox-flOfEIYbIiATFdz0lwnuyHP5rJ8A6_7FmCXBHFE9hzbu)
15. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMWOEuFOON0NXgQ_FCK5pAep3cR_MnNZd8o6_nFbFmvjN0GbipUzANI_16MMY8H91YpTjGp5_QdywSkrekuqPSvaQaBNro5GE49_vGnKe2qm1UvsqQebLm_Vws1WgU619Eb7svSSmM)
16. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHGBSH2cl1-CIVsztUWFBGZ1I0Lhx0ditlxcSTMZz_6IPFMipA2uxVAIFXFqXsWje0emuAeE1mQDASBMoMylmjl38MDdUr9gSOifb46dNGox0Dmq641qdlG1atY0dp2PXFmQU8NUDWD4cZBg==)
17. [liposomes.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHs8ZZwCx5MeWpcBN9Zyc7gGzIYz02lxMzLyLZg0qHKQ54TFXQDgpHMgv2YoungU71cIuG4bYSUyDpoQEQOaCnJqq_KVhM4lxeruKvVgUFE3Gh5KFhhZijpA6GQPt-iHHuuuYHMROD5vZIhT03rWAEFRw2zEwl2QnKLYCGNKdlyItMWovzAit7mqBfurShRCzdGaXShHbL6JNo-BJbGegXYp5bklrKENiQWYbBeoou7ncQI-3hAw9xQEFKKGfbpHAIMnZ7_VJ8BDATcKBoZKge8FQIdIPw=)
18. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJ69dPgePVR3V7ASebZRefBvJJdm6K3g3Dr_nnlxdtOjLJ1D_nav3cXEatyDxAXcnXfBa61sjRLx2nHDNkj-ujLefU1X2x8Pw-XnUXCu5BqLxsZzxEjpsanbfxhSZKD-Ft)
19. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEun-6IHSkgtUJs5O5Y4NLj50xm_Yij2nFEW9W9mOhwWnnXugN9zAqV7QEvZ3B2WiwpfLGGQqDS1zLAAVVuo2HPrQNGvnwD2YoX7RyF3Gj91FaGeDAjqEj7_-lOl_2omIXskp2Yil-Y)
20. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLway3ItQ0RJNZLD3_yuCgEz-3XWNRVLItzMORswXRg9OuF0H422iraFM5wb13a4Dj0cl5T9qvxsCw4p43BwRFIlMtoNrtIb4SWtciVynKHcen-X0AER-QwEm-nRC5j0djs93pjgg=)
21. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGN5wrQXb5KYmC87_AMqIUSU_LY8ilrB3b9kXg35pbAlPUTMcrcwAsVSu3zOKcDnOeNNLclZPWj4OLXwNQxk8jxwX4kfUUPQ0nk6xlpGrKDNsTJptIvyFx4I42ZsPP5sg==)
22. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpy1vagRcVRix0ISqIz14zm1kpKjXBMo-Gj8TqCVA3he06PmPbzkED4tpPH3LqhoJZzeGx8E3SEjJ9vBuwLOSizGMGt1cjWCJ_vv08X4Tf-Hk-obbKhK-ncHESbxGzfxdT35UvCqqcZaumB5v3Tbjijv17T105xvBuXddI8D1NN2rMNxmqIl8lzkAidnAo7llilqNKMorOA519Y-TIH-sJ5SKGNjCYV9FNBYSDE15JWrXI8uhC4EowhhlqlncofBEhWQ==)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYblcbfW_lP9iYdqKLiIIGtsWx7WFWAXif7o97_74B5UtwRHyBHgPwo-s3n0DEO8z7X672VRb83vXXnh4lhV_XBcQXXHBuxzyutE4EbpcEYU164-YFHiApIikKwqDiGFH0CPyAadjElJ_4IkWDV8pWyCdlc6HKETPIyLKSsdIPYYgfAK97iu_PImbQcTRTm0O_0Zz-OA2DbGZW6Wx1v8xetfcvPHI0HVLjVy6zv_wkeXK2kkT3e6NcU5blVng=)
24. [pnas.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNu_87I5IT1C-wgF5VLW_K-k1DaHUmu3nzhUap0WvUH8Xijpr-fklUJxKmgK9dxkHUzdFYTgGW909WPedOoabG-aij317bZbGqDUOGINP607oClacWW8OMIYNXMJpE-C1km73SMDU=)
25. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUph1xcrhcofbfbUV9HgbGFzyUbbINlU9awOLuAaj93tS5G31g7gwb3gczhSa68vueAdsr8CY0iTptcdVZhSmNJBv23OyyB-yISZJAPOnnGJD2Yy-drFUw37lQjmreew==)
26. [Link](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE99QBHaGPmHqZF1dAnUPRdGgb7Fv2f6_bcOkQOtbJ8hQgiPZf6q-p3s8jnj2j7fVBk-YZS07wzOernwp71zFRV9y4MzGdbxbGqy2iVKAHo1CEn4zkihbsc45TgAcAtgZEfE5Kzm-2tHA==)
27. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHg9Q9sgokxUIpLUH7lGfCjX0As2COY2TZJ1K5qLVWyLPdSNR6Fa_0caN4DTXa4sNMsRJ9EeeLIxnTY-T2hfX2I_LiKkX8A7kpBMmLebm8rNlNm-HZyMseZ9X-QMj3YqSNTW9mgeZEU)
28. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN1anU774BC3HENVYNLw8TMP_Kllo07scEtKILgua2QxnUxQ7Jwvh8APf8ZzuNiFYp2jlCs3mcD_NPrFGlcgDyWxdn1LwfVLgjG4KVcvRZ_gNp9pAV1zVMVVpzVangPrUbePAs7GXP)
29. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHO1NnIuoUNnkeB7qlVnd6pAF2fVcbPEHyRq8S5v7brNmIyO5XrPGX0nnQQLjuRTcDbmigq1aR-QiZzV6ATh3YBLixMTVfEEpS3r9q3lZC9R_jl1_t_887woDqwDNvN)
30. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL9noBOFPwx-VcH-x2SRzNhfbxKqSPfXV-smrx6r1U3TKnQm-JGCat0rSV0BbXni4O86erqI8r5RiCUR8EdGI5hkc8LQ3TtRCYih_kWHOcpiaDEI9FmwINXq-WcHWTxyCPkVh1cIcf)
31. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsd5YzKsJhU8HFCACmmQbJmJxec_xiEjUPWatiOjvNyqXD6QdDjHRR8Wp7snxNPy-GiKmDd3nxQ7EnSAhO0fE_s4EA2_OunnU48dAiCKLhP67uRZXtZv3_-_jgNeJKvxUkqadiOvRq)
32. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqOS133-GmOg2ax_Tic08x5RNAiYKl8chVxa3ULtJczN6x0oKIOHTFt5gvn3xOjFWHzI0Bv_Nyo1JYNABqwtINHF9jfZ-GqXyEKIXMsNlZiRifkmUMmpRjh8-DgfRvFT9jJgWejocD)
33. [beilstein-journals.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHC3uJKIYsmSXEkjcxYfGxjAScXosnohSpNXYWtH1Yil_FMQS2Eyi-Tuz1JbnFc2Pr8VaMVhFnYf5Nym0Ayy3irDX00oH3GCODBuNtjbEMV0dVRZkLLU-69ZrOm0heQukQqY_NiW-MFQD7RIxQENg==)
34. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHG4VRNCXqdFr48YWipo1QwQ5Bj7ZA7m7ZV-1mNW8Ig-fBH5c7DQ5aAxYObkIash8ASCtyb96O73AgTp15HyjOJRSfvUKuFOEtHGeI8VvKM7Xn7-I_diJPLOj9MHrO1aMyiFVR1HC-VcQ==)
35. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2tXVRWAbm5H0KKguQ5VoPmJvtt3QKuJh7C79TIARYjuMQHQexUoDAA8GyuIbD04_NJXQ2pc7_KivVT_lWF4Ey3UnUJpyaerMLsnRpuSjyGEZYJ5ubhJSVPiFcpwf37xbFdxfMaAPf_7cW_pDvzL6yTsCmgagpLw==)
36. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPFD1k7w2mpJ61YZ8pXQ0JawbKTc9JoOl4Cb5dogGUT6hAe3v8e3iZjoR9sezEFzKUC4lyEjO-XGoXJ4IRZEu6-15--sFkaze0CFJluv2SsyUGFB4HfItI3RT2MhhJoQ==)
37. [scienceopen.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHi32WwsaUfNrDFS2UZsHIUtVzehiv3x3-0t819dYC2NtyW7axNH86Zgm-XZvi7_I7MeP26gVHiUe5jtFNWkjVtETf46L01AbUPtqD7JQMA5r9modpcgM1SUoo-Vnn7IRG_kZTUhfEgIZyEqqo35V7uXVBSG_NR63Hl569_PrCkYhSR8hD-74HR3O9wMstHOlulYvfSeJp-S3UMC017v7t3OOVpb-NVgjmYF3kiofA0IiSpUkXE8_8dyUDjcg==)
38. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE66BuCn3RD8pWd-yXBVp4jaZG_Kl3XiEqT_ITI1SafXw59QSTs0Koad47KMRrtQC3cJeTOGP2shqgWUx0AL9hBW3LYIk37P4EdJEox310WlHSkoRAQWztykvBPd3v2miEJdPkJMOaZL6ukaeCF2a8T0ktQkzptZVtaIQOpvdVIfbv3_DUFSiHhA74e3P-cUP_pPOaJWjMH5Rm4C_XuCBz9dsMp1kIxmbIUtBIMiOTzFZhauJTf0LlCuoa0mYHj4nGw_cInx6OiKQZcJKcCjqDzfHWkrwFLPgweirioxeUcibFjPloKw-YsDZHjqKC0bUslF2yL1Q==)
39. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFihxyqkii5XorqY_KHmKDmTp3_uM1qOPpsrZW3gCIkoAMG5KKTDKwgcYJ8a6SPlFkY2kbaDoDS9cdggfL9sVOtqL826YQbNbGacQV0X7SyXQ1Efv_XEBiEG1LjPdZS8W5kLKHbu_h)
40. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_fDCtxTv77IL2-Vozbl5novTHZgz2DcZQPjIzjpTyZJbIp95iLniOW_-HwmGLidXcgXv1LtxEQcvVygWSuyUblQHfMaSl-ErMxC5F2pA6tExocwCe95UwOLhtEA5r9ei3WyytmcVI)
41. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbsUZGun5G_liO7gN6RqlmzmPDTQdLxY4Lo8A09h1VAC_Xn9bE7NDheKNTcl3Vt8omzYXKP0VDYOPUVwLxkv9D3I7wZogEuycfOq1gAPWj5Y_2i3kde4e0A1qEiOn0NI4OBnOg2ikAQIrTLI3UNKzWPFJhbRDiVzGijhhAijRvMsE-9pmXAZeqUui-2AtRD6nqfVx9Foy4ky08ylk6-oM54KmjdR2vkZV6mCg_Ecw4i2TS)
42. [dovepress.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgovwpf_DVbnAeFKbHptkKGDl90Cc00b0iy1jlq-wYssCeLqZsMlxtw3EDvx3YKZLyVh5OxINDNtxt1SugOvzrBv1wBA29N6GixzE8VBPxx6xyCp1zJMuPJG2FWLAufNGyioCux4qrGEw2o4ie_pTzTUbCzwzWvxFL_OhSg5IPZsuWQY1Y2VI4gZoRcjz1b4ArGmwvx-_2vuwY7Cx_ZIi1RLDoGZ-TXxVuZovSR4bwwsk-c-fKc0uI5aA=)
43. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdldrG1XHel_hAQNZdA0usMgHi82eGvCKFqrc2Hw0pHFjOgFwiZJitcurq2PkDXpYpxQ5lkrU1ERi7ob6IuCSMKnqu30k-TjlGSsZZW7TxE9CaTY56CeBJQeCaAlyAjtUtboSD6wX9PHBHDE8_mUTDI3mcIg==)
44. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbzLmcwekWH4sVMzW88ncXyhkZCl0oAvHCL5dAEK1I6sVS53RCZvzcTtV_HEXnk7R1omxilEQWiFO6rhgXQFzb-fC38XHcvsOqlwY2mvkkQ9ehOtjlnS7NZIopY_sDfOMOOgWDGEhTXus=)
45. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEla9nyf59lfjNTwYsr9shoArEPkEHQ1cBylmfO8bZFiBR5WIFj-2Xr1Sf2wQJ1qmNXcCLXykVKASjYTuOxxLEIqa7oCjfWTTZfTEAFZ6h2DsuyKkZtJ3kN71cg1OG9DaRUEqPjVhMHj7ihnupgbzPLRHBOfbqrM7a7yRBa1LKGin9P-wGpKYk0o5oNp8tFoBaAjz7J_AmMN3lxbrqSIYbPkx0hF3X3SBMlFbKWA22JVUiF)
46. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUkkUtoN00FJqzF8J1tMVrjI4blvN2cv8ghcDgUJUcQQPaaiLRFLVpz6gHYpOtIeIVrY3F0qnVkLqR0stKIaafwLxu4C3QNUWmcP3tzre7odIbyDFmLYkrhJ8Vg9T4)
47. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4IBkdTDZZATAYLxutwxlnMZQiWoTJMRTzaF6Avp_SrQw76Tx39eD_24OiOeiPgLGj0OkJkQbWjXKaRz5RFSVFM_8bsmKZ5TfOKJkWhkk1ofhF-6JzqxsV7YDUOa7wLRMn9yJUgSbC)
48. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNowlCpnkWRaaBgXjLUmlCjeaG-OYEVI8A_c1KtCTw1YF-8-jk93gBum0esCOFL6_xPnyYaHX105eS_djTOLWw0_AL5LY807Tc4ek3HTlfEBdgxCv0tdw0FaI7vBsyfzK6I98yhI1Nz_mlWmIfq3Vk6vD9coTA9Q==)
49. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOlG4_PVFs4VoTXXkFVfr-9i30fjEzpZGU2u7kAvO1amXsXnYv1cOhkK9s4vWNvP9Sx8GSXlc89r_3n10JaCdvvYo50YMsMAyQSszmjz1ETm1PwLCWMIRXLA0zA_Y3giUdjUA8qOWT)
50. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF1MWjWw97Gh8ZGI9hhZ65moJx2_WHuB4vlt2b2SCiYUwG_z2E4-sEGAsOVLlTTFM1XImNmAIu9aB_lpuoDhdsAIGYBvZ0vLZAY65wW7A3bTUUpa3WgXzDBYMgle5dyvPpRY2OW3L-M)
51. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAzmqxUbctmfq2kq976_A4j6TWD8BCDzCR8O1dPXrhKyq5k-dAEUw8c1Mz4V9L0dmmMYpvLpxJD3r6hB5XVbC4oIy0MokUryIivrbZy4dbpSXlnMtbhRJhNbNUW_Cv78dYO_Pk6Urt)
52. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZs-vFphzc18v9fcE94kKUwQG4a3bmuWYji9W0i1VG4BCVG7mc_l--4qaHRqe1Q-nTebFoq19gDLN7cxei1Jj0K2fgmHkhELfQzPCPcQc24TSRjt9RK87pe_7LNBDiK9ofOOUV0RdPVR-n4DLriziLudXEds_2XO9WOZ7ogJs0_SRVU3DjGj_34hDcVC7V6NJUhkmHK6HnMQQw8X55s9Gq8otlZ48yu0xlKb8hDDmvdw7HHrnPHFzdaPvP0uNShSGWA0SwLJsYTMcYrTT02xr1H5aizAWi)
53. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQER8sqRmmKrJvJsgGuSgxKMOHsgIKgzeO6mvF75IP-y3vUrmVDoxkwqxxkLlwzTW2OOPboxHWz7dT-4-7mmUhGS2tIbzfgS-nIhle6TKIT0NVep4sKwYOYyB-n1a-02Vbc=)
54. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiicWcNzZ6hWkNMY9QlZrG4ein9KIJsK6kpuM3rzjQJcIAFlWQW5fiSoFmOfiwuz2O4TjZL-Xx9nKQuQJExJHwIZdtc2pQBSqHDYVNRMRTE5oIXu0-HsMcHvWaIsubinTpCQI9zSs6)
55. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnKy6juC4U0_PuiN1NbRCB3dZPkyl5mBgvkbq9tDXu33VJONkmNskyXGE1JYHqV-L-X3pceQWVvYWVNQF9MHM6OVbUrtG6qRgbYjE64Lzj8qjjU-CwGl-LK-rdHudntg==)
56. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_AymdTNq9I4bk0GcvEIBo5ruoaNhyyRFCzGYTuCog8xbAdDZ6JB-S0kXqz6xUu5W4NQ2Y8BGfo9mbZoqtkwNIlIWK7w_KViO9BWXt7gsBqct248olYDof_QNbVnEiEA==)
57. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5IxO3ZGIUxIpn5Pg9WrMnWtjK0TxFwZoC8opn8DyHEWk9tqzcVPQleyqbCIu6hK__GHtahxEsvz8Pur6Yq_oJHaJpKtp5yoRa1p1opwpqIj-0h9t5tXwd3ww09fimNBGoQRkTh12O)
58. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgUq6-FwKfbFcQU9In0-W3aNeDYyoLxqhrnXomuw2UGzDCTcznVI4LWj9wfxL0Hp7IH1ZTIPgAu0EjvDtZfFUNSpIfViZUxXJkzy7rJoiPRyfyRBBq_w3ZMNq1JuOwhDA=)
59. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHH1svq4yC70ZkZXgZjGorfn0bDXaXF5XGhPBjaHgzs1zRdWhGjOe-8ki62TNgha_u8wAIAaniS5_X5xSadCdDIE4mRUHDIA35yPmS5kqotNTxmdAgbexA0BEkYL7b18u9R2wpktM8GkdJRV6pv_TrP6CUhDWmzXsVyBvdl6gAtD9PE5VkQAI0dE7DkB1qpUxs_KdlomArqhLREYqaO-oAKx32hTDbo1WnpbHf1AYCs8phZF-XJsiBXQgBvGsVM1SM=)
60. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6LgCDRpjoWbO_pc23bZH-JBpIHTv25aPstaHewtzMLoXhVPeWAzYLfdBfFhDBx8s6HYPsfeQVzAbjBqEuvixjvHHBNycEqoA-XjF-ClnwdmWXEGf6qGIP2IokDvkGBQ==)


## Annotations
Annotation(end_index=2953, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDcTCzZJSHMZp4epV5HXFBF70JCHbjAJgW4NPb7D2ju82KlYJsf-c_nrSidr5n7zRAJ1w2_R1sVJShJ1g2UJ5QyOIEItDjLbxLKg6pRCiW_-xtBnrYESeJH3TYiqLNokZprnmyk39d', start_index=2938)
Annotation(end_index=2953, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZGopu1ibDVDgXTkh5OknBTQ-GggMsCianaeWMU90G3YE3sq7ypl6jWAJ3lCtu5C1OOLZkHtdjGhuDqM91ccIL-uf7qPk1lWKhmKlcQVnq0fXA4AS-ouZERbuN7yC_6mN7O-8_uTWwN9C3766wiirFGW4A5u6GbCX4_zXefRe7Ljs2pMD9_JIhgn_eBT09z8EeYUnv_uP26VRYfgyDcOFwqBz3pUeKheSZZ5mr36Vgbl5lg75enQRyCATplnDKVNtO42Gf', start_index=2938)
Annotation(end_index=2953, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmuxbH1NYqbRGm3rU9WD6WfIg2lT7QdC_F3FlZ7l9VMIeUYlEyxzK8B1Nnb26k3J4ta7PDhxf3Q8pzCDaCuN2DMozDg1ikM8gkj5zI6Bnhaix8Ph2hxMp8Kpk0yjjQNYHjGb_m1UWGqXTcdT6sf66BjhAyFdgqi1gUo0Wa3XTL', start_index=2938)
Annotation(end_index=3358, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqiLUCHSXYuOxmkTE7UytkCKrm5NPvFw4Ra-RK1AFYdodYpOwq2KTb8gpm1wW3T7caV1ul0dZLPPpj-wI_Vlu0OxJnPhv5qpvC_zVSVhM-6NKbI5eDwia-8e9DDFcsnusewEoyUUIV0XBAU_5tVB7ryXCnh2_yaxroS_xebRsbtPLz3teVEFO0E9vOdC5MUjoAqs1SHaLC2kp94OBUAcBgdKbQtKoou8d5KqwLtLj3Usp0FZyXVXYChOfYci1AyfJa0Tdk1Zajjh_mrakXQm69fi2cLYOMPOEyDsvLqEHyIfxQV7BmuA==', start_index=3343)
Annotation(end_index=3358, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN8xLTb6qJX1nVq1dhNFiz-NvSPQolNBWc4tONU9w72eBh_Uif6Q6dWLIVBodENBw5efK7aVzktRDSGZkodTRzpyCD0-4MJhev9ckoY_EW6EYJ24PNazjhm7DxsYRrb4eqv4QcVtB5zxWiHVeO1GTiiPeF_-7yrTcS05HQGqjc', start_index=3343)
Annotation(end_index=3358, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRlSgan1HljMfnhy-2cwGO7bTARW3fBsVTj81VONpaHkVt11zykgaLsqJ45pw6CAXjytXx2WlRL9_2ZMQjXJgZ8xFZBXbxV0tu9HMp0-i2WJMmOHN3UutSxLbQxbp4f_0d6YElt1rJ-w==', start_index=3343)
Annotation(end_index=3664, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGh_gHcbf4J7HWcI1weD_ietlz7aA_363NMKSyR4E3piPl7IrEoJtbmrCUcGbE3H4b6-dymDVPLaq-RmUzGWbGQW9GpqyBKC1TwOAbi7rKQ6eu0c-B4_4mVn5CJfG7On2nb8SKmVg==', start_index=3652)
Annotation(end_index=3664, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNG3cGE05CAjjCYZwMSwukbAgiCfwPrinhfMLRH1DepuAoAvtwXi3DzgfMdzUdVW_Muu-kDMXaUp-_25lM0Q8O23hQVeHYlFoCWPDE_HNSXWaaNZSkdw2Vhe1_FXn7_t_56dZUCiLZ_eC_PGK54_AwtUG9mj958FyGB9OpyREfPRA7a9k6m6BqWdGpJ3A5_wrdKuAzEPw2nMoi_wKQJXssOJtFQF0mVpuuWL-7TQhuJMJXJgcPD_otpR1KRad80hciIh14_NHutmwIID8k', start_index=3652)
Annotation(end_index=3829, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVkDWZL2ye83tGCbO3kDYW2v5upbEQXtic9rNXLFFDdR5IIJM25QaT71TUptKfhoq82OZc1ZQjwn2jpvfX9Xw3RSryQ-f72B5Fe3R0YXVFDd4sTsNAs7cV2BmyxVVGLiT9aEDAsRxD', start_index=3816)
Annotation(end_index=3829, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqMsmZmzUhqJRpq_R7i48zJpPuqhO8Qkyt1H6rBDpq5pDmthThglUsNz5Kp7Ljp2kVs_SOoaa7QMV6yAt-h7r0VXd9rhJ9e01swV8Fs2ZEAxPpbvUXrmInBu7KSLvdmi90CBcbpO6G', start_index=3816)
Annotation(end_index=4022, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqV8DtIj4-MnrsmndhRavm8uPkJEuUe8QUaN-c9eE0rvpYZHvRPKGU4GxyyCZz7RYqccVpH5DzxmtJqGteNXt4wlQzNKBX6e6o1rgN37zIhuVq6pVFhAJ5hwBflYICvy71GM9n72JOh1KQ5IjvYGlf86y3Zj1A0Ey1AFOg8cAJI7Bfg-AIEfCU_Quf5zV2ww==', start_index=4008)
Annotation(end_index=4022, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNeXP98Y1_qpgHzwwb9mJYAJ80ZGHI_K9nFTKHgUoivuf94AEAfI9lOjznb0AGVhPLvrwpeT2kF7gP9KHZY9uwtYh7uSntRO_N_yLJkmokGPnkiO2OdJEdndXS4WhBfAPEpBlknMdZ', start_index=4008)
Annotation(end_index=4273, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDZ_OznrJ7OCrGdpbvINLJmdn60pfgWfKEF1zA5AWpxNMkiGzZgp5KAbWhu1NSHRp445Yw676qjTt4J0w6ABymXMgRzjYRoizxOMBe9MaFLgOsXObl3sFGSOZUqwswNAB3N9DkNke24fG0vK2c5LWcNl8ndMf6DGFeGthEaJq1jX2TCgu9CIFM9yHf7ccIjlBmcyAJAsjJ06QbI0LHuheGqTqpPnhZ', start_index=4260)
Annotation(end_index=4273, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN8xLTb6qJX1nVq1dhNFiz-NvSPQolNBWc4tONU9w72eBh_Uif6Q6dWLIVBodENBw5efK7aVzktRDSGZkodTRzpyCD0-4MJhev9ckoY_EW6EYJ24PNazjhm7DxsYRrb4eqv4QcVtB5zxWiHVeO1GTiiPeF_-7yrTcS05HQGqjc', start_index=4260)
Annotation(end_index=4648, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMWOEuFOON0NXgQ_FCK5pAep3cR_MnNZd8o6_nFbFmvjN0GbipUzANI_16MMY8H91YpTjGp5_QdywSkrekuqPSvaQaBNro5GE49_vGnKe2qm1UvsqQebLm_Vws1WgU619Eb7svSSmM', start_index=4634)
Annotation(end_index=4648, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHe3jWqaIH4etzHCUumhcP1imBtxzYZU1zyO1NybGMABPF6N_y-ehbE1mb0lXLfdMiZhe160mgQ9-5u1oJ97222knuY5Q-XjFvQ44dWhXdovDe9JZflzO1xn1VHKa419BKwdbAFomA58u0W7ybGqLyA8mubvuVganVSeSmYciaiYGx2E9skKm85Nox-flOfEIYbIiATFdz0lwnuyHP5rJ8A6_7FmCXBHFE9hzbu', start_index=4634)
Annotation(end_index=4843, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHGBSH2cl1-CIVsztUWFBGZ1I0Lhx0ditlxcSTMZz_6IPFMipA2uxVAIFXFqXsWje0emuAeE1mQDASBMoMylmjl38MDdUr9gSOifb46dNGox0Dmq641qdlG1atY0dp2PXFmQU8NUDWD4cZBg==', start_index=4829)
Annotation(end_index=4843, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHs8ZZwCx5MeWpcBN9Zyc7gGzIYz02lxMzLyLZg0qHKQ54TFXQDgpHMgv2YoungU71cIuG4bYSUyDpoQEQOaCnJqq_KVhM4lxeruKvVgUFE3Gh5KFhhZijpA6GQPt-iHHuuuYHMROD5vZIhT03rWAEFRw2zEwl2QnKLYCGNKdlyItMWovzAit7mqBfurShRCzdGaXShHbL6JNo-BJbGegXYp5bklrKENiQWYbBeoou7ncQI-3hAw9xQEFKKGfbpHAIMnZ7_VJ8BDATcKBoZKge8FQIdIPw=', start_index=4829)
Annotation(end_index=5033, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJ69dPgePVR3V7ASebZRefBvJJdm6K3g3Dr_nnlxdtOjLJ1D_nav3cXEatyDxAXcnXfBa61sjRLx2nHDNkj-ujLefU1X2x8Pw-XnUXCu5BqLxsZzxEjpsanbfxhSZKD-Ft', start_index=5020)
Annotation(end_index=5033, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmuxbH1NYqbRGm3rU9WD6WfIg2lT7QdC_F3FlZ7l9VMIeUYlEyxzK8B1Nnb26k3J4ta7PDhxf3Q8pzCDaCuN2DMozDg1ikM8gkj5zI6Bnhaix8Ph2hxMp8Kpk0yjjQNYHjGb_m1UWGqXTcdT6sf66BjhAyFdgqi1gUo0Wa3XTL', start_index=5020)
Annotation(end_index=5836, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEun-6IHSkgtUJs5O5Y4NLj50xm_Yij2nFEW9W9mOhwWnnXugN9zAqV7QEvZ3B2WiwpfLGGQqDS1zLAAVVuo2HPrQNGvnwD2YoX7RyF3Gj91FaGeDAjqEj7_-lOl_2omIXskp2Yil-Y', start_index=5818)
Annotation(end_index=5836, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLway3ItQ0RJNZLD3_yuCgEz-3XWNRVLItzMORswXRg9OuF0H422iraFM5wb13a4Dj0cl5T9qvxsCw4p43BwRFIlMtoNrtIb4SWtciVynKHcen-X0AER-QwEm-nRC5j0djs93pjgg=', start_index=5818)
Annotation(end_index=5836, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGN5wrQXb5KYmC87_AMqIUSU_LY8ilrB3b9kXg35pbAlPUTMcrcwAsVSu3zOKcDnOeNNLclZPWj4OLXwNQxk8jxwX4kfUUPQ0nk6xlpGrKDNsTJptIvyFx4I42ZsPP5sg==', start_index=5818)
Annotation(end_index=6151, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYblcbfW_lP9iYdqKLiIIGtsWx7WFWAXif7o97_74B5UtwRHyBHgPwo-s3n0DEO8z7X672VRb83vXXnh4lhV_XBcQXXHBuxzyutE4EbpcEYU164-YFHiApIikKwqDiGFH0CPyAadjElJ_4IkWDV8pWyCdlc6HKETPIyLKSsdIPYYgfAK97iu_PImbQcTRTm0O_0Zz-OA2DbGZW6Wx1v8xetfcvPHI0HVLjVy6zv_wkeXK2kkT3e6NcU5blVng=', start_index=6137)
Annotation(end_index=6151, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpy1vagRcVRix0ISqIz14zm1kpKjXBMo-Gj8TqCVA3he06PmPbzkED4tpPH3LqhoJZzeGx8E3SEjJ9vBuwLOSizGMGt1cjWCJ_vv08X4Tf-Hk-obbKhK-ncHESbxGzfxdT35UvCqqcZaumB5v3Tbjijv17T105xvBuXddI8D1NN2rMNxmqIl8lzkAidnAo7llilqNKMorOA519Y-TIH-sJ5SKGNjCYV9FNBYSDE15JWrXI8uhC4EowhhlqlncofBEhWQ==', start_index=6137)
Annotation(end_index=6540, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUph1xcrhcofbfbUV9HgbGFzyUbbINlU9awOLuAaj93tS5G31g7gwb3gczhSa68vueAdsr8CY0iTptcdVZhSmNJBv23OyyB-yISZJAPOnnGJD2Yy-drFUw37lQjmreew==', start_index=6526)
Annotation(end_index=6540, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNu_87I5IT1C-wgF5VLW_K-k1DaHUmu3nzhUap0WvUH8Xijpr-fklUJxKmgK9dxkHUzdFYTgGW909WPedOoabG-aij317bZbGqDUOGINP607oClacWW8OMIYNXMJpE-C1km73SMDU=', start_index=6526)
Annotation(end_index=6684, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE99QBHaGPmHqZF1dAnUPRdGgb7Fv2f6_bcOkQOtbJ8hQgiPZf6q-p3s8jnj2j7fVBk-YZS07wzOernwp71zFRV9y4MzGdbxbGqy2iVKAHo1CEn4zkihbsc45TgAcAtgZEfE5Kzm-2tHA==', start_index=6674)
Annotation(end_index=7251, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJ69dPgePVR3V7ASebZRefBvJJdm6K3g3Dr_nnlxdtOjLJ1D_nav3cXEatyDxAXcnXfBa61sjRLx2nHDNkj-ujLefU1X2x8Pw-XnUXCu5BqLxsZzxEjpsanbfxhSZKD-Ft', start_index=7237)
Annotation(end_index=7251, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHg9Q9sgokxUIpLUH7lGfCjX0As2COY2TZJ1K5qLVWyLPdSNR6Fa_0caN4DTXa4sNMsRJ9EeeLIxnTY-T2hfX2I_LiKkX8A7kpBMmLebm8rNlNm-HZyMseZ9X-QMj3YqSNTW9mgeZEU', start_index=7237)
Annotation(end_index=7661, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHg9Q9sgokxUIpLUH7lGfCjX0As2COY2TZJ1K5qLVWyLPdSNR6Fa_0caN4DTXa4sNMsRJ9EeeLIxnTY-T2hfX2I_LiKkX8A7kpBMmLebm8rNlNm-HZyMseZ9X-QMj3YqSNTW9mgeZEU', start_index=7651)
Annotation(end_index=8068, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmuxbH1NYqbRGm3rU9WD6WfIg2lT7QdC_F3FlZ7l9VMIeUYlEyxzK8B1Nnb26k3J4ta7PDhxf3Q8pzCDaCuN2DMozDg1ikM8gkj5zI6Bnhaix8Ph2hxMp8Kpk0yjjQNYHjGb_m1UWGqXTcdT6sf66BjhAyFdgqi1gUo0Wa3XTL', start_index=8059)
Annotation(end_index=8577, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNu_87I5IT1C-wgF5VLW_K-k1DaHUmu3nzhUap0WvUH8Xijpr-fklUJxKmgK9dxkHUzdFYTgGW909WPedOoabG-aij317bZbGqDUOGINP607oClacWW8OMIYNXMJpE-C1km73SMDU=', start_index=8564)
Annotation(end_index=8577, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDcTCzZJSHMZp4epV5HXFBF70JCHbjAJgW4NPb7D2ju82KlYJsf-c_nrSidr5n7zRAJ1w2_R1sVJShJ1g2UJ5QyOIEItDjLbxLKg6pRCiW_-xtBnrYESeJH3TYiqLNokZprnmyk39d', start_index=8564)
Annotation(end_index=8901, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE99QBHaGPmHqZF1dAnUPRdGgb7Fv2f6_bcOkQOtbJ8hQgiPZf6q-p3s8jnj2j7fVBk-YZS07wzOernwp71zFRV9y4MzGdbxbGqy2iVKAHo1CEn4zkihbsc45TgAcAtgZEfE5Kzm-2tHA==', start_index=8887)
Annotation(end_index=8901, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDZ_OznrJ7OCrGdpbvINLJmdn60pfgWfKEF1zA5AWpxNMkiGzZgp5KAbWhu1NSHRp445Yw676qjTt4J0w6ABymXMgRzjYRoizxOMBe9MaFLgOsXObl3sFGSOZUqwswNAB3N9DkNke24fG0vK2c5LWcNl8ndMf6DGFeGthEaJq1jX2TCgu9CIFM9yHf7ccIjlBmcyAJAsjJ06QbI0LHuheGqTqpPnhZ', start_index=8887)
Annotation(end_index=9620, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN1anU774BC3HENVYNLw8TMP_Kllo07scEtKILgua2QxnUxQ7Jwvh8APf8ZzuNiFYp2jlCs3mcD_NPrFGlcgDyWxdn1LwfVLgjG4KVcvRZ_gNp9pAV1zVMVVpzVangPrUbePAs7GXP', start_index=9606)
Annotation(end_index=9620, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMWOEuFOON0NXgQ_FCK5pAep3cR_MnNZd8o6_nFbFmvjN0GbipUzANI_16MMY8H91YpTjGp5_QdywSkrekuqPSvaQaBNro5GE49_vGnKe2qm1UvsqQebLm_Vws1WgU619Eb7svSSmM', start_index=9606)
Annotation(end_index=9826, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL9noBOFPwx-VcH-x2SRzNhfbxKqSPfXV-smrx6r1U3TKnQm-JGCat0rSV0BbXni4O86erqI8r5RiCUR8EdGI5hkc8LQ3TtRCYih_kWHOcpiaDEI9FmwINXq-WcHWTxyCPkVh1cIcf', start_index=9812)
Annotation(end_index=9826, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHO1NnIuoUNnkeB7qlVnd6pAF2fVcbPEHyRq8S5v7brNmIyO5XrPGX0nnQQLjuRTcDbmigq1aR-QiZzV6ATh3YBLixMTVfEEpS3r9q3lZC9R_jl1_t_887woDqwDNvN', start_index=9812)
Annotation(end_index=10195, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN1anU774BC3HENVYNLw8TMP_Kllo07scEtKILgua2QxnUxQ7Jwvh8APf8ZzuNiFYp2jlCs3mcD_NPrFGlcgDyWxdn1LwfVLgjG4KVcvRZ_gNp9pAV1zVMVVpzVangPrUbePAs7GXP', start_index=10177)
Annotation(end_index=10195, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqOS133-GmOg2ax_Tic08x5RNAiYKl8chVxa3ULtJczN6x0oKIOHTFt5gvn3xOjFWHzI0Bv_Nyo1JYNABqwtINHF9jfZ-GqXyEKIXMsNlZiRifkmUMmpRjh8-DgfRvFT9jJgWejocD', start_index=10177)
Annotation(end_index=10195, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsd5YzKsJhU8HFCACmmQbJmJxec_xiEjUPWatiOjvNyqXD6QdDjHRR8Wp7snxNPy-GiKmDd3nxQ7EnSAhO0fE_s4EA2_OunnU48dAiCKLhP67uRZXtZv3_-_jgNeJKvxUkqadiOvRq', start_index=10177)
Annotation(end_index=10409, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHe3jWqaIH4etzHCUumhcP1imBtxzYZU1zyO1NybGMABPF6N_y-ehbE1mb0lXLfdMiZhe160mgQ9-5u1oJ97222knuY5Q-XjFvQ44dWhXdovDe9JZflzO1xn1VHKa419BKwdbAFomA58u0W7ybGqLyA8mubvuVganVSeSmYciaiYGx2E9skKm85Nox-flOfEIYbIiATFdz0lwnuyHP5rJ8A6_7FmCXBHFE9hzbu', start_index=10399)
Annotation(end_index=10713, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHGBSH2cl1-CIVsztUWFBGZ1I0Lhx0ditlxcSTMZz_6IPFMipA2uxVAIFXFqXsWje0emuAeE1mQDASBMoMylmjl38MDdUr9gSOifb46dNGox0Dmq641qdlG1atY0dp2PXFmQU8NUDWD4cZBg==', start_index=10695)
Annotation(end_index=10713, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHC3uJKIYsmSXEkjcxYfGxjAScXosnohSpNXYWtH1Yil_FMQS2Eyi-Tuz1JbnFc2Pr8VaMVhFnYf5Nym0Ayy3irDX00oH3GCODBuNtjbEMV0dVRZkLLU-69ZrOm0heQukQqY_NiW-MFQD7RIxQENg==', start_index=10695)
Annotation(end_index=10713, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHs8ZZwCx5MeWpcBN9Zyc7gGzIYz02lxMzLyLZg0qHKQ54TFXQDgpHMgv2YoungU71cIuG4bYSUyDpoQEQOaCnJqq_KVhM4lxeruKvVgUFE3Gh5KFhhZijpA6GQPt-iHHuuuYHMROD5vZIhT03rWAEFRw2zEwl2QnKLYCGNKdlyItMWovzAit7mqBfurShRCzdGaXShHbL6JNo-BJbGegXYp5bklrKENiQWYbBeoou7ncQI-3hAw9xQEFKKGfbpHAIMnZ7_VJ8BDATcKBoZKge8FQIdIPw=', start_index=10695)
Annotation(end_index=10960, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHGBSH2cl1-CIVsztUWFBGZ1I0Lhx0ditlxcSTMZz_6IPFMipA2uxVAIFXFqXsWje0emuAeE1mQDASBMoMylmjl38MDdUr9gSOifb46dNGox0Dmq641qdlG1atY0dp2PXFmQU8NUDWD4cZBg==', start_index=10946)
Annotation(end_index=10960, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHG4VRNCXqdFr48YWipo1QwQ5Bj7ZA7m7ZV-1mNW8Ig-fBH5c7DQ5aAxYObkIash8ASCtyb96O73AgTp15HyjOJRSfvUKuFOEtHGeI8VvKM7Xn7-I_diJPLOj9MHrO1aMyiFVR1HC-VcQ==', start_index=10946)
Annotation(end_index=11476, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2tXVRWAbm5H0KKguQ5VoPmJvtt3QKuJh7C79TIARYjuMQHQexUoDAA8GyuIbD04_NJXQ2pc7_KivVT_lWF4Ey3UnUJpyaerMLsnRpuSjyGEZYJ5ubhJSVPiFcpwf37xbFdxfMaAPf_7cW_pDvzL6yTsCmgagpLw==', start_index=11462)
Annotation(end_index=11476, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHe3jWqaIH4etzHCUumhcP1imBtxzYZU1zyO1NybGMABPF6N_y-ehbE1mb0lXLfdMiZhe160mgQ9-5u1oJ97222knuY5Q-XjFvQ44dWhXdovDe9JZflzO1xn1VHKa419BKwdbAFomA58u0W7ybGqLyA8mubvuVganVSeSmYciaiYGx2E9skKm85Nox-flOfEIYbIiATFdz0lwnuyHP5rJ8A6_7FmCXBHFE9hzbu', start_index=11462)
Annotation(end_index=11785, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN8xLTb6qJX1nVq1dhNFiz-NvSPQolNBWc4tONU9w72eBh_Uif6Q6dWLIVBodENBw5efK7aVzktRDSGZkodTRzpyCD0-4MJhev9ckoY_EW6EYJ24PNazjhm7DxsYRrb4eqv4QcVtB5zxWiHVeO1GTiiPeF_-7yrTcS05HQGqjc', start_index=11773)
Annotation(end_index=11785, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRlSgan1HljMfnhy-2cwGO7bTARW3fBsVTj81VONpaHkVt11zykgaLsqJ45pw6CAXjytXx2WlRL9_2ZMQjXJgZ8xFZBXbxV0tu9HMp0-i2WJMmOHN3UutSxLbQxbp4f_0d6YElt1rJ-w==', start_index=11773)
Annotation(end_index=12489, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPFD1k7w2mpJ61YZ8pXQ0JawbKTc9JoOl4Cb5dogGUT6hAe3v8e3iZjoR9sezEFzKUC4lyEjO-XGoXJ4IRZEu6-15--sFkaze0CFJluv2SsyUGFB4HfItI3RT2MhhJoQ==', start_index=12471)
Annotation(end_index=12489, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHi32WwsaUfNrDFS2UZsHIUtVzehiv3x3-0t819dYC2NtyW7axNH86Zgm-XZvi7_I7MeP26gVHiUe5jtFNWkjVtETf46L01AbUPtqD7JQMA5r9modpcgM1SUoo-Vnn7IRG_kZTUhfEgIZyEqqo35V7uXVBSG_NR63Hl569_PrCkYhSR8hD-74HR3O9wMstHOlulYvfSeJp-S3UMC017v7t3OOVpb-NVgjmYF3kiofA0IiSpUkXE8_8dyUDjcg==', start_index=12471)
Annotation(end_index=12489, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHs8ZZwCx5MeWpcBN9Zyc7gGzIYz02lxMzLyLZg0qHKQ54TFXQDgpHMgv2YoungU71cIuG4bYSUyDpoQEQOaCnJqq_KVhM4lxeruKvVgUFE3Gh5KFhhZijpA6GQPt-iHHuuuYHMROD5vZIhT03rWAEFRw2zEwl2QnKLYCGNKdlyItMWovzAit7mqBfurShRCzdGaXShHbL6JNo-BJbGegXYp5bklrKENiQWYbBeoou7ncQI-3hAw9xQEFKKGfbpHAIMnZ7_VJ8BDATcKBoZKge8FQIdIPw=', start_index=12471)
Annotation(end_index=12777, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJ69dPgePVR3V7ASebZRefBvJJdm6K3g3Dr_nnlxdtOjLJ1D_nav3cXEatyDxAXcnXfBa61sjRLx2nHDNkj-ujLefU1X2x8Pw-XnUXCu5BqLxsZzxEjpsanbfxhSZKD-Ft', start_index=12763)
Annotation(end_index=12777, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPFD1k7w2mpJ61YZ8pXQ0JawbKTc9JoOl4Cb5dogGUT6hAe3v8e3iZjoR9sezEFzKUC4lyEjO-XGoXJ4IRZEu6-15--sFkaze0CFJluv2SsyUGFB4HfItI3RT2MhhJoQ==', start_index=12763)
Annotation(end_index=13032, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE66BuCn3RD8pWd-yXBVp4jaZG_Kl3XiEqT_ITI1SafXw59QSTs0Koad47KMRrtQC3cJeTOGP2shqgWUx0AL9hBW3LYIk37P4EdJEox310WlHSkoRAQWztykvBPd3v2miEJdPkJMOaZL6ukaeCF2a8T0ktQkzptZVtaIQOpvdVIfbv3_DUFSiHhA74e3P-cUP_pPOaJWjMH5Rm4C_XuCBz9dsMp1kIxmbIUtBIMiOTzFZhauJTf0LlCuoa0mYHj4nGw_cInx6OiKQZcJKcCjqDzfHWkrwFLPgweirioxeUcibFjPloKw-YsDZHjqKC0bUslF2yL1Q==', start_index=13018)
Annotation(end_index=13032, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHi32WwsaUfNrDFS2UZsHIUtVzehiv3x3-0t819dYC2NtyW7axNH86Zgm-XZvi7_I7MeP26gVHiUe5jtFNWkjVtETf46L01AbUPtqD7JQMA5r9modpcgM1SUoo-Vnn7IRG_kZTUhfEgIZyEqqo35V7uXVBSG_NR63Hl569_PrCkYhSR8hD-74HR3O9wMstHOlulYvfSeJp-S3UMC017v7t3OOVpb-NVgjmYF3kiofA0IiSpUkXE8_8dyUDjcg==', start_index=13018)
Annotation(end_index=13733, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFihxyqkii5XorqY_KHmKDmTp3_uM1qOPpsrZW3gCIkoAMG5KKTDKwgcYJ8a6SPlFkY2kbaDoDS9cdggfL9sVOtqL826YQbNbGacQV0X7SyXQ1Efv_XEBiEG1LjPdZS8W5kLKHbu_h', start_index=13720)
Annotation(end_index=13733, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqMsmZmzUhqJRpq_R7i48zJpPuqhO8Qkyt1H6rBDpq5pDmthThglUsNz5Kp7Ljp2kVs_SOoaa7QMV6yAt-h7r0VXd9rhJ9e01swV8Fs2ZEAxPpbvUXrmInBu7KSLvdmi90CBcbpO6G', start_index=13720)
Annotation(end_index=14067, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDZ_OznrJ7OCrGdpbvINLJmdn60pfgWfKEF1zA5AWpxNMkiGzZgp5KAbWhu1NSHRp445Yw676qjTt4J0w6ABymXMgRzjYRoizxOMBe9MaFLgOsXObl3sFGSOZUqwswNAB3N9DkNke24fG0vK2c5LWcNl8ndMf6DGFeGthEaJq1jX2TCgu9CIFM9yHf7ccIjlBmcyAJAsjJ06QbI0LHuheGqTqpPnhZ', start_index=14054)
Annotation(end_index=14067, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqMsmZmzUhqJRpq_R7i48zJpPuqhO8Qkyt1H6rBDpq5pDmthThglUsNz5Kp7Ljp2kVs_SOoaa7QMV6yAt-h7r0VXd9rhJ9e01swV8Fs2ZEAxPpbvUXrmInBu7KSLvdmi90CBcbpO6G', start_index=14054)
Annotation(end_index=14483, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFihxyqkii5XorqY_KHmKDmTp3_uM1qOPpsrZW3gCIkoAMG5KKTDKwgcYJ8a6SPlFkY2kbaDoDS9cdggfL9sVOtqL826YQbNbGacQV0X7SyXQ1Efv_XEBiEG1LjPdZS8W5kLKHbu_h', start_index=14469)
Annotation(end_index=14483, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_fDCtxTv77IL2-Vozbl5novTHZgz2DcZQPjIzjpTyZJbIp95iLniOW_-HwmGLidXcgXv1LtxEQcvVygWSuyUblQHfMaSl-ErMxC5F2pA6tExocwCe95UwOLhtEA5r9ei3WyytmcVI', start_index=14469)
Annotation(end_index=14803, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbsUZGun5G_liO7gN6RqlmzmPDTQdLxY4Lo8A09h1VAC_Xn9bE7NDheKNTcl3Vt8omzYXKP0VDYOPUVwLxkv9D3I7wZogEuycfOq1gAPWj5Y_2i3kde4e0A1qEiOn0NI4OBnOg2ikAQIrTLI3UNKzWPFJhbRDiVzGijhhAijRvMsE-9pmXAZeqUui-2AtRD6nqfVx9Foy4ky08ylk6-oM54KmjdR2vkZV6mCg_Ecw4i2TS', start_index=14789)
Annotation(end_index=14803, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgovwpf_DVbnAeFKbHptkKGDl90Cc00b0iy1jlq-wYssCeLqZsMlxtw3EDvx3YKZLyVh5OxINDNtxt1SugOvzrBv1wBA29N6GixzE8VBPxx6xyCp1zJMuPJG2FWLAufNGyioCux4qrGEw2o4ie_pTzTUbCzwzWvxFL_OhSg5IPZsuWQY1Y2VI4gZoRcjz1b4ArGmwvx-_2vuwY7Cx_ZIi1RLDoGZ-TXxVuZovSR4bwwsk-c-fKc0uI5aA=', start_index=14789)
Annotation(end_index=15709, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdldrG1XHel_hAQNZdA0usMgHi82eGvCKFqrc2Hw0pHFjOgFwiZJitcurq2PkDXpYpxQ5lkrU1ERi7ob6IuCSMKnqu30k-TjlGSsZZW7TxE9CaTY56CeBJQeCaAlyAjtUtboSD6wX9PHBHDE8_mUTDI3mcIg==', start_index=15692)
Annotation(end_index=15709, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRlSgan1HljMfnhy-2cwGO7bTARW3fBsVTj81VONpaHkVt11zykgaLsqJ45pw6CAXjytXx2WlRL9_2ZMQjXJgZ8xFZBXbxV0tu9HMp0-i2WJMmOHN3UutSxLbQxbp4f_0d6YElt1rJ-w==', start_index=15692)
Annotation(end_index=15709, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbzLmcwekWH4sVMzW88ncXyhkZCl0oAvHCL5dAEK1I6sVS53RCZvzcTtV_HEXnk7R1omxilEQWiFO6rhgXQFzb-fC38XHcvsOqlwY2mvkkQ9ehOtjlnS7NZIopY_sDfOMOOgWDGEhTXus=', start_index=15692)
Annotation(end_index=16166, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNeXP98Y1_qpgHzwwb9mJYAJ80ZGHI_K9nFTKHgUoivuf94AEAfI9lOjznb0AGVhPLvrwpeT2kF7gP9KHZY9uwtYh7uSntRO_N_yLJkmokGPnkiO2OdJEdndXS4WhBfAPEpBlknMdZ', start_index=16156)
Annotation(end_index=16327, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUkkUtoN00FJqzF8J1tMVrjI4blvN2cv8ghcDgUJUcQQPaaiLRFLVpz6gHYpOtIeIVrY3F0qnVkLqR0stKIaafwLxu4C3QNUWmcP3tzre7odIbyDFmLYkrhJ8Vg9T4', start_index=16313)
Annotation(end_index=16327, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEla9nyf59lfjNTwYsr9shoArEPkEHQ1cBylmfO8bZFiBR5WIFj-2Xr1Sf2wQJ1qmNXcCLXykVKASjYTuOxxLEIqa7oCjfWTTZfTEAFZ6h2DsuyKkZtJ3kN71cg1OG9DaRUEqPjVhMHj7ihnupgbzPLRHBOfbqrM7a7yRBa1LKGin9P-wGpKYk0o5oNp8tFoBaAjz7J_AmMN3lxbrqSIYbPkx0hF3X3SBMlFbKWA22JVUiF', start_index=16313)
Annotation(end_index=16595, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4IBkdTDZZATAYLxutwxlnMZQiWoTJMRTzaF6Avp_SrQw76Tx39eD_24OiOeiPgLGj0OkJkQbWjXKaRz5RFSVFM_8bsmKZ5TfOKJkWhkk1ofhF-6JzqxsV7YDUOa7wLRMn9yJUgSbC', start_index=16578)
Annotation(end_index=16595, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqV8DtIj4-MnrsmndhRavm8uPkJEuUe8QUaN-c9eE0rvpYZHvRPKGU4GxyyCZz7RYqccVpH5DzxmtJqGteNXt4wlQzNKBX6e6o1rgN37zIhuVq6pVFhAJ5hwBflYICvy71GM9n72JOh1KQ5IjvYGlf86y3Zj1A0Ey1AFOg8cAJI7Bfg-AIEfCU_Quf5zV2ww==', start_index=16578)
Annotation(end_index=16595, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGh_gHcbf4J7HWcI1weD_ietlz7aA_363NMKSyR4E3piPl7IrEoJtbmrCUcGbE3H4b6-dymDVPLaq-RmUzGWbGQW9GpqyBKC1TwOAbi7rKQ6eu0c-B4_4mVn5CJfG7On2nb8SKmVg==', start_index=16578)
Annotation(end_index=16855, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEla9nyf59lfjNTwYsr9shoArEPkEHQ1cBylmfO8bZFiBR5WIFj-2Xr1Sf2wQJ1qmNXcCLXykVKASjYTuOxxLEIqa7oCjfWTTZfTEAFZ6h2DsuyKkZtJ3kN71cg1OG9DaRUEqPjVhMHj7ihnupgbzPLRHBOfbqrM7a7yRBa1LKGin9P-wGpKYk0o5oNp8tFoBaAjz7J_AmMN3lxbrqSIYbPkx0hF3X3SBMlFbKWA22JVUiF', start_index=16845)
Annotation(end_index=17397, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN8xLTb6qJX1nVq1dhNFiz-NvSPQolNBWc4tONU9w72eBh_Uif6Q6dWLIVBodENBw5efK7aVzktRDSGZkodTRzpyCD0-4MJhev9ckoY_EW6EYJ24PNazjhm7DxsYRrb4eqv4QcVtB5zxWiHVeO1GTiiPeF_-7yrTcS05HQGqjc', start_index=17385)
Annotation(end_index=17397, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRlSgan1HljMfnhy-2cwGO7bTARW3fBsVTj81VONpaHkVt11zykgaLsqJ45pw6CAXjytXx2WlRL9_2ZMQjXJgZ8xFZBXbxV0tu9HMp0-i2WJMmOHN3UutSxLbQxbp4f_0d6YElt1rJ-w==', start_index=17385)
Annotation(end_index=17505, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqiLUCHSXYuOxmkTE7UytkCKrm5NPvFw4Ra-RK1AFYdodYpOwq2KTb8gpm1wW3T7caV1ul0dZLPPpj-wI_Vlu0OxJnPhv5qpvC_zVSVhM-6NKbI5eDwia-8e9DDFcsnusewEoyUUIV0XBAU_5tVB7ryXCnh2_yaxroS_xebRsbtPLz3teVEFO0E9vOdC5MUjoAqs1SHaLC2kp94OBUAcBgdKbQtKoou8d5KqwLtLj3Usp0FZyXVXYChOfYci1AyfJa0Tdk1Zajjh_mrakXQm69fi2cLYOMPOEyDsvLqEHyIfxQV7BmuA==', start_index=17496)
Annotation(end_index=17749, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNowlCpnkWRaaBgXjLUmlCjeaG-OYEVI8A_c1KtCTw1YF-8-jk93gBum0esCOFL6_xPnyYaHX105eS_djTOLWw0_AL5LY807Tc4ek3HTlfEBdgxCv0tdw0FaI7vBsyfzK6I98yhI1Nz_mlWmIfq3Vk6vD9coTA9Q==', start_index=17735)
Annotation(end_index=17749, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbzLmcwekWH4sVMzW88ncXyhkZCl0oAvHCL5dAEK1I6sVS53RCZvzcTtV_HEXnk7R1omxilEQWiFO6rhgXQFzb-fC38XHcvsOqlwY2mvkkQ9ehOtjlnS7NZIopY_sDfOMOOgWDGEhTXus=', start_index=17735)
Annotation(end_index=17986, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHGBSH2cl1-CIVsztUWFBGZ1I0Lhx0ditlxcSTMZz_6IPFMipA2uxVAIFXFqXsWje0emuAeE1mQDASBMoMylmjl38MDdUr9gSOifb46dNGox0Dmq641qdlG1atY0dp2PXFmQU8NUDWD4cZBg==', start_index=17972)
Annotation(end_index=17986, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOlG4_PVFs4VoTXXkFVfr-9i30fjEzpZGU2u7kAvO1amXsXnYv1cOhkK9s4vWNvP9Sx8GSXlc89r_3n10JaCdvvYo50YMsMAyQSszmjz1ETm1PwLCWMIRXLA0zA_Y3giUdjUA8qOWT', start_index=17972)
Annotation(end_index=18278, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmuxbH1NYqbRGm3rU9WD6WfIg2lT7QdC_F3FlZ7l9VMIeUYlEyxzK8B1Nnb26k3J4ta7PDhxf3Q8pzCDaCuN2DMozDg1ikM8gkj5zI6Bnhaix8Ph2hxMp8Kpk0yjjQNYHjGb_m1UWGqXTcdT6sf66BjhAyFdgqi1gUo0Wa3XTL', start_index=18269)
Annotation(end_index=18621, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF1MWjWw97Gh8ZGI9hhZ65moJx2_WHuB4vlt2b2SCiYUwG_z2E4-sEGAsOVLlTTFM1XImNmAIu9aB_lpuoDhdsAIGYBvZ0vLZAY65wW7A3bTUUpa3WgXzDBYMgle5dyvPpRY2OW3L-M', start_index=18603)
Annotation(end_index=18621, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHG4VRNCXqdFr48YWipo1QwQ5Bj7ZA7m7ZV-1mNW8Ig-fBH5c7DQ5aAxYObkIash8ASCtyb96O73AgTp15HyjOJRSfvUKuFOEtHGeI8VvKM7Xn7-I_diJPLOj9MHrO1aMyiFVR1HC-VcQ==', start_index=18603)
Annotation(end_index=18621, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsd5YzKsJhU8HFCACmmQbJmJxec_xiEjUPWatiOjvNyqXD6QdDjHRR8Wp7snxNPy-GiKmDd3nxQ7EnSAhO0fE_s4EA2_OunnU48dAiCKLhP67uRZXtZv3_-_jgNeJKvxUkqadiOvRq', start_index=18603)
Annotation(end_index=18773, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAzmqxUbctmfq2kq976_A4j6TWD8BCDzCR8O1dPXrhKyq5k-dAEUw8c1Mz4V9L0dmmMYpvLpxJD3r6hB5XVbC4oIy0MokUryIivrbZy4dbpSXlnMtbhRJhNbNUW_Cv78dYO_Pk6Urt', start_index=18759)
Annotation(end_index=18773, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHG4VRNCXqdFr48YWipo1QwQ5Bj7ZA7m7ZV-1mNW8Ig-fBH5c7DQ5aAxYObkIash8ASCtyb96O73AgTp15HyjOJRSfvUKuFOEtHGeI8VvKM7Xn7-I_diJPLOj9MHrO1aMyiFVR1HC-VcQ==', start_index=18759)
Annotation(end_index=19872, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDZ_OznrJ7OCrGdpbvINLJmdn60pfgWfKEF1zA5AWpxNMkiGzZgp5KAbWhu1NSHRp445Yw676qjTt4J0w6ABymXMgRzjYRoizxOMBe9MaFLgOsXObl3sFGSOZUqwswNAB3N9DkNke24fG0vK2c5LWcNl8ndMf6DGFeGthEaJq1jX2TCgu9CIFM9yHf7ccIjlBmcyAJAsjJ06QbI0LHuheGqTqpPnhZ', start_index=19862)
Annotation(end_index=19998, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZs-vFphzc18v9fcE94kKUwQG4a3bmuWYji9W0i1VG4BCVG7mc_l--4qaHRqe1Q-nTebFoq19gDLN7cxei1Jj0K2fgmHkhELfQzPCPcQc24TSRjt9RK87pe_7LNBDiK9ofOOUV0RdPVR-n4DLriziLudXEds_2XO9WOZ7ogJs0_SRVU3DjGj_34hDcVC7V6NJUhkmHK6HnMQQw8X55s9Gq8otlZ48yu0xlKb8hDDmvdw7HHrnPHFzdaPvP0uNShSGWA0SwLJsYTMcYrTT02xr1H5aizAWi', start_index=19988)
Annotation(end_index=20119, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_fDCtxTv77IL2-Vozbl5novTHZgz2DcZQPjIzjpTyZJbIp95iLniOW_-HwmGLidXcgXv1LtxEQcvVygWSuyUblQHfMaSl-ErMxC5F2pA6tExocwCe95UwOLhtEA5r9ei3WyytmcVI', start_index=20109)
Annotation(end_index=20210, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmuxbH1NYqbRGm3rU9WD6WfIg2lT7QdC_F3FlZ7l9VMIeUYlEyxzK8B1Nnb26k3J4ta7PDhxf3Q8pzCDaCuN2DMozDg1ikM8gkj5zI6Bnhaix8Ph2hxMp8Kpk0yjjQNYHjGb_m1UWGqXTcdT6sf66BjhAyFdgqi1gUo0Wa3XTL', start_index=20201)
Annotation(end_index=20318, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZGopu1ibDVDgXTkh5OknBTQ-GggMsCianaeWMU90G3YE3sq7ypl6jWAJ3lCtu5C1OOLZkHtdjGhuDqM91ccIL-uf7qPk1lWKhmKlcQVnq0fXA4AS-ouZERbuN7yC_6mN7O-8_uTWwN9C3766wiirFGW4A5u6GbCX4_zXefRe7Ljs2pMD9_JIhgn_eBT09z8EeYUnv_uP26VRYfgyDcOFwqBz3pUeKheSZZ5mr36Vgbl5lg75enQRyCATplnDKVNtO42Gf', start_index=20309)
Annotation(end_index=20427, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNeXP98Y1_qpgHzwwb9mJYAJ80ZGHI_K9nFTKHgUoivuf94AEAfI9lOjznb0AGVhPLvrwpeT2kF7gP9KHZY9uwtYh7uSntRO_N_yLJkmokGPnkiO2OdJEdndXS4WhBfAPEpBlknMdZ', start_index=20417)
Annotation(end_index=20521, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4IBkdTDZZATAYLxutwxlnMZQiWoTJMRTzaF6Avp_SrQw76Tx39eD_24OiOeiPgLGj0OkJkQbWjXKaRz5RFSVFM_8bsmKZ5TfOKJkWhkk1ofhF-6JzqxsV7YDUOa7wLRMn9yJUgSbC', start_index=20511)
Annotation(end_index=20577, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqMsmZmzUhqJRpq_R7i48zJpPuqhO8Qkyt1H6rBDpq5pDmthThglUsNz5Kp7Ljp2kVs_SOoaa7QMV6yAt-h7r0VXd9rhJ9e01swV8Fs2ZEAxPpbvUXrmInBu7KSLvdmi90CBcbpO6G', start_index=20568)
Annotation(end_index=20671, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEla9nyf59lfjNTwYsr9shoArEPkEHQ1cBylmfO8bZFiBR5WIFj-2Xr1Sf2wQJ1qmNXcCLXykVKASjYTuOxxLEIqa7oCjfWTTZfTEAFZ6h2DsuyKkZtJ3kN71cg1OG9DaRUEqPjVhMHj7ihnupgbzPLRHBOfbqrM7a7yRBa1LKGin9P-wGpKYk0o5oNp8tFoBaAjz7J_AmMN3lxbrqSIYbPkx0hF3X3SBMlFbKWA22JVUiF', start_index=20661)
Annotation(end_index=20757, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHO1NnIuoUNnkeB7qlVnd6pAF2fVcbPEHyRq8S5v7brNmIyO5XrPGX0nnQQLjuRTcDbmigq1aR-QiZzV6ATh3YBLixMTVfEEpS3r9q3lZC9R_jl1_t_887woDqwDNvN', start_index=20747)
Annotation(end_index=20851, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF1MWjWw97Gh8ZGI9hhZ65moJx2_WHuB4vlt2b2SCiYUwG_z2E4-sEGAsOVLlTTFM1XImNmAIu9aB_lpuoDhdsAIGYBvZ0vLZAY65wW7A3bTUUpa3WgXzDBYMgle5dyvPpRY2OW3L-M', start_index=20841)
Annotation(end_index=20938, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQER8sqRmmKrJvJsgGuSgxKMOHsgIKgzeO6mvF75IP-y3vUrmVDoxkwqxxkLlwzTW2OOPboxHWz7dT-4-7mmUhGS2tIbzfgS-nIhle6TKIT0NVep4sKwYOYyB-n1a-02Vbc=', start_index=20928)
Annotation(end_index=21025, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNu_87I5IT1C-wgF5VLW_K-k1DaHUmu3nzhUap0WvUH8Xijpr-fklUJxKmgK9dxkHUzdFYTgGW909WPedOoabG-aij317bZbGqDUOGINP607oClacWW8OMIYNXMJpE-C1km73SMDU=', start_index=21015)
Annotation(end_index=21157, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE99QBHaGPmHqZF1dAnUPRdGgb7Fv2f6_bcOkQOtbJ8hQgiPZf6q-p3s8jnj2j7fVBk-YZS07wzOernwp71zFRV9y4MzGdbxbGqy2iVKAHo1CEn4zkihbsc45TgAcAtgZEfE5Kzm-2tHA==', start_index=21147)
Annotation(end_index=21245, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUph1xcrhcofbfbUV9HgbGFzyUbbINlU9awOLuAaj93tS5G31g7gwb3gczhSa68vueAdsr8CY0iTptcdVZhSmNJBv23OyyB-yISZJAPOnnGJD2Yy-drFUw37lQjmreew==', start_index=21235)
Annotation(end_index=21333, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOlG4_PVFs4VoTXXkFVfr-9i30fjEzpZGU2u7kAvO1amXsXnYv1cOhkK9s4vWNvP9Sx8GSXlc89r_3n10JaCdvvYo50YMsMAyQSszmjz1ETm1PwLCWMIRXLA0zA_Y3giUdjUA8qOWT', start_index=21323)
Annotation(end_index=21421, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPFD1k7w2mpJ61YZ8pXQ0JawbKTc9JoOl4Cb5dogGUT6hAe3v8e3iZjoR9sezEFzKUC4lyEjO-XGoXJ4IRZEu6-15--sFkaze0CFJluv2SsyUGFB4HfItI3RT2MhhJoQ==', start_index=21411)
Annotation(end_index=21511, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJ69dPgePVR3V7ASebZRefBvJJdm6K3g3Dr_nnlxdtOjLJ1D_nav3cXEatyDxAXcnXfBa61sjRLx2nHDNkj-ujLefU1X2x8Pw-XnUXCu5BqLxsZzxEjpsanbfxhSZKD-Ft', start_index=21501)
Annotation(end_index=21601, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdldrG1XHel_hAQNZdA0usMgHi82eGvCKFqrc2Hw0pHFjOgFwiZJitcurq2PkDXpYpxQ5lkrU1ERi7ob6IuCSMKnqu30k-TjlGSsZZW7TxE9CaTY56CeBJQeCaAlyAjtUtboSD6wX9PHBHDE8_mUTDI3mcIg==', start_index=21591)
Annotation(end_index=21690, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN8xLTb6qJX1nVq1dhNFiz-NvSPQolNBWc4tONU9w72eBh_Uif6Q6dWLIVBodENBw5efK7aVzktRDSGZkodTRzpyCD0-4MJhev9ckoY_EW6EYJ24PNazjhm7DxsYRrb4eqv4QcVtB5zxWiHVeO1GTiiPeF_-7yrTcS05HQGqjc', start_index=21681)
Annotation(end_index=21784, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqiLUCHSXYuOxmkTE7UytkCKrm5NPvFw4Ra-RK1AFYdodYpOwq2KTb8gpm1wW3T7caV1ul0dZLPPpj-wI_Vlu0OxJnPhv5qpvC_zVSVhM-6NKbI5eDwia-8e9DDFcsnusewEoyUUIV0XBAU_5tVB7ryXCnh2_yaxroS_xebRsbtPLz3teVEFO0E9vOdC5MUjoAqs1SHaLC2kp94OBUAcBgdKbQtKoou8d5KqwLtLj3Usp0FZyXVXYChOfYci1AyfJa0Tdk1Zajjh_mrakXQm69fi2cLYOMPOEyDsvLqEHyIfxQV7BmuA==', start_index=21775)
Annotation(end_index=21861, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVkDWZL2ye83tGCbO3kDYW2v5upbEQXtic9rNXLFFDdR5IIJM25QaT71TUptKfhoq82OZc1ZQjwn2jpvfX9Xw3RSryQ-f72B5Fe3R0YXVFDd4sTsNAs7cV2BmyxVVGLiT9aEDAsRxD', start_index=21851)
Annotation(end_index=21956, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiicWcNzZ6hWkNMY9QlZrG4ein9KIJsK6kpuM3rzjQJcIAFlWQW5fiSoFmOfiwuz2O4TjZL-Xx9nKQuQJExJHwIZdtc2pQBSqHDYVNRMRTE5oIXu0-HsMcHvWaIsubinTpCQI9zSs6', start_index=21946)
Annotation(end_index=22037, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnKy6juC4U0_PuiN1NbRCB3dZPkyl5mBgvkbq9tDXu33VJONkmNskyXGE1JYHqV-L-X3pceQWVvYWVNQF9MHM6OVbUrtG6qRgbYjE64Lzj8qjjU-CwGl-LK-rdHudntg==', start_index=22027)
Annotation(end_index=22124, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNeXP98Y1_qpgHzwwb9mJYAJ80ZGHI_K9nFTKHgUoivuf94AEAfI9lOjznb0AGVhPLvrwpeT2kF7gP9KHZY9uwtYh7uSntRO_N_yLJkmokGPnkiO2OdJEdndXS4WhBfAPEpBlknMdZ', start_index=22114)
Annotation(end_index=22211, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUkkUtoN00FJqzF8J1tMVrjI4blvN2cv8ghcDgUJUcQQPaaiLRFLVpz6gHYpOtIeIVrY3F0qnVkLqR0stKIaafwLxu4C3QNUWmcP3tzre7odIbyDFmLYkrhJ8Vg9T4', start_index=22201)
Annotation(end_index=22298, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_AymdTNq9I4bk0GcvEIBo5ruoaNhyyRFCzGYTuCog8xbAdDZ6JB-S0kXqz6xUu5W4NQ2Y8BGfo9mbZoqtkwNIlIWK7w_KViO9BWXt7gsBqct248olYDof_QNbVnEiEA==', start_index=22288)
Annotation(end_index=22369, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHg9Q9sgokxUIpLUH7lGfCjX0As2COY2TZJ1K5qLVWyLPdSNR6Fa_0caN4DTXa4sNMsRJ9EeeLIxnTY-T2hfX2I_LiKkX8A7kpBMmLebm8rNlNm-HZyMseZ9X-QMj3YqSNTW9mgeZEU', start_index=22359)
Annotation(end_index=22440, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHG4VRNCXqdFr48YWipo1QwQ5Bj7ZA7m7ZV-1mNW8Ig-fBH5c7DQ5aAxYObkIash8ASCtyb96O73AgTp15HyjOJRSfvUKuFOEtHGeI8VvKM7Xn7-I_diJPLOj9MHrO1aMyiFVR1HC-VcQ==', start_index=22430)
Annotation(end_index=22511, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHGBSH2cl1-CIVsztUWFBGZ1I0Lhx0ditlxcSTMZz_6IPFMipA2uxVAIFXFqXsWje0emuAeE1mQDASBMoMylmjl38MDdUr9gSOifb46dNGox0Dmq641qdlG1atY0dp2PXFmQU8NUDWD4cZBg==', start_index=22501)
Annotation(end_index=22582, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEun-6IHSkgtUJs5O5Y4NLj50xm_Yij2nFEW9W9mOhwWnnXugN9zAqV7QEvZ3B2WiwpfLGGQqDS1zLAAVVuo2HPrQNGvnwD2YoX7RyF3Gj91FaGeDAjqEj7_-lOl_2omIXskp2Yil-Y', start_index=22572)
Annotation(end_index=22647, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLway3ItQ0RJNZLD3_yuCgEz-3XWNRVLItzMORswXRg9OuF0H422iraFM5wb13a4Dj0cl5T9qvxsCw4p43BwRFIlMtoNrtIb4SWtciVynKHcen-X0AER-QwEm-nRC5j0djs93pjgg=', start_index=22637)
Annotation(end_index=22712, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHe3jWqaIH4etzHCUumhcP1imBtxzYZU1zyO1NybGMABPF6N_y-ehbE1mb0lXLfdMiZhe160mgQ9-5u1oJ97222knuY5Q-XjFvQ44dWhXdovDe9JZflzO1xn1VHKa419BKwdbAFomA58u0W7ybGqLyA8mubvuVganVSeSmYciaiYGx2E9skKm85Nox-flOfEIYbIiATFdz0lwnuyHP5rJ8A6_7FmCXBHFE9hzbu', start_index=22702)
Annotation(end_index=22790, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2tXVRWAbm5H0KKguQ5VoPmJvtt3QKuJh7C79TIARYjuMQHQexUoDAA8GyuIbD04_NJXQ2pc7_KivVT_lWF4Ey3UnUJpyaerMLsnRpuSjyGEZYJ5ubhJSVPiFcpwf37xbFdxfMaAPf_7cW_pDvzL6yTsCmgagpLw==', start_index=22780)
Annotation(end_index=22868, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMWOEuFOON0NXgQ_FCK5pAep3cR_MnNZd8o6_nFbFmvjN0GbipUzANI_16MMY8H91YpTjGp5_QdywSkrekuqPSvaQaBNro5GE49_vGnKe2qm1UvsqQebLm_Vws1WgU619Eb7svSSmM', start_index=22858)
Annotation(end_index=22946, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN1anU774BC3HENVYNLw8TMP_Kllo07scEtKILgua2QxnUxQ7Jwvh8APf8ZzuNiFYp2jlCs3mcD_NPrFGlcgDyWxdn1LwfVLgjG4KVcvRZ_gNp9pAV1zVMVVpzVangPrUbePAs7GXP', start_index=22936)
Annotation(end_index=23014, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsd5YzKsJhU8HFCACmmQbJmJxec_xiEjUPWatiOjvNyqXD6QdDjHRR8Wp7snxNPy-GiKmDd3nxQ7EnSAhO0fE_s4EA2_OunnU48dAiCKLhP67uRZXtZv3_-_jgNeJKvxUkqadiOvRq', start_index=23004)
Annotation(end_index=23082, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHs8ZZwCx5MeWpcBN9Zyc7gGzIYz02lxMzLyLZg0qHKQ54TFXQDgpHMgv2YoungU71cIuG4bYSUyDpoQEQOaCnJqq_KVhM4lxeruKvVgUFE3Gh5KFhhZijpA6GQPt-iHHuuuYHMROD5vZIhT03rWAEFRw2zEwl2QnKLYCGNKdlyItMWovzAit7mqBfurShRCzdGaXShHbL6JNo-BJbGegXYp5bklrKENiQWYbBeoou7ncQI-3hAw9xQEFKKGfbpHAIMnZ7_VJ8BDATcKBoZKge8FQIdIPw=', start_index=23072)
Annotation(end_index=23167, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHi32WwsaUfNrDFS2UZsHIUtVzehiv3x3-0t819dYC2NtyW7axNH86Zgm-XZvi7_I7MeP26gVHiUe5jtFNWkjVtETf46L01AbUPtqD7JQMA5r9modpcgM1SUoo-Vnn7IRG_kZTUhfEgIZyEqqo35V7uXVBSG_NR63Hl569_PrCkYhSR8hD-74HR3O9wMstHOlulYvfSeJp-S3UMC017v7t3OOVpb-NVgjmYF3kiofA0IiSpUkXE8_8dyUDjcg==', start_index=23157)
Annotation(end_index=23252, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHC3uJKIYsmSXEkjcxYfGxjAScXosnohSpNXYWtH1Yil_FMQS2Eyi-Tuz1JbnFc2Pr8VaMVhFnYf5Nym0Ayy3irDX00oH3GCODBuNtjbEMV0dVRZkLLU-69ZrOm0heQukQqY_NiW-MFQD7RIxQENg==', start_index=23242)
Annotation(end_index=23337, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5IxO3ZGIUxIpn5Pg9WrMnWtjK0TxFwZoC8opn8DyHEWk9tqzcVPQleyqbCIu6hK__GHtahxEsvz8Pur6Yq_oJHaJpKtp5yoRa1p1opwpqIj-0h9t5tXwd3ww09fimNBGoQRkTh12O', start_index=23327)
Annotation(end_index=23433, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDcTCzZJSHMZp4epV5HXFBF70JCHbjAJgW4NPb7D2ju82KlYJsf-c_nrSidr5n7zRAJ1w2_R1sVJShJ1g2UJ5QyOIEItDjLbxLKg6pRCiW_-xtBnrYESeJH3TYiqLNokZprnmyk39d', start_index=23424)
Annotation(end_index=23528, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGh_gHcbf4J7HWcI1weD_ietlz7aA_363NMKSyR4E3piPl7IrEoJtbmrCUcGbE3H4b6-dymDVPLaq-RmUzGWbGQW9GpqyBKC1TwOAbi7rKQ6eu0c-B4_4mVn5CJfG7On2nb8SKmVg==', start_index=23519)
Annotation(end_index=23609, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqV8DtIj4-MnrsmndhRavm8uPkJEuUe8QUaN-c9eE0rvpYZHvRPKGU4GxyyCZz7RYqccVpH5DzxmtJqGteNXt4wlQzNKBX6e6o1rgN37zIhuVq6pVFhAJ5hwBflYICvy71GM9n72JOh1KQ5IjvYGlf86y3Zj1A0Ey1AFOg8cAJI7Bfg-AIEfCU_Quf5zV2ww==', start_index=23599)
Annotation(end_index=23689, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNG3cGE05CAjjCYZwMSwukbAgiCfwPrinhfMLRH1DepuAoAvtwXi3DzgfMdzUdVW_Muu-kDMXaUp-_25lM0Q8O23hQVeHYlFoCWPDE_HNSXWaaNZSkdw2Vhe1_FXn7_t_56dZUCiLZ_eC_PGK54_AwtUG9mj958FyGB9OpyREfPRA7a9k6m6BqWdGpJ3A5_wrdKuAzEPw2nMoi_wKQJXssOJtFQF0mVpuuWL-7TQhuJMJXJgcPD_otpR1KRad80hciIh14_NHutmwIID8k', start_index=23680)
Annotation(end_index=23801, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgUq6-FwKfbFcQU9In0-W3aNeDYyoLxqhrnXomuw2UGzDCTcznVI4LWj9wfxL0Hp7IH1ZTIPgAu0EjvDtZfFUNSpIfViZUxXJkzy7rJoiPRyfyRBBq_w3ZMNq1JuOwhDA=', start_index=23791)
Annotation(end_index=23882, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHH1svq4yC70ZkZXgZjGorfn0bDXaXF5XGhPBjaHgzs1zRdWhGjOe-8ki62TNgha_u8wAIAaniS5_X5xSadCdDIE4mRUHDIA35yPmS5kqotNTxmdAgbexA0BEkYL7b18u9R2wpktM8GkdJRV6pv_TrP6CUhDWmzXsVyBvdl6gAtD9PE5VkQAI0dE7DkB1qpUxs_KdlomArqhLREYqaO-oAKx32hTDbo1WnpbHf1AYCs8phZF-XJsiBXQgBvGsVM1SM=', start_index=23872)
Annotation(end_index=23967, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmuxbH1NYqbRGm3rU9WD6WfIg2lT7QdC_F3FlZ7l9VMIeUYlEyxzK8B1Nnb26k3J4ta7PDhxf3Q8pzCDaCuN2DMozDg1ikM8gkj5zI6Bnhaix8Ph2hxMp8Kpk0yjjQNYHjGb_m1UWGqXTcdT6sf66BjhAyFdgqi1gUo0Wa3XTL', start_index=23958)
Annotation(end_index=24053, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHG4VRNCXqdFr48YWipo1QwQ5Bj7ZA7m7ZV-1mNW8Ig-fBH5c7DQ5aAxYObkIash8ASCtyb96O73AgTp15HyjOJRSfvUKuFOEtHGeI8VvKM7Xn7-I_diJPLOj9MHrO1aMyiFVR1HC-VcQ==', start_index=24043)
Annotation(end_index=24123, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGN5wrQXb5KYmC87_AMqIUSU_LY8ilrB3b9kXg35pbAlPUTMcrcwAsVSu3zOKcDnOeNNLclZPWj4OLXwNQxk8jxwX4kfUUPQ0nk6xlpGrKDNsTJptIvyFx4I42ZsPP5sg==', start_index=24113)
Annotation(end_index=24205, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpy1vagRcVRix0ISqIz14zm1kpKjXBMo-Gj8TqCVA3he06PmPbzkED4tpPH3LqhoJZzeGx8E3SEjJ9vBuwLOSizGMGt1cjWCJ_vv08X4Tf-Hk-obbKhK-ncHESbxGzfxdT35UvCqqcZaumB5v3Tbjijv17T105xvBuXddI8D1NN2rMNxmqIl8lzkAidnAo7llilqNKMorOA519Y-TIH-sJ5SKGNjCYV9FNBYSDE15JWrXI8uhC4EowhhlqlncofBEhWQ==', start_index=24195)
Annotation(end_index=24287, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYblcbfW_lP9iYdqKLiIIGtsWx7WFWAXif7o97_74B5UtwRHyBHgPwo-s3n0DEO8z7X672VRb83vXXnh4lhV_XBcQXXHBuxzyutE4EbpcEYU164-YFHiApIikKwqDiGFH0CPyAadjElJ_4IkWDV8pWyCdlc6HKETPIyLKSsdIPYYgfAK97iu_PImbQcTRTm0O_0Zz-OA2DbGZW6Wx1v8xetfcvPHI0HVLjVy6zv_wkeXK2kkT3e6NcU5blVng=', start_index=24277)
Annotation(end_index=24369, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqOS133-GmOg2ax_Tic08x5RNAiYKl8chVxa3ULtJczN6x0oKIOHTFt5gvn3xOjFWHzI0Bv_Nyo1JYNABqwtINHF9jfZ-GqXyEKIXMsNlZiRifkmUMmpRjh8-DgfRvFT9jJgWejocD', start_index=24359)
Annotation(end_index=24451, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNowlCpnkWRaaBgXjLUmlCjeaG-OYEVI8A_c1KtCTw1YF-8-jk93gBum0esCOFL6_xPnyYaHX105eS_djTOLWw0_AL5LY807Tc4ek3HTlfEBdgxCv0tdw0FaI7vBsyfzK6I98yhI1Nz_mlWmIfq3Vk6vD9coTA9Q==', start_index=24441)
Annotation(end_index=24556, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRlSgan1HljMfnhy-2cwGO7bTARW3fBsVTj81VONpaHkVt11zykgaLsqJ45pw6CAXjytXx2WlRL9_2ZMQjXJgZ8xFZBXbxV0tu9HMp0-i2WJMmOHN3UutSxLbQxbp4f_0d6YElt1rJ-w==', start_index=24547)
Annotation(end_index=24662, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgovwpf_DVbnAeFKbHptkKGDl90Cc00b0iy1jlq-wYssCeLqZsMlxtw3EDvx3YKZLyVh5OxINDNtxt1SugOvzrBv1wBA29N6GixzE8VBPxx6xyCp1zJMuPJG2FWLAufNGyioCux4qrGEw2o4ie_pTzTUbCzwzWvxFL_OhSg5IPZsuWQY1Y2VI4gZoRcjz1b4ArGmwvx-_2vuwY7Cx_ZIi1RLDoGZ-TXxVuZovSR4bwwsk-c-fKc0uI5aA=', start_index=24652)
Annotation(end_index=24752, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE99QBHaGPmHqZF1dAnUPRdGgb7Fv2f6_bcOkQOtbJ8hQgiPZf6q-p3s8jnj2j7fVBk-YZS07wzOernwp71zFRV9y4MzGdbxbGqy2iVKAHo1CEn4zkihbsc45TgAcAtgZEfE5Kzm-2tHA==', start_index=24742)
Annotation(end_index=24843, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHe3jWqaIH4etzHCUumhcP1imBtxzYZU1zyO1NybGMABPF6N_y-ehbE1mb0lXLfdMiZhe160mgQ9-5u1oJ97222knuY5Q-XjFvQ44dWhXdovDe9JZflzO1xn1VHKa419BKwdbAFomA58u0W7ybGqLyA8mubvuVganVSeSmYciaiYGx2E9skKm85Nox-flOfEIYbIiATFdz0lwnuyHP5rJ8A6_7FmCXBHFE9hzbu', start_index=24833)
Annotation(end_index=24922, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL9noBOFPwx-VcH-x2SRzNhfbxKqSPfXV-smrx6r1U3TKnQm-JGCat0rSV0BbXni4O86erqI8r5RiCUR8EdGI5hkc8LQ3TtRCYih_kWHOcpiaDEI9FmwINXq-WcHWTxyCPkVh1cIcf', start_index=24912)
Annotation(end_index=25001, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbzLmcwekWH4sVMzW88ncXyhkZCl0oAvHCL5dAEK1I6sVS53RCZvzcTtV_HEXnk7R1omxilEQWiFO6rhgXQFzb-fC38XHcvsOqlwY2mvkkQ9ehOtjlnS7NZIopY_sDfOMOOgWDGEhTXus=', start_index=24991)
Annotation(end_index=25065, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6LgCDRpjoWbO_pc23bZH-JBpIHTv25aPstaHewtzMLoXhVPeWAzYLfdBfFhDBx8s6HYPsfeQVzAbjBqEuvixjvHHBNycEqoA-XjF-ClnwdmWXEGf6qGIP2IokDvkGBQ==', start_index=25055)
Annotation(end_index=25156, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHg9Q9sgokxUIpLUH7lGfCjX0As2COY2TZJ1K5qLVWyLPdSNR6Fa_0caN4DTXa4sNMsRJ9EeeLIxnTY-T2hfX2I_LiKkX8A7kpBMmLebm8rNlNm-HZyMseZ9X-QMj3YqSNTW9mgeZEU', start_index=25146)
Annotation(end_index=25247, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFihxyqkii5XorqY_KHmKDmTp3_uM1qOPpsrZW3gCIkoAMG5KKTDKwgcYJ8a6SPlFkY2kbaDoDS9cdggfL9sVOtqL826YQbNbGacQV0X7SyXQ1Efv_XEBiEG1LjPdZS8W5kLKHbu_h', start_index=25237)

## Sources
