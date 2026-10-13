# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 5bdad63b | **Time:** 175.02s | **Cost:** $0.12458
--------------------------------------------------------------------------------

# How Sentinel Surveillance Systems Optimize the Trade-Off Between Early Warning Sensitivity and Resource Consumption Using ILI Reporting Thresholds and Epidemic Prediction

## Executive Summary

Sentinel surveillance systems represent a critical component of modern public health infrastructure, serving as the frontline defense against infectious disease outbreaks. These systems face an inherent tension between two competing objectives: maximizing sensitivity to detect emerging threats at the earliest possible moment while simultaneously managing finite resources efficiently. The optimization of this trade-off has become increasingly sophisticated, leveraging advances in statistical modeling, machine learning, and dynamic threshold adaptation. This report examines how influenza-like illness (ILI) reporting thresholds and epidemic prediction methodologies enable sentinel surveillance systems to achieve this balance, drawing upon contemporary research in epidemiological surveillance, artificial intelligence applications, and operational guidelines from international health organizations.

The analysis reveals that modern sentinel surveillance systems employ multi-layered approaches combining static baseline thresholds with dynamic adaptive mechanisms, statistical time series methods, and machine learning algorithms to optimize detection performance. Participatory surveillance systems have demonstrated particular value in extending coverage beyond healthcare-seeking populations while maintaining cost-effectiveness. The integration of artificial intelligence, particularly deep learning models and adaptive threshold methods, offers promising advances in early warning capability, though implementation requires careful consideration of local context, data quality, and resource constraints.

---

## 1. Introduction

### 1.1 The Fundamental Challenge in Sentinel Surveillance

Sentinel surveillance systems occupy a unique position within the broader landscape of infectious disease monitoring. Unlike comprehensive population-based surveillance, which attempts to capture all cases within a defined population, sentinel surveillance relies on strategically selected reporting sites to provide timely and representative data on disease trends [1]. This approach offers significant advantages in terms of data quality and resource efficiency but introduces inherent limitations in sensitivity and representativeness.

The central challenge facing sentinel surveillance systems lies in what might be termed the "sensitivity-efficiency paradox." Increasing sensitivity—defined as the system's ability to detect true outbreaks promptly—typically requires lower reporting thresholds, more intensive monitoring, and broader case definitions. However, these adjustments generate higher volumes of data, increase false positive rates, and demand greater resource investment in data collection, analysis, and response coordination. Conversely, optimizing for resource efficiency often necessitates higher thresholds and more conservative case definitions, potentially delaying the detection of emerging outbreaks [2].

This trade-off becomes particularly acute in the context of influenza-like illness surveillance, where the boundary between seasonal epidemic activity and potential pandemic emergence requires careful judgment. ILI syndromes encompass a broad range of respiratory pathogens, and seasonal influenza epidemics occur annually with varying intensity. The challenge lies in distinguishing the early signals of a significant epidemic from normal seasonal variation while avoiding the resource burden of responding to routine fluctuations [3].

### 1.2 The Role of ILI Reporting Thresholds

Influenza-like illness reporting thresholds serve as the primary mechanism through which sentinel surveillance systems balance sensitivity against resource consumption. These thresholds define the criteria for what constitutes "elevated" activity warranting investigation, alert, or response. The selection of appropriate thresholds involves complex considerations of epidemiological context, healthcare-seeking behavior, laboratory confirmation capacity, and public health response capability [4].

Traditional approaches to threshold setting relied heavily on historical baselines derived from multi-year surveillance data. These static thresholds offered simplicity and consistency but suffered from significant limitations, particularly in the face of changing population immunity, viral evolution, and healthcare-seeking patterns. The recognition of these limitations has driven the development of more sophisticated threshold methodologies that incorporate dynamic adaptation, real-time data streams, and predictive modeling [5].

The World Health Organization's Global Epidemiological Surveillance Standards for Influenza, developed following the 2009 H1N1 pandemic, established foundational guidance for ILI surveillance while acknowledging the need for flexibility in implementation across diverse settings [1]. Subsequent advances in computational epidemiology and machine learning have expanded the toolkit available for threshold optimization, enabling more nuanced approaches to the sensitivity-efficiency trade-off.

---

## 2. Theoretical Framework for Threshold Optimization

