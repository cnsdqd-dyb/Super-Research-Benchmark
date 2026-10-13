# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** df233221 | **Time:** 647.30s | **Cost:** $0.20590
--------------------------------------------------------------------------------

# Planning Strategy for Head and Neck Tumor Radiotherapy: Balancing Target Dose Coverage with Organ-at-Risk Tolerance to Maximize Local Control While Minimizing Injury

## Executive Summary

Head and neck cancer (HNC) radiotherapy represents one of the most technically challenging domains in radiation oncology due to the complex anatomical arrangement of critical structures surrounding the tumor targets. The fundamental objective of treatment planning is to deliver tumoricidal doses to the planning target volume (PTV) while simultaneously minimizing radiation exposure to adjacent organs-at-risk (OARs) such as the salivary glands, spinal cord, brain stem, optic nerves, and swallowing structures. This report synthesizes current evidence on planning strategies that optimize this balance, examining the comparative efficacy of various delivery techniques including intensity-modulated radiotherapy (IMRT), volumetric modulated arc therapy (VMAT), proton beam therapy, and emerging approaches such as 4π radiotherapy. Furthermore, this analysis explores the integration of normal tissue complication probability (NTCP) models into the optimization process, knowledge-based planning systems, and multi-criteria optimization frameworks that enable clinicians to navigate the inherent trade-offs between tumor control and toxicity reduction. The evidence suggests that while photon-based techniques like VMAT have achieved a mature level of clinical implementation with demonstrated equivalence to step-and-shoot IMRT, proton therapy offers superior OAR sparing for specific patient populations, particularly those receiving unilateral radiation. The future of optimized HNC planning lies in the systematic integration of biological optimization objectives, automated knowledge-based planning tools, and model-based patient selection methodologies that individualize treatment approaches based on predicted toxicity profiles.

## 1. Introduction and Clinical Context

### 1.1 The Therapeutic Challenge in Head and Neck Cancer

Head and neck cancers present unique challenges for radiation therapy planning due to the dense concentration of critical structures within a relatively small anatomical volume. The treatment region encompasses numerous OARs including the parotid and submandibular salivary glands, mandible, larynx, pharyngeal constrictor muscles, spinal cord, brain stem, optic nerves, chiasm, and oral cavity, all in intimate proximity to the tumor-bearing tissues [1]. This anatomical complexity, combined with the high doses required for tumor control, creates a narrow therapeutic index where small deviations in dose distribution can significantly impact either treatment efficacy or toxicity outcomes.

The evolution of treatment planning techniques over the past two decades has fundamentally transformed the approach to HNC radiotherapy. Conventional three-dimensional conformal radiotherapy (3D-CRT) has been largely superseded by intensity-modulated approaches that enable more conformal dose distributions and improved normal tissue sparing [2]. This transition was driven by the recognition that reducing dose to critical structures could significantly impact patient quality of life, particularly regarding long-term xerostomia, dysphagia, and other treatment-related morbidities that substantially affect functional outcomes and survivorship.

### 1.2 The Fundamental Trade-off

The central challenge in HNC treatment planning lies in balancing two competing objectives: achieving adequate target coverage to maximize local tumor control while respecting dose constraints for OARs to minimize treatment-related toxicity [3]. This trade-off is particularly acute in HNC due to the proximity of targets to critical structures and the steep dose-response relationships for both tumor control and normal tissue complications. Recommended dose-volume constraints for individual OARs provide quantitative planning goals, but the clinical reality involves prioritizing between sparing certain risk organs at the expense of others, as simultaneous optimization of all structures is often mathematically impossible [4].

The quantification of this trade-off has evolved from purely physical dose-volume metrics toward biological indices that more directly relate dose distributions to clinical outcomes. Normal tissue complication probability models, which estimate the probability of specific toxicities based on dose-volume parameters and clinical factors, have become increasingly sophisticated and clinically applicable [5]. This shift toward biologically-based optimization represents a paradigm change in treatment planning philosophy, moving from constraint satisfaction toward outcome prediction and maximization.

