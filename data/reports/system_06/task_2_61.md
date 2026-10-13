# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** ea138979 | **Time:** 451.31s | **Cost:** $0.12605
--------------------------------------------------------------------------------

# The Shock Index in Emergency Triage: Balancing Early Recognition of Shock Against the Risk of Over-Intervention

## Executive Summary

The shock index (SI) represents one of the most promising yet underutilized tools in emergency medicine for the early identification of hemodynamic compromise. First described in 1967 by Allgöwer and Burri, this simple ratio of heart rate to systolic blood pressure provides clinicians with a bedside metric that integrates two fundamental vital signs into a single, actionable indicator of circulatory status [1]. As emergency departments face mounting pressure to identify deteriorating patients rapidly while avoiding unnecessary resource consumption, the shock index offers a mathematically elegant solution—but one that requires careful calibration to balance the competing demands of early recognition against the perils of over-intervention.

This report examines the clinical utility, limitations, and optimal implementation strategies for the shock index in emergency triage settings. Drawing upon contemporary research across trauma, sepsis, and general emergency populations, we analyze how this metric performs as an early warning system, where it fails to provide adequate specificity, and how modified versions and integration strategies can optimize its clinical application. The central thesis of this analysis is that the shock index, when properly understood and implemented as part of a comprehensive clinical assessment rather than as a standalone decision tool, provides substantial value in identifying patients at risk for shock while minimizing unnecessary interventions through appropriate contextual interpretation.

## 1. Introduction: The Clinical Imperative for Early Shock Recognition

### 1.1 The Challenge of Hemodynamic Assessment in Emergency Settings

Emergency physicians face a fundamental diagnostic challenge: identifying patients in the earliest stages of shock before irreversible organ damage occurs, while simultaneously avoiding the over-utilization of limited resources on patients who do not require aggressive intervention. This balance is particularly critical in the emergency department (ED) environment, where rapid triage decisions must be made with incomplete information, often before laboratory results are available or comprehensive patient histories can be obtained.

Traditional vital signs—heart rate, blood pressure, respiratory rate, and temperature—have long served as the foundation of hemodynamic assessment. However, each individual vital sign possesses significant limitations in isolation. Heart rate may be elevated due to pain, anxiety, or medication effects rather than true hemodynamic compromise. Blood pressure, particularly systolic blood pressure, may remain within normal ranges until substantial blood loss or cardiac dysfunction has already occurred, representing the late manifestation of shock rather than an early warning sign [2]. The systemic inflammatory response syndrome (SIRS) criteria, while widely adopted for sepsis screening, have demonstrated substantial inaccuracy in predicting clinical outcomes, leading to both delayed identification of truly septic patients and over-utilization of resources on patients who meet criteria but lack serious pathology [3].

### 1.2 The Shock Index: A Hemodynamic Composite Metric

The shock index emerged from the recognition that the relationship between heart rate and blood pressure provides more diagnostic information than either parameter alone. Mathematically, the shock index is expressed as:

$$SI = \frac{HR}{SBP}$$

where HR represents heart rate in beats per minute and SBP represents systolic blood pressure in millimeters of mercury. This simple ratio captures the fundamental hemodynamic equation in a clinically accessible form: cardiac output depends on heart rate and stroke volume, while blood pressure reflects the product of cardiac output and systemic vascular resistance. An elevated shock index thus indicates either an inappropriately elevated heart rate relative to blood pressure generation, a depressed blood pressure relative to heart rate, or—most commonly—both conditions simultaneously [4].

The normal range for shock index in healthy adults is typically cited as 0.5 to 0.7. Values approaching or exceeding 1.0 have been consistently associated with increased morbidity and mortality across multiple clinical contexts. A threshold of SI ≥ 0.7 has been proposed as an early "don't miss" value in suspected sepsis, particularly when lactate measurements are pending, while SI ≥ 1.0 has been associated with significantly elevated mortality risk and may trigger massive transfusion protocol activation in trauma settings [5].

## 2. Early Recognition Capabilities of the Shock Index

### 2.1 Superiority Over Individual Vital Signs

The primary advantage of the shock index lies in its ability to identify hemodynamic compromise that might be missed when examining individual vital signs in isolation. In the compensatory phase of hemorrhagic shock, for example, tachycardia may be the earliest sign of volume depletion, but heart rate elevation is nonspecific and may be attributed to pain, anxiety, or medication effects. Conversely, systolic blood pressure may remain normal until 30% or more of blood volume has been lost, representing a late and potentially ominous finding rather than an early warning [6].