### 2.1 Understanding the Sensitivity-Resource Trade-off

The optimization of sentinel surveillance performance can be conceptualized through the lens of signal detection theory, where the system must distinguish between "signal" (true outbreak emergence) and "noise" (routine epidemiological variation). This framework yields four possible outcomes: true positives (correctly detected outbreaks), true negatives (correctly identified absence of outbreak), false positives (erroneous outbreak alerts), and false negatives (missed outbreaks) [6].

The relationship between these outcomes and resource consumption follows predictable patterns. Lowering reporting thresholds increases sensitivity (reducing false negatives) but simultaneously increases false positive rates, generating additional demands on investigation and response resources. Raising thresholds reduces false positives but may delay outbreak detection, potentially allowing wider transmission before intervention [7].

Mathematically, this relationship can be expressed through the receiver operating characteristic (ROC) framework, where system performance is characterized by the trade-off between sensitivity (true positive rate) and specificity (true negative rate). The optimal operating point depends on the relative costs of false positives versus false negatives, which vary according to disease characteristics, outbreak severity potential, and available response resources [8].

### 2.2 Baseline and Threshold Concepts in ILI Surveillance

Two fundamental concepts underpin ILI surveillance threshold optimization: baselines and thresholds. While these terms are often used interchangeably in practice, they serve distinct functions in surveillance systems [4].

Baselines represent the expected level of disease activity in the absence of an outbreak, accounting for seasonal patterns, secular trends, and random variation. Establishing accurate baselines requires historical data spanning multiple years to capture typical seasonal patterns and year-to-year variability. The baseline serves as the reference point against which current observations are compared [9].

Thresholds represent the level of activity above which surveillance systems generate alerts or initiate responses. Thresholds may be defined in absolute terms (e.g., ILI consultation rate per 1,000 population) or relative terms (e.g., percentage increase above baseline). The threshold selection determines the system's sensitivity-specificity balance [4].

The relationship between baselines and thresholds can be expressed mathematically. Let $B_t$ represent the baseline ILI rate at time $t$, and let $T$ represent the threshold value. An alert is generated when the observed ILI rate $O_t$ satisfies $O_t > B_t + T$ or, equivalently, when the ratio $O_t / B_t$ exceeds a defined value. The threshold $T$ thus controls the trade-off between sensitivity and positive predictive value [10].

### 2.3 Dynamic Versus Static Threshold Approaches

The distinction between static and dynamic threshold approaches represents a fundamental divide in surveillance methodology, with significant implications for the sensitivity-resource trade-off [11].

Static thresholds maintain fixed values over time, typically derived from historical data analysis. These thresholds offer simplicity in implementation and interpretation, requiring minimal ongoing adjustment. However, static thresholds fail to adapt to changing conditions, potentially generating false positives during periods of elevated baseline activity or missing outbreaks during periods of suppressed activity [12].

Dynamic thresholds, in contrast, adapt continuously based on recent observations. These approaches use rolling averages, exponential smoothing, or machine learning algorithms to establish expected values and detect deviations. Dynamic thresholds can account for seasonal patterns, day-of-week effects, and gradual trend changes that would trigger false alerts under static approaches [11].

The advantages of dynamic thresholds extend beyond improved accuracy to operational efficiency. By reducing false positive rates, dynamic approaches decrease the resource burden associated with investigating spurious alerts while maintaining or improving sensitivity to true outbreaks. Research in IT monitoring domains has demonstrated that dynamic thresholds can reduce alert fatigue and enable more proactive issue detection [12].

---

## 3. ILI Reporting Thresholds: Methods and Implementation

### 3.1 Traditional Threshold Methodologies

Traditional ILI threshold methodologies rely primarily on historical data analysis to establish expected activity levels. The Moving Epidemic Method (MEM), as implemented in various national surveillance systems, represents a statistically sophisticated approach that accounts for the epidemic curve shape rather than simply using mean values [13].

The MEM approach involves several key steps. First, historical ILI data are aligned by epidemic week, identifying the week of peak activity for each season. Second, pre-epidemic, epidemic, and post-epidemic periods are distinguished based on statistical criteria. Third, threshold values are calculated based on the distribution of activity levels during defined periods, typically using percentiles of historical data [13].

