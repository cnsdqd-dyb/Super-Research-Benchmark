# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 73f16633 | **Time:** 279.75s | **Cost:** $1.12199
--------------------------------------------------------------------------------

# Optimizing Service-Cost Trade-offs in Safety Stock Strategies under Forecast Error Autocorrelation

### Key Points
*   **Standard Formulas are Flawed:** Traditional safety stock calculations assume forecast errors are independent and identically distributed (IID). Research indicates that ignoring autocorrelation (serial dependence) in forecast errors can lead to safety stocks that are up to 30% too low and service levels significantly below targets [cite: 1].
*   **The Cost of Positive Autocorrelation:** Positive autocorrelation (meandering demand) compounds risk over the lead time. If a forecast is low in one period, it is likely to be low in subsequent periods, requiring significantly higher inventory buffers to maintain the same service level compared to IID demand [cite: 2, 3].
*   **The Benefit of Negative Autocorrelation:** Negative autocorrelation (erratic/choppy demand) can naturally smooth replenishment requirements. This phenomenon can improve lead time performance and reduce the necessary safety stock relative to IID scenarios, provided the inventory policy accounts for it [cite: 2].
*   **Endogenous Lead Times:** Lead times are not purely exogenous; they are influenced by the ordering behavior induced by autocorrelated demand. Strategies that ignore this feedback loop fail to optimize the service-cost frontier [cite: 3, 4].
*   **Optimization Strategy:** To optimize the trade-off, firms must transition from static "square root of time" formulas to dynamic models that incorporate variance correction factors, utilize advanced forecasting (e.g., ARIMA) to "whiten" errors, and adopt dynamic safety stock policies that adjust to volatility shifts [cite: 1, 5, 6].

### Executive Summary
In supply chain management, the safety stock serves as a financial hedge against uncertainty. The fundamental objective is to balance the cost of holding inventory against the cost of stockouts (lost sales and customer dissatisfaction). Most Enterprise Resource Planning (ERP) systems and textbook models calculate this buffer using the standard deviation of forecast error multiplied by the square root of the lead time. This approach relies on the critical assumption that forecast errors are independent across time periods.

However, empirical evidence and advanced inventory theory demonstrate that forecast errors are frequently autocorrelated. When errors are positively correlated, a shortage in week one implies a high probability of a shortage in week two, compounding the risk over the replenishment lead time. Failing to account for this correlation results in a systematic underestimation of risk, leading to service failures despite "optimal" theoretical stock levels. Conversely, negative autocorrelation can lead to over-stocking if standard formulas are used. Optimizing the service-cost trade-off requires abandoning the IID assumption in favor of corrected variance expressions, dynamic inventory policies, and the recognition of endogenous lead time dynamics.

---

## 1. The Mechanics of Forecast Error Autocorrelation

To understand how to optimize safety stock, one must first define the statistical nature of the error being hedged against. Safety stock is not a buffer for total demand; it is a buffer for the *uncertainty* of demand, specifically the portion that cannot be predicted [cite: 6, 7].

### 1.1 Defining Autocorrelation in Supply Chains
Autocorrelation (or serial correlation) occurs when the residual error in a time series prediction is correlated with the error of previous periods. In the context of inventory forecasting:
*   **Positive Autocorrelation:** Indicates a persistence in the direction of error. If actual demand exceeds the forecast in period $t$, it is statistically likely to exceed the forecast in period $t+1$. This is common in "meandering" demand patterns where trends are not fully captured by the forecasting model [cite: 2].
*   **Negative Autocorrelation:** Indicates an oscillatory pattern. An over-forecast in period $t$ is likely followed by an under-forecast in period $t+1$. This is often seen in "erratic" demand or scenarios involving pantry loading, where consumers stock up during promotions and buy less subsequently [cite: 2, 3].

### 1.2 The Failure of the Square Root Rule
The standard industry formula for the standard deviation of demand over lead time ($\sigma_L$) is:
\[ \sigma_L = \sigma_1 \sqrt{L} \]
Where $\sigma_1$ is the standard deviation of forecast error per period and $L$ is the lead time.

This formula is only valid if errors are IID. When errors are positively autocorrelated, the variance grows faster than the square root of time. Research by Prak and Teunter (2016) highlights that using the standard approach under these conditions results in safety stocks that are insufficient to meet target service levels [cite: 1]. The errors do not cancel each other out over the lead time; they accumulate. Consequently, the actual service level achieved is lower than the target service level (e.g., achieving 85% when targeting 95%), implying that the "optimization" is based on flawed inputs.

## 2. The Service-Cost Trade-off Under Autocorrelation

The service-cost trade-off is the decision boundary where a firm decides how much capital to immobilize in inventory to achieve a specific probability of fulfilling demand. Autocorrelation fundamentally shifts this curve.

### 2.1 The Non-Linear Cost of High Service Levels
The relationship between inventory investment and service level is non-linear. As service level targets approach 100%, the required safety stock rises exponentially [cite: 8, 9]. When forecast error autocorrelation is introduced, this curve shifts:
*   **Under Positive Autocorrelation:** The curve shifts upward. To achieve the *same* 98% service level, a firm must hold significantly more inventory than the IID model suggests. If the firm sticks to the IID-calculated budget, the service level plummets [cite: 1, 2].
*   **Under Negative Autocorrelation:** The curve may shift downward. The oscillatory nature of errors provides a natural dampening effect, allowing for higher service levels with lower inventory investments compared to the IID baseline [cite: 2].

### 2.2 Cost Implications of Estimation Errors
The financial implications of ignoring autocorrelation are twofold:
1.  **Stockout Costs (Under-stocking):** In positively correlated scenarios, the traditional formula underestimates the variance of lead time demand. This leads to frequent stockouts, lost revenue, and expedited shipping costs to recover. The "cost" side of the trade-off is artificially suppressed in planning, but explodes in execution [cite: 1, 10].
2.  **Holding Costs (Over-stocking):** In negatively correlated scenarios, or when managers arbitrarily inflate safety stocks to compensate for perceived instability without statistical basis, firms incur unnecessary holding costs. Capital is tied up in stock that is statistically unlikely to be needed due to the self-correcting nature of the demand signal [cite: 3, 11].

## 3. Strategies for Optimization

Optimizing the trade-off requires moving from heuristic adjustments to statistical corrections and dynamic policies.

### 3.1 Corrected Variance Expressions
To optimize the trade-off, the safety stock calculation must use the *conditional* variance of lead time demand, not the marginal variance. Prak and Teunter derive correction factors for inventory systems where demand is forecasted using methods like Simple Moving Average (SMA) or Single Exponential Smoothing (SES) [cite: 1].

