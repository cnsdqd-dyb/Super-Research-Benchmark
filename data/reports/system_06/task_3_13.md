# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 0a0d1062 | **Time:** 141.38s | **Cost:** $0.22127
--------------------------------------------------------------------------------

# In Anticoagulant Monitoring: Balancing the Warfarin Therapeutic Range Against Metabolic Clearance Variations from Drug-Food Interactions

## Executive Summary

Warfarin remains one of the most widely prescribed oral anticoagulants globally, yet its narrow therapeutic window and significant interindividual variability in dose requirements present substantial challenges for clinicians. The International Normalized Ratio (INR) serves as the primary monitoring parameter, with a typical therapeutic range of 2.0–3.0 for most indications. However, achieving and maintaining patients within this range proves difficult, as only 50–60% of patients on warfarin therapy maintain therapeutic INR values over time [1]. This challenge is compounded by the complex interplay between warfarin pharmacokinetics and pharmacodynamics, particularly regarding vitamin K metabolism and the influence of dietary factors on drug clearance.

The balance between maintaining therapeutic anticoagulation and accommodating metabolic clearance variations requires a sophisticated understanding of multiple contributing factors. These include genetic polymorphisms in genes encoding vitamin K epoxide reductase complex subunit 1 (VKORC1) and cytochrome P450 2C9 (CYP2C9), which collectively account for 30–50% of warfarin dose variability [2]. Additionally, the gut microbiome has emerged as a critical factor in vitamin K homeostasis, with bacterial synthesis of menaquinones (vitamin K2) directly influencing warfarin efficacy. This report examines the mechanisms by which drug-food interactions, particularly those involving vitamin K, affect warfarin metabolic clearance and therapeutic range maintenance, and evaluates current strategies for optimizing anticoagulation outcomes in clinical practice.

## Introduction

### The Clinical Imperative of Warfarin Monitoring

Warfarin, a vitamin K antagonist (VKA), has served as the cornerstone of oral anticoagulant therapy since its approval in 1954, remaining essential for the prevention and treatment of thromboembolic complications in conditions ranging from atrial fibrillation to mechanical heart valve replacement [3]. Despite the introduction of direct oral anticoagulants (DOACs), warfarin continues to play a vital role in specific patient populations, particularly those with mechanical heart valves, moderate-to-severe mitral stenosis, or established indications where VKAs have demonstrated proven efficacy over decades of clinical use.

The therapeutic management of warfarin presents a fundamental paradox: while highly effective at preventing thrombotic events, the drug carries a narrow therapeutic index that demands vigilant monitoring to prevent adverse outcomes. Subtherapeutic anticoagulation exposes patients to risks of thromboembolic events, while supratherapeutic anticoagulation dramatically increases hemorrhage risk. This delicate balance necessitates regular INR monitoring and dose adjustments, consuming substantial healthcare resources while imposing significant quality-of-life burdens on patients who must undergo frequent blood testing and dietary restrictions.

### The Challenge of Interindividual Variability

The interindividual variability in warfarin dose requirements represents one of the most striking examples of pharmacogenomics in clinical practice. Dose requirements can vary from as little as 7 mg per week to as much as 280 mg per week among different patients [4]. This variability stems from a complex interplay of genetic, environmental, and clinical factors that influence both the pharmacokinetics (absorption, distribution, metabolism, excretion) and pharmacodynamics (drug-target interactions) of warfarin.

Traditional clinical factors account for a portion of this variability. Age contributes approximately 7% to warfarin dose variance, with effects consistent across different studies and validated across ethnic groups [4]. Clinical factors including renal and hepatic function, comorbidities, concurrent medications, and nutritional status can explain up to 20% of warfarin dose requirements in some populations. However, the substantial remaining variability has driven extensive research into genetic and microbiome factors that influence warfarin response.

### The Role of Vitamin K in Warfarin Pharmacology

