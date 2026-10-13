# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 002650a6 | **Time:** 331.09s | **Cost:** $1.49648
--------------------------------------------------------------------------------

# Optimizing Strain Sensing Sensitivity and Linearity in Flexible Substrates for Wearable Biomedical Monitoring

### Key Points
*   **The Core Challenge:** Flexible strain sensors often suffer from a trade-off between high sensitivity (Gauge Factor) and linearity. Material deformation typically induces nonlinear conductivity changes due to percolation threshold effects, viscoelastic hysteresis of polymer substrates, and uncontrolled crack propagation.
*   **Structural Solutions:** Engineering geometric structures such as **kirigami cuts**, **gradient architectures**, and **bio-inspired wrinkles** can mechanically linearize the sensor response. These designs convert large global strains into smaller, controlled local deformations, maintaining the active material within its linear conductive regime.
*   **Material Strategies:** **Hybrid filler networks** (combining 1D nanotubes/nanowires with 2D graphene/MXene) and **interfacial engineering** (e.g., dopamine treatment) create "stepwise" disconnection mechanisms. This prevents sudden conductivity losses, smoothing the resistance-strain curve into a linear response.
*   **Electronic Compensation:** For sensor arrays, **Active Matrix (AM)** readouts using thin-film transistors (TFTs) are essential to eliminate crosstalk and maintain signal linearity across high-density pixels, a critical requirement for precise biomedical mapping like pulse wave monitoring.

### Introduction
The rapid proliferation of wearable biomedical devices has necessitated the development of flexible strain sensors capable of detecting physiological signals ranging from subtle arterial pulses (0.1% strain) to large joint movements (>50% strain). However, a persistent bottleneck in this field is the inherent nonlinearity between material deformation and conductivity changes. Most flexible sensors rely on the piezoresistive effect in conductive polymer composites (CPCs) or crack-based mechanisms. While these mechanisms can yield ultra-high gauge factors (GF), they frequently exhibit severe nonlinearity, hysteresis, and signal drift due to the viscoelastic nature of elastomeric substrates (e.g., PDMS, Ecoflex) and the stochastic breakdown of conductive networks [cite: 1, 2].

Optimizing sensitivity while enforcing linearity requires a multi-scale approach. At the micro-scale, interfacial interactions between conductive fillers and substrates must be strengthened to reduce slippage and hysteresis. At the meso-scale, hybrid conductive networks can be designed to bridge micro-cracks, ensuring a gradual, linear resistance change. At the macro-scale, structural engineering techniques like kirigami and gradient patterning redistribute stress, allowing sensors to operate linearly over broad strain ranges. This report provides an exhaustive analysis of these optimization strategies, synthesizing recent advancements in materials science, structural mechanics, and electronic readout schemes.

---

## 1. Material-Level Optimization Strategies

The fundamental transduction mechanism in resistive flexible sensors is the alteration of conductive pathways within a polymer matrix. Optimization at the material level focuses on stabilizing these pathways to ensure that resistance changes are proportional to applied strain.

### 1.1 Hybrid Filler Networks and Synergistic Percolation
Single-component conductive fillers, such as carbon nanotubes (CNTs) or graphene, often face limitations. CNTs can slide and bundle, leading to hysteresis, while graphene sheets can fracture abruptly, causing nonlinear signal spikes. Hybridizing 1D and 2D materials creates a synergistic network that enhances both linearity and sensitivity.

*   **1D-2D Bridging Mechanisms:** Combining 1D fillers (e.g., silver nanowires (AgNWs) or CNTs) with 2D fillers (e.g., graphene or MXene) creates a robust "bridge-and-island" structure. When the substrate stretches, the 2D islands may separate, but the 1D fillers bridge the gaps, maintaining electrical continuity. This prevents the abrupt resistance jumps characteristic of crack-based sensors, resulting in a smoother, more linear response [cite: 3, 4].
*   **Double-Layer Coating:** A specific optimization strategy involves layer-by-layer assembly. Research has demonstrated that a double-layer coating—specifically a first layer of carboxylated single-walled CNTs (SWCNTs) followed by a second layer of hydroxylated multi-walled CNTs (MWCNTs)—can significantly improve performance. The carboxylated layer enhances adhesion to the substrate, while the hydroxylated layer fills voids, creating a uniform network. This configuration has achieved a linearity of $R^2 = 0.997$ and a GF of 60, effectively overcoming the "J-shaped" nonlinear response often seen in single-layer coatings [cite: 3].

### 1.2 Interfacial Engineering and Adhesion Enhancement
The viscoelasticity of polymer substrates (e.g., PDMS, TPU) contributes significantly to hysteresis, a form of nonlinear error where the sensor's output depends on its loading history. Weak adhesion between the active material and the substrate exacerbates this by allowing interfacial sliding.

