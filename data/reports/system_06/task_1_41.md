# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** e333975c | **Time:** 479.63s | **Cost:** $0.20428
--------------------------------------------------------------------------------

# How Does Antiepileptic Drug Research Balance Seizure Control Thresholds with Metabolic Interaction Risks?

## A Technical Analysis of Contemporary Challenges in Epilepsy Pharmacotherapy

---

## Executive Summary

The pharmacological management of epilepsy represents one of the most complex balancing acts in modern therapeutics. Clinicians must navigate the imperative to achieve adequate seizure control while simultaneously managing the intricate web of metabolic interactions that can compromise therapeutic efficacy or precipitate adverse effects. This challenge has intensified as the therapeutic armamentarium has expanded to include over 30 antiepileptic drugs (AEDs), each with distinct pharmacokinetic profiles, enzyme-inducing or inhibiting properties, and variable responses across patient populations [1].

The fundamental tension in antiepileptic drug therapy arises from the narrow therapeutic indices characteristic of many AEDs, combined with the extensive involvement of hepatic cytochrome P450 (CYP) enzymes in their metabolism. Approximately 30% of patients develop drug-resistant epilepsy, necessitating combination therapy that exponentially increases the potential for clinically significant drug-drug interactions [1]. This report examines how contemporary research and clinical practice approaches this balance, exploring the roles of therapeutic drug monitoring, pharmacogenetic testing, individualized dosing strategies, and rational polytherapy design in optimizing patient outcomes.

---

## 1. Introduction: The Therapeutic Challenge in Epilepsy Management

Epilepsy remains one of the most prevalent neurological disorders globally, characterized by recurrent, unpredictable disruptions in brain function resulting from abnormal neuronal discharge [1]. Despite significant advances in antiepileptic drug development over recent decades, approximately one-third of patients fail to achieve adequate seizure control with monotherapy, necessitating more complex treatment regimens that introduce additional therapeutic variables and potential complications [1].

The challenge of balancing seizure control with metabolic safety concerns is multifaceted. On one hand, insufficient drug exposure results in treatment failure and continued seizure activity, with associated risks of injury, cognitive decline, and reduced quality of life. On the other hand, excessive drug exposure—whether from overdose, accumulation due to impaired clearance, or pharmacokinetic interactions—can produce dose-dependent adverse effects including cognitive impairment, sedation, ataxia, and, in severe cases, life-threatening toxicity [2][3].

Contemporary antiepileptic drug research has increasingly focused on understanding the metabolic pathways that govern drug disposition, the mechanisms by which drugs interact with each other and with endogenous enzyme systems, and the patient-specific factors that influence individual response. This knowledge base has enabled the development of more sophisticated approaches to treatment optimization, including therapeutic drug monitoring, pharmacogenetic-guided therapy, and rational combination strategies designed to maximize efficacy while minimizing interaction-related risks [4][5].

---

## 2. Cytochrome P450 Enzymes: The Metabolic Foundation of Drug Interactions

### 2.1 Enzyme Systems and Their Clinical Relevance

The cytochrome P450 enzyme system constitutes the primary metabolic machinery responsible for the biotransformation of xenobiotics, including the vast majority of antiepileptic drugs. This enzyme superfamily comprises more than 50 distinct isoforms, though a remarkably small subset accounts for the metabolism of the majority of drugs encountered in clinical practice [6]. Specifically, six enzymes metabolize approximately 90% of pharmaceuticals, with CYP3A4 and CYP2D6 emerging as the two most clinically significant isoforms [6].

The clinical importance of CYP450 enzymes in antiepileptic therapy stems from several interrelated factors. First, many AEDs are substrates for these enzymes, meaning their metabolism and clearance depend on enzymatic activity. Second, numerous AEDs function as enzyme inhibitors or inducers, capable of altering the metabolic capacity for themselves and for co-administered medications. Third, substantial genetic variability exists within the population regarding CYP450 enzyme expression and activity, leading to considerable interindividual differences in drug response [6].

The clinical consequences of CYP450-mediated drug interactions can be profound. Enzyme inhibition typically results in reduced metabolic clearance of affected drugs, leading to elevated plasma concentrations and increased risk of concentration-dependent adverse effects. Conversely, enzyme induction accelerates metabolism, potentially reducing drug exposure below therapeutic thresholds and compromising efficacy [6][7]. These interactions are particularly consequential in epilepsy management, where small changes in drug concentration can determine the difference between seizure freedom and breakthrough seizures.