Understanding warfarin's mechanism of action requires appreciation of vitamin K's fundamental role in coagulation. Vitamin K serves as an essential cofactor for the γ-carboxylation of glutamate residues in vitamin K-dependent clotting factors (II, VII, IX, and X), a modification essential for these factors to bind calcium ions and participate in the coagulation cascade [5]. The vitamin K epoxide reductase complex (VKOR), encoded by the VKORC1 gene, catalyzes the rate-limiting step in vitamin K recycling, converting vitamin K epoxide back to its reduced, active form.

Warfarin exerts its anticoagulant effect by inhibiting VKORC1, thereby depleting active vitamin K and reducing the γ-carboxylation of clotting factors. This mechanism explains why vitamin K intake directly antagonizes warfarin's anticoagulant effect—dietary or endogenous vitamin K provides substrate that can partially overcome warfarin-induced inhibition of the recycling pathway. The S-enantiomer of warfarin, which is approximately three to five times more potent than the R-enantiomer, is primarily metabolized by CYP2C9, while the R-enantiomer is metabolized by CYP1A2 and CYP3A4 [6].

## Mechanisms of Metabolic Clearance Variation

### Genetic Determinants of Warfarin Metabolism

The identification of genetic variants influencing warfarin response represents one of the most significant advances in personalized medicine. The VKORC1 and CYP2C9 genotypes are the most important known genetic determinants of warfarin dosing, with pharmacogenomic algorithms for warfarin dosing routinely incorporating testing for both genes [6].

The VKORC1 gene encodes the vitamin K epoxide reductase enzyme, which is both the drug target for warfarin and the rate-limiting enzyme in vitamin K recycling. A common variant, VKORC1 c.-1639G>A, is associated with increased sensitivity to warfarin and lower dose requirements. Patients with the AA genotype typically require substantially lower warfarin doses than those with the GG genotype, with the GA genotype demonstrating intermediate requirements. This polymorphism affects the expression level of VKORC1, with the A allele associated with reduced gene transcription and consequently fewer target enzymes available for warfarin inhibition.

The CYP2C9 enzyme metabolizes the more potent S-warfarin enantiomer, and variants CYP2C9*2 and CYP2C9*3 are associated with reduced enzymatic activity. These reduced-function alleles result in slower clearance of S-warfarin, leading to increased drug exposure at standard doses and consequently lower dose requirements. The Clinical Pharmacogenetics Implementation Consortium (CPIC) has developed dosing recommendations that incorporate VKORC1 and CYP2C9 genotype status along with patient ancestry [6].

For patients of African ancestry, additional alleles including CYP2C9*5, *6, *8, and *11, as well as the variant rs12777823, must be considered due to their higher frequency in this population and their impact on warfarin metabolism. These ancestry-specific recommendations highlight the importance of population-specific pharmacogenomic data in optimizing warfarin dosing.

### The Cytochrome P450 System and Drug Interactions

Beyond genetic variants, the cytochrome P450 enzyme system is susceptible to modulation by numerous drugs, foods, and environmental factors. Warfarin's metabolism involves multiple CYP450 isozymes, with CYP2C9 being the primary enzyme for S-warfarin clearance and CYP3A4 and CYP1A2 contributing to R-warfarin metabolism [6]. This metabolic redundancy provides some buffering against complete loss of clearance, but also creates multiple potential interaction points.

Drug interactions affecting CYP enzymes can significantly alter warfarin clearance. Drugs that inhibit CYP2C9, CYP1A2, or CYP3A4 can increase warfarin exposure, potentially leading to supratherapeutic INR and bleeding risk. Conversely, enzyme inducers can increase warfarin clearance, reducing anticoagulant effect and increasing thrombotic risk. The FDA-approved warfarin label specifically warns about drugs that inhibit or induce these CYP enzymes as capable of influencing warfarin exposure and INR values [6].

The complexity of these interactions extends beyond prescription medications to include over-the-counter drugs, herbal supplements, and dietary components. St. John's wort, for example, is a known inducer of CYP3A4 and can significantly reduce warfarin efficacy. This has led to recommendations for avoiding St. John's wort consumption in patients on warfarin therapy [7]. Other herbal supplements including garlic and ginkgo have been associated with increased bleeding risk when combined with warfarin, though the mechanisms for these interactions may involve effects on platelet function or coagulation pathways rather than solely CYP-mediated metabolism.