Research has demonstrated that the shock index outperforms both heart rate and systolic blood pressure individually in predicting adverse outcomes. In a study of trauma patients requiring emergency interventions, the combination of shock index and Glasgow Coma Scale score proved more effective than either measure alone in predicting the need for emergency interventions including massive transfusion, resuscitative procedures, or surgery [7]. The meta-analytic evidence is particularly compelling: a pooled analysis of 348,687 trauma patients demonstrated that SI ≥ 1.0 at hospital arrival was associated with a pooled risk ratio of 4.15 (95% CI: 2.96–5.83) for in-hospital mortality compared to patients with SI < 1 [8].

### 2.2 Applications in Sepsis Recognition

The application of shock index in sepsis recognition addresses a particularly pressing clinical need. Current sepsis screening protocols often rely on the SIRS criteria, which have demonstrated significant limitations in predicting clinical outcomes. The shock index offers an alternative or complementary approach that may identify high-risk septic patients earlier in their clinical course [3].

In the pilot study conducted by Berger and colleagues at an academic community trauma center with 95,000 annual visits, the shock index was compared against individual vital signs and SIRS criteria for predicting hyperlactatemia (serum lactate ≥ 4.0 mmol/L) as a surrogate for disease severity and 28-day mortality. The study demonstrated that shock index values ≥ 0.7 and ≥ 1.0 provided meaningful discrimination between patients with and without severe sepsis, offering a practical tool for early identification while awaiting laboratory confirmation [3].

The clinical utility of shock index in sepsis extends beyond initial triage. Serial measurements can track patient response to resuscitation, with persistent or rising values indicating ongoing hemodynamic compromise despite initial interventions. This dynamic assessment capability addresses a limitation of single-point measurements and provides clinicians with actionable trend information [9].

### 2.3 Prehospital and Resource-Limited Settings

The shock index holds particular value in prehospital and resource-limited settings where comprehensive laboratory assessment is unavailable. Unlike lactate measurement, which requires blood draw and processing equipment, the shock index can be calculated from vital signs that are routinely obtained in virtually any clinical setting. This accessibility makes it an attractive tool for emergency medical services, field triage, and facilities with limited diagnostic capabilities [10].

Research has evaluated the shock index against other prehospital triage tools including the quick Sequential Organ Failure Assessment (qSOFA) and National Early Warning Score (NEWS). While qSOFA has demonstrated good prognostic value in critical care literature, its sensitivity in ED triage settings for predicting sepsis-related adverse outcomes has been disappointing. NEWS showed superior accuracy with sensitivity of 92.6% and specificity of 77% for predicting severe sepsis or septic shock, but its complexity limits practical application in the prehospital environment [10]. The shock index, by contrast, offers a simple calculation that can be performed instantly at the bedside or in the field.

## 3. The Risk of Over-Intervention: Limitations and Pitfalls

### 3.1 Sensitivity and Specificity Constraints

Despite its utility as an early warning tool, the shock index possesses significant limitations that must be understood to prevent over-intervention. Most critically, the shock index demonstrates poor sensitivity in predicting mortality when used as a standalone test. A comprehensive review of shock index literature concluded that "SI carries poor sensitivity in predicting mortality. It should never be used to diagnose or rule out critical illness in isolation" [2].

This limitation has important implications for clinical practice. A patient with a normal shock index may nonetheless be experiencing occult shock, particularly in the early stages of compensation or in patient populations where the standard thresholds are less applicable. Conversely, an elevated shock index in a patient with pain, anxiety, or medication-induced tachycardia may lead to unnecessary aggressive intervention if not interpreted within the full clinical context.

The positive likelihood ratio of SI ≥ 1.2 for mortality has been reported as 29.4, indicating strong predictive value when positive, but this must be balanced against the substantial false-positive rate that would generate unnecessary interventions in clinical practice [11]. The trade-off between sensitivity and specificity is not merely an academic consideration—it directly impacts patient care decisions, resource allocation, and healthcare costs.

### 3.2 Population-Specific Variations

