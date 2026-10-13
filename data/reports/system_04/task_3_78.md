# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 96b27ec8 | **Time:** 268.09s | **Cost:** $1.28990
--------------------------------------------------------------------------------

# Determination of Attribution Weights in Purchase Conversion Models

**Key Points**
*   **Attribution Weight Definition:** Attribution weights represent the proportional credit assigned to specific marketing touchpoints (e.g., ads, emails, social posts) for generating a conversion.
*   **Methodological Divide:** Approaches are categorized into **Heuristic (Rule-Based)** models, which use predetermined, static weights (e.g., First-Touch, Time-Decay), and **Data-Driven (Algorithmic)** models, which dynamically calculate weights based on observed performance and interaction patterns.
*   **Game Theory (Shapley Value):** Determines weights by calculating the average marginal contribution of a channel across all possible permutations of the customer journey, ensuring a "fair" distribution based on cooperative game theory axioms.
*   **Probabilistic Models (Markov Chains):** Models the customer journey as a directed graph of states. Weights are determined via the **Removal Effect**, which measures the drop in global conversion probability when a specific channel is removed from the graph.
*   **Regression & Survival Analysis:** Statistical methods like Logistic Regression and Cox Proportional Hazards derive weights from regression coefficients ($\beta$) or hazard ratios, quantifying the change in conversion probability or speed associated with channel exposure.
*   **Machine Learning (Random Forest):** Uses ensemble decision trees to determine weights based on **Feature Importance** metrics, such as Mean Decrease in Impurity (Gini) or Permutation Importance.

## 1. Introduction to Attribution Weight Determination

In the domain of marketing analytics, the determination of attribution weights is the fundamental mathematical challenge of Multi-Touch Attribution (MTA). It seeks to solve the "credit assignment problem": given a conversion event $C$ that was preceded by a sequence of marketing interactions $I = \{i_1, i_2, ..., i_n\}$, how should the total value $V$ of the conversion be distributed among the interactions such that the sum of assigned weights equals the total value?

The determination of these weights is critical for budget allocation, calculating Return on Ad Spend (ROAS), and optimizing the marketing mix. Historically, this was achieved through simplistic heuristics. However, the field has shifted toward probabilistic and algorithmic methodologies that utilize historical data to infer causal or correlational weights [cite: 1, 2].

This report provides an exhaustive analysis of the mathematical and theoretical frameworks used to determine these weights, contrasting rigid rule-based systems with dynamic data-driven architectures including Cooperative Game Theory, Markov Chains, and advanced regression techniques.

## 2. Heuristic and Rule-Based Weight Determination

Heuristic models, often referred to as "prescriptive" or "static" models, determine attribution weights based on fixed, predetermined logic sets. These weights are not derived from the dataset's intrinsic patterns but are imposed by the marketer based on assumptions regarding the customer journey [cite: 1, 3].

### 2.1 Single-Touch Weighting
Single-touch models assign a binary weight of 100% (or 1.0) to a single interaction and 0% to all others.
*   **Last Interaction (Last-Click):** The weight $w_n = 1$ is assigned to the final touchpoint $t_n$ immediately preceding the conversion. All prior touchpoints $t_{1}...t_{n-1}$ receive $w = 0$. This assumes the closing action is the sole driver of value [cite: 2, 4].
*   **First Interaction (First-Click):** The weight $w_1 = 1$ is assigned to the initial touchpoint $t_1$. This assumes the introductory channel deserves full credit for initiating the funnel [cite: 2, 5].

### 2.2 Multi-Touch Heuristic Weighting
Multi-touch heuristics distribute fractional weights across multiple events in the path $P$.

#### 2.2.1 Linear Attribution
The Linear model assigns equal weight to every touchpoint in the conversion path. For a path of length $N$, the weight for any channel $i$ is determined as:
\[ w_i = \frac{1}{N} \]
This method assumes that every interaction contributes equally to the purchase decision, regardless of its position or nature [cite: 2, 3].

#### 2.2.2 Time Decay Attribution
Time Decay models determine weights based on the temporal proximity of the touchpoint to the conversion event. The assumption is that interactions closer to the conversion had a greater influence. The weight is typically calculated using an exponential decay half-life formula:
\[ w(t) \propto 2^{-t/HL} \]
Where $t$ is the time difference between the interaction and the conversion, and $HL$ is the half-life parameter (e.g., 7 days). Weights are normalized so that $\sum w_i = 1$. This approach is favored for short sales cycles but may undervalue early funnel activities in B2B contexts [cite: 6, 7, 8].

#### 2.2.3 Position-Based (U-Shaped) Attribution
This model determines weights based on the ordinal position of the touchpoint. A standard U-shaped configuration assigns:
*   **First Touch ($t_1$):** 40% weight ($0.4$).
*   **Last Touch ($t_n$):** 40% weight ($0.4$).
*   **Middle Touches ($t_2...t_{n-1}$):** The remaining 20% ($0.2$) is distributed linearly among intermediate events.
This heuristic attempts to balance the importance of acquisition (first touch) and closing (last touch) while acknowledging the nurturing phase [cite: 3, 9, 10].

## 3. Algorithmic and Data-Driven Weight Determination

Unlike heuristics, data-driven attribution (DDA) models utilize statistical algorithms and machine learning to calculate weights based on observed correlations and causal relationships within the data. These models analyze both converting and non-converting paths to assess the true contribution of each channel [cite: 1, 11, 12].

### 3.1 Cooperative Game Theory: The Shapley Value
The Shapley Value is widely regarded as the most theoretically robust method for attribution, satisfying axioms of fairness (efficiency, symmetry, dummy, and additivity). It treats marketing channels as players in a cooperative game where the "payoff" is the conversion [cite: 4, 13, 14, 15].

#### 3.1.1 Mathematical Determination of Weights
The Shapley Value $\phi_i(v)$ for a channel $i$ is calculated by averaging its **marginal contribution** across all possible permutations of the coalition of channels.

The formula is defined as:
\[ \phi_i(v) = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|! (n-|S|-1)!}{n!} (v(S \cup \{i\}) - v(S)) \]

Where:
*   $N$: The set of all marketing channels.
*   $n$: The total number of channels ($|N|$).
*   $S$: A subset (coalition) of channels excluding $i$.
*   $v(S)$: The characteristic function, representing the total value (e.g., conversion rate or revenue) generated by the coalition $S$.
*   $v(S \cup \{i\}) - v(S)$: The **marginal contribution** of channel $i$ when added to coalition $S$ [cite: 14, 16, 17].

#### 3.1.2 Calculation Process
1.  **Coalition Enumeration:** Identify all possible subsets of channels (e.g., {Email}, {Search}, {Email, Search}).
2.  **Characteristic Function Evaluation:** Calculate the conversion rate $v(S)$ for each subset using historical data.
3.  **Marginal Contribution:** For every subset $S$ not containing channel $i$, calculate the difference in conversion rate when $i$ is added.
4.  **Weighted Averaging:** Average these marginal contributions, weighted by the probability of that specific coalition occurring (represented by the factorials in the formula).
5.  **Normalization:** The resulting Shapley values are normalized to sum to the total conversion value, providing the final attribution weights [cite: 13, 17].

This method ensures that a channel is weighted based on its incremental impact. If a channel adds no value to any coalition (marginal contribution is zero), its weight is zero (Dummy axiom) [cite: 17, 18].

### 3.2 Probabilistic Graph Models: Markov Chains
Markov Chain attribution models the customer journey as a sequence of states (touchpoints) in a directed graph. The determination of weights relies on the concept of the **Removal Effect** [cite: 13, 14, 19, 20].

#### 3.2.1 Transition Matrix Construction
The model first calculates a transition probability matrix $M$, where each entry $p_{ij}$ represents the probability of a user moving from channel $i$ to channel $j$.
\[ p_{ij} = \frac{\text{Count}(i \to j)}{\text{Count}(i)} \]
This matrix captures the dynamic flow of users through the funnel, including loops and sequential dependencies [cite: 8, 21, 22].

#### 3.2.2 The Removal Effect Methodology
The attribution weight for a specific channel $C$ is determined by simulating the impact of its absence:
1.  **Baseline Probability:** Calculate the total probability of conversion $P(Conv_{total})$ starting from the "Start" state to the "Conversion" state using the full transition matrix.
2.  **Removal Simulation:** "Remove" channel $C$ from the graph. This is mathematically achieved by setting all transitions to and from $C$ to zero (or redirecting them to a "Null" or "Exit" state).
3.  **Recalculation:** Calculate the new probability of conversion $P(Conv_{\neg C})$ on this reduced graph.
4.  **Removal Effect Calculation:** The removal effect $R_C$ is the proportional drop in conversion probability:
    \[ R_C = 1 - \frac{P(Conv_{\neg C})}{P(Conv_{total})} \]
5.  **Weight Normalization:** The final attribution weight $W_C$ is the removal effect of channel $C$ divided by the sum of removal effects for all channels:
    \[ W_C = \frac{R_C}{\sum_{k \in Channels} R_k} \]

This method assigns higher weights to channels that act as critical "bridges" in the graph; if their removal causes the path to conversion to break significantly, they receive a higher attribution weight [cite: 19, 20, 22, 23, 24].

### 3.3 Regression-Based Weight Determination
Logistic Regression is a common statistical approach for determining attribution weights, particularly when analyzing the binary outcome of conversion (1) vs. non-conversion (0) [cite: 8, 10, 25, 26].

#### 3.3.1 Logistic Regression Coefficients
The model estimates the log-odds of conversion as a linear combination of channel exposures:
\[ \ln\left(\frac{P(Y=1)}{1-P(Y=1)}\right) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + ... + \beta_n x_n \]
Where:
*   $x_i$: Binary indicator (1 if exposed to channel $i$, 0 otherwise) or frequency count.
*   $\beta_i$: The regression coefficient for channel $i$.

#### 3.3.2 Interpreting Coefficients as Weights
The coefficient $\beta_i$ represents the change in the log-odds of conversion associated with exposure to channel $i$.
*   **Positive $\beta$:** Indicates the channel increases conversion probability.
*   **Weight Derivation:** Weights are often derived directly from the standardized coefficients or by converting coefficients to Odds Ratios ($OR = e^{\beta_i}$).
*   **Marginal Effects:** In more advanced applications, the "average marginal effect" is calculated to determine the discrete change in probability $P(Y=1)$ for a unit change in $x_i$, providing a more intuitive weight than the raw log-odds coefficient [cite: 27, 28, 29, 30].

**Bagging (Bootstrap Aggregating):** To stabilize the weights and handle multicollinearity (where channels are highly correlated), marketers often use Bagging. This involves training the logistic regression on multiple random subsets of the data and averaging the coefficients to determine the final attribution weight [cite: 8].

### 3.4 Survival Analysis (Time-to-Event)
Survival analysis determines weights by modeling the *time* until conversion, rather than just the binary outcome. This accounts for "censored" data (users who have not converted *yet* but might in the future) [cite: 8, 31, 32].

#### 3.4.1 Cox Proportional Hazards Model
The hazard function $h(t)$ (instantaneous rate of conversion) is modeled as:
\[ h(t|X) = h_0(t) \exp(\beta_1 x_1 + ... + \beta_n x_n) \]
Here, the coefficients $\beta_i$ determine the **Hazard Ratio (HR)**.
*   **Hazard Ratio ($e^{\beta_i}$):** If $HR > 1$, exposure to the channel increases the speed/likelihood of conversion.
*   **Weight Determination:** The attribution weight is proportional to the channel's ability to accelerate the conversion event. Channels with higher hazard ratios are assigned greater credit because they significantly shorten the time-to-conversion [cite: 33, 34, 35, 36, 37].

### 3.5 Machine Learning Ensembles: Random Forest
Random Forest models determine attribution weights through **Feature Importance** metrics. The model builds an ensemble of decision trees to predict conversion [cite: 38, 39].

#### 3.5.1 Feature Importance Metrics
1.  **Mean Decrease Impurity (Gini Importance):** Measures how much a feature (channel) decreases the weighted impurity (e.g., Gini or Entropy) across all trees in the forest. When a node splits based on channel $X$, the decrease in impurity is attributed to $X$. The sum of these decreases, averaged over all trees, determines the weight [cite: 39, 40, 41].
2.  **Permutation Importance (Mean Decrease Accuracy):**
    *   Measure the baseline accuracy of the model.
    *   Randomly shuffle the values of channel $X$ (breaking its relationship with the outcome).
    *   Measure the drop in model accuracy.
    *   **Weight Determination:** A large drop in accuracy implies the channel is highly important for predicting conversion. The magnitude of the accuracy drop serves as the attribution weight [cite: 39, 40, 42].

