# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** a3d7abe5 | **Time:** 337.99s | **Cost:** $1.27410
--------------------------------------------------------------------------------

# Dynamic Safety Stock Adjustment Boundaries in High-Velocity Flash Sale Environments

### Key Points
*   **Dynamic vs. Static Boundaries:** Traditional static safety stock formulas fail during flash sales due to extreme demand volatility; adjustment boundaries must be dynamic, often utilizing a "Promo Multiplier" or real-time Conversion Rate (CVR) variance triggers [cite: 1].
*   **The Conversion Rate Feedback Loop:** Inventory availability directly influences conversion rates; research indicates that when stock availability drops to 10%, conversion rates can halve, necessitating a safety stock boundary that accounts for this non-linear relationship [cite: 2, 3, 4].
*   **Threshold Triggers:** Operational best practices suggest setting automated alerts or adjustment triggers when conversion rates deviate by more than 30% from the baseline or forecast, allowing for real-time recalibration of safety stock [cite: 5].
*   **Historical Data Reuse (HDR):** Advanced adjustment boundaries are set using Historical Data Reuse approaches, where data from past similar promotions is used to fine-tune CVR prediction models, reducing the "cold start" problem of inventory allocation [cite: 6].
*   **Oversell Protection:** In flash sale contexts, the safety stock boundary often functions as "oversell protection," a technical buffer set to prevent negative inventory caused by system latency during high-transaction volume events [cite: 7, 8].

---

## 1. Introduction

The management of inventory during flash sales represents a distinct paradigm within supply chain operations, characterized by extreme velocity, high uncertainty, and the critical importance of service levels. Unlike steady-state retail environments where demand follows a relatively normal distribution, flash sales introduce "fat-tail" risks where demand spikes can deplete inventory in minutes. A central variable in this equation is the Conversion Rate (CVR)—the percentage of visitors who execute a purchase. In flash sales, CVR is not a static metric; it fluctuates wildly based on urgency, scarcity, and social proof. Consequently, the "safety stock adjustment boundary"—the threshold at which safety stock levels are recalibrated or inventory is partitioned—must be set dynamically to accommodate these fluctuations.

This report examines the mechanisms for setting these boundaries. It explores how CVR volatility impacts standard inventory formulas, the statistical methods for calculating dynamic buffers, and the operational triggers used to prevent both stockouts and overselling. By synthesizing data on promotional multipliers, historical data reuse, and real-time variance monitoring, we establish a framework for optimizing safety stock in high-volatility promotional events.

## 2. Theoretical Framework of Safety Stock in Promotional Contexts

### 2.1 The Limitations of Static Formulas
The traditional determination of safety stock ($SS$) relies on the standard deviation of demand ($\sigma_D$) and the standard deviation of lead time ($\sigma_{LT}$) over a fixed period, multiplied by a Z-score ($Z$) corresponding to a desired service level. The standard formula is expressed as:

\[ SS = Z \times \sqrt{(\bar{D} \times \sigma_{LT})^2 + (\bar{LT} \times \sigma_D)^2} \]

However, this static approach assumes that demand variability ($\sigma_D$) is independent of the sales mechanism itself [cite: 9, 10]. In a flash sale, the sales mechanism (urgency, limited time) actively manipulates $\sigma_D$. The demand is not merely a function of customer need but is artificially compressed into a "golden hour," where up to 50% of total event revenue may be generated [cite: 11].

### 2.2 The Role of the Adjustment Boundary
The "adjustment boundary" in this context refers to the decision limits set by inventory planners or algorithmic systems. It defines the range of acceptable variance in demand or conversion rate before the safety stock level must be modified.
*   **Lower Boundary:** The minimum stock level required to maintain the "scarcity effect" without causing conversion rate collapse due to visible stockouts [cite: 2].
*   **Upper Boundary:** The maximum buffer held to prevent "overselling" (selling more units than physically available due to cart latency) without trapping excessive working capital [cite: 7, 8].

Research suggests that during flash sales, the safety stock calculation must transition from a "days of coverage" model to a "transaction velocity" model, where the boundary is set based on the maximum expected conversion rate rather than average daily usage [cite: 12, 13].

## 3. The Mechanics of Conversion Rate Fluctuations

To set an accurate safety stock boundary, one must quantify the volatility of the conversion rate. CVR in flash sales is influenced by three primary factors: urgency, scarcity, and availability.

### 3.1 The Scarcity-Conversion Feedback Loop
There is a documented causal relationship between inventory levels and conversion rates. As inventory depletes, the "scarcity effect" can initially boost CVR as customers rush to buy before the item is gone [cite: 14, 15]. However, this relationship is non-linear.
*   **High Availability (100%):** Maximizes CVR as all variants (sizes/colors) are available [cite: 3, 4].
*   **Moderate Availability (60%):** CVR remains stable or slightly elevated due to urgency.
*   **Low Availability (<10%):** CVR collapses. Research indicates that when stock availability drops to 10%, the conversion rate is approximately half of what it is at 60% availability [cite: 2, 3, 4].

This drastic drop occurs because the most popular variants (e.g., medium sizes) sell out first, rendering the "parent" SKU effectively useless to the majority of traffic [cite: 2, 4]. Therefore, the safety stock adjustment boundary must be set *above* this 10% threshold to maintain campaign efficiency.

### 3.2 Promotional Multipliers and Traffic Surges
Flash sales generate traffic spikes that distort standard CVR metrics. The "Promo Multiplier" is a variable used to adjust forecasted demand.
\[ \text{Demand Forecast} = (\text{Sales Velocity} \times \text{Promo Multiplier} \times \text{Lead Time}) + \text{Safety Stock} \]
Here, the Promo Multiplier accounts for the expected lift in CVR and traffic [cite: 1]. For example, if a flash sale typically drives a 3x increase in demand, the safety stock boundary must be expanded proportionally to absorb the variance of that 3x multiplier, not just the baseline variance [cite: 1].

### 3.3 Mobile Dominance and Velocity
Flash sales convert 48% better on mobile devices than desktops due to the immediacy of push notifications and SMS alerts [cite: 11, 14]. This mobile dominance accelerates the "time-to-stockout," meaning the safety stock boundary must be responsive to faster transaction cycles. A boundary set for desktop conversion speeds may result in overselling on mobile platforms where "pocket-sized" notifications trigger near-instantaneous checkout surges [cite: 11].

## 4. Setting the Safety Stock Adjustment Boundary

The setting of the adjustment boundary is a function of risk tolerance (Service Level) and predictive accuracy (Forecast Variance).

### 4.1 The 30% Deviation Rule
A critical operational metric for setting the adjustment boundary is the "30% deviation" rule. Integrated inventory systems often set alerts or automatic triggers when the conversion rate jumps more than 30% above the baseline [cite: 5].
*   **Trigger Logic:** If $CVR_{actual} > 1.3 \times CVR_{forecast}$, the system identifies a "high-velocity" event.
*   **Action:** The safety stock buffer is dynamically increased (if replenishment is possible) or the "available to sell" (ATS) quantity displayed to the frontend is throttled to prevent overselling.
*   **Outcome:** Implementing such dynamic alerts has been shown to reduce stockouts by 43% and improve full-price sell-through by 21% [cite: 5].

### 4.2 Historical Data Reuse (HDR) Approach
For setting the initial boundary before the sale begins, advanced models use Historical Data Reuse (HDR). This involves retrieving data from historically similar promotions to fine-tune the CVR prediction model [cite: 6].
*   **Methodology:** Instead of using a generic CVR (e.g., 2%), the system analyzes past flash sales for similar SKUs (e.g., "viral lip gloss" or "summer desk fans" [cite: 1, 16]).
*   **Boundary Setting:** The safety stock is set to cover the *variance* observed in those specific historical events. If past events showed a CVR variance of $\pm 5\%$, the safety stock boundary is widened to accommodate the upper limit of that variance [cite: 6, 17].

### 4.3 The "Oversell Protection" Boundary
In flash sales, the technical limitation of inventory synchronization becomes a safety stock factor. "Oversell protection" is a buffer set specifically to account for the latency between a customer adding an item to the cart and the inventory system updating [cite: 7, 8].
*   **Calculation:** If the system latency is $t$ seconds and the maximum transaction rate is $r$ orders/second, the technical safety stock boundary ($SS_{tech}$) must be at least $t \times r$.
*   **Implementation:** This is often a "hard" boundary. If physical stock is 1,000 units, the system may report 0 availability once 950 units are sold (a 50-unit safety buffer) to ensure the final 50 simultaneous clicks do not result in unfulfillable orders [cite: 8].

## 5. Dynamic vs. Static Adjustment Models

### 5.1 Static Models (The "Set and Forget" Approach)
Static models rely on fixed rules, such as the "50% rule," which suggests holding safety stock equal to 50% of the lead time demand [cite: 13, 18].
*   **Application:** $SS = 0.5 \times (Daily Sales \times Lead Time)$.
*   **Failure Mode in Flash Sales:** This model fails when demand is not linear. If 50% of sales occur in the first hour [cite: 11], a static buffer calculated on *daily* averages will be insufficient to absorb the *hourly* variance.

### 5.2 Dynamic Models (Real-Time Recalculation)
Dynamic safety stock models continuously adjust the boundary based on real-time inputs [cite: 19, 20].
*   **Inputs:** Real-time CVR, traffic velocity, and supplier reliability.
*   **Mechanism:** As the CVR fluctuates, the Z-score (service level target) or the standard deviation of demand ($\sigma_D$) is recalculated.
*   **Example:** If CVR increases due to a "viral" social media post, the dynamic model instantly increases the safety stock requirement (or "reserve" stock) to protect the most critical channels or high-value customers [cite: 5, 19].
*   **Benefits:** Dynamic models reduce stockouts during uncertainty and lower overstock when demand stabilizes [cite: 19].

