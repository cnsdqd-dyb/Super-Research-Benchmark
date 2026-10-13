# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** ee1a34aa | **Time:** 22.54s | **Cost:** $0.02845
--------------------------------------------------------------------------------

In purchase-conversion (a.k.a. “multi-touch”) models you never “see” the true causal contribution of a single ad, e-mail or call; you only observe the sequence of touches that finished in a sale.  
Attribution weight is therefore the model’s estimate of how much that sale would **not have happened** (or would have been delayed) if the touch in question had been removed from the journey.  
All practical methods are just different ways of approximating that counter-factual.

1.  **Rule-based short-cuts (no modelling)**  
    - Last-touch, first-touch, linear, U-shaped, W-shaped, time-decay, etc.  
    - The analyst fixes the weights (40 % / 40 % / 20 %, exponential half-life of 7 days, …).  
    - Cheap and transparent, but the numbers are arbitrary; two journeys that differ only in the order of the same touches get identical weights even if one ends in a sale and the other does not.

2.  **Shapley-value (co-operative game theory)**  
    - Treat every marketing channel as a “player” and every conversion as the “pay-off”.  
    - Compute the **marginal contribution** of the channel averaged over all possible orders in which the touches could have occurred.  
    - Gives a unique, fair split that sums to 100 % and is unbiased by position, but needs all combinations of channels to be observed; computationally heavy when >15–20 channels.

3.  **Markov “removal effect” (graph-based)**  
    - Build a first (or higher) order Markov chain: probability of moving from state A → B → … → Conversion.  
    - Drop one channel completely, re-normalise the remaining probabilities and measure how much the overall **conversion rate falls**.  
    - Normalise the falls:  
      weight_i  =  (ΔCR_i  /  Σ_j ΔCR_j )  
    - Fast, scalable, needs only journey logs, no spend or cost data; captures substitution (“if I remove e-mail, do people just click the next retargeting ad?”).

4.  **Survival / hazard models**  
    - Model the **time-to-conversion** while each touch is “active”.  
    - A touch that shortens the hazard (increases the instantaneous probability of buying) receives a higher coefficient; weights are the proportion of the **log-hazard** explained by the touch.  
    - Naturally incorporates decay: older touches get smaller coefficients.

5.  **Logit / probabilistic uplift**  
    - Estimate P(convert | path) with a nested logit, probit, or tree-based model that includes dummy variables (or embeddings) for every touch.  
    - Convert the coefficient β_i to a weight via the **average marginal effect**:  
      weight_i  =  Σ_j ( P(convert | path_j ) – P(convert | path_j  without touch_i ) ) / total_conversions  
    - Works well when you also need to control for customer attributes, creative, device, etc.

6.  **Machine-learning attention (Transformer, LSTM, etc.)**  
    - Represent the journey as a sequence; let an attention layer learn which positions and which features (campaign, creative, recency, frequency, spacing) receive high attention scores.  
    - The **normalised attention score** for a touch is its attribution weight.  
    - Handles long journeys, missing touches, text/creative embeddings, and calibrates automatically to incremental sales (LinkedIn’s LiDDA, Google’s Data-Driven Attribution, etc.).

7.  **Incrementality calibration**  
    - Whichever method above is chosen, the raw weights are re-scaled so that the **sum of attributed conversions equals the increment measured by controlled experiments** (geo-lift, ghost-bids, hold-out cells).  
    - Without this step the model can over- or under-attribute by 30–80 %.

Practical checklist used by most platforms:

1.  Collect every logged touch plus the final sale/lead.  
2.  Build at least one “non-converted” path for every converted path (negative sampling).  
3.  Pick one of the algorithmic families (Markov, Shapley, Logit, Attention).  
4.  Compute raw channel-level weights.  
5.  Validate with lift tests; adjust global multiplier so total attributed = incremental.  
6.  Report both fractional credits and ROI.

Hence, “how is the weight determined?” – it is the **normalised incremental impact of removing that touch**, estimated with whichever of the above techniques best matches data richness, business cycle length and experimental budget.

## Annotations


## Sources
