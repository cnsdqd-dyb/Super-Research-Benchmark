# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 9ea1e796 | **Time:** 362.94s | **Cost:** $0.11752
--------------------------------------------------------------------------------

# Balancing Diagnostic Specificity with Treatment Timing in the TNM Staging System for Liver Cancer: Tumor Burden Quantification versus Lymph Node Metastasis Prediction

## Abstract

The Tumor-Node-Metastasis (TNM) staging system represents the cornerstone of hepatocellular carcinoma (HCC) classification, providing a standardized framework for prognostic assessment and treatment planning. However, the system faces an inherent tension between diagnostic specificity and treatment timing, particularly when quantifying tumor burden through T descriptors while simultaneously predicting lymph node metastasis via N categorization. This report examines how the TNM system navigates this balance, analyzing the anatomical constraints of tumor burden quantification, the challenges inherent in lymph node metastasis prediction, and the clinical implications of these dynamics. The analysis reveals that while TNM excels in anatomical staging for surgical candidates, its exclusion of hepatic function and binary N classification limit its predictive utility, particularly for lymph node metastasis where sensitivity and specificity remain suboptimal. Understanding this balance is essential for clinicians seeking to optimize treatment timing while maintaining diagnostic accuracy in HCC management.

## 1. Introduction

Hepatocellular carcinoma represents one of the most prevalent malignancies worldwide, with staging systems playing a pivotal role in determining prognosis and guiding therapeutic interventions [1]. Among the various staging frameworks available—including the Barcelona Clinic Liver Cancer (BCLC) system, Cancer of the Liver Italian Program (CLIP) score, and Okuda system—the TNM classification established by the American Joint Committee on Cancer (AJCC) remains the most widely utilized anatomical staging system, particularly in the United States [2]. The TNM system provides a detailed assessment of tumor extent through three fundamental components: the T category describing primary tumor characteristics, the N category indicating lymph node involvement, and the M category denoting distant metastasis [3].

The fundamental challenge confronting the TNM staging system lies in its attempt to balance diagnostic specificity with treatment timing. Diagnostic specificity refers to the system's ability to accurately classify disease extent, while treatment timing encompasses the urgency and appropriateness of therapeutic intervention based on stage assignment. This balance becomes particularly complex when considering tumor burden quantification versus lymph node metastasis prediction, as these two aspects of staging carry different implications for both prognosis and treatment selection [4].

The TNM system's anatomical foundation, while providing objective criteria for disease classification, creates inherent limitations when applied to HCC. Unlike other malignancies where anatomical extent alone may sufficiently guide treatment decisions, HCC occurs in the context of underlying liver disease, making hepatic functional assessment critical for optimal management [5]. Furthermore, the relatively low incidence of lymph node metastasis in HCC—reported between 1.23% and 7.5%—presents unique challenges for nodal staging, as the rarity of this phenomenon complicates both detection and predictive modeling [6].

This report synthesizes current evidence to examine how the TNM staging system navigates the balance between diagnostic specificity and treatment timing in the context of tumor burden quantification and lymph node metastasis prediction. By analyzing the structural components of TNM classification, the clinical performance of its various elements, and comparative data with alternative staging systems, we aim to provide a comprehensive understanding of this critical balance in HCC management.

## 2. Tumor Burden Quantification in the TNM System

### 2.1 Anatomical Principles of T Classification

The T category in the AJCC TNM system for HCC quantifies tumor burden through a hierarchical classification based on tumor size, number, and vascular invasion [7]. The current 8th edition classification establishes distinct categories that reflect progressively increasing tumor burden and associated prognostic implications:

