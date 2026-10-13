# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** e0b3f067 | **Time:** 478.39s | **Cost:** $1.60156
--------------------------------------------------------------------------------

# Anticoagulation Management in Extracorporeal Membrane Oxygenation (ECMO): Balancing Thromboembolism and Hemorrhage

### Key Points
*   **Standard of Care:** Unfractionated heparin (UFH) remains the predominant anticoagulant for ECMO due to its reversibility and familiarity, though practice varies significantly between centers.
*   **Dosing Guidelines:** The Extracorporeal Life Support Organization (ELSO) generally recommends an initial bolus of 50–100 units/kg followed by a maintenance infusion of 7.5–20 units/kg/h, titrated to effect.
*   **Monitoring Challenges:** There is no single "gold standard" for monitoring. Activated Clotting Time (ACT) is widely used for bedside monitoring but correlates poorly with heparin concentration. Anti-Factor Xa (Anti-Xa) is increasingly preferred for specificity, while Activated Partial Thromboplastin Time (aPTT) remains a common intermediate.
*   **Heparin Resistance:** Up to 50% of patients may exhibit heparin resistance, often driven by Antithrombin III (ATIII) deficiency. Supplementation of ATIII is debated; while it restores heparin sensitivity, its impact on mortality and bleeding outcomes is inconsistent.
*   **Heparin-Sparing Strategies:** In patients with high bleeding risk (e.g., trauma, post-cardiotomy), heparin-free or low-dose strategies are feasible, relying on high circuit flow rates (>3 L/min) to prevent thrombosis.

### Introduction
The management of anticoagulation during Extracorporeal Membrane Oxygenation (ECMO) represents one of the most complex challenges in critical care medicine. The fundamental dilemma lies in the interaction between blood and the non-biologic surfaces of the ECMO circuit, which triggers a massive inflammatory and pro-coagulant response [cite: 1, 2]. Without anticoagulation, this contact activation leads to rapid circuit thrombosis and systemic embolization. Conversely, the systemic anticoagulation required to maintain circuit patency significantly increases the risk of life-threatening hemorrhage, particularly intracranial and surgical site bleeding [cite: 1, 3].

Unfractionated heparin (UFH) is the standard anticoagulant used worldwide, yet optimal dosing and monitoring strategies remain a subject of intense debate and variation [cite: 4, 5]. This report provides an exhaustive analysis of heparin management strategies, monitoring modalities, mechanisms of resistance, and protocols for balancing hemostatic risks.

---

## Standard Heparin Administration Protocols

The administration of UFH during ECMO is typically divided into two phases: the initial bolus at cannulation and the maintenance infusion. The goal is to achieve a therapeutic level of anticoagulation that inhibits the coagulation cascade sufficiently to prevent circuit clotting without rendering the patient coagulopathic.

### Initiation and Bolus Dosing
Upon the decision to initiate ECMO, a bolus of UFH is standard practice to prevent immediate thrombus formation on the guidewires and cannulas.
*   **Standard Bolus:** ELSO guidelines recommend an initial UFH bolus of 50–100 units/kg administered intravenously at the time of cannulation [cite: 1, 6].
*   **Target ACT:** The bolus is typically titrated to achieve an Activated Clotting Time (ACT) between 300 and 350 seconds prior to the insertion of cannulas to ensure adequate suppression of the coagulation cascade during the most thrombogenic phase of the procedure [cite: 6, 7].
*   **Exceptions:** In patients with active bleeding, significant coagulopathy, or those undergoing Extracorporeal Cardiopulmonary Resuscitation (ECPR) where bleeding risk is undetermined, the bolus may be reduced (e.g., 25–50 units/kg) or withheld entirely [cite: 8, 9, 10].

### Maintenance Infusion
Following cannulation, a continuous infusion of UFH is initiated to maintain therapeutic anticoagulation.
*   **Infusion Rates:** ELSO guidelines suggest a maintenance infusion rate ranging from 7.5 to 20.0 units/kg/h [cite: 4, 6]. However, older or alternative recommendations cite ranges of 20–50 units/kg/h depending on the patient population (pediatric vs. adult) and circuit type [cite: 1, 11].
*   **Titration:** The infusion is adjusted based on laboratory parameters (ACT, aPTT, or Anti-Xa). A common protocol involves adjusting the rate by 1–2 units/kg/h based on whether the patient is sub- or supra-therapeutic [cite: 12].
*   **Pediatric Considerations:** Neonates and children often require higher weight-based doses (e.g., 20–28 units/kg/h) compared to adults due to faster heparin clearance and developmental differences in hemostasis [cite: 10].

### Table 1: ELSO and Institutional Heparin Dosing Recommendations
| Parameter | Recommendation | Context/Notes |
| :--- | :--- | :--- |
| **Initial Bolus** | 50–100 units/kg | Administered at cannulation. May be withheld in ECPR or active bleeding [cite: 1, 6]. |
| **Maintenance Rate** | 7.5–20 units/kg/h | Lower range typical for adults; higher for pediatrics [cite: 4, 6]. |
| **Alternative Rate** | 20–50 units/kg/h | Cited in some protocols for achieving ACT 180–220s [cite: 1, 11]. |
| **Target ACT** | 180–220 seconds | Standard therapeutic range for maintenance [cite: 4, 6]. |
| **Target aPTT** | 40–60 or 60–80 seconds | Varies by bleeding risk (low vs. high) [cite: 4, 12]. |
| **Target Anti-Xa** | 0.3–0.7 IU/mL | Considered more specific for heparin effect [cite: 4, 13]. |

---

## Monitoring Strategies: The Search for Accuracy

One of the most significant challenges in ECMO management is the lack of a single, universally reliable laboratory test for monitoring UFH. The correlation between heparin dose and coagulation metrics is often poor, leading to discordant results and clinical uncertainty [cite: 14, 15].

### Activated Clotting Time (ACT)
Historically, ACT has been the primary method for monitoring heparin during ECMO due to its point-of-care availability and rapid turnaround.
*   **Target Range:** The typical therapeutic goal is 180–220 seconds [cite: 1, 4, 6].
*   **Limitations:** ACT measures the time for whole blood to clot and is influenced by numerous factors independent of heparin, including platelet count, fibrinogen levels, hypothermia, hemodilution, and factor deficiencies [cite: 4, 5, 16].
*   **Correlation:** Studies consistently show that ACT correlates poorly with heparin dosage and Anti-Xa levels [cite: 4, 15, 16]. Consequently, relying solely on ACT can lead to under- or over-anticoagulation.

### Activated Partial Thromboplastin Time (aPTT)
aPTT is a plasma-based test that measures the intrinsic and common pathways of the coagulation cascade.
*   **Target Range:** Common targets are 40–60 seconds or 60–80 seconds (approx. 1.5–2.5 times baseline) [cite: 4, 17, 18].
*   **Advantages:** aPTT generally correlates better with heparin concentration than ACT [cite: 4, 19].
*   **Limitations:** Like ACT, aPTT can be prolonged by coagulopathies (e.g., liver dysfunction, DIC) unrelated to heparin. It is also sensitive to acute phase reactants and factor levels (VIII, XII), which can vary in critically ill patients [cite: 13, 20]. In patients with COVID-19, aPTT has shown weak correlation with Anti-Xa, potentially due to high fibrinogen or lupus anticoagulants [cite: 21].

### Anti-Factor Xa (Anti-Xa)
Anti-Xa assays measure the inhibition of Factor Xa by the heparin-antithrombin complex, providing a direct quantification of heparin activity.
*   **Target Range:** The standard therapeutic range is 0.3–0.7 IU/mL [cite: 4, 13, 20]. Some trials (e.g., EOLIA) have used lower targets (0.2–0.3 IU/mL) with acceptable outcomes [cite: 4].
*   **Advantages:** Anti-Xa is considered the "gold standard" for specificity, as it is less affected by other coagulation factors or thrombocytopenia compared to ACT or aPTT [cite: 4, 13]. It correlates best with the actual heparin dose administered [cite: 15, 16].
*   **Limitations:** The assay relies on adequate Antithrombin III (ATIII) levels. In patients with ATIII deficiency, Anti-Xa levels may underestimate the anticoagulant effect if the assay does not add exogenous ATIII (though most "heparin level" assays do not, "Anti-Xa" assays for monitoring often do not add AT, reflecting in vivo efficacy) [cite: 4, 22]. Furthermore, high plasma free hemoglobin (hemolysis) and hyperbilirubinemia can interfere with the assay [cite: 20, 22].

### Viscoelastic Testing (TEG/ROTEM)
Thromboelastography (TEG) and Rotational Thromboelastometry (ROTEM) provide a global assessment of hemostasis, including clot initiation, strength, and fibrinolysis.
*   **Utility:** TEG can differentiate between enzymatic anticoagulation (heparin effect) and factor/platelet deficiency. The R-time (reaction time) is used to monitor heparin; a target of 2–4 times baseline (or 16–24 minutes) is often used [cite: 4].
*   **Comparison:** In randomized trials, TEG-guided dosing resulted in lower heparin doses compared to aPTT-guided dosing, with a trend toward fewer bleeding events [cite: 4]. However, discordance between TEG and standard assays is common [cite: 14].

### Discordance Among Assays
Research indicates a high rate of discordance between aPTT, ACT, and Anti-Xa. For example, a study found that aPTT and Anti-Xa were discordant in 46% of measurements [cite: 14]. Another study highlighted that while aPTT correlates strongly with Anti-Xa in patients with normal ATIII levels, the correlation weakens significantly in patients with ATIII deficiency [cite: 16]. This suggests that a multi-modal monitoring approach, rather than reliance on a single metric, may be safer.

---

## Heparin Resistance and Antithrombin III

Heparin resistance is a frequent complication in ECMO, defined as the requirement for unusually high doses of heparin (e.g., >35,000 units/day or >20 units/kg/h) to achieve therapeutic targets [cite: 23].

### Mechanisms
The primary mechanism of UFH is the potentiation of Antithrombin III (ATIII), which inhibits Thrombin and Factor Xa.
*   **ATIII Deficiency:** Critically ill patients, particularly those with sepsis or on prolonged ECMO, often develop acquired ATIII deficiency due to consumption, reduced synthesis (liver dysfunction), and hemodilution [cite: 23, 24]. Neonates have naturally lower ATIII levels (approx. 50% of adult values) [cite: 25].
*   **Acute Phase Reactants:** High levels of heparin-binding proteins (e.g., vitronectin, fibrinogen) can compete with ATIII for heparin binding, reducing its efficacy [cite: 16, 23].

### Management of Resistance
1.  **Dose Escalation:** The simplest approach is to increase the heparin dose. Studies suggest that increasing the dose is generally safe and does not necessarily increase bleeding rates compared to non-resistant patients [cite: 23].
2.  **Antithrombin Supplementation:** Administering ATIII concentrates or Fresh Frozen Plasma (FFP) to maintain ATIII activity >50% or >80% is a common but controversial practice [cite: 4, 22].
    *   *Arguments For:* Supplementation restores heparin sensitivity, lowers heparin dose requirements, and may reduce circuit thrombosis [cite: 22, 24].
    *   *Arguments Against:* A meta-analysis and retrospective studies have shown that while ATIII supplementation reduces heparin requirements, it does not consistently reduce mortality or bleeding, and in some cases, may be associated with increased thrombotic events (possibly due to rebound effects or underlying severity of illness) [cite: 4, 26]. Routine supplementation is not currently universally recommended by ELSO but is left to institutional discretion [cite: 4, 22].
3.  **Alternative Anticoagulants:** Switching to Direct Thrombin Inhibitors (DTIs) like bivalirudin or argatroban bypasses the need for ATIII. Bivalirudin has shown more predictable pharmacokinetics and stable anticoagulation profiles in ECMO patients compared to heparin [cite: 27, 28].

---

## Balancing Risks: Bleeding vs. Thrombosis

The therapeutic window for heparin in ECMO is narrow. The goal is to balance the prevention of circuit thrombosis (which can lead to oxygenator failure and embolism) against the risk of patient hemorrhage.

### Bleeding Complications
Bleeding occurs in 30–60% of ECMO patients and is a leading cause of mortality [cite: 1].
*   **Risk Factors:** Post-cardiotomy status, trauma, coagulopathy (low fibrinogen, thrombocytopenia), and supratherapeutic anticoagulation [cite: 1].
*   **Sites:** Surgical sites, cannulation sites, and intracranial hemorrhage (ICH) are most common. ICH is particularly devastating, with high mortality [cite: 29, 30].
*   **Management:** In the event of major bleeding, heparin is often paused. Evidence suggests that pausing heparin for 12–24 hours (or even days) is feasible if flow rates are maintained [cite: 6, 31].

### Thrombotic Complications
Thrombosis can occur within the patient (DVT, PE, stroke) or the circuit (oxygenator clots, pump thrombus).
*   **Incidence:** Circuit thrombosis occurs in 10–30% of cases [cite: 29].
*   **Prevention:** Adequate anticoagulation and maintaining high circuit flow rates are the primary preventative measures. Low flow states (<3 L/min) significantly increase the risk of stasis and clot formation [cite: 32, 33].

---

## Alternative and Sparing Strategies

In patients with prohibitive bleeding risks (e.g., severe trauma, recent neurosurgery, active hemorrhage), standard heparin protocols are dangerous. "Heparin-sparing" or "heparin-free" strategies have emerged as viable alternatives.

### Heparin-Sparing / Heparin-Free ECMO
This approach involves withholding systemic anticoagulation either entirely or for prolonged periods.
*   **Feasibility:** Studies have demonstrated that VV-ECMO and VA-ECMO can be managed without heparin for days (mean duration without heparin ~80 hours in some studies) without a significant increase in pump failure or thromboembolic complications [cite: 8, 33].
*   **Key Requirement:** High blood flow (>3 L/min) is critical to prevent stasis within the oxygenator and circuit [cite: 32, 33].
*   **Outcomes:** Survival and thrombotic event rates in heparin-sparing groups are often comparable to fully anticoagulated groups, suggesting that the intrinsic thrombogenicity of modern coated circuits is lower than historically believed [cite: 8, 34, 35].