## 2. Comparative Analysis of Delivery Techniques

### 2.1 Intensity-Modulated Radiotherapy versus Volumetric Modulated Arc Therapy

The comparison between step-and-shoot IMRT and VMAT has been extensively studied in the HNC population, with evidence demonstrating that both techniques are capable of meeting the majority of planning goals for locally advanced disease [6]. A comparative analysis of these approaches revealed that plan quality was not significantly different between nine-field step-and-shoot IMRT and dual-arc VMAT (DA-VMAT) when analyzing data for the entire patient cohort or on an individual case basis [6]. This equivalence in planning objectives establishes a foundation for exploring the practical trade-offs between these delivery modalities.

The primary differentiators between IMRT and VMAT relate to delivery efficiency and resource utilization rather than fundamental dosimetric quality. DA-VMAT demonstrated shorter treatment delivery times, fewer total monitor units (MUs), and similar delivery accuracy compared to conventional IMRT [6]. These advantages translate into improved patient comfort, reduced intrafraction motion, and potentially lower leakage radiation exposure. However, DA-VMAT planning required more time per optimization cycle and necessitated greater data storage for three-dimensional dose information within the treatment planning system [6].

From a clinical implementation perspective, these trade-offs require consideration at the institutional level. The shorter delivery time of VMAT offers clear advantages for patient throughput and comfort, while the longer planning time and computational requirements may strain departmental resources, particularly during the initial implementation phase of new technology [6]. The evidence supports the use of either IMRT or VMAT for locally advanced HNC, with the choice depending on institutional capabilities, patient factors, and specific clinical scenarios. Many centers have adopted DA-VMAT as a standard treatment approach for this population, recognizing its practical advantages without sacrificing planning quality [6].

### 2.2 Proton Beam Therapy: Superior Sparing with Equivalent Control

Proton beam therapy represents a fundamentally different approach to HNC radiotherapy, leveraging the physical characteristics of charged particle beams to achieve highly conformal dose distributions. The Bragg peak phenomenon allows extremely localized dose delivery at precise depths with no exit dose after the distal tail, theoretically eliminating radiation exposure to tissues beyond the target volume [7]. This physical advantage translates into clinical benefits for specific patient populations.

Recent clinical trial results presented at the 2025 American Society for Radiation Oncology Annual Meeting demonstrated that proton beam radiotherapy achieved disease control and survival comparable to IMRT, with significantly less toxicity and improved quality of life for patients with head and neck cancers undergoing ipsilateral radiation therapy [8]. The analysis found no significant differences between proton beam radiotherapy and IMRT for key oncologic endpoints including local control, regional control, and distant metastasis-free survival. Three-year progression-free survival rates were 92.3% for proton therapy and 94.1% for IMRT, while overall survival rates were 97.4% and 97.6%, respectively [8].

The toxicity profile favored proton therapy across multiple domains. Patient-reported outcomes of functional and global health were higher for proton beam radiotherapy compared to IMRT. More patients in the IMRT group reported mouth and throat soreness, higher skin burn sensitivity, and skin darkening that affected their quality of life [8]. These findings support the clinical advantage of proton therapy for appropriate patient selection, particularly for unilateral HNC where the absence of exit dose can substantially reduce dose to contralateral structures.

However, proton therapy is not universally superior for all HNC patients. The selection of patients who will benefit most from proton therapy remains a critical clinical decision. Model-based approaches using NTCP estimation have been developed to identify patients with the greatest potential for toxicity reduction [9]. Automated knowledge-based planning systems have demonstrated that proton knowledge-based plans (KBPs) yielded on average 7.1 Gy lower dose to salivary structures, 6.1 Gy lower dose to swallowing structures, and 7.6 Gy lower dose to the oral cavity compared to photon KBPs [9]. This translated to reductions in average grade 2-3 dysphagia and xerostomia by 7.1 and 5.5 percentage points, respectively, with 22% of patients in one study population being indicated for proton treatment based on NTCP criteria [9].

### 2.3 Emerging Techniques: 4π Radiotherapy and Non-Coplanar Approaches

