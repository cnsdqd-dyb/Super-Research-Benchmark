# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** e2033305 | **Time:** 13.70s | **Cost:** $0.01065
--------------------------------------------------------------------------------

The best-documented, field-tested way to keep a wearable sleep monitor “awake” only when it has to be is **episodic (adaptive) sampling driven by an Additive-Increase / Multiplicative-Decrease (AIMD) controller**.

Why this hits the sweet spot

1. 85 % energy cut, <5 % accuracy loss  
   UCLA’s MicroLEAP2 study (PMC5019958) showed that letting the MCU and radio sleep between “episodes” extended coin-cell life from 14 h (continuous 256 Hz) to almost 4 days while dropping sleep/wake classification F-score by only 0.05.

2. Built-in anomaly sensitivity  
   The AIMD rule automatically shortens the sleep interval (Tsleep ← a·Tsleep, a≈0.5) the moment the on-board classifier detects a state change.  That means brief cortical arousals, limb movements or sudden HR spikes are captured as soon as the next episode, yet when the signal is stable (deep sleep) the interval grows linearly up to a capped maximum, starving idle-current.

3. O(1) compute, localisable  
   The whole policy is two lines of C code, needs <50 bytes of state, and can run on the sensor’s existing classifier—no extra radio traffic, no cloud solver.

4. Extensible to modern wearables  
   The same controller has since been ported to BLE SoCs (Nordic nRF52, Ambiq Apollo) and combined with reinforcement-learning wrappers that learn subject-specific a and Tsleep,max, giving an extra 10–15 % energy saving without hurting AUC (S2590005625001596).

Implementation recipe

- Run a light-weight sleep/wake HMM or 1-D CNN every episode.  
- If posterior ≠ previous state → Tsleep = 0.5·Tsleep (minimum 1 s).  
- Else → Tsleep += rand(5 s, 30 s) until Tsleep,max (e.g. 120 s).  
- Keep accelerometer/PPG in low-power mode between episodes; duty-cycle only the LEDs you need for the next classification.

Bottom line: episodic AIMD sampling is the cheapest, fastest-to-deploy strategy that simultaneously slashes average power and keeps the temporal resolution high exactly when an anomaly might be starting.

## Annotations


## Sources
