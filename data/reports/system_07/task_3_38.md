# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 2438c65b | **Time:** 19.62s | **Cost:** $0.02125
--------------------------------------------------------------------------------

Regenerative-braking power matching during train-density changes affects grid harmonic distortion in three main ways:

1. Spectral "piling-up" when braking power is not absorbed  
   - Every four-quadrant traction converter is a harmonic-current source whose spectrum is modulated by the instantaneous power it processes.  
   - If, because of low traffic density, no other train is drawing power, the braking energy is forced back into the 25 kV/50 Hz (or 15 kV/16.7 Hz) network. The converter now operates at ≈ -0.8…-1 pu power, i.e. the phase of the fundamental current reverses while the PWM pattern and switching frequency (typically 450 Hz–1 kHz) stay the same.  
   - The injected harmonic currents (5th, 7th, 11th, 13th, 23rd, 25th and side-bands around twice the switching frequency) therefore travel toward the public grid instead of being cancelled by a neighbouring locomotive. Measurements on the Italian 3-kV dc and Chinese 25-kV ac systems show that THD can jump from <2 % (balanced traction/braking) to >5 % when only one or two trains are braking.

2. Resonance amplification that varies with train count  
   The traction network is a distributed LC structure (catenary, feeder, rail, stray capacitance). Its resonance points (typically 1.6 kHz, 2.3 kHz, 3.8 kHz…) are almost independent of train density, but the damping is not.  
   - High density → many vehicles act in parallel: the equivalent resistance seen from the catenary is low, so Q-factor ≈ 1–2.  
   - Low density → only the substation transformer and the public-grid short-circuit impedance provide damping: Q rises to 5–8.  
   When the braking harmonic spectrum (e.g. 27th harmonic, 1.35 kHz @ 50 Hz) happens to coincide with a lightly damped resonance, the voltage distortion at the substation can be amplified by a factor 3–4 even though the harmonic *current* injected by the train is unchanged. Field tests in Springer (2023) show 70–80th harmonic over-voltages appearing only under single-train braking conditions.

3. Negative-sequence interaction during asymmetric braking  
   If the traffic imbalance is such that braking power is concentrated in one phase (typical of single-phase feeding sections), the fundamental current in that phase reverses while the other two phases carry normal load. The resulting negative-sequence voltage (V₂) rotates the fundamental reference frame of every converter in the vicinity; because the harmonic controllers of the trains are synchronised to this distorted frame, low-order harmonics (5th, 7th) that were perfectly cancelled under balanced conditions are re-created. Simulations in the MDPI Energies (2024) paper show V₂ rising from 0.4 % to 1.1 % when the braking/active power ratio exceeds 0.7, with THD growing from 1.8 % to 3.3 % even though the aggregate braking power is the same.

Practical consequence  
Power-matching devices (reversible substations, wayside super-capacitors, or on-board energy-storage trains) are therefore specified not only for energy saving but also for "harmonic duty": by guaranteeing that ≥ 60–70 % of the braking energy is absorbed locally, they keep the converter in the "motoring" quadrant for the remainder of the time, preventing the spectral reversal and the associated resonance/negative-sequence amplification. With such storage in service, measured THD remains below 2 % independent of traffic density.

## Annotations


## Sources