## 4. Comparative Analysis of Weight Determination Methodologies

| Methodology | Basis of Weight Determination | Key Metric | Strengths | Weaknesses |
| :--- | :--- | :--- | :--- | :--- |
| **Heuristic** | Pre-defined rules | Position / Time | Simple, transparent, easy to implement [cite: 11, 43]. | Subjective, ignores data patterns, lacks causality [cite: 1, 3]. |
| **Shapley Value** | Cooperative Game Theory | Marginal Contribution | Theoretically fair, accounts for order and presence/absence [cite: 14]. | Computationally expensive ($2^n$ complexity), assumes all combinations are valid [cite: 3, 17]. |
| **Markov Chains** | Graph Theory / Probability | Removal Effect | Captures sequence and structural importance, handles loops [cite: 19, 20]. | Can overvalue high-traffic nodes, "memoryless" assumption (Markov property) [cite: 23, 44]. |
| **Logistic Regression** | Statistical Correlation | Coefficient ($\beta$) / Log-Odds | Well-understood, provides statistical significance tests [cite: 25, 26]. | Struggles with multicollinearity, assumes linear relationship with log-odds [cite: 27, 29]. |
| **Survival Analysis** | Time-to-Event | Hazard Ratio | Accounts for time and censoring (incomplete journeys) [cite: 8, 31]. | Complex data preparation, assumes proportional hazards [cite: 32, 36]. |
| **Random Forest** | Ensemble Learning | Gini / Permutation Importance | Handles non-linear interactions and high dimensionality [cite: 38]. | "Black box" nature, bias toward high-cardinality features [cite: 40, 45]. |

## 5. Implementation and Calculation Nuances

### 5.1 The Role of Propensity Scoring
Propensity models are often used in conjunction with attribution to adjust weights based on the user's baseline likelihood to convert.
*   **Weight Adjustment:** If a user had a 90% propensity to convert regardless of marketing, the attribution weights for subsequent ads might be dampened (down-weighted) to avoid over-crediting marketing for "sure thing" conversions.
*   **Inverse Probability Weighting (IPW):** Used to create a synthetic sample where treatment assignment is independent of covariates, allowing for causal weight estimation [cite: 45, 46, 47, 48].

### 5.2 Handling Multicollinearity in Regression
In regression-based attribution, marketing channels are often highly correlated (e.g., a user seeing a Facebook ad is also likely to see a Google ad). This makes coefficient estimates ($\beta$) unstable.
*   **Regularization (Ridge/Lasso):** Techniques like Ridge Regression (L2 regularization) are applied to constrain coefficients, preventing them from exploding and allowing for more stable weight determination [cite: 49].

### 5.3 Computational Complexity in Shapley
Calculating the exact Shapley value requires iterating through $2^n$ coalitions, which is computationally infeasible for campaigns with many touchpoints.
*   **Approximation Methods:** Monte Carlo sampling is used to approximate the Shapley value by sampling a subset of permutations rather than calculating the exhaustive set, allowing for weight determination in polynomial time [cite: 18, 22].

## 6. Conclusion

The determination of attribution weights has evolved from arbitrary rule-setting to sophisticated estimation problems involving counterfactual reasoning. While heuristic models remain in use for their simplicity, the industry standard for accuracy has shifted to **Shapley Values** and **Markov Chains**. These methods determine weights by rigorously simulating the *absence* of a channel (marginal contribution or removal effect), thereby isolating the incremental value generated by specific marketing efforts. Advanced implementations further refine these weights using **Survival Analysis** to account for temporal dynamics and **Random Forests** to capture complex, non-linear interactions between touchpoints.

### References
[cite: 1] Attribute This. (n.d.). Demystifying Data-Driven Attribution Models.
[cite: 2] Internetrix. (n.d.). Types of Attribution.
[cite: 11, 43] HockeyStack. (2024). Different Attribution Models.
[cite: 6] Corvidae. (2023). Attribution Models.
[cite: 3] Factors.ai. (n.d.). Types of Attribution Models.
[cite: 4, 16] Lebesgue. (2024). Attribution Modeling Methods.
[cite: 12] Google Support. (n.d.). Data-driven attribution.
[cite: 9] Usermaven. (2025). How to measure marketing attribution.
[cite: 13] Koehn.ai. (2021). Dynamic Marketing Attribution Modelling: Markov Chain and Shapley Value.
[cite: 19] Adequate Digital. (n.d.). Markov Chain Attribution Modeling.
[cite: 14] Boolean Maths. (2024). A Deep Dive into Attribution Maths.
[cite: 21] Windsor.ai. (2025). Shapley Value vs Markov Model.
[cite: 5] Adobe. (2025). Marketing Attribution Explained.
[cite: 49] Towards Data Science. (2022). Modeling Marketing Mix with Constrained Coefficients.
[cite: 10] Medium. (2023). Data Science in Training: MMM and MTA.
[cite: 20] RedTrack. (2025). Markov Chain Attribution Model.
[cite: 22] Mister Spex Tech. (2022). How to calculate removal effects in Markov attribution.
[cite: 15] The Data Cherry. (n.d.). Understanding Attribution Model: Shapley Value.
[cite: 17] LeadSources. (2026). Shapley Value Attribution.
[cite: 38] Medium. (2023). Random Forest in Marketing Strategy.
[cite: 39] GeeksforGeeks. (2025). Feature Importance with Random Forests.
[cite: 25] Bookdown. (n.d.). Interpretation of Regression Coefficients.
[cite: 27] Quora. (2020). How do you interpret weights in logistic regression.
[cite: 46] Databricks. (2022). Personalization through Propensity Scoring.
[cite: 33] Statistics By Jim. (n.d.). Hazard Ratio.
[cite: 31] Arxiv. (2020). Survival Analysis for Attribution.
[cite: 8] Internetrix. (n.d.). Attribution Methods: Survival Analysis.
[cite: 26] Statsig. (2025). Marketing Attribution Models Tech Survey.
[cite: 8] Internetrix. (n.d.). Logistic Regression in Attribution.
[cite: 18] Arxiv. (2018). Shapley Value Method for Attribution Modeling.
[cite: 40] MLJAR. (2020). Feature Importance in Random Forest.

