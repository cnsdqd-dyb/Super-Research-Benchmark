# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 2/5 | **Run ID:** 5fade244 | **Time:** 295.75s | **Cost:** $1.14861
--------------------------------------------------------------------------------

# Predicting Clinical Efficacy of Multi-Target Antipsychotics: Integrating Dose-Response, Animal Models, and Human Receptor Affinity

**Key Points**
*   **The Translation Gap:** Direct scaling of doses from animal models to humans based solely on body surface area often fails for antipsychotics due to significant interspecies differences in receptor affinity and protein binding.
*   **Receptor Occupancy (RO) as the Bridge:** The most reliable predictor of clinical efficacy is not the absolute dose, but the achievement of specific receptor occupancy thresholds (e.g., 65–80% striatal D2 occupancy) in the human brain, which must be modeled from animal data.
*   **Affinity Balancing:** Multi-target drugs (e.g., atypical antipsychotics) rely on specific affinity ratios (such as 5-HT2A/D2) to achieve efficacy with reduced side effects. Predictive models must account for the fact that these ratios may differ between rodents and humans due to structural receptor variances (e.g., 5-HT2A residue differences).
*   **PK/PD Integration:** Modern prediction utilizes Physiologically Based Pharmacokinetic (PBPK) modeling to link plasma concentrations to brain extracellular fluid concentrations, subsequently using binding kinetics ($K_{on}$, $K_{off}$) to predict dynamic receptor occupancy over time.
*   **Functional Potency vs. Binding:** Recent research emphasizes that binding affinity ($K_i$) alone is insufficient; functional potency (e.g., GTP$\gamma$S binding, signaling pathway activation) and residence time (binding kinetics) are critical for accurate translation.

## 1. Introduction

The development of antipsychotic medications has evolved from the serendipitous discovery of chlorpromazine to the rational design of multi-target ligands (MTLs). While First-Generation Antipsychotics (FGAs) primarily targeted the dopamine D2 receptor, Second-Generation Antipsychotics (SGAs), or "atypicals," are defined by their complex polypharmacology, interacting with a spectrum of serotonergic, dopaminergic, adrenergic, muscarinic, and histaminergic receptors [cite: 1, 2]. This shift towards "dirty drugs"—or more accurately, richly pharmacologic agents—offers enhanced efficacy against negative symptoms and cognitive deficits while mitigating extrapyramidal side effects (EPS) [cite: 2].

However, the increased complexity of these pharmacological profiles presents a formidable challenge in translational medicine: predicting the clinically effective dose and efficacy profile in humans based on preclinical animal data. The traditional paradigm of allometric scaling (e.g., converting animal doses to human doses based on body surface area) is often insufficient for CNS drugs because it fails to account for species-specific differences in receptor homology, transporter function, and neurochemistry [cite: 3, 4].

To bridge this gap, researchers employ a sophisticated integration of dose-response curves from animal models (such as conditioned avoidance response or prepulse inhibition) with human receptor affinity data. This process involves "affinity balancing," where the ratios of engagement at various targets (e.g., the 5-HT2A/D2 ratio) are optimized, and "translational PK/PD modeling," which uses receptor occupancy (RO) as a universal biomarker to translate plasma concentrations across species [cite: 5, 6]. This report provides an exhaustive analysis of the methodologies, biological underpinnings, and mathematical frameworks used to predict the clinical efficacy of multi-target antipsychotics.

## 2. The Pharmacodynamic Basis: Receptor Affinity and Occupancy

The fundamental premise of antipsychotic dosing prediction is that clinical effects—both therapeutic and adverse—are driven by the extent to which specific receptors in the brain are occupied by the drug.

### 2.1 The Dopamine D2 Threshold Hypothesis
The cornerstone of antipsychotic pharmacodynamics is the D2 receptor occupancy theory. Extensive Positron Emission Tomography (PET) studies using radioligands like [11C]raclopride have established a "therapeutic window" for antipsychotic action.
*   **Efficacy Threshold:** Clinical antipsychotic response is consistently associated with striatal D2 receptor occupancy exceeding **65–70%** [cite: 7, 8, 9, 10].
*   **Safety Threshold:** Occupancy levels exceeding **80%** are strongly correlated with the emergence of Extrapyramidal Symptoms (EPS), such as parkinsonism and dystonia [cite: 7, 8, 9].
*   **The Window:** Therefore, the optimal clinical dose is one that maintains D2 occupancy between 65% and 80% [cite: 8, 10].

This threshold appears consistent across chemically distinct drug classes, including both FGAs like haloperidol and SGAs like risperidone [cite: 10]. Consequently, the primary goal of preclinical modeling is not merely to find a dose that changes behavior in a rat, but to find the dose that achieves 65–80% D2 occupancy in the human brain.

### 2.2 The Role of 5-HT2A and Affinity Ratios
While D2 blockade drives antipsychotic efficacy against positive symptoms (hallucinations, delusions), the "atypicality" of SGAs—characterized by low EPS liability and efficacy in treatment-resistant cases—is often attributed to their high affinity for serotonin 5-HT2A receptors relative to D2 receptors [cite: 11, 12].

*   **The Meltzer Hypothesis:** This theory posits that a high 5-HT2A/D2 affinity ratio ($pK_i$ ratio) is the defining feature of atypical antipsychotics [cite: 12, 13]. For example, risperidone has a 5-HT2A/D2 affinity ratio of approximately 20, meaning it binds 20 times more potently to 5-HT2A receptors than D2 receptors [cite: 14, 15].
*   **Mechanism:** 5-HT2A antagonism promotes dopamine release in the nigrostriatal pathway, which competes with the antipsychotic for D2 receptors. This competitive displacement prevents the complete blockade (depolarization block) that leads to EPS, effectively widening the therapeutic window [cite: 15].
*   **Clinical Translation:** In clinical settings, atypical antipsychotics often achieve >90% 5-HT2A occupancy at doses where D2 occupancy is only 60–70% [cite: 16, 17].

### 2.3 Multi-Target Profiles (Polypharmacology)
Beyond D2 and 5-HT2A, the clinical profile is shaped by a "fingerprint" of affinities:
*   **5-HT1A Agonism:** Associated with anxiolytic effects and cognitive enhancement (e.g., ziprasidone, quetiapine, clozapine) [cite: 12, 13].
*   **5-HT7 Antagonism:** Implicated in cognitive improvement and antidepressant effects [cite: 14].
*   **D3 Antagonism:** Preferential D3 binding (e.g., cariprazine) is linked to improvements in negative symptoms and motivation [cite: 18].
*   **Off-Target Effects:** High affinity for Histamine H1 and 5-HT2C receptors predicts weight gain and metabolic syndrome [cite: 11, 19], while $\alpha_1$-adrenergic blockade predicts orthostatic hypotension [cite: 14].

Predicting the clinical efficacy of a new compound requires balancing these affinities. A compound with high D2 affinity but low 5-HT2A affinity would be predicted to behave like a typical antipsychotic (high EPS risk), whereas a compound with balanced D2/5-HT2A affinity and moderate 5-HT1A activity would be predicted to have an atypical profile [cite: 1, 20].

## 3. Animal Models in Dose Prediction

Animal models serve two primary functions in this context: establishing the *functional* dose-response relationship for antipsychotic-like activity and providing tissue for pharmacokinetic (PK) analysis.

### 3.1 Models of Efficacy and Side Effects
To predict the clinical therapeutic index, researchers compare the dose-response curves for efficacy models against side-effect models.

*   **Predictive Efficacy Models:**
    *   **Hyperlocomotion:** The reversal of amphetamine- or phencyclidine (PCP)-induced hyperlocomotion in rodents is a standard screen. It correlates well with D2 blockade [cite: 21, 22].
    *   **Conditioned Avoidance Response (CAR):** Antipsychotics selectively suppress avoidance behavior without suppressing escape behavior. The ED50 in CAR is a robust predictor of the clinical antipsychotic dose [cite: 7].
    *   **Prepulse Inhibition (PPI):** Patients with schizophrenia show deficits in sensorimotor gating (PPI). Reversal of PPI deficits in animals (induced by apomorphine or PCP) predicts efficacy against cognitive/sensorimotor deficits [cite: 23].

*   **Side Effect Models:**
    *   **Catalepsy:** The bar test measures the latency of a rodent to correct an imposed posture. Catalepsy in rats is the preclinical equivalent of EPS in humans. It typically occurs at D2 occupancy levels >80% [cite: 7, 24].

### 3.2 The "Receptor Tautology" Problem
A major limitation in using animal models to predict efficacy is "receptor tautology." Many models (like amphetamine-induced hyperlocomotion) are driven by dopamine release. Therefore, any D2 antagonist will show efficacy. These models often fail to predict efficacy for negative symptoms or cognitive deficits, which are not solely dopamine-dependent [cite: 23]. This necessitates the use of multi-target models (e.g., MAM models, isolation rearing) to assess the contribution of non-D2 mechanisms [cite: 21, 25].

### 3.3 Dosing Discrepancies
Historically, animal studies often used arbitrary high doses (e.g., haloperidol 1 mg/kg). Research has shown that 1 mg/kg of haloperidol in rats produces near-saturation of D2 receptors, far exceeding the clinical therapeutic range [cite: 7].
*   **Correction:** To accurately predict clinical efficacy, researchers must identify the animal dose that produces **equivalent receptor occupancy** to the human therapeutic range (60–80%), rather than simply scaling by weight. For haloperidol in rats, a dose as low as 0.03–0.06 mg/kg is sufficient to achieve ~75% occupancy [cite: 7, 21].

## 4. The Translational Challenge: Species Differences

A critical failure point in predicting clinical efficacy is the assumption that a drug interacts with a rat receptor exactly as it does with a human receptor.