Beyond conventional coplanar IMRT and VMAT, non-coplanar treatment approaches have demonstrated potential for further OAR dose sparing in HNC. The 4π radiotherapy technique utilizes a large number of non-coplanar beam angles to achieve superior normal tissue sparing compared to standard VMAT approaches [7]. This technique does not require new expensive equipment like proton therapy but necessitates sophisticated geometrical modeling to prevent gantry-patient collisions.

The delivery time of 4π plans involving large numbers of beams can be excessively long in manual mode, representing a practical limitation for widespread clinical implementation [7]. However, automation of non-coplanar plan delivery is advancing to overcome this limitation. The theoretical advantage of 4π radiotherapy lies in its ability to exploit angular freedom to avoid critical structures, potentially achieving dose distributions that are impossible with coplanar techniques while maintaining the cost advantages and widespread availability of photon therapy.

## 3. Dose Calculation Algorithms and Their Clinical Impact

### 3.1 Evolution of Algorithm Accuracy

The accuracy of dose calculation algorithms directly impacts treatment plan quality and the reliability of dose-volume metrics used for clinical decision-making. The evolution from Type A to Type B algorithms, and subsequently to advanced Type B algorithms such as Monte Carlo and collapsed cone convolution methods, has improved the accuracy of dose predictions, particularly in heterogeneous tissue regions [10]. However, this evolution has also introduced challenges during implementation phases, particularly where significant differences in target volume coverage are observed between algorithms.

A study quantifying the effect of switching from a conventional Type B algorithm to an advanced Type B algorithm demonstrated clinically significant variations in standard dosimetry metrics for head and neck IMRT plans [10]. While differences to soft tissue appeared relatively small, the impact on clinical dosimetry metrics was substantial enough to require clinical decision-making regarding planning objectives. This poses a clinical conundrum: radiation oncologists must either continue using conventional minimum target volume coverage recommendations based on older algorithms, potentially resulting in increased dose to normal tissue, or accept lower target volume coverage with newer algorithms, provoking anxiety regarding potential loss in tumor control probability [10].

### 3.2 Implications for Treatment Planning

The challenge is particularly relevant in HNC owing to both the number of complex tissue interfaces and the narrow therapeutic index characteristic of this disease site [10]. Accepting even small increases in delivered radiation dose has the potential for significant normal tissue toxicity, while inadequate target coverage risks local treatment failure. The transition between dose calculation algorithms therefore requires careful validation and potentially re-optimization of planning constraints to maintain clinical standards.

This algorithmic sensitivity underscores the importance of understanding the limitations and characteristics of specific dose calculation engines within treatment planning systems. Planning objectives and constraints that were validated using one algorithm may not translate directly when upgrading to more accurate algorithms, necessitating a review of clinical protocols and potentially re-establishing planning goals based on the new calculation methodology.

## 4. Biological Optimization and NTCP Integration

### 4.1 The Rationale for Biologically-Based Planning

Traditional treatment planning optimization relies on physical dose-volume constraints derived from empirical observations of dose-toxicity relationships. While this approach has proven clinically valuable, it does not directly optimize for the probability of treatment outcomes. Biologically-based optimization using normal tissue complication probability models represents an advancement toward directly maximizing clinical outcomes [11].

The concept of equivalent uniform dose (EUD), including the generalized EUD (gEUD), has found considerable support among proponents of biologically-based optimization because it offers a compromise between purely biological indices such as tumor control probability (TCP) and NTCP and traditional dose-volume metrics [11]. Incorporating EUD-based cost functions into inverse treatment planning algorithms has been demonstrated to result in improved OAR sparing without sacrificing target coverage in multiple studies [11].

### 4.2 Multi-Variable NTCP Models in Clinical Practice

Clinically validated multi-variable NTCP models have recently become available for head and neck cancer patients, enabling estimation of side-effect risks prior to treatment to facilitate informed decision-making and treatment optimization [5]. These models incorporate dose-volume parameters as well as clinical factors such as patient age, smoking status, concurrent chemotherapy, and tumor stage, enabling personalized risk prediction.

