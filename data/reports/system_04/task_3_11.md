# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 542c229d | **Time:** 327.57s | **Cost:** $1.59835
--------------------------------------------------------------------------------

# Balancing Anti-Inflammatory Efficacy and Adrenal Suppression in Glucocorticoid Research

### Key Points
*   **The Fundamental Trade-off:** Glucocorticoids (GCs) are potent anti-inflammatory agents, but their use is strictly limited by the risk of Glucocorticoid-Induced Adrenal Insufficiency (GIAI). The balance is currently managed clinically through dose minimization and duration limits, with a threshold for HPA axis suppression generally identified as doses exceeding 4–5 mg of prednisone equivalent for longer than 3–4 weeks.
*   **Mechanism of Action vs. Side Effects:** The "dissociation hypothesis" suggests that anti-inflammatory effects are primarily mediated by **transrepression** (inhibiting pro-inflammatory transcription factors like NF-κB), while metabolic side effects arise from **transactivation** (direct DNA binding to upregulate genes).
*   **The HPA Suppression Paradox:** Research indicates that HPA axis suppression (specifically the repression of the POMC gene in the pituitary) is mediated by mechanisms similar to anti-inflammatory transrepression (e.g., nGREs or tethering). Consequently, novel "dissociated" agonists (SEGRAs) that preserve anti-inflammatory efficacy often fail to spare the adrenal axis, despite reducing other metabolic side effects like hyperglycemia.
*   **Clinical Management:** Current strategies to balance these factors rely on mimicking circadian rhythms (chronotherapy), utilizing alternative delivery routes (e.g., inhaled ciclesonide), and adhering to strict tapering regimens to allow HPA axis recovery, which can take 6–12 months after cessation of long-term therapy.

### Introduction
Glucocorticoids (GCs) remain the cornerstone of anti-inflammatory and immunosuppressive therapy, utilized in approximately 1% of the general population and up to 3% of older adults [cite: 1, 2]. Their efficacy in conditions ranging from asthma and rheumatoid arthritis to autoimmune disorders is unparalleled. However, their therapeutic window is constrained by a plethora of adverse effects, the most insidious of which is the suppression of the Hypothalamic-Pituitary-Adrenal (HPA) axis. This suppression leads to secondary adrenal insufficiency, a condition where the adrenal glands atrophy and fail to produce sufficient cortisol upon the withdrawal of exogenous steroids, potentially leading to life-threatening adrenal crises [cite: 1, 3].

The central challenge in glucocorticoid research is balancing the dose-dependent anti-inflammatory benefits with the risk of HPA axis suppression. This report examines the physiological thresholds of suppression, the molecular mechanisms that couple efficacy with adrenal toxicity, and the pharmacological and clinical strategies employed to mitigate this risk.

## Physiological Basis of Glucocorticoid Action and HPA Axis Regulation

To understand the balance between therapy and toxicity, one must first establish the physiological baseline of endogenous glucocorticoid production and regulation.

### Endogenous Cortisol Production
Cortisol is synthesized in the zona fasciculata of the adrenal cortex under the control of Adrenocorticotropic Hormone (ACTH). Historically, cortisol production rates were overestimated, leading to excessive replacement doses. Modern stable isotope dilution methods estimate the daily cortisol production rate (DCPR) to be approximately **5–10 mg/m²/day**, or roughly **15–20 mg/day** for an average adult [cite: 4, 5].

This physiological production follows a distinct circadian rhythm, peaking between 02:00 and 08:00 and reaching a nadir around midnight [cite: 5, 6]. This rhythmicity is critical for homeostasis and is the primary target disrupted by exogenous therapy.

### The Negative Feedback Loop
The HPA axis operates via a tightly regulated negative feedback loop:
1.  **Hypothalamus:** Secretes Corticotropin-Releasing Hormone (CRH).
2.  **Pituitary:** CRH stimulates the anterior pituitary to synthesize Pro-opiomelanocortin (POMC), which is processed into ACTH [cite: 7].
3.  **Adrenal Gland:** ACTH stimulates the adrenal cortex to release cortisol.
4.  **Feedback:** Elevated cortisol (or exogenous GCs) binds to Glucocorticoid Receptors (GR) in the hypothalamus and pituitary, inhibiting the synthesis and release of CRH and POMC/ACTH [cite: 8, 9].

Exogenous GCs mimic this feedback signal. When administered at supraphysiological doses or for prolonged periods, they cause a profound and sustained inhibition of CRH and ACTH. Without ACTH stimulation, the adrenal cortex undergoes atrophy, losing the enzymatic capacity to produce cortisol [cite: 2, 8].

## Clinical Thresholds for Adrenal Suppression

The risk of adrenal suppression is inextricably linked to the dose and duration of glucocorticoid therapy. Recent guidelines have attempted to quantify the "tipping point" where the anti-inflammatory benefit is outweighed by the risk of HPA axis collapse.

### Dose-Duration Thresholds
According to the 2024 Joint Clinical Guideline by the European Society of Endocrinology and the Endocrine Society, the risk of adrenal insufficiency becomes significant when exposure exceeds specific thresholds [cite: 1].

**Table 1: Thresholds for Risk of Glucocorticoid-Induced Adrenal Insufficiency (GIAI)**

| Parameter | High Risk Threshold | Low Risk / Physiological Equivalent |
| :--- | :--- | :--- |
| **Duration** | > 3–4 weeks | < 2–3 weeks (short courses) |
| **Prednisone Dose** | > 5 mg/day | < 5 mg/day |
| **Hydrocortisone Dose** | > 20–30 mg/day | 15–25 mg/day |
| **Dexamethasone Dose** | > 0.5 mg/day | < 0.25–0.5 mg/day |
| **Route** | Oral, Intra-articular (high dose) | Topical (limited), Intranasal |

*Data synthesized from [cite: 1, 10].*

The guideline states that any dose greater than the daily hydrocortisone equivalent of **15–25 mg** (approx. 4–6 mg prednisone) administered for **3–4 weeks or longer** poses a risk for adrenal insufficiency [cite: 1]. Conversely, patients treated for less than 3 weeks, or those on physiological replacement doses, are generally considered at low risk for suppression, although individual susceptibility varies significantly [cite: 1, 11].

### Individual Variability
There is substantial inter-individual variability in susceptibility to adrenal suppression. Factors influencing this include:
*   **Metabolism:** Variations in liver enzymes (e.g., CYP3A4) affecting GC clearance.
*   **GR Sensitivity:** Polymorphisms in the *NR3C1* gene affecting receptor sensitivity [cite: 10, 12].
*   **Timing of Administration:** Evening doses suppress the early morning ACTH surge more profoundly than morning doses, increasing the risk of adrenal atrophy [cite: 11, 13].

## Molecular Mechanisms: The Balance of Transactivation and Transrepression

The "Holy Grail" of glucocorticoid research has been to separate the beneficial anti-inflammatory effects from the deleterious side effects. This pursuit is grounded in the hypothesis that these effects are mediated by distinct molecular mechanisms.

### The Classical Model
The Glucocorticoid Receptor (GR) is a ligand-activated transcription factor. Upon binding a GC, the GR translocates to the nucleus and modulates gene expression via two primary modes:

1.  **Transactivation (Genomic):** The GR homodimerizes and binds directly to specific DNA sequences called Glucocorticoid Response Elements (GREs) in the promoters of target genes. This upregulates genes involved in gluconeogenesis (e.g., *TAT*, *PEPCK*) and other metabolic processes. This mechanism is historically associated with metabolic side effects like hyperglycemia, diabetes, and skin atrophy [cite: 14, 15, 16].

2.  **Transrepression (Tethering):** The GR (often as a monomer) interacts with other DNA-bound transcription factors, such as NF-κB and AP-1, without binding directly to DNA. This interaction prevents these factors from upregulating pro-inflammatory genes (e.g., cytokines, COX-2). This mechanism is widely believed to mediate the primary anti-inflammatory effects of GCs [cite: 14, 16, 17, 18].

### The Dissociation Hypothesis
Based on the classical model, researchers hypothesized that "dissociated" steroids—Selective Glucocorticoid Receptor Agonists (SEGRAs)—could be designed to favor transrepression (anti-inflammatory) while minimizing transactivation (side effects) [cite: 17, 19, 20].

Compounds like **ZK 216348** and **Compound A** were developed to test this. In preclinical models, these compounds successfully inhibited inflammation (via NF-κB repression) with reduced impact on blood glucose and skin thickness (transactivation-dependent effects) [cite: 21, 22].

### The Failure to Spare the HPA Axis
Despite the success in reducing metabolic side effects, SEGRAs have largely failed to eliminate the risk of adrenal suppression. Research indicates that the suppression of the HPA axis—specifically the repression of the *POMC* gene in the pituitary—is mechanistically similar to the anti-inflammatory pathway.

#### Mechanisms of POMC Repression
The repression of the *POMC* gene (which encodes ACTH) does not follow the simple transactivation model. Instead, it involves mechanisms that overlap with transrepression:

1.  **Negative GREs (nGREs):** The GR binds to specific negative response elements (nGREs) on the *POMC* promoter. Unlike positive GREs, nGREs may recruit corepressors (like NCoR/SMRT) or prevent the binding of other transcription factors [cite: 23, 24, 25, 26].
2.  **Tethering/Interference:** GR may tether to or interfere with the orphan nuclear receptor **Nur77** (also known as NGFI-B), which is required for *POMC* transcription. This mechanism is analogous to the tethering of GR to NF-κB to suppress inflammation [cite: 27].

Because HPA axis suppression relies on nGREs and tethering—the very mechanisms utilized for anti-inflammatory efficacy—it is inherently difficult to dissociate the two. Studies on the dissociated agonist ZK 216348 showed that while it spared the spleen and skin, it suppressed ACTH levels just as potently as prednisolone [cite: 21]. This suggests that **adrenal suppression is mechanistically linked to the anti-inflammatory potency of the drug** [cite: 12, 21].

## Strategies to Balance Efficacy and Adrenal Risk

Given the molecular difficulty in separating efficacy from HPA suppression, clinical and pharmacological strategies focus on management and mitigation.

### 1. Tapering and Withdrawal Protocols
The most common clinical strategy to balance risk is the careful management of withdrawal.
*   **Short Courses:** For therapies lasting <3 weeks, abrupt cessation is generally safe as the HPA axis has not fully atrophied [cite: 1, 11].
*   **Long Courses:** For chronic therapy, tapering is essential. The 2024 guidelines recommend tapering to a physiological dose (e.g., 4–6 mg prednisone) to control the underlying disease, followed by a slower wean to allow adrenal recovery [cite: 1].
*   **Recovery Timeline:** Recovery is slow. Even after biochemical normalization, the adrenal reserve may remain impaired for 6–12 months, necessitating "stress dose" coverage during illness or surgery [cite: 1, 11, 28].

### 2. Chronotherapy
Timing administration to mimic the body's natural rhythm can minimize suppression.
*   **Morning Dosing:** Administering intermediate-acting GCs (like prednisone) as a single morning dose coincides with the natural cortisol peak. This avoids high GC levels during the nocturnal nadir, allowing for some recovery of the ACTH surge in the early morning [cite: 5, 13, 29].
*   **Evening Dosing:** Conversely, evening doses or split doses obliterate the nocturnal nadir and the morning ACTH surge, resulting in significantly profounder adrenal suppression [cite: 11, 13].

### 3. Alternative Delivery Systems
Minimizing systemic exposure is a key strategy.
*   **Inhaled/Topical GCs:** While safer, high doses of inhaled corticosteroids (ICS) can still cause suppression. The liver's "first-pass" metabolism is crucial here.
*   **Ciclesonide:** This is a prodrug activated by esterases in the lung. It has high protein binding and rapid clearance if it enters systemic circulation, theoretically reducing the risk of HPA suppression compared to older ICS like fluticasone [cite: 2].

### 4. Selective Glucocorticoid Receptor Agonists (SEGRAs)
While SEGRAs like **Velsecorat** and **Mapracorat** have shown promise in separating metabolic side effects (diabetes, osteoporosis) from anti-inflammatory effects, they have not solved the adrenal suppression problem. The shared mechanism (transrepression/nGRE) means that any agent potent enough to repress cytokines via GR will likely repress ACTH via GR [cite: 12, 21, 30].

## Conclusion

The balance between anti-inflammatory dose-dependence and the risk of adrenal suppression is defined by a rigid physiological reality: the molecular machinery that silences inflammation (transrepression of cytokines) is perilously similar to the machinery that silences the HPA axis (repression of *POMC*).

Current research suggests that a "perfect" glucocorticoid that completely spares the adrenal gland while maintaining full anti-inflammatory potency may be biologically impossible via the GR pathway alone. Therefore, the "balance" is currently achieved not by molecular dissociation, but by clinical precision: using the lowest effective dose, adhering to circadian-aligned dosing schedules, and managing the inevitable suppression through vigilant tapering and stress-dose coverage.

## Detailed Analysis of Research Findings

### Section 1: Glucocorticoid Usage and the Burden of Adrenal Insufficiency

Glucocorticoids are among the most widely prescribed medications worldwide. It is estimated that **1% to 3%** of the adult population utilizes chronic glucocorticoid therapy for conditions such as rheumatoid arthritis, polymyalgia rheumatica, inflammatory bowel disease, and asthma [cite: 1, 2, 10].

While these drugs are life-saving, their use comes at a high cost. The suppression of the HPA axis is an inevitable consequence of chronic therapy. A systematic review indicated that the absolute risk of developing adrenal insufficiency in patients taking oral glucocorticoids is approximately **48.7%** [cite: 10, 31]. This prevalence highlights the critical need to understand the boundaries of safe dosing.

#### The Spectrum of Suppression
Adrenal suppression is not binary; it exists on a spectrum.
1.  **Biochemical Suppression:** The HPA axis is dampened, and basal cortisol levels may be low, but the patient is asymptomatic under normal conditions.
2.  **Clinical Adrenal Insufficiency:** The adrenal glands cannot mount a sufficient cortisol response to stress (surgery, infection), leading to adrenal crisis (hypotension, shock, death) [cite: 3, 32].

The risk is highest with oral and intra-articular administration (52%) and lower, though not negligible, with inhaled (7.8%), topical (4.7%), and nasal (4.2%) formulations [cite: 10].

### Section 2: Defining the Physiological and Supraphysiological Dose

To balance efficacy with risk, one must define the "physiological" baseline. If a therapeutic dose does not exceed the body's natural output, the risk of suppression is theoretically minimized (though not eliminated due to pharmacokinetic differences).

#### Daily Cortisol Production Rate (DCPR)
Historical estimates of cortisol production were high, leading to replacement doses of 30 mg hydrocortisone or more. Modern techniques using stable isotope dilution/mass spectrometry have revised this figure downward.
*   **Mean DCPR:** Approximately **5–10 mg/m²/day** [cite: 4, 33].
*   **Adult Equivalent:** For an average adult (1.7 m²), this equates to roughly **9.9 mg/day** (± 2.7 mg) to **15–20 mg/day** [cite: 4, 5, 10].

#### Equivalence Table
Understanding potency is vital for calculating risk. The following equivalencies are generally accepted [cite: 1, 6, 33]:

| Glucocorticoid | Anti-inflammatory Potency | Equivalent Dose (mg) | Duration of Action |
| :--- | :--- | :--- | :--- |
| **Hydrocortisone** | 1 | 20 | Short (8–12h) |
| **Prednisone** | 4 | 5 | Intermediate (12–36h) |
| **Prednisolone** | 4 | 5 | Intermediate (12–36h) |
| **Methylprednisolone** | 5 | 4 | Intermediate (12–36h) |
| **Dexamethasone** | 25 | 0.75 | Long (36–72h) |

**Key Insight:** A dose of **5 mg prednisone** is roughly equivalent to the body's daily output. Doses exceeding this are considered supraphysiological and, if maintained, will activate negative feedback loops to suppress endogenous production [cite: 10].

