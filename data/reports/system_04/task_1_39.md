# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** bc915e0f | **Time:** 404.40s | **Cost:** $1.57186
--------------------------------------------------------------------------------

# Preclinical Evaluation of Anti-Tumor Drugs: Balancing Therapeutic Index and Toxicity Thresholds

### Key Points
*   **Therapeutic Index (TI) Definition:** The TI serves as a quantitative ratio comparing the toxic dose to the effective dose (e.g., \(TD_{50}/ED_{50}\)). In oncology, unlike other therapeutic areas, a narrow TI is often accepted due to the life-threatening nature of the disease, though recent regulatory shifts aim to widen this window.
*   **In Vitro Selectivity:** Initial screening relies on the Selectivity Index (SI), calculated as the ratio of cytotoxicity in normal cells to cancer cells (\(CC_{50}/IC_{50}\)). An SI > 3 is generally considered a baseline for selectivity, while an SI > 10 represents a highly promising safety profile for further development.
*   **In Vivo Toxicity Thresholds:** While traditional protocols allowed for up to 20% body weight loss (BWL) in rodent models, modern guidelines (e.g., NC3Rs) recommend a refined limit of 10% BWL. This refinement improves animal welfare without compromising the scientific validity of Maximum Tolerated Dose (MTD) determination.
*   **Regulatory Paradigm Shift:** The FDA’s "Project Optimus" marks a transition from identifying the Maximum Tolerated Dose (MTD) to the Optimal Biological Dose (OBD). This initiative compels sponsors to evaluate multiple dose levels preclinically and clinically to maximize efficacy while minimizing chronic toxicity, particularly for targeted therapies and immunotherapies.
*   **Translational Scaling:** Body Surface Area (BSA) conversion remains the standard for estimating human equivalent doses for small molecules, predicting clinical doses within a 3-fold range for approximately 85% of agents. However, this method is less predictive for biologics and antibody-drug conjugates (ADCs).

---

## 1. Introduction

The preclinical evaluation of anti-tumor drugs is a rigorous, multi-stage process designed to identify compounds that possess a favorable balance between antineoplastic efficacy and host toxicity. This balance is quantified as the Therapeutic Index (TI), a critical parameter that defines the margin of safety for a pharmaceutical agent. In the context of oncology, where traditional cytotoxic agents often target fundamental cellular mechanisms shared by both malignant and healthy tissues, achieving a sufficient TI is historically challenging.

The development pipeline has evolved from empirical screening of cytotoxic compounds to the rational design of targeted therapies. This evolution has necessitated a re-evaluation of how TI is assessed. The traditional "nanomolar rule"—which prioritized compounds solely based on high *in vitro* potency (low \(IC_{50}\))—has been criticized for failing to account for pharmacokinetic (PK) properties, off-target effects, and *in vivo* toxicity profiles [cite: 1, 2]. Consequently, modern preclinical frameworks integrate complex *in vitro* assays, sophisticated *in vivo* models, and computational translation strategies to predict the clinical therapeutic window more accurately.

Furthermore, regulatory bodies, particularly the FDA through Project Optimus and the International Council for Harmonisation (ICH) via the S9 guidelines, have fundamentally altered the objectives of preclinical dose-finding. The focus is shifting from solely defining the Maximum Tolerated Dose (MTD) toward identifying an Optimal Biological Dose (OBD) that maintains efficacy while reducing long-term toxicity [cite: 3, 4]. This report provides an exhaustive analysis of the methodologies used to balance efficacy and toxicity, the thresholds employed to make go/no-go decisions, and the translational strategies that bridge the gap between the laboratory and the clinic.

---

## 2. In Vitro Evaluation: Establishing the Selectivity Index

Before a compound enters animal testing, it must undergo rigorous *in vitro* profiling to establish its baseline potency against tumor cells and its safety profile against non-malignant cells. This stage is critical for "triaging" compounds to prevent the unnecessary use of animals for agents with poor safety margins [cite: 5].

### 2.1 The Selectivity Index (SI)
The primary metric for *in vitro* TI is the Selectivity Index (SI). The SI is calculated as the ratio of the concentration required to kill 50% of normal cells (\(CC_{50}\) or \(LC_{50}\)) to the concentration required to inhibit 50% of cancer cells (\(IC_{50}\)) [cite: 6, 7, 8].

\[
SI = \frac{IC_{50} \text{ (Normal Cells)}}{IC_{50} \text{ (Cancer Cells)}}
\]

#### 2.1.1 Thresholds for Selectivity
There is no single global standard for a "good" SI, but literature and industrial practices have established functional thresholds used for decision-making:
*   **SI < 1:** Indicates non-selective toxicity; the compound kills healthy cells at concentrations equal to or lower than those required to kill cancer cells. Such compounds are typically discarded [cite: 7, 9].
*   **SI ≥ 3:** Often cited as the minimum threshold for classifying a compound as "selective." Compounds with an SI > 3 are considered to have a potential therapeutic window warranting further investigation [cite: 10, 11, 12].
*   **SI > 10:** Considered "highly selective." Compounds achieving this margin are viewed as having a favorable safety profile and are prioritized for *in vivo* studies [cite: 13, 14, 15].

**Table 1: Interpretation of In Vitro Selectivity Index (SI) Values**

| SI Value | Classification | Implication for Drug Development |
| :--- | :--- | :--- |
| < 1.0 | Non-selective | High risk of toxicity; typically halted (No-Go). |
| 1.0 – 2.0 | Low Selectivity | Moderate toxicity risk; requires structural optimization. |
| ≥ 3.0 | Selective | Minimum threshold for advancing to mechanism studies [cite: 10, 12]. |
| > 10.0 | Highly Selective | Strong candidate for *in vivo* efficacy/toxicity testing [cite: 13, 15]. |

### 2.2 Limitations of the "Nanomolar Rule"
Historically, drug discovery programs prioritized "hits" with nanomolar potency (e.g., \(IC_{50} < 100 \text{ nM}\)). This approach, known as the "nanomolar rule," assumes that higher potency allows for lower dosing, thereby reducing toxicity. However, retrospective analyses have shown that nanomolar potency *in vitro* does not necessarily correlate with clinical efficacy or safety [cite: 1].
*   **Failure of Correlation:** Many approved chemotherapeutics (e.g., alkylating agents, antimetabolites) possess only micromolar potency but are clinically effective due to favorable pharmacokinetic profiles or accumulation in tumor tissues [cite: 1].
*   **PK/PD Disconnect:** A compound with nanomolar potency may have poor solubility, rapid metabolic clearance, or high protein binding, rendering it ineffective *in vivo* despite promising *in vitro* data [cite: 2, 16]. Therefore, TI assessment must integrate potency with physicochemical properties (ADME) rather than relying on \(IC_{50}\) values alone.

### 2.3 Advanced In Vitro Models
To improve the predictive value of TI assessments, researchers are moving beyond 2D monolayer cultures.
*   **NCI-60 Panel:** The National Cancer Institute’s panel of 60 human tumor cell lines allows for the evaluation of antiproliferative activity across diverse histologies. The COMPARE algorithm analyzes these patterns to predict mechanisms of action and potential cross-resistance [cite: 1, 17].
*   **3D Spheroids and Organoids:** 3D models better recapitulate the tumor microenvironment, including gradients of oxygen, pH, and drug penetration. These models often show higher drug resistance than 2D cultures, providing a more realistic estimation of the effective concentration required *in vivo*, thereby refining the TI calculation before animal testing [cite: 18, 19].

---

## 3. In Vivo Evaluation: Balancing Efficacy and Toxicity

Once a compound demonstrates a favorable *in vitro* SI, it advances to *in vivo* testing. Here, the TI is defined by the relationship between the Minimum Effective Dose (MED) and the Maximum Tolerated Dose (MTD).

### 3.1 Defining the Maximum Tolerated Dose (MTD)
The MTD is traditionally defined as the highest dose of a drug that does not cause unacceptable side effects or death. In preclinical rodent studies, this is rigorously quantified using specific endpoints.

#### 3.1.1 Body Weight Loss (BWL) Thresholds
Body weight loss is the most common objective surrogate for toxicity in short-term studies.
*   **Traditional Limits:** Historically, a BWL of up to 20% was often permitted before euthanasia was required.
*   **Refined NC3Rs Guidelines:** Recent large-scale collaborations involving pharmaceutical companies and the NC3Rs (National Centre for the Replacement, Refinement and Reduction of Animals in Research) have demonstrated that a **10% BWL limit** is scientifically sufficient to determine MTD in rats and dogs [cite: 20, 21].
    *   **Scientific Justification:** Data from 151 compounds showed that exceeding 10% BWL rarely provides additional scientific value and is almost always associated with other overt clinical signs of toxicity.
    *   **Welfare Impact:** Adopting the 10% threshold significantly refines animal welfare without compromising the ability to detect dose-limiting toxicities [cite: 21, 22].

**Table 2: Refined Toxicity Thresholds for MTD Determination (NC3Rs Recommendations)**

| Species | Traditional BWL Limit | Recommended Refined BWL Limit | Rationale |
| :--- | :--- | :--- | :--- |
| Rat | ~20% | **10%** | BWL >10% correlates strongly with other adverse clinical signs; exceeding this limit offers little additional data [cite: 20, 21]. |
| Dog | ~15-20% | **10%** | Similar to rats, 10% is sufficient for decision-making regarding dose escalation [cite: 20]. |
| Non-Human Primate | ~10-15% | **6%** | NHPs are highly sensitive; 6% BWL is sufficient to identify MTD [cite: 21, 22]. |

#### 3.1.2 Other Toxicity Endpoints
Beyond BWL, toxicity is assessed via:
*   **Clinical Signs:** Piloerection, lethargy, abnormal posture.
*   **Hematology/Biochemistry:** Myelosuppression (neutropenia, thrombocytopenia) is a common dose-limiting toxicity (DLT) for cytotoxic drugs [cite: 23].
*   **Organ Toxicity:** Histopathological evaluation of major organs (liver, kidney, heart) to identify target organ toxicity [cite: 24].

### 3.2 Efficacy Models and TI Calculation
Efficacy is typically measured in tumor xenograft models (immunodeficient mice with human tumors) or syngeneic models (immunocompetent mice with murine tumors).
*   **Endpoints:** Tumor Growth Inhibition (TGI) relative to control, or tumor regression.
*   **In Vivo TI Calculation:**
    \[
    TI_{in\ vivo} = \frac{MTD}{MED} \quad \text{or} \quad \frac{TD_{50}}{ED_{50}}
    \]
    *   **MTD:** The dose causing ~10% BWL or other defined toxicity limits.
    *   **MED:** The lowest dose producing a statistically significant TGI (often defined as >50% inhibition) [cite: 25, 26].

A "wide" therapeutic index in preclinical models (e.g., TI > 2-5) suggests a safer clinical profile, whereas a TI < 1 implies that effective doses are likely to be toxic [cite: 25].

---

## 4. Translational Dose Prediction

Bridging the gap from preclinical data to First-in-Human (FIH) trials requires robust scaling methods to predict safe starting doses and potential therapeutic ranges.