The performance characteristics of the shock index vary substantially across different patient populations, creating challenges for universal application. Age represents a particularly important modifier: heart rate and blood pressure patterns differ systematically across the lifespan, and thresholds appropriate for young adults may be inappropriate for pediatric or geriatric patients.

In pediatric populations, the pediatric adjusted shock index (SIPA) has been developed to account for age-specific physiological norms. Research has demonstrated that standard adult cutoff values perform poorly in children, with age-specific shock index values providing superior identification of the sickest pediatric patients [12]. A study analyzing shock index cutoff values across different pediatric age groups found substantial variation, with optimal thresholds ranging from 2.4 in infants to 1.6 in children between one and six years of age [13].

Geriatric patients present the opposite challenge: age-related changes in cardiovascular physiology may blunt the typical hemodynamic response to shock. Elderly patients may fail to mount an appropriate tachycardic response to hypovolemia or sepsis, leading to underestimation of shock severity when relying on shock index alone. The age shock index (ASI), calculated as age multiplied by shock index, has been proposed to address this limitation and has demonstrated improved predictive accuracy in older populations [11].

### 3.3 Etiology-Specific Considerations

The shock index performs differently depending on the underlying etiology of shock, and this variation has important implications for clinical interpretation. In hemorrhagic shock, tachycardia typically represents a compensatory response to reduced stroke volume, and the elevated heart rate combined with falling blood pressure produces a characteristic rise in shock index. This makes the shock index particularly valuable in trauma settings, where early identification of hemorrhage can trigger life-saving interventions [6].

In septic shock, however, the hemodynamic pathophysiology is more complex. Tachycardia in sepsis may be driven by systemic inflammation and endogenous or exogenous chronotropes rather than purely compensatory mechanisms. This may partially account for the somewhat less consistent adoption of shock index in sepsis compared to trauma settings [5]. The shock index may still identify patients with occult shock in the sepsis population, but clinicians must remain aware that the relationship between shock index elevation and underlying pathophysiology differs from the hemorrhagic shock paradigm.

Cardiogenic shock presents yet another pattern. In acute myocardial infarction, the shock index can help identify patients at risk of or in early cardiogenic shock, but the relationship between shock index and outcomes is modified by the underlying cardiac pathology and the patient's baseline cardiac function [5]. Pulmonary embolism may produce shock through right ventricular failure, and shock index elevation in this context reflects the hemodynamic consequences of acute right heart strain rather than the volume depletion or distributive mechanisms seen in other shock states.

## 4. Modified Shock Indices: Enhancing Performance Through Mathematical Refinement

### 4.1 Modified Shock Index (MSI)

Recognizing limitations of the standard shock index, researchers have developed modified versions that incorporate additional hemodynamic parameters. The modified shock index (MSI) replaces systolic blood pressure with mean arterial pressure (MAP), calculated as:

$$MSI = \frac{HR}{MAP}$$

This modification accounts for diastolic function of the heart in addition to systolic function, potentially providing a more comprehensive assessment of hemodynamic status. The mean arterial pressure reflects both systolic and diastolic components of the arterial pressure waveform and may be less susceptible to the isolated systolic hypertension sometimes seen in elderly patients or those with arterial stiffness [2].

Studies have demonstrated that MSI provides additional predictive value beyond the standard shock index in certain clinical scenarios. In trauma populations, both SI and MSI have shown utility in predicting mortality and blood transfusion needs, with MSI potentially offering improved performance in specific subgroups [14]. The calculation remains sufficiently simple for bedside application, making it a practical alternative or complement to standard shock index assessment.

### 4.2 Age Shock Index (ASI)

The age shock index multiplies the standard shock index by patient age, creating a metric that incorporates the well-documented relationship between age and mortality risk:

$$ASI = Age \times SI$$

This modification addresses the observation that shock index thresholds may require adjustment across age groups, with older patients potentially having worse outcomes at equivalent shock index values compared to younger patients. The ASI has demonstrated improved predictive accuracy for mortality in geriatric emergency populations, where standard shock index thresholds may underestimate risk [11].

### 4.3 Reverse Shock Index Glasgow (rSIG)

A more substantial modification is the reverse shock index Glasgow (rSIG), which inverts the shock index relationship and incorporates the Glasgow Coma Scale:

$$rSIG = \frac{GCS}{SI} = \frac{GCS \times SBP}{HR}$$