### 2.2 Antiepileptic Drugs as Enzyme Modulators

The antiepileptic pharmacopeia includes numerous agents with significant capacity for enzyme modulation. Valproate, for example, functions as a potent CYP450 enzyme inhibitor and can substantially slow the metabolism of other drugs, leading to increased plasma concentrations and heightened adverse effect risk [7]. This property necessitates careful dose adjustment when valproate is combined with other agents and vigilant monitoring for signs of toxicity.

Conversely, enzyme-inducing AEDs such as carbamazepine, phenytoin, and phenobarbital enhance the expression and activity of CYP450 isoforms, accelerating the metabolism of both themselves and co-administered medications [7]. This induction effect can substantially reduce plasma concentrations of concomitant drugs, potentially compromising therapeutic efficacy. The induction process itself requires time to develop fully and persists for some period after drug discontinuation, adding temporal complexity to clinical management.

Modern AEDs exhibit varying degrees of CYP450 involvement. Some agents, such as levetracetam, undergo minimal CYP450 metabolism and are primarily eliminated through alternative pathways, potentially reducing their susceptibility to pharmacokinetic interactions [8]. Others, including lacosamide, are CYP substrates, placing them at risk for interactions with enzyme modulators [8]. Understanding these metabolic profiles is essential for predicting and managing potential interactions in clinical practice.

### 2.3 Genetic Polymorphism and Variable Response

Genetic variability in CYP450 enzymes represents a major source of interindividual differences in drug response. Polymorphisms in genes encoding CYP enzymes can result in phenotypes ranging from poor metabolizers, who have substantially reduced enzymatic activity, to ultra-rapid metabolizers, who exhibit enhanced metabolic capacity [6]. These genetic variations influence patient response to multiple drug classes, including antiepileptic agents.

The clinical implications of CYP450 polymorphism extend beyond simple dose adjustment. Poor metabolizers may experience excessive drug exposure and concentration-dependent adverse effects at standard doses, while ultra-rapid metabolizers may achieve subtherapeutic concentrations despite appropriate dosing. This variability underscores the importance of therapeutic drug monitoring and, increasingly, pharmacogenetic testing in optimizing antiepileptic therapy [4][5].

---

## 3. Therapeutic Drug Monitoring: Quantifying the Balance

### 3.1 Principles and Clinical Application

Therapeutic drug monitoring (TDM) represents the primary quantitative tool available for balancing seizure control with metabolic safety in antiepileptic therapy. TDM involves the measurement of drug concentrations in biological specimens, typically blood or saliva, to guide individualized dosing decisions [2][3]. The fundamental premise of TDM is that drug concentration, rather than dose, correlates more reliably with both therapeutic effect and adverse effects, enabling optimization of the therapeutic index.

The clinical utility of TDM in epilepsy management encompasses several key applications. During initial treatment, TDM helps establish the expected effective concentration for an individual patient, accounting for their specific characteristics including age, gender, comorbidities, and genetic factors [2]. This individual therapeutic concentration (ITC) represents the drug level at which optimal seizure control is achieved with acceptable tolerability, serving as a personalized target for ongoing management.

TDM is particularly valuable during transitions in patient status or treatment that may alter drug pharmacokinetics. Situations warranting TDM include initiation of therapy, achievement of stable seizure control (to document the individual therapeutic concentration), suspected toxicity, assessment of adherence, and circumstances of increased pharmacokinetic variability such as pregnancy, extremes of age, or changes in drug formulation [3][9].

### 3.2 Analytical Considerations and Interpretation

The accuracy and clinical utility of TDM depend critically on appropriate specimen collection, handling, and analytical methodology. Contemporary analytical approaches include chromatography and mass spectrometry techniques capable of precise and consistent measurement of drug concentrations across the therapeutic range [9]. Immunoassays offer alternatives with varying degrees of specificity and sensitivity depending on the drug and platform.

Interpretation of TDM results requires integration of the measured concentration with clinical context. The traditional therapeutic range, while useful as a general guide, represents population-based estimates that may not reflect optimal concentrations for individual patients. Some patients achieve seizure freedom at concentrations below the traditional therapeutic range, while others require concentrations above the typical range to achieve adequate control [2][3]. Conversely, some patients experience adverse effects at concentrations considered therapeutic for the general population.

The timing of sample collection relative to dosing is crucial for accurate interpretation. Trough concentrations, obtained immediately before the next dose, provide the most reliable assessment of steady-state exposure and facilitate comparison across time points and clinical settings [9]. Random or peak concentrations may be useful in specific circumstances but require careful interpretation accounting for the dosing schedule and absorption kinetics.