The T1 classification is subdivided into T1a and T1b, where T1a denotes a solitary tumor measuring 2 cm or less in greatest dimension, while T1b represents a solitary tumor exceeding 2 cm without vascular invasion [7]. This distinction acknowledges that very small solitary tumors carry a more favorable prognosis, even when exceeding the 2 cm threshold, provided vascular invasion is absent. The T2 category encompasses either a solitary tumor larger than 2 cm with vascular invasion or multiple tumors, none exceeding 5 cm in maximum dimension [7]. This category reflects the adverse prognostic impact of vascular invasion, which represents a critical milestone in tumor progression.

The T3 category captures more advanced tumor burden through the presence of multiple tumors with at least one tumor exceeding 5 cm, while T4 represents the most advanced local disease, characterized by tumors involving a major branch of the portal vein or hepatic vein, or direct invasion of adjacent organs [7]. This anatomical progression from T1 through T4 provides a structured framework for quantifying tumor burden, with each category carrying distinct prognostic and therapeutic implications.

### 2.2 Diagnostic Specificity in Tumor Burden Assessment

The TNM system's approach to tumor burden quantification offers considerable diagnostic specificity through its anatomical foundation. The reliance on measurable morphological characteristics—tumor size, number, and vascular relationships—provides objective criteria that can be assessed through standard imaging modalities including computed tomography (CT) and magnetic resonance imaging (MRI) [8]. This anatomical precision facilitates consistent staging across different clinical settings and enables meaningful comparisons of outcomes across patient populations.

However, this anatomical focus introduces limitations when applied to HCC specifically. The TNM system's exclusion of hepatic functional assessment represents a significant gap in prognostic accuracy, as liver function profoundly influences both treatment tolerance and overall survival [1]. Studies comparing staging systems have demonstrated that TNM shows inferior predictive ability compared to systems that incorporate hepatic function, such as the BCLC and CLIP systems [1]. This limitation becomes particularly relevant when considering treatment timing, as patients with substantial tumor burden but preserved hepatic function may tolerate aggressive interventions, while those with limited tumor burden but decompensated liver disease face restricted therapeutic options.

The tumor burden score (TBS) represents a recent innovation that attempts to enhance prognostic accuracy by combining tumor size and number into a single metric [9]. Research has demonstrated that TBS exhibits optimal discrimination and calibration compared to conventional staging systems, with higher TBS values associated with progressively worse prognosis [9]. This approach suggests that refined quantification of tumor burden—beyond the categorical T classification—may improve prognostic accuracy while maintaining the anatomical specificity that makes TNM valuable.

### 2.3 Treatment Timing Implications of Tumor Burden Staging

The T classification directly influences treatment timing through its impact on therapeutic decision-making. Early-stage tumors (T1a) may be amenable to curative treatments including surgical resection, transplantation, or local ablation, with treatment timing less critical due to the availability of multiple effective options [10]. As tumor burden increases through T2 and T3 categories, treatment options narrow, and timing becomes increasingly consequential. The presence of multiple tumors exceeding 5 cm (T3) typically necessitates consideration of locoregional therapies such as transarterial chemoembolization (TACE) or systemic therapy, with delayed treatment potentially allowing further disease progression.

The T4 category, characterized by major vascular invasion, represents a critical juncture where treatment timing becomes paramount. Vascular invasion in HCC is associated with rapid disease progression and significantly reduced survival, making prompt initiation of appropriate therapy essential [7]. However, the anatomical classification alone cannot guide the selection between surgical intervention, locoregional therapy, or systemic treatment—decisions that require integration of hepatic function, performance status, and tumor biology.

## 3. Lymph Node Metastasis Prediction in the TNM System

### 3.1 Current N Classification Structure

The N category in the AJCC TNM system for HCC employs a binary classification, distinguishing between N0 (no regional lymph node metastasis) and N1 (regional lymph node metastasis) [7]. This simplified approach reflects the historical challenge of nodal staging in HCC, where the low incidence of lymph node involvement has limited the development of more granular classification systems. The 8th edition AJCC manual maintains this binary structure for HCC, unlike some other malignancies where N classification has been expanded to reflect the number and extent of involved nodes [4].

