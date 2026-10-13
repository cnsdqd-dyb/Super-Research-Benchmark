# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 5196965e | **Time:** 916.89s | **Cost:** $4.41323
--------------------------------------------------------------------------------

# Impact of Asymmetric Transport Delay Distribution on the Response Resilience of Inventory Allocation

### Key Points
*   **Asymmetry vs. Normality:** Traditional inventory models often assume normally distributed lead times. However, real-world transport delays are frequently asymmetric and right-skewed (long-tail), meaning extreme delay events occur more often than standard models predict. This discrepancy leads to severe underestimations of risk.
*   **Inventory Drift:** Asymmetric delays, particularly when misperceived by inventory control systems, cause "inventory drift." This is a phenomenon where actual inventory levels permanently diverge from target levels due to errors in the feedback loops of replenishment policies, leading to instability and stockouts.
*   **Response Resilience Trade-offs:** Research indicates a fundamental trade-off between resilience (speed of recovery) and robustness (stability under uncertainty). Inventory policies tuned for optimal response resilience under assumed constant delays may become unstable or chaotic when facing asymmetric delay distributions.
*   **Control Engineering Metrics:** The Integral of Time Absolute Error (ITAE) is a critical metric for quantifying response resilience. It measures the cumulative deviation of inventory from the target over time. Asymmetric delays significantly increase ITAE, indicating poor resilience performance.
*   **Mitigation Strategies:** Static safety stocks are often insufficient for asymmetric delays. Effective mitigation requires dynamic mechanisms, such as variable Goods in Transit (GIT) targets, postponement strategies, and advanced "digital twin" visibility to correct lead-time parameters in real-time.

---

## 1. Introduction

The resilience of global supply chains has emerged as a paramount concern for academia and industry, driven by the increasing frequency of disruptions ranging from natural disasters to geopolitical instability. A critical, yet often under-analyzed, component of this resilience is the impact of **asymmetric transport delay distributions** on inventory allocation. While classical inventory theory frequently relies on the assumption of linearity and normal distributions for lead times, empirical evidence suggests that transport delays are inherently asymmetric, often characterized by "long tails" or right-skewed distributions where the probability of extreme delays significantly exceeds that of early arrivals.

This report provides an exhaustive analysis of how these asymmetric delays influence the **response resilience** of inventory systems. Response resilience is defined not merely as the ability to survive a disruption, but as the dynamic capacity to minimize the deviation of inventory levels from their targets and recover equilibrium rapidly.

The analysis draws heavily on control engineering approaches to supply chain dynamics, specifically examining the phenomenon of **inventory drift**, the destabilizing effects of misperceived lead times, and the nonlinear behaviors that arise when allocation policies interact with stochastic, asymmetric transport networks. By synthesizing findings from recent literature, this report elucidates the mechanisms through which delay asymmetry degrades supply chain performance and explores advanced strategies for enhancing resilience in the face of such uncertainty.

---

## 2. Theoretical Framework of Supply Chain Resilience

To understand the impact of transport delays, one must first establish a rigorous definition of supply chain resilience (SCR) and the metrics used to quantify it.

### 2.1 Defining Response Resilience
Supply chain resilience is a multidimensional concept. While early definitions focused on the static ability to absorb shocks, modern frameworks emphasize a dynamic process. Research identifies three critical phases of resilience: **readiness, response, and recovery** [cite: 1, 2, 3].

*   **Readiness:** The proactive phase involving the preparation of resources, redundancy, and flexibility before a disruption occurs.
*   **Response:** The reactive phase where the system adapts to the immediate impact of the shock. This is the primary focus of this report regarding "response resilience." It involves the speed and effectiveness of the reaction to deviations in supply or demand.
*   **Recovery:** The restoration phase where the system returns to a steady state, ideally a more robust one than before [cite: 4].

**Response resilience** specifically refers to the system's ability to minimize the immediate impact of a disruption (e.g., a transport delay) and dampen the oscillation of inventory levels. It is often quantified using the **Integral of Time Absolute Error (ITAE)**, a control engineering metric that aggregates the absolute difference between the actual inventory level and the target level over time [cite: 2, 3, 5]. A lower ITAE indicates higher resilience, signifying that the system spent less time and magnitude away from its desired state.

### 2.2 The Control Engineering Perspective
The supply chain can be modeled as a complex adaptive system using control theory. In this view, inventory allocation policies (such as Order-Up-To rules) act as controllers that adjust inputs (orders) based on feedback (current inventory and work-in-process) to maintain a setpoint (target inventory) [cite: 6, 7].

Spiegler et al. (2012) and subsequent researchers have utilized this framework to mathematically model resilience. They demonstrate that resilience is determined by the dynamic behavior of stock and shipment responses, specifically the **overshoot** (excess inventory), **undershoot** (stockouts), and **settling time** (duration of instability) [cite: 3, 5, 8].

### 2.3 Inventory Allocation Mechanisms
Inventory allocation in this context refers to the decision-making rules that determine how much stock is ordered and where it is deployed. These rules typically rely on:
1.  **Demand Forecasting:** Estimating future consumption.
2.  **Lead Time Estimation:** Predicting the time delay between placing an order and receiving goods.
3.  **Feedback Loops:** Monitoring actual inventory ($AINV$) and Goods in Transit ($GIT$) or Work in Process ($WIP$) [cite: 7].

The resilience of these allocation mechanisms is heavily dependent on the accuracy of the parameters used, particularly the lead time. When the actual transport delay distribution deviates from the parameters assumed by the allocation policy—specifically through asymmetry—the system's control loops can fail, leading to performance degradation [cite: 6, 7].

---

## 3. Dynamics of Asymmetric Transport Delay Distribution

Transport delays are rarely deterministic. They are stochastic variables subject to numerous external factors, including weather, port congestion, and labor strikes.

### 3.1 The Nature of Asymmetry
In standard inventory models, lead times are often treated as constant or normally distributed for mathematical simplicity. However, empirical data shows that transport delays follow asymmetric distributions, often log-normal or Gamma distributions [cite: 9, 10].

*   **Right-Skewed (Long-Tail):** There is a hard lower bound on transport time (a truck cannot arrive instantly), but there is theoretically no upper bound on delay. This creates a "long tail" of low-probability, high-impact delay events [cite: 10, 11].
*   **Implication of Skewness:** The mean lead time may remain low, but the variance and the potential for extreme outliers are high. Standard deviation alone often fails to capture the risk profile of these "long tail" events [cite: 9].

### 3.2 Sources of Asymmetry
Asymmetry arises from the physical and operational constraints of the supply chain:
*   **Capacity Constraints:** When transport capacity is reached, delays do not increase linearly; they spike exponentially as backlogs accumulate. This creates nonlinear delay functions [cite: 12].
*   **Disruption Propagation:** A minor delay in one node (e.g., a port strike) can cascade through the network, creating amplified delays downstream, a phenomenon exacerbated by the lack of coordinated action among administrators [cite: 13].
*   **Operational Failures:** Machine failures or customs holds create discrete jumps in delay time that do not fit symmetric probability curves [cite: 11].

### 3.3 Modeling Challenges
The presence of asymmetry presents significant difficulties for modeling inventory allocation. Standard forecasting and replenishment algorithms that assume normality will underestimate the frequency of extreme delays. Research indicates that logarithmic adjustments or specific "long tail" considerations are necessary to equalize data distribution and improve reliability [cite: 9]. Failure to account for this asymmetry leads to "misperceived lead times," a core driver of instability.

---

## 4. Impact on Inventory Allocation and Stability

The interaction between asymmetric transport delays and inventory allocation policies results in specific dynamic failure modes. The most significant of these is **inventory drift**.

### 4.1 The Phenomenon of Inventory Drift
Inventory drift is a condition where the actual inventory level systematically diverges from the target level, failing to converge back to the setpoint even after the disruption has passed. This phenomenon is directly linked to the mismatch between the *actual* transport delay and the *perceived* delay used in the inventory control algorithm [cite: 6, 7].

*   **Mechanism of Drift:** Inventory policies (like APVIOBPCS - Automatic Pipeline, Variable Inventory and Order Based Production Control System) use a parameter to estimate the pipeline stock (Goods in Transit). If the transport delay distribution is asymmetric, the "expected" lead time (often the mean) may not accurately reflect the "effective" delay experienced by the system.
*   **Feedback Error:** When the lead time is misperceived (e.g., the system assumes a delay of 1 period, but the long-tail distribution results in frequent delays of 2+ periods), the feedback loop regarding Work-In-Process ($WIP$) becomes corrupted. The system believes it has sufficient inventory "on the way," but it does not arrive when expected [cite: 7].
*   **Consequence:** This leads to a permanent offset or "drift" in inventory levels. The system may perpetually under-order (leading to stockouts) or over-order (leading to bloat) because the integral error in the control loop is never fully resolved [cite: 3, 14].

### 4.2 Instability and Chaos
Beyond simple drift, asymmetric delays can push inventory allocation systems into instability. Research using eigenvalue analysis on piecewise linear models of inventory systems shows that:
*   **Bounded Fluctuations:** Outside the asymptotically stable regions, systems with asymmetric delays can enter regions of "bounded fluctuations" that continue forever. These can manifest as periodicity (oscillations) or chaos [cite: 6, 7].
*   **Nonlinear Behaviors:** The combination of asymmetric delays and nonlinear constraints (such as the "forbidden returns" constraint, where orders cannot be negative) creates complex dynamic behaviors. A system might be stable under normal delay conditions but flip into a limit cycle (permanent oscillation) when a long-tail delay event occurs [cite: 6, 15].

### 4.3 The Bullwhip Effect
Asymmetric delays exacerbate the Bullwhip Effect—the amplification of demand variability as orders move upstream.
*   **Variance Amplification:** Longer and more variable lead times force inventory managers to hold higher safety stocks. When delays are asymmetric, managers often overreact to the "long tail" events, placing massive orders to compensate for perceived shortages [cite: 16, 17, 18].
*   **Panic Ordering:** The uncertainty associated with the "tail" of the delay distribution reduces trust in the supply line. This leads to "shortage gaming" or panic ordering, which further clogs the transport network and increases the asymmetry of the delay (a positive feedback loop) [cite: 19].