### 3.3 Saliva-Based Monitoring and Accessibility

Recent developments in TDM have expanded the range of available specimen types for antiepileptic drug measurement. Saliva-based testing offers a non-invasive alternative to blood collection, particularly valuable for pediatric populations, patients with difficult venous access, or situations requiring frequent monitoring [2]. Several AEDs, including carbamazepine, clobazam, lamotrigine, levetiracetam, phenobarbital, phenytoin, and zonisamide, can be reliably measured in saliva, providing clinically useful information regarding the unbound, pharmacologically active drug fraction [2].

The correlation between saliva and plasma concentrations varies by drug and depends on the extent of plasma protein binding. For drugs with minimal protein binding, saliva concentrations closely approximate unbound plasma concentrations, providing direct insight into the pharmacologically active drug fraction. For highly protein-bound drugs, the relationship is more complex and requires drug-specific validation [2].

---

## 4. Combination Therapy: Amplified Benefits and Risks

### 4.1 The Rationale for Polytherapy

Despite the initial preference for monotherapy in epilepsy treatment, approximately 30% of patients require combination therapy to achieve adequate seizure control [1][7]. This statistic reflects the heterogeneous nature of epilepsy, the variable mechanisms of seizure generation across patients, and the limitations of individual drugs in addressing all seizure types and syndromes.

The theoretical rationale for combination therapy rests on the premise that drugs with complementary mechanisms of action may produce additive or synergistic anticonvulsant effects. Combining agents that target different aspects of neuronal excitability—voltage-gated ion channels, neurotransmitter receptors, synaptic vesicle proteins—may achieve superior seizure control compared to maximizing any single agent [1][7]. This mechanistic diversity may also allow lower doses of individual agents, potentially reducing dose-dependent adverse effects.

However, the benefits of combination therapy must be weighed against the substantially increased complexity of pharmacokinetic management. Each additional agent introduces potential for drug-drug interactions, additive adverse effects, and challenges in adherence. The clinical challenge lies in identifying combinations that provide synergistic efficacy while minimizing interaction-related risks [7].

### 4.2 Metabolic Interaction Risks in Polytherapy

Drug interactions represent a significant concern in antiepileptic combination therapy, particularly for focal epilepsy where polytherapy is most commonly employed [7]. These interactions frequently involve modulation of hepatic enzyme systems, with consequences for the efficacy and tolerability of affected agents.

Valproate exemplifies the interaction potential of enzyme-inhibiting AEDs. As a potent CYP450 inhibitor, valproate can substantially increase plasma concentrations of co-administered drugs metabolized by these enzymes [7]. This inhibition may produce apparent "dose-dependent" adverse effects when the underlying cause is actually pharmacokinetic interaction. Clinicians must thoroughly understand these interactions when designing combination therapies to avoid unstable efficacy or increased adverse effects.

The interaction potential extends beyond hepatic metabolism to include effects on drug transporters, plasma protein binding, and renal excretion. Additionally, emerging evidence suggests that CYP enzymes within the central nervous system may influence local drug metabolism and availability at target sites, adding another layer of complexity to interaction prediction [8].

### 4.3 Cognitive and Behavioral Considerations

Beyond metabolic interactions, combination therapy introduces risks of additive cognitive and behavioral adverse effects that can significantly impact patient quality of life. AED combination therapy may disrupt neurotransmitter balance in the central nervous system, leading to cognitive dysfunction particularly with drug combinations affecting the GABA system [10]. Patients may experience attention deficits, memory impairment, and other cognitive issues that can worsen with higher doses and have long-term impacts on social functioning and quality of life [10].

Research has demonstrated that cognitive AED effects are common, with attention and executive functions most sensitive to drug load and individual drug effects [11]. Individual AEDs may not be independently associated with impaired cognitive function when controlling for other variables, suggesting that total drug burden and specific drug combinations may be more important determinants than any single agent [11].

Certain drug combinations may amplify adverse effects when used with other centrally active substances, including cognitive stimulants such as caffeine or cannabinoids [10]. This interaction potential necessitates ongoing cognitive assessment during treatment and careful consideration of the patient's full medication profile.

---

## 5. Individualized Treatment Approaches

### 5.1 Pharmacogenetic Testing and Personalized Medicine

The integration of genetic testing into clinical practice has opened new avenues for personalizing antiepileptic therapy. Pharmacogenetic testing enables more precise selection and dosing of antiseizure medications based on individual genetic characteristics, potentially enhancing efficacy while minimizing the risk of adverse drug reactions [4][5].