Research evaluating the MEM methodology in the Moroccan influenza surveillance system found it to be more statistically sophisticated than simpler WHO manual approaches, potentially enabling better detection of seasonal epidemic onset [13]. However, the authors noted that the WHO manual methodology offers advantages in simplicity and ease of adoption, highlighting the ongoing tension between methodological sophistication and practical implementation.

The WHO-recommended threshold methodology involves calculating average epidemic curve values and using these to define seasonal thresholds. In some implementations, composite parameters combining ILI rates with laboratory positivity rates provide more accurate threshold estimation [4]. This approach recognizes that ILI surveillance captures respiratory illness from multiple etiologies, and the proportion of specimens testing positive for influenza provides additional signal specificity.

### 3.2 Adaptive and Dynamic Threshold Approaches

Adaptive threshold methods represent the evolution beyond static approaches, incorporating real-time data and automated adjustment mechanisms. These methods address the fundamental limitation of static thresholds: their inability to account for changing baseline conditions [11].

Auto-adaptive thresholds, as implemented in contemporary monitoring systems, establish reference values that change over time based on observed data patterns. The Dynatrace platform, for example, calculates independent auto-adaptive thresholds for each monitored entity, enabling detection of anomalies relative to entity-specific baselines rather than global thresholds [11]. This approach recognizes that different populations, healthcare facilities, or geographic regions may exhibit different baseline activity patterns.

The application of adaptive thresholds to ILI surveillance involves several technical considerations. First, the adaptation speed must balance responsiveness to genuine changes against stability during transient fluctuations. Second, the threshold must account for known patterns including seasonal variation, day-of-week effects, and holiday periods. Third, the system must handle missing data and reporting delays gracefully [14].

Research by Zhang et al. compared adaptive dynamic threshold methods (ADTM) against machine learning approaches for respiratory infectious disease early warning, finding that both approaches offer advantages depending on the specific context and data characteristics [14]. This finding suggests that hybrid approaches combining threshold-based rules with machine learning may optimize the sensitivity-resource trade-off more effectively than either approach alone.

### 3.3 Participatory Surveillance and Threshold Optimization

Participatory surveillance systems represent a distinctive approach to ILI monitoring that engages the general population in symptom reporting. Systems such as Influenzanet and Flu Near You have demonstrated the ability to detect influenza activity earlier than traditional sentinel systems while extending coverage to populations that do not seek medical care [1].

The advantages of participatory surveillance for threshold optimization are multifaceted. First, the large sample sizes achievable through crowdsourced reporting provide statistical power that enables more precise threshold setting. Second, the inclusion of individuals who do not seek medical care captures transmission dynamics invisible to facility-based surveillance. Third, the consistency of data collection across geographic areas enables standardized threshold application [1].

Research validating participatory surveillance against traditional sentinel doctor reporting has demonstrated consistency in detected timing and relative intensities of influenza epidemics [1]. Furthermore, participatory systems have proven capable of estimating age-specific influenza attack rates and vaccine effectiveness, demonstrating data quality sufficient for sophisticated epidemiological analysis.

The threshold optimization challenge in participatory surveillance involves balancing the high sensitivity of community-based reporting against the lower specificity inherent in symptom-based case definitions. The baseline prevalence of ILI in the general population generates substantial background noise that must be distinguished from epidemic signals [15]. Wearable device strategies, which provide continuous monitoring and automated alert generation, offer potential improvements in this regard by incorporating physiological indicators beyond self-reported symptoms [15].

---

## 4. Epidemic Prediction and Early Warning Systems

### 4.1 Statistical and Mathematical Time Series Methods

Time series analysis provides the statistical foundation for epidemic prediction in sentinel surveillance systems. These methods analyze historical patterns to establish expected values and detect deviations signaling potential outbreaks [16].

Classical time series methods include autoregressive integrated moving average (ARIMA) models, exponential smoothing techniques, and regression-based approaches. The Holt-Winters algorithm, an exponential smoothing method that accounts for trend and seasonality, has demonstrated strong performance in outbreak detection when baseline frequency and dispersion parameters fall within specific ranges [16].

The EARS (Early Aberration Reporting System) C3 method represents a specialized approach designed for public health surveillance. This algorithm compares observed counts against expected values derived from recent historical data, generating alerts when observations exceed defined thresholds. Comparative studies have found the EARS C3 method superior to alternative algorithms in certain surveillance contexts, though performance depends on data characteristics including trend patterns and baseline infection levels [16].

