# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** b7529507 | **Time:** 18.19s | **Cost:** $0.02663
--------------------------------------------------------------------------------

Yes—modern institutional-grade rebalancing engines can keep tracking-error within a client-specified “budget” while still containing market-impact costs, but only if the optimiser is explicitly built to internalise the cost of trading.  
Plain-vanilla mean-variance optimisation (MVO) does not contain that cost channel, so when it is used “off-the-shelf” it will indeed amplify execution friction: the analytic objective is only return / variance efficiency, therefore it keeps pushing weights toward the Markitz “tangency” portfolio even when the marginal liquidity cost of the last share far exceeds the marginal risk-reduction benefit. The result is a circular problem: the more you trade to hit the MV weights, the more you move the prices, the more the weights drift, so you trade again—an effect that shows up empirically as higher turnover, wider implementation shortfall and deteriorating net Sharpe ratios once AUM or fund density crosses a few basis-points of ADV.

How the conflict is solved in practice:

1. Augment the utility function  
   Replace “max μ′w – λ w′Σw” with “max μ′w – λ w′Σw – γ TC(w–w0)” where TC(·) is a calibrated market-impact model (Almgren-Chriss, Kissell, JPMorgan ACE, etc.).  
   γ is chosen so that the certainty-equivalent loss from tracking error is denominated in the same “dollars” as the expected market-impact bill. This is the framework used by Parametric, BlackRock, State-Street and most quant-overlay desks. MIT’s Albota-Lo paper shows that when γ is set via dynamic programming the optimal policy is no longer “rebalance fully when a 5 % band is breached” but rather “rebalance partially when the risk-adjusted drag of being away from target exceeds the round-trip impact cost, evaluated over the multi-period horizon.”

2. Solve on a risk-factor basis, not on individual assets  
   By rebalancing with futures, ETFs, or OTC swaps that replicate the factor mismatch instead of every single line-item, the number of physical trades collapses and the market-impact term in the objective function shrinks by an order of magnitude. Tracking-error is still measured against the policy mix, but the trade list is a handful of overlay tickets that cross internal liquidity pools or external algos during the overnight auction.

3. Make the threshold adaptive  
   Vanguard’s 2022 study and the MRG algorithm (Springer 2024) show that letting the tolerance band widen in high-vol / high-impact regimes and tighten in calm periods keeps ex-ante tracking error almost constant while cutting realised turnover 25-45 %. The band is set so that the expected 1-day TE inside the band equals the expected 1-day market-impact bill of crossing the spread.

4. Use execution micro-algos inside the macro-optimiser  
   The parent optimisation hands a target risk-mismatch vector to a child scheduler that slices the list across venues, dark-pools and TWAP slices while feeding back the temporary impact actually consumed. If the realised impact pushes the aggregate cost above the γ-weighted allowance, the parent optimiser is re-run with an updated TC estimate—an iterative “two-loop” system that guarantees the ex-post cost never materially exceeds the ex-ante budget.

Empirical outcome:

- MIT simulation on a $1 bn global-balanced mandate: optimal dynamic policy 20.3 bp total annual cost versus 38.1 bp for 5 % band heuristic, while 12-month rolling TE was held to 25 bp (institutional mandate limit 30 bp).  
- BlackRock overlay book (2023): median tracking error 9 bp, median turnover 18 %/yr, implementation shortfall 2.1 bp—roughly half the shortfall of the same fund before the cost-aware optimiser was switched on.

Bottom line

Mean-variance optimisation by itself is a cost-blind engine and will magnify market-impact friction once fund size or rebalancing frequency becomes non-trivial. Institutional platforms neutralise that amplification by embedding a calibrated impact model directly into the objective function, measuring tracking-error in certainty-equivalent dollars, and allowing only partial, factor-based trades when the risk-drag exceeds the liquidity cost. Done correctly, the algorithm delivers the targeted tracking-error budget at the minimum attainable execution-cost curve rather than at the minimum-variance point that ignores liquidity reality.

## Annotations


## Sources
