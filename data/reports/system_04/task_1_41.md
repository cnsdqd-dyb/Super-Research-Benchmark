# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 567d0963 | **Time:** 336.57s | **Cost:** $1.55808
--------------------------------------------------------------------------------

# Balancing Seizure Control and Metabolic Safety in Antiepileptic Drug Discovery: A Comprehensive Analysis

### Key Points
*   **Evolution of Drug Design:** The field has shifted from serendipitous discovery and broad screening to rational drug design and Multi-Parameter Optimization (MPO), aiming to decouple seizure suppression from hepatic enzyme induction or inhibition.
*   **Metabolic Liability as a Gatekeeper:** Modern screening cascades prioritize metabolic stability and the absence of reactive metabolites (e.g., avoiding structural alerts like those found in felbamate) as heavily as anticonvulsant efficacy in early-stage development.
*   **The Pharmacokinetic Trade-off:** Research focuses on identifying compounds with renal elimination (like levetiracetam) to bypass the complex cytochrome P450 interactions characteristic of older generation drugs (like phenytoin and carbamazepine).
*   **Therapeutic Index Optimization:** A primary goal is widening the therapeutic index (TI), moving away from narrow TI agents (e.g., phenytoin, TI ≈ 2) toward agents where effective doses do not overlap with toxic thresholds.
*   **Systemic Metabolic Impact:** Beyond drug-drug interactions, current research evaluates long-term metabolic risks, such as bone density reduction and lipid profile alteration, integrating these endpoints into preclinical toxicology.

### Introduction to the Equilibrium
The development of antiepileptic drugs (AEDs), also known as antiseizure medications (ASMs), represents a complex optimization problem within medicinal chemistry and pharmacology. The primary objective is the suppression of abnormal neuronal synchrony to prevent seizures. However, the historical trajectory of AED development reveals that efficacy often comes at the cost of significant metabolic burden. Older generation drugs, while effective, frequently act as potent inducers or inhibitors of hepatic enzymes, leading to a cascade of pharmacokinetic interactions and systemic metabolic dysregulation.

Modern research aims to balance these competing demands through rigorous screening cascades. Scientists must ensure that a compound is lipophilic enough to cross the blood-brain barrier (BBB) to reach neuronal targets, yet hydrophilic and stable enough to avoid rapid hepatic clearance or the formation of toxic reactive metabolites. This report details the mechanisms, screening strategies, and pharmacological principles used to navigate the trade-off between seizure control thresholds and metabolic interaction risks.

---

## 1. Historical Context and the Metabolic Burden of First-Generation AEDs

To understand how current research balances efficacy and metabolism, one must first analyze the metabolic liabilities of established therapies. The "first-generation" and some "second-generation" AEDs serve as case studies for high metabolic risk, establishing the baseline against which new compounds are measured.

### 1.1 Hepatic Enzyme Induction and Inhibition
The majority of clinically significant interactions involving AEDs arise from their influence on the cytochrome P450 (CYP) system and uridine diphosphate glucuronosyltransferase (UGT) enzymes [cite: 1, 2].

*   **Enzyme Inducers:** Phenytoin (PHT), carbamazepine (CBZ), phenobarbital (PB), and primidone are potent, broad-spectrum inducers. They upregulate CYP3A4, CYP2C9, CYP2C19, and UGTs [cite: 3, 4]. This induction accelerates the metabolism of co-administered drugs (e.g., oral contraceptives, anticoagulants, chemotherapeutics) and endogenous substances (e.g., Vitamin D, sex steroids), leading to therapeutic failure of comorbidities or systemic metabolic disorders [cite: 4, 5].
*   **Enzyme Inhibitors:** Valproic acid (VPA) represents the opposite spectrum. It acts as a broad inhibitor, notably of CYP2C9 and UGT enzymes [cite: 3]. For instance, VPA inhibits the glucuronidation of lamotrigine, doubling its half-life and increasing the risk of life-threatening rash (Stevens-Johnson syndrome) if dosing is not adjusted [cite: 2, 3].
*   **Autoinduction:** Carbamazepine induces its own metabolism (autoinduction), complicating dose titration as serum concentrations may fall despite consistent dosing [cite: 4, 6].

### 1.2 The Therapeutic Index (TI) Challenge
The therapeutic index serves as a quantitative measure of the balance between efficacy and toxicity. Research indicates that older AEDs possess a dangerously narrow TI.
*   **Phenytoin:** Literature reviews suggest the TI of phenytoin is approximately 2, meaning the concentration required for toxicity (typically >20 µg/mL) is only twice that of the minimum effective concentration (10 µg/mL) [cite: 7, 8]. This leaves little margin for error regarding metabolic fluctuations caused by drug interactions or genetic polymorphisms.
*   **Variability:** Because these drugs are heavily metabolized by the liver, their serum levels are highly susceptible to inter-patient variability in CYP expression, necessitating rigorous Therapeutic Drug Monitoring (TDM) [cite: 9, 10].

### 1.3 Reactive Metabolites and Idiosyncratic Toxicity
A critical failure mode in AED development is the formation of reactive metabolites (RMs). These electrophilic species can covalently bind to cellular proteins or DNA, triggering immune-mediated idiosyncratic drug reactions (IDRs) such as hepatotoxicity or aplastic anemia [cite: 11, 12].
*   **Felbamate:** Although highly effective for refractory epilepsy, felbamate's use is severely restricted due to IDRs. Research identified that felbamate is bioactivated to **atropaldehyde** (2-phenylpropenal), a highly reactive electrophile, causing cellular damage and immune activation [cite: 11, 13].
*   **Valproic Acid:** VPA hepatotoxicity, particularly in children with mitochondrial disorders, is linked to the formation of **4-ene-VPA** and the inhibition of mitochondrial $\beta$-oxidation [cite: 14, 15].

---

## 2. Strategies in Rational Drug Design and Lead Optimization

Modern AED discovery has moved away from random screening toward rational design, specifically targeting "clean" pharmacokinetic profiles to minimize metabolic risks while maintaining seizure control.

### 2.1 Structural Modification to Block Metabolic Hotspots
Medicinal chemists utilize Structure-Activity Relationship (SAR) data to modify lead compounds, blocking sites prone to rapid metabolism or bioactivation without compromising receptor binding.

#### 2.1.1 Amide Derivatives and Chirality
Valproic acid (VPA) has high efficacy but significant teratogenicity and hepatotoxicity risks. Research into VPA derivatives aims to retain the anticonvulsant potency while eliminating the carboxylic acid moiety responsible for toxic metabolite formation.
*   **Valnoctamide (VCD):** VCD is a constitutional isomer of valpromide. Unlike valpromide, which acts as a prodrug and is rapidly converted to VPA in vivo, VCD is not biotransformed into its corresponding acid (valnoctic acid) [cite: 16, 17].
*   **Metabolic Advantage:** VCD avoids the formation of the hepatotoxic 4-ene metabolites associated with VPA. Furthermore, VCD exhibits stereoselective pharmacokinetics; it is a chiral drug, and research suggests it may possess a better safety profile regarding teratogenicity compared to VPA [cite: 18, 19].
*   **Mitochondrial Safety:** Studies on rat liver mitochondria show that while VPA strongly inhibits $\alpha$-lipoamide dehydrogenase (a key enzyme in oxidative metabolism), amide analogues like VCD show significantly lower inhibitory effects, suggesting a reduced risk of mitochondrial toxicity [cite: 20, 21].

#### 2.1.2 Deuterium Substitution
A specific strategy to enhance metabolic stability is the replacement of hydrogen atoms with deuterium at metabolic "soft spots."
*   **Mechanism:** The carbon-deuterium bond is stronger than the carbon-hydrogen bond, making it more resistant to enzymatic cleavage by CYP450 enzymes. This can extend the half-life of a drug and reduce the formation of toxic metabolites without altering the drug's binding affinity to its target [cite: 22].
*   **Application:** This approach is used in lead optimization to reduce dosing frequency and improve the safety margin of anticonvulsants [cite: 22].

#### 2.1.3 Steric Hindrance
Modifying the steric environment around a metabolic site can prevent enzymatic attack.
*   **Benzamide Analogues:** In the development of 4-amino-N-phenylbenzamide anticonvulsants, researchers introduced methyl groups ortho to the amino substituent. This steric hindrance precluded N-acetylation, a major metabolic pathway. The resulting dimethyl analogue (Compound 4) showed exceptionally high and prolonged plasma concentrations compared to the unmethylated parent, effectively balancing high potency (ED50 5.6 mg/kg) with metabolic stability [cite: 23].

### 2.2 Multi-Parameter Optimization (MPO)
Drug discovery is no longer about maximizing potency alone. It involves the simultaneous optimization of potency, selectivity, and ADMET (Absorption, Distribution, Metabolism, Excretion, and Toxicity) properties.
*   **The MPO Challenge:** High potency often correlates with high lipophilicity, which unfortunately increases the likelihood of non-specific binding, HERG channel inhibition (cardiotoxicity), and rapid metabolic clearance [cite: 24, 25].
*   **Pareto Optimization:** Researchers use Pareto optimization algorithms to identify compounds that represent the best possible compromise between conflicting objectives (e.g., high brain penetration vs. low metabolic liability) [cite: 24, 26].
*   **Ligand Efficiency:** Metrics such as Ligand Efficiency (LE) and Lipophilic Ligand Efficiency (LLE) are used to ensure that potency is achieved through specific interactions rather than just increasing lipophilicity, which reduces the risk of metabolic promiscuity [cite: 27].

---

## 3. Preclinical Screening Cascades: The Filter for Metabolic Safety

To ensure that new AEDs balance seizure control with safety, candidates pass through a rigorous "screening cascade." This funnel eliminates compounds with poor metabolic profiles early in the process.

