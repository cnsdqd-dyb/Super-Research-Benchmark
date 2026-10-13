# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 8d87a23b | **Time:** 506.54s | **Cost:** $1.27787
--------------------------------------------------------------------------------

# The Equilibrium of Staging: Balancing Diagnostic Specificity and Treatment Timing in Liver Cancer TNM Classification

### Key Points
*   **The T1a "2 cm Rule" as the Primary Balance Mechanism:** In the 8th edition of the AJCC TNM system for Hepatocellular Carcinoma (HCC), the classification of solitary tumors $\le$ 2 cm as T1a *regardless of vascular invasion* represents the most significant structural compromise. This rule sacrifices the diagnostic specificity of identifying microvascular invasion (MVI) to prioritize treatment timing, acknowledging that small tumors have excellent prognoses and that delaying treatment for pathological confirmation yields diminishing returns.
*   **Clinical vs. Pathological Staging Dichotomy:** The system maintains balance by utilizing two distinct staging tracks. Clinical staging (cTNM), based on imaging, prioritizes *treatment timing* by allowing rapid decision-making (e.g., ablation, transplant) without invasive tissue sampling. Pathological staging (pTNM), derived from resection, prioritizes *diagnostic specificity* for prognostication and adjuvant therapy planning, quantifying the true tumor burden (including MVI and occult lymph node metastasis).
*   **Surrogate Markers for Lymph Node Metastasis (LNM):** Because biopsy of lymph nodes is invasive and imaging has low sensitivity, the system increasingly relies on "Tumor Burden Scores" (TBS) and biomarkers (e.g., CA 19-9, AFP) to predict LNM. This probabilistic approach balances the risk of undertreatment (missing N1 disease) against the morbidity and delay of routine lymphadenectomy.
*   **The Divergence of HCC and ICC:** The balance point differs by histology. In Intrahepatic Cholangiocarcinoma (ICC), the T-stage cutoff is 5 cm (T1a vs. T1b), and lymphadenectomy is more strongly recommended due to higher LNM rates, shifting the balance toward diagnostic specificity compared to HCC, where LNM is rare and treatment timing often takes precedence.

---

### Executive Summary
The Tumor-Node-Metastasis (TNM) staging system for liver cancer serves as the global language for cancer classification, yet it faces a unique challenge: the liver is a highly vascular organ where tumor burden and functional status are inextricably linked. The central tension in staging liver cancer lies between **diagnostic specificity**—the precise quantification of microscopic spread, vascular invasion, and nodal involvement—and **treatment timing**—the urgency to intervene before liver function decompensates or the tumor progresses beyond transplant criteria.

Research indicates that the primary mechanism balancing these competing demands is the **stratification of early-stage tumors (T1)** and the **selective application of lymphadenectomy**. Specifically, the 8th edition of the American Joint Committee on Cancer (AJCC) manual introduced a critical revision for Hepatocellular Carcinoma (HCC): solitary tumors $\le$ 2 cm are classified as T1a *regardless of vascular invasion*. This change acknowledges that for very small tumors, the time and invasiveness required to diagnose microscopic vascular invasion (specificity) are outweighed by the clinical benefit of immediate ablation or resection (timing). Conversely, for Intrahepatic Cholangiocarcinoma (ICC), where lymph node metastasis is a potent driver of mortality, the system shifts focus toward specificity, encouraging lymphadenectomy to accurately stage the N-category, even at the cost of increased surgical time.

This report provides an exhaustive analysis of how the TNM system navigates this trade-off, examining the evolution of T-stage definitions, the predictive modeling of lymph node metastasis, and the integration of radiomics to enhance specificity without compromising the therapeutic window.

---

## 1. Introduction: The Staging Dilemma in Liver Malignancies

Liver cancer, primarily Hepatocellular Carcinoma (HCC) and Intrahepatic Cholangiocarcinoma (ICC), presents a complex staging challenge that differs significantly from other solid tumors. Unlike breast or colorectal cancer, where the anatomical extent of the tumor is the sole determinant of resectability, liver cancer treatment is dictated equally by the **tumor burden** and the **underlying liver function** (often compromised by cirrhosis).

### 1.1 The Conflict: Specificity vs. Timing
The fundamental conflict addressed in this report is the trade-off between knowing the *exact* extent of the disease (Diagnostic Specificity) and acting *quickly* enough to ensure curative intent (Treatment Timing).

*   **Diagnostic Specificity** requires high-resolution data: presence of microvascular invasion (MVI), exact number of satellite nodules, and histological confirmation of lymph node metastasis (LNM). Obtaining this often requires surgical resection or extensive biopsy, which can delay therapy or be contraindicated in patients with coagulopathy.
*   **Treatment Timing** requires rapid categorization: Is the patient a candidate for transplant *now*? Can the lesion be ablated *today*? Delays to improve specificity can lead to "dropout" from transplant lists or progression from potentially resectable to unresectable disease.

### 1.2 The TNM Solution
The TNM system, maintained by the AJCC and the Union for International Cancer Control (UICC), attempts to resolve this by evolving its definitions. The transition from the 7th to the 8th edition marked a pivotal shift in how "early" liver cancer is defined, specifically manipulating the **T (Tumor)** and **N (Node)** categories to optimize the window for therapeutic intervention [cite: 1, 2, 3].

---

## 2. Quantifying Tumor Burden (T-Stage): The "2 cm Rule" and Vascular Invasion

The most distinct manifestation of the balance between specificity and timing is found in the definition of the T1 category for Hepatocellular Carcinoma.

### 2.1 The Evolution of T1: From 7th to 8th Edition
In the AJCC 7th edition, the distinction between T1 and T2 was heavily dependent on vascular invasion.
*   **7th Ed T1:** Solitary tumor without vascular invasion.
*   **7th Ed T2:** Solitary tumor *with* vascular invasion OR multiple tumors < 5 cm.

This system prioritized **specificity**. A 1.5 cm tumor with microscopic vascular invasion was upstaged to T2, theoretically grouping it with larger or multifocal tumors. However, clinically, this created a paradox: MVI is rarely diagnosable preoperatively. Therefore, a clinician could not accurately stage a patient as T1 or T2 without resecting the liver, rendering the staging system less useful for pre-treatment planning (timing) [cite: 3, 4].

**The 8th Edition Revision:**
To correct this, the 8th edition introduced a size-based split for T1, creating a "safe harbor" for small tumors:
*   **T1a:** Solitary tumor $\le$ 2 cm **regardless of vascular invasion**.
*   **T1b:** Solitary tumor > 2 cm **without vascular invasion**.
*   **T2:** Solitary tumor > 2 cm **with vascular invasion** OR multiple tumors < 5 cm [cite: 3, 5, 6].

### 2.2 The "Regardless of Vascular Invasion" Clause
The phrase "regardless of vascular invasion" for T1a tumors is the precise mechanism that balances specificity with timing.