### 4.1 Body Surface Area (BSA) Conversion
For small molecule oncology drugs, allometric scaling based on Body Surface Area (BSA) is the standard method for interspecies dose conversion.
*   **Methodology:** Animal doses (mg/kg) are converted to Human Equivalent Doses (HED) (mg/m²) using correction factors (e.g., divide mouse mg/kg dose by 12.3 to get human mg/kg, or multiply by 3 to get mg/m²) [cite: 27, 28].
*   **Predictive Accuracy:** Retrospective analysis of 90 approved small-molecule oncology drugs indicates that BSA-corrected mouse efficacious doses predict the human clinical dose range within a **3-fold margin for approximately 85.6% of compounds** [cite: 29].
*   **Limitations:** BSA scaling performs poorly for monoclonal antibodies (mAbs) and Antibody-Drug Conjugates (ADCs), where prediction accuracy drops significantly (only ~16.7% within 3-fold for antibodies) [cite: 29]. For these large molecules, body weight-based scaling or physiologically based pharmacokinetic (PBPK) modeling is preferred.

### 4.2 ICH S9 Guidelines: Specifics for Anticancer Pharmaceuticals
The International Council for Harmonisation (ICH) S9 guideline governs the nonclinical evaluation of anticancer pharmaceuticals intended for patients with advanced disease.
*   **Starting Dose:** Unlike healthy volunteer trials (which use 1/10th the NOAEL), oncology trials in patients often start at **1/10th of the Severely Toxic Dose in 10% of rodents (STD10)** or 1/6th of the Highest Non-Severely Toxic Dose (HNSTD) in non-rodents [cite: 24, 27, 30].
*   **Rationale:** This aggressive starting dose is permitted because the target population (advanced cancer patients) has a higher tolerance for toxicity in exchange for potential therapeutic benefit, and the risk-benefit analysis differs from healthy volunteers [cite: 31].

---

## 5. Regulatory Evolution: From MTD to Project Optimus

A significant paradigm shift is currently underway in oncology drug development, driven by the US FDA's "Project Optimus."

### 5.1 The Traditional MTD Paradigm
Historically, oncology drug development operated on the "more is better" philosophy derived from cytotoxic chemotherapy. The goal was to dose as close to the MTD as possible to maximize tumor cell kill. Phase I trials were designed solely to find the MTD, which then became the Recommended Phase 2 Dose (RP2D) [cite: 3, 32].

### 5.2 The Project Optimus Paradigm (OBD)
With the rise of targeted therapies (kinase inhibitors) and immunotherapies, the dose-response relationship is often not linear. These drugs may reach a plateau of efficacy at doses well below the MTD. Dosing at the MTD for these agents often results in unnecessary chronic toxicity without additional efficacy [cite: 4, 33].
*   **Optimal Biological Dose (OBD):** Project Optimus requires sponsors to characterize the dose-response relationship more fully. The goal is to identify the OBD—the lowest dose that provides maximum efficacy—rather than the highest tolerable dose [cite: 3, 34].
*   **Impact on Preclinical Evaluation:**
    *   Sponsors must now conduct more robust dose-ranging studies *in vivo* to define the MED and the plateau of efficacy.
    *   Preclinical data must support the selection of multiple dose levels for evaluation in early clinical trials, rather than a single escalation to MTD [cite: 32, 33].

---

## 6. Strategies for Optimizing Therapeutic Index

When preclinical evaluation reveals a narrow TI, several strategies are employed to widen the window before clinical entry.

### 6.1 Medicinal Chemistry and Lead Optimization
*   **Structure-Activity Relationship (SAR):** Iterative chemical modifications are used to improve potency (lowering ED50) or reduce off-target binding (raising TD50). For example, optimizing lipophilicity can improve tumor penetration while reducing CNS toxicity [cite: 35, 36].
*   **Selectivity Enhancement:** Designing compounds that target mutant proteins specific to cancer cells (e.g., mutant BRAF or EGFR) rather than wild-type proteins significantly improves the SI [cite: 37].

### 6.2 Antibody-Drug Conjugates (ADCs)
ADCs represent a structural strategy to improve TI by delivering potent cytotoxic payloads directly to cells expressing specific tumor antigens.
*   **Mechanism:** The antibody targets the tumor, while the linker ensures stability in circulation (reducing systemic toxicity) and release of the payload inside the cancer cell [cite: 38].
*   **TI Improvement:** ADCs can lower the MED significantly compared to the free payload, thereby widening the TI. However, they introduce new toxicity concerns (e.g., "bystander effect" or off-target uptake by the liver) which must be evaluated in antigen-expressing animal models [cite: 38, 39].

### 6.3 Click Chemistry and Prodrugs
Novel approaches like "Click Activated Protodrugs Against Cancer" (CAPAC) utilize bio-orthogonal chemistry to activate drugs only at the tumor site.
*   **Method:** An activator is targeted to the tumor, and a prodrug is administered systemically. The drug is activated only where the activator is present.
*   **Result:** This decouples systemic exposure from tumor exposure, allowing for supratherapeutic concentrations at the tumor site with minimal systemic toxicity, effectively expanding the TI [cite: 23].

---

## 7. Conclusion

The preclinical evaluation of anti-tumor drugs is a complex exercise in risk management, requiring a continuous balancing act between therapeutic potential and physiological cost. The assessment begins *in vitro* with the determination of the Selectivity Index, where a threshold of **SI > 3** serves as a standard gatekeeper for advancement. *In vivo*, the focus shifts to defining the therapeutic window between the Minimum Effective Dose (MED) and the Maximum Tolerated Dose (MTD), with modern ethical standards enforcing a **10% body weight loss limit** to refine toxicity data.

The field is currently undergoing a major transformation driven by **Project Optimus**, moving away from the historical reliance on MTD towards the identification of the **Optimal Biological Dose (OBD)**. This shift necessitates more granular preclinical data regarding dose-response relationships, ensuring that patients receive doses that are effective without being unnecessarily toxic. By integrating these rigorous evaluation models with translational scaling methods like BSA conversion and adhering to ICH S9 guidelines, researchers can maximize the probability of clinical success while safeguarding patient safety.

### References
[cite: 6] ResearchGate. (n.d.). Concept of the in vitro therapeutic index.
[cite: 1] Johnson, J. I., et al. (2001). Relationships between drug activity in NCI preclinical in vitro and in vivo models and early clinical trials. *British Journal of Cancer*.
[cite: 40] Evaluation of CDK9 inhibition in preclinical models. (2022). *Cancer Research*.
[cite: 25] Therapeutic index in drug development. (2024). *MDPI*.
[cite: 38] Colombo, R., & Rich, J. R. (2023). Re-evaluating the therapeutic index of ADCs. *Cancer Cell*.
[cite: 26] Pharmacology Canada. (n.d.). Therapeutic Index Definition.
[cite: 41] Preclinical to clinical translation in oncology. (2024). *PMC*.
[cite: 37] Comparison of steady-state concentration and IC50. (2020). *PMC*.
[cite: 42] Dosage optimization in oncology. (2025). *PMC*.
[cite: 24] ICH S9 Nonclinical evaluation for anticancer pharmaceuticals. (2010). *EMA*.
[cite: 43] FDA Guidance. (2020). S9 Nonclinical Evaluation for Anticancer Pharmaceuticals.
[cite: 39] ICH S9 Q&A. (2018). *ICH*.
[cite: 20] NC3Rs. (2013). Recommendations for upper bodyweight loss limits.
[cite: 21] Chapman, K., et al. (2013). A Global Pharmaceutical Company Initiative: An Evidence-Based Approach to Define the Upper Limit of Body Weight Loss. *Regulatory Toxicology and Pharmacology*.
[cite: 5] Noble Life Sciences. (n.d.). In vitro tumor cell model systems.
[cite: 1] Limitations of the nanomolar rule. (2012). *JPET*.
[cite: 18] 3D cell culture models in preclinical testing. (2023). *PMC*.
[cite: 19] Preclinical models for anticancer therapy. (2017). *PMC*.
[cite: 10] Selectivity index values in anticancer compounds. (2017). *ResearchGate*.
[cite: 17] NCI-60 Screen and COMPARE algorithm. (n.d.). *DCTD*.
[cite: 35] Optimization of natural leads. (2015). *PMC*.
[cite: 29] Correlation between mouse and human doses. (2022). *PMC*.
[cite: 27] Estimating first-in-human dose. (2013). *Hrcak*.
[cite: 20] NC3Rs Factsheet. (2022). Bodyweight loss recommendations.
[cite: 29] BSA conversion accuracy. (2022). *PMC*.
[cite: 3] Veristat. (n.d.). Project Optimus Explained.
[cite: 4] Caidya. (n.d.). Strategies for Dose Selection.
[cite: 34] Fortrea. (2025). Understanding oncology asset and defining possibilities.
[cite: 32] Applied Clinical Trials. (2024). FDA Project Optimus.
[cite: 23] Click chemistry for therapeutic index expansion. (2025). *PMC*.
[cite: 7] Selectivity index calculation. (2023). *ResearchGate*.
[cite: 8] Pinostrobin anticancer activity. (2023). *PMC*.
[cite: 13] Selectivity index interpretation. (2024). *Frontiers*.
[cite: 14] Antimicrobial activity and selectivity index. (2025). *ResearchGate*.
[cite: 2] The nanomolar rule in drug discovery. (2012). *PubMed*.
[cite: 12] Selectivity index of plant extracts. (2019). *PMC*.

