# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 2dfd39d3 | **Time:** 350.19s | **Cost:** $1.68224
--------------------------------------------------------------------------------

# Kinetic Control Steps in Extraction Models and Their Impact on the Process Economics of Rare Earth Separation from Waste

**Key Points**
*   **Economic Determinism of Kinetics:** Kinetic control steps are not merely theoretical constraints but direct drivers of Capital Expenditure (CAPEX) and Operating Expenditure (OPEX). They dictate reactor residence times, equipment sizing, and energy consumption. For instance, reducing residence times from 32 hours to 8 hours in pilot operations has been shown to significantly lower capital intensity.
*   **Selectivity Beyond Equilibrium:** Traditional thermodynamic separation is limited by the chemical similarity of Rare Earth Elements (REEs). Kinetic separation—exploiting differences in reaction rates rather than equilibrium states—can achieve separation factors orders of magnitude higher (e.g., >200 vs. <2.5), fundamentally altering the economic viability of separating high-value heavy REEs.
*   **Modeling for Cost Reduction:** Dynamic non-equilibrium models are essential for optimizing industrial circuits. Unlike steady-state equilibrium models, dynamic simulations can predict the weeks-long stabilization periods required for solvent extraction plants, preventing costly operational inefficiencies during startup and upset conditions.
*   **Waste-Specific Economic Levers:** In waste valorization (e.g., phosphogypsum, e-waste), kinetic barriers such as product layer diffusion (Shrinking Core Model) often dictate the feasibility of extraction. Technologies like Flash Joule Heating leverage millisecond-scale kinetics to bypass the high reagent costs of traditional hydrometallurgy.

---

## 1. Introduction

The economic viability of recovering Rare Earth Elements (REEs) from secondary waste sources—such as electronic waste, phosphogypsum, coal fly ash, and mine tailings—is frequently constrained by the extreme difficulty of separating these chemically similar elements. Traditional hydrometallurgical processes rely heavily on thermodynamic equilibrium, utilizing slight differences in Gibbs free energy to achieve separation via solvent extraction (SX). However, this approach often necessitates hundreds of mixer-settler stages, resulting in high capital costs and substantial chemical consumption.

Recent research indicates that **kinetic control steps**—processes governed by reaction rates, diffusion velocities, and non-equilibrium mass transfer—play a pivotal role in determining the process economics. By shifting the design philosophy from thermodynamic equilibrium to kinetic control, operators can potentially reduce residence times, shrink equipment footprints, and achieve separation factors unattainable by conventional means. This report provides an exhaustive analysis of how kinetic control steps in extraction models influence the economics of REE separation from waste, synthesizing data from kinetic modeling, pilot plant operations, and techno-economic analyses (TEA).

## 2. Theoretical Framework: Kinetic Models in REE Extraction

To understand the economic implications, one must first establish the theoretical models used to describe REE extraction kinetics. These models identify the rate-limiting steps (RLS) that ultimately define the reactor volume and energy input required for a profitable operation.

### 2.1 The Shrinking Core Model (SCM) and Economic Implications
The Shrinking Core Model (SCM) is the dominant theoretical framework for describing the leaching of REEs from solid waste matrices, such as clay, coal waste, and phosphogypsum. The model assumes that the reaction initiates at the particle surface and moves inward, leaving behind an inert product layer (ash) [cite: 1, 2].

The SCM identifies three potential rate-controlling mechanisms, each with distinct economic consequences:
1.  **Film Diffusion Control:** The resistance lies in the liquid film surrounding the particle.
2.  **Chemical Reaction Control:** The resistance lies in the chemical reaction at the phase boundary.
3.  **Product Layer Diffusion Control:** The resistance lies in the diffusion of lixiviant through the porous product layer (ash/gangue).

Research on REE leaching from aluminosilicate ores and phosphogypsum consistently points to **product layer diffusion** or **mixed control** as the dominant mechanisms [cite: 1, 3, 4]. For example, in the leaching of fire clay seam coal, the activation energy was found to be 36 kJ/mol initially (chemical control) dropping to 27 kJ/mol (diffusion control) as the product layer formed [cite: 3].

**Economic Impact:**
*   **Grinding Costs (Comminution):** If a process is product-layer diffusion-controlled, reducing particle size is the most effective way to increase rates. However, comminution is energy-intensive. A kinetic model that accurately identifies diffusion limitations allows engineers to optimize the trade-off between grinding energy (OPEX) and leaching time (residence time/CAPEX) [cite: 5].
*   **Temperature Sensitivity:** Chemical reaction-controlled processes are highly sensitive to temperature (Arrhenius dependence). If the model indicates chemical control, investing in reactor heating (OPEX) yields significant rate increases. Conversely, for diffusion-controlled processes, raising temperature yields diminishing returns, suggesting that economic optimization should focus on agitation or particle size rather than heat [cite: 4].

### 2.2 Dynamic vs. Equilibrium Solvent Extraction Models
While solid-liquid leaching relies on SCM, liquid-liquid solvent extraction (SX) is traditionally modeled using equilibrium isotherms. However, industrial SX plants rarely operate at perfect equilibrium due to fluctuations in feed composition and flow rates.

**Non-Equilibrium (Dynamic) Models:**
Recent advancements emphasize dynamic modeling that accounts for mass transfer kinetics and stage efficiency. Research indicates that steady-state conditions in REE pilot plants can take up to 14 days to stabilize [cite: 6]. Dynamic models, such as those integrated with SysCAD or MATLAB/SIMULINK, simulate the transient behavior of hundreds of mixer-settlers [cite: 7, 8].

**Economic Impact:**
*   **Startup and Upset Costs:** The inability to predict the time-to-equilibrium leads to off-spec product during the weeks-long startup phase. Dynamic models mitigate this by optimizing control strategies, directly reducing the volume of waste product and the labor costs associated with prolonged stabilization periods [cite: 6].
*   **Stage Efficiency:** Equilibrium models assume 100% stage efficiency. Kinetic models reveal that actual mass transfer rates may require longer residence times in the mixer to approach equilibrium. Ignoring kinetics leads to undersized equipment (bottlenecks) or oversized equipment (wasted CAPEX) [cite: 8, 9].

## 3. Process Economics: The Role of Residence Time and Throughput

The most direct link between kinetic control and economics is **residence time**. In chemical engineering, residence time ($\tau$) determines the volume ($V$) of the reactor required for a given volumetric flow rate ($Q$): $V = Q \times \tau$. Therefore, faster kinetics allow for smaller reactors (lower CAPEX) or higher throughput for the same reactor size.

### 3.1 Case Study: Phalaborwa Rare Earths Project
A definitive example of kinetic optimization affecting economics is found in the Phalaborwa project (Rainbow Rare Earths). Pilot plant test work optimized the leaching circuit for phosphogypsum waste.
*   **Kinetic Improvement:** The optimization reduced the leach residence time from **32 hours to 8 hours** [cite: 10].
*   **Economic Result:** This reduction allows for a significantly smaller plant footprint, reducing civil works, steel, and concrete requirements. Furthermore, the optimization reduced the number of required filters by half and lowered heating requirements, positively impacting both CAPEX and OPEX [cite: 10].

### 3.2 Solvent Extraction Residence Times
In solvent extraction, the "contact time" or residence time in the mixer is critical.
*   **Optimal Contact Time:** Research on extracting Yttrium (Y) using D2EHPA determined an optimum stirring time of **25 minutes** to achieve equilibrium [cite: 11].
*   **Impurity Rejection (Kinetic Selectivity):** Crucially, kinetic control can be used to reject impurities. In the extraction of REEs from ion-adsorption ores, Aluminum (Al) leaches slower than REEs. By controlling the contact time (e.g., using non-equilibrium bubbling organic liquid membranes), operators can extract REEs while leaving Al in the raffinate. This "kinetic non-equilibrium separation" achieved a separation coefficient of 44.89, which is impossible under thermodynamic equilibrium where Al co-extracts [cite: 12, 13, 14].
*   **Cost Implication:** By preventing Al extraction kinetically, the downstream scrubbing stages (which consume acid and base) can be eliminated or reduced, significantly lowering reagent costs (OPEX) [cite: 12].

### 3.3 Flash Joule Heating: Extreme Kinetic Acceleration
Flash Joule Heating (FJH) represents the extreme end of kinetic control. By passing a high current through e-waste (magnets) for milliseconds to seconds, the material reaches 3000°C, enabling rapid thermal reduction or phase transformation.
*   **Kinetic Advantage:** The process completes in seconds, compared to hours for acid leaching.
*   **Economic Analysis:** Techno-economic analysis (TEA) of FJH combined with chlorination shows a reduction in energy consumption by **87%** and operating costs by **54%** compared to traditional hydrometallurgy [cite: 15]. This is a purely kinetic advantage—achieving separation speeds that render thermodynamic barriers (like stable oxides) irrelevant via thermal shock.

## 4. Kinetic Selectivity: Breaking the Thermodynamic Limit

The "Lanthanide Contraction" results in adjacent REEs having nearly identical ionic radii and thermodynamic properties, leading to low separation factors (typically 1.5–2.5 for adjacent elements in SX). This necessitates extensive cascades of mixer-settlers. Kinetic control offers a paradigm shift by exploiting differences in reaction *rates* rather than equilibrium states.

### 4.1 Redox-Active Ligands
A breakthrough study demonstrated the use of a redox-active ligand to separate Yttrium (Y) and Lutetium (Lu).
*   **Mechanism:** The separation relies on the difference in oxidation rates of the metal-ligand complexes.
*   **Result:** A single-step **separation factor of 261** was achieved [cite: 16, 17, 18].
*   **Economic Impact:** A separation factor of 261 implies that high purity can be achieved in very few stages (potentially 1-3), compared to dozens of stages required for a separation factor of 2.0. This would drastically reduce the CAPEX of the separation plant (fewer mixer-settlers, smaller building) and the chemical inventory (solvent inventory) [cite: 16].

### 4.2 Kinetic Separation of Impurities
In the processing of waste, impurities like Iron (Fe) and Aluminum (Al) often dominate the feedstock.
*   **Liquid Membrane Kinetics:** As mentioned, Al transfer kinetics are slower than REE kinetics in certain amine extraction systems (N1923). By limiting the contact time in a bubbling liquid membrane reactor, REEs are extracted while Al remains in the aqueous phase [cite: 12, 13].
*   **Economic Benefit:** This reduces the cost of "impurity removal" stages. In traditional flowsheets, Al removal requires precipitation (consuming ammonia or lime) and filtration, which incurs solid waste disposal costs and REE co-precipitation losses. Kinetic separation avoids these steps [cite: 14].

