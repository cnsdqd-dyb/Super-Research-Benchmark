# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 18ae5edf | **Time:** 277.79s | **Cost:** $0.83491
--------------------------------------------------------------------------------

# Optimizing Cardiovascular Drug Combinations: Balancing Blood Pressure Reduction and Cardiac Output Maintenance

### Key Points
*   **Hemodynamic Equation:** Blood pressure (BP) is the product of Cardiac Output (CO) and Systemic Vascular Resistance (SVR). Effective optimization requires targeting the specific hemodynamic derangement (e.g., elevated SVR) rather than simply lowering pressure, which can inadvertently compromise organ perfusion if CO is suppressed.
*   **Complementary Mechanisms:** The most effective combinations pair agents that lower SVR (vasodilators like CCBs or ACEIs) with agents that modulate compensatory cardiac responses (like beta-blockers or diuretics). For instance, ACE inhibitors can blunt the reflex tachycardia sometimes associated with calcium channel blockers.
*   **Vasodilating Beta-Blockers:** Newer generation beta-blockers (e.g., carvedilol, nebivolol) offer a distinct advantage over traditional agents (e.g., atenolol) by reducing SVR while maintaining cardiac output and peripheral blood flow, making them critical in optimizing hemodynamic balance.
*   **Precision Hemodynamics:** Advanced optimization increasingly utilizes thoracic bioimpedance (impedance cardiography) to phenotype patients. This allows clinicians to distinguish between "vasoconstricted" (high SVR) and "hyperdynamic" (high CO) hypertension, guiding the choice between vasodilators and cardio-depressants respectively.
*   **Computational Modeling:** Emerging in silico models and machine learning algorithms are being used to predict adverse drug reactions and simulate patient-specific hemodynamic responses to multidrug regimens, moving therapy from trial-and-error to predictive precision.

---

## Introduction: The Hemodynamic Imperative in Hypertension Management

The management of cardiovascular disease, particularly hypertension and heart failure, is fundamentally a challenge of fluid dynamics. Arterial blood pressure (BP) is determined by the hydraulic equation $BP = CO \times SVR$, where $CO$ represents cardiac output (the volume of blood pumped by the heart per minute) and $SVR$ represents systemic vascular resistance (the resistance to flow offered by the peripheral circulation) [cite: 1, 2]. While the clinical goal is often defined by a target blood pressure (e.g., <130/80 mmHg), the physiological imperative is to achieve this reduction without compromising tissue perfusion, which is dependent on maintaining adequate cardiac output [cite: 3, 4].

Monotherapy often fails to achieve this balance due to compensatory homeostatic mechanisms. For example, a pure vasodilator that lowers SVR may trigger a baroreceptor-mediated reflex increase in heart rate and contractility, thereby increasing CO and partially negating the antihypertensive effect or causing palpitations [cite: 5, 6]. Conversely, agents that suppress cardiac function to lower BP may result in fatigue and exercise intolerance due to inadequate CO [cite: 7]. Therefore, optimizing drug combinations requires a mechanistic approach that addresses the specific hemodynamic profile of the patient—balancing afterload reduction (lowering SVR) with the preservation of cardiac pump function [cite: 8, 9].

This report examines the pharmacological principles, combination strategies, and technological advancements used to optimize this delicate hemodynamic balance.

---

## Hemodynamic Pharmacology of Major Drug Classes

To understand optimization, one must first delineate how individual drug classes influence the variables of the BP equation.

### 1. Agents Primarily Reducing Systemic Vascular Resistance (SVR)

**Angiotensin-Converting Enzyme Inhibitors (ACEIs) and Angiotensin Receptor Blockers (ARBs):**
These agents are the cornerstone of "hemodynamically neutral" or positive therapy. By inhibiting the renin-angiotensin-aldosterone system (RAAS), they prevent the formation or action of Angiotensin II, a potent vasoconstrictor.
*   **Hemodynamic Effect:** They consistently reduce SVR. Crucially, in patients with essential hypertension, they typically maintain cardiac output or allow it to rise slightly by reducing afterload. They do not typically suppress the heart rate [cite: 3, 10].
*   **Organ Perfusion:** Because they lower SVR without compromising CO, they maintain or improve blood flow to vital organs (brain, kidney, heart) [cite: 3].

**Calcium Channel Blockers (CCBs):**
*   **Dihydropyridines (e.g., Amlodipine, Nifedipine):** These are potent arterial vasodilators. They lower BP by reducing SVR. However, the rapid vasodilation can trigger a reflex sympathetic activation, potentially increasing heart rate and CO, particularly with short-acting formulations [cite: 2, 9].
*   **Non-Dihydropyridines (e.g., Verapamil, Diltiazem):** These agents have a dual effect. They cause some vasodilation (lowering SVR) but also depress the sinoatrial and atrioventricular nodes (negative chronotropy) and myocardial contractility (negative inotropy). Consequently, they lower BP by reducing both SVR and CO [cite: 2, 11].

**Direct Vasodilators (e.g., Hydralazine, Minoxidil):**
These drugs act directly on vascular smooth muscle to cause profound relaxation.
*   **Hemodynamic Consequence:** They drastically reduce SVR. However, this triggers a powerful baroreceptor reflex, leading to significant tachycardia and increased cardiac output. Without concurrent blockade of this reflex, the heart works harder, increasing myocardial oxygen demand [cite: 5, 9, 12].

### 2. Agents Primarily Modulating Cardiac Output (CO)

**Beta-Adrenergic Blockers (Beta-Blockers):**
*   **Traditional (e.g., Atenolol, Metoprolol):** These agents block $\beta_1$ receptors, reducing heart rate and contractility. This lowers BP primarily by reducing CO. A significant limitation is that SVR often rises reflexively or remains elevated, which can compromise peripheral blood flow and lead to fatigue [cite: 7, 13, 14].
*   **Vasodilating Beta-Blockers (e.g., Carvedilol, Nebivolol):** These represent a hemodynamic optimization within a single molecule. They block $\beta$ receptors (lowering CO/HR) but also block $\alpha_1$ receptors (Carvedilol) or stimulate nitric oxide release (Nebivolol), leading to vasodilation. This dual action lowers BP by reducing both CO and SVR, preserving organ perfusion better than traditional beta-blockers [cite: 15, 16, 17].

**Diuretics (e.g., Thiazides, Loop Diuretics):**
Initially, diuretics lower BP by reducing plasma volume, which decreases venous return (preload) and subsequently cardiac output. With chronic use, CO tends to normalize, and the persistent BP reduction is attributed to a decrease in SVR, likely due to reduced vascular sodium content and autoregulatory adjustments [cite: 2, 6].

---

## Strategies for Optimizing Drug Combinations

Optimization involves selecting drug pairs that target different physiological mechanisms to achieve additive BP reduction while neutralizing compensatory hemodynamic reflexes.

### 1. The ACE Inhibitor + Calcium Channel Blocker Paradigm
This combination is widely regarded as hemodynamically superior to older regimens (such as beta-blockers plus diuretics) for reducing cardiovascular events [cite: 8, 18].

*   **Mechanism of Balance:** CCBs (specifically dihydropyridines) dilate arteries to lower SVR. Monotherapy might cause reflex sympathetic activation or peripheral edema (due to preferential arteriolar dilation causing capillary hypertension). ACE inhibitors counteract these side effects. By blocking the RAAS, ACE inhibitors blunt the sympathetic response and cause venodilation, which normalizes capillary hydrostatic pressure and reduces edema [cite: 8, 19].
*   **Cardiac Output Maintenance:** Both classes are effective at lowering afterload. The combination results in "fully additive" BP reduction without suppressing cardiac function. In the ACCOMPLISH trial, this combination reduced cardiovascular morbidity more effectively than ACEI plus diuretics, likely due to better preservation of central hemodynamics and metabolic neutrality [cite: 8, 18].

### 2. Managing Reflex Tachycardia: Vasodilators + Beta-Blockers
When potent vasodilation is required (e.g., in resistant hypertension using minoxidil or hydralazine), the maintenance of cardiac output becomes a liability rather than a goal; the heart beats too fast and too hard (reflex tachycardia).

*   **Optimization Strategy:** A beta-blocker is added specifically to inhibit the $\beta_1$-mediated sympathetic surge caused by the vasodilator. This prevents the "overshoot" in cardiac output that would otherwise counteract the blood pressure lowering effects and increase myocardial oxygen consumption [cite: 5, 12].
*   **Hemodynamic Result:** The vasodilator lowers SVR, while the beta-blocker prevents the maladaptive increase in CO. The net result is a controlled reduction in BP with a stable heart rate [cite: 20].

