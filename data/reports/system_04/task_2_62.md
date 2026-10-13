# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** c3e83fa1 | **Time:** 342.55s | **Cost:** $1.72993
--------------------------------------------------------------------------------

# Optimization of Solid Tumor Chemotherapy Dosing: Balancing Tumor Cytotoxicity with Hematopoietic Recovery

**Key Points**
*   **The Therapeutic Index Challenge:** Chemotherapy dosing is a critical optimization problem constrained by the narrow therapeutic index between tumor cytotoxicity and host toxicity, particularly myelosuppression (neutropenia and thrombocytopenia).
*   **Mathematical Modeling of Hematopoiesis:** The Friberg model serves as the gold standard for predicting chemotherapy-induced myelosuppression. It utilizes a semi-mechanistic framework involving proliferating, transit, and circulating compartments to predict the depth (nadir) and duration of neutropenia based on drug exposure.
*   **Biomarker Loads and the "Sink Effect":** In specific contexts like radioligand therapy (RLT) for solid tumors (e.g., prostate cancer), tumor burden acts as a "biomarker load" that creates a "sink effect." High tumor burden can sequester therapeutic agents, potentially protecting healthy organs (like bone marrow) from toxicity, whereas low tumor burden may paradoxically increase hematological toxicity risk, necessitating inverse dose adjustments.
*   **Model-Informed Precision Dosing (MIPD):** Moving beyond Body Surface Area (BSA) dosing, MIPD integrates patient-specific covariates (renal function, prior toxicity, body composition) and therapeutic drug monitoring (TDM) to individualize doses. This approach aims to maximize efficacy while keeping hematological toxicity within manageable thresholds (e.g., ANC > 1.5 x 10⁹/L).
*   **Adaptive Therapy:** Emerging strategies utilize evolutionary game theory to adjust doses dynamically. Rather than maintaining Maximum Tolerated Dose (MTD), adaptive therapy modulates dosing based on tumor burden response to maintain a population of sensitive cells that suppress resistant phenotypes, often resulting in lower cumulative toxicity and preserved hematopoietic function.

## 1. Introduction

The administration of cytotoxic chemotherapy for solid tumors represents a complex balancing act between maximizing tumor cell kill and preserving the functional integrity of healthy tissues, most notably the hematopoietic system. The bone marrow is frequently the dose-limiting organ for many antineoplastic agents due to the high proliferation rate of hematopoietic stem and progenitor cells (HSPCs), rendering them collaterally sensitive to drugs targeting rapidly dividing tumor cells [cite: 1, 2].

Historically, chemotherapy dosing has relied on the Maximum Tolerated Dose (MTD) paradigm, determined in Phase I clinical trials, and standardized using Body Surface Area (BSA) [cite: 3, 4]. However, this "one-size-fits-all" approach often fails to account for significant inter-individual variability in pharmacokinetics (PK) and pharmacodynamics (PD), leading to either underdosing (therapeutic failure) or overdosing (life-threatening toxicity) [cite: 5, 6].

This report examines the mechanisms and methodologies used to adjust chemotherapy doses to balance these competing objectives. It explores the physiological basis of hematopoietic recovery, the mathematical models (specifically the Friberg model) used to predict toxicity, the influence of biomarker loads (including tumor burden and the "sink effect"), and the clinical guidelines governing dose modifications. Furthermore, it details advanced strategies such as Model-Informed Precision Dosing (MIPD) and adaptive therapy, which integrate tumor dynamics and toxicity constraints to optimize treatment outcomes.

## 2. Pathophysiology of Chemotherapy-Induced Hematological Toxicity

To understand dose adjustment strategies, one must first understand the biological constraints imposed by the hematopoietic system. Chemotherapy-induced myelosuppression, particularly neutropenia and thrombocytopenia, is the most common dose-limiting toxicity (DLT) in solid tumor treatment [cite: 1, 7].

### 2.1 The Hematopoietic Hierarchy and Drug Sensitivity
Hematopoiesis is a hierarchical process where quiescent Hematopoietic Stem Cells (HSCs) differentiate into rapidly dividing progenitor cells and finally into mature blood cells. Cytotoxic drugs, such as taxanes, anthracyclines, and alkylating agents, primarily target the rapidly dividing progenitor cells rather than the quiescent HSCs or the fully mature circulating cells [cite: 8, 9].

*   **Neutrophils:** Due to their short half-life (6–12 hours) and rapid turnover, neutrophils are the first lineage to exhibit depletion. The "nadir" (lowest count) typically occurs 10–14 days post-administration, with recovery dependent on the replenishment of the progenitor pool [cite: 10, 11].
*   **Platelets:** Thrombocytopenia follows a slightly different kinetic profile due to the maturation time of megakaryocytes. Severe thrombocytopenia (e.g., <25 x 10⁹/L) increases bleeding risk and often necessitates dose delays [cite: 11, 12].
*   **The "Bottleneck" Effect:** Chemotherapy creates a bottleneck by depleting the transit population (progenitors). Recovery requires the recruitment of quiescent HSCs into the cell cycle. Repeated cycles of high-dose chemotherapy can exhaust the stem cell reserve or damage the microenvironment (niche), leading to cumulative or prolonged myelosuppression [cite: 8, 13].

### 2.2 Clinical Toxicity Thresholds
Dose adjustments are triggered when hematological parameters breach specific safety thresholds, defined by the Common Terminology Criteria for Adverse Events (CTCAE).

*   **Neutropenia:**
    *   **Grade 3:** ANC 0.5 – 1.0 x 10⁹/L.
    *   **Grade 4:** ANC < 0.5 x 10⁹/L.
    *   **Clinical Action:** Most protocols require ANC recovery to $\ge$ 1.5 x 10⁹/L before starting a new cycle. Grade 4 neutropenia or Febrile Neutropenia (FN) usually mandates a dose reduction (e.g., 20-25%) or the addition of Granulocyte-Colony Stimulating Factor (G-CSF) [cite: 14].
*   **Thrombocytopenia:**
    *   **Thresholds:** Treatment is often held if platelets are < 75–100 x 10⁹/L.
    *   **Surgical/Interventional Threshold:** < 50 x 10⁹/L.
    *   **Critical Bleeding Risk:** < 10–25 x 10⁹/L [cite: 11, 12, 15].

## 3. Mathematical Modeling of Myelosuppression: The Friberg Model

The adjustment of chemotherapy doses to balance tumor kill with hematopoietic recovery has been significantly advanced by semi-mechanistic mathematical modeling. The most influential framework in this domain is the **Friberg Model**, developed to describe chemotherapy-induced myelosuppression [cite: 9, 16, 17].

### 3.1 Structure of the Friberg Model
The Friberg model links the pharmacokinetics (PK) of a drug to the pharmacodynamics (PD) of the neutrophil count. It conceptualizes the hematopoietic system as a series of compartments [cite: 9, 16]:

1.  **Proliferative Compartment ($Prol$):** Represents stem cells and early progenitors that are sensitive to cytotoxic drugs.
2.  **Transit Compartments ($T_1, T_2, T_3$):** Represent the maturation chain of non-mitotic cells (e.g., myelocytes, metamyelocytes, bands) which are generally insensitive to chemotherapy. The number of compartments (usually 3) determines the shape of the time-delay curve.
3.  **Circulating Compartment ($Circ$):** Represents mature neutrophils in the blood.

### 3.2 Governing Equations and Feedback Mechanisms
The model is governed by a system of ordinary differential equations (ODEs). A critical component is the negative feedback loop, where the proliferation rate of stem cells is regulated by the concentration of circulating neutrophils. When circulating neutrophils drop (neutropenia), the system upregulates proliferation to accelerate recovery [cite: 18, 19].

The proliferation rate ($k_{prol}$) is modified by a feedback factor:
\[ \text{Feedback} = \left( \frac{Circ_0}{Circ(t)} \right)^\gamma \]
Where:
*   $Circ_0$ is the baseline neutrophil count.
*   $Circ(t)$ is the count at time $t$.
*   $\gamma$ is the feedback parameter determining the intensity of the rebound response.

The drug effect ($E_{drug}$) inhibits proliferation, typically modeled as a linear function of drug concentration ($C_p$) or an $E_{max}$ model:
\[ E_{drug} = \text{Slope} \times C_p \quad \text{or} \quad E_{drug} = \frac{E_{max} \times C_p}{EC_{50} + C_p} \]

The transit time through the maturation compartments is defined by the Mean Transit Time ($MTT$), which dictates the delay between drug administration and the observed nadir [cite: 16, 20].

### 3.3 Clinical Application of the Model
The Friberg model allows clinicians and pharmacometricians to:
*   **Predict Nadir:** By estimating drug-specific parameters (Slope) and patient-specific parameters ($MTT$, $Circ_0$), the model predicts the depth of the nadir.
*   **Optimize Intervals:** It helps determine the minimum safe interval between cycles to allow $Circ$ to return to baseline.
*   **Simulate Regimens:** It allows for the simulation of fractionated dosing or "dose-dense" regimens to see if they will cause cumulative toxicity [cite: 21, 22].
*   **Consistency Across Drugs:** The model has been successfully applied to various agents, including etoposide, paclitaxel, docetaxel, and irinotecan, demonstrating that the system-related parameters ($MTT$, $\gamma$) remain relatively consistent while drug potency varies [cite: 9, 17].

## 4. Biomarker Loads and the "Tumor Sink Effect"

The query specifically asks about "biomarker loads." In the context of solid tumor treatment, this refers to the total burden of tumor antigen or tumor volume, which can significantly alter the pharmacokinetics and biodistribution of therapeutic agents. This is most prominently observed in **Radioligand Therapy (RLT)** (e.g., $^{177}$Lu-PSMA for prostate cancer or $^{177}$Lu-DOTATATE for neuroendocrine tumors), but the principles of tumor burden influencing dosing extend to other modalities [cite: 23, 24].

### 4.1 The Tumor Sink Effect
The "Tumor Sink Effect" describes a phenomenon where a high volume of tumor tissue (high biomarker load) sequesters a large proportion of the administered drug (specifically targeted radiopharmaceuticals). This sequestration reduces the amount of drug available to circulate to healthy organs-at-risk (OARs), such as the bone marrow, kidneys, and salivary glands [cite: 23, 25].

*   **High Tumor Burden:**
    *   **Mechanism:** Massive expression of the target (e.g., PSMA) acts as a "sink," rapidly clearing the agent from the blood.
    *   **Consequence:** Lower absorbed dose to the bone marrow and kidneys.
    *   **Dosing Implication:** Patients with very high tumor burdens might tolerate *higher* or *more frequent* doses because their healthy tissues are relatively spared ("shielded") by the tumor sink [cite: 23, 26]. Conversely, they may require higher doses to ensure sufficient penetration into the tumor mass itself [cite: 27].

*   **Low Tumor Burden:**
    *   **Mechanism:** Less tumor tissue is available to bind the drug, leaving more free drug circulating in the blood.
    *   **Consequence:** Higher uptake in off-target organs (e.g., salivary glands, bone marrow), increasing the risk of hematological toxicity (anemia, thrombocytopenia) [cite: 24, 28].
    *   **Dosing Implication:** Patients with low tumor burden (e.g., micrometastatic disease) may require *dose reduction* or careful monitoring to prevent toxicity, as the "sink" protection is absent [cite: 29, 30].

### 4.2 Tumor Burden and Cytotoxic Chemotherapy
In traditional cytotoxic chemotherapy, the relationship between tumor burden and dosing is less about a "sink" and more about **resistance and heterogeneity**.
*   **Goldie-Coldman Hypothesis:** Larger tumors (high burden) are more likely to contain drug-resistant clones. This historically justified "dose-intense" strategies to eradicate resistant cells before they dominate [cite: 7].
*   **Toxicity Correlation:** High tumor burden often correlates with poor performance status and prior heavy pretreatment, which are independent risk factors for severe hematological toxicity. Thus, while high burden theoretically demands high doses for efficacy, patient frailty often necessitates dose reduction [cite: 28, 31].
*   **Neutrophil Dynamics:** Some studies suggest that high tumor burden can suppress immune function or alter neutrophil dynamics (e.g., via G-CSF secretion by tumors), complicating the recovery prediction [cite: 32, 33].

## 5. Model-Informed Precision Dosing (MIPD)

To address the limitations of BSA-based dosing and integrate factors like biomarker load and toxicity thresholds, oncology is shifting toward **Model-Informed Precision Dosing (MIPD)**. MIPD uses mathematical models to individualize dosing regimens [cite: 5, 6].

### 5.1 A Priori vs. A Posteriori Adjustment
*   **A Priori (Before Treatment):** Doses are selected based on patient covariates included in population PK (popPK) models.
    *   *Covariates:* Renal function (GFR), liver function, age, body composition (sarcopenia vs. obesity), and genetic variants (e.g., DPYD for 5-FU) [cite: 5].
    *   *Obesity:* Guidelines suggest using actual body weight rather than capped doses for obese patients to avoid underdosing, as evidence suggests toxicity is not disproportionately higher [cite: 3, 34].
*   **A Posteriori (During Treatment):** Doses are adjusted based on observed feedback (Therapeutic Drug Monitoring or Toxicity).
    *   *TDM:* Measuring plasma drug concentrations (e.g., 5-FU, methotrexate, busulfan) to ensure they fall within a therapeutic window [cite: 4, 5].
    *   *Toxicity-Guided:* Using the previous cycle's ANC nadir to adjust the next cycle's dose. If a patient experiences Grade 4 neutropenia, the model calculates the exact dose reduction needed to keep the next nadir above the threshold (e.g., > 0.5 x 10⁹/L) rather than an arbitrary 25% cut [cite: 20, 35].

### 5.2 Bayesian Forecasting
MIPD often employs Bayesian forecasting. The model starts with "priors" (population averages). As patient-specific data (drug levels or neutrophil counts) becomes available, the model updates the "posteriors" (individual parameters). This allows the model to "learn" the patient's specific sensitivity and clearance, refining dose recommendations with each cycle to balance tumor kill (exposure) with safety [cite: 35, 36].

## 6. Adaptive Therapy: Integrating Evolutionary Dynamics

While MIPD optimizes *standard* dosing to hit specific targets, **Adaptive Therapy** rethinks the *strategy* of dosing itself. It is based on evolutionary game theory and challenges the MTD paradigm [cite: 37, 38].