The selection of appropriate time series methods involves trade-offs between model complexity and interpretability, adaptation speed and stability, and computational requirements. Simpler methods offer transparency and ease of implementation but may fail to capture complex temporal patterns. More sophisticated methods can improve prediction accuracy but require greater technical expertise and computational resources [16].

### 4.2 Machine Learning Approaches to Epidemic Prediction

Machine learning algorithms have increasingly been applied to infectious disease surveillance, offering capabilities for pattern recognition, classification, and prediction that extend beyond traditional statistical methods [17].

Support Vector Machines (SVM), Random Forest, Decision Tree, and Naive Bayes classifiers have been applied to outbreak detection using diverse data sources including social media keywords, search query data, and traditional surveillance reports. Research evaluating these methods for H1N1 detection in India found SVM to perform best in classification tasks, enabling early warning system development that detected epidemic spikes before official surveillance systems [16].

Deep learning models, including custom attention-based networks, have demonstrated strong early warning performance for influenza surveillance using ILI data [17]. These models can capture complex non-linear relationships in high-dimensional data that may be missed by traditional statistical approaches. However, deep learning methods require substantial training data and computational resources, potentially limiting applicability in resource-constrained settings.

The integration of machine learning with traditional surveillance data represents a promising direction. Traditional epidemiological data from official health notifications, ILI reports, hospital records, and laboratory information systems provide essential training and validation data for AI models [17]. The combination of structured surveillance data with alternative data sources such as search queries, social media, and mobility data can enhance early warning capability while maintaining the representativeness of traditional systems.

### 4.3 AI-Driven Early Warning Systems

Artificial intelligence applications in infectious disease early warning have expanded significantly, encompassing prediction, anomaly detection, and decision support functions. Google Flu Trends represented an early high-profile attempt to predict influenza activity using search query data, demonstrating both the potential and limitations of AI-driven surveillance [17].

Contemporary AI-driven early warning systems incorporate multiple data streams and analytical techniques. EPIWEEK, for example, includes components for predicting flu season severity using ensemble methods that combine multiple model outputs [17]. These systems aim to provide actionable predictions at time scales useful for public health intervention.

The application of AI to address resource constraints represents a particularly important development. In low-income countries where human resources for traditional surveillance are limited, AI can automate processes and offer cost-effective solutions [17]. Edge AI technologies enable local analysis where centralized infrastructure is unavailable, potentially extending advanced surveillance capabilities to underserved areas.

However, the effectiveness of AI-driven early warning systems varies significantly between high-resource and low-resource settings [17]. This variation reflects differences in data quality, infrastructure availability, and technical capacity. Successful implementation requires adaptation to local contexts rather than simple technology transfer.

---

## 5. Optimizing the Trade-off: Integrated Approaches

### 5.1 Multi-Layered Surveillance Architectures

The optimization of sensitivity and resource consumption in sentinel surveillance increasingly relies on multi-layered architectures that combine different threshold approaches and prediction methods. These architectures recognize that no single method optimizes all aspects of the sensitivity-resource trade-off across all contexts [18].

A typical multi-layered architecture might include first-level screening using simple static thresholds to identify potential signals, second-level analysis using dynamic thresholds to filter false positives, and third-level investigation using machine learning models to prioritize alerts and predict outbreak characteristics. This layered approach concentrates resources on the most promising signals while maintaining broad coverage [18].

The Moving Epidemic Method and similar sophisticated threshold approaches can serve as intermediate layers, providing more accurate baseline estimation than simple static methods while requiring less computational resources than full machine learning systems [13]. The integration of virological data into composite parameters, as recommended by WHO, can increase threshold estimation accuracy while maintaining interpretability [4].

### 5.2 Cost-Effectiveness Considerations

The optimization of sentinel surveillance must account for cost-effectiveness, recognizing that resources available for surveillance are finite and must be allocated across competing priorities. Research on surveillance strategies has emphasized the importance of combining lower-cost technologies for initial screening with higher-cost technologies for confirmation [15].

