# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 99bfca3a | **Time:** 387.62s | **Cost:** $2.34286
--------------------------------------------------------------------------------

# Adsorption Energy Level Distribution as a Constraint in Fuel Cell Durability Design Under Thermal Cycling

### Key Points
*   **The Fundamental Constraint:** Adsorption Energy Distribution (AED) acts as a critical design boundary because the thermodynamic requirements for catalytic activity (Sabatier principle) often conflict with the requirements for material stability under thermal stress. Sites with optimal adsorption energy for reaction kinetics are frequently the most susceptible to metal dissolution and restructuring during thermal cycling.
*   **Thermal Cycling Amplification:** Temperature fluctuations induce mechanical stress (expansion/contraction) and shift the chemical potential of adsorbates. This dynamic environment causes the AED to evolve over time—typically widening or shifting toward inactive regions—driving degradation mechanisms like Ostwald ripening, particle sintering, and surface segregation.
*   **Scaling Relations:** The linear scaling relationships between the adsorption energies of different intermediates (e.g., *O, *OH, *OOH) severely restrict the design space. It is difficult to optimize the AED for durability (e.g., weakening *O binding to prevent oxidation/dissolution) without simultaneously suppressing the catalytic activity for the primary reaction (e.g., Oxygen Reduction Reaction).
*   **Emerging Descriptors:** Recent computational advances propose AED as a distinct descriptor that aggregates binding energies across various facets and sites. This allows for the identification of complex alloys (e.g., High Entropy Alloys) where a broad AED provides a "buffer" against thermal degradation, maintaining active sites even as the surface reconstructs.

### Executive Summary
The durability of fuel cells, particularly Proton Exchange Membrane Fuel Cells (PEMFCs) and Solid Oxide Fuel Cells (SOFCs), is fundamentally limited by the physicochemical stability of the catalyst and electrode interfaces under dynamic operating conditions. Among these conditions, thermal cycling represents one of the most severe stressors, driving mechanical fatigue, chemical segregation, and active site degradation. This report investigates the role of **Adsorption Energy Level Distribution (AED)** as a governing constraint in the design of durable fuel cell components.

AED refers to the spectrum of binding energies available on a heterogeneous catalyst surface, dictated by the geometric arrangement (coordination number) and electronic structure (d-band center) of surface atoms. Under thermal cycling, the AED constrains design in three primary ways: (1) **Thermodynamic Instability:** High-energy adsorption sites required for high activity often serve as nucleation points for metal dissolution and corrosion; (2) **Kinetic Hysteresis:** The temperature dependence of adsorption isotherms (e.g., Temkin vs. Langmuir) alters the coverage of intermediates during heating and cooling transients, leading to localized starvation or poisoning; and (3) **Structural Evolution:** The drive to minimize surface energy during thermal cycling leads to surface reconstruction (sintering), which permanently alters the AED, typically removing the most active defect sites.

This report synthesizes current research on scaling relations, generalized coordination numbers (GCN), and high-entropy alloy (HEA) design to elucidate how AED manipulation—through strain engineering, ligand effects, and ensemble control—can mitigate thermal degradation while adhering to the Sabatier principle.

---

## 1. Introduction: The Physics of Adsorption and Durability

The performance of a fuel cell is dictated by the efficiency of electrochemical reactions at the triple-phase boundary, primarily the Hydrogen Oxidation Reaction (HOR) at the anode and the Oxygen Reduction Reaction (ORR) at the cathode. The rate of these reactions is governed by the adsorption energy of intermediates (*H, *O, *OH) onto the catalyst surface.

### 1.1 Defining Adsorption Energy Level Distribution (AED)
Classically, catalytic surfaces were modeled assuming a uniform adsorption energy (Langmuir isotherm). However, real catalysts—nanoparticles, alloys, and defect-rich surfaces—exhibit a distribution of adsorption energies. The **Adsorption Energy Distribution (AED)** is a probability density function representing the number of surface sites available at a specific binding energy [cite: 1].

The AED is not a static property; it is a function of:
*   **Surface Facets:** Different crystallographic planes (e.g., Pt(111) vs. Pt(100)) possess distinct binding energies [cite: 2].
*   **Coordination Environment:** Atoms at steps, edges, and kinks (low coordination) bind adsorbates more strongly than terrace atoms [cite: 3, 4].
*   **Electronic Ligand Effects:** In alloys, the proximity of different elements (e.g., Co or Ni near Pt) alters the d-band center, shifting the local adsorption energy [cite: 5, 6].

### 1.2 The Challenge of Thermal Cycling
Thermal cycling involves repeated temperature excursions, such as those experienced during startup/shutdown sequences or load variations in automotive applications. This creates a hostile environment characterized by:
*   **Mechanical Stress:** Mismatched thermal expansion coefficients (TEC) between the catalyst, support, and ionomer cause delamination and particle detachment [cite: 7, 8].
*   **Chemical Potential Shifts:** The free energy of adsorption ($\Delta G_{ads}$) is temperature-dependent ($\Delta G = \Delta H - T\Delta S$). A site that is optimal at operating temperature ($80^\circ$C for PEMFC, $800^\circ$C for SOFC) may bind intermediates too strongly or too weakly at ambient or transient temperatures, leading to poisoning or passivation [cite: 9, 10].
*   **Accelerated Kinetics of Degradation:** High temperatures exponentially increase the rates of metal dissolution, carbon corrosion, and Ostwald ripening [cite: 11, 12].

The central design problem is that the **AED required for high activity** (sites with optimal intermediate binding) often overlaps with the **AED that promotes degradation** (sites prone to oxidation and dissolution).

---

## 2. Theoretical Constraints: Scaling Relations and the Sabatier Principle

To understand how AED constrains durability, one must first understand the rigid theoretical framework governing catalysis: the scaling relations.

### 2.1 The Sabatier Principle and Volcano Plots
The Sabatier principle states that for a reaction to proceed efficiently, the catalyst must bind intermediates neither too strongly (poisoning the surface) nor too weakly (failing to activate reactants). This creates a "volcano plot" relationship between activity and adsorption energy [cite: 13, 14, 15].
*   **Constraint:** Design is restricted to a narrow window of adsorption energies (the volcano peak). Deviating from this to improve stability (e.g., making the metal more noble/inert) immediately sacrifices activity.

### 2.2 Linear Scaling Relations (LSR)
A profound constraint in catalyst design is the linear correlation between the adsorption energies of chemically similar intermediates. For ORR, the binding energies of *O, *OH, and *OOH are linearly correlated because they all bind through the oxygen atom [cite: 16, 17, 18].
*   **Equation:** $\Delta E_{*OOH} \approx \Delta E_{*OH} + 3.2 \text{ eV}$.
*   **Durability Implication:** To prevent catalyst degradation via surface oxidation (formation of Pt-oxide), one might wish to weaken the binding of *O. However, scaling relations dictate that weakening *O binding will also weaken *OH and *OOH binding. If *OOH binding becomes too weak, the initial protonation step of O2 becomes kinetically impossible, killing the reaction. Thus, the AED cannot be arbitrarily tuned to avoid "dangerous" adsorption energies that lead to degradation; the chemistry is coupled [cite: 13, 19].

### 2.3 Breaking Scaling Relations for Durability
Research suggests that "breaking" these scaling relations is necessary to decouple activity from instability. Strategies include:
*   **Geometric Manipulation:** Using specific facets or generalized coordination numbers (GCN) to preferentially stabilize one intermediate over another [cite: 2, 20].
*   **Bifunctional Catalysts:** Using different sites for different steps (e.g., High Entropy Alloys), creating a broad AED where specific sites handle specific intermediates, potentially bypassing the linear constraint [cite: 6, 21].

---

## 3. Mechanisms of Degradation Driven by Adsorption Energy

The distribution of adsorption energies on a catalyst surface is the primary driver for several degradation modes accelerated by thermal cycling.