### 6.1 The Evolutionary Rationale
Standard high-dose chemotherapy (MTD) kills sensitive cells efficiently but selects for resistant cells (competitive release), leading to treatment failure. Adaptive therapy aims to keep the tumor volume stable (or slowly declining) by maintaining a population of sensitive cells. These sensitive cells compete with resistant cells for resources (space, nutrients), suppressing the outgrowth of the resistant population [cite: 38, 39].

### 6.2 Dosing Algorithms and Toxicity
Adaptive protocols adjust doses based on **tumor burden** (biomarker load) measured dynamically (e.g., via PSA or imaging).
*   **Algorithm:** If tumor burden decreases below a threshold (e.g., 50% of baseline), therapy is paused or reduced. If it grows, therapy is restarted or increased [cite: 37, 39].
*   **Hematological Benefit:** Because adaptive therapy often uses lower cumulative doses and includes treatment holidays, it generally results in less severe hematological toxicity compared to MTD. This allows for better hematopoietic recovery and maintenance of the patient's immune reserve [cite: 40, 41].
*   **Toxicity Constraints:** Recent mathematical frameworks explicitly integrate toxicity constraints into adaptive algorithms. For example, a model might optimize tumor control subject to the constraint that the cumulative toxicity (or ANC nadir) does not violate a safety limit. If toxicity is too high, the dose is capped, even if tumor burden suggests a higher dose is needed [cite: 37].

## 7. Clinical Guidelines for Dose Modification

Despite the sophistication of mathematical models, clinical practice relies on established guidelines (e.g., NCCN, ASCO) to manage the balance between efficacy and toxicity.

### 7.1 Management of Neutropenia
*   **Prophylaxis:** G-CSF (filgrastim, pegfilgrastim) is recommended if the risk of Febrile Neutropenia (FN) is > 20%. This allows for the maintenance of Dose Intensity (DI) [cite: 7, 42].
*   **Dose Delays:** If ANC is < 1.5 x 10⁹/L on the day of treatment, therapy is typically delayed by 1 week to allow marrow recovery [cite: 14].
*   **Dose Reductions:** If a patient experiences FN or prolonged Grade 4 neutropenia despite G-CSF, the dose of the causative agent is reduced (usually by 15-25%) for subsequent cycles [cite: 43, 44].

### 7.2 Management of Thrombocytopenia
*   **Thresholds:** Treatment is held for platelets < 75–100 x 10⁹/L.
*   **Recovery:** Unlike neutrophils, there are no highly effective agents for acute chemotherapy-induced thrombocytopenia (though thrombopoietin agonists are studied). Management relies heavily on dose delays and reductions [cite: 11, 12].

### 7.3 Dose Rounding and Efficiency
To reduce waste and improve pharmacy workflow without compromising efficacy, guidelines support dose rounding (e.g., within 5-10% of the calculated dose). This practice is considered clinically insignificant regarding tumor control but simplifies administration [cite: 45].

## 8. Conclusion

Balancing tumor cell killing with hematopoietic recovery is a dynamic optimization problem.
1.  **Standard of Care:** Currently relies on BSA-based dosing with reactive adjustments (delays/reductions) based on toxicity thresholds (ANC < 1.5 x 10⁹/L, Platelets < 100 x 10⁹/L) [cite: 14, 43].
2.  **Mathematical Refinement:** The Friberg model provides the mechanistic understanding of the delay between dosing and nadir, allowing for rational schedule design [cite: 9, 16].
3.  **Biomarker Integration:** Tumor burden acts as a critical variable. In radioligand therapy, the "sink effect" dictates that high tumor burden may actually protect the marrow, necessitating counter-intuitive dose adjustments [cite: 23, 29].
4.  **Future Paradigm:** The field is moving toward Model-Informed Precision Dosing (MIPD) and Adaptive Therapy. These strategies utilize patient-specific feedback (biomarkers, toxicity history) to dynamically tune doses, ensuring that the "cost" of toxicity does not outweigh the "benefit" of tumor control, ultimately aiming to convert cancer into a manageable chronic condition rather than pursuing eradication at the cost of the host [cite: 5, 38].

## References
[cite: 8] PMC3312607
[cite: 3] JCO.21.00471
[cite: 1] PMC7174767
[cite: 4] PMC12339818
[cite: 43] Altai Oncology Dose Modifications
[cite: 45] NCCN Dose Rounding
[cite: 44] Case Comprehensive Cancer Center Guidelines
[cite: 42] AccessMedicine Guidelines
[cite: 14] Cancer Care Ontario Appendix 6
[cite: 13] PubMed 9256143
[cite: 2] NCBI Bookshelf NBK12920
[cite: 34] Oxford Haematology Guidelines
[cite: 5] PMC11946950
[cite: 6] D-NB 1368154026
[cite: 46] TCR 17108
[cite: 9] ResearchGate 10986102
[cite: 21] PMC8129710
[cite: 47] Anticancer Research 40/12/6585
[cite: 22] D-NB 1245226363
[cite: 37] bioRxiv 2025.04.24.650205v1
[cite: 7] Tandfonline 10.1080/14737140.2021.1941891
[cite: 32] PMC7882695
[cite: 48] MDPI Cancers 17/22/3720
[cite: 35] PubMed 19084287
[cite: 20] DIVA Portal 210418
[cite: 39] PMC10205748
[cite: 40] ResearchGate 386264664
[cite: 7] Tandfonline 10.1080/14737140.2021.1941891
[cite: 33] PMC10395252
[cite: 10] ResearchGate 361458041
[cite: 49] JITC 10/12/e005678
[cite: 31] SpringerMedizin 19329024
[cite: 28] JNM 66/supplement_1/251681
[cite: 50] PMC9364902
[cite: 51] PMC10119067
[cite: 52] ResearchGate 336913827
[cite: 53] ResearchGate 342602043
[cite: 12] PMC9281983
[cite: 15] Healthline Platelet Count
[cite: 11] PMC9152964
[cite: 14] Cancer Care Ontario Appendix 6
[cite: 9] ResearchGate 10986102
[cite: 16] Monolix Friberg Model
[cite: 17] PubMed 12488418
[cite: 54] JCO.2002.02.140
[cite: 18] MDPI Pharmaceutics 14/5/914
[cite: 5] PMC11946950
[cite: 55] ResearchGate 388929809
[cite: 36] PMC8846635
[cite: 56] MDPI Pharmaceutics 14/12/2731
[cite: 57] MDPI Book 7075
[cite: 41] PMC7721100
[cite: 38] PMC3728826
[cite: 23] PMC10177482
[cite: 25] ResearchGate 351960705
[cite: 58] PLOS ONE 0260073
[cite: 29] UP Repository 12c8c9bb
[cite: 27] JNM 60/4/517
[cite: 16] Monolix Friberg Model
[cite: 19] PMC5445232
[cite: 24] D-NB 1272135861
[cite: 59] THNO v14p3404
[cite: 60] SemanticScholar 21d3
[cite: 61] PMC11430653
[cite: 25] ResearchGate 351960705
[cite: 29] UP Repository 12c8c9bb
[cite: 30] MDPI Biomedicines 12/10/2355
[cite: 26] ResearchGate 393710693
[cite: 23] PMC10177482
[cite: 62] JNM 65/11/1685