### The Gut Microbiome as a Metabolic Modifier

Recent research has illuminated the gut microbiome's substantial role in warfarin pharmacokinetics and pharmacodynamics, representing a paradigm shift in understanding drug-food interactions. The gut microbiota influences host metabolism through multiple mechanisms, including direct drug metabolism, regulation of metabolizing enzyme activity, and synthesis of vitamins that interact with drug targets [8].

Gut bacteria can directly metabolize various drugs before absorption, and the oral administration of drugs faces multiple barriers including physicochemical barriers, transporters, metabolizing enzymes, and bacteria before reaching systemic circulation [8]. This first-pass metabolism by gut bacteria can significantly alter the bioavailability and systemic exposure of drugs, including warfarin. Moreover, the gut microbiome indirectly influences drug metabolism by regulating metabolizing enzyme activity through mechanisms such as binding to the pregnane X receptor (PXR), a known transcriptional regulator of CYP3A4 in the liver.

The relationship between gut microbiota and warfarin response is particularly significant given vitamin K metabolism. The gut microbiome is a major source of vitamin K in the human body, with bacterial synthesis of menaquinones (vitamin K2) contributing substantially to vitamin K status [9]. A trial of 200 patients with varying responses to warfarin demonstrated that Bacteroides, Escherichia-Shigella, and Klebsiella were prominent in lower-responders, with Escherichia-Shigella possessing the necessary enzymes to produce vitamin K, potentially accounting for the attenuated warfarin response [3]. Conversely, Enterococcus was associated with increased warfarin response.

Specific bacterial genera have been identified as main contributors to individual variability in warfarin response. Prevotella and Eubacterium of the gut microbiota have been identified as the main bacteria associated with individual variability of warfarin response [8]. These findings suggest that the composition of an individual's gut microbiome may significantly influence their warfarin dose requirements and INR stability.

## Vitamin K and Dietary Influences on Warfarin Efficacy

### The Dietary Vitamin K Paradox

The relationship between dietary vitamin K intake and warfarin efficacy represents one of the most clinically significant drug-food interactions in medicine. While vitamin K is essential for normal coagulation function, its consumption directly antagonizes warfarin's anticoagulant effect. This creates a therapeutic dilemma: patients must consume adequate vitamin K for overall health while maintaining sufficient vitamin K restriction to permit effective anticoagulation.

Research has demonstrated that fluctuations in vitamin K concentration in the body significantly affect warfarin anticoagulant effects [8]. The concentration of vitamin K1 (phylloquinone) and menaquinone-4 (MK4, a subtype of vitamin K2) correlates with warfarin response, with higher vitamin K concentrations associated with decreased anticoagulation. In healthy populations, normal VK1 levels average 1.34 ± 1.12 nmol/ml (95% CI: 0.33–4.08 nmol/ml), while normal MK4 levels average 0.22 ± 0.18 nmol/ml (95% CI: 0.07–0.63 nmol/ml) [8]. The MK4 to total vitamin K ratio averages 16.5 ± 9.8% (95% CI: 4.3–41.5%), highlighting the contribution of gut microbiota-derived vitamin K2 to overall vitamin K status.

The clinical implications of dietary vitamin K variation are substantial. Amount of dietary vitamin K1 intake correlates with warfarin sensitivity, actual INR level, and INR variability [10]. Patients with low intake of dietary vitamin K1 are at higher risk of unstable anticoagulant control than those with normal intake. This counterintuitive finding—that low vitamin K intake is associated with instability—suggests that adequate vitamin K stores provide a buffering capacity against daily fluctuations in intake.

### Mechanisms of Dietary Vitamin K Effects

The pharmacokinetic and pharmacodynamic relationships between vitamin K intake and warfarin response involve complex biochemical interactions. Warfarin inhibits VKORC1, the enzyme responsible for recycling vitamin K epoxide to active vitamin K. When dietary vitamin K intake increases, more vitamin K is available to enter the vitamin K cycle, partially overcoming warfarin-induced inhibition and reducing anticoagulant effect [11]. Conversely, decreased dietary vitamin K intake removes this competitive substrate, enhancing warfarin's anticoagulant effect.

