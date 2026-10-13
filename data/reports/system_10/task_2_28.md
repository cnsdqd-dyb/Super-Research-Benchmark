# Deep Research Report: perplexity/sonar-deep-research
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 4f2fec16 | **Time:** 113.10s | **Cost:** $1.15824
--------------------------------------------------------------------------------

# Signal Processing Algorithms for Motion Artifact Suppression in Power-Constrained Wearable Vital Sign Monitors

**Wearable vital sign monitoring systems face a fundamental challenge: motion artifacts generated during daily activities severely corrupt physiological signals, yet the algorithms required to remove these artifacts must operate within stringent power budgets measured in milliwatts. This comprehensive report examines the state-of-the-art signal processing algorithms enabling wearable devices to achieve both high-fidelity artifact suppression and extended battery life through innovative hardware designs, efficient software implementations, and intelligent power management strategies.**

## Understanding the Motion Artifact Problem in Wearable Physiological Monitoring

Motion artifacts represent one of the most significant obstacles to accurate wearable health monitoring, particularly for electrocardiogram (ECG), photoplethysmogram (PPG), and electroencephalogram (EEG) signals.[4] The fundamental difficulty arises from the unpredictable nature of body movements—unlike electromagnetic interference or other stationary noise sources that can be effectively mitigated with conventional filters, motion artifacts exhibit time-frequency characteristics that vary dynamically based on the type, intensity, and direction of physical activity.[1] When patients wearing wearable monitors engage in routine activities such as walking, exercising, or simply adjusting their position, the mechanical deformation of skin, electrode displacement, and shifts in the electrical impedance at the electrode-skin interface generate artifacts that often exceed the amplitude of the underlying physiological signal by a factor of ten or more.[4]

The specific manifestation of motion artifacts depends on the signal modality being monitored and the electrode architecture employed. In wearable ECG systems, motion artifacts appear as low-frequency baseline wander and high-frequency noise that can obscure the QRS complex—the most diagnostically significant feature of the cardiac waveform.[8] For PPG signals acquired through optical sensors, motion artifacts arise from both sensor displacement relative to the tissue and changes in perfusion caused by muscle tension during physical activity, making heart rate estimation particularly challenging during exercise.[4][12] In EEG systems designed for brain-computer interfaces or sleep monitoring, motion artifacts from scalp muscle activity and head movements can easily mask the subtle neural signals of interest, with amplitudes sometimes exceeding the EEG signal by orders of magnitude.[4]

The power constraints inherent to wearable devices create a fundamental tension between accuracy and energy efficiency. Traditional clinical monitoring systems operate with unlimited access to power and can therefore employ computationally intensive signal processing techniques without concern for battery life. Wearable systems, by contrast, must typically operate for eight to twenty-four hours on batteries weighing only a few grams, with each megahertz of processing and each milliwatt of power consumption directly reducing operational lifetime.[8][15][18] This constraint means that even theoretically superior algorithms become practically infeasible if they require sustained high processor utilization or specialized hardware accelerators that consume excessive power.

## Adaptive Filtering Approaches for Motion Artifact Reduction

Adaptive filtering represents one of the most successful and widely-deployed approaches to motion artifact suppression in wearable vital sign monitors, primarily because these algorithms can achieve substantial artifact reduction with relatively modest computational demands.[1][3][5] The fundamental principle underlying adaptive filtering is elegantly simple: if a reference signal correlated with the motion artifact but uncorrelated with the physiological signal of interest can be obtained, an adaptive filter can estimate and subtract the artifact component from the contaminated primary signal.

### Reference Signal Selection and Correlation Requirements

The practical success of adaptive filtering hinges critically on the availability and quality of the reference signal, as the algorithm can only suppress artifact components that exhibit correlation with this reference.[1][3] Multiple reference signal sources have been investigated across different wearable implementations. Accelerometer signals measuring body acceleration represent perhaps the most intuitively appealing reference source, as they directly capture the physical motion generating artifacts.[1][3][9] However, research demonstrates that accelerometer-based adaptation exhibits inconsistent performance depending on the type of motion and electrode configuration—while some studies report substantial noise reduction, others find that motion artifacts resulting from skin deformation that does not significantly displace the electrode remain largely unsuppressed.[1]

More sophisticated reference signal approaches have proven more effective for specific applications. Impedance pneumography signals, which measure respiration-related changes in thoracic impedance, provide excellent correlation with motion artifacts while maintaining minimal correlation with the cardiac components of ECG signals.[1] Through careful filtering and correlation analysis, researchers demonstrated that impedance pneumography reference signals achieve correlation coefficients exceeding 0.6 with motion artifacts under diverse physical activities, enabling substantial artifact reduction without distorting the underlying cardiac waveform.[1] Skin strain measurements obtained through optical sensors integrated into electrode structures represent another promising approach, capturing the mechanical deformation of tissue that directly generates motion artifacts in contact-based biosensors.[3]

### Least Mean Squares and Normalized Variants

The Least Mean Squares (LMS) algorithm and its variants, particularly the Normalized Least Mean Squares (NLMS) algorithm, have become standard implementations for adaptive motion artifact filtering in wearable systems because they offer exceptional computational efficiency while maintaining good convergence properties.[26][29] The NLMS algorithm automatically adapts its step size based on the reference signal power, providing more stable convergence across varying signal amplitudes and motion intensities compared to conventional LMS implementations.[26][29]

