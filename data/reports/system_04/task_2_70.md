# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 42ce7e1f | **Time:** 294.09s | **Cost:** $1.72618
--------------------------------------------------------------------------------

# Pharmacokinetic Optimization of Novel Antibiotics: Balancing Clearance Half-Life and Accumulation Toxicity Thresholds

### Key Points
*   **The Central Trade-off:** Antibiotic development faces a critical tension between maintaining sufficient plasma half-life ($t_{1/2}$) for therapeutic efficacy and preventing excessive tissue accumulation that triggers toxicity thresholds.
*   **Novel Chemical Strategies:** "Soft drug" design (e.g., MRX-8) utilizes metabolically labile ester linkages to ensure rapid deactivation after therapeutic action, decoupling systemic efficacy from tissue toxicity.
*   **Trojan Horse Mechanisms:** Siderophore-cephalosporins (e.g., cefiderocol) exploit bacterial iron transport systems to enhance periplasmic accumulation without relying on high systemic concentrations that drive host toxicity.
*   **Transporter-Targeted Design:** Next-generation aminoglycosides and polymyxins are being engineered with reduced cationic charge to lower affinity for renal transporters like megalin, thereby reducing nephrotoxic uptake while maintaining antimicrobial potency.
*   **Advanced Modeling:** Physiologically Based Pharmacokinetic (PBPK) modeling has become indispensable for predicting tissue-specific accumulation and optimizing dosing regimens before clinical trials, particularly for special populations.

### Introduction
The optimization of pharmacokinetics (PK) in novel antibiotic development is a complex multidimensional challenge that requires balancing the duration of drug exposure necessary for bacterial eradication against the risks of host toxicity caused by drug accumulation. Traditionally, a longer elimination half-life ($t_{1/2}$) was viewed as advantageous for patient compliance and maintaining time-dependent pharmacodynamic (PD) indices. However, for drug classes with narrow therapeutic indices—such as polymyxins and aminoglycosides—extended residence time often correlates with saturation of uptake transporters in the kidney and inner ear, leading to dose-limiting nephrotoxicity and ototoxicity.

Modern strategies to resolve this conflict involve a tripartite approach: (1) **Medicinal Chemistry**, utilizing soft drug design and charge modulation to alter tissue distribution; (2) **Dosing Regimen Optimization**, employing extended intervals or continuous infusions to maximize bacterial killing while respecting host toxicity thresholds; and (3) **Computational Modeling**, specifically PBPK, to simulate tissue-level exposure. This report provides an exhaustive analysis of these strategies, synthesizing current research on how novel antibiotics are optimized to navigate the narrow window between clearance and accumulation toxicity.

---

## 1. Fundamentals of Antibiotic PK/PD Optimization

To understand how novel antibiotics are optimized, one must first establish the relationship between pharmacokinetic parameters and pharmacodynamic targets. The goal is to maximize the probability of target attainment (PTA) while minimizing the probability of toxicity.

### 1.1 Pharmacokinetic Parameters Defining Exposure
Pharmacokinetics describes the time course of drug concentration in body fluids resulting from absorption, distribution, metabolism, and excretion (ADME) [cite: 1, 2].
*   **Clearance (CL) and Half-life ($t_{1/2}$):** The elimination half-life is the time required for plasma concentration to decrease by 50%, determined by the volume of distribution ($V_d$) and clearance ($t_{1/2} = 0.693 \times V_d / CL$) [cite: 2, 3]. While a longer $t_{1/2}$ allows for less frequent dosing, it increases the risk of accumulation if the dosing interval is shorter than 4–5 half-lives [cite: 2].
*   **Volume of Distribution ($V_d$):** This parameter reflects the extent of drug distribution into tissues. Hydrophilic antibiotics (e.g., beta-lactams, aminoglycosides) typically have a low $V_d$ ($<0.3$ L/kg), restricted to extracellular fluid, whereas lipophilic drugs (e.g., fluoroquinolones) have high $V_d$, indicating extensive tissue penetration [cite: 2, 4].
*   **Area Under the Curve (AUC):** The AUC represents total drug exposure over time. For many antibiotics, toxicity is driven by the total AUC (cumulative exposure) rather than peak concentration ($C_{max}$) [cite: 1, 5].

### 1.2 Pharmacodynamic Indices for Efficacy
Antibiotics are categorized by the PK/PD index that best predicts bacterial killing [cite: 1, 5, 6]:
1.  **Time-Dependent ($fT > MIC$):** Efficacy depends on the time free drug concentration exceeds the Minimum Inhibitory Concentration (MIC). Examples: Beta-lactams. Optimization focuses on maintaining levels above MIC for 40–100% of the dosing interval [cite: 5, 7].
2.  **Concentration-Dependent ($C_{max}/MIC$):** Efficacy is driven by high peak concentrations. Examples: Aminoglycosides. Optimization focuses on maximizing the peak to achieve rapid bactericidal activity [cite: 5, 8].
3.  **Exposure-Dependent ($AUC/MIC$):** Efficacy depends on the total exposure relative to pathogen susceptibility. Examples: Vancomycin, Fluoroquinolones [cite: 1, 5].

### 1.3 The Toxicity Threshold Dilemma
The optimization challenge arises because the mechanisms driving efficacy often overlap with those driving toxicity. For instance, increasing the dose of an aminoglycoside to maximize $C_{max}/MIC$ enhances bacterial killing but may saturate renal megalin transporters, leading to accumulation in proximal tubule cells and subsequent necrosis [cite: 9, 10]. Similarly, extending the infusion of beta-lactams to improve $fT > MIC$ can lead to sustained high trough levels, which are associated with neurotoxicity (e.g., seizures with cefepime/imipenem) in patients with reduced clearance [cite: 2, 11].

---

## 2. Mechanisms of Accumulation-Mediated Toxicity

Understanding the cellular mechanisms of toxicity is a prerequisite for designing safer antibiotics. The kidney is the primary organ of concern for accumulation toxicity due to its role in filtration and secretion.

### 2.1 Renal Accumulation and Transporter-Mediated Uptake
Many antibiotics, particularly cationic peptides and aminoglycosides, are nephrotoxic because they accumulate in the renal cortex at concentrations far exceeding plasma levels.
*   **Megalin/Cubilin Receptor System:** Research has definitively identified the megalin/cubilin endocytic receptor complex as the primary gateway for the uptake of polybasic drugs (aminoglycosides, polymyxins) into renal proximal tubule cells [cite: 9, 10, 12].
    *   **Mechanism:** These drugs bind to the anionic sites on megalin in the brush border. The complex is internalized via endocytosis, transporting the drug into lysosomes [cite: 13, 14].
    *   **Toxicity Cascade:** Once intracellular, these drugs induce lysosomal phospholipidosis, rupture lysosomal membranes, and release reactive oxygen species (ROS) and cytotoxic enzymes into the cytoplasm, triggering mitochondrial dysfunction and apoptosis [cite: 9, 13].
*   **Saturation Kinetics:** Crucially, megalin-mediated uptake is saturable. This biological reality underpins the strategy of once-daily dosing for aminoglycosides: a single large dose saturates the transporter (limiting total uptake) while providing a high $C_{max}$ for efficacy. In contrast, continuous low-level exposure allows continuous uptake, maximizing intracellular accumulation and toxicity [cite: 10, 15].

### 2.2 Intracellular Accumulation and Oxidative Stress
Beyond the kidney, intracellular accumulation in immune cells or general tissues can lead to adverse events.
*   **Double-Membrane Barrier:** In Gram-negative bacteria, drugs must penetrate the outer membrane and avoid efflux to accumulate. However, chemical properties that facilitate bacterial entry (e.g., amphiphilicity, cationic charge) often facilitate entry into mammalian cells, leading to off-target toxicity [cite: 16, 17].
*   **Oxidative Damage:** Bactericidal antibiotics (quinolones, beta-lactams, aminoglycosides) have been linked to a common mechanism of cell death involving the production of hydroxyl radicals. Excessive accumulation of these agents in mammalian mitochondria can trigger similar oxidative stress pathways, contributing to side effects like tendinopathy (fluoroquinolones) or ototoxicity [cite: 18, 19].

---

## 3. Medicinal Chemistry Strategies for Optimization

To break the link between efficacy and toxicity, researchers are employing novel chemical design strategies that modify how drugs interact with host transporters or how they are metabolized.

### 3.1 Soft Drug Design: The Case of MRX-8
"Soft drug" design involves engineering a therapeutic agent to undergo predictable, rapid metabolism into non-toxic metabolites after exerting its pharmacological effect. This strategy is particularly effective for reducing systemic and organ-specific toxicity [cite: 20, 21].

*   **Design Principle:** MRX-8 is a novel polymyxin derivative designed to combat multidrug-resistant (MDR) Gram-negative bacteria. Traditional polymyxins (e.g., colistin, polymyxin B) are limited by severe nephrotoxicity. MRX-8 incorporates a metabolically labile ester linkage in its fatty acyl tail [cite: 22, 23].
*   **Pharmacokinetic Optimization:**
    *   **Systemic Stability:** The drug remains intact long enough in plasma to distribute to the site of infection and kill bacteria.
    *   **Tissue Deactivation:** Upon uptake into renal tissues (or prolonged circulation), esterases hydrolyze the ester bond, converting MRX-8 into a metabolite (MRX-8039) that lacks the fatty acid tail required for membrane disruption [cite: 23, 24].
    *   **Toxicity Profile:** Studies in rats demonstrate that MRX-8 induces significantly less nephrotoxicity than polymyxin B. Biomarkers of kidney injury (KIM-1, NGAL) were markedly lower, and histopathology showed reduced tubular damage [cite: 23, 25].
*   **Clinical Translation:** Phase I trials have shown MRX-8 to be safe and tolerable, validating the soft drug approach for balancing potent antibacterial activity with a reduced toxicity threshold [cite: 26, 27].

### 3.2 Siderophore Conjugation: The Case of Cefiderocol
Cefiderocol represents a paradigm shift in optimizing accumulation. Instead of relying on passive diffusion (which requires high concentrations), it uses a "Trojan horse" strategy.