### 4.1 Structural Differences in Receptors
While G-protein coupled receptors (GPCRs) are evolutionarily conserved, minor amino acid substitutions can drastically alter drug affinity.
*   **The 5-HT2A Divergence:** There is a significant species difference in the 5-HT2A receptor between rodents and humans. Specifically, a serine residue in the human receptor (Ser242) is replaced by an alanine (Ala242) in the rat receptor (transmembrane domain 5) [cite: 26, 27].
*   **Impact on Affinity:** This single mutation can change the binding affinity ($K_i$) and functional potency of ligands by orders of magnitude. For example, certain N-substituted ergolines show high affinity for the human receptor but low affinity for the rat receptor [cite: 27].
*   **Consequence:** If a multi-target drug relies on a specific 5-HT2A/D2 ratio for its atypical profile, and the rat 5-HT2A affinity is 10-fold lower than human, the drug might appear "typical" (low 5-HT2A/D2 ratio) in rats but "atypical" in humans. Conversely, a dose selected to achieve 5-HT2A blockade in rats might be toxic in humans [cite: 26, 28].

### 4.2 Pharmacokinetic Differences
Rodents generally metabolize drugs much faster than humans.
*   **Half-life Disparity:** Haloperidol has a half-life of ~2.5 hours in rats versus ~24 hours in humans [cite: 7]. This means that a single daily dose in rats results in "sawtooth" occupancy—high peak occupancy (toxicity risk) followed by low trough occupancy (loss of efficacy)—whereas humans maintain steady-state occupancy.
*   **Protein Binding:** Differences in plasma protein binding ($f_u$, fraction unbound) mean that total plasma concentration is a poor predictor of brain exposure across species. Translational models must use **unbound** drug concentration ($C_u$) to predict target engagement [cite: 28, 29].

## 5. Methodologies for Prediction: Balancing Curves and Affinity

To predict the clinical dose and efficacy, researchers employ a stepwise integration of the data described above.

### 5.1 Step 1: In Vitro Profiling (The Affinity Fingerprint)
The first step is determining the binding affinity ($K_i$) and functional potency ($EC_{50}$/$IC_{50}$) of the compound for a broad panel of *human* receptors [cite: 30, 31].
*   **Affinity Balancing:** Researchers calculate ratios (e.g., 5-HT2A/D2, D2/D3) to predict the class of the drug. A ratio >1 (higher affinity for 5-HT2A) suggests atypical potential [cite: 14, 15].
*   **Functional Potency:** Recent work emphasizes that $K_i$ (binding) does not always equal function. A drug might bind tightly but have low intrinsic efficacy or slow signaling kinetics. Functional assays (e.g., GTP$\gamma$S binding) are used to refine these predictions [cite: 31, 32].

### 5.2 Step 2: In Vivo Receptor Occupancy (Animal)
The compound is administered to animals, and ex vivo or in vivo (microPET) methods measure receptor occupancy at various doses.
*   **PK/RO Modeling:** A sigmoidal $E_{max}$ model is fitted to the data to determine the plasma concentration required for 50% occupancy ($EC_{50\_RO}$) [cite: 33].
    \[ RO = \frac{C_{plasma} \times B_{max}}{C_{plasma} + EC_{50\_RO}} \]
    *(Note: This is a simplified representation; actual models account for free fraction and active transport).*

### 5.3 Step 3: Translational PK/PD Modeling
This is the critical "balancing" step where animal data is converted to human predictions.
*   **Correction for Affinity ($K_i$ Ratio):** If the drug has different affinities for the human vs. rat receptor, the target concentration must be adjusted.
    \[ C_{human\_target} = C_{rat\_target} \times \frac{K_{i\_human}}{K_{i\_rat}} \]
    For example, in the development of vortioxetine, a 10-fold higher plasma concentration was required in rats to achieve the same serotonin transporter (SERT) occupancy as in humans due to a 6-fold weaker affinity in rats [cite: 28].
*   **PBPK Modeling:** Physiologically Based Pharmacokinetic models simulate the distribution of the drug into the human brain. These models incorporate:
    1.  **Physicochemical properties:** Lipophilicity, pKa, solubility.
    2.  **In vitro data:** Human microsomal stability, plasma protein binding.
    3.  **Transporter kinetics:** P-glycoprotein (P-gp) efflux at the blood-brain barrier (BBB) [cite: 5].
*   **Prediction:** The model predicts the human dose required to maintain unbound brain extracellular fluid ($C_{brain,u}$) concentrations within the range that achieves 65–80% D2 occupancy (and appropriate occupancy at other targets like 5-HT2A) [cite: 5, 6].

### 5.4 Step 4: Clinical Verification (Phase I/II)
The predicted doses are tested in Phase I (safety) and Phase II (efficacy) trials. PET imaging in humans is often used to validate the predicted occupancy.
*   **Success/Failure Analysis:** If the predicted dose fails to show efficacy, it may be due to:
    *   **Incorrect Target:** The hypothesis that the target (e.g., D2) drives efficacy was wrong for that specific symptom.
    *   **Trial Design:** Testing in chronic patients with supersensitive receptors (due to prior treatment) rather than drug-naive patients [cite: 25].
    *   **Translational Error:** Failure to account for active metabolites or species-specific protein binding [cite: 34].

## 6. Advanced Concepts in Prediction

### 6.1 Binding Kinetics (The "Fast-Off" Theory)
Beyond static affinity ($K_i$), the *residence time* of the drug on the receptor is crucial.
*   **Theory:** Atypical antipsychotics like clozapine and quetiapine have "fast-off" kinetics—they dissociate rapidly from the D2 receptor. This allows physiological dopamine surges (e.g., in response to reward) to temporarily displace the drug, preserving normal signaling and reducing side effects [cite: 10, 15].
*   **Prediction:** Translational models now incorporate association ($k_{on}$) and dissociation ($k_{off}$) rates. A drug with high affinity but fast dissociation might require a different dosing strategy than a "tight binder" like haloperidol [cite: 5].

### 6.2 Quantitative Systems Pharmacology (QSP)
QSP moves beyond simple receptor occupancy to simulate the downstream effects of drug binding on neuronal networks.
*   **Network Effect:** A QSP model might simulate how 5-HT2A blockade in the cortex combined with D2 blockade in the striatum affects the firing rate of pyramidal neurons. This approach helps predict complex clinical outcomes like cognitive improvement or EPS liability better than simple occupancy thresholds [cite: 35].

### 6.3 Allometric Scaling vs. Mechanism-Based Prediction
While simple allometric scaling (e.g., FDA guidance based on Body Surface Area) is used for starting dose estimation in Phase I [cite: 3, 4, 36], it is often inaccurate for efficacy prediction in CNS drugs.
*   **The Case of Fingolimod:** In MS, animal models predicted the effective dose (0.5 mg) accurately, whereas initial clinical trials tested much higher doses (1.25–5 mg) based on safety margins, only to scale back later [cite: 3].
*   **The Case of Risperidone:** Early clinical trials tested doses up to 16 mg, but PET studies and clinical experience later confirmed that 4–6 mg was the optimal range (corresponding to the 65–80% occupancy window) [cite: 15, 37]. This highlights the value of mechanism-based (occupancy) prediction over empirical dose-escalation.

## 7. Conclusion

The clinical efficacy of multi-target antipsychotics is predicted not by a linear extrapolation of animal doses, but by a complex integration of **pharmacokinetics** (how much drug gets to the brain) and **pharmacodynamics** (how the drug interacts with receptors).

The "balancing" act involves:
1.  **Balancing Affinities:** Designing molecules with specific ratios (e.g., high 5-HT2A/D2) to maximize the therapeutic index.
2.  **Balancing Species Differences:** Correcting for the fact that rats and humans have different receptor structures (e.g., 5-HT2A residues) and metabolic rates.
3.  **Balancing Occupancy:** Targeting the specific window of 65–80% D2 occupancy in humans, while simultaneously engaging other targets (5-HT2A, 5-HT1A) to confer atypical properties.

By utilizing PBPK modeling, receptor occupancy biomarkers, and correcting for species-specific binding kinetics, researchers can translate dose-response curves from animal models into accurate predictions of human clinical efficacy, reducing the attrition rate in psychiatric drug development.

## 8. Detailed Breakdown of Key Drug Classes and Translational Profiles

### 8.1 Clozapine: The Multi-Target Prototype
Clozapine remains the gold standard for treatment-resistant schizophrenia but is difficult to model.
*   **Profile:** Low D2 affinity, high 5-HT2A, 5-HT2C, 5-HT1A, $\alpha_1$, $\alpha_2$, H1, and M1 affinity [cite: 12].
*   **Occupancy:** Uniquely, clozapine is effective at D2 occupancy levels as low as 40–60%, far below the 65% threshold required for other drugs [cite: 10]. This is attributed to its fast dissociation kinetics and heavy contribution from non-D2 mechanisms (e.g., D4, 5-HT2A).
*   **Prediction Challenge:** Because clozapine relies on a "rich" receptor profile, animal models that focus solely on D2-mediated behaviors (like catalepsy) fail to predict its efficacy. It requires models of cognitive function and negative symptoms [cite: 22].

### 8.2 Risperidone: The High-Affinity Antagonist
*   **Profile:** Very high affinity for D2 and 5-HT2A.
*   **Translation:** Risperidone fits the standard model well. It is effective when D2 occupancy reaches 65% and causes EPS above 80%. Its high 5-HT2A affinity (ratio ~20) widens the therapeutic window compared to haloperidol [cite: 14, 15].
*   **Metabolites:** Translational models must account for its active metabolite, 9-hydroxy-risperidone (paliperidone), which has a similar pharmacological profile [cite: 5].

### 8.3 Partial Agonists (Aripiprazole, Cariprazine, Brexpiprazole)
*   **Mechanism:** These drugs act as partial agonists at D2 receptors, stimulating the receptor at low tone and blocking it at high tone.
*   **Occupancy:** They require much higher occupancy (>90%) to achieve efficacy because they do not fully silence the receptor. The "threshold" concept is different here; efficacy is driven by *intrinsic activity* rather than just blockade [cite: 25, 38].
*   **Affinity Balancing:** Cariprazine has a unique D3 > D2 affinity profile. Predicting its efficacy required models sensitive to D3 function (e.g., motivation/reward tasks) rather than just hyperlocomotion [cite: 18].

