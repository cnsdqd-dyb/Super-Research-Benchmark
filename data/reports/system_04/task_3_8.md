# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** dc6d88a3 | **Time:** 261.45s | **Cost:** $1.13111
--------------------------------------------------------------------------------

# Temporal Dynamics and Metabolic Clearance in CYP450 Induction Research: Balancing Exposure Time with Enzyme Activity

### Key Points
*   **Mechanism of Delay:** Unlike direct inhibition, which occurs rapidly based on drug concentration, CYP450 induction is a transcriptional process requiring the synthesis of new enzyme proteins. Consequently, the time to reach maximal metabolic clearance effects is governed primarily by the degradation half-life of the enzyme ($k_{deg}$), not just the elimination half-life of the inducer.
*   **The 14-Day Standard:** Research and regulatory guidance generally converge on a 14-day administration period for strong inducers (e.g., rifampin) in clinical drug-drug interaction (DDI) studies. This duration ensures that enzyme synthesis reaches a new steady state, preventing the underestimation of clearance changes that could lead to therapeutic failure of co-administered drugs.
*   **De-induction Lag:** The return to baseline metabolic activity (de-induction) is a slow, first-order process dependent on the natural turnover of the induced proteins. This "washout" period often exceeds the time required to eliminate the inducing drug from the plasma, necessitating prolonged monitoring in clinical practice.
*   **Modeling Integration:** Physiologically based pharmacokinetic (PBPK) modeling is increasingly used to balance trial duration with scientific rigor. These models utilize in vitro data to predict the time course of induction, though accurate predictions are currently limited by variability in estimates of human CYP turnover rates (e.g., CYP3A4 half-life estimates range from 10 to 140 hours).

### Introduction
In the field of pharmacokinetics and drug development, the accurate characterization of cytochrome P450 (CYP450) enzyme induction is critical for predicting clinical drug-drug interactions (DDIs). Unlike enzyme inhibition, which often involves direct interference with the active site and occurs rapidly, enzyme induction is an adaptive biological response involving the upregulation of gene transcription and the subsequent synthesis of new enzyme proteins [cite: 1, 2]. This fundamental difference introduces a significant temporal dimension to research design: the exposure time of the inducer must be carefully balanced against the magnitude of change in metabolic clearance to capture the true extent of the interaction.

The "balance" in this context refers to the optimization of study duration to ensure that the maximal effect on metabolic clearance is observed without extending clinical trials unnecessarily. If the inducer exposure time is insufficient, the enzyme levels may not reach a new steady state, leading to an underestimation of the clearance increase and a false assurance of safety regarding the object drug's efficacy [cite: 3, 4]. Conversely, understanding the kinetics of enzyme degradation is essential for determining how long the interaction persists after the inducer is discontinued (de-induction) [cite: 5]. This report examines the interplay between inducer pharmacokinetics, enzyme turnover rates, and metabolic clearance significance, synthesizing current regulatory standards and mechanistic modeling approaches.

## 1. Mechanisms of CYP450 Induction and Temporal Latency

To understand why exposure time is the critical variable in induction research, one must first understand the molecular mechanism. Induction is not an instantaneous event but a cascade of intracellular signaling.

### 1.1 Transcriptional Activation
The most common mechanism of CYP450 induction is receptor-mediated transcriptional gene activation. Xenobiotics (inducers) enter the hepatocyte and bind to nuclear receptors, which act as transcription factors. The primary receptors involved include:
*   **Pregnane X Receptor (PXR):** Primarily induces the CYP3A and CYP2C subfamilies [cite: 2, 6].
*   **Constitutive Androstane Receptor (CAR):** Primarily induces the CYP2B family [cite: 2, 6].
*   **Aryl Hydrocarbon Receptor (AhR):** Primarily induces the CYP1A family [cite: 2, 6].

Upon ligand binding, these receptors translocate to the nucleus, heterodimerize (often with the Retinoid X Receptor), and bind to response elements in the promoter regions of target genes. This leads to increased mRNA transcription, followed by translation into functional protein [cite: 7, 8].

### 1.2 The Lag Phase
Because induction requires the synthesis of new proteins, there is an inherent lag phase between the administration of the inducer and the observable increase in metabolic clearance. This contrasts sharply with competitive inhibition, where the effect is immediate upon the inhibitor reaching the enzyme site.
*   **Onset Latency:** An increase in enzyme activity is usually not observable immediately. For example, while rifampin has a short plasma half-life (~4 hours), the time required to produce maximum enzyme induction is much longer because the liver must physically manufacture additional enzyme [cite: 3].
*   **Steady-State Induction:** The system eventually reaches a new steady state where the rate of enzyme synthesis (elevated by the inducer) equals the rate of enzyme degradation. The time to reach this plateau is the critical factor in designing DDI studies [cite: 3, 9].

## 2. Balancing Exposure Time: The Role of Enzyme Turnover

The central challenge in designing induction studies is determining how long to administer the inducer to ensure maximal metabolic clearance changes are captured. This duration is governed by the interplay between the pharmacokinetics of the inducer and the turnover kinetics of the enzyme itself.

### 2.1 Enzyme Degradation Half-Life ($k_{deg}$)
The time required for induction to reach steady state is determined by the degradation rate constant ($k_{deg}$) of the enzyme, provided the elimination half-life of the inducer is shorter than the enzyme turnover half-life [cite: 3, 10].
*   **First-Order Process:** The accumulation of enzyme follows first-order kinetics, similar to the accumulation of a drug to steady state. It typically takes 3.3 to 5 half-lives of the *enzyme* (not necessarily the drug) to reach a new steady-state protein level [cite: 3, 9].
*   **Variability in Estimates:** A significant limitation in current research is the lack of consensus on the in vivo turnover half-lives of human CYP enzymes. For CYP3A4, reported turnover half-lives range widely from 10 to 140 hours [cite: 9, 11]. This uncertainty complicates the precise prediction of the time to maximal induction.
*   **General Estimates:** Evidence suggests that the enzyme turnover half-life is approximately 3 days for CYP3A4 and 4 days for CYP1A2. This implies that maximal induction could theoretically take several weeks, although clinical protocols often standardize this to shorter periods [cite: 10].

### 2.2 Inducer Half-Life vs. Enzyme Half-Life
The time to steady-state induction depends on which half-life is longer: the drug's or the enzyme's.
*   **Short Half-Life Inducers (e.g., Rifampin):** Rifampin has a half-life of ~3-5 hours. Since this is much shorter than the degradation half-life of CYP enzymes (days), the time to maximal induction is rate-limited by the enzyme turnover. Consequently, even though rifampin is cleared quickly, it must be administered for 10–14 days to allow enzyme levels to plateau [cite: 3].
*   **Long Half-Life Inducers (e.g., Phenobarbital):** Phenobarbital has a very long half-life (up to 5 days). In this case, the time to reach steady-state *drug* concentrations is the rate-limiting step. It may take weeks for phenobarbital to accumulate to therapeutic levels, and enzyme induction will rise in parallel with the drug concentration. Therefore, maximal induction may take 2–3 weeks or longer to manifest fully [cite: 3, 12].

### 2.3 The 14-Day Consensus
To balance these variables and ensure safety margins, regulatory bodies and researchers have converged on a standard duration for clinical DDI studies involving strong inducers.
*   **Standard Protocol:** It is common practice to administer the inducer for at least 14 days before assessing the pharmacokinetics of the substrate drug [cite: 4, 13].
*   **Scientific Basis:** Simulations and clinical data indicate that 14 days allows for >90% of the maximal induction to be realized for most major CYP enzymes, covering the turnover requirements for both the enzyme and most inducers [cite: 4, 14].
*   **Exceptions:** Some studies suggest that for specific enzymes and potent inducers like rifampin, maximal induction of intestinal CYP3A4 may occur faster (within 5 days) than hepatic CYP3A4 (10 days) [cite: 15]. However, the 14-day rule remains the conservative standard to avoid under-predicting the interaction [cite: 4].

## 3. Metabolic Clearance Significance: Magnitude of Effect

The "significance" of metabolic clearance refers to the clinical impact of the induced state. Induction increases the intrinsic clearance ($CL_{int}$) of the victim drug, leading to reduced systemic exposure (AUC) and peak concentrations ($C_{max}$).

### 3.1 Impact on Pharmacokinetics
The increase in enzyme abundance leads to a proportional increase in hepatic clearance for drugs with low extraction ratios.
*   **Reduction in Efficacy:** The primary clinical concern with induction is the loss of therapeutic efficacy. For example, rifampin can reduce the AUC of rosiglitazone (a CYP2C8 substrate) by approximately 65% and reduce its half-life from 3.9 to 1.5 hours [cite: 16, 17]. Similarly, rifampin reduces the exposure of vilaprisan by 96%, rendering it ineffective [cite: 18].
*   **Extraction Ratio Considerations:** For high-extraction ratio drugs, induction may have a minimal effect on hepatic clearance (which is blood-flow limited) but can significantly reduce oral bioavailability by increasing first-pass metabolism [cite: 19].