**Sources:**
1. [attributethis.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJnWS9CC4wu6CHBu-bc60D6Kt1oaz3PKtpkm1GqwvpeioBtH1kKGnkVgsWtQLswjBTGjnQf9GPYRN4LYwhqeCHV6xLQkIm5vgwRIo3wCEKij-lg5f4rHuO3j22P3exsh1FmT7PMefKolRleHT3SNE1lFWBC4cMCj9y)
2. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFnAAe8CkDdhPMEjITc3M3_WzoJRj6nLNU6MYUSNIR65VFrEKwirJTfErzfs_lG3XJq0gfUU_Rt3aVg0ZW_d7A3qWZ-jmcz6M-CPSgO_YWGwfXLHH4UwyPlc-xwoe5QRI0QBlwjCtC7x0XZismok8NUeQQsG9GLRXqQX6FW6FFIJo1)
3. [factors.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPGMi7RGr1q1XhdNRzzQhNawuYra4MSSFxeVadRW5QEsfOAvd0jDkFGXmk0dpqJv-thvQ3Qfj6VBl8LmK7_Jz7rvWot6C7XUa98s19Gbpnu3Q9VFy7qyHH6zRa4cW55-_ehyX3ZFwN47jkPmQ=)
4. [lebesgue.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHdNAKAumDSf0rfs8JQSrsBtQ1Q5QqIaVtl8_8BKeGUkGZaASmFiHEN2NuXDLl2Bs9gQOLFqqu8JKw88sSp8Jc7X8TWYGVgNezzzfia1XtyTXjmXM3Eq6Kc-Wt81qasoK2IlzLUQduqFspdKvlV-avZ_oI-ZhxFhbFwNrbLziGmERO2gVLn-tBpyRszH5rh71J)
5. [adobe.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsDyr-bXiCI5N4DZGyQFsLiTf7kW3aAIJRi1tvnsKe2bQOzqIoM3KoUi8Q-NPDpEMy3C13ecFncKEicSLXZ0yPy5KrSaLHUx1ff61J72STOYGnSqiN-zYHSVq2LdlUTWiWgIeV-RUxmIE-_7qMlN61VA==)
6. [corvidae.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFapy5V8jBp4rR7GuhLawljFoVQSA1CpiHuU9yomMgpw9qf4qRUAZOhOpYq0M37z84xkU_O_sJSIplPXXKRshRdn5TD-0cd7CmQ5HC8zaUREUB0Xl2ji9WZwampzIN6ppnS)
7. [growth-onomics.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWI2eEiVa8dwJhL7jeuiGeL2qKdFsntlIAe892d85KwT3_eAqhsHFgBweAP1PUXt9-FOWS4hgOBEo2R6lybcjrBAVr5pLnOdN4zqo6INphVUGslbJap3KRPolGBE3Z6-dCzxSZJy2VZPpsnAtWZyDa)
8. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsRq9nzQn9aYb8Bdk9ZZXrjPRcu9fzri4GY7MDxKxbN48Z7MK3mS_cZgy2IDcii3eTi_bGVPdLaPRj57MEEkXhj2WOSNzV9abYryQT8eFE1wVhLczF6coKYnsyHUEdKYJG7XthPqoplb3GUAjaZTFi_5zH18E=)
9. [usermaven.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFxRrVAcggSDCFPCR4Zxm9nXlU2VGwvfy40lc0Qucn0EqltL3pMCuwxthR8NwXYoHtx8WDsN8e6zWBeQCXprYlSagH1CbriiDxRgT_wGknfSyFUGNavn_dET3GOmXkHElTTtz4u2wHJ2FifMRC8mrYhe1kgw==)
10. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRdSmgwQgZq_5PNvvGZbsPNeMsuIOq0Csd6-xhF2rv5jQMwzQGNsUF2NM_Fa7SUjq3ZiRfcdqqgDwWWMP2yUI6tVfwUZUPLVGgOtzNMROm3DLpdjHJXrJIKmlzBFv_-FYgMHhEATzoe7a_XkITt9NjZBMMffzvzgyFfDGO7p5ABNzG9UMRoH6p13OQPDMXUODxWLBKUPfuvaCdBcXlXbMNY_olaZZ4ImwWsmnaw5dEilO6)
11. [hockeystack.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmA1iM4FZKLOuyxJDP3Hu8F2v8hGChfFZ8S5L-lTbh6FEMWPflIWyrdAt4SPIlG1f2bBt_P4FzpRj5xdlH-cuD_mTrS6H-XDlyJp4lOzyK9fQpxW3DaahFifA5KQo1vCoLzqxH6F1Kdwvqkptq2ecjH0sBdAaSEK8=)
12. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGouRbE37WG2fvTul3bYYTO9LmTH991M0Y9evMi7_r0UzqOJax5_cobhuDebuW9WUZeSh-YVXFOPajR76PDEPIhh4q82xklJRXLcJVxau4-sny_kTvit_k8GlK5cm-lcHQzmy7Ec1QuS9aZtC2L96w=)
13. [koehn.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLf3agVjo0AJK-g_uS-1yTrh2uwD_aH8llFThPA3XOgKk-rbCk6ALUUt5swsae32xZwDTXDyItaLkrONF0LQQkQbBL3xTr8lhDY4cFASzj1mJwwAEFlsJJDsLOwZ_nR1gQ-HW9dWfio_gKJwuPLPes4RBbbmPzedQQmo_Xqfy722u4PpaZIo_b3SWfH2mtVoCwXup9jPZkY8A=)
14. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRWXxLuDbVDCcQRxGOoOJ7YFjk1rh7H-ygrzYTEkEH1pzzZREHukCUC22B4MZKvKqNQ8X_2UUN85_f6iiLDbDZVVJnb5Z2ikiyjpbJpL806eMtlB1ezkf7Hgs5Dbtsb2LqZ0kPBxd04_JQHnJch8_ZMuVHDNDWV8_bDFfj3xu9YC6WilVLwqidcb9iPw==)
15. [thedatacherry.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFys7n7swyANW6bUif_Evzi4-sTLa9NRUaJ1Gqd3dA_dNFwz9PNnNitEGxbY0NK8EVZpRKvhxUUhNnETcVsJf_wfH9iCmYbUdc0wzGN5j4JOEB0R9VluMJh9m-Pbcfe5gvz1vAQWCHvjvPCSf2OTupfvVVXCynfFOVd8jvnbaE3d-4ZtnDDi1S5vMoJa7Hmo7jO7sFlA0nyRMJ59Q==)
16. [lebesgue.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPhH6dU-Updstk-OW1aca6xG4fsONYgKSNu1KL7AmrM-Gi5fUiZ0UdEoY1Ht7LhJ0f0CN3_8WPTHzjbEGSeZZNUkJXLf7RoQi1HNG5_r_nk8lCdrvHbqYDv7LJe-nBXDy8pjvN_-w1taHK2SYD8pIpMgF3UyQWWKolfJAxssNefBbYqAaU-4Gn)
17. [leadsources.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkSfR1COGvhtlKh0HcXO2k-UieG51QCnUeN2UbzBLaCyJSUtCMnroTcKMlOGZLo6jZTvO10sJ8Sd7dMqaRjwGwYoxEG6Bs_m7lrZwx0n0z-zAd-5mhK_Mrk6O3QzmBAwQpNefehp2ithSemrnfGQ==)
18. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHF7rNwH37kZeSpz5jEDvA1ra0PFn8nDQ8rqh6wUqcaiuqkFz45widwuun5cUauysctJ8zRbwazW12uPficmEYcZxRBb-q0Itjl9HIXgnaqiOWhZwHc)
19. [adequate.digital](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGung8nveqPCP8DeVU3MUbb84YsibEdWLFgPx1waOofG45bsfVAS6Z3YL9nTlV77BpCSYR8PfpjR1VqULNjpJrJeu3DDoI03kv2__ywm7vwl7M8tqccMadT9EBtDTMrf7Kw5dTBFASx5Gpfl-95Q3CVBj0sPLAb_lUbMRBY70OL5Qf_)
20. [redtrack.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1YB_KRzFeCjjOeva6lbXC0Gd5hRvmErua2LCwDvEYIsvlXNmjpGHCGlLz-4zOiqVKI2sraEJf15JdtE5GwCgkEfumL14XZxXhpgc5sgkPEOJ5XsgRuKRavrW_K-UdJyJvI68Qf2GdZcEXlkE9-7Bdzw==)
21. [windsor.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5pvsw9sGXgRE5O3v8f4QpOrJf6Sp9w4TuKCIH3ieQluy-3EcE5F2AIUbjWFfD-VT0RGuZI4lzfkPZIOwlaVrQPV8tJUuIEnjBYu8Y6zjoUm5eXEQwVGgBAWCC0lReTZlUnpvaaSsD-bTSoGdJkb8ZHydxeIooujEcbsyPd4YE)
22. [misterspex.tech](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2SvFgbakYvIb_69cWQIA0aNGj77TTN2avsBB5ph3i_yq8YKv1SawO3PewfA9_nnyH54ZtrEtbmOQUBLlx1xb4zhrRyhLZC8kinU2lZ3nYn-Z1f2Ma8nAONA_L4k5ef48j1epeXUpoGv5dxNqUuwYpI7lsxKjb6NdnAjmZUQNIc3awFtD83t7REB_wOwypx5V_miKFJQ==)
23. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmao8rtXFZw7ckSGIJHOXmivof9BOFfxCdy2L3d9eYE8vICyJ90oABTDE3hp0ARcK5rG0Zcpm8d01d9krf1myTC715oJU4LzwpmGVVPYTA2d7da6V30YCqW9VBa40g9ebXyQGaYzMbZHcuBUN3gViZuJ1n-oHWYxQxdlXBhDItYqUACOCunNXgQjadLCw=)
24. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMUyezSYICAFGK9qeM3nN3NQu64oOUaMZur-77mTxbi05JZUcft2wUz7cXHwCMUXTU03lCuYHCRT3rXI8z1ydpu_Y08Z7QbVv7SfJJYhoGspReod7ZZi2Eyl7IHr_928CyO1vp-gOAKXr_Im_H-6K91Hcao9SdGKZNf_SG1OEVt57soHb0gwO77XzjVTdOA-LUQrAzaJCaXXsCUZNbVuaZ7JfND8kICkwrVuzxcNvxW3hBWw==)
25. [bookdown.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGBoDPsMQgKdLtpQ36Uvz5HAKkv5UZj-XBlxJGD5oaCIt1aRKT3agTxE5dM7TOHA8LCFbA2IBsLo8s46Z5rIm2zpnt3SrgOGwKKzeGeqo6Cw48uSUuSUdtDuieGSSXzBSMG9s-nm2AMn2_-g==)
26. [statsig.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7AVCJ62phWxUpjcLfUikinEKS6eO9nF8mTBVZabc-znpnncePQMW7lhfTQjDrMDZhZ4CAGfhIIEFbntuZQm4u_GfaUryiZNA8NHLvyitiGhC_5INYj8dINBqclNLzKFn13Lx8741oGaxlseOK9nfl_Fn23e-kaCG2vA==)
27. [quora.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFe28QLUHmQy5JQk8ipZ6hU6-5M1mFQw-QnubFEpsoq0RNoNrWLTfw1cvWcFZfNEmGw790dPPxCnePpU-upd-nq81UHIjiXhn2xvo5GsJY-S9zOEttS7C4ZGluXtksCyEux4luviZFx_M1kF1xKau6oQqS9gUSpMzK448v1DQc=)
28. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYSnYjUnzRGRdDc5ck6ZsEAqAYOgjuqngKpzSw-LFZHYuyHps7lw5Y3Wbb0HMl_yhVxMMiOPrgYP6VEGhkv-9tw7uOf0VQkO1O0ra0EfqEYmBzhmqjPWBvzs5to-7OLEASYkgW3HJ02r3_gN8HZ2o6I9TS3wgnKIWE4hBrpFUGarpUffl-gCdgZLDD86XDPMqkhSdRW2ZSFZI-Gd-x)
29. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFinIDhKRE4oxTcye_AdIH996rAhErISJb9C2WnV1t3L-4Hs_3mwgDR3VQ01_hO0YyeVUyJStNe5_En4LEsqt33HxblWNyKx-WWC1jmixieeL-IvwqkxsUfYmTmYa4HVSWeABChafFWZtAP_RekKCGKTb-wv_M=)
30. [displayr.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE67srvnannvot-0Qte538ImVYZKf371DvCe3mF7WiYa9r4tqPAMTExUc9Kev1v0tCKADexZw-KaTtkRetWCyU7POHvOIhnYDF0SzODg0hj3LJVQyXX8PiwPxf0jrWRZhbgbE3NPsWY5OdK5gUGJyCw3IXyLfqEsb3E5OzgsYYNHw==)
31. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExYjIiydcReIXpGy1yS2djk5jVvm528XZCRR9GyCwY20ogxRGJ1rbS04teVpIsPkUFoZPeqW68Nsu0t09IxlZ-fdzdK5IAVwT-a0ui6UtbZTl0p1Uq)
32. [prooveintelligence.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGApZXUhCha5V7Mu2qLgN4MiiF7LWA29LE52YcKW_4D-RQPNZgAfNm_yVEFRe0NM72NVIvadI37Jq2t5CU9qaydnCZSpgyQil1rzE3_TI5bpjOqmLXeGi3g7GVnwsKFwV6Tn0ChfPW-QTrcHT5PX4wPuVi4V0vCp-r5YlEfpPA1w-5K91g-OxRsdBBqbyrpggGw)
33. [statisticsbyjim.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHN9ltRqQx94mngHd6SKD4hzUOqYY0GqPBSFvnT1m7BsUEzyQtdclI-NE6_FS4V1MmOcKKWZeJcHM24WN8rnRJzFLzmjntjFNpcys-YjWNoIQT0Dt9tBulvfQ0tBNn8ge3i_qPj82R2psWQ)
34. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgyjTNZSISYr-IY2KHBNb6Pmvem5f6tctbdspJH0Gt2VQBEUnKapGNtFbMnTMeNii5EdteGlTw2TIx5fMJjigkQtfovUmW5xoMSSTiWEF6KqGMkflFxD9k5DUIL8i2KA==)
35. [statsimprove.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQED3BcKNmi1pbv0BzWHWopAM0jMhottYVFQMzGNQyTOUlhsq_gydv-UtyjfHl7192pqxav_BEbcWPuQfUVleQ-vxnF4Ng9oW61Q34w1OqYn_PPOk124zBD9fFQILG81AU2uKHTMfHDRhEaG8Pd5UGVPt09RkIp7bk6VJztoBwK49IyQJBruciIfKf60vg==)
36. [graphpad.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGF21VxBY3wytmegxfb58whuOqtE7VxScYW3nkypNAEOJEoseL5PsCqo9WkxEyuWKsawgkOaGewXqtTlp1dGrU57EV38gSZjL_gy-35FIp7peBiaWcvc3PAMZoaJFjxdEQbyKKDe7Qx030bmyW7IGivcRZUNNu5_6PVVjOxSxEEyr4LV6GcXA==)
37. [oreateai.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETFuE1-n2w9NBeGCgspeS0BX5NA0LDfGL9RpWPgqgYwXS-uRaI1Y2juVxV8CKcL2JhfgWnZ05gD2HPBwU8Wi5YBsiM1lg4FGiTWNwBSrJHq7g4qSClqMUZuynjeydTaPNpH5C54gJlk3Pp5igVC6A1ZTibkYqBdVd3XhGNwLuBU1zu9mVNfGkUZp7OjKLgHggXzHjMvCoDthAlaKXgElIAsg8QYh28m4Klq_dzqXcjj8CDZF-Jo7faMyDDFfrayT-MEQ==)
38. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJJ3SwSZvi60sA5Jd0vSmudqDDlpyVHDXOqXtH0fELzb1sMrSv4TAORILqwx1VPZDR4ue4v8yx76I1EkUZMpyq_OcQEZ5KMrXUfzlu7NihaX8J-JNUjlAJqRwIps5jbpuhQH4IqF8E8zP4uaaIWfx9346-6Jj-L-lX2OeKFWxJoVB9eVdEUnZ-xPBCijaHPPnzGjiFhBcaagcFv0YybqQLs_0yY52ATYZSJIWVc1svlvegFvcj4wCcD--2)
39. [geeksforgeeks.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlWsLKzWbz9aeT8h0Ewtaujxc2LXGbBAdot7WXoxoS8IwQQAgjCI_w4FCQWYu2DBeqchwzTAOu3ojQLABIJW1HRk2F-N2_4pY6yGiL5YfX2h2AYAaYklB8SWMvoa3a7StTGx2PdDWXBN6WhGYamLmzaf9yTiquSsXSFkXSp2Z4I8LrV9uSBVbHhxBF)
40. [mljar.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvCTcOpxcMGt48z2mS2A5WusS2bjs6JIjDGcjZNGPMDuKLnHzfexxRucqZv-yisOvotWl-EJ8R2xP-eZ2MMSDIo6aHg7_UBGDnwq4TTUA_AzAePxzYIfU0RV2JyJzxAf--kWSn_EEVeQbwErjurgJ-)
41. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4YfTOtIjvGbg76JIM7uH0ZX7NvapaBSyU8yuApGCNtLhXmCmgfXgfKp59HJH3c4hBcc84L2_GJPlCP0w5R-TvK3PmyPPnJXzBvWH4TbpdkvUfRIF5dO6ME-P00QxLDaolcgSM_c-TzjXo9lhJzqrHg9NE33WojIlkYBktrweny12aJRhst7O9Cku8EakCyQSMRvY=)
42. [stackexchange.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_wPa0uxYkyAbeH51122GAaZdOVHY7YHwy7OV-sFrNyFebBo1ww1z6E_2tcIKnRDRlEyZ847Yg6AXFYFCoeAgkPqdfiEEUZtqJYjGtTLqVX46NnEFkQ1O5dtfdty8NBQEoMEg6NAj6QLMDxrXtZPSajtAxqbQ72Jp9MfKC6BimvUwBvmynr-zpXLhmGw==)
43. [dreamdata.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmZpab3do3IaaXUTSUPQxYUC1gnWxGWvZ5PW8XiLJq5kZOjVI7LW_HkelCtsS1eeo9M3rjfmrXK9I42jFg9bCaQtl8sWNYf5IhwUKOpBPGEO2M3vRwpPt_P_C89x8C9cJlkM9gon0IoUgIAjDCgjWIjh17)
44. [stackexchange.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmpR3U9-5bSBnZus6nRfYdvHZsAkafgguxavS0JAclHjupOLSK9taKXOgzXs4KkucsLZZeByj2Ri2HSxekud4c1YlXJhDleFRHKSdy9yFaZ0X_-xz1jF9zFjZLX58o0MMH7weQaSBz6wmJmEOu9YWyBl_3-4TY_Ji1djL0fL7_cqeOk238NsvAEPQ5bazGPCFeuPXVoOxpkY47XhXcVmIJ92cc3vqh3g==)
45. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvYX7l5JTppIBFOHvT9UBHMxYevDQMj1-i1EfvzjBPnPyE6S7Comt1ROGVoA38aq7EmO326nIGmtun4eqFlEWD25YTBnxTPTha6FJITFVF7GYFkYtxFQH4llp8gTIAbzyDZS-gxYCUs2h4snn5Z4gko_zs7NtlvVQhVXm22MTaSNXUSG4i-0BS3m9zx9eSz9dS)
46. [databricks.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVtGdRNuRPnH14GtskMYKNjJHAJyrbHD8SyF9ZYHOW1xi5mJigfp0zOqiET-7VKQAyYjWnxWVn9b7Pr4cqeRUK0N4KkWNS883r2D2XihzrDy1aMBH-3i3JTZKHwCIP9oSLTuE9Q_gqx8Jq5IlpSug-Z3dUdYRa6zEZaJw30fTzlJgg1WkfRSDHbRU-1F_ctg==)
47. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKwwum-HRRzq3ioymqKKZM17-vK_n0cWu5rsC5yzjO4koMMR4qW0vFYQ-i_i1ljvtExuJ871dXGPFauk2uCZS4aKyH3yPAl2cboYOLAvn2xGLq4EApzkfG-NJUUcYxP5QA61_pQCI=)
48. [berkeley.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE692IF1S-Ht4x6FU72zypNhdv6qUXkT5_cHl_8ni3Em3LN8VBBYHmHHvS70qbWKe5yqJDolA264HuTE7yRo818HgV0Sn10_Kd87n1YCP_7UHdU0Jij5kB93agh9djsuslzLgHTYA==)
49. [towardsdatascience.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXwCfcNKbu9Htn73ze0JDroLGof1RauhvsYpWLNlSo7V1iTyKupR6GEqkv6VR5TZDOBjuQL0txvFRvETXjuf1IMnYCVI1uHKvNOkJ2N9y8hX2Z_zIokQTp33LrH29sCCrpgrTO_AZbcUuCMF6MFlQAB6_nBBdd2WI1_mFVvyQuoVFLmslhupsLSVgowZ6f5zhxFBgDNmM=)