### 3.1 Metal Dissolution and Surface Energy
Metal dissolution is the most severe degradation mechanism for cathode catalysts (e.g., Pt, Pt-Co) under thermal and voltage cycling.
*   **The Link to Adsorption Energy:** There is a direct correlation between oxygen adsorption energy and the dissolution potential of surface atoms. Atoms that bind oxygen strongly (high adsorption energy) are more easily extracted from the lattice to form dissolved ions ($Pt^{2+}$) or oxides [cite: 19, 22].
*   **Low-Coordination Sites:** Sites with low Generalized Coordination Numbers (GCN), such as corners and edges, have the highest adsorption energies (strongest binding). Consequently, these are the most active sites for ORR but also the first to dissolve during thermal transients [cite: 3, 4].
*   **Thermal Cycling Effect:** As temperature rises, the kinetics of dissolution increase. Furthermore, the formation of surface oxides during the high-potential/high-temperature phase of a cycle, followed by their reduction during low-potential phases, roughens the surface and accelerates mass loss [cite: 11, 23].

### 3.2 Ostwald Ripening and Sintering
Sintering involves the growth of large particles at the expense of smaller ones to minimize total surface energy.
*   **AED Driving Force:** Small particles have a high proportion of low-coordination sites (edges/corners) with high surface energy (and high adsorption energy). This high energy state is thermodynamically unfavorable. Thermal cycling provides the activation energy for atoms to diffuse and merge, eliminating these high-energy sites [cite: 24, 25].
*   **Resulting AED Shift:** As particles sinter, the population of high-energy edge sites decreases, and the population of lower-energy terrace sites increases. The AED narrows and shifts, typically resulting in a loss of catalytic activity (movement down the volcano plot) [cite: 26].

### 3.3 Carbon Corrosion and Support Interaction
The adsorption energy of water and oxygen on the carbon support also plays a role.
*   **Hydrophilicity/Hydrophobicity:** Thermal cycling affects the hydrophobicity of the Gas Diffusion Layer (GDL) and catalyst support. Degradation of the hydrophobic PTFE coating changes the water distribution, leading to local flooding or acid leaching (in HT-PEMFCs) [cite: 9, 27].
*   **Corrosion Mechanism:** High potentials and temperatures facilitate the adsorption of oxygenated species on the carbon support, leading to its electrochemical oxidation ($C + 2H_2O \to CO_2 + 4H^+ + 4e^-$). This corrosion detaches catalyst nanoparticles, leading to catastrophic active area loss [cite: 11].

---

## 4. Thermal Cycling Specifics: Hysteresis and Transient States

Thermal cycling introduces dynamic constraints that are absent in steady-state operation.

### 4.1 Temperature-Dependent Adsorption Isotherms
The coverage of adsorbates ($\theta$) is governed by isotherms (e.g., Langmuir, Temkin, Freundlich) which are temperature dependent.
*   **Temkin vs. Freundlich:** Research indicates that adsorption behavior shifts models based on temperature. For example, in perovskite cathodes, low-temperature adsorption ($550-650^\circ$C) follows the Temkin model (linear decrease in heat of adsorption with coverage), while high-temperature adsorption ($700-800^\circ$C) follows the Freundlich model [cite: 10].
*   **Polarization Resistance:** The polarization resistance associated with adsorption rises exponentially with decreasing temperature. During the cooling phase of a thermal cycle, the resistance can surge (e.g., from $0.01 \Omega cm^2$ at $700^\circ$C to $1.20 \Omega cm^2$ at $550^\circ$C), creating massive overpotentials that can damage the cell materials [cite: 10].

### 4.2 Acid Redistribution in HT-PEMFCs
For High-Temperature PEMFCs (using Phosphoric Acid doped PBI membranes), thermal cycling drives the physical migration of the electrolyte.
*   **Adsorption/Desorption of Acid:** Phosphoric acid is adsorbed into the catalyst layer and GDL. High temperatures increase the vapor pressure of PA, promoting evaporation and migration. Upon cooling, the acid may re-adsorb in non-optimal locations, leading to flooding or pore blockage [cite: 7, 27].
*   **Design Constraint:** The GDL and microporous layer (MPL) must be designed with specific adsorption energy properties (surface energy) to retain acid within the active area during thermal expansion and contraction [cite: 27].

### 4.3 CO Poisoning Hysteresis
In reformate-fed fuel cells, CO poisoning is a major issue. CO adsorption is strongly exothermic.
*   **Thermal Effect:** High temperatures ($>120^\circ$C) significantly reduce the Gibbs free energy of CO adsorption, alleviating poisoning. However, during the cool-down phase of a thermal cycle, CO coverage rapidly increases, potentially "choking" the catalyst before the system completely shuts down. The AED must be tuned to minimize CO affinity even at lower transient temperatures [cite: 9].

---

## 5. Design Strategies: Manipulating AED for Durability

Given these constraints, modern fuel cell design focuses on engineering the AED to balance activity and stability.

### 5.1 High Entropy Alloys (HEAs)
HEAs (alloys of 5+ elements) represent a paradigm shift. Instead of a single adsorption peak (like Pt), HEAs possess a broad, continuous AED due to the millions of different local atomic environments (ensemble and ligand effects) [cite: 6, 21, 28].
*   **The "Buffer" Effect:** A broad AED ensures that at any given temperature or operating condition, there is a sub-population of sites with optimal binding energy.
*   **Stability:** The high entropy of mixing stabilizes the solid solution phase, retarding diffusion and sintering. Even if some surface atoms dissolve, the statistical distribution ensures other active sites remain. HEAs like **ZnPt3** and **ZnRh** have been proposed via machine learning as candidates with optimal AEDs and high stability [cite: 1, 29, 30].
*   **Constraint Mitigation:** The broad AED allows the catalyst to "defy" the trade-off to some extent, maintaining activity while the bulk structure resists thermal degradation [cite: 31].

### 5.2 Generalized Coordination Number (GCN) Engineering
Designers now use GCN as a descriptor to tailor the surface geometry.
*   **Optimization:** The optimal GCN for ORR on Pt is approximately 8.3 (concave defects). Standard nanoparticles have a mix of low-GCN (corners, <7) and high-GCN (terraces, 9).
*   **Durability Strategy:** By synthesizing catalysts with specific shapes (e.g., nanowires, framed structures) that maximize the population of sites with GCN ~8.3 while minimizing sites with GCN < 7 (which are prone to dissolution), designers can narrow the AED around the "sweet spot" for activity while truncating the "tail" of the distribution that causes instability [cite: 3, 20, 26, 32].

### 5.3 Surface Passivation and Skin Structures
To manage the AED, "skin" structures are employed.
*   **Pt-Skin:** In Pt-Ni or Pt-Co alloys, a surface layer of pure Pt (skin) is formed over the alloy core. The subsurface alloy exerts a ligand/strain effect on the skin, shifting its d-band center and weakening oxygen adsorption (optimizing AED for activity) [cite: 2, 33].
*   **Protection:** This skin also protects the less noble core metals (Co, Ni) from dissolution. The AED of the skin is tuned to be active, while the core provides the electronic modification and structural stability [cite: 5].

### 5.4 Machine Learning and AED Descriptors
Recent computational frameworks explicitly use AED as a descriptor for discovering new materials.
*   **Methodology:** Machine learning models aggregate binding energies from thousands of surface motifs to predict the full AED of a candidate material. This allows for the screening of materials that not only have high theoretical activity but also possess an AED profile indicative of thermal stability (i.e., lacking sites with excessively strong binding that leads to corrosion) [cite: 1, 34].
*   **Candidates:** This approach has identified materials like **ZnPt3** and **ZnRh** as promising stable catalysts for thermal catalysis, a concept now being translated to electrocatalysis [cite: 29, 30].

---

## 6. Conclusion

The **Adsorption Energy Level Distribution (AED)** is the physicochemical fingerprint that determines both the life and death of a fuel cell catalyst. Under thermal cycling, the AED acts as a rigorous constraint:

1.  **The Stability Constraint:** The high-energy tail of the AED, often necessary for high activity, is the Achilles' heel where dissolution and corrosion initiate. Thermal cycling exacerbates this by providing the thermal activation for these degradation processes.
2.  **The Dynamic Constraint:** The temperature dependence of adsorption means the "optimal" AED is a moving target. A catalyst designed for peak performance at $80^\circ$C may suffer from poisoning or kinetic sluggishness during the thermal transients of startup and shutdown.
3.  **The Design Imperative:** Successful durability design does not merely seek the highest activity (peak of the volcano). Instead, it seeks to **shape the AED**—truncating the high-energy sites that cause dissolution (via GCN engineering), broadening the distribution to ensure resilience (via High Entropy Alloys), or shifting the mean via ligand effects (core-shell structures)—to survive the mechanical and chemical rigors of thermal cycling.