The RAND Corporation analysis of surveillance strategies provides a framework for evaluating detection performance against system costs [15]. This analysis assessed surveillance strategies combining traditional and novel detection technologies, measuring performance through the proportion of population infected at detection time and the time from emergence to detection. Such frameworks enable quantitative comparison of alternative approaches to the sensitivity-resource trade-off.

Cost-effectiveness optimization involves identifying the point where additional sensitivity yields diminishing returns relative to resource investment. This optimal point depends on disease characteristics (transmissibility, severity, intervention options), population factors (size, density, vulnerability), and available resources [15]. Dynamic approaches that adjust sensitivity based on current conditions can achieve better cost-effectiveness than fixed approaches by intensifying monitoring during high-risk periods while conserving resources during low-risk periods.

### 5.3 Balancing Sensitivity and Specificity in Practice

The practical implementation of threshold optimization requires balancing theoretical considerations with operational realities. Research on syndromic surveillance effectiveness has documented the challenges of achieving both high sensitivity and high specificity simultaneously [6].

Studies evaluating ILI surveillance systems have reported varying performance characteristics. Research in Spain achieved 70% sensitivity and 89% specificity with optimized algorithm settings for syndromic surveillance [6]. Studies in Ghana reported lower positive predictive values, ranging from 4.7% to 14.8% for ILI surveillance in the Greater Accra region [6]. These findings highlight the importance of local validation and adaptation rather than assuming universal threshold values.

The relationship between sensitivity and specificity can be visualized through ROC curves, with the optimal operating point determined by the relative costs of false positives versus false negatives. For severe diseases with pandemic potential, the cost of false negatives may be very high, justifying lower thresholds and higher false positive rates. For routine seasonal surveillance, the balance may favor higher specificity to conserve resources [8].

---

## 6. Emerging Technologies and Future Directions

### 6.1 Integration of Wearable Devices and IoT

Wearable devices and Internet of Things (IoT) technologies offer new opportunities for sentinel surveillance that may fundamentally alter the sensitivity-resource trade-off. Continuous physiological monitoring can provide earlier detection of infection than symptom-based reporting, potentially before individuals seek healthcare [15].

The wearable strategy analyzed in surveillance research assumes population-wide wearable deployment providing daily status updates [15]. Individuals receive alerts based on physiological indicators suggesting ongoing illness, including ILI. The system must distinguish true infection signals from baseline illness prevalence and false positive rates inherent in wearable sensors.

The integration of wearable data with traditional surveillance creates hybrid systems that combine the breadth of population-level monitoring with the depth of clinical surveillance. Edge AI technologies enable local analysis where centralized infrastructure is unavailable, potentially extending advanced surveillance capabilities to resource-constrained settings [17].

### 6.2 One Health Approaches and Multi-Source Integration

The One Health approach, which integrates data across human, animal, and environmental domains, provides a more comprehensive framework for infectious disease surveillance [18]. This approach recognizes that many emerging infectious diseases have zoonotic origins, and early signals may appear in animal populations before human transmission.

Multi-source data integration encompasses clinical triage data, wastewater virus concentrations, digital search trends, and environmental indicators [18]. The combination of diverse data sources can improve early warning capability while distributing the resource burden across multiple monitoring streams. However, effective integration requires sophisticated analytical tools to interpret diverse data types and identify coherent signals amid noise.

The selection of warning thresholds and categorization of warning models becomes more complex in multi-source systems [18]. Threshold values must be calibrated for each data stream, and the combination of signals from multiple sources requires careful weighting and fusion algorithms. Research on intelligent, multi-source data-driven monitoring systems continues to advance these capabilities.

### 6.3 Capacity Building and Localized Systems

The effectiveness of advanced surveillance technologies depends critically on capacity building at multiple levels [19]. Technical skills in risk analysis, data interpretation, and forecasting using advanced technologies such as AI, GIS, and remote sensing are essential for effective implementation.

Localized data collection and analysis ensure that surveillance systems are context-specific and relevant to local conditions [19]. The integration of indigenous and local knowledge with modern scientific surveillance can enhance community trust and improve data quality. Regular community-based training, simulation exercises, and localized training materials support better preparedness and timely responses.

The development of localized surveillance capacity addresses a fundamental limitation of centralized approaches: the gap between global surveillance systems and local implementation realities. Effective threshold optimization requires understanding of local healthcare-seeking behavior, population characteristics, and epidemiological context that may not be captured by globally standardized approaches.