Regional lymph nodes for HCC include hilar nodes, periduodenal nodes, and peripancreatic nodes for tumors involving the right hepatic lobe, while left hepatic lobe tumors involve hilar and gastrohepatic nodes [4]. The identification of nodal metastasis relies on both imaging assessment and pathological evaluation, with imaging predictors such as hilar invasion or short-axis lymph node diameter ≥9 mm demonstrating variable sensitivity and specificity [6].

### 3.2 Challenges in Lymph Node Metastasis Detection

The prediction of lymph node metastasis in HCC presents unique challenges that impact the diagnostic specificity of N classification. The low incidence of nodal involvement—ranging from 1.23% to 7.5%—creates a fundamental difficulty in developing sensitive and specific predictive models [6]. This rarity means that even imaging findings with high positive predictive values in other malignancies may perform suboptimally in HCC due to the low pretest probability of nodal disease.

Current clinical assessment relies primarily on imaging modalities including CT and MRI, with proposed predictors including nodal size, shape, and architectural characteristics [4]. However, studies have demonstrated that ovoid nodal shape, clustering of nodes, and absence of a fatty hilum on CT are not useful predictors of malignancy in HCC [4]. MRI provides superior characterization of suspicious lymph nodes compared to CT, but both modalities face limitations in distinguishing reactive from metastatic nodal enlargement, particularly in the context of underlying liver disease and inflammation.

The reliance on size criteria alone represents a significant limitation, as metastatic nodes may not demonstrate sufficient enlargement for reliable detection, while benign reactive nodes may exceed size thresholds [6]. This creates a tension between diagnostic specificity—accurately identifying true nodal metastasis—and sensitivity—avoiding false negative classifications that might delay appropriate treatment.

### 3.3 Performance Metrics of Nodal Prediction

Research examining the performance of nodal prediction in HCC reveals the inherent challenges facing the TNM system's N classification. A large-scale study utilizing the SEER database evaluated multiple predictive approaches, including traditional TNM-based nomograms and more sophisticated models [6]. The results demonstrate the variable performance of different predictive strategies, with sensitivity values ranging from 0.66 to 0.78 and specificity values ranging from 0.50 to 0.75 across different cohorts and validation sets [6].

These performance metrics highlight the fundamental tension between diagnostic specificity and treatment timing. High sensitivity ensures that patients with nodal metastasis are identified promptly, enabling timely escalation of treatment. However, the moderate specificity observed in these studies indicates that a substantial proportion of patients classified as N1 may not actually harbor nodal disease, potentially leading to overtreatment and associated morbidity. Conversely, imperfect sensitivity means some patients with nodal involvement may be understaged, potentially delaying necessary treatment.

The external validation cohorts in these studies demonstrate somewhat degraded performance compared to training sets, suggesting that predictive models may not generalize well across different populations and clinical settings [6]. This variability further complicates the balance between diagnostic accuracy and treatment timing, as clinicians must consider the limitations of nodal prediction when making treatment decisions.

### 3.4 Evolution of N Classification in AJCC Editions

The evolution of N classification across AJCC editions reflects ongoing efforts to improve the balance between diagnostic specificity and clinical utility. The change from a binary N1/N0 classification in the 7th edition to a stratified approach in the 8th edition for other hepatobiliary malignancies acknowledges the prognostic significance of nodal burden [4]. For gallbladder and cholangiocarcinoma, the 8th edition distinguishes between N1 (1-3 involved nodes) and N2 (≥4 involved nodes), with N2 disease carrying significantly worse overall survival.

However, HCC has retained the binary N classification, likely reflecting the lower incidence of nodal metastasis and the associated challenges in developing a meaningful stratification system [4]. This conservative approach prioritizes simplicity and consistency over granular prognostic discrimination, but it limits the TNM system's ability to provide nuanced predictions regarding lymph node involvement and its implications for treatment timing.