### 3. The Role of Vasodilating Beta-Blockers
In conditions where beta-blockade is necessary (e.g., heart failure, post-MI) but maintenance of cardiac output and peripheral flow is critical, vasodilating beta-blockers are preferred over traditional ones.

*   **Comparison:** Traditional beta-blockers (atenolol) reduce CO but increase SVR, which can impair exercise capacity. Vasodilating beta-blockers (carvedilol) reduce SVR while preventing the drop in CO during exercise, maintaining renal and cerebral blood flow [cite: 7, 15].
*   **Clinical Outcome:** This profile is associated with better functional outcomes and less fatigue, representing an optimized balance for patients requiring adrenergic blockade [cite: 16, 17].

---

## Advanced Optimization: Hemodynamic Monitoring and Phenotyping

A major evolution in optimization is the shift from empirical "stepped care" to "physiologically individualized" therapy based on non-invasive hemodynamic monitoring, specifically **Impedance Cardiography (ICG)** or Thoracic Bioimpedance.

### 1. The Hemodynamic Phenotype
Hypertension is heterogeneous. Two patients with a BP of 160/100 mmHg may have diametrically opposite hemodynamic profiles:
*   **Hypodynamic/Vasoconstricted:** Low CO, very high SVR.
*   **Hyperdynamic:** High CO, normal/mildly elevated SVR.

Treating a "hypodynamic" patient (who relies on SVR to maintain pressure) with a beta-blocker (which lowers CO) would be hemodynamically counterproductive, potentially worsening fatigue and failing to lower BP effectively. Conversely, treating a "hyperdynamic" patient with a pure vasodilator might exacerbate their high output state [cite: 2, 21].

### 2. ICG-Guided Therapy
Thoracic bioimpedance measures changes in thoracic fluid conductivity to calculate Stroke Volume (SV), Cardiac Output (CO), and Systemic Vascular Resistance (SVR) [cite: 22].

*   **Clinical Application:** Studies utilizing the HOTMAN system or similar ICG devices have demonstrated that tailoring drugs to the hemodynamic phenotype improves control rates.
    *   **High SVR / Low CO:** Therapy is optimized by adding vasodilators (ACEIs, ARBs, CCBs) to unload the ventricle and reduce resistance.
    *   **High CO / Normal SVR:** Therapy is optimized by using beta-blockers to reduce the cardiac drive [cite: 21, 23, 24].
*   **Case Evidence:** In resistant hypertension cases where patients were uncontrolled on multiple drugs, ICG often reveals an untreated hemodynamic derangement (e.g., persistent vasoconstriction despite diuretic use). Switching to an agent that targets the specific anomaly (e.g., adding an alpha-blocker or CCB for high SVR) often achieves control within days [cite: 21, 25].
*   **Pregnancy:** In hypertensive disorders of pregnancy, ICG has been used to distinguish between high-output and high-resistance states, allowing for therapy that reduces fetal growth restriction risks by avoiding over-reduction of cardiac output [cite: 26, 27].

---

## Computational Modeling and In Silico Optimization

Beyond bedside monitoring, computational biology is providing new tools to optimize drug combinations.

### 1. Virtual Patient Models
Researchers are developing multi-scale mathematical models of the cardiovascular system that integrate fluid dynamics (Navier-Stokes equations) with electromechanical models of the heart. These "virtual patients" allow for the simulation of drug effects on both macro-hemodynamics (BP, CO) and micro-hemodynamics (cellular calcium transients) [cite: 28, 29].

### 2. Predicting Interactions
Machine learning algorithms are being trained on vast datasets to predict adverse drug reactions (ADRs) and hemodynamic incompatibility. For example, models can predict the risk of QT prolongation or excessive bradycardia when combining specific cardioinhibitory drugs, ensuring that the "maintenance of cardiac output" does not cross the line into cardiac arrest [cite: 30, 31].

### 3. The SILICOFCM Project
This project exemplifies the use of finite element modeling to simulate the effects of drugs like disopyramide (negative inotrope) versus mavacamten on Left Ventricular (LV) pressure-volume loops. Such modeling helps predict which drug combination will optimize the stroke volume in patients with hypertrophic cardiomyopathy, a condition where the balance between obstruction relief and CO maintenance is precarious [cite: 28].

---

## Clinical Scenarios: Balancing BP and CO

### 1. Heart Failure with Reduced Ejection Fraction (HFrEF)
In HFrEF, CO is intrinsically low. The optimization challenge is to lower SVR (afterload) to allow the weak heart to pump more easily, without lowering BP so much that perfusion pressure fails.
*   **Afterload Reduction:** Vasodilators (ACEIs, Hydralazine+Nitrates) reduce SVR. In the failing heart, this paradoxically *increases* or maintains CO by shifting the heart to a more favorable position on the Frank-Starling curve (unloading) [cite: 3, 32].
*   **Sympathetic Blockade:** Beta-blockers are mandatory to prevent arrhythmia and remodeling, but they must be titrated carefully to avoid acute decompensation (dropping CO too fast). The combination of ACEI + Beta-blocker is the gold standard for balancing neurohormonal blockade with hemodynamic stability [cite: 33, 34].

### 2. Resistant Hypertension
Patients with resistant hypertension often have expanded fluid volume and high SVR.
*   **Triple Therapy:** The standard optimization is A+C+D (ACEI/ARB + CCB + Diuretic). This attacks all three mechanisms: SVR (A+C), Volume (D), and RAAS (A).
*   **The Fourth Drug:** If BP remains uncontrolled, spironolactone is added. If ICG shows high SVR, powerful vasodilators like minoxidil may be used, but strictly combined with a loop diuretic (for volume) and a beta-blocker (for reflex tachycardia) to maintain the hemodynamic equilibrium [cite: 5, 18, 35].

---

## Conclusion

The optimization of cardiovascular drug combinations has evolved from a trial-and-error approach to a sophisticated balancing act of hemodynamic variables. The fundamental principle remains the equation $BP = CO \times SVR$. Successful combination therapy—such as the pairing of ACE inhibitors with CCBs, or the use of vasodilating beta-blockers—works by synergistically reducing systemic vascular resistance while preserving or enabling the heart's pumping ability.

The integration of thoracic bioimpedance monitoring represents the frontier of this field, allowing clinicians to visualize the hemodynamic phenotype and select drugs that correct the specific underlying imbalance (high resistance vs. high output). Furthermore, computational modeling is beginning to offer predictive capabilities that may eventually allow for fully personalized, in silico testing of drug combinations before a single pill is prescribed. Through these methods, clinicians can achieve the dual goals of blood pressure control and organ perfusion maintenance, reducing long-term cardiovascular morbidity.

## References

[cite: 18] *Journal of Hypertension* (2010). "Optimizing antihypertensive drug combinations to maintain cardiac output."
[cite: 35] *Hypertension* (2025). "Starting With Combination Therapy Versus Stepped Care."
[cite: 13] *Dr. Oracle* (2025). "What medication increases vascular peripheral resistance increases blood pressure."
[cite: 8] *Journal of Clinical Hypertension* (2011). "Position Paper on Combination Therapy for Hypertension."
[cite: 22] *Therapeutic Advances in Cardiovascular Disease* (2010). "Hemodynamic patterns of age-related changes in blood pressure."
[cite: 11] *CV Pharmacology* (2023). "Cardioinhibitory Drugs."
[cite: 9] *StatPearls* (2023). "Afterload Reduction."
[cite: 32] *CV Physiology* (2023). "Cardiac Afterload."
[cite: 5] *Wikipedia* (2023). "Minoxidil."
[cite: 20] *YouTube* (2025). "Antihypertensive Combination Therapy: Pros & Cons."
[cite: 15] *Drugs* (1992). "Hemodynamic effects of antihypertensive agents."
[cite: 14] *Cleveland Clinic Journal of Medicine* (1992). "The hemodynamic effects of adrenergic blocking agents."
[cite: 30] *Journal of Translational Medicine* (2019). "Machine learning based approach for cardiovascular ADRs prediction."
[cite: 28] *Pharmaceutics* (2023). "Computational Modeling and Drug Design in Cardiomyopathy."
[cite: 21] *Journal of Medicine and Life* (2018). "Hemodynamic monitoring using thoracic bioimpedance."
[cite: 23] *ResearchGate* (2018). "Hemodynamic monitoring using thoracic bioimpedance - an optimal solution."
[cite: 26] *Journal of Clinical Medicine* (2022). "Impedance-guided antihypertensive therapy in pregnancy."
[cite: 24] *Zeal Journals* (2024). "Role of Bioimpedancemetry in Optimizing Antihypertensive Therapy."
[cite: 7] *Journal for Cardiology* (2008). "Functional-physiological effect of beta blockers vs vasodilators."
[cite: 16] *Journal of Clinical Hypertension* (2007). "Vasodilating beta-blockers vs traditional beta-blockers."
[cite: 17] *Revista Española de Cardiología* (2019). "Beta-blockers: Historical Perspective."
[cite: 3] *Journal of Hypertension* (1990). "Hemodynamic effects of ACE inhibitors."
[cite: 19] *Journal of Clinical Hypertension* (2008). "Combination Therapy with ACEIs and CCBs."
[cite: 10] *American Journal of Cardiology* (1995). "Hemodynamic effects of ACE inhibitors and calcium antagonists."
[cite: 1] *Cleveland Clinic Journal of Medicine* (1992). "Current Drug Therapy: Hemodynamic effects."
[cite: 2] *American Journal of Hypertension* (2005). "Hemodynamic balance in hypertension treatment."
[cite: 4] *StatPearls* (2023). "Peripheral Vascular Resistance."
[cite: 6] *CV Physiology* (2023). "How Changes in SVR Affect Vascular Pressures."
[cite: 25] *Annals of Clinical and Experimental Hypertension* (2017). "Impedance Cardiography to Guide Antihypertensive Treatment."
[cite: 27] *Journal of Clinical Medicine* (2025). "Thoracic Bioimpedance in Hypertensive Disorders of Pregnancy."