The direct use of multivariable NTCP models in treatment plan optimization has been investigated as a method for producing clinically acceptable treatment plans with improved dose distributions [12]. In comparative studies, intensity-modulated radiotherapy plans were optimized using objective functions either based on generalized EUD or based on multivariable NTCP models. NTCP models for patient-rated xerostomia, physician-rated RTOG grade II-IV dysphagia, tube-feeding dependence, and various patient-rated aspects of swallowing dysfunction were incorporated into the optimization process [12].

The comparison of optimization techniques using pseudo-Pareto fronts, which visualize the trade-off between target dose conformity and the sum of NTCPs, demonstrated that NTCP-based optimization could achieve favorable balances between target coverage and normal tissue sparing [12]. This approach allows planners to explicitly consider the clinical consequences of dose distributions rather than relying solely on physical constraints that may not directly correlate with outcome probabilities.

### 4.3 QUANTEC and Contemporary Dose-Volume Constraints

The Quantitative Analysis of Normal Tissue Effects in the Clinic (QUANTEC) initiative provided a comprehensive review of radiation dose-volume effects relating to multiple OARs, resulting in updated suggested dose-volume parameters associated with given risks of normal tissue complications [4]. This represented a data-driven update to earlier empirical guidelines and has served as a foundation for clinical planning constraints in the IMRT era.

However, nearly a decade has passed since the QUANTEC reviews, and much of the evidence was based on conventional 3D conformal radiotherapy rather than IMRT [4]. The shift toward IMRT has enabled more conformal dose distributions with non-uniform dose patterns that may not be fully characterized by traditional dose-volume metrics. Furthermore, there has been a transition in focus from physician-scored objective measures of normal tissue complications toward patient-reported outcomes (PROs) facilitated by validated instruments such as the EORTC QLQ H&N35 and PRO-CTCAE [4]. This evolution necessitates ongoing refinement of dose-response models and planning objectives to reflect contemporary treatment techniques and outcome assessment methodologies.

## 5. Multi-Criteria Optimization and Knowledge-Based Planning

### 5.1 Addressing Inter-Planner Variability

A major challenge in HNC IMRT planning is the large variation in plan quality among treatment planners, attributable to varied planning skills and limited planning time [3]. This variability can result in inconsistent patient care and suboptimal treatment outcomes when less experienced planners are unable to achieve the quality standards established by expert practitioners. Addressing this challenge has become a priority for departments seeking to standardize care quality.

Multi-criteria optimization (MCO) represents one approach to this problem, creating many planning solutions for a single clinical case so that clinicians can make decisions based on the trade-offs among dose coverage of tumor volume and protections of sensitive structures [3]. Rather than producing a single optimized plan, MCO generates a database of plans representing different points along the Pareto front, allowing clinicians to select the plan that best balances competing objectives for the specific clinical scenario.

### 5.2 Automated Planning Tools

Automatic planning tools developed within commercial treatment planning systems aim to mimic the manual processes of skilled planners by progressively and iteratively adjusting and adding planning objectives [3]. This approach may mitigate the shortcomings of gradient-based optimization by incorporating the heuristic knowledge experienced planners use to achieve high-quality solutions. These tools can reduce inter-planner variability and improve planning efficiency, particularly for complex cases like HNC where achieving optimal balance among multiple structures is challenging.

Knowledge-based planning (KBP) represents another advancement in automated plan generation, using statistical models derived from high-quality historical plans to predict achievable dose distributions for new patients [13]. PlanIQ Feasibility, for example, predicts achievable dose volume histograms based on energy-specific dose spread calculations, reflecting the characteristics of photon dose distribution in media [3]. These predictions can serve as initial inputs for planning objectives, establishing realistic goals based on patient-specific anatomy rather than generic constraints.

### 5.3 Integration of Prediction and Optimization Tools

The ideal planning workflow would incorporate multiple complementary tools: a tool that reliably predicts achievable DVHs as initial inputs for planning objectives, a tool that automatically and progressively adjusts planning objectives, and a tool that offers multiple solutions based on different trade-offs [3]. The integration of these capabilities within a cohesive workflow could substantially improve planning consistency, efficiency, and quality for HNC radiotherapy.

