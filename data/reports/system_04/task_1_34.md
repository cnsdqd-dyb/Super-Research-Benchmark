# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 38c86ad4 | **Time:** 446.41s | **Cost:** $1.85459
--------------------------------------------------------------------------------

# Balancing Clinical Rigor and Behavioral Flexibility in Digital Health Interventions for Type 2 Diabetes

**Key Points**
*   **Integration of Data Streams:** Successful digital health interventions (DHIs) bridge the gap between clinical outcomes (HbA1c) and daily behaviors by utilizing connected devices (glucometers, CGMs, scales) that automatically upload data. This allows for "passive sensing," reducing the user burden of manual logging while providing clinicians with real-time actionable data.
*   **Algorithmic Triage:** Platforms like Livongo and Omada utilize algorithmic triage to balance safety with lifestyle guidance. Acute biometric outliers (e.g., severe hypoglycemia) trigger immediate clinical escalation to human professionals, while routine data points trigger automated, behavioral "nudges" or educational content, ensuring resources are allocated efficiently without overwhelming the patient.
*   **The Role of Human-in-the-Loop:** While AI and automation handle routine monitoring, sustained adherence is significantly higher when human coaching is integrated. The "accountability factor" provided by remote coaches or peer groups (as seen in Omada and Virta Health) is critical for long-term lifestyle maintenance, whereas standalone apps often suffer from high attrition rates after 3–6 months.
*   **Precision and Personalization:** Emerging "Digital Twin" technologies (e.g., Twin Health) and nutritional ketosis programs (e.g., Virta) move beyond generic lifestyle advice. By correlating specific behaviors (sleep, specific meals) directly with glucose responses, these platforms shift the patient's motivation from abstract clinical goals (lowering HbA1c) to immediate, tangible feedback, thereby reinforcing adherence through visible cause-and-effect relationships.
*   **Mitigating Digital Burden:** A major challenge in balancing monitoring with adherence is "digital burden" or "surveillance fatigue." Interventions that require excessive manual entry or generate frequent, non-actionable alarms can decrease adherence. Successful platforms mitigate this by emphasizing "support" over "surveillance," using gamification, and ensuring that data sharing results in empowering feedback rather than judgment.

## 1. Introduction

The management of Type 2 Diabetes Mellitus (T2DM) has historically been bifurcated into clinical monitoring—periodic assessment of glycated hemoglobin (HbA1c) and fasting blood glucose—and lifestyle modification, which encompasses diet, physical activity, and weight management. Traditional care models often struggle to bridge the temporal and practical gap between these two domains; patients receive clinical feedback retrospectively during infrequent office visits, leaving them without guidance during the daily decision-making processes that drive metabolic health. Digital health interventions (DHIs) have emerged as a critical mechanism to close this loop, offering a continuum of care that integrates clinical surveillance with real-time behavioral support.

The core challenge for these interventions lies in balancing the rigor of clinical monitoring with the flexibility required for sustainable lifestyle change. Excessive monitoring can lead to patient burnout and "surveillance fatigue," while insufficient guidance can result in non-adherence and clinical inertia. Contemporary DHIs address this balance through a convergence of technologies: mobile health (mHealth) applications, wearable sensors (such as Continuous Glucose Monitors or CGMs), telemedicine, and algorithmic analytics. These tools function not merely as data repositories but as active agents of behavioral change, utilizing techniques such as gamification, feedback loops, and precision coaching to translate biometric data into actionable lifestyle adjustments [cite: 1, 2].

This report examines the mechanisms by which DHIs achieve this balance. It explores the theoretical frameworks underpinning digital adherence, the technological infrastructure of remote monitoring, and the specific strategies employed by leading platforms to maintain patient engagement while ensuring clinical safety.

## 2. Theoretical Frameworks of Adherence in Digital Health

To understand how DHIs balance monitoring with guidance, it is necessary to examine the behavioral frameworks that drive adherence in a digital context. Adherence in T2DM is multifaceted, requiring compliance with medication regimens, dietary restrictions, and self-monitoring protocols.

### 2.1 The Chronic Care Model and Digital Adaptation
The Chronic Care Model (CCM) posits that effective management requires an informed, active patient and a proactive practice team. DHIs operationalize the CCM by shifting the locus of control from the clinic to the patient’s daily life. Digital tools facilitate this by providing "self-management support" through automated reminders and educational content, and "decision support" through algorithmic analysis of blood glucose trends [cite: 3].

Research indicates that DHIs that align with CCM principles—specifically those fostering productive interactions between patients and providers—demonstrate superior outcomes. For instance, interventions that combine remote monitoring with feedback loops (a core CCM component) significantly reduce HbA1c compared to usual care [cite: 4, 5]. The digital adaptation of CCM ensures that monitoring is not a passive activity but a trigger for engagement, thereby maintaining adherence through continuous, rather than episodic, care.

### 2.2 Self-Efficacy and Behavioral Change Techniques (BCTs)
Self-efficacy—the belief in one's ability to execute behaviors necessary to produce specific performance attainments—is a primary predictor of adherence in T2DM management. DHIs enhance self-efficacy by breaking down complex metabolic management into manageable, trackable tasks.

A systematic review of mHealth apps identified "self-monitoring of behavior" as the BCT most strongly associated with improved metabolic outcomes [cite: 6, 7]. By allowing patients to visualize the correlation between their actions (e.g., a specific meal) and their clinical results (e.g., a glucose spike), DHIs transform abstract clinical goals into concrete, manageable behavioral targets.
*   **Feedback and Monitoring:** The most effective interventions combine self-monitoring with feedback. Apps that provide immediate automated feedback or facilitate review by a healthcare professional (HCP) create a sense of accountability and progression [cite: 8].
*   **Problem Solving:** Interventions that include BCTs focused on problem-solving (e.g., "How do I handle a social dinner?") and "reward and threat" (e.g., gamified points or health warnings) show greater HbA1c reductions than those that do not [cite: 8].

### 2.3 The "Digital Burden" Framework
While BCTs promote adherence, the "work" of being a patient in a digital ecosystem can impede it. This is conceptualized as "digital treatment burden." Patients must calibrate devices, interpret data, charge batteries, and respond to alerts. Qualitative studies reveal that when the burden of these tasks outweighs the perceived benefit (e.g., constant alarms causing fatigue), adherence drops [cite: 9, 10]. Therefore, the balance between monitoring and guidance is essentially a balance between the *effort* required to input data and the *value* of the guidance received.

## 3. Mechanisms of Integration: Linking HbA1c to Lifestyle

The technological architecture of DHIs is designed to ingest clinical data and output lifestyle guidance. This process relies on distinct mechanisms that filter, analyze, and triage information.

### 3.1 Passive Sensing and Connected Devices
To reduce the friction of self-monitoring, modern DHIs utilize cellular-connected devices that transmit data automatically. This "passive sensing" approach is critical for maintaining long-term adherence, as it removes the need for manual logbooks.
*   **Connected Glucometers:** Platforms like Livongo and Omada provide glucometers that upload readings to the cloud immediately upon testing. This allows the system to capture data without requiring the patient to open an app or enter numbers manually [cite: 1, 11].
*   **Continuous Glucose Monitoring (CGM):** CGMs represent a paradigm shift from "snapshots" of glucose to continuous video-like data streams. They provide immediate biofeedback, showing patients exactly how lifestyle choices affect glycemic variability. This real-time data is more actionable for lifestyle modification than HbA1c, which is a lagging indicator [cite: 12, 13].
*   **Integration with Wearables:** Activity trackers (e.g., Apple Watch, Fitbit) integrate physical activity data with glucose data. This allows DHIs to contextualize glucose readings—for example, identifying that a post-prandial spike was blunted by a subsequent walk [cite: 1, 14].

### 3.2 Algorithmic Triage and Clinical Escalation
A critical function of DHIs is distinguishing between data points that require behavioral "nudges" and those that require clinical intervention. This "algorithmic triage" ensures that patients receive the right level of care without overwhelming human coaching resources.

**The Livongo Model of Triage:**
Livongo (now part of Teladoc Health) employs a "Smart Cloud" system that analyzes every blood glucose (BG) reading uploaded by its connected meter.
1.  **Routine/Behavioral Range:** If a reading is within a standard range (e.g., slightly elevated), the meter or app provides an automated "nudge" or educational tip (e.g., "Drink a glass of water" or "Walk for 15 minutes") [cite: 15].
2.  **Acute/Clinical Range:** If a reading breaches a safety threshold (e.g., <50 mg/dL or >400 mg/dL), the system triggers a clinical alert. Within minutes (often <3 minutes), a Certified Diabetes Care and Education Specialist (CDCES) contacts the patient via phone or text to ensure safety, troubleshoot the cause, and advise on immediate remediation [cite: 16, 17].

This mechanism balances monitoring with guidance by automating the routine lifestyle advice while reserving human clinical supervision for safety-critical moments. This prevents "alert fatigue" for the provider while ensuring the patient feels supported rather than surveilled.

### 3.3 The Feedback Loop: From Data to Insight
The effectiveness of monitoring depends on the latency and quality of the feedback. Traditional care offers delayed feedback (months later). DHIs offer two types of feedback loops:
*   **Synchronous (Real-Time):** Automated messages on a meter or app immediately following a test. This influences immediate behavior (e.g., correcting a low, avoiding a snack) [cite: 15].
*   **Asynchronous (Coaching):** Human coaches review aggregated data to identify patterns (e.g., "Your glucose is consistently high after Tuesday lunches"). This supports long-term lifestyle restructuring [cite: 18].

Research indicates that apps providing *personalized* feedback based on user data are significantly more effective at improving HbA1c than those that simply track data [cite: 19].

## 4. Remote Guidance Strategies

Once data is collected, DHIs employ various strategies to guide patient behavior. These strategies range from human interaction to gamified digital environments.

### 4.1 Human Coaching vs. AI Guidance
The "human-in-the-loop" remains a vital component of adherence. While AI can identify patterns, human coaches provide the empathy and accountability necessary for sustained behavioral change.
*   **The Hybrid Model:** Most successful platforms (Omada, Virta, Livongo) use a hybrid model. AI handles data collection and pattern recognition, while human coaches focus on barrier identification, motivation, and complex problem-solving [cite: 20, 21].
*   **Accountability:** The knowledge that a human coach is monitoring their progress creates a "sentinel effect," where patients adhere to protocols partly because they know they are being observed by a supportive figure. Omada Health attributes its high retention rates to the relationship built between participants and their dedicated health coaches [cite: 21, 22].