Practical implementations of NLMS filtering in wearable ECG and PPG systems demonstrate the algorithm's practical utility. When applied to wrist-based PPG signals during physical exercise—one of the most challenging monitoring scenarios—NLMS adaptive filtering combined with accelerometer reference data achieved mean heart rate errors of approximately 1 bpm, a result substantially superior to unfiltered signals which exhibited errors exceeding 17 bpm during moderate physical activity.[26] The normalized variant proved particularly valuable because the acceleration signals from different body axes and activity types vary dramatically in magnitude; NLMS automatically compensates for these variations without requiring manual tuning of filter parameters for different users or activity contexts.

The computational load of NLMS filtering remains remarkably modest for real-time wearable implementation. With filter lengths typically between 50 and 100 coefficients and sampling rates in the range of 35-100 Hz, modern microcontrollers execute the NLMS algorithm with less than one millisecond of latency, consuming negligible processor cycles relative to other wearable signal processing tasks.[26] This efficiency becomes particularly important in power-constrained environments where extended battery life depends on minimizing processor wake time and clock frequency.

### Recursive Least Squares and Advanced Adaptive Techniques

The Recursive Least Squares (RLS) algorithm offers superior convergence speed and steady-state error compared to LMS variants, though at the cost of increased computational complexity.[1] Research on wearable ECG-impedance pneumography systems demonstrated that RLS adaptive filtering with impedance pneumography reference signals achieved correlation coefficients of 0.88 between denoised and clean ECG signals, representing a substantial improvement from baseline values of 0.71 when motion artifacts contaminate the signal.[1] The mathematical elegance of RLS filtering arises from its direct minimization of mean-squared error through recursive matrix updates, providing optimal filter coefficients in a mean-square sense.

However, the implementation challenges of RLS in power-constrained wearable systems deserve careful consideration. The algorithm requires matrix operations and reciprocal computations that demand substantially more floating-point arithmetic than LMS variants, typically consuming three to five times the processor cycles.[1] For systems operating at minimal clock frequencies to conserve power, this computational overhead can become prohibitive. Consequently, RLS filtering finds practical application primarily in wearable devices with dedicated signal processing hardware, such as those employing specialized analog front-end circuits or digital signal processors designed specifically for biomedical applications.

## Wavelet Transform and Decomposition-Based Artifact Removal

Wavelet-based decomposition methods provide an alternative mathematical framework for motion artifact suppression that operates according to fundamentally different principles than adaptive filtering.[2][13] Rather than attempting to estimate and subtract artifact signals, wavelet approaches decompose the contaminated signal into multiple components at different frequency and time scales, then identify and suppress the components predominantly containing artifact energy while preserving physiologically meaningful information.

### Stationary Wavelet Transform Methods

The Stationary Wavelet Transform (SWT) provides a particularly effective approach for wearable ECG systems because it maintains time alignment throughout the decomposition process—a critical requirement when analyzing dynamic cardiac waveforms where temporal accuracy of milliseconds directly impacts diagnostic accuracy.[2][13] Unlike conventional discrete wavelet transforms that downsample coefficients at each decomposition level, the SWT maintains full resolution by upsampling filter coefficients, preserving the correspondence between time indices in the original and decomposed signals.

The practical implementation of SWT-based motion artifact removal for wearable ECG systems typically proceeds in several stages. First, the algorithm analyzes the wavelet coefficients at multiple decomposition levels to identify the QRS complex—the diagnostic reference feature containing the R-wave peak. Using energy-based QRS detection and temporal constraints recognizing that QRS complexes occur with known timing intervals, the algorithm identifies genuine R-waves versus motion artifact peaks by exploiting the physiological constraint that heart rates remain within physiologically plausible ranges.[2] Once QRS complexes are located, wavelet coefficients corresponding to these regions are preserved, while coefficients in other time periods—particularly those exceeding amplitude thresholds consistent with artifact rather than physiological signals—are attenuated or zeroed.

The performance of SWT-based artifact removal is documented through controlled experiments using artificially superimposed motion artifacts on clean ECG reference signals. When researchers applied SWT methods to ECG signals with superimposed motion artifact from real body movements, correlation coefficients between the processed signals and clean references improved from baseline values of 0.71 to post-processing values of 0.88—a substantial improvement comparable to advanced adaptive filtering approaches.[2][13] Importantly, the SWT method achieved this improvement while introducing minimal distortion to the underlying cardiac waveform morphology, a critical requirement for preserving diagnostic information.

### Empirical Mode Decomposition

Empirical Mode Decomposition (EMD) represents a data-driven alternative to wavelet decomposition that adapts automatically to signal characteristics without requiring specification of wavelet types or decomposition levels.[31][34] The EMD algorithm recursively decomposes signals into Intrinsic Mode Functions (IMFs)—zero-mean oscillatory components representing different time scales inherent to the data itself. By separating motion artifact components (typically appearing in lower-frequency IMFs) from cardiac or respiratory signals (usually occupying intermediate frequency ranges), EMD enables effective artifact identification and suppression.

The advantage of EMD over fixed wavelet bases stems from its data-adaptive nature—the decomposition automatically adjusts to the signal's instantaneous characteristics rather than forcing decomposition into predetermined frequency bands.[31][34] For wearable systems where users engage in diverse activities with varying motion characteristics, this adaptivity provides advantages over fixed-parameter methods. However, EMD's computational demands exceed those of wavelet transforms or adaptive filters, as the algorithm requires identification and interpolation of local extrema at each decomposition level. These operations consume substantially more processor cycles, rendering pure EMD decomposition less suitable for ultra-low-power wearable implementations unless executed on specialized hardware accelerators.[31]

## Independent Component Analysis and Blind Source Separation