### 3.1 Efficacy Screening (The Seizure Control Threshold)
Before assessing metabolic risk, a compound must prove it works. The National Institute of Neurological Disorders and Stroke (NINDS) Epilepsy Therapy Screening Program (ETSP) utilizes specific in vivo models.
*   **Maximal Electroshock (MES):** Identifies agents effective against generalized tonic-clonic seizures and those acting on sodium channels (e.g., phenytoin, carbamazepine) [cite: 28, 29].
*   **6 Hz Model:** A model for "psychomotor" or focal seizures. It is particularly useful for identifying drugs effective in pharmacoresistant epilepsy (e.g., levetiracetam is active here but less so in MES) [cite: 29, 30].
*   **Kindling Models:** (e.g., Corneal Kindled Mouse, Amygdala Kindling). These models mimic epileptogenesis and complex partial seizures, providing data on a drug's ability to raise seizure thresholds in a hyperexcitable brain [cite: 29, 30].

### 3.2 Metabolic Stability and Interaction Screening
Once efficacy is established, the "balance" is tested via in vitro ADME assays.
*   **Microsomal Stability:** Compounds are incubated with liver microsomes (containing CYP enzymes) to determine intrinsic clearance ($CL_{int}$). High throughput LC-MS/MS systems allow rapid ranking of compounds based on their metabolic half-life ($t_{1/2}$) [cite: 22, 31].
*   **CYP Inhibition/Induction Assays:** Candidates are screened for their potential to inhibit major CYP isoforms (1A2, 2C9, 2C19, 2D6, 3A4).
    *   *Selectivity:* Rules of thumb suggest that a good candidate should have an $IC_{50}$ for CYP inhibition that is significantly higher (e.g., >10 µM) than its therapeutic concentration. Compounds like ketoconazole are used as positive controls for lack of selectivity [cite: 32, 33].
    *   *Prediction:* In silico models (e.g., CypReact, vNN-ADMET) predict CYP specificity before synthesis, allowing chemists to design *out* interaction liabilities [cite: 34].

### 3.3 Reactive Metabolite Trapping
To avoid repeating the felbamate disaster, screening for reactive metabolites is now standard.
*   **Glutathione (GSH) Trapping:** Compounds are incubated with microsomes and glutathione. If a reactive electrophile is formed, it will form a conjugate with GSH. These adducts are detected via mass spectrometry (neutral loss scanning). A high "body burden" of covalent binding correlates with idiosyncratic toxicity risk [cite: 35, 36, 37].
*   **Gene Expression Signatures:** Research indicates that even if covalent binding is low, drugs like felbamate induce specific oxidative stress gene signatures in rat liver, providing a sensitive biomarker for idiosyncratic potential [cite: 12, 38].

---

## 4. Pharmacokinetic Profiles of Newer Generation AEDs

The culmination of these research strategies is evident in the "Third Generation" of AEDs. These drugs are characterized by pharmacokinetic profiles designed to minimize metabolic interactions.

### 4.1 Renal Elimination and Low Protein Binding
The ideal AED profile involves renal excretion of the unchanged parent drug, bypassing the hepatic CYP system entirely.
*   **Levetiracetam:** It is the archetype of this strategy. It has linear pharmacokinetics, <10% protein binding, and is primarily excreted unchanged by the kidneys (66%) or via cytosolic hydrolysis (not CYP-dependent) [cite: 39, 40, 41]. Consequently, it has almost no clinically relevant drug-drug interactions [cite: 39, 42].
*   **Gabapentin & Pregabalin:** These are eliminated unchanged by the kidneys. They do not induce or inhibit hepatic enzymes, making them ideal for polytherapy, particularly in elderly patients or those with liver disease [cite: 3, 43, 44].

### 4.2 Non-CYP Metabolism
Some newer drugs are metabolized, but via pathways with lower interaction potential than the CYP system.
*   **Lacosamide:** Primarily cleared renally and metabolized by CYP2C19, but it has a low potential for drug interactions compared to first-generation agents [cite: 4, 28].
*   **Eslicarbazepine Acetate:** Designed as a prodrug to avoid the formation of the toxic epoxide metabolite found in carbamazepine metabolism. It undergoes hydrolytic first-pass metabolism (non-CYP) to the active eslicarbazepine, significantly reducing enzyme induction potential [cite: 3].

### 4.3 The Case of Retigabine (Ezogabine): A Cautionary Tale
Retigabine represented a novel mechanism (Kv7/KCNQ potassium channel opener) and had a metabolic profile independent of CYP450 (metabolized via glucuronidation and acetylation) [cite: 45, 46].
*   **Efficacy:** It showed robust efficacy in resistant partial-onset seizures [cite: 45].
*   **The Imbalance:** Despite a "clean" CYP profile, it was withdrawn due to tissue discoloration (blue skin/retina) and eye toxicity [cite: 47, 48]. This highlights that "metabolic safety" extends beyond just liver enzymes to tissue deposition and other toxicological endpoints.

---

## 5. Systemic Metabolic Risks: Beyond the Liver

Research balancing seizure control with metabolic risk also addresses the chronic, systemic effects of AEDs, which are often mediated by metabolic interference.

### 5.1 Bone Health and Vitamin D Metabolism
Long-term use of enzyme-inducing AEDs (PHT, CBZ, PB) accelerates the catabolism of Vitamin D into inactive metabolites via CYP induction. This leads to hypocalcemia, secondary hyperparathyroidism, and reduced Bone Mineral Density (BMD) [cite: 5, 49, 50].
*   **Research Response:** Screening now includes evaluation of bone turnover markers. There is a preference for non-inducing AEDs (Levetiracetam, Lamotrigine) in populations at risk for osteoporosis. However, data on newer AEDs remains mixed, with some evidence suggesting even non-inducers may affect bone via other mechanisms [cite: 5, 51].

### 5.2 Lipid Profiles and Cardiovascular Risk
Enzyme-inducing AEDs are linked to elevated Total Cholesterol (TC) and Low-Density Lipoprotein (LDL), increasing cardiovascular risk [cite: 52, 53].
*   **Comparative Data:** Studies show that while Phenytoin and Carbamazepine worsen lipid profiles, Valproate and Levetiracetam generally have neutral effects or different metabolic impacts (e.g., weight gain with VPA) [cite: 52, 53].
*   **Clinical Integration:** Research suggests that lipid monitoring should be integral to the safety evaluation of new AEDs, influencing the selection of lead compounds [cite: 52].

---

## 6. Comparative Analysis of AED Generations

The following table summarizes how research has evolved to balance these factors:

| Feature | First Generation (e.g., Phenytoin, Carbamazepine) | Second/Third Generation (e.g., Levetiracetam, Gabapentin) |
| :--- | :--- | :--- |
| **Metabolism** | Extensive Hepatic (CYP450) | Renal Elimination or Non-CYP (Hydrolysis/Glucuronidation) |
| **Interaction Potential** | High (Induction/Inhibition) | Low to Negligible |
| **Protein Binding** | High (>90%) - Displacement risks | Low (<10%) - Minimal displacement risk |
| **Therapeutic Index** | Narrow (~2 for Phenytoin) | Wide |
| **Pharmacokinetics** | Often Non-linear (Zero-order) | Linear (First-order) |
| **Reactive Metabolites** | Common (e.g., Epoxides, Arenes) | Rare / Screened out early |
| **Primary Design Goal** | Efficacy (Screening-based) | Efficacy + ADMET Balance (Rational Design) |

*Data synthesized from [cite: 1, 3, 7, 41, 44].*

---

## 7. Conclusion

The balance between seizure control thresholds and metabolic interaction risks is achieved through a paradigm shift in drug discovery. The field has moved from identifying compounds solely based on anticonvulsant activity in rodent models to a holistic **Multi-Parameter Optimization** approach.

Current research prioritizes:
1.  **Metabolic "Cleanliness":** Selecting candidates that are renally excreted or metabolized by high-capacity, non-inducible pathways (e.g., glucuronidation) to avoid drug-drug interactions [cite: 3, 44].
2.  **Reactive Metabolite Screening:** Utilizing GSH trapping and gene expression assays to detect and eliminate compounds with idiosyncratic toxicity potential (like felbamate) before they reach the clinic [cite: 35, 36].
3.  **Structural Refinement:** Using chemical modification (e.g., amides, deuterium) to block metabolic soft spots and improve safety margins [cite: 18, 22].

While the "perfect" AED—one with complete seizure freedom and zero metabolic liability—remains elusive, the transition from phenytoin to levetiracetam demonstrates the success of this balanced approach. Future directions involving pharmacogenomics and precision medicine promise to further refine this balance, tailoring metabolic safety to the individual patient's genetic profile [cite: 54, 55].