Genetic variants can influence antiepileptic drug response at multiple points in the pharmacokinetic pathway. Variants in drug-metabolizing enzymes affect the rate and extent of drug clearance. Variants in drug transporters influence absorption, distribution, and brain penetration. Variants in drug targets may alter sensitivity to pharmacologic effects [4]. Together, these genetic factors contribute substantially to the observed variability in drug response among patients.

The clinical application of pharmacogenetics in epilepsy has been advanced by studies demonstrating improved outcomes with genotype-guided treatment selection. Patients receiving genetically-guided ASM selection may achieve seizure freedom more rapidly than those treated empirically [4]. Furthermore, this approach enables identification of patients at risk for developing drug-resistant epilepsy earlier in their treatment journey, allowing for timely adjustments in treatment strategies or consideration of surgical options [4].

### 5.2 The PREPARE Study and Clinical Implementation

The PREPARE study represents a landmark investigation in preemptive pharmacogenomic testing, utilizing a 12-gene panel encompassing 50 germline variants to assess adverse reactions associated with genotype-guided drug treatment compared to standard of care [12]. Notably, genotype-guided treatments resulted in a 30% decrease in clinically relevant drug reactions, demonstrating the tangible benefit of pharmacogenetic integration into therapeutic decision-making [12].

These findings have important implications for antiepileptic drug therapy, where adverse effects represent a significant barrier to treatment adherence and quality of life. By identifying patients at genetic risk for adverse reactions before treatment initiation, clinicians can select alternative agents or implement enhanced monitoring strategies to mitigate risk.

### 5.3 Individual Therapeutic Concentration Establishment

The concept of individual therapeutic concentration (ITC) represents a practical application of individualized medicine in epilepsy management. Rather than targeting population-based therapeutic ranges, the ITC approach seeks to identify the specific drug concentration at which optimal seizure control is achieved for each individual patient [2].

Establishing the ITC requires systematic TDM correlated with clinical response. When a patient achieves stable seizure control, the corresponding drug concentration represents their personal therapeutic target. This concentration may fall within, above, or below the traditional therapeutic range, reflecting individual pharmacodynamic sensitivity and pharmacokinetic characteristics [2][3].

The ITC concept is particularly valuable during treatment transitions, such as formulation changes, addition or removal of interacting medications, or changes in patient status affecting drug disposition. By maintaining the established ITC rather than a fixed dose, clinicians can preserve therapeutic response while accommodating changing pharmacokinetic circumstances.

---

## 6. Clinical Strategies for Optimization

### 6.1 Drug Titration Principles

The process of drug titration represents a critical period during which the balance between efficacy and tolerability is established. Current guidelines recommend a "start low, go slow" approach to antiepileptic drug initiation, which has been shown to reduce the risk of severe idiosyncratic reactions with certain medications and improve tolerability regarding central nervous system-related adverse effects such as somnolence and dizziness [13].

This conservative titration strategy acknowledges the substantial interindividual variability in drug response and allows identification of the minimum effective dose for each patient. Starting with low doses and making gradual increments enables tolerance development to adverse effects while titrating toward therapeutic response. The optimal titration rate varies by drug, patient characteristics, and clinical circumstances [13].

Flexible titration and adjustment of concomitant ASMs may improve tolerability during combination therapy initiation [13]. Rather than maximizing each agent before considering alternatives, this approach allows real-time optimization of the regimen based on individual response and tolerability. Communication with patients during titration promotes adherence and enables early identification of emerging adverse effects.

### 6.2 Fixed-Dose Combinations and Simplified Regimens

The complexity of polytherapy regimens contributes to poor adherence and increased risk of dosing errors. Fixed-dose combinations (FDCs)—single tablets containing multiple drugs—have been proposed as a strategy to reduce pill burden and simplify medication administration [7]. These formulations may be particularly beneficial for patients with refractory epilepsy requiring long-term polytherapy.

Beyond adherence benefits, FDCs may offer pharmacokinetic advantages by ensuring consistent ratios of co-administered agents. This consistency can facilitate TDM interpretation and reduce variability in drug exposure. However, FDCs also limit flexibility in dose adjustment and may not be appropriate for all drug combinations or patient populations.

### 6.3 Multi-Target Drug Development

Contemporary antiepileptic drug research has increasingly focused on multi-target drugs that address multiple aspects of seizure pathophysiology simultaneously [7]. Traditional single-target strategies have proven increasingly limited in addressing the complex mechanisms underlying epilepsy and treatment resistance.