The development of knowledge-based planning has provided guidance for planners to decide on trade-offs in a more objective manner, reducing reliance on individual experience and judgment [13]. Furthermore, advances in radiomics and artificial intelligence may strengthen the advantages of optimized planning approaches in terms of OAR sparing and tumor dose escalation, enabling increasingly personalized treatment strategies.

## 6. Clinical Implementation Considerations

### 6.1 Resource and Infrastructure Requirements

The implementation of advanced planning strategies for HNC requires consideration of resource allocation and infrastructure capabilities. Proton therapy facilities remain limited in number and high in cost, restricting accessibility for many patients [7]. The decision to implement proton therapy programs must weigh the clinical benefits against the substantial capital and operational investments required.

For photon-based techniques, the implementation of VMAT or advanced IMRT requires appropriate linear accelerator equipment with dynamic multileaf collimator capabilities, treatment planning system software with advanced optimization algorithms, and physicist and dosimetrist expertise in complex planning techniques [6]. The additional planning time and computational resources required for VMAT optimization, particularly with advanced algorithms, must be factored into departmental workflow and staffing models.

### 6.2 Quality Assurance and Validation

Regardless of the technique employed, comprehensive quality assurance programs are essential to ensure that planned dose distributions are accurately delivered. Delivery accuracy for both IMRT and VMAT has been demonstrated to be similar, with both techniques capable of achieving the precision required for conformal HNC treatment [6]. However, the complexity of HNC plans necessitates rigorous verification procedures, including patient-specific dose measurement and imaging verification of patient positioning.

The validation of NTCP models for clinical use requires careful consideration of their generalizability across different treatment approaches, institutions, and patient populations [5]. Studies investigating the international generalizability of NTCP models have promoted their integration into more widespread clinical practice, but local validation remains important for ensuring that model predictions are applicable to specific clinical contexts.

### 6.3 Patient Selection and Individualization

The selection of appropriate patients for different treatment modalities represents a critical clinical decision that can significantly impact outcomes. For proton therapy, model-based approaches using NTCP estimation have emerged as objective methodologies for patient selection [9]. These approaches calculate the predicted reduction in toxicity probability for individual patients and select those who meet predefined thresholds for proton therapy indication.

For photon-based treatments, patient-specific factors including tumor location, stage, laterality, and concurrent treatment modalities influence the optimal planning strategy. Unilateral HNC treatments may benefit particularly from techniques that minimize dose to contralateral structures, while bilateral treatments require balancing multiple competing objectives across both sides of the treatment volume [8]. The integration of clinical factors into NTCP models enables truly personalized treatment planning that accounts for individual patient characteristics beyond anatomical considerations.

## 7. Future Directions and Emerging Paradigms

### 7.1 Adaptive Radiotherapy

Adaptive radiotherapy (ART) based on image guidance represents an evolving approach to managing anatomical changes during the treatment course [2]. Weight loss, tumor regression, and changes in soft tissue configuration during the 6-7 week treatment course can significantly alter the relationship between planned and delivered dose distributions. ART enables replanning based on updated imaging to maintain target coverage and OAR sparing throughout treatment.

However, adaptive RT based on image guidance is yet to be clinically optimized in head and neck cancer [2]. Challenges include the identification of appropriate triggers for adaptation, the efficiency of the replanning workflow, and the demonstration of clinical benefit in prospective studies. The integration of automated planning tools may facilitate more widespread implementation of adaptive approaches by reducing the resource burden associated with manual replanning.

### 7.2 Artificial Intelligence and Machine Learning

The application of artificial intelligence and machine learning to treatment planning is rapidly expanding, with potential applications in automated plan generation, quality assurance, outcome prediction, and patient selection [13]. Deep learning models trained on high-quality treatment plans may be able to generate clinically acceptable plans more rapidly than traditional optimization approaches, potentially addressing the challenge of planning time requirements for complex techniques.

