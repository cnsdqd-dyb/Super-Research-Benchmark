# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** a5edc420 | **Time:** 457.41s | **Cost:** $1.70248
--------------------------------------------------------------------------------

# Determinants of the Temporal Discount Function in Review and Reputation Systems

### Key Points
*   **Volatility of the Underlying Quality:** The primary determinant of the temporal discount function is the rate at which the "true" quality of the item changes. Dynamic products (e.g., software, restaurants) require steeper decay functions (faster obsolescence of old ratings) than static products (e.g., books, movies) to maintain accuracy [cite: 1, 2].
*   **Effective Sample Size ($N_{eff}$) Constraints:** Discounting reduces the effective number of data points available for aggregation. Systems must balance the need for recency (responsiveness) with the need for statistical significance (stability). High decay rates in sparse data environments lead to volatile, unreliable ratings [cite: 3, 4].
*   **Responsiveness vs. Stability Trade-off:** The decay factor ($\lambda$) is optimized to minimize prediction error (RMSE). A lower $\lambda$ (faster decay) improves responsiveness to recent changes (e.g., a bad software update) but increases noise; a higher $\lambda$ (slower decay) ensures stability but results in lag [cite: 3, 5].
*   **Platform-Specific Objectives:** Different platforms employ distinct functions based on their ecosystem. Amazon uses machine-learned models that weigh recency alongside reviewer credibility and verified status [cite: 6, 7]. Steam utilizes a bifurcated approach, displaying a 30-day "Recent" score alongside an "All-time" score to highlight short-term performance shifts [cite: 2].
*   **Psychological and Behavioral Alignment:** Discount functions are often calibrated to match user heuristics. Users exhibit "recency bias," trusting newer reviews significantly more. Algorithms that fail to discount old data risk presenting a "reputation lag" that frustrates users who encounter a product that no longer matches its historical rating [cite: 8, 9].

### Introduction to Temporal Dynamics in Rating Aggregation
The temporal discount function in review systems serves as the mathematical mechanism that governs the obsolescence of information. In any reputation system—whether for e-commerce products, service providers, or digital content—a rating contributed at time $t$ does not necessarily hold the same predictive value at time $t+n$. The determination of *how* that value decays is a complex optimization problem involving statistical validity, system responsiveness, and human psychology.

At its core, the discount function addresses the "stationarity" of the attribute being measured. If a product's quality is invariant (stationary), all ratings regardless of age should theoretically carry equal weight to maximize the sample size. However, most real-world entities are non-stationary; software is patched, manufacturing batches change, and service quality fluctuates. Consequently, review systems must implement weighting mechanisms—typically exponential or window-based—to prioritize recent signals while retaining enough historical data to ensure the rating is statistically robust.

### The Tension Between Information Aging and Accumulation
The fundamental challenge in determining the temporal discount function is the trade-off between **information aging** and **information accumulation**. As data ages, its relevance typically declines due to changes in the item itself or the context of its use. Conversely, accumulating data reduces the standard error of the estimated rating. A discount function that is too aggressive (steep decay) renders the rating susceptible to manipulation and short-term variance (noise). A function that is too conservative (flat or no decay) creates "reputation inertia," where an item rests on its past laurels despite current deterioration [cite: 1, 3].

---

## 1. Theoretical Frameworks of Temporal Discounting

To understand what determines the discount function, one must first establish the mathematical forms these functions take in review and reputation systems. The choice of function dictates the system's sensitivity to time.

### 1.1 Exponential Decay (EWMA)
The most prevalent model in both financial risk management and dynamic reputation systems is Exponentially Weighted Moving Average (EWMA). In this model, the weight of a rating decays exponentially as time passes. The weight $w_t$ for a rating with age $t$ is often expressed as:

\[ w_t = \lambda (1 - \lambda)^t \]

Or recursively for variance/rating estimation:
\[ \sigma_t^2 = \lambda \sigma_{t-1}^2 + (1-\lambda) r_t^2 \]

Here, $\lambda$ (lambda) is the **decay factor** (or smoothing constant).
*   **High $\lambda$ (e.g., 0.99):** Slow decay, long memory, high stability.
*   **Low $\lambda$ (e.g., 0.80):** Fast decay, short memory, high responsiveness.

Research in financial volatility (which parallels rating volatility) suggests that the optimal $\lambda$ depends on the horizon of the forecast. For example, RiskMetrics recommends $\lambda = 0.94$ for daily data and $\lambda = 0.97$ for monthly data [cite: 10, 11]. In review systems, this parameter is tuned based on the expected frequency of product updates or service changes.

### 1.2 Hyperbolic Discounting
While exponential decay is computationally convenient, human psychology often follows a **hyperbolic discount function**, where value drops sharply in the immediate short term and then levels off.
\[ V = \frac{A}{1 + kD} \]
Where $V$ is subjective value, $A$ is amount, $D$ is delay, and $k$ is the discounting parameter [cite: 12, 13].
In review systems, this might manifest as a system that heavily weights reviews from the last week, but treats a review from 6 months ago and 12 months ago relatively similarly (both being "old"), whereas an exponential model would continue to distinguish significantly between them. Some research suggests hyperbolic decay fits "mechanical" factors (like momentum in stock or viral trends) better than exponential models [cite: 14].

### 1.3 Step-Wise and Windowed Functions
Some systems eschew continuous decay for discrete windows.
*   **Sliding Window:** Ratings inside the window (e.g., last 30 days) have weight $w=1$; ratings outside have weight $w=0$.
*   **Bifurcated Scoring:** Steam displays two scores: "Recent" (last 30 days) and "All Reviews" (lifetime). This effectively allows the user to apply their own weighting preference [cite: 2].

---

## 2. Determinants of the Decay Function

The specific shape and parameters of the discount function are determined by a confluence of statistical, environmental, and strategic factors.

### 2.1 Volatility of the Underlying Entity
The most critical determinant is the **volatility** (or stationarity) of the quality being measured.
*   **High Volatility (Dynamic Products):** Items that change frequently require a steeper discount function (lower half-life).
    *   *Software/Games:* A video game might launch in a broken state (negative ratings) but be fixed via patches (positive ratings). A system that does not discount the launch ratings fails to represent the current product. Steam’s introduction of "Recent Review Scores" was explicitly driven by the need to accommodate games changing over time (Early Access, patches) [cite: 2].
    *   *Service Industry:* Restaurants and hotels experience staff turnover. A 5-star rating from three years ago is less predictive of a meal today than a 5-star rating from yesterday.
*   **Low Volatility (Static Products):** Items that remain unchanged allow for slower discounting.
    *   *Media:* A book or a movie does not change content after release. While social context might shift, the artifact is static. Amazon’s algorithm still weights recent reviews higher, but the necessity is less acute than for software [cite: 6, 15].

Research indicates that when the "true" quality is unstable, the optimal decay factor $\lambda$ must be lower (faster decay) to minimize the Mean Squared Error (MSE) of the prediction. Conversely, stable quality allows for a $\lambda$ closer to 1, maximizing the effective sample size [cite: 3, 11].

### 2.2 Effective Sample Size ($N_{eff}$) and Sparsity
A major constraint on temporal discounting is the volume of data. Aggressive discounting reduces the **Effective Sample Size ($N_{eff}$)**.
\[ N_{eff} \approx \frac{1}{\sum w_i^2} \]
If a product has few reviews, applying a steep time decay renders the aggregate score statistically insignificant, making it susceptible to outliers (e.g., a single recent 1-star review tanking the score of a generally good product) [cite: 4, 16].
*   **Sparse Data:** Systems often revert to simple averages or very slow decay for items with few ratings to maintain stability.
*   **Dense Data:** Popular items with thousands of reviews allow the system to aggressively discount old data without sacrificing statistical confidence. Amazon’s system, for instance, requires a certain volume before its machine-learning weighting fully kicks in; otherwise, it may look closer to a simple average [cite: 6, 7].

### 2.3 Reviewer Credibility and Trust
The discount function is often intertwined with credibility metrics. A rating's weight is not solely a function of time ($t$) but also of the rater's reliability ($R$).
\[ Weight = f(t) \times g(R) \]
*   **Verified Purchases:** Amazon weights verified purchases higher. Over time, an older verified review might retain more weight than a newer unverified review, creating a complex, non-linear decay surface [cite: 6, 7].
*   **Reviewer History:** Users with a history of helpful reviews may have their contributions decay slower than low-credibility users. This helps mitigate "review bombing" where new, low-credibility accounts flood a system [cite: 1].

### 2.4 Strategic Platform Objectives
Platforms tune their discount functions to drive specific user behaviors:
*   **Encouraging Fresh Content:** By heavily weighting recent reviews, platforms like Yelp or Amazon incentivize users to write new reviews and sellers to solicit them. If old reviews remained dominant, there would be little incentive to generate new feedback for established products [cite: 6, 9].
*   **Mitigating "Cold Start" vs. "Established" Bias:** New products need to build reputation quickly (requiring high responsiveness), while established products need protection from flash mobs (requiring stability). Some systems use adaptive $\lambda$ values that change based on the product's lifecycle stage [cite: 16, 17].

---

## 3. Mathematical Models and Algorithmic Implementations

The implementation of temporal discounting varies from simple heuristics to complex machine learning models.

### 3.1 The Exponentially Weighted Moving Average (EWMA) in Depth
In financial and reputation systems, EWMA is favored for its recursive property—it does not require storing the entire history of ratings, only the current aggregate and the new rating.

**The Recursive Update:**
\[ R_t = \lambda R_{t-1} + (1 - \lambda) r_t \]
Where:
*   $R_t$ is the new aggregate rating.
*   $R_{t-1}$ is the previous aggregate.
*   $r_t$ is the new incoming rating.
*   $\lambda$ is the decay factor (0 < $\lambda$ < 1).

**Determining $\lambda$:**
Research in volatility modeling (e.g., GARCH, RiskMetrics) suggests that $\lambda$ should be chosen to minimize the root mean square error (RMSE) of future predictions.
*   **Standard Values:** In finance, $\lambda=0.94$ is standard for daily volatility. In review systems, this might be adjusted to $\lambda=0.99$ for daily updates to prevent a single day's reviews from swinging the score too wildly [cite: 5, 10].
*   **Adaptive $\lambda$:** Advanced systems use a dynamic $\lambda$ that decreases (faster decay) when a "shock" or structural break is detected (e.g., a sudden surge in review volume indicating a product update or controversy) and increases (slower decay) during stable periods [cite: 16, 17].

