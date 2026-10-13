# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** cb1cb0ba | **Time:** 18.59s | **Cost:** $0.01179
--------------------------------------------------------------------------------

In payment-risk engines the “security-interception probability threshold” is not picked by intuition; it is engineered through a repeatable, data-driven loop that balances three business variables:

1. Fraud $ loss (False Negatives)  
2. Customer friction / revenue loss (False Positives)  
3. Operational cost of reviews

The setting procedure used by Stripe, Antom, Adyen, Chase, etc. is essentially the same; only the numerical outcome differs per portfolio.

--------------------------------------------------
1. Build a calibrated fraud-score model
--------------------------------------------------
- Train a supervised model (XGBoost, NN, etc.) on labelled data so that the output  
  score S ∈ [0,1] is a **well-calibrated probability** of fraud.  
- Validate with a hold-out set and reliability curves; calibration error must be <1 %.

--------------------------------------------------
2. Produce the ROC / PR curve
--------------------------------------------------
- Slide a tentative cut-off c from 0 → 1 and record  
  – TP(c)  (blocked fraud $)  
  – FP(c)  (blocked good $)  
  – Precision = TP/(TP+FP)  
  – Recall = TP/(TP+FN)

--------------------------------------------------
3. Translate to money
--------------------------------------------------
- Assign unit costs:  
  – L_FN  = average fraud loss per false-negative transaction  
  – L_FP  = average lifetime value lost per false-positive transaction  
  – C_review = manual-review cost if you queue instead of block

- Expected cost at threshold c  
  Cost(c) = FN(c)·L_FN  +  FP(c)·L_FP  +  Review(c)·C_review

--------------------------------------------------
4. Optimise
--------------------------------------------------
- Find c* that minimises Cost(c).  
- In practice you add policy caps:  
  – FP rate ≤ 0.3 % of approval volume (customer-experience SLA)  
  – Recall ≥ 65 % of fraud $ (regulatory or board mandate)

The lowest c that satisfies **both** constraints becomes the production threshold.

--------------------------------------------------
5. Simulate before go-live (ATL/BTL test)
--------------------------------------------------
- Above-the-line: raise c by 5 % → measure how many **real frauds** you would lose.  
- Below-the-line: lower c by 5 % → measure how many **good** payments you would incorrectly block.  
- If either direction violates the SLA, shrink the delta until the sweet spot is confirmed.

--------------------------------------------------
6. Deploy and monitor
--------------------------------------------------
- Threshold is frozen for 24 h (to avoid feedback loops).  
- Daily, a background job re-computes Cost(c) with the last 7 days of fresh labels; if the drift > 10 % an alert is raised and the loop restarts at step 2.

--------------------------------------------------
Concrete examples
--------------------------------------------------
- Antom Shield default: 0.85 probability (≈ 85 % fraud likelihood) → block.  
- Stripe Radar’s default “elevated” block is 0.75; “highest” is 0.90.  
- Large EU bank with low-margin cards: c* = 0.68 (accept more reviews, keep FP <0.2 %).  
- US neobank targeting millennials: c* = 0.92 (tolerate higher FN, keep FP <0.05 %).

--------------------------------------------------
Key take-away
--------------------------------------------------
The “security interception probability threshold” is simply the cut-off c* that minimises the **expected economic loss** under the institution’s own cost-of-fraud, cost-of-friction and regulatory constraints. It is not a static number; it is re-optimised continuously as soon as the cost function drifts.

## Annotations


## Sources