Independent Component Analysis (ICA) and related blind source separation techniques operate according to principles fundamentally distinct from adaptive filtering or time-frequency decomposition methods.[5][14][38] Rather than assuming specific characteristics of the artifact or requiring reference signals, ICA assumes that the measured signals represent linear mixtures of underlying independent sources—including physiological signals of interest and artifact components—that can be separated through identification of statistical independence.

### Multi-Channel ICA for PPG and ECG Signals

For PPG systems employing multiple wavelengths of light sources (typically red, infrared, and green LEDs), ICA provides powerful capabilities for artifact suppression by exploiting the fact that cardiac pulsations manifest similarly across all wavelengths while motion artifacts and other interference typically exhibit wavelength-dependent characteristics.[14] The practical implementation typically acquires PPG signals from multiple LEDs simultaneously, applies ICA to decompose these multi-channel measurements into independent components, then identifies which components represent genuine cardiac pulsations through morphological analysis.

This approach achieved documented sensitivity of 82.49% and positive predictive value of 99.83% for artifact detection in PPG signals recorded during running—one of the most challenging monitoring scenarios.[14] The strength of multi-channel ICA emerges from the fact that when using multi-LED systems, the number of independent components equals or exceeds the number of measurement channels, providing sufficient degrees of freedom for effective source separation. However, the practical implementation requirement for multiple measurement channels increases hardware complexity and power consumption relative to single-channel alternatives.

### Redundant Denoising ICA for Improved Performance

Advanced variants of ICA incorporate redundancy and multimodal information to achieve superior performance. The Redundant denoising Independent Component Analysis (Rd-ICA) method, developed specifically for wearable ECG systems, acquires ECG signals simultaneously from both chest and back positions, combines these with triaxial accelerometer data from inertial measurement units, and applies multichannel ICA followed by comparison with a reference ECG model derived from ensemble averaging.[5][17] This approach substantially reduces false positive artifact detection by validating that identified components represent physiologically plausible cardiac signals rather than artifact components mimicking cardiac rhythms.

The Rd-ICA method demonstrated superior performance to conventional wavelet shrinkage and standard ICA approaches when evaluated on experimentally recorded noisy ECG signals.[5][17] The improvement arises from multiple factors: redundant signal acquisition enables validation that identified components appear consistently across channels; integration of motion data from accelerometers helps distinguish between genuine motion artifacts and cardiac signals that might otherwise be confused; and comparison with a reference model derived from the individual's baseline rhythm provides personalization that improves accuracy for diverse users.

## Hardware-Integrated Solutions for Artifact Reduction

While algorithmic approaches to motion artifact suppression receive substantial research attention, hardware-level design choices often prove equally or more important for achieving practical artifact reduction within power constraints.[1][3][7]

### Electrode Architecture and Materials

The design of electrodes and their interfaces with skin fundamentally influences the magnitude and character of motion artifacts generated during body movement.[1][3] Traditional rigid metal electrodes exhibit significant motion artifact vulnerability because mechanical deformation of skin relative to the electrode creates large impedance fluctuations at the electrode-skin interface. Textile-based electrodes, by contrast, demonstrate substantially better mechanical compliance with skin deformation, reducing motion-induced impedance changes by as much as an order of magnitude for certain movement types.[1]

Specialized electrode designs incorporating optical sensors enable particularly effective motion artifact reduction by measuring skin strain directly.[3] These designs integrate tiny optical sensors into ECG electrodes that measure changes in skin stretch during body movement. The skin strain signal provides a nearly ideal reference input for adaptive filtering because it exhibits high correlation with motion artifacts while remaining nearly uncorrelated with genuine cardiac signals. Clinical demonstrations of optical strain-based adaptive filtering achieved average motion artifact reduction of 83-77% depending on the specific movement type, with minimal distortion to the underlying ECG waveform.[3]

### Multi-Modal Sensor Integration

Integrating multiple sensor modalities into wearable systems provides opportunities for artifact detection and mitigation that single-modality approaches cannot achieve.[1][7][10][19][56] A chest patch incorporating simultaneous ECG, impedance pneumography, and photoplethysmography sensors, combined with triaxial accelerometry and acoustic measurement capabilities, enables cross-modal validation that improves artifact detection accuracy and reference signal quality for adaptive processing.[7]

The multi-modal integration approach addresses a fundamental limitation of single-reference adaptive filtering: if the reference signal becomes corrupted by artifacts unrelated to those in the primary signal, filtering performance degrades substantially.[1] By maintaining multiple reference signal sources with different artifact characteristics, wearable systems can automatically select or weight the reference signals based on signal quality metrics, maintaining effective artifact suppression across diverse motion scenarios.

## Deep Learning and Neural Network Approaches

Recent advances in embedded machine learning have enabled deployment of deep neural networks for motion artifact suppression directly on wearable microcontrollers, opening new possibilities for artifact detection and removal that adapt automatically to individual user characteristics and motion patterns.[20][23][25]

### Denoising Autoencoders

Denoising autoencoders trained on synthetic datasets containing simulated motion artifacts and physiological signals demonstrate strong performance for artifact removal in functional near-infrared spectroscopy (fNIRS) data—a modality exhibiting motion artifact challenges similar to wearable ECG and PPG systems.[20] The architecture consists of convolutional layers that learn hierarchical representations of signal patterns, followed by upsampling layers that reconstruct clean signals. The loss function incorporates both reconstruction error terms and explicit penalty terms based on motion artifact detection metrics, ensuring that the network learns to suppress artifacts rather than merely reconstructing averaged approximations.