---

## 5. Quantitative Assessment of Resilience

To rigorously evaluate the impact of asymmetric delays, researchers employ quantitative metrics, primarily derived from control theory.

### 5.1 ITAE Analysis
The **Integral of Time Absolute Error (ITAE)** is the gold standard for measuring response resilience in this context. It calculates the area between the response curve and the target curve.
*   **Impact of Asymmetry:** Studies show that as the uncertainty or asymmetry of the lead time increases, the ITAE value rises significantly. This indicates a degradation in resilience: the system takes longer to recover and deviates further from the target [cite: 2, 3, 5].
*   **Optimization Failure:** A critical finding is that parameter settings that optimize ITAE for a *fixed* lead time often perform poorly when the lead time becomes variable or asymmetric. There is a lack of robustness; a system tuned for high resilience (fast response) is often hypersensitive to delay variations [cite: 2, 5, 20].

### 5.2 Resilience vs. Robustness Trade-off
A recurring theme in the literature is the trade-off between resilience and robustness.
*   **Resilience:** The ability to recover quickly (low settling time).
*   **Robustness:** The ability to maintain stability despite parameter changes (e.g., lead time fluctuating from 5 days to 15 days).
*   **The Conflict:** To achieve high resilience (fast recovery), inventory controllers often use aggressive gain parameters (high $\alpha$ in control loops). However, these aggressive settings make the system unstable if the transport delay increases (asymmetry). Conversely, a robust system (conservative settings) will remain stable during a long-tail delay but will be sluggish to recover, exhibiting poor response resilience [cite: 2, 5, 20].

### 5.3 Service Level and Cost Implications
The degradation of response resilience due to asymmetric delays has direct operational consequences:
*   **Inventory Costs:** To buffer against the "long tail" of the delay distribution, firms must hold excessive inventory. Research indicates that inventory levels are positively related to procurement lead time and its variance [cite: 21, 22].
*   **Stockouts:** Despite higher average inventory, the "drift" phenomenon can lead to stockouts during the specific periods when the delay distribution skews right. The system fails to "catch up" with the delayed supply [cite: 23, 24].
*   **Backlogs:** Asymmetric delays often result in the simultaneous occurrence of high inventory costs (due to safety stock) and high backlog costs (due to stockouts during tail events), a "worst of both worlds" scenario [cite: 25].

---

## 6. Mitigation Strategies and Adaptive Mechanisms

Given the destabilizing effects of asymmetric transport delays, the research suggests several strategies to enhance response resilience.

### 6.1 Dynamic Parameter Adjustment
Static inventory policies fail under asymmetric conditions. Resilience requires adaptive mechanisms.
*   **Variable GIT Targets:** Spiegler et al. propose making the target Goods in Transit (GIT) a variable function of demand and *actual* lead time, rather than a fixed constant. This allows the system to adjust its expectations dynamically, reducing inventory drift [cite: 3].
*   **Lead-Time Dependent Ordering:** Ordering policies must be designed in accordance with the *actual* lead time. If the lead time extends (tail event), the ordering logic must account for the increased pipeline stock required to maintain flow, without over-ordering (panic) [cite: 6, 7].

### 6.2 Postponement and Stock Sharing
Strategies that decouple inventory allocation from immediate transport dependency can mitigate delay impacts.
*   **Postponement:** Delaying the final differentiation of products (e.g., branding or packaging) until the product is closer to the customer or until demand is confirmed. This allows for pooling of inventory risks. Research shows a U-shaped relationship between response time and postponement rate, indicating an optimal level of postponement can significantly enhance resilience [cite: 26].
*   **Stock Sharing:** In humanitarian and commercial logistics, sharing unbranded stock among different actors can buffer against asymmetric delays affecting specific routes. This increases the effective inventory availability without increasing total system stock [cite: 26].

### 6.3 Visibility and Digital Twins
The "misperception" of lead time is a primary cause of inventory drift. Therefore, increasing visibility is a direct resilience enabler.
*   **Real-Time Tracking:** Utilizing technologies (like RFID or GPS) to obtain accurate, real-time distributions of transport delays allows the inventory controller to update its $T_p$ (lead time) parameter dynamically [cite: 7, 27].
*   **Digital Twins:** Creating a digital replica of the supply chain allows managers to simulate the impact of "long tail" delay events and test the stability of their inventory policies. This helps in identifying the "breaking points" where resilience gives way to instability [cite: 13].
*   **Predictive Analytics:** Machine learning models (e.g., Random Forest, Gradient Boosted Trees) can be used to predict delay anomalies and "long tail" events better than simple averages, allowing for proactive inventory adjustments [cite: 9, 11, 28].

### 6.4 Redundancy and Multi-Sourcing
*   **Backup Supply:** Establishing backup suppliers with different transport routes (and thus different delay distributions) can truncate the "long tail" of the aggregate delay distribution. If the primary route fails (extreme delay), the backup route is activated [cite: 21, 29].
*   **Buffer Stocks:** While costly, strategically placed buffer stocks at critical nodes (e.g., regional warehouses) are necessary to cover the "time to recover" during a delay event [cite: 4, 23].

---

## 7. Empirical and Simulation Evidence

### 7.1 Grocery and Retail Sectors
Studies in the grocery sector, which operates with low margins and high volume, show that inventory drift under demand uncertainty and variable lead times minimizes resilience performance. Simulation models of distribution centers reveal that nonlinearities (like truck capacity limits) combined with delay asymmetry create complex oscillations in stock levels [cite: 3, 8, 29].

### 7.2 Semiconductor and PC Industry
In Assemble-to-Order (ATO) systems like the PC industry, capacity constraints act as a major source of asymmetric delay (delays spike when capacity is hit). Research indicates that these capacity-induced delays negatively influence supply chain performance, creating permanent inventory drift if feedback loops are not corrected [cite: 12, 30].

### 7.3 Humanitarian Logistics
In disaster response, transport delays are inherently asymmetric and extreme. Case studies in the Caribbean demonstrate that "prepositioning" and "postponement" (delaying branding) are effective strategies. The "response time" metric in these scenarios is critical, and stock-sharing policies were found to improve fill rates and utilization despite the uncertain transport environment [cite: 26].

---

## 8. Conclusion

The impact of asymmetric transport delay distribution on the response resilience of inventory allocation is profound and destabilizing. The research conclusively shows that treating transport delays as symmetric or constant leads to **inventory drift**, where inventory levels permanently diverge from targets, and **instability**, where the system oscillates or becomes chaotic.

**Key Findings:**
1.  **Drift is Inevitable without Correction:** Without accurate, real-time updates to lead-time parameters, standard inventory policies (like APVIOBPCS) cannot maintain target levels under asymmetric delay conditions [cite: 6, 7].
2.  **Resilience-Robustness Conflict:** There is no "free lunch." Tuning a system for maximum response resilience (fast recovery) makes it vulnerable to instability when delays fluctuate. Managers must choose a balance point or employ adaptive controllers [cite: 2, 5].
3.  **Asymmetry Requires Nonlinear Solutions:** Linear models fail to capture the risks of "long tail" delays. Solutions must involve nonlinear interventions like dynamic GIT targets, postponement, and capacity buffering [cite: 3, 26].

**Future Outlook:**
The field is moving toward **adaptive control systems** and **AI-driven parameterization**. Future inventory systems will likely not use a static "lead time" parameter but will instead ingest a real-time probability distribution of arrival times, adjusting order rates continuously to maintain stability and resilience in an increasingly asymmetric world.

---

### References
*   **[cite: 4]** Simo, "Response resilience inventory allocation transport delay," *ECMS 2024*.
*   **[cite: 13]** "Emergency Response Resilience Assessment," *Sustainability*, 2024.
*   **[cite: 9, 28]** Ladva et al., "The Impact of Supply Chain Delays on Inventory Levels," *Engineering, Technology & Applied Science Research*, 2024.
*   **[cite: 6]** Wang et al., "Stability analysis of constrained inventory systems," *EJOR*, 2012.
*   **[cite: 26]** "Prepositioning and postponement in humanitarian logistics," *Ozyegin University*, 2024.
*   **[cite: 7]** Wang, Disney, & Wang, "Stability analysis of constrained inventory systems with transportation delay," *EJOR*, 2012.
*   **[cite: 23]** Mohammed & Mandal, "Impact of lead time variability on SCM," *IJSCM*, 2024.
*   **[cite: 3]** Spiegler et al., "A control engineering approach to the assessment of supply chain resilience," *International Journal of Production Research*, 2012/2015.
*   **[cite: 12, 30]** Lin, "Dynamic modelling and analysis of a personal computer ATO system," *Cardiff University*, 2018.
*   **[cite: 2, 5, 20, 31]** Spiegler, Naim, & Wikner, "A control engineering approach to the assessment of supply chain resilience," *IJPR*, 2012.
*   **[cite: 1, 2]** Ke et al., "Identification and formation mechanism of key elements of supply chain resilience," *PLoS ONE*, 2023.
*   **[cite: 27]** "Resilience of a three-echelon supply chain subject to potential disruptions," *The ASPD*, 2025.
*   **[cite: 10, 11]** "Predicting supply chain disruptions," *INFORMS/CIRRELT*, 2021.

