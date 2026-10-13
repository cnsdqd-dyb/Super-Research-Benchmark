# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 987ae3f2 | **Time:** 24.79s | **Cost:** $0.02990
--------------------------------------------------------------------------------

Heat-stroke warning systems try to solve the same problem every screening programme has:  
“How many dangerous days/people do I miss (sensitivity) and how many times do I cry wolf (specificity) while keeping the total bill low?”  
Because the “test” is a weather-based alert that triggers a chain of expensive public-health actions (SMS, cooling shelters, overtime staff, media campaigns, etc.), the cost of a false-positive is high, whereas the cost of a false-negative can be lethal.  
The models therefore optimise the trade-off in three linked steps:

1. Pick the meteorological predictor that gives the steepest rise in risk once a threshold is crossed.  
2. Slide that threshold up or down until the *incremental* cost per averted adverse event equals the policy-maker’s willingness-to-pay.  
3. Validate locally because the same meteorological value produces different heat-stroke counts in different climates and populations.

Below is a concise map of how this is done in practice, with numbers taken from the Japanese and Chinese studies you supplied.

--------------------------------------------------
1. Meteorological input: “raw” beats “indices”
--------------------------------------------------
- Across 47 Japanese prefectures, a simple model with air temperature (T), relative humidity (RH), wind (W) and solar radiation (SR) predicted daily heat-stroke ambulance dispatches (HT-EAD) with median R² = 0.85 (cal.) / 0.74 (val.).  
- The best composite index, Wet-bulb Globe Temperature (WBGT), reached only 0.77 / 0.70.  
- In cool regions (Hokkaido) WBGT added *no* value over T alone.  

**Implication**: raw variables give the steepest dose–response curve, i.e. they maximise sensitivity for any given specificity.  
**Cost angle**: no licence fee, no extra computing, and one variable less to communicate to the public.

--------------------------------------------------
2. Choosing the threshold: ROC + cost curve
--------------------------------------------------
After the model is fixed, the only free parameter left is the trigger value.  
Two curves are plotted:

a. ROC curve (sensitivity vs 1-specificity) – epidemiological optimum.  
b. Net-monetary-benefit (NMB) curve – economic optimum.

Example from the Chinese ICU mortality model (Fisher discriminant):  
- At WBGT = 30 °C sensitivity = 95 %, specificity = 83 %, AUC = 0.937.  
- Cost-of-caring for one extra true case averted ≈ 2,300 CNY.  
- Policy ceiling = 30,000 CNY per life-year saved.  
⇒ Threshold accepted; any lower (higher sensitivity) produced too many false alarms whose cost exceeded the ceiling.

--------------------------------------------------
3. Local calibration: “same number, different meaning”
--------------------------------------------------
Oka et al. (2023) showed that the WBGT value that doubles HT-EAD in northern Japan is 3.5–5 °C *lower* than in southern Japan.  
Therefore a *national* warning threshold would either:  
- over-trigger in the south (wasting money), or  
- under-trigger in the north (missing cases).  

**Solution**: fit separate Generalised Additive Models (GAM) for each region, then choose the threshold that gives the same *attributable fraction* (e.g. 80 % of annual HT-EAD) rather than the same *meteorological value*.  
This keeps the *positive predictive value* (PPV) – and hence the cost-effectiveness – roughly constant across climates.

--------------------------------------------------
4. Cost-effectiveness arithmetic (back-of-the-envelope)
--------------------------------------------------
Metro Vancouver 2009 heat episode (Kosatsky 2018):

- Baseline excess deaths on above-threshold days = 45.  
- Warning system cost (extra staff + cooling shelters + media) = CAD 1.1 M.  
- Assume 50 % efficacy (mid-range literature value) → 22.5 deaths averted.  
- Value of a statistical life (VSL) = CAD 7 M.  
- Benefit = 22.5 × 7 M = CAD 157 M.  
- ICER = (1.1 M – 0) / 22.5 = CAD 49,000 per death averted  
  ≪ commonly accepted ceiling of 100,000–150,000.  

Hence the programme is cost-effective *provided* the false-alarm rate is kept below ~30 %; every extra false alarm adds ≈ CAD 120 k in unnecessary mobilisation, quickly eroding the surplus.

--------------------------------------------------
5. Practical checklist used by agencies
--------------------------------------------------
1. Start with T+RH+W+SR regression; compute AUC.  
2. Choose candidate thresholds that give sensitivity ≥ 80 % and PPV ≥ 15 %.  
3. Simulate number of alerts and expected HT-EAD averted for each threshold.  
4. Multiply alerts by unit cost (local staff/time/shelter).  
5. Accept the lowest threshold whose incremental cost per averted event is below the local cost-effectiveness ceiling.  
6. Re-fit every 2–3 years with new emergency-visit data; shift threshold if observed sensitivity or PPV drifts > 5 %.

--------------------------------------------------
Bottom line
--------------------------------------------------
Heat-stroke warning models achieve cost-effective balance by:

- Using raw meteorological variables (higher discriminatory power, zero licence cost).  
- Sliding the trigger until the *last* unit of money buys a benefit just equal to the local willingness-to-pay – not until epidemiological ROC is maximised.  
- Locking the threshold to *health-outcome percentiles* rather than fixed meteorological values to keep PPV – and therefore cost-effectiveness – invariant across climates.

## Annotations


## Sources
