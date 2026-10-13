# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 44ade72a | **Time:** 462.35s | **Cost:** $2.03747
--------------------------------------------------------------------------------

# The Hemodynamic Balancing Act: Shock Index in Emergency Triage

**Key Points**
*   **The Shock Index (SI)**, calculated as heart rate divided by systolic blood pressure (HR/SBP), is a sensitive bedside tool for detecting **occult shock**—a state of tissue hypoperfusion present despite normal blood pressure.
*   **Early Recognition:** SI values > 0.9 are strongly associated with increased mortality, hyperlactatemia, and the need for massive transfusion or ICU admission, often outperforming traditional vital signs in identifying patients in the compensatory phase of shock.
*   **Risk of Over-Intervention:** While highly sensitive, the SI lacks specificity at lower thresholds (0.7–0.9), potentially leading to **overtriage**. This can result in resource exhaustion during mass casualty incidents or unnecessary fluid loading in septic patients, risking fluid overload.
*   **Confounding Factors:** The utility of SI is significantly blunted in **geriatric populations** and patients on **beta-blockers**, where physiological responses to shock are masked, leading to dangerous false negatives (undertriage) rather than over-intervention.
*   **Balancing Strategy:** To balance sensitivity and specificity, clinicians increasingly utilize **dynamic trending (Delta SI)** rather than static measurements, and employ tiered thresholds: using lower values (>0.7) for screening and higher values (>1.0) for triggering aggressive interventions like massive transfusion protocols.

### Introduction
In the high-stakes environment of emergency triage, the rapid identification of hemodynamic instability is paramount. Traditional vital signs, specifically heart rate (HR) and systolic blood pressure (SBP), are often looked at in isolation, yet they can be deceptively normal during the compensatory phase of shock. The **Shock Index (SI)**, defined as the ratio of heart rate to systolic blood pressure (SI = HR / SBP), integrates these two parameters to provide a more sensitive measure of hemodynamic status [cite: 1, 2]. By identifying patients with "occult shock"—those who are maintaining blood pressure through compensatory tachycardia—the SI aims to facilitate early intervention before irreversible organ failure occurs.

However, the clinical application of the Shock Index involves a critical trade-off. A lower threshold for intervention maximizes early recognition (sensitivity) but risks **over-intervention** (low specificity), leading to the potential waste of scarce resources such as blood products and trauma team activations, or clinical harm through fluid overload [cite: 3, 4]. Conversely, setting a higher threshold increases specificity but risks missing patients in the early stages of deterioration. This report examines how the Shock Index balances the imperative of early shock recognition against the risks of over-intervention, analyzing its application across trauma, sepsis, and mass casualty scenarios while accounting for confounding variables like age and medication.

---

## The Physiological Basis of the Shock Index
The utility of the Shock Index is rooted in the pathophysiology of the compensatory phase of shock. When circulatory volume decreases (as in hemorrhage) or vasodilation occurs (as in sepsis), the autonomic nervous system responds to maintain cardiac output and perfusion pressure.

### The Compensatory Mechanism
In early shock (Class I and II hemorrhage), catecholamine release increases the heart rate (tachycardia) and systemic vascular resistance. This compensatory mechanism often maintains the systolic blood pressure within a "normal" range (>90 mmHg) despite significant hypoperfusion [cite: 2, 5]. Consequently, a patient may present with a HR of 100 bpm and an SBP of 100 mmHg. Viewed individually, neither value may trigger an alarm; however, the resulting SI of 1.0 significantly exceeds the normal range of 0.5–0.7, signaling hemodynamic instability [cite: 1, 6].

### Normal vs. Abnormal Ranges
*   **Normal Range:** 0.5 to 0.7 [cite: 1, 2].
*   **Gray Zone:** 0.7 to 0.9. This range suggests early physiological stress or "impending badness" but lacks high specificity [cite: 1, 7].
*   **Abnormal (Shock):** > 0.9. Values above this threshold are widely accepted as indicative of shock and are associated with increased mortality and therapy requirements [cite: 1, 8].
*   **Critical:** > 1.0 to 1.3. These values are strongly correlated with severe outcomes, including the need for massive transfusion and high mortality rates [cite: 1, 5].

---

## Early Recognition: The Case for Sensitivity
The primary argument for using the Shock Index in triage is its superior sensitivity compared to traditional vital signs for detecting occult hypoperfusion.

### Detecting Occult Shock in Trauma
In trauma triage, the "normotensive" patient presents a diagnostic challenge. Reliance on hypotension (SBP < 90 mmHg) as a trigger for trauma team activation often results in delayed care because hypotension is a late sign of decompensation, typically appearing only after 30–40% of blood volume is lost [cite: 5, 9].

Research indicates that an SI > 0.9 is a more reliable predictor of severe injury and transfusion needs than hypotension alone.
*   **Predicting Hemorrhage:** In a study of normotensive trauma patients, an admission SI > 0.7 was associated with a progressively increased risk of requiring transfusion. Specifically, compared to an SI < 0.7, an SI > 0.9 showed significantly higher odds ratios for transfusion, effectively identifying compensated shock that SBP alone missed [cite: 10].
*   **Mortality and Morbidity:** An SI ≥ 1.0 has been associated with a 57% higher odds of significant injury and a 64% higher odds of needing emergent operation compared to hypotension, which failed to predict these outcomes in some cohorts [cite: 9, 11].
*   **Massive Transfusion:** An SI > 0.9 is frequently cited as a specific predictor for massive transfusion protocols (MTP). One study found that patients with an SI > 0.9 were at high risk for exsanguinating hemorrhage, suggesting that SI can serve as an early trigger for blood product preparation before frank hypotension develops [cite: 8, 12].

### Predicting Hyperlactatemia in Sepsis
In sepsis, "occult shock" manifests as tissue hypoperfusion (hyperlactatemia) in the absence of hypotension. Early Goal-Directed Therapy (EGDT) relies on recognizing this state early.
*   **Surrogate for Lactate:** The SI correlates strongly with serum lactate levels. A retrospective analysis found that an SI ≥ 0.7 was the most sensitive screening test for hyperlactatemia (lactate ≥ 4.0 mmol/L) and 28-day mortality, with a negative predictive value (NPV) of 95% [cite: 6, 13].
*   **Triage Utility:** For patients presenting with vague symptoms (e.g., "weakness"), an elevated SI can alert clinicians to screen for sepsis and initiate lactate measurement, potentially reducing time to antibiotic administration [cite: 6, 14].

---

## The Risk of Over-Intervention: The Specificity Trade-off
While high sensitivity ensures fewer missed cases, it inevitably leads to a higher rate of false positives. In emergency triage, this "overtriage" has tangible costs and clinical risks.

### Overtriage in Trauma Systems
Overtriage occurs when patients who do not require high-level trauma care are assigned to it, diluting resources.
*   **False Positives:** An SI between 0.7 and 0.9 is often considered a "gray zone." Factors such as pain, anxiety, and sympathomimetic drug use can elevate heart rate without underlying hemorrhage, leading to an elevated SI in a stable patient [cite: 1, 2].
*   **Resource Utilization:** Activating a full trauma team or a massive transfusion protocol based solely on an SI > 0.9 can lead to unnecessary mobilization of surgeons, anesthesiologists, and blood bank resources. A study on the "Reverse Shock Index" (rSI) noted that adding hemodynamic criteria to trauma team activation could result in overtriage, increasing hospital length of stay and costs without necessarily improving outcomes for the "false positive" group [cite: 3].
*   **Mass Casualty Incidents (MCI):** In MCI settings, where resources are strictly limited, specificity becomes more critical than sensitivity. A study using the Alberta Trauma Registry found that while an SI threshold of 0.72 maximized sensitivity (0.53), it had poor specificity. Conversely, a threshold of 1.00 had high specificity (0.92) but a dismal sensitivity (0.19) for identifying "Priority 1" patients [cite: 15]. This suggests that strictly applying SI in mass casualty triage could lead to either overwhelming the system (low threshold) or missing salvageable patients (high threshold).

### Risks of Fluid Overload in Sepsis
In sepsis management, the risk of over-intervention manifests as **fluid overload**.
*   **Fluid Responsiveness vs. Tolerance:** An elevated SI is often used as a trigger for fluid resuscitation. However, research indicates that a higher SI is associated with a *lower* likelihood of fluid responsiveness. One study showed that for every point increase in SI, the odds of responding to fluid therapy decreased significantly [cite: 4].
*   **Iatrogenic Harm:** Aggressive fluid resuscitation driven by an elevated SI in a non-fluid-responsive patient can lead to pulmonary edema, respiratory failure, and increased mortality. Approximately 67% of septic patients treated with early goal-directed therapy developed evidence of fluid overload, which was associated with increased hospital mortality [cite: 16]. Therefore, using SI as a standalone trigger for fluids without assessing fluid responsiveness can be dangerous.

