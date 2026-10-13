# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 408efdcf | **Time:** 20.83s | **Cost:** $0.01870
--------------------------------------------------------------------------------

Heterogeneous-agent models (HAMs) in behavioural finance are built to do two things at once:  
(i) let every artificial trader be psychologically recognisable (over-confidence, memory bias, diagnostic expectations, etc.) and  
(ii) watch how thousands of such biased traders aggregate into prices, volume, volatility clustering, fat tails, etc.  

Whether they actually “balance” the two goals, or are forced to sacrifice one because the computer runs out of steam, depends on where the modeller sits on the tractability-realism-resources triangle.

1. What the models can already deliver  
   – Single-bias experiments: one or two well-documented biases (conservatism, representativeness, over-confidence, cognitive discounting) can be embedded at agent level and the resulting moments (skewness, excess volatility, post-earnings-announcement drift, forward-guidance puzzle) reproduced with 10³–10⁴ agents and a few thousand trading rounds on a desktop.  
   – Calibration to micro data: using survey expectations, trading-account data or lab experiments, the distribution of bias parameters can be estimated and fed into the simulation; the simulated price and order-book statistics then match the empirical ones (Chiarella–Iori–Perelló type LOM models, HANK models with behavioural households).  
   – Policy counter-factuals: once the model is calibrated, transparency rules, transaction taxes, forward-guidance announcements, etc. can be switched on/off and the differential impact traced back to the heterogeneity in bias and balance-sheet exposure.

2. Where resource constraints bite first  
   – Dimensionality explosion: every extra bias parameter, memory lag, learning rate or portfolio rule adds a state variable. With 10⁴ agents and 10 biases each, the state space is 10⁵–10⁶ numbers per period; moments-based solution methods collapse and Monte-Carlo variance is still large after tens of thousands of runs.  
   – Calibration cost: method-of-moments or simulated-ML estimation requires the model to be solved thousands of times. A single 10 000-agent, 5 000-period market with full order book already takes hours on a GPU; a full SMM estimation can need weeks unless closed-form aggregation shortcuts are found.  
   – LLM-based agents: recent attempts to give traders a large-language-model “brain” produce very realistic chat transcripts, but each trading round consumes thousands of tokens; 300 independent runs already cost ≈ $20 with GPT-3.5 and scale linearly in the number of agents and rounds. Real-time or large-N experiments are quickly prohibitive, and the model still has to be run many times for sensitivity analysis.  
   – Memory-span heterogeneity: Levy-Levy-Solomon models show that long memory is crucial for realistic volatility persistence, but every extra lag increases the Markov-state dimension; analytical HAMs therefore truncate memory to 1–2 lags, sacrificing the very feature that generates long-range dependence.

3. Current coping strategies  
   – Representative + hand-to-mouth split: the behavioural-HANK literature collapses the full wealth distribution into two “as-if” agents whose consumption functions are solved once offline; the micro bias (cognitive discounting, MPC heterogeneity) is retained, but the cross-sectional detail is lost.  
   – Clustering or meta-agents: variational auto-encoders or k-means are used to lump the 10⁴ traders into 10–20 behavioural types; within each type the agents are identical, cutting the state space by two orders of magnitude while still capturing between-type heterogeneity.  
   – Emulation / surrogate models: a deep neural net is trained on a small number of high-fidelity simulations and then used as a fast proxy during calibration or MCMC estimation (similar to “emulation” in climate modelling).  
   – Hybrid GPU–CPU codes and cloud bursting: order-book matching is done on GPUs, while expectation updating (the heavy bias part) is done in parallel on CPUs; elastic cloud instances are spun up only for the calibration window and released afterwards, keeping dollar cost finite.

4. Bottom-line assessment  
   – For qualitative insight (“does over-confidence generate fat tails?”) or policy scenarios that vary one rule at a time, present hardware and code are already sufficient; the balance between micro bias and aggregate outcome is effectively achieved.  
   – For full quantitative calibration to micro data, joint identification of many behavioural parameters, or for models that let every single agent be an LLM, the computational budget becomes the binding constraint. In practice the modeller either (i) keeps the rich heterogeneity but collapses the number of agents/types, or (ii) keeps the large population but simplifies the psychological kernel.  
   – Rapidly falling GPU-hour prices, compact open-source LLMs, and emulation techniques are pushing the frontier outward, but for the next few years the “right” degree of heterogeneity will still be dictated less by behavioural finance theory than by the size of the research grant or the cloud-credit budget.

## Annotations


## Sources
