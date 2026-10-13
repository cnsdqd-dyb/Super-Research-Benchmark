# Deep Research Report: grok-4-1-fast-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** adbdee60 | **Time:** 47.58s | **Cost:** $0.01099
--------------------------------------------------------------------------------

**Adsorption energy level distribution refers to the heterogeneity of binding energies for key reaction intermediates (e.g., *OH, *O, or *OOH in oxygen reduction reaction (ORR), or H* in HOR) across different surface sites on a fuel cell catalyst, often modeled as a probability density function X(E) where E is the adsorption energy.[[1]](https://pmc.ncbi.nlm.nih.gov/articles/PMC7155130)[[2]](https://onlinelibrary.wiley.com/doi/abs/10.1002/anie.201914666)**

This distribution critically influences both activity (via Sabatier principle/volcano plots) and stability. Optimal activity requires sites near the volcano peak (~0.2 eV for *O binding relative to Pt), but heterogeneity broadens the effective activity curve, enhancing tolerance to poisons or off-peak shifts.[[3]](https://academic.oup.com/nsr/article/5/3/327/4222803)[[4]](https://www.cell.com/joule/fulltext/S2542-4351(18)30621-4)

**Under thermal cycling (e.g., -40°C to 100°C in PEMFCs for cold starts, or 100–200°C in HT-PEMFCs/SOFCs), surface atoms diffuse/restructure, Ostwald ripening occurs, and facets redistribute, dynamically altering the adsorption energy distribution.[[5]](https://www.sciencedirect.com/science/article/pii/S0378775324013636)[[6]](https://pubs.rsc.org/en/content/articlehtml/2025/ta/d5ta07002c) This constrains durability as follows:**

1. **Surface Reconstruction and Site Loss**: High-temperature phases favor low-energy facets (e.g., Pt(111) over (100)), narrowing distribution toward weaker binding. Upon cooling, incomplete reconstruction traps metastable sites, reducing active site density or shifting away from optimal E_ads, degrading ORR kinetics (e.g., 20–50% ECSA loss in Pt/C after cycling).[[7]](https://www.nature.com/articles/s41467-022-33892-8)

2. **Adsorbate Trapping/Hysteresis**: In HT-PEMFCs, phosphoric acid (PA) exhibits adsorption hysteresis on Pt; stronger-binding sites (deeper E_ads tail) retain PA during cool-down, blocking ORR sites and causing reversible/irreversible current loss (up to 30–50 mV voltage drop). Broad distributions exacerbate this, as weak sites recover but strong ones poison cumulatively.[[8]](https://onlinelibrary.wiley.com/doi/10.1002/fuce.201000102)[[9]](https://www.researchgate.net/publication/264564731_Experimental_Investigations_into_Phosphoric_Acid_Adsorption_on_Platinum_Catalysts_in_a_High_Temperature_PEM_Fuel_Cell)

3. **Poisoning and Segregation Sensitivity**: Broad distributions (common in nanoparticles) provide initial robustness but degrade faster under cycling if tails shift (e.g., via alloy segregation). Narrow distributions risk total failure if peak shifts.[[10]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12502897)

**Design Constraints for Enhanced Durability:**
- **Broaden/Tune Distribution via Alloys/HEAs**: High-entropy alloys (e.g., Pt-Pd-Ir-Ru-Os) create site ensembles spanning optimal E_ads (±0.5 eV), maintaining ensemble-averaged activity despite restructuring (~2–5x better stability in ORR).[[4]](https://www.cell.com/joule/fulltext/S2542-4351(18)30621-4)
- **Stabilize with Supports**: N-doped carbon or oxides anchor Pt, preserving distribution (e.g., <50% ECSA loss vs. 70% in commercial Pt/C after 30k cycles).[[7]](https://www.nature.com/articles/s41467-022-33892-8)
- **Minimize Strong-Binding Tails**: Core-shell or single-atom catalysts shift distribution toward weaker E_ads, reducing hysteresis/poisoning in PA environments.[[11]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5527280)
- **Targets**: Aim for Gaussian-like distributions centered at optimal E_ads with σ ~0.1–0.3 eV, validated via DFT/microkinetics; test under ASTM-like thermal cycles (e.g., 1000 cycles, 60–140°C).[[12]](https://arxiv.org/html/2412.13838v3)

Overall, narrow distributions maximize peak activity but falter under cycling-induced shifts, while engineered broad distributions (e.g., HEAs) trade slight initial activity for superior long-term robustness, guiding durable fuel cell cathodes toward 8,000+ hour lifetimes.[[13]](https://www.hydrogen.energy.gov/docs/hydrogenprogramlibraries/pdfs/review06/fc_28_borup.pdf?sfvrsn=18344e3d_1)

## Annotations (Inline Citations)
Citation [1] (Pos: 334-389): [Web] https://pmc.ncbi.nlm.nih.gov/articles/PMC7155130
Citation [2] (Pos: 389-458): [Web] https://onlinelibrary.wiley.com/doi/abs/10.1002/anie.201914666
Citation [3] (Pos: 772-831): [Web] https://academic.oup.com/nsr/article/5/3/327/4222803
Citation [4] (Pos: 831-895): [Web] https://www.cell.com/joule/fulltext/S2542-4351(18)30621-4
Citation [5] (Pos: 1145-1219): [Web] https://www.sciencedirect.com/science/article/pii/S0378775324013636
Citation [6] (Pos: 1219-1288): [Web] https://pubs.rsc.org/en/content/articlehtml/2025/ta/d5ta07002c
Citation [7] (Pos: 1698-1755): [Web] https://www.nature.com/articles/s41467-022-33892-8
Citation [8] (Pos: 2133-2198): [Web] https://onlinelibrary.wiley.com/doi/10.1002/fuce.201000102
Citation [9] (Pos: 2198-2373): [Web] https://www.researchgate.net/publication/264564731_Experimental_Investigations_into_Phosphoric_Acid_Adsorption_on_Platinum_Catalysts_in_a_High_Temperature_PEM_Fuel_Cell
Citation [10] (Pos: 2628-2685): [Web] https://pmc.ncbi.nlm.nih.gov/articles/PMC12502897
Citation [4] (Pos: 2976-3040): [Web] https://www.cell.com/joule/fulltext/S2542-4351(18)30621-4
Citation [7] (Pos: 3199-3256): [Web] https://www.nature.com/articles/s41467-022-33892-8
Citation [11] (Pos: 3419-3475): [Web] https://pmc.ncbi.nlm.nih.gov/articles/PMC5527280
Citation [12] (Pos: 3672-3715): [Web] https://arxiv.org/html/2412.13838v3
Citation [13] (Pos: 3990-4107): [Web] https://www.hydrogen.energy.gov/docs/hydrogenprogramlibraries/pdfs/review06/fc_28_borup.pdf?sfvrsn=18344e3d_1


## Sources
[1] https://www.researchgate.net/publication/322840502_Carbon_Dioxide_Adsorption_over_Amine-Functionalized_MOFs
[2] https://pubs.acs.org/doi/10.1021/acs.jpcc.4c05086
[3] https://www.mdpi.com/1420-3049/29/21/5086
[4] https://www.mdpi.com/2073-4344/8/10/478
[5] https://chemrxiv.org/engage/api-gateway/chemrxiv/assets/orp/resource/item/66cd8a18f3f4b052903b9dd9/original/competitive-strain-modulation-of-oxygen-reduction-reaction-in-monolayer-binary-alloy-surfaces.pdf
[6] https://onlinelibrary.wiley.com/doi/abs/10.1002/anie.201914666
[7] https://jae.cardiffuniversitypress.org/articles/48/files/67fca24aaf778.pdf
[8] https://pmc.ncbi.nlm.nih.gov/articles/PMC5527280
[9] https://jelectrochem.xmu.edu.cn/cgi/viewcontent.cgi?article=1130&context=online_first
[10] https://www.sciencedirect.com/science/article/pii/S0378775324013636
[11] https://www.researchgate.net/publication/306048433_Understanding_and_Optimization_of_Chemical_Reactor_Performance_for_Bimodal_Reaction_Sequences
[12] https://pmc.ncbi.nlm.nih.gov/articles/PMC12697762
[13] https://pmc.ncbi.nlm.nih.gov/articles/PMC7155130
[14] https://bibbase.org/network/publication/kamat-herrmann-ternes-klein-krewer-scholl-experimentalinvestigationsintophosphoricacidadsorptiononplatinumcatalystsinahightemperaturepemfuelcell-2011
[15] https://advanced.onlinelibrary.wiley.com/doi/10.1002/aenm.201902106
[16] https://www.nature.com/articles/s41598-025-05309-1
[17] https://asmedigitalcollection.asme.org/electrochemical/article/19/1/011002/1103644/Experimental-Study-of-Thermal-Management-and
[18] http://research.buaa.edu.cn/en/publications/boosting-the-performance-and-durability-of-fenc-fuel-cell-catalys
[19] https://chemrxiv.org/engage/api-gateway/chemrxiv/assets/orp/resource/item/655486b32c3c11ed716e86bd/original/CN_coupling_HEA_manuscript.pdf
[20] https://hal.science/hal-04285372/document
[21] https://link.springer.com/article/10.1007/s41918-022-00175-1
[22] https://www.sciencedirect.com/science/article/abs/pii/S0360319917336467
[23] https://academic.oup.com/nsr/article/11/10/nwae193/7687839
[24] https://www.sciencedirect.com/science/article/pii/S0378775325026400
[25] https://www.hydrogen.energy.gov/docs/hydrogenprogramlibraries/pdfs/review06/fc_28_borup.pdf?sfvrsn=18344e3d_1
[26] https://pmc.ncbi.nlm.nih.gov/articles/PMC8514433
[27] https://publikationen.bibliothek.kit.edu/1000159758/151948321
[28] https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202302207
[29] https://www.sciencedirect.com/science/article/pii/S2949736124000058
[30] https://ui.adsabs.harvard.edu/abs/2020ACIE...59.5844L/abstract
[31] https://pubs.rsc.org/en/content/articlehtml/2025/ta/d5ta07002c
[32] https://www.researchgate.net/publication/322307634_Stresses_and_their_impacts_on_proton_exchange_membrane_fuel_cells_A_review
[33] https://www.cell.com/joule/fulltext/S2542-4351(18)30621-4
[34] https://arxiv.org/html/2412.13838v3
[35] https://www.sciopen.com/article/10.26599/CF.2025.9200041
[36] https://eprintspublications.npl.co.uk/3056/1/DEPC_MPE2.pdf
[37] https://pubs.acs.org/doi/10.1021/jacs.3c03345
[38] https://pmc.ncbi.nlm.nih.gov/articles/PMC11471586
[39] https://www.researchgate.net/publication/297725195_Durability_of_Platinum-Based_Fuel_Cell_Electrocatalysts_Dissolution_of_Bulk_and_Nanoscale_Platinum
[40] https://pubs.aip.org/aip/jap/article/133/15/155103/2883321/Changes-in-breakdown-and-charge-migration-of
[41] https://www.scitepress.org/Papers/2024/138754/138754.pdf
[42] https://www.sciencedirect.com/science/article/abs/pii/S1385894723034824
[43] https://pubs.acs.org/doi/10.1021/acsomega.3c08469
[44] https://pubs.acs.org/doi/10.1021/acsengineeringau.5c00031
[45] https://onlinelibrary.wiley.com/doi/10.1002/smll.202512669?af=R
[46] https://pubs.rsc.org/en/content/articlehtml/2023/su/d2su00129b
[47] https://academic.oup.com/nsr/article/5/3/327/4222803
[48] https://www.sciencedirect.com/science/article/pii/S0360319925022839
[49] https://www.sciencedirect.com/science/article/pii/S2590049822000765
[50] https://pubs.acs.org/doi/10.1021/acsami.2c15451
[51] https://cordis.europa.eu/project/id/325368/reporting
[52] https://www.sciencedirect.com/science/article/abs/pii/S0360319924050304
[53] https://www.sciencedirect.com/science/article/abs/pii/S0896844617302012
[54] https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202102576
[55] https://pmc.ncbi.nlm.nih.gov/articles/PMC12502897
[56] https://www.mdpi.com/2071-1050/17/3/943
[57] https://www.researchgate.net/publication/233869785_Determination_of_the_adsorption_energy_distribution_function_of_upd_hydrogen_on_monocrystalline_platinum
[58] https://pubs.rsc.org/en/content/articlehtml/2026/fd/d5fd00095e
[59] https://onlinelibrary.wiley.com/doi/10.1002/fuce.201000102
[60] https://www.tandfonline.com/doi/full/10.1080/15435075.2024.2448296?src=
[61] https://docs.nrel.gov/docs/fy18osti/71738.pdf
[62] https://link.springer.com/article/10.1007/s40820-025-01815-z
[63] https://www.mdpi.com/1420-3049/30/13/2818
[64] https://pubs.acs.org/doi/10.1021/acs.energyfuels.4c04834
[65] https://link.springer.com/article/10.1007/s43995-025-00258-2
[66] https://rcr.colab.ws/publications/10.59761/RCR5135
[67] https://pubs.acs.org/doi/10.1021/jacs.3c14486
[68] https://spj.science.org/doi/10.34133/energymatadv.0067
[69] https://pubs.acs.org/doi/10.1021/acsaem.5c01392
[70] https://pmc.ncbi.nlm.nih.gov/articles/PMC10875640
[71] https://research.chalmers.se/publication/533802/file/533802_Fulltext.pdf
[72] https://www.sciencedirect.com/science/article/abs/pii/S016943320501514X
[73] https://www.researchgate.net/publication/264564731_Experimental_Investigations_into_Phosphoric_Acid_Adsorption_on_Platinum_Catalysts_in_a_High_Temperature_PEM_Fuel_Cell
[74] https://www.osti.gov/servlets/purl/2204201
[75] https://www.sciencedirect.com/science/article/pii/S2949821X24000231
[76] https://www.mdpi.com/2673-4141/6/3/65
[77] https://pubs.aip.org/aip/rsi/article-pdf/doi/10.1063/1.4908169/15732736/024102_1_online.pdf
[78] https://iopscience.iop.org/article/10.1149/1945-7111/ad5624
[79] https://iopscience.iop.org/article/10.1149/1945-7111/ae078c/pdf
[80] https://www.sciencedirect.com/science/article/pii/S2590238525005302/pdf
[81] https://www.nature.com/articles/s41467-025-66532-y
[82] https://www.diva-portal.org/smash/get/diva2:12197/FULLTEXT01.pdf
[83] https://www.nature.com/articles/s41467-022-33892-8
[84] https://pubs.rsc.org/en/content/articlehtml/2023/ya/d2ya00316c
[85] https://www.nature.com/articles/s41467-025-61376-y