---

## 7. Conclusions and Recommendations

### 7.1 Key Findings

This analysis has examined how sentinel surveillance systems optimize the trade-off between early warning sensitivity and resource consumption through ILI reporting thresholds and epidemic prediction methodologies. Several key findings emerge from this examination.

First, the optimization of the sensitivity-resource trade-off requires sophisticated approaches that go beyond simple static thresholds. Dynamic and adaptive threshold methods offer significant advantages in reducing false positive rates while maintaining sensitivity to true outbreaks. These approaches automatically adjust to changing baseline conditions, reducing the operational burden of manual threshold tuning [11][12].

Second, participatory surveillance systems provide valuable extensions to traditional facility-based sentinel surveillance, offering earlier detection capability, broader population coverage, and cost-effective scalability [1]. The integration of community-based reporting with clinical surveillance creates more robust systems than either approach alone.

Third, machine learning and AI-driven approaches offer powerful capabilities for pattern recognition and prediction that extend beyond traditional statistical methods [16][17]. However, these methods require substantial data and technical capacity, and their effectiveness varies across settings. Hybrid approaches combining threshold-based rules with machine learning may optimize performance across diverse contexts.

Fourth, threshold optimization must account for local context, including healthcare-seeking behavior, population characteristics, and available resources [6][19]. Universal threshold values are unlikely to perform optimally across all settings, and local validation and adaptation are essential.

### 7.2 Recommendations for Practice

Based on this analysis, several recommendations can be offered for practitioners implementing or optimizing sentinel surveillance systems.

Organizations should implement dynamic threshold approaches that adapt to real-time data rather than relying solely on static historical thresholds. The initial investment in implementing adaptive systems yields returns through reduced false positive rates and improved early warning capability [11][12].

Surveillance systems should incorporate multiple data streams and analytical methods in layered architectures. The combination of traditional statistical methods, machine learning approaches, and alternative data sources can achieve better optimization than any single method alone [18].

Capacity building in advanced analytical methods, including AI and machine learning applications, should be prioritized to enable effective use of emerging technologies [17][19]. However, capacity building should be balanced with maintenance of core epidemiological skills and local knowledge integration.

Local validation of threshold settings should be conducted regularly, recognizing that optimal thresholds may change over time as populations, pathogens, and healthcare systems evolve [6]. Surveillance systems should incorporate mechanisms for ongoing threshold calibration rather than treating threshold values as fixed parameters.

### 7.3 Future Research Directions

Several areas warrant further research to advance the optimization of sentinel surveillance systems.

Comparative evaluation of threshold methodologies across diverse settings would provide valuable guidance for method selection. Current research has evaluated methods in specific contexts, but systematic comparison across geographic, demographic, and epidemiological contexts remains limited [13][14].

The integration of novel data sources, including wearable devices, social media, and environmental monitoring, with traditional surveillance requires continued methodological development. Questions of data quality, privacy, and representativeness must be addressed to realize the potential of these sources [15][18].

The application of AI methods in resource-constrained settings deserves particular attention. While AI offers significant potential for extending surveillance capability where human resources are limited, effective implementation requires adaptation to local conditions and capacity building [17].

Finally, the evaluation of surveillance system performance in terms of public health outcomes rather than purely epidemiological metrics would strengthen the evidence base for threshold optimization. Understanding how different threshold settings affect outbreak response timing and effectiveness would provide practical guidance for system design [15].

---

## References

[1] World Health Organization. Participatory surveillance guidance 2022. WHO; 2022.

[2] Mayaki LD. Enhancing real-time infectious disease surveillance through AI-driven early warning and predictive outbreak detection systems. GSC Biological and Pharmaceutical Sciences. 2025;33(03):001-014.

[3] Chen Y, et al. Progress and challenges in infectious disease surveillance and early warning. Medicine Plus. 2025;2(1):100071.

[4] Pan American Health Organization. Operational guidelines for sentinel SARI surveillance. PAHO; 2015.

[5] LogicMonitor. Static thresholds vs dynamic thresholds. LogicMonitor Blog; 2024.

[6] Schrell S, et al. Effectiveness and accuracy of syndromic surveillance in Spain. JMIR Public Health and Surveillance. 2024;10(1):e62641.