**Sources:**
1. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExMsEggLea7SPeX8Knvds8I8xJhlg3C9a9xdXjZru8ad-FsFpTqzu78pl7JejgDICGNf_SaOnsRRhThV0ed7HbSrOrDJfxrEo9Dv0KRgtHyTXY8nuy6Dfjm71Q28YazfKe09w8cQg=)
2. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWN5ayJDEOz9_-P0TBze67RGd_dP1LMHxLh2vqIjjWZxfHUjiYrOHd8Zhw4zNC14nM-5R-IPPbBtVx98ZpKK-IZFCC74ZIe3nTs7Qsi4_UBoMFBwIKcbNNN783I_Tf)
3. [veristat.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7cKVOvEXM6G6IqoZ9T7J902ZL2vFnp_O3h-AWaVAPcBJX-ishthvpXevWlAAlKb6bpyOaEJebdBs7ZBrroWNJPvfB3AwM1JJ1dhEJRjmp57e1OswdidlLyGdUfLyG4jvQ8eIyDMA_Vf7FUxTdK46joupW2LAKclWVrJbCH3b7yVIGck6WZMjtuGhjuge6gd9heS3ABQ1z5_B063GtCzw3g3vdQgBwLqVHt7cpLQVMKsg=)
4. [caidya.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqIDROLVYaxNmWeqXPWdtYzj-9MWfO-miV3SI0sRpr17ge5QTadojv3UpFMVfDvaHU70RZhNE0wweCDJENQenh48qp9rZeXMCdiCdyqzuviWhIvO-Gk8oTVntDvftJowQT9HRAw72JXIA7)
5. [noblelifesci.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_bCXOa2EcTmgLTFIG-4HJoWzZ-R4YzxZwVwBZNMLrdin-9CN7sNyaiw9KHK4Y-23aUlgIS7C0RsIbHPUmD3tQxYoAHT6BSbTNAavIGpqIBm-NfmrYsqyMiAFbjr0K4f9SRn9DzJA1yL8UACgxdKe3zELl6hhJYS_dAT-YOr0cvcMAfJIoQ1gdRd31Ku_GC_jbx6FdfsX1DaZ2_Q==)
6. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-JuOIGGb7AjEKQ67A9HQig5A-w2-rJCmE0g5c05Jl9uooEHULueLR0jCB4ROtuZDyQ_CuQtjQHnixSEOSghTDZ7r_wSVNZOHdpQA_0vQEKzb5TPhkAnZVN11JY94xXvBzJ_jsJ9u8eIoa4NbTPkLw9NvJ35336iWhKjbg-uuzoB_jVKut2DfdfY4cbc6PwIWRde7Hs31tOq9mVtJq4N-naQIjOkXFBBBcC9J4lxQOX18ZXcO2je8lww==)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRUyFSgwKOlnbDnvWxYAKBuvf4qFIOPlz8tpjgKf1y1r_9s7H4KKbUmERwpXp4yOo3xXS8QV_KOZnejRjU1guf9YVpNBr6d7ntKw0IYoIVuPoG7csRUwFvFvolhatvHguLIS4eMURfeVqEWnrf3-6KKG4cRCk3R0RCdP4M8JZytYs0tV9sHRe7CbcigX3kpEbx69-m9dd9iSUc1rUw09MszyNVnEvhL-lrG1Yu5Ddjkj07-e21fjnEin4KfXaSPg==)
8. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjje6t6ex1CCGCA3srEZApI_K4U5TQ_2n52V5zMFTg2K1SermfMsq8x7fd8Mndu96MT8t1ucWb1kNyBYXp1KzEvCAeZF9CxTB-G2-d3s2NhtEf1FibTO60q7LE5DmrKerQ_VFW_YHS)
9. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6Ell0WskP5AzhMLK4QzsCZrSqiwYVRCnIYmUjfy3HzHRYbRfgKSYnvN1Q-seE_9lzSUGk8exGd4nm_wWUJHED_ae6WIrlNZefpNANndIT6WdM6lL8MkEV0EfoYCc=)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsNuHHpL6RU_4lk7q1FAkAxexscXiuONeIBu5JvWr-6gtOAYa-4fXtZkY-4fBMLE232p8V5-Mx0clcN3vdUiWuf0n3GUUm-IM8JoMkFIOhfVr9oWIs8Ca9ciYXnYkg03pLgDagHzkO-m-Dw6p7glP_UXu1rvmwVPsH-_vUXIPGDcA3FJCPqFzpPS_LkXTbnbwEbPuPGRTxq3E_yEOo6c9Utg9f2W_s9IWtTykYAQ==)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLUyrdwIT9NqXO8h5DB7JL1t6NrieA6K17kXziXQJwtgfSSpDYWToZvhFShrguz_KR7RFC3lVi7ikniB1tM2N5ZWG462gY37p3Ni6sRu20dbKrrOaDPXkhq9Y3jzPiqnZ_fytSBnJwVVpIyDPfLtBWiWqd9MzuLmxJLTyciAn999GAzvz-WzDg1kNkhxhmBjqGMAiXCk_44cOwb_ucARkUyXRUpcDgXFh1dEU=)
12. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBsXUwXK3KMRNYFmYSBv9fPC5KeQBAOqEokoYU6LaQk6FXuP4shJR8QFZoSvBln56P5khza4I9AD6he9TCFlXiYLd6xmqLx4-1ZJWY-GTuAMPmlSs6Lxh72fWW01wYVeFwd8GL7-8=)
13. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXsGHCnbQqvwEpa7r7ADJvSNaF6MghzYCOjhVLGp3CpB6AH7M_4EL5WFaeWNqrSfEVu27UJ-36e6dqczTEzobTlFaY2hy1WySWMDAW0BQIFiFpxFDiKJsbWQfpMrFCgWXvwUq5qIatT16z5gv8rJVhFoJ8I-n1ZtLk-jckPWbPgsfPf4OJCf2jH8p1GYBfEg==)
14. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0WsnYyEurtrMVhP5doP7T8GIFgAlYoJeuerSlxDZQG8YRgKP-YtAT2Fq9AmWco68GZagm23052QZ0RU7W84uZf0ZbMhjMCZ9Hx0bQd2Xu56zYbtcl0o27vjiIqVEDwCjNlOHD4ofXZo15osnmVrMhwDtQjPYaFbpXHqFx4I9_zjKIIZwF_ATbLtmEDPHGNFvd_FmcNqaDsSruZgx2Xb41df7BP4G9R0wUqD35zKQ-yzTdg9_vB84vfv65sQ_XYKZj8FhxLwuvowbxt_OJqCZhlqy_qvUkEk2jED5roiIV4VwShITzIA5YJ2TKC1BxJnOV7uRmbD8S)
15. [escholarship.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGV1VBqZ6dpaalLz0e_IQAGWqU-Vay1mWL1C0dCyclvU6Ab_clirGNKFNdwx79MXjDZx0FJjjA3KfAQud9ntabtwrzAH7dJs2UuaiWOUQEShdSUR2vYBiIWKxxbjcgNRuVFN5xdxI0o2YG2vZICzFQAL1Vn-dxM04q_3w7WIaoRUCmbTf5Zh_i0EfptQtm6i2SZVUTauRyXCKA=)
16. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFU6Uv0EmY-iVr2256ZRmcEZJo2kwbGUBgP8pJX9LUrUjlp7UB415vTIKSyW4tvoVxZ9bywZNMvl6LbygeAnzZpGvf1PpWFY7x2j8SKY-LB0f1hakgE5gmJ4wd7ilJ6)
17. [cancer.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEQZGfQG-HQG7l3Cj0x9FFjzcFVLOPR_tUWt7uZwAk3jm1zVBmvxyvFSA_X5cjs1W-17xuTxEVH8M6_FnPYtIIS5jFUKkCi4LYAtp8B0PakVa_lIR87UBkXzB34CqsO3bHXXck9whVa9ztum6LzWlHyg==)
18. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcfRZtU6dn9yUJX6HesLRbnUxrzOeTTglvTd4FtB1z06fQhuLZJa-XBZC4uxZcoQwtvrYBrGw50VSwQ7HZD9xmcFgsEwmViX0ZKEb0mvIXBooeHoJdn0PKO0YydKcEXV8Ws4n_VJzb)
19. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhIt4ZpbpZjA96ZfnFxFnmvTgoCnuEcT21QXmp3_9ic_eX38arD0LGxutZZw7xZ1vnNYGapl9wXjAhh1ipRkdUYU_im-K37rFdqBMSlZfX383eOHO3D1jfPSoneQfn8UVdbGiFsVY=)
20. [nc3rs.org.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG27xoNdgf_4ZVvoNQy6QwXKs4WvaVhwFyWG1-X7CKDNTEpd8jp0p8a3AuVIdRP5EE5YHnRkg9XNcbrsb8xYkq8KLkVkXzs80PAHQUtxBzUOLVENsSqI4DnAGBvj2Bq5gPESPQHcnUHL-47P3BYPBuxE3oJ_Z57huXVJzryVyRA_ovHfvwwi-scAhOrGVAemaKtLoP2rso2ZMD0L-1cz4Cf34nF3bVZNA==)
21. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs5mQSNrD-DXPUhVZ42XQOh7lGz2UzSCuwbfAJ9L4dv2ShyDzgfqLo3_WT-HKq4GycxUA8S9m5unHxhkcDDaXOSUt0GK7ge4sL3tVBX6GvcfDrDwgrg8-of83F7-Eb787RRGP1jHOUVdnKiKw9Flhi2FQwk9tSo_nT9dJOQa4mdNYF5yKykjYb1tnr9yhvVzIsz3jB-HOJ3JzcLX0GgaSaeYemo9BnrjuNTL5qbjKY9qYvmYkLXt-XlJZRkJbSFcpYXss4RmFq94aOBCrxy5g8qLI-xet3kQcAPSpS8kkqEUjNduIYGgKLRtxVdGqk3wlgnsSDP38zp_uzhg==)
22. [nc3rs.org.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEs_eCh0PaONu6CqeT_NK8F1T9y1Ke-vmb-UDtViwUuGOn-2NfiMzL6zbu-uLIqdge4Q04S8SK3St-p4oRmzC27wnvnH1oDrvF3cCsndhlv3Cug2cMrtrV6SfgkKlQbe8QY6gVSlGPJoQdVA0w=)
23. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyjXCK8e0okuj8667zBDwcTEwOcPi9vliHJ4UuVvimoUVvWzBZ10Y-JQHGZvic2c5wBrQtv10G8FCbMansla0XfNzZUfW6mvC7gCWsoeObxpYSxz1S7LaQ00gRiNLzL2eCk4s2rRhP)
24. [europa.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhd93EsaumLtaPHqBdookZ1NQO2KyMSOSL4HgHSs15IZKqwINWIgUGc6IPIrfNoS6nvuSZBNQLUCUA605GLpuMQjNdjxWBF66D9NSoDEdhIK3_QM46Xlrkg4sM6A2EavLV7QGYQZSRLWOGeRnM_qPwCDSwOTfMtmFvoIVcQvpI_1H4i0X12XdS6OGED95_2c-R7FUb4bZ4cs9XysWZmuv9)
25. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVXUj-SD32tOuTuxmPjUP5gLaphOV67edewzaoGrv_eI5R9SOHKBSR5tEWkNhwerB2gGLr_B7GOjhmy1rzTWo4JPRcCwdFSyAEJNKz12uk7G2QIL8Q9ztRVjYqcQ==)
26. [pharmacologycanada.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXciRt_-zghj-P9U5C9RP7H1imXrQ6I5jm4hDquaR7S5cPpwqexxSTsJAIo46YabIRQ2XGHb10F1U8cox3FZtgZMLI04qEzFGJ_cEGfPsY6WCBFWo5_yNQ06Xaiwaj-2AqtBH-0A==)
27. [srce.hr](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7-TZapdD8mINavlOhglSeQIZ-i-mSSDs020093lCPknYEYwV-r2AukvPr-XJAOGxOqGHicjzq-5OsBsRFUizyNoQQFxtSzoHOXjiS-gEgdEt_UisgAg==)
28. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKgoCKAQMHL3I51N3UpzYmVHPvCSi0MsSvPrqG4rvNE_orh1eaDAlH4oIAbfadyaHO8OFrtvOD9Erl3KMmMAZNdVOB_eDBBfYUXFwX243JnEuJssErr3qTNiUoP46h)
29. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfy1cJgg6wfWS0alIT8LrLt7GWKXHpidpWksygsUOifOd7j52KVPOCaOXI4YkB0WT0XHudvyU1AftkEZ-s4IRnDyTG_zM5Rsuu-M-eP6VDVFrP6SHgIj24OtbFK1Xg_B2uky6UKBE=)
30. [complianceonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoG-_169VuzGL7WEfRfk18SaAc5tGDmLe8uwloPr0XwvuoAeFwwTQHboxubIVm4mqy6WV5NU7eYfyZHwsH1h8yFHtefZVNtnXUPRWlwbu-ON9dxQTCF4oDPM8pfB0eQdBn2OHobs5nWm1Ws6WsLQ6VeTQ6zmJ4vJeNsFcEFNGz-3d7Jwo6fjxmHT163-baQBwUehIEEUp2nxfMIQ8=)
31. [europa.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYbPgQZFVkFHWB4jDDNhkqL1VCmInWsTxU3buEX8-3Vf6ze_ehD1B4FFxokyMVE4xlN_MKzGg3Q_uzSxV3IGgTQ85hK8c9Uy4JpSIIfN_XygRNkOgMo4rVV3Y_oLRxfpp-cQIvaBX0bA1N-68UgvEz0k78cL0y3m2xQaSAfy3Wq44pjE2X0ii8M7NaZvM8HXTW-AFkDHE_WdNCGnIufTrUq9tWXHpwPYmt2Pg2xxZhnPGBNtcE7jWbiQcAhwKUfKKogXo=)
32. [appliedclinicaltrialsonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGT771VK1M5eV0ObHoXQeA-BSridN-I8V6liis31FAWMaE_MeRgEEwSX1HIKe5biLWeP5rS4WJEmhsEQ8sZYBrYmZrXyOMDPEpnKs4nDEn2KSogEx-Gul1C20OegPKFNUswQEwG9e3VwlOiNAR_4UnWt77fh5NcuSACCG70hkFHz0h4TrLW9pkzUhXCof5dYJLh9Cbz)
33. [precisionformedicine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPbl0eMaZ7vwPyNGoTwPEowIH-iFjTBeDNb-nWQ3BwtMiqoKwEjIHAz_kL3TzsAjgjLfX-DDuQLE4ZKxQE7wdXkxWDLaqT5LAo1tKmbDdXIOi6PvXUg0N52Cnz6JpU5-OY9S2RRjSGEYwET-MjOMxYDxV2INY9jrB1iTsTHv9PSPtJ3vCsO8GFn_sDKXgWbZiLfU13O8yOVQ==)
34. [fortrea.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwqNXqZQI3dEvwbZHaxlUk4NMzwAkdnepICT6vrbGFaW4cg_w3fK4KPotb0yrw7ZIONFEZ-sXYrV2mH6nE2411_mH5PrSH4uzZlAHqrRxl1axrKIbGZuebQ6HreCOQm9fkFJxCZ3wZBgyoM_PGRDYrpISlfBEuInIOiVXBiAnlrIbHwCTLchYCCF-GVZzYKtfMAKhXBJsfcYI-LEUwdNExCZtaYxqW-rmB)
35. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhLkWTDc7RVH_N-svayGBQd3kLVOytAdOY7rPRPqQi1DvT11iEj_zGJPP7a8Tj1wOuJN0i_q19Hc9gJPtHpNnLgjaW-fTpoC7rdFnzbuH0hyKMSddyWkOYRU9IZ12LoKm8Mx20GM4=)
36. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzhXbWkrQn_LOWdWDsf0CBAxRxy2tFqfFVNnZWFOeAka63tn08OpScUKU1pTMJcUSUk6wl4BA3UmJfR_oXSd3Zv-l59L5ceL9Rzgdmtt_JVs-GEdWlsyLVoV5L6Dqg0xwn6vC_yy-avhpm8KWqSY3MEOYd-Tc7HbZKr-gSIyR7dzPtlmbtFr6bAGWHzQ-UvicVXddJo1SWNmzoGvBFhR5cDlcPrsqo9s-TzUJkhAJkZDG3ZUsrjHnXzW3uQCOStTrNaQDc4_HQoBSKPxxSorryRdmxXk7c58BLasswlBwOJEm9S7w=)
37. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgbfXbiYm8sDql1EFdpAnizoe3vU31vnF53eggcQmLE_niK0llZY9zSZG0n2LOUvgDGP7fAHQpGby4aWqYTT9BvgbQd73862K7vKOWe0SdboLKRIGVhQTiYUp2PnP-0fmSNlv_atA=)
38. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF19cls8i5n1XIg1UjzQ4yeJZEBxoT9H9MBAFjsoGA-Q-c4RjSMRSSBYHLLBDpguz946qqDtR0fL9XLi8WHUFoNw2JunuCbUtWBuODeOQkPtaTcQrEVpomIoZJMyWC_EvzGO9JFmjZu)
39. [scribd.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnwdor6DW7EibPfQSZ6MVZPOxfalPyPatKrUIy3wr_waoZ1f24-NEJZDmRlSy2VJls8DzPQcoGcYv94OojgnE7NoHsQkPHsNZ2aBRaVI04ZciCrEhoylsKklk8BYVPMW2MLnhu)
40. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAr60ei0LFJH5xLblKdcBSb2ONJgAu2o5ErwECYJjMqb7ZBH07J8iTb0oBPUWkEOjf2aWcfT7uZe1HN263JtHs_B3cDXOUCiGMBOqPizlhCQD9i04rDwhfO1FYmvqvEZ5i8uXuil8=)
41. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2hFPmdk7SuJ8ObjjRn0Mb6uM55D6OuVjMz_A7-1mQKspmm7sDlZD_SOfzDjM8QP5InFojyNy_8VlJvwqjIA7pg8o87pKRbEkhwbId7GfliuhszqEQMBT0qKkwOFeJwjIUyl-k0VMa)
42. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNGkbKeQlaxjNCwfY7YhjZV4n3iPgbG0T3xJWFb-HWtTeUId17KC8k5FfWzDxLbH1U9Z4iBmShUwLkXw63fnocUn8AbDSLUspbvMu1rrVIqa_Uy6deReEVZoRIhNSxe65OPyE31ANx)
43. [fda.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwPV0kCrtdnIE6Eu5SYnueWB1SsG2CRefzfqAnR19Q6E_jR8GOjfgUJmmhtdoOFPBgiCibMc8YHsYE04uAPvm5NGSZQ1ArM6J-qLL-jjHbaQR63vwWf1WK63iPwfHkK28Dr8UE8-kyfcgFy6SwmmOwy9lwAraQ7slLpjgSx204-VJDFIzcOfAEq-SJNEYITQIpmnHb7cReFYzujSe6fn3ThhcpxUxn9mViLjrMkJbR46Kl)