*   **Dopamine Treatment:** Polydopamine (PDA) is a bio-inspired adhesive that can be polymerized on hydrophobic substrates like Ecoflex or PDMS to introduce hydrophilic functional groups. This treatment significantly enhances the bonding force between the substrate and conductive fillers (like CNTs). Stronger interfacial bonding reduces the sliding of fillers during stretching cycles, thereby minimizing hysteresis and improving the linearity of the electromechanical response [cite: 3].
*   **Surface Modification:** Other surface treatments, such as ultraviolet ozone (UVO) irradiation, modify the surface energy of substrates to promote better wetting and adhesion of conductive inks. This is crucial for preventing delamination during the large deformations associated with joint monitoring [cite: 5].

### 1.3 Substrate Selection and Viscoelastic Control
The choice of substrate dictates the mechanical baseline of the sensor. While silicones like PDMS are popular, their viscoelastic relaxation can cause signal drift.
*   **Pre-straining Strategies:** Applying a pre-strain to the substrate before depositing the conductive layer is a potent technique for linearization. When the substrate is released, the conductive layer buckles or overlaps. Upon subsequent stretching, these structures unfold (a geometric change) rather than fracturing (a material change). This "unfolding" mechanism is inherently more linear and reversible than crack propagation. For instance, applying CNT powder to an acrylic elastomer pre-strained to 47% resulted in a sensor with a constant GF of 1.46 and strong linearity up to 100% strain [cite: 6].

---

## 2. Structural Engineering for Linearization

When material properties alone cannot achieve the desired linearity, geometric structuring of the sensor element offers a powerful alternative. These methods control how strain is distributed across the sensing material.

### 2.1 Controlled Crack Propagation
Crack-based sensors are known for ultra-high sensitivity (GF > 2000) but notoriously poor linearity and repeatability. The resistance in these sensors changes exponentially as cracks open. "Stepwise" crack propagation is a novel strategy to linearize this response.

*   **Bilayer Architectures:** A sophisticated design involves a bilayer structure comprising an aligned CNT array on top of a periodically wrinkled and cracked CNT-graphene oxide (GO) film. The transversely aligned CNTs in the top layer act as bridges over the microcracks in the bottom layer. As strain increases, these bridges limit the rapid opening of cracks, forcing the resistance to change in a stepwise, controlled manner rather than exponentially. This mechanism has demonstrated extraordinary linearity ($R^2 \approx 0.99$) up to 100% strain with a high gauge factor of ~287 [cite: 4].
*   **Brittle Layer Tuned Propagation:** Introducing a brittle intermediate layer between the substrate and the conductive film can guide crack formation. By pre-crazing this brittle layer, a dense network of uniform microcracks is formed. During stretching, these microcracks open uniformly, avoiding the catastrophic propagation of large cracks and yielding a highly linear response ($R^2 \approx 0.97$) [cite: 7].

### 2.2 Kirigami and Serpentine Structures
Kirigami, the art of paper cutting, allows rigid or semi-rigid materials to stretch by rotating and buckling out of plane. This geometric transformation dominates the global strain response, shielding the local material from excessive deformation.

*   **Stress Redistribution:** By patterning conductive films (e.g., AgNWs/Ecoflex) with kirigami cuts, the tensile strain applied to the sensor is converted into the rotation of the cut segments. This ensures that the local strain on the conductive network remains low and within the linear elastic region, even when the overall device is stretched significantly (e.g., up to 70%). This approach has yielded sensors with excellent linearity ($R^2 = 0.99$) and no obvious hysteresis, making them ideal for monitoring complex joint movements without signal distortion [cite: 8].
*   **Piezoelectric Kirigami:** For piezoelectric sensors (e.g., PVDF), kirigami cuts can enhance stretchability by over 300%. The structural distortion allows the sensor to operate in a linear voltage-strain region over a much wider range than a continuous film, which would saturate or fracture [cite: 9, 10].

### 2.3 Gradient Structures
Biological tissues often exhibit gradient structures (e.g., from soft cartilage to hard bone) to manage stress. Mimicking this in sensors can optimize the sensitivity-stretchability trade-off.

*   **Gradient CNT Density:** A sensor with a gradient in CNT alignment and density can combine the benefits of random networks (high sensitivity) and aligned networks (high stretchability). In such a design, the randomly oriented regions provide the initial resistance change (sensitivity), while the aligned regions maintain connectivity at high strains. This architecture has achieved a GF of 13.5 with ultra-stretchability (>550%) and extraordinary linearity, capable of detecting high-frequency (8 Hz) signals without loss [cite: 11, 12].

---

## 3. Electronic and Circuit-Level Optimization

Even with optimized materials and structures, intrinsic nonlinearities may persist. Electronic readout strategies are the final line of defense to ensure data fidelity, particularly in sensor arrays.

### 3.1 Active Matrix (AM) Readout for Arrays
In wearable monitoring, arrays of sensors are often used to map pressure or strain (e.g., pulse wave mapping). Passive matrix arrays suffer from "crosstalk," where the signal from one pixel leaks into neighbors, causing nonlinearity and ghosting artifacts.