The AJCC manual notes that N2 and T4 disease are prognostically equivalent, as either condition upgrades disease to at least stage III [4]. This equivalence reflects the poor prognosis associated with either extensive nodal involvement or major vascular invasion, suggesting that the TNM system recognizes the clinical significance of both tumor burden and nodal status. However, this equivalence does not resolve the underlying tension between diagnostic specificity and treatment timing, as the binary N classification still limits precise risk stratification.

## 4. The Balance: Diagnostic Specificity versus Treatment Timing

### 4.1 Fundamental Tension in Staging Philosophy

The TNM staging system embodies a fundamental tension between diagnostic specificity and treatment timing that manifests most clearly in the comparison of tumor burden quantification and lymph node metastasis prediction. Tumor burden assessment through T classification offers high anatomical specificity, with clear, measurable criteria that enable consistent staging across clinical settings. This specificity supports treatment planning by providing reliable information about disease extent and prognosis. However, the anatomical focus excludes critical factors such as hepatic function and tumor biology that influence treatment tolerance and response.

Lymph node metastasis prediction presents the opposite challenge: while nodal status carries significant prognostic implications, the low incidence of nodal involvement in HCC and the limitations of current detection methods compromise diagnostic specificity. The binary N classification in TNM simplifies staging but may not adequately capture the spectrum of nodal involvement, potentially leading to both over-treatment of false positives and under-treatment of missed metastases. This uncertainty directly impacts treatment timing, as clinicians must weigh the risks of delayed treatment against the risks of overtreatment based on imperfect nodal assessment.

### 4.2 Impact on Clinical Decision-Making

The balance between diagnostic specificity and treatment timing significantly influences clinical decision-making in HCC management. For patients with early-stage disease (T1-T2, N0), the high specificity of tumor burden assessment supports confident selection of curative-intent treatments, with treatment timing guided primarily by tumor characteristics and hepatic function rather than nodal concerns. The low probability of nodal involvement in this population means that N classification has limited impact on treatment decisions, and the binary N0/N1 distinction provides sufficient information for most clinical scenarios.

As tumor burden increases, the importance of accurate nodal assessment grows, but the challenges of lymph node metastasis prediction become more consequential. Patients with T3-T4 tumors face higher risks of nodal involvement, making accurate N classification more critical for treatment planning. However, the limitations of current predictive methods create uncertainty that may either delay appropriate treatment (if clinicians await pathological confirmation) or lead to overtreatment (if empirical nodal treatment is administered based on imaging findings).

The treatment timing implications extend beyond the selection of primary therapy to include decisions regarding adjuvant treatment and surveillance intensity. Patients with confirmed nodal metastasis (N1) may benefit from more aggressive adjuvant approaches, while those with suspected but unconfirmed nodal disease present management dilemmas that balance the risks of undertreatment against treatment-related morbidity.

### 4.3 Comparative Performance of Staging Systems

Comparative analyses of HCC staging systems provide insight into how different approaches balance diagnostic specificity and treatment timing. Studies evaluating seven staging systems—including TNM, BCLC, CLIP, JIS, CUPI, CIS, and Okuda—have demonstrated variable performance in predicting mortality [11]. The TNM system consistently showed lower predictive value compared to systems incorporating hepatic function, with CLIP demonstrating the highest area under curve (AUC) values for mortality prediction [11].

These findings suggest that the TNM system's anatomical specificity, while valuable for surgical planning, may be insufficient for comprehensive prognostic assessment and treatment timing in HCC. The exclusion of hepatic function—a critical determinant of treatment tolerance and overall survival—limits the system's ability to guide treatment decisions that require balancing disease extent with patient physiological reserve.

However, the TNM system demonstrates particular strength in specific clinical contexts. For patients treated with hepatic resection or transplantation, TNM remains the only validated staging system and performs better than clinical staging systems in predicting prognosis after resection [4]. This superiority reflects the system's anatomical precision, which is particularly relevant for surgical decision-making where accurate assessment of tumor extent and vascular involvement directly impacts resectability and surgical planning.