### Direct Thrombin Inhibitors (DTIs)
Bivalirudin and Argatroban are increasingly used, especially in cases of Heparin-Induced Thrombocytopenia (HIT) or severe heparin resistance.
*   **Bivalirudin:** Offers enzymatic inhibition of thrombin without requiring ATIII. It has a short half-life (~25 mins) and is partly metabolized by proteolysis, making it safer in renal/hepatic failure than heparin. Some data suggest it leads to less bleeding and more time in therapeutic range than UFH [cite: 5, 6, 27].
*   **Argatroban:** Hepatically cleared, used primarily in HIT. Requires careful monitoring in patients with liver dysfunction [cite: 6, 20].

---

## Protocol for Management of Bleeding and Restarting Heparin

When bleeding complications occur, a structured approach to pausing and restarting anticoagulation is essential.

### Management of Active Bleeding
1.  **Cessation:** Stop heparin infusion immediately.
2.  **Correction:** Correct coagulopathies aggressively.
    *   Platelets: Target >50,000–100,000/mm³ [cite: 7, 31].
    *   Fibrinogen: Target >1.5 g/L (using Cryoprecipitate) [cite: 31].
    *   INR: Target <1.3–1.5 (using FFP or Prothrombin Complex Concentrate) [cite: 31].
3.  **Circuit Flow:** Maintain high circuit flow rates to prevent thrombosis during the heparin-free period [cite: 6, 33].

### Restarting Heparin
The timing of resumption depends on the severity of bleeding and the type of intervention.
*   **Minor/Controlled Bleeding:** Heparin can often be restarted after 12–24 hours of hemostasis [cite: 31].
*   **Post-Surgical:** For high-bleeding risk procedures (e.g., thoracotomy), delay restart for 24–48 hours. For neurosurgery or intracranial hemorrhage, delays of 48–72 hours or longer (up to 7 days) are often necessary and have been shown to be safe regarding circuit patency [cite: 30, 36, 37].
*   **Titration:** Restart at a lower dose (e.g., no bolus, infusion at 5–10 units/kg/h) and titrate slowly [cite: 36, 38].

---

## Conclusion

Managing heparin dosage during ECMO is a dynamic exercise in risk stratification. While ELSO guidelines provide a framework (initial bolus 50–100 U/kg, maintenance 7.5–20 U/kg/h), clinical practice must be tailored to the individual patient. The emergence of Anti-Xa monitoring offers improved specificity over ACT and aPTT, though discordance remains a clinical reality.

The most significant shift in recent practice is the recognition that lower levels of anticoagulation—or even heparin-free intervals—are tolerated well by modern ECMO circuits, particularly when flow rates are maintained. This allows clinicians to prioritize hemostasis in bleeding patients without inevitably sacrificing circuit integrity. Future research will likely focus on the broader adoption of bivalirudin and the refinement of viscoelastic testing to guide personalized anticoagulation strategies.

### References
[cite: 4] PMC6753426
[cite: 16] PMC8112950
[cite: 39] PMC8216320
[cite: 13] PMC10635598
[cite: 14] firstwordpharma.com/story/5933684
[cite: 6] PMC8062644
[cite: 5] researchgate.net/publication/357984019
[cite: 34] PMC10212260
[cite: 35] pubmed.ncbi.nlm.nih.gov/31277018
[cite: 27] PMC9782867
[cite: 8] cdn.fortunejournals.com/articles/the-safety-of-heparinfree-strategy-in-patients-supported-by-venoarterial.pdf
[cite: 3] PMC12597358
[cite: 1] PMC9020579
[cite: 17] ovid.com/journals/ajrccm/fulltext/10.1164/rccm.202305-0896oc~anticoagulation-and-bleeding-during-veno-venous
[cite: 10] cdn-links.lww.com/permalink/asaio/b/asaio_1_1_2023_10_27_sath_1_sdc1.pdf
[cite: 18] researchgate.net/figure/Anticoagulation-protocol-for-ECMO-and-Procedures_tbl1_232721043
[cite: 29] annalscts.com/article/view/16529/pdf
[cite: 22] PMC6971875
[cite: 40] pubmed.ncbi.nlm.nih.gov/24296776/
[cite: 24] PMC12620714
[cite: 41] blog.transonic.com/mechanical-circulatory-support/critical-covid-19-cases-challenge-ecmo-centers
[cite: 32] PMC9811850
[cite: 2] mdpi.com/2077-0383/11/17/5147
[cite: 42] PMC10878372
[cite: 38] cdn-links.lww.com/permalink/aacr/a/aacr_2020_06_18_rezny_xaa-d-20-00140_sdc1.pdf
[cite: 9] elsolatam.net/wp-content/uploads/2020/08/Extracorporeal_Life_Support_Organization__ELSO-2020.pdf
[cite: 6] PMC8062644
[cite: 8] cdn.fortunejournals.com/articles/the-safety-of-heparinfree-strategy-in-patients-supported-by-venoarterial.pdf
[cite: 43] heartuniversity.org/wp-content/uploads/ELSO-2018-Guidelines-Pediatric-Cardiac-Failure.pdf
[cite: 23] PMC9019066
[cite: 11] frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2022.884063/full
[cite: 20] PMC9187844
[cite: 12] vcportal.ventura.org/vchca/hospitals/pharmacy%20resources/heparin-drip-protocol.pdf
[cite: 4] PMC6753426
[cite: 31] ecmo.icu/daily-care-anticoagulation-bleeding/
[cite: 10] cdn-links.lww.com/permalink/asaio/b/asaio_1_1_2023_10_27_sath_1_sdc1.pdf
[cite: 1] PMC9020579
[cite: 6] PMC8062644
[cite: 36] droracle.ai/articles/575433/when-should-heparin-unfractionated-heparin-be-restarted-after-a
[cite: 30] PMC10236353
[cite: 37] ahajournals.org/doi/10.1161/JAHA.123.032094
[cite: 23] PMC9019066
[cite: 28] ashpublications.org/hematology/article/2024/1/186/526159/Troubleshooting-heparin-resistance
[cite: 25] PMC12322988
[cite: 26] researchgate.net/publication/394279232_The_impact_of_antithrombin_III_supplementation_on_prognosis_during_extracorporeal_membrane_oxygenation_a_systematic_review_and_meta-analysis
[cite: 15] pubmed.ncbi.nlm.nih.gov/34055407/
[cite: 21] outbreak.info/resources/pmid36478046
[cite: 19] PMC4576157
[cite: 13] PMC10635598
[cite: 33] researchgate.net/publication/308547357_Is_Stopping_Heparin_Safe_in_Patients_on_Extracorporeal_Membrane_Oxygenation_Treatment
[cite: 7] en.wikipedia.org/wiki/Extracorporeal_membrane_oxygenation
[cite: 6] PMC8062644
[cite: 5] researchgate.net/publication/357984019_2021_ELSO_Adult_and_Pediatric_Anticoagulation_Guidelines
[cite: 6] PMC8062644
[cite: 33] researchgate.net/publication/308547357_Is_Stopping_Heparin_Safe_in_Patients_on_Extracorporeal_Membrane_Oxygenation_Treatment
[cite: 7] en.wikipedia.org/wiki/Extracorporeal_membrane_oxygenation

