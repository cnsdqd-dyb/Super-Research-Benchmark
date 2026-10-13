# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 85844bbb | **Time:** 258.06s | **Cost:** $1.15827
--------------------------------------------------------------------------------

# Temporal Dynamics and Rating Correction in Seller Reputation Systems: Methodologies, Algorithms, and Mathematical Determinations

### Key Points
*   **Temporal Decay Necessity:** Static rating systems fail to reflect current seller behavior; therefore, systems employ temporal functions (aging factors) to weight recent feedback more heavily than historical data.
*   **Determination Algorithms:** The specific value of decay factors (e.g., $\lambda$) is often determined through iterative optimization algorithms that minimize the difference between calculated reputation and actual ranking stability (e.g., the RBTR scheme).
*   **Rating Correction Coefficients:** Advanced collaborative filtering models utilize rating correction coefficients ($rev_1$) derived from the exponential of rating discrepancies to adjust user-to-user similarity measures before temporal weighting is applied.
*   **Anomaly Detection in Time Domain:** Systems like TAUCA and TATA determine rating corrections by analyzing the time-domain sequence of ratings to detect sudden shifts indicative of "whitewashing" or "bad-mouthing" attacks, rather than applying a simple uniform decay.
*   **Proportional Decay:** Research indicates that in some competitive models, the rate of reputation decay is proportional to the current rating magnitude relative to a lower bound, causing high reputations to decay faster in the absence of new positive reinforcement.

### Executive Summary
The determination of the temporal function in rating correction within seller reputation systems is a complex interplay of statistical modeling, anomaly detection, and heuristic optimization. Unlike static systems that average all historical ratings equally, modern reputation engines recognize that a seller's performance is dynamic. The "temporal function" generally refers to the mathematical mechanism—often an exponential decay or aging factor—used to discount older ratings. The "rating correction" refers to the pre- or post-processing steps taken to filter out noise (both natural inconsistencies and malicious manipulation) before the reputation score is finalized.

This report details how these functions are derived. It explores the **RBTR (Review-Based Trust Reputation)** scheme, which algorithmically selects an aging factor to maximize ranking stability. It examines **TAUCA (Temporal and User Correlation Analysis)**, which uses time-series analysis to identify and correct anomalous rating intervals. Furthermore, it analyzes mathematical formulations where correction coefficients are embedded into similarity functions in collaborative filtering to account for user preference variations over time. Finally, it addresses the strategic implications of these determinations, such as the "regression to the mean" phenomena where high reputations are engineered to decay more rapidly to incentivize continued high performance.

---

## 1. Introduction to Temporal Dynamics in Reputation Systems

Reputation systems serve as the trust layer of electronic commerce, mitigating information asymmetry between buyers and sellers. However, a fundamental challenge in these systems is the **temporal validity** of the data. A seller who provided excellent service two years ago but has recently deteriorated in quality should not maintain a high reputation score based solely on accumulated historical inertia. Conversely, a seller who has improved should not be permanently penalized for early mistakes.

To address this, reputation systems incorporate **temporal functions** that adjust the weight of ratings based on their age. This process is often coupled with **rating correction**, a methodology designed to identify and rectify erroneous or malicious ratings (noise) before they impact the final score. The determination of these functions is not arbitrary; it relies on specific mathematical models and optimization algorithms designed to balance **responsiveness** (reacting to recent changes) with **stability** (resisting volatility from sparse data).

### 1.1 The Necessity of Rating Correction and Time Decay
Raw ratings are subject to various forms of error:
1.  **Natural Noise:** Inconsistencies due to user subjectivity or mood, unrelated to the actual product or service quality [cite: 1, 2].
2.  **Malicious Noise:** Sybil attacks, ballot stuffing, or bad-mouthing attacks where ratings are fabricated to manipulate reputation [cite: 3].
3.  **Temporal Irrelevance:** Accurate ratings that have lost predictive power due to the passage of time [cite: 4, 5].

The integration of temporal functions into rating correction aims to filter these noises while preserving the signal of the seller's current true behavior.

---

## 2. Mathematical Determination of Temporal Decay Factors

The core of temporal rating correction is the **decay function**, often parameterized by a variable (commonly $\lambda$ or $\alpha$) known as the aging or forgetting factor. The determination of this factor is critical: if set too high, the system ignores history and becomes volatile; if set too low, the system becomes unresponsive to recent behavior changes.

### 2.1 The Exponential Decay Principle
The most prevalent model for temporal adjustment is exponential decay. In this model, the weight $w$ of a rating $r$ at time $t$ is calculated relative to the current time $t_{current}$.

The general formula for the weight is often expressed as:
\[ w_i = e^{-\mu(t_{current} - t_{i})} \]
or
\[ w_i = \lambda^{(t_{current} - t_{i})} \]
where $\mu$ is a decay constant and $\lambda$ is the aging factor ($0 < \lambda \le 1$) [cite: 5, 6].

In discrete time models, such as Dirichlet reputation systems, the accumulated reputation is updated by scaling down past evidence by a constant factor each time a new rating window opens [cite: 7].

### 2.2 Algorithmic Determination of the Aging Factor ($\lambda$)
A critical question is how the specific value of $\lambda$ is chosen. It is rarely a fixed static value in advanced systems; rather, it is determined via optimization algorithms.

#### The RBTR Optimization Approach
The **Review-Based Trust Reputation (RBTR)** scheme provides a concrete algorithm for determining $\lambda$. The goal is to find a $\lambda$ that makes the reputation score "representative and timely" [cite: 4].

**Algorithm for Determining $\lambda$:**
The RBTR scheme employs an iterative decision algorithm to select $\lambda$. The process involves:
1.  **Initialization:** The algorithm starts with a high $\lambda$ (close to 1, implying little decay).
2.  **Comparison Function $\Upsilon(\alpha)$:** This function calculates the average ranking distance between the reputation scores derived using the candidate $\lambda = \alpha$ and a baseline (e.g., the current market ranking or a "ground truth" dataset).
3.  **Iterative Adjustment:**
    *   The algorithm tests decreasing values of $\lambda$ (e.g., $\alpha_1 = 1 - 10^i$).
    *   It computes the stability or difference metric $\delta = \Upsilon(\alpha)$.
    *   It compares the difference between consecutive iterations ($|\delta_1 - \delta_2| / \delta_1$).
    *   If the change in the ranking distance stabilizes (drops below a threshold, e.g., 0.1), the current $\alpha$ is accepted as the optimal aging factor.

