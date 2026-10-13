# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 69ec9858 | **Time:** 292.14s | **Cost:** $1.55324
--------------------------------------------------------------------------------

# Biogeochemical Processes in Water Quality Models and Their Impact on Treatment Thresholds Given Baseflow Recharge

### Key Points
*   **Biogeochemical Attenuation as a Regulatory Variable:** Biogeochemical processes, particularly denitrification in the hyporheic zone and groundwater aquifers, significantly alter nutrient loads delivered to surface waters. Models that accurately simulate these attenuation mechanisms can justify adjustments to Total Maximum Daily Loads (TMDLs) and Waste Load Allocations (WLAs), potentially altering treatment thresholds for point source dischargers.
*   **The "Lag Time" Challenge:** Groundwater residence times create a temporal disconnect between land-surface management actions and stream water quality improvements. Research indicates lag times ranging from years to decades (e.g., 20–40 years in parts of the Chesapeake Bay watershed), complicating the establishment of regulatory compliance deadlines and treatment milestones.
*   **Baseflow as a Critical Load Vector:** In many watersheds, groundwater baseflow contributes a majority of the streamflow and nutrient load, particularly during dry periods. Failure to account for baseflow nutrient concentrations—often driven by legacy agricultural inputs—can lead to unattainable treatment thresholds for wastewater facilities, as the "background" load consumes the river's assimilative capacity.
*   **Model Complexity and Legal Implications:** The integration of coupled models (e.g., SWAT-MODFLOW-RT3D) allows for spatially distributed simulation of groundwater-surface water interactions. However, the legal requirement for NPDES permits to address "functional equivalent" discharges (following *County of Maui v. Hawaii Wildlife Fund*) necessitates rigorous modeling of subsurface transport and biogeochemical transformation to define liability and permit limits.

---

## 1. Introduction

The determination of treatment thresholds for wastewater and drinking water systems is intrinsically linked to the predictive capabilities of water quality models. These models must account for the complex interplay between hydrological transport—specifically baseflow recharge—and the biogeochemical transformations that occur within the subsurface and the hyporheic zone. As regulatory frameworks like the Clean Water Act (CWA) in the United States increasingly focus on watershed-scale compliance, the ability to model the fate and transport of nutrients and contaminants across the groundwater-surface water interface (GSI) has become a linchpin of environmental engineering and policy.

Biogeochemical processes, such as denitrification, redox-mediated metal mobilization, and organic carbon cycling, define the "assimilative capacity" of a water body. This capacity dictates the maximum pollutant load a stream can receive while meeting water quality standards. Consequently, errors in modeling these processes—or the omission of groundwater baseflow contributions—can lead to the establishment of treatment thresholds that are either insufficiently protective of aquatic life or technically and economically unachievable for dischargers.

This report provides an exhaustive analysis of how biogeochemical processes within water quality models influence treatment thresholds in the context of baseflow recharge. It examines the mechanistic underpinnings of these processes, the specific modeling platforms used to simulate them (e.g., SWAT, MODFLOW, QUAL2K), and the regulatory implications for TMDLs and NPDES permitting.

---

## 2. Biogeochemical Dynamics in the Groundwater-Surface Water Interface

The interaction between groundwater and surface water is not merely a hydraulic exchange; it is a biogeochemical hotspot where distinct redox gradients drive the transformation of nutrients and contaminants. The accuracy of water quality models depends on their representation of these zones.

### 2.1 The Hyporheic Zone as a Bioreactor
The hyporheic zone (HZ)—the saturated transition zone beneath and alongside the stream bed where surface water and groundwater mix—functions as a natural bioreactor. It is critical for the self-purification capacity of streams [cite: 1].
*   **Redox Zonation:** The HZ is characterized by steep gradients in dissolved oxygen (DO), creating micro-environments that support diverse microbial communities. Upwelling groundwater (often low in DO and high in electron donors) mixes with downwelling surface water (high in DO), facilitating sequential reduction-oxidation reactions [cite: 2, 3].
*   **Denitrification:** This is the primary attenuation mechanism for nitrate ($NO_3^-$) in baseflow. In the absence of oxygen, facultative anaerobes use nitrate as an electron acceptor, converting it to inert dinitrogen gas ($N_2$). Research indicates that biogeochemical processes in the HZ of small streams can substantially influence solute loads, although this effect may diminish in larger rivers where the HZ volume is small relative to total discharge [cite: 2].
*   **Macrophyte Interaction:** In some systems, macrophyte-associated denitrification can account for significant nitrogen removal (e.g., 67% of unexplained attenuation in freshwater ponds), a process often underrepresented in standard models [cite: 4].

### 2.2 Groundwater Attenuation Factors
As groundwater moves through an aquifer toward a surface water body, it undergoes natural attenuation. Quantifying this attenuation is essential for determining the "delivered load" in TMDL calculations.
*   **Magnitude of Attenuation:** Studies in the Chesapeake Bay watershed have demonstrated that groundwater attenuation factors can be substantial. For instance, in the Piedmont region, groundwater attenuation factors for nitrogen ranged from 74% to 92%, with an average of 86% [cite: 5]. This means that only a small fraction of the nitrogen leached from septic systems or agriculture reaches the stream.
*   **Modeling Implications:** If a model assumes 100% transport of leached nitrate to the stream (i.e., an attenuation factor of 0), the calculated load allocation for non-point sources will be artificially high. To compensate and meet water quality standards, regulators might impose unnecessarily strict treatment thresholds on point sources (Wastewater Treatment Plants - WWTPs). Conversely, overestimating attenuation can lead to permit limits that fail to protect water quality.

### 2.3 Legacy Nutrients and Baseflow
Baseflow often carries "legacy" nutrients derived from historical land use.
*   **Lag Times:** Groundwater travel times can range from years to decades. In the Delmarva Peninsula, groundwater return times are such that nitrate currently discharging to streams may reflect fertilizer applications from 20 to 40 years ago [cite: 6, 7].
*   **Biogeochemical Inertia:** In aquifers lacking electron donors (e.g., organic carbon or pyrite), nitrate behaves conservatively and accumulates. At sites like Woburn, Massachusetts, the lack of energy sources to drive reductive dechlorination or denitrification resulted in the persistence of contaminants for extended periods [cite: 8].

---

## 3. Water Quality Modeling Frameworks

To determine treatment thresholds, scientists employ various mathematical models that simulate the coupling of hydrology and biogeochemistry. The sophistication of these models varies from simple 1D steady-state formulations to complex 3D coupled systems.

### 3.1 QUAL2K and QUAL2Kw
QUAL2K is a one-dimensional, steady-state model widely used for TMDL development and waste load allocation.
*   **Process Representation:** It simulates parameters such as DO, BOD, temperature, pH, and nutrients. Crucially, newer versions (QUAL2Kw) include algorithms for hyporheic exchange, sediment oxygen demand (SOD), and denitrification [cite: 9, 10, 11].
*   **Hyporheic Simulation:** The model represents the HZ as a distinct compartment interacting with the main channel. Mass exchange is calculated based on bulk hyporheic exchange flow and concentration gradients [cite: 12].
*   **Limitations:** Being steady-state, QUAL2K assumes constant flow and waste loads, which limits its ability to simulate storm events or seasonal variations in baseflow recharge. However, it remains a primary tool for determining assimilative capacity during critical low-flow conditions (7Q10), which often dictate permit limits [cite: 10, 12].

### 3.2 SWAT and SWAT-MODFLOW
The Soil and Water Assessment Tool (SWAT) is a semi-distributed watershed model often coupled with MODFLOW to handle groundwater dynamics.
*   **Nitrate Transport:** SWAT simulates the nitrogen cycle, including mineralization, nitrification, and denitrification in soil profiles. When coupled with MODFLOW and RT3D (Reactive Transport in 3 Dimensions), it can simulate the 3D movement of nitrate in aquifers and its discharge to streams [cite: 13, 14, 15].
*   **Baseflow Interaction:** The coupled model (SWAT-MODFLOW) exchanges data on recharge and channel seepage on a daily time step. This allows for a more physical representation of how groundwater heads drive baseflow and how riparian evapotranspiration affects water tables [cite: 13, 16].
*   **Reactive Transport (RT3D):** By integrating RT3D, the model can simulate specific chemical reactions within the aquifer, such as the degradation of dissolved organic carbon (DOC) or the denitrification of nitrate, providing a more accurate estimate of the load entering the stream from the subsurface [cite: 17].

### 3.3 HydroGeoSphere (HGS) and Integrated Modeling
Fully integrated surface-subsurface models like HydroGeoSphere allow for the seamless simulation of water and solute transport.
*   **Baseflow Separation:** These models can differentiate between baseflow generated from local, intermediate, and regional flow paths. This distinction is vital because regional flow paths typically have longer residence times and different geochemical signatures compared to local shallow flow [cite: 18].
*   **Topographic Controls:** Research using such mechanistic approaches shows that ignoring lower-order streams in models biases baseflow mean age to be older and alters predicted solute concentrations [cite: 18].

---

## 4. Impact of Biogeochemical Processes on Treatment Thresholds

The primary regulatory mechanism for controlling water pollution is the NPDES permit, which contains effluent limits derived from Water Quality-Based Effluent Limitations (WQBELs). These limits are set to ensure the receiving water body meets its Water Quality Standards (WQS).

### 4.1 The Concept of Assimilative Capacity
Assimilative capacity is the maximum load of a pollutant a water body can receive without violating water quality standards. It is the sum of the Waste Load Allocation (WLA) for point sources, Load Allocation (LA) for non-point sources, and a Margin of Safety (MOS) [cite: 19, 20].

$$ \text{TMDL} = \sum \text{WLA} + \sum \text{LA} + \text{MOS} $$

*   **Biogeochemical Influence:** Biogeochemical processes like denitrification increase the assimilative capacity of a stream. If a model accounts for in-stream and hyporheic denitrification, the calculated remaining capacity for point source discharges increases. This can result in *less stringent* treatment thresholds for WWTPs [cite: 21, 22].
*   **Baseflow Constraints:** Conversely, if baseflow recharge is highly polluted (e.g., high nitrate from legacy agriculture) and biogeochemical attenuation is low (e.g., oxic aquifer conditions), the "background" concentration in the stream will be high. This consumes the available assimilative capacity. In such cases, the WLA for point sources must be reduced, forcing WWTPs to implement advanced treatment technologies (e.g., reverse osmosis or limit-of-technology nutrient removal) to meet extremely low effluent limits [cite: 23].