In comparative evaluations, denoising autoencoders substantially outperformed conventional methods including spline interpolation and wavelet filtering, reducing residual motion artifacts more effectively while requiring less computational time for inference.[20] The neural network approach proved particularly effective at handling multiple overlapping artifacts and complex motion patterns that challenge conventional fixed-parameter algorithms. However, the computational cost of running even relatively small neural networks on microcontrollers remains substantial—inference typically requires multiple millions of operations—limiting deployment to systems with dedicated neural accelerator hardware or higher-end processors.

### Convolutional Neural Networks with Attention Mechanisms

Hybrid approaches combining convolutional neural networks with attention mechanisms have demonstrated exceptional performance for artifact detection and localization in wearable sleep EEG systems.[25] The CNN-CBAM (CNN with Convolutional Block Attention Module) architecture achieved area under receiver operating characteristic curve of 0.88, sensitivity of 0.81, and specificity of 0.86 for artifact classification—performance exceeding standard feature-based approaches and conventional signal processing methods.[25]

The attention mechanism enables the network to automatically identify which features and time intervals most strongly indicate artifact presence, providing interpretability alongside accuracy. This interpretability proves valuable for wearable systems because it enables adaptive parameter adjustment based on detected artifact patterns. For instance, if attention maps consistently indicate that specific frequency bands contain artifact energy, the system can automatically adjust filter parameters to more aggressively suppress those frequencies in subsequent monitoring periods.

### Practical Constraints on Neural Network Deployment

Despite their superior performance, neural network approaches face substantial practical constraints for power-constrained wearable deployment.[28] A trained LSTM network achieving 98.76% classification accuracy on activity recognition from sensor data required 424,100 individual weights and 713 activation functions—computational demands that consumed 6001 binary multiplications and 424 additions per inference.[28] In comparison, simpler recurrent architectures like FIRNN achieved 95.74% accuracy with minimal computational complexity, consuming only 1 binary multiplication and 5 additions per inference.[28]

For wearable systems operating battery-powered microcontrollers at clock frequencies below 100 MHz and requiring real-time processing of multi-channel biosignals, the computational burden of deep neural networks can quickly exhaust available processor cycles or require dedicated hardware acceleration. Consequently, practical wearable implementations typically employ hybrid approaches: computationally efficient conventional algorithms (adaptive filters, wavelet decomposition) handle routine artifact suppression, while selective deployment of neural networks occurs during specific high-artifact scenarios where the improved performance justifies increased power consumption.

## Power Consumption Optimization Strategies

Achieving motion artifact suppression within the severe power constraints of battery-powered wearable systems requires careful system-level optimization strategies that extend beyond individual algorithm selection.

### Adaptive Sampling and Event-Driven Processing

Continuous acquisition and processing of biosignals at fixed sampling rates—a standard approach in clinical monitoring—becomes prohibitively expensive for wearable systems when extrapolated over many hours of operation.[18] Adaptive sampling approaches dynamically adjust acquisition and processing rates based on detected signal characteristics or predicted activity patterns. The Change Point-based Activity Monitoring (CPAM) algorithm, for example, identifies transitions between different activity states through unsupervised statistical analysis of sensor data, then adjusts sampling rates accordingly—dramatically reducing energy consumption while maintaining activity recognition accuracy.[18]

This approach achieved 74.64% energy consumption reduction compared to continuous sampling while retaining activity recognition performance—a substantial efficiency improvement without sacrificing functional capability.[18] The underlying principle exploits the observation that most wearable monitoring scenarios involve extended periods of relatively stable physiological state (sitting, walking at consistent pace, sleeping) punctuated by transitions where sampling rate increases become justifiable. By detecting these transitions automatically and only increasing sampling rates when necessary, wearable systems extend battery life dramatically.

### Compressive Sensing for Data Reduction

Compressive sensing techniques enable reconstruction of full-bandwidth signals from sparse measurements, reducing the data rates that must be transmitted or stored by 70% or greater while maintaining signal fidelity sufficient for diagnosis.[15][18] This approach proves particularly valuable for wearable systems where wireless transmission represents a major power consumer—reducing data rates directly reduces required transmit time and power.

Implementation of digital compressive sensing on a Bluetooth ECG node achieved 77.4% reduction in radio energy consumption through combination of periodic sleep/wake cycles and compression algorithms, reducing overall node energy consumption to 6.53 millijoules per measurement interval—enabling multi-day operation on small coin-cell batteries.[8][15] The compressed data could be reconstructed on a receiving device with minimal information loss, enabling clinical-grade signal analysis despite aggressive reduction in transmitted data volume.

### Selective Signal Processing and Hierarchical Filtering

Rather than applying full-complexity signal processing algorithms to every measurement, hierarchical approaches apply simple, computationally efficient tests first to identify epochs requiring intensive processing.[30] For example, a low-complexity threshold-based test identifies PPG segments that are clearly corrupted by motion artifacts (exhibiting sudden amplitude changes, unusual spectral content, or extreme values), and only segments passing this screening undergo intensive adaptive filtering or ICA-based processing.

This selective processing approach can reduce average computational load by 50-80% depending on the activity context, because most measurement epochs during normal daily activity maintain reasonable signal quality requiring only minimal processing. Only during exercise or activities generating substantial motion artifacts does the full-complexity processing pipeline execute, at which point the improved accuracy justifies the increased power consumption.

### Hardware Acceleration and Specialized Processing Cores

Deploying signal processing operations on hardware accelerators rather than general-purpose processor cores reduces energy consumption per operation by 5-10 fold, as specialized hardware can execute algorithms without the overhead of general-purpose instruction fetching, decoding, and execution.[8][21][58] Wearable systems increasingly incorporate dedicated analog front-end circuits optimized for ECG or PPG acquisition, reducing the dynamic range required from the main analog-to-digital converter and enabling continuous operation at minimal power levels.[8][10]