## 9. References
*   **[cite: 5]** *Translational PK/PD modeling of multi-target antipsychotics...*
*   **[cite: 7]** *Animal models are crucial for understanding the mechanism...*
*   **[cite: 1]** *Polypharmacology is nowadays considered an increasingly crucial aspect...*
*   **[cite: 8]** *D2 and 5-HT2 Receptor Effects of Antipsychotics...*
*   **[cite: 26]** *Species differences in 5-HT2A expression and function...*
*   **[cite: 15]** *Clinical pharmacology of atypical antipsychotics: An update...*
*   **[cite: 10]** *Mechanism of Action of Classical Antipsychotic Drugs...*
*   **[cite: 28]** *Examples of successful applications of target occupancy studies...*
*   (And all other cited sources in the text).

**Sources:**
1. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFaXezti0CL-aCbJ3BLUn7ECWDCKoHOM2lXtErfGemJw2c5u22BrN8boIwp_tWVYvRgPwUmSS7khU7e7WuRwBcJoscGfUDl5Ds9PPw0sY52MtCYFMDfGydSNAf2qBpB1VeW-uQLV-A2)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrlBF3IiRVcPk-DdgPuhUo95Xz_ZxX2hOGmtVVbbvZXFOLB0S0DLuDy3YOM9ZKDcFsIUc7S_-tydqXXUqf5UKEk24IfV7IZ5oJOkpqgVjZEWh0SfgD1nTtP8-qdhvE03MUua9TaT-t8Lh8vGICNCSowupi5wBnxv2hxyAk5Q97kZjFAXaL2HDllT9dbtPUtlXESPTV0ZkonccDXWL_kEudbL3r6Iv0iA==)
3. [escholarship.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG646dNrhsc3_nUAxPsNsB9kIVzA3PpBGJHgxy-vKF9cTQmd-0fWPAmOXi5wO2HvN8p_G4hdbrdFjhOMGUdNt2GTKt_gOaY3C_tse9p9c93g7Y5BnB6HED6aL5MBnFYSw==)
4. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfIE_YB902471AgjUjMCy0asYk-GT3Uy64yN6vW_JMmh4p7tYjS9bG3z-9E-txFqKc_P4uuPAcsvapO0wRKOQyPa84nlKRGRKXSlOtdK2C0-KdlZyt4LISkJxDFuQI5tlaiXzUDULGPg==)
5. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2WrnPBsxVgUdYmUSLnns2bGQvhcGk0LkFUK3-Wibx90t-zAQgkdPcIaCCBOxeG-SCGWjUsCfEcj1XUetSax7p2JYx6vIyp8DVfEnu7aIKWuVub8Gf2T220RiZSAf5Uw==)
6. [rug.nl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6umsgV51ljhPNpDNZBUbO0KaAc_unhAbC_2RmcSqkGECovJt7465_hSm3m3U7FFjMa4d1nF3_D86-hMpwsDF-qRjXpHE-OJRJyhg2KyMLWmW-4_W7Ft76mpuoiEGY7YSWXSqllGQt4nEHU4EaO3Gmcnr63TUMAqjkmlKMYHgSWK8RdYnaHtEiO5Ghf85sw3HJ68wDCUSr15mzMH0SIqfEWQo=)
7. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgBAWdDPqL0KXkbRieMod_-sampSq5p-IMt8UgeQcPs1nnprwgiegdZ0RVSeoJ500hqVeMorNxAyNA3lBLMhhSsUgLb-8mczE1SMSxasmqh3MuebOR2akBmR0RCiXSpQ==)
8. [psychiatrist.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrzJ7EhprUVV3lSuMhxevd6STlaOoifsc-wHchmnCZLXQJdXHOqrM0X-Bj7_XOEIFjctv_Y3lr4CPjShulh3B0EQWstfiK5_kRFS-_tCbtsVP0PnM-5yJTTT9Ckp0LkYAvZn4Ok5VrQ4uiCjsw_RpKpRyGifEqg4t9RTVNyBlK2l1Ckv1au4mrrhTa240cJCx430UVmB_Z0vtFW3kmVYYUMYQjF0-VyNOdFtnwqp4cj_n6sKrpjFJ8_vNK)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAiecz0lhsU2KjSe61x8F2O5wcUQK-tdxlahNQA7UVFgV84ZvPxk8FBzkVzkxjEaSjH8NsbsajdWR4O-WUUdRqqO4RLjUFW0_TlGfUERHwgF9jCz2PC5UdugeerAk697sUlZXqZUNi)
10. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTn9zsPRHHou4QXPNuNkwzvbF3PTpe-Kn9ucsIHlZPR7FLzqNwKyvgpCnyMg-_16lC0ODekUF4ZTJoZ9nmmpFOj71_Xc4fe_1kUc3BEjTBNLywkGamS4iOtPAn_bedG5GxZmQsZDnY)
11. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEu3j_D8-I3RLnWGmuO9WqD2ui6JalbRwJ8so0Uj-gb87TX6xJtYfGiWBOlPXegT5f19vlt-1jkti9w0JqLoh-Jsi-EKhX3xNQCBHP8Q_Cn4nehsUeC4wXEXvmqBCWYYAPdIXNGQHxe)
12. [qmul.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbeTbSZ1klQkazsk6r_SA4sZwVdwEIY1qeQ9GIHPy9nBx2b_cU4VCpIguUJ8vwfX3L55AGCXoigvXg3hAcgMr6X0Kcab6dZM3M_hf5FADVbbbi_98kYW-DF_yyewAUKyfSQ-dEC1CQOhv9yiCcZqsKNgBgXwS2ihwnF7fYcuF3vDVdSJIVkfsWNhNJeDXNHeII1em4wa5flGixx7Uh62S_iRz67JzLr0zIkxXktfY2m-4fKK_-KGEYWMjdahxEyCDqFwlAp1eiHj48upy_W-TNoY18xXanZew=)
13. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETrCQDlV2r1bhgSdWGCosHLrrPxnIIBW9LOreUXXZ74ojzRm-iyrRxF7AyzwbL8pRcsdNMDWW6ocLy9vFb149LSDiT0XfofuxELK2u-GhXokK8XRnY_Ecm5hnXhSJdvaryf7rCS7smNjl70d9IpWV--jduWMo-jbvQHdinq7dA7jQ8hQ4=)
14. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExaNb1DRpUB-8wlNzGA3fUTot6O8r1gv_41DxE0-lhJntBGdGxjdTZhj3yelbt05DFEmbrfsD9qroH7yq1ZszKiQj6tPTqh9z91RDr2SPIwo-JF1SVkmEhPu9DTRjixw==)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN3h8NVPAHAxqq9UxRWdtE2mmmnpV5Hy7I6TeoLc45vCW5KhlmeiIqRcTpuqqQHkXRp56XevPauE4Cetpoidrcr5Gp0rPnwo9mIlBvmIqU68_BI8h7pHh2pVmxQokBd6PSM83rRGUHIvAwdyEov568WdUgVVjVks6fENd4otWiUInKCdKSQi-jK3CW89JRKXNxJ82KmxSQK_Rl2ArcHRdRYFyR)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbHMP7gRpPhi7NeRqflO4TQLdG5p6Ct8jwbZhrur05e9ATT5gjnN8jcxsDFmuu5M-is91lQ5whF4dNuzDC49PeLRqMiAMlsP6Oxe0hFM8Iw31SOnBsQ2Y6rvjCefFGLA661yUeNAUkuwc0igLkm2g-bmu9gYiqdbmeXrvoPxlDqnR5Fp2pac1GPI4pt6mnp1H4jGtex6Mfqs9pBbBSYqfolZ-V07OFmQ6B6lLrQYJR16KYiXWYLsBeq976QR1Soohg1Vv1_bU=)
17. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFv5gsq1-TD395vueCEw-S8dyELWODkMt8lZEMjqNHkKJFXpv_e7lnsfXheIOLRc9De62tq_uwiXQSQI1Y1iutHoL2wBqFktx6NOBAgsfR-gf0LzK-RMxeWlOfviKM=)
18. [preprints.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFK1ErIrSdyyliEex8q9OulAY45GSbosfi056xKFFUKhWyydFBa1w8p1J-mPxbFEojJKLu9or_uoghb58yybEtp_E42yX0mWui5igpp8Wfd3tvhZyZjaGRHL_3sPPQGjlIycX2VxtCy5XYxa5P7J7HFvKg=)
19. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPBIbzM8eV9t2hE3OdXeNvoAwxuU4Ewlodh1aT-OlApxHLuJ3-2jfGbO5PfQ8L1DyP5L25_9kU85nDgzxTWXIr_1la3oiKfmfGd2EOUzDOLZEL2BKihOljNdTGLV_x5QFQny3Rd9eW)
20. [dokumen.pub](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEE5rTcITSghgFoTZoHDzge64biV8xLHyR8XWQ7N9KyzOLDJDyDQAhVDyghbEQrH8o_Q9FtWc6qMWjM0uKKFlNOpQV37VU09XyDuSaMJTZDcS6Mzz3KiQsaZW2C0jm3RukrwUrdy051tZEy-VTYg-s0zcH06sNmK5GrSQibsZOEihcaAvMits5uX1rtkFo8Pw72XbAVHdXrxC61E1ryMpNWBdfb2g==)
21. [metris.nl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhpu0Y0Uw_3s1NPPMURazMLzVG0qawyA8pYMrF6FE0gb2-csP_zOWK7NXn_azH929efr8MfnDcc1_R_tgO5KaYNMPfDviu2BW22eInqumz1NI4fBqlHtD-V3GTT6-QmBIKzLbIRQkg0KeLy3itutBpCeJgu41nNoC8SUZzpDTdxMGD2cOTAfdbS4HWnrbHD6W_w8-6T6qTGrPdrkxpjlw-qJHRqOSZ3j3xqx2GNK_XgnI8024W8dpZfhGkVaR74qndfo7747eTCsTo39lkcrMGCVVHXRqqGR2GYD3YNbe7ezIcrwKX)
22. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFItsS15hlmjg7YDTgFcu4Iab2hAf1GeWc85nUUQNsLtzhSCVlBxV8MwX4YFU2f_PEHzf7XvJEA6RPESzG8dM7HNCyae2fQhk0hcffmdHMoqKb5uGMI0KONgm4Un7mHexqpZRz0y4Lg3pt2KiKUj3Zxpo36QHC6J9uayrucVcR0Tx0xfP9N8Zf5KfpJ3W_WtonbyyzAN1hLTercGUIgGe2MhDbYh7l3YqFBQEcCJWB6vZmVYjnIWa6jTtu3ULjx3zoUcOhyYiU8ReLcVyknvlMcOsL5moAs42f4qMSlKFLwYdVhAGLf00jSAj7Jv25aqbFAuVtubSKZj7nh1ftMOAwpK9NnpkP0ac9XrP6byinq5vx48yMTd3XuXwor)
23. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4z6tELZ4tQFJ-s6pF0JberZtZIC8ctfLqFRmc7MfurZifRdrdP9bVIlDLi1eW2hvbgGVx2z3csPOia5JlPmAgdqsqK3udckcoSykkH8oFOInUALjFdtBWFR95_YaEBnUKflJ3smgM)
24. [scielo.br](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuGzeGNdpAvBR_-AA_rIXkKSvBqShiBenmFq-1wUSNR7nf0g_rrOwFi3kaFTSdy3yWURI9vkDS4mci2N242O4HllzYsT2AAgM1GDNmr-KqAbFGAWbBsiWCBLD2Uj0l0QGrV51M2vvurmeYcDmMJ6b_J4L2Sg==)
25. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsEGJDZx2GYXMR5OnNq80YdilxPRZSrcDJdKQTgyTMmnQwB7hxMnKAzn6SrOolSMZEnZWbbn6qlwfgUGaTIhFepiejYBTrzXoM1SiT3MuhndJb9w4Ar7Y6b2HzazhmHNE=)
26. [reprocell.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQET33kegcQJW9GZefJi6GR3W4__5xZlBNWwaakfRmOyfobSJXRKTnbTN6W8xcmz4EiPFg0P9UBkbY4t5NbkO-y8h1PT0e4HrYXNCL18oonaYYVf_TPYqdoC3HFMQVfIMHbCTNcjOalS5vNIQ30Vud6KyqbtCA==)
27. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDhbNJvo3PTS5WwcuRox37gy6MY4XLELii2nRpvCO8lUzkd84ycm74gLPjNJgaaBsVsPGIzybybr0NEoRZ7d22lXjabR3j38qbRKh7KmNpsPQeIeXV8e7BHO6Q96FC2MFu3FQLou_g)
28. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmda9SJB5coKuyf_z7mccJR02VlWi6gLI5nBft7saWannqZ_ZQdTt_rEvOrhxrfCROdq-2X7WGURZDpZjJIpJ4VUJakhO-GdLRbWT77p7pPvyYLsGQFPnP020PsN3KjzeQ16cPcHzH)
29. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2DYuAxaVyT3Yc1MUHkuJPyOr2xvhCvNtTjf5EFK7_Bxny8sXfxt5PEu_PLWRqBt36rELvgDjH7OdCwFjIEOWUdGcADoVTvdmF8s9_EnAsrZ8g8oA2KI4z736pKJ89nSBW)
30. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZyMAou8QxJXu0UDsromu_ye1xHJPfeh1TQtu_UydQw2xe3BLXbtmXTTh_UiLLdbqAaHvknN-d8IJbmirQzArxYbTmGV7OEQWUAdpNYAZ4y6Q4Y7f1elKrnhD_ENVwqqY-N6x1lKEs4CXmVxCNsgDSZemrZdlMMf_4SU7gRjCB9p87Glct5b_1_rZ5TPjddgmwnAyDiAlGRbdsS_4h5J8bKGo-3ewE0A0M5re-)
31. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8HRaozquTRYpQodb3vbq1EWdYhvvzl4TVxB7paGD6ambP8bFxw-gmceUxZ5LBGVQvlgB4e5z-fb6Fmc7nP8SDdUIh-Ate8agG-DQGLHHJQKxfShFs50VyTSeIxil0Rgo1saIAF-Rz)
32. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVFolCggLq7igB2GEXCHT8sndMqRgEeWk4xm0CKi05IFh9KyIBE67IXZa2__QGRG9MKOHvRjM40l0djZlOKpSOFU6oAzenyJCQENQknA9qYrXyuHZNwwsO-HoFJ1jV3TLv0PVYGmtJQzSVVQ==)
33. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpbbn25pbJV390SPrFIxLysFPudzmniRFzlp7Qj5xytUqQRlwDRSvu0sR3mG6VbHlTT6roSXfRMe_v2J2zCKmP8PQce9OtfFZDM1213J5g_SsYDQ3ttBH7jxPYdgIbMQ==)
34. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEO3y0joFk-YtXYR5gUN78IfLSLoGBYFLcBb_ryq8YjwzomhnU5qn9Pc2oNG2msBTTzISvTOY8Xv9LED09rF8DuX4IXPQ5Q2Z9GjyslwPt4jW6X8YGbqxJl8UJfh2BAgw9laVmG3o84dyf8ASWcMb8mxNmUMaT6UAo28FDDDGFQdDK2-zaC3_qUZifhl2GlsGYR-93_3gec0Ku7TpxJztNMzD4-_lyBMmA2CZ9PCy4b2E2cFO3iyp0tCalXOeYwKiqGqXeE-3rvRlfyqvxf8xmjTAzTcCQc)
35. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRQgzE_BvRGY4BLozH8AZLFoiVvlvVZX6XJ38oeNqDKMgm9iXMcO0jUpKaUy5olbdqUufezBg1Y2Auv9vv_M9qI_YsHHtEAlGckshWz8LCJwAcb9OXIX9OKPKe9YZSsfHNTy4iqTVzadElR7hP1sD49ntPzQ10ikdqm07gNDiY3KKaIv_PmzzOiXJEyPPhBchojgQkV-zW5NSIPEe5m95sGVnppWZZNUJdmZMK3kt4z7HcBxNNflveDO3J0bFmDVqoKQi_xKCx9zH0Zs6YnD7iQDnYE7hHFQ==)
36. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSjNvag7EH8LZZ1LPSVchVwyK6_w-FaDPx7KtcCv3QwmNQsf3B-UOsh2ER5wpzrlkKDMmMXwhYXSg81QZ6Zh7291I6z73CbALcs5k2yA3lGmWaPszfwQz02I820IzhVSdyaWP5h55C)
37. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKAWM2cKCEru-Iu19-y-pKYHWq3Yae47qRFHndqd05QaxTiPT0sDzmJA5v8FTCNv7Op_gpSCnPy3ivj9tZBIO71vSUPItWoawv5qWgwefZguHVEjmTRXJZ5WhvJZ96rHMu_ADktTnt)
38. [unimi.it](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhgKxSIpijS1ppDcV5o4-SVHrvtsicZIhaGi45g0PP9gSOIQTk_VyqUbNSQ82LTrCxBreppO04Yo_Y-2ML7vAKf-yJRTcVjG2LpTbfGQLcjDp9q2AI5XbrJg5LaQhmbBFpihYKoTD0SFf63bk9iQYOj7W8pz5eyJlSo8LHD40oH4JZQlf6tSCbpb8dtNgh1lM--vdxzDruTeOKsACUIwElVX4M4A==)


