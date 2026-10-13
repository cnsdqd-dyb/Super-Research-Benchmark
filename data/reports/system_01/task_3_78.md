# Deep Research Report: alibaba/tongyi-deepresearch-30b-a3b
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** fd95f93b | **Time:** 24.99s | **Cost:** $0.00062
--------------------------------------------------------------------------------

The attribution weight assigned to each marketing touchpoint in a conversion path is determined by **the specific attribution model used and its underlying rules or algorithms**. There's no single universal method, but several established approaches:

### Core Attribution Models & How They Assign Weights:
1.  **First-Touch (Attribution):**
    *   **Weights:** **100%** to the *first* interaction.
    *   **Rationale:** Credits the initial lead/awareness driver as the key influencer. Ignores subsequent interactions.

2.  **Last-Touch (Attribution):**
    *   **Weights:** **100%** to the *last* interaction before conversion.
    *   **Rationale:** Credits the final push/closing action. Most common historically (e.g., eCommerce cart abandonment).
    *   **Also Known As:** Last Click.

3.  **Linear Attribution:**
    *   **Weights:** **Equal weight (1/N)** to *every* interaction in the path (where N = number of unique clicks/touchpoints).
    *   **Rationale:** Assesses each interaction's contribution equally, acknowledging all played a role.

4.  **Time-Decay Attribution:**
    *   **Weights:** Increases weight for interactions closer in time to the conversion.
    *   **Rationale:** Assumes the immediate precursor to the conversion has the strongest influence. Often weights interactions exponentially closer.

5.  **Position-Based (MDirect, U-Shaped, etc.):**
    *   **Weights:** High weight (e.g., 40%) to the First and/or Last interaction, with the remaining weight distributed equally among middle interactions (e.g., 20% to each middle touchpoint, 40% first, 40% last).
    *   **Rationale:** Acknowledges the importance of initial awareness/lead generation *and* the final push, while still crediting useful consideration/middle-stage interactions.

6.  **Algorithmic / Data-Driven Attribution (DDA):** (Most advanced)
    *   **Weights:** Derived using statistical models and machine learning on historical conversion data. Common methods include:
        *   **Markov Chain Models:** Calculate the probability that a user would convert *if one touchpoint were removed*, reflecting its marginal contribution. Weights are derived mathematically from transition probabilities between touchpoints.
        *   **Multivariate Regression / Regression Modeling (GLM):** Model the complex relationship between multiple marketing channels/touches and the conversion outcome, isolating their individual contributions.
        *   **Shapley Value:** A game theory solution calculating the average marginal contribution of each channel across *all possible combinations* it could appear in a conversion path.
    *   **Rationale:** Uses empirical data to objectively assign value based on actual historical performance patterns, aiming for the most accurate reflection of each touch's influence.

### Key Factors Influencing Weight Determination:
*   **Model Choice:** The marketer/analyst chooses the model based on goals (awareness, direct response), stage of sales funnel, industry norms, and available data.
*   **Path Data Availability:** Algorithms require sufficient interaction data per user path. Click-through data is essential; view-through often harder to attribute accurately.
*   **Conversion Definition:** The specific event defining a "conversion" (e.g., purchase, sign-up) impacts how touchpoints are weighted.
*   **Attribution Window:** The time period considered between the initial interaction and the conversion (e.g., 7-day click, 1-day view). Touches outside this window receive no credit.

### Evaluating Attribution Models:
No model is perfect. Effectiveness is judged by:
1.  **Incrementality Testing:** Comparing results from campaigns attributed using different models against controlled experiments where channels are deliberately suppressed/boosted offline to measure *actual* impact.
2.  **Business Goal Alignment:** Does the model support stated strategic goals (e.g., brand awareness leans towards First-Touch/U-Shaped; direct sales leans towards Last-Touch or certain DDA outcomes)?
3.  **Cross-Channel Consistency:** Does the attribution make sense when viewed across different marketing channels and campaigns?

**In Summary:** Attribution weights are not "discovered" but are **assigned by the rules of the chosen model**. Simple models (First, Last, Linear, Position-Based) use predetermined formulas. Advanced models (Algorithmic/DA) use statistical methods and historical data to calculate weights dynamically based on the actual observed impact of each touchpoint within the full customer journey. The choice of model reflects business strategy and available data.

## Annotations


## Sources