**Sources:**
1. [mdedge.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVr616nt6vOBehMKCX8HDUCpZqo_hwdUNEVVg43S1UAnCMSzhWaTbmaklRhATNj6HewG2MzP3h_E3FbJTzqzU1W6lgWAZI9vHkuhvesIw0bnfLHdVoNy8XlOaQVIffXcbsWGN-4_CY8xU6C5ktaR6r_Rwzqs8XUvnPj1fWRbFlNkJG6_YspLtg-HZhqguz)
2. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhMwTPKd0FTofk416YZRSIvWmkl2MqDfmG3HM-MLmDuiORG2LyHb7R90isz9cvfxPsmQHt46I2hbP-dQq-KK4nkLw7ufniON_wcvLGACjuIxXcR2JuIouZzIJ0SSwFO2Kz5N2QhPM4wIcANw==)
3. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjHcoNFvwWQyB1LQ96xfLsByOzfuk6mkR73wGb6_63tjF2dd_Zy6NrM8HI-uWiysF6mUgGvf-IpVDBLtThhUKuu4MpDaqMuZHe8NSVgXtmT8fTCEmvbs2lRqz4OtCH)
4. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnFVf4FI1CnjIKqBREbLD1tfJIwexv6qiJM8kZM8Eq3tQG277nT9K8bJgqotWuZB8e95Mxo-KoO5s19Ul_ZRVmxedd5ISHOGvr1dyOEy5evBiJMTFJ4RyYZ37Pq-axiX50XzI=)
5. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvYH5pTPjGbTHK1dwcH2jSvmUleUYRVHFP3031aR5cxz7DJ8Qh3aT9h8TonuA1wiUzFhFhctM0eFVZDgMAa0jnW4cxP_S-0kM9NZdJX8xHffIecpOyHC94C1vsOfI=)
6. [cvphysiology.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOs1slFvlPWOMRwgymAjt-yZWZvAiDlIQD4ydLnYuy3xNuP9W_Y9PD7Sq790NOwYS1zAtnivm4Uo93Gp1PGH53VEqggO4BkNnN-D7zCSFEbk0U89yjp_7S0LNcRM69kxqRM3U=)
7. [kup.at](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKuegmSemNoYfdKkGk-X495tE29hP1SFSbeD5kIs9Ho6rz4_3dlKa2d7QYU_fD6vdlUReBhGNx5ax5p4r-ddXA4ey2sk6DKIOlX5mpRvsrU0Q3rWllq8rPZw==)
8. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFxmmpfkwn0u33KyL7pkfAI5tw8a1nmdczp-dZgj6I0n2qHnQA1Yjdpol2WbldAckjnSoodj9KSXBgIhTAozkhkoLeIieEdx0YSkrSb3TkzFEBaekgXw_xvI1eMqZWlo83CRF3mFQm)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAWcy1vBGpkaBrbrb7eA0rYX4BUHT0sMxQzBw2PF8oBB4DUhQFkhLYPQhwOEvlu9jpKCPo4Sp4prkOwvUdkdA-YuF7RMJshaUlb85_n38nKl5Nh5adikDCpinAZFroYRqp1eE=)
10. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfnKN4rTayDFy1p5xXfbLv-I9mjv56UErs50zbZGp_rr8kZveei0A6pDwkWFEdxWPJnEf92meS4E7lsG9IUOdQVId7nugNkibQtwltcp0WatdPMa7_5Dr1iVHX0zmt)
11. [cvpharmacology.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTgYXcgbIsnTf_Zhr0EY0iR4G3LNL1E3rHI2u6hYMwMfmgBwbIMe5FKQep2yXlbY8ZR1Wxa4TX11g1lJ03Y-8Fe9RVnyw_B7lfy8d81sqElHRQkZooZtawg2gWyyT1QyTiZ0RyW3rcaEISidGwtIdGWJY=)
12. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWG69BUFPUJB-ZxYVmjI_TMIcT1r5UtLnx_Qogah2HwU2NZ8q9dhwnsDsmG2sR5dLdNDmITigLGkm_FuVTLJ1FDDaiZvzwaM_aOjCmpIn5SYLlGi6MenNHDrCC2w==)
13. [droracle.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9go_ED6nAMErLtxgnb3GgeJm_wkcNOPJtIn2F2sLUeBQD0iwAAS4p4BU43jKUqkxCm6I4Vbas-kx4j_VjTYHEHl-po7hSIZDoNHzYuLGjHPWACl2zrRIEztu0VD8E7C0VaXzGpM_Bb0o6GR1OSEoZgmg4AlGLMDoMljJyYESY7YL8cf-81Sx92-oBp6VUFx9Zj4R_GT9lCRaBHfBgBiaaxlTo1fJh4qlhGQ5-yw==)
14. [ccjm.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTGd-WK3VeoaNfwcWoi86J9m7grH-MKbAbRmsNZAxAJs-pc6gX1c7NAEA9htleXPjudWUCya0FxH6umZFNEDdcnsFEKQPe8iyNQhVpe1vxsi6X8mj9dFJv7qMhGO2HQpDkRLBREr8LZLFB)
15. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLo5IAl5yDUjVL2U9s5fly6V_-f0BL2GFlgYNh5GzvGQy2-KGYGtcz13iUWAQDZDTI7U5OdEbeQHB3jRknEcKRIhOgmeuXTdbt8G1nUN7j4R5SYcSQCpQspxKk-De2)
16. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFWcc9qs3gypWS_VjgwGzMnGeNeMXEP3DqROp0LxWchxKgVpvzkFdG9KY3k6aBGKV_thE7-E3irc830GDMCgbzXLkOLYyEzSVPEWPg2ZpW1INwUfACHtEKPsy4B01AxA==)
17. [revespcardiol.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtCIwL1P4YUuOFgBJDj2co84PfvOPraCcY2yvRLBksJwi_jqv5R8xUfiMcSqIOLQ-tJBH1l8olY0pTSCN5IhaP5_v7U-6AaMOZUrHwWH-lBM7lWPPgWlddVe1ZtwmTHFGgIDDuijAwn7WmjHz6Vh31HvPVKLw0wradbnSMzb7JjJ6l0VxRkD12W5DdfN_InlH4eVMT517wdkc_)
18. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZdIs_gyiE35QY5RgaxZoB9N8tw1r8SJhRGhzS_TX0vkCi-D_udbqs35yQm6obnl76hfr6W_0HzU_lS9aH1yFMzudq-2kLGHOPGLYPK_cdAbDQnbvG2cOrlj0XAyjhsgjNH_tWlYdd)
19. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGb5txRchP9Hxus316GWtA2YKGUYzYMsmrRu1zQEbRgdyPQs0yz-sG6xV3Ih37_WvHPAJiw33reJNgiYqcCmFiZOySkdxFzrp8_xmfU0jpIl841a23Icy5TWbXa9MzwWGQJIxZ-8kOT)
20. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcwLdtNt4LojI0-nNyXi-wi_H6IWMwu6XHpld-Sv-MK8UFn8TPb-OyQhvoLaoqGH4J12DCmCBZVhD0xSIMSDnmYJxo4CAWSHUUPcd7J5-oX5jaV_JIrsfrav2XbSiMez9Y)
21. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_tOB9Pz2F6fkmC7T9z7Az6r3PEA9HSxgn6ecDipN9PQzZflWPeFLl5VYVMQcTzVN6iEbXdRfyClngStsmrmGZw1ZZITdj6QJ7v8-dVJorTjaNfJ6MVmMk6VM73lNhqdPIfcmP5_PM)
22. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZ_ASbQNOjrsQ0ShCJ4y7jhJi6C73awnRHKljKZw2PMzmLS8eJ8HqsTU5Bm2Ry4_0eHLVKxgX46XT4kCS9QJJt3OWD2S7ZxP4Zy24OxpqLcypnE49YYikXREGvdQeSigJkUtfeNHNe)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJikN31AGXGH18RnD6zPY9SWjvvJRwH2bRHg7tEYM3Yc7FnDKr0NRh0OGQlfXqMjGcvxASnEanEJn1JRTQMC41wYZ32yyVDlJGxcbHxZRbgr4VaLLQQlSlmbs2Fwv8ryDlVjEdCHPzscIvt00N_5YvbxZP5UX-9z3SdQkv6Bd4c6uCvySMV9P6DZTPKcVdC2QBAK_WzbiDQo2wqgig0_en-TytkgucMjv467inopytyJpIvsWDzix-YCoQY-hzmS74fbc5hHXO1XZcP68YaWv1cspYpA==)
24. [zealjournals.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE89gOx3OF77EAm1AQ9VsyKJ2-ViEOWvWFgnXSAMzyBbjQnr6ou8sMy-fth7PdZyjWGLaS7bQcQ_53kN-uYeJiib9bhHj6-KozTtb9S8pUzMyNV2zc_DLiX03E_g3kcdTZJj9QFH5athcSeHvFYge80eGatZPu3KOjlaOC_W45cRl9RVu_Ev6OhOVzyQVb8-9weGDac_jpDJMqXyU6Cw-H5AEyF6mcdskZRsfDGohRbjQg=)
25. [jscimedcentral.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFolnlgu_lwX3vCZaCcK3Bj4k10fD02aCjNuaygDnX7QU7ZC6etoIuwgCSdkuwn-ujFruj3v0AUI3ur_fZklIoKz6XcXzqEUq0yvUojAqsh-NJDJmy-9oiNLnjw561CuMPTeYgACEJGcUx-7xN4Yig1ectZsZ3V83dIaithvWzIbUegH8q05JfvFXL6qbu0Q08NNpsv4XLicp_Rj5NSg6--VHUQqF5qaG9QmW0HamcQO7Dx3RGox8tGOqi9eUQWsZQ6Y06pRt6V8CvJO7pY6mb5rW9PyGdzU6KF8vwXXT7FiKSvTYt8vqJ-MN_nVf-pZvB7wflSuZvrPunawtnh_rwPt0wh_G9iOe-Ytfaw)
26. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGygi0XpQrrcKitIRHetIom01j3jUiEI_s60KP4ZssAYW8J4dDenbZkNxsmDeXJVMmeKVn6LT-tOlIaSFVK4Q8osP9tN3a6CpY_0x-mITXjqapQxIa3BnlquJFiomeYtw==)
27. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgrYxdTggni8N9S9a-Xm3XJDAyJCa5CHNjMd2Fop5wNGnUubBhNW_AuW4P0AZBgpMIJMN8LdWeeGWAF9GGNI1K6bNIsgNvWRDwmvukQomk2xkcbUZC0Df5VRg7bUhLJ1ENw7L7YVb8uA==)
28. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2TScpeRpr7sDAByiYxXrtEzXXDsnZwHAhJCf8EoWWYBFY-2JWdTtouVlmuDs8uHD6c6XSqu1QN-SoToA2qkjqgUnncGqyVC3Ld2KAyex7bPEf7qkiax5Llxkebl0=)
29. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYJuOwopPoPFknL7kFtTQAsurWN2EQEEJ86U-US7st4QO48gPC2CZz608CyhtCAHboBvp-mHslmQA_hXh1Io1AnUOqEsXL1KrsTY4077GwFmiNTgLenytmH3DnBCBlU57F)
30. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEj_hfvj_jXKAhCDn7tWljaQNeeTwUrO4mZxr7Lry7MZL5YZ5z54oxmlQ1KGkCT1ZgPtvbOau-7ba8p-jhgCpYg0Uudc0j84JVru5xNrX2pR7WUkVR7Cy8kAYPKl98A-N43_BIveWSu)
31. [plos.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjUd4QG5-rOUsuhbeS1lgvqE2vOqUu2xPOVAgvH6RLwCGvea9DhuJK_zYurA76COPiTGywGo9LhsWAFJ6_WrezZOTm74WpvALNJ64xS6O16EABm22ESZWl14X3Afu3RWZiY1ZQNNom9GEFek8BdCf8Oz7UbCMdhg_zJ6asyc4W)
32. [cvphysiology.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPGiqFL2AcbLwQXo85C-y-nIH52-GSgGXIbDCzdirTV1VtTBw_fLhqZR0Z-rG5dVuQAnoAeT7rw3EWQGTF3jK-g3uCNqNsQSizZ4zNXShfWOOKFNa_Yu4zGa_J5QpbigDiHIDg0Q==)
33. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJL8Uqrw6COxaKb7A5qR_TpE89P3oU3lNqqyHabasOow3JAJQ0GeRvYkHwi2fnrxG-7eIC-bB5fAxOxod_1fGeEAE71ve2k8Nzutzh7FoEtVzdgRjcIwBkd0SzRkycmxyjDEAfwnXGmA==)
34. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEo28Sw-IhlkO0F-9WBNwmTPP6qR8p19PlmyPdC2gxqUhUYeed96G6kfThYaG_SR-DgNSvkVb6MOEluhBeo0rX3w165COOqMwDp1ijLLsEbnVfInjNHqlFilLwHjzSyHWRT)
35. [ahajournals.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpwvbAn-18rkQ7SKyZ-EAnesrESlOd9R83mzSXTO7fNSphZOQPE11iRhS6Lj03WdHjuth-fgnE9mgnJFNQmjAeUhyTclFHPmejcdC1ahHV4G5rkmaRFAHKSFYDkGVJt2SmaOSWAeuP7u_bymbJ5d8WcZQ=)