Existing AEDs already exhibit multi-mechanistic properties in many cases. For example, some agents demonstrate dual modulation of sodium channels, calcium channels, and GABAergic systems [7]. These multi-target profiles may contribute to efficacy while potentially allowing lower doses of individual mechanisms, reducing adverse effect burden.

Future drug development is expected to leverage advances in computational biology and neuroscience to design agents with optimized multi-target profiles. Multidisciplinary collaboration among pharmacologists, neuroscientists, and computational biologists is essential to advance this approach and translate multi-target concepts into clinical therapeutics [7].

---

## 7. Special Populations and Considerations

### 7.1 Cardiovascular and Cardiac Rhythm Effects

Some antiepileptic drugs have been associated with effects on cardiac rhythm, particularly in patients with underlying cardiovascular conditions [10]. This consideration adds another dimension to the risk-benefit assessment in patient populations with cardiac comorbidities. The potential for AED-related QT prolongation, conduction abnormalities, or other electrophysiologic effects must be considered when selecting therapies for these patients.

### 7.2 Pediatric and Geriatric Populations

Extremes of age present unique challenges in antiepileptic drug management. Pediatric patients may exhibit altered pharmacokinetics due to developmental differences in drug-metabolizing enzymes and organ function. Additionally, the developing brain may be more susceptible to certain adverse cognitive effects of AEDs [3].

Geriatric patients similarly exhibit age-related changes in drug disposition, often compounded by polypharmacy and multiple comorbidities. Increased pharmacokinetic variability in elderly patients necessitates careful monitoring and dose adjustment. The risk-benefit calculation may differ from that in younger adults, with greater emphasis on tolerability and quality of life [3].

### 7.3 Pregnancy and Hormonal Interactions

Pregnancy represents a dynamic state of altered pharmacokinetics, with changes in drug absorption, distribution, metabolism, and elimination. Many AEDs require dose adjustment during pregnancy to maintain therapeutic concentrations, and TDM is particularly valuable in this setting [3]. Additionally, enzyme-inducing AEDs may reduce the efficacy of hormonal contraceptives, requiring counseling regarding alternative contraceptive strategies.

---

## 8. Future Directions and Emerging Technologies

### 8.1 Advanced Therapeutic Drug Monitoring

The future of TDM in antiepileptic therapy is likely to involve enhanced analytical capabilities, improved standardization across laboratories, and integration with pharmacogenetic data. N-of-1 clinical trials, which treat each subject as an independent study, may enable determination of the most effective treatment for individual patients and facilitate personalized optimization [12].

The combination of TDM with pharmacogenetic testing represents a particularly promising approach. By integrating genetic information regarding drug-metabolizing enzyme activity with measured drug concentrations, clinicians can achieve more precise prediction of individual pharmacokinetic profiles and optimize dosing accordingly [12].

### 8.2 Novel Drug Targets and Mechanisms

Advances in understanding epilepsy pathophysiology are revealing new potential drug targets beyond traditional ion channels and neurotransmitter systems. Inflammatory, immune, and oxidative stress pathways have emerged as contributors to epileptogenesis and seizure susceptibility [1]. Drugs targeting these mechanisms may offer new therapeutic options with potentially favorable interaction profiles.

### 8.3 Computational Approaches to Interaction Prediction

The complexity of drug interaction networks in polytherapy regimens exceeds human cognitive capacity for complete analysis. Computational approaches leveraging artificial intelligence and machine learning may enable more comprehensive prediction of interaction potential based on drug properties, patient characteristics, and existing medication profiles. These tools could support clinical decision-making and reduce the risk of unrecognized interactions.

---

## 9. Conclusion

The balance between seizure control and metabolic interaction risk represents a fundamental challenge in antiepileptic drug therapy. Contemporary research has elucidated the critical role of cytochrome P450 enzymes in drug metabolism and the mechanisms by which enzyme inhibition and induction produce clinically significant interactions. This understanding has informed the development of therapeutic drug monitoring, pharmacogenetic testing, and rational combination therapy strategies that enable more individualized and effective treatment.

The path forward requires continued integration of pharmacokinetic and pharmacodynamic knowledge with emerging technologies. Fixed-dose combinations, multi-target drug development, and computational prediction tools offer potential solutions to the complexity of polytherapy management. Ultimately, the goal remains the optimization of therapeutic outcomes—achieving seizure freedom with the fewest adverse effects and the highest quality of life for each individual patient.