The integration of FPGA-based coprocessors with MCU cores in hybrid wearable architectures provides another powerful approach to power-efficient signal processing.[58] Signal processing operations like FIR filtering or ICA-based decomposition execute on the FPGA while control logic and higher-level decision making run on the MCU core, achieving overall energy efficiency superior to either architecture alone. This codesign approach balances flexibility (software running on MCU) against energy efficiency (hardware acceleration on FPGA).

## Sensor Fusion and Multimodal Integration

The integration of multiple complementary signal modalities provides opportunities for substantially improved artifact detection and suppression beyond what single-modality approaches can achieve.[19][56][59]

### Lead Switching and Signal Quality Index-Based Selection

When monitoring systems acquire multiple redundant channels (such as multi-lead ECG or multi-wavelength PPG), signal quality indices enable intelligent selection of the highest-quality channel at each instant, automatically avoiding channels corrupted by motion artifacts.[19][59] Rather than attempting to combine all channels into a single estimate, lead-switching approaches identify which individual channel maintains highest signal quality—determined through metrics like signal-to-noise ratio, signal regularity, or correlation with physiological templates—and use only that channel for feature extraction.

This approach proved particularly effective in multi-lead ECG systems where different electrode positions exhibit motion artifacts with different magnitudes and characteristics depending on the user's specific movement pattern.[19][59] By dynamically switching between leads based on estimated signal quality, wearable systems maintained accurate R-peak detection and heart rate measurement across diverse physical activities, with substantially better reliability than fixed-lead approaches.

### Fusion of Redundant ECG Acquisitions

Acquisition of ECG signals from multiple electrode positions (chest and back, for instance) enables detection of inconsistencies that indicate artifact contamination rather than genuine cardiac activity.[5] When motion artifacts corrupt both signals identically, they appear correlated in a way that rarely occurs for genuine cardiac signals that exhibit different amplitudes and sometimes different polarities across electrode positions. By comparing multi-position ECG recordings through techniques like redundant ICA, wearable systems can identify and suppress artifacts affecting specific leads while preserving information from uncorrupted channels.

### PPG and ECG Fusion for Robust Heart Rate Estimation

The combination of PPG and ECG signals through data fusion approaches provides complementary information that substantially improves heart rate estimation robustness during motion-induced artifacts.[56][59] When PPG signals become corrupted by motion, cardiac information remains available from ECG (if the system is configured to acquire ECG). Conversely, when ECG becomes severely corrupted, PPG often retains sufficient signal quality to enable accurate heart rate estimation. Fusion approaches that intelligently weight the contributions of each modality based on estimated signal quality achieve superior overall accuracy compared to relying on either modality alone.

## Recent Practical Implementations and Clinical Validation

The theoretical and algorithmic advances discussed above have now been validated through real-world clinical implementations demonstrating practical feasibility and clinical utility of motion artifact suppression in wearable vital sign monitoring.

### Home-Based Continuous Monitoring Studies

A clinical feasibility study of continuous vital sign monitoring in home settings following hospital discharge demonstrated that wearable systems employing the signal processing techniques described herein achieved valid monitoring time of 59-89% after artifact removal—a substantial improvement from raw signal quality that was often 20-40% due to motion artifacts.[30] The chest patch acquiring ECG and respiratory rate proved most reliable, with higher adherence and artifact removal success rates than wrist-based sensors. Importantly, the continuous monitoring revealed physiological information not apparent from standard spot measurements—oxygen desaturation episodes occurring three to four times more frequently during continuous monitoring compared to spot measurements, and sustained respiratory abnormalities in patients discharged after acute exacerbation of COPD.

### Integration into Commercial Wearable Devices

Commercial wearable platforms now routinely integrate motion artifact suppression into their signal acquisition and processing pipelines. Wrist-worn devices equipped with PPG sensors employ combinations of adaptive filtering with accelerometer reference signals, enabling continuous heart rate monitoring during diverse activities including running and exercise.[9] The practical implementations achieve mean heart rate errors below 2 beats per minute during moderate physical activity—substantially better than uncorrected PPG signals but slightly worse than clinical-grade ECG, reflecting fundamental trade-offs between sensor modality and form factor constraints.

Chest patches incorporating multiple sensors and dedicated signal processing circuits demonstrate even higher performance, achieving correlation coefficients above 0.9 with clinical ECG references even during vigorous exercise.[56] The multi-modal approach combining ECG, phonocardiography (PCG), and PPG enabled extraction of advanced physiological parameters like pre-ejection period and pulse transit time that provide diagnostic information beyond simple heart rate.

## Comparing Algorithm Performance and Trade-offs

Different motion artifact suppression approaches involve fundamental trade-offs between accuracy, computational complexity, power consumption, and robustness across diverse user populations and motion patterns. A comprehensive understanding of these trade-offs guides practical system design.

| Algorithm Approach | Motion Artifact Reduction | Computational Complexity | Power Efficiency | Hardware Requirements | Robustness |
|---|---|---|---|---|---|
| Adaptive LMS Filtering | Moderate (40-70%) | Very Low | Excellent | None | Moderate-Dependent on reference signal quality |
| Normalized LMS | Moderate (50-75%) | Low | Excellent | None | Moderate-Better than standard LMS |
| Recursive Least Squares | High (70-85%) | Moderate | Good | DSP preferred | Moderate-Computationally intensive |
| Stationary Wavelet Transform | Moderate-High (65-80%) | Moderate | Good | General processor | Moderate-Fixed parameters across users |
| Empirical Mode Decomposition | High (75-85%) | High | Fair | General processor | High-Adaptive to signal characteristics |
| Independent Component Analysis | High (75-90%) | High | Fair | General processor | High-Multi-channel dependency |
| Neural Networks (Shallow) | High (80-90%) | Moderate-High | Fair | None or accelerator | High-Learned from training data |
| Neural Networks (Deep) | Very High (85-95%) | Very High | Poor | Accelerator required | Very High-Complex pattern recognition |