### 4.2 Defining Treatment Thresholds in Low-Flow Conditions
Treatment thresholds are often determined based on critical low-flow conditions (e.g., 7Q10—the lowest 7-day average flow that occurs once every 10 years).
*   **Baseflow Dominance:** During these periods, streamflow is almost entirely composed of groundwater baseflow [cite: 24, 25]. Therefore, the chemistry of the baseflow dictates the stream's baseline quality.
*   **Dilution Factors:** NPDES permits typically allow for a mixing zone. The dilution factor is calculated using the upstream river flow (baseflow). If baseflow decreases due to extraction or climate change, or if its quality degrades, the dilution factor drops. This necessitates stricter end-of-pipe treatment thresholds for dischargers to maintain the same downstream water quality [cite: 26, 27].
*   **Temperature and pH:** Biogeochemical processes also affect parameters like pH and temperature. For example, groundwater discharge is typically cooler than surface water in summer. Models that fail to account for the cooling effect of baseflow (and hyporheic exchange) may overestimate stream temperatures, leading to unnecessarily strict thermal load limits for industrial dischargers [cite: 28].

### 4.3 The Role of Natural Attenuation Credits
Regulators may allow "natural attenuation" to be counted as a reduction mechanism, effectively treating the environment as part of the treatment train.
*   **Monitored Natural Attenuation (MNA):** In groundwater remediation and some surface water contexts, MNA is an accepted strategy if it can be demonstrated that natural processes (biodegradation, sorption, dispersion) will reduce contaminant concentrations to acceptable levels within a reasonable timeframe [cite: 8, 29].
*   **Verification Requirements:** To grant regulatory credit for attenuation (thereby relaxing active treatment thresholds), models must be backed by empirical data showing stable or shrinking plumes and favorable geochemical indicators (e.g., presence of daughter products, depletion of electron acceptors) [cite: 30].

---

## 5. Regulatory Frameworks and Legal Precedents

The intersection of modeling and law determines how physical data translates into enforceable permits.

### 5.1 TMDL Development and Waste Load Allocations
*   **Daily Load Expressions:** Following the *Friends of the Earth, Inc. v. EPA* decision, TMDLs must be expressed in daily terms. However, models often output annual or seasonal averages. The conversion of these long-term averages into daily limits requires statistical approaches that must account for the variability driven by baseflow and storm events [cite: 31].
*   **Consistency Requirement:** NPDES permit limits must be "consistent with the assumptions and requirements" of the TMDL's WLA. If a TMDL assumes a certain rate of denitrification in the watershed (a biogeochemical assumption), the permit writer must ensure that the effluent limit reflects that assumption. If the natural attenuation is overestimated in the TMDL, the permit limits may be insufficient to protect the water body [cite: 19, 32].

### 5.2 The "Functional Equivalent" Standard
The U.S. Supreme Court decision in *County of Maui v. Hawaii Wildlife Fund* (2020) fundamentally changed the regulation of groundwater discharges.
*   **The Ruling:** The Court held that an NPDES permit is required if a discharge to groundwater is the "functional equivalent" of a direct discharge to navigable waters [cite: 33].
*   **Factors:** Key factors include transit time and distance traveled. Biogeochemical models are now essential to quantify these factors. If a model shows that pollutants are significantly attenuated (chemically transformed) during transit through groundwater, a discharger might argue that the discharge is *not* the functional equivalent of a direct discharge, potentially avoiding the need for an NPDES permit or securing less stringent limits [cite: 33].

### 5.3 "End Result" Limitations
A 2025 Supreme Court ruling (*City and County of San Francisco v. EPA*) limited the EPA's ability to impose generic "end result" limitations (e.g., "discharge must not cause a violation of water quality standards") without specific numeric limits. This forces regulators to rely even more heavily on models to derive precise, numeric effluent limitations based on specific pollutant dynamics, rather than relying on broad narrative prohibitions [cite: 34, 35, 36].

---

## 6. Challenges: Lag Time and Legacy Loads

One of the most significant complications in setting treatment thresholds based on biogeochemical modeling is the temporal lag.

### 6.1 The Lag Time Dilemma
*   **Decadal Delays:** In the Chesapeake Bay, the median age of groundwater discharging to streams is often 10–20 years, with some fractions exceeding 50 years. This means that current stream water quality is a response to land management practices from decades ago [cite: 6, 7].
*   **Regulatory Friction:** TMDLs often set compliance deadlines (e.g., "meet water quality standards by 2025"). However, if the "load" is coming from groundwater with a 30-year residence time, no amount of surface treatment or BMP implementation will achieve immediate compliance.
*   **Impact on Treatment Thresholds:** To compensate for the "uncontrollable" legacy load entering via baseflow, regulators may be forced to ratchet down limits on point sources (WWTPs) to the limit of technology, as these are the only loads that can be reduced instantaneously [cite: 37].

### 6.2 Modeling Lag Times
*   **Groundwater Dating:** Models are increasingly incorporating groundwater age distributions (using tracers like tritium or CFCs) to simulate these lags. Studies show that ignoring these lags leads to unrealistic expectations for water quality improvement [cite: 6].
*   **NMBR Models:** Nitrogen Mass-Balance Regression (NMBR) models coupled with groundwater flow models have been used to forecast future nitrogen delivery under different reduction scenarios, demonstrating that several decades are required to see the full effects of current BMPs [cite: 6].

---

## 7. Case Studies

### 7.1 Chesapeake Bay: Nitrogen and Baseflow
The Chesapeake Bay Program utilizes a complex suite of models (Watershed Model, Estuarine Model).
*   **Issue:** Early models underestimated the lag time of nutrient transport in groundwater.
*   **Adjustment:** USGS studies quantified residence times and attenuation factors (e.g., 86% attenuation in Piedmont).
*   **Outcome:** This understanding shifted the focus toward addressing legacy loads and refined the expectations for when TMDL goals would be met. It also highlighted the disproportionate burden placed on wastewater plants to achieve immediate reductions while non-point source improvements lagged [cite: 5, 6, 7, 37].

### 7.2 Urban Streams and LID: Sindun Stream
*   **Context:** Urban streams often suffer from low baseflow and high pollutant concentrations.
*   **Modeling:** A SWAT-MODFLOW application in the Sindun Stream watershed evaluated Low Impact Development (LID) techniques.
*   **Result:** LID increased baseflow by 43% and reduced Total Phosphorus (T-P) by 41% during dry periods. By enhancing recharge and baseflow, the concentration of pollutants was diluted, effectively improving the water quality without changing the treatment thresholds of upstream facilities [cite: 24].

### 7.3 Nitrate in the San Joaquin and Arkansas River Basins
*   **Modeling:** Application of SWAT-MODFLOW-RT3D.
*   **Findings:** The model quantified nitrate exchange between the aquifer and stream. It showed that denitrification and other removal processes in the subsurface significantly reduced the nitrate load recharging the stream. This type of modeling is critical for establishing "baseline" conditions for nitrate TMDLs in agriculturally intensive valleys [cite: 13, 15].

---

## 8. Future Directions and Gaps

Despite advances, significant gaps remain in the ability of models to inform treatment thresholds accurately.

*   **Coupling Gaps:** Many models still struggle to fully couple atmospheric, surface, and subsurface domains. Specifically, the feedback loop where changing groundwater quality affects surface water treatment costs is often modeled in isolation [cite: 38, 39].
*   **Data Scarcity:** High-resolution data on hyporheic exchange rates and subsurface biogeochemical coefficients (e.g., denitrification rates) are rare. Models often rely on literature values, introducing high uncertainty [cite: 2, 38].
*   **Emerging Contaminants:** Modeling the biogeochemical fate of Contaminants of Emerging Concern (CECs) in baseflow is a major frontier. Current models lack the kinetic data to predict how these compounds transform in the GSI, making it difficult to set appropriate treatment thresholds [cite: 38].

---

## 9. Conclusion

Biogeochemical processes in water quality models are not merely academic variables; they are decisive factors in the economic and regulatory landscape of water management. By governing the rate at which pollutants are removed (attenuation) or delayed (lag time) in the subsurface, these processes determine the **effective load** delivered to surface waters via baseflow.

*   **High Attenuation:** If models demonstrate high rates of natural denitrification in the hyporheic zone or aquifer, the assimilative capacity of the receiving water is effectively higher. This can allow for **higher (less stringent) treatment thresholds** for point source dischargers, provided the natural capacity is not overwhelmed.
*   **Low Attenuation / High Legacy Load:** Conversely, if models reveal that baseflow is a major source of conserved pollutants (e.g., legacy nitrate) with long lag times, the assimilative capacity available for current dischargers is severely restricted. This scenario necessitates **lower (stricter) treatment thresholds**, often pushing wastewater treatment facilities toward costly technological upgrades to compensate for the uncontrollable background load.

Ultimately, the integration of robust biogeochemical algorithms into coupled surface-subsurface models (like SWAT-MODFLOW-RT3D) provides the scientific defensibility required for modern regulatory frameworks. These models allow regulators to distinguish between current and legacy sources, justify natural attenuation credits, and establish treatment thresholds that are both protective of the environment and grounded in physical reality.

---

### References
[cite: 38, 39] - Gaps in water quality modeling and research needs.
[cite: 40] - Hydrogeochemical models for drinking water treatment.
[cite: 18] - Topographic controls on baseflow and solute concentration.
[cite: 23] - Importance of groundwater baseflow in TMDLs.
[cite: 1, 2] - Hyporheic zone biogeochemistry and self-purification.
[cite: 3] - Hyporheic zone impacts on stream chemistry and mining waste.
[cite: 24] - LID effects on baseflow and water quality (SWAT-MODFLOW).
[cite: 9, 10] - QUAL2K model applications and capabilities.
[cite: 21, 41] - Assimilative capacity and water quality modeling.
[cite: 19, 32] - EPA guidance on TMDLs, WLAs, and NPDES permits.
[cite: 31] - Daily load expressions in TMDLs.
[cite: 8, 29] - Monitored Natural Attenuation (MNA).
[cite: 34, 35] - Supreme Court rulings on NPDES permits (San Francisco v. EPA).
[cite: 33] - Supreme Court ruling on functional equivalent discharge (Maui).
[cite: 13, 15] - SWAT-MODFLOW-RT3D model development and application.
[cite: 5] - Groundwater attenuation factors in Chesapeake Bay.
[cite: 6, 37] - Lag times in groundwater and Chesapeake Bay modeling.
[cite: 7] - Groundwater lag times by geologic region.
[cite: 20] - TMDL modeling categories and loading capacity.
[cite: 4] - Macrophyte-associated denitrification.
[cite: 12] - Hyporheic exchange in QUAL2Kw.
[cite: 28] - Temperature and hyporheic exchange in TMDLs.
[cite: 17] - SWAT-MODFLOW-RT3D for DOC simulation.
[cite: 16] - Nitrate fate and transport using coupled models.