### 3.2 Logistic and Sigmoid Weighting
Some researchers propose logistic functions to model relevance. This assigns a weight of ~1 to recent reviews and drops smoothly to ~0 for reviews older than a specific threshold (e.g., 1 year).
\[ w(t) = \frac{1}{1 + e^{k(t - t_0)}} \]
This models the "shelf-life" of a review more naturally than exponential decay, which theoretically never reaches zero. This approach is useful for systems that want to completely phase out very old data (e.g., reviews for a previous version of an app) [cite: 18].

### 3.3 The "Machine Learned" Approach (Amazon)
Amazon has moved away from transparent deterministic formulas (like simple averages) to "machine-learned models."
*   **Inputs:** Recency, Verified Purchase status, Helpfulness votes, Reviewer propensity for outliers.
*   **Mechanism:** The model likely trains on sales conversion data. It asks: "Which combination of review weights best predicts a customer's likelihood to buy and be satisfied?"
*   **Time Decay:** While not a simple formula, the system exhibits behavior where "newer reviews hold more weight." However, this is conditional; a 2-year-old "most helpful" review might still outrank a 1-day-old generic review [cite: 6, 7].

---

## 4. Case Studies: Industry Implementations

### 4.1 Amazon: The Black Box of Relevance
Amazon explicitly states: *"Amazon calculates a product's star rating using machine-learned models instead of a simple average... These models consider factors such as how recent the rating or review is and verified purchase status."* [cite: 7].
*   **Observation:** A product can have a 4.5-star average but a displayed rating of 4.2 if recent reviews are negative.
*   **Determinant:** The primary determinant here is **conversion optimization**. Amazon's algorithm is likely tuned to maximize the predictive accuracy of the rating regarding the *current* customer experience, thereby reducing returns and increasing trust [cite: 6, 19].

### 4.2 Steam: The Bifurcated Solution
Steam (Valve) addresses the volatility of video games (patches, DLC, review bombs) by separating the temporal signals.
*   **Overall Score:** All reviews since launch.
*   **Recent Score:** Reviews from the last 30 days.
*   **Determinant:** **Product Evolution.** Games change drastically. A "Mixed" overall score but "Overwhelmingly Positive" recent score signals to the user that the developers have fixed the game. This puts the burden of temporal discounting on the user's cognitive processing rather than the algorithm [cite: 2, 20].
*   **Anti-Gaming:** Steam also identifies "off-topic review activity" (review bombs) and excludes them from the score, effectively applying a time-and-context-based filter (a weight of 0 for specific periods) [cite: 20, 21].

### 4.3 Financial Risk Models (RiskMetrics)
While not a consumer review system, financial risk models provide the mathematical foundation for volatility-based discounting.
*   **Method:** EWMA with $\lambda = 0.94$.
*   **Determinant:** **Market Memory.** The value 0.94 was empirically determined to balance the "memory" of past volatility with the need to react to new market shocks. This parallels how reputation systems must balance "reputation history" with "current behavior" [cite: 10, 11].

### 4.4 Competitive Gaming (Elo/Glicko)
Rating systems for players (e.g., Chess, League of Legends) use temporal discounting to model **uncertainty**.
*   **Glicko System:** Introduces a "Ratings Deviation" (RD) that increases over time when a player is inactive.
*   **Mechanism:** $RD_{new} = \sqrt{RD_{old}^2 + c^2 t}$. As time $t$ passes without play, uncertainty grows.
*   **Effect:** When the player returns, their rating changes more drastically (high responsiveness) because the system has "discounted" the certainty of their old rating.
*   **Determinant:** **Skill Atrophy.** The assumption is that skill is not static; inactivity leads to a decay in the *confidence* of the rating, if not the rating itself [cite: 22].

---

## 5. Psychological Factors in Temporal Discounting

The design of these algorithms is heavily influenced by how human users perceive time and value.

### 5.1 Recency Bias and Trust
Surveys indicate that 77% of shoppers consider reviews older than 3 months to be irrelevant [cite: 9].
*   **Determinant:** **Perceived Diagnosticity.** Users view recent information as more diagnostic of the current state of the product. If an algorithm displays a 5-star rating based on 2-year-old data, but the recent reviews are 1-star, the user feels deceived. The algorithm must discount old ratings to align with the user's *expectation* of relevance [cite: 8, 23].

### 5.2 Hyperbolic Discounting in User Behavior
Behavioral economics shows that humans discount future (and past) value hyperbolically.
*   **Implication:** Users care intensely about the "now" and the "very recent." The difference in value between a review from yesterday and last week is perceived as greater than the difference between a review from 6 months ago and 7 months ago.
*   **System Response:** Systems like Steam and Amazon prioritize the display of "Recent" reviews and weight them heavily in the aggregate score to match this psychological preference [cite: 12, 24].

---

## 6. Optimization and Calibration of the Discount Function

How do system designers choose the specific decay rate ($\lambda$)?

### 6.1 Minimizing Prediction Error (RMSE)
The objective function for calibrating $\lambda$ is often to minimize the error between the *predicted* rating and the *actual* future rating (or user satisfaction).
\[ \min_{\lambda} \sum (R_{t+1} - \hat{R}_{t+1}(\lambda))^2 \]
*   **Process:** Designers run historical simulations. They calculate what the rating *would have been* at time $t$ using various $\lambda$ values and compare it to the actual ratings received at $t+1$.
*   **Result:** If the product category is volatile (e.g., fashion trends), the optimal $\lambda$ will be lower (faster decay). If stable (e.g., hardware tools), $\lambda$ will be higher [cite: 3, 5].

### 6.2 Adaptive Temporal Discounting
Advanced systems do not use a fixed $\lambda$. Instead, they use **Adaptive Temporal Discounting**.
*   **Mechanism:** The system monitors the "volatility" of the incoming ratings.
    *   *Low Volatility:* Ratings are consistent. $\lambda$ increases (slow decay) to build sample size and precision.
    *   *High Volatility:* A sudden spike in variance (e.g., mixed 1-star and 5-star reviews). $\lambda$ decreases (fast decay) to allow the score to shift rapidly to the new equilibrium.
*   **Benefit:** This solves the trade-off between stability and responsiveness dynamically [cite: 16, 17, 25].

### 6.3 The "Half-Life" Concept
The decay can be conceptualized as a half-life:
\[ \tau = \frac{\ln(0.5)}{\ln(1-\lambda)} \]
This metric helps designers communicate the system's behavior. For example, "This rating system has a half-life of 30 days," meaning a review's weight drops by 50% every 30 days. This is a crucial design parameter determined by the product cycle length [cite: 10].

---

## 7. Challenges and Limitations

### 7.1 The Cold Start Problem
When a new product launches, it has no history. Temporal discounting is irrelevant until a history exists. However, for *re-emerging* products (e.g., a product out of stock for a year), strict time decay might reset their rating to zero/neutral. Systems must decide whether to "freeze" ratings during inactivity or let them decay. Glicko handles this by increasing uncertainty, not necessarily lowering the rating [cite: 22].

### 7.2 Review Bombing and Anomalies
Temporal discounting can exacerbate review bombing. If a system is highly responsive (fast decay), a coordinated attack of negative reviews can instantly destroy a reputation.
*   **Counter-measure:** Systems detect "abnormal" volume and may temporarily *suspend* the time decay or exclude the anomaly period entirely (as Steam does) [cite: 20].

### 7.3 Data Sparsity and Noise
In long-tail products with few reviews, time decay can be destructive. If a product gets one review a year, and the system decays weights by 50% every month, the product effectively never has a rating.
*   **Solution:** Decay functions are often triggered by *events* (new reviews) rather than just wall-clock time, or they are weighted by the *volume* of recent data (Effective Sample Size maintenance) [cite: 4, 26].

---

## Conclusion

The temporal discount function in review systems is not a static variable but a dynamic parameter determined by the **volatility of the item**, the **volume of data**, and **user psychology**.

1.  **Volatility:** The faster the item changes, the faster the decay.
2.  **Volume:** The more data available, the faster the decay can be without risking statistical insignificance.
3.  **Psychology:** The function must mirror the user's "recency bias" to maintain trust.

While simple exponential decay (EWMA) provides a robust mathematical baseline, modern platforms like Amazon and Steam have evolved toward complex, adaptive, and bifurcated models. These systems prioritize **predictive accuracy** (conversion) over simple statistical description, using time as a feature in a broader machine-learning context rather than just a weight in a weighted average. The future of these systems lies in **adaptive discounting**, where the decay rate itself adjusts in real-time to the detected stability of the product's reputation.

### Summary Table: Determinants and Effects

| Determinant | Condition | Effect on Discount Function | Outcome |
| :--- | :--- | :--- | :--- |
| **Product Volatility** | High (e.g., Software) | Fast Decay (Low $\lambda$) | High Responsiveness, Low Lag |
| **Product Volatility** | Low (e.g., Books) | Slow Decay (High $\lambda$) | High Stability, Low Noise |
| **Data Volume** | Sparse | Slow/No Decay | Maintains Effective Sample Size |
| **Data Volume** | Dense | Fast Decay | Captures Trends, Reduces Inertia |
| **User Psychology** | High Recency Bias | Hyperbolic/Windowed | Matches User Trust Heuristics |
| **Platform Strategy** | Conversion Focus | Machine Learned (Black Box) | Maximizes Sales/Trust |

### References
[cite: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]