Future design methodologies will increasingly rely on computational AED mapping to predict not just how a catalyst performs when fresh, but how its energy distribution—and therefore its performance—will evolve over thousands of thermal cycles.

---

## 7. Detailed Analysis of Research Findings

### 7.1 Adsorption Energy Scaling and Durability
The concept of scaling relations is pivotal. As noted in [cite: 16, 17], scaling relations have evolved from simple transition metal surfaces to complex alloys. The breakdown of these relations is often the goal of advanced catalyst design. For durability, the constraint is that stabilizing the surface (making adsorption energies more positive/weaker) often pushes the material into an inactive regime.
*   **Dissolution vs. Adsorption:** [cite: 19] explicitly links the energy required to dissolve a metal atom to its oxygen adsorption energy. The "uphill" energy to break metal-metal bonds is often compensated by the "downhill" energy of forming metal-oxygen bonds. Therefore, elements with high oxygen affinity (strong adsorption) are inherently less stable against dissolution in oxidative environments.
*   **Magnetic Effects:** [cite: 35] highlights how external fields (magnetic) can alter the Fermi level and adsorption properties, potentially offering a non-material way to tune AED dynamically, though this is less conventional.

### 7.2 The Role of Support and Interface
The AED is not limited to the catalyst particle; it extends to the support interface.
*   **GDL and Acid:** [cite: 27] demonstrates that the GDL's ability to retain phosphoric acid is a function of the adsorption energy of the acid on the carbon fibers and microporous layer. Thermal cycling drives acid out of the pores (desorption/evaporation). Durability depends on selecting GDL materials with an AED that favors acid retention even at high T.
*   **PTL Interface:** [cite: 36] discusses the porous transport layer (PTL) in electrolyzers (analogous to FCs). The interface contact and pore structure affect mass transport. Mismatched AEDs (hydrophilicity) at the interface lead to gas trapping and increased resistance.

### 7.3 High Temperature PEMFC Specifics
HT-PEMFCs operate at $160-200^\circ$C.
*   **Thermal Stress:** [cite: 7] identifies thermal cycling as the "most severe operational stress." The membrane and electrodes expand/contract, leading to delamination.
*   **Adsorption Physics:** At these temperatures, water is vapor. The proton conductivity depends on PA doping. The AED of PA on the PBI membrane is critical. If the interaction is too weak, PA leaches out during cycling. If too strong, it may not facilitate proton hopping effectively.

### 7.4 Machine Learning and Future Directions
The emergence of AED as a formal descriptor in machine learning [cite: 1, 30] is a significant leap.
*   **Aggregated Descriptor:** Instead of using a single value (e.g., binding energy on the (111) facet), the AED descriptor accounts for the *entire* surface. This is crucial for thermal cycling because degradation often starts at minority sites (defects) that a single-value descriptor would miss.
*   **Predictive Power:** By mapping the full AED, models can predict which materials will maintain a stable population of active sites even after the surface has undergone thermal restructuring.

### 7.5 Synthesis of Constraints
The constraints can be visualized as a multi-dimensional optimization problem where:
*   **X-axis:** Adsorption Energy (Activity).
*   **Y-axis:** Lattice Stability (Dissolution Energy).
*   **Z-axis:** Temperature (Thermal Cycling).
The "safe" operating volume is bounded by the Sabatier optimum on the X-axis, the dissolution threshold on the Y-axis, and the phase stability limits on the Z-axis. Thermal cycling forces the system to traverse the Z-axis repeatedly, often pushing the material across the Y-axis threshold (dissolution) or away from the X-axis optimum (hysteresis).

**Final Conclusion on Design:** To design for durability under thermal cycling, one must engineer the **Adsorption Energy Distribution** to be robust against temperature swings. This implies using materials (like HEAs or specific intermetallics) where the active sites are thermodynamically stable against segregation and dissolution, and where the distribution of energies is broad enough to sustain activity across the transient temperature range of the thermal cycle.