**Sources:**
1. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbbErfgOThSi_oQJXz4CbXCcOSyOw50c_LHoKUqIiEzZtyfmgCqGB82MzCmhQqLQZTtVcE3ukTndkwc94LKEgYJ15sJrLt35lfX6aqYjua8r-proxxf1opdswwMeOJnvNHDqKslb2t)
2. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHODmmhu2IhVQDPWQKpd5mhW2yAZjU9AJiKPw1vtS1HSDy0qnDi4kX0_Hxx_N8gzKopZgerFi5NgjL22EWlUDbMhr9GO5-FONQUe_ZByCAkwBy5ijiyZ4DTEC8qvuHxlg==)
3. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgAjKo5Lj3xxIiT8sieLb-epybmVcRodF1tu8ApDcL0IiHo9q6rH20p8reMB3aRmNZ-2Flsr96nisCbCvKV1RFjRZbHK0ItF7vbHpx9YKTRNN1rwkvTknJ0IezB3GqdkTaSQBOS1vswg==)
4. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgawDDl456z6fBdWRBs5C9OlnKpMujtxFYVbvyhQfkYOi6lQJHf1h4KTE5PMwBpAs9zA2bO6X6REmjlO6G5ZmCUFCIbQuN3JYAtYvPdisosuK5YrCiOtbAW7ikJpoGLp1ChcSRvj7Q)
5. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0y5nBRmoU_lT7vEv1aruiZVpsTkxCruEwgOwxbfjl68mC4QBe3KT9fJX2CuYk3tcsCU2ayW9a3PlTZOYQYUIHtfoP9lkGRMEa-zJEGRFHsGk4EaYakttT7Lo5T-oPJq_Bkg8yebLvBfaNcxC9Wx4FyCkvszP8M9_DXAL8QKc1h2o4RvMLx6wpajOrSyRA4uQBPDkWT_8FT6n5RbQz6ZyX_g==)
6. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXtrA67AlHDPCqSvbSwAvwLGyqQigJy9xAqNE4KW00sB5VRUznOxGCmYkeR9P_rXx4O8WKpgrrhtynCvhZxqooyak3UswJBfLdchv8ouB9g77WtwP185fMd-uSbNOQxwJcVieI4p_p)
7. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqpLmUGST42bJNPuJim-zP0EozmltYFA2mXaHxDhVGKSagVMO1ptHY7Ps-i_-JqyKJMAMNmx7BoxeaiU9vTf_HzMLoc-PhR28aYsybs0IqTx0yf2ad81tSYRdrb3-gAGtC5MxsjVvNGIfSWGIYX4dz7XHMB7UOHA==)
8. [fortunejournals.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRSGsd1SpuGSh3j6YsDAFpWbLrcigECNttxEa4F-in_O4Dp5QKofWJ5VjV6ap2eSlu_9L4TEYwnsU5BB-58MsBwHDxfLOfvUXXvU7HLbhcAlunAqtGIn9O_MVQV1sinSD8R42488FOXrreMDDVDyCqOBYabtuZiKmo8r951mjZJQGG_JP0pwz7WOzyynFOBfvA5_EBMNQ6hnj2NGzl1jr_ClWuFDEpwAW-Nvk=)
9. [elsolatam.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZ45ik4L03jUsCr3294JJx8hGasao82LyiuVnGAPR1P3uyFIPl7sMNUyPRINhk1fV21PSF8OTHG7LOZKjtot8LYDJPbT6rO4vYqS233BDm_bK1UH6uEbtGt27nQfWN_AyHS14KfS4h3IoJe0mhQ6wMOSOw_Gd8xv8F5r7YWT0D_AI551I5i9NXArmHk3Rn6m-yROxo_wWTukPzrMmivA==)
10. [lww.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHt4XOQBC-CfZmv4cp5RmnpXDYgrp_B4IBDr013BFE3FWrnytsrgVSgL9DRGSINTzu-0uABC9FXQKL-La6DwoxEHlUTWXPh_9nGdPJKmUaqtmUpuyWlztyLmzG8VFNJSRbVHEG_cZtlRqHUnN40hkCmIq30jqq4cBhpfr8ZaLJVTCggSpyhLg==)
11. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCJ-Ndf9Mhf9SXBJy4aoBkn_xgKQSAnu_vF3cQD6rsboi_5VbYsrLEq8fGvCfbDAu7HGpzPDfGlziR9FpTGS_k3sm4sMoTL-dnxZr-sab7VvIYkAqvE-YqABsHxfTUhosDpSvKrWBrVj7bT9YaAX9mLf4cx3nYnt9md_V_dFAZum5xm7usKzPMkkBZk3d1pWo9S71NJzqoRwI=)
12. [ventura.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJqf1kyyEREWTUqdhrBXAXPX_KgABF_-WJlqZhacyvT3t3VzuaM9pJBpXJgs42K3hAGlZBAqOGzn3-EDPCC12wRHfXPl_YtgmmCc0HylcjQ5SikU2SvwUv3tD4TIT20Oi400_Jkd0AhdqXSHtykJYUuFbu4Y6h0B9421_5k0aHcYckzFrfhiUQxr79xjeRzhQ=)
13. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFldB6OjQ2keDwzmNxCbuz--vv37yZ8jlaANY8CMXeR1BXldeKzFzhOq5xpXAGpwiJp7oXHB3OBm8hKXmMvWAF7xEOoQkxhCyY38gcbRUB-iUhTV8FUnrzKYFpH-Y9NN9VLuvBGo_rWAQ==)
14. [firstwordpharma.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNuBJjQU-HggOiQdcpUk31YQWtQrVl1QuNhBHo-KZu7ZcHMpSiK9-zcXSsafLd1yfoF1Iu0NYJpn8OGI37ChUVuD4Fe2s8cYh50iwnjV0HhhK088QTo_x3RQoBYVFnwA==)
15. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHv1Bmc-H2qtlDzjSUGmMpujfX5MmqIRKVb7FGj6IhtFiBPPEhKFqwWEzjHw1H7BzWCo6SZGulvRuCTewS3MTfobWU058cN8O3MZMYFoCPVq8xGb4xAcCrXECdSzoWYXg==)
16. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlN39niJcAS998XbdVu2Eqh4pr01E1eGvziWR1qJ5DUARi-pmkwCp2lUT4J1wjzEQoIabcf1PKLRWP_QSVsox5tNhGrZiXLDzCDdmjTfHrY7cZQCTa9zoBAk_ioG6LXf5N7GaybJEu)
17. [ovid.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1nWDih7Srpe8A64T4yMTS1ZSBvqtq4_s0nKbtVu2dEf-EsrIbMT8VXJ4m4zWBzwroe6PYS9Thu1vOuyA6KnhAYoP-3Mz7tIdVB9-MOudT9wRaXaTUX8SHLcs4Yd-vnHGWhKGhTjK9a4CCpnMvjk28Qnurcxw84JZdr2q-efzUdSakO_6WpvDgJ8NJOFDnnEjUk1-Lf6ZR3tj3urgHXuT244E4ZDPKBPMlxmb-lUg=)
18. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxfQNNjM5pw-ETTPuyXYhrBf9-xGCLFvw_SNGoLL9vR-62rTcJECtTuhnd4IU-RUroyyJd9Mhq8Xd-9UPnyDO2igdbSzCZwrZ22HdxEqoFJZptA2UuS86LjZ9MABfeUkZ0aX3IJ99S9hjk0qleBuAOvbWWkOE8Q1lgKUMpAuDKqYA3A-zZssIPEn_43ZstZyAzH920xeH3Xoo=)
19. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-XeivKqHOpHtSN_x5lr8Xt3ivx6_4iAXpo_WYJqBe3PzaLfAEOuQ8zAfxJLgFPe6UrLH6lxlXgm1JnFCfZBRHzdKUq7zmd3CJWerzNn9_b1PcmQJXOnc0l0UwUpULyk_IIcgjx60T)
20. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTufz6mR_MTnVKXyFBvmPIh2x4cxAkbGUdDH0UWmGcLOTWB49cnTDujWJjA6ijKkzle2RS_JPYDuIEjmATnwKLFRu4d9NKrIxpq2yvMNft6ddUDuaIVywB8j_4ktGTPe-sADfIPAsh)
21. [outbreak.info](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFM-dBIOKbYffv5EL5dHNZTb-tzX4SCxaOWfBBYEVbXPeTUEp8P_rjisHIPIMmGWdKywa1H0nLjJWaoyzn7i1do5_hOp9E21oacHkiOYOfy-1IvuagHNN2AzRT43ZX6GbZjkA==)
22. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0Klk6lndZPdZnMYhCn0xGtpUbam8_wjbWYXvEYt0CyWCHJkrjdmZuOgJUUOKG3a5LNy6gtcgp9Nj6fq6cQesRoBjzbbl1SObEGxLHb5s0ekzPQcKNRgeYcaaKg2VwOBBYVoXfPCku)
23. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMJkBeOjuxtDzuevM4UTQCr-86-Ln59HRPqeZBnqaRuPI5rK6qXM-XnRsmvJR2fIH__Hy9xs0xRGOhHZHO61LXzHq5OkVmeKKVbEksO2zwHyx8WJFJUWc4eXS1ndhLYFml-YoUN2h3)
24. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCsgh7vQirlRHLBDKHHZeo8VYk5L-5ltOgwBdNMVqGfaOv1GT1J6QHUk-9vtvOfUWNW5iwQ0K5jSS-DWC5HB1uq-5W-u8D3Khi6Kpe-0ZQya4P8EpHb5JB0pESR6_0L8MzHxEm5UySKQ==)
25. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGm3Uy7VQpnX4WreXqpVq_6cgXCumC8SiR8E59m7gG97u3M0URuN5mQEOyDSagQhvpgU7g3MhBbishslIVJLN0glp8lWJnzxOUauHx57mKQHL-D3LmqWNOvUTdcRxv4GfqNHb9h3eDhSg==)
26. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkwx8uUetiN7EkJZdyiarqqrX2QvgBqDLkgCsp_st8phATIOysRzHbXGYjHa2cp0_lHBGp4fN273fLcgJUxkrFh51zEdJ7jXTpFdUmGlOflwZzmIjjt49-xbX5kqzvTk5z0miyI-fk6MtA4kP-yxWAo2LLUQyUWjQplbuk_yvPMXS5-E1XwiOckVymU48mZpVadlfRKDcw6F3nIhJnEjy5rsSBEbO2HYpv0I6opifvZ0USK2mDWIcbymzgCgN9tm5CKRKJh-9JRmkiSZZxWcToGhShlL0kWc9LGiQUhQAFpAUE-FCuKOoXGYhsO-F-SUaGVXag8oA=)
27. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHwOXYP0HWsKGb7Udoc5TQn8KZtvC2u7VeCJx7vIdvenTcNHvOjZ7WthJuK_rZrsW7gIHRKMhGrGmZn74pjqGqS7u1tTmGCkSy-OieoSg9oJdsMobYFpkORbr2jS6mOd47Mh56Xa-O)
28. [ashpublications.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMIeKazBW-lyElNIte-V2wkrfF-hBB-Oi8-DQABTwGxnrXaF3qgO2qcNCcTl0AQDFJK0hzvGKsoTcDx9pEI0E9aLbL5uykQHL9QNgrRZwpct83yw-5fy9vuujvEMTmD374YX3ECOK-IUoRJ878xQ6dFZ7T7SGCOSWVlUqDbpK_RtgnFKO2u5AVdhoAsTYBVJp0pRsc3yGwLmM=)
29. [annalscts.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgBr3-CZgpkwe6YE8fl0XZw_a9ymKDux7BpZBue356gsBunAoqxL442xfUd0poQIOy1DveHyAT5hBS1QsFnc0Iqzv3tKRTRXC-XuKTOkeeU8lvGrJhL9GIxkhSATO8j_NQL-7le4g=)
30. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2i64is9pHLfNyplAUcT2Z9fZNlTamyMpIKmrAoHTIt2xLVFOjBLiuOWNZwPkKCw4kUw6Gb1enQbADeImTOyBKFjJ8h2eLx6DPeCXwvH6zVNI6_2uftSiYJ81vPJDoRo4v8ZRDt28TdA==)
31. [ecmo.icu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZyEMTX1WxhHlhuYYE-AV4QnJSaQrgh7swH5iD0jgxqyu9JvZO8we2rEZHX0AD6dX_BGWwCTSIiOIfwBb6WKKCDKIlQ_RADEUDjbeaF8zLWtrjTG6TrkTdLQWQ7F6IMUd12FJikrItveWfbw==)
32. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzJZxdDaOKRzehQDqSFpYmAHiBKQA_-Xmai2LD7p0vxbZJPrbZsgZnBiwggdqjlv3HjdQfRuvvxHsLfcXwTc4z5GeQlSWwBbYqyuXTG20XyaEmZGImLDJSw_OoFuu4sdrWIu_EgXkk)
33. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkHshAwQBIQb0F6oUyUJ_Ls4tZoVPsn4I7wtzgzd9fxZqY8nNVjh8lWOmFeKrDPsjmegHZ7E4MKoIED5wi_BsjLuqjmDzM-Z0Vw_w-6QvwsHb2587GUsoaKhGzk0DEBdcEc8KV97VQ4UikF7RbAdzT6Pq4kAYw3h28mCOKhoFRGsGCgXzB0iYrilHedD_JfEvVdyQfGwCx-6TtXmy6d4mvwJLxpt3F7y08vEdnGO3bwYAhbTkXtWcppmopdPspKg==)
34. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTXN15wvY1uyfogqsIoZO5YVAs-1xUmoKb7kmsTk-16tJ1903EP29fgNfO6TwjblueuV85JvEH-BfDETXt8JzUrn3BRNWavn5HJ2TSPufvWjcQ8co8zyB17gPcKZWOXyQ4tC6hWAyxWg==)
35. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlZteviB67iKCS0L29-B8CDW3aT3Vf3X_YsmFd3yA_4c6HE1IzJFXIASOpeRbMamq0dqF2dE5-kIE563vuqVR_b-2RQh2b5IdFWv3pkCB1-X94GbBamTq-XvEaPfS7jw==)
36. [droracle.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGC3O8DCc5v3CV_a4TLRLvrfLSV35egeVUcjDc-kNN-vFUNKC18kM2krAb-ySYLDNWCUd6wats9Wn568oYh28LWVRp5pNzoNoec0JOD8CMcqVWIo3OeHUzMY626mNjJC-NIVyUyngIlFegcf1JSBo9BikJj9eWQQ0mq5vfkNqXtIikFg69uZci0HlECH68ydYDBj3sS3BBIwpzln-Ak)
37. [ahajournals.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfEVfVSWJiABHSLvkBTPFXjckvVh2kJeSacghNehMCnJMpG8mPMNhRXIQyhUWMl9Q8zC_If-sDxqv1orWQIEC_xdV0g0OVUP9oBvUR7TpFlu2Hw8LxBSgrGMbNTiMGvid27w2F9lkaCMqGQiCB)
38. [lww.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE07i0SzhcV60hMgAJsW52b_Onf1omuW5mRWbd4desUndkBB8zy6CI1fxHo07dP1VjoINi8nHl1pZ_HNNL_KXriAgTW9ck7fJNze2nvEkJNM8uyjhLXmoCqEzfES4RQ7KAkvdV2mPwyvs3_HXSyOiqHcJKBsSOKXql1uP6CDGLE8pKpGO4Fd23yqMxzwYIX)
39. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYK3aH3cerj5TA-_tZRJB1tUIYDLZVbUv3l4wix_SYQgNzMElWFR5gK6v1gJxACSqjSOSKj6r62P-s93xTNzEtfPgafiDo6mMw1CunjfarV13F-clNhQgscMBkbGHiQAh2_JtZti7z)
40. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHp6ihngxoWLuc1CCruFAzZbfi-XQbWIdFlD3MfwglWhRhubPDrZB3dAPJmOv2y_QdiyUGAsRZR6HPlZ0SqsMqnCwbCFVOFrnu5d8-ZV5YU0e9PmHXUcm8CVnNHnfiaMQ==)
41. [transonic.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLP2UOP1TWaAZaktSFcQnu-fQ-32RY_ukelmqoKNd47CuWDLTiqqYE-y11NOeGNBkjX8NrxlzUE-aQ0aJc_NHI1xONDuwgC56qH8oewQFTaUth-v8XtFRoNWsfhRNuG27pTHCgqtxWCZfrNxXKvrNKbQp7KHkdGn27l7IC6vyYSaNNAj5VF6AwrLD5r4-m0jTAH__bLDsaZtm97-ej_Q==)
42. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPslDIQEmPX6JbYY0gsD0lR-rnEPhqCur_2-z-LyM1J2mEEazEhC-JObqgwL42MpKmI-Ga3wQirlf45Y8imf_4-Fj1xd3F2oqB7gz66Kqxd2_buwD2-5VOBvTG-gFHn4xxU2xqcj1yaQ==)
43. [heartuniversity.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnLbi-UBMfE8BH_KYxYBDZGTtH4tW_mCoC4bxtpgNAea0AniLc-ffo3PeMB8lZLVz3qv4zHXOf5hvpmHZshE_bAHm_4u_Jwv2UJ0MMxEZoUWb-D30mISRQ4wcbbLGeErtdFuL2aG_xhpa6OsDM0tdICe4FkNYTAR_xvGgUJy84epF1aCQuzE3TlWMScxKFoGd0_lSUNnPZLjsZ_g==)