[7] Morr D, et al. Systematic scoping review of AI capability in epidemic/pandemic early warning systems. 2023.

[8] Awekeya T, et al. Evaluation of Ghana's COVID surveillance system effectiveness. 2023.

[9] Zhang Y, et al. Adaptive dynamic threshold method for respiratory infectious disease early warning. 2023.

[10] Garcia-Vozmediano A, et al. Machine learning early warning system for foodborne outbreaks. 2023.

[11] Dynatrace. Auto-adaptive thresholds for anomaly detection. Dynatrace Documentation; 2024.

[12] LogicMonitor. Managing alert fatigue: How dynamic thresholds help. 2024.

[13] Assessment of two complementary influenza surveillance systems using the moving epidemic method. Academia.edu; 2024.

[14] Zhang Z, et al. Comparison of threshold vs AI early warning approaches for respiratory infectious diseases. 2023.

[15] RAND Corporation. Evaluation of surveillance strategies for early detection. RAND Research Report; 2024.

[16] Statistical and mathematical time series methods for outbreak detection. arXiv:2410.17290; 2024.

[17] Frontiers in Public Health. AI applications in influenza surveillance. Frontiers; 2025.

[18] Chen Y, et al. Progress and challenges in infectious disease surveillance and early warning. ScienceDirect; 2025.

[19] Global Network for Disaster Reduction. LEWS global findings survey report. GNDR; 2025.

## Annotations


## Sources
[1] https://applications.emro.who.int/imemrf/250/J-Infection-Public-Health-2020-13-3-430-437-eng.pdf
[2] https://arxiv.org/html/2408.02575v1
[3] https://arxiv.org/html/2410.17290v1
[4] https://cdn.who.int/media/docs/default-source/influenza/participatory_surveillance_guidance_2022_10_18.pdf?sfvrsn=34905d39_1
[5] https://councilonstrategicrisks.org/wp-content/uploads/2021/07/Toward-A-Global-Pathogen-Early-Warning-System_2021_07_20-1.pdf
[6] https://docs.dynatrace.com/docs/discover-dynatrace/platform/davis-ai/anomaly-detection/concepts/auto-adaptive-threshold
[7] https://gsconlinepress.com/journals/gscbps/sites/default/files/GSCBPS-2025-0484.pdf
[8] https://ieeexplore.ieee.org/iel8/6488907/6702522/10835091.pdf
[9] https://pmc.ncbi.nlm.nih.gov/articles/PMC12230060/
[10] https://pmc.ncbi.nlm.nih.gov/articles/PMC12245528/
[11] https://pmc.ncbi.nlm.nih.gov/articles/PMC6440585/
[12] https://pmc.ncbi.nlm.nih.gov/articles/PMC9702983/
[13] https://pmc.ncbi.nlm.nih.gov/articles/PMC9707072/
[14] https://publichealth.jmir.org/2024/1/e62641
[15] https://www.academia.edu/51479124/Assessment_of_two_complementary_influenza_surveillance_systems_sentinel_primary_care_influenza_like_illness_versus_severe_hospitalized_laboratory_confirmed_influenza_using_the_moving_epidemic_method
[16] https://www.cureus.com/articles/378889-infectious-disease-surveillance-in-the-era-of-big-data-and-ai-opportunities-and-pitfalls
[17] https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2025.1609615/full
[18] https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2025.1609615/pdf
[19] https://www.gndr.org/wp-content/uploads/2025/06/LEWS-Global-findings-survey-report.pdf
[20] https://www.logicmonitor.com/blog/static-thresholds-vs-dynamic-thresholds
[21] https://www.medrxiv.org/content/10.1101/2024.10.27.24316208v1.full.pdf
[22] https://www.medrxiv.org/content/10.1101/2025.10.10.25337739v1.full.pdf
[23] https://www.paho.org/sites/default/files/2025-01/2015-cha-operational-guidelines-sentinel-sari.pdf
[24] https://www.rand.org/content/dam/rand/pubs/research_reports/RRA3700/RRA3704-1/RAND_RRA3704-1.pdf
[25] https://www.sciencedirect.com/science/article/pii/S2950347725000027
[26] https://www.splunk.com/en_us/blog/learn/adaptive-thresholding.html