*   **Mechanism:** Cefiderocol contains a catechol moiety (siderophore) that binds ferric iron. This complex is actively transported into the bacterial periplasm via bacterial iron uptake systems, bypassing porin downregulation resistance mechanisms [cite: 28, 29].
*   **Pharmacokinetic Balance:**
    *   **Linear PK:** Cefiderocol exhibits linear pharmacokinetics with a $t_{1/2}$ of 2–3 hours and is primarily excreted unchanged by the kidneys [cite: 19, 28].
    *   **Accumulation:** Unlike aminoglycosides, cefiderocol does not show significant accumulation in the human body with multiple dosing (q8h) [cite: 19, 30]. Its distribution volume ($V_d \approx 13-18$ L) corresponds to extracellular fluid, minimizing intracellular accumulation in host tissues [cite: 29].
    *   **Safety:** Because it achieves high *bacterial* concentrations via active transport without requiring massive *systemic* concentrations, it maintains a favorable safety profile similar to other cephalosporins, avoiding the dose-limiting toxicity of agents like colistin [cite: 29, 31].

### 3.3 Reducing Cationic Charge: Next-Generation Aminoglycosides
The nephrotoxicity of aminoglycosides and polymyxins is directly linked to their polycationic nature, which drives affinity for the anionic megalin receptor [cite: 32, 33].

*   **Charge Reduction Strategy:** Researchers are modifying the scaffolds of these drugs to reduce the net positive charge without abolishing antibacterial activity.
    *   **Polymyxin Derivatives:** New nonapeptides (e.g., SPR206, VRP-034) have been developed with modified N-termini or amino acid substitutions (e.g., removing a Dab residue) to lower their isoelectric point. This reduces affinity for renal transporters [cite: 34, 35, 36].
    *   **Aminoglycoside Modification:** Derivatives like compound 9d or sisomicin analogs have been synthesized with fewer amino groups. These compounds show reduced uptake into hair cells (lower ototoxicity) and proximal tubule cells while retaining ribosomal binding affinity [cite: 32, 37].
*   **Efficacy vs. Toxicity Trade-off:** The challenge is that cationic charge is often essential for the initial electrostatic attraction to the bacterial outer membrane (LPS). Therefore, optimization requires a delicate "tuning" to find a charge density that permits bacterial entry but falls below the threshold for high-affinity megalin binding [cite: 33, 38].

---

## 4. Dosing Strategies to Balance Half-Life and Toxicity

When the chemical structure cannot be altered, the dosing regimen must be optimized to exploit the differences in the kinetics of bacterial killing versus host toxicity.

### 4.1 Extended-Interval Dosing (Aminoglycosides)
This strategy is the gold standard for balancing efficacy and toxicity for concentration-dependent antibiotics.
*   **The Principle:** Aminoglycoside uptake into the renal cortex is saturable. Once the transporters are saturated, increasing the serum concentration does not proportionally increase renal accumulation [cite: 15, 39].
*   **The Regimen:** Administering the total daily dose as a single infusion (Extended-Interval Dosing, EID) achieves a high $C_{max}$ (optimizing $C_{max}/MIC$ for efficacy) but allows a long "washout" period where serum levels drop below the threshold for uptake.
*   **Outcome:** This maximizes bacterial killing and the post-antibiotic effect (PAE) while minimizing the time the kidney is exposed to toxic uptake concentrations. Clinical data confirms EID reduces nephrotoxicity compared to multiple-daily dosing without compromising efficacy [cite: 15, 40].

### 4.2 Extended and Continuous Infusion (Beta-Lactams)
For time-dependent antibiotics (beta-lactams), the goal is to maintain $fT > MIC$.
*   **The Problem:** Rapid bolus injections produce high peaks (unnecessary for efficacy) and low troughs (risking failure). To maintain $fT > MIC$ with boluses, frequent high doses are needed, which can lead to accumulation in patients with renal impairment.
*   **The Solution:** Extended infusions (3–4 hours) or continuous infusions maintain steady-state concentrations just above the MIC. This allows for lower total daily doses to achieve the same PD target, reducing the total toxic burden on the host [cite: 8, 11, 41].
*   **Toxicity Reduction:** By avoiding high peak concentrations, extended infusions may reduce the risk of concentration-dependent neurotoxicity (e.g., with cefepime) while improving clinical outcomes in critically ill patients [cite: 11, 42].

---

## 5. Advanced Modeling Techniques (PBPK)

Physiologically Based Pharmacokinetic (PBPK) modeling has revolutionized the ability to predict the balance between clearance and accumulation before a drug enters human trials.

### 5.1 Mechanism of PBPK
PBPK models divide the body into physiologically relevant compartments (liver, kidney, lung, adipose) connected by blood flow. They integrate drug-specific data (physicochemical properties, permeability) with system-specific data (organ blood flow, tissue volume, transporter expression) [cite: 43, 44].

### 5.2 Applications in Optimization
*   **Predicting Tissue Accumulation:** PBPK models can simulate drug concentrations in specific tissues (e.g., renal cortex, epithelial lining fluid) rather than just plasma. This allows developers to flag compounds that show dangerous tissue accumulation despite "normal" plasma half-lives [cite: 45, 46, 47].
*   **Special Populations:** PBPK is critical for scaling doses to pediatrics, where organ maturation affects clearance, or to obese patients, where lipophilic drugs may accumulate in adipose tissue, altering $t_{1/2}$ and toxicity risks [cite: 45, 48, 49].
*   **Model-Informed Precision Dosing (MIPD):** Clinicians use these models to individualize therapy. For example, in a patient with renal failure, a PBPK model can predict the exact dose reduction needed to prevent accumulation while maintaining lung tissue concentrations for pneumonia treatment [cite: 45, 50].

---

## 6. Special Populations and Pathophysiological Variability

The balance between half-life and toxicity is not static; it shifts dramatically based on patient physiology.

### 6.1 Critical Illness and Augmented Renal Clearance (ARC)
*   **ARC:** In younger, critically ill patients (e.g., trauma, sepsis), hyperdynamic circulation increases glomerular filtration, leading to rapid antibiotic elimination (shortened $t_{1/2}$). This risks therapeutic failure. Optimization here requires increased dosing or continuous infusion [cite: 4, 51].
*   **Tissue Edema:** "Third-spacing" of fluids increases the volume of distribution for hydrophilic drugs, diluting concentrations. PBPK modeling helps adjust loading doses to ensure target attainment [cite: 4, 6].

### 6.2 Renal Impairment and Accumulation
*   **The Risk:** In patients with reduced GFR, renally cleared drugs (cefiderocol, aminoglycosides) have prolonged half-lives. Without dose adjustment, accumulation occurs, leading to seizures (beta-lactams) or worsening AKI [cite: 2, 28].
*   **Optimization:** Dosing nomograms based on creatinine clearance are standard. However, for novel agents like cefiderocol, studies show that even in end-stage renal disease, the drug is removed by hemodialysis, requiring supplemental dosing to maintain efficacy [cite: 52].

---

## 7. Future Directions and Conclusion

The optimization of novel antibiotics is moving away from a "one-size-fits-all" approach toward precision medicine and precision design.

*   **Kidney-on-a-Chip:** New microphysiological systems are being used to screen novel polymyxins (like VRP-034) for nephrotoxicity early in discovery, providing data superior to traditional animal models [cite: 36].
*   **Adjuvant Therapies:** Research suggests co-administering nephroprotectants (e.g., cilastatin, which inhibits renal dehydropeptidase and blocks megalin uptake) could allow higher doses of antibiotics by blocking the accumulation pathway [cite: 27].
*   **Conclusion:** The pharmacokinetics of novel antibiotics are optimized by integrating "soft" chemical design to limit tissue persistence, exploiting active transport for bacterial targeting (siderophores), and utilizing advanced PBPK modeling to design dosing regimens that respect the saturable nature of toxicity pathways. This multi-pronged approach ensures that potent new agents like MRX-8 and cefiderocol can be used safely against multidrug-resistant pathogens.

### References
[cite: 1, 2] - PK/PD principles and toxicity thresholds.
[cite: 8, 11] - Extended infusion strategies.
[cite: 9, 10] - Megalin-mediated renal accumulation.
[cite: 22, 24] - Soft drug design (MRX-8).
[cite: 19, 28] - Cefiderocol PK and safety.
[cite: 43, 44] - PBPK modeling applications.
[cite: 15, 39] - Extended-interval aminoglycoside dosing.
[cite: 34, 36] - Novel polymyxin derivatives and kidney-on-a-chip.

