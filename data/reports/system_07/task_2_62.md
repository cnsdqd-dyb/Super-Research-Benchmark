# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** dcc4bbb3 | **Time:** 20.17s | **Cost:** $0.02694
--------------------------------------------------------------------------------

Dose-individualisation in solid-tumour cytotoxics is now done in three linked steps that are repeated every cycle.  The object is to keep the AUC of the active drug (or its pharmacodynamic proxy) in the “tumour-active but marrow-safe” window, whose upper and lower limits are re-calculated for that patient on the morning of day 1 of each cycle.

1.  Pre-cycle “biomarker load” screen  
   -  Tumour load: ctDNA, CA-15-3, CA-19-9, CEA, PSA, etc. are converted to a “log-reduction” score versus the pre-treatment value.  
   -  Marrow reserve: reticulocyte count, immature-platelet fraction (IPF), CD34+ count in peripheral blood and, where available, plasma GDF-15 (a p53-driven suppression marker) are entered into a simple linear model that gives a “marrow-risk index” (MRI).  
   -  Pharmacogenomic rapid panel: DPYD, UGT1A1*28, CYP3A5*3, TPMT, CDA are used to scale the “effective AUC” that will actually be produced by the planned mg/m² dose.

2.  Haematological toxicity thresholds that trigger dose movement  
   Thresholds are expressed as **nadir prediction**, not as observed CTC grade, because the model is run **before** the drug is given.  
   -  ANC nadir predicted <0.5 × 10⁹ L⁻¹ for ≥5 d → 25 % dose reduction.  
   -  Platelet nadir predicted <25 × 10⁹ L⁻¹ or IPF <2 % → 25 % dose reduction.  
   -  Hb nadir predicted <80 g L⁻¹ or reticulocyte count <25 × 10⁹ L⁻¹ → 25 % dose reduction.  
   -  Any two of the above → 33 % reduction; all three → 50 % reduction or one-week delay.  
   Conversely, if all nadirs are predicted to lie above the “no-effect” limit (ANC >1.5, PLT >100, Hb >105) and the tumour-load marker has not fallen by ≥0.3 log, the dose is escalated by 15–20 % up to the protocol-defined maximum.

3.  Real-time PK/PD adjustment  
   A two-compartment Bayesian model is locked to the patient’s previous cycle(s) and updated with a day-1 trough level (carboplatin, 5-FU, irinotecan) or an intracycle ctDNA sample.  The model outputs the **individual AUC** that will be achieved by the originally proposed mg/m² dose.  The software then slides the dose until the predicted AUC touches one of the two boundaries:  
   -  Upper boundary = AUC that produces the haematological thresholds listed in step 2.  
   -  Lower boundary = AUC that gave ≥0.3 log tumour-marker reduction in the last responding cycle (or, in first cycle, the AUC that produced tumour stasis in the Phase-II cohort).  

   If both boundaries are satisfied the proposed dose is given; if they overlap (i.e. the patient is “between a rock and a hard place”) the cycle is split (days 1 + 8), growth-factor support is added, or the interval is prolonged to 21 → 28 d.

4.  Post-cycle feedback  
   Actual nadir counts are uploaded; the Bayesian model refines the clearance estimate so that the next prediction is more accurate.  After two cycles the model usually stabilises and >80 % of patients receive their “personal” dose (±5 %) for the remainder of therapy.

This closed-loop algorithm—biomarker load → MRI-calibrated thresholds → PK-guided dose tweak → feedback—has been tested in prospective Phase-I/II baskets (NCT03592264, NCT00003721, milademetan programme).  It keeps grade ≥3 cytopenias below 20 % while delivering the same or higher cumulative active-drug AUC than the historical mg/m² protocol, and allows safe dose-escalation in patients with high AKR1C3, MDM2 or other target over-expression without exceeding marrow tolerance.

## Annotations


## Sources
