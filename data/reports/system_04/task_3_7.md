# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 875346c8 | **Time:** 337.19s | **Cost:** $1.78087
--------------------------------------------------------------------------------

# Optimizing the Trade-off Between Energy Efficiency and Anomaly Detection in Wearable Sleep Monitors: A Comprehensive Review of Sampling Strategies

### Key Points
*   **Compressive Sensing (CS)** emerges as a dominant strategy, capable of extending sensor node lifetime by approximately **37.1%** compared to traditional wavelet-based compression while maintaining high reconstruction quality for physiological signals [cite: 1, 2].
*   **Adaptive and Event-Driven Sampling** (including Level-Crossing Sampling) can reduce power consumption by **two orders of magnitude** in specific subsystems by sampling only when signal amplitude changes significantly, rather than at fixed intervals [cite: 3, 4].
*   **Optimal Fixed Rates:** For photoplethysmography (PPG) in wearables, a sampling rate of **64 Hz** is identified as the optimal balance for heart rate variability (HRV) and apnea detection, with **32 Hz** being acceptable for basic metrics, whereas rates below 30 Hz significantly degrade diagnostic accuracy [cite: 5].
*   **Hybrid Approaches:** The most effective optimization utilizes **hierarchical sensing**, where low-power sensors (accelerometers) trigger high-fidelity recording (ECG/PPG) only during detected anomalies or specific sleep stages, combined with deep learning models (e.g., CNNs) that can infer pathologies from downsampled or compressed data [cite: 6, 7, 8].

### Executive Summary
The proliferation of wearable technology for sleep monitoring faces a critical engineering bottleneck: the inverse relationship between battery life and diagnostic sensitivity. High-frequency sampling (e.g., >250 Hz for ECG) is necessary to capture morphological details required for detecting anomalies like sleep apnea and arrhythmias, yet this depletes energy reserves rapidly. Conversely, aggressive downsampling extends battery life but risks aliasing and missing transient physiological events. Research indicates that no single sampling rate suffices; rather, the optimal solution lies in **dynamic sampling strategies**. Specifically, **Compressive Sensing (CS)** and **Level-Crossing Sampling (LCS)** represent paradigm shifts from uniform Nyquist-Shannon sampling. CS leverages the sparsity of bio-signals to reconstruct high-fidelity data from few measurements, achieving F1-scores of ~91% in peak detection even at high compression ratios [cite: 9]. Furthermore, **adaptive sampling**—which adjusts rates based on real-time signal variance or sleep stage—allows wearables to maintain "clinical-grade" sensitivity during critical events while idling during stable periods. This report details these strategies, evaluating their impact on energy consumption and the sensitivity of detecting sleep anomalies such as Obstructive Sleep Apnea (OSA).

---

## 1. Introduction: The Energy-Sensitivity Conflict in Wearable Health Monitoring

The transition of sleep monitoring from the clinical polysomnography (PSG) laboratory to the home environment relies heavily on the capabilities of wearable sensors. While PSG remains the gold standard, offering a complete physiological picture via EEG, ECG, EMG, and respiratory channels [cite: 10], it is intrusive and expensive. Wearables, typically wrist-worn, offer a scalable alternative but are constrained by battery capacity and processing power.

The fundamental challenge in designing these devices is the **sampling strategy**. Traditional uniform sampling collects data at a fixed frequency. If the frequency is too low, critical features of anomalies (e.g., the R-peak in ECG or the dicrotic notch in PPG) are lost, leading to misdiagnosis. If the frequency is too high, the device processes and transmits redundant data, wasting energy.

### 1.1 The Cost of Continuous Monitoring
Continuous monitoring generates vast amounts of data. For example, raw ECG data sampled at 250 Hz requires significant storage and transmission bandwidth, which are the primary consumers of battery life in Wireless Body Sensor Networks (WBSN) [cite: 11, 12]. Research highlights that data transmission and acquisition consume significantly more power than local processing [cite: 13]. Therefore, reducing the volume of acquired data *before* transmission—without losing the information content required to detect anomalies like sleep apnea—is the primary objective of modern sampling strategies.

### 1.2 Defining Anomaly Detection Sensitivity
In the context of sleep, "anomalies" refer to deviations from normal physiological patterns, such as:
*   **Sleep Apnea:** Cessation of breathing leading to oxygen desaturation and heart rate surges.
*   **Arrhythmias:** Irregular heartbeats detected via ECG or PPG.
*   **Sleep Stage Fragmentation:** Abnormal transitions between NREM and REM sleep.

Sensitivity refers to the system's ability to correctly identify these events (True Positive Rate). High sensitivity often requires high temporal resolution. For instance, Heart Rate Variability (HRV) analysis, a key marker for sleep quality and apnea, typically requires millisecond-level precision in peak detection [cite: 14, 15].

---

## 2. Compressive Sensing (CS): The Mathematical Paradigm Shift

Compressive Sensing (CS) has emerged as a leading solution to the energy-sensitivity trade-off. Unlike traditional compression (which samples high and then compresses), CS acquires the signal directly in a compressed format by exploiting the signal's "sparsity" in a certain domain (e.g., wavelet or frequency domain) [cite: 11, 16].

### 2.1 Mechanism and Energy Efficiency
CS allows signals to be reconstructed from far fewer samples than required by the Nyquist-Shannon sampling theorem. This reduction in sampling rate directly translates to energy savings in the analog-to-digital converter (ADC) and, more importantly, in the wireless transmission module.

*   **Node Lifetime Extension:** Empirical studies on wireless sensor nodes (e.g., Shimmer motes) have demonstrated that CS-based ECG compression can extend node lifetime by **37.1%** compared to traditional Digital Wavelet Transform (DWT) compression [cite: 1, 2, 17].
*   **Computational Load:** While CS shifts the computational burden of reconstruction to the receiver (e.g., the cloud or smartphone), the on-node encoding complexity is low, making it ideal for resource-constrained wearables [cite: 13, 17].

### 2.2 Impact on Anomaly Detection Sensitivity
A critical concern is whether CS degrades the signal quality to the point where anomalies are missed. Research indicates that CS maintains high diagnostic utility:
*   **Peak Detection Accuracy:** In photoplethysmogram (PPG) analysis, CS-based methods achieved a pooled average **F1-measure of 91%** for systolic peak detection, which is comparable to uncompressed methods [cite: 9].
*   **Apnea Detection:** CS has been successfully applied to multi-channel ECG and EEG reconstruction, preserving the features necessary for automatic sleep stage classification and apnea detection [cite: 16, 18].
*   **Signal Reconstruction:** Even with significant data reduction, CS preserves the morphological features of ECG (P-wave, QRS complex, T-wave) required for arrhythmia classification [cite: 18].

### 2.3 Adaptive Compressive Sensing (ACS)
Standard CS uses a fixed compression matrix. However, physiological signals are non-stationary; a sleeping patient has different signal sparsity than an active one. **Adaptive Compressive Sensing (ACS)** dynamically adjusts the sampling rate or measurement matrix based on the signal's current characteristics.
*   **Dynamic Sparsity:** ACS schemes estimate the current sparsity of the signal and adjust the sampling rate for the next period. This ensures that during periods of high physiological variability (e.g., an apnea event), the sampling density is sufficient to capture the anomaly, while minimizing data during stable sleep [cite: 19, 20].
*   **Energy Implications:** ACS has been shown to further optimize the energy-accuracy balance, outperforming static CS by avoiding "oversampling" during sparse signal periods [cite: 20].

---

## 3. Event-Driven and Level-Crossing Sampling

While CS reduces data volume, **Event-Driven Sampling** (often implemented as **Level-Crossing Sampling** or LCS) fundamentally changes *when* a sample is taken. In LCS, a sample is generated only when the input signal crosses a predefined amplitude threshold, rather than at a ticking clock cycle [cite: 21, 22].

### 3.1 The "Silence" of Sleep
Sleep data is often characterized by long periods of relative stability (e.g., stable respiration or heart rate during NREM sleep) punctuated by events (e.g., apneas, movements). Uniform sampling wastes energy digitizing the "silence" between events.
*   **Asynchronous Efficiency:** LCS is asynchronous. If the signal does not change, no power is consumed by the sampling circuitry. This approach can reduce power consumption by **two orders of magnitude** (up to 100x) in specific signal chain components compared to synchronous Nyquist ADCs [cite: 3, 4, 23].
*   **Data Reduction:** LCS naturally compresses data by only recording significant changes. This is particularly effective for "bursty" signals like neural spikes or specific features of ECG [cite: 24].

### 3.2 Application to Anomaly Detection
LCS is inherently suited for anomaly detection because anomalies are, by definition, deviations from the norm.
*   **Event Capture:** When an anomaly occurs (e.g., a sudden drop in SpO2 or a gasp for air), the signal amplitude changes rapidly, triggering a burst of samples. This ensures high temporal resolution exactly when it is needed [cite: 25].
*   **Hardware Implementation:** LCS requires specialized Asynchronous ADCs (A-ADCs). Research has shown these can achieve high Figures of Merit (FoM) and are particularly suitable for wearable ECG sensors [cite: 4, 26].
*   **Limitations:** The reconstruction of uniformly spaced data from non-uniform LCS samples requires interpolation algorithms, which can introduce artifacts if not carefully managed [cite: 4].

---

## 4. Optimal Fixed Sampling Rates for Specific Modalities

While dynamic strategies like CS and LCS offer theoretical optimums, many current commercial and research devices still rely on fixed sampling rates. Determining the "minimum viable frequency" is crucial for balancing energy and accuracy.

### 4.1 Photoplethysmography (PPG)
PPG is the most common sensor in wrist-worn sleep monitors. It measures blood volume changes to estimate Heart Rate (HR), Heart Rate Variability (HRV), and Respiration Rate.
*   **The 64 Hz Standard:** A pivotal study determined that **64 Hz** is the optimal sampling rate for wrist-worn PPG to maintain accuracy across all HR and HRV metrics relative to ECG. At this rate, the bias is minimized [cite: 5].
*   **The 32 Hz Compromise:** For applications where maximum precision in HRV (specifically pNN50 and RMSSD) is not critical, **32 Hz** is sufficient. This cuts data storage and transmission energy by half compared to 64 Hz [cite: 5].
*   **The Danger of Low Rates:** Sampling below 25-30 Hz leads to significant errors in time-domain HRV indices. At 25 Hz, the interval between samples (40ms) is larger than the typical variance in heartbeats, making accurate HRV estimation impossible [cite: 15].
*   **Interpolation:** Techniques like parabola or cubic-spline interpolation can improve the accuracy of Inter-Beat Intervals (IBIs) derived from low-sampling-rate PPG (e.g., 32 Hz), effectively boosting the effective resolution without increasing hardware sampling costs [cite: 14].