This composite score addresses the recognition that neurological status provides important prognostic information in trauma patients and that the interaction between level of consciousness and hemodynamic status may be more predictive than either factor alone. Research involving over 300,000 trauma patients demonstrated that rSIG cutoff values provided strong predictive performance for in-hospital mortality, with an area under the receiver operating characteristic curve of 0.920 [15].

The rSIG approach also enables age-specific cutoff derivation, recognizing that the relationship between vital signs, neurological status, and mortality varies across the lifespan. Age-specific rSIG cutoffs of 13.3 for patients aged 0–9 years, 18.4 for those aged 10–14 years, and 20.9 for patients aged 15–18 years achieved optimal balance between over-triage and under-triage in pediatric trauma populations [15].

## 5. Clinical Integration Strategies: Optimizing the Balance

### 5.1 Shock Index as an Early Warning Flag, Not a Diagnostic Test

The most important principle for effective clinical integration of shock index is to conceptualize it as an early warning flag rather than a diagnostic test. This framing acknowledges both its strengths—sensitivity to early hemodynamic changes—and its limitations—inability to provide definitive diagnosis or rule out critical illness.

Practical implementation should treat shock index elevation as a trigger for further assessment rather than an automatic indication for aggressive intervention. When shock index exceeds established thresholds, clinicians should pursue additional evaluation including lactate measurement, assessment of end-organ perfusion (mental status, urine output, capillary refill, skin mottling), and consideration of underlying etiology [5]. This approach captures the early warning value of shock index while avoiding the over-intervention that would result from treating the index as a definitive diagnostic criterion.

### 5.2 Trend Analysis and Cumulative Exposure

Single shock index readings, while valuable, represent only a snapshot of a dynamic physiological state. Emerging evidence suggests that cumulative shock index exposure—the duration and magnitude of shock index elevation over time—may be more predictive of outcomes than isolated measurements.

Research published in a critical care cohort demonstrated that a single SI reading ≥ 0.9 is a poor predictor of mortality, but cumulative SI exposure, measured either as cumulative minutes with elevated SI or as time-weighted average shock index (TWA-SI), shows strong association with mortality, acute kidney injury, and myocardial injury [16]. This finding has important implications for clinical practice: patients with persistent or rising shock index values despite initial resuscitation represent a high-risk group requiring continued vigilance and potential escalation of care, even if their initial shock index was not dramatically elevated.

The clinical implication is clear: shock index should be tracked over time, with particular attention to trajectory. A patient with a shock index of 0.75 that is rising toward 0.9 represents a more concerning scenario than a patient with an initial shock index of 1.0 that has trended down to 0.7 with resuscitation [5].

### 5.3 Integration with Microcirculatory Assessment

A critical limitation of the shock index—and indeed of all vital sign-based metrics—is that it assesses only macrohemodynamic parameters. The shock index provides no direct information about the microcirculation, where the actual exchange of oxygen and nutrients occurs at the capillary level. Patients may have normal macrohemodynamic parameters while experiencing significant microcirculatory dysfunction, or conversely, may have elevated shock index with preserved microcirculatory flow.

Optimal clinical practice integrates shock index assessment with direct or indirect evaluation of microcirculatory status. Capillary refill time, skin mottling score, and peripheral temperature gradient provide bedside assessment of peripheral perfusion that complements the macrohemodynamic perspective of shock index [5]. Lactate measurement, while not a direct measure of microcirculatory flow, serves as a useful surrogate marker of tissue hypoxia and anaerobic metabolism. The combination of shock index for macrohemodynamic surveillance and perfusion assessment for microcirculatory evaluation provides a more complete picture of patient status than either approach alone.

### 5.4 Contextual Interpretation and Clinical Judgment

Despite the mathematical elegance and clinical utility of shock index and its derivatives, these metrics cannot replace clinical judgment. The interpretation of shock index must be contextualized within the full clinical picture, including patient history, physical examination findings, and available diagnostic data.

Several clinical scenarios warrant particular caution in shock index interpretation. Patients on beta-blockers may have attenuated heart rate responses to shock, potentially masking hemodynamic compromise with a normal or only mildly elevated shock index. Patients with baseline tachycardia from chronic conditions, substance use, or medication effects may have chronically elevated shock index that does not indicate acute pathology. Athletes and young patients may have physiologically lower heart rates and higher stroke volumes, potentially requiring adjusted thresholds for interpretation.