### Section 3: The Molecular Mechanisms of Action

The glucocorticoid receptor (GR) is the mediator of both efficacy and toxicity. Encoded by the *NR3C1* gene, the GR resides in the cytoplasm bound to heat shock proteins (Hsp90, Hsp70). Upon ligand binding, it dissociates and translocates to the nucleus [cite: 2, 18].

#### Transactivation (The "Side Effect" Pathway)
In this mode, GR homodimers bind to Glucocorticoid Response Elements (GREs) on DNA.
*   **Mechanism:** Direct DNA binding -> Recruitment of coactivators -> Gene transcription.
*   **Targets:** Genes involved in gluconeogenesis (*PEPCK*), protein catabolism, and lipolysis.
*   **Consequence:** This pathway is largely responsible for metabolic adverse effects: diabetes, muscle wasting, and skin atrophy [cite: 14, 16, 20].

#### Transrepression (The "Anti-Inflammatory" Pathway)
In this mode, the GR interferes with other transcription factors.
*   **Mechanism:** The GR (often monomeric) physically interacts with ("tethers" to) pro-inflammatory transcription factors like **NF-κB** and **AP-1**.
*   **Effect:** It prevents these factors from binding to DNA or recruiting coactivators (like CBP/p300), effectively silencing pro-inflammatory genes (cytokines, COX-2) [cite: 17, 18, 34].
*   **Consequence:** This is the primary mechanism for the anti-inflammatory effect.

#### The "Dissociation" Concept
The distinct nature of these two pathways led to the development of **Selective Glucocorticoid Receptor Agonists (SEGRAs)**. The goal was to create ligands that induce the conformational change required for tethering (transrepression) but *not* the conformational change required for dimerization and DNA binding (transactivation) [cite: 17, 19].
*   **Example:** **Compound A** and **ZK 216348**. These compounds showed reduced diabetic and atrophic effects in mice while maintaining anti-inflammatory efficacy [cite: 21, 22].

### Section 4: The Mechanism of HPA Axis Suppression

If SEGRAs can separate inflammation from diabetes, can they separate inflammation from adrenal suppression? The evidence suggests **no**.

#### The POMC Promoter
The suppression of ACTH is driven by the repression of the *Pro-opiomelanocortin* (*POMC*) gene in the anterior pituitary. This repression is mediated by the GR, but the mechanism is complex and debated.

1.  **The nGRE Model:** Early research identified a "negative GRE" (nGRE) in the *POMC* promoter. The GR binds to this sequence (an inverted repeat) and recruits corepressors (NCoR/SMRT) to silence the gene [cite: 23, 24, 25, 26].
2.  **The Tethering Model:** Other research suggests that GR repression of *POMC* involves tethering to the orphan nuclear receptor **Nur77** (NGFI-B). Nur77 is a potent activator of *POMC*; GR binds to Nur77 and inhibits its activity, similar to how it inhibits NF-κB [cite: 27].

#### The Implication for "Balance"
Both the nGRE and tethering mechanisms share structural similarities with the anti-inflammatory transrepression pathway.
*   **Study Evidence:** The dissociated agonist **ZK 216348** was tested in mice. It successfully dissociated anti-inflammatory effects from skin atrophy and spleen involution. However, **ACTH suppression was similar for both ZK 216348 and prednisolone** [cite: 21].
*   **Conclusion:** The structural requirements for GR to repress *POMC* (and thus suppress the adrenal gland) are likely the same requirements for GR to repress inflammatory cytokines. Therefore, **adrenal suppression tracks with anti-inflammatory potency**, making it difficult to engineer out of the molecule [cite: 12].

### Section 5: Clinical Management of the Balance

Since pharmacological dissociation of adrenal risk is currently elusive, clinical management strategies are paramount.

#### 1. Dose and Duration Limits
The 2024 Guidelines provide clear cutoffs for risk stratification [cite: 1]:
*   **Safe Zone:** < 3 weeks duration. In these cases, GCs can usually be stopped without tapering because the adrenal cortex has not significantly atrophied.
*   **Danger Zone:** > 3–4 weeks at > 5 mg prednisone. Tapering is mandatory.

#### 2. Tapering Regimens
Tapering serves two purposes: preventing disease flare (recrudescence) and allowing HPA recovery.
*   **Rapid Taper:** Down to physiological levels (5–7.5 mg prednisone).
*   **Slow Taper:** Once at physiological levels, the taper must slow down (e.g., 1 mg reduction per month) to force the HPA axis to wake up.
*   **Testing:** A morning cortisol test can guide cessation. If cortisol is > 10 μg/dL (> 300 nmol/L), the axis has likely recovered [cite: 1, 8].

#### 3. Chronotherapy (Circadian Dosing)
The timing of the dose profoundly affects the "balance."
*   **Mechanism:** The HPA axis is driven by a morning surge of ACTH.
*   **Strategy:** Giving the total daily dose in the **morning** exposes tissues to GCs when endogenous levels would naturally be high, and allows levels to fall by nighttime. This nocturnal "washout" period permits the pituitary to secrete ACTH in the early morning, maintaining some adrenal trophic function [cite: 13, 29].
*   **Risk:** Split doses (e.g., bid or tid) or evening doses maintain high GC levels 24/7, completely blocking ACTH release and accelerating adrenal atrophy [cite: 11, 13].

#### 4. Route of Administration
*   **Inhaled Corticosteroids (ICS):** Used for asthma. Older drugs like fluticasone have high lipophilicity and can be absorbed systemically, causing suppression at high doses.
*   **Newer Agents:** **Ciclesonide** is a prodrug activated only in the lung epithelium. It has very low oral bioavailability and high protein binding, significantly reducing the risk of systemic HPA suppression compared to other ICS [cite: 2].

### Section 6: Future Directions

The search for a "safer steroid" continues. While SEGRAs have not solved the adrenal suppression issue, they offer hope for reducing other comorbidities like steroid-induced diabetes and osteoporosis.
*   **Velsecorat:** A non-steroidal SGRM currently in trials for asthma. It shows potent anti-inflammatory efficacy with a reduced side-effect profile, though its impact on the HPA axis remains a critical endpoint to watch [cite: 30].
*   **Biomarkers:** Future research aims to identify biomarkers for glucocorticoid sensitivity. Since sensitivity varies widely (some patients suppress at low doses, others do not), personalized dosing could optimize the balance for individual patients [cite: 35].

### Summary Table: Balancing Factors

| Factor | Increases Anti-Inflammatory Efficacy | Increases Adrenal Suppression Risk | Strategy for Balance |
| :--- | :--- | :--- | :--- |
| **Dose** | Higher Dose | Higher Dose | Use lowest effective dose; taper to physiological levels ASAP. |
| **Duration** | Longer Duration | > 3–4 Weeks | Limit courses to < 2 weeks when possible. |
| **Timing** | Split Dosing (sustained levels) | Evening/Split Dosing | **Single Morning Dose** (spares HPA axis). |
| **Molecule** | High Potency (Dexamethasone) | High Potency | Use shorter-acting agents (Hydrocortisone/Prednisone) for maintenance. |
| **Mechanism** | Transrepression (NF-κB inhibition) | Transrepression/nGRE (POMC inhibition) | **SEGRAs** (spare metabolic effects, but likely *not* adrenal effects). |

### Conclusion
In glucocorticoid research, the balance between anti-inflammatory dose-dependence and the risk of adrenal suppression is constrained by the overlapping molecular mechanisms of *POMC* repression and cytokine repression. While "dissociated" agonists have successfully separated metabolic side effects from efficacy, they have largely failed to spare the HPA axis. Consequently, the balance is currently maintained through clinical vigilance: adhering to physiological dosing thresholds (~5 mg prednisone), utilizing circadian-based dosing schedules, and implementing rigorous tapering protocols for any therapy extending beyond 3–4 weeks.

## References
[cite: 1] Endocrine Society. (2024). *Guideline: Diagnosis and therapy of glucocorticoid-induced adrenal insufficiency*. [cite: 1]
[cite: 8] JCEM. (2024). *Glucocorticoid taper for patients on long-term glucocorticoid therapy*. [cite: 1, 8]
[cite: 2] NCBI Bookshelf. (2018). *Glucocorticoid Action and Side Effects*. [cite: 2]
[cite: 33] RCH Guidelines. *Adrenal suppression secondary to exogenous glucocorticoids*. [cite: 33]
[cite: 10] MJA. (2023). *Glucocorticoid-induced adrenal suppression: physiological basis and strategies*. [cite: 10]
[cite: 31] PMC. (2023). *Adrenal insufficiency in corticosteroids use: systematic review*. [cite: 10, 31]
[cite: 12] MDPI. (2017). *Individual differences in GC sensitivity*. [cite: 12]
[cite: 9] Endocrinology. (2018). *Glucocorticoids: Restoring Balance During Stress*. [cite: 9]
[cite: 13] Endotext. (2018). *Adrenal Suppression: Timing of administration*. [cite: 11, 13]
[cite: 17] PMC. (2012). *Selective glucocorticoid receptor agonists (SEGRAs)*. [cite: 17, 19]
[cite: 14] PubMed. (2007). *Glucocorticoid receptor: Transactivation vs Transrepression*. [cite: 14, 16]
[cite: 19] Wikipedia. *Selective glucocorticoid receptor modulator*. [cite: 19]
[cite: 11] NCBI. (2018). *Adrenal Suppression: Recovery Timeline*. [cite: 11]
[cite: 1] Endocrine Society. (2024). *Joint Clinical Guideline Announcement*. [cite: 1]
[cite: 15] YouTube/Professor Dave. (2022). *Glucocorticoid Mechanisms*. [cite: 15]
[cite: 34] PMC. (2013). *Binding of glucocorticoid to the GR may repress inflammatory gene transcription*. [cite: 34]
[cite: 21] PNAS. (2003). *Dissociated glucocorticoid ZK 216348*. [cite: 20, 21]
[cite: 16] ResearchGate. (2007). *Separating Transrepression and Transactivation*. [cite: 16]
[cite: 23] PMC. (1993). *Negative glucocorticoid response element (nGRE) of POMC*. [cite: 23, 25]
[cite: 24] NCBI. (2020). *nGREs and Transrepression*. [cite: 24]
[cite: 27] PLOS ONE. (2017). *GR homodimer binds to nGRE of Pomc promoter*. [cite: 27]
[cite: 25] PubMed. (1989). *nGRE in POMC promoter*. [cite: 25]
[cite: 7] Physiology Reviews. (2017). *POMC Processing*. [cite: 7]
[cite: 2] NCBI. (2018). *Ciclesonide and HPA axis*. [cite: 2]
[cite: 3] Medscape. (2024). *Adrenal Crisis Overview*. [cite: 3]
[cite: 28] NIDDK. *Symptoms & Causes of Adrenal Insufficiency*. [cite: 28]
[cite: 1] JCEM. (2024). *Full Guideline: Diagnosis and therapy of glucocorticoid-induced adrenal insufficiency*. [cite: 1]
[cite: 11] NCBI. (2018). *Predictors of Glucocorticoid-Induced HPA Axis Suppression*. [cite: 11]
[cite: 10] MJA. (2023). *Risk factors for adrenal insufficiency*. [cite: 10]
[cite: 4] PMC. (2022). *Daily glucocorticoid replacement dose*. [cite: 4]
[cite: 5] Dr. Oracle. (2025). *Prednisone to Cortisol Conversion*. [cite: 5]
[cite: 6] LITFL. (2022). *Corticosteroids Overview*. [cite: 6]
[cite: 20] PMC. (2003). *ZK 216348 and side effect profile*. [cite: 20]
[cite: 30] ResearchGate. (2020). *Model of GR transactivation and transrepression*. [cite: 30]
[cite: 18] Wikipedia. *Glucocorticoid Receptor Structure*. [cite: 18]
[cite: 26] PMC. (2013). *nGRE mediated transrepression*. [cite: 26]
[cite: 22] Frontiers. (2017). *Compound A and transrepression*. [cite: 22]
[cite: 12] MDPI. (2017). *SEGRAs and Adrenal Insufficiency Risk*. [cite: 12]
[cite: 35] Endocrine Reviews. (2024). *Glucocorticoid Sensitivity and HPA Axis*. [cite: 35]
[cite: 29] Plastic Surgery Key. (2016). *Systemic Glucocorticoids and Chronotherapy*. [cite: 29]