### 3.2 Auto-induction
Some drugs induce their own metabolism (auto-induction), complicating the assessment of exposure time.
*   **Mechanism:** A drug acts as a ligand for a nuclear receptor that upregulates the enzyme responsible for its own elimination.
*   **Time Course:** This results in time-dependent pharmacokinetics where the drug's half-life decreases over time. For example, carbamazepine induces CYP3A4 (its own metabolizer). It must be initiated at a low dose and titrated upward because its clearance increases over the first few weeks of therapy [cite: 12].
*   **Research Implication:** In DDI studies involving auto-inducers, the "precipitant" drug must be dosed long enough to reach its own induced steady state before the "object" drug is introduced [cite: 7].

### 3.3 Toxicological Significance
While reduced efficacy is the most common outcome, induction can also increase toxicity if the metabolite is reactive.
*   **Acetaminophen:** Induction of CYP2E1 (e.g., by ethanol or isoniazid) increases the conversion of acetaminophen to its toxic metabolite, NAPQI. This lowers the threshold for hepatotoxicity [cite: 20].
*   **Research Balance:** In these cases, research must balance the duration of inducer exposure to ensure that the formation rate of the toxic metabolite is accurately characterized at steady state.

## 4. De-induction: The Return to Baseline

Balancing exposure time also requires understanding the "offset" or de-induction phase. When the inducer is stopped, elevated enzyme levels do not return to baseline immediately.

### 4.1 Kinetics of De-induction
De-induction is governed by the degradation rate of the enzyme ($k_{deg}$) and the elimination of the inducer.
*   **Lag Effect:** Even after the inducer is cleared from the plasma, the excess enzyme remains active until it is naturally degraded. This process is slower than the offset of inhibition [cite: 3].
*   **Timeframe:** It typically takes 2 to 4 weeks for enzyme activity to return to baseline after discontinuing a strong inducer like rifampin. For example, rifampin-induced midazolam clearance required roughly 2–4 weeks to normalize, with a calculated de-induction half-life of ~7.7 days [cite: 3].

### 4.2 Clinical and Research Implications
*   **Washout Periods:** In crossover study designs, the washout period between treatment arms must be sufficiently long (often 3–4 weeks) to ensure no residual induction affects the subsequent phase [cite: 5].
*   **Dose Adjustment:** Clinicians are advised to maintain dose adjustments for the object drug for at least 2 weeks after the inducer is stopped to avoid toxicity as clearance normalizes [cite: 4, 13].

## 5. Regulatory Guidelines and In Vitro-In Vivo Extrapolation (IVIVE)

Regulatory agencies (FDA, EMA) provide specific guidance on how to balance exposure time with metabolic clearance assessment in drug development.

### 5.1 In Vitro Assessment
Before clinical trials, induction potential is screened in vitro using human hepatocytes.
*   **Incubation Time:** The FDA suggests incubation times of 48–72 hours for hepatocytes to allow sufficient time for mRNA upregulation and protein synthesis [cite: 21].
*   **Endpoints:** Induction is assessed by measuring mRNA levels (fold-change) and enzyme activity. A concentration-dependent increase in mRNA >2-fold typically triggers the need for clinical evaluation [cite: 22].
*   **Optimization:** Recent industry working groups have suggested that 48 hours is the primary time point for in vitro assessment, as 72 hours offers no further benefit in predicting risk [cite: 21].

### 5.2 In Vivo Clinical Design
If in vitro signals are positive, a clinical DDI study is required.
*   **Duration:** The FDA guidance emphasizes that inducers should be administered for a sufficient duration to achieve maximal induction. While 14 days is the standard, shorter durations (e.g., 10 days) may be acceptable if justified by mechanistic modeling or the specific half-life of the inducer [cite: 23, 24].
*   **Substrate Timing:** The substrate (victim drug) is typically administered on the last day of inducer treatment or after steady state is confirmed.
*   **Cocktail Studies:** To maximize efficiency, researchers often use "cocktail" studies where multiple probe substrates (e.g., midazolam for CYP3A4, caffeine for CYP1A2) are administered simultaneously after the induction period to assess multiple enzymes at once [cite: 3].

## 6. Mathematical and PBPK Modeling

Given the logistical burden of long clinical trials, Physiologically Based Pharmacokinetic (PBPK) modeling has become a vital tool for balancing exposure time and predicting clearance changes.

### 6.1 The Turnover Model
The change in enzyme amount ($E$) over time is described by the zero-order synthesis rate ($k_{syn}$) and the first-order degradation rate ($k_{deg}$):
\[ \frac{dE}{dt} = k_{syn} - k_{deg} \cdot E \]
Induction increases $k_{syn}$. The time to reach the new steady state is determined by $k_{deg}$ [cite: 9, 25].

### 6.2 PBPK Applications
PBPK models integrate in vitro induction parameters ($E_{max}$, $EC_{50}$) with system parameters (enzyme turnover) to simulate the time course of induction.
*   **Predicting Time to Steady State:** Models can simulate whether a 10-day study will yield results comparable to a 14-day study, potentially saving time and resources [cite: 11, 18].
*   **Sensitivity Analysis:** Because $k_{deg}$ values are uncertain, researchers perform sensitivity analyses to see how different enzyme half-lives affect the predicted interaction magnitude. This helps quantify the confidence in the safety margins [cite: 9].
*   **Complex Interactions:** PBPK is particularly useful for drugs that are both inhibitors and inducers (e.g., rifampin inhibits OATP1B1 transporters acutely but induces CYP3A4 chronically). Modeling helps disentangle these opposing effects over time [cite: 26, 27].

## 7. Conclusion

In drug interaction research, the balance between inducer exposure time and metabolic clearance significance is dictated by the biological reality of protein turnover. Unlike the rapid onset of inhibition, CYP450 induction is a slow, adaptive process. The "significance" of the metabolic clearance change—often a dramatic reduction in drug exposure—can only be accurately assessed if the inducer is administered long enough for enzyme synthesis to reach a new steady state.

Current consensus and regulatory guidance point to a **14-day exposure period** as the gold standard for strong inducers to avoid underestimating clinical risk. This duration accounts for the degradation half-life of the enzyme, which is the rate-limiting step in the accumulation of catalytic activity. Furthermore, the slow offset of induction (de-induction) requires that safety monitoring and washout periods extend weeks beyond the discontinuation of the inducer. As PBPK modeling evolves, it offers the potential to refine these timelines, but the fundamental dependence on enzyme turnover kinetics remains the cornerstone of robust study design.

## References
[cite: 1] Pharmacist Academy. (2021). CYP450 Enzymes Drug Interactions MADE EASY.
[cite: 3] Horn, J. R., & Hansten, P. D. (2011). Enzyme Induction Time Course. Pharmacy Times.
[cite: 13] Bettonte, S., et al. (2023). Evaluation of the Time to Maximal Induction... Springer.
[cite: 7] FDA. (2006). Drug-Drug Interaction Guidance.
[cite: 2] Charles River. (n.d.). Cytochrome P450 Interaction Assays.
[cite: 22] Admescope. (2020). The 2020 FDA Guidance for In Vitro DDI Studies.
[cite: 23] FDA. (2017). Clinical Drug Interaction Studies — Study Design, Data Analysis, and Clinical Implications.
[cite: 21] Fahmi, O. A., et al. (2020). Time Course for Cytochrome P450 Induction in Primary Human Hepatocytes.
[cite: 6] Charles River. (n.d.). Drug-Drug Interaction Studies.
[cite: 12] AAFP. (2007). Drug Interactions: A Review.
[cite: 7] Hewitt, N. J., et al. (2007). Induction of drug metabolizing enzymes...
[cite: 20] Taylor & Francis. (2018). Enzyme induction.
[cite: 9] Yang, J., et al. (2008). Cytochrome P450 turnover: regulation of synthesis and degradation...
[cite: 8] Riley, R. J., & Wilson, C. E. (2015). Cytochrome P450 time-dependent inhibition and induction...
[cite: 5] HCT. (2025). Duration of drug interactions...
[cite: 25] PubMed. (1979). Pharmacokinetic theory of induction.
[cite: 3] Pharmacy Times. (2011). Enzyme Induction Time Course.
[cite: 19] LITFL. (2021). Hepatic Drug Metabolism.
[cite: 16] Park, J. Y., et al. (2004). Effect of rifampin on the pharmacokinetics of rosiglitazone...
[cite: 17] Drugs.com. (2011). Rifabutin and Rosiglitazone Interactions.
[cite: 24] FDA. (1997). Guidance for Industry: In Vivo Drug Metabolism/Drug Interaction Studies.
[cite: 26] FDA. (2013). Drug Interaction Studies.
[cite: 4] Bettonte, S., et al. (2023). Time to reach maximal enzyme induction...
[cite: 14] ResearchGate. (2025). Duration of drug interactions...
[cite: 3] Pharmacy Times. (2011). Enzyme Deinduction Time Course.
[cite: 15] ResearchGate. (2025). Guidance for Rifampin and Midazolam Dosing Protocols...
[cite: 18] Gerisch, M., et al. (2018). Physiologically Based Pharmacokinetic Modeling...
[cite: 27] Baneyx, G., et al. (2014). Clinical DDI study design for RIF...
[cite: 28] PubMed. (2022). Time course of CYP3A modulation...
[cite: 11] PLOS ONE. (2013). Modeling of the induction dynamics...
[cite: 10] ResearchGate. (2016). What is the clinical importance of determining CYP half-life...

