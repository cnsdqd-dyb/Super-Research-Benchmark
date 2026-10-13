# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 2d519374 | **Time:** 17.71s | **Cost:** $0.01489
--------------------------------------------------------------------------------

The “temporal function” that decides when and how a seller’s reputation score is corrected is not a single industry-standard formula; it is a design choice that has converged on four practical patterns.  Each pattern explicitly answers the two questions that define the function:

1. When is the score re-computed?  
2. How much weight does every past rating lose as it ages?

Below are the four patterns that appear in the recent literature and in live platforms.

--------------------------------------------------------------------
1. Exponential-age decay with every new rating
--------------------------------------------------------------------
Used in: agent-based trust models (Zhang & Zhang 2013, JATIT 2021)  
Re-calculation trigger: immediately after a new rating arrives.  
Decay rule:  
RF(rk)=exp(−|tc−tk|/λ) , λ∈(0,1]

- The “clock” is event-driven: each fresh rating re-opens the calculation.  
- λ is a platform tuning knob; smaller λ makes the system forget faster, protecting buyers from sellers that oscillate in quality.  
- Because the update is O(1) in the number of past ratings, it can be executed in real time even on large marketplaces.

--------------------------------------------------------------------
2. Sliding calendar window
--------------------------------------------------------------------
Used in: MIT cluster-filtering extension (Dellarocas 2000), Shapiro-efficient design  
Re-calculation trigger: at fixed calendar length (e.g., every day or every week).  
Decay rule: binary weight inside the window, zero outside.

R(s,t)=average of ratings in [t−W,t]

- W is chosen by policy (30 d, 90 d, 1 year).  
- No gradient of forgetting—ratings are either fully counted or fully dropped—so the correction is easy to explain to users.  
- Works well when seller quality is believed to be piece-wise constant over short horizons.

--------------------------------------------------------------------
3. Iterative EWMA with period boundary
--------------------------------------------------------------------
Used in: Gao 2017 (RR/CR ranking), JATIT 2021 windowed EWMA  
Re-calculation trigger: at the end of each pre-set time slice (hour, day, week).  
Decay rule: exponential smoothing between the last stored value and the slice average.

Rn=χRn−1+(1−χ)Rcur , χ∈[0,1]

- The reputation vector is materialised only once per slice, so computation and storage load is bounded.  
- χ plays the same economic role as λ in pattern 1, but the update is synchronous rather than event-driven.

--------------------------------------------------------------------
4. Feedback-count window (negative-triggered refresh)
--------------------------------------------------------------------
Used in: Cabral & Hortaçsu (eBay study)  
Re-calculation trigger: when the cumulative number of new feedbacks since the last negative reaches a threshold, or when a fresh negative arrives.  
Decay rule: none explicit; instead, the platform re-averages all ratings that arrived since the last “reset point”.

- Empirically, eBay sellers see a correction every ≈ 160 feedbacks on average, but the interval shortens after the first negative, indicating the system is more sensitive once evidence of a quality drop exists.  
- The temporal function is therefore state-dependent: the clock speeds up when the seller’s recent performance deteriorates.

--------------------------------------------------------------------
Which one to choose?
--------------------------------------------------------------------
- If the marketplace wants “real-time” reputation and has light latency constraints → pattern 1.  
- If explainability and regulatory audit are primary → pattern 2 (calendar window).  
- If the platform has billions of ratings and needs batch compaction → pattern 3.  
- If the risk team wants the score to react faster once red flags appear → pattern 4 (or a hybrid of 1 and 4).

In short, the temporal function is determined by selecting one of these four update clocks and then tuning its single decay parameter (λ, W, χ or the feedback threshold).  The choice fixes how quickly the system “forgives” old behaviour and therefore how strongly sellers are incentivised to keep quality high today rather than yesterday.

## Annotations


## Sources