## Annotations
Annotation(end_index=2480, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFnAAe8CkDdhPMEjITc3M3_WzoJRj6nLNU6MYUSNIR65VFrEKwirJTfErzfs_lG3XJq0gfUU_Rt3aVg0ZW_d7A3qWZ-jmcz6M-CPSgO_YWGwfXLHH4UwyPlc-xwoe5QRI0QBlwjCtC7x0XZismok8NUeQQsG9GLRXqQX6FW6FFIJo1', start_index=2468)
Annotation(end_index=2480, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJnWS9CC4wu6CHBu-bc60D6Kt1oaz3PKtpkm1GqwvpeioBtH1kKGnkVgsWtQLswjBTGjnQf9GPYRN4LYwhqeCHV6xLQkIm5vgwRIo3wCEKij-lg5f4rHuO3j22P3exsh1FmT7PMefKolRleHT3SNE1lFWBC4cMCj9y', start_index=2468)
Annotation(end_index=3133, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPGMi7RGr1q1XhdNRzzQhNawuYra4MSSFxeVadRW5QEsfOAvd0jDkFGXmk0dpqJv-thvQ3Qfj6VBl8LmK7_Jz7rvWot6C7XUa98s19Gbpnu3Q9VFy7qyHH6zRa4cW55-_ehyX3ZFwN47jkPmQ=', start_index=3121)
Annotation(end_index=3133, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJnWS9CC4wu6CHBu-bc60D6Kt1oaz3PKtpkm1GqwvpeioBtH1kKGnkVgsWtQLswjBTGjnQf9GPYRN4LYwhqeCHV6xLQkIm5vgwRIo3wCEKij-lg5f4rHuO3j22P3exsh1FmT7PMefKolRleHT3SNE1lFWBC4cMCj9y', start_index=3121)
Annotation(end_index=3542, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHdNAKAumDSf0rfs8JQSrsBtQ1Q5QqIaVtl8_8BKeGUkGZaASmFiHEN2NuXDLl2Bs9gQOLFqqu8JKw88sSp8Jc7X8TWYGVgNezzzfia1XtyTXjmXM3Eq6Kc-Wt81qasoK2IlzLUQduqFspdKvlV-avZ_oI-ZhxFhbFwNrbLziGmERO2gVLn-tBpyRszH5rh71J', start_index=3530)
Annotation(end_index=3542, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFnAAe8CkDdhPMEjITc3M3_WzoJRj6nLNU6MYUSNIR65VFrEKwirJTfErzfs_lG3XJq0gfUU_Rt3aVg0ZW_d7A3qWZ-jmcz6M-CPSgO_YWGwfXLHH4UwyPlc-xwoe5QRI0QBlwjCtC7x0XZismok8NUeQQsG9GLRXqQX6FW6FFIJo1', start_index=3530)
Annotation(end_index=3748, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsDyr-bXiCI5N4DZGyQFsLiTf7kW3aAIJRi1tvnsKe2bQOzqIoM3KoUi8Q-NPDpEMy3C13ecFncKEicSLXZ0yPy5KrSaLHUx1ff61J72STOYGnSqiN-zYHSVq2LdlUTWiWgIeV-RUxmIE-_7qMlN61VA==', start_index=3736)
Annotation(end_index=3748, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFnAAe8CkDdhPMEjITc3M3_WzoJRj6nLNU6MYUSNIR65VFrEKwirJTfErzfs_lG3XJq0gfUU_Rt3aVg0ZW_d7A3qWZ-jmcz6M-CPSgO_YWGwfXLHH4UwyPlc-xwoe5QRI0QBlwjCtC7x0XZismok8NUeQQsG9GLRXqQX6FW6FFIJo1', start_index=3736)
Annotation(end_index=4234, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPGMi7RGr1q1XhdNRzzQhNawuYra4MSSFxeVadRW5QEsfOAvd0jDkFGXmk0dpqJv-thvQ3Qfj6VBl8LmK7_Jz7rvWot6C7XUa98s19Gbpnu3Q9VFy7qyHH6zRa4cW55-_ehyX3ZFwN47jkPmQ=', start_index=4222)
Annotation(end_index=4234, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFnAAe8CkDdhPMEjITc3M3_WzoJRj6nLNU6MYUSNIR65VFrEKwirJTfErzfs_lG3XJq0gfUU_Rt3aVg0ZW_d7A3qWZ-jmcz6M-CPSgO_YWGwfXLHH4UwyPlc-xwoe5QRI0QBlwjCtC7x0XZismok8NUeQQsG9GLRXqQX6FW6FFIJo1', start_index=4222)
Annotation(end_index=4876, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFapy5V8jBp4rR7GuhLawljFoVQSA1CpiHuU9yomMgpw9qf4qRUAZOhOpYq0M37z84xkU_O_sJSIplPXXKRshRdn5TD-0cd7CmQ5HC8zaUREUB0Xl2ji9WZwampzIN6ppnS', start_index=4861)
Annotation(end_index=4876, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsRq9nzQn9aYb8Bdk9ZZXrjPRcu9fzri4GY7MDxKxbN48Z7MK3mS_cZgy2IDcii3eTi_bGVPdLaPRj57MEEkXhj2WOSNzV9abYryQT8eFE1wVhLczF6coKYnsyHUEdKYJG7XthPqoplb3GUAjaZTFi_5zH18E=', start_index=4861)
Annotation(end_index=4876, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWI2eEiVa8dwJhL7jeuiGeL2qKdFsntlIAe892d85KwT3_eAqhsHFgBweAP1PUXt9-FOWS4hgOBEo2R6lybcjrBAVr5pLnOdN4zqo6INphVUGslbJap3KRPolGBE3Z6-dCzxSZJy2VZPpsnAtWZyDa', start_index=4861)
Annotation(end_index=5426, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPGMi7RGr1q1XhdNRzzQhNawuYra4MSSFxeVadRW5QEsfOAvd0jDkFGXmk0dpqJv-thvQ3Qfj6VBl8LmK7_Jz7rvWot6C7XUa98s19Gbpnu3Q9VFy7qyHH6zRa4cW55-_ehyX3ZFwN47jkPmQ=', start_index=5410)
Annotation(end_index=5426, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFxRrVAcggSDCFPCR4Zxm9nXlU2VGwvfy40lc0Qucn0EqltL3pMCuwxthR8NwXYoHtx8WDsN8e6zWBeQCXprYlSagH1CbriiDxRgT_wGknfSyFUGNavn_dET3GOmXkHElTTtz4u2wHJ2FifMRC8mrYhe1kgw==', start_index=5410)
Annotation(end_index=5426, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRdSmgwQgZq_5PNvvGZbsPNeMsuIOq0Csd6-xhF2rv5jQMwzQGNsUF2NM_Fa7SUjq3ZiRfcdqqgDwWWMP2yUI6tVfwUZUPLVGgOtzNMROm3DLpdjHJXrJIKmlzBFv_-FYgMHhEATzoe7a_XkITt9NjZBMMffzvzgyFfDGO7p5ABNzG9UMRoH6p13OQPDMXUODxWLBKUPfuvaCdBcXlXbMNY_olaZZ4ImwWsmnaw5dEilO6', start_index=5410)
Annotation(end_index=5814, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJnWS9CC4wu6CHBu-bc60D6Kt1oaz3PKtpkm1GqwvpeioBtH1kKGnkVgsWtQLswjBTGjnQf9GPYRN4LYwhqeCHV6xLQkIm5vgwRIo3wCEKij-lg5f4rHuO3j22P3exsh1FmT7PMefKolRleHT3SNE1lFWBC4cMCj9y', start_index=5797)
Annotation(end_index=5814, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGouRbE37WG2fvTul3bYYTO9LmTH991M0Y9evMi7_r0UzqOJax5_cobhuDebuW9WUZeSh-YVXFOPajR76PDEPIhh4q82xklJRXLcJVxau4-sny_kTvit_k8GlK5cm-lcHQzmy7Ec1QuS9aZtC2L96w=', start_index=5797)
Annotation(end_index=5814, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmA1iM4FZKLOuyxJDP3Hu8F2v8hGChfFZ8S5L-lTbh6FEMWPflIWyrdAt4SPIlG1f2bBt_P4FzpRj5xdlH-cuD_mTrS6H-XDlyJp4lOzyK9fQpxW3DaahFifA5KQo1vCoLzqxH6F1Kdwvqkptq2ecjH0sBdAaSEK8=', start_index=5797)
Annotation(end_index=6159, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHdNAKAumDSf0rfs8JQSrsBtQ1Q5QqIaVtl8_8BKeGUkGZaASmFiHEN2NuXDLl2Bs9gQOLFqqu8JKw88sSp8Jc7X8TWYGVgNezzzfia1XtyTXjmXM3Eq6Kc-Wt81qasoK2IlzLUQduqFspdKvlV-avZ_oI-ZhxFhbFwNrbLziGmERO2gVLn-tBpyRszH5rh71J', start_index=6138)
Annotation(end_index=6159, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFys7n7swyANW6bUif_Evzi4-sTLa9NRUaJ1Gqd3dA_dNFwz9PNnNitEGxbY0NK8EVZpRKvhxUUhNnETcVsJf_wfH9iCmYbUdc0wzGN5j4JOEB0R9VluMJh9m-Pbcfe5gvz1vAQWCHvjvPCSf2OTupfvVVXCynfFOVd8jvnbaE3d-4ZtnDDi1S5vMoJa7Hmo7jO7sFlA0nyRMJ59Q==', start_index=6138)
Annotation(end_index=6159, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRWXxLuDbVDCcQRxGOoOJ7YFjk1rh7H-ygrzYTEkEH1pzzZREHukCUC22B4MZKvKqNQ8X_2UUN85_f6iiLDbDZVVJnb5Z2ikiyjpbJpL806eMtlB1ezkf7Hgs5Dbtsb2LqZ0kPBxd04_JQHnJch8_ZMuVHDNDWV8_bDFfj3xu9YC6WilVLwqidcb9iPw==', start_index=6138)
Annotation(end_index=6159, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLf3agVjo0AJK-g_uS-1yTrh2uwD_aH8llFThPA3XOgKk-rbCk6ALUUt5swsae32xZwDTXDyItaLkrONF0LQQkQbBL3xTr8lhDY4cFASzj1mJwwAEFlsJJDsLOwZ_nR1gQ-HW9dWfio_gKJwuPLPes4RBbbmPzedQQmo_Xqfy722u4PpaZIo_b3SWfH2mtVoCwXup9jPZkY8A=', start_index=6138)
Annotation(end_index=6928, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPhH6dU-Updstk-OW1aca6xG4fsONYgKSNu1KL7AmrM-Gi5fUiZ0UdEoY1Ht7LhJ0f0CN3_8WPTHzjbEGSeZZNUkJXLf7RoQi1HNG5_r_nk8lCdrvHbqYDv7LJe-nBXDy8pjvN_-w1taHK2SYD8pIpMgF3UyQWWKolfJAxssNefBbYqAaU-4Gn', start_index=6910)
Annotation(end_index=6928, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRWXxLuDbVDCcQRxGOoOJ7YFjk1rh7H-ygrzYTEkEH1pzzZREHukCUC22B4MZKvKqNQ8X_2UUN85_f6iiLDbDZVVJnb5Z2ikiyjpbJpL806eMtlB1ezkf7Hgs5Dbtsb2LqZ0kPBxd04_JQHnJch8_ZMuVHDNDWV8_bDFfj3xu9YC6WilVLwqidcb9iPw==', start_index=6910)
Annotation(end_index=6928, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkSfR1COGvhtlKh0HcXO2k-UieG51QCnUeN2UbzBLaCyJSUtCMnroTcKMlOGZLo6jZTvO10sJ8Sd7dMqaRjwGwYoxEG6Bs_m7lrZwx0n0z-zAd-5mhK_Mrk6O3QzmBAwQpNefehp2ithSemrnfGQ==', start_index=6910)
Annotation(end_index=7680, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkSfR1COGvhtlKh0HcXO2k-UieG51QCnUeN2UbzBLaCyJSUtCMnroTcKMlOGZLo6jZTvO10sJ8Sd7dMqaRjwGwYoxEG6Bs_m7lrZwx0n0z-zAd-5mhK_Mrk6O3QzmBAwQpNefehp2ithSemrnfGQ==', start_index=7666)
Annotation(end_index=7680, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLf3agVjo0AJK-g_uS-1yTrh2uwD_aH8llFThPA3XOgKk-rbCk6ALUUt5swsae32xZwDTXDyItaLkrONF0LQQkQbBL3xTr8lhDY4cFASzj1mJwwAEFlsJJDsLOwZ_nR1gQ-HW9dWfio_gKJwuPLPes4RBbbmPzedQQmo_Xqfy722u4PpaZIo_b3SWfH2mtVoCwXup9jPZkY8A=', start_index=7666)
Annotation(end_index=7887, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkSfR1COGvhtlKh0HcXO2k-UieG51QCnUeN2UbzBLaCyJSUtCMnroTcKMlOGZLo6jZTvO10sJ8Sd7dMqaRjwGwYoxEG6Bs_m7lrZwx0n0z-zAd-5mhK_Mrk6O3QzmBAwQpNefehp2ithSemrnfGQ==', start_index=7873)
Annotation(end_index=7887, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHF7rNwH37kZeSpz5jEDvA1ra0PFn8nDQ8rqh6wUqcaiuqkFz45widwuun5cUauysctJ8zRbwazW12uPficmEYcZxRBb-q0Itjl9HIXgnaqiOWhZwHc', start_index=7873)
Annotation(end_index=8151, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1YB_KRzFeCjjOeva6lbXC0Gd5hRvmErua2LCwDvEYIsvlXNmjpGHCGlLz-4zOiqVKI2sraEJf15JdtE5GwCgkEfumL14XZxXhpgc5sgkPEOJ5XsgRuKRavrW_K-UdJyJvI68Qf2GdZcEXlkE9-7Bdzw==', start_index=8129)
Annotation(end_index=8151, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRWXxLuDbVDCcQRxGOoOJ7YFjk1rh7H-ygrzYTEkEH1pzzZREHukCUC22B4MZKvKqNQ8X_2UUN85_f6iiLDbDZVVJnb5Z2ikiyjpbJpL806eMtlB1ezkf7Hgs5Dbtsb2LqZ0kPBxd04_JQHnJch8_ZMuVHDNDWV8_bDFfj3xu9YC6WilVLwqidcb9iPw==', start_index=8129)
Annotation(end_index=8151, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGung8nveqPCP8DeVU3MUbb84YsibEdWLFgPx1waOofG45bsfVAS6Z3YL9nTlV77BpCSYR8PfpjR1VqULNjpJrJeu3DDoI03kv2__ywm7vwl7M8tqccMadT9EBtDTMrf7Kw5dTBFASx5Gpfl-95Q3CVBj0sPLAb_lUbMRBY70OL5Qf_', start_index=8129)
Annotation(end_index=8151, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLf3agVjo0AJK-g_uS-1yTrh2uwD_aH8llFThPA3XOgKk-rbCk6ALUUt5swsae32xZwDTXDyItaLkrONF0LQQkQbBL3xTr8lhDY4cFASzj1mJwwAEFlsJJDsLOwZ_nR1gQ-HW9dWfio_gKJwuPLPes4RBbbmPzedQQmo_Xqfy722u4PpaZIo_b3SWfH2mtVoCwXup9jPZkY8A=', start_index=8129)
Annotation(end_index=8552, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsRq9nzQn9aYb8Bdk9ZZXrjPRcu9fzri4GY7MDxKxbN48Z7MK3mS_cZgy2IDcii3eTi_bGVPdLaPRj57MEEkXhj2WOSNzV9abYryQT8eFE1wVhLczF6coKYnsyHUEdKYJG7XthPqoplb3GUAjaZTFi_5zH18E=', start_index=8535)
Annotation(end_index=8552, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5pvsw9sGXgRE5O3v8f4QpOrJf6Sp9w4TuKCIH3ieQluy-3EcE5F2AIUbjWFfD-VT0RGuZI4lzfkPZIOwlaVrQPV8tJUuIEnjBYu8Y6zjoUm5eXEQwVGgBAWCC0lReTZlUnpvaaSsD-bTSoGdJkb8ZHydxeIooujEcbsyPd4YE', start_index=8535)
Annotation(end_index=8552, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2SvFgbakYvIb_69cWQIA0aNGj77TTN2avsBB5ph3i_yq8YKv1SawO3PewfA9_nnyH54ZtrEtbmOQUBLlx1xb4zhrRyhLZC8kinU2lZ3nYn-Z1f2Ma8nAONA_L4k5ef48j1epeXUpoGv5dxNqUuwYpI7lsxKjb6NdnAjmZUQNIc3awFtD83t7REB_wOwypx5V_miKFJQ==', start_index=8535)
Annotation(end_index=9813, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1YB_KRzFeCjjOeva6lbXC0Gd5hRvmErua2LCwDvEYIsvlXNmjpGHCGlLz-4zOiqVKI2sraEJf15JdtE5GwCgkEfumL14XZxXhpgc5sgkPEOJ5XsgRuKRavrW_K-UdJyJvI68Qf2GdZcEXlkE9-7Bdzw==', start_index=9787)
Annotation(end_index=9813, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMUyezSYICAFGK9qeM3nN3NQu64oOUaMZur-77mTxbi05JZUcft2wUz7cXHwCMUXTU03lCuYHCRT3rXI8z1ydpu_Y08Z7QbVv7SfJJYhoGspReod7ZZi2Eyl7IHr_928CyO1vp-gOAKXr_Im_H-6K91Hcao9SdGKZNf_SG1OEVt57soHb0gwO77XzjVTdOA-LUQrAzaJCaXXsCUZNbVuaZ7JfND8kICkwrVuzxcNvxW3hBWw==', start_index=9787)
Annotation(end_index=9813, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmao8rtXFZw7ckSGIJHOXmivof9BOFfxCdy2L3d9eYE8vICyJ90oABTDE3hp0ARcK5rG0Zcpm8d01d9krf1myTC715oJU4LzwpmGVVPYTA2d7da6V30YCqW9VBa40g9ebXyQGaYzMbZHcuBUN3gViZuJ1n-oHWYxQxdlXBhDItYqUACOCunNXgQjadLCw=', start_index=9787)
Annotation(end_index=9813, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGung8nveqPCP8DeVU3MUbb84YsibEdWLFgPx1waOofG45bsfVAS6Z3YL9nTlV77BpCSYR8PfpjR1VqULNjpJrJeu3DDoI03kv2__ywm7vwl7M8tqccMadT9EBtDTMrf7Kw5dTBFASx5Gpfl-95Q3CVBj0sPLAb_lUbMRBY70OL5Qf_', start_index=9787)
Annotation(end_index=9813, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2SvFgbakYvIb_69cWQIA0aNGj77TTN2avsBB5ph3i_yq8YKv1SawO3PewfA9_nnyH54ZtrEtbmOQUBLlx1xb4zhrRyhLZC8kinU2lZ3nYn-Z1f2Ma8nAONA_L4k5ef48j1epeXUpoGv5dxNqUuwYpI7lsxKjb6NdnAjmZUQNIc3awFtD83t7REB_wOwypx5V_miKFJQ==', start_index=9787)
Annotation(end_index=10061, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7AVCJ62phWxUpjcLfUikinEKS6eO9nF8mTBVZabc-znpnncePQMW7lhfTQjDrMDZhZ4CAGfhIIEFbntuZQm4u_GfaUryiZNA8NHLvyitiGhC_5INYj8dINBqclNLzKFn13Lx8741oGaxlseOK9nfl_Fn23e-kaCG2vA==', start_index=10040)
Annotation(end_index=10061, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRdSmgwQgZq_5PNvvGZbsPNeMsuIOq0Csd6-xhF2rv5jQMwzQGNsUF2NM_Fa7SUjq3ZiRfcdqqgDwWWMP2yUI6tVfwUZUPLVGgOtzNMROm3DLpdjHJXrJIKmlzBFv_-FYgMHhEATzoe7a_XkITt9NjZBMMffzvzgyFfDGO7p5ABNzG9UMRoH6p13OQPDMXUODxWLBKUPfuvaCdBcXlXbMNY_olaZZ4ImwWsmnaw5dEilO6', start_index=10040)
Annotation(end_index=10061, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsRq9nzQn9aYb8Bdk9ZZXrjPRcu9fzri4GY7MDxKxbN48Z7MK3mS_cZgy2IDcii3eTi_bGVPdLaPRj57MEEkXhj2WOSNzV9abYryQT8eFE1wVhLczF6coKYnsyHUEdKYJG7XthPqoplb3GUAjaZTFi_5zH18E=', start_index=10040)
Annotation(end_index=10061, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGBoDPsMQgKdLtpQ36Uvz5HAKkv5UZj-XBlxJGD5oaCIt1aRKT3agTxE5dM7TOHA8LCFbA2IBsLo8s46Z5rIm2zpnt3SrgOGwKKzeGeqo6Cw48uSUuSUdtDuieGSSXzBSMG9s-nm2AMn2_-g==', start_index=10040)
Annotation(end_index=11152, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE67srvnannvot-0Qte538ImVYZKf371DvCe3mF7WiYa9r4tqPAMTExUc9Kev1v0tCKADexZw-KaTtkRetWCyU7POHvOIhnYDF0SzODg0hj3LJVQyXX8PiwPxf0jrWRZhbgbE3NPsWY5OdK5gUGJyCw3IXyLfqEsb3E5OzgsYYNHw==', start_index=11130)
Annotation(end_index=11152, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFe28QLUHmQy5JQk8ipZ6hU6-5M1mFQw-QnubFEpsoq0RNoNrWLTfw1cvWcFZfNEmGw790dPPxCnePpU-upd-nq81UHIjiXhn2xvo5GsJY-S9zOEttS7C4ZGluXtksCyEux4luviZFx_M1kF1xKau6oQqS9gUSpMzK448v1DQc=', start_index=11130)
Annotation(end_index=11152, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFinIDhKRE4oxTcye_AdIH996rAhErISJb9C2WnV1t3L-4Hs_3mwgDR3VQ01_hO0YyeVUyJStNe5_En4LEsqt33HxblWNyKx-WWC1jmixieeL-IvwqkxsUfYmTmYa4HVSWeABChafFWZtAP_RekKCGKTb-wv_M=', start_index=11130)
Annotation(end_index=11152, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYSnYjUnzRGRdDc5ck6ZsEAqAYOgjuqngKpzSw-LFZHYuyHps7lw5Y3Wbb0HMl_yhVxMMiOPrgYP6VEGhkv-9tw7uOf0VQkO1O0ra0EfqEYmBzhmqjPWBvzs5to-7OLEASYkgW3HJ02r3_gN8HZ2o6I9TS3wgnKIWE4hBrpFUGarpUffl-gCdgZLDD86XDPMqkhSdRW2ZSFZI-Gd-x', start_index=11130)
Annotation(end_index=11483, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsRq9nzQn9aYb8Bdk9ZZXrjPRcu9fzri4GY7MDxKxbN48Z7MK3mS_cZgy2IDcii3eTi_bGVPdLaPRj57MEEkXhj2WOSNzV9abYryQT8eFE1wVhLczF6coKYnsyHUEdKYJG7XthPqoplb3GUAjaZTFi_5zH18E=', start_index=11474)
Annotation(end_index=11755, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExYjIiydcReIXpGy1yS2djk5jVvm528XZCRR9GyCwY20ogxRGJ1rbS04teVpIsPkUFoZPeqW68Nsu0t09IxlZ-fdzdK5IAVwT-a0ui6UtbZTl0p1Uq', start_index=11738)
Annotation(end_index=11755, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsRq9nzQn9aYb8Bdk9ZZXrjPRcu9fzri4GY7MDxKxbN48Z7MK3mS_cZgy2IDcii3eTi_bGVPdLaPRj57MEEkXhj2WOSNzV9abYryQT8eFE1wVhLczF6coKYnsyHUEdKYJG7XthPqoplb3GUAjaZTFi_5zH18E=', start_index=11738)
Annotation(end_index=11755, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGApZXUhCha5V7Mu2qLgN4MiiF7LWA29LE52YcKW_4D-RQPNZgAfNm_yVEFRe0NM72NVIvadI37Jq2t5CU9qaydnCZSpgyQil1rzE3_TI5bpjOqmLXeGi3g7GVnwsKFwV6Tn0ChfPW-QTrcHT5PX4wPuVi4V0vCp-r5YlEfpPA1w-5K91g-OxRsdBBqbyrpggGw', start_index=11738)
Annotation(end_index=12405, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQED3BcKNmi1pbv0BzWHWopAM0jMhottYVFQMzGNQyTOUlhsq_gydv-UtyjfHl7192pqxav_BEbcWPuQfUVleQ-vxnF4Ng9oW61Q34w1OqYn_PPOk124zBD9fFQILG81AU2uKHTMfHDRhEaG8Pd5UGVPt09RkIp7bk6VJztoBwK49IyQJBruciIfKf60vg==', start_index=12379)
Annotation(end_index=12405, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETFuE1-n2w9NBeGCgspeS0BX5NA0LDfGL9RpWPgqgYwXS-uRaI1Y2juVxV8CKcL2JhfgWnZ05gD2HPBwU8Wi5YBsiM1lg4FGiTWNwBSrJHq7g4qSClqMUZuynjeydTaPNpH5C54gJlk3Pp5igVC6A1ZTibkYqBdVd3XhGNwLuBU1zu9mVNfGkUZp7OjKLgHggXzHjMvCoDthAlaKXgElIAsg8QYh28m4Klq_dzqXcjj8CDZF-Jo7faMyDDFfrayT-MEQ==', start_index=12379)
Annotation(end_index=12405, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGF21VxBY3wytmegxfb58whuOqtE7VxScYW3nkypNAEOJEoseL5PsCqo9WkxEyuWKsawgkOaGewXqtTlp1dGrU57EV38gSZjL_gy-35FIp7peBiaWcvc3PAMZoaJFjxdEQbyKKDe7Qx030bmyW7IGivcRZUNNu5_6PVVjOxSxEEyr4LV6GcXA==', start_index=12379)
Annotation(end_index=12405, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgyjTNZSISYr-IY2KHBNb6Pmvem5f6tctbdspJH0Gt2VQBEUnKapGNtFbMnTMeNii5EdteGlTw2TIx5fMJjigkQtfovUmW5xoMSSTiWEF6KqGMkflFxD9k5DUIL8i2KA==', start_index=12379)
Annotation(end_index=12405, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHN9ltRqQx94mngHd6SKD4hzUOqYY0GqPBSFvnT1m7BsUEzyQtdclI-NE6_FS4V1MmOcKKWZeJcHM24WN8rnRJzFLzmjntjFNpcys-YjWNoIQT0Dt9tBulvfQ0tBNn8ge3i_qPj82R2psWQ', start_index=12379)
Annotation(end_index=12632, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJJ3SwSZvi60sA5Jd0vSmudqDDlpyVHDXOqXtH0fELzb1sMrSv4TAORILqwx1VPZDR4ue4v8yx76I1EkUZMpyq_OcQEZ5KMrXUfzlu7NihaX8J-JNUjlAJqRwIps5jbpuhQH4IqF8E8zP4uaaIWfx9346-6Jj-L-lX2OeKFWxJoVB9eVdEUnZ-xPBCijaHPPnzGjiFhBcaagcFv0YybqQLs_0yY52ATYZSJIWVc1svlvegFvcj4wCcD--2', start_index=12618)
Annotation(end_index=12632, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlWsLKzWbz9aeT8h0Ewtaujxc2LXGbBAdot7WXoxoS8IwQQAgjCI_w4FCQWYu2DBeqchwzTAOu3ojQLABIJW1HRk2F-N2_4pY6yGiL5YfX2h2AYAaYklB8SWMvoa3a7StTGx2PdDWXBN6WhGYamLmzaf9yTiquSsXSFkXSp2Z4I8LrV9uSBVbHhxBF', start_index=12618)
Annotation(end_index=13030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvCTcOpxcMGt48z2mS2A5WusS2bjs6JIjDGcjZNGPMDuKLnHzfexxRucqZv-yisOvotWl-EJ8R2xP-eZ2MMSDIo6aHg7_UBGDnwq4TTUA_AzAePxzYIfU0RV2JyJzxAf--kWSn_EEVeQbwErjurgJ-', start_index=13012)
Annotation(end_index=13030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4YfTOtIjvGbg76JIM7uH0ZX7NvapaBSyU8yuApGCNtLhXmCmgfXgfKp59HJH3c4hBcc84L2_GJPlCP0w5R-TvK3PmyPPnJXzBvWH4TbpdkvUfRIF5dO6ME-P00QxLDaolcgSM_c-TzjXo9lhJzqrHg9NE33WojIlkYBktrweny12aJRhst7O9Cku8EakCyQSMRvY=', start_index=13012)
Annotation(end_index=13030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlWsLKzWbz9aeT8h0Ewtaujxc2LXGbBAdot7WXoxoS8IwQQAgjCI_w4FCQWYu2DBeqchwzTAOu3ojQLABIJW1HRk2F-N2_4pY6yGiL5YfX2h2AYAaYklB8SWMvoa3a7StTGx2PdDWXBN6WhGYamLmzaf9yTiquSsXSFkXSp2Z4I8LrV9uSBVbHhxBF', start_index=13012)
Annotation(end_index=13494, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_wPa0uxYkyAbeH51122GAaZdOVHY7YHwy7OV-sFrNyFebBo1ww1z6E_2tcIKnRDRlEyZ847Yg6AXFYFCoeAgkPqdfiEEUZtqJYjGtTLqVX46NnEFkQ1O5dtfdty8NBQEoMEg6NAj6QLMDxrXtZPSajtAxqbQ72Jp9MfKC6BimvUwBvmynr-zpXLhmGw==', start_index=13476)
Annotation(end_index=13494, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvCTcOpxcMGt48z2mS2A5WusS2bjs6JIjDGcjZNGPMDuKLnHzfexxRucqZv-yisOvotWl-EJ8R2xP-eZ2MMSDIo6aHg7_UBGDnwq4TTUA_AzAePxzYIfU0RV2JyJzxAf--kWSn_EEVeQbwErjurgJ-', start_index=13476)
Annotation(end_index=13494, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlWsLKzWbz9aeT8h0Ewtaujxc2LXGbBAdot7WXoxoS8IwQQAgjCI_w4FCQWYu2DBeqchwzTAOu3ojQLABIJW1HRk2F-N2_4pY6yGiL5YfX2h2AYAaYklB8SWMvoa3a7StTGx2PdDWXBN6WhGYamLmzaf9yTiquSsXSFkXSp2Z4I8LrV9uSBVbHhxBF', start_index=13476)
Annotation(end_index=13795, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmZpab3do3IaaXUTSUPQxYUC1gnWxGWvZ5PW8XiLJq5kZOjVI7LW_HkelCtsS1eeo9M3rjfmrXK9I42jFg9bCaQtl8sWNYf5IhwUKOpBPGEO2M3vRwpPt_P_C89x8C9cJlkM9gon0IoUgIAjDCgjWIjh17', start_index=13781)
Annotation(end_index=13795, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmA1iM4FZKLOuyxJDP3Hu8F2v8hGChfFZ8S5L-lTbh6FEMWPflIWyrdAt4SPIlG1f2bBt_P4FzpRj5xdlH-cuD_mTrS6H-XDlyJp4lOzyK9fQpxW3DaahFifA5KQo1vCoLzqxH6F1Kdwvqkptq2ecjH0sBdAaSEK8=', start_index=13781)
Annotation(end_index=13862, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPGMi7RGr1q1XhdNRzzQhNawuYra4MSSFxeVadRW5QEsfOAvd0jDkFGXmk0dpqJv-thvQ3Qfj6VBl8LmK7_Jz7rvWot6C7XUa98s19Gbpnu3Q9VFy7qyHH6zRa4cW55-_ehyX3ZFwN47jkPmQ=', start_index=13850)
Annotation(end_index=13862, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJnWS9CC4wu6CHBu-bc60D6Kt1oaz3PKtpkm1GqwvpeioBtH1kKGnkVgsWtQLswjBTGjnQf9GPYRN4LYwhqeCHV6xLQkIm5vgwRIo3wCEKij-lg5f4rHuO3j22P3exsh1FmT7PMefKolRleHT3SNE1lFWBC4cMCj9y', start_index=13850)
Annotation(end_index=14008, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRWXxLuDbVDCcQRxGOoOJ7YFjk1rh7H-ygrzYTEkEH1pzzZREHukCUC22B4MZKvKqNQ8X_2UUN85_f6iiLDbDZVVJnb5Z2ikiyjpbJpL806eMtlB1ezkf7Hgs5Dbtsb2LqZ0kPBxd04_JQHnJch8_ZMuVHDNDWV8_bDFfj3xu9YC6WilVLwqidcb9iPw==', start_index=13998)
Annotation(end_index=14106, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPGMi7RGr1q1XhdNRzzQhNawuYra4MSSFxeVadRW5QEsfOAvd0jDkFGXmk0dpqJv-thvQ3Qfj6VBl8LmK7_Jz7rvWot6C7XUa98s19Gbpnu3Q9VFy7qyHH6zRa4cW55-_ehyX3ZFwN47jkPmQ=', start_index=14093)
Annotation(end_index=14106, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkSfR1COGvhtlKh0HcXO2k-UieG51QCnUeN2UbzBLaCyJSUtCMnroTcKMlOGZLo6jZTvO10sJ8Sd7dMqaRjwGwYoxEG6Bs_m7lrZwx0n0z-zAd-5mhK_Mrk6O3QzmBAwQpNefehp2ithSemrnfGQ==', start_index=14093)
Annotation(end_index=14251, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1YB_KRzFeCjjOeva6lbXC0Gd5hRvmErua2LCwDvEYIsvlXNmjpGHCGlLz-4zOiqVKI2sraEJf15JdtE5GwCgkEfumL14XZxXhpgc5sgkPEOJ5XsgRuKRavrW_K-UdJyJvI68Qf2GdZcEXlkE9-7Bdzw==', start_index=14237)
Annotation(end_index=14251, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGung8nveqPCP8DeVU3MUbb84YsibEdWLFgPx1waOofG45bsfVAS6Z3YL9nTlV77BpCSYR8PfpjR1VqULNjpJrJeu3DDoI03kv2__ywm7vwl7M8tqccMadT9EBtDTMrf7Kw5dTBFASx5Gpfl-95Q3CVBj0sPLAb_lUbMRBY70OL5Qf_', start_index=14237)
Annotation(end_index=14345, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmao8rtXFZw7ckSGIJHOXmivof9BOFfxCdy2L3d9eYE8vICyJ90oABTDE3hp0ARcK5rG0Zcpm8d01d9krf1myTC715oJU4LzwpmGVVPYTA2d7da6V30YCqW9VBa40g9ebXyQGaYzMbZHcuBUN3gViZuJ1n-oHWYxQxdlXBhDItYqUACOCunNXgQjadLCw=', start_index=14331)
Annotation(end_index=14345, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmpR3U9-5bSBnZus6nRfYdvHZsAkafgguxavS0JAclHjupOLSK9taKXOgzXs4KkucsLZZeByj2Ri2HSxekud4c1YlXJhDleFRHKSdy9yFaZ0X_-xz1jF9zFjZLX58o0MMH7weQaSBz6wmJmEOu9YWyBl_3-4TY_Ji1djL0fL7_cqeOk238NsvAEPQ5bazGPCFeuPXVoOxpkY47XhXcVmIJ92cc3vqh3g==', start_index=14331)
Annotation(end_index=14509, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7AVCJ62phWxUpjcLfUikinEKS6eO9nF8mTBVZabc-znpnncePQMW7lhfTQjDrMDZhZ4CAGfhIIEFbntuZQm4u_GfaUryiZNA8NHLvyitiGhC_5INYj8dINBqclNLzKFn13Lx8741oGaxlseOK9nfl_Fn23e-kaCG2vA==', start_index=14495)
Annotation(end_index=14509, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGBoDPsMQgKdLtpQ36Uvz5HAKkv5UZj-XBlxJGD5oaCIt1aRKT3agTxE5dM7TOHA8LCFbA2IBsLo8s46Z5rIm2zpnt3SrgOGwKKzeGeqo6Cw48uSUuSUdtDuieGSSXzBSMG9s-nm2AMn2_-g==', start_index=14495)
Annotation(end_index=14603, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFe28QLUHmQy5JQk8ipZ6hU6-5M1mFQw-QnubFEpsoq0RNoNrWLTfw1cvWcFZfNEmGw790dPPxCnePpU-upd-nq81UHIjiXhn2xvo5GsJY-S9zOEttS7C4ZGluXtksCyEux4luviZFx_M1kF1xKau6oQqS9gUSpMzK448v1DQc=', start_index=14589)
Annotation(end_index=14603, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFinIDhKRE4oxTcye_AdIH996rAhErISJb9C2WnV1t3L-4Hs_3mwgDR3VQ01_hO0YyeVUyJStNe5_En4LEsqt33HxblWNyKx-WWC1jmixieeL-IvwqkxsUfYmTmYa4HVSWeABChafFWZtAP_RekKCGKTb-wv_M=', start_index=14589)
Annotation(end_index=14731, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExYjIiydcReIXpGy1yS2djk5jVvm528XZCRR9GyCwY20ogxRGJ1rbS04teVpIsPkUFoZPeqW68Nsu0t09IxlZ-fdzdK5IAVwT-a0ui6UtbZTl0p1Uq', start_index=14718)
Annotation(end_index=14731, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsRq9nzQn9aYb8Bdk9ZZXrjPRcu9fzri4GY7MDxKxbN48Z7MK3mS_cZgy2IDcii3eTi_bGVPdLaPRj57MEEkXhj2WOSNzV9abYryQT8eFE1wVhLczF6coKYnsyHUEdKYJG7XthPqoplb3GUAjaZTFi_5zH18E=', start_index=14718)
Annotation(end_index=14804, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGApZXUhCha5V7Mu2qLgN4MiiF7LWA29LE52YcKW_4D-RQPNZgAfNm_yVEFRe0NM72NVIvadI37Jq2t5CU9qaydnCZSpgyQil1rzE3_TI5bpjOqmLXeGi3g7GVnwsKFwV6Tn0ChfPW-QTrcHT5PX4wPuVi4V0vCp-r5YlEfpPA1w-5K91g-OxRsdBBqbyrpggGw', start_index=14790)
Annotation(end_index=14804, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGF21VxBY3wytmegxfb58whuOqtE7VxScYW3nkypNAEOJEoseL5PsCqo9WkxEyuWKsawgkOaGewXqtTlp1dGrU57EV38gSZjL_gy-35FIp7peBiaWcvc3PAMZoaJFjxdEQbyKKDe7Qx030bmyW7IGivcRZUNNu5_6PVVjOxSxEEyr4LV6GcXA==', start_index=14790)
Annotation(end_index=14948, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJJ3SwSZvi60sA5Jd0vSmudqDDlpyVHDXOqXtH0fELzb1sMrSv4TAORILqwx1VPZDR4ue4v8yx76I1EkUZMpyq_OcQEZ5KMrXUfzlu7NihaX8J-JNUjlAJqRwIps5jbpuhQH4IqF8E8zP4uaaIWfx9346-6Jj-L-lX2OeKFWxJoVB9eVdEUnZ-xPBCijaHPPnzGjiFhBcaagcFv0YybqQLs_0yY52ATYZSJIWVc1svlvegFvcj4wCcD--2', start_index=14938)
Annotation(end_index=15024, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvCTcOpxcMGt48z2mS2A5WusS2bjs6JIjDGcjZNGPMDuKLnHzfexxRucqZv-yisOvotWl-EJ8R2xP-eZ2MMSDIo6aHg7_UBGDnwq4TTUA_AzAePxzYIfU0RV2JyJzxAf--kWSn_EEVeQbwErjurgJ-', start_index=15010)
Annotation(end_index=15024, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvYX7l5JTppIBFOHvT9UBHMxYevDQMj1-i1EfvzjBPnPyE6S7Comt1ROGVoA38aq7EmO326nIGmtun4eqFlEWD25YTBnxTPTha6FJITFVF7GYFkYtxFQH4llp8gTIAbzyDZS-gxYCUs2h4snn5Z4gko_zs7NtlvVQhVXm22MTaSNXUSG4i-0BS3m9zx9eSz9dS', start_index=15010)
Annotation(end_index=15680, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE692IF1S-Ht4x6FU72zypNhdv6qUXkT5_cHl_8ni3Em3LN8VBBYHmHHvS70qbWKe5yqJDolA264HuTE7yRo818HgV0Sn10_Kd87n1YCP_7UHdU0Jij5kB93agh9djsuslzLgHTYA==', start_index=15658)
Annotation(end_index=15680, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKwwum-HRRzq3ioymqKKZM17-vK_n0cWu5rsC5yzjO4koMMR4qW0vFYQ-i_i1ljvtExuJ871dXGPFauk2uCZS4aKyH3yPAl2cboYOLAvn2xGLq4EApzkfG-NJUUcYxP5QA61_pQCI=', start_index=15658)
Annotation(end_index=15680, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVtGdRNuRPnH14GtskMYKNjJHAJyrbHD8SyF9ZYHOW1xi5mJigfp0zOqiET-7VKQAyYjWnxWVn9b7Pr4cqeRUK0N4KkWNS883r2D2XihzrDy1aMBH-3i3JTZKHwCIP9oSLTuE9Q_gqx8Jq5IlpSug-Z3dUdYRa6zEZaJw30fTzlJgg1WkfRSDHbRU-1F_ctg==', start_index=15658)
Annotation(end_index=15680, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvYX7l5JTppIBFOHvT9UBHMxYevDQMj1-i1EfvzjBPnPyE6S7Comt1ROGVoA38aq7EmO326nIGmtun4eqFlEWD25YTBnxTPTha6FJITFVF7GYFkYtxFQH4llp8gTIAbzyDZS-gxYCUs2h4snn5Z4gko_zs7NtlvVQhVXm22MTaSNXUSG4i-0BS3m9zx9eSz9dS', start_index=15658)
Annotation(end_index=16157, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXwCfcNKbu9Htn73ze0JDroLGof1RauhvsYpWLNlSo7V1iTyKupR6GEqkv6VR5TZDOBjuQL0txvFRvETXjuf1IMnYCVI1uHKvNOkJ2N9y8hX2Z_zIokQTp33LrH29sCCrpgrTO_AZbcUuCMF6MFlQAB6_nBBdd2WI1_mFVvyQuoVFLmslhupsLSVgowZ6f5zhxFBgDNmM=', start_index=16147)
Annotation(end_index=16599, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2SvFgbakYvIb_69cWQIA0aNGj77TTN2avsBB5ph3i_yq8YKv1SawO3PewfA9_nnyH54ZtrEtbmOQUBLlx1xb4zhrRyhLZC8kinU2lZ3nYn-Z1f2Ma8nAONA_L4k5ef48j1epeXUpoGv5dxNqUuwYpI7lsxKjb6NdnAjmZUQNIc3awFtD83t7REB_wOwypx5V_miKFJQ==', start_index=16585)
Annotation(end_index=16599, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHF7rNwH37kZeSpz5jEDvA1ra0PFn8nDQ8rqh6wUqcaiuqkFz45widwuun5cUauysctJ8zRbwazW12uPficmEYcZxRBb-q0Itjl9HIXgnaqiOWhZwHc', start_index=16585)
Annotation(end_index=17361, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJnWS9CC4wu6CHBu-bc60D6Kt1oaz3PKtpkm1GqwvpeioBtH1kKGnkVgsWtQLswjBTGjnQf9GPYRN4LYwhqeCHV6xLQkIm5vgwRIo3wCEKij-lg5f4rHuO3j22P3exsh1FmT7PMefKolRleHT3SNE1lFWBC4cMCj9y', start_index=17352)
Annotation(end_index=17440, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFnAAe8CkDdhPMEjITc3M3_WzoJRj6nLNU6MYUSNIR65VFrEKwirJTfErzfs_lG3XJq0gfUU_Rt3aVg0ZW_d7A3qWZ-jmcz6M-CPSgO_YWGwfXLHH4UwyPlc-xwoe5QRI0QBlwjCtC7x0XZismok8NUeQQsG9GLRXqQX6FW6FFIJo1', start_index=17431)
Annotation(end_index=17498, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmZpab3do3IaaXUTSUPQxYUC1gnWxGWvZ5PW8XiLJq5kZOjVI7LW_HkelCtsS1eeo9M3rjfmrXK9I42jFg9bCaQtl8sWNYf5IhwUKOpBPGEO2M3vRwpPt_P_C89x8C9cJlkM9gon0IoUgIAjDCgjWIjh17', start_index=17484)
Annotation(end_index=17498, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmA1iM4FZKLOuyxJDP3Hu8F2v8hGChfFZ8S5L-lTbh6FEMWPflIWyrdAt4SPIlG1f2bBt_P4FzpRj5xdlH-cuD_mTrS6H-XDlyJp4lOzyK9fQpxW3DaahFifA5KQo1vCoLzqxH6F1Kdwvqkptq2ecjH0sBdAaSEK8=', start_index=17484)
Annotation(end_index=17559, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFapy5V8jBp4rR7GuhLawljFoVQSA1CpiHuU9yomMgpw9qf4qRUAZOhOpYq0M37z84xkU_O_sJSIplPXXKRshRdn5TD-0cd7CmQ5HC8zaUREUB0Xl2ji9WZwampzIN6ppnS', start_index=17550)
Annotation(end_index=17607, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPGMi7RGr1q1XhdNRzzQhNawuYra4MSSFxeVadRW5QEsfOAvd0jDkFGXmk0dpqJv-thvQ3Qfj6VBl8LmK7_Jz7rvWot6C7XUa98s19Gbpnu3Q9VFy7qyHH6zRa4cW55-_ehyX3ZFwN47jkPmQ=', start_index=17598)
Annotation(end_index=17670, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHdNAKAumDSf0rfs8JQSrsBtQ1Q5QqIaVtl8_8BKeGUkGZaASmFiHEN2NuXDLl2Bs9gQOLFqqu8JKw88sSp8Jc7X8TWYGVgNezzzfia1XtyTXjmXM3Eq6Kc-Wt81qasoK2IlzLUQduqFspdKvlV-avZ_oI-ZhxFhbFwNrbLziGmERO2gVLn-tBpyRszH5rh71J', start_index=17657)
Annotation(end_index=17670, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPhH6dU-Updstk-OW1aca6xG4fsONYgKSNu1KL7AmrM-Gi5fUiZ0UdEoY1Ht7LhJ0f0CN3_8WPTHzjbEGSeZZNUkJXLf7RoQi1HNG5_r_nk8lCdrvHbqYDv7LJe-nBXDy8pjvN_-w1taHK2SYD8pIpMgF3UyQWWKolfJAxssNefBbYqAaU-4Gn', start_index=17657)
Annotation(end_index=17729, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGouRbE37WG2fvTul3bYYTO9LmTH991M0Y9evMi7_r0UzqOJax5_cobhuDebuW9WUZeSh-YVXFOPajR76PDEPIhh4q82xklJRXLcJVxau4-sny_kTvit_k8GlK5cm-lcHQzmy7Ec1QuS9aZtC2L96w=', start_index=17719)
Annotation(end_index=17788, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFxRrVAcggSDCFPCR4Zxm9nXlU2VGwvfy40lc0Qucn0EqltL3pMCuwxthR8NwXYoHtx8WDsN8e6zWBeQCXprYlSagH1CbriiDxRgT_wGknfSyFUGNavn_dET3GOmXkHElTTtz4u2wHJ2FifMRC8mrYhe1kgw==', start_index=17779)
Annotation(end_index=17856, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLf3agVjo0AJK-g_uS-1yTrh2uwD_aH8llFThPA3XOgKk-rbCk6ALUUt5swsae32xZwDTXDyItaLkrONF0LQQkQbBL3xTr8lhDY4cFASzj1mJwwAEFlsJJDsLOwZ_nR1gQ-HW9dWfio_gKJwuPLPes4RBbbmPzedQQmo_Xqfy722u4PpaZIo_b3SWfH2mtVoCwXup9jPZkY8A=', start_index=17846)
Annotation(end_index=17958, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGung8nveqPCP8DeVU3MUbb84YsibEdWLFgPx1waOofG45bsfVAS6Z3YL9nTlV77BpCSYR8PfpjR1VqULNjpJrJeu3DDoI03kv2__ywm7vwl7M8tqccMadT9EBtDTMrf7Kw5dTBFASx5Gpfl-95Q3CVBj0sPLAb_lUbMRBY70OL5Qf_', start_index=17948)
Annotation(end_index=18030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRWXxLuDbVDCcQRxGOoOJ7YFjk1rh7H-ygrzYTEkEH1pzzZREHukCUC22B4MZKvKqNQ8X_2UUN85_f6iiLDbDZVVJnb5Z2ikiyjpbJpL806eMtlB1ezkf7Hgs5Dbtsb2LqZ0kPBxd04_JQHnJch8_ZMuVHDNDWV8_bDFfj3xu9YC6WilVLwqidcb9iPw==', start_index=18020)
Annotation(end_index=18100, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5pvsw9sGXgRE5O3v8f4QpOrJf6Sp9w4TuKCIH3ieQluy-3EcE5F2AIUbjWFfD-VT0RGuZI4lzfkPZIOwlaVrQPV8tJUuIEnjBYu8Y6zjoUm5eXEQwVGgBAWCC0lReTZlUnpvaaSsD-bTSoGdJkb8ZHydxeIooujEcbsyPd4YE', start_index=18090)
Annotation(end_index=18161, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsDyr-bXiCI5N4DZGyQFsLiTf7kW3aAIJRi1tvnsKe2bQOzqIoM3KoUi8Q-NPDpEMy3C13ecFncKEicSLXZ0yPy5KrSaLHUx1ff61J72STOYGnSqiN-zYHSVq2LdlUTWiWgIeV-RUxmIE-_7qMlN61VA==', start_index=18152)
Annotation(end_index=18220, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXwCfcNKbu9Htn73ze0JDroLGof1RauhvsYpWLNlSo7V1iTyKupR6GEqkv6VR5TZDOBjuQL0txvFRvETXjuf1IMnYCVI1uHKvNOkJ2N9y8hX2Z_zIokQTp33LrH29sCCrpgrTO_AZbcUuCMF6MFlQAB6_nBBdd2WI1_mFVvyQuoVFLmslhupsLSVgowZ6f5zhxFBgDNmM=', start_index=18210)
Annotation(end_index=18315, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRdSmgwQgZq_5PNvvGZbsPNeMsuIOq0Csd6-xhF2rv5jQMwzQGNsUF2NM_Fa7SUjq3ZiRfcdqqgDwWWMP2yUI6tVfwUZUPLVGgOtzNMROm3DLpdjHJXrJIKmlzBFv_-FYgMHhEATzoe7a_XkITt9NjZBMMffzvzgyFfDGO7p5ABNzG9UMRoH6p13OQPDMXUODxWLBKUPfuvaCdBcXlXbMNY_olaZZ4ImwWsmnaw5dEilO6', start_index=18305)
Annotation(end_index=18381, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1YB_KRzFeCjjOeva6lbXC0Gd5hRvmErua2LCwDvEYIsvlXNmjpGHCGlLz-4zOiqVKI2sraEJf15JdtE5GwCgkEfumL14XZxXhpgc5sgkPEOJ5XsgRuKRavrW_K-UdJyJvI68Qf2GdZcEXlkE9-7Bdzw==', start_index=18371)
Annotation(end_index=18442, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2SvFgbakYvIb_69cWQIA0aNGj77TTN2avsBB5ph3i_yq8YKv1SawO3PewfA9_nnyH54ZtrEtbmOQUBLlx1xb4zhrRyhLZC8kinU2lZ3nYn-Z1f2Ma8nAONA_L4k5ef48j1epeXUpoGv5dxNqUuwYpI7lsxKjb6NdnAjmZUQNIc3awFtD83t7REB_wOwypx5V_miKFJQ==', start_index=18432)
Annotation(end_index=18535, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFys7n7swyANW6bUif_Evzi4-sTLa9NRUaJ1Gqd3dA_dNFwz9PNnNitEGxbY0NK8EVZpRKvhxUUhNnETcVsJf_wfH9iCmYbUdc0wzGN5j4JOEB0R9VluMJh9m-Pbcfe5gvz1vAQWCHvjvPCSf2OTupfvVVXCynfFOVd8jvnbaE3d-4ZtnDDi1S5vMoJa7Hmo7jO7sFlA0nyRMJ59Q==', start_index=18525)
Annotation(end_index=18619, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkSfR1COGvhtlKh0HcXO2k-UieG51QCnUeN2UbzBLaCyJSUtCMnroTcKMlOGZLo6jZTvO10sJ8Sd7dMqaRjwGwYoxEG6Bs_m7lrZwx0n0z-zAd-5mhK_Mrk6O3QzmBAwQpNefehp2ithSemrnfGQ==', start_index=18609)
Annotation(end_index=18678, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJJ3SwSZvi60sA5Jd0vSmudqDDlpyVHDXOqXtH0fELzb1sMrSv4TAORILqwx1VPZDR4ue4v8yx76I1EkUZMpyq_OcQEZ5KMrXUfzlu7NihaX8J-JNUjlAJqRwIps5jbpuhQH4IqF8E8zP4uaaIWfx9346-6Jj-L-lX2OeKFWxJoVB9eVdEUnZ-xPBCijaHPPnzGjiFhBcaagcFv0YybqQLs_0yY52ATYZSJIWVc1svlvegFvcj4wCcD--2', start_index=18668)
Annotation(end_index=18742, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlWsLKzWbz9aeT8h0Ewtaujxc2LXGbBAdot7WXoxoS8IwQQAgjCI_w4FCQWYu2DBeqchwzTAOu3ojQLABIJW1HRk2F-N2_4pY6yGiL5YfX2h2AYAaYklB8SWMvoa3a7StTGx2PdDWXBN6WhGYamLmzaf9yTiquSsXSFkXSp2Z4I8LrV9uSBVbHhxBF', start_index=18732)
Annotation(end_index=18816, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGBoDPsMQgKdLtpQ36Uvz5HAKkv5UZj-XBlxJGD5oaCIt1aRKT3agTxE5dM7TOHA8LCFbA2IBsLo8s46Z5rIm2zpnt3SrgOGwKKzeGeqo6Cw48uSUuSUdtDuieGSSXzBSMG9s-nm2AMn2_-g==', start_index=18806)
Annotation(end_index=18888, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFe28QLUHmQy5JQk8ipZ6hU6-5M1mFQw-QnubFEpsoq0RNoNrWLTfw1cvWcFZfNEmGw790dPPxCnePpU-upd-nq81UHIjiXhn2xvo5GsJY-S9zOEttS7C4ZGluXtksCyEux4luviZFx_M1kF1xKau6oQqS9gUSpMzK448v1DQc=', start_index=18878)
Annotation(end_index=18967, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVtGdRNuRPnH14GtskMYKNjJHAJyrbHD8SyF9ZYHOW1xi5mJigfp0zOqiET-7VKQAyYjWnxWVn9b7Pr4cqeRUK0N4KkWNS883r2D2XihzrDy1aMBH-3i3JTZKHwCIP9oSLTuE9Q_gqx8Jq5IlpSug-Z3dUdYRa6zEZaJw30fTzlJgg1WkfRSDHbRU-1F_ctg==', start_index=18957)
Annotation(end_index=19042, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHN9ltRqQx94mngHd6SKD4hzUOqYY0GqPBSFvnT1m7BsUEzyQtdclI-NE6_FS4V1MmOcKKWZeJcHM24WN8rnRJzFLzmjntjFNpcys-YjWNoIQT0Dt9tBulvfQ0tBNn8ge3i_qPj82R2psWQ', start_index=19032)
Annotation(end_index=19094, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExYjIiydcReIXpGy1yS2djk5jVvm528XZCRR9GyCwY20ogxRGJ1rbS04teVpIsPkUFoZPeqW68Nsu0t09IxlZ-fdzdK5IAVwT-a0ui6UtbZTl0p1Uq', start_index=19084)
Annotation(end_index=19154, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsRq9nzQn9aYb8Bdk9ZZXrjPRcu9fzri4GY7MDxKxbN48Z7MK3mS_cZgy2IDcii3eTi_bGVPdLaPRj57MEEkXhj2WOSNzV9abYryQT8eFE1wVhLczF6coKYnsyHUEdKYJG7XthPqoplb3GUAjaZTFi_5zH18E=', start_index=19145)
Annotation(end_index=19226, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7AVCJ62phWxUpjcLfUikinEKS6eO9nF8mTBVZabc-znpnncePQMW7lhfTQjDrMDZhZ4CAGfhIIEFbntuZQm4u_GfaUryiZNA8NHLvyitiGhC_5INYj8dINBqclNLzKFn13Lx8741oGaxlseOK9nfl_Fn23e-kaCG2vA==', start_index=19216)
Annotation(end_index=19295, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsRq9nzQn9aYb8Bdk9ZZXrjPRcu9fzri4GY7MDxKxbN48Z7MK3mS_cZgy2IDcii3eTi_bGVPdLaPRj57MEEkXhj2WOSNzV9abYryQT8eFE1wVhLczF6coKYnsyHUEdKYJG7XthPqoplb3GUAjaZTFi_5zH18E=', start_index=19286)
Annotation(end_index=19363, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHF7rNwH37kZeSpz5jEDvA1ra0PFn8nDQ8rqh6wUqcaiuqkFz45widwuun5cUauysctJ8zRbwazW12uPficmEYcZxRBb-q0Itjl9HIXgnaqiOWhZwHc', start_index=19353)
Annotation(end_index=19436, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvCTcOpxcMGt48z2mS2A5WusS2bjs6JIjDGcjZNGPMDuKLnHzfexxRucqZv-yisOvotWl-EJ8R2xP-eZ2MMSDIo6aHg7_UBGDnwq4TTUA_AzAePxzYIfU0RV2JyJzxAf--kWSn_EEVeQbwErjurgJ-', start_index=19426)

## Sources