### 4.2 Gamification and Social Dynamics
Gamification applies game-design elements to non-game contexts to enhance engagement. In diabetes management, this transforms the drudgery of monitoring into a rewarding activity.
*   **Mechanisms:** Common elements include points, badges, leaderboards, and streaks. For example, the *mySugr* app uses a "diabetes monster" avatar that users must "tame" through logging and adherence [cite: 23].
*   **Outcomes:** Gamification has been shown to improve HbA1c, body weight, and lipid profiles by increasing motivation and self-efficacy [cite: 24, 25]. A study on the *SidekickHealth* gamified program showed significant reductions in HbA1c and disease-specific distress compared to standard care [cite: 26].
*   **Social Support:** Many platforms incorporate peer groups. Omada places users in "cohorts" of similar individuals (e.g., by region or start date). This fosters a sense of community and shared struggle, which is a powerful driver of long-term adherence [cite: 22, 27].

### 4.3 Precision Nutrition and "Digital Twins"
Advanced DHIs are moving toward hyper-personalization using "Digital Twin" technology.
*   **Concept:** A Digital Twin is a dynamic virtual representation of a patient's metabolism, built using data from CGMs, activity trackers, and food logs.
*   **Application:** Twin Health’s "Whole Body Digital Twin" analyzes thousands of data points daily to predict how a specific food will affect a specific patient. Instead of generic advice ("eat less carbs"), the system provides precise guidance ("avoid this specific oatmeal brand").
*   **Adherence Mechanism:** This precision reduces the trial-and-error frustration of diabetes management. By seeing immediate, personalized cause-and-effect relationships, patients are more likely to adhere to dietary changes. Clinical trials have shown this approach can lead to significant HbA1c reduction and even remission [cite: 14, 28, 29].

## 5. Case Studies in Balancing Clinical and Lifestyle Goals

Different platforms prioritize different aspects of the monitoring-guidance balance depending on their clinical philosophy.

### 5.1 Omada Health: The Behavioral Change Focus
*   **Philosophy:** Omada is based on the Diabetes Prevention Program (DPP) curriculum, focusing heavily on weight loss and behavioral psychology.
*   **Balance Strategy:** Omada prioritizes *passive sensing* to minimize burden. It provides a cellular-connected scale and glucometer that sync automatically. The clinical monitoring is secondary to the behavioral coaching; the data serves primarily to inform the coach's conversation with the patient rather than to trigger acute medical alarms.
*   **Adherence:** By grouping patients into peer cohorts and providing a dedicated human coach, Omada achieves high engagement, with studies showing clinically meaningful HbA1c reductions and weight loss [cite: 21, 27].

### 5.2 Livongo (Teladoc): The Acute Management Focus
*   **Philosophy:** Livongo focuses on "empowerment" through timely information and safety.
*   **Balance Strategy:** The balance is achieved through its "Smart Cloud" triage. It acts as a safety net (clinical monitoring) while providing "nudges" (lifestyle guidance). The ability to order test strips directly from the meter reduces a logistical barrier to adherence [cite: 11, 30].
*   **Adherence:** The immediate feedback loop (within minutes) reinforces the value of testing. Users feel safe knowing a CDCES will call if things go wrong, which encourages them to continue monitoring [cite: 16, 31].

### 5.3 Virta Health: The Medical Supervision Focus
*   **Philosophy:** Virta aims for diabetes *reversal* through nutritional ketosis (very low carbohydrate intake).
*   **Balance Strategy:** Because nutritional ketosis can rapidly alter insulin requirements, Virta requires *intensive* clinical monitoring. Patients log biomarkers frequently, and a physician-led team actively manages medications (deprescribing). The "lifestyle guidance" is rigorous nutritional therapy.
*   **Adherence:** The primary motivator is "medication elimination." The tangible reward of stopping insulin or other drugs drives adherence to the strict dietary protocol. Virta reports high retention (83% at one year) because the clinical outcome (deprescribing) is highly valued by patients [cite: 32, 33, 34].

### 5.4 Twin Health: The Precision Data Focus
*   **Philosophy:** Reversing metabolic disease through AI-driven precision nutrition.
*   **Balance Strategy:** Twin Health utilizes the most intensive monitoring (CGMs + other sensors) to feed its AI Digital Twin. The high burden of data collection is balanced by the high value of the output: hyper-personalized recommendations that allow for "metabolic flexibility."
*   **Adherence:** The gamification of the "Metabolic Flexibility Score" and the visual proof of improvement via the app encourage users to maintain the regimen [cite: 29, 35].

## 6. The Challenge of "Digital Burden" and Surveillance

While DHIs offer significant benefits, they introduce new challenges regarding the patient experience.

### 6.1 Monitoring Fatigue and Intrusiveness
Qualitative research highlights that the work of digital self-management—calibrating devices, responding to alarms, and entering data—can become a "treatment burden."
*   **Alarm Fatigue:** Constant alerts from CGMs or apps can cause anxiety and sleep disruption, leading some patients to discontinue use [cite: 9].
*   **Intrusiveness:** Patients often feel that remote monitoring is a form of "surveillance." There is a tension between feeling "supported" (someone is watching *over* me) and "watched" (someone is judging me). Design features that emphasize autonomy and non-judgmental feedback are crucial for mitigating this feeling [cite: 36].

### 6.2 User Experience (UX) and Accessibility
Adherence is heavily influenced by UX. Apps that are difficult to navigate, have small fonts, or lack integration with other aspects of life (e.g., meal planning) see lower adoption, particularly among older adults who make up a significant portion of the T2DM population [cite: 37, 38].
*   **Passive vs. Active:** Strategies that rely on passive data collection (wearables) are generally more sustainable than those requiring active manual entry (food logging), which has high attrition [cite: 6].

## 7. Clinical Efficacy vs. Long-term Adherence

The ultimate measure of these interventions is whether the balance of monitoring and guidance leads to sustained clinical improvement.

### 7.1 HbA1c Reduction
Meta-analyses consistently show that DHIs lead to statistically significant reductions in HbA1c compared to control groups.
*   **Magnitude:** Reductions typically range from 0.3% to 1.0% [cite: 5, 39, 40].
*   **Context:** These reductions are comparable to or better than some pharmacological interventions, particularly when combined with human coaching.

### 7.2 Sustainability of Results
A key question is whether these gains persist after the novelty of the digital tool wears off.
*   **Long-term Data:** Some studies show sustained benefits up to 3 years. For example, a study on a digital lifestyle tool showed sustained HbA1c reduction even in patients who ceased using the tool after one year, suggesting that the *educational* impact of the guidance led to lasting behavioral changes [cite: 41].
*   **Attrition:** However, dropout rates in RCTs for apps can be high (up to 40%). Interventions that include human interaction (coaching) tend to have lower attrition than standalone apps [cite: 39].

### 7.3 Medication Deprescribing
Platforms like Virta and Twin Health have demonstrated that rigorous digital interventions can lead to significant deprescribing of insulin and other anti-diabetic medications. This "reversal" or "remission" outcome is a powerful metric of success that goes beyond simple HbA1c management [cite: 14, 42].

## 8. Future Directions

The future of balancing clinical monitoring with lifestyle guidance lies in increasing automation and personalization while reducing burden.
*   **AI Agents:** New tools like Omada's "OmadaSpark" use Generative AI to provide real-time, conversational support, potentially scaling the "human-like" coaching experience [cite: 43].
*   **Interoperability:** Better integration with Electronic Health Records (EHRs) will allow DHIs to function seamlessly within the broader healthcare ecosystem, reducing the fragmentation of care [cite: 44].
*   **Equity:** Addressing the "digital divide" is essential. Ensuring that older adults and those with lower digital literacy can access these tools requires simplified interfaces and robust technical support [cite: 3].

## 9. Conclusion

Digital health interventions for Type 2 diabetes achieve a balance between clinical HbA1c monitoring and remote lifestyle guidance by transforming static data into dynamic, actionable insights. Through the use of passive sensing, algorithmic triage, and hybrid human-AI coaching models, these platforms create a safety net that supports rather than stifles the patient.

The most successful interventions are those that minimize the "digital burden" of monitoring while maximizing the personalization of the guidance. By shifting the focus from "surveillance" to "support," and by leveraging behavioral motivators like gamification and medication elimination, DHIs can drive sustained adherence and significant clinical improvements. As technology evolves, the integration of Digital Twins and AI agents promises to further refine this balance, making precision diabetes management accessible, scalable, and sustainable.

## 10. Comparative Table of Intervention Strategies

| Platform | Primary Focus | Monitoring Mechanism | Guidance Strategy | Adherence Driver |
| :--- | :--- | :--- | :--- | :--- |
| **Livongo** | Empowerment & Safety | Connected Meter (Smart Cloud) | Algorithmic Nudges + Acute Human Outreach | Safety net (3-min call rule) & ease of supply ordering |
| **Omada** | Behavioral Change (DPP) | Connected Scale & Meter | Human Coach + Peer Groups + Curriculum | Relationship with coach & peer accountability |
| **Virta** | Disease Reversal | Biomarkers + Symptom Logging | Physician-led Deprescribing + Keto Nutrition | Motivation to stop medications (insulin/sulfonylureas) |
| **Twin Health** | Precision Metabolism | Multi-sensor (CGM, Activity) | AI "Digital Twin" + Precision Nutrition | Visualizing cause-and-effect (Metabolic Flexibility) |
| **Mebix** | Lifestyle Education | App-based Logging | Gamified Modules | Gamification elements (points, progress) |

## 11. References

*   **[cite: 1]** Calcium Health. (2023). How to Improve Diabetes Medication Adherence with Digital Health.
*   **[cite: 2]** PMC. (2025). Mechanisms of adherence in digital health for type 2 diabetes.
*   **[cite: 4]** African Journal of Diabetes Medicine. (2021). Effectiveness of digital health interventions for diabetes.
*   **[cite: 5]** PMC. (2025). Meta-analysis of digital health interventions for diabetes HbA1c.
*   **[cite: 20]** Dr. Shumard. Apps vs Coaching: Which Type 2 Diabetes Program Works.
*   **[cite: 14]** Contemporary Health. (2025). AI-Powered Precision Health and Lifestyle Coaching Improves Outcomes.
*   **[cite: 21]** Omada Health. (2020). Omada for Diabetes Program Achieves Key Clinical Outcomes.
*   **[cite: 16]** PMC. (2021). Livongo Diabetes Intervention Study of Patient Engagement.
*   **[cite: 15]** PMC. (2017). The Livongo for Diabetes Program: Clinical and Behavioral Outcomes.
*   **[cite: 26]** PMC. SidekickHealth digital lifestyle program outcomes.
*   **[cite: 28]** Twin Health. Twin Health Outperforms Traditional Care.
*   **[cite: 8]** PMC. (2025). Behavior change techniques in m-health apps.
*   **[cite: 6]** HTN. (2024). Research journal explores best behaviour change techniques.
*   **[cite: 32]** Virta Health. How It Works: Nutrition-First Approach.
*   **[cite: 24]** PMC. Gamification in chronic disease self-management.
*   **[cite: 3]** MDPI. (2023). Long-term adherence strategies in digital health.
*   **[cite: 9]** PubMed. (2024). Digital Medicine Tools and Treatment Burden.
*   **[cite: 36]** ResearchGate. What makes digital health intrusive?
*   **[cite: 33]** Virta Health. How Reversal Works: Nutritional Ketosis.
*   **[cite: 17]** Teladoc Health. Livongo for Diabetes User Guide.
*   **[cite: 29]** PMC. (2024). One-year outcomes of a digital twin intervention.
*   **[cite: 27]** Omada Health. Omada Product One Pagers.
*   **[cite: 23]** Imaginovation. (2021). Step-by-Step Guide to Health App Gamification.
*   **[cite: 34]** Virta Health. (2019). 4 Reasons Virta Achieves 90% Retention.