*   **Sacrificing Specificity:** By ignoring vascular invasion in tumors $\le$ 2 cm, the system accepts a loss of prognostic precision. Studies show that even in small tumors, MVI is a risk factor for recurrence [cite: 5, 7]. A T1a tumor with MVI technically has a worse biology than a T1a tumor without it.
*   **Gaining Treatment Timing:** However, the absolute survival difference for tumors $\le$ 2 cm with vs. without MVI is clinically small compared to the risk of delaying treatment. By classifying all such tumors as T1a, the system allows clinicians to proceed immediately to curative treatments (ablation, resection, transplant) based on imaging size alone. It eliminates the need to "guess" the vascular status or perform risky biopsies, thereby streamlining the treatment pathway [cite: 3, 4].

### 2.3 The T1b vs. T2 Distinction
For tumors > 2 cm, the balance shifts back toward **specificity**. Here, vascular invasion remains a discriminator between T1b and T2.
*   **Rationale:** As tumor size increases, the probability and prognostic weight of vascular invasion increase. A 5 cm tumor with vascular invasion (T2) behaves significantly worse than a 5 cm tumor without it (T1b). In this cohort, the system demands higher diagnostic specificity (often inferred from radiologic features of macrovascular invasion or high-risk imaging features) because the treatment decision (e.g., extent of resection vs. systemic therapy) hinges on this distinction [cite: 4, 8].

### 2.4 Intrahepatic Cholangiocarcinoma (ICC) Divergence
It is crucial to note that this balance is calibrated differently for ICC.
*   **ICC T1a:** Solitary tumor $\le$ 5 cm without vascular invasion.
*   **ICC T1b:** Solitary tumor > 5 cm without vascular invasion.
*   **ICC T2:** Solitary tumor with vascular invasion OR multiple tumors [cite: 9, 10].

In ICC, the size cutoff is 5 cm rather than 2 cm, and vascular invasion immediately upstages even small tumors to T2 (if solitary with invasion) or higher. This reflects the more aggressive biological nature of ICC, where vascular invasion is a stronger driver of mortality than in very early HCC, necessitating a staging system that prioritizes specificity over the "fast-track" approach seen in HCC T1a [cite: 10].

---

## 3. Predicting Lymph Node Metastasis (N-Stage): The Surrogate Balance

While T-stage quantifies the primary mass, the N-stage (Regional Lymph Nodes) represents a binary crisis in liver cancer management. Lymph node metastasis (LNM) is a catastrophic prognostic indicator, yet it is notoriously difficult to diagnose without surgery.

### 3.1 The Diagnostic Deficit
*   **Imaging Limitations:** CT and MRI have low sensitivity for detecting LNM in liver cancer. Hyperplastic nodes (reactive to cirrhosis/hepatitis) often mimic metastatic nodes.
*   **Surgical Dilemma:** Routine lymphadenectomy (LND) provides 100% specificity (pN staging) but increases operative time and morbidity. In HCC, LNM is rare (~1-2% in early stage), making routine LND unjustified. In ICC, LNM is common (20-40%), making LND essential but often underperformed [cite: 11, 12].

### 3.2 Balancing via Predictive Surrogates
To balance the need for N-stage specificity with the desire to avoid unnecessary surgical trauma (treatment timing/recovery), the field has adopted **predictive surrogates** to quantify "Tumor Burden" as a proxy for N-stage risk.

#### 3.2.1 The Tumor Burden Score (TBS)
The Tumor Burden Score is a mathematical model used to predict outcomes and the likelihood of LNM, effectively bridging the gap between T-stage and N-stage.
*   **Formula:** $TBS^2 = (Maximum Tumor Diameter)^2 + (Number of Tumors)^2$.
*   **Application:** Research indicates that patients with a high TBS are statistically more likely to harbor occult LNM.
*   **The Balance:** Instead of performing LND on everyone (high specificity, poor efficiency) or no one (low specificity, high efficiency), clinicians use TBS to stratify.
    *   *Low TBS:* Skip LND (Prioritize timing/safety).
    *   *High TBS:* Perform LND (Prioritize specificity) [cite: 11, 12].

#### 3.2.2 Biomarkers as N-Stage Proxies
*   **CA 19-9:** In ICC, elevated CA 19-9 is strongly correlated with LNM. A cutoff (e.g., > 37 U/mL or > 80 U/mL) is often used to trigger a more extensive lymph node search or diagnostic laparoscopy before definitive resection [cite: 11, 13].
*   **Radiomics:** Advanced analysis of MRI/CT textures is emerging as a non-invasive method to predict LNM. By analyzing the "roughness" or heterogeneity of the primary tumor (T-stage features), algorithms can predict N-stage status with increasing accuracy (AUC > 0.80), offering a "virtual biopsy" that improves specificity without the delay of surgical staging [cite: 14, 15, 16].

### 3.3 The "Adequate" Lymphadenectomy
The AJCC 8th edition introduced a requirement for specificity in ICC: a minimum of **6 lymph nodes** must be retrieved to accurately designate a patient as pN0 [cite: 9].
*   **Impact on Timing:** This requirement forces surgeons to spend more time during resection to ensure adequate staging.
*   **Impact on Specificity:** It eliminates the "false N0" phenomenon where patients are understaged simply because nodes weren't sampled. Here, the system explicitly prioritizes specificity over operative speed [cite: 12].

---

## 4. Vascular Invasion: The "Invisible" Variable

Vascular invasion (VI) is the single most critical prognostic factor in liver cancer, yet it sits at the center of the specificity vs. timing conflict because of the difficulty in diagnosing it preoperatively.

### 4.1 Microvascular Invasion (MVI) vs. Macrovascular Invasion
*   **Macrovascular Invasion:** Visible on CT/MRI (invasion of portal vein branches). This is a T4 (or T3b in older systems) finding. It is highly specific and immediately alters treatment (contraindication for transplant).
*   **Microvascular Invasion (MVI):** Only visible under a microscope.
    *   *The Conflict:* MVI is present in 20-30% of small HCCs. Knowing it exists would change the prognosis (specificity). However, discovering it requires removing the tumor.
    *   *The Resolution:* The TNM system (specifically T1a) largely ignores MVI for staging small tumors to prevent "analysis paralysis." If the system required MVI status for all T1 tumors, no patient could be staged pre-operatively [cite: 3, 13, 17].

### 4.2 Preoperative Prediction of MVI
To regain some of the lost specificity without delaying treatment, researchers use **radiogenomics** and **clinical predictors**.
*   **Predictors:** Tumor size > 2 cm, multifocality, non-smooth tumor margins, and arterial peritumoral enhancement on MRI are strong predictors of MVI [cite: 13, 17].
*   **Clinical Utility:** If a patient has a 3 cm tumor (T1b) with radiologic features suggesting MVI, the clinician might opt for a wider resection margin or adjuvant therapy, effectively treating the patient as T2 even if the clinical stage is T1b. This represents a "functional" balance where clinical judgment supplements the rigid TNM definitions [cite: 13].

---

## 5. Comparative Analysis: HCC vs. ICC Staging Strategies

The TNM system applies different "weighting" to specificity and timing depending on the liver cancer subtype.

