# Deep Research Report: grok-4-1-fast-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** eb5bb7a0 | **Time:** 31.25s | **Cost:** $0.00595
--------------------------------------------------------------------------------

**In RFM (Recency, Frequency, Monetary value) value stratification, customer grade partition boundaries are typically determined using a percentile-based or quantile approach, most commonly quintiles, to divide customers into equal-sized groups (e.g., 5 grades scored 1–5, with 5 being the best).[[1]](https://justdataplease.medium.com/rfm-customer-segmentation-analysis-in-action-9108c906c628)[[2]](https://www.braze.com/resources/articles/rfm-segmentation)**

### Key Steps for Determining Boundaries:
1. **Calculate Raw RFM Metrics**:
   - **Recency (R)**: Days since last purchase (lower is better).
   - **Frequency (F)**: Number of purchases (higher is better).
   - **Monetary (M)**: Total spend (higher is better).[[3]](https://rfm.rsquaredacademy.com/articles/rfm-customer-level-data.html)

2. **Sort Customers**:
   - Recency: Ascending order (most recent first).
   - Frequency & Monetary: Descending order (highest first).[[1]](https://justdataplease.medium.com/rfm-customer-segmentation-analysis-in-action-9108c906c628)

3. **Compute Partition Boundaries Using Percentiles**:
   - Divide into 5 equal groups of 20% each (quintiles).
   - Boundaries are set at the **20th, 40th, 60th, and 80th percentiles**.
   - Formula for boundary position:  
     **Position = (percentile / 100) × N**  
     where *N* is the total number of customers.[[1]](https://justdataplease.medium.com/rfm-customer-segmentation-analysis-in-action-9108c906c628)
   - Example for Monetary (descending sort):
     | Grade | Percentile Range | Interpretation |
     |-------|------------------|----------------|
     | 5     | 80th–100th      | Top 20% spenders (best)[[1]](https://justdataplease.medium.com/rfm-customer-segmentation-analysis-in-action-9108c906c628) |
     | 4     | 60th–80th       | Next 20% |
     | 3     | 40th–60th       | Middle 20% |
     | 2     | 20th–40th       | Lower 20% |
     | 1     | 0th–20th        | Bottom 20% (worst) |

4. **Assign Grades**: Customers falling into each range get the corresponding score (1–5) for that RFM dimension. Combine into an RFM score (e.g., 555 for top grade across all).[[2]](https://www.braze.com/resources/articles/rfm-segmentation)[[3]](https://rfm.rsquaredacademy.com/articles/rfm-customer-level-data.html)

### Variations:
- **Custom Thresholds**: Some use business-specific cutoffs (e.g., Recency <7 days =5, Frequency >3/year=5) instead of data-driven quantiles.[[4]](https://www.moengage.com/blog/rfm-analysis-using-rfm-segments)
- **Other Bins**: Quartiles (1–4, at 25%/50%/75%) for smaller datasets (~30k customers) or more bins for larger ones.[[1]](https://justdataplease.medium.com/rfm-customer-segmentation-analysis-in-action-9108c906c628)
- **Alternatives**: K-means clustering for non-equal groups, but quantile partitioning is the standard for basic stratification.[[5]](https://www.issm.org/articles/jrmrfm.pdf)

This ensures relative, equitable grading within your customer base, ideal for segmenting into value grades like "Champions" (high RFM) or "At Risk" (low RFM).[[2]](https://www.braze.com/resources/articles/rfm-segmentation)

## Annotations (Inline Citations)
Citation [1] (Pos: 296-394): [Web] https://justdataplease.medium.com/rfm-customer-segmentation-analysis-in-action-9108c906c628
Citation [2] (Pos: 394-458): [Web] https://www.braze.com/resources/articles/rfm-segmentation
Citation [3] (Pos: 722-798): [Web] https://rfm.rsquaredacademy.com/articles/rfm-customer-level-data.html
Citation [1] (Pos: 934-1032): [Web] https://justdataplease.medium.com/rfm-customer-segmentation-analysis-in-action-9108c906c628
Citation [1] (Pos: 1352-1450): [Web] https://justdataplease.medium.com/rfm-customer-segmentation-analysis-in-action-9108c906c628
Citation [1] (Pos: 1654-1752): [Web] https://justdataplease.medium.com/rfm-customer-segmentation-analysis-in-action-9108c906c628
Citation [2] (Pos: 2122-2186): [Web] https://www.braze.com/resources/articles/rfm-segmentation
Citation [3] (Pos: 2186-2262): [Web] https://rfm.rsquaredacademy.com/articles/rfm-customer-level-data.html
Citation [4] (Pos: 2421-2489): [Web] https://www.moengage.com/blog/rfm-analysis-using-rfm-segments
Citation [1] (Pos: 2607-2705): [Web] https://justdataplease.medium.com/rfm-customer-segmentation-analysis-in-action-9108c906c628
Citation [5] (Pos: 2834-2881): [Web] https://www.issm.org/articles/jrmrfm.pdf
Citation [2] (Pos: 3041-3105): [Web] https://www.braze.com/resources/articles/rfm-segmentation


## Sources
[1] https://www.barilliance.com/rfm-analysis
[2] https://medium.com/@zargi.teddy7/a-comparative-study-of-k-means-clustering-and-rule-based-segmentation-for-rfm-analysis-on-the-uci-5ca3db89fc0b
[3] https://blog.rsquaredacademy.com/customer-segmentation-using-rfm-analysis
[4] https://www.kevel.com/blog/rfm-analysis
[5] https://loyalytics.ai/blogs/how-to-determine-your-most-valuable-customers-using-rfm-analysis
[6] https://www.researchgate.net/publication/392017535_Using_RFM_Analysis_to_Predict_High-_Value_Customers
[7] https://www.rejoiner.com/resources/rfm-analysis
[8] https://medium.com/@harsh1995hg/beyond-top-spenders-the-complete-guide-to-rfm-customer-segmentation-with-sql-27ec1925962b
[9] https://clevertap.com/blog/rfm-analysis
[10] https://www.moengage.com/blog/rfm-analysis-using-rfm-segments
[11] https://www.dase-analytics.com/blog/en/rfm-analysis
[12] https://thesai.org/Downloads/Volume16No12/Paper_35-RFM_K_OPT_Based_Machine_Learning_Framework.pdf
[13] https://www.daasity.com/post/rfm-analysis
[14] https://www.dinmo.com/customer-segmentation/rfm-segmentation
[15] https://pmc.ncbi.nlm.nih.gov/articles/PMC10059577
[16] https://www.sciencedirect.com/science/article/pii/S1319157819309802
[17] https://graphite-note.com/rfm-analysis-and-its-role-in-customer-valuation
[18] https://datascience.cmu.ac.th/storage/articles/74.pdf
[19] https://www.researchgate.net/publication/373967831_RFM_model_customer_segmentation_based_on_hierarchical_approach_using_FCA
[20] https://www.r-bloggers.com/2019/07/customer-segmentation-using-rfm-analysis
[21] https://klaviyo.tech/the-research-behind-our-new-rfm-feature-4c38be17b184
[22] https://www.sciencedirect.com/science/article/pii/S0970389625000266
[23] https://www.braze.com/resources/articles/rfm-segmentation
[24] https://www.omniconvert.com/blog/rfm-analysis
[25] https://www.tsc.reapress.com/journal/article/download/34/12
[26] https://mercurycloud.studio/blog/rfm-analysis
[27] https://justdataplease.medium.com/rfm-customer-segmentation-analysis-in-action-9108c906c628
[28] https://www.wearetesters.com/en/market-research/rfm-analysis
[29] https://documentation.bloomreach.com/engagement/docs/rfm-segmentation
[30] https://www.diva-portal.org/smash/get/diva2:1998264/FULLTEXT01.pdf
[31] https://patchretention.com/blog/how-to-calculate-rfm-score
[32] https://www.sciencedirect.com/science/article/abs/pii/S0963996924011670
[33] https://www.expressanalytics.com/blog/rfm-analysis-customer-segmentation
[34] https://www.stellasource.com/blog/rfm-analysis-strategy
[35] https://www.kaggle.com/code/casalicchio/customer-segmentation-based-on-rfm-scores
[36] https://help.retentionx.com/hc/en-us/articles/360017353160-Percentile-Analysis
[37] https://rfmcube.com/en/how-to-define-rfm-values-for-your-customers
[38] https://www.researchgate.net/publication/385833497_Master_Stockist_Customer_Segmentation_Using_RFM_Model_and_Self-Organizing_Maps_Algorithm
[39] https://www.graphed.com/blog/how-to-do-rfm-analysis-in-excel
[40] https://rfm.rsquaredacademy.com/articles/rfm-customer-level-data.html
[41] https://www.kaggle.com/code/manishkr1754/online-retail-customer-segmentation-rfm-analysis
[42] https://www.issm.org/articles/jrmrfm.pdf