**Sources:**
1. [endocrine.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdbqWvngsOMlNFfHMpwfz8uV_1zKNvM2pqU-mJ5vAhKw2pIkOuuwoc_Aq1Vds2_de4DLsTFiksdIKc1s7dBBVRa-m4otkJq6-6fww2elK31de26Tr5sHQtvACu_kcE9tFaax8N3ciK03pms-BLxVoUJixL4GMak4txctU294K7mlTk_l43FTDj5TWkSOk2ecw91WHGK3TyYw==)
2. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-n5CICFPCJPvbAQK9oR47hCd17H5DeK0iPo57gjO294qQH4WeywqRD6S-AjZBtQBheQNFpVna2XINYRRTcTixGhlCez_fyxzC4lgCYpNKHmnj4oRxreeuSh9AudYW56KSiA==)
3. [medscape.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIyehVZ8diqh7NsvGhHopvzcmFJbM7gBnfzoNXT-3AKXoHQ4Z5CNlq2fH6x-dPLLErKDnimpNQ64ovItcFDigq2gswmQgdNHHXINA0yDMh_hOYh60AY2bultfUkyolGggn6XqrOyIsznNw_w==)
4. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUz25xJYlZ3pyjThXJ8dZD7P0c8_W7HGeAuBlmmd06dcsigxbBNTtaobUoaZDUvck8ImwssnZGsb2_yAPaiWuPEOy26sJVXOd6B_Vhq-rgaKB18mEww2ZPmm1EGDHXUjVSoNfJgRg=)
5. [droracle.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrOLUi9jJPEae5f8KpvjgkaudHyEiFy7d8NYADMI2AuxmmT6iXBSpZY9mTbd8IvsTXZUg88HJc69X9bPBVxr8TGpKBd6nyUe6aovrcqh0K9NDuls5-qVwG-C1Nlq-TgfgM875hVes0_mUbBxqVgIWPwA9UOjYvs1Ho6hD0SOsyHfMzJYncgKHYAVjDf8a9B-Rb)
6. [litfl.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCQASWikPK8qskTyeIrV1g3arBlVxL1npT0Yi1RLIL8_Ohb0suu92pnfbYs9bq1nnC4DFdRO-0CvHER26V4CNXK-5Z2HpEkJuSPmjr1Xx17QJLFVJiX56RbweTJHQa7yM=)
7. [physiology.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVS6OD0MoEqgdZxty8WMrlCOYr8SVbbsg8lAh_nRVBJTH24ieFAzEESrzxV_r_uHd9sCTxQKxEe9oLcnhScHsgO2b2HxweOBrXlGnMzBGwmWl8DdZcCzIeu_3E7Gm25QRdcz1nPaFk_SNm44xMuVNi78ebZZIVaAo=)
8. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExY5duGG9aGFCgtkx9op1-E7cd2qRoUCoAtBpE-ZaqclZT9LjufmZ_fWhpaMikndMxa2e9nEdXnESwkt_dU6ZEMyt-7ADV2sn1ZjvZ_k7vkCoAGVyUfH_si5dRCcf_ZRj0hVgHEE6Vmm71l3ZU)
9. [endocrinology.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCl0bZHYljB2BTv7LFqXTOSdMZqNj_nQ2ZxH8eK0oyH_LkG_o9cS4HWlpY4y9dJq8u8tZqlntjsV0L8D0bcgvKUe1rZv4UqE2KpL8ZClpB06IkpERtjYpQVOuG_1gAnQd-YyqFbJKeOlDOWUUPye-sAjIsYnUb-Hfo8ptnXT0Tn2BGs0gkDO1OTtZ7JkynCmib3pOghd9G9mA8FeMQNMXLPBFQs9ZkLCHy)
10. [mja.com.au](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOaQUAzpJ0PK0gyeqo2Km5dQ2nVYG2NKEZ1-LxWIaoAL6aqPhFPpy91u-2LZCbyeg6RCHhsu7d8RBldhryMLSIpE49GDwgcEqpgkQVwzYSAG_-GQEOHCSLmTdd15xllmVkM_mykmgkZP4nK4zS7IBFDo61jndxzJ-RHOgjyihx5Ux2J7DqHte6z_5u4ODz9hQTKEPXRfHV025F9VvFia8foBEBaCyhF_nk6W51ew==)
11. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHq86Oo9t5pygnE-RJxajrMPtELlWPnHFk-w_bW0ZNk4SJFZVsoHfdy_mdSmCBGptI1OCW1P-QoStt05fC35Lim3dzRdz_OzPG_uRVBakgt3zTdMN1C3Cf2k4OydfLLHJ_iFQ==)
12. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfGvMwp8jTiOIm2IEiMj5zw0hj_HkAdzIWSCPvXCaPpWah_EMMnX0FIQEJq8IE_aZ29_qH_R7XUoDvlMYKq5FrXvfYbRMY_6FKxlYpTILjt7rYPa_bXSBA_Uxem6QV)
13. [endotext.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtaOoLLnQOeh7O4EqritSz0HyOsl3p_y3z4fsZDSbFpBarOePW52aJwcCZ1xcYxrOl_7HbUuaqmadFbkU5L9Ybom_1riHXbqImnPFd3W3Tzy6k1qPkjtrQa5u0i7m9DmHmyVL1C4BTUhyqwAadB-B5EaIVwjQ_Rg-afjHTXg==)
14. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4kNIs99xS7PpdMMgzhKJMBh-WsspZItacynW-nTCtmhdbAC-ttwRLR2MlhxsDrWBK4RFTR1a3IcyahcuHzRWEjIkH125-mGUG_nv_wpVchoThs-EjCh2p1mm1PzBm)
15. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9Mlnj2ZAQzpOzxVDDmmnyI2Bpq_4rERy5uQ82XpYS4chILRDR-ckqbCGLI8kfZxkDOy1h_A7X7xjf6PB_g5hujLU_ZlcFQcFV9Hny626g2qmErD95WXdIL0mIiytI4IE=)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUUYX_v0yAVyr9M3GFNUgjDopf_CfpZ5cwy7fYoiahrCkX41kElFvrCMnf0eHGQ5B6hVkGipfdRm2QbicDcX4N3f6tQiAaCvjFIhHbRRzsSqfgaNJ7LcsgoV9QMUhoPG21mmly_Qehz-qp1wtREKNVZzQl_ifVeNNEmqy3a_bp1NSsXyZDyLRIIyQw79QW_DSvG_TxqFIThGndc5XGsuHDlELcxsa-Uqf-lrctRugnUll89E8oaFTOwQylm6_wVn1wnwHBlg1lDlNrew==)
17. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtyOoDFinTrir1b2TbZj8dbyEogkWIaeopX90mOV7G9HVqhlLEpQXaSjYy7_4lIcz-LKqyvfjz8abZ8xXvOYhZuVVqc2KzBm9psOtYezebkMvINPROyeJsdeGXsfdCE_VH2dGuy94=)
18. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEf7iuq130ZmuwzMMWi6PogS1WwNaXxX4Q7ZT421JDVZ-fz7WRhCIxxW2uVSi6vy_DlLQ-_RNk1Y3y8j1NV0-EIHq4nDFxb6hAq1NHJGpQgegHDNs0c4P1o6eEHddtAO2efdjLO9iMD0SrQ)
19. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFBXE9LwAsyslEYF7tDql_qufbMubk-lYR_lrbZGmnMLW7-IgMNhv-zuwg9WgFQxSJywS24t1u2acIpZ2cX_K--UipKoDXOqbBOKOztlvtdYfU7JWzsENNbQiBNmMlgV31-l6ti7JJrcCme3IvBs9uVBpZvvs7Pn3EvHqZXdg=)
20. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0fI0s_0jmfqnekyQn6VnTjf1j4F0G-uM4QSr2tAazLXppbNRbuLaOOGTjkK5q_vlwXGB5AINknsQ5TdutlMA-GXCJTZ2sO9dhSouvkKbt0kR3mHMxD6rztjSXj5fDx3qt9y0Hgg==)
21. [pnas.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0cLsGfV_qgUET0d7kbYua-eRVJ19aOIKYQJC684xDadqGOVhbSpNLOx81W-_tcrFZRxgzwVKA4HWi3rbtslmIKRUo_1ivzT4-JVtOsvkDlK5ICAe8KGpb1Zti78KbDQ3kewlN2A==)
22. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMt2z3Dhksg-_S2jOqh3QogBDX6o8loNkh8ky_NYqswCX38l-YqBl2aCNSb2jY5Ez08clSeOH26a7Jd2g6_St5kU-UMvTUxjsVog8vosT_tst3JqFXBK5D1QNhEYXUB9j2NY3cZ-2gh070L0SI--qn7vy4I_W-O3HD1flOrzZBqTi6-stOrowjUssulIiP)
23. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFE8NTExaasRDx4ybpn1DL5f4KQRcoq5UXVqvMYWaboQAHau9NEp1KDKKvb9haBWJjm915IbxUGTtWFR7ZhUrtMA-IwsFpIdwB8GTnEpEwvoiJFOTQHW5TKHpzAIzIVRBbqFH8tiw==)
24. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtVPVz_6Se3gXMA-Z-r8jCGAXll8PoQxVQR1t3q-8-o-OyQZ3pX6k6T_zZ4S3OACkQU4DbEQ0-Kd6AqG9p0COxyEa3HbDSrCaI-WpbMYez_eJEZfmyeEGkjaG0BDLtxDe_5Q==)
25. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBUmcjUR3O2J_zxDQE16VAttss9nO8wa4PjovztP2eQnb0kk9xTHiqQ1_2XxynOaQrShjsd6AWAABtoo5PaBVt5r81sJ5T5lX4Bjfw-GaYjWwkGL0srD75ELkgrZc=)
26. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAr8--YpwqQWw3E5EKlNzQtvY5wK4JOACaiqovfW4S_mw6-uQNM1bIVYJE4QYG-iI6fm5YVB8bY9EiaSr8AJaSXGUWajWN5CQ1ZBL7ffZfLHdc0ZMhVX0v6xpKu5LNIP_4N-OezLA=)
27. [plos.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_Yw5N0fcJHPPkMpVoKw4kc7rcj_34UsWFJg4wvAH2lnd3hyW1MtJAtoZSX1nFK-nEdWSOGaG-h9YBhq2BSwrO2OMfFZ9s6IKJQk2jWOWQvDeAzZn3GTqe8O2rmEdypzM7gxSA_JyU0INzIs5d_6bUlaRjeIx0MV3ER9mZQ90=)
28. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkyCmSW9Km845CYjKvbN3TPmQmmCQHA4y1AG8o85Z3fuLrqTkg60vMLlqcFq_8RzO9c1QzEoZSZEg4GYyoPfsYwnnADJRcPANtrQA1mNEdnKbjO4kiNCDQe6ZXIcmQs8SqgTABP-mLnfnlGZcCZ22Z65wmlpQ1eCoOaWjLfibeo2kYLPDjFZgKxnFueWyak3Z2b153QX5FivwPILwugYPSYxwuoDyNjFXklhU=)
29. [plasticsurgerykey.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFf3bQtZn9u56efKNr2H8JkuAk_IVcUUJ8Q6-h2RQSslrYbfJfherKXkkZyS4UByycrlWA-zJRVC_bQ_CwDPiVoHV4juVd3ClqfdkBLHqr2VWUIuuwEKtYsh2rIIZHk9X0Slig7r_ccvfbGPQE=)
30. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQESi8ARuhJly1EzaRV338vjU1ZDFpBwi-5lUp3sV2WXrZ2odsJNXxKh25GpP0BN8ZZ2dAxGfdLSMFx36ympHUTZVeEKZCeTs32R5dCTCcJ3DNAlVEJz2QSyp5AMWVli8pWXdjo8Psqrbw_H_QWVRgCqy5il8ytrxYQdDMylVjbUmg3KRBnU1PkJGZZwm3GYF31NV107wFaGrEvbiSdj-LJPZqXAbJGbcTTXVD2noKSX1sJZsr9i70wkoXbrGsDA==)
31. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEloVB9DZx4h1AEB7bh4rjMgj8WDMCFnDZHQvx1clcNOkHJHMYkgkYyzzGTrIFkgCTaf6bx_wKOBVkbk2dq9KIS3qbvKoTbBJeGdStI0iDCiGOBLKFtPGYJ74ZAW4gzYbb0LZhbrhJu)
32. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZ_UwPXP5TEHIZfmYok91cEE1drOQOwubik-oswtOfmIZ4qQFXJ-1ZLIszb2gaC2L2lTu3cD_Dy37mq5hPDzIyIEeq63dAGAstHgCaaaJB0IFvaBkfESiNjhRWA2RikP6I2A==)
33. [rch.org.au](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4Hnthi65f5Q9Ywv0il0_M1s9GSpMxaHqu1MriztfVAdNA4dC4pVe-0dw2xD58TebyPBJG1DPEa3VU_mDBhImsZe37IOboNXa1WvABBoutkvqgcOLtTeIJ9a4-2AtDJB4vgITIwU4wrkFXABMJeskdON8jg1rKeWg9pCF67lupdEI7sFQFRV3frBm9RNSM4DVIUYbNsE0kAwbCC9X8gm6JMo_uo3WtGSmvk0JqXotdj-FJCS52QuMpHy7__ufYmM7Fsgz_6lcIMImRxw==)
34. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIUITSQQuFrrG6LO6cmIFQBbeSImfh-TRQcrWyjo980qnx0vdFbC6_vDb07HLao4502Xvr1L7ITqFiMwoRmo4ZJyAJosfb9rZVjl8S451LXl7Fxkpn-AN2fdNnCjFQoqtzhaZgjyE=)
35. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfNwfHjDobuOg-9dgu4IjIMbV4zNyoJKbgBvQmC5TTnLNm20mIVdYRjbBYLie3CxCEXMoVvnlA29Dps8yyOWzIOk3enmqretsxxC96wrP7U5H1nRxYexX8bb1bFyGGnXucYM3PlKroPdZgwQ==)


