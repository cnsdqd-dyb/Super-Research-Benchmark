# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 568f2579 | **Time:** 350.35s | **Cost:** $0.96447
--------------------------------------------------------------------------------

# Optimizing Influenza-Like Illness Reporting Systems: Balancing Epidemiological Timeliness with Diagnostic Accuracy

### Key Points
*   **The Core Dilemma:** Public health surveillance faces an inherent trade-off between **timeliness** (rapid detection of outbreaks via syndromic data) and **diagnostic accuracy** (confirmation of the specific pathogen via laboratory testing). Syndromic data is immediate but non-specific; laboratory data is specific but delayed by 1–2 weeks.
*   **The Consensus Solution:** The optimal design is an **Integrated Sentinel Surveillance System**. This model combines broad, rapid syndromic monitoring (e.g., emergency department chief complaints) with a statistically representative subset of "sentinel" providers who perform systematic virological testing. This allows public health officials to extrapolate the *cause* of a syndromic spike without the cost and delay of universal testing.
*   **Technological Enablers:** Modern designs utilize **Electronic Health Record (EHR) Adapters** and **Artificial Intelligence (AI)**. Automated adapters extract clinical data in real-time to reduce reporting lag. AI models, particularly Long Short-Term Memory (LSTM) networks, can now predict laboratory results based on symptom clusters with high accuracy, effectively creating a "proxy" for immediate confirmation.
*   **Operational Protocols:** A **Two-Tiered Reporting Protocol** (classifying cases as "Suspect/Probable" vs. "Confirmed") allows for immediate public health interventions (like isolation) based on clinical presentation while awaiting virological confirmation, thereby bridging the temporal gap operationally if not data-wise.

---

## 1. Introduction: The Surveillance Design Paradox

The design of reporting systems for Influenza-Like Illness (ILI) is governed by a fundamental tension between the speed of information flow and the precision of that information. Effective public health response relies on **epidemiological timeliness**—the ability to detect an outbreak early enough to implement non-pharmaceutical interventions (NPIs) or distribute antivirals effectively. Conversely, the credibility and specificity of the response depend on **diagnostic accuracy**—ensuring that the detected surge is indeed caused by the influenza virus rather than co-circulating pathogens such as SARS-CoV-2, Respiratory Syncytial Virus (RSV), or adenoviruses [cite: 1, 2].

Traditional surveillance systems have historically bifurcated these functions. Syndromic surveillance systems, which monitor non-specific indicators like fever and cough, offer near real-time situational awareness but suffer from low specificity (high false-positive rates). Laboratory surveillance systems provide the "ground truth" regarding circulating strains and viral evolution but are plagued by reporting lags often exceeding one week [cite: 3, 4].

This report analyzes the optimal system designs that reconcile these competing demands. It examines the **Integrated Sentinel Surveillance** framework as the primary structural solution, supported by **Two-Tiered Reporting Protocols** and **AI-Enhanced Data Fusion**. The analysis draws upon global case studies, including the U.S. ILINet, China’s National Notifiable Disease Reporting System (NNDRS), and Taiwan’s EHR-integrated frameworks, to propose a design architecture that maximizes both speed and precision.

---

## 2. Theoretical Frameworks of Surveillance Design

To understand how to balance timeliness and accuracy, one must first categorize the existing architectures of disease reporting. The literature identifies distinct modalities, each with a specific profile regarding the timeliness-accuracy trade-off.

### 2.1 Universal vs. Sentinel Surveillance
**Universal surveillance** attempts to capture every case of a disease. While necessary for rare, high-consequence pathogens (e.g., Ebola), it is logistically impossible and financially prohibitive for seasonal influenza due to the sheer volume of cases.
**Sentinel surveillance** is the standard design for ILI. It involves a network of selected reporting sites (hospitals, outpatient clinics) that report the total number of patient visits and the number of ILI cases. A subset of these cases is sampled for virological testing.
*   **Timeliness:** Sentinel systems are generally faster than universal systems because the data volume is manageable, and reporting channels are established.
*   **Accuracy:** By linking syndromic counts from the sentinel sites with the *positivity rate* of the samples collected at those same sites, the system estimates the total burden of disease with high statistical confidence [cite: 4, 5].

### 2.2 Syndromic vs. Laboratory Surveillance
**Syndromic Surveillance:** Monitors pre-diagnostic data. This includes chief complaints in Emergency Departments (EDs), over-the-counter (OTC) medication sales, and school absenteeism.
*   **Advantage:** Timeliness. Data is often available within 24 hours of the patient encounter [cite: 3, 6].
*   **Limitation:** Low diagnostic accuracy. "Fever and cough" (the standard ILI definition) captures a wide range of respiratory infections. During the COVID-19 pandemic, the specificity of ILI for influenza dropped significantly [cite: 2, 7].

**Laboratory Surveillance:** Relies on confirmed virological results (PCR, culture, rapid antigen tests).
*   **Advantage:** High diagnostic accuracy. It is the only way to confirm the circulating strain (e.g., H3N2 vs. H1N1) and detect novel variants [cite: 3, 5].
*   **Limitation:** Latency. The turnaround time for PCR tests, combined with the time for sample transport and batch reporting, results in a lag of 1.1 days to over a week [cite: 3, 4].

### 2.3 The "Right Size" Approach
The Association of Public Health Laboratories (APHL) and CDC developed the "Right Size" roadmap, which argues that an optimal system does not maximize *all* attributes but rather optimizes the *combination* of data sources to meet specific public health goals. The design objective is to determine the minimum number of specimens required to achieve a desired level of confidence in the data, thereby reducing the burden on the system and improving speed without sacrificing statistical accuracy [cite: 5].

---

## 3. The Integrated Sentinel Surveillance Model

The most robust design solution identified in the literature is the **Integrated Sentinel Surveillance System**. This architecture does not view syndromic and laboratory data as separate streams but fuses them into a single reporting pipeline.

### 3.1 System Architecture
In an integrated model, the reporting system is designed to capture syndromic data from a broad network while simultaneously channeling virological data from a sub-network.
*   **Broad Syndromic Net:** A large number of providers report aggregate ILI counts. This provides the "signal" regarding the *magnitude* and *location* of the outbreak [cite: 2, 4].
*   **Targeted Virologic Overlay:** A subset of these providers (sentinels) are equipped and mandated to swab a systematic sample of patients (e.g., the first 5 ILI patients of the week).
*   **Data Fusion:** The system calculates the **proxy-confirmed incidence**. For example, if the syndromic network reports 10,000 ILI visits and the sentinel laboratory network reports a 20% influenza positivity rate, the system estimates 2,000 true influenza cases. This method retains the timeliness of the syndromic reporting (available immediately) while correcting for accuracy using the laboratory percentage (available with a slight lag, but applicable retrospectively to the real-time volume) [cite: 4, 8].

### 3.2 Case Study: Taiwan’s Integrated Framework
Taiwan implemented a highly advanced version of this design using an **Integrated Influenza Surveillance Framework**.
*   **Mechanism:** The system uses an "EMR Adapter" and an "ILI Open Data Adapter." The EMR Adapter connects directly to hospital Electronic Medical Records (EMRs) to extract specific surveillance variables (ICD codes, temperature, lab results) automatically.
*   **Outcome:** This automation eliminates the manual reporting delay. By integrating national-level ILI incidence with hospital-level EMR data, the system can predict epidemics with high accuracy. The framework demonstrated that integrating these streams allows for early prediction of influenza activity, effectively balancing the timeliness of the ILI data with the richness of the EMR clinical data [cite: 9, 10].

### 3.3 Case Study: China’s Multi-Channel System
China employs a multi-layered approach involving the National Notifiable Disease Reporting System (NNDRS) and specific ILI sentinel hospitals.
*   **Challenge:** During periods of co-circulation (e.g., multiple respiratory pathogens), the ILI system's effectiveness is compromised because the "noise" from other pathogens obscures the influenza signal.
*   **Design Adjustment:** Research suggests that prioritizing NNDRS-reported case data (which includes clinician-diagnosed and lab-confirmed cases) over raw ILI counts enhances accuracy. However, to maintain timeliness, China utilizes automated alert algorithms (like CUSUM and moving percentile methods) on the syndromic data to trigger early warnings, which are then verified by the slower laboratory channels [cite: 7, 11].

---

## 4. The Two-Tiered Reporting Protocol

While the *integrated* model addresses the data architecture, the **Two-Tiered Reporting Protocol** addresses the operational need to act before data is confirmed. This design is particularly critical during the early stages of a pandemic or a severe seasonal outbreak.

### 4.1 Suspect vs. Probable vs. Confirmed
This design categorizes cases into tiers based on the level of evidence available, allowing the reporting system to trigger different levels of response at different times.
1.  **Suspect Case (Tier 1):** Based solely on clinical criteria (e.g., fever >38°C + cough).
    *   *Timeliness:* Immediate.
    *   *Action:* Isolation, initiation of contact tracing (in pandemic scenarios), or general alerts.
    *   *Reporting:* Entered into the system immediately to flag potential clusters [cite: 12, 13].
2.  **Probable Case (Tier 2):** A suspect case with an epidemiological link (e.g., contact with a confirmed case) or supportive but inconclusive lab results (e.g., antigen test).
    *   *Timeliness:* Hours to 1 day.
    *   *Action:* Presumptive treatment (antivirals), broader community notifications.
3.  **Confirmed Case (Tier 3):** Verified by PCR or culture.
    *   *Timeliness:* Days to weeks.
    *   *Action:* Definitive epidemiological characterization, vaccine strain selection [cite: 13, 14].

### 4.2 Operational Benefits
This tiered design "balances" the trade-off by decoupling the *alert* from the *confirmation*. The system does not wait for accuracy to generate an alert (timeliness is prioritized for the "Suspect" tier), but it does not record the event as a definitive statistic until the "Confirmed" tier is reached (accuracy is prioritized for historical records).
*   **Historical Precedent:** During the SARS outbreak, Taiwan adopted a two-tiered approach (Suspect/Probable) recommended by CDC officials. This strategy enabled authorities to institute precautionary control measures (isolation) *before* confirmation, which was credited with stopping the outbreak [cite: 12, 15].
*   **Application to Influenza:** In pediatric influenza deaths, a "suspect" report triggers an immediate investigation, while the "confirmed" report finalizes the surveillance record. This ensures that no time is lost in the investigation phase due to laboratory delays [cite: 14].

