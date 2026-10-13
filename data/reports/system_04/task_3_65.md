# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** f33e6a9e | **Time:** 385.62s | **Cost:** $2.24046
--------------------------------------------------------------------------------

# Does Geochemical Anomaly Identification Constrain Urban Mineral Development Economics Based on Grade Gradients?

## Executive Summary

The identification of geochemical anomalies acts as a primary economic constraint on urban mineral development, fundamentally governed by the characterization of **grade gradients**. Research indicates that the economic viability of extracting mineral resources—whether from natural deposits situated in peri-urban environments or from "urban mines" (anthropogenic stocks like landfills and tailings)—is contingent upon the precise delineation of ore-waste boundaries. These boundaries are defined by grade gradients: the spatial rate of change in element concentration.

In urban settings, geochemical baselines are obscured by high spatial variability and anthropogenic contamination, necessitating advanced identification methods such as **fractal/multifractal modeling** (e.g., Concentration-Area methods, Singularity Mapping) and **machine learning** (e.g., Memory-Augmented Autoencoders). The failure to accurately resolve grade gradients leads to suboptimal **dig limits**, increased **dilution**, and misclassification of resources, directly impacting the Net Present Value (NPV) of a project. Consequently, the ability to identify and model these gradients determines the sampling density required, the mining selectivity possible, and ultimately, the economic feasibility of development.

### Key Findings
*   **Grade Gradients as Economic Determinants:** The steepness of a grade gradient dictates the "digability" and selectivity of extraction. Sharp gradients (common in anthropogenic anomalies) allow for precise separation but require high-density sampling to map. Diffuse gradients (low continuity) increase the risk of dilution, constraining economic recovery [cite: 1, 2].
*   **Urban Geochemical Noise:** Urban environments lack typical vertical stratification and exhibit high "nugget effects" due to human activity. This complicates the separation of economic mineralization from background pollution, imposing higher costs on exploration and resource estimation [cite: 3, 4, 5].
*   **Advanced Identification Necessity:** Traditional statistical thresholds (e.g., mean + 2SD) are insufficient for urban mineral development. Structural and multifractal methods (Singularity Mapping, MemAE) are required to constrain anomalies effectively, thereby reducing financial risk [cite: 6, 7].
*   **Dig Limit Optimization:** The economic constraint is operationalized through dig limit optimization algorithms (e.g., Simulated Annealing), which rely on the accurate representation of grade gradients to maximize profit under equipment constraints [cite: 2, 8, 9].

---

## 1. Introduction

The intersection of exploration geochemistry, urban development, and resource economics presents a complex matrix of constraints that govern the feasibility of mineral projects. As global urbanization expands, the distinction between "natural" mineral exploration and "urban" environmental geochemistry blurs. Mineral deposits are increasingly sought beneath or adjacent to urban infrastructure, while simultaneously, the concept of "urban mining"—the recovery of resources from anthropogenic waste streams—gains traction as a viable economic activity.

Central to the economics of these endeavors is the **geochemical anomaly**: a deviation from the background concentration of elements that indicates potential mineralization or resource accumulation. However, the mere presence of an anomaly is insufficient for economic development. The spatial distribution of the valuable elements, characterized by **grade gradients** (the rate of change of concentration over distance), determines whether a resource can be extracted profitably.

This report provides an exhaustive analysis of how the identification of these anomalies, and specifically the resolution of their grade gradients, constrains the economics of urban mineral development. It synthesizes findings from geostatistics, machine learning, and environmental geochemistry to demonstrate that accurate gradient modeling is the linchpin of resource estimation, dig limit optimization, and financial risk management in complex urban environments.

### 1.1 Defining the Core Concepts

**Geochemical Anomaly Identification:**
This refers to the analytical and statistical process of separating "signal" (enrichment related to mineralization or anthropogenic accumulation) from "noise" (background geological or environmental variation). In urban settings, this is complicated by the superposition of pollution halos over natural geochemical signatures [cite: 3, 10].

**Urban Mineral Development:**
This term encompasses two distinct but related activities:
1.  **Peri-urban Exploration:** The search for and extraction of natural mineral deposits located within or near urban boundaries, where land-use constraints and environmental regulations are paramount.
2.  **Anthropogenic Urban Mining:** The characterization and extraction of secondary resources from urban stocks, such as municipal solid waste incineration (MSWI) residues, landfills, and construction waste [cite: 11, 12].

**Grade Gradients:**
In the context of resource estimation, the grade gradient represents the local spatial variability of the resource grade. It is a vector quantity describing the direction and steepness of grade change. High gradients imply sharp contacts between ore and waste (e.g., a vein or a distinct landfill cell), while low gradients imply diffuse mineralization. The gradient directly influences the "continuity" of the deposit, a critical factor in resource classification (Measured, Indicated, Inferred) [cite: 1, 13].

---

## 2. Geochemical Anomaly Identification in Urban Environments

The identification of geochemical anomalies in urban environments is the first step in the mineral development value chain. However, unlike pristine wilderness environments, urban landscapes present unique geochemical challenges that constrain how anomalies are defined and subsequently valued.

### 2.1 The Challenge of the Urban Geochemical Landscape

Urban geochemistry is characterized by extreme lateral and vertical variability, often described as a "mosaic" of anthropogenic and natural signals. Research indicates that urban soils do not possess the typical vertical stratification associated with naturally developed pedogenic horizons [cite: 3]. Instead, they are mixtures of:
*   **Technogenic Substrates:** Construction rubble, asphalt, and industrial waste.
*   **Imported Materials:** Garden soils and fill material brought from outside the local geological context.
*   **Atmospheric Deposition:** Fallout from traffic, industry, and incineration [cite: 3, 5].

**Constraint on Identification:**
This heterogeneity creates a high "nugget effect" (random short-scale variability) in geochemical data. Traditional anomaly identification methods, which assume a single background population (e.g., a normal distribution of element concentrations), fail in urban settings. They often misclassify anthropogenic pollution as mineralization or, conversely, mask subtle deep-seated mineralization behind surface noise [cite: 14, 15].

**Vertical Stratification Issues:**
In natural soils, element concentrations typically follow predictable depth profiles due to leaching and weathering. In urban soils, vertical distribution is chaotic. Studies have shown that while some elements (e.g., Pb, Zn) decrease with depth due to surface deposition, others may show inverted C-shaped distributions or random spikes due to buried waste or fill layers [cite: 4, 16, 17]. This lack of continuity constrains the ability to project surface anomalies to depth, increasing the risk of drilling or excavation programs.

### 2.2 Advanced Identification Methodologies

To overcome the constraints of urban variability, advanced statistical and machine learning models have been developed. These methods are essential for resolving the **grade gradients** necessary for economic evaluation.

#### 2.2.1 Fractal and Multifractal Models
Fractal geometry provides a robust framework for separating anomalies in complex datasets. The underlying premise is that geological and anthropogenic processes operate at different scales, resulting in distinct fractal dimensions.
*   **Concentration-Area (C-A) Method:** This method plots the cumulative area $A(\rho)$ with concentration greater than $\rho$ against $\rho$ on a log-log scale. Distinct straight-line segments indicate different geochemical populations (e.g., background vs. anomaly) [cite: 16, 18, 19].
*   **Spectrum-Area (S-A) and Singularity Mapping:** These techniques analyze the frequency domain of geochemical data. They are particularly effective at identifying "weak" anomalies hidden within strong background noise, a common scenario in urban exploration where a deep orebody's signal is faint compared to surface pollution [cite: 7, 14].
*   **Local Singularity Analysis:** This characterizes the scaling behavior of element concentrations at a specific location. It can distinguish between sharp, high-gradient anomalies (often anthropogenic or high-grade veins) and diffuse, low-gradient patterns [cite: 20].

#### 2.2.2 Machine Learning and Deep Learning
Recent advancements utilize deep learning to capture non-linear relationships in geochemical data.
*   **Memory-Augmented Autoencoders (MemAE):** Traditional autoencoders can over-generalize, reconstructing anomalies as well as normal data. MemAEs incorporate a memory module to learn the "prototypical" patterns of the background. When an anomaly is encountered, the model fails to reconstruct it accurately using the memory slots, resulting in a high reconstruction error that flags the anomaly. This is crucial for identifying subtle mineralization in heterogeneous urban data [cite: 6, 21].
*   **Random Forests (RF) and Support Vector Machines (SVM):** These supervised algorithms integrate multiple data layers (geochemistry, geology, structural faults) to predict mineralization. In the Torud-Chahshirin belt, for example, RF assisted by singularity mapping achieved 98.85% accuracy in distinguishing Cu-Au anomalies [cite: 7].

**Economic Implication:**
The choice of identification method directly constrains the **resource model**. A method that fails to resolve the sharp gradient between a pollution hotspot and a mineral target will result in a "smeared" resource model, leading to incorrect tonnage and grade estimates. Conversely, high-precision methods (like MemAE) allow for tighter grade control and more accurate economic forecasting [cite: 6].

---

## 3. Grade Gradients: The Geometry of Economic Constraint

Once an anomaly is identified, its economic potential is defined by its internal structure, specifically the **grade gradient**. The grade gradient is not merely a geological curiosity; it is a fundamental geostatistical descriptor that dictates mining engineering and profitability.

### 3.1 Defining Grade Gradients and Spatial Variability

In geostatistics, the grade gradient refers to the magnitude of the change in grade over a given distance. It is a measure of **local spatial variability**.
*   **High Grade Gradient:** Indicates a rapid change in concentration. Examples include the sharp contact between a pegmatite dike and host rock [cite: 22], or the boundary of a distinct waste cell in a landfill.
*   **Low Grade Gradient:** Indicates a gradual change. Examples include disseminated porphyry copper deposits or diffuse soil contamination plumes [cite: 1, 23].