## Annotations
Annotation(end_index=2856, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExMsEggLea7SPeX8Knvds8I8xJhlg3C9a9xdXjZru8ad-FsFpTqzu78pl7JejgDICGNf_SaOnsRRhThV0ed7HbSrOrDJfxrEo9Dv0KRgtHyTXY8nuy6Dfjm71Q28YazfKe09w8cQg=', start_index=2844)
Annotation(end_index=2856, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWN5ayJDEOz9_-P0TBze67RGd_dP1LMHxLh2vqIjjWZxfHUjiYrOHd8Zhw4zNC14nM-5R-IPPbBtVx98ZpKK-IZFCC74ZIe3nTs7Qsi4_UBoMFBwIKcbNNN783I_Tf', start_index=2844)
Annotation(end_index=3496, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7cKVOvEXM6G6IqoZ9T7J902ZL2vFnp_O3h-AWaVAPcBJX-ishthvpXevWlAAlKb6bpyOaEJebdBs7ZBrroWNJPvfB3AwM1JJ1dhEJRjmp57e1OswdidlLyGdUfLyG4jvQ8eIyDMA_Vf7FUxTdK46joupW2LAKclWVrJbCH3b7yVIGck6WZMjtuGhjuge6gd9heS3ABQ1z5_B063GtCzw3g3vdQgBwLqVHt7cpLQVMKsg=', start_index=3484)
Annotation(end_index=3496, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqIDROLVYaxNmWeqXPWdtYzj-9MWfO-miV3SI0sRpr17ge5QTadojv3UpFMVfDvaHU70RZhNE0wweCDJENQenh48qp9rZeXMCdiCdyqzuviWhIvO-Gk8oTVntDvftJowQT9HRAw72JXIA7', start_index=3484)
Annotation(end_index=4143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_bCXOa2EcTmgLTFIG-4HJoWzZ-R4YzxZwVwBZNMLrdin-9CN7sNyaiw9KHK4Y-23aUlgIS7C0RsIbHPUmD3tQxYoAHT6BSbTNAavIGpqIBm-NfmrYsqyMiAFbjr0K4f9SRn9DzJA1yL8UACgxdKe3zELl6hhJYS_dAT-YOr0cvcMAfJIoQ1gdRd31Ku_GC_jbx6FdfsX1DaZ2_Q==', start_index=4134)
Annotation(end_index=4460, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-JuOIGGb7AjEKQ67A9HQig5A-w2-rJCmE0g5c05Jl9uooEHULueLR0jCB4ROtuZDyQ_CuQtjQHnixSEOSghTDZ7r_wSVNZOHdpQA_0vQEKzb5TPhkAnZVN11JY94xXvBzJ_jsJ9u8eIoa4NbTPkLw9NvJ35336iWhKjbg-uuzoB_jVKut2DfdfY4cbc6PwIWRde7Hs31tOq9mVtJq4N-naQIjOkXFBBBcC9J4lxQOX18ZXcO2je8lww==', start_index=4445)
Annotation(end_index=4460, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRUyFSgwKOlnbDnvWxYAKBuvf4qFIOPlz8tpjgKf1y1r_9s7H4KKbUmERwpXp4yOo3xXS8QV_KOZnejRjU1guf9YVpNBr6d7ntKw0IYoIVuPoG7csRUwFvFvolhatvHguLIS4eMURfeVqEWnrf3-6KKG4cRCk3R0RCdP4M8JZytYs0tV9sHRe7CbcigX3kpEbx69-m9dd9iSUc1rUw09MszyNVnEvhL-lrG1Yu5Ddjkj07-e21fjnEin4KfXaSPg==', start_index=4445)
Annotation(end_index=4460, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjje6t6ex1CCGCA3srEZApI_K4U5TQ_2n52V5zMFTg2K1SermfMsq8x7fd8Mndu96MT8t1ucWb1kNyBYXp1KzEvCAeZF9CxTB-G2-d3s2NhtEf1FibTO60q7LE5DmrKerQ_VFW_YHS', start_index=4445)
Annotation(end_index=4952, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6Ell0WskP5AzhMLK4QzsCZrSqiwYVRCnIYmUjfy3HzHRYbRfgKSYnvN1Q-seE_9lzSUGk8exGd4nm_wWUJHED_ae6WIrlNZefpNANndIT6WdM6lL8MkEV0EfoYCc=', start_index=4940)
Annotation(end_index=4952, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRUyFSgwKOlnbDnvWxYAKBuvf4qFIOPlz8tpjgKf1y1r_9s7H4KKbUmERwpXp4yOo3xXS8QV_KOZnejRjU1guf9YVpNBr6d7ntKw0IYoIVuPoG7csRUwFvFvolhatvHguLIS4eMURfeVqEWnrf3-6KKG4cRCk3R0RCdP4M8JZytYs0tV9sHRe7CbcigX3kpEbx69-m9dd9iSUc1rUw09MszyNVnEvhL-lrG1Yu5Ddjkj07-e21fjnEin4KfXaSPg==', start_index=4940)
Annotation(end_index=5182, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsNuHHpL6RU_4lk7q1FAkAxexscXiuONeIBu5JvWr-6gtOAYa-4fXtZkY-4fBMLE232p8V5-Mx0clcN3vdUiWuf0n3GUUm-IM8JoMkFIOhfVr9oWIs8Ca9ciYXnYkg03pLgDagHzkO-m-Dw6p7glP_UXu1rvmwVPsH-_vUXIPGDcA3FJCPqFzpPS_LkXTbnbwEbPuPGRTxq3E_yEOo6c9Utg9f2W_s9IWtTykYAQ==', start_index=5164)
Annotation(end_index=5182, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBsXUwXK3KMRNYFmYSBv9fPC5KeQBAOqEokoYU6LaQk6FXuP4shJR8QFZoSvBln56P5khza4I9AD6he9TCFlXiYLd6xmqLx4-1ZJWY-GTuAMPmlSs6Lxh72fWW01wYVeFwd8GL7-8=', start_index=5164)
Annotation(end_index=5182, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLUyrdwIT9NqXO8h5DB7JL1t6NrieA6K17kXziXQJwtgfSSpDYWToZvhFShrguz_KR7RFC3lVi7ikniB1tM2N5ZWG462gY37p3Ni6sRu20dbKrrOaDPXkhq9Y3jzPiqnZ_fytSBnJwVVpIyDPfLtBWiWqd9MzuLmxJLTyciAn999GAzvz-WzDg1kNkhxhmBjqGMAiXCk_44cOwb_ucARkUyXRUpcDgXFh1dEU=', start_index=5164)
Annotation(end_index=5372, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGV1VBqZ6dpaalLz0e_IQAGWqU-Vay1mWL1C0dCyclvU6Ab_clirGNKFNdwx79MXjDZx0FJjjA3KfAQud9ntabtwrzAH7dJs2UuaiWOUQEShdSUR2vYBiIWKxxbjcgNRuVFN5xdxI0o2YG2vZICzFQAL1Vn-dxM04q_3w7WIaoRUCmbTf5Zh_i0EfptQtm6i2SZVUTauRyXCKA=', start_index=5354)
Annotation(end_index=5372, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0WsnYyEurtrMVhP5doP7T8GIFgAlYoJeuerSlxDZQG8YRgKP-YtAT2Fq9AmWco68GZagm23052QZ0RU7W84uZf0ZbMhjMCZ9Hx0bQd2Xu56zYbtcl0o27vjiIqVEDwCjNlOHD4ofXZo15osnmVrMhwDtQjPYaFbpXHqFx4I9_zjKIIZwF_ATbLtmEDPHGNFvd_FmcNqaDsSruZgx2Xb41df7BP4G9R0wUqD35zKQ-yzTdg9_vB84vfv65sQ_XYKZj8FhxLwuvowbxt_OJqCZhlqy_qvUkEk2jED5roiIV4VwShITzIA5YJ2TKC1BxJnOV7uRmbD8S', start_index=5354)
Annotation(end_index=5372, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXsGHCnbQqvwEpa7r7ADJvSNaF6MghzYCOjhVLGp3CpB6AH7M_4EL5WFaeWNqrSfEVu27UJ-36e6dqczTEzobTlFaY2hy1WySWMDAW0BQIFiFpxFDiKJsbWQfpMrFCgWXvwUq5qIatT16z5gv8rJVhFoJ8I-n1ZtLk-jckPWbPgsfPf4OJCf2jH8p1GYBfEg==', start_index=5354)
Annotation(end_index=5796, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsNuHHpL6RU_4lk7q1FAkAxexscXiuONeIBu5JvWr-6gtOAYa-4fXtZkY-4fBMLE232p8V5-Mx0clcN3vdUiWuf0n3GUUm-IM8JoMkFIOhfVr9oWIs8Ca9ciYXnYkg03pLgDagHzkO-m-Dw6p7glP_UXu1rvmwVPsH-_vUXIPGDcA3FJCPqFzpPS_LkXTbnbwEbPuPGRTxq3E_yEOo6c9Utg9f2W_s9IWtTykYAQ==', start_index=5782)
Annotation(end_index=5796, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBsXUwXK3KMRNYFmYSBv9fPC5KeQBAOqEokoYU6LaQk6FXuP4shJR8QFZoSvBln56P5khza4I9AD6he9TCFlXiYLd6xmqLx4-1ZJWY-GTuAMPmlSs6Lxh72fWW01wYVeFwd8GL7-8=', start_index=5782)
Annotation(end_index=5901, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGV1VBqZ6dpaalLz0e_IQAGWqU-Vay1mWL1C0dCyclvU6Ab_clirGNKFNdwx79MXjDZx0FJjjA3KfAQud9ntabtwrzAH7dJs2UuaiWOUQEShdSUR2vYBiIWKxxbjcgNRuVFN5xdxI0o2YG2vZICzFQAL1Vn-dxM04q_3w7WIaoRUCmbTf5Zh_i0EfptQtm6i2SZVUTauRyXCKA=', start_index=5887)
Annotation(end_index=5901, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXsGHCnbQqvwEpa7r7ADJvSNaF6MghzYCOjhVLGp3CpB6AH7M_4EL5WFaeWNqrSfEVu27UJ-36e6dqczTEzobTlFaY2hy1WySWMDAW0BQIFiFpxFDiKJsbWQfpMrFCgWXvwUq5qIatT16z5gv8rJVhFoJ8I-n1ZtLk-jckPWbPgsfPf4OJCf2jH8p1GYBfEg==', start_index=5887)
Annotation(end_index=6344, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExMsEggLea7SPeX8Knvds8I8xJhlg3C9a9xdXjZru8ad-FsFpTqzu78pl7JejgDICGNf_SaOnsRRhThV0ed7HbSrOrDJfxrEo9Dv0KRgtHyTXY8nuy6Dfjm71Q28YazfKe09w8cQg=', start_index=6335)
Annotation(end_index=6598, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExMsEggLea7SPeX8Knvds8I8xJhlg3C9a9xdXjZru8ad-FsFpTqzu78pl7JejgDICGNf_SaOnsRRhThV0ed7HbSrOrDJfxrEo9Dv0KRgtHyTXY8nuy6Dfjm71Q28YazfKe09w8cQg=', start_index=6589)
Annotation(end_index=6820, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFU6Uv0EmY-iVr2256ZRmcEZJo2kwbGUBgP8pJX9LUrUjlp7UB415vTIKSyW4tvoVxZ9bywZNMvl6LbygeAnzZpGvf1PpWFY7x2j8SKY-LB0f1hakgE5gmJ4wd7ilJ6', start_index=6807)
Annotation(end_index=6820, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWN5ayJDEOz9_-P0TBze67RGd_dP1LMHxLh2vqIjjWZxfHUjiYrOHd8Zhw4zNC14nM-5R-IPPbBtVx98ZpKK-IZFCC74ZIe3nTs7Qsi4_UBoMFBwIKcbNNN783I_Tf', start_index=6807)
Annotation(end_index=7393, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEQZGfQG-HQG7l3Cj0x9FFjzcFVLOPR_tUWt7uZwAk3jm1zVBmvxyvFSA_X5cjs1W-17xuTxEVH8M6_FnPYtIIS5jFUKkCi4LYAtp8B0PakVa_lIR87UBkXzB34CqsO3bHXXck9whVa9ztum6LzWlHyg==', start_index=7380)
Annotation(end_index=7393, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExMsEggLea7SPeX8Knvds8I8xJhlg3C9a9xdXjZru8ad-FsFpTqzu78pl7JejgDICGNf_SaOnsRRhThV0ed7HbSrOrDJfxrEo9Dv0KRgtHyTXY8nuy6Dfjm71Q28YazfKe09w8cQg=', start_index=7380)
Annotation(end_index=7772, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcfRZtU6dn9yUJX6HesLRbnUxrzOeTTglvTd4FtB1z06fQhuLZJa-XBZC4uxZcoQwtvrYBrGw50VSwQ7HZD9xmcFgsEwmViX0ZKEb0mvIXBooeHoJdn0PKO0YydKcEXV8Ws4n_VJzb', start_index=7758)
Annotation(end_index=7772, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhIt4ZpbpZjA96ZfnFxFnmvTgoCnuEcT21QXmp3_9ic_eX38arD0LGxutZZw7xZ1vnNYGapl9wXjAhh1ipRkdUYU_im-K37rFdqBMSlZfX383eOHO3D1jfPSoneQfn8UVdbGiFsVY=', start_index=7758)
Annotation(end_index=8884, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG27xoNdgf_4ZVvoNQy6QwXKs4WvaVhwFyWG1-X7CKDNTEpd8jp0p8a3AuVIdRP5EE5YHnRkg9XNcbrsb8xYkq8KLkVkXzs80PAHQUtxBzUOLVENsSqI4DnAGBvj2Bq5gPESPQHcnUHL-47P3BYPBuxE3oJ_Z57huXVJzryVyRA_ovHfvwwi-scAhOrGVAemaKtLoP2rso2ZMD0L-1cz4Cf34nF3bVZNA==', start_index=8870)
Annotation(end_index=8884, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs5mQSNrD-DXPUhVZ42XQOh7lGz2UzSCuwbfAJ9L4dv2ShyDzgfqLo3_WT-HKq4GycxUA8S9m5unHxhkcDDaXOSUt0GK7ge4sL3tVBX6GvcfDrDwgrg8-of83F7-Eb787RRGP1jHOUVdnKiKw9Flhi2FQwk9tSo_nT9dJOQa4mdNYF5yKykjYb1tnr9yhvVzIsz3jB-HOJ3JzcLX0GgaSaeYemo9BnrjuNTL5qbjKY9qYvmYkLXt-XlJZRkJbSFcpYXss4RmFq94aOBCrxy5g8qLI-xet3kQcAPSpS8kkqEUjNduIYGgKLRtxVdGqk3wlgnsSDP38zp_uzhg==', start_index=8870)
Annotation(end_index=9273, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEs_eCh0PaONu6CqeT_NK8F1T9y1Ke-vmb-UDtViwUuGOn-2NfiMzL6zbu-uLIqdge4Q04S8SK3St-p4oRmzC27wnvnH1oDrvF3cCsndhlv3Cug2cMrtrV6SfgkKlQbe8QY6gVSlGPJoQdVA0w=', start_index=9259)
Annotation(end_index=9273, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs5mQSNrD-DXPUhVZ42XQOh7lGz2UzSCuwbfAJ9L4dv2ShyDzgfqLo3_WT-HKq4GycxUA8S9m5unHxhkcDDaXOSUt0GK7ge4sL3tVBX6GvcfDrDwgrg8-of83F7-Eb787RRGP1jHOUVdnKiKw9Flhi2FQwk9tSo_nT9dJOQa4mdNYF5yKykjYb1tnr9yhvVzIsz3jB-HOJ3JzcLX0GgaSaeYemo9BnrjuNTL5qbjKY9qYvmYkLXt-XlJZRkJbSFcpYXss4RmFq94aOBCrxy5g8qLI-xet3kQcAPSpS8kkqEUjNduIYGgKLRtxVdGqk3wlgnsSDP38zp_uzhg==', start_index=9259)
Annotation(end_index=9628, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG27xoNdgf_4ZVvoNQy6QwXKs4WvaVhwFyWG1-X7CKDNTEpd8jp0p8a3AuVIdRP5EE5YHnRkg9XNcbrsb8xYkq8KLkVkXzs80PAHQUtxBzUOLVENsSqI4DnAGBvj2Bq5gPESPQHcnUHL-47P3BYPBuxE3oJ_Z57huXVJzryVyRA_ovHfvwwi-scAhOrGVAemaKtLoP2rso2ZMD0L-1cz4Cf34nF3bVZNA==', start_index=9614)
Annotation(end_index=9628, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs5mQSNrD-DXPUhVZ42XQOh7lGz2UzSCuwbfAJ9L4dv2ShyDzgfqLo3_WT-HKq4GycxUA8S9m5unHxhkcDDaXOSUt0GK7ge4sL3tVBX6GvcfDrDwgrg8-of83F7-Eb787RRGP1jHOUVdnKiKw9Flhi2FQwk9tSo_nT9dJOQa4mdNYF5yKykjYb1tnr9yhvVzIsz3jB-HOJ3JzcLX0GgaSaeYemo9BnrjuNTL5qbjKY9qYvmYkLXt-XlJZRkJbSFcpYXss4RmFq94aOBCrxy5g8qLI-xet3kQcAPSpS8kkqEUjNduIYGgKLRtxVdGqk3wlgnsSDP38zp_uzhg==', start_index=9614)
Annotation(end_index=9751, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG27xoNdgf_4ZVvoNQy6QwXKs4WvaVhwFyWG1-X7CKDNTEpd8jp0p8a3AuVIdRP5EE5YHnRkg9XNcbrsb8xYkq8KLkVkXzs80PAHQUtxBzUOLVENsSqI4DnAGBvj2Bq5gPESPQHcnUHL-47P3BYPBuxE3oJ_Z57huXVJzryVyRA_ovHfvwwi-scAhOrGVAemaKtLoP2rso2ZMD0L-1cz4Cf34nF3bVZNA==', start_index=9741)
Annotation(end_index=9874, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEs_eCh0PaONu6CqeT_NK8F1T9y1Ke-vmb-UDtViwUuGOn-2NfiMzL6zbu-uLIqdge4Q04S8SK3St-p4oRmzC27wnvnH1oDrvF3cCsndhlv3Cug2cMrtrV6SfgkKlQbe8QY6gVSlGPJoQdVA0w=', start_index=9860)
Annotation(end_index=9874, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs5mQSNrD-DXPUhVZ42XQOh7lGz2UzSCuwbfAJ9L4dv2ShyDzgfqLo3_WT-HKq4GycxUA8S9m5unHxhkcDDaXOSUt0GK7ge4sL3tVBX6GvcfDrDwgrg8-of83F7-Eb787RRGP1jHOUVdnKiKw9Flhi2FQwk9tSo_nT9dJOQa4mdNYF5yKykjYb1tnr9yhvVzIsz3jB-HOJ3JzcLX0GgaSaeYemo9BnrjuNTL5qbjKY9qYvmYkLXt-XlJZRkJbSFcpYXss4RmFq94aOBCrxy5g8qLI-xet3kQcAPSpS8kkqEUjNduIYGgKLRtxVdGqk3wlgnsSDP38zp_uzhg==', start_index=9860)
Annotation(end_index=10172, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyjXCK8e0okuj8667zBDwcTEwOcPi9vliHJ4UuVvimoUVvWzBZ10Y-JQHGZvic2c5wBrQtv10G8FCbMansla0XfNzZUfW6mvC7gCWsoeObxpYSxz1S7LaQ00gRiNLzL2eCk4s2rRhP', start_index=10162)
Annotation(end_index=10310, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhd93EsaumLtaPHqBdookZ1NQO2KyMSOSL4HgHSs15IZKqwINWIgUGc6IPIrfNoS6nvuSZBNQLUCUA605GLpuMQjNdjxWBF66D9NSoDEdhIK3_QM46Xlrkg4sM6A2EavLV7QGYQZSRLWOGeRnM_qPwCDSwOTfMtmFvoIVcQvpI_1H4i0X12XdS6OGED95_2c-R7FUb4bZ4cs9XysWZmuv9', start_index=10300)
Annotation(end_index=10937, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXciRt_-zghj-P9U5C9RP7H1imXrQ6I5jm4hDquaR7S5cPpwqexxSTsJAIo46YabIRQ2XGHb10F1U8cox3FZtgZMLI04qEzFGJ_cEGfPsY6WCBFWo5_yNQ06Xaiwaj-2AqtBH-0A==', start_index=10923)
Annotation(end_index=10937, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVXUj-SD32tOuTuxmPjUP5gLaphOV67edewzaoGrv_eI5R9SOHKBSR5tEWkNhwerB2gGLr_B7GOjhmy1rzTWo4JPRcCwdFSyAEJNKz12uk7G2QIL8Q9ztRVjYqcQ==', start_index=10923)
Annotation(end_index=11120, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVXUj-SD32tOuTuxmPjUP5gLaphOV67edewzaoGrv_eI5R9SOHKBSR5tEWkNhwerB2gGLr_B7GOjhmy1rzTWo4JPRcCwdFSyAEJNKz12uk7G2QIL8Q9ztRVjYqcQ==', start_index=11110)
Annotation(end_index=11747, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKgoCKAQMHL3I51N3UpzYmVHPvCSi0MsSvPrqG4rvNE_orh1eaDAlH4oIAbfadyaHO8OFrtvOD9Erl3KMmMAZNdVOB_eDBBfYUXFwX243JnEuJssErr3qTNiUoP46h', start_index=11733)
Annotation(end_index=11747, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7-TZapdD8mINavlOhglSeQIZ-i-mSSDs020093lCPknYEYwV-r2AukvPr-XJAOGxOqGHicjzq-5OsBsRFUizyNoQQFxtSzoHOXjiS-gEgdEt_UisgAg==', start_index=11733)
Annotation(end_index=12011, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfy1cJgg6wfWS0alIT8LrLt7GWKXHpidpWksygsUOifOd7j52KVPOCaOXI4YkB0WT0XHudvyU1AftkEZ-s4IRnDyTG_zM5Rsuu-M-eP6VDVFrP6SHgIj24OtbFK1Xg_B2uky6UKBE=', start_index=12001)
Annotation(end_index=12231, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfy1cJgg6wfWS0alIT8LrLt7GWKXHpidpWksygsUOifOd7j52KVPOCaOXI4YkB0WT0XHudvyU1AftkEZ-s4IRnDyTG_zM5Rsuu-M-eP6VDVFrP6SHgIj24OtbFK1Xg_B2uky6UKBE=', start_index=12221)
Annotation(end_index=12880, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhd93EsaumLtaPHqBdookZ1NQO2KyMSOSL4HgHSs15IZKqwINWIgUGc6IPIrfNoS6nvuSZBNQLUCUA605GLpuMQjNdjxWBF66D9NSoDEdhIK3_QM46Xlrkg4sM6A2EavLV7QGYQZSRLWOGeRnM_qPwCDSwOTfMtmFvoIVcQvpI_1H4i0X12XdS6OGED95_2c-R7FUb4bZ4cs9XysWZmuv9', start_index=12862)
Annotation(end_index=12880, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7-TZapdD8mINavlOhglSeQIZ-i-mSSDs020093lCPknYEYwV-r2AukvPr-XJAOGxOqGHicjzq-5OsBsRFUizyNoQQFxtSzoHOXjiS-gEgdEt_UisgAg==', start_index=12862)
Annotation(end_index=12880, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoG-_169VuzGL7WEfRfk18SaAc5tGDmLe8uwloPr0XwvuoAeFwwTQHboxubIVm4mqy6WV5NU7eYfyZHwsH1h8yFHtefZVNtnXUPRWlwbu-ON9dxQTCF4oDPM8pfB0eQdBn2OHobs5nWm1Ws6WsLQ6VeTQ6zmJ4vJeNsFcEFNGz-3d7Jwo6fjxmHT163-baQBwUehIEEUp2nxfMIQ8=', start_index=12862)
Annotation(end_index=13156, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYbPgQZFVkFHWB4jDDNhkqL1VCmInWsTxU3buEX8-3Vf6ze_ehD1B4FFxokyMVE4xlN_MKzGg3Q_uzSxV3IGgTQ85hK8c9Uy4JpSIIfN_XygRNkOgMo4rVV3Y_oLRxfpp-cQIvaBX0bA1N-68UgvEz0k78cL0y3m2xQaSAfy3Wq44pjE2X0ii8M7NaZvM8HXTW-AFkDHE_WdNCGnIufTrUq9tWXHpwPYmt2Pg2xxZhnPGBNtcE7jWbiQcAhwKUfKKogXo=', start_index=13146)
Annotation(end_index=13705, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7cKVOvEXM6G6IqoZ9T7J902ZL2vFnp_O3h-AWaVAPcBJX-ishthvpXevWlAAlKb6bpyOaEJebdBs7ZBrroWNJPvfB3AwM1JJ1dhEJRjmp57e1OswdidlLyGdUfLyG4jvQ8eIyDMA_Vf7FUxTdK46joupW2LAKclWVrJbCH3b7yVIGck6WZMjtuGhjuge6gd9heS3ABQ1z5_B063GtCzw3g3vdQgBwLqVHt7cpLQVMKsg=', start_index=13692)
Annotation(end_index=13705, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGT771VK1M5eV0ObHoXQeA-BSridN-I8V6liis31FAWMaE_MeRgEEwSX1HIKe5biLWeP5rS4WJEmhsEQ8sZYBrYmZrXyOMDPEpnKs4nDEn2KSogEx-Gul1C20OegPKFNUswQEwG9e3VwlOiNAR_4UnWt77fh5NcuSACCG70hkFHz0h4TrLW9pkzUhXCof5dYJLh9Cbz', start_index=13692)
Annotation(end_index=14075, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPbl0eMaZ7vwPyNGoTwPEowIH-iFjTBeDNb-nWQ3BwtMiqoKwEjIHAz_kL3TzsAjgjLfX-DDuQLE4ZKxQE7wdXkxWDLaqT5LAo1tKmbDdXIOi6PvXUg0N52Cnz6JpU5-OY9S2RRjSGEYwET-MjOMxYDxV2INY9jrB1iTsTHv9PSPtJ3vCsO8GFn_sDKXgWbZiLfU13O8yOVQ==', start_index=14062)
Annotation(end_index=14075, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqIDROLVYaxNmWeqXPWdtYzj-9MWfO-miV3SI0sRpr17ge5QTadojv3UpFMVfDvaHU70RZhNE0wweCDJENQenh48qp9rZeXMCdiCdyqzuviWhIvO-Gk8oTVntDvftJowQT9HRAw72JXIA7', start_index=14062)
Annotation(end_index=14344, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwqNXqZQI3dEvwbZHaxlUk4NMzwAkdnepICT6vrbGFaW4cg_w3fK4KPotb0yrw7ZIONFEZ-sXYrV2mH6nE2411_mH5PrSH4uzZlAHqrRxl1axrKIbGZuebQ6HreCOQm9fkFJxCZ3wZBgyoM_PGRDYrpISlfBEuInIOiVXBiAnlrIbHwCTLchYCCF-GVZzYKtfMAKhXBJsfcYI-LEUwdNExCZtaYxqW-rmB', start_index=14331)
Annotation(end_index=14344, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7cKVOvEXM6G6IqoZ9T7J902ZL2vFnp_O3h-AWaVAPcBJX-ishthvpXevWlAAlKb6bpyOaEJebdBs7ZBrroWNJPvfB3AwM1JJ1dhEJRjmp57e1OswdidlLyGdUfLyG4jvQ8eIyDMA_Vf7FUxTdK46joupW2LAKclWVrJbCH3b7yVIGck6WZMjtuGhjuge6gd9heS3ABQ1z5_B063GtCzw3g3vdQgBwLqVHt7cpLQVMKsg=', start_index=14331)
Annotation(end_index=14682, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPbl0eMaZ7vwPyNGoTwPEowIH-iFjTBeDNb-nWQ3BwtMiqoKwEjIHAz_kL3TzsAjgjLfX-DDuQLE4ZKxQE7wdXkxWDLaqT5LAo1tKmbDdXIOi6PvXUg0N52Cnz6JpU5-OY9S2RRjSGEYwET-MjOMxYDxV2INY9jrB1iTsTHv9PSPtJ3vCsO8GFn_sDKXgWbZiLfU13O8yOVQ==', start_index=14668)
Annotation(end_index=14682, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGT771VK1M5eV0ObHoXQeA-BSridN-I8V6liis31FAWMaE_MeRgEEwSX1HIKe5biLWeP5rS4WJEmhsEQ8sZYBrYmZrXyOMDPEpnKs4nDEn2KSogEx-Gul1C20OegPKFNUswQEwG9e3VwlOiNAR_4UnWt77fh5NcuSACCG70hkFHz0h4TrLW9pkzUhXCof5dYJLh9Cbz', start_index=14668)
Annotation(end_index=15195, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhLkWTDc7RVH_N-svayGBQd3kLVOytAdOY7rPRPqQi1DvT11iEj_zGJPP7a8Tj1wOuJN0i_q19Hc9gJPtHpNnLgjaW-fTpoC7rdFnzbuH0hyKMSddyWkOYRU9IZ12LoKm8Mx20GM4=', start_index=15181)
Annotation(end_index=15195, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzhXbWkrQn_LOWdWDsf0CBAxRxy2tFqfFVNnZWFOeAka63tn08OpScUKU1pTMJcUSUk6wl4BA3UmJfR_oXSd3Zv-l59L5ceL9Rzgdmtt_JVs-GEdWlsyLVoV5L6Dqg0xwn6vC_yy-avhpm8KWqSY3MEOYd-Tc7HbZKr-gSIyR7dzPtlmbtFr6bAGWHzQ-UvicVXddJo1SWNmzoGvBFhR5cDlcPrsqo9s-TzUJkhAJkZDG3ZUsrjHnXzW3uQCOStTrNaQDc4_HQoBSKPxxSorryRdmxXk7c58BLasswlBwOJEm9S7w=', start_index=15181)
Annotation(end_index=15402, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgbfXbiYm8sDql1EFdpAnizoe3vU31vnF53eggcQmLE_niK0llZY9zSZG0n2LOUvgDGP7fAHQpGby4aWqYTT9BvgbQd73862K7vKOWe0SdboLKRIGVhQTiYUp2PnP-0fmSNlv_atA=', start_index=15392)
Annotation(end_index=15780, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF19cls8i5n1XIg1UjzQ4yeJZEBxoT9H9MBAFjsoGA-Q-c4RjSMRSSBYHLLBDpguz946qqDtR0fL9XLi8WHUFoNw2JunuCbUtWBuODeOQkPtaTcQrEVpomIoZJMyWC_EvzGO9JFmjZu', start_index=15770)
Annotation(end_index=16079, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF19cls8i5n1XIg1UjzQ4yeJZEBxoT9H9MBAFjsoGA-Q-c4RjSMRSSBYHLLBDpguz946qqDtR0fL9XLi8WHUFoNw2JunuCbUtWBuODeOQkPtaTcQrEVpomIoZJMyWC_EvzGO9JFmjZu', start_index=16065)
Annotation(end_index=16079, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnwdor6DW7EibPfQSZ6MVZPOxfalPyPatKrUIy3wr_waoZ1f24-NEJZDmRlSy2VJls8DzPQcoGcYv94OojgnE7NoHsQkPHsNZ2aBRaVI04ZciCrEhoylsKklk8BYVPMW2MLnhu', start_index=16065)
Annotation(end_index=16630, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyjXCK8e0okuj8667zBDwcTEwOcPi9vliHJ4UuVvimoUVvWzBZ10Y-JQHGZvic2c5wBrQtv10G8FCbMansla0XfNzZUfW6mvC7gCWsoeObxpYSxz1S7LaQ00gRiNLzL2eCk4s2rRhP', start_index=16620)
Annotation(end_index=17889, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-JuOIGGb7AjEKQ67A9HQig5A-w2-rJCmE0g5c05Jl9uooEHULueLR0jCB4ROtuZDyQ_CuQtjQHnixSEOSghTDZ7r_wSVNZOHdpQA_0vQEKzb5TPhkAnZVN11JY94xXvBzJ_jsJ9u8eIoa4NbTPkLw9NvJ35336iWhKjbg-uuzoB_jVKut2DfdfY4cbc6PwIWRde7Hs31tOq9mVtJq4N-naQIjOkXFBBBcC9J4lxQOX18ZXcO2je8lww==', start_index=17880)
Annotation(end_index=17964, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExMsEggLea7SPeX8Knvds8I8xJhlg3C9a9xdXjZru8ad-FsFpTqzu78pl7JejgDICGNf_SaOnsRRhThV0ed7HbSrOrDJfxrEo9Dv0KRgtHyTXY8nuy6Dfjm71Q28YazfKe09w8cQg=', start_index=17955)
Annotation(end_index=18145, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAr60ei0LFJH5xLblKdcBSb2ONJgAu2o5ErwECYJjMqb7ZBH07J8iTb0oBPUWkEOjf2aWcfT7uZe1HN263JtHs_B3cDXOUCiGMBOqPizlhCQD9i04rDwhfO1FYmvqvEZ5i8uXuil8=', start_index=18135)
Annotation(end_index=18236, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVXUj-SD32tOuTuxmPjUP5gLaphOV67edewzaoGrv_eI5R9SOHKBSR5tEWkNhwerB2gGLr_B7GOjhmy1rzTWo4JPRcCwdFSyAEJNKz12uk7G2QIL8Q9ztRVjYqcQ==', start_index=18226)
Annotation(end_index=18302, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF19cls8i5n1XIg1UjzQ4yeJZEBxoT9H9MBAFjsoGA-Q-c4RjSMRSSBYHLLBDpguz946qqDtR0fL9XLi8WHUFoNw2JunuCbUtWBuODeOQkPtaTcQrEVpomIoZJMyWC_EvzGO9JFmjZu', start_index=18292)
Annotation(end_index=18408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXciRt_-zghj-P9U5C9RP7H1imXrQ6I5jm4hDquaR7S5cPpwqexxSTsJAIo46YabIRQ2XGHb10F1U8cox3FZtgZMLI04qEzFGJ_cEGfPsY6WCBFWo5_yNQ06Xaiwaj-2AqtBH-0A==', start_index=18398)
Annotation(end_index=18478, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2hFPmdk7SuJ8ObjjRn0Mb6uM55D6OuVjMz_A7-1mQKspmm7sDlZD_SOfzDjM8QP5InFojyNy_8VlJvwqjIA7pg8o87pKRbEkhwbId7GfliuhszqEQMBT0qKkwOFeJwjIUyl-k0VMa', start_index=18468)
Annotation(end_index=18553, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgbfXbiYm8sDql1EFdpAnizoe3vU31vnF53eggcQmLE_niK0llZY9zSZG0n2LOUvgDGP7fAHQpGby4aWqYTT9BvgbQd73862K7vKOWe0SdboLKRIGVhQTiYUp2PnP-0fmSNlv_atA=', start_index=18543)
Annotation(end_index=18630, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNGkbKeQlaxjNCwfY7YhjZV4n3iPgbG0T3xJWFb-HWtTeUId17KC8k5FfWzDxLbH1U9Z4iBmShUwLkXw63fnocUn8AbDSLUspbvMu1rrVIqa_Uy6deReEVZoRIhNSxe65OPyE31ANx', start_index=18620)
Annotation(end_index=18689, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhd93EsaumLtaPHqBdookZ1NQO2KyMSOSL4HgHSs15IZKqwINWIgUGc6IPIrfNoS6nvuSZBNQLUCUA605GLpuMQjNdjxWBF66D9NSoDEdhIK3_QM46Xlrkg4sM6A2EavLV7QGYQZSRLWOGeRnM_qPwCDSwOTfMtmFvoIVcQvpI_1H4i0X12XdS6OGED95_2c-R7FUb4bZ4cs9XysWZmuv9', start_index=18679)
Annotation(end_index=18777, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwPV0kCrtdnIE6Eu5SYnueWB1SsG2CRefzfqAnR19Q6E_jR8GOjfgUJmmhtdoOFPBgiCibMc8YHsYE04uAPvm5NGSZQ1ArM6J-qLL-jjHbaQR63vwWf1WK63iPwfHkK28Dr8UE8-kyfcgFy6SwmmOwy9lwAraQ7slLpjgSx204-VJDFIzcOfAEq-SJNEYITQIpmnHb7cReFYzujSe6fn3ThhcpxUxn9mViLjrMkJbR46Kl', start_index=18767)
Annotation(end_index=18868, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnwdor6DW7EibPfQSZ6MVZPOxfalPyPatKrUIy3wr_waoZ1f24-NEJZDmRlSy2VJls8DzPQcoGcYv94OojgnE7NoHsQkPHsNZ2aBRaVI04ZciCrEhoylsKklk8BYVPMW2MLnhu', start_index=18858)
Annotation(end_index=18906, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG27xoNdgf_4ZVvoNQy6QwXKs4WvaVhwFyWG1-X7CKDNTEpd8jp0p8a3AuVIdRP5EE5YHnRkg9XNcbrsb8xYkq8KLkVkXzs80PAHQUtxBzUOLVENsSqI4DnAGBvj2Bq5gPESPQHcnUHL-47P3BYPBuxE3oJ_Z57huXVJzryVyRA_ovHfvwwi-scAhOrGVAemaKtLoP2rso2ZMD0L-1cz4Cf34nF3bVZNA==', start_index=18896)
Annotation(end_index=18982, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs5mQSNrD-DXPUhVZ42XQOh7lGz2UzSCuwbfAJ9L4dv2ShyDzgfqLo3_WT-HKq4GycxUA8S9m5unHxhkcDDaXOSUt0GK7ge4sL3tVBX6GvcfDrDwgrg8-of83F7-Eb787RRGP1jHOUVdnKiKw9Flhi2FQwk9tSo_nT9dJOQa4mdNYF5yKykjYb1tnr9yhvVzIsz3jB-HOJ3JzcLX0GgaSaeYemo9BnrjuNTL5qbjKY9qYvmYkLXt-XlJZRkJbSFcpYXss4RmFq94aOBCrxy5g8qLI-xet3kQcAPSpS8kkqEUjNduIYGgKLRtxVdGqk3wlgnsSDP38zp_uzhg==', start_index=18972)
Annotation(end_index=19180, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_bCXOa2EcTmgLTFIG-4HJoWzZ-R4YzxZwVwBZNMLrdin-9CN7sNyaiw9KHK4Y-23aUlgIS7C0RsIbHPUmD3tQxYoAHT6BSbTNAavIGpqIBm-NfmrYsqyMiAFbjr0K4f9SRn9DzJA1yL8UACgxdKe3zELl6hhJYS_dAT-YOr0cvcMAfJIoQ1gdRd31Ku_GC_jbx6FdfsX1DaZ2_Q==', start_index=19171)
Annotation(end_index=19254, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExMsEggLea7SPeX8Knvds8I8xJhlg3C9a9xdXjZru8ad-FsFpTqzu78pl7JejgDICGNf_SaOnsRRhThV0ed7HbSrOrDJfxrEo9Dv0KRgtHyTXY8nuy6Dfjm71Q28YazfKe09w8cQg=', start_index=19245)
Annotation(end_index=19316, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcfRZtU6dn9yUJX6HesLRbnUxrzOeTTglvTd4FtB1z06fQhuLZJa-XBZC4uxZcoQwtvrYBrGw50VSwQ7HZD9xmcFgsEwmViX0ZKEb0mvIXBooeHoJdn0PKO0YydKcEXV8Ws4n_VJzb', start_index=19306)
Annotation(end_index=19389, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhIt4ZpbpZjA96ZfnFxFnmvTgoCnuEcT21QXmp3_9ic_eX38arD0LGxutZZw7xZ1vnNYGapl9wXjAhh1ipRkdUYU_im-K37rFdqBMSlZfX383eOHO3D1jfPSoneQfn8UVdbGiFsVY=', start_index=19379)
Annotation(end_index=19458, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsNuHHpL6RU_4lk7q1FAkAxexscXiuONeIBu5JvWr-6gtOAYa-4fXtZkY-4fBMLE232p8V5-Mx0clcN3vdUiWuf0n3GUUm-IM8JoMkFIOhfVr9oWIs8Ca9ciYXnYkg03pLgDagHzkO-m-Dw6p7glP_UXu1rvmwVPsH-_vUXIPGDcA3FJCPqFzpPS_LkXTbnbwEbPuPGRTxq3E_yEOo6c9Utg9f2W_s9IWtTykYAQ==', start_index=19448)
Annotation(end_index=19543, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEQZGfQG-HQG7l3Cj0x9FFjzcFVLOPR_tUWt7uZwAk3jm1zVBmvxyvFSA_X5cjs1W-17xuTxEVH8M6_FnPYtIIS5jFUKkCi4LYAtp8B0PakVa_lIR87UBkXzB34CqsO3bHXXck9whVa9ztum6LzWlHyg==', start_index=19533)
Annotation(end_index=19607, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhLkWTDc7RVH_N-svayGBQd3kLVOytAdOY7rPRPqQi1DvT11iEj_zGJPP7a8Tj1wOuJN0i_q19Hc9gJPtHpNnLgjaW-fTpoC7rdFnzbuH0hyKMSddyWkOYRU9IZ12LoKm8Mx20GM4=', start_index=19597)
Annotation(end_index=19664, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfy1cJgg6wfWS0alIT8LrLt7GWKXHpidpWksygsUOifOd7j52KVPOCaOXI4YkB0WT0XHudvyU1AftkEZ-s4IRnDyTG_zM5Rsuu-M-eP6VDVFrP6SHgIj24OtbFK1Xg_B2uky6UKBE=', start_index=19654)
Annotation(end_index=19733, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7-TZapdD8mINavlOhglSeQIZ-i-mSSDs020093lCPknYEYwV-r2AukvPr-XJAOGxOqGHicjzq-5OsBsRFUizyNoQQFxtSzoHOXjiS-gEgdEt_UisgAg==', start_index=19723)
Annotation(end_index=19793, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG27xoNdgf_4ZVvoNQy6QwXKs4WvaVhwFyWG1-X7CKDNTEpd8jp0p8a3AuVIdRP5EE5YHnRkg9XNcbrsb8xYkq8KLkVkXzs80PAHQUtxBzUOLVENsSqI4DnAGBvj2Bq5gPESPQHcnUHL-47P3BYPBuxE3oJ_Z57huXVJzryVyRA_ovHfvwwi-scAhOrGVAemaKtLoP2rso2ZMD0L-1cz4Cf34nF3bVZNA==', start_index=19783)
Annotation(end_index=19862, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfy1cJgg6wfWS0alIT8LrLt7GWKXHpidpWksygsUOifOd7j52KVPOCaOXI4YkB0WT0XHudvyU1AftkEZ-s4IRnDyTG_zM5Rsuu-M-eP6VDVFrP6SHgIj24OtbFK1Xg_B2uky6UKBE=', start_index=19852)
Annotation(end_index=19912, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7cKVOvEXM6G6IqoZ9T7J902ZL2vFnp_O3h-AWaVAPcBJX-ishthvpXevWlAAlKb6bpyOaEJebdBs7ZBrroWNJPvfB3AwM1JJ1dhEJRjmp57e1OswdidlLyGdUfLyG4jvQ8eIyDMA_Vf7FUxTdK46joupW2LAKclWVrJbCH3b7yVIGck6WZMjtuGhjuge6gd9heS3ABQ1z5_B063GtCzw3g3vdQgBwLqVHt7cpLQVMKsg=', start_index=19903)
Annotation(end_index=19967, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqIDROLVYaxNmWeqXPWdtYzj-9MWfO-miV3SI0sRpr17ge5QTadojv3UpFMVfDvaHU70RZhNE0wweCDJENQenh48qp9rZeXMCdiCdyqzuviWhIvO-Gk8oTVntDvftJowQT9HRAw72JXIA7', start_index=19958)
Annotation(end_index=20025, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwqNXqZQI3dEvwbZHaxlUk4NMzwAkdnepICT6vrbGFaW4cg_w3fK4KPotb0yrw7ZIONFEZ-sXYrV2mH6nE2411_mH5PrSH4uzZlAHqrRxl1axrKIbGZuebQ6HreCOQm9fkFJxCZ3wZBgyoM_PGRDYrpISlfBEuInIOiVXBiAnlrIbHwCTLchYCCF-GVZzYKtfMAKhXBJsfcYI-LEUwdNExCZtaYxqW-rmB', start_index=20015)
Annotation(end_index=20110, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGT771VK1M5eV0ObHoXQeA-BSridN-I8V6liis31FAWMaE_MeRgEEwSX1HIKe5biLWeP5rS4WJEmhsEQ8sZYBrYmZrXyOMDPEpnKs4nDEn2KSogEx-Gul1C20OegPKFNUswQEwG9e3VwlOiNAR_4UnWt77fh5NcuSACCG70hkFHz0h4TrLW9pkzUhXCof5dYJLh9Cbz', start_index=20100)
Annotation(end_index=20175, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyjXCK8e0okuj8667zBDwcTEwOcPi9vliHJ4UuVvimoUVvWzBZ10Y-JQHGZvic2c5wBrQtv10G8FCbMansla0XfNzZUfW6mvC7gCWsoeObxpYSxz1S7LaQ00gRiNLzL2eCk4s2rRhP', start_index=20165)
Annotation(end_index=20249, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRUyFSgwKOlnbDnvWxYAKBuvf4qFIOPlz8tpjgKf1y1r_9s7H4KKbUmERwpXp4yOo3xXS8QV_KOZnejRjU1guf9YVpNBr6d7ntKw0IYoIVuPoG7csRUwFvFvolhatvHguLIS4eMURfeVqEWnrf3-6KKG4cRCk3R0RCdP4M8JZytYs0tV9sHRe7CbcigX3kpEbx69-m9dd9iSUc1rUw09MszyNVnEvhL-lrG1Yu5Ddjkj07-e21fjnEin4KfXaSPg==', start_index=20240)
Annotation(end_index=20314, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjje6t6ex1CCGCA3srEZApI_K4U5TQ_2n52V5zMFTg2K1SermfMsq8x7fd8Mndu96MT8t1ucWb1kNyBYXp1KzEvCAeZF9CxTB-G2-d3s2NhtEf1FibTO60q7LE5DmrKerQ_VFW_YHS', start_index=20305)
Annotation(end_index=20373, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXsGHCnbQqvwEpa7r7ADJvSNaF6MghzYCOjhVLGp3CpB6AH7M_4EL5WFaeWNqrSfEVu27UJ-36e6dqczTEzobTlFaY2hy1WySWMDAW0BQIFiFpxFDiKJsbWQfpMrFCgWXvwUq5qIatT16z5gv8rJVhFoJ8I-n1ZtLk-jckPWbPgsfPf4OJCf2jH8p1GYBfEg==', start_index=20363)
Annotation(end_index=20439, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0WsnYyEurtrMVhP5doP7T8GIFgAlYoJeuerSlxDZQG8YRgKP-YtAT2Fq9AmWco68GZagm23052QZ0RU7W84uZf0ZbMhjMCZ9Hx0bQd2Xu56zYbtcl0o27vjiIqVEDwCjNlOHD4ofXZo15osnmVrMhwDtQjPYaFbpXHqFx4I9_zjKIIZwF_ATbLtmEDPHGNFvd_FmcNqaDsSruZgx2Xb41df7BP4G9R0wUqD35zKQ-yzTdg9_vB84vfv65sQ_XYKZj8FhxLwuvowbxt_OJqCZhlqy_qvUkEk2jED5roiIV4VwShITzIA5YJ2TKC1BxJnOV7uRmbD8S', start_index=20429)
Annotation(end_index=20519, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWN5ayJDEOz9_-P0TBze67RGd_dP1LMHxLh2vqIjjWZxfHUjiYrOHd8Zhw4zNC14nM-5R-IPPbBtVx98ZpKK-IZFCC74ZIe3nTs7Qsi4_UBoMFBwIKcbNNN783I_Tf', start_index=20510)
Annotation(end_index=20586, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBsXUwXK3KMRNYFmYSBv9fPC5KeQBAOqEokoYU6LaQk6FXuP4shJR8QFZoSvBln56P5khza4I9AD6he9TCFlXiYLd6xmqLx4-1ZJWY-GTuAMPmlSs6Lxh72fWW01wYVeFwd8GL7-8=', start_index=20576)

## Sources