**Sources:**
1. [calciumhealth.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYkQX6Cdqpy6DjEPrZgz9NNCFgTmmg7vRIqng534QsoT1iXqyNpBMewyjQAVt5gTjn1L5d0SasARUH18lsSqwzNL-RT8cAWLqsw1GDyNrOWSzxT2l5d1kPT9wgAAWef0666DmIfPENm_mALNa3z2TwbceU7S60gQ1MKAYxt3PiOaIDBAXcDg-XCjShU6DYVuqU)
2. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuDltcpMxj44R-e1oRZXT5vn5WJ31iKVXZbsWuryG9BhxmRoUlrTJIm2WXPj_fFHrv0bKqiQjYWwTXTRFdNsIo7SANIo1qO00QTL9KBhSnpluQlofGxUgxcxgTjPibmm48oJ35uq9xqA==)
3. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2QosTzCdik2HpF10umbDO2PjkG4D5JzcL-id7JCJc1fvKvzu7Ofk1yCrLiuraSuRIDh0w1V6C1T5xO7r7m3M4_8GBfu0rqM0yCl68bRGVe_85Bmw9vK5wCFYl)
4. [africanjournalofdiabetesmedicine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHi15R80TH05ms6PPH1klETqPRPDzqyKi79k_9j5qqN4yIGHC0P878sipCYuP9BrlzC0cg7p0pi2N-SEFZ5flvKrO9m0-BgbRI6RA3Jn12Eh9IoutcqZ-8f7nxXM7ryh5fbCUrWiQDb2eZZWpsqP4Zv8LeOGlJhPOA8we9IRL226sXrT_KPICubkqK6LoKl50sGX_FTOuZN-ogk4LKmEdOpPD5QNRhU2o7VbsE2b6X3vKvNiP47k5xBY31eBmgSsWBSISNomOGF4OrdAg-W4z_1EjlOVJa7fUniRiKE1Bc=)
5. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzsS4N7HmZW8b_qs-qlKDJijiLjdtUGr0bx83xwDmU4RCWl1q41fuUo4A7OSdfWxkTNuLqWlGic131mhZAM2Dg5xAcbsIPUklFIW7uqdz2OdRPgyWF9qmtEysWrm6jIH1sRs6c4_kIjQ==)
6. [htn.co.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGe3mGt4NJm0Y96XpEG1PRNKHjXzsjqMiPD_hTCoafb1lluE0rIqIYX8KeVi1B6O5MpviPN8L5NDWMGxSn9HQDqWbctpFfchsGwqI6T_r1itESpEfiCWxLmyp3FtFm8T9NnxEO3uufuxJ7HbAFT3YpYjiiOGIwny9ZK4lVe-EGaWDlcqubi8DfG5g3s5FqvXQIisavfBaGJT7REDseZSDMIACmCG9VIM12319qgcaPcCzBoUHasW5lM)
7. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-F_xOPCBIhJaZr5oiPP-brmi9OAc-ZeuHRBssUoCJZVL1dcb6iYyu6IC8r8jS0IdPQWp48rfO9v8zLjgHZ_2rJjjJ3k9RIYz3xvWBc53Sy0WbdDWO3oAznT9br79jBQ==)
8. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrKygGOxX6rxHsdlxNzUdCbIMtaavSfE7HNnYQP-nu-daXGQ9eBVQItYbW0YQsHxNMZ-dnQjinfDXqYOKZ-jeVMBXzyfydeCZ7LVgi0_pncbtwu9Q4KDJtR9EPfHt3Nou5a1Cov_Gqmg==)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmBvaD9FlRin0h4IQnAYiIdDAfXZT4pTnlc_1a5AVV2IkEIbaA4jyU-GgvU5zSvCuMHGgfK_n4IFxQZY59ZEGqcq6S1tg5ZRB0ZDqtwyvX55AYnW6iTHU7pbupuTkBqw==)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJYori-SQP-gSy4bD7JtdYL1M-jtN25n3dxgtA_b0hyWR9RdaJOP-Q8kMJoN6_5iHCtJpzaAIYS-faNPuAKkPm-zCNhG3DD9KIN6qz_VUb5nV5fTsPsbQC3r2fFi0q8qa2YbR8PM_VO9sDOsVvS122st43wkg_yiA0KiPzheQOoe2YTTs2S8ssrTDnHV-doMy-mOhKqoSIkWcHJThHXap3bAuNQWzfxejmWa-XD9WoOonl_tzuqm3nh4hPkrFGNXkBmD22dUDXXwERuWEwG5wxIT21SkFuZAwntpn65y3pwQ1iWbdBAmGmb8L_VpifF_wUBQ==)
11. [teladochealth.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsBXpP0kFL6OzC64OBDr5CuAEoewwdY4JoKiEpvDbF04DzSiEF0WvnUnyfXmh3XSiRPWcoYeVlIfdWsG0767IADuzwOE2SQaE7ya-9vz-hGTVtlXcSy9GBlhDSC0TEi7fdUBLlhvsGFak=)
12. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSpkbLUJE7oUi6N78LzoyI4bka5k4mOrWeIpLzpOjclOuAEAQL4MF35RmWe7JRVbE4ErblmRMYaT1a7LiIntgEbJkduMTW357dupUtwXmnKgPnmDoSJ8zDm2QS89OooQ==)
13. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgUSw2pd1IApHJ1OgebI96qGqns7wv9jBw2ZDHHdQ0wbMNe3B8eaKyMGP7ZHsHH3ZxMfKXrutdeEe8zzEa_1tBpnlZSiHJtAJpIsvczRgzdo96Mzew7oY1d-i-TKzfJoTH5dOgwGeYTQ==)
14. [contemporaryhealth.co.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRqxzqHO4jV6tBQVmTHqJmnhbGAliNNycMJjVN_2MoBwkeYraKjJsZiYhbTSbBqpUIrpdqgXa_pnCAfhfJmw9tZp6esZ9xsfgE1NACmiRxxthwN0UVPF7p9flEQh8d9bJbA8yM4ARqaUJZZy8p8UKH-N6DpjaMr6zSwMbkqgVOo-tO21yskr_2ruseStiJsLlp6gIqYNym5-sLcs1jewrOu_3fkxdL8nzH3WeERlwi22BKSacZ5T5vKKz92tpt0N5YMzDJMwMGIaClXTiJX_a2jmYhOjkMM9EDf33ToKt6HedsvPT4ogKgb0uJol-pYAE=)
15. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg6RBxGeurCDqhFNABj5JQqAssxlBtIqxiiddpI3qunAlUvGomfcCkL__AcO2Se-sz8zEb9hbY62FGQ_tx3JYLOss3TPAYolmCm0pEVonZjudC-LOWw6NEhaXWqNqI38sqni2FY8-d)
16. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsvpagWFh6xzAeSeOQWzGqnDx_VD-oao7AA7ksPZdxejkA7vgRWNSYDw4aVFh_swFhmRqPg9VhPAWS6-ETZWTGM00GXSlZ70Amx2V9y7wBsnXHsVuCTkYHdeNpO6dnVnwV2lk-dnZJ)
17. [teladochealth.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfwcWf93iRugy9h3iFDLoGuWnaSPevnE25V8QyPIdi0Jhnw7sdvQWJdOAq_pz5scCOLrjnlB9ufbt1njp31p5NCI9rz2Olv-0XzxykowInRAPyo0EgJfasiiPUTlmuDxFyga92QftcsOVW7zmXtjhQDVjtMDu0QuQLDBTLKatDMvmQ6VR6WlKTTshG)
18. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtbREPxsE_Ebtxxq2B0Osut5zifuJcAz14GVmdqg1pYY4O6y1EFrWsbpzyC485b4mkYwM4r5w4nCVxBWU3nFxvEfJl7VW5f70iRKyms3q_qqciFe7aRFPEQ9iB7p8FTMT1z2U7sP8dMw==)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPTaWTZjomErxoaCgkLTn0wtmYrVyar3d6kwCm2s77UNpMNo8E8zRTt2ciKm3HxI6qEtsNDGnQSIwt9Co18w2vi__O6ZnevqpAkb0SdgmCzoNtsTkGUwq4fC5F-BlTzCBW1ypIzVQEEvqtkLS6CsXsvuUYbjLIA14mH2NBjNpZ7X9jszBIH30Nc9bHkn7d2eJzShzM9Vz_9tOgl3fJeEhFrgwjmgxtYm3IaYTBunJClDJQkvJt3FPEGYMKlOHFnpsygQ1zevjtcAlSmpiO2QYOcMoTE3SxPFZWo2D9uijzJavgd7OK)
20. [drshumard.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1ZQTTdDQcSOXQjtk6R7Ox0HwGSDGrt-_ZkS-KAIJ2ytcnZs_T474GIAu72ugEm7jFYXZDRV4kA9uI5GcVxFugzGzZox8SBfh2Dv_ck1EZSG3fLTfh-tUt-E2PKLTm2_PWxVwez4gEX92Nos2E2YuaZ7v_wlGlLnE5eirV0sLoLwA=)
21. [omadahealth.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRTLteKqKSALzdkypAnlEkYNcbbByHY4y1TKtLIDknGLDTZB7QG9rVlN8uroaj-Ra1qVlrLXb_qOh-V1E__QruDrw0iwsyHAjyGD0rxkG8lGCO5bU6tRwzEtZ9Di3cIDOQsQXV2lPbJ0SkQ29Yw1shgtt4s29weFZ_-tv-aDqB9vBZKVKXDRcSIX1z2aLbQ-egZe7OmIvNR5sv8A==)
22. [amazonaws.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHY9K1Mw7jiUWzT7JytBVB_TbRrOae1Oe1waPAGdO5BYSYa_Dwisw_o4FTWGcnQMctRiMDX3eDz1bzluqD5HLz4WHeFGO50g_LNdoxU_eQTKMN4zbEh8TQA7JV66WRIRw04jk8FOWHhm-PH6dXPBojWfkqNo1ZIFfje0Debyw0Bw4Bqev19PE_I4YIiLSsKiIyMxIjKrs9TCWiQexrnqXz5)
23. [imaginovation.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOliFHwK1vJI9a50fPRIinb6V2TJP-g8WD2MaQKJ17Rge7DMWp9m6SLUGaboVMnP4uM7EKBm8ZftQPh9YHbXLTaGd_zx0Eqa5VtL5_vIvw_zJ5X6ID65xItisrWm9Qbc4ZUhY6SRljs27-vvsC4WVRZ5OflCA2LQWcAXxxROUESBGyz4_0VCsxNPD_sZMf)
24. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuVTVIxeckN1AsCrgcBBtMsdyXwqs9U3ib-rcYMJvbeZjKjCAvkXgFM5rhrtg2qj-AOCn7xiRGGvV3HOH28Pd1vdwuElYfvgZxTOyfJ5HTxcc9qxo-8Gv6qRTFX63jQH4Y6Axof7Ccaw==)
25. [openloophealth.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwuUIZaeX7CFQHBuxW_qriT3dDJwP4mfg0OE0AwD_cYQIGdZ7UpqHEKkVQzcUH2_T2b3ihyPLK-Xs15W8jJ0OldSjSBXapkLlLTmXEkQxv1HpZ35JEEYBmwySI-KNJSIjbSOUGQRHeGyxqRpPzmc85dueFsR9BuPmZgrPWKd_5ZW3lI7q00wWn_tFZ-352-n4inOygoBQh)
26. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJS2kgKoUcNu8RyeSDCly-OmPwHqcCbMnzO756sBePWmxMp59j8eRndwo_phVZbZz6H5aRQBkCKwAdbI7HlK6ybrS0WsHEtmeFGNDVL0LHYOaazQ-LMqYkHNNpJmMlCe6ke9Xus5CF)
27. [finalsite.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9dQGEoS1Jg_89RsiWz8E-vDxhKCUkevDsZUJnfjIL7Od3ATZIcqZE7XrEkjjW6eht4mUjzD_KM3kbccrqMHZIvCo-mLH-_CSck4ChOWHXnnGsUpaOHOperqTuVtzZKagKvgBx8GTWsA4v2uT0cw12nuoLzW1GLxzqNpWqPvuOVF92aKjYJFzvAVzB6jnm1YgkjxD7H8n3xmB9iiosyLdmXwN2)
28. [twinhealth.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3w5rmU2_DBHJJuSF4buTEQSrZEiy_z7cAKPjMR-mjqL_EfMyiv5biHbpj2j4AKX5pjC8RBefjYBVfp_MvlweMJWZHunNdwaS_qQeej9lOJI8-P9fGWiXUDlUZrbSDGaKhcrR6V_EPI2rAPZKu4rKBOVJxqxwPgABzI2bN5Dhdizo9jQ8GYwC1MmHZm8D3V62qU1edeBsK1ljFOeaBpdfAgIKR3Qg_r5S4F9QoLq0DxxdjAZ9hfqXP51eeVjZACGmGFQ97ZYzyzsy72QkTWBLvwX9_0egi)
29. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8KMxgZb0dEmrV3ny1RxMCTefgGKpYi02oIWsAIWzcv2-s_MK2phmQWHvQ2IOhz2HDLuOpflK31h81gbnNMzzsfkoePHqmVxLZg5d5TXFds2NvyWPRoUv4FYUTN46UKuNNtbpgUk-VPA==)
30. [ajmc.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEB9K_60GeYk5rO_07zWNBsqWomVuUYVRjjq0Ug4HgA_l0mTBsoNR-BgE9mgu4P1Y3jDkwb_AI6MraVD4Fo6YHZEnf4ZdODj1PkOtq2ZB4pXDzEhNdPkwd3B0kzYlc2lZmuVCqD9_n3mB1ZpDGFfdFZBTsWCQ88KBQtHVkE8O7iJPeV38wpRnG4QqBQmVonyW5wFQBhR2Aywb-UQQ==)
31. [teladochealth.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFquq5tveT3WokGHNV4bATbGuilng4xiopsHtsFGMa7ZICghYF_b5Zfkn68gTpc2YRktITaRekjFebqMXqmvwZNQqlmhH-sC3kzDSgGkou0jKSJW0NI-6coZ7dQXei98a_7bg0K)
32. [virtahealth.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzh91fQKzj5eOzJlt28qx1uTVbQ6i0AqyWILJMMCg9RvPhxpUH6DS0AMMkAXZxX2ApapDUoL0OZ-8mb3QM7o_23DahiFidL3eKcqwr09E4F4n6k5QZesRmYdKqBxSM)
33. [virtahealth.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEENfnXNimDcoJlaGk76qmyh4rBtrxxrN_CpwRrFAMRprkzA2xzSUYjsuN8SAnNnFPfKOpllyVAIwocEJtIenBzXv29dRko3FQdacUisxdb8KAsQI_OaFuWunhZQV8sTo8o)
34. [virtahealth.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpiu31ry9v20egd7fpewXIYbGf-TRD8eFNDcfU4Xvn3Qf3Iw8o09UmXOC6xMAhlxZsk5AtX1UVut6ya1q0z4_MdI4FwsIiheTJkwSPcFAfv6TtiyLacOypOormJ73dOQy3RKkmdyZyeXk5r61EArkgN8yvUTlWF6ijvOsUeSSQ)
35. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDPZCnkW3Q2J1xZu9UBpIt3qdhAitGygxXUtVGPkKiHLbww7BIKhUrPbtTy_y3z_e8KlnWWnqHLtHCJv37aCnRSy78ATnnM8yJRIvSDtRhYE29HrvxqnMh3ZzTCqYaAIDfS1hULlUOcw==)
36. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQevdGoO5Z6JH5-bAgidRUsqIlV6x6WvZUTnpoUanXZx5K3W-4KO52UYOTXg5E29FtHc40Vq5eGN8k9mC8u3DHOIinzpW4p_VDnm1na_HslpQcQTgmzHGLU36rxOVgWWvQ7uPVZ5FONGJi43AtIG-d7YvdY_gSWFfFNsOpbsQCvUOdi_j1T6otWMHK1tfE9vdkv8OgMzazEOGe8QtUB5clv7yWWwEGu3mV5ZJudL-MhEwT_bjem2YD2Czia-rCTsAOaKgjV6iog2LG)
37. [medicine20.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTwzGdaSohyJuGPNvl3Y4xeROyWRDQoW5u5tEYaLoZWbm3vRnxgSuYFdhSFAYvKqfmZ_XC46khRiy8_1XNo23d7LRovnIXam8OKMUJnG0NWt805OJ4BOspouo=)
38. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHASwtFc-a3LIT0IOUTVAjureCZF8U_ke3nrq7tlZTo_uKwm-EVJEqmIrvzIr7cjpFOWWGRH_9LnmJNTnMMEtPZM7JjrxGNH3e4zbrM25Kr_HTJhvNrZxgyULYaok43jcuyprGx56Xa7cHGmTQECXAwS2673b_Cs6kvRuFzceigFEzpgrwF8iwyvuGBKz2Vtx8tvt1YFMDZhyDMdqrLzffGm2r4OdlmyoLxWam8iF-YDZzIk4FGyLOMT-088ltsu0f_7aBOIw2nV8u6kGGx9aOU2LJf8vgi-vfVU1UR6Ps=)
39. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPuKsGJmXy9ZmABzeOthxh5VAWhVrbk_1gnKhFcOR05EBubrJfihjmP2jx6Qwv6ahw6cUnUeeWziSwWENPgRmVcakpl65z68wv476u5Vfmx2oiszUIqemCAYSjsAhgS5joqgthjFrJfs1eDrvfk-li11zxjdgmkD6mDLBhzx3Suj4Q_wT_LYKrU0c3WZkBz0TaVBc4D_SzVw48O2-obW6QHaqR)
40. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8VpMT96T2tG62VApxWNiZWIPGIj8Dj0ES10rgPnTWuyA6kuo2Kbqm87iDMO8gxGIJMa0HI47VXJq57fiq_jlNl5O6cBn5sM8MovkMGmruJMNbGY0eiDk6lC9Al7NR2g==)
41. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFvsLsjdEVP0Y5RXJAbiX2Hw0J9wRbYbwRQX4U4Ys4ObsncSW9p73ruxEFnJa6Jj-e3n1FjF32ElRxpdfbMEivFi0vP_St0_C8kRohUPeP2dogxToVnYHDozoaC6Oxej9CFZE8IAKeBg==)
42. [virtahealth.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBhHFAiU-21J3JyRb7jssIfH0LCtMtNyr1ci8PgaRdmcXi12JvtaS_wGTUi-50CG7xBY_3Zz-0Aajie628NUqS4OpkK-mmZSUzHxotvMbPc0mlkcrIxZS7Q3gslkDjXYCcbiRtpV34pIqqiiJZ1sPw3VZK6gI_xOOFUmpYymQLJmQZEG6o8etFDkzAQUfhKN1U5RCUqgabO8B8fZo5fmhnJHF-OxbY47BCmsy3-26_lQISWrTwQbqd8oCdq3RzaE0g6Z4L1n9yVvgUdv54nfd8)
43. [omadahealth.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjboFJFp4b_7KPWaxYOijckboJQJIPR1XKa6lSKpv-vYZyt7gfqNkwIIR1e_cbWUlFqSUN1ZdwE2_lmxMU6inktJRraF_RH3GSdrY7Zfa_LPe45ILPBuEu0e6qaBQvHZ10ebx_ju9kAYk6knkXKKTZIqPjZO54qU1Xlx8TvZIW-UX-Fq_jXbHrC37J4mVD9Xz96yg-6a1E4d-JNKkqXMBvi5bjshaVgIHMyd6xhFEPy7pcANnrjxmeAv_bAyLA7pIYBEPPn8RXsF4NJvCn3nAa)
44. [ama-assn.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsR9Q9cGd3_rFaau2pyt3ghg5DC5nrGKjm6KUwBeApPe8gqj2F0z06vTLGRs-hVM2sAuLOprU8yjf7CGrgrWMwaNjwMxtAwjCymSX54z4suANUjqOoInaTO0vZSzPTRCRTsPIRCAwhWfTYXZ37SQCIK_vO6hyqJbDuHyRovenHge3H7aGJ)