### 4.3 Chromatographic Separations
Centrifugal Partition Chromatography (CPC) and other chromatographic methods rely on the kinetics of partition between mobile and stationary phases.
*   **Throughput:** CPC replaces solid stationary phases with a liquid stationary phase held by centrifugal force. This allows for higher flow rates and reduced run times compared to traditional columns [cite: 19, 20].
*   **Cost Structure:** The absence of solid silica support (which degrades and requires replacement) reduces OPEX. The high separation efficiency (driven by multiple theoretical plates in a compact rotor) reduces the physical footprint (CAPEX) compared to mixer-settler cascades [cite: 20, 21].

## 5. Techno-Economic Analysis (TEA) and Modeling Inputs

Techno-economic analyses of REE recovery projects rely heavily on inputs derived from kinetic models. The accuracy of these inputs determines the reliability of the cost estimation.

### 5.1 Equipment Sizing Equations
Capital costs ($C_e$) are typically estimated using power-law scaling based on size ($S$):
\[ C_e = a + b \cdot S^n \]
where $S$ is often volume or throughput [cite: 22].
*   **Kinetic Link:** Since $S$ (Volume) is a function of residence time (determined by kinetics), an error in the kinetic model (e.g., assuming 10 minutes when 25 minutes is needed) leads to a direct underestimation of CAPEX.
*   **Example:** In the leaching of coal waste, the residence time for acid leaching (2 hours vs. 18 hours) dictates the size of the agitated reactors. A TEA for REE recovery from acid mine drainage showed that capital cost is a major factor influencing the rate of return [cite: 22, 23].

### 5.2 Reagent Consumption (OPEX)
Kinetic models also predict reagent consumption over time.
*   **Bioleaching:** In bioleaching REEs from waste, glucose consumption (for the bacteria) constituted **44.3%** of the total operating cost [cite: 24]. Kinetic models that optimize bacterial growth rates and lixiviant production can directly lower this dominant cost driver.
*   **Acid Consumption:** In the SCM, the consumption of acid is proportional to the conversion $x$. Kinetic studies determine the minimum acid concentration required to overcome diffusion resistance. Using excess acid to speed up a diffusion-limited reaction is economically wasteful; kinetic modeling prevents this by identifying the true rate-limiting step [cite: 4].

### 5.3 Sensitivity Analysis
Sensitivity analyses in TEAs consistently show that **recovery rate** and **production volume** are top economic drivers [cite: 25].
*   **Recovery vs. Time:** Kinetic models define the curve of Recovery vs. Time. Economic optimization involves finding the point on this curve where the marginal cost of additional residence time (larger tank) exceeds the marginal revenue of additional REE recovered. For example, leaching for 25 minutes might yield 87% Nd, while 90 minutes yields 100% [cite: 26]. A TEA would evaluate if the extra 65 minutes of residence time (tripling reactor size) is worth the extra 13% recovery.

## 6. Waste-Specific Kinetic Challenges

Different waste streams present unique kinetic challenges that influence their specific processing economics.

### 6.1 Coal Waste and Fly Ash
*   **Challenge:** REEs are often encapsulated in aluminosilicate glass phases.
*   **Kinetics:** Leaching is often diffusion-controlled through the ash layer.
*   **Economics:** High temperatures or pressure (autoclaves) are often required to break the glass phase kinetics, leading to high CAPEX. Alternatively, bio-oxidation (heap leaching) offers slow kinetics but very low CAPEX ($5/ton processing cost) [cite: 27]. The economic trade-off here is purely kinetic: fast/expensive (autoclave) vs. slow/cheap (heap).

### 6.2 End-of-Life Magnets (NdFeB)
*   **Challenge:** Iron (Fe) dissolution competes with REE extraction.
*   **Kinetics:** Thermal oxidative pre-treatment alters the leaching kinetics, making Fe less soluble (kinetic selectivity) [cite: 28].
*   **Economics:** This pre-treatment step adds energy cost but significantly reduces the downstream cost of solvent extraction (which would otherwise be overwhelmed by Fe). The "Hydro-Nd" process utilizes citric acid and kinetic modeling to optimize this selective leaching [cite: 29].

### 6.3 Phosphogypsum
*   **Challenge:** REEs are trapped in the gypsum lattice or as surface oxides.
*   **Kinetics:** The shrinking core model with cylindrical geometry fits the dissolution, with activation energy ~20 kJ/mol [cite: 4].
*   **Economics:** The low activation energy suggests diffusion control. Therefore, economic efficiency is gained by finer grinding (increasing surface area) rather than high-temperature leaching. The Phalaborwa pilot plant's success in reducing residence time was key to making this low-grade source economical [cite: 10].

## 7. Conclusion

The research conclusively demonstrates that **kinetic control steps are a primary determinant of process economics** in REE separation from waste. The influence manifests through three main channels:

1.  **Capital Intensity (CAPEX):** Kinetic rates dictate residence times, which in turn define the physical volume of reactors and mixer-settlers. Optimizations that accelerate kinetics (e.g., reducing leaching time from 32 to 8 hours) directly reduce capital investment.
2.  **Operational Efficiency (OPEX):** Kinetic models allow for the identification of rate-limiting steps (diffusion vs. reaction), enabling operators to optimize energy inputs (grinding vs. heating) and reagent usage. Dynamic modeling prevents costly startup delays and off-spec production.
3.  **Strategic Selectivity:** Kinetic separation methods (e.g., redox kinetics, liquid membrane diffusion rates) offer a pathway to bypass the thermodynamic limitations of the lanthanide contraction. Achieving separation factors >200 via kinetics, compared to <2.5 via thermodynamics, represents a disruptive economic advantage by collapsing the size of separation plants.

In summary, accurate kinetic modeling is not merely an academic exercise but a fundamental requirement for the financial feasibility of REE recycling projects. It bridges the gap between theoretical chemistry and the bankability of industrial plants.

## 8. Detailed Analysis of Kinetic Control in Extraction Models

### 8.1 The Shrinking Core Model (SCM) in Depth
The SCM is ubiquitous in REE waste processing literature because it accurately describes the heterogeneous reaction between solid waste particles and liquid lixiviants.

**Mathematical Representation:**
The integrated rate equations for the SCM depend on the rate-limiting step:
*   **Chemical Reaction Control:** $1 - (1-x)^{1/3} = k_c t$
*   **Product Layer Diffusion Control:** $1 - 3(1-x)^{2/3} + 2(1-x) = k_d t$
where $x$ is conversion, $t$ is time, and $k$ is the apparent rate constant [cite: 4, 30].

**Economic Interpretation of SCM Parameters:**
*   **Activation Energy ($E_a$):**
    *   $E_a < 20$ kJ/mol usually indicates diffusion control.
    *   $E_a > 40$ kJ/mol usually indicates chemical reaction control.
    *   **Economic Decision:** If $E_a$ is high (chemical control), the process economics will be heavily dependent on energy costs for heating. If $E_a$ is low (diffusion control), economics depend on comminution (grinding) costs. For example, leaching REEs from phosphogypsum showed an $E_a$ of 20.65 kJ/mol, indicating diffusion control [cite: 4]. This tells the process engineer that spending money on steam to heat the reactor above 60°C is likely waste; money is better spent on crushers to reduce particle size.

### 8.2 Dynamic Simulation of Solvent Extraction
Solvent extraction (SX) plants for REEs are notoriously complex due to the "scrambling" effect where hundreds of stages interact.

**The Problem with Equilibrium Models:**
Standard design uses McCabe-Thiele diagrams or equilibrium isotherms. These assume steady state. However, real plants experience disturbances.
*   **Research Finding:** A dynamic model using MATLAB/SIMULINK was required to predict the transient behavior of a Nd/Pr separation circuit. The model revealed that transient concentration profiles deviate from experimental results if mixer-settler holdup volumes are not accurately accounted for [cite: 8].
*   **Economic Consequence:** If a plant is designed solely on equilibrium data, the control systems may fail to handle flow surges, leading to the contamination of the high-purity REE product. Reprocessing off-spec material effectively doubles the OPEX for that batch. Dynamic models allow for the design of robust control loops that maintain product purity (and thus value) during operation [cite: 7, 31].

### 8.3 Kinetic Separation vs. Thermodynamic Separation
This is perhaps the most critical distinction for future economics.

**Thermodynamic Control:**
*   Relies on $\Delta G = -RT \ln K$.
*   Separation Factor $\beta = D_A / D_B$.
*   For REEs, $\beta$ is often small (e.g., 1.4 for Nd/Pr).
*   **Economic Result:** Requires many stages ($N \approx \frac{\log(\text{purity})}{\log(\beta)}$). High CAPEX.

**Kinetic Control:**
*   Relies on $\Delta \Delta G^\ddagger$ (difference in activation energy).
*   Separation depends on time $t$.
*   **Research Finding:** In the separation of Yttrium and Lutetium using a redox-active ligand, the oxidation rate difference led to a separation factor of **261** [cite: 16, 17].
*   **Economic Result:** A separation factor of 261 allows for essentially single-stage separation. This eliminates the need for a cascade, reducing the plant size by 90%+.

**Table 1: Comparison of Thermodynamic vs. Kinetic Separation Economics**

| Feature | Thermodynamic Control (Standard SX) | Kinetic Control (Novel Methods) | Economic Impact |
| :--- | :--- | :--- | :--- |
| **Separation Factor ($\beta$)** | Low (1.5 – 2.5) | High (>100 possible) | Kinetic control reduces stage count. |
| **Equilibration Time** | Must reach equilibrium (10-30 min) | Must interrupt before equilibrium | Kinetic control requires precise timing. |
| **Equipment** | Mixer-Settlers (Hundreds) | Centrifugal Contactors / Pulse Columns | Kinetic control favors compact, fast equipment. |
| **Control Complexity** | Low (Steady State) | High (Dynamic/Transient) | Kinetic control requires advanced automation. |
| **Impurity Rejection** | Co-extraction common | Rate-based rejection (e.g., Al) | Kinetic control lowers scrubbing costs. |

### 8.4 Emerging Technologies and Kinetic Economics

**Electrokinetic Mining (EKM):**
*   **Concept:** Uses electric fields to migrate REE ions through the ore/waste matrix.
*   **Kinetics:** Migration rate is controlled by electrophoretic mobility.
*   **Economics:** A new EKM technique achieved >95% recovery while reducing leaching agent usage by 80% and energy by 60% [cite: 32]. This is a direct result of applying a kinetic force (electric field) to overcome diffusion limitations that plague static leaching.