**Sources:**
1. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHB7pEE6Fp-TjCczTCQ64IxSALyCRFirOS7qdD4uI8mdS63dgRxq90_Rhs2bGZCjLye9b3pj_K6ComnpO9V04IH_xsMjG9fT9BXxP1kxqy9-PIIj8PlcKvP8m4hsbBov4VKcHzlRoiAKvWXEKYKH3dW0Ej4QBbZqB2kS1EooIIRMo8usadTD7m6EZU6XyNhcPe0ax8LJLBOTVGRxWMipqT6JGoqsCJ2DQGjopPon1E=)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeYBXJ9ADLB52GTvVlki5-0jPX411uIn2xvsWExgvLcJTf3oDLwjVxXNzBsrkMBMIM1qlL7xrmV6qD9K77Tif6iMEawwRKOTkaXu9cJQji9X5Fk9ZJ562liB4OwSF3Hj1BoWVCswj-oVBj1diw1M1AeD6adT8im69vCVyIQAftqivzDvZC1mroOHl_iI70lYxk_Y1GI-ewGK6ONVNi2HpHnvc=)
3. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_dATi7ImTI0Zx7GfsuyGBJA8DwOe2VidB-0A_KZBNGGO6xppe1eKZ6SCB2e_x6dx2d5A7Rs17JAnr2WkouQS-YvTnY2-MROdTb3g3f2fojCpaenppe-sqWrPoX5MMU6vlKajnsuDn)
4. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7d_eka8KWLaka_TkHcHtPkdWZ1zvGGPZgog62O-ZU3dKR6YnD4u6QNFwS4ZBwdv5U9GTp3k2e1E3VtFKq3iQTW6BS-CJqpD6qzJAZJA2CDEvAP33NCTJfchWAJ0ACZC18VzIRRwId)
5. [jefferson.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDv2OHmJQgM_0CEQzz6Gpb-evx3bc1TwRZq8U_lYZGwdUGniScGZ3zADmmKQqn7mfF7Emq2MkeCTxDktvKJzwHdv7cCVMXOxl9Ho7Do2ENxbFgb143PW4Oa8ix_jAppQFx9RBlCu0lFElAVziEDgKYc8z0jlbor6aYQCq3mrIETrm5thw=)
6. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVV_LxLLPJUZOMWY5piTDv5vjE3u-i9Tk8D8kIICvcOQwxIsWjF4qOBZ9tUMD2HCK-ED8yCQIpFS19Np4OAbFivSzVfvxRF-IzAJ1nuGPm63iCxddFXUiEN-tRHGTzXPY4q9FtIbQ3)
7. [aesnet.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE09iaEuRkHjLONx-IXueyvxzlvWW1KcXgl_WlnAN3eIAVHJbgOWgQmisbBKd60Kgncpow2wu-cN69ehuYDKETZvRJ9HkUO3JoyQksH4MZckv_Jw7mW62NHKSE8zABsZQrFcwNQor3Bz7ETgztk9LtDRMAwsKvuNETdecAcn6kwk0PVKbV6cKafpND_mVFasnNXRA_xiMin6Q==)
8. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHa9xvcf7wkYqy-hOoMu9GjZ07ebkJIVcwS3mRVC0rEbqQwsy717HHZfZ8R-WD4M0AK0TxtOwQoiKSWQxf6GuQC0_gKAmAcr1scTVwk9ZQHcSsD8S_UpznAqUeJavlAcv95i-ivBV9z)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESAsikv0A7Rts4KjPPlN_4NHo9o5OvFuKsvubve5B2c-2ADFBKah9s9p3-8P9N8YoeAk2iUA9C88WpLHRHmkzDu0186Ct18PeabCbaE7zu0w4cDp2Thv2KMbNvPIu-ts1Km1U=)
10. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcumt9mA-e1J9-1pE5AOjy0DT34x8ONkEy4xUiZmJIkD5A1C-SpYBMWem4kMBzCWTCt8f9qscUY7UsTgtj9OJgTdM0ohHQs7oYvfBYLIVwqVbV_qTsjZRa587ENwakIjBFAZo=)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKVzk8lto3njDaj6FvRMlMTmXxqBYp9Se3S857JHVeM8tR4v3JGfIzgi-XoTYMsgwn4PXMt21i2MVa-t8VGtIIfBfeRwO2WtWkJqx1y4c_74cLZpK3V30B9u7p5BGrXvKnuoZu3V4oc62hHG1o7X6qTE8o0PjEo2I-Ob2DD7Ee3R_Rm6eNjDkk9wA0aGj0sZgbGl9Mx9Vk89AeHmZduqjPJUf9EBc-F_s=)
12. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG06q0YvMDmtnew4cZaiR5lAH29PJQjUIPCHhFRP56cg8V_VNdLy-z9ujdn7qGI8dH0KRYR7EwsOJ5WqMJrOftJoRnUdQo0mtmBtyAs0F0JWRs5OwUCuQ7PyqrrvRSrAmTM10Og)
13. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5UhlpBxojnvhzv9WfponRdGPbeVgZovBcuxCuTcIL0KMulBOs5Z3Kfs4OR1rteWho0q0k1nRxY6OTDvSF3F0z75jXDBAwkBXiJo9oCpa5RFI-MrDisoBphng2ctnuSg==)
14. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEj-tCuMUWENvELed7O2nCNl4YkcMUZ81GeNOWeX7JVwaQ1mZxlcNmFQbCnjfSfclYan9j3sHYt4CUDdoyJryuzfrDspbDR59lCnzrFRlRe6t1ZczB-_jigZe7aiuFURg==)
15. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYzRxvmjBE0rE72DxFnGZTgfjXVY5nAmeXQGt90PiqBMGvFJYZVDy4xdmk_J3OExh4QmY0h5gwRkjcmzsXmtcCR_p8p8qp_oyoCMtuKp0OzXBzkZ7zHGkhruwF1UZqWA==)
16. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGm5toynHs9JM7eqCkBsbhDr1srBMqBV0WOzasYVZMTKC3ICV5CbiyIJrmoD_xiC0g2-d1rKe7ySisTpg_89udkf1nHPYuUG1E2iBIw2hIb5bktiDS-tXRwxk2UrKhXO8wL4KjrA-UF)
17. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDmdFOks6nMPO64333ATmBtkMe3foMBhD-TnsZAO--Ex5RV5qhepnfzFQ5OCyTrYVj71im4YItZTTYnXsLSbNrBgO3Hmz7ykGSeOLFIlxc1VIUICA71EndsqzPrZ6u)
18. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFK46ify518OooAhoXbqh6tMkAmjhXDqRJJSauVt4WUz2O3c4wSMmhiJI65KwbNFNxhDOOZgzJ387qZzbKpdJIYVZbup7fwfnLXbUtDPFfGBxqpkgWm1DjbrHxBcutVA==)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDhSEyZq2kCLL2G7gsyPKBTVQ82U9fHzZGDeewJzfeT5ds8dBhU1gzdnY-_orMPeAFejb_FZCZu8WP4UVNDXR8WgouX68gO4nfep_k1m9Zh2KqKppSz5acvf1ErWOc0vCqbPAx70v9scSw0G00m5pwyGzr1sP6M_xs9l3d8jj96BN7ZxTzTCUXyI7S-XuF6fLP9XNs-HRY1hs7Z82XU5mUnl-6Yj4Zui9JpVaFJ1ZVfrQRQUX-kgpaTxpPmFCd9rQcxwDqpjHoDqV85RKc)
20. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNw3CMgRM1JhWaDs5ZqYOYYx24UagjwwI9hU8sFwJ9sK6pQ0d4D_ZBvQ8UXuNayu59JoTJ9hxwZmoL_Voh28EnPfGK25ZLz36v_INhqXhPokSrNeMpJ2coXjl5YBIQ)
21. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQpT0oIexoKJaxP9qf9qCvYSw7Hmo0dmdf9DrIBm0jEh6Xq9EjTuUGuDx1sgO-AjOZFWW9DfIrYEqT4uqi8zI08YW_NLCHTBCxCjjfifVpItR0l5JwXTc0438-T095T9fVEMUkCMYg7GNga2ccUxc5tEh8QwBTC-3yxCHu_ZrOLDN6ZtTKZeSppaVMQ2cHKmDqorctdwDFXS7CBkueydMBRWX1WZYya2CUlQUaKfXAwT8GNwzkrvYmrw8x6bwHkCaMXClPPba0kWfMDsOSTa1HRoXA3EdtwlJr_MohlPSibBn8xA0pyg==)
22. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWGDovo0GxU8iSklPWa0wSTIzQFtqlV9DriL3EKQzXM-5Rv1schy8L4I-Kf66HcemRtm3756d6BpHzjVRn2bO3hwccley-LAvCKoy9D8pgrKAjUeHzFdvM7_xI8m_e8Q==)
23. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE180L-_KUzW6Frne5nKOOTv1fdml3LZlAppsr5NWk8FKZ2P_csH8ESetwEfSjo90sFFOtrS9OpR6Z5rr0IWrlg-IVG2K69YImJlTu1nLzachj1daFHQIR1FL-qJIGO)
24. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7L9pxOK5p-44xuOUFCAGnX8Wo-lsUsuBkFQuRT_CaecjgIK5kb5IT5yxr98GKPrn7tOBA8LS3kzCbsyrUHVldZd5cKROcDXMaezj877tl-BEIqIeC7daDPqFsG3Xllg==)
25. [optibrium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHo-QeE_6QJE6BxCSlqATy5ezdOoweaeA11UjNpYCeAghAbfILYpq4PyeJoIqVB5-aaXvFsy5AfLAgY-jhuEAmNHHV4vLseSaoayIgudYSUWexOsyqfWJUIhPOP2ZszlAH9Al7M1V2C-R7C7TYP)
26. [chemrxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4c255_CahM25h1wLaBJBPtEjL1JXvxv4qgJFYD8rAqaZzUaNVGEEZYg32fgGX9WKlpWQY4ZAw3twh15yoQXupC2a5VvigaMQRgmsSjt0zqJ8dxQ7QwvPBGZwz96xgKGHL93t57CEka_A7zmGPUEEjCMbm0ZDwq0apcsXyXTvSDFrYhQ==)
27. [optibrium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaSiNahpQeqY6_wQ3zyTNS1G3kOE98PYaHxW5QwVmPvBxBNiHL1XVpwMYksKRG8YoDZ-dkWND70y1724gseLa8bg8W-DQaYjqJ8mW3IGT3YKou962NsRFh_2lAWtszijA1U3YnCY0SYhJGpmBv_0979dsIYCBVw2jS-AVNCgYLDAI_SPInAc1BNs1Z7uXLzX0HCMoXeKCFluSjHmRnOPA=)
28. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcYtti7fH9kyvK7GJHJHsSEV2PgYjN1vDaxPi7tEH_PfQZQJTi58QPhOsW0y5dnR6SgW98NBFuhW2WVkiMR9I6kp0ZmAOFi4QQmPnqvO98FLurQ1zNAmlKvwAmMqqKD0OOrdhRghJC)
29. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHL_rg7Hwdbmwgz2KOCXJruETmUFVwXvnWPOfUiLAF4t7LXUUo26EgSOSC2SD0jan83YYJD4i8qIjR8-3LNSIWUGNB5aGiKKegp-D8a6xXgxwG3rJkMO_gsWQqqeLJtDbGknfX3oruu)
30. [aesnet.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnwheH9W_I-uFOSVyCu1e8KnME1Wi70eThxYtM9zPKL7W6yvEznslFeYNhPRMgG-5SAVzEfEZVADCeGRFGdDLrHw1CsQasQ6nM_HbNdR6y7n1BDGF191tqx2pTqb7QJsRLzVXE-y2knvyuYvGJX0-XiKNNPwvoi3zxleqJBc3yxrjx5VnXvZQo0fow9CCJ_Z3ScU_HhVQJXKLdjqd6m4OzmyTNag==)
31. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6oexXXdnLHJTw_MewZEnWbYyIxF2Q_PjF239OKvCsnuNmmIsli63nyFBLn5AxsjuilCdpmqhrpdc5TnAmDSbelVrbhsjnwZj9MLTm8qdmF9w_0VW7A2qhBi8_Nhj-yQ==)
32. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdKc-limseGotMQNUG5jAh8YW5si0avpvjykBkHgV21zkfmv4AvqEiDhS-JO8U99yYOkXExh3P988BH77l7bcsfG8kyspZcT2nsjfkGGsW89sHLxIqRQvNUCfxnAmPng==)
33. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEk7ElpNGRmr-mosfOkmrEWpI3u86YfPNyTah3NMQfiWnhagA-L9zrI_lkA4U-K133wiI-cK9CzpRfQDNAQWGVxzv1vJ5Wuu1BsnNaPnQ9DTVpqA-HZAOggpZvTGF0S9q8x8U9xR2LCSltypaH1NiDs9-Q_PZkx55WxldTbyvMav4vSj1InrzWfxYU6Dv6AERdT_MGnTTGYkFJgVo3KcOxagbgt9GQEERRaQlYZnv06ChzvVy25xEP8rhqgRO5bU-hKoiBfuvkUczB5hOWN4y1wxomdoP_rNPeOSok8uFp55w965hoK2qjLjpo-6C7JwChI7bUe5u0U5GM29aWOdR1TwWVZLc6q_0WMlyqnt6bb0Wm4BLjhVyeLfsldTaKPVIlu)
34. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPcjeTmEIiX8NUnUvs6T5wHJtEs1bdpXUsut2nLAPmL6mij0EFUxJ1xghTupzWdOZ-FT7-a1Mqg0C6o913aqHYbKRof6JXEwSnJWyYTLnEPoRaSbm1OWmvpKefJKtGDzx_yZbdHuyh)
35. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuFxXaCmN-oxapjzRb4rKaYGs2ezk3f0AuQNYYkS_g8c4v5nSQEgjBnGOFU17pKqWhXszv3jbqe-Usu0pLvhU9AF1H-rNIzwGSeT8TvuSOorOpDqTMwPt6pEN49RReuA==)
36. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1PaUl9MOoz5AzoGWsRwomcMtwUvVjRTPrlixlM7bdXJH8XidpGZ-MFIutZhY35zhNELABT7r-aPJ1TqERgvrrQgez-_vC0LQY4WBeKl3Eo3OVRvwpALK8ijMfuM9LrA==)
37. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHd1okHvLSa7Iz9dTopn-efUWi1b971tDTR-dlEJFYN39_3drr-fN7MQh0MsZt_yyxjSAU44-1Tl1WZmb8X821O8Nts5ijfnV3g6zP3sMEbL2Rk2v9MWRPw7C9hjIvLUKLYyRNbCM_m6oYoSxplvK7)
38. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkP9np56kJ-8wNoALtgGT1uFO_siF2Jj9iEkiqLIuFV6HdtpY34ZRBtIWHNCikOFAXMIw3w5pfpGjldlGqUJcpFzcpxFarV4goZ4VGXpkQ3-CdOrkLrIb3kD8ZuzrRQw==)
39. [droracle.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL3gY7V1EBPxfQizVnxb3HzcNCmZXj0VRMCan9lGny7dTmWLzg7FhJI6UVUFwb0wVxGYQXBUwS3sJu9uHzBjfGx9aD6LsPosRKR53_8CnzJqy5Xu4NX8NfpY-cKKEI3IjZXO5xN6yzrHjLzl78uS096mI-J2SprWtxDeCo4T39WkWsbdTDfeHJheVpCzimn30ryK96zGPX9pbuHg1cFRwQ2EVdm6kEYQ==)
40. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElBwW2vRSJ5vTsB-UyBIr2r9EsLRujeEjn9M1380PMKr0iULCjl7Y8qV_FSYPHeRAkjSpbiy4mZtVozPcUmxhxR4LJZ1iyMIowRroVm0rFUvpiKY5A8yls1WOSu38Ouc6-MYI=)
41. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjpOFJHzKgMqP5LVFEJXQp5DS6Keq9Comqcbu9EUI8WZjI69lRCt9C1SbxTlVMZGe-IzhPxQmdtnRwCxxutktFa3S-AwVC4hVL_i5hccXACsmw-5tm6wbm1Cldy8cfFA==)
42. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPZc3QEl1ewDpMMF6jWnpTqeJm95jAYRFibjNLGjzm7uBMgdEr47ygJeEYsfyti1BGFSIT-0FlhgZiKPTtdSjtYiIfJDuwl73qyDFvxPmF9NiY76Yfm15bsVVuCGMyD0QSnIvbyapL)
43. [drugs.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMogUPj6gwqJXgf0ChZ3Ab8jPBEJFX9cx-gZ_P7IPdN5f44bCKeMajVk5kHqWl0UTQ2ca8AGp6-eyO1K1mB06cqxbBw02mcikaH6y4T9AEHDiu9wZRIO4c1KMygjmP202gf6KXbL4oYihUsWuUHxozCJqV2-zqyQRLL4jeeA25QU6EVF8LK2R2-3qorhhSY1tr1QrdU57OL2DZ0rzg)
44. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhv3o3a5ifcoCA3f1UhyThb5qWnHJ-TOXtahey3ieI0T_DaAKRqQrAkOJfqdTLVexXAkN4plWa-L33djr7S4HnLQ4oJWwfve5uz2NpgsZQlVoXJr2FMrUozwyOIeEOKQ==)
45. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkuhznw3w05Yed-6p_IiPyJwTGzzO4Sjr1Bv92gPBkH3fWJ4xPSuEzLlbVK2KvjHQsXrtiR1N1z6rot6Y_d2VzRe6kdc6mjA7Tym9PFW5H0cbxG-XkWgrBZbRlZPKzqQ==)
46. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHiJnmRIagUZF-nVj8wWG2EfyNbTltoWnHcEAiWtIrUw1EVG2zWBXoDXodecmDkSApY-0W93GtM6qEObQqtX7IC7a8pCRHr3MhO5mAjRCQS45O9IZKf8gjKY4TxlA77Ag==)
47. [alzdiscovery.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJdSTPBn220duejecSs07CEHERedpmbeg0xYynzYd493yYkmCBZhtV06P3TOL0WmJiqelEFQW9BjkkcxL5k8qnjNCkUDSktD7urpz6RoSRxo9ykcvTAR_QBsXqBgg55M8UXyffRsIG2SNz6oLSwL33hYHpO50vMDGQI_gmoJdojPdA)
48. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQA12AdvbDs6Kp8ej5Bj9ewNIH1g6PgZJw_-6Y-trPqcTMa95W9VVdwBsbQIRLynL6OnZ408P3NC9A0D-RM4mw0fJl99RL8FwNmcVIk7UU9ErjXJrqKSz54P8f3b-BSzovIytImiCK6OgJlkR1lzCdk3yoGOtgJxCSLoHtgUnW47RWvYlya1QNpJSgESrN_KYMOO5Pf8AzvhwX1sS_vaAWy-5uzr1kYhrc3av9dRfH9WV7Tpnnl4NKvsR1HJl5s7fpYPjbWqijLc53wkzGHX4wwYITCtbHS1h4)
49. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEf31DxgXE8l2IRLA5Brya1cD5g12ZXEljsQ_wRQ5jyT_mBYKiOeQBmzf7iNOFaG9mbblDQwrRx0BZrokUJaXjo4btW3vfeFyTV29uzqRE-SbewhVH9wt1NhjsHfvtQ)
50. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIUJYZ7mH3JhZjTtYSMY5vd3OMWuSIbhbGWRpXToWQyNuQuyeds1uw8zHuDZyhbhyvuU51BW2ciWSwUpNimWq3jQ-KtbqkLiWsh9SCaZTkoFUoQ-gKJ68dV4WZfSbArISkthBTHxdm3A==)
51. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERECx7RzpsPGHfyV4xghPgTtinYnXsdpBF0_B7nPIMcgXEZ4BQpbjeP-o7ztckRs3gLCtsJOz6go7ABEJNvEPimmtg7LH0Ypc24JuERGQRX22fXHy_xKYxLIKvwv7iBz_yzrfTmBSe)
52. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdiO4RJcXea0rC5vd9k_n70hYeywgyk8T4WPXMUzxstsZEMJPtKJg_SDL0Pezj0VOjVIOgqwecCVYs6qmwDIz5nm_AwFT3GRv__Fqs26ndDV_FUQBYKSOxWC28TRZdzw==)
53. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoXFoD_0JcW1vxcYJt8o4vaW85P1JkVR4zWzMMz-uc4-VrVwmJCQoJvwRxwuTjUBJXTe5-6vw7PCJ6LsB4LF7_FX_A2qnVcJmc0THJ-CQQ21amhy3Ox_XGzC_3tsDWZ1C4Xc5aL7cu)
54. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7xKiPakGNbPNPR3tG74xEClgK6htL1akcz7_DyO5qsDotj7sD057dqtkbY_GnvB4jViWrpEDf2c-_c1gmEjxyNmGY8u14bbbGy52WLvrgcl739mwYlP52RzfZOSqgcC1HMzKFVfZbw0ZSpk3Q8tVXjxyZTql2HtyZAmJ6cNN9tTeN_eICQb3Zi_5p9wxFcqHJYHtOlWJuAnWaIZAtvwKmnOc61iUvrobK-6ypQu7AVFHwAdBYh5iVW_YBxyTFP933jIk0B7jJwijVxDYE-P5KTYXaPtTBGZSOHvt0087O5V1SSrY3LQ==)
55. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGX6h_ersKiKyYdRwMzkLGm77avR51xAKNfDAwqooy7q4CkHXeEQUpF_I1pTZ2ZNxXK6CWXldEb2CQUgNDIkiXGKj51CvXKJQ0iNP0u3QKbfGDQg7BRDDlypWA20oK57Jv-5NS1KC9Z)