**Sources:**
1. [igb-berlin.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErqpETxJZfvK2oSr0gt9zbSxPtEkFvLBc9SGyOLfCdLmu7LRKItQbvsCje1JmhwhDIBt48Cp6D3PJSOe66t2l8S5pp2HlhizwqXlHKUIUe801_eeSdUBxk5tGjtyZlRcoH1ObbnB7jn5E=)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwOg52kZ8qrPHWxH7n5k54_qoVecuxB2R4qEc94wrT_VJxaibNaRT-CbClY2Zt7M1zfCPtZwKnER8F6pYvYJUAvllFuyrvLMfbD22V9yPV1LwXxdT78a3R2KsBoNHT-ZGBfulFNQHS7SUYPIpdz7b6ufqINvYso4scjwLD7jtm8pWWczfkqvHZvTAJB1Ax0bbX3Sup3_BOnj4=)
3. [stonybrook.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHw8ZWltsIM9CnR0AaHQvy0ySZNST2KXQ4R22oyRZJlPzdPsDhf7bxPYrfCkFaDxoaK7oWwe1XYU1iNqBFXXEQIhJLnU21Mf3OcIll1sWOzxeqibWaSxZ-_G4zXdW-1X9K7XoJ6TKR7OhbDN1basiTEpiPyb3__c04U5CfrabUw4GgS5JbA-MNXwnWIeNJVMxp_AiFnYCCvHg==)
4. [umassd.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIlu10RJxKd9P5dA3yfM15A6Xh8eh2O9XB5WOEGV1s_uEQrnbUCwXvqq_STSbO2nlRIjh88xEZj64GFR4hXzkXXKvUaqzRHIV7UWh0ZyXgBSAhHsKazCsWOI-0fUf0pvzvakBHLaNCIE3x-qBeGhZFMm0_f5Yj_YJ7tXp8OLgwZknoN3d5DVbnw9uW2vpR6hMW1bqPbrytcLK6vZ2nwkYZfnyOtz82ww==)
5. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHy3NuNk5PGem51cD0X_N-ojCqBBgdkxrg4k01nyTx6XDXoekzxChCGpdXT70RLlT44XzoHxuX0urIvkwldQ92o9q3hliwY8ehpV7HqVtjViZD3hVaDa763WMw1p-kzXpUgJKLIrvLnWIO6PbrIQDkkUUfzz3fE-ISf_Zpdp4QbdPrIKOT875wuInvqJAnNtS3uE-SslfNdIbvlUlg1QTAqg476cD5w37HjxECxT-pDcD-52VlJwxs1yrvVRIu8lxQbpkujwMbEIrp0TZoCDVdpiTfXHKLblAXvOQMXJIe-imemfZQ=)
6. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcgLoVsxWh0imhJSmX-bqgt9pXuXVczirWsqdkJXlOYa5qpUlcOSSIbR8uRLb0clFBs3ZyUWiLk-GSdjVv5urvqHv5eVmxjLjn8JfjeYbv5_JngFckGxzGUbJSyQCC6DI=)
7. [arcgis.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTTS-0B7djNGN6HTsHVGoM42Ya7GlKCOdYGvu3epnSXM-Xl-dsul2_omgbl5MrXVib1UFHFFitPbagDX3TKqv7okIUo0kaNxveGEmdESRnh8EhFj31NxPNlNEPFq9Z79T-7YbxFa7m5zCOyxO_V_nBRZgLpSYvMHfZPWA=)
8. [usgs.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGkT-Z5kp6jxGAGgTLXF6WaEKzxH_5MuznoTljOuFRehDPyzzJd0pFJ1GjMBR6ZLqcMEk_ajk-z3E_rf1mGgIw5t_zx-lksh2iqR_A4OyRZL1lPQK4L_1jYnIBbEaXCqZ2Sj-KUNWnuy43)
9. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAIqn6on1u63E2RiVRD-i_HJYi6-IGzSWiCMyue1Wa8RR9M1tw8JjkXgXeP6CyxIfbLX9hDmTPC8A8m5lvQk9cH_WHT2zT5esBnPLE3gowY6-o5HD2OX1zg6R4i6FyteiuBvM2J8NUBeqPWCc4nSAddLCRhgTSJZRVxxnFd3VUq4fg4kumO8Bt8YS3icozQw==)
10. [ijsat.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIFOGxTICFsxZpZv5QI_OMglHvOldFZ1VbUhpbf_T6CAIK1Q---f1PvcJhoQ2g6xccS0udQSlxVjYeHpKK2n5wLTqlh67_9KvytpXf6hTdP4gk1eV1jHGq02Cnyj6zNxNkag==)
11. [wa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmMRRmZyfnxEioR-tWWs1fT_IBjV5z64umrwi6Et4DGNGsW19X5-o-Zc7__J2V6kV-WMYgeAJgZMXuqYw7McLjQjWd-d8oHm3hum6qwGzYdfeITUTGigQL7VgU3d31M2qimLPmOcp7w8eXAHxWgixI7d0EkA==)
12. [scirp.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqFuWE2EX7MqL3YGQMDcBTyhe0CEG4Uw4PTh9dTaJhUATUVa6RTz0W_4NIDkHjz5ohVjECdi2TmH-B3iOg2LdlFb3AJRDdKS9gleAHUezxZZfkKRcTIFK4w3saN3O6CB8qs15GAPN5Kx1nvYxzSHxna8g=)
13. [copernicus.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNRak46RCSKv0C8KSXUcJKl0vZwB-9BSJtF-tIoYgMwgVWYCF_budlnxzZkV3PCu6UEPX0BqNavj51NlwRFXc33leGJkK4PJ-04OQ17E5toM47tnGEj_xkIUF5DL2YFGI78zlNXd-AkRsLhwjdCf4N38gW1ZwblSHFxIF9ApNRFdqF1L2DMMEOYnSyLF0TLw==)
14. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVRR53ZxVhQtDUtWv9f40VPPjJfwqy3eZTdkb3CeVDBmhrzIYsBBIHomo8F7MxKsgQGloGRVm_eu9UMZl-rPnq1JyBuV65OAMh41IjeqZIPZwX8lCRCGW78MecYAXY)
15. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDe0Cau5eUKbAySDsc_sE6NXmklitanqbfaFfnEb83LIc9TL-pudRM0-maO6V4zz_ppRFucNAK3w-RYtDdMx9qSSPHpXZvauUmG8WkwyMcKL5D1s5YlfHnPIcgZvgX9w==)
16. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFU-zcHVXX_duNRZh_P6txdHWAwuk9JwPz697l8sRJf5MePK9oF7VHj2Pi8t73r2vgqjp37u8UlZ8JULl3ZsmGkbbZ9G8oU6e_FCwW1ORIP6DwMiFVdw_MdF3nWtSZM6w==)
17. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHowvqnn5juaGLzJrtVhsQc4bZ6GTn8yR0NrylHebnr1VAi6FEOuaJBv1lDAkI3KzB05Q6JkhX0bPgqXSsBpsNJ5vyE74WBtyZwo7qfYKz0nWIXGSDjYqsxeOMVbwCznQ==)
18. [nmsu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqz_n8cFDfpoyoZphV-fN4naSqjsWRuQAvDfA9GV5b44idXMXQcxejk217yLFIGlUr4v6QTj6NSpwx91sw_2hsJezl_aqPNVI3wNpN0To4Z0tHo_tpplNZxaM9To7lJmnjFZn1_VF2IvA7IH7nS6VJSofEv78vkwntalRZsQq7BsVZ3A==)
19. [epa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtQxiZeXkDefgPPBnBTnDEfa6bEhm7EKVzQ5m2HdDpJTZ4YoyaQYsDbfY5HvuKS2CfSy7U4ppzxt7GgaQK9bkjzvSU4Y-J9gJ83E-e56yNRO6p7y6t4e2UBDTWr5nD7mndKmyZqkiF1p66UfvHaIA3qdTLIWart8xtNKjT2otnWtaJwHbmNSvxG4gp)
20. [oregon.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGufhlfDWdMsXKsZvYPsVhj4NTB9gxECocKIUDkQppOtF50sLtujeGZXgZBKo-0xnaPi-qJ10MWI6vWpV-h0-looq1jq0YnBmG4c7L85KReZw7_7rPJi0ZtE_zzLonCj31nJLro9g58dj95ayELeno=)
21. [iwaponline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVwVGvdZz-4hLmIbVkUqws1xngqoXNBJWMflJ-1Rvcbbyx7iXKjGQRLSCMQhB8SonQszbsMP4kxUEn2SPetZIfgbjLm_1EhB2cPh0YUWCuUV2DDJkXyDQARwq1UwFIKsNUJ2Q0uxExn38Zb3m1lPCnm129OixjhNoNhKOjS8uK9S0V4ihIe0L3YdBnJMtgBSQmW-sTXZv7So6YJw==)
22. [gjesm.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGg-ngOzbkLXSI_9NTZjc_-mK4r-MFXCkbBvZOgnUshu2Nz7b3OIbOQlkKT1s189JWtXLAkIbtHJaD1Aq1Ts-zQGLEsoswZ1B9qn8RgOvpaZPK8rjjw2bVDYownL7SOQlRDa8ksU8Ly2WGG2ctAnsvARJQGPL5XBu73juCkGVL)
23. [wellntel.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAMSh7Xg8GS-2jIgeWenHb6GrIFp2XW3FUo7NUo1qcv3iVvHA5UhdxoCR56r8N4T5zWBrsPJv1cx1uigaPp2miHND9kXEpaj5yZEPs7kgvY4maKo6hiNBYJSD_FsRHQuHDHmDoN8iIr_z0ldapJ7cOiUW0f92qq8uFLFz9XMpUU8MzsmZ-i1XDTMBaLZCBefI4O1VFJBW_iG7DFA==)
24. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWG6ufGrFuPh3OsI8-97gzhaVMxNJ9On6ScFzkg930R0OzX45BPrYgqUqFQIe0oqf0GmsatSPGR0bFkoJi6owvWmQmNuJib2suKw1iTLlW3zSP1V1n8ByK8rYFcgl5ag==)
25. [uwaterloo.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHg08Ql1sLT1EzFbXxr1MPoJubq4BY4BtW6gMcb1gQdeB7N_Jdzm8aojFz9aFXYKlah212a0F7QtHVBu1nxBIAD4NS66dUGFtbNaCDj1ocY73UHondUrdg-fxfNMyradcZxSQjQd9Xn4RUG9Iel9QavPojU4JDTlmshSQI1RQ==)
26. [pca.state.mn.us](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxtumFQXMgDlgWJYHQOv1SLuNW6AGTp4pmDOkDgc2R9K7qAmlUgzHTr5mnQOYBK_VhrNVWstUkQxoOATyBcMbxB6q1mRK0aEeBvZaGEuD9AEPq53S-lYLQ2wTZHFPvtVgmVNTGDEaraagkPaGn2-nYU4ck0JY=)
27. [pa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFaLYtE5tQx8SC3fh2-C87qi8Dm7qaF0ZjDhqm_cQrbDCWIXvYTjQ4aFNpTsHC8qMbBDbigm7B__bgsXlmYYdi29ooDiu1kFTG_X5JLDcaq3dOUlkzkvBbLU0RRSxgczZobPKlSTq9Z0WiJYA0AEkQkeI1k9bEVVk5_RG0_vJ3pvA5rxM2iRL-dOexbPbomNNBnXQe3J83Ep8824-pK6foYY9dWInDj8_bcDv4etlIn6OMwuv2M7bAxvlL16a08HIkeFgn146yfARNx3Z5GFvGpRQ57PJITNEbxk68TBqofnFjXjlT-x4uGTNmJG7GXZ2NYmlv7RK3ozg59JkbEwAO7b4VcSvvd6MzIoxZSBPuxaWunl2thzTHMmD57O5KxUdW1L7CkiicNLHQmdCGePaIztMpkaZbXsQDq0tHcopdcI1QgPEbubnTlGW06nBV-5R3QM0VlYq4XvCidVjd_5xlFx3sQjucbZO2F6mVgKNaTdL-H5uDUukeIBskVifCjDYGbXshUFYlqlqWUIOJqxTbekaJvKSM-GQ7l0umZwvUeFpBlTNkL)
28. [wa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGpH7HHbv6P95jwEnYzWpMc3JmOj87-f2HuF_cm6axpRL8LcT3E9PthpJaNs6t0t2jV98i3KJvz8QOxFeXHSC7o2OBNc6gbMXA3tcT_KRSrxOu90D_7e85gJ5LE3sdi7kR2FpSHz12Mdne3waDClTJJ6fJGg==)
29. [mo.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtl9embS4qLFvsRTn92OQuN-yccrJPjuRv46BmmsGnpthvQcMeJBkvUpWLEkqGAJtnjHPktyUT_sNFzke4wz2qc2p2RdB_tL1uIFAy8Uew7aArocZ0aaQXZv7HQvkFNmLypkLeIubB6OC4tobmo7n8uyuIM3SXIAiKlOEuWc7YW1nyxWEjVcEuJUAkFzGjGxxPWould8oTF_HVD0YK6h5P8fhqWkqpDs0mKtG_983eAhJC5MCLbOD8jCKBBfXSPP1ZVX3lrJHkEfnZEG4_)
30. [ct.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI6dScDkcOsMoPAhJZDlI9jHSTaNs6SLD9lifb32nQq87_apnYSC7icPGJ5jZP0sCY93ym0XYuFbVMhtZ0A2gFRfd0vuBr9bknno0RbDN_Mx1AhoZiAFK9rscVj5noH0ISZSTRLYcGg901C7JYrEbdyX9Mmv1Vd8llzDqxtvMGTpcZlsButPDo7famHD7OuF_zdKgk-hVMHg==)
31. [pca.state.mn.us](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUx2nX8n7CM794hpjg4kBs9POQf4T6WI-Lk6-v84Cwj0dRj_kza-MLvHp_Eo_xOCgkbcNN_drVSUirVDGih5po8EtToWpwdjKxRlZmrF2kz5GZniixwMcCjbAuQzXTloZsFQ4mv5SbyzJxtw8W4vCWFmVK)
32. [epa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGv62BGPOzIqk96ihNPeWXmV0dyaTh91DmAk4Q8AxOpftsDoHO7L6m8Q3qtTZvSZyKOBzhNoqSbLFbBfClCvkum0IwnIUT4LsmgwmmeO6c3YR1hLleb0nr90E2Smsff83udqC5KAWqLQAcE5kJrpg==)
33. [baileyglasser.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE551IUwDt5paos8mwOWhRrXP7GArfTRYQ8M9FBQ0kpRfkW3JHIetK1RXvmoOAqgpHkIJgGB0Whl56qXGj2F9xiadSJ8xW51JAeAupbS-_P9tpjKJdQS-NfjklBYDX6NRhA-zNRpRnm9KwOr8i20i8DgYBUFJEd7tCx1y5FKIs6itVKOxjWJKN7ve7y12Up0rJtHjofj7hE5El6DQ==)
34. [boardmanclark.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVv8OOJjilGjy6BAhMJIp9qAAuTPW2SfjpBKvGwSXdcduJ8QHVYBW63tgkUT1ZWAfV6ZpKaJNJF4vxNRDHXZQ1ltQvH5Ce4-T4C5oQmxUAO6_6Uzc9PwDYKoRLyUAvHe6a1IJzd6PgWvIWgto_xM7-MjogZPhUOzWynW-ssRcm2V3fCBCeAZUrurPs1PuFuabIwMBNCTxmlnf3RgatpX5fPM0oXo7y1XXF2F_m3Exw0BZtq6y7dlKZ5jjSWF11TXOBCdD2WQ==)
35. [tonkon.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP8kqAJgJzEKvBsaEeO1JmpulzZKbZI4-jYCdxOZVRUXIH2idjjMiCecfE5UYTy4em521v9Gb_qK_CNS-z-iAT90nUtKSyBvZr8M0JPUp-F29i_SK32kVhorNjvdrby0X0RBqHwVQFjtFHB7lrxC47gudGb174bOL0RrigwNwZ37ZonJBSONflkFTfBZ2J6eXF1oa0niguvZ8G979nZ95XazkLnZgcSwMocg==)
36. [supremecourt.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXmBwLF8voNpJkizziyizwFsJXfVAFrV2kSwB1m7HoEDqQOjfQdSTPCEtJ2AWRXCXbR7LCAMdwbQOawtFKyJkp3GO65i5qBbEr7_h0bOJHf4o7epN-FCI3893QdRypMYlWn2SbDlJx8K9GWWDOcd6Lb_-fReGVgp8-9bfyY8kSwF2Jf4x9JxYcGEJYWxj4NDjMGsycoJyQdc8lly9U6LVbtEY7px1gAr4=)
37. [chesapeake.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTOFCNL5F-qDzC3pKaFokKKWts38b8nLA5H7JupzHRKomthfCyD8rHJGmdwlAPWvLVvCdhUsgR1TdF06vWHc0QeE2RRSwMY4MNqeONeVuNkfag-5n35euk5ExAOUK5hZv_i-nbREBJcw==)
38. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8rtNchYbzEESVNFbAMXKY2_uCdVJ30xFMJ4nRrgMmWD6zPv50_pze6CwPi2rKV56Xz-ztFxfVAenBaVzbU0R9Fmm996XsbCGQsAvFkSczJ1AWSS_zK-oBYVrFkBo1)
39. [epa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEH6sxL5JEjQVTp--nI2HSXVaZMfy0O5Aun5DbZWqT52_7STcXBGylu7GmclkBoEnA7htcHPW3UeuXxY6JWP6k-32nxKjpC7l5MPECyTb5A1RPXizRtGPvsrjxqzzk3MTocadpczCazjLqDFmPLcsczH6gxVDyCaL4dQOZoDA==)
40. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeho5LSDdUoiYJp3rRz0IST6HcaCCXPwDy0vozZg28mJd6XPh_jeuykPdiDTfUMvflaH7DgjaoDbku5p4a5Qom_YYLn7l5MMVCQI5N5zX9Doq56iJ_E3smQ1zddTmU-w==)
41. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUHM3ykn-7KZ84yjio8nfc-3fCMYjoTBulsJtS1xSEdHRbMC8Gw-DsBtDtbFIbW5nbVkmyLD2W_mC0OjW1jQxWH54QU5CXtmfE1o1ncZU_aHKIJ955TY4fCowyM1W5D5wuLK62jLwl2dSW7vhMNUc00_gcxt3XUVh8CxA9qs1a7RvJMUljmm9XlpPY9seSazXRA3fYnz6y7ynpGJFq5-4aXKhijWp8mAA1lCkp)