**Sources:**
1. [ucla.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZEm_I8DRZtIJPSAh7CA7hwMezhT1TvPRWkmLPGRTb46-olJCiCaSJUZUrrUETEuCoKu_-ZdbkUVdrdJ96mYHidqiX8snIRLpDTrLFxS5Tc3TwUgA06kEEmbliI7-puwfil85Az1yeJFcxgdYIRbbq49OTWry1EIjVMQj7fiK1wgS7)
2. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL3Fn2hMoDqg1NlU_DIKPVobBQ2cRq9LdF2IvHSNxGvQApoHwUYC_hz66v9JiDoZteK93dkXjnZ9iH0lLGYzz3lcXb6YavV6Bm9vpWCL9nVzaC9VSHDwo5OTOwXuYXwPhDTJuKOk5A)
3. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7ztfFFxfSXP7iXY9rTxmM4koa3G3XSmarzB1TNy56GZfEQF3P__DjLlUK3SIDqiKmJBNrC46Ci6dxU9598tuXquYd0azEgl-OkFnfyMRPeGFQLwcdPYuqSQI_ee5laiwBk48=)
4. [derangedphysiology.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzg9JxHl8q0XKDhPDV3mk9uKMoMcKJAsk9RJiPtGsHDf0qnggAWsYYhic2dmsTArupAT-xkcAOKqIFF9sTMjPJzcONCLlSU0miGQB7VowI2ZlzRvMyQC424n7vEYBjoEyZ0YHhHO7tmfG7QufQUzPXvrcA17dFye570IGa1BlI4-p-fvpuT5lPS03D4nDF_GgMcz_g1WzraKzBV6a5UsEzcDyKp0NzCW63Xyhn0-afM0woxtQLneNmsf0I)
5. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6x2r7BN2fxabb8HGJUrvcK40uQGW-TZDqiOjML77RaOyy_8hq9zuSPrfqez-rYRGJm8-WVeHJWtCDbqW1A_18XOTXHketWVepz4ybRvuxTwmPPKbkfNlvW9XFMUDcY1dhQB-tHTvzVvk3He7waBkmOAKSt2BqoJF7I_2kAwpa8ho1avTVam1_gugAN2jkwhEK90BMY9raJBvhcz6ZDjFkooaChYJkaX6t1tzAiZrZ7lZv5uRe-jsganGD0e-o48eXFY1ZAIs=)
6. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0cLkO5mmuw0FkqYdet-iPd3-vfhfZ2UaLJbIfG6cQjr91Zn_quSizlAFejXGBw-kz0qSOMc0nGMBHXnU4MFiyzvhBeFeZ_73BiqaxGkZXPSPOxAtGsf6fsdEADt4Dbkm7cMe6HHXi)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrhCU6AoJmzlY7ownNvp6KIFtG3zIssMfcTJlFon-CihC1zycKzxYX6wkmqz5GnBnZYJeP4GHeNEr8zzPIe7Yb50gfJ7b8CHHcvbalJtbkj8Pgla2h6yBXzT2xn_Cs5KODtB4jfYtz5ARAmQSLU_SF4s6LygJClo6G1uefzd_A1aIiL13i1yijGehUwXIWccnaYLkbavsRXxFTANpwzp0JbcH85rc=)
8. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8e-jkJpV6dRGc0Aq8DnxnMD7FAWsIW81yj-FFBiCatsB3EWpkOoTYtQA8ObhHP1mk2gFtILQZM0d691ZcFT8MvgfvwfbntXJaedFAbujOyF_45F05EbgWlouvlcNhceS8)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtXMYAUEGQXVE06jTQ0IN5fcgtLQ0hhOJCzwrxFtW7Bn8f4gXIqhVE__kUJTWXp5CzbPOQ4JkLduYDUCd0tPP5mB_01r9b0W2Br0DcmJlbC4qPwOQQkzxBwIi33Wx1gAQrdWReW-gE8w==)
10. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4GBxe8Y--pMf60fkjQD7Ke8jl7KwbtwvpM4cmx2lPJmvMtMyKJwmIrN3xyAXyRa3HFBsHWmz9O-TLnMBICBWu1LXPZ7hIknrT5MwF6YYdIR5EzrUc0-VigcksL3LqoB-B1siDVH-h)
11. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG70B3pRd4E9dxVA8ss-j-NMGpq-E1Z_ChsUYvobXrMdLOtd-ogcMr7T7mIPDpiB8LlhvVAppLwGBMLgQ4R9X7aBSXP237WQ9_BxYh9UzUAWPlEvrcF66ufhAkS8sXYnQ2roXJWUP0n)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcvTV7qPzILDaUT9yKC9lZ-o9Cxks8wtNJTyU7N6FPwmkg2Lo6NMV9e9TvYBe-MvMzqKDW_JWoiFasKFSNXiHzvYWLA5LGmjQAhbCaa7xDQQns8LQE9Vj1rZTtXJPQJ1Za-i6nT92LgXd5xufD5Fi-kH-wXgGE264ElCJDKpD6fKc7wv7XLATEXTxzhgNQonNqvHa5nwrFVI8DUr7_379TCV1SF1ogHA-qsuX_NMaEE8V2bg==)
13. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHInLhdrablAMI36jvxQHd3Du0WpOlPHGUYXTclnjs95HQrWj3kJTqqZqfCqwxvV8mOKMjH_-ybWQeDpQNNA5Z03HaaFfU_uJm3d-3JRE5c3WBKHI77YhPrAjjZwLjCyS7M6TIPN-s)
14. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8xNXZIucI7bUXfTo5mJtDP9BfEIQCX7y0Z9mLhoMt9kdsBbh7zUyL7PaZWUz0N1hpADg2F4qq4ZcDIviJmQWVKxNgejO2eCQI4GDBsi98UbaPIaAc9ogEqyExylLXnaOPZ49EOl5v)
15. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhs4y1kApsr_IWZQiMZX-f5pnWM2dPuXATOTpAnJdyEBOJV-ZzxKdq_N_XWw1Y4U1OFy6sXAMiubRCgyWXB-SY5JqJNOGwoCB23MxiYdY5YHMnwkovvjhLPcxc0b123poSGYZxcfGo)
16. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXlsWkXWk6oEkg4w1rfCVBFX96mdXb5MIFgJvdk_ntmyw4mIbo3LuOnJDNMxu-OdWgU78ndRMQGrVgU0xtZbWijwPhCxuVehtI7d5c2hkowFtHOkU3vgw6ZP4W9NikmqVH_qxKimBf)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPJNS_sL3OZoRBG5WFOMj9M3y63nuMruqHyzOsblWcfyzr2AbsycV30Uv-fRJcHdhtU5n3YWjOpo2K0x47VDAXN8WebsKlo3HF3E6NXobXhn_qaFGsKiYwdljcntGriq6J7mQfGESRG3RAanL26Ro2ZbLsnZlfOCpwToGm9Zm9ZwbHmtD7q-xAOqQ075So-j9iA8SLxhhi5kPe8q0J-KEPkeLpXSx5rvtxYgvnKUGNijU=)
18. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtSCLlhsvgxGLKdpkg8ZmrPSLfhGB1SZTFZhPtKfNuwmmhYydd6YBOfFj6398s9lneIGgIXMXSXVhK4yrtUDlweDSgzr74ZwXpuieMaK6wruPtxC7mo13fyL790pRllz0sD7UfgWDU)
19. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5ac8YgV4sz9Oaumbakc-Ki0Vn0inEwPJTjQBsBk-dEay7JNfuNtGUjRI-zazMiTzBg1fmDYGzhYV1pPF_c9pINgU_uzYbMYUsUh1u6FTPUcCSeyq_0xsdWytqnnB684qbUe5knInu)
20. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-hwYUU8XFwJxlX7Ya9M9AHY1KUcXLpvGG9D5hM0CxXev8duQGb_spJnV1dqymNNHZlOpsX_EOuAfCQ9A--QRtMWKVj2WlpqWxLI-S-738ilZqd0cXibB5DuDH-8jskRLdQHYg_RkjiPMjDy0n7tvdP4e-P829NSflcUj9FRKDFGc4i8pEW8BlQRIrAcgw6f4UcPYZN1osf6UmVbPRB2dKl7eA)
21. [gsconlinepress.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoEbfzweiuYZT2dOFugywaQJyPDTqeD_m2lu5fjv0IEIZ0Q5pQtcTZMA4-NmDg7xGNkMQGWLlpg2jh6aFzFmasqqNDzqaf7yoTf4zVbFHlLubz_eRQtRyu_WtMqhkj6_d27aaRIMSAVRNKVslC7bG1j8xJiKAYYebINxt3CKfxm2tegw5YGL4gmg==)
22. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_Sb1Qb-h_XqhanbwH8Nco43isFFKp1THrTZZE1khsoX6Cp3ILNBE0rneuwYD7qflZ9XcS5t78ojQ_lh86qnHHvC9Nfulfqrl55gdEGG_2bpTl_3mWdkc7YukJ7XmANL3iVuvTm2IM)
23. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErZeSWJSMHsYxmjnXJekpWbHyhCouYEGjbLBVx6yWM8WMhYuS03UvvjwU6zXkDkyjimsj2P3bJnCp4zdEh0_1sNGnrLDWDM4rD_SIhnCB_FdEk0Zy-69prWeZYk2JYPAvMDkBGtaLtuA==)
24. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8dWUtz25nuIkUSWx5LSxVZK7srAaI0bX8PO0N_bjOHayjkXCiiRenUtLmXDGjkwQfQg9b7xB0JGJsNmz6tAU79ECJfGFfAjGwLTIwjnOM2Zc2vjCpD_Vqvcn0Jh8=)
25. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7CqUog0uHi2Gat0x8r2CUZzXwgeoPHZqKtey_7PpB6uFYRswNPtaVFUCHSeGSf_vTJ9hX2LdW4XEovbQx9FmXtyMWWBXoQJXHXFk_vZJrmNnO1gC3gIwAyqZ1lL89SXgL-rlvd289gEcLluP7ebbewsTTh5PZnQjXiyXYgqjqWa2y7pAUH4qpQzjnQMO2qWI3zzcAclcl65yd3zE18RvMMtdifWkIkUxMp34xOAMK88eCWtVgOsZAqBu_f9VvFC0SppbhEjCATm4-H7OSy5Zyxgjyq5loXM6jvlL1kak-)
26. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIbU001cEN_7hYUhkgKe6cmAZQxizFIWsHUlxEio8OOXJiZuJnShokOA32EzvzG_ONjxn1SwcnByDlFqQjwWKlrnOFJo0cMoxvIV-4yZNJWSH9WsYyJlKtZPi56k_1evCsQaL6MYNrMw==)
27. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVG_VhU2z_dME9CZmaTUEFCoT8GiiMiQM65NTal9DoT32PUhRv0HENmZ0oY04FHE40u1s4vX71tOKyobGIoJ8YiKcs4UlBIg6cZtLFgu-kt6YNGyz0wFHMG6TkgOAcXxndP0mRSy3TCw==)
28. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoWy9nGjFC2BllvahVYpzBQC7vc7EvPyJDHD5CoMGAN9EWeecyxWgEjdUopc-MrDOJ-MBoyBhOM1iVTjTuUXwcPJX6m2hKZP69woLE39r1iZnLsDnvcoLIvwEBXr4rCg==)
29. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBvCTFwwWMCWkTTrYUx63n7VD6KIyGnlZALcgmxR2mjVS2BKl1KnhZTlWIedpOvRI7aQAoflLAo0o7jmK0TEzabeZy1JjcWIuKX6eAKRlCO-HzQqBTBMFrXlb7UHDEtvEEl3UVu0Zm)
30. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoqqv4VgqSYowCnO9QmF8HQ1N5ZDadFc3pUE6z46wOPAwNzIMDgXMGo1G6K2acJAgg4BGiXJc392UqP0bjEWDhDDONQyReZAB3-g2KlFmGuc64gP0YiMGte1jowLm4wL3DWQSyAP2i)
31. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUfiGhSvyKk8eLtcHh8yuPYkZAl1QF3MSguU9uK2bEaXns9bALUowqs8rDEPkqffcbenV941sXh27RcQPH1j63c5cTBFfklcavu5PVqzNWx0JoiF0Xszrs1tOLjbeqW0HXEfyNOBpDeNxrTf0lWVPjXzGhbBPXcQ==)
32. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6bYnPeKT2KxXDuCBCvCPNDtR1dGcL5Bb3v_Y1Q3Gtphd4Oui3cFLkUHiCZETJ4jqy1aIDA_RnzoWyCPsBxT-UwgAc1SyZTjroVAxX3j5AyGrcinwWCIIY4eL3dRev0dJ2ZcRsNHWV)
33. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEA2lHPLMFdEHXuv-Dr9rdpjUGRPsK1EeZU8plW8Gi911ePvxB9nOh_PEuHr5tPTsyG4c5SBmVxpVofeyLSvIvxBsYMZDpGtyGSzuCLq98ST00wq6wB-JKT8NUzrxlwZPA=)
34. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLuxUUpi3mEpv3HOiqjG8UPd1UZO0H6Vlz4KJfVPArLLUGXqQ4K9RYM02dc2lq3EWPJBZvEktpQw4gUkm9aTaZxc_u1bQxDxYQVk6OgjgRzFlPXELRUQ_q6qOOZIQ2dO-sJ2SzoPnP)
35. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4F2NXzyPbHTN1R0ms9ItJEnrrgqDB03bSeQnn0itHFajiRc1OHrOSH0SE4M0NaB912y_XkcjrlF7clJLjRQhgNCUSDBnyAI28ncIHLRki-b6TJZVWhJ71cWitshG9ZqqM_zdgXwIwbCn7ww==)
36. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBtvHoHr7klfO7AxOKx2YndyLym-hRk75N1-qG8raPqMcwe0HbbsFaal141gBET2j_P7HG69KwJFqY8ySOLgGXtwHboqwO4Lhzz3rHla5Kq7N_m0eWp6yX8egYq0vcR5UDLVNyo6njaw==)
37. [jci.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyJGgowaTsSNEmq6kiUBFbY51hlStmbla4r3jdpalKLVzlXyPFoGtVQ8duo_grmhBGoVl643CQd78Jqj5i6hRZC-c0nwO4U8jl_CXYm5p1ZJw8YSimjm6m8UjtIxQ=)
38. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOrVQafagCcrD-ZPkaB8DxCnPutte7jL1U4erkp2DNJCv8jkP5nPMYmH-v7baD01ubNR1fUtIzW_t5MY-AGppiADP5Tq92aANhrdbnsykumS-Q_EYn2RXRZF3hJYbeCg==)
39. [rxkinetics.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxdRHLYZ3AVPqkTQm_WIguQkhqgDua0VQQe-_-FI74Qb3VrA-sf7KWgJbi0yIuGe-q8WYnduhSVqohuVQ5QN6-7nrvM1lFYRXWvzvpqtYhpoL9wfrKB6GblA==)
40. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNO8EJ8lc3B4beNp0XgZQFD3gmGL9U0K_i0xQalPSU6rZvZ9hn-UeUsJ5Br_4UpEF3O5y7uH4m9knHoRNQdYA13e-RaHc5nZBnlgAZGKa7Ea4x1mSCgI_uiIt1I44D)
41. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmRoOMSs8iu6XppO5duOcLF_CzevB7KZ9t1T_5xPF62URm44Q1b9q9Pq0WnbpzElTJ1fEHYy2qaz7FmtQBYh_6Y8CQnblSYjHxFbtHkIqgaxL5RmZGmzokRgmlfkdxqhaA)
42. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZkFYe8ws2YvzCb0ZNCM0af71Vzt3RRlRKXFCyX6cQIcNzPFzMhUZFop0Zq1xCg7xFjXKQX8Y0w9mAKGrB6YgAKP20IFbGM12Q8CQdmcwwPCoBikBNqn8qV-vL6CEtFzxr43X6_3jE3w==)
43. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbFv_ecG4wsjzHoIlsoJ71eyVd4zJ_lVjwILpKtaW0y_66EpBQV76LCUYXiZmLKECFFAU22gIftrt9NnifBQBD3JQMJrtLXgVALFUnGsqOR-mJio0BdIhgQ1cd4MkF)
44. [open-systems-pharmacology.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGB2wdV0ufwMCOvHpwnD24lgxRg64tezmKYzy5RJdQ-sEeoG6IU2WXQQ0Mp9zzlOid4n-Q1sGJWXx-e1xgWoHc47hs8qBqftVcC0d1T_OR-Cq2O6or3j4nw0unfbvwf1_MVTV9TxKOBkYVRLNAMrY6iMPZ2CoPlJ38arU7dfechbHmWOZ15q-okq-mVO8l-8XbAGQNFmru5gDdRxmhWKIvqaJisvmm3r3plvfILB4XwATJX9uZOucP0s_cl-IcGykBMPYL3EpDi8zc=)
45. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAUivXdfcsXVw6FGgRvpbxtps5Of4E3IhPk-ZbNBKNh27W5kPD4OgJrDywgye-QhjQNrAsoxmhWZAoEXbi2hFITCT3FVi8-tsmOdhqBEK06q26-kADdl6iW5XRE4fcAVW1ygsV0Rne8A==)
46. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbYe8YqfnhaaJWizIm00fdrJ1tw-us8hKFIfGG-mTSg8vtrwPobDzSu39HojiNdqHFuscwcMxE6oLeZfmcjfmZBGKp-b65HVLK8oqJmFl8NqxomLR2tC3RxfhdhDpz7DssnJb7GGVyTwrXHnzeAYtOBKtHWlUM7UPzBo9kpbPwxamVhn6AIgd61DZvdE6zRO4=)
47. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRHJ1NUYfbc2EYttNkT9iRsdHhOjb5IQVW5LxqW-Jn6Bg5R-4QeKvv0dHZIUk2Dlrclg2ZMLjPDCBuf6a6NT61RBJCJoWwdydWUBrZjGp_nb3dpLqTAXaxN4PIrLE9N-mA-cXaxYCw)
48. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKBiOvCpPppimWI_FQMfQ4I5Vv_wxZ-uWb3k0c7ck2ggcHkolMj6eUqdeok7YBh8S9mI3VP4eNJogitdJXf_bTNXyBa8RWzxFpji8XTcZPttjyvCnburMkfGgJYodqTm9a0nQeYQXh)
49. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF52YGpSJSlsh0Uv4g5KUtA5OE7MYTs1QBDJHbpAUyxLFw7sVAwVB_uUppQaz8NzZmG7FpFDDp-rPbEZc6QnGEt5MPIq0ap0o438E--wSuHT59fPpT12CjB6G63doA=)
50. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWLmbn7Fut3KdD0Q0XT-wTdn2P9EwqrvIL40V8FoihttEbUSYNGAbpMMfbBnYuVFSdinaPry1DE5N4ZNntp_RNcgAFJ4xAQDuKRm0YmlRpefXRsPpLXHxMDpH53ejcAMOx0CP0RkKY4JdqBeYOTGUTnDGgQZ5lPqUafJUNxmDcCiLbh9Wy-w--wimKo1266t9gR98vRXpcCx7wDceeiOXGozU0Ed28lDanQXO0Nse38cXOl8iis-vJVATQPEmFYzIG-gMYi3wmDn-H66zqqmpYe5V6)
51. [litfl.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFl2NE8gJh8dr6JjkSUovVjTYSC9It4iiibg_13tgiepQ3iQWx7rpJeI29gf1oCBUpXsrdEr7618eft3rwLFiQRKPqQppuuxLpdAZK394fsROtmSpqdKb_Hy5hr6NcZY8AiZMw-V_OnNQvTuU6UEYei--w5NWSa)
52. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEn1RmbGGAa6Yhw1xxVQR3PkoIToXyfSTaPJO1Gb-4mtWYqfpOat4z-yaUdPoEF3-vZ5J3l_qMhXeA27LdYfliEokdG6gG8sK8z0-a17EDet1PzVe0bB02pEWfNaPxFZEIhYHD1v3Zh)


