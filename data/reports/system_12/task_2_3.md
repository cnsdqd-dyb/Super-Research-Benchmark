# Deep Research Report: grok-4-1-fast-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** afe16ea7 | **Time:** 44.22s | **Cost:** $0.00652
--------------------------------------------------------------------------------

**The Doherty power amplifier (DPA) architecture is widely regarded as the best approach for optimizing the trade-off between power amplifier (PA) efficiency and linearity in millimeter-wave (mmWave) RF front-end circuits.**[[1]](https://ieeexplore.ieee.org/document/10403646)[[2]](https://theses.hal.science/tel-03227382v1/file/TH2020PESC2026.pdf)

### Why Doherty Excels in mmWave
mmWave frequencies (e.g., 24–100 GHz for 5G NR) demand PAs with high peak and back-off efficiency (e.g., >30–50% PAE at 6–10 dB power back-off, PBO) due to high peak-to-average power ratio (PAPR, 8–12 dB) signals, while ensuring linearity (low error vector magnitude, EVM <3–5%; adjacent channel leakage ratio, ACLR >35–40 dBc) to minimize spectral regrowth and support massive MIMO arrays.[[3]](https://ieeexplore.ieee.org/document/9318742)[[2]](https://theses.hal.science/tel-03227382v1/file/TH2020PESC2026.pdf)

Traditional classes (A/B: linear but <20% avg PAE at PBO; switched-mode E/F: high peak efficiency ~70–90% but poor linearity) fail this trade-off. Doherty addresses it via **active load modulation**:
- **Carrier (main) PA** operates in Class AB/B for linearity at low power.
- **Peaking PA(s)** activate at ~6 dB PBO, modulating the load impedance (from high-Z at low power to low-Z at peak) to restore efficiency, yielding dual peaks (~70–80% at 0/6 dB PBO).[[4]](https://www.5gtechnologyworld.com/how-doherty-amplifiers-improve-pa-efficiency)[[2]](https://theses.hal.science/tel-03227382v1/file/TH2020PESC2026.pdf)
- **Theoretical 1:1 efficiency flattening** over 6 dB range, reducing avg power consumption by 2–3x vs. Class AB.[[2]](https://theses.hal.science/tel-03227382v1/file/TH2020PESC2026.pdf)

In mmWave ICs (CMOS/SiGe/GaN MMICs), implementations use transformers or stubs for compact impedance inversion/combining, achieving:
- 25–40% PAE at 6 dB PBO (vs. 10–20% for baseline).[[1]](https://ieeexplore.ieee.org/document/10403646)[[2]](https://theses.hal.science/tel-03227382v1/file/TH2020PESC2026.pdf)
- Improved linearity via bias/phase tuning (e.g., dual-bias for reduced memory effects) or asymmetric sizing.[[5]](https://www.microwavejournal.com/articles/36731-improving-linearity-of-a-doherty-power-amplifier-with-a-dual-bias-structure)

### Comparison to Alternatives
| Approach | Efficiency (PBO) | Linearity | mmWave Suitability | Drawbacks |
|----------|------------------|-----------|---------------------|-----------|
| **Doherty** | High (dual peaks) | Good (inherent; DPD optional) | Excellent (compact ICs) | Bandwidth-limited (~10–20%; mitigated by multi-way/multi-primary)[[6]](https://ui.adsabs.harvard.edu/abs/2021IJSSC..56.1668W) |
| **Outphasing/Chireix** | High back-off | Moderate (phase linearity issues) | Good | Reactive loads cause AM-PM distortion[[2]](https://theses.hal.science/tel-03227382v1/file/TH2020PESC2026.pdf) |
| **Class-F/J (harmonic-tuned)** | High peak | Poor at PBO | Moderate (parasitics limit harmonics) | Needs load-pull optimization[[2]](https://theses.hal.science/tel-03227382v1/file/TH2020PESC2026.pdf) |
| **Load-Modulated Balanced Amp (LMBA)** | Very high (>50% at 6–7 dB) | Excellent (tunable trajectories) | Promising but complex | Emerging; mmWave parasitics challenge[[2]](https://theses.hal.science/tel-03227382v1/file/TH2020PESC2026.pdf) |
| **Envelope Tracking/DPD** | Variable | Excellent | Challenging (BW/memory at mmWave) | Overhead, not architectural[[7]](https://research.chalmers.se/publication/522527/file/522527_Fulltext.pdf) |
| **Stacked/Neutralized** | Moderate | Good | Baseline for CMOS | Low back-off efficiency[[8]](https://www.mdpi.com/2674-0729/4/4/52) |

Doherty variants (e.g., GaN MMIC, continuous-mode hybrids) dominate ISSCC/JSSC papers for 28/39 GHz 5G, balancing integration, power (>20–30 dBm), and performance.[[9]](https://www.researching.cn/articles/OJ2c4967a1cc5e75f7)

### Design Considerations for mmWave Front-Ends
- **Tech**: GaN for high power; SiGe/CMOS for integration.[[1]](https://ieeexplore.ieee.org/document/10403646)
- **Enhancements**: Harmonic tuning (Class J), input splitters, DPD for residual distortion.
- **Trade-offs**: Prioritize PBO efficiency > peak for avg metrics; simulate load-pull for trajectories minimizing AM/PM distortion.[[2]](https://theses.hal.science/tel-03227382v1/file/TH2020PESC2026.pdf)

This makes Doherty the optimal choice for high-frequency signal processing in front-ends.[[10]](https://onlinelibrary.wiley.com/doi/10.1155/2018/6793814)

## Annotations (Inline Citations)
Citation [1] (Pos: 224-276): [Web] https://ieeexplore.ieee.org/document/10403646
Citation [2] (Pos: 276-348): [Web] https://theses.hal.science/tel-03227382v1/file/TH2020PESC2026.pdf
Citation [3] (Pos: 773-824): [Web] https://ieeexplore.ieee.org/document/9318742
Citation [2] (Pos: 824-896): [Web] https://theses.hal.science/tel-03227382v1/file/TH2020PESC2026.pdf
Citation [4] (Pos: 1357-1442): [Web] https://www.5gtechnologyworld.com/how-doherty-amplifiers-improve-pa-efficiency
Citation [2] (Pos: 1442-1514): [Web] https://theses.hal.science/tel-03227382v1/file/TH2020PESC2026.pdf
Citation [2] (Pos: 1628-1700): [Web] https://theses.hal.science/tel-03227382v1/file/TH2020PESC2026.pdf
Citation [1] (Pos: 1886-1938): [Web] https://ieeexplore.ieee.org/document/10403646
Citation [2] (Pos: 1938-2010): [Web] https://theses.hal.science/tel-03227382v1/file/TH2020PESC2026.pdf
Citation [5] (Pos: 2120-2250): [Web] https://www.microwavejournal.com/articles/36731-improving-linearity-of-a-doherty-power-amplifier-with-a-dual-bias-structure
Citation [6] (Pos: 2597-2657): [Web] https://ui.adsabs.harvard.edu/abs/2021IJSSC..56.1668W
Citation [2] (Pos: 2783-2855): [Web] https://theses.hal.science/tel-03227382v1/file/TH2020PESC2026.pdf
Citation [2] (Pos: 2987-3059): [Web] https://theses.hal.science/tel-03227382v1/file/TH2020PESC2026.pdf
Citation [2] (Pos: 3230-3302): [Web] https://theses.hal.science/tel-03227382v1/file/TH2020PESC2026.pdf
Citation [7] (Pos: 3421-3500): [Web] https://research.chalmers.se/publication/522527/file/522527_Fulltext.pdf
Citation [8] (Pos: 3592-3636): [Web] https://www.mdpi.com/2674-0729/4/4/52
Citation [9] (Pos: 3803-3864): [Web] https://www.researching.cn/articles/OJ2c4967a1cc5e75f7
Citation [1] (Pos: 3972-4024): [Web] https://ieeexplore.ieee.org/document/10403646
Citation [2] (Pos: 4250-4322): [Web] https://theses.hal.science/tel-03227382v1/file/TH2020PESC2026.pdf
Citation [10] (Pos: 4413-4477): [Web] https://onlinelibrary.wiley.com/doi/10.1155/2018/6793814


## Sources
[1] https://www.mdpi.com/2674-0729/4/4/52
[2] https://mtt.org/app/uploads/2024/06/12_GF_FR_HanZhou.pdf
[3] https://ieeexplore.ieee.org/document/10403646
[4] https://core.ac.uk/download/pdf/344940352.pdf
[5] https://www.researchgate.net/publication/326206712_A_Review_of_5G_Power_Amplifier_Design_at_cm-Wave_and_mm-Wave_Frequencies
[6] https://rex.libraries.wsu.edu/view/pdfCoverPage?download=true&filePid=13422897630001842&instCode=01ALLIANCE_WSU
[7] https://www.youtube.com/watch?v=yNiHhQO0_zk
[8] https://dataspace.princeton.edu/handle/88435/dsp01w9505340j
[9] https://ieeexplore.ieee.org/iel7/9171629/9316332/09318742.pdf
[10] https://escholarship.org/content/qt8q63z1ch/qt8q63z1ch_noSplash_f2660bbb085a25f75f2d6f65f7378364.pdf
[11] https://onlinelibrary.wiley.com/doi/10.1155/2018/6793814
[12] https://www.sciencedirect.com/science/article/abs/pii/S1434841120327886
[13] https://research.chalmers.se/publication/540870/file/540870_Fulltext.pdf
[14] https://webthesis.biblio.polito.it/37658/1/tesi.pdf
[15] https://zenodo.org/records/1276321/files/article.pdf
[16] https://www.researchgate.net/publication/398076764_Design_Techniques_for_Efficient_Mm_wave_Transceivers_A_Focus_on_Low-Noise_Amplifiers_and_Power_Amplifiers
[17] https://theses.hal.science/tel-03227382v1/file/TH2020PESC2026.pdf
[18] https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/el.2014.2178
[19] https://ui.adsabs.harvard.edu/abs/2021IJSSC..56.1668W
[20] https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-53.pdf
[21] https://aber.apacsci.com/index.php/CTE/article/viewFile/2305/3422
[22] https://www.semanticscholar.org/paper/A-Review-of-5G-Power-Amplifier-Design-at-cm-Wave-Lie-Mayeda/028c93246b38160a8b56447c759fb02a78ec6428
[23] https://www.mdpi.com/2674-0729/4/2/20
[24] https://onlinelibrary.wiley.com/doi/chapter-epub/10.1002/9781119792949.ch8
[25] https://www.youtube.com/watch?v=aN2TkGKLZrE
[26] https://www.keysight.com/us/en/assets/3123-1395/case-studies/Creating-Highly-Efficient-and-Reliable-mmWave-Power-Amplifiers.pdf
[27] https://drpress.org/ojs/index.php/ajst/article/view/31994
[28] https://www.researchgate.net/publication/224351882_Improving_Power_Amplifier_Efficiency_and_Linearity_Using_a_Dynamically_Controlled_Tunable_Matching_Network
[29] https://www.researchgate.net/publication/224189682_Power_Efficiency_and_Linearity_Enhancement_Using_Optimized_Asymmetrical_Doherty_Power_Amplifiers
[30] https://www.scilit.com/publications/da5d38f21deb46a91f7741accfcac8e4
[31] https://rfmwblog.com/2023/11/13/how-to-balance-linearity-and-efficiency-in-rf-power-amplifiers
[32] https://www.rfinsights.com/insights/design/transmitter/mm-wave-pa-design
[33] https://rex.libraries.wsu.edu/esploro/outputs/doctoral/HIGHLY-EFFICIENT-AND-LINEAR-RECONFIGURABLE-MM-WAVE/99900581818201842
[34] https://www.airo.co.in/display-publication/2511
[35] https://www.5gtechnologyworld.com/how-doherty-amplifiers-improve-pa-efficiency
[36] https://repository.up.ac.za/bitstreams/ca523b4f-4374-4c69-bdd4-4bb6320b207e/download
[37] https://research.chalmers.se/publication/522527/file/522527_Fulltext.pdf
[38] https://www.researching.cn/articles/OJ2c4967a1cc5e75f7
[39] https://ieeexplore.ieee.org/document/9318742
[40] https://www.microwavejournal.com/articles/36731-improving-linearity-of-a-doherty-power-amplifier-with-a-dual-bias-structure
[41] https://resourcecenter.mtt.ieee.org/education/webinars/mtt_edu_web_piacibello_111125