**Sources:**
1. [plos.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH43YIrTLY7jciMyrplJP81tTgQu1-WEDn0j1ceqBNvphCeOmaUxv_tgtT_EgZ6-aOuwelqUEwt4huOrP-EZGUMXgkqQ9DCwr5lo6MpFyo9tr3q3CI5YAS_7zZPvo97DO-kOGipu1eAaEE2O7VQ4e64YNVr8R70oKNV4WI-rS-x)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtuFsocw2Zr7u8XJcq2To23vrvXSOG4_eEn_Kay1mSUlZ1hqmuq2FFdWcXl445_WG7j7c93tmhZOHnGCpZNvUGWOMbIOvmYs87k6H12yF7s2-F5bSeUnf49x5Xd_JFy3wClCdZpGnBLNTUSsRpteSmhhCLpAOTX5TJUgEE8wLfyPrezV3nlJlgrfkkDLlr5S5ZwtP6MfgFQLTcMc1A5v6JsHscFLNneopf3BKO2xjK2Ap6i-A=)
3. [core.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnXDZB3qZo324iEriG9LN5f4Rimafi_mwtmi_ocU2-OmMU5E8ZfosswNLCF4KOse66bM5dnRz2B2gL4X6p3G5aiUo8mzPg2pbNTWuDebPvbKV82jcrpqU5zZ-8HmDR)
4. [scs-europe.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuoNWePM-dQnz16braEUX9ktnBqABCJsYlQQKyIStvoh3sGapY6pYSei-3_o9rtJBs-FBKkndo-64TzCl7f_RUmE02-eavMWNn-vWo2PqmD4yaWSAesfA8qjNxpK3hd7QAHLr3NAa6rodwsFYGuLMwYuQGoq9k9WomA39KfLRPws6fv-1Kx5wpDdwn_Yg=)
5. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyBYEfKWFhyKiZiArgS-bmj-QWr-A2Jr3JkSSgkjsM5Ik8_IKoYW-ifTO52sjA1Ey4avCw0HHDVJhY11258IW0UfGYUsO7t3Zr0usmMOUJmaxxYvmEw84Ha9ga4IOtIjpAOfH0S5xdlBq-xt4OqYP7qPPLO1y4)
6. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGG8mweI31PumGDFIK4wITzsRVHoNX18TLISwU-enX1h9IWgvJtJcqsWHaHu6nOS06LWY-WTxuxLqYBRUKkpwd3ecA61neyq6WwqmHd5dc3f6vGpzevLCbOGWMxGEBjN7kgrB70dn6XsF-F3bvNNAvQDA==)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVGcHGdgqcuaPKIsBlZRrlaOCTcwFkkgOza5mWHXGARXqR_VuATGVUFwMev4Xyt-5QWBJ2RDG7kLIUjYB0cNZhRqnPdZ49Nhw9BP8jfRQ3R5Yky740kms5s7eg8-G6FjCroGfNteNT8zRMCnPTzHBlVb2b12QwMNLiQo5azDhUAyGSvQO7IvBwLl0xGRfOWFQYGlrA7KrADvk-MLob1m7Cob5JZcEDNU86HwzBSjGxmLPtd6zPajE=)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENp9mvWcgVqagRkFZDtXeGIZ0fmlnHJ4cbwZ8cbksrUlAUhe23pkFRBWEsTqcccEXY6My5eUiitwedH_Z0pBtOeuFQ8OWNsRbjerKmTq5Il6RbBf3xnCd2muAID9Z2w1vmOziyTwcozJ1unaloL3P9mfA9686g4WbYzCn3gf4ZdIEqnKGWmP7lEX5amp9VLVCa9UwbpWJQK6LxS2pDaMBgne06U8dolcHvPCslMg39V_oyNwLjjklurDtMIVZuXI-6yHSbP_bvZdZxARgK2FqMGL4FscyS7WnBY7-ltw22DUk=)
9. [etasr.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHH38nyYlwLfLVglcS_e7QYIfJ4wbVSaE_Kt3Ytfijxz1IKT5v4yLdfOMlhoKyf1I12knOfq-EqKuyc2X6kWdyFtNvtLsaKx3ltEfZv92pFgUq07JhvSlN8JspUA94w7n9Jk6VPcBJQ7syfyUYQ-Hr8bTgSR1nVT0c=)
10. [informs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJN2QHoK9MnuXX8LzcQearM25A313guHCWAb0MNYjaFJ-qI5ato2a1Aj4tPMohjlK2IedvqLqvN6kU6isEBlgCgSVmwbV1wULXEekBoJcxdXN_iICIhkkUuibrZhicuWoBtssBvJ7iQh3e1-jpQPk=)
11. [cirrelt.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcjKGc4p9vEgdpaYtCF1F22ysiC9fPFtIA5sNyJb-URyIAsCyzsyRZk3SA2pgSskyHxrXceOsMLtk2w8vJl9C9k4VJdU1I_MDPW4DQVbF5HVPFbd6XFsIwb9hzIv80MSEASiGMxi3ppyP0x-3ODp7xSg==)
12. [cardiff.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrND2j4r-0XTVEj99cb9Y1eIo9togUK3Gir0xhgnw-sKBEWEvQObWpN6rjJS5UB1tHSyvA6zabzADvdEDvPiDsF4IXFTGkXc0akH-_5CKQDUakQEyfpYNTajFU8m5WQqFKzSO2qpZzCze6CFaZNjq66LkkyESzot9Zj3G-R_J50NC9)
13. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrdsXNhGmuN5ABkbTTov3m39ywC3fKTKG-CZ6wmIPF16Do-JxU63434jczqIMsK91atBWFkHRx8XjmqNTPCAnVZav1s-B0RRVczDnsnkvv-I4IvpUh5ERUeGmNaOWSVA==)
14. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3Uk9EvWZQteAYYyQOcAgiq8EsyZfPB8GmuLL3BLbSVaoHAx2dEq_DyNtalg8XG_fzoTbICRsK0-H4PDyoMIIWOm8nQyjBqe4Pjshr340tc2j-ujpChysVTMs9oTBcwIJisNfgf7aeeagcC4Lg5geS-0nBk7DtgDGPnX6ykTXLTumUmqdKV_aUZGSMMnErjmTweS1WCuSYb6mi1u2fryYPChr0PCduYpnmzwxKCfHkZso3QV-vG9dx6z72lO97AgmK1sYKLfbim_JCr_mkDkKr)
15. [kent.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZP1uizzRkTmxzGK-vIjYNZ04ipcuig_-9PitG4R_EnmVJfFVGk4V-M4t6U7x8QkzHzg6EbaUwrQV5L1MNSfZ5ksigRybktNZE97aoltTOsfcqc5XE95hjaSlzqRIf4mkw8yQ=)
16. [unityscm.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElU5cihqWDY4---7TcuxSBh1MjVokmfzCc6KVgV8VGnB95oVEvWtZiO2nT1BqPXviELMZuPtFAfJh6AQhlTp1hHh0ckEq-pxXS3_HtU5MqxRTiCC21j8lLZfOZ9YDsjOBpQRw6_H_jSDVO2t3w4qcyTd3KVNyjjaCA78R0qHouEZl5CCyatxnDd3-zCouj_VEn2pfwhEITGbzrxtK7xRaEOiL8YQ==)
17. [quloi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7lrLwIU_BvIw0HlYhZeYNeVaUhnAcWpERLomRvag6puZ-PxXIOn-gU3VXB6BtT9IMZTz_OlYyuhrzQ4S9f3ZK984F7Pc3be5D75vbP6AOR4Mo6kUNQsvwAnmthq2kQoj55ccULGrDvOlE0pgWKJhyLRiBq2Zm0iqxj7FXUuE8LpUduP_e)
18. [patrickrigoni.ch](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3rZBcF_X-PnUZKDJF8hxkUi9S6nbzVhIeIPGZNcR0-bIp-Vz0NV4fLXDp2tgjqFrWftjrfLlKE8iHTV_DU59GmGHVFDs_9JrhfW6Huen7k9g-c7k3gQEI9-FES3JeTyjLYZghc9rvU14mcuPOcwi9JKs4ovRMbIFFkXMPWHcflRyOuUGulB-8IlCrMPIsjFDijmDZEk7f5iv3L12NwUc7dlvF9_dAWvAWaqg9GQ==)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJDx-m1JRqtU-QAXUoc7WPcIj9AfvU4AyXlw3g0hLHwOnL1imks9aG9H_6i40ywcjYHZVav_N6f-vy2cqVS4xdK65UMflaEpepk0l8BlEIfs1AGbY5ZXxvFDBACGgJr0MZP_ScnsXU2_POV2W43nTVXAjMWQTyj_mY-JQvoh64XdlMh18uxsUwkCQm3BtMVm6TIPASsw1rbN6piekVMslmJrO3VzFTajHzx15L)
20. [brunel.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0bjWp8tZBHUQsGzVuWL-WW25fwwbFLoWIJD1Lmk-vWABUTiiFUXvG-XgRBcMuz7oPpiGUGp8mGd5-DYqJvLNma2CaWvr5WjWmY9gNHP-0_MgxoRpYsmBnWYPclb3LdGGwDfYYNu1i2I3mROzjthhjkBY=)
21. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcy9-dMRKkpSCuK47rECFNOJWcT3nKSPUnOrDgjpEz621gmMirL-yIB99Ns2QRYM4QvTuuD2cZ26zB2ZstkBBvK9T7bFZUNcWcZIHvRHyw7UU5EO-k4CYDAOA2_iZ0O6q874YO6RwFF6TQWJnjtZBu2zdRSLDC98ZHPVzNp8xOwZATLx1Mww52TeQqdCTipve6xzsdFc54EkdDpgDWdwDSUxwjSJEMSw==)
22. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIapZDo6SMkD9z1WJoKbi-kiiCVFn_FwcvdzygMgmJjrAA1LEwGVLA0TjSdwoHVG7RU45trCd5kF27s0v_-8xjMNsxHH1nhJnmfIvt0RV3TilB8dgX47_ZFu32pErv5flKUcOndwHrTCEOKwTnmUy1LIOOMQOZt_yhplMc8dlC-KrjuRIdt90uKLdva7eQYVYJZo-J_1Ho54HYpuGPkNiXgCykb-ta-1yuIU0emf_0EYOLt2wBAPndT7CkJCgm2slJ)
23. [iprjb.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFj1enGr-JkIP5DVAmsByg3CkArGn3reSZEJMVQtLg91hPVal4VcT5MXc8nFP0Nq9cfuVQPmaBErkgIT-63VMLmfXJ11EchqmlYOVEZq7H127n3-EnZNNgXeIZhAceYEDa2Jzub7Yoo9Q==)
24. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0qYXcB2Y7grPn70CH4YDH064a3dQ1XobVb9EkiI6r7iQR0dy8YbC6adH4ksCDb0lW8qgtTXEdn-Y2tE7vz9r5YkhppcYnr5gYcWzL59NfFH3OxHI2qOFr0BS_8wDpDMkgnphPIFplIK3ZaXppeMPBZiiBb9cV2O532_KlMOzXyIt-C6XMn1MRIiBzpyyXlNJaWKWkQ_IFW0_spjIo5M9beNliFxBB6A==)
25. [kent.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeieJDnA9NoCr9kRI8Szx3EE-a0oYtaLaQeESKdW2BKoeidvYJtttKmna6nNbNYWHnEU85DzkkMF5AxaikZOu9SMjKEDlREUsaxwdKL-KK0v26ki7X8HcQsAffgWPMM8jrifh57LxbZ96t4ZevdwKUG7ZGl6kyH1XfcBqmNN-d)
26. [ozyegin.edu.tr](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3NVL7Mw_Az-E9Ojlldg33VqInXP4ZA88ESZnEjyauEvKZ9e8Qis0PluwALKaXDlkeqx1EMG1KyuT3iq9Nzf6qgEABfTBBpMlyTqQEG9l6i84YbdKUquuhTMimdvZc0aAP5Z8Nw1-dgXpwgyHdhaWHF3uU8RoITd5e-KjK6qsx0OTOZgp01SlfQlcFuPM4LmF39jbx0Bm3MNwOBhmKig==)
27. [theaspd.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEf-TeIv8OCNun9Fy4RyvGh0yXgaJQmXZ5cwynGO4kHnMwS4SxlAIE8QawKsDgzq79AzDkbg-F8duu9-01C3QWEdsilF-E_WyAD3gXWoIOEw8h4w1SAxq_c8rDtMIuPHroilUCC3Pt83Xa1)
28. [etasr.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGivCq_t703CwHf00BtW154FOSeXmE6LzLNrqQt9vPxiu4cGH2H51MW-eqCmyjliNYyA0I-TagDWy6D-bANz891Phk4Qh89cCOIu2ifYidS6R8qIVvGdpChmnW6sggI6A3ETMptoMHn4vw=)
29. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHimZvICvZOAYkMLpL6NqT2oURTQrlfWDZxpLCWwwFCkBU6Qfh3tFDpGllohUNzPN78_NZKPIJKzHg2Bx3UG6Xf1qqxy6cwrfzyN4iIaZ0cuDN3VM4Il3MuyMLagabgRxfQWhwcbwJC-iyxq4YCWK3XAdXl-1oitgAHQzo2ErEHEF03SoTKo6ll4QFSk6Tnw_ETeyOnw6fUUg==)
30. [cardiff.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPry6IfaDDHEfOzhAg3iJb_mqZ3bKaVYm1beyL-mb2V0aA_YE0N_Wz3gWEOcVpvdXTvuCq39WZUOrS1LAngDRrrTUJK8pT1HXXlATLBKM29SOg70BA417aBOWlNLuLVU60JgRmnSs72dTGdzIfjFqDlW6y)
31. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHta-R-lxYonMfbBNi45se3B9JrTFq2TguUOXbUsHxsSlIf3xkC69Dv9QmlvhGkLK9n34aHGjf68wBQGhgT8LmjEqQRlxp0868JHT3effkNi0bfjiD8qtyXzbI1oA==)