## 6. Mathematical Modeling of the Adjustment

To mathematically derive the adjustment boundary ($B_{adj}$) given CVR fluctuations, we must modify the standard demand deviation component.

Let Demand ($D$) be a function of Traffic ($T$) and Conversion Rate ($CR$):
\[ D = T \times CR \]

The variance of demand ($\sigma_D^2$) is an approximation based on the variance of traffic and conversion rate (assuming independence for simplification, though they are often correlated):
\[ \sigma_D^2 \approx \bar{T}^2\sigma_{CR}^2 + \bar{CR}^2\sigma_T^2 \]

The Safety Stock ($SS$) adjusted for CVR fluctuation is:
\[ SS = Z \times \sqrt{LT \times (\bar{T}^2\sigma_{CR}^2 + \bar{CR}^2\sigma_T^2) + \bar{D}^2\sigma_{LT}^2} \]

*   **$\sigma_{CR}$ (Standard Deviation of CVR):** This is the critical variable. In flash sales, $\sigma_{CR}$ is high.
*   **Adjustment Boundary:** The boundary is set by selecting a Z-score that reflects the cost of a stockout. In flash sales, where customer acquisition is a primary goal, the cost of a stockout (lost customer lifetime value) is high, justifying a higher Z-score (e.g., 98% or 99% service level) [cite: 10, 21].

Furthermore, the "Promo Multiplier" ($M$) acts as a scalar on the entire demand function:
\[ SS_{flash} = SS_{base} \times f(M) \]
Where $f(M)$ is a function derived from the expected lift [cite: 1].

## 7. Operational Implementation and Triggers

### 7.1 Inventory Rationing and Channel Allocation
When CVR fluctuates across different channels (e.g., mobile app vs. desktop vs. social media), the safety stock boundary may be applied differently per channel.
*   **Dynamic Allocation:** Inventory is "rationed" or reserved for channels with the highest CVR or strategic importance [cite: 19].
*   **Thresholds:** If the mobile CVR exceeds the desktop CVR by a significant margin (e.g., >48% difference [cite: 11]), the system may shift the safety stock boundary to favor mobile fulfillment, ensuring the highest probability of conversion.

### 7.2 The "Last Call" Phenomenon
Data shows that 30% of flash sale revenue often comes from "Last Call" notifications [cite: 22]. This creates a secondary demand spike at the end of the sale.
*   **Adjustment:** The safety stock boundary must account for this "U-shaped" demand curve (high at start, high at end).
*   **Strategy:** Inventory planners may release "safety stock" into the general pool during the final hours to capture this last wave, effectively lowering the safety boundary to zero as the sale concludes to maximize sell-through [cite: 22, 23].

### 7.3 Technical Buffers and Latency
To manage the "oversell" risk, a technical buffer is often hard-coded.
*   **Buffer Size:** Often set between 5-10% of the total stock for high-velocity items, or a fixed unit count (e.g., 20 units) [cite: 24, 25, 26]. *Note: While some sources discuss technical buffers in environmental contexts, the concept of a "buffer zone" for oversell protection is explicitly cited in e-commerce logistics [cite: 8].*
*   **Function:** This buffer absorbs the variance caused by the time lag between "Add to Cart" and "Payment Confirmation."

## 8. Case Studies and Empirical Evidence

### 8.1 The "Viral Lip Gloss" Scenario
A case study of a beauty brand on TikTok Shop illustrates the failure of static boundaries. A $12 item sold out in 4.5 hours due to a viral spike, causing a 3-day stockout and $180,000 in lost sales [cite: 1].
*   **Analysis:** The brand likely used a static safety stock based on average daily sales.
*   **Correction:** A dynamic boundary using a "Promo Multiplier" (e.g., 3x or 5x demand) and real-time CVR monitoring would have triggered an earlier replenishment or a "pre-order" mode to capture the excess demand [cite: 1].

### 8.2 Seasonal Demand: Desk Fans vs. Razor Blades
Comparing stable products (razor blades) with volatile ones (desk fans during a heatwave) highlights the need for different boundaries.
*   **Stable:** Low $\sigma_{CR}$, low safety stock required.
*   **Volatile (Flash/Seasonal):** High $\sigma_{CR}$. The safety stock boundary for the desk fans must be set significantly higher (e.g., covering peak variance rather than average) to prevent stockouts during the demand spike [cite: 16].

## 9. Conclusion

The safety stock adjustment boundary for flash sales is not a static line but a dynamic threshold that breathes with the conversion rate. It is set by integrating the **Promo Multiplier** into demand forecasts, monitoring **CVR deviation** (with a 30% trigger being a standard benchmark), and utilizing **Historical Data Reuse** to predict variance.

Effective management requires a tripartite approach:
1.  **Statistical:** Using modified formulas that account for $\sigma_{CR}$ and high Z-scores (98%+).
2.  **Technological:** Implementing "oversell protection" buffers to handle system latency.
3.  **Operational:** Using dynamic alerts to manually or automatically adjust "available to sell" quantities when CVR spikes.

By treating the conversion rate as a volatile input variable rather than a fixed constant, retailers can set safety stock boundaries that maximize revenue during the "golden hours" of retail while mitigating the risks of stockouts and customer alienation.

## References
[cite: 9] Demand Works. (2017). IBP and Safety Stock Calculation Methods.
[cite: 10] Netstock. (n.d.). Safety Stock Meaning, Formula & How to Calculate.
[cite: 18] NetSuite. (2025). Safety Stock.
[cite: 16] Linnworks. (2025). Safety Stock Formula.
[cite: 12] Pallite Group. (n.d.). Safety Stock Formula.
[cite: 21] ASCM. (n.d.). Safety Stock: A Contingency Plan.
[cite: 19] Imperia SCM. (n.d.). Dynamic Safety Stock.
[cite: 17] RELEX Solutions. (2025). Safety Stock.
[cite: 2] Vervaunt. (n.d.). The Impact of Product Availability on Conversion Rate.
[cite: 6] Chan, Z., et al. (2023). Capturing Conversion Rate Fluctuation during Sales Promotions.
[cite: 3] Bidnamic. (2024). How does stock availability affect conversion rate?
[cite: 23] H&H Accounting Services. (2025). The Impact of Sales on Inventory Management.
[cite: 11] ConvertCart. (2025). Flash Sales Guide.
[cite: 14] MobiLoud. (2025). What are Flash Sales?
[cite: 13] inFlow Inventory. (2025). Safety Stock Calculation.
[cite: 10] Netstock. (n.d.). Safety Stock Meaning (Duplicate).
[cite: 20] Demand Driven Tech. (n.d.). How to Calculate Safety Stock Accurately.
[cite: 5] EasyReplenish. (2025). Inventory Optimization Process.
[cite: 27] Bassamboo, A., et al. (2022). Inventory Availability and Flash Sales.
[cite: 1] CedCommerce. (2025). How to Avoid Stockouts in BFCM 2025.
[cite: 24] Lab Unlimited. (n.d.). General Laboratory Catalogue.
[cite: 25] World Bank. (n.d.). Technical Buffer Zones.
[cite: 26] WBGU. (2025). Technical Buffer Systems.
[cite: 2] Vervaunt. (n.d.). Impact of Product Availability (Duplicate).
[cite: 4] Bidnamic. (n.d.). Stock Availability and Conversion Rate (Duplicate).
[cite: 15] Checkout Champ. (n.d.). Cart Promotions.
[cite: 1] CedCommerce. (2025). Promo Multiplier (Duplicate).
[cite: 6] ResearchGate. (2023). Capturing Conversion Rate Fluctuation (Duplicate).
[cite: 7] WPXPO. (n.d.). Black Friday Ecommerce Checklist.
[cite: 8] IronLinx. (n.d.). Jewelry Order Fulfillment.
[cite: 11] ConvertCart. (2025). Flash Sales Guide (Duplicate).
[cite: 22] Retainful. (2026). Flash Sale Examples.
[cite: 28] Service Bureau. (n.d.). Optimizing Promotional Campaigns.
[cite: 29] ActiveCampaign. (2024). Flash Sale.