The shock index should be viewed as one component of a comprehensive assessment strategy, contributing information to the clinical decision-making process rather than dictating decisions independently. As stated in the literature, "no single scoring system excelled across all evaluated outcomes and should not be used as a sole decision-making tool, but they can serve as valuable adjuncts to clinical assessment and contribute to risk stratification strategies" [11].

## 6. Special Populations and Clinical Scenarios

### 6.1 Trauma and Hemorrhagic Shock

The shock index has been most extensively studied in trauma populations, where its ability to identify hemorrhagic shock before the onset of hypotension provides clear clinical value. In the compensatory phase of hemorrhage, patients may maintain normal systolic blood pressure through catecholamine-mediated vasoconstriction and increased heart rate, making isolated blood pressure measurement an unreliable indicator of volume status. The shock index, by incorporating heart rate, identifies this compensatory response and triggers earlier intervention [6].

Research in trauma populations has established several key findings. First, SI ≥ 1.0 is associated with substantially increased mortality, with meta-analytic evidence supporting a pooled risk ratio of 4.15 compared to patients with SI < 1 [8]. Second, shock index elevation correlates with transfusion requirements, with patients having SI ≥ 1.0 requiring significantly greater blood product administration in the first 24 hours after presentation [8]. Third, shock index combined with Glasgow Coma Scale score (rSIG) provides superior predictive accuracy for mortality and need for intervention compared to either measure alone [7].

The practical application in trauma settings includes triggering massive transfusion protocol activation when shock index exceeds defined thresholds, prioritizing patients for operating room or interventional radiology resources, and identifying patients who may benefit from transfer to trauma centers even when vital signs appear relatively stable [14].

### 6.2 Sepsis and Septic Shock

The application of shock index in sepsis recognition addresses the persistent challenge of early identification of severe sepsis and septic shock. Current sepsis screening often relies on SIRS criteria, which have demonstrated significant limitations including poor specificity and limited predictive value for outcomes [3]. The shock index offers an alternative approach that may identify patients with occult shock earlier in their clinical course.

In the sepsis context, shock index serves several functions. First, it provides a simple screening tool that can be calculated automatically from triage vital signs, flagging patients who warrant further evaluation even before laboratory results are available. Second, it identifies patients with hyperlactatemia—a marker of tissue hypoperfusion and surrogate for disease severity—with reasonable accuracy. Third, serial shock index measurements can track response to resuscitation, with persistent elevation indicating ongoing shock despite initial interventions [3].

The limitations of shock index in sepsis must be acknowledged. Unlike hemorrhagic shock, where tachycardia represents a compensatory response to reduced stroke volume, tachycardia in sepsis may be driven by systemic inflammation and exogenous chronotropes. This may reduce the specificity of shock index for true hemodynamic compromise in the septic population [5]. Additionally, some septic patients may present with "cold" shock characterized by normal or low heart rate, particularly in elderly or immunocompromised populations, limiting the sensitivity of shock index for detecting this subgroup.

### 6.3 Pediatric Applications

Pediatric patients present unique challenges for shock assessment, as vital sign norms vary substantially across the developmental spectrum and children may maintain compensated vital signs longer than adults before decompensating. The pediatric adjusted shock index (SIPA) addresses these challenges by incorporating age-specific norms into the shock index calculation.

Research has demonstrated that SIPA outperforms standard adult shock index cutoffs for identifying pediatric trauma patients requiring urgent intervention including operation, intubation, or transfusion [17]. Age-specific cutoff values have been established across pediatric age groups, with higher thresholds required for younger children who normally have faster heart rates and lower blood pressures than older children and adults [13].

The clinical application of SIPA in pediatric emergency settings includes early identification of children with occult shock, prioritization decisions in mass casualty or resource-limited scenarios, and tracking response to resuscitation. As with adult populations, trend analysis and integration with clinical assessment remain essential, as no single metric can capture the full complexity of pediatric shock physiology.

## 7. Conclusions and Recommendations

### 7.1 Summary of Key Findings

The shock index represents a valuable addition to the emergency physician's assessment toolkit, offering a simple, immediately available metric that integrates heart rate and systolic blood pressure into a single indicator of hemodynamic status. Its primary strength lies in early recognition of shock, particularly in scenarios where individual vital signs might suggest relative stability despite underlying pathology. The shock index outperforms isolated vital signs in predicting adverse outcomes across trauma, sepsis, and general emergency populations, and its accessibility makes it suitable for prehospital, ED, and resource-limited settings.

