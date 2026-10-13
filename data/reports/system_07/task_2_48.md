# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 5666e20f | **Time:** 21.02s | **Cost:** $0.01481
--------------------------------------------------------------------------------

Yes—modern alpha-extraction pipelines are explicitly designed to trade off “edge” against turnover cost, but the very techniques that let us hunt for micro-edge also expose us to the curse of dimensionality, and that curse does not merely add noise; it changes the *shape* of the noise, making it look like signal.

Below is the short answer, followed by the quant-level details most PMs care about.

--------------------------------------------------
1. 30-second summary
--------------------------------------------------
- Signal/TC optimisation is done every day in production: you maximise  
  E[α] – λ · √turnover – TC(turnover)  
  instead of just E[α].  
- The dimensionality you need to capture the small, short-lived alphas is exactly the dimensionality that lets spurious correlations survive all the usual statistical filters.  
- Therefore you *can* balance strength and cost, but only if you embed the cost term *inside* the feature-selection objective; otherwise the curse silently inflates the t-stats that you rely on to size positions.

--------------------------------------------------
2. How the trade-off is implemented
--------------------------------------------------
a. Cost-aware objective in the *same* optimisation that finds the signal  
   – e.g. “turnover-penalised LASSO” (Tibshirani 1996 + Novy-Marx 2016):  
     min_w ½‖r – Xw‖² + γ‖w‖₁ + κ‖w – w₋₁‖₁  
     The last term is the L1 turnover penalty; κ is chosen so that the *net* IR is maximised out-of-sample.  
   – Result: coefficients are shrunk to zero *unless* they survive both risk-adjusted return *and* the projected commission–market-impact schedule.

b. Dynamic holding period optimisation  
   – Use an Ornstein–Uhlenbeck signal-decay model:  
     dSₜ = –κSₜdt + σdWₜ  
     Solve for the optimal holding time τ* that maximises  
     (½κS₀² – c·κτ – ½γσ²τ)  
     where c is one-way cost in bps.  
   – Typical outcome: a signal whose half-life is 0.7 days is held for 1.4 days only if round-trip cost < 8 bps; otherwise the position is skipped completely.

c. Portfolio-level turnover budgeting  
   – Solve a second-stage quadratic programme:  
     max_w  α’w – ½λw’Σw – ψ‖w – w₀‖₁  
     with the constraint ‖w – w₀‖₁ ≤ Θ (turnover budget).  
   – Θ is calibrated so that the *ex-ante* market-impact model (Almgren-Chriss) keeps expected slippage below a target % of gross alpha.

--------------------------------------------------
3. Where dimensionality bites
--------------------------------------------------
- Data sparsity: to keep the same false-discovery rate when you move from 50 to 5000 features you need ~100× more observations *if* the features are orthogonal.  
  In practice they are highly collinear, so the *effective* dimensionality is lower, but the *noise ceiling* rises because the eigenvalue spectrum of the covariance matrix becomes almost flat → smallest eigenvalues are indistinguishable from sampling error.  
- Turnover *itself* becomes a high-dimensional object: every micro-feature can push the optimal portfolio in a different direction; the LP/QP in (2c) ends up with a dense solution unless you regularise *explicitly* for turnover.  
- Interaction terms (e.g. stock × sector × time-of-month) explode cardinality; without a hierarchical prior you are almost guaranteed to fit bid-ask bounce rather than risk premium.

--------------------------------------------------
4. Practical antidotes that actually work
--------------------------------------------------
1. Dual-penalty elastic-net: λ₁‖w‖₁ + λ₂‖w‖₂ + κ‖Δw‖₁  
   Cross-validate λ₁, λ₂, κ *simultaneously* on a *net*-IR metric, not on R².  
2. Bayesian shrinkage with a turnover-cost prior:  
   w ~ N(0, Σ_prior) with Σ_prior estimated from past realised TC.  
3. Tree-based feature screening *before* linear model:  
   – Use a cost-aware XGBoost objective that includes  
     (prediction gain – η · feature turnover)  
     in the split criterion.  
4. Drop eigen-portfolios whose eigenvalue < 1 + √(p/n)  
   (Marchenko–Pastur upper edge) and *also* whose *turnover* > budget.  
5. Live *transaction-cost audit*: every new micro-alpha must show  
   t-stat(net) > 3.5 *and* break-even cost ≥ 95th percentile of realised cost distribution; otherwise the feature is zero-weighted automatically.

--------------------------------------------------
5. Bottom line
--------------------------------------------------
You *can* have your cake and eat it—*provided* the objective function you maximise already contains the commission, the market-impact model and the turnover norm.  
If you first select “strong” signals and only later ask “can we afford to trade them?”, the dimensionality curse will have already manufactured an army of 3-sigma noise soldiers that look exactly like alpha.

## Annotations


## Sources