**Sources:**
1. [cedcommerce.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7kQ9Px_DPd4CFfacvkb0WexTOpyeUoMHI6d2RHGMHBskBcyNGN6fx0ra09yPxcBNYII3YHEXa_1DwCqtvi16TaXtF2PJ3pxkPMRspAi2MRCENgbGsq5dVeS4RgTXch_g5L5SUTXCh3h4yQh4HSz2BYbnQQu9iW_x8mE_6s-0loaQ1K3DhbkWKt2kc0GbpwK9P8wfVtetr7pxu5mJVSjQ=)
2. [vervaunt.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFESkgva78Y1H0E8qb5SP7d7YHuPblJNCQEoOOKmDoD9sWURzoUqKPCpFRyTuAZMr0TvKKn9NiGjC1uF9v-OpueOZhzANjrJVIuEXzFYFLki4sjzXDpzUxoVIMiIg37qeXc_QkYj-XMsda3zNhmk5E1kvtCv_Rpd86mYgTEPhYKJdQWYcdPzVmpq2nuKNeO7vfOglKOAR_XplMu11O4C3hg8RqhWqZNsx5c-v78sd0=)
3. [bidnamic.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESPfRZFeUCzEmjqygTSzofr0rp9KisEA6XtINOZALFMBru3CAh3wtCwjuBSA0J8fB9yrXIqVKCNMZ0HYmldiHUQV1Nx4wi1rzc2W07QtoRE3aeWtA2Q-TZJf06MTSpRHBprAN_cGoZP7rOWu6F5Ft9Y0Ph8njJcRFtdv-G1DSw28miT_D7ncCVVC0xZe33e29f)
4. [bidnamic.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwS8NpXIf7sd0nHwh1Lnu4VhhNYjSt28T9VdfHn2ne8tqZ8JE5BTo0gyQ_GrRM0O1NGgxNDLQ_18nfmMozZ4X6S7d7CZVMlSEn-r1RqC_KbPWDdCswmIGrkoyswKLnyfb5Rz6SbJHd6xtMJuzmnUUfWrmWAKldPPmMUtmxta05yZudgWRiQKaAueE2)
5. [easyreplenish.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyBgt2fxeePoAkX_5RLjivzy_v-AIGUtxvL2SBhrgyP6d0Ekqr1WELMMWLUzO00iMYxjWCxwCyeJRjoQ_RkalU6V92ZsoOWf6g31squ02Nzsy9Tu7JUd9ZddK6cl3wb7k09HaWilZ17Zbumv5qFNkfB1sOEB2end8FJIu_VVr5m14DnZWJZ3kNbiY3ee73dJGv)
6. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF26iFNHRm9b-5qx-QBHBIgFbfh2tINgTWFUgECCpRWqz78SKjWdF2HO6ApP1rWsl__yDg6hlldc4Obh9psi28S6e18osgQ_9cfEfyirigii7gilXeM1P2RUdKRiYKiujbDWvY1ue9P6ITiSuQqY1ohhI31j2lc5K9xmtdIu4TRPIX9Nu1TPg-kTwQGVDo7x6EO13XtMV5q6-3oK0CPNgefCjnL4qPzSr-TaSfHUcb3X6FmNiTppEZlR8549JvViUEEtqbIVu_wS81QZsC0Jg==)
7. [wpxpo.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjhdRRcCjyVjwiq5s-ilcCLp8_SD4TUjPwVtlzF5m-SH1fZMcP75DNO3kXSf-zft89SO8KQfz2BNjiCN-xsRXbDxAVB7huE0txakFtkKV2AhiGLDb8BlFGxSh_NkKNva3UCy90DoddULMOZ0L2)
8. [ironlinx.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-f-E3s01wunL6JKUhrG_wNpSXI966YTWiga_9IY22obiAlZMfhXDnKiQIzRfWphNvpUYTd9PVos2jjluJD8gUraoeJLhC0EqLxbtD3MzmTPF0IuSzYA_XEPRbnrCEuRU8lwOJrw==)
9. [demandworks.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8c9NrddBh9PNVTTvmTxYgq4Bof8xZnZmc-Ys9pK3Fxvj3ckb3LlFuGZ8HZtP6DEYBPaNbpLq-7nSlYg6BtsjjRyLSRri1VzIFhurEEcAdiQw4hISMGkckJ1ZTSNazhU3IWXDvPxWSelvrX5R_Q_aGhIkXB0_Z90DtnvbhnsvkMxRJoRJ2K-vjCVoNtwqk681ljvRd8w==)
10. [netstock.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7ixHSlXHI792qIlODqHfTzDJxmw4LlBeh1-8qQ6M9gyXzte76han9r4WIAbhwya0K0kgiZSmhy7rgS7dwwKICvOgepiy0izx7qpfSpJZONVJXIKQ1mzPG41HVMDkKnB87PD1k_iOPdCSdXFSsrYt6bTSVEvkTYqhfwvuD_1w0Rlub)
11. [convertcart.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9Ium619G7FcufZ7tH3dB_xsIrLjkFDBgVcO7z8hDBie3waUEMvvpaaOtXQVZtfev5L2SLgL39M625faNsmlf9m8ncMhwbdtUpQYzd_V4jyCq1j2Zgi9k0g_fFZ3K1zqyiTeBuXuNNHA==)
12. [pallitegroup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHODTLrVrzxAQ2X192qbB4PS-MxdovIt5mlNfYhD7D1CEo2EuaOEXgI7M9Ty4zDlIx3iXM6swz9KwaMm3WpEQcn2BCvkfI2Ofeh8bhm8_hzqN4mNZ60-e8CGpiyj-yH4zHeqz8V0VkZergnzdk=)
13. [inflowinventory.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcsw_T6Ki9AbJyZ6kdYkygJeZw5H_vNOYFTzwNzMsBfTPNxyF_SD6KxFOko5RpNrbqilDjx5X6-KcAlO2fJRyHQNrp-FMH74Jl0lwlPU-rkBWl5sN9qWp7-SNagEsvBD0tXWvyOmi3-5aj4neJrkc6hpoNhg==)
14. [mobiloud.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGeJwMJ6ahMsWN7zOAaf_cZtGASe7FrMc781theRdchKphWjR1w2XGvLMKcRLMEChxFWYJHwD5M0MP6OaJzsZ0XyocKY26VChVbLQmMRD0qktrz6D-uG00EPk7wuyDAWD749A94_GPvjBtdA==)
15. [checkoutchamp.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8kmOHyGkbyoD69dJm1d9NzDvR1QogyIXxAq96mxgsVsi13GE7N1Hwq9_Q91I_HBkQgLdmsR-CtKUlavVIiufsyrDvFzAgOipR6kIS71XJ3dah_cN-R1p93wkZaTvs8b4LJ5kuINY=)
16. [linnworks.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKqDQGYfQFmvo2HIvgEp9Vx3j0nLliE9CoM3ZI6PRuff-EIj95PPsDsQGauMy5tlR0gqnbtDYGdudt42c3uXzQd2VtqdknlwiJQZfsvO1dCbAbFzZ5VhkZBboXpoCHzsNYSta7i3jWyxsU)
17. [relexsolutions.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQ5sNHDe1i06q4P8K3ubc4QVmqSWzWueef6-s_KgxEyo3dreAF1fROPN7zxtENdLlvrvYjl8BgYtV1BWQfTCglvi1Pbq2yrgGUOmQ3BoCMsMnuIndoatB98piRzBFAGvfGvxEaozRuIznGJsw=)
18. [netsuite.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMja3yhLGDwwcX7K0S9dohBMu4o5piSQWsvLUPoV8T_1fX_C9ViyZOriMT598WacmsfawmcsY8lmbOPQG_Oc40w_MPxF_2jYnRhlcGUolhROQjB7p9lshJAPaG2M-gayhZrTXt74tqs2d21mmLLLphDO6Fy315f2mulRgyp7KUSKRyd38U_BWcDSr9H10RzQ==)
19. [imperiascm.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfZcIdsRhEAMqTcxoil2ABaXzYgcAx7uMiJQll0fp7o2wZ2LkM1I2QNMyschcfJJxGzKjdGITBWkzgcsZJ-wyHBVKp8K1eheBCMnl-4nt5pVW5jlXcmXOaotNzaAB-ULUIVJn_uYA=)
20. [demanddriventech.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjl19kZTNdk_IrnOIQzkZtTAQMKlCybUaFdrvNnzzljHC8tnwA8n6povQ4-PzwBqGxOOLkqt8Os90_TKN1hrqi6Zfe6bSa6todjod9AlYu3H4jGgX2nUwYmUmwZ0Mwv_sU4sNiI6kjbxWJUlHWTge0Xcgzv-8o0woFoFYzMtgzHQ==)
21. [ascm.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwNVfG9M6qYyQC7oYx3d9uqOS_BxzG0GVoDVHiLqdLVKASLRcEY5bJUMhmE7vB1CTcjYw-VSUYbXKbAXZ1wHNFnB1lzarwvcDEqCQw-Hw1iQM9MNutJuyLwNW05yCHQhc1XC4ljfp7gUyuDVqy-t3tKc7tUuJ9w5BdET8LHPbMxBIq8LvgucCi-4qJOn3TGr0JU243laT9-tuI2Q==)
22. [retainful.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsf7eecXzfpB4E42LHWZw-UbarBrAzDy13lDb5PaIt1umh9sUqIbgBxLRFCEZOunsUkDEhFWMwaZHnM7bc8NnnGbtucOKY2YJWtNOVRTJD87Ow9i_gFKsD_iO20FsEKLeoR62S4LcQsg==)
23. [hhcpaservices.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgX893Wv-QWEunjy_9FFbd9F7l0AER3TS_us7PcmxgxK7uS_ZwDe18Ma8-4VrDtn8JCzulFXHNP1qIdkYVXcyQuAm7dV9LdWsaWJ0iByokCSwGGgNHotEVkQ1uNTcFqZnRY48FWsHNMTbloUCLs_W-D5jmiHsDROMfU5u_Lka7C85YaJ9WNJ73NUGQ9uGTeRRbqw==)
24. [labunlimited.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZjiAGox2-lwpQGKLT73J-C2nres5OM6IKRhJ1PlkST9kZQJS1SDi0Vn9vn65xEuRy9jmx-nBO15tWNQAoWIi6zmupql8KnkuWLZdeEfDCsMqW-YMvKopSv_Y-CXkRQAIB0YpZ8sIjvsozdcIJqsGLhOTIdspCSCrdCwuE1as=)
25. [worldbank.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuQHxe2xng77eeh7J916E6aTuC6_8lISMb0gISMgsZjtGz8VyiUyaGi4OJQy3v9DszUOFrheF1nC-yv4XY9cOgi-Hmu-CcIilCVMH95sYncauzeAxqmhKaS8inlXFxvLAbQRNYQ5v4IcQFLdVwT3tMEBJdI0LspwudcjEEXmZ0Qi5znSIVxg==)
26. [issuu.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyJxfeiPgbrm4I7bzuECbyeOrPz1f3oTipDyDeDpikb4GkiQnW1b9JJ7LKYHsLZI3j1es2nm4GV_Re1r3xKtydFRroHwfoh4hpV2lWw1FP8nSuMSVobtK0uUQhY4Y0c4RiTJzHvbvvfgx0WnFxBhA=)
27. [utdallas.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrqnOa6ztqvzVyPeHW33HWRx38W49tkrtYnOaIFL8Amf6PF2JVeLxNJulklWoJNwYsXRuPLUVmhuNMsfgl3hKtmDglHU01eoEVg5lwL6ilMQikoaNF8HN3b_IBOn3YuLmBVzNPya9ROUxdrAIxQxnBmfX-5lxJSebG)
28. [servicebureau.nl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWvBxcEkR9Bthpa7E2ZZA2p3IPJB59tcf7mfvcr8qOgj0LzP9OmZ2I-0If1EW_BqSSqCbBEVmrFay-TRIS9c2khLpJtD6ZGFUEjKM2QCsH9wYzP6tqIp0yKqNsDzczYM1LMeHQuQd5FAUFxEEF5iTmpk5-KSeEM0qFzuYUZ6tjhJw9ubPGlz4ZFElVecVXkyV-ldEmot8vqqKTijFjqaORZ0tqYRtAa328ETz4NIegXqg-mf86g38Yt5YExPXS2BwDPYDEVfIrGEUg8xyWSB8xzn6xFLoZvxNalMQU_aEIpA8xgyJ86MgceXyAjGI=)
29. [activecampaign.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHd-uL_x85vkWdljjRd5UR9stjXmzqAREwsZjw2fhAkuxvGwjnMumPhR3EDWqfUR87uyM9ZaMiddktLuNqdbrGHwkEVGasue1XDPaJ6hn8nkscZBjtZT1tLSt_DFcZ8q3SnGLxC)