## Annotations
Annotation(end_index=3916, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtuFsocw2Zr7u8XJcq2To23vrvXSOG4_eEn_Kay1mSUlZ1hqmuq2FFdWcXl445_WG7j7c93tmhZOHnGCpZNvUGWOMbIOvmYs87k6H12yF7s2-F5bSeUnf49x5Xd_JFy3wClCdZpGnBLNTUSsRpteSmhhCLpAOTX5TJUgEE8wLfyPrezV3nlJlgrfkkDLlr5S5ZwtP6MfgFQLTcMc1A5v6JsHscFLNneopf3BKO2xjK2Ap6i-A=', start_index=3901)
Annotation(end_index=3916, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnXDZB3qZo324iEriG9LN5f4Rimafi_mwtmi_ocU2-OmMU5E8ZfosswNLCF4KOse66bM5dnRz2B2gL4X6p3G5aiUo8mzPg2pbNTWuDebPvbKV82jcrpqU5zZ-8HmDR', start_index=3901)
Annotation(end_index=3916, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH43YIrTLY7jciMyrplJP81tTgQu1-WEDn0j1ceqBNvphCeOmaUxv_tgtT_EgZ6-aOuwelqUEwt4huOrP-EZGUMXgkqQ9DCwr5lo6MpFyo9tr3q3CI5YAS_7zZPvo97DO-kOGipu1eAaEE2O7VQ4e64YNVr8R70oKNV4WI-rS-x', start_index=3901)
Annotation(end_index=4449, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuoNWePM-dQnz16braEUX9ktnBqABCJsYlQQKyIStvoh3sGapY6pYSei-3_o9rtJBs-FBKkndo-64TzCl7f_RUmE02-eavMWNn-vWo2PqmD4yaWSAesfA8qjNxpK3hd7QAHLr3NAa6rodwsFYGuLMwYuQGoq9k9WomA39KfLRPws6fv-1Kx5wpDdwn_Yg=', start_index=4440)
Annotation(end_index=4870, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtuFsocw2Zr7u8XJcq2To23vrvXSOG4_eEn_Kay1mSUlZ1hqmuq2FFdWcXl445_WG7j7c93tmhZOHnGCpZNvUGWOMbIOvmYs87k6H12yF7s2-F5bSeUnf49x5Xd_JFy3wClCdZpGnBLNTUSsRpteSmhhCLpAOTX5TJUgEE8wLfyPrezV3nlJlgrfkkDLlr5S5ZwtP6MfgFQLTcMc1A5v6JsHscFLNneopf3BKO2xjK2Ap6i-A=', start_index=4855)
Annotation(end_index=4870, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyBYEfKWFhyKiZiArgS-bmj-QWr-A2Jr3JkSSgkjsM5Ik8_IKoYW-ifTO52sjA1Ey4avCw0HHDVJhY11258IW0UfGYUsO7t3Zr0usmMOUJmaxxYvmEw84Ha9ga4IOtIjpAOfH0S5xdlBq-xt4OqYP7qPPLO1y4', start_index=4855)
Annotation(end_index=4870, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnXDZB3qZo324iEriG9LN5f4Rimafi_mwtmi_ocU2-OmMU5E8ZfosswNLCF4KOse66bM5dnRz2B2gL4X6p3G5aiUo8mzPg2pbNTWuDebPvbKV82jcrpqU5zZ-8HmDR', start_index=4855)
Annotation(end_index=5359, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVGcHGdgqcuaPKIsBlZRrlaOCTcwFkkgOza5mWHXGARXqR_VuATGVUFwMev4Xyt-5QWBJ2RDG7kLIUjYB0cNZhRqnPdZ49Nhw9BP8jfRQ3R5Yky740kms5s7eg8-G6FjCroGfNteNT8zRMCnPTzHBlVb2b12QwMNLiQo5azDhUAyGSvQO7IvBwLl0xGRfOWFQYGlrA7KrADvk-MLob1m7Cob5JZcEDNU86HwzBSjGxmLPtd6zPajE=', start_index=5347)
Annotation(end_index=5359, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGG8mweI31PumGDFIK4wITzsRVHoNX18TLISwU-enX1h9IWgvJtJcqsWHaHu6nOS06LWY-WTxuxLqYBRUKkpwd3ecA61neyq6WwqmHd5dc3f6vGpzevLCbOGWMxGEBjN7kgrB70dn6XsF-F3bvNNAvQDA==', start_index=5347)
Annotation(end_index=5723, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENp9mvWcgVqagRkFZDtXeGIZ0fmlnHJ4cbwZ8cbksrUlAUhe23pkFRBWEsTqcccEXY6My5eUiitwedH_Z0pBtOeuFQ8OWNsRbjerKmTq5Il6RbBf3xnCd2muAID9Z2w1vmOziyTwcozJ1unaloL3P9mfA9686g4WbYzCn3gf4ZdIEqnKGWmP7lEX5amp9VLVCa9UwbpWJQK6LxS2pDaMBgne06U8dolcHvPCslMg39V_oyNwLjjklurDtMIVZuXI-6yHSbP_bvZdZxARgK2FqMGL4FscyS7WnBY7-ltw22DUk=', start_index=5708)
Annotation(end_index=5723, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyBYEfKWFhyKiZiArgS-bmj-QWr-A2Jr3JkSSgkjsM5Ik8_IKoYW-ifTO52sjA1Ey4avCw0HHDVJhY11258IW0UfGYUsO7t3Zr0usmMOUJmaxxYvmEw84Ha9ga4IOtIjpAOfH0S5xdlBq-xt4OqYP7qPPLO1y4', start_index=5708)
Annotation(end_index=5723, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnXDZB3qZo324iEriG9LN5f4Rimafi_mwtmi_ocU2-OmMU5E8ZfosswNLCF4KOse66bM5dnRz2B2gL4X6p3G5aiUo8mzPg2pbNTWuDebPvbKV82jcrpqU5zZ-8HmDR', start_index=5708)
Annotation(end_index=6224, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVGcHGdgqcuaPKIsBlZRrlaOCTcwFkkgOza5mWHXGARXqR_VuATGVUFwMev4Xyt-5QWBJ2RDG7kLIUjYB0cNZhRqnPdZ49Nhw9BP8jfRQ3R5Yky740kms5s7eg8-G6FjCroGfNteNT8zRMCnPTzHBlVb2b12QwMNLiQo5azDhUAyGSvQO7IvBwLl0xGRfOWFQYGlrA7KrADvk-MLob1m7Cob5JZcEDNU86HwzBSjGxmLPtd6zPajE=', start_index=6215)
Annotation(end_index=6588, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVGcHGdgqcuaPKIsBlZRrlaOCTcwFkkgOza5mWHXGARXqR_VuATGVUFwMev4Xyt-5QWBJ2RDG7kLIUjYB0cNZhRqnPdZ49Nhw9BP8jfRQ3R5Yky740kms5s7eg8-G6FjCroGfNteNT8zRMCnPTzHBlVb2b12QwMNLiQo5azDhUAyGSvQO7IvBwLl0xGRfOWFQYGlrA7KrADvk-MLob1m7Cob5JZcEDNU86HwzBSjGxmLPtd6zPajE=', start_index=6576)
Annotation(end_index=6588, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGG8mweI31PumGDFIK4wITzsRVHoNX18TLISwU-enX1h9IWgvJtJcqsWHaHu6nOS06LWY-WTxuxLqYBRUKkpwd3ecA61neyq6WwqmHd5dc3f6vGpzevLCbOGWMxGEBjN7kgrB70dn6XsF-F3bvNNAvQDA==', start_index=6576)
Annotation(end_index=7116, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJN2QHoK9MnuXX8LzcQearM25A313guHCWAb0MNYjaFJ-qI5ato2a1Aj4tPMohjlK2IedvqLqvN6kU6isEBlgCgSVmwbV1wULXEekBoJcxdXN_iICIhkkUuibrZhicuWoBtssBvJ7iQh3e1-jpQPk=', start_index=7103)
Annotation(end_index=7116, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHH38nyYlwLfLVglcS_e7QYIfJ4wbVSaE_Kt3Ytfijxz1IKT5v4yLdfOMlhoKyf1I12knOfq-EqKuyc2X6kWdyFtNvtLsaKx3ltEfZv92pFgUq07JhvSlN8JspUA94w7n9Jk6VPcBJQ7syfyUYQ-Hr8bTgSR1nVT0c=', start_index=7103)
Annotation(end_index=7372, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJN2QHoK9MnuXX8LzcQearM25A313guHCWAb0MNYjaFJ-qI5ato2a1Aj4tPMohjlK2IedvqLqvN6kU6isEBlgCgSVmwbV1wULXEekBoJcxdXN_iICIhkkUuibrZhicuWoBtssBvJ7iQh3e1-jpQPk=', start_index=7358)
Annotation(end_index=7372, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcjKGc4p9vEgdpaYtCF1F22ysiC9fPFtIA5sNyJb-URyIAsCyzsyRZk3SA2pgSskyHxrXceOsMLtk2w8vJl9C9k4VJdU1I_MDPW4DQVbF5HVPFbd6XFsIwb9hzIv80MSEASiGMxi3ppyP0x-3ODp7xSg==', start_index=7358)
Annotation(end_index=7610, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHH38nyYlwLfLVglcS_e7QYIfJ4wbVSaE_Kt3Ytfijxz1IKT5v4yLdfOMlhoKyf1I12knOfq-EqKuyc2X6kWdyFtNvtLsaKx3ltEfZv92pFgUq07JhvSlN8JspUA94w7n9Jk6VPcBJQ7syfyUYQ-Hr8bTgSR1nVT0c=', start_index=7601)
Annotation(end_index=7923, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrND2j4r-0XTVEj99cb9Y1eIo9togUK3Gir0xhgnw-sKBEWEvQObWpN6rjJS5UB1tHSyvA6zabzADvdEDvPiDsF4IXFTGkXc0akH-_5CKQDUakQEyfpYNTajFU8m5WQqFKzSO2qpZzCze6CFaZNjq66LkkyESzot9Zj3G-R_J50NC9', start_index=7913)
Annotation(end_index=8166, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrdsXNhGmuN5ABkbTTov3m39ywC3fKTKG-CZ6wmIPF16Do-JxU63434jczqIMsK91atBWFkHRx8XjmqNTPCAnVZav1s-B0RRVczDnsnkvv-I4IvpUh5ERUeGmNaOWSVA==', start_index=8156)
Annotation(end_index=8323, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcjKGc4p9vEgdpaYtCF1F22ysiC9fPFtIA5sNyJb-URyIAsCyzsyRZk3SA2pgSskyHxrXceOsMLtk2w8vJl9C9k4VJdU1I_MDPW4DQVbF5HVPFbd6XFsIwb9hzIv80MSEASiGMxi3ppyP0x-3ODp7xSg==', start_index=8313)
Annotation(end_index=8737, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHH38nyYlwLfLVglcS_e7QYIfJ4wbVSaE_Kt3Ytfijxz1IKT5v4yLdfOMlhoKyf1I12knOfq-EqKuyc2X6kWdyFtNvtLsaKx3ltEfZv92pFgUq07JhvSlN8JspUA94w7n9Jk6VPcBJQ7syfyUYQ-Hr8bTgSR1nVT0c=', start_index=8728)
Annotation(end_index=9483, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVGcHGdgqcuaPKIsBlZRrlaOCTcwFkkgOza5mWHXGARXqR_VuATGVUFwMev4Xyt-5QWBJ2RDG7kLIUjYB0cNZhRqnPdZ49Nhw9BP8jfRQ3R5Yky740kms5s7eg8-G6FjCroGfNteNT8zRMCnPTzHBlVb2b12QwMNLiQo5azDhUAyGSvQO7IvBwLl0xGRfOWFQYGlrA7KrADvk-MLob1m7Cob5JZcEDNU86HwzBSjGxmLPtd6zPajE=', start_index=9471)
Annotation(end_index=9483, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGG8mweI31PumGDFIK4wITzsRVHoNX18TLISwU-enX1h9IWgvJtJcqsWHaHu6nOS06LWY-WTxuxLqYBRUKkpwd3ecA61neyq6WwqmHd5dc3f6vGpzevLCbOGWMxGEBjN7kgrB70dn6XsF-F3bvNNAvQDA==', start_index=9471)
Annotation(end_index=10228, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVGcHGdgqcuaPKIsBlZRrlaOCTcwFkkgOza5mWHXGARXqR_VuATGVUFwMev4Xyt-5QWBJ2RDG7kLIUjYB0cNZhRqnPdZ49Nhw9BP8jfRQ3R5Yky740kms5s7eg8-G6FjCroGfNteNT8zRMCnPTzHBlVb2b12QwMNLiQo5azDhUAyGSvQO7IvBwLl0xGRfOWFQYGlrA7KrADvk-MLob1m7Cob5JZcEDNU86HwzBSjGxmLPtd6zPajE=', start_index=10219)
Annotation(end_index=10495, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnXDZB3qZo324iEriG9LN5f4Rimafi_mwtmi_ocU2-OmMU5E8ZfosswNLCF4KOse66bM5dnRz2B2gL4X6p3G5aiUo8mzPg2pbNTWuDebPvbKV82jcrpqU5zZ-8HmDR', start_index=10482)
Annotation(end_index=10495, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3Uk9EvWZQteAYYyQOcAgiq8EsyZfPB8GmuLL3BLbSVaoHAx2dEq_DyNtalg8XG_fzoTbICRsK0-H4PDyoMIIWOm8nQyjBqe4Pjshr340tc2j-ujpChysVTMs9oTBcwIJisNfgf7aeeagcC4Lg5geS-0nBk7DtgDGPnX6ykTXLTumUmqdKV_aUZGSMMnErjmTweS1WCuSYb6mi1u2fryYPChr0PCduYpnmzwxKCfHkZso3QV-vG9dx6z72lO97AgmK1sYKLfbim_JCr_mkDkKr', start_index=10482)
Annotation(end_index=10959, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVGcHGdgqcuaPKIsBlZRrlaOCTcwFkkgOza5mWHXGARXqR_VuATGVUFwMev4Xyt-5QWBJ2RDG7kLIUjYB0cNZhRqnPdZ49Nhw9BP8jfRQ3R5Yky740kms5s7eg8-G6FjCroGfNteNT8zRMCnPTzHBlVb2b12QwMNLiQo5azDhUAyGSvQO7IvBwLl0xGRfOWFQYGlrA7KrADvk-MLob1m7Cob5JZcEDNU86HwzBSjGxmLPtd6zPajE=', start_index=10947)
Annotation(end_index=10959, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGG8mweI31PumGDFIK4wITzsRVHoNX18TLISwU-enX1h9IWgvJtJcqsWHaHu6nOS06LWY-WTxuxLqYBRUKkpwd3ecA61neyq6WwqmHd5dc3f6vGpzevLCbOGWMxGEBjN7kgrB70dn6XsF-F3bvNNAvQDA==', start_index=10947)
Annotation(end_index=11322, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZP1uizzRkTmxzGK-vIjYNZ04ipcuig_-9PitG4R_EnmVJfFVGk4V-M4t6U7x8QkzHzg6EbaUwrQV5L1MNSfZ5ksigRybktNZE97aoltTOsfcqc5XE95hjaSlzqRIf4mkw8yQ=', start_index=11309)
Annotation(end_index=11322, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGG8mweI31PumGDFIK4wITzsRVHoNX18TLISwU-enX1h9IWgvJtJcqsWHaHu6nOS06LWY-WTxuxLqYBRUKkpwd3ecA61neyq6WwqmHd5dc3f6vGpzevLCbOGWMxGEBjN7kgrB70dn6XsF-F3bvNNAvQDA==', start_index=11309)
Annotation(end_index=11751, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElU5cihqWDY4---7TcuxSBh1MjVokmfzCc6KVgV8VGnB95oVEvWtZiO2nT1BqPXviELMZuPtFAfJh6AQhlTp1hHh0ckEq-pxXS3_HtU5MqxRTiCC21j8lLZfOZ9YDsjOBpQRw6_H_jSDVO2t3w4qcyTd3KVNyjjaCA78R0qHouEZl5CCyatxnDd3-zCouj_VEn2pfwhEITGbzrxtK7xRaEOiL8YQ==', start_index=11733)
Annotation(end_index=11751, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7lrLwIU_BvIw0HlYhZeYNeVaUhnAcWpERLomRvag6puZ-PxXIOn-gU3VXB6BtT9IMZTz_OlYyuhrzQ4S9f3ZK984F7Pc3be5D75vbP6AOR4Mo6kUNQsvwAnmthq2kQoj55ccULGrDvOlE0pgWKJhyLRiBq2Zm0iqxj7FXUuE8LpUduP_e', start_index=11733)
Annotation(end_index=11751, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3rZBcF_X-PnUZKDJF8hxkUi9S6nbzVhIeIPGZNcR0-bIp-Vz0NV4fLXDp2tgjqFrWftjrfLlKE8iHTV_DU59GmGHVFDs_9JrhfW6Huen7k9g-c7k3gQEI9-FES3JeTyjLYZghc9rvU14mcuPOcwi9JKs4ovRMbIFFkXMPWHcflRyOuUGulB-8IlCrMPIsjFDijmDZEk7f5iv3L12NwUc7dlvF9_dAWvAWaqg9GQ==', start_index=11733)
Annotation(end_index=12051, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJDx-m1JRqtU-QAXUoc7WPcIj9AfvU4AyXlw3g0hLHwOnL1imks9aG9H_6i40ywcjYHZVav_N6f-vy2cqVS4xdK65UMflaEpepk0l8BlEIfs1AGbY5ZXxvFDBACGgJr0MZP_ScnsXU2_POV2W43nTVXAjMWQTyj_mY-JQvoh64XdlMh18uxsUwkCQm3BtMVm6TIPASsw1rbN6piekVMslmJrO3VzFTajHzx15L', start_index=12041)
Annotation(end_index=12728, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtuFsocw2Zr7u8XJcq2To23vrvXSOG4_eEn_Kay1mSUlZ1hqmuq2FFdWcXl445_WG7j7c93tmhZOHnGCpZNvUGWOMbIOvmYs87k6H12yF7s2-F5bSeUnf49x5Xd_JFy3wClCdZpGnBLNTUSsRpteSmhhCLpAOTX5TJUgEE8wLfyPrezV3nlJlgrfkkDLlr5S5ZwtP6MfgFQLTcMc1A5v6JsHscFLNneopf3BKO2xjK2Ap6i-A=', start_index=12713)
Annotation(end_index=12728, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyBYEfKWFhyKiZiArgS-bmj-QWr-A2Jr3JkSSgkjsM5Ik8_IKoYW-ifTO52sjA1Ey4avCw0HHDVJhY11258IW0UfGYUsO7t3Zr0usmMOUJmaxxYvmEw84Ha9ga4IOtIjpAOfH0S5xdlBq-xt4OqYP7qPPLO1y4', start_index=12713)
Annotation(end_index=12728, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnXDZB3qZo324iEriG9LN5f4Rimafi_mwtmi_ocU2-OmMU5E8ZfosswNLCF4KOse66bM5dnRz2B2gL4X6p3G5aiUo8mzPg2pbNTWuDebPvbKV82jcrpqU5zZ-8HmDR', start_index=12713)
Annotation(end_index=13063, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtuFsocw2Zr7u8XJcq2To23vrvXSOG4_eEn_Kay1mSUlZ1hqmuq2FFdWcXl445_WG7j7c93tmhZOHnGCpZNvUGWOMbIOvmYs87k6H12yF7s2-F5bSeUnf49x5Xd_JFy3wClCdZpGnBLNTUSsRpteSmhhCLpAOTX5TJUgEE8wLfyPrezV3nlJlgrfkkDLlr5S5ZwtP6MfgFQLTcMc1A5v6JsHscFLNneopf3BKO2xjK2Ap6i-A=', start_index=13047)
Annotation(end_index=13063, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyBYEfKWFhyKiZiArgS-bmj-QWr-A2Jr3JkSSgkjsM5Ik8_IKoYW-ifTO52sjA1Ey4avCw0HHDVJhY11258IW0UfGYUsO7t3Zr0usmMOUJmaxxYvmEw84Ha9ga4IOtIjpAOfH0S5xdlBq-xt4OqYP7qPPLO1y4', start_index=13047)
Annotation(end_index=13063, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0bjWp8tZBHUQsGzVuWL-WW25fwwbFLoWIJD1Lmk-vWABUTiiFUXvG-XgRBcMuz7oPpiGUGp8mGd5-DYqJvLNma2CaWvr5WjWmY9gNHP-0_MgxoRpYsmBnWYPclb3LdGGwDfYYNu1i2I3mROzjthhjkBY=', start_index=13047)
Annotation(end_index=13850, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtuFsocw2Zr7u8XJcq2To23vrvXSOG4_eEn_Kay1mSUlZ1hqmuq2FFdWcXl445_WG7j7c93tmhZOHnGCpZNvUGWOMbIOvmYs87k6H12yF7s2-F5bSeUnf49x5Xd_JFy3wClCdZpGnBLNTUSsRpteSmhhCLpAOTX5TJUgEE8wLfyPrezV3nlJlgrfkkDLlr5S5ZwtP6MfgFQLTcMc1A5v6JsHscFLNneopf3BKO2xjK2Ap6i-A=', start_index=13834)
Annotation(end_index=13850, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyBYEfKWFhyKiZiArgS-bmj-QWr-A2Jr3JkSSgkjsM5Ik8_IKoYW-ifTO52sjA1Ey4avCw0HHDVJhY11258IW0UfGYUsO7t3Zr0usmMOUJmaxxYvmEw84Ha9ga4IOtIjpAOfH0S5xdlBq-xt4OqYP7qPPLO1y4', start_index=13834)
Annotation(end_index=13850, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0bjWp8tZBHUQsGzVuWL-WW25fwwbFLoWIJD1Lmk-vWABUTiiFUXvG-XgRBcMuz7oPpiGUGp8mGd5-DYqJvLNma2CaWvr5WjWmY9gNHP-0_MgxoRpYsmBnWYPclb3LdGGwDfYYNu1i2I3mROzjthhjkBY=', start_index=13834)
Annotation(end_index=14241, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcy9-dMRKkpSCuK47rECFNOJWcT3nKSPUnOrDgjpEz621gmMirL-yIB99Ns2QRYM4QvTuuD2cZ26zB2ZstkBBvK9T7bFZUNcWcZIHvRHyw7UU5EO-k4CYDAOA2_iZ0O6q874YO6RwFF6TQWJnjtZBu2zdRSLDC98ZHPVzNp8xOwZATLx1Mww52TeQqdCTipve6xzsdFc54EkdDpgDWdwDSUxwjSJEMSw==', start_index=14227)
Annotation(end_index=14241, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIapZDo6SMkD9z1WJoKbi-kiiCVFn_FwcvdzygMgmJjrAA1LEwGVLA0TjSdwoHVG7RU45trCd5kF27s0v_-8xjMNsxHH1nhJnmfIvt0RV3TilB8dgX47_ZFu32pErv5flKUcOndwHrTCEOKwTnmUy1LIOOMQOZt_yhplMc8dlC-KrjuRIdt90uKLdva7eQYVYJZo-J_1Ho54HYpuGPkNiXgCykb-ta-1yuIU0emf_0EYOLt2wBAPndT7CkJCgm2slJ', start_index=14227)
Annotation(end_index=14479, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFj1enGr-JkIP5DVAmsByg3CkArGn3reSZEJMVQtLg91hPVal4VcT5MXc8nFP0Nq9cfuVQPmaBErkgIT-63VMLmfXJ11EchqmlYOVEZq7H127n3-EnZNNgXeIZhAceYEDa2Jzub7Yoo9Q==', start_index=14465)
Annotation(end_index=14479, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0qYXcB2Y7grPn70CH4YDH064a3dQ1XobVb9EkiI6r7iQR0dy8YbC6adH4ksCDb0lW8qgtTXEdn-Y2tE7vz9r5YkhppcYnr5gYcWzL59NfFH3OxHI2qOFr0BS_8wDpDMkgnphPIFplIK3ZaXppeMPBZiiBb9cV2O532_KlMOzXyIt-C6XMn1MRIiBzpyyXlNJaWKWkQ_IFW0_spjIo5M9beNliFxBB6A==', start_index=14465)
Annotation(end_index=14713, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeieJDnA9NoCr9kRI8Szx3EE-a0oYtaLaQeESKdW2BKoeidvYJtttKmna6nNbNYWHnEU85DzkkMF5AxaikZOu9SMjKEDlREUsaxwdKL-KK0v26ki7X8HcQsAffgWPMM8jrifh57LxbZ96t4ZevdwKUG7ZGl6kyH1XfcBqmNN-d', start_index=14703)
Annotation(end_index=15326, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnXDZB3qZo324iEriG9LN5f4Rimafi_mwtmi_ocU2-OmMU5E8ZfosswNLCF4KOse66bM5dnRz2B2gL4X6p3G5aiUo8mzPg2pbNTWuDebPvbKV82jcrpqU5zZ-8HmDR', start_index=15317)
Annotation(end_index=15617, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVGcHGdgqcuaPKIsBlZRrlaOCTcwFkkgOza5mWHXGARXqR_VuATGVUFwMev4Xyt-5QWBJ2RDG7kLIUjYB0cNZhRqnPdZ49Nhw9BP8jfRQ3R5Yky740kms5s7eg8-G6FjCroGfNteNT8zRMCnPTzHBlVb2b12QwMNLiQo5azDhUAyGSvQO7IvBwLl0xGRfOWFQYGlrA7KrADvk-MLob1m7Cob5JZcEDNU86HwzBSjGxmLPtd6zPajE=', start_index=15605)
Annotation(end_index=15617, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGG8mweI31PumGDFIK4wITzsRVHoNX18TLISwU-enX1h9IWgvJtJcqsWHaHu6nOS06LWY-WTxuxLqYBRUKkpwd3ecA61neyq6WwqmHd5dc3f6vGpzevLCbOGWMxGEBjN7kgrB70dn6XsF-F3bvNNAvQDA==', start_index=15605)
Annotation(end_index=16161, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3NVL7Mw_Az-E9Ojlldg33VqInXP4ZA88ESZnEjyauEvKZ9e8Qis0PluwALKaXDlkeqx1EMG1KyuT3iq9Nzf6qgEABfTBBpMlyTqQEG9l6i84YbdKUquuhTMimdvZc0aAP5Z8Nw1-dgXpwgyHdhaWHF3uU8RoITd5e-KjK6qsx0OTOZgp01SlfQlcFuPM4LmF39jbx0Bm3MNwOBhmKig==', start_index=16151)
Annotation(end_index=16439, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3NVL7Mw_Az-E9Ojlldg33VqInXP4ZA88ESZnEjyauEvKZ9e8Qis0PluwALKaXDlkeqx1EMG1KyuT3iq9Nzf6qgEABfTBBpMlyTqQEG9l6i84YbdKUquuhTMimdvZc0aAP5Z8Nw1-dgXpwgyHdhaWHF3uU8RoITd5e-KjK6qsx0OTOZgp01SlfQlcFuPM4LmF39jbx0Bm3MNwOBhmKig==', start_index=16429)
Annotation(end_index=16849, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVGcHGdgqcuaPKIsBlZRrlaOCTcwFkkgOza5mWHXGARXqR_VuATGVUFwMev4Xyt-5QWBJ2RDG7kLIUjYB0cNZhRqnPdZ49Nhw9BP8jfRQ3R5Yky740kms5s7eg8-G6FjCroGfNteNT8zRMCnPTzHBlVb2b12QwMNLiQo5azDhUAyGSvQO7IvBwLl0xGRfOWFQYGlrA7KrADvk-MLob1m7Cob5JZcEDNU86HwzBSjGxmLPtd6zPajE=', start_index=16836)
Annotation(end_index=16849, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEf-TeIv8OCNun9Fy4RyvGh0yXgaJQmXZ5cwynGO4kHnMwS4SxlAIE8QawKsDgzq79AzDkbg-F8duu9-01C3QWEdsilF-E_WyAD3gXWoIOEw8h4w1SAxq_c8rDtMIuPHroilUCC3Pt83Xa1', start_index=16836)
Annotation(end_index=17140, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrdsXNhGmuN5ABkbTTov3m39ywC3fKTKG-CZ6wmIPF16Do-JxU63434jczqIMsK91atBWFkHRx8XjmqNTPCAnVZav1s-B0RRVczDnsnkvv-I4IvpUh5ERUeGmNaOWSVA==', start_index=17130)
Annotation(end_index=17395, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGivCq_t703CwHf00BtW154FOSeXmE6LzLNrqQt9vPxiu4cGH2H51MW-eqCmyjliNYyA0I-TagDWy6D-bANz891Phk4Qh89cCOIu2ifYidS6R8qIVvGdpChmnW6sggI6A3ETMptoMHn4vw=', start_index=17378)
Annotation(end_index=17395, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHH38nyYlwLfLVglcS_e7QYIfJ4wbVSaE_Kt3Ytfijxz1IKT5v4yLdfOMlhoKyf1I12knOfq-EqKuyc2X6kWdyFtNvtLsaKx3ltEfZv92pFgUq07JhvSlN8JspUA94w7n9Jk6VPcBJQ7syfyUYQ-Hr8bTgSR1nVT0c=', start_index=17378)
Annotation(end_index=17395, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcjKGc4p9vEgdpaYtCF1F22ysiC9fPFtIA5sNyJb-URyIAsCyzsyRZk3SA2pgSskyHxrXceOsMLtk2w8vJl9C9k4VJdU1I_MDPW4DQVbF5HVPFbd6XFsIwb9hzIv80MSEASiGMxi3ppyP0x-3ODp7xSg==', start_index=17378)
Annotation(end_index=17716, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcy9-dMRKkpSCuK47rECFNOJWcT3nKSPUnOrDgjpEz621gmMirL-yIB99Ns2QRYM4QvTuuD2cZ26zB2ZstkBBvK9T7bFZUNcWcZIHvRHyw7UU5EO-k4CYDAOA2_iZ0O6q874YO6RwFF6TQWJnjtZBu2zdRSLDC98ZHPVzNp8xOwZATLx1Mww52TeQqdCTipve6xzsdFc54EkdDpgDWdwDSUxwjSJEMSw==', start_index=17702)
Annotation(end_index=17716, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHimZvICvZOAYkMLpL6NqT2oURTQrlfWDZxpLCWwwFCkBU6Qfh3tFDpGllohUNzPN78_NZKPIJKzHg2Bx3UG6Xf1qqxy6cwrfzyN4iIaZ0cuDN3VM4Il3MuyMLagabgRxfQWhwcbwJC-iyxq4YCWK3XAdXl-1oitgAHQzo2ErEHEF03SoTKo6ll4QFSk6Tnw_ETeyOnw6fUUg==', start_index=17702)
Annotation(end_index=17915, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFj1enGr-JkIP5DVAmsByg3CkArGn3reSZEJMVQtLg91hPVal4VcT5MXc8nFP0Nq9cfuVQPmaBErkgIT-63VMLmfXJ11EchqmlYOVEZq7H127n3-EnZNNgXeIZhAceYEDa2Jzub7Yoo9Q==', start_index=17902)
Annotation(end_index=17915, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuoNWePM-dQnz16braEUX9ktnBqABCJsYlQQKyIStvoh3sGapY6pYSei-3_o9rtJBs-FBKkndo-64TzCl7f_RUmE02-eavMWNn-vWo2PqmD4yaWSAesfA8qjNxpK3hd7QAHLr3NAa6rodwsFYGuLMwYuQGoq9k9WomA39KfLRPws6fv-1Kx5wpDdwn_Yg=', start_index=17902)
Annotation(end_index=18376, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENp9mvWcgVqagRkFZDtXeGIZ0fmlnHJ4cbwZ8cbksrUlAUhe23pkFRBWEsTqcccEXY6My5eUiitwedH_Z0pBtOeuFQ8OWNsRbjerKmTq5Il6RbBf3xnCd2muAID9Z2w1vmOziyTwcozJ1unaloL3P9mfA9686g4WbYzCn3gf4ZdIEqnKGWmP7lEX5amp9VLVCa9UwbpWJQK6LxS2pDaMBgne06U8dolcHvPCslMg39V_oyNwLjjklurDtMIVZuXI-6yHSbP_bvZdZxARgK2FqMGL4FscyS7WnBY7-ltw22DUk=', start_index=18360)
Annotation(end_index=18376, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnXDZB3qZo324iEriG9LN5f4Rimafi_mwtmi_ocU2-OmMU5E8ZfosswNLCF4KOse66bM5dnRz2B2gL4X6p3G5aiUo8mzPg2pbNTWuDebPvbKV82jcrpqU5zZ-8HmDR', start_index=18360)
Annotation(end_index=18376, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHimZvICvZOAYkMLpL6NqT2oURTQrlfWDZxpLCWwwFCkBU6Qfh3tFDpGllohUNzPN78_NZKPIJKzHg2Bx3UG6Xf1qqxy6cwrfzyN4iIaZ0cuDN3VM4Il3MuyMLagabgRxfQWhwcbwJC-iyxq4YCWK3XAdXl-1oitgAHQzo2ErEHEF03SoTKo6ll4QFSk6Tnw_ETeyOnw6fUUg==', start_index=18360)
Annotation(end_index=18760, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPry6IfaDDHEfOzhAg3iJb_mqZ3bKaVYm1beyL-mb2V0aA_YE0N_Wz3gWEOcVpvdXTvuCq39WZUOrS1LAngDRrrTUJK8pT1HXXlATLBKM29SOg70BA417aBOWlNLuLVU60JgRmnSs72dTGdzIfjFqDlW6y', start_index=18746)
Annotation(end_index=18760, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrND2j4r-0XTVEj99cb9Y1eIo9togUK3Gir0xhgnw-sKBEWEvQObWpN6rjJS5UB1tHSyvA6zabzADvdEDvPiDsF4IXFTGkXc0akH-_5CKQDUakQEyfpYNTajFU8m5WQqFKzSO2qpZzCze6CFaZNjq66LkkyESzot9Zj3G-R_J50NC9', start_index=18746)
Annotation(end_index=19190, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3NVL7Mw_Az-E9Ojlldg33VqInXP4ZA88ESZnEjyauEvKZ9e8Qis0PluwALKaXDlkeqx1EMG1KyuT3iq9Nzf6qgEABfTBBpMlyTqQEG9l6i84YbdKUquuhTMimdvZc0aAP5Z8Nw1-dgXpwgyHdhaWHF3uU8RoITd5e-KjK6qsx0OTOZgp01SlfQlcFuPM4LmF39jbx0Bm3MNwOBhmKig==', start_index=19180)
Annotation(end_index=19845, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVGcHGdgqcuaPKIsBlZRrlaOCTcwFkkgOza5mWHXGARXqR_VuATGVUFwMev4Xyt-5QWBJ2RDG7kLIUjYB0cNZhRqnPdZ49Nhw9BP8jfRQ3R5Yky740kms5s7eg8-G6FjCroGfNteNT8zRMCnPTzHBlVb2b12QwMNLiQo5azDhUAyGSvQO7IvBwLl0xGRfOWFQYGlrA7KrADvk-MLob1m7Cob5JZcEDNU86HwzBSjGxmLPtd6zPajE=', start_index=19833)
Annotation(end_index=19845, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGG8mweI31PumGDFIK4wITzsRVHoNX18TLISwU-enX1h9IWgvJtJcqsWHaHu6nOS06LWY-WTxuxLqYBRUKkpwd3ecA61neyq6WwqmHd5dc3f6vGpzevLCbOGWMxGEBjN7kgrB70dn6XsF-F3bvNNAvQDA==', start_index=19833)
Annotation(end_index=20115, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtuFsocw2Zr7u8XJcq2To23vrvXSOG4_eEn_Kay1mSUlZ1hqmuq2FFdWcXl445_WG7j7c93tmhZOHnGCpZNvUGWOMbIOvmYs87k6H12yF7s2-F5bSeUnf49x5Xd_JFy3wClCdZpGnBLNTUSsRpteSmhhCLpAOTX5TJUgEE8wLfyPrezV3nlJlgrfkkDLlr5S5ZwtP6MfgFQLTcMc1A5v6JsHscFLNneopf3BKO2xjK2Ap6i-A=', start_index=20103)
Annotation(end_index=20115, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyBYEfKWFhyKiZiArgS-bmj-QWr-A2Jr3JkSSgkjsM5Ik8_IKoYW-ifTO52sjA1Ey4avCw0HHDVJhY11258IW0UfGYUsO7t3Zr0usmMOUJmaxxYvmEw84Ha9ga4IOtIjpAOfH0S5xdlBq-xt4OqYP7qPPLO1y4', start_index=20103)
Annotation(end_index=20351, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3NVL7Mw_Az-E9Ojlldg33VqInXP4ZA88ESZnEjyauEvKZ9e8Qis0PluwALKaXDlkeqx1EMG1KyuT3iq9Nzf6qgEABfTBBpMlyTqQEG9l6i84YbdKUquuhTMimdvZc0aAP5Z8Nw1-dgXpwgyHdhaWHF3uU8RoITd5e-KjK6qsx0OTOZgp01SlfQlcFuPM4LmF39jbx0Bm3MNwOBhmKig==', start_index=20338)
Annotation(end_index=20351, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnXDZB3qZo324iEriG9LN5f4Rimafi_mwtmi_ocU2-OmMU5E8ZfosswNLCF4KOse66bM5dnRz2B2gL4X6p3G5aiUo8mzPg2pbNTWuDebPvbKV82jcrpqU5zZ-8HmDR', start_index=20338)
Annotation(end_index=20766, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuoNWePM-dQnz16braEUX9ktnBqABCJsYlQQKyIStvoh3sGapY6pYSei-3_o9rtJBs-FBKkndo-64TzCl7f_RUmE02-eavMWNn-vWo2PqmD4yaWSAesfA8qjNxpK3hd7QAHLr3NAa6rodwsFYGuLMwYuQGoq9k9WomA39KfLRPws6fv-1Kx5wpDdwn_Yg=', start_index=20757)
Annotation(end_index=20864, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrdsXNhGmuN5ABkbTTov3m39ywC3fKTKG-CZ6wmIPF16Do-JxU63434jczqIMsK91atBWFkHRx8XjmqNTPCAnVZav1s-B0RRVczDnsnkvv-I4IvpUh5ERUeGmNaOWSVA==', start_index=20854)
Annotation(end_index=20954, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGivCq_t703CwHf00BtW154FOSeXmE6LzLNrqQt9vPxiu4cGH2H51MW-eqCmyjliNYyA0I-TagDWy6D-bANz891Phk4Qh89cCOIu2ifYidS6R8qIVvGdpChmnW6sggI6A3ETMptoMHn4vw=', start_index=20941)
Annotation(end_index=20954, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHH38nyYlwLfLVglcS_e7QYIfJ4wbVSaE_Kt3Ytfijxz1IKT5v4yLdfOMlhoKyf1I12knOfq-EqKuyc2X6kWdyFtNvtLsaKx3ltEfZv92pFgUq07JhvSlN8JspUA94w7n9Jk6VPcBJQ7syfyUYQ-Hr8bTgSR1nVT0c=', start_index=20941)
Annotation(end_index=21103, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGG8mweI31PumGDFIK4wITzsRVHoNX18TLISwU-enX1h9IWgvJtJcqsWHaHu6nOS06LWY-WTxuxLqYBRUKkpwd3ecA61neyq6WwqmHd5dc3f6vGpzevLCbOGWMxGEBjN7kgrB70dn6XsF-F3bvNNAvQDA==', start_index=21094)
Annotation(end_index=21204, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3NVL7Mw_Az-E9Ojlldg33VqInXP4ZA88ESZnEjyauEvKZ9e8Qis0PluwALKaXDlkeqx1EMG1KyuT3iq9Nzf6qgEABfTBBpMlyTqQEG9l6i84YbdKUquuhTMimdvZc0aAP5Z8Nw1-dgXpwgyHdhaWHF3uU8RoITd5e-KjK6qsx0OTOZgp01SlfQlcFuPM4LmF39jbx0Bm3MNwOBhmKig==', start_index=21194)
Annotation(end_index=21311, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVGcHGdgqcuaPKIsBlZRrlaOCTcwFkkgOza5mWHXGARXqR_VuATGVUFwMev4Xyt-5QWBJ2RDG7kLIUjYB0cNZhRqnPdZ49Nhw9BP8jfRQ3R5Yky740kms5s7eg8-G6FjCroGfNteNT8zRMCnPTzHBlVb2b12QwMNLiQo5azDhUAyGSvQO7IvBwLl0xGRfOWFQYGlrA7KrADvk-MLob1m7Cob5JZcEDNU86HwzBSjGxmLPtd6zPajE=', start_index=21302)
Annotation(end_index=21447, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFj1enGr-JkIP5DVAmsByg3CkArGn3reSZEJMVQtLg91hPVal4VcT5MXc8nFP0Nq9cfuVQPmaBErkgIT-63VMLmfXJ11EchqmlYOVEZq7H127n3-EnZNNgXeIZhAceYEDa2Jzub7Yoo9Q==', start_index=21437)
Annotation(end_index=21541, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnXDZB3qZo324iEriG9LN5f4Rimafi_mwtmi_ocU2-OmMU5E8ZfosswNLCF4KOse66bM5dnRz2B2gL4X6p3G5aiUo8mzPg2pbNTWuDebPvbKV82jcrpqU5zZ-8HmDR', start_index=21532)
Annotation(end_index=21719, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPry6IfaDDHEfOzhAg3iJb_mqZ3bKaVYm1beyL-mb2V0aA_YE0N_Wz3gWEOcVpvdXTvuCq39WZUOrS1LAngDRrrTUJK8pT1HXXlATLBKM29SOg70BA417aBOWlNLuLVU60JgRmnSs72dTGdzIfjFqDlW6y', start_index=21705)
Annotation(end_index=21719, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrND2j4r-0XTVEj99cb9Y1eIo9togUK3Gir0xhgnw-sKBEWEvQObWpN6rjJS5UB1tHSyvA6zabzADvdEDvPiDsF4IXFTGkXc0akH-_5CKQDUakQEyfpYNTajFU8m5WQqFKzSO2qpZzCze6CFaZNjq66LkkyESzot9Zj3G-R_J50NC9', start_index=21705)
Annotation(end_index=21849, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtuFsocw2Zr7u8XJcq2To23vrvXSOG4_eEn_Kay1mSUlZ1hqmuq2FFdWcXl445_WG7j7c93tmhZOHnGCpZNvUGWOMbIOvmYs87k6H12yF7s2-F5bSeUnf49x5Xd_JFy3wClCdZpGnBLNTUSsRpteSmhhCLpAOTX5TJUgEE8wLfyPrezV3nlJlgrfkkDLlr5S5ZwtP6MfgFQLTcMc1A5v6JsHscFLNneopf3BKO2xjK2Ap6i-A=', start_index=21829)
Annotation(end_index=21849, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyBYEfKWFhyKiZiArgS-bmj-QWr-A2Jr3JkSSgkjsM5Ik8_IKoYW-ifTO52sjA1Ey4avCw0HHDVJhY11258IW0UfGYUsO7t3Zr0usmMOUJmaxxYvmEw84Ha9ga4IOtIjpAOfH0S5xdlBq-xt4OqYP7qPPLO1y4', start_index=21829)
Annotation(end_index=21849, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0bjWp8tZBHUQsGzVuWL-WW25fwwbFLoWIJD1Lmk-vWABUTiiFUXvG-XgRBcMuz7oPpiGUGp8mGd5-DYqJvLNma2CaWvr5WjWmY9gNHP-0_MgxoRpYsmBnWYPclb3LdGGwDfYYNu1i2I3mROzjthhjkBY=', start_index=21829)
Annotation(end_index=21849, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHta-R-lxYonMfbBNi45se3B9JrTFq2TguUOXbUsHxsSlIf3xkC69Dv9QmlvhGkLK9n34aHGjf68wBQGhgT8LmjEqQRlxp0868JHT3effkNi0bfjiD8qtyXzbI1oA==', start_index=21829)
Annotation(end_index=21989, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtuFsocw2Zr7u8XJcq2To23vrvXSOG4_eEn_Kay1mSUlZ1hqmuq2FFdWcXl445_WG7j7c93tmhZOHnGCpZNvUGWOMbIOvmYs87k6H12yF7s2-F5bSeUnf49x5Xd_JFy3wClCdZpGnBLNTUSsRpteSmhhCLpAOTX5TJUgEE8wLfyPrezV3nlJlgrfkkDLlr5S5ZwtP6MfgFQLTcMc1A5v6JsHscFLNneopf3BKO2xjK2Ap6i-A=', start_index=21977)
Annotation(end_index=21989, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH43YIrTLY7jciMyrplJP81tTgQu1-WEDn0j1ceqBNvphCeOmaUxv_tgtT_EgZ6-aOuwelqUEwt4huOrP-EZGUMXgkqQ9DCwr5lo6MpFyo9tr3q3CI5YAS_7zZPvo97DO-kOGipu1eAaEE2O7VQ4e64YNVr8R70oKNV4WI-rS-x', start_index=21977)
Annotation(end_index=22122, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEf-TeIv8OCNun9Fy4RyvGh0yXgaJQmXZ5cwynGO4kHnMwS4SxlAIE8QawKsDgzq79AzDkbg-F8duu9-01C3QWEdsilF-E_WyAD3gXWoIOEw8h4w1SAxq_c8rDtMIuPHroilUCC3Pt83Xa1', start_index=22112)
Annotation(end_index=22242, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJN2QHoK9MnuXX8LzcQearM25A313guHCWAb0MNYjaFJ-qI5ato2a1Aj4tPMohjlK2IedvqLqvN6kU6isEBlgCgSVmwbV1wULXEekBoJcxdXN_iICIhkkUuibrZhicuWoBtssBvJ7iQh3e1-jpQPk=', start_index=22228)
Annotation(end_index=22242, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcjKGc4p9vEgdpaYtCF1F22ysiC9fPFtIA5sNyJb-URyIAsCyzsyRZk3SA2pgSskyHxrXceOsMLtk2w8vJl9C9k4VJdU1I_MDPW4DQVbF5HVPFbd6XFsIwb9hzIv80MSEASiGMxi3ppyP0x-3ODp7xSg==', start_index=22228)

## Sources