**Sources:**
1. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENFf_kK5ss0F8tY5vAZ8tttmqHwmQBJF_6KBr6qRPPP63Ygh8i0yCOHau6EmZgIMgfA812uGBPZhiN0HBnil8zA8eXkCR8aKlcYd34BxihTaPyxv6ODd34FGjT57j7da3NmUWUP1URqpnsbOD6iyObFoNacMzD9xrd4LTX3B4n7rKWyZjItxYuJMgyzBsa5_LrMuGiceAuJ_vZ609K7kjkdACEctxkDHCbc-1LiLTzZTwWTGu5H6GK4H7Fq9UNUALh1IXI-6BsPrpGak3Jqg==)
2. [steampowered.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFL0pY2uWGZUUTX_JfvC0xtj-iS14t2CVyaRG_wF0QNF_FD_Ixl6hnEvc7sSiZSYLv9O9cwe2Tiz0Z3avI_peYOWJzxYC-arVFXsQxOCNVomCDXRBJH99GG6UTFSxVT-kg=)
3. [sjtu.edu.cn](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-ACv_HLNhDPOsnj44rQxNpuIM2HQfZ0rZGyVOkfoGSB2RU6zLSfqX5TVFHYxn8mMI2LjPZ14Lcso-a7j_qexTnyhKG1dwomIv9iEiGAd4p5MNsAX71ynfjv4SONLJVABWeUd9k_Ub7oykznVgGkLV)
4. [q-researchsoftware.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPSp7riSJQg1JLUDB49qsb0agUey-xgztOeVsFpx9EPkz_762giefUxJRNpN3YCLDQIUmKLvarkvcqJ-Yw-5-TVuibi0meVCTHOjyKXE9j6IMGsYITbxATI4672Tfw3SzYJ3E8UlnyRk-Ge-8cdg90EgZD6et87mB7WGMoY2WLcX_xzW-MnyJfPTnZfxXjl9o=)
5. [portfoliooptimizer.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqJFJnKNnDXU44NPuUfWrKjrhAGc2b4g7K6cvZsNL-CbiZyeMgpGx7UwqFTS4ZsbCmegHd623YR5e2X_CtLbXd23b9EW5HWv6lJp3S83DLlqlZeLW0lqn523ITXPxIbBvAI0NcxQV87tXih1bi3WcqO7d6cMZYjC556YcRGcnbT4g5LpODAZhVVCCOP4JLxnHIvsgB84r7Cv1LF18nvzs_YOl0ZBjnbSA=)
6. [ecomtriage.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6HrFxDHoeEMEefWRlGkWJQZwrtLgrZRT_ZSBf83eay9JlpFc2e1RH5l9pPO4J8bxCVMuVdKaMWVGUlmMW3DmDMcKGcIsW1l-FkiDhHI-OQ99PzZDmNd1c6ftBsPd_a6FX5JYQklx9GUhx_pqlCRY8TwjqcEgjWQ==)
7. [kdpcommunity.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlt5Yy5eC_GonfR-nPxD_g_5SvotERSw51PdmNtRBC5drup0FMwBIrgzPvN3vF4am0gYSAWKjomB0xRedzHT0X16L3VaxSfT55GpKjb5ZwzG1aEDbk4yDDp5zJfExoc2aFOFsJn1NREyM8N2jWD7kk1pbLfQi5hajIOQHxPC7MohqR2JxDHwKVPVJP4B_YbH7tPjeQ5gxrDX2e8oeCQtTqVWxaes5aE3U=)
8. [eiris.it](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-mDw7Yk0jCcyZQLdQfUIRDYymdh68UBUW-k8j4nLTyLJY5rnpftJ_TBN88xLFtNpGovug0t_ScF1r2rIfnE05HjZiEGQyL_I3ARGTtfXphVqlpYUmsYnODplTvkdZWmI-ZUD25ou7UmE35FIMqFkIe_NMEs0pNO3toKHembWI)
9. [powerreviews.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsm5h5grbsuGr9o_5g-02v8r4gP23phq8RpmZj2XEGUwBgXmwegaVOhsWsgu6bnpMt4LBbG9cySSxObX_H99LsICJhczLWkSfT91Fz2ni8EqQ5ejIcejQNrhDGoLC01bzHxqi0ibD8d6-BpC_k6Gdv9ZeXLgjMZgRz)
10. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNunJOJjgijac-OwfZWYRT5CLYDJfrj8Vu4mqwR3HAEDYVMbVV46ps-S1jyTQcJc5aFACUoeZ6P62SHy3q73fssLXZdLvpOUjp9U8sMnvu5c5HIrGJanFBi_5ie5aDprbOOaXYsnLsW6eI77hkzmswbT6I1XVtWTCI33EXxWRP9_tVK44BPTzwmNIdHAo=)
11. [une.edu.au](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdK7UkNnrNJ2EsIy7iNylSyORPrB9S2j68EZcHzdwjXuei_ft9IJgsFac6TOcI8zUM799losnQbNx8ZSyF4JOo4GPu0eq9HozEajLvlgaA2FTYS7I_BLJMAlEewRsKwWDq2HdbsGN2qMyxUBXAa4ZYLj70gXWQiQUaHCuX8zE=)
12. [investopedia.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8G-GHpQSxYf2Nh_aKgvBBrX5QWvK6X3KEGXcsCnZHBwwG4BTpga5RYZ9q-_8EYS0PgEWP7zJCnr-bJTZ5DEA_izi4GYjCn3Zh1K8MHd6ZF3W1mSQMvOJ_iipYiWFM96ryxrsTCiCD1-6VWbTSDVY=)
13. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXmK35kR-gXzeJJt4eE5Ow_rupw-A77xnqTLhYxnLIsWUnMzbZRusz5o2b7NPY9VVFxBddSD96kI1zjaXs9nWTBHGgWBROisB05ii5lgCuCHQ-UprntFvyecR2CiVyWtcMWgRdl8cgqw==)
14. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGle67wI0wMGRVXMHjHg7GdGD6WXbUUxxvNu0M3LF0AHzM3qvzLLxyDZc6_2RZ3HxA_FXllnaIVhyKaJXbR3r-x2Chn6Q9Gt-8W_LMuD1D9WP8jL-_eFxfK_oNaI-0ZHq4FTnvjBGNPYSdVxL-89v8DAo28pV4P2lB2TGReJ_ytN8QIdBtFJVlRHd-kKco6Wgxj42v0cDrrEszoy-8H2VUaFN5qasVl8HdSOZzSwUdBYiL6VvY=)
15. [selfpublishingreview.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-ZsQnD5cemTcuUy01ZmzLzqLsoMMxiWdo9H-x0TW9ToqoyGLrFyV9J6v3RuZ82g6A3FoqbafQVH-fZZ1JOiEXqf19EQ9JXZPkbLGZmVztczf-t3cfzpeG1Gf3CuTeMkyse4cCbHDi7Nc0Gd0hAqAlswonuMPw_6FO2bI0PdfAf0hjK1GbgSG5y1JG8whBs0nOwGQkTTG8ie473qSouvcH3u6-9g==)
16. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtK_nhdpifLhExpTwAkeiBBMrGrsvwEQ6BvG8Oh4RCYZVVABg47e1laKT_dz5FIK_Oxs4X8-tF_zboJNjBZIKqDHArJ-bc7bELwju3F4eQ3wtsH_ENUZqb_g34RO_WWA==)
17. [umass.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrSyq_-cpV4hvM7Hgo5oaoZEXfHk0SczuFdy-ounSRagqZFL9bps7pbTLcpMX6v8igb2ix5DAEDS1Ofw5UuNTzi4vECCx1aR8DrRTUT2InhuBtb60jW41hYHzFFbiUfvaHZqwBcd-IgIl8cN8ucQg=)
18. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOpYhvOYisZNObPrbLWix_QgVDvcekBy8Up5ElepV64Y5phBrNluncJX6AOJ-N7MUOAxMIQWw5v4_5633JuI55KndhdqzdD8OWyooDKtUJ1xQXACL7eZvR0WybY8ruJUG3_YfL5JS7lnONPG6oETnVVxD4kwsOvvZcNTaZ2TwD9ZeOLqM6KYJxT5eNR7NlTIqCTuycCqjVeS6-mMZH8g8wUIxO43ljW-5nH-cqqm4O1cmneQeDr733OFHrMA==)
19. [ecomsellershq.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuG1JhBoOkk0VydGRFpsmrvo9pc-zB4ILT_LFCSvEUcvx1G31c7gVWrOw7mOwRfNQiaLuKCxSQ93XsjOlWQUpaXJ76LKk8nPmTrSDdr2ZAxqwZH3ECVnboh0o8Q3zqBIrKD82UJDZZ8GkPqN4OXBxwVYqXxetxVtz2zfU=)
20. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxIMUW5hBA84zDztvYfM1JxBKEmnBxq1hWQhGfoHuaz0EsOXw9cJB_S30hd0xBUoZGh8u7-rO70EV-c2EfaJBMKN15Ve13-4jDNqAJrsm2Hq_M6xrgIFoWyNxV1B44m0e2)
21. [stackexchange.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9-ht6j_YF1wE04gCnmr3YvIfAsHnxwwQ_izc1zFLRFieuo0oPErClvCO89KY82KvLh8crHX7N60Pyk_grbGHIEhfMElhu8wuLoPSvZpWL8eCVPnv6ihk6fSU5B3ptOFHdYt8VGsXG6tg06uqH5EH35bP9ncKef0ooPuB61eHzvTfviEjfzAc4L9Jf4CKmMn7PoJhQlEYoqS-g)
22. [oreateai.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFysfsvxtP2QQKjMkpTHLz9zxH9rPiw_4BGf93hc51rztcn7CZMzkhNnA5p8sDZ_tP_M5Jji0fKmHIqq-OYPvVC4DdJPbRf2A3CT9WKpCGpYrEsueAzVbd8t_2bx2-y02W_0l64dhpN9S-5-zXvhlrfN-aRFpfjJcBxCkz4kDkC5tnNxsxgQJcvW7mDAVJqjclmQ3waamo2_bq3sCvK_ykY3dHwN2GZau8nmkYPIpTjMDKDiL7Q78POQIDadXLxUw==)
23. [ntu.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDklfAoEl2MudTfkqzSnbd5aMgDkclVXGPNMridE3r50o4_R8_aEb1Ogs5ZeVAwwEKF4wcrd49gaqirz6GFLs4-NZpYn5APIz5ourRIDTJvmWchtktRkplimdSk-gACuC-PjsH8PxPwI4bN-j1Qmcq0INtyJqv6vc=)
24. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzLuw4-uEq-vw1l-8e_WHKHEkAuglZkSL-flj8RPZcEIh1roaoa-8SjFBjWWCMncTMNPy3eLwPCUiAONRMsK_ZShyqnu_9BHlgtBW5PrwXCXjTXGMNHW3bk2ZQHDYGK2ONHGb3JNSU-vvwEhOfIPiWsPS-OJ1WJuYXhY4R9EbFJwe0-Wemuy2_gBq4A0UJXDc-3s-skaxN6Sn8BL2uzjnnFrl3YrwK)
25. [umass.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6MMA3WAF-AHk9zyTuxP8U7ZnxRWeNVSX-nI14ZmuLppD5e3JZmPrqmb7kYOJNRfcVX_HfkZMQ9yl5ghRMJnRr5ZcOkQchmdHJxeoOvotVWUWMf8-xzLcnG90Jb18qq8_v1CYKuI9iHg==)
26. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSq8XHuPwEV28NX2u2I31_famA21nSoy2nYES17pFtX1WBt-NANUVgkPl8W7pjF3NpWxLdnQrpdZwExAMZGy4k7IUSturV_7d2b1ZUwAjonYeRbM4FGwJUDJu3sMr88gV4DX6Xlc_e_ZbYqPrkK8KwB-FYLwf8Uy3Gv_KX2QE5uuxKn8Bwvz7sd146b5VUhPv8cW2mGvYbdTHKmGRVYwWLIs6Yfj8NVCVsWfC_e8IWZtFBops6Uu5-Bg==)
27. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQq7Xpoc6fMtvknH7C_jydgDzPu_NL8ZavESOC3p5dhL7kLUIV8mdDOCQVljmQ6WRHvQFGEYBv9MHNMe5n82kzyuUbPloi7wpsk__1zS3KrnGA5q5gj-TiOv438fDIPvOxCpdcW7BFncwwcaHsdkvXX_zDfoxptH0OjMFYGabyLk7W_gMSk79R1a_wUQ6LScyFikYbF1OArN1spMMnt1c=)
28. [stackexchange.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiFyBBGeyjc1oWK8K1J16LsYLNnlAtojK8ReZH8G3gzZD7gkWT0sRlDJxIgY9UI2i7Y52b1fxIYWCO_36DntuG8f9SZvbKYWyGJvsu4a0YZf24kxDB32MwP2gjc3FquUwbrmTnz6slfCwMxI1OdCeB_y9Ep6ysIjGQCj9-q4dpBuKsQhFfPqjSv5u27YHWUC0CXnB28LQ_fnEzZZXA6EQn_wBT2pRjLrCtDzJ6T0Vw3Sua2sn19_8=)
29. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjNJHuljKZoFvlUaj5oaxYGX7lsx8L3emD-Zmq_3n4KHNQpwwUBlzyAFWI-HJ0hfni1IQZBqn9NoRTfT6DCnJ848LYU1hT-plpvWQ2zVhyNlFsGNLU0opk-Fq0ag9mcxbwMbKRTcA2HO7icOINbPjZhNLFpYVLK6G0qgCLO9cuD1YrSy8QoSmU_OwvZOD-1Fe1embqmyAk9PvzntHkVgCRX-JA3BltPHa020AiExCIWGm2kg==)
30. [fortressofdoors.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2LNl-6u_9Q7ZnHWJ9vxyvcImsgS3apc8xihjqltMi6JE6ypbq1f6hSiaCF78Dx64WrA6-ie1l2bEuoFM0K7upcglnf5Z_DdrNL66vokBViKeP-3jpaxrMlX4P_dQyUc0Sn3ponCRyDLmJjIa1FgiPpPhZHxVvGw==)
31. [steamdb.info](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXmIR0lAkSXjHbqq3Klbs02y8mrqFM7PW_vOHKtCwzLDPgoQB9JyfT30pifrWn2gKbRs1KlpNvdjl93nR7wpcAnRDqoEhjdxyl73ISTvrq7-MDuMZsVq47i2Govdl2uQ==)
32. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElAXpvkG7ku5qwbmuVMnmNhT9pJ5qODMAVuyJC9TBM7Y-qSekTdR2X9jOv13pjUtoauK7tOa33eEH3hSC9RDnZ0mOFv8-S4s5elXXZcRTWLTRDcQpV3DU=)
33. [tradingview.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8LTNju8GnD7-7zdmhGtoxXlY4YjxANqO94eR72ZSqGvN0rT4-dxHW6O3gXZi5o-MvX8X90TvnFyGoOnevu8_Jen3d8ZSvbqoAQNtvnJWzbsUQ33Tn9kd7tWfjBJrz4BXMbrM=)