**Sources:**
1. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoFDPfupsGmiw9R9q8rQ0OlzAiey1GHYluzS0eev0RiuK26eaubMKGAt5veH0bR_R6o1LZI7sg06vTFJUlBs4QIT9DUzpYqzxxgtJkjnu-fADcluzrDghe2GssnHCBbSIg)
2. [criver.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4HQZbICNlj1vKICyAmmAhqZmYRpgDuIHcZ8Ud3j2K0nYhnj8z45z60qyUGbgK9N5vm7OqiUkXWKNaiiWeP7wHHP9TMLBDMeB5CB257QOJ4vrvh1JJW5A6CjwXRhhekEkmwYNsGSsd9ppJk5laR5IGW7QSogxUwYP3OikUZXWIt_At5q2cORUDsdd9vGpg2YdyGcU=)
3. [pharmacytimes.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy2pBLt3-JFTEePeyyAGA7RG8boVN7fDYwlTErpvHU7f-NMOVBQcJwvowCpUL5Jx_dJXE1ECPLQtF84l23xN6KM7CtsdR_Ybpl3gCcWxR8SCzna5VITSXLxXXVkCQkhEsJUgQAETgq_OKseiSqKQ==)
4. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmMU5z2kLp738rjJfhBObNFhRWtMY4TITI0Lm22cDtGoAD64ixuyDE_KLKNVYs2x3WDlN8mMhFC5yprV1Lh-AOTlrP4z0wtZNCyf40_bRZMtl2JFLioK-LK0s9z2ecMQwsnI8B9Oj43A==)
5. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEr6nW0hArlux6iTFDNgsuatbyvaFJda5kgdcsvCTb5SboTraXQyCg0jQW5A36DJY-E7YYMN5ull7wFVkRIsjvEpzO_LgWNky0zXmrEDDpSimfvcx7y0vIejr6QSxLZvJzDSE_gmhNVyi83ZcTZTmcsnlLHiFpwm91W1SdnpoT3uJnFfS4uHFQroHMK1ldVDg0prLSjWynM2ZY=)
6. [criver.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdcQoP3rPS4Ke10xPkZq8ZCermzehOGqKthedlLWcj78pYqEr7wj4dC03YDfosKS3LQ0Ol_j5aTCcEWh1H015J70we1vsorqIO8YrBrJeKwZ03HTgXYzem4gA738Z7_Y9KaUi1CZM2IOF5nPTMzaMQyUib3qBaZyfo0UuBQLFviedt7e0JYcfJvFEFc3H7)
7. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElUAGDBcQLqTQpWLKz3q15N4AR1ux37CBHKG4Dq3fN3592587LtR8PMsYEvZAon3UXqsn-UX01gAcqCyaKFF9ethgO7XxCUFTpsxm4DcrGMPDN8Kk6xQrqziscIOf_oTe5jsNoGhiT)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFR_ug2vfUnB5l7y2QhOAuMlalXJUWfLGSXhZ3qSmUlJj0dFID2hJHo3r_WZV0-yrP0PoXy19_dBB-g0KLY9FTSE2ABR0L_xk29hYRW-KPuiqNfUHweAATiT7P7mBtEnSvzQkwyOSF9sWTz-V26ePCi4CLGz2aF5BnVy83Z6Piuf1nJiTsNyZbEyMaf9hrauSQCu9E5PApk_0lQdyfHpge6T2qhm-WVMFIysTSfIxgczV9pxjSJYcIiUyGetOL0vwEEbnFdJl9aV5Exp0IsYE7J)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdkufWNhlC6E3kWOC9BZFlcHBTb7LceG6_bpIntTsUdythdcpRp6IYnKodxUdJYtXRnypMyUF9ugQXJ9YkM8Yiu9dHNS9-rA9bjIg7uT5a35M8YFLZ44ghqhqwnUrzsA==)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlqf4x7tJMCpkRrqr-oF8cb6yLNIDL6bAQ_C4VO0v-iaPyNOj79ezzUL_8ThWKj9oh9OIop7x8maEN8d4L_J3DFys03qORGDVBELigYzEnLwKsoJmhYoWMQf_I7LnKLs68KFEmWMv5fP05IHgrlM7LW3PAiTZWK0GDxdExeN4iU4ysX-DIisYQHjlnVY2PL7t7HRQBIdjaN14-KlqlqXQBkt1PwSb9eclqMw==)
11. [plos.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNtuROMOiLLrDsTx6fiPwty6DOqa9Flsgoi1F7V-zoNrTsE37yNyuiv71AbPP-HD7mZTCz_sOAbXIUv6Js43I6B8Y9ccpUco8bYCh19RMewZUCbXwCamGp4LBpdv3YJZxhe9mYbE79S6EWXiGY0kssG5fgZ91TLmkAzj_QpsGa)
12. [aafp.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxzASIzc2-5U6LtMWIdSIs8bNYsgY5NkAIeB1kVQKP1xm_sBgHXKYJAI9R6hUor4w790JPxT22JTG2ryR-53dlCi-SxnlmYTNECL1gvp0wg7ynCaaAb_nzAttfqUoW8JFQpIxlYnyx_9nBOMZHdA==)
13. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzry8kmUet-5k2hBsBgMaTkHtple5u5-9a58W2svs45FIuA_3YCXNyYVVCbwH5OiUiVmN4X4CkXHPcNOpW2Te3xe4XTyy_PzMj1nqJNIu0Te2iU7DXWy3QfQ_7zFCN0A==)
14. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFODi2hV4G6OjCoAVD8DIJuCpTS4VaEfqqos8yfJ0Dg7iY3b1eZzRe6pAwPjHK3P35nUXHIWJihZYMpXsSOXUQfGHAutEMmKvOwDoL7gL6xmlP5O-0SHaNGFvG6jgyhN4qxD6YmbloTIUyGxgP5p5LnW_lmgaKGD09gdn3J5wXnmnz0u0sAw3bHk99plSRF3j29YG6V5KXA7sywGF6hhnO-Tj2Y9S0oxdRG9dgIHqO33MuOMRICJpxKw_Y30G3lNT6PO6rYBg5Hp7D6xySbKoo1OEs=)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFffLELJCyGKlCy3iJk5UqFZtYCa3zmnABsNiG85fF9KjsjpWZ3sJXMBVv10ifRV0tIM-Jz2bruMJME21xdG0MsdNUp1o5pW7Efj7xo8P7YdgUt1qwq5v1OHNuLTtYSP4B3AIwuI56Q-RNLL1oT3Ws9mKdJBdIHCK8NgxQ-gkS7OLvF7l0CxqYeDo08HewwWcEV5jD9sMzG9D6vdYraNpPhMJKaWf-v22ENhcy-zCaEth3s3X0EoOF3AuUVMnbde-xyJHq7y1tBWamDwkCeDNgWy31nVXI-7bul1e0mlD5b8AZxf7Yp3TvMAs2gn6JjkLUi)
16. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPpmWWSlJ3QScjyEIIj_Z4rvdtw3b-gekMfHkwB7AcZi80Hv_EJe5zprxJJPa8_SEF2kT8c1BYS0ZQ2w5WrxZQXu5tc-nUs__iT8h9a3YSV7OF_tQBTyaTWzCOvut-_Q==)
17. [drugs.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGeoo7EhsKd7IITP4Bbg7lu-DF2M2jUVHDTmApHJbtTsQclCO5Pwdjxdbd7LLXoyZ-CDJFSzwsaQQMZSmfgIJs0ysgs_Uly-4VA9HHc0qKJdDbrREPmzdVfMkx61c91VxEd50TSPb_gy0Nq9e4gbP8DaEopbwrCspRjFP89QmIRMRjreU9qQMf8tsVtXSXSYb_yjlJ5jF3monQ4k1A=)
18. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkCuTwHgGIH0pmOynj1MXbovLqrRsEeoPHOSwv8N8pmvH1bigWrsMX5QjQSTKfQKMPVErxsR1kg5KpmD3xmoW71GrPRr4XIk9IVvav6xTWrdC_ddGPf2c8JR6IQPSLtRJ5M-0gDLc6)
19. [litfl.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_Rk9M1umbNh8Qanv88XW6ChKDecP-mlBMpbJa5jrjY4DeRXdR7eXaHE4AiXWSW_6bWktNiQ3jtejequkQ8x90dMZodxEBqOdhUWUVLgvMbWYqejvmZbPAZK6RHwakYA==)
20. [taylorandfrancis.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFworSeTF62U-Xvucjfy8HbBezCh7UkoCD1J10UYGgaCEcOku0Ks6GtGmsCDY0ljP4IENL7uglpG9UpUFfjnhXhmdbC_JZxNspsEUlF2ukkJYz7Iy2Uadogf4E00hS6a-_1rPy2SYxL3k_gz6IzPvGD72wV3AqCLsyftXqVDSdPWTLAGlE_NybBGyHiIfARygqJ7uvZ9vXVU9Qwm8g01g==)
21. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEKmfmVwkFpU3HkcQDcmb9BAVsrgBT1BmuBk0q-eSBd8g5aogcDhsIxv2PU22bqidNkl7-fpHsbs8nDrs_MfRQ823qVTDylEfUR60KAVqq-ubTD8x24NbMQUuC-KDSUA==)
22. [admescope.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAIBbTMhtzlz_Sr0I8tZx-kmNltCUO7kK9azw_QKjOTaCSqA_GzmW0DEm6u-LEIuhVsOx_Dk-sBZ-aDvUzCAFpEwc6POdLzEcGBB3uP07xz2AIB6QYTMi9eWvJL7BPDNjRuJ4ya7d7PBFcSVdE3CW59w3_MZ8gOye5sh6j2cooiR9ZjZRJR-2RTwmUy7-gnK02Jw==)
23. [regulations.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0UUdRJHze51MQmmwmz2vM4ryZeWg-rDL24krE3rWahQBwpKJwMZUMh55sDot2EHoYXmXAo9pP_K81s2sN5hq2zkmi-DLBnqvkslOczdP7XBB1pwPrivvYHxLU8FUzOfEcJXgVXz-SsDW1A1qZvJrynTB-7YX2ZuX9jtB2nw==)
24. [uspto.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGapIul2yAZVvfPXCUO1EucHeu_WRpKqbsQqsXM524aM66KSFWQKgf9FHg2fEuz4fhUnMN_YMFJtmsUYaiUU40j1SkH21f_o3lVpeg89Uzu5vFCNpr22XpalJnbpNNZgxXRjq11xfxi8poTRNS0KNJno8izZiRHP3EUTdxjROyespZ_PxVRcTIdIgZsuH0C8mlN0IW_HpYrbLVZzuHgBOlMsm2zx205NehS61JMfeujRULPdDO1ctTMhMurNlzWm4r6aXkDYYrtAOHjLTS1W-JL298=)
25. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoIr0X-JT4phTlsxt-SmiwLb3AjzdxjnVTpd86fLkCn_oz3e0LSRZ0Ana-yxZbopiTpNPzvg6o55QTIiHT4JzbrGJlgZLJbq7wub7erdUo2QlJnaW9l2RQhqjt7_w=)
26. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzu55uJs_ZudRlzOtSHiKfxp8kDJj6G0A0v0a9mPZO3JODHEFYMxywopH6Iulbfa2BIWDJw9mTz2BNEifedYo1O7NdyS55Z8d6WvXrfQbO_y90ZXLcOuBXBBIdcfqj5NLAyRSxj-8k)
27. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmZEESmuyCWw9cOWV3-6KK-EVjLSa-kbpDc_VmqxY-4DT7_nUYwNkBfqvZ4fEUN4LM6Bf8hXCxqAADnmgcXDfRlkCyJq9-1zzg_C1bCKiLKt6YHk23qU_YDMjk32H5QA==)
28. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ6XZ-GnpMRkjGdQ3w5xnsn6KWjwlvm0PeG1vp1SOwu-NlsWKgt0VU9odX7CAIgaNz2Tc7GyTZH0_lsP-rZkWm0fuB6IZwY3wkjVnofPZEd2GUttpPD0FdFyO0axhd9MikBlPvo2Ov)