---

## Confounding Factors: The "Silent" Risks
The balance between recognition and over-intervention is further complicated by patient-specific factors that alter the physiological relationship between HR and SBP.

### The Geriatric Population
Elderly patients present a unique challenge where the SI often *underestimates* shock (undertriage) rather than leading to over-intervention.
*   **Blunted Tachycardia:** Aging results in a reduced beta-adrenergic response, meaning elderly patients may not mount a significant tachycardia in response to shock. Furthermore, the prevalence of **beta-blocker** and **calcium channel blocker** use prevents the HR from rising, artificially lowering the SI [cite: 17, 18].
*   **Baseline Hypertension:** Many elderly patients have baseline hypertension. A "normal" SBP of 120 mmHg in a patient who normally runs 160 mmHg represents relative hypotension. However, the math of the SI (e.g., HR 80 / SBP 120 = 0.66) would categorize this patient as stable [cite: 2].
*   **Mortality Risk:** Despite these limitations, an SI > 1.0 in the elderly is an ominous sign, associated with significantly higher mortality than in younger cohorts. However, the absence of an elevated SI does not rule out shock in this group [cite: 17, 19].

### Pediatric Considerations
Children have higher baseline heart rates and lower baseline blood pressures, making standard adult SI thresholds (0.5–0.7) inapplicable. The **Pediatric Age-Adjusted Shock Index (SIPA)** has been developed to address this, using age-specific cutoffs. Using unadjusted adult SI values in children would lead to massive overtriage (false positives) due to normal pediatric physiology [cite: 2].

---

## Strategies to Balance the Scale
To optimize the trade-off between early recognition and the risk of over-intervention, modern triage protocols employ tiered thresholds, dynamic monitoring, and integration with other clinical tools.

### 1. Tiered Thresholds
Clinicians use different SI cutoffs for different decisions:
*   **Screening (SI > 0.7):** Used for "ruling out" pathology. A normal SI (< 0.7) has a high Negative Predictive Value (95%) for hyperlactatemia, allowing clinicians to deprioritize these patients safely [cite: 6, 13].
*   **Monitoring (SI 0.7 – 0.9):** The "Gray Zone." These patients do not trigger immediate massive intervention but are flagged for closer monitoring, repeat vitals, and adjunct testing (e.g., lactate, FAST exam) [cite: 1].
*   **Intervention (SI > 1.0):** Used as a "rule in" for shock. This threshold has high specificity and is used to trigger resource-intensive protocols like Massive Transfusion or Trauma Team Activation [cite: 5, 6].

### 2. Dynamic Trending (Delta SI)
A single SI measurement is a static snapshot. The **Delta SI** (change in SI over time) balances the risk of over-intervention by filtering out transient elevations caused by pain or anxiety.
*   **Resuscitation Response:** If an elevated SI normalizes after initial treatment (e.g., pain control or a small fluid bolus), the patient may not require aggressive intervention. Conversely, a persistently elevated SI despite intervention is a strong predictor of mortality and the need for hemostasis [cite: 2, 20].
*   **Prehospital to Admission:** An SI that rises between the prehospital setting and ED arrival is a more ominous predictor of mortality than a stable elevated SI, warranting aggressive care [cite: 21].

### 3. Alternative Indices
*   **Modified Shock Index (MSI):** Calculated as HR / Mean Arterial Pressure (MAP). Since MAP includes diastolic pressure, MSI may better reflect vascular resistance and diastolic runoff. Some studies suggest MSI is a better predictor of mortality than SI, potentially reducing false positives [cite: 2, 22].
*   **Reverse Shock Index (rSI):** Calculated as SBP / HR. An rSI < 1.0 (equivalent to SI > 1.0) is used to simplify the math for clinicians (is the BP lower than the HR?). This is often used to trigger trauma team activation, accepting some overtriage to prevent missed injuries [cite: 3, 23].

### 4. Clinical Context Integration
To prevent over-intervention (e.g., fluid overload), the SI must be interpreted alongside other markers.
*   **Sepsis:** In sepsis, an elevated SI should trigger an assessment of *fluid responsiveness* (e.g., passive leg raise) rather than automatic fluid boluses, mitigating the risk of overload [cite: 4].
*   **Trauma:** In trauma, SI is combined with anatomical criteria (mechanism of injury) and point-of-care ultrasound (FAST) to confirm the need for surgery or blood products, reducing the reliance on SI alone [cite: 9].

### Conclusion
The Shock Index serves as a vital hemodynamic "smoke detector" in emergency triage. It balances early recognition against over-intervention primarily through its **sensitivity to occult shock**, allowing it to catch decompensating patients that traditional vital signs miss. However, this sensitivity comes at the cost of specificity, creating a risk of **overtriage** and **resource strain** if used in isolation.

The optimal balance is achieved not by relying on a single cutoff, but by using the SI as a **tiered screening tool**: using lower thresholds (>0.7) to identify at-risk patients for further investigation (lactate, imaging) and higher thresholds (>1.0) to trigger life-saving interventions (transfusion, surgery). Furthermore, recognizing the limitations in geriatric and medicated populations is essential to prevent dangerous undertriage. Ultimately, the Shock Index is most effective when used dynamically—trending changes over time—and integrated into a holistic clinical assessment rather than as a rigid trigger for intervention.

## References
[cite: 1] WhiteBoardMedicine. (2025). Shock Index emergency triage early recognition vs over-intervention.
[cite: 6] Berger, T., et al. (2013). Shock index and early recognition of sepsis in the emergency department: pilot study. *Western Journal of Emergency Medicine*.
[cite: 2] Koch, E., et al. (2019). Shock index in the emergency department: utility and limitations. *Open Access Emergency Medicine*.
[cite: 3] Unnamed Study. (2016). Strengths and limitations of this study regarding Reverse Shock Index. *BMJ Open*.
[cite: 8] JEMS. (2023). Assessing Trauma: The Shock Index.
[cite: 15] Unnamed Study. (2025). The Use of the Shock Index to Classify Patients During Mass-Casualty Incident Triage.
[cite: 21] Unnamed Study. (2024). Shock Index overtriage risk over-intervention. *International Journal of Paramedicine*.
[cite: 3] Unnamed Study. (2016). Reverse shock index and trauma team activation. *BMJ Open*.
[cite: 17] Unnamed Study. (2015). Shock index limitations in elderly and beta blockers. *PubMed*.
[cite: 18] Unnamed Study. (2013). Effect of beta-blockers on shock index in urosepsis. *PMC*.
[cite: 24] Unnamed Study. (2014). Pre-injury beta-blocker use in geriatric trauma. *PMC*.
[cite: 25] Unnamed Study. (2025). Preinjury Beta Blockers are Associated With Increased Mortality in Geriatric Trauma Patients.
[cite: 9] Unnamed Study. (2021). Shock Index vs hypotension early recognition trade-offs. *PMC*.
[cite: 11] Unnamed Study. (2021). Shock Index vs hypotension early recognition trade-offs. *PubMed*.
[cite: 2] Koch, E., et al. (2019). Shock Index false positives causes emergency department. *PMC*.
[cite: 6] Berger, T., et al. (2013). Shock Index false positives causes emergency department. *PMC*.
[cite: 1] WhiteBoardMedicine. (2025). Shock Index false positives causes emergency department.
[cite: 4] Unnamed Study. (2020). Shock Index sepsis fluid overload risk. *PMC*.
[cite: 16] Unnamed Study. (2014). Fluid overload in sepsis and EGDT. *PMC*.
[cite: 22] Unnamed Study. (2019). Algorithm using shock index for triage decision making. *PubMed*.
[cite: 15] Unnamed Study. (2025). The Use of the Shock Index to Classify Patients During Mass-Casualty Incident Triage.
[cite: 26] Unnamed Study. (2025). Algorithm using shock index for triage decision making. *PMC*.
[cite: 6] Berger, T., et al. (2013). Shock Index 0.7 vs 0.9 intervention protocol. *PMC*.
[cite: 2] Koch, E., et al. (2019). Shock Index 0.7 vs 0.9 intervention protocol. *PMC*.
[cite: 5] Unnamed Study. (2024). Shock Index tiered protocol trauma sepsis. *MDPI*.
[cite: 1] WhiteBoardMedicine. (2025). Shock Index tiered protocol trauma sepsis.
[cite: 14] Berger, T., et al. (2013). Shock Index tiered protocol trauma sepsis. *ResearchGate*.
[cite: 20] Unnamed Study. (2019). Shock Index threshold 0.9 massive transfusion mortality. *PMC*.
[cite: 12] Unnamed Study. (2021). Shock Index threshold 0.9 massive transfusion mortality. *Revista Emergencias*.
[cite: 2] Koch, E., et al. (2019). Shock Index > 0.7 hyperlactatemia sensitivity specificity. *PMC*.
[cite: 13] Berger, T., et al. (2013). Shock Index early recognition occult shock vs risk of over-intervention. *PubMed*.
[cite: 10] Unnamed Study. (2024). Shock Index Identifies Compensated Shock in the 'Normotensive' Trauma Patient. *ResearchGate*.
[cite: 23] Unnamed Study. (2016). Shock Index trauma team activation overtriage risk. *PMC*.
[cite: 19] Unnamed Study. (2025). Is Shock Index a Valid Predictor of Mortality in Emergency Department Patients With Hypertension... *ResearchGate*.
[cite: 7] Unnamed Study. (2022). Shock Index 0.7 to 0.9 "gray zone". *Gavin Publishers*.
[cite: 15] Unnamed Study. (2025). The Use of the Shock Index to Classify Patients During Mass-Casualty Incident Triage. *ResearchGate*.
[cite: 26] Unnamed Study. (2025). Shock Index mass casualty incident triage sensitivity specificity. *PMC*.
[cite: 27] Unnamed Study. (2025). Shock Index mass casualty incident triage sensitivity specificity. *PubMed*.