Radiomic analysis of diagnostic and planning imaging may provide additional predictive information for treatment optimization, enabling the integration of tumor biology and spatial characteristics into the planning process. The combination of radiomic features with clinical and dosimetric variables in NTCP models may improve the accuracy of toxicity prediction and enable more refined treatment individualization.

### 7.3 Integration of Multimodal Data

Future planning strategies will likely integrate multiple data streams including diagnostic imaging, molecular profiling, clinical factors, and patient-reported outcomes to optimize treatment decisions. The comprehensive individual toxicity risk (CITOR) profile approach represents a step toward this integration, incorporating diverse data sources to generate personalized risk predictions [5].

The extension of NTCP models to incorporate longitudinal data on treatment response and toxicity development may enable adaptive risk prediction throughout the treatment course. This dynamic modeling approach could inform decisions regarding treatment adaptation, supportive care interventions, and follow-up strategies based on individual patient trajectories.

## 8. Conclusions and Clinical Recommendations

The evidence synthesized in this report supports several key conclusions regarding optimal planning strategies for head and neck tumor radiotherapy. First, both IMRT and VMAT are capable of achieving high-quality treatment plans for locally advanced HNC, with equivalence in plan quality established across multiple comparative studies [6]. The choice between these techniques should be guided by institutional capabilities, resource considerations, and specific clinical scenarios, with recognition that VMAT offers practical advantages in delivery efficiency without sacrificing dosimetric quality.

Second, proton beam therapy provides superior OAR sparing compared to photon-based techniques for appropriately selected patients, with clinical trials demonstrating equivalent oncologic outcomes and reduced toxicity, particularly for unilateral HNC [8]. Model-based patient selection using NTCP estimation provides an objective methodology for identifying patients who will benefit most from proton therapy, with approximately 20-25% of HNC patients meeting criteria for proton indication in contemporary analyses [9].

Third, the integration of NTCP models into treatment planning optimization represents a paradigm shift toward biologically-based planning that directly optimizes for clinical outcomes rather than physical dose constraints [12]. The direct use of multivariable NTCP models in inverse planning optimization is technically feasible and may achieve more favorable balances between target coverage and toxicity risk than traditional dose-volume-based optimization.

Fourth, multi-criteria optimization and knowledge-based planning tools address the challenge of inter-planner variability and planning efficiency, enabling more consistent and reproducible plan quality across an institution [3]. The integration of prediction tools, automated optimization, and multi-criteria exploration within cohesive workflows represents the current frontier of treatment planning advancement.

Finally, the selection of planning strategies must account for the specific clinical context including tumor location and extent, treatment intent, concurrent systemic therapy, and patient-specific factors influencing toxicity risk. The narrow therapeutic index in HNC necessitates careful attention to the trade-offs inherent in treatment planning, with recognition that optimizing for one objective may necessarily compromise others. The future of HNC radiotherapy planning lies in the systematic integration of advanced delivery techniques, biological optimization objectives, automated planning tools, and individualized risk prediction to achieve the optimal balance between tumor control and quality of life preservation for each patient.

## References

[1] PMC3479880 - IMRT enables delivery of adequate doses to head and neck tumors while minimizing dose to critical structures including optic nerves, orbits, optic chiasm, pituitary gland, and brain stem.

[2] PMC3479880 - Tomotherapy enables simultaneous use of image guidance and treatment delivery; however, adaptive RT based on image guidance is yet to be clinically optimised in head and neck cancer.

[3] PMC6612692 - Major challenge in HN IMRT planning is large variations in plan quality among treatment planners due to varied planning skills and limited planning time; multi-criteria optimization and automatic planning tools address these challenges.

[4] PMC6481934 - QUANTEC provided comprehensive review of dose-volume effects; shift from physician-scored objective measures toward patient-reported outcomes is relevant for contemporary IMRT planning.

[5] PMC11950982 - NTCP models estimate side-effect risks pretreatment; comprehensive individual toxicity risk (CITOR) profile developed for HNC patients.