The evidence supports a personalized approach to antiepileptic therapy, recognizing that population-based guidelines provide only starting points for individual optimization. Through systematic application of TDM, thoughtful consideration of interaction potential, and integration of genetic information where available, clinicians can navigate the complex balance between efficacy and safety that defines contemporary epilepsy management.

---

## References

[1] PubMed. "Antiepileptic Drug Combinations for Epilepsy: Mechanisms, Clinical Strategies, and Future Prospects." *International Journal of Molecular Sciences*, 2025.

[2] Epilepsy Society. "Monitoring Your Medication." https://epilepsysociety.org.uk/about-epilepsy/anti-seizure-medication/monitoring-your-medication

[3] American Academy of Family Physicians. "Antiepileptic Drugs: Treatment Guidelines." *American Family Physician*, 2017.

[4] Frontiers in Pharmacology. "Pharmacogenetics of Antiseizure Medications." 2024.

[5] Frontiers in Pharmacology. "Personalized Medicine in Epilepsy Treatment." 2024.

[6] American Academy of Family Physicians. "Cytochrome P450 Enzymes: Clinical Considerations." *American Family Physician*, 2007.

[7] MDPI. "Antiepileptic Drug Combinations for Epilepsy: Mechanisms, Clinical Strategies, and Future Prospects." *International Journal of Molecular Sciences*, 2025.

[8] Frontiers in Pharmacology. "CYP Enzymes in Brain and Antiseizure Medication Metabolism." 2022.

[9] Springer. "Therapeutic Drug Monitoring: Clinical Applications and Best Practices." 2024.

[10] PMC. "Potential Risks of AED Combination Therapy." 2024.

[11] Neurology. "Cognitive Effects of Antiepileptic Drugs." 2020.

[12] PMC. "Pharmacogenetic Testing and Therapeutic Drug Monitoring Integration." 2024.

[13] Epilepsy & Behavior. "The Importance of Drug Titration in the Management of Patients with Epilepsy." 2022.

## Annotations


## Sources
[1] https://alameed.edu.iq/DocumentPdf/Library/eBook/6181.pdf
[2] https://emedicine.medscape.com/article/1187334-overview
[3] https://epilepsysociety.org.uk/about-epilepsy/anti-seizure-medication/monitoring-your-medication
[4] https://link.springer.com/article/10.1007/s12272-025-01581-x
[5] https://link.springer.com/chapter/10.1007/978-981-97-4283-7_4
[6] https://openaccess.sgul.ac.uk/108264/1/Hitchings%20-%20Drugs%20that%20lower%20the%20seizure%20threshold%20-%20Author%20final%20version.pdf
[7] https://pdfs.semanticscholar.org/68b2/abcbdb2fbdc5ba10e07bdd40ea1673a3c32b.pdf
[8] https://pmc.ncbi.nlm.nih.gov/articles/PMC10564003/
[9] https://pmc.ncbi.nlm.nih.gov/articles/PMC10965556/
[10] https://pmc.ncbi.nlm.nih.gov/articles/PMC12071858/
[11] https://pmc.ncbi.nlm.nih.gov/articles/PMC3001218/
[12] https://pubmed.ncbi.nlm.nih.gov/40362274/
[13] https://www.aafp.org/pubs/afp/issues/2007/0801/p391.html
[14] https://www.aafp.org/pubs/afp/issues/2017/0715/p87.html
[15] https://www.capbluecross.com/wps/wcm/connect/prod_nws.capblue.com29556/e98e8d7b-3077-4c5d-b325-612e9ccee2c9/medical-policy-genetic-testing-for-epilepsy.pdf?MOD=AJPERES&CACHEID=ROOTWORKSPACE.Z18_4G00HA41L8PI50ALUD09N53000-e98e8d7b-3077-4c5d-b325-612e9ccee2c9-oI0I0xu
[16] https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2022.983233/full
[17] https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2024.1411487/full
[18] https://www.mdpi.com/1422-0067/26/9/4035
[19] https://www.mdpi.com/2039-4713/15/2/44
[20] https://www.mdpi.com/2218-273X/15/12/1668
[21] https://www.neurology.org/doi/10.1212/WNL.0000000000009061
[22] https://www.sciencedirect.com/science/article/abs/pii/S1474442203004095
[23] https://www.sciencedirect.com/science/article/pii/S0035378725004965
[24] https://www.sciencedirect.com/science/article/pii/S1059131122002011
[25] https://www.sciencedirect.com/science/article/pii/S1525505021007782