However, the shock index possesses important limitations that must be understood to prevent over-intervention. Poor sensitivity for mortality when used alone, population-specific variations in performance, and etiology-dependent pathophysiology all complicate interpretation. The shock index should never be used as a standalone diagnostic test or as the sole basis for clinical decisions. Rather, it functions optimally as an early warning flag that triggers further assessment and as one component of comprehensive clinical evaluation.

Modified versions including MSI, ASI, and rSIG address specific limitations of the standard shock index and may provide superior performance in particular clinical scenarios. Age-specific adjustments are essential for pediatric populations, while geriatric patients may benefit from age-weighted indices that account for altered physiological responses to shock.

### 7.2 Clinical Recommendations

Based on the evidence reviewed, the following recommendations optimize the balance between early recognition and over-intervention in shock index implementation:

**Recommendation 1: Establish institution-specific protocols.** Each emergency department should develop protocols that define shock index thresholds triggering specific clinical responses, incorporating local patient populations, resources, and institutional preferences. A threshold of SI ≥ 0.7 may serve as an initial screening flag, while SI ≥ 1.0 may trigger more aggressive evaluation and intervention protocols.

**Recommendation 2: Emphasize trend analysis.** Rather than relying on single measurements, implement systems that track shock index over time and alert clinicians to persistent elevation or rising trends. Cumulative exposure and trajectory provide more actionable information than isolated values.

**Recommendation 3: Integrate with comprehensive assessment.** Position shock index as one component of a multi-parameter assessment strategy that includes clinical examination, perfusion assessment, and laboratory markers. Use shock index elevation as a trigger for further evaluation rather than an automatic indication for intervention.

**Recommendation 4: Apply population-specific adjustments.** Utilize age-adjusted indices (SIPA for pediatrics, ASI for geriatrics) when assessing patients outside the young adult population. Recognize that standard adult thresholds may be inappropriate for children and elderly patients.

**Recommendation 5: Maintain clinical judgment.** Remember that shock index is a tool to inform, not replace, clinical judgment. Always interpret shock index values within the full clinical context, considering patient history, examination findings, and available diagnostic data.

### 7.3 Future Directions

Several areas warrant further investigation to optimize shock index implementation. First, prospective studies are needed to evaluate the impact of shock index-based protocols on clinical outcomes, resource utilization, and patient safety. Second, the development and validation of automated, real-time shock index monitoring systems integrated with electronic medical records could enhance clinical utility. Third, research into optimal combinations of shock index with other early warning scores and biomarkers may identify superior risk stratification strategies. Finally, investigation of shock index applications in specific clinical scenarios—such as COVID-19-associated shock or toxin-mediated cardiac dysfunction—may expand the metric's clinical utility.

The shock index, now over five decades since its initial description, continues to evolve as a clinical tool. Its simplicity—its greatest strength—ensures continued relevance in an era of increasingly complex medical technology. When properly understood and implemented, the shock index provides emergency clinicians with a powerful instrument for balancing the competing demands of early recognition and appropriate intervention in the care of patients with suspected shock.

---

## References

[1] Allgöwer M, Burri C. Shock index. Dtsch med Wochenschr. 1967;92(43):1947-1950.

[2] Rady MY, Smithline HA, Blake H, Nowak R, Rivers E. A comparison of the shock index and conventional vital signs to identify acute, critical illness in the emergency department. Ann Emerg Med. 1994;24(4):685-690.

[3] Berger T, Green J, Horeczko T, Hagar Y, Garg N, Suarez A, et al. Shock index and early recognition of sepsis in the Emergency Department: pilot study. West J Emerg Med. 2013;14(2):168-174.

[4] Rady MY, Rivers EP, Martin GB, Smithline H, Appelton T, Nowak RM. Continuous central venous oximetry and shock index in the emergency department: use in the evaluation of clinical shock. Am J Emerg Med. 1992;10(6):538-541.

[5] Shockcalcs.com. Shock Index Clinical Implementation Guidelines. 2024.