**Sources:**
1. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWa8DIBrGZAnW5GAA1Pnl8W6bNoh73bbHpSUiGX-l8n1JH3fgM9JBi_PtPGyyZtV4rcTzc0z3K127Hn3smtBSLRlga29GoVBzwPOhpJzxgr29jDm2XaJy1CJBb7SSChQ-lw3Q0hHQx)
2. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsvQDpe-s6QL0zDC9A725RrumBD2YU0hodoq8MntArKQtyS4HTT5tYE1P1WI-ZhoNVqy-rDynTTik9UejbcAuLujjx7F60PijqOcmS4pmMrYDXjM_67CM_dF2rLtyVY6-zOg==)
3. [ascopubs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0rpqnlk1rPc1Sm_Uh_WHRORij5c6JdB7-5-_pFSiSn94b0QfyfCTZDVPBGQZgWm18EJ3xNbA7kmbNFt130UyJv4Fo2LLoxoNKO3_kdTRyHQP7GePCiaVT--rpm2uc6vST4OM=)
4. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQzNusutnMCqLIQpVjdqwk_OS5DVHzjaQ34QrdbE3uJ7ifKbsGC2AW8Z9huSRCPzCI0FdHszee6bi4yMHJ0rhNxgCWwjBM0b6gLCmBlitEhmASJ73BIlLtRMjUBLR_6zkzGeInkg4FBg==)
5. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5xU--RU_2_P7Hx_W3J_Q6BCAzo7KqFkygKB86dwlNxS-ix70jrECRITEHqgm8KUtQk-hs493qONDDgQNDTQrGUPW3O2OkOO437lIqp6TNKsn6bO0Vl-3CCYVcKCj4TiDWGnKW3oDCXQ==)
6. [d-nb.info](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8HZy0V01CN3fHXWNbU9MfRFEjAlbDmTW9L-0fM89rKMQmXPrmlB6QTVpGfG4vfqmOfDjRsSqyxsypSSy_nHOtQpiEi8nyfsq1bWvVIU1Vkpz24N77)
7. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEv9w48aLXTjP56_vpe9D1cBdWDgc4c-bLsSXakqjDpmr84V__tFv2YAmn3dpehp4V5WrtjNtsfAnpR81UnAGvmpkxTlD45cqpbEXDrqYw0wQMD6BLhwMxV2v1R98nkwXKtjrrjNYRaFjaF5pOkabgjT377LLG2e3k=)
8. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXupczIeT8tC3Bqj3E7FV60Q-Ou286li466m7N_51KOW7E8tvKr0TOspIpF3ev_bNV2ybXBw-foOTPkrJyQm59fPS7EuKMhA5MAgcv47SG1Ml5cxfJJ4XifCUUunnRs7_qn5uMh6Oy)
9. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9YQiBW1OThGVlSj2-RaoNMnntPmWFM-QphKhpjxU-dCntJBJ-ouYSYP9eGpASJmSCnNDNTS5X7O52hxcRg-b4yBzcg-Fz-835kOWLyvyQBC7P-LGCkoe0gXfWYynH8nHFksvlBWi0a6oPsWQgj7tJfhF7fv06HPmVv8X1ZXyyDv3bkhNWZEf0RE82SZ3lBR8iMFADuCZZ1XVM8PADgqq-rTDZb-QvrK_dTRS7hLGPesWM38YJLspS0RlG0EOc7g==)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIl-J5nMjWstsK-QXrxQFUejA7NmpLe6oAEBX2snuMdlvtN3IOdoXBCKNeCC0Ix3Dqus-92xnp_Fwf6e-nE_hmrNgYHctD1onlnnNYsDph6Goqth0VjSHbfigTICb5sPzxn2avWhq02axi-dFGzC8I6KplU4oZt-za_2o1Wgxhu4rMBdngYhJdTt85sIIUwKUV1WtO4Wz_BtZuRLs9F9ZdqDScK2fhq3lUqWpHTrMItdvSfM50YOSpaVdk0fWj6pahjWrh)
11. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdfpm6V2AptWMkB0l8E2W_zmVZoVyQeMKvEmqIFHejOH_cUb2-mr7UTV2c3l9OqaQE_AlM10TpT2zoMyBdEKkYK2dkNa4FQ1i8rZ8ePVrEBnyWPegBrZUfhKwdvYmOmaoXer-LjYb2)
12. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGf69MQVYLEGSiPV6VV9CB_b-jX4p0Xg_JVEaXODNViR5ODvlUZe3RjBRRkn3XknoHuuWIKcO5kqEovelJ9cPoVL49rKP483Omr6CyrEoSJLexXifSaY30JyIA_khZncoPEnC2jkJM0)
13. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4vzehNqeLrFB2J84wZmboLXAmvqKnHaqcyW2uCuT0kGQ5NWdsnZe5n9v4dr7EUKe6pD1V5JgeOD9jEKqbQgfJpO0WdqLGm00YY8EfEAroq4MRdyKZ2iIoLOA81_H7)
14. [cancercareontario.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8qXK1O0aBy3RKnX3gOqSQICWED3LyTCzylBtw7IDYkFjqrfu5ZTQrO-JhIBPsYC7DZjFtlnd0cIInDR-aMyeGul7H7RsW7HDg030d2Cd_HdMqVdjqeuTFU3jHJr8z-JHEGeBbF661YjF-HsqRyr_8KjhTI-zEspSckGfzWNagUiA6hjzHpj9SNjALNe-l49RLwiKKHrE4bg==)
15. [healthline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZEjguttA4j52wiULJrv_SMyGug51wZ_VJD49bltmq24wt7kGy8ROMXRYT0z9GQo4AXFFq1lzEEOKqXiy7gmnlq0I1sT4omMSMRn8xIdBMNrZ6m_DJ6AHkCaZNPa6jBuGujgtSsswyIubkYr_R57U_UrOeE8jxagxgbmZia1J8kNHwHeTX9Q==)
16. [slp-software.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4W1tnbSgICpLCOcz7uq45NK4EwBj5D_NsyHli4ekbNjR6HxXjwaYcEgoFzuWeB_clUVVFr9uiWCKOMHhPMrBFt3e8lt92TStm19fKKU9yLZByeNJKXBQEPc1-0Jcm6P6DPNaTIFn1loMqkxIA0HCYAHwBFsEfVmFQ0aSsXr1MAxZVob7SwnkH_ZyYdA==)
17. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_IZ_xbFYH1u9c8ZWDuTta3JsyseOxAwE8kelqg_HziaxKh-GAT2VT9SdYbR2NniYSj5mQcCNZM-jBUcocIJzsUfEoyRnI7zcE3yCqUE_G66rqaL-cGVBsRjxoyyyDew==)
18. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGsrhJbPBZzObi5xuQb66LuOGy8UCJSJ3vOwwZgIuaZoQ0u019f2Dzaw_0aOpTuT3QAECGqY3Iw_5d3ecRbvD5C71bR_jgDm0EqiPGvFd08dtE_jQqLFbh-dmZ-E4=)
19. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkMyv68NUrwZeC7UBNl4wujVbNTcZDUnkecwQoNcrohh3CDAhdCMDl8VVVyX3YQhIbTTaV9TjIIeecjYU-NoyTHZbqYR7Hhcvts_DyxZ0szD-GGdD-o59VU8kIibm93yZhQAqIsMWE)
20. [diva-portal.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9hv9SewvqmTTfC5Aag89yBFvlABxEqxWkhYGD3HZtvr_a8TrOb00GPcRNd-PJ-a33J6_v7WKb6H05So2SomyYr79wyk6-8A9dz9lhon_zQEMoJA9D11UBio0jQpbDOUhXPJnPFiaWY9WvCLtwCtlX8yrrdokUUA==)
21. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4jUZ45dygFsstQ_tzBw6Oc9ouwao1aQiXtZsR5YYSvGfX8Ej5XcV8-Qno8OXmYHsp8iBTHqDnHSAhEUDDc95NknIrfo9j_cMkSpwmWOwIWk1jzf_4pUMBu2WNClNHnyLCK0Wwn-kP)
22. [d-nb.info](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvlQfX_8GBDRZGzBMncqVeYrlGZ07dtuPQeEQpjiUdTQoSeBO9pKn2V-rkSMPVY-gvfhCY0YXrZBrcM_tFwKJEURIrOrnt6_ocwC_UiDlkIWTpuE6-)
23. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1ptghs36j-F3IFBVISZzT3cOcnKvADk3B9m-3chTfRpJsrxfLMEyIuqaYDy_6nOAIH1WCOTTCfXFKTBcq5q1ehgqE1jT6wlTINZ1_QxyferXcZ3xhpndfKFXqPc2w8MubU7KJPnV23Q==)
24. [d-nb.info](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ26tMA1YVtZyAaEFdxfrbnpXKAXgCcpfMX09xLoAwKBRqFbWRYStasESrd50oy5j_2SFaYT-G0Em5Ls05iqdeZLiX_XCS8O8DnTV9E8ieyh_mLT4n)
25. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEps-KZ4G6riaE2l8sgQVITXuIIGgFvxoEcboedRpJXzcrtOO3iyHon6CNiKuoaOzKQFh_umkAqio2lzUxFcLgC1PBLaews_Du49RzooSS3h8UCI7zozXve16HvMlAx3IlLoDef4mmWgFHAGx1O38J6a_SASGrkvJ8E7LttBf7tLms-LXTkj29N4Od57OUePp8fvUiEqbIp92-okdq-hvI=)
26. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkuVcbM5N95U27PDanbKHsU-ffWs-TltNvNSa3KSDFlncI2MhtRUoF9bQrhqRVB7se7gauQ8WpXQImOi4ZCaE_YM0V0j-56xzs-Q9Vwc3g72_tyLTxfrKGfhrj_vvNhbSmf3LbY-VE7IMpJeWXYVsAPCw3txmGD_IO8XP7XgDKwwat6XQqdkifn3OKkkLZX_5gIWZaarswas9f5arEpcZNrwAkKJs2puvf2_doJkcYVB-PWCf17dazfVYqv3zb4xzKS1PN4VE86JC7YBxiO5Ljd84wArguar6ezncGqi_DWjLUbBrD5qqTo3y-LixjHwZ7yUoHMvlV9-lFryx3jov35qhr2xTcRNR4dw==)
27. [snmjournals.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJQBkT7tnpXXZK07kQyCTYdBbqgCN2zl2vYRQAN30Dpf7YoR8xaZZboSRC5tR7TqLmlTkmZktFodcfO5rmX6H3lWaDCxbxRbu_ZTe8Ju-iLjfYeHiLonc_8Dc36dmsrla6YA==)
28. [snmjournals.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEgslbPsgkrId8VNhBxcgZCdFFyZelrJShlky0sQdUiShExPJdpb4hDhws9-d6BaRCSVt8bEbs0kU_cLhqqGn6sBCOR6sQpnJzDCdK_toTZkcb0WwvWZ-IjaodZmzukdBrJpHElY5HQEadBV3FqI51)
29. [up.ac.za](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHa5Z2yPjDSc-9RXhxJMJAUcMt4q4fRoikKxTQHbumtep6aREV7Z7MljfbKznXNBdp-9DRBSZ32rJMuOz2ME7uYtfTDiqBzlS63MTj0f1kAjt8Z0Zyc16_WM6WeBb6UKzQYKM802yzDHTdRdi_9x6uK8_7bR7Vo4Q0l6shDSIWqKZ6j6Lb46RsvrrymsZfTzlO4i6Noi08Cs4=)
30. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbz8glrkGtw1ezFeRwsT6OIzFTY5HkhuXypobqdw0lSrku4rbCXau4PkSQkzhturuIYYBtugRCWEJLQNnCGKaq-UgHF-94BANSJ5CLEwTuPd2lm--CUVhPTJWQID8__Q==)
31. [springermedizin.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGAK35qf-LuhBNAUdmKN2VazPB3yFDsTW2F3ur1LW558s8Kg3Z13u0P8Rbchxjmth-zaotEVYxi3StGfTqwq2rdyQtxoftUHvS4MEjiY0_gUw9KiHgGIWt-S94xUZaueG4qVu74QXDJuO9x7cn2K4RLYIIQOUbvwCHey1jifTbnM8KIwTpJ90aOVMbRXvq_lGTIF5SyAQSK_Fz0zoTew==)
32. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7xwpvhS0ZJ-RNWvTY8bRNkympbgsPlVjLMbM7UtWOXQoLsSujOr_vms_HI0Hm4tYOmb-CL6BTGy_Ynhbw9erPKTIuYOvrHNPF-GngdevE5YsWY_3Y_GtrEnKg51BPC0th41l4eMHL)
33. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsA-Oo2Ga1BI3nkwBNFVDcEkSS5-mrt4CQa5yb4CtCD5N-HNBRVi3bAx9FnSvTxDykDN5WE_IxEvqgwFRW5tvXLHxH2TcB0NEEqBfH1df8dq-k46DXBKihNetvU4b0RnHetcYRIQJ6VQ==)
34. [oxford-haematology.org.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQrZA4fVv6cDfGDlDB1OHJijke_MkvrdI9flq84iUDQd9FGlE5VHYTP1DWJAH-i-wzMyv85ibTGHJAoI_nxdGIiKGovHQzjHNSEjT3PZ-OkkdJbSJCA0R_-uBR4daW7SnPYe5Zz3NxbUxtUccEfY1NgNQoBTHVxwyR3bs3d1JfuRs-bHDhXj76Oov1IWHpLaAYtJ6oSe3spToYEi3-Cjo-xCZ59vE=)
35. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHZ3hx-Il5aYgzL_gvPnprentjHgEi6VagoNpNKt34f7wpt4iBQdW3bKDJmtQBOmPvZo6v_pCM2R5ui6ypSDGPgcCLcXqgJLTN1QNvgtz3WN08Dp5douzwU2KrfcvLAQ==)
36. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1L19HWzUWTBHUHmaurpXziETKNVuLeTpxi4fNiD52zFBCJif3c6WYLYy_umt5Iu1FcL14WwRBNd3ZC4kE6VcKRbrn8N8jvuYsiAxH2_flLQW3D1EoFIfQ1jdfbLup87QylvOly3xK)
37. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgStil9BiL1DPyme__W9Eb6IOyuOr_9WFx6CLyDN7kasmU-UWKvyM8knGMK0VuLAzMyswiXSM9q40TgUw24POX_U221E8XIFTcojjzXndbTf6cIPcYBZvZ0UT7cg3gCbtKd0DMz_WfbQ8LMUFPx8MgM3JihGLR5LcuKw==)
38. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs0WmGsleth38vSK3wzuMrO8LGxHL2X_kUT0DnsYQ-pP4wux1bvLEGubBTrB8RbV_ib40lhtc9IhchRlCrpvuexsnjEsizYT47GjzEN9NSKiWjJg2mEG1PbKYmT0vM2g9ivi-pLrnE)
39. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEVvyOqP01Ajrg_mit6CfN2Cyz-FB04LZSBmuFpNgf6rOYdVGcNr4HNlQJx8HwXiNsLyzUG-yZYAyhrm4x60FXGX2CAq4y3A1c1ALmmp095IN-hwxD004lYrwNFsBdZ-8ut_rI_xDxSg==)
40. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHsCFUc78ePHdORtLshRrGnMB6iO4afKtvRj4ZO5wdBunNwnbhmzDPsUMyWF_j5QnbUh9OHADBG2KshgKbMTVXSHjfL9yBX8ZRL8wD195J0z4SKcFI8__8ykT357kCxlqGSLlgNjkV_zOyt5YiK4fqVkCg5cjfiL5lr0D0Ay4wys_RBoW6frut__pKWu3Q6499NdPodQDFpt6cEbkTwe6_lJQvnzFIsUfrzZZPQUv_yelxHduQ8mjPN2qchF9yKRdbu2i4kX9m3v5pqMvlqAqPNgvZ4pZTWV_tVQ==)
41. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE95e3zKsITNT1ApsDpPYxzW_3M2XMznjbLf1DKXSWdxVXJf7npzk1MCp-WrbcbTPvuIgfyTM6NkerGovHzTTk8P_JezVwjO7uL2kGvsBQampUtzyDaKgsuyd0_MgDJZt0sklwGV64i)
42. [mhmedical.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0d6SXwBum3ADhAsX-eBUNrwclUkqe8fhleiCy1gv9h__QNyuWA5JXngpKy4lFfdj_umn9jZDIWaw-JuKLwqK7mmLZAMqTywlpcmDDMxBoUSX7rAVykipDMsUUz3plgBtAV3ICaPZZAmIKuufEEPt4UNk9N7rmNUjt2f0V3tckPkoqL2OPtcI=)
43. [altaioncology.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5JeG78gjbNgowyHW0gL5S4csQmZOUt6Uv7UXIPPs8J9apYLxQSVTgcN9tqezPSCzoezezF3VtsRUK1S81dkoPG21bAZL78gjkdkl78F-ugO4CaSlwNtoQrnygcZqOPdeu2qoh67th__U_cdIgY3RgxXhM1Th1-In9WV9R1cFcYn3UYaQihbsUJ2bqmIjQC3P7GcdBAmSnP1oC)
44. [case.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvICwrbDcHvqXTgw1kOKmvBeG-PRMNPwRvbDZJDrPapHEf432KLAziZi_gRn7DPWyIBRUYxjBoV90yg2yIV4kKcOp7STZ3dRFqJgU3ortxHslv-sdEn9EtctriZvGvk3b4tXK3awv34veAj1f9WDOafgpdZb-hL0KQrkx5ltRpfUI=)
45. [nccn.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsS8SHM4L3mz8WBE4xZJOrBnAPOrZy8UljLtMB9hxCwUPX4i_WysgzCamGLTZokHh84q3Efv2fyFxmGAmLxyC69piduAPHWTKFt8_ZYeEA8lY6UAQRZKQxb4hH7YDKleWLgtj2zI7wrPI77wwzDO6fgfo4bdngDNTScWKNVW8uJifxhcp5hkPtDVefdTsClIyF1g==)
46. [amegroups.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEM_PHe5WV5GXYZU8x6Ybhmj_bZNV5VEY67QZOixKAQfus8_gjDsGu-Cu91f1TcPY_tsEWnY5j5AcpyIKVZCPtuOQA8uEdmhjYByDbuGJNqhVGbQ1RK7RgkR3CFQertmghOb2evm5D3)
47. [iiarjournals.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMWaiyDVZFOLK0ShTlM4kXCnkI7fLpJrtMb1J0-mZqJN_lciwAWBsEKkrR_ZZHJAgRh9TDg2N62myeSGy_V-AyiMh0H7tYt4GOCn_kyfDAglbvgd1KKm-Nl41IC9NLiHfZzuRb)
48. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcoTW1nFlJBKt9hvyVXxIwOT-mkpgryBUwl9jKURQuDzbuhQb1li9U4lmDF9VPZffg-Mftii3qYDq4U2Bcv0Ad5hBJ6MagrT-VqWKeRz-dtntoo0mOzY1YowQ_US5QuQ==)
49. [bmj.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9DMQ-03EWNU5b94rWOZgEthLE2ZTpLnkzlg21GB_AJXLhGpFLOWFEVaxFXlgrS66lA4kbPY0w-yfLY_k6MElKLqqyKdNdekptKuk-ytsmXYRNwSTXley6kya72AhzXds=)
50. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP10pU6thA6F6hJ14N9Xd58KpT-haBzgckcHq-cJqqTxAOBkvorsr7pUsClQYoFjaybJ9y-0ArmsFurZKieosnFrgM0M12xe5F2Usvx3xlW_Hj2C0oNSxOinip6kgkkW8nbVp7fKub)
51. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGk3goOhhgJ7NY8E8yLnsof0GGnQkv4WoJErWfuOOuMOV0GKD98u0BvtdoQxwXXIY3pEpeMuaQMNpYgt8_oEz5uJ60_XkMLKdEEnWyNEAI8vPbFZLRiw7QosuE2DRANrpHx_xUnyg6w5w==)
52. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGvefHhJnamgkkfUDYdOW_raYEbR9bVAMai349H8iKzZtf2Lu0e51gVTrhl0EWZOd8SeouGOBowxbwN8bnjjfsps04ULnW4Laj4EJVSrJC8Gcy4cAdBC-ucTRPK3ZhaO5_pmhygn9h2U_fDTfw4NRfezxDIyC8QKoylfwJqT49AKWtOf56lt6nQnEMYgHlEUrPH967ZZx3AFkQj1_xu3H7xlPH2AaEyt8n3tO2ePgSea-kIPw9sIqFaFNzZtUmtnrnXlbevgW3UcxOuTXEcEo=)
53. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKLitcrewzOsO3-a19i1XMXMscRatScyoXav4idoVfLhUUubJbpUVfZ7IY6yK49i50KI76l6T7hOiP271EuXFRESj3zNGlm7eCaKE6bq3xAn4P6tdG0gpXQjPN6e7yoc4WXmnjLiABgZ0Nuln-Mjvw2wXvO1Oi7PNra85jD4mDdhzZvHX5IvCnTbMF_dhTsWTiamavo5d2uCPqMXzYkHcpi5ufR4nfZ1WYJ7mXVZm3o5UGmVhUoCrnM1haEReKA-OJOYiCugsChJLlZ1y63LXDYWcXXkOoX760XO14wbHRwPufJackiPQKpHGOBZoQpsWMUSg=)
54. [ascopubs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEm42H-kmOYGIOtTrAKZ-boG79Qe29gHbPSvDGtriR1lVOq438wSQ-rI7EiNhJrNCplgw4qx43tJgbkjUbvo9UT7aY2OP9T6ogPmGNUODQNSv-BHkWZ2k0X5jYOOPaz_w6LYPixFIdpet1B)
55. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkj7OYbCT8x4rdwDS-RxSDH57qdWhv4iKy1sF16neK1aad46DFFRLbO-T30apvQRBXL6LdrymABJrCuGv9ZX0hsn8WaEVNidsx65M_W2AyaJ6ZV-2TQ1EZ3MYe8DPTR3qpg92D1aOiEr_UbF3XfDGdRx8TAEKhecj__mG4uoyITz-rDU6u-_owA5JwEu3HiV70LsdJgnmvqGPU1cyy42Is72CFfIUmYOPOgEZ6LqhclQZVEa5gWPNLsk30jHkw)
56. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPiT6eXWCICfkYpFV53IL4xDKXJgFLcrElgDekMoak62R4qUCVkWrB1qnX8FdnHY2RZ9wAncfLokhKIvqgzH9kYiuHmNC6VtUjmKs85fWmRC6zPxUIZhxKIuhEIxN4VA==)
57. [mdpi-res.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfmCu8NVwSsFmo4f-zZpljX_oTA6a_MNz7EDwwTWyJ22PFGBPNvkRbIa5KaM6G5WsSuiXnTjtB7WBfkpJAMBX1h73tc5-X4j7J3LObuFNiBrlr2rKPRPgC-Neign6aS8eosj3YDR8uFYqJtzHVVhWIUKLI6Mw2vN4beaBzkSZWeFy9XZjYlG_qM4Ib05aU)
58. [plos.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9I7cuyqpb814DyZQ3C3ueH8X8iabDgaQFX61I5CIOdPgABsjWyIH1UjfA5deUu2ye6KdRAGUX0C9nBA3q3Q1oQzZb3Tg2QTgHEaqcEaHd4ieeBsbEPpnfR_ezZ_qyvIoYlqJxFN14y5KMKeVyDi5-Qbf5npLSXu4w0AMxbmSVk10FmSySf_EfKCBtyHYA-VGJgEo=)
59. [thno.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHCmDQt2FHpRCXPxO0DFzgNB1xLfCWXQvjbg7sETWlA2YeZMA22HUqoNlanZAoAsiG141vSojAw9OVJTM7t4yNyn4q4SwJQOfCgIfTNxiVatN8Bq8I9F5I=)
60. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9QXX8IkOW_MSeVNzLFSMiszsn_6tB1eXzTr-JsxBU4C3rmdV63QeA2F40KsBKwRhDPzUdwr0JDVMSH99iKGuaeQESAzGnraODubFjv-mMfMboeqqkxWxDCehkGlP_WySoRysc0A9uatW2QL7DpHPBWDg_huUsdWHR5NLdNWcavipoqmM=)
61. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjk0ElEzTVlyV0uiz9sprFKupnLJnHuGvlxraRHrK1U0yXsnkFX8sA4NLTA1g9gpEl2CeqyRgoJrtZeZoVyYh3NxvFHQVFSr6IjHH4bBnDylW0ALa5-xL2p-n5UX7FBNfjnp5jDCr4gQ==)
62. [snmjournals.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGo3rEsx5h5ONgbjzXmJHUwA2nApBQ0qZ_-7soyIhEiAMymlHMOpwEZxpTXjnPclvd-Vn7hO7wB993nXOnOoc8v5yqJXtjw8qDr1wtOpMUtjac4-vX2NgCuOePJVIQCGRARBSC)