## Annotations
Annotation(end_index=3825, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYkQX6Cdqpy6DjEPrZgz9NNCFgTmmg7vRIqng534QsoT1iXqyNpBMewyjQAVt5gTjn1L5d0SasARUH18lsSqwzNL-RT8cAWLqsw1GDyNrOWSzxT2l5d1kPT9wgAAWef0666DmIfPENm_mALNa3z2TwbceU7S60gQ1MKAYxt3PiOaIDBAXcDg-XCjShU6DYVuqU', start_index=3813)
Annotation(end_index=3825, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuDltcpMxj44R-e1oRZXT5vn5WJ31iKVXZbsWuryG9BhxmRoUlrTJIm2WXPj_fFHrv0bKqiQjYWwTXTRFdNsIo7SANIo1qO00QTL9KBhSnpluQlofGxUgxcxgTjPibmm48oJ35uq9xqA==', start_index=3813)
Annotation(end_index=4997, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2QosTzCdik2HpF10umbDO2PjkG4D5JzcL-id7JCJc1fvKvzu7Ofk1yCrLiuraSuRIDh0w1V6C1T5xO7r7m3M4_8GBfu0rqM0yCl68bRGVe_85Bmw9vK5wCFYl', start_index=4988)
Annotation(end_index=5343, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzsS4N7HmZW8b_qs-qlKDJijiLjdtUGr0bx83xwDmU4RCWl1q41fuUo4A7OSdfWxkTNuLqWlGic131mhZAM2Dg5xAcbsIPUklFIW7uqdz2OdRPgyWF9qmtEysWrm6jIH1sRs6c4_kIjQ==', start_index=5331)
Annotation(end_index=5343, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHi15R80TH05ms6PPH1klETqPRPDzqyKi79k_9j5qqN4yIGHC0P878sipCYuP9BrlzC0cg7p0pi2N-SEFZ5flvKrO9m0-BgbRI6RA3Jn12Eh9IoutcqZ-8f7nxXM7ryh5fbCUrWiQDb2eZZWpsqP4Zv8LeOGlJhPOA8we9IRL226sXrT_KPICubkqK6LoKl50sGX_FTOuZN-ogk4LKmEdOpPD5QNRhU2o7VbsE2b6X3vKvNiP47k5xBY31eBmgSsWBSISNomOGF4OrdAg-W4z_1EjlOVJa7fUniRiKE1Bc=', start_index=5331)
Annotation(end_index=6039, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-F_xOPCBIhJaZr5oiPP-brmi9OAc-ZeuHRBssUoCJZVL1dcb6iYyu6IC8r8jS0IdPQWp48rfO9v8zLjgHZ_2rJjjJ3k9RIYz3xvWBc53Sy0WbdDWO3oAznT9br79jBQ==', start_index=6027)
Annotation(end_index=6039, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGe3mGt4NJm0Y96XpEG1PRNKHjXzsjqMiPD_hTCoafb1lluE0rIqIYX8KeVi1B6O5MpviPN8L5NDWMGxSn9HQDqWbctpFfchsGwqI6T_r1itESpEfiCWxLmyp3FtFm8T9NnxEO3uufuxJ7HbAFT3YpYjiiOGIwny9ZK4lVe-EGaWDlcqubi8DfG5g3s5FqvXQIisavfBaGJT7REDseZSDMIACmCG9VIM12319qgcaPcCzBoUHasW5lM', start_index=6027)
Annotation(end_index=6540, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrKygGOxX6rxHsdlxNzUdCbIMtaavSfE7HNnYQP-nu-daXGQ9eBVQItYbW0YQsHxNMZ-dnQjinfDXqYOKZ-jeVMBXzyfydeCZ7LVgi0_pncbtwu9Q4KDJtR9EPfHt3Nou5a1Cov_Gqmg==', start_index=6531)
Annotation(end_index=6798, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrKygGOxX6rxHsdlxNzUdCbIMtaavSfE7HNnYQP-nu-daXGQ9eBVQItYbW0YQsHxNMZ-dnQjinfDXqYOKZ-jeVMBXzyfydeCZ7LVgi0_pncbtwu9Q4KDJtR9EPfHt3Nou5a1Cov_Gqmg==', start_index=6789)
Annotation(end_index=7247, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJYori-SQP-gSy4bD7JtdYL1M-jtN25n3dxgtA_b0hyWR9RdaJOP-Q8kMJoN6_5iHCtJpzaAIYS-faNPuAKkPm-zCNhG3DD9KIN6qz_VUb5nV5fTsPsbQC3r2fFi0q8qa2YbR8PM_VO9sDOsVvS122st43wkg_yiA0KiPzheQOoe2YTTs2S8ssrTDnHV-doMy-mOhKqoSIkWcHJThHXap3bAuNQWzfxejmWa-XD9WoOonl_tzuqm3nh4hPkrFGNXkBmD22dUDXXwERuWEwG5wxIT21SkFuZAwntpn65y3pwQ1iWbdBAmGmb8L_VpifF_wUBQ==', start_index=7234)
Annotation(end_index=7247, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmBvaD9FlRin0h4IQnAYiIdDAfXZT4pTnlc_1a5AVV2IkEIbaA4jyU-GgvU5zSvCuMHGgfK_n4IFxQZY59ZEGqcq6S1tg5ZRB0ZDqtwyvX55AYnW6iTHU7pbupuTkBqw==', start_index=7234)
Annotation(end_index=8235, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsBXpP0kFL6OzC64OBDr5CuAEoewwdY4JoKiEpvDbF04DzSiEF0WvnUnyfXmh3XSiRPWcoYeVlIfdWsG0767IADuzwOE2SQaE7ya-9vz-hGTVtlXcSy9GBlhDSC0TEi7fdUBLlhvsGFak=', start_index=8222)
Annotation(end_index=8235, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYkQX6Cdqpy6DjEPrZgz9NNCFgTmmg7vRIqng534QsoT1iXqyNpBMewyjQAVt5gTjn1L5d0SasARUH18lsSqwzNL-RT8cAWLqsw1GDyNrOWSzxT2l5d1kPT9wgAAWef0666DmIfPENm_mALNa3z2TwbceU7S60gQ1MKAYxt3PiOaIDBAXcDg-XCjShU6DYVuqU', start_index=8222)
Annotation(end_index=8614, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSpkbLUJE7oUi6N78LzoyI4bka5k4mOrWeIpLzpOjclOuAEAQL4MF35RmWe7JRVbE4ErblmRMYaT1a7LiIntgEbJkduMTW357dupUtwXmnKgPnmDoSJ8zDm2QS89OooQ==', start_index=8600)
Annotation(end_index=8614, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgUSw2pd1IApHJ1OgebI96qGqns7wv9jBw2ZDHHdQ0wbMNe3B8eaKyMGP7ZHsHH3ZxMfKXrutdeEe8zzEa_1tBpnlZSiHJtAJpIsvczRgzdo96Mzew7oY1d-i-TKzfJoTH5dOgwGeYTQ==', start_index=8600)
Annotation(end_index=8901, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRqxzqHO4jV6tBQVmTHqJmnhbGAliNNycMJjVN_2MoBwkeYraKjJsZiYhbTSbBqpUIrpdqgXa_pnCAfhfJmw9tZp6esZ9xsfgE1NACmiRxxthwN0UVPF7p9flEQh8d9bJbA8yM4ARqaUJZZy8p8UKH-N6DpjaMr6zSwMbkqgVOo-tO21yskr_2ruseStiJsLlp6gIqYNym5-sLcs1jewrOu_3fkxdL8nzH3WeERlwi22BKSacZ5T5vKKz92tpt0N5YMzDJMwMGIaClXTiJX_a2jmYhOjkMM9EDf33ToKt6HedsvPT4ogKgb0uJol-pYAE=', start_index=8888)
Annotation(end_index=8901, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYkQX6Cdqpy6DjEPrZgz9NNCFgTmmg7vRIqng534QsoT1iXqyNpBMewyjQAVt5gTjn1L5d0SasARUH18lsSqwzNL-RT8cAWLqsw1GDyNrOWSzxT2l5d1kPT9wgAAWef0666DmIfPENm_mALNa3z2TwbceU7S60gQ1MKAYxt3PiOaIDBAXcDg-XCjShU6DYVuqU', start_index=8888)
Annotation(end_index=9644, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg6RBxGeurCDqhFNABj5JQqAssxlBtIqxiiddpI3qunAlUvGomfcCkL__AcO2Se-sz8zEb9hbY62FGQ_tx3JYLOss3TPAYolmCm0pEVonZjudC-LOWw6NEhaXWqNqI38sqni2FY8-d', start_index=9634)
Annotation(end_index=10013, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsvpagWFh6xzAeSeOQWzGqnDx_VD-oao7AA7ksPZdxejkA7vgRWNSYDw4aVFh_swFhmRqPg9VhPAWS6-ETZWTGM00GXSlZ70Amx2V9y7wBsnXHsVuCTkYHdeNpO6dnVnwV2lk-dnZJ', start_index=9999)
Annotation(end_index=10013, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfwcWf93iRugy9h3iFDLoGuWnaSPevnE25V8QyPIdi0Jhnw7sdvQWJdOAq_pz5scCOLrjnlB9ufbt1njp31p5NCI9rz2Olv-0XzxykowInRAPyo0EgJfasiiPUTlmuDxFyga92QftcsOVW7zmXtjhQDVjtMDu0QuQLDBTLKatDMvmQ6VR6WlKTTshG', start_index=9999)
Annotation(end_index=10712, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg6RBxGeurCDqhFNABj5JQqAssxlBtIqxiiddpI3qunAlUvGomfcCkL__AcO2Se-sz8zEb9hbY62FGQ_tx3JYLOss3TPAYolmCm0pEVonZjudC-LOWw6NEhaXWqNqI38sqni2FY8-d', start_index=10702)
Annotation(end_index=10930, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtbREPxsE_Ebtxxq2B0Osut5zifuJcAz14GVmdqg1pYY4O6y1EFrWsbpzyC485b4mkYwM4r5w4nCVxBWU3nFxvEfJl7VW5f70iRKyms3q_qqciFe7aRFPEQ9iB7p8FTMT1z2U7sP8dMw==', start_index=10920)
Annotation(end_index=11111, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPTaWTZjomErxoaCgkLTn0wtmYrVyar3d6kwCm2s77UNpMNo8E8zRTt2ciKm3HxI6qEtsNDGnQSIwt9Co18w2vi__O6ZnevqpAkb0SdgmCzoNtsTkGUwq4fC5F-BlTzCBW1ypIzVQEEvqtkLS6CsXsvuUYbjLIA14mH2NBjNpZ7X9jszBIH30Nc9bHkn7d2eJzShzM9Vz_9tOgl3fJeEhFrgwjmgxtYm3IaYTBunJClDJQkvJt3FPEGYMKlOHFnpsygQ1zevjtcAlSmpiO2QYOcMoTE3SxPFZWo2D9uijzJavgd7OK', start_index=11101)
Annotation(end_index=11797, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRTLteKqKSALzdkypAnlEkYNcbbByHY4y1TKtLIDknGLDTZB7QG9rVlN8uroaj-Ra1qVlrLXb_qOh-V1E__QruDrw0iwsyHAjyGD0rxkG8lGCO5bU6tRwzEtZ9Di3cIDOQsQXV2lPbJ0SkQ29Yw1shgtt4s29weFZ_-tv-aDqB9vBZKVKXDRcSIX1z2aLbQ-egZe7OmIvNR5sv8A==', start_index=11783)
Annotation(end_index=11797, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1ZQTTdDQcSOXQjtk6R7Ox0HwGSDGrt-_ZkS-KAIJ2ytcnZs_T474GIAu72ugEm7jFYXZDRV4kA9uI5GcVxFugzGzZox8SBfh2Dv_ck1EZSG3fLTfh-tUt-E2PKLTm2_PWxVwez4gEX92Nos2E2YuaZ7v_wlGlLnE5eirV0sLoLwA=', start_index=11783)
Annotation(end_index=12167, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRTLteKqKSALzdkypAnlEkYNcbbByHY4y1TKtLIDknGLDTZB7QG9rVlN8uroaj-Ra1qVlrLXb_qOh-V1E__QruDrw0iwsyHAjyGD0rxkG8lGCO5bU6tRwzEtZ9Di3cIDOQsQXV2lPbJ0SkQ29Yw1shgtt4s29weFZ_-tv-aDqB9vBZKVKXDRcSIX1z2aLbQ-egZe7OmIvNR5sv8A==', start_index=12153)
Annotation(end_index=12167, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHY9K1Mw7jiUWzT7JytBVB_TbRrOae1Oe1waPAGdO5BYSYa_Dwisw_o4FTWGcnQMctRiMDX3eDz1bzluqD5HLz4WHeFGO50g_LNdoxU_eQTKMN4zbEh8TQA7JV66WRIRw04jk8FOWHhm-PH6dXPBojWfkqNo1ZIFfje0Debyw0Bw4Bqev19PE_I4YIiLSsKiIyMxIjKrs9TCWiQexrnqXz5', start_index=12153)
Annotation(end_index=12604, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOliFHwK1vJI9a50fPRIinb6V2TJP-g8WD2MaQKJ17Rge7DMWp9m6SLUGaboVMnP4uM7EKBm8ZftQPh9YHbXLTaGd_zx0Eqa5VtL5_vIvw_zJ5X6ID65xItisrWm9Qbc4ZUhY6SRljs27-vvsC4WVRZ5OflCA2LQWcAXxxROUESBGyz4_0VCsxNPD_sZMf', start_index=12594)
Annotation(end_index=12759, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuVTVIxeckN1AsCrgcBBtMsdyXwqs9U3ib-rcYMJvbeZjKjCAvkXgFM5rhrtg2qj-AOCn7xiRGGvV3HOH28Pd1vdwuElYfvgZxTOyfJ5HTxcc9qxo-8Gv6qRTFX63jQH4Y6Axof7Ccaw==', start_index=12745)
Annotation(end_index=12759, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwuUIZaeX7CFQHBuxW_qriT3dDJwP4mfg0OE0AwD_cYQIGdZ7UpqHEKkVQzcUH2_T2b3ihyPLK-Xs15W8jJ0OldSjSBXapkLlLTmXEkQxv1HpZ35JEEYBmwySI-KNJSIjbSOUGQRHeGyxqRpPzmc85dueFsR9BuPmZgrPWKd_5ZW3lI7q00wWn_tFZ-352-n4inOygoBQh', start_index=12745)
Annotation(end_index=12915, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJS2kgKoUcNu8RyeSDCly-OmPwHqcCbMnzO756sBePWmxMp59j8eRndwo_phVZbZz6H5aRQBkCKwAdbI7HlK6ybrS0WsHEtmeFGNDVL0LHYOaazQ-LMqYkHNNpJmMlCe6ke9Xus5CF', start_index=12905)
Annotation(end_index=13188, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9dQGEoS1Jg_89RsiWz8E-vDxhKCUkevDsZUJnfjIL7Od3ATZIcqZE7XrEkjjW6eht4mUjzD_KM3kbccrqMHZIvCo-mLH-_CSck4ChOWHXnnGsUpaOHOperqTuVtzZKagKvgBx8GTWsA4v2uT0cw12nuoLzW1GLxzqNpWqPvuOVF92aKjYJFzvAVzB6jnm1YgkjxD7H8n3xmB9iiosyLdmXwN2', start_index=13174)
Annotation(end_index=13188, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHY9K1Mw7jiUWzT7JytBVB_TbRrOae1Oe1waPAGdO5BYSYa_Dwisw_o4FTWGcnQMctRiMDX3eDz1bzluqD5HLz4WHeFGO50g_LNdoxU_eQTKMN4zbEh8TQA7JV66WRIRw04jk8FOWHhm-PH6dXPBojWfkqNo1ZIFfje0Debyw0Bw4Bqev19PE_I4YIiLSsKiIyMxIjKrs9TCWiQexrnqXz5', start_index=13174)
Annotation(end_index=14118, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8KMxgZb0dEmrV3ny1RxMCTefgGKpYi02oIWsAIWzcv2-s_MK2phmQWHvQ2IOhz2HDLuOpflK31h81gbnNMzzsfkoePHqmVxLZg5d5TXFds2NvyWPRoUv4FYUTN46UKuNNtbpgUk-VPA==', start_index=14100)
Annotation(end_index=14118, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3w5rmU2_DBHJJuSF4buTEQSrZEiy_z7cAKPjMR-mjqL_EfMyiv5biHbpj2j4AKX5pjC8RBefjYBVfp_MvlweMJWZHunNdwaS_qQeej9lOJI8-P9fGWiXUDlUZrbSDGaKhcrR6V_EPI2rAPZKu4rKBOVJxqxwPgABzI2bN5Dhdizo9jQ8GYwC1MmHZm8D3V62qU1edeBsK1ljFOeaBpdfAgIKR3Qg_r5S4F9QoLq0DxxdjAZ9hfqXP51eeVjZACGmGFQ97ZYzyzsy72QkTWBLvwX9_0egi', start_index=14100)
Annotation(end_index=14118, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRqxzqHO4jV6tBQVmTHqJmnhbGAliNNycMJjVN_2MoBwkeYraKjJsZiYhbTSbBqpUIrpdqgXa_pnCAfhfJmw9tZp6esZ9xsfgE1NACmiRxxthwN0UVPF7p9flEQh8d9bJbA8yM4ARqaUJZZy8p8UKH-N6DpjaMr6zSwMbkqgVOo-tO21yskr_2ruseStiJsLlp6gIqYNym5-sLcs1jewrOu_3fkxdL8nzH3WeERlwi22BKSacZ5T5vKKz92tpt0N5YMzDJMwMGIaClXTiJX_a2jmYhOjkMM9EDf33ToKt6HedsvPT4ogKgb0uJol-pYAE=', start_index=14100)
Annotation(end_index=15073, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRTLteKqKSALzdkypAnlEkYNcbbByHY4y1TKtLIDknGLDTZB7QG9rVlN8uroaj-Ra1qVlrLXb_qOh-V1E__QruDrw0iwsyHAjyGD0rxkG8lGCO5bU6tRwzEtZ9Di3cIDOQsQXV2lPbJ0SkQ29Yw1shgtt4s29weFZ_-tv-aDqB9vBZKVKXDRcSIX1z2aLbQ-egZe7OmIvNR5sv8A==', start_index=15059)
Annotation(end_index=15073, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9dQGEoS1Jg_89RsiWz8E-vDxhKCUkevDsZUJnfjIL7Od3ATZIcqZE7XrEkjjW6eht4mUjzD_KM3kbccrqMHZIvCo-mLH-_CSck4ChOWHXnnGsUpaOHOperqTuVtzZKagKvgBx8GTWsA4v2uT0cw12nuoLzW1GLxzqNpWqPvuOVF92aKjYJFzvAVzB6jnm1YgkjxD7H8n3xmB9iiosyLdmXwN2', start_index=15059)
Annotation(end_index=15512, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEB9K_60GeYk5rO_07zWNBsqWomVuUYVRjjq0Ug4HgA_l0mTBsoNR-BgE9mgu4P1Y3jDkwb_AI6MraVD4Fo6YHZEnf4ZdODj1PkOtq2ZB4pXDzEhNdPkwd3B0kzYlc2lZmuVCqD9_n3mB1ZpDGFfdFZBTsWCQ88KBQtHVkE8O7iJPeV38wpRnG4QqBQmVonyW5wFQBhR2Aywb-UQQ==', start_index=15498)
Annotation(end_index=15512, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsBXpP0kFL6OzC64OBDr5CuAEoewwdY4JoKiEpvDbF04DzSiEF0WvnUnyfXmh3XSiRPWcoYeVlIfdWsG0767IADuzwOE2SQaE7ya-9vz-hGTVtlXcSy9GBlhDSC0TEi7fdUBLlhvsGFak=', start_index=15498)
Annotation(end_index=15732, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsvpagWFh6xzAeSeOQWzGqnDx_VD-oao7AA7ksPZdxejkA7vgRWNSYDw4aVFh_swFhmRqPg9VhPAWS6-ETZWTGM00GXSlZ70Amx2V9y7wBsnXHsVuCTkYHdeNpO6dnVnwV2lk-dnZJ', start_index=15718)
Annotation(end_index=15732, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFquq5tveT3WokGHNV4bATbGuilng4xiopsHtsFGMa7ZICghYF_b5Zfkn68gTpc2YRktITaRekjFebqMXqmvwZNQqlmhH-sC3kzDSgGkou0jKSJW0NI-6coZ7dQXei98a_7bg0K', start_index=15718)
Annotation(end_index=16522, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEENfnXNimDcoJlaGk76qmyh4rBtrxxrN_CpwRrFAMRprkzA2xzSUYjsuN8SAnNnFPfKOpllyVAIwocEJtIenBzXv29dRko3FQdacUisxdb8KAsQI_OaFuWunhZQV8sTo8o', start_index=16504)
Annotation(end_index=16522, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpiu31ry9v20egd7fpewXIYbGf-TRD8eFNDcfU4Xvn3Qf3Iw8o09UmXOC6xMAhlxZsk5AtX1UVut6ya1q0z4_MdI4FwsIiheTJkwSPcFAfv6TtiyLacOypOormJ73dOQy3RKkmdyZyeXk5r61EArkgN8yvUTlWF6ijvOsUeSSQ', start_index=16504)
Annotation(end_index=16522, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzh91fQKzj5eOzJlt28qx1uTVbQ6i0AqyWILJMMCg9RvPhxpUH6DS0AMMkAXZxX2ApapDUoL0OZ-8mb3QM7o_23DahiFidL3eKcqwr09E4F4n6k5QZesRmYdKqBxSM', start_index=16504)
Annotation(end_index=17117, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8KMxgZb0dEmrV3ny1RxMCTefgGKpYi02oIWsAIWzcv2-s_MK2phmQWHvQ2IOhz2HDLuOpflK31h81gbnNMzzsfkoePHqmVxLZg5d5TXFds2NvyWPRoUv4FYUTN46UKuNNtbpgUk-VPA==', start_index=17103)
Annotation(end_index=17117, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGDPZCnkW3Q2J1xZu9UBpIt3qdhAitGygxXUtVGPkKiHLbww7BIKhUrPbtTy_y3z_e8KlnWWnqHLtHCJv37aCnRSy78ATnnM8yJRIvSDtRhYE29HrvxqnMh3ZzTCqYaAIDfS1hULlUOcw==', start_index=17103)
Annotation(end_index=17645, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmBvaD9FlRin0h4IQnAYiIdDAfXZT4pTnlc_1a5AVV2IkEIbaA4jyU-GgvU5zSvCuMHGgfK_n4IFxQZY59ZEGqcq6S1tg5ZRB0ZDqtwyvX55AYnW6iTHU7pbupuTkBqw==', start_index=17636)
Annotation(end_index=17978, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQevdGoO5Z6JH5-bAgidRUsqIlV6x6WvZUTnpoUanXZx5K3W-4KO52UYOTXg5E29FtHc40Vq5eGN8k9mC8u3DHOIinzpW4p_VDnm1na_HslpQcQTgmzHGLU36rxOVgWWvQ7uPVZ5FONGJi43AtIG-d7YvdY_gSWFfFNsOpbsQCvUOdi_j1T6otWMHK1tfE9vdkv8OgMzazEOGe8QtUB5clv7yWWwEGu3mV5ZJudL-MhEwT_bjem2YD2Czia-rCTsAOaKgjV6iog2LG', start_index=17968)
Annotation(end_index=18314, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHASwtFc-a3LIT0IOUTVAjureCZF8U_ke3nrq7tlZTo_uKwm-EVJEqmIrvzIr7cjpFOWWGRH_9LnmJNTnMMEtPZM7JjrxGNH3e4zbrM25Kr_HTJhvNrZxgyULYaok43jcuyprGx56Xa7cHGmTQECXAwS2673b_Cs6kvRuFzceigFEzpgrwF8iwyvuGBKz2Vtx8tvt1YFMDZhyDMdqrLzffGm2r4OdlmyoLxWam8iF-YDZzIk4FGyLOMT-088ltsu0f_7aBOIw2nV8u6kGGx9aOU2LJf8vgi-vfVU1UR6Ps=', start_index=18300)
Annotation(end_index=18314, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTwzGdaSohyJuGPNvl3Y4xeROyWRDQoW5u5tEYaLoZWbm3vRnxgSuYFdhSFAYvKqfmZ_XC46khRiy8_1XNo23d7LRovnIXam8OKMUJnG0NWt805OJ4BOspouo=', start_index=18300)
Annotation(end_index=18526, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGe3mGt4NJm0Y96XpEG1PRNKHjXzsjqMiPD_hTCoafb1lluE0rIqIYX8KeVi1B6O5MpviPN8L5NDWMGxSn9HQDqWbctpFfchsGwqI6T_r1itESpEfiCWxLmyp3FtFm8T9NnxEO3uufuxJ7HbAFT3YpYjiiOGIwny9ZK4lVe-EGaWDlcqubi8DfG5g3s5FqvXQIisavfBaGJT7REDseZSDMIACmCG9VIM12319qgcaPcCzBoUHasW5lM', start_index=18517)
Annotation(end_index=18943, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8VpMT96T2tG62VApxWNiZWIPGIj8Dj0ES10rgPnTWuyA6kuo2Kbqm87iDMO8gxGIJMa0HI47VXJq57fiq_jlNl5O6cBn5sM8MovkMGmruJMNbGY0eiDk6lC9Al7NR2g==', start_index=18926)
Annotation(end_index=18943, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPuKsGJmXy9ZmABzeOthxh5VAWhVrbk_1gnKhFcOR05EBubrJfihjmP2jx6Qwv6ahw6cUnUeeWziSwWENPgRmVcakpl65z68wv476u5Vfmx2oiszUIqemCAYSjsAhgS5joqgthjFrJfs1eDrvfk-li11zxjdgmkD6mDLBhzx3Suj4Q_wT_LYKrU0c3WZkBz0TaVBc4D_SzVw48O2-obW6QHaqR', start_index=18926)
Annotation(end_index=18943, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzsS4N7HmZW8b_qs-qlKDJijiLjdtUGr0bx83xwDmU4RCWl1q41fuUo4A7OSdfWxkTNuLqWlGic131mhZAM2Dg5xAcbsIPUklFIW7uqdz2OdRPgyWF9qmtEysWrm6jIH1sRs6c4_kIjQ==', start_index=18926)
Annotation(end_index=19544, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFvsLsjdEVP0Y5RXJAbiX2Hw0J9wRbYbwRQX4U4Ys4ObsncSW9p73ruxEFnJa6Jj-e3n1FjF32ElRxpdfbMEivFi0vP_St0_C8kRohUPeP2dogxToVnYHDozoaC6Oxej9CFZE8IAKeBg==', start_index=19534)
Annotation(end_index=19746, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPuKsGJmXy9ZmABzeOthxh5VAWhVrbk_1gnKhFcOR05EBubrJfihjmP2jx6Qwv6ahw6cUnUeeWziSwWENPgRmVcakpl65z68wv476u5Vfmx2oiszUIqemCAYSjsAhgS5joqgthjFrJfs1eDrvfk-li11zxjdgmkD6mDLBhzx3Suj4Q_wT_LYKrU0c3WZkBz0TaVBc4D_SzVw48O2-obW6QHaqR', start_index=19736)
Annotation(end_index=20085, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBhHFAiU-21J3JyRb7jssIfH0LCtMtNyr1ci8PgaRdmcXi12JvtaS_wGTUi-50CG7xBY_3Zz-0Aajie628NUqS4OpkK-mmZSUzHxotvMbPc0mlkcrIxZS7Q3gslkDjXYCcbiRtpV34pIqqiiJZ1sPw3VZK6gI_xOOFUmpYymQLJmQZEG6o8etFDkzAQUfhKN1U5RCUqgabO8B8fZo5fmhnJHF-OxbY47BCmsy3-26_lQISWrTwQbqd8oCdq3RzaE0g6Z4L1n9yVvgUdv54nfd8', start_index=20071)
Annotation(end_index=20085, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRqxzqHO4jV6tBQVmTHqJmnhbGAliNNycMJjVN_2MoBwkeYraKjJsZiYhbTSbBqpUIrpdqgXa_pnCAfhfJmw9tZp6esZ9xsfgE1NACmiRxxthwN0UVPF7p9flEQh8d9bJbA8yM4ARqaUJZZy8p8UKH-N6DpjaMr6zSwMbkqgVOo-tO21yskr_2ruseStiJsLlp6gIqYNym5-sLcs1jewrOu_3fkxdL8nzH3WeERlwi22BKSacZ5T5vKKz92tpt0N5YMzDJMwMGIaClXTiJX_a2jmYhOjkMM9EDf33ToKt6HedsvPT4ogKgb0uJol-pYAE=', start_index=20071)
Annotation(end_index=20440, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjboFJFp4b_7KPWaxYOijckboJQJIPR1XKa6lSKpv-vYZyt7gfqNkwIIR1e_cbWUlFqSUN1ZdwE2_lmxMU6inktJRraF_RH3GSdrY7Zfa_LPe45ILPBuEu0e6qaBQvHZ10ebx_ju9kAYk6knkXKKTZIqPjZO54qU1Xlx8TvZIW-UX-Fq_jXbHrC37J4mVD9Xz96yg-6a1E4d-JNKkqXMBvi5bjshaVgIHMyd6xhFEPy7pcANnrjxmeAv_bAyLA7pIYBEPPn8RXsF4NJvCn3nAa', start_index=20430)
Annotation(end_index=20650, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsR9Q9cGd3_rFaau2pyt3ghg5DC5nrGKjm6KUwBeApPe8gqj2F0z06vTLGRs-hVM2sAuLOprU8yjf7CGrgrWMwaNjwMxtAwjCymSX54z4suANUjqOoInaTO0vZSzPTRCRTsPIRCAwhWfTYXZ37SQCIK_vO6hyqJbDuHyRovenHge3H7aGJ', start_index=20640)
Annotation(end_index=20871, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2QosTzCdik2HpF10umbDO2PjkG4D5JzcL-id7JCJc1fvKvzu7Ofk1yCrLiuraSuRIDh0w1V6C1T5xO7r7m3M4_8GBfu0rqM0yCl68bRGVe_85Bmw9vK5wCFYl', start_index=20862)
Annotation(end_index=22814, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYkQX6Cdqpy6DjEPrZgz9NNCFgTmmg7vRIqng534QsoT1iXqyNpBMewyjQAVt5gTjn1L5d0SasARUH18lsSqwzNL-RT8cAWLqsw1GDyNrOWSzxT2l5d1kPT9wgAAWef0666DmIfPENm_mALNa3z2TwbceU7S60gQ1MKAYxt3PiOaIDBAXcDg-XCjShU6DYVuqU', start_index=22805)
Annotation(end_index=22922, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuDltcpMxj44R-e1oRZXT5vn5WJ31iKVXZbsWuryG9BhxmRoUlrTJIm2WXPj_fFHrv0bKqiQjYWwTXTRFdNsIo7SANIo1qO00QTL9KBhSnpluQlofGxUgxcxgTjPibmm48oJ35uq9xqA==', start_index=22913)
Annotation(end_index=23016, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHi15R80TH05ms6PPH1klETqPRPDzqyKi79k_9j5qqN4yIGHC0P878sipCYuP9BrlzC0cg7p0pi2N-SEFZ5flvKrO9m0-BgbRI6RA3Jn12Eh9IoutcqZ-8f7nxXM7ryh5fbCUrWiQDb2eZZWpsqP4Zv8LeOGlJhPOA8we9IRL226sXrT_KPICubkqK6LoKl50sGX_FTOuZN-ogk4LKmEdOpPD5QNRhU2o7VbsE2b6X3vKvNiP47k5xBY31eBmgSsWBSISNomOGF4OrdAg-W4z_1EjlOVJa7fUniRiKE1Bc=', start_index=23007)
Annotation(end_index=23140, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzsS4N7HmZW8b_qs-qlKDJijiLjdtUGr0bx83xwDmU4RCWl1q41fuUo4A7OSdfWxkTNuLqWlGic131mhZAM2Dg5xAcbsIPUklFIW7uqdz2OdRPgyWF9qmtEysWrm6jIH1sRs6c4_kIjQ==', start_index=23131)
Annotation(end_index=23238, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1ZQTTdDQcSOXQjtk6R7Ox0HwGSDGrt-_ZkS-KAIJ2ytcnZs_T474GIAu72ugEm7jFYXZDRV4kA9uI5GcVxFugzGzZox8SBfh2Dv_ck1EZSG3fLTfh-tUt-E2PKLTm2_PWxVwez4gEX92Nos2E2YuaZ7v_wlGlLnE5eirV0sLoLwA=', start_index=23228)
Annotation(end_index=23325, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRqxzqHO4jV6tBQVmTHqJmnhbGAliNNycMJjVN_2MoBwkeYraKjJsZiYhbTSbBqpUIrpdqgXa_pnCAfhfJmw9tZp6esZ9xsfgE1NACmiRxxthwN0UVPF7p9flEQh8d9bJbA8yM4ARqaUJZZy8p8UKH-N6DpjaMr6zSwMbkqgVOo-tO21yskr_2ruseStiJsLlp6gIqYNym5-sLcs1jewrOu_3fkxdL8nzH3WeERlwi22BKSacZ5T5vKKz92tpt0N5YMzDJMwMGIaClXTiJX_a2jmYhOjkMM9EDf33ToKt6HedsvPT4ogKgb0uJol-pYAE=', start_index=23315)
Annotation(end_index=23443, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRTLteKqKSALzdkypAnlEkYNcbbByHY4y1TKtLIDknGLDTZB7QG9rVlN8uroaj-Ra1qVlrLXb_qOh-V1E__QruDrw0iwsyHAjyGD0rxkG8lGCO5bU6tRwzEtZ9Di3cIDOQsQXV2lPbJ0SkQ29Yw1shgtt4s29weFZ_-tv-aDqB9vBZKVKXDRcSIX1z2aLbQ-egZe7OmIvNR5sv8A==', start_index=23433)
Annotation(end_index=23543, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsvpagWFh6xzAeSeOQWzGqnDx_VD-oao7AA7ksPZdxejkA7vgRWNSYDw4aVFh_swFhmRqPg9VhPAWS6-ETZWTGM00GXSlZ70Amx2V9y7wBsnXHsVuCTkYHdeNpO6dnVnwV2lk-dnZJ', start_index=23533)
Annotation(end_index=23634, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFg6RBxGeurCDqhFNABj5JQqAssxlBtIqxiiddpI3qunAlUvGomfcCkL__AcO2Se-sz8zEb9hbY62FGQ_tx3JYLOss3TPAYolmCm0pEVonZjudC-LOWw6NEhaXWqNqI38sqni2FY8-d', start_index=23624)
Annotation(end_index=23734, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJS2kgKoUcNu8RyeSDCly-OmPwHqcCbMnzO756sBePWmxMp59j8eRndwo_phVZbZz6H5aRQBkCKwAdbI7HlK6ybrS0WsHEtmeFGNDVL0LHYOaazQ-LMqYkHNNpJmMlCe6ke9Xus5CF', start_index=23724)
Annotation(end_index=23809, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3w5rmU2_DBHJJuSF4buTEQSrZEiy_z7cAKPjMR-mjqL_EfMyiv5biHbpj2j4AKX5pjC8RBefjYBVfp_MvlweMJWZHunNdwaS_qQeej9lOJI8-P9fGWiXUDlUZrbSDGaKhcrR6V_EPI2rAPZKu4rKBOVJxqxwPgABzI2bN5Dhdizo9jQ8GYwC1MmHZm8D3V62qU1edeBsK1ljFOeaBpdfAgIKR3Qg_r5S4F9QoLq0DxxdjAZ9hfqXP51eeVjZACGmGFQ97ZYzyzsy72QkTWBLvwX9_0egi', start_index=23799)
Annotation(end_index=23882, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrKygGOxX6rxHsdlxNzUdCbIMtaavSfE7HNnYQP-nu-daXGQ9eBVQItYbW0YQsHxNMZ-dnQjinfDXqYOKZ-jeVMBXzyfydeCZ7LVgi0_pncbtwu9Q4KDJtR9EPfHt3Nou5a1Cov_Gqmg==', start_index=23873)
Annotation(end_index=23958, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGe3mGt4NJm0Y96XpEG1PRNKHjXzsjqMiPD_hTCoafb1lluE0rIqIYX8KeVi1B6O5MpviPN8L5NDWMGxSn9HQDqWbctpFfchsGwqI6T_r1itESpEfiCWxLmyp3FtFm8T9NnxEO3uufuxJ7HbAFT3YpYjiiOGIwny9ZK4lVe-EGaWDlcqubi8DfG5g3s5FqvXQIisavfBaGJT7REDseZSDMIACmCG9VIM12319qgcaPcCzBoUHasW5lM', start_index=23949)
Annotation(end_index=24050, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzh91fQKzj5eOzJlt28qx1uTVbQ6i0AqyWILJMMCg9RvPhxpUH6DS0AMMkAXZxX2ApapDUoL0OZ-8mb3QM7o_23DahiFidL3eKcqwr09E4F4n6k5QZesRmYdKqBxSM', start_index=24040)
Annotation(end_index=24123, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEuVTVIxeckN1AsCrgcBBtMsdyXwqs9U3ib-rcYMJvbeZjKjCAvkXgFM5rhrtg2qj-AOCn7xiRGGvV3HOH28Pd1vdwuElYfvgZxTOyfJ5HTxcc9qxo-8Gv6qRTFX63jQH4Y6Axof7Ccaw==', start_index=24113)
Annotation(end_index=24195, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2QosTzCdik2HpF10umbDO2PjkG4D5JzcL-id7JCJc1fvKvzu7Ofk1yCrLiuraSuRIDh0w1V6C1T5xO7r7m3M4_8GBfu0rqM0yCl68bRGVe_85Bmw9vK5wCFYl', start_index=24186)
Annotation(end_index=24277, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmBvaD9FlRin0h4IQnAYiIdDAfXZT4pTnlc_1a5AVV2IkEIbaA4jyU-GgvU5zSvCuMHGgfK_n4IFxQZY59ZEGqcq6S1tg5ZRB0ZDqtwyvX55AYnW6iTHU7pbupuTkBqw==', start_index=24268)
Annotation(end_index=24357, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQevdGoO5Z6JH5-bAgidRUsqIlV6x6WvZUTnpoUanXZx5K3W-4KO52UYOTXg5E29FtHc40Vq5eGN8k9mC8u3DHOIinzpW4p_VDnm1na_HslpQcQTgmzHGLU36rxOVgWWvQ7uPVZ5FONGJi43AtIG-d7YvdY_gSWFfFNsOpbsQCvUOdi_j1T6otWMHK1tfE9vdkv8OgMzazEOGe8QtUB5clv7yWWwEGu3mV5ZJudL-MhEwT_bjem2YD2Czia-rCTsAOaKgjV6iog2LG', start_index=24347)
Annotation(end_index=24427, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEENfnXNimDcoJlaGk76qmyh4rBtrxxrN_CpwRrFAMRprkzA2xzSUYjsuN8SAnNnFPfKOpllyVAIwocEJtIenBzXv29dRko3FQdacUisxdb8KAsQI_OaFuWunhZQV8sTo8o', start_index=24417)
Annotation(end_index=24501, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfwcWf93iRugy9h3iFDLoGuWnaSPevnE25V8QyPIdi0Jhnw7sdvQWJdOAq_pz5scCOLrjnlB9ufbt1njp31p5NCI9rz2Olv-0XzxykowInRAPyo0EgJfasiiPUTlmuDxFyga92QftcsOVW7zmXtjhQDVjtMDu0QuQLDBTLKatDMvmQ6VR6WlKTTshG', start_index=24491)
Annotation(end_index=24569, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8KMxgZb0dEmrV3ny1RxMCTefgGKpYi02oIWsAIWzcv2-s_MK2phmQWHvQ2IOhz2HDLuOpflK31h81gbnNMzzsfkoePHqmVxLZg5d5TXFds2NvyWPRoUv4FYUTN46UKuNNtbpgUk-VPA==', start_index=24559)
Annotation(end_index=24651, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9dQGEoS1Jg_89RsiWz8E-vDxhKCUkevDsZUJnfjIL7Od3ATZIcqZE7XrEkjjW6eht4mUjzD_KM3kbccrqMHZIvCo-mLH-_CSck4ChOWHXnnGsUpaOHOperqTuVtzZKagKvgBx8GTWsA4v2uT0cw12nuoLzW1GLxzqNpWqPvuOVF92aKjYJFzvAVzB6jnm1YgkjxD7H8n3xmB9iiosyLdmXwN2', start_index=24641)
Annotation(end_index=24710, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOliFHwK1vJI9a50fPRIinb6V2TJP-g8WD2MaQKJ17Rge7DMWp9m6SLUGaboVMnP4uM7EKBm8ZftQPh9YHbXLTaGd_zx0Eqa5VtL5_vIvw_zJ5X6ID65xItisrWm9Qbc4ZUhY6SRljs27-vvsC4WVRZ5OflCA2LQWcAXxxROUESBGyz4_0VCsxNPD_sZMf', start_index=24700)
Annotation(end_index=24799, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpiu31ry9v20egd7fpewXIYbGf-TRD8eFNDcfU4Xvn3Qf3Iw8o09UmXOC6xMAhlxZsk5AtX1UVut6ya1q0z4_MdI4FwsIiheTJkwSPcFAfv6TtiyLacOypOormJ73dOQy3RKkmdyZyeXk5r61EArkgN8yvUTlWF6ijvOsUeSSQ', start_index=24789)

## Sources
