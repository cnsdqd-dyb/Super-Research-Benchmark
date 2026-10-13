# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** d090fa09 | **Time:** 343.43s | **Cost:** $1.77839
--------------------------------------------------------------------------------

# Factors Balancing Treatment Response Prediction Against Myelosuppression Thresholds in Molecularly Subtyped Chemotherapy Selection

### Key Points
*   **Tumor Molecular Subtype Dictates Regimen Intensity:** Aggressive subtypes, such as Triple-Negative Breast Cancer (TNBC) and Uterine Leiomyosarcoma (uLMS), often require high-intensity regimens (e.g., dose-dense anthracyclines or doxorubicin-trabectedin combinations) to achieve pathological complete response (pCR) or survival benefits. In these cases, the threshold for tolerating myelosuppression is higher, necessitating aggressive supportive care (G-CSF) rather than dose reductions.
*   **Pharmacogenomics Modulates the Therapeutic Window:** Germline variations in *DPYD* (fluoropyrimidines) and *UGT1A1* (irinotecan) are critical independent factors. Even if a tumor subtype is highly sensitive to a specific agent, the presence of these variants necessitates preemptive dose reductions (e.g., 50%) to prevent life-threatening myelosuppression, fundamentally altering the risk-benefit calculus.
*   **Relative Dose Intensity (RDI) is Subtype-Dependent:** Evidence suggests that maintaining an RDI >85% is critical for survival in TNBC and HER2+ breast cancers, whereas the impact of dose intensity may be less pronounced in other contexts. This dictates that myelosuppression in these subtypes must be managed with growth factors rather than dose delays to preserve curative intent.
*   **Novel Myelopreservation Strategies Exploit Molecular Vulnerabilities:** The use of trilaciclib in Small Cell Lung Cancer (SCLC) represents a paradigm shift where the molecular feature of the tumor (RB1 deficiency) allows for the selective protection of hematopoietic stem cells (which are RB1-intact and CDK4/6-dependent) without protecting the tumor, effectively decoupling efficacy from toxicity.
*   **Clinical Biomarkers Refine Risk Prediction:** Beyond molecular features, host factors such as pretreatment albumin levels, BMI, and age serve as robust predictors of myelosuppression severity. These factors are increasingly integrated into machine learning nomograms to personalize the balance between aggressive therapy and safety thresholds.

---

## 1. Introduction

The selection of chemotherapy regimens in modern oncology is increasingly driven by a dual mandate: maximizing antineoplastic efficacy based on tumor molecular characteristics while minimizing dose-limiting toxicities, of which myelosuppression is the most prevalent and clinically significant. Chemotherapy-induced myelosuppression (CIM)—manifesting as neutropenia, anemia, and thrombocytopenia—remains a primary cause of dose reductions, treatment delays, and discontinuation, all of which can compromise survival outcomes in curative settings [cite: 1, 2].

The "balance" referenced in this report refers to the clinical decision-making process that weighs the predicted chemosensitivity of a specific tumor molecular subtype against the patient's physiological reserve and genetic predisposition to hematologic toxicity. This calculation has evolved from empirical dosing based on Body Surface Area (BSA) to a precision medicine approach integrating somatic tumor profiling (e.g., HER2 status, RB1 loss) and germline pharmacogenomics (e.g., *DPYD*, *UGT1A1*) [cite: 1, 3].

This report examines the multifactorial framework used to align treatment response predictions with myelosuppression thresholds. It explores how molecular subtyping informs the necessity of dose intensity, how pharmacogenomic testing adjusts the safety ceiling, and how emerging predictive models and myelopreservation strategies are reshaping the therapeutic index.

---

## 2. Tumor Molecular Subtypes and Regimen Selection

The molecular classification of tumors serves as the primary determinant of the chemotherapy regimen's composition and required intensity. The intrinsic sensitivity of specific subtypes to cytotoxic agents dictates the "acceptable" level of myelosuppression risk clinicians are willing to accept.

### 2.1 Breast Cancer Subtypes and Relative Dose Intensity (RDI)
In breast cancer, molecular subtyping via immunohistochemistry (ER, PR, HER2) and genomic assays (e.g., Oncotype DX, MammaPrint) fundamentally stratifies the need for chemotherapy and the requisite dose intensity.

*   **Triple-Negative (TNBC) and HER2-Positive Breast Cancer:** These subtypes are characterized by high proliferation rates and genomic instability, making them highly chemosensitive but also requiring high Relative Dose Intensity (RDI) for optimal outcomes. Research indicates that maintaining an RDI of $\ge 85\%$ is significantly associated with better disease-free survival (DFS) and overall survival (OS) in these subtypes [cite: 4, 5]. Consequently, the management of myelosuppression in these patients prioritizes the use of Granulocyte Colony-Stimulating Factors (G-CSF) to maintain schedule and dose, rather than reducing chemotherapy intensity [cite: 6, 7].
*   **Luminal A (ER+/HER2-):** In contrast, Luminal A tumors often show lower sensitivity to cytotoxic chemotherapy. Genomic profiling (e.g., Recurrence Score) is used to predict whether chemotherapy offers any benefit over endocrine therapy alone. For patients with low recurrence scores, chemotherapy can be omitted entirely, thereby avoiding myelosuppression risks without compromising survival [cite: 8]. When chemotherapy is indicated, the correlation between high RDI and survival is less consistent than in TNBC, potentially allowing for more flexible management of hematologic toxicity [cite: 4].

### 2.2 Sarcoma Subtypes: Uterine vs. Soft Tissue Leiomyosarcoma
The distinction between Uterine Leiomyosarcoma (uLMS) and Soft Tissue Leiomyosarcoma (stLMS) illustrates how histological and molecular origin influences regimen selection and toxicity tolerance.

*   **Efficacy vs. Toxicity Trade-off:** The LMS-04 phase III trial demonstrated that the combination of doxorubicin and trabectedin significantly improved progression-free survival (PFS) and overall survival (OS) compared to doxorubicin alone in metastatic LMS [cite: 9, 10]. However, this combination resulted in significantly higher rates of Grade 3-4 myelosuppression (neutropenia: 80% vs. 13%; thrombocytopenia: 47% vs. 0%) [cite: 9].
*   **Subtype-Specific Response:** uLMS patients often exhibit higher response rates to this combination compared to stLMS, despite uLMS generally having a worse prognosis [cite: 9, 11]. Consequently, for a patient with uLMS (a molecularly distinct aggressive entity), the severe myelosuppression associated with the combination regimen is often deemed an acceptable trade-off for the significant survival advantage, whereas in less responsive subtypes, the toxicity might outweigh the benefit.

### 2.3 Small Cell Lung Cancer (SCLC) and RB1 Deficiency
SCLC is characterized by the universal loss of *RB1* function, a molecular feature that drives rapid cell cycling and high chemosensitivity but also distinct vulnerabilities.
*   **The RB1 Paradigm:** Because SCLC tumors are *RB1*-deficient, they replicate independently of CDK4/6 activity. In contrast, hematopoietic stem and progenitor cells (HSPCs) are *RB1*-intact and require CDK4/6 for cell cycle progression. This molecular divergence allows for the use of CDK4/6 inhibitors (e.g., trilaciclib) to induce transient G1 arrest in HSPCs (myelopreservation) without protecting the tumor cells [cite: 12, 13]. This represents a molecularly rationalized strategy to decouple treatment response from myelosuppression thresholds.

---

## 3. Pharmacogenomics: The Germline-Somatic Interface

While tumor molecular subtyping predicts *efficacy*, germline pharmacogenomics predicts *toxicity*. The balance between these two factors is critical when selecting dosing strategies for standard chemotherapy backbones.

### 3.1 DPYD Variants and Fluoropyrimidines
Fluoropyrimidines (5-FU, capecitabine) are foundational in the treatment of colorectal, gastric, and breast cancers. The enzyme dihydropyrimidine dehydrogenase (DPD), encoded by *DPYD*, is responsible for catabolizing >80% of administered 5-FU.
*   **Toxicity Thresholds:** Patients carrying decreased-function *DPYD* variants (e.g., *2A, *13, c.2846A>T) are at significantly elevated risk for severe, potentially fatal myelosuppression and mucositis [cite: 3, 14].
*   **Balancing Prediction:** Clinical Pharmacogenetics Implementation Consortium (CPIC) guidelines recommend a 50% dose reduction for intermediate metabolizers [cite: 15, 16]. This adjustment balances the prediction of severe toxicity against the need for therapeutic exposure. Studies show that genotype-guided dose reductions do not compromise survival outcomes, suggesting that "standard" doses in these patients represent overdosing relative to their metabolic capacity [cite: 17, 18].