[6] PMC3611711 - DA-VMAT and nine-field step-and-shoot IMRT demonstrate equivalent plan quality for locally advanced HNC; trade-offs include shorter delivery time for VMAT but longer planning time.

[7] PMC5225526 - Proton therapy has advantageous Bragg peaks but higher cost; 4π radiotherapy is non-coplanar IMRT with superior OAR sparing compared to VMAT.

[8] MSKCC Clinical Update - Proton beam radiotherapy achieves similar oncologic outcomes with less toxicity and improved quality of life compared to IMRT for unilateral HNC.

[9] Advances in Radiation Oncology - Automated knowledge-based planning using NTCP to identify patients for proton therapy; proton KBPs yielded lower dose to salivary/swallowing structures.

[10] PMC7807679 - Switch from Type B to advanced Type B dose calculation algorithms causes clinically significant variations in HNC IMRT plan dosimetry.

[11] AAPM Report 166 - EUD-based cost functions in inverse planning improve OAR sparing without sacrificing target coverage; multi-criterial optimization supported.

[12] UMCG Research - Direct use of multivariable NTCP models in treatment plan optimization produces clinically acceptable HNC treatment plans.

[13] Intechopen - Knowledge-based planning provides guidance for trade-off decisions; 4π VMAT strengthens IMRT advantage in OAR sparing and tumor dose escalation.

## Annotations


## Sources
[1] http://waocp.com/journal/index.php/apjcc/article/view/1187
[2] http://www.diva-portal.org/smash/get/diva2:1348582/FULLTEXT01.pdf
[3] https://advancesradonc.com/article/S2452-1094(22)00010-0/fulltext
[4] https://onlinelibrary.wiley.com/doi/10.1002/hed.27469
[5] https://pmc.ncbi.nlm.nih.gov/articles/PMC11574792/
[6] https://pmc.ncbi.nlm.nih.gov/articles/PMC11950982/
[7] https://pmc.ncbi.nlm.nih.gov/articles/PMC12265974/
[8] https://pmc.ncbi.nlm.nih.gov/articles/PMC3479880/
[9] https://pmc.ncbi.nlm.nih.gov/articles/PMC3611711/
[10] https://pmc.ncbi.nlm.nih.gov/articles/PMC3818806/
[11] https://pmc.ncbi.nlm.nih.gov/articles/PMC4041542/
[12] https://pmc.ncbi.nlm.nih.gov/articles/PMC5225526/
[13] https://pmc.ncbi.nlm.nih.gov/articles/PMC6481934/
[14] https://pmc.ncbi.nlm.nih.gov/articles/PMC6612692/
[15] https://pmc.ncbi.nlm.nih.gov/articles/PMC7807679/
[16] https://pmc.ncbi.nlm.nih.gov/articles/PMC8906058/
[17] https://pmc.ncbi.nlm.nih.gov/articles/PMC9284789/
[18] https://pps4rt.com/wp-content/uploads/2019/07/S10-S19_Marks_UseOfNTCPModels.pdf
[19] https://pubmed.ncbi.nlm.nih.gov/12648791/
[20] https://www.aapm.org/pubs/reports/rpt_166.pdf
[21] https://www.astro.org/news-and-publications/news-and-media-center/news-releases/2025/imrt-matches-proton-therapy-in-patient-reported-outcomes-for
[22] https://www.hca.wa.gov/assets/program/071712_imrt_excluded_studies_final[1]_0.pdf
[23] https://www.intechopen.com/chapters/80909
[24] https://www.medrxiv.org/content/10.1101/2024.04.01.24305163v3.full.pdf
[25] https://www.mskcc.org/clinical-updates/proton-beam-reduces-acute-toxicities-compared-to-imrt-for-head-and-neck-cancer-patients-who-receive-unilateral-radiation
[26] https://www.sciencedirect.com/science/article/pii/S1368837525000533
[27] https://www.sciencedirect.com/science/article/pii/S2405631625000016
[28] https://www.umcgradiotherapie.nl/en/research/medical-physics-research/adaptive-radiotherapy-and-treatment-planning/ntcp-based-treatment-planning-optimization