## Annotations
Annotation(end_index=3188, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHB7pEE6Fp-TjCczTCQ64IxSALyCRFirOS7qdD4uI8mdS63dgRxq90_Rhs2bGZCjLye9b3pj_K6ComnpO9V04IH_xsMjG9fT9BXxP1kxqy9-PIIj8PlcKvP8m4hsbBov4VKcHzlRoiAKvWXEKYKH3dW0Ej4QBbZqB2kS1EooIIRMo8usadTD7m6EZU6XyNhcPe0ax8LJLBOTVGRxWMipqT6JGoqsCJ2DQGjopPon1E=', start_index=3176)
Annotation(end_index=3188, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeYBXJ9ADLB52GTvVlki5-0jPX411uIn2xvsWExgvLcJTf3oDLwjVxXNzBsrkMBMIM1qlL7xrmV6qD9K77Tif6iMEawwRKOTkaXu9cJQji9X5Fk9ZJ562liB4OwSF3Hj1BoWVCswj-oVBj1diw1M1AeD6adT8im69vCVyIQAftqivzDvZC1mroOHl_iI70lYxk_Y1GI-ewGK6ONVNi2HpHnvc=', start_index=3176)
Annotation(end_index=3387, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7d_eka8KWLaka_TkHcHtPkdWZ1zvGGPZgog62O-ZU3dKR6YnD4u6QNFwS4ZBwdv5U9GTp3k2e1E3VtFKq3iQTW6BS-CJqpD6qzJAZJA2CDEvAP33NCTJfchWAJ0ACZC18VzIRRwId', start_index=3375)
Annotation(end_index=3387, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_dATi7ImTI0Zx7GfsuyGBJA8DwOe2VidB-0A_KZBNGGO6xppe1eKZ6SCB2e_x6dx2d5A7Rs17JAnr2WkouQS-YvTnY2-MROdTb3g3f2fojCpaenppe-sqWrPoX5MMU6vlKajnsuDn', start_index=3375)
Annotation(end_index=3670, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7d_eka8KWLaka_TkHcHtPkdWZ1zvGGPZgog62O-ZU3dKR6YnD4u6QNFwS4ZBwdv5U9GTp3k2e1E3VtFKq3iQTW6BS-CJqpD6qzJAZJA2CDEvAP33NCTJfchWAJ0ACZC18VzIRRwId', start_index=3658)
Annotation(end_index=3670, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDv2OHmJQgM_0CEQzz6Gpb-evx3bc1TwRZq8U_lYZGwdUGniScGZ3zADmmKQqn7mfF7Emq2MkeCTxDktvKJzwHdv7cCVMXOxl9Ho7Do2ENxbFgb143PW4Oa8ix_jAppQFx9RBlCu0lFElAVziEDgKYc8z0jlbor6aYQCq3mrIETrm5thw=', start_index=3658)
Annotation(end_index=3826, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_dATi7ImTI0Zx7GfsuyGBJA8DwOe2VidB-0A_KZBNGGO6xppe1eKZ6SCB2e_x6dx2d5A7Rs17JAnr2WkouQS-YvTnY2-MROdTb3g3f2fojCpaenppe-sqWrPoX5MMU6vlKajnsuDn', start_index=3817)
Annotation(end_index=4028, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_dATi7ImTI0Zx7GfsuyGBJA8DwOe2VidB-0A_KZBNGGO6xppe1eKZ6SCB2e_x6dx2d5A7Rs17JAnr2WkouQS-YvTnY2-MROdTb3g3f2fojCpaenppe-sqWrPoX5MMU6vlKajnsuDn', start_index=4016)
Annotation(end_index=4028, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeYBXJ9ADLB52GTvVlki5-0jPX411uIn2xvsWExgvLcJTf3oDLwjVxXNzBsrkMBMIM1qlL7xrmV6qD9K77Tif6iMEawwRKOTkaXu9cJQji9X5Fk9ZJ562liB4OwSF3Hj1BoWVCswj-oVBj1diw1M1AeD6adT8im69vCVyIQAftqivzDvZC1mroOHl_iI70lYxk_Y1GI-ewGK6ONVNi2HpHnvc=', start_index=4016)
Annotation(end_index=4210, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7d_eka8KWLaka_TkHcHtPkdWZ1zvGGPZgog62O-ZU3dKR6YnD4u6QNFwS4ZBwdv5U9GTp3k2e1E3VtFKq3iQTW6BS-CJqpD6qzJAZJA2CDEvAP33NCTJfchWAJ0ACZC18VzIRRwId', start_index=4198)
Annotation(end_index=4210, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVV_LxLLPJUZOMWY5piTDv5vjE3u-i9Tk8D8kIICvcOQwxIsWjF4qOBZ9tUMD2HCK-ED8yCQIpFS19Np4OAbFivSzVfvxRF-IzAJ1nuGPm63iCxddFXUiEN-tRHGTzXPY4q9FtIbQ3', start_index=4198)
Annotation(end_index=4666, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE09iaEuRkHjLONx-IXueyvxzlvWW1KcXgl_WlnAN3eIAVHJbgOWgQmisbBKd60Kgncpow2wu-cN69ehuYDKETZvRJ9HkUO3JoyQksH4MZckv_Jw7mW62NHKSE8zABsZQrFcwNQor3Bz7ETgztk9LtDRMAwsKvuNETdecAcn6kwk0PVKbV6cKafpND_mVFasnNXRA_xiMin6Q==', start_index=4654)
Annotation(end_index=4666, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHa9xvcf7wkYqy-hOoMu9GjZ07ebkJIVcwS3mRVC0rEbqQwsy717HHZfZ8R-WD4M0AK0TxtOwQoiKSWQxf6GuQC0_gKAmAcr1scTVwk9ZQHcSsD8S_UpznAqUeJavlAcv95i-ivBV9z', start_index=4654)
Annotation(end_index=5030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESAsikv0A7Rts4KjPPlN_4NHo9o5OvFuKsvubve5B2c-2ADFBKah9s9p3-8P9N8YoeAk2iUA9C88WpLHRHmkzDu0186Ct18PeabCbaE7zu0w4cDp2Thv2KMbNvPIu-ts1Km1U=', start_index=5017)
Annotation(end_index=5030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcumt9mA-e1J9-1pE5AOjy0DT34x8ONkEy4xUiZmJIkD5A1C-SpYBMWem4kMBzCWTCt8f9qscUY7UsTgtj9OJgTdM0ohHQs7oYvfBYLIVwqVbV_qTsjZRa587ENwakIjBFAZo=', start_index=5017)
Annotation(end_index=5376, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG06q0YvMDmtnew4cZaiR5lAH29PJQjUIPCHhFRP56cg8V_VNdLy-z9ujdn7qGI8dH0KRYR7EwsOJ5WqMJrOftJoRnUdQo0mtmBtyAs0F0JWRs5OwUCuQ7PyqrrvRSrAmTM10Og', start_index=5362)
Annotation(end_index=5376, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKVzk8lto3njDaj6FvRMlMTmXxqBYp9Se3S857JHVeM8tR4v3JGfIzgi-XoTYMsgwn4PXMt21i2MVa-t8VGtIIfBfeRwO2WtWkJqx1y4c_74cLZpK3V30B9u7p5BGrXvKnuoZu3V4oc62hHG1o7X6qTE8o0PjEo2I-Ob2DD7Ee3R_Rm6eNjDkk9wA0aGj0sZgbGl9Mx9Vk89AeHmZduqjPJUf9EBc-F_s=', start_index=5362)
Annotation(end_index=5684, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5UhlpBxojnvhzv9WfponRdGPbeVgZovBcuxCuTcIL0KMulBOs5Z3Kfs4OR1rteWho0q0k1nRxY6OTDvSF3F0z75jXDBAwkBXiJo9oCpa5RFI-MrDisoBphng2ctnuSg==', start_index=5670)
Annotation(end_index=5684, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKVzk8lto3njDaj6FvRMlMTmXxqBYp9Se3S857JHVeM8tR4v3JGfIzgi-XoTYMsgwn4PXMt21i2MVa-t8VGtIIfBfeRwO2WtWkJqx1y4c_74cLZpK3V30B9u7p5BGrXvKnuoZu3V4oc62hHG1o7X6qTE8o0PjEo2I-Ob2DD7Ee3R_Rm6eNjDkk9wA0aGj0sZgbGl9Mx9Vk89AeHmZduqjPJUf9EBc-F_s=', start_index=5670)
Annotation(end_index=5896, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYzRxvmjBE0rE72DxFnGZTgfjXVY5nAmeXQGt90PiqBMGvFJYZVDy4xdmk_J3OExh4QmY0h5gwRkjcmzsXmtcCR_p8p8qp_oyoCMtuKp0OzXBzkZ7zHGkhruwF1UZqWA==', start_index=5882)
Annotation(end_index=5896, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEj-tCuMUWENvELed7O2nCNl4YkcMUZ81GeNOWeX7JVwaQ1mZxlcNmFQbCnjfSfclYan9j3sHYt4CUDdoyJryuzfrDspbDR59lCnzrFRlRe6t1ZczB-_jigZe7aiuFURg==', start_index=5882)
Annotation(end_index=6966, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDmdFOks6nMPO64333ATmBtkMe3foMBhD-TnsZAO--Ex5RV5qhepnfzFQ5OCyTrYVj71im4YItZTTYnXsLSbNrBgO3Hmz7ykGSeOLFIlxc1VIUICA71EndsqzPrZ6u', start_index=6952)
Annotation(end_index=6966, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGm5toynHs9JM7eqCkBsbhDr1srBMqBV0WOzasYVZMTKC3ICV5CbiyIJrmoD_xiC0g2-d1rKe7ySisTpg_89udkf1nHPYuUG1E2iBIw2hIb5bktiDS-tXRwxk2UrKhXO8wL4KjrA-UF', start_index=6952)
Annotation(end_index=7277, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFK46ify518OooAhoXbqh6tMkAmjhXDqRJJSauVt4WUz2O3c4wSMmhiJI65KwbNFNxhDOOZgzJ387qZzbKpdJIYVZbup7fwfnLXbUtDPFfGBxqpkgWm1DjbrHxBcutVA==', start_index=7263)
Annotation(end_index=7277, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDhSEyZq2kCLL2G7gsyPKBTVQ82U9fHzZGDeewJzfeT5ds8dBhU1gzdnY-_orMPeAFejb_FZCZu8WP4UVNDXR8WgouX68gO4nfep_k1m9Zh2KqKppSz5acvf1ErWOc0vCqbPAx70v9scSw0G00m5pwyGzr1sP6M_xs9l3d8jj96BN7ZxTzTCUXyI7S-XuF6fLP9XNs-HRY1hs7Z82XU5mUnl-6Yj4Zui9JpVaFJ1ZVfrQRQUX-kgpaTxpPmFCd9rQcxwDqpjHoDqV85RKc', start_index=7263)
Annotation(end_index=7590, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNw3CMgRM1JhWaDs5ZqYOYYx24UagjwwI9hU8sFwJ9sK6pQ0d4D_ZBvQ8UXuNayu59JoTJ9hxwZmoL_Voh28EnPfGK25ZLz36v_INhqXhPokSrNeMpJ2coXjl5YBIQ', start_index=7576)
Annotation(end_index=7590, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQpT0oIexoKJaxP9qf9qCvYSw7Hmo0dmdf9DrIBm0jEh6Xq9EjTuUGuDx1sgO-AjOZFWW9DfIrYEqT4uqi8zI08YW_NLCHTBCxCjjfifVpItR0l5JwXTc0438-T095T9fVEMUkCMYg7GNga2ccUxc5tEh8QwBTC-3yxCHu_ZrOLDN6ZtTKZeSppaVMQ2cHKmDqorctdwDFXS7CBkueydMBRWX1WZYya2CUlQUaKfXAwT8GNwzkrvYmrw8x6bwHkCaMXClPPba0kWfMDsOSTa1HRoXA3EdtwlJr_MohlPSibBn8xA0pyg==', start_index=7576)
Annotation(end_index=8066, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWGDovo0GxU8iSklPWa0wSTIzQFtqlV9DriL3EKQzXM-5Rv1schy8L4I-Kf66HcemRtm3756d6BpHzjVRn2bO3hwccley-LAvCKoy9D8pgrKAjUeHzFdvM7_xI8m_e8Q==', start_index=8056)
Annotation(end_index=8218, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWGDovo0GxU8iSklPWa0wSTIzQFtqlV9DriL3EKQzXM-5Rv1schy8L4I-Kf66HcemRtm3756d6BpHzjVRn2bO3hwccley-LAvCKoy9D8pgrKAjUeHzFdvM7_xI8m_e8Q==', start_index=8208)
Annotation(end_index=8804, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE180L-_KUzW6Frne5nKOOTv1fdml3LZlAppsr5NWk8FKZ2P_csH8ESetwEfSjo90sFFOtrS9OpR6Z5rr0IWrlg-IVG2K69YImJlTu1nLzachj1daFHQIR1FL-qJIGO', start_index=8794)
Annotation(end_index=9301, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7L9pxOK5p-44xuOUFCAGnX8Wo-lsUsuBkFQuRT_CaecjgIK5kb5IT5yxr98GKPrn7tOBA8LS3kzCbsyrUHVldZd5cKROcDXMaezj877tl-BEIqIeC7daDPqFsG3Xllg==', start_index=9287)
Annotation(end_index=9301, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHo-QeE_6QJE6BxCSlqATy5ezdOoweaeA11UjNpYCeAghAbfILYpq4PyeJoIqVB5-aaXvFsy5AfLAgY-jhuEAmNHHV4vLseSaoayIgudYSUWexOsyqfWJUIhPOP2ZszlAH9Al7M1V2C-R7C7TYP', start_index=9287)
Annotation(end_index=9549, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4c255_CahM25h1wLaBJBPtEjL1JXvxv4qgJFYD8rAqaZzUaNVGEEZYg32fgGX9WKlpWQY4ZAw3twh15yoQXupC2a5VvigaMQRgmsSjt0zqJ8dxQ7QwvPBGZwz96xgKGHL93t57CEka_A7zmGPUEEjCMbm0ZDwq0apcsXyXTvSDFrYhQ==', start_index=9535)
Annotation(end_index=9549, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7L9pxOK5p-44xuOUFCAGnX8Wo-lsUsuBkFQuRT_CaecjgIK5kb5IT5yxr98GKPrn7tOBA8LS3kzCbsyrUHVldZd5cKROcDXMaezj877tl-BEIqIeC7daDPqFsG3Xllg==', start_index=9535)
Annotation(end_index=9831, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaSiNahpQeqY6_wQ3zyTNS1G3kOE98PYaHxW5QwVmPvBxBNiHL1XVpwMYksKRG8YoDZ-dkWND70y1724gseLa8bg8W-DQaYjqJ8mW3IGT3YKou962NsRFh_2lAWtszijA1U3YnCY0SYhJGpmBv_0979dsIYCBVw2jS-AVNCgYLDAI_SPInAc1BNs1Z7uXLzX0HCMoXeKCFluSjHmRnOPA=', start_index=9821)
Annotation(end_index=10569, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcYtti7fH9kyvK7GJHJHsSEV2PgYjN1vDaxPi7tEH_PfQZQJTi58QPhOsW0y5dnR6SgW98NBFuhW2WVkiMR9I6kp0ZmAOFi4QQmPnqvO98FLurQ1zNAmlKvwAmMqqKD0OOrdhRghJC', start_index=10555)
Annotation(end_index=10569, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHL_rg7Hwdbmwgz2KOCXJruETmUFVwXvnWPOfUiLAF4t7LXUUo26EgSOSC2SD0jan83YYJD4i8qIjR8-3LNSIWUGNB5aGiKKegp-D8a6xXgxwG3rJkMO_gsWQqqeLJtDbGknfX3oruu', start_index=10555)
Annotation(end_index=10794, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnwheH9W_I-uFOSVyCu1e8KnME1Wi70eThxYtM9zPKL7W6yvEznslFeYNhPRMgG-5SAVzEfEZVADCeGRFGdDLrHw1CsQasQ6nM_HbNdR6y7n1BDGF191tqx2pTqb7QJsRLzVXE-y2knvyuYvGJX0-XiKNNPwvoi3zxleqJBc3yxrjx5VnXvZQo0fow9CCJ_Z3ScU_HhVQJXKLdjqd6m4OzmyTNag==', start_index=10780)
Annotation(end_index=10794, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHL_rg7Hwdbmwgz2KOCXJruETmUFVwXvnWPOfUiLAF4t7LXUUo26EgSOSC2SD0jan83YYJD4i8qIjR8-3LNSIWUGNB5aGiKKegp-D8a6xXgxwG3rJkMO_gsWQqqeLJtDbGknfX3oruu', start_index=10780)
Annotation(end_index=11039, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnwheH9W_I-uFOSVyCu1e8KnME1Wi70eThxYtM9zPKL7W6yvEznslFeYNhPRMgG-5SAVzEfEZVADCeGRFGdDLrHw1CsQasQ6nM_HbNdR6y7n1BDGF191tqx2pTqb7QJsRLzVXE-y2knvyuYvGJX0-XiKNNPwvoi3zxleqJBc3yxrjx5VnXvZQo0fow9CCJ_Z3ScU_HhVQJXKLdjqd6m4OzmyTNag==', start_index=11025)
Annotation(end_index=11039, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHL_rg7Hwdbmwgz2KOCXJruETmUFVwXvnWPOfUiLAF4t7LXUUo26EgSOSC2SD0jan83YYJD4i8qIjR8-3LNSIWUGNB5aGiKKegp-D8a6xXgxwG3rJkMO_gsWQqqeLJtDbGknfX3oruu', start_index=11025)
Annotation(end_index=11451, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWGDovo0GxU8iSklPWa0wSTIzQFtqlV9DriL3EKQzXM-5Rv1schy8L4I-Kf66HcemRtm3756d6BpHzjVRn2bO3hwccley-LAvCKoy9D8pgrKAjUeHzFdvM7_xI8m_e8Q==', start_index=11437)
Annotation(end_index=11451, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6oexXXdnLHJTw_MewZEnWbYyIxF2Q_PjF239OKvCsnuNmmIsli63nyFBLn5AxsjuilCdpmqhrpdc5TnAmDSbelVrbhsjnwZj9MLTm8qdmF9w_0VW7A2qhBi8_Nhj-yQ==', start_index=11437)
Annotation(end_index=11885, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEk7ElpNGRmr-mosfOkmrEWpI3u86YfPNyTah3NMQfiWnhagA-L9zrI_lkA4U-K133wiI-cK9CzpRfQDNAQWGVxzv1vJ5Wuu1BsnNaPnQ9DTVpqA-HZAOggpZvTGF0S9q8x8U9xR2LCSltypaH1NiDs9-Q_PZkx55WxldTbyvMav4vSj1InrzWfxYU6Dv6AERdT_MGnTTGYkFJgVo3KcOxagbgt9GQEERRaQlYZnv06ChzvVy25xEP8rhqgRO5bU-hKoiBfuvkUczB5hOWN4y1wxomdoP_rNPeOSok8uFp55w965hoK2qjLjpo-6C7JwChI7bUe5u0U5GM29aWOdR1TwWVZLc6q_0WMlyqnt6bb0Wm4BLjhVyeLfsldTaKPVIlu', start_index=11871)
Annotation(end_index=11885, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdKc-limseGotMQNUG5jAh8YW5si0avpvjykBkHgV21zkfmv4AvqEiDhS-JO8U99yYOkXExh3P988BH77l7bcsfG8kyspZcT2nsjfkGGsW89sHLxIqRQvNUCfxnAmPng==', start_index=11871)
Annotation(end_index=12064, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPcjeTmEIiX8NUnUvs6T5wHJtEs1bdpXUsut2nLAPmL6mij0EFUxJ1xghTupzWdOZ-FT7-a1Mqg0C6o913aqHYbKRof6JXEwSnJWyYTLnEPoRaSbm1OWmvpKefJKtGDzx_yZbdHuyh', start_index=12054)
Annotation(end_index=12542, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHd1okHvLSa7Iz9dTopn-efUWi1b971tDTR-dlEJFYN39_3drr-fN7MQh0MsZt_yyxjSAU44-1Tl1WZmb8X821O8Nts5ijfnV3g6zP3sMEbL2Rk2v9MWRPw7C9hjIvLUKLYyRNbCM_m6oYoSxplvK7', start_index=12524)
Annotation(end_index=12542, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1PaUl9MOoz5AzoGWsRwomcMtwUvVjRTPrlixlM7bdXJH8XidpGZ-MFIutZhY35zhNELABT7r-aPJ1TqERgvrrQgez-_vC0LQY4WBeKl3Eo3OVRvwpALK8ijMfuM9LrA==', start_index=12524)
Annotation(end_index=12542, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuFxXaCmN-oxapjzRb4rKaYGs2ezk3f0AuQNYYkS_g8c4v5nSQEgjBnGOFU17pKqWhXszv3jbqe-Usu0pLvhU9AF1H-rNIzwGSeT8TvuSOorOpDqTMwPt6pEN49RReuA==', start_index=12524)
Annotation(end_index=12795, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkP9np56kJ-8wNoALtgGT1uFO_siF2Jj9iEkiqLIuFV6HdtpY34ZRBtIWHNCikOFAXMIw3w5pfpGjldlGqUJcpFzcpxFarV4goZ4VGXpkQ3-CdOrkLrIb3kD8ZuzrRQw==', start_index=12781)
Annotation(end_index=12795, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG06q0YvMDmtnew4cZaiR5lAH29PJQjUIPCHhFRP56cg8V_VNdLy-z9ujdn7qGI8dH0KRYR7EwsOJ5WqMJrOftJoRnUdQo0mtmBtyAs0F0JWRs5OwUCuQ7PyqrrvRSrAmTM10Og', start_index=12781)
Annotation(end_index=13463, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElBwW2vRSJ5vTsB-UyBIr2r9EsLRujeEjn9M1380PMKr0iULCjl7Y8qV_FSYPHeRAkjSpbiy4mZtVozPcUmxhxR4LJZ1iyMIowRroVm0rFUvpiKY5A8yls1WOSu38Ouc6-MYI=', start_index=13445)
Annotation(end_index=13463, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL3gY7V1EBPxfQizVnxb3HzcNCmZXj0VRMCan9lGny7dTmWLzg7FhJI6UVUFwb0wVxGYQXBUwS3sJu9uHzBjfGx9aD6LsPosRKR53_8CnzJqy5Xu4NX8NfpY-cKKEI3IjZXO5xN6yzrHjLzl78uS096mI-J2SprWtxDeCo4T39WkWsbdTDfeHJheVpCzimn30ryK96zGPX9pbuHg1cFRwQ2EVdm6kEYQ==', start_index=13445)
Annotation(end_index=13463, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjpOFJHzKgMqP5LVFEJXQp5DS6Keq9Comqcbu9EUI8WZjI69lRCt9C1SbxTlVMZGe-IzhPxQmdtnRwCxxutktFa3S-AwVC4hVL_i5hccXACsmw-5tm6wbm1Cldy8cfFA==', start_index=13445)
Annotation(end_index=13553, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL3gY7V1EBPxfQizVnxb3HzcNCmZXj0VRMCan9lGny7dTmWLzg7FhJI6UVUFwb0wVxGYQXBUwS3sJu9uHzBjfGx9aD6LsPosRKR53_8CnzJqy5Xu4NX8NfpY-cKKEI3IjZXO5xN6yzrHjLzl78uS096mI-J2SprWtxDeCo4T39WkWsbdTDfeHJheVpCzimn30ryK96zGPX9pbuHg1cFRwQ2EVdm6kEYQ==', start_index=13539)
Annotation(end_index=13553, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPZc3QEl1ewDpMMF6jWnpTqeJm95jAYRFibjNLGjzm7uBMgdEr47ygJeEYsfyti1BGFSIT-0FlhgZiKPTtdSjtYiIfJDuwl73qyDFvxPmF9NiY76Yfm15bsVVuCGMyD0QSnIvbyapL', start_index=13539)
Annotation(end_index=13795, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_dATi7ImTI0Zx7GfsuyGBJA8DwOe2VidB-0A_KZBNGGO6xppe1eKZ6SCB2e_x6dx2d5A7Rs17JAnr2WkouQS-YvTnY2-MROdTb3g3f2fojCpaenppe-sqWrPoX5MMU6vlKajnsuDn', start_index=13778)
Annotation(end_index=13795, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhv3o3a5ifcoCA3f1UhyThb5qWnHJ-TOXtahey3ieI0T_DaAKRqQrAkOJfqdTLVexXAkN4plWa-L33djr7S4HnLQ4oJWwfve5uz2NpgsZQlVoXJr2FMrUozwyOIeEOKQ==', start_index=13778)
Annotation(end_index=13795, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMogUPj6gwqJXgf0ChZ3Ab8jPBEJFX9cx-gZ_P7IPdN5f44bCKeMajVk5kHqWl0UTQ2ca8AGp6-eyO1K1mB06cqxbBw02mcikaH6y4T9AEHDiu9wZRIO4c1KMygjmP202gf6KXbL4oYihUsWuUHxozCJqV2-zqyQRLL4jeeA25QU6EVF8LK2R2-3qorhhSY1tr1QrdU57OL2DZ0rzg', start_index=13778)
Annotation(end_index=14102, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7d_eka8KWLaka_TkHcHtPkdWZ1zvGGPZgog62O-ZU3dKR6YnD4u6QNFwS4ZBwdv5U9GTp3k2e1E3VtFKq3iQTW6BS-CJqpD6qzJAZJA2CDEvAP33NCTJfchWAJ0ACZC18VzIRRwId', start_index=14089)
Annotation(end_index=14102, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcYtti7fH9kyvK7GJHJHsSEV2PgYjN1vDaxPi7tEH_PfQZQJTi58QPhOsW0y5dnR6SgW98NBFuhW2WVkiMR9I6kp0ZmAOFi4QQmPnqvO98FLurQ1zNAmlKvwAmMqqKD0OOrdhRghJC', start_index=14089)
Annotation(end_index=14395, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_dATi7ImTI0Zx7GfsuyGBJA8DwOe2VidB-0A_KZBNGGO6xppe1eKZ6SCB2e_x6dx2d5A7Rs17JAnr2WkouQS-YvTnY2-MROdTb3g3f2fojCpaenppe-sqWrPoX5MMU6vlKajnsuDn', start_index=14386)
Annotation(end_index=14651, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHiJnmRIagUZF-nVj8wWG2EfyNbTltoWnHcEAiWtIrUw1EVG2zWBXoDXodecmDkSApY-0W93GtM6qEObQqtX7IC7a8pCRHr3MhO5mAjRCQS45O9IZKf8gjKY4TxlA77Ag==', start_index=14637)
Annotation(end_index=14651, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkuhznw3w05Yed-6p_IiPyJwTGzzO4Sjr1Bv92gPBkH3fWJ4xPSuEzLlbVK2KvjHQsXrtiR1N1z6rot6Y_d2VzRe6kdc6mjA7Tym9PFW5H0cbxG-XkWgrBZbRlZPKzqQ==', start_index=14637)
Annotation(end_index=14743, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkuhznw3w05Yed-6p_IiPyJwTGzzO4Sjr1Bv92gPBkH3fWJ4xPSuEzLlbVK2KvjHQsXrtiR1N1z6rot6Y_d2VzRe6kdc6mjA7Tym9PFW5H0cbxG-XkWgrBZbRlZPKzqQ==', start_index=14733)
Annotation(end_index=14894, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJdSTPBn220duejecSs07CEHERedpmbeg0xYynzYd493yYkmCBZhtV06P3TOL0WmJiqelEFQW9BjkkcxL5k8qnjNCkUDSktD7urpz6RoSRxo9ykcvTAR_QBsXqBgg55M8UXyffRsIG2SNz6oLSwL33hYHpO50vMDGQI_gmoJdojPdA', start_index=14880)
Annotation(end_index=14894, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQA12AdvbDs6Kp8ej5Bj9ewNIH1g6PgZJw_-6Y-trPqcTMa95W9VVdwBsbQIRLynL6OnZ408P3NC9A0D-RM4mw0fJl99RL8FwNmcVIk7UU9ErjXJrqKSz54P8f3b-BSzovIytImiCK6OgJlkR1lzCdk3yoGOtgJxCSLoHtgUnW47RWvYlya1QNpJSgESrN_KYMOO5Pf8AzvhwX1sS_vaAWy-5uzr1kYhrc3av9dRfH9WV7Tpnnl4NKvsR1HJl5s7fpYPjbWqijLc53wkzGHX4wwYITCtbHS1h4', start_index=14880)
Annotation(end_index=15542, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEf31DxgXE8l2IRLA5Brya1cD5g12ZXEljsQ_wRQ5jyT_mBYKiOeQBmzf7iNOFaG9mbblDQwrRx0BZrokUJaXjo4btW3vfeFyTV29uzqRE-SbewhVH9wt1NhjsHfvtQ', start_index=15525)
Annotation(end_index=15542, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIUJYZ7mH3JhZjTtYSMY5vd3OMWuSIbhbGWRpXToWQyNuQuyeds1uw8zHuDZyhbhyvuU51BW2ciWSwUpNimWq3jQ-KtbqkLiWsh9SCaZTkoFUoQ-gKJ68dV4WZfSbArISkthBTHxdm3A==', start_index=15525)
Annotation(end_index=15542, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDv2OHmJQgM_0CEQzz6Gpb-evx3bc1TwRZq8U_lYZGwdUGniScGZ3zADmmKQqn7mfF7Emq2MkeCTxDktvKJzwHdv7cCVMXOxl9Ho7Do2ENxbFgb143PW4Oa8ix_jAppQFx9RBlCu0lFElAVziEDgKYc8z0jlbor6aYQCq3mrIETrm5thw=', start_index=15525)
Annotation(end_index=15886, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERECx7RzpsPGHfyV4xghPgTtinYnXsdpBF0_B7nPIMcgXEZ4BQpbjeP-o7ztckRs3gLCtsJOz6go7ABEJNvEPimmtg7LH0Ypc24JuERGQRX22fXHy_xKYxLIKvwv7iBz_yzrfTmBSe', start_index=15873)
Annotation(end_index=15886, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDv2OHmJQgM_0CEQzz6Gpb-evx3bc1TwRZq8U_lYZGwdUGniScGZ3zADmmKQqn7mfF7Emq2MkeCTxDktvKJzwHdv7cCVMXOxl9Ho7Do2ENxbFgb143PW4Oa8ix_jAppQFx9RBlCu0lFElAVziEDgKYc8z0jlbor6aYQCq3mrIETrm5thw=', start_index=15873)
Annotation(end_index=16083, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoXFoD_0JcW1vxcYJt8o4vaW85P1JkVR4zWzMMz-uc4-VrVwmJCQoJvwRxwuTjUBJXTe5-6vw7PCJ6LsB4LF7_FX_A2qnVcJmc0THJ-CQQ21amhy3Ox_XGzC_3tsDWZ1C4Xc5aL7cu', start_index=16069)
Annotation(end_index=16083, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdiO4RJcXea0rC5vd9k_n70hYeywgyk8T4WPXMUzxstsZEMJPtKJg_SDL0Pezj0VOjVIOgqwecCVYs6qmwDIz5nm_AwFT3GRv__Fqs26ndDV_FUQBYKSOxWC28TRZdzw==', start_index=16069)
Annotation(end_index=16319, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoXFoD_0JcW1vxcYJt8o4vaW85P1JkVR4zWzMMz-uc4-VrVwmJCQoJvwRxwuTjUBJXTe5-6vw7PCJ6LsB4LF7_FX_A2qnVcJmc0THJ-CQQ21amhy3Ox_XGzC_3tsDWZ1C4Xc5aL7cu', start_index=16305)
Annotation(end_index=16319, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdiO4RJcXea0rC5vd9k_n70hYeywgyk8T4WPXMUzxstsZEMJPtKJg_SDL0Pezj0VOjVIOgqwecCVYs6qmwDIz5nm_AwFT3GRv__Fqs26ndDV_FUQBYKSOxWC28TRZdzw==', start_index=16305)
Annotation(end_index=16502, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdiO4RJcXea0rC5vd9k_n70hYeywgyk8T4WPXMUzxstsZEMJPtKJg_SDL0Pezj0VOjVIOgqwecCVYs6qmwDIz5nm_AwFT3GRv__Fqs26ndDV_FUQBYKSOxWC28TRZdzw==', start_index=16492)
Annotation(end_index=17456, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE09iaEuRkHjLONx-IXueyvxzlvWW1KcXgl_WlnAN3eIAVHJbgOWgQmisbBKd60Kgncpow2wu-cN69ehuYDKETZvRJ9HkUO3JoyQksH4MZckv_Jw7mW62NHKSE8zABsZQrFcwNQor3Bz7ETgztk9LtDRMAwsKvuNETdecAcn6kwk0PVKbV6cKafpND_mVFasnNXRA_xiMin6Q==', start_index=17433)
Annotation(end_index=17456, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_dATi7ImTI0Zx7GfsuyGBJA8DwOe2VidB-0A_KZBNGGO6xppe1eKZ6SCB2e_x6dx2d5A7Rs17JAnr2WkouQS-YvTnY2-MROdTb3g3f2fojCpaenppe-sqWrPoX5MMU6vlKajnsuDn', start_index=17433)
Annotation(end_index=17456, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhv3o3a5ifcoCA3f1UhyThb5qWnHJ-TOXtahey3ieI0T_DaAKRqQrAkOJfqdTLVexXAkN4plWa-L33djr7S4HnLQ4oJWwfve5uz2NpgsZQlVoXJr2FMrUozwyOIeEOKQ==', start_index=17433)
Annotation(end_index=17456, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjpOFJHzKgMqP5LVFEJXQp5DS6Keq9Comqcbu9EUI8WZjI69lRCt9C1SbxTlVMZGe-IzhPxQmdtnRwCxxutktFa3S-AwVC4hVL_i5hccXACsmw-5tm6wbm1Cldy8cfFA==', start_index=17433)
Annotation(end_index=17456, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHB7pEE6Fp-TjCczTCQ64IxSALyCRFirOS7qdD4uI8mdS63dgRxq90_Rhs2bGZCjLye9b3pj_K6ComnpO9V04IH_xsMjG9fT9BXxP1kxqy9-PIIj8PlcKvP8m4hsbBov4VKcHzlRoiAKvWXEKYKH3dW0Ej4QBbZqB2kS1EooIIRMo8usadTD7m6EZU6XyNhcPe0ax8LJLBOTVGRxWMipqT6JGoqsCJ2DQGjopPon1E=', start_index=17433)
Annotation(end_index=18015, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_dATi7ImTI0Zx7GfsuyGBJA8DwOe2VidB-0A_KZBNGGO6xppe1eKZ6SCB2e_x6dx2d5A7Rs17JAnr2WkouQS-YvTnY2-MROdTb3g3f2fojCpaenppe-sqWrPoX5MMU6vlKajnsuDn', start_index=18002)
Annotation(end_index=18015, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFhv3o3a5ifcoCA3f1UhyThb5qWnHJ-TOXtahey3ieI0T_DaAKRqQrAkOJfqdTLVexXAkN4plWa-L33djr7S4HnLQ4oJWwfve5uz2NpgsZQlVoXJr2FMrUozwyOIeEOKQ==', start_index=18002)
Annotation(end_index=18238, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1PaUl9MOoz5AzoGWsRwomcMtwUvVjRTPrlixlM7bdXJH8XidpGZ-MFIutZhY35zhNELABT7r-aPJ1TqERgvrrQgez-_vC0LQY4WBeKl3Eo3OVRvwpALK8ijMfuM9LrA==', start_index=18224)
Annotation(end_index=18238, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuFxXaCmN-oxapjzRb4rKaYGs2ezk3f0AuQNYYkS_g8c4v5nSQEgjBnGOFU17pKqWhXszv3jbqe-Usu0pLvhU9AF1H-rNIzwGSeT8TvuSOorOpDqTMwPt6pEN49RReuA==', start_index=18224)
Annotation(end_index=18396, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWGDovo0GxU8iSklPWa0wSTIzQFtqlV9DriL3EKQzXM-5Rv1schy8L4I-Kf66HcemRtm3756d6BpHzjVRn2bO3hwccley-LAvCKoy9D8pgrKAjUeHzFdvM7_xI8m_e8Q==', start_index=18382)
Annotation(end_index=18396, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFK46ify518OooAhoXbqh6tMkAmjhXDqRJJSauVt4WUz2O3c4wSMmhiJI65KwbNFNxhDOOZgzJ387qZzbKpdJIYVZbup7fwfnLXbUtDPFfGBxqpkgWm1DjbrHxBcutVA==', start_index=18382)
Annotation(end_index=18799, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7xKiPakGNbPNPR3tG74xEClgK6htL1akcz7_DyO5qsDotj7sD057dqtkbY_GnvB4jViWrpEDf2c-_c1gmEjxyNmGY8u14bbbGy52WLvrgcl739mwYlP52RzfZOSqgcC1HMzKFVfZbw0ZSpk3Q8tVXjxyZTql2HtyZAmJ6cNN9tTeN_eICQb3Zi_5p9wxFcqHJYHtOlWJuAnWaIZAtvwKmnOc61iUvrobK-6ypQu7AVFHwAdBYh5iVW_YBxyTFP933jIk0B7jJwijVxDYE-P5KTYXaPtTBGZSOHvt0087O5V1SSrY3LQ==', start_index=18785)
Annotation(end_index=18799, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGX6h_ersKiKyYdRwMzkLGm77avR51xAKNfDAwqooy7q4CkHXeEQUpF_I1pTZ2ZNxXK6CWXldEb2CQUgNDIkiXGKj51CvXKJQ0iNP0u3QKbfGDQg7BRDDlypWA20oK57Jv-5NS1KC9Z', start_index=18785)

## Sources