For a lead time $L$, the variance of the forecast error over the lead time is not simply the sum of single-period variances. It must include the covariance terms between errors in different periods of the lead time.
*   **Strategy:** Implement corrected variance formulas that include a scalar multiplier based on the autocorrelation coefficient ($\rho$) and the forecasting parameter (e.g., the smoothing constant $\alpha$).
*   **Outcome:** This ensures the calculated safety stock actually delivers the targeted service level. While this often increases the required stock (in positive correlation cases), it "optimizes" the trade-off by eliminating unplanned stockout costs that far exceed the cost of the additional inventory [cite: 1].

### 3.2 Endogenous Lead Time Management
A sophisticated optimization strategy recognizes that lead times are endogenous—they depend on the workload placed on the supplier.
*   **The Mechanism:** Autocorrelated demand creates autocorrelated order streams. A retailer facing positively correlated demand will place a sequence of large orders, potentially congesting the supplier's queue and extending lead times. This creates a vicious cycle: higher demand variance $\rightarrow$ variable orders $\rightarrow$ longer/variable lead times $\rightarrow$ higher safety stock needs [cite: 2, 4].
*   **Optimization:**
    *   **For Negative Autocorrelation:** The erratic order pattern naturally smooths out utilization at the supplier, improving lead time performance. Firms can aggressively reduce safety stocks in these scenarios [cite: 2, 3].
    *   **For Positive Autocorrelation:** The firm must recognize that the "cost" of service includes the impact on the supplier. Optimization may involve smoothing the *ordering* policy (even if demand is not smooth) to stabilize lead times, rather than simply raising safety stock to cover the chaos [cite: 2, 12].

### 3.3 Forecasting Model Selection: ARIMA vs. Exponential Smoothing
The choice of forecasting model is a primary lever in optimizing the inventory trade-off.
*   **Exponential Smoothing (SES/Holt-Winters):** These models are robust and widely used but often fail to eliminate autocorrelation from the residuals. If SES is used, the safety stock formula *must* be adjusted for the induced autocorrelation in errors [cite: 1, 13].
*   **ARIMA (Auto-Regressive Integrated Moving Average):** ARIMA models are explicitly designed to model autocorrelation. By capturing the serial dependence within the forecast itself (the "AR" and "MA" terms), ARIMA can theoretically produce "whitened" residuals (errors that are IID) [cite: 13].
*   **Optimization Strategy:** If a firm has the computational capability, switching to ARIMA for highly autocorrelated SKUs can reduce the *unexplained* variance (error) that necessitates safety stock. By moving variance from the "error" bucket to the "forecast" bucket, the safety stock requirement decreases, directly improving the service-cost ratio [cite: 14, 15].

## 4. Dynamic vs. Static Safety Stock Policies

Optimization is rarely achieved through "set and forget" parameters.

### 4.1 Limitations of Static Policies
Static safety stock (e.g., "keep 100 units" or "2 weeks of supply") fails to account for the changing magnitude of forecast errors. In periods where demand becomes more predictable (lower error variance), static policies hold too much stock (high cost). In volatile periods, they hold too little (low service) [cite: 16, 17].

### 4.2 Dynamic Safety Stock (DSS)
Dynamic safety stock adjusts the buffer level in each review period based on the updated estimate of forecast error variance.
*   **Mechanism:** $SS_t = Z \times \sigma_{t, L}$. As the forecast updates, the expected error distribution ($\sigma$) is recalculated.
*   **Handling Autocorrelation:** In a dynamic system, if recent errors show a trend (autocorrelation), the system updates the variance estimate upward, immediately increasing protection. This responsiveness ensures that the service level target is maintained during volatile periods and inventory is shed during stable periods [cite: 5, 18].
*   **Service-Cost Impact:** DSS optimizes the trade-off by aligning inventory investment temporally with risk. Capital is only deployed when the risk of stockout (driven by high variance/autocorrelation) is high [cite: 6, 19].

## 5. Managerial Implications and Implementation

### 5.1 Data Quality and Granularity
Optimizing for autocorrelation requires high-quality historical data. Outliers must be managed carefully; treating a one-off event as part of an autocorrelated pattern will inflate safety stocks unnecessarily. Conversely, filtering out genuine autocorrelation as "noise" will expose the firm to risk [cite: 20, 21].

### 5.2 The Role of Service Level Targets
Firms often set arbitrary service levels (e.g., 95% across the board). Optimization under autocorrelation suggests a segmented approach:
*   **High Margin/Critical Items:** The cost of stockouts is high. Even with positive autocorrelation increasing the cost of inventory, the optimal strategy is to buffer fully using corrected formulas [cite: 6, 20].
*   **Low Margin/Replaceable Items:** If positive autocorrelation makes the required safety stock prohibitively expensive, the optimal trade-off may be to lower the target service level rather than investing in the massive inventory required to guarantee availability [cite: 20, 22].

### 5.3 Software Limitations
Most standard ERPs do not natively handle forecast error autocorrelation or endogenous lead times [cite: 7]. Implementing these strategies often requires:
*   **Overlay Solutions:** Using specialized inventory optimization software (e.g., Netstock, Slim4, Lokad) that utilizes advanced statistical methods [cite: 23].
*   **Custom Scripting:** Implementing the Prak/Teunter correction factors or ARIMA models via Python/R scripts that feed into the ERP's safety stock fields [cite: 19, 24].

## 6. Conclusion

Safety stock strategies optimize the service-cost trade-off given forecast error autocorrelation by acknowledging that **risk is not static nor independent**. Standard IID-based formulas systematically misprice risk, leading to suboptimal outcomes—either excessive holding costs or unacceptable service failures.

To optimize this trade-off, supply chain practitioners must:
1.  **Diagnose:** Test forecast errors for autocorrelation.
2.  **Correct:** Apply variance inflation factors to safety stock formulas when positive autocorrelation is present [cite: 1].
3.  **Leverage:** Recognize the natural smoothing effect of negative autocorrelation to reduce inventory where appropriate [cite: 2].
4.  **Adapt:** Shift from static policies to dynamic, variance-sensitive buffering strategies [cite: 5, 6].

By aligning the mathematical model of safety stock with the statistical reality of demand patterns, firms can achieve the efficient frontier where every dollar of inventory investment delivers the maximum possible protection against stockouts.

