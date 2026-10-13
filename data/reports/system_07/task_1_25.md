# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 50ff284d | **Time:** 18.90s | **Cost:** $0.02712
--------------------------------------------------------------------------------

Market-microstructure models that try to reconcile *fast* price discovery with *robust* liquidity do not deliver a clean trade-off; under stress the same stochastic order-book dynamics that tighten spreads in calm periods amplify liquidity illusions and can destabilise prices.  
The argument can be laid out in four steps.

1.  What the models promise  
   – Kyle (1985)–type, Glosten-Milgrom, or more recent mean-field / stochastic-game setups (Lachapelle-Lasry-Lehalle-Lions 2013, Budish-Cramton-Shim 2015) show that when *n* fast market-makers compete, the half-spread collapses to the instantaneous cost of adverse-selection plus inventory risk.  
   – Because quotes are refreshed every millisecond, the *responsiveness* parameter λ in Δp = λQ falls and the book looks *deep* for any given Q.  
   – In simulations with only risk-neutral agents the stationary distribution of the inside queue has thin tails, so “liquidity” and “price discovery” appear to be delivered simultaneously.

2.  How the promise is kept only in calm data  
   – Empirical calibration of the same models (ECB working-paper 2020, Kirilenko et al. 2017, Nasdaq M-ELO study 2022) shows that the key structural parameters—arrival rate of informed market orders, cancellation rate of limit orders, and the ratio of *latent* depth to *displayed* depth—are *state-dependent*.  
   – When order-flow toxicity η (the probability that the next market order is informed) rises above a threshold η*(θ), the optimal quote of a high-frequency market-maker becomes *non-monotonic* in η: she widens the spread *and* cancels part of the displayed size.  
   – The stationary distribution of the book then switches from thin-tailed to power-law: the probability that the best-queue length falls below ε becomes P(ε) ∝ ε^{–α} with α < 1, i.e. the mean depth diverges.  
   – Because the switch is triggered by *common-knowledge* of toxicity, the stochastic process for the *visible* book becomes *multiplicative* rather than additive: small shocks to η produce *finite-time* vanishing of depth (“liquidity run”). The models therefore contain a *regime-shift* that is absent from the calm-period calibration.

3.  Why the run is mis-read as “still liquid”  
   – Fragmentation and dark pools split the *total* depth into many visible and hidden queues. During the run the *volume* that continues to print on the tape is supplied by slow traders or by HFTs trading *among themselves* (Menkveld-Yueshen 2019).  
   – Classic microstructure metrics—volume, time-weighted spread, VPIN—do not filter out this *endogenous* volume, so the market *looks* liquid right up to the instant that the mid-price gaps.  
   – The illusion is therefore a *measurement* consequence of the same stochastic order-book dynamics: the observable sufficient statistics (queue length, trade size, cancellation rate) have *non-stationary* innovations whose variance explodes precisely when depth collapses.

4.  Net assessment  
   – In *normal* time the models *do* balance discovery and stability: faster quotes mean smaller λ and quicker convergence to efficient price.  
   – In *stress* time the balance breaks down because the *feedback* between η, cancellation speed and visible depth is *positive*. The order-book evolution amplifies rather than absorbs shocks, and the liquidity that the models predicted becomes an *illusion*—a transient statistical artefact that disappears exactly when it is needed.  
   – Hence the answer to the question is *contextual*: the models contain both outcomes, but the stochastic mechanics of the book ensure that the *illusion* dominates in high-frequency regimes once toxicity crosses the endogenous threshold.

## Annotations


## Sources