**Sources:**
1. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTuoolj84OSH665wJmTpHJJi9bZl9SThB0H4MUZ2jRRwMuvtOoaoQVshhbZSi2e51cPWRFYopOHYbCPs3vKn45mEp03wxdCi8-PTKiZHZflkmtCBIh9zK_Sc8kpbtlwc8=)
2. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIK9NJlo_x3Fl9lQPbwCUjiKJmp_DyZyaLh6tzcegBP9Z7M8dd5o7WejWBmkWz2cApyKetnXi75ypYuMltZF2-3au7iJSK0HpLTwl8y5m4-DNVfLIxnCrsc96mRqPVh3KEffGvdxs=)
3. [bmj.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMPmvibiVFBYrSb6so4DDjnsh8jMEMBeQnbBvLbt1jqFUR-ioVxqIBwe02D1KnVtWnd_lXpx1iucT3kWGK_t7Qjm09YMJrJcqPWR7CP4syZc8smN8Zws6xZg7nxilgbDQ=)
4. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlMltPaUpt7XeaHWc_rg5Xds-ibs37k_LR41OPci2urykQGdttOBPvWjcy485M2bOmmwlvD_rdo7UhFMIxe0ha_6bEYX2OLd_dpEeWlWOXaocbZQ8khHXSjaz1x09yBgzXYEfMKXc=)
5. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGAwZY2WtUNSVDmOcZOVVN7lSQgqQIWexBqwstwXP-1deWJaid9wTS7eXjK4k53APhF_RbxxG9DJlG493rEEWgdg_cMju4szYvimLayYgCjSA0ej62cIbRGQ==)
6. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGi_kxcBJJfDsFIfYFYSLddtJRJsrQcCNlQ8hyw_Wn-q6wz1gn9szeQa3RWSY8XGWtYmrCpOQA4QMfr2kXF9KnEwEOw1QLArt_z7tVGvakPhCNpLi3F-QjhENMIfgcnAOZDctzPfHk=)
7. [gavinpublishers.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwCMRLmmkZtBwRc0U5g1XNbthzXHa30vsFFuem9WaIxuT_zV2TQTG3AIYBwRGYFN8Y_0rEl892wOlYKsuxyT80iXuMlH6Qtbjo9fS7ZrxQ_NkEvEfG-fEQf5RYkZiaGsU05J27ud_psRHq-3pT0YH02t9kEWHqu9XwEc1Sp_bQ_0QgSlTRpMelaqea7HrEdJH0mAsTc0zG0ULM-4bHuGSTvaQ4VKNOeAt2H7KWnNNRx0uCUA==)
8. [jems.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQT6M7anAqMG5jtHtbOuUBk4qMtrUAQPTZe_6RmUngd9PFTbiVbzem82wJNuV6j2kGt48K09pbW-_39tcUOLW2r-rbDw3M-gXSd5xHjrQ0TtoJn06ZFgSevZ02c6b1NmKDxAMnOed3BLbC_c8-2FiAIBS0T_qADZYqmWePNsx3hwDbn43O4uoA2gfuuzhp)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5AWjekRe7lVfg8N6OGrpcgitSq4DR4JlVBtmBBOUGnXQp-2H7G3d9ve0vBmCICZNMW47e_crF2gD0SCvoYYR-OdUrG00NVavlokkxkhHTDnOTH1YAjhY5OVQfZE-0IKYRuJhRzI4=)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCRaJW6s4qpLl8oQfFkgeEYcuvBxyCxY9KX7barec-ZbMhorrEhveeUzv0yI7Rz1Gc3UJ0M0zor3ojbk031V9b3lzr1T-w6IYplKBM6vR-x5NY4YvrnzjxqR9gN1UQkkq5qzMhdD-iRjXXNMpX3lJvVc1f0tqfDm-5K8orjf4jyoly_b-xz0b7fVM_Hd0pVsH7XwMXDV_YohCKh6P9wv1WkPMhl-yEinpXz3nnvQ_aCUGxO2Ba7A==)
11. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvfs7_yVN3PaB68y0N03dwmcsKnf2q-HfW1frvidqVJvLP-07S_r5UyN9HyRPb1w6m39LKudfqdA49Ne5LSqumIJ73bfZ4Gz5x3MPKrBM6TjlmM8wjpYxXxKW-t5rk)
12. [revistaemergencias.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFn4Js4lF3cQGEi_kNDaeWda5m2IOAuXpYGfEUmJfPv6XBN1N1vWu881XamPV7tJeaLQZM6Azp0h9JFQ5kL5-X80TX7lBHyEHVUYn0kC0ZH-o0mIITh8yGYBJcHgULgCjrQhW-XYfQ0_KpBr9clL4g3nsawAvGDNE36Mu7f_RPJ9Eb55p8BspgtLiD88uSQB8ZL4tqoAQ==)
13. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoAsqoLJGTPFijEEG5gO8z2_kUs34tOwWCMkgplIA9dRYlpA5ka4mLFKgFLqfKETvW-wExOd-jldJjKjPSvR4-SzJoVgycijq2mraZxG87hXba_gvvRmE8S7sUrMia)
14. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEE8wJ3AlTKK93wqtGj10gHyPhR0AJj2CA6WNJdsEBLTVcJu4z-0FQyux73RAdEx38Yzo2su5H_Mp7egOdZU7Jz1worwG8OUL27z2HZMp8tMAlKpQ22XATIsGhfGWia5CQrMzxcL8RilBcj8gjYlBF-8oQNRS9iKtSdGQUEVuRnJHCNTOOAVtzQ1ED5UgEPY1HWuKsLS9XsGAZ6NBXwWpfQmW7z_zrlFPg84HWBVN5GWh6r0r4D2KR_iJdAzQ==)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwaduvQuc2ynE85U9KqUalTcUMG97hN5dHMvls9YYjybmsEePVPvhPmWgkuK20g568_OK28Lze_Z-UTjFFhWw1PNx5rWSCQs1gH9-t05qOlzNRKS4ouYAcThibbAb1eYhTTREV_GrMTiIamWVTU9VLrYBtqTEglwoEaZNcgRC7lPBfUUYyOzPT6ZNWFw3tDRSB_4QgHDvwGJ5_Xs4lWk4WwmwY0-EOBV4EfJ-ReOVenJfEn_00s5WmxiX6I80=)
16. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFGCx0EQSfWMjD2h-1iOQWBz9qYJmmIAyHRs4C21tviRd31JQtM_Y_u44_QxR2K5Tb2_4Vu2m1XLiIydLccWfK4TWfElCHm3TlMeZjpuIhIz24zWQj5ULPBgucF-Eh3l_Y_R04q_E=)
17. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8tue68EHFeF15sODhJ-65kvn_RP_FSbh1TzextBgjUJDnrigymoq_wSeB0zSAiNtnYxDN8TjI0_xPHemHUEUohThhCU0h_B_02M7J9nYpqUhNk-nHrqIZhgmLENXh)
18. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEubZGoTPSI95FeSXZ8eztVd6Yd9JmOBE7040pd9z0k_QBhH1xjPsVc1F7pvLxQbfRzxB8XJ90kB1vm4RSygOpr8y7RV2oytlkg4s5BUt61BcCMXHWGwCkaiu6I6qCaq8N0Mu5QLXo=)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1gLqDrK3Sl7y5XRIQN8ZDWvONKtQWlCcFrvTbGCn-R9SVOxqdhMYif_RCn3xmnKS8ghGtJEpL7PdtBPnMS6XLLBUy-Jomz-TaE2yijsaBFa7Zv_GzM9Q6rnn1KdrvVLmYiDulc8K6AQeocKli-XP5jtjQOK1zQomWAI2u_UcZc7ZBHsWo78TlyV1fw-czDU5-49P23AgPvMrkZ-bvdLhedJv3kZ540kxDNvqsFefmttKxum9c8GZUf3TjRqQexxoOjdSuh8E62t6-6hkm0OntN2n3yr_XKl-4ezh2XLvO0QKZ8MNUPrH0Q2Pw1vKOkarJ892Llr84UdTyMBsO3LkjvxbZf_JcEwM=)
20. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5lqo3Onm3tX9YGInRB0KNWES-P3P7sRNhst3a4ftLwXQ_xld2LQHzWLsz-eus6eHK49AylVQtdFt8MNDfnZo7B01ZmGZ95Va8Cc2cBqybexU8oJV8IBARYCrx0lrMlAcF8uCZMLY=)
21. [internationaljournalofparamedicine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzlqYyquXNycC7usL_Ox3CY8qj9O7EW4d3DGz2oNjSghflQ6HVGI_2YILHoHzMxcRYIW2qpS3fC8_dp0LEagyGLreTbEa_0ggx9oQLXYCNTYqmFyG_tk7V51e3sjQMLGJK4BuyJ9u3TPfUPaKOU6U5ADrt9wo9WEw18KWGgUjjcqY3OUQ=)
22. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdrA2GPwwBSf18rwrs3NM5CfUDK4Mfi6pb4Ny35X1MlspDbo6H776oQY5oncOBsiDRqhtvUKfgzBO7NhL5TG9YKcKnTVSUlmcwNtbLpmdtpryerzspzSaggJ7bDwKV)
23. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGv5DJsNS4DeI6T0VUl9cZgZklclkRnznu9Q7PqEfhT-jm6MW-N09dmlLA25gzPkHC13rP1fek78jFplVWuhpuyCcATQZKoQSYAcFIO_IyqjxCCRy5HifPNqEmWsvlGm5tAkhmFXvA=)
24. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHrMx16GbhXSHGHy86_WK50UWobDG7fG-GknDWng_6dLJ7vFBb-34iiHgSSMNJglh8bhPZeWbU4sOhrdMLhWwAhGzzOKlRGaqk569cSu4U4iun130X-jl9gjzeRsKaq5HOnIKU2fU=)
25. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeyIlQMu9b94ozUmR2I3d1fV5-NI8ekpIcgacEVO3Qw0ZyV8nYNExiCObwj1jLgpMTzjqEYyH-k7ofuNhvK2UZ1CXRzx_bnTbb__rhqSoUQnZ0g9Nc2eXA5RS9Q_9Bt6AVGKo0Ak3MavxByh7Fr5_oybJAQyocZzyvh8ndAJzWN2gYQzTw5G84dfPZsTjdw9Pu0woUg37VB4ybn5cC1bCb7dPGkoekuzpoBS2glVyrXvXONpk25eaHx4834Fq_mwpz4VCm)
26. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPChzLWEnjxEqLMCmbLo1SpheLyKBNtIsewmbUUXyDGtEFfIbgON4LzaT45pX9pZkefNCv5P-myaZ-1p_hJpNGYAtOEMEdlu7kc2NSEldbiMck3Vfv2_qKasyh-w-SJEdmu0u57rSz)
27. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcpDCsx-G_u84XyEmhODTyjWZcaX7ENxxeAHWSMDWXijpVyAX5DhXdVGp_uRGZ3bpPJdh3q7HCQXyuE8nRzDQ_Q3Ct5gV6LaKidvd3Axn7T0A0VdbPUPkt2V_MjB2U)