## Annotations
Annotation(end_index=455, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENFf_kK5ss0F8tY5vAZ8tttmqHwmQBJF_6KBr6qRPPP63Ygh8i0yCOHau6EmZgIMgfA812uGBPZhiN0HBnil8zA8eXkCR8aKlcYd34BxihTaPyxv6ODd34FGjT57j7da3NmUWUP1URqpnsbOD6iyObFoNacMzD9xrd4LTX3B4n7rKWyZjItxYuJMgyzBsa5_LrMuGiceAuJ_vZ609K7kjkdACEctxkDHCbc-1LiLTzZTwWTGu5H6GK4H7Fq9UNUALh1IXI-6BsPrpGak3Jqg==', start_index=443)
Annotation(end_index=455, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFL0pY2uWGZUUTX_JfvC0xtj-iS14t2CVyaRG_wF0QNF_FD_Ixl6hnEvc7sSiZSYLv9O9cwe2Tiz0Z3avI_peYOWJzxYC-arVFXsQxOCNVomCDXRBJH99GG6UTFSxVT-kg=', start_index=443)
Annotation(end_index=804, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-ACv_HLNhDPOsnj44rQxNpuIM2HQfZ0rZGyVOkfoGSB2RU6zLSfqX5TVFHYxn8mMI2LjPZ14Lcso-a7j_qexTnyhKG1dwomIv9iEiGAd4p5MNsAX71ynfjv4SONLJVABWeUd9k_Ub7oykznVgGkLV', start_index=792)
Annotation(end_index=804, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPSp7riSJQg1JLUDB49qsb0agUey-xgztOeVsFpx9EPkz_762giefUxJRNpN3YCLDQIUmKLvarkvcqJ-Yw-5-TVuibi0meVCTHOjyKXE9j6IMGsYITbxATI4672Tfw3SzYJ3E8UlnyRk-Ge-8cdg90EgZD6et87mB7WGMoY2WLcX_xzW-MnyJfPTnZfxXjl9o=', start_index=792)
Annotation(end_index=1142, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqJFJnKNnDXU44NPuUfWrKjrhAGc2b4g7K6cvZsNL-CbiZyeMgpGx7UwqFTS4ZsbCmegHd623YR5e2X_CtLbXd23b9EW5HWv6lJp3S83DLlqlZeLW0lqn523ITXPxIbBvAI0NcxQV87tXih1bi3WcqO7d6cMZYjC556YcRGcnbT4g5LpODAZhVVCCOP4JLxnHIvsgB84r7Cv1LF18nvzs_YOl0ZBjnbSA=', start_index=1130)
Annotation(end_index=1142, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-ACv_HLNhDPOsnj44rQxNpuIM2HQfZ0rZGyVOkfoGSB2RU6zLSfqX5TVFHYxn8mMI2LjPZ14Lcso-a7j_qexTnyhKG1dwomIv9iEiGAd4p5MNsAX71ynfjv4SONLJVABWeUd9k_Ub7oykznVgGkLV', start_index=1130)
Annotation(end_index=1371, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6HrFxDHoeEMEefWRlGkWJQZwrtLgrZRT_ZSBf83eay9JlpFc2e1RH5l9pPO4J8bxCVMuVdKaMWVGUlmMW3DmDMcKGcIsW1l-FkiDhHI-OQ99PzZDmNd1c6ftBsPd_a6FX5JYQklx9GUhx_pqlCRY8TwjqcEgjWQ==', start_index=1359)
Annotation(end_index=1371, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlt5Yy5eC_GonfR-nPxD_g_5SvotERSw51PdmNtRBC5drup0FMwBIrgzPvN3vF4am0gYSAWKjomB0xRedzHT0X16L3VaxSfT55GpKjb5ZwzG1aEDbk4yDDp5zJfExoc2aFOFsJn1NREyM8N2jWD7kk1pbLfQi5hajIOQHxPC7MohqR2JxDHwKVPVJP4B_YbH7tPjeQ5gxrDX2e8oeCQtTqVWxaes5aE3U=', start_index=1359)
Annotation(end_index=1528, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFL0pY2uWGZUUTX_JfvC0xtj-iS14t2CVyaRG_wF0QNF_FD_Ixl6hnEvc7sSiZSYLv9O9cwe2Tiz0Z3avI_peYOWJzxYC-arVFXsQxOCNVomCDXRBJH99GG6UTFSxVT-kg=', start_index=1519)
Annotation(end_index=1897, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-mDw7Yk0jCcyZQLdQfUIRDYymdh68UBUW-k8j4nLTyLJY5rnpftJ_TBN88xLFtNpGovug0t_ScF1r2rIfnE05HjZiEGQyL_I3ARGTtfXphVqlpYUmsYnODplTvkdZWmI-ZUD25ou7UmE35FIMqFkIe_NMEs0pNO3toKHembWI', start_index=1885)
Annotation(end_index=1897, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsm5h5grbsuGr9o_5g-02v8r4gP23phq8RpmZj2XEGUwBgXmwegaVOhsWsgu6bnpMt4LBbG9cySSxObX_H99LsICJhczLWkSfT91Fz2ni8EqQ5ejIcejQNrhDGoLC01bzHxqi0ibD8d6-BpC_k6Gdv9ZeXLgjMZgRz', start_index=1885)
Annotation(end_index=3760, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENFf_kK5ss0F8tY5vAZ8tttmqHwmQBJF_6KBr6qRPPP63Ygh8i0yCOHau6EmZgIMgfA812uGBPZhiN0HBnil8zA8eXkCR8aKlcYd34BxihTaPyxv6ODd34FGjT57j7da3NmUWUP1URqpnsbOD6iyObFoNacMzD9xrd4LTX3B4n7rKWyZjItxYuJMgyzBsa5_LrMuGiceAuJ_vZ609K7kjkdACEctxkDHCbc-1LiLTzZTwWTGu5H6GK4H7Fq9UNUALh1IXI-6BsPrpGak3Jqg==', start_index=3748)
Annotation(end_index=3760, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-ACv_HLNhDPOsnj44rQxNpuIM2HQfZ0rZGyVOkfoGSB2RU6zLSfqX5TVFHYxn8mMI2LjPZ14Lcso-a7j_qexTnyhKG1dwomIv9iEiGAd4p5MNsAX71ynfjv4SONLJVABWeUd9k_Ub7oykznVgGkLV', start_index=3748)
Annotation(end_index=5007, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNunJOJjgijac-OwfZWYRT5CLYDJfrj8Vu4mqwR3HAEDYVMbVV46ps-S1jyTQcJc5aFACUoeZ6P62SHy3q73fssLXZdLvpOUjp9U8sMnvu5c5HIrGJanFBi_5ie5aDprbOOaXYsnLsW6eI77hkzmswbT6I1XVtWTCI33EXxWRP9_tVK44BPTzwmNIdHAo=', start_index=4993)
Annotation(end_index=5007, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdK7UkNnrNJ2EsIy7iNylSyORPrB9S2j68EZcHzdwjXuei_ft9IJgsFac6TOcI8zUM799losnQbNx8ZSyF4JOo4GPu0eq9HozEajLvlgaA2FTYS7I_BLJMAlEewRsKwWDq2HdbsGN2qMyxUBXAa4ZYLj70gXWQiQUaHCuX8zE=', start_index=4993)
Annotation(end_index=5490, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8G-GHpQSxYf2Nh_aKgvBBrX5QWvK6X3KEGXcsCnZHBwwG4BTpga5RYZ9q-_8EYS0PgEWP7zJCnr-bJTZ5DEA_izi4GYjCn3Zh1K8MHd6ZF3W1mSQMvOJ_iipYiWFM96ryxrsTCiCD1-6VWbTSDVY=', start_index=5476)
Annotation(end_index=5490, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXmK35kR-gXzeJJt4eE5Ow_rupw-A77xnqTLhYxnLIsWUnMzbZRusz5o2b7NPY9VVFxBddSD96kI1zjaXs9nWTBHGgWBROisB05ii5lgCuCHQ-UprntFvyecR2CiVyWtcMWgRdl8cgqw==', start_index=5476)
Annotation(end_index=5924, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGle67wI0wMGRVXMHjHg7GdGD6WXbUUxxvNu0M3LF0AHzM3qvzLLxyDZc6_2RZ3HxA_FXllnaIVhyKaJXbR3r-x2Chn6Q9Gt-8W_LMuD1D9WP8jL-_eFxfK_oNaI-0ZHq4FTnvjBGNPYSdVxL-89v8DAo28pV4P2lB2TGReJ_ytN8QIdBtFJVlRHd-kKco6Wgxj42v0cDrrEszoy-8H2VUaFN5qasVl8HdSOZzSwUdBYiL6VvY=', start_index=5914)
Annotation(end_index=6343, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFL0pY2uWGZUUTX_JfvC0xtj-iS14t2CVyaRG_wF0QNF_FD_Ixl6hnEvc7sSiZSYLv9O9cwe2Tiz0Z3avI_peYOWJzxYC-arVFXsQxOCNVomCDXRBJH99GG6UTFSxVT-kg=', start_index=6334)
Annotation(end_index=7192, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFL0pY2uWGZUUTX_JfvC0xtj-iS14t2CVyaRG_wF0QNF_FD_Ixl6hnEvc7sSiZSYLv9O9cwe2Tiz0Z3avI_peYOWJzxYC-arVFXsQxOCNVomCDXRBJH99GG6UTFSxVT-kg=', start_index=7183)
Annotation(end_index=7734, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-ZsQnD5cemTcuUy01ZmzLzqLsoMMxiWdo9H-x0TW9ToqoyGLrFyV9J6v3RuZ82g6A3FoqbafQVH-fZZ1JOiEXqf19EQ9JXZPkbLGZmVztczf-t3cfzpeG1Gf3CuTeMkyse4cCbHDi7Nc0Gd0hAqAlswonuMPw_6FO2bI0PdfAf0hjK1GbgSG5y1JG8whBs0nOwGQkTTG8ie473qSouvcH3u6-9g==', start_index=7721)
Annotation(end_index=7734, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6HrFxDHoeEMEefWRlGkWJQZwrtLgrZRT_ZSBf83eay9JlpFc2e1RH5l9pPO4J8bxCVMuVdKaMWVGUlmMW3DmDMcKGcIsW1l-FkiDhHI-OQ99PzZDmNd1c6ftBsPd_a6FX5JYQklx9GUhx_pqlCRY8TwjqcEgjWQ==', start_index=7721)
Annotation(end_index=8035, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-ACv_HLNhDPOsnj44rQxNpuIM2HQfZ0rZGyVOkfoGSB2RU6zLSfqX5TVFHYxn8mMI2LjPZ14Lcso-a7j_qexTnyhKG1dwomIv9iEiGAd4p5MNsAX71ynfjv4SONLJVABWeUd9k_Ub7oykznVgGkLV', start_index=8022)
Annotation(end_index=8035, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdK7UkNnrNJ2EsIy7iNylSyORPrB9S2j68EZcHzdwjXuei_ft9IJgsFac6TOcI8zUM799losnQbNx8ZSyF4JOo4GPu0eq9HozEajLvlgaA2FTYS7I_BLJMAlEewRsKwWDq2HdbsGN2qMyxUBXAa4ZYLj70gXWQiQUaHCuX8zE=', start_index=8022)
Annotation(end_index=8522, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPSp7riSJQg1JLUDB49qsb0agUey-xgztOeVsFpx9EPkz_762giefUxJRNpN3YCLDQIUmKLvarkvcqJ-Yw-5-TVuibi0meVCTHOjyKXE9j6IMGsYITbxATI4672Tfw3SzYJ3E8UlnyRk-Ge-8cdg90EgZD6et87mB7WGMoY2WLcX_xzW-MnyJfPTnZfxXjl9o=', start_index=8509)
Annotation(end_index=8522, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtK_nhdpifLhExpTwAkeiBBMrGrsvwEQ6BvG8Oh4RCYZVVABg47e1laKT_dz5FIK_Oxs4X8-tF_zboJNjBZIKqDHArJ-bc7bELwju3F4eQ3wtsH_ENUZqb_g34RO_WWA==', start_index=8509)
Annotation(end_index=8984, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6HrFxDHoeEMEefWRlGkWJQZwrtLgrZRT_ZSBf83eay9JlpFc2e1RH5l9pPO4J8bxCVMuVdKaMWVGUlmMW3DmDMcKGcIsW1l-FkiDhHI-OQ99PzZDmNd1c6ftBsPd_a6FX5JYQklx9GUhx_pqlCRY8TwjqcEgjWQ==', start_index=8972)
Annotation(end_index=8984, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlt5Yy5eC_GonfR-nPxD_g_5SvotERSw51PdmNtRBC5drup0FMwBIrgzPvN3vF4am0gYSAWKjomB0xRedzHT0X16L3VaxSfT55GpKjb5ZwzG1aEDbk4yDDp5zJfExoc2aFOFsJn1NREyM8N2jWD7kk1pbLfQi5hajIOQHxPC7MohqR2JxDHwKVPVJP4B_YbH7tPjeQ5gxrDX2e8oeCQtTqVWxaes5aE3U=', start_index=8972)
Annotation(end_index=9447, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6HrFxDHoeEMEefWRlGkWJQZwrtLgrZRT_ZSBf83eay9JlpFc2e1RH5l9pPO4J8bxCVMuVdKaMWVGUlmMW3DmDMcKGcIsW1l-FkiDhHI-OQ99PzZDmNd1c6ftBsPd_a6FX5JYQklx9GUhx_pqlCRY8TwjqcEgjWQ==', start_index=9435)
Annotation(end_index=9447, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlt5Yy5eC_GonfR-nPxD_g_5SvotERSw51PdmNtRBC5drup0FMwBIrgzPvN3vF4am0gYSAWKjomB0xRedzHT0X16L3VaxSfT55GpKjb5ZwzG1aEDbk4yDDp5zJfExoc2aFOFsJn1NREyM8N2jWD7kk1pbLfQi5hajIOQHxPC7MohqR2JxDHwKVPVJP4B_YbH7tPjeQ5gxrDX2e8oeCQtTqVWxaes5aE3U=', start_index=9435)
Annotation(end_index=9682, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENFf_kK5ss0F8tY5vAZ8tttmqHwmQBJF_6KBr6qRPPP63Ygh8i0yCOHau6EmZgIMgfA812uGBPZhiN0HBnil8zA8eXkCR8aKlcYd34BxihTaPyxv6ODd34FGjT57j7da3NmUWUP1URqpnsbOD6iyObFoNacMzD9xrd4LTX3B4n7rKWyZjItxYuJMgyzBsa5_LrMuGiceAuJ_vZ609K7kjkdACEctxkDHCbc-1LiLTzZTwWTGu5H6GK4H7Fq9UNUALh1IXI-6BsPrpGak3Jqg==', start_index=9673)
Annotation(end_index=10095, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6HrFxDHoeEMEefWRlGkWJQZwrtLgrZRT_ZSBf83eay9JlpFc2e1RH5l9pPO4J8bxCVMuVdKaMWVGUlmMW3DmDMcKGcIsW1l-FkiDhHI-OQ99PzZDmNd1c6ftBsPd_a6FX5JYQklx9GUhx_pqlCRY8TwjqcEgjWQ==', start_index=10083)
Annotation(end_index=10095, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsm5h5grbsuGr9o_5g-02v8r4gP23phq8RpmZj2XEGUwBgXmwegaVOhsWsgu6bnpMt4LBbG9cySSxObX_H99LsICJhczLWkSfT91Fz2ni8EqQ5ejIcejQNrhDGoLC01bzHxqi0ibD8d6-BpC_k6Gdv9ZeXLgjMZgRz', start_index=10083)
Annotation(end_index=10422, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrSyq_-cpV4hvM7Hgo5oaoZEXfHk0SczuFdy-ounSRagqZFL9bps7pbTLcpMX6v8igb2ix5DAEDS1Ofw5UuNTzi4vECCx1aR8DrRTUT2InhuBtb60jW41hYHzFFbiUfvaHZqwBcd-IgIl8cN8ucQg=', start_index=10408)
Annotation(end_index=10422, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtK_nhdpifLhExpTwAkeiBBMrGrsvwEQ6BvG8Oh4RCYZVVABg47e1laKT_dz5FIK_Oxs4X8-tF_zboJNjBZIKqDHArJ-bc7bELwju3F4eQ3wtsH_ENUZqb_g34RO_WWA==', start_index=10408)
Annotation(end_index=11551, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqJFJnKNnDXU44NPuUfWrKjrhAGc2b4g7K6cvZsNL-CbiZyeMgpGx7UwqFTS4ZsbCmegHd623YR5e2X_CtLbXd23b9EW5HWv6lJp3S83DLlqlZeLW0lqn523ITXPxIbBvAI0NcxQV87tXih1bi3WcqO7d6cMZYjC556YcRGcnbT4g5LpODAZhVVCCOP4JLxnHIvsgB84r7Cv1LF18nvzs_YOl0ZBjnbSA=', start_index=11538)
Annotation(end_index=11551, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNunJOJjgijac-OwfZWYRT5CLYDJfrj8Vu4mqwR3HAEDYVMbVV46ps-S1jyTQcJc5aFACUoeZ6P62SHy3q73fssLXZdLvpOUjp9U8sMnvu5c5HIrGJanFBi_5ie5aDprbOOaXYsnLsW6eI77hkzmswbT6I1XVtWTCI33EXxWRP9_tVK44BPTzwmNIdHAo=', start_index=11538)
Annotation(end_index=11847, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrSyq_-cpV4hvM7Hgo5oaoZEXfHk0SczuFdy-ounSRagqZFL9bps7pbTLcpMX6v8igb2ix5DAEDS1Ofw5UuNTzi4vECCx1aR8DrRTUT2InhuBtb60jW41hYHzFFbiUfvaHZqwBcd-IgIl8cN8ucQg=', start_index=11833)
Annotation(end_index=11847, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtK_nhdpifLhExpTwAkeiBBMrGrsvwEQ6BvG8Oh4RCYZVVABg47e1laKT_dz5FIK_Oxs4X8-tF_zboJNjBZIKqDHArJ-bc7bELwju3F4eQ3wtsH_ENUZqb_g34RO_WWA==', start_index=11833)
Annotation(end_index=12389, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOpYhvOYisZNObPrbLWix_QgVDvcekBy8Up5ElepV64Y5phBrNluncJX6AOJ-N7MUOAxMIQWw5v4_5633JuI55KndhdqzdD8OWyooDKtUJ1xQXACL7eZvR0WybY8ruJUG3_YfL5JS7lnONPG6oETnVVxD4kwsOvvZcNTaZ2TwD9ZeOLqM6KYJxT5eNR7NlTIqCTuycCqjVeS6-mMZH8g8wUIxO43ljW-5nH-cqqm4O1cmneQeDr733OFHrMA==', start_index=12379)
Annotation(end_index=13078, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6HrFxDHoeEMEefWRlGkWJQZwrtLgrZRT_ZSBf83eay9JlpFc2e1RH5l9pPO4J8bxCVMuVdKaMWVGUlmMW3DmDMcKGcIsW1l-FkiDhHI-OQ99PzZDmNd1c6ftBsPd_a6FX5JYQklx9GUhx_pqlCRY8TwjqcEgjWQ==', start_index=13066)
Annotation(end_index=13078, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlt5Yy5eC_GonfR-nPxD_g_5SvotERSw51PdmNtRBC5drup0FMwBIrgzPvN3vF4am0gYSAWKjomB0xRedzHT0X16L3VaxSfT55GpKjb5ZwzG1aEDbk4yDDp5zJfExoc2aFOFsJn1NREyM8N2jWD7kk1pbLfQi5hajIOQHxPC7MohqR2JxDHwKVPVJP4B_YbH7tPjeQ5gxrDX2e8oeCQtTqVWxaes5aE3U=', start_index=13066)
Annotation(end_index=13419, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlt5Yy5eC_GonfR-nPxD_g_5SvotERSw51PdmNtRBC5drup0FMwBIrgzPvN3vF4am0gYSAWKjomB0xRedzHT0X16L3VaxSfT55GpKjb5ZwzG1aEDbk4yDDp5zJfExoc2aFOFsJn1NREyM8N2jWD7kk1pbLfQi5hajIOQHxPC7MohqR2JxDHwKVPVJP4B_YbH7tPjeQ5gxrDX2e8oeCQtTqVWxaes5aE3U=', start_index=13410)
Annotation(end_index=13813, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6HrFxDHoeEMEefWRlGkWJQZwrtLgrZRT_ZSBf83eay9JlpFc2e1RH5l9pPO4J8bxCVMuVdKaMWVGUlmMW3DmDMcKGcIsW1l-FkiDhHI-OQ99PzZDmNd1c6ftBsPd_a6FX5JYQklx9GUhx_pqlCRY8TwjqcEgjWQ==', start_index=13800)
Annotation(end_index=13813, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuG1JhBoOkk0VydGRFpsmrvo9pc-zB4ILT_LFCSvEUcvx1G31c7gVWrOw7mOwRfNQiaLuKCxSQ93XsjOlWQUpaXJ76LKk8nPmTrSDdr2ZAxqwZH3ECVnboh0o8Q3zqBIrKD82UJDZZ8GkPqN4OXBxwVYqXxetxVtz2zfU=', start_index=13800)
Annotation(end_index=14393, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFL0pY2uWGZUUTX_JfvC0xtj-iS14t2CVyaRG_wF0QNF_FD_Ixl6hnEvc7sSiZSYLv9O9cwe2Tiz0Z3avI_peYOWJzxYC-arVFXsQxOCNVomCDXRBJH99GG6UTFSxVT-kg=', start_index=14380)
Annotation(end_index=14393, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxIMUW5hBA84zDztvYfM1JxBKEmnBxq1hWQhGfoHuaz0EsOXw9cJB_S30hd0xBUoZGh8u7-rO70EV-c2EfaJBMKN15Ve13-4jDNqAJrsm2Hq_M6xrgIFoWyNxV1B44m0e2', start_index=14380)
Annotation(end_index=14619, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9-ht6j_YF1wE04gCnmr3YvIfAsHnxwwQ_izc1zFLRFieuo0oPErClvCO89KY82KvLh8crHX7N60Pyk_grbGHIEhfMElhu8wuLoPSvZpWL8eCVPnv6ihk6fSU5B3ptOFHdYt8VGsXG6tg06uqH5EH35bP9ncKef0ooPuB61eHzvTfviEjfzAc4L9Jf4CKmMn7PoJhQlEYoqS-g', start_index=14605)
Annotation(end_index=14619, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxIMUW5hBA84zDztvYfM1JxBKEmnBxq1hWQhGfoHuaz0EsOXw9cJB_S30hd0xBUoZGh8u7-rO70EV-c2EfaJBMKN15Ve13-4jDNqAJrsm2Hq_M6xrgIFoWyNxV1B44m0e2', start_index=14605)
Annotation(end_index=15118, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNunJOJjgijac-OwfZWYRT5CLYDJfrj8Vu4mqwR3HAEDYVMbVV46ps-S1jyTQcJc5aFACUoeZ6P62SHy3q73fssLXZdLvpOUjp9U8sMnvu5c5HIrGJanFBi_5ie5aDprbOOaXYsnLsW6eI77hkzmswbT6I1XVtWTCI33EXxWRP9_tVK44BPTzwmNIdHAo=', start_index=15104)
Annotation(end_index=15118, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdK7UkNnrNJ2EsIy7iNylSyORPrB9S2j68EZcHzdwjXuei_ft9IJgsFac6TOcI8zUM799losnQbNx8ZSyF4JOo4GPu0eq9HozEajLvlgaA2FTYS7I_BLJMAlEewRsKwWDq2HdbsGN2qMyxUBXAa4ZYLj70gXWQiQUaHCuX8zE=', start_index=15104)
Annotation(end_index=15850, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFysfsvxtP2QQKjMkpTHLz9zxH9rPiw_4BGf93hc51rztcn7CZMzkhNnA5p8sDZ_tP_M5Jji0fKmHIqq-OYPvVC4DdJPbRf2A3CT9WKpCGpYrEsueAzVbd8t_2bx2-y02W_0l64dhpN9S-5-zXvhlrfN-aRFpfjJcBxCkz4kDkC5tnNxsxgQJcvW7mDAVJqjclmQ3waamo2_bq3sCvK_ykY3dHwN2GZau8nmkYPIpTjMDKDiL7Q78POQIDadXLxUw==', start_index=15840)
Annotation(end_index=16141, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsm5h5grbsuGr9o_5g-02v8r4gP23phq8RpmZj2XEGUwBgXmwegaVOhsWsgu6bnpMt4LBbG9cySSxObX_H99LsICJhczLWkSfT91Fz2ni8EqQ5ejIcejQNrhDGoLC01bzHxqi0ibD8d6-BpC_k6Gdv9ZeXLgjMZgRz', start_index=16132)
Annotation(end_index=16511, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-mDw7Yk0jCcyZQLdQfUIRDYymdh68UBUW-k8j4nLTyLJY5rnpftJ_TBN88xLFtNpGovug0t_ScF1r2rIfnE05HjZiEGQyL_I3ARGTtfXphVqlpYUmsYnODplTvkdZWmI-ZUD25ou7UmE35FIMqFkIe_NMEs0pNO3toKHembWI', start_index=16498)
Annotation(end_index=16511, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDklfAoEl2MudTfkqzSnbd5aMgDkclVXGPNMridE3r50o4_R8_aEb1Ogs5ZeVAwwEKF4wcrd49gaqirz6GFLs4-NZpYn5APIz5ourRIDTJvmWchtktRkplimdSk-gACuC-PjsH8PxPwI4bN-j1Qmcq0INtyJqv6vc=', start_index=16498)
Annotation(end_index=17096, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8G-GHpQSxYf2Nh_aKgvBBrX5QWvK6X3KEGXcsCnZHBwwG4BTpga5RYZ9q-_8EYS0PgEWP7zJCnr-bJTZ5DEA_izi4GYjCn3Zh1K8MHd6ZF3W1mSQMvOJ_iipYiWFM96ryxrsTCiCD1-6VWbTSDVY=', start_index=17082)
Annotation(end_index=17096, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzLuw4-uEq-vw1l-8e_WHKHEkAuglZkSL-flj8RPZcEIh1roaoa-8SjFBjWWCMncTMNPy3eLwPCUiAONRMsK_ZShyqnu_9BHlgtBW5PrwXCXjTXGMNHW3bk2ZQHDYGK2ONHGb3JNSU-vvwEhOfIPiWsPS-OJ1WJuYXhY4R9EbFJwe0-Wemuy2_gBq4A0UJXDc-3s-skaxN6Sn8BL2uzjnnFrl3YrwK', start_index=17082)
Annotation(end_index=17908, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqJFJnKNnDXU44NPuUfWrKjrhAGc2b4g7K6cvZsNL-CbiZyeMgpGx7UwqFTS4ZsbCmegHd623YR5e2X_CtLbXd23b9EW5HWv6lJp3S83DLlqlZeLW0lqn523ITXPxIbBvAI0NcxQV87tXih1bi3WcqO7d6cMZYjC556YcRGcnbT4g5LpODAZhVVCCOP4JLxnHIvsgB84r7Cv1LF18nvzs_YOl0ZBjnbSA=', start_index=17896)
Annotation(end_index=17908, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-ACv_HLNhDPOsnj44rQxNpuIM2HQfZ0rZGyVOkfoGSB2RU6zLSfqX5TVFHYxn8mMI2LjPZ14Lcso-a7j_qexTnyhKG1dwomIv9iEiGAd4p5MNsAX71ynfjv4SONLJVABWeUd9k_Ub7oykznVgGkLV', start_index=17896)
Annotation(end_index=18547, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrSyq_-cpV4hvM7Hgo5oaoZEXfHk0SczuFdy-ounSRagqZFL9bps7pbTLcpMX6v8igb2ix5DAEDS1Ofw5UuNTzi4vECCx1aR8DrRTUT2InhuBtb60jW41hYHzFFbiUfvaHZqwBcd-IgIl8cN8ucQg=', start_index=18529)
Annotation(end_index=18547, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6MMA3WAF-AHk9zyTuxP8U7ZnxRWeNVSX-nI14ZmuLppD5e3JZmPrqmb7kYOJNRfcVX_HfkZMQ9yl5ghRMJnRr5ZcOkQchmdHJxeoOvotVWUWMf8-xzLcnG90Jb18qq8_v1CYKuI9iHg==', start_index=18529)
Annotation(end_index=18547, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtK_nhdpifLhExpTwAkeiBBMrGrsvwEQ6BvG8Oh4RCYZVVABg47e1laKT_dz5FIK_Oxs4X8-tF_zboJNjBZIKqDHArJ-bc7bELwju3F4eQ3wtsH_ENUZqb_g34RO_WWA==', start_index=18529)
Annotation(end_index=18938, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNunJOJjgijac-OwfZWYRT5CLYDJfrj8Vu4mqwR3HAEDYVMbVV46ps-S1jyTQcJc5aFACUoeZ6P62SHy3q73fssLXZdLvpOUjp9U8sMnvu5c5HIrGJanFBi_5ie5aDprbOOaXYsnLsW6eI77hkzmswbT6I1XVtWTCI33EXxWRP9_tVK44BPTzwmNIdHAo=', start_index=18928)
Annotation(end_index=19435, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFysfsvxtP2QQKjMkpTHLz9zxH9rPiw_4BGf93hc51rztcn7CZMzkhNnA5p8sDZ_tP_M5Jji0fKmHIqq-OYPvVC4DdJPbRf2A3CT9WKpCGpYrEsueAzVbd8t_2bx2-y02W_0l64dhpN9S-5-zXvhlrfN-aRFpfjJcBxCkz4kDkC5tnNxsxgQJcvW7mDAVJqjclmQ3waamo2_bq3sCvK_ykY3dHwN2GZau8nmkYPIpTjMDKDiL7Q78POQIDadXLxUw==', start_index=19425)
Annotation(end_index=19819, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxIMUW5hBA84zDztvYfM1JxBKEmnBxq1hWQhGfoHuaz0EsOXw9cJB_S30hd0xBUoZGh8u7-rO70EV-c2EfaJBMKN15Ve13-4jDNqAJrsm2Hq_M6xrgIFoWyNxV1B44m0e2', start_index=19809)
Annotation(end_index=20271, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPSp7riSJQg1JLUDB49qsb0agUey-xgztOeVsFpx9EPkz_762giefUxJRNpN3YCLDQIUmKLvarkvcqJ-Yw-5-TVuibi0meVCTHOjyKXE9j6IMGsYITbxATI4672Tfw3SzYJ3E8UlnyRk-Ge-8cdg90EgZD6et87mB7WGMoY2WLcX_xzW-MnyJfPTnZfxXjl9o=', start_index=20258)
Annotation(end_index=20271, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSq8XHuPwEV28NX2u2I31_famA21nSoy2nYES17pFtX1WBt-NANUVgkPl8W7pjF3NpWxLdnQrpdZwExAMZGy4k7IUSturV_7d2b1ZUwAjonYeRbM4FGwJUDJu3sMr88gV4DX6Xlc_e_ZbYqPrkK8KwB-FYLwf8Uy3Gv_KX2QE5uuxKn8Bwvz7sd146b5VUhPv8cW2mGvYbdTHKmGRVYwWLIs6Yfj8NVCVsWfC_e8IWZtFBops6Uu5-Bg==', start_index=20258)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-ZsQnD5cemTcuUy01ZmzLzqLsoMMxiWdo9H-x0TW9ToqoyGLrFyV9J6v3RuZ82g6A3FoqbafQVH-fZZ1JOiEXqf19EQ9JXZPkbLGZmVztczf-t3cfzpeG1Gf3CuTeMkyse4cCbHDi7Nc0Gd0hAqAlswonuMPw_6FO2bI0PdfAf0hjK1GbgSG5y1JG8whBs0nOwGQkTTG8ie473qSouvcH3u6-9g==', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2LNl-6u_9Q7ZnHWJ9vxyvcImsgS3apc8xihjqltMi6JE6ypbq1f6hSiaCF78Dx64WrA6-ie1l2bEuoFM0K7upcglnf5Z_DdrNL66vokBViKeP-3jpaxrMlX4P_dQyUc0Sn3ponCRyDLmJjIa1FgiPpPhZHxVvGw==', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6HrFxDHoeEMEefWRlGkWJQZwrtLgrZRT_ZSBf83eay9JlpFc2e1RH5l9pPO4J8bxCVMuVdKaMWVGUlmMW3DmDMcKGcIsW1l-FkiDhHI-OQ99PzZDmNd1c6ftBsPd_a6FX5JYQklx9GUhx_pqlCRY8TwjqcEgjWQ==', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENFf_kK5ss0F8tY5vAZ8tttmqHwmQBJF_6KBr6qRPPP63Ygh8i0yCOHau6EmZgIMgfA812uGBPZhiN0HBnil8zA8eXkCR8aKlcYd34BxihTaPyxv6ODd34FGjT57j7da3NmUWUP1URqpnsbOD6iyObFoNacMzD9xrd4LTX3B4n7rKWyZjItxYuJMgyzBsa5_LrMuGiceAuJ_vZ609K7kjkdACEctxkDHCbc-1LiLTzZTwWTGu5H6GK4H7Fq9UNUALh1IXI-6BsPrpGak3Jqg==', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiFyBBGeyjc1oWK8K1J16LsYLNnlAtojK8ReZH8G3gzZD7gkWT0sRlDJxIgY9UI2i7Y52b1fxIYWCO_36DntuG8f9SZvbKYWyGJvsu4a0YZf24kxDB32MwP2gjc3FquUwbrmTnz6slfCwMxI1OdCeB_y9Ep6ysIjGQCj9-q4dpBuKsQhFfPqjSv5u27YHWUC0CXnB28LQ_fnEzZZXA6EQn_wBT2pRjLrCtDzJ6T0Vw3Sua2sn19_8=', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElAXpvkG7ku5qwbmuVMnmNhT9pJ5qODMAVuyJC9TBM7Y-qSekTdR2X9jOv13pjUtoauK7tOa33eEH3hSC9RDnZ0mOFv8-S4s5elXXZcRTWLTRDcQpV3DU=', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-mDw7Yk0jCcyZQLdQfUIRDYymdh68UBUW-k8j4nLTyLJY5rnpftJ_TBN88xLFtNpGovug0t_ScF1r2rIfnE05HjZiEGQyL_I3ARGTtfXphVqlpYUmsYnODplTvkdZWmI-ZUD25ou7UmE35FIMqFkIe_NMEs0pNO3toKHembWI', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8G-GHpQSxYf2Nh_aKgvBBrX5QWvK6X3KEGXcsCnZHBwwG4BTpga5RYZ9q-_8EYS0PgEWP7zJCnr-bJTZ5DEA_izi4GYjCn3Zh1K8MHd6ZF3W1mSQMvOJ_iipYiWFM96ryxrsTCiCD1-6VWbTSDVY=', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9-ht6j_YF1wE04gCnmr3YvIfAsHnxwwQ_izc1zFLRFieuo0oPErClvCO89KY82KvLh8crHX7N60Pyk_grbGHIEhfMElhu8wuLoPSvZpWL8eCVPnv6ihk6fSU5B3ptOFHdYt8VGsXG6tg06uqH5EH35bP9ncKef0ooPuB61eHzvTfviEjfzAc4L9Jf4CKmMn7PoJhQlEYoqS-g', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFL0pY2uWGZUUTX_JfvC0xtj-iS14t2CVyaRG_wF0QNF_FD_Ixl6hnEvc7sSiZSYLv9O9cwe2Tiz0Z3avI_peYOWJzxYC-arVFXsQxOCNVomCDXRBJH99GG6UTFSxVT-kg=', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqJFJnKNnDXU44NPuUfWrKjrhAGc2b4g7K6cvZsNL-CbiZyeMgpGx7UwqFTS4ZsbCmegHd623YR5e2X_CtLbXd23b9EW5HWv6lJp3S83DLlqlZeLW0lqn523ITXPxIbBvAI0NcxQV87tXih1bi3WcqO7d6cMZYjC556YcRGcnbT4g5LpODAZhVVCCOP4JLxnHIvsgB84r7Cv1LF18nvzs_YOl0ZBjnbSA=', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrSyq_-cpV4hvM7Hgo5oaoZEXfHk0SczuFdy-ounSRagqZFL9bps7pbTLcpMX6v8igb2ix5DAEDS1Ofw5UuNTzi4vECCx1aR8DrRTUT2InhuBtb60jW41hYHzFFbiUfvaHZqwBcd-IgIl8cN8ucQg=', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFysfsvxtP2QQKjMkpTHLz9zxH9rPiw_4BGf93hc51rztcn7CZMzkhNnA5p8sDZ_tP_M5Jji0fKmHIqq-OYPvVC4DdJPbRf2A3CT9WKpCGpYrEsueAzVbd8t_2bx2-y02W_0l64dhpN9S-5-zXvhlrfN-aRFpfjJcBxCkz4kDkC5tnNxsxgQJcvW7mDAVJqjclmQ3waamo2_bq3sCvK_ykY3dHwN2GZau8nmkYPIpTjMDKDiL7Q78POQIDadXLxUw==', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzLuw4-uEq-vw1l-8e_WHKHEkAuglZkSL-flj8RPZcEIh1roaoa-8SjFBjWWCMncTMNPy3eLwPCUiAONRMsK_ZShyqnu_9BHlgtBW5PrwXCXjTXGMNHW3bk2ZQHDYGK2ONHGb3JNSU-vvwEhOfIPiWsPS-OJ1WJuYXhY4R9EbFJwe0-Wemuy2_gBq4A0UJXDc-3s-skaxN6Sn8BL2uzjnnFrl3YrwK', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-ACv_HLNhDPOsnj44rQxNpuIM2HQfZ0rZGyVOkfoGSB2RU6zLSfqX5TVFHYxn8mMI2LjPZ14Lcso-a7j_qexTnyhKG1dwomIv9iEiGAd4p5MNsAX71ynfjv4SONLJVABWeUd9k_Ub7oykznVgGkLV', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPSp7riSJQg1JLUDB49qsb0agUey-xgztOeVsFpx9EPkz_762giefUxJRNpN3YCLDQIUmKLvarkvcqJ-Yw-5-TVuibi0meVCTHOjyKXE9j6IMGsYITbxATI4672Tfw3SzYJ3E8UlnyRk-Ge-8cdg90EgZD6et87mB7WGMoY2WLcX_xzW-MnyJfPTnZfxXjl9o=', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSq8XHuPwEV28NX2u2I31_famA21nSoy2nYES17pFtX1WBt-NANUVgkPl8W7pjF3NpWxLdnQrpdZwExAMZGy4k7IUSturV_7d2b1ZUwAjonYeRbM4FGwJUDJu3sMr88gV4DX6Xlc_e_ZbYqPrkK8KwB-FYLwf8Uy3Gv_KX2QE5uuxKn8Bwvz7sd146b5VUhPv8cW2mGvYbdTHKmGRVYwWLIs6Yfj8NVCVsWfC_e8IWZtFBops6Uu5-Bg==', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXmK35kR-gXzeJJt4eE5Ow_rupw-A77xnqTLhYxnLIsWUnMzbZRusz5o2b7NPY9VVFxBddSD96kI1zjaXs9nWTBHGgWBROisB05ii5lgCuCHQ-UprntFvyecR2CiVyWtcMWgRdl8cgqw==', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGle67wI0wMGRVXMHjHg7GdGD6WXbUUxxvNu0M3LF0AHzM3qvzLLxyDZc6_2RZ3HxA_FXllnaIVhyKaJXbR3r-x2Chn6Q9Gt-8W_LMuD1D9WP8jL-_eFxfK_oNaI-0ZHq4FTnvjBGNPYSdVxL-89v8DAo28pV4P2lB2TGReJ_ytN8QIdBtFJVlRHd-kKco6Wgxj42v0cDrrEszoy-8H2VUaFN5qasVl8HdSOZzSwUdBYiL6VvY=', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuG1JhBoOkk0VydGRFpsmrvo9pc-zB4ILT_LFCSvEUcvx1G31c7gVWrOw7mOwRfNQiaLuKCxSQ93XsjOlWQUpaXJ76LKk8nPmTrSDdr2ZAxqwZH3ECVnboh0o8Q3zqBIrKD82UJDZZ8GkPqN4OXBxwVYqXxetxVtz2zfU=', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6MMA3WAF-AHk9zyTuxP8U7ZnxRWeNVSX-nI14ZmuLppD5e3JZmPrqmb7kYOJNRfcVX_HfkZMQ9yl5ghRMJnRr5ZcOkQchmdHJxeoOvotVWUWMf8-xzLcnG90Jb18qq8_v1CYKuI9iHg==', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8LTNju8GnD7-7zdmhGtoxXlY4YjxANqO94eR72ZSqGvN0rT4-dxHW6O3gXZi5o-MvX8X90TvnFyGoOnevu8_Jen3d8ZSvbqoAQNtvnJWzbsUQ33Tn9kd7tWfjBJrz4BXMbrM=', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDklfAoEl2MudTfkqzSnbd5aMgDkclVXGPNMridE3r50o4_R8_aEb1Ogs5ZeVAwwEKF4wcrd49gaqirz6GFLs4-NZpYn5APIz5ourRIDTJvmWchtktRkplimdSk-gACuC-PjsH8PxPwI4bN-j1Qmcq0INtyJqv6vc=', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNunJOJjgijac-OwfZWYRT5CLYDJfrj8Vu4mqwR3HAEDYVMbVV46ps-S1jyTQcJc5aFACUoeZ6P62SHy3q73fssLXZdLvpOUjp9U8sMnvu5c5HIrGJanFBi_5ie5aDprbOOaXYsnLsW6eI77hkzmswbT6I1XVtWTCI33EXxWRP9_tVK44BPTzwmNIdHAo=', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOpYhvOYisZNObPrbLWix_QgVDvcekBy8Up5ElepV64Y5phBrNluncJX6AOJ-N7MUOAxMIQWw5v4_5633JuI55KndhdqzdD8OWyooDKtUJ1xQXACL7eZvR0WybY8ruJUG3_YfL5JS7lnONPG6oETnVVxD4kwsOvvZcNTaZ2TwD9ZeOLqM6KYJxT5eNR7NlTIqCTuycCqjVeS6-mMZH8g8wUIxO43ljW-5nH-cqqm4O1cmneQeDr733OFHrMA==', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQq7Xpoc6fMtvknH7C_jydgDzPu_NL8ZavESOC3p5dhL7kLUIV8mdDOCQVljmQ6WRHvQFGEYBv9MHNMe5n82kzyuUbPloi7wpsk__1zS3KrnGA5q5gj-TiOv438fDIPvOxCpdcW7BFncwwcaHsdkvXX_zDfoxptH0OjMFYGabyLk7W_gMSk79R1a_wUQ6LScyFikYbF1OArN1spMMnt1c=', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXmIR0lAkSXjHbqq3Klbs02y8mrqFM7PW_vOHKtCwzLDPgoQB9JyfT30pifrWn2gKbRs1KlpNvdjl93nR7wpcAnRDqoEhjdxyl73ISTvrq7-MDuMZsVq47i2Govdl2uQ==', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdK7UkNnrNJ2EsIy7iNylSyORPrB9S2j68EZcHzdwjXuei_ft9IJgsFac6TOcI8zUM799losnQbNx8ZSyF4JOo4GPu0eq9HozEajLvlgaA2FTYS7I_BLJMAlEewRsKwWDq2HdbsGN2qMyxUBXAa4ZYLj70gXWQiQUaHCuX8zE=', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjNJHuljKZoFvlUaj5oaxYGX7lsx8L3emD-Zmq_3n4KHNQpwwUBlzyAFWI-HJ0hfni1IQZBqn9NoRTfT6DCnJ848LYU1hT-plpvWQ2zVhyNlFsGNLU0opk-Fq0ag9mcxbwMbKRTcA2HO7icOINbPjZhNLFpYVLK6G0qgCLO9cuD1YrSy8QoSmU_OwvZOD-1Fe1embqmyAk9PvzntHkVgCRX-JA3BltPHa020AiExCIWGm2kg==', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlt5Yy5eC_GonfR-nPxD_g_5SvotERSw51PdmNtRBC5drup0FMwBIrgzPvN3vF4am0gYSAWKjomB0xRedzHT0X16L3VaxSfT55GpKjb5ZwzG1aEDbk4yDDp5zJfExoc2aFOFsJn1NREyM8N2jWD7kk1pbLfQi5hajIOQHxPC7MohqR2JxDHwKVPVJP4B_YbH7tPjeQ5gxrDX2e8oeCQtTqVWxaes5aE3U=', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsm5h5grbsuGr9o_5g-02v8r4gP23phq8RpmZj2XEGUwBgXmwegaVOhsWsgu6bnpMt4LBbG9cySSxObX_H99LsICJhczLWkSfT91Fz2ni8EqQ5ejIcejQNrhDGoLC01bzHxqi0ibD8d6-BpC_k6Gdv9ZeXLgjMZgRz', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtK_nhdpifLhExpTwAkeiBBMrGrsvwEQ6BvG8Oh4RCYZVVABg47e1laKT_dz5FIK_Oxs4X8-tF_zboJNjBZIKqDHArJ-bc7bELwju3F4eQ3wtsH_ENUZqb_g34RO_WWA==', start_index=22047)
Annotation(end_index=22176, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxIMUW5hBA84zDztvYfM1JxBKEmnBxq1hWQhGfoHuaz0EsOXw9cJB_S30hd0xBUoZGh8u7-rO70EV-c2EfaJBMKN15Ve13-4jDNqAJrsm2Hq_M6xrgIFoWyNxV1B44m0e2', start_index=22047)

## Sources