**Sources:**
1. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMTx2b7NhORGqa8pW2ElJas_O2iHlb-dE-IU86Qn5XhlarJb2z1yMZtlQwInCcDCrV8iGVe5emmPhSgyP3yvAgmkQm1NoU8ZgbbeRV4WvWuycu0a5pTjPwLmvzeWunurAUGUWhZHl7ZEBBOw-dxduxA1qYnxsxYFZDIGS0VWyKdDUPkDnGlpW2FQlxH13QKESZdLA5njRBbAkea-8Gx1_0uDEFytSL)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7yIGjLYV_FIL8TUTw2darYIuwGEw7QUTFHdGyHyt6tSrDpQo6YJ-s3iM5JJ8gDJnB4hS7nck-eACmrS6L9ScoeVV6dwvkahmvv5qgC0B3-5EOTFD4KYcKs6uYm78qcMT5JYwUQhIX4M0OJr-4i-30TYKhdaBuCaoEZq8Z_7-pIuVnLwYxpwMXNMIhfdi5N3w3Oeco8_phMABdNQY3LWNWNYYB5SPxZRG41WQHBYo=)
3. [uantwerpen.be](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFlZRuPl7p3xHlHrxnNTHxGjEl4JG4RveVxfLpytX-BtEC9Q42-cAbLiaksmDcUYax3JGfqdEs-oSlZTJZKuJbA5rcJ95HOAsYtkjI8yqJ7VwiOL84fGWtXawO25fUQCpS8F6IGrU2lPGljJ-KTPfwf3a9pDYzKxZSbQ==)
4. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTXBKlZxsnEHR-TlJ9lrHGzIRfqpbSSaO8WEqOk0UZSdnPExoeMDpr696BzDfXlKYYrFqSK2zZbFXuQIrXbBFWdPOIFvzyvMfDcbaFdRxvCxS14eyyXKvUEpXfLYgfnF-dXJtn4dc5DtLNit2Uy0DUjQ==)
5. [gainsystems.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcqPAbMNhS_Uf41yNcLhfn9fV426MmT1vnHsqJwQsQTNC571qMx0CxOajBlNwX_eEtdZbkmywN5ac9WR6GyOFGet0MD4ThsaH0W01uMVJXZ-0zda3MZXz16ujiFb6RVMg29QSvY8JRl0Jn1gcz3VS2oDBG4UHt6_5qRGM3levFHHt3Rykx4DltuI6ORC-J5Cne28q9_rT0mmjQ2gXoHN44KVJ2-w==)
6. [Link](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEugbPiZ3amy5TjxoIgnmjLPyKB70KzV09PO4OJu8ffDDLud5nx9B1elX0tyWGXjn96CHCSwd_Yg-qhZDO0ZtW_G64yDgS4_6WK7C09_HgOvwdXy0aLJ7PqCZRLC71WixTFcZE2BG3T74LCKm01HnnA2vgPN50Ma5N4_XZ5u7HvKvnFmZPg8wU1dQDrJSNS9PtbOw==)
7. [lokad.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHAzjgv9iriyHxjz3Pjzvsr0o5tux6xzeOU2vjyu5AJ-pJS9WCda_T8gBeGTK_57r53h-0OgUdRHGhDWaQ2VMK6uq9BoGtsM1shBNYGYbZ4ZC_H-oUPhI_uk10v-6-okIVZeUbnroSQyUdBdnmRrQm3QuHVfO2gBpk9ns=)
8. [argosoftware.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFm02HE1amVusyX2hiT4JPN1IEoA7QKFanQV3q1_h7g0aDH1FToAQqCNAlemu8MPlKoonJjJkIOGFqhpVQ-c83Paz8AohF0kHOsgKD-kcLEfwIZx4cFJax-iZ4syh-APEALiWoyzA==)
9. [mit.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH72etbR2eGrSiUoefLUcSzI7LXmIo8Eu16Q00ZO2ACN6HHAMK2vhVoQ32qH8Ydp54Ppp4iBehMSET6MwA3aaATUp3fTEJH0J91LrkxpZ4RrYgEiQLpMr2Hd_X-Yxh8ssPp2k3AEo1A8JxJhdKzz7z4y2aTn3o80Q==)
10. [opexsociety.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHq-WlnQSCIw8eT2oFSZx9kz0eIThtgKTToK2LkijTrN2fe6mUJLJx7VIANb1-ka1zI3xw5KgdGWmCmUaiLpkpy1FJmJnqdfbFDXcXiczjtkAQxtGIj7-lb_5AFmqsV44Jzd71XhbO6HEVy7jdp4a86esb8YnksVddqMX_XrxC2w74CmC-a)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3O5mA4UXbJSZru-V4Ivwrqwn4dUL4cInOKVVFY_0w9kBp9n1etJbIMExm_scGqcZhDc2exgPkznXp342K0AT0p1tbRIIYAX1xQyE6oUoRCjznlioY3jzhu3z1JJsUdIS8vFUMxgJ85QpPmf4wEPxq4o2_CrKBqpj5tFuso3dMCpFbi1Pu3cc232Sqm672YHm9eviTl6iyxBmZmMsTm--X9DRUBJhF1FvtxUguQCadeFag-IBII5rLCA==)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdwDwdruBS2tUOxrn0t0aIQy-l5wF_DVo7bqF_2vII1eV7yr-fR00gqwWYGigFdIUkOLKp3BEQJ86tCByYS2qbIh6F68pfXMvNHoBuZDGH0Mm5WcWie1G-fbmv9KFNcr3azxSotDBfvYyRw_klN24cPDhwcasUU0mv9P-1LsaXdI17M-UiBa0T9WORivOFmtwbtHYKKuHThwc9Rxg2NC1H8jdLcIB6gok9i8_qJAVzbxbr5g==)
13. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOyKg7wY0DFGSsCqE6VytkdUdC3VLwiN0QS12CWimcTzttEJHkYO36a616OmU8pPCwqOaRuLUbVMBVAkYfUcP7n-X8zT34GrYkQ6ZuOI1baxm4lM4v3-5fy-1IoiRZ6UU3dWKqbTlP579i4iZaO0qlEP_HOqQKSFSLx6X2yboMo6xr03RKhQwDRBzHkZO_R0vjssU6ambf2Gse5pqvb7igZlDSwIFQDPs7kyQCCuh-ZsAW2iKZODV5zbrCdBS7kzX-yjE=)
14. [bircu-journal.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrO9PdzeUnNILVQPtw_EuHwoS08zwh0cLtJhlBPlCbiaHdeXNSukbddaiw2x78TElFXnVjSeZnwdsy1tvioDVg6dzqRPXDhjJU7lPH5YtAA3YTiaFmR1EaVUxdW4n8yk-PBHXV3kL_RFywvsi_rkI1voeLzyWOESpKxE1pjA==)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfbiiqBS1Q0VJoJFEziZGrOsBRkTjfTGzcUCaORwdy3k8-BxDQMmiw7OUedpr6ps2oUS8BzbL08sgTOZfMTYnetOsYiEb8WGZ5Dnkrz3PvHxPbx3y2MZ2Q5sgYQ62iC1x5oB7USCz-728smq26d-RdklHLPJ4r1JwMbjPVbqWrVeW95-1IQ-XsaTJOhtviwCBiDlPwlVp0eKKWt7yuB0sujUkgjK1Qlvf9uYh7n80Zo5Ej0dRYxhEKuqq1-A==)
16. [sap.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHno-xAo4vc8qviJxdS8f9zVxFW22DwzCBKJDAmuuLMissUzp0l0PYIN2jAPq5tvZnIytlD_G8B9f60UR6tjSjVt7AXKm3sGeXQL65hTIW8b7omL9iwjqkCnkOYbzoIdpAAQRymOOZ9lElhY0fiY4YiBfgq1RkfBjt3aJooJw19EyRv7VrvHLxByeTsOm-BHn37EIT8A7KNMbL5wdCAk3PS)
17. [teamideagroup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfniT_NxDVQQp2x2-UASEMwmSAJOxrTmEUgnQlCw2EqZDj-x_mg-taBS_azAYpd6pJcxeMXC0cp_5ejsokXMlB8QyVWT1aAAvKMtkmBF8iZEgZgUM3X9Z7EbTSCPgWQhpTE5ocSRP-LqmiImKZGLEDeHnk8opVuQejTPK7u5-lT7MO2wOC5CA_X6lWZi7Z3S70bGnvAucnjHhE64BLV5Dq0UU0pr3RTbRh79SKepNgNdieshwjiIQ=)
18. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMGp6zcxx-WxogX2KA9-MlGTRAUXHU3vp7xv9b4qB_i1lh7k40vrLQsEDo5kVHFtWRf5EY8Wh7zCp87jr3om5ONAaGzcfUpQfrfgyJH4ORjJKpIToXteu6c31Yo0ZoSSsImjKo4q1c3hIf3_ROoC5GDySJ_IR1FznJ2BeMKaKtoeH6f2pq6jNgLgbC_qCRAFGKXeCQbK_GiQ==)
19. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHw1FrLtpZUZceG8CcZDhzejGDYRawj-XnST8wZTDX5qwNjwDMgkuvA2Pqi8hdhO92VhxjJzQNUSoXZuv8A6Fv4jvsHMfhzZLXu4lFDqL85xu2Q5-TZtxgDfclfyMPP9TXx)
20. [linnworks.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnv5rZ6IfHwAQmY8jDsdQDvHprmyjF0D9XNbey6xE0nVpMw5YyEMIOc16f3eSeolXyz90NET9zoojoVH20moAe0I__xS3RotCFHhhGmjKejhsf2Z-1Ye_ciEhjUEtxV6T7KxuPGoqxEFOn)
21. [eazystock.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvEQ18TDJIBkrhcuS-JvdYDn6vAANNA2lUdICqZ0Yd_Mb1MzOVV-LjqcBqXqlihQokDPPjnD-STfo1IpCCcbbNsTLU0ZsFKFOPDI5tFwFGPaX_ykm8rudUtnSfpVosU4hsy2uynMoLOayz7XZC6NPHS-cWmnryIyiamA==)
22. [owox.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTClO7J7B2bKocjFR7hqWI7Cn9Nq1ye3get1oWFgDsHR6pvZDsAbmpU4YWOiFAfSwHUb3K6v9e0GlWc-CkC2fb55pIzo5C9ORp9ib3VT-BjTZA-v5sCgO45ohOU4jMaUL0vGQRPSvn86pT8eD1W5RrQJBDDxgs3YI4bQ==)
23. [netstock.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGymVWPzX9JFXMmHXQVAGz7FMZ3uuTLY5iWOgE46a6RurawdzDHoDkxAH827HVQzP24wf8P3pXh_HDJS3bFWLY8bYuAI3nuRCOwzyQTL_vjHVs2r0tKdr3RT9uTQK5cchK9xmpIjk0l69K5PYUz7sPuFFikGVTWxP0IzdlmE3udnfwC)
24. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlX2QD5g5U6M_E5O5rzeeJRnvp-zwiOMlkEEgZ6XjRn99vf0tpRajQLgnnC4i71xGCm9hbH4D7u7nX1jucPPRhuMrbR6dQJv5Mz49DGel4Q8pmDG2dAiZFCLmeM7k=)