## Annotations
Annotation(end_index=2139, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4HQZbICNlj1vKICyAmmAhqZmYRpgDuIHcZ8Ud3j2K0nYhnj8z45z60qyUGbgK9N5vm7OqiUkXWKNaiiWeP7wHHP9TMLBDMeB5CB257QOJ4vrvh1JJW5A6CjwXRhhekEkmwYNsGSsd9ppJk5laR5IGW7QSogxUwYP3OikUZXWIt_At5q2cORUDsdd9vGpg2YdyGcU=', start_index=2127)
Annotation(end_index=2139, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoFDPfupsGmiw9R9q8rQ0OlzAiey1GHYluzS0eev0RiuK26eaubMKGAt5veH0bR_R6o1LZI7sg06vTFJUlBs4QIT9DUzpYqzxxgtJkjnu-fADcluzrDghe2GssnHCBbSIg', start_index=2127)
Annotation(end_index=2824, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy2pBLt3-JFTEePeyyAGA7RG8boVN7fDYwlTErpvHU7f-NMOVBQcJwvowCpUL5Jx_dJXE1ECPLQtF84l23xN6KM7CtsdR_Ybpl3gCcWxR8SCzna5VITSXLxXXVkCQkhEsJUgQAETgq_OKseiSqKQ==', start_index=2812)
Annotation(end_index=2824, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmMU5z2kLp738rjJfhBObNFhRWtMY4TITI0Lm22cDtGoAD64ixuyDE_KLKNVYs2x3WDlN8mMhFC5yprV1Lh-AOTlrP4z0wtZNCyf40_bRZMtl2JFLioK-LK0s9z2ecMQwsnI8B9Oj43A==', start_index=2812)
Annotation(end_index=3008, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEr6nW0hArlux6iTFDNgsuatbyvaFJda5kgdcsvCTb5SboTraXQyCg0jQW5A36DJY-E7YYMN5ull7wFVkRIsjvEpzO_LgWNky0zXmrEDDpSimfvcx7y0vIejr6QSxLZvJzDSE_gmhNVyi83ZcTZTmcsnlLHiFpwm91W1SdnpoT3uJnFfS4uHFQroHMK1ldVDg0prLSjWynM2ZY=', start_index=2999)
Annotation(end_index=3876, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4HQZbICNlj1vKICyAmmAhqZmYRpgDuIHcZ8Ud3j2K0nYhnj8z45z60qyUGbgK9N5vm7OqiUkXWKNaiiWeP7wHHP9TMLBDMeB5CB257QOJ4vrvh1JJW5A6CjwXRhhekEkmwYNsGSsd9ppJk5laR5IGW7QSogxUwYP3OikUZXWIt_At5q2cORUDsdd9vGpg2YdyGcU=', start_index=3864)
Annotation(end_index=3876, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdcQoP3rPS4Ke10xPkZq8ZCermzehOGqKthedlLWcj78pYqEr7wj4dC03YDfosKS3LQ0Ol_j5aTCcEWh1H015J70we1vsorqIO8YrBrJeKwZ03HTgXYzem4gA738Z7_Y9KaUi1CZM2IOF5nPTMzaMQyUib3qBaZyfo0UuBQLFviedt7e0JYcfJvFEFc3H7', start_index=3864)
Annotation(end_index=3973, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4HQZbICNlj1vKICyAmmAhqZmYRpgDuIHcZ8Ud3j2K0nYhnj8z45z60qyUGbgK9N5vm7OqiUkXWKNaiiWeP7wHHP9TMLBDMeB5CB257QOJ4vrvh1JJW5A6CjwXRhhekEkmwYNsGSsd9ppJk5laR5IGW7QSogxUwYP3OikUZXWIt_At5q2cORUDsdd9vGpg2YdyGcU=', start_index=3961)
Annotation(end_index=3973, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdcQoP3rPS4Ke10xPkZq8ZCermzehOGqKthedlLWcj78pYqEr7wj4dC03YDfosKS3LQ0Ol_j5aTCcEWh1H015J70we1vsorqIO8YrBrJeKwZ03HTgXYzem4gA738Z7_Y9KaUi1CZM2IOF5nPTMzaMQyUib3qBaZyfo0UuBQLFviedt7e0JYcfJvFEFc3H7', start_index=3961)
Annotation(end_index=4063, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4HQZbICNlj1vKICyAmmAhqZmYRpgDuIHcZ8Ud3j2K0nYhnj8z45z60qyUGbgK9N5vm7OqiUkXWKNaiiWeP7wHHP9TMLBDMeB5CB257QOJ4vrvh1JJW5A6CjwXRhhekEkmwYNsGSsd9ppJk5laR5IGW7QSogxUwYP3OikUZXWIt_At5q2cORUDsdd9vGpg2YdyGcU=', start_index=4051)
Annotation(end_index=4063, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdcQoP3rPS4Ke10xPkZq8ZCermzehOGqKthedlLWcj78pYqEr7wj4dC03YDfosKS3LQ0Ol_j5aTCcEWh1H015J70we1vsorqIO8YrBrJeKwZ03HTgXYzem4gA738Z7_Y9KaUi1CZM2IOF5nPTMzaMQyUib3qBaZyfo0UuBQLFviedt7e0JYcfJvFEFc3H7', start_index=4051)
Annotation(end_index=4359, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElUAGDBcQLqTQpWLKz3q15N4AR1ux37CBHKG4Dq3fN3592587LtR8PMsYEvZAon3UXqsn-UX01gAcqCyaKFF9ethgO7XxCUFTpsxm4DcrGMPDN8Kk6xQrqziscIOf_oTe5jsNoGhiT', start_index=4347)
Annotation(end_index=4359, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFR_ug2vfUnB5l7y2QhOAuMlalXJUWfLGSXhZ3qSmUlJj0dFID2hJHo3r_WZV0-yrP0PoXy19_dBB-g0KLY9FTSE2ABR0L_xk29hYRW-KPuiqNfUHweAATiT7P7mBtEnSvzQkwyOSF9sWTz-V26ePCi4CLGz2aF5BnVy83Z6Piuf1nJiTsNyZbEyMaf9hrauSQCu9E5PApk_0lQdyfHpge6T2qhm-WVMFIysTSfIxgczV9pxjSJYcIiUyGetOL0vwEEbnFdJl9aV5Exp0IsYE7J', start_index=4347)
Annotation(end_index=4998, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy2pBLt3-JFTEePeyyAGA7RG8boVN7fDYwlTErpvHU7f-NMOVBQcJwvowCpUL5Jx_dJXE1ECPLQtF84l23xN6KM7CtsdR_Ybpl3gCcWxR8SCzna5VITSXLxXXVkCQkhEsJUgQAETgq_OKseiSqKQ==', start_index=4989)
Annotation(end_index=5272, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy2pBLt3-JFTEePeyyAGA7RG8boVN7fDYwlTErpvHU7f-NMOVBQcJwvowCpUL5Jx_dJXE1ECPLQtF84l23xN6KM7CtsdR_Ybpl3gCcWxR8SCzna5VITSXLxXXVkCQkhEsJUgQAETgq_OKseiSqKQ==', start_index=5260)
Annotation(end_index=5272, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdkufWNhlC6E3kWOC9BZFlcHBTb7LceG6_bpIntTsUdythdcpRp6IYnKodxUdJYtXRnypMyUF9ugQXJ9YkM8Yiu9dHNS9-rA9bjIg7uT5a35M8YFLZ44ghqhqwnUrzsA==', start_index=5260)
Annotation(end_index=5920, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy2pBLt3-JFTEePeyyAGA7RG8boVN7fDYwlTErpvHU7f-NMOVBQcJwvowCpUL5Jx_dJXE1ECPLQtF84l23xN6KM7CtsdR_Ybpl3gCcWxR8SCzna5VITSXLxXXVkCQkhEsJUgQAETgq_OKseiSqKQ==', start_index=5907)
Annotation(end_index=5920, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlqf4x7tJMCpkRrqr-oF8cb6yLNIDL6bAQ_C4VO0v-iaPyNOj79ezzUL_8ThWKj9oh9OIop7x8maEN8d4L_J3DFys03qORGDVBELigYzEnLwKsoJmhYoWMQf_I7LnKLs68KFEmWMv5fP05IHgrlM7LW3PAiTZWK0GDxdExeN4iU4ysX-DIisYQHjlnVY2PL7t7HRQBIdjaN14-KlqlqXQBkt1PwSb9eclqMw==', start_index=5907)
Annotation(end_index=6199, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy2pBLt3-JFTEePeyyAGA7RG8boVN7fDYwlTErpvHU7f-NMOVBQcJwvowCpUL5Jx_dJXE1ECPLQtF84l23xN6KM7CtsdR_Ybpl3gCcWxR8SCzna5VITSXLxXXVkCQkhEsJUgQAETgq_OKseiSqKQ==', start_index=6187)
Annotation(end_index=6199, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdkufWNhlC6E3kWOC9BZFlcHBTb7LceG6_bpIntTsUdythdcpRp6IYnKodxUdJYtXRnypMyUF9ugQXJ9YkM8Yiu9dHNS9-rA9bjIg7uT5a35M8YFLZ44ghqhqwnUrzsA==', start_index=6187)
Annotation(end_index=6450, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdkufWNhlC6E3kWOC9BZFlcHBTb7LceG6_bpIntTsUdythdcpRp6IYnKodxUdJYtXRnypMyUF9ugQXJ9YkM8Yiu9dHNS9-rA9bjIg7uT5a35M8YFLZ44ghqhqwnUrzsA==', start_index=6437)
Annotation(end_index=6450, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNtuROMOiLLrDsTx6fiPwty6DOqa9Flsgoi1F7V-zoNrTsE37yNyuiv71AbPP-HD7mZTCz_sOAbXIUv6Js43I6B8Y9ccpUco8bYCh19RMewZUCbXwCamGp4LBpdv3YJZxhe9mYbE79S6EWXiGY0kssG5fgZ91TLmkAzj_QpsGa', start_index=6437)
Annotation(end_index=6832, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlqf4x7tJMCpkRrqr-oF8cb6yLNIDL6bAQ_C4VO0v-iaPyNOj79ezzUL_8ThWKj9oh9OIop7x8maEN8d4L_J3DFys03qORGDVBELigYzEnLwKsoJmhYoWMQf_I7LnKLs68KFEmWMv5fP05IHgrlM7LW3PAiTZWK0GDxdExeN4iU4ysX-DIisYQHjlnVY2PL7t7HRQBIdjaN14-KlqlqXQBkt1PwSb9eclqMw==', start_index=6822)
Annotation(end_index=7364, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy2pBLt3-JFTEePeyyAGA7RG8boVN7fDYwlTErpvHU7f-NMOVBQcJwvowCpUL5Jx_dJXE1ECPLQtF84l23xN6KM7CtsdR_Ybpl3gCcWxR8SCzna5VITSXLxXXVkCQkhEsJUgQAETgq_OKseiSqKQ==', start_index=7355)
Annotation(end_index=7807, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy2pBLt3-JFTEePeyyAGA7RG8boVN7fDYwlTErpvHU7f-NMOVBQcJwvowCpUL5Jx_dJXE1ECPLQtF84l23xN6KM7CtsdR_Ybpl3gCcWxR8SCzna5VITSXLxXXVkCQkhEsJUgQAETgq_OKseiSqKQ==', start_index=7794)
Annotation(end_index=7807, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxzASIzc2-5U6LtMWIdSIs8bNYsgY5NkAIeB1kVQKP1xm_sBgHXKYJAI9R6hUor4w790JPxT22JTG2ryR-53dlCi-SxnlmYTNECL1gvp0wg7ynCaaAb_nzAttfqUoW8JFQpIxlYnyx_9nBOMZHdA==', start_index=7794)
Annotation(end_index=8186, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzry8kmUet-5k2hBsBgMaTkHtple5u5-9a58W2svs45FIuA_3YCXNyYVVCbwH5OiUiVmN4X4CkXHPcNOpW2Te3xe4XTyy_PzMj1nqJNIu0Te2iU7DXWy3QfQ_7zFCN0A==', start_index=8173)
Annotation(end_index=8186, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmMU5z2kLp738rjJfhBObNFhRWtMY4TITI0Lm22cDtGoAD64ixuyDE_KLKNVYs2x3WDlN8mMhFC5yprV1Lh-AOTlrP4z0wtZNCyf40_bRZMtl2JFLioK-LK0s9z2ecMQwsnI8B9Oj43A==', start_index=8173)
Annotation(end_index=8436, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFODi2hV4G6OjCoAVD8DIJuCpTS4VaEfqqos8yfJ0Dg7iY3b1eZzRe6pAwPjHK3P35nUXHIWJihZYMpXsSOXUQfGHAutEMmKvOwDoL7gL6xmlP5O-0SHaNGFvG6jgyhN4qxD6YmbloTIUyGxgP5p5LnW_lmgaKGD09gdn3J5wXnmnz0u0sAw3bHk99plSRF3j29YG6V5KXA7sywGF6hhnO-Tj2Y9S0oxdRG9dgIHqO33MuOMRICJpxKw_Y30G3lNT6PO6rYBg5Hp7D6xySbKoo1OEs=', start_index=8423)
Annotation(end_index=8436, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmMU5z2kLp738rjJfhBObNFhRWtMY4TITI0Lm22cDtGoAD64ixuyDE_KLKNVYs2x3WDlN8mMhFC5yprV1Lh-AOTlrP4z0wtZNCyf40_bRZMtl2JFLioK-LK0s9z2ecMQwsnI8B9Oj43A==', start_index=8423)
Annotation(end_index=8652, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFffLELJCyGKlCy3iJk5UqFZtYCa3zmnABsNiG85fF9KjsjpWZ3sJXMBVv10ifRV0tIM-Jz2bruMJME21xdG0MsdNUp1o5pW7Efj7xo8P7YdgUt1qwq5v1OHNuLTtYSP4B3AIwuI56Q-RNLL1oT3Ws9mKdJBdIHCK8NgxQ-gkS7OLvF7l0CxqYeDo08HewwWcEV5jD9sMzG9D6vdYraNpPhMJKaWf-v22ENhcy-zCaEth3s3X0EoOF3AuUVMnbde-xyJHq7y1tBWamDwkCeDNgWy31nVXI-7bul1e0mlD5b8AZxf7Yp3TvMAs2gn6JjkLUi', start_index=8642)
Annotation(end_index=8764, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmMU5z2kLp738rjJfhBObNFhRWtMY4TITI0Lm22cDtGoAD64ixuyDE_KLKNVYs2x3WDlN8mMhFC5yprV1Lh-AOTlrP4z0wtZNCyf40_bRZMtl2JFLioK-LK0s9z2ecMQwsnI8B9Oj43A==', start_index=8755)
Annotation(end_index=9513, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPpmWWSlJ3QScjyEIIj_Z4rvdtw3b-gekMfHkwB7AcZi80Hv_EJe5zprxJJPa8_SEF2kT8c1BYS0ZQ2w5WrxZQXu5tc-nUs__iT8h9a3YSV7OF_tQBTyaTWzCOvut-_Q==', start_index=9499)
Annotation(end_index=9513, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGeoo7EhsKd7IITP4Bbg7lu-DF2M2jUVHDTmApHJbtTsQclCO5Pwdjxdbd7LLXoyZ-CDJFSzwsaQQMZSmfgIJs0ysgs_Uly-4VA9HHc0qKJdDbrREPmzdVfMkx61c91VxEd50TSPb_gy0Nq9e4gbP8DaEopbwrCspRjFP89QmIRMRjreU9qQMf8tsVtXSXSYb_yjlJ5jF3monQ4k1A=', start_index=9499)
Annotation(end_index=9613, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkCuTwHgGIH0pmOynj1MXbovLqrRsEeoPHOSwv8N8pmvH1bigWrsMX5QjQSTKfQKMPVErxsR1kg5KpmD3xmoW71GrPRr4XIk9IVvav6xTWrdC_ddGPf2c8JR6IQPSLtRJ5M-0gDLc6', start_index=9603)
Annotation(end_index=9872, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_Rk9M1umbNh8Qanv88XW6ChKDecP-mlBMpbJa5jrjY4DeRXdR7eXaHE4AiXWSW_6bWktNiQ3jtejequkQ8x90dMZodxEBqOdhUWUVLgvMbWYqejvmZbPAZK6RHwakYA==', start_index=9862)
Annotation(end_index=10447, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxzASIzc2-5U6LtMWIdSIs8bNYsgY5NkAIeB1kVQKP1xm_sBgHXKYJAI9R6hUor4w790JPxT22JTG2ryR-53dlCi-SxnlmYTNECL1gvp0wg7ynCaaAb_nzAttfqUoW8JFQpIxlYnyx_9nBOMZHdA==', start_index=10437)
Annotation(end_index=10654, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElUAGDBcQLqTQpWLKz3q15N4AR1ux37CBHKG4Dq3fN3592587LtR8PMsYEvZAon3UXqsn-UX01gAcqCyaKFF9ethgO7XxCUFTpsxm4DcrGMPDN8Kk6xQrqziscIOf_oTe5jsNoGhiT', start_index=10645)
Annotation(end_index=11015, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFworSeTF62U-Xvucjfy8HbBezCh7UkoCD1J10UYGgaCEcOku0Ks6GtGmsCDY0ljP4IENL7uglpG9UpUFfjnhXhmdbC_JZxNspsEUlF2ukkJYz7Iy2Uadogf4E00hS6a-_1rPy2SYxL3k_gz6IzPvGD72wV3AqCLsyftXqVDSdPWTLAGlE_NybBGyHiIfARygqJ7uvZ9vXVU9Qwm8g01g==', start_index=11005)
Annotation(end_index=11784, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy2pBLt3-JFTEePeyyAGA7RG8boVN7fDYwlTErpvHU7f-NMOVBQcJwvowCpUL5Jx_dJXE1ECPLQtF84l23xN6KM7CtsdR_Ybpl3gCcWxR8SCzna5VITSXLxXXVkCQkhEsJUgQAETgq_OKseiSqKQ==', start_index=11775)
Annotation(end_index=12087, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy2pBLt3-JFTEePeyyAGA7RG8boVN7fDYwlTErpvHU7f-NMOVBQcJwvowCpUL5Jx_dJXE1ECPLQtF84l23xN6KM7CtsdR_Ybpl3gCcWxR8SCzna5VITSXLxXXVkCQkhEsJUgQAETgq_OKseiSqKQ==', start_index=12078)
Annotation(end_index=12344, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEr6nW0hArlux6iTFDNgsuatbyvaFJda5kgdcsvCTb5SboTraXQyCg0jQW5A36DJY-E7YYMN5ull7wFVkRIsjvEpzO_LgWNky0zXmrEDDpSimfvcx7y0vIejr6QSxLZvJzDSE_gmhNVyi83ZcTZTmcsnlLHiFpwm91W1SdnpoT3uJnFfS4uHFQroHMK1ldVDg0prLSjWynM2ZY=', start_index=12335)
Annotation(end_index=12548, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzry8kmUet-5k2hBsBgMaTkHtple5u5-9a58W2svs45FIuA_3YCXNyYVVCbwH5OiUiVmN4X4CkXHPcNOpW2Te3xe4XTyy_PzMj1nqJNIu0Te2iU7DXWy3QfQ_7zFCN0A==', start_index=12535)
Annotation(end_index=12548, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmMU5z2kLp738rjJfhBObNFhRWtMY4TITI0Lm22cDtGoAD64ixuyDE_KLKNVYs2x3WDlN8mMhFC5yprV1Lh-AOTlrP4z0wtZNCyf40_bRZMtl2JFLioK-LK0s9z2ecMQwsnI8B9Oj43A==', start_index=12535)
Annotation(end_index=13059, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEKmfmVwkFpU3HkcQDcmb9BAVsrgBT1BmuBk0q-eSBd8g5aogcDhsIxv2PU22bqidNkl7-fpHsbs8nDrs_MfRQ823qVTDylEfUR60KAVqq-ubTD8x24NbMQUuC-KDSUA==', start_index=13049)
Annotation(end_index=13275, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAIBbTMhtzlz_Sr0I8tZx-kmNltCUO7kK9azw_QKjOTaCSqA_GzmW0DEm6u-LEIuhVsOx_Dk-sBZ-aDvUzCAFpEwc6POdLzEcGBB3uP07xz2AIB6QYTMi9eWvJL7BPDNjRuJ4ya7d7PBFcSVdE3CW59w3_MZ8gOye5sh6j2cooiR9ZjZRJR-2RTwmUy7-gnK02Jw==', start_index=13265)
Annotation(end_index=13477, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEKmfmVwkFpU3HkcQDcmb9BAVsrgBT1BmuBk0q-eSBd8g5aogcDhsIxv2PU22bqidNkl7-fpHsbs8nDrs_MfRQ823qVTDylEfUR60KAVqq-ubTD8x24NbMQUuC-KDSUA==', start_index=13467)
Annotation(end_index=13894, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGapIul2yAZVvfPXCUO1EucHeu_WRpKqbsQqsXM524aM66KSFWQKgf9FHg2fEuz4fhUnMN_YMFJtmsUYaiUU40j1SkH21f_o3lVpeg89Uzu5vFCNpr22XpalJnbpNNZgxXRjq11xfxi8poTRNS0KNJno8izZiRHP3EUTdxjROyespZ_PxVRcTIdIgZsuH0C8mlN0IW_HpYrbLVZzuHgBOlMsm2zx205NehS61JMfeujRULPdDO1ctTMhMurNlzWm4r6aXkDYYrtAOHjLTS1W-JL298=', start_index=13880)
Annotation(end_index=13894, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0UUdRJHze51MQmmwmz2vM4ryZeWg-rDL24krE3rWahQBwpKJwMZUMh55sDot2EHoYXmXAo9pP_K81s2sN5hq2zkmi-DLBnqvkslOczdP7XBB1pwPrivvYHxLU8FUzOfEcJXgVXz-SsDW1A1qZvJrynTB-7YX2ZuX9jtB2nw==', start_index=13880)
Annotation(end_index=14325, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy2pBLt3-JFTEePeyyAGA7RG8boVN7fDYwlTErpvHU7f-NMOVBQcJwvowCpUL5Jx_dJXE1ECPLQtF84l23xN6KM7CtsdR_Ybpl3gCcWxR8SCzna5VITSXLxXXVkCQkhEsJUgQAETgq_OKseiSqKQ==', start_index=14316)
Annotation(end_index=14897, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdkufWNhlC6E3kWOC9BZFlcHBTb7LceG6_bpIntTsUdythdcpRp6IYnKodxUdJYtXRnypMyUF9ugQXJ9YkM8Yiu9dHNS9-rA9bjIg7uT5a35M8YFLZ44ghqhqwnUrzsA==', start_index=14884)
Annotation(end_index=14897, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoIr0X-JT4phTlsxt-SmiwLb3AjzdxjnVTpd86fLkCn_oz3e0LSRZ0Ana-yxZbopiTpNPzvg6o55QTIiHT4JzbrGJlgZLJbq7wub7erdUo2QlJnaW9l2RQhqjt7_w=', start_index=14884)
Annotation(end_index=15269, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkCuTwHgGIH0pmOynj1MXbovLqrRsEeoPHOSwv8N8pmvH1bigWrsMX5QjQSTKfQKMPVErxsR1kg5KpmD3xmoW71GrPRr4XIk9IVvav6xTWrdC_ddGPf2c8JR6IQPSLtRJ5M-0gDLc6', start_index=15255)
Annotation(end_index=15269, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNtuROMOiLLrDsTx6fiPwty6DOqa9Flsgoi1F7V-zoNrTsE37yNyuiv71AbPP-HD7mZTCz_sOAbXIUv6Js43I6B8Y9ccpUco8bYCh19RMewZUCbXwCamGp4LBpdv3YJZxhe9mYbE79S6EWXiGY0kssG5fgZ91TLmkAzj_QpsGa', start_index=15255)
Annotation(end_index=15531, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdkufWNhlC6E3kWOC9BZFlcHBTb7LceG6_bpIntTsUdythdcpRp6IYnKodxUdJYtXRnypMyUF9ugQXJ9YkM8Yiu9dHNS9-rA9bjIg7uT5a35M8YFLZ44ghqhqwnUrzsA==', start_index=15522)
Annotation(end_index=15800, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmZEESmuyCWw9cOWV3-6KK-EVjLSa-kbpDc_VmqxY-4DT7_nUYwNkBfqvZ4fEUN4LM6Bf8hXCxqAADnmgcXDfRlkCyJq9-1zzg_C1bCKiLKt6YHk23qU_YDMjk32H5QA==', start_index=15786)
Annotation(end_index=15800, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzu55uJs_ZudRlzOtSHiKfxp8kDJj6G0A0v0a9mPZO3JODHEFYMxywopH6Iulbfa2BIWDJw9mTz2BNEifedYo1O7NdyS55Z8d6WvXrfQbO_y90ZXLcOuBXBBIdcfqj5NLAyRSxj-8k', start_index=15786)
Annotation(end_index=16977, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoFDPfupsGmiw9R9q8rQ0OlzAiey1GHYluzS0eev0RiuK26eaubMKGAt5veH0bR_R6o1LZI7sg06vTFJUlBs4QIT9DUzpYqzxxgtJkjnu-fADcluzrDghe2GssnHCBbSIg', start_index=16968)
Annotation(end_index=17059, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy2pBLt3-JFTEePeyyAGA7RG8boVN7fDYwlTErpvHU7f-NMOVBQcJwvowCpUL5Jx_dJXE1ECPLQtF84l23xN6KM7CtsdR_Ybpl3gCcWxR8SCzna5VITSXLxXXVkCQkhEsJUgQAETgq_OKseiSqKQ==', start_index=17050)
Annotation(end_index=17154, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzry8kmUet-5k2hBsBgMaTkHtple5u5-9a58W2svs45FIuA_3YCXNyYVVCbwH5OiUiVmN4X4CkXHPcNOpW2Te3xe4XTyy_PzMj1nqJNIu0Te2iU7DXWy3QfQ_7zFCN0A==', start_index=17144)
Annotation(end_index=17250, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElUAGDBcQLqTQpWLKz3q15N4AR1ux37CBHKG4Dq3fN3592587LtR8PMsYEvZAon3UXqsn-UX01gAcqCyaKFF9ethgO7XxCUFTpsxm4DcrGMPDN8Kk6xQrqziscIOf_oTe5jsNoGhiT', start_index=17241)
Annotation(end_index=17305, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4HQZbICNlj1vKICyAmmAhqZmYRpgDuIHcZ8Ud3j2K0nYhnj8z45z60qyUGbgK9N5vm7OqiUkXWKNaiiWeP7wHHP9TMLBDMeB5CB257QOJ4vrvh1JJW5A6CjwXRhhekEkmwYNsGSsd9ppJk5laR5IGW7QSogxUwYP3OikUZXWIt_At5q2cORUDsdd9vGpg2YdyGcU=', start_index=17296)
Annotation(end_index=17375, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAIBbTMhtzlz_Sr0I8tZx-kmNltCUO7kK9azw_QKjOTaCSqA_GzmW0DEm6u-LEIuhVsOx_Dk-sBZ-aDvUzCAFpEwc6POdLzEcGBB3uP07xz2AIB6QYTMi9eWvJL7BPDNjRuJ4ya7d7PBFcSVdE3CW59w3_MZ8gOye5sh6j2cooiR9ZjZRJR-2RTwmUy7-gnK02Jw==', start_index=17365)
Annotation(end_index=17453, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0UUdRJHze51MQmmwmz2vM4ryZeWg-rDL24krE3rWahQBwpKJwMZUMh55sDot2EHoYXmXAo9pP_K81s2sN5hq2zkmi-DLBnqvkslOczdP7XBB1pwPrivvYHxLU8FUzOfEcJXgVXz-SsDW1A1qZvJrynTB-7YX2ZuX9jtB2nw==', start_index=17443)
Annotation(end_index=17571, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEKmfmVwkFpU3HkcQDcmb9BAVsrgBT1BmuBk0q-eSBd8g5aogcDhsIxv2PU22bqidNkl7-fpHsbs8nDrs_MfRQ823qVTDylEfUR60KAVqq-ubTD8x24NbMQUuC-KDSUA==', start_index=17561)
Annotation(end_index=17682, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdcQoP3rPS4Ke10xPkZq8ZCermzehOGqKthedlLWcj78pYqEr7wj4dC03YDfosKS3LQ0Ol_j5aTCcEWh1H015J70we1vsorqIO8YrBrJeKwZ03HTgXYzem4gA738Z7_Y9KaUi1CZM2IOF5nPTMzaMQyUib3qBaZyfo0UuBQLFviedt7e0JYcfJvFEFc3H7', start_index=17673)
Annotation(end_index=17747, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxzASIzc2-5U6LtMWIdSIs8bNYsgY5NkAIeB1kVQKP1xm_sBgHXKYJAI9R6hUor4w790JPxT22JTG2ryR-53dlCi-SxnlmYTNECL1gvp0wg7ynCaaAb_nzAttfqUoW8JFQpIxlYnyx_9nBOMZHdA==', start_index=17737)
Annotation(end_index=17800, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElUAGDBcQLqTQpWLKz3q15N4AR1ux37CBHKG4Dq3fN3592587LtR8PMsYEvZAon3UXqsn-UX01gAcqCyaKFF9ethgO7XxCUFTpsxm4DcrGMPDN8Kk6xQrqziscIOf_oTe5jsNoGhiT', start_index=17791)
Annotation(end_index=17883, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFworSeTF62U-Xvucjfy8HbBezCh7UkoCD1J10UYGgaCEcOku0Ks6GtGmsCDY0ljP4IENL7uglpG9UpUFfjnhXhmdbC_JZxNspsEUlF2ukkJYz7Iy2Uadogf4E00hS6a-_1rPy2SYxL3k_gz6IzPvGD72wV3AqCLsyftXqVDSdPWTLAGlE_NybBGyHiIfARygqJ7uvZ9vXVU9Qwm8g01g==', start_index=17873)
Annotation(end_index=17937, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdkufWNhlC6E3kWOC9BZFlcHBTb7LceG6_bpIntTsUdythdcpRp6IYnKodxUdJYtXRnypMyUF9ugQXJ9YkM8Yiu9dHNS9-rA9bjIg7uT5a35M8YFLZ44ghqhqwnUrzsA==', start_index=17928)
Annotation(end_index=18041, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFR_ug2vfUnB5l7y2QhOAuMlalXJUWfLGSXhZ3qSmUlJj0dFID2hJHo3r_WZV0-yrP0PoXy19_dBB-g0KLY9FTSE2ABR0L_xk29hYRW-KPuiqNfUHweAATiT7P7mBtEnSvzQkwyOSF9sWTz-V26ePCi4CLGz2aF5BnVy83Z6Piuf1nJiTsNyZbEyMaf9hrauSQCu9E5PApk_0lQdyfHpge6T2qhm-WVMFIysTSfIxgczV9pxjSJYcIiUyGetOL0vwEEbnFdJl9aV5Exp0IsYE7J', start_index=18032)
Annotation(end_index=18148, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEr6nW0hArlux6iTFDNgsuatbyvaFJda5kgdcsvCTb5SboTraXQyCg0jQW5A36DJY-E7YYMN5ull7wFVkRIsjvEpzO_LgWNky0zXmrEDDpSimfvcx7y0vIejr6QSxLZvJzDSE_gmhNVyi83ZcTZTmcsnlLHiFpwm91W1SdnpoT3uJnFfS4uHFQroHMK1ldVDg0prLSjWynM2ZY=', start_index=18139)
Annotation(end_index=18205, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoIr0X-JT4phTlsxt-SmiwLb3AjzdxjnVTpd86fLkCn_oz3e0LSRZ0Ana-yxZbopiTpNPzvg6o55QTIiHT4JzbrGJlgZLJbq7wub7erdUo2QlJnaW9l2RQhqjt7_w=', start_index=18195)
Annotation(end_index=18268, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy2pBLt3-JFTEePeyyAGA7RG8boVN7fDYwlTErpvHU7f-NMOVBQcJwvowCpUL5Jx_dJXE1ECPLQtF84l23xN6KM7CtsdR_Ybpl3gCcWxR8SCzna5VITSXLxXXVkCQkhEsJUgQAETgq_OKseiSqKQ==', start_index=18259)
Annotation(end_index=18333, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_Rk9M1umbNh8Qanv88XW6ChKDecP-mlBMpbJa5jrjY4DeRXdR7eXaHE4AiXWSW_6bWktNiQ3jtejequkQ8x90dMZodxEBqOdhUWUVLgvMbWYqejvmZbPAZK6RHwakYA==', start_index=18323)
Annotation(end_index=18384, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPpmWWSlJ3QScjyEIIj_Z4rvdtw3b-gekMfHkwB7AcZi80Hv_EJe5zprxJJPa8_SEF2kT8c1BYS0ZQ2w5WrxZQXu5tc-nUs__iT8h9a3YSV7OF_tQBTyaTWzCOvut-_Q==', start_index=18374)
Annotation(end_index=18486, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGeoo7EhsKd7IITP4Bbg7lu-DF2M2jUVHDTmApHJbtTsQclCO5Pwdjxdbd7LLXoyZ-CDJFSzwsaQQMZSmfgIJs0ysgs_Uly-4VA9HHc0qKJdDbrREPmzdVfMkx61c91VxEd50TSPb_gy0Nq9e4gbP8DaEopbwrCspRjFP89QmIRMRjreU9qQMf8tsVtXSXSYb_yjlJ5jF3monQ4k1A=', start_index=18476)
Annotation(end_index=18558, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGapIul2yAZVvfPXCUO1EucHeu_WRpKqbsQqsXM524aM66KSFWQKgf9FHg2fEuz4fhUnMN_YMFJtmsUYaiUU40j1SkH21f_o3lVpeg89Uzu5vFCNpr22XpalJnbpNNZgxXRjq11xfxi8poTRNS0KNJno8izZiRHP3EUTdxjROyespZ_PxVRcTIdIgZsuH0C8mlN0IW_HpYrbLVZzuHgBOlMsm2zx205NehS61JMfeujRULPdDO1ctTMhMurNlzWm4r6aXkDYYrtAOHjLTS1W-JL298=', start_index=18548)
Annotation(end_index=18655, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzu55uJs_ZudRlzOtSHiKfxp8kDJj6G0A0v0a9mPZO3JODHEFYMxywopH6Iulbfa2BIWDJw9mTz2BNEifedYo1O7NdyS55Z8d6WvXrfQbO_y90ZXLcOuBXBBIdcfqj5NLAyRSxj-8k', start_index=18645)
Annotation(end_index=18704, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmMU5z2kLp738rjJfhBObNFhRWtMY4TITI0Lm22cDtGoAD64ixuyDE_KLKNVYs2x3WDlN8mMhFC5yprV1Lh-AOTlrP4z0wtZNCyf40_bRZMtl2JFLioK-LK0s9z2ecMQwsnI8B9Oj43A==', start_index=18695)
Annotation(end_index=18786, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFODi2hV4G6OjCoAVD8DIJuCpTS4VaEfqqos8yfJ0Dg7iY3b1eZzRe6pAwPjHK3P35nUXHIWJihZYMpXsSOXUQfGHAutEMmKvOwDoL7gL6xmlP5O-0SHaNGFvG6jgyhN4qxD6YmbloTIUyGxgP5p5LnW_lmgaKGD09gdn3J5wXnmnz0u0sAw3bHk99plSRF3j29YG6V5KXA7sywGF6hhnO-Tj2Y9S0oxdRG9dgIHqO33MuOMRICJpxKw_Y30G3lNT6PO6rYBg5Hp7D6xySbKoo1OEs=', start_index=18776)
Annotation(end_index=18851, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy2pBLt3-JFTEePeyyAGA7RG8boVN7fDYwlTErpvHU7f-NMOVBQcJwvowCpUL5Jx_dJXE1ECPLQtF84l23xN6KM7CtsdR_Ybpl3gCcWxR8SCzna5VITSXLxXXVkCQkhEsJUgQAETgq_OKseiSqKQ==', start_index=18842)
Annotation(end_index=18918, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFffLELJCyGKlCy3iJk5UqFZtYCa3zmnABsNiG85fF9KjsjpWZ3sJXMBVv10ifRV0tIM-Jz2bruMJME21xdG0MsdNUp1o5pW7Efj7xo8P7YdgUt1qwq5v1OHNuLTtYSP4B3AIwuI56Q-RNLL1oT3Ws9mKdJBdIHCK8NgxQ-gkS7OLvF7l0CxqYeDo08HewwWcEV5jD9sMzG9D6vdYraNpPhMJKaWf-v22ENhcy-zCaEth3s3X0EoOF3AuUVMnbde-xyJHq7y1tBWamDwkCeDNgWy31nVXI-7bul1e0mlD5b8AZxf7Yp3TvMAs2gn6JjkLUi', start_index=18908)
Annotation(end_index=19007, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkCuTwHgGIH0pmOynj1MXbovLqrRsEeoPHOSwv8N8pmvH1bigWrsMX5QjQSTKfQKMPVErxsR1kg5KpmD3xmoW71GrPRr4XIk9IVvav6xTWrdC_ddGPf2c8JR6IQPSLtRJ5M-0gDLc6', start_index=18997)
Annotation(end_index=19096, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmZEESmuyCWw9cOWV3-6KK-EVjLSa-kbpDc_VmqxY-4DT7_nUYwNkBfqvZ4fEUN4LM6Bf8hXCxqAADnmgcXDfRlkCyJq9-1zzg_C1bCKiLKt6YHk23qU_YDMjk32H5QA==', start_index=19086)
Annotation(end_index=19171, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ6XZ-GnpMRkjGdQ3w5xnsn6KWjwlvm0PeG1vp1SOwu-NlsWKgt0VU9odX7CAIgaNz2Tc7GyTZH0_lsP-rZkWm0fuB6IZwY3wkjVnofPZEd2GUttpPD0FdFyO0axhd9MikBlPvo2Ov', start_index=19161)
Annotation(end_index=19233, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNtuROMOiLLrDsTx6fiPwty6DOqa9Flsgoi1F7V-zoNrTsE37yNyuiv71AbPP-HD7mZTCz_sOAbXIUv6Js43I6B8Y9ccpUco8bYCh19RMewZUCbXwCamGp4LBpdv3YJZxhe9mYbE79S6EWXiGY0kssG5fgZ91TLmkAzj_QpsGa', start_index=19223)
Annotation(end_index=19300, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlqf4x7tJMCpkRrqr-oF8cb6yLNIDL6bAQ_C4VO0v-iaPyNOj79ezzUL_8ThWKj9oh9OIop7x8maEN8d4L_J3DFys03qORGDVBELigYzEnLwKsoJmhYoWMQf_I7LnKLs68KFEmWMv5fP05IHgrlM7LW3PAiTZWK0GDxdExeN4iU4ysX-DIisYQHjlnVY2PL7t7HRQBIdjaN14-KlqlqXQBkt1PwSb9eclqMw==', start_index=19290)

## Sources