## Annotations
Annotation(end_index=2232, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVr616nt6vOBehMKCX8HDUCpZqo_hwdUNEVVg43S1UAnCMSzhWaTbmaklRhATNj6HewG2MzP3h_E3FbJTzqzU1W6lgWAZI9vHkuhvesIw0bnfLHdVoNy8XlOaQVIffXcbsWGN-4_CY8xU6C5ktaR6r_Rwzqs8XUvnPj1fWRbFlNkJG6_YspLtg-HZhqguz', start_index=2220)
Annotation(end_index=2232, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhMwTPKd0FTofk416YZRSIvWmkl2MqDfmG3HM-MLmDuiORG2LyHb7R90isz9cvfxPsmQHt46I2hbP-dQq-KK4nkLw7ufniON_wcvLGACjuIxXcR2JuIouZzIJ0SSwFO2Kz5N2QhPM4wIcANw==', start_index=2220)
Annotation(end_index=2491, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnFVf4FI1CnjIKqBREbLD1tfJIwexv6qiJM8kZM8Eq3tQG277nT9K8bJgqotWuZB8e95Mxo-KoO5s19Ul_ZRVmxedd5ISHOGvr1dyOEy5evBiJMTFJ4RyYZ37Pq-axiX50XzI=', start_index=2479)
Annotation(end_index=2491, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjHcoNFvwWQyB1LQ96xfLsByOzfuk6mkR73wGb6_63tjF2dd_Zy6NrM8HI-uWiysF6mUgGvf-IpVDBLtThhUKuu4MpDaqMuZHe8NSVgXtmT8fTCEmvbs2lRqz4OtCH', start_index=2479)
Annotation(end_index=2828, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOs1slFvlPWOMRwgymAjt-yZWZvAiDlIQD4ydLnYuy3xNuP9W_Y9PD7Sq790NOwYS1zAtnivm4Uo93Gp1PGH53VEqggO4BkNnN-D7zCSFEbk0U89yjp_7S0LNcRM69kxqRM3U=', start_index=2816)
Annotation(end_index=2828, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvYH5pTPjGbTHK1dwcH2jSvmUleUYRVHFP3031aR5cxz7DJ8Qh3aT9h8TonuA1wiUzFhFhctM0eFVZDgMAa0jnW4cxP_S-0kM9NZdJX8xHffIecpOyHC94C1vsOfI=', start_index=2816)
Annotation(end_index=2969, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKuegmSemNoYfdKkGk-X495tE29hP1SFSbeD5kIs9Ho6rz4_3dlKa2d7QYU_fD6vdlUReBhGNx5ax5p4r-ddXA4ey2sk6DKIOlX5mpRvsrU0Q3rWllq8rPZw==', start_index=2960)
Annotation(end_index=3212, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFxmmpfkwn0u33KyL7pkfAI5tw8a1nmdczp-dZgj6I0n2qHnQA1Yjdpol2WbldAckjnSoodj9KSXBgIhTAozkhkoLeIieEdx0YSkrSb3TkzFEBaekgXw_xvI1eMqZWlo83CRF3mFQm', start_index=3200)
Annotation(end_index=3212, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAWcy1vBGpkaBrbrb7eA0rYX4BUHT0sMxQzBw2PF8oBB4DUhQFkhLYPQhwOEvlu9jpKCPo4Sp4prkOwvUdkdA-YuF7RMJshaUlb85_n38nKl5Nh5adikDCpinAZFroYRqp1eE=', start_index=3200)
Annotation(end_index=4210, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfnKN4rTayDFy1p5xXfbLv-I9mjv56UErs50zbZGp_rr8kZveei0A6pDwkWFEdxWPJnEf92meS4E7lsG9IUOdQVId7nugNkibQtwltcp0WatdPMa7_5Dr1iVHX0zmt', start_index=4197)
Annotation(end_index=4210, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjHcoNFvwWQyB1LQ96xfLsByOzfuk6mkR73wGb6_63tjF2dd_Zy6NrM8HI-uWiysF6mUgGvf-IpVDBLtThhUKuu4MpDaqMuZHe8NSVgXtmT8fTCEmvbs2lRqz4OtCH', start_index=4197)
Annotation(end_index=4369, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjHcoNFvwWQyB1LQ96xfLsByOzfuk6mkR73wGb6_63tjF2dd_Zy6NrM8HI-uWiysF6mUgGvf-IpVDBLtThhUKuu4MpDaqMuZHe8NSVgXtmT8fTCEmvbs2lRqz4OtCH', start_index=4360)
Annotation(end_index=4712, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAWcy1vBGpkaBrbrb7eA0rYX4BUHT0sMxQzBw2PF8oBB4DUhQFkhLYPQhwOEvlu9jpKCPo4Sp4prkOwvUdkdA-YuF7RMJshaUlb85_n38nKl5Nh5adikDCpinAZFroYRqp1eE=', start_index=4700)
Annotation(end_index=4712, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhMwTPKd0FTofk416YZRSIvWmkl2MqDfmG3HM-MLmDuiORG2LyHb7R90isz9cvfxPsmQHt46I2hbP-dQq-KK4nkLw7ufniON_wcvLGACjuIxXcR2JuIouZzIJ0SSwFO2Kz5N2QhPM4wIcANw==', start_index=4700)
Annotation(end_index=5051, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTgYXcgbIsnTf_Zhr0EY0iR4G3LNL1E3rHI2u6hYMwMfmgBwbIMe5FKQep2yXlbY8ZR1Wxa4TX11g1lJ03Y-8Fe9RVnyw_B7lfy8d81sqElHRQkZooZtawg2gWyyT1QyTiZ0RyW3rcaEISidGwtIdGWJY=', start_index=5038)
Annotation(end_index=5051, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhMwTPKd0FTofk416YZRSIvWmkl2MqDfmG3HM-MLmDuiORG2LyHb7R90isz9cvfxPsmQHt46I2hbP-dQq-KK4nkLw7ufniON_wcvLGACjuIxXcR2JuIouZzIJ0SSwFO2Kz5N2QhPM4wIcANw==', start_index=5038)
Annotation(end_index=5493, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWG69BUFPUJB-ZxYVmjI_TMIcT1r5UtLnx_Qogah2HwU2NZ8q9dhwnsDsmG2sR5dLdNDmITigLGkm_FuVTLJ1FDDaiZvzwaM_aOjCmpIn5SYLlGi6MenNHDrCC2w==', start_index=5477)
Annotation(end_index=5493, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAWcy1vBGpkaBrbrb7eA0rYX4BUHT0sMxQzBw2PF8oBB4DUhQFkhLYPQhwOEvlu9jpKCPo4Sp4prkOwvUdkdA-YuF7RMJshaUlb85_n38nKl5Nh5adikDCpinAZFroYRqp1eE=', start_index=5477)
Annotation(end_index=5493, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvYH5pTPjGbTHK1dwcH2jSvmUleUYRVHFP3031aR5cxz7DJ8Qh3aT9h8TonuA1wiUzFhFhctM0eFVZDgMAa0jnW4cxP_S-0kM9NZdJX8xHffIecpOyHC94C1vsOfI=', start_index=5477)
Annotation(end_index=5930, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9go_ED6nAMErLtxgnb3GgeJm_wkcNOPJtIn2F2sLUeBQD0iwAAS4p4BU43jKUqkxCm6I4Vbas-kx4j_VjTYHEHl-po7hSIZDoNHzYuLGjHPWACl2zrRIEztu0VD8E7C0VaXzGpM_Bb0o6GR1OSEoZgmg4AlGLMDoMljJyYESY7YL8cf-81Sx92-oBp6VUFx9Zj4R_GT9lCRaBHfBgBiaaxlTo1fJh4qlhGQ5-yw==', start_index=5913)
Annotation(end_index=5930, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTGd-WK3VeoaNfwcWoi86J9m7grH-MKbAbRmsNZAxAJs-pc6gX1c7NAEA9htleXPjudWUCya0FxH6umZFNEDdcnsFEKQPe8iyNQhVpe1vxsi6X8mj9dFJv7qMhGO2HQpDkRLBREr8LZLFB', start_index=5913)
Annotation(end_index=5930, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKuegmSemNoYfdKkGk-X495tE29hP1SFSbeD5kIs9Ho6rz4_3dlKa2d7QYU_fD6vdlUReBhGNx5ax5p4r-ddXA4ey2sk6DKIOlX5mpRvsrU0Q3rWllq8rPZw==', start_index=5913)
Annotation(end_index=6373, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtCIwL1P4YUuOFgBJDj2co84PfvOPraCcY2yvRLBksJwi_jqv5R8xUfiMcSqIOLQ-tJBH1l8olY0pTSCN5IhaP5_v7U-6AaMOZUrHwWH-lBM7lWPPgWlddVe1ZtwmTHFGgIDDuijAwn7WmjHz6Vh31HvPVKLw0wradbnSMzb7JjJ6l0VxRkD12W5DdfN_InlH4eVMT517wdkc_', start_index=6355)
Annotation(end_index=6373, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFWcc9qs3gypWS_VjgwGzMnGeNeMXEP3DqROp0LxWchxKgVpvzkFdG9KY3k6aBGKV_thE7-E3irc830GDMCgbzXLkOLYyEzSVPEWPg2ZpW1INwUfACHtEKPsy4B01AxA==', start_index=6355)
Annotation(end_index=6373, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLo5IAl5yDUjVL2U9s5fly6V_-f0BL2GFlgYNh5GzvGQy2-KGYGtcz13iUWAQDZDTI7U5OdEbeQHB3jRknEcKRIhOgmeuXTdbt8G1nUN7j4R5SYcSQCpQspxKk-De2', start_index=6355)
Annotation(end_index=6753, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhMwTPKd0FTofk416YZRSIvWmkl2MqDfmG3HM-MLmDuiORG2LyHb7R90isz9cvfxPsmQHt46I2hbP-dQq-KK4nkLw7ufniON_wcvLGACjuIxXcR2JuIouZzIJ0SSwFO2Kz5N2QhPM4wIcANw==', start_index=6741)
Annotation(end_index=6753, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOs1slFvlPWOMRwgymAjt-yZWZvAiDlIQD4ydLnYuy3xNuP9W_Y9PD7Sq790NOwYS1zAtnivm4Uo93Gp1PGH53VEqggO4BkNnN-D7zCSFEbk0U89yjp_7S0LNcRM69kxqRM3U=', start_index=6741)
Annotation(end_index=7216, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFxmmpfkwn0u33KyL7pkfAI5tw8a1nmdczp-dZgj6I0n2qHnQA1Yjdpol2WbldAckjnSoodj9KSXBgIhTAozkhkoLeIieEdx0YSkrSb3TkzFEBaekgXw_xvI1eMqZWlo83CRF3mFQm', start_index=7203)
Annotation(end_index=7216, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZdIs_gyiE35QY5RgaxZoB9N8tw1r8SJhRGhzS_TX0vkCi-D_udbqs35yQm6obnl76hfr6W_0HzU_lS9aH1yFMzudq-2kLGHOPGLYPK_cdAbDQnbvG2cOrlj0XAyjhsgjNH_tWlYdd', start_index=7203)
Annotation(end_index=7681, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFxmmpfkwn0u33KyL7pkfAI5tw8a1nmdczp-dZgj6I0n2qHnQA1Yjdpol2WbldAckjnSoodj9KSXBgIhTAozkhkoLeIieEdx0YSkrSb3TkzFEBaekgXw_xvI1eMqZWlo83CRF3mFQm', start_index=7668)
Annotation(end_index=7681, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGb5txRchP9Hxus316GWtA2YKGUYzYMsmrRu1zQEbRgdyPQs0yz-sG6xV3Ih37_WvHPAJiw33reJNgiYqcCmFiZOySkdxFzrp8_xmfU0jpIl841a23Icy5TWbXa9MzwWGQJIxZ-8kOT', start_index=7668)
Annotation(end_index=8078, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFxmmpfkwn0u33KyL7pkfAI5tw8a1nmdczp-dZgj6I0n2qHnQA1Yjdpol2WbldAckjnSoodj9KSXBgIhTAozkhkoLeIieEdx0YSkrSb3TkzFEBaekgXw_xvI1eMqZWlo83CRF3mFQm', start_index=8065)
Annotation(end_index=8078, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZdIs_gyiE35QY5RgaxZoB9N8tw1r8SJhRGhzS_TX0vkCi-D_udbqs35yQm6obnl76hfr6W_0HzU_lS9aH1yFMzudq-2kLGHOPGLYPK_cdAbDQnbvG2cOrlj0XAyjhsgjNH_tWlYdd', start_index=8065)
Annotation(end_index=8703, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWG69BUFPUJB-ZxYVmjI_TMIcT1r5UtLnx_Qogah2HwU2NZ8q9dhwnsDsmG2sR5dLdNDmITigLGkm_FuVTLJ1FDDaiZvzwaM_aOjCmpIn5SYLlGi6MenNHDrCC2w==', start_index=8690)
Annotation(end_index=8703, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvYH5pTPjGbTHK1dwcH2jSvmUleUYRVHFP3031aR5cxz7DJ8Qh3aT9h8TonuA1wiUzFhFhctM0eFVZDgMAa0jnW4cxP_S-0kM9NZdJX8xHffIecpOyHC94C1vsOfI=', start_index=8690)
Annotation(end_index=8907, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcwLdtNt4LojI0-nNyXi-wi_H6IWMwu6XHpld-Sv-MK8UFn8TPb-OyQhvoLaoqGH4J12DCmCBZVhD0xSIMSDnmYJxo4CAWSHUUPcd7J5-oX5jaV_JIrsfrav2XbSiMez9Y', start_index=8897)
Annotation(end_index=9442, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKuegmSemNoYfdKkGk-X495tE29hP1SFSbeD5kIs9Ho6rz4_3dlKa2d7QYU_fD6vdlUReBhGNx5ax5p4r-ddXA4ey2sk6DKIOlX5mpRvsrU0Q3rWllq8rPZw==', start_index=9429)
Annotation(end_index=9442, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLo5IAl5yDUjVL2U9s5fly6V_-f0BL2GFlgYNh5GzvGQy2-KGYGtcz13iUWAQDZDTI7U5OdEbeQHB3jRknEcKRIhOgmeuXTdbt8G1nUN7j4R5SYcSQCpQspxKk-De2', start_index=9429)
Annotation(end_index=9638, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtCIwL1P4YUuOFgBJDj2co84PfvOPraCcY2yvRLBksJwi_jqv5R8xUfiMcSqIOLQ-tJBH1l8olY0pTSCN5IhaP5_v7U-6AaMOZUrHwWH-lBM7lWPPgWlddVe1ZtwmTHFGgIDDuijAwn7WmjHz6Vh31HvPVKLw0wradbnSMzb7JjJ6l0VxRkD12W5DdfN_InlH4eVMT517wdkc_', start_index=9624)
Annotation(end_index=9638, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFWcc9qs3gypWS_VjgwGzMnGeNeMXEP3DqROp0LxWchxKgVpvzkFdG9KY3k6aBGKV_thE7-E3irc830GDMCgbzXLkOLYyEzSVPEWPg2ZpW1INwUfACHtEKPsy4B01AxA==', start_index=9624)
Annotation(end_index=10576, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhMwTPKd0FTofk416YZRSIvWmkl2MqDfmG3HM-MLmDuiORG2LyHb7R90isz9cvfxPsmQHt46I2hbP-dQq-KK4nkLw7ufniON_wcvLGACjuIxXcR2JuIouZzIJ0SSwFO2Kz5N2QhPM4wIcANw==', start_index=10563)
Annotation(end_index=10576, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_tOB9Pz2F6fkmC7T9z7Az6r3PEA9HSxgn6ecDipN9PQzZflWPeFLl5VYVMQcTzVN6iEbXdRfyClngStsmrmGZw1ZZITdj6QJ7v8-dVJorTjaNfJ6MVmMk6VM73lNhqdPIfcmP5_PM', start_index=10563)
Annotation(end_index=10778, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZ_ASbQNOjrsQ0ShCJ4y7jhJi6C73awnRHKljKZw2PMzmLS8eJ8HqsTU5Bm2Ry4_0eHLVKxgX46XT4kCS9QJJt3OWD2S7ZxP4Zy24OxpqLcypnE49YYikXREGvdQeSigJkUtfeNHNe', start_index=10768)
Annotation(end_index=11228, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE89gOx3OF77EAm1AQ9VsyKJ2-ViEOWvWFgnXSAMzyBbjQnr6ou8sMy-fth7PdZyjWGLaS7bQcQ_53kN-uYeJiib9bhHj6-KozTtb9S8pUzMyNV2zc_DLiX03E_g3kcdTZJj9QFH5athcSeHvFYge80eGatZPu3KOjlaOC_W45cRl9RVu_Ev6OhOVzyQVb8-9weGDac_jpDJMqXyU6Cw-H5AEyF6mcdskZRsfDGohRbjQg=', start_index=11210)
Annotation(end_index=11228, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_tOB9Pz2F6fkmC7T9z7Az6r3PEA9HSxgn6ecDipN9PQzZflWPeFLl5VYVMQcTzVN6iEbXdRfyClngStsmrmGZw1ZZITdj6QJ7v8-dVJorTjaNfJ6MVmMk6VM73lNhqdPIfcmP5_PM', start_index=11210)
Annotation(end_index=11228, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJikN31AGXGH18RnD6zPY9SWjvvJRwH2bRHg7tEYM3Yc7FnDKr0NRh0OGQlfXqMjGcvxASnEanEJn1JRTQMC41wYZ32yyVDlJGxcbHxZRbgr4VaLLQQlSlmbs2Fwv8ryDlVjEdCHPzscIvt00N_5YvbxZP5UX-9z3SdQkv6Bd4c6uCvySMV9P6DZTPKcVdC2QBAK_WzbiDQo2wqgig0_en-TytkgucMjv467inopytyJpIvsWDzix-YCoQY-hzmS74fbc5hHXO1XZcP68YaWv1cspYpA==', start_index=11210)
Annotation(end_index=11607, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFolnlgu_lwX3vCZaCcK3Bj4k10fD02aCjNuaygDnX7QU7ZC6etoIuwgCSdkuwn-ujFruj3v0AUI3ur_fZklIoKz6XcXzqEUq0yvUojAqsh-NJDJmy-9oiNLnjw561CuMPTeYgACEJGcUx-7xN4Yig1ectZsZ3V83dIaithvWzIbUegH8q05JfvFXL6qbu0Q08NNpsv4XLicp_Rj5NSg6--VHUQqF5qaG9QmW0HamcQO7Dx3RGox8tGOqi9eUQWsZQ6Y06pRt6V8CvJO7pY6mb5rW9PyGdzU6KF8vwXXT7FiKSvTYt8vqJ-MN_nVf-pZvB7wflSuZvrPunawtnh_rwPt0wh_G9iOe-Ytfaw', start_index=11593)
Annotation(end_index=11607, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_tOB9Pz2F6fkmC7T9z7Az6r3PEA9HSxgn6ecDipN9PQzZflWPeFLl5VYVMQcTzVN6iEbXdRfyClngStsmrmGZw1ZZITdj6QJ7v8-dVJorTjaNfJ6MVmMk6VM73lNhqdPIfcmP5_PM', start_index=11593)
Annotation(end_index=11873, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgrYxdTggni8N9S9a-Xm3XJDAyJCa5CHNjMd2Fop5wNGnUubBhNW_AuW4P0AZBgpMIJMN8LdWeeGWAF9GGNI1K6bNIsgNvWRDwmvukQomk2xkcbUZC0Df5VRg7bUhLJ1ENw7L7YVb8uA==', start_index=11859)
Annotation(end_index=11873, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGygi0XpQrrcKitIRHetIom01j3jUiEI_s60KP4ZssAYW8J4dDenbZkNxsmDeXJVMmeKVn6LT-tOlIaSFVK4Q8osP9tN3a6CpY_0x-mITXjqapQxIa3BnlquJFiomeYtw==', start_index=11859)
Annotation(end_index=12426, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2TScpeRpr7sDAByiYxXrtEzXXDsnZwHAhJCf8EoWWYBFY-2JWdTtouVlmuDs8uHD6c6XSqu1QN-SoToA2qkjqgUnncGqyVC3Ld2KAyex7bPEf7qkiax5Llxkebl0=', start_index=12412)
Annotation(end_index=12426, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYJuOwopPoPFknL7kFtTQAsurWN2EQEEJ86U-US7st4QO48gPC2CZz608CyhtCAHboBvp-mHslmQA_hXh1Io1AnUOqEsXL1KrsTY4077GwFmiNTgLenytmH3DnBCBlU57F', start_index=12412)
Annotation(end_index=12838, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEj_hfvj_jXKAhCDn7tWljaQNeeTwUrO4mZxr7Lry7MZL5YZ5z54oxmlQ1KGkCT1ZgPtvbOau-7ba8p-jhgCpYg0Uudc0j84JVru5xNrX2pR7WUkVR7Cy8kAYPKl98A-N43_BIveWSu', start_index=12824)
Annotation(end_index=12838, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjUd4QG5-rOUsuhbeS1lgvqE2vOqUu2xPOVAgvH6RLwCGvea9DhuJK_zYurA76COPiTGywGo9LhsWAFJ6_WrezZOTm74WpvALNJ64xS6O16EABm22ESZWl14X3Afu3RWZiY1ZQNNom9GEFek8BdCf8Oz7UbCMdhg_zJ6asyc4W', start_index=12824)
Annotation(end_index=13296, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2TScpeRpr7sDAByiYxXrtEzXXDsnZwHAhJCf8EoWWYBFY-2JWdTtouVlmuDs8uHD6c6XSqu1QN-SoToA2qkjqgUnncGqyVC3Ld2KAyex7bPEf7qkiax5Llxkebl0=', start_index=13286)
Annotation(end_index=13859, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPGiqFL2AcbLwQXo85C-y-nIH52-GSgGXIbDCzdirTV1VtTBw_fLhqZR0Z-rG5dVuQAnoAeT7rw3EWQGTF3jK-g3uCNqNsQSizZ4zNXShfWOOKFNa_Yu4zGa_J5QpbigDiHIDg0Q==', start_index=13846)
Annotation(end_index=13859, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjHcoNFvwWQyB1LQ96xfLsByOzfuk6mkR73wGb6_63tjF2dd_Zy6NrM8HI-uWiysF6mUgGvf-IpVDBLtThhUKuu4MpDaqMuZHe8NSVgXtmT8fTCEmvbs2lRqz4OtCH', start_index=13846)
Annotation(end_index=14185, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEo28Sw-IhlkO0F-9WBNwmTPP6qR8p19PlmyPdC2gxqUhUYeed96G6kfThYaG_SR-DgNSvkVb6MOEluhBeo0rX3w165COOqMwDp1ijLLsEbnVfInjNHqlFilLwHjzSyHWRT', start_index=14171)
Annotation(end_index=14185, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJL8Uqrw6COxaKb7A5qR_TpE89P3oU3lNqqyHabasOow3JAJQ0GeRvYkHwi2fnrxG-7eIC-bB5fAxOxod_1fGeEAE71ve2k8Nzutzh7FoEtVzdgRjcIwBkd0SzRkycmxyjDEAfwnXGmA==', start_index=14171)
Annotation(end_index=14770, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpwvbAn-18rkQ7SKyZ-EAnesrESlOd9R83mzSXTO7fNSphZOQPE11iRhS6Lj03WdHjuth-fgnE9mgnJFNQmjAeUhyTclFHPmejcdC1ahHV4G5rkmaRFAHKSFYDkGVJt2SmaOSWAeuP7u_bymbJ5d8WcZQ=', start_index=14753)
Annotation(end_index=14770, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZdIs_gyiE35QY5RgaxZoB9N8tw1r8SJhRGhzS_TX0vkCi-D_udbqs35yQm6obnl76hfr6W_0HzU_lS9aH1yFMzudq-2kLGHOPGLYPK_cdAbDQnbvG2cOrlj0XAyjhsgjNH_tWlYdd', start_index=14753)
Annotation(end_index=14770, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvYH5pTPjGbTHK1dwcH2jSvmUleUYRVHFP3031aR5cxz7DJ8Qh3aT9h8TonuA1wiUzFhFhctM0eFVZDgMAa0jnW4cxP_S-0kM9NZdJX8xHffIecpOyHC94C1vsOfI=', start_index=14753)
Annotation(end_index=15912, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZdIs_gyiE35QY5RgaxZoB9N8tw1r8SJhRGhzS_TX0vkCi-D_udbqs35yQm6obnl76hfr6W_0HzU_lS9aH1yFMzudq-2kLGHOPGLYPK_cdAbDQnbvG2cOrlj0XAyjhsgjNH_tWlYdd', start_index=15902)
Annotation(end_index=16033, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpwvbAn-18rkQ7SKyZ-EAnesrESlOd9R83mzSXTO7fNSphZOQPE11iRhS6Lj03WdHjuth-fgnE9mgnJFNQmjAeUhyTclFHPmejcdC1ahHV4G5rkmaRFAHKSFYDkGVJt2SmaOSWAeuP7u_bymbJ5d8WcZQ=', start_index=16023)
Annotation(end_index=16124, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9go_ED6nAMErLtxgnb3GgeJm_wkcNOPJtIn2F2sLUeBQD0iwAAS4p4BU43jKUqkxCm6I4Vbas-kx4j_VjTYHEHl-po7hSIZDoNHzYuLGjHPWACl2zrRIEztu0VD8E7C0VaXzGpM_Bb0o6GR1OSEoZgmg4AlGLMDoMljJyYESY7YL8cf-81Sx92-oBp6VUFx9Zj4R_GT9lCRaBHfBgBiaaxlTo1fJh4qlhGQ5-yw==', start_index=16114)
Annotation(end_index=16240, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFxmmpfkwn0u33KyL7pkfAI5tw8a1nmdczp-dZgj6I0n2qHnQA1Yjdpol2WbldAckjnSoodj9KSXBgIhTAozkhkoLeIieEdx0YSkrSb3TkzFEBaekgXw_xvI1eMqZWlo83CRF3mFQm', start_index=16231)
Annotation(end_index=16352, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZ_ASbQNOjrsQ0ShCJ4y7jhJi6C73awnRHKljKZw2PMzmLS8eJ8HqsTU5Bm2Ry4_0eHLVKxgX46XT4kCS9QJJt3OWD2S7ZxP4Zy24OxpqLcypnE49YYikXREGvdQeSigJkUtfeNHNe', start_index=16342)
Annotation(end_index=16485, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTgYXcgbIsnTf_Zhr0EY0iR4G3LNL1E3rHI2u6hYMwMfmgBwbIMe5FKQep2yXlbY8ZR1Wxa4TX11g1lJ03Y-8Fe9RVnyw_B7lfy8d81sqElHRQkZooZtawg2gWyyT1QyTiZ0RyW3rcaEISidGwtIdGWJY=', start_index=16475)
Annotation(end_index=16547, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAWcy1vBGpkaBrbrb7eA0rYX4BUHT0sMxQzBw2PF8oBB4DUhQFkhLYPQhwOEvlu9jpKCPo4Sp4prkOwvUdkdA-YuF7RMJshaUlb85_n38nKl5Nh5adikDCpinAZFroYRqp1eE=', start_index=16538)
Annotation(end_index=16602, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPGiqFL2AcbLwQXo85C-y-nIH52-GSgGXIbDCzdirTV1VtTBw_fLhqZR0Z-rG5dVuQAnoAeT7rw3EWQGTF3jK-g3uCNqNsQSizZ4zNXShfWOOKFNa_Yu4zGa_J5QpbigDiHIDg0Q==', start_index=16592)
Annotation(end_index=16657, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvYH5pTPjGbTHK1dwcH2jSvmUleUYRVHFP3031aR5cxz7DJ8Qh3aT9h8TonuA1wiUzFhFhctM0eFVZDgMAa0jnW4cxP_S-0kM9NZdJX8xHffIecpOyHC94C1vsOfI=', start_index=16648)
Annotation(end_index=16701, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcwLdtNt4LojI0-nNyXi-wi_H6IWMwu6XHpld-Sv-MK8UFn8TPb-OyQhvoLaoqGH4J12DCmCBZVhD0xSIMSDnmYJxo4CAWSHUUPcd7J5-oX5jaV_JIrsfrav2XbSiMez9Y', start_index=16691)
Annotation(end_index=16783, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLo5IAl5yDUjVL2U9s5fly6V_-f0BL2GFlgYNh5GzvGQy2-KGYGtcz13iUWAQDZDTI7U5OdEbeQHB3jRknEcKRIhOgmeuXTdbt8G1nUN7j4R5SYcSQCpQspxKk-De2', start_index=16773)
Annotation(end_index=16860, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTGd-WK3VeoaNfwcWoi86J9m7grH-MKbAbRmsNZAxAJs-pc6gX1c7NAEA9htleXPjudWUCya0FxH6umZFNEDdcnsFEKQPe8iyNQhVpe1vxsi6X8mj9dFJv7qMhGO2HQpDkRLBREr8LZLFB', start_index=16850)
Annotation(end_index=16975, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEj_hfvj_jXKAhCDn7tWljaQNeeTwUrO4mZxr7Lry7MZL5YZ5z54oxmlQ1KGkCT1ZgPtvbOau-7ba8p-jhgCpYg0Uudc0j84JVru5xNrX2pR7WUkVR7Cy8kAYPKl98A-N43_BIveWSu', start_index=16965)
Annotation(end_index=17100, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2TScpeRpr7sDAByiYxXrtEzXXDsnZwHAhJCf8EoWWYBFY-2JWdTtouVlmuDs8uHD6c6XSqu1QN-SoToA2qkjqgUnncGqyVC3Ld2KAyex7bPEf7qkiax5Llxkebl0=', start_index=17090)
Annotation(end_index=17195, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_tOB9Pz2F6fkmC7T9z7Az6r3PEA9HSxgn6ecDipN9PQzZflWPeFLl5VYVMQcTzVN6iEbXdRfyClngStsmrmGZw1ZZITdj6QJ7v8-dVJorTjaNfJ6MVmMk6VM73lNhqdPIfcmP5_PM', start_index=17185)
Annotation(end_index=17299, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJikN31AGXGH18RnD6zPY9SWjvvJRwH2bRHg7tEYM3Yc7FnDKr0NRh0OGQlfXqMjGcvxASnEanEJn1JRTQMC41wYZ32yyVDlJGxcbHxZRbgr4VaLLQQlSlmbs2Fwv8ryDlVjEdCHPzscIvt00N_5YvbxZP5UX-9z3SdQkv6Bd4c6uCvySMV9P6DZTPKcVdC2QBAK_WzbiDQo2wqgig0_en-TytkgucMjv467inopytyJpIvsWDzix-YCoQY-hzmS74fbc5hHXO1XZcP68YaWv1cspYpA==', start_index=17289)
Annotation(end_index=17409, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGygi0XpQrrcKitIRHetIom01j3jUiEI_s60KP4ZssAYW8J4dDenbZkNxsmDeXJVMmeKVn6LT-tOlIaSFVK4Q8osP9tN3a6CpY_0x-mITXjqapQxIa3BnlquJFiomeYtw==', start_index=17399)
Annotation(end_index=17517, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE89gOx3OF77EAm1AQ9VsyKJ2-ViEOWvWFgnXSAMzyBbjQnr6ou8sMy-fth7PdZyjWGLaS7bQcQ_53kN-uYeJiib9bhHj6-KozTtb9S8pUzMyNV2zc_DLiX03E_g3kcdTZJj9QFH5athcSeHvFYge80eGatZPu3KOjlaOC_W45cRl9RVu_Ev6OhOVzyQVb8-9weGDac_jpDJMqXyU6Cw-H5AEyF6mcdskZRsfDGohRbjQg=', start_index=17507)
Annotation(end_index=17619, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKuegmSemNoYfdKkGk-X495tE29hP1SFSbeD5kIs9Ho6rz4_3dlKa2d7QYU_fD6vdlUReBhGNx5ax5p4r-ddXA4ey2sk6DKIOlX5mpRvsrU0Q3rWllq8rPZw==', start_index=17610)
Annotation(end_index=17731, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFWcc9qs3gypWS_VjgwGzMnGeNeMXEP3DqROp0LxWchxKgVpvzkFdG9KY3k6aBGKV_thE7-E3irc830GDMCgbzXLkOLYyEzSVPEWPg2ZpW1INwUfACHtEKPsy4B01AxA==', start_index=17721)
Annotation(end_index=17844, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtCIwL1P4YUuOFgBJDj2co84PfvOPraCcY2yvRLBksJwi_jqv5R8xUfiMcSqIOLQ-tJBH1l8olY0pTSCN5IhaP5_v7U-6AaMOZUrHwWH-lBM7lWPPgWlddVe1ZtwmTHFGgIDDuijAwn7WmjHz6Vh31HvPVKLw0wradbnSMzb7JjJ6l0VxRkD12W5DdfN_InlH4eVMT517wdkc_', start_index=17834)
Annotation(end_index=17939, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjHcoNFvwWQyB1LQ96xfLsByOzfuk6mkR73wGb6_63tjF2dd_Zy6NrM8HI-uWiysF6mUgGvf-IpVDBLtThhUKuu4MpDaqMuZHe8NSVgXtmT8fTCEmvbs2lRqz4OtCH', start_index=17930)
Annotation(end_index=18025, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGb5txRchP9Hxus316GWtA2YKGUYzYMsmrRu1zQEbRgdyPQs0yz-sG6xV3Ih37_WvHPAJiw33reJNgiYqcCmFiZOySkdxFzrp8_xmfU0jpIl841a23Icy5TWbXa9MzwWGQJIxZ-8kOT', start_index=18015)
Annotation(end_index=18122, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfnKN4rTayDFy1p5xXfbLv-I9mjv56UErs50zbZGp_rr8kZveei0A6pDwkWFEdxWPJnEf92meS4E7lsG9IUOdQVId7nugNkibQtwltcp0WatdPMa7_5Dr1iVHX0zmt', start_index=18112)
Annotation(end_index=18238, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVr616nt6vOBehMKCX8HDUCpZqo_hwdUNEVVg43S1UAnCMSzhWaTbmaklRhATNj6HewG2MzP3h_E3FbJTzqzU1W6lgWAZI9vHkuhvesIw0bnfLHdVoNy8XlOaQVIffXcbsWGN-4_CY8xU6C5ktaR6r_Rwzqs8XUvnPj1fWRbFlNkJG6_YspLtg-HZhqguz', start_index=18229)
Annotation(end_index=18340, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhMwTPKd0FTofk416YZRSIvWmkl2MqDfmG3HM-MLmDuiORG2LyHb7R90isz9cvfxPsmQHt46I2hbP-dQq-KK4nkLw7ufniON_wcvLGACjuIxXcR2JuIouZzIJ0SSwFO2Kz5N2QhPM4wIcANw==', start_index=18331)
Annotation(end_index=18442, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnFVf4FI1CnjIKqBREbLD1tfJIwexv6qiJM8kZM8Eq3tQG277nT9K8bJgqotWuZB8e95Mxo-KoO5s19Ul_ZRVmxedd5ISHOGvr1dyOEy5evBiJMTFJ4RyYZ37Pq-axiX50XzI=', start_index=18433)
Annotation(end_index=18507, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOs1slFvlPWOMRwgymAjt-yZWZvAiDlIQD4ydLnYuy3xNuP9W_Y9PD7Sq790NOwYS1zAtnivm4Uo93Gp1PGH53VEqggO4BkNnN-D7zCSFEbk0U89yjp_7S0LNcRM69kxqRM3U=', start_index=18498)
Annotation(end_index=18590, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFolnlgu_lwX3vCZaCcK3Bj4k10fD02aCjNuaygDnX7QU7ZC6etoIuwgCSdkuwn-ujFruj3v0AUI3ur_fZklIoKz6XcXzqEUq0yvUojAqsh-NJDJmy-9oiNLnjw561CuMPTeYgACEJGcUx-7xN4Yig1ectZsZ3V83dIaithvWzIbUegH8q05JfvFXL6qbu0Q08NNpsv4XLicp_Rj5NSg6--VHUQqF5qaG9QmW0HamcQO7Dx3RGox8tGOqi9eUQWsZQ6Y06pRt6V8CvJO7pY6mb5rW9PyGdzU6KF8vwXXT7FiKSvTYt8vqJ-MN_nVf-pZvB7wflSuZvrPunawtnh_rwPt0wh_G9iOe-Ytfaw', start_index=18580)
Annotation(end_index=18722, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgrYxdTggni8N9S9a-Xm3XJDAyJCa5CHNjMd2Fop5wNGnUubBhNW_AuW4P0AZBgpMIJMN8LdWeeGWAF9GGNI1K6bNIsgNvWRDwmvukQomk2xkcbUZC0Df5VRg7bUhLJ1ENw7L7YVb8uA==', start_index=18712)

## Sources