| Feature | Hepatocellular Carcinoma (HCC) | Intrahepatic Cholangiocarcinoma (ICC) |
| :--- | :--- | :--- |
| **T1 Definition** | **T1a:** $\le$ 2 cm *regardless* of VI.<br>**T1b:** > 2 cm *without* VI. | **T1a:** $\le$ 5 cm *without* VI.<br>**T1b:** > 5 cm *without* VI. |
| **Balance Strategy** | **Prioritizes Timing:** Ignores VI in small tumors to facilitate transplant/ablation. | **Prioritizes Specificity:** VI immediately upstages to T2; size cutoff is larger (5 cm). |
| **N-Stage Approach** | **Passive:** LND not routine; N1 is rare. Staging often relies on imaging (cN0). | **Active:** LND recommended (min. 6 nodes). N1/N2 split (8th Ed) reflects burden. |
| **Vascular Invasion** | Differentiates T1b from T2. | Differentiates T1 from T2. |
| **Key Surrogate** | AFP, Tumor Size. | CA 19-9, Tumor Burden Score. |

**Analysis:**
*   **HCC** staging is designed for **speed and allocation**. Because HCC patients often compete for liver transplants (Milan Criteria), the staging must be rapid and reproducible based on imaging. The "2 cm rule" facilitates this.
*   **ICC** staging is designed for **surgical stratification**. Because transplant is rare for ICC, the focus is on determining which patients will benefit from major hepatectomy. The rigorous N-stage requirements and strict VI penalties reflect a need to avoid futile surgeries (high specificity) [cite: 9, 10].

---

## 6. The Role of Imaging in Balancing the Equation

Imaging (CT/MRI) is the technological bridge that allows the TNM system to function. It provides the "Clinical Stage" (cTNM) which dictates treatment timing, while attempting to approximate the "Pathological Stage" (pTNM) which offers specificity.

### 6.1 LI-RADS and Diagnostic Specificity
For HCC, the **Liver Imaging Reporting and Data System (LI-RADS)** provides the specificity needed to treat without biopsy.
*   **Mechanism:** A LI-RADS 5 lesion is treated as HCC with near 100% specificity.
*   **Impact on TNM:** This allows a cT1a diagnosis to be made with high confidence, enabling immediate treatment (ablation) and bypassing the delay of biopsy. This is a prime example of diagnostic specificity (via imaging criteria) enabling optimized treatment timing [cite: 13, 17].

### 6.2 The "Gap" in N-Staging
Imaging fails to balance the equation for Lymph Nodes.
*   **Sensitivity:** CT/MRI sensitivity for LNM is < 50%.
*   **Consequence:** This forces the reliance on the "Tumor Burden" surrogates discussed in Section 3. The system accepts that cN0 is often inaccurate (low specificity) to avoid delaying surgery for every patient to undergo PET-CT or laparoscopy (treatment timing) [cite: 11, 16].

---

## 7. Limitations and Controversies

### 7.1 The "T1a" Controversy
Critics argue that the AJCC 8th edition's T1a classification ($\le$ 2 cm regardless of VI) oversimplifies the disease.
*   **Argument:** Small tumors with MVI have recurrence rates similar to larger tumors. Ignoring MVI leads to under-staging and potentially undertreatment (e.g., narrow margins).
*   **Counter-Argument:** Preoperative diagnosis of MVI is impossible. Creating a "T1a-MVI" category would be clinically useless for treatment selection (timing) because it could only be assigned retrospectively [cite: 3, 5, 7].

### 7.2 The "N0" Illusion in ICC
In ICC, many patients staged as N0 (no metastasis) simply did not have lymph nodes removed.
*   **Correction:** The 8th edition's recommendation for 6 nodes attempts to fix this. However, adherence is variable.
*   **Result:** A patient may be "timed" for surgery quickly but "specifically" understaged, leading to early recurrence. This remains a major area of imbalance in the system [cite: 9, 12].

---

## 8. Conclusion

In the TNM staging system for liver cancer, the balance between diagnostic specificity and treatment timing is engineered through **size-based thresholds** and **hierarchical staging definitions**.

1.  **For Tumor Burden (T-Stage):** The system prioritizes **treatment timing** for the smallest tumors. The classification of HCC $\le$ 2 cm as T1a *regardless of vascular invasion* is the definitive structural element that prevents diagnostic hurdles (biopsy/resection for MVI) from delaying curative therapy. As tumor burden increases (> 2 cm), the system pivots to prioritize **diagnostic specificity**, requiring the differentiation of vascular invasion (T1b vs. T2) to guide complex surgical decision-making.
2.  **For Lymph Node Metastasis (N-Stage):** The system navigates the poor specificity of imaging by utilizing **surrogate markers of tumor burden** (TBS, CA 19-9, radiomics). These tools allow clinicians to estimate the probability of N1 disease, thereby balancing the risk of futile surgery against the morbidity of routine lymphadenectomy.

Ultimately, the TNM system functions not just as a static classification, but as a dynamic risk-stratification tool. It accepts calculated losses in specificity (e.g., ignoring MVI in T1a) to secure gains in therapeutic efficacy, ensuring that patients with early-stage disease receive timely, life-saving intervention.

---

### References
*   **[cite: 1]** Cancer Research UK. TNM staging for liver cancer.
*   **[cite: 17]** QIMS. Diagnostic imaging features of MVI.
*   **[cite: 11]** J Gastrointest Surg. Predicting lymph node metastasis in intrahepatic cholangiocarcinoma.
*   **[cite: 14]** Frontiers in Oncology. Predicting ISLN pCR.
*   **[cite: 13]** Liver Cancer. Preoperative Prediction of Microvascular Invasion.
*   **[cite: 12]** SPCIR. Predicting Lymph Node Metastasis.
*   **[cite: 5]** Cancer Res Treat. Evaluation of AJCC 8th Edition Staging System for HCC.
*   **[cite: 6]** TNM Classification of Malignant Tumours 8th edition.
*   **[cite: 9]** Chin Clin Oncol. Intrahepatic cholangiocarcinoma: the AJCC/UICC 8th edition updates.
*   **[cite: 3]** Cancer Res Treat. Validation of AJCC 8th Edition.
*   **[cite: 4]** J Surg Oncol. Impact of T and N classification on survival in AJCC 8th edition.
*   **[cite: 7]** PubMed. AJCC 8th edition staging system for HCC.
*   **[cite: 8]** AJCP. Tumor size not small vessel invasion predicts survival.
*   **[cite: 16]** Frontiers in Oncology. Application of radiomics in predicting lymph node metastasis.
*   **[cite: 13]** Liver Cancer. Preoperative Prediction of Microvascular Invasion (MRI).
*   **[cite: 10]** E-EMJ. Predicting lymph node metastasis in intrahepatic cholangiocarcinoma.