## Annotations
Annotation(end_index=4189, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErqpETxJZfvK2oSr0gt9zbSxPtEkFvLBc9SGyOLfCdLmu7LRKItQbvsCje1JmhwhDIBt48Cp6D3PJSOe66t2l8S5pp2HlhizwqXlHKUIUe801_eeSdUBxk5tGjtyZlRcoH1ObbnB7jn5E=', start_index=4180)
Annotation(end_index=4541, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwOg52kZ8qrPHWxH7n5k54_qoVecuxB2R4qEc94wrT_VJxaibNaRT-CbClY2Zt7M1zfCPtZwKnER8F6pYvYJUAvllFuyrvLMfbD22V9yPV1LwXxdT78a3R2KsBoNHT-ZGBfulFNQHS7SUYPIpdz7b6ufqINvYso4scjwLD7jtm8pWWczfkqvHZvTAJB1Ax0bbX3Sup3_BOnj4=', start_index=4529)
Annotation(end_index=4541, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHw8ZWltsIM9CnR0AaHQvy0ySZNST2KXQ4R22oyRZJlPzdPsDhf7bxPYrfCkFaDxoaK7oWwe1XYU1iNqBFXXEQIhJLnU21Mf3OcIll1sWOzxeqibWaSxZ-_G4zXdW-1X9K7XoJ6TKR7OhbDN1basiTEpiPyb3__c04U5CfrabUw4GgS5JbA-MNXwnWIeNJVMxp_AiFnYCCvHg==', start_index=4529)
Annotation(end_index=5013, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwOg52kZ8qrPHWxH7n5k54_qoVecuxB2R4qEc94wrT_VJxaibNaRT-CbClY2Zt7M1zfCPtZwKnER8F6pYvYJUAvllFuyrvLMfbD22V9yPV1LwXxdT78a3R2KsBoNHT-ZGBfulFNQHS7SUYPIpdz7b6ufqINvYso4scjwLD7jtm8pWWczfkqvHZvTAJB1Ax0bbX3Sup3_BOnj4=', start_index=5004)
Annotation(end_index=5268, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIlu10RJxKd9P5dA3yfM15A6Xh8eh2O9XB5WOEGV1s_uEQrnbUCwXvqq_STSbO2nlRIjh88xEZj64GFR4hXzkXXKvUaqzRHIV7UWh0ZyXgBSAhHsKazCsWOI-0fUf0pvzvakBHLaNCIE3x-qBeGhZFMm0_f5Yj_YJ7tXp8OLgwZknoN3d5DVbnw9uW2vpR6hMW1bqPbrytcLK6vZ2nwkYZfnyOtz82ww==', start_index=5259)
Annotation(end_index=5803, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHy3NuNk5PGem51cD0X_N-ojCqBBgdkxrg4k01nyTx6XDXoekzxChCGpdXT70RLlT44XzoHxuX0urIvkwldQ92o9q3hliwY8ehpV7HqVtjViZD3hVaDa763WMw1p-kzXpUgJKLIrvLnWIO6PbrIQDkkUUfzz3fE-ISf_Zpdp4QbdPrIKOT875wuInvqJAnNtS3uE-SslfNdIbvlUlg1QTAqg476cD5w37HjxECxT-pDcD-52VlJwxs1yrvVRIu8lxQbpkujwMbEIrp0TZoCDVdpiTfXHKLblAXvOQMXJIe-imemfZQ=', start_index=5794)
Annotation(end_index=6778, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTTS-0B7djNGN6HTsHVGoM42Ya7GlKCOdYGvu3epnSXM-Xl-dsul2_omgbl5MrXVib1UFHFFitPbagDX3TKqv7okIUo0kaNxveGEmdESRnh8EhFj31NxPNlNEPFq9Z79T-7YbxFa7m5zCOyxO_V_nBRZgLpSYvMHfZPWA=', start_index=6766)
Annotation(end_index=6778, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcgLoVsxWh0imhJSmX-bqgt9pXuXVczirWsqdkJXlOYa5qpUlcOSSIbR8uRLb0clFBs3ZyUWiLk-GSdjVv5urvqHv5eVmxjLjn8JfjeYbv5_JngFckGxzGUbJSyQCC6DI=', start_index=6766)
Annotation(end_index=7121, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGkT-Z5kp6jxGAGgTLXF6WaEKzxH_5MuznoTljOuFRehDPyzzJd0pFJ1GjMBR6ZLqcMEk_ajk-z3E_rf1mGgIw5t_zx-lksh2iqR_A4OyRZL1lPQK4L_1jYnIBbEaXCqZ2Sj-KUNWnuy43', start_index=7112)
Annotation(end_index=7813, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIFOGxTICFsxZpZv5QI_OMglHvOldFZ1VbUhpbf_T6CAIK1Q---f1PvcJhoQ2g6xccS0udQSlxVjYeHpKK2n5wLTqlh67_9KvytpXf6hTdP4gk1eV1jHGq02Cnyj6zNxNkag==', start_index=7796)
Annotation(end_index=7813, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmMRRmZyfnxEioR-tWWs1fT_IBjV5z64umrwi6Et4DGNGsW19X5-o-Zc7__J2V6kV-WMYgeAJgZMXuqYw7McLjQjWd-d8oHm3hum6qwGzYdfeITUTGigQL7VgU3d31M2qimLPmOcp7w8eXAHxWgixI7d0EkA==', start_index=7796)
Annotation(end_index=7813, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAIqn6on1u63E2RiVRD-i_HJYi6-IGzSWiCMyue1Wa8RR9M1tw8JjkXgXeP6CyxIfbLX9hDmTPC8A8m5lvQk9cH_WHT2zT5esBnPLE3gowY6-o5HD2OX1zg6R4i6FyteiuBvM2J8NUBeqPWCc4nSAddLCRhgTSJZRVxxnFd3VUq4fg4kumO8Bt8YS3icozQw==', start_index=7796)
Annotation(end_index=8038, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqFuWE2EX7MqL3YGQMDcBTyhe0CEG4Uw4PTh9dTaJhUATUVa6RTz0W_4NIDkHjz5ohVjECdi2TmH-B3iOg2LdlFb3AJRDdKS9gleAHUezxZZfkKRcTIFK4w3saN3O6CB8qs15GAPN5Kx1nvYxzSHxna8g=', start_index=8028)
Annotation(end_index=8387, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIFOGxTICFsxZpZv5QI_OMglHvOldFZ1VbUhpbf_T6CAIK1Q---f1PvcJhoQ2g6xccS0udQSlxVjYeHpKK2n5wLTqlh67_9KvytpXf6hTdP4gk1eV1jHGq02Cnyj6zNxNkag==', start_index=8373)
Annotation(end_index=8387, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqFuWE2EX7MqL3YGQMDcBTyhe0CEG4Uw4PTh9dTaJhUATUVa6RTz0W_4NIDkHjz5ohVjECdi2TmH-B3iOg2LdlFb3AJRDdKS9gleAHUezxZZfkKRcTIFK4w3saN3O6CB8qs15GAPN5Kx1nvYxzSHxna8g=', start_index=8373)
Annotation(end_index=8875, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNRak46RCSKv0C8KSXUcJKl0vZwB-9BSJtF-tIoYgMwgVWYCF_budlnxzZkV3PCu6UEPX0BqNavj51NlwRFXc33leGJkK4PJ-04OQ17E5toM47tnGEj_xkIUF5DL2YFGI78zlNXd-AkRsLhwjdCf4N38gW1ZwblSHFxIF9ApNRFdqF1L2DMMEOYnSyLF0TLw==', start_index=8857)
Annotation(end_index=8875, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDe0Cau5eUKbAySDsc_sE6NXmklitanqbfaFfnEb83LIc9TL-pudRM0-maO6V4zz_ppRFucNAK3w-RYtDdMx9qSSPHpXZvauUmG8WkwyMcKL5D1s5YlfHnPIcgZvgX9w==', start_index=8857)
Annotation(end_index=8875, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVRR53ZxVhQtDUtWv9f40VPPjJfwqy3eZTdkb3CeVDBmhrzIYsBBIHomo8F7MxKsgQGloGRVm_eu9UMZl-rPnq1JyBuV65OAMh41IjeqZIPZwX8lCRCGW78MecYAXY', start_index=8857)
Annotation(end_index=9167, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNRak46RCSKv0C8KSXUcJKl0vZwB-9BSJtF-tIoYgMwgVWYCF_budlnxzZkV3PCu6UEPX0BqNavj51NlwRFXc33leGJkK4PJ-04OQ17E5toM47tnGEj_xkIUF5DL2YFGI78zlNXd-AkRsLhwjdCf4N38gW1ZwblSHFxIF9ApNRFdqF1L2DMMEOYnSyLF0TLw==', start_index=9153)
Annotation(end_index=9167, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFU-zcHVXX_duNRZh_P6txdHWAwuk9JwPz697l8sRJf5MePK9oF7VHj2Pi8t73r2vgqjp37u8UlZ8JULl3ZsmGkbbZ9G8oU6e_FCwW1ORIP6DwMiFVdw_MdF3nWtSZM6w==', start_index=9153)
Annotation(end_index=9486, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHowvqnn5juaGLzJrtVhsQc4bZ6GTn8yR0NrylHebnr1VAi6FEOuaJBv1lDAkI3KzB05Q6JkhX0bPgqXSsBpsNJ5vyE74WBtyZwo7qfYKz0nWIXGSDjYqsxeOMVbwCznQ==', start_index=9476)
Annotation(end_index=9978, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqz_n8cFDfpoyoZphV-fN4naSqjsWRuQAvDfA9GV5b44idXMXQcxejk217yLFIGlUr4v6QTj6NSpwx91sw_2hsJezl_aqPNVI3wNpN0To4Z0tHo_tpplNZxaM9To7lJmnjFZn1_VF2IvA7IH7nS6VJSofEv78vkwntalRZsQq7BsVZ3A==', start_index=9968)
Annotation(end_index=10193, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqz_n8cFDfpoyoZphV-fN4naSqjsWRuQAvDfA9GV5b44idXMXQcxejk217yLFIGlUr4v6QTj6NSpwx91sw_2hsJezl_aqPNVI3wNpN0To4Z0tHo_tpplNZxaM9To7lJmnjFZn1_VF2IvA7IH7nS6VJSofEv78vkwntalRZsQq7BsVZ3A==', start_index=10183)
Annotation(end_index=10871, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtQxiZeXkDefgPPBnBTnDEfa6bEhm7EKVzQ5m2HdDpJTZ4YoyaQYsDbfY5HvuKS2CfSy7U4ppzxt7GgaQK9bkjzvSU4Y-J9gJ83E-e56yNRO6p7y6t4e2UBDTWr5nD7mndKmyZqkiF1p66UfvHaIA3qdTLIWart8xtNKjT2otnWtaJwHbmNSvxG4gp', start_index=10857)
Annotation(end_index=10871, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGufhlfDWdMsXKsZvYPsVhj4NTB9gxECocKIUDkQppOtF50sLtujeGZXgZBKo-0xnaPi-qJ10MWI6vWpV-h0-looq1jq0YnBmG4c7L85KReZw7_7rPJi0ZtE_zzLonCj31nJLro9g58dj95ayELeno=', start_index=10857)
Annotation(end_index=11288, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVwVGvdZz-4hLmIbVkUqws1xngqoXNBJWMflJ-1Rvcbbyx7iXKjGQRLSCMQhB8SonQszbsMP4kxUEn2SPetZIfgbjLm_1EhB2cPh0YUWCuUV2DDJkXyDQARwq1UwFIKsNUJ2Q0uxExn38Zb3m1lPCnm129OixjhNoNhKOjS8uK9S0V4ihIe0L3YdBnJMtgBSQmW-sTXZv7So6YJw==', start_index=11274)
Annotation(end_index=11288, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGg-ngOzbkLXSI_9NTZjc_-mK4r-MFXCkbBvZOgnUshu2Nz7b3OIbOQlkKT1s189JWtXLAkIbtHJaD1Aq1Ts-zQGLEsoswZ1B9qn8RgOvpaZPK8rjjw2bVDYownL7SOQlRDa8ksU8Ly2WGG2ctAnsvARJQGPL5XBu73juCkGVL', start_index=11274)
Annotation(end_index=11827, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAMSh7Xg8GS-2jIgeWenHb6GrIFp2XW3FUo7NUo1qcv3iVvHA5UhdxoCR56r8N4T5zWBrsPJv1cx1uigaPp2miHND9kXEpaj5yZEPs7kgvY4maKo6hiNBYJSD_FsRHQuHDHmDoN8iIr_z0ldapJ7cOiUW0f92qq8uFLFz9XMpUU8MzsmZ-i1XDTMBaLZCBefI4O1VFJBW_iG7DFA==', start_index=11817)
Annotation(end_index=12176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWG6ufGrFuPh3OsI8-97gzhaVMxNJ9On6ScFzkg930R0OzX45BPrYgqUqFQIe0oqf0GmsatSPGR0bFkoJi6owvWmQmNuJib2suKw1iTLlW3zSP1V1n8ByK8rYFcgl5ag==', start_index=12162)
Annotation(end_index=12176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHg08Ql1sLT1EzFbXxr1MPoJubq4BY4BtW6gMcb1gQdeB7N_Jdzm8aojFz9aFXYKlah212a0F7QtHVBu1nxBIAD4NS66dUGFtbNaCDj1ocY73UHondUrdg-fxfNMyradcZxSQjQd9Xn4RUG9Iel9QavPojU4JDTlmshSQI1RQ==', start_index=12162)
Annotation(end_index=12660, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFaLYtE5tQx8SC3fh2-C87qi8Dm7qaF0ZjDhqm_cQrbDCWIXvYTjQ4aFNpTsHC8qMbBDbigm7B__bgsXlmYYdi29ooDiu1kFTG_X5JLDcaq3dOUlkzkvBbLU0RRSxgczZobPKlSTq9Z0WiJYA0AEkQkeI1k9bEVVk5_RG0_vJ3pvA5rxM2iRL-dOexbPbomNNBnXQe3J83Ep8824-pK6foYY9dWInDj8_bcDv4etlIn6OMwuv2M7bAxvlL16a08HIkeFgn146yfARNx3Z5GFvGpRQ57PJITNEbxk68TBqofnFjXjlT-x4uGTNmJG7GXZ2NYmlv7RK3ozg59JkbEwAO7b4VcSvvd6MzIoxZSBPuxaWunl2thzTHMmD57O5KxUdW1L7CkiicNLHQmdCGePaIztMpkaZbXsQDq0tHcopdcI1QgPEbubnTlGW06nBV-5R3QM0VlYq4XvCidVjd_5xlFx3sQjucbZO2F6mVgKNaTdL-H5uDUukeIBskVifCjDYGbXshUFYlqlqWUIOJqxTbekaJvKSM-GQ7l0umZwvUeFpBlTNkL', start_index=12646)
Annotation(end_index=12660, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxtumFQXMgDlgWJYHQOv1SLuNW6AGTp4pmDOkDgc2R9K7qAmlUgzHTr5mnQOYBK_VhrNVWstUkQxoOATyBcMbxB6q1mRK0aEeBvZaGEuD9AEPq53S-lYLQ2wTZHFPvtVgmVNTGDEaraagkPaGn2-nYU4ck0JY=', start_index=12646)
Annotation(end_index=13063, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGpH7HHbv6P95jwEnYzWpMc3JmOj87-f2HuF_cm6axpRL8LcT3E9PthpJaNs6t0t2jV98i3KJvz8QOxFeXHSC7o2OBNc6gbMXA3tcT_KRSrxOu90D_7e85gJ5LE3sdi7kR2FpSHz12Mdne3waDClTJJ6fJGg==', start_index=13053)
Annotation(end_index=13590, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtl9embS4qLFvsRTn92OQuN-yccrJPjuRv46BmmsGnpthvQcMeJBkvUpWLEkqGAJtnjHPktyUT_sNFzke4wz2qc2p2RdB_tL1uIFAy8Uew7aArocZ0aaQXZv7HQvkFNmLypkLeIubB6OC4tobmo7n8uyuIM3SXIAiKlOEuWc7YW1nyxWEjVcEuJUAkFzGjGxxPWould8oTF_HVD0YK6h5P8fhqWkqpDs0mKtG_983eAhJC5MCLbOD8jCKBBfXSPP1ZVX3lrJHkEfnZEG4_', start_index=13577)
Annotation(end_index=13590, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGkT-Z5kp6jxGAGgTLXF6WaEKzxH_5MuznoTljOuFRehDPyzzJd0pFJ1GjMBR6ZLqcMEk_ajk-z3E_rf1mGgIw5t_zx-lksh2iqR_A4OyRZL1lPQK4L_1jYnIBbEaXCqZ2Sj-KUNWnuy43', start_index=13577)
Annotation(end_index=13911, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI6dScDkcOsMoPAhJZDlI9jHSTaNs6SLD9lifb32nQq87_apnYSC7icPGJ5jZP0sCY93ym0XYuFbVMhtZ0A2gFRfd0vuBr9bknno0RbDN_Mx1AhoZiAFK9rscVj5noH0ISZSTRLYcGg901C7JYrEbdyX9Mmv1Vd8llzDqxtvMGTpcZlsButPDo7famHD7OuF_zdKgk-hVMHg==', start_index=13901)
Annotation(end_index=14492, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUx2nX8n7CM794hpjg4kBs9POQf4T6WI-Lk6-v84Cwj0dRj_kza-MLvHp_Eo_xOCgkbcNN_drVSUirVDGih5po8EtToWpwdjKxRlZmrF2kz5GZniixwMcCjbAuQzXTloZsFQ4mv5SbyzJxtw8W4vCWFmVK', start_index=14482)
Annotation(end_index=14940, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtQxiZeXkDefgPPBnBTnDEfa6bEhm7EKVzQ5m2HdDpJTZ4YoyaQYsDbfY5HvuKS2CfSy7U4ppzxt7GgaQK9bkjzvSU4Y-J9gJ83E-e56yNRO6p7y6t4e2UBDTWr5nD7mndKmyZqkiF1p66UfvHaIA3qdTLIWart8xtNKjT2otnWtaJwHbmNSvxG4gp', start_index=14926)
Annotation(end_index=14940, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGv62BGPOzIqk96ihNPeWXmV0dyaTh91DmAk4Q8AxOpftsDoHO7L6m8Q3qtTZvSZyKOBzhNoqSbLFbBfClCvkum0IwnIUT4LsmgwmmeO6c3YR1hLleb0nr90E2Smsff83udqC5KAWqLQAcE5kJrpg==', start_index=14926)
Annotation(end_index=15316, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE551IUwDt5paos8mwOWhRrXP7GArfTRYQ8M9FBQ0kpRfkW3JHIetK1RXvmoOAqgpHkIJgGB0Whl56qXGj2F9xiadSJ8xW51JAeAupbS-_P9tpjKJdQS-NfjklBYDX6NRhA-zNRpRnm9KwOr8i20i8DgYBUFJEd7tCx1y5FKIs6itVKOxjWJKN7ve7y12Up0rJtHjofj7hE5El6DQ==', start_index=15306)
Annotation(end_index=15777, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE551IUwDt5paos8mwOWhRrXP7GArfTRYQ8M9FBQ0kpRfkW3JHIetK1RXvmoOAqgpHkIJgGB0Whl56qXGj2F9xiadSJ8xW51JAeAupbS-_P9tpjKJdQS-NfjklBYDX6NRhA-zNRpRnm9KwOr8i20i8DgYBUFJEd7tCx1y5FKIs6itVKOxjWJKN7ve7y12Up0rJtHjofj7hE5El6DQ==', start_index=15767)
Annotation(end_index=16276, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXmBwLF8voNpJkizziyizwFsJXfVAFrV2kSwB1m7HoEDqQOjfQdSTPCEtJ2AWRXCXbR7LCAMdwbQOawtFKyJkp3GO65i5qBbEr7_h0bOJHf4o7epN-FCI3893QdRypMYlWn2SbDlJx8K9GWWDOcd6Lb_-fReGVgp8-9bfyY8kSwF2Jf4x9JxYcGEJYWxj4NDjMGsycoJyQdc8lly9U6LVbtEY7px1gAr4=', start_index=16258)
Annotation(end_index=16276, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP8kqAJgJzEKvBsaEeO1JmpulzZKbZI4-jYCdxOZVRUXIH2idjjMiCecfE5UYTy4em521v9Gb_qK_CNS-z-iAT90nUtKSyBvZr8M0JPUp-F29i_SK32kVhorNjvdrby0X0RBqHwVQFjtFHB7lrxC47gudGb174bOL0RrigwNwZ37ZonJBSONflkFTfBZ2J6eXF1oa0niguvZ8G979nZ95XazkLnZgcSwMocg==', start_index=16258)
Annotation(end_index=16276, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVv8OOJjilGjy6BAhMJIp9qAAuTPW2SfjpBKvGwSXdcduJ8QHVYBW63tgkUT1ZWAfV6ZpKaJNJF4vxNRDHXZQ1ltQvH5Ce4-T4C5oQmxUAO6_6Uzc9PwDYKoRLyUAvHe6a1IJzd6PgWvIWgto_xM7-MjogZPhUOzWynW-ssRcm2V3fCBCeAZUrurPs1PuFuabIwMBNCTxmlnf3RgatpX5fPM0oXo7y1XXF2F_m3Exw0BZtq6y7dlKZ5jjSWF11TXOBCdD2WQ==', start_index=16258)
Annotation(end_index=16768, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTTS-0B7djNGN6HTsHVGoM42Ya7GlKCOdYGvu3epnSXM-Xl-dsul2_omgbl5MrXVib1UFHFFitPbagDX3TKqv7okIUo0kaNxveGEmdESRnh8EhFj31NxPNlNEPFq9Z79T-7YbxFa7m5zCOyxO_V_nBRZgLpSYvMHfZPWA=', start_index=16756)
Annotation(end_index=16768, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcgLoVsxWh0imhJSmX-bqgt9pXuXVczirWsqdkJXlOYa5qpUlcOSSIbR8uRLb0clFBs3ZyUWiLk-GSdjVv5urvqHv5eVmxjLjn8JfjeYbv5_JngFckGxzGUbJSyQCC6DI=', start_index=16756)
Annotation(end_index=17342, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTOFCNL5F-qDzC3pKaFokKKWts38b8nLA5H7JupzHRKomthfCyD8rHJGmdwlAPWvLVvCdhUsgR1TdF06vWHc0QeE2RRSwMY4MNqeONeVuNkfag-5n35euk5ExAOUK5hZv_i-nbREBJcw==', start_index=17332)
Annotation(end_index=17640, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcgLoVsxWh0imhJSmX-bqgt9pXuXVczirWsqdkJXlOYa5qpUlcOSSIbR8uRLb0clFBs3ZyUWiLk-GSdjVv5urvqHv5eVmxjLjn8JfjeYbv5_JngFckGxzGUbJSyQCC6DI=', start_index=17631)
Annotation(end_index=17933, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcgLoVsxWh0imhJSmX-bqgt9pXuXVczirWsqdkJXlOYa5qpUlcOSSIbR8uRLb0clFBs3ZyUWiLk-GSdjVv5urvqHv5eVmxjLjn8JfjeYbv5_JngFckGxzGUbJSyQCC6DI=', start_index=17924)
Annotation(end_index=18638, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTOFCNL5F-qDzC3pKaFokKKWts38b8nLA5H7JupzHRKomthfCyD8rHJGmdwlAPWvLVvCdhUsgR1TdF06vWHc0QeE2RRSwMY4MNqeONeVuNkfag-5n35euk5ExAOUK5hZv_i-nbREBJcw==', start_index=18619)
Annotation(end_index=18638, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTTS-0B7djNGN6HTsHVGoM42Ya7GlKCOdYGvu3epnSXM-Xl-dsul2_omgbl5MrXVib1UFHFFitPbagDX3TKqv7okIUo0kaNxveGEmdESRnh8EhFj31NxPNlNEPFq9Z79T-7YbxFa7m5zCOyxO_V_nBRZgLpSYvMHfZPWA=', start_index=18619)
Annotation(end_index=18638, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcgLoVsxWh0imhJSmX-bqgt9pXuXVczirWsqdkJXlOYa5qpUlcOSSIbR8uRLb0clFBs3ZyUWiLk-GSdjVv5urvqHv5eVmxjLjn8JfjeYbv5_JngFckGxzGUbJSyQCC6DI=', start_index=18619)
Annotation(end_index=18638, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHy3NuNk5PGem51cD0X_N-ojCqBBgdkxrg4k01nyTx6XDXoekzxChCGpdXT70RLlT44XzoHxuX0urIvkwldQ92o9q3hliwY8ehpV7HqVtjViZD3hVaDa763WMw1p-kzXpUgJKLIrvLnWIO6PbrIQDkkUUfzz3fE-ISf_Zpdp4QbdPrIKOT875wuInvqJAnNtS3uE-SslfNdIbvlUlg1QTAqg476cD5w37HjxECxT-pDcD-52VlJwxs1yrvVRIu8lxQbpkujwMbEIrp0TZoCDVdpiTfXHKLblAXvOQMXJIe-imemfZQ=', start_index=18619)
Annotation(end_index=19214, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWG6ufGrFuPh3OsI8-97gzhaVMxNJ9On6ScFzkg930R0OzX45BPrYgqUqFQIe0oqf0GmsatSPGR0bFkoJi6owvWmQmNuJib2suKw1iTLlW3zSP1V1n8ByK8rYFcgl5ag==', start_index=19204)
Annotation(end_index=19698, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNRak46RCSKv0C8KSXUcJKl0vZwB-9BSJtF-tIoYgMwgVWYCF_budlnxzZkV3PCu6UEPX0BqNavj51NlwRFXc33leGJkK4PJ-04OQ17E5toM47tnGEj_xkIUF5DL2YFGI78zlNXd-AkRsLhwjdCf4N38gW1ZwblSHFxIF9ApNRFdqF1L2DMMEOYnSyLF0TLw==', start_index=19684)
Annotation(end_index=19698, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDe0Cau5eUKbAySDsc_sE6NXmklitanqbfaFfnEb83LIc9TL-pudRM0-maO6V4zz_ppRFucNAK3w-RYtDdMx9qSSPHpXZvauUmG8WkwyMcKL5D1s5YlfHnPIcgZvgX9w==', start_index=19684)
Annotation(end_index=20112, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEH6sxL5JEjQVTp--nI2HSXVaZMfy0O5Aun5DbZWqT52_7STcXBGylu7GmclkBoEnA7htcHPW3UeuXxY6JWP6k-32nxKjpC7l5MPECyTb5A1RPXizRtGPvsrjxqzzk3MTocadpczCazjLqDFmPLcsczH6gxVDyCaL4dQOZoDA==', start_index=20098)
Annotation(end_index=20112, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8rtNchYbzEESVNFbAMXKY2_uCdVJ30xFMJ4nRrgMmWD6zPv50_pze6CwPi2rKV56Xz-ztFxfVAenBaVzbU0R9Fmm996XsbCGQsAvFkSczJ1AWSS_zK-oBYVrFkBo1', start_index=20098)
Annotation(end_index=20351, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8rtNchYbzEESVNFbAMXKY2_uCdVJ30xFMJ4nRrgMmWD6zPv50_pze6CwPi2rKV56Xz-ztFxfVAenBaVzbU0R9Fmm996XsbCGQsAvFkSczJ1AWSS_zK-oBYVrFkBo1', start_index=20338)
Annotation(end_index=20351, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwOg52kZ8qrPHWxH7n5k54_qoVecuxB2R4qEc94wrT_VJxaibNaRT-CbClY2Zt7M1zfCPtZwKnER8F6pYvYJUAvllFuyrvLMfbD22V9yPV1LwXxdT78a3R2KsBoNHT-ZGBfulFNQHS7SUYPIpdz7b6ufqINvYso4scjwLD7jtm8pWWczfkqvHZvTAJB1Ax0bbX3Sup3_BOnj4=', start_index=20338)
Annotation(end_index=20653, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8rtNchYbzEESVNFbAMXKY2_uCdVJ30xFMJ4nRrgMmWD6zPv50_pze6CwPi2rKV56Xz-ztFxfVAenBaVzbU0R9Fmm996XsbCGQsAvFkSczJ1AWSS_zK-oBYVrFkBo1', start_index=20643)
Annotation(end_index=22332, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEH6sxL5JEjQVTp--nI2HSXVaZMfy0O5Aun5DbZWqT52_7STcXBGylu7GmclkBoEnA7htcHPW3UeuXxY6JWP6k-32nxKjpC7l5MPECyTb5A1RPXizRtGPvsrjxqzzk3MTocadpczCazjLqDFmPLcsczH6gxVDyCaL4dQOZoDA==', start_index=22318)
Annotation(end_index=22332, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8rtNchYbzEESVNFbAMXKY2_uCdVJ30xFMJ4nRrgMmWD6zPv50_pze6CwPi2rKV56Xz-ztFxfVAenBaVzbU0R9Fmm996XsbCGQsAvFkSczJ1AWSS_zK-oBYVrFkBo1', start_index=22318)
Annotation(end_index=22396, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeho5LSDdUoiYJp3rRz0IST6HcaCCXPwDy0vozZg28mJd6XPh_jeuykPdiDTfUMvflaH7DgjaoDbku5p4a5Qom_YYLn7l5MMVCQI5N5zX9Doq56iJ_E3smQ1zddTmU-w==', start_index=22386)
Annotation(end_index=22463, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqz_n8cFDfpoyoZphV-fN4naSqjsWRuQAvDfA9GV5b44idXMXQcxejk217yLFIGlUr4v6QTj6NSpwx91sw_2hsJezl_aqPNVI3wNpN0To4Z0tHo_tpplNZxaM9To7lJmnjFZn1_VF2IvA7IH7nS6VJSofEv78vkwntalRZsQq7BsVZ3A==', start_index=22453)
Annotation(end_index=22535, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAMSh7Xg8GS-2jIgeWenHb6GrIFp2XW3FUo7NUo1qcv3iVvHA5UhdxoCR56r8N4T5zWBrsPJv1cx1uigaPp2miHND9kXEpaj5yZEPs7kgvY4maKo6hiNBYJSD_FsRHQuHDHmDoN8iIr_z0ldapJ7cOiUW0f92qq8uFLFz9XMpUU8MzsmZ-i1XDTMBaLZCBefI4O1VFJBW_iG7DFA==', start_index=22525)
Annotation(end_index=22595, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErqpETxJZfvK2oSr0gt9zbSxPtEkFvLBc9SGyOLfCdLmu7LRKItQbvsCje1JmhwhDIBt48Cp6D3PJSOe66t2l8S5pp2HlhizwqXlHKUIUe801_eeSdUBxk5tGjtyZlRcoH1ObbnB7jn5E=', start_index=22583)
Annotation(end_index=22595, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwOg52kZ8qrPHWxH7n5k54_qoVecuxB2R4qEc94wrT_VJxaibNaRT-CbClY2Zt7M1zfCPtZwKnER8F6pYvYJUAvllFuyrvLMfbD22V9yPV1LwXxdT78a3R2KsBoNHT-ZGBfulFNQHS7SUYPIpdz7b6ufqINvYso4scjwLD7jtm8pWWczfkqvHZvTAJB1Ax0bbX3Sup3_BOnj4=', start_index=22583)
Annotation(end_index=22661, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHw8ZWltsIM9CnR0AaHQvy0ySZNST2KXQ4R22oyRZJlPzdPsDhf7bxPYrfCkFaDxoaK7oWwe1XYU1iNqBFXXEQIhJLnU21Mf3OcIll1sWOzxeqibWaSxZ-_G4zXdW-1X9K7XoJ6TKR7OhbDN1basiTEpiPyb3__c04U5CfrabUw4GgS5JbA-MNXwnWIeNJVMxp_AiFnYCCvHg==', start_index=22652)
Annotation(end_index=22735, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWG6ufGrFuPh3OsI8-97gzhaVMxNJ9On6ScFzkg930R0OzX45BPrYgqUqFQIe0oqf0GmsatSPGR0bFkoJi6owvWmQmNuJib2suKw1iTLlW3zSP1V1n8ByK8rYFcgl5ag==', start_index=22725)
Annotation(end_index=22809, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIFOGxTICFsxZpZv5QI_OMglHvOldFZ1VbUhpbf_T6CAIK1Q---f1PvcJhoQ2g6xccS0udQSlxVjYeHpKK2n5wLTqlh67_9KvytpXf6hTdP4gk1eV1jHGq02Cnyj6zNxNkag==', start_index=22796)
Annotation(end_index=22809, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAIqn6on1u63E2RiVRD-i_HJYi6-IGzSWiCMyue1Wa8RR9M1tw8JjkXgXeP6CyxIfbLX9hDmTPC8A8m5lvQk9cH_WHT2zT5esBnPLE3gowY6-o5HD2OX1zg6R4i6FyteiuBvM2J8NUBeqPWCc4nSAddLCRhgTSJZRVxxnFd3VUq4fg4kumO8Bt8YS3icozQw==', start_index=22796)
Annotation(end_index=22870, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUHM3ykn-7KZ84yjio8nfc-3fCMYjoTBulsJtS1xSEdHRbMC8Gw-DsBtDtbFIbW5nbVkmyLD2W_mC0OjW1jQxWH54QU5CXtmfE1o1ncZU_aHKIJ955TY4fCowyM1W5D5wuLK62jLwl2dSW7vhMNUc00_gcxt3XUVh8CxA9qs1a7RvJMUljmm9XlpPY9seSazXRA3fYnz6y7ynpGJFq5-4aXKhijWp8mAA1lCkp', start_index=22856)
Annotation(end_index=22870, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVwVGvdZz-4hLmIbVkUqws1xngqoXNBJWMflJ-1Rvcbbyx7iXKjGQRLSCMQhB8SonQszbsMP4kxUEn2SPetZIfgbjLm_1EhB2cPh0YUWCuUV2DDJkXyDQARwq1UwFIKsNUJ2Q0uxExn38Zb3m1lPCnm129OixjhNoNhKOjS8uK9S0V4ihIe0L3YdBnJMtgBSQmW-sTXZv7So6YJw==', start_index=22856)
Annotation(end_index=22937, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtQxiZeXkDefgPPBnBTnDEfa6bEhm7EKVzQ5m2HdDpJTZ4YoyaQYsDbfY5HvuKS2CfSy7U4ppzxt7GgaQK9bkjzvSU4Y-J9gJ83E-e56yNRO6p7y6t4e2UBDTWr5nD7mndKmyZqkiF1p66UfvHaIA3qdTLIWart8xtNKjT2otnWtaJwHbmNSvxG4gp', start_index=22923)
Annotation(end_index=22937, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGv62BGPOzIqk96ihNPeWXmV0dyaTh91DmAk4Q8AxOpftsDoHO7L6m8Q3qtTZvSZyKOBzhNoqSbLFbBfClCvkum0IwnIUT4LsmgwmmeO6c3YR1hLleb0nr90E2Smsff83udqC5KAWqLQAcE5kJrpg==', start_index=22923)
Annotation(end_index=22998, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUx2nX8n7CM794hpjg4kBs9POQf4T6WI-Lk6-v84Cwj0dRj_kza-MLvHp_Eo_xOCgkbcNN_drVSUirVDGih5po8EtToWpwdjKxRlZmrF2kz5GZniixwMcCjbAuQzXTloZsFQ4mv5SbyzJxtw8W4vCWFmVK', start_index=22988)
Annotation(end_index=23047, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtl9embS4qLFvsRTn92OQuN-yccrJPjuRv46BmmsGnpthvQcMeJBkvUpWLEkqGAJtnjHPktyUT_sNFzke4wz2qc2p2RdB_tL1uIFAy8Uew7aArocZ0aaQXZv7HQvkFNmLypkLeIubB6OC4tobmo7n8uyuIM3SXIAiKlOEuWc7YW1nyxWEjVcEuJUAkFzGjGxxPWould8oTF_HVD0YK6h5P8fhqWkqpDs0mKtG_983eAhJC5MCLbOD8jCKBBfXSPP1ZVX3lrJHkEfnZEG4_', start_index=23034)
Annotation(end_index=23047, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGkT-Z5kp6jxGAGgTLXF6WaEKzxH_5MuznoTljOuFRehDPyzzJd0pFJ1GjMBR6ZLqcMEk_ajk-z3E_rf1mGgIw5t_zx-lksh2iqR_A4OyRZL1lPQK4L_1jYnIBbEaXCqZ2Sj-KUNWnuy43', start_index=23034)
Annotation(end_index=23101, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP8kqAJgJzEKvBsaEeO1JmpulzZKbZI4-jYCdxOZVRUXIH2idjjMiCecfE5UYTy4em521v9Gb_qK_CNS-z-iAT90nUtKSyBvZr8M0JPUp-F29i_SK32kVhorNjvdrby0X0RBqHwVQFjtFHB7lrxC47gudGb174bOL0RrigwNwZ37ZonJBSONflkFTfBZ2J6eXF1oa0niguvZ8G979nZ95XazkLnZgcSwMocg==', start_index=23087)
Annotation(end_index=23101, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVv8OOJjilGjy6BAhMJIp9qAAuTPW2SfjpBKvGwSXdcduJ8QHVYBW63tgkUT1ZWAfV6ZpKaJNJF4vxNRDHXZQ1ltQvH5Ce4-T4C5oQmxUAO6_6Uzc9PwDYKoRLyUAvHe6a1IJzd6PgWvIWgto_xM7-MjogZPhUOzWynW-ssRcm2V3fCBCeAZUrurPs1PuFuabIwMBNCTxmlnf3RgatpX5fPM0oXo7y1XXF2F_m3Exw0BZtq6y7dlKZ5jjSWF11TXOBCdD2WQ==', start_index=23087)
Annotation(end_index=23177, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE551IUwDt5paos8mwOWhRrXP7GArfTRYQ8M9FBQ0kpRfkW3JHIetK1RXvmoOAqgpHkIJgGB0Whl56qXGj2F9xiadSJ8xW51JAeAupbS-_P9tpjKJdQS-NfjklBYDX6NRhA-zNRpRnm9KwOr8i20i8DgYBUFJEd7tCx1y5FKIs6itVKOxjWJKN7ve7y12Up0rJtHjofj7hE5El6DQ==', start_index=23167)
Annotation(end_index=23258, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNRak46RCSKv0C8KSXUcJKl0vZwB-9BSJtF-tIoYgMwgVWYCF_budlnxzZkV3PCu6UEPX0BqNavj51NlwRFXc33leGJkK4PJ-04OQ17E5toM47tnGEj_xkIUF5DL2YFGI78zlNXd-AkRsLhwjdCf4N38gW1ZwblSHFxIF9ApNRFdqF1L2DMMEOYnSyLF0TLw==', start_index=23244)
Annotation(end_index=23258, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDe0Cau5eUKbAySDsc_sE6NXmklitanqbfaFfnEb83LIc9TL-pudRM0-maO6V4zz_ppRFucNAK3w-RYtDdMx9qSSPHpXZvauUmG8WkwyMcKL5D1s5YlfHnPIcgZvgX9w==', start_index=23244)
Annotation(end_index=23323, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHy3NuNk5PGem51cD0X_N-ojCqBBgdkxrg4k01nyTx6XDXoekzxChCGpdXT70RLlT44XzoHxuX0urIvkwldQ92o9q3hliwY8ehpV7HqVtjViZD3hVaDa763WMw1p-kzXpUgJKLIrvLnWIO6PbrIQDkkUUfzz3fE-ISf_Zpdp4QbdPrIKOT875wuInvqJAnNtS3uE-SslfNdIbvlUlg1QTAqg476cD5w37HjxECxT-pDcD-52VlJwxs1yrvVRIu8lxQbpkujwMbEIrp0TZoCDVdpiTfXHKLblAXvOQMXJIe-imemfZQ=', start_index=23314)
Annotation(end_index=23390, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTOFCNL5F-qDzC3pKaFokKKWts38b8nLA5H7JupzHRKomthfCyD8rHJGmdwlAPWvLVvCdhUsgR1TdF06vWHc0QeE2RRSwMY4MNqeONeVuNkfag-5n35euk5ExAOUK5hZv_i-nbREBJcw==', start_index=23377)
Annotation(end_index=23390, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcgLoVsxWh0imhJSmX-bqgt9pXuXVczirWsqdkJXlOYa5qpUlcOSSIbR8uRLb0clFBs3ZyUWiLk-GSdjVv5urvqHv5eVmxjLjn8JfjeYbv5_JngFckGxzGUbJSyQCC6DI=', start_index=23377)
Annotation(end_index=23456, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTTS-0B7djNGN6HTsHVGoM42Ya7GlKCOdYGvu3epnSXM-Xl-dsul2_omgbl5MrXVib1UFHFFitPbagDX3TKqv7okIUo0kaNxveGEmdESRnh8EhFj31NxPNlNEPFq9Z79T-7YbxFa7m5zCOyxO_V_nBRZgLpSYvMHfZPWA=', start_index=23447)
Annotation(end_index=23511, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGufhlfDWdMsXKsZvYPsVhj4NTB9gxECocKIUDkQppOtF50sLtujeGZXgZBKo-0xnaPi-qJ10MWI6vWpV-h0-looq1jq0YnBmG4c7L85KReZw7_7rPJi0ZtE_zzLonCj31nJLro9g58dj95ayELeno=', start_index=23501)
Annotation(end_index=23570, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIlu10RJxKd9P5dA3yfM15A6Xh8eh2O9XB5WOEGV1s_uEQrnbUCwXvqq_STSbO2nlRIjh88xEZj64GFR4hXzkXXKvUaqzRHIV7UWh0ZyXgBSAhHsKazCsWOI-0fUf0pvzvakBHLaNCIE3x-qBeGhZFMm0_f5Yj_YJ7tXp8OLgwZknoN3d5DVbnw9uW2vpR6hMW1bqPbrytcLK6vZ2nwkYZfnyOtz82ww==', start_index=23561)
Annotation(end_index=23622, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqFuWE2EX7MqL3YGQMDcBTyhe0CEG4Uw4PTh9dTaJhUATUVa6RTz0W_4NIDkHjz5ohVjECdi2TmH-B3iOg2LdlFb3AJRDdKS9gleAHUezxZZfkKRcTIFK4w3saN3O6CB8qs15GAPN5Kx1nvYxzSHxna8g=', start_index=23612)
Annotation(end_index=23666, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGpH7HHbv6P95jwEnYzWpMc3JmOj87-f2HuF_cm6axpRL8LcT3E9PthpJaNs6t0t2jV98i3KJvz8QOxFeXHSC7o2OBNc6gbMXA3tcT_KRSrxOu90D_7e85gJ5LE3sdi7kR2FpSHz12Mdne3waDClTJJ6fJGg==', start_index=23656)
Annotation(end_index=23724, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHowvqnn5juaGLzJrtVhsQc4bZ6GTn8yR0NrylHebnr1VAi6FEOuaJBv1lDAkI3KzB05Q6JkhX0bPgqXSsBpsNJ5vyE74WBtyZwo7qfYKz0nWIXGSDjYqsxeOMVbwCznQ==', start_index=23714)
Annotation(end_index=23775, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFU-zcHVXX_duNRZh_P6txdHWAwuk9JwPz697l8sRJf5MePK9oF7VHj2Pi8t73r2vgqjp37u8UlZ8JULl3ZsmGkbbZ9G8oU6e_FCwW1ORIP6DwMiFVdw_MdF3nWtSZM6w==', start_index=23765)

## Sources