## Annotations
Annotation(end_index=2027, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIK9NJlo_x3Fl9lQPbwCUjiKJmp_DyZyaLh6tzcegBP9Z7M8dd5o7WejWBmkWz2cApyKetnXi75ypYuMltZF2-3au7iJSK0HpLTwl8y5m4-DNVfLIxnCrsc96mRqPVh3KEffGvdxs=', start_index=2015)
Annotation(end_index=2027, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTuoolj84OSH665wJmTpHJJi9bZl9SThB0H4MUZ2jRRwMuvtOoaoQVshhbZSi2e51cPWRFYopOHYbCPs3vKn45mEp03wxdCi8-PTKiZHZflkmtCBIh9zK_Sc8kpbtlwc8=', start_index=2015)
Annotation(end_index=2606, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMPmvibiVFBYrSb6so4DDjnsh8jMEMBeQnbBvLbt1jqFUR-ioVxqIBwe02D1KnVtWnd_lXpx1iucT3kWGK_t7Qjm09YMJrJcqPWR7CP4syZc8smN8Zws6xZg7nxilgbDQ=', start_index=2594)
Annotation(end_index=2606, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlMltPaUpt7XeaHWc_rg5Xds-ibs37k_LR41OPci2urykQGdttOBPvWjcy485M2bOmmwlvD_rdo7UhFMIxe0ha_6bEYX2OLd_dpEeWlWOXaocbZQ8khHXSjaz1x09yBgzXYEfMKXc=', start_index=2594)
Annotation(end_index=3668, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGAwZY2WtUNSVDmOcZOVVN7lSQgqQIWexBqwstwXP-1deWJaid9wTS7eXjK4k53APhF_RbxxG9DJlG493rEEWgdg_cMju4szYvimLayYgCjSA0ej62cIbRGQ==', start_index=3656)
Annotation(end_index=3668, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIK9NJlo_x3Fl9lQPbwCUjiKJmp_DyZyaLh6tzcegBP9Z7M8dd5o7WejWBmkWz2cApyKetnXi75ypYuMltZF2-3au7iJSK0HpLTwl8y5m4-DNVfLIxnCrsc96mRqPVh3KEffGvdxs=', start_index=3656)
Annotation(end_index=3940, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTuoolj84OSH665wJmTpHJJi9bZl9SThB0H4MUZ2jRRwMuvtOoaoQVshhbZSi2e51cPWRFYopOHYbCPs3vKn45mEp03wxdCi8-PTKiZHZflkmtCBIh9zK_Sc8kpbtlwc8=', start_index=3928)
Annotation(end_index=3940, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGi_kxcBJJfDsFIfYFYSLddtJRJsrQcCNlQ8hyw_Wn-q6wz1gn9szeQa3RWSY8XGWtYmrCpOQA4QMfr2kXF9KnEwEOw1QLArt_z7tVGvakPhCNpLi3F-QjhENMIfgcnAOZDctzPfHk=', start_index=3928)
Annotation(end_index=4019, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIK9NJlo_x3Fl9lQPbwCUjiKJmp_DyZyaLh6tzcegBP9Z7M8dd5o7WejWBmkWz2cApyKetnXi75ypYuMltZF2-3au7iJSK0HpLTwl8y5m4-DNVfLIxnCrsc96mRqPVh3KEffGvdxs=', start_index=4007)
Annotation(end_index=4019, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTuoolj84OSH665wJmTpHJJi9bZl9SThB0H4MUZ2jRRwMuvtOoaoQVshhbZSi2e51cPWRFYopOHYbCPs3vKn45mEp03wxdCi8-PTKiZHZflkmtCBIh9zK_Sc8kpbtlwc8=', start_index=4007)
Annotation(end_index=4161, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwCMRLmmkZtBwRc0U5g1XNbthzXHa30vsFFuem9WaIxuT_zV2TQTG3AIYBwRGYFN8Y_0rEl892wOlYKsuxyT80iXuMlH6Qtbjo9fS7ZrxQ_NkEvEfG-fEQf5RYkZiaGsU05J27ud_psRHq-3pT0YH02t9kEWHqu9XwEc1Sp_bQ_0QgSlTRpMelaqea7HrEdJH0mAsTc0zG0ULM-4bHuGSTvaQ4VKNOeAt2H7KWnNNRx0uCUA==', start_index=4149)
Annotation(end_index=4161, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTuoolj84OSH665wJmTpHJJi9bZl9SThB0H4MUZ2jRRwMuvtOoaoQVshhbZSi2e51cPWRFYopOHYbCPs3vKn45mEp03wxdCi8-PTKiZHZflkmtCBIh9zK_Sc8kpbtlwc8=', start_index=4149)
Annotation(end_index=4348, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQT6M7anAqMG5jtHtbOuUBk4qMtrUAQPTZe_6RmUngd9PFTbiVbzem82wJNuV6j2kGt48K09pbW-_39tcUOLW2r-rbDw3M-gXSd5xHjrQ0TtoJn06ZFgSevZ02c6b1NmKDxAMnOed3BLbC_c8-2FiAIBS0T_qADZYqmWePNsx3hwDbn43O4uoA2gfuuzhp', start_index=4336)
Annotation(end_index=4348, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTuoolj84OSH665wJmTpHJJi9bZl9SThB0H4MUZ2jRRwMuvtOoaoQVshhbZSi2e51cPWRFYopOHYbCPs3vKn45mEp03wxdCi8-PTKiZHZflkmtCBIh9zK_Sc8kpbtlwc8=', start_index=4336)
Annotation(end_index=4521, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGAwZY2WtUNSVDmOcZOVVN7lSQgqQIWexBqwstwXP-1deWJaid9wTS7eXjK4k53APhF_RbxxG9DJlG493rEEWgdg_cMju4szYvimLayYgCjSA0ej62cIbRGQ==', start_index=4509)
Annotation(end_index=4521, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTuoolj84OSH665wJmTpHJJi9bZl9SThB0H4MUZ2jRRwMuvtOoaoQVshhbZSi2e51cPWRFYopOHYbCPs3vKn45mEp03wxdCi8-PTKiZHZflkmtCBIh9zK_Sc8kpbtlwc8=', start_index=4509)
Annotation(end_index=5089, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5AWjekRe7lVfg8N6OGrpcgitSq4DR4JlVBtmBBOUGnXQp-2H7G3d9ve0vBmCICZNMW47e_crF2gD0SCvoYYR-OdUrG00NVavlokkxkhHTDnOTH1YAjhY5OVQfZE-0IKYRuJhRzI4=', start_index=5077)
Annotation(end_index=5089, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGAwZY2WtUNSVDmOcZOVVN7lSQgqQIWexBqwstwXP-1deWJaid9wTS7eXjK4k53APhF_RbxxG9DJlG493rEEWgdg_cMju4szYvimLayYgCjSA0ej62cIbRGQ==', start_index=5077)
Annotation(end_index=5576, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCRaJW6s4qpLl8oQfFkgeEYcuvBxyCxY9KX7barec-ZbMhorrEhveeUzv0yI7Rz1Gc3UJ0M0zor3ojbk031V9b3lzr1T-w6IYplKBM6vR-x5NY4YvrnzjxqR9gN1UQkkq5qzMhdD-iRjXXNMpX3lJvVc1f0tqfDm-5K8orjf4jyoly_b-xz0b7fVM_Hd0pVsH7XwMXDV_YohCKh6P9wv1WkPMhl-yEinpXz3nnvQ_aCUGxO2Ba7A==', start_index=5566)
Annotation(end_index=5835, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5AWjekRe7lVfg8N6OGrpcgitSq4DR4JlVBtmBBOUGnXQp-2H7G3d9ve0vBmCICZNMW47e_crF2gD0SCvoYYR-OdUrG00NVavlokkxkhHTDnOTH1YAjhY5OVQfZE-0IKYRuJhRzI4=', start_index=5822)
Annotation(end_index=5835, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvfs7_yVN3PaB68y0N03dwmcsKnf2q-HfW1frvidqVJvLP-07S_r5UyN9HyRPb1w6m39LKudfqdA49Ne5LSqumIJ73bfZ4Gz5x3MPKrBM6TjlmM8wjpYxXxKW-t5rk', start_index=5822)
Annotation(end_index=6185, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQT6M7anAqMG5jtHtbOuUBk4qMtrUAQPTZe_6RmUngd9PFTbiVbzem82wJNuV6j2kGt48K09pbW-_39tcUOLW2r-rbDw3M-gXSd5xHjrQ0TtoJn06ZFgSevZ02c6b1NmKDxAMnOed3BLbC_c8-2FiAIBS0T_qADZYqmWePNsx3hwDbn43O4uoA2gfuuzhp', start_index=6172)
Annotation(end_index=6185, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFn4Js4lF3cQGEi_kNDaeWda5m2IOAuXpYGfEUmJfPv6XBN1N1vWu881XamPV7tJeaLQZM6Azp0h9JFQ5kL5-X80TX7lBHyEHVUYn0kC0ZH-o0mIITh8yGYBJcHgULgCjrQhW-XYfQ0_KpBr9clL4g3nsawAvGDNE36Mu7f_RPJ9Eb55p8BspgtLiD88uSQB8ZL4tqoAQ==', start_index=6172)
Annotation(end_index=6712, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoAsqoLJGTPFijEEG5gO8z2_kUs34tOwWCMkgplIA9dRYlpA5ka4mLFKgFLqfKETvW-wExOd-jldJjKjPSvR4-SzJoVgycijq2mraZxG87hXba_gvvRmE8S7sUrMia', start_index=6699)
Annotation(end_index=6712, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGi_kxcBJJfDsFIfYFYSLddtJRJsrQcCNlQ8hyw_Wn-q6wz1gn9szeQa3RWSY8XGWtYmrCpOQA4QMfr2kXF9KnEwEOw1QLArt_z7tVGvakPhCNpLi3F-QjhENMIfgcnAOZDctzPfHk=', start_index=6699)
Annotation(end_index=6961, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEE8wJ3AlTKK93wqtGj10gHyPhR0AJj2CA6WNJdsEBLTVcJu4z-0FQyux73RAdEx38Yzo2su5H_Mp7egOdZU7Jz1worwG8OUL27z2HZMp8tMAlKpQ22XATIsGhfGWia5CQrMzxcL8RilBcj8gjYlBF-8oQNRS9iKtSdGQUEVuRnJHCNTOOAVtzQ1ED5UgEPY1HWuKsLS9XsGAZ6NBXwWpfQmW7z_zrlFPg84HWBVN5GWh6r0r4D2KR_iJdAzQ==', start_index=6948)
Annotation(end_index=6961, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGi_kxcBJJfDsFIfYFYSLddtJRJsrQcCNlQ8hyw_Wn-q6wz1gn9szeQa3RWSY8XGWtYmrCpOQA4QMfr2kXF9KnEwEOw1QLArt_z7tVGvakPhCNpLi3F-QjhENMIfgcnAOZDctzPfHk=', start_index=6948)
Annotation(end_index=7621, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIK9NJlo_x3Fl9lQPbwCUjiKJmp_DyZyaLh6tzcegBP9Z7M8dd5o7WejWBmkWz2cApyKetnXi75ypYuMltZF2-3au7iJSK0HpLTwl8y5m4-DNVfLIxnCrsc96mRqPVh3KEffGvdxs=', start_index=7609)
Annotation(end_index=7621, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTuoolj84OSH665wJmTpHJJi9bZl9SThB0H4MUZ2jRRwMuvtOoaoQVshhbZSi2e51cPWRFYopOHYbCPs3vKn45mEp03wxdCi8-PTKiZHZflkmtCBIh9zK_Sc8kpbtlwc8=', start_index=7609)
Annotation(end_index=8100, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMPmvibiVFBYrSb6so4DDjnsh8jMEMBeQnbBvLbt1jqFUR-ioVxqIBwe02D1KnVtWnd_lXpx1iucT3kWGK_t7Qjm09YMJrJcqPWR7CP4syZc8smN8Zws6xZg7nxilgbDQ=', start_index=8091)
Annotation(end_index=8526, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwaduvQuc2ynE85U9KqUalTcUMG97hN5dHMvls9YYjybmsEePVPvhPmWgkuK20g568_OK28Lze_Z-UTjFFhWw1PNx5rWSCQs1gH9-t05qOlzNRKS4ouYAcThibbAb1eYhTTREV_GrMTiIamWVTU9VLrYBtqTEglwoEaZNcgRC7lPBfUUYyOzPT6ZNWFw3tDRSB_4QgHDvwGJ5_Xs4lWk4WwmwY0-EOBV4EfJ-ReOVenJfEn_00s5WmxiX6I80=', start_index=8516)
Annotation(end_index=9175, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlMltPaUpt7XeaHWc_rg5Xds-ibs37k_LR41OPci2urykQGdttOBPvWjcy485M2bOmmwlvD_rdo7UhFMIxe0ha_6bEYX2OLd_dpEeWlWOXaocbZQ8khHXSjaz1x09yBgzXYEfMKXc=', start_index=9166)
Annotation(end_index=9548, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFGCx0EQSfWMjD2h-1iOQWBz9qYJmmIAyHRs4C21tviRd31JQtM_Y_u44_QxR2K5Tb2_4Vu2m1XLiIydLccWfK4TWfElCHm3TlMeZjpuIhIz24zWQj5ULPBgucF-Eh3l_Y_R04q_E=', start_index=9538)
Annotation(end_index=10375, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEubZGoTPSI95FeSXZ8eztVd6Yd9JmOBE7040pd9z0k_QBhH1xjPsVc1F7pvLxQbfRzxB8XJ90kB1vm4RSygOpr8y7RV2oytlkg4s5BUt61BcCMXHWGwCkaiu6I6qCaq8N0Mu5QLXo=', start_index=10361)
Annotation(end_index=10375, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8tue68EHFeF15sODhJ-65kvn_RP_FSbh1TzextBgjUJDnrigymoq_wSeB0zSAiNtnYxDN8TjI0_xPHemHUEUohThhCU0h_B_02M7J9nYpqUhNk-nHrqIZhgmLENXh', start_index=10361)
Annotation(end_index=10666, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIK9NJlo_x3Fl9lQPbwCUjiKJmp_DyZyaLh6tzcegBP9Z7M8dd5o7WejWBmkWz2cApyKetnXi75ypYuMltZF2-3au7iJSK0HpLTwl8y5m4-DNVfLIxnCrsc96mRqPVh3KEffGvdxs=', start_index=10657)
Annotation(end_index=10929, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8tue68EHFeF15sODhJ-65kvn_RP_FSbh1TzextBgjUJDnrigymoq_wSeB0zSAiNtnYxDN8TjI0_xPHemHUEUohThhCU0h_B_02M7J9nYpqUhNk-nHrqIZhgmLENXh', start_index=10915)
Annotation(end_index=10929, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1gLqDrK3Sl7y5XRIQN8ZDWvONKtQWlCcFrvTbGCn-R9SVOxqdhMYif_RCn3xmnKS8ghGtJEpL7PdtBPnMS6XLLBUy-Jomz-TaE2yijsaBFa7Zv_GzM9Q6rnn1KdrvVLmYiDulc8K6AQeocKli-XP5jtjQOK1zQomWAI2u_UcZc7ZBHsWo78TlyV1fw-czDU5-49P23AgPvMrkZ-bvdLhedJv3kZ540kxDNvqsFefmttKxum9c8GZUf3TjRqQexxoOjdSuh8E62t6-6hkm0OntN2n3yr_XKl-4ezh2XLvO0QKZ8MNUPrH0Q2Pw1vKOkarJ892Llr84UdTyMBsO3LkjvxbZf_JcEwM=', start_index=10915)
Annotation(end_index=11355, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIK9NJlo_x3Fl9lQPbwCUjiKJmp_DyZyaLh6tzcegBP9Z7M8dd5o7WejWBmkWz2cApyKetnXi75ypYuMltZF2-3au7iJSK0HpLTwl8y5m4-DNVfLIxnCrsc96mRqPVh3KEffGvdxs=', start_index=11346)
Annotation(end_index=11903, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoAsqoLJGTPFijEEG5gO8z2_kUs34tOwWCMkgplIA9dRYlpA5ka4mLFKgFLqfKETvW-wExOd-jldJjKjPSvR4-SzJoVgycijq2mraZxG87hXba_gvvRmE8S7sUrMia', start_index=11890)
Annotation(end_index=11903, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGi_kxcBJJfDsFIfYFYSLddtJRJsrQcCNlQ8hyw_Wn-q6wz1gn9szeQa3RWSY8XGWtYmrCpOQA4QMfr2kXF9KnEwEOw1QLArt_z7tVGvakPhCNpLi3F-QjhENMIfgcnAOZDctzPfHk=', start_index=11890)
Annotation(end_index=12130, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTuoolj84OSH665wJmTpHJJi9bZl9SThB0H4MUZ2jRRwMuvtOoaoQVshhbZSi2e51cPWRFYopOHYbCPs3vKn45mEp03wxdCi8-PTKiZHZflkmtCBIh9zK_Sc8kpbtlwc8=', start_index=12121)
Annotation(end_index=12347, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGAwZY2WtUNSVDmOcZOVVN7lSQgqQIWexBqwstwXP-1deWJaid9wTS7eXjK4k53APhF_RbxxG9DJlG493rEEWgdg_cMju4szYvimLayYgCjSA0ej62cIbRGQ==', start_index=12335)
Annotation(end_index=12347, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGi_kxcBJJfDsFIfYFYSLddtJRJsrQcCNlQ8hyw_Wn-q6wz1gn9szeQa3RWSY8XGWtYmrCpOQA4QMfr2kXF9KnEwEOw1QLArt_z7tVGvakPhCNpLi3F-QjhENMIfgcnAOZDctzPfHk=', start_index=12335)
Annotation(end_index=12896, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIK9NJlo_x3Fl9lQPbwCUjiKJmp_DyZyaLh6tzcegBP9Z7M8dd5o7WejWBmkWz2cApyKetnXi75ypYuMltZF2-3au7iJSK0HpLTwl8y5m4-DNVfLIxnCrsc96mRqPVh3KEffGvdxs=', start_index=12883)
Annotation(end_index=12896, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5lqo3Onm3tX9YGInRB0KNWES-P3P7sRNhst3a4ftLwXQ_xld2LQHzWLsz-eus6eHK49AylVQtdFt8MNDfnZo7B01ZmGZ95Va8Cc2cBqybexU8oJV8IBARYCrx0lrMlAcF8uCZMLY=', start_index=12883)
Annotation(end_index=13101, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzlqYyquXNycC7usL_Ox3CY8qj9O7EW4d3DGz2oNjSghflQ6HVGI_2YILHoHzMxcRYIW2qpS3fC8_dp0LEagyGLreTbEa_0ggx9oQLXYCNTYqmFyG_tk7V51e3sjQMLGJK4BuyJ9u3TPfUPaKOU6U5ADrt9wo9WEw18KWGgUjjcqY3OUQ=', start_index=13091)
Annotation(end_index=13439, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIK9NJlo_x3Fl9lQPbwCUjiKJmp_DyZyaLh6tzcegBP9Z7M8dd5o7WejWBmkWz2cApyKetnXi75ypYuMltZF2-3au7iJSK0HpLTwl8y5m4-DNVfLIxnCrsc96mRqPVh3KEffGvdxs=', start_index=13426)
Annotation(end_index=13439, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdrA2GPwwBSf18rwrs3NM5CfUDK4Mfi6pb4Ny35X1MlspDbo6H776oQY5oncOBsiDRqhtvUKfgzBO7NhL5TG9YKcKnTVSUlmcwNtbLpmdtpryerzspzSaggJ7bDwKV', start_index=13426)
Annotation(end_index=13734, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMPmvibiVFBYrSb6so4DDjnsh8jMEMBeQnbBvLbt1jqFUR-ioVxqIBwe02D1KnVtWnd_lXpx1iucT3kWGK_t7Qjm09YMJrJcqPWR7CP4syZc8smN8Zws6xZg7nxilgbDQ=', start_index=13721)
Annotation(end_index=13734, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGv5DJsNS4DeI6T0VUl9cZgZklclkRnznu9Q7PqEfhT-jm6MW-N09dmlLA25gzPkHC13rP1fek78jFplVWuhpuyCcATQZKoQSYAcFIO_IyqjxCCRy5HifPNqEmWsvlGm5tAkhmFXvA=', start_index=13721)
Annotation(end_index=14079, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlMltPaUpt7XeaHWc_rg5Xds-ibs37k_LR41OPci2urykQGdttOBPvWjcy485M2bOmmwlvD_rdo7UhFMIxe0ha_6bEYX2OLd_dpEeWlWOXaocbZQ8khHXSjaz1x09yBgzXYEfMKXc=', start_index=14070)
Annotation(end_index=14300, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5AWjekRe7lVfg8N6OGrpcgitSq4DR4JlVBtmBBOUGnXQp-2H7G3d9ve0vBmCICZNMW47e_crF2gD0SCvoYYR-OdUrG00NVavlokkxkhHTDnOTH1YAjhY5OVQfZE-0IKYRuJhRzI4=', start_index=14291)
Annotation(end_index=15397, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTuoolj84OSH665wJmTpHJJi9bZl9SThB0H4MUZ2jRRwMuvtOoaoQVshhbZSi2e51cPWRFYopOHYbCPs3vKn45mEp03wxdCi8-PTKiZHZflkmtCBIh9zK_Sc8kpbtlwc8=', start_index=15388)
Annotation(end_index=15504, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGi_kxcBJJfDsFIfYFYSLddtJRJsrQcCNlQ8hyw_Wn-q6wz1gn9szeQa3RWSY8XGWtYmrCpOQA4QMfr2kXF9KnEwEOw1QLArt_z7tVGvakPhCNpLi3F-QjhENMIfgcnAOZDctzPfHk=', start_index=15495)
Annotation(end_index=15668, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIK9NJlo_x3Fl9lQPbwCUjiKJmp_DyZyaLh6tzcegBP9Z7M8dd5o7WejWBmkWz2cApyKetnXi75ypYuMltZF2-3au7iJSK0HpLTwl8y5m4-DNVfLIxnCrsc96mRqPVh3KEffGvdxs=', start_index=15659)
Annotation(end_index=15803, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMPmvibiVFBYrSb6so4DDjnsh8jMEMBeQnbBvLbt1jqFUR-ioVxqIBwe02D1KnVtWnd_lXpx1iucT3kWGK_t7Qjm09YMJrJcqPWR7CP4syZc8smN8Zws6xZg7nxilgbDQ=', start_index=15794)
Annotation(end_index=15919, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQT6M7anAqMG5jtHtbOuUBk4qMtrUAQPTZe_6RmUngd9PFTbiVbzem82wJNuV6j2kGt48K09pbW-_39tcUOLW2r-rbDw3M-gXSd5xHjrQ0TtoJn06ZFgSevZ02c6b1NmKDxAMnOed3BLbC_c8-2FiAIBS0T_qADZYqmWePNsx3hwDbn43O4uoA2gfuuzhp', start_index=15910)
Annotation(end_index=15979, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwaduvQuc2ynE85U9KqUalTcUMG97hN5dHMvls9YYjybmsEePVPvhPmWgkuK20g568_OK28Lze_Z-UTjFFhWw1PNx5rWSCQs1gH9-t05qOlzNRKS4ouYAcThibbAb1eYhTTREV_GrMTiIamWVTU9VLrYBtqTEglwoEaZNcgRC7lPBfUUYyOzPT6ZNWFw3tDRSB_4QgHDvwGJ5_Xs4lWk4WwmwY0-EOBV4EfJ-ReOVenJfEn_00s5WmxiX6I80=', start_index=15969)
Annotation(end_index=16099, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzlqYyquXNycC7usL_Ox3CY8qj9O7EW4d3DGz2oNjSghflQ6HVGI_2YILHoHzMxcRYIW2qpS3fC8_dp0LEagyGLreTbEa_0ggx9oQLXYCNTYqmFyG_tk7V51e3sjQMLGJK4BuyJ9u3TPfUPaKOU6U5ADrt9wo9WEw18KWGgUjjcqY3OUQ=', start_index=16089)
Annotation(end_index=16220, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMPmvibiVFBYrSb6so4DDjnsh8jMEMBeQnbBvLbt1jqFUR-ioVxqIBwe02D1KnVtWnd_lXpx1iucT3kWGK_t7Qjm09YMJrJcqPWR7CP4syZc8smN8Zws6xZg7nxilgbDQ=', start_index=16211)
Annotation(end_index=16314, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8tue68EHFeF15sODhJ-65kvn_RP_FSbh1TzextBgjUJDnrigymoq_wSeB0zSAiNtnYxDN8TjI0_xPHemHUEUohThhCU0h_B_02M7J9nYpqUhNk-nHrqIZhgmLENXh', start_index=16304)
Annotation(end_index=16412, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEubZGoTPSI95FeSXZ8eztVd6Yd9JmOBE7040pd9z0k_QBhH1xjPsVc1F7pvLxQbfRzxB8XJ90kB1vm4RSygOpr8y7RV2oytlkg4s5BUt61BcCMXHWGwCkaiu6I6qCaq8N0Mu5QLXo=', start_index=16402)
Annotation(end_index=16506, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHrMx16GbhXSHGHy86_WK50UWobDG7fG-GknDWng_6dLJ7vFBb-34iiHgSSMNJglh8bhPZeWbU4sOhrdMLhWwAhGzzOKlRGaqk569cSu4U4iun130X-jl9gjzeRsKaq5HOnIKU2fU=', start_index=16496)
Annotation(end_index=16596, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeyIlQMu9b94ozUmR2I3d1fV5-NI8ekpIcgacEVO3Qw0ZyV8nYNExiCObwj1jLgpMTzjqEYyH-k7ofuNhvK2UZ1CXRzx_bnTbb__rhqSoUQnZ0g9Nc2eXA5RS9Q_9Bt6AVGKo0Ak3MavxByh7Fr5_oybJAQyocZzyvh8ndAJzWN2gYQzTw5G84dfPZsTjdw9Pu0woUg37VB4ybn5cC1bCb7dPGkoekuzpoBS2glVyrXvXONpk25eaHx4834Fq_mwpz4VCm', start_index=16586)
Annotation(end_index=16723, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5AWjekRe7lVfg8N6OGrpcgitSq4DR4JlVBtmBBOUGnXQp-2H7G3d9ve0vBmCICZNMW47e_crF2gD0SCvoYYR-OdUrG00NVavlokkxkhHTDnOTH1YAjhY5OVQfZE-0IKYRuJhRzI4=', start_index=16714)
Annotation(end_index=16821, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvfs7_yVN3PaB68y0N03dwmcsKnf2q-HfW1frvidqVJvLP-07S_r5UyN9HyRPb1w6m39LKudfqdA49Ne5LSqumIJ73bfZ4Gz5x3MPKrBM6TjlmM8wjpYxXxKW-t5rk', start_index=16811)
Annotation(end_index=16921, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIK9NJlo_x3Fl9lQPbwCUjiKJmp_DyZyaLh6tzcegBP9Z7M8dd5o7WejWBmkWz2cApyKetnXi75ypYuMltZF2-3au7iJSK0HpLTwl8y5m4-DNVfLIxnCrsc96mRqPVh3KEffGvdxs=', start_index=16912)
Annotation(end_index=17020, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGi_kxcBJJfDsFIfYFYSLddtJRJsrQcCNlQ8hyw_Wn-q6wz1gn9szeQa3RWSY8XGWtYmrCpOQA4QMfr2kXF9KnEwEOw1QLArt_z7tVGvakPhCNpLi3F-QjhENMIfgcnAOZDctzPfHk=', start_index=17011)
Annotation(end_index=17121, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTuoolj84OSH665wJmTpHJJi9bZl9SThB0H4MUZ2jRRwMuvtOoaoQVshhbZSi2e51cPWRFYopOHYbCPs3vKn45mEp03wxdCi8-PTKiZHZflkmtCBIh9zK_Sc8kpbtlwc8=', start_index=17112)
Annotation(end_index=17216, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlMltPaUpt7XeaHWc_rg5Xds-ibs37k_LR41OPci2urykQGdttOBPvWjcy485M2bOmmwlvD_rdo7UhFMIxe0ha_6bEYX2OLd_dpEeWlWOXaocbZQ8khHXSjaz1x09yBgzXYEfMKXc=', start_index=17207)
Annotation(end_index=17297, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFGCx0EQSfWMjD2h-1iOQWBz9qYJmmIAyHRs4C21tviRd31JQtM_Y_u44_QxR2K5Tb2_4Vu2m1XLiIydLccWfK4TWfElCHm3TlMeZjpuIhIz24zWQj5ULPBgucF-Eh3l_Y_R04q_E=', start_index=17287)
Annotation(end_index=17373, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdrA2GPwwBSf18rwrs3NM5CfUDK4Mfi6pb4Ny35X1MlspDbo6H776oQY5oncOBsiDRqhtvUKfgzBO7NhL5TG9YKcKnTVSUlmcwNtbLpmdtpryerzspzSaggJ7bDwKV', start_index=17363)
Annotation(end_index=17473, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwaduvQuc2ynE85U9KqUalTcUMG97hN5dHMvls9YYjybmsEePVPvhPmWgkuK20g568_OK28Lze_Z-UTjFFhWw1PNx5rWSCQs1gH9-t05qOlzNRKS4ouYAcThibbAb1eYhTTREV_GrMTiIamWVTU9VLrYBtqTEglwoEaZNcgRC7lPBfUUYyOzPT6ZNWFw3tDRSB_4QgHDvwGJ5_Xs4lWk4WwmwY0-EOBV4EfJ-ReOVenJfEn_00s5WmxiX6I80=', start_index=17463)
Annotation(end_index=17593, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPChzLWEnjxEqLMCmbLo1SpheLyKBNtIsewmbUUXyDGtEFfIbgON4LzaT45pX9pZkefNCv5P-myaZ-1p_hJpNGYAtOEMEdlu7kc2NSEldbiMck3Vfv2_qKasyh-w-SJEdmu0u57rSz', start_index=17583)
Annotation(end_index=17689, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGi_kxcBJJfDsFIfYFYSLddtJRJsrQcCNlQ8hyw_Wn-q6wz1gn9szeQa3RWSY8XGWtYmrCpOQA4QMfr2kXF9KnEwEOw1QLArt_z7tVGvakPhCNpLi3F-QjhENMIfgcnAOZDctzPfHk=', start_index=17680)
Annotation(end_index=17779, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIK9NJlo_x3Fl9lQPbwCUjiKJmp_DyZyaLh6tzcegBP9Z7M8dd5o7WejWBmkWz2cApyKetnXi75ypYuMltZF2-3au7iJSK0HpLTwl8y5m4-DNVfLIxnCrsc96mRqPVh3KEffGvdxs=', start_index=17770)
Annotation(end_index=17867, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEGAwZY2WtUNSVDmOcZOVVN7lSQgqQIWexBqwstwXP-1deWJaid9wTS7eXjK4k53APhF_RbxxG9DJlG493rEEWgdg_cMju4szYvimLayYgCjSA0ej62cIbRGQ==', start_index=17858)
Annotation(end_index=17951, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTuoolj84OSH665wJmTpHJJi9bZl9SThB0H4MUZ2jRRwMuvtOoaoQVshhbZSi2e51cPWRFYopOHYbCPs3vKn45mEp03wxdCi8-PTKiZHZflkmtCBIh9zK_Sc8kpbtlwc8=', start_index=17942)
Annotation(end_index=18033, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEE8wJ3AlTKK93wqtGj10gHyPhR0AJj2CA6WNJdsEBLTVcJu4z-0FQyux73RAdEx38Yzo2su5H_Mp7egOdZU7Jz1worwG8OUL27z2HZMp8tMAlKpQ22XATIsGhfGWia5CQrMzxcL8RilBcj8gjYlBF-8oQNRS9iKtSdGQUEVuRnJHCNTOOAVtzQ1ED5UgEPY1HWuKsLS9XsGAZ6NBXwWpfQmW7z_zrlFPg84HWBVN5GWh6r0r4D2KR_iJdAzQ==', start_index=18023)
Annotation(end_index=18130, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5lqo3Onm3tX9YGInRB0KNWES-P3P7sRNhst3a4ftLwXQ_xld2LQHzWLsz-eus6eHK49AylVQtdFt8MNDfnZo7B01ZmGZ95Va8Cc2cBqybexU8oJV8IBARYCrx0lrMlAcF8uCZMLY=', start_index=18120)
Annotation(end_index=18228, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFn4Js4lF3cQGEi_kNDaeWda5m2IOAuXpYGfEUmJfPv6XBN1N1vWu881XamPV7tJeaLQZM6Azp0h9JFQ5kL5-X80TX7lBHyEHVUYn0kC0ZH-o0mIITh8yGYBJcHgULgCjrQhW-XYfQ0_KpBr9clL4g3nsawAvGDNE36Mu7f_RPJ9Eb55p8BspgtLiD88uSQB8ZL4tqoAQ==', start_index=18218)
Annotation(end_index=18341, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIK9NJlo_x3Fl9lQPbwCUjiKJmp_DyZyaLh6tzcegBP9Z7M8dd5o7WejWBmkWz2cApyKetnXi75ypYuMltZF2-3au7iJSK0HpLTwl8y5m4-DNVfLIxnCrsc96mRqPVh3KEffGvdxs=', start_index=18332)
Annotation(end_index=18443, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoAsqoLJGTPFijEEG5gO8z2_kUs34tOwWCMkgplIA9dRYlpA5ka4mLFKgFLqfKETvW-wExOd-jldJjKjPSvR4-SzJoVgycijq2mraZxG87hXba_gvvRmE8S7sUrMia', start_index=18433)
Annotation(end_index=18564, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCRaJW6s4qpLl8oQfFkgeEYcuvBxyCxY9KX7barec-ZbMhorrEhveeUzv0yI7Rz1Gc3UJ0M0zor3ojbk031V9b3lzr1T-w6IYplKBM6vR-x5NY4YvrnzjxqR9gN1UQkkq5qzMhdD-iRjXXNMpX3lJvVc1f0tqfDm-5K8orjf4jyoly_b-xz0b7fVM_Hd0pVsH7XwMXDV_YohCKh6P9wv1WkPMhl-yEinpXz3nnvQ_aCUGxO2Ba7A==', start_index=18554)
Annotation(end_index=18693, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGv5DJsNS4DeI6T0VUl9cZgZklclkRnznu9Q7PqEfhT-jm6MW-N09dmlLA25gzPkHC13rP1fek78jFplVWuhpuyCcATQZKoQSYAcFIO_IyqjxCCRy5HifPNqEmWsvlGm5tAkhmFXvA=', start_index=18683)
Annotation(end_index=18786, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1gLqDrK3Sl7y5XRIQN8ZDWvONKtQWlCcFrvTbGCn-R9SVOxqdhMYif_RCn3xmnKS8ghGtJEpL7PdtBPnMS6XLLBUy-Jomz-TaE2yijsaBFa7Zv_GzM9Q6rnn1KdrvVLmYiDulc8K6AQeocKli-XP5jtjQOK1zQomWAI2u_UcZc7ZBHsWo78TlyV1fw-czDU5-49P23AgPvMrkZ-bvdLhedJv3kZ540kxDNvqsFefmttKxum9c8GZUf3TjRqQexxoOjdSuh8E62t6-6hkm0OntN2n3yr_XKl-4ezh2XLvO0QKZ8MNUPrH0Q2Pw1vKOkarJ892Llr84UdTyMBsO3LkjvxbZf_JcEwM=', start_index=18776)
Annotation(end_index=18935, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwCMRLmmkZtBwRc0U5g1XNbthzXHa30vsFFuem9WaIxuT_zV2TQTG3AIYBwRGYFN8Y_0rEl892wOlYKsuxyT80iXuMlH6Qtbjo9fS7ZrxQ_NkEvEfG-fEQf5RYkZiaGsU05J27ud_psRHq-3pT0YH02t9kEWHqu9XwEc1Sp_bQ_0QgSlTRpMelaqea7HrEdJH0mAsTc0zG0ULM-4bHuGSTvaQ4VKNOeAt2H7KWnNNRx0uCUA==', start_index=18926)
Annotation(end_index=19025, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwaduvQuc2ynE85U9KqUalTcUMG97hN5dHMvls9YYjybmsEePVPvhPmWgkuK20g568_OK28Lze_Z-UTjFFhWw1PNx5rWSCQs1gH9-t05qOlzNRKS4ouYAcThibbAb1eYhTTREV_GrMTiIamWVTU9VLrYBtqTEglwoEaZNcgRC7lPBfUUYyOzPT6ZNWFw3tDRSB_4QgHDvwGJ5_Xs4lWk4WwmwY0-EOBV4EfJ-ReOVenJfEn_00s5WmxiX6I80=', start_index=19015)
Annotation(end_index=19161, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPChzLWEnjxEqLMCmbLo1SpheLyKBNtIsewmbUUXyDGtEFfIbgON4LzaT45pX9pZkefNCv5P-myaZ-1p_hJpNGYAtOEMEdlu7kc2NSEldbiMck3Vfv2_qKasyh-w-SJEdmu0u57rSz', start_index=19151)
Annotation(end_index=19269, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcpDCsx-G_u84XyEmhODTyjWZcaX7ENxxeAHWSMDWXijpVyAX5DhXdVGp_uRGZ3bpPJdh3q7HCQXyuE8nRzDQ_Q3Ct5gV6LaKidvd3Axn7T0A0VdbPUPkt2V_MjB2U', start_index=19259)

## Sources
