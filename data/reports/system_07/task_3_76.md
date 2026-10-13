# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 6092006c | **Time:** 19.34s | **Cost:** $0.02547
--------------------------------------------------------------------------------

There is no single “magic” number.  
What you set as the “fire-alarm” probability depends on (a) how expensive the save play is, (b) how much a lost customer is worth, and (c) how much noise your team can tolerate.  
The companies that publish their numbers cluster around four practical bands:

1. 0.15 – 0.30  “Early-warning” band  
   Used when the intervention is cheap (automated e-mail, in-app banner).  
   Example: Medium post on an e-commerce model that peaks on F1-score at 0.15; anything above that gets the first nurture track.

2. 0.50 – 0.60  “Medium-risk” band  
   Typical for SMB SaaS or subscription apps where a CS rep phone-call costs money but is still economical.  
   Example: Klaviyo documentation recommends ≥ 50 % to add a customer to the retention flow; gym-chain case flags 0.519 so that 80 % of future churners are caught without flooding staff.

3. 0.70 – 0.75  “High-risk / high-touch” band  
   Used when the save play is expensive (discount, executive outreach, on-site visit).  
   Example: FasterCapital playbook: “if probability > 70 %, trigger retention campaign.”

4. 0.85 – 1.0   “Critical – red-alert” band  
   Reserved for VIP or gaming/gambling where lifetime value is huge.  
   Example: Smartico AI divides players into six ranks; 0.85–1.0 is “action highly recommended” and immediately queues a personal call plus bonus offer.

Rule-of-thumb design process you see in the literature

Step 1  Decide the recall you must hit.  
   “We need to catch 80 % of all true churners” → read the precision-recall curve and pick the lowest probability that still gives 80 % recall (often lands near 0.5–0.55).

Step 2  Check precision at that cut-off.  
   If the false-positive rate drives intervention cost higher than the expected saving, raise the threshold until the maths works.

Step 3  Segment.  
   Enterprise accounts get a lower threshold (expensive to lose) than free-trial users.  
   Example: PropelloCloud recommends top 5-10 % of risk scores within each ARR tier, not one global number.

Step 4  Validate monthly.  
   Churn prevalence drifts; re-optimise on the latest precision-recall curve instead of keeping a fixed number forever.

So in practice you will see operational models run two or three tiers:

- ≥ 0.30  → automated e-mail track  
- ≥ 0.60  → CS rep task created  
- ≥ 0.85  → executive escalation / discount authority triggered

Pick the probabilities that balance “save-rate vs. spend” for your own cost structure and keep recalibrating.

## Annotations


## Sources
