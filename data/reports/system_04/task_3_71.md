# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 1e61b394 | **Time:** 268.70s | **Cost:** $1.17439
--------------------------------------------------------------------------------

# Determinants of Optimal Budget Allocation Ratios in Multi-Channel Marketing Resource Models

### Key Points
*   **The Equi-Marginal Principle:** The fundamental economic determinant of optimal allocation is the equalization of marginal returns across all channels; the last unit of currency spent on each channel should yield the exact same marginal benefit [cite: 1, 2].
*   **Saturation and Diminishing Returns:** Optimal ratios are heavily constrained by the saturation point of each channel, often modeled using Hill functions. Allocation must stop before the marginal cost exceeds the marginal revenue, which varies significantly by channel [cite: 3, 4].
*   **Attribution Methodology:** The choice of attribution model (e.g., Shapley Value vs. Last-Touch) fundamentally alters the perceived value of a channel, thereby dictating the allocation ratio. Cooperative game theory (Shapley Value) is increasingly favored for capturing cross-channel synergies [cite: 5, 6].
*   **Dynamic Constraints:** Allocation is not static; it is determined by temporal factors including adstock (decay effects), lag effects, and external market conditions (seasonality, competition), often solved using Lagrangian optimization or Reinforcement Learning [cite: 7, 8, 9].

### Executive Summary
The determination of optimal budget allocation ratios in multi-channel marketing is a complex optimization problem that integrates microeconomic theory, statistical modeling, and algorithmic game theory. It moves beyond heuristic rules of thumb, such as the 70-20-10 rule, into rigorous quantitative frameworks. The optimal ratio is determined by the interplay of **channel elasticity**, **saturation curves**, **cross-channel interference (synergy/cannibalization)**, and **budgetary constraints**. Modern resource models utilize Marketing Mix Modeling (MMM) to estimate parameters like adstock and shape effects, while employing mathematical techniques such as Lagrange Multipliers and Reinforcement Learning to solve for the maximization of an objective function (usually Revenue or ROI) subject to cost constraints.

---

## 1. Theoretical Foundations of Resource Allocation

The allocation of marketing resources is fundamentally an economic problem of scarcity. The determination of how much budget to assign to specific channels (e.g., Search, Social, TV, Print) rests on established economic laws regarding utility and productivity.

### 1.1 The Equi-Marginal Principle
The cornerstone of optimal budget allocation is the **Equi-Marginal Principle** (also known as the Law of Equi-Marginal Utility). In the context of marketing, this principle dictates that a firm maximizes its total return (sales, leads, or brand equity) when the marginal rate of return (MRR) is equalized across all marketing channels [cite: 1, 10].

Mathematically, if a firm has a budget \( B \) to allocate across \( n \) channels with costs \( C_1, C_2, ..., C_n \) and resulting benefits \( MU_1, MU_2, ..., MU_n \), the optimal allocation occurs when:

\[
\frac{MU_1}{MC_1} = \frac{MU_2}{MC_2} = ... = \frac{MU_n}{MC_n}
\]

Where:
*   \( MU_i \) is the Marginal Utility (incremental revenue) of channel \( i \).
*   \( MC_i \) is the Marginal Cost of channel \( i \).

If \( \frac{MU_x}{MC_x} > \frac{MU_y}{MC_y} \), the firm should reallocate budget from channel \( y \) to channel \( x \) until the ratios equalize [cite: 11, 12]. This principle implies that "optimal" is not a fixed percentage but a dynamic equilibrium reached when no further reallocation can increase total output [cite: 2].

### 1.2 The Law of Diminishing Marginal Returns
The Equi-Marginal Principle relies on the assumption of diminishing marginal returns. As investment in a specific channel increases, the incremental gain from each additional dollar eventually decreases due to audience saturation and frequency fatigue [cite: 1, 13].

*   **Linear Phase:** Initial spend may show increasing or linear returns as the campaign gains traction.
*   **Concave Phase:** As spend increases, the curve flattens. The optimal allocation point is determined by the curvature of this function (elasticity) relative to other channels [cite: 3].

### 1.3 Opportunity Cost and Substitution
Budget allocation models must account for the opportunity cost of capital. The optimal ratio is determined by the "next best alternative." If the ROI of Digital Display drops below the ROI of Paid Search, the budget flows to Search. This substitution effect is driven by the **cross-elasticity of demand** between channels—how a change in spend in one channel affects the performance of another [cite: 14].

---

## 2. Mathematical Frameworks for Optimization

To operationalize economic principles, marketing scientists employ specific mathematical frameworks to solve for the optimal vector of budget weights.

### 2.1 Lagrangian Optimization
The most rigorous method for determining budget ratios under a fixed budget constraint is the method of **Lagrange Multipliers**. This technique finds the local maxima of a multivariate function subject to equality constraints [cite: 15, 16].

**The Problem Formulation:**
Maximize the Revenue Function \( R(x_1, x_2, ..., x_n) \) subject to the Budget Constraint \( \sum_{i=1}^{n} x_i = B \), where \( x_i \) is the spend on channel \( i \).

**The Lagrangian Function:**
\[
\mathcal{L}(x_1, ..., x_n, \lambda) = R(x_1, ..., x_n) - \lambda \left( \sum_{i=1}^{n} x_i - B \right)
\]

Here, \( \lambda \) (Lambda) represents the **shadow price** of the budget—effectively the marginal value of relaxing the budget constraint by one unit [cite: 15, 17].

**Solving for Optimality:**
By taking the partial derivatives of \( \mathcal{L} \) with respect to each \( x_i \) and \( \lambda \) and setting them to zero, marketers can solve for the optimal spend levels.
\[
\frac{\partial \mathcal{L}}{\partial x_i} = \frac{\partial R}{\partial x_i} - \lambda = 0 \implies \frac{\partial R}{\partial x_i} = \lambda
\]
This result mathematically confirms the Equi-Marginal Principle: at the optimal allocation, the marginal revenue of every channel equals \( \lambda \) [cite: 18, 19].

### 2.2 Linear and Non-Linear Programming
While Lagrangian methods solve for equality constraints, real-world marketing has inequality constraints (e.g., "Spend on Brand Search cannot exceed $50k" or "TV spend must be at least $1M").

*   **Linear Programming (LP):** Used when relationships are assumed to be linear (constant ROI). However, this often leads to "corner solutions" where the entire budget is dumped into the single most efficient channel, ignoring saturation [cite: 20, 21].
*   **Non-Linear Programming (NLP):** Essential for realistic modeling. It incorporates the non-linear response curves (diminishing returns) of marketing channels. Algorithms like Sequential Least Squares Programming (SLSQP) are frequently used to solve these non-linear constrained optimization problems [cite: 8, 22].

### 2.3 Reinforcement Learning (RL)
Advanced models treat budget allocation as a sequential decision-making problem. **Reinforcement Learning**, specifically Q-learning and Markov Decision Processes (MDP), determines optimal ratios by learning from the environment over time [cite: 7, 23].

*   **State Space:** Current market conditions, remaining budget.
*   **Action Space:** Allocation of budget across channels.
*   **Reward Function:** Long-term ROI or Customer Lifetime Value (CLV).

RL models are superior in handling dynamic environments where the effectiveness of a channel changes over time (non-stationarity) and where actions in one period affect the state in the next (carryover effects) [cite: 7].

---

## 3. Marketing Mix Modeling (MMM) Determinants

Marketing Mix Modeling (MMM) provides the empirical parameters that feed into the optimization equations. The specific transformations applied to the data within MMM directly dictate the resulting optimal ratios.

### 3.1 The Hill Function (Saturation)
The shape of the response curve is the primary determinant of how much budget a channel can absorb before becoming inefficient. The **Hill Function** is the standard for modeling this S-shaped or concave saturation [cite: 3, 4].

**Hill Function Equation:**
\[
Response = \beta \times \frac{Spend^\alpha}{Spend^\alpha + K^\alpha}
\]
Where:
*   \( \beta \) (Beta): The maximum capacity or saturation level of the channel.
*   \( K \) (Half-saturation point): The spend level at which the response is half of the maximum.
*   \( \alpha \) (Alpha/Slope): The shape parameter. An S-shape (\( \alpha > 1 \)) implies a threshold effect (minimum spend required), while a C-shape (\( \alpha \leq 1 \)) implies immediate diminishing returns [cite: 24].

**Impact on Allocation:**
*   **High \( K \):** The channel requires significant investment to reach efficiency; the model will allocate larger chunks of budget or nothing (if budget < threshold) [cite: 25].
*   **Low \( \alpha \):** The channel saturates quickly; the model will restrict allocation to avoid waste [cite: 26].

### 3.2 Adstock (Time Decay and Lag)
Marketing effects are not instantaneous. **Adstock** transformations model the carryover effect, where spend in period \( t \) influences sales in period \( t+1, t+2 \), etc. [cite: 8, 27].

**Adstock Formula (Simple Decay):**
\[
A_t = X_t + \lambda A_{t-1}
\]
Where \( \lambda \) is the decay rate (0 to 1).

**Impact on Allocation:**
Channels with high retention rates (high \( \lambda \), e.g., TV or Brand Building) build up "stock" over time. Optimization models that account for adstock will allocate budget to these channels earlier in a campaign to maximize the cumulative effect over the period, whereas short-term models might under-allocate to them [cite: 13, 28].

### 3.3 Baseline vs. Incremental Volume
MMM separates sales into "Base" (sales that would happen without marketing) and "Incremental" (sales driven by marketing). Optimal allocation focuses strictly on maximizing **incremental** volume. If a model incorrectly attributes base sales to a channel (e.g., Branded Search often claims credit for organic intent), the allocation ratio will be inefficiently skewed toward that channel [cite: 29].

---

## 4. Attribution Modeling and Game Theory

While MMM is a top-down approach, Multi-Touch Attribution (MTA) is bottom-up. The method used to assign credit to touchpoints fundamentally changes the input data for optimization.

### 4.1 Shapley Values (Cooperative Game Theory)
The **Shapley Value** is considered the most "fair" method for attribution and subsequent budget allocation. It treats marketing channels as players in a cooperative game working to generate a conversion [cite: 5, 30].