## Annotations
Annotation(end_index=1761, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbbErfgOThSi_oQJXz4CbXCcOSyOw50c_LHoKUqIiEzZtyfmgCqGB82MzCmhQqLQZTtVcE3ukTndkwc94LKEgYJ15sJrLt35lfX6aqYjua8r-proxxf1opdswwMeOJnvNHDqKslb2t', start_index=1749)
Annotation(end_index=1761, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHODmmhu2IhVQDPWQKpd5mhW2yAZjU9AJiKPw1vtS1HSDy0qnDi4kX0_Hxx_N8gzKopZgerFi5NgjL22EWlUDbMhr9GO5-FONQUe_ZByCAkwBy5ijiyZ4DTEC8qvuHxlg==', start_index=1749)
Annotation(end_index=2081, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbbErfgOThSi_oQJXz4CbXCcOSyOw50c_LHoKUqIiEzZtyfmgCqGB82MzCmhQqLQZTtVcE3ukTndkwc94LKEgYJ15sJrLt35lfX6aqYjua8r-proxxf1opdswwMeOJnvNHDqKslb2t', start_index=2069)
Annotation(end_index=2081, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgAjKo5Lj3xxIiT8sieLb-epybmVcRodF1tu8ApDcL0IiHo9q6rH20p8reMB3aRmNZ-2Flsr96nisCbCvKV1RFjRZbHK0ItF7vbHpx9YKTRNN1rwkvTknJ0IezB3GqdkTaSQBOS1vswg==', start_index=2069)
Annotation(end_index=2265, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0y5nBRmoU_lT7vEv1aruiZVpsTkxCruEwgOwxbfjl68mC4QBe3KT9fJX2CuYk3tcsCU2ayW9a3PlTZOYQYUIHtfoP9lkGRMEa-zJEGRFHsGk4EaYakttT7Lo5T-oPJq_Bkg8yebLvBfaNcxC9Wx4FyCkvszP8M9_DXAL8QKc1h2o4RvMLx6wpajOrSyRA4uQBPDkWT_8FT6n5RbQz6ZyX_g==', start_index=2253)
Annotation(end_index=2265, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgawDDl456z6fBdWRBs5C9OlnKpMujtxFYVbvyhQfkYOi6lQJHf1h4KTE5PMwBpAs9zA2bO6X6REmjlO6G5ZmCUFCIbQuN3JYAtYvPdisosuK5YrCiOtbAW7ikJpoGLp1ChcSRvj7Q', start_index=2253)
Annotation(end_index=3152, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXtrA67AlHDPCqSvbSwAvwLGyqQigJy9xAqNE4KW00sB5VRUznOxGCmYkeR9P_rXx4O8WKpgrrhtynCvhZxqooyak3UswJBfLdchv8ouB9g77WtwP185fMd-uSbNOQxwJcVieI4p_p', start_index=3140)
Annotation(end_index=3152, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbbErfgOThSi_oQJXz4CbXCcOSyOw50c_LHoKUqIiEzZtyfmgCqGB82MzCmhQqLQZTtVcE3ukTndkwc94LKEgYJ15sJrLt35lfX6aqYjua8r-proxxf1opdswwMeOJnvNHDqKslb2t', start_index=3140)
Annotation(end_index=3435, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXtrA67AlHDPCqSvbSwAvwLGyqQigJy9xAqNE4KW00sB5VRUznOxGCmYkeR9P_rXx4O8WKpgrrhtynCvhZxqooyak3UswJBfLdchv8ouB9g77WtwP185fMd-uSbNOQxwJcVieI4p_p', start_index=3423)
Annotation(end_index=3435, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqpLmUGST42bJNPuJim-zP0EozmltYFA2mXaHxDhVGKSagVMO1ptHY7Ps-i_-JqyKJMAMNmx7BoxeaiU9vTf_HzMLoc-PhR28aYsybs0IqTx0yf2ad81tSYRdrb3-gAGtC5MxsjVvNGIfSWGIYX4dz7XHMB7UOHA==', start_index=3423)
Annotation(end_index=3713, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRSGsd1SpuGSh3j6YsDAFpWbLrcigECNttxEa4F-in_O4Dp5QKofWJ5VjV6ap2eSlu_9L4TEYwnsU5BB-58MsBwHDxfLOfvUXXvU7HLbhcAlunAqtGIn9O_MVQV1sinSD8R42488FOXrreMDDVDyCqOBYabtuZiKmo8r951mjZJQGG_JP0pwz7WOzyynFOBfvA5_EBMNQ6hnj2NGzl1jr_ClWuFDEpwAW-Nvk=', start_index=3697)
Annotation(end_index=3713, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZ45ik4L03jUsCr3294JJx8hGasao82LyiuVnGAPR1P3uyFIPl7sMNUyPRINhk1fV21PSF8OTHG7LOZKjtot8LYDJPbT6rO4vYqS233BDm_bK1UH6uEbtGt27nQfWN_AyHS14KfS4h3IoJe0mhQ6wMOSOw_Gd8xv8F5r7YWT0D_AI551I5i9NXArmHk3Rn6m-yROxo_wWTukPzrMmivA==', start_index=3697)
Annotation(end_index=3713, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHt4XOQBC-CfZmv4cp5RmnpXDYgrp_B4IBDr013BFE3FWrnytsrgVSgL9DRGSINTzu-0uABC9FXQKL-La6DwoxEHlUTWXPh_9nGdPJKmUaqtmUpuyWlztyLmzG8VFNJSRbVHEG_cZtlRqHUnN40hkCmIq30jqq4cBhpfr8ZaLJVTCggSpyhLg==', start_index=3697)
Annotation(end_index=3971, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXtrA67AlHDPCqSvbSwAvwLGyqQigJy9xAqNE4KW00sB5VRUznOxGCmYkeR9P_rXx4O8WKpgrrhtynCvhZxqooyak3UswJBfLdchv8ouB9g77WtwP185fMd-uSbNOQxwJcVieI4p_p', start_index=3959)
Annotation(end_index=3971, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgawDDl456z6fBdWRBs5C9OlnKpMujtxFYVbvyhQfkYOi6lQJHf1h4KTE5PMwBpAs9zA2bO6X6REmjlO6G5ZmCUFCIbQuN3JYAtYvPdisosuK5YrCiOtbAW7ikJpoGLp1ChcSRvj7Q', start_index=3959)
Annotation(end_index=4141, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbbErfgOThSi_oQJXz4CbXCcOSyOw50c_LHoKUqIiEzZtyfmgCqGB82MzCmhQqLQZTtVcE3ukTndkwc94LKEgYJ15sJrLt35lfX6aqYjua8r-proxxf1opdswwMeOJnvNHDqKslb2t', start_index=4128)
Annotation(end_index=4141, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCJ-Ndf9Mhf9SXBJy4aoBkn_xgKQSAnu_vF3cQD6rsboi_5VbYsrLEq8fGvCfbDAu7HGpzPDfGlziR9FpTGS_k3sm4sMoTL-dnxZr-sab7VvIYkAqvE-YqABsHxfTUhosDpSvKrWBrVj7bT9YaAX9mLf4cx3nYnt9md_V_dFAZum5xm7usKzPMkkBZk3d1pWo9S71NJzqoRwI=', start_index=4128)
Annotation(end_index=4377, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJqf1kyyEREWTUqdhrBXAXPX_KgABF_-WJlqZhacyvT3t3VzuaM9pJBpXJgs42K3hAGlZBAqOGzn3-EDPCC12wRHfXPl_YtgmmCc0HylcjQ5SikU2SvwUv3tD4TIT20Oi400_Jkd0AhdqXSHtykJYUuFbu4Y6h0B9421_5k0aHcYckzFrfhiUQxr79xjeRzhQ=', start_index=4367)
Annotation(end_index=4607, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHt4XOQBC-CfZmv4cp5RmnpXDYgrp_B4IBDr013BFE3FWrnytsrgVSgL9DRGSINTzu-0uABC9FXQKL-La6DwoxEHlUTWXPh_9nGdPJKmUaqtmUpuyWlztyLmzG8VFNJSRbVHEG_cZtlRqHUnN40hkCmIq30jqq4cBhpfr8ZaLJVTCggSpyhLg==', start_index=4597)
Annotation(end_index=4873, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXtrA67AlHDPCqSvbSwAvwLGyqQigJy9xAqNE4KW00sB5VRUznOxGCmYkeR9P_rXx4O8WKpgrrhtynCvhZxqooyak3UswJBfLdchv8ouB9g77WtwP185fMd-uSbNOQxwJcVieI4p_p', start_index=4861)
Annotation(end_index=4873, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbbErfgOThSi_oQJXz4CbXCcOSyOw50c_LHoKUqIiEzZtyfmgCqGB82MzCmhQqLQZTtVcE3ukTndkwc94LKEgYJ15sJrLt35lfX6aqYjua8r-proxxf1opdswwMeOJnvNHDqKslb2t', start_index=4861)
Annotation(end_index=4990, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXtrA67AlHDPCqSvbSwAvwLGyqQigJy9xAqNE4KW00sB5VRUznOxGCmYkeR9P_rXx4O8WKpgrrhtynCvhZxqooyak3UswJBfLdchv8ouB9g77WtwP185fMd-uSbNOQxwJcVieI4p_p', start_index=4978)
Annotation(end_index=4990, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgawDDl456z6fBdWRBs5C9OlnKpMujtxFYVbvyhQfkYOi6lQJHf1h4KTE5PMwBpAs9zA2bO6X6REmjlO6G5ZmCUFCIbQuN3JYAtYvPdisosuK5YrCiOtbAW7ikJpoGLp1ChcSRvj7Q', start_index=4978)
Annotation(end_index=5106, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbbErfgOThSi_oQJXz4CbXCcOSyOw50c_LHoKUqIiEzZtyfmgCqGB82MzCmhQqLQZTtVcE3ukTndkwc94LKEgYJ15sJrLt35lfX6aqYjua8r-proxxf1opdswwMeOJnvNHDqKslb2t', start_index=5093)
Annotation(end_index=5106, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCJ-Ndf9Mhf9SXBJy4aoBkn_xgKQSAnu_vF3cQD6rsboi_5VbYsrLEq8fGvCfbDAu7HGpzPDfGlziR9FpTGS_k3sm4sMoTL-dnxZr-sab7VvIYkAqvE-YqABsHxfTUhosDpSvKrWBrVj7bT9YaAX9mLf4cx3nYnt9md_V_dFAZum5xm7usKzPMkkBZk3d1pWo9S71NJzqoRwI=', start_index=5093)
Annotation(end_index=5204, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXtrA67AlHDPCqSvbSwAvwLGyqQigJy9xAqNE4KW00sB5VRUznOxGCmYkeR9P_rXx4O8WKpgrrhtynCvhZxqooyak3UswJBfLdchv8ouB9g77WtwP185fMd-uSbNOQxwJcVieI4p_p', start_index=5192)
Annotation(end_index=5204, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgawDDl456z6fBdWRBs5C9OlnKpMujtxFYVbvyhQfkYOi6lQJHf1h4KTE5PMwBpAs9zA2bO6X6REmjlO6G5ZmCUFCIbQuN3JYAtYvPdisosuK5YrCiOtbAW7ikJpoGLp1ChcSRvj7Q', start_index=5192)
Annotation(end_index=5309, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJqf1kyyEREWTUqdhrBXAXPX_KgABF_-WJlqZhacyvT3t3VzuaM9pJBpXJgs42K3hAGlZBAqOGzn3-EDPCC12wRHfXPl_YtgmmCc0HylcjQ5SikU2SvwUv3tD4TIT20Oi400_Jkd0AhdqXSHtykJYUuFbu4Y6h0B9421_5k0aHcYckzFrfhiUQxr79xjeRzhQ=', start_index=5296)
Annotation(end_index=5309, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgawDDl456z6fBdWRBs5C9OlnKpMujtxFYVbvyhQfkYOi6lQJHf1h4KTE5PMwBpAs9zA2bO6X6REmjlO6G5ZmCUFCIbQuN3JYAtYvPdisosuK5YrCiOtbAW7ikJpoGLp1ChcSRvj7Q', start_index=5296)
Annotation(end_index=5411, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFldB6OjQ2keDwzmNxCbuz--vv37yZ8jlaANY8CMXeR1BXldeKzFzhOq5xpXAGpwiJp7oXHB3OBm8hKXmMvWAF7xEOoQkxhCyY38gcbRUB-iUhTV8FUnrzKYFpH-Y9NN9VLuvBGo_rWAQ==', start_index=5398)
Annotation(end_index=5411, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgawDDl456z6fBdWRBs5C9OlnKpMujtxFYVbvyhQfkYOi6lQJHf1h4KTE5PMwBpAs9zA2bO6X6REmjlO6G5ZmCUFCIbQuN3JYAtYvPdisosuK5YrCiOtbAW7ikJpoGLp1ChcSRvj7Q', start_index=5398)
Annotation(end_index=5757, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNuBJjQU-HggOiQdcpUk31YQWtQrVl1QuNhBHo-KZu7ZcHMpSiK9-zcXSsafLd1yfoF1Iu0NYJpn8OGI37ChUVuD4Fe2s8cYh50iwnjV0HhhK088QTo_x3RQoBYVFnwA==', start_index=5743)
Annotation(end_index=5757, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHv1Bmc-H2qtlDzjSUGmMpujfX5MmqIRKVb7FGj6IhtFiBPPEhKFqwWEzjHw1H7BzWCo6SZGulvRuCTewS3MTfobWU058cN8O3MZMYFoCPVq8xGb4xAcCrXECdSzoWYXg==', start_index=5743)
Annotation(end_index=6022, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXtrA67AlHDPCqSvbSwAvwLGyqQigJy9xAqNE4KW00sB5VRUznOxGCmYkeR9P_rXx4O8WKpgrrhtynCvhZxqooyak3UswJBfLdchv8ouB9g77WtwP185fMd-uSbNOQxwJcVieI4p_p', start_index=6007)
Annotation(end_index=6022, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbbErfgOThSi_oQJXz4CbXCcOSyOw50c_LHoKUqIiEzZtyfmgCqGB82MzCmhQqLQZTtVcE3ukTndkwc94LKEgYJ15sJrLt35lfX6aqYjua8r-proxxf1opdswwMeOJnvNHDqKslb2t', start_index=6007)
Annotation(end_index=6022, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgawDDl456z6fBdWRBs5C9OlnKpMujtxFYVbvyhQfkYOi6lQJHf1h4KTE5PMwBpAs9zA2bO6X6REmjlO6G5ZmCUFCIbQuN3JYAtYvPdisosuK5YrCiOtbAW7ikJpoGLp1ChcSRvj7Q', start_index=6007)
Annotation(end_index=6265, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0y5nBRmoU_lT7vEv1aruiZVpsTkxCruEwgOwxbfjl68mC4QBe3KT9fJX2CuYk3tcsCU2ayW9a3PlTZOYQYUIHtfoP9lkGRMEa-zJEGRFHsGk4EaYakttT7Lo5T-oPJq_Bkg8yebLvBfaNcxC9Wx4FyCkvszP8M9_DXAL8QKc1h2o4RvMLx6wpajOrSyRA4uQBPDkWT_8FT6n5RbQz6ZyX_g==', start_index=6249)
Annotation(end_index=6265, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlN39niJcAS998XbdVu2Eqh4pr01E1eGvziWR1qJ5DUARi-pmkwCp2lUT4J1wjzEQoIabcf1PKLRWP_QSVsox5tNhGrZiXLDzCDdmjTfHrY7cZQCTa9zoBAk_ioG6LXf5N7GaybJEu', start_index=6249)
Annotation(end_index=6265, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgawDDl456z6fBdWRBs5C9OlnKpMujtxFYVbvyhQfkYOi6lQJHf1h4KTE5PMwBpAs9zA2bO6X6REmjlO6G5ZmCUFCIbQuN3JYAtYvPdisosuK5YrCiOtbAW7ikJpoGLp1ChcSRvj7Q', start_index=6249)
Annotation(end_index=6397, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlN39niJcAS998XbdVu2Eqh4pr01E1eGvziWR1qJ5DUARi-pmkwCp2lUT4J1wjzEQoIabcf1PKLRWP_QSVsox5tNhGrZiXLDzCDdmjTfHrY7cZQCTa9zoBAk_ioG6LXf5N7GaybJEu', start_index=6380)
Annotation(end_index=6397, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgawDDl456z6fBdWRBs5C9OlnKpMujtxFYVbvyhQfkYOi6lQJHf1h4KTE5PMwBpAs9zA2bO6X6REmjlO6G5ZmCUFCIbQuN3JYAtYvPdisosuK5YrCiOtbAW7ikJpoGLp1ChcSRvj7Q', start_index=6380)
Annotation(end_index=6397, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHv1Bmc-H2qtlDzjSUGmMpujfX5MmqIRKVb7FGj6IhtFiBPPEhKFqwWEzjHw1H7BzWCo6SZGulvRuCTewS3MTfobWU058cN8O3MZMYFoCPVq8xGb4xAcCrXECdSzoWYXg==', start_index=6380)
Annotation(end_index=6761, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxfQNNjM5pw-ETTPuyXYhrBf9-xGCLFvw_SNGoLL9vR-62rTcJECtTuhnd4IU-RUroyyJd9Mhq8Xd-9UPnyDO2igdbSzCZwrZ22HdxEqoFJZptA2UuS86LjZ9MABfeUkZ0aX3IJ99S9hjk0qleBuAOvbWWkOE8Q1lgKUMpAuDKqYA3A-zZssIPEn_43ZstZyAzH920xeH3Xoo=', start_index=6744)
Annotation(end_index=6761, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1nWDih7Srpe8A64T4yMTS1ZSBvqtq4_s0nKbtVu2dEf-EsrIbMT8VXJ4m4zWBzwroe6PYS9Thu1vOuyA6KnhAYoP-3Mz7tIdVB9-MOudT9wRaXaTUX8SHLcs4Yd-vnHGWhKGhTjK9a4CCpnMvjk28Qnurcxw84JZdr2q-efzUdSakO_6WpvDgJ8NJOFDnnEjUk1-Lf6ZR3tj3urgHXuT244E4ZDPKBPMlxmb-lUg=', start_index=6744)
Annotation(end_index=6761, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgawDDl456z6fBdWRBs5C9OlnKpMujtxFYVbvyhQfkYOi6lQJHf1h4KTE5PMwBpAs9zA2bO6X6REmjlO6G5ZmCUFCIbQuN3JYAtYvPdisosuK5YrCiOtbAW7ikJpoGLp1ChcSRvj7Q', start_index=6744)
Annotation(end_index=6865, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-XeivKqHOpHtSN_x5lr8Xt3ivx6_4iAXpo_WYJqBe3PzaLfAEOuQ8zAfxJLgFPe6UrLH6lxlXgm1JnFCfZBRHzdKUq7zmd3CJWerzNn9_b1PcmQJXOnc0l0UwUpULyk_IIcgjx60T', start_index=6852)
Annotation(end_index=6865, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgawDDl456z6fBdWRBs5C9OlnKpMujtxFYVbvyhQfkYOi6lQJHf1h4KTE5PMwBpAs9zA2bO6X6REmjlO6G5ZmCUFCIbQuN3JYAtYvPdisosuK5YrCiOtbAW7ikJpoGLp1ChcSRvj7Q', start_index=6852)
Annotation(end_index=7124, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFldB6OjQ2keDwzmNxCbuz--vv37yZ8jlaANY8CMXeR1BXldeKzFzhOq5xpXAGpwiJp7oXHB3OBm8hKXmMvWAF7xEOoQkxhCyY38gcbRUB-iUhTV8FUnrzKYFpH-Y9NN9VLuvBGo_rWAQ==', start_index=7110)
Annotation(end_index=7124, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTufz6mR_MTnVKXyFBvmPIh2x4cxAkbGUdDH0UWmGcLOTWB49cnTDujWJjA6ijKkzle2RS_JPYDuIEjmATnwKLFRu4d9NKrIxpq2yvMNft6ddUDuaIVywB8j_4ktGTPe-sADfIPAsh', start_index=7110)
Annotation(end_index=7268, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFM-dBIOKbYffv5EL5dHNZTb-tzX4SCxaOWfBBYEVbXPeTUEp8P_rjisHIPIMmGWdKywa1H0nLjJWaoyzn7i1do5_hOp9E21oacHkiOYOfy-1IvuagHNN2AzRT43ZX6GbZjkA==', start_index=7258)
Annotation(end_index=7532, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFldB6OjQ2keDwzmNxCbuz--vv37yZ8jlaANY8CMXeR1BXldeKzFzhOq5xpXAGpwiJp7oXHB3OBm8hKXmMvWAF7xEOoQkxhCyY38gcbRUB-iUhTV8FUnrzKYFpH-Y9NN9VLuvBGo_rWAQ==', start_index=7515)
Annotation(end_index=7532, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTufz6mR_MTnVKXyFBvmPIh2x4cxAkbGUdDH0UWmGcLOTWB49cnTDujWJjA6ijKkzle2RS_JPYDuIEjmATnwKLFRu4d9NKrIxpq2yvMNft6ddUDuaIVywB8j_4ktGTPe-sADfIPAsh', start_index=7515)
Annotation(end_index=7532, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgawDDl456z6fBdWRBs5C9OlnKpMujtxFYVbvyhQfkYOi6lQJHf1h4KTE5PMwBpAs9zA2bO6X6REmjlO6G5ZmCUFCIbQuN3JYAtYvPdisosuK5YrCiOtbAW7ikJpoGLp1ChcSRvj7Q', start_index=7515)
Annotation(end_index=7636, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgawDDl456z6fBdWRBs5C9OlnKpMujtxFYVbvyhQfkYOi6lQJHf1h4KTE5PMwBpAs9zA2bO6X6REmjlO6G5ZmCUFCIbQuN3JYAtYvPdisosuK5YrCiOtbAW7ikJpoGLp1ChcSRvj7Q', start_index=7627)
Annotation(end_index=7826, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFldB6OjQ2keDwzmNxCbuz--vv37yZ8jlaANY8CMXeR1BXldeKzFzhOq5xpXAGpwiJp7oXHB3OBm8hKXmMvWAF7xEOoQkxhCyY38gcbRUB-iUhTV8FUnrzKYFpH-Y9NN9VLuvBGo_rWAQ==', start_index=7813)
Annotation(end_index=7826, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgawDDl456z6fBdWRBs5C9OlnKpMujtxFYVbvyhQfkYOi6lQJHf1h4KTE5PMwBpAs9zA2bO6X6REmjlO6G5ZmCUFCIbQuN3JYAtYvPdisosuK5YrCiOtbAW7ikJpoGLp1ChcSRvj7Q', start_index=7813)
Annotation(end_index=7903, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlN39niJcAS998XbdVu2Eqh4pr01E1eGvziWR1qJ5DUARi-pmkwCp2lUT4J1wjzEQoIabcf1PKLRWP_QSVsox5tNhGrZiXLDzCDdmjTfHrY7cZQCTa9zoBAk_ioG6LXf5N7GaybJEu', start_index=7889)
Annotation(end_index=7903, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHv1Bmc-H2qtlDzjSUGmMpujfX5MmqIRKVb7FGj6IhtFiBPPEhKFqwWEzjHw1H7BzWCo6SZGulvRuCTewS3MTfobWU058cN8O3MZMYFoCPVq8xGb4xAcCrXECdSzoWYXg==', start_index=7889)
Annotation(end_index=8262, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0Klk6lndZPdZnMYhCn0xGtpUbam8_wjbWYXvEYt0CyWCHJkrjdmZuOgJUUOKG3a5LNy6gtcgp9Nj6fq6cQesRoBjzbbl1SObEGxLHb5s0ekzPQcKNRgeYcaaKg2VwOBBYVoXfPCku', start_index=8249)
Annotation(end_index=8262, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgawDDl456z6fBdWRBs5C9OlnKpMujtxFYVbvyhQfkYOi6lQJHf1h4KTE5PMwBpAs9zA2bO6X6REmjlO6G5ZmCUFCIbQuN3JYAtYvPdisosuK5YrCiOtbAW7ikJpoGLp1ChcSRvj7Q', start_index=8249)
Annotation(end_index=8383, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTufz6mR_MTnVKXyFBvmPIh2x4cxAkbGUdDH0UWmGcLOTWB49cnTDujWJjA6ijKkzle2RS_JPYDuIEjmATnwKLFRu4d9NKrIxpq2yvMNft6ddUDuaIVywB8j_4ktGTPe-sADfIPAsh', start_index=8369)
Annotation(end_index=8383, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0Klk6lndZPdZnMYhCn0xGtpUbam8_wjbWYXvEYt0CyWCHJkrjdmZuOgJUUOKG3a5LNy6gtcgp9Nj6fq6cQesRoBjzbbl1SObEGxLHb5s0ekzPQcKNRgeYcaaKg2VwOBBYVoXfPCku', start_index=8369)
Annotation(end_index=8843, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgawDDl456z6fBdWRBs5C9OlnKpMujtxFYVbvyhQfkYOi6lQJHf1h4KTE5PMwBpAs9zA2bO6X6REmjlO6G5ZmCUFCIbQuN3JYAtYvPdisosuK5YrCiOtbAW7ikJpoGLp1ChcSRvj7Q', start_index=8834)
Annotation(end_index=9020, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgawDDl456z6fBdWRBs5C9OlnKpMujtxFYVbvyhQfkYOi6lQJHf1h4KTE5PMwBpAs9zA2bO6X6REmjlO6G5ZmCUFCIbQuN3JYAtYvPdisosuK5YrCiOtbAW7ikJpoGLp1ChcSRvj7Q', start_index=9011)
Annotation(end_index=9095, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNuBJjQU-HggOiQdcpUk31YQWtQrVl1QuNhBHo-KZu7ZcHMpSiK9-zcXSsafLd1yfoF1Iu0NYJpn8OGI37ChUVuD4Fe2s8cYh50iwnjV0HhhK088QTo_x3RQoBYVFnwA==', start_index=9085)
Annotation(end_index=9303, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNuBJjQU-HggOiQdcpUk31YQWtQrVl1QuNhBHo-KZu7ZcHMpSiK9-zcXSsafLd1yfoF1Iu0NYJpn8OGI37ChUVuD4Fe2s8cYh50iwnjV0HhhK088QTo_x3RQoBYVFnwA==', start_index=9293)
Annotation(end_index=9500, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlN39niJcAS998XbdVu2Eqh4pr01E1eGvziWR1qJ5DUARi-pmkwCp2lUT4J1wjzEQoIabcf1PKLRWP_QSVsox5tNhGrZiXLDzCDdmjTfHrY7cZQCTa9zoBAk_ioG6LXf5N7GaybJEu', start_index=9490)
Annotation(end_index=9864, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMJkBeOjuxtDzuevM4UTQCr-86-Ln59HRPqeZBnqaRuPI5rK6qXM-XnRsmvJR2fIH__Hy9xs0xRGOhHZHO61LXzHq5OkVmeKKVbEksO2zwHyx8WJFJUWc4eXS1ndhLYFml-YoUN2h3', start_index=9854)
Annotation(end_index=10233, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMJkBeOjuxtDzuevM4UTQCr-86-Ln59HRPqeZBnqaRuPI5rK6qXM-XnRsmvJR2fIH__Hy9xs0xRGOhHZHO61LXzHq5OkVmeKKVbEksO2zwHyx8WJFJUWc4eXS1ndhLYFml-YoUN2h3', start_index=10219)
Annotation(end_index=10233, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCsgh7vQirlRHLBDKHHZeo8VYk5L-5ltOgwBdNMVqGfaOv1GT1J6QHUk-9vtvOfUWNW5iwQ0K5jSS-DWC5HB1uq-5W-u8D3Khi6Kpe-0ZQya4P8EpHb5JB0pESR6_0L8MzHxEm5UySKQ==', start_index=10219)
Annotation(end_index=10318, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGm3Uy7VQpnX4WreXqpVq_6cgXCumC8SiR8E59m7gG97u3M0URuN5mQEOyDSagQhvpgU7g3MhBbishslIVJLN0glp8lWJnzxOUauHx57mKQHL-D3LmqWNOvUTdcRxv4GfqNHb9h3eDhSg==', start_index=10308)
Annotation(end_index=10503, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMJkBeOjuxtDzuevM4UTQCr-86-Ln59HRPqeZBnqaRuPI5rK6qXM-XnRsmvJR2fIH__Hy9xs0xRGOhHZHO61LXzHq5OkVmeKKVbEksO2zwHyx8WJFJUWc4eXS1ndhLYFml-YoUN2h3', start_index=10489)
Annotation(end_index=10503, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlN39niJcAS998XbdVu2Eqh4pr01E1eGvziWR1qJ5DUARi-pmkwCp2lUT4J1wjzEQoIabcf1PKLRWP_QSVsox5tNhGrZiXLDzCDdmjTfHrY7cZQCTa9zoBAk_ioG6LXf5N7GaybJEu', start_index=10489)
Annotation(end_index=10768, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMJkBeOjuxtDzuevM4UTQCr-86-Ln59HRPqeZBnqaRuPI5rK6qXM-XnRsmvJR2fIH__Hy9xs0xRGOhHZHO61LXzHq5OkVmeKKVbEksO2zwHyx8WJFJUWc4eXS1ndhLYFml-YoUN2h3', start_index=10758)
Annotation(end_index=10962, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0Klk6lndZPdZnMYhCn0xGtpUbam8_wjbWYXvEYt0CyWCHJkrjdmZuOgJUUOKG3a5LNy6gtcgp9Nj6fq6cQesRoBjzbbl1SObEGxLHb5s0ekzPQcKNRgeYcaaKg2VwOBBYVoXfPCku', start_index=10949)
Annotation(end_index=10962, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgawDDl456z6fBdWRBs5C9OlnKpMujtxFYVbvyhQfkYOi6lQJHf1h4KTE5PMwBpAs9zA2bO6X6REmjlO6G5ZmCUFCIbQuN3JYAtYvPdisosuK5YrCiOtbAW7ikJpoGLp1ChcSRvj7Q', start_index=10949)
Annotation(end_index=11117, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCsgh7vQirlRHLBDKHHZeo8VYk5L-5ltOgwBdNMVqGfaOv1GT1J6QHUk-9vtvOfUWNW5iwQ0K5jSS-DWC5HB1uq-5W-u8D3Khi6Kpe-0ZQya4P8EpHb5JB0pESR6_0L8MzHxEm5UySKQ==', start_index=11103)
Annotation(end_index=11117, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0Klk6lndZPdZnMYhCn0xGtpUbam8_wjbWYXvEYt0CyWCHJkrjdmZuOgJUUOKG3a5LNy6gtcgp9Nj6fq6cQesRoBjzbbl1SObEGxLHb5s0ekzPQcKNRgeYcaaKg2VwOBBYVoXfPCku', start_index=11103)
Annotation(end_index=11470, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgawDDl456z6fBdWRBs5C9OlnKpMujtxFYVbvyhQfkYOi6lQJHf1h4KTE5PMwBpAs9zA2bO6X6REmjlO6G5ZmCUFCIbQuN3JYAtYvPdisosuK5YrCiOtbAW7ikJpoGLp1ChcSRvj7Q', start_index=11457)
Annotation(end_index=11470, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkwx8uUetiN7EkJZdyiarqqrX2QvgBqDLkgCsp_st8phATIOysRzHbXGYjHa2cp0_lHBGp4fN273fLcgJUxkrFh51zEdJ7jXTpFdUmGlOflwZzmIjjt49-xbX5kqzvTk5z0miyI-fk6MtA4kP-yxWAo2LLUQyUWjQplbuk_yvPMXS5-E1XwiOckVymU48mZpVadlfRKDcw6F3nIhJnEjy5rsSBEbO2HYpv0I6opifvZ0USK2mDWIcbymzgCgN9tm5CKRKJh-9JRmkiSZZxWcToGhShlL0kWc9LGiQUhQAFpAUE-FCuKOoXGYhsO-F-SUaGVXag8oA=', start_index=11457)
Annotation(end_index=11598, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0Klk6lndZPdZnMYhCn0xGtpUbam8_wjbWYXvEYt0CyWCHJkrjdmZuOgJUUOKG3a5LNy6gtcgp9Nj6fq6cQesRoBjzbbl1SObEGxLHb5s0ekzPQcKNRgeYcaaKg2VwOBBYVoXfPCku', start_index=11585)
Annotation(end_index=11598, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgawDDl456z6fBdWRBs5C9OlnKpMujtxFYVbvyhQfkYOi6lQJHf1h4KTE5PMwBpAs9zA2bO6X6REmjlO6G5ZmCUFCIbQuN3JYAtYvPdisosuK5YrCiOtbAW7ikJpoGLp1ChcSRvj7Q', start_index=11585)
Annotation(end_index=11886, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMIeKazBW-lyElNIte-V2wkrfF-hBB-Oi8-DQABTwGxnrXaF3qgO2qcNCcTl0AQDFJK0hzvGKsoTcDx9pEI0E9aLbL5uykQHL9QNgrRZwpct83yw-5fy9vuujvEMTmD374YX3ECOK-IUoRJ878xQ6dFZ7T7SGCOSWVlUqDbpK_RtgnFKO2u5AVdhoAsTYBVJp0pRsc3yGwLmM=', start_index=11872)
Annotation(end_index=11886, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHwOXYP0HWsKGb7Udoc5TQn8KZtvC2u7VeCJx7vIdvenTcNHvOjZ7WthJuK_rZrsW7gIHRKMhGrGmZn74pjqGqS7u1tTmGCkSy-OieoSg9oJdsMobYFpkORbr2jS6mOd47Mh56Xa-O', start_index=11872)
Annotation(end_index=12263, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbbErfgOThSi_oQJXz4CbXCcOSyOw50c_LHoKUqIiEzZtyfmgCqGB82MzCmhQqLQZTtVcE3ukTndkwc94LKEgYJ15sJrLt35lfX6aqYjua8r-proxxf1opdswwMeOJnvNHDqKslb2t', start_index=12254)
Annotation(end_index=12414, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbbErfgOThSi_oQJXz4CbXCcOSyOw50c_LHoKUqIiEzZtyfmgCqGB82MzCmhQqLQZTtVcE3ukTndkwc94LKEgYJ15sJrLt35lfX6aqYjua8r-proxxf1opdswwMeOJnvNHDqKslb2t', start_index=12405)
Annotation(end_index=12584, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgBr3-CZgpkwe6YE8fl0XZw_a9ymKDux7BpZBue356gsBunAoqxL442xfUd0poQIOy1DveHyAT5hBS1QsFnc0Iqzv3tKRTRXC-XuKTOkeeU8lvGrJhL9GIxkhSATO8j_NQL-7le4g=', start_index=12570)
Annotation(end_index=12584, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2i64is9pHLfNyplAUcT2Z9fZNlTamyMpIKmrAoHTIt2xLVFOjBLiuOWNZwPkKCw4kUw6Gb1enQbADeImTOyBKFjJ8h2eLx6DPeCXwvH6zVNI6_2uftSiYJ81vPJDoRo4v8ZRDt28TdA==', start_index=12570)
Annotation(end_index=12789, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXtrA67AlHDPCqSvbSwAvwLGyqQigJy9xAqNE4KW00sB5VRUznOxGCmYkeR9P_rXx4O8WKpgrrhtynCvhZxqooyak3UswJBfLdchv8ouB9g77WtwP185fMd-uSbNOQxwJcVieI4p_p', start_index=12776)
Annotation(end_index=12789, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZyEMTX1WxhHlhuYYE-AV4QnJSaQrgh7swH5iD0jgxqyu9JvZO8we2rEZHX0AD6dX_BGWwCTSIiOIfwBb6WKKCDKIlQ_RADEUDjbeaF8zLWtrjTG6TrkTdLQWQ7F6IMUd12FJikrItveWfbw==', start_index=12776)
Annotation(end_index=13005, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgBr3-CZgpkwe6YE8fl0XZw_a9ymKDux7BpZBue356gsBunAoqxL442xfUd0poQIOy1DveHyAT5hBS1QsFnc0Iqzv3tKRTRXC-XuKTOkeeU8lvGrJhL9GIxkhSATO8j_NQL-7le4g=', start_index=12995)
Annotation(end_index=13233, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkHshAwQBIQb0F6oUyUJ_Ls4tZoVPsn4I7wtzgzd9fxZqY8nNVjh8lWOmFeKrDPsjmegHZ7E4MKoIED5wi_BsjLuqjmDzM-Z0Vw_w-6QvwsHb2587GUsoaKhGzk0DEBdcEc8KV97VQ4UikF7RbAdzT6Pq4kAYw3h28mCOKhoFRGsGCgXzB0iYrilHedD_JfEvVdyQfGwCx-6TtXmy6d4mvwJLxpt3F7y08vEdnGO3bwYAhbTkXtWcppmopdPspKg==', start_index=13219)
Annotation(end_index=13233, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzJZxdDaOKRzehQDqSFpYmAHiBKQA_-Xmai2LD7p0vxbZJPrbZsgZnBiwggdqjlv3HjdQfRuvvxHsLfcXwTc4z5GeQlSWwBbYqyuXTG20XyaEmZGImLDJSw_OoFuu4sdrWIu_EgXkk', start_index=13219)
Annotation(end_index=13918, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRSGsd1SpuGSh3j6YsDAFpWbLrcigECNttxEa4F-in_O4Dp5QKofWJ5VjV6ap2eSlu_9L4TEYwnsU5BB-58MsBwHDxfLOfvUXXvU7HLbhcAlunAqtGIn9O_MVQV1sinSD8R42488FOXrreMDDVDyCqOBYabtuZiKmo8r951mjZJQGG_JP0pwz7WOzyynFOBfvA5_EBMNQ6hnj2NGzl1jr_ClWuFDEpwAW-Nvk=', start_index=13905)
Annotation(end_index=13918, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkHshAwQBIQb0F6oUyUJ_Ls4tZoVPsn4I7wtzgzd9fxZqY8nNVjh8lWOmFeKrDPsjmegHZ7E4MKoIED5wi_BsjLuqjmDzM-Z0Vw_w-6QvwsHb2587GUsoaKhGzk0DEBdcEc8KV97VQ4UikF7RbAdzT6Pq4kAYw3h28mCOKhoFRGsGCgXzB0iYrilHedD_JfEvVdyQfGwCx-6TtXmy6d4mvwJLxpt3F7y08vEdnGO3bwYAhbTkXtWcppmopdPspKg==', start_index=13905)
Annotation(end_index=14050, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkHshAwQBIQb0F6oUyUJ_Ls4tZoVPsn4I7wtzgzd9fxZqY8nNVjh8lWOmFeKrDPsjmegHZ7E4MKoIED5wi_BsjLuqjmDzM-Z0Vw_w-6QvwsHb2587GUsoaKhGzk0DEBdcEc8KV97VQ4UikF7RbAdzT6Pq4kAYw3h28mCOKhoFRGsGCgXzB0iYrilHedD_JfEvVdyQfGwCx-6TtXmy6d4mvwJLxpt3F7y08vEdnGO3bwYAhbTkXtWcppmopdPspKg==', start_index=14036)
Annotation(end_index=14050, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzJZxdDaOKRzehQDqSFpYmAHiBKQA_-Xmai2LD7p0vxbZJPrbZsgZnBiwggdqjlv3HjdQfRuvvxHsLfcXwTc4z5GeQlSWwBbYqyuXTG20XyaEmZGImLDJSw_OoFuu4sdrWIu_EgXkk', start_index=14036)
Annotation(end_index=14310, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRSGsd1SpuGSh3j6YsDAFpWbLrcigECNttxEa4F-in_O4Dp5QKofWJ5VjV6ap2eSlu_9L4TEYwnsU5BB-58MsBwHDxfLOfvUXXvU7HLbhcAlunAqtGIn9O_MVQV1sinSD8R42488FOXrreMDDVDyCqOBYabtuZiKmo8r951mjZJQGG_JP0pwz7WOzyynFOBfvA5_EBMNQ6hnj2NGzl1jr_ClWuFDEpwAW-Nvk=', start_index=14293)
Annotation(end_index=14310, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTXN15wvY1uyfogqsIoZO5YVAs-1xUmoKb7kmsTk-16tJ1903EP29fgNfO6TwjblueuV85JvEH-BfDETXt8JzUrn3BRNWavn5HJ2TSPufvWjcQ8co8zyB17gPcKZWOXyQ4tC6hWAyxWg==', start_index=14293)
Annotation(end_index=14310, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlZteviB67iKCS0L29-B8CDW3aT3Vf3X_YsmFd3yA_4c6HE1IzJFXIASOpeRbMamq0dqF2dE5-kIE563vuqVR_b-2RQh2b5IdFWv3pkCB1-X94GbBamTq-XvEaPfS7jw==', start_index=14293)
Annotation(end_index=14816, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0y5nBRmoU_lT7vEv1aruiZVpsTkxCruEwgOwxbfjl68mC4QBe3KT9fJX2CuYk3tcsCU2ayW9a3PlTZOYQYUIHtfoP9lkGRMEa-zJEGRFHsGk4EaYakttT7Lo5T-oPJq_Bkg8yebLvBfaNcxC9Wx4FyCkvszP8M9_DXAL8QKc1h2o4RvMLx6wpajOrSyRA4uQBPDkWT_8FT6n5RbQz6ZyX_g==', start_index=14800)
Annotation(end_index=14816, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXtrA67AlHDPCqSvbSwAvwLGyqQigJy9xAqNE4KW00sB5VRUznOxGCmYkeR9P_rXx4O8WKpgrrhtynCvhZxqooyak3UswJBfLdchv8ouB9g77WtwP185fMd-uSbNOQxwJcVieI4p_p', start_index=14800)
Annotation(end_index=14816, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHwOXYP0HWsKGb7Udoc5TQn8KZtvC2u7VeCJx7vIdvenTcNHvOjZ7WthJuK_rZrsW7gIHRKMhGrGmZn74pjqGqS7u1tTmGCkSy-OieoSg9oJdsMobYFpkORbr2jS6mOd47Mh56Xa-O', start_index=14800)
Annotation(end_index=14958, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXtrA67AlHDPCqSvbSwAvwLGyqQigJy9xAqNE4KW00sB5VRUznOxGCmYkeR9P_rXx4O8WKpgrrhtynCvhZxqooyak3UswJBfLdchv8ouB9g77WtwP185fMd-uSbNOQxwJcVieI4p_p', start_index=14945)
Annotation(end_index=14958, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTufz6mR_MTnVKXyFBvmPIh2x4cxAkbGUdDH0UWmGcLOTWB49cnTDujWJjA6ijKkzle2RS_JPYDuIEjmATnwKLFRu4d9NKrIxpq2yvMNft6ddUDuaIVywB8j_4ktGTPe-sADfIPAsh', start_index=14945)
Annotation(end_index=15350, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZyEMTX1WxhHlhuYYE-AV4QnJSaQrgh7swH5iD0jgxqyu9JvZO8we2rEZHX0AD6dX_BGWwCTSIiOIfwBb6WKKCDKIlQ_RADEUDjbeaF8zLWtrjTG6TrkTdLQWQ7F6IMUd12FJikrItveWfbw==', start_index=15337)
Annotation(end_index=15350, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqpLmUGST42bJNPuJim-zP0EozmltYFA2mXaHxDhVGKSagVMO1ptHY7Ps-i_-JqyKJMAMNmx7BoxeaiU9vTf_HzMLoc-PhR28aYsybs0IqTx0yf2ad81tSYRdrb3-gAGtC5MxsjVvNGIfSWGIYX4dz7XHMB7UOHA==', start_index=15337)
Annotation(end_index=15422, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZyEMTX1WxhHlhuYYE-AV4QnJSaQrgh7swH5iD0jgxqyu9JvZO8we2rEZHX0AD6dX_BGWwCTSIiOIfwBb6WKKCDKIlQ_RADEUDjbeaF8zLWtrjTG6TrkTdLQWQ7F6IMUd12FJikrItveWfbw==', start_index=15412)
Annotation(end_index=15512, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZyEMTX1WxhHlhuYYE-AV4QnJSaQrgh7swH5iD0jgxqyu9JvZO8we2rEZHX0AD6dX_BGWwCTSIiOIfwBb6WKKCDKIlQ_RADEUDjbeaF8zLWtrjTG6TrkTdLQWQ7F6IMUd12FJikrItveWfbw==', start_index=15502)
Annotation(end_index=15635, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXtrA67AlHDPCqSvbSwAvwLGyqQigJy9xAqNE4KW00sB5VRUznOxGCmYkeR9P_rXx4O8WKpgrrhtynCvhZxqooyak3UswJBfLdchv8ouB9g77WtwP185fMd-uSbNOQxwJcVieI4p_p', start_index=15622)
Annotation(end_index=15635, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkHshAwQBIQb0F6oUyUJ_Ls4tZoVPsn4I7wtzgzd9fxZqY8nNVjh8lWOmFeKrDPsjmegHZ7E4MKoIED5wi_BsjLuqjmDzM-Z0Vw_w-6QvwsHb2587GUsoaKhGzk0DEBdcEc8KV97VQ4UikF7RbAdzT6Pq4kAYw3h28mCOKhoFRGsGCgXzB0iYrilHedD_JfEvVdyQfGwCx-6TtXmy6d4mvwJLxpt3F7y08vEdnGO3bwYAhbTkXtWcppmopdPspKg==', start_index=15622)
Annotation(end_index=15862, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZyEMTX1WxhHlhuYYE-AV4QnJSaQrgh7swH5iD0jgxqyu9JvZO8we2rEZHX0AD6dX_BGWwCTSIiOIfwBb6WKKCDKIlQ_RADEUDjbeaF8zLWtrjTG6TrkTdLQWQ7F6IMUd12FJikrItveWfbw==', start_index=15852)
Annotation(end_index=16164, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGC3O8DCc5v3CV_a4TLRLvrfLSV35egeVUcjDc-kNN-vFUNKC18kM2krAb-ySYLDNWCUd6wats9Wn568oYh28LWVRp5pNzoNoec0JOD8CMcqVWIo3OeHUzMY626mNjJC-NIVyUyngIlFegcf1JSBo9BikJj9eWQQ0mq5vfkNqXtIikFg69uZci0HlECH68ydYDBj3sS3BBIwpzln-Ak', start_index=16146)
Annotation(end_index=16164, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfEVfVSWJiABHSLvkBTPFXjckvVh2kJeSacghNehMCnJMpG8mPMNhRXIQyhUWMl9Q8zC_If-sDxqv1orWQIEC_xdV0g0OVUP9oBvUR7TpFlu2Hw8LxBSgrGMbNTiMGvid27w2F9lkaCMqGQiCB', start_index=16146)
Annotation(end_index=16164, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2i64is9pHLfNyplAUcT2Z9fZNlTamyMpIKmrAoHTIt2xLVFOjBLiuOWNZwPkKCw4kUw6Gb1enQbADeImTOyBKFjJ8h2eLx6DPeCXwvH6zVNI6_2uftSiYJ81vPJDoRo4v8ZRDt28TdA==', start_index=16146)
Annotation(end_index=16290, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE07i0SzhcV60hMgAJsW52b_Onf1omuW5mRWbd4desUndkBB8zy6CI1fxHo07dP1VjoINi8nHl1pZ_HNNL_KXriAgTW9ck7fJNze2nvEkJNM8uyjhLXmoCqEzfES4RQ7KAkvdV2mPwyvs3_HXSyOiqHcJKBsSOKXql1uP6CDGLE8pKpGO4Fd23yqMxzwYIX', start_index=16276)
Annotation(end_index=16290, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGC3O8DCc5v3CV_a4TLRLvrfLSV35egeVUcjDc-kNN-vFUNKC18kM2krAb-ySYLDNWCUd6wats9Wn568oYh28LWVRp5pNzoNoec0JOD8CMcqVWIo3OeHUzMY626mNjJC-NIVyUyngIlFegcf1JSBo9BikJj9eWQQ0mq5vfkNqXtIikFg69uZci0HlECH68ydYDBj3sS3BBIwpzln-Ak', start_index=16276)
Annotation(end_index=17226, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgawDDl456z6fBdWRBs5C9OlnKpMujtxFYVbvyhQfkYOi6lQJHf1h4KTE5PMwBpAs9zA2bO6X6REmjlO6G5ZmCUFCIbQuN3JYAtYvPdisosuK5YrCiOtbAW7ikJpoGLp1ChcSRvj7Q', start_index=17217)
Annotation(end_index=17248, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlN39niJcAS998XbdVu2Eqh4pr01E1eGvziWR1qJ5DUARi-pmkwCp2lUT4J1wjzEQoIabcf1PKLRWP_QSVsox5tNhGrZiXLDzCDdmjTfHrY7cZQCTa9zoBAk_ioG6LXf5N7GaybJEu', start_index=17238)
Annotation(end_index=17270, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYK3aH3cerj5TA-_tZRJB1tUIYDLZVbUv3l4wix_SYQgNzMElWFR5gK6v1gJxACSqjSOSKj6r62P-s93xTNzEtfPgafiDo6mMw1CunjfarV13F-clNhQgscMBkbGHiQAh2_JtZti7z', start_index=17260)
Annotation(end_index=17292, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFldB6OjQ2keDwzmNxCbuz--vv37yZ8jlaANY8CMXeR1BXldeKzFzhOq5xpXAGpwiJp7oXHB3OBm8hKXmMvWAF7xEOoQkxhCyY38gcbRUB-iUhTV8FUnrzKYFpH-Y9NN9VLuvBGo_rWAQ==', start_index=17282)
Annotation(end_index=17315, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNuBJjQU-HggOiQdcpUk31YQWtQrVl1QuNhBHo-KZu7ZcHMpSiK9-zcXSsafLd1yfoF1Iu0NYJpn8OGI37ChUVuD4Fe2s8cYh50iwnjV0HhhK088QTo_x3RQoBYVFnwA==', start_index=17305)
Annotation(end_index=17359, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXtrA67AlHDPCqSvbSwAvwLGyqQigJy9xAqNE4KW00sB5VRUznOxGCmYkeR9P_rXx4O8WKpgrrhtynCvhZxqooyak3UswJBfLdchv8ouB9g77WtwP185fMd-uSbNOQxwJcVieI4p_p', start_index=17350)
Annotation(end_index=17380, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0y5nBRmoU_lT7vEv1aruiZVpsTkxCruEwgOwxbfjl68mC4QBe3KT9fJX2CuYk3tcsCU2ayW9a3PlTZOYQYUIHtfoP9lkGRMEa-zJEGRFHsGk4EaYakttT7Lo5T-oPJq_Bkg8yebLvBfaNcxC9Wx4FyCkvszP8M9_DXAL8QKc1h2o4RvMLx6wpajOrSyRA4uQBPDkWT_8FT6n5RbQz6ZyX_g==', start_index=17371)
Annotation(end_index=17430, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTXN15wvY1uyfogqsIoZO5YVAs-1xUmoKb7kmsTk-16tJ1903EP29fgNfO6TwjblueuV85JvEH-BfDETXt8JzUrn3BRNWavn5HJ2TSPufvWjcQ8co8zyB17gPcKZWOXyQ4tC6hWAyxWg==', start_index=17420)
Annotation(end_index=17453, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlZteviB67iKCS0L29-B8CDW3aT3Vf3X_YsmFd3yA_4c6HE1IzJFXIASOpeRbMamq0dqF2dE5-kIE563vuqVR_b-2RQh2b5IdFWv3pkCB1-X94GbBamTq-XvEaPfS7jw==', start_index=17443)
Annotation(end_index=17497, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHwOXYP0HWsKGb7Udoc5TQn8KZtvC2u7VeCJx7vIdvenTcNHvOjZ7WthJuK_rZrsW7gIHRKMhGrGmZn74pjqGqS7u1tTmGCkSy-OieoSg9oJdsMobYFpkORbr2jS6mOd47Mh56Xa-O', start_index=17487)
Annotation(end_index=17518, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRSGsd1SpuGSh3j6YsDAFpWbLrcigECNttxEa4F-in_O4Dp5QKofWJ5VjV6ap2eSlu_9L4TEYwnsU5BB-58MsBwHDxfLOfvUXXvU7HLbhcAlunAqtGIn9O_MVQV1sinSD8R42488FOXrreMDDVDyCqOBYabtuZiKmo8r951mjZJQGG_JP0pwz7WOzyynFOBfvA5_EBMNQ6hnj2NGzl1jr_ClWuFDEpwAW-Nvk=', start_index=17509)
Annotation(end_index=17638, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgAjKo5Lj3xxIiT8sieLb-epybmVcRodF1tu8ApDcL0IiHo9q6rH20p8reMB3aRmNZ-2Flsr96nisCbCvKV1RFjRZbHK0ItF7vbHpx9YKTRNN1rwkvTknJ0IezB3GqdkTaSQBOS1vswg==', start_index=17629)
Annotation(end_index=17660, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbbErfgOThSi_oQJXz4CbXCcOSyOw50c_LHoKUqIiEzZtyfmgCqGB82MzCmhQqLQZTtVcE3ukTndkwc94LKEgYJ15sJrLt35lfX6aqYjua8r-proxxf1opdswwMeOJnvNHDqKslb2t', start_index=17651)
Annotation(end_index=17682, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1nWDih7Srpe8A64T4yMTS1ZSBvqtq4_s0nKbtVu2dEf-EsrIbMT8VXJ4m4zWBzwroe6PYS9Thu1vOuyA6KnhAYoP-3Mz7tIdVB9-MOudT9wRaXaTUX8SHLcs4Yd-vnHGWhKGhTjK9a4CCpnMvjk28Qnurcxw84JZdr2q-efzUdSakO_6WpvDgJ8NJOFDnnEjUk1-Lf6ZR3tj3urgHXuT244E4ZDPKBPMlxmb-lUg=', start_index=17672)
Annotation(end_index=17802, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHt4XOQBC-CfZmv4cp5RmnpXDYgrp_B4IBDr013BFE3FWrnytsrgVSgL9DRGSINTzu-0uABC9FXQKL-La6DwoxEHlUTWXPh_9nGdPJKmUaqtmUpuyWlztyLmzG8VFNJSRbVHEG_cZtlRqHUnN40hkCmIq30jqq4cBhpfr8ZaLJVTCggSpyhLg==', start_index=17792)
Annotation(end_index=17886, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxfQNNjM5pw-ETTPuyXYhrBf9-xGCLFvw_SNGoLL9vR-62rTcJECtTuhnd4IU-RUroyyJd9Mhq8Xd-9UPnyDO2igdbSzCZwrZ22HdxEqoFJZptA2UuS86LjZ9MABfeUkZ0aX3IJ99S9hjk0qleBuAOvbWWkOE8Q1lgKUMpAuDKqYA3A-zZssIPEn_43ZstZyAzH920xeH3Xoo=', start_index=17876)
Annotation(end_index=17985, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgBr3-CZgpkwe6YE8fl0XZw_a9ymKDux7BpZBue356gsBunAoqxL442xfUd0poQIOy1DveHyAT5hBS1QsFnc0Iqzv3tKRTRXC-XuKTOkeeU8lvGrJhL9GIxkhSATO8j_NQL-7le4g=', start_index=17975)
Annotation(end_index=18033, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0Klk6lndZPdZnMYhCn0xGtpUbam8_wjbWYXvEYt0CyWCHJkrjdmZuOgJUUOKG3a5LNy6gtcgp9Nj6fq6cQesRoBjzbbl1SObEGxLHb5s0ekzPQcKNRgeYcaaKg2VwOBBYVoXfPCku', start_index=18023)
Annotation(end_index=18055, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHp6ihngxoWLuc1CCruFAzZbfi-XQbWIdFlD3MfwglWhRhubPDrZB3dAPJmOv2y_QdiyUGAsRZR6HPlZ0SqsMqnCwbCFVOFrnu5d8-ZV5YU0e9PmHXUcm8CVnNHnfiaMQ==', start_index=18045)
Annotation(end_index=18100, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCsgh7vQirlRHLBDKHHZeo8VYk5L-5ltOgwBdNMVqGfaOv1GT1J6QHUk-9vtvOfUWNW5iwQ0K5jSS-DWC5HB1uq-5W-u8D3Khi6Kpe-0ZQya4P8EpHb5JB0pESR6_0L8MzHxEm5UySKQ==', start_index=18090)
Annotation(end_index=18123, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLP2UOP1TWaAZaktSFcQnu-fQ-32RY_ukelmqoKNd47CuWDLTiqqYE-y11NOeGNBkjX8NrxlzUE-aQ0aJc_NHI1xONDuwgC56qH8oewQFTaUth-v8XtFRoNWsfhRNuG27pTHCgqtxWCZfrNxXKvrNKbQp7KHkdGn27l7IC6vyYSaNNAj5VF6AwrLD5r4-m0jTAH__bLDsaZtm97-ej_Q==', start_index=18113)
Annotation(end_index=18231, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzJZxdDaOKRzehQDqSFpYmAHiBKQA_-Xmai2LD7p0vxbZJPrbZsgZnBiwggdqjlv3HjdQfRuvvxHsLfcXwTc4z5GeQlSWwBbYqyuXTG20XyaEmZGImLDJSw_OoFuu4sdrWIu_EgXkk', start_index=18221)
Annotation(end_index=18252, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHODmmhu2IhVQDPWQKpd5mhW2yAZjU9AJiKPw1vtS1HSDy0qnDi4kX0_Hxx_N8gzKopZgerFi5NgjL22EWlUDbMhr9GO5-FONQUe_ZByCAkwBy5ijiyZ4DTEC8qvuHxlg==', start_index=18243)
Annotation(end_index=18293, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPslDIQEmPX6JbYY0gsD0lR-rnEPhqCur_2-z-LyM1J2mEEazEhC-JObqgwL42MpKmI-Ga3wQirlf45Y8imf_4-Fj1xd3F2oqB7gz66Kqxd2_buwD2-5VOBvTG-gFHn4xxU2xqcj1yaQ==', start_index=18283)
Annotation(end_index=18316, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE07i0SzhcV60hMgAJsW52b_Onf1omuW5mRWbd4desUndkBB8zy6CI1fxHo07dP1VjoINi8nHl1pZ_HNNL_KXriAgTW9ck7fJNze2nvEkJNM8uyjhLXmoCqEzfES4RQ7KAkvdV2mPwyvs3_HXSyOiqHcJKBsSOKXql1uP6CDGLE8pKpGO4Fd23yqMxzwYIX', start_index=18306)
Annotation(end_index=18407, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZ45ik4L03jUsCr3294JJx8hGasao82LyiuVnGAPR1P3uyFIPl7sMNUyPRINhk1fV21PSF8OTHG7LOZKjtot8LYDJPbT6rO4vYqS233BDm_bK1UH6uEbtGt27nQfWN_AyHS14KfS4h3IoJe0mhQ6wMOSOw_Gd8xv8F5r7YWT0D_AI551I5i9NXArmHk3Rn6m-yROxo_wWTukPzrMmivA==', start_index=18398)
Annotation(end_index=18514, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXtrA67AlHDPCqSvbSwAvwLGyqQigJy9xAqNE4KW00sB5VRUznOxGCmYkeR9P_rXx4O8WKpgrrhtynCvhZxqooyak3UswJBfLdchv8ouB9g77WtwP185fMd-uSbNOQxwJcVieI4p_p', start_index=18505)
Annotation(end_index=18535, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRSGsd1SpuGSh3j6YsDAFpWbLrcigECNttxEa4F-in_O4Dp5QKofWJ5VjV6ap2eSlu_9L4TEYwnsU5BB-58MsBwHDxfLOfvUXXvU7HLbhcAlunAqtGIn9O_MVQV1sinSD8R42488FOXrreMDDVDyCqOBYabtuZiKmo8r951mjZJQGG_JP0pwz7WOzyynFOBfvA5_EBMNQ6hnj2NGzl1jr_ClWuFDEpwAW-Nvk=', start_index=18526)
Annotation(end_index=18656, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnLbi-UBMfE8BH_KYxYBDZGTtH4tW_mCoC4bxtpgNAea0AniLc-ffo3PeMB8lZLVz3qv4zHXOf5hvpmHZshE_bAHm_4u_Jwv2UJ0MMxEZoUWb-D30mISRQ4wcbbLGeErtdFuL2aG_xhpa6OsDM0tdICe4FkNYTAR_xvGgUJy84epF1aCQuzE3TlWMScxKFoGd0_lSUNnPZLjsZ_g==', start_index=18646)
Annotation(end_index=18757, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMJkBeOjuxtDzuevM4UTQCr-86-Ln59HRPqeZBnqaRuPI5rK6qXM-XnRsmvJR2fIH__Hy9xs0xRGOhHZHO61LXzHq5OkVmeKKVbEksO2zwHyx8WJFJUWc4eXS1ndhLYFml-YoUN2h3', start_index=18747)
Annotation(end_index=18779, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCJ-Ndf9Mhf9SXBJy4aoBkn_xgKQSAnu_vF3cQD6rsboi_5VbYsrLEq8fGvCfbDAu7HGpzPDfGlziR9FpTGS_k3sm4sMoTL-dnxZr-sab7VvIYkAqvE-YqABsHxfTUhosDpSvKrWBrVj7bT9YaAX9mLf4cx3nYnt9md_V_dFAZum5xm7usKzPMkkBZk3d1pWo9S71NJzqoRwI=', start_index=18769)
Annotation(end_index=18878, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTufz6mR_MTnVKXyFBvmPIh2x4cxAkbGUdDH0UWmGcLOTWB49cnTDujWJjA6ijKkzle2RS_JPYDuIEjmATnwKLFRu4d9NKrIxpq2yvMNft6ddUDuaIVywB8j_4ktGTPe-sADfIPAsh', start_index=18868)
Annotation(end_index=18900, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJqf1kyyEREWTUqdhrBXAXPX_KgABF_-WJlqZhacyvT3t3VzuaM9pJBpXJgs42K3hAGlZBAqOGzn3-EDPCC12wRHfXPl_YtgmmCc0HylcjQ5SikU2SvwUv3tD4TIT20Oi400_Jkd0AhdqXSHtykJYUuFbu4Y6h0B9421_5k0aHcYckzFrfhiUQxr79xjeRzhQ=', start_index=18890)
Annotation(end_index=18994, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgawDDl456z6fBdWRBs5C9OlnKpMujtxFYVbvyhQfkYOi6lQJHf1h4KTE5PMwBpAs9zA2bO6X6REmjlO6G5ZmCUFCIbQuN3JYAtYvPdisosuK5YrCiOtbAW7ikJpoGLp1ChcSRvj7Q', start_index=18985)
Annotation(end_index=19016, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZyEMTX1WxhHlhuYYE-AV4QnJSaQrgh7swH5iD0jgxqyu9JvZO8we2rEZHX0AD6dX_BGWwCTSIiOIfwBb6WKKCDKIlQ_RADEUDjbeaF8zLWtrjTG6TrkTdLQWQ7F6IMUd12FJikrItveWfbw==', start_index=19006)
Annotation(end_index=19073, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHt4XOQBC-CfZmv4cp5RmnpXDYgrp_B4IBDr013BFE3FWrnytsrgVSgL9DRGSINTzu-0uABC9FXQKL-La6DwoxEHlUTWXPh_9nGdPJKmUaqtmUpuyWlztyLmzG8VFNJSRbVHEG_cZtlRqHUnN40hkCmIq30jqq4cBhpfr8ZaLJVTCggSpyhLg==', start_index=19063)
Annotation(end_index=19156, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbbErfgOThSi_oQJXz4CbXCcOSyOw50c_LHoKUqIiEzZtyfmgCqGB82MzCmhQqLQZTtVcE3ukTndkwc94LKEgYJ15sJrLt35lfX6aqYjua8r-proxxf1opdswwMeOJnvNHDqKslb2t', start_index=19147)
Annotation(end_index=19177, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXtrA67AlHDPCqSvbSwAvwLGyqQigJy9xAqNE4KW00sB5VRUznOxGCmYkeR9P_rXx4O8WKpgrrhtynCvhZxqooyak3UswJBfLdchv8ouB9g77WtwP185fMd-uSbNOQxwJcVieI4p_p', start_index=19168)
Annotation(end_index=19199, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGC3O8DCc5v3CV_a4TLRLvrfLSV35egeVUcjDc-kNN-vFUNKC18kM2krAb-ySYLDNWCUd6wats9Wn568oYh28LWVRp5pNzoNoec0JOD8CMcqVWIo3OeHUzMY626mNjJC-NIVyUyngIlFegcf1JSBo9BikJj9eWQQ0mq5vfkNqXtIikFg69uZci0HlECH68ydYDBj3sS3BBIwpzln-Ak', start_index=19189)
Annotation(end_index=19302, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2i64is9pHLfNyplAUcT2Z9fZNlTamyMpIKmrAoHTIt2xLVFOjBLiuOWNZwPkKCw4kUw6Gb1enQbADeImTOyBKFjJ8h2eLx6DPeCXwvH6zVNI6_2uftSiYJ81vPJDoRo4v8ZRDt28TdA==', start_index=19292)
Annotation(end_index=19325, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfEVfVSWJiABHSLvkBTPFXjckvVh2kJeSacghNehMCnJMpG8mPMNhRXIQyhUWMl9Q8zC_If-sDxqv1orWQIEC_xdV0g0OVUP9oBvUR7TpFlu2Hw8LxBSgrGMbNTiMGvid27w2F9lkaCMqGQiCB', start_index=19315)
Annotation(end_index=19380, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMJkBeOjuxtDzuevM4UTQCr-86-Ln59HRPqeZBnqaRuPI5rK6qXM-XnRsmvJR2fIH__Hy9xs0xRGOhHZHO61LXzHq5OkVmeKKVbEksO2zwHyx8WJFJUWc4eXS1ndhLYFml-YoUN2h3', start_index=19370)
Annotation(end_index=19402, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMIeKazBW-lyElNIte-V2wkrfF-hBB-Oi8-DQABTwGxnrXaF3qgO2qcNCcTl0AQDFJK0hzvGKsoTcDx9pEI0E9aLbL5uykQHL9QNgrRZwpct83yw-5fy9vuujvEMTmD374YX3ECOK-IUoRJ878xQ6dFZ7T7SGCOSWVlUqDbpK_RtgnFKO2u5AVdhoAsTYBVJp0pRsc3yGwLmM=', start_index=19392)
Annotation(end_index=19505, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGm3Uy7VQpnX4WreXqpVq_6cgXCumC8SiR8E59m7gG97u3M0URuN5mQEOyDSagQhvpgU7g3MhBbishslIVJLN0glp8lWJnzxOUauHx57mKQHL-D3LmqWNOvUTdcRxv4GfqNHb9h3eDhSg==', start_index=19495)
Annotation(end_index=19528, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkwx8uUetiN7EkJZdyiarqqrX2QvgBqDLkgCsp_st8phATIOysRzHbXGYjHa2cp0_lHBGp4fN273fLcgJUxkrFh51zEdJ7jXTpFdUmGlOflwZzmIjjt49-xbX5kqzvTk5z0miyI-fk6MtA4kP-yxWAo2LLUQyUWjQplbuk_yvPMXS5-E1XwiOckVymU48mZpVadlfRKDcw6F3nIhJnEjy5rsSBEbO2HYpv0I6opifvZ0USK2mDWIcbymzgCgN9tm5CKRKJh-9JRmkiSZZxWcToGhShlL0kWc9LGiQUhQAFpAUE-FCuKOoXGYhsO-F-SUaGVXag8oA=', start_index=19518)
Annotation(end_index=19719, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHv1Bmc-H2qtlDzjSUGmMpujfX5MmqIRKVb7FGj6IhtFiBPPEhKFqwWEzjHw1H7BzWCo6SZGulvRuCTewS3MTfobWU058cN8O3MZMYFoCPVq8xGb4xAcCrXECdSzoWYXg==', start_index=19709)
Annotation(end_index=19764, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFM-dBIOKbYffv5EL5dHNZTb-tzX4SCxaOWfBBYEVbXPeTUEp8P_rjisHIPIMmGWdKywa1H0nLjJWaoyzn7i1do5_hOp9E21oacHkiOYOfy-1IvuagHNN2AzRT43ZX6GbZjkA==', start_index=19754)
Annotation(end_index=19812, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-XeivKqHOpHtSN_x5lr8Xt3ivx6_4iAXpo_WYJqBe3PzaLfAEOuQ8zAfxJLgFPe6UrLH6lxlXgm1JnFCfZBRHzdKUq7zmd3CJWerzNn9_b1PcmQJXOnc0l0UwUpULyk_IIcgjx60T', start_index=19802)
Annotation(end_index=19834, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFldB6OjQ2keDwzmNxCbuz--vv37yZ8jlaANY8CMXeR1BXldeKzFzhOq5xpXAGpwiJp7oXHB3OBm8hKXmMvWAF7xEOoQkxhCyY38gcbRUB-iUhTV8FUnrzKYFpH-Y9NN9VLuvBGo_rWAQ==', start_index=19824)
Annotation(end_index=19857, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkHshAwQBIQb0F6oUyUJ_Ls4tZoVPsn4I7wtzgzd9fxZqY8nNVjh8lWOmFeKrDPsjmegHZ7E4MKoIED5wi_BsjLuqjmDzM-Z0Vw_w-6QvwsHb2587GUsoaKhGzk0DEBdcEc8KV97VQ4UikF7RbAdzT6Pq4kAYw3h28mCOKhoFRGsGCgXzB0iYrilHedD_JfEvVdyQfGwCx-6TtXmy6d4mvwJLxpt3F7y08vEdnGO3bwYAhbTkXtWcppmopdPspKg==', start_index=19847)
Annotation(end_index=19992, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqpLmUGST42bJNPuJim-zP0EozmltYFA2mXaHxDhVGKSagVMO1ptHY7Ps-i_-JqyKJMAMNmx7BoxeaiU9vTf_HzMLoc-PhR28aYsybs0IqTx0yf2ad81tSYRdrb3-gAGtC5MxsjVvNGIfSWGIYX4dz7XHMB7UOHA==', start_index=19983)
Annotation(end_index=20060, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXtrA67AlHDPCqSvbSwAvwLGyqQigJy9xAqNE4KW00sB5VRUznOxGCmYkeR9P_rXx4O8WKpgrrhtynCvhZxqooyak3UswJBfLdchv8ouB9g77WtwP185fMd-uSbNOQxwJcVieI4p_p', start_index=20051)
Annotation(end_index=20081, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0y5nBRmoU_lT7vEv1aruiZVpsTkxCruEwgOwxbfjl68mC4QBe3KT9fJX2CuYk3tcsCU2ayW9a3PlTZOYQYUIHtfoP9lkGRMEa-zJEGRFHsGk4EaYakttT7Lo5T-oPJq_Bkg8yebLvBfaNcxC9Wx4FyCkvszP8M9_DXAL8QKc1h2o4RvMLx6wpajOrSyRA4uQBPDkWT_8FT6n5RbQz6ZyX_g==', start_index=20072)
Annotation(end_index=20187, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXtrA67AlHDPCqSvbSwAvwLGyqQigJy9xAqNE4KW00sB5VRUznOxGCmYkeR9P_rXx4O8WKpgrrhtynCvhZxqooyak3UswJBfLdchv8ouB9g77WtwP185fMd-uSbNOQxwJcVieI4p_p', start_index=20178)
Annotation(end_index=20209, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkHshAwQBIQb0F6oUyUJ_Ls4tZoVPsn4I7wtzgzd9fxZqY8nNVjh8lWOmFeKrDPsjmegHZ7E4MKoIED5wi_BsjLuqjmDzM-Z0Vw_w-6QvwsHb2587GUsoaKhGzk0DEBdcEc8KV97VQ4UikF7RbAdzT6Pq4kAYw3h28mCOKhoFRGsGCgXzB0iYrilHedD_JfEvVdyQfGwCx-6TtXmy6d4mvwJLxpt3F7y08vEdnGO3bwYAhbTkXtWcppmopdPspKg==', start_index=20199)
Annotation(end_index=20344, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqpLmUGST42bJNPuJim-zP0EozmltYFA2mXaHxDhVGKSagVMO1ptHY7Ps-i_-JqyKJMAMNmx7BoxeaiU9vTf_HzMLoc-PhR28aYsybs0IqTx0yf2ad81tSYRdrb3-gAGtC5MxsjVvNGIfSWGIYX4dz7XHMB7UOHA==', start_index=20335)

## Sources