*   **Thin-Film Transistor (TFT) Isolation:** Active Matrix technology places a transistor (TFT) at each pixel to switch it on and off. This isolates the pixel during readout, eliminating crosstalk. Recent advancements have integrated flexible TFTs (using carbon nanotubes, metal oxides, or organic semiconductors) with pressure-sensitive rubber. This configuration ensures that the readout remains linear and accurate even in high-density arrays (e.g., 4096 pixels/cm²), which is critical for spatially resolving the arterial pulse wave [cite: 13, 14, 15].
*   **Crosstalk Elimination:** By preventing current leakage through parallel paths, AM arrays ensure that the measured resistance change is linearly proportional to the local strain/pressure, independent of the state of surrounding pixels [cite: 16].

### 3.2 Analog Linearization Circuits
For individual sensors, analog front-end circuits can compensate for resistive nonlinearity.
*   **Variable Excitation:** Standard Wheatstone bridges can be nonlinear for large resistance changes. Advanced interface circuits (e.g., using chips like the XTR105 or PGA309) employ variable excitation techniques or feedback loops to linearize the output voltage with respect to the changing sensor resistance. This is particularly useful for sensors with "downward bowing" nonlinearity [cite: 17].
*   **Feedback Topologies:** In respiration monitoring, where the baseline offset can drift significantly, feedback topologies using voltage-controlled resistors (VCRs) or digital potentiometers can dynamically balance the bridge, keeping the sensor in its linear operating point [cite: 18].

---

## 4. Case Studies in Biomedical Applications

The optimization strategies discussed above are directly applicable to specific biomedical monitoring challenges.

### 4.1 Arterial Pulse Wave Monitoring
Pulse monitoring requires high sensitivity to detect minute skin deformations (micrometer scale) and high linearity to accurately reproduce the pulse waveform (P-wave, percussion wave, dicrotic notch) for blood pressure estimation.
*   **Soft-Strain Effect:** A sensor utilizing the "soft-strain effect" in a microstructured contact design achieved an ultra-high sensitivity of ~636 kPa⁻¹ and a wide linear range. This allowed for the precise capture of arterial pulse waves from deep tissues (e.g., dorsal pedal arteries), enabling cuffless blood pressure estimation via pulse transit time [cite: 19, 20].
*   **Interference Rejection:** The linearity provided by AM arrays allows these sensors to distinguish the pulse signal from artifacts caused by wrist movement or skin stretching [cite: 21].

### 4.2 Respiration and Motion Monitoring
Respiration involves moderate strains, while joint motion involves large strains. A single sensor must often handle both regimes linearly.
*   **Nanocomposite Performance:** A screen-printed rGO/Pd sensor demonstrated a GF of 1523 at 45% strain with a response time of 47 ms. Its high linearity allowed for the real-time differentiation between normal breathing and deep breathing patterns, as well as the detection of abrupt motions like coughing [cite: 1].
*   **Vertical Graphene (VG):** To overcome the durability limits of crack-based sensors, vertical graphene grown on PDMS offers a non-cracking alternative. The vertical orientation allows the graphene sheets to bend and recover without fracturing, resulting in a sensor with high sensitivity (GF > 5000), remarkable durability (>10,000 cycles), and completely reversible behavior (no hysteresis), ideal for long-term motion tracking [cite: 22].

---

## 5. Conclusion

Optimizing the strain sensing sensitivity of flexible substrates while mitigating nonlinear responses requires a convergence of material science and structural mechanics. **Material-level strategies** like hybrid 1D-2D filler networks and dopamine-assisted interfacial bonding address the root causes of hysteresis and stochastic breakdown. **Structural strategies** such as kirigami cuts, gradient architectures, and controlled stepwise crack propagation provide geometric solutions that linearize the global response of the device. Finally, **electronic strategies** like Active Matrix readout ensure that these optimized signals are acquired with high fidelity, free from crosstalk.

For future wearable biomedical devices, the most promising direction appears to be the integration of **gradient-structured nanocomposites** within **Active Matrix arrays**. This combination offers the high sensitivity needed for pulse detection, the large linear range required for motion tracking, and the signal integrity essential for clinical-grade diagnostics.

### Summary of Optimization Techniques

| Strategy | Mechanism | Key Benefit | Target Application |
| :--- | :--- | :--- | :--- |
| **Hybrid Fillers (1D+2D)** | 1D fillers bridge gaps between 2D islands during stretch. | Prevents abrupt disconnects; smooths response. | Large-strain motion (Joints). |
| **Dopamine Treatment** | Enhances substrate-filler adhesion. | Reduces interfacial sliding and hysteresis. | Dynamic monitoring (Respiration). |
| **Stepwise Crack Propagation** | Bilayer design controls crack opening speed. | Linearizes response of high-GF crack sensors. | High-sensitivity pulse detection. |
| **Kirigami/Cuts** | Converts stretch to rotation/unfolding. | Keeps local strain in linear elastic regime. | Ultra-stretchable e-skin. |
| **Active Matrix (AM)** | TFT at each pixel isolates signal. | Eliminates crosstalk in arrays; improves linearity. | Spatially resolved pulse mapping. |
| **Gradient Structure** | Varies density/alignment of fillers. | Balances sensitivity (sparse) and stretchability (dense). | Multi-functional sensing. |

