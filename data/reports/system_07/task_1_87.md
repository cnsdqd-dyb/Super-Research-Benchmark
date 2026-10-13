# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 8e60a71f | **Time:** 15.17s | **Cost:** $0.00945
--------------------------------------------------------------------------------

In a product-classification hierarchy the “where to stop” question—i.e., how many levels to create and how fine the leaf category should be—is not set by a single knob but by a balance of four pragmatic constraints that are negotiated by the data/taxonomy team and the business stakeholders.

1. Business process granularity  
   - Inventory, purchasing, pricing, promotions, SEO, compliance and reporting all need a category that is “just detailed enough”.  
   - If the merchandisers never plan to run a separate promotion on “red stiletto-heel patent-leather pumps”, there is no value in creating that node even if photographs could support it.

2. Visual / attribute distinguishability (data separability)  
   - The lowest level must contain items that share enough observable attributes that a human or a model can place a new product in the node with acceptable confidence.  
   - Papers such as the VERD study and the MOGB “granular-ball” work show that purity and sample-count thresholds are used explicitly: if a candidate split does not improve visual separability above pt or would leave nodes with < nt examples, the split is abandoned.

3. User-need & catalogue coverage  
   - Search logs, facet usage and click-through tell the team how shoppers actually refine queries.  
   - A level is kept only if a meaningful share of traffic would use it as a filter or landing page.

4. Operational cost & stability  
   - Every extra level adds annotation cost, classifier training time, translation, compliance mapping, risk of mis-classification, and future migration work.  
   - Standards bodies (GS1, Amazon, Google, ECC) therefore publish recommended depth ceilings (usually 3–5 levels) and discourage “ornamental” depth.

Hence the boundary is drawn at the coarsest node that simultaneously:

- satisfies the business rule “we manage / report / promote at this level”,  
- can be populated with products that are visually/semantically separable with the available data,  
- is demanded by a non-trivial fraction of customers, and  
- does not impose an unsustainable maintenance burden.

Whenever one of these four forces changes—new legislation, new imagery, new shopper behaviour, new supplier base—the taxonomy team revisits the cut-off level and may prune or split categories accordingly.

## Annotations


## Sources