## Annotations
Annotation(end_index=2463, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWa8DIBrGZAnW5GAA1Pnl8W6bNoh73bbHpSUiGX-l8n1JH3fgM9JBi_PtPGyyZtV4rcTzc0z3K127Hn3smtBSLRlga29GoVBzwPOhpJzxgr29jDm2XaJy1CJBb7SSChQ-lw3Q0hHQx', start_index=2451)
Annotation(end_index=2463, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsvQDpe-s6QL0zDC9A725RrumBD2YU0hodoq8MntArKQtyS4HTT5tYE1P1WI-ZhoNVqy-rDynTTik9UejbcAuLujjx7F60PijqOcmS4pmMrYDXjM_67CM_dF2rLtyVY6-zOg==', start_index=2451)
Annotation(end_index=2655, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0rpqnlk1rPc1Sm_Uh_WHRORij5c6JdB7-5-_pFSiSn94b0QfyfCTZDVPBGQZgWm18EJ3xNbA7kmbNFt130UyJv4Fo2LLoxoNKO3_kdTRyHQP7GePCiaVT--rpm2uc6vST4OM=', start_index=2643)
Annotation(end_index=2655, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQzNusutnMCqLIQpVjdqwk_OS5DVHzjaQ34QrdbE3uJ7ifKbsGC2AW8Z9huSRCPzCI0FdHszee6bi4yMHJ0rhNxgCWwjBM0b6gLCmBlitEhmASJ73BIlLtRMjUBLR_6zkzGeInkg4FBg==', start_index=2643)
Annotation(end_index=2926, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8HZy0V01CN3fHXWNbU9MfRFEjAlbDmTW9L-0fM89rKMQmXPrmlB6QTVpGfG4vfqmOfDjRsSqyxsypSSy_nHOtQpiEi8nyfsq1bWvVIU1Vkpz24N77', start_index=2914)
Annotation(end_index=2926, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5xU--RU_2_P7Hx_W3J_Q6BCAzo7KqFkygKB86dwlNxS-ix70jrECRITEHqgm8KUtQk-hs493qONDDgQNDTQrGUPW3O2OkOO437lIqp6TNKsn6bO0Vl-3CCYVcKCj4TiDWGnKW3oDCXQ==', start_index=2914)
Annotation(end_index=3916, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEv9w48aLXTjP56_vpe9D1cBdWDgc4c-bLsSXakqjDpmr84V__tFv2YAmn3dpehp4V5WrtjNtsfAnpR81UnAGvmpkxTlD45cqpbEXDrqYw0wQMD6BLhwMxV2v1R98nkwXKtjrrjNYRaFjaF5pOkabgjT377LLG2e3k=', start_index=3904)
Annotation(end_index=3916, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWa8DIBrGZAnW5GAA1Pnl8W6bNoh73bbHpSUiGX-l8n1JH3fgM9JBi_PtPGyyZtV4rcTzc0z3K127Hn3smtBSLRlga29GoVBzwPOhpJzxgr29jDm2XaJy1CJBb7SSChQ-lw3Q0hHQx', start_index=3904)
Annotation(end_index=4363, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9YQiBW1OThGVlSj2-RaoNMnntPmWFM-QphKhpjxU-dCntJBJ-ouYSYP9eGpASJmSCnNDNTS5X7O52hxcRg-b4yBzcg-Fz-835kOWLyvyQBC7P-LGCkoe0gXfWYynH8nHFksvlBWi0a6oPsWQgj7tJfhF7fv06HPmVv8X1ZXyyDv3bkhNWZEf0RE82SZ3lBR8iMFADuCZZ1XVM8PADgqq-rTDZb-QvrK_dTRS7hLGPesWM38YJLspS0RlG0EOc7g==', start_index=4351)
Annotation(end_index=4363, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXupczIeT8tC3Bqj3E7FV60Q-Ou286li466m7N_51KOW7E8tvKr0TOspIpF3ev_bNV2ybXBw-foOTPkrJyQm59fPS7EuKMhA5MAgcv47SG1Ml5cxfJJ4XifCUUunnRs7_qn5uMh6Oy', start_index=4351)
Annotation(end_index=4667, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIl-J5nMjWstsK-QXrxQFUejA7NmpLe6oAEBX2snuMdlvtN3IOdoXBCKNeCC0Ix3Dqus-92xnp_Fwf6e-nE_hmrNgYHctD1onlnnNYsDph6Goqth0VjSHbfigTICb5sPzxn2avWhq02axi-dFGzC8I6KplU4oZt-za_2o1Wgxhu4rMBdngYhJdTt85sIIUwKUV1WtO4Wz_BtZuRLs9F9ZdqDScK2fhq3lUqWpHTrMItdvSfM50YOSpaVdk0fWj6pahjWrh', start_index=4653)
Annotation(end_index=4667, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdfpm6V2AptWMkB0l8E2W_zmVZoVyQeMKvEmqIFHejOH_cUb2-mr7UTV2c3l9OqaQE_AlM10TpT2zoMyBdEKkYK2dkNa4FQ1i8rZ8ePVrEBnyWPegBrZUfhKwdvYmOmaoXer-LjYb2', start_index=4653)
Annotation(end_index=4915, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGf69MQVYLEGSiPV6VV9CB_b-jX4p0Xg_JVEaXODNViR5ODvlUZe3RjBRRkn3XknoHuuWIKcO5kqEovelJ9cPoVL49rKP483Omr6CyrEoSJLexXifSaY30JyIA_khZncoPEnC2jkJM0', start_index=4901)
Annotation(end_index=4915, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdfpm6V2AptWMkB0l8E2W_zmVZoVyQeMKvEmqIFHejOH_cUb2-mr7UTV2c3l9OqaQE_AlM10TpT2zoMyBdEKkYK2dkNa4FQ1i8rZ8ePVrEBnyWPegBrZUfhKwdvYmOmaoXer-LjYb2', start_index=4901)
Annotation(end_index=5289, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4vzehNqeLrFB2J84wZmboLXAmvqKnHaqcyW2uCuT0kGQ5NWdsnZe5n9v4dr7EUKe6pD1V5JgeOD9jEKqbQgfJpO0WdqLGm00YY8EfEAroq4MRdyKZ2iIoLOA81_H7', start_index=5276)
Annotation(end_index=5289, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXupczIeT8tC3Bqj3E7FV60Q-Ou286li466m7N_51KOW7E8tvKr0TOspIpF3ev_bNV2ybXBw-foOTPkrJyQm59fPS7EuKMhA5MAgcv47SG1Ml5cxfJJ4XifCUUunnRs7_qn5uMh6Oy', start_index=5276)
Annotation(end_index=5897, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8qXK1O0aBy3RKnX3gOqSQICWED3LyTCzylBtw7IDYkFjqrfu5ZTQrO-JhIBPsYC7DZjFtlnd0cIInDR-aMyeGul7H7RsW7HDg030d2Cd_HdMqVdjqeuTFU3jHJr8z-JHEGeBbF661YjF-HsqRyr_8KjhTI-zEspSckGfzWNagUiA6hjzHpj9SNjALNe-l49RLwiKKHrE4bg==', start_index=5887)
Annotation(end_index=6149, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZEjguttA4j52wiULJrv_SMyGug51wZ_VJD49bltmq24wt7kGy8ROMXRYT0z9GQo4AXFFq1lzEEOKqXiy7gmnlq0I1sT4omMSMRn8xIdBMNrZ6m_DJ6AHkCaZNPa6jBuGujgtSsswyIubkYr_R57U_UrOeE8jxagxgbmZia1J8kNHwHeTX9Q==', start_index=6131)
Annotation(end_index=6149, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGf69MQVYLEGSiPV6VV9CB_b-jX4p0Xg_JVEaXODNViR5ODvlUZe3RjBRRkn3XknoHuuWIKcO5kqEovelJ9cPoVL49rKP483Omr6CyrEoSJLexXifSaY30JyIA_khZncoPEnC2jkJM0', start_index=6131)
Annotation(end_index=6149, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdfpm6V2AptWMkB0l8E2W_zmVZoVyQeMKvEmqIFHejOH_cUb2-mr7UTV2c3l9OqaQE_AlM10TpT2zoMyBdEKkYK2dkNa4FQ1i8rZ8ePVrEBnyWPegBrZUfhKwdvYmOmaoXer-LjYb2', start_index=6131)
Annotation(end_index=6531, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9YQiBW1OThGVlSj2-RaoNMnntPmWFM-QphKhpjxU-dCntJBJ-ouYSYP9eGpASJmSCnNDNTS5X7O52hxcRg-b4yBzcg-Fz-835kOWLyvyQBC7P-LGCkoe0gXfWYynH8nHFksvlBWi0a6oPsWQgj7tJfhF7fv06HPmVv8X1ZXyyDv3bkhNWZEf0RE82SZ3lBR8iMFADuCZZ1XVM8PADgqq-rTDZb-QvrK_dTRS7hLGPesWM38YJLspS0RlG0EOc7g==', start_index=6514)
Annotation(end_index=6531, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4W1tnbSgICpLCOcz7uq45NK4EwBj5D_NsyHli4ekbNjR6HxXjwaYcEgoFzuWeB_clUVVFr9uiWCKOMHhPMrBFt3e8lt92TStm19fKKU9yLZByeNJKXBQEPc1-0Jcm6P6DPNaTIFn1loMqkxIA0HCYAHwBFsEfVmFQ0aSsXr1MAxZVob7SwnkH_ZyYdA==', start_index=6514)
Annotation(end_index=6531, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_IZ_xbFYH1u9c8ZWDuTta3JsyseOxAwE8kelqg_HziaxKh-GAT2VT9SdYbR2NniYSj5mQcCNZM-jBUcocIJzsUfEoyRnI7zcE3yCqUE_G66rqaL-cGVBsRjxoyyyDew==', start_index=6514)
Annotation(end_index=6771, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9YQiBW1OThGVlSj2-RaoNMnntPmWFM-QphKhpjxU-dCntJBJ-ouYSYP9eGpASJmSCnNDNTS5X7O52hxcRg-b4yBzcg-Fz-835kOWLyvyQBC7P-LGCkoe0gXfWYynH8nHFksvlBWi0a6oPsWQgj7tJfhF7fv06HPmVv8X1ZXyyDv3bkhNWZEf0RE82SZ3lBR8iMFADuCZZ1XVM8PADgqq-rTDZb-QvrK_dTRS7hLGPesWM38YJLspS0RlG0EOc7g==', start_index=6758)
Annotation(end_index=6771, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4W1tnbSgICpLCOcz7uq45NK4EwBj5D_NsyHli4ekbNjR6HxXjwaYcEgoFzuWeB_clUVVFr9uiWCKOMHhPMrBFt3e8lt92TStm19fKKU9yLZByeNJKXBQEPc1-0Jcm6P6DPNaTIFn1loMqkxIA0HCYAHwBFsEfVmFQ0aSsXr1MAxZVob7SwnkH_ZyYdA==', start_index=6758)
Annotation(end_index=7673, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGsrhJbPBZzObi5xuQb66LuOGy8UCJSJ3vOwwZgIuaZoQ0u019f2Dzaw_0aOpTuT3QAECGqY3Iw_5d3ecRbvD5C71bR_jgDm0EqiPGvFd08dtE_jQqLFbh-dmZ-E4=', start_index=7659)
Annotation(end_index=7673, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkMyv68NUrwZeC7UBNl4wujVbNTcZDUnkecwQoNcrohh3CDAhdCMDl8VVVyX3YQhIbTTaV9TjIIeecjYU-NoyTHZbqYR7Hhcvts_DyxZ0szD-GGdD-o59VU8kIibm93yZhQAqIsMWE', start_index=7659)
Annotation(end_index=8449, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9hv9SewvqmTTfC5Aag89yBFvlABxEqxWkhYGD3HZtvr_a8TrOb00GPcRNd-PJ-a33J6_v7WKb6H05So2SomyYr79wyk6-8A9dz9lhon_zQEMoJA9D11UBio0jQpbDOUhXPJnPFiaWY9WvCLtwCtlX8yrrdokUUA==', start_index=8435)
Annotation(end_index=8449, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4W1tnbSgICpLCOcz7uq45NK4EwBj5D_NsyHli4ekbNjR6HxXjwaYcEgoFzuWeB_clUVVFr9uiWCKOMHhPMrBFt3e8lt92TStm19fKKU9yLZByeNJKXBQEPc1-0Jcm6P6DPNaTIFn1loMqkxIA0HCYAHwBFsEfVmFQ0aSsXr1MAxZVob7SwnkH_ZyYdA==', start_index=8435)
Annotation(end_index=9012, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvlQfX_8GBDRZGzBMncqVeYrlGZ07dtuPQeEQpjiUdTQoSeBO9pKn2V-rkSMPVY-gvfhCY0YXrZBrcM_tFwKJEURIrOrnt6_ocwC_UiDlkIWTpuE6-', start_index=8998)
Annotation(end_index=9012, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4jUZ45dygFsstQ_tzBw6Oc9ouwao1aQiXtZsR5YYSvGfX8Ej5XcV8-Qno8OXmYHsp8iBTHqDnHSAhEUDDc95NknIrfo9j_cMkSpwmWOwIWk1jzf_4pUMBu2WNClNHnyLCK0Wwn-kP', start_index=8998)
Annotation(end_index=9302, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9YQiBW1OThGVlSj2-RaoNMnntPmWFM-QphKhpjxU-dCntJBJ-ouYSYP9eGpASJmSCnNDNTS5X7O52hxcRg-b4yBzcg-Fz-835kOWLyvyQBC7P-LGCkoe0gXfWYynH8nHFksvlBWi0a6oPsWQgj7tJfhF7fv06HPmVv8X1ZXyyDv3bkhNWZEf0RE82SZ3lBR8iMFADuCZZ1XVM8PADgqq-rTDZb-QvrK_dTRS7hLGPesWM38YJLspS0RlG0EOc7g==', start_index=9289)
Annotation(end_index=9302, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_IZ_xbFYH1u9c8ZWDuTta3JsyseOxAwE8kelqg_HziaxKh-GAT2VT9SdYbR2NniYSj5mQcCNZM-jBUcocIJzsUfEoyRnI7zcE3yCqUE_G66rqaL-cGVBsRjxoyyyDew==', start_index=9289)
Annotation(end_index=9866, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1ptghs36j-F3IFBVISZzT3cOcnKvADk3B9m-3chTfRpJsrxfLMEyIuqaYDy_6nOAIH1WCOTTCfXFKTBcq5q1ehgqE1jT6wlTINZ1_QxyferXcZ3xhpndfKFXqPc2w8MubU7KJPnV23Q==', start_index=9852)
Annotation(end_index=9866, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ26tMA1YVtZyAaEFdxfrbnpXKAXgCcpfMX09xLoAwKBRqFbWRYStasESrd50oy5j_2SFaYT-G0Em5Ls05iqdeZLiX_XCS8O8DnTV9E8ieyh_mLT4n', start_index=9852)
Annotation(end_index=10276, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1ptghs36j-F3IFBVISZzT3cOcnKvADk3B9m-3chTfRpJsrxfLMEyIuqaYDy_6nOAIH1WCOTTCfXFKTBcq5q1ehgqE1jT6wlTINZ1_QxyferXcZ3xhpndfKFXqPc2w8MubU7KJPnV23Q==', start_index=10262)
Annotation(end_index=10276, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEps-KZ4G6riaE2l8sgQVITXuIIGgFvxoEcboedRpJXzcrtOO3iyHon6CNiKuoaOzKQFh_umkAqio2lzUxFcLgC1PBLaews_Du49RzooSS3h8UCI7zozXve16HvMlAx3IlLoDef4mmWgFHAGx1O38J6a_SASGrkvJ8E7LttBf7tLms-LXTkj29N4Od57OUePp8fvUiEqbIp92-okdq-hvI=', start_index=10262)
Annotation(end_index=10729, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1ptghs36j-F3IFBVISZzT3cOcnKvADk3B9m-3chTfRpJsrxfLMEyIuqaYDy_6nOAIH1WCOTTCfXFKTBcq5q1ehgqE1jT6wlTINZ1_QxyferXcZ3xhpndfKFXqPc2w8MubU7KJPnV23Q==', start_index=10715)
Annotation(end_index=10729, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkuVcbM5N95U27PDanbKHsU-ffWs-TltNvNSa3KSDFlncI2MhtRUoF9bQrhqRVB7se7gauQ8WpXQImOi4ZCaE_YM0V0j-56xzs-Q9Vwc3g72_tyLTxfrKGfhrj_vvNhbSmf3LbY-VE7IMpJeWXYVsAPCw3txmGD_IO8XP7XgDKwwat6XQqdkifn3OKkkLZX_5gIWZaarswas9f5arEpcZNrwAkKJs2puvf2_doJkcYVB-PWCf17dazfVYqv3zb4xzKS1PN4VE86JC7YBxiO5Ljd84wArguar6ezncGqi_DWjLUbBrD5qqTo3y-LixjHwZ7yUoHMvlV9-lFryx3jov35qhr2xTcRNR4dw==', start_index=10715)
Annotation(end_index=10843, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJQBkT7tnpXXZK07kQyCTYdBbqgCN2zl2vYRQAN30Dpf7YoR8xaZZboSRC5tR7TqLmlTkmZktFodcfO5rmX6H3lWaDCxbxRbu_ZTe8Ju-iLjfYeHiLonc_8Dc36dmsrla6YA==', start_index=10833)
Annotation(end_index=11178, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEgslbPsgkrId8VNhBxcgZCdFFyZelrJShlky0sQdUiShExPJdpb4hDhws9-d6BaRCSVt8bEbs0kU_cLhqqGn6sBCOR6sQpnJzDCdK_toTZkcb0WwvWZ-IjaodZmzukdBrJpHElY5HQEadBV3FqI51', start_index=11164)
Annotation(end_index=11178, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ26tMA1YVtZyAaEFdxfrbnpXKAXgCcpfMX09xLoAwKBRqFbWRYStasESrd50oy5j_2SFaYT-G0Em5Ls05iqdeZLiX_XCS8O8DnTV9E8ieyh_mLT4n', start_index=11164)
Annotation(end_index=11396, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHa5Z2yPjDSc-9RXhxJMJAUcMt4q4fRoikKxTQHbumtep6aREV7Z7MljfbKznXNBdp-9DRBSZ32rJMuOz2ME7uYtfTDiqBzlS63MTj0f1kAjt8Z0Zyc16_WM6WeBb6UKzQYKM802yzDHTdRdi_9x6uK8_7bR7Vo4Q0l6shDSIWqKZ6j6Lb46RsvrrymsZfTzlO4i6Noi08Cs4=', start_index=11382)
Annotation(end_index=11396, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbz8glrkGtw1ezFeRwsT6OIzFTY5HkhuXypobqdw0lSrku4rbCXau4PkSQkzhturuIYYBtugRCWEJLQNnCGKaq-UgHF-94BANSJ5CLEwTuPd2lm--CUVhPTJWQID8__Q==', start_index=11382)
Annotation(end_index=11833, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEv9w48aLXTjP56_vpe9D1cBdWDgc4c-bLsSXakqjDpmr84V__tFv2YAmn3dpehp4V5WrtjNtsfAnpR81UnAGvmpkxTlD45cqpbEXDrqYw0wQMD6BLhwMxV2v1R98nkwXKtjrrjNYRaFjaF5pOkabgjT377LLG2e3k=', start_index=11824)
Annotation(end_index=12164, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEgslbPsgkrId8VNhBxcgZCdFFyZelrJShlky0sQdUiShExPJdpb4hDhws9-d6BaRCSVt8bEbs0kU_cLhqqGn6sBCOR6sQpnJzDCdK_toTZkcb0WwvWZ-IjaodZmzukdBrJpHElY5HQEadBV3FqI51', start_index=12150)
Annotation(end_index=12164, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGAK35qf-LuhBNAUdmKN2VazPB3yFDsTW2F3ur1LW558s8Kg3Z13u0P8Rbchxjmth-zaotEVYxi3StGfTqwq2rdyQtxoftUHvS4MEjiY0_gUw9KiHgGIWt-S94xUZaueG4qVu74QXDJuO9x7cn2K4RLYIIQOUbvwCHey1jifTbnM8KIwTpJ90aOVMbRXvq_lGTIF5SyAQSK_Fz0zoTew==', start_index=12150)
Annotation(end_index=12387, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7xwpvhS0ZJ-RNWvTY8bRNkympbgsPlVjLMbM7UtWOXQoLsSujOr_vms_HI0Hm4tYOmb-CL6BTGy_Ynhbw9erPKTIuYOvrHNPF-GngdevE5YsWY_3Y_GtrEnKg51BPC0th41l4eMHL', start_index=12373)
Annotation(end_index=12387, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsA-Oo2Ga1BI3nkwBNFVDcEkSS5-mrt4CQa5yb4CtCD5N-HNBRVi3bAx9FnSvTxDykDN5WE_IxEvqgwFRW5tvXLHxH2TcB0NEEqBfH1df8dq-k46DXBKihNetvU4b0RnHetcYRIQJ6VQ==', start_index=12373)
Annotation(end_index=12697, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8HZy0V01CN3fHXWNbU9MfRFEjAlbDmTW9L-0fM89rKMQmXPrmlB6QTVpGfG4vfqmOfDjRsSqyxsypSSy_nHOtQpiEi8nyfsq1bWvVIU1Vkpz24N77', start_index=12685)
Annotation(end_index=12697, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5xU--RU_2_P7Hx_W3J_Q6BCAzo7KqFkygKB86dwlNxS-ix70jrECRITEHqgm8KUtQk-hs493qONDDgQNDTQrGUPW3O2OkOO437lIqp6TNKsn6bO0Vl-3CCYVcKCj4TiDWGnKW3oDCXQ==', start_index=12685)
Annotation(end_index=13031, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5xU--RU_2_P7Hx_W3J_Q6BCAzo7KqFkygKB86dwlNxS-ix70jrECRITEHqgm8KUtQk-hs493qONDDgQNDTQrGUPW3O2OkOO437lIqp6TNKsn6bO0Vl-3CCYVcKCj4TiDWGnKW3oDCXQ==', start_index=13022)
Annotation(end_index=13238, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0rpqnlk1rPc1Sm_Uh_WHRORij5c6JdB7-5-_pFSiSn94b0QfyfCTZDVPBGQZgWm18EJ3xNbA7kmbNFt130UyJv4Fo2LLoxoNKO3_kdTRyHQP7GePCiaVT--rpm2uc6vST4OM=', start_index=13225)
Annotation(end_index=13238, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQrZA4fVv6cDfGDlDB1OHJijke_MkvrdI9flq84iUDQd9FGlE5VHYTP1DWJAH-i-wzMyv85ibTGHJAoI_nxdGIiKGovHQzjHNSEjT3PZ-OkkdJbSJCA0R_-uBR4daW7SnPYe5Zz3NxbUxtUccEfY1NgNQoBTHVxwyR3bs3d1JfuRs-bHDhXj76Oov1IWHpLaAYtJ6oSe3spToYEi3-Cjo-xCZ59vE=', start_index=13225)
Annotation(end_index=13519, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQzNusutnMCqLIQpVjdqwk_OS5DVHzjaQ34QrdbE3uJ7ifKbsGC2AW8Z9huSRCPzCI0FdHszee6bi4yMHJ0rhNxgCWwjBM0b6gLCmBlitEhmASJ73BIlLtRMjUBLR_6zkzGeInkg4FBg==', start_index=13507)
Annotation(end_index=13519, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5xU--RU_2_P7Hx_W3J_Q6BCAzo7KqFkygKB86dwlNxS-ix70jrECRITEHqgm8KUtQk-hs493qONDDgQNDTQrGUPW3O2OkOO437lIqp6TNKsn6bO0Vl-3CCYVcKCj4TiDWGnKW3oDCXQ==', start_index=13507)
Annotation(end_index=13831, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9hv9SewvqmTTfC5Aag89yBFvlABxEqxWkhYGD3HZtvr_a8TrOb00GPcRNd-PJ-a33J6_v7WKb6H05So2SomyYr79wyk6-8A9dz9lhon_zQEMoJA9D11UBio0jQpbDOUhXPJnPFiaWY9WvCLtwCtlX8yrrdokUUA==', start_index=13817)
Annotation(end_index=13831, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHZ3hx-Il5aYgzL_gvPnprentjHgEi6VagoNpNKt34f7wpt4iBQdW3bKDJmtQBOmPvZo6v_pCM2R5ui6ypSDGPgcCLcXqgJLTN1QNvgtz3WN08Dp5douzwU2KrfcvLAQ==', start_index=13817)
Annotation(end_index=14285, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1L19HWzUWTBHUHmaurpXziETKNVuLeTpxi4fNiD52zFBCJif3c6WYLYy_umt5Iu1FcL14WwRBNd3ZC4kE6VcKRbrn8N8jvuYsiAxH2_flLQW3D1EoFIfQ1jdfbLup87QylvOly3xK', start_index=14271)
Annotation(end_index=14285, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHZ3hx-Il5aYgzL_gvPnprentjHgEi6VagoNpNKt34f7wpt4iBQdW3bKDJmtQBOmPvZo6v_pCM2R5ui6ypSDGPgcCLcXqgJLTN1QNvgtz3WN08Dp5douzwU2KrfcvLAQ==', start_index=14271)
Annotation(end_index=14560, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgStil9BiL1DPyme__W9Eb6IOyuOr_9WFx6CLyDN7kasmU-UWKvyM8knGMK0VuLAzMyswiXSM9q40TgUw24POX_U221E8XIFTcojjzXndbTf6cIPcYBZvZ0UT7cg3gCbtKd0DMz_WfbQ8LMUFPx8MgM3JihGLR5LcuKw==', start_index=14546)
Annotation(end_index=14560, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs0WmGsleth38vSK3wzuMrO8LGxHL2X_kUT0DnsYQ-pP4wux1bvLEGubBTrB8RbV_ib40lhtc9IhchRlCrpvuexsnjEsizYT47GjzEN9NSKiWjJg2mEG1PbKYmT0vM2g9ivi-pLrnE', start_index=14546)
Annotation(end_index=15032, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs0WmGsleth38vSK3wzuMrO8LGxHL2X_kUT0DnsYQ-pP4wux1bvLEGubBTrB8RbV_ib40lhtc9IhchRlCrpvuexsnjEsizYT47GjzEN9NSKiWjJg2mEG1PbKYmT0vM2g9ivi-pLrnE', start_index=15018)
Annotation(end_index=15032, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEVvyOqP01Ajrg_mit6CfN2Cyz-FB04LZSBmuFpNgf6rOYdVGcNr4HNlQJx8HwXiNsLyzUG-yZYAyhrm4x60FXGX2CAq4y3A1c1ALmmp095IN-hwxD004lYrwNFsBdZ-8ut_rI_xDxSg==', start_index=15018)
Annotation(end_index=15377, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgStil9BiL1DPyme__W9Eb6IOyuOr_9WFx6CLyDN7kasmU-UWKvyM8knGMK0VuLAzMyswiXSM9q40TgUw24POX_U221E8XIFTcojjzXndbTf6cIPcYBZvZ0UT7cg3gCbtKd0DMz_WfbQ8LMUFPx8MgM3JihGLR5LcuKw==', start_index=15363)
Annotation(end_index=15377, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEVvyOqP01Ajrg_mit6CfN2Cyz-FB04LZSBmuFpNgf6rOYdVGcNr4HNlQJx8HwXiNsLyzUG-yZYAyhrm4x60FXGX2CAq4y3A1c1ALmmp095IN-hwxD004lYrwNFsBdZ-8ut_rI_xDxSg==', start_index=15363)
Annotation(end_index=15686, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE95e3zKsITNT1ApsDpPYxzW_3M2XMznjbLf1DKXSWdxVXJf7npzk1MCp-WrbcbTPvuIgfyTM6NkerGovHzTTk8P_JezVwjO7uL2kGvsBQampUtzyDaKgsuyd0_MgDJZt0sklwGV64i', start_index=15672)
Annotation(end_index=15686, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHsCFUc78ePHdORtLshRrGnMB6iO4afKtvRj4ZO5wdBunNwnbhmzDPsUMyWF_j5QnbUh9OHADBG2KshgKbMTVXSHjfL9yBX8ZRL8wD195J0z4SKcFI8__8ykT357kCxlqGSLlgNjkV_zOyt5YiK4fqVkCg5cjfiL5lr0D0Ay4wys_RBoW6frut__pKWu3Q6499NdPodQDFpt6cEbkTwe6_lJQvnzFIsUfrzZZPQUv_yelxHduQ8mjPN2qchF9yKRdbu2i4kX9m3v5pqMvlqAqPNgvZ4pZTWV_tVQ==', start_index=15672)
Annotation(end_index=16079, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgStil9BiL1DPyme__W9Eb6IOyuOr_9WFx6CLyDN7kasmU-UWKvyM8knGMK0VuLAzMyswiXSM9q40TgUw24POX_U221E8XIFTcojjzXndbTf6cIPcYBZvZ0UT7cg3gCbtKd0DMz_WfbQ8LMUFPx8MgM3JihGLR5LcuKw==', start_index=16069)
Annotation(end_index=16528, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0d6SXwBum3ADhAsX-eBUNrwclUkqe8fhleiCy1gv9h__QNyuWA5JXngpKy4lFfdj_umn9jZDIWaw-JuKLwqK7mmLZAMqTywlpcmDDMxBoUSX7rAVykipDMsUUz3plgBtAV3ICaPZZAmIKuufEEPt4UNk9N7rmNUjt2f0V3tckPkoqL2OPtcI=', start_index=16515)
Annotation(end_index=16528, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEv9w48aLXTjP56_vpe9D1cBdWDgc4c-bLsSXakqjDpmr84V__tFv2YAmn3dpehp4V5WrtjNtsfAnpR81UnAGvmpkxTlD45cqpbEXDrqYw0wQMD6BLhwMxV2v1R98nkwXKtjrrjNYRaFjaF5pOkabgjT377LLG2e3k=', start_index=16515)
Annotation(end_index=16676, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8qXK1O0aBy3RKnX3gOqSQICWED3LyTCzylBtw7IDYkFjqrfu5ZTQrO-JhIBPsYC7DZjFtlnd0cIInDR-aMyeGul7H7RsW7HDg030d2Cd_HdMqVdjqeuTFU3jHJr8z-JHEGeBbF661YjF-HsqRyr_8KjhTI-zEspSckGfzWNagUiA6hjzHpj9SNjALNe-l49RLwiKKHrE4bg==', start_index=16666)
Annotation(end_index=16878, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5JeG78gjbNgowyHW0gL5S4csQmZOUt6Uv7UXIPPs8J9apYLxQSVTgcN9tqezPSCzoezezF3VtsRUK1S81dkoPG21bAZL78gjkdkl78F-ugO4CaSlwNtoQrnygcZqOPdeu2qoh67th__U_cdIgY3RgxXhM1Th1-In9WV9R1cFcYn3UYaQihbsUJ2bqmIjQC3P7GcdBAmSnP1oC', start_index=16864)
Annotation(end_index=16878, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvICwrbDcHvqXTgw1kOKmvBeG-PRMNPwRvbDZJDrPapHEf432KLAziZi_gRn7DPWyIBRUYxjBoV90yg2yIV4kKcOp7STZ3dRFqJgU3ortxHslv-sdEn9EtctriZvGvk3b4tXK3awv34veAj1f9WDOafgpdZb-hL0KQrkx5ltRpfUI=', start_index=16864)
Annotation(end_index=17233, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGf69MQVYLEGSiPV6VV9CB_b-jX4p0Xg_JVEaXODNViR5ODvlUZe3RjBRRkn3XknoHuuWIKcO5kqEovelJ9cPoVL49rKP483Omr6CyrEoSJLexXifSaY30JyIA_khZncoPEnC2jkJM0', start_index=17219)
Annotation(end_index=17233, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdfpm6V2AptWMkB0l8E2W_zmVZoVyQeMKvEmqIFHejOH_cUb2-mr7UTV2c3l9OqaQE_AlM10TpT2zoMyBdEKkYK2dkNa4FQ1i8rZ8ePVrEBnyWPegBrZUfhKwdvYmOmaoXer-LjYb2', start_index=17219)
Annotation(end_index=17545, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsS8SHM4L3mz8WBE4xZJOrBnAPOrZy8UljLtMB9hxCwUPX4i_WysgzCamGLTZokHh84q3Efv2fyFxmGAmLxyC69piduAPHWTKFt8_ZYeEA8lY6UAQRZKQxb4hH7YDKleWLgtj2zI7wrPI77wwzDO6fgfo4bdngDNTScWKNVW8uJifxhcp5hkPtDVefdTsClIyF1g==', start_index=17535)
Annotation(end_index=17859, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5JeG78gjbNgowyHW0gL5S4csQmZOUt6Uv7UXIPPs8J9apYLxQSVTgcN9tqezPSCzoezezF3VtsRUK1S81dkoPG21bAZL78gjkdkl78F-ugO4CaSlwNtoQrnygcZqOPdeu2qoh67th__U_cdIgY3RgxXhM1Th1-In9WV9R1cFcYn3UYaQihbsUJ2bqmIjQC3P7GcdBAmSnP1oC', start_index=17845)
Annotation(end_index=17859, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8qXK1O0aBy3RKnX3gOqSQICWED3LyTCzylBtw7IDYkFjqrfu5ZTQrO-JhIBPsYC7DZjFtlnd0cIInDR-aMyeGul7H7RsW7HDg030d2Cd_HdMqVdjqeuTFU3jHJr8z-JHEGeBbF661YjF-HsqRyr_8KjhTI-zEspSckGfzWNagUiA6hjzHpj9SNjALNe-l49RLwiKKHrE4bg==', start_index=17845)
Annotation(end_index=18041, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9YQiBW1OThGVlSj2-RaoNMnntPmWFM-QphKhpjxU-dCntJBJ-ouYSYP9eGpASJmSCnNDNTS5X7O52hxcRg-b4yBzcg-Fz-835kOWLyvyQBC7P-LGCkoe0gXfWYynH8nHFksvlBWi0a6oPsWQgj7tJfhF7fv06HPmVv8X1ZXyyDv3bkhNWZEf0RE82SZ3lBR8iMFADuCZZ1XVM8PADgqq-rTDZb-QvrK_dTRS7hLGPesWM38YJLspS0RlG0EOc7g==', start_index=18028)
Annotation(end_index=18041, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4W1tnbSgICpLCOcz7uq45NK4EwBj5D_NsyHli4ekbNjR6HxXjwaYcEgoFzuWeB_clUVVFr9uiWCKOMHhPMrBFt3e8lt92TStm19fKKU9yLZByeNJKXBQEPc1-0Jcm6P6DPNaTIFn1loMqkxIA0HCYAHwBFsEfVmFQ0aSsXr1MAxZVob7SwnkH_ZyYdA==', start_index=18028)
Annotation(end_index=18286, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1ptghs36j-F3IFBVISZzT3cOcnKvADk3B9m-3chTfRpJsrxfLMEyIuqaYDy_6nOAIH1WCOTTCfXFKTBcq5q1ehgqE1jT6wlTINZ1_QxyferXcZ3xhpndfKFXqPc2w8MubU7KJPnV23Q==', start_index=18272)
Annotation(end_index=18286, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHa5Z2yPjDSc-9RXhxJMJAUcMt4q4fRoikKxTQHbumtep6aREV7Z7MljfbKznXNBdp-9DRBSZ32rJMuOz2ME7uYtfTDiqBzlS63MTj0f1kAjt8Z0Zyc16_WM6WeBb6UKzQYKM802yzDHTdRdi_9x6uK8_7bR7Vo4Q0l6shDSIWqKZ6j6Lb46RsvrrymsZfTzlO4i6Noi08Cs4=', start_index=18272)
Annotation(end_index=18739, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs0WmGsleth38vSK3wzuMrO8LGxHL2X_kUT0DnsYQ-pP4wux1bvLEGubBTrB8RbV_ib40lhtc9IhchRlCrpvuexsnjEsizYT47GjzEN9NSKiWjJg2mEG1PbKYmT0vM2g9ivi-pLrnE', start_index=18726)
Annotation(end_index=18739, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5xU--RU_2_P7Hx_W3J_Q6BCAzo7KqFkygKB86dwlNxS-ix70jrECRITEHqgm8KUtQk-hs493qONDDgQNDTQrGUPW3O2OkOO437lIqp6TNKsn6bO0Vl-3CCYVcKCj4TiDWGnKW3oDCXQ==', start_index=18726)
Annotation(end_index=18765, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXupczIeT8tC3Bqj3E7FV60Q-Ou286li466m7N_51KOW7E8tvKr0TOspIpF3ev_bNV2ybXBw-foOTPkrJyQm59fPS7EuKMhA5MAgcv47SG1Ml5cxfJJ4XifCUUunnRs7_qn5uMh6Oy', start_index=18756)
Annotation(end_index=18786, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0rpqnlk1rPc1Sm_Uh_WHRORij5c6JdB7-5-_pFSiSn94b0QfyfCTZDVPBGQZgWm18EJ3xNbA7kmbNFt130UyJv4Fo2LLoxoNKO3_kdTRyHQP7GePCiaVT--rpm2uc6vST4OM=', start_index=18777)
Annotation(end_index=18809, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWa8DIBrGZAnW5GAA1Pnl8W6bNoh73bbHpSUiGX-l8n1JH3fgM9JBi_PtPGyyZtV4rcTzc0z3K127Hn3smtBSLRlga29GoVBzwPOhpJzxgr29jDm2XaJy1CJBb7SSChQ-lw3Q0hHQx', start_index=18800)
Annotation(end_index=18830, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQzNusutnMCqLIQpVjdqwk_OS5DVHzjaQ34QrdbE3uJ7ifKbsGC2AW8Z9huSRCPzCI0FdHszee6bi4yMHJ0rhNxgCWwjBM0b6gLCmBlitEhmASJ73BIlLtRMjUBLR_6zkzGeInkg4FBg==', start_index=18821)
Annotation(end_index=18853, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5JeG78gjbNgowyHW0gL5S4csQmZOUt6Uv7UXIPPs8J9apYLxQSVTgcN9tqezPSCzoezezF3VtsRUK1S81dkoPG21bAZL78gjkdkl78F-ugO4CaSlwNtoQrnygcZqOPdeu2qoh67th__U_cdIgY3RgxXhM1Th1-In9WV9R1cFcYn3UYaQihbsUJ2bqmIjQC3P7GcdBAmSnP1oC', start_index=18843)
Annotation(end_index=18898, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsS8SHM4L3mz8WBE4xZJOrBnAPOrZy8UljLtMB9hxCwUPX4i_WysgzCamGLTZokHh84q3Efv2fyFxmGAmLxyC69piduAPHWTKFt8_ZYeEA8lY6UAQRZKQxb4hH7YDKleWLgtj2zI7wrPI77wwzDO6fgfo4bdngDNTScWKNVW8uJifxhcp5hkPtDVefdTsClIyF1g==', start_index=18888)
Annotation(end_index=18928, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvICwrbDcHvqXTgw1kOKmvBeG-PRMNPwRvbDZJDrPapHEf432KLAziZi_gRn7DPWyIBRUYxjBoV90yg2yIV4kKcOp7STZ3dRFqJgU3ortxHslv-sdEn9EtctriZvGvk3b4tXK3awv34veAj1f9WDOafgpdZb-hL0KQrkx5ltRpfUI=', start_index=18918)
Annotation(end_index=18983, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0d6SXwBum3ADhAsX-eBUNrwclUkqe8fhleiCy1gv9h__QNyuWA5JXngpKy4lFfdj_umn9jZDIWaw-JuKLwqK7mmLZAMqTywlpcmDDMxBoUSX7rAVykipDMsUUz3plgBtAV3ICaPZZAmIKuufEEPt4UNk9N7rmNUjt2f0V3tckPkoqL2OPtcI=', start_index=18973)
Annotation(end_index=19020, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8qXK1O0aBy3RKnX3gOqSQICWED3LyTCzylBtw7IDYkFjqrfu5ZTQrO-JhIBPsYC7DZjFtlnd0cIInDR-aMyeGul7H7RsW7HDg030d2Cd_HdMqVdjqeuTFU3jHJr8z-JHEGeBbF661YjF-HsqRyr_8KjhTI-zEspSckGfzWNagUiA6hjzHpj9SNjALNe-l49RLwiKKHrE4bg==', start_index=19010)
Annotation(end_index=19062, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4vzehNqeLrFB2J84wZmboLXAmvqKnHaqcyW2uCuT0kGQ5NWdsnZe5n9v4dr7EUKe6pD1V5JgeOD9jEKqbQgfJpO0WdqLGm00YY8EfEAroq4MRdyKZ2iIoLOA81_H7', start_index=19052)
Annotation(end_index=19087, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsvQDpe-s6QL0zDC9A725RrumBD2YU0hodoq8MntArKQtyS4HTT5tYE1P1WI-ZhoNVqy-rDynTTik9UejbcAuLujjx7F60PijqOcmS4pmMrYDXjM_67CM_dF2rLtyVY6-zOg==', start_index=19078)
Annotation(end_index=19122, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQrZA4fVv6cDfGDlDB1OHJijke_MkvrdI9flq84iUDQd9FGlE5VHYTP1DWJAH-i-wzMyv85ibTGHJAoI_nxdGIiKGovHQzjHNSEjT3PZ-OkkdJbSJCA0R_-uBR4daW7SnPYe5Zz3NxbUxtUccEfY1NgNQoBTHVxwyR3bs3d1JfuRs-bHDhXj76Oov1IWHpLaAYtJ6oSe3spToYEi3-Cjo-xCZ59vE=', start_index=19112)
Annotation(end_index=19162, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5xU--RU_2_P7Hx_W3J_Q6BCAzo7KqFkygKB86dwlNxS-ix70jrECRITEHqgm8KUtQk-hs493qONDDgQNDTQrGUPW3O2OkOO437lIqp6TNKsn6bO0Vl-3CCYVcKCj4TiDWGnKW3oDCXQ==', start_index=19153)
Annotation(end_index=19184, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8HZy0V01CN3fHXWNbU9MfRFEjAlbDmTW9L-0fM89rKMQmXPrmlB6QTVpGfG4vfqmOfDjRsSqyxsypSSy_nHOtQpiEi8nyfsq1bWvVIU1Vkpz24N77', start_index=19175)
Annotation(end_index=19211, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEM_PHe5WV5GXYZU8x6Ybhmj_bZNV5VEY67QZOixKAQfus8_gjDsGu-Cu91f1TcPY_tsEWnY5j5AcpyIKVZCPtuOQA8uEdmhjYByDbuGJNqhVGbQ1RK7RgkR3CFQertmghOb2evm5D3', start_index=19201)
Annotation(end_index=19231, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9YQiBW1OThGVlSj2-RaoNMnntPmWFM-QphKhpjxU-dCntJBJ-ouYSYP9eGpASJmSCnNDNTS5X7O52hxcRg-b4yBzcg-Fz-835kOWLyvyQBC7P-LGCkoe0gXfWYynH8nHFksvlBWi0a6oPsWQgj7tJfhF7fv06HPmVv8X1ZXyyDv3bkhNWZEf0RE82SZ3lBR8iMFADuCZZ1XVM8PADgqq-rTDZb-QvrK_dTRS7hLGPesWM38YJLspS0RlG0EOc7g==', start_index=19222)
Annotation(end_index=19264, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4jUZ45dygFsstQ_tzBw6Oc9ouwao1aQiXtZsR5YYSvGfX8Ej5XcV8-Qno8OXmYHsp8iBTHqDnHSAhEUDDc95NknIrfo9j_cMkSpwmWOwIWk1jzf_4pUMBu2WNClNHnyLCK0Wwn-kP', start_index=19254)
Annotation(end_index=19286, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMWaiyDVZFOLK0ShTlM4kXCnkI7fLpJrtMb1J0-mZqJN_lciwAWBsEKkrR_ZZHJAgRh9TDg2N62myeSGy_V-AyiMh0H7tYt4GOCn_kyfDAglbvgd1KKm-Nl41IC9NLiHfZzuRb', start_index=19276)
Annotation(end_index=19328, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvlQfX_8GBDRZGzBMncqVeYrlGZ07dtuPQeEQpjiUdTQoSeBO9pKn2V-rkSMPVY-gvfhCY0YXrZBrcM_tFwKJEURIrOrnt6_ocwC_UiDlkIWTpuE6-', start_index=19318)
Annotation(end_index=19355, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgStil9BiL1DPyme__W9Eb6IOyuOr_9WFx6CLyDN7kasmU-UWKvyM8knGMK0VuLAzMyswiXSM9q40TgUw24POX_U221E8XIFTcojjzXndbTf6cIPcYBZvZ0UT7cg3gCbtKd0DMz_WfbQ8LMUFPx8MgM3JihGLR5LcuKw==', start_index=19345)
Annotation(end_index=19393, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEv9w48aLXTjP56_vpe9D1cBdWDgc4c-bLsSXakqjDpmr84V__tFv2YAmn3dpehp4V5WrtjNtsfAnpR81UnAGvmpkxTlD45cqpbEXDrqYw0wQMD6BLhwMxV2v1R98nkwXKtjrrjNYRaFjaF5pOkabgjT377LLG2e3k=', start_index=19384)
Annotation(end_index=19446, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7xwpvhS0ZJ-RNWvTY8bRNkympbgsPlVjLMbM7UtWOXQoLsSujOr_vms_HI0Hm4tYOmb-CL6BTGy_Ynhbw9erPKTIuYOvrHNPF-GngdevE5YsWY_3Y_GtrEnKg51BPC0th41l4eMHL', start_index=19436)
Annotation(end_index=19468, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcoTW1nFlJBKt9hvyVXxIwOT-mkpgryBUwl9jKURQuDzbuhQb1li9U4lmDF9VPZffg-Mftii3qYDq4U2Bcv0Ad5hBJ6MagrT-VqWKeRz-dtntoo0mOzY1YowQ_US5QuQ==', start_index=19458)
Annotation(end_index=19503, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHZ3hx-Il5aYgzL_gvPnprentjHgEi6VagoNpNKt34f7wpt4iBQdW3bKDJmtQBOmPvZo6v_pCM2R5ui6ypSDGPgcCLcXqgJLTN1QNvgtz3WN08Dp5douzwU2KrfcvLAQ==', start_index=19493)
Annotation(end_index=19530, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9hv9SewvqmTTfC5Aag89yBFvlABxEqxWkhYGD3HZtvr_a8TrOb00GPcRNd-PJ-a33J6_v7WKb6H05So2SomyYr79wyk6-8A9dz9lhon_zQEMoJA9D11UBio0jQpbDOUhXPJnPFiaWY9WvCLtwCtlX8yrrdokUUA==', start_index=19520)
Annotation(end_index=19560, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEVvyOqP01Ajrg_mit6CfN2Cyz-FB04LZSBmuFpNgf6rOYdVGcNr4HNlQJx8HwXiNsLyzUG-yZYAyhrm4x60FXGX2CAq4y3A1c1ALmmp095IN-hwxD004lYrwNFsBdZ-8ut_rI_xDxSg==', start_index=19550)
Annotation(end_index=19583, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHsCFUc78ePHdORtLshRrGnMB6iO4afKtvRj4ZO5wdBunNwnbhmzDPsUMyWF_j5QnbUh9OHADBG2KshgKbMTVXSHjfL9yBX8ZRL8wD195J0z4SKcFI8__8ykT357kCxlqGSLlgNjkV_zOyt5YiK4fqVkCg5cjfiL5lr0D0Ay4wys_RBoW6frut__pKWu3Q6499NdPodQDFpt6cEbkTwe6_lJQvnzFIsUfrzZZPQUv_yelxHduQ8mjPN2qchF9yKRdbu2i4kX9m3v5pqMvlqAqPNgvZ4pZTWV_tVQ==', start_index=19573)
Annotation(end_index=19616, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEv9w48aLXTjP56_vpe9D1cBdWDgc4c-bLsSXakqjDpmr84V__tFv2YAmn3dpehp4V5WrtjNtsfAnpR81UnAGvmpkxTlD45cqpbEXDrqYw0wQMD6BLhwMxV2v1R98nkwXKtjrrjNYRaFjaF5pOkabgjT377LLG2e3k=', start_index=19607)
Annotation(end_index=19669, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsA-Oo2Ga1BI3nkwBNFVDcEkSS5-mrt4CQa5yb4CtCD5N-HNBRVi3bAx9FnSvTxDykDN5WE_IxEvqgwFRW5tvXLHxH2TcB0NEEqBfH1df8dq-k46DXBKihNetvU4b0RnHetcYRIQJ6VQ==', start_index=19659)
Annotation(end_index=19692, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIl-J5nMjWstsK-QXrxQFUejA7NmpLe6oAEBX2snuMdlvtN3IOdoXBCKNeCC0Ix3Dqus-92xnp_Fwf6e-nE_hmrNgYHctD1onlnnNYsDph6Goqth0VjSHbfigTICb5sPzxn2avWhq02axi-dFGzC8I6KplU4oZt-za_2o1Wgxhu4rMBdngYhJdTt85sIIUwKUV1WtO4Wz_BtZuRLs9F9ZdqDScK2fhq3lUqWpHTrMItdvSfM50YOSpaVdk0fWj6pahjWrh', start_index=19682)
Annotation(end_index=19726, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9DMQ-03EWNU5b94rWOZgEthLE2ZTpLnkzlg21GB_AJXLhGpFLOWFEVaxFXlgrS66lA4kbPY0w-yfLY_k6MElKLqqyKdNdekptKuk-ytsmXYRNwSTXley6kya72AhzXds=', start_index=19716)
Annotation(end_index=19756, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGAK35qf-LuhBNAUdmKN2VazPB3yFDsTW2F3ur1LW558s8Kg3Z13u0P8Rbchxjmth-zaotEVYxi3StGfTqwq2rdyQtxoftUHvS4MEjiY0_gUw9KiHgGIWt-S94xUZaueG4qVu74QXDJuO9x7cn2K4RLYIIQOUbvwCHey1jifTbnM8KIwTpJ90aOVMbRXvq_lGTIF5SyAQSK_Fz0zoTew==', start_index=19746)
Annotation(end_index=19792, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEgslbPsgkrId8VNhBxcgZCdFFyZelrJShlky0sQdUiShExPJdpb4hDhws9-d6BaRCSVt8bEbs0kU_cLhqqGn6sBCOR6sQpnJzDCdK_toTZkcb0WwvWZ-IjaodZmzukdBrJpHElY5HQEadBV3FqI51', start_index=19782)
Annotation(end_index=19830, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP10pU6thA6F6hJ14N9Xd58KpT-haBzgckcHq-cJqqTxAOBkvorsr7pUsClQYoFjaybJ9y-0ArmsFurZKieosnFrgM0M12xe5F2Usvx3xlW_Hj2C0oNSxOinip6kgkkW8nbVp7fKub', start_index=19820)
Annotation(end_index=19852, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGk3goOhhgJ7NY8E8yLnsof0GGnQkv4WoJErWfuOOuMOV0GKD98u0BvtdoQxwXXIY3pEpeMuaQMNpYgt8_oEz5uJ60_XkMLKdEEnWyNEAI8vPbFZLRiw7QosuE2DRANrpHx_xUnyg6w5w==', start_index=19842)
Annotation(end_index=19875, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGvefHhJnamgkkfUDYdOW_raYEbR9bVAMai349H8iKzZtf2Lu0e51gVTrhl0EWZOd8SeouGOBowxbwN8bnjjfsps04ULnW4Laj4EJVSrJC8Gcy4cAdBC-ucTRPK3ZhaO5_pmhygn9h2U_fDTfw4NRfezxDIyC8QKoylfwJqT49AKWtOf56lt6nQnEMYgHlEUrPH967ZZx3AFkQj1_xu3H7xlPH2AaEyt8n3tO2ePgSea-kIPw9sIqFaFNzZtUmtnrnXlbevgW3UcxOuTXEcEo=', start_index=19865)
Annotation(end_index=19909, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKLitcrewzOsO3-a19i1XMXMscRatScyoXav4idoVfLhUUubJbpUVfZ7IY6yK49i50KI76l6T7hOiP271EuXFRESj3zNGlm7eCaKE6bq3xAn4P6tdG0gpXQjPN6e7yoc4WXmnjLiABgZ0Nuln-Mjvw2wXvO1Oi7PNra85jD4mDdhzZvHX5IvCnTbMF_dhTsWTiamavo5d2uCPqMXzYkHcpi5ufR4nfZ1WYJ7mXVZm3o5UGmVhUoCrnM1haEReKA-OJOYiCugsChJLlZ1y63LXDYWcXXkOoX760XO14wbHRwPufJackiPQKpHGOBZoQpsWMUSg=', start_index=19899)
Annotation(end_index=19943, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGf69MQVYLEGSiPV6VV9CB_b-jX4p0Xg_JVEaXODNViR5ODvlUZe3RjBRRkn3XknoHuuWIKcO5kqEovelJ9cPoVL49rKP483Omr6CyrEoSJLexXifSaY30JyIA_khZncoPEnC2jkJM0', start_index=19933)
Annotation(end_index=19965, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZEjguttA4j52wiULJrv_SMyGug51wZ_VJD49bltmq24wt7kGy8ROMXRYT0z9GQo4AXFFq1lzEEOKqXiy7gmnlq0I1sT4omMSMRn8xIdBMNrZ6m_DJ6AHkCaZNPa6jBuGujgtSsswyIubkYr_R57U_UrOeE8jxagxgbmZia1J8kNHwHeTX9Q==', start_index=19955)
Annotation(end_index=20002, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdfpm6V2AptWMkB0l8E2W_zmVZoVyQeMKvEmqIFHejOH_cUb2-mr7UTV2c3l9OqaQE_AlM10TpT2zoMyBdEKkYK2dkNa4FQ1i8rZ8ePVrEBnyWPegBrZUfhKwdvYmOmaoXer-LjYb2', start_index=19992)
Annotation(end_index=20024, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8qXK1O0aBy3RKnX3gOqSQICWED3LyTCzylBtw7IDYkFjqrfu5ZTQrO-JhIBPsYC7DZjFtlnd0cIInDR-aMyeGul7H7RsW7HDg030d2Cd_HdMqVdjqeuTFU3jHJr8z-JHEGeBbF661YjF-HsqRyr_8KjhTI-zEspSckGfzWNagUiA6hjzHpj9SNjALNe-l49RLwiKKHrE4bg==', start_index=20014)
Annotation(end_index=20065, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9YQiBW1OThGVlSj2-RaoNMnntPmWFM-QphKhpjxU-dCntJBJ-ouYSYP9eGpASJmSCnNDNTS5X7O52hxcRg-b4yBzcg-Fz-835kOWLyvyQBC7P-LGCkoe0gXfWYynH8nHFksvlBWi0a6oPsWQgj7tJfhF7fv06HPmVv8X1ZXyyDv3bkhNWZEf0RE82SZ3lBR8iMFADuCZZ1XVM8PADgqq-rTDZb-QvrK_dTRS7hLGPesWM38YJLspS0RlG0EOc7g==', start_index=20056)
Annotation(end_index=20098, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4W1tnbSgICpLCOcz7uq45NK4EwBj5D_NsyHli4ekbNjR6HxXjwaYcEgoFzuWeB_clUVVFr9uiWCKOMHhPMrBFt3e8lt92TStm19fKKU9yLZByeNJKXBQEPc1-0Jcm6P6DPNaTIFn1loMqkxIA0HCYAHwBFsEfVmFQ0aSsXr1MAxZVob7SwnkH_ZyYdA==', start_index=20088)
Annotation(end_index=20131, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_IZ_xbFYH1u9c8ZWDuTta3JsyseOxAwE8kelqg_HziaxKh-GAT2VT9SdYbR2NniYSj5mQcCNZM-jBUcocIJzsUfEoyRnI7zcE3yCqUE_G66rqaL-cGVBsRjxoyyyDew==', start_index=20121)
Annotation(end_index=20158, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEm42H-kmOYGIOtTrAKZ-boG79Qe29gHbPSvDGtriR1lVOq438wSQ-rI7EiNhJrNCplgw4qx43tJgbkjUbvo9UT7aY2OP9T6ogPmGNUODQNSv-BHkWZ2k0X5jYOOPaz_w6LYPixFIdpet1B', start_index=20148)
Annotation(end_index=20185, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGsrhJbPBZzObi5xuQb66LuOGy8UCJSJ3vOwwZgIuaZoQ0u019f2Dzaw_0aOpTuT3QAECGqY3Iw_5d3ecRbvD5C71bR_jgDm0EqiPGvFd08dtE_jQqLFbh-dmZ-E4=', start_index=20175)
Annotation(end_index=20223, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5xU--RU_2_P7Hx_W3J_Q6BCAzo7KqFkygKB86dwlNxS-ix70jrECRITEHqgm8KUtQk-hs493qONDDgQNDTQrGUPW3O2OkOO437lIqp6TNKsn6bO0Vl-3CCYVcKCj4TiDWGnKW3oDCXQ==', start_index=20214)
Annotation(end_index=20246, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkj7OYbCT8x4rdwDS-RxSDH57qdWhv4iKy1sF16neK1aad46DFFRLbO-T30apvQRBXL6LdrymABJrCuGv9ZX0hsn8WaEVNidsx65M_W2AyaJ6ZV-2TQ1EZ3MYe8DPTR3qpg92D1aOiEr_UbF3XfDGdRx8TAEKhecj__mG4uoyITz-rDU6u-_owA5JwEu3HiV70LsdJgnmvqGPU1cyy42Is72CFfIUmYOPOgEZ6LqhclQZVEa5gWPNLsk30jHkw', start_index=20236)
Annotation(end_index=20280, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1L19HWzUWTBHUHmaurpXziETKNVuLeTpxi4fNiD52zFBCJif3c6WYLYy_umt5Iu1FcL14WwRBNd3ZC4kE6VcKRbrn8N8jvuYsiAxH2_flLQW3D1EoFIfQ1jdfbLup87QylvOly3xK', start_index=20270)
Annotation(end_index=20302, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPiT6eXWCICfkYpFV53IL4xDKXJgFLcrElgDekMoak62R4qUCVkWrB1qnX8FdnHY2RZ9wAncfLokhKIvqgzH9kYiuHmNC6VtUjmKs85fWmRC6zPxUIZhxKIuhEIxN4VA==', start_index=20292)
Annotation(end_index=20343, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfmCu8NVwSsFmo4f-zZpljX_oTA6a_MNz7EDwwTWyJ22PFGBPNvkRbIa5KaM6G5WsSuiXnTjtB7WBfkpJAMBX1h73tc5-X4j7J3LObuFNiBrlr2rKPRPgC-Neign6aS8eosj3YDR8uFYqJtzHVVhWIUKLI6Mw2vN4beaBzkSZWeFy9XZjYlG_qM4Ib05aU', start_index=20333)
Annotation(end_index=20369, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE95e3zKsITNT1ApsDpPYxzW_3M2XMznjbLf1DKXSWdxVXJf7npzk1MCp-WrbcbTPvuIgfyTM6NkerGovHzTTk8P_JezVwjO7uL2kGvsBQampUtzyDaKgsuyd0_MgDJZt0sklwGV64i', start_index=20359)
Annotation(end_index=20391, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs0WmGsleth38vSK3wzuMrO8LGxHL2X_kUT0DnsYQ-pP4wux1bvLEGubBTrB8RbV_ib40lhtc9IhchRlCrpvuexsnjEsizYT47GjzEN9NSKiWjJg2mEG1PbKYmT0vM2g9ivi-pLrnE', start_index=20381)
Annotation(end_index=20413, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1ptghs36j-F3IFBVISZzT3cOcnKvADk3B9m-3chTfRpJsrxfLMEyIuqaYDy_6nOAIH1WCOTTCfXFKTBcq5q1ehgqE1jT6wlTINZ1_QxyferXcZ3xhpndfKFXqPc2w8MubU7KJPnV23Q==', start_index=20403)
Annotation(end_index=20436, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEps-KZ4G6riaE2l8sgQVITXuIIGgFvxoEcboedRpJXzcrtOO3iyHon6CNiKuoaOzKQFh_umkAqio2lzUxFcLgC1PBLaews_Du49RzooSS3h8UCI7zozXve16HvMlAx3IlLoDef4mmWgFHAGx1O38J6a_SASGrkvJ8E7LttBf7tLms-LXTkj29N4Od57OUePp8fvUiEqbIp92-okdq-hvI=', start_index=20426)
Annotation(end_index=20470, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9I7cuyqpb814DyZQ3C3ueH8X8iabDgaQFX61I5CIOdPgABsjWyIH1UjfA5deUu2ye6KdRAGUX0C9nBA3q3Q1oQzZb3Tg2QTgHEaqcEaHd4ieeBsbEPpnfR_ezZ_qyvIoYlqJxFN14y5KMKeVyDi5-Qbf5npLSXu4w0AMxbmSVk10FmSySf_EfKCBtyHYA-VGJgEo=', start_index=20460)
Annotation(end_index=20498, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHa5Z2yPjDSc-9RXhxJMJAUcMt4q4fRoikKxTQHbumtep6aREV7Z7MljfbKznXNBdp-9DRBSZ32rJMuOz2ME7uYtfTDiqBzlS63MTj0f1kAjt8Z0Zyc16_WM6WeBb6UKzQYKM802yzDHTdRdi_9x6uK8_7bR7Vo4Q0l6shDSIWqKZ6j6Lb46RsvrrymsZfTzlO4i6Noi08Cs4=', start_index=20488)
Annotation(end_index=20532, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJQBkT7tnpXXZK07kQyCTYdBbqgCN2zl2vYRQAN30Dpf7YoR8xaZZboSRC5tR7TqLmlTkmZktFodcfO5rmX6H3lWaDCxbxRbu_ZTe8Ju-iLjfYeHiLonc_8Dc36dmsrla6YA==', start_index=20522)
Annotation(end_index=20556, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4W1tnbSgICpLCOcz7uq45NK4EwBj5D_NsyHli4ekbNjR6HxXjwaYcEgoFzuWeB_clUVVFr9uiWCKOMHhPMrBFt3e8lt92TStm19fKKU9yLZByeNJKXBQEPc1-0Jcm6P6DPNaTIFn1loMqkxIA0HCYAHwBFsEfVmFQ0aSsXr1MAxZVob7SwnkH_ZyYdA==', start_index=20546)
Annotation(end_index=20589, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkMyv68NUrwZeC7UBNl4wujVbNTcZDUnkecwQoNcrohh3CDAhdCMDl8VVVyX3YQhIbTTaV9TjIIeecjYU-NoyTHZbqYR7Hhcvts_DyxZ0szD-GGdD-o59VU8kIibm93yZhQAqIsMWE', start_index=20579)
Annotation(end_index=20611, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ26tMA1YVtZyAaEFdxfrbnpXKAXgCcpfMX09xLoAwKBRqFbWRYStasESrd50oy5j_2SFaYT-G0Em5Ls05iqdeZLiX_XCS8O8DnTV9E8ieyh_mLT4n', start_index=20601)
Annotation(end_index=20638, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHCmDQt2FHpRCXPxO0DFzgNB1xLfCWXQvjbg7sETWlA2YeZMA22HUqoNlanZAoAsiG141vSojAw9OVJTM7t4yNyn4q4SwJQOfCgIfTNxiVatN8Bq8I9F5I=', start_index=20628)
Annotation(end_index=20663, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9QXX8IkOW_MSeVNzLFSMiszsn_6tB1eXzTr-JsxBU4C3rmdV63QeA2F40KsBKwRhDPzUdwr0JDVMSH99iKGuaeQESAzGnraODubFjv-mMfMboeqqkxWxDCehkGlP_WySoRysc0A9uatW2QL7DpHPBWDg_huUsdWHR5NLdNWcavipoqmM=', start_index=20653)
Annotation(end_index=20695, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjk0ElEzTVlyV0uiz9sprFKupnLJnHuGvlxraRHrK1U0yXsnkFX8sA4NLTA1g9gpEl2CeqyRgoJrtZeZoVyYh3NxvFHQVFSr6IjHH4bBnDylW0ALa5-xL2p-n5UX7FBNfjnp5jDCr4gQ==', start_index=20685)
Annotation(end_index=20718, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEps-KZ4G6riaE2l8sgQVITXuIIGgFvxoEcboedRpJXzcrtOO3iyHon6CNiKuoaOzKQFh_umkAqio2lzUxFcLgC1PBLaews_Du49RzooSS3h8UCI7zozXve16HvMlAx3IlLoDef4mmWgFHAGx1O38J6a_SASGrkvJ8E7LttBf7tLms-LXTkj29N4Od57OUePp8fvUiEqbIp92-okdq-hvI=', start_index=20708)
Annotation(end_index=20752, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHa5Z2yPjDSc-9RXhxJMJAUcMt4q4fRoikKxTQHbumtep6aREV7Z7MljfbKznXNBdp-9DRBSZ32rJMuOz2ME7uYtfTDiqBzlS63MTj0f1kAjt8Z0Zyc16_WM6WeBb6UKzQYKM802yzDHTdRdi_9x6uK8_7bR7Vo4Q0l6shDSIWqKZ6j6Lb46RsvrrymsZfTzlO4i6Noi08Cs4=', start_index=20742)
Annotation(end_index=20786, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbz8glrkGtw1ezFeRwsT6OIzFTY5HkhuXypobqdw0lSrku4rbCXau4PkSQkzhturuIYYBtugRCWEJLQNnCGKaq-UgHF-94BANSJ5CLEwTuPd2lm--CUVhPTJWQID8__Q==', start_index=20776)
Annotation(end_index=20826, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkuVcbM5N95U27PDanbKHsU-ffWs-TltNvNSa3KSDFlncI2MhtRUoF9bQrhqRVB7se7gauQ8WpXQImOi4ZCaE_YM0V0j-56xzs-Q9Vwc3g72_tyLTxfrKGfhrj_vvNhbSmf3LbY-VE7IMpJeWXYVsAPCw3txmGD_IO8XP7XgDKwwat6XQqdkifn3OKkkLZX_5gIWZaarswas9f5arEpcZNrwAkKJs2puvf2_doJkcYVB-PWCf17dazfVYqv3zb4xzKS1PN4VE86JC7YBxiO5Ljd84wArguar6ezncGqi_DWjLUbBrD5qqTo3y-LixjHwZ7yUoHMvlV9-lFryx3jov35qhr2xTcRNR4dw==', start_index=20816)
Annotation(end_index=20860, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1ptghs36j-F3IFBVISZzT3cOcnKvADk3B9m-3chTfRpJsrxfLMEyIuqaYDy_6nOAIH1WCOTTCfXFKTBcq5q1ehgqE1jT6wlTINZ1_QxyferXcZ3xhpndfKFXqPc2w8MubU7KJPnV23Q==', start_index=20850)
Annotation(end_index=20883, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGo3rEsx5h5ONgbjzXmJHUwA2nApBQ0qZ_-7soyIhEiAMymlHMOpwEZxpTXjnPclvd-Vn7hO7wB993nXOnOoc8v5yqJXtjw8qDr1wtOpMUtjac4-vX2NgCuOePJVIQCGRARBSC', start_index=20873)

## Sources