**Sources:**
1. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHVjo5qWybOyD-njhoftlH-UwA-5gkgl-76Gwc8AXI4r2aSpNcE12Gg7-fe0ZRBJnWqt-RHQQc_sAdDoiEeP50N99ZR4BeEYMx2ihzJmp4L42rPgpGovFv)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzisIDhvIEil_sN72M8MKgUcKRjqyFV9i3uv4p3244crx5izTs2EKhr1aTJvJ9TiJspvBfgws8Kx2xtLB6KrRnc23WIV3AO4P7ADbEqFD70vmNVWhj0mvKDN2rTZ3SCEs82RJLltKczoV5unX2-vc5hpJlNNanzWsfOCP1-0zV8kgStIJHlU9NwjMvQtQZoyo6DSp0JDPyhcZ7XNwbL5iI3Nljok6dJ1UMezLXTcvKiht7IjIx-NYIb28Y6yw6hIVL-JSgAInKttcUHn_QwTn0Lkjryw==)
3. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHm78yWDCPRmnU0xjjR7FAc6LYs_XmrA-N8pMY5KpHR0sGWQG25-2_F9CdPvgvZ4CRfRcL3HvEGSK3NDsEriwP8FIgzjHVQZo2kc8fNw-_RVO7kex_P)
4. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGO42APmJnoVhJemXq2LFtm19c2VekDXFkJE6udsGPS5UgXa-GS6hRTHVehVdCq0QG2_0HgXcOmGN1AH2UOPG3aCrSTkcMhtebpScx8M9qh7geoyME6iySLMyrLJBX2MrNBna6TK0NlQQPRxr1GQdu8-PHh)
5. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4icaeTwi86ZNLZUGo3bO8wrnzS8Y2Fgp5hurgmyMZZduiNSh30J7sFQjYf1pFStmx3w3WKQFtcjay7MygUT8bAKxRt1j0FHxdr17d1oX0Nv2YhSEXwrpiW3jk0ffXDb3gsISj9ndvXmm3B0w4c38FLxQRew9HEvBJDysg589Js4Mm0U82DeWo417l853STB9JFw-pBNyVhNFYm2RMwlB48OWLzL2-KoNnQfZ5SJVG9KMRs3wuL4jVDTXOV2F47xgVmQp-mcY66TRmqybcmJ-SWYfBPt6QLh5UFaab2YpJO_7J8_zYbzTUZMMl1PZ4)
6. [doi.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5Lb8VR2rTjRdlU8VfImIVd3Z4Lkzm7anRvm30-21wgUDA3ETT16uB09bUnAe0mXYhroXyIVVFfbCpHSArXhvbyz4b-q6-lVYJc7DbgRHhYvqA3g3nd0an1lLU64eH_Gn9feutYW4L)
7. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjEYqEY5Y8KfwcEHChS8dTHFUR8iS02PPFTljxh-3qqrBqQ9gmhQ9D8w9o02kXoUX2hgh-IlIa5hIbrexhyhWfa04CtfXPI494VDHpm1ZYeIr4dbNNWJhga_HjURZ5WKPWwU8V-65TqCbRI6opSQpcE8DN)
8. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESduNn2KtVliX5D89RiDr2HRw_6UBUSQFQjnQns0wYARsaNGmV2wOyBI9OFR7yf9_gMMJ9z5FxUMJvTYT0EqvmyHGtVpvi1oGiJQprjNGUZXOKn1NbmUs26zjec40-xiT9Y63yfASATu4u6tHajJ8R731vEzxMmM_lKnJjiCo-XQ4geYUc__soPChDuT1R8LHilw==)
9. [dtu.dk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXdEuEh-MG1FLp_kieM3rdaY9Epe6dV_7P8LxyOV092XlD5ItjG6HatcKw60kvBqArKH_0xvR7Yrf6_bMlEaH2fMSA53FzI7EKkav8SGLkmn86KQm6r0IeVo4e9n7WPGnwRmhuIf3UHSR9P0TrCwIHRX61F_T_OKssF3h9fT-fdNr1O6AWFzMMjkI=)
10. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBqL66U9kIwEiFpmJkh-Jm0JU2Sg1_HVGVWdiY-QbygK8bpby0vhR5Cxrmfr3uYSHtygANRB-lX9NK3n0ioJusysjbyFJj_icV-hqHSQYk23l-QRsIR-TP36JVk7hc)
11. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoGGtls1MkmLzZY3u-t5Zq-88tCsYlrYDwL4N8FVfeUaMk6GPlGZO3OR6J9cTW0fI7KP9QD4VrEBj859lDOn0Y_TcHovRIqTNUA7iU0XVNUmQqCPKytN-PYA376_-1Y1SwWmFF8p8=)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhkellkd9JblNakpcx60t5Q0sc8xEIVjtzqFF9QiDsODOdlRS4OWCDQ298tPF6q06g_yUSpBSO3Z9xqMU8s9M3i_PV-pqAawFlCc-B00MJ6hbW9Wk225NZjwmT8TlyJBYkEStxmw6Mf6JMGHryRbTwdnAZGdDYgyZSVuOjt6c0ufVJ3Fo5qJcLDtDZZU28KCeulTnj8B267BhQ1jHHw7TdwrGldjuW3h_WFK3GDchATJC8LnsEnbA=)
13. [chemrxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwSpZ5MMWxfVKh8UTc6RL3YVAWJ_Y_VsjOSNdg-TSZ435DgxJkQunwyKJKmaYAgLghAcz8agI50IiH2CpY9GHjpyhBLoQCmKAvBJ3BR9o4yXgybkB3iv9w0WuaUTDiTQs9C7m6p8z_v35Okr-8gA==)
14. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE146wCznOwbm6CQlvQyrr1zsBHd9JZCd4m4FePgEDCpVHUa1BC8-ViqQmiZGIHbRzthvPCMBAEE0qv8GzWoxHemg3-kFG-xnjiJ0E2AwuPC8iaHKjgI8GOr-ZR7Vseqy5L39eS)
15. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrBPRDdZ4eKKrtB-9sPoHAd_zF8qks3RBtE3E639fG0LPXZjbMwn7QjYCOt-b7O0Nu5bk16fjYI0p4nodX0b6XR2ZgLM8eC7YHTe8Cza6hB2J4POUbltl1ijAtFDe7h8FvT0mGpeRgqmJjI7ouvm_sw7d_)
16. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5HSyVi7o_ZpYFghACFV6BZwQdx7PSZwcLmvyh4eBgx1kSpz34HuKVSOWiYeAWTkEYo8a514YnEh-rqvsC86BDwDIzcoctcUIf8t37NfGOtMKgXGpF)
17. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGx2HegxLDnXFHevPpVKnG0AKLGQP-dGU7FqAYbHsje10_J3r1DqMgPT7u1GKtJlY-MjkeVWcQuk3bdXv5MyujLyCuYHB_SjKOK7g2FqARcNpgFGiGbNrPbUG_HjldZqk7Pohe6TjRVO_5g6X9tTtdjEOHTjTQe)
18. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvRYw-7ZO9R7gP2j769o0EhBOzqFo74EORyvkxp0baUFfQIn2Cxg7QEMJQotaWmEGVOZIoze2sM-IXafoBT28YgdsxZyeKLnAUpIjM_mBvcEt6-lFSKZWE6FZjoEamXuRpqzRT)
19. [Link](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYmfemR-M9x-vmuDJ156mJBdHDOkeUhSRgtxCmUV0KjfBqJ1qOvATzIk6UEbtgQPPx8dTpGXMUMWodtyi2ufz4s-j7EACGXW_B5iG5pZTj3xlX0bxY9e8_nbCRUtkub_EJ8Vw6E_o=)
20. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGV4v-ilS6hYm0ZWc1tYqPGGnyK0ZZIEyGm11ccK2ynysdE85PNrI7NitniEhoiq5ScUk7FLLZ-xzM2HR2_chgrIvX880eLHh8t36DAmZI3NXMOm00q1sVDuu-XaLl_lv1kHH-Ce8uc)
21. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlnxrB0lxR5tpZGpciFXDdNgZ3zTEbaEBVwiEDPuY-T4sFeVuatkqgrLgPAruJyVZlvL3MhqWMkn2UyvXtGwArdraJoS9q00rasifSkMyWPmD6Rs-ApeVZ_w9jbKm423PD858alQs=)
22. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFs0Pb059h8b40kaj-krtzjzAkHk4iGI9ppl5NHne0_BG6jAHgklhrOGF-HAtPbnj3ZZgJCcKQyG2EykESka1gIRf170anlQqrZAnpHHeCmff6amAlxP__cpvm_f-iw58_4o128VXA=)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGszFLkqrmaEzz6IxdsJYA72NDuKg0mq_KcpHpf1-QiFHjouuI8AbzXULpyfJybCkyLwOEXvutzV1bQI5-LfsaUKWhpNSSMwc-Gg4otxChX2xfvDgzdp9xV4B1l6UBTwLmi2aIIyOUFg7cMcQA0uW09H9wWQ_-RrajWdR8D8Lh3wJDj20hm2G1ySrm_8tXaUCBr5ZuwhSLm4vR18tAGRVbFU28eUJus-iNan6XDVIrOKDs=)
24. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDJ1RrsZBh9-FiNWQ5V98VQLa5qWOn3PQmGn6agV93YnjX8ttJhStcDI1W5HidAR1nEgSM7Yum-go2gJeDZz2-3aJoyKuN6YP4BaAOFLZsSiyAS-m7QCMKhOxVR69Km4T37UKV2TYFXt7Ial6d)
25. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKdyXuO-PYpuFiA7TMWEH69EYcxMpnhKxvUvaeBFa6pD6xspp6y0ObWvxHT37pdgS0DeoY5cirLkYc9TvVQ8crC7ocWxHqDaW7HWFM0impeM5jLDw_pqO6hec4BV1i66gzaa9T-rg=)
26. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPHhSNM6WMOmfPnRGdXiGajadJqeodpd9ot9NHUWlAaKY7shiKex-_DJIrgnnM1SQFkXaPEiV5SOVLhK3FIRT62TUkyqrjrniifETqpK537jcVLJ1yzicMtJg9_30WxqTQtwjVMJI=)
27. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBxhUJIb4uRdUgnj-H-WQaMQVvBLA8Yo3_QLgTHpXN0S8NqoIFyJvawi1YuXNiwurzRU_jP4-Jc76B_0w0LesA94Ypoq0ZeSxBdAt6iZzHs9xwyWB1U7gJTc0t5rRJGxjLi01Q-NKjtW5K7m0atTb_97RdKYMtU-VT_lOBisqq4wQaGabD8w-PZtdteyooio_BzMGZIfoKYMALjYsvD5Yg9dRCE6rB6vj_Q4qJWLeEYrSt4Vv6XkkptDSDAXRBXso=)
28. [hep.com.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4WlGMkD8UxLVki548qhaO4vukkGEoRWMp73ytc4060od7T1SRX0SoI3821twgEbKedttDlKyd1rRQ_gQNvmByL2bS-qmlrybodndDftqrVn8QgANxToVGiWWhPsMvNj7f5HW0jqhYUnLm)
29. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkKy7b71EzpQNb_64BNJeKh8Xe5SvWf_LkGvujVNBEWoCx7ycusjzBOz5omfsvrFp_PCN9RdV_9hX0Cox9HyYChQwacOzLeDCdoqy9ScqKtLPhKyx6gerTLtRWaYkvlSih7ewD8Nr6pgzmVB2rD2lsFNTH04ejKeATGByk9a1JIEscaZyeOBAqQruVyMxtu01Wl4q10JxECw-3ykoA-6R6Ti_BsOfaMAshpGoD6NWBvDa52FOkcLtA17nxlQ==)
30. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7bR9HWu9tIPmD_svYcVkCF92goQ-G9fpEZH1L8RWM3pJsZ_fFwm0MmPXRSBkuntIJdSVBulBETag9QF-1vjKGXDXy87a_4uUZ0z6gq118Akyg06_y)
31. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHo9rHWLeOZ_YBR-Gt5ql2TcU6oEKBHnRnfGkXzLBW_aUecm8dA0kUbJqzcn22mwgmCFwi_zRlaUNuORVDlo3kzf6XeA_R7VLLzwUepJKY1LUHRXJHB8tGZt16L_EAwOYpis9E1oUjz)
32. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjEhalclfK6R3M0LlLp5H2Izv0A2q9yVX44sH92OGCa5ZOVsHTgHWuUqMi46xMtHdN2jVRuJajGFPdOospTsKk50_Fu6YMSBpcvnkfyqDmRYpLdBSUP5Ta8ADN4oyY1H_JKdnFOYzQtU02kammLFQtlKcbrzk21807b5vfegtIcQbY1XiapUEjjPv7eZkk4u12EYI4Arr-yfABbboKgrHRyLx3Ty1HUDtciuhMQQb6vD2m5TETHwqvj-iBW23RkgSG9A5JJ_0=)
33. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIDpj7ng7QrGnheYezkMBc6rOrhyTbj1ztJ0-oWav1giQC_RLiV_NN8pzDMW8qNPAQMoyr6sPBC-twV9Nw3KNCVBZ1xRnY2851ccwXOHrdi4aUDfNYV269thhf6RzyKr_UJnZM)
34. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEF-vko3Kawnyk027AblEC5jBrIsC7YgRO3wBVXl5hE8uL1xjsWEZeQNa5yqyt38cFeWUOJtCmsN3fP-oiQg-1BHUWLZz51OhU0kZcBKPYOHooTkaFkYfKIM03GiuJeSjBVym94Y0yJtN-Fbk_XtlVF6dT0TEyn2Wbg2lb6crVmQOZMC6ZH5h4z-FAYJHukADfthiOJAwtahL7JG-tHAKXC64sL1yZgag0W_MqmqwaVkc1b3oq-yxj3uSoZnM7URUCwdIn__AuOu83q-yE=)
35. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7cJOKxRq2DFyVWP43Psk-3x000ztixlfigvS59KQ8luxxJRzGEGw1u2axno9bZjvAuKVDh4MrIOwk9FUZI9UfP7PqIq9cnscrvyi-f2ksZnhEQAx-AODSwOkwQRyJsWQ_Ag==)
36. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3979HZFJIB7IybvOz8TM2bPz2a4z8n12BmDKkxoMwKqI0H-vaubYBwg8I1v2kcJP3gNmAyGgGJtOfKNqYCaqycVyuOLaa6-c888So9LYONPm3oKSlrpm7aRlwSg==)