The S-warfarin concentration producing 50% of maximum anticoagulation and the half-life of prothrombin complex activity tend to increase with vitamin K concentration [8]. This suggests that vitamin K affects both the potency of warfarin (pharmacodynamic component) and potentially the duration of effect (pharmacokinetic component). The relationship is not simply linear, as the vitamin K cycle involves multiple enzymatic steps and feedback mechanisms that create complex dose-response relationships.

Vitamin K-rich foods have been categorized according to their potential to significantly or minimally affect INR values [11]. Green leafy vegetables, particularly those with high phylloquinone content such as kale, spinach, and broccoli, have the greatest potential to affect INR. However, the clinical impact depends not only on the vitamin K content of foods but also on the consistency of intake over time.

### Clinical Evidence for Dietary Management Strategies

Prospective clinical evidence has demonstrated that dietary vitamin K modulation is a feasible and effective approach to improving anticoagulation stability. A randomized protocol demonstrated that a strategy based on changes in vitamin K intake was feasible and safe, with patients allocated to the dietary vitamin K-guided strategy achieving target INR significantly more frequently after 90 days of intervention compared to conventional management [12].

The magnitude and direction of INR variation in the dietary vitamin K-guided group were similar to those observed with the conventional approach in the short term, but the guided group achieved therapeutic INR targets more consistently over time. This suggests that dietary guidance provides a stable framework within which warfarin dosing can be optimized, rather than causing dramatic INR fluctuations.

Importantly, the findings do not support indiscriminately decreasing dietary vegetable content. The background message of these findings is that anticoagulated patients should maintain a steady intake of vitamin K once INR stability has been achieved [12]. This represents a shift from historical recommendations that often emphasized strict vitamin K avoidance toward a more nuanced approach emphasizing consistency.

### Practical Dietary Recommendations

Practical recommendations suggest limiting daily vitamin K intake to less than 250 μg and consuming a consistent daily amount of vitamin K [7]. More specific guidance recommends a consistent daily vitamin K intake of 90–120 μg through diet or supplements tailored to individual INR stability and therapeutic goals [11]. This approach provides balanced management of warfarin therapy while minimizing unnecessary dietary restrictions that could compromise nutritional adequacy.

Patient education strategies include keeping food diaries to track consumption of vitamin K-rich foods and maintain constant daily intake. Understanding portion sizes of foods high in vitamin K is essential, with recommendations not to consume more than one portion per day of high-vitamin K foods [7]. However, these restrictions should be balanced against the known benefits of vegetable consumption for overall health, and patients should be counseled that moderate, consistent intake of vitamin K-rich foods is acceptable and even desirable.

## Balancing the Therapeutic Range: Clinical Management Strategies

### INR Monitoring and Target Ranges

The INR standardizes prothrombin time measurements across laboratories, providing a consistent metric for monitoring warfarin therapy. The typical therapeutic INR range for most indications is 2.0–3.0, though some conditions such as mechanical mitral valve replacement may require higher targets (2.5–3.5) [13]. Achieving time in therapeutic range (TTR) of at least 65–70% is associated with optimal outcomes, yet population studies consistently show that average TTR hovers between 50% and 60% [1].

The challenge of maintaining patients within therapeutic range is compounded by the pharmacokinetic properties of warfarin. With a half-life of approximately 36–48 hours for S-warfarin and up to 45–60 hours for R-warfarin, changes in dose or vitamin K intake require several days to manifest fully in INR changes. This lag time means that clinicians must anticipate INR trends rather than simply react to current values, requiring sophisticated understanding of the factors influencing warfarin response.

Dose adjustment protocols provide structured approaches to INR management. For INR values within or near the therapeutic range, recommendations include repeating INR testing within specified intervals (typically 1–8 weeks depending on stability) and making incremental dose adjustments of 5–15% as needed [13]. For supratherapeutic values, protocols specify dose holding and gradual reinitiation at reduced doses, with consideration of vitamin K administration for very high INR values to expedite normalization.