## Annotations
Annotation(end_index=1849, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdbqWvngsOMlNFfHMpwfz8uV_1zKNvM2pqU-mJ5vAhKw2pIkOuuwoc_Aq1Vds2_de4DLsTFiksdIKc1s7dBBVRa-m4otkJq6-6fww2elK31de26Tr5sHQtvACu_kcE9tFaax8N3ciK03pms-BLxVoUJixL4GMak4txctU294K7mlTk_l43FTDj5TWkSOk2ecw91WHGK3TyYw==', start_index=1837)
Annotation(end_index=1849, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-n5CICFPCJPvbAQK9oR47hCd17H5DeK0iPo57gjO294qQH4WeywqRD6S-AjZBtQBheQNFpVna2XINYRRTcTixGhlCez_fyxzC4lgCYpNKHmnj4oRxreeuSh9AudYW56KSiA==', start_index=1837)
Annotation(end_index=2400, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIyehVZ8diqh7NsvGhHopvzcmFJbM7gBnfzoNXT-3AKXoHQ4Z5CNlq2fH6x-dPLLErKDnimpNQ64ovItcFDigq2gswmQgdNHHXINA0yDMh_hOYh60AY2bultfUkyolGggn6XqrOyIsznNw_w==', start_index=2388)
Annotation(end_index=2400, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdbqWvngsOMlNFfHMpwfz8uV_1zKNvM2pqU-mJ5vAhKw2pIkOuuwoc_Aq1Vds2_de4DLsTFiksdIKc1s7dBBVRa-m4otkJq6-6fww2elK31de26Tr5sHQtvACu_kcE9tFaax8N3ciK03pms-BLxVoUJixL4GMak4txctU294K7mlTk_l43FTDj5TWkSOk2ecw91WHGK3TyYw==', start_index=2388)
Annotation(end_index=3462, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUz25xJYlZ3pyjThXJ8dZD7P0c8_W7HGeAuBlmmd06dcsigxbBNTtaobUoaZDUvck8ImwssnZGsb2_yAPaiWuPEOy26sJVXOd6B_Vhq-rgaKB18mEww2ZPmm1EGDHXUjVSoNfJgRg=', start_index=3450)
Annotation(end_index=3462, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrOLUi9jJPEae5f8KpvjgkaudHyEiFy7d8NYADMI2AuxmmT6iXBSpZY9mTbd8IvsTXZUg88HJc69X9bPBVxr8TGpKBd6nyUe6aovrcqh0K9NDuls5-qVwG-C1Nlq-TgfgM875hVes0_mUbBxqVgIWPwA9UOjYvs1Ho6hD0SOsyHfMzJYncgKHYAVjDf8a9B-Rb', start_index=3450)
Annotation(end_index=3613, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCQASWikPK8qskTyeIrV1g3arBlVxL1npT0Yi1RLIL8_Ohb0suu92pnfbYs9bq1nnC4DFdRO-0CvHER26V4CNXK-5Z2HpEkJuSPmjr1Xx17QJLFVJiX56RbweTJHQa7yM=', start_index=3601)
Annotation(end_index=3613, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrOLUi9jJPEae5f8KpvjgkaudHyEiFy7d8NYADMI2AuxmmT6iXBSpZY9mTbd8IvsTXZUg88HJc69X9bPBVxr8TGpKBd6nyUe6aovrcqh0K9NDuls5-qVwG-C1Nlq-TgfgM875hVes0_mUbBxqVgIWPwA9UOjYvs1Ho6hD0SOsyHfMzJYncgKHYAVjDf8a9B-Rb', start_index=3601)
Annotation(end_index=4028, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVS6OD0MoEqgdZxty8WMrlCOYr8SVbbsg8lAh_nRVBJTH24ieFAzEESrzxV_r_uHd9sCTxQKxEe9oLcnhScHsgO2b2HxweOBrXlGnMzBGwmWl8DdZcCzIeu_3E7Gm25QRdcz1nPaFk_SNm44xMuVNi78ebZZIVaAo=', start_index=4019)
Annotation(end_index=4308, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExY5duGG9aGFCgtkx9op1-E7cd2qRoUCoAtBpE-ZaqclZT9LjufmZ_fWhpaMikndMxa2e9nEdXnESwkt_dU6ZEMyt-7ADV2sn1ZjvZ_k7vkCoAGVyUfH_si5dRCcf_ZRj0hVgHEE6Vmm71l3ZU', start_index=4296)
Annotation(end_index=4308, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCl0bZHYljB2BTv7LFqXTOSdMZqNj_nQ2ZxH8eK0oyH_LkG_o9cS4HWlpY4y9dJq8u8tZqlntjsV0L8D0bcgvKUe1rZv4UqE2KpL8ZClpB06IkpERtjYpQVOuG_1gAnQd-YyqFbJKeOlDOWUUPye-sAjIsYnUb-Hfo8ptnXT0Tn2BGs0gkDO1OTtZ7JkynCmib3pOghd9G9mA8FeMQNMXLPBFQs9ZkLCHy', start_index=4296)
Annotation(end_index=4615, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExY5duGG9aGFCgtkx9op1-E7cd2qRoUCoAtBpE-ZaqclZT9LjufmZ_fWhpaMikndMxa2e9nEdXnESwkt_dU6ZEMyt-7ADV2sn1ZjvZ_k7vkCoAGVyUfH_si5dRCcf_ZRj0hVgHEE6Vmm71l3ZU', start_index=4603)
Annotation(end_index=4615, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-n5CICFPCJPvbAQK9oR47hCd17H5DeK0iPo57gjO294qQH4WeywqRD6S-AjZBtQBheQNFpVna2XINYRRTcTixGhlCez_fyxzC4lgCYpNKHmnj4oRxreeuSh9AudYW56KSiA==', start_index=4603)
Annotation(end_index=5172, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdbqWvngsOMlNFfHMpwfz8uV_1zKNvM2pqU-mJ5vAhKw2pIkOuuwoc_Aq1Vds2_de4DLsTFiksdIKc1s7dBBVRa-m4otkJq6-6fww2elK31de26Tr5sHQtvACu_kcE9tFaax8N3ciK03pms-BLxVoUJixL4GMak4txctU294K7mlTk_l43FTDj5TWkSOk2ecw91WHGK3TyYw==', start_index=5163)
Annotation(end_index=5723, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOaQUAzpJ0PK0gyeqo2Km5dQ2nVYG2NKEZ1-LxWIaoAL6aqPhFPpy91u-2LZCbyeg6RCHhsu7d8RBldhryMLSIpE49GDwgcEqpgkQVwzYSAG_-GQEOHCSLmTdd15xllmVkM_mykmgkZP4nK4zS7IBFDo61jndxzJ-RHOgjyihx5Ux2J7DqHte6z_5u4ODz9hQTKEPXRfHV025F9VvFia8foBEBaCyhF_nk6W51ew==', start_index=5710)
Annotation(end_index=5723, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdbqWvngsOMlNFfHMpwfz8uV_1zKNvM2pqU-mJ5vAhKw2pIkOuuwoc_Aq1Vds2_de4DLsTFiksdIKc1s7dBBVRa-m4otkJq6-6fww2elK31de26Tr5sHQtvACu_kcE9tFaax8N3ciK03pms-BLxVoUJixL4GMak4txctU294K7mlTk_l43FTDj5TWkSOk2ecw91WHGK3TyYw==', start_index=5710)
Annotation(end_index=5950, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdbqWvngsOMlNFfHMpwfz8uV_1zKNvM2pqU-mJ5vAhKw2pIkOuuwoc_Aq1Vds2_de4DLsTFiksdIKc1s7dBBVRa-m4otkJq6-6fww2elK31de26Tr5sHQtvACu_kcE9tFaax8N3ciK03pms-BLxVoUJixL4GMak4txctU294K7mlTk_l43FTDj5TWkSOk2ecw91WHGK3TyYw==', start_index=5941)
Annotation(end_index=6172, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdbqWvngsOMlNFfHMpwfz8uV_1zKNvM2pqU-mJ5vAhKw2pIkOuuwoc_Aq1Vds2_de4DLsTFiksdIKc1s7dBBVRa-m4otkJq6-6fww2elK31de26Tr5sHQtvACu_kcE9tFaax8N3ciK03pms-BLxVoUJixL4GMak4txctU294K7mlTk_l43FTDj5TWkSOk2ecw91WHGK3TyYw==', start_index=6159)
Annotation(end_index=6172, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHq86Oo9t5pygnE-RJxajrMPtELlWPnHFk-w_bW0ZNk4SJFZVsoHfdy_mdSmCBGptI1OCW1P-QoStt05fC35Lim3dzRdz_OzPG_uRVBakgt3zTdMN1C3Cf2k4OydfLLHJ_iFQ==', start_index=6159)
Annotation(end_index=6518, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfGvMwp8jTiOIm2IEiMj5zw0hj_HkAdzIWSCPvXCaPpWah_EMMnX0FIQEJq8IE_aZ29_qH_R7XUoDvlMYKq5FrXvfYbRMY_6FKxlYpTILjt7rYPa_bXSBA_Uxem6QV', start_index=6504)
Annotation(end_index=6518, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOaQUAzpJ0PK0gyeqo2Km5dQ2nVYG2NKEZ1-LxWIaoAL6aqPhFPpy91u-2LZCbyeg6RCHhsu7d8RBldhryMLSIpE49GDwgcEqpgkQVwzYSAG_-GQEOHCSLmTdd15xllmVkM_mykmgkZP4nK4zS7IBFDo61jndxzJ-RHOgjyihx5Ux2J7DqHte6z_5u4ODz9hQTKEPXRfHV025F9VvFia8foBEBaCyhF_nk6W51ew==', start_index=6504)
Annotation(end_index=6695, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHq86Oo9t5pygnE-RJxajrMPtELlWPnHFk-w_bW0ZNk4SJFZVsoHfdy_mdSmCBGptI1OCW1P-QoStt05fC35Lim3dzRdz_OzPG_uRVBakgt3zTdMN1C3Cf2k4OydfLLHJ_iFQ==', start_index=6681)
Annotation(end_index=6695, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtaOoLLnQOeh7O4EqritSz0HyOsl3p_y3z4fsZDSbFpBarOePW52aJwcCZ1xcYxrOl_7HbUuaqmadFbkU5L9Ybom_1riHXbqImnPFd3W3Tzy6k1qPkjtrQa5u0i7m9DmHmyVL1C4BTUhyqwAadB-B5EaIVwjQ_Rg-afjHTXg==', start_index=6681)
Annotation(end_index=7657, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4kNIs99xS7PpdMMgzhKJMBh-WsspZItacynW-nTCtmhdbAC-ttwRLR2MlhxsDrWBK4RFTR1a3IcyahcuHzRWEjIkH125-mGUG_nv_wpVchoThs-EjCh2p1mm1PzBm', start_index=7639)
Annotation(end_index=7657, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9Mlnj2ZAQzpOzxVDDmmnyI2Bpq_4rERy5uQ82XpYS4chILRDR-ckqbCGLI8kfZxkDOy1h_A7X7xjf6PB_g5hujLU_ZlcFQcFV9Hny626g2qmErD95WXdIL0mIiytI4IE=', start_index=7639)
Annotation(end_index=7657, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUUYX_v0yAVyr9M3GFNUgjDopf_CfpZ5cwy7fYoiahrCkX41kElFvrCMnf0eHGQ5B6hVkGipfdRm2QbicDcX4N3f6tQiAaCvjFIhHbRRzsSqfgaNJ7LcsgoV9QMUhoPG21mmly_Qehz-qp1wtREKNVZzQl_ifVeNNEmqy3a_bp1NSsXyZDyLRIIyQw79QW_DSvG_TxqFIThGndc5XGsuHDlELcxsa-Uqf-lrctRugnUll89E8oaFTOwQylm6_wVn1wnwHBlg1lDlNrew==', start_index=7639)
Annotation(end_index=8056, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEf7iuq130ZmuwzMMWi6PogS1WwNaXxX4Q7ZT421JDVZ-fz7WRhCIxxW2uVSi6vy_DlLQ-_RNk1Y3y8j1NV0-EIHq4nDFxb6hAq1NHJGpQgegHDNs0c4P1o6eEHddtAO2efdjLO9iMD0SrQ', start_index=8034)
Annotation(end_index=8056, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtyOoDFinTrir1b2TbZj8dbyEogkWIaeopX90mOV7G9HVqhlLEpQXaSjYy7_4lIcz-LKqyvfjz8abZ8xXvOYhZuVVqc2KzBm9psOtYezebkMvINPROyeJsdeGXsfdCE_VH2dGuy94=', start_index=8034)
Annotation(end_index=8056, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4kNIs99xS7PpdMMgzhKJMBh-WsspZItacynW-nTCtmhdbAC-ttwRLR2MlhxsDrWBK4RFTR1a3IcyahcuHzRWEjIkH125-mGUG_nv_wpVchoThs-EjCh2p1mm1PzBm', start_index=8034)
Annotation(end_index=8056, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUUYX_v0yAVyr9M3GFNUgjDopf_CfpZ5cwy7fYoiahrCkX41kElFvrCMnf0eHGQ5B6hVkGipfdRm2QbicDcX4N3f6tQiAaCvjFIhHbRRzsSqfgaNJ7LcsgoV9QMUhoPG21mmly_Qehz-qp1wtREKNVZzQl_ifVeNNEmqy3a_bp1NSsXyZDyLRIIyQw79QW_DSvG_TxqFIThGndc5XGsuHDlELcxsa-Uqf-lrctRugnUll89E8oaFTOwQylm6_wVn1wnwHBlg1lDlNrew==', start_index=8034)
Annotation(end_index=8359, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0fI0s_0jmfqnekyQn6VnTjf1j4F0G-uM4QSr2tAazLXppbNRbuLaOOGTjkK5q_vlwXGB5AINknsQ5TdutlMA-GXCJTZ2sO9dhSouvkKbt0kR3mHMxD6rztjSXj5fDx3qt9y0Hgg==', start_index=8341)
Annotation(end_index=8359, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtyOoDFinTrir1b2TbZj8dbyEogkWIaeopX90mOV7G9HVqhlLEpQXaSjYy7_4lIcz-LKqyvfjz8abZ8xXvOYhZuVVqc2KzBm9psOtYezebkMvINPROyeJsdeGXsfdCE_VH2dGuy94=', start_index=8341)
Annotation(end_index=8359, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFBXE9LwAsyslEYF7tDql_qufbMubk-lYR_lrbZGmnMLW7-IgMNhv-zuwg9WgFQxSJywS24t1u2acIpZ2cX_K--UipKoDXOqbBOKOztlvtdYfU7JWzsENNbQiBNmMlgV31-l6ti7JJrcCme3IvBs9uVBpZvvs7Pn3EvHqZXdg=', start_index=8341)
Annotation(end_index=8644, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0cLsGfV_qgUET0d7kbYua-eRVJ19aOIKYQJC684xDadqGOVhbSpNLOx81W-_tcrFZRxgzwVKA4HWi3rbtslmIKRUo_1ivzT4-JVtOsvkDlK5ICAe8KGpb1Zti78KbDQ3kewlN2A==', start_index=8630)
Annotation(end_index=8644, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMt2z3Dhksg-_S2jOqh3QogBDX6o8loNkh8ky_NYqswCX38l-YqBl2aCNSb2jY5Ez08clSeOH26a7Jd2g6_St5kU-UMvTUxjsVog8vosT_tst3JqFXBK5D1QNhEYXUB9j2NY3cZ-2gh070L0SI--qn7vy4I_W-O3HD1flOrzZBqTi6-stOrowjUssulIiP', start_index=8630)
Annotation(end_index=9469, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBUmcjUR3O2J_zxDQE16VAttss9nO8wa4PjovztP2eQnb0kk9xTHiqQ1_2XxynOaQrShjsd6AWAABtoo5PaBVt5r81sJ5T5lX4Bjfw-GaYjWwkGL0srD75ELkgrZc=', start_index=9447)
Annotation(end_index=9469, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAr8--YpwqQWw3E5EKlNzQtvY5wK4JOACaiqovfW4S_mw6-uQNM1bIVYJE4QYG-iI6fm5YVB8bY9EiaSr8AJaSXGUWajWN5CQ1ZBL7ffZfLHdc0ZMhVX0v6xpKu5LNIP_4N-OezLA=', start_index=9447)
Annotation(end_index=9469, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFE8NTExaasRDx4ybpn1DL5f4KQRcoq5UXVqvMYWaboQAHau9NEp1KDKKvb9haBWJjm915IbxUGTtWFR7ZhUrtMA-IwsFpIdwB8GTnEpEwvoiJFOTQHW5TKHpzAIzIVRBbqFH8tiw==', start_index=9447)
Annotation(end_index=9469, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtVPVz_6Se3gXMA-Z-r8jCGAXll8PoQxVQR1t3q-8-o-OyQZ3pX6k6T_zZ4S3OACkQU4DbEQ0-Kd6AqG9p0COxyEa3HbDSrCaI-WpbMYez_eJEZfmyeEGkjaG0BDLtxDe_5Q==', start_index=9447)
Annotation(end_index=9740, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_Yw5N0fcJHPPkMpVoKw4kc7rcj_34UsWFJg4wvAH2lnd3hyW1MtJAtoZSX1nFK-nEdWSOGaG-h9YBhq2BSwrO2OMfFZ9s6IKJQk2jWOWQvDeAzZn3GTqe8O2rmEdypzM7gxSA_JyU0INzIs5d_6bUlaRjeIx0MV3ER9mZQ90=', start_index=9730)
Annotation(end_index=10079, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0cLsGfV_qgUET0d7kbYua-eRVJ19aOIKYQJC684xDadqGOVhbSpNLOx81W-_tcrFZRxgzwVKA4HWi3rbtslmIKRUo_1ivzT4-JVtOsvkDlK5ICAe8KGpb1Zti78KbDQ3kewlN2A==', start_index=10069)
Annotation(end_index=10209, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfGvMwp8jTiOIm2IEiMj5zw0hj_HkAdzIWSCPvXCaPpWah_EMMnX0FIQEJq8IE_aZ29_qH_R7XUoDvlMYKq5FrXvfYbRMY_6FKxlYpTILjt7rYPa_bXSBA_Uxem6QV', start_index=10195)
Annotation(end_index=10209, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0cLsGfV_qgUET0d7kbYua-eRVJ19aOIKYQJC684xDadqGOVhbSpNLOx81W-_tcrFZRxgzwVKA4HWi3rbtslmIKRUo_1ivzT4-JVtOsvkDlK5ICAe8KGpb1Zti78KbDQ3kewlN2A==', start_index=10195)
Annotation(end_index=10692, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdbqWvngsOMlNFfHMpwfz8uV_1zKNvM2pqU-mJ5vAhKw2pIkOuuwoc_Aq1Vds2_de4DLsTFiksdIKc1s7dBBVRa-m4otkJq6-6fww2elK31de26Tr5sHQtvACu_kcE9tFaax8N3ciK03pms-BLxVoUJixL4GMak4txctU294K7mlTk_l43FTDj5TWkSOk2ecw91WHGK3TyYw==', start_index=10679)
Annotation(end_index=10692, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHq86Oo9t5pygnE-RJxajrMPtELlWPnHFk-w_bW0ZNk4SJFZVsoHfdy_mdSmCBGptI1OCW1P-QoStt05fC35Lim3dzRdz_OzPG_uRVBakgt3zTdMN1C3Cf2k4OydfLLHJ_iFQ==', start_index=10679)
Annotation(end_index=10947, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdbqWvngsOMlNFfHMpwfz8uV_1zKNvM2pqU-mJ5vAhKw2pIkOuuwoc_Aq1Vds2_de4DLsTFiksdIKc1s7dBBVRa-m4otkJq6-6fww2elK31de26Tr5sHQtvACu_kcE9tFaax8N3ciK03pms-BLxVoUJixL4GMak4txctU294K7mlTk_l43FTDj5TWkSOk2ecw91WHGK3TyYw==', start_index=10938)
Annotation(end_index=11171, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkyCmSW9Km845CYjKvbN3TPmQmmCQHA4y1AG8o85Z3fuLrqTkg60vMLlqcFq_8RzO9c1QzEoZSZEg4GYyoPfsYwnnADJRcPANtrQA1mNEdnKbjO4kiNCDQe6ZXIcmQs8SqgTABP-mLnfnlGZcCZ22Z65wmlpQ1eCoOaWjLfibeo2kYLPDjFZgKxnFueWyak3Z2b153QX5FivwPILwugYPSYxwuoDyNjFXklhU=', start_index=11154)
Annotation(end_index=11171, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdbqWvngsOMlNFfHMpwfz8uV_1zKNvM2pqU-mJ5vAhKw2pIkOuuwoc_Aq1Vds2_de4DLsTFiksdIKc1s7dBBVRa-m4otkJq6-6fww2elK31de26Tr5sHQtvACu_kcE9tFaax8N3ciK03pms-BLxVoUJixL4GMak4txctU294K7mlTk_l43FTDj5TWkSOk2ecw91WHGK3TyYw==', start_index=11154)
Annotation(end_index=11171, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHq86Oo9t5pygnE-RJxajrMPtELlWPnHFk-w_bW0ZNk4SJFZVsoHfdy_mdSmCBGptI1OCW1P-QoStt05fC35Lim3dzRdz_OzPG_uRVBakgt3zTdMN1C3Cf2k4OydfLLHJ_iFQ==', start_index=11154)
Annotation(end_index=11563, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFf3bQtZn9u56efKNr2H8JkuAk_IVcUUJ8Q6-h2RQSslrYbfJfherKXkkZyS4UByycrlWA-zJRVC_bQ_CwDPiVoHV4juVd3ClqfdkBLHqr2VWUIuuwEKtYsh2rIIZHk9X0Slig7r_ccvfbGPQE=', start_index=11546)
Annotation(end_index=11563, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrOLUi9jJPEae5f8KpvjgkaudHyEiFy7d8NYADMI2AuxmmT6iXBSpZY9mTbd8IvsTXZUg88HJc69X9bPBVxr8TGpKBd6nyUe6aovrcqh0K9NDuls5-qVwG-C1Nlq-TgfgM875hVes0_mUbBxqVgIWPwA9UOjYvs1Ho6hD0SOsyHfMzJYncgKHYAVjDf8a9B-Rb', start_index=11546)
Annotation(end_index=11563, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtaOoLLnQOeh7O4EqritSz0HyOsl3p_y3z4fsZDSbFpBarOePW52aJwcCZ1xcYxrOl_7HbUuaqmadFbkU5L9Ybom_1riHXbqImnPFd3W3Tzy6k1qPkjtrQa5u0i7m9DmHmyVL1C4BTUhyqwAadB-B5EaIVwjQ_Rg-afjHTXg==', start_index=11546)
Annotation(end_index=11761, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHq86Oo9t5pygnE-RJxajrMPtELlWPnHFk-w_bW0ZNk4SJFZVsoHfdy_mdSmCBGptI1OCW1P-QoStt05fC35Lim3dzRdz_OzPG_uRVBakgt3zTdMN1C3Cf2k4OydfLLHJ_iFQ==', start_index=11747)
Annotation(end_index=11761, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtaOoLLnQOeh7O4EqritSz0HyOsl3p_y3z4fsZDSbFpBarOePW52aJwcCZ1xcYxrOl_7HbUuaqmadFbkU5L9Ybom_1riHXbqImnPFd3W3Tzy6k1qPkjtrQa5u0i7m9DmHmyVL1C4BTUhyqwAadB-B5EaIVwjQ_Rg-afjHTXg==', start_index=11747)
Annotation(end_index=12273, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-n5CICFPCJPvbAQK9oR47hCd17H5DeK0iPo57gjO294qQH4WeywqRD6S-AjZBtQBheQNFpVna2XINYRRTcTixGhlCez_fyxzC4lgCYpNKHmnj4oRxreeuSh9AudYW56KSiA==', start_index=12264)
Annotation(end_index=12711, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfGvMwp8jTiOIm2IEiMj5zw0hj_HkAdzIWSCPvXCaPpWah_EMMnX0FIQEJq8IE_aZ29_qH_R7XUoDvlMYKq5FrXvfYbRMY_6FKxlYpTILjt7rYPa_bXSBA_Uxem6QV', start_index=12693)
Annotation(end_index=12711, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0cLsGfV_qgUET0d7kbYua-eRVJ19aOIKYQJC684xDadqGOVhbSpNLOx81W-_tcrFZRxgzwVKA4HWi3rbtslmIKRUo_1ivzT4-JVtOsvkDlK5ICAe8KGpb1Zti78KbDQ3kewlN2A==', start_index=12693)
Annotation(end_index=12711, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQESi8ARuhJly1EzaRV338vjU1ZDFpBwi-5lUp3sV2WXrZ2odsJNXxKh25GpP0BN8ZZ2dAxGfdLSMFx36ympHUTZVeEKZCeTs32R5dCTCcJ3DNAlVEJz2QSyp5AMWVli8pWXdjo8Psqrbw_H_QWVRgCqy5il8ytrxYQdDMylVjbUmg3KRBnU1PkJGZZwm3GYF31NV107wFaGrEvbiSdj-LJPZqXAbJGbcTTXVD2noKSX1sJZsr9i70wkoXbrGsDA==', start_index=12693)
Annotation(end_index=13939, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOaQUAzpJ0PK0gyeqo2Km5dQ2nVYG2NKEZ1-LxWIaoAL6aqPhFPpy91u-2LZCbyeg6RCHhsu7d8RBldhryMLSIpE49GDwgcEqpgkQVwzYSAG_-GQEOHCSLmTdd15xllmVkM_mykmgkZP4nK4zS7IBFDo61jndxzJ-RHOgjyihx5Ux2J7DqHte6z_5u4ODz9hQTKEPXRfHV025F9VvFia8foBEBaCyhF_nk6W51ew==', start_index=13923)
Annotation(end_index=13939, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdbqWvngsOMlNFfHMpwfz8uV_1zKNvM2pqU-mJ5vAhKw2pIkOuuwoc_Aq1Vds2_de4DLsTFiksdIKc1s7dBBVRa-m4otkJq6-6fww2elK31de26Tr5sHQtvACu_kcE9tFaax8N3ciK03pms-BLxVoUJixL4GMak4txctU294K7mlTk_l43FTDj5TWkSOk2ecw91WHGK3TyYw==', start_index=13923)
Annotation(end_index=13939, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-n5CICFPCJPvbAQK9oR47hCd17H5DeK0iPo57gjO294qQH4WeywqRD6S-AjZBtQBheQNFpVna2XINYRRTcTixGhlCez_fyxzC4lgCYpNKHmnj4oRxreeuSh9AudYW56KSiA==', start_index=13923)
Annotation(end_index=14260, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEloVB9DZx4h1AEB7bh4rjMgj8WDMCFnDZHQvx1clcNOkHJHMYkgkYyzzGTrIFkgCTaf6bx_wKOBVkbk2dq9KIS3qbvKoTbBJeGdStI0iDCiGOBLKFtPGYJ74ZAW4gzYbb0LZhbrhJu', start_index=14246)
Annotation(end_index=14260, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOaQUAzpJ0PK0gyeqo2Km5dQ2nVYG2NKEZ1-LxWIaoAL6aqPhFPpy91u-2LZCbyeg6RCHhsu7d8RBldhryMLSIpE49GDwgcEqpgkQVwzYSAG_-GQEOHCSLmTdd15xllmVkM_mykmgkZP4nK4zS7IBFDo61jndxzJ-RHOgjyihx5Ux2J7DqHte6z_5u4ODz9hQTKEPXRfHV025F9VvFia8foBEBaCyhF_nk6W51ew==', start_index=14246)
Annotation(end_index=14802, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIyehVZ8diqh7NsvGhHopvzcmFJbM7gBnfzoNXT-3AKXoHQ4Z5CNlq2fH6x-dPLLErKDnimpNQ64ovItcFDigq2gswmQgdNHHXINA0yDMh_hOYh60AY2bultfUkyolGggn6XqrOyIsznNw_w==', start_index=14789)
Annotation(end_index=14802, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZ_UwPXP5TEHIZfmYok91cEE1drOQOwubik-oswtOfmIZ4qQFXJ-1ZLIszb2gaC2L2lTu3cD_Dy37mq5hPDzIyIEeq63dAGAstHgCaaaJB0IFvaBkfESiNjhRWA2RikP6I2A==', start_index=14789)
Annotation(end_index=14987, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOaQUAzpJ0PK0gyeqo2Km5dQ2nVYG2NKEZ1-LxWIaoAL6aqPhFPpy91u-2LZCbyeg6RCHhsu7d8RBldhryMLSIpE49GDwgcEqpgkQVwzYSAG_-GQEOHCSLmTdd15xllmVkM_mykmgkZP4nK4zS7IBFDo61jndxzJ-RHOgjyihx5Ux2J7DqHte6z_5u4ODz9hQTKEPXRfHV025F9VvFia8foBEBaCyhF_nk6W51ew==', start_index=14977)
Annotation(end_index=15644, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4Hnthi65f5Q9Ywv0il0_M1s9GSpMxaHqu1MriztfVAdNA4dC4pVe-0dw2xD58TebyPBJG1DPEa3VU_mDBhImsZe37IOboNXa1WvABBoutkvqgcOLtTeIJ9a4-2AtDJB4vgITIwU4wrkFXABMJeskdON8jg1rKeWg9pCF67lupdEI7sFQFRV3frBm9RNSM4DVIUYbNsE0kAwbCC9X8gm6JMo_uo3WtGSmvk0JqXotdj-FJCS52QuMpHy7__ufYmM7Fsgz_6lcIMImRxw==', start_index=15631)
Annotation(end_index=15644, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUz25xJYlZ3pyjThXJ8dZD7P0c8_W7HGeAuBlmmd06dcsigxbBNTtaobUoaZDUvck8ImwssnZGsb2_yAPaiWuPEOy26sJVXOd6B_Vhq-rgaKB18mEww2ZPmm1EGDHXUjVSoNfJgRg=', start_index=15631)
Annotation(end_index=15793, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOaQUAzpJ0PK0gyeqo2Km5dQ2nVYG2NKEZ1-LxWIaoAL6aqPhFPpy91u-2LZCbyeg6RCHhsu7d8RBldhryMLSIpE49GDwgcEqpgkQVwzYSAG_-GQEOHCSLmTdd15xllmVkM_mykmgkZP4nK4zS7IBFDo61jndxzJ-RHOgjyihx5Ux2J7DqHte6z_5u4ODz9hQTKEPXRfHV025F9VvFia8foBEBaCyhF_nk6W51ew==', start_index=15777)
Annotation(end_index=15793, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUz25xJYlZ3pyjThXJ8dZD7P0c8_W7HGeAuBlmmd06dcsigxbBNTtaobUoaZDUvck8ImwssnZGsb2_yAPaiWuPEOy26sJVXOd6B_Vhq-rgaKB18mEww2ZPmm1EGDHXUjVSoNfJgRg=', start_index=15777)
Annotation(end_index=15793, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrOLUi9jJPEae5f8KpvjgkaudHyEiFy7d8NYADMI2AuxmmT6iXBSpZY9mTbd8IvsTXZUg88HJc69X9bPBVxr8TGpKBd6nyUe6aovrcqh0K9NDuls5-qVwG-C1Nlq-TgfgM875hVes0_mUbBxqVgIWPwA9UOjYvs1Ho6hD0SOsyHfMzJYncgKHYAVjDf8a9B-Rb', start_index=15777)
Annotation(end_index=15939, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4Hnthi65f5Q9Ywv0il0_M1s9GSpMxaHqu1MriztfVAdNA4dC4pVe-0dw2xD58TebyPBJG1DPEa3VU_mDBhImsZe37IOboNXa1WvABBoutkvqgcOLtTeIJ9a4-2AtDJB4vgITIwU4wrkFXABMJeskdON8jg1rKeWg9pCF67lupdEI7sFQFRV3frBm9RNSM4DVIUYbNsE0kAwbCC9X8gm6JMo_uo3WtGSmvk0JqXotdj-FJCS52QuMpHy7__ufYmM7Fsgz_6lcIMImRxw==', start_index=15923)
Annotation(end_index=15939, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCQASWikPK8qskTyeIrV1g3arBlVxL1npT0Yi1RLIL8_Ohb0suu92pnfbYs9bq1nnC4DFdRO-0CvHER26V4CNXK-5Z2HpEkJuSPmjr1Xx17QJLFVJiX56RbweTJHQa7yM=', start_index=15923)
Annotation(end_index=15939, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdbqWvngsOMlNFfHMpwfz8uV_1zKNvM2pqU-mJ5vAhKw2pIkOuuwoc_Aq1Vds2_de4DLsTFiksdIKc1s7dBBVRa-m4otkJq6-6fww2elK31de26Tr5sHQtvACu_kcE9tFaax8N3ciK03pms-BLxVoUJixL4GMak4txctU294K7mlTk_l43FTDj5TWkSOk2ecw91WHGK3TyYw==', start_index=15923)
Annotation(end_index=16589, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOaQUAzpJ0PK0gyeqo2Km5dQ2nVYG2NKEZ1-LxWIaoAL6aqPhFPpy91u-2LZCbyeg6RCHhsu7d8RBldhryMLSIpE49GDwgcEqpgkQVwzYSAG_-GQEOHCSLmTdd15xllmVkM_mykmgkZP4nK4zS7IBFDo61jndxzJ-RHOgjyihx5Ux2J7DqHte6z_5u4ODz9hQTKEPXRfHV025F9VvFia8foBEBaCyhF_nk6W51ew==', start_index=16579)
Annotation(end_index=16910, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEf7iuq130ZmuwzMMWi6PogS1WwNaXxX4Q7ZT421JDVZ-fz7WRhCIxxW2uVSi6vy_DlLQ-_RNk1Y3y8j1NV0-EIHq4nDFxb6hAq1NHJGpQgegHDNs0c4P1o6eEHddtAO2efdjLO9iMD0SrQ', start_index=16897)
Annotation(end_index=16910, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-n5CICFPCJPvbAQK9oR47hCd17H5DeK0iPo57gjO294qQH4WeywqRD6S-AjZBtQBheQNFpVna2XINYRRTcTixGhlCez_fyxzC4lgCYpNKHmnj4oRxreeuSh9AudYW56KSiA==', start_index=16897)
Annotation(end_index=17384, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0fI0s_0jmfqnekyQn6VnTjf1j4F0G-uM4QSr2tAazLXppbNRbuLaOOGTjkK5q_vlwXGB5AINknsQ5TdutlMA-GXCJTZ2sO9dhSouvkKbt0kR3mHMxD6rztjSXj5fDx3qt9y0Hgg==', start_index=17366)
Annotation(end_index=17384, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4kNIs99xS7PpdMMgzhKJMBh-WsspZItacynW-nTCtmhdbAC-ttwRLR2MlhxsDrWBK4RFTR1a3IcyahcuHzRWEjIkH125-mGUG_nv_wpVchoThs-EjCh2p1mm1PzBm', start_index=17366)
Annotation(end_index=17384, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUUYX_v0yAVyr9M3GFNUgjDopf_CfpZ5cwy7fYoiahrCkX41kElFvrCMnf0eHGQ5B6hVkGipfdRm2QbicDcX4N3f6tQiAaCvjFIhHbRRzsSqfgaNJ7LcsgoV9QMUhoPG21mmly_Qehz-qp1wtREKNVZzQl_ifVeNNEmqy3a_bp1NSsXyZDyLRIIyQw79QW_DSvG_TxqFIThGndc5XGsuHDlELcxsa-Uqf-lrctRugnUll89E8oaFTOwQylm6_wVn1wnwHBlg1lDlNrew==', start_index=17366)
Annotation(end_index=17850, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEf7iuq130ZmuwzMMWi6PogS1WwNaXxX4Q7ZT421JDVZ-fz7WRhCIxxW2uVSi6vy_DlLQ-_RNk1Y3y8j1NV0-EIHq4nDFxb6hAq1NHJGpQgegHDNs0c4P1o6eEHddtAO2efdjLO9iMD0SrQ', start_index=17832)
Annotation(end_index=17850, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtyOoDFinTrir1b2TbZj8dbyEogkWIaeopX90mOV7G9HVqhlLEpQXaSjYy7_4lIcz-LKqyvfjz8abZ8xXvOYhZuVVqc2KzBm9psOtYezebkMvINPROyeJsdeGXsfdCE_VH2dGuy94=', start_index=17832)
Annotation(end_index=17850, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIUITSQQuFrrG6LO6cmIFQBbeSImfh-TRQcrWyjo980qnx0vdFbC6_vDb07HLao4502Xvr1L7ITqFiMwoRmo4ZJyAJosfb9rZVjl8S451LXl7Fxkpn-AN2fdNnCjFQoqtzhaZgjyE=', start_index=17832)
Annotation(end_index=18315, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtyOoDFinTrir1b2TbZj8dbyEogkWIaeopX90mOV7G9HVqhlLEpQXaSjYy7_4lIcz-LKqyvfjz8abZ8xXvOYhZuVVqc2KzBm9psOtYezebkMvINPROyeJsdeGXsfdCE_VH2dGuy94=', start_index=18301)
Annotation(end_index=18315, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFBXE9LwAsyslEYF7tDql_qufbMubk-lYR_lrbZGmnMLW7-IgMNhv-zuwg9WgFQxSJywS24t1u2acIpZ2cX_K--UipKoDXOqbBOKOztlvtdYfU7JWzsENNbQiBNmMlgV31-l6ti7JJrcCme3IvBs9uVBpZvvs7Pn3EvHqZXdg=', start_index=18301)
Annotation(end_index=18496, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0cLsGfV_qgUET0d7kbYua-eRVJ19aOIKYQJC684xDadqGOVhbSpNLOx81W-_tcrFZRxgzwVKA4HWi3rbtslmIKRUo_1ivzT4-JVtOsvkDlK5ICAe8KGpb1Zti78KbDQ3kewlN2A==', start_index=18482)
Annotation(end_index=18496, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMt2z3Dhksg-_S2jOqh3QogBDX6o8loNkh8ky_NYqswCX38l-YqBl2aCNSb2jY5Ez08clSeOH26a7Jd2g6_St5kU-UMvTUxjsVog8vosT_tst3JqFXBK5D1QNhEYXUB9j2NY3cZ-2gh070L0SI--qn7vy4I_W-O3HD1flOrzZBqTi6-stOrowjUssulIiP', start_index=18482)
Annotation(end_index=19149, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBUmcjUR3O2J_zxDQE16VAttss9nO8wa4PjovztP2eQnb0kk9xTHiqQ1_2XxynOaQrShjsd6AWAABtoo5PaBVt5r81sJ5T5lX4Bjfw-GaYjWwkGL0srD75ELkgrZc=', start_index=19127)
Annotation(end_index=19149, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAr8--YpwqQWw3E5EKlNzQtvY5wK4JOACaiqovfW4S_mw6-uQNM1bIVYJE4QYG-iI6fm5YVB8bY9EiaSr8AJaSXGUWajWN5CQ1ZBL7ffZfLHdc0ZMhVX0v6xpKu5LNIP_4N-OezLA=', start_index=19127)
Annotation(end_index=19149, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFE8NTExaasRDx4ybpn1DL5f4KQRcoq5UXVqvMYWaboQAHau9NEp1KDKKvb9haBWJjm915IbxUGTtWFR7ZhUrtMA-IwsFpIdwB8GTnEpEwvoiJFOTQHW5TKHpzAIzIVRBbqFH8tiw==', start_index=19127)
Annotation(end_index=19149, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtVPVz_6Se3gXMA-Z-r8jCGAXll8PoQxVQR1t3q-8-o-OyQZ3pX6k6T_zZ4S3OACkQU4DbEQ0-Kd6AqG9p0COxyEa3HbDSrCaI-WpbMYez_eJEZfmyeEGkjaG0BDLtxDe_5Q==', start_index=19127)
Annotation(end_index=19431, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_Yw5N0fcJHPPkMpVoKw4kc7rcj_34UsWFJg4wvAH2lnd3hyW1MtJAtoZSX1nFK-nEdWSOGaG-h9YBhq2BSwrO2OMfFZ9s6IKJQk2jWOWQvDeAzZn3GTqe8O2rmEdypzM7gxSA_JyU0INzIs5d_6bUlaRjeIx0MV3ER9mZQ90=', start_index=19421)
Annotation(end_index=19855, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0cLsGfV_qgUET0d7kbYua-eRVJ19aOIKYQJC684xDadqGOVhbSpNLOx81W-_tcrFZRxgzwVKA4HWi3rbtslmIKRUo_1ivzT4-JVtOsvkDlK5ICAe8KGpb1Zti78KbDQ3kewlN2A==', start_index=19845)
Annotation(end_index=20179, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfGvMwp8jTiOIm2IEiMj5zw0hj_HkAdzIWSCPvXCaPpWah_EMMnX0FIQEJq8IE_aZ29_qH_R7XUoDvlMYKq5FrXvfYbRMY_6FKxlYpTILjt7rYPa_bXSBA_Uxem6QV', start_index=20169)
Annotation(end_index=20461, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdbqWvngsOMlNFfHMpwfz8uV_1zKNvM2pqU-mJ5vAhKw2pIkOuuwoc_Aq1Vds2_de4DLsTFiksdIKc1s7dBBVRa-m4otkJq6-6fww2elK31de26Tr5sHQtvACu_kcE9tFaax8N3ciK03pms-BLxVoUJixL4GMak4txctU294K7mlTk_l43FTDj5TWkSOk2ecw91WHGK3TyYw==', start_index=20452)
Annotation(end_index=21191, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExY5duGG9aGFCgtkx9op1-E7cd2qRoUCoAtBpE-ZaqclZT9LjufmZ_fWhpaMikndMxa2e9nEdXnESwkt_dU6ZEMyt-7ADV2sn1ZjvZ_k7vkCoAGVyUfH_si5dRCcf_ZRj0hVgHEE6Vmm71l3ZU', start_index=21179)
Annotation(end_index=21191, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdbqWvngsOMlNFfHMpwfz8uV_1zKNvM2pqU-mJ5vAhKw2pIkOuuwoc_Aq1Vds2_de4DLsTFiksdIKc1s7dBBVRa-m4otkJq6-6fww2elK31de26Tr5sHQtvACu_kcE9tFaax8N3ciK03pms-BLxVoUJixL4GMak4txctU294K7mlTk_l43FTDj5TWkSOk2ecw91WHGK3TyYw==', start_index=21179)
Annotation(end_index=21686, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFf3bQtZn9u56efKNr2H8JkuAk_IVcUUJ8Q6-h2RQSslrYbfJfherKXkkZyS4UByycrlWA-zJRVC_bQ_CwDPiVoHV4juVd3ClqfdkBLHqr2VWUIuuwEKtYsh2rIIZHk9X0Slig7r_ccvfbGPQE=', start_index=21672)
Annotation(end_index=21686, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtaOoLLnQOeh7O4EqritSz0HyOsl3p_y3z4fsZDSbFpBarOePW52aJwcCZ1xcYxrOl_7HbUuaqmadFbkU5L9Ybom_1riHXbqImnPFd3W3Tzy6k1qPkjtrQa5u0i7m9DmHmyVL1C4BTUhyqwAadB-B5EaIVwjQ_Rg-afjHTXg==', start_index=21672)
Annotation(end_index=21860, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHq86Oo9t5pygnE-RJxajrMPtELlWPnHFk-w_bW0ZNk4SJFZVsoHfdy_mdSmCBGptI1OCW1P-QoStt05fC35Lim3dzRdz_OzPG_uRVBakgt3zTdMN1C3Cf2k4OydfLLHJ_iFQ==', start_index=21846)
Annotation(end_index=21860, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtaOoLLnQOeh7O4EqritSz0HyOsl3p_y3z4fsZDSbFpBarOePW52aJwcCZ1xcYxrOl_7HbUuaqmadFbkU5L9Ybom_1riHXbqImnPFd3W3Tzy6k1qPkjtrQa5u0i7m9DmHmyVL1C4BTUhyqwAadB-B5EaIVwjQ_Rg-afjHTXg==', start_index=21846)
Annotation(end_index=22317, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-n5CICFPCJPvbAQK9oR47hCd17H5DeK0iPo57gjO294qQH4WeywqRD6S-AjZBtQBheQNFpVna2XINYRRTcTixGhlCez_fyxzC4lgCYpNKHmnj4oRxreeuSh9AudYW56KSiA==', start_index=22308)
Annotation(end_index=22788, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQESi8ARuhJly1EzaRV338vjU1ZDFpBwi-5lUp3sV2WXrZ2odsJNXxKh25GpP0BN8ZZ2dAxGfdLSMFx36ympHUTZVeEKZCeTs32R5dCTCcJ3DNAlVEJz2QSyp5AMWVli8pWXdjo8Psqrbw_H_QWVRgCqy5il8ytrxYQdDMylVjbUmg3KRBnU1PkJGZZwm3GYF31NV107wFaGrEvbiSdj-LJPZqXAbJGbcTTXVD2noKSX1sJZsr9i70wkoXbrGsDA==', start_index=22778)
Annotation(end_index=23053, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfNwfHjDobuOg-9dgu4IjIMbV4zNyoJKbgBvQmC5TTnLNm20mIVdYRjbBYLie3CxCEXMoVvnlA29Dps8yyOWzIOk3enmqretsxxC96wrP7U5H1nRxYexX8bb1bFyGGnXucYM3PlKroPdZgwQ==', start_index=23043)
Annotation(end_index=24538, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdbqWvngsOMlNFfHMpwfz8uV_1zKNvM2pqU-mJ5vAhKw2pIkOuuwoc_Aq1Vds2_de4DLsTFiksdIKc1s7dBBVRa-m4otkJq6-6fww2elK31de26Tr5sHQtvACu_kcE9tFaax8N3ciK03pms-BLxVoUJixL4GMak4txctU294K7mlTk_l43FTDj5TWkSOk2ecw91WHGK3TyYw==', start_index=24529)
Annotation(end_index=24659, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdbqWvngsOMlNFfHMpwfz8uV_1zKNvM2pqU-mJ5vAhKw2pIkOuuwoc_Aq1Vds2_de4DLsTFiksdIKc1s7dBBVRa-m4otkJq6-6fww2elK31de26Tr5sHQtvACu_kcE9tFaax8N3ciK03pms-BLxVoUJixL4GMak4txctU294K7mlTk_l43FTDj5TWkSOk2ecw91WHGK3TyYw==', start_index=24650)
Annotation(end_index=24669, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExY5duGG9aGFCgtkx9op1-E7cd2qRoUCoAtBpE-ZaqclZT9LjufmZ_fWhpaMikndMxa2e9nEdXnESwkt_dU6ZEMyt-7ADV2sn1ZjvZ_k7vkCoAGVyUfH_si5dRCcf_ZRj0hVgHEE6Vmm71l3ZU', start_index=24660)
Annotation(end_index=24769, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExY5duGG9aGFCgtkx9op1-E7cd2qRoUCoAtBpE-ZaqclZT9LjufmZ_fWhpaMikndMxa2e9nEdXnESwkt_dU6ZEMyt-7ADV2sn1ZjvZ_k7vkCoAGVyUfH_si5dRCcf_ZRj0hVgHEE6Vmm71l3ZU', start_index=24757)
Annotation(end_index=24769, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdbqWvngsOMlNFfHMpwfz8uV_1zKNvM2pqU-mJ5vAhKw2pIkOuuwoc_Aq1Vds2_de4DLsTFiksdIKc1s7dBBVRa-m4otkJq6-6fww2elK31de26Tr5sHQtvACu_kcE9tFaax8N3ciK03pms-BLxVoUJixL4GMak4txctU294K7mlTk_l43FTDj5TWkSOk2ecw91WHGK3TyYw==', start_index=24757)
Annotation(end_index=24779, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-n5CICFPCJPvbAQK9oR47hCd17H5DeK0iPo57gjO294qQH4WeywqRD6S-AjZBtQBheQNFpVna2XINYRRTcTixGhlCez_fyxzC4lgCYpNKHmnj4oRxreeuSh9AudYW56KSiA==', start_index=24770)
Annotation(end_index=24855, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-n5CICFPCJPvbAQK9oR47hCd17H5DeK0iPo57gjO294qQH4WeywqRD6S-AjZBtQBheQNFpVna2XINYRRTcTixGhlCez_fyxzC4lgCYpNKHmnj4oRxreeuSh9AudYW56KSiA==', start_index=24846)
Annotation(end_index=24866, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4Hnthi65f5Q9Ywv0il0_M1s9GSpMxaHqu1MriztfVAdNA4dC4pVe-0dw2xD58TebyPBJG1DPEa3VU_mDBhImsZe37IOboNXa1WvABBoutkvqgcOLtTeIJ9a4-2AtDJB4vgITIwU4wrkFXABMJeskdON8jg1rKeWg9pCF67lupdEI7sFQFRV3frBm9RNSM4DVIUYbNsE0kAwbCC9X8gm6JMo_uo3WtGSmvk0JqXotdj-FJCS52QuMpHy7__ufYmM7Fsgz_6lcIMImRxw==', start_index=24856)
Annotation(end_index=24955, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4Hnthi65f5Q9Ywv0il0_M1s9GSpMxaHqu1MriztfVAdNA4dC4pVe-0dw2xD58TebyPBJG1DPEa3VU_mDBhImsZe37IOboNXa1WvABBoutkvqgcOLtTeIJ9a4-2AtDJB4vgITIwU4wrkFXABMJeskdON8jg1rKeWg9pCF67lupdEI7sFQFRV3frBm9RNSM4DVIUYbNsE0kAwbCC9X8gm6JMo_uo3WtGSmvk0JqXotdj-FJCS52QuMpHy7__ufYmM7Fsgz_6lcIMImRxw==', start_index=24945)
Annotation(end_index=24966, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOaQUAzpJ0PK0gyeqo2Km5dQ2nVYG2NKEZ1-LxWIaoAL6aqPhFPpy91u-2LZCbyeg6RCHhsu7d8RBldhryMLSIpE49GDwgcEqpgkQVwzYSAG_-GQEOHCSLmTdd15xllmVkM_mykmgkZP4nK4zS7IBFDo61jndxzJ-RHOgjyihx5Ux2J7DqHte6z_5u4ODz9hQTKEPXRfHV025F9VvFia8foBEBaCyhF_nk6W51ew==', start_index=24956)
Annotation(end_index=25072, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOaQUAzpJ0PK0gyeqo2Km5dQ2nVYG2NKEZ1-LxWIaoAL6aqPhFPpy91u-2LZCbyeg6RCHhsu7d8RBldhryMLSIpE49GDwgcEqpgkQVwzYSAG_-GQEOHCSLmTdd15xllmVkM_mykmgkZP4nK4zS7IBFDo61jndxzJ-RHOgjyihx5Ux2J7DqHte6z_5u4ODz9hQTKEPXRfHV025F9VvFia8foBEBaCyhF_nk6W51ew==', start_index=25062)
Annotation(end_index=25083, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEloVB9DZx4h1AEB7bh4rjMgj8WDMCFnDZHQvx1clcNOkHJHMYkgkYyzzGTrIFkgCTaf6bx_wKOBVkbk2dq9KIS3qbvKoTbBJeGdStI0iDCiGOBLKFtPGYJ74ZAW4gzYbb0LZhbrhJu', start_index=25073)
Annotation(end_index=25178, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEloVB9DZx4h1AEB7bh4rjMgj8WDMCFnDZHQvx1clcNOkHJHMYkgkYyzzGTrIFkgCTaf6bx_wKOBVkbk2dq9KIS3qbvKoTbBJeGdStI0iDCiGOBLKFtPGYJ74ZAW4gzYbb0LZhbrhJu', start_index=25164)
Annotation(end_index=25178, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOaQUAzpJ0PK0gyeqo2Km5dQ2nVYG2NKEZ1-LxWIaoAL6aqPhFPpy91u-2LZCbyeg6RCHhsu7d8RBldhryMLSIpE49GDwgcEqpgkQVwzYSAG_-GQEOHCSLmTdd15xllmVkM_mykmgkZP4nK4zS7IBFDo61jndxzJ-RHOgjyihx5Ux2J7DqHte6z_5u4ODz9hQTKEPXRfHV025F9VvFia8foBEBaCyhF_nk6W51ew==', start_index=25164)
Annotation(end_index=25189, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfGvMwp8jTiOIm2IEiMj5zw0hj_HkAdzIWSCPvXCaPpWah_EMMnX0FIQEJq8IE_aZ29_qH_R7XUoDvlMYKq5FrXvfYbRMY_6FKxlYpTILjt7rYPa_bXSBA_Uxem6QV', start_index=25179)
Annotation(end_index=25258, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfGvMwp8jTiOIm2IEiMj5zw0hj_HkAdzIWSCPvXCaPpWah_EMMnX0FIQEJq8IE_aZ29_qH_R7XUoDvlMYKq5FrXvfYbRMY_6FKxlYpTILjt7rYPa_bXSBA_Uxem6QV', start_index=25248)
Annotation(end_index=25268, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCl0bZHYljB2BTv7LFqXTOSdMZqNj_nQ2ZxH8eK0oyH_LkG_o9cS4HWlpY4y9dJq8u8tZqlntjsV0L8D0bcgvKUe1rZv4UqE2KpL8ZClpB06IkpERtjYpQVOuG_1gAnQd-YyqFbJKeOlDOWUUPye-sAjIsYnUb-Hfo8ptnXT0Tn2BGs0gkDO1OTtZ7JkynCmib3pOghd9G9mA8FeMQNMXLPBFQs9ZkLCHy', start_index=25259)
Annotation(end_index=25353, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCl0bZHYljB2BTv7LFqXTOSdMZqNj_nQ2ZxH8eK0oyH_LkG_o9cS4HWlpY4y9dJq8u8tZqlntjsV0L8D0bcgvKUe1rZv4UqE2KpL8ZClpB06IkpERtjYpQVOuG_1gAnQd-YyqFbJKeOlDOWUUPye-sAjIsYnUb-Hfo8ptnXT0Tn2BGs0gkDO1OTtZ7JkynCmib3pOghd9G9mA8FeMQNMXLPBFQs9ZkLCHy', start_index=25344)
Annotation(end_index=25364, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtaOoLLnQOeh7O4EqritSz0HyOsl3p_y3z4fsZDSbFpBarOePW52aJwcCZ1xcYxrOl_7HbUuaqmadFbkU5L9Ybom_1riHXbqImnPFd3W3Tzy6k1qPkjtrQa5u0i7m9DmHmyVL1C4BTUhyqwAadB-B5EaIVwjQ_Rg-afjHTXg==', start_index=25354)
Annotation(end_index=25446, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHq86Oo9t5pygnE-RJxajrMPtELlWPnHFk-w_bW0ZNk4SJFZVsoHfdy_mdSmCBGptI1OCW1P-QoStt05fC35Lim3dzRdz_OzPG_uRVBakgt3zTdMN1C3Cf2k4OydfLLHJ_iFQ==', start_index=25432)
Annotation(end_index=25446, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtaOoLLnQOeh7O4EqritSz0HyOsl3p_y3z4fsZDSbFpBarOePW52aJwcCZ1xcYxrOl_7HbUuaqmadFbkU5L9Ybom_1riHXbqImnPFd3W3Tzy6k1qPkjtrQa5u0i7m9DmHmyVL1C4BTUhyqwAadB-B5EaIVwjQ_Rg-afjHTXg==', start_index=25432)
Annotation(end_index=25457, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtyOoDFinTrir1b2TbZj8dbyEogkWIaeopX90mOV7G9HVqhlLEpQXaSjYy7_4lIcz-LKqyvfjz8abZ8xXvOYhZuVVqc2KzBm9psOtYezebkMvINPROyeJsdeGXsfdCE_VH2dGuy94=', start_index=25447)
Annotation(end_index=25540, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtyOoDFinTrir1b2TbZj8dbyEogkWIaeopX90mOV7G9HVqhlLEpQXaSjYy7_4lIcz-LKqyvfjz8abZ8xXvOYhZuVVqc2KzBm9psOtYezebkMvINPROyeJsdeGXsfdCE_VH2dGuy94=', start_index=25526)
Annotation(end_index=25540, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFBXE9LwAsyslEYF7tDql_qufbMubk-lYR_lrbZGmnMLW7-IgMNhv-zuwg9WgFQxSJywS24t1u2acIpZ2cX_K--UipKoDXOqbBOKOztlvtdYfU7JWzsENNbQiBNmMlgV31-l6ti7JJrcCme3IvBs9uVBpZvvs7Pn3EvHqZXdg=', start_index=25526)
Annotation(end_index=25551, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4kNIs99xS7PpdMMgzhKJMBh-WsspZItacynW-nTCtmhdbAC-ttwRLR2MlhxsDrWBK4RFTR1a3IcyahcuHzRWEjIkH125-mGUG_nv_wpVchoThs-EjCh2p1mm1PzBm', start_index=25541)
Annotation(end_index=25645, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4kNIs99xS7PpdMMgzhKJMBh-WsspZItacynW-nTCtmhdbAC-ttwRLR2MlhxsDrWBK4RFTR1a3IcyahcuHzRWEjIkH125-mGUG_nv_wpVchoThs-EjCh2p1mm1PzBm', start_index=25631)
Annotation(end_index=25645, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUUYX_v0yAVyr9M3GFNUgjDopf_CfpZ5cwy7fYoiahrCkX41kElFvrCMnf0eHGQ5B6hVkGipfdRm2QbicDcX4N3f6tQiAaCvjFIhHbRRzsSqfgaNJ7LcsgoV9QMUhoPG21mmly_Qehz-qp1wtREKNVZzQl_ifVeNNEmqy3a_bp1NSsXyZDyLRIIyQw79QW_DSvG_TxqFIThGndc5XGsuHDlELcxsa-Uqf-lrctRugnUll89E8oaFTOwQylm6_wVn1wnwHBlg1lDlNrew==', start_index=25631)
Annotation(end_index=25656, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFBXE9LwAsyslEYF7tDql_qufbMubk-lYR_lrbZGmnMLW7-IgMNhv-zuwg9WgFQxSJywS24t1u2acIpZ2cX_K--UipKoDXOqbBOKOztlvtdYfU7JWzsENNbQiBNmMlgV31-l6ti7JJrcCme3IvBs9uVBpZvvs7Pn3EvHqZXdg=', start_index=25646)
Annotation(end_index=25725, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFBXE9LwAsyslEYF7tDql_qufbMubk-lYR_lrbZGmnMLW7-IgMNhv-zuwg9WgFQxSJywS24t1u2acIpZ2cX_K--UipKoDXOqbBOKOztlvtdYfU7JWzsENNbQiBNmMlgV31-l6ti7JJrcCme3IvBs9uVBpZvvs7Pn3EvHqZXdg=', start_index=25715)
Annotation(end_index=25736, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHq86Oo9t5pygnE-RJxajrMPtELlWPnHFk-w_bW0ZNk4SJFZVsoHfdy_mdSmCBGptI1OCW1P-QoStt05fC35Lim3dzRdz_OzPG_uRVBakgt3zTdMN1C3Cf2k4OydfLLHJ_iFQ==', start_index=25726)
Annotation(end_index=25803, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHq86Oo9t5pygnE-RJxajrMPtELlWPnHFk-w_bW0ZNk4SJFZVsoHfdy_mdSmCBGptI1OCW1P-QoStt05fC35Lim3dzRdz_OzPG_uRVBakgt3zTdMN1C3Cf2k4OydfLLHJ_iFQ==', start_index=25793)
Annotation(end_index=25813, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdbqWvngsOMlNFfHMpwfz8uV_1zKNvM2pqU-mJ5vAhKw2pIkOuuwoc_Aq1Vds2_de4DLsTFiksdIKc1s7dBBVRa-m4otkJq6-6fww2elK31de26Tr5sHQtvACu_kcE9tFaax8N3ciK03pms-BLxVoUJixL4GMak4txctU294K7mlTk_l43FTDj5TWkSOk2ecw91WHGK3TyYw==', start_index=25804)
Annotation(end_index=25891, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdbqWvngsOMlNFfHMpwfz8uV_1zKNvM2pqU-mJ5vAhKw2pIkOuuwoc_Aq1Vds2_de4DLsTFiksdIKc1s7dBBVRa-m4otkJq6-6fww2elK31de26Tr5sHQtvACu_kcE9tFaax8N3ciK03pms-BLxVoUJixL4GMak4txctU294K7mlTk_l43FTDj5TWkSOk2ecw91WHGK3TyYw==', start_index=25882)
Annotation(end_index=25902, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9Mlnj2ZAQzpOzxVDDmmnyI2Bpq_4rERy5uQ82XpYS4chILRDR-ckqbCGLI8kfZxkDOy1h_A7X7xjf6PB_g5hujLU_ZlcFQcFV9Hny626g2qmErD95WXdIL0mIiytI4IE=', start_index=25892)
Annotation(end_index=25974, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9Mlnj2ZAQzpOzxVDDmmnyI2Bpq_4rERy5uQ82XpYS4chILRDR-ckqbCGLI8kfZxkDOy1h_A7X7xjf6PB_g5hujLU_ZlcFQcFV9Hny626g2qmErD95WXdIL0mIiytI4IE=', start_index=25964)
Annotation(end_index=25985, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIUITSQQuFrrG6LO6cmIFQBbeSImfh-TRQcrWyjo980qnx0vdFbC6_vDb07HLao4502Xvr1L7ITqFiMwoRmo4ZJyAJosfb9rZVjl8S451LXl7Fxkpn-AN2fdNnCjFQoqtzhaZgjyE=', start_index=25975)
Annotation(end_index=26092, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIUITSQQuFrrG6LO6cmIFQBbeSImfh-TRQcrWyjo980qnx0vdFbC6_vDb07HLao4502Xvr1L7ITqFiMwoRmo4ZJyAJosfb9rZVjl8S451LXl7Fxkpn-AN2fdNnCjFQoqtzhaZgjyE=', start_index=26082)
Annotation(end_index=26103, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0cLsGfV_qgUET0d7kbYua-eRVJ19aOIKYQJC684xDadqGOVhbSpNLOx81W-_tcrFZRxgzwVKA4HWi3rbtslmIKRUo_1ivzT4-JVtOsvkDlK5ICAe8KGpb1Zti78KbDQ3kewlN2A==', start_index=26093)
Annotation(end_index=26172, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0fI0s_0jmfqnekyQn6VnTjf1j4F0G-uM4QSr2tAazLXppbNRbuLaOOGTjkK5q_vlwXGB5AINknsQ5TdutlMA-GXCJTZ2sO9dhSouvkKbt0kR3mHMxD6rztjSXj5fDx3qt9y0Hgg==', start_index=26158)
Annotation(end_index=26172, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0cLsGfV_qgUET0d7kbYua-eRVJ19aOIKYQJC684xDadqGOVhbSpNLOx81W-_tcrFZRxgzwVKA4HWi3rbtslmIKRUo_1ivzT4-JVtOsvkDlK5ICAe8KGpb1Zti78KbDQ3kewlN2A==', start_index=26158)
Annotation(end_index=26183, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUUYX_v0yAVyr9M3GFNUgjDopf_CfpZ5cwy7fYoiahrCkX41kElFvrCMnf0eHGQ5B6hVkGipfdRm2QbicDcX4N3f6tQiAaCvjFIhHbRRzsSqfgaNJ7LcsgoV9QMUhoPG21mmly_Qehz-qp1wtREKNVZzQl_ifVeNNEmqy3a_bp1NSsXyZDyLRIIyQw79QW_DSvG_TxqFIThGndc5XGsuHDlELcxsa-Uqf-lrctRugnUll89E8oaFTOwQylm6_wVn1wnwHBlg1lDlNrew==', start_index=26173)
Annotation(end_index=26266, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUUYX_v0yAVyr9M3GFNUgjDopf_CfpZ5cwy7fYoiahrCkX41kElFvrCMnf0eHGQ5B6hVkGipfdRm2QbicDcX4N3f6tQiAaCvjFIhHbRRzsSqfgaNJ7LcsgoV9QMUhoPG21mmly_Qehz-qp1wtREKNVZzQl_ifVeNNEmqy3a_bp1NSsXyZDyLRIIyQw79QW_DSvG_TxqFIThGndc5XGsuHDlELcxsa-Uqf-lrctRugnUll89E8oaFTOwQylm6_wVn1wnwHBlg1lDlNrew==', start_index=26256)
Annotation(end_index=26277, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFE8NTExaasRDx4ybpn1DL5f4KQRcoq5UXVqvMYWaboQAHau9NEp1KDKKvb9haBWJjm915IbxUGTtWFR7ZhUrtMA-IwsFpIdwB8GTnEpEwvoiJFOTQHW5TKHpzAIzIVRBbqFH8tiw==', start_index=26267)
Annotation(end_index=26364, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBUmcjUR3O2J_zxDQE16VAttss9nO8wa4PjovztP2eQnb0kk9xTHiqQ1_2XxynOaQrShjsd6AWAABtoo5PaBVt5r81sJ5T5lX4Bjfw-GaYjWwkGL0srD75ELkgrZc=', start_index=26350)
Annotation(end_index=26364, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFE8NTExaasRDx4ybpn1DL5f4KQRcoq5UXVqvMYWaboQAHau9NEp1KDKKvb9haBWJjm915IbxUGTtWFR7ZhUrtMA-IwsFpIdwB8GTnEpEwvoiJFOTQHW5TKHpzAIzIVRBbqFH8tiw==', start_index=26350)
Annotation(end_index=26375, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtVPVz_6Se3gXMA-Z-r8jCGAXll8PoQxVQR1t3q-8-o-OyQZ3pX6k6T_zZ4S3OACkQU4DbEQ0-Kd6AqG9p0COxyEa3HbDSrCaI-WpbMYez_eJEZfmyeEGkjaG0BDLtxDe_5Q==', start_index=26365)
Annotation(end_index=26429, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtVPVz_6Se3gXMA-Z-r8jCGAXll8PoQxVQR1t3q-8-o-OyQZ3pX6k6T_zZ4S3OACkQU4DbEQ0-Kd6AqG9p0COxyEa3HbDSrCaI-WpbMYez_eJEZfmyeEGkjaG0BDLtxDe_5Q==', start_index=26419)
Annotation(end_index=26440, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_Yw5N0fcJHPPkMpVoKw4kc7rcj_34UsWFJg4wvAH2lnd3hyW1MtJAtoZSX1nFK-nEdWSOGaG-h9YBhq2BSwrO2OMfFZ9s6IKJQk2jWOWQvDeAzZn3GTqe8O2rmEdypzM7gxSA_JyU0INzIs5d_6bUlaRjeIx0MV3ER9mZQ90=', start_index=26430)
Annotation(end_index=26516, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_Yw5N0fcJHPPkMpVoKw4kc7rcj_34UsWFJg4wvAH2lnd3hyW1MtJAtoZSX1nFK-nEdWSOGaG-h9YBhq2BSwrO2OMfFZ9s6IKJQk2jWOWQvDeAzZn3GTqe8O2rmEdypzM7gxSA_JyU0INzIs5d_6bUlaRjeIx0MV3ER9mZQ90=', start_index=26506)
Annotation(end_index=26527, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBUmcjUR3O2J_zxDQE16VAttss9nO8wa4PjovztP2eQnb0kk9xTHiqQ1_2XxynOaQrShjsd6AWAABtoo5PaBVt5r81sJ5T5lX4Bjfw-GaYjWwkGL0srD75ELkgrZc=', start_index=26517)
Annotation(end_index=26579, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBUmcjUR3O2J_zxDQE16VAttss9nO8wa4PjovztP2eQnb0kk9xTHiqQ1_2XxynOaQrShjsd6AWAABtoo5PaBVt5r81sJ5T5lX4Bjfw-GaYjWwkGL0srD75ELkgrZc=', start_index=26569)
Annotation(end_index=26589, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVS6OD0MoEqgdZxty8WMrlCOYr8SVbbsg8lAh_nRVBJTH24ieFAzEESrzxV_r_uHd9sCTxQKxEe9oLcnhScHsgO2b2HxweOBrXlGnMzBGwmWl8DdZcCzIeu_3E7Gm25QRdcz1nPaFk_SNm44xMuVNi78ebZZIVaAo=', start_index=26580)
Annotation(end_index=26646, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFVS6OD0MoEqgdZxty8WMrlCOYr8SVbbsg8lAh_nRVBJTH24ieFAzEESrzxV_r_uHd9sCTxQKxEe9oLcnhScHsgO2b2HxweOBrXlGnMzBGwmWl8DdZcCzIeu_3E7Gm25QRdcz1nPaFk_SNm44xMuVNi78ebZZIVaAo=', start_index=26637)
Annotation(end_index=26656, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-n5CICFPCJPvbAQK9oR47hCd17H5DeK0iPo57gjO294qQH4WeywqRD6S-AjZBtQBheQNFpVna2XINYRRTcTixGhlCez_fyxzC4lgCYpNKHmnj4oRxreeuSh9AudYW56KSiA==', start_index=26647)
Annotation(end_index=26708, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-n5CICFPCJPvbAQK9oR47hCd17H5DeK0iPo57gjO294qQH4WeywqRD6S-AjZBtQBheQNFpVna2XINYRRTcTixGhlCez_fyxzC4lgCYpNKHmnj4oRxreeuSh9AudYW56KSiA==', start_index=26699)
Annotation(end_index=26718, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIyehVZ8diqh7NsvGhHopvzcmFJbM7gBnfzoNXT-3AKXoHQ4Z5CNlq2fH6x-dPLLErKDnimpNQ64ovItcFDigq2gswmQgdNHHXINA0yDMh_hOYh60AY2bultfUkyolGggn6XqrOyIsznNw_w==', start_index=26709)
Annotation(end_index=26773, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIyehVZ8diqh7NsvGhHopvzcmFJbM7gBnfzoNXT-3AKXoHQ4Z5CNlq2fH6x-dPLLErKDnimpNQ64ovItcFDigq2gswmQgdNHHXINA0yDMh_hOYh60AY2bultfUkyolGggn6XqrOyIsznNw_w==', start_index=26764)
Annotation(end_index=26784, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkyCmSW9Km845CYjKvbN3TPmQmmCQHA4y1AG8o85Z3fuLrqTkg60vMLlqcFq_8RzO9c1QzEoZSZEg4GYyoPfsYwnnADJRcPANtrQA1mNEdnKbjO4kiNCDQe6ZXIcmQs8SqgTABP-mLnfnlGZcCZ22Z65wmlpQ1eCoOaWjLfibeo2kYLPDjFZgKxnFueWyak3Z2b153QX5FivwPILwugYPSYxwuoDyNjFXklhU=', start_index=26774)
Annotation(end_index=26848, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkyCmSW9Km845CYjKvbN3TPmQmmCQHA4y1AG8o85Z3fuLrqTkg60vMLlqcFq_8RzO9c1QzEoZSZEg4GYyoPfsYwnnADJRcPANtrQA1mNEdnKbjO4kiNCDQe6ZXIcmQs8SqgTABP-mLnfnlGZcCZ22Z65wmlpQ1eCoOaWjLfibeo2kYLPDjFZgKxnFueWyak3Z2b153QX5FivwPILwugYPSYxwuoDyNjFXklhU=', start_index=26838)
Annotation(end_index=26858, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdbqWvngsOMlNFfHMpwfz8uV_1zKNvM2pqU-mJ5vAhKw2pIkOuuwoc_Aq1Vds2_de4DLsTFiksdIKc1s7dBBVRa-m4otkJq6-6fww2elK31de26Tr5sHQtvACu_kcE9tFaax8N3ciK03pms-BLxVoUJixL4GMak4txctU294K7mlTk_l43FTDj5TWkSOk2ecw91WHGK3TyYw==', start_index=26849)
Annotation(end_index=26971, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdbqWvngsOMlNFfHMpwfz8uV_1zKNvM2pqU-mJ5vAhKw2pIkOuuwoc_Aq1Vds2_de4DLsTFiksdIKc1s7dBBVRa-m4otkJq6-6fww2elK31de26Tr5sHQtvACu_kcE9tFaax8N3ciK03pms-BLxVoUJixL4GMak4txctU294K7mlTk_l43FTDj5TWkSOk2ecw91WHGK3TyYw==', start_index=26962)
Annotation(end_index=26982, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHq86Oo9t5pygnE-RJxajrMPtELlWPnHFk-w_bW0ZNk4SJFZVsoHfdy_mdSmCBGptI1OCW1P-QoStt05fC35Lim3dzRdz_OzPG_uRVBakgt3zTdMN1C3Cf2k4OydfLLHJ_iFQ==', start_index=26972)
Annotation(end_index=27068, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHq86Oo9t5pygnE-RJxajrMPtELlWPnHFk-w_bW0ZNk4SJFZVsoHfdy_mdSmCBGptI1OCW1P-QoStt05fC35Lim3dzRdz_OzPG_uRVBakgt3zTdMN1C3Cf2k4OydfLLHJ_iFQ==', start_index=27058)
Annotation(end_index=27079, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOaQUAzpJ0PK0gyeqo2Km5dQ2nVYG2NKEZ1-LxWIaoAL6aqPhFPpy91u-2LZCbyeg6RCHhsu7d8RBldhryMLSIpE49GDwgcEqpgkQVwzYSAG_-GQEOHCSLmTdd15xllmVkM_mykmgkZP4nK4zS7IBFDo61jndxzJ-RHOgjyihx5Ux2J7DqHte6z_5u4ODz9hQTKEPXRfHV025F9VvFia8foBEBaCyhF_nk6W51ew==', start_index=27069)
Annotation(end_index=27145, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOaQUAzpJ0PK0gyeqo2Km5dQ2nVYG2NKEZ1-LxWIaoAL6aqPhFPpy91u-2LZCbyeg6RCHhsu7d8RBldhryMLSIpE49GDwgcEqpgkQVwzYSAG_-GQEOHCSLmTdd15xllmVkM_mykmgkZP4nK4zS7IBFDo61jndxzJ-RHOgjyihx5Ux2J7DqHte6z_5u4ODz9hQTKEPXRfHV025F9VvFia8foBEBaCyhF_nk6W51ew==', start_index=27135)
Annotation(end_index=27155, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUz25xJYlZ3pyjThXJ8dZD7P0c8_W7HGeAuBlmmd06dcsigxbBNTtaobUoaZDUvck8ImwssnZGsb2_yAPaiWuPEOy26sJVXOd6B_Vhq-rgaKB18mEww2ZPmm1EGDHXUjVSoNfJgRg=', start_index=27146)
Annotation(end_index=27219, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUz25xJYlZ3pyjThXJ8dZD7P0c8_W7HGeAuBlmmd06dcsigxbBNTtaobUoaZDUvck8ImwssnZGsb2_yAPaiWuPEOy26sJVXOd6B_Vhq-rgaKB18mEww2ZPmm1EGDHXUjVSoNfJgRg=', start_index=27210)
Annotation(end_index=27229, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrOLUi9jJPEae5f8KpvjgkaudHyEiFy7d8NYADMI2AuxmmT6iXBSpZY9mTbd8IvsTXZUg88HJc69X9bPBVxr8TGpKBd6nyUe6aovrcqh0K9NDuls5-qVwG-C1Nlq-TgfgM875hVes0_mUbBxqVgIWPwA9UOjYvs1Ho6hD0SOsyHfMzJYncgKHYAVjDf8a9B-Rb', start_index=27220)
Annotation(end_index=27296, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrOLUi9jJPEae5f8KpvjgkaudHyEiFy7d8NYADMI2AuxmmT6iXBSpZY9mTbd8IvsTXZUg88HJc69X9bPBVxr8TGpKBd6nyUe6aovrcqh0K9NDuls5-qVwG-C1Nlq-TgfgM875hVes0_mUbBxqVgIWPwA9UOjYvs1Ho6hD0SOsyHfMzJYncgKHYAVjDf8a9B-Rb', start_index=27287)
Annotation(end_index=27306, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCQASWikPK8qskTyeIrV1g3arBlVxL1npT0Yi1RLIL8_Ohb0suu92pnfbYs9bq1nnC4DFdRO-0CvHER26V4CNXK-5Z2HpEkJuSPmjr1Xx17QJLFVJiX56RbweTJHQa7yM=', start_index=27297)
Annotation(end_index=27359, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCQASWikPK8qskTyeIrV1g3arBlVxL1npT0Yi1RLIL8_Ohb0suu92pnfbYs9bq1nnC4DFdRO-0CvHER26V4CNXK-5Z2HpEkJuSPmjr1Xx17QJLFVJiX56RbweTJHQa7yM=', start_index=27350)
Annotation(end_index=27370, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0fI0s_0jmfqnekyQn6VnTjf1j4F0G-uM4QSr2tAazLXppbNRbuLaOOGTjkK5q_vlwXGB5AINknsQ5TdutlMA-GXCJTZ2sO9dhSouvkKbt0kR3mHMxD6rztjSXj5fDx3qt9y0Hgg==', start_index=27360)
Annotation(end_index=27431, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0fI0s_0jmfqnekyQn6VnTjf1j4F0G-uM4QSr2tAazLXppbNRbuLaOOGTjkK5q_vlwXGB5AINknsQ5TdutlMA-GXCJTZ2sO9dhSouvkKbt0kR3mHMxD6rztjSXj5fDx3qt9y0Hgg==', start_index=27421)
Annotation(end_index=27442, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQESi8ARuhJly1EzaRV338vjU1ZDFpBwi-5lUp3sV2WXrZ2odsJNXxKh25GpP0BN8ZZ2dAxGfdLSMFx36ympHUTZVeEKZCeTs32R5dCTCcJ3DNAlVEJz2QSyp5AMWVli8pWXdjo8Psqrbw_H_QWVRgCqy5il8ytrxYQdDMylVjbUmg3KRBnU1PkJGZZwm3GYF31NV107wFaGrEvbiSdj-LJPZqXAbJGbcTTXVD2noKSX1sJZsr9i70wkoXbrGsDA==', start_index=27432)
Annotation(end_index=27526, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQESi8ARuhJly1EzaRV338vjU1ZDFpBwi-5lUp3sV2WXrZ2odsJNXxKh25GpP0BN8ZZ2dAxGfdLSMFx36ympHUTZVeEKZCeTs32R5dCTCcJ3DNAlVEJz2QSyp5AMWVli8pWXdjo8Psqrbw_H_QWVRgCqy5il8ytrxYQdDMylVjbUmg3KRBnU1PkJGZZwm3GYF31NV107wFaGrEvbiSdj-LJPZqXAbJGbcTTXVD2noKSX1sJZsr9i70wkoXbrGsDA==', start_index=27516)
Annotation(end_index=27537, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEf7iuq130ZmuwzMMWi6PogS1WwNaXxX4Q7ZT421JDVZ-fz7WRhCIxxW2uVSi6vy_DlLQ-_RNk1Y3y8j1NV0-EIHq4nDFxb6hAq1NHJGpQgegHDNs0c4P1o6eEHddtAO2efdjLO9iMD0SrQ', start_index=27527)
Annotation(end_index=27596, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEf7iuq130ZmuwzMMWi6PogS1WwNaXxX4Q7ZT421JDVZ-fz7WRhCIxxW2uVSi6vy_DlLQ-_RNk1Y3y8j1NV0-EIHq4nDFxb6hAq1NHJGpQgegHDNs0c4P1o6eEHddtAO2efdjLO9iMD0SrQ', start_index=27586)
Annotation(end_index=27607, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAr8--YpwqQWw3E5EKlNzQtvY5wK4JOACaiqovfW4S_mw6-uQNM1bIVYJE4QYG-iI6fm5YVB8bY9EiaSr8AJaSXGUWajWN5CQ1ZBL7ffZfLHdc0ZMhVX0v6xpKu5LNIP_4N-OezLA=', start_index=27597)
Annotation(end_index=27664, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAr8--YpwqQWw3E5EKlNzQtvY5wK4JOACaiqovfW4S_mw6-uQNM1bIVYJE4QYG-iI6fm5YVB8bY9EiaSr8AJaSXGUWajWN5CQ1ZBL7ffZfLHdc0ZMhVX0v6xpKu5LNIP_4N-OezLA=', start_index=27654)
Annotation(end_index=27675, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMt2z3Dhksg-_S2jOqh3QogBDX6o8loNkh8ky_NYqswCX38l-YqBl2aCNSb2jY5Ez08clSeOH26a7Jd2g6_St5kU-UMvTUxjsVog8vosT_tst3JqFXBK5D1QNhEYXUB9j2NY3cZ-2gh070L0SI--qn7vy4I_W-O3HD1flOrzZBqTi6-stOrowjUssulIiP', start_index=27665)
Annotation(end_index=27739, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMt2z3Dhksg-_S2jOqh3QogBDX6o8loNkh8ky_NYqswCX38l-YqBl2aCNSb2jY5Ez08clSeOH26a7Jd2g6_St5kU-UMvTUxjsVog8vosT_tst3JqFXBK5D1QNhEYXUB9j2NY3cZ-2gh070L0SI--qn7vy4I_W-O3HD1flOrzZBqTi6-stOrowjUssulIiP', start_index=27729)
Annotation(end_index=27750, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfGvMwp8jTiOIm2IEiMj5zw0hj_HkAdzIWSCPvXCaPpWah_EMMnX0FIQEJq8IE_aZ29_qH_R7XUoDvlMYKq5FrXvfYbRMY_6FKxlYpTILjt7rYPa_bXSBA_Uxem6QV', start_index=27740)
Annotation(end_index=27816, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfGvMwp8jTiOIm2IEiMj5zw0hj_HkAdzIWSCPvXCaPpWah_EMMnX0FIQEJq8IE_aZ29_qH_R7XUoDvlMYKq5FrXvfYbRMY_6FKxlYpTILjt7rYPa_bXSBA_Uxem6QV', start_index=27806)
Annotation(end_index=27827, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfNwfHjDobuOg-9dgu4IjIMbV4zNyoJKbgBvQmC5TTnLNm20mIVdYRjbBYLie3CxCEXMoVvnlA29Dps8yyOWzIOk3enmqretsxxC96wrP7U5H1nRxYexX8bb1bFyGGnXucYM3PlKroPdZgwQ==', start_index=27817)
Annotation(end_index=27908, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfNwfHjDobuOg-9dgu4IjIMbV4zNyoJKbgBvQmC5TTnLNm20mIVdYRjbBYLie3CxCEXMoVvnlA29Dps8yyOWzIOk3enmqretsxxC96wrP7U5H1nRxYexX8bb1bFyGGnXucYM3PlKroPdZgwQ==', start_index=27898)
Annotation(end_index=27919, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFf3bQtZn9u56efKNr2H8JkuAk_IVcUUJ8Q6-h2RQSslrYbfJfherKXkkZyS4UByycrlWA-zJRVC_bQ_CwDPiVoHV4juVd3ClqfdkBLHqr2VWUIuuwEKtYsh2rIIZHk9X0Slig7r_ccvfbGPQE=', start_index=27909)
Annotation(end_index=28005, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFf3bQtZn9u56efKNr2H8JkuAk_IVcUUJ8Q6-h2RQSslrYbfJfherKXkkZyS4UByycrlWA-zJRVC_bQ_CwDPiVoHV4juVd3ClqfdkBLHqr2VWUIuuwEKtYsh2rIIZHk9X0Slig7r_ccvfbGPQE=', start_index=27995)

## Sources