**Flash Joule Heating (FJH):**
*   **Concept:** Rapid electrical heating of e-waste.
*   **Kinetics:** Millisecond timescale prevents the formation of refractory phases that occur in slow roasting.
*   **Economics:** The drastic reduction in process time (from hours to seconds) and the elimination of water/acid usage results in an 87% energy reduction. This fundamentally changes the OPEX profile from reagent-heavy to electricity-driven [cite: 15].

## 9. Recommendations for Future Economic Modeling

Based on the reviewed literature, future economic assessments of REE waste recovery must integrate kinetic parameters more rigorously:

1.  **Incorporate Dynamic Holdup:** TEAs should not assume instant equilibrium. Capital cost estimates must account for the actual residence time required to reach >95% stage efficiency, which may be significantly longer than theoretical equilibrium times [cite: 8].
2.  **Evaluate Kinetic Separation Routes:** When designing flowsheets for heavy REEs (where thermodynamic separation is hardest), TEAs should evaluate kinetic separation technologies (e.g., redox ligands, CPC) as alternatives to traditional SX cascades [cite: 16, 19].
3.  **Optimize Grinding vs. Leaching:** For waste streams like phosphogypsum and coal ash, the trade-off between comminution costs (to overcome product layer diffusion) and reactor size (residence time) should be mathematically optimized using the Shrinking Core Model [cite: 3, 4].

## 10. References

*   **[cite: 1]** Journal of Civil Engineering and Industrial Building, "Shrinking core model rare earth leaching waste economics," 2025.
*   **[cite: 23]** Minerals, "Techno-Economic Assessment of REE/CM Recovery from AMD," 2021.
*   **[cite: 24]** ResearchGate, "Techno-economic and Life Cycle Analysis for Bioleaching Rare Earth Elements," 2017.
*   **[cite: 6]** ALTA 2024, "Thermodynamic model of solvent extraction (SX) embedded in SysCAD," 2024.
*   **[cite: 27]** NETL, "Economic Extraction, Recovery, and Upgrading of Rare Earth Elements from Coal-Based Resources," 2019.
*   **[cite: 33]** RSC Advances, "Neodymium extraction from decrepitated magnet powder using liquid magnesium," 2023.
*   **[cite: 29]** Separation and Purification Technology, "Kinetics and mechanisms of rare earth elements leaching from end-of-life NdFeB magnets," 2024.
*   **[cite: 7]** Processes, "Simulation of Rare Earth Elements Separation," 2023.
*   **[cite: 8]** ResearchGate, "Dynamic Modeling for the Separation of Rare Earth Elements Using Solvent Extraction," 2017.
*   **[cite: 32]** SciTechDaily, "Revolutionizing Rare Earth Mining: Electrokinetic Technology," 2025.
*   **[cite: 15]** ChemRxiv, "Flash Joule heating (FJH) combined with chlorination," 2025.
*   **[cite: 16, 17, 18]** OSTI/PubMed, "Enhanced Separation of Rare Earth Elements (Separation Factor 261)," 2017.
*   **[cite: 12, 13, 14]** ResearchGate, "Kinetic non-equilibrium separation behavior of rare earths and Al," 2025.
*   **[cite: 3]** ResearchGate, "Leaching Kinetics of Rare Earth Elements from Fire Clay Seam Coal," 2025.
*   **[cite: 4]** Minerals, "Kinetic analysis of the acid leaching results reflected that leaching kinetics of REEs from PG," 2022.
*   **[cite: 10]** FMP TV, "Rainbow Rare Earths launches Johannesburg pilot plant," 2026.
*   **[cite: 11]** Journal of Physics: Conference Series, "Extraction of Yttrium from Nd Hydroxide concentrate by using D2EHPA," 2020.