**Sources:**
1. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLAGNU2CsYRplIo4WINwdVb0pGK_kneIOJzTujB6BIXk8bM8S0dw0DUQpDgp1pN9Q1_rduoImL-6GY9L45pxuAn6cN4t1y2k7HndczMpL0TYa1kknYghEGx2eIWkPQ)
2. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8yqmCmq0ZDx-eY_BP07I3w2hUf0xnhQVuYa5UctZpzSHwEq6g58V0M-pzPWA9EYZxo_SUaWbOaatWr3Jv9NMSP4I9hTs8x1rWhDPVmTvO-DkeExIcPOYpfDbaByT_)
3. [cas.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR7zbcpLkUD9JjinueQaU-cqzkybDMT55l8prKL6EIjCkMTfiXClCTHh1TjCHUn3Eo-uMZn4FdLB5NTvxV8VANdGPwCLYnhqghFaBXCIyKl4N7IJS9RMeY318s30TuXja_ELbn2WOtyudCNFMZ553BW2GSAM7kX7zwoU_q_KA1VUsZwgu2BZeL)
4. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmUv-VAf5P2qijDggrmgf54eSJhzxMu_7_BKrYa1t99hifQYM7ytRJYOu4nWWLikNFl6qGZUe_aD8qoOv8z9qaQCmv1ojC2u2s8tiMpdLoGo-bu5m0mjKB-g_nhjWIfIrgXwifnYg=)
5. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWBCuBImV3NiNMrXCtbh5z1wpT-_tkFJxR8A6R2ShRafqR9ZA1BrpdTrnm2g0gATHHaloLflxVNd2pfkhdbIA2ALsa6qtWSEQLfUGnwdtGhXQsZ-D-dZ_hR77SSA==)
6. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELF1jrmHq3lCnduuan8M3i1ohBzt8tw-sWuOemZq56JtAFgoocsXWSNvsDjgzlGxr2zipTDRL74c96UPCxUX_RY_8VN7amAfHYP1V6fFWTMMvHuEkGd6resnoMTOtbiB5yjQNguXiGyHzJ4BLx4ox1muzNZpKbMh6XAlA-glYXESJx3FEAL_7N57z3I58nUUw286ZMB_E_422qJuu2dfJgH572s0fG1HFGf1ZnXSJdezBPdfbOrcLYRZlTMeTY32X86LBj9pZwUtxndWTx1hlIgURGNrsph3nL)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVeiooZYAQdDdB0wo0Z_9hAnsDUVTFO7s-Kpr22tOpvUxxvSg6rOToK0oi2tbMFcke2KeJLsIJueF6Vhv4xrorXoThtfHB6v5IO3f2HnsUeBqr6R-uO7X2jPZTvJZG_DWUKWqkn2HSplGv4-u5Y4Sk8Ra1LB9CSrRuJOlhuQ1PfNU1yTKBeLRvVn2dP1EmIMzJAWuyzgJdnC3zX5A4QM7WUrlAh78NMNWP5fq_wyPZDOF1fWwB84XgfsiElFVIIMlWIms=)
8. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmV5EsacYtbX5HW0_H6brvEcC26pgmD5Y_OuAXGDoBmB-w-BsGAY4BMQNwHj7FD_XpAS9bUTuTrijr4U0qhoS1dCJ4rx-6l13u6A-jeIj-52U-Pjw1GToDNsGK)
9. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJ-VxpT_CJ1f7NzRwJItvTWaiOaTmMCFG1qljS3nXdlR5F20PD9_LVE357waxqO689nlflvL_xpivUmIyy3_Il-RWr-iZ3j2vSDCz4W0ujqROiz0USMiwMEkUfjgiqZT09mEqTIi4OMi-p_VTsmP2L8Qq3_GpCC2IpkTncnH_FbgZ8Zu1xOWz2_9YTseyq27_RjqNUX5iZEzUp6Qr9PCptV7u4hUndbdL2hoKaCGSQZwXgdR0JSIiAkbHWgz0MHBJeQhmkHRW042mUBJOsTk6A9vS_)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3WLpI4JJNgoCKKQSnRLfvwimcB8UGPUY9MZv0AnnYTD40evdoZ3c1auO5NgqST7DjH0EHuecley8rc9b0ns6YdoQ_IqyOiL2UulCAqyqTmwAkkgDZwG6SopsyTJq7hrw9j-1ccFPkhdGDybqZQjwQrDQvfMqeuZCisUDRQzY_OttUG-3N_k_ua5Lf7ZGOxMjSC0a_RHqWmwCKy26ho7a_xolZnkTOAX5kwe4cKzk=)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGR4u2yPRz5Zhyt9av_PaXRsf_U2FHpT2zRYoT2ThaLRQ6w8ROJpIA9a-bxZdCaIoybIxh7mhuowIQrtvQtaF3Ym2ieRef-mp2zW0q-tMuomJzlB8Dv512OBdPvSL8bhlQKW6dhK4jSF27f-iLbanyhkYjE_jNnBvQkvODXdKXYwzNEyqNiqGdwmzfFu18W7ppL_1zY-Ft2RzslAN2VsiQlaRfhQt-RR_dajwGsn3MVltFW9cAPIrx-pRRx-ZI9mllqEiHyNhpolEjw)
12. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuD9m049Xa3-YmxRzffRSB0adh5RI8ExgM8mDM7zhNUzwtjMVsRPOayc2dfBNF8irxhx4Y2zJiUrDoEh_53RwA3sHHQFMOZcanpb5CGz3zv0fMX6dl9lcfhySoDeOPWMvuV3Ua0_Rkyom7LMstCCP4mYLwAWQL)
13. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEklf8yHrlvdIc-3oSy8_CP3mhIArxdd7p3s-E51V6eeb11A_2NSBIrrUQeFeVcwbhZzIhK_bH2R11lECjPpkumdbcqm9JxVDqURBtZsPr4VMxp1aweiKCR3F8tW9af6AkIXoo1Z7jjH_L_gkMgvlb7FHLkcr52b8Wze133Oxk4wOBGa7_Ywglvwh2RbOKj3mS1NfFr4lHoltchQ7omflBW31v-Ns9sKAihekW43uJUTDWQBPtpvmIV771RkoA4PIAdoE62eZycEhJkeQQyAO3nqwTdr8B7pNGNUN8bCjwfw==)
14. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjvlOVsH553Wp4WZ4YZbacSNkqhTS-qpkbKWIOj2fCWr4lxsXNqI_TjpEDifCJADzTAGNnlJrc8PqGMLhJ6YZQ8QzfFaA_f-mzEC5_ESX8age_zUwg8-xJ4XYoz-LSdt7Htfw1gwl6bbq4ftfCVw5LDQEWFFqQ3fcj8uC8MZf80zYE9kqkgug-M1qRyV3AZnOy2xqLaSC_6I-bELuP81FE4Z3F6RtD7HSS52vBOLQfEiMgbP3Nhw1s)
15. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0_KMCI1C2-sBflcBfM3h2xeP1HfmvJqw2GOSj6145G6HBIG5am2FCKea6FPeqNrOoe60aMc9Q1KdQGAIbvYHHeWro-DUr77FbydhGV0-5Vuugqk87KhG6Qa-OpA==)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlxWeKDEAkTbDNixM2WHBxecH6c0v96oQ9cNqFkOF4L-q_905VAX9cFZtQDnulpG41LwIqjho0AP41CwWYWo4UKJ7fDKE1M3QrTS6YPgcnaOFWhg6D8jO0wa4s5BIDs6z_G3wpNgbXLnX14aPpQGB6subcNNw4iDmJ48MHj-gnLNIyEFByamEbNF5Ozen2fC6H5KsYe1X6eSa8Q6_yPgfCOuNjNtkw1O42uNTTRrWCwj4XgFMMZMnzsh_nAIMsLQc-lsZ2Qd6qFi4=)
17. [ti.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPg3A6N_l7lW2BSmuFEehs-1MwjfRkJSfesu13eq8-4WmNg_YhMK3OqePmtR8q1YOQz0DWNyDa_Ldc7dQ1zVoBtqPCpsGL4pCKiB2wFowpotBqyhtdqIY=)
18. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZKolj6sRJw354VKy3m1-GZ1IWT9ie6dKR7pkczHSQMmt6IUZOObfNSMHOUbb-SgemhUEPWYZ8I8tsYb8Z06q6pZNGGku9rRIxjSdXT5KlOEA4g9okOtzpaetZJr89)
19. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4xTG42QW-KhPDE2mmM8jeAJGtq8zBNq4ZPbDSTdnz6db8_eEYBQpcnpscLMm_8wKOef6jFD_BgVKqg76IgeGLsk7AoPBGkI6-r-ypCKNCsWaEJAo3hyBCPkuNBE4RiIrJhmdhpEva)
20. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEeWnDAL-lJ4rDpb1kJlGq5XMwDJ1XaSUP_SVyaaCWKL6uOyHQqirVZM9SMdDlkVPAa93dIUhxbg_as9yk7oNGL6NiiwGQvxuY5Stb2sbJ7cqODP-6-o8MhS_GARQyZccRqla3L7LM-sW-78a2zhy_H39tR0xwd0n6rudSUagxXY92OjY7wzpggZ8Zb9bE7kSH7dQ8fCKATd_tbgkZtiCdO2FtO9Y--ixuc5LznqhK9oOC0HjOOHv50M--twHv_CnyEQecu52dYTiquGXhXxgFgbPvR7jQ-KBdONuqV6Ytv)
21. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHwIp6SUGtL7QuS7YNRj35lESHYrFuJcxTTGPAvQxv3LZmw9Xk7P2IPCi_Rwvo_F-hUztNuoDErz7pm-kMzqwkbJmuEQ_rBELkSJvQq0uHXJ7NmfWJC7cAmZksrveamyr7YLKfAmu4bHOqSmjx9uSwGPjc)
22. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSKD1iQI37_aoV2UnOCWuwpnK9CCekK-MDQfZ8wia10EXV2temS3eqNcxvG1JkHSiai_GdNXi8skHVovnMWD6p83gwva-TFLtSLiyAmkA6ZSyeDtUYmcQrHcMm_JFYtn5hXn2O9A4VYAtOiZ3ynwSy7GkALoVfjRgGyzpTkT0oPfmch3laKZylvK1sKrq3UGrntgmD1lB4HSNWyVLmP3fareNmC0A21RUEoR7pwGrBZXKebZRTvpsuuMZQpblm5QKHRqa9Xch9DbrA)


## Annotations
Annotation(end_index=2227, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8yqmCmq0ZDx-eY_BP07I3w2hUf0xnhQVuYa5UctZpzSHwEq6g58V0M-pzPWA9EYZxo_SUaWbOaatWr3Jv9NMSP4I9hTs8x1rWhDPVmTvO-DkeExIcPOYpfDbaByT_', start_index=2215)
Annotation(end_index=2227, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLAGNU2CsYRplIo4WINwdVb0pGK_kneIOJzTujB6BIXk8bM8S0dw0DUQpDgp1pN9Q1_rduoImL-6GY9L45pxuAn6cN4t1y2k7HndczMpL0TYa1kknYghEGx2eIWkPQ', start_index=2215)
Annotation(end_index=4139, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmUv-VAf5P2qijDggrmgf54eSJhzxMu_7_BKrYa1t99hifQYM7ytRJYOu4nWWLikNFl6qGZUe_aD8qoOv8z9qaQCmv1ojC2u2s8tiMpdLoGo-bu5m0mjKB-g_nhjWIfIrgXwifnYg=', start_index=4127)
Annotation(end_index=4139, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR7zbcpLkUD9JjinueQaU-cqzkybDMT55l8prKL6EIjCkMTfiXClCTHh1TjCHUn3Eo-uMZn4FdLB5NTvxV8VANdGPwCLYnhqghFaBXCIyKl4N7IJS9RMeY318s30TuXja_ELbn2WOtyudCNFMZ553BW2GSAM7kX7zwoU_q_KA1VUsZwgu2BZeL', start_index=4127)
Annotation(end_index=4784, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR7zbcpLkUD9JjinueQaU-cqzkybDMT55l8prKL6EIjCkMTfiXClCTHh1TjCHUn3Eo-uMZn4FdLB5NTvxV8VANdGPwCLYnhqghFaBXCIyKl4N7IJS9RMeY318s30TuXja_ELbn2WOtyudCNFMZ553BW2GSAM7kX7zwoU_q_KA1VUsZwgu2BZeL', start_index=4775)
Annotation(end_index=5630, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR7zbcpLkUD9JjinueQaU-cqzkybDMT55l8prKL6EIjCkMTfiXClCTHh1TjCHUn3Eo-uMZn4FdLB5NTvxV8VANdGPwCLYnhqghFaBXCIyKl4N7IJS9RMeY318s30TuXja_ELbn2WOtyudCNFMZ553BW2GSAM7kX7zwoU_q_KA1VUsZwgu2BZeL', start_index=5621)
Annotation(end_index=5948, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWBCuBImV3NiNMrXCtbh5z1wpT-_tkFJxR8A6R2ShRafqR9ZA1BrpdTrnm2g0gATHHaloLflxVNd2pfkhdbIA2ALsa6qtWSEQLfUGnwdtGhXQsZ-D-dZ_hR77SSA==', start_index=5939)
Annotation(end_index=6779, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELF1jrmHq3lCnduuan8M3i1ohBzt8tw-sWuOemZq56JtAFgoocsXWSNvsDjgzlGxr2zipTDRL74c96UPCxUX_RY_8VN7amAfHYP1V6fFWTMMvHuEkGd6resnoMTOtbiB5yjQNguXiGyHzJ4BLx4ox1muzNZpKbMh6XAlA-glYXESJx3FEAL_7N57z3I58nUUw286ZMB_E_422qJuu2dfJgH572s0fG1HFGf1ZnXSJdezBPdfbOrcLYRZlTMeTY32X86LBj9pZwUtxndWTx1hlIgURGNrsph3nL', start_index=6770)
Annotation(end_index=7956, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmUv-VAf5P2qijDggrmgf54eSJhzxMu_7_BKrYa1t99hifQYM7ytRJYOu4nWWLikNFl6qGZUe_aD8qoOv8z9qaQCmv1ojC2u2s8tiMpdLoGo-bu5m0mjKB-g_nhjWIfIrgXwifnYg=', start_index=7947)
Annotation(end_index=8373, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVeiooZYAQdDdB0wo0Z_9hAnsDUVTFO7s-Kpr22tOpvUxxvSg6rOToK0oi2tbMFcke2KeJLsIJueF6Vhv4xrorXoThtfHB6v5IO3f2HnsUeBqr6R-uO7X2jPZTvJZG_DWUKWqkn2HSplGv4-u5Y4Sk8Ra1LB9CSrRuJOlhuQ1PfNU1yTKBeLRvVn2dP1EmIMzJAWuyzgJdnC3zX5A4QM7WUrlAh78NMNWP5fq_wyPZDOF1fWwB84XgfsiElFVIIMlWIms=', start_index=8364)
Annotation(end_index=9244, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmV5EsacYtbX5HW0_H6brvEcC26pgmD5Y_OuAXGDoBmB-w-BsGAY4BMQNwHj7FD_XpAS9bUTuTrijr4U0qhoS1dCJ4rx-6l13u6A-jeIj-52U-Pjw1GToDNsGK', start_index=9235)
Annotation(end_index=9556, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJ-VxpT_CJ1f7NzRwJItvTWaiOaTmMCFG1qljS3nXdlR5F20PD9_LVE357waxqO689nlflvL_xpivUmIyy3_Il-RWr-iZ3j2vSDCz4W0ujqROiz0USMiwMEkUfjgiqZT09mEqTIi4OMi-p_VTsmP2L8Qq3_GpCC2IpkTncnH_FbgZ8Zu1xOWz2_9YTseyq27_RjqNUX5iZEzUp6Qr9PCptV7u4hUndbdL2hoKaCGSQZwXgdR0JSIiAkbHWgz0MHBJeQhmkHRW042mUBJOsTk6A9vS_', start_index=9543)
Annotation(end_index=9556, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3WLpI4JJNgoCKKQSnRLfvwimcB8UGPUY9MZv0AnnYTD40evdoZ3c1auO5NgqST7DjH0EHuecley8rc9b0ns6YdoQ_IqyOiL2UulCAqyqTmwAkkgDZwG6SopsyTJq7hrw9j-1ccFPkhdGDybqZQjwQrDQvfMqeuZCisUDRQzY_OttUG-3N_k_ua5Lf7ZGOxMjSC0a_RHqWmwCKy26ho7a_xolZnkTOAX5kwe4cKzk=', start_index=9543)
Annotation(end_index=10323, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuD9m049Xa3-YmxRzffRSB0adh5RI8ExgM8mDM7zhNUzwtjMVsRPOayc2dfBNF8irxhx4Y2zJiUrDoEh_53RwA3sHHQFMOZcanpb5CGz3zv0fMX6dl9lcfhySoDeOPWMvuV3Ua0_Rkyom7LMstCCP4mYLwAWQL', start_index=10309)
Annotation(end_index=10323, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGR4u2yPRz5Zhyt9av_PaXRsf_U2FHpT2zRYoT2ThaLRQ6w8ROJpIA9a-bxZdCaIoybIxh7mhuowIQrtvQtaF3Ym2ieRef-mp2zW0q-tMuomJzlB8Dv512OBdPvSL8bhlQKW6dhK4jSF27f-iLbanyhkYjE_jNnBvQkvODXdKXYwzNEyqNiqGdwmzfFu18W7ppL_1zY-Ft2RzslAN2VsiQlaRfhQt-RR_dajwGsn3MVltFW9cAPIrx-pRRx-ZI9mllqEiHyNhpolEjw', start_index=10309)
Annotation(end_index=11442, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjvlOVsH553Wp4WZ4YZbacSNkqhTS-qpkbKWIOj2fCWr4lxsXNqI_TjpEDifCJADzTAGNnlJrc8PqGMLhJ6YZQ8QzfFaA_f-mzEC5_ESX8age_zUwg8-xJ4XYoz-LSdt7Htfw1gwl6bbq4ftfCVw5LDQEWFFqQ3fcj8uC8MZf80zYE9kqkgug-M1qRyV3AZnOy2xqLaSC_6I-bELuP81FE4Z3F6RtD7HSS52vBOLQfEiMgbP3Nhw1s', start_index=11424)
Annotation(end_index=11442, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0_KMCI1C2-sBflcBfM3h2xeP1HfmvJqw2GOSj6145G6HBIG5am2FCKea6FPeqNrOoe60aMc9Q1KdQGAIbvYHHeWro-DUr77FbydhGV0-5Vuugqk87KhG6Qa-OpA==', start_index=11424)
Annotation(end_index=11442, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEklf8yHrlvdIc-3oSy8_CP3mhIArxdd7p3s-E51V6eeb11A_2NSBIrrUQeFeVcwbhZzIhK_bH2R11lECjPpkumdbcqm9JxVDqURBtZsPr4VMxp1aweiKCR3F8tW9af6AkIXoo1Z7jjH_L_gkMgvlb7FHLkcr52b8Wze133Oxk4wOBGa7_Ywglvwh2RbOKj3mS1NfFr4lHoltchQ7omflBW31v-Ns9sKAihekW43uJUTDWQBPtpvmIV771RkoA4PIAdoE62eZycEhJkeQQyAO3nqwTdr8B7pNGNUN8bCjwfw==', start_index=11424)
Annotation(end_index=11694, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlxWeKDEAkTbDNixM2WHBxecH6c0v96oQ9cNqFkOF4L-q_905VAX9cFZtQDnulpG41LwIqjho0AP41CwWYWo4UKJ7fDKE1M3QrTS6YPgcnaOFWhg6D8jO0wa4s5BIDs6z_G3wpNgbXLnX14aPpQGB6subcNNw4iDmJ48MHj-gnLNIyEFByamEbNF5Ozen2fC6H5KsYe1X6eSa8Q6_yPgfCOuNjNtkw1O42uNTTRrWCwj4XgFMMZMnzsh_nAIMsLQc-lsZ2Qd6qFi4=', start_index=11684)
Annotation(end_index=12228, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPg3A6N_l7lW2BSmuFEehs-1MwjfRkJSfesu13eq8-4WmNg_YhMK3OqePmtR8q1YOQz0DWNyDa_Ldc7dQ1zVoBtqPCpsGL4pCKiB2wFowpotBqyhtdqIY=', start_index=12218)
Annotation(end_index=12520, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZKolj6sRJw354VKy3m1-GZ1IWT9ie6dKR7pkczHSQMmt6IUZOObfNSMHOUbb-SgemhUEPWYZ8I8tsYb8Z06q6pZNGGku9rRIxjSdXT5KlOEA4g9okOtzpaetZJr89', start_index=12510)
Annotation(end_index=13337, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEeWnDAL-lJ4rDpb1kJlGq5XMwDJ1XaSUP_SVyaaCWKL6uOyHQqirVZM9SMdDlkVPAa93dIUhxbg_as9yk7oNGL6NiiwGQvxuY5Stb2sbJ7cqODP-6-o8MhS_GARQyZccRqla3L7LM-sW-78a2zhy_H39tR0xwd0n6rudSUagxXY92OjY7wzpggZ8Zb9bE7kSH7dQ8fCKATd_tbgkZtiCdO2FtO9Y--ixuc5LznqhK9oOC0HjOOHv50M--twHv_CnyEQecu52dYTiquGXhXxgFgbPvR7jQ-KBdONuqV6Ytv', start_index=13323)
Annotation(end_index=13337, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4xTG42QW-KhPDE2mmM8jeAJGtq8zBNq4ZPbDSTdnz6db8_eEYBQpcnpscLMm_8wKOef6jFD_BgVKqg76IgeGLsk7AoPBGkI6-r-ypCKNCsWaEJAo3hyBCPkuNBE4RiIrJhmdhpEva', start_index=13323)
Annotation(end_index=13529, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHwIp6SUGtL7QuS7YNRj35lESHYrFuJcxTTGPAvQxv3LZmw9Xk7P2IPCi_Rwvo_F-hUztNuoDErz7pm-kMzqwkbJmuEQ_rBELkSJvQq0uHXJ7NmfWJC7cAmZksrveamyr7YLKfAmu4bHOqSmjx9uSwGPjc', start_index=13519)
Annotation(end_index=14031, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLAGNU2CsYRplIo4WINwdVb0pGK_kneIOJzTujB6BIXk8bM8S0dw0DUQpDgp1pN9Q1_rduoImL-6GY9L45pxuAn6cN4t1y2k7HndczMpL0TYa1kknYghEGx2eIWkPQ', start_index=14022)
Annotation(end_index=14477, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSKD1iQI37_aoV2UnOCWuwpnK9CCekK-MDQfZ8wia10EXV2temS3eqNcxvG1JkHSiai_GdNXi8skHVovnMWD6p83gwva-TFLtSLiyAmkA6ZSyeDtUYmcQrHcMm_JFYtn5hXn2O9A4VYAtOiZ3ynwSy7GkALoVfjRgGyzpTkT0oPfmch3laKZylvK1sKrq3UGrntgmD1lB4HSNWyVLmP3fareNmC0A21RUEoR7pwGrBZXKebZRTvpsuuMZQpblm5QKHRqa9Xch9DbrA', start_index=14467)

## Sources