### 4.4 Integration of Emerging Predictive Approaches

The limitations of conventional TNM-based nodal prediction have motivated the development of more sophisticated predictive approaches. Traditional TNM nomograms typically incorporate only single clinical variables and neglect tumor biology and multidimensional patient data, limiting their predictive accuracy [6]. Recent studies have explored radiomics, artificial intelligence, and integration of pathological and genetic information to improve prognostic prediction [1].

These innovative approaches show promise for enhancing the balance between diagnostic specificity and treatment timing. Machine learning models incorporating multiple clinical, radiological, and molecular variables may achieve superior discrimination for lymph node metastasis prediction compared to traditional TNM-based approaches [6]. However, these systems still lack practical and clinical application, and their complexity may limit widespread adoption in routine clinical practice [1].

The tumor burden score represents a more immediately applicable innovation that enhances tumor burden quantification while maintaining the anatomical specificity of TNM [9]. By combining tumor size and number into a single metric, TBS provides more granular prognostic discrimination than categorical T classification alone, potentially improving treatment timing decisions without requiring fundamental changes to staging infrastructure.

## 5. Clinical Implications and Future Directions

### 5.1 Current Clinical Recommendations

Based on the analysis of TNM staging and its balance between diagnostic specificity and treatment timing, several clinical recommendations emerge for HCC management. First, T classification should remain central to treatment planning, with the anatomical specificity of tumor burden assessment guiding decisions regarding surgical resection, transplantation, and locoregional therapies. The clear criteria of T1-T4 categories provide reliable information for treatment selection, particularly for curative-intent approaches where complete tumor removal or destruction is the goal.

Second, N classification should be interpreted with awareness of its limitations, particularly the moderate sensitivity and specificity of nodal prediction. For patients with imaging findings suspicious for nodal metastasis, pathological confirmation through biopsy should be considered when feasible, as this provides the highest diagnostic specificity and directly impacts treatment planning. However, the low yield of biopsy in suspected nodal disease—given the overall low incidence of lymph node involvement—must be weighed against the risks and delays associated with invasive procedures.

Third, hepatic functional assessment should complement TNM staging in treatment decision-making, despite the TNM system's exclusion of this critical factor. The Child-Pugh score and albumin-bilirubin (ALBI) grade provide essential information regarding treatment tolerance and should guide the selection of appropriate therapies within each TNM stage [5]. This integration acknowledges that optimal treatment timing requires balancing disease extent with physiological reserve.

### 5.2 Limitations of Current Staging Approaches

Several limitations of current TNM-based staging warrant acknowledgment. The binary N classification fails to capture the spectrum of nodal involvement, potentially missing clinically meaningful distinctions between patients with single versus multiple involved nodes or limited versus extensive nodal disease. While the low incidence of nodal metastasis in HCC limits the statistical power for developing more granular classifications, the clinical significance of nodal burden for individual patients remains substantial.

The exclusion of hepatic function from TNM staging represents a fundamental limitation that is partially addressed by complementary staging systems but creates inconsistency in clinical practice. The variable characteristics and emphases between different classical HCC staging systems cause clinical selection to be inconsistent, with no clear consensus on which system is most appropriate for specific clinical scenarios [1].

Furthermore, the retrospective nature of many comparative studies introduces selection bias and limits generalizability. Prospective validation of staging systems in diverse populations—particularly within the Chinese mainland and other regions with high HCC incidence—is needed to establish robust evidence for clinical application [1].

### 5.3 Future Directions for Staging Development

Future development of HCC staging should focus on improving the balance between diagnostic specificity and treatment timing through several potential approaches. First, refinement of N classification to incorporate nodal burden—potentially distinguishing between single and multiple involved nodes—could enhance prognostic discrimination while maintaining clinical simplicity. The experience of other hepatobiliary malignancies with stratified N classification provides a template for this evolution [4].

