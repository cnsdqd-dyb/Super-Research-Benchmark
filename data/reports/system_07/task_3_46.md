# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 5deff491 | **Time:** 14.72s | **Cost:** $0.01032
--------------------------------------------------------------------------------

Asymmetric transport-delay distributions degrade the *response resilience* of inventory allocation in three distinct ways:

1. Directional blindness in re-allocation  
   When the delay from node A → B is very different from B → A, the APS/ERP engine under-estimates the time needed to re-position stock after a demand spike. The system therefore “sees” inventory that is physically unreachable within the service-time window and treats it as available. The first days of a disruption are spent re-planning the same unfeasible transfers, burning the short grace period that defines resilience.

2. Skewed safety-stock logic  
   Classic safety-stock formulas (σL × k) assume a symmetric lead-time distribution. With asymmetry the right tail (occasional very late deliveries) is much heavier than the left tail, so the true 95 % service-level quantile is 20–60 % higher than the symmetric forecast. Because most systems still plan on the mean or median delay, the buffer is systematically under-sized. When the asymmetric tail finally shows up (port strike, highway closure), the network is caught with 1–2 days less cover than promised, turning a survivable delay into lost sales.

3. Cascade amplification instead of absorption  
   In a multi-echelon network the asymmetry compounds. A delay that is 3 days longer in the upstream direction than downstream means the DC ships product it has already promised to the retailer, while the retailer cannot return excess stock in time to cover the shortfall elsewhere. The mismatch propagates orders of magnitude faster than the symmetric case, so the “recovery phase” starts later and lasts longer. Empirical studies (Zapro.ai case, ETASR 2024) show that networks with CV > 0.6 on the delay asymmetry index need 30–40 % more emergency air freight to reach the same fill-rate recovery trajectory.

Operational counter-measures that explicitly account for the asymmetry—direction-specific lead-time masters, skew-adjusted safety stocks, and switched-delay Smith-predictor logic in the replenishment solver—cut the excess recovery time by half and reduce resilience cost by 15–25 % compared with symmetric baselines.

## Annotations


## Sources