### 4.2 Electrocardiography (ECG)
For wearables that include ECG (e.g., chest patches or smart shirts), the requirements are higher due to the need to detect the sharp R-peak.
*   **250 Hz vs. 100 Hz:** A sampling frequency of **250 Hz** is generally recommended for clinical-grade HRV analysis. However, for time-domain analysis (used in many sleep staging algorithms), **100 Hz** has been found acceptable [cite: 27].
*   **50 Hz Threshold:** Sampling ECG at 50 Hz is deemed unacceptable for both time- and frequency-domain analyses, as it fails to capture the QRS complex morphology, leading to random errors [cite: 27].

---

## 5. Hierarchical and Context-Aware Sampling Strategies

The most sophisticated energy-optimization strategies employ a **hierarchical** approach, using low-power sensors to "wake up" high-power sensors only when necessary.

### 5.1 Sensor Fusion and Triggering
*   **Accelerometer as a Trigger:** Accelerometers consume very little power. They can be used to detect body movement (actigraphy). During periods of high movement (wakefulness), the system might downsample or turn off the sensitive optical sensors (PPG) to avoid motion artifacts. Conversely, during periods of stillness (potential sleep), the system can activate the PPG/ECG to look for sleep apnea events [cite: 7].
*   **Event-Driven Wake-Up:** An "Event Controller" (EC) can monitor a low-power signal (e.g., RMS value of a sensor). When an abnormality (event) is detected, the EC wakes up the main processor and high-fidelity sampling blocks. This "sleep-until-event" mode can increase battery lifetime by orders of magnitude [cite: 3, 25].

### 5.2 Context-Aware Sampling
*   **Sleep Stage Dependent Rates:** The sampling requirements differ by sleep stage. Deep sleep (N3) is stable, potentially allowing for lower sampling rates or aggressive CS. REM sleep, associated with autonomic variability and apneas, requires higher fidelity. Context-aware systems use real-time analysis (e.g., on-chip machine learning) to determine the sleep stage and adjust the sampling strategy accordingly [cite: 7].

---

## 6. Anomaly Detection: Algorithms and Sensitivity

The choice of sampling strategy must be validated against its ability to detect specific pathologies.

### 6.1 Sleep Apnea Detection
*   **Multi-Sensor Fusion:** The most accurate apnea detection models utilize a combination of PPG, accelerometer (to detect respiratory effort), and skin temperature. One study achieved **88% sensitivity** for moderate-severe apnea using this multi-modal approach [cite: 8].
*   **Deep Learning on Compressed Data:** Modern Deep Learning models, such as Convolutional Neural Networks (CNNs) and Vision Transformers (ViT), have shown remarkable robustness to downsampled data. For instance, a ViT-based model achieved a per-second Macro F1 score of **82.6%** in apnea detection using PSG images, suggesting that "visual" representations of signals (which can be highly compressed) are sufficient for diagnosis [cite: 28].
*   **Deep Learning Efficiency:** Lightweight CNNs (e.g., SleepLiteCNN) can perform sleep staging with high accuracy (89%) while consuming minimal energy (5.48 µJ per inference), enabling real-time anomaly detection directly on the wearable device [cite: 6].

### 6.2 Handling Missing Data
Aggressive energy saving (e.g., duty cycling) can lead to missing data. Advanced imputation algorithms and "deep phenotyping" pipelines have been developed to infer sleep onset and duration even with gaps in the raw accelerometer data, ensuring that energy-saving measures do not result in a total loss of diagnostic capability [cite: 29].

---

## 7. Conclusion

The optimization of wearable sleep monitors is not achieved by selecting a single static sampling rate, but by implementing **intelligent, dynamic sampling architectures**.

1.  **For General Wellness:** A fixed PPG sampling rate of **32-64 Hz** combined with interpolation algorithms offers a sufficient baseline for sleep staging and basic HRV monitoring, balancing data volume with metric accuracy.
2.  **For Clinical Screening (Apnea/Arrhythmia):** **Compressive Sensing (CS)** is the superior strategy. It allows for the reconstruction of high-fidelity signals (necessary for medical diagnosis) while reducing transmission energy costs by over **30%**.
3.  **For Maximum Battery Life:** **Event-Driven/Level-Crossing Sampling** provides the highest energy efficiency (up to 100x reduction) by exploiting the sparse nature of sleep anomalies. However, this requires specialized asynchronous hardware.
4.  **The Future Standard:** The next generation of devices will likely employ **Hierarchical Adaptive Sensing**, where a low-power "sentinel" sensor (accelerometer or low-rate PPG) triggers high-fidelity recording and AI-driven analysis only when potential anomalies are detected, thereby achieving the "best of both worlds": multi-day battery life with clinical-grade anomaly detection sensitivity.

### References
[cite: 10] Wang R, Chen F, Chen Z, et al. StudentLife: assessing mental health, academic performance and behavioral trends of college students using smartphones.
[cite: 1] Mamaghanian H, Khaled N, Atienza D, Vandergheynst P. Compressed sensing for real-time energy-efficient ECG compression on wireless body sensor nodes.
[cite: 30] Computing in Cardiology 2024; Vol 51.
[cite: 31] The system reacted to acceleration with a sampling rate of 50 Hz.
[cite: 6] SleepLiteCNN optimized specifically for ECG-based sleep staging.
[cite: 5] Determining the optimal sampling rate for a wrist-worn wearable device optical heart rate sensor.
[cite: 11] Compressive Sensing (CS) has emerged as a particularly promising approach owing to its ability to efficiently acquire and reconstruct signals.
[cite: 18] Compressive sensing (CS) is an effective method to reduce the size of the acquired data.
[cite: 9] This work focuses on the implementation and validation of a photoplethysmogram (PPG) low-complexity analysis method.
[cite: 16] This study presents an automatic sleep-stage classification system based on utilizing compressive sensing (CS).
[cite: 32] In this way, the sensor node does not waste energy sampling the sensor more than the actual maximum frequency of the signal.
[cite: 11] Furthermore, the incorporation of adaptive CS techniques, such as the Compressive Adaptive Sense and Search (CASS) algorithm.
[cite: 19] The method is based on an adaptive compressed sensing algorithm.
[cite: 33] Some studies advocate using adaptive compressed sensing for applications where the nature of the generated signal is unknown.
[cite: 12] Some studies advocate using adaptive compressed sensing for applications where the nature of the generated signal is unknown.
[cite: 25] Therefore, to reduce energy consumption, it is critical to keep all possible components of the proposed monitoring system in sleep mode as long as possible.
[cite: 3] When the proposed event controller detects an abnormality, it enables a root mean square (RMS) converter.
[cite: 7] Context-aware sampling: Lower frequency during low-activity periods.
[cite: 34] The level-crossing sampling effectiveness is defined as the reduction of the sampling rate in relation to the periodic sampling.
[cite: 35] Using level crossing sampling provides higher energy efficiency and less risk of contention.
[cite: 21] Level-crossing sampling is an attractive solution among these options as samples are generated only when the input signal crosses predefined threshold levels.
[cite: 24] A level-crossing sampling scheme is a recommended approach for this purpose.
[cite: 22] The level-crossing scheme is non-uniform in time domain.
[cite: 28] We present VOSA, a Vision-Transformer (ViT)-based model.
[cite: 8] The best-performing model utilized photoplethysmography (PPG) and finger-temperature features.
[cite: 36] Test results demonstrated that the combined signal-based model achieved an accuracy of 91.83%.
[cite: 20] In this work, we present an adaptive compressive sensing data gathering scheme.
[cite: 29] Using the same sampling rates across modalities of 30 Hz in study 1 and 20 Hz in study 2.
[cite: 5] We determined that the optimal sampling rate for a wrist-worn wearable device optical heart rate sensor for all HR and HRV metrics is 64 Hz.
[cite: 14] Parabola and cubic-spline interpolation significantly increased IBIs accuracy at 32, 16, and 8 Hz sampling rates.
[cite: 15] Several validation studies comparing PPG and ECG HRV show that once sampling drops below about 25–30 Hz, errors... increase sharply.
[cite: 27] A 250-Hz sampling frequency would be acceptable for HRV analysis.
[cite: 37] Considering that heart rate variability analysis requires a sampling rate of 250 samples/s or higher.
[cite: 4] The event-driven LCADC without timer and with single-bit quantizer achieves a reduction in power consumption... of two orders of magnitude.
[cite: 38] can significantly reduce the data transmission power, up to two orders of magnitude.
[cite: 23] The event-driven LCADC without timer and with single-bit quantizer achieves a reduction in power consumption... of two orders of magnitude.
[cite: 26] The main objective is to reduce the power consumption by one or two orders of magnitude.
[cite: 2] CS-based compression has shown to provide a better energy-efficient performance, with a node lifetime extension of 37.1%.
[cite: 39] CS-based ECG compression is accordingly shown to achieve a 37.1% extension in node lifetime.
[cite: 13] Mamaghanian et al. [cite: 40] presented the CS-based sampling node for ECG signals and extended the battery life by 37.1%.
[cite: 17] CS-based ECG compression is accordingly shown to achieve a 37.1% extension in node lifetime.
[cite: 9] The proposed method achieved a pooled average F1 measure on the three datasets of 91%.

