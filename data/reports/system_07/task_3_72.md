# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 508d40cc | **Time:** 24.66s | **Cost:** $0.02163
--------------------------------------------------------------------------------

In a point-incentive mechanism the "gradient" is the marginal value of the next point.  
Designing that gradient is nothing more than deciding how much extra benefit a user gets when he crosses the next point threshold.  
There are only three levers you can pull, and every successful program combines them in a way that (a) feels fair, (b) is easy to explain, and (c) still pays for itself.

1. Threshold spacing (how far apart the rungs are)  
2. Reward jump at each rung (how much better the perk becomes)  
3. Point-earning multiplier (how fast you climb toward the next rung)

Below is the cookbook that practitioners actually use.

--------------------------------------------------
1. Pick the currency first
--------------------------------------------------
- 1 point per 1 currency unit spent is the cognitive baseline.  
- Keep the *nominal* numbers small: 100 pts = \$1 feels richer than 1 pt = \$0.01.  
- Fix the *real* value early: target a 1–3 % give-back for the base tier; you will give away more at the top, so model the blended cost at every tier before you go live.

--------------------------------------------------
2. Draw the tier ladder
--------------------------------------------------
Three to five tiers is the sweet spot; more tiers create noise, fewer feel trivial.

Typical spacing (annual spend or trailing 12-month points):

Tier 0 (entry)     0  
Tier 1             100–499 pts  
Tier 2             500–1 999  
Tier 3             2 000–4 999  
Tier 4             5 000+

The *width* of each band controls the gradient:

- Narrow bands (2× jump every time) → steep gradient, short-term binge.  
- Wide bands (3–4× jump) → shallow gradient, long-term retention.

Most retail programs use a 3–4× width because it matches the natural cadence of Christmas + one big discretionary purchase per year.

--------------------------------------------------
3. Attach a “delta” reward to every crossing
--------------------------------------------------
Users must *feel* the upgrade. The smallest noticeable reward is roughly a 25 % lift in the perk they already care about.

Example gradient (cash-back language, but same idea for miles, status, etc.)

Tier 0   1 pt/\$1   → 1 % voucher  
Tier 1   1 pt/\$1   → 1 % voucher + free shipping  
Tier 2   1.25 pt/\$1 → 1.25 % + free ship + birthday gift  
Tier 3   1.5 pt/\$1 → 1.5 % + free expedited + 24 h early access  
Tier 4   2 pt/\$1   → 2 % + all above + concierge line

Notice the *marginal* jump is never smaller than 25 % (1 → 1.25 → 1.5 → 2).

--------------------------------------------------
4. Use multipliers to steepen the gradient without busting the budget
--------------------------------------------------
Instead of giving 2 % back to everyone, give 1 % base and *temporarily* 2×–5× points on selected actions or products.  
This lets you:

- steepen the perceived gradient (user sees 200 pts instead of 40),  
- keep the *nominal* reward liability unchanged,  
- steer behaviour (clear slow-moving SKUs, push app orders, etc.).

--------------------------------------------------
5. Add a soft floor and a hard cliff
--------------------------------------------------
- Soft floor: if a user drops below the threshold, downgrade only after a 12-month grace period; keeps the emotional pain low.  
- Hard cliff: points expire after N months idle; prevents infinite liability and forces periodic re-engagement.

--------------------------------------------------
6. Check the maths: blended cost ≤ contribution margin
--------------------------------------------------
Work backwards:

1. Forecast spend per tier.  
2. Multiply by the *effective* earn rate (base × multiplier × promo share).  
3. Multiply by the *cost* of each point (reward face value × breakage).  
4. Ensure the sum is < incremental margin – 1 % (leave headroom for error).

If the gradient is too rich, widen the bands or lower the multiplier first—never cut the headline reward once the program is live.

--------------------------------------------------
7. Communicate the gradient in one sentence
--------------------------------------------------
“Every \$1 you spend earns at least 1 point; hit 500 points and we start giving you 25 % more on every purchase, forever.”  
If you cannot explain the next benefit in one line, the gradient is too complex.

--------------------------------------------------
Quick reference cheat-sheet
--------------------------------------------------
- 3–5 tiers, 3–4× spend width each.  
- Marginal perk lift ≥ 25 %.  
- Point multiplier 1 → 1.25 → 1.5 → 2.  
- Blended give-back 1–3 % base, 4–6 % top tier.  
- 12-month grace, 24-month expiry.  
- Model breakage; never exceed 50 % of promo points unredeemed.

Apply those six numbers and you have a reward distribution gradient that feels steep enough to climb but flat enough to fund.

## Annotations


## Sources