**Sources:**
1. [cancerresearchuk.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqrN7cYoeYGSPOsBs-8q9OA9BH8-lzy2vcq7fyFzyM5mGglGycIs7-Jt4-wQRWCBbdzHc0lwr7WDwKUNlAPGnWGgxBrcai3af4mDwKlt7clu_pckg9VW9XKJMMtOGatBUt3gSoTpb_uftjH2bTvV5djXiKt3GWO1mv9jxbzl3T0XXBDA==)
2. [cancer.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEU1n6KZF-Wm4B5Dqs7FEG0Gaw-QqZJgYbhNL_VOKM8wKK8tICscr0Slt2DlhkjGxVyq6qao4IxIzS7DG5RjmMUEKGeRA_huoWspAzny_8DsE_VudbWB9DHblRt9QX2iGlJJQ3fax9jGZv2JmVLdN5-IKGNbfltkGj9TJ4fb8QWj4bQOXbrbDuYrQTykn4XcA==)
3. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdhpz6jh4Qy3pl2Xgss6S95KJSXILRvn9VEpR_sqNFlznWp6hUOap_i1MHtk1dwUEdb8w947DQfbqcwysD6d291x_lvEUF6gw_Q8ESxKV8Sv_EbPEQaBTwyyTEA0lYEKhjpIv8FEvM)
4. [umich.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFV_wB4LEEP4QVifk1GoYwAJ_cCsThaCWJ-Cxn_h0cdlfoAiYBi0U7VIXh0iL-O9jDNx99q-7UdQ6DDjoIDfPSffPPYQgVT3Q5txZa3dS2en9Wi-3vDAPbmFcXeoUM72JiI7LLEVgK7G-VUetyZDrpjlzI6aWX78ya00Fw43LH1hsRCBaWrupFs1Yns9g==)
5. [bvsalud.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1D2rMpbckBeaT_sooR6wVmxCqCdHS4jpup1OifimJaUPWf6qT495sPmd4P9oC220I4I-VUTWDi3T_KlRi2ZIAIt5ZeW-ev1YgaxV-cFtAZ8diXoUm1PswIK0peKcIEETSsgtGWWcDWZMXniy1IRmZ)
6. [mom.gov.az](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwROVCd1j4bF-wVJOtPWFNzPfMvoTBfv-Pyv5glp0C426ewAQdYWCNwvgpb4W0olBGaNY8-6Wh52SLAh_KHwNaqGdB1V38IPjowLvpWt5FYYpMNFaJRO01YPgDX3NPENIu52Vbmjkgm60ZcjlAFPpyOtE6YRXGEmD8ShXfG2b6tNz88arRCly07QE00Ot3Vo3Lx1NUAC5ig1wLnO8_)
7. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9TfI6wZiBUkZZTFGORtfo5UdhOuwGiqymrQJGPi-0Ipwm2Ndiac0Z8yHn_ZGiSD3MAxzHVuJTBOoayBWP-D8YDzBkxoJHRAgkiJ5M2u70jvaMMfUQWxWe_jCFPdYGVQ==)
8. [ovid.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcFFT_e6FcNNgjdaVFxPQvPYfn0L-9cbIriKsMmgWf__z6CqUiT-r5QamK0MbSo1MN7IWltDuSudFJXBeNWakJQXkp0dC7670xRmhAtKUEUeGf2FWDG70AVkgFW1T9plXyBIYiHBcBuOJ90GKWJVihB_eSw9ont3XopZjN0R7UVHHtjKPOqsm74MUeehtfuz9bEHAZv9YwJX8o2J9QUCuWluFaE8wj-WsdDSai)
9. [amegroups.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrAx2qNnVjBisoKH2rGH7olwNUsDCh7UDy4s7PcJd5RloMEGV3wKcJFbwM9ILx_JWhX2zZ1wEjWtJC5XOdbIstMV1WmYK3dvfa-lmO9BZhJYY9Ee22xqiktdxNj58TlbpPj8Do_P8=)
10. [e-emj.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBwEXx3N6guzdrxBucthU2iXxlCmzzUVZOOVQR_hZe3R4q6DMIluGaEeWhlFp6GAJHaDYfd9XuqWvtZreR6np1Ysku7IlVYQOWOwUelFq_nNWWqSc6rkpxRke3Fbwd5C36iA==)
11. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHivqb0fIeY3rMKyyCqwTaMN0KvK3iEaxbf48GpLGD2hEPWKamn-IDfky7SwBFrBkPlPRQZ_d_Eeb_f8eJEL8DbH6PfBXX9GirbEuQJAQdLzxJp4mSmNg6-aO_6CA0ivfO4uEXFYJwjFQ==)
12. [spcir.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErP9Sr9hVy4K1jQAdf_8eiXRj4PFYz_BpEkZDUBlQ3uTGj5ld4GtC1u1mlhYU_jVu5_QQyHSB9PxautoYvhbY5TFojlTSx1i4ZeSM1jKnEW6dixxOqnpzss12VD7z_-CRidz_E-tw0DSh2frLfY1RPBLO_4uiR24stF3VRZu4=)
13. [karger.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzFAjJZZhaxdgAgq4KyJnnhVCF-SEXINXRGwneRnAuO23D6-NmYMWxo0FngacFODL_3au1Sdfc5570DNpKtQNqNo9wQbf5rwgQxwHY7kakyW4c-QIwjgsZhaDNYirPjaycvLK-53q7Ta5JIcd8wa-fYvQMgZ4gOcPrqx2g06L2aw_73ZwnrlDxb5DfPkFkfd-36RwKdbGPfW4z2a68e0z3MDa6)
14. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHm8l6d07V_sLl8A0cEl5ovvCdRJe6DaDwT9wa4DdCXvvkMjaJ63WymOfT59OGFDsijRKH8lk5sHR25dZitBCKW54qhlvSWI33-EGJLTKNiB2fOcmvQBh1ym2AlLnDDg644n5p-sWrmwBlPebYYRZGs7KXdKX0vPd9z-os_qkxkN4riuPRRkoQgaMg2)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMf9V819-976D7vkyCTM0nZ0ItQfOZQByB235wnHSHriXf0cMvVhuYwrvD2UNT4hKi8d8dpSaJYjUf47wock9k7GX1Y6EDkJAwUPTmk5GLZz9Sil1gfuBPzLjCfqqlFHILJ7RUMvJ4ij3sn52oYd3ceVUl7O3w3v_jRSxp1LNGdxm6xQHTG3gDCMEGlj99tHgMGf6mGGwTfcx9CKcsmbOfWybjFIikYDtfrrDr5VcmPHQMH9PYHIcczAyIp5aDptYoRxoO6ccvmtUdxkSMQ1EHN1_7Hv7WpM-f6MJyiVabHgjxJSemPe83dHq3vVFsYPCq_FZAAxA=)
16. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUVHxtnaryDCBvSLSC5aLNe8OiwAk1xGXXQGdIPQEfsMmDwjpv5ewj2yEHzvxunn9Ic2um6m12-876csYYczTPIJeKjhP5of1MiDKPjoAi7ho7Omg1hoQKKzjaNPgGUT5jXmLf0Vz6HYkFJ74OOMhcjWLYGpCi-mc36_ooRN8Zm-9Rl40HLvQ10OLZ)
17. [amegroups.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHw-Ja4YOQv2NAoX5InXfGc6iyUbNxtA8iBGTmjXZdas1Z7hHfj34EwDEbUPjKMYX9hiooxqav12e1caOj2jQ6Xle7JK7w0PFbXgP1_PPNFfd9hAylf0vyT0wECIMLedYKxzUrcxuOBxE=)