This method ensures that the decay factor is not arbitrary but is empirically tuned to the specific sensitivity of the item type or market category [cite: 4]. Different product categories (e.g., electronics vs. books) may require different decay rates, and this algorithm dynamically determines the appropriate rate.

### 2.3 Proportional Decay and Current Rating Magnitude
In competitive environments, the determination of decay is sometimes linked to the *magnitude* of the current reputation. Research into response strategies in competitive markets suggests a **proportional decay structure**.

The decay rate can be modeled as proportional to the difference between the current rating $x_i(t)$ and a lower bound $a$:
\[ \text{Decay Rate} \propto (x_i(t) - a) \]
This formulation implies that **decay is faster when the current rating is high** [cite: 8]. The intuition is that maintaining a high reputation requires constant effort; without new positive information ("maintenance"), a high reputation naturally regresses toward the mean or a lower bound more aggressively than a mediocre reputation does. This acts as a "gravity" force in rating correction, ensuring that high scores represent active excellence rather than historical accumulation.

---

## 3. Rating Correction Coefficients in Collaborative Filtering

Beyond simple time decay, "rating correction" involves adjusting the similarity measures between users in recommender systems to account for variations in rating behavior. This is often implemented via **correction coefficients**.

### 3.1 The Rating Correction Coefficient ($rev_1$)
Traditional cosine similarity metrics often fail to capture the nuance of user preference variations embedded in rating differences. To address this, researchers have introduced a **rating correction coefficient**, denoted as $rev_1$.

The formula for determining this coefficient is:
\[ rev_1(\vec{u}, \vec{v}) = e^{-\frac{1}{n} \sum_{i \in I_{u,v}} |r_{u,i} - r_{v,i}|} \]
Where:
*   $n$ is the number of co-rated items.
*   $|r_{u,i} - r_{v,i}|$ is the absolute difference in ratings provided by users $u$ and $v$ for item $i$ [cite: 9, 10].

**Function:** This coefficient quantifies the discrepancy in rating values. As the discrepancy increases, the exponential function drives the coefficient toward 0, reducing the similarity weight. This serves as a correction mechanism that penalizes the similarity score between users who might have rated the same items but with significantly different values, effectively filtering out "noise" from divergent rating scales before temporal weights are applied [cite: 10, 11].

### 3.2 Item Popularity Correction ($rev_2$)
To further correct for biases related to item trends (a temporal phenomenon), an item popularity coefficient is used:
\[ rev_2(i) = e^{\frac{N(i)}{|U|} - 1} \]
Where $N(i)$ is the number of ratings for item $i$ and $|U|$ is the total number of users. This coefficient adjusts the weight based on how widely rated (popular) an item is, correcting for the tendency of popular items to dominate similarity calculations [cite: 9, 10].

