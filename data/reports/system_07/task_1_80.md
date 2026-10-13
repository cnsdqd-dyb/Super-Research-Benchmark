# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 91dbd2d0 | **Time:** 12.00s | **Cost:** $0.01362
--------------------------------------------------------------------------------

There is no single “magic number” that every order-tracking system uses; instead, the critical threshold is chosen so that the probability of seeing the observed value (or one more extreme) is ≤ 0.3 % under normal conditions.  
In practice this is implemented as:

mean (μ) + 5 standard-deviations (σ)

If the metric being watched—order age, dwell time, cost impact, % of late line-items, etc.—crosses this 5-σ band, the system raises a CRITICAL anomaly warning.  
(μ and σ are re-computed every sliding window, so the band moves with seasonality and demand shifts.)

This 5-σ rule keeps the natural false-positive rate below 1 in 1 000 observations, which operations teams usually accept as the point where an alert is actionable rather than noise.

## Annotations


## Sources