The table reveals that moderate artifact reduction techniques like basic adaptive filtering offer the best power efficiency and require minimal hardware, making them suitable for ultra-low-power wearable systems where every milliwatt matters. Higher-performance algorithms like ICA or deep neural networks achieve superior artifact suppression but demand substantially increased computational resources and power, requiring either specialized hardware acceleration or acceptance of reduced battery life. Practical systems typically employ hybrid approaches: computationally efficient algorithms handle routine monitoring, while more intensive processing activates only when motion artifact levels exceed thresholds justifying the increased power consumption.

## Future Directions and Emerging Technologies

The field of motion artifact suppression in wearable vital sign monitors continues to evolve, with several promising directions emerging from recent research.[4][11][58]

### Artificial Intelligence-Driven Adaptive Algorithms

Machine learning approaches that learn individual user characteristics and adapt signal processing parameters to maximize artifact suppression for specific users represent a particularly promising direction. By analyzing motion patterns and resulting artifact characteristics for individual wearers, AI models can predict which reference signals prove most effective, which filter parameters minimize distortion to physiological signals, and which signal modalities maintain best quality under specific activity types. This personalization promises to substantially improve practical performance compared to fixed-parameter algorithms designed for average users.

### Integration with Emerging Wearable Modalities

Next-generation wearable systems will integrate increasingly diverse sensor modalities including wearable ultrasound, thermal imaging, and non-contact sensors like radar-based vital sign monitoring.[36] These emerging modalities exhibit motion artifact characteristics quite different from traditional contact-based sensors, requiring development of novel artifact suppression algorithms specifically adapted to their particular vulnerability profiles. Radar-based systems, for instance, require entirely different approaches to distinguishing cardiac and respiratory signals from body motion.

### Self-Powered Wearable Devices

Energy harvesting technologies that convert body heat, motion, or sweat into electrical power promise to extend wearable device operational lifetime from hours to days or weeks.[57][60] As these harvested power sources become increasingly reliable, algorithm design can become less constrained by power limitations, enabling deployment of more computationally intensive but higher-performance motion artifact suppression techniques. The shift from battery-powered to energy-harvesting powered devices represents a fundamental paradigm change in wearable signal processing optimization.

## Conclusion

Motion artifact suppression within power constraints remains one of the most important and challenging problems in wearable vital sign monitoring. The algorithms and approaches examined in this comprehensive review demonstrate that solutions exist across a spectrum of complexity, power consumption, and artifact suppression performance. Adaptive filtering techniques using carefully selected reference signals achieve moderate artifact reduction with minimal computational overhead, enabling their deployment even on ultra-low-power microcontrollers. More sophisticated approaches including ICA-based source separation and wavelet decomposition achieve superior artifact reduction at the cost of increased computational demands. Deep learning approaches offer highest performance but require either substantial computational resources or specialized hardware acceleration.

Practical wearable systems deployed in real-world clinical and consumer applications achieve the best outcomes through hybrid approaches that combine algorithmic sophistication with hardware optimization and power management strategies. Rather than attempting to apply the most powerful algorithms uniformly to all data, practical systems employ hierarchical processing that applies simple efficient filtering to routine data and reserves intensive signal processing for epochs when motion artifact levels justify the increased power consumption.

The field continues to evolve, with emerging technologies including AI-driven adaptive algorithms, integration of novel sensor modalities, and energy harvesting approaches promising further improvements in both artifact suppression performance and power efficiency. As wearable vital sign monitoring becomes increasingly integrated into mainstream healthcare delivery and consumer fitness tracking, continued refinement of motion artifact suppression techniques that balance accuracy, power consumption, and robustness across diverse users and activity patterns will remain a critical area for research and development.

