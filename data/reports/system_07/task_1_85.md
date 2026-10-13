# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 7cbb21d6 | **Time:** 10.85s | **Cost:** $0.00726
--------------------------------------------------------------------------------

There is no single, industry-wide number that “is” the substitute-similarity threshold.  
What sets the cut-off is always a **business-tuned decision rule** that is learned/validated on the retailer’s own basket data.  
The rule is expressed in whichever similarity metric the chosen algorithm uses, and the value is picked so that the **precision-recall curve for “substitute” shows a lift over random while still giving a usable catalogue size**.  
Typical practical ranges that come out of this optimisation are:

- Lift ≤ 0.7–0.8 (association-rule methods)  
- Cosine / dot-product ≤ 0.35–0.45 (embedding-based or graph methods)  
- Wasserstein / Jaccard distance ≥ 0.6–0.7 (distance-based basket matchers)

But the exact figure is **data-set-specific** and is re-estimated every time the model is re-trained.

## Annotations


## Sources