## Annotations
Annotation(end_index=378, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7kQ9Px_DPd4CFfacvkb0WexTOpyeUoMHI6d2RHGMHBskBcyNGN6fx0ra09yPxcBNYII3YHEXa_1DwCqtvi16TaXtF2PJ3pxkPMRspAi2MRCENgbGsq5dVeS4RgTXch_g5L5SUTXCh3h4yQh4HSz2BYbnQQu9iW_x8mE_6s-0loaQ1K3DhbkWKt2kc0GbpwK9P8wfVtetr7pxu5mJVSjQ=', start_index=369)
Annotation(end_index=674, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESPfRZFeUCzEmjqygTSzofr0rp9KisEA6XtINOZALFMBru3CAh3wtCwjuBSA0J8fB9yrXIqVKCNMZ0HYmldiHUQV1Nx4wi1rzc2W07QtoRE3aeWtA2Q-TZJf06MTSpRHBprAN_cGoZP7rOWu6F5Ft9Y0Ph8njJcRFtdv-G1DSw28miT_D7ncCVVC0xZe33e29f', start_index=659)
Annotation(end_index=674, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFESkgva78Y1H0E8qb5SP7d7YHuPblJNCQEoOOKmDoD9sWURzoUqKPCpFRyTuAZMr0TvKKn9NiGjC1uF9v-OpueOZhzANjrJVIuEXzFYFLki4sjzXDpzUxoVIMiIg37qeXc_QkYj-XMsda3zNhmk5E1kvtCv_Rpd86mYgTEPhYKJdQWYcdPzVmpq2nuKNeO7vfOglKOAR_XplMu11O4C3hg8RqhWqZNsx5c-v78sd0=', start_index=659)
Annotation(end_index=674, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwS8NpXIf7sd0nHwh1Lnu4VhhNYjSt28T9VdfHn2ne8tqZ8JE5BTo0gyQ_GrRM0O1NGgxNDLQ_18nfmMozZ4X6S7d7CZVMlSEn-r1RqC_KbPWDdCswmIGrkoyswKLnyfb5Rz6SbJHd6xtMJuzmnUUfWrmWAKldPPmMUtmxta05yZudgWRiQKaAueE2', start_index=659)
Annotation(end_index=927, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyBgt2fxeePoAkX_5RLjivzy_v-AIGUtxvL2SBhrgyP6d0Ekqr1WELMMWLUzO00iMYxjWCxwCyeJRjoQ_RkalU6V92ZsoOWf6g31squ02Nzsy9Tu7JUd9ZddK6cl3wb7k09HaWilZ17Zbumv5qFNkfB1sOEB2end8FJIu_VVr5m14DnZWJZ3kNbiY3ee73dJGv', start_index=918)
Annotation(end_index=1196, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF26iFNHRm9b-5qx-QBHBIgFbfh2tINgTWFUgECCpRWqz78SKjWdF2HO6ApP1rWsl__yDg6hlldc4Obh9psi28S6e18osgQ_9cfEfyirigii7gilXeM1P2RUdKRiYKiujbDWvY1ue9P6ITiSuQqY1ohhI31j2lc5K9xmtdIu4TRPIX9Nu1TPg-kTwQGVDo7x6EO13XtMV5q6-3oK0CPNgefCjnL4qPzSr-TaSfHUcb3X6FmNiTppEZlR8549JvViUEEtqbIVu_wS81QZsC0Jg==', start_index=1187)
Annotation(end_index=1447, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-f-E3s01wunL6JKUhrG_wNpSXI966YTWiga_9IY22obiAlZMfhXDnKiQIzRfWphNvpUYTd9PVos2jjluJD8gUraoeJLhC0EqLxbtD3MzmTPF0IuSzYA_XEPRbnrCEuRU8lwOJrw==', start_index=1435)
Annotation(end_index=1447, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjhdRRcCjyVjwiq5s-ilcCLp8_SD4TUjPwVtlzF5m-SH1fZMcP75DNO3kXSf-zft89SO8KQfz2BNjiCN-xsRXbDxAVB7huE0txakFtkKV2AhiGLDb8BlFGxSh_NkKNva3UCy90DoddULMOZ0L2', start_index=1435)
Annotation(end_index=3407, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7ixHSlXHI792qIlODqHfTzDJxmw4LlBeh1-8qQ6M9gyXzte76han9r4WIAbhwya0K0kgiZSmhy7rgS7dwwKICvOgepiy0izx7qpfSpJZONVJXIKQ1mzPG41HVMDkKnB87PD1k_iOPdCSdXFSsrYt6bTSVEvkTYqhfwvuD_1w0Rlub', start_index=3394)
Annotation(end_index=3407, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8c9NrddBh9PNVTTvmTxYgq4Bof8xZnZmc-Ys9pK3Fxvj3ckb3LlFuGZ8HZtP6DEYBPaNbpLq-7nSlYg6BtsjjRyLSRri1VzIFhurEEcAdiQw4hISMGkckJ1ZTSNazhU3IWXDvPxWSelvrX5R_Q_aGhIkXB0_Z90DtnvbhnsvkMxRJoRJ2K-vjCVoNtwqk681ljvRd8w==', start_index=3394)
Annotation(end_index=3675, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9Ium619G7FcufZ7tH3dB_xsIrLjkFDBgVcO7z8hDBie3waUEMvvpaaOtXQVZtfev5L2SLgL39M625faNsmlf9m8ncMhwbdtUpQYzd_V4jyCq1j2Zgi9k0g_fFZ3K1zqyiTeBuXuNNHA==', start_index=3665)
Annotation(end_index=4131, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFESkgva78Y1H0E8qb5SP7d7YHuPblJNCQEoOOKmDoD9sWURzoUqKPCpFRyTuAZMr0TvKKn9NiGjC1uF9v-OpueOZhzANjrJVIuEXzFYFLki4sjzXDpzUxoVIMiIg37qeXc_QkYj-XMsda3zNhmk5E1kvtCv_Rpd86mYgTEPhYKJdQWYcdPzVmpq2nuKNeO7vfOglKOAR_XplMu11O4C3hg8RqhWqZNsx5c-v78sd0=', start_index=4122)
Annotation(end_index=4328, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-f-E3s01wunL6JKUhrG_wNpSXI966YTWiga_9IY22obiAlZMfhXDnKiQIzRfWphNvpUYTd9PVos2jjluJD8gUraoeJLhC0EqLxbtD3MzmTPF0IuSzYA_XEPRbnrCEuRU8lwOJrw==', start_index=4316)
Annotation(end_index=4328, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjhdRRcCjyVjwiq5s-ilcCLp8_SD4TUjPwVtlzF5m-SH1fZMcP75DNO3kXSf-zft89SO8KQfz2BNjiCN-xsRXbDxAVB7huE0txakFtkKV2AhiGLDb8BlFGxSh_NkKNva3UCy90DoddULMOZ0L2', start_index=4316)
Annotation(end_index=4604, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHODTLrVrzxAQ2X192qbB4PS-MxdovIt5mlNfYhD7D1CEo2EuaOEXgI7M9Ty4zDlIx3iXM6swz9KwaMm3WpEQcn2BCvkfI2Ofeh8bhm8_hzqN4mNZ60-e8CGpiyj-yH4zHeqz8V0VkZergnzdk=', start_index=4590)
Annotation(end_index=4604, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcsw_T6Ki9AbJyZ6kdYkygJeZw5H_vNOYFTzwNzMsBfTPNxyF_SD6KxFOko5RpNrbqilDjx5X6-KcAlO2fJRyHQNrp-FMH74Jl0lwlPU-rkBWl5sN9qWp7-SNagEsvBD0tXWvyOmi3-5aj4neJrkc6hpoNhg==', start_index=4590)
Annotation(end_index=5123, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGeJwMJ6ahMsWN7zOAaf_cZtGASe7FrMc781theRdchKphWjR1w2XGvLMKcRLMEChxFWYJHwD5M0MP6OaJzsZ0XyocKY26VChVbLQmMRD0qktrz6D-uG00EPk7wuyDAWD749A94_GPvjBtdA==', start_index=5109)
Annotation(end_index=5123, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8kmOHyGkbyoD69dJm1d9NzDvR1QogyIXxAq96mxgsVsi13GE7N1Hwq9_Q91I_HBkQgLdmsR-CtKUlavVIiufsyrDvFzAgOipR6kIS71XJ3dah_cN-R1p93wkZaTvs8b4LJ5kuINY=', start_index=5109)
Annotation(end_index=5272, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESPfRZFeUCzEmjqygTSzofr0rp9KisEA6XtINOZALFMBru3CAh3wtCwjuBSA0J8fB9yrXIqVKCNMZ0HYmldiHUQV1Nx4wi1rzc2W07QtoRE3aeWtA2Q-TZJf06MTSpRHBprAN_cGoZP7rOWu6F5Ft9Y0Ph8njJcRFtdv-G1DSw28miT_D7ncCVVC0xZe33e29f', start_index=5260)
Annotation(end_index=5272, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwS8NpXIf7sd0nHwh1Lnu4VhhNYjSt28T9VdfHn2ne8tqZ8JE5BTo0gyQ_GrRM0O1NGgxNDLQ_18nfmMozZ4X6S7d7CZVMlSEn-r1RqC_KbPWDdCswmIGrkoyswKLnyfb5Rz6SbJHd6xtMJuzmnUUfWrmWAKldPPmMUtmxta05yZudgWRiQKaAueE2', start_index=5260)
Annotation(end_index=5568, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESPfRZFeUCzEmjqygTSzofr0rp9KisEA6XtINOZALFMBru3CAh3wtCwjuBSA0J8fB9yrXIqVKCNMZ0HYmldiHUQV1Nx4wi1rzc2W07QtoRE3aeWtA2Q-TZJf06MTSpRHBprAN_cGoZP7rOWu6F5Ft9Y0Ph8njJcRFtdv-G1DSw28miT_D7ncCVVC0xZe33e29f', start_index=5553)
Annotation(end_index=5568, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFESkgva78Y1H0E8qb5SP7d7YHuPblJNCQEoOOKmDoD9sWURzoUqKPCpFRyTuAZMr0TvKKn9NiGjC1uF9v-OpueOZhzANjrJVIuEXzFYFLki4sjzXDpzUxoVIMiIg37qeXc_QkYj-XMsda3zNhmk5E1kvtCv_Rpd86mYgTEPhYKJdQWYcdPzVmpq2nuKNeO7vfOglKOAR_XplMu11O4C3hg8RqhWqZNsx5c-v78sd0=', start_index=5553)
Annotation(end_index=5568, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwS8NpXIf7sd0nHwh1Lnu4VhhNYjSt28T9VdfHn2ne8tqZ8JE5BTo0gyQ_GrRM0O1NGgxNDLQ_18nfmMozZ4X6S7d7CZVMlSEn-r1RqC_KbPWDdCswmIGrkoyswKLnyfb5Rz6SbJHd6xtMJuzmnUUfWrmWAKldPPmMUtmxta05yZudgWRiQKaAueE2', start_index=5553)
Annotation(end_index=5753, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFESkgva78Y1H0E8qb5SP7d7YHuPblJNCQEoOOKmDoD9sWURzoUqKPCpFRyTuAZMr0TvKKn9NiGjC1uF9v-OpueOZhzANjrJVIuEXzFYFLki4sjzXDpzUxoVIMiIg37qeXc_QkYj-XMsda3zNhmk5E1kvtCv_Rpd86mYgTEPhYKJdQWYcdPzVmpq2nuKNeO7vfOglKOAR_XplMu11O4C3hg8RqhWqZNsx5c-v78sd0=', start_index=5741)
Annotation(end_index=5753, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwS8NpXIf7sd0nHwh1Lnu4VhhNYjSt28T9VdfHn2ne8tqZ8JE5BTo0gyQ_GrRM0O1NGgxNDLQ_18nfmMozZ4X6S7d7CZVMlSEn-r1RqC_KbPWDdCswmIGrkoyswKLnyfb5Rz6SbJHd6xtMJuzmnUUfWrmWAKldPPmMUtmxta05yZudgWRiQKaAueE2', start_index=5741)
Annotation(end_index=6287, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7kQ9Px_DPd4CFfacvkb0WexTOpyeUoMHI6d2RHGMHBskBcyNGN6fx0ra09yPxcBNYII3YHEXa_1DwCqtvi16TaXtF2PJ3pxkPMRspAi2MRCENgbGsq5dVeS4RgTXch_g5L5SUTXCh3h4yQh4HSz2BYbnQQu9iW_x8mE_6s-0loaQ1K3DhbkWKt2kc0GbpwK9P8wfVtetr7pxu5mJVSjQ=', start_index=6278)
Annotation(end_index=6504, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7kQ9Px_DPd4CFfacvkb0WexTOpyeUoMHI6d2RHGMHBskBcyNGN6fx0ra09yPxcBNYII3YHEXa_1DwCqtvi16TaXtF2PJ3pxkPMRspAi2MRCENgbGsq5dVeS4RgTXch_g5L5SUTXCh3h4yQh4HSz2BYbnQQu9iW_x8mE_6s-0loaQ1K3DhbkWKt2kc0GbpwK9P8wfVtetr7pxu5mJVSjQ=', start_index=6495)
Annotation(end_index=6680, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9Ium619G7FcufZ7tH3dB_xsIrLjkFDBgVcO7z8hDBie3waUEMvvpaaOtXQVZtfev5L2SLgL39M625faNsmlf9m8ncMhwbdtUpQYzd_V4jyCq1j2Zgi9k0g_fFZ3K1zqyiTeBuXuNNHA==', start_index=6666)
Annotation(end_index=6680, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGeJwMJ6ahMsWN7zOAaf_cZtGASe7FrMc781theRdchKphWjR1w2XGvLMKcRLMEChxFWYJHwD5M0MP6OaJzsZ0XyocKY26VChVbLQmMRD0qktrz6D-uG00EPk7wuyDAWD749A94_GPvjBtdA==', start_index=6666)
Annotation(end_index=7002, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9Ium619G7FcufZ7tH3dB_xsIrLjkFDBgVcO7z8hDBie3waUEMvvpaaOtXQVZtfev5L2SLgL39M625faNsmlf9m8ncMhwbdtUpQYzd_V4jyCq1j2Zgi9k0g_fFZ3K1zqyiTeBuXuNNHA==', start_index=6992)
Annotation(end_index=7457, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyBgt2fxeePoAkX_5RLjivzy_v-AIGUtxvL2SBhrgyP6d0Ekqr1WELMMWLUzO00iMYxjWCxwCyeJRjoQ_RkalU6V92ZsoOWf6g31squ02Nzsy9Tu7JUd9ZddK6cl3wb7k09HaWilZ17Zbumv5qFNkfB1sOEB2end8FJIu_VVr5m14DnZWJZ3kNbiY3ee73dJGv', start_index=7448)
Annotation(end_index=7921, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyBgt2fxeePoAkX_5RLjivzy_v-AIGUtxvL2SBhrgyP6d0Ekqr1WELMMWLUzO00iMYxjWCxwCyeJRjoQ_RkalU6V92ZsoOWf6g31squ02Nzsy9Tu7JUd9ZddK6cl3wb7k09HaWilZ17Zbumv5qFNkfB1sOEB2end8FJIu_VVr5m14DnZWJZ3kNbiY3ee73dJGv', start_index=7912)
Annotation(end_index=8189, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF26iFNHRm9b-5qx-QBHBIgFbfh2tINgTWFUgECCpRWqz78SKjWdF2HO6ApP1rWsl__yDg6hlldc4Obh9psi28S6e18osgQ_9cfEfyirigii7gilXeM1P2RUdKRiYKiujbDWvY1ue9P6ITiSuQqY1ohhI31j2lc5K9xmtdIu4TRPIX9Nu1TPg-kTwQGVDo7x6EO13XtMV5q6-3oK0CPNgefCjnL4qPzSr-TaSfHUcb3X6FmNiTppEZlR8549JvViUEEtqbIVu_wS81QZsC0Jg==', start_index=8180)
Annotation(end_index=8369, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7kQ9Px_DPd4CFfacvkb0WexTOpyeUoMHI6d2RHGMHBskBcyNGN6fx0ra09yPxcBNYII3YHEXa_1DwCqtvi16TaXtF2PJ3pxkPMRspAi2MRCENgbGsq5dVeS4RgTXch_g5L5SUTXCh3h4yQh4HSz2BYbnQQu9iW_x8mE_6s-0loaQ1K3DhbkWKt2kc0GbpwK9P8wfVtetr7pxu5mJVSjQ=', start_index=8356)
Annotation(end_index=8369, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKqDQGYfQFmvo2HIvgEp9Vx3j0nLliE9CoM3ZI6PRuff-EIj95PPsDsQGauMy5tlR0gqnbtDYGdudt42c3uXzQd2VtqdknlwiJQZfsvO1dCbAbFzZ5VhkZBboXpoCHzsNYSta7i3jWyxsU', start_index=8356)
Annotation(end_index=8641, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF26iFNHRm9b-5qx-QBHBIgFbfh2tINgTWFUgECCpRWqz78SKjWdF2HO6ApP1rWsl__yDg6hlldc4Obh9psi28S6e18osgQ_9cfEfyirigii7gilXeM1P2RUdKRiYKiujbDWvY1ue9P6ITiSuQqY1ohhI31j2lc5K9xmtdIu4TRPIX9Nu1TPg-kTwQGVDo7x6EO13XtMV5q6-3oK0CPNgefCjnL4qPzSr-TaSfHUcb3X6FmNiTppEZlR8549JvViUEEtqbIVu_wS81QZsC0Jg==', start_index=8628)
Annotation(end_index=8641, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQ5sNHDe1i06q4P8K3ubc4QVmqSWzWueef6-s_KgxEyo3dreAF1fROPN7zxtENdLlvrvYjl8BgYtV1BWQfTCglvi1Pbq2yrgGUOmQ3BoCMsMnuIndoatB98piRzBFAGvfGvxEaozRuIznGJsw=', start_index=8628)
Annotation(end_index=8958, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-f-E3s01wunL6JKUhrG_wNpSXI966YTWiga_9IY22obiAlZMfhXDnKiQIzRfWphNvpUYTd9PVos2jjluJD8gUraoeJLhC0EqLxbtD3MzmTPF0IuSzYA_XEPRbnrCEuRU8lwOJrw==', start_index=8946)
Annotation(end_index=8958, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjhdRRcCjyVjwiq5s-ilcCLp8_SD4TUjPwVtlzF5m-SH1fZMcP75DNO3kXSf-zft89SO8KQfz2BNjiCN-xsRXbDxAVB7huE0txakFtkKV2AhiGLDb8BlFGxSh_NkKNva3UCy90DoddULMOZ0L2', start_index=8946)
Annotation(end_index=9422, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-f-E3s01wunL6JKUhrG_wNpSXI966YTWiga_9IY22obiAlZMfhXDnKiQIzRfWphNvpUYTd9PVos2jjluJD8gUraoeJLhC0EqLxbtD3MzmTPF0IuSzYA_XEPRbnrCEuRU8lwOJrw==', start_index=9413)
Annotation(end_index=9669, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMja3yhLGDwwcX7K0S9dohBMu4o5piSQWsvLUPoV8T_1fX_C9ViyZOriMT598WacmsfawmcsY8lmbOPQG_Oc40w_MPxF_2jYnRhlcGUolhROQjB7p9lshJAPaG2M-gayhZrTXt74tqs2d21mmLLLphDO6Fy315f2mulRgyp7KUSKRyd38U_BWcDSr9H10RzQ==', start_index=9655)
Annotation(end_index=9669, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcsw_T6Ki9AbJyZ6kdYkygJeZw5H_vNOYFTzwNzMsBfTPNxyF_SD6KxFOko5RpNrbqilDjx5X6-KcAlO2fJRyHQNrp-FMH74Jl0lwlPU-rkBWl5sN9qWp7-SNagEsvBD0tXWvyOmi3-5aj4neJrkc6hpoNhg==', start_index=9655)
Annotation(end_index=9873, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9Ium619G7FcufZ7tH3dB_xsIrLjkFDBgVcO7z8hDBie3waUEMvvpaaOtXQVZtfev5L2SLgL39M625faNsmlf9m8ncMhwbdtUpQYzd_V4jyCq1j2Zgi9k0g_fFZ3K1zqyiTeBuXuNNHA==', start_index=9863)
Annotation(end_index=10127, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjl19kZTNdk_IrnOIQzkZtTAQMKlCybUaFdrvNnzzljHC8tnwA8n6povQ4-PzwBqGxOOLkqt8Os90_TKN1hrqi6Zfe6bSa6todjod9AlYu3H4jGgX2nUwYmUmwZ0Mwv_sU4sNiI6kjbxWJUlHWTge0Xcgzv-8o0woFoFYzMtgzHQ==', start_index=10113)
Annotation(end_index=10127, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfZcIdsRhEAMqTcxoil2ABaXzYgcAx7uMiJQll0fp7o2wZ2LkM1I2QNMyschcfJJxGzKjdGITBWkzgcsZJ-wyHBVKp8K1eheBCMnl-4nt5pVW5jlXcmXOaotNzaAB-ULUIVJn_uYA=', start_index=10113)
Annotation(end_index=10580, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfZcIdsRhEAMqTcxoil2ABaXzYgcAx7uMiJQll0fp7o2wZ2LkM1I2QNMyschcfJJxGzKjdGITBWkzgcsZJ-wyHBVKp8K1eheBCMnl-4nt5pVW5jlXcmXOaotNzaAB-ULUIVJn_uYA=', start_index=10567)
Annotation(end_index=10580, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyBgt2fxeePoAkX_5RLjivzy_v-AIGUtxvL2SBhrgyP6d0Ekqr1WELMMWLUzO00iMYxjWCxwCyeJRjoQ_RkalU6V92ZsoOWf6g31squ02Nzsy9Tu7JUd9ZddK6cl3wb7k09HaWilZ17Zbumv5qFNkfB1sOEB2end8FJIu_VVr5m14DnZWJZ3kNbiY3ee73dJGv', start_index=10567)
Annotation(end_index=10704, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfZcIdsRhEAMqTcxoil2ABaXzYgcAx7uMiJQll0fp7o2wZ2LkM1I2QNMyschcfJJxGzKjdGITBWkzgcsZJ-wyHBVKp8K1eheBCMnl-4nt5pVW5jlXcmXOaotNzaAB-ULUIVJn_uYA=', start_index=10694)
Annotation(end_index=11855, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwNVfG9M6qYyQC7oYx3d9uqOS_BxzG0GVoDVHiLqdLVKASLRcEY5bJUMhmE7vB1CTcjYw-VSUYbXKbAXZ1wHNFnB1lzarwvcDEqCQw-Hw1iQM9MNutJuyLwNW05yCHQhc1XC4ljfp7gUyuDVqy-t3tKc7tUuJ9w5BdET8LHPbMxBIq8LvgucCi-4qJOn3TGr0JU243laT9-tuI2Q==', start_index=11841)
Annotation(end_index=11855, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7ixHSlXHI792qIlODqHfTzDJxmw4LlBeh1-8qQ6M9gyXzte76han9r4WIAbhwya0K0kgiZSmhy7rgS7dwwKICvOgepiy0izx7qpfSpJZONVJXIKQ1mzPG41HVMDkKnB87PD1k_iOPdCSdXFSsrYt6bTSVEvkTYqhfwvuD_1w0Rlub', start_index=11841)
Annotation(end_index=12056, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7kQ9Px_DPd4CFfacvkb0WexTOpyeUoMHI6d2RHGMHBskBcyNGN6fx0ra09yPxcBNYII3YHEXa_1DwCqtvi16TaXtF2PJ3pxkPMRspAi2MRCENgbGsq5dVeS4RgTXch_g5L5SUTXCh3h4yQh4HSz2BYbnQQu9iW_x8mE_6s-0loaQ1K3DhbkWKt2kc0GbpwK9P8wfVtetr7pxu5mJVSjQ=', start_index=12047)
Annotation(end_index=12450, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfZcIdsRhEAMqTcxoil2ABaXzYgcAx7uMiJQll0fp7o2wZ2LkM1I2QNMyschcfJJxGzKjdGITBWkzgcsZJ-wyHBVKp8K1eheBCMnl-4nt5pVW5jlXcmXOaotNzaAB-ULUIVJn_uYA=', start_index=12440)
Annotation(end_index=12571, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9Ium619G7FcufZ7tH3dB_xsIrLjkFDBgVcO7z8hDBie3waUEMvvpaaOtXQVZtfev5L2SLgL39M625faNsmlf9m8ncMhwbdtUpQYzd_V4jyCq1j2Zgi9k0g_fFZ3K1zqyiTeBuXuNNHA==', start_index=12561)
Annotation(end_index=12829, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsf7eecXzfpB4E42LHWZw-UbarBrAzDy13lDb5PaIt1umh9sUqIbgBxLRFCEZOunsUkDEhFWMwaZHnM7bc8NnnGbtucOKY2YJWtNOVRTJD87Ow9i_gFKsD_iO20FsEKLeoR62S4LcQsg==', start_index=12819)
Annotation(end_index=13261, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsf7eecXzfpB4E42LHWZw-UbarBrAzDy13lDb5PaIt1umh9sUqIbgBxLRFCEZOunsUkDEhFWMwaZHnM7bc8NnnGbtucOKY2YJWtNOVRTJD87Ow9i_gFKsD_iO20FsEKLeoR62S4LcQsg==', start_index=13247)
Annotation(end_index=13261, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgX893Wv-QWEunjy_9FFbd9F7l0AER3TS_us7PcmxgxK7uS_ZwDe18Ma8-4VrDtn8JCzulFXHNP1qIdkYVXcyQuAm7dV9LdWsaWJ0iByokCSwGGgNHotEVkQ1uNTcFqZnRY48FWsHNMTbloUCLs_W-D5jmiHsDROMfU5u_Lka7C85YaJ9WNJ73NUGQ9uGTeRRbqw==', start_index=13247)
Annotation(end_index=13519, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZjiAGox2-lwpQGKLT73J-C2nres5OM6IKRhJ1PlkST9kZQJS1SDi0Vn9vn65xEuRy9jmx-nBO15tWNQAoWIi6zmupql8KnkuWLZdeEfDCsMqW-YMvKopSv_Y-CXkRQAIB0YpZ8sIjvsozdcIJqsGLhOTIdspCSCrdCwuE1as=', start_index=13501)
Annotation(end_index=13519, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuQHxe2xng77eeh7J916E6aTuC6_8lISMb0gISMgsZjtGz8VyiUyaGi4OJQy3v9DszUOFrheF1nC-yv4XY9cOgi-Hmu-CcIilCVMH95sYncauzeAxqmhKaS8inlXFxvLAbQRNYQ5v4IcQFLdVwT3tMEBJdI0LspwudcjEEXmZ0Qi5znSIVxg==', start_index=13501)
Annotation(end_index=13519, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyJxfeiPgbrm4I7bzuECbyeOrPz1f3oTipDyDeDpikb4GkiQnW1b9JJ7LKYHsLZI3j1es2nm4GV_Re1r3xKtydFRroHwfoh4hpV2lWw1FP8nSuMSVobtK0uUQhY4Y0c4RiTJzHvbvvfgx0WnFxBhA=', start_index=13501)
Annotation(end_index=13708, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-f-E3s01wunL6JKUhrG_wNpSXI966YTWiga_9IY22obiAlZMfhXDnKiQIzRfWphNvpUYTd9PVos2jjluJD8gUraoeJLhC0EqLxbtD3MzmTPF0IuSzYA_XEPRbnrCEuRU8lwOJrw==', start_index=13699)
Annotation(end_index=14126, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7kQ9Px_DPd4CFfacvkb0WexTOpyeUoMHI6d2RHGMHBskBcyNGN6fx0ra09yPxcBNYII3YHEXa_1DwCqtvi16TaXtF2PJ3pxkPMRspAi2MRCENgbGsq5dVeS4RgTXch_g5L5SUTXCh3h4yQh4HSz2BYbnQQu9iW_x8mE_6s-0loaQ1K3DhbkWKt2kc0GbpwK9P8wfVtetr7pxu5mJVSjQ=', start_index=14117)
Annotation(end_index=14445, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7kQ9Px_DPd4CFfacvkb0WexTOpyeUoMHI6d2RHGMHBskBcyNGN6fx0ra09yPxcBNYII3YHEXa_1DwCqtvi16TaXtF2PJ3pxkPMRspAi2MRCENgbGsq5dVeS4RgTXch_g5L5SUTXCh3h4yQh4HSz2BYbnQQu9iW_x8mE_6s-0loaQ1K3DhbkWKt2kc0GbpwK9P8wfVtetr7pxu5mJVSjQ=', start_index=14436)
Annotation(end_index=14936, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKqDQGYfQFmvo2HIvgEp9Vx3j0nLliE9CoM3ZI6PRuff-EIj95PPsDsQGauMy5tlR0gqnbtDYGdudt42c3uXzQd2VtqdknlwiJQZfsvO1dCbAbFzZ5VhkZBboXpoCHzsNYSta7i3jWyxsU', start_index=14926)
Annotation(end_index=15962, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG8c9NrddBh9PNVTTvmTxYgq4Bof8xZnZmc-Ys9pK3Fxvj3ckb3LlFuGZ8HZtP6DEYBPaNbpLq-7nSlYg6BtsjjRyLSRri1VzIFhurEEcAdiQw4hISMGkckJ1ZTSNazhU3IWXDvPxWSelvrX5R_Q_aGhIkXB0_Z90DtnvbhnsvkMxRJoRJ2K-vjCVoNtwqk681ljvRd8w==', start_index=15953)
Annotation(end_index=16037, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7ixHSlXHI792qIlODqHfTzDJxmw4LlBeh1-8qQ6M9gyXzte76han9r4WIAbhwya0K0kgiZSmhy7rgS7dwwKICvOgepiy0izx7qpfSpJZONVJXIKQ1mzPG41HVMDkKnB87PD1k_iOPdCSdXFSsrYt6bTSVEvkTYqhfwvuD_1w0Rlub', start_index=16027)
Annotation(end_index=16116, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMja3yhLGDwwcX7K0S9dohBMu4o5piSQWsvLUPoV8T_1fX_C9ViyZOriMT598WacmsfawmcsY8lmbOPQG_Oc40w_MPxF_2jYnRhlcGUolhROQjB7p9lshJAPaG2M-gayhZrTXt74tqs2d21mmLLLphDO6Fy315f2mulRgyp7KUSKRyd38U_BWcDSr9H10RzQ==', start_index=16106)
Annotation(end_index=16159, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKqDQGYfQFmvo2HIvgEp9Vx3j0nLliE9CoM3ZI6PRuff-EIj95PPsDsQGauMy5tlR0gqnbtDYGdudt42c3uXzQd2VtqdknlwiJQZfsvO1dCbAbFzZ5VhkZBboXpoCHzsNYSta7i3jWyxsU', start_index=16149)
Annotation(end_index=16211, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHODTLrVrzxAQ2X192qbB4PS-MxdovIt5mlNfYhD7D1CEo2EuaOEXgI7M9Ty4zDlIx3iXM6swz9KwaMm3WpEQcn2BCvkfI2Ofeh8bhm8_hzqN4mNZ60-e8CGpiyj-yH4zHeqz8V0VkZergnzdk=', start_index=16201)
Annotation(end_index=16267, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwNVfG9M6qYyQC7oYx3d9uqOS_BxzG0GVoDVHiLqdLVKASLRcEY5bJUMhmE7vB1CTcjYw-VSUYbXKbAXZ1wHNFnB1lzarwvcDEqCQw-Hw1iQM9MNutJuyLwNW05yCHQhc1XC4ljfp7gUyuDVqy-t3tKc7tUuJ9w5BdET8LHPbMxBIq8LvgucCi-4qJOn3TGr0JU243laT9-tuI2Q==', start_index=16257)
Annotation(end_index=16326, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfZcIdsRhEAMqTcxoil2ABaXzYgcAx7uMiJQll0fp7o2wZ2LkM1I2QNMyschcfJJxGzKjdGITBWkzgcsZJ-wyHBVKp8K1eheBCMnl-4nt5pVW5jlXcmXOaotNzaAB-ULUIVJn_uYA=', start_index=16316)
Annotation(end_index=16380, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQ5sNHDe1i06q4P8K3ubc4QVmqSWzWueef6-s_KgxEyo3dreAF1fROPN7zxtENdLlvrvYjl8BgYtV1BWQfTCglvi1Pbq2yrgGUOmQ3BoCMsMnuIndoatB98piRzBFAGvfGvxEaozRuIznGJsw=', start_index=16370)
Annotation(end_index=16429, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFESkgva78Y1H0E8qb5SP7d7YHuPblJNCQEoOOKmDoD9sWURzoUqKPCpFRyTuAZMr0TvKKn9NiGjC1uF9v-OpueOZhzANjrJVIuEXzFYFLki4sjzXDpzUxoVIMiIg37qeXc_QkYj-XMsda3zNhmk5E1kvtCv_Rpd86mYgTEPhYKJdQWYcdPzVmpq2nuKNeO7vfOglKOAR_XplMu11O4C3hg8RqhWqZNsx5c-v78sd0=', start_index=16420)
Annotation(end_index=16512, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF26iFNHRm9b-5qx-QBHBIgFbfh2tINgTWFUgECCpRWqz78SKjWdF2HO6ApP1rWsl__yDg6hlldc4Obh9psi28S6e18osgQ_9cfEfyirigii7gilXeM1P2RUdKRiYKiujbDWvY1ue9P6ITiSuQqY1ohhI31j2lc5K9xmtdIu4TRPIX9Nu1TPg-kTwQGVDo7x6EO13XtMV5q6-3oK0CPNgefCjnL4qPzSr-TaSfHUcb3X6FmNiTppEZlR8549JvViUEEtqbIVu_wS81QZsC0Jg==', start_index=16503)
Annotation(end_index=16610, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESPfRZFeUCzEmjqygTSzofr0rp9KisEA6XtINOZALFMBru3CAh3wtCwjuBSA0J8fB9yrXIqVKCNMZ0HYmldiHUQV1Nx4wi1rzc2W07QtoRE3aeWtA2Q-TZJf06MTSpRHBprAN_cGoZP7rOWu6F5Ft9Y0Ph8njJcRFtdv-G1DSw28miT_D7ncCVVC0xZe33e29f', start_index=16601)
Annotation(end_index=16691, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgX893Wv-QWEunjy_9FFbd9F7l0AER3TS_us7PcmxgxK7uS_ZwDe18Ma8-4VrDtn8JCzulFXHNP1qIdkYVXcyQuAm7dV9LdWsaWJ0iByokCSwGGgNHotEVkQ1uNTcFqZnRY48FWsHNMTbloUCLs_W-D5jmiHsDROMfU5u_Lka7C85YaJ9WNJ73NUGQ9uGTeRRbqw==', start_index=16681)
Annotation(end_index=16780, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9Ium619G7FcufZ7tH3dB_xsIrLjkFDBgVcO7z8hDBie3waUEMvvpaaOtXQVZtfev5L2SLgL39M625faNsmlf9m8ncMhwbdtUpQYzd_V4jyCq1j2Zgi9k0g_fFZ3K1zqyiTeBuXuNNHA==', start_index=16770)
Annotation(end_index=16831, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGeJwMJ6ahMsWN7zOAaf_cZtGASe7FrMc781theRdchKphWjR1w2XGvLMKcRLMEChxFWYJHwD5M0MP6OaJzsZ0XyocKY26VChVbLQmMRD0qktrz6D-uG00EPk7wuyDAWD749A94_GPvjBtdA==', start_index=16821)
Annotation(end_index=16882, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcsw_T6Ki9AbJyZ6kdYkygJeZw5H_vNOYFTzwNzMsBfTPNxyF_SD6KxFOko5RpNrbqilDjx5X6-KcAlO2fJRyHQNrp-FMH74Jl0lwlPU-rkBWl5sN9qWp7-SNagEsvBD0tXWvyOmi3-5aj4neJrkc6hpoNhg==', start_index=16872)
Annotation(end_index=16945, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7ixHSlXHI792qIlODqHfTzDJxmw4LlBeh1-8qQ6M9gyXzte76han9r4WIAbhwya0K0kgiZSmhy7rgS7dwwKICvOgepiy0izx7qpfSpJZONVJXIKQ1mzPG41HVMDkKnB87PD1k_iOPdCSdXFSsrYt6bTSVEvkTYqhfwvuD_1w0Rlub', start_index=16935)
Annotation(end_index=17008, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjl19kZTNdk_IrnOIQzkZtTAQMKlCybUaFdrvNnzzljHC8tnwA8n6povQ4-PzwBqGxOOLkqt8Os90_TKN1hrqi6Zfe6bSa6todjod9AlYu3H4jGgX2nUwYmUmwZ0Mwv_sU4sNiI6kjbxWJUlHWTge0Xcgzv-8o0woFoFYzMtgzHQ==', start_index=16998)
Annotation(end_index=17088, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyBgt2fxeePoAkX_5RLjivzy_v-AIGUtxvL2SBhrgyP6d0Ekqr1WELMMWLUzO00iMYxjWCxwCyeJRjoQ_RkalU6V92ZsoOWf6g31squ02Nzsy9Tu7JUd9ZddK6cl3wb7k09HaWilZ17Zbumv5qFNkfB1sOEB2end8FJIu_VVr5m14DnZWJZ3kNbiY3ee73dJGv', start_index=17079)
Annotation(end_index=17154, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrqnOa6ztqvzVyPeHW33HWRx38W49tkrtYnOaIFL8Amf6PF2JVeLxNJulklWoJNwYsXRuPLUVmhuNMsfgl3hKtmDglHU01eoEVg5lwL6ilMQikoaNF8HN3b_IBOn3YuLmBVzNPya9ROUxdrAIxQxnBmfX-5lxJSebG', start_index=17144)
Annotation(end_index=17234, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7kQ9Px_DPd4CFfacvkb0WexTOpyeUoMHI6d2RHGMHBskBcyNGN6fx0ra09yPxcBNYII3YHEXa_1DwCqtvi16TaXtF2PJ3pxkPMRspAi2MRCENgbGsq5dVeS4RgTXch_g5L5SUTXCh3h4yQh4HSz2BYbnQQu9iW_x8mE_6s-0loaQ1K3DhbkWKt2kc0GbpwK9P8wfVtetr7pxu5mJVSjQ=', start_index=17225)
Annotation(end_index=17303, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZjiAGox2-lwpQGKLT73J-C2nres5OM6IKRhJ1PlkST9kZQJS1SDi0Vn9vn65xEuRy9jmx-nBO15tWNQAoWIi6zmupql8KnkuWLZdeEfDCsMqW-YMvKopSv_Y-CXkRQAIB0YpZ8sIjvsozdcIJqsGLhOTIdspCSCrdCwuE1as=', start_index=17293)
Annotation(end_index=17367, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuQHxe2xng77eeh7J916E6aTuC6_8lISMb0gISMgsZjtGz8VyiUyaGi4OJQy3v9DszUOFrheF1nC-yv4XY9cOgi-Hmu-CcIilCVMH95sYncauzeAxqmhKaS8inlXFxvLAbQRNYQ5v4IcQFLdVwT3tMEBJdI0LspwudcjEEXmZ0Qi5znSIVxg==', start_index=17357)
Annotation(end_index=17422, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyJxfeiPgbrm4I7bzuECbyeOrPz1f3oTipDyDeDpikb4GkiQnW1b9JJ7LKYHsLZI3j1es2nm4GV_Re1r3xKtydFRroHwfoh4hpV2lWw1FP8nSuMSVobtK0uUQhY4Y0c4RiTJzHvbvvfgx0WnFxBhA=', start_index=17412)
Annotation(end_index=17472, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFESkgva78Y1H0E8qb5SP7d7YHuPblJNCQEoOOKmDoD9sWURzoUqKPCpFRyTuAZMr0TvKKn9NiGjC1uF9v-OpueOZhzANjrJVIuEXzFYFLki4sjzXDpzUxoVIMiIg37qeXc_QkYj-XMsda3zNhmk5E1kvtCv_Rpd86mYgTEPhYKJdQWYcdPzVmpq2nuKNeO7vfOglKOAR_XplMu11O4C3hg8RqhWqZNsx5c-v78sd0=', start_index=17463)
Annotation(end_index=17544, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwS8NpXIf7sd0nHwh1Lnu4VhhNYjSt28T9VdfHn2ne8tqZ8JE5BTo0gyQ_GrRM0O1NGgxNDLQ_18nfmMozZ4X6S7d7CZVMlSEn-r1RqC_KbPWDdCswmIGrkoyswKLnyfb5Rz6SbJHd6xtMJuzmnUUfWrmWAKldPPmMUtmxta05yZudgWRiQKaAueE2', start_index=17535)
Annotation(end_index=17625, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8kmOHyGkbyoD69dJm1d9NzDvR1QogyIXxAq96mxgsVsi13GE7N1Hwq9_Q91I_HBkQgLdmsR-CtKUlavVIiufsyrDvFzAgOipR6kIS71XJ3dah_cN-R1p93wkZaTvs8b4LJ5kuINY=', start_index=17615)
Annotation(end_index=17676, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7kQ9Px_DPd4CFfacvkb0WexTOpyeUoMHI6d2RHGMHBskBcyNGN6fx0ra09yPxcBNYII3YHEXa_1DwCqtvi16TaXtF2PJ3pxkPMRspAi2MRCENgbGsq5dVeS4RgTXch_g5L5SUTXCh3h4yQh4HSz2BYbnQQu9iW_x8mE_6s-0loaQ1K3DhbkWKt2kc0GbpwK9P8wfVtetr7pxu5mJVSjQ=', start_index=17667)
Annotation(end_index=17737, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF26iFNHRm9b-5qx-QBHBIgFbfh2tINgTWFUgECCpRWqz78SKjWdF2HO6ApP1rWsl__yDg6hlldc4Obh9psi28S6e18osgQ_9cfEfyirigii7gilXeM1P2RUdKRiYKiujbDWvY1ue9P6ITiSuQqY1ohhI31j2lc5K9xmtdIu4TRPIX9Nu1TPg-kTwQGVDo7x6EO13XtMV5q6-3oK0CPNgefCjnL4qPzSr-TaSfHUcb3X6FmNiTppEZlR8549JvViUEEtqbIVu_wS81QZsC0Jg==', start_index=17728)
Annotation(end_index=17820, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjhdRRcCjyVjwiq5s-ilcCLp8_SD4TUjPwVtlzF5m-SH1fZMcP75DNO3kXSf-zft89SO8KQfz2BNjiCN-xsRXbDxAVB7huE0txakFtkKV2AhiGLDb8BlFGxSh_NkKNva3UCy90DoddULMOZ0L2', start_index=17811)
Annotation(end_index=17879, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-f-E3s01wunL6JKUhrG_wNpSXI966YTWiga_9IY22obiAlZMfhXDnKiQIzRfWphNvpUYTd9PVos2jjluJD8gUraoeJLhC0EqLxbtD3MzmTPF0IuSzYA_XEPRbnrCEuRU8lwOJrw==', start_index=17870)
Annotation(end_index=17935, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9Ium619G7FcufZ7tH3dB_xsIrLjkFDBgVcO7z8hDBie3waUEMvvpaaOtXQVZtfev5L2SLgL39M625faNsmlf9m8ncMhwbdtUpQYzd_V4jyCq1j2Zgi9k0g_fFZ3K1zqyiTeBuXuNNHA==', start_index=17925)
Annotation(end_index=17998, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsf7eecXzfpB4E42LHWZw-UbarBrAzDy13lDb5PaIt1umh9sUqIbgBxLRFCEZOunsUkDEhFWMwaZHnM7bc8NnnGbtucOKY2YJWtNOVRTJD87Ow9i_gFKsD_iO20FsEKLeoR62S4LcQsg==', start_index=17988)
Annotation(end_index=18049, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWvBxcEkR9Bthpa7E2ZZA2p3IPJB59tcf7mfvcr8qOgj0LzP9OmZ2I-0If1EW_BqSSqCbBEVmrFay-TRIS9c2khLpJtD6ZGFUEjKM2QCsH9wYzP6tqIp0yKqNsDzczYM1LMeHQuQd5FAUFxEEF5iTmpk5-KSeEM0qFzuYUZ6tjhJw9ubPGlz4ZFElVecVXkyV-ldEmot8vqqKTijFjqaORZ0tqYRtAa328ETz4NIegXqg-mf86g38Yt5YExPXS2BwDPYDEVfIrGEUg8xyWSB8xzn6xFLoZvxNalMQU_aEIpA8xgyJ86MgceXyAjGI=', start_index=18039)
Annotation(end_index=18118, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHd-uL_x85vkWdljjRd5UR9stjXmzqAREwsZjw2fhAkuxvGwjnMumPhR3EDWqfUR87uyM9ZaMiddktLuNqdbrGHwkEVGasue1XDPaJ6hn8nkscZBjtZT1tLSt_DFcZ8q3SnGLxC', start_index=18108)

## Sources
