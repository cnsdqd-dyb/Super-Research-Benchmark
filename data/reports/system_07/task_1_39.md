# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 0c8ae579 | **Time:** 27.04s | **Cost:** $0.02860
--------------------------------------------------------------------------------

In preclinical oncology, the “therapeutic index” (TI) is simply the ratio  
**TI = Toxic dose (in animals) ÷ Effective dose (in animals).**  
The job of the screening cascade is to keep that number as large as possible while still hitting a biologically meaningful exposure in man.  
The balancing act is done in three tightly-coupled layers:

1. In-vitro “first-pass” triage  
2. Rodent efficacy / dose-finding  
3. Formal rodent & non-rodent toxicology  

Each layer supplies the numbers that go into the ratio, and each is used to re-write the decision criteria for the next.

--------------------------------------------------------
1. In-vitro layer – define the minimal pharmacological exposure
--------------------------------------------------------
- Potency: GI₅₀/IC₅₀ in a disease-relevant human cell panel (e.g. NCI-60, CellTiter-Glo, 3-D spheroids).  
- Mechanism assays: cell-cycle arrest, caspase-3, γ-H2AX, ROS, target occupancy, etc.  
- Off-target counter-screens: hERG, CYP inhibition, mitochondrial membrane potential, a panel of kinases/GPCRs.  
- Early cytotoxicity to “slow” normal cells (HDF, RPTEC, hepatocytes) gives a first idea of selectivity; the ratio  
  **IC₅₀ (normal cell) / IC₅₀ (tumor cell)** is the *in-vitro therapeutic index*.  
  Compounds with a ratio < 5 are usually dropped unless they show a clear exposure window *in vivo*.

These data fix the *lowest anticipated pharmacologically active concentration* (LOPAC) and the *cellular no-effect level* (cNEL) that will later be compared with plasma Cmax and AUC.

--------------------------------------------------------
2. Rodent pharmacology – turn potency into an *in-vivo* effective dose
--------------------------------------------------------
Mouse or rat xenograft/syngeneic models (sub-cutaneous, orthotopic, PDX, GEMM) are run with 3–5 dose levels.  
End-points: %TGI, regression, time-to-tumor-quadrupling, survival.  
PK is taken on day 1 and at steady-state; AUC₀₋₂₄ h and Cmax are recorded.

From these studies we obtain  
**ED₅₀/ED₉₀** (mg kg⁻¹ or µM·h AUC) that gives the chosen efficacy end-point.

--------------------------------------------------------
3. Rodent & non-rodent toxicology – define the first toxic dose
--------------------------------------------------------
- Acute (single-dose) in healthy mice → MTD or LD₁₀.  
- Repeat-dose (7-, 14-, 28-day) GLP studies in two species (one rodent, one non-rodent).  
- Dose-limiting toxicities (DLT) are graded (CTCAE); haematology, clinical chemistry, histopathology, ECG, ophthalmology recorded.  
- Exposure at the *highest non-severely toxic dose* (HNSTD) or *no-observed-adverse-effect level* (NOAEL) is measured as Cmax and AUC.

--------------------------------------------------------
Putting the numbers together – TI calculation
--------------------------------------------------------
Classical *dose-based* TI (small molecules)  
TI = MTD (mg kg⁻¹) ÷ ED₅₀ (mg kg⁻¹)

Exposure-based TI (biologics, ADCs, highly potent agents)  
TI = AUC (HNSTD) ÷ AUC (ED₉₀)

Acceptance benchmarks used in most pharma companies  
- Cytotoxic payloads: TI ≥ 4–5 (dose) or ≥10-fold AUC window  
- Cytostatic/targeted agents: TI ≥ 10 (dose) or ≥25-fold AUC window  
- ADCs: TI ≥ 5 *and* <5% free payload in circulation

--------------------------------------------------------
How the balance is *actively* managed
--------------------------------------------------------
1. If TI is borderline, the project team first tries to *push the toxic curve to the right*:  
   – re-formulate (nano-particle, liposome, pro-drug) to lower Cmax;  
   – change schedule (daily → weekly, continuous infusion, metronomic);  
   – add protective adjuvant (e.g. dexrazoxane for anthracyclines).

2. If toxicity is on-target (bone-marrow, gut) the *efficacy curve* can sometimes be moved to the left by biomarker-enriched models (e.g. BRC1-deficient PDX, HER2-amplified line) so that the same exposure gives more tumour kill, widening the TI *for that population*.

3. For agents that work at <1 mg kg⁻¹ (many ADCs, radioligands, degraders) exposure-based TI is the only meaningful metric; dose (mg kg⁻¹) can look “good” while the AUC window is tiny. Hence *systemic exposure multiples* (NOAEL AUC ÷ human-predicted AUC) are written into every IND-enabling package.

--------------------------------------------------------
Worked mini-example – Alternol (natural product)
--------------------------------------------------------
- In-vitro: GI₅₀ ≤ 5 µM in 83 % of NCI-60 lines; no cytotoxicity up to 50 µM in HDF.  
- Mouse xenograft: ED₅₀ tumour growth inhibition = 50 mg kg⁻¹ qd × 14.  
- Acute toxicity in healthy mice: MTD = 665 mg kg⁻¹.  
→ Dose-based TI = 665 / 50 ≈ **13.3**, above the ≥5 hurdle; project advanced.

--------------------------------------------------------
Take-home
--------------------------------------------------------
The therapeutic index is not a single measurement but a *decision tree* that moves from  
in-vitro selectivity → in-vivo rodent efficacy → GLP toxicology exposure.  
At every node the compound must deliver a pre-agreed *exposure window* (usually ≥5- to ≥10-fold) between the dose/exposure that first hurts the animal and the dose/exposure that reproducibly shrinks the tumour. If that window cannot be created by chemistry, formulation, schedule, or patient selection, the programme is halted before first-in-human studies.

## Annotations


## Sources