### 3.2 UGT1A1 and Irinotecan
Irinotecan, used extensively in colorectal cancer (often in combination with 5-FU), causes neutropenia and diarrhea. The active metabolite SN-38 is glucuronidated by UGT1A1.
*   **Variant Impact:** The *UGT1A1* *28/*28 genotype (Gilbert's syndrome) results in reduced glucuronidation and increased exposure to SN-38, leading to higher rates of Grade 3-4 neutropenia [cite: 18, 19].
*   **Regimen Selection:** In patients known to be homozygous for *UGT1A1* *28, clinicians may modify the starting dose of irinotecan or select alternative regimens if the risk of myelosuppression (e.g., in an elderly, frail patient) outweighs the marginal benefit of full-dose therapy [cite: 3, 18].

---

## 4. Relative Dose Intensity (RDI) and Survival Correlations

The concept of Relative Dose Intensity (RDI)—the ratio of the delivered dose intensity to the standard planned dose intensity—is a central factor in balancing efficacy and toxicity. The "threshold" for myelosuppression management is often dictated by the RDI required to maintain curative potential.

### 4.1 The 85% Threshold
Retrospective and prospective analyses consistently identify 85% RDI as a critical threshold for survival in adjuvant breast cancer settings.
*   **Subtype Specificity:** The impact of RDI is most pronounced in hormone receptor-negative (TNBC) and HER2-positive tumors. In these subtypes, RDI <85% is associated with significantly inferior overall survival [cite: 4, 5].
*   **Clinical Implication:** For these molecular subtypes, the occurrence of myelosuppression should trigger supportive care interventions (e.g., secondary G-CSF prophylaxis) rather than dose reductions. In contrast, for subtypes with less dependence on dose intensity, or in palliative settings, dose delays or reductions may be an appropriate strategy to manage toxicity thresholds [cite: 4, 20].

### 4.2 Dose-Dense Regimens
Dose-dense chemotherapy (e.g., biweekly administration) increases RDI by shortening the interval between cycles. This approach exploits the Norton-Simon hypothesis of minimizing tumor regrowth between cycles.
*   **Balancing Act:** Dose-dense regimens improve survival in high-risk breast cancer but are inherently more myelosuppressive [cite: 6, 21]. The balance is achieved through the mandatory use of G-CSF support. Here, the prediction of high treatment response justifies the deliberate induction of myelosuppression risk, which is then mitigated pharmacologically [cite: 7, 22].

---

## 5. Predictive Models and Clinical Risk Factors

Beyond molecular and genetic markers, clinical variables are essential for predicting which patients will exceed myelosuppression thresholds. These factors are increasingly integrated into multivariable nomograms.

### 5.1 Clinical Biomarkers
*   **Albumin:** Pretreatment serum albumin is a robust independent predictor of myelosuppression. Hypoalbuminemia correlates with altered drug distribution and reduced physiological reserve. In colorectal cancer patients, low albumin significantly increases the odds of severe chemotherapy-induced myelosuppression (CIM) [cite: 23, 24].
*   **Body Mass Index (BMI):** Both low and high BMI can influence toxicity. Low BMI often indicates frailty and poor nutritional status, increasing CIM risk. Conversely, dosing based on actual body weight in obese patients can lead to overdosing if not capped, although current guidelines generally recommend full weight-based dosing to avoid under-treatment [cite: 1, 25, 26].
*   **Age:** Advanced age (>65) is a consistent risk factor for severe neutropenia due to reduced bone marrow cellularity and renal clearance. This factor often triggers primary G-CSF prophylaxis in intermediate-risk regimens [cite: 27, 28].

### 5.2 Machine Learning Nomograms
Recent studies have developed machine learning-based nomograms (e.g., using XGBoost or logistic regression) that integrate tumor location, chemotherapy regimen (e.g., oxaliplatin vs. irinotecan based), and clinical factors (age, albumin, lymphocyte count) to predict the probability of Grade 3-4 myelosuppression [cite: 2, 23]. These tools allow clinicians to calculate a personalized risk score. If the predicted risk exceeds a certain threshold (e.g., >20%), the regimen may be modified, or prophylactic growth factors initiated [cite: 20].

---

## 6. Myelopreservation: Decoupling Toxicity from Efficacy

The development of agents that selectively protect the bone marrow represents a novel method to balance treatment intensity against myelosuppression thresholds.

### 6.1 Trilaciclib in SCLC
Trilaciclib is a first-in-class CDK4/6 inhibitor approved for use prior to platinum/etoposide or topotecan in extensive-stage SCLC.
*   **Mechanism:** It induces transient G1 arrest in HSPCs. Since SCLC is *RB1*-null, the tumor cells do not require CDK4/6 for replication and continue to cycle, remaining vulnerable to chemotherapy. HSPCs, being *RB1*-wildtype, are arrested and protected from cytotoxicity [cite: 12, 29].
*   **Outcome:** Clinical trials demonstrated that trilaciclib significantly reduced the duration of severe neutropenia and the need for G-CSF and transfusions, without compromising antitumor efficacy [cite: 12, 13]. This allows patients to receive full-dose chemotherapy on schedule, maintaining RDI while staying below critical myelosuppression thresholds.

---

## 7. Clinical Guidelines and Decision Frameworks

Professional guidelines (ASCO, NCCN, ESMO) provide the structural framework for balancing these factors.

### 7.1 Curative vs. Palliative Intent
The threshold for acceptable myelosuppression varies by intent.
*   **Curative Setting:** In adjuvant therapy for high-risk subtypes (e.g., TNBC, uLMS), the goal is eradication of micrometastases. Guidelines prioritize maintaining dose intensity. Severe myelosuppression is managed aggressively with G-CSF to prevent dose reductions that could compromise cure rates [cite: 20, 30].
*   **Palliative Setting:** In metastatic disease (where cure is not possible), the goal is life extension and symptom control. If myelosuppression impacts quality of life, dose reductions or delays are standard, as the marginal survival benefit of high dose intensity is often outweighed by toxicity [cite: 1, 31].

### 7.2 Neutropenia Thresholds
Standard guidelines define neutropenia thresholds for treatment modification:
*   **Absolute Neutrophil Count (ANC):** Typically, chemotherapy is withheld if ANC < 1.5 x 10^9/L.
*   **Febrile Neutropenia (FN):** The occurrence of FN (fever + ANC < 0.5) is a critical event. If a patient experiences FN, secondary prophylaxis with G-CSF is recommended for subsequent cycles. If FN recurs despite G-CSF, dose reduction is mandated [cite: 20, 32].

---

## 8. Conclusion

The selection of chemotherapy regimens involves a complex, multi-dimensional trade-off between the predicted magnitude of tumor response and the patient's specific threshold for myelosuppression. This balance is no longer static but is dynamically adjusted based on:

1.  **Tumor Molecular Subtype:** Determining the necessity of high Relative Dose Intensity (e.g., TNBC, uLMS) versus the potential for de-escalation (e.g., Luminal A).
2.  **Pharmacogenomic Profile:** Identifying *DPYD* or *UGT1A1* variants that mandate dose reductions to prevent predictable, severe toxicity.
3.  **Host Clinical Factors:** Utilizing albumin, BMI, and age to stratify risk via predictive nomograms.
4.  **Availability of Myelopreservation:** Leveraging molecular differences (e.g., *RB1* status) to use protective agents like trilaciclib.

Ultimately, the goal is to tailor the therapeutic index such that the chemotherapy dose is sufficient to exploit the tumor's molecular vulnerabilities while remaining within the safety margins defined by the patient's genomic and physiological hematopoietic reserve.

---

### References
[cite: 1] Wikipedia. Chemotherapy.
[cite: 2] PMC12635783. Colorectal cancer is a common digestive malignancy...
[cite: 33] ResearchGate. Molecular Subtypes and Tumor Response to Neoadjuvant Chemotherapy...
[cite: 9] MDPI. Leiomyosarcoma (LMS) is broadly classified into uterine...
[cite: 8] PMC11818289. Therefore, a better understanding of tumor biology...
[cite: 3] PMC8796462. DPYD and UGT1A1 Pharmacogenetic Testing...
[cite: 34] ResearchGate. DPYD and UGT1A1 Pharmacogenetic Testing...
[cite: 18] Diatech Pharmacogenetics. UGT1A1 & DPYD: Safer chemotherapy starts with genotyping.
[cite: 35] PMC12352563. To determine the feasibility and effectiveness of implementing pretreatment DPYD/UGT1A1 testing...
[cite: 17] Pharmacy Times. DPYD Testing Gains Ground: NCCN Guideline Update...
[cite: 2] PMC12635783. Among ten machine learning algorithms, extreme gradient boosting...
[cite: 9] MDPI. Due to the absence of head-to-head randomized trials...
[cite: 23] ResearchGate. Risk Prediction of Myelosuppression Following First-line Chemotherapy...
[cite: 36] PMC11786037. Colorectal cancer (CRC) is a leading cause of cancer-related deaths...
[cite: 20] Cancer Care Ontario. Prevention and Outpatient Management of Febrile Neutropenia 2021.
[cite: 30] Medscape. Prophylactic therapy recommendations in the NCCN guidelines...
[cite: 6] CancerConnect. Dose Dense & Intensive Chemotherapy Improves Survival...
[cite: 7] Cancer Network. Benefit of Dose-Dense Chemo in High-Risk Breast Cancer...
[cite: 37] PMC10665989. In conclusion, patients with HR+ and Her2- BC were revealed...
[cite: 12] ASCO Post. Trilaciclib to Reduce Chemotherapy-Induced Bone Marrow Suppression...
[cite: 29] OncLive. Trilaciclib Prior to Myelosuppressive Chemo Reduces Need for Supportive Care...
[cite: 4] PMC6190707. Higher RDI of chemotherapy is associated with better survival...
[cite: 13] PMC6857609. SCLC was chosen as the first clinical setting...
[cite: 24] PMC12537429. Establishing this simple and cost-effective predictive biomarker...
[cite: 10] NEJM. The addition of trabectedin to doxorubicin...
[cite: 14] MJA. Patients who carry functional gene variants...
[cite: 19] Oncotarget. ESMO consensus guidelines for the management of patients...
[cite: 5] PMC12607806. Triple-negative breast cancer (TNBC) is an aggressive disease...
[cite: 15] CPIC. Guideline for Fluoropyrimidines and DPYD.
[cite: 16] PharmGKB. Clinical Pharmacogenetics Implementation Consortium Guidelines...
[cite: 11] PMC8446791. New associations have been tested with and without doxorubicin...

**Sources:**
1. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlgBqyd7HoeA_tH4WyHNke0PlCgxoPBrO1LnVPKF_tH_A-YxQfqCBF8d9jXKm8h-eqBsF6UL1oXnmBJd2pzfbvqGXBd-2cfngYCPK2Lm1zrjHb6-4VTuMQU5Ed8DEoKGM=)
2. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnC3b5XaNELUrCIPtJxV73HEFCl-eU4C6w7GfVtFJ4-Hd2cepsFjShOg4j7HUR6VjzWn-tkyB3zVw1uLkjte3mouX-lYA7WU23w3BV7mJNiet-AmFOo3KQT3xcD1Y3SryTCvaXUXyahA==)
3. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElODk0JWyhftHXU9wO2QZiM5LAXh9_0ApSKrpvWenulaMIndKM_sjgfdvF-LXvXghkM7CVGe7FAgD7gZJwIzR0pFodnOyqqNz2p0tBC7yZzuKAcb592xRpknWUaWcdMDk_MZSNDQiD)
4. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZnqaOFItCJLAouyMDfZUin6xtUXcbSJYtoPcPTFtqhkTrCWRO7XxtlMlUXNx5rxqZC3zEsQGmtCmwZUMEI7XhPMd-mWMYCKkyfgqeqf2ojcBye8IwyWqJYw8Lid9U338SBrGzlr-g)
5. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQt6Z_1v1Y44RIT6AmSQlKYlo_ENBBBuw3IxM4mtkU3Xj0fhKOvOEWnrQkGVnlU-vpvEbgz9M6Jc7ZQ82Yp_Uph2-joDju32oZapacL3KwnBy9FPFNpbteDnJssZkNCufhaYA-7xoDxA==)
6. [cancerconnect.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiIziB8k3glCq9DAbSRIKfdQ6QObtJClrR8rdLXo0Fw4vME_H8lVpD68QKOdz9SewjkSXt-whq3dRZV1hLFu5iM_A_Y1HK97_XMva5l_xWKM5uSh8HeED1V_Xl_yRa58G8yEsKGXRUqDp-1l_nqtj7IohXKWthqicPtqGZV4AiDyZUhvF4z_HmrCJ2coaFfWzOLn6uCoKjck7moF5Rgdpy-db2u8Y-)
7. [cancernetwork.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaoBy6NO-Lk5M65LEDdgGZusG0JcD5V4QM4ybCvjOOyrgTVq9T7T6ywjLa6vf-tWjFbHy7Xw7ZdGZUe973Cw5btahf0Sz3XxlbX-tmo7wMcL3qS9PK4UBNMcOhcG8wi0k0GOj3q-CpPwOe536YVq4b2ZOmfiJCa4GSxHRk6Kkw8QX66jEA-wwL67vm4qMp-vphoI4BIP0CYfNI)
8. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxX-4gBAnYdQTy45Ah1ioDoibuPPvwEdxPkLBHZIAhTPI4qx4R31A0QNfjAsUAtTpVQSKkYcHfKYyuUp4TPGfPwzg9hS4mPPEoG9z_p2Dvl5HIYbOtVh7IWe_MxdFM37CmqTMTc9qw_A==)
9. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZujCVEdvx8G_7ReZ23KQbQhWHXdJsUSgUOifHGyohLQqY8YMN1ZgcRv6Mnlp9JwH4y17QVUz0mll3xOqOzPKzhPnWbZG_HuHtERn6-TSGzKDJjcSAN_H4YuX0IE8=)
10. [unicancer.fr](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnlkL4NYiQcERZqCePEbTiJ23Md1udspeQ-wzGD5pDKoS4OxRpGUQxuEWIEIFT9JDpMdo_YMX0IxEAoWmE1pptGnDT5MF_oqeNG86_I0bsi8OTX7FgA2w9CiGT5ZPOoESkGGfRXKkI7iIcmlGHzoVLUxMBvP76pcS_BYZ8TT5v2Gdgoddzc4pJuJZXYSev0NG0_h5j71psBbEISSf-LuV4VJj1pc-eEP8HE178zUYvpYHDZgYz)
11. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDQwmJ3xbdmB2Nj26PLbYpOqJMi6AP1V8tzn-wysy2c8fwj2htFViQUHG1PsVPeGjx0yPlEIGs-XWu0vvZCW6qz0T5XrPLYvEOj3fw2crqhquGIhCysJOmlL300YX0GmAV4rFgE7sQ)
12. [ascopost.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFnUERbr9B4q3nxgyYyD2NgPcMo5r0plNe7yX3rkPG2PcMYAHsu1Kihdhw24ksiqahSWJMgn5g-RywhQ4wyJgKfB7EwRU9dzcmdzRCJpT0RN51NBFXJgtpX0Gjpweh-Hq3Z9dHnxU0iW2vSxyRyE30MfwE9l4Svswt2y5y2TvsPpxW7Nd7QfZ-RvFrJI5XONto8iJpasbNIZJby1YDOwa3Hm6igUKoFftA7GhBU_VaKxGu2md0e2eMDrseZwj0Rlfp0FincJKatZpCEIrlbOI=)
13. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPIa8gcFvyngyBf5-UodneqXVlQIHHC2_lHl4GDyZtIPArU225-j3A3oqLIbRSu93X0IdaXFf4oPITPl8MWMjBqJinqBWCh6w8uKx13yLfVdDllSmNbAMQAUGkO1-87kcBl224SaDN)
14. [mja.com.au](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbtSI8cE__uJ2cRyXCrETQDGIOJnsoLn-xyUhFfka6Wwze6HRFIpZ1xI-QG_IH2IRemVs7Fz1xTDnqDJ7Y9Be3bym-rez4ZYREdWktcfz_wvPWFbb3eblSIjIW0eYrwsu8uvSi5pXsLn4mF92NtSNLbCO7cIf-_kk=)
15. [cpicpgx.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF67ruMJJZRlUGcnRniGKnEoi-BuYFAYT-HIdWapaRYk2IhstnNZa0QVdqLZ_caRtTdQfiLlfL_uAfIieMsAicvALXt4fssJ9VS1xcx7F2TftG_W5pB5ZhnAiHrfNfjHGxj5Q13aRDZRbWv3_0o247b6NKIRXFE355ZecgIoGQ=)
16. [clinpgx.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-7gjGmr-aLcvF4x8rpJK2ZFMQdZJ2k22FacxW-0E8ODJPP6XE6caLUyplkcybNLW6emRvVJJa1_4xFH-YKedMfp4_1Zb6Vv6WxrperRZxhD8B8AzYdKcx-KbDc6PmKReclJY5d2nE5ctLK_vW)
17. [pharmacytimes.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAxmqPU-DOQdlBfh74hKiuUWp-KJtVeg6IgLkIhkItH7vI8HaI5vt9TwL_T4uo_A4y6Mb83X68LDurSd4x6mZHSyAddAnM7HIkCpPzAeu-6ydZZh2R9Cn3W49rP_kEneMuQQoeEFqNWgCLcWUYRlxuBJ_DXtXIUKUKZDW-QP-vwzvn1bRuNtvTnkiJmvUODxt2YO8jGMYZTufVCJX7cMFNwpRAZnmvN1_DijvZtNEO8ca-dtZv4Ak5FY9A4w==)
18. [diatechpharmacogenetics.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlBcrgn1RYniGyNYOKx3tg9Da9EuWfdW_ptEsndOGt_5lMyQwcgs8wCbECraRFw3bAK7J3KcHt0JnizndZyq5dbOCtKwkBq2PnWaKgJZdu_SngSjGZiRQKR5dhi_r_hlP4_yNlFohNTCHAYl4QnvZ9Sk1qODKD7vwShzaFYke2MShz_asMj1OotV7saozm7GLCccPsLCKeAxvqAYPb0J8QSwo-QA==)
19. [oncotarget.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_HZLxaGBx-sI5QvNrqs6swRtlzHYHYuF4FfK053nYfGdLcfdJ60mOOBAxvoGzz8eJreSuCosUPE-MyaY0romTpuG4G4sUD8BpW-9vzvr8_mynNlXLNmc4jH-iwrEo5KGNacuv)
20. [cancercareontario.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGv_D0KTxZnL34oLfwn4D3rvKORumJqg9_OLJj9n_8zjj0DyoP_3nF6IQ3QbKRgeBsxHqRS9szD4R84xIp5yw0LYPsFvviOAwAV3GmUZkLEpqFZ8MkrIUSSQxEk293rsrGdh_toEacUTJQeSDYhz1LRC4CjKBA4vzJCuaP0)
21. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxPSjhvCoZsT_V6acTTaOYRzCDL4HY1xYKcGIUHci9-KYVjjss2LEVOriFYS3JRX9XW6TeH9qwhSqjBk2K8HWd7hjdNUjCiy92hEMM9DLRXUwLzuiSjZwjr4PWmMHGOPhsPjAON7qR)
22. [the-hospitalist.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEumtMf5CIBEe_kiGxrADpbgt-WVCI24UB6SF1awsSP5F6fC6ro49upJ07CLTECRzvK4IhaKRKAJbkyy-at-R0Gpyw3GT-jLHtad9H5PhUMpYB0CVsrbsy5GPZSmLosxKSME2qUPi5SmlLXzmoO5zlCiT98fuK0SdQQ0yMB4phYghV35FRfWsdfitUxem-pSHG9xKls3hY=)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1O2iN2qdKDpDb8PTu5VnA5sav5MMeLR5vge1K9e8CePvWSQKneYj0qnMx0bGakHxJw2xojEDaRET58eer8zwJZNsfoSK_VyEoPLxREuA4P7bu8AlsCAgcSGq8WU3vH-xILaTH4ru0HOWLMPa8zJKXHNEfoXUFHstmXqknv4dbxkfups2lsgmrnxEWRusZo8hAt6cp8PfSp7XkZcd3zcEGQzBkOIR3JapccSvxeptVN8QCPWFG9b4aZLQRMCbCMufpHbeI)
24. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzJWu8moK5DZ32cNPfsZPNCizU7PqLyko81uebaRPQZ3vniIMzs9weFKhRljggnx4XQqxdY1QDDPonYTh9wYA9lCWZFyuHfS45HvxOH8cr_RIXU_q-rZu4TyD0IzA5KaKkzQMdNo9tmQ==)
25. [e-century.us](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdk9fRYpFJKOs8mbFpi6TLJjf-mAqwlDSz9C1QNMRMvZlrVtdNERbOQYcz3ePjsEhWFJ1GtI7lnDp1o_haJuVViNjyf2JMIaITA9b_OrrtG9_kg9sMP2BlCryuP4uI8WkCSCCyw4p_WFuc)
26. [foxchase.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0qCgdjAu-GmPhRuVK796NJo1mENtzZSstseTd-CCE8t-Ba6EWFFZ56R-iTdqDMocxWARRExgCviXyTs6wTRlpmbEKDpu6WA7dm5bINquKRBF_GrrecGD-_awdgKIPcINDJYrQ-l0KArySpzrVD2cJx7MjtmxVPkvS_hsAFvvvRElPa-SBs1VYxxSlOa2ylmr7QZVxawOYLNEAx-A78Bk_fRckEYID8mSeQZ7Yug3ognf14v245ENTGWaQwJEn9zE=)
27. [magonlinelibrary.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwXhmcoluyt0z4Sjqi2M2ZjTwLlEJGpn-TY3DL0dQNMlwkuw2bn40oCzvcJ6AT_cx71pSCNGDoOS8cRqLwZ__sMGyCYr5Q136L5WKnYoPzjdNogwn1PckE1ITJJAHdnfRAOH6foFj35QaN8Y77uyAZcEk=)
28. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGi4d4dlMpl72Y5ClgPxQbcj22n2-5HRp-VL0ilI5bWJ3JR9WJhhVwlT4KiOYWbmnlsmZ0Cu3HXeQyvwEaRvIBnut5gOp1YE6pF_g4kJbAGbC_iVenemA39bMADRhWpqcVrY3EMcV5GFkDNwTt2ooR0rYNxOt-1lh1CE_dyJHMc_Blx3L1ULmw7ZtntVCkGw63Dxe2ciNCNE6WKfomDjR86q6UI20GVXlejUKYPsuitUuVeOALhK3Y-QrgUiAl7HB0=)
29. [onclive.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTB1VkCHF9k_7UNZeuQeeQd3WBRKhzvimUQe9Mqp-Z-U0ZTm97w2_KP9ES2ImKPTWfIfe-5T8BFJt_STKuUP0l5StSPVBVuDChO-G_OIFHB0DAYTUMs0NiaS14PtD1CAyV23fOfk74JIZwdtjq0gm6uoMAlKwCcDszzj8FlRB35sSIpK6zax8cNyX8zuXbv9CPnFMWWpFO7rBhc08ZxUxbq8D4h7dgceAKcDx3qEtM8GhEs-QSnF4HScU=)
30. [medscape.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNkPjeTs5ZteYnsmOrvEeXOkw_vtzdr-d14pxCq_yFW3Ad1Vsnq2HD61KbESIo0qTN4d3SBk01fzVBDQ7Fzlr2PFGsoTS-fFS0fCB-oMBmiFGd4cp1rUDQJ2TnPNlzwXoBtgDeKfGYUGlD08bD)
31. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHELPXXMN0lXIkRLIhewlxNTmrhu2mfgsu1zD0sZjADN1WqC0bA4OZxh0ZIUICgEuIt4zRJXGyFb0yH7ULk9d_MvX9ayoKnThzrl5lt0ZtGECkYjQWBU1Csx0nH00WztYvsJ3lQ5brQ)
32. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUu41Q7LlwSf9ezZX8I4FoTT8CktIb1n8-Tj64GLCx_f6gRXEIRXkvnXLQKYKGdRRmDTnW7z9A6ebnY-R7_5lJ7YV86AjD0Z17eKSHGHJ8Ai3fRGk36rMjQarLS5JsqdC8NbSlegwQ)
33. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0uLCrdwCcxCzk69dDReJ4KnLWG4WrlUO12xodsAq_kIbfuP2Ge2qv1GFfr0Q32w_UIDaYH7U6bauCjKbTKFh75FJZ_xE0K-Kmw4m6adXp7hQtGKi0e1XWEntfBPuRTZbOTpAur9kCzyvnR0xvcxlM_Pb64U1B0EM1JIi4Xu7m9FNh30dIa3j3vMBieqFi-Ce1WyNi2HnLTwpNtc7FaXa78n68Bukw7U5Q2T8kdBljzkyJ3QPuT7b4wo3vwZA_OiTnw09pPaR9EPf3KWK4cCh2AB_tNucNLHNVMg==)
34. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTrK2woy9ekdBXd8AyAHOEDrTGgqHv6egdaSjrZmHrILak3gPgiuufZiOrDayPq3Mu8GFyfpUqxCU-4ajNHkJdi3T5ZF3VlTY8v4JdRqe-HmWusploaf4sDgnEcWC4qeA5gYnN4sLyFNOaIT39ue4aMmF5jZBUKrjrYm8OMhiRyu8IDNKIIQ435l3TOwhrECdn1PJ42keIbNkehbFBbLXZ4BwUxD7tMEHL1yV2NbbYxW9BKzgr8hhoynbd0_7QsZbm8bde_FnEjaNIJBg9t-mWWMRt7p2TuuvQ4h4IeTCfhTSuoveSMUve3PO8z6r5rNjeeQhNBTo27Hp2W69QGtP1RtOiLqLqdP2xdow=)
35. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkoF3tzMEEgCEi2sszKMqEJhRkmwAAmVUqBmtnii8B9NxXW7VkzErSEVcj6NtwzHcwqMqiB4NIr3bqvZdRm_iMheV31opSod6dZ2P8JiSGdk9iI2YsgpPeNa37V0YLp2XXvFE-huA2Gg==)
36. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSBdY1vRTM1F_cUvieBYgqszMJL-3c_MglTqYEdSMkzo0PctqeHxZeKg_QsfH1H1DXEDbDTWrIKvZHsStDJzU94mQURA-sRAkvaAhf-O0UOqNPwHK9sXiy4x6iCvCErPcNhglHfhGkwg==)
37. [windows.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFH6q1wi336OImpOPiC1tSCCwQXtcf7JYq2OX0yKVxmQ-i7aKs3TDYXPAFw6SD5oAcEGJCwPzur7mip3k2ph6KqpoFgnXVbvQOwJTlTWhh3QDD5yXkpUOyLk_-h5ILMwB21z-NhmqSXA7XVee9pfkRFhg8jAJn14A8ImG5uDX4UZ6twyZz7fPIBg7SIFO28DVZK_RSVoHLOQnY1J77lbe2x)


## Annotations
Annotation(end_index=2787, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnC3b5XaNELUrCIPtJxV73HEFCl-eU4C6w7GfVtFJ4-Hd2cepsFjShOg4j7HUR6VjzWn-tkyB3zVw1uLkjte3mouX-lYA7WU23w3BV7mJNiet-AmFOo3KQT3xcD1Y3SryTCvaXUXyahA==', start_index=2775)
Annotation(end_index=2787, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlgBqyd7HoeA_tH4WyHNke0PlCgxoPBrO1LnVPKF_tH_A-YxQfqCBF8d9jXKm8h-eqBsF6UL1oXnmBJd2pzfbvqGXBd-2cfngYCPK2Lm1zrjHb6-4VTuMQU5Ed8DEoKGM=', start_index=2775)
Annotation(end_index=3304, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElODk0JWyhftHXU9wO2QZiM5LAXh9_0ApSKrpvWenulaMIndKM_sjgfdvF-LXvXghkM7CVGe7FAgD7gZJwIzR0pFodnOyqqNz2p0tBC7yZzuKAcb592xRpknWUaWcdMDk_MZSNDQiD', start_index=3292)
Annotation(end_index=3304, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlgBqyd7HoeA_tH4WyHNke0PlCgxoPBrO1LnVPKF_tH_A-YxQfqCBF8d9jXKm8h-eqBsF6UL1oXnmBJd2pzfbvqGXBd-2cfngYCPK2Lm1zrjHb6-4VTuMQU5Ed8DEoKGM=', start_index=3292)
Annotation(end_index=4753, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZnqaOFItCJLAouyMDfZUin6xtUXcbSJYtoPcPTFtqhkTrCWRO7XxtlMlUXNx5rxqZC3zEsQGmtCmwZUMEI7XhPMd-mWMYCKkyfgqeqf2ojcBye8IwyWqJYw8Lid9U338SBrGzlr-g', start_index=4741)
Annotation(end_index=4753, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQt6Z_1v1Y44RIT6AmSQlKYlo_ENBBBuw3IxM4mtkU3Xj0fhKOvOEWnrQkGVnlU-vpvEbgz9M6Jc7ZQ82Yp_Uph2-joDju32oZapacL3KwnBy9FPFNpbteDnJssZkNCufhaYA-7xoDxA==', start_index=4741)
Annotation(end_index=4979, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaoBy6NO-Lk5M65LEDdgGZusG0JcD5V4QM4ybCvjOOyrgTVq9T7T6ywjLa6vf-tWjFbHy7Xw7ZdGZUe973Cw5btahf0Sz3XxlbX-tmo7wMcL3qS9PK4UBNMcOhcG8wi0k0GOj3q-CpPwOe536YVq4b2ZOmfiJCa4GSxHRk6Kkw8QX66jEA-wwL67vm4qMp-vphoI4BIP0CYfNI', start_index=4967)
Annotation(end_index=4979, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiIziB8k3glCq9DAbSRIKfdQ6QObtJClrR8rdLXo0Fw4vME_H8lVpD68QKOdz9SewjkSXt-whq3dRZV1hLFu5iM_A_Y1HK97_XMva5l_xWKM5uSh8HeED1V_Xl_yRa58G8yEsKGXRUqDp-1l_nqtj7IohXKWthqicPtqGZV4AiDyZUhvF4z_HmrCJ2coaFfWzOLn6uCoKjck7moF5Rgdpy-db2u8Y-', start_index=4967)
Annotation(end_index=5388, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxX-4gBAnYdQTy45Ah1ioDoibuPPvwEdxPkLBHZIAhTPI4qx4R31A0QNfjAsUAtTpVQSKkYcHfKYyuUp4TPGfPwzg9hS4mPPEoG9z_p2Dvl5HIYbOtVh7IWe_MxdFM37CmqTMTc9qw_A==', start_index=5379)
Annotation(end_index=5584, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZnqaOFItCJLAouyMDfZUin6xtUXcbSJYtoPcPTFtqhkTrCWRO7XxtlMlUXNx5rxqZC3zEsQGmtCmwZUMEI7XhPMd-mWMYCKkyfgqeqf2ojcBye8IwyWqJYw8Lid9U338SBrGzlr-g', start_index=5575)
Annotation(end_index=6124, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZujCVEdvx8G_7ReZ23KQbQhWHXdJsUSgUOifHGyohLQqY8YMN1ZgcRv6Mnlp9JwH4y17QVUz0mll3xOqOzPKzhPnWbZG_HuHtERn6-TSGzKDJjcSAN_H4YuX0IE8=', start_index=6111)
Annotation(end_index=6124, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnlkL4NYiQcERZqCePEbTiJ23Md1udspeQ-wzGD5pDKoS4OxRpGUQxuEWIEIFT9JDpMdo_YMX0IxEAoWmE1pptGnDT5MF_oqeNG86_I0bsi8OTX7FgA2w9CiGT5ZPOoESkGGfRXKkI7iIcmlGHzoVLUxMBvP76pcS_BYZ8TT5v2Gdgoddzc4pJuJZXYSev0NG0_h5j71psBbEISSf-LuV4VJj1pc-eEP8HE178zUYvpYHDZgYz', start_index=6111)
Annotation(end_index=6287, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZujCVEdvx8G_7ReZ23KQbQhWHXdJsUSgUOifHGyohLQqY8YMN1ZgcRv6Mnlp9JwH4y17QVUz0mll3xOqOzPKzhPnWbZG_HuHtERn6-TSGzKDJjcSAN_H4YuX0IE8=', start_index=6278)
Annotation(end_index=6474, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDQwmJ3xbdmB2Nj26PLbYpOqJMi6AP1V8tzn-wysy2c8fwj2htFViQUHG1PsVPeGjx0yPlEIGs-XWu0vvZCW6qz0T5XrPLYvEOj3fw2crqhquGIhCysJOmlL300YX0GmAV4rFgE7sQ', start_index=6461)
Annotation(end_index=6474, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZujCVEdvx8G_7ReZ23KQbQhWHXdJsUSgUOifHGyohLQqY8YMN1ZgcRv6Mnlp9JwH4y17QVUz0mll3xOqOzPKzhPnWbZG_HuHtERn6-TSGzKDJjcSAN_H4YuX0IE8=', start_index=6461)
Annotation(end_index=7452, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPIa8gcFvyngyBf5-UodneqXVlQIHHC2_lHl4GDyZtIPArU225-j3A3oqLIbRSu93X0IdaXFf4oPITPl8MWMjBqJinqBWCh6w8uKx13yLfVdDllSmNbAMQAUGkO1-87kcBl224SaDN', start_index=7438)
Annotation(end_index=7452, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFnUERbr9B4q3nxgyYyD2NgPcMo5r0plNe7yX3rkPG2PcMYAHsu1Kihdhw24ksiqahSWJMgn5g-RywhQ4wyJgKfB7EwRU9dzcmdzRCJpT0RN51NBFXJgtpX0Gjpweh-Hq3Z9dHnxU0iW2vSxyRyE30MfwE9l4Svswt2y5y2TvsPpxW7Nd7QfZ-RvFrJI5XONto8iJpasbNIZJby1YDOwa3Hm6igUKoFftA7GhBU_VaKxGu2md0e2eMDrseZwj0Rlfp0FincJKatZpCEIrlbOI=', start_index=7438)
Annotation(end_index=8362, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbtSI8cE__uJ2cRyXCrETQDGIOJnsoLn-xyUhFfka6Wwze6HRFIpZ1xI-QG_IH2IRemVs7Fz1xTDnqDJ7Y9Be3bym-rez4ZYREdWktcfz_wvPWFbb3eblSIjIW0eYrwsu8uvSi5pXsLn4mF92NtSNLbCO7cIf-_kk=', start_index=8349)
Annotation(end_index=8362, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElODk0JWyhftHXU9wO2QZiM5LAXh9_0ApSKrpvWenulaMIndKM_sjgfdvF-LXvXghkM7CVGe7FAgD7gZJwIzR0pFodnOyqqNz2p0tBC7yZzuKAcb592xRpknWUaWcdMDk_MZSNDQiD', start_index=8349)
Annotation(end_index=8539, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-7gjGmr-aLcvF4x8rpJK2ZFMQdZJ2k22FacxW-0E8ODJPP6XE6caLUyplkcybNLW6emRvVJJa1_4xFH-YKedMfp4_1Zb6Vv6WxrperRZxhD8B8AzYdKcx-KbDc6PmKReclJY5d2nE5ctLK_vW', start_index=8525)
Annotation(end_index=8539, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF67ruMJJZRlUGcnRniGKnEoi-BuYFAYT-HIdWapaRYk2IhstnNZa0QVdqLZ_caRtTdQfiLlfL_uAfIieMsAicvALXt4fssJ9VS1xcx7F2TftG_W5pB5ZhnAiHrfNfjHGxj5Q13aRDZRbWv3_0o247b6NKIRXFE355ZecgIoGQ=', start_index=8525)
Annotation(end_index=8853, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAxmqPU-DOQdlBfh74hKiuUWp-KJtVeg6IgLkIhkItH7vI8HaI5vt9TwL_T4uo_A4y6Mb83X68LDurSd4x6mZHSyAddAnM7HIkCpPzAeu-6ydZZh2R9Cn3W49rP_kEneMuQQoeEFqNWgCLcWUYRlxuBJ_DXtXIUKUKZDW-QP-vwzvn1bRuNtvTnkiJmvUODxt2YO8jGMYZTufVCJX7cMFNwpRAZnmvN1_DijvZtNEO8ca-dtZv4Ak5FY9A4w==', start_index=8839)
Annotation(end_index=8853, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlBcrgn1RYniGyNYOKx3tg9Da9EuWfdW_ptEsndOGt_5lMyQwcgs8wCbECraRFw3bAK7J3KcHt0JnizndZyq5dbOCtKwkBq2PnWaKgJZdu_SngSjGZiRQKR5dhi_r_hlP4_yNlFohNTCHAYl4QnvZ9Sk1qODKD7vwShzaFYke2MShz_asMj1OotV7saozm7GLCccPsLCKeAxvqAYPb0J8QSwo-QA==', start_index=8839)
Annotation(end_index=9266, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_HZLxaGBx-sI5QvNrqs6swRtlzHYHYuF4FfK053nYfGdLcfdJ60mOOBAxvoGzz8eJreSuCosUPE-MyaY0romTpuG4G4sUD8BpW-9vzvr8_mynNlXLNmc4jH-iwrEo5KGNacuv', start_index=9252)
Annotation(end_index=9266, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlBcrgn1RYniGyNYOKx3tg9Da9EuWfdW_ptEsndOGt_5lMyQwcgs8wCbECraRFw3bAK7J3KcHt0JnizndZyq5dbOCtKwkBq2PnWaKgJZdu_SngSjGZiRQKR5dhi_r_hlP4_yNlFohNTCHAYl4QnvZ9Sk1qODKD7vwShzaFYke2MShz_asMj1OotV7saozm7GLCccPsLCKeAxvqAYPb0J8QSwo-QA==', start_index=9252)
Annotation(end_index=9567, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElODk0JWyhftHXU9wO2QZiM5LAXh9_0ApSKrpvWenulaMIndKM_sjgfdvF-LXvXghkM7CVGe7FAgD7gZJwIzR0pFodnOyqqNz2p0tBC7yZzuKAcb592xRpknWUaWcdMDk_MZSNDQiD', start_index=9554)
Annotation(end_index=9567, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlBcrgn1RYniGyNYOKx3tg9Da9EuWfdW_ptEsndOGt_5lMyQwcgs8wCbECraRFw3bAK7J3KcHt0JnizndZyq5dbOCtKwkBq2PnWaKgJZdu_SngSjGZiRQKR5dhi_r_hlP4_yNlFohNTCHAYl4QnvZ9Sk1qODKD7vwShzaFYke2MShz_asMj1OotV7saozm7GLCccPsLCKeAxvqAYPb0J8QSwo-QA==', start_index=9554)
Annotation(end_index=10338, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZnqaOFItCJLAouyMDfZUin6xtUXcbSJYtoPcPTFtqhkTrCWRO7XxtlMlUXNx5rxqZC3zEsQGmtCmwZUMEI7XhPMd-mWMYCKkyfgqeqf2ojcBye8IwyWqJYw8Lid9U338SBrGzlr-g', start_index=10326)
Annotation(end_index=10338, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQt6Z_1v1Y44RIT6AmSQlKYlo_ENBBBuw3IxM4mtkU3Xj0fhKOvOEWnrQkGVnlU-vpvEbgz9M6Jc7ZQ82Yp_Uph2-joDju32oZapacL3KwnBy9FPFNpbteDnJssZkNCufhaYA-7xoDxA==', start_index=10326)
Annotation(end_index=10738, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZnqaOFItCJLAouyMDfZUin6xtUXcbSJYtoPcPTFtqhkTrCWRO7XxtlMlUXNx5rxqZC3zEsQGmtCmwZUMEI7XhPMd-mWMYCKkyfgqeqf2ojcBye8IwyWqJYw8Lid9U338SBrGzlr-g', start_index=10725)
Annotation(end_index=10738, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGv_D0KTxZnL34oLfwn4D3rvKORumJqg9_OLJj9n_8zjj0DyoP_3nF6IQ3QbKRgeBsxHqRS9szD4R84xIp5yw0LYPsFvviOAwAV3GmUZkLEpqFZ8MkrIUSSQxEk293rsrGdh_toEacUTJQeSDYhz1LRC4CjKBA4vzJCuaP0', start_index=10725)
Annotation(end_index=11119, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiIziB8k3glCq9DAbSRIKfdQ6QObtJClrR8rdLXo0Fw4vME_H8lVpD68QKOdz9SewjkSXt-whq3dRZV1hLFu5iM_A_Y1HK97_XMva5l_xWKM5uSh8HeED1V_Xl_yRa58G8yEsKGXRUqDp-1l_nqtj7IohXKWthqicPtqGZV4AiDyZUhvF4z_HmrCJ2coaFfWzOLn6uCoKjck7moF5Rgdpy-db2u8Y-', start_index=11106)
Annotation(end_index=11119, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxPSjhvCoZsT_V6acTTaOYRzCDL4HY1xYKcGIUHci9-KYVjjss2LEVOriFYS3JRX9XW6TeH9qwhSqjBk2K8HWd7hjdNUjCiy92hEMM9DLRXUwLzuiSjZwjr4PWmMHGOPhsPjAON7qR', start_index=11106)
Annotation(end_index=11353, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaoBy6NO-Lk5M65LEDdgGZusG0JcD5V4QM4ybCvjOOyrgTVq9T7T6ywjLa6vf-tWjFbHy7Xw7ZdGZUe973Cw5btahf0Sz3XxlbX-tmo7wMcL3qS9PK4UBNMcOhcG8wi0k0GOj3q-CpPwOe536YVq4b2ZOmfiJCa4GSxHRk6Kkw8QX66jEA-wwL67vm4qMp-vphoI4BIP0CYfNI', start_index=11340)
Annotation(end_index=11353, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEumtMf5CIBEe_kiGxrADpbgt-WVCI24UB6SF1awsSP5F6fC6ro49upJ07CLTECRzvK4IhaKRKAJbkyy-at-R0Gpyw3GT-jLHtad9H5PhUMpYB0CVsrbsy5GPZSmLosxKSME2qUPi5SmlLXzmoO5zlCiT98fuK0SdQQ0yMB4phYghV35FRfWsdfitUxem-pSHG9xKls3hY=', start_index=11340)
Annotation(end_index=11991, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzJWu8moK5DZ32cNPfsZPNCizU7PqLyko81uebaRPQZ3vniIMzs9weFKhRljggnx4XQqxdY1QDDPonYTh9wYA9lCWZFyuHfS45HvxOH8cr_RIXU_q-rZu4TyD0IzA5KaKkzQMdNo9tmQ==', start_index=11977)
Annotation(end_index=11991, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1O2iN2qdKDpDb8PTu5VnA5sav5MMeLR5vge1K9e8CePvWSQKneYj0qnMx0bGakHxJw2xojEDaRET58eer8zwJZNsfoSK_VyEoPLxREuA4P7bu8AlsCAgcSGq8WU3vH-xILaTH4ru0HOWLMPa8zJKXHNEfoXUFHstmXqknv4dbxkfups2lsgmrnxEWRusZo8hAt6cp8PfSp7XkZcd3zcEGQzBkOIR3JapccSvxeptVN8QCPWFG9b4aZLQRMCbCMufpHbeI', start_index=11977)
Annotation(end_index=12370, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0qCgdjAu-GmPhRuVK796NJo1mENtzZSstseTd-CCE8t-Ba6EWFFZ56R-iTdqDMocxWARRExgCviXyTs6wTRlpmbEKDpu6WA7dm5bINquKRBF_GrrecGD-_awdgKIPcINDJYrQ-l0KArySpzrVD2cJx7MjtmxVPkvS_hsAFvvvRElPa-SBs1VYxxSlOa2ylmr7QZVxawOYLNEAx-A78Bk_fRckEYID8mSeQZ7Yug3ognf14v245ENTGWaQwJEn9zE=', start_index=12353)
Annotation(end_index=12370, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdk9fRYpFJKOs8mbFpi6TLJjf-mAqwlDSz9C1QNMRMvZlrVtdNERbOQYcz3ePjsEhWFJ1GtI7lnDp1o_haJuVViNjyf2JMIaITA9b_OrrtG9_kg9sMP2BlCryuP4uI8WkCSCCyw4p_WFuc', start_index=12353)
Annotation(end_index=12370, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlgBqyd7HoeA_tH4WyHNke0PlCgxoPBrO1LnVPKF_tH_A-YxQfqCBF8d9jXKm8h-eqBsF6UL1oXnmBJd2pzfbvqGXBd-2cfngYCPK2Lm1zrjHb6-4VTuMQU5Ed8DEoKGM=', start_index=12353)
Annotation(end_index=12612, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwXhmcoluyt0z4Sjqi2M2ZjTwLlEJGpn-TY3DL0dQNMlwkuw2bn40oCzvcJ6AT_cx71pSCNGDoOS8cRqLwZ__sMGyCYr5Q136L5WKnYoPzjdNogwn1PckE1ITJJAHdnfRAOH6foFj35QaN8Y77uyAZcEk=', start_index=12598)
Annotation(end_index=12612, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGi4d4dlMpl72Y5ClgPxQbcj22n2-5HRp-VL0ilI5bWJ3JR9WJhhVwlT4KiOYWbmnlsmZ0Cu3HXeQyvwEaRvIBnut5gOp1YE6pF_g4kJbAGbC_iVenemA39bMADRhWpqcVrY3EMcV5GFkDNwTt2ooR0rYNxOt-1lh1CE_dyJHMc_Blx3L1ULmw7ZtntVCkGw63Dxe2ciNCNE6WKfomDjR86q6UI20GVXlejUKYPsuitUuVeOALhK3Y-QrgUiAl7HB0=', start_index=12598)
Annotation(end_index=12976, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnC3b5XaNELUrCIPtJxV73HEFCl-eU4C6w7GfVtFJ4-Hd2cepsFjShOg4j7HUR6VjzWn-tkyB3zVw1uLkjte3mouX-lYA7WU23w3BV7mJNiet-AmFOo3KQT3xcD1Y3SryTCvaXUXyahA==', start_index=12963)
Annotation(end_index=12976, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1O2iN2qdKDpDb8PTu5VnA5sav5MMeLR5vge1K9e8CePvWSQKneYj0qnMx0bGakHxJw2xojEDaRET58eer8zwJZNsfoSK_VyEoPLxREuA4P7bu8AlsCAgcSGq8WU3vH-xILaTH4ru0HOWLMPa8zJKXHNEfoXUFHstmXqknv4dbxkfups2lsgmrnxEWRusZo8hAt6cp8PfSp7XkZcd3zcEGQzBkOIR3JapccSvxeptVN8QCPWFG9b4aZLQRMCbCMufpHbeI', start_index=12963)
Annotation(end_index=13191, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGv_D0KTxZnL34oLfwn4D3rvKORumJqg9_OLJj9n_8zjj0DyoP_3nF6IQ3QbKRgeBsxHqRS9szD4R84xIp5yw0LYPsFvviOAwAV3GmUZkLEpqFZ8MkrIUSSQxEk293rsrGdh_toEacUTJQeSDYhz1LRC4CjKBA4vzJCuaP0', start_index=13181)
Annotation(end_index=13870, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTB1VkCHF9k_7UNZeuQeeQd3WBRKhzvimUQe9Mqp-Z-U0ZTm97w2_KP9ES2ImKPTWfIfe-5T8BFJt_STKuUP0l5StSPVBVuDChO-G_OIFHB0DAYTUMs0NiaS14PtD1CAyV23fOfk74JIZwdtjq0gm6uoMAlKwCcDszzj8FlRB35sSIpK6zax8cNyX8zuXbv9CPnFMWWpFO7rBhc08ZxUxbq8D4h7dgceAKcDx3qEtM8GhEs-QSnF4HScU=', start_index=13856)
Annotation(end_index=13870, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFnUERbr9B4q3nxgyYyD2NgPcMo5r0plNe7yX3rkPG2PcMYAHsu1Kihdhw24ksiqahSWJMgn5g-RywhQ4wyJgKfB7EwRU9dzcmdzRCJpT0RN51NBFXJgtpX0Gjpweh-Hq3Z9dHnxU0iW2vSxyRyE30MfwE9l4Svswt2y5y2TvsPpxW7Nd7QfZ-RvFrJI5XONto8iJpasbNIZJby1YDOwa3Hm6igUKoFftA7GhBU_VaKxGu2md0e2eMDrseZwj0Rlfp0FincJKatZpCEIrlbOI=', start_index=13856)
Annotation(end_index=14087, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPIa8gcFvyngyBf5-UodneqXVlQIHHC2_lHl4GDyZtIPArU225-j3A3oqLIbRSu93X0IdaXFf4oPITPl8MWMjBqJinqBWCh6w8uKx13yLfVdDllSmNbAMQAUGkO1-87kcBl224SaDN', start_index=14073)
Annotation(end_index=14087, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFnUERbr9B4q3nxgyYyD2NgPcMo5r0plNe7yX3rkPG2PcMYAHsu1Kihdhw24ksiqahSWJMgn5g-RywhQ4wyJgKfB7EwRU9dzcmdzRCJpT0RN51NBFXJgtpX0Gjpweh-Hq3Z9dHnxU0iW2vSxyRyE30MfwE9l4Svswt2y5y2TvsPpxW7Nd7QfZ-RvFrJI5XONto8iJpasbNIZJby1YDOwa3Hm6igUKoFftA7GhBU_VaKxGu2md0e2eMDrseZwj0Rlfp0FincJKatZpCEIrlbOI=', start_index=14073)
Annotation(end_index=14813, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNkPjeTs5ZteYnsmOrvEeXOkw_vtzdr-d14pxCq_yFW3Ad1Vsnq2HD61KbESIo0qTN4d3SBk01fzVBDQ7Fzlr2PFGsoTS-fFS0fCB-oMBmiFGd4cp1rUDQJ2TnPNlzwXoBtgDeKfGYUGlD08bD', start_index=14799)
Annotation(end_index=14813, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGv_D0KTxZnL34oLfwn4D3rvKORumJqg9_OLJj9n_8zjj0DyoP_3nF6IQ3QbKRgeBsxHqRS9szD4R84xIp5yw0LYPsFvviOAwAV3GmUZkLEpqFZ8MkrIUSSQxEk293rsrGdh_toEacUTJQeSDYhz1LRC4CjKBA4vzJCuaP0', start_index=14799)
Annotation(end_index=15129, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHELPXXMN0lXIkRLIhewlxNTmrhu2mfgsu1zD0sZjADN1WqC0bA4OZxh0ZIUICgEuIt4zRJXGyFb0yH7ULk9d_MvX9ayoKnThzrl5lt0ZtGECkYjQWBU1Csx0nH00WztYvsJ3lQ5brQ', start_index=15116)
Annotation(end_index=15129, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlgBqyd7HoeA_tH4WyHNke0PlCgxoPBrO1LnVPKF_tH_A-YxQfqCBF8d9jXKm8h-eqBsF6UL1oXnmBJd2pzfbvqGXBd-2cfngYCPK2Lm1zrjHb6-4VTuMQU5Ed8DEoKGM=', start_index=15116)
Annotation(end_index=15606, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGv_D0KTxZnL34oLfwn4D3rvKORumJqg9_OLJj9n_8zjj0DyoP_3nF6IQ3QbKRgeBsxHqRS9szD4R84xIp5yw0LYPsFvviOAwAV3GmUZkLEpqFZ8MkrIUSSQxEk293rsrGdh_toEacUTJQeSDYhz1LRC4CjKBA4vzJCuaP0', start_index=15592)
Annotation(end_index=15606, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUu41Q7LlwSf9ezZX8I4FoTT8CktIb1n8-Tj64GLCx_f6gRXEIRXkvnXLQKYKGdRRmDTnW7z9A6ebnY-R7_5lJ7YV86AjD0Z17eKSHGHJ8Ai3fRGk36rMjQarLS5JsqdC8NbSlegwQ', start_index=15592)
Annotation(end_index=16755, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlgBqyd7HoeA_tH4WyHNke0PlCgxoPBrO1LnVPKF_tH_A-YxQfqCBF8d9jXKm8h-eqBsF6UL1oXnmBJd2pzfbvqGXBd-2cfngYCPK2Lm1zrjHb6-4VTuMQU5Ed8DEoKGM=', start_index=16746)
Annotation(end_index=16790, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnC3b5XaNELUrCIPtJxV73HEFCl-eU4C6w7GfVtFJ4-Hd2cepsFjShOg4j7HUR6VjzWn-tkyB3zVw1uLkjte3mouX-lYA7WU23w3BV7mJNiet-AmFOo3KQT3xcD1Y3SryTCvaXUXyahA==', start_index=16781)
Annotation(end_index=16868, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0uLCrdwCcxCzk69dDReJ4KnLWG4WrlUO12xodsAq_kIbfuP2Ge2qv1GFfr0Q32w_UIDaYH7U6bauCjKbTKFh75FJZ_xE0K-Kmw4m6adXp7hQtGKi0e1XWEntfBPuRTZbOTpAur9kCzyvnR0xvcxlM_Pb64U1B0EM1JIi4Xu7m9FNh30dIa3j3vMBieqFi-Ce1WyNi2HnLTwpNtc7FaXa78n68Bukw7U5Q2T8kdBljzkyJ3QPuT7b4wo3vwZA_OiTnw09pPaR9EPf3KWK4cCh2AB_tNucNLHNVMg==', start_index=16858)
Annotation(end_index=16961, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZujCVEdvx8G_7ReZ23KQbQhWHXdJsUSgUOifHGyohLQqY8YMN1ZgcRv6Mnlp9JwH4y17QVUz0mll3xOqOzPKzhPnWbZG_HuHtERn6-TSGzKDJjcSAN_H4YuX0IE8=', start_index=16952)
Annotation(end_index=17036, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxX-4gBAnYdQTy45Ah1ioDoibuPPvwEdxPkLBHZIAhTPI4qx4R31A0QNfjAsUAtTpVQSKkYcHfKYyuUp4TPGfPwzg9hS4mPPEoG9z_p2Dvl5HIYbOtVh7IWe_MxdFM37CmqTMTc9qw_A==', start_index=17027)
Annotation(end_index=17113, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElODk0JWyhftHXU9wO2QZiM5LAXh9_0ApSKrpvWenulaMIndKM_sjgfdvF-LXvXghkM7CVGe7FAgD7gZJwIzR0pFodnOyqqNz2p0tBC7yZzuKAcb592xRpknWUaWcdMDk_MZSNDQiD', start_index=17104)
Annotation(end_index=17179, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTrK2woy9ekdBXd8AyAHOEDrTGgqHv6egdaSjrZmHrILak3gPgiuufZiOrDayPq3Mu8GFyfpUqxCU-4ajNHkJdi3T5ZF3VlTY8v4JdRqe-HmWusploaf4sDgnEcWC4qeA5gYnN4sLyFNOaIT39ue4aMmF5jZBUKrjrYm8OMhiRyu8IDNKIIQ435l3TOwhrECdn1PJ42keIbNkehbFBbLXZ4BwUxD7tMEHL1yV2NbbYxW9BKzgr8hhoynbd0_7QsZbm8bde_FnEjaNIJBg9t-mWWMRt7p2TuuvQ4h4IeTCfhTSuoveSMUve3PO8z6r5rNjeeQhNBTo27Hp2W69QGtP1RtOiLqLqdP2xdow=', start_index=17169)
Annotation(end_index=17247, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlBcrgn1RYniGyNYOKx3tg9Da9EuWfdW_ptEsndOGt_5lMyQwcgs8wCbECraRFw3bAK7J3KcHt0JnizndZyq5dbOCtKwkBq2PnWaKgJZdu_SngSjGZiRQKR5dhi_r_hlP4_yNlFohNTCHAYl4QnvZ9Sk1qODKD7vwShzaFYke2MShz_asMj1OotV7saozm7GLCccPsLCKeAxvqAYPb0J8QSwo-QA==', start_index=17237)
Annotation(end_index=17342, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkoF3tzMEEgCEi2sszKMqEJhRkmwAAmVUqBmtnii8B9NxXW7VkzErSEVcj6NtwzHcwqMqiB4NIr3bqvZdRm_iMheV31opSod6dZ2P8JiSGdk9iI2YsgpPeNa37V0YLp2XXvFE-huA2Gg==', start_index=17332)
Annotation(end_index=17465, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAxmqPU-DOQdlBfh74hKiuUWp-KJtVeg6IgLkIhkItH7vI8HaI5vt9TwL_T4uo_A4y6Mb83X68LDurSd4x6mZHSyAddAnM7HIkCpPzAeu-6ydZZh2R9Cn3W49rP_kEneMuQQoeEFqNWgCLcWUYRlxuBJ_DXtXIUKUKZDW-QP-vwzvn1bRuNtvTnkiJmvUODxt2YO8jGMYZTufVCJX7cMFNwpRAZnmvN1_DijvZtNEO8ca-dtZv4Ak5FY9A4w==', start_index=17455)
Annotation(end_index=17543, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnC3b5XaNELUrCIPtJxV73HEFCl-eU4C6w7GfVtFJ4-Hd2cepsFjShOg4j7HUR6VjzWn-tkyB3zVw1uLkjte3mouX-lYA7WU23w3BV7mJNiet-AmFOo3KQT3xcD1Y3SryTCvaXUXyahA==', start_index=17534)
Annotation(end_index=17634, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZujCVEdvx8G_7ReZ23KQbQhWHXdJsUSgUOifHGyohLQqY8YMN1ZgcRv6Mnlp9JwH4y17QVUz0mll3xOqOzPKzhPnWbZG_HuHtERn6-TSGzKDJjcSAN_H4YuX0IE8=', start_index=17625)
Annotation(end_index=17707, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1O2iN2qdKDpDb8PTu5VnA5sav5MMeLR5vge1K9e8CePvWSQKneYj0qnMx0bGakHxJw2xojEDaRET58eer8zwJZNsfoSK_VyEoPLxREuA4P7bu8AlsCAgcSGq8WU3vH-xILaTH4ru0HOWLMPa8zJKXHNEfoXUFHstmXqknv4dbxkfups2lsgmrnxEWRusZo8hAt6cp8PfSp7XkZcd3zcEGQzBkOIR3JapccSvxeptVN8QCPWFG9b4aZLQRMCbCMufpHbeI', start_index=17697)
Annotation(end_index=17805, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSBdY1vRTM1F_cUvieBYgqszMJL-3c_MglTqYEdSMkzo0PctqeHxZeKg_QsfH1H1DXEDbDTWrIKvZHsStDJzU94mQURA-sRAkvaAhf-O0UOqNPwHK9sXiy4x6iCvCErPcNhglHfhGkwg==', start_index=17795)
Annotation(end_index=17900, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGv_D0KTxZnL34oLfwn4D3rvKORumJqg9_OLJj9n_8zjj0DyoP_3nF6IQ3QbKRgeBsxHqRS9szD4R84xIp5yw0LYPsFvviOAwAV3GmUZkLEpqFZ8MkrIUSSQxEk293rsrGdh_toEacUTJQeSDYhz1LRC4CjKBA4vzJCuaP0', start_index=17890)
Annotation(end_index=17998, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNkPjeTs5ZteYnsmOrvEeXOkw_vtzdr-d14pxCq_yFW3Ad1Vsnq2HD61KbESIo0qTN4d3SBk01fzVBDQ7Fzlr2PFGsoTS-fFS0fCB-oMBmiFGd4cp1rUDQJ2TnPNlzwXoBtgDeKfGYUGlD08bD', start_index=17988)
Annotation(end_index=18081, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiIziB8k3glCq9DAbSRIKfdQ6QObtJClrR8rdLXo0Fw4vME_H8lVpD68QKOdz9SewjkSXt-whq3dRZV1hLFu5iM_A_Y1HK97_XMva5l_xWKM5uSh8HeED1V_Xl_yRa58G8yEsKGXRUqDp-1l_nqtj7IohXKWthqicPtqGZV4AiDyZUhvF4z_HmrCJ2coaFfWzOLn6uCoKjck7moF5Rgdpy-db2u8Y-', start_index=18072)
Annotation(end_index=18163, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaoBy6NO-Lk5M65LEDdgGZusG0JcD5V4QM4ybCvjOOyrgTVq9T7T6ywjLa6vf-tWjFbHy7Xw7ZdGZUe973Cw5btahf0Sz3XxlbX-tmo7wMcL3qS9PK4UBNMcOhcG8wi0k0GOj3q-CpPwOe536YVq4b2ZOmfiJCa4GSxHRk6Kkw8QX66jEA-wwL67vm4qMp-vphoI4BIP0CYfNI', start_index=18154)
Annotation(end_index=18248, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFH6q1wi336OImpOPiC1tSCCwQXtcf7JYq2OX0yKVxmQ-i7aKs3TDYXPAFw6SD5oAcEGJCwPzur7mip3k2ph6KqpoFgnXVbvQOwJTlTWhh3QDD5yXkpUOyLk_-h5ILMwB21z-NhmqSXA7XVee9pfkRFhg8jAJn14A8ImG5uDX4UZ6twyZz7fPIBg7SIFO28DVZK_RSVoHLOQnY1J77lbe2x', start_index=18238)
Annotation(end_index=18335, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFnUERbr9B4q3nxgyYyD2NgPcMo5r0plNe7yX3rkPG2PcMYAHsu1Kihdhw24ksiqahSWJMgn5g-RywhQ4wyJgKfB7EwRU9dzcmdzRCJpT0RN51NBFXJgtpX0Gjpweh-Hq3Z9dHnxU0iW2vSxyRyE30MfwE9l4Svswt2y5y2TvsPpxW7Nd7QfZ-RvFrJI5XONto8iJpasbNIZJby1YDOwa3Hm6igUKoFftA7GhBU_VaKxGu2md0e2eMDrseZwj0Rlfp0FincJKatZpCEIrlbOI=', start_index=18325)
Annotation(end_index=18427, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTB1VkCHF9k_7UNZeuQeeQd3WBRKhzvimUQe9Mqp-Z-U0ZTm97w2_KP9ES2ImKPTWfIfe-5T8BFJt_STKuUP0l5StSPVBVuDChO-G_OIFHB0DAYTUMs0NiaS14PtD1CAyV23fOfk74JIZwdtjq0gm6uoMAlKwCcDszzj8FlRB35sSIpK6zax8cNyX8zuXbv9CPnFMWWpFO7rBhc08ZxUxbq8D4h7dgceAKcDx3qEtM8GhEs-QSnF4HScU=', start_index=18417)
Annotation(end_index=18526, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZnqaOFItCJLAouyMDfZUin6xtUXcbSJYtoPcPTFtqhkTrCWRO7XxtlMlUXNx5rxqZC3zEsQGmtCmwZUMEI7XhPMd-mWMYCKkyfgqeqf2ojcBye8IwyWqJYw8Lid9U338SBrGzlr-g', start_index=18517)
Annotation(end_index=18614, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPIa8gcFvyngyBf5-UodneqXVlQIHHC2_lHl4GDyZtIPArU225-j3A3oqLIbRSu93X0IdaXFf4oPITPl8MWMjBqJinqBWCh6w8uKx13yLfVdDllSmNbAMQAUGkO1-87kcBl224SaDN', start_index=18604)
Annotation(end_index=18686, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzJWu8moK5DZ32cNPfsZPNCizU7PqLyko81uebaRPQZ3vniIMzs9weFKhRljggnx4XQqxdY1QDDPonYTh9wYA9lCWZFyuHfS45HvxOH8cr_RIXU_q-rZu4TyD0IzA5KaKkzQMdNo9tmQ==', start_index=18676)
Annotation(end_index=18778, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnlkL4NYiQcERZqCePEbTiJ23Md1udspeQ-wzGD5pDKoS4OxRpGUQxuEWIEIFT9JDpMdo_YMX0IxEAoWmE1pptGnDT5MF_oqeNG86_I0bsi8OTX7FgA2w9CiGT5ZPOoESkGGfRXKkI7iIcmlGHzoVLUxMBvP76pcS_BYZ8TT5v2Gdgoddzc4pJuJZXYSev0NG0_h5j71psBbEISSf-LuV4VJj1pc-eEP8HE178zUYvpYHDZgYz', start_index=18768)
Annotation(end_index=18841, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbtSI8cE__uJ2cRyXCrETQDGIOJnsoLn-xyUhFfka6Wwze6HRFIpZ1xI-QG_IH2IRemVs7Fz1xTDnqDJ7Y9Be3bym-rez4ZYREdWktcfz_wvPWFbb3eblSIjIW0eYrwsu8uvSi5pXsLn4mF92NtSNLbCO7cIf-_kk=', start_index=18831)
Annotation(end_index=18904, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_HZLxaGBx-sI5QvNrqs6swRtlzHYHYuF4FfK053nYfGdLcfdJ60mOOBAxvoGzz8eJreSuCosUPE-MyaY0romTpuG4G4sUD8BpW-9vzvr8_mynNlXLNmc4jH-iwrEo5KGNacuv', start_index=18894)
Annotation(end_index=18986, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQt6Z_1v1Y44RIT6AmSQlKYlo_ENBBBuw3IxM4mtkU3Xj0fhKOvOEWnrQkGVnlU-vpvEbgz9M6Jc7ZQ82Yp_Uph2-joDju32oZapacL3KwnBy9FPFNpbteDnJssZkNCufhaYA-7xoDxA==', start_index=18977)
Annotation(end_index=19075, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF67ruMJJZRlUGcnRniGKnEoi-BuYFAYT-HIdWapaRYk2IhstnNZa0QVdqLZ_caRtTdQfiLlfL_uAfIieMsAicvALXt4fssJ9VS1xcx7F2TftG_W5pB5ZhnAiHrfNfjHGxj5Q13aRDZRbWv3_0o247b6NKIRXFE355ZecgIoGQ=', start_index=19065)
Annotation(end_index=19134, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-7gjGmr-aLcvF4x8rpJK2ZFMQdZJ2k22FacxW-0E8ODJPP6XE6caLUyplkcybNLW6emRvVJJa1_4xFH-YKedMfp4_1Zb6Vv6WxrperRZxhD8B8AzYdKcx-KbDc6PmKReclJY5d2nE5ctLK_vW', start_index=19124)
Annotation(end_index=19221, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDQwmJ3xbdmB2Nj26PLbYpOqJMi6AP1V8tzn-wysy2c8fwj2htFViQUHG1PsVPeGjx0yPlEIGs-XWu0vvZCW6qz0T5XrPLYvEOj3fw2crqhquGIhCysJOmlL300YX0GmAV4rFgE7sQ', start_index=19211)

## Sources