Second, integration of hepatic function into TNM-based staging, either through modification of the existing system or through complementary assessment tools, could address the current gap in treatment tolerance prediction. The success of clinical staging systems like BCLC in incorporating liver function suggests that hybrid approaches may offer advantages over purely anatomical or purely clinical systems.

Third, development and validation of predictive models incorporating radiomics, artificial intelligence, and molecular markers could enhance both tumor burden quantification and lymph node metastasis prediction. While current innovative systems lack practical application, continued development may eventually enable more precise prognostication and treatment response prediction [1].

Finally, prospective comparative studies across diverse populations and clinical settings are needed to establish evidence-based recommendations for staging system selection. The current lack of consensus regarding optimal staging for specific clinical scenarios reflects the need for rigorous comparative effectiveness research that considers both diagnostic accuracy and treatment timing implications.

## 6. Conclusion

The TNM staging system for hepatocellular carcinoma navigates a complex balance between diagnostic specificity and treatment timing when quantifying tumor burden versus predicting lymph node metastasis. The T classification provides high anatomical specificity through clear, measurable criteria that support confident treatment planning, particularly for surgical candidates where tumor extent directly impacts resectability. However, the exclusion of hepatic function limits the system's ability to guide treatment timing decisions that require balancing disease extent with physiological reserve.

The N classification presents the opposite challenge: while nodal status carries significant prognostic implications, the binary classification and limitations of current detection methods compromise diagnostic specificity. The moderate sensitivity and specificity of nodal prediction create tension between avoiding delayed treatment for true nodal metastasis and preventing overtreatment based on false-positive findings.

This balance has direct implications for clinical practice. For early-stage disease, T classification provides sufficient information for treatment planning, with N classification having limited impact due to the low probability of nodal involvement. For advanced disease, accurate nodal assessment becomes more critical but also more challenging, creating management dilemmas that require careful consideration of the limitations of current predictive methods.

Future development of HCC staging should focus on refining N classification, integrating hepatic function assessment, and validating innovative predictive approaches that enhance the balance between diagnostic accuracy and treatment timing. Until such advances are realized, clinicians must remain aware of the inherent limitations of TNM staging and complement anatomical assessment with hepatic functional evaluation and appropriate use of pathological confirmation when indicated.

The optimal balance between diagnostic specificity and treatment timing ultimately requires individualized assessment that considers not only disease extent but also patient characteristics, treatment options, and the inherent uncertainties of current staging approaches. This nuanced approach acknowledges that staging systems provide frameworks for clinical decision-making rather than definitive answers, with the goal of supporting personalized treatment strategies that optimize outcomes for patients with hepatocellular carcinoma.

---

## References

[1] PMC11732340 - Classical hepatocellular carcinoma (HCC) staging systems are still the mainstream tool for stratification and prognosis prediction of patients with hepatocellular carcinoma. However, the variable characteristics and emphases between different classical HCC staging systems cause the clinical selection to be inconsistent.

[2] PMC12593328 - In the United States, the American Joint Committee on Cancer TNM system is most commonly used and assesses tumor size (T), lymph node involvement (N), and distant metastasis (M).

[3] Oncolink - The AJCC system for staging for liver cancer is based on the size of your tumor seen on imaging tests, if the lymph nodes have cancer cells in them, and any evidence of spread to other organs.

[4] AJR - The change in the N category from a binary (N1 or N0) classification in the 7th edition to a stratified approach in the 8th edition reflects the significantly worse overall survival of patients with four or more involved LNs.

[5] PMC12593328 - Although the TNM system provides a detailed assessment of the extent of liver cancer, it does not account for liver function. To address this limitation, other staging systems have been developed that incorporate both tumor characteristics and liver function.