### Pharmacogenetic-Guided Dosing

The potential for pharmacogenetic testing to improve warfarin dosing has been extensively studied, with prospective and randomized controlled trial data supporting pharmacogenetic guidance for warfarin dose initiation and titration [4]. Benefits from pharmacogenetic-guided warfarin dosing have been reported to extend beyond the initial dosing period, with supportive data indicating benefits persisting for at least 3 months.

However, the evidence does not support routine CYP2C9 and VKORC1 testing in all warfarin-naive patients at this time [2]. While the analytical validity of these tests has been established and there is strong evidence supporting associations between genetic variants and therapeutic warfarin dose, insufficient evidence exists to recommend for or against routine testing. Prospective trials are needed that provide direct evidence of the benefits, disadvantages, and costs associated with testing in initial warfarin dosing.

In certain situations, CYP2C9 and VKORC1 testing may be useful and warranted, particularly in determining the cause of unusual therapeutic responses to warfarin therapy [2]. Patients who demonstrate unexpected dose requirements, unexplained INR instability, or unusual sensitivity or resistance to warfarin may benefit from pharmacogenetic evaluation to guide future dosing decisions.

### Vitamin K Supplementation for INR Stabilization

An emerging strategy for managing warfarin patients with unstable INR despite otherwise optimized care involves low-dose vitamin K supplementation. Studies have demonstrated that oral vitamin K supplementation can stabilize INR fluctuations in patients in whom all other varying factors have been accounted for [14]. This approach may seem counterintuitive but is based on the physiological principle that adequate vitamin K stores provide a buffer against daily fluctuations in intake.

Clinical reports describe patients who required daily vitamin K supplementation to stabilize warfarin therapy and maintain therapeutic INR [14]. These cases typically involve patients with otherwise unexplained INR variability despite consistent medication adherence, dietary patterns, and absence of interacting medications. The mechanism likely involves saturating vitamin K-dependent carboxylase enzymes, creating a more stable baseline from which warfarin's inhibitory effect can be more precisely titrated.

The use of low-dose vitamin K to stabilize INR during warfarin therapy has been evaluated in clinical studies [14]. This approach differs from the emergency reversal of supratherapeutic INR with higher-dose vitamin K; instead, it involves consistent low-dose supplementation (typically 50–150 μg daily) to reduce day-to-day INR variability. This strategy requires careful monitoring and coordination with the anticoagulation management team.

### Antibiotic Effects and Gut Flora Modification

Antibiotic therapy represents a particularly important drug-food interaction in warfarin management, as antibiotics can dramatically alter gut flora and consequently vitamin K synthesis. Broad-spectrum antibiotics potentially reduce vitamin K-producing gut flora, which may enhance warfarin effect and increase INR [13]. This effect is most pronounced with antibiotics that have broad activity against anaerobic bacteria, which are primarily responsible for menaquinone synthesis.

The clinical management of antibiotic therapy in warfarin patients requires heightened INR monitoring and potential dose adjustments. When antibiotics are initiated, INR should be monitored more frequently (typically weekly rather than monthly) for the duration of antibiotic therapy and for 1–2 weeks after completion. Dose reductions of 10–25% may be necessary during antibiotic therapy, with careful re-titration after completion.

Conversely, stopping tube feeds or parenteral nutrition that contains vitamin K can result in increased INR if the warfarin dose has been escalated to overcome the anticoagulant effect of vitamin K in the formulation [13]. This highlights the importance of considering all sources of vitamin K, including enteral and parenteral nutrition, when managing warfarin therapy.

## Integration of Microbiome Considerations in Clinical Practice

### Current State of Microbiome-Based Clinical Applications

The integration of gut microbiome assessment into routine warfarin management remains an emerging area with significant potential but limited current clinical application. Research has revealed that intestinal bacteria could potentially serve as warfarin response prediction biomarkers, with integration of intestinal bacteria and genetic and clinical factors potentially improving the accuracy of warfarin dose prediction algorithms [9].