## Annotations
Annotation(end_index=5616, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEU1n6KZF-Wm4B5Dqs7FEG0Gaw-QqZJgYbhNL_VOKM8wKK8tICscr0Slt2DlhkjGxVyq6qao4IxIzS7DG5RjmMUEKGeRA_huoWspAzny_8DsE_VudbWB9DHblRt9QX2iGlJJQ3fax9jGZv2JmVLdN5-IKGNbfltkGj9TJ4fb8QWj4bQOXbrbDuYrQTykn4XcA==', start_index=5601)
Annotation(end_index=5616, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdhpz6jh4Qy3pl2Xgss6S95KJSXILRvn9VEpR_sqNFlznWp6hUOap_i1MHtk1dwUEdb8w947DQfbqcwysD6d291x_lvEUF6gw_Q8ESxKV8Sv_EbPEQaBTwyyTEA0lYEKhjpIv8FEvM', start_index=5601)
Annotation(end_index=5616, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqrN7cYoeYGSPOsBs-8q9OA9BH8-lzy2vcq7fyFzyM5mGglGycIs7-Jt4-wQRWCBbdzHc0lwr7WDwKUNlAPGnWGgxBrcai3af4mDwKlt7clu_pckg9VW9XKJMMtOGatBUt3gSoTpb_uftjH2bTvV5djXiKt3GWO1mv9jxbzl3T0XXBDA==', start_index=5601)
Annotation(end_index=6612, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdhpz6jh4Qy3pl2Xgss6S95KJSXILRvn9VEpR_sqNFlznWp6hUOap_i1MHtk1dwUEdb8w947DQfbqcwysD6d291x_lvEUF6gw_Q8ESxKV8Sv_EbPEQaBTwyyTEA0lYEKhjpIv8FEvM', start_index=6600)
Annotation(end_index=6612, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFV_wB4LEEP4QVifk1GoYwAJ_cCsThaCWJ-Cxn_h0cdlfoAiYBi0U7VIXh0iL-O9jDNx99q-7UdQ6DDjoIDfPSffPPYQgVT3Q5txZa3dS2en9Wi-3vDAPbmFcXeoUM72JiI7LLEVgK7G-VUetyZDrpjlzI6aWX78ya00Fw43LH1hsRCBaWrupFs1Yns9g==', start_index=6600)
Annotation(end_index=7003, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1D2rMpbckBeaT_sooR6wVmxCqCdHS4jpup1OifimJaUPWf6qT495sPmd4P9oC220I4I-VUTWDi3T_KlRi2ZIAIt5ZeW-ev1YgaxV-cFtAZ8diXoUm1PswIK0peKcIEETSsgtGWWcDWZMXniy1IRmZ', start_index=6988)
Annotation(end_index=7003, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdhpz6jh4Qy3pl2Xgss6S95KJSXILRvn9VEpR_sqNFlznWp6hUOap_i1MHtk1dwUEdb8w947DQfbqcwysD6d291x_lvEUF6gw_Q8ESxKV8Sv_EbPEQaBTwyyTEA0lYEKhjpIv8FEvM', start_index=6988)
Annotation(end_index=7003, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwROVCd1j4bF-wVJOtPWFNzPfMvoTBfv-Pyv5glp0C426ewAQdYWCNwvgpb4W0olBGaNY8-6Wh52SLAh_KHwNaqGdB1V38IPjowLvpWt5FYYpMNFaJRO01YPgDX3NPENIu52Vbmjkgm60ZcjlAFPpyOtE6YRXGEmD8ShXfG2b6tNz88arRCly07QE00Ot3Vo3Lx1NUAC5ig1wLnO8_', start_index=6988)
Annotation(end_index=7408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1D2rMpbckBeaT_sooR6wVmxCqCdHS4jpup1OifimJaUPWf6qT495sPmd4P9oC220I4I-VUTWDi3T_KlRi2ZIAIt5ZeW-ev1YgaxV-cFtAZ8diXoUm1PswIK0peKcIEETSsgtGWWcDWZMXniy1IRmZ', start_index=7396)
Annotation(end_index=7408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9TfI6wZiBUkZZTFGORtfo5UdhOuwGiqymrQJGPi-0Ipwm2Ndiac0Z8yHn_ZGiSD3MAxzHVuJTBOoayBWP-D8YDzBkxoJHRAgkiJ5M2u70jvaMMfUQWxWe_jCFPdYGVQ==', start_index=7396)
Annotation(end_index=7988, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdhpz6jh4Qy3pl2Xgss6S95KJSXILRvn9VEpR_sqNFlznWp6hUOap_i1MHtk1dwUEdb8w947DQfbqcwysD6d291x_lvEUF6gw_Q8ESxKV8Sv_EbPEQaBTwyyTEA0lYEKhjpIv8FEvM', start_index=7976)
Annotation(end_index=7988, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFV_wB4LEEP4QVifk1GoYwAJ_cCsThaCWJ-Cxn_h0cdlfoAiYBi0U7VIXh0iL-O9jDNx99q-7UdQ6DDjoIDfPSffPPYQgVT3Q5txZa3dS2en9Wi-3vDAPbmFcXeoUM72JiI7LLEVgK7G-VUetyZDrpjlzI6aWX78ya00Fw43LH1hsRCBaWrupFs1Yns9g==', start_index=7976)
Annotation(end_index=8661, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFV_wB4LEEP4QVifk1GoYwAJ_cCsThaCWJ-Cxn_h0cdlfoAiYBi0U7VIXh0iL-O9jDNx99q-7UdQ6DDjoIDfPSffPPYQgVT3Q5txZa3dS2en9Wi-3vDAPbmFcXeoUM72JiI7LLEVgK7G-VUetyZDrpjlzI6aWX78ya00Fw43LH1hsRCBaWrupFs1Yns9g==', start_index=8649)
Annotation(end_index=8661, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcFFT_e6FcNNgjdaVFxPQvPYfn0L-9cbIriKsMmgWf__z6CqUiT-r5QamK0MbSo1MN7IWltDuSudFJXBeNWakJQXkp0dC7670xRmhAtKUEUeGf2FWDG70AVkgFW1T9plXyBIYiHBcBuOJ90GKWJVihB_eSw9ont3XopZjN0R7UVHHtjKPOqsm74MUeehtfuz9bEHAZv9YwJX8o2J9QUCuWluFaE8wj-WsdDSai', start_index=8649)
Annotation(end_index=9018, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBwEXx3N6guzdrxBucthU2iXxlCmzzUVZOOVQR_hZe3R4q6DMIluGaEeWhlFp6GAJHaDYfd9XuqWvtZreR6np1Ysku7IlVYQOWOwUelFq_nNWWqSc6rkpxRke3Fbwd5C36iA==', start_index=9005)
Annotation(end_index=9018, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrAx2qNnVjBisoKH2rGH7olwNUsDCh7UDy4s7PcJd5RloMEGV3wKcJFbwM9ILx_JWhX2zZ1wEjWtJC5XOdbIstMV1WmYK3dvfa-lmO9BZhJYY9Ee22xqiktdxNj58TlbpPj8Do_P8=', start_index=9005)
Annotation(end_index=9436, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBwEXx3N6guzdrxBucthU2iXxlCmzzUVZOOVQR_hZe3R4q6DMIluGaEeWhlFp6GAJHaDYfd9XuqWvtZreR6np1Ysku7IlVYQOWOwUelFq_nNWWqSc6rkpxRke3Fbwd5C36iA==', start_index=9426)
Annotation(end_index=10297, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErP9Sr9hVy4K1jQAdf_8eiXRj4PFYz_BpEkZDUBlQ3uTGj5ld4GtC1u1mlhYU_jVu5_QQyHSB9PxautoYvhbY5TFojlTSx1i4ZeSM1jKnEW6dixxOqnpzss12VD7z_-CRidz_E-tw0DSh2frLfY1RPBLO_4uiR24stF3VRZu4=', start_index=10283)
Annotation(end_index=10297, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHivqb0fIeY3rMKyyCqwTaMN0KvK3iEaxbf48GpLGD2hEPWKamn-IDfky7SwBFrBkPlPRQZ_d_Eeb_f8eJEL8DbH6PfBXX9GirbEuQJAQdLzxJp4mSmNg6-aO_6CA0ivfO4uEXFYJwjFQ==', start_index=10283)
Annotation(end_index=11272, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErP9Sr9hVy4K1jQAdf_8eiXRj4PFYz_BpEkZDUBlQ3uTGj5ld4GtC1u1mlhYU_jVu5_QQyHSB9PxautoYvhbY5TFojlTSx1i4ZeSM1jKnEW6dixxOqnpzss12VD7z_-CRidz_E-tw0DSh2frLfY1RPBLO_4uiR24stF3VRZu4=', start_index=11258)
Annotation(end_index=11272, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHivqb0fIeY3rMKyyCqwTaMN0KvK3iEaxbf48GpLGD2hEPWKamn-IDfky7SwBFrBkPlPRQZ_d_Eeb_f8eJEL8DbH6PfBXX9GirbEuQJAQdLzxJp4mSmNg6-aO_6CA0ivfO4uEXFYJwjFQ==', start_index=11258)
Annotation(end_index=11559, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzFAjJZZhaxdgAgq4KyJnnhVCF-SEXINXRGwneRnAuO23D6-NmYMWxo0FngacFODL_3au1Sdfc5570DNpKtQNqNo9wQbf5rwgQxwHY7kakyW4c-QIwjgsZhaDNYirPjaycvLK-53q7Ta5JIcd8wa-fYvQMgZ4gOcPrqx2g06L2aw_73ZwnrlDxb5DfPkFkfd-36RwKdbGPfW4z2a68e0z3MDa6', start_index=11545)
Annotation(end_index=11559, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHivqb0fIeY3rMKyyCqwTaMN0KvK3iEaxbf48GpLGD2hEPWKamn-IDfky7SwBFrBkPlPRQZ_d_Eeb_f8eJEL8DbH6PfBXX9GirbEuQJAQdLzxJp4mSmNg6-aO_6CA0ivfO4uEXFYJwjFQ==', start_index=11545)
Annotation(end_index=11944, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUVHxtnaryDCBvSLSC5aLNe8OiwAk1xGXXQGdIPQEfsMmDwjpv5ewj2yEHzvxunn9Ic2um6m12-876csYYczTPIJeKjhP5of1MiDKPjoAi7ho7Omg1hoQKKzjaNPgGUT5jXmLf0Vz6HYkFJ74OOMhcjWLYGpCi-mc36_ooRN8Zm-9Rl40HLvQ10OLZ', start_index=11926)
Annotation(end_index=11944, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMf9V819-976D7vkyCTM0nZ0ItQfOZQByB235wnHSHriXf0cMvVhuYwrvD2UNT4hKi8d8dpSaJYjUf47wock9k7GX1Y6EDkJAwUPTmk5GLZz9Sil1gfuBPzLjCfqqlFHILJ7RUMvJ4ij3sn52oYd3ceVUl7O3w3v_jRSxp1LNGdxm6xQHTG3gDCMEGlj99tHgMGf6mGGwTfcx9CKcsmbOfWybjFIikYDtfrrDr5VcmPHQMH9PYHIcczAyIp5aDptYoRxoO6ccvmtUdxkSMQ1EHN1_7Hv7WpM-f6MJyiVabHgjxJSemPe83dHq3vVFsYPCq_FZAAxA=', start_index=11926)
Annotation(end_index=11944, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHm8l6d07V_sLl8A0cEl5ovvCdRJe6DaDwT9wa4DdCXvvkMjaJ63WymOfT59OGFDsijRKH8lk5sHR25dZitBCKW54qhlvSWI33-EGJLTKNiB2fOcmvQBh1ym2AlLnDDg644n5p-sWrmwBlPebYYRZGs7KXdKX0vPd9z-os_qkxkN4riuPRRkoQgaMg2', start_index=11926)
Annotation(end_index=12155, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrAx2qNnVjBisoKH2rGH7olwNUsDCh7UDy4s7PcJd5RloMEGV3wKcJFbwM9ILx_JWhX2zZ1wEjWtJC5XOdbIstMV1WmYK3dvfa-lmO9BZhJYY9Ee22xqiktdxNj58TlbpPj8Do_P8=', start_index=12146)
Annotation(end_index=12503, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErP9Sr9hVy4K1jQAdf_8eiXRj4PFYz_BpEkZDUBlQ3uTGj5ld4GtC1u1mlhYU_jVu5_QQyHSB9PxautoYvhbY5TFojlTSx1i4ZeSM1jKnEW6dixxOqnpzss12VD7z_-CRidz_E-tw0DSh2frLfY1RPBLO_4uiR24stF3VRZu4=', start_index=12493)
Annotation(end_index=13560, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHw-Ja4YOQv2NAoX5InXfGc6iyUbNxtA8iBGTmjXZdas1Z7hHfj34EwDEbUPjKMYX9hiooxqav12e1caOj2jQ6Xle7JK7w0PFbXgP1_PPNFfd9hAylf0vyT0wECIMLedYKxzUrcxuOBxE=', start_index=13543)
Annotation(end_index=13560, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdhpz6jh4Qy3pl2Xgss6S95KJSXILRvn9VEpR_sqNFlznWp6hUOap_i1MHtk1dwUEdb8w947DQfbqcwysD6d291x_lvEUF6gw_Q8ESxKV8Sv_EbPEQaBTwyyTEA0lYEKhjpIv8FEvM', start_index=13543)
Annotation(end_index=13560, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzFAjJZZhaxdgAgq4KyJnnhVCF-SEXINXRGwneRnAuO23D6-NmYMWxo0FngacFODL_3au1Sdfc5570DNpKtQNqNo9wQbf5rwgQxwHY7kakyW4c-QIwjgsZhaDNYirPjaycvLK-53q7Ta5JIcd8wa-fYvQMgZ4gOcPrqx2g06L2aw_73ZwnrlDxb5DfPkFkfd-36RwKdbGPfW4z2a68e0z3MDa6', start_index=13543)
Annotation(end_index=13899, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHw-Ja4YOQv2NAoX5InXfGc6iyUbNxtA8iBGTmjXZdas1Z7hHfj34EwDEbUPjKMYX9hiooxqav12e1caOj2jQ6Xle7JK7w0PFbXgP1_PPNFfd9hAylf0vyT0wECIMLedYKxzUrcxuOBxE=', start_index=13885)
Annotation(end_index=13899, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzFAjJZZhaxdgAgq4KyJnnhVCF-SEXINXRGwneRnAuO23D6-NmYMWxo0FngacFODL_3au1Sdfc5570DNpKtQNqNo9wQbf5rwgQxwHY7kakyW4c-QIwjgsZhaDNYirPjaycvLK-53q7Ta5JIcd8wa-fYvQMgZ4gOcPrqx2g06L2aw_73ZwnrlDxb5DfPkFkfd-36RwKdbGPfW4z2a68e0z3MDa6', start_index=13885)
Annotation(end_index=14263, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzFAjJZZhaxdgAgq4KyJnnhVCF-SEXINXRGwneRnAuO23D6-NmYMWxo0FngacFODL_3au1Sdfc5570DNpKtQNqNo9wQbf5rwgQxwHY7kakyW4c-QIwjgsZhaDNYirPjaycvLK-53q7Ta5JIcd8wa-fYvQMgZ4gOcPrqx2g06L2aw_73ZwnrlDxb5DfPkFkfd-36RwKdbGPfW4z2a68e0z3MDa6', start_index=14253)
Annotation(end_index=15829, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBwEXx3N6guzdrxBucthU2iXxlCmzzUVZOOVQR_hZe3R4q6DMIluGaEeWhlFp6GAJHaDYfd9XuqWvtZreR6np1Ysku7IlVYQOWOwUelFq_nNWWqSc6rkpxRke3Fbwd5C36iA==', start_index=15816)
Annotation(end_index=15829, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrAx2qNnVjBisoKH2rGH7olwNUsDCh7UDy4s7PcJd5RloMEGV3wKcJFbwM9ILx_JWhX2zZ1wEjWtJC5XOdbIstMV1WmYK3dvfa-lmO9BZhJYY9Ee22xqiktdxNj58TlbpPj8Do_P8=', start_index=15816)
Annotation(end_index=16673, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHw-Ja4YOQv2NAoX5InXfGc6iyUbNxtA8iBGTmjXZdas1Z7hHfj34EwDEbUPjKMYX9hiooxqav12e1caOj2jQ6Xle7JK7w0PFbXgP1_PPNFfd9hAylf0vyT0wECIMLedYKxzUrcxuOBxE=', start_index=16659)
Annotation(end_index=16673, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzFAjJZZhaxdgAgq4KyJnnhVCF-SEXINXRGwneRnAuO23D6-NmYMWxo0FngacFODL_3au1Sdfc5570DNpKtQNqNo9wQbf5rwgQxwHY7kakyW4c-QIwjgsZhaDNYirPjaycvLK-53q7Ta5JIcd8wa-fYvQMgZ4gOcPrqx2g06L2aw_73ZwnrlDxb5DfPkFkfd-36RwKdbGPfW4z2a68e0z3MDa6', start_index=16659)
Annotation(end_index=17099, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUVHxtnaryDCBvSLSC5aLNe8OiwAk1xGXXQGdIPQEfsMmDwjpv5ewj2yEHzvxunn9Ic2um6m12-876csYYczTPIJeKjhP5of1MiDKPjoAi7ho7Omg1hoQKKzjaNPgGUT5jXmLf0Vz6HYkFJ74OOMhcjWLYGpCi-mc36_ooRN8Zm-9Rl40HLvQ10OLZ', start_index=17085)
Annotation(end_index=17099, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHivqb0fIeY3rMKyyCqwTaMN0KvK3iEaxbf48GpLGD2hEPWKamn-IDfky7SwBFrBkPlPRQZ_d_Eeb_f8eJEL8DbH6PfBXX9GirbEuQJAQdLzxJp4mSmNg6-aO_6CA0ivfO4uEXFYJwjFQ==', start_index=17085)
Annotation(end_index=17699, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1D2rMpbckBeaT_sooR6wVmxCqCdHS4jpup1OifimJaUPWf6qT495sPmd4P9oC220I4I-VUTWDi3T_KlRi2ZIAIt5ZeW-ev1YgaxV-cFtAZ8diXoUm1PswIK0peKcIEETSsgtGWWcDWZMXniy1IRmZ', start_index=17684)
Annotation(end_index=17699, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdhpz6jh4Qy3pl2Xgss6S95KJSXILRvn9VEpR_sqNFlznWp6hUOap_i1MHtk1dwUEdb8w947DQfbqcwysD6d291x_lvEUF6gw_Q8ESxKV8Sv_EbPEQaBTwyyTEA0lYEKhjpIv8FEvM', start_index=17684)
Annotation(end_index=17699, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9TfI6wZiBUkZZTFGORtfo5UdhOuwGiqymrQJGPi-0Ipwm2Ndiac0Z8yHn_ZGiSD3MAxzHVuJTBOoayBWP-D8YDzBkxoJHRAgkiJ5M2u70jvaMMfUQWxWe_jCFPdYGVQ==', start_index=17684)
Annotation(end_index=18134, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErP9Sr9hVy4K1jQAdf_8eiXRj4PFYz_BpEkZDUBlQ3uTGj5ld4GtC1u1mlhYU_jVu5_QQyHSB9PxautoYvhbY5TFojlTSx1i4ZeSM1jKnEW6dixxOqnpzss12VD7z_-CRidz_E-tw0DSh2frLfY1RPBLO_4uiR24stF3VRZu4=', start_index=18121)
Annotation(end_index=18134, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrAx2qNnVjBisoKH2rGH7olwNUsDCh7UDy4s7PcJd5RloMEGV3wKcJFbwM9ILx_JWhX2zZ1wEjWtJC5XOdbIstMV1WmYK3dvfa-lmO9BZhJYY9Ee22xqiktdxNj58TlbpPj8Do_P8=', start_index=18121)
Annotation(end_index=19574, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGqrN7cYoeYGSPOsBs-8q9OA9BH8-lzy2vcq7fyFzyM5mGglGycIs7-Jt4-wQRWCBbdzHc0lwr7WDwKUNlAPGnWGgxBrcai3af4mDwKlt7clu_pckg9VW9XKJMMtOGatBUt3gSoTpb_uftjH2bTvV5djXiKt3GWO1mv9jxbzl3T0XXBDA==', start_index=19565)
Annotation(end_index=19643, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHw-Ja4YOQv2NAoX5InXfGc6iyUbNxtA8iBGTmjXZdas1Z7hHfj34EwDEbUPjKMYX9hiooxqav12e1caOj2jQ6Xle7JK7w0PFbXgP1_PPNFfd9hAylf0vyT0wECIMLedYKxzUrcxuOBxE=', start_index=19633)
Annotation(end_index=19704, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHivqb0fIeY3rMKyyCqwTaMN0KvK3iEaxbf48GpLGD2hEPWKamn-IDfky7SwBFrBkPlPRQZ_d_Eeb_f8eJEL8DbH6PfBXX9GirbEuQJAQdLzxJp4mSmNg6-aO_6CA0ivfO4uEXFYJwjFQ==', start_index=19694)
Annotation(end_index=19813, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHm8l6d07V_sLl8A0cEl5ovvCdRJe6DaDwT9wa4DdCXvvkMjaJ63WymOfT59OGFDsijRKH8lk5sHR25dZitBCKW54qhlvSWI33-EGJLTKNiB2fOcmvQBh1ym2AlLnDDg644n5p-sWrmwBlPebYYRZGs7KXdKX0vPd9z-os_qkxkN4riuPRRkoQgaMg2', start_index=19803)
Annotation(end_index=19876, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzFAjJZZhaxdgAgq4KyJnnhVCF-SEXINXRGwneRnAuO23D6-NmYMWxo0FngacFODL_3au1Sdfc5570DNpKtQNqNo9wQbf5rwgQxwHY7kakyW4c-QIwjgsZhaDNYirPjaycvLK-53q7Ta5JIcd8wa-fYvQMgZ4gOcPrqx2g06L2aw_73ZwnrlDxb5DfPkFkfd-36RwKdbGPfW4z2a68e0z3MDa6', start_index=19866)
Annotation(end_index=19960, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErP9Sr9hVy4K1jQAdf_8eiXRj4PFYz_BpEkZDUBlQ3uTGj5ld4GtC1u1mlhYU_jVu5_QQyHSB9PxautoYvhbY5TFojlTSx1i4ZeSM1jKnEW6dixxOqnpzss12VD7z_-CRidz_E-tw0DSh2frLfY1RPBLO_4uiR24stF3VRZu4=', start_index=19950)
Annotation(end_index=20019, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1D2rMpbckBeaT_sooR6wVmxCqCdHS4jpup1OifimJaUPWf6qT495sPmd4P9oC220I4I-VUTWDi3T_KlRi2ZIAIt5ZeW-ev1YgaxV-cFtAZ8diXoUm1PswIK0peKcIEETSsgtGWWcDWZMXniy1IRmZ', start_index=20010)
Annotation(end_index=20110, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwROVCd1j4bF-wVJOtPWFNzPfMvoTBfv-Pyv5glp0C426ewAQdYWCNwvgpb4W0olBGaNY8-6Wh52SLAh_KHwNaqGdB1V38IPjowLvpWt5FYYpMNFaJRO01YPgDX3NPENIu52Vbmjkgm60ZcjlAFPpyOtE6YRXGEmD8ShXfG2b6tNz88arRCly07QE00Ot3Vo3Lx1NUAC5ig1wLnO8_', start_index=20101)
Annotation(end_index=20181, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrAx2qNnVjBisoKH2rGH7olwNUsDCh7UDy4s7PcJd5RloMEGV3wKcJFbwM9ILx_JWhX2zZ1wEjWtJC5XOdbIstMV1WmYK3dvfa-lmO9BZhJYY9Ee22xqiktdxNj58TlbpPj8Do_P8=', start_index=20172)
Annotation(end_index=20284, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdhpz6jh4Qy3pl2Xgss6S95KJSXILRvn9VEpR_sqNFlznWp6hUOap_i1MHtk1dwUEdb8w947DQfbqcwysD6d291x_lvEUF6gw_Q8ESxKV8Sv_EbPEQaBTwyyTEA0lYEKhjpIv8FEvM', start_index=20275)
Annotation(end_index=20352, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFV_wB4LEEP4QVifk1GoYwAJ_cCsThaCWJ-Cxn_h0cdlfoAiYBi0U7VIXh0iL-O9jDNx99q-7UdQ6DDjoIDfPSffPPYQgVT3Q5txZa3dS2en9Wi-3vDAPbmFcXeoUM72JiI7LLEVgK7G-VUetyZDrpjlzI6aWX78ya00Fw43LH1hsRCBaWrupFs1Yns9g==', start_index=20343)
Annotation(end_index=20450, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9TfI6wZiBUkZZTFGORtfo5UdhOuwGiqymrQJGPi-0Ipwm2Ndiac0Z8yHn_ZGiSD3MAxzHVuJTBOoayBWP-D8YDzBkxoJHRAgkiJ5M2u70jvaMMfUQWxWe_jCFPdYGVQ==', start_index=20441)
Annotation(end_index=20517, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcFFT_e6FcNNgjdaVFxPQvPYfn0L-9cbIriKsMmgWf__z6CqUiT-r5QamK0MbSo1MN7IWltDuSudFJXBeNWakJQXkp0dC7670xRmhAtKUEUeGf2FWDG70AVkgFW1T9plXyBIYiHBcBuOJ90GKWJVihB_eSw9ont3XopZjN0R7UVHHtjKPOqsm74MUeehtfuz9bEHAZv9YwJX8o2J9QUCuWluFaE8wj-WsdDSai', start_index=20508)
Annotation(end_index=20598, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUVHxtnaryDCBvSLSC5aLNe8OiwAk1xGXXQGdIPQEfsMmDwjpv5ewj2yEHzvxunn9Ic2um6m12-876csYYczTPIJeKjhP5of1MiDKPjoAi7ho7Omg1hoQKKzjaNPgGUT5jXmLf0Vz6HYkFJ74OOMhcjWLYGpCi-mc36_ooRN8Zm-9Rl40HLvQ10OLZ', start_index=20588)
Annotation(end_index=20702, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzFAjJZZhaxdgAgq4KyJnnhVCF-SEXINXRGwneRnAuO23D6-NmYMWxo0FngacFODL_3au1Sdfc5570DNpKtQNqNo9wQbf5rwgQxwHY7kakyW4c-QIwjgsZhaDNYirPjaycvLK-53q7Ta5JIcd8wa-fYvQMgZ4gOcPrqx2g06L2aw_73ZwnrlDxb5DfPkFkfd-36RwKdbGPfW4z2a68e0z3MDa6', start_index=20692)
Annotation(end_index=20792, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBwEXx3N6guzdrxBucthU2iXxlCmzzUVZOOVQR_hZe3R4q6DMIluGaEeWhlFp6GAJHaDYfd9XuqWvtZreR6np1Ysku7IlVYQOWOwUelFq_nNWWqSc6rkpxRke3Fbwd5C36iA==', start_index=20782)

## Sources
