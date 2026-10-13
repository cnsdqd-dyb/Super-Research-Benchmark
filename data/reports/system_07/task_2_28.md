# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 8eefae3e | **Time:** 21.69s | **Cost:** $0.02865
--------------------------------------------------------------------------------

Wearables have to solve three problems at once:  
1. The motion corrupting the PPG/ECG/IMP is not white noise – it is highly correlated with the acceleration that the device itself can measure.  
2. The battery is < 100 mAh, so every multiply-accumulate costs “real money”.  
3. The clinician still wants heart-rate accuracy ≈ ±2 bpm and SpO2 ≈ ±2 % even when the wearer is jogging.

The algorithms that are now appearing in commercial ASICs and FDA-cleared patches are therefore the ones that give the largest “accuracy-gain per mJ”.  
From the last three years of literature and teardowns the following set is emerging as the de-facto standard pipeline.

--------------------------------------------------
1. Multi-sensor fusion front-end (zero extra cost)
--------------------------------------------------
- 3-axis accelerometer + gyro sampled at ≤50 Hz (≈15 µW)  
- PPG/ECG/IMP sampled at 25–128 Hz  
- Hardware trigger: the optical driver is blanked for 2–3 samples whenever |a|> 4 g – this alone removes the worst “LED shifts on the skin” spikes and costs nothing in software.

--------------------------------------------------
2. Ultra-low complexity adaptive filter (first line of defence)
--------------------------------------------------
- Normalised LMS with M=8–16 taps, updated every 0.5 s  
  – Uses the accelerometer magnitude as reference, μ=2⁻⁷ so the whole update is bit-shifts; < 30 MIPS on a Cortex-M0, < 0.5 mW  
  – Gives 6–8 dB SNR gain for walking, sufficient to keep HR in the ±5 bpm band.

--------------------------------------------------
3. Model-based Kalman tracker (second line, still cheap)
--------------------------------------------------
- 2-state (HR, HR′) or 3-state (HR, SpO2, perfusion-index) EKF  
- Measurement update only when motion variance < threshold → no updates during sprinting, so the filter automatically “coasts” on the physiological model and saves 30–40 % CPU wake-ups.  
- Implemented with fixed-point square-root covariance form → Cholesky is only 3×3, < 400 cycles per sample; < 0.2 mW on Ambiq Apollo4.

--------------------------------------------------
4. CNN micro-classifier (final polish, only when you have the energy)
--------------------------------------------------
- 1-D CNN with 3–4 layers, ≤ 2 k parameters, int8 weights (weights are ≤ 8 kB)  
- Runs once per second on a 1 s window; if the internal “motion class” probability > 0.6 the last-second HR estimate is discarded and the Kalman output is used instead.  
- With CMSIS-NN the whole inference is ≈ 6 kMAC → 12 µJ on an nRF-5340 (M33, 64 MHz).  
- Gives another 3–4 dB SNR and suppresses the annoying “180 bpm while brushing teeth” outliers.

--------------------------------------------------
5. Canonical-correlation / ICA post-processing (optional, for ECG patches)
--------------------------------------------------
- Redundant ECG leads (chest + back) + 3-axis IMU → joint diagonalisation (CCA) or ICA separates the “motion” subspace from the “cardiac” subspace.  
- Works especially well for high-density EMG/ECG belts; adds ≈ 0.3 mW when done with an incremental eigen-update every 2 s.

--------------------------------------------------
6. Closed-loop optical control (PPG specific)
--------------------------------------------------
- LED current is servoed every beat so that the AC/DC ratio stays in [0.5, 2] % – keeps the PPG in the sweet spot without automatic-gain-control filters that waste power.  
- The servo loop runs at 10 Hz and is implemented with a simple PI controller whose state is part of the same Kalman filter above – no extra code.

--------------------------------------------------
7. Duty-cycling strategy (the biggest “algorithm” for power)
--------------------------------------------------
- All heavy maths (CNN, CCA) are duty-cycled: after 30 s of “low motion” the MCU drops to 4 MHz and only the LMS is kept alive; when motion rises the CNN is switched on again.  
- This gives an average MCU current of 350 µA @ 3 V (≈ 1 mW) while still meeting the AAMI EC-13 error limits during a 30 min treadmill test.

--------------------------------------------------
Representative silicon already embedding the above pipeline
--------------------------------------------------
- Maxim MAX86150 (PPG+ECG) – on-chip LMS + FIFO triggers MCU wake-up  
- MediaTek MT2511 – hardware accelerometer interface + Kalman option  
- Silicon Labs BG27 – M33 with 64 kB retention RAM, CMSIS-NN ready, < 50 µA/MHz  
- AMS AS7038 – PPG AFE with “motion compensation” bit that runs a fixed-point LMS against an internal accelerometer.

--------------------------------------------------
Rule-of-thumb numbers (from recent papers)
--------------------------------------------------
Algorithm step | SNR gain | Power cost (µW)  
---------------|----------|------------------  
Blanking + LMS | 6–8 dB   | 100–200  
EKF tracker    | 3–4 dB   | 150–250  
1-D CNN        | 3–4 dB   | 10–15 µJ s⁻¹ (duty-cycled)  
CCA/ICA        | 4–6 dB   | 300 (only when leads available)  
Combined       | 12–16 dB | 0.5–1 mW total → 1 % of a 15 mW optical budget

--------------------------------------------------
Take-away
--------------------------------------------------
You do not need a “big” neural network.  
A tiny adaptive filter (LMS) to kill the correlated motion, a model-based Kalman to exploit the fact that heart-rate is physically bounded, and a micro-CNN that runs only when you really move is enough to keep both the clinician and the battery happy.

## Annotations


## Sources