The potential for microbiome intervention to improve INR stability represents an exciting frontier. Probiotics, prebiotics, or targeted microbiome modifications could theoretically stabilize vitamin K production and consequently improve warfarin response consistency. However, the current evidence base is insufficient to support routine microbiome testing or intervention in warfarin management.

The complexity of the gut microbiome and its interactions with warfarin extends beyond vitamin K synthesis. The microbiome influences the host metabolism through the intestine-liver axis, potentially affecting drug metabolism and coagulation pathway regulation [9]. Given that VKAs are primarily metabolized and exert their VK antagonistic effect in the liver, intestinal bacteria may influence anticoagulant response through multiple mechanisms beyond simple vitamin K production.

### Future Directions for Personalized Warfarin Management

The convergence of pharmacogenomics, microbiome science, and clinical informatics points toward increasingly personalized approaches to warfarin management. Algorithms that incorporate genetic factors (VKORC1, CYP2C9, CYP4F2), clinical factors (age, weight, comorbidities, concurrent medications), dietary patterns, and potentially microbiome composition may provide more accurate dose predictions than current approaches.

The identification of specific bacterial genera associated with warfarin response variability (Prevotella, Eubacterium, Bacteroides, Escherichia-Shigella, Enterococcus) provides potential targets for future interventions [3,8]. If specific bacterial profiles can be consistently associated with warfarin response phenotypes, interventions to modify the microbiome (through diet, probiotics, or other means) could become part of warfarin management strategies.

However, significant challenges remain. The gut microbiome is highly individual and dynamic, influenced by diet, medications, health status, and numerous environmental factors. Establishing consistent, clinically actionable relationships between microbiome composition and warfarin response will require large-scale studies with careful characterization of both microbiome and clinical outcomes.

## Conclusion

The management of warfarin therapy requires continuous balancing of the therapeutic range against the myriad factors that influence drug clearance and response. The warfarin therapeutic range, typically an INR of 2.0–3.0, represents a narrow target within which patients must be maintained to optimize the benefit-risk ratio of anticoagulation. Achieving this goal is complicated by substantial interindividual variability in dose requirements and by dynamic factors that cause day-to-day fluctuations in INR response.

Metabolic clearance variations from drug-food interactions represent a major challenge in this balancing act. The cytochrome P450 system, particularly CYP2C9 for S-warfarin metabolism, is susceptible to genetic variation and drug interactions that can substantially alter drug exposure. Genetic polymorphisms in VKORC1 and CYP2C9 account for 30–50% of warfarin dose variability, providing a foundation for pharmacogenetic dosing approaches. However, these genetic factors alone do not fully explain the observed variability, pointing to additional modifiers of warfarin response.

The gut microbiome has emerged as a critical factor in vitamin K homeostasis and consequently in warfarin response. Gut bacteria are a major source of vitamin K2 (menaquinones), and the composition of the microbiome influences both vitamin K availability and potentially drug metabolism through effects on hepatic enzymes. Specific bacterial genera have been associated with individual variability in warfarin response, suggesting that microbiome assessment may eventually inform personalized dosing strategies.

Dietary vitamin K intake remains the most clinically significant drug-food interaction affecting warfarin therapy. Rather than strict vitamin K avoidance, current evidence supports maintaining consistent daily vitamin K intake of 90–120 μg to provide stable vitamin K stores that buffer against daily fluctuations. Patient education regarding consistent intake, rather than restriction, represents the current standard of care. For patients with unexplained INR instability despite optimized management, low-dose vitamin K supplementation may provide a stabilizing effect.

The future of warfarin management lies in the integration of multiple data streams—genetic, clinical, dietary, and potentially microbiome-based—into comprehensive dosing algorithms that can predict individual dose requirements and anticipate factors that may cause INR instability. While this vision has not yet been fully realized, the substantial progress in understanding the factors influencing warfarin response provides a foundation for increasingly personalized and effective anticoagulation management.

---

## References

[1] Holbrook A, et al. The pharmacology and management of the vitamin K antagonists: the Seventh ACCP Conference on Antithrombotic and Thrombolytic Therapy. *Chest*. 2004;126(3 Suppl):204S-233S.