## Annotations
Annotation(end_index=464, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMTx2b7NhORGqa8pW2ElJas_O2iHlb-dE-IU86Qn5XhlarJb2z1yMZtlQwInCcDCrV8iGVe5emmPhSgyP3yvAgmkQm1NoU8ZgbbeRV4WvWuycu0a5pTjPwLmvzeWunurAUGUWhZHl7ZEBBOw-dxduxA1qYnxsxYFZDIGS0VWyKdDUPkDnGlpW2FQlxH13QKESZdLA5njRBbAkea-8Gx1_0uDEFytSL', start_index=455)
Annotation(end_index=793, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7yIGjLYV_FIL8TUTw2darYIuwGEw7QUTFHdGyHyt6tSrDpQo6YJ-s3iM5JJ8gDJnB4hS7nck-eACmrS6L9ScoeVV6dwvkahmvv5qgC0B3-5EOTFD4KYcKs6uYm78qcMT5JYwUQhIX4M0OJr-4i-30TYKhdaBuCaoEZq8Z_7-pIuVnLwYxpwMXNMIhfdi5N3w3Oeco8_phMABdNQY3LWNWNYYB5SPxZRG41WQHBYo=', start_index=781)
Annotation(end_index=793, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFlZRuPl7p3xHlHrxnNTHxGjEl4JG4RveVxfLpytX-BtEC9Q42-cAbLiaksmDcUYax3JGfqdEs-oSlZTJZKuJbA5rcJ95HOAsYtkjI8yqJ7VwiOL84fGWtXawO25fUQCpS8F6IGrU2lPGljJ-KTPfwf3a9pDYzKxZSbQ==', start_index=781)
Annotation(end_index=1112, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7yIGjLYV_FIL8TUTw2darYIuwGEw7QUTFHdGyHyt6tSrDpQo6YJ-s3iM5JJ8gDJnB4hS7nck-eACmrS6L9ScoeVV6dwvkahmvv5qgC0B3-5EOTFD4KYcKs6uYm78qcMT5JYwUQhIX4M0OJr-4i-30TYKhdaBuCaoEZq8Z_7-pIuVnLwYxpwMXNMIhfdi5N3w3Oeco8_phMABdNQY3LWNWNYYB5SPxZRG41WQHBYo=', start_index=1103)
Annotation(end_index=1358, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTXBKlZxsnEHR-TlJ9lrHGzIRfqpbSSaO8WEqOk0UZSdnPExoeMDpr696BzDfXlKYYrFqSK2zZbFXuQIrXbBFWdPOIFvzyvMfDcbaFdRxvCxS14eyyXKvUEpXfLYgfnF-dXJtn4dc5DtLNit2Uy0DUjQ==', start_index=1346)
Annotation(end_index=1358, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFlZRuPl7p3xHlHrxnNTHxGjEl4JG4RveVxfLpytX-BtEC9Q42-cAbLiaksmDcUYax3JGfqdEs-oSlZTJZKuJbA5rcJ95HOAsYtkjI8yqJ7VwiOL84fGWtXawO25fUQCpS8F6IGrU2lPGljJ-KTPfwf3a9pDYzKxZSbQ==', start_index=1346)
Annotation(end_index=1698, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEugbPiZ3amy5TjxoIgnmjLPyKB70KzV09PO4OJu8ffDDLud5nx9B1elX0tyWGXjn96CHCSwd_Yg-qhZDO0ZtW_G64yDgS4_6WK7C09_HgOvwdXy0aLJ7PqCZRLC71WixTFcZE2BG3T74LCKm01HnnA2vgPN50Ma5N4_XZ5u7HvKvnFmZPg8wU1dQDrJSNS9PtbOw==', start_index=1683)
Annotation(end_index=1698, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMTx2b7NhORGqa8pW2ElJas_O2iHlb-dE-IU86Qn5XhlarJb2z1yMZtlQwInCcDCrV8iGVe5emmPhSgyP3yvAgmkQm1NoU8ZgbbeRV4WvWuycu0a5pTjPwLmvzeWunurAUGUWhZHl7ZEBBOw-dxduxA1qYnxsxYFZDIGS0VWyKdDUPkDnGlpW2FQlxH13QKESZdLA5njRBbAkea-8Gx1_0uDEFytSL', start_index=1683)
Annotation(end_index=1698, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcqPAbMNhS_Uf41yNcLhfn9fV426MmT1vnHsqJwQsQTNC571qMx0CxOajBlNwX_eEtdZbkmywN5ac9WR6GyOFGet0MD4ThsaH0W01uMVJXZ-0zda3MZXz16ujiFb6RVMg29QSvY8JRl0Jn1gcz3VS2oDBG4UHt6_5qRGM3levFHHt3Rykx4DltuI6ORC-J5Cne28q9_rT0mmjQ2gXoHN44KVJ2-w==', start_index=1683)
Annotation(end_index=3345, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEugbPiZ3amy5TjxoIgnmjLPyKB70KzV09PO4OJu8ffDDLud5nx9B1elX0tyWGXjn96CHCSwd_Yg-qhZDO0ZtW_G64yDgS4_6WK7C09_HgOvwdXy0aLJ7PqCZRLC71WixTFcZE2BG3T74LCKm01HnnA2vgPN50Ma5N4_XZ5u7HvKvnFmZPg8wU1dQDrJSNS9PtbOw==', start_index=3333)
Annotation(end_index=3345, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHAzjgv9iriyHxjz3Pjzvsr0o5tux6xzeOU2vjyu5AJ-pJS9WCda_T8gBeGTK_57r53h-0OgUdRHGhDWaQ2VMK6uq9BoGtsM1shBNYGYbZ4ZC_H-oUPhI_uk10v-6-okIVZeUbnroSQyUdBdnmRrQm3QuHVfO2gBpk9ns=', start_index=3333)
Annotation(end_index=3910, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7yIGjLYV_FIL8TUTw2darYIuwGEw7QUTFHdGyHyt6tSrDpQo6YJ-s3iM5JJ8gDJnB4hS7nck-eACmrS6L9ScoeVV6dwvkahmvv5qgC0B3-5EOTFD4KYcKs6uYm78qcMT5JYwUQhIX4M0OJr-4i-30TYKhdaBuCaoEZq8Z_7-pIuVnLwYxpwMXNMIhfdi5N3w3Oeco8_phMABdNQY3LWNWNYYB5SPxZRG41WQHBYo=', start_index=3901)
Annotation(end_index=4227, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7yIGjLYV_FIL8TUTw2darYIuwGEw7QUTFHdGyHyt6tSrDpQo6YJ-s3iM5JJ8gDJnB4hS7nck-eACmrS6L9ScoeVV6dwvkahmvv5qgC0B3-5EOTFD4KYcKs6uYm78qcMT5JYwUQhIX4M0OJr-4i-30TYKhdaBuCaoEZq8Z_7-pIuVnLwYxpwMXNMIhfdi5N3w3Oeco8_phMABdNQY3LWNWNYYB5SPxZRG41WQHBYo=', start_index=4215)
Annotation(end_index=4227, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFlZRuPl7p3xHlHrxnNTHxGjEl4JG4RveVxfLpytX-BtEC9Q42-cAbLiaksmDcUYax3JGfqdEs-oSlZTJZKuJbA5rcJ95HOAsYtkjI8yqJ7VwiOL84fGWtXawO25fUQCpS8F6IGrU2lPGljJ-KTPfwf3a9pDYzKxZSbQ==', start_index=4215)
Annotation(end_index=4841, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMTx2b7NhORGqa8pW2ElJas_O2iHlb-dE-IU86Qn5XhlarJb2z1yMZtlQwInCcDCrV8iGVe5emmPhSgyP3yvAgmkQm1NoU8ZgbbeRV4WvWuycu0a5pTjPwLmvzeWunurAUGUWhZHl7ZEBBOw-dxduxA1qYnxsxYFZDIGS0VWyKdDUPkDnGlpW2FQlxH13QKESZdLA5njRBbAkea-8Gx1_0uDEFytSL', start_index=4832)
Annotation(end_index=5617, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFm02HE1amVusyX2hiT4JPN1IEoA7QKFanQV3q1_h7g0aDH1FToAQqCNAlemu8MPlKoonJjJkIOGFqhpVQ-c83Paz8AohF0kHOsgKD-kcLEfwIZx4cFJax-iZ4syh-APEALiWoyzA==', start_index=5605)
Annotation(end_index=5617, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH72etbR2eGrSiUoefLUcSzI7LXmIo8Eu16Q00ZO2ACN6HHAMK2vhVoQ32qH8Ydp54Ppp4iBehMSET6MwA3aaATUp3fTEJH0J91LrkxpZ4RrYgEiQLpMr2Hd_X-Yxh8ssPp2k3AEo1A8JxJhdKzz7z4y2aTn3o80Q==', start_index=5605)
Annotation(end_index=5958, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMTx2b7NhORGqa8pW2ElJas_O2iHlb-dE-IU86Qn5XhlarJb2z1yMZtlQwInCcDCrV8iGVe5emmPhSgyP3yvAgmkQm1NoU8ZgbbeRV4WvWuycu0a5pTjPwLmvzeWunurAUGUWhZHl7ZEBBOw-dxduxA1qYnxsxYFZDIGS0VWyKdDUPkDnGlpW2FQlxH13QKESZdLA5njRBbAkea-8Gx1_0uDEFytSL', start_index=5946)
Annotation(end_index=5958, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7yIGjLYV_FIL8TUTw2darYIuwGEw7QUTFHdGyHyt6tSrDpQo6YJ-s3iM5JJ8gDJnB4hS7nck-eACmrS6L9ScoeVV6dwvkahmvv5qgC0B3-5EOTFD4KYcKs6uYm78qcMT5JYwUQhIX4M0OJr-4i-30TYKhdaBuCaoEZq8Z_7-pIuVnLwYxpwMXNMIhfdi5N3w3Oeco8_phMABdNQY3LWNWNYYB5SPxZRG41WQHBYo=', start_index=5946)
Annotation(end_index=6206, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7yIGjLYV_FIL8TUTw2darYIuwGEw7QUTFHdGyHyt6tSrDpQo6YJ-s3iM5JJ8gDJnB4hS7nck-eACmrS6L9ScoeVV6dwvkahmvv5qgC0B3-5EOTFD4KYcKs6uYm78qcMT5JYwUQhIX4M0OJr-4i-30TYKhdaBuCaoEZq8Z_7-pIuVnLwYxpwMXNMIhfdi5N3w3Oeco8_phMABdNQY3LWNWNYYB5SPxZRG41WQHBYo=', start_index=6197)
Annotation(end_index=6675, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMTx2b7NhORGqa8pW2ElJas_O2iHlb-dE-IU86Qn5XhlarJb2z1yMZtlQwInCcDCrV8iGVe5emmPhSgyP3yvAgmkQm1NoU8ZgbbeRV4WvWuycu0a5pTjPwLmvzeWunurAUGUWhZHl7ZEBBOw-dxduxA1qYnxsxYFZDIGS0VWyKdDUPkDnGlpW2FQlxH13QKESZdLA5njRBbAkea-8Gx1_0uDEFytSL', start_index=6662)
Annotation(end_index=6675, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHq-WlnQSCIw8eT2oFSZx9kz0eIThtgKTToK2LkijTrN2fe6mUJLJx7VIANb1-ka1zI3xw5KgdGWmCmUaiLpkpy1FJmJnqdfbFDXcXiczjtkAQxtGIj7-lb_5AFmqsV44Jzd71XhbO6HEVy7jdp4a86esb8YnksVddqMX_XrxC2w74CmC-a', start_index=6662)
Annotation(end_index=7049, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3O5mA4UXbJSZru-V4Ivwrqwn4dUL4cInOKVVFY_0w9kBp9n1etJbIMExm_scGqcZhDc2exgPkznXp342K0AT0p1tbRIIYAX1xQyE6oUoRCjznlioY3jzhu3z1JJsUdIS8vFUMxgJ85QpPmf4wEPxq4o2_CrKBqpj5tFuso3dMCpFbi1Pu3cc232Sqm672YHm9eviTl6iyxBmZmMsTm--X9DRUBJhF1FvtxUguQCadeFag-IBII5rLCA==', start_index=7036)
Annotation(end_index=7049, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFlZRuPl7p3xHlHrxnNTHxGjEl4JG4RveVxfLpytX-BtEC9Q42-cAbLiaksmDcUYax3JGfqdEs-oSlZTJZKuJbA5rcJ95HOAsYtkjI8yqJ7VwiOL84fGWtXawO25fUQCpS8F6IGrU2lPGljJ-KTPfwf3a9pDYzKxZSbQ==', start_index=7036)
Annotation(end_index=7570, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMTx2b7NhORGqa8pW2ElJas_O2iHlb-dE-IU86Qn5XhlarJb2z1yMZtlQwInCcDCrV8iGVe5emmPhSgyP3yvAgmkQm1NoU8ZgbbeRV4WvWuycu0a5pTjPwLmvzeWunurAUGUWhZHl7ZEBBOw-dxduxA1qYnxsxYFZDIGS0VWyKdDUPkDnGlpW2FQlxH13QKESZdLA5njRBbAkea-8Gx1_0uDEFytSL', start_index=7561)
Annotation(end_index=8313, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMTx2b7NhORGqa8pW2ElJas_O2iHlb-dE-IU86Qn5XhlarJb2z1yMZtlQwInCcDCrV8iGVe5emmPhSgyP3yvAgmkQm1NoU8ZgbbeRV4WvWuycu0a5pTjPwLmvzeWunurAUGUWhZHl7ZEBBOw-dxduxA1qYnxsxYFZDIGS0VWyKdDUPkDnGlpW2FQlxH13QKESZdLA5njRBbAkea-8Gx1_0uDEFytSL', start_index=8304)
Annotation(end_index=8905, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTXBKlZxsnEHR-TlJ9lrHGzIRfqpbSSaO8WEqOk0UZSdnPExoeMDpr696BzDfXlKYYrFqSK2zZbFXuQIrXbBFWdPOIFvzyvMfDcbaFdRxvCxS14eyyXKvUEpXfLYgfnF-dXJtn4dc5DtLNit2Uy0DUjQ==', start_index=8893)
Annotation(end_index=8905, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7yIGjLYV_FIL8TUTw2darYIuwGEw7QUTFHdGyHyt6tSrDpQo6YJ-s3iM5JJ8gDJnB4hS7nck-eACmrS6L9ScoeVV6dwvkahmvv5qgC0B3-5EOTFD4KYcKs6uYm78qcMT5JYwUQhIX4M0OJr-4i-30TYKhdaBuCaoEZq8Z_7-pIuVnLwYxpwMXNMIhfdi5N3w3Oeco8_phMABdNQY3LWNWNYYB5SPxZRG41WQHBYo=', start_index=8893)
Annotation(end_index=9156, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7yIGjLYV_FIL8TUTw2darYIuwGEw7QUTFHdGyHyt6tSrDpQo6YJ-s3iM5JJ8gDJnB4hS7nck-eACmrS6L9ScoeVV6dwvkahmvv5qgC0B3-5EOTFD4KYcKs6uYm78qcMT5JYwUQhIX4M0OJr-4i-30TYKhdaBuCaoEZq8Z_7-pIuVnLwYxpwMXNMIhfdi5N3w3Oeco8_phMABdNQY3LWNWNYYB5SPxZRG41WQHBYo=', start_index=9144)
Annotation(end_index=9156, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFlZRuPl7p3xHlHrxnNTHxGjEl4JG4RveVxfLpytX-BtEC9Q42-cAbLiaksmDcUYax3JGfqdEs-oSlZTJZKuJbA5rcJ95HOAsYtkjI8yqJ7VwiOL84fGWtXawO25fUQCpS8F6IGrU2lPGljJ-KTPfwf3a9pDYzKxZSbQ==', start_index=9144)
Annotation(end_index=9473, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7yIGjLYV_FIL8TUTw2darYIuwGEw7QUTFHdGyHyt6tSrDpQo6YJ-s3iM5JJ8gDJnB4hS7nck-eACmrS6L9ScoeVV6dwvkahmvv5qgC0B3-5EOTFD4KYcKs6uYm78qcMT5JYwUQhIX4M0OJr-4i-30TYKhdaBuCaoEZq8Z_7-pIuVnLwYxpwMXNMIhfdi5N3w3Oeco8_phMABdNQY3LWNWNYYB5SPxZRG41WQHBYo=', start_index=9460)
Annotation(end_index=9473, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdwDwdruBS2tUOxrn0t0aIQy-l5wF_DVo7bqF_2vII1eV7yr-fR00gqwWYGigFdIUkOLKp3BEQJ86tCByYS2qbIh6F68pfXMvNHoBuZDGH0Mm5WcWie1G-fbmv9KFNcr3azxSotDBfvYyRw_klN24cPDhwcasUU0mv9P-1LsaXdI17M-UiBa0T9WORivOFmtwbtHYKKuHThwc9Rxg2NC1H8jdLcIB6gok9i8_qJAVzbxbr5g==', start_index=9460)
Annotation(end_index=9904, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMTx2b7NhORGqa8pW2ElJas_O2iHlb-dE-IU86Qn5XhlarJb2z1yMZtlQwInCcDCrV8iGVe5emmPhSgyP3yvAgmkQm1NoU8ZgbbeRV4WvWuycu0a5pTjPwLmvzeWunurAUGUWhZHl7ZEBBOw-dxduxA1qYnxsxYFZDIGS0VWyKdDUPkDnGlpW2FQlxH13QKESZdLA5njRBbAkea-8Gx1_0uDEFytSL', start_index=9891)
Annotation(end_index=9904, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOyKg7wY0DFGSsCqE6VytkdUdC3VLwiN0QS12CWimcTzttEJHkYO36a616OmU8pPCwqOaRuLUbVMBVAkYfUcP7n-X8zT34GrYkQ6ZuOI1baxm4lM4v3-5fy-1IoiRZ6UU3dWKqbTlP579i4iZaO0qlEP_HOqQKSFSLx6X2yboMo6xr03RKhQwDRBzHkZO_R0vjssU6ambf2Gse5pqvb7igZlDSwIFQDPs7kyQCCuh-ZsAW2iKZODV5zbrCdBS7kzX-yjE=', start_index=9891)
Annotation(end_index=10202, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOyKg7wY0DFGSsCqE6VytkdUdC3VLwiN0QS12CWimcTzttEJHkYO36a616OmU8pPCwqOaRuLUbVMBVAkYfUcP7n-X8zT34GrYkQ6ZuOI1baxm4lM4v3-5fy-1IoiRZ6UU3dWKqbTlP579i4iZaO0qlEP_HOqQKSFSLx6X2yboMo6xr03RKhQwDRBzHkZO_R0vjssU6ambf2Gse5pqvb7igZlDSwIFQDPs7kyQCCuh-ZsAW2iKZODV5zbrCdBS7kzX-yjE=', start_index=10192)
Annotation(end_index=10572, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfbiiqBS1Q0VJoJFEziZGrOsBRkTjfTGzcUCaORwdy3k8-BxDQMmiw7OUedpr6ps2oUS8BzbL08sgTOZfMTYnetOsYiEb8WGZ5Dnkrz3PvHxPbx3y2MZ2Q5sgYQ62iC1x5oB7USCz-728smq26d-RdklHLPJ4r1JwMbjPVbqWrVeW95-1IQ-XsaTJOhtviwCBiDlPwlVp0eKKWt7yuB0sujUkgjK1Qlvf9uYh7n80Zo5Ej0dRYxhEKuqq1-A==', start_index=10558)
Annotation(end_index=10572, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrO9PdzeUnNILVQPtw_EuHwoS08zwh0cLtJhlBPlCbiaHdeXNSukbddaiw2x78TElFXnVjSeZnwdsy1tvioDVg6dzqRPXDhjJU7lPH5YtAA3YTiaFmR1EaVUxdW4n8yk-PBHXV3kL_RFywvsi_rkI1voeLzyWOESpKxE1pjA==', start_index=10558)
Annotation(end_index=11056, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfniT_NxDVQQp2x2-UASEMwmSAJOxrTmEUgnQlCw2EqZDj-x_mg-taBS_azAYpd6pJcxeMXC0cp_5ejsokXMlB8QyVWT1aAAvKMtkmBF8iZEgZgUM3X9Z7EbTSCPgWQhpTE5ocSRP-LqmiImKZGLEDeHnk8opVuQejTPK7u5-lT7MO2wOC5CA_X6lWZi7Z3S70bGnvAucnjHhE64BLV5Dq0UU0pr3RTbRh79SKepNgNdieshwjiIQ=', start_index=11042)
Annotation(end_index=11056, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHno-xAo4vc8qviJxdS8f9zVxFW22DwzCBKJDAmuuLMissUzp0l0PYIN2jAPq5tvZnIytlD_G8B9f60UR6tjSjVt7AXKm3sGeXQL65hTIW8b7omL9iwjqkCnkOYbzoIdpAAQRymOOZ9lElhY0fiY4YiBfgq1RkfBjt3aJooJw19EyRv7VrvHLxByeTsOm-BHn37EIT8A7KNMbL5wdCAk3PS', start_index=11042)
Annotation(end_index=11698, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMGp6zcxx-WxogX2KA9-MlGTRAUXHU3vp7xv9b4qB_i1lh7k40vrLQsEDo5kVHFtWRf5EY8Wh7zCp87jr3om5ONAaGzcfUpQfrfgyJH4ORjJKpIToXteu6c31Yo0ZoSSsImjKo4q1c3hIf3_ROoC5GDySJ_IR1FznJ2BeMKaKtoeH6f2pq6jNgLgbC_qCRAFGKXeCQbK_GiQ==', start_index=11685)
Annotation(end_index=11698, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcqPAbMNhS_Uf41yNcLhfn9fV426MmT1vnHsqJwQsQTNC571qMx0CxOajBlNwX_eEtdZbkmywN5ac9WR6GyOFGet0MD4ThsaH0W01uMVJXZ-0zda3MZXz16ujiFb6RVMg29QSvY8JRl0Jn1gcz3VS2oDBG4UHt6_5qRGM3levFHHt3Rykx4DltuI6ORC-J5Cne28q9_rT0mmjQ2gXoHN44KVJ2-w==', start_index=11685)
Annotation(end_index=11926, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEugbPiZ3amy5TjxoIgnmjLPyKB70KzV09PO4OJu8ffDDLud5nx9B1elX0tyWGXjn96CHCSwd_Yg-qhZDO0ZtW_G64yDgS4_6WK7C09_HgOvwdXy0aLJ7PqCZRLC71WixTFcZE2BG3T74LCKm01HnnA2vgPN50Ma5N4_XZ5u7HvKvnFmZPg8wU1dQDrJSNS9PtbOw==', start_index=11913)
Annotation(end_index=11926, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHw1FrLtpZUZceG8CcZDhzejGDYRawj-XnST8wZTDX5qwNjwDMgkuvA2Pqi8hdhO92VhxjJzQNUSoXZuv8A6Fv4jvsHMfhzZLXu4lFDqL85xu2Q5-TZtxgDfclfyMPP9TXx', start_index=11913)
Annotation(end_index=12330, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnv5rZ6IfHwAQmY8jDsdQDvHprmyjF0D9XNbey6xE0nVpMw5YyEMIOc16f3eSeolXyz90NET9zoojoVH20moAe0I__xS3RotCFHhhGmjKejhsf2Z-1Ye_ciEhjUEtxV6T7KxuPGoqxEFOn', start_index=12316)
Annotation(end_index=12330, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvEQ18TDJIBkrhcuS-JvdYDn6vAANNA2lUdICqZ0Yd_Mb1MzOVV-LjqcBqXqlihQokDPPjnD-STfo1IpCCcbbNsTLU0ZsFKFOPDI5tFwFGPaX_ykm8rudUtnSfpVosU4hsy2uynMoLOayz7XZC6NPHS-cWmnryIyiamA==', start_index=12316)
Annotation(end_index=12726, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEugbPiZ3amy5TjxoIgnmjLPyKB70KzV09PO4OJu8ffDDLud5nx9B1elX0tyWGXjn96CHCSwd_Yg-qhZDO0ZtW_G64yDgS4_6WK7C09_HgOvwdXy0aLJ7PqCZRLC71WixTFcZE2BG3T74LCKm01HnnA2vgPN50Ma5N4_XZ5u7HvKvnFmZPg8wU1dQDrJSNS9PtbOw==', start_index=12713)
Annotation(end_index=12726, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnv5rZ6IfHwAQmY8jDsdQDvHprmyjF0D9XNbey6xE0nVpMw5YyEMIOc16f3eSeolXyz90NET9zoojoVH20moAe0I__xS3RotCFHhhGmjKejhsf2Z-1Ye_ciEhjUEtxV6T7KxuPGoqxEFOn', start_index=12713)
Annotation(end_index=13010, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnv5rZ6IfHwAQmY8jDsdQDvHprmyjF0D9XNbey6xE0nVpMw5YyEMIOc16f3eSeolXyz90NET9zoojoVH20moAe0I__xS3RotCFHhhGmjKejhsf2Z-1Ye_ciEhjUEtxV6T7KxuPGoqxEFOn', start_index=12996)
Annotation(end_index=13010, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTClO7J7B2bKocjFR7hqWI7Cn9Nq1ye3get1oWFgDsHR6pvZDsAbmpU4YWOiFAfSwHUb3K6v9e0GlWc-CkC2fb55pIzo5C9ORp9ib3VT-BjTZA-v5sCgO45ohOU4jMaUL0vGQRPSvn86pT8eD1W5RrQJBDDxgs3YI4bQ==', start_index=12996)
Annotation(end_index=13149, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHAzjgv9iriyHxjz3Pjzvsr0o5tux6xzeOU2vjyu5AJ-pJS9WCda_T8gBeGTK_57r53h-0OgUdRHGhDWaQ2VMK6uq9BoGtsM1shBNYGYbZ4ZC_H-oUPhI_uk10v-6-okIVZeUbnroSQyUdBdnmRrQm3QuHVfO2gBpk9ns=', start_index=13140)
Annotation(end_index=13358, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGymVWPzX9JFXMmHXQVAGz7FMZ3uuTLY5iWOgE46a6RurawdzDHoDkxAH827HVQzP24wf8P3pXh_HDJS3bFWLY8bYuAI3nuRCOwzyQTL_vjHVs2r0tKdr3RT9uTQK5cchK9xmpIjk0l69K5PYUz7sPuFFikGVTWxP0IzdlmE3udnfwC', start_index=13348)
Annotation(end_index=13531, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFlX2QD5g5U6M_E5O5rzeeJRnvp-zwiOMlkEEgZ6XjRn99vf0tpRajQLgnnC4i71xGCm9hbH4D7u7nX1jucPPRhuMrbR6dQJv5Mz49DGel4Q8pmDG2dAiZFCLmeM7k=', start_index=13517)
Annotation(end_index=13531, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHw1FrLtpZUZceG8CcZDhzejGDYRawj-XnST8wZTDX5qwNjwDMgkuvA2Pqi8hdhO92VhxjJzQNUSoXZuv8A6Fv4jvsHMfhzZLXu4lFDqL85xu2Q5-TZtxgDfclfyMPP9TXx', start_index=13517)
Annotation(end_index=14114, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMTx2b7NhORGqa8pW2ElJas_O2iHlb-dE-IU86Qn5XhlarJb2z1yMZtlQwInCcDCrV8iGVe5emmPhSgyP3yvAgmkQm1NoU8ZgbbeRV4WvWuycu0a5pTjPwLmvzeWunurAUGUWhZHl7ZEBBOw-dxduxA1qYnxsxYFZDIGS0VWyKdDUPkDnGlpW2FQlxH13QKESZdLA5njRBbAkea-8Gx1_0uDEFytSL', start_index=14105)
Annotation(end_index=14248, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7yIGjLYV_FIL8TUTw2darYIuwGEw7QUTFHdGyHyt6tSrDpQo6YJ-s3iM5JJ8gDJnB4hS7nck-eACmrS6L9ScoeVV6dwvkahmvv5qgC0B3-5EOTFD4KYcKs6uYm78qcMT5JYwUQhIX4M0OJr-4i-30TYKhdaBuCaoEZq8Z_7-pIuVnLwYxpwMXNMIhfdi5N3w3Oeco8_phMABdNQY3LWNWNYYB5SPxZRG41WQHBYo=', start_index=14239)
Annotation(end_index=14356, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEugbPiZ3amy5TjxoIgnmjLPyKB70KzV09PO4OJu8ffDDLud5nx9B1elX0tyWGXjn96CHCSwd_Yg-qhZDO0ZtW_G64yDgS4_6WK7C09_HgOvwdXy0aLJ7PqCZRLC71WixTFcZE2BG3T74LCKm01HnnA2vgPN50Ma5N4_XZ5u7HvKvnFmZPg8wU1dQDrJSNS9PtbOw==', start_index=14344)
Annotation(end_index=14356, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcqPAbMNhS_Uf41yNcLhfn9fV426MmT1vnHsqJwQsQTNC571qMx0CxOajBlNwX_eEtdZbkmywN5ac9WR6GyOFGet0MD4ThsaH0W01uMVJXZ-0zda3MZXz16ujiFb6RVMg29QSvY8JRl0Jn1gcz3VS2oDBG4UHt6_5qRGM3levFHHt3Rykx4DltuI6ORC-J5Cne28q9_rT0mmjQ2gXoHN44KVJ2-w==', start_index=14344)

## Sources