## Annotations
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Adaptive Motion Artifact Reduction in Wearable ECG Measurements ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9332869/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Motion artefact removals for wearable ECG using stationary wavelet ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5569871/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Reduction of Motion Artifacts In Electrocardiogram Monitoring Using ...', 'url': 'https://array.aami.org/doi/full/10.2345/0899-8205-45.2.155'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Motion Artifact Removal Techniques for Wearable EEG and PPG ...', 'url': 'https://www.frontiersin.org/journals/electronics/articles/10.3389/felec.2021.685513/full'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Motion Artifact Reduction in Electrocardiogram Signals Through a ...', 'url': 'https://medinform.jmir.org/2022/11/e40826/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A new particle filter algorithm filtering motion artifact noise for clean ...', 'url': 'https://pubs.aip.org/aip/rsi/article/95/1/014101/2933008/A-new-particle-filter-algorithm-filtering-motion'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Low Power Wearable Systems for Continuous Monitoring of ... - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5124429/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Smart Wearables in Healthcare: Signal Processing, Device ... - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6198576/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Motion Artifact Removal for PPG Signals based on Accurate ...', 'url': 'https://pubmed.ncbi.nlm.nih.gov/30441021/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Wearable Health Monitor Solutions - Analog Devices', 'url': 'https://www.analog.com/en/solutions/healthcare/vital-signs-measurements/wearable-health-monitor.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Advances in Wearable Sensors for Health Management', 'url': 'https://advanced.onlinelibrary.wiley.com/doi/10.1002/adfm.202518767'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Motion Artifact Removal Techniques for Wearable EEG and PPG ...', 'url': 'https://www.frontiersin.org/journals/electronics/articles/10.3389/felec.2021.685513/full'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Motion artefact removals for wearable ECG using stationary wavelet ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5569871/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Motion Artifact Reduction in Wearable Photoplethysmography ... - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC7085621/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'System‐Level Power Consumption Analysis of the Wearable ...', 'url': 'https://onlinelibrary.wiley.com/doi/10.1155/2018/6564158'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Motion artefact removals for wearable ECG using stationary wavelet ...', 'url': 'https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/htl.2016.0100'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Motion Artifact Reduction in Electrocardiogram Signals Through a ...', 'url': 'https://medinform.jmir.org/2022/11/e40826/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Easing Power Consumption of Wearable Activity Monitoring ... - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6982794/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A Review on Multisensor Data Fusion for Wearable Health Monitoring', 'url': 'https://arxiv.org/html/2412.05895v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Deep learning-based motion artifact removal in functional near ... - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9034734/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'For Efficient Signal Processing in Embedded Systems, Take a DSP ...', 'url': 'https://www.analog.com/en/resources/analog-dialogue/articles/dsp-signal-processing-in-embedded-systems.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Smart Canes Sensor Fusion: Cut False Alarms & Improve Fall ...', 'url': 'https://www.walking-canes.net/blogs/news/sensor-fusion-in-smart-canes-how-combining-accelerometers-gyroscopes-gps-reduces-false-alarms-and-boosts-fall-detection-accuracy'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Real-time motion artifact suppression using convolution neural ...', 'url': 'https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2024.1432138/full'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Signal Processing in Embedded Systems', 'url': 'https://www.embedded.com/signal-processing-in-embedded-systems/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Artifact detection and localization in single-channel mobile EEG for ...', 'url': 'https://arxiv.org/html/2504.08469v2'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Adaptive Frequency Tracking for Robust Heart Rate Estimation ...', 'url': 'https://cinc.org/archives/2015/pdf/0925.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Non-invasive arterial blood pressure measurement and SpO2 ... - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10362790/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Wearable Sensor-Based Human Activity Recognition - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC12299264/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Performance Comparison of Variants of LMS Algorithms for Motion ...', 'url': 'https://biomedres.us/fulltexts/BJSTR.MS.ID.002485.php'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Continuous Monitoring of Vital Signs After Hospital Discharge', 'url': 'https://patientsafetyj.com/article/77776-continuous-monitoring-of-vital-signs-after-hospital-discharge-a-feasibility-study'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The Empirical Mode Decomposition-Decision Tree Method to ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6293644/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Precise detection and localization of R-peaks from ECG signals', 'url': 'https://pubmed.ncbi.nlm.nih.gov/38052596/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Vital signs monitoring with an FMCW MMwave radar sensor', 'url': 'https://essay.utwente.nl/fileshare/file/91720/Berenschot_BA_EEMCS.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Empirical Mode Decomposition - MATLAB - MathWorks', 'url': 'https://www.mathworks.com/discovery/empirical-mode-decomposition.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Heart Rate Variability—Preparing Data for Analysis Using ... - BIOPAC', 'url': 'https://www.biopac.com/heart-rate-variability-preparing-data-for-analysis-2/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Continuous Monitoring of Vital Signs Using Cameras - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9185528/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Difference between IIR and FIR filters: a practical design guide', 'url': 'https://www.advsolned.com/difference-between-iir-and-fir-filters-a-practical-design-guide/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Hybrid algorithm for multi artifact removal from single channel EEG', 'url': 'https://pubmed.ncbi.nlm.nih.gov/33930879/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Real-Time Operating Systems for ARM Cortex-M Microcontrollers', 'url': 'https://faculty.uobasrah.edu.iq/uploads/1631127575.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Design and Implementation of High Performance FIR and IIR Digital ...', 'url': 'https://ijireeice.com/wp-content/uploads/2025/09/IJIREEICE.2025.13907.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A Hybrid Pre-Processing Techniques for Artifacts Removal to ...', 'url': 'https://www.rroij.com/open-access/a-hybrid-preprocessing-techniques-for-artifactsremoval-to-improve-the-performance-ofelectroencephalogram-eeg-features-extraction.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Stm32 FreeRTOS real time task management essentials guide', 'url': 'https://bugprove.com/stm32-freertos/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Optimal Signal Quality Index for Photoplethysmogram Signals - PMC', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5597264/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Wearable Motion Sensors for Athlete Performance Monitoring', 'url': 'https://www.221e.com/fitness-and-sport-science'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Noise-aware Dictionary-Learning-Based Sparse Representation ...', 'url': 'https://pubmed.ncbi.nlm.nih.gov/28529758/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Detection and Monitoring of Viral Infections via Wearable Devices ...', 'url': 'https://www.annualreviews.org/content/journals/10.1146/annurev-bioeng-103020-040136?crawler=true'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Fusing Wearable Biosensors with Artificial Intelligence for Mental ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC12025234/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Sparse dictionary learning - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Sparse_dictionary_learning'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Principal component analysis of photoplethysmography signals for ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9669422/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'What is Bluetooth Low Energy (BLE) and How Does It Work? - AB&R', 'url': 'https://abr.com/what-is-bluetooth-low-energy/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'An Adaptive Filter for Suppression of Cardiac and Respiratory Noise ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC1716734/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Signal and Noise Classification in Bio-Signals via unsupervised ...', 'url': 'https://arxiv.org/html/2512.07851v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Bluetooth Low Energy - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Bluetooth_Low_Energy'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Motion and Noise Artifact Detection', 'url': 'https://biosignal.uconn.edu/wp-content/uploads/sites/2503/2018/09/11_Chong_2014_AnnalsBME.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Implementing Digital Signal Processing (DSP) Pipelines ... - Promwad', 'url': 'https://promwad.com/news/dsp-pipelines-on-embedded-platforms'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A Multimodal System for Comprehensive Cardiovascular Monitoring ...', 'url': 'https://pubmed.ncbi.nlm.nih.gov/41228931/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Advances in Energy Harvesting Technologies for Wearable Devices', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11279352/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A Codesign Framework for the Development of Next Generation ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC12610069/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A Review on Multisensor Data Fusion for Wearable Health Monitoring', 'url': 'https://arxiv.org/html/2412.05895v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Self-charging Wearable Technology! - INVIZA® Health', 'url': 'https://inviza.com/technology'}}