**The Concept:**
It calculates the average marginal contribution of a channel across all possible permutations of the marketing mix.
\[
\phi_i(v) = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|! (|N|-|S|-1)!}{|N|!} (v(S \cup \{i\}) - v(S))
\]
Where \( v(S) \) is the value (conversions) generated by coalition \( S \).

**Determinant of Allocation:**
Unlike heuristic models (Last-Click) that overvalue the bottom of the funnel, Shapley Values reveal the "assist" value of upper-funnel channels (e.g., Display, Video). Using Shapley Values typically shifts optimal allocation ratios **away from Search/Retargeting and toward Social/Video**, as it mathematically accounts for their contribution to initiating the customer journey [cite: 6, 31].

### 4.2 Markov Chains
Markov models calculate the probability of moving from one state (channel interaction) to another (conversion). By calculating the "Removal Effect" (how many conversions are lost if a channel is removed), marketers derive a weight for allocation. This probabilistic approach is robust for sequential decision-making and often yields different optimal ratios than Shapley values in complex, multi-path journeys [cite: 32].

---

## 5. Heuristic and Strategic Allocation Models

In the absence of granular data or for strategic portfolio management, heuristic models determine allocation based on risk profiles and innovation targets.

### 5.1 The 70-20-10 Rule
A widely cited framework for portfolio management in marketing [cite: 33, 34, 35, 36].
*   **70% Core (Proven):** Allocated to channels with historically low CPA and predictable ROI (e.g., Google Ads, SEO).
*   **20% Adjacent (Growth):** Allocated to channels showing promise or scaling potential (e.g., New social platforms, Influencer marketing).
*   **10% Transformational (Experimental):** High-risk, high-reward bets with no historical data (e.g., Metaverse, emerging tech).

**Determinant:**
Here, the determinant is **risk tolerance** and the **need for innovation**. This model prevents the "local maximum" trap where algorithms only fund what worked yesterday, eventually leading to stagnation as core channels saturate or decline [cite: 37, 38].

### 5.2 Competitive Parity and Percentage of Sales
*   **Competitive Parity:** Allocating budget to match the "Share of Voice" of competitors. The determinant is external market activity [cite: 39].
*   **Percentage of Sales:** Setting budget as a fixed ratio of revenue (e.g., 10%). While common, this is theoretically flawed as it treats marketing as a cost of sales rather than an investment that drives sales [cite: 40, 41].

---

## 6. Key Determinants of Allocation Ratios

Synthesizing the theoretical and mathematical models, the specific factors that determine the final ratio can be categorized as follows:

### 6.1 Channel-Specific Factors
*   **Cost Per Acquisition (CPA) / ROI:** The primary driver. Channels with lower CPA receive higher allocation until diminishing returns set in [cite: 42, 43].
*   **Scalability (Reach):** A channel may have high ROI but low volume (e.g., Branded Search). Optimal allocation fills this bucket first but is capped by search volume, forcing remaining budget to lower-ROI, higher-reach channels [cite: 25].
*   **Granularity of Targeting:** Channels allowing precise segmentation (e.g., Social) may receive higher allocation for niche products compared to mass media [cite: 44].

### 6.2 Cross-Channel Interaction (Synergy)
*   **Halo Effects:** Spend in TV often improves the performance of Search (people search for what they see on TV). Models that ignore this interaction (siloed optimization) will under-allocate to TV. Optimal models use interaction terms in regression (\( \beta_{TV \times Search} \)) to capture this, increasing the ratio for the "assisting" channel [cite: 29, 45].
*   **Cannibalization:** If two channels target the exact same audience with similar mechanisms (e.g., SEO and PPC on brand terms), the model must determine the incremental lift of the second channel. High cannibalization reduces the optimal allocation to the overlapping channel [cite: 29].

### 6.3 External Environmental Factors
*   **Seasonality:** Optimal ratios fluctuate throughout the year. During peak demand (e.g., Black Friday), conversion rates rise, shifting the saturation curve upward. This dictates a higher budget allocation during these periods to capture demand [cite: 33].
*   **Market Maturity:** In new markets, allocation favors awareness (Display/Video). In mature markets, it favors efficiency (Search/Email) [cite: 25].

### 6.4 Internal Constraints
*   **Budget Size:** Small budgets are often concentrated in high-efficiency, bottom-funnel channels (corner solutions). As budget grows, the optimal ratio diversifies into upper-funnel channels because the efficient channels saturate [cite: 20, 46].
*   **Business Goals:** If the goal is **Profit**, allocation favors high-margin, low-CPA channels. If the goal is **Growth/Revenue**, allocation shifts to high-volume channels even at a lower ROI [cite: 39, 47].

---

## 7. Conclusion

The "optimal" budget allocation ratio is not a static benchmark but the solution to a dynamic constrained optimization problem. It is determined by:
1.  **The Marginal Rate of Return:** Governed by the Equi-Marginal Principle.
2.  **Response Curves:** Specifically the saturation (Hill function) and decay (Adstock) parameters derived from Marketing Mix Modeling.
3.  **Attribution Logic:** The mathematical method (Shapley, Markov) used to value cross-channel contributions.
4.  **Constraints:** Budget caps, minimum spend thresholds, and strategic risk guardrails (70-20-10).

Advanced organizations move beyond static spreadsheets to **algorithmic allocation**, where Reinforcement Learning and Non-Linear Programming continuously adjust ratios in real-time to maintain the equi-marginal state across an evolving media landscape.

---

### References Table

| Source ID | Topic | Relevance |
| :--- | :--- | :--- |
| [cite: 1, 2, 10] | Equi-Marginal Principle | Foundational economic theory for allocation. |
| [cite: 15, 16, 18] | Lagrange Multipliers | Mathematical method for constrained optimization. |
| [cite: 3, 4, 24] | Hill Function | Modeling saturation and diminishing returns. |
| [cite: 8, 13, 27] | Adstock | Modeling time decay and carryover effects. |
| [cite: 5, 6, 30] | Shapley Values | Game theory approach to fair attribution. |
| [cite: 33, 34, 35] | 70-20-10 Rule | Heuristic framework for portfolio management. |
| [cite: 7, 23] | Reinforcement Learning | Advanced sequential decision-making models. |
| [cite: 29] | MMM Components | Base vs. Incremental, Halo effects, Cannibalization. |