**Sources:**
1. [ump.edu.my](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdDFR27Wz_iUjVFsLy-wCHAte9wScF6JEzYz0Y6j75WNRd9gHvuj1dLrLBR9zsTBSksEmgpnx24rxGk4Ja8JMbNQMcMp8r9J3Fh-RZ_Uf8gW2q0tGRdK98ihMFMuH2j343QaNswNfPMCs=)
2. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsAHyWgtIrBIHY5GE3CLl4LOIX9-MhFl6bQYAO5WADHskwm4dn_cGVVTM_98izs9a1Ex6pwPyTX2fUS4ADdz1W3PrmINu-zbbSVGYzjJQrxaVQCfUHUu8qsBkpn3k=)
3. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHTqfKxSnfJqiHkIiCoY2HEGRyw9rfmbZK0fcRaf2Ved_-BGBBQc9hFGHjOO2nZDQc6UXHQ-93N8uGNrm1LoMumNYNoO9NJtVR5tFnRVw7Q2aEEiYpyabUzhtr4pyCGyELnQtcrggbt1aMalLqbEO6Y8J99TqqMxCYXiWoiK87SJczpAO0Jsi2CiOes0Lk18QYYDfU0Ns8Waw2xBhuqXbCUtr5VptgKi01lw==)
4. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpNVrQKLXKnHCa_FAI5HCmFWTu1GJEiUjvKKbPH-dVQsLdV8oyZu2YGUnAx4C-fFcJBLUH5jCvdfFQ3FDqKR7-qdCKq_lFlwL6BIz_Uxabc5H3Za6hAfdrOI06WgU=)
5. [uq.edu.au](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPbkE-xT32pWMnl3uci4Hbf_nMGB49DpQMdjiWwkdJq2R4zuLpGT8-hlz6wLKjnU1Nj4LFVVnpky68oTDaj2h6xkSobdtTtUje3kZJVVg5YQx7Ej_dErvQaUwdj4MLmO_FQLK5Tqi69KYswlSsFjKNe4XmxaWTeziL-efm)
6. [cloudfront.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbbC8-g4JFvHTDYsJ0DlAOYYkGeIIVGTujvqv80BWaWY7rkQ6xA9ZtMoiAb2zwX_GpGECiZWRfZvx82S-MkQZ0T_uNpjG5WRXYHDaTyzTKgIsMuUALiSswzpf7-ErI8Q7Qjm7wBvA3durxk25BZbxXBKjk9IT-2GwYTvTjHore4PW1KZbvi62fq_t3-m6bhdibN8jXHw==)
7. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHsiG_Qy3PhXuy0WAZErM1JinLwF0DZNhde03xweBrC9ELrqlMKbTy2xLw0dduH2VDcobO05Z8CGKzBoXrfRHRZoOQQTmG5F5cTUV5IFY-brglaum_N0sLVz47hlaXUME_6jkSDJ0o7Cz0tFGWeBlnfcpmndYidwg-HeBH-uO5zQFBG2Q=)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElyb24Oi8hlaD7u67JKH_sR4CFDCxefmrf7_xr_F3OQ-tNqHXdnW_-hzALNM4uHr9egqrGi6zjm9yhBrAIMaVn-LXJZfCuI54HsSz4DT_riiSf1mk-H2WMsJxDlRBzJNh0nBUjd4PiSMzOgQ6IJ8X6XAKW5UeaUSOwn5W3CplbZluJIJpWIf-1bJaEkH9YVKXY19ot89JZ7AUPdtvNKUq4yNO4nJL-I0iQPa_ovsmtncDjW9zsR1XETS8pcgk1ED0D3yGHzxgM77rAdVrDNZjz1Z5TJPIe0TpX7qh7EMi7ZWRjeq01B8rgKBmVbuNcf9diYBxi3C1GI5wKTTJoDl9NQg==)
9. [osti.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcLfN8EZ14I9Fg3W6ra1sqwEE8V0LrxzU7T9GrkzmNE1u7z8469hOplwMAGQSa_uQvoIdziJHGShv_ZCI8fF7k9X0Q7_NAn1bjOsnjt8aEIZzkVO6pExr0300IK6B1fZ4=)
10. [fmp-tv.co.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLWaToeLAZp5USsp5kXTVm0Y_wYOFhZgPBmfSL0_YdAtze4abTBAwV3n8Bf2Gwf3PeCPAOt25tYXLPP1c_wibJGytMyBz4cC5x2zddK8MxQSB30d6F0zaDKz6V_YgGeQ_j_iEAaW4U_vrXRlcfBYpUhx_vQ6dCGtlqHYJycr1spSEBVWhBEbDKlnKy7dVfd3QVfd_umue6v09nk8rl-th1M-ll7lZD45Tg6Bo=)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWZMz3jSUSD6eWi94GVsGHZtKqxTKz8QXUnCKYHjDCNmSBLWwqsWxneaWWSm4KBSNInT9o9DimCEv-_hS7jzzZ6KJsMGUai2dwdcgbFCVouzTYkdN9PpNNY46cr3gDDtmnzYXYxg1vry35TFdVGo7jn5uTovRCuc_A1eVAHoVWZM1xR0tLTbrAQiRdMYGAsPOb3sll1o0QtbFXiYtOoB-LKdiIlBs_du5724zk)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQbUwf9rE2LDaWSnQeM2JmcA0g8OiiJva7dyOBY5j6SEgQwu88w9dX8pL-OVPoGludr0cNgAx7ajv2D5AgJ4TxHV4zAOC2MjOsnIdis_IrUAifd2rJnaZnTWVG-hSQskT0hvZV4wOoKqBP5GEE2Ue2qQ_t1P1ZV39m-HBkZKO47Ta2DD4zl8lr7MhMvp6QBAzEjS7rNIujhmV2E4WXlY8gWYSUu396BtGYN93bRXSSqfhxIfiud_j0iJ3NnWxaUW8qMwTCirCZibj1P0I1kLa5Y513mP5EsjlFm0tCazFNUuASEH-ugEk=)
13. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5hhAbpu2eJjvrhxPD6wG23RFOsMMj8J42jET_IFj7JGFSfYCEK1onqtJnnjoMiWFyBKMyKpnTK7ia7IzCRAdrxY5jGUAPHf1Zd2OfbmP4FpMEzO8x9IyGoSxM66VB_42Q2C9QQBC60yHFPkUEWXyYO-yO__bw8N3X6cOZtvjdFQ_WWggTPGnlcVeypf-EXNzK-YFc1HStN8F6xu7YdFu2UmlOrOzFP9eY-3Z95ksxFsk4snQDnVd5PeJWzYnHUOH8fl8iIjSysQ5ObWg-R0sfhrO5a-4_FgGis7_WuyunvgxoHE980-dGZE1CttXIHMDRnlvUXwC3fL8tW8A=)
14. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXe8IX_EfuQiQgcP9WTIVJylbLxlNaeIv-CCPi9CpCzVnQFd5gLW_HHRb3_WtuxdlY_E6kMsltKWKZmROOmqSj-PGN5ZyUOQW5dwkUJ8MK05UWCcVR8yYu3Eb7P-PJT--Z233MKfLqP6CspX7fGM7fQjLFcPAD4HxkwUIjdJhh62IVI4EgA54JKQnqwoiJhwzPBOPNj-y-r6UBPtVpU5SOmNLq22n0xCs12AG5P3gitGpSYIYLB3aqhCTDJY6S5MUiwKJsVVw7YWjeCapD7GU07BGFGQ8F3cEkkKD1DK20c9XWamr3mZJxK-9YUhK3WGdU3-2kGwN7JTQ=)
15. [chemrxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECZLJhN1fVpnUuDAJ54TCxzyf0bR1jXkdt1A-KcIiaU892infzY5TeyogARWiG_w-SnRcdPJhOJmPbiBI_JTUQPuOvOrpu3StPAHYnRq487wcFC7S94XKfMk87gzEGrDD90XZFkE5nGE2elYv00uQQKFWutfVOSQzGOls9zp4rAgwHDg==)
16. [osti.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR_3BZQtZBi1vcnHCIIdPqsNf2NfW1Auq1P1CMhoGZjILNH28LQVpcjdbjygxTTcvYfYWYYH8f53lorn1ajafgCXX_pd7aWUE2tAwNwX0fcBd7ITQsYVSrrw==)
17. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAH8MYt1B73WP2bGx16_VwUAMc7TLivAffJ1LOvqQnGW5cw0Ltj79CFa1m2WbrC4wuxWT1EuvTzvwQ1FGfmzG-MwREHpWGIfZ76lWKwJUN5Lq_BaOvr8ldUXcmd-i5EQ==)
18. [osti.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoa5BJePhNBfOKDxSccRR3W1LhlyX9vFYdzG6ec5_RnPy-5_B1iR3tGOKU4vl07WzvgHH6Vzm5OKoQYML6y2tmFL5jYIQrdilWQd6Zxvnm_KqcjPa_6-S1sNwjSd9LUQ==)
19. [rotachrom.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmZ-53OgwXHmXEBbBmdVQM0y-W4Ks9m-Y7cO7srBU2wjd8gqzOlR-O0ZXTN5BEIjhGe0Y1TAJwhrDC3Zs0L3qSTchg3hjmUozbBq6AvxEqJd2FI45TEu0dWg17Wsx0l0XT6qMlkle5s2PNIRfv0wV0VCxZVAgvk9A4GL-g5GcpA8lJGKafUzGIgKxAzYk-BdI8KaycPs2cSnPur6ADx4Fl7pdEiPw57v0UnUM=)
20. [gilson.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEm2PsRv0gqLz8yhLPBqWeXYqIs5NmUnpod2t1je6aLYfKp5gZpv0OO2r1zBJAQa_SV4dOKfOa83qi2gEnQyjcGBKgr4hza29Q-3fOELM3qBqH921RepabQqRvuskLaTKQe3iXDncB8atVn49fLYJZ-mBrDFjhYizFpmiEeQ==)
21. [ijpra.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESKjrTJktNG41c7AJo_CzWiBsbq_qmU6fIh_tq95J3s95QdRY7sMRUzTU3A3vT8CwAPGsat4TccqSk6lWi332LwUeeZAvtsl2_sZM_QDbxEEc1MlwwUpl8mCZNN72CZn3mdh7ckztzJPA=)
22. [osti.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGe1k0jaVdZvQ7pOhyRzVJGWeUmssEQqn-GLp6MWfz-S2njd69MVfQTO3w0DeOEFA6ZNP8qoP-tvpCIEUFe2__YsAoaRMIVF0HetWI3zfTa6Ss5NObzkOQqTE0dF_iMhic=)
23. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGILkw-qe-ln6ujuiGOpg-Lmf2UNRGe5Jo2iHiefMJdcUoJwBBUvH1shG-MxjgD8wc0-8NVAtl_4xs9BU_xHAkwzHQPMX8Qv_tMTwtP8jXRTmBDInVQeiKHNculFGyHpA==)
24. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUg2Gj90XCbmbCddi9JD2nwuGYMwlr_ImscoS3IdNBGcQFWbDioHs9II9M1Ob8mqOvU7reBdbxoK7N1W-a7ClsMNdmtRzC6QCp9IBjlps8-Hagec6FEKwNPtjWqyxI5CJHVt_6lBr536BUIFfJRET2KPRerRZRPRIMsHWObKsrq7XA7-hOHmL2m-MPHmvKgefWurH778f0spUmwLFtO8kPOHTSmAoj0Duzjk2CdEdGaFWB92_sE5Tg27Fkh-qWT0zyEhpG23sCpc57)
25. [saimm.co.za](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1WUn-_xGxBwaCTKXNnj5R1AIfAwe9wKYTbHxtZMAwOcLBPg4sZ4K-YTBxnNfzUZCAu8fdH0UiL4SahmYeh3b_630fp2RzSMTcdYyS81GWOBUyc8mEYQt4T02v17uFSe_mbA72fw==)
26. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVjrffdz6imWjmIBdd_dLavrtOCfPw0nKNAuZk3Wvs1S72_Xgbz0zX1hRq_U7kBJcNdjbMlUFrgypEd2GH8UpTDUDIGmjzGrAvvP4lEVN1Dvz1eUx6WX_yfkKKAiZ4bRhS1AetcV8o5VT8mzMiax0X8RVzew==)
27. [doe.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrlLm4jVzv4_0LLe_VCfwL2wkNT2Rh6DXY8Dxd_U8fa2RfdR3H52O57ab9Ay1eYPb7fLYuSfMBGub5fN8pcK48C8s_1pNFa1d3iPY-JPuNtFWDv7HZs6U4y7yhhejsjJfyGVlpm2WzMsCmTnVw2EfrEr5AaAe96B7i7uBKGI2BHPxOk7SaAqLdGi4w8U03qYvTfRVScnPqUwOxhN9g80hOtmGZf9fxkY-x32JbTqCDad-u)
28. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbRmHoPlKCGkMtS6vo05gV6Qsfdhqlhy6Cu2nlc342l4v2F8yuPf0y2eKESwB85oXKrZ4AETDaebJck0FvA5YS5B0XTI1vRr7O-kfrYc59t0TDTcWQQrL0klUuIB2plOGpGOwHybQhL3MqrBCnmkHVVaMS)
29. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEDzL-eYdtdskb6zjYy0bWvWC6FzTfBpmkFyKGBNughxG2s8pJ3nFHZhGmX52mPPDTUX-g8TYWC1LmL0IeuUUhwzl06OOHc39aICxaQO-u5kp1SPASDZ60iHmHEpasZKKBgnGSjBhKka7ngVZisbSbIslkIXmjjkdeun5Z-ijQezaOV03umUxMURiCfgszMe4gzaHRBnoLerKTLuM6B8Pg_TkVbgVirjZjXX_lFKVCsYlNAJSIqEStCXcnW8PliNuDCaX6jHt_BoFRC-z0qZPMka5j5kCucTJgmY7hie_P0nmpzaMI-A==)
30. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYpQPCIc38O5Ih6IMIcqDovEY56-ckCSwcRov5PbaXRvOPYIXYP-iALXC0xvF_E52UUsYUQWyRQ1dyamUwtR4OfXSOKsvk_I_L2u3jyN4mONC08Bs4IH5AHElfnVDA6hM3SNkmuwz4)
31. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKYtgicT65qFdG3DWb6-pwKlFx8WyOoQ6OeT3v9iyBqDU1L0y5ycWKq3fu3AF4g6-tmaTmkGkF0hJwqTxv9ukmjF576CHoI7b11OFj-mPehPLlkixFzSgOYfoRpREgnQ==)
32. [scitechdaily.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGw6S11A_Abn-LXUIxZ4NQWSi64xhy-0ea30V_wH-YGhycAcDayRnTeqoxLK7TDDmEOcse1wNS13GdRigWouTsaXXJ9IA01EXplwKFUdDiUUXsR4j6vlZE_v9FPUzkNXU26LBlVc6nDcpdaKXVcH6pgAT-te0SqjXYVkg94VjyqUIBiSajcCee9TGVW2f1JeJNj0xbDsDx_zcAfuumjTQ3q)
33. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyFn8r9fVgey9-Mxfmu7bigrjFmfCScuwgoq5JXXsk37iKA2J4eXJlH_XSpmOT-oHa7LJURLn7PCnH-RZUuIkqD2V_irojeB4RPyAWJtawFHuDviBcREn-xS13NyDnNlvkQXV1DqAgRF5CRSA7_G1_tk4hjPfWww==)