### 3.3 Modified Similarity Calculation
The final temporal rating correction is often a composite of these factors. The modified similarity $sim'(\vec{u}, \vec{v})$ combines the correction coefficients with standard measures:
\[ sim'(\vec{u}, \vec{v}) = rev_1(\vec{u}, \vec{v}) \cdot rev_2(i) \cdot \text{CosineSim}(\vec{u}, \vec{v}) \]
This corrected similarity is then used to predict ratings, often integrated with time-decay functions to prioritize recent data [cite: 11, 12].

---

## 4. Time-Domain Anomaly Detection for Rating Correction

While decay factors handle the natural aging of data, **anomaly detection** handles the correction of malicious ratings (attacks). The determination of which ratings to correct (or discard) is heavily reliant on **time-domain analysis**.

### 4.1 The TAUCA and TATA Schemes
**TAUCA (Temporal and User Correlation Analysis)** and its related scheme **TATA (Time Domain Anomaly Detection)** represent a class of algorithms that determine rating correction by analyzing the *sequence* of ratings over time [cite: 3, 13].

**Mechanism of Determination:**
1.  **Time-Sorting:** Ratings for an item are organized in descending order of their timestamps.
2.  **Change Detection (CUSUM):** The system employs a Cumulative Sum (CUSUM) control chart or similar change-point detection algorithms on the time-sorted sequence.
3.  **Anomaly Identification:**
    *   The algorithm looks for rapid changes in the rating distribution (e.g., a sudden spike in 5-star ratings or a drop to 1-star).
    *   It also detects "small changes accumulated over time," which might indicate a "slow-poisoning" attack where malicious ratings are inserted gradually to evade simple filters [cite: 14].
4.  **Correction:** Once a time interval is flagged as anomalous, the system analyzes the user correlation within that window. If a cluster of users in that timeframe shows high similarity (collusion) and deviation from the historical trend, their ratings are flagged as malicious.
5.  **Reputation Recovery:** The final reputation score is "corrected" by removing or down-weighting the ratings identified in the anomalous time windows [cite: 3].

This approach determines the "temporal function" not as a smooth decay, but as a **binary or weighted filter** applied to specific time intervals identified as suspicious.

### 4.2 Handling Natural Noise
Distinct from malicious attacks is **natural noise**—inconsistencies in honest user behavior. Systems handle this by classifying users and items into categories (e.g., "Benevolent," "Critical," "Variable") based on their rating history.

**Correction Strategy:**
*   **Detection:** A rating is flagged as noise if it contradicts the established user or item class (e.g., a "Critical" user giving a high rating to a generally "No-Preferred" item) [cite: 1, 2].
*   **Correction Formula:** If a rating $r_{u,i}$ is deemed noisy, it is corrected using probabilistic thresholds. For example, a low rating might be corrected using a formula involving the probability of the rating falling into different preference intervals ($k, v$ thresholds) [cite: 15].
*   **Temporal Integration:** After noise correction, a **power decay function** is often applied to give more weight to recent, corrected ratings [cite: 1, 16].

---

## 5. Strategic and Economic Implications of Temporal Correction

The determination of temporal functions is not merely a technical calibration but an economic strategy that influences seller behavior.

### 5.1 Strategic Pricing and Ratings Management
Sellers are aware of the temporal nature of reputation. Research shows that sellers may engage in **strategic pricing** to manage their ratings over time.
*   **High Prices & Ratings:** Higher prices generally reduce "value for money," potentially lowering ratings. However, they also filter for consumers with a "strong taste" for the product, who may rate it higher.
*   **Platform Sensitivity:** The platform must determine the **sensitivity** of its rating system (how quickly it reacts to new reviews). The optimal sensitivity depends on the elasticity of reviews to price changes. If a system decays too slowly, sellers have little incentive to lower prices or improve quality once a high reputation is established. If it decays too quickly, the system becomes unstable [cite: 17].

### 5.2 Reputation Cycles
The interaction between seller strategy and temporal rating correction can lead to **endogenous price and rating cycles**. Sellers may build up a reputation (high quality/low price), then "harvest" it (high price/lower quality) as the reputation decays, before rebuilding it again. The determination of the decay factor $\lambda$ directly influences the frequency and amplitude of these cycles [cite: 17].

---

## 6. Comparative Analysis of Temporal Correction Approaches

| Feature | **Exponential Decay / Aging Factor** | **Time-Domain Anomaly Detection (TAUCA/TATA)** | **Correction Coefficients ($rev_1$)** |
| :--- | :--- | :--- | :--- |
| **Primary Goal** | Devalue old information to reflect current state. | Identify and remove malicious attacks based on timing. | Adjust for user rating heterogeneity and preference variations. |
| **Determination Method** | Optimization algorithms (e.g., RBTR) minimizing ranking error. | CUSUM / Change-point detection on time-sorted sequences. | Mathematical formula based on rating discrepancies ($e^{-\Delta}$). |
| **Temporal Granularity** | Continuous or Discrete (Time Windows). | Interval-based (detecting specific attack windows). | Interaction-based (pairwise user comparison). |
| **Key Parameter** | $\lambda$ (Aging Factor) or $\mu$ (Decay Constant). | Thresholds for change detection and correlation. | $rev_1$ and $rev_2$ coefficients. |
| **Application** | General reputation maintenance; handling drift. | Security; defense against whitewashing/bad-mouthing. | Collaborative filtering; improving recommendation accuracy. |

### 6.1 The "Cold Start" vs. "Long-Term" Trade-off
A critical aspect of determining the temporal function is handling the **Cold Start** problem. New sellers have no history, so decay functions are irrelevant. However, for established sellers, the system must decide how much "reputation capital" they can bank.
*   **Logarithmic Weighting:** Some systems use logarithmic weighting for reputation increments to ensure that feedback from new authors/buyers is not completely drowned out by established high-reputation entities. This is a form of correction that balances the temporal accumulation of influence [cite: 18].
*   **Adaptive Decay:** Advanced systems may use an **adaptive decay factor** that changes based on the volume of ratings. For items with sparse ratings, decay might be slower to retain information; for items with high velocity, decay might be faster to reflect the latest trends [cite: 4].

---

## 7. Conclusion

The temporal function of rating correction in seller reputation systems is determined through a multi-layered process that goes beyond simple averaging. It begins with **noise detection**, utilizing time-domain analysis (TAUCA) and statistical classification to identify and correct anomalies. It proceeds to **similarity correction**, employing coefficients ($rev_1$) to adjust for user heterogeneity. Finally, it applies **temporal weighting**, typically using an exponential decay model where the aging factor $\lambda$ is algorithmically optimized (RBTR) to maximize the predictive accuracy and stability of the rankings.

Recent advancements suggest a move toward **proportional decay**, where the rate of decay is a function of the current rating's magnitude, thereby enforcing a "maintenance cost" on high-reputation sellers. These mechanisms collectively ensure that seller reputation remains a dynamic, trustworthy, and current reflection of market behavior, resilient to both the ravages of time and the manipulations of malicious actors.

### References
[cite: 17] Carnehl, C., et al. (2023). "Pricing for the Stars: Dynamic Pricing in the Presence of Rating Systems."
[cite: 3] "Anomaly Detection in Feedback-based Reputation Systems through Temporal and Correlation Analysis."
[cite: 1] Choudhary, P., et al. (2017). "Handling Natural Noise in Multi Criteria Recommender System..."
[cite: 2] "Managing natural noise in collaborative recommender systems."
[cite: 9] "Rating Correction Coefficient Formula."
[cite: 11] "CFSF: On Cloud-Based Recommendation for Large-Scale E-commerce."
[cite: 8] "Responding to Online Reviews in Competitive Markets."
[cite: 4] Wang, B.-C., et al. (2011). "RBTR: A Review-Based Trust Reputation Scheme."
[cite: 15] "An Efficient Approach to Manage Natural Noises in Recommender Systems."
[cite: 10] "Bundle recommendation methods considering rating data differences."
[cite: 3] "TAUCA: Temporal and User Correlation Analysis."
[cite: 13] "Providing Security on Online Reputation System Using Rate Auditing Technique."
[cite: 14] "TATA: Time Domain Anomaly Detection."
[cite: 18] "Reputation-based framework for high integrity sensor networks."
[cite: 6] "Blockchain Reputation Systems and Temporal Relevance."
[cite: 4] "RBTR Scheme Evaluation."
[cite: 5] "Time-Decay-Based Reputation Method."

**Sources:**
1. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjDTRIqgZJu44h37ZnUPABHvWuD-OiFSjRVQngLqCE0gSPD_YeCHOlGoXFnlqsW5YCss4mzqBuKxhxIOv7grX58-pST0_l3FMvj3bapctqu2hDWau_2jdgbGtaVHRhFv8USCueShMi6yQFV15oBB1j2HTyef4fXLVJ23Ya5EaY7DuYZovrXVROZ1lGyG7MGr6WM9SjoqjE8ZWFAlnwkR7sXK1uGXkJNlQH4OxyfudfY9TE7TkB9HgsvO7Xi01oAMAkVTyOAZ7y6TU4ADu12pHxhsBl0pX2jZ12SxiYr5QNUhdKcmjjk57sZyIFKQ==)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXgmdXGFo9Yh_5j_gDhwfPdOef8TqHxVEDVADmAyfvMbENvhAkWaP2PYhIvW_XhvNmeTtHYzHnK3GFKLrkGqT1X6YX7e72ER8WNDJ3dgYrloAZsetDFNnQRkmErfx3dkNP_IpaptsXR_ooJ_Jr1QOHy4QHwneEDxMG4Lknh9QlclREpzbavg22MVQKKru91wscP6ZwJ-RH9IY5Z51Ulc69JapQcg==)
3. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERS2FQb5hahEyXJylfy1dAvhrFh8ObycdwS-9rBZd0z6TYqM3tzIwYQJdkYK6-ePzfUuVHFZu9rUAFUbZnwmmFLOCuDNyVWYGFIY5OrG-2zF9Pj452P9eDlsUii86LAFS3o8c0HvTHaE_-prkXJOoLX3JXYco80HFacrattcT03P74IOiiu49MI4oD0XX5WEs_hZ86n0SUskMCih5bqDn3Q25I451mMxivrc7vLnne5jCkWtjxT3eoCbNm6laUnwDeaOLGWj5QD7Js)
4. [informatica.si](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKk-02J-nONYRjFaJONeCGWKN2ZZ3-t7zNwQp1dFkpE74cGuG2JW80Rct6LMy7rYscM4C8ZBywuyEsoR_JgICIMKrH88TM0FtSOhBnTr_BOsfKOyB-fKxq9iuSS1RnmeZgHySDpaKV6nZlHfxeiyWofEUWH-y5KmVmPgI=)
5. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMNw-MmTPyoFVdEK2GuXQXcniw-Kz8h33h7yUwIBkpkzmQBNOHkM8633Oo6BN4QzfqByGuu6RTVmR52IP1AMkrgc6uyZXTUhIxolK7gC2aUey7YTgT33hePD5J-Mk=)
6. [ijsat.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjIp_11fo2C6kR0t9mhsq2L2nbAOvsbFPKI1yL0ChetzXyH64f2OhaVZw7mut0m03zo-9Ln09guDw31oIJHyMie5JZizu8W4F7sWQ9Iw9Fj07J35t8BN7-OPW4XD0gkawF3g==)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_IhvTkPJBzv3_VGqN1XfMLLQcNecoIk9FTj2YFWkaAjq6FUsBWRre2Vzt8Qwybhg7fwcs4WURrc9C1Pdl8UMSFnH8muaT5rtFwHqecQHrHd4ihP11VVFMyI1Upzhe2ieXIe_EuS_18NrPuqWVEjYxMNFnHeh3l8DBVMnh_nQlPzPD6nn2janFuLycwJr3nARNGg83KU9rg9VKP6Tvff63Nm5BVjaZHxCUiodgP_amgVcOtXu2)
8. [umn.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxNiZUss7cC5BQnjluYEGiYCtV-xMkDxrm5NHln6L4sEFDM4K1JkWe5ZQf0tGKSYQOVdEGOHjAy2mgkAz5jAuKEAwgXnnqI0mj2Pe_oudXJ-BQ8u4DubvcTvWCVAl94G9aGuDCbnAsDuaPp58E5sba9nAZ9BTHQvU3lqEG0NhpD90Kyjxj6MSXZ0v5ueP_h2LL)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7aF4JlZarTbMkNigd5RvD9v7PeeIntEeJfpoh86x-KH6dV2aUav5Jz8cWOK01jJ9nEa-hn4t0F7ORAkMlSJrhoEJsCSpvPHRRBgbDTONhOu3eqf0YNeKfI3TDTonHCTlc7hzg4T8Nsg==)
10. [plos.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGb9TreF1Htj2mUf9d48do2Bpy2wqU6EW5a8mVK28eRdd7z_YjiK5lm1yCIM7PEgkiu207IrQbyJGQFACy6_Ll-VRK7Ol1SxJt5SzUCXKa-K47u70szh7TDYCZkg6b4dPYVNfD6wRad1FLHD9w1_Jr7g9A-FHVRdvvC4K6ZoWAl)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVab4zw4AE8kLhUUHDSKSrAvzmgZdMnjhvH7Jc6hveTNU9HhELPmUMod0i9S_hCVgyrIpB_EImt7RzQ-AsGMiS-OOF-H68sGz_oneTwPKOkpbb2J3yNiVtDWmK7Q9b9d3BpRFB82UM3BT0sf6f89TIZ8JQoP28nVaGynSJT9zWlTI-Jp4SLbicgiQH3v_lu9z72KNXeazSwSN3POznAkDZ234VNX1P)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9qZfqPCcTtR_y9lAgMDPL7JoBvA2XoMKqRUM1uaolUTvTGWjAY2EsQ5YzsvjfhGk6ms7r9JjStEihRDCQ4TKSb2cMT85c_S3uypmWC307YBMryTZyqUFRPNA7ZSsJekQ2gRCAB_M8z2tMu-ZiZwRf43GJBNQl3gpndAICvwyfstQguYejx8ERbw==)
13. [ijert.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzuPE58aMZlWXeK4tj4Ohw6AN_cKGQlZqkaZ2s4uEaEISRCQzUZ9ZDnnjaoKE-gxdoELursWfgjaI4FR7_y5VXMAphSRjBzgodv_1093aN2vqbkegEWlS7ymCRemeSgHbdbW2DdVkgdtk6BdS3kVP_BKL1In9ZYoP5ViqgJ2vXN6-SoLETC0aSbp5XLFqKSQIrIaWxe2Ut0XC4pQ==)
14. [ijcsit.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6DixvqbVEiCVdL0VM8-2PIqlKkJsXytlNs5BROwTTpzMJ40qSx9xZsl_4_49ozwcbQz64xxJfF5PtIdBShyCPZI1QD1-kjNpeD6KYi8ZVFSJ-1uu_dVO2pn91IVRKMLhNrdB_Gd27NV0_NI6tz1ZYTUb2Cta89rB37VgD3w==)
15. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVOK7zsidcngbJBZIiUTujux8BLp7O0BD8i9W9MhEeL1W_HS4Auz_LrgSsqDJVN6JZgX7K4OvWA1dHSo8kEC2i-5vO4z34ZcsQPymQWdc6XVU6rpNcyPuhg0e8I8M=)
16. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGts3rwJ4ROeO9x3Xcb8wlRJv_cI2zos3sfu7gpOGNh4HQWPV2R1CCpi9yRb4qdNcyHROd9FG77Qh7f5QHkL-4LpxZ9TTIt4yo7WVwkojdb11JSXEH-lrffDkIyTe7d0g==)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHtzgKjHu-nKeNGNnfgRF3U9ckPGp3MeE2FmwubfuVFQk2MH8gStgBjl6vBRvgLWT91-0PXn7tOF0jNP6ppSNAs1wq_DxLSlQ37ji7GRhfeb6ibQb1UAIRcnwxz6jQRSC6J466g984FmJvpAVjPD3y78UghdVp_dQUFQ==)
18. [iw3c2.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrKd88LoDosT-qKbw4z9eEMtLG34gy37hbrI7Fvr9bdL89x4f2uwnTpelWFN4nXtN7yrefMM_7Qg2h0bt1wQFr-GWllWk3RDXzBG-IUTohsuaiDUlRZMD36T6BEmRN56Za8RKheMG52m6CKHE=)