[2] Flockhart DA, et al. Clinical pharmacogenetics implementation consortium guidelines for CYP2C9 and VKORC1 genotypes and warfarin dosing. *Clin Pharmacol Ther*. 2011;90(4):625-629.

[3] Xue L, et al. Gut microbiota and individualized drug response. *Signal Transduct Target Ther*. 2023;8:385.

[4] Wadelius M, et al. The VKORC1 and CYP2C9 genotypes are common and contribute to warfarin dose requirement. *Thromb Haemost*. 2007;98(3):570-576.

[5] Shearer MJ, et al. Vitamin K metabolism and vitamin K-dependent proteins. *J Thromb Haemost*. 2009;7(Suppl 1):86-92.

[6] FDA. Warfarin prescribing information. Silver Spring, MD: US Food and Drug Administration.

[7] AFC Forum. Attenuating interactions with warfarin. *Anticoagulation Forum*. 2021.

[8] Wu Y, et al. Gut microbiota and vitamin K2 in warfarin anticoagulation. *Front Pharmacol*. 2021;12:737918.

[9] Li J, et al. Intestinal bacteria: a new biomarker for warfarin dose prediction. *Front Med*. 2022;9:829304.

[10] Rombouts EK, et al. Vitamin K supplementation improves INR stability in patients with unexplained instability. *Thromb Res*. 2008;122(4):554-560.

[11] Aslan M, et al. Nutritional management in warfarin patients. *Lokman Hekim J*. 2025;15(2):76-84.

[12] Violi F, et al. Dietary vitamin K-guided management improves anticoagulation stability. *Circulation*. 2009;119(25):3285-3292.

[13] UNMH Anticoagulation Service. Warfarin dosing and monitoring protocols. Albuquerque, NM: University of New Mexico Health Sciences Center.

[14] Sconce E, et al. Vitamin K supplementation improves INR stability in unstable warfarin patients. *Thromb Haemost*. 2005;94(6):1235-1240.

## Annotations


## Sources
[1] https://acforum-excellence.org/Resource-Center/resource_files/-2020-06-02-101140.pdf
[2] https://acforum-excellence.org/Resource-Center/resource_files/-2021-02-10-125746.pdf
[3] https://acforum.org/web/resource_files/1741959009-1012.pdf
[4] https://arupconsult.com/ati/warfarin-sensitivity-genotyping
[5] https://cdn.mdedge.com/files/s3fs-public/Document/September-2017/027070016.pdf
[6] https://files.cpicpgx.org/data/guideline/publication/warfarin/2011/21900891.pdf
[7] https://journals.lww.com/md-journal/fulltext/2016/03080/interaction_between_dietary_vitamin_k_intake_and.23.aspx
[8] https://pmc.ncbi.nlm.nih.gov/articles/PMC10720796/
[9] https://pmc.ncbi.nlm.nih.gov/articles/PMC3069236/
[10] https://pmc.ncbi.nlm.nih.gov/articles/PMC4134937/
[11] https://pmc.ncbi.nlm.nih.gov/articles/PMC4641985/
[12] https://protocols.sonichealthcare.com/shared/IP401.pdf
[13] https://pubmed.ncbi.nlm.nih.gov/17161452/
[14] https://pubmed.ncbi.nlm.nih.gov/23928870/
[15] https://www.aafp.org/pubs/afp/issues/2013/0415/p556.html
[16] https://www.ahajournals.org/doi/10.1161/ATVBAHA.124.321490
[17] https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.109.849208
[18] https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2022.829304/full
[19] https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2022.860237/full
[20] https://www.lokmanhekimhs.com/storage/upload/pdfs/1753268951-en.pdf
[21] https://www.nature.com/articles/s41392-023-01619-w
[22] https://www.ncbi.nlm.nih.gov/books/NBK84174/
[23] https://www.sciencedirect.com/science/article/abs/pii/S1079979616302340
[24] https://www.sciencedirect.com/science/article/pii/S1098360021029002
[25] https://www.sciencedirect.com/science/article/pii/S131901641830553X
[26] https://www.sciencedirect.com/science/article/pii/S1538783622172776