[6] PMC12289565 - Proposed imaging predictors, including hilar invasion or a short-axis lymph node diameter ≥9 mm, have demonstrated variable sensitivity and specificity, reflecting the low incidence of HCC nodal metastasis (1.23%–7.5%).

[7] eMedicine - T1a: Solitary tumor ≤2 cm; T1b: Solitary tumor >2 cm without vascular invasion; T2: Solitary tumor >2 cm with vascular invasion, or multiple tumors, none >5 cm; T3: Multiple tumors, at least one >5 cm; T4: Major vascular invasion.

[8] EASL - Contrast-enhanced imaging methods are necessary for the diagnosis of HCC and are based on vascular phases, with the typical hallmark being hypervascularity in late arterial phase and wash-out on portal venous and/or delayed phases.

[9] ScienceDirect - TBS exhibited best discrimination within these predictive models, as evidenced by the highest c-index and area under curve values of time-dependent receiver operating curves within 5 years post-surgery.

[10] eMedicine - TNM is the only validated system in patients treated with hepatic resection or transplant and seems to perform better than clinical systems in predicting prognosis after resection.

[11] Spandidos - CLIP had the highest AUC for predicting mortality, while TNM showed lower predictive value compared to CLIP, CIS, and JIS systems in patients with advanced HBV-associated HCC.

## Annotations


## Sources
[1] http://www.breastsurgeonsweb.com/wp-content/uploads/downloads/2020/10/AJCC-Breast-Cancer-Staging-System.pdf
[2] https://apm.amegroups.org/article/view/64818/html
[3] https://cco.amegroups.org/article/view/2528/html
[4] https://easl.eu/wp-content/uploads/2018/10/EASL-CPG-Management-of-hepatocellular-carcinoma-.pdf
[5] https://emedicine.medscape.com/article/2007061-overview
[6] https://pmc.ncbi.nlm.nih.gov/articles/PMC10953220/
[7] https://pmc.ncbi.nlm.nih.gov/articles/PMC11732340/
[8] https://pmc.ncbi.nlm.nih.gov/articles/PMC12049291/
[9] https://pmc.ncbi.nlm.nih.gov/articles/PMC12289565/
[10] https://pmc.ncbi.nlm.nih.gov/articles/PMC12446205/
[11] https://pmc.ncbi.nlm.nih.gov/articles/PMC12593328/
[12] https://pmc.ncbi.nlm.nih.gov/articles/PMC4381166/
[13] https://pmc.ncbi.nlm.nih.gov/articles/PMC5605901/
[14] https://www.ajronline.org/doi/10.2214/AJR.19.22636
[15] https://www.albertahealthservices.ca/assets/info/hp/cancer/if-hp-cancer-guide-systemic-therapy-early-breast.pdf
[16] https://www.cancer.gov/about-cancer/diagnosis-staging/staging
[17] https://www.cancer.gov/types/liver/hp/adult-liver-treatment-pdq
[18] https://www.cancer.org/cancer/types/liver-cancer/detection-diagnosis-staging/staging.html
[19] https://www.clinicsinoncology.com/open-access/enhancing-tnm-staging-in-breast-cancer-a-hybrid-approach-with-9781.pdf
[20] https://www.entnet.org/wp-content/uploads/files/NeckDissection_QuickRefGuide_highresFINAL.pdf
[21] https://www.facs.org/media/j30havyf/ajcc_7thed_cancer_staging_manual.pdf
[22] https://www.nature.com/articles/s41392-023-01576-4
[23] https://www.nature.com/articles/s41392-024-01885-2
[24] https://www.oaepublish.com/articles/2394-5079.2024.60
[25] https://www.oncolink.org/cancers/gastrointestinal/liver-cancer-hepatoma/liver-cancer-staging-and-treatment
[26] https://www.sciencedirect.com/science/article/pii/S0748798324006620
[27] https://www.spandidos-publications.com/10.3892/ol.2017.6222