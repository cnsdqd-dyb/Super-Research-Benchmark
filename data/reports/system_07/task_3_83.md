# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 69196a9c | **Time:** 13.39s | **Cost:** $0.00938
--------------------------------------------------------------------------------

In every card-network “violation ladder” the gradient is produced by the same three-step arithmetic engine:

1.  **Map the raw violation metric to a dimension-less index**  
    -   ECM/HECM (charge-backs):  
      index = (charge-backs in month t ÷ sales in month t-1) × 10 000 (basis-points).  
    -   EFM (fraud):  
      index = (fraud-related charge-backs ÷ e-commerce sales in month t-1) × 10 000.  
    -   VDMP (Visa):  
      index = (disputes ÷ sales in the same month) × 100 (%).  

2.  **Cut the index into fixed bands**  
    The networks publish the bands in their operating regulations; they never change between assessments.  
    Example – Mastercard ECM:  
    -   0-99 bp → “safe”  
    -   100-199 bp → ECM  
    -   200 bp+ → HECM  

3.  **Read the monetary gradient from the corresponding row of the penalty table**  
    The table is simply a look-up: “if the index falls in band X and this is the merchant’s nth consecutive month in that band, the fine is Y”.  
    The amount rises linearly (or piece-wise linearly) with every extra month the merchant stays above the threshold, producing the observed “gradient”.

Because the index is normalized by sales volume, a merchant cannot dilute its violation by growing volume; the only way to flatten the gradient is to push the index down into the next lower band.

## Annotations


## Sources