## Annotations
Annotation(end_index=4282, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXgmdXGFo9Yh_5j_gDhwfPdOef8TqHxVEDVADmAyfvMbENvhAkWaP2PYhIvW_XhvNmeTtHYzHnK3GFKLrkGqT1X6YX7e72ER8WNDJ3dgYrloAZsetDFNnQRkmErfx3dkNP_IpaptsXR_ooJ_Jr1QOHy4QHwneEDxMG4Lknh9QlclREpzbavg22MVQKKru91wscP6ZwJ-RH9IY5Z51Ulc69JapQcg==', start_index=4270)
Annotation(end_index=4282, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjDTRIqgZJu44h37ZnUPABHvWuD-OiFSjRVQngLqCE0gSPD_YeCHOlGoXFnlqsW5YCss4mzqBuKxhxIOv7grX58-pST0_l3FMvj3bapctqu2hDWau_2jdgbGtaVHRhFv8USCueShMi6yQFV15oBB1j2HTyef4fXLVJ23Ya5EaY7DuYZovrXVROZ1lGyG7MGr6WM9SjoqjE8ZWFAlnwkR7sXK1uGXkJNlQH4OxyfudfY9TE7TkB9HgsvO7Xi01oAMAkVTyOAZ7y6TU4ADu12pHxhsBl0pX2jZ12SxiYr5QNUhdKcmjjk57sZyIFKQ==', start_index=4270)
Annotation(end_index=4428, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERS2FQb5hahEyXJylfy1dAvhrFh8ObycdwS-9rBZd0z6TYqM3tzIwYQJdkYK6-ePzfUuVHFZu9rUAFUbZnwmmFLOCuDNyVWYGFIY5OrG-2zF9Pj452P9eDlsUii86LAFS3o8c0HvTHaE_-prkXJOoLX3JXYco80HFacrattcT03P74IOiiu49MI4oD0XX5WEs_hZ86n0SUskMCih5bqDn3Q25I451mMxivrc7vLnne5jCkWtjxT3eoCbNm6laUnwDeaOLGWj5QD7Js', start_index=4419)
Annotation(end_index=4548, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMNw-MmTPyoFVdEK2GuXQXcniw-Kz8h33h7yUwIBkpkzmQBNOHkM8633Oo6BN4QzfqByGuu6RTVmR52IP1AMkrgc6uyZXTUhIxolK7gC2aUey7YTgT33hePD5J-Mk=', start_index=4536)
Annotation(end_index=4548, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKk-02J-nONYRjFaJONeCGWKN2ZZ3-t7zNwQp1dFkpE74cGuG2JW80Rct6LMy7rYscM4C8ZBywuyEsoR_JgICIMKrH88TM0FtSOhBnTr_BOsfKOyB-fKxq9iuSS1RnmeZgHySDpaKV6nZlHfxeiyWofEUWH-y5KmVmPgI=', start_index=4536)
Annotation(end_index=5611, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMNw-MmTPyoFVdEK2GuXQXcniw-Kz8h33h7yUwIBkpkzmQBNOHkM8633Oo6BN4QzfqByGuu6RTVmR52IP1AMkrgc6uyZXTUhIxolK7gC2aUey7YTgT33hePD5J-Mk=', start_index=5599)
Annotation(end_index=5611, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjIp_11fo2C6kR0t9mhsq2L2nbAOvsbFPKI1yL0ChetzXyH64f2OhaVZw7mut0m03zo-9Ln09guDw31oIJHyMie5JZizu8W4F7sWQ9Iw9Fj07J35t8BN7-OPW4XD0gkawF3g==', start_index=5599)
Annotation(end_index=5811, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_IhvTkPJBzv3_VGqN1XfMLLQcNecoIk9FTj2YFWkaAjq6FUsBWRre2Vzt8Qwybhg7fwcs4WURrc9C1Pdl8UMSFnH8muaT5rtFwHqecQHrHd4ihP11VVFMyI1Upzhe2ieXIe_EuS_18NrPuqWVEjYxMNFnHeh3l8DBVMnh_nQlPzPD6nn2janFuLycwJr3nARNGg83KU9rg9VKP6Tvff63Nm5BVjaZHxCUiodgP_amgVcOtXu2', start_index=5802)
Annotation(end_index=6306, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKk-02J-nONYRjFaJONeCGWKN2ZZ3-t7zNwQp1dFkpE74cGuG2JW80Rct6LMy7rYscM4C8ZBywuyEsoR_JgICIMKrH88TM0FtSOhBnTr_BOsfKOyB-fKxq9iuSS1RnmeZgHySDpaKV6nZlHfxeiyWofEUWH-y5KmVmPgI=', start_index=6297)
Annotation(end_index=7434, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKk-02J-nONYRjFaJONeCGWKN2ZZ3-t7zNwQp1dFkpE74cGuG2JW80Rct6LMy7rYscM4C8ZBywuyEsoR_JgICIMKrH88TM0FtSOhBnTr_BOsfKOyB-fKxq9iuSS1RnmeZgHySDpaKV6nZlHfxeiyWofEUWH-y5KmVmPgI=', start_index=7425)
Annotation(end_index=8135, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxNiZUss7cC5BQnjluYEGiYCtV-xMkDxrm5NHln6L4sEFDM4K1JkWe5ZQf0tGKSYQOVdEGOHjAy2mgkAz5jAuKEAwgXnnqI0mj2Pe_oudXJ-BQ8u4DubvcTvWCVAl94G9aGuDCbnAsDuaPp58E5sba9nAZ9BTHQvU3lqEG0NhpD90Kyjxj6MSXZ0v5ueP_h2LL', start_index=8126)
Annotation(end_index=9429, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGb9TreF1Htj2mUf9d48do2Bpy2wqU6EW5a8mVK28eRdd7z_YjiK5lm1yCIM7PEgkiu207IrQbyJGQFACy6_Ll-VRK7Ol1SxJt5SzUCXKa-K47u70szh7TDYCZkg6b4dPYVNfD6wRad1FLHD9w1_Jr7g9A-FHVRdvvC4K6ZoWAl', start_index=9416)
Annotation(end_index=9429, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7aF4JlZarTbMkNigd5RvD9v7PeeIntEeJfpoh86x-KH6dV2aUav5Jz8cWOK01jJ9nEa-hn4t0F7ORAkMlSJrhoEJsCSpvPHRRBgbDTONhOu3eqf0YNeKfI3TDTonHCTlc7hzg4T8Nsg==', start_index=9416)
Annotation(end_index=9906, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVab4zw4AE8kLhUUHDSKSrAvzmgZdMnjhvH7Jc6hveTNU9HhELPmUMod0i9S_hCVgyrIpB_EImt7RzQ-AsGMiS-OOF-H68sGz_oneTwPKOkpbb2J3yNiVtDWmK7Q9b9d3BpRFB82UM3BT0sf6f89TIZ8JQoP28nVaGynSJT9zWlTI-Jp4SLbicgiQH3v_lu9z72KNXeazSwSN3POznAkDZ234VNX1P', start_index=9892)
Annotation(end_index=9906, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGb9TreF1Htj2mUf9d48do2Bpy2wqU6EW5a8mVK28eRdd7z_YjiK5lm1yCIM7PEgkiu207IrQbyJGQFACy6_Ll-VRK7Ol1SxJt5SzUCXKa-K47u70szh7TDYCZkg6b4dPYVNfD6wRad1FLHD9w1_Jr7g9A-FHVRdvvC4K6ZoWAl', start_index=9892)
Annotation(end_index=10383, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGb9TreF1Htj2mUf9d48do2Bpy2wqU6EW5a8mVK28eRdd7z_YjiK5lm1yCIM7PEgkiu207IrQbyJGQFACy6_Ll-VRK7Ol1SxJt5SzUCXKa-K47u70szh7TDYCZkg6b4dPYVNfD6wRad1FLHD9w1_Jr7g9A-FHVRdvvC4K6ZoWAl', start_index=10370)
Annotation(end_index=10383, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7aF4JlZarTbMkNigd5RvD9v7PeeIntEeJfpoh86x-KH6dV2aUav5Jz8cWOK01jJ9nEa-hn4t0F7ORAkMlSJrhoEJsCSpvPHRRBgbDTONhOu3eqf0YNeKfI3TDTonHCTlc7hzg4T8Nsg==', start_index=10370)
Annotation(end_index=10865, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9qZfqPCcTtR_y9lAgMDPL7JoBvA2XoMKqRUM1uaolUTvTGWjAY2EsQ5YzsvjfhGk6ms7r9JjStEihRDCQ4TKSb2cMT85c_S3uypmWC307YBMryTZyqUFRPNA7ZSsJekQ2gRCAB_M8z2tMu-ZiZwRf43GJBNQl3gpndAICvwyfstQguYejx8ERbw==', start_index=10851)
Annotation(end_index=10865, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVab4zw4AE8kLhUUHDSKSrAvzmgZdMnjhvH7Jc6hveTNU9HhELPmUMod0i9S_hCVgyrIpB_EImt7RzQ-AsGMiS-OOF-H68sGz_oneTwPKOkpbb2J3yNiVtDWmK7Q9b9d3BpRFB82UM3BT0sf6f89TIZ8JQoP28nVaGynSJT9zWlTI-Jp4SLbicgiQH3v_lu9z72KNXeazSwSN3POznAkDZ234VNX1P', start_index=10851)
Annotation(end_index=11448, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERS2FQb5hahEyXJylfy1dAvhrFh8ObycdwS-9rBZd0z6TYqM3tzIwYQJdkYK6-ePzfUuVHFZu9rUAFUbZnwmmFLOCuDNyVWYGFIY5OrG-2zF9Pj452P9eDlsUii86LAFS3o8c0HvTHaE_-prkXJOoLX3JXYco80HFacrattcT03P74IOiiu49MI4oD0XX5WEs_hZ86n0SUskMCih5bqDn3Q25I451mMxivrc7vLnne5jCkWtjxT3eoCbNm6laUnwDeaOLGWj5QD7Js', start_index=11435)
Annotation(end_index=11448, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzuPE58aMZlWXeK4tj4Ohw6AN_cKGQlZqkaZ2s4uEaEISRCQzUZ9ZDnnjaoKE-gxdoELursWfgjaI4FR7_y5VXMAphSRjBzgodv_1093aN2vqbkegEWlS7ymCRemeSgHbdbW2DdVkgdtk6BdS3kVP_BKL1In9ZYoP5ViqgJ2vXN6-SoLETC0aSbp5XLFqKSQIrIaWxe2Ut0XC4pQ==', start_index=11435)
Annotation(end_index=12104, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6DixvqbVEiCVdL0VM8-2PIqlKkJsXytlNs5BROwTTpzMJ40qSx9xZsl_4_49ozwcbQz64xxJfF5PtIdBShyCPZI1QD1-kjNpeD6KYi8ZVFSJ-1uu_dVO2pn91IVRKMLhNrdB_Gd27NV0_NI6tz1ZYTUb2Cta89rB37VgD3w==', start_index=12094)
Annotation(end_index=12551, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERS2FQb5hahEyXJylfy1dAvhrFh8ObycdwS-9rBZd0z6TYqM3tzIwYQJdkYK6-ePzfUuVHFZu9rUAFUbZnwmmFLOCuDNyVWYGFIY5OrG-2zF9Pj452P9eDlsUii86LAFS3o8c0HvTHaE_-prkXJOoLX3JXYco80HFacrattcT03P74IOiiu49MI4oD0XX5WEs_hZ86n0SUskMCih5bqDn3Q25I451mMxivrc7vLnne5jCkWtjxT3eoCbNm6laUnwDeaOLGWj5QD7Js', start_index=12542)
Annotation(end_index=13218, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXgmdXGFo9Yh_5j_gDhwfPdOef8TqHxVEDVADmAyfvMbENvhAkWaP2PYhIvW_XhvNmeTtHYzHnK3GFKLrkGqT1X6YX7e72ER8WNDJ3dgYrloAZsetDFNnQRkmErfx3dkNP_IpaptsXR_ooJ_Jr1QOHy4QHwneEDxMG4Lknh9QlclREpzbavg22MVQKKru91wscP6ZwJ-RH9IY5Z51Ulc69JapQcg==', start_index=13206)
Annotation(end_index=13218, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjDTRIqgZJu44h37ZnUPABHvWuD-OiFSjRVQngLqCE0gSPD_YeCHOlGoXFnlqsW5YCss4mzqBuKxhxIOv7grX58-pST0_l3FMvj3bapctqu2hDWau_2jdgbGtaVHRhFv8USCueShMi6yQFV15oBB1j2HTyef4fXLVJ23Ya5EaY7DuYZovrXVROZ1lGyG7MGr6WM9SjoqjE8ZWFAlnwkR7sXK1uGXkJNlQH4OxyfudfY9TE7TkB9HgsvO7Xi01oAMAkVTyOAZ7y6TU4ADu12pHxhsBl0pX2jZ12SxiYr5QNUhdKcmjjk57sZyIFKQ==', start_index=13206)
Annotation(end_index=13510, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVOK7zsidcngbJBZIiUTujux8BLp7O0BD8i9W9MhEeL1W_HS4Auz_LrgSsqDJVN6JZgX7K4OvWA1dHSo8kEC2i-5vO4z34ZcsQPymQWdc6XVU6rpNcyPuhg0e8I8M=', start_index=13500)
Annotation(end_index=13672, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjDTRIqgZJu44h37ZnUPABHvWuD-OiFSjRVQngLqCE0gSPD_YeCHOlGoXFnlqsW5YCss4mzqBuKxhxIOv7grX58-pST0_l3FMvj3bapctqu2hDWau_2jdgbGtaVHRhFv8USCueShMi6yQFV15oBB1j2HTyef4fXLVJ23Ya5EaY7DuYZovrXVROZ1lGyG7MGr6WM9SjoqjE8ZWFAlnwkR7sXK1uGXkJNlQH4OxyfudfY9TE7TkB9HgsvO7Xi01oAMAkVTyOAZ7y6TU4ADu12pHxhsBl0pX2jZ12SxiYr5QNUhdKcmjjk57sZyIFKQ==', start_index=13659)
Annotation(end_index=13672, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGts3rwJ4ROeO9x3Xcb8wlRJv_cI2zos3sfu7gpOGNh4HQWPV2R1CCpi9yRb4qdNcyHROd9FG77Qh7f5QHkL-4LpxZ9TTIt4yo7WVwkojdb11JSXEH-lrffDkIyTe7d0g==', start_index=13659)
Annotation(end_index=14718, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHtzgKjHu-nKeNGNnfgRF3U9ckPGp3MeE2FmwubfuVFQk2MH8gStgBjl6vBRvgLWT91-0PXn7tOF0jNP6ppSNAs1wq_DxLSlQ37ji7GRhfeb6ibQb1UAIRcnwxz6jQRSC6J466g984FmJvpAVjPD3y78UghdVp_dQUFQ==', start_index=14708)
Annotation(end_index=15151, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHtzgKjHu-nKeNGNnfgRF3U9ckPGp3MeE2FmwubfuVFQk2MH8gStgBjl6vBRvgLWT91-0PXn7tOF0jNP6ppSNAs1wq_DxLSlQ37ji7GRhfeb6ibQb1UAIRcnwxz6jQRSC6J466g984FmJvpAVjPD3y78UghdVp_dQUFQ==', start_index=15141)
Annotation(end_index=16952, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrKd88LoDosT-qKbw4z9eEMtLG34gy37hbrI7Fvr9bdL89x4f2uwnTpelWFN4nXtN7yrefMM_7Qg2h0bt1wQFr-GWllWk3RDXzBG-IUTohsuaiDUlRZMD36T6BEmRN56Za8RKheMG52m6CKHE=', start_index=16942)
Annotation(end_index=17243, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKk-02J-nONYRjFaJONeCGWKN2ZZ3-t7zNwQp1dFkpE74cGuG2JW80Rct6LMy7rYscM4C8ZBywuyEsoR_JgICIMKrH88TM0FtSOhBnTr_BOsfKOyB-fKxq9iuSS1RnmeZgHySDpaKV6nZlHfxeiyWofEUWH-y5KmVmPgI=', start_index=17234)
Annotation(end_index=18344, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHtzgKjHu-nKeNGNnfgRF3U9ckPGp3MeE2FmwubfuVFQk2MH8gStgBjl6vBRvgLWT91-0PXn7tOF0jNP6ppSNAs1wq_DxLSlQ37ji7GRhfeb6ibQb1UAIRcnwxz6jQRSC6J466g984FmJvpAVjPD3y78UghdVp_dQUFQ==', start_index=18334)
Annotation(end_index=18458, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERS2FQb5hahEyXJylfy1dAvhrFh8ObycdwS-9rBZd0z6TYqM3tzIwYQJdkYK6-ePzfUuVHFZu9rUAFUbZnwmmFLOCuDNyVWYGFIY5OrG-2zF9Pj452P9eDlsUii86LAFS3o8c0HvTHaE_-prkXJOoLX3JXYco80HFacrattcT03P74IOiiu49MI4oD0XX5WEs_hZ86n0SUskMCih5bqDn3Q25I451mMxivrc7vLnne5jCkWtjxT3eoCbNm6laUnwDeaOLGWj5QD7Js', start_index=18449)
Annotation(end_index=18568, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjDTRIqgZJu44h37ZnUPABHvWuD-OiFSjRVQngLqCE0gSPD_YeCHOlGoXFnlqsW5YCss4mzqBuKxhxIOv7grX58-pST0_l3FMvj3bapctqu2hDWau_2jdgbGtaVHRhFv8USCueShMi6yQFV15oBB1j2HTyef4fXLVJ23Ya5EaY7DuYZovrXVROZ1lGyG7MGr6WM9SjoqjE8ZWFAlnwkR7sXK1uGXkJNlQH4OxyfudfY9TE7TkB9HgsvO7Xi01oAMAkVTyOAZ7y6TU4ADu12pHxhsBl0pX2jZ12SxiYr5QNUhdKcmjjk57sZyIFKQ==', start_index=18559)
Annotation(end_index=18673, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXgmdXGFo9Yh_5j_gDhwfPdOef8TqHxVEDVADmAyfvMbENvhAkWaP2PYhIvW_XhvNmeTtHYzHnK3GFKLrkGqT1X6YX7e72ER8WNDJ3dgYrloAZsetDFNnQRkmErfx3dkNP_IpaptsXR_ooJ_Jr1QOHy4QHwneEDxMG4Lknh9QlclREpzbavg22MVQKKru91wscP6ZwJ-RH9IY5Z51Ulc69JapQcg==', start_index=18664)
Annotation(end_index=18746, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7aF4JlZarTbMkNigd5RvD9v7PeeIntEeJfpoh86x-KH6dV2aUav5Jz8cWOK01jJ9nEa-hn4t0F7ORAkMlSJrhoEJsCSpvPHRRBgbDTONhOu3eqf0YNeKfI3TDTonHCTlc7hzg4T8Nsg==', start_index=18737)
Annotation(end_index=18798, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVab4zw4AE8kLhUUHDSKSrAvzmgZdMnjhvH7Jc6hveTNU9HhELPmUMod0i9S_hCVgyrIpB_EImt7RzQ-AsGMiS-OOF-H68sGz_oneTwPKOkpbb2J3yNiVtDWmK7Q9b9d3BpRFB82UM3BT0sf6f89TIZ8JQoP28nVaGynSJT9zWlTI-Jp4SLbicgiQH3v_lu9z72KNXeazSwSN3POznAkDZ234VNX1P', start_index=18788)
Annotation(end_index=18874, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxNiZUss7cC5BQnjluYEGiYCtV-xMkDxrm5NHln6L4sEFDM4K1JkWe5ZQf0tGKSYQOVdEGOHjAy2mgkAz5jAuKEAwgXnnqI0mj2Pe_oudXJ-BQ8u4DubvcTvWCVAl94G9aGuDCbnAsDuaPp58E5sba9nAZ9BTHQvU3lqEG0NhpD90Kyjxj6MSXZ0v5ueP_h2LL', start_index=18865)
Annotation(end_index=18939, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKk-02J-nONYRjFaJONeCGWKN2ZZ3-t7zNwQp1dFkpE74cGuG2JW80Rct6LMy7rYscM4C8ZBywuyEsoR_JgICIMKrH88TM0FtSOhBnTr_BOsfKOyB-fKxq9iuSS1RnmeZgHySDpaKV6nZlHfxeiyWofEUWH-y5KmVmPgI=', start_index=18930)
Annotation(end_index=19026, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVOK7zsidcngbJBZIiUTujux8BLp7O0BD8i9W9MhEeL1W_HS4Auz_LrgSsqDJVN6JZgX7K4OvWA1dHSo8kEC2i-5vO4z34ZcsQPymQWdc6XVU6rpNcyPuhg0e8I8M=', start_index=19016)
Annotation(end_index=19110, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGb9TreF1Htj2mUf9d48do2Bpy2wqU6EW5a8mVK28eRdd7z_YjiK5lm1yCIM7PEgkiu207IrQbyJGQFACy6_Ll-VRK7Ol1SxJt5SzUCXKa-K47u70szh7TDYCZkg6b4dPYVNfD6wRad1FLHD9w1_Jr7g9A-FHVRdvvC4K6ZoWAl', start_index=19100)
Annotation(end_index=19189, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERS2FQb5hahEyXJylfy1dAvhrFh8ObycdwS-9rBZd0z6TYqM3tzIwYQJdkYK6-ePzfUuVHFZu9rUAFUbZnwmmFLOCuDNyVWYGFIY5OrG-2zF9Pj452P9eDlsUii86LAFS3o8c0HvTHaE_-prkXJOoLX3JXYco80HFacrattcT03P74IOiiu49MI4oD0XX5WEs_hZ86n0SUskMCih5bqDn3Q25I451mMxivrc7vLnne5jCkWtjxT3eoCbNm6laUnwDeaOLGWj5QD7Js', start_index=19180)
Annotation(end_index=19249, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzuPE58aMZlWXeK4tj4Ohw6AN_cKGQlZqkaZ2s4uEaEISRCQzUZ9ZDnnjaoKE-gxdoELursWfgjaI4FR7_y5VXMAphSRjBzgodv_1093aN2vqbkegEWlS7ymCRemeSgHbdbW2DdVkgdtk6BdS3kVP_BKL1In9ZYoP5ViqgJ2vXN6-SoLETC0aSbp5XLFqKSQIrIaWxe2Ut0XC4pQ==', start_index=19239)
Annotation(end_index=19340, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6DixvqbVEiCVdL0VM8-2PIqlKkJsXytlNs5BROwTTpzMJ40qSx9xZsl_4_49ozwcbQz64xxJfF5PtIdBShyCPZI1QD1-kjNpeD6KYi8ZVFSJ-1uu_dVO2pn91IVRKMLhNrdB_Gd27NV0_NI6tz1ZYTUb2Cta89rB37VgD3w==', start_index=19330)
Annotation(end_index=19390, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrKd88LoDosT-qKbw4z9eEMtLG34gy37hbrI7Fvr9bdL89x4f2uwnTpelWFN4nXtN7yrefMM_7Qg2h0bt1wQFr-GWllWk3RDXzBG-IUTohsuaiDUlRZMD36T6BEmRN56Za8RKheMG52m6CKHE=', start_index=19380)
Annotation(end_index=19465, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjIp_11fo2C6kR0t9mhsq2L2nbAOvsbFPKI1yL0ChetzXyH64f2OhaVZw7mut0m03zo-9Ln09guDw31oIJHyMie5JZizu8W4F7sWQ9Iw9Fj07J35t8BN7-OPW4XD0gkawF3g==', start_index=19456)
Annotation(end_index=19531, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKk-02J-nONYRjFaJONeCGWKN2ZZ3-t7zNwQp1dFkpE74cGuG2JW80Rct6LMy7rYscM4C8ZBywuyEsoR_JgICIMKrH88TM0FtSOhBnTr_BOsfKOyB-fKxq9iuSS1RnmeZgHySDpaKV6nZlHfxeiyWofEUWH-y5KmVmPgI=', start_index=19522)
Annotation(end_index=19567, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMNw-MmTPyoFVdEK2GuXQXcniw-Kz8h33h7yUwIBkpkzmQBNOHkM8633Oo6BN4QzfqByGuu6RTVmR52IP1AMkrgc6uyZXTUhIxolK7gC2aUey7YTgT33hePD5J-Mk=', start_index=19558)

## Sources