**Sources:**
1. [theintactone.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaHEqpVwn7sGoTyHAhXBAPI_cj_bF0qmQXs3vQUwj6Jz9gANTA41XkeFsYW6nYzTSTkpc3KTFEXHVaL28gEuHUadNbbBkEWwM9BSEoCP8ZY0P49xlT2DWwulYJaTlAHjw-Lu0wpquBxWyLtKj9xZpZi75jnB9SGrJRZfamuJnRrQ==)
2. [slm.mba](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqTC3qym66BbgcqxWnfo199YLG1ekTlHJZ6vA5Wk4kg5aYXqJ3pSXJkqrurZ6Zo-l5l55UMKm96G4atBBYYH4f-C0f7IrWzcJHHXnhuKcItQvWkuqyKbK_bU9P0YICSsVHemD3ovdE2SfXoHzfR-rfDk_IKmLjqnW-fA==)
3. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHaYtlTSEk8nrognEk45ZIjyA7wZ6PQzHgBDrMND4CnE5eju7c3ZZcdQxxI6030wBouqQ-rmC-WBWQV0JhN4P-xoZssdwZZdvpOUk1U51zRJ-rDgTwFYPUS8j4dbS4SPllFpnMM0t95d_ymH-Fwbi_43w-WYd_jWO-KPIbD_Lx_xXpYJ-tZsIV1lXODdhTlyPJBpntKlDC8bPMgg0=)
4. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE495ga4WB2-ozX44LCrktaJ_y64R1CYuH6wlDGmbMyKG82lRvQq_JzUZbsRaJYCj8Cp37CHDQY0Q32aEreGg_R9-kzWyzzScq0I_Dwe0x-5Zfpm0VMiydb4l-fysinWtltr9KvpsY5d5vh37b6Md6PchOg0z-xVrD4xwfC1VKLoKDvtjsH6UP_A8QqJ3pkOzJA-994PvyXEdr2ZMU4M52VaCJt)
5. [lebesgue.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpvNCL1XdUNP8idoCBrFiIbqoADm1U54EsxusSFlngpi8znRNq8Cqw8CD_2dj5VV-yZRZjmI0HCpNLvqAYemtk-cKALt3R5p4KovmDtL3cO2ErcCzQJKfK9KkvgOrQh1zY2x5clcz4uC0JtaggvSHD42RcsUTrelUcQNPgNvzZSnnyhrCeUEfrpg==)
6. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfW0_n_7wOoyeyY_wwb86KRVK5wCFi4RPIc1VNx8bw77LnHbXV2TOMy_cvrpXeWY74v_2wXK2CayhlEOu35qtiBvGxqVgcwHznt2TIDMknaMgZLkyUAg==)
7. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqEx7Qg1nuhJ0HKG15FKx_kNMrrTwPYAxmyok0bsJCxMwhvw4iHlVxJnVLmHEvHD2SYxrAMAC7prbzAFLLkQ8xzB5tgDQBPN4BL7S2-PzIZAqJgi-IxiERW24igD_Gj8kwiCs0hXhy7e0aSL-tEHroreWDxA==)
8. [towardsdatascience.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfn0y5TVlmM_Ug2eJDlsBPl8bc1LvncUaXtbgjRdM-PYABAeG3YpAPG_DPxwEeryTcLvAFs8uEsF8sPstqmyo7JSq6U3XfymuxT_LCvv0ULz4dtNYlDpY2z6Ttnz13Ofgjdl5KujCugIKLaS8Jms8uzvslWOkNQLEXbdEoRXVXn6rV98SG_eEqoylt3xXEqHzegA23Z8pUFN9tyjdZOzAg3HxKeEs=)
9. [eur.nl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJdDhgkc-45qXmzOvpCpHJExyApVanSiXElLjOqAyVnW508lmsd4iNO75Jdm95HxkgvIFks8_LpUrMzSmc2oSeAZ24dDKFEn2595Kv6l_HRiDEHKfqC65XAZ2hruXcRn8xDHhOjp3vyg==)
10. [universalteacher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9I8nRvS7LUiyImBx8pu58FOtC_YUManJToqPv4BUzZy8loy5ueCISq1QfsOG_NlqEdVUHoc0ZRsRULBShCcEpu9Opo5iSLHAYFUGSqwf-FFFNCxN4KdiZFbeZlkhGFm07QU8RCXTWsP-ovEXQSa6CO6SFSf-y7p_P)
11. [tutorchase.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFc-31oAM-pMiJ-4SnCnQUAdLovuRC7mk2Pa30AKQ1yEN40OjPD9AcGu-lxZZjcuCgUvATl7H4QvunVui8exSEQx8ii8Ow-_7STB7Azd5r0ZkgNZy0hG7L5zWyO1b2fMKLWnqJJXFNnq8Ij6VQ4HRin2dfckc-EHx9wF_9T0jCvo7MqSFUr8w8JwUHwqMpblenAmyCmaXQYnKOUpfY=)
12. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzmzYLOOX7kUH7WTswYkuS1xdlyS6YnZrLgUzxganZ1Et3bQnv2wRx-cj-sMfLFmfVCyeMhaiYhMNSEfAPO7KZMQMkKukhw44kK3b6Qx3u3aIO95rl4dIOK25jxbHx9QIi)
13. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTcJL8WrHlnjgm6l3vwf0oo6XarYAqXpqiZPQK4p4BMZ5UXu1bqw1mrw8R9X4EGPWG7eLwwDi1zEohVfAsSveaagJZF6F7Gj7mpWzrEnrM55cbz-zQh0rXy7NBb5hzKBDpq8nZT-6MyDVHDbgkk2ev_IspVMy5FRbnjtHAXJ7tLGCzcA==)
14. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGmyp8gWZOqfsNqukbBWQWe_WQAQBio-9TcqoRaVkCIhYaFwBCOQYDtWWg28_CzRc9cJxNLrsvYWSvtsSbpPYj9R_e4E9DjMzRCtuET4RaJxK4LHQ0tfUYf7ORcDbk8gwEirnnKIkjpEXFFjdl3s_8cfkAprz7zvZVGPM=)
15. [sfu.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLf7aUwrwR5aXgsUJlL9zxSgIH2eZYn33pBeBeS7DmmSNhK90g5Ct6gfqMMl0-_LOPsu3lXjAD3RRzD-y4VAf84efr08RxPGqLWwmBkD1ZNYGfTlKhpWJVOsal2NShRoYUZtoXQxJBVNQh)
16. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFShoyH6nMFEg-Z_jgkU3HgwV4gO859FIQghUTyaaC6L_Jbb4ZFtgqj1rG9YPkH03FXsIIzvhx8xSsqkEMrKNfp9WAKyHan3EPem4vDzWQqNqcpLQpjbzclLklCQwIskAnp)
17. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4B7NjRIh4sPnfaKo1k47yDEoOkW6XpG_LdAeV92JhNxxOaoknd32blCgzaVUvqEbHZK8t0FxA1yN6G_CpjJhZVSpsvG4Ttv-apussWAlRBmWyIJEBUA==)
18. [lumenlearning.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGa7qLmxfNSX6x-37qtO1QRf0Q8Th2ZOh2eJ6W5fmQR-5L3yBd13ZtStVTLmg-9O8p4WRYSd3w4n09PaIoNP6_ll8HSLiSoN9rxo3xfIBPxMhrAzFdBYRdgK5y8Q0JwrVYGvHErpxDwoRBQgN5V9tTd79DChHdcC6frWdO6_t0e)
19. [studysmarter.co.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWpOps_8iZobpiDBDgYdXwfSjF-1BW4ica6bgTcDD-gGS4MggBXEnJWI9w0-9pkmnAIddRW_VTTTH5Wz7w6fOs3Ho90GDjYu6FXmAms-zq-ow2dh4P3KN4rOSNZFxFW0tHCHk892b4aFdxuiZ_j_nb7U15QNZo9tuMq8QE703IrDSwu5D0CeHPzjpcq2tV5KqckAhT-7BSviA2s2KUBifp)
20. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbmcyfds1N1KoI49_R-b6QxylT7ES3eRYAk7RYj-Hvu9IvIAkReYMwgwCkqRfWbPYIhpHvol_1XSioTukkBEPrac7v1icc1qunNC0ARPzUaG-TJoMCEDNjyMAC0tBgPJOvQqBMAEV9-qe0lSSlEchZakfmIpUvqHRhlaGs8TvyPBQhxInqfhc_-xEpJzzXljTddGYjas_FnKFGObP7H92XoL6_nQvBtLVkOr4=)
21. [xpon.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNIhdButtGOt7qEeJLtruDZZHPFnrsjOHpbBxJB6BkhyFR4IHzg-7CpXcpS2_bFUK1kac3taPYXiTxvXfAAVZd0wFQLhFzlNTggZYYqSU43lBdOQcULj5naUi7VF4zWyDxiv4wDYOA)
22. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGezDtuFo9yqBs_QGcGz5YYqdqwfOtBFIf326r9oN8iujHxutPag8BwJMxvcqgHtGtEE3LcwL9-L6RkgO3FWAeLx_4iNrDUaT9xAE3hjdtMmVYk4ViyYyKPzUyGDHfgBQNlIyQ04ThYRqhLwafsiBAC18VcIIOa59RAFN_5lDb9Tizl-QpVQ9sCMIWSeh3oAvIMKdxWbD7gNgBw3apzpEpHVioqSv4zfHujK2cYoOZNpf9WmvHsWb1p8gz4FKx1TwVL8nCPh_9AhI8HMJ-es4tm)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFxm2DhehDvtGfBocuqXkJwZeRkTco2026sbHxHH7w6S2bwVRBDqbRSAYJs-c8CXUP_teXgXE3HyJp7DWZfkhCrtyJF4MUihYIyNHOnvEBPDA5MDNtqiFsuVHsbgmiefRJiaYPBQN2lz3BxdCJQvM21FL9Qw5erKK09GNpMfOlLw0HEVEnSpMujADaLROALZ7MLk1E84htB749uSYgvSnxG2kaOsm10F-zNFQTY9bf_VBbdUsSlfzWyTh_HOQb4YrcKvjKqqzw9s6Jjwt13DSecw__BCMVpJ-CEmj814QhYlIw32VTnQoF3kOq0PFG3gk42_GMPRVzmxxnLHrvfLwe6E4D3C89cjlcgUCdfQSPoEHRm-SVfCCxZeUC8vVVqav5k3O2I2HKMMdBq7rzQy7Z)
24. [indaru.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpmatE3GW-nOqGI7kni8DfISrfZrwR79nlSV0WSm9co_9KJicuJL1aVi4qt_aWquiswbkSVgVJF2j90BTk_PQ1Spxk-jeDfwjCdUAZ2pNy9TL-ZpjZSgKsAnkleR0XOrc_yJk=)
25. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR9NDF1Yo1EkvZvHYs13nyoh5o8OzHSkE_WZUGDMk-b29_yQw9FbWfDJ2a70zvEDTHaYGN7tkC7LOlbaWasbVeY5we9VbD4Nvtz_B6gImJLbcOAPgxW1HzjPy3J7WJj3HwVYilZB2u_xPd9A85XdyT_H2sriJyigQg36-Wf-jg_4S3pjWtxg9IYFgOtbBxYHt2_vK0dfeg_lso5RJx6m--IQiEFaI-AH7RkeC9PC25hu0aP6HUwRovAxUULZJ9kF8nsZhJx9tl8Ts=)
26. [dataslush.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENWlt4kB9NQ927q6PLULFYuMo7hJ-_roVk16DxuP8AqOXSNuupVH7A9KcVj8siTmKLtIlt54hRQuf5mOewz0bjxHeX1-E_lkFyZz56FHN-LQ9ZUIFGXlNRQcQ4xaaSMrbjG_NTnu4YezyJBjL0RbHl)
27. [exploratory.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaViAoCEHX1vYNFWpH0jv-LKjasleRM0rqVOxHRFCCcI7iZLBXdveDz_1CqvsExjH_vOo4WkKT28p824v-tP-BlvUiPkmB-Grioaa_SFMaJUwc6JouG6F-avJ2YJnkR2zrnsh8yubbHOXI7HFT42iWKPJDYaePcv1LnA42uEbOdKNhZDJpDpztgJGpUreGYktYwzhnkvSmwCvZehNbmjDWLXLJGCvatc5dBHE=)
28. [indaru.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_xkdaEtLqXS9CsXPsgbLH392by_toh2kcE22LNWbmgPy8ksRcknKb3JDcr8tB-pN19l9_ZetwA1wjpg7WowRSSAW20RNxGuD9BJjz5x7J9RNOhVYz60I441ahI8YiTpn78HXquq0Po-FqTtJLDHGV6vBbGpYj8vv20qU=)
29. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtUIF5XJN22YT9GkIaVz41LMiirXtILwHpoKwXWKHHXXEtpONHEEXvX4UsBOSYW2RSbdiEyHMsvdgjXCT3iox99kbfpW4MkORLc1vlYAzJBSfPzEf41Fafy_8SIUUdgzVLIycuj3d3Kejk)
30. [quirks.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGy0yVmMRIg394P1McwaK_XB7gS0HrEiqYE5ZiM1XKc2oXMpFdpjpZ1o71UpbE7QEiS-7uwb8nvvy0nyFj82icvurxVpg8a4RQnRVvh7iDMbhsgR4_C_tln75VRu2-wojJkD4NwCMW1egRelGu1IDcWyBjYmfr_NmjC81IpPJrU-w-2qJZ1CoUnlg7XkaQ=)
31. [thedatacherry.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhoQESiiUnHzRjiAT4VhA-KG-yVlKRMDz6XGeAc3U3oJGhgfpIS6QFbxdxvOn8GRfbbQHHhHaapvzAQZ2PqeEQA3JODxqoV-GaD5GyJPeOPz7i2NX5WjxUvMTeUr9lBl4PFuY7Q_4hucJhVhB5I4n2iO6VqQabXM0kP-xHW9ede4PpDsN2jo3BEdc7XAjmqN03FtEY5O1l5-TLIXc=)
32. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtu-SXwWZCLK2wY2pG_tBawjpNcXsFXJPqdM5JhkPFoyVxOnl9L_2yIOo61DSVfNRTJnrnyLsFOcfiZTagVYpFkL7oKXQV0thJt_Nb2T8Ao0MOK7PIUR63h50GvfJcbc6cjhLLcg8gWi087W0pVQB_X9uFBvZThAASfl-zn7fx7l-KWWM1pZ3m0_VyCx35Qy7e8UxZ)
33. [growth-onomics.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuwx-VbCcnbQqqsVG38-HgBLB7NKNGl1mtz4hX71Eqho2Ze5LEaFfzBJw_EHw3lfixTi_i2tLlR0gj1dXqQJYkrIoBov_glhgQeNsRH2ObpjrCyNyRCby4DsjiivLUooYuyi0cM1UFMn1_SR1SbRK0Jz2XVCBbzPAHAvNp)
34. [camphouse.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGg_VxY3Xuh_Dc_mm5YmhJSqpzwj9bbLhrBitwkeuRqZRiM72sGw501mPYzFkBV5AwL9z-TOhwifsz7URqGYQgM07He1PPREyDMZC4KTF6TAJ7K7LWsnNJAqTnurHdRQYxyf0t1xxXCK91T3g==)
35. [smartinsights.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZctZJEPeue9xEcx9iRor8lNGrO-oQ8iNkmLCy-VM_yWnOp0FT0sdjidGdky6uK_Tjq-XDmOwIeQgydyy_NLmbTKyc8dN3NT4Q54dmi6qhf2f1tVcR-eNUYniMww8Zv0-nBATKuVo9LCvLTGNzrfHcVRx6NyMg20Cur1jOz4WWnEVx3GncOiRYuvK0akfj1iKJP0OVfI0_roTBbw==)
36. [growthmethod.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMr2Pk5vlqkiddi51jNIGrp8thio8ktxGgP6uxnXegN7Fzk7t6__MW9737sk_uIRAJH-kNUtXj4rW1XX3tgmLvK7QaY0OS6QRKfwZO65M72mozFyzICWIX)
37. [itonics-innovation.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHo9a6D7yT8sHOPRIffLy8Mvzp2EOz1cbcPJvgl2Ox6oEJ0MdOb72YZOS9C3BcA6odz6pbppng8rYy0OgJvfUyv916QQIojJwUAPnT2fKlFPvTSiTKcNvb8yR73YcvY-iwlkib4Ixs9jwc6JhcjGoS1DaQABkmbrw==)
38. [daily.dev](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrgVJxxzwCZWArdDOWmzovyMFMmq4_O8ZV90gLXKTVxcAJ3A0EC2cr59C5ia5olywbqfJxRFiTjtjvzFDCRnC8qomtWImtPAfzz1WHc99FbdhQqid77ldWdSy3T99U2Oy8aRQzEWb7D_-X9bkQMFiL2OHxO_VB-upNtIX5B8KeYAGVczIefGRUHzG1ySILRZ4FtXXzjD5BRbmFj7SmYjvkoJye)
39. [fiveable.me](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8YoJdpRMWdT0Mf3nUeBNsvgS44dml3cHm5i6kqmrrqJBwLb98A3zuUCmbzb3wkoTk356tDLhioKUQIQEn50W7LSlJu4L_eaRWK8dOnpiJfuOQnsctevl8naC6g72aN-GnHMVnID2_ZJt5cyEfcbsLo9IbBJac-DHF77btSD-NSzEnpBu7OuGkloaENdyhLGOB7-yK6L3ECgohTAh8)
40. [improvado.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJ6Z2fiHO_52wc9l9jZFHcfxK4j0hBnu-6X2W2tP_2RgRWEloHBFDg1FFzJlg9_shY9FrZAuLIN9hhXOCRbInXa-MCLVFRhEBzM4KJr1GjQmcHvtFowBiyfrxrDJAM0sYmShoSbbYLoWjBvQ==)
41. [wise.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4-K-Jc08Pd_1sYYCK-1D-6YRJtkNavhHSfeNHgGtBSJkReubFiJuy3qFZ2GEDRFv178aijRHAiocWnO7GhjLIrAXcFzmy-WH5PeVMRwh9vVeUZntOFaweBPEKuh9X0HsQNrMVoHWqgP2s)
42. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3sv1bOMSwu3otKoDGF_M54rx9U-dXqw60PHNs1ja5RHAPCfrtVhqSXpd_L9LGXXnJ3Flqrz_KacU51eiUBelEjahK1blOi0pFyt99booIS3kwbq2Dj9AMLwynCDiwbI6gahveJ9cr-A-W0Fg2XAxAqIFxENKXSmAFSMrRu4cnDU2giIh6cbs-x79_KUSM9Mm52NBhVqGc0C1ItWo503ot0pLc_Ie13KUev4_xQZQWtLTGiU0cOCILYszqj-oyWtNIcyNz)
43. [connectivewebdesign.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0jdimWrOhXHB_NiHu5R5gjp2W8_1k_gS8EyImQwWR10JdFC6_yJyIoqkBz03RoZCk5nw5qE64b6i0X-UgX_MgN92gm9z8okMXaQGZugW_MmxTvVPtYT4-rD_eF4EEItUvYobK2I2A633HFhBkFm5mwOcofknG)
44. [inbound281.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwZAYzmRCQRDEIW6Q7QdwDrqL5m_UaVMnz8SKLrM7SiUYp-ZVLdfAhno7CllBZYktJJINth-Gr-HNbZmwMcRaZ0X8KEenCF2qZQS5YKdhiRyqh2FTO7jMviFdjJ-7sfxrVfirZbvB60IfhUkysCn8QIcOEoywT9HXPs8J7DPgBq5uqU8jyZqVlzQcYaa5Ne0Q=)
45. [keends.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMJ2if4ab3fxYbDd9bh3-_BdPwvGS48Ujn8xyCgSDIo_zMUOaWC5TssUEOjMlwVIxTYex6N__jDunMLMnN40xPlSdmYNp6Kl_cWOJrPLDtDp4nv7Q0ek_aNafSZONxQ2RMQ_TZ)
46. [abacum.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbwIPIZftrXjUN2LYBM3W1R5_itHlRKmlLNbouZz8GQR8SWDY2OgZRsy4G2hE3tiKCUxEBw0PElb2AKNUKzSI3O2cTjhCnE3zDYi9VV6pLxaPjXWilEhK9QtbV3_Fg5rcjtRzVhCMmKlZsotY=)
47. [funnel.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3QdrI_XZgIfUrBXT1hv9nn_yi3MWcXdt65qKGoLHyGvDnyq7ytPsCCarys95_3BCSty1vbIwrWGpeQHm7au-BDLqxMdSuc-e2nJsajuIgfn8iIOe4-k7eCcjclY9mvBHIQjsKOgrWQR9P76W7vQ==)


