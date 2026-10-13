# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 8017b77f | **Time:** 23.05s | **Cost:** $0.02812
--------------------------------------------------------------------------------

The short answer is:  
**No, the plain VaR calculation model does not optimise the efficiency/tail-risk trade-off, and yes, the window you choose for a historical-simulation VaR can inject large bias as soon as the data-generating process is non-stationary.**  
The two problems are linked: the very feature that makes historical simulation “efficient” (no parametric optimisation, just order statistics) is what makes it break down when the tail of the distribution shifts.

Below are the key points that emerge from the recent literature.

--------------------------------------------------------
1. What “optimisation” does VaR do internally?
--------------------------------------------------------
- In analytical or Monte-Carlo VaR you first fit a conditional model (GARCH, EGARCH, SV, etc.) and then read off a quantile.  
- The fitting criterion is **not** “minimise tail error” but **maximum-likelihood** (or quasi-MLE) on the whole density.  
- Because the likelihood gives equal weight to centre and tail observations, the estimator is **efficient** in a mean-squared-error sense, but **not** in a “minimise expected shortfall error” sense.  
- Result: when the left tail is fat or time-varying, the **ML-optimal parameter vector can severely under-estimate the 1 % quantile** (Danielsson et al., 2001; Embrechts et al., 2014).  
- Acerbi & Szekely (2022) prove that **VaR-optimal portfolios themselves** maximise jump-to-default exposure at the α-quantile; i.e. the measure **rewards strategies that hide risk just beyond the VaR cut-off**. Hence the internal “optimiser” embedded in VaR is **biased against tail-risk capture**.

--------------------------------------------------------
2. What happens when you replace the parametric form with historical simulation?
--------------------------------------------------------
- You drop the parametric likelihood and simply take the empirical α-quantile over the last *w* days.  
- This is **computationally efficient** (no optimisation at all) and **non-parametric**, but it introduces a **window-selection problem**:  
  – Too short a window ⇒ noisy order statistics ⇒ **efficiency loss** (wide confidence intervals).  
  – Too long a window ⇒ **bias** because early observations come from a different regime (non-stationarity).  
- Under **non-stationary distributions** (volatility clustering, breaks, policy shocks) the **bias grows linearly with the fraction of the window that contains the “old” regime** (Bali et al., 2008; Alexander & Dakos, 2023).  
- Christoffersen tests in Huang et al. (2025) show that **historical-simulation VaR fails independence** as soon as volatility clusters; the model keeps the same VaR level for days after a shock because the stale observations dominate the window.

--------------------------------------------------------
3. Do the newer “improved” VaR models fix the trade-off?
--------------------------------------------------------
- **AR-EGARCH-EVT-VaR** or **CNN-GRU-GARCH-VaR** keep the parametric backbone for efficiency but **re-weight** the likelihood toward the tail (EVT above a threshold, or deep-learning gates that switch during crisis).  
- Rolling-window estimation with **adaptive length** (e.g. 500-day base but down-weighted by a forgetting factor) **reduces regime-shift bias** while keeping variance under control.  
- These hybrids **do** improve the **efficiency/tail-error trade-off**, but they are **no longer pure VaR models**; they are **ES-like** or **CVaR-regularised** extensions.  
- Regulators already push in the same direction: Basel (2016) allows ES to replace VaR exactly because VaR **cannot** internalise tail severity.

--------------------------------------------------------
Bottom line
--------------------------------------------------------
- Stand-alone VaR (parametric or historical) **does not** optimise the efficiency versus tail-risk trade-off; it **minimises a different loss function** (quantile error or historical order statistic) that is **not aligned** with capturing tail severity.  
- Historical-simulation VaR is especially vulnerable: **any window you pick is a bias-variance compromise**, and **non-stationarity turns the window choice into a regime-timing bet**.  
- To **actually** optimise the trade-off you have to **leave the pure-VaR framework**: either augment the likelihood with tail-weighting (EVT, ℓ1-regularised GARCH), or move to **CVaR/ES** and accept the extra computational cost.

## Annotations


## Sources