## Annotations
Annotation(end_index=2083, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFaXezti0CL-aCbJ3BLUn7ECWDCKoHOM2lXtErfGemJw2c5u22BrN8boIwp_tWVYvRgPwUmSS7khU7e7WuRwBcJoscGfUDl5Ds9PPw0sY52MtCYFMDfGydSNAf2qBpB1VeW-uQLV-A2', start_index=2071)
Annotation(end_index=2083, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrlBF3IiRVcPk-DdgPuhUo95Xz_ZxX2hOGmtVVbbvZXFOLB0S0DLuDy3YOM9ZKDcFsIUc7S_-tydqXXUqf5UKEk24IfV7IZ5oJOkpqgVjZEWh0SfgD1nTtP8-qdhvE03MUua9TaT-t8Lh8vGICNCSowupi5wBnxv2hxyAk5Q97kZjFAXaL2HDllT9dbtPUtlXESPTV0ZkonccDXWL_kEudbL3r6Iv0iA==', start_index=2071)
Annotation(end_index=2304, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrlBF3IiRVcPk-DdgPuhUo95Xz_ZxX2hOGmtVVbbvZXFOLB0S0DLuDy3YOM9ZKDcFsIUc7S_-tydqXXUqf5UKEk24IfV7IZ5oJOkpqgVjZEWh0SfgD1nTtP8-qdhvE03MUua9TaT-t8Lh8vGICNCSowupi5wBnxv2hxyAk5Q97kZjFAXaL2HDllT9dbtPUtlXESPTV0ZkonccDXWL_kEudbL3r6Iv0iA==', start_index=2295)
Annotation(end_index=2833, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG646dNrhsc3_nUAxPsNsB9kIVzA3PpBGJHgxy-vKF9cTQmd-0fWPAmOXi5wO2HvN8p_G4hdbrdFjhOMGUdNt2GTKt_gOaY3C_tse9p9c93g7Y5BnB6HED6aL5MBnFYSw==', start_index=2821)
Annotation(end_index=2833, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfIE_YB902471AgjUjMCy0asYk-GT3Uy64yN6vW_JMmh4p7tYjS9bG3z-9E-txFqKc_P4uuPAcsvapO0wRKOQyPa84nlKRGRKXSlOtdK2C0-KdlZyt4LISkJxDFuQI5tlaiXzUDULGPg==', start_index=2821)
Annotation(end_index=3340, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2WrnPBsxVgUdYmUSLnns2bGQvhcGk0LkFUK3-Wibx90t-zAQgkdPcIaCCBOxeG-SCGWjUsCfEcj1XUetSax7p2JYx6vIyp8DVfEnu7aIKWuVub8Gf2T220RiZSAf5Uw==', start_index=3328)
Annotation(end_index=3340, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6umsgV51ljhPNpDNZBUbO0KaAc_unhAbC_2RmcSqkGECovJt7465_hSm3m3U7FFjMa4d1nF3_D86-hMpwsDF-qRjXpHE-OJRJyhg2KyMLWmW-4_W7Ft76mpuoiEGY7YSWXSqllGQt4nEHU4EaO3Gmcnr63TUMAqjkmlKMYHgSWK8RdYnaHtEiO5Ghf85sw3HJ68wDCUSr15mzMH0SIqfEWQo=', start_index=3328)
Annotation(end_index=4265, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAiecz0lhsU2KjSe61x8F2O5wcUQK-tdxlahNQA7UVFgV84ZvPxk8FBzkVzkxjEaSjH8NsbsajdWR4O-WUUdRqqO4RLjUFW0_TlGfUERHwgF9jCz2PC5UdugeerAk697sUlZXqZUNi', start_index=4246)
Annotation(end_index=4265, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTn9zsPRHHou4QXPNuNkwzvbF3PTpe-Kn9ucsIHlZPR7FLzqNwKyvgpCnyMg-_16lC0ODekUF4ZTJoZ9nmmpFOj71_Xc4fe_1kUc3BEjTBNLywkGamS4iOtPAn_bedG5GxZmQsZDnY', start_index=4246)
Annotation(end_index=4265, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgBAWdDPqL0KXkbRieMod_-sampSq5p-IMt8UgeQcPs1nnprwgiegdZ0RVSeoJ500hqVeMorNxAyNA3lBLMhhSsUgLb-8mczE1SMSxasmqh3MuebOR2akBmR0RCiXSpQ==', start_index=4246)
Annotation(end_index=4265, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrzJ7EhprUVV3lSuMhxevd6STlaOoifsc-wHchmnCZLXQJdXHOqrM0X-Bj7_XOEIFjctv_Y3lr4CPjShulh3B0EQWstfiK5_kRFS-_tCbtsVP0PnM-5yJTTT9Ckp0LkYAvZn4Ok5VrQ4uiCjsw_RpKpRyGifEqg4t9RTVNyBlK2l1Ckv1au4mrrhTa240cJCx430UVmB_Z0vtFW3kmVYYUMYQjF0-VyNOdFtnwqp4cj_n6sKrpjFJ8_vNK', start_index=4246)
Annotation(end_index=4454, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAiecz0lhsU2KjSe61x8F2O5wcUQK-tdxlahNQA7UVFgV84ZvPxk8FBzkVzkxjEaSjH8NsbsajdWR4O-WUUdRqqO4RLjUFW0_TlGfUERHwgF9jCz2PC5UdugeerAk697sUlZXqZUNi', start_index=4439)
Annotation(end_index=4454, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgBAWdDPqL0KXkbRieMod_-sampSq5p-IMt8UgeQcPs1nnprwgiegdZ0RVSeoJ500hqVeMorNxAyNA3lBLMhhSsUgLb-8mczE1SMSxasmqh3MuebOR2akBmR0RCiXSpQ==', start_index=4439)
Annotation(end_index=4454, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrzJ7EhprUVV3lSuMhxevd6STlaOoifsc-wHchmnCZLXQJdXHOqrM0X-Bj7_XOEIFjctv_Y3lr4CPjShulh3B0EQWstfiK5_kRFS-_tCbtsVP0PnM-5yJTTT9Ckp0LkYAvZn4Ok5VrQ4uiCjsw_RpKpRyGifEqg4t9RTVNyBlK2l1Ckv1au4mrrhTa240cJCx430UVmB_Z0vtFW3kmVYYUMYQjF0-VyNOdFtnwqp4cj_n6sKrpjFJ8_vNK', start_index=4439)
Annotation(end_index=4581, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTn9zsPRHHou4QXPNuNkwzvbF3PTpe-Kn9ucsIHlZPR7FLzqNwKyvgpCnyMg-_16lC0ODekUF4ZTJoZ9nmmpFOj71_Xc4fe_1kUc3BEjTBNLywkGamS4iOtPAn_bedG5GxZmQsZDnY', start_index=4568)
Annotation(end_index=4581, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrzJ7EhprUVV3lSuMhxevd6STlaOoifsc-wHchmnCZLXQJdXHOqrM0X-Bj7_XOEIFjctv_Y3lr4CPjShulh3B0EQWstfiK5_kRFS-_tCbtsVP0PnM-5yJTTT9Ckp0LkYAvZn4Ok5VrQ4uiCjsw_RpKpRyGifEqg4t9RTVNyBlK2l1Ckv1au4mrrhTa240cJCx430UVmB_Z0vtFW3kmVYYUMYQjF0-VyNOdFtnwqp4cj_n6sKrpjFJ8_vNK', start_index=4568)
Annotation(end_index=4732, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTn9zsPRHHou4QXPNuNkwzvbF3PTpe-Kn9ucsIHlZPR7FLzqNwKyvgpCnyMg-_16lC0ODekUF4ZTJoZ9nmmpFOj71_Xc4fe_1kUc3BEjTBNLywkGamS4iOtPAn_bedG5GxZmQsZDnY', start_index=4722)
Annotation(end_index=5298, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbeTbSZ1klQkazsk6r_SA4sZwVdwEIY1qeQ9GIHPy9nBx2b_cU4VCpIguUJ8vwfX3L55AGCXoigvXg3hAcgMr6X0Kcab6dZM3M_hf5FADVbbbi_98kYW-DF_yyewAUKyfSQ-dEC1CQOhv9yiCcZqsKNgBgXwS2ihwnF7fYcuF3vDVdSJIVkfsWNhNJeDXNHeII1em4wa5flGixx7Uh62S_iRz67JzLr0zIkxXktfY2m-4fKK_-KGEYWMjdahxEyCDqFwlAp1eiHj48upy_W-TNoY18xXanZew=', start_index=5284)
Annotation(end_index=5298, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEu3j_D8-I3RLnWGmuO9WqD2ui6JalbRwJ8so0Uj-gb87TX6xJtYfGiWBOlPXegT5f19vlt-1jkti9w0JqLoh-Jsi-EKhX3xNQCBHP8Q_Cn4nehsUeC4wXEXvmqBCWYYAPdIXNGQHxe', start_index=5284)
Annotation(end_index=5469, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETrCQDlV2r1bhgSdWGCosHLrrPxnIIBW9LOreUXXZ74ojzRm-iyrRxF7AyzwbL8pRcsdNMDWW6ocLy9vFb149LSDiT0XfofuxELK2u-GhXokK8XRnY_Ecm5hnXhSJdvaryf7rCS7smNjl70d9IpWV--jduWMo-jbvQHdinq7dA7jQ8hQ4=', start_index=5455)
Annotation(end_index=5469, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbeTbSZ1klQkazsk6r_SA4sZwVdwEIY1qeQ9GIHPy9nBx2b_cU4VCpIguUJ8vwfX3L55AGCXoigvXg3hAcgMr6X0Kcab6dZM3M_hf5FADVbbbi_98kYW-DF_yyewAUKyfSQ-dEC1CQOhv9yiCcZqsKNgBgXwS2ihwnF7fYcuF3vDVdSJIVkfsWNhNJeDXNHeII1em4wa5flGixx7Uh62S_iRz67JzLr0zIkxXktfY2m-4fKK_-KGEYWMjdahxEyCDqFwlAp1eiHj48upy_W-TNoY18xXanZew=', start_index=5455)
Annotation(end_index=5640, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExaNb1DRpUB-8wlNzGA3fUTot6O8r1gv_41DxE0-lhJntBGdGxjdTZhj3yelbt05DFEmbrfsD9qroH7yq1ZszKiQj6tPTqh9z91RDr2SPIwo-JF1SVkmEhPu9DTRjixw==', start_index=5626)
Annotation(end_index=5640, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN3h8NVPAHAxqq9UxRWdtE2mmmnpV5Hy7I6TeoLc45vCW5KhlmeiIqRcTpuqqQHkXRp56XevPauE4Cetpoidrcr5Gp0rPnwo9mIlBvmIqU68_BI8h7pHh2pVmxQokBd6PSM83rRGUHIvAwdyEov568WdUgVVjVks6fENd4otWiUInKCdKSQi-jK3CW89JRKXNxJ82KmxSQK_Rl2ArcHRdRYFyR', start_index=5626)
Annotation(end_index=5948, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN3h8NVPAHAxqq9UxRWdtE2mmmnpV5Hy7I6TeoLc45vCW5KhlmeiIqRcTpuqqQHkXRp56XevPauE4Cetpoidrcr5Gp0rPnwo9mIlBvmIqU68_BI8h7pHh2pVmxQokBd6PSM83rRGUHIvAwdyEov568WdUgVVjVks6fENd4otWiUInKCdKSQi-jK3CW89JRKXNxJ82KmxSQK_Rl2ArcHRdRYFyR', start_index=5938)
Annotation(end_index=6121, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFv5gsq1-TD395vueCEw-S8dyELWODkMt8lZEMjqNHkKJFXpv_e7lnsfXheIOLRc9De62tq_uwiXQSQI1Y1iutHoL2wBqFktx6NOBAgsfR-gf0LzK-RMxeWlOfviKM=', start_index=6107)
Annotation(end_index=6121, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbHMP7gRpPhi7NeRqflO4TQLdG5p6Ct8jwbZhrur05e9ATT5gjnN8jcxsDFmuu5M-is91lQ5whF4dNuzDC49PeLRqMiAMlsP6Oxe0hFM8Iw31SOnBsQ2Y6rvjCefFGLA661yUeNAUkuwc0igLkm2g-bmu9gYiqdbmeXrvoPxlDqnR5Fp2pac1GPI4pt6mnp1H4jGtex6Mfqs9pBbBSYqfolZ-V07OFmQ6B6lLrQYJR16KYiXWYLsBeq976QR1Soohg1Vv1_bU=', start_index=6107)
Annotation(end_index=6402, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETrCQDlV2r1bhgSdWGCosHLrrPxnIIBW9LOreUXXZ74ojzRm-iyrRxF7AyzwbL8pRcsdNMDWW6ocLy9vFb149LSDiT0XfofuxELK2u-GhXokK8XRnY_Ecm5hnXhSJdvaryf7rCS7smNjl70d9IpWV--jduWMo-jbvQHdinq7dA7jQ8hQ4=', start_index=6388)
Annotation(end_index=6402, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbeTbSZ1klQkazsk6r_SA4sZwVdwEIY1qeQ9GIHPy9nBx2b_cU4VCpIguUJ8vwfX3L55AGCXoigvXg3hAcgMr6X0Kcab6dZM3M_hf5FADVbbbi_98kYW-DF_yyewAUKyfSQ-dEC1CQOhv9yiCcZqsKNgBgXwS2ihwnF7fYcuF3vDVdSJIVkfsWNhNJeDXNHeII1em4wa5flGixx7Uh62S_iRz67JzLr0zIkxXktfY2m-4fKK_-KGEYWMjdahxEyCDqFwlAp1eiHj48upy_W-TNoY18xXanZew=', start_index=6388)
Annotation(end_index=6503, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExaNb1DRpUB-8wlNzGA3fUTot6O8r1gv_41DxE0-lhJntBGdGxjdTZhj3yelbt05DFEmbrfsD9qroH7yq1ZszKiQj6tPTqh9z91RDr2SPIwo-JF1SVkmEhPu9DTRjixw==', start_index=6493)
Annotation(end_index=6644, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFK1ErIrSdyyliEex8q9OulAY45GSbosfi056xKFFUKhWyydFBa1w8p1J-mPxbFEojJKLu9or_uoghb58yybEtp_E42yX0mWui5igpp8Wfd3tvhZyZjaGRHL_3sPPQGjlIycX2VxtCy5XYxa5P7J7HFvKg=', start_index=6634)
Annotation(end_index=6784, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPBIbzM8eV9t2hE3OdXeNvoAwxuU4Ewlodh1aT-OlApxHLuJ3-2jfGbO5PfQ8L1DyP5L25_9kU85nDgzxTWXIr_1la3oiKfmfGd2EOUzDOLZEL2BKihOljNdTGLV_x5QFQny3Rd9eW', start_index=6770)
Annotation(end_index=6784, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEu3j_D8-I3RLnWGmuO9WqD2ui6JalbRwJ8so0Uj-gb87TX6xJtYfGiWBOlPXegT5f19vlt-1jkti9w0JqLoh-Jsi-EKhX3xNQCBHP8Q_Cn4nehsUeC4wXEXvmqBCWYYAPdIXNGQHxe', start_index=6770)
Annotation(end_index=6866, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExaNb1DRpUB-8wlNzGA3fUTot6O8r1gv_41DxE0-lhJntBGdGxjdTZhj3yelbt05DFEmbrfsD9qroH7yq1ZszKiQj6tPTqh9z91RDr2SPIwo-JF1SVkmEhPu9DTRjixw==', start_index=6856)
Annotation(end_index=7230, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEE5rTcITSghgFoTZoHDzge64biV8xLHyR8XWQ7N9KyzOLDJDyDQAhVDyghbEQrH8o_Q9FtWc6qMWjM0uKKFlNOpQV37VU09XyDuSaMJTZDcS6Mzz3KiQsaZW2C0jm3RukrwUrdy051tZEy-VTYg-s0zcH06sNmK5GrSQibsZOEihcaAvMits5uX1rtkFo8Pw72XbAVHdXrxC61E1ryMpNWBdfb2g==', start_index=7217)
Annotation(end_index=7230, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFaXezti0CL-aCbJ3BLUn7ECWDCKoHOM2lXtErfGemJw2c5u22BrN8boIwp_tWVYvRgPwUmSS7khU7e7WuRwBcJoscGfUDl5Ds9PPw0sY52MtCYFMDfGydSNAf2qBpB1VeW-uQLV-A2', start_index=7217)
Annotation(end_index=7883, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFItsS15hlmjg7YDTgFcu4Iab2hAf1GeWc85nUUQNsLtzhSCVlBxV8MwX4YFU2f_PEHzf7XvJEA6RPESzG8dM7HNCyae2fQhk0hcffmdHMoqKb5uGMI0KONgm4Un7mHexqpZRz0y4Lg3pt2KiKUj3Zxpo36QHC6J9uayrucVcR0Tx0xfP9N8Zf5KfpJ3W_WtonbyyzAN1hLTercGUIgGe2MhDbYh7l3YqFBQEcCJWB6vZmVYjnIWa6jTtu3ULjx3zoUcOhyYiU8ReLcVyknvlMcOsL5moAs42f4qMSlKFLwYdVhAGLf00jSAj7Jv25aqbFAuVtubSKZj7nh1ftMOAwpK9NnpkP0ac9XrP6byinq5vx48yMTd3XuXwor', start_index=7869)
Annotation(end_index=7883, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhpu0Y0Uw_3s1NPPMURazMLzVG0qawyA8pYMrF6FE0gb2-csP_zOWK7NXn_azH929efr8MfnDcc1_R_tgO5KaYNMPfDviu2BW22eInqumz1NI4fBqlHtD-V3GTT6-QmBIKzLbIRQkg0KeLy3itutBpCeJgu41nNoC8SUZzpDTdxMGD2cOTAfdbS4HWnrbHD6W_w8-6T6qTGrPdrkxpjlw-qJHRqOSZ3j3xqx2GNK_XgnI8024W8dpZfhGkVaR74qndfo7747eTCsTo39lkcrMGCVVHXRqqGR2GYD3YNbe7ezIcrwKX', start_index=7869)
Annotation(end_index=8109, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgBAWdDPqL0KXkbRieMod_-sampSq5p-IMt8UgeQcPs1nnprwgiegdZ0RVSeoJ500hqVeMorNxAyNA3lBLMhhSsUgLb-8mczE1SMSxasmqh3MuebOR2akBmR0RCiXSpQ==', start_index=8100)
Annotation(end_index=8358, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4z6tELZ4tQFJ-s6pF0JberZtZIC8ctfLqFRmc7MfurZifRdrdP9bVIlDLi1eW2hvbgGVx2z3csPOia5JlPmAgdqsqK3udckcoSykkH8oFOInUALjFdtBWFR95_YaEBnUKflJ3smgM', start_index=8348)
Annotation(end_index=8616, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgBAWdDPqL0KXkbRieMod_-sampSq5p-IMt8UgeQcPs1nnprwgiegdZ0RVSeoJ500hqVeMorNxAyNA3lBLMhhSsUgLb-8mczE1SMSxasmqh3MuebOR2akBmR0RCiXSpQ==', start_index=8603)
Annotation(end_index=8616, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuGzeGNdpAvBR_-AA_rIXkKSvBqShiBenmFq-1wUSNR7nf0g_rrOwFi3kaFTSdy3yWURI9vkDS4mci2N242O4HllzYsT2AAgM1GDNmr-KqAbFGAWbBsiWCBLD2Uj0l0QGrV51M2vvurmeYcDmMJ6b_J4L2Sg==', start_index=8603)
Annotation(end_index=9022, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4z6tELZ4tQFJ-s6pF0JberZtZIC8ctfLqFRmc7MfurZifRdrdP9bVIlDLi1eW2hvbgGVx2z3csPOia5JlPmAgdqsqK3udckcoSykkH8oFOInUALjFdtBWFR95_YaEBnUKflJ3smgM', start_index=9012)
Annotation(end_index=9173, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsEGJDZx2GYXMR5OnNq80YdilxPRZSrcDJdKQTgyTMmnQwB7hxMnKAzn6SrOolSMZEnZWbbn6qlwfgUGaTIhFepiejYBTrzXoM1SiT3MuhndJb9w4Ar7Y6b2HzazhmHNE=', start_index=9159)
Annotation(end_index=9173, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhpu0Y0Uw_3s1NPPMURazMLzVG0qawyA8pYMrF6FE0gb2-csP_zOWK7NXn_azH929efr8MfnDcc1_R_tgO5KaYNMPfDviu2BW22eInqumz1NI4fBqlHtD-V3GTT6-QmBIKzLbIRQkg0KeLy3itutBpCeJgu41nNoC8SUZzpDTdxMGD2cOTAfdbS4HWnrbHD6W_w8-6T6qTGrPdrkxpjlw-qJHRqOSZ3j3xqx2GNK_XgnI8024W8dpZfhGkVaR74qndfo7747eTCsTo39lkcrMGCVVHXRqqGR2GYD3YNbe7ezIcrwKX', start_index=9159)
Annotation(end_index=9446, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgBAWdDPqL0KXkbRieMod_-sampSq5p-IMt8UgeQcPs1nnprwgiegdZ0RVSeoJ500hqVeMorNxAyNA3lBLMhhSsUgLb-8mczE1SMSxasmqh3MuebOR2akBmR0RCiXSpQ==', start_index=9437)
Annotation(end_index=9793, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgBAWdDPqL0KXkbRieMod_-sampSq5p-IMt8UgeQcPs1nnprwgiegdZ0RVSeoJ500hqVeMorNxAyNA3lBLMhhSsUgLb-8mczE1SMSxasmqh3MuebOR2akBmR0RCiXSpQ==', start_index=9780)
Annotation(end_index=9793, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhpu0Y0Uw_3s1NPPMURazMLzVG0qawyA8pYMrF6FE0gb2-csP_zOWK7NXn_azH929efr8MfnDcc1_R_tgO5KaYNMPfDviu2BW22eInqumz1NI4fBqlHtD-V3GTT6-QmBIKzLbIRQkg0KeLy3itutBpCeJgu41nNoC8SUZzpDTdxMGD2cOTAfdbS4HWnrbHD6W_w8-6T6qTGrPdrkxpjlw-qJHRqOSZ3j3xqx2GNK_XgnI8024W8dpZfhGkVaR74qndfo7747eTCsTo39lkcrMGCVVHXRqqGR2GYD3YNbe7ezIcrwKX', start_index=9780)
Annotation(end_index=10476, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQET33kegcQJW9GZefJi6GR3W4__5xZlBNWwaakfRmOyfobSJXRKTnbTN6W8xcmz4EiPFg0P9UBkbY4t5NbkO-y8h1PT0e4HrYXNCL18oonaYYVf_TPYqdoC3HFMQVfIMHbCTNcjOalS5vNIQ30Vud6KyqbtCA==', start_index=10462)
Annotation(end_index=10476, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDhbNJvo3PTS5WwcuRox37gy6MY4XLELii2nRpvCO8lUzkd84ycm74gLPjNJgaaBsVsPGIzybybr0NEoRZ7d22lXjabR3j38qbRKh7KmNpsPQeIeXV8e7BHO6Q96FC2MFu3FQLou_g', start_index=10462)
Annotation(end_index=10760, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDhbNJvo3PTS5WwcuRox37gy6MY4XLELii2nRpvCO8lUzkd84ycm74gLPjNJgaaBsVsPGIzybybr0NEoRZ7d22lXjabR3j38qbRKh7KmNpsPQeIeXV8e7BHO6Q96FC2MFu3FQLou_g', start_index=10750)
Annotation(end_index=11116, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQET33kegcQJW9GZefJi6GR3W4__5xZlBNWwaakfRmOyfobSJXRKTnbTN6W8xcmz4EiPFg0P9UBkbY4t5NbkO-y8h1PT0e4HrYXNCL18oonaYYVf_TPYqdoC3HFMQVfIMHbCTNcjOalS5vNIQ30Vud6KyqbtCA==', start_index=11102)
Annotation(end_index=11116, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmda9SJB5coKuyf_z7mccJR02VlWi6gLI5nBft7saWannqZ_ZQdTt_rEvOrhxrfCROdq-2X7WGURZDpZjJIpJ4VUJakhO-GdLRbWT77p7pPvyYLsGQFPnP020PsN3KjzeQ16cPcHzH', start_index=11102)
Annotation(end_index=11330, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgBAWdDPqL0KXkbRieMod_-sampSq5p-IMt8UgeQcPs1nnprwgiegdZ0RVSeoJ500hqVeMorNxAyNA3lBLMhhSsUgLb-8mczE1SMSxasmqh3MuebOR2akBmR0RCiXSpQ==', start_index=11321)
Annotation(end_index=11840, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmda9SJB5coKuyf_z7mccJR02VlWi6gLI5nBft7saWannqZ_ZQdTt_rEvOrhxrfCROdq-2X7WGURZDpZjJIpJ4VUJakhO-GdLRbWT77p7pPvyYLsGQFPnP020PsN3KjzeQ16cPcHzH', start_index=11826)
Annotation(end_index=11840, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2DYuAxaVyT3Yc1MUHkuJPyOr2xvhCvNtTjf5EFK7_Bxny8sXfxt5PEu_PLWRqBt36rELvgDjH7OdCwFjIEOWUdGcADoVTvdmF8s9_EnAsrZ8g8oA2KI4z736pKJ89nSBW', start_index=11826)
Annotation(end_index=12260, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8HRaozquTRYpQodb3vbq1EWdYhvvzl4TVxB7paGD6ambP8bFxw-gmceUxZ5LBGVQvlgB4e5z-fb6Fmc7nP8SDdUIh-Ate8agG-DQGLHHJQKxfShFs50VyTSeIxil0Rgo1saIAF-Rz', start_index=12246)
Annotation(end_index=12260, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZyMAou8QxJXu0UDsromu_ye1xHJPfeh1TQtu_UydQw2xe3BLXbtmXTTh_UiLLdbqAaHvknN-d8IJbmirQzArxYbTmGV7OEQWUAdpNYAZ4y6Q4Y7f1elKrnhD_ENVwqqY-N6x1lKEs4CXmVxCNsgDSZemrZdlMMf_4SU7gRjCB9p87Glct5b_1_rZ5TPjddgmwnAyDiAlGRbdsS_4h5J8bKGo-3ewE0A0M5re-', start_index=12246)
Annotation(end_index=12460, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExaNb1DRpUB-8wlNzGA3fUTot6O8r1gv_41DxE0-lhJntBGdGxjdTZhj3yelbt05DFEmbrfsD9qroH7yq1ZszKiQj6tPTqh9z91RDr2SPIwo-JF1SVkmEhPu9DTRjixw==', start_index=12446)
Annotation(end_index=12460, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN3h8NVPAHAxqq9UxRWdtE2mmmnpV5Hy7I6TeoLc45vCW5KhlmeiIqRcTpuqqQHkXRp56XevPauE4Cetpoidrcr5Gp0rPnwo9mIlBvmIqU68_BI8h7pHh2pVmxQokBd6PSM83rRGUHIvAwdyEov568WdUgVVjVks6fENd4otWiUInKCdKSQi-jK3CW89JRKXNxJ82KmxSQK_Rl2ArcHRdRYFyR', start_index=12446)
Annotation(end_index=12750, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVFolCggLq7igB2GEXCHT8sndMqRgEeWk4xm0CKi05IFh9KyIBE67IXZa2__QGRG9MKOHvRjM40l0djZlOKpSOFU6oAzenyJCQENQknA9qYrXyuHZNwwsO-HoFJ1jV3TLv0PVYGmtJQzSVVQ==', start_index=12736)
Annotation(end_index=12750, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8HRaozquTRYpQodb3vbq1EWdYhvvzl4TVxB7paGD6ambP8bFxw-gmceUxZ5LBGVQvlgB4e5z-fb6Fmc7nP8SDdUIh-Ate8agG-DQGLHHJQKxfShFs50VyTSeIxil0Rgo1saIAF-Rz', start_index=12736)
Annotation(end_index=13098, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpbbn25pbJV390SPrFIxLysFPudzmniRFzlp7Qj5xytUqQRlwDRSvu0sR3mG6VbHlTT6roSXfRMe_v2J2zCKmP8PQce9OtfFZDM1213J5g_SsYDQ3ttBH7jxPYdgIbMQ==', start_index=13088)
Annotation(end_index=13902, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmda9SJB5coKuyf_z7mccJR02VlWi6gLI5nBft7saWannqZ_ZQdTt_rEvOrhxrfCROdq-2X7WGURZDpZjJIpJ4VUJakhO-GdLRbWT77p7pPvyYLsGQFPnP020PsN3KjzeQ16cPcHzH', start_index=13892)
Annotation(end_index=14314, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2WrnPBsxVgUdYmUSLnns2bGQvhcGk0LkFUK3-Wibx90t-zAQgkdPcIaCCBOxeG-SCGWjUsCfEcj1XUetSax7p2JYx6vIyp8DVfEnu7aIKWuVub8Gf2T220RiZSAf5Uw==', start_index=14305)
Annotation(end_index=14578, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2WrnPBsxVgUdYmUSLnns2bGQvhcGk0LkFUK3-Wibx90t-zAQgkdPcIaCCBOxeG-SCGWjUsCfEcj1XUetSax7p2JYx6vIyp8DVfEnu7aIKWuVub8Gf2T220RiZSAf5Uw==', start_index=14566)
Annotation(end_index=14578, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6umsgV51ljhPNpDNZBUbO0KaAc_unhAbC_2RmcSqkGECovJt7465_hSm3m3U7FFjMa4d1nF3_D86-hMpwsDF-qRjXpHE-OJRJyhg2KyMLWmW-4_W7Ft76mpuoiEGY7YSWXSqllGQt4nEHU4EaO3Gmcnr63TUMAqjkmlKMYHgSWK8RdYnaHtEiO5Ghf85sw3HJ68wDCUSr15mzMH0SIqfEWQo=', start_index=14566)
Annotation(end_index=15162, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsEGJDZx2GYXMR5OnNq80YdilxPRZSrcDJdKQTgyTMmnQwB7hxMnKAzn6SrOolSMZEnZWbbn6qlwfgUGaTIhFepiejYBTrzXoM1SiT3MuhndJb9w4Ar7Y6b2HzazhmHNE=', start_index=15152)
Annotation(end_index=15285, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEO3y0joFk-YtXYR5gUN78IfLSLoGBYFLcBb_ryq8YjwzomhnU5qn9Pc2oNG2msBTTzISvTOY8Xv9LED09rF8DuX4IXPQ5Q2Z9GjyslwPt4jW6X8YGbqxJl8UJfh2BAgw9laVmG3o84dyf8ASWcMb8mxNmUMaT6UAo28FDDDGFQdDK2-zaC3_qUZifhl2GlsGYR-93_3gec0Ku7TpxJztNMzD4-_lyBMmA2CZ9PCy4b2E2cFO3iyp0tCalXOeYwKiqGqXeE-3rvRlfyqvxf8xmjTAzTcCQc', start_index=15275)
Annotation(end_index=15786, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN3h8NVPAHAxqq9UxRWdtE2mmmnpV5Hy7I6TeoLc45vCW5KhlmeiIqRcTpuqqQHkXRp56XevPauE4Cetpoidrcr5Gp0rPnwo9mIlBvmIqU68_BI8h7pHh2pVmxQokBd6PSM83rRGUHIvAwdyEov568WdUgVVjVks6fENd4otWiUInKCdKSQi-jK3CW89JRKXNxJ82KmxSQK_Rl2ArcHRdRYFyR', start_index=15772)
Annotation(end_index=15786, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTn9zsPRHHou4QXPNuNkwzvbF3PTpe-Kn9ucsIHlZPR7FLzqNwKyvgpCnyMg-_16lC0ODekUF4ZTJoZ9nmmpFOj71_Xc4fe_1kUc3BEjTBNLywkGamS4iOtPAn_bedG5GxZmQsZDnY', start_index=15772)
Annotation(end_index=16042, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2WrnPBsxVgUdYmUSLnns2bGQvhcGk0LkFUK3-Wibx90t-zAQgkdPcIaCCBOxeG-SCGWjUsCfEcj1XUetSax7p2JYx6vIyp8DVfEnu7aIKWuVub8Gf2T220RiZSAf5Uw==', start_index=16033)
Annotation(end_index=16530, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRQgzE_BvRGY4BLozH8AZLFoiVvlvVZX6XJ38oeNqDKMgm9iXMcO0jUpKaUy5olbdqUufezBg1Y2Auv9vv_M9qI_YsHHtEAlGckshWz8LCJwAcb9OXIX9OKPKe9YZSsfHNTy4iqTVzadElR7hP1sD49ntPzQ10ikdqm07gNDiY3KKaIv_PmzzOiXJEyPPhBchojgQkV-zW5NSIPEe5m95sGVnppWZZNUJdmZMK3kt4z7HcBxNNflveDO3J0bFmDVqoKQi_xKCx9zH0Zs6YnD7iQDnYE7hHFQ==', start_index=16520)
Annotation(end_index=16735, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSjNvag7EH8LZZ1LPSVchVwyK6_w-FaDPx7KtcCv3QwmNQsf3B-UOsh2ER5wpzrlkKDMmMXwhYXSg81QZ6Zh7291I6z73CbALcs5k2yA3lGmWaPszfwQz02I820IzhVSdyaWP5h55C', start_index=16719)
Annotation(end_index=16735, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG646dNrhsc3_nUAxPsNsB9kIVzA3PpBGJHgxy-vKF9cTQmd-0fWPAmOXi5wO2HvN8p_G4hdbrdFjhOMGUdNt2GTKt_gOaY3C_tse9p9c93g7Y5BnB6HED6aL5MBnFYSw==', start_index=16719)
Annotation(end_index=16735, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfIE_YB902471AgjUjMCy0asYk-GT3Uy64yN6vW_JMmh4p7tYjS9bG3z-9E-txFqKc_P4uuPAcsvapO0wRKOQyPa84nlKRGRKXSlOtdK2C0-KdlZyt4LISkJxDFuQI5tlaiXzUDULGPg==', start_index=16719)
Annotation(end_index=17031, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG646dNrhsc3_nUAxPsNsB9kIVzA3PpBGJHgxy-vKF9cTQmd-0fWPAmOXi5wO2HvN8p_G4hdbrdFjhOMGUdNt2GTKt_gOaY3C_tse9p9c93g7Y5BnB6HED6aL5MBnFYSw==', start_index=17022)
Annotation(end_index=17269, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN3h8NVPAHAxqq9UxRWdtE2mmmnpV5Hy7I6TeoLc45vCW5KhlmeiIqRcTpuqqQHkXRp56XevPauE4Cetpoidrcr5Gp0rPnwo9mIlBvmIqU68_BI8h7pHh2pVmxQokBd6PSM83rRGUHIvAwdyEov568WdUgVVjVks6fENd4otWiUInKCdKSQi-jK3CW89JRKXNxJ82KmxSQK_Rl2ArcHRdRYFyR', start_index=17255)
Annotation(end_index=17269, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKAWM2cKCEru-Iu19-y-pKYHWq3Yae47qRFHndqd05QaxTiPT0sDzmJA5v8FTCNv7Op_gpSCnPy3ivj9tZBIO71vSUPItWoawv5qWgwefZguHVEjmTRXJZ5WhvJZ96rHMu_ADktTnt', start_index=17255)
Annotation(end_index=18800, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEbeTbSZ1klQkazsk6r_SA4sZwVdwEIY1qeQ9GIHPy9nBx2b_cU4VCpIguUJ8vwfX3L55AGCXoigvXg3hAcgMr6X0Kcab6dZM3M_hf5FADVbbbi_98kYW-DF_yyewAUKyfSQ-dEC1CQOhv9yiCcZqsKNgBgXwS2ihwnF7fYcuF3vDVdSJIVkfsWNhNJeDXNHeII1em4wa5flGixx7Uh62S_iRz67JzLr0zIkxXktfY2m-4fKK_-KGEYWMjdahxEyCDqFwlAp1eiHj48upy_W-TNoY18xXanZew=', start_index=18790)
Annotation(end_index=18960, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTn9zsPRHHou4QXPNuNkwzvbF3PTpe-Kn9ucsIHlZPR7FLzqNwKyvgpCnyMg-_16lC0ODekUF4ZTJoZ9nmmpFOj71_Xc4fe_1kUc3BEjTBNLywkGamS4iOtPAn_bedG5GxZmQsZDnY', start_index=18950)
Annotation(end_index=19343, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFItsS15hlmjg7YDTgFcu4Iab2hAf1GeWc85nUUQNsLtzhSCVlBxV8MwX4YFU2f_PEHzf7XvJEA6RPESzG8dM7HNCyae2fQhk0hcffmdHMoqKb5uGMI0KONgm4Un7mHexqpZRz0y4Lg3pt2KiKUj3Zxpo36QHC6J9uayrucVcR0Tx0xfP9N8Zf5KfpJ3W_WtonbyyzAN1hLTercGUIgGe2MhDbYh7l3YqFBQEcCJWB6vZmVYjnIWa6jTtu3ULjx3zoUcOhyYiU8ReLcVyknvlMcOsL5moAs42f4qMSlKFLwYdVhAGLf00jSAj7Jv25aqbFAuVtubSKZj7nh1ftMOAwpK9NnpkP0ac9XrP6byinq5vx48yMTd3XuXwor', start_index=19333)
Annotation(end_index=19691, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExaNb1DRpUB-8wlNzGA3fUTot6O8r1gv_41DxE0-lhJntBGdGxjdTZhj3yelbt05DFEmbrfsD9qroH7yq1ZszKiQj6tPTqh9z91RDr2SPIwo-JF1SVkmEhPu9DTRjixw==', start_index=19677)
Annotation(end_index=19691, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN3h8NVPAHAxqq9UxRWdtE2mmmnpV5Hy7I6TeoLc45vCW5KhlmeiIqRcTpuqqQHkXRp56XevPauE4Cetpoidrcr5Gp0rPnwo9mIlBvmIqU68_BI8h7pHh2pVmxQokBd6PSM83rRGUHIvAwdyEov568WdUgVVjVks6fENd4otWiUInKCdKSQi-jK3CW89JRKXNxJ82KmxSQK_Rl2ArcHRdRYFyR', start_index=19677)
Annotation(end_index=19866, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2WrnPBsxVgUdYmUSLnns2bGQvhcGk0LkFUK3-Wibx90t-zAQgkdPcIaCCBOxeG-SCGWjUsCfEcj1XUetSax7p2JYx6vIyp8DVfEnu7aIKWuVub8Gf2T220RiZSAf5Uw==', start_index=19857)
Annotation(end_index=20331, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsEGJDZx2GYXMR5OnNq80YdilxPRZSrcDJdKQTgyTMmnQwB7hxMnKAzn6SrOolSMZEnZWbbn6qlwfgUGaTIhFepiejYBTrzXoM1SiT3MuhndJb9w4Ar7Y6b2HzazhmHNE=', start_index=20317)
Annotation(end_index=20331, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhgKxSIpijS1ppDcV5o4-SVHrvtsicZIhaGi45g0PP9gSOIQTk_VyqUbNSQ82LTrCxBreppO04Yo_Y-2ML7vAKf-yJRTcVjG2LpTbfGQLcjDp9q2AI5XbrJg5LaQhmbBFpihYKoTD0SFf63bk9iQYOj7W8pz5eyJlSo8LHD40oH4JZQlf6tSCbpb8dtNgh1lM--vdxzDruTeOKsACUIwElVX4M4A==', start_index=20317)
Annotation(end_index=20552, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFK1ErIrSdyyliEex8q9OulAY45GSbosfi056xKFFUKhWyydFBa1w8p1J-mPxbFEojJKLu9or_uoghb58yybEtp_E42yX0mWui5igpp8Wfd3tvhZyZjaGRHL_3sPPQGjlIycX2VxtCy5XYxa5P7J7HFvKg=', start_index=20542)
Annotation(end_index=20587, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2WrnPBsxVgUdYmUSLnns2bGQvhcGk0LkFUK3-Wibx90t-zAQgkdPcIaCCBOxeG-SCGWjUsCfEcj1XUetSax7p2JYx6vIyp8DVfEnu7aIKWuVub8Gf2T220RiZSAf5Uw==', start_index=20578)
Annotation(end_index=20670, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgBAWdDPqL0KXkbRieMod_-sampSq5p-IMt8UgeQcPs1nnprwgiegdZ0RVSeoJ500hqVeMorNxAyNA3lBLMhhSsUgLb-8mczE1SMSxasmqh3MuebOR2akBmR0RCiXSpQ==', start_index=20661)
Annotation(end_index=20751, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFaXezti0CL-aCbJ3BLUn7ECWDCKoHOM2lXtErfGemJw2c5u22BrN8boIwp_tWVYvRgPwUmSS7khU7e7WuRwBcJoscGfUDl5Ds9PPw0sY52MtCYFMDfGydSNAf2qBpB1VeW-uQLV-A2', start_index=20742)
Annotation(end_index=20845, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrzJ7EhprUVV3lSuMhxevd6STlaOoifsc-wHchmnCZLXQJdXHOqrM0X-Bj7_XOEIFjctv_Y3lr4CPjShulh3B0EQWstfiK5_kRFS-_tCbtsVP0PnM-5yJTTT9Ckp0LkYAvZn4Ok5VrQ4uiCjsw_RpKpRyGifEqg4t9RTVNyBlK2l1Ckv1au4mrrhTa240cJCx430UVmB_Z0vtFW3kmVYYUMYQjF0-VyNOdFtnwqp4cj_n6sKrpjFJ8_vNK', start_index=20836)
Annotation(end_index=20917, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQET33kegcQJW9GZefJi6GR3W4__5xZlBNWwaakfRmOyfobSJXRKTnbTN6W8xcmz4EiPFg0P9UBkbY4t5NbkO-y8h1PT0e4HrYXNCL18oonaYYVf_TPYqdoC3HFMQVfIMHbCTNcjOalS5vNIQ30Vud6KyqbtCA==', start_index=20907)
Annotation(end_index=20995, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN3h8NVPAHAxqq9UxRWdtE2mmmnpV5Hy7I6TeoLc45vCW5KhlmeiIqRcTpuqqQHkXRp56XevPauE4Cetpoidrcr5Gp0rPnwo9mIlBvmIqU68_BI8h7pHh2pVmxQokBd6PSM83rRGUHIvAwdyEov568WdUgVVjVks6fENd4otWiUInKCdKSQi-jK3CW89JRKXNxJ82KmxSQK_Rl2ArcHRdRYFyR', start_index=20985)
Annotation(end_index=21079, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTn9zsPRHHou4QXPNuNkwzvbF3PTpe-Kn9ucsIHlZPR7FLzqNwKyvgpCnyMg-_16lC0ODekUF4ZTJoZ9nmmpFOj71_Xc4fe_1kUc3BEjTBNLywkGamS4iOtPAn_bedG5GxZmQsZDnY', start_index=21069)
Annotation(end_index=21156, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmda9SJB5coKuyf_z7mccJR02VlWi6gLI5nBft7saWannqZ_ZQdTt_rEvOrhxrfCROdq-2X7WGURZDpZjJIpJ4VUJakhO-GdLRbWT77p7pPvyYLsGQFPnP020PsN3KjzeQ16cPcHzH', start_index=21146)

## Sources