## Annotations
Annotation(end_index=372, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaHEqpVwn7sGoTyHAhXBAPI_cj_bF0qmQXs3vQUwj6Jz9gANTA41XkeFsYW6nYzTSTkpc3KTFEXHVaL28gEuHUadNbbBkEWwM9BSEoCP8ZY0P49xlT2DWwulYJaTlAHjw-Lu0wpquBxWyLtKj9xZpZi75jnB9SGrJRZfamuJnRrQ==', start_index=360)
Annotation(end_index=372, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqTC3qym66BbgcqxWnfo199YLG1ekTlHJZ6vA5Wk4kg5aYXqJ3pSXJkqrurZ6Zo-l5l55UMKm96G4atBBYYH4f-C0f7IrWzcJHHXnhuKcItQvWkuqyKbK_bU9P0YICSsVHemD3ovdE2SfXoHzfR-rfDk_IKmLjqnW-fA==', start_index=360)
Annotation(end_index=660, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE495ga4WB2-ozX44LCrktaJ_y64R1CYuH6wlDGmbMyKG82lRvQq_JzUZbsRaJYCj8Cp37CHDQY0Q32aEreGg_R9-kzWyzzScq0I_Dwe0x-5Zfpm0VMiydb4l-fysinWtltr9KvpsY5d5vh37b6Md6PchOg0z-xVrD4xwfC1VKLoKDvtjsH6UP_A8QqJ3pkOzJA-994PvyXEdr2ZMU4M52VaCJt', start_index=648)
Annotation(end_index=660, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHaYtlTSEk8nrognEk45ZIjyA7wZ6PQzHgBDrMND4CnE5eju7c3ZZcdQxxI6030wBouqQ-rmC-WBWQV0JhN4P-xoZssdwZZdvpOUk1U51zRJ-rDgTwFYPUS8j4dbS4SPllFpnMM0t95d_ymH-Fwbi_43w-WYd_jWO-KPIbD_Lx_xXpYJ-tZsIV1lXODdhTlyPJBpntKlDC8bPMgg0=', start_index=648)
Annotation(end_index=973, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpvNCL1XdUNP8idoCBrFiIbqoADm1U54EsxusSFlngpi8znRNq8Cqw8CD_2dj5VV-yZRZjmI0HCpNLvqAYemtk-cKALt3R5p4KovmDtL3cO2ErcCzQJKfK9KkvgOrQh1zY2x5clcz4uC0JtaggvSHD42RcsUTrelUcQNPgNvzZSnnyhrCeUEfrpg==', start_index=961)
Annotation(end_index=973, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfW0_n_7wOoyeyY_wwb86KRVK5wCFi4RPIc1VNx8bw77LnHbXV2TOMy_cvrpXeWY74v_2wXK2CayhlEOu35qtiBvGxqVgcwHznt2TIDMknaMgZLkyUAg==', start_index=961)
Annotation(end_index=1258, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJdDhgkc-45qXmzOvpCpHJExyApVanSiXElLjOqAyVnW508lmsd4iNO75Jdm95HxkgvIFks8_LpUrMzSmc2oSeAZ24dDKFEn2595Kv6l_HRiDEHKfqC65XAZ2hruXcRn8xDHhOjp3vyg==', start_index=1243)
Annotation(end_index=1258, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfn0y5TVlmM_Ug2eJDlsBPl8bc1LvncUaXtbgjRdM-PYABAeG3YpAPG_DPxwEeryTcLvAFs8uEsF8sPstqmyo7JSq6U3XfymuxT_LCvv0ULz4dtNYlDpY2z6Ttnz13Ofgjdl5KujCugIKLaS8Jms8uzvslWOkNQLEXbdEoRXVXn6rV98SG_eEqoylt3xXEqHzegA23Z8pUFN9tyjdZOzAg3HxKeEs=', start_index=1243)
Annotation(end_index=1258, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqEx7Qg1nuhJ0HKG15FKx_kNMrrTwPYAxmyok0bsJCxMwhvw4iHlVxJnVLmHEvHD2SYxrAMAC7prbzAFLLkQ8xzB5tgDQBPN4BL7S2-PzIZAqJgi-IxiERW24igD_Gj8kwiCs0hXhy7e0aSL-tEHroreWDxA==', start_index=1243)
Annotation(end_index=2810, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9I8nRvS7LUiyImBx8pu58FOtC_YUManJToqPv4BUzZy8loy5ueCISq1QfsOG_NlqEdVUHoc0ZRsRULBShCcEpu9Opo5iSLHAYFUGSqwf-FFFNCxN4KdiZFbeZlkhGFm07QU8RCXTWsP-ovEXQSa6CO6SFSf-y7p_P', start_index=2797)
Annotation(end_index=2810, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaHEqpVwn7sGoTyHAhXBAPI_cj_bF0qmQXs3vQUwj6Jz9gANTA41XkeFsYW6nYzTSTkpc3KTFEXHVaL28gEuHUadNbbBkEWwM9BSEoCP8ZY0P49xlT2DWwulYJaTlAHjw-Lu0wpquBxWyLtKj9xZpZi75jnB9SGrJRZfamuJnRrQ==', start_index=2797)
Annotation(end_index=3399, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFc-31oAM-pMiJ-4SnCnQUAdLovuRC7mk2Pa30AKQ1yEN40OjPD9AcGu-lxZZjcuCgUvATl7H4QvunVui8exSEQx8ii8Ow-_7STB7Azd5r0ZkgNZy0hG7L5zWyO1b2fMKLWnqJJXFNnq8Ij6VQ4HRin2dfckc-EHx9wF_9T0jCvo7MqSFUr8w8JwUHwqMpblenAmyCmaXQYnKOUpfY=', start_index=3385)
Annotation(end_index=3399, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzmzYLOOX7kUH7WTswYkuS1xdlyS6YnZrLgUzxganZ1Et3bQnv2wRx-cj-sMfLFmfVCyeMhaiYhMNSEfAPO7KZMQMkKukhw44kK3b6Qx3u3aIO95rl4dIOK25jxbHx9QIi', start_index=3385)
Annotation(end_index=3563, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqTC3qym66BbgcqxWnfo199YLG1ekTlHJZ6vA5Wk4kg5aYXqJ3pSXJkqrurZ6Zo-l5l55UMKm96G4atBBYYH4f-C0f7IrWzcJHHXnhuKcItQvWkuqyKbK_bU9P0YICSsVHemD3ovdE2SfXoHzfR-rfDk_IKmLjqnW-fA==', start_index=3554)
Annotation(end_index=3879, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTcJL8WrHlnjgm6l3vwf0oo6XarYAqXpqiZPQK4p4BMZ5UXu1bqw1mrw8R9X4EGPWG7eLwwDi1zEohVfAsSveaagJZF6F7Gj7mpWzrEnrM55cbz-zQh0rXy7NBb5hzKBDpq8nZT-6MyDVHDbgkk2ev_IspVMy5FRbnjtHAXJ7tLGCzcA==', start_index=3866)
Annotation(end_index=3879, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaHEqpVwn7sGoTyHAhXBAPI_cj_bF0qmQXs3vQUwj6Jz9gANTA41XkeFsYW6nYzTSTkpc3KTFEXHVaL28gEuHUadNbbBkEWwM9BSEoCP8ZY0P49xlT2DWwulYJaTlAHjw-Lu0wpquBxWyLtKj9xZpZi75jnB9SGrJRZfamuJnRrQ==', start_index=3866)
Annotation(end_index=4177, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHaYtlTSEk8nrognEk45ZIjyA7wZ6PQzHgBDrMND4CnE5eju7c3ZZcdQxxI6030wBouqQ-rmC-WBWQV0JhN4P-xoZssdwZZdvpOUk1U51zRJ-rDgTwFYPUS8j4dbS4SPllFpnMM0t95d_ymH-Fwbi_43w-WYd_jWO-KPIbD_Lx_xXpYJ-tZsIV1lXODdhTlyPJBpntKlDC8bPMgg0=', start_index=4168)
Annotation(end_index=4629, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGmyp8gWZOqfsNqukbBWQWe_WQAQBio-9TcqoRaVkCIhYaFwBCOQYDtWWg28_CzRc9cJxNLrsvYWSvtsSbpPYj9R_e4E9DjMzRCtuET4RaJxK4LHQ0tfUYf7ORcDbk8gwEirnnKIkjpEXFFjdl3s_8cfkAprz7zvZVGPM=', start_index=4619)
Annotation(end_index=5110, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFShoyH6nMFEg-Z_jgkU3HgwV4gO859FIQghUTyaaC6L_Jbb4ZFtgqj1rG9YPkH03FXsIIzvhx8xSsqkEMrKNfp9WAKyHan3EPem4vDzWQqNqcpLQpjbzclLklCQwIskAnp', start_index=5096)
Annotation(end_index=5110, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLf7aUwrwR5aXgsUJlL9zxSgIH2eZYn33pBeBeS7DmmSNhK90g5Ct6gfqMMl0-_LOPsu3lXjAD3RRzD-y4VAf84efr08RxPGqLWwmBkD1ZNYGfTlKhpWJVOsal2NShRoYUZtoXQxJBVNQh', start_index=5096)
Annotation(end_index=5620, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4B7NjRIh4sPnfaKo1k47yDEoOkW6XpG_LdAeV92JhNxxOaoknd32blCgzaVUvqEbHZK8t0FxA1yN6G_CpjJhZVSpsvG4Ttv-apussWAlRBmWyIJEBUA==', start_index=5606)
Annotation(end_index=5620, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLf7aUwrwR5aXgsUJlL9zxSgIH2eZYn33pBeBeS7DmmSNhK90g5Ct6gfqMMl0-_LOPsu3lXjAD3RRzD-y4VAf84efr08RxPGqLWwmBkD1ZNYGfTlKhpWJVOsal2NShRoYUZtoXQxJBVNQh', start_index=5606)
Annotation(end_index=6143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWpOps_8iZobpiDBDgYdXwfSjF-1BW4ica6bgTcDD-gGS4MggBXEnJWI9w0-9pkmnAIddRW_VTTTH5Wz7w6fOs3Ho90GDjYu6FXmAms-zq-ow2dh4P3KN4rOSNZFxFW0tHCHk892b4aFdxuiZ_j_nb7U15QNZo9tuMq8QE703IrDSwu5D0CeHPzjpcq2tV5KqckAhT-7BSviA2s2KUBifp', start_index=6129)
Annotation(end_index=6143, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGa7qLmxfNSX6x-37qtO1QRf0Q8Th2ZOh2eJ6W5fmQR-5L3yBd13ZtStVTLmg-9O8p4WRYSd3w4n09PaIoNP6_ll8HSLiSoN9rxo3xfIBPxMhrAzFdBYRdgK5y8Q0JwrVYGvHErpxDwoRBQgN5V9tTd79DChHdcC6frWdO6_t0e', start_index=6129)
Annotation(end_index=6635, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbmcyfds1N1KoI49_R-b6QxylT7ES3eRYAk7RYj-Hvu9IvIAkReYMwgwCkqRfWbPYIhpHvol_1XSioTukkBEPrac7v1icc1qunNC0ARPzUaG-TJoMCEDNjyMAC0tBgPJOvQqBMAEV9-qe0lSSlEchZakfmIpUvqHRhlaGs8TvyPBQhxInqfhc_-xEpJzzXljTddGYjas_FnKFGObP7H92XoL6_nQvBtLVkOr4=', start_index=6621)
Annotation(end_index=6635, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNIhdButtGOt7qEeJLtruDZZHPFnrsjOHpbBxJB6BkhyFR4IHzg-7CpXcpS2_bFUK1kac3taPYXiTxvXfAAVZd0wFQLhFzlNTggZYYqSU43lBdOQcULj5naUi7VF4zWyDxiv4wDYOA', start_index=6621)
Annotation(end_index=6955, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfn0y5TVlmM_Ug2eJDlsBPl8bc1LvncUaXtbgjRdM-PYABAeG3YpAPG_DPxwEeryTcLvAFs8uEsF8sPstqmyo7JSq6U3XfymuxT_LCvv0ULz4dtNYlDpY2z6Ttnz13Ofgjdl5KujCugIKLaS8Jms8uzvslWOkNQLEXbdEoRXVXn6rV98SG_eEqoylt3xXEqHzegA23Z8pUFN9tyjdZOzAg3HxKeEs=', start_index=6942)
Annotation(end_index=6955, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGezDtuFo9yqBs_QGcGz5YYqdqwfOtBFIf326r9oN8iujHxutPag8BwJMxvcqgHtGtEE3LcwL9-L6RkgO3FWAeLx_4iNrDUaT9xAE3hjdtMmVYk4ViyYyKPzUyGDHfgBQNlIyQ04ThYRqhLwafsiBAC18VcIIOa59RAFN_5lDb9Tizl-QpVQ9sCMIWSeh3oAvIMKdxWbD7gNgBw3apzpEpHVioqSv4zfHujK2cYoOZNpf9WmvHsWb1p8gz4FKx1TwVL8nCPh_9AhI8HMJ-es4tm', start_index=6942)
Annotation(end_index=7246, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFxm2DhehDvtGfBocuqXkJwZeRkTco2026sbHxHH7w6S2bwVRBDqbRSAYJs-c8CXUP_teXgXE3HyJp7DWZfkhCrtyJF4MUihYIyNHOnvEBPDA5MDNtqiFsuVHsbgmiefRJiaYPBQN2lz3BxdCJQvM21FL9Qw5erKK09GNpMfOlLw0HEVEnSpMujADaLROALZ7MLk1E84htB749uSYgvSnxG2kaOsm10F-zNFQTY9bf_VBbdUsSlfzWyTh_HOQb4YrcKvjKqqzw9s6Jjwt13DSecw__BCMVpJ-CEmj814QhYlIw32VTnQoF3kOq0PFG3gk42_GMPRVzmxxnLHrvfLwe6E4D3C89cjlcgUCdfQSPoEHRm-SVfCCxZeUC8vVVqav5k3O2I2HKMMdBq7rzQy7Z', start_index=7233)
Annotation(end_index=7246, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqEx7Qg1nuhJ0HKG15FKx_kNMrrTwPYAxmyok0bsJCxMwhvw4iHlVxJnVLmHEvHD2SYxrAMAC7prbzAFLLkQ8xzB5tgDQBPN4BL7S2-PzIZAqJgi-IxiERW24igD_Gj8kwiCs0hXhy7e0aSL-tEHroreWDxA==', start_index=7233)
Annotation(end_index=7669, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqEx7Qg1nuhJ0HKG15FKx_kNMrrTwPYAxmyok0bsJCxMwhvw4iHlVxJnVLmHEvHD2SYxrAMAC7prbzAFLLkQ8xzB5tgDQBPN4BL7S2-PzIZAqJgi-IxiERW24igD_Gj8kwiCs0hXhy7e0aSL-tEHroreWDxA==', start_index=7660)
Annotation(end_index=8206, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE495ga4WB2-ozX44LCrktaJ_y64R1CYuH6wlDGmbMyKG82lRvQq_JzUZbsRaJYCj8Cp37CHDQY0Q32aEreGg_R9-kzWyzzScq0I_Dwe0x-5Zfpm0VMiydb4l-fysinWtltr9KvpsY5d5vh37b6Md6PchOg0z-xVrD4xwfC1VKLoKDvtjsH6UP_A8QqJ3pkOzJA-994PvyXEdr2ZMU4M52VaCJt', start_index=8194)
Annotation(end_index=8206, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHaYtlTSEk8nrognEk45ZIjyA7wZ6PQzHgBDrMND4CnE5eju7c3ZZcdQxxI6030wBouqQ-rmC-WBWQV0JhN4P-xoZssdwZZdvpOUk1U51zRJ-rDgTwFYPUS8j4dbS4SPllFpnMM0t95d_ymH-Fwbi_43w-WYd_jWO-KPIbD_Lx_xXpYJ-tZsIV1lXODdhTlyPJBpntKlDC8bPMgg0=', start_index=8194)
Annotation(end_index=8721, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpmatE3GW-nOqGI7kni8DfISrfZrwR79nlSV0WSm9co_9KJicuJL1aVi4qt_aWquiswbkSVgVJF2j90BTk_PQ1Spxk-jeDfwjCdUAZ2pNy9TL-ZpjZSgKsAnkleR0XOrc_yJk=', start_index=8711)
Annotation(end_index=8930, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR9NDF1Yo1EkvZvHYs13nyoh5o8OzHSkE_WZUGDMk-b29_yQw9FbWfDJ2a70zvEDTHaYGN7tkC7LOlbaWasbVeY5we9VbD4Nvtz_B6gImJLbcOAPgxW1HzjPy3J7WJj3HwVYilZB2u_xPd9A85XdyT_H2sriJyigQg36-Wf-jg_4S3pjWtxg9IYFgOtbBxYHt2_vK0dfeg_lso5RJx6m--IQiEFaI-AH7RkeC9PC25hu0aP6HUwRovAxUULZJ9kF8nsZhJx9tl8Ts=', start_index=8920)
Annotation(end_index=9049, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENWlt4kB9NQ927q6PLULFYuMo7hJ-_roVk16DxuP8AqOXSNuupVH7A9KcVj8siTmKLtIlt54hRQuf5mOewz0bjxHeX1-E_lkFyZz56FHN-LQ9ZUIFGXlNRQcQ4xaaSMrbjG_NTnu4YezyJBjL0RbHl', start_index=9039)
Annotation(end_index=9277, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaViAoCEHX1vYNFWpH0jv-LKjasleRM0rqVOxHRFCCcI7iZLBXdveDz_1CqvsExjH_vOo4WkKT28p824v-tP-BlvUiPkmB-Grioaa_SFMaJUwc6JouG6F-avJ2YJnkR2zrnsh8yubbHOXI7HFT42iWKPJDYaePcv1LnA42uEbOdKNhZDJpDpztgJGpUreGYktYwzhnkvSmwCvZehNbmjDWLXLJGCvatc5dBHE=', start_index=9264)
Annotation(end_index=9277, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfn0y5TVlmM_Ug2eJDlsBPl8bc1LvncUaXtbgjRdM-PYABAeG3YpAPG_DPxwEeryTcLvAFs8uEsF8sPstqmyo7JSq6U3XfymuxT_LCvv0ULz4dtNYlDpY2z6Ttnz13Ofgjdl5KujCugIKLaS8Jms8uzvslWOkNQLEXbdEoRXVXn6rV98SG_eEqoylt3xXEqHzegA23Z8pUFN9tyjdZOzAg3HxKeEs=', start_index=9264)
Annotation(end_index=9763, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_xkdaEtLqXS9CsXPsgbLH392by_toh2kcE22LNWbmgPy8ksRcknKb3JDcr8tB-pN19l9_ZetwA1wjpg7WowRSSAW20RNxGuD9BJjz5x7J9RNOhVYz60I441ahI8YiTpn78HXquq0Po-FqTtJLDHGV6vBbGpYj8vv20qU=', start_index=9749)
Annotation(end_index=9763, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTcJL8WrHlnjgm6l3vwf0oo6XarYAqXpqiZPQK4p4BMZ5UXu1bqw1mrw8R9X4EGPWG7eLwwDi1zEohVfAsSveaagJZF6F7Gj7mpWzrEnrM55cbz-zQh0rXy7NBb5hzKBDpq8nZT-6MyDVHDbgkk2ev_IspVMy5FRbnjtHAXJ7tLGCzcA==', start_index=9749)
Annotation(end_index=10204, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtUIF5XJN22YT9GkIaVz41LMiirXtILwHpoKwXWKHHXXEtpONHEEXvX4UsBOSYW2RSbdiEyHMsvdgjXCT3iox99kbfpW4MkORLc1vlYAzJBSfPzEf41Fafy_8SIUUdgzVLIycuj3d3Kejk', start_index=10194)
Annotation(end_index=10704, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpvNCL1XdUNP8idoCBrFiIbqoADm1U54EsxusSFlngpi8znRNq8Cqw8CD_2dj5VV-yZRZjmI0HCpNLvqAYemtk-cKALt3R5p4KovmDtL3cO2ErcCzQJKfK9KkvgOrQh1zY2x5clcz4uC0JtaggvSHD42RcsUTrelUcQNPgNvzZSnnyhrCeUEfrpg==', start_index=10691)
Annotation(end_index=10704, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGy0yVmMRIg394P1McwaK_XB7gS0HrEiqYE5ZiM1XKc2oXMpFdpjpZ1o71UpbE7QEiS-7uwb8nvvy0nyFj82icvurxVpg8a4RQnRVvh7iDMbhsgR4_C_tln75VRu2-wojJkD4NwCMW1egRelGu1IDcWyBjYmfr_NmjC81IpPJrU-w-2qJZ1CoUnlg7XkaQ=', start_index=10691)
Annotation(end_index=11450, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfW0_n_7wOoyeyY_wwb86KRVK5wCFi4RPIc1VNx8bw77LnHbXV2TOMy_cvrpXeWY74v_2wXK2CayhlEOu35qtiBvGxqVgcwHznt2TIDMknaMgZLkyUAg==', start_index=11437)
Annotation(end_index=11450, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhoQESiiUnHzRjiAT4VhA-KG-yVlKRMDz6XGeAc3U3oJGhgfpIS6QFbxdxvOn8GRfbbQHHhHaapvzAQZ2PqeEQA3JODxqoV-GaD5GyJPeOPz7i2NX5WjxUvMTeUr9lBl4PFuY7Q_4hucJhVhB5I4n2iO6VqQabXM0kP-xHW9ede4PpDsN2jo3BEdc7XAjmqN03FtEY5O1l5-TLIXc=', start_index=11437)
Annotation(end_index=11895, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtu-SXwWZCLK2wY2pG_tBawjpNcXsFXJPqdM5JhkPFoyVxOnl9L_2yIOo61DSVfNRTJnrnyLsFOcfiZTagVYpFkL7oKXQV0thJt_Nb2T8Ao0MOK7PIUR63h50GvfJcbc6cjhLLcg8gWi087W0pVQB_X9uFBvZThAASfl-zn7fx7l-KWWM1pZ3m0_VyCx35Qy7e8UxZ', start_index=11885)
Annotation(end_index=12220, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMr2Pk5vlqkiddi51jNIGrp8thio8ktxGgP6uxnXegN7Fzk7t6__MW9737sk_uIRAJH-kNUtXj4rW1XX3tgmLvK7QaY0OS6QRKfwZO65M72mozFyzICWIX', start_index=12198)
Annotation(end_index=12220, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZctZJEPeue9xEcx9iRor8lNGrO-oQ8iNkmLCy-VM_yWnOp0FT0sdjidGdky6uK_Tjq-XDmOwIeQgydyy_NLmbTKyc8dN3NT4Q54dmi6qhf2f1tVcR-eNUYniMww8Zv0-nBATKuVo9LCvLTGNzrfHcVRx6NyMg20Cur1jOz4WWnEVx3GncOiRYuvK0akfj1iKJP0OVfI0_roTBbw==', start_index=12198)
Annotation(end_index=12220, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGg_VxY3Xuh_Dc_mm5YmhJSqpzwj9bbLhrBitwkeuRqZRiM72sGw501mPYzFkBV5AwL9z-TOhwifsz7URqGYQgM07He1PPREyDMZC4KTF6TAJ7K7LWsnNJAqTnurHdRQYxyf0t1xxXCK91T3g==', start_index=12198)
Annotation(end_index=12220, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuwx-VbCcnbQqqsVG38-HgBLB7NKNGl1mtz4hX71Eqho2Ze5LEaFfzBJw_EHw3lfixTi_i2tLlR0gj1dXqQJYkrIoBov_glhgQeNsRH2ObpjrCyNyRCby4DsjiivLUooYuyi0cM1UFMn1_SR1SbRK0Jz2XVCBbzPAHAvNp', start_index=12198)
Annotation(end_index=12889, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrgVJxxzwCZWArdDOWmzovyMFMmq4_O8ZV90gLXKTVxcAJ3A0EC2cr59C5ia5olywbqfJxRFiTjtjvzFDCRnC8qomtWImtPAfzz1WHc99FbdhQqid77ldWdSy3T99U2Oy8aRQzEWb7D_-X9bkQMFiL2OHxO_VB-upNtIX5B8KeYAGVczIefGRUHzG1ySILRZ4FtXXzjD5BRbmFj7SmYjvkoJye', start_index=12875)
Annotation(end_index=12889, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHo9a6D7yT8sHOPRIffLy8Mvzp2EOz1cbcPJvgl2Ox6oEJ0MdOb72YZOS9C3BcA6odz6pbppng8rYy0OgJvfUyv916QQIojJwUAPnT2fKlFPvTSiTKcNvb8yR73YcvY-iwlkib4Ixs9jwc6JhcjGoS1DaQABkmbrw==', start_index=12875)
Annotation(end_index=13089, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8YoJdpRMWdT0Mf3nUeBNsvgS44dml3cHm5i6kqmrrqJBwLb98A3zuUCmbzb3wkoTk356tDLhioKUQIQEn50W7LSlJu4L_eaRWK8dOnpiJfuOQnsctevl8naC6g72aN-GnHMVnID2_ZJt5cyEfcbsLo9IbBJac-DHF77btSD-NSzEnpBu7OuGkloaENdyhLGOB7-yK6L3ECgohTAh8', start_index=13079)
Annotation(end_index=13319, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJ6Z2fiHO_52wc9l9jZFHcfxK4j0hBnu-6X2W2tP_2RgRWEloHBFDg1FFzJlg9_shY9FrZAuLIN9hhXOCRbInXa-MCLVFRhEBzM4KJr1GjQmcHvtFowBiyfrxrDJAM0sYmShoSbbYLoWjBvQ==', start_index=13305)
Annotation(end_index=13319, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4-K-Jc08Pd_1sYYCK-1D-6YRJtkNavhHSfeNHgGtBSJkReubFiJuy3qFZ2GEDRFv178aijRHAiocWnO7GhjLIrAXcFzmy-WH5PeVMRwh9vVeUZntOFaweBPEKuh9X0HsQNrMVoHWqgP2s', start_index=13305)
Annotation(end_index=13702, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0jdimWrOhXHB_NiHu5R5gjp2W8_1k_gS8EyImQwWR10JdFC6_yJyIoqkBz03RoZCk5nw5qE64b6i0X-UgX_MgN92gm9z8okMXaQGZugW_MmxTvVPtYT4-rD_eF4EEItUvYobK2I2A633HFhBkFm5mwOcofknG', start_index=13688)
Annotation(end_index=13702, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3sv1bOMSwu3otKoDGF_M54rx9U-dXqw60PHNs1ja5RHAPCfrtVhqSXpd_L9LGXXnJ3Flqrz_KacU51eiUBelEjahK1blOi0pFyt99booIS3kwbq2Dj9AMLwynCDiwbI6gahveJ9cr-A-W0Fg2XAxAqIFxENKXSmAFSMrRu4cnDU2giIh6cbs-x79_KUSM9Mm52NBhVqGc0C1ItWo503ot0pLc_Ie13KUev4_xQZQWtLTGiU0cOCILYszqj-oyWtNIcyNz', start_index=13688)
Annotation(end_index=13946, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR9NDF1Yo1EkvZvHYs13nyoh5o8OzHSkE_WZUGDMk-b29_yQw9FbWfDJ2a70zvEDTHaYGN7tkC7LOlbaWasbVeY5we9VbD4Nvtz_B6gImJLbcOAPgxW1HzjPy3J7WJj3HwVYilZB2u_xPd9A85XdyT_H2sriJyigQg36-Wf-jg_4S3pjWtxg9IYFgOtbBxYHt2_vK0dfeg_lso5RJx6m--IQiEFaI-AH7RkeC9PC25hu0aP6HUwRovAxUULZJ9kF8nsZhJx9tl8Ts=', start_index=13936)
Annotation(end_index=14118, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwZAYzmRCQRDEIW6Q7QdwDrqL5m_UaVMnz8SKLrM7SiUYp-ZVLdfAhno7CllBZYktJJINth-Gr-HNbZmwMcRaZ0X8KEenCF2qZQS5YKdhiRyqh2FTO7jMviFdjJ-7sfxrVfirZbvB60IfhUkysCn8QIcOEoywT9HXPs8J7DPgBq5uqU8jyZqVlzQcYaa5Ne0Q=', start_index=14108)
Annotation(end_index=14530, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMJ2if4ab3fxYbDd9bh3-_BdPwvGS48Ujn8xyCgSDIo_zMUOaWC5TssUEOjMlwVIxTYex6N__jDunMLMnN40xPlSdmYNp6Kl_cWOJrPLDtDp4nv7Q0ek_aNafSZONxQ2RMQ_TZ', start_index=14516)
Annotation(end_index=14530, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtUIF5XJN22YT9GkIaVz41LMiirXtILwHpoKwXWKHHXXEtpONHEEXvX4UsBOSYW2RSbdiEyHMsvdgjXCT3iox99kbfpW4MkORLc1vlYAzJBSfPzEf41Fafy_8SIUUdgzVLIycuj3d3Kejk', start_index=14516)
Annotation(end_index=14822, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtUIF5XJN22YT9GkIaVz41LMiirXtILwHpoKwXWKHHXXEtpONHEEXvX4UsBOSYW2RSbdiEyHMsvdgjXCT3iox99kbfpW4MkORLc1vlYAzJBSfPzEf41Fafy_8SIUUdgzVLIycuj3d3Kejk', start_index=14812)
Annotation(end_index=15123, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuwx-VbCcnbQqqsVG38-HgBLB7NKNGl1mtz4hX71Eqho2Ze5LEaFfzBJw_EHw3lfixTi_i2tLlR0gj1dXqQJYkrIoBov_glhgQeNsRH2ObpjrCyNyRCby4DsjiivLUooYuyi0cM1UFMn1_SR1SbRK0Jz2XVCBbzPAHAvNp', start_index=15113)
Annotation(end_index=15276, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR9NDF1Yo1EkvZvHYs13nyoh5o8OzHSkE_WZUGDMk-b29_yQw9FbWfDJ2a70zvEDTHaYGN7tkC7LOlbaWasbVeY5we9VbD4Nvtz_B6gImJLbcOAPgxW1HzjPy3J7WJj3HwVYilZB2u_xPd9A85XdyT_H2sriJyigQg36-Wf-jg_4S3pjWtxg9IYFgOtbBxYHt2_vK0dfeg_lso5RJx6m--IQiEFaI-AH7RkeC9PC25hu0aP6HUwRovAxUULZJ9kF8nsZhJx9tl8Ts=', start_index=15266)
Annotation(end_index=15557, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbmcyfds1N1KoI49_R-b6QxylT7ES3eRYAk7RYj-Hvu9IvIAkReYMwgwCkqRfWbPYIhpHvol_1XSioTukkBEPrac7v1icc1qunNC0ARPzUaG-TJoMCEDNjyMAC0tBgPJOvQqBMAEV9-qe0lSSlEchZakfmIpUvqHRhlaGs8TvyPBQhxInqfhc_-xEpJzzXljTddGYjas_FnKFGObP7H92XoL6_nQvBtLVkOr4=', start_index=15543)
Annotation(end_index=15557, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGbwIPIZftrXjUN2LYBM3W1R5_itHlRKmlLNbouZz8GQR8SWDY2OgZRsy4G2hE3tiKCUxEBw0PElb2AKNUKzSI3O2cTjhCnE3zDYi9VV6pLxaPjXWilEhK9QtbV3_Fg5rcjtRzVhCMmKlZsotY=', start_index=15543)
Annotation(end_index=15770, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3QdrI_XZgIfUrBXT1hv9nn_yi3MWcXdt65qKGoLHyGvDnyq7ytPsCCarys95_3BCSty1vbIwrWGpeQHm7au-BDLqxMdSuc-e2nJsajuIgfn8iIOe4-k7eCcjclY9mvBHIQjsKOgrWQR9P76W7vQ==', start_index=15756)
Annotation(end_index=15770, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8YoJdpRMWdT0Mf3nUeBNsvgS44dml3cHm5i6kqmrrqJBwLb98A3zuUCmbzb3wkoTk356tDLhioKUQIQEn50W7LSlJu4L_eaRWK8dOnpiJfuOQnsctevl8naC6g72aN-GnHMVnID2_ZJt5cyEfcbsLo9IbBJac-DHF77btSD-NSzEnpBu7OuGkloaENdyhLGOB7-yK6L3ECgohTAh8', start_index=15756)
Annotation(end_index=16732, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9I8nRvS7LUiyImBx8pu58FOtC_YUManJToqPv4BUzZy8loy5ueCISq1QfsOG_NlqEdVUHoc0ZRsRULBShCcEpu9Opo5iSLHAYFUGSqwf-FFFNCxN4KdiZFbeZlkhGFm07QU8RCXTWsP-ovEXQSa6CO6SFSf-y7p_P', start_index=16716)
Annotation(end_index=16732, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaHEqpVwn7sGoTyHAhXBAPI_cj_bF0qmQXs3vQUwj6Jz9gANTA41XkeFsYW6nYzTSTkpc3KTFEXHVaL28gEuHUadNbbBkEWwM9BSEoCP8ZY0P49xlT2DWwulYJaTlAHjw-Lu0wpquBxWyLtKj9xZpZi75jnB9SGrJRZfamuJnRrQ==', start_index=16716)
Annotation(end_index=16732, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqTC3qym66BbgcqxWnfo199YLG1ekTlHJZ6vA5Wk4kg5aYXqJ3pSXJkqrurZ6Zo-l5l55UMKm96G4atBBYYH4f-C0f7IrWzcJHHXnhuKcItQvWkuqyKbK_bU9P0YICSsVHemD3ovdE2SfXoHzfR-rfDk_IKmLjqnW-fA==', start_index=16716)
Annotation(end_index=16828, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFShoyH6nMFEg-Z_jgkU3HgwV4gO859FIQghUTyaaC6L_Jbb4ZFtgqj1rG9YPkH03FXsIIzvhx8xSsqkEMrKNfp9WAKyHan3EPem4vDzWQqNqcpLQpjbzclLklCQwIskAnp', start_index=16810)
Annotation(end_index=16828, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGa7qLmxfNSX6x-37qtO1QRf0Q8Th2ZOh2eJ6W5fmQR-5L3yBd13ZtStVTLmg-9O8p4WRYSd3w4n09PaIoNP6_ll8HSLiSoN9rxo3xfIBPxMhrAzFdBYRdgK5y8Q0JwrVYGvHErpxDwoRBQgN5V9tTd79DChHdcC6frWdO6_t0e', start_index=16810)
Annotation(end_index=16828, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLf7aUwrwR5aXgsUJlL9zxSgIH2eZYn33pBeBeS7DmmSNhK90g5Ct6gfqMMl0-_LOPsu3lXjAD3RRzD-y4VAf84efr08RxPGqLWwmBkD1ZNYGfTlKhpWJVOsal2NShRoYUZtoXQxJBVNQh', start_index=16810)
Annotation(end_index=16924, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE495ga4WB2-ozX44LCrktaJ_y64R1CYuH6wlDGmbMyKG82lRvQq_JzUZbsRaJYCj8Cp37CHDQY0Q32aEreGg_R9-kzWyzzScq0I_Dwe0x-5Zfpm0VMiydb4l-fysinWtltr9KvpsY5d5vh37b6Md6PchOg0z-xVrD4xwfC1VKLoKDvtjsH6UP_A8QqJ3pkOzJA-994PvyXEdr2ZMU4M52VaCJt', start_index=16908)
Annotation(end_index=16924, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHaYtlTSEk8nrognEk45ZIjyA7wZ6PQzHgBDrMND4CnE5eju7c3ZZcdQxxI6030wBouqQ-rmC-WBWQV0JhN4P-xoZssdwZZdvpOUk1U51zRJ-rDgTwFYPUS8j4dbS4SPllFpnMM0t95d_ymH-Fwbi_43w-WYd_jWO-KPIbD_Lx_xXpYJ-tZsIV1lXODdhTlyPJBpntKlDC8bPMgg0=', start_index=16908)
Annotation(end_index=16924, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpmatE3GW-nOqGI7kni8DfISrfZrwR79nlSV0WSm9co_9KJicuJL1aVi4qt_aWquiswbkSVgVJF2j90BTk_PQ1Spxk-jeDfwjCdUAZ2pNy9TL-ZpjZSgKsAnkleR0XOrc_yJk=', start_index=16908)
Annotation(end_index=17009, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaViAoCEHX1vYNFWpH0jv-LKjasleRM0rqVOxHRFCCcI7iZLBXdveDz_1CqvsExjH_vOo4WkKT28p824v-tP-BlvUiPkmB-Grioaa_SFMaJUwc6JouG6F-avJ2YJnkR2zrnsh8yubbHOXI7HFT42iWKPJDYaePcv1LnA42uEbOdKNhZDJpDpztgJGpUreGYktYwzhnkvSmwCvZehNbmjDWLXLJGCvatc5dBHE=', start_index=16992)
Annotation(end_index=17009, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfn0y5TVlmM_Ug2eJDlsBPl8bc1LvncUaXtbgjRdM-PYABAeG3YpAPG_DPxwEeryTcLvAFs8uEsF8sPstqmyo7JSq6U3XfymuxT_LCvv0ULz4dtNYlDpY2z6Ttnz13Ofgjdl5KujCugIKLaS8Jms8uzvslWOkNQLEXbdEoRXVXn6rV98SG_eEqoylt3xXEqHzegA23Z8pUFN9tyjdZOzAg3HxKeEs=', start_index=16992)
Annotation(end_index=17009, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTcJL8WrHlnjgm6l3vwf0oo6XarYAqXpqiZPQK4p4BMZ5UXu1bqw1mrw8R9X4EGPWG7eLwwDi1zEohVfAsSveaagJZF6F7Gj7mpWzrEnrM55cbz-zQh0rXy7NBb5hzKBDpq8nZT-6MyDVHDbgkk2ev_IspVMy5FRbnjtHAXJ7tLGCzcA==', start_index=16992)
Annotation(end_index=17085, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpvNCL1XdUNP8idoCBrFiIbqoADm1U54EsxusSFlngpi8znRNq8Cqw8CD_2dj5VV-yZRZjmI0HCpNLvqAYemtk-cKALt3R5p4KovmDtL3cO2ErcCzQJKfK9KkvgOrQh1zY2x5clcz4uC0JtaggvSHD42RcsUTrelUcQNPgNvzZSnnyhrCeUEfrpg==', start_index=17069)
Annotation(end_index=17085, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGy0yVmMRIg394P1McwaK_XB7gS0HrEiqYE5ZiM1XKc2oXMpFdpjpZ1o71UpbE7QEiS-7uwb8nvvy0nyFj82icvurxVpg8a4RQnRVvh7iDMbhsgR4_C_tln75VRu2-wojJkD4NwCMW1egRelGu1IDcWyBjYmfr_NmjC81IpPJrU-w-2qJZ1CoUnlg7XkaQ=', start_index=17069)
Annotation(end_index=17085, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfW0_n_7wOoyeyY_wwb86KRVK5wCFi4RPIc1VNx8bw77LnHbXV2TOMy_cvrpXeWY74v_2wXK2CayhlEOu35qtiBvGxqVgcwHznt2TIDMknaMgZLkyUAg==', start_index=17069)
Annotation(end_index=17169, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZctZJEPeue9xEcx9iRor8lNGrO-oQ8iNkmLCy-VM_yWnOp0FT0sdjidGdky6uK_Tjq-XDmOwIeQgydyy_NLmbTKyc8dN3NT4Q54dmi6qhf2f1tVcR-eNUYniMww8Zv0-nBATKuVo9LCvLTGNzrfHcVRx6NyMg20Cur1jOz4WWnEVx3GncOiRYuvK0akfj1iKJP0OVfI0_roTBbw==', start_index=17151)
Annotation(end_index=17169, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGg_VxY3Xuh_Dc_mm5YmhJSqpzwj9bbLhrBitwkeuRqZRiM72sGw501mPYzFkBV5AwL9z-TOhwifsz7URqGYQgM07He1PPREyDMZC4KTF6TAJ7K7LWsnNJAqTnurHdRQYxyf0t1xxXCK91T3g==', start_index=17151)
Annotation(end_index=17169, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuwx-VbCcnbQqqsVG38-HgBLB7NKNGl1mtz4hX71Eqho2Ze5LEaFfzBJw_EHw3lfixTi_i2tLlR0gj1dXqQJYkrIoBov_glhgQeNsRH2ObpjrCyNyRCby4DsjiivLUooYuyi0cM1UFMn1_SR1SbRK0Jz2XVCBbzPAHAvNp', start_index=17151)
Annotation(end_index=17251, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFxm2DhehDvtGfBocuqXkJwZeRkTco2026sbHxHH7w6S2bwVRBDqbRSAYJs-c8CXUP_teXgXE3HyJp7DWZfkhCrtyJF4MUihYIyNHOnvEBPDA5MDNtqiFsuVHsbgmiefRJiaYPBQN2lz3BxdCJQvM21FL9Qw5erKK09GNpMfOlLw0HEVEnSpMujADaLROALZ7MLk1E84htB749uSYgvSnxG2kaOsm10F-zNFQTY9bf_VBbdUsSlfzWyTh_HOQb4YrcKvjKqqzw9s6Jjwt13DSecw__BCMVpJ-CEmj814QhYlIw32VTnQoF3kOq0PFG3gk42_GMPRVzmxxnLHrvfLwe6E4D3C89cjlcgUCdfQSPoEHRm-SVfCCxZeUC8vVVqav5k3O2I2HKMMdBq7rzQy7Z', start_index=17238)
Annotation(end_index=17251, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqEx7Qg1nuhJ0HKG15FKx_kNMrrTwPYAxmyok0bsJCxMwhvw4iHlVxJnVLmHEvHD2SYxrAMAC7prbzAFLLkQ8xzB5tgDQBPN4BL7S2-PzIZAqJgi-IxiERW24igD_Gj8kwiCs0hXhy7e0aSL-tEHroreWDxA==', start_index=17238)
Annotation(end_index=17337, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtUIF5XJN22YT9GkIaVz41LMiirXtILwHpoKwXWKHHXXEtpONHEEXvX4UsBOSYW2RSbdiEyHMsvdgjXCT3iox99kbfpW4MkORLc1vlYAzJBSfPzEf41Fafy_8SIUUdgzVLIycuj3d3Kejk', start_index=17327)

## Sources