---

## 5. Technological Enablers: AI and Electronic Reporting

Modern reporting system designs leverage technology to artificially enhance the accuracy of timely data, effectively narrowing the gap between syndromic speed and laboratory precision.

### 5.1 AI as a Proxy for Laboratory Confirmation
Artificial Intelligence (AI) and Machine Learning (ML) models are increasingly used to "predict" the laboratory result based on syndromic data.
*   **Mechanism:** Models like **Long Short-Term Memory (LSTM)** networks or **Deep Learning** classifiers analyze patterns in syndromic data (symptoms, demographics, seasonality) and historical correlations with lab data.
*   **Result:** The AI generates a "risk score" or a predicted diagnosis. This prediction is available immediately (timely) but has a much higher correlation with the true viral cause than raw syndromic counts (accurate).
*   **Evidence:**
    *   Studies show that AI models can predict influenza outbreaks by integrating search engine data with historical illness data, outperforming traditional models [cite: 1, 16].
    *   In clinical settings, ML algorithms using vital signs and chief complaints (e.g., "InSight scores") can predict sepsis or specific infections before lab confirmation, acting as a high-fidelity proxy [cite: 17].
    *   A study on "ARGO" (AutoRegression with GOogle search data) demonstrated that combining electronic health data with internet search queries significantly improves the accuracy of real-time influenza tracking [cite: 18, 19].

### 5.2 Electronic Health Record (EHR) Integration
Manual reporting is a major bottleneck in timeliness. Systems designed with **EHR Adapters** automate the extraction of data.
*   **Design:** The system pulls "structured" data (ICD-10 codes, temperature readings) and "unstructured" data (chief complaint text) directly from the hospital's server.
*   **Impact:** This removes the burden from the provider and ensures that the data enters the public health system the moment it is entered into the patient's chart.
*   **CDC's ESSENCE:** The Electronic Surveillance System for the Early Notification of Community-Based Epidemics (ESSENCE) utilizes this approach. While it was criticized for lack of timeliness during the 2009 H1N1 pandemic (due to data transmission delays), improvements in automated transmission frequency have since enhanced its utility [cite: 3, 20].

---

## 6. Optimizing Case Definitions

The "software" of the reporting system—the case definition—is as critical as the hardware. The design must choose between sensitivity (catching all cases) and specificity (catching *only* influenza).

### 6.1 The ILI vs. ARI vs. SARI Spectrum
*   **ILI (Influenza-Like Illness):** Typically defined as fever ≥38°C + cough/sore throat.
    *   *Balance:* Moderate sensitivity, moderate specificity. It is the global standard but struggles when other pathogens (like COVID-19) cause similar symptoms [cite: 2, 11].
*   **ARI (Acute Respiratory Infection):** Broader definition (often includes runny nose, difficulty breathing).
    *   *Balance:* High sensitivity, low specificity. Useful for early warning but prone to false alarms [cite: 11, 21].
*   **SARI (Severe Acute Respiratory Infection):** Requires hospitalization.
    *   *Balance:* High specificity for severe disease, but low timeliness (patients are already hospitalized) and misses mild cases [cite: 4, 22].

### 6.2 Impact of Co-circulation (The COVID-19 Factor)
The emergence of SARS-CoV-2 necessitated a redesign of influenza reporting. Because COVID-19 symptoms mimic ILI, the "diagnostic accuracy" of traditional ILI reporting plummeted.
*   **Design Adaptation:** The WHO and ECDC now recommend **Integrated Respiratory Surveillance**. The design no longer looks for "Influenza" in isolation but monitors "Respiratory Viruses" as a group. Sentinel specimens are tested for *both* Influenza and SARS-CoV-2 (multiplex testing).
*   **Result:** The reporting system tracks the *relative contribution* of each virus to the ILI syndrome. This restores accuracy by clarifying that, for example, "ILI is rising, but it is 80% COVID-19 and only 5% Influenza" [cite: 23, 24, 25].

---

## 7. Comparative Analysis of Global Systems

Different nations have adopted variations of these designs to suit their resources and populations.

| Feature | **United States (ILINet/NREVSS)** | **China (NNDRS/CNIC)** | **Taiwan (Integrated Framework)** | **United Kingdom (PHE/FluSurvey)** |
| :--- | :--- | :--- | :--- | :--- |
| **Design Type** | Sentinel + Virologic (Dual streams) | Multi-channel (Mandatory reporting + Sentinel) | Fully Integrated (EHR-linked) | Sentinel + Participatory |
| **Timeliness Strategy** | Weekly aggregate reports from providers. | Real-time web-based reporting (NNDRS). | Automated EMR extraction. | Self-reporting via apps/web (FluSurvey). |
| **Accuracy Strategy** | Public health labs (NREVSS) provide the "virologic view" to correct the ILI data. | Lab confirmation required for "Confirmed" status in NNDRS. | Lab data integrated into the EMR stream. | Self-swabbing pilots (FluSurvey) [cite: 26]. |
| **Key Strength** | High representativeness and historical continuity [cite: 2]. | Massive scale and speed of the web-based infrastructure [cite: 7, 11]. | Automation and data richness (clinical + lab combined) [cite: 9]. | Engagement of the public; captures non-medically attended cases [cite: 27, 28]. |
| **Key Weakness** | Reporting lag (1-2 weeks) for finalized data [cite: 4]. | Complexity of managing massive data volumes; co-circulation noise [cite: 7]. | High technical infrastructure requirement. | Lower diagnostic accuracy of self-reported data [cite: 29]. |

---

## 8. Future Directions and Recommendations

To achieve the ideal balance, future reporting systems must move toward **"Nowcasting"**—the use of real-time data and statistical models to estimate the current state of the epidemic before the confirmed data arrives.

### 8.1 Recommendations for System Design
1.  **Adopt Multiplex Sentinel Surveillance:** Systems should never test for influenza alone. Sentinel sites must use multiplex panels (Flu A/B, SARS-CoV-2, RSV) to accurately attribute the cause of the syndromic signal [cite: 23, 25].
2.  **Implement Automated EMR Extraction:** Moving away from manual reporting to automated "backend" extraction (as seen in Taiwan and modern US systems) is the single most effective way to improve timeliness without sacrificing the detail needed for accuracy [cite: 9].
3.  **Utilize AI for Signal Verification:** Algorithms should be trained to "read" the syndromic signal and predict the probability of influenza. This provides a "synthetic accuracy" that bridges the gap until lab results are finalized [cite: 1, 30].
4.  **Maintain the Two-Tiered Protocol:** For operational response, public health authorities must retain the ability to act on "Suspect" cases. The reporting system must support these provisional categories to facilitate rapid intervention [cite: 12, 13].

### 8.2 Conclusion
The reporting system design that best balances epidemiological timeliness with diagnostic accuracy is not a single tool, but a **layered ecosystem**. It relies on a foundation of broad, rapid **syndromic surveillance** (Tier 1) to provide the "when" and "where," validated by a rigorous **sentinel laboratory network** (Tier 2) to provide the "what." The integration of these two layers through **automated electronic data exchange** and **AI-driven probabilistic modeling** represents the state-of-the-art in influenza surveillance, transforming raw data into actionable public health intelligence with minimal latency.

---

### References
[cite: 1] PMC12307093 - Optimal design for influenza surveillance systems
[cite: 31] PLoS Comput Biol 8(4): e1002472 - Optimizing Provider Recruitment
[cite: 32] WHO Guidance 2024 - Participatory surveillance
[cite: 5] APHL/CDC - Right Size Roadmap
[cite: 18] MDPI 1660-4601/19/6/3681 - Balancing timeliness and accuracy (ARGO)
[cite: 7] PMC11425297 - ILI surveillance in China
[cite: 2] medRxiv 2025.12.03.25341530v1 - ILI Surveillance Network
[cite: 27] JMIR mHealth 2020;8(12):e19712 - FluMob effectiveness
[cite: 6] PMC1975801 - Timeliness of alternative data sources
[cite: 20] MMWR 60(13);406-410 - ESSENCE evaluation
[cite: 30] Frontiers in Public Health 2025 - AI model-assisted diagnosis
[cite: 3] J Biomed Inform 2016 - Data Sources for Biosurveillance
[cite: 33] PMC2794282 - Syndromic vs Laboratory advantage
[cite: 4] GlobalRPH 2022 - Sentinel surveillance limitations
[cite: 11] PMC12116594 - Multi-model frameworks (China)
[cite: 34] PMC8967469 - Integrated surveillance strategy
[cite: 9] PMC6376337 - Integrated Influenza Surveillance Framework (Taiwan)
[cite: 21] CID 2025 - ILI vs ARI case definitions
[cite: 16] MDPI J. Clin. Med. 2024 - Integrated surveillance and Google Trends
[cite: 35] Frontiers Public Health 2025 - DL models for forecasting
[cite: 36] PMC8389830 - Sentinel surveillance of COVID-19
[cite: 8] JID 2025 - Sentinel vs Universal surveillance
[cite: 11] PMC12116594 - Early-warning models in China
[cite: 37] JMIR 2025 - Deep learning for ILI forecasting
[cite: 29] PMC10587643 - Participatory surveillance attributes
[cite: 19] PNAS 2015 - ARGO model
[cite: 12] GAO-04-564 - SARS reporting and two-tiered approach
[cite: 23] ECDC 2021-2027 - Long-term surveillance framework
[cite: 22] PMC10123393 - ILI/SARI tool validity
[cite: 24] WHO Policy Brief 2024 - Integrated surveillance
[cite: 38] JID 2026 - Case definition sensitivity
[cite: 25] WHO 2021 - Integrated respiratory sentinel surveillance
[cite: 13] CDC - Junior Disease Detectives (Case Definitions)
[cite: 14] KDHE 2018 - Influenza Death Investigation Guideline
[cite: 15] GAO-04-564 - SARS reporting delays
[cite: 39] National Academies - Two-tiered model recommendation
[cite: 17] PMC10800769 - ML algorithms for sepsis/infection prediction
[cite: 9] PMC6376337 - Integrated Framework Adapters
[cite: 10] PMC6920914 - EMR Adapters and Blockchain
[cite: 26] JMIR Public Health 2022 - Self-swabbing pilots

