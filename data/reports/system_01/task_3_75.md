# Deep Research Report: alibaba/tongyi-deepresearch-30b-a3b
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** b378128b | **Time:** 12.27s | **Cost:** $0.00056
--------------------------------------------------------------------------------

The **temporal function** in seller reputation systems determines how a seller's rating evolves over time, reflecting the **recency and frequency** of feedback. This ensures the reputation accurately represents **current performance** rather than being overly influenced by historical events. Key mechanisms include:

### 1. **Time-Weighted Decay**
   - **Principle:** Older feedback loses influence over time.
   - **Implementation:** 
     - *Exponential/Logarithmic Decay:* Negative feedback from 2 years ago decays faster (e.g., counts as 50% weight) than feedback from 2 weeks ago (e.g., 90% weight).
     - *Linear Decay:* Each month older a review, it loses 2–5% of its initial weight.
   - **Example:** A seller with 100 past 5-star reviews but 1 negative review from 6 months ago will see their rating improve faster than one with a negative review from 3 years ago.

### 2. **Dynamic Weighting by Activity**
   - **Active Sellers:** Recent feedback has higher weight (e.g., Amazon's "Seller Rating Metric" updates rankings daily for active sellers).
   - **Inactive Sellers:** Ratings stabilize as no new feedback is received (minimal decay).
   - **Reactivation:** Sellers re-entering the platform may start with a "probationary" rating until new feedback accumulates.

### 3. **Moving Time Windows**
   - **Recent Activity Focus:** Platforms like eBay sometimes prioritize reviews within the last 90–365 days (e.g., calculating ratings on a rolling 12-month window).
   - **"Freshness Score":** Elite reputation levels (e.g., eBay Top Rated) may require maintaining high ratings over the *last 12 months*.

### 4. **Algorithmic Models**
   - **Bayesian Adjustments:** Weight new feedback more heavily while gradually incorporating past data (e.g., Amazon's "Expected Defect Rate" dashboard).
   - **Machine Learning:** Systems learn buyer preferences, given higher weight to recent feedback if users consistently ignore historical data.
   - **Stochastic Models:** Probabilistic weights based on feedback density (e.g., a burst of 20 recent reviews outweighs 10 reviews from 5 years ago).

### 5. **Recency vs. Consistency**
   - Platforms balance **improvements** (e.g., a series of recent 5-star ratings boosting scores rapidly) against **past misconduct** (e.g., a single severe violation retaining high weight for 6–12 months).
   - *Example:* A seller with a tax evasion violation may retain a negative marker for 24 months regardless of recent performance.

### Why Temporal Functions Matter:
| **Risk without Temporal Adjustments** | **Benefits of Temporal Functions** |
|--------------------------------------|-----------------------------------|
| Penalizes sellers for past mistakes once corrected. | Reflects genuine improvements quickly. |
| Rewards stagnant/no-longer-affecting sellers. | Discourages fraudulent behavior (e.g., anchoring to early high ratings). |
| Misrepresents true risk to buyers. | Maintains trust through evolving accuracy. |

### Platform-Specific Examples:
- **Ebay:** Focuses on the last 12 months for Top Rated status; utilizes "gap scoring" to minimize negative impacts over time.
- **Amazon:** FBA programs prioritize "Recent Received Defect Rate" (90-day window).
- **Etsy:** Warns buyers about sellers with "recent negative feedback" on their shop.

**In essence**, temporal functions balance **fairness** (allowing sellers to rebuild reputation) and **buyer protection** (retaining critical historical data where warranted). The optimal decay rate is determined empirically based on user behavior, transaction types, and risk tolerance.

## Annotations


## Sources
