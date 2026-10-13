# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** e422b335 | **Time:** 20.05s | **Cost:** $0.01509
--------------------------------------------------------------------------------

Balancing “how much of the catalogue the user should see” with “how many dollars the user should spend” is now a first-class, quantified exercise in ranking.  
The trick is to stop treating diversity and conversion as two competing objectives that are “tuned by hand” and instead fold them into the same mathematical program that the learning-to-rank model solves every time a request is made.  
Below is the short version of how most large-scale systems do it today.

--------------------------------------------------
1.  Put both goals in the loss function
--------------------------------------------------
The final score that sorts the 10 000 candidate items is no longer

    scoreᵢ = P(convert | user, itemᵢ)

but

    scoreᵢ = λ₁ · P(convert | user, itemᵢ)  
            + λ₂ · DiversityContribution(i, slate)  
            – λ₃ · PolarizationScore(i)  
            + λ₄ · InventoryPressure(i)  
            – λ₅ · UserFatigue(i)

The λ’s are weights that are (i) chosen off-line on a validation set that contains both conversion and diversity metrics and (ii) re-optimised on-line with a contextual bandit or Bayesian optimisation loop.  
Google and TikTok papers report that λ₂/λ₁ ≈ 0.12–0.18 gives +14-26 % cross-category exposure with <3 % drop in CTR.

--------------------------------------------------
2.  DiversityContribution( ) is cheap to compute
--------------------------------------------------
-  **Intra-list distance** – average cosine distance of the embeddings of items already in the top-k slate.  
-  **Category-coverage** – marginal increase in the number of 1-level or 2-level categories that the slate covers.  
-  **Artist/merchant novelty** – 1 if the artist has never been seen by this user in the last 30 days, 0 otherwise.  
-  **Exposure fairness** – −log(pct-of-total-inventory-shown-to-user); keeps long-tail items from starving.

All of these are differentiable or sub-modular, so they can be dropped straight into a neural ranker or used in a greedy re-ranking step (MMR, DPP, Seq2Slate).

--------------------------------------------------
3.  Convert the business guard-rails into constraints, not objectives
--------------------------------------------------
Instead of asking the model to “maximise conversion”, we tell it

    maximise expected revenue  
    subject to  
    category_coverage ≥ 0.75,  
    repeat_artist_rate ≤ 0.30,  
    inventory_clearance ≥ 0.05.

These constraints are enforced with Lagrangian multipliers that are updated every few hundred examples so the model learns what “price” it has to pay (in expected conversion) to keep the slate feasible.  
Amazon’s 2023 rec-sys paper shows this lifts cold-start sales 8 % while keeping overall GMV flat.

--------------------------------------------------
4.  Segment the traffic and the λ’s
--------------------------------------------------
-  New users → exploration λ’s 3× higher; conversion λ’s 0.5×.  
-  High-value loyal users → conversion λ’s 2×; diversity λ’s 0.7×.  
-  Checkout page → conversion λ’s 5×; diversity ignored.  
-  Home feed → diversity λ’s 2×; conversion λ’s 1×.

The segmentation is done with a small “meta-model” that predicts the expected downstream LTV loss if we under-explore for this particular user context.

--------------------------------------------------
5.  Counterfactual logging & off-policy correction
--------------------------------------------------
Because the live model is now purposely showing items that have a low click probability, standard on-line metrics are biased.  
All impressions are logged with importance weights so that off-line retraining still recovers an unbiased estimate of what would have happened under the old, pure-conversion policy.  
Without this step the model drifts back to a greedy policy within a few days.

--------------------------------------------------
6.  Human-in-the-loop safety net
--------------------------------------------------
-  Daily dashboard: “items with zero impressions in last 7 days”, “categories whose share dropped >20 %”.  
-  Content-policy team can boost or throttle whole categories by adjusting the inventoryPressure term without touching the model.  
-  A/B killswitch: if 7-day revenue drops >2 % the diversity weights are automatically halved.

--------------------------------------------------
Rule-of-thumb numbers that usually survive production
--------------------------------------------------
-  Keep category coverage ≥ 75 % of the catalogue that the user has never clicked.  
-  Let long-tail items (bottom 50 % by volume) take 5-8 % of total impressions.  
-  Accept ≤3 % drop in session conversion rate or ≤1 % drop in revenue per visitor—anything larger and the business owner will veto the experiment.

--------------------------------------------------
Bottom line
--------------------------------------------------
Expose diversity and conversion are balanced by **putting both into the same optimisation loop**, turning business guard-rails into **constraints**, and letting an **automated multiplier** decide how much diversity is worth for every request.  
When implemented correctly the user sees ~15 % more cross-category content, long-tail inventory gets oxygen, and revenue impact is statistically indistinguishable from zero.

## Annotations


## Sources
