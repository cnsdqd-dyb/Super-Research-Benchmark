# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 6f5aaafb | **Time:** 13.69s | **Cost:** $0.02307
--------------------------------------------------------------------------------

At mm-wave frequencies the classical "back-off" compromise (run the PA several dB below Psat so that the waveform is not clipped) is no longer acceptable: every dB of back-off is multiplied by the low antenna gain of a 5G/6G element and by the high atmospheric loss, so the link budget collapses.  
The only way out is to let the PA operate close to, or even into, compression while still delivering an EVM-compliant signal.  
The architectures that do this with the smallest penalty in DC power are the ones that:

1. Keep the instantaneous load impedance seen by the transistor close to the optimum power/efficiency contour for every envelope level, and  
2. Correct the resulting AM-AM/AM-PM distortion digitally.

Hence the best practical answer today is:

- Use a load-modulating analogue PA stage (Doherty, Out-phasing, or LMBA) to obtain high back-off efficiency,  
- Drive it with a mixed-signal control loop that aligns the auxiliary paths in time and amplitude (MS-DPA, RF-DAC, or digitally-assisted Doherty), and  
- Close the linearity budget with a low-rate, robust digital pre-distortion (DPD) that runs on the base-band chip, not in the element.

This "load-modulated PA + light DPD" combination has demonstrated:
- >30 % PAE at 6 dB back-off at 28 GHz in CMOS/SOI,  
- −25 dB EVM for 64-QAM OFDM without heavy DSP,  
- Scalable to phased arrays because the calibration overhead is only a few coefficients per element.

Other single-ended tricks (adaptive bias, Class-AB with huge back-off, or heavy full-band DPD) either burn too much power or cannot be replicated across hundreds of array elements.

## Annotations


## Sources