## Annotations
Annotation(end_index=3255, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZEm_I8DRZtIJPSAh7CA7hwMezhT1TvPRWkmLPGRTb46-olJCiCaSJUZUrrUETEuCoKu_-ZdbkUVdrdJ96mYHidqiX8snIRLpDTrLFxS5Tc3TwUgA06kEEmbliI7-puwfil85Az1yeJFcxgdYIRbbq49OTWry1EIjVMQj7fiK1wgS7', start_index=3243)
Annotation(end_index=3255, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL3Fn2hMoDqg1NlU_DIKPVobBQ2cRq9LdF2IvHSNxGvQApoHwUYC_hz66v9JiDoZteK93dkXjnZ9iH0lLGYzz3lcXb6YavV6Bm9vpWCL9nVzaC9VSHDwo5OTOwXuYXwPhDTJuKOk5A', start_index=3243)
Annotation(end_index=3510, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7ztfFFxfSXP7iXY9rTxmM4koa3G3XSmarzB1TNy56GZfEQF3P__DjLlUK3SIDqiKmJBNrC46Ci6dxU9598tuXquYd0azEgl-OkFnfyMRPeGFQLwcdPYuqSQI_ee5laiwBk48=', start_index=3498)
Annotation(end_index=3510, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL3Fn2hMoDqg1NlU_DIKPVobBQ2cRq9LdF2IvHSNxGvQApoHwUYC_hz66v9JiDoZteK93dkXjnZ9iH0lLGYzz3lcXb6YavV6Bm9vpWCL9nVzaC9VSHDwo5OTOwXuYXwPhDTJuKOk5A', start_index=3498)
Annotation(end_index=3673, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL3Fn2hMoDqg1NlU_DIKPVobBQ2cRq9LdF2IvHSNxGvQApoHwUYC_hz66v9JiDoZteK93dkXjnZ9iH0lLGYzz3lcXb6YavV6Bm9vpWCL9nVzaC9VSHDwo5OTOwXuYXwPhDTJuKOk5A', start_index=3664)
Annotation(end_index=4043, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzg9JxHl8q0XKDhPDV3mk9uKMoMcKJAsk9RJiPtGsHDf0qnggAWsYYhic2dmsTArupAT-xkcAOKqIFF9sTMjPJzcONCLlSU0miGQB7VowI2ZlzRvMyQC424n7vEYBjoEyZ0YHhHO7tmfG7QufQUzPXvrcA17dFye570IGa1BlI4-p-fvpuT5lPS03D4nDF_GgMcz_g1WzraKzBV6a5UsEzcDyKp0NzCW63Xyhn0-afM0woxtQLneNmsf0I', start_index=4031)
Annotation(end_index=4043, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL3Fn2hMoDqg1NlU_DIKPVobBQ2cRq9LdF2IvHSNxGvQApoHwUYC_hz66v9JiDoZteK93dkXjnZ9iH0lLGYzz3lcXb6YavV6Bm9vpWCL9nVzaC9VSHDwo5OTOwXuYXwPhDTJuKOk5A', start_index=4031)
Annotation(end_index=4266, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZEm_I8DRZtIJPSAh7CA7hwMezhT1TvPRWkmLPGRTb46-olJCiCaSJUZUrrUETEuCoKu_-ZdbkUVdrdJ96mYHidqiX8snIRLpDTrLFxS5Tc3TwUgA06kEEmbliI7-puwfil85Az1yeJFcxgdYIRbbq49OTWry1EIjVMQj7fiK1wgS7', start_index=4254)
Annotation(end_index=4266, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6x2r7BN2fxabb8HGJUrvcK40uQGW-TZDqiOjML77RaOyy_8hq9zuSPrfqez-rYRGJm8-WVeHJWtCDbqW1A_18XOTXHketWVepz4ybRvuxTwmPPKbkfNlvW9XFMUDcY1dhQB-tHTvzVvk3He7waBkmOAKSt2BqoJF7I_2kAwpa8ho1avTVam1_gugAN2jkwhEK90BMY9raJBvhcz6ZDjFkooaChYJkaX6t1tzAiZrZ7lZv5uRe-jsganGD0e-o48eXFY1ZAIs=', start_index=4254)
Annotation(end_index=4413, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZEm_I8DRZtIJPSAh7CA7hwMezhT1TvPRWkmLPGRTb46-olJCiCaSJUZUrrUETEuCoKu_-ZdbkUVdrdJ96mYHidqiX8snIRLpDTrLFxS5Tc3TwUgA06kEEmbliI7-puwfil85Az1yeJFcxgdYIRbbq49OTWry1EIjVMQj7fiK1wgS7', start_index=4398)
Annotation(end_index=4413, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6x2r7BN2fxabb8HGJUrvcK40uQGW-TZDqiOjML77RaOyy_8hq9zuSPrfqez-rYRGJm8-WVeHJWtCDbqW1A_18XOTXHketWVepz4ybRvuxTwmPPKbkfNlvW9XFMUDcY1dhQB-tHTvzVvk3He7waBkmOAKSt2BqoJF7I_2kAwpa8ho1avTVam1_gugAN2jkwhEK90BMY9raJBvhcz6ZDjFkooaChYJkaX6t1tzAiZrZ7lZv5uRe-jsganGD0e-o48eXFY1ZAIs=', start_index=4398)
Annotation(end_index=4413, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0cLkO5mmuw0FkqYdet-iPd3-vfhfZ2UaLJbIfG6cQjr91Zn_quSizlAFejXGBw-kz0qSOMc0nGMBHXnU4MFiyzvhBeFeZ_73BiqaxGkZXPSPOxAtGsf6fsdEADt4Dbkm7cMe6HHXi', start_index=4398)
Annotation(end_index=4683, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6x2r7BN2fxabb8HGJUrvcK40uQGW-TZDqiOjML77RaOyy_8hq9zuSPrfqez-rYRGJm8-WVeHJWtCDbqW1A_18XOTXHketWVepz4ybRvuxTwmPPKbkfNlvW9XFMUDcY1dhQB-tHTvzVvk3He7waBkmOAKSt2BqoJF7I_2kAwpa8ho1avTVam1_gugAN2jkwhEK90BMY9raJBvhcz6ZDjFkooaChYJkaX6t1tzAiZrZ7lZv5uRe-jsganGD0e-o48eXFY1ZAIs=', start_index=4671)
Annotation(end_index=4683, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrhCU6AoJmzlY7ownNvp6KIFtG3zIssMfcTJlFon-CihC1zycKzxYX6wkmqz5GnBnZYJeP4GHeNEr8zzPIe7Yb50gfJ7b8CHHcvbalJtbkj8Pgla2h6yBXzT2xn_Cs5KODtB4jfYtz5ARAmQSLU_SF4s6LygJClo6G1uefzd_A1aIiL13i1yijGehUwXIWccnaYLkbavsRXxFTANpwzp0JbcH85rc=', start_index=4671)
Annotation(end_index=4904, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6x2r7BN2fxabb8HGJUrvcK40uQGW-TZDqiOjML77RaOyy_8hq9zuSPrfqez-rYRGJm8-WVeHJWtCDbqW1A_18XOTXHketWVepz4ybRvuxTwmPPKbkfNlvW9XFMUDcY1dhQB-tHTvzVvk3He7waBkmOAKSt2BqoJF7I_2kAwpa8ho1avTVam1_gugAN2jkwhEK90BMY9raJBvhcz6ZDjFkooaChYJkaX6t1tzAiZrZ7lZv5uRe-jsganGD0e-o48eXFY1ZAIs=', start_index=4892)
Annotation(end_index=4904, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8e-jkJpV6dRGc0Aq8DnxnMD7FAWsIW81yj-FFBiCatsB3EWpkOoTYtQA8ObhHP1mk2gFtILQZM0d691ZcFT8MvgfvwfbntXJaedFAbujOyF_45F05EbgWlouvlcNhceS8', start_index=4892)
Annotation(end_index=5073, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZEm_I8DRZtIJPSAh7CA7hwMezhT1TvPRWkmLPGRTb46-olJCiCaSJUZUrrUETEuCoKu_-ZdbkUVdrdJ96mYHidqiX8snIRLpDTrLFxS5Tc3TwUgA06kEEmbliI7-puwfil85Az1yeJFcxgdYIRbbq49OTWry1EIjVMQj7fiK1wgS7', start_index=5061)
Annotation(end_index=5073, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6x2r7BN2fxabb8HGJUrvcK40uQGW-TZDqiOjML77RaOyy_8hq9zuSPrfqez-rYRGJm8-WVeHJWtCDbqW1A_18XOTXHketWVepz4ybRvuxTwmPPKbkfNlvW9XFMUDcY1dhQB-tHTvzVvk3He7waBkmOAKSt2BqoJF7I_2kAwpa8ho1avTVam1_gugAN2jkwhEK90BMY9raJBvhcz6ZDjFkooaChYJkaX6t1tzAiZrZ7lZv5uRe-jsganGD0e-o48eXFY1ZAIs=', start_index=5061)
Annotation(end_index=5471, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4GBxe8Y--pMf60fkjQD7Ke8jl7KwbtwvpM4cmx2lPJmvMtMyKJwmIrN3xyAXyRa3HFBsHWmz9O-TLnMBICBWu1LXPZ7hIknrT5MwF6YYdIR5EzrUc0-VigcksL3LqoB-B1siDVH-h', start_index=5458)
Annotation(end_index=5471, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtXMYAUEGQXVE06jTQ0IN5fcgtLQ0hhOJCzwrxFtW7Bn8f4gXIqhVE__kUJTWXp5CzbPOQ4JkLduYDUCd0tPP5mB_01r9b0W2Br0DcmJlbC4qPwOQQkzxBwIi33Wx1gAQrdWReW-gE8w==', start_index=5458)
Annotation(end_index=5715, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG70B3pRd4E9dxVA8ss-j-NMGpq-E1Z_ChsUYvobXrMdLOtd-ogcMr7T7mIPDpiB8LlhvVAppLwGBMLgQ4R9X7aBSXP237WQ9_BxYh9UzUAWPlEvrcF66ufhAkS8sXYnQ2roXJWUP0n', start_index=5702)
Annotation(end_index=5715, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL3Fn2hMoDqg1NlU_DIKPVobBQ2cRq9LdF2IvHSNxGvQApoHwUYC_hz66v9JiDoZteK93dkXjnZ9iH0lLGYzz3lcXb6YavV6Bm9vpWCL9nVzaC9VSHDwo5OTOwXuYXwPhDTJuKOk5A', start_index=5702)
Annotation(end_index=6489, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4GBxe8Y--pMf60fkjQD7Ke8jl7KwbtwvpM4cmx2lPJmvMtMyKJwmIrN3xyAXyRa3HFBsHWmz9O-TLnMBICBWu1LXPZ7hIknrT5MwF6YYdIR5EzrUc0-VigcksL3LqoB-B1siDVH-h', start_index=6472)
Annotation(end_index=6489, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcvTV7qPzILDaUT9yKC9lZ-o9Cxks8wtNJTyU7N6FPwmkg2Lo6NMV9e9TvYBe-MvMzqKDW_JWoiFasKFSNXiHzvYWLA5LGmjQAhbCaa7xDQQns8LQE9Vj1rZTtXJPQJ1Za-i6nT92LgXd5xufD5Fi-kH-wXgGE264ElCJDKpD6fKc7wv7XLATEXTxzhgNQonNqvHa5nwrFVI8DUr7_379TCV1SF1ogHA-qsuX_NMaEE8V2bg==', start_index=6472)
Annotation(end_index=6489, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtXMYAUEGQXVE06jTQ0IN5fcgtLQ0hhOJCzwrxFtW7Bn8f4gXIqhVE__kUJTWXp5CzbPOQ4JkLduYDUCd0tPP5mB_01r9b0W2Br0DcmJlbC4qPwOQQkzxBwIi33Wx1gAQrdWReW-gE8w==', start_index=6472)
Annotation(end_index=6680, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHInLhdrablAMI36jvxQHd3Du0WpOlPHGUYXTclnjs95HQrWj3kJTqqZqfCqwxvV8mOKMjH_-ybWQeDpQNNA5Z03HaaFfU_uJm3d-3JRE5c3WBKHI77YhPrAjjZwLjCyS7M6TIPN-s', start_index=6666)
Annotation(end_index=6680, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8xNXZIucI7bUXfTo5mJtDP9BfEIQCX7y0Z9mLhoMt9kdsBbh7zUyL7PaZWUz0N1hpADg2F4qq4ZcDIviJmQWVKxNgejO2eCQI4GDBsi98UbaPIaAc9ogEqyExylLXnaOPZ49EOl5v', start_index=6666)
Annotation(end_index=6956, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHInLhdrablAMI36jvxQHd3Du0WpOlPHGUYXTclnjs95HQrWj3kJTqqZqfCqwxvV8mOKMjH_-ybWQeDpQNNA5Z03HaaFfU_uJm3d-3JRE5c3WBKHI77YhPrAjjZwLjCyS7M6TIPN-s', start_index=6943)
Annotation(end_index=6956, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtXMYAUEGQXVE06jTQ0IN5fcgtLQ0hhOJCzwrxFtW7Bn8f4gXIqhVE__kUJTWXp5CzbPOQ4JkLduYDUCd0tPP5mB_01r9b0W2Br0DcmJlbC4qPwOQQkzxBwIi33Wx1gAQrdWReW-gE8w==', start_index=6943)
Annotation(end_index=7376, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4GBxe8Y--pMf60fkjQD7Ke8jl7KwbtwvpM4cmx2lPJmvMtMyKJwmIrN3xyAXyRa3HFBsHWmz9O-TLnMBICBWu1LXPZ7hIknrT5MwF6YYdIR5EzrUc0-VigcksL3LqoB-B1siDVH-h', start_index=7362)
Annotation(end_index=7376, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhs4y1kApsr_IWZQiMZX-f5pnWM2dPuXATOTpAnJdyEBOJV-ZzxKdq_N_XWw1Y4U1OFy6sXAMiubRCgyWXB-SY5JqJNOGwoCB23MxiYdY5YHMnwkovvjhLPcxc0b123poSGYZxcfGo', start_index=7362)
Annotation(end_index=7867, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPJNS_sL3OZoRBG5WFOMj9M3y63nuMruqHyzOsblWcfyzr2AbsycV30Uv-fRJcHdhtU5n3YWjOpo2K0x47VDAXN8WebsKlo3HF3E6NXobXhn_qaFGsKiYwdljcntGriq6J7mQfGESRG3RAanL26Ro2ZbLsnZlfOCpwToGm9Zm9ZwbHmtD7q-xAOqQ075So-j9iA8SLxhhi5kPe8q0J-KEPkeLpXSx5rvtxYgvnKUGNijU=', start_index=7853)
Annotation(end_index=7867, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXlsWkXWk6oEkg4w1rfCVBFX96mdXb5MIFgJvdk_ntmyw4mIbo3LuOnJDNMxu-OdWgU78ndRMQGrVgU0xtZbWijwPhCxuVehtI7d5c2hkowFtHOkU3vgw6ZP4W9NikmqVH_qxKimBf', start_index=7853)
Annotation(end_index=8271, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5ac8YgV4sz9Oaumbakc-Ki0Vn0inEwPJTjQBsBk-dEay7JNfuNtGUjRI-zazMiTzBg1fmDYGzhYV1pPF_c9pINgU_uzYbMYUsUh1u6FTPUcCSeyq_0xsdWytqnnB684qbUe5knInu', start_index=8257)
Annotation(end_index=8271, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtSCLlhsvgxGLKdpkg8ZmrPSLfhGB1SZTFZhPtKfNuwmmhYydd6YBOfFj6398s9lneIGgIXMXSXVhK4yrtUDlweDSgzr74ZwXpuieMaK6wruPtxC7mo13fyL790pRllz0sD7UfgWDU', start_index=8257)
Annotation(end_index=8845, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-hwYUU8XFwJxlX7Ya9M9AHY1KUcXLpvGG9D5hM0CxXev8duQGb_spJnV1dqymNNHZlOpsX_EOuAfCQ9A--QRtMWKVj2WlpqWxLI-S-738ilZqd0cXibB5DuDH-8jskRLdQHYg_RkjiPMjDy0n7tvdP4e-P829NSflcUj9FRKDFGc4i8pEW8BlQRIrAcgw6f4UcPYZN1osf6UmVbPRB2dKl7eA', start_index=8831)
Annotation(end_index=8845, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoEbfzweiuYZT2dOFugywaQJyPDTqeD_m2lu5fjv0IEIZ0Q5pQtcTZMA4-NmDg7xGNkMQGWLlpg2jh6aFzFmasqqNDzqaf7yoTf4zVbFHlLubz_eRQtRyu_WtMqhkj6_d27aaRIMSAVRNKVslC7bG1j8xJiKAYYebINxt3CKfxm2tegw5YGL4gmg==', start_index=8831)
Annotation(end_index=9165, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_Sb1Qb-h_XqhanbwH8Nco43isFFKp1THrTZZE1khsoX6Cp3ILNBE0rneuwYD7qflZ9XcS5t78ojQ_lh86qnHHvC9Nfulfqrl55gdEGG_2bpTl_3mWdkc7YukJ7XmANL3iVuvTm2IM', start_index=9151)
Annotation(end_index=9165, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErZeSWJSMHsYxmjnXJekpWbHyhCouYEGjbLBVx6yWM8WMhYuS03UvvjwU6zXkDkyjimsj2P3bJnCp4zdEh0_1sNGnrLDWDM4rD_SIhnCB_FdEk0Zy-69prWeZYk2JYPAvMDkBGtaLtuA==', start_index=9151)
Annotation(end_index=9593, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErZeSWJSMHsYxmjnXJekpWbHyhCouYEGjbLBVx6yWM8WMhYuS03UvvjwU6zXkDkyjimsj2P3bJnCp4zdEh0_1sNGnrLDWDM4rD_SIhnCB_FdEk0Zy-69prWeZYk2JYPAvMDkBGtaLtuA==', start_index=9579)
Annotation(end_index=9593, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8dWUtz25nuIkUSWx5LSxVZK7srAaI0bX8PO0N_bjOHayjkXCiiRenUtLmXDGjkwQfQg9b7xB0JGJsNmz6tAU79ECJfGFfAjGwLTIwjnOM2Zc2vjCpD_Vqvcn0Jh8=', start_index=9579)
Annotation(end_index=9850, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErZeSWJSMHsYxmjnXJekpWbHyhCouYEGjbLBVx6yWM8WMhYuS03UvvjwU6zXkDkyjimsj2P3bJnCp4zdEh0_1sNGnrLDWDM4rD_SIhnCB_FdEk0Zy-69prWeZYk2JYPAvMDkBGtaLtuA==', start_index=9836)
Annotation(end_index=9850, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7CqUog0uHi2Gat0x8r2CUZzXwgeoPHZqKtey_7PpB6uFYRswNPtaVFUCHSeGSf_vTJ9hX2LdW4XEovbQx9FmXtyMWWBXoQJXHXFk_vZJrmNnO1gC3gIwAyqZ1lL89SXgL-rlvd289gEcLluP7ebbewsTTh5PZnQjXiyXYgqjqWa2y7pAUH4qpQzjnQMO2qWI3zzcAclcl65yd3zE18RvMMtdifWkIkUxMp34xOAMK88eCWtVgOsZAqBu_f9VvFC0SppbhEjCATm4-H7OSy5Zyxgjyq5loXM6jvlL1kak-', start_index=9836)
Annotation(end_index=10066, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVG_VhU2z_dME9CZmaTUEFCoT8GiiMiQM65NTal9DoT32PUhRv0HENmZ0oY04FHE40u1s4vX71tOKyobGIoJ8YiKcs4UlBIg6cZtLFgu-kt6YNGyz0wFHMG6TkgOAcXxndP0mRSy3TCw==', start_index=10052)
Annotation(end_index=10066, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIbU001cEN_7hYUhkgKe6cmAZQxizFIWsHUlxEio8OOXJiZuJnShokOA32EzvzG_ONjxn1SwcnByDlFqQjwWKlrnOFJo0cMoxvIV-4yZNJWSH9WsYyJlKtZPi56k_1evCsQaL6MYNrMw==', start_index=10052)
Annotation(end_index=10572, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBvCTFwwWMCWkTTrYUx63n7VD6KIyGnlZALcgmxR2mjVS2BKl1KnhZTlWIedpOvRI7aQAoflLAo0o7jmK0TEzabeZy1JjcWIuKX6eAKRlCO-HzQqBTBMFrXlb7UHDEtvEEl3UVu0Zm', start_index=10558)
Annotation(end_index=10572, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoWy9nGjFC2BllvahVYpzBQC7vc7EvPyJDHD5CoMGAN9EWeecyxWgEjdUopc-MrDOJ-MBoyBhOM1iVTjTuUXwcPJX6m2hKZP69woLE39r1iZnLsDnvcoLIvwEBXr4rCg==', start_index=10558)
Annotation(end_index=10772, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoWy9nGjFC2BllvahVYpzBQC7vc7EvPyJDHD5CoMGAN9EWeecyxWgEjdUopc-MrDOJ-MBoyBhOM1iVTjTuUXwcPJX6m2hKZP69woLE39r1iZnLsDnvcoLIvwEBXr4rCg==', start_index=10758)
Annotation(end_index=10772, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5ac8YgV4sz9Oaumbakc-Ki0Vn0inEwPJTjQBsBk-dEay7JNfuNtGUjRI-zazMiTzBg1fmDYGzhYV1pPF_c9pINgU_uzYbMYUsUh1u6FTPUcCSeyq_0xsdWytqnnB684qbUe5knInu', start_index=10758)
Annotation(end_index=10934, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5ac8YgV4sz9Oaumbakc-Ki0Vn0inEwPJTjQBsBk-dEay7JNfuNtGUjRI-zazMiTzBg1fmDYGzhYV1pPF_c9pINgU_uzYbMYUsUh1u6FTPUcCSeyq_0xsdWytqnnB684qbUe5knInu', start_index=10920)
Annotation(end_index=10934, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoqqv4VgqSYowCnO9QmF8HQ1N5ZDadFc3pUE6z46wOPAwNzIMDgXMGo1G6K2acJAgg4BGiXJc392UqP0bjEWDhDDONQyReZAB3-g2KlFmGuc64gP0YiMGte1jowLm4wL3DWQSyAP2i', start_index=10920)
Annotation(end_index=11084, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBvCTFwwWMCWkTTrYUx63n7VD6KIyGnlZALcgmxR2mjVS2BKl1KnhZTlWIedpOvRI7aQAoflLAo0o7jmK0TEzabeZy1JjcWIuKX6eAKRlCO-HzQqBTBMFrXlb7UHDEtvEEl3UVu0Zm', start_index=11074)
Annotation(end_index=11379, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBvCTFwwWMCWkTTrYUx63n7VD6KIyGnlZALcgmxR2mjVS2BKl1KnhZTlWIedpOvRI7aQAoflLAo0o7jmK0TEzabeZy1JjcWIuKX6eAKRlCO-HzQqBTBMFrXlb7UHDEtvEEl3UVu0Zm', start_index=11365)
Annotation(end_index=11379, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUfiGhSvyKk8eLtcHh8yuPYkZAl1QF3MSguU9uK2bEaXns9bALUowqs8rDEPkqffcbenV941sXh27RcQPH1j63c5cTBFfklcavu5PVqzNWx0JoiF0Xszrs1tOLjbeqW0HXEfyNOBpDeNxrTf0lWVPjXzGhbBPXcQ==', start_index=11365)
Annotation(end_index=11619, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEA2lHPLMFdEHXuv-Dr9rdpjUGRPsK1EeZU8plW8Gi911ePvxB9nOh_PEuHr5tPTsyG4c5SBmVxpVofeyLSvIvxBsYMZDpGtyGSzuCLq98ST00wq6wB-JKT8NUzrxlwZPA=', start_index=11605)
Annotation(end_index=11619, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6bYnPeKT2KxXDuCBCvCPNDtR1dGcL5Bb3v_Y1Q3Gtphd4Oui3cFLkUHiCZETJ4jqy1aIDA_RnzoWyCPsBxT-UwgAc1SyZTjroVAxX3j5AyGrcinwWCIIY4eL3dRev0dJ2ZcRsNHWV', start_index=11605)
Annotation(end_index=12065, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4F2NXzyPbHTN1R0ms9ItJEnrrgqDB03bSeQnn0itHFajiRc1OHrOSH0SE4M0NaB912y_XkcjrlF7clJLjRQhgNCUSDBnyAI28ncIHLRki-b6TJZVWhJ71cWitshG9ZqqM_zdgXwIwbCn7ww==', start_index=12047)
Annotation(end_index=12065, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBtvHoHr7klfO7AxOKx2YndyLym-hRk75N1-qG8raPqMcwe0HbbsFaal141gBET2j_P7HG69KwJFqY8ySOLgGXtwHboqwO4Lhzz3rHla5Kq7N_m0eWp6yX8egYq0vcR5UDLVNyo6njaw==', start_index=12047)
Annotation(end_index=12065, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLuxUUpi3mEpv3HOiqjG8UPd1UZO0H6Vlz4KJfVPArLLUGXqQ4K9RYM02dc2lq3EWPJBZvEktpQw4gUkm9aTaZxc_u1bQxDxYQVk6OgjgRzFlPXELRUQ_q6qOOZIQ2dO-sJ2SzoPnP', start_index=12047)
Annotation(end_index=12360, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6bYnPeKT2KxXDuCBCvCPNDtR1dGcL5Bb3v_Y1Q3Gtphd4Oui3cFLkUHiCZETJ4jqy1aIDA_RnzoWyCPsBxT-UwgAc1SyZTjroVAxX3j5AyGrcinwWCIIY4eL3dRev0dJ2ZcRsNHWV', start_index=12346)
Annotation(end_index=12360, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyJGgowaTsSNEmq6kiUBFbY51hlStmbla4r3jdpalKLVzlXyPFoGtVQ8duo_grmhBGoVl643CQd78Jqj5i6hRZC-c0nwO4U8jl_CXYm5p1ZJw8YSimjm6m8UjtIxQ=', start_index=12346)
Annotation(end_index=12725, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEA2lHPLMFdEHXuv-Dr9rdpjUGRPsK1EeZU8plW8Gi911ePvxB9nOh_PEuHr5tPTsyG4c5SBmVxpVofeyLSvIvxBsYMZDpGtyGSzuCLq98ST00wq6wB-JKT8NUzrxlwZPA=', start_index=12711)
Annotation(end_index=12725, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOrVQafagCcrD-ZPkaB8DxCnPutte7jL1U4erkp2DNJCv8jkP5nPMYmH-v7baD01ubNR1fUtIzW_t5MY-AGppiADP5Tq92aANhrdbnsykumS-Q_EYn2RXRZF3hJYbeCg==', start_index=12711)
Annotation(end_index=13345, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhs4y1kApsr_IWZQiMZX-f5pnWM2dPuXATOTpAnJdyEBOJV-ZzxKdq_N_XWw1Y4U1OFy6sXAMiubRCgyWXB-SY5JqJNOGwoCB23MxiYdY5YHMnwkovvjhLPcxc0b123poSGYZxcfGo', start_index=13331)
Annotation(end_index=13345, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxdRHLYZ3AVPqkTQm_WIguQkhqgDua0VQQe-_-FI74Qb3VrA-sf7KWgJbi0yIuGe-q8WYnduhSVqohuVQ5QN6-7nrvM1lFYRXWvzvpqtYhpoL9wfrKB6GblA==', start_index=13331)
Annotation(end_index=13908, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhs4y1kApsr_IWZQiMZX-f5pnWM2dPuXATOTpAnJdyEBOJV-ZzxKdq_N_XWw1Y4U1OFy6sXAMiubRCgyWXB-SY5JqJNOGwoCB23MxiYdY5YHMnwkovvjhLPcxc0b123poSGYZxcfGo', start_index=13894)
Annotation(end_index=13908, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNO8EJ8lc3B4beNp0XgZQFD3gmGL9U0K_i0xQalPSU6rZvZ9hn-UeUsJ5Br_4UpEF3O5y7uH4m9knHoRNQdYA13e-RaHc5nZBnlgAZGKa7Ea4x1mSCgI_uiIt1I44D', start_index=13894)
Annotation(end_index=14578, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmRoOMSs8iu6XppO5duOcLF_CzevB7KZ9t1T_5xPF62URm44Q1b9q9Pq0WnbpzElTJ1fEHYy2qaz7FmtQBYh_6Y8CQnblSYjHxFbtHkIqgaxL5RmZGmzokRgmlfkdxqhaA', start_index=14561)
Annotation(end_index=14578, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG70B3pRd4E9dxVA8ss-j-NMGpq-E1Z_ChsUYvobXrMdLOtd-ogcMr7T7mIPDpiB8LlhvVAppLwGBMLgQ4R9X7aBSXP237WQ9_BxYh9UzUAWPlEvrcF66ufhAkS8sXYnQ2roXJWUP0n', start_index=14561)
Annotation(end_index=14578, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8e-jkJpV6dRGc0Aq8DnxnMD7FAWsIW81yj-FFBiCatsB3EWpkOoTYtQA8ObhHP1mk2gFtILQZM0d691ZcFT8MvgfvwfbntXJaedFAbujOyF_45F05EbgWlouvlcNhceS8', start_index=14561)
Annotation(end_index=14823, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZkFYe8ws2YvzCb0ZNCM0af71Vzt3RRlRKXFCyX6cQIcNzPFzMhUZFop0Zq1xCg7xFjXKQX8Y0w9mAKGrB6YgAKP20IFbGM12Q8CQdmcwwPCoBikBNqn8qV-vL6CEtFzxr43X6_3jE3w==', start_index=14809)
Annotation(end_index=14823, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG70B3pRd4E9dxVA8ss-j-NMGpq-E1Z_ChsUYvobXrMdLOtd-ogcMr7T7mIPDpiB8LlhvVAppLwGBMLgQ4R9X7aBSXP237WQ9_BxYh9UzUAWPlEvrcF66ufhAkS8sXYnQ2roXJWUP0n', start_index=14809)
Annotation(end_index=15381, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGB2wdV0ufwMCOvHpwnD24lgxRg64tezmKYzy5RJdQ-sEeoG6IU2WXQQ0Mp9zzlOid4n-Q1sGJWXx-e1xgWoHc47hs8qBqftVcC0d1T_OR-Cq2O6or3j4nw0unfbvwf1_MVTV9TxKOBkYVRLNAMrY6iMPZ2CoPlJ38arU7dfechbHmWOZ15q-okq-mVO8l-8XbAGQNFmru5gDdRxmhWKIvqaJisvmm3r3plvfILB4XwATJX9uZOucP0s_cl-IcGykBMPYL3EpDi8zc=', start_index=15367)
Annotation(end_index=15381, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbFv_ecG4wsjzHoIlsoJ71eyVd4zJ_lVjwILpKtaW0y_66EpBQV76LCUYXiZmLKECFFAU22gIftrt9NnifBQBD3JQMJrtLXgVALFUnGsqOR-mJio0BdIhgQ1cd4MkF', start_index=15367)
Annotation(end_index=15731, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRHJ1NUYfbc2EYttNkT9iRsdHhOjb5IQVW5LxqW-Jn6Bg5R-4QeKvv0dHZIUk2Dlrclg2ZMLjPDCBuf6a6NT61RBJCJoWwdydWUBrZjGp_nb3dpLqTAXaxN4PIrLE9N-mA-cXaxYCw', start_index=15713)
Annotation(end_index=15731, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAUivXdfcsXVw6FGgRvpbxtps5Of4E3IhPk-ZbNBKNh27W5kPD4OgJrDywgye-QhjQNrAsoxmhWZAoEXbi2hFITCT3FVi8-tsmOdhqBEK06q26-kADdl6iW5XRE4fcAVW1ygsV0Rne8A==', start_index=15713)
Annotation(end_index=15731, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbYe8YqfnhaaJWizIm00fdrJ1tw-us8hKFIfGG-mTSg8vtrwPobDzSu39HojiNdqHFuscwcMxE6oLeZfmcjfmZBGKp-b65HVLK8oqJmFl8NqxomLR2tC3RxfhdhDpz7DssnJb7GGVyTwrXHnzeAYtOBKtHWlUM7UPzBo9kpbPwxamVhn6AIgd61DZvdE6zRO4=', start_index=15713)
Annotation(end_index=15989, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKBiOvCpPppimWI_FQMfQ4I5Vv_wxZ-uWb3k0c7ck2ggcHkolMj6eUqdeok7YBh8S9mI3VP4eNJogitdJXf_bTNXyBa8RWzxFpji8XTcZPttjyvCnburMkfGgJYodqTm9a0nQeYQXh', start_index=15971)
Annotation(end_index=15989, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF52YGpSJSlsh0Uv4g5KUtA5OE7MYTs1QBDJHbpAUyxLFw7sVAwVB_uUppQaz8NzZmG7FpFDDp-rPbEZc6QnGEt5MPIq0ap0o438E--wSuHT59fPpT12CjB6G63doA=', start_index=15971)
Annotation(end_index=15989, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAUivXdfcsXVw6FGgRvpbxtps5Of4E3IhPk-ZbNBKNh27W5kPD4OgJrDywgye-QhjQNrAsoxmhWZAoEXbi2hFITCT3FVi8-tsmOdhqBEK06q26-kADdl6iW5XRE4fcAVW1ygsV0Rne8A==', start_index=15971)
Annotation(end_index=16303, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAUivXdfcsXVw6FGgRvpbxtps5Of4E3IhPk-ZbNBKNh27W5kPD4OgJrDywgye-QhjQNrAsoxmhWZAoEXbi2hFITCT3FVi8-tsmOdhqBEK06q26-kADdl6iW5XRE4fcAVW1ygsV0Rne8A==', start_index=16289)
Annotation(end_index=16303, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWLmbn7Fut3KdD0Q0XT-wTdn2P9EwqrvIL40V8FoihttEbUSYNGAbpMMfbBnYuVFSdinaPry1DE5N4ZNntp_RNcgAFJ4xAQDuKRm0YmlRpefXRsPpLXHxMDpH53ejcAMOx0CP0RkKY4JdqBeYOTGUTnDGgQZ5lPqUafJUNxmDcCiLbh9Wy-w--wimKo1266t9gR98vRXpcCx7wDceeiOXGozU0Ed28lDanQXO0Nse38cXOl8iis-vJVATQPEmFYzIG-gMYi3wmDn-H66zqqmpYe5V6', start_index=16289)
Annotation(end_index=16851, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFl2NE8gJh8dr6JjkSUovVjTYSC9It4iiibg_13tgiepQ3iQWx7rpJeI29gf1oCBUpXsrdEr7618eft3rwLFiQRKPqQppuuxLpdAZK394fsROtmSpqdKb_Hy5hr6NcZY8AiZMw-V_OnNQvTuU6UEYei--w5NWSa', start_index=16838)
Annotation(end_index=16851, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzg9JxHl8q0XKDhPDV3mk9uKMoMcKJAsk9RJiPtGsHDf0qnggAWsYYhic2dmsTArupAT-xkcAOKqIFF9sTMjPJzcONCLlSU0miGQB7VowI2ZlzRvMyQC424n7vEYBjoEyZ0YHhHO7tmfG7QufQUzPXvrcA17dFye570IGa1BlI4-p-fvpuT5lPS03D4nDF_GgMcz_g1WzraKzBV6a5UsEzcDyKp0NzCW63Xyhn0-afM0woxtQLneNmsf0I', start_index=16838)
Annotation(end_index=17067, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzg9JxHl8q0XKDhPDV3mk9uKMoMcKJAsk9RJiPtGsHDf0qnggAWsYYhic2dmsTArupAT-xkcAOKqIFF9sTMjPJzcONCLlSU0miGQB7VowI2ZlzRvMyQC424n7vEYBjoEyZ0YHhHO7tmfG7QufQUzPXvrcA17dFye570IGa1BlI4-p-fvpuT5lPS03D4nDF_GgMcz_g1WzraKzBV6a5UsEzcDyKp0NzCW63Xyhn0-afM0woxtQLneNmsf0I', start_index=17055)
Annotation(end_index=17067, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0cLkO5mmuw0FkqYdet-iPd3-vfhfZ2UaLJbIfG6cQjr91Zn_quSizlAFejXGBw-kz0qSOMc0nGMBHXnU4MFiyzvhBeFeZ_73BiqaxGkZXPSPOxAtGsf6fsdEADt4Dbkm7cMe6HHXi', start_index=17055)
Annotation(end_index=17351, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoWy9nGjFC2BllvahVYpzBQC7vc7EvPyJDHD5CoMGAN9EWeecyxWgEjdUopc-MrDOJ-MBoyBhOM1iVTjTuUXwcPJX6m2hKZP69woLE39r1iZnLsDnvcoLIvwEBXr4rCg==', start_index=17338)
Annotation(end_index=17351, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL3Fn2hMoDqg1NlU_DIKPVobBQ2cRq9LdF2IvHSNxGvQApoHwUYC_hz66v9JiDoZteK93dkXjnZ9iH0lLGYzz3lcXb6YavV6Bm9vpWCL9nVzaC9VSHDwo5OTOwXuYXwPhDTJuKOk5A', start_index=17338)
Annotation(end_index=17629, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEn1RmbGGAa6Yhw1xxVQR3PkoIToXyfSTaPJO1Gb-4mtWYqfpOat4z-yaUdPoEF3-vZ5J3l_qMhXeA27LdYfliEokdG6gG8sK8z0-a17EDet1PzVe0bB02pEWfNaPxFZEIhYHD1v3Zh', start_index=17619)
Annotation(end_index=18031, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBtvHoHr7klfO7AxOKx2YndyLym-hRk75N1-qG8raPqMcwe0HbbsFaal141gBET2j_P7HG69KwJFqY8ySOLgGXtwHboqwO4Lhzz3rHla5Kq7N_m0eWp6yX8egYq0vcR5UDLVNyo6njaw==', start_index=18021)
Annotation(end_index=18285, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVG_VhU2z_dME9CZmaTUEFCoT8GiiMiQM65NTal9DoT32PUhRv0HENmZ0oY04FHE40u1s4vX71tOKyobGIoJ8YiKcs4UlBIg6cZtLFgu-kt6YNGyz0wFHMG6TkgOAcXxndP0mRSy3TCw==', start_index=18275)
Annotation(end_index=18789, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZEm_I8DRZtIJPSAh7CA7hwMezhT1TvPRWkmLPGRTb46-olJCiCaSJUZUrrUETEuCoKu_-ZdbkUVdrdJ96mYHidqiX8snIRLpDTrLFxS5Tc3TwUgA06kEEmbliI7-puwfil85Az1yeJFcxgdYIRbbq49OTWry1EIjVMQj7fiK1wgS7', start_index=18777)
Annotation(end_index=18789, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL3Fn2hMoDqg1NlU_DIKPVobBQ2cRq9LdF2IvHSNxGvQApoHwUYC_hz66v9JiDoZteK93dkXjnZ9iH0lLGYzz3lcXb6YavV6Bm9vpWCL9nVzaC9VSHDwo5OTOwXuYXwPhDTJuKOk5A', start_index=18777)
Annotation(end_index=18847, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG70B3pRd4E9dxVA8ss-j-NMGpq-E1Z_ChsUYvobXrMdLOtd-ogcMr7T7mIPDpiB8LlhvVAppLwGBMLgQ4R9X7aBSXP237WQ9_BxYh9UzUAWPlEvrcF66ufhAkS8sXYnQ2roXJWUP0n', start_index=18834)
Annotation(end_index=18847, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8e-jkJpV6dRGc0Aq8DnxnMD7FAWsIW81yj-FFBiCatsB3EWpkOoTYtQA8ObhHP1mk2gFtILQZM0d691ZcFT8MvgfvwfbntXJaedFAbujOyF_45F05EbgWlouvlcNhceS8', start_index=18834)
Annotation(end_index=18893, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4GBxe8Y--pMf60fkjQD7Ke8jl7KwbtwvpM4cmx2lPJmvMtMyKJwmIrN3xyAXyRa3HFBsHWmz9O-TLnMBICBWu1LXPZ7hIknrT5MwF6YYdIR5EzrUc0-VigcksL3LqoB-B1siDVH-h', start_index=18880)
Annotation(end_index=18893, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtXMYAUEGQXVE06jTQ0IN5fcgtLQ0hhOJCzwrxFtW7Bn8f4gXIqhVE__kUJTWXp5CzbPOQ4JkLduYDUCd0tPP5mB_01r9b0W2Br0DcmJlbC4qPwOQQkzxBwIi33Wx1gAQrdWReW-gE8w==', start_index=18880)
Annotation(end_index=18947, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_Sb1Qb-h_XqhanbwH8Nco43isFFKp1THrTZZE1khsoX6Cp3ILNBE0rneuwYD7qflZ9XcS5t78ojQ_lh86qnHHvC9Nfulfqrl55gdEGG_2bpTl_3mWdkc7YukJ7XmANL3iVuvTm2IM', start_index=18933)
Annotation(end_index=18947, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8dWUtz25nuIkUSWx5LSxVZK7srAaI0bX8PO0N_bjOHayjkXCiiRenUtLmXDGjkwQfQg9b7xB0JGJsNmz6tAU79ECJfGFfAjGwLTIwjnOM2Zc2vjCpD_Vqvcn0Jh8=', start_index=18933)
Annotation(end_index=18990, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoWy9nGjFC2BllvahVYpzBQC7vc7EvPyJDHD5CoMGAN9EWeecyxWgEjdUopc-MrDOJ-MBoyBhOM1iVTjTuUXwcPJX6m2hKZP69woLE39r1iZnLsDnvcoLIvwEBXr4rCg==', start_index=18976)
Annotation(end_index=18990, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5ac8YgV4sz9Oaumbakc-Ki0Vn0inEwPJTjQBsBk-dEay7JNfuNtGUjRI-zazMiTzBg1fmDYGzhYV1pPF_c9pINgU_uzYbMYUsUh1u6FTPUcCSeyq_0xsdWytqnnB684qbUe5knInu', start_index=18976)
Annotation(end_index=19034, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGB2wdV0ufwMCOvHpwnD24lgxRg64tezmKYzy5RJdQ-sEeoG6IU2WXQQ0Mp9zzlOid4n-Q1sGJWXx-e1xgWoHc47hs8qBqftVcC0d1T_OR-Cq2O6or3j4nw0unfbvwf1_MVTV9TxKOBkYVRLNAMrY6iMPZ2CoPlJ38arU7dfechbHmWOZ15q-okq-mVO8l-8XbAGQNFmru5gDdRxmhWKIvqaJisvmm3r3plvfILB4XwATJX9uZOucP0s_cl-IcGykBMPYL3EpDi8zc=', start_index=19020)
Annotation(end_index=19034, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbFv_ecG4wsjzHoIlsoJ71eyVd4zJ_lVjwILpKtaW0y_66EpBQV76LCUYXiZmLKECFFAU22gIftrt9NnifBQBD3JQMJrtLXgVALFUnGsqOR-mJio0BdIhgQ1cd4MkF', start_index=19020)
Annotation(end_index=19079, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhs4y1kApsr_IWZQiMZX-f5pnWM2dPuXATOTpAnJdyEBOJV-ZzxKdq_N_XWw1Y4U1OFy6sXAMiubRCgyWXB-SY5JqJNOGwoCB23MxiYdY5YHMnwkovvjhLPcxc0b123poSGYZxcfGo', start_index=19065)
Annotation(end_index=19079, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxdRHLYZ3AVPqkTQm_WIguQkhqgDua0VQQe-_-FI74Qb3VrA-sf7KWgJbi0yIuGe-q8WYnduhSVqohuVQ5QN6-7nrvM1lFYRXWvzvpqtYhpoL9wfrKB6GblA==', start_index=19065)
Annotation(end_index=19137, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBtvHoHr7klfO7AxOKx2YndyLym-hRk75N1-qG8raPqMcwe0HbbsFaal141gBET2j_P7HG69KwJFqY8ySOLgGXtwHboqwO4Lhzz3rHla5Kq7N_m0eWp6yX8egYq0vcR5UDLVNyo6njaw==', start_index=19123)
Annotation(end_index=19137, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLuxUUpi3mEpv3HOiqjG8UPd1UZO0H6Vlz4KJfVPArLLUGXqQ4K9RYM02dc2lq3EWPJBZvEktpQw4gUkm9aTaZxc_u1bQxDxYQVk6OgjgRzFlPXELRUQ_q6qOOZIQ2dO-sJ2SzoPnP', start_index=19123)

## Sources