**Sources:**
1. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwHcOhIhsJLRgvT3CT23fbrE51pf3qXBnXcCJtECWQi1YxqtbNuahajhT2JbxRo4pPXcIhS4Ujnql-s4h5mmBTpxxbhZWnPe1TfcEc7lAdOSxd7PCAdHAzY1p-IFmPfLgInmFlJUMwuw==)
2. [medrxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeMjXZFTsYMH7tPRHRH3ZSUnJ4sRZ-_22JZ2xpZneWMRc3rzcxmD9i2SAfXCDUSab8zw0siupapOxmSfBwlELjRJ55u3YjgJZL_e2xpb4OJteclv26xrCUTTRkpTV6SfVjGtBTEwj0pFYAzLet_kCzp8bps28LhoWdqyYbzVg=)
3. [cdc.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEOWgcT89kDcJsoH5DeJzzCLWe8FkyTzZl5dM_bP8PmClUWV9VMKJ0v8xkECOaB2l8IGe17K8fyRYgGtTHXd2arhM_JK2w4f5I0Xdd62pccaIW96V1iESa1ZgyENK35B8TVibmHNgEbejWcVBbA)
4. [globalrph.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQu1LHbqDJeGSLRb4iUKwrK1gGKz85yTYNNgRgCo3tbLcYgc08YqGNCaqQx7v-3mom6llrKdZBTeI1tA_P1EbZ2ixeoXHtBm5kuAzm_mwd3SswSIq145N1PdYvBtmOWfwygmVQbiBThFIxVp6ws4oLngLaLhckG3LUXWEimO0NNX9ZVKGZPEpfnzdgEAv37nTa5ZbFrOOcv2dewIBEGkLxG8H7LnE=)
5. [aphl.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENdYz7BSxiNQ-3HDz93iLhwSXqPf5jbit0gKe5zTsQoedIwN49PMuIMjwNLuThKD6UdJ4laZrJ1G-3cA9Liat-x-xe7WAYPmRTMsxQV8zlC1EnJZMEH43u45mmpJr3cJQb9E1svHJPq4CwzemxcuSu2Qw3JbLmFvMFSTMTFASW7gHJ5DZY9Wbdxn_clBGcM1-Z2JZbNvRXyQ==)
6. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5005g6h0WE8LZux2pZbSVz_cN8IKHCSKMCNTpSYpLB6XPwsItNfthNNg62i4VzjK7DY_OkKQFXsyZ-BmxUKfH8deNQSQJm_bTAUNzSsCgY_TUo7rTFGFp8X-JhOsJ9uHMCHkeiutp)
7. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkgr5uGYxyF9JDQXDgQ63EH_38GlJ3BMqFvLoEvYUN86FAbEqs2-FEg5TqUFTXnV58Q_yNAhaXvTJ0ab1r5xZc8-5GjgrPexOnUR-yX2RxTKpvkr8zMynlW3iouvSi7y908aFGKChZeA==)
8. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQ9C5xo_Kc_gjkXRfDBw4NDPQzF4gAv5d3ZJEUp0s8LkWaiguMCfaEq8mUajNioQxzFTkP1ig78QNxgByxRgFxj2RoAcW7CaMC2SM952unvRpkEEwkrNnRhPqpDHwadbRAJhrz380h_Cpio-llqCz1PYGXSu67xdg=)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHEerA0AIeHHVfMsIot_QIz89ycMqWgVEPWpsFH3hbpi7huWGOmJsUinQwV4yHBLjLLSaltnMnkBcJedc6MHbyT3pZxOpd5HrZ-fxSPabLc8BMMT2nZaqemIIinHWd4o9jh9uOwRTS)
10. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGSHqPbh__-L_wtBmGG97gBUqKLu6TSF8s8ahgzetr-u6sbQ67VA6GgAp6F0N6ffxYYsZ5-jv9qKeN2E81FXqbQS-BYCG1zJJvEP3RZZrgj9UxE_yx3aPZ40EX2Kpw2J-TiSbLgKiQ)
11. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3oQ2qEem7ItAx2e5AaPL0vP2LaLJ1GIeMeOI0S-F-Kfdqf_LHwjN5xrVyG5zf88rp-RHA5Z9ET-O1JgAGMI3fDORXC73h2TQ2JmZDUuGoisrzlx9F7uL1Nm1LmjyLIX6qk3YGyQqZuw==)
12. [gao.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNOyn-BqjLUTzybzIfZRAL3OjVuFmLSQ_vYjUCYRE8sARizFdPbSTtK3gdByBGjm-KAYaXu1AjpOnPZyycb1LagfMFSbDP2HzI7K2ZRlESuv2r857NstUYjpd5E7s=)
13. [cdc.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEynvI4_ahEMHEpdXwYpROyOakAw1wiV3cYceo5FL_vaudJUhy7xFJcHav9WtN7McI9W1JKpNSh9xKQaXcHWauUALe3oKOxfn4cEMMzoU4asEUwIYFtaLJHni8-I2M6WekEgHcycxcckQS3SeVH_Aa6OVEd2d9ZCTV1lTt5_A==)
14. [ks.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKQYHI5KK-kbA8BMa1rgThChLAAC2sPQ9jgFeRk4ZuU67t8ddH339zn_r4C49R_ojp6PK0RWalcJ4b_FrttVxHYAFY1ZGsdf6UTkLdM0gjRwtjvDrKjtavfKgWKwTlsLYK2lW9LZ5knwWsc6K_jvt5gYJFDmbJhTbNIU1rDayOGq1TNkotrQMEapVPSKTo2HheVDwejvvj0khrOjWqKp7H39fG2NsDu_E=)
15. [gao.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcRofjqa0g4LTKV2_i0sE_kIGTHu7VrVtAcGMgUjYJ8yLMHqn2RRyD_paZaSUtjW2lV_lBU_G4x2nuOYbmp3GIYJK8F7WpbrXe_conb_9LERC5C_dYV-A5QCuSM99P1A==)
16. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFfamqk5v46WIORfdEMPt091O0yMEWz6KHh__Pa88lfkLs-gFIx1HSeVnB88CKvBNOXsNEgI7TF4uWkvSK_WB6SjmwGQYUqsKosNBMyk0bD4X4TOU_XCnZ0f2KlFyS)
17. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLRgZHJWo1ZgsV4OTpv9TYB57gqJxz8uWGF4EodXJMun1o2HmV97SdUHC0JhygOISUjUqJU9Hva0gcxj91RNmJxJS2WtGSzVdOkdEvmzkHzfiPBMBLv5ggUDN-Y8xT56xXotxW47myFA==)
18. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjencLLWxe0LQWvNefU7ktizYYVhwAN6S-mtFomIMzvzQYC2Qvgo_hMSMxMEVsQ0fPjt0y26J4Ggt4RzgkLrd5wpzzzeSgRvmFc_YC1YVOvnZ3hz-zQ_ku7B3UeyyF)
19. [pnas.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMvY8HP4btnv2tf6sXjRU3s5rgDaqzFYeX-UpdnLHwy5i9k3K1uH6ajVAexiWI9vfLgZl9fGeK6NSaKtMQcN50Q0CC0SKlT2N_KCs5JukbPQmDfRpn5N6ayll8wyVy5tkBIrioob8=)
20. [cdc.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSktnhwQnVijHzFhxAn5dbzWa13ISuPvS59rl04zWGmS0LBBO_YECFfjv-f59YRh7qfCjVxOrC8ZRCXsaG65WriuIUwI2oF4hoVgZLgRz_WdmlFbdnbRC1Gj_IB2d3M9v5Or3BhX4cW9syjdc=)
21. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4RUQGNDvFDj_-0C2vSscuDBGFt3FLhs-HcBWT_FPfrYFmBMF2nW_g_lNvPaOSk3N0R2d4LAZRV_DH95dEypzZ6-7HUbh7CBvpoVsuT52UdLrMJ5X-tVumH1Wh8Zv3YTxpYIQNdlvpb-FMpA==)
22. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEBUFY_z550_WEth0NwDpMGXDi_56kbNfGO9PLn-t-8-pmaQeVsOzuW5vWbcCz-wP-cYfTQjgiBoOSN-S9SuS_aX2N1oC1CmwyrNQwpBa07VZ6K7p5ICGRnmw_nxc_my0AtedFzb4EsQ==)
23. [europa.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEipVKKhfcPFgiUSUr_Yo-9vKGg-rAccNAYTOqil3PX5SsYRE7o4QEAF43VtUElMXP5XB8Bg3pjEfnh-KG7o9AM5DwVXPlRM2gAPAw7Jdl-In4T-2K8BlKyxgfvYerKjn6tNYLAl5Zc9CDgi0Pbs2P6BV8ks9AkKlaEF6dav21kWYztDqlWAeNB-Uo20LaOGUOYUCLrmPs6eFPo343)
24. [who.int](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFStL4OqvNJ-jDfUi7XUvdaZK_XXg95Hl9s4051f2F9iJWZ5DX_T6PBAqvUMenIEiIq94B7EG_yN5rUP9Unh5Is-gZKopRs7mzHxT4KsjmkA8W3uLnQMGDpG_EVxR5QusK1HO76-leHP0RfEkAZtJNXicBQaxlwqwUVF0ZhkFZKVNaK4dROjo5qw7S8nmiwujWn0mfZJyZIGJIzVK-TCDE=)
25. [who.int](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHx7Vj0a_ch6Zv63EYtPIhyC9dTuMe5KE2HnoVzHoZHH9Uv1YligeKX9Jg7s6BzOXIEHzycNaI_Byyr0K8bcNs7F2O-gb6moD39VCjwBw_6Upt89xy1M40Rh9KDFXQE8KqgRyeh9u7_51wJwC1OYN4xSlsgMuMGCqaNtmceEr9HNDCVu7ZkTTnm_hyWODzh2mmfTQ==)
26. [jmir.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkY43Fe5cxQMYdP-mVLkTwwd--XgJ5302I7eQ3EAhQnYtGO-EvZNigKfi30CwR7rCIXrTCvMP-HPFH4AfX8jiuPFRKKTeb3hNQlpzXdnsVYgKZC9ABtog7aIlnX4Zx5QfeGw==)
27. [jmir.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9zUN7m_OQ51GcDo-IoGHzoTKqad4Pw3pSoXs-Oe1IWIJHp-y8jJ2DZ1cIRMW1HTH778x6LTsj0PzfS9dBZflu-N213H84cdnulcFEOIEfCRjvZN8j4EETjfecG_5B)
28. [jmir.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOIdhII8MBAOoPKuR41ctwQISN2m772lZv3mmKdIX9Nml5V_3cO4Hg8KMFItWpGeBDd7QALl7pkuquJ1IYhZCUkVfoOVz8HEmQfUY9MoklJmL02RjjMPCiuQ==)
29. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGer_XnMM3vNlK1-sziU2Q3FL_YSgBkjk4aEPZwiLb46g8xP2TF6kuzDE1DpvV03x0S6dDzA0oX7WHfmy9vr36rQfSYtcLrDAdZhOJaMEoLMv98N4ymOMv7rxR0niftSiI9W4AILlYqyg==)
30. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGljLKSRs-nj9Q--8HMEEtVrsUnlhL0tBpNaG0fA57phCVHMSODEPbHMYQkJHQT2CaPVszK9OERmdbThNF8yW8-fO0W0OfFpXnJ2zWzSN-QV5oKMB5HP9cyty2y5tl_ZoisBTmVjtcIAnw1og4rQKej79ruUPsJFOOS2syjv44CM0yhOOt-VGF4rRiQR_dvRyMW)
31. [plos.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjDu09SEUplpmX0B8vUwBT6d2Hn9PkVR5ZCgAXP_fuN27_WP9IG8eMk2J2YKaVgXjUMKZbNs5ktdMSClzp0ZrtwbwWO4sVfeRXULniC0yWZ-1uxKcn2QSqn0D0u8t1L-vDxkrr6I3fBJwFpp-_dfyqezwWabo1H25Ov5PDxbIJMsUvzsA=)
32. [who.int](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcWBV3TFLiMlVDCMItWu5LOMa-CJHkdKTXYOFSkqF6Vb1I721kQeyPH94-9n2DSyLN-L-5Qj_wppEyLVdcLI0h5lkiqI7M5hv5MxY4sYghN6IJXvfKS_Y6RPW2JEMNLXRb7P9hYX16tGaZAg==)
33. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGq5vsrY34WqfDoyQ7b3Ehp1rfPbOSWigfLo3CEGqglVHpsa9aZWFm9fr60AQH1qJTvnaVjCu5THuipJtH-CSQb4S6z836OqI5hG4agZpVpglzyJjuoS7DEpw4TZhdyUjeBGeB85d5u)
34. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE30t4kclw9Htv3bSTmzgcQ2LaorrBj-KNiqpPiuGZGJMhmonAsnJV-jeey1tPnAUn1LVvVQgtLtuMUuvbbduM-AXam974xy3DdsNX1xCiewn3icK2XaOJOyPEVQbhSdhPNVg9ogWnn)
35. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9LQplxvpT-U1nunKA15TMzfXFOm3PuD7i0gAAkMATAiO8AldC0rrr-pHPcDRh2mMzIzYhfQ6T4__9BC15dEiYuJ3r7Nd-72coffjsvxuVRxNORjXFJDcFDEryJ1aehN_8Cid0sioyVoNGrM-xDCQzwQNtBX8QlplgC-LmbTaTsMdbX5YUqplFfmTyp5IFZx89)
36. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRpMmzSJSLcc9tV1Y-EEm2C61ena_kESN7T3paQMV9z8tRLx4usV4vPANbMr7k76HCYcJQQEO6nWcc6cZYmR8Urxmap0F3_XO-JijQL8JPguaMa33S2GDRkhf5fy_3cFCiz2usvha6)
37. [jmir.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEeH-PtnnahwpDE6-WlZPvABGNhZjiHBLrWfXhhsAkq6O3WBcZDX8z3yomZe2HbVHk9L3wsofI84eEruqp94ErB08aU8pzJAJjclq5FwMB4bqqkm5fTKkhl)
38. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8Y0Fosz6SaqyRfOGP2IRpb-cPm4l2hSFI9mK8evtl90FFowoN7-VSipoQhLwJxGBScC6PXuLGnlCP4gqA4R6fu3WVhP5t1oHhxFsgtkhU0lywCfxNHx4jkNPG0E_nPf2gXNWbYnqveYZgaww=)
39. [nationalacademies.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_mB9siqfnWWLqeusArdSdVeqlVeKQmEPdD4d3WH48hSi3DUQaZLJgJGv6XN70xK2JuhICImeaTC10lphCaXhXCqlHYiqVPrXLe1Y4PFy6mVaDWBsufwZFulh38h1Kg_RhumN5UslHiTWN50E=)


