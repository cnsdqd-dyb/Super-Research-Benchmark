# Deep Research Report: grok-4-1-fast-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 5f5b4492 | **Time:** 347.15s | **Cost:** $0.01061
--------------------------------------------------------------------------------

**The prediction of clinical efficacy for multi-target (atypical) antipsychotics relies on integrating preclinical dose-response data from animal models with human receptor binding affinities (e.g., Ki values), primarily to align dopamine D2 receptor occupancy and therapeutic windows.[[1]](https://pubmed.ncbi.nlm.nih.gov/12606608)[[2]](https://pmc.ncbi.nlm.nih.gov/articles/PMC4821196)**

### Key Animal Models and Dose-Response Curves
Animal models generate sigmoidal dose-response curves (often plotted as % response vs. log dose) to assess efficacy and side effects:
- **Efficacy models** (positive symptom analogs): Conditioned avoidance response (CAR) suppression, amphetamine- or phencyclidine (PCP)-induced hyperlocomotion, or apomorphine-induced climbing. These are D2-mediated, with ED50 doses typically achieving ~60–70% striatal D2 occupancy.[[3]](https://www.sciencedirect.com/science/article/pii/S0022356524363268/pdf)[[4]](https://accp1.onlinelibrary.wiley.com/doi/full/10.1002/jcph.1365)
- **Side effect models** (EPS analogs): Catalepsy or bar test, requiring higher D2 occupancy (~80%).[[5]](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2022.1020831/full)

The **therapeutic index (TI or window)** is calculated as TI = ED50_side effect / ED50_efficacy (e.g., catalepsy ED50 / CAR ED50). Atypicals like risperidone or olanzapine show wider TIs (>10) vs. typicals like haloperidol (~2–5) due to multi-target actions (high 5-HT2A/D2 affinity ratio >1, faster D2 dissociation kinetics).[[6]](https://pubmed.ncbi.nlm.nih.gov/11129112)[[7]](https://www.kjpp.net/journal/download_pdf.php?doi=10.4196%2Fkjpp.2009.13.2.71)

### Balancing with Human Receptor Affinity and Occupancy
Raw animal mg/kg doses poorly translate to humans due to 4–6x shorter antipsychotic half-lives in rodents, leading to under- or over-dosing.[[1]](https://pubmed.ncbi.nlm.nih.gov/12606608)
- **Occupancy-guided adjustment** (Kapur et al.): Shift animal dose-response curves to match human clinical D2 occupancy (60–80% via PET imaging correlates with efficacy; >80% risks EPS). Predicted human occupancy = [dose / (dose + Kd)], where Kd ≈ Ki (inhibition constant from human cloned receptors).[[8]](https://psychiatryonline.org/doi/10.1176/appi.ajp.2019.19010034)[[3]](https://www.sciencedirect.com/science/article/pii/S0022356524363268/pdf)
  - Normalize animal ED50 by (human Ki_D2 / rodent Ki_D2) × PK factor (e.g., human equivalent dose via allometry).
  - For multi-target drugs, balance multi-receptor occupancies: e.g., ensure 5-HT2A occupancy precedes full D2 at efficacy doses, widening TI.[[9]](https://www.sciencedirect.com/science/article/pii/S0149763415303341)

### Prediction Workflow
1. Generate animal dose-response curves; compute TI.[[10]](https://pmc.ncbi.nlm.nih.gov/articles/PMC2766698)
2. Use human Ki (D2, 5-HT2A, etc.) to estimate equivalent human doses: Human equiv. dose ≈ animal ED50 × (human plasma conc. for 70% D2 occ / animal plasma at ED50).[[11]](https://psychiatryonline.org/doi/pdf/10.1176/appi.ajp.158.3.360)
3. Validate against clinical data: Drugs with animal TI >10 and matched 65–80% D2 occ predict good efficacy/low EPS (e.g., clozapine, quetiapine).[[8]](https://psychiatryonline.org/doi/10.1176/appi.ajp.2019.19010034)
4. Human meta-analyses confirm hyperbolic dose-response plateaus at ED95 (near-max efficacy), often aligning with animal predictions after adjustment.[[8]](https://psychiatryonline.org/doi/10.1176/appi.ajp.2019.19010034)

This approach flagged issues like over-dosing haloperidol in rodents (false narrow TI) and predicts multi-target drugs' success by their balanced receptor profiles.[[12]](https://journals.sagepub.com/doi/10.1177/070674370004500302) Limitations: Ignores human PK variability, negative symptoms.[[2]](https://pmc.ncbi.nlm.nih.gov/articles/PMC4821196)

## Annotations (Inline Citations)
Citation [1] (Pos: 285-332): [Web] https://pubmed.ncbi.nlm.nih.gov/12606608
Citation [2] (Pos: 332-387): [Web] https://pmc.ncbi.nlm.nih.gov/articles/PMC4821196
Citation [3] (Pos: 855-933): [Web] https://www.sciencedirect.com/science/article/pii/S0022356524363268/pdf
Citation [4] (Pos: 933-1004): [Web] https://accp1.onlinelibrary.wiley.com/doi/full/10.1002/jcph.1365
Citation [5] (Pos: 1105-1200): [Web] https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2022.1020831/full
Citation [6] (Pos: 1528-1575): [Web] https://pubmed.ncbi.nlm.nih.gov/11129112
Citation [7] (Pos: 1575-1659): [Web] https://www.kjpp.net/journal/download_pdf.php?doi=10.4196%2Fkjpp.2009.13.2.71
Citation [1] (Pos: 1858-1905): [Web] https://pubmed.ncbi.nlm.nih.gov/12606608
Citation [8] (Pos: 2208-2278): [Web] https://psychiatryonline.org/doi/10.1176/appi.ajp.2019.19010034
Citation [3] (Pos: 2278-2356): [Web] https://www.sciencedirect.com/science/article/pii/S0022356524363268/pdf
Citation [9] (Pos: 2614-2688): [Web] https://www.sciencedirect.com/science/article/pii/S0149763415303341
Citation [10] (Pos: 2766-2822): [Web] https://pmc.ncbi.nlm.nih.gov/articles/PMC2766698
Citation [11] (Pos: 2988-3059): [Web] https://psychiatryonline.org/doi/pdf/10.1176/appi.ajp.158.3.360
Citation [8] (Pos: 3206-3276): [Web] https://psychiatryonline.org/doi/10.1176/appi.ajp.2019.19010034
Citation [8] (Pos: 3427-3497): [Web] https://psychiatryonline.org/doi/10.1176/appi.ajp.2019.19010034
Citation [12] (Pos: 3663-3730): [Web] https://journals.sagepub.com/doi/10.1177/070674370004500302
Citation [2] (Pos: 3792-3847): [Web] https://pmc.ncbi.nlm.nih.gov/articles/PMC4821196


## Sources
[1] https://www.sciencedirect.com/science/article/abs/pii/S0022356524192038
[2] https://jpet.aspetjournals.org/article/S0022-3565(24)36326-8/abstract
[3] https://www.nature.com/articles/1300983
[4] https://www.nature.com/articles/4000327
[5] https://farmacologia.icb.ufrj.br/posgraduacao/Doc_Pat/Defesas/2015/TeseDoutoradoJessicaBNViana.pdf
[6] https://psychiatryonline.org/doi/10.1176/appi.ajp.2019.19010034
[7] https://www.biorxiv.org/content/10.1101/2020.03.19.999615.full
[8] https://www.accessdata.fda.gov/drugsatfda_docs/nda/2024/216158Orig1s000IntegratedR.pdf
[9] https://pmc.ncbi.nlm.nih.gov/articles/PMC5529745
[10] https://www.researchgate.net/publication/8500801_Dose_Response_and_Dose_Equivalence_of_Antipsychotics
[11] https://www.researchgate.net/publication/324604493_Galantamine_is_not_a_positive_allosteric_modulator_of_human_a4b2_or_a7_nicotinic_acetylcholine_receptors
[12] https://pmc.ncbi.nlm.nih.gov/articles/PMC9841785
[13] https://www.nature.com/articles/s41386-025-02287-w
[14] https://pmc.ncbi.nlm.nih.gov/articles/PMC6187748
[15] https://public-pages-files-2025.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2024.1298061/pdf
[16] https://www.sciencedirect.com/science/article/abs/pii/S0022356524363268
[17] https://pubmed.ncbi.nlm.nih.gov/12606608
[18] https://www.nature.com/articles/1380474.pdf
[19] https://www.psychiatrist.com/pdf/behavioral-pharmacology-of-olanzapine-a-novel-antipsychotic-drug-pdf
[20] https://www.benchchem.com/product/b119527
[21] https://www.researchgate.net/publication/372342276_Antipsychotic_drug_efficacy_correlates_with_the_modulation_of_D1_rather_than_D2_receptor-expressing_striatal_projection_neurons
[22] https://www.nature.com/articles/1395704
[23] http://academic.oup.com/ijnp/article-pdf/11/3/309/2285595/11-3-309.pdf
[24] https://www.metris.nl/media/documents/laboras/Publications/2010%20-%20Dawe%20-%20Antipsychotic%20drugs%20dose-dependently%20suppress%20hyperactivity%20of%20Chakra%20mouse.pdf
[25] https://www.nature.com/articles/s41386-024-01951-x
[26] https://cdnsciencepub.com/doi/full/10.1139/jpn.0954
[27] https://pubs.rsc.org/en/content/articlehtml/2021/ra/d1ra02426d
[28] https://epub.ub.uni-muenchen.de/15176/1/Striatal_dopamine.pdf
[29] https://pubmed.ncbi.nlm.nih.gov/11129112
[30] https://www.cpn.or.kr/journal/download_pdf.php?number=1&spage=19&volume=5
[31] https://jpet.aspetjournals.org/article/S0022-3565(24)32686-2/pdf
[32] https://pubs.acs.org/doi/10.1021/acsptsci.2c00202
[33] https://www.researchgate.net/publication/297162039_Erratum_Antipsychotic_dosing_in_preclinical_models_is_often_unrepresentative_of_the_clinical_condition_A_suggested_solution_based_on_in_vivo_occupancy_Journal_of_Pharmacology_and_Experimental_Therapeu
[34] https://www.nature.com/articles/1380604.pdf
[35] https://www.accessdata.fda.gov/drugsatfda_docs/nda/2010/200603Orig1s000PharmR.pdf
[36] https://www.ibroneuroscience.org/article/S0306-4522(10)01211-X/abstract
[37] https://www.tandfonline.com/doi/pdf/10.1080/14737175.2016.1174577
[38] https://www.researchgate.net/publication/7448889_Dissociation_between_In_Vivo_Occupancy_and_Functional_Antagonism_of_Dopamine_D2_Receptors_Comparing_Aripiprazole_to_Other_Antipsychotics_in_Animal_Models
[39] https://www.researchgate.net/publication/260760130_5-HT6_receptor_antagonists_as_treatment_for_age-related_cognitive_decline
[40] https://www.dovepress.com/new-therapeutic-targets-and-drugs-for-schizophrenia-beyond-dopamine-d2-peer-reviewed-fulltext-article-NDT
[41] https://psychiatryonline.org/doi/10.1176/appi.ajp.157.4.514
[42] https://www.sciencedirect.com/science/article/pii/S0165178125001015
[43] https://www.researchgate.net/publication/12536638_Are_animal_studies_of_antipsychotics_appropriately_dosed_Lessons_from_bedside_to_bench
[44] https://scispace.com/pdf/partial-agonists-in-schizophrenia-why-some-work-and-others-2b4guhzstj.pdf
[45] https://scispace.com/papers/antipsychotic-dosing-in-preclinical-models-is-often-2j1rr9f4lf
[46] https://pmc.ncbi.nlm.nih.gov/articles/PMC4821196
[47] https://www.semanticscholar.org/paper/A-PET-study-of-dopamine-D2-and-serotonin-5-HT2-in-Mamo-Kapur/c6a6c541506e7910494f434d7e4d6b84b9558598
[48] https://bpspubs.onlinelibrary.wiley.com/doi/pdfdirect/10.1038/sj.bjp.0707159
[49] https://core.ac.uk/download/pdf/204199918.pdf
[50] https://www.psychiatrist.com/pdf/antipsychotics-from-theory-to-practice-integrating-clinical-and-basic-data-pdf
[51] https://jpet.aspetjournals.org/article/S0022-3565(24)26870-1/pdf
[52] https://pmc.ncbi.nlm.nih.gov/articles/PMC11632090
[53] https://www.researchgate.net/publication/395404114_Lipidic_nanocarriers_for_the_treatment_of_schizophrenia_progress_and_prospects_of_solid_lipid_nanoparticles_and_nanostructured_lipid_carriers
[54] https://www.sciencedirect.com/science/article/abs/pii/S0149763499000378
[55] https://academic.oup.com/ijnp/article-pdf/10/3/405/2683662/10-3-405.pdf
[56] https://www.kjpp.net/journal/download_pdf.php?doi=10.4196%2Fkjpp.2009.13.2.71
[57] https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2022.1020831/full
[58] https://psychiatryonline.org/doi/pdf/10.1176/appi.ajp.158.3.360
[59] https://pubmed.ncbi.nlm.nih.gov/10779880
[60] https://www.sciencedirect.com/science/article/pii/S0149763415303341
[61] https://pmc.ncbi.nlm.nih.gov/articles/PMC10842629
[62] https://link.springer.com/article/10.1007/s11095-011-0477-7
[63] https://www.researchgate.net/publication/23653561_Discovery_of_a_New_Class_of_Potential_Multifunctional_Atypical_Antipsychotic_Agents_Targeting_Dopamine_D-3_and_Serotonin_5-HT1A_and_5-HT2A_Receptors_Design_Synthesis_and_Effects_on_Behavior
[64] https://pubmed.ncbi.nlm.nih.gov/9577837
[65] https://journals.sagepub.com/doi/10.1177/070674370004500302
[66] https://people.socsci.tau.ac.il/mu/daphnajoel/files/2014/11/Weiner2000_screening.pdf
[67] https://pmc.ncbi.nlm.nih.gov/articles/PMC4074233
[68] https://www.researchgate.net/publication/262438598_Animal_models_for_predicting_the_efficacy_and_side_effects_of_antipsychotic_drugs
[69] https://www.benchchem.com/product/b181983
[70] https://accp1.onlinelibrary.wiley.com/doi/full/10.1002/jcph.1365
[71] https://www.sciencedirect.com/science/article/pii/S0022356524363268/pdf
[72] https://www.ovid.com/journals/jpsyc/pdf/10.1177/026988110201600302~striatal-dopamine-d2-receptor-binding-of-risperidone-in
[73] https://cdnsciencepub.com/doi/abs/10.1503/jpn.130191
[74] https://www.benchchem.com/product/b027284
[75] https://scholarworks.indianapolis.iu.edu/items/dc71c5c7-48fe-422a-bd41-13fae1851b89
[76] https://www.researchgate.net/publication/283209416_New_Multi-target_Antagonists_of_a1A-_a1D-Adrenoceptors_and_5-HT1A_Receptors_Reduce_Human_Hyperplastic_Prostate_Cell_Growth_and_the_Increase_of_Intraurethral_Pressure
[77] https://www.mentalhealthjournal.org/articles/fine-tuning-the-use-of-second-generation-antipsychotics.html
[78] https://pmc.ncbi.nlm.nih.gov/articles/PMC2766698
[79] https://www.biorxiv.org/content/10.1101/2021.11.14.468520.full
[80] https://www.biorxiv.org/content/10.1101/2025.10.25.684561v1.full.pdf
[81] https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1011793
[82] https://www.semanticscholar.org/paper/Antipsychotic-Dosing-in-Preclinical-Models-Is-Often-Kapur-VanderSpek/1136540abcb781e07e6881d1f156a77b3c6b5bfb