## Annotations
Annotation(end_index=4414, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHVjo5qWybOyD-njhoftlH-UwA-5gkgl-76Gwc8AXI4r2aSpNcE12Gg7-fe0ZRBJnWqt-RHQQc_sAdDoiEeP50N99ZR4BeEYMx2ihzJmp4L42rPgpGovFv', start_index=4405)
Annotation(end_index=4601, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzisIDhvIEil_sN72M8MKgUcKRjqyFV9i3uv4p3244crx5izTs2EKhr1aTJvJ9TiJspvBfgws8Kx2xtLB6KrRnc23WIV3AO4P7ADbEqFD70vmNVWhj0mvKDN2rTZ3SCEs82RJLltKczoV5unX2-vc5hpJlNNanzWsfOCP1-0zV8kgStIJHlU9NwjMvQtQZoyo6DSp0JDPyhcZ7XNwbL5iI3Nljok6dJ1UMezLXTcvKiht7IjIx-NYIb28Y6yw6hIVL-JSgAInKttcUHn_QwTn0Lkjryw==', start_index=4592)
Annotation(end_index=4750, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGO42APmJnoVhJemXq2LFtm19c2VekDXFkJE6udsGPS5UgXa-GS6hRTHVehVdCq0QG2_0HgXcOmGN1AH2UOPG3aCrSTkcMhtebpScx8M9qh7geoyME6iySLMyrLJBX2MrNBna6TK0NlQQPRxr1GQdu8-PHh', start_index=4738)
Annotation(end_index=4750, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHm78yWDCPRmnU0xjjR7FAc6LYs_XmrA-N8pMY5KpHR0sGWQG25-2_F9CdPvgvZ4CRfRcL3HvEGSK3NDsEriwP8FIgzjHVQZo2kc8fNw-_RVO7kex_P', start_index=4738)
Annotation(end_index=4934, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5Lb8VR2rTjRdlU8VfImIVd3Z4Lkzm7anRvm30-21wgUDA3ETT16uB09bUnAe0mXYhroXyIVVFfbCpHSArXhvbyz4b-q6-lVYJc7DbgRHhYvqA3g3nd0an1lLU64eH_Gn9feutYW4L', start_index=4922)
Annotation(end_index=4934, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4icaeTwi86ZNLZUGo3bO8wrnzS8Y2Fgp5hurgmyMZZduiNSh30J7sFQjYf1pFStmx3w3WKQFtcjay7MygUT8bAKxRt1j0FHxdr17d1oX0Nv2YhSEXwrpiW3jk0ffXDb3gsISj9ndvXmm3B0w4c38FLxQRew9HEvBJDysg589Js4Mm0U82DeWo417l853STB9JFw-pBNyVhNFYm2RMwlB48OWLzL2-KoNnQfZ5SJVG9KMRs3wuL4jVDTXOV2F47xgVmQp-mcY66TRmqybcmJ-SWYfBPt6QLh5UFaab2YpJO_7J8_zYbzTUZMMl1PZ4', start_index=4922)
Annotation(end_index=5369, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESduNn2KtVliX5D89RiDr2HRw_6UBUSQFQjnQns0wYARsaNGmV2wOyBI9OFR7yf9_gMMJ9z5FxUMJvTYT0EqvmyHGtVpvi1oGiJQprjNGUZXOKn1NbmUs26zjec40-xiT9Y63yfASATu4u6tHajJ8R731vEzxMmM_lKnJjiCo-XQ4geYUc__soPChDuT1R8LHilw==', start_index=5357)
Annotation(end_index=5369, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjEYqEY5Y8KfwcEHChS8dTHFUR8iS02PPFTljxh-3qqrBqQ9gmhQ9D8w9o02kXoUX2hgh-IlIa5hIbrexhyhWfa04CtfXPI494VDHpm1ZYeIr4dbNNWJhga_HjURZ5WKPWwU8V-65TqCbRI6opSQpcE8DN', start_index=5357)
Annotation(end_index=5749, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXdEuEh-MG1FLp_kieM3rdaY9Epe6dV_7P8LxyOV092XlD5ItjG6HatcKw60kvBqArKH_0xvR7Yrf6_bMlEaH2fMSA53FzI7EKkav8SGLkmn86KQm6r0IeVo4e9n7WPGnwRmhuIf3UHSR9P0TrCwIHRX61F_T_OKssF3h9fT-fdNr1O6AWFzMMjkI=', start_index=5736)
Annotation(end_index=5749, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBqL66U9kIwEiFpmJkh-Jm0JU2Sg1_HVGVWdiY-QbygK8bpby0vhR5Cxrmfr3uYSHtygANRB-lX9NK3n0ioJusysjbyFJj_icV-hqHSQYk23l-QRsIR-TP36JVk7hc', start_index=5736)
Annotation(end_index=5922, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoGGtls1MkmLzZY3u-t5Zq-88tCsYlrYDwL4N8FVfeUaMk6GPlGZO3OR6J9cTW0fI7KP9QD4VrEBj859lDOn0Y_TcHovRIqTNUA7iU0XVNUmQqCPKytN-PYA376_-1Y1SwWmFF8p8=', start_index=5908)
Annotation(end_index=5922, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhkellkd9JblNakpcx60t5Q0sc8xEIVjtzqFF9QiDsODOdlRS4OWCDQ298tPF6q06g_yUSpBSO3Z9xqMU8s9M3i_PV-pqAawFlCc-B00MJ6hbW9Wk225NZjwmT8TlyJBYkEStxmw6Mf6JMGHryRbTwdnAZGdDYgyZSVuOjt6c0ufVJ3Fo5qJcLDtDZZU28KCeulTnj8B267BhQ1jHHw7TdwrGldjuW3h_WFK3GDchATJC8LnsEnbA=', start_index=5908)
Annotation(end_index=6727, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE146wCznOwbm6CQlvQyrr1zsBHd9JZCd4m4FePgEDCpVHUa1BC8-ViqQmiZGIHbRzthvPCMBAEE0qv8GzWoxHemg3-kFG-xnjiJ0E2AwuPC8iaHKjgI8GOr-ZR7Vseqy5L39eS', start_index=6709)
Annotation(end_index=6727, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrBPRDdZ4eKKrtB-9sPoHAd_zF8qks3RBtE3E639fG0LPXZjbMwn7QjYCOt-b7O0Nu5bk16fjYI0p4nodX0b6XR2ZgLM8eC7YHTe8Cza6hB2J4POUbltl1ijAtFDe7h8FvT0mGpeRgqmJjI7ouvm_sw7d_', start_index=6709)
Annotation(end_index=6727, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwSpZ5MMWxfVKh8UTc6RL3YVAWJ_Y_VsjOSNdg-TSZ435DgxJkQunwyKJKmaYAgLghAcz8agI50IiH2CpY9GHjpyhBLoQCmKAvBJ3BR9o4yXgybkB3iv9w0WuaUTDiTQs9C7m6p8z_v35Okr-8gA==', start_index=6709)
Annotation(end_index=7263, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5HSyVi7o_ZpYFghACFV6BZwQdx7PSZwcLmvyh4eBgx1kSpz34HuKVSOWiYeAWTkEYo8a514YnEh-rqvsC86BDwDIzcoctcUIf8t37NfGOtMKgXGpF', start_index=7245)
Annotation(end_index=7263, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvRYw-7ZO9R7gP2j769o0EhBOzqFo74EORyvkxp0baUFfQIn2Cxg7QEMJQotaWmEGVOZIoze2sM-IXafoBT28YgdsxZyeKLnAUpIjM_mBvcEt6-lFSKZWE6FZjoEamXuRpqzRT', start_index=7245)
Annotation(end_index=7263, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGx2HegxLDnXFHevPpVKnG0AKLGQP-dGU7FqAYbHsje10_J3r1DqMgPT7u1GKtJlY-MjkeVWcQuk3bdXv5MyujLyCuYHB_SjKOK7g2FqARcNpgFGiGbNrPbUG_HjldZqk7Pohe6TjRVO_5g6X9tTtdjEOHTjTQe', start_index=7245)
Annotation(end_index=7868, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYmfemR-M9x-vmuDJ156mJBdHDOkeUhSRgtxCmUV0KjfBqJ1qOvATzIk6UEbtgQPPx8dTpGXMUMWodtyi2ufz4s-j7EACGXW_B5iG5pZTj3xlX0bxY9e8_nbCRUtkub_EJ8Vw6E_o=', start_index=7854)
Annotation(end_index=7868, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwSpZ5MMWxfVKh8UTc6RL3YVAWJ_Y_VsjOSNdg-TSZ435DgxJkQunwyKJKmaYAgLghAcz8agI50IiH2CpY9GHjpyhBLoQCmKAvBJ3BR9o4yXgybkB3iv9w0WuaUTDiTQs9C7m6p8z_v35Okr-8gA==', start_index=7854)
Annotation(end_index=8218, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzisIDhvIEil_sN72M8MKgUcKRjqyFV9i3uv4p3244crx5izTs2EKhr1aTJvJ9TiJspvBfgws8Kx2xtLB6KrRnc23WIV3AO4P7ADbEqFD70vmNVWhj0mvKDN2rTZ3SCEs82RJLltKczoV5unX2-vc5hpJlNNanzWsfOCP1-0zV8kgStIJHlU9NwjMvQtQZoyo6DSp0JDPyhcZ7XNwbL5iI3Nljok6dJ1UMezLXTcvKiht7IjIx-NYIb28Y6yw6hIVL-JSgAInKttcUHn_QwTn0Lkjryw==', start_index=8205)
Annotation(end_index=8218, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGV4v-ilS6hYm0ZWc1tYqPGGnyK0ZZIEyGm11ccK2ynysdE85PNrI7NitniEhoiq5ScUk7FLLZ-xzM2HR2_chgrIvX880eLHh8t36DAmZI3NXMOm00q1sVDuu-XaLl_lv1kHH-Ce8uc', start_index=8205)
Annotation(end_index=8453, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5Lb8VR2rTjRdlU8VfImIVd3Z4Lkzm7anRvm30-21wgUDA3ETT16uB09bUnAe0mXYhroXyIVVFfbCpHSArXhvbyz4b-q6-lVYJc7DbgRHhYvqA3g3nd0an1lLU64eH_Gn9feutYW4L', start_index=8440)
Annotation(end_index=8453, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlnxrB0lxR5tpZGpciFXDdNgZ3zTEbaEBVwiEDPuY-T4sFeVuatkqgrLgPAruJyVZlvL3MhqWMkn2UyvXtGwArdraJoS9q00rasifSkMyWPmD6Rs-ApeVZ_w9jbKm423PD858alQs=', start_index=8440)
Annotation(end_index=9157, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFs0Pb059h8b40kaj-krtzjzAkHk4iGI9ppl5NHne0_BG6jAHgklhrOGF-HAtPbnj3ZZgJCcKQyG2EykESka1gIRf170anlQqrZAnpHHeCmff6amAlxP__cpvm_f-iw58_4o128VXA=', start_index=9143)
Annotation(end_index=9157, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYmfemR-M9x-vmuDJ156mJBdHDOkeUhSRgtxCmUV0KjfBqJ1qOvATzIk6UEbtgQPPx8dTpGXMUMWodtyi2ufz4s-j7EACGXW_B5iG5pZTj3xlX0bxY9e8_nbCRUtkub_EJ8Vw6E_o=', start_index=9143)
Annotation(end_index=9454, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGO42APmJnoVhJemXq2LFtm19c2VekDXFkJE6udsGPS5UgXa-GS6hRTHVehVdCq0QG2_0HgXcOmGN1AH2UOPG3aCrSTkcMhtebpScx8M9qh7geoyME6iySLMyrLJBX2MrNBna6TK0NlQQPRxr1GQdu8-PHh', start_index=9442)
Annotation(end_index=9454, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHm78yWDCPRmnU0xjjR7FAc6LYs_XmrA-N8pMY5KpHR0sGWQG25-2_F9CdPvgvZ4CRfRcL3HvEGSK3NDsEriwP8FIgzjHVQZo2kc8fNw-_RVO7kex_P', start_index=9442)
Annotation(end_index=9772, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoGGtls1MkmLzZY3u-t5Zq-88tCsYlrYDwL4N8FVfeUaMk6GPlGZO3OR6J9cTW0fI7KP9QD4VrEBj859lDOn0Y_TcHovRIqTNUA7iU0XVNUmQqCPKytN-PYA376_-1Y1SwWmFF8p8=', start_index=9758)
Annotation(end_index=9772, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGszFLkqrmaEzz6IxdsJYA72NDuKg0mq_KcpHpf1-QiFHjouuI8AbzXULpyfJybCkyLwOEXvutzV1bQI5-LfsaUKWhpNSSMwc-Gg4otxChX2xfvDgzdp9xV4B1l6UBTwLmi2aIIyOUFg7cMcQA0uW09H9wWQ_-RrajWdR8D8Lh3wJDj20hm2G1ySrm_8tXaUCBr5ZuwhSLm4vR18tAGRVbFU28eUJus-iNan6XDVIrOKDs=', start_index=9758)
Annotation(end_index=10277, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDJ1RrsZBh9-FiNWQ5V98VQLa5qWOn3PQmGn6agV93YnjX8ttJhStcDI1W5HidAR1nEgSM7Yum-go2gJeDZz2-3aJoyKuN6YP4BaAOFLZsSiyAS-m7QCMKhOxVR69Km4T37UKV2TYFXt7Ial6d', start_index=10263)
Annotation(end_index=10277, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKdyXuO-PYpuFiA7TMWEH69EYcxMpnhKxvUvaeBFa6pD6xspp6y0ObWvxHT37pdgS0DeoY5cirLkYc9TvVQ8crC7ocWxHqDaW7HWFM0impeM5jLDw_pqO6hec4BV1i66gzaa9T-rg=', start_index=10263)
Annotation(end_index=10564, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPHhSNM6WMOmfPnRGdXiGajadJqeodpd9ot9NHUWlAaKY7shiKex-_DJIrgnnM1SQFkXaPEiV5SOVLhK3FIRT62TUkyqrjrniifETqpK537jcVLJ1yzicMtJg9_30WxqTQtwjVMJI=', start_index=10554)
Annotation(end_index=10983, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXdEuEh-MG1FLp_kieM3rdaY9Epe6dV_7P8LxyOV092XlD5ItjG6HatcKw60kvBqArKH_0xvR7Yrf6_bMlEaH2fMSA53FzI7EKkav8SGLkmn86KQm6r0IeVo4e9n7WPGnwRmhuIf3UHSR9P0TrCwIHRX61F_T_OKssF3h9fT-fdNr1O6AWFzMMjkI=', start_index=10970)
Annotation(end_index=10983, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBxhUJIb4uRdUgnj-H-WQaMQVvBLA8Yo3_QLgTHpXN0S8NqoIFyJvawi1YuXNiwurzRU_jP4-Jc76B_0w0LesA94Ypoq0ZeSxBdAt6iZzHs9xwyWB1U7gJTc0t5rRJGxjLi01Q-NKjtW5K7m0atTb_97RdKYMtU-VT_lOBisqq4wQaGabD8w-PZtdteyooio_BzMGZIfoKYMALjYsvD5Yg9dRCE6rB6vj_Q4qJWLeEYrSt4Vv6XkkptDSDAXRBXso=', start_index=10970)
Annotation(end_index=11296, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoGGtls1MkmLzZY3u-t5Zq-88tCsYlrYDwL4N8FVfeUaMk6GPlGZO3OR6J9cTW0fI7KP9QD4VrEBj859lDOn0Y_TcHovRIqTNUA7iU0XVNUmQqCPKytN-PYA376_-1Y1SwWmFF8p8=', start_index=11286)
Annotation(end_index=12011, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBqL66U9kIwEiFpmJkh-Jm0JU2Sg1_HVGVWdiY-QbygK8bpby0vhR5Cxrmfr3uYSHtygANRB-lX9NK3n0ioJusysjbyFJj_icV-hqHSQYk23l-QRsIR-TP36JVk7hc', start_index=12001)
Annotation(end_index=12384, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBqL66U9kIwEiFpmJkh-Jm0JU2Sg1_HVGVWdiY-QbygK8bpby0vhR5Cxrmfr3uYSHtygANRB-lX9NK3n0ioJusysjbyFJj_icV-hqHSQYk23l-QRsIR-TP36JVk7hc', start_index=12374)
Annotation(end_index=12870, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjEYqEY5Y8KfwcEHChS8dTHFUR8iS02PPFTljxh-3qqrBqQ9gmhQ9D8w9o02kXoUX2hgh-IlIa5hIbrexhyhWfa04CtfXPI494VDHpm1ZYeIr4dbNNWJhga_HjURZ5WKPWwU8V-65TqCbRI6opSQpcE8DN', start_index=12857)
Annotation(end_index=12870, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBxhUJIb4uRdUgnj-H-WQaMQVvBLA8Yo3_QLgTHpXN0S8NqoIFyJvawi1YuXNiwurzRU_jP4-Jc76B_0w0LesA94Ypoq0ZeSxBdAt6iZzHs9xwyWB1U7gJTc0t5rRJGxjLi01Q-NKjtW5K7m0atTb_97RdKYMtU-VT_lOBisqq4wQaGabD8w-PZtdteyooio_BzMGZIfoKYMALjYsvD5Yg9dRCE6rB6vj_Q4qJWLeEYrSt4Vv6XkkptDSDAXRBXso=', start_index=12857)
Annotation(end_index=13101, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBxhUJIb4uRdUgnj-H-WQaMQVvBLA8Yo3_QLgTHpXN0S8NqoIFyJvawi1YuXNiwurzRU_jP4-Jc76B_0w0LesA94Ypoq0ZeSxBdAt6iZzHs9xwyWB1U7gJTc0t5rRJGxjLi01Q-NKjtW5K7m0atTb_97RdKYMtU-VT_lOBisqq4wQaGabD8w-PZtdteyooio_BzMGZIfoKYMALjYsvD5Yg9dRCE6rB6vj_Q4qJWLeEYrSt4Vv6XkkptDSDAXRBXso=', start_index=13091)
Annotation(end_index=13631, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXdEuEh-MG1FLp_kieM3rdaY9Epe6dV_7P8LxyOV092XlD5ItjG6HatcKw60kvBqArKH_0xvR7Yrf6_bMlEaH2fMSA53FzI7EKkav8SGLkmn86KQm6r0IeVo4e9n7WPGnwRmhuIf3UHSR9P0TrCwIHRX61F_T_OKssF3h9fT-fdNr1O6AWFzMMjkI=', start_index=13622)
Annotation(end_index=14095, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4WlGMkD8UxLVki548qhaO4vukkGEoRWMp73ytc4060od7T1SRX0SoI3821twgEbKedttDlKyd1rRQ_gQNvmByL2bS-qmlrybodndDftqrVn8QgANxToVGiWWhPsMvNj7f5HW0jqhYUnLm', start_index=14078)
Annotation(end_index=14095, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5Lb8VR2rTjRdlU8VfImIVd3Z4Lkzm7anRvm30-21wgUDA3ETT16uB09bUnAe0mXYhroXyIVVFfbCpHSArXhvbyz4b-q6-lVYJc7DbgRHhYvqA3g3nd0an1lLU64eH_Gn9feutYW4L', start_index=14078)
Annotation(end_index=14095, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlnxrB0lxR5tpZGpciFXDdNgZ3zTEbaEBVwiEDPuY-T4sFeVuatkqgrLgPAruJyVZlvL3MhqWMkn2UyvXtGwArdraJoS9q00rasifSkMyWPmD6Rs-ApeVZ_w9jbKm423PD858alQs=', start_index=14078)
Annotation(end_index=14624, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7bR9HWu9tIPmD_svYcVkCF92goQ-G9fpEZH1L8RWM3pJsZ_fFwm0MmPXRSBkuntIJdSVBulBETag9QF-1vjKGXDXy87a_4uUZ0z6gq118Akyg06_y', start_index=14607)
Annotation(end_index=14624, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkKy7b71EzpQNb_64BNJeKh8Xe5SvWf_LkGvujVNBEWoCx7ycusjzBOz5omfsvrFp_PCN9RdV_9hX0Cox9HyYChQwacOzLeDCdoqy9ScqKtLPhKyx6gerTLtRWaYkvlSih7ewD8Nr6pgzmVB2rD2lsFNTH04ejKeATGByk9a1JIEscaZyeOBAqQruVyMxtu01Wl4q10JxECw-3ykoA-6R6Ti_BsOfaMAshpGoD6NWBvDa52FOkcLtA17nxlQ==', start_index=14607)
Annotation(end_index=14624, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHVjo5qWybOyD-njhoftlH-UwA-5gkgl-76Gwc8AXI4r2aSpNcE12Gg7-fe0ZRBJnWqt-RHQQc_sAdDoiEeP50N99ZR4BeEYMx2ihzJmp4L42rPgpGovFv', start_index=14607)
Annotation(end_index=14815, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHo9rHWLeOZ_YBR-Gt5ql2TcU6oEKBHnRnfGkXzLBW_aUecm8dA0kUbJqzcn22mwgmCFwi_zRlaUNuORVDlo3kzf6XeA_R7VLLzwUepJKY1LUHRXJHB8tGZt16L_EAwOYpis9E1oUjz', start_index=14805)
Annotation(end_index=15519, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPHhSNM6WMOmfPnRGdXiGajadJqeodpd9ot9NHUWlAaKY7shiKex-_DJIrgnnM1SQFkXaPEiV5SOVLhK3FIRT62TUkyqrjrniifETqpK537jcVLJ1yzicMtJg9_30WxqTQtwjVMJI=', start_index=15498)
Annotation(end_index=15519, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjEhalclfK6R3M0LlLp5H2Izv0A2q9yVX44sH92OGCa5ZOVsHTgHWuUqMi46xMtHdN2jVRuJajGFPdOospTsKk50_Fu6YMSBpcvnkfyqDmRYpLdBSUP5Ta8ADN4oyY1H_JKdnFOYzQtU02kammLFQtlKcbrzk21807b5vfegtIcQbY1XiapUEjjPv7eZkk4u12EYI4Arr-yfABbboKgrHRyLx3Ty1HUDtciuhMQQb6vD2m5TETHwqvj-iBW23RkgSG9A5JJ_0=', start_index=15498)
Annotation(end_index=15519, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGV4v-ilS6hYm0ZWc1tYqPGGnyK0ZZIEyGm11ccK2ynysdE85PNrI7NitniEhoiq5ScUk7FLLZ-xzM2HR2_chgrIvX880eLHh8t36DAmZI3NXMOm00q1sVDuu-XaLl_lv1kHH-Ce8uc', start_index=15498)
Annotation(end_index=15519, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHm78yWDCPRmnU0xjjR7FAc6LYs_XmrA-N8pMY5KpHR0sGWQG25-2_F9CdPvgvZ4CRfRcL3HvEGSK3NDsEriwP8FIgzjHVQZo2kc8fNw-_RVO7kex_P', start_index=15498)
Annotation(end_index=15895, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzisIDhvIEil_sN72M8MKgUcKRjqyFV9i3uv4p3244crx5izTs2EKhr1aTJvJ9TiJspvBfgws8Kx2xtLB6KrRnc23WIV3AO4P7ADbEqFD70vmNVWhj0mvKDN2rTZ3SCEs82RJLltKczoV5unX2-vc5hpJlNNanzWsfOCP1-0zV8kgStIJHlU9NwjMvQtQZoyo6DSp0JDPyhcZ7XNwbL5iI3Nljok6dJ1UMezLXTcvKiht7IjIx-NYIb28Y6yw6hIVL-JSgAInKttcUHn_QwTn0Lkjryw==', start_index=15882)
Annotation(end_index=15895, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIDpj7ng7QrGnheYezkMBc6rOrhyTbj1ztJ0-oWav1giQC_RLiV_NN8pzDMW8qNPAQMoyr6sPBC-twV9Nw3KNCVBZ1xRnY2851ccwXOHrdi4aUDfNYV269thhf6RzyKr_UJnZM', start_index=15882)
Annotation(end_index=16124, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4icaeTwi86ZNLZUGo3bO8wrnzS8Y2Fgp5hurgmyMZZduiNSh30J7sFQjYf1pFStmx3w3WKQFtcjay7MygUT8bAKxRt1j0FHxdr17d1oX0Nv2YhSEXwrpiW3jk0ffXDb3gsISj9ndvXmm3B0w4c38FLxQRew9HEvBJDysg589Js4Mm0U82DeWo417l853STB9JFw-pBNyVhNFYm2RMwlB48OWLzL2-KoNnQfZ5SJVG9KMRs3wuL4jVDTXOV2F47xgVmQp-mcY66TRmqybcmJ-SWYfBPt6QLh5UFaab2YpJO_7J8_zYbzTUZMMl1PZ4', start_index=16115)
Annotation(end_index=16667, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEF-vko3Kawnyk027AblEC5jBrIsC7YgRO3wBVXl5hE8uL1xjsWEZeQNa5yqyt38cFeWUOJtCmsN3fP-oiQg-1BHUWLZz51OhU0kZcBKPYOHooTkaFkYfKIM03GiuJeSjBVym94Y0yJtN-Fbk_XtlVF6dT0TEyn2Wbg2lb6crVmQOZMC6ZH5h4z-FAYJHukADfthiOJAwtahL7JG-tHAKXC64sL1yZgag0W_MqmqwaVkc1b3oq-yxj3uSoZnM7URUCwdIn__AuOu83q-yE=', start_index=16654)
Annotation(end_index=16667, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHVjo5qWybOyD-njhoftlH-UwA-5gkgl-76Gwc8AXI4r2aSpNcE12Gg7-fe0ZRBJnWqt-RHQQc_sAdDoiEeP50N99ZR4BeEYMx2ihzJmp4L42rPgpGovFv', start_index=16654)
Annotation(end_index=16874, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7bR9HWu9tIPmD_svYcVkCF92goQ-G9fpEZH1L8RWM3pJsZ_fFwm0MmPXRSBkuntIJdSVBulBETag9QF-1vjKGXDXy87a_4uUZ0z6gq118Akyg06_y', start_index=16860)
Annotation(end_index=16874, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkKy7b71EzpQNb_64BNJeKh8Xe5SvWf_LkGvujVNBEWoCx7ycusjzBOz5omfsvrFp_PCN9RdV_9hX0Cox9HyYChQwacOzLeDCdoqy9ScqKtLPhKyx6gerTLtRWaYkvlSih7ewD8Nr6pgzmVB2rD2lsFNTH04ejKeATGByk9a1JIEscaZyeOBAqQruVyMxtu01Wl4q10JxECw-3ykoA-6R6Ti_BsOfaMAshpGoD6NWBvDa52FOkcLtA17nxlQ==', start_index=16860)
Annotation(end_index=18534, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5HSyVi7o_ZpYFghACFV6BZwQdx7PSZwcLmvyh4eBgx1kSpz34HuKVSOWiYeAWTkEYo8a514YnEh-rqvsC86BDwDIzcoctcUIf8t37NfGOtMKgXGpF', start_index=18520)
Annotation(end_index=18534, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGx2HegxLDnXFHevPpVKnG0AKLGQP-dGU7FqAYbHsje10_J3r1DqMgPT7u1GKtJlY-MjkeVWcQuk3bdXv5MyujLyCuYHB_SjKOK7g2FqARcNpgFGiGbNrPbUG_HjldZqk7Pohe6TjRVO_5g6X9tTtdjEOHTjTQe', start_index=18520)
Annotation(end_index=18914, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYmfemR-M9x-vmuDJ156mJBdHDOkeUhSRgtxCmUV0KjfBqJ1qOvATzIk6UEbtgQPPx8dTpGXMUMWodtyi2ufz4s-j7EACGXW_B5iG5pZTj3xlX0bxY9e8_nbCRUtkub_EJ8Vw6E_o=', start_index=18904)
Annotation(end_index=19310, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7cJOKxRq2DFyVWP43Psk-3x000ztixlfigvS59KQ8luxxJRzGEGw1u2axno9bZjvAuKVDh4MrIOwk9FUZI9UfP7PqIq9cnscrvyi-f2ksZnhEQAx-AODSwOkwQRyJsWQ_Ag==', start_index=19300)
Annotation(end_index=19666, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBxhUJIb4uRdUgnj-H-WQaMQVvBLA8Yo3_QLgTHpXN0S8NqoIFyJvawi1YuXNiwurzRU_jP4-Jc76B_0w0LesA94Ypoq0ZeSxBdAt6iZzHs9xwyWB1U7gJTc0t5rRJGxjLi01Q-NKjtW5K7m0atTb_97RdKYMtU-VT_lOBisqq4wQaGabD8w-PZtdteyooio_BzMGZIfoKYMALjYsvD5Yg9dRCE6rB6vj_Q4qJWLeEYrSt4Vv6XkkptDSDAXRBXso=', start_index=19656)
Annotation(end_index=20029, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3979HZFJIB7IybvOz8TM2bPz2a4z8n12BmDKkxoMwKqI0H-vaubYBwg8I1v2kcJP3gNmAyGgGJtOfKNqYCaqycVyuOLaa6-c888So9LYONPm3oKSlrpm7aRlwSg==', start_index=20019)
Annotation(end_index=20385, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjEYqEY5Y8KfwcEHChS8dTHFUR8iS02PPFTljxh-3qqrBqQ9gmhQ9D8w9o02kXoUX2hgh-IlIa5hIbrexhyhWfa04CtfXPI494VDHpm1ZYeIr4dbNNWJhga_HjURZ5WKPWwU8V-65TqCbRI6opSQpcE8DN', start_index=20376)
Annotation(end_index=20937, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7bR9HWu9tIPmD_svYcVkCF92goQ-G9fpEZH1L8RWM3pJsZ_fFwm0MmPXRSBkuntIJdSVBulBETag9QF-1vjKGXDXy87a_4uUZ0z6gq118Akyg06_y', start_index=20924)
Annotation(end_index=20937, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHVjo5qWybOyD-njhoftlH-UwA-5gkgl-76Gwc8AXI4r2aSpNcE12Gg7-fe0ZRBJnWqt-RHQQc_sAdDoiEeP50N99ZR4BeEYMx2ihzJmp4L42rPgpGovFv', start_index=20924)

## Sources