## Annotations
Annotation(end_index=2417, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwHcOhIhsJLRgvT3CT23fbrE51pf3qXBnXcCJtECWQi1YxqtbNuahajhT2JbxRo4pPXcIhS4Ujnql-s4h5mmBTpxxbhZWnPe1TfcEc7lAdOSxd7PCAdHAzY1p-IFmPfLgInmFlJUMwuw==', start_index=2405)
Annotation(end_index=2417, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeMjXZFTsYMH7tPRHRH3ZSUnJ4sRZ-_22JZ2xpZneWMRc3rzcxmD9i2SAfXCDUSab8zw0siupapOxmSfBwlELjRJ55u3YjgJZL_e2xpb4OJteclv26xrCUTTRkpTV6SfVjGtBTEwj0pFYAzLet_kCzp8bps28LhoWdqyYbzVg=', start_index=2405)
Annotation(end_index=2875, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEOWgcT89kDcJsoH5DeJzzCLWe8FkyTzZl5dM_bP8PmClUWV9VMKJ0v8xkECOaB2l8IGe17K8fyRYgGtTHXd2arhM_JK2w4f5I0Xdd62pccaIW96V1iESa1ZgyENK35B8TVibmHNgEbejWcVBbA', start_index=2863)
Annotation(end_index=2875, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQu1LHbqDJeGSLRb4iUKwrK1gGKz85yTYNNgRgCo3tbLcYgc08YqGNCaqQx7v-3mom6llrKdZBTeI1tA_P1EbZ2ixeoXHtBm5kuAzm_mwd3SswSIq145N1PdYvBtmOWfwygmVQbiBThFIxVp6ws4oLngLaLhckG3LUXWEimO0NNX9ZVKGZPEpfnzdgEAv37nTa5ZbFrOOcv2dewIBEGkLxG8H7LnE=', start_index=2863)
Annotation(end_index=4680, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENdYz7BSxiNQ-3HDz93iLhwSXqPf5jbit0gKe5zTsQoedIwN49PMuIMjwNLuThKD6UdJ4laZrJ1G-3cA9Liat-x-xe7WAYPmRTMsxQV8zlC1EnJZMEH43u45mmpJr3cJQb9E1svHJPq4CwzemxcuSu2Qw3JbLmFvMFSTMTFASW7gHJ5DZY9Wbdxn_clBGcM1-Z2JZbNvRXyQ==', start_index=4668)
Annotation(end_index=4680, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQu1LHbqDJeGSLRb4iUKwrK1gGKz85yTYNNgRgCo3tbLcYgc08YqGNCaqQx7v-3mom6llrKdZBTeI1tA_P1EbZ2ixeoXHtBm5kuAzm_mwd3SswSIq145N1PdYvBtmOWfwygmVQbiBThFIxVp6ws4oLngLaLhckG3LUXWEimO0NNX9ZVKGZPEpfnzdgEAv37nTa5ZbFrOOcv2dewIBEGkLxG8H7LnE=', start_index=4668)
Annotation(end_index=5023, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEOWgcT89kDcJsoH5DeJzzCLWe8FkyTzZl5dM_bP8PmClUWV9VMKJ0v8xkECOaB2l8IGe17K8fyRYgGtTHXd2arhM_JK2w4f5I0Xdd62pccaIW96V1iESa1ZgyENK35B8TVibmHNgEbejWcVBbA', start_index=5011)
Annotation(end_index=5023, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5005g6h0WE8LZux2pZbSVz_cN8IKHCSKMCNTpSYpLB6XPwsItNfthNNg62i4VzjK7DY_OkKQFXsyZ-BmxUKfH8deNQSQJm_bTAUNzSsCgY_TUo7rTFGFp8X-JhOsJ9uHMCHkeiutp', start_index=5011)
Annotation(end_index=5268, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkgr5uGYxyF9JDQXDgQ63EH_38GlJ3BMqFvLoEvYUN86FAbEqs2-FEg5TqUFTXnV58Q_yNAhaXvTJ0ab1r5xZc8-5GjgrPexOnUR-yX2RxTKpvkr8zMynlW3iouvSi7y908aFGKChZeA==', start_index=5256)
Annotation(end_index=5268, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeMjXZFTsYMH7tPRHRH3ZSUnJ4sRZ-_22JZ2xpZneWMRc3rzcxmD9i2SAfXCDUSab8zw0siupapOxmSfBwlELjRJ55u3YjgJZL_e2xpb4OJteclv26xrCUTTRkpTV6SfVjGtBTEwj0pFYAzLet_kCzp8bps28LhoWdqyYbzVg=', start_index=5256)
Annotation(end_index=5535, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENdYz7BSxiNQ-3HDz93iLhwSXqPf5jbit0gKe5zTsQoedIwN49PMuIMjwNLuThKD6UdJ4laZrJ1G-3cA9Liat-x-xe7WAYPmRTMsxQV8zlC1EnJZMEH43u45mmpJr3cJQb9E1svHJPq4CwzemxcuSu2Qw3JbLmFvMFSTMTFASW7gHJ5DZY9Wbdxn_clBGcM1-Z2JZbNvRXyQ==', start_index=5523)
Annotation(end_index=5535, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEOWgcT89kDcJsoH5DeJzzCLWe8FkyTzZl5dM_bP8PmClUWV9VMKJ0v8xkECOaB2l8IGe17K8fyRYgGtTHXd2arhM_JK2w4f5I0Xdd62pccaIW96V1iESa1ZgyENK35B8TVibmHNgEbejWcVBbA', start_index=5523)
Annotation(end_index=5722, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEOWgcT89kDcJsoH5DeJzzCLWe8FkyTzZl5dM_bP8PmClUWV9VMKJ0v8xkECOaB2l8IGe17K8fyRYgGtTHXd2arhM_JK2w4f5I0Xdd62pccaIW96V1iESa1ZgyENK35B8TVibmHNgEbejWcVBbA', start_index=5710)
Annotation(end_index=5722, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQu1LHbqDJeGSLRb4iUKwrK1gGKz85yTYNNgRgCo3tbLcYgc08YqGNCaqQx7v-3mom6llrKdZBTeI1tA_P1EbZ2ixeoXHtBm5kuAzm_mwd3SswSIq145N1PdYvBtmOWfwygmVQbiBThFIxVp6ws4oLngLaLhckG3LUXWEimO0NNX9ZVKGZPEpfnzdgEAv37nTa5ZbFrOOcv2dewIBEGkLxG8H7LnE=', start_index=5710)
Annotation(end_index=6264, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENdYz7BSxiNQ-3HDz93iLhwSXqPf5jbit0gKe5zTsQoedIwN49PMuIMjwNLuThKD6UdJ4laZrJ1G-3cA9Liat-x-xe7WAYPmRTMsxQV8zlC1EnJZMEH43u45mmpJr3cJQb9E1svHJPq4CwzemxcuSu2Qw3JbLmFvMFSTMTFASW7gHJ5DZY9Wbdxn_clBGcM1-Z2JZbNvRXyQ==', start_index=6255)
Annotation(end_index=6950, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQu1LHbqDJeGSLRb4iUKwrK1gGKz85yTYNNgRgCo3tbLcYgc08YqGNCaqQx7v-3mom6llrKdZBTeI1tA_P1EbZ2ixeoXHtBm5kuAzm_mwd3SswSIq145N1PdYvBtmOWfwygmVQbiBThFIxVp6ws4oLngLaLhckG3LUXWEimO0NNX9ZVKGZPEpfnzdgEAv37nTa5ZbFrOOcv2dewIBEGkLxG8H7LnE=', start_index=6938)
Annotation(end_index=6950, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeMjXZFTsYMH7tPRHRH3ZSUnJ4sRZ-_22JZ2xpZneWMRc3rzcxmD9i2SAfXCDUSab8zw0siupapOxmSfBwlELjRJ55u3YjgJZL_e2xpb4OJteclv26xrCUTTRkpTV6SfVjGtBTEwj0pFYAzLet_kCzp8bps28LhoWdqyYbzVg=', start_index=6938)
Annotation(end_index=7654, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQu1LHbqDJeGSLRb4iUKwrK1gGKz85yTYNNgRgCo3tbLcYgc08YqGNCaqQx7v-3mom6llrKdZBTeI1tA_P1EbZ2ixeoXHtBm5kuAzm_mwd3SswSIq145N1PdYvBtmOWfwygmVQbiBThFIxVp6ws4oLngLaLhckG3LUXWEimO0NNX9ZVKGZPEpfnzdgEAv37nTa5ZbFrOOcv2dewIBEGkLxG8H7LnE=', start_index=7642)
Annotation(end_index=7654, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQ9C5xo_Kc_gjkXRfDBw4NDPQzF4gAv5d3ZJEUp0s8LkWaiguMCfaEq8mUajNioQxzFTkP1ig78QNxgByxRgFxj2RoAcW7CaMC2SM952unvRpkEEwkrNnRhPqpDHwadbRAJhrz380h_Cpio-llqCz1PYGXSu67xdg=', start_index=7642)
Annotation(end_index=8504, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHEerA0AIeHHVfMsIot_QIz89ycMqWgVEPWpsFH3hbpi7huWGOmJsUinQwV4yHBLjLLSaltnMnkBcJedc6MHbyT3pZxOpd5HrZ-fxSPabLc8BMMT2nZaqemIIinHWd4o9jh9uOwRTS', start_index=8491)
Annotation(end_index=8504, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGSHqPbh__-L_wtBmGG97gBUqKLu6TSF8s8ahgzetr-u6sbQ67VA6GgAp6F0N6ffxYYsZ5-jv9qKeN2E81FXqbQS-BYCG1zJJvEP3RZZrgj9UxE_yx3aPZ40EX2Kpw2J-TiSbLgKiQ', start_index=8491)
Annotation(end_index=9337, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3oQ2qEem7ItAx2e5AaPL0vP2LaLJ1GIeMeOI0S-F-Kfdqf_LHwjN5xrVyG5zf88rp-RHA5Z9ET-O1JgAGMI3fDORXC73h2TQ2JmZDUuGoisrzlx9F7uL1Nm1LmjyLIX6qk3YGyQqZuw==', start_index=9324)
Annotation(end_index=9337, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkgr5uGYxyF9JDQXDgQ63EH_38GlJ3BMqFvLoEvYUN86FAbEqs2-FEg5TqUFTXnV58Q_yNAhaXvTJ0ab1r5xZc8-5GjgrPexOnUR-yX2RxTKpvkr8zMynlW3iouvSi7y908aFGKChZeA==', start_index=9324)
Annotation(end_index=10202, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEynvI4_ahEMHEpdXwYpROyOakAw1wiV3cYceo5FL_vaudJUhy7xFJcHav9WtN7McI9W1JKpNSh9xKQaXcHWauUALe3oKOxfn4cEMMzoU4asEUwIYFtaLJHni8-I2M6WekEgHcycxcckQS3SeVH_Aa6OVEd2d9ZCTV1lTt5_A==', start_index=10188)
Annotation(end_index=10202, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNOyn-BqjLUTzybzIfZRAL3OjVuFmLSQ_vYjUCYRE8sARizFdPbSTtK3gdByBGjm-KAYaXu1AjpOnPZyycb1LagfMFSbDP2HzI7K2ZRlESuv2r857NstUYjpd5E7s=', start_index=10188)
Annotation(end_index=10708, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEynvI4_ahEMHEpdXwYpROyOakAw1wiV3cYceo5FL_vaudJUhy7xFJcHav9WtN7McI9W1JKpNSh9xKQaXcHWauUALe3oKOxfn4cEMMzoU4asEUwIYFtaLJHni8-I2M6WekEgHcycxcckQS3SeVH_Aa6OVEd2d9ZCTV1lTt5_A==', start_index=10694)
Annotation(end_index=10708, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKQYHI5KK-kbA8BMa1rgThChLAAC2sPQ9jgFeRk4ZuU67t8ddH339zn_r4C49R_ojp6PK0RWalcJ4b_FrttVxHYAFY1ZGsdf6UTkLdM0gjRwtjvDrKjtavfKgWKwTlsLYK2lW9LZ5knwWsc6K_jvt5gYJFDmbJhTbNIU1rDayOGq1TNkotrQMEapVPSKTo2HheVDwejvvj0khrOjWqKp7H39fG2NsDu_E=', start_index=10694)
Annotation(end_index=11408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcRofjqa0g4LTKV2_i0sE_kIGTHu7VrVtAcGMgUjYJ8yLMHqn2RRyD_paZaSUtjW2lV_lBU_G4x2nuOYbmp3GIYJK8F7WpbrXe_conb_9LERC5C_dYV-A5QCuSM99P1A==', start_index=11394)
Annotation(end_index=11408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNOyn-BqjLUTzybzIfZRAL3OjVuFmLSQ_vYjUCYRE8sARizFdPbSTtK3gdByBGjm-KAYaXu1AjpOnPZyycb1LagfMFSbDP2HzI7K2ZRlESuv2r857NstUYjpd5E7s=', start_index=11394)
Annotation(end_index=11691, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKQYHI5KK-kbA8BMa1rgThChLAAC2sPQ9jgFeRk4ZuU67t8ddH339zn_r4C49R_ojp6PK0RWalcJ4b_FrttVxHYAFY1ZGsdf6UTkLdM0gjRwtjvDrKjtavfKgWKwTlsLYK2lW9LZ5knwWsc6K_jvt5gYJFDmbJhTbNIU1rDayOGq1TNkotrQMEapVPSKTo2HheVDwejvvj0khrOjWqKp7H39fG2NsDu_E=', start_index=11681)
Annotation(end_index=12779, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwHcOhIhsJLRgvT3CT23fbrE51pf3qXBnXcCJtECWQi1YxqtbNuahajhT2JbxRo4pPXcIhS4Ujnql-s4h5mmBTpxxbhZWnPe1TfcEc7lAdOSxd7PCAdHAzY1p-IFmPfLgInmFlJUMwuw==', start_index=12766)
Annotation(end_index=12779, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFfamqk5v46WIORfdEMPt091O0yMEWz6KHh__Pa88lfkLs-gFIx1HSeVnB88CKvBNOXsNEgI7TF4uWkvSK_WB6SjmwGQYUqsKosNBMyk0bD4X4TOU_XCnZ0f2KlFyS', start_index=12766)
Annotation(end_index=12998, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLRgZHJWo1ZgsV4OTpv9TYB57gqJxz8uWGF4EodXJMun1o2HmV97SdUHC0JhygOISUjUqJU9Hva0gcxj91RNmJxJS2WtGSzVdOkdEvmzkHzfiPBMBLv5ggUDN-Y8xT56xXotxW47myFA==', start_index=12988)
Annotation(end_index=13229, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjencLLWxe0LQWvNefU7ktizYYVhwAN6S-mtFomIMzvzQYC2Qvgo_hMSMxMEVsQ0fPjt0y26J4Ggt4RzgkLrd5wpzzzeSgRvmFc_YC1YVOvnZ3hz-zQ_ku7B3UeyyF', start_index=13215)
Annotation(end_index=13229, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMvY8HP4btnv2tf6sXjRU3s5rgDaqzFYeX-UpdnLHwy5i9k3K1uH6ajVAexiWI9vfLgZl9fGeK6NSaKtMQcN50Q0CC0SKlT2N_KCs5JukbPQmDfRpn5N6ayll8wyVy5tkBIrioob8=', start_index=13215)
Annotation(end_index=14102, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEOWgcT89kDcJsoH5DeJzzCLWe8FkyTzZl5dM_bP8PmClUWV9VMKJ0v8xkECOaB2l8IGe17K8fyRYgGtTHXd2arhM_JK2w4f5I0Xdd62pccaIW96V1iESa1ZgyENK35B8TVibmHNgEbejWcVBbA', start_index=14089)
Annotation(end_index=14102, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSktnhwQnVijHzFhxAn5dbzWa13ISuPvS59rl04zWGmS0LBBO_YECFfjv-f59YRh7qfCjVxOrC8ZRCXsaG65WriuIUwI2oF4hoVgZLgRz_WdmlFbdnbRC1Gj_IB2d3M9v5Or3BhX4cW9syjdc=', start_index=14089)
Annotation(end_index=14663, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3oQ2qEem7ItAx2e5AaPL0vP2LaLJ1GIeMeOI0S-F-Kfdqf_LHwjN5xrVyG5zf88rp-RHA5Z9ET-O1JgAGMI3fDORXC73h2TQ2JmZDUuGoisrzlx9F7uL1Nm1LmjyLIX6qk3YGyQqZuw==', start_index=14650)
Annotation(end_index=14663, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeMjXZFTsYMH7tPRHRH3ZSUnJ4sRZ-_22JZ2xpZneWMRc3rzcxmD9i2SAfXCDUSab8zw0siupapOxmSfBwlELjRJ55u3YjgJZL_e2xpb4OJteclv26xrCUTTRkpTV6SfVjGtBTEwj0pFYAzLet_kCzp8bps28LhoWdqyYbzVg=', start_index=14650)
Annotation(end_index=14897, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3oQ2qEem7ItAx2e5AaPL0vP2LaLJ1GIeMeOI0S-F-Kfdqf_LHwjN5xrVyG5zf88rp-RHA5Z9ET-O1JgAGMI3fDORXC73h2TQ2JmZDUuGoisrzlx9F7uL1Nm1LmjyLIX6qk3YGyQqZuw==', start_index=14883)
Annotation(end_index=14897, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4RUQGNDvFDj_-0C2vSscuDBGFt3FLhs-HcBWT_FPfrYFmBMF2nW_g_lNvPaOSk3N0R2d4LAZRV_DH95dEypzZ6-7HUbh7CBvpoVsuT52UdLrMJ5X-tVumH1Wh8Zv3YTxpYIQNdlvpb-FMpA==', start_index=14883)
Annotation(end_index=15122, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQu1LHbqDJeGSLRb4iUKwrK1gGKz85yTYNNgRgCo3tbLcYgc08YqGNCaqQx7v-3mom6llrKdZBTeI1tA_P1EbZ2ixeoXHtBm5kuAzm_mwd3SswSIq145N1PdYvBtmOWfwygmVQbiBThFIxVp6ws4oLngLaLhckG3LUXWEimO0NNX9ZVKGZPEpfnzdgEAv37nTa5ZbFrOOcv2dewIBEGkLxG8H7LnE=', start_index=15109)
Annotation(end_index=15122, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEBUFY_z550_WEth0NwDpMGXDi_56kbNfGO9PLn-t-8-pmaQeVsOzuW5vWbcCz-wP-cYfTQjgiBoOSN-S9SuS_aX2N1oC1CmwyrNQwpBa07VZ6K7p5ICGRnmw_nxc_my0AtedFzb4EsQ==', start_index=15109)
Annotation(end_index=15891, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFStL4OqvNJ-jDfUi7XUvdaZK_XXg95Hl9s4051f2F9iJWZ5DX_T6PBAqvUMenIEiIq94B7EG_yN5rUP9Unh5Is-gZKopRs7mzHxT4KsjmkA8W3uLnQMGDpG_EVxR5QusK1HO76-leHP0RfEkAZtJNXicBQaxlwqwUVF0ZhkFZKVNaK4dROjo5qw7S8nmiwujWn0mfZJyZIGJIzVK-TCDE=', start_index=15873)
Annotation(end_index=15891, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEipVKKhfcPFgiUSUr_Yo-9vKGg-rAccNAYTOqil3PX5SsYRE7o4QEAF43VtUElMXP5XB8Bg3pjEfnh-KG7o9AM5DwVXPlRM2gAPAw7Jdl-In4T-2K8BlKyxgfvYerKjn6tNYLAl5Zc9CDgi0Pbs2P6BV8ks9AkKlaEF6dav21kWYztDqlWAeNB-Uo20LaOGUOYUCLrmPs6eFPo343', start_index=15873)
Annotation(end_index=15891, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHx7Vj0a_ch6Zv63EYtPIhyC9dTuMe5KE2HnoVzHoZHH9Uv1YligeKX9Jg7s6BzOXIEHzycNaI_Byyr0K8bcNs7F2O-gb6moD39VCjwBw_6Upt89xy1M40Rh9KDFXQE8KqgRyeh9u7_51wJwC1OYN4xSlsgMuMGCqaNtmceEr9HNDCVu7ZkTTnm_hyWODzh2mmfTQ==', start_index=15873)
Annotation(end_index=16835, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkY43Fe5cxQMYdP-mVLkTwwd--XgJ5302I7eQ3EAhQnYtGO-EvZNigKfi30CwR7rCIXrTCvMP-HPFH4AfX8jiuPFRKKTeb3hNQlpzXdnsVYgKZC9ABtog7aIlnX4Zx5QfeGw==', start_index=16825)
Annotation(end_index=16919, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeMjXZFTsYMH7tPRHRH3ZSUnJ4sRZ-_22JZ2xpZneWMRc3rzcxmD9i2SAfXCDUSab8zw0siupapOxmSfBwlELjRJ55u3YjgJZL_e2xpb4OJteclv26xrCUTTRkpTV6SfVjGtBTEwj0pFYAzLet_kCzp8bps28LhoWdqyYbzVg=', start_index=16910)
Annotation(end_index=16992, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3oQ2qEem7ItAx2e5AaPL0vP2LaLJ1GIeMeOI0S-F-Kfdqf_LHwjN5xrVyG5zf88rp-RHA5Z9ET-O1JgAGMI3fDORXC73h2TQ2JmZDUuGoisrzlx9F7uL1Nm1LmjyLIX6qk3YGyQqZuw==', start_index=16979)
Annotation(end_index=16992, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkgr5uGYxyF9JDQXDgQ63EH_38GlJ3BMqFvLoEvYUN86FAbEqs2-FEg5TqUFTXnV58Q_yNAhaXvTJ0ab1r5xZc8-5GjgrPexOnUR-yX2RxTKpvkr8zMynlW3iouvSi7y908aFGKChZeA==', start_index=16979)
Annotation(end_index=17060, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHEerA0AIeHHVfMsIot_QIz89ycMqWgVEPWpsFH3hbpi7huWGOmJsUinQwV4yHBLjLLSaltnMnkBcJedc6MHbyT3pZxOpd5HrZ-fxSPabLc8BMMT2nZaqemIIinHWd4o9jh9uOwRTS', start_index=17051)
Annotation(end_index=17142, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOIdhII8MBAOoPKuR41ctwQISN2m772lZv3mmKdIX9Nml5V_3cO4Hg8KMFItWpGeBDd7QALl7pkuquJ1IYhZCUkVfoOVz8HEmQfUY9MoklJmL02RjjMPCiuQ==', start_index=17128)
Annotation(end_index=17142, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9zUN7m_OQ51GcDo-IoGHzoTKqad4Pw3pSoXs-Oe1IWIJHp-y8jJ2DZ1cIRMW1HTH778x6LTsj0PzfS9dBZflu-N213H84cdnulcFEOIEfCRjvZN8j4EETjfecG_5B', start_index=17128)
Annotation(end_index=17221, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQu1LHbqDJeGSLRb4iUKwrK1gGKz85yTYNNgRgCo3tbLcYgc08YqGNCaqQx7v-3mom6llrKdZBTeI1tA_P1EbZ2ixeoXHtBm5kuAzm_mwd3SswSIq145N1PdYvBtmOWfwygmVQbiBThFIxVp6ws4oLngLaLhckG3LUXWEimO0NNX9ZVKGZPEpfnzdgEAv37nTa5ZbFrOOcv2dewIBEGkLxG8H7LnE=', start_index=17212)
Annotation(end_index=17300, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkgr5uGYxyF9JDQXDgQ63EH_38GlJ3BMqFvLoEvYUN86FAbEqs2-FEg5TqUFTXnV58Q_yNAhaXvTJ0ab1r5xZc8-5GjgrPexOnUR-yX2RxTKpvkr8zMynlW3iouvSi7y908aFGKChZeA==', start_index=17291)
Annotation(end_index=17407, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGer_XnMM3vNlK1-sziU2Q3FL_YSgBkjk4aEPZwiLb46g8xP2TF6kuzDE1DpvV03x0S6dDzA0oX7WHfmy9vr36rQfSYtcLrDAdZhOJaMEoLMv98N4ymOMv7rxR0niftSiI9W4AILlYqyg==', start_index=17397)
Annotation(end_index=17960, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEipVKKhfcPFgiUSUr_Yo-9vKGg-rAccNAYTOqil3PX5SsYRE7o4QEAF43VtUElMXP5XB8Bg3pjEfnh-KG7o9AM5DwVXPlRM2gAPAw7Jdl-In4T-2K8BlKyxgfvYerKjn6tNYLAl5Zc9CDgi0Pbs2P6BV8ks9AkKlaEF6dav21kWYztDqlWAeNB-Uo20LaOGUOYUCLrmPs6eFPo343', start_index=17946)
Annotation(end_index=17960, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHx7Vj0a_ch6Zv63EYtPIhyC9dTuMe5KE2HnoVzHoZHH9Uv1YligeKX9Jg7s6BzOXIEHzycNaI_Byyr0K8bcNs7F2O-gb6moD39VCjwBw_6Upt89xy1M40Rh9KDFXQE8KqgRyeh9u7_51wJwC1OYN4xSlsgMuMGCqaNtmceEr9HNDCVu7ZkTTnm_hyWODzh2mmfTQ==', start_index=17946)
Annotation(end_index=18231, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHEerA0AIeHHVfMsIot_QIz89ycMqWgVEPWpsFH3hbpi7huWGOmJsUinQwV4yHBLjLLSaltnMnkBcJedc6MHbyT3pZxOpd5HrZ-fxSPabLc8BMMT2nZaqemIIinHWd4o9jh9uOwRTS', start_index=18222)
Annotation(end_index=18482, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwHcOhIhsJLRgvT3CT23fbrE51pf3qXBnXcCJtECWQi1YxqtbNuahajhT2JbxRo4pPXcIhS4Ujnql-s4h5mmBTpxxbhZWnPe1TfcEc7lAdOSxd7PCAdHAzY1p-IFmPfLgInmFlJUMwuw==', start_index=18469)
Annotation(end_index=18482, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGljLKSRs-nj9Q--8HMEEtVrsUnlhL0tBpNaG0fA57phCVHMSODEPbHMYQkJHQT2CaPVszK9OERmdbThNF8yW8-fO0W0OfFpXnJ2zWzSN-QV5oKMB5HP9cyty2y5tl_ZoisBTmVjtcIAnw1og4rQKej79ruUPsJFOOS2syjv44CM0yhOOt-VGF4rRiQR_dvRyMW', start_index=18469)
Annotation(end_index=18739, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEynvI4_ahEMHEpdXwYpROyOakAw1wiV3cYceo5FL_vaudJUhy7xFJcHav9WtN7McI9W1JKpNSh9xKQaXcHWauUALe3oKOxfn4cEMMzoU4asEUwIYFtaLJHni8-I2M6WekEgHcycxcckQS3SeVH_Aa6OVEd2d9ZCTV1lTt5_A==', start_index=18725)
Annotation(end_index=18739, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNOyn-BqjLUTzybzIfZRAL3OjVuFmLSQ_vYjUCYRE8sARizFdPbSTtK3gdByBGjm-KAYaXu1AjpOnPZyycb1LagfMFSbDP2HzI7K2ZRlESuv2r857NstUYjpd5E7s=', start_index=18725)
Annotation(end_index=19412, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwHcOhIhsJLRgvT3CT23fbrE51pf3qXBnXcCJtECWQi1YxqtbNuahajhT2JbxRo4pPXcIhS4Ujnql-s4h5mmBTpxxbhZWnPe1TfcEc7lAdOSxd7PCAdHAzY1p-IFmPfLgInmFlJUMwuw==', start_index=19403)
Annotation(end_index=19487, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjDu09SEUplpmX0B8vUwBT6d2Hn9PkVR5ZCgAXP_fuN27_WP9IG8eMk2J2YKaVgXjUMKZbNs5ktdMSClzp0ZrtwbwWO4sVfeRXULniC0yWZ-1uxKcn2QSqn0D0u8t1L-vDxkrr6I3fBJwFpp-_dfyqezwWabo1H25Ov5PDxbIJMsUvzsA=', start_index=19477)
Annotation(end_index=19564, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcWBV3TFLiMlVDCMItWu5LOMa-CJHkdKTXYOFSkqF6Vb1I721kQeyPH94-9n2DSyLN-L-5Qj_wppEyLVdcLI0h5lkiqI7M5hv5MxY4sYghN6IJXvfKS_Y6RPW2JEMNLXRb7P9hYX16tGaZAg==', start_index=19554)
Annotation(end_index=19621, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENdYz7BSxiNQ-3HDz93iLhwSXqPf5jbit0gKe5zTsQoedIwN49PMuIMjwNLuThKD6UdJ4laZrJ1G-3cA9Liat-x-xe7WAYPmRTMsxQV8zlC1EnJZMEH43u45mmpJr3cJQb9E1svHJPq4CwzemxcuSu2Qw3JbLmFvMFSTMTFASW7gHJ5DZY9Wbdxn_clBGcM1-Z2JZbNvRXyQ==', start_index=19612)
Annotation(end_index=19662, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjencLLWxe0LQWvNefU7ktizYYVhwAN6S-mtFomIMzvzQYC2Qvgo_hMSMxMEVsQ0fPjt0y26J4Ggt4RzgkLrd5wpzzzeSgRvmFc_YC1YVOvnZ3hz-zQ_ku7B3UeyyF', start_index=19652)
Annotation(end_index=19740, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkgr5uGYxyF9JDQXDgQ63EH_38GlJ3BMqFvLoEvYUN86FAbEqs2-FEg5TqUFTXnV58Q_yNAhaXvTJ0ab1r5xZc8-5GjgrPexOnUR-yX2RxTKpvkr8zMynlW3iouvSi7y908aFGKChZeA==', start_index=19731)
Annotation(end_index=19790, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeMjXZFTsYMH7tPRHRH3ZSUnJ4sRZ-_22JZ2xpZneWMRc3rzcxmD9i2SAfXCDUSab8zw0siupapOxmSfBwlELjRJ55u3YjgJZL_e2xpb4OJteclv26xrCUTTRkpTV6SfVjGtBTEwj0pFYAzLet_kCzp8bps28LhoWdqyYbzVg=', start_index=19781)
Annotation(end_index=19858, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9zUN7m_OQ51GcDo-IoGHzoTKqad4Pw3pSoXs-Oe1IWIJHp-y8jJ2DZ1cIRMW1HTH778x6LTsj0PzfS9dBZflu-N213H84cdnulcFEOIEfCRjvZN8j4EETjfecG_5B', start_index=19848)
Annotation(end_index=19922, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5005g6h0WE8LZux2pZbSVz_cN8IKHCSKMCNTpSYpLB6XPwsItNfthNNg62i4VzjK7DY_OkKQFXsyZ-BmxUKfH8deNQSQJm_bTAUNzSsCgY_TUo7rTFGFp8X-JhOsJ9uHMCHkeiutp', start_index=19913)
Annotation(end_index=19985, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSktnhwQnVijHzFhxAn5dbzWa13ISuPvS59rl04zWGmS0LBBO_YECFfjv-f59YRh7qfCjVxOrC8ZRCXsaG65WriuIUwI2oF4hoVgZLgRz_WdmlFbdnbRC1Gj_IB2d3M9v5Or3BhX4cW9syjdc=', start_index=19975)
Annotation(end_index=20037, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGljLKSRs-nj9Q--8HMEEtVrsUnlhL0tBpNaG0fA57phCVHMSODEPbHMYQkJHQT2CaPVszK9OERmdbThNF8yW8-fO0W0OfFpXnJ2zWzSN-QV5oKMB5HP9cyty2y5tl_ZoisBTmVjtcIAnw1og4rQKej79ruUPsJFOOS2syjv44CM0yhOOt-VGF4rRiQR_dvRyMW', start_index=20027)
Annotation(end_index=20109, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEOWgcT89kDcJsoH5DeJzzCLWe8FkyTzZl5dM_bP8PmClUWV9VMKJ0v8xkECOaB2l8IGe17K8fyRYgGtTHXd2arhM_JK2w4f5I0Xdd62pccaIW96V1iESa1ZgyENK35B8TVibmHNgEbejWcVBbA', start_index=20100)
Annotation(end_index=20176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGq5vsrY34WqfDoyQ7b3Ehp1rfPbOSWigfLo3CEGqglVHpsa9aZWFm9fr60AQH1qJTvnaVjCu5THuipJtH-CSQb4S6z836OqI5hG4agZpVpglzyJjuoS7DEpw4TZhdyUjeBGeB85d5u', start_index=20166)
Annotation(end_index=20233, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQu1LHbqDJeGSLRb4iUKwrK1gGKz85yTYNNgRgCo3tbLcYgc08YqGNCaqQx7v-3mom6llrKdZBTeI1tA_P1EbZ2ixeoXHtBm5kuAzm_mwd3SswSIq145N1PdYvBtmOWfwygmVQbiBThFIxVp6ws4oLngLaLhckG3LUXWEimO0NNX9ZVKGZPEpfnzdgEAv37nTa5ZbFrOOcv2dewIBEGkLxG8H7LnE=', start_index=20224)
Annotation(end_index=20295, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3oQ2qEem7ItAx2e5AaPL0vP2LaLJ1GIeMeOI0S-F-Kfdqf_LHwjN5xrVyG5zf88rp-RHA5Z9ET-O1JgAGMI3fDORXC73h2TQ2JmZDUuGoisrzlx9F7uL1Nm1LmjyLIX6qk3YGyQqZuw==', start_index=20285)
Annotation(end_index=20351, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE30t4kclw9Htv3bSTmzgcQ2LaorrBj-KNiqpPiuGZGJMhmonAsnJV-jeey1tPnAUn1LVvVQgtLtuMUuvbbduM-AXam974xy3DdsNX1xCiewn3icK2XaOJOyPEVQbhSdhPNVg9ogWnn', start_index=20341)
Annotation(end_index=20407, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHEerA0AIeHHVfMsIot_QIz89ycMqWgVEPWpsFH3hbpi7huWGOmJsUinQwV4yHBLjLLSaltnMnkBcJedc6MHbyT3pZxOpd5HrZ-fxSPabLc8BMMT2nZaqemIIinHWd4o9jh9uOwRTS', start_index=20398)
Annotation(end_index=20484, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4RUQGNDvFDj_-0C2vSscuDBGFt3FLhs-HcBWT_FPfrYFmBMF2nW_g_lNvPaOSk3N0R2d4LAZRV_DH95dEypzZ6-7HUbh7CBvpoVsuT52UdLrMJ5X-tVumH1Wh8Zv3YTxpYIQNdlvpb-FMpA==', start_index=20474)
Annotation(end_index=20534, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFfamqk5v46WIORfdEMPt091O0yMEWz6KHh__Pa88lfkLs-gFIx1HSeVnB88CKvBNOXsNEgI7TF4uWkvSK_WB6SjmwGQYUqsKosNBMyk0bD4X4TOU_XCnZ0f2KlFyS', start_index=20524)
Annotation(end_index=20613, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9LQplxvpT-U1nunKA15TMzfXFOm3PuD7i0gAAkMATAiO8AldC0rrr-pHPcDRh2mMzIzYhfQ6T4__9BC15dEiYuJ3r7Nd-72coffjsvxuVRxNORjXFJDcFDEryJ1aehN_8Cid0sioyVoNGrM-xDCQzwQNtBX8QlplgC-LmbTaTsMdbX5YUqplFfmTyp5IFZx89', start_index=20603)
Annotation(end_index=20681, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRpMmzSJSLcc9tV1Y-EEm2C61ena_kESN7T3paQMV9z8tRLx4usV4vPANbMr7k76HCYcJQQEO6nWcc6cZYmR8Urxmap0F3_XO-JijQL8JPguaMa33S2GDRkhf5fy_3cFCiz2usvha6', start_index=20671)
Annotation(end_index=20738, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQ9C5xo_Kc_gjkXRfDBw4NDPQzF4gAv5d3ZJEUp0s8LkWaiguMCfaEq8mUajNioQxzFTkP1ig78QNxgByxRgFxj2RoAcW7CaMC2SM952unvRpkEEwkrNnRhPqpDHwadbRAJhrz380h_Cpio-llqCz1PYGXSu67xdg=', start_index=20729)
Annotation(end_index=20795, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3oQ2qEem7ItAx2e5AaPL0vP2LaLJ1GIeMeOI0S-F-Kfdqf_LHwjN5xrVyG5zf88rp-RHA5Z9ET-O1JgAGMI3fDORXC73h2TQ2JmZDUuGoisrzlx9F7uL1Nm1LmjyLIX6qk3YGyQqZuw==', start_index=20785)
Annotation(end_index=20850, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEeH-PtnnahwpDE6-WlZPvABGNhZjiHBLrWfXhhsAkq6O3WBcZDX8z3yomZe2HbVHk9L3wsofI84eEruqp94ErB08aU8pzJAJjclq5FwMB4bqqkm5fTKkhl', start_index=20840)
Annotation(end_index=20907, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGer_XnMM3vNlK1-sziU2Q3FL_YSgBkjk4aEPZwiLb46g8xP2TF6kuzDE1DpvV03x0S6dDzA0oX7WHfmy9vr36rQfSYtcLrDAdZhOJaMEoLMv98N4ymOMv7rxR0niftSiI9W4AILlYqyg==', start_index=20897)
Annotation(end_index=20970, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMvY8HP4btnv2tf6sXjRU3s5rgDaqzFYeX-UpdnLHwy5i9k3K1uH6ajVAexiWI9vfLgZl9fGeK6NSaKtMQcN50Q0CC0SKlT2N_KCs5JukbPQmDfRpn5N6ayll8wyVy5tkBIrioob8=', start_index=20960)
Annotation(end_index=21004, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNOyn-BqjLUTzybzIfZRAL3OjVuFmLSQ_vYjUCYRE8sARizFdPbSTtK3gdByBGjm-KAYaXu1AjpOnPZyycb1LagfMFSbDP2HzI7K2ZRlESuv2r857NstUYjpd5E7s=', start_index=20994)
Annotation(end_index=21067, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEipVKKhfcPFgiUSUr_Yo-9vKGg-rAccNAYTOqil3PX5SsYRE7o4QEAF43VtUElMXP5XB8Bg3pjEfnh-KG7o9AM5DwVXPlRM2gAPAw7Jdl-In4T-2K8BlKyxgfvYerKjn6tNYLAl5Zc9CDgi0Pbs2P6BV8ks9AkKlaEF6dav21kWYztDqlWAeNB-Uo20LaOGUOYUCLrmPs6eFPo343', start_index=21057)
Annotation(end_index=21128, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEBUFY_z550_WEth0NwDpMGXDi_56kbNfGO9PLn-t-8-pmaQeVsOzuW5vWbcCz-wP-cYfTQjgiBoOSN-S9SuS_aX2N1oC1CmwyrNQwpBa07VZ6K7p5ICGRnmw_nxc_my0AtedFzb4EsQ==', start_index=21118)
Annotation(end_index=21176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFStL4OqvNJ-jDfUi7XUvdaZK_XXg95Hl9s4051f2F9iJWZ5DX_T6PBAqvUMenIEiIq94B7EG_yN5rUP9Unh5Is-gZKopRs7mzHxT4KsjmkA8W3uLnQMGDpG_EVxR5QusK1HO76-leHP0RfEkAZtJNXicBQaxlwqwUVF0ZhkFZKVNaK4dROjo5qw7S8nmiwujWn0mfZJyZIGJIzVK-TCDE=', start_index=21166)
Annotation(end_index=21235, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8Y0Fosz6SaqyRfOGP2IRpb-cPm4l2hSFI9mK8evtl90FFowoN7-VSipoQhLwJxGBScC6PXuLGnlCP4gqA4R6fu3WVhP5t1oHhxFsgtkhU0lywCfxNHx4jkNPG0E_nPf2gXNWbYnqveYZgaww=', start_index=21225)
Annotation(end_index=21285, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHx7Vj0a_ch6Zv63EYtPIhyC9dTuMe5KE2HnoVzHoZHH9Uv1YligeKX9Jg7s6BzOXIEHzycNaI_Byyr0K8bcNs7F2O-gb6moD39VCjwBw_6Upt89xy1M40Rh9KDFXQE8KqgRyeh9u7_51wJwC1OYN4xSlsgMuMGCqaNtmceEr9HNDCVu7ZkTTnm_hyWODzh2mmfTQ==', start_index=21275)
Annotation(end_index=21352, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEynvI4_ahEMHEpdXwYpROyOakAw1wiV3cYceo5FL_vaudJUhy7xFJcHav9WtN7McI9W1JKpNSh9xKQaXcHWauUALe3oKOxfn4cEMMzoU4asEUwIYFtaLJHni8-I2M6WekEgHcycxcckQS3SeVH_Aa6OVEd2d9ZCTV1lTt5_A==', start_index=21342)
Annotation(end_index=21414, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKQYHI5KK-kbA8BMa1rgThChLAAC2sPQ9jgFeRk4ZuU67t8ddH339zn_r4C49R_ojp6PK0RWalcJ4b_FrttVxHYAFY1ZGsdf6UTkLdM0gjRwtjvDrKjtavfKgWKwTlsLYK2lW9LZ5knwWsc6K_jvt5gYJFDmbJhTbNIU1rDayOGq1TNkotrQMEapVPSKTo2HheVDwejvvj0khrOjWqKp7H39fG2NsDu_E=', start_index=21404)
Annotation(end_index=21477, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcRofjqa0g4LTKV2_i0sE_kIGTHu7VrVtAcGMgUjYJ8yLMHqn2RRyD_paZaSUtjW2lV_lBU_G4x2nuOYbmp3GIYJK8F7WpbrXe_conb_9LERC5C_dYV-A5QCuSM99P1A==', start_index=21467)
Annotation(end_index=21523, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_mB9siqfnWWLqeusArdSdVeqlVeKQmEPdD4d3WH48hSi3DUQaZLJgJGv6XN70xK2JuhICImeaTC10lphCaXhXCqlHYiqVPrXLe1Y4PFy6mVaDWBsufwZFulh38h1Kg_RhumN5UslHiTWN50E=', start_index=21513)
Annotation(end_index=21587, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLRgZHJWo1ZgsV4OTpv9TYB57gqJxz8uWGF4EodXJMun1o2HmV97SdUHC0JhygOISUjUqJU9Hva0gcxj91RNmJxJS2WtGSzVdOkdEvmzkHzfiPBMBLv5ggUDN-Y8xT56xXotxW47myFA==', start_index=21577)
Annotation(end_index=21657, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHEerA0AIeHHVfMsIot_QIz89ycMqWgVEPWpsFH3hbpi7huWGOmJsUinQwV4yHBLjLLSaltnMnkBcJedc6MHbyT3pZxOpd5HrZ-fxSPabLc8BMMT2nZaqemIIinHWd4o9jh9uOwRTS', start_index=21648)
Annotation(end_index=21711, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGSHqPbh__-L_wtBmGG97gBUqKLu6TSF8s8ahgzetr-u6sbQ67VA6GgAp6F0N6ffxYYsZ5-jv9qKeN2E81FXqbQS-BYCG1zJJvEP3RZZrgj9UxE_yx3aPZ40EX2Kpw2J-TiSbLgKiQ', start_index=21701)
Annotation(end_index=21763, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkY43Fe5cxQMYdP-mVLkTwwd--XgJ5302I7eQ3EAhQnYtGO-EvZNigKfi30CwR7rCIXrTCvMP-HPFH4AfX8jiuPFRKKTeb3hNQlpzXdnsVYgKZC9ABtog7aIlnX4Zx5QfeGw==', start_index=21753)

## Sources