## Sources
https://pmc.ncbi.nlm.nih.gov/articles/PMC9332869/
https://pmc.ncbi.nlm.nih.gov/articles/PMC5569871/
https://array.aami.org/doi/full/10.2345/0899-8205-45.2.155
https://www.frontiersin.org/journals/electronics/articles/10.3389/felec.2021.685513/full
https://medinform.jmir.org/2022/11/e40826/
https://pubs.aip.org/aip/rsi/article/95/1/014101/2933008/A-new-particle-filter-algorithm-filtering-motion
https://pmc.ncbi.nlm.nih.gov/articles/PMC5124429/
https://pmc.ncbi.nlm.nih.gov/articles/PMC6198576/
https://pubmed.ncbi.nlm.nih.gov/30441021/
https://www.analog.com/en/solutions/healthcare/vital-signs-measurements/wearable-health-monitor.html
https://advanced.onlinelibrary.wiley.com/doi/10.1002/adfm.202518767
https://www.frontiersin.org/journals/electronics/articles/10.3389/felec.2021.685513/full
https://pmc.ncbi.nlm.nih.gov/articles/PMC5569871/
https://pmc.ncbi.nlm.nih.gov/articles/PMC7085621/
https://onlinelibrary.wiley.com/doi/10.1155/2018/6564158
https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/htl.2016.0100
https://medinform.jmir.org/2022/11/e40826/
https://pmc.ncbi.nlm.nih.gov/articles/PMC6982794/
https://arxiv.org/html/2412.05895v1
https://pmc.ncbi.nlm.nih.gov/articles/PMC9034734/
https://www.analog.com/en/resources/analog-dialogue/articles/dsp-signal-processing-in-embedded-systems.html
https://www.walking-canes.net/blogs/news/sensor-fusion-in-smart-canes-how-combining-accelerometers-gyroscopes-gps-reduces-false-alarms-and-boosts-fall-detection-accuracy
https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2024.1432138/full
https://www.embedded.com/signal-processing-in-embedded-systems/
https://arxiv.org/html/2504.08469v2
https://cinc.org/archives/2015/pdf/0925.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC10362790/
https://pmc.ncbi.nlm.nih.gov/articles/PMC12299264/
https://biomedres.us/fulltexts/BJSTR.MS.ID.002485.php
https://patientsafetyj.com/article/77776-continuous-monitoring-of-vital-signs-after-hospital-discharge-a-feasibility-study
https://pmc.ncbi.nlm.nih.gov/articles/PMC6293644/
https://pubmed.ncbi.nlm.nih.gov/38052596/
https://essay.utwente.nl/fileshare/file/91720/Berenschot_BA_EEMCS.pdf
https://www.mathworks.com/discovery/empirical-mode-decomposition.html
https://www.biopac.com/heart-rate-variability-preparing-data-for-analysis-2/
https://pmc.ncbi.nlm.nih.gov/articles/PMC9185528/
https://www.advsolned.com/difference-between-iir-and-fir-filters-a-practical-design-guide/
https://pubmed.ncbi.nlm.nih.gov/33930879/
https://faculty.uobasrah.edu.iq/uploads/1631127575.pdf
https://ijireeice.com/wp-content/uploads/2025/09/IJIREEICE.2025.13907.pdf
https://www.rroij.com/open-access/a-hybrid-preprocessing-techniques-for-artifactsremoval-to-improve-the-performance-ofelectroencephalogram-eeg-features-extraction.pdf
https://bugprove.com/stm32-freertos/
https://pmc.ncbi.nlm.nih.gov/articles/PMC5597264/
https://www.221e.com/fitness-and-sport-science
https://pubmed.ncbi.nlm.nih.gov/28529758/
https://www.annualreviews.org/content/journals/10.1146/annurev-bioeng-103020-040136?crawler=true
https://pmc.ncbi.nlm.nih.gov/articles/PMC12025234/
https://en.wikipedia.org/wiki/Sparse_dictionary_learning
https://pmc.ncbi.nlm.nih.gov/articles/PMC9669422/
https://abr.com/what-is-bluetooth-low-energy/
https://pmc.ncbi.nlm.nih.gov/articles/PMC1716734/
https://arxiv.org/html/2512.07851v1
https://en.wikipedia.org/wiki/Bluetooth_Low_Energy
https://biosignal.uconn.edu/wp-content/uploads/sites/2503/2018/09/11_Chong_2014_AnnalsBME.pdf
https://promwad.com/news/dsp-pipelines-on-embedded-platforms
https://pubmed.ncbi.nlm.nih.gov/41228931/
https://pmc.ncbi.nlm.nih.gov/articles/PMC11279352/
https://pmc.ncbi.nlm.nih.gov/articles/PMC12610069/
https://arxiv.org/html/2412.05895v1
https://inviza.com/technology