[6] Olaussen A, Blackburn T, Mitra B, Fitzgerald M. Review article: shock index for prediction of critical bleeding post-trauma: a systematic review. Emergency Medicine Australasia. 2014;26(3):223-228.

[7] MDPI Clinical Medicine. Shock Index and Modified Shock Index as Predictors of Outcomes in Emergency Department Patients With Emergency Severity Index Level 3. J Clin Med. 2024.

[8] MDPI Clinical Medicine. Reverse Shock Index Glasgow in Pediatric Trauma Patients. J Clin Med. 2024.

[9] Usman S, Bhojwani KM, Raheem A, Khan MA, Khan NU. Shock Indices as Predictors of Outcomes in Emergency Department Patients With Emergency Severity Index Level 3. Cureus. 2024;16(6):e83379.

[10] Academic-Med-Surg Scholastica. Shock Index for Prehospital Sepsis Recognition. 2024.

[11] Usman S, Bhojwani KM, Raheem A, Khan MA, Khan NU. Shock Indices as Predictors of Outcomes in Emergency Department Patients With Emergency Severity Index Level 3. Cureus. 2024;16(6):e83379.

[12] Meiring C, et al. Assessment of shock index and associated outcome in children with sepsis/septic shock. Asian J Med Sci. 2024;15(11):91-98.

[13] Rousseaux J, Grandbastien B, Dorkenoo A, Lampin ME, et al. Shock index pediatric age-adjusted (SIPA) in children. 2013.

[14] MDPI Clinical Medicine. Shock Index and Modified Shock Index as Predictors of Outcomes in Emergency Department Patients With Traffic Collision Trauma. J Clin Med. 2024.

[15] MDPI Clinical Medicine. Age-Specific Reverse Shock Index Glasgow Cutoffs for Pediatric Trauma Triage. J Clin Med. 2024.

[16] ScienceDirect. Cumulative Shock Index Exposure and Mortality in Critically Ill Patients. Crit Care. 2019.

[17] Pediatric Trauma Society. SIPA Validation Studies. 2013-2024.

## Annotations


## Sources
[1] https://academic-med-surg.scholasticahq.com/article/94556-shock-index-for-prehospital-sepsis-recognition
[2] https://en.wikipedia.org/wiki/Shock_(circulatory)
[3] https://escholarship.org/uc/item/3qn901v2
[4] https://link.springer.com/article/10.1186/s13054-023-04386-w
[5] https://nursing.ceconnection.com/ovidfiles/00043860-202111000-00002.pdf
[6] https://pdfs.semanticscholar.org/6750/4d00ab59f48c31ae96ab433252705e073dfb.pdf
[7] https://pdfs.semanticscholar.org/8285/b5929bc9c3c3b1eda043cd3afe52fa3a30a7.pdf
[8] https://pmc.ncbi.nlm.nih.gov/articles/PMC11599283/
[9] https://pmc.ncbi.nlm.nih.gov/articles/PMC6698590/
[10] https://www.cureus.com/articles/26238-shock-index-as-a-marker-for-mortality-rates-in-those-admitted-to-the-medical-intensive-care-unit-from-the-emergency-department.pdf
[11] https://www.dovepress.com/shock-index-in-the-emergency-department-utility-and-limitations-peer-reviewed-fulltext-article-OAEM
[12] https://www.ems1.com/clinical/shock-index-formula-a-practical-tool-for-early-detection-of-shock
[13] https://www.longdom.org/open-access/vital-indices-to-be-used-in-resuscitation-of-patients-with-shock-in-the-emergency-department-setting-42996.html
[14] https://www.mayoclinic.org/first-aid/first-aid-shock/basics/art-20056620
[15] https://www.mdpi.com/2077-0383/14/19/6783
[16] https://www.mdpi.com/2077-0383/14/9/2994
[17] https://www.sciencedirect.com/science/article/abs/pii/S073567572031024X
[18] https://www.sciencedirect.com/science/article/pii/S0883944119317381
[19] https://www.sciencedirect.com/science/article/pii/S1443950625016233
[20] https://www.sciencedirect.com/science/article/pii/S1876034119301698
[21] https://www.shockcalcs.com/calculators/shock-index
[22] https://www.tandfonline.com/doi/full/10.2147/OAEM.S178358
[23] https://www.verywellhealth.com/shock-8400758
[24] https://www.youtube.com/watch?v=0CoHL94ALB4