**The Continuity Constraint:**
Grade continuity is the consistency of the grade between sampling points. High gradients often imply lower continuity at larger scales (the "nugget effect"), making prediction between drill holes risky. Research emphasizes that classification of Mineral Resources (Measured, Indicated, Inferred) relies heavily on confidence in this continuity [cite: 13, 24]. In urban deposits, where continuity is disrupted by infrastructure or heterogeneous waste placement, the risk of misclassification is elevated.

### 3.2 Grade Gradients and Resource Estimation

The estimation of mineral resources involves interpolating grades from point data (drill holes, samples) into block models. The accuracy of this interpolation is constrained by the grade gradient.
*   **Smoothing Effect:** Traditional interpolation methods like Kriging tend to smooth data, underestimating high grades and overestimating low grades. In deposits with sharp gradients (e.g., urban gold veins or e-waste hotspots), this smoothing causes "ore loss" (high-grade material treated as waste) and "dilution" (waste treated as ore) [cite: 1, 25].
*   **Geological Constraints:** To mitigate smoothing, estimation must be constrained by geological boundaries (domains). In urban mining, these domains might be defined by alteration zones or, in the case of landfills, by the stratigraphy of waste deposition. Machine learning models (e.g., PSO-RF) attempt to integrate these domain boundaries to preserve the sharpness of the grade gradients in the final model [cite: 1].

### 3.3 The "Dig Limit" Problem

The ultimate economic constraint imposed by grade gradients is the determination of **dig limits**—the operational boundaries that separate material sent to the mill (profit) from material sent to the waste dump (cost).

**The Optimization Challenge:**
Dig limit optimization aims to maximize profit subject to constraints:
1.  **Economic Constraint:** The block must generate positive revenue (Grade > Cut-off).
2.  **Equipment Constraint:** The mining equipment (excavators, shovels) has a minimum selective mining unit (SMU). It cannot mine a single 1x1m block of ore if it is surrounded by waste.
3.  **Gradient Constraint:** The sharpness of the grade gradient determines how much waste must be mined to recover the ore (dilution).

**Simulated Annealing (SA):**
Research highlights Simulated Annealing as a powerful stochastic method for optimizing dig limits. SA iteratively perturbs the dig boundary to find a global maximum for profit while respecting the "digability" constraints imposed by the equipment.
*   *Scenario:* If the grade gradient is shallow (gradual transition), the optimal dig line is sensitive to small price changes and grade errors.
*   *Scenario:* If the grade gradient is steep (sharp contact), the dig line is robust.
*   *Urban Application:* In urban mining, where "grades" (e.g., copper in incineration ash) can change abruptly, SA helps define precise extraction polygons that minimize the processing of hazardous or non-valuable material [cite: 2, 8, 9, 26].

---

## 4. Economic Constraints in Urban Mineral Development Scenarios

The theoretical constraints of anomaly identification and grade gradients manifest differently depending on the specific type of urban mineral development.

### 4.1 Scenario A: Peri-Urban Mineral Exploration

Exploration near cities (e.g., the Garpenberg mine in Sweden or historical districts in the UK) faces the dual challenge of **depth** and **surface noise**.
*   **Constraint:** Urban infrastructure prevents dense surface sampling. Geochemical anomalies must be identified from sparse data or deep drilling.
*   **Gradient Impact:** The "primary geochemical halo" of a deep deposit creates a vertical gradient that extends to the surface. However, in urban areas, this subtle gradient is often swamped by surface pollution (high anthropogenic gradient).
*   **Economic Consequence:** If the identification method cannot distinguish the deep, low-gradient signal from the shallow, high-gradient noise, the project fails. Methods like **Singularity Mapping** are specifically designed to enhance these weak, deep signals, thereby "unlocking" the economic potential of covered terrains [cite: 7, 14].
*   **Case Study Evidence:** In the Torud-Chahshirin belt, the integration of structural factors (fault density) with geochemical data using Random Forests allowed for the detection of Cu-Au anomalies that were otherwise invisible, directly impacting the prospectivity and economic valuation of the belt [cite: 7].

### 4.2 Scenario B: Urban Mining (Anthropogenic Resources)

Urban mining involves the extraction of metals from secondary sources like municipal solid waste (MSW) incineration ash, landfills, and tailings.
*   **Constraint:** These "deposits" are extremely heterogeneous. A landfill might contain a pocket of high-grade industrial waste next to inert construction rubble.
*   **Gradient Impact:** The grade gradients in anthropogenic deposits are often much sharper than in natural geological deposits.
    *   *Natural:* Hydrothermal alteration zones often fade over tens of meters.
    *   *Anthropogenic:* A battery disposal site might drop from 5% Li to 0% over a few centimeters.
*   **Economic Consequence:** The "nugget effect" is extreme. Standard geostatistical methods (Kriging) may fail because the assumption of spatial continuity holds only over very short distances. This necessitates **high-density sampling** (e.g., sensor-based sorting or dense drilling), which significantly increases the **Capital Expenditure (CAPEX)** and **Operating Expenditure (OPEX)** of the project [cite: 11, 12].
*   **Dig Limits:** The ability to mine these resources depends on the selectivity of the equipment relative to the grade gradient. If the gradient is sharper than the equipment's resolution, dilution destroys the project's economics.

### 4.3 Scenario C: Brownfield Remediation as Resource Recovery

In many urban projects, mineral development is tied to remediation (cleaning up contaminated land).
*   **Constraint:** The "anomaly" is a contaminant (e.g., Pb, As) that must be removed.
*   **Gradient Impact:** The cost of remediation is a function of the volume of soil to be treated. Accurate identification of the contamination gradient (the plume boundary) is critical.
*   **Fractal Analysis:** Using C-A fractal models allows for the precise definition of the "threshold" between background and contaminated soil. A slight shift in this threshold (e.g., defining the boundary at 500 ppm vs. 400 ppm) can change the volume of material to be excavated by orders of magnitude, fundamentally altering the project's economics [cite: 16, 18, 19].

---

## 5. Detailed Analysis of Identification Methods and Their Economic Impact

This section details *how* specific identification methods mitigate economic risks associated with grade gradients.

### 5.1 Fractal and Multifractal Modeling (C-A, S-A)
*   **Mechanism:** These methods decompose the geochemical field into components based on scaling properties. They do not rely on a fixed "cut-off" grade but rather identify the *structure* of the data.
*   **Economic Benefit:** By accurately separating multiple geochemical populations (e.g., background, weak anomaly, strong anomaly), these methods reduce the risk of **Type I errors** (false positives, leading to wasted exploration funds) and **Type II errors** (false negatives, leading to missed ore).
*   **Application:** In the Nakhilab region, the C-A method successfully separated Au and Cu anomalies from background, providing clear targets for follow-up, which optimizes the exploration budget [cite: 19].

### 5.2 Machine Learning: MemAE and Random Forests
*   **Mechanism:** Deep learning models like Memory-Augmented Autoencoders (MemAE) learn the complex, non-linear correlations between elements in the "normal" (background) data. When presented with anomalous data (mineralization), the reconstruction error spikes.
*   **Geological Constraints:** Adding geological constraints (e.g., distance to faults) to the loss function of these models forces them to respect the geological controls on grade gradients. This results in anomaly maps that are not just statistically significant but geologically plausible.
*   **Economic Benefit:** This increases the **Probability of Success (PoS)**. In the Nanling region, a geologically constrained MemAE achieved an AUC of 0.802, significantly outperforming standard methods. This precision allows for more targeted (and thus cheaper) drilling programs [cite: 6, 21].

### 5.3 Geostatistical Simulation and Uncertainty
*   **Mechanism:** Unlike estimation (which gives a single "best" grade), simulation generates hundreds of equiprobable realizations of the deposit. This captures the uncertainty in the grade gradients.
*   **Economic Benefit:** This allows for **risk analysis**. A miner can calculate the probability that a specific block is above the cut-off grade. In urban mining, where heterogeneity is high, knowing the *probability* of a block being waste vs. ore is often more valuable than knowing the *average* grade, as it informs the financial risk model [cite: 2, 8].

---

## 6. Conclusion

The identification of geochemical anomalies is not merely a technical exercise in exploration; it is a foundational economic constraint on urban mineral development. The link between the two is the **grade gradient**.

1.  **Constraint on Viability:** The economic viability of an urban mineral project is determined by the ability to selectively extract valuable material while minimizing waste. This selectivity is physically constrained by the **grade gradient** (sharpness of the ore-waste contact) and operationally constrained by the **dig limits**.
2.  **Constraint on Cost:** The nature of urban geochemical anomalies—characterized by high spatial variability, lack of vertical continuity, and anthropogenic noise—imposes a requirement for advanced, computation-heavy identification methods (Fractal, ML) and high-density sampling. This raises the entry cost for urban mineral development compared to greenfield exploration.
3.  **Constraint on Accuracy:** Failure to accurately model grade gradients using appropriate geostatistical or fractal tools leads to the smoothing of resources. In the high-value, low-margin context of urban mining, this smoothing can render a viable project uneconomic by diluting the grade or underestimating the tonnage of high-grade "hotspots."

In summary, geochemical anomaly identification constrains urban mineral development economics by defining the **spatial geometry of value**. The precision with which grade gradients can be resolved—amidst the noise of the urban environment—directly dictates the efficiency of extraction, the accuracy of resource estimation, and the ultimate profitability of the venture.

---

## 7. References

*   **[cite: 3]** Albanese, S., et al. (2008). *Urban Geochemical Mapping*.
*   **[cite: 14]** Zuo, R. (2018). *Identification of geochemical anomalies*.
*   **[cite: 6]** Luo, T., et al. (2024). *Identification of Geochemical Anomalies Using a Memory-Augmented Autoencoder Model with Geological Constraint*.
*   **[cite: 1]** Emery, X., et al. (2020). *Geostatistics for the Mining Industry*.
*   **[cite: 10]** Johnson, C.C., & Ander, E.L. (2008). *Urban geochemical mapping studies: how and why we do them*.
*   **[cite: 11]** Bielowicz, B., et al. (2025). *Exploring elemental variability in incineration residues for urban mining*.
*   **[cite: 13]** Dominy, S.C., et al. (2003). *Grade and geological continuity in high-nugget effect gold-quartz reefs*.
*   **[cite: 16]** Zuo, R., et al. (2009). *Application of fractal models to characterization of vertical distribution of geochemical element concentration*.
*   **[cite: 2]** Nelis, G., et al. (2022). *Stochastic analysis of dig limit optimization using simulated annealing*.
*   **[cite: 8]** Nelis, G., et al. (2022). *Stochastic analysis of dig limit optimization using simulated annealing*.
*   **[cite: 27]** Vranješ, T., et al. (2025). *Geochemical Anomalies in Soils... Topsoil vs. Subsoil*.
*   **[cite: 4]** Kříbek, B., et al. (2024). *Geochemical anomalies... depth profile analyses*.
*   **[cite: 18]** Daya, A.A., et al. (2017). *Identification of geochemical anomalies by the use of concentration-area (C-A) fractal model*.
*   **[cite: 7]** Kheirkhah, M., et al. (2023). *Identifying the local geochemical anomalies... using singularity mapping and random forests*.
*   **[cite: 5]** De la Torre, M.L., et al. (2023). *Geochemical Anomalies in Soils and Surface Waters in an Area Adjacent to a Long-Used Controlled Municipal Landfill*.
*   **[cite: 1]** Rossi, M.E., & Deutsch, C.V. (2014). *Mineral Resource Estimation*.
*   **[cite: 6]** Luo, T., et al. (2024). *Identification of Geochemical Anomalies Using a Memory-Augmented Autoencoder*.
*   **[cite: 9]** Sari, Y.A., & Kumral, M. (2018). *Dig-limits optimization*.
*   **[cite: 26]** Norrena, K., & Deutsch, C.V. (2001). *Automatic Determination of Dig Limits*.

**Sources:**
1. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFohRE3h5fw-Ubs1-7_bLeEHzK7ImscsalAlu8f5RpZrpu9-UtJqFItXy2EyCGh9A5doXzNeXrzi6jyBILrtnjELurncM-PeRfk1T3_s8Ja-t7Wn498k_r3MOuC6DZPcw==)
2. [saimm.co.za](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0zPmEiEDv7kN9hGwZTsqVIm8ZxcxUNRcacwQJpPl-AfO6kw5ymf0YDCCZGv8Wr_NemIvYyJNnNjgEtzWhOIq5iVx2csSfP1I5VWdGP4DUW4I_31--vqgI8Uocq64ZBXCiV5T_eQ==)
3. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP6doYW7Q4HnGFm_TsmR1ZDw1Mtp6pGAMrOUQC1kKzIZFsUSYxi4jrhHIKXRgH7AvPYvATOdTdWpKS4Akx2KbZQlkRRsnZawtpzoDS8aRWLFaOw16m1cyAXmgAqjXQ_AWU6hGFft9sGij6rlXGoU5kuJiLnFIqKX_pSs8fimGvguW-)
4. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4S6QcDSddSR3rCMbgj1foO6IoOA-oz7wsJqpT74gP_qkXbbX75rKhTxWZhOQAJuDLft0M6R0CdWW-70yrKBH-wLpa860eInQ3U9wnKYh6HIMHw9fkBL3Dc9e3gdE=)
5. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJPkHgZ-X6mP0anTWLiSgKU961vVf3-97jlRs2zJfYGG403tbXywVSg65xtaalUpImurc7VznVWb5G3g99GxRK2HapeEYJklwjKGRg0b986Ow9bhtZRve2ucECY1iULXm0z41J8NJ1NKb3LcygY2V9vwS6XCZTOiV1ikycMuUwuUwVoEZKUd0y00fCeFQaU6-MlovLtJjTfBWxo-kRmknFJj2ywTuJ0IwdAq6-V6gOBwH2ise5TWxFRKR7TSscsZlu9H9dJyzaHTx_3gnx44eE-KKIL9wv5r1KSK-0)
6. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9g-V-KEX69alQgvn3ZgBNpiKXeLGGcS2UQjWcsk7env8IwE7pB0Nt_9nqU_GCzNkQlPpXwZzrIBcTFp-ljZBGNz_q_1zHso3fGRjjMy1O9J9ii-6DquUHVATYoxmtI4pXo35IDxYPyi00k9LnVAogDMTNuPG66mJ40dFMKlZAMVIvbOrQDxLX1FLIbI3fPgSUBlXEAxRmjUYhiM4PqOLtrO6xVK5ALRRhplmHIWLjfMjRFDPTXjZYH-SylrMUIT1jpNf_JXZZI0T3vG8JcQ8_oCm7RLJdXQ==)
7. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEghqTsRo5fgTb_e4AD6A9Vw9xWrKOGc8h5OZHKNksAkvDkycdWTtABiQ8Il-IlJRur72xGQGEzECnUwPXvtQrT_MAnfYFhmIhMXGGE6-YAy2vbl7iEklBUIgjSreqdQw==)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQl4ZWpfSmxpaygayR7owWBLs72R-MaZ3uLJlSF8kK8DF3Wj8tt8ieF6GcNH7xRhgrriRHcYZjY0kujCYAUDd8wrb_DUYn50_U8m_8nNwsY2CjW_NfGSKXNLX7gc9KfmyYwa0lLvyRdPyQrHSOsz8EpIlM3b60VSxY341mqWsv9xV5XZxk4azEm6HK5_ohGL0xj5TZt5HVcmR3UefZCP4R-EcXvXrxhF-urg5wln06JA==)
9. [f1000research.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpdyPcMPGvvmg8JJ4i-CjrqKqMo3pYuYj4j8ydlwbbhRDVufeJvs8dRJ2_GMBOJSz5GnOkCz7Ss-bAcTenPjQP_LJ4STxoajB0vGuV9fS8DURUzlvccKB19FbO06nOsCDPqHhOM5e73v8BfoUrqBeW0g8tDF0DE6ta1mFacCm2eitJyjP2D0FwXBbEWu8-PsPk1IQ9W4RFdD8=)
10. [nerc.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFK1GrcIFlMJOZpziOj89M63kEiMDY-geatwuudrc4qrTG0qURiRpofndcHEjMV07u-rdhgW-msaJ_PcQ8iOsYT6Wv0nkWcCApebvvptiOSb9rqUFUQwyn5Mz6eBJaFbMMnj90CP8erxj0Hn4oZRiAEustGD2xj9u8Igk7r0sq0SYVP)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMYefhwaeY98fHpfwzfIkl-OGC2jdZ1TSvnIE0mqCFvPo3tNLhg2_2Tf-i0KXAk0PXE13887vLgv0Q7X-YrbPCdqL2numDaq0P2IEw0tmN9mSViaNqXxaqKuNo0cu0iSI27TwkDqD1VXyzL8Ly2xEW13AA2D2C_Eph7x-FVCAUlNevpPufam2pEZopQCTWlWKaB1G71_fWRbxCmN36c4f2SXiNnYa2ybTfyUEip62BAUNYbaIXovARMcFLW3tXhXErD4bYD88e8XzUuLEDLYYJjlBCWj2RJrk9UOGUfA==)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVWZjwDq_Z_Z30_eCAR1PnM_ev5j4nxO-VctNHwSGTrYkzxuuGg9OgOFlEzUeD7iKeY1m_sM_2BwX2DeU1_fMCgXKoAOTwQoQsMSwCQrJ7p9X3EOKPquCQGG6FT4Qgcf6Z04qW3zKyMrNL5j7wocp68dJZUHdVXzGyDRl06zhhmQsha4Uq8DpsasMFjyGq7FngJG_GJ2Aq_kp3_8oE1eyfR_9yKymcx154ElZFB722eZp_ERgHTw62XmAgGD6QLqAo2ZWW6FigK23k_BZrBYW02h6mt1wkATIl-K5JbIVZ_fJpOC1TS0X7YrEKqR70LnOhAlt3nSP3XbHSl9gcpg==)
13. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmZmptybTvOD6Ck3FzqgVcqccVLg8FKH7D_JgxA4wX7IVJKP-Fy3ykPC6sSIQBKTZ2YiHk2lvIF4iSPnwK0w1sYffaqF72VbV25-BK7mw661ovRLbAI4p5_weKq5Rjy6nMek6OUHMxKKUPDCbYxk63RSJyQQ==)
14. [researcher.life](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0tjgjApFjOdjKtMW61BNquIglZwoizZHmwQwCPaZ0QmUCW3zmEV84EtViFTIHrhFJI6BYRy2wFEX4tss3AictO3n3wqjPa13Im8x-IbUaxBXy-fJmrLsgD8E3uPz__kdEqeQ7t4QWB3KSdkoieIDv6GPA-xK3sNxwHUE2_NDDpU5zqN1JMlZjvmU0o9vMsgFWxuek)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVbVcxpuGyBWqCf7Yh_BNojjK-W7s29e0r5YQ-stLaza4eTroLn7Mv6XZY6MAsG1SKEXTIOP_1Az7lI2APaIzjtRc_NFUl8ktpNfSSGXK-RvdXBGHp3Gg43hB3WyDKVRy-ZYVMhNCwqb7pUMTK2ApKmQRlAxVROTxLqsMKyRHrsWkjwShNEG5xgV4=)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa6YO_M67KnpNWEnMOMUUMZHluoK9w59a6vsmcKoSBKkTBBYfSY1_8HYGXp91EeXjG6vVOhEj7A6i0kPyo0yA2iyINCae5cPZN5iQXV1g2-7b6jO4yMwAJqjcbQ7HxSRhOSshgR2VK29kqTmq0akonc6HbFEXT9K1L_9P_IQlEp1kG9Tn5OdF2u5NMbdhr2c2lzHlmDwn7zGG6p7Ni-F_BHgw87lAFdc6YyW_f9x7jUbWa-2Q9agP-qXLe2KsuvclBRuYTBfuSwfI-YnWsoA5qmcPSCWXQwnj2)
17. [preprints.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErlK6TYQ74GkfcSP-wtDLBMa7e6iW2crjNKGDb7OIJPSN_q9JbqtrjZ9CEpci-bECmlxawfGtilwzoEwV5pQblSP-ivCaNze57VR_5KTe70q0rULUih-i7w6otA5pzeMmQym6Iij3HiRh_HE2p0womo1M=)
18. [eares.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnq6afognn5G6xMsrX-ifmlgDebL-glfqURIUJIADxJR64zbGbUw0T2zUsy_orK7RlIFvxkv2YG2Hr-8nfmefZYXa8CBTgRjIPnAJSTRcIou3Ga8oOaa8mjdnxBh3_5a0Ta-lKK4gtipB1iV0FFg==)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVZO69kJdh9PYWtIwVVXtc7Gqs_cwfzCb3UpShWLIgaNqb8EUW0hSb1RtC1OjYnBVdZLpZ5AfMzKe2PjthnWhDqRwrQcZewN0clxWNjCqZhKW4Sf1lq3Fuba7UND-UR-WMQdccS5Q8i914VPiIkpD5XrOEA3LyjuLMzEKXyf2gR6lQjMQFT4lSChXCltnFoHwPt_Mdl5qbrpn7DXPiedUnMdevVWI2z5Icpg0aY1sAK102FjJExLbx913KPtDuxpdJ4G2vzngKzJBICdQm56y3lcZz0QG6cyKjwglJSPg1)
20. [hep.com.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFr_OWLOqt9u_Gk0x2MIotx2jq5P8Dt_xl18HGwqrnUpG_VlVVJaH0OjqOJ3Jl8m3wkosD-NWz7pJ1tweJkdmsSb7gI5yaktsCeAPOGJFnPt4U4LUfGEBA9smKC5B0-1AvOGrIzIivHDzhaFtgBGmPbNJOq)
21. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMrOiLm9sNKmiz8ie-yOStZRSVradkS-RTFQusWfF2WCfg_OT7m0kYvlEJgTkmFaJUZ417fhRjCWeB3Qvq1t_WfBEp2cj7nDiKOjfDuAv0w6MccakpxFcVbuUZs1d75SKYYrHk0TfoVfzBj2LxmUKytnbdW4GqT_Qc4bqZu52yuT6LLbGgWfxcoKi8vE-m4DWVSt069HxHIvTVFRDTKuf459dkROP58Mee3sCD3jySzNeKb4-YpMVtE0z6lF7XvFq_e66asNY=)
22. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4o7tj6CFFbBUO91F3vRAAZch9NRwy2t1jJGoY8j2fQyp5P3sp59ZM62dYDmnr8cXp94RBZjjnx4SJwuzysZUs0cTeOtG6IEa9Jan8TI1M77JmGn6FCoBCzmn_Tyo=)
23. [geoscienceworld.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDfpcUBrbLP-Ldt15ve79-yaqZ4f-GVYJQfVj40FwFAqP4pgC5RcTmvAeFownwBKkKxKElNyFuSJ5Bu8shJQNXETO1tlgnHB7FPRb-SSwnTvCkPvsHlnziyD71r4P5g85Ur6jZ3YwRzXnfXVfN4v4wSd4L8ZkratRETxULe6_UJZ51YuZGugJDI6nbFtZlbOGdZFXF0eokaaBWSLNG9S6s0lEHd0Yl5GHCU9l0Qzg0JXE8w7E=)
24. [cim.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRSDXMtEq1Fe2PBbo5JRJ48hS5860GJKTmMr60Eblt26MRfXA7wrcZgW8xR4wrAsDeZc59jYB6gHcmR2Q-EE7fcqkgXh8VZfKe6Aw5r_nmAeo0BniV191s0O3VkAe9bc3pYfDXgPWqRV5uXaIyEODU8ytK1S3rcsDfYgZlCiKEn0EbeMYiDpBrrLo4RyM=)
25. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsIyz_Jqijhk8dVzDJa1IsLjJzOMivshOLWjGjdw28Ur1Uzy8NTqRY4pTAwh6SX1pCqoB8Fm8ho7G6X416ZUxwYVYZ-_vlC7P3X6gEVEcYkvU-AqvKg0B8thYj5bvMDHF81Y0x7SfOpHqJDrU1nUchW8uk4ycZeovVXfnKw6djB7GJQB1CVM9CrkuoimjlkWCfyC8EUp68NYaOgsues17fDKDr8U9lZUB1bg==)
26. [ccgalberta.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHD0kWY1oXwagukmzothyuidWx73fGgrVLFLRmOF55L_GxxxMTiaizvuWa09rtZUVs0C9qP1x0TYHGSXXh6VVscvgoUUc7xiEr7qqmyiJLHE5_RFliLi0BIlBIMXMcxn8XuQkppPif4dCWDG3IKKP9zp5xhYs01zqp67A==)
27. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHD6OJFGG-rS0Zh59uv6eEk_25uajRYMYklYUs0Nj8xA-6NZlK8QJQIai8qwg3DkCGbydun-snFLKwA4ROAn3KIEF6EFDaHduk6IOxa7Pcj35VqvYlP_MSjqrjhDxE=)


## Annotations
Annotation(end_index=1830, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0zPmEiEDv7kN9hGwZTsqVIm8ZxcxUNRcacwQJpPl-AfO6kw5ymf0YDCCZGv8Wr_NemIvYyJNnNjgEtzWhOIq5iVx2csSfP1I5VWdGP4DUW4I_31--vqgI8Uocq64ZBXCiV5T_eQ==', start_index=1818)
Annotation(end_index=1830, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFohRE3h5fw-Ubs1-7_bLeEHzK7ImscsalAlu8f5RpZrpu9-UtJqFItXy2EyCGh9A5doXzNeXrzi6jyBILrtnjELurncM-PeRfk1T3_s8Ja-t7Wn498k_r3MOuC6DZPcw==', start_index=1818)
Annotation(end_index=2140, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4S6QcDSddSR3rCMbgj1foO6IoOA-oz7wsJqpT74gP_qkXbbX75rKhTxWZhOQAJuDLft0M6R0CdWW-70yrKBH-wLpa860eInQ3U9wnKYh6HIMHw9fkBL3Dc9e3gdE=', start_index=2125)
Annotation(end_index=2140, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP6doYW7Q4HnGFm_TsmR1ZDw1Mtp6pGAMrOUQC1kKzIZFsUSYxi4jrhHIKXRgH7AvPYvATOdTdWpKS4Akx2KbZQlkRRsnZawtpzoDS8aRWLFaOw16m1cyAXmgAqjXQ_AWU6hGFft9sGij6rlXGoU5kuJiLnFIqKX_pSs8fimGvguW-', start_index=2125)
Annotation(end_index=2140, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJPkHgZ-X6mP0anTWLiSgKU961vVf3-97jlRs2zJfYGG403tbXywVSg65xtaalUpImurc7VznVWb5G3g99GxRK2HapeEYJklwjKGRg0b986Ow9bhtZRve2ucECY1iULXm0z41J8NJ1NKb3LcygY2V9vwS6XCZTOiV1ikycMuUwuUwVoEZKUd0y00fCeFQaU6-MlovLtJjTfBWxo-kRmknFJj2ywTuJ0IwdAq6-V6gOBwH2ise5TWxFRKR7TSscsZlu9H9dJyzaHTx_3gnx44eE-KKIL9wv5r1KSK-0', start_index=2125)
Annotation(end_index=2445, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEghqTsRo5fgTb_e4AD6A9Vw9xWrKOGc8h5OZHKNksAkvDkycdWTtABiQ8Il-IlJRur72xGQGEzECnUwPXvtQrT_MAnfYFhmIhMXGGE6-YAy2vbl7iEklBUIgjSreqdQw==', start_index=2433)
Annotation(end_index=2445, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9g-V-KEX69alQgvn3ZgBNpiKXeLGGcS2UQjWcsk7env8IwE7pB0Nt_9nqU_GCzNkQlPpXwZzrIBcTFp-ljZBGNz_q_1zHso3fGRjjMy1O9J9ii-6DquUHVATYoxmtI4pXo35IDxYPyi00k9LnVAogDMTNuPG66mJ40dFMKlZAMVIvbOrQDxLX1FLIbI3fPgSUBlXEAxRmjUYhiM4PqOLtrO6xVK5ALRRhplmHIWLjfMjRFDPTXjZYH-SylrMUIT1jpNf_JXZZI0T3vG8JcQ8_oCm7RLJdXQ==', start_index=2433)
Annotation(end_index=2716, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQl4ZWpfSmxpaygayR7owWBLs72R-MaZ3uLJlSF8kK8DF3Wj8tt8ieF6GcNH7xRhgrriRHcYZjY0kujCYAUDd8wrb_DUYn50_U8m_8nNwsY2CjW_NfGSKXNLX7gc9KfmyYwa0lLvyRdPyQrHSOsz8EpIlM3b60VSxY341mqWsv9xV5XZxk4azEm6HK5_ohGL0xj5TZt5HVcmR3UefZCP4R-EcXvXrxhF-urg5wln06JA==', start_index=2701)
Annotation(end_index=2716, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpdyPcMPGvvmg8JJ4i-CjrqKqMo3pYuYj4j8ydlwbbhRDVufeJvs8dRJ2_GMBOJSz5GnOkCz7Ss-bAcTenPjQP_LJ4STxoajB0vGuV9fS8DURUzlvccKB19FbO06nOsCDPqHhOM5e73v8BfoUrqBeW0g8tDF0DE6ta1mFacCm2eitJyjP2D0FwXBbEWu8-PsPk1IQ9W4RFdD8=', start_index=2701)
Annotation(end_index=2716, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0zPmEiEDv7kN9hGwZTsqVIm8ZxcxUNRcacwQJpPl-AfO6kw5ymf0YDCCZGv8Wr_NemIvYyJNnNjgEtzWhOIq5iVx2csSfP1I5VWdGP4DUW4I_31--vqgI8Uocq64ZBXCiV5T_eQ==', start_index=2701)
Annotation(end_index=4670, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFK1GrcIFlMJOZpziOj89M63kEiMDY-geatwuudrc4qrTG0qURiRpofndcHEjMV07u-rdhgW-msaJ_PcQ8iOsYT6Wv0nkWcCApebvvptiOSb9rqUFUQwyn5Mz6eBJaFbMMnj90CP8erxj0Hn4oZRiAEustGD2xj9u8Igk7r0sq0SYVP', start_index=4657)
Annotation(end_index=4670, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP6doYW7Q4HnGFm_TsmR1ZDw1Mtp6pGAMrOUQC1kKzIZFsUSYxi4jrhHIKXRgH7AvPYvATOdTdWpKS4Akx2KbZQlkRRsnZawtpzoDS8aRWLFaOw16m1cyAXmgAqjXQ_AWU6hGFft9sGij6rlXGoU5kuJiLnFIqKX_pSs8fimGvguW-', start_index=4657)
Annotation(end_index=5188, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMYefhwaeY98fHpfwzfIkl-OGC2jdZ1TSvnIE0mqCFvPo3tNLhg2_2Tf-i0KXAk0PXE13887vLgv0Q7X-YrbPCdqL2numDaq0P2IEw0tmN9mSViaNqXxaqKuNo0cu0iSI27TwkDqD1VXyzL8Ly2xEW13AA2D2C_Eph7x-FVCAUlNevpPufam2pEZopQCTWlWKaB1G71_fWRbxCmN36c4f2SXiNnYa2ybTfyUEip62BAUNYbaIXovARMcFLW3tXhXErD4bYD88e8XzUuLEDLYYJjlBCWj2RJrk9UOGUfA==', start_index=5174)
Annotation(end_index=5188, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVWZjwDq_Z_Z30_eCAR1PnM_ev5j4nxO-VctNHwSGTrYkzxuuGg9OgOFlEzUeD7iKeY1m_sM_2BwX2DeU1_fMCgXKoAOTwQoQsMSwCQrJ7p9X3EOKPquCQGG6FT4Qgcf6Z04qW3zKyMrNL5j7wocp68dJZUHdVXzGyDRl06zhhmQsha4Uq8DpsasMFjyGq7FngJG_GJ2Aq_kp3_8oE1eyfR_9yKymcx154ElZFB722eZp_ERgHTw62XmAgGD6QLqAo2ZWW6FigK23k_BZrBYW02h6mt1wkATIl-K5JbIVZ_fJpOC1TS0X7YrEKqR70LnOhAlt3nSP3XbHSl9gcpg==', start_index=5174)
Annotation(end_index=5722, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFohRE3h5fw-Ubs1-7_bLeEHzK7ImscsalAlu8f5RpZrpu9-UtJqFItXy2EyCGh9A5doXzNeXrzi6jyBILrtnjELurncM-PeRfk1T3_s8Ja-t7Wn498k_r3MOuC6DZPcw==', start_index=5709)
Annotation(end_index=5722, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmZmptybTvOD6Ck3FzqgVcqccVLg8FKH7D_JgxA4wX7IVJKP-Fy3ykPC6sSIQBKTZ2YiHk2lvIF4iSPnwK0w1sYffaqF72VbV25-BK7mw661ovRLbAI4p5_weKq5Rjy6nMek6OUHMxKKUPDCbYxk63RSJyQQ==', start_index=5709)
Annotation(end_index=6448, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP6doYW7Q4HnGFm_TsmR1ZDw1Mtp6pGAMrOUQC1kKzIZFsUSYxi4jrhHIKXRgH7AvPYvATOdTdWpKS4Akx2KbZQlkRRsnZawtpzoDS8aRWLFaOw16m1cyAXmgAqjXQ_AWU6hGFft9sGij6rlXGoU5kuJiLnFIqKX_pSs8fimGvguW-', start_index=6439)
Annotation(end_index=6768, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP6doYW7Q4HnGFm_TsmR1ZDw1Mtp6pGAMrOUQC1kKzIZFsUSYxi4jrhHIKXRgH7AvPYvATOdTdWpKS4Akx2KbZQlkRRsnZawtpzoDS8aRWLFaOw16m1cyAXmgAqjXQ_AWU6hGFft9sGij6rlXGoU5kuJiLnFIqKX_pSs8fimGvguW-', start_index=6756)
Annotation(end_index=6768, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJPkHgZ-X6mP0anTWLiSgKU961vVf3-97jlRs2zJfYGG403tbXywVSg65xtaalUpImurc7VznVWb5G3g99GxRK2HapeEYJklwjKGRg0b986Ow9bhtZRve2ucECY1iULXm0z41J8NJ1NKb3LcygY2V9vwS6XCZTOiV1ikycMuUwuUwVoEZKUd0y00fCeFQaU6-MlovLtJjTfBWxo-kRmknFJj2ywTuJ0IwdAq6-V6gOBwH2ise5TWxFRKR7TSscsZlu9H9dJyzaHTx_3gnx44eE-KKIL9wv5r1KSK-0', start_index=6756)
Annotation(end_index=7233, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0tjgjApFjOdjKtMW61BNquIglZwoizZHmwQwCPaZ0QmUCW3zmEV84EtViFTIHrhFJI6BYRy2wFEX4tss3AictO3n3wqjPa13Im8x-IbUaxBXy-fJmrLsgD8E3uPz__kdEqeQ7t4QWB3KSdkoieIDv6GPA-xK3sNxwHUE2_NDDpU5zqN1JMlZjvmU0o9vMsgFWxuek', start_index=7219)
Annotation(end_index=7233, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVbVcxpuGyBWqCf7Yh_BNojjK-W7s29e0r5YQ-stLaza4eTroLn7Mv6XZY6MAsG1SKEXTIOP_1Az7lI2APaIzjtRc_NFUl8ktpNfSSGXK-RvdXBGHp3Gg43hB3WyDKVRy-ZYVMhNCwqb7pUMTK2ApKmQRlAxVROTxLqsMKyRHrsWkjwShNEG5xgV4=', start_index=7219)
Annotation(end_index=7662, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa6YO_M67KnpNWEnMOMUUMZHluoK9w59a6vsmcKoSBKkTBBYfSY1_8HYGXp91EeXjG6vVOhEj7A6i0kPyo0yA2iyINCae5cPZN5iQXV1g2-7b6jO4yMwAJqjcbQ7HxSRhOSshgR2VK29kqTmq0akonc6HbFEXT9K1L_9P_IQlEp1kG9Tn5OdF2u5NMbdhr2c2lzHlmDwn7zGG6p7Ni-F_BHgw87lAFdc6YyW_f9x7jUbWa-2Q9agP-qXLe2KsuvclBRuYTBfuSwfI-YnWsoA5qmcPSCWXQwnj2', start_index=7645)
Annotation(end_index=7662, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErlK6TYQ74GkfcSP-wtDLBMa7e6iW2crjNKGDb7OIJPSN_q9JbqtrjZ9CEpci-bECmlxawfGtilwzoEwV5pQblSP-ivCaNze57VR_5KTe70q0rULUih-i7w6otA5pzeMmQym6Iij3HiRh_HE2p0womo1M=', start_index=7645)
Annotation(end_index=7662, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4S6QcDSddSR3rCMbgj1foO6IoOA-oz7wsJqpT74gP_qkXbbX75rKhTxWZhOQAJuDLft0M6R0CdWW-70yrKBH-wLpa860eInQ3U9wnKYh6HIMHw9fkBL3Dc9e3gdE=', start_index=7645)
Annotation(end_index=8638, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVZO69kJdh9PYWtIwVVXtc7Gqs_cwfzCb3UpShWLIgaNqb8EUW0hSb1RtC1OjYnBVdZLpZ5AfMzKe2PjthnWhDqRwrQcZewN0clxWNjCqZhKW4Sf1lq3Fuba7UND-UR-WMQdccS5Q8i914VPiIkpD5XrOEA3LyjuLMzEKXyf2gR6lQjMQFT4lSChXCltnFoHwPt_Mdl5qbrpn7DXPiedUnMdevVWI2z5Icpg0aY1sAK102FjJExLbx913KPtDuxpdJ4G2vzngKzJBICdQm56y3lcZz0QG6cyKjwglJSPg1', start_index=8620)
Annotation(end_index=8638, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa6YO_M67KnpNWEnMOMUUMZHluoK9w59a6vsmcKoSBKkTBBYfSY1_8HYGXp91EeXjG6vVOhEj7A6i0kPyo0yA2iyINCae5cPZN5iQXV1g2-7b6jO4yMwAJqjcbQ7HxSRhOSshgR2VK29kqTmq0akonc6HbFEXT9K1L_9P_IQlEp1kG9Tn5OdF2u5NMbdhr2c2lzHlmDwn7zGG6p7Ni-F_BHgw87lAFdc6YyW_f9x7jUbWa-2Q9agP-qXLe2KsuvclBRuYTBfuSwfI-YnWsoA5qmcPSCWXQwnj2', start_index=8620)
Annotation(end_index=8638, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnq6afognn5G6xMsrX-ifmlgDebL-glfqURIUJIADxJR64zbGbUw0T2zUsy_orK7RlIFvxkv2YG2Hr-8nfmefZYXa8CBTgRjIPnAJSTRcIou3Ga8oOaa8mjdnxBh3_5a0Ta-lKK4gtipB1iV0FFg==', start_index=8620)
Annotation(end_index=8984, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0tjgjApFjOdjKtMW61BNquIglZwoizZHmwQwCPaZ0QmUCW3zmEV84EtViFTIHrhFJI6BYRy2wFEX4tss3AictO3n3wqjPa13Im8x-IbUaxBXy-fJmrLsgD8E3uPz__kdEqeQ7t4QWB3KSdkoieIDv6GPA-xK3sNxwHUE2_NDDpU5zqN1JMlZjvmU0o9vMsgFWxuek', start_index=8971)
Annotation(end_index=8984, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEghqTsRo5fgTb_e4AD6A9Vw9xWrKOGc8h5OZHKNksAkvDkycdWTtABiQ8Il-IlJRur72xGQGEzECnUwPXvtQrT_MAnfYFhmIhMXGGE6-YAy2vbl7iEklBUIgjSreqdQw==', start_index=8971)
Annotation(end_index=9257, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFr_OWLOqt9u_Gk0x2MIotx2jq5P8Dt_xl18HGwqrnUpG_VlVVJaH0OjqOJ3Jl8m3wkosD-NWz7pJ1tweJkdmsSb7gI5yaktsCeAPOGJFnPt4U4LUfGEBA9smKC5B0-1AvOGrIzIivHDzhaFtgBGmPbNJOq', start_index=9247)
Annotation(end_index=9899, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMrOiLm9sNKmiz8ie-yOStZRSVradkS-RTFQusWfF2WCfg_OT7m0kYvlEJgTkmFaJUZ417fhRjCWeB3Qvq1t_WfBEp2cj7nDiKOjfDuAv0w6MccakpxFcVbuUZs1d75SKYYrHk0TfoVfzBj2LxmUKytnbdW4GqT_Qc4bqZu52yuT6LLbGgWfxcoKi8vE-m4DWVSt069HxHIvTVFRDTKuf459dkROP58Mee3sCD3jySzNeKb4-YpMVtE0z6lF7XvFq_e66asNY=', start_index=9886)
Annotation(end_index=9899, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9g-V-KEX69alQgvn3ZgBNpiKXeLGGcS2UQjWcsk7env8IwE7pB0Nt_9nqU_GCzNkQlPpXwZzrIBcTFp-ljZBGNz_q_1zHso3fGRjjMy1O9J9ii-6DquUHVATYoxmtI4pXo35IDxYPyi00k9LnVAogDMTNuPG66mJ40dFMKlZAMVIvbOrQDxLX1FLIbI3fPgSUBlXEAxRmjUYhiM4PqOLtrO6xVK5ALRRhplmHIWLjfMjRFDPTXjZYH-SylrMUIT1jpNf_JXZZI0T3vG8JcQ8_oCm7RLJdXQ==', start_index=9886)
Annotation(end_index=10239, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEghqTsRo5fgTb_e4AD6A9Vw9xWrKOGc8h5OZHKNksAkvDkycdWTtABiQ8Il-IlJRur72xGQGEzECnUwPXvtQrT_MAnfYFhmIhMXGGE6-YAy2vbl7iEklBUIgjSreqdQw==', start_index=10230)
Annotation(end_index=10668, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9g-V-KEX69alQgvn3ZgBNpiKXeLGGcS2UQjWcsk7env8IwE7pB0Nt_9nqU_GCzNkQlPpXwZzrIBcTFp-ljZBGNz_q_1zHso3fGRjjMy1O9J9ii-6DquUHVATYoxmtI4pXo35IDxYPyi00k9LnVAogDMTNuPG66mJ40dFMKlZAMVIvbOrQDxLX1FLIbI3fPgSUBlXEAxRmjUYhiM4PqOLtrO6xVK5ALRRhplmHIWLjfMjRFDPTXjZYH-SylrMUIT1jpNf_JXZZI0T3vG8JcQ8_oCm7RLJdXQ==', start_index=10659)
Annotation(end_index=11392, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4o7tj6CFFbBUO91F3vRAAZch9NRwy2t1jJGoY8j2fQyp5P3sp59ZM62dYDmnr8cXp94RBZjjnx4SJwuzysZUs0cTeOtG6IEa9Jan8TI1M77JmGn6FCoBCzmn_Tyo=', start_index=11382)
Annotation(end_index=11611, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDfpcUBrbLP-Ldt15ve79-yaqZ4f-GVYJQfVj40FwFAqP4pgC5RcTmvAeFownwBKkKxKElNyFuSJ5Bu8shJQNXETO1tlgnHB7FPRb-SSwnTvCkPvsHlnziyD71r4P5g85Ur6jZ3YwRzXnfXVfN4v4wSd4L8ZkratRETxULe6_UJZ51YuZGugJDI6nbFtZlbOGdZFXF0eokaaBWSLNG9S6s0lEHd0Yl5GHCU9l0Qzg0JXE8w7E=', start_index=11598)
Annotation(end_index=11611, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFohRE3h5fw-Ubs1-7_bLeEHzK7ImscsalAlu8f5RpZrpu9-UtJqFItXy2EyCGh9A5doXzNeXrzi6jyBILrtnjELurncM-PeRfk1T3_s8Ja-t7Wn498k_r3MOuC6DZPcw==', start_index=11598)
Annotation(end_index=12003, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRSDXMtEq1Fe2PBbo5JRJ48hS5860GJKTmMr60Eblt26MRfXA7wrcZgW8xR4wrAsDeZc59jYB6gHcmR2Q-EE7fcqkgXh8VZfKe6Aw5r_nmAeo0BniV191s0O3VkAe9bc3pYfDXgPWqRV5uXaIyEODU8ytK1S3rcsDfYgZlCiKEn0EbeMYiDpBrrLo4RyM=', start_index=11989)
Annotation(end_index=12003, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmZmptybTvOD6Ck3FzqgVcqccVLg8FKH7D_JgxA4wX7IVJKP-Fy3ykPC6sSIQBKTZ2YiHk2lvIF4iSPnwK0w1sYffaqF72VbV25-BK7mw661ovRLbAI4p5_weKq5Rjy6nMek6OUHMxKKUPDCbYxk63RSJyQQ==', start_index=11989)
Annotation(end_index=12751, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsIyz_Jqijhk8dVzDJa1IsLjJzOMivshOLWjGjdw28Ur1Uzy8NTqRY4pTAwh6SX1pCqoB8Fm8ho7G6X416ZUxwYVYZ-_vlC7P3X6gEVEcYkvU-AqvKg0B8thYj5bvMDHF81Y0x7SfOpHqJDrU1nUchW8uk4ycZeovVXfnKw6djB7GJQB1CVM9CrkuoimjlkWCfyC8EUp68NYaOgsues17fDKDr8U9lZUB1bg==', start_index=12738)
Annotation(end_index=12751, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFohRE3h5fw-Ubs1-7_bLeEHzK7ImscsalAlu8f5RpZrpu9-UtJqFItXy2EyCGh9A5doXzNeXrzi6jyBILrtnjELurncM-PeRfk1T3_s8Ja-t7Wn498k_r3MOuC6DZPcw==', start_index=12738)
Annotation(end_index=13175, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFohRE3h5fw-Ubs1-7_bLeEHzK7ImscsalAlu8f5RpZrpu9-UtJqFItXy2EyCGh9A5doXzNeXrzi6jyBILrtnjELurncM-PeRfk1T3_s8Ja-t7Wn498k_r3MOuC6DZPcw==', start_index=13166)
Annotation(end_index=14706, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQl4ZWpfSmxpaygayR7owWBLs72R-MaZ3uLJlSF8kK8DF3Wj8tt8ieF6GcNH7xRhgrriRHcYZjY0kujCYAUDd8wrb_DUYn50_U8m_8nNwsY2CjW_NfGSKXNLX7gc9KfmyYwa0lLvyRdPyQrHSOsz8EpIlM3b60VSxY341mqWsv9xV5XZxk4azEm6HK5_ohGL0xj5TZt5HVcmR3UefZCP4R-EcXvXrxhF-urg5wln06JA==', start_index=14687)
Annotation(end_index=14706, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpdyPcMPGvvmg8JJ4i-CjrqKqMo3pYuYj4j8ydlwbbhRDVufeJvs8dRJ2_GMBOJSz5GnOkCz7Ss-bAcTenPjQP_LJ4STxoajB0vGuV9fS8DURUzlvccKB19FbO06nOsCDPqHhOM5e73v8BfoUrqBeW0g8tDF0DE6ta1mFacCm2eitJyjP2D0FwXBbEWu8-PsPk1IQ9W4RFdD8=', start_index=14687)
Annotation(end_index=14706, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0zPmEiEDv7kN9hGwZTsqVIm8ZxcxUNRcacwQJpPl-AfO6kw5ymf0YDCCZGv8Wr_NemIvYyJNnNjgEtzWhOIq5iVx2csSfP1I5VWdGP4DUW4I_31--vqgI8Uocq64ZBXCiV5T_eQ==', start_index=14687)
Annotation(end_index=14706, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHD0kWY1oXwagukmzothyuidWx73fGgrVLFLRmOF55L_GxxxMTiaizvuWa09rtZUVs0C9qP1x0TYHGSXXh6VVscvgoUUc7xiEr7qqmyiJLHE5_RFliLi0BIlBIMXMcxn8XuQkppPif4dCWDG3IKKP9zp5xhYs01zqp67A==', start_index=14687)
Annotation(end_index=15885, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0tjgjApFjOdjKtMW61BNquIglZwoizZHmwQwCPaZ0QmUCW3zmEV84EtViFTIHrhFJI6BYRy2wFEX4tss3AictO3n3wqjPa13Im8x-IbUaxBXy-fJmrLsgD8E3uPz__kdEqeQ7t4QWB3KSdkoieIDv6GPA-xK3sNxwHUE2_NDDpU5zqN1JMlZjvmU0o9vMsgFWxuek', start_index=15872)
Annotation(end_index=15885, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEghqTsRo5fgTb_e4AD6A9Vw9xWrKOGc8h5OZHKNksAkvDkycdWTtABiQ8Il-IlJRur72xGQGEzECnUwPXvtQrT_MAnfYFhmIhMXGGE6-YAy2vbl7iEklBUIgjSreqdQw==', start_index=15872)
Annotation(end_index=16200, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEghqTsRo5fgTb_e4AD6A9Vw9xWrKOGc8h5OZHKNksAkvDkycdWTtABiQ8Il-IlJRur72xGQGEzECnUwPXvtQrT_MAnfYFhmIhMXGGE6-YAy2vbl7iEklBUIgjSreqdQw==', start_index=16191)
Annotation(end_index=17308, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMYefhwaeY98fHpfwzfIkl-OGC2jdZ1TSvnIE0mqCFvPo3tNLhg2_2Tf-i0KXAk0PXE13887vLgv0Q7X-YrbPCdqL2numDaq0P2IEw0tmN9mSViaNqXxaqKuNo0cu0iSI27TwkDqD1VXyzL8Ly2xEW13AA2D2C_Eph7x-FVCAUlNevpPufam2pEZopQCTWlWKaB1G71_fWRbxCmN36c4f2SXiNnYa2ybTfyUEip62BAUNYbaIXovARMcFLW3tXhXErD4bYD88e8XzUuLEDLYYJjlBCWj2RJrk9UOGUfA==', start_index=17294)
Annotation(end_index=17308, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVWZjwDq_Z_Z30_eCAR1PnM_ev5j4nxO-VctNHwSGTrYkzxuuGg9OgOFlEzUeD7iKeY1m_sM_2BwX2DeU1_fMCgXKoAOTwQoQsMSwCQrJ7p9X3EOKPquCQGG6FT4Qgcf6Z04qW3zKyMrNL5j7wocp68dJZUHdVXzGyDRl06zhhmQsha4Uq8DpsasMFjyGq7FngJG_GJ2Aq_kp3_8oE1eyfR_9yKymcx154ElZFB722eZp_ERgHTw62XmAgGD6QLqAo2ZWW6FigK23k_BZrBYW02h6mt1wkATIl-K5JbIVZ_fJpOC1TS0X7YrEKqR70LnOhAlt3nSP3XbHSl9gcpg==', start_index=17294)
Annotation(end_index=18358, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVZO69kJdh9PYWtIwVVXtc7Gqs_cwfzCb3UpShWLIgaNqb8EUW0hSb1RtC1OjYnBVdZLpZ5AfMzKe2PjthnWhDqRwrQcZewN0clxWNjCqZhKW4Sf1lq3Fuba7UND-UR-WMQdccS5Q8i914VPiIkpD5XrOEA3LyjuLMzEKXyf2gR6lQjMQFT4lSChXCltnFoHwPt_Mdl5qbrpn7DXPiedUnMdevVWI2z5Icpg0aY1sAK102FjJExLbx913KPtDuxpdJ4G2vzngKzJBICdQm56y3lcZz0QG6cyKjwglJSPg1', start_index=18340)
Annotation(end_index=18358, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa6YO_M67KnpNWEnMOMUUMZHluoK9w59a6vsmcKoSBKkTBBYfSY1_8HYGXp91EeXjG6vVOhEj7A6i0kPyo0yA2iyINCae5cPZN5iQXV1g2-7b6jO4yMwAJqjcbQ7HxSRhOSshgR2VK29kqTmq0akonc6HbFEXT9K1L_9P_IQlEp1kG9Tn5OdF2u5NMbdhr2c2lzHlmDwn7zGG6p7Ni-F_BHgw87lAFdc6YyW_f9x7jUbWa-2Q9agP-qXLe2KsuvclBRuYTBfuSwfI-YnWsoA5qmcPSCWXQwnj2', start_index=18340)
Annotation(end_index=18358, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnq6afognn5G6xMsrX-ifmlgDebL-glfqURIUJIADxJR64zbGbUw0T2zUsy_orK7RlIFvxkv2YG2Hr-8nfmefZYXa8CBTgRjIPnAJSTRcIou3Ga8oOaa8mjdnxBh3_5a0Ta-lKK4gtipB1iV0FFg==', start_index=18340)
Annotation(end_index=19329, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVZO69kJdh9PYWtIwVVXtc7Gqs_cwfzCb3UpShWLIgaNqb8EUW0hSb1RtC1OjYnBVdZLpZ5AfMzKe2PjthnWhDqRwrQcZewN0clxWNjCqZhKW4Sf1lq3Fuba7UND-UR-WMQdccS5Q8i914VPiIkpD5XrOEA3LyjuLMzEKXyf2gR6lQjMQFT4lSChXCltnFoHwPt_Mdl5qbrpn7DXPiedUnMdevVWI2z5Icpg0aY1sAK102FjJExLbx913KPtDuxpdJ4G2vzngKzJBICdQm56y3lcZz0QG6cyKjwglJSPg1', start_index=19319)
Annotation(end_index=20238, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMrOiLm9sNKmiz8ie-yOStZRSVradkS-RTFQusWfF2WCfg_OT7m0kYvlEJgTkmFaJUZ417fhRjCWeB3Qvq1t_WfBEp2cj7nDiKOjfDuAv0w6MccakpxFcVbuUZs1d75SKYYrHk0TfoVfzBj2LxmUKytnbdW4GqT_Qc4bqZu52yuT6LLbGgWfxcoKi8vE-m4DWVSt069HxHIvTVFRDTKuf459dkROP58Mee3sCD3jySzNeKb4-YpMVtE0z6lF7XvFq_e66asNY=', start_index=20225)
Annotation(end_index=20238, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9g-V-KEX69alQgvn3ZgBNpiKXeLGGcS2UQjWcsk7env8IwE7pB0Nt_9nqU_GCzNkQlPpXwZzrIBcTFp-ljZBGNz_q_1zHso3fGRjjMy1O9J9ii-6DquUHVATYoxmtI4pXo35IDxYPyi00k9LnVAogDMTNuPG66mJ40dFMKlZAMVIvbOrQDxLX1FLIbI3fPgSUBlXEAxRmjUYhiM4PqOLtrO6xVK5ALRRhplmHIWLjfMjRFDPTXjZYH-SylrMUIT1jpNf_JXZZI0T3vG8JcQ8_oCm7RLJdXQ==', start_index=20225)
Annotation(end_index=20854, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQl4ZWpfSmxpaygayR7owWBLs72R-MaZ3uLJlSF8kK8DF3Wj8tt8ieF6GcNH7xRhgrriRHcYZjY0kujCYAUDd8wrb_DUYn50_U8m_8nNwsY2CjW_NfGSKXNLX7gc9KfmyYwa0lLvyRdPyQrHSOsz8EpIlM3b60VSxY341mqWsv9xV5XZxk4azEm6HK5_ohGL0xj5TZt5HVcmR3UefZCP4R-EcXvXrxhF-urg5wln06JA==', start_index=20842)
Annotation(end_index=20854, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0zPmEiEDv7kN9hGwZTsqVIm8ZxcxUNRcacwQJpPl-AfO6kw5ymf0YDCCZGv8Wr_NemIvYyJNnNjgEtzWhOIq5iVx2csSfP1I5VWdGP4DUW4I_31--vqgI8Uocq64ZBXCiV5T_eQ==', start_index=20842)
Annotation(end_index=22584, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP6doYW7Q4HnGFm_TsmR1ZDw1Mtp6pGAMrOUQC1kKzIZFsUSYxi4jrhHIKXRgH7AvPYvATOdTdWpKS4Akx2KbZQlkRRsnZawtpzoDS8aRWLFaOw16m1cyAXmgAqjXQ_AWU6hGFft9sGij6rlXGoU5kuJiLnFIqKX_pSs8fimGvguW-', start_index=22575)
Annotation(end_index=22661, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0tjgjApFjOdjKtMW61BNquIglZwoizZHmwQwCPaZ0QmUCW3zmEV84EtViFTIHrhFJI6BYRy2wFEX4tss3AictO3n3wqjPa13Im8x-IbUaxBXy-fJmrLsgD8E3uPz__kdEqeQ7t4QWB3KSdkoieIDv6GPA-xK3sNxwHUE2_NDDpU5zqN1JMlZjvmU0o9vMsgFWxuek', start_index=22651)
Annotation(end_index=22738, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9g-V-KEX69alQgvn3ZgBNpiKXeLGGcS2UQjWcsk7env8IwE7pB0Nt_9nqU_GCzNkQlPpXwZzrIBcTFp-ljZBGNz_q_1zHso3fGRjjMy1O9J9ii-6DquUHVATYoxmtI4pXo35IDxYPyi00k9LnVAogDMTNuPG66mJ40dFMKlZAMVIvbOrQDxLX1FLIbI3fPgSUBlXEAxRmjUYhiM4PqOLtrO6xVK5ALRRhplmHIWLjfMjRFDPTXjZYH-SylrMUIT1jpNf_JXZZI0T3vG8JcQ8_oCm7RLJdXQ==', start_index=22729)
Annotation(end_index=22893, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFohRE3h5fw-Ubs1-7_bLeEHzK7ImscsalAlu8f5RpZrpu9-UtJqFItXy2EyCGh9A5doXzNeXrzi6jyBILrtnjELurncM-PeRfk1T3_s8Ja-t7Wn498k_r3MOuC6DZPcw==', start_index=22884)
Annotation(end_index=22979, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFK1GrcIFlMJOZpziOj89M63kEiMDY-geatwuudrc4qrTG0qURiRpofndcHEjMV07u-rdhgW-msaJ_PcQ8iOsYT6Wv0nkWcCApebvvptiOSb9rqUFUQwyn5Mz6eBJaFbMMnj90CP8erxj0Hn4oZRiAEustGD2xj9u8Igk7r0sq0SYVP', start_index=22969)
Annotation(end_index=23096, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMYefhwaeY98fHpfwzfIkl-OGC2jdZ1TSvnIE0mqCFvPo3tNLhg2_2Tf-i0KXAk0PXE13887vLgv0Q7X-YrbPCdqL2numDaq0P2IEw0tmN9mSViaNqXxaqKuNo0cu0iSI27TwkDqD1VXyzL8Ly2xEW13AA2D2C_Eph7x-FVCAUlNevpPufam2pEZopQCTWlWKaB1G71_fWRbxCmN36c4f2SXiNnYa2ybTfyUEip62BAUNYbaIXovARMcFLW3tXhXErD4bYD88e8XzUuLEDLYYJjlBCWj2RJrk9UOGUfA==', start_index=23086)
Annotation(end_index=23222, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmZmptybTvOD6Ck3FzqgVcqccVLg8FKH7D_JgxA4wX7IVJKP-Fy3ykPC6sSIQBKTZ2YiHk2lvIF4iSPnwK0w1sYffaqF72VbV25-BK7mw661ovRLbAI4p5_weKq5Rjy6nMek6OUHMxKKUPDCbYxk63RSJyQQ==', start_index=23212)
Annotation(end_index=23345, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEa6YO_M67KnpNWEnMOMUUMZHluoK9w59a6vsmcKoSBKkTBBYfSY1_8HYGXp91EeXjG6vVOhEj7A6i0kPyo0yA2iyINCae5cPZN5iQXV1g2-7b6jO4yMwAJqjcbQ7HxSRhOSshgR2VK29kqTmq0akonc6HbFEXT9K1L_9P_IQlEp1kG9Tn5OdF2u5NMbdhr2c2lzHlmDwn7zGG6p7Ni-F_BHgw87lAFdc6YyW_f9x7jUbWa-2Q9agP-qXLe2KsuvclBRuYTBfuSwfI-YnWsoA5qmcPSCWXQwnj2', start_index=23335)
Annotation(end_index=23502, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0zPmEiEDv7kN9hGwZTsqVIm8ZxcxUNRcacwQJpPl-AfO6kw5ymf0YDCCZGv8Wr_NemIvYyJNnNjgEtzWhOIq5iVx2csSfP1I5VWdGP4DUW4I_31--vqgI8Uocq64ZBXCiV5T_eQ==', start_index=23493)
Annotation(end_index=23621, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQl4ZWpfSmxpaygayR7owWBLs72R-MaZ3uLJlSF8kK8DF3Wj8tt8ieF6GcNH7xRhgrriRHcYZjY0kujCYAUDd8wrb_DUYn50_U8m_8nNwsY2CjW_NfGSKXNLX7gc9KfmyYwa0lLvyRdPyQrHSOsz8EpIlM3b60VSxY341mqWsv9xV5XZxk4azEm6HK5_ohGL0xj5TZt5HVcmR3UefZCP4R-EcXvXrxhF-urg5wln06JA==', start_index=23612)
Annotation(end_index=23741, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHD6OJFGG-rS0Zh59uv6eEk_25uajRYMYklYUs0Nj8xA-6NZlK8QJQIai8qwg3DkCGbydun-snFLKwA4ROAn3KIEF6EFDaHduk6IOxa7Pcj35VqvYlP_MSjqrjhDxE=', start_index=23731)
Annotation(end_index=23845, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4S6QcDSddSR3rCMbgj1foO6IoOA-oz7wsJqpT74gP_qkXbbX75rKhTxWZhOQAJuDLft0M6R0CdWW-70yrKBH-wLpa860eInQ3U9wnKYh6HIMHw9fkBL3Dc9e3gdE=', start_index=23836)
Annotation(end_index=23944, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnq6afognn5G6xMsrX-ifmlgDebL-glfqURIUJIADxJR64zbGbUw0T2zUsy_orK7RlIFvxkv2YG2Hr-8nfmefZYXa8CBTgRjIPnAJSTRcIou3Ga8oOaa8mjdnxBh3_5a0Ta-lKK4gtipB1iV0FFg==', start_index=23934)
Annotation(end_index=24085, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEghqTsRo5fgTb_e4AD6A9Vw9xWrKOGc8h5OZHKNksAkvDkycdWTtABiQ8Il-IlJRur72xGQGEzECnUwPXvtQrT_MAnfYFhmIhMXGGE6-YAy2vbl7iEklBUIgjSreqdQw==', start_index=24076)
Annotation(end_index=24228, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJPkHgZ-X6mP0anTWLiSgKU961vVf3-97jlRs2zJfYGG403tbXywVSg65xtaalUpImurc7VznVWb5G3g99GxRK2HapeEYJklwjKGRg0b986Ow9bhtZRve2ucECY1iULXm0z41J8NJ1NKb3LcygY2V9vwS6XCZTOiV1ikycMuUwuUwVoEZKUd0y00fCeFQaU6-MlovLtJjTfBWxo-kRmknFJj2ywTuJ0IwdAq6-V6gOBwH2ise5TWxFRKR7TSscsZlu9H9dJyzaHTx_3gnx44eE-KKIL9wv5r1KSK-0', start_index=24219)
Annotation(end_index=24398, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFohRE3h5fw-Ubs1-7_bLeEHzK7ImscsalAlu8f5RpZrpu9-UtJqFItXy2EyCGh9A5doXzNeXrzi6jyBILrtnjELurncM-PeRfk1T3_s8Ja-t7Wn498k_r3MOuC6DZPcw==', start_index=24389)
Annotation(end_index=24484, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9g-V-KEX69alQgvn3ZgBNpiKXeLGGcS2UQjWcsk7env8IwE7pB0Nt_9nqU_GCzNkQlPpXwZzrIBcTFp-ljZBGNz_q_1zHso3fGRjjMy1O9J9ii-6DquUHVATYoxmtI4pXo35IDxYPyi00k9LnVAogDMTNuPG66mJ40dFMKlZAMVIvbOrQDxLX1FLIbI3fPgSUBlXEAxRmjUYhiM4PqOLtrO6xVK5ALRRhplmHIWLjfMjRFDPTXjZYH-SylrMUIT1jpNf_JXZZI0T3vG8JcQ8_oCm7RLJdXQ==', start_index=24475)
Annotation(end_index=24606, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpdyPcMPGvvmg8JJ4i-CjrqKqMo3pYuYj4j8ydlwbbhRDVufeJvs8dRJ2_GMBOJSz5GnOkCz7Ss-bAcTenPjQP_LJ4STxoajB0vGuV9fS8DURUzlvccKB19FbO06nOsCDPqHhOM5e73v8BfoUrqBeW0g8tDF0DE6ta1mFacCm2eitJyjP2D0FwXBbEWu8-PsPk1IQ9W4RFdD8=', start_index=24597)
Annotation(end_index=24685, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHD0kWY1oXwagukmzothyuidWx73fGgrVLFLRmOF55L_GxxxMTiaizvuWa09rtZUVs0C9qP1x0TYHGSXXh6VVscvgoUUc7xiEr7qqmyiJLHE5_RFliLi0BIlBIMXMcxn8XuQkppPif4dCWDG3IKKP9zp5xhYs01zqp67A==', start_index=24675)

## Sources
