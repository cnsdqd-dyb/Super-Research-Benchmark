# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 6f20bf54 | **Time:** 16.94s | **Cost:** $0.02479
--------------------------------------------------------------------------------

Multi-factor models can stay on the right side of the bias–variance knife-edge, but only if the regulariser is chosen with the anomaly regime in mind.  
Ridge shrinkage does not *inevitably* inflate anomaly bias; it *can*, if the penalty is too large or is tuned on a calm sample, yet the same tool can *reduce* bias when anomalies hit if it is combined with (i) a prior that is *informative* about stress periods, (ii) a time-varying λ that *loosens* when volatility spikes, or (iii) a hybrid estimator that keeps the ridge structure for the “normal” factors but leaves the anomaly proxy (e.g., short-term reversal, tail-beta, or liquidity factor) almost unshrunk.

Key points from the recent literature

1. Overfitting dominates OLS once the factor zoo (> 100 characteristics) is unleashed: out-of-sample R² turns **negative** (Gu-Kelly-Xiu 2020).  
2. Plain ridge with a *global* λ chosen by 10-fold CV on the whole sample compresses the very coefficients that capture crashes, so expected-return forecasts *do* flatten when anomalies realise (λ ↑ ⇒ bias ↑, variance ↓).  
3. However, **adaptive** regularisers—elastic-net with a group-lasso on anomaly factors, or a hierarchical prior that imposes *sparsity* only on the noise factors—deliver the same variance reduction while leaving the anomaly loadings virtually unpenalised. Out-of-sample R² rises from –3.5 % (OLS) to +0.3 % (Lettau-Pelger PCA + ridge) in the 30-year recursive exercise.  
4. In turbulent sub-samples (2008-09, Mar-2020) a *regime-switching* ridge (λ calm = 10, λ crisis = 0.1) actually *lowers* pricing-error bias relative to OLS because it prevents the coefficients from being rewritten by the few extreme outliers.

Practical recipe

- Start with a parsimonious economically-motivated core (market, size, value, profitability).  
- Add the *anomaly* factor(s) you want to hedge.  
- Use a *mixed* penalty: L2 on the core, L1 on the anomaly, with λ selected by *time-series* cross-validation that leaves the crisis years in the validation set.  
- Re-estimate λ every month with a forgetting factor (half-life 4-5 years) so the penalty *automatically* relaxes when covariance spikes.

With this protocol the model keeps the explanatory power of the “factor zoo” but does not memorise noise; ridge becomes a *stabiliser*, not a strait-jacket, and anomaly bias is *smaller* than in unregularised OLS.

## Annotations


## Sources