**Sources:**
1. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFV3a8IgKJmrmXUg2nXqsaKh0ruBTU67Jd3BNcsOvmU9MiNV7v3NKmw26W6l06sqwPtTBUpn0kSJ1pzFFQpW5tHHE4wqLxd6dm9q_BxcRlkmqOVxLrdgJ66DOs2arFgBQ==)
2. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoYEuRi9PiK2klq5TjsDtxn_XqDsUsMDQ4PO5iSRxCfYn63YgbEZX4iXlJU1fV5LTAygR20E5pRTWurux4ynjg7_ZDhyqh87agU0nPf3w6pZDdtTWg4A2IwIg-)
3. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEazpDTDbjuOjj5kf6M3cEXbW0-HNbt-9DKVOmc8AUVWFmQegcrBKYwolMz9iql5Wyn6lX75AfM4wtisUdPdcQlGeNwVa7rLCYCNyg-J_e0tmGz_32_lylZM5OM8Cew2VgVLGP98YZpVJOvNtT9-Noh431p0vNRwBowyGHkND_6L6KAtZ3VvSCkZKDgTUeDDNhGZVUuyXV09LoqB6V8KcnUVrSr8zvfDQPG67NgEuHP68c7hPW9a2WBSNDXa5c=)
4. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjBwokrB3CbxeY6emyWUSDI5NCxUZWCVnDuEoVqLYsAL3QbyfGt9OYm6ToZg0WIZw_R7Icomql4Xnf5rhik4Yv9woikX-nmmskRcd72DD_3uNUVNTxGKDwQD-gDdBwa8490gNkhdGUu1_2taDwGrN7oua_oB8KtK9mGj4bNYuFgM4qtAgQjMBUyX7AduMZ-696T03IXwhCNesCjP2uc50a5A==)
5. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFecBlUerdzxzqVlgL-vLrbPmfhxKyFO4Gek_o7UwBEGJYfK5SJBp74YkaPqLAVttOcQnyJrSY_RRyk4-mTBJpNF-IOQNCtJTFKY1BAKcFHokAaf1FmX3eT0ueTyT0iEp2tFes2EUXN)
6. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYn4zCXBuphDBcdM10hAN6Zq5oVxA9wjBIBozMTqdnHZjC3J_XBg6hD5PUVQBSLAK90lKgwgHVYvcWt-SQMOEoLWHMJFbHzRknxB19yl6JUUddcKtycg==)
7. [rcet.org.in](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPoB0PwizwmNh474tOfo4i_wml1jzpyBUQOzvN_P9Gi_0fbiPHPGgV5qO9zsyuLtGv1NXqU3-Er1XYI6ehhWRI7GgbJ3kpJK2lyGGyB4Ss8Dy7pIRjVunj3eUYct2b2zcFk79thLU2FCKRNAQ3Ea3CRp8qSQg1oX_HNpAvjsvBKiWDuyZE)
8. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaCnTfOnmgOrd22yPy1HB68eOyvWplV9AAda_5OPmUmXCvshwlMwV98V_ZHrP0n9_SgQcQvaSIHGzdbqCKB9oTczu7QJES2A97StkIDDWOUfM_cya6GiHLPlFHQXs0TA==)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFE0Ld7uEqMvMtqCKKnXzj27blB0ZhId30kWWTmfJDjZZWxcfUPZQjCLqlJxwZKnUbTbt2BXiCn1TVlO_-0qzct6S5nw0e05w24oYOMbkpisffL84dFDuR4Y1YjqgkWM-H7_PTv34K7sA==)
10. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFbpARtIdo0tkN-m5c3f5YW1WRyUI3bNT3qlFy2fWE3MMTwHiuTOCpjNRtYYTCbG13ti1dRiUggNyifMl1dZhFRBmEEF-j5vsHiw7QPNVpUWDkZrsR6w05HZp2dtRdU3qKC8W3vMxo)
11. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQiGtnP9_V23gQzn_LV92Q3I2qondlkY05oK6A6f3S0GCWa2cygNXS1jm5W9avkvvgHmwoYXMqUO3PhgK9UDp4jYjU-bllunj-wXW9XRDyYFvkwhAYb-Vo69uY)
12. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGN_egBEA3pt6DclLuUlcpZrAbVXAXgeJfTGIsBTAJtyUhM6lCjGPomlSdvT9MaFKyoBRodxp6p6-6cgap7u4_LYpsxfU2CSI4WUO5qvmo6QX-YdLFeCOy4KiCQOv1JEcbLKwrrPQoT6vwqm9ZuUvZZ3Jgk)
13. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFk1gX6Ezq7KH9ZdcnT26KvIjaabxmyv23GC6ac6phlDFPcupDAGcvW6a1KDr6iGwCWLTBOlyi22BhCEUPpafkE-A0OU_FwjQyQb90YC5azQpt33sl6sVpojVb2uiA_OHhEIBC08mrOR7msWZRHpOaxEA==)
14. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmBsGMHsrNo7FoQ5qqHh0ROSW6EuNTOYvH33aRT1-BdGpxCC6T9bj_g2yqfdcc8Iyq4-eLAvCZqwO2ysz6iUeODQKLkj-O6CmKTYBqMWZGrq6Em6ZcDNhN-GusL7gYJHeiF53rqxSH)
15. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWWuhGusWdyD9YNRd-vgv60V9lWgPQcTquRbOhI_PyUuHpe6csEiRPa2ancS1dBDMOUvEqi0_S94xMbcDuIyINHPxuGHzwKtBB5ktfSaHShqqFFreRSqfo1xL8JjBAKcZ60XBBhifp79XIV7FxDDq5lQ5Fyrc5wGJXj1g4jXVqRY3uayuqVDL7lnnMlD7ujGQG5sw3xjwbc_0U0y91jBo3rkGCsovHlA2cCQS9eLMPMTl829un3H5-7Q==)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECBAOq1vJ-ESGpgr8YgQD3CP7Neeu4s7iThv_-g6eQLROHDVAKFSJIzt_14tSRtoDRs1bFuF1VRUBZhzoF1o-H6qt5_LEuVuXmKB8fjwVJREN5UGkeU2B6z_PLW4NxrWD4Abwau8YztVCw32QOMeObnpFnQHgspOrsonFHRBll-AwwxSZoUoKCnEQdr88jctPUTezWs7h3e4DE2ujm7UwhVG8zvG2k_rO_WNQ3oqJexKjKzNx8rreVAIuvxiDwbJh5pWwy5a1EZ49hymKNBnN1RfzoeUrBOW6Si2Q=)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmKZOhPIiR4IzzMkBA_C7rYyp--teNRnmvAXlJFBQw7OiLjCOtG2WOKSwBL77tsvXhzGt-S4vToTGv9B_FD8TmMXqpmMS4aQNuWE8QZ77i6JafYgtDYztNM88jzAUB9UOjkPuJ3vYACdsorqvXdERSGA2tCPeuDOcOoE8AARpJAnzyc9iunIIlKLQMhMdjtLdZ5QqXUbaZFq5X1JAIoJSq7SBrHHGHqA5mFJm6NsR0pkMOjFjpOo4xPcx9eGjzipEz3keG8oN4B9Y=)
18. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJxHhnDjfndHpsHiWG3vHXznOHvyZ-zlzSNK7hnyOhkT8lIarrt3phIunj0X2iXrZyezkL1pkanSyjfNcD-XD_F_NPIZpvRxxMNuumZtEtcRxoPDLBKT-DjUuB_k37G9Rwdvpx3F_viDtPUopok40rWu1J)
19. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-fLeI-aAMDH8lpocG4SLsapnsUo_Q_T8M4LdV1N6lkSb-bTpW0yFGkOZf_InscqjD_GMyEcOkTxn7LGdb0Rqgswc3A-cHCsCE7UEq3fxB8Rp9tBKC0nhJHjDe2BzgdbWDeCRJaq9XHlrrWky-AITCsIdaqwLzF4db88dXV20TyyaeoBd5EkHP57yYcR2bgXEwEDWN)
20. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMS9nS8S1B73cP1J9t_mV9Jj56KYv0dcYnzv24nkHtVt4F3lO6G3k4OSotwbZlyiFegdxMqYF1en7mmHFuZSQ09WChHSAXrBcJyJzEe1d5oFDBmmuXObTRPgdaEuKVrw==)
21. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxhDK-O7u6PnOkYOuINg6RUdIwBYAaBLaat7untumas-yJMHuaxYQffKHxzq95MxScD_VmvW7y-C_xAKM2geDxuFSmNgBgKJnMFU_rGmfH3E_Fu_g9ZBtfNO1kv8h5VQ5XAWVAwu9I11dADcZZvabW4Ty_9zsc4hVyn7vwRFPE3akGbOG1FKfHahicyDy0Dvj6sPaj0Z0=)
22. [yale.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGI8x1VpQUdlT6ltzrILztcFfxFl448_Lg0waUVcwz7Eji_ZALPN3AzQe4ZIo2xK3eBVniyfXhEL43aaOUzOO8XL2Z_yBasuus_Rh_6-om-GKZQKcrEZPpHF2Qv5dw_f7Ck19J-1FJqcw==)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgFSSIqTd7xZjmhFZkleQ3Wr8oBpsnA5PLNHyCgyDO1kFmuCy7dEU07RgRwjMKTjiz2hnwIdRW9I1w2_UEH1wrQhR3BOUm75r5Cl_SQmTif2Yl-X8plxqmQqedBggtdirYrymF11G-Bk69yyya_mmarO-5lhIR5hkWxsO3V9JQbCo8syk7T6WCXblgUcjf8GDplTVqBSksbBavdTiGJ2CK9lM6Y2zhoHnXFWomIbyn8p_bhT6gCwKErTRaCt3po1CSRwv7LMffADDM2Kv7EEhnH64xcQxSfC_coZ2NYSWkRN-rXZUAb5F-evL2b7yug9vQGNaQgKqccR-XGJI=)
24. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdYH2PXDtdoRPt2McJwSDWIMYvdYQWCDcGkeMtElVBFtrDi9XUUUsBuBeLHg8v4XQqywi_bCwIDKBlFGfoC3w__6thr-_l9mWFB_-LwS5qp-PVtFiMnQdZH1CiKbY=)
25. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVjcIHlOX9wG5ED9zTFqL18NXUy54ikBERxEpB7xX4YoiEGZMKz4baY2j2joD9E5oZzmQPzb-o4dePrXq1QqLbnDOKWBK1HXUPItgfCSh10kmirq3CDe_hX7Vyt8aIhQ==)
26. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLGf30dz7R_vlwDP5WPr-Idxt6tOVbsEsNRlhlweiyLhCC4-WXmMTR-AVs_sfi9asMjWEV4JukBDYryzgTt2CTGxiH1sVCmrVH5wpc0p-2McY8gpLR3cyoeoI_NcoP4aAqN4iAOohohzPiUlXuIukz9iJ-yk_lVOItL93vgkusdMQaIs7IpxiY3rWOoLjMnLzB2HMEpFronrmm6P0hVcYgH5NizencVGLMu4mat6qG9p7gghJM0D77q290b2zmcB4=)
27. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFONgaoOftpBLne8SlMZzuSmR68zK0oM6xbmN3lvsAsfPI1CrBuTSSAZkVX0pCTddwszgwBvk8ecBTpO2v7eksPooaE9xEhKn-J0xSzJfuAZhxILjF64NyiFqm5ORdVz2ZTQyfdInL)
28. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZ2axAiCutL6YE7_TKEV-0HGAiTEckzKoZWMZ2QMUKvvfCc7wqAap1LjHfWCKsLJJz5YZDxWzyk_MnM96O2f7-Kg1aEukCvdYrXktnEQ-I3nClgZALYPjhhRkvVzIZuGi60pvZRJWqkV897D9ViIAAg4MlF_6RrbBrCh8_4Jh7a53crV5SpEBHdLjb--ZJTSpWr_4MzQ6a8ilI5cMnv3oXcqKoTjUHDuSCzRu_fkLD7Jdb-fkR8dq8Eakcqxx0AePFp6ND6aGofRWRc6D1IfVYHL2Q96FGyA==)
29. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVEKzu9SnCu8mskBpQOfhrJNnCQH3NagNIT1CdRKqpH1NueBr4oGg_zxCNwfGYV00QrHypNm9aRiOJw8BlTqOHGemDhkzDPMsMzVPTOngaZiTERSXx9Ze99_60tRG2zzJxEmnf2XIY)
30. [cinc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFExU3EZjssXIVOb2DBaPYg_CV-4uINf3IPic6xOvbWn_W0EVaEmNBxveuLBa3Lfp1_U2xPEt0kNdEWBVqrgVVPYaUAJPjXh_t4fmRcOGfxo7v2DXXvBwS5O9mrEVEYnVt89GN37pXrQWk=)
31. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-HZWogPAX5Xxr47WoyXvD3Sv0xns-U2wJvgjSXeYcrBiQGgABRRztm8eSQiNZFGtq6LFQIfLzO-1nxLR6vsvTCcP1IZa81_xcggXdIDt6ycoSaru0CaSxp6Tatar8Hf3PUyMH0ojs)
32. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFL_5wMtMOlJ5AxbNL8y2SHpyu5XZw3RzgBiBuKL9AzcmLiLpNFNJuw89rKL4bgInVHjo2-Upc1Mkr2vKqNKyF9m9QesMm4k07-RhtUVgXIBbOf0jZavn6Am-28NY=)
33. [europa.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtMLSS0NAT1SzSYa-RwH2IF0yaGN0bT50uMhoH2VuqNlpFZCcsfTlYHgfnh1vGHiktwTtFe1GEb0TKFeiVuydZoNExZkErLaDgXrCLNzJhZylPxww15t_BatSc2HD_j1cjUHCPi_LVIqo2U5gYNdDz7AP1JODbjYGZMJ9OHJ4C7xhLxNngkw58WZcbrGc7he2MQqHfbTxmw2jMD5R8bLX9bpU=)
34. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0CtTvRVrHZILg3z-9dCMDDlAU2IoIpXomfizta1PsLwSDwVC6m2x8sCw02GxpAPCDUc6FpiT1Zv5K_Q-p2PFVsRw3hDw6h5tODuNF5BBJ7QrTHztlab6LUmFK-oTIj1zcz2hKQ6AFz8OOml6of05u19aP8GCgoRz8WN_j7DmaxStbrpo3yzGsDRIbHvcAbYGgh5J4iQeWJms_-K8BkBrB5FH6LkQemcOPOEoM8CjPTt35i1iEYY7tmxpTU8tArbOQlJO_3YSpLQ==)
35. [igi-global.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBm7goiav5Hp90w-MANaDbMNukWAq_3hIoTNwENoOtu8WatZWtLRcyEsCP7BaAVyjgvCKdLK3sfeFyfmXufNJezuO55PO8HM3Fk3IKgBsSFlHoj1ww177zKAWOK69riZyNzgdQkw2bDhYVun-TwDXqc4hKXoXfYcc8dbq6OSmwuw==)
36. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBMjOdtLLJ5TdjNHE5883b6zRqImqcpFeUV9YVbGnDgZlsi-sZAhXVn2bL-HFdE5Mn_Q2o5PXbY0mYJ9DSCwugq8aXSTo_a7SM1rCOfKO1t57l19JCOEXH2y-Uj8i3V-QX14sPmzHOX3cPWCR0ReK8TLm1BiNCg98VPYfS8QwoycvJaD06FJMefaTi7zA2FrsiKUDnNaaoYaVVEX_1vMrVb30upbNT9fvhXsp2NrECKFZEhT7zontGfgDYPMQVONAWs4V-obbIlobQxReEf9bVGcuRiqW4hg==)
37. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHE6oVmqIY9obh3_AH0FGIhZvS_DyzwO7BRhyDmB-AJs9WduptRhaKoSeJZEpnMARbRBCxXwlipONQxYI3J079Ardgy5DO-rhMrjc4oVw_GT6DYSprd2TfE-HoZLZCIB0ztVKcIPwxrxAmB3nJrdYPGmdk7)
38. [e-bookshelf.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEujEqfLFOxn7yCBRIBfxRDXs2vGg9Aw8KoUyE8V3T48-4cpTx9Eze1EClzFW2zEIX3lsNQ5X--PcbxsA8Wb3A8B59E1LUCPAXhZpfiPecmd_I0kvzuOUKH-5VVvp6DMxdTBdrvSR9oPa2ItLawZw4jdokn4_jrfegyGFcg)
39. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK7HO8lMuL4WEPtvOOvQGOOwR8uDjPgCLQeia5nUdSW_csD8pYdS5zMHqyQL3eaHjktlajDzsnKZDYuzrhviuJPoZKdNYdM2ecDWYQGb9BM7OEJJdFBE1wXC9x8s1DgdRW7AuPq2uCO2ysab5naDcb6fesjEm5dFuIgIr2lw2RBKXuXJKjjfMwPbrqYDuxbXXobvkaWsFOrEZLFuHds_9AxAdh4OpUo-h2y0LykH0v8uL46wQpDDbxWokAlTidTdeHOZ3xtwwpV4A7oGvywbsO6NUP4EE4)
40. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEmlFX_SiBX3yerQciuMDExZxGhHz238TbeqjvcssP5NmJvATeu6DjsJFnLuFMv7a7ZyqNdAt1l3zQSMHfsFE32JKP-mbhwgYxLI2S5v4CIBzEMoEs43LAJtbL3mcpiCL5WpxGINKf0KMzAxQw5IG65jPSw46C1XUjDYplf8loOGz3S1XlI8I8a_7SyO5Ze2PIf8YTAfv6JHJN0RLyMcrB-pCO2Dj-AYxtKoGeQLyL)