## Annotations
Annotation(end_index=3703, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsAHyWgtIrBIHY5GE3CLl4LOIX9-MhFl6bQYAO5WADHskwm4dn_cGVVTM_98izs9a1Ex6pwPyTX2fUS4ADdz1W3PrmINu-zbbSVGYzjJQrxaVQCfUHUu8qsBkpn3k=', start_index=3691)
Annotation(end_index=3703, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdDFR27Wz_iUjVFsLy-wCHAte9wScF6JEzYz0Y6j75WNRd9gHvuj1dLrLBR9zsTBSksEmgpnx24rxGk4Ja8JMbNQMcMp8r9J3Fh-RZ_Uf8gW2q0tGRdK98ihMFMuH2j343QaNswNfPMCs=', start_index=3691)
Annotation(end_index=4334, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHTqfKxSnfJqiHkIiCoY2HEGRyw9rfmbZK0fcRaf2Ved_-BGBBQc9hFGHjOO2nZDQc6UXHQ-93N8uGNrm1LoMumNYNoO9NJtVR5tFnRVw7Q2aEEiYpyabUzhtr4pyCGyELnQtcrggbt1aMalLqbEO6Y8J99TqqMxCYXiWoiK87SJczpAO0Jsi2CiOes0Lk18QYYDfU0Ns8Waw2xBhuqXbCUtr5VptgKi01lw==', start_index=4319)
Annotation(end_index=4334, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpNVrQKLXKnHCa_FAI5HCmFWTu1GJEiUjvKKbPH-dVQsLdV8oyZu2YGUnAx4C-fFcJBLUH5jCvdfFQ3FDqKR7-qdCKq_lFlwL6BIz_Uxabc5H3Za6hAfdrOI06WgU=', start_index=4319)
Annotation(end_index=4334, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdDFR27Wz_iUjVFsLy-wCHAte9wScF6JEzYz0Y6j75WNRd9gHvuj1dLrLBR9zsTBSksEmgpnx24rxGk4Ja8JMbNQMcMp8r9J3Fh-RZ_Uf8gW2q0tGRdK98ihMFMuH2j343QaNswNfPMCs=', start_index=4319)
Annotation(end_index=4545, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHTqfKxSnfJqiHkIiCoY2HEGRyw9rfmbZK0fcRaf2Ved_-BGBBQc9hFGHjOO2nZDQc6UXHQ-93N8uGNrm1LoMumNYNoO9NJtVR5tFnRVw7Q2aEEiYpyabUzhtr4pyCGyELnQtcrggbt1aMalLqbEO6Y8J99TqqMxCYXiWoiK87SJczpAO0Jsi2CiOes0Lk18QYYDfU0Ns8Waw2xBhuqXbCUtr5VptgKi01lw==', start_index=4536)
Annotation(end_index=4958, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPbkE-xT32pWMnl3uci4Hbf_nMGB49DpQMdjiWwkdJq2R4zuLpGT8-hlz6wLKjnU1Nj4LFVVnpky68oTDaj2h6xkSobdtTtUje3kZJVVg5YQx7Ej_dErvQaUwdj4MLmO_FQLK5Tqi69KYswlSsFjKNe4XmxaWTeziL-efm', start_index=4949)
Annotation(end_index=5407, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpNVrQKLXKnHCa_FAI5HCmFWTu1GJEiUjvKKbPH-dVQsLdV8oyZu2YGUnAx4C-fFcJBLUH5jCvdfFQ3FDqKR7-qdCKq_lFlwL6BIz_Uxabc5H3Za6hAfdrOI06WgU=', start_index=5398)
Annotation(end_index=5989, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbbC8-g4JFvHTDYsJ0DlAOYYkGeIIVGTujvqv80BWaWY7rkQ6xA9ZtMoiAb2zwX_GpGECiZWRfZvx82S-MkQZ0T_uNpjG5WRXYHDaTyzTKgIsMuUALiSswzpf7-ErI8Q7Qjm7wBvA3durxk25BZbxXBKjk9IT-2GwYTvTjHore4PW1KZbvi62fq_t3-m6bhdibN8jXHw==', start_index=5980)
Annotation(end_index=6138, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHsiG_Qy3PhXuy0WAZErM1JinLwF0DZNhde03xweBrC9ELrqlMKbTy2xLw0dduH2VDcobO05Z8CGKzBoXrfRHRZoOQQTmG5F5cTUV5IFY-brglaum_N0sLVz47hlaXUME_6jkSDJ0o7Cz0tFGWeBlnfcpmndYidwg-HeBH-uO5zQFBG2Q=', start_index=6126)
Annotation(end_index=6138, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElyb24Oi8hlaD7u67JKH_sR4CFDCxefmrf7_xr_F3OQ-tNqHXdnW_-hzALNM4uHr9egqrGi6zjm9yhBrAIMaVn-LXJZfCuI54HsSz4DT_riiSf1mk-H2WMsJxDlRBzJNh0nBUjd4PiSMzOgQ6IJ8X6XAKW5UeaUSOwn5W3CplbZluJIJpWIf-1bJaEkH9YVKXY19ot89JZ7AUPdtvNKUq4yNO4nJL-I0iQPa_ovsmtncDjW9zsR1XETS8pcgk1ED0D3yGHzxgM77rAdVrDNZjz1Z5TJPIe0TpX7qh7EMi7ZWRjeq01B8rgKBmVbuNcf9diYBxi3C1GI5wKTTJoDl9NQg==', start_index=6126)
Annotation(end_index=6493, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbbC8-g4JFvHTDYsJ0DlAOYYkGeIIVGTujvqv80BWaWY7rkQ6xA9ZtMoiAb2zwX_GpGECiZWRfZvx82S-MkQZ0T_uNpjG5WRXYHDaTyzTKgIsMuUALiSswzpf7-ErI8Q7Qjm7wBvA3durxk25BZbxXBKjk9IT-2GwYTvTjHore4PW1KZbvi62fq_t3-m6bhdibN8jXHw==', start_index=6484)
Annotation(end_index=6809, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElyb24Oi8hlaD7u67JKH_sR4CFDCxefmrf7_xr_F3OQ-tNqHXdnW_-hzALNM4uHr9egqrGi6zjm9yhBrAIMaVn-LXJZfCuI54HsSz4DT_riiSf1mk-H2WMsJxDlRBzJNh0nBUjd4PiSMzOgQ6IJ8X6XAKW5UeaUSOwn5W3CplbZluJIJpWIf-1bJaEkH9YVKXY19ot89JZ7AUPdtvNKUq4yNO4nJL-I0iQPa_ovsmtncDjW9zsR1XETS8pcgk1ED0D3yGHzxgM77rAdVrDNZjz1Z5TJPIe0TpX7qh7EMi7ZWRjeq01B8rgKBmVbuNcf9diYBxi3C1GI5wKTTJoDl9NQg==', start_index=6797)
Annotation(end_index=6809, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcLfN8EZ14I9Fg3W6ra1sqwEE8V0LrxzU7T9GrkzmNE1u7z8469hOplwMAGQSa_uQvoIdziJHGShv_ZCI8fF7k9X0Q7_NAn1bjOsnjt8aEIZzkVO6pExr0300IK6B1fZ4=', start_index=6797)
Annotation(end_index=7611, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLWaToeLAZp5USsp5kXTVm0Y_wYOFhZgPBmfSL0_YdAtze4abTBAwV3n8Bf2Gwf3PeCPAOt25tYXLPP1c_wibJGytMyBz4cC5x2zddK8MxQSB30d6F0zaDKz6V_YgGeQ_j_iEAaW4U_vrXRlcfBYpUhx_vQ6dCGtlqHYJycr1spSEBVWhBEbDKlnKy7dVfd3QVfd_umue6v09nk8rl-th1M-ll7lZD45Tg6Bo=', start_index=7601)
Annotation(end_index=7923, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLWaToeLAZp5USsp5kXTVm0Y_wYOFhZgPBmfSL0_YdAtze4abTBAwV3n8Bf2Gwf3PeCPAOt25tYXLPP1c_wibJGytMyBz4cC5x2zddK8MxQSB30d6F0zaDKz6V_YgGeQ_j_iEAaW4U_vrXRlcfBYpUhx_vQ6dCGtlqHYJycr1spSEBVWhBEbDKlnKy7dVfd3QVfd_umue6v09nk8rl-th1M-ll7lZD45Tg6Bo=', start_index=7913)
Annotation(end_index=8220, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWZMz3jSUSD6eWi94GVsGHZtKqxTKz8QXUnCKYHjDCNmSBLWwqsWxneaWWSm4KBSNInT9o9DimCEv-_hS7jzzZ6KJsMGUai2dwdcgbFCVouzTYkdN9PpNNY46cr3gDDtmnzYXYxg1vry35TFdVGo7jn5uTovRCuc_A1eVAHoVWZM1xR0tLTbrAQiRdMYGAsPOb3sll1o0QtbFXiYtOoB-LKdiIlBs_du5724zk', start_index=8210)
Annotation(end_index=8761, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXe8IX_EfuQiQgcP9WTIVJylbLxlNaeIv-CCPi9CpCzVnQFd5gLW_HHRb3_WtuxdlY_E6kMsltKWKZmROOmqSj-PGN5ZyUOQW5dwkUJ8MK05UWCcVR8yYu3Eb7P-PJT--Z233MKfLqP6CspX7fGM7fQjLFcPAD4HxkwUIjdJhh62IVI4EgA54JKQnqwoiJhwzPBOPNj-y-r6UBPtVpU5SOmNLq22n0xCs12AG5P3gitGpSYIYLB3aqhCTDJY6S5MUiwKJsVVw7YWjeCapD7GU07BGFGQ8F3cEkkKD1DK20c9XWamr3mZJxK-9YUhK3WGdU3-2kGwN7JTQ=', start_index=8743)
Annotation(end_index=8761, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5hhAbpu2eJjvrhxPD6wG23RFOsMMj8J42jET_IFj7JGFSfYCEK1onqtJnnjoMiWFyBKMyKpnTK7ia7IzCRAdrxY5jGUAPHf1Zd2OfbmP4FpMEzO8x9IyGoSxM66VB_42Q2C9QQBC60yHFPkUEWXyYO-yO__bw8N3X6cOZtvjdFQ_WWggTPGnlcVeypf-EXNzK-YFc1HStN8F6xu7YdFu2UmlOrOzFP9eY-3Z95ksxFsk4snQDnVd5PeJWzYnHUOH8fl8iIjSysQ5ObWg-R0sfhrO5a-4_FgGis7_WuyunvgxoHE980-dGZE1CttXIHMDRnlvUXwC3fL8tW8A=', start_index=8743)
Annotation(end_index=8761, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQbUwf9rE2LDaWSnQeM2JmcA0g8OiiJva7dyOBY5j6SEgQwu88w9dX8pL-OVPoGludr0cNgAx7ajv2D5AgJ4TxHV4zAOC2MjOsnIdis_IrUAifd2rJnaZnTWVG-hSQskT0hvZV4wOoKqBP5GEE2Ue2qQ_t1P1ZV39m-HBkZKO47Ta2DD4zl8lr7MhMvp6QBAzEjS7rNIujhmV2E4WXlY8gWYSUu396BtGYN93bRXSSqfhxIfiud_j0iJ3NnWxaUW8qMwTCirCZibj1P0I1kLa5Y513mP5EsjlFm0tCazFNUuASEH-ugEk=', start_index=8743)
Annotation(end_index=8976, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQbUwf9rE2LDaWSnQeM2JmcA0g8OiiJva7dyOBY5j6SEgQwu88w9dX8pL-OVPoGludr0cNgAx7ajv2D5AgJ4TxHV4zAOC2MjOsnIdis_IrUAifd2rJnaZnTWVG-hSQskT0hvZV4wOoKqBP5GEE2Ue2qQ_t1P1ZV39m-HBkZKO47Ta2DD4zl8lr7MhMvp6QBAzEjS7rNIujhmV2E4WXlY8gWYSUu396BtGYN93bRXSSqfhxIfiud_j0iJ3NnWxaUW8qMwTCirCZibj1P0I1kLa5Y513mP5EsjlFm0tCazFNUuASEH-ugEk=', start_index=8966)
Annotation(end_index=9601, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECZLJhN1fVpnUuDAJ54TCxzyf0bR1jXkdt1A-KcIiaU892infzY5TeyogARWiG_w-SnRcdPJhOJmPbiBI_JTUQPuOvOrpu3StPAHYnRq487wcFC7S94XKfMk87gzEGrDD90XZFkE5nGE2elYv00uQQKFWutfVOSQzGOls9zp4rAgwHDg==', start_index=9591)
Annotation(end_index=10534, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAH8MYt1B73WP2bGx16_VwUAMc7TLivAffJ1LOvqQnGW5cw0Ltj79CFa1m2WbrC4wuxWT1EuvTzvwQ1FGfmzG-MwREHpWGIfZ76lWKwJUN5Lq_BaOvr8ldUXcmd-i5EQ==', start_index=10516)
Annotation(end_index=10534, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoa5BJePhNBfOKDxSccRR3W1LhlyX9vFYdzG6ec5_RnPy-5_B1iR3tGOKU4vl07WzvgHH6Vzm5OKoQYML6y2tmFL5jYIQrdilWQd6Zxvnm_KqcjPa_6-S1sNwjSd9LUQ==', start_index=10516)
Annotation(end_index=10534, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR_3BZQtZBi1vcnHCIIdPqsNf2NfW1Auq1P1CMhoGZjILNH28LQVpcjdbjygxTTcvYfYWYYH8f53lorn1ajafgCXX_pd7aWUE2tAwNwX0fcBd7ITQsYVSrrw==', start_index=10516)
Annotation(end_index=10899, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR_3BZQtZBi1vcnHCIIdPqsNf2NfW1Auq1P1CMhoGZjILNH28LQVpcjdbjygxTTcvYfYWYYH8f53lorn1ajafgCXX_pd7aWUE2tAwNwX0fcBd7ITQsYVSrrw==', start_index=10889)
Annotation(end_index=11327, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5hhAbpu2eJjvrhxPD6wG23RFOsMMj8J42jET_IFj7JGFSfYCEK1onqtJnnjoMiWFyBKMyKpnTK7ia7IzCRAdrxY5jGUAPHf1Zd2OfbmP4FpMEzO8x9IyGoSxM66VB_42Q2C9QQBC60yHFPkUEWXyYO-yO__bw8N3X6cOZtvjdFQ_WWggTPGnlcVeypf-EXNzK-YFc1HStN8F6xu7YdFu2UmlOrOzFP9eY-3Z95ksxFsk4snQDnVd5PeJWzYnHUOH8fl8iIjSysQ5ObWg-R0sfhrO5a-4_FgGis7_WuyunvgxoHE980-dGZE1CttXIHMDRnlvUXwC3fL8tW8A=', start_index=11313)
Annotation(end_index=11327, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQbUwf9rE2LDaWSnQeM2JmcA0g8OiiJva7dyOBY5j6SEgQwu88w9dX8pL-OVPoGludr0cNgAx7ajv2D5AgJ4TxHV4zAOC2MjOsnIdis_IrUAifd2rJnaZnTWVG-hSQskT0hvZV4wOoKqBP5GEE2Ue2qQ_t1P1ZV39m-HBkZKO47Ta2DD4zl8lr7MhMvp6QBAzEjS7rNIujhmV2E4WXlY8gWYSUu396BtGYN93bRXSSqfhxIfiud_j0iJ3NnWxaUW8qMwTCirCZibj1P0I1kLa5Y513mP5EsjlFm0tCazFNUuASEH-ugEk=', start_index=11313)
Annotation(end_index=11633, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXe8IX_EfuQiQgcP9WTIVJylbLxlNaeIv-CCPi9CpCzVnQFd5gLW_HHRb3_WtuxdlY_E6kMsltKWKZmROOmqSj-PGN5ZyUOQW5dwkUJ8MK05UWCcVR8yYu3Eb7P-PJT--Z233MKfLqP6CspX7fGM7fQjLFcPAD4HxkwUIjdJhh62IVI4EgA54JKQnqwoiJhwzPBOPNj-y-r6UBPtVpU5SOmNLq22n0xCs12AG5P3gitGpSYIYLB3aqhCTDJY6S5MUiwKJsVVw7YWjeCapD7GU07BGFGQ8F3cEkkKD1DK20c9XWamr3mZJxK-9YUhK3WGdU3-2kGwN7JTQ=', start_index=11623)
Annotation(end_index=12038, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEm2PsRv0gqLz8yhLPBqWeXYqIs5NmUnpod2t1je6aLYfKp5gZpv0OO2r1zBJAQa_SV4dOKfOa83qi2gEnQyjcGBKgr4hza29Q-3fOELM3qBqH921RepabQqRvuskLaTKQe3iXDncB8atVn49fLYJZ-mBrDFjhYizFpmiEeQ==', start_index=12024)
Annotation(end_index=12038, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmZ-53OgwXHmXEBbBmdVQM0y-W4Ks9m-Y7cO7srBU2wjd8gqzOlR-O0ZXTN5BEIjhGe0Y1TAJwhrDC3Zs0L3qSTchg3hjmUozbBq6AvxEqJd2FI45TEu0dWg17Wsx0l0XT6qMlkle5s2PNIRfv0wV0VCxZVAgvk9A4GL-g5GcpA8lJGKafUzGIgKxAzYk-BdI8KaycPs2cSnPur6ADx4Fl7pdEiPw57v0UnUM=', start_index=12024)
Annotation(end_index=12334, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESKjrTJktNG41c7AJo_CzWiBsbq_qmU6fIh_tq95J3s95QdRY7sMRUzTU3A3vT8CwAPGsat4TccqSk6lWi332LwUeeZAvtsl2_sZM_QDbxEEc1MlwwUpl8mCZNN72CZn3mdh7ckztzJPA=', start_index=12320)
Annotation(end_index=12334, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEm2PsRv0gqLz8yhLPBqWeXYqIs5NmUnpod2t1je6aLYfKp5gZpv0OO2r1zBJAQa_SV4dOKfOa83qi2gEnQyjcGBKgr4hza29Q-3fOELM3qBqH921RepabQqRvuskLaTKQe3iXDncB8atVn49fLYJZ-mBrDFjhYizFpmiEeQ==', start_index=12320)
Annotation(end_index=12782, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGe1k0jaVdZvQ7pOhyRzVJGWeUmssEQqn-GLp6MWfz-S2njd69MVfQTO3w0DeOEFA6ZNP8qoP-tvpCIEUFe2__YsAoaRMIVF0HetWI3zfTa6Ss5NObzkOQqTE0dF_iMhic=', start_index=12772)
Annotation(end_index=13298, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGILkw-qe-ln6ujuiGOpg-Lmf2UNRGe5Jo2iHiefMJdcUoJwBBUvH1shG-MxjgD8wc0-8NVAtl_4xs9BU_xHAkwzHQPMX8Qv_tMTwtP8jXRTmBDInVQeiKHNculFGyHpA==', start_index=13284)
Annotation(end_index=13298, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGe1k0jaVdZvQ7pOhyRzVJGWeUmssEQqn-GLp6MWfz-S2njd69MVfQTO3w0DeOEFA6ZNP8qoP-tvpCIEUFe2__YsAoaRMIVF0HetWI3zfTa6Ss5NObzkOQqTE0dF_iMhic=', start_index=13284)
Annotation(end_index=13547, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUg2Gj90XCbmbCddi9JD2nwuGYMwlr_ImscoS3IdNBGcQFWbDioHs9II9M1Ob8mqOvU7reBdbxoK7N1W-a7ClsMNdmtRzC6QCp9IBjlps8-Hagec6FEKwNPtjWqyxI5CJHVt_6lBr536BUIFfJRET2KPRerRZRPRIMsHWObKsrq7XA7-hOHmL2m-MPHmvKgefWurH778f0spUmwLFtO8kPOHTSmAoj0Duzjk2CdEdGaFWB92_sE5Tg27Fkh-qWT0zyEhpG23sCpc57', start_index=13537)
Annotation(end_index=14041, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpNVrQKLXKnHCa_FAI5HCmFWTu1GJEiUjvKKbPH-dVQsLdV8oyZu2YGUnAx4C-fFcJBLUH5jCvdfFQ3FDqKR7-qdCKq_lFlwL6BIz_Uxabc5H3Za6hAfdrOI06WgU=', start_index=14032)
Annotation(end_index=14204, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1WUn-_xGxBwaCTKXNnj5R1AIfAwe9wKYTbHxtZMAwOcLBPg4sZ4K-YTBxnNfzUZCAu8fdH0UiL4SahmYeh3b_630fp2RzSMTcdYyS81GWOBUyc8mEYQt4T02v17uFSe_mbA72fw==', start_index=14194)
Annotation(end_index=14571, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVjrffdz6imWjmIBdd_dLavrtOCfPw0nKNAuZk3Wvs1S72_Xgbz0zX1hRq_U7kBJcNdjbMlUFrgypEd2GH8UpTDUDIGmjzGrAvvP4lEVN1Dvz1eUx6WX_yfkKKAiZ4bRhS1AetcV8o5VT8mzMiax0X8RVzew==', start_index=14561)
Annotation(end_index=15296, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrlLm4jVzv4_0LLe_VCfwL2wkNT2Rh6DXY8Dxd_U8fa2RfdR3H52O57ab9Ay1eYPb7fLYuSfMBGub5fN8pcK48C8s_1pNFa1d3iPY-JPuNtFWDv7HZs6U4y7yhhejsjJfyGVlpm2WzMsCmTnVw2EfrEr5AaAe96B7i7uBKGI2BHPxOk7SaAqLdGi4w8U03qYvTfRVScnPqUwOxhN9g80hOtmGZf9fxkY-x32JbTqCDad-u', start_index=15286)
Annotation(end_index=15638, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbRmHoPlKCGkMtS6vo05gV6Qsfdhqlhy6Cu2nlc342l4v2F8yuPf0y2eKESwB85oXKrZ4AETDaebJck0FvA5YS5B0XTI1vRr7O-kfrYc59t0TDTcWQQrL0klUuIB2plOGpGOwHybQhL3MqrBCnmkHVVaMS', start_index=15628)
Annotation(end_index=15925, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEDzL-eYdtdskb6zjYy0bWvWC6FzTfBpmkFyKGBNughxG2s8pJ3nFHZhGmX52mPPDTUX-g8TYWC1LmL0IeuUUhwzl06OOHc39aICxaQO-u5kp1SPASDZ60iHmHEpasZKKBgnGSjBhKka7ngVZisbSbIslkIXmjjkdeun5Z-ijQezaOV03umUxMURiCfgszMe4gzaHRBnoLerKTLuM6B8Pg_TkVbgVirjZjXX_lFKVCsYlNAJSIqEStCXcnW8PliNuDCaX6jHt_BoFRC-z0qZPMka5j5kCucTJgmY7hie_P0nmpzaMI-A==', start_index=15915)
Annotation(end_index=16164, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpNVrQKLXKnHCa_FAI5HCmFWTu1GJEiUjvKKbPH-dVQsLdV8oyZu2YGUnAx4C-fFcJBLUH5jCvdfFQ3FDqKR7-qdCKq_lFlwL6BIz_Uxabc5H3Za6hAfdrOI06WgU=', start_index=16155)
Annotation(end_index=16488, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLWaToeLAZp5USsp5kXTVm0Y_wYOFhZgPBmfSL0_YdAtze4abTBAwV3n8Bf2Gwf3PeCPAOt25tYXLPP1c_wibJGytMyBz4cC5x2zddK8MxQSB30d6F0zaDKz6V_YgGeQ_j_iEAaW4U_vrXRlcfBYpUhx_vQ6dCGtlqHYJycr1spSEBVWhBEbDKlnKy7dVfd3QVfd_umue6v09nk8rl-th1M-ll7lZD45Tg6Bo=', start_index=16478)
Annotation(end_index=18520, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpNVrQKLXKnHCa_FAI5HCmFWTu1GJEiUjvKKbPH-dVQsLdV8oyZu2YGUnAx4C-fFcJBLUH5jCvdfFQ3FDqKR7-qdCKq_lFlwL6BIz_Uxabc5H3Za6hAfdrOI06WgU=', start_index=18507)
Annotation(end_index=18520, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYpQPCIc38O5Ih6IMIcqDovEY56-ckCSwcRov5PbaXRvOPYIXYP-iALXC0xvF_E52UUsYUQWyRQ1dyamUwtR4OfXSOKsvk_I_L2u3jyN4mONC08Bs4IH5AHElfnVDA6hM3SNkmuwz4', start_index=18507)
Annotation(end_index=19088, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpNVrQKLXKnHCa_FAI5HCmFWTu1GJEiUjvKKbPH-dVQsLdV8oyZu2YGUnAx4C-fFcJBLUH5jCvdfFQ3FDqKR7-qdCKq_lFlwL6BIz_Uxabc5H3Za6hAfdrOI06WgU=', start_index=19079)
Annotation(end_index=19931, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElyb24Oi8hlaD7u67JKH_sR4CFDCxefmrf7_xr_F3OQ-tNqHXdnW_-hzALNM4uHr9egqrGi6zjm9yhBrAIMaVn-LXJZfCuI54HsSz4DT_riiSf1mk-H2WMsJxDlRBzJNh0nBUjd4PiSMzOgQ6IJ8X6XAKW5UeaUSOwn5W3CplbZluJIJpWIf-1bJaEkH9YVKXY19ot89JZ7AUPdtvNKUq4yNO4nJL-I0iQPa_ovsmtncDjW9zsR1XETS8pcgk1ED0D3yGHzxgM77rAdVrDNZjz1Z5TJPIe0TpX7qh7EMi7ZWRjeq01B8rgKBmVbuNcf9diYBxi3C1GI5wKTTJoDl9NQg==', start_index=19922)
Annotation(end_index=20339, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHsiG_Qy3PhXuy0WAZErM1JinLwF0DZNhde03xweBrC9ELrqlMKbTy2xLw0dduH2VDcobO05Z8CGKzBoXrfRHRZoOQQTmG5F5cTUV5IFY-brglaum_N0sLVz47hlaXUME_6jkSDJ0o7Cz0tFGWeBlnfcpmndYidwg-HeBH-uO5zQFBG2Q=', start_index=20326)
Annotation(end_index=20339, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKYtgicT65qFdG3DWb6-pwKlFx8WyOoQ6OeT3v9iyBqDU1L0y5ycWKq3fu3AF4g6-tmaTmkGkF0hJwqTxv9ukmjF576CHoI7b11OFj-mPehPLlkixFzSgOYfoRpREgnQ==', start_index=20326)
Annotation(end_index=21061, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAH8MYt1B73WP2bGx16_VwUAMc7TLivAffJ1LOvqQnGW5cw0Ltj79CFa1m2WbrC4wuxWT1EuvTzvwQ1FGfmzG-MwREHpWGIfZ76lWKwJUN5Lq_BaOvr8ldUXcmd-i5EQ==', start_index=21047)
Annotation(end_index=21061, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR_3BZQtZBi1vcnHCIIdPqsNf2NfW1Auq1P1CMhoGZjILNH28LQVpcjdbjygxTTcvYfYWYYH8f53lorn1ajafgCXX_pd7aWUE2tAwNwX0fcBd7ITQsYVSrrw==', start_index=21047)
Annotation(end_index=22475, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGw6S11A_Abn-LXUIxZ4NQWSi64xhy-0ea30V_wH-YGhycAcDayRnTeqoxLK7TDDmEOcse1wNS13GdRigWouTsaXXJ9IA01EXplwKFUdDiUUXsR4j6vlZE_v9FPUzkNXU26LBlVc6nDcpdaKXVcH6pgAT-te0SqjXYVkg94VjyqUIBiSajcCee9TGVW2f1JeJNj0xbDsDx_zcAfuumjTQ3q', start_index=22465)
Annotation(end_index=23060, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECZLJhN1fVpnUuDAJ54TCxzyf0bR1jXkdt1A-KcIiaU892infzY5TeyogARWiG_w-SnRcdPJhOJmPbiBI_JTUQPuOvOrpu3StPAHYnRq487wcFC7S94XKfMk87gzEGrDD90XZFkE5nGE2elYv00uQQKFWutfVOSQzGOls9zp4rAgwHDg==', start_index=23050)
Annotation(end_index=23516, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElyb24Oi8hlaD7u67JKH_sR4CFDCxefmrf7_xr_F3OQ-tNqHXdnW_-hzALNM4uHr9egqrGi6zjm9yhBrAIMaVn-LXJZfCuI54HsSz4DT_riiSf1mk-H2WMsJxDlRBzJNh0nBUjd4PiSMzOgQ6IJ8X6XAKW5UeaUSOwn5W3CplbZluJIJpWIf-1bJaEkH9YVKXY19ot89JZ7AUPdtvNKUq4yNO4nJL-I0iQPa_ovsmtncDjW9zsR1XETS8pcgk1ED0D3yGHzxgM77rAdVrDNZjz1Z5TJPIe0TpX7qh7EMi7ZWRjeq01B8rgKBmVbuNcf9diYBxi3C1GI5wKTTJoDl9NQg==', start_index=23507)
Annotation(end_index=23785, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmZ-53OgwXHmXEBbBmdVQM0y-W4Ks9m-Y7cO7srBU2wjd8gqzOlR-O0ZXTN5BEIjhGe0Y1TAJwhrDC3Zs0L3qSTchg3hjmUozbBq6AvxEqJd2FI45TEu0dWg17Wsx0l0XT6qMlkle5s2PNIRfv0wV0VCxZVAgvk9A4GL-g5GcpA8lJGKafUzGIgKxAzYk-BdI8KaycPs2cSnPur6ADx4Fl7pdEiPw57v0UnUM=', start_index=23771)
Annotation(end_index=23785, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR_3BZQtZBi1vcnHCIIdPqsNf2NfW1Auq1P1CMhoGZjILNH28LQVpcjdbjygxTTcvYfYWYYH8f53lorn1ajafgCXX_pd7aWUE2tAwNwX0fcBd7ITQsYVSrrw==', start_index=23771)
Annotation(end_index=24068, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHTqfKxSnfJqiHkIiCoY2HEGRyw9rfmbZK0fcRaf2Ved_-BGBBQc9hFGHjOO2nZDQc6UXHQ-93N8uGNrm1LoMumNYNoO9NJtVR5tFnRVw7Q2aEEiYpyabUzhtr4pyCGyELnQtcrggbt1aMalLqbEO6Y8J99TqqMxCYXiWoiK87SJczpAO0Jsi2CiOes0Lk18QYYDfU0Ns8Waw2xBhuqXbCUtr5VptgKi01lw==', start_index=24056)
Annotation(end_index=24068, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpNVrQKLXKnHCa_FAI5HCmFWTu1GJEiUjvKKbPH-dVQsLdV8oyZu2YGUnAx4C-fFcJBLUH5jCvdfFQ3FDqKR7-qdCKq_lFlwL6BIz_Uxabc5H3Za6hAfdrOI06WgU=', start_index=24056)
Annotation(end_index=24105, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdDFR27Wz_iUjVFsLy-wCHAte9wScF6JEzYz0Y6j75WNRd9gHvuj1dLrLBR9zsTBSksEmgpnx24rxGk4Ja8JMbNQMcMp8r9J3Fh-RZ_Uf8gW2q0tGRdK98ihMFMuH2j343QaNswNfPMCs=', start_index=24096)
Annotation(end_index=24244, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGILkw-qe-ln6ujuiGOpg-Lmf2UNRGe5Jo2iHiefMJdcUoJwBBUvH1shG-MxjgD8wc0-8NVAtl_4xs9BU_xHAkwzHQPMX8Qv_tMTwtP8jXRTmBDInVQeiKHNculFGyHpA==', start_index=24234)
Annotation(end_index=24337, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUg2Gj90XCbmbCddi9JD2nwuGYMwlr_ImscoS3IdNBGcQFWbDioHs9II9M1Ob8mqOvU7reBdbxoK7N1W-a7ClsMNdmtRzC6QCp9IBjlps8-Hagec6FEKwNPtjWqyxI5CJHVt_6lBr536BUIFfJRET2KPRerRZRPRIMsHWObKsrq7XA7-hOHmL2m-MPHmvKgefWurH778f0spUmwLFtO8kPOHTSmAoj0Duzjk2CdEdGaFWB92_sE5Tg27Fkh-qWT0zyEhpG23sCpc57', start_index=24327)
Annotation(end_index=24454, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbbC8-g4JFvHTDYsJ0DlAOYYkGeIIVGTujvqv80BWaWY7rkQ6xA9ZtMoiAb2zwX_GpGECiZWRfZvx82S-MkQZ0T_uNpjG5WRXYHDaTyzTKgIsMuUALiSswzpf7-ErI8Q7Qjm7wBvA3durxk25BZbxXBKjk9IT-2GwYTvTjHore4PW1KZbvi62fq_t3-m6bhdibN8jXHw==', start_index=24445)
Annotation(end_index=24559, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrlLm4jVzv4_0LLe_VCfwL2wkNT2Rh6DXY8Dxd_U8fa2RfdR3H52O57ab9Ay1eYPb7fLYuSfMBGub5fN8pcK48C8s_1pNFa1d3iPY-JPuNtFWDv7HZs6U4y7yhhejsjJfyGVlpm2WzMsCmTnVw2EfrEr5AaAe96B7i7uBKGI2BHPxOk7SaAqLdGi4w8U03qYvTfRVScnPqUwOxhN9g80hOtmGZf9fxkY-x32JbTqCDad-u', start_index=24549)
Annotation(end_index=24687, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyFn8r9fVgey9-Mxfmu7bigrjFmfCScuwgoq5JXXsk37iKA2J4eXJlH_XSpmOT-oHa7LJURLn7PCnH-RZUuIkqD2V_irojeB4RPyAWJtawFHuDviBcREn-xS13NyDnNlvkQXV1DqAgRF5CRSA7_G1_tk4hjPfWww==', start_index=24677)
Annotation(end_index=24805, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEDzL-eYdtdskb6zjYy0bWvWC6FzTfBpmkFyKGBNughxG2s8pJ3nFHZhGmX52mPPDTUX-g8TYWC1LmL0IeuUUhwzl06OOHc39aICxaQO-u5kp1SPASDZ60iHmHEpasZKKBgnGSjBhKka7ngVZisbSbIslkIXmjjkdeun5Z-ijQezaOV03umUxMURiCfgszMe4gzaHRBnoLerKTLuM6B8Pg_TkVbgVirjZjXX_lFKVCsYlNAJSIqEStCXcnW8PliNuDCaX6jHt_BoFRC-z0qZPMka5j5kCucTJgmY7hie_P0nmpzaMI-A==', start_index=24795)
Annotation(end_index=24959, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHsiG_Qy3PhXuy0WAZErM1JinLwF0DZNhde03xweBrC9ELrqlMKbTy2xLw0dduH2VDcobO05Z8CGKzBoXrfRHRZoOQQTmG5F5cTUV5IFY-brglaum_N0sLVz47hlaXUME_6jkSDJ0o7Cz0tFGWeBlnfcpmndYidwg-HeBH-uO5zQFBG2Q=', start_index=24950)
Annotation(end_index=25042, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElyb24Oi8hlaD7u67JKH_sR4CFDCxefmrf7_xr_F3OQ-tNqHXdnW_-hzALNM4uHr9egqrGi6zjm9yhBrAIMaVn-LXJZfCuI54HsSz4DT_riiSf1mk-H2WMsJxDlRBzJNh0nBUjd4PiSMzOgQ6IJ8X6XAKW5UeaUSOwn5W3CplbZluJIJpWIf-1bJaEkH9YVKXY19ot89JZ7AUPdtvNKUq4yNO4nJL-I0iQPa_ovsmtncDjW9zsR1XETS8pcgk1ED0D3yGHzxgM77rAdVrDNZjz1Z5TJPIe0TpX7qh7EMi7ZWRjeq01B8rgKBmVbuNcf9diYBxi3C1GI5wKTTJoDl9NQg==', start_index=25033)
Annotation(end_index=25168, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGw6S11A_Abn-LXUIxZ4NQWSi64xhy-0ea30V_wH-YGhycAcDayRnTeqoxLK7TDDmEOcse1wNS13GdRigWouTsaXXJ9IA01EXplwKFUdDiUUXsR4j6vlZE_v9FPUzkNXU26LBlVc6nDcpdaKXVcH6pgAT-te0SqjXYVkg94VjyqUIBiSajcCee9TGVW2f1JeJNj0xbDsDx_zcAfuumjTQ3q', start_index=25158)
Annotation(end_index=25271, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECZLJhN1fVpnUuDAJ54TCxzyf0bR1jXkdt1A-KcIiaU892infzY5TeyogARWiG_w-SnRcdPJhOJmPbiBI_JTUQPuOvOrpu3StPAHYnRq487wcFC7S94XKfMk87gzEGrDD90XZFkE5nGE2elYv00uQQKFWutfVOSQzGOls9zp4rAgwHDg==', start_index=25261)
Annotation(end_index=25370, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAH8MYt1B73WP2bGx16_VwUAMc7TLivAffJ1LOvqQnGW5cw0Ltj79CFa1m2WbrC4wuxWT1EuvTzvwQ1FGfmzG-MwREHpWGIfZ76lWKwJUN5Lq_BaOvr8ldUXcmd-i5EQ==', start_index=25352)
Annotation(end_index=25370, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoa5BJePhNBfOKDxSccRR3W1LhlyX9vFYdzG6ec5_RnPy-5_B1iR3tGOKU4vl07WzvgHH6Vzm5OKoQYML6y2tmFL5jYIQrdilWQd6Zxvnm_KqcjPa_6-S1sNwjSd9LUQ==', start_index=25352)
Annotation(end_index=25370, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR_3BZQtZBi1vcnHCIIdPqsNf2NfW1Auq1P1CMhoGZjILNH28LQVpcjdbjygxTTcvYfYWYYH8f53lorn1ajafgCXX_pd7aWUE2tAwNwX0fcBd7ITQsYVSrrw==', start_index=25352)
Annotation(end_index=25486, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXe8IX_EfuQiQgcP9WTIVJylbLxlNaeIv-CCPi9CpCzVnQFd5gLW_HHRb3_WtuxdlY_E6kMsltKWKZmROOmqSj-PGN5ZyUOQW5dwkUJ8MK05UWCcVR8yYu3Eb7P-PJT--Z233MKfLqP6CspX7fGM7fQjLFcPAD4HxkwUIjdJhh62IVI4EgA54JKQnqwoiJhwzPBOPNj-y-r6UBPtVpU5SOmNLq22n0xCs12AG5P3gitGpSYIYLB3aqhCTDJY6S5MUiwKJsVVw7YWjeCapD7GU07BGFGQ8F3cEkkKD1DK20c9XWamr3mZJxK-9YUhK3WGdU3-2kGwN7JTQ=', start_index=25468)
Annotation(end_index=25486, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5hhAbpu2eJjvrhxPD6wG23RFOsMMj8J42jET_IFj7JGFSfYCEK1onqtJnnjoMiWFyBKMyKpnTK7ia7IzCRAdrxY5jGUAPHf1Zd2OfbmP4FpMEzO8x9IyGoSxM66VB_42Q2C9QQBC60yHFPkUEWXyYO-yO__bw8N3X6cOZtvjdFQ_WWggTPGnlcVeypf-EXNzK-YFc1HStN8F6xu7YdFu2UmlOrOzFP9eY-3Z95ksxFsk4snQDnVd5PeJWzYnHUOH8fl8iIjSysQ5ObWg-R0sfhrO5a-4_FgGis7_WuyunvgxoHE980-dGZE1CttXIHMDRnlvUXwC3fL8tW8A=', start_index=25468)
Annotation(end_index=25486, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQbUwf9rE2LDaWSnQeM2JmcA0g8OiiJva7dyOBY5j6SEgQwu88w9dX8pL-OVPoGludr0cNgAx7ajv2D5AgJ4TxHV4zAOC2MjOsnIdis_IrUAifd2rJnaZnTWVG-hSQskT0hvZV4wOoKqBP5GEE2Ue2qQ_t1P1ZV39m-HBkZKO47Ta2DD4zl8lr7MhMvp6QBAzEjS7rNIujhmV2E4WXlY8gWYSUu396BtGYN93bRXSSqfhxIfiud_j0iJ3NnWxaUW8qMwTCirCZibj1P0I1kLa5Y513mP5EsjlFm0tCazFNUuASEH-ugEk=', start_index=25468)
Annotation(end_index=25593, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHTqfKxSnfJqiHkIiCoY2HEGRyw9rfmbZK0fcRaf2Ved_-BGBBQc9hFGHjOO2nZDQc6UXHQ-93N8uGNrm1LoMumNYNoO9NJtVR5tFnRVw7Q2aEEiYpyabUzhtr4pyCGyELnQtcrggbt1aMalLqbEO6Y8J99TqqMxCYXiWoiK87SJczpAO0Jsi2CiOes0Lk18QYYDfU0Ns8Waw2xBhuqXbCUtr5VptgKi01lw==', start_index=25584)
Annotation(end_index=25700, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpNVrQKLXKnHCa_FAI5HCmFWTu1GJEiUjvKKbPH-dVQsLdV8oyZu2YGUnAx4C-fFcJBLUH5jCvdfFQ3FDqKR7-qdCKq_lFlwL6BIz_Uxabc5H3Za6hAfdrOI06WgU=', start_index=25691)
Annotation(end_index=25833, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLWaToeLAZp5USsp5kXTVm0Y_wYOFhZgPBmfSL0_YdAtze4abTBAwV3n8Bf2Gwf3PeCPAOt25tYXLPP1c_wibJGytMyBz4cC5x2zddK8MxQSB30d6F0zaDKz6V_YgGeQ_j_iEAaW4U_vrXRlcfBYpUhx_vQ6dCGtlqHYJycr1spSEBVWhBEbDKlnKy7dVfd3QVfd_umue6v09nk8rl-th1M-ll7lZD45Tg6Bo=', start_index=25823)
Annotation(end_index=25923, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWZMz3jSUSD6eWi94GVsGHZtKqxTKz8QXUnCKYHjDCNmSBLWwqsWxneaWWSm4KBSNInT9o9DimCEv-_hS7jzzZ6KJsMGUai2dwdcgbFCVouzTYkdN9PpNNY46cr3gDDtmnzYXYxg1vry35TFdVGo7jn5uTovRCuc_A1eVAHoVWZM1xR0tLTbrAQiRdMYGAsPOb3sll1o0QtbFXiYtOoB-LKdiIlBs_du5724zk', start_index=25913)

## Sources