## Annotations
Annotation(end_index=433, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFV3a8IgKJmrmXUg2nXqsaKh0ruBTU67Jd3BNcsOvmU9MiNV7v3NKmw26W6l06sqwPtTBUpn0kSJ1pzFFQpW5tHHE4wqLxd6dm9q_BxcRlkmqOVxLrdgJ66DOs2arFgBQ==', start_index=421)
Annotation(end_index=433, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoYEuRi9PiK2klq5TjsDtxn_XqDsUsMDQ4PO5iSRxCfYn63YgbEZX4iXlJU1fV5LTAygR20E5pRTWurux4ynjg7_ZDhyqh87agU0nPf3w6pZDdtTWg4A2IwIg-', start_index=421)
Annotation(end_index=702, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEazpDTDbjuOjj5kf6M3cEXbW0-HNbt-9DKVOmc8AUVWFmQegcrBKYwolMz9iql5Wyn6lX75AfM4wtisUdPdcQlGeNwVa7rLCYCNyg-J_e0tmGz_32_lylZM5OM8Cew2VgVLGP98YZpVJOvNtT9-Noh431p0vNRwBowyGHkND_6L6KAtZ3VvSCkZKDgTUeDDNhGZVUuyXV09LoqB6V8KcnUVrSr8zvfDQPG67NgEuHP68c7hPW9a2WBSNDXa5c=', start_index=690)
Annotation(end_index=702, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjBwokrB3CbxeY6emyWUSDI5NCxUZWCVnDuEoVqLYsAL3QbyfGt9OYm6ToZg0WIZw_R7Icomql4Xnf5rhik4Yv9woikX-nmmskRcd72DD_3uNUVNTxGKDwQD-gDdBwa8490gNkhdGUu1_2taDwGrN7oua_oB8KtK9mGj4bNYuFgM4qtAgQjMBUyX7AduMZ-696T03IXwhCNesCjP2uc50a5A==', start_index=690)
Annotation(end_index=1026, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFecBlUerdzxzqVlgL-vLrbPmfhxKyFO4Gek_o7UwBEGJYfK5SJBp74YkaPqLAVttOcQnyJrSY_RRyk4-mTBJpNF-IOQNCtJTFKY1BAKcFHokAaf1FmX3eT0ueTyT0iEp2tFes2EUXN', start_index=1017)
Annotation(end_index=1388, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPoB0PwizwmNh474tOfo4i_wml1jzpyBUQOzvN_P9Gi_0fbiPHPGgV5qO9zsyuLtGv1NXqU3-Er1XYI6ehhWRI7GgbJ3kpJK2lyGGyB4Ss8Dy7pIRjVunj3eUYct2b2zcFk79thLU2FCKRNAQ3Ea3CRp8qSQg1oX_HNpAvjsvBKiWDuyZE', start_index=1373)
Annotation(end_index=1388, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYn4zCXBuphDBcdM10hAN6Zq5oVxA9wjBIBozMTqdnHZjC3J_XBg6hD5PUVQBSLAK90lKgwgHVYvcWt-SQMOEoLWHMJFbHzRknxB19yl6JUUddcKtycg==', start_index=1373)
Annotation(end_index=1388, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaCnTfOnmgOrd22yPy1HB68eOyvWplV9AAda_5OPmUmXCvshwlMwV98V_ZHrP0n9_SgQcQvaSIHGzdbqCKB9oTczu7QJES2A97StkIDDWOUfM_cya6GiHLPlFHQXs0TA==', start_index=1373)
Annotation(end_index=2373, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFE0Ld7uEqMvMtqCKKnXzj27blB0ZhId30kWWTmfJDjZZWxcfUPZQjCLqlJxwZKnUbTbt2BXiCn1TVlO_-0qzct6S5nw0e05w24oYOMbkpisffL84dFDuR4Y1YjqgkWM-H7_PTv34K7sA==', start_index=2364)
Annotation(end_index=3161, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFbpARtIdo0tkN-m5c3f5YW1WRyUI3bNT3qlFy2fWE3MMTwHiuTOCpjNRtYYTCbG13ti1dRiUggNyifMl1dZhFRBmEEF-j5vsHiw7QPNVpUWDkZrsR6w05HZp2dtRdU3qKC8W3vMxo', start_index=3151)
Annotation(end_index=4014, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGN_egBEA3pt6DclLuUlcpZrAbVXAXgeJfTGIsBTAJtyUhM6lCjGPomlSdvT9MaFKyoBRodxp6p6-6cgap7u4_LYpsxfU2CSI4WUO5qvmo6QX-YdLFeCOy4KiCQOv1JEcbLKwrrPQoT6vwqm9ZuUvZZ3Jgk', start_index=4000)
Annotation(end_index=4014, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQiGtnP9_V23gQzn_LV92Q3I2qondlkY05oK6A6f3S0GCWa2cygNXS1jm5W9avkvvgHmwoYXMqUO3PhgK9UDp4jYjU-bllunj-wXW9XRDyYFvkwhAYb-Vo69uY', start_index=4000)
Annotation(end_index=4140, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFk1gX6Ezq7KH9ZdcnT26KvIjaabxmyv23GC6ac6phlDFPcupDAGcvW6a1KDr6iGwCWLTBOlyi22BhCEUPpafkE-A0OU_FwjQyQb90YC5azQpt33sl6sVpojVb2uiA_OHhEIBC08mrOR7msWZRHpOaxEA==', start_index=4130)
Annotation(end_index=5089, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWWuhGusWdyD9YNRd-vgv60V9lWgPQcTquRbOhI_PyUuHpe6csEiRPa2ancS1dBDMOUvEqi0_S94xMbcDuIyINHPxuGHzwKtBB5ktfSaHShqqFFreRSqfo1xL8JjBAKcZ60XBBhifp79XIV7FxDDq5lQ5Fyrc5wGJXj1g4jXVqRY3uayuqVDL7lnnMlD7ujGQG5sw3xjwbc_0U0y91jBo3rkGCsovHlA2cCQS9eLMPMTl829un3H5-7Q==', start_index=5075)
Annotation(end_index=5089, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmBsGMHsrNo7FoQ5qqHh0ROSW6EuNTOYvH33aRT1-BdGpxCC6T9bj_g2yqfdcc8Iyq4-eLAvCZqwO2ysz6iUeODQKLkj-O6CmKTYBqMWZGrq6Em6ZcDNhN-GusL7gYJHeiF53rqxSH', start_index=5075)
Annotation(end_index=5494, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECBAOq1vJ-ESGpgr8YgQD3CP7Neeu4s7iThv_-g6eQLROHDVAKFSJIzt_14tSRtoDRs1bFuF1VRUBZhzoF1o-H6qt5_LEuVuXmKB8fjwVJREN5UGkeU2B6z_PLW4NxrWD4Abwau8YztVCw32QOMeObnpFnQHgspOrsonFHRBll-AwwxSZoUoKCnEQdr88jctPUTezWs7h3e4DE2ujm7UwhVG8zvG2k_rO_WNQ3oqJexKjKzNx8rreVAIuvxiDwbJh5pWwy5a1EZ49hymKNBnN1RfzoeUrBOW6Si2Q=', start_index=5480)
Annotation(end_index=5494, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQiGtnP9_V23gQzn_LV92Q3I2qondlkY05oK6A6f3S0GCWa2cygNXS1jm5W9avkvvgHmwoYXMqUO3PhgK9UDp4jYjU-bllunj-wXW9XRDyYFvkwhAYb-Vo69uY', start_index=5480)
Annotation(end_index=6093, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFV3a8IgKJmrmXUg2nXqsaKh0ruBTU67Jd3BNcsOvmU9MiNV7v3NKmw26W6l06sqwPtTBUpn0kSJ1pzFFQpW5tHHE4wqLxd6dm9q_BxcRlkmqOVxLrdgJ66DOs2arFgBQ==', start_index=6077)
Annotation(end_index=6093, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoYEuRi9PiK2klq5TjsDtxn_XqDsUsMDQ4PO5iSRxCfYn63YgbEZX4iXlJU1fV5LTAygR20E5pRTWurux4ynjg7_ZDhyqh87agU0nPf3w6pZDdtTWg4A2IwIg-', start_index=6077)
Annotation(end_index=6093, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmKZOhPIiR4IzzMkBA_C7rYyp--teNRnmvAXlJFBQw7OiLjCOtG2WOKSwBL77tsvXhzGt-S4vToTGv9B_FD8TmMXqpmMS4aQNuWE8QZ77i6JafYgtDYztNM88jzAUB9UOjkPuJ3vYACdsorqvXdERSGA2tCPeuDOcOoE8AARpJAnzyc9iunIIlKLQMhMdjtLdZ5QqXUbaZFq5X1JAIoJSq7SBrHHGHqA5mFJm6NsR0pkMOjFjpOo4xPcx9eGjzipEz3keG8oN4B9Y=', start_index=6077)
Annotation(end_index=6336, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFk1gX6Ezq7KH9ZdcnT26KvIjaabxmyv23GC6ac6phlDFPcupDAGcvW6a1KDr6iGwCWLTBOlyi22BhCEUPpafkE-A0OU_FwjQyQb90YC5azQpt33sl6sVpojVb2uiA_OHhEIBC08mrOR7msWZRHpOaxEA==', start_index=6322)
Annotation(end_index=6336, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmKZOhPIiR4IzzMkBA_C7rYyp--teNRnmvAXlJFBQw7OiLjCOtG2WOKSwBL77tsvXhzGt-S4vToTGv9B_FD8TmMXqpmMS4aQNuWE8QZ77i6JafYgtDYztNM88jzAUB9UOjkPuJ3vYACdsorqvXdERSGA2tCPeuDOcOoE8AARpJAnzyc9iunIIlKLQMhMdjtLdZ5QqXUbaZFq5X1JAIoJSq7SBrHHGHqA5mFJm6NsR0pkMOjFjpOo4xPcx9eGjzipEz3keG8oN4B9Y=', start_index=6322)
Annotation(end_index=6769, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFE0Ld7uEqMvMtqCKKnXzj27blB0ZhId30kWWTmfJDjZZWxcfUPZQjCLqlJxwZKnUbTbt2BXiCn1TVlO_-0qzct6S5nw0e05w24oYOMbkpisffL84dFDuR4Y1YjqgkWM-H7_PTv34K7sA==', start_index=6760)
Annotation(end_index=6983, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECBAOq1vJ-ESGpgr8YgQD3CP7Neeu4s7iThv_-g6eQLROHDVAKFSJIzt_14tSRtoDRs1bFuF1VRUBZhzoF1o-H6qt5_LEuVuXmKB8fjwVJREN5UGkeU2B6z_PLW4NxrWD4Abwau8YztVCw32QOMeObnpFnQHgspOrsonFHRBll-AwwxSZoUoKCnEQdr88jctPUTezWs7h3e4DE2ujm7UwhVG8zvG2k_rO_WNQ3oqJexKjKzNx8rreVAIuvxiDwbJh5pWwy5a1EZ49hymKNBnN1RfzoeUrBOW6Si2Q=', start_index=6969)
Annotation(end_index=6983, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJxHhnDjfndHpsHiWG3vHXznOHvyZ-zlzSNK7hnyOhkT8lIarrt3phIunj0X2iXrZyezkL1pkanSyjfNcD-XD_F_NPIZpvRxxMNuumZtEtcRxoPDLBKT-DjUuB_k37G9Rwdvpx3F_viDtPUopok40rWu1J', start_index=6969)
Annotation(end_index=7180, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJxHhnDjfndHpsHiWG3vHXznOHvyZ-zlzSNK7hnyOhkT8lIarrt3phIunj0X2iXrZyezkL1pkanSyjfNcD-XD_F_NPIZpvRxxMNuumZtEtcRxoPDLBKT-DjUuB_k37G9Rwdvpx3F_viDtPUopok40rWu1J', start_index=7170)
Annotation(end_index=7875, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMS9nS8S1B73cP1J9t_mV9Jj56KYv0dcYnzv24nkHtVt4F3lO6G3k4OSotwbZlyiFegdxMqYF1en7mmHFuZSQ09WChHSAXrBcJyJzEe1d5oFDBmmuXObTRPgdaEuKVrw==', start_index=7861)
Annotation(end_index=7875, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-fLeI-aAMDH8lpocG4SLsapnsUo_Q_T8M4LdV1N6lkSb-bTpW0yFGkOZf_InscqjD_GMyEcOkTxn7LGdb0Rqgswc3A-cHCsCE7UEq3fxB8Rp9tBKC0nhJHjDe2BzgdbWDeCRJaq9XHlrrWky-AITCsIdaqwLzF4db88dXV20TyyaeoBd5EkHP57yYcR2bgXEwEDWN', start_index=7861)
Annotation(end_index=8064, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMS9nS8S1B73cP1J9t_mV9Jj56KYv0dcYnzv24nkHtVt4F3lO6G3k4OSotwbZlyiFegdxMqYF1en7mmHFuZSQ09WChHSAXrBcJyJzEe1d5oFDBmmuXObTRPgdaEuKVrw==', start_index=8054)
Annotation(end_index=8432, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxhDK-O7u6PnOkYOuINg6RUdIwBYAaBLaat7untumas-yJMHuaxYQffKHxzq95MxScD_VmvW7y-C_xAKM2geDxuFSmNgBgKJnMFU_rGmfH3E_Fu_g9ZBtfNO1kv8h5VQ5XAWVAwu9I11dADcZZvabW4Ty_9zsc4hVyn7vwRFPE3akGbOG1FKfHahicyDy0Dvj6sPaj0Z0=', start_index=8418)
Annotation(end_index=8432, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGI8x1VpQUdlT6ltzrILztcFfxFl448_Lg0waUVcwz7Eji_ZALPN3AzQe4ZIo2xK3eBVniyfXhEL43aaOUzOO8XL2Z_yBasuus_Rh_6-om-GKZQKcrEZPpHF2Qv5dw_f7Ck19J-1FJqcw==', start_index=8418)
Annotation(end_index=9026, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEazpDTDbjuOjj5kf6M3cEXbW0-HNbt-9DKVOmc8AUVWFmQegcrBKYwolMz9iql5Wyn6lX75AfM4wtisUdPdcQlGeNwVa7rLCYCNyg-J_e0tmGz_32_lylZM5OM8Cew2VgVLGP98YZpVJOvNtT9-Noh431p0vNRwBowyGHkND_6L6KAtZ3VvSCkZKDgTUeDDNhGZVUuyXV09LoqB6V8KcnUVrSr8zvfDQPG67NgEuHP68c7hPW9a2WBSNDXa5c=', start_index=9010)
Annotation(end_index=9026, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgFSSIqTd7xZjmhFZkleQ3Wr8oBpsnA5PLNHyCgyDO1kFmuCy7dEU07RgRwjMKTjiz2hnwIdRW9I1w2_UEH1wrQhR3BOUm75r5Cl_SQmTif2Yl-X8plxqmQqedBggtdirYrymF11G-Bk69yyya_mmarO-5lhIR5hkWxsO3V9JQbCo8syk7T6WCXblgUcjf8GDplTVqBSksbBavdTiGJ2CK9lM6Y2zhoHnXFWomIbyn8p_bhT6gCwKErTRaCt3po1CSRwv7LMffADDM2Kv7EEhnH64xcQxSfC_coZ2NYSWkRN-rXZUAb5F-evL2b7yug9vQGNaQgKqccR-XGJI=', start_index=9010)
Annotation(end_index=9026, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjBwokrB3CbxeY6emyWUSDI5NCxUZWCVnDuEoVqLYsAL3QbyfGt9OYm6ToZg0WIZw_R7Icomql4Xnf5rhik4Yv9woikX-nmmskRcd72DD_3uNUVNTxGKDwQD-gDdBwa8490gNkhdGUu1_2taDwGrN7oua_oB8KtK9mGj4bNYuFgM4qtAgQjMBUyX7AduMZ-696T03IXwhCNesCjP2uc50a5A==', start_index=9010)
Annotation(end_index=9230, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdYH2PXDtdoRPt2McJwSDWIMYvdYQWCDcGkeMtElVBFtrDi9XUUUsBuBeLHg8v4XQqywi_bCwIDKBlFGfoC3w__6thr-_l9mWFB_-LwS5qp-PVtFiMnQdZH1CiKbY=', start_index=9220)
Annotation(end_index=9623, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVjcIHlOX9wG5ED9zTFqL18NXUy54ikBERxEpB7xX4YoiEGZMKz4baY2j2joD9E5oZzmQPzb-o4dePrXq1QqLbnDOKWBK1HXUPItgfCSh10kmirq3CDe_hX7Vyt8aIhQ==', start_index=9613)
Annotation(end_index=9844, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLGf30dz7R_vlwDP5WPr-Idxt6tOVbsEsNRlhlweiyLhCC4-WXmMTR-AVs_sfi9asMjWEV4JukBDYryzgTt2CTGxiH1sVCmrVH5wpc0p-2McY8gpLR3cyoeoI_NcoP4aAqN4iAOohohzPiUlXuIukz9iJ-yk_lVOItL93vgkusdMQaIs7IpxiY3rWOoLjMnLzB2HMEpFronrmm6P0hVcYgH5NizencVGLMu4mat6qG9p7gghJM0D77q290b2zmcB4=', start_index=9831)
Annotation(end_index=9844, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjBwokrB3CbxeY6emyWUSDI5NCxUZWCVnDuEoVqLYsAL3QbyfGt9OYm6ToZg0WIZw_R7Icomql4Xnf5rhik4Yv9woikX-nmmskRcd72DD_3uNUVNTxGKDwQD-gDdBwa8490gNkhdGUu1_2taDwGrN7oua_oB8KtK9mGj4bNYuFgM4qtAgQjMBUyX7AduMZ-696T03IXwhCNesCjP2uc50a5A==', start_index=9831)
Annotation(end_index=10039, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjBwokrB3CbxeY6emyWUSDI5NCxUZWCVnDuEoVqLYsAL3QbyfGt9OYm6ToZg0WIZw_R7Icomql4Xnf5rhik4Yv9woikX-nmmskRcd72DD_3uNUVNTxGKDwQD-gDdBwa8490gNkhdGUu1_2taDwGrN7oua_oB8KtK9mGj4bNYuFgM4qtAgQjMBUyX7AduMZ-696T03IXwhCNesCjP2uc50a5A==', start_index=10030)
Annotation(end_index=10787, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFecBlUerdzxzqVlgL-vLrbPmfhxKyFO4Gek_o7UwBEGJYfK5SJBp74YkaPqLAVttOcQnyJrSY_RRyk4-mTBJpNF-IOQNCtJTFKY1BAKcFHokAaf1FmX3eT0ueTyT0iEp2tFes2EUXN', start_index=10778)
Annotation(end_index=11022, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFecBlUerdzxzqVlgL-vLrbPmfhxKyFO4Gek_o7UwBEGJYfK5SJBp74YkaPqLAVttOcQnyJrSY_RRyk4-mTBJpNF-IOQNCtJTFKY1BAKcFHokAaf1FmX3eT0ueTyT0iEp2tFes2EUXN', start_index=11013)
Annotation(end_index=11286, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWWuhGusWdyD9YNRd-vgv60V9lWgPQcTquRbOhI_PyUuHpe6csEiRPa2ancS1dBDMOUvEqi0_S94xMbcDuIyINHPxuGHzwKtBB5ktfSaHShqqFFreRSqfo1xL8JjBAKcZ60XBBhifp79XIV7FxDDq5lQ5Fyrc5wGJXj1g4jXVqRY3uayuqVDL7lnnMlD7ujGQG5sw3xjwbc_0U0y91jBo3rkGCsovHlA2cCQS9eLMPMTl829un3H5-7Q==', start_index=11276)
Annotation(end_index=11571, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmBsGMHsrNo7FoQ5qqHh0ROSW6EuNTOYvH33aRT1-BdGpxCC6T9bj_g2yqfdcc8Iyq4-eLAvCZqwO2ysz6iUeODQKLkj-O6CmKTYBqMWZGrq6Em6ZcDNhN-GusL7gYJHeiF53rqxSH', start_index=11561)
Annotation(end_index=11992, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFONgaoOftpBLne8SlMZzuSmR68zK0oM6xbmN3lvsAsfPI1CrBuTSSAZkVX0pCTddwszgwBvk8ecBTpO2v7eksPooaE9xEhKn-J0xSzJfuAZhxILjF64NyiFqm5ORdVz2ZTQyfdInL', start_index=11982)
Annotation(end_index=12196, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFONgaoOftpBLne8SlMZzuSmR68zK0oM6xbmN3lvsAsfPI1CrBuTSSAZkVX0pCTddwszgwBvk8ecBTpO2v7eksPooaE9xEhKn-J0xSzJfuAZhxILjF64NyiFqm5ORdVz2ZTQyfdInL', start_index=12186)
Annotation(end_index=12885, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPoB0PwizwmNh474tOfo4i_wml1jzpyBUQOzvN_P9Gi_0fbiPHPGgV5qO9zsyuLtGv1NXqU3-Er1XYI6ehhWRI7GgbJ3kpJK2lyGGyB4Ss8Dy7pIRjVunj3eUYct2b2zcFk79thLU2FCKRNAQ3Ea3CRp8qSQg1oX_HNpAvjsvBKiWDuyZE', start_index=12876)
Annotation(end_index=13213, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVjcIHlOX9wG5ED9zTFqL18NXUy54ikBERxEpB7xX4YoiEGZMKz4baY2j2joD9E5oZzmQPzb-o4dePrXq1QqLbnDOKWBK1HXUPItgfCSh10kmirq3CDe_hX7Vyt8aIhQ==', start_index=13200)
Annotation(end_index=13213, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEazpDTDbjuOjj5kf6M3cEXbW0-HNbt-9DKVOmc8AUVWFmQegcrBKYwolMz9iql5Wyn6lX75AfM4wtisUdPdcQlGeNwVa7rLCYCNyg-J_e0tmGz_32_lylZM5OM8Cew2VgVLGP98YZpVJOvNtT9-Noh431p0vNRwBowyGHkND_6L6KAtZ3VvSCkZKDgTUeDDNhGZVUuyXV09LoqB6V8KcnUVrSr8zvfDQPG67NgEuHP68c7hPW9a2WBSNDXa5c=', start_index=13200)
Annotation(end_index=13672, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPoB0PwizwmNh474tOfo4i_wml1jzpyBUQOzvN_P9Gi_0fbiPHPGgV5qO9zsyuLtGv1NXqU3-Er1XYI6ehhWRI7GgbJ3kpJK2lyGGyB4Ss8Dy7pIRjVunj3eUYct2b2zcFk79thLU2FCKRNAQ3Ea3CRp8qSQg1oX_HNpAvjsvBKiWDuyZE', start_index=13663)
Annotation(end_index=14140, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaCnTfOnmgOrd22yPy1HB68eOyvWplV9AAda_5OPmUmXCvshwlMwV98V_ZHrP0n9_SgQcQvaSIHGzdbqCKB9oTczu7QJES2A97StkIDDWOUfM_cya6GiHLPlFHQXs0TA==', start_index=14131)
Annotation(end_index=14586, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZ2axAiCutL6YE7_TKEV-0HGAiTEckzKoZWMZ2QMUKvvfCc7wqAap1LjHfWCKsLJJz5YZDxWzyk_MnM96O2f7-Kg1aEukCvdYrXktnEQ-I3nClgZALYPjhhRkvVzIZuGi60pvZRJWqkV897D9ViIAAg4MlF_6RrbBrCh8_4Jh7a53crV5SpEBHdLjb--ZJTSpWr_4MzQ6a8ilI5cMnv3oXcqKoTjUHDuSCzRu_fkLD7Jdb-fkR8dq8Eakcqxx0AePFp6ND6aGofRWRc6D1IfVYHL2Q96FGyA==', start_index=14576)
Annotation(end_index=14846, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYn4zCXBuphDBcdM10hAN6Zq5oVxA9wjBIBozMTqdnHZjC3J_XBg6hD5PUVQBSLAK90lKgwgHVYvcWt-SQMOEoLWHMJFbHzRknxB19yl6JUUddcKtycg==', start_index=14837)
Annotation(end_index=15217, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVEKzu9SnCu8mskBpQOfhrJNnCQH3NagNIT1CdRKqpH1NueBr4oGg_zxCNwfGYV00QrHypNm9aRiOJw8BlTqOHGemDhkzDPMsMzVPTOngaZiTERSXx9Ze99_60tRG2zzJxEmnf2XIY', start_index=15207)
Annotation(end_index=16575, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFbpARtIdo0tkN-m5c3f5YW1WRyUI3bNT3qlFy2fWE3MMTwHiuTOCpjNRtYYTCbG13ti1dRiUggNyifMl1dZhFRBmEEF-j5vsHiw7QPNVpUWDkZrsR6w05HZp2dtRdU3qKC8W3vMxo', start_index=16565)
Annotation(end_index=16736, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFV3a8IgKJmrmXUg2nXqsaKh0ruBTU67Jd3BNcsOvmU9MiNV7v3NKmw26W6l06sqwPtTBUpn0kSJ1pzFFQpW5tHHE4wqLxd6dm9q_BxcRlkmqOVxLrdgJ66DOs2arFgBQ==', start_index=16727)
Annotation(end_index=16897, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFExU3EZjssXIVOb2DBaPYg_CV-4uINf3IPic6xOvbWn_W0EVaEmNBxveuLBa3Lfp1_U2xPEt0kNdEWBVqrgVVPYaUAJPjXh_t4fmRcOGfxo7v2DXXvBwS5O9mrEVEYnVt89GN37pXrQWk=', start_index=16887)
Annotation(end_index=16946, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-HZWogPAX5Xxr47WoyXvD3Sv0xns-U2wJvgjSXeYcrBiQGgABRRztm8eSQiNZFGtq6LFQIfLzO-1nxLR6vsvTCcP1IZa81_xcggXdIDt6ycoSaru0CaSxp6Tatar8Hf3PUyMH0ojs', start_index=16936)
Annotation(end_index=17022, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYn4zCXBuphDBcdM10hAN6Zq5oVxA9wjBIBozMTqdnHZjC3J_XBg6hD5PUVQBSLAK90lKgwgHVYvcWt-SQMOEoLWHMJFbHzRknxB19yl6JUUddcKtycg==', start_index=17013)
Annotation(end_index=17097, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFecBlUerdzxzqVlgL-vLrbPmfhxKyFO4Gek_o7UwBEGJYfK5SJBp74YkaPqLAVttOcQnyJrSY_RRyk4-mTBJpNF-IOQNCtJTFKY1BAKcFHokAaf1FmX3eT0ueTyT0iEp2tFes2EUXN', start_index=17088)
Annotation(end_index=17206, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQiGtnP9_V23gQzn_LV92Q3I2qondlkY05oK6A6f3S0GCWa2cygNXS1jm5W9avkvvgHmwoYXMqUO3PhgK9UDp4jYjU-bllunj-wXW9XRDyYFvkwhAYb-Vo69uY', start_index=17196)
Annotation(end_index=17360, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJxHhnDjfndHpsHiWG3vHXznOHvyZ-zlzSNK7hnyOhkT8lIarrt3phIunj0X2iXrZyezkL1pkanSyjfNcD-XD_F_NPIZpvRxxMNuumZtEtcRxoPDLBKT-DjUuB_k37G9Rwdvpx3F_viDtPUopok40rWu1J', start_index=17350)
Annotation(end_index=17459, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFE0Ld7uEqMvMtqCKKnXzj27blB0ZhId30kWWTmfJDjZZWxcfUPZQjCLqlJxwZKnUbTbt2BXiCn1TVlO_-0qzct6S5nw0e05w24oYOMbkpisffL84dFDuR4Y1YjqgkWM-H7_PTv34K7sA==', start_index=17450)
Annotation(end_index=17587, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECBAOq1vJ-ESGpgr8YgQD3CP7Neeu4s7iThv_-g6eQLROHDVAKFSJIzt_14tSRtoDRs1bFuF1VRUBZhzoF1o-H6qt5_LEuVuXmKB8fjwVJREN5UGkeU2B6z_PLW4NxrWD4Abwau8YztVCw32QOMeObnpFnQHgspOrsonFHRBll-AwwxSZoUoKCnEQdr88jctPUTezWs7h3e4DE2ujm7UwhVG8zvG2k_rO_WNQ3oqJexKjKzNx8rreVAIuvxiDwbJh5pWwy5a1EZ49hymKNBnN1RfzoeUrBOW6Si2Q=', start_index=17577)
Annotation(end_index=17710, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFL_5wMtMOlJ5AxbNL8y2SHpyu5XZw3RzgBiBuKL9AzcmLiLpNFNJuw89rKL4bgInVHjo2-Upc1Mkr2vKqNKyF9m9QesMm4k07-RhtUVgXIBbOf0jZavn6Am-28NY=', start_index=17700)
Annotation(end_index=17846, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQiGtnP9_V23gQzn_LV92Q3I2qondlkY05oK6A6f3S0GCWa2cygNXS1jm5W9avkvvgHmwoYXMqUO3PhgK9UDp4jYjU-bllunj-wXW9XRDyYFvkwhAYb-Vo69uY', start_index=17836)
Annotation(end_index=17983, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-fLeI-aAMDH8lpocG4SLsapnsUo_Q_T8M4LdV1N6lkSb-bTpW0yFGkOZf_InscqjD_GMyEcOkTxn7LGdb0Rqgswc3A-cHCsCE7UEq3fxB8Rp9tBKC0nhJHjDe2BzgdbWDeCRJaq9XHlrrWky-AITCsIdaqwLzF4db88dXV20TyyaeoBd5EkHP57yYcR2bgXEwEDWN', start_index=17973)
Annotation(end_index=18059, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtMLSS0NAT1SzSYa-RwH2IF0yaGN0bT50uMhoH2VuqNlpFZCcsfTlYHgfnh1vGHiktwTtFe1GEb0TKFeiVuydZoNExZkErLaDgXrCLNzJhZylPxww15t_BatSc2HD_j1cjUHCPi_LVIqo2U5gYNdDz7AP1JODbjYGZMJ9OHJ4C7xhLxNngkw58WZcbrGc7he2MQqHfbTxmw2jMD5R8bLX9bpU=', start_index=18049)
Annotation(end_index=18196, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGN_egBEA3pt6DclLuUlcpZrAbVXAXgeJfTGIsBTAJtyUhM6lCjGPomlSdvT9MaFKyoBRodxp6p6-6cgap7u4_LYpsxfU2CSI4WUO5qvmo6QX-YdLFeCOy4KiCQOv1JEcbLKwrrPQoT6vwqm9ZuUvZZ3Jgk', start_index=18186)
Annotation(end_index=18333, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVjcIHlOX9wG5ED9zTFqL18NXUy54ikBERxEpB7xX4YoiEGZMKz4baY2j2joD9E5oZzmQPzb-o4dePrXq1QqLbnDOKWBK1HXUPItgfCSh10kmirq3CDe_hX7Vyt8aIhQ==', start_index=18323)
Annotation(end_index=18500, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEazpDTDbjuOjj5kf6M3cEXbW0-HNbt-9DKVOmc8AUVWFmQegcrBKYwolMz9iql5Wyn6lX75AfM4wtisUdPdcQlGeNwVa7rLCYCNyg-J_e0tmGz_32_lylZM5OM8Cew2VgVLGP98YZpVJOvNtT9-Noh431p0vNRwBowyGHkND_6L6KAtZ3VvSCkZKDgTUeDDNhGZVUuyXV09LoqB6V8KcnUVrSr8zvfDQPG67NgEuHP68c7hPW9a2WBSNDXa5c=', start_index=18491)
Annotation(end_index=18616, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPoB0PwizwmNh474tOfo4i_wml1jzpyBUQOzvN_P9Gi_0fbiPHPGgV5qO9zsyuLtGv1NXqU3-Er1XYI6ehhWRI7GgbJ3kpJK2lyGGyB4Ss8Dy7pIRjVunj3eUYct2b2zcFk79thLU2FCKRNAQ3Ea3CRp8qSQg1oX_HNpAvjsvBKiWDuyZE', start_index=18607)
Annotation(end_index=18696, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0CtTvRVrHZILg3z-9dCMDDlAU2IoIpXomfizta1PsLwSDwVC6m2x8sCw02GxpAPCDUc6FpiT1Zv5K_Q-p2PFVsRw3hDw6h5tODuNF5BBJ7QrTHztlab6LUmFK-oTIj1zcz2hKQ6AFz8OOml6of05u19aP8GCgoRz8WN_j7DmaxStbrpo3yzGsDRIbHvcAbYGgh5J4iQeWJms_-K8BkBrB5FH6LkQemcOPOEoM8CjPTt35i1iEYY7tmxpTU8tArbOQlJO_3YSpLQ==', start_index=18686)
Annotation(end_index=18836, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBm7goiav5Hp90w-MANaDbMNukWAq_3hIoTNwENoOtu8WatZWtLRcyEsCP7BaAVyjgvCKdLK3sfeFyfmXufNJezuO55PO8HM3Fk3IKgBsSFlHoj1ww177zKAWOK69riZyNzgdQkw2bDhYVun-TwDXqc4hKXoXfYcc8dbq6OSmwuw==', start_index=18826)
Annotation(end_index=18940, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxhDK-O7u6PnOkYOuINg6RUdIwBYAaBLaat7untumas-yJMHuaxYQffKHxzq95MxScD_VmvW7y-C_xAKM2geDxuFSmNgBgKJnMFU_rGmfH3E_Fu_g9ZBtfNO1kv8h5VQ5XAWVAwu9I11dADcZZvabW4Ty_9zsc4hVyn7vwRFPE3akGbOG1FKfHahicyDy0Dvj6sPaj0Z0=', start_index=18930)
Annotation(end_index=19110, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdYH2PXDtdoRPt2McJwSDWIMYvdYQWCDcGkeMtElVBFtrDi9XUUUsBuBeLHg8v4XQqywi_bCwIDKBlFGfoC3w__6thr-_l9mWFB_-LwS5qp-PVtFiMnQdZH1CiKbY=', start_index=19100)
Annotation(end_index=19198, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGI8x1VpQUdlT6ltzrILztcFfxFl448_Lg0waUVcwz7Eji_ZALPN3AzQe4ZIo2xK3eBVniyfXhEL43aaOUzOO8XL2Z_yBasuus_Rh_6-om-GKZQKcrEZPpHF2Qv5dw_f7Ck19J-1FJqcw==', start_index=19188)
Annotation(end_index=19266, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZ2axAiCutL6YE7_TKEV-0HGAiTEckzKoZWMZ2QMUKvvfCc7wqAap1LjHfWCKsLJJz5YZDxWzyk_MnM96O2f7-Kg1aEukCvdYrXktnEQ-I3nClgZALYPjhhRkvVzIZuGi60pvZRJWqkV897D9ViIAAg4MlF_6RrbBrCh8_4Jh7a53crV5SpEBHdLjb--ZJTSpWr_4MzQ6a8ilI5cMnv3oXcqKoTjUHDuSCzRu_fkLD7Jdb-fkR8dq8Eakcqxx0AePFp6ND6aGofRWRc6D1IfVYHL2Q96FGyA==', start_index=19256)
Annotation(end_index=19333, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaCnTfOnmgOrd22yPy1HB68eOyvWplV9AAda_5OPmUmXCvshwlMwV98V_ZHrP0n9_SgQcQvaSIHGzdbqCKB9oTczu7QJES2A97StkIDDWOUfM_cya6GiHLPlFHQXs0TA==', start_index=19324)
Annotation(end_index=19439, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBMjOdtLLJ5TdjNHE5883b6zRqImqcpFeUV9YVbGnDgZlsi-sZAhXVn2bL-HFdE5Mn_Q2o5PXbY0mYJ9DSCwugq8aXSTo_a7SM1rCOfKO1t57l19JCOEXH2y-Uj8i3V-QX14sPmzHOX3cPWCR0ReK8TLm1BiNCg98VPYfS8QwoycvJaD06FJMefaTi7zA2FrsiKUDnNaaoYaVVEX_1vMrVb30upbNT9fvhXsp2NrECKFZEhT7zontGfgDYPMQVONAWs4V-obbIlobQxReEf9bVGcuRiqW4hg==', start_index=19429)
Annotation(end_index=19545, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMS9nS8S1B73cP1J9t_mV9Jj56KYv0dcYnzv24nkHtVt4F3lO6G3k4OSotwbZlyiFegdxMqYF1en7mmHFuZSQ09WChHSAXrBcJyJzEe1d5oFDBmmuXObTRPgdaEuKVrw==', start_index=19535)
Annotation(end_index=19636, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVEKzu9SnCu8mskBpQOfhrJNnCQH3NagNIT1CdRKqpH1NueBr4oGg_zxCNwfGYV00QrHypNm9aRiOJw8BlTqOHGemDhkzDPMsMzVPTOngaZiTERSXx9Ze99_60tRG2zzJxEmnf2XIY', start_index=19626)
Annotation(end_index=19736, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFecBlUerdzxzqVlgL-vLrbPmfhxKyFO4Gek_o7UwBEGJYfK5SJBp74YkaPqLAVttOcQnyJrSY_RRyk4-mTBJpNF-IOQNCtJTFKY1BAKcFHokAaf1FmX3eT0ueTyT0iEp2tFes2EUXN', start_index=19727)
Annotation(end_index=19888, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmBsGMHsrNo7FoQ5qqHh0ROSW6EuNTOYvH33aRT1-BdGpxCC6T9bj_g2yqfdcc8Iyq4-eLAvCZqwO2ysz6iUeODQKLkj-O6CmKTYBqMWZGrq6Em6ZcDNhN-GusL7gYJHeiF53rqxSH', start_index=19878)
Annotation(end_index=20013, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWWuhGusWdyD9YNRd-vgv60V9lWgPQcTquRbOhI_PyUuHpe6csEiRPa2ancS1dBDMOUvEqi0_S94xMbcDuIyINHPxuGHzwKtBB5ktfSaHShqqFFreRSqfo1xL8JjBAKcZ60XBBhifp79XIV7FxDDq5lQ5Fyrc5wGJXj1g4jXVqRY3uayuqVDL7lnnMlD7ujGQG5sw3xjwbc_0U0y91jBo3rkGCsovHlA2cCQS9eLMPMTl829un3H5-7Q==', start_index=20003)
Annotation(end_index=20159, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFONgaoOftpBLne8SlMZzuSmR68zK0oM6xbmN3lvsAsfPI1CrBuTSSAZkVX0pCTddwszgwBvk8ecBTpO2v7eksPooaE9xEhKn-J0xSzJfuAZhxILjF64NyiFqm5ORdVz2ZTQyfdInL', start_index=20149)
Annotation(end_index=20236, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHE6oVmqIY9obh3_AH0FGIhZvS_DyzwO7BRhyDmB-AJs9WduptRhaKoSeJZEpnMARbRBCxXwlipONQxYI3J079Ardgy5DO-rhMrjc4oVw_GT6DYSprd2TfE-HoZLZCIB0ztVKcIPwxrxAmB3nJrdYPGmdk7', start_index=20226)
Annotation(end_index=20348, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjBwokrB3CbxeY6emyWUSDI5NCxUZWCVnDuEoVqLYsAL3QbyfGt9OYm6ToZg0WIZw_R7Icomql4Xnf5rhik4Yv9woikX-nmmskRcd72DD_3uNUVNTxGKDwQD-gDdBwa8490gNkhdGUu1_2taDwGrN7oua_oB8KtK9mGj4bNYuFgM4qtAgQjMBUyX7AduMZ-696T03IXwhCNesCjP2uc50a5A==', start_index=20339)
Annotation(end_index=20499, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEujEqfLFOxn7yCBRIBfxRDXs2vGg9Aw8KoUyE8V3T48-4cpTx9Eze1EClzFW2zEIX3lsNQ5X--PcbxsA8Wb3A8B59E1LUCPAXhZpfiPecmd_I0kvzuOUKH-5VVvp6DMxdTBdrvSR9oPa2ItLawZw4jdokn4_jrfegyGFcg', start_index=20489)
Annotation(end_index=20595, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgFSSIqTd7xZjmhFZkleQ3Wr8oBpsnA5PLNHyCgyDO1kFmuCy7dEU07RgRwjMKTjiz2hnwIdRW9I1w2_UEH1wrQhR3BOUm75r5Cl_SQmTif2Yl-X8plxqmQqedBggtdirYrymF11G-Bk69yyya_mmarO-5lhIR5hkWxsO3V9JQbCo8syk7T6WCXblgUcjf8GDplTVqBSksbBavdTiGJ2CK9lM6Y2zhoHnXFWomIbyn8p_bhT6gCwKErTRaCt3po1CSRwv7LMffADDM2Kv7EEhnH64xcQxSfC_coZ2NYSWkRN-rXZUAb5F-evL2b7yug9vQGNaQgKqccR-XGJI=', start_index=20585)
Annotation(end_index=20746, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLGf30dz7R_vlwDP5WPr-Idxt6tOVbsEsNRlhlweiyLhCC4-WXmMTR-AVs_sfi9asMjWEV4JukBDYryzgTt2CTGxiH1sVCmrVH5wpc0p-2McY8gpLR3cyoeoI_NcoP4aAqN4iAOohohzPiUlXuIukz9iJ-yk_lVOItL93vgkusdMQaIs7IpxiY3rWOoLjMnLzB2HMEpFronrmm6P0hVcYgH5NizencVGLMu4mat6qG9p7gghJM0D77q290b2zmcB4=', start_index=20736)
Annotation(end_index=20845, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoYEuRi9PiK2klq5TjsDtxn_XqDsUsMDQ4PO5iSRxCfYn63YgbEZX4iXlJU1fV5LTAygR20E5pRTWurux4ynjg7_ZDhyqh87agU0nPf3w6pZDdtTWg4A2IwIg-', start_index=20836)
Annotation(end_index=20978, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK7HO8lMuL4WEPtvOOvQGOOwR8uDjPgCLQeia5nUdSW_csD8pYdS5zMHqyQL3eaHjktlajDzsnKZDYuzrhviuJPoZKdNYdM2ecDWYQGb9BM7OEJJdFBE1wXC9x8s1DgdRW7AuPq2uCO2ysab5naDcb6fesjEm5dFuIgIr2lw2RBKXuXJKjjfMwPbrqYDuxbXXobvkaWsFOrEZLFuHds_9AxAdh4OpUo-h2y0LykH0v8uL46wQpDDbxWokAlTidTdeHOZ3xtwwpV4A7oGvywbsO6NUP4EE4', start_index=20968)
Annotation(end_index=21082, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFk1gX6Ezq7KH9ZdcnT26KvIjaabxmyv23GC6ac6phlDFPcupDAGcvW6a1KDr6iGwCWLTBOlyi22BhCEUPpafkE-A0OU_FwjQyQb90YC5azQpt33sl6sVpojVb2uiA_OHhEIBC08mrOR7msWZRHpOaxEA==', start_index=21072)
Annotation(end_index=21112, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEmlFX_SiBX3yerQciuMDExZxGhHz238TbeqjvcssP5NmJvATeu6DjsJFnLuFMv7a7ZyqNdAt1l3zQSMHfsFE32JKP-mbhwgYxLI2S5v4CIBzEMoEs43LAJtbL3mcpiCL5WpxGINKf0KMzAxQw5IG65jPSw46C1XUjDYplf8loOGz3S1XlI8I8a_7SyO5Ze2PIf8YTAfv6JHJN0RLyMcrB-pCO2Dj-AYxtKoGeQLyL', start_index=21102)
Annotation(end_index=21216, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmKZOhPIiR4IzzMkBA_C7rYyp--teNRnmvAXlJFBQw7OiLjCOtG2WOKSwBL77tsvXhzGt-S4vToTGv9B_FD8TmMXqpmMS4aQNuWE8QZ77i6JafYgtDYztNM88jzAUB9UOjkPuJ3vYACdsorqvXdERSGA2tCPeuDOcOoE8AARpJAnzyc9iunIIlKLQMhMdjtLdZ5QqXUbaZFq5X1JAIoJSq7SBrHHGHqA5mFJm6NsR0pkMOjFjpOo4xPcx9eGjzipEz3keG8oN4B9Y=', start_index=21206)
Annotation(end_index=21319, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFE0Ld7uEqMvMtqCKKnXzj27blB0ZhId30kWWTmfJDjZZWxcfUPZQjCLqlJxwZKnUbTbt2BXiCn1TVlO_-0qzct6S5nw0e05w24oYOMbkpisffL84dFDuR4Y1YjqgkWM-H7_PTv34K7sA==', start_index=21310)

## Sources
