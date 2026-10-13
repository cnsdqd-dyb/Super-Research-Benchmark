# Deep Research Report: grok-4-1-fast-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** f5508e3e | **Time:** 79.90s | **Cost:** $0.01052
--------------------------------------------------------------------------------

**Power-law distributions of travel distances (or displacements) in urban mobility typically follow forms like P(d) ∝ d^{-(1+β)} or P(d) ∝ d^{-α}, where β or α (often ~1.5–3) characterizes the tail heaviness—smaller values indicate fatter tails with more long-distance trips.**[[1]](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0037027)[[2]](https://transportation.northwestern.edu/docs/research/core-topics/transportation-demand-economics-and-forecasting/Brockmann_TheScalingLaw.pdf)

**City scale (e.g., population N or area):**  
Empirical studies across dozens of cities show the power-law exponent is roughly universal (~1.75) when using *rank-distance* (intervening locations), independent of size.[[1]](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0037027) However, for *physical distance*, exponents vary across cities, with no strong universal pattern tied explicitly to size, though larger cities often exhibit extended power-law regimes (higher cutoffs) due to greater spatial extent and opportunities for long trips.[[1]](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0037027) Average trip distance ⟨d⟩ scales sublinearly with city radius R ~ N^{1/d_f} (d_f ~2–3 effective dimension), often ⟨d⟩ ∝ R^{0.6–1}, while the exponent β remains stable or slightly decreases (fatter tails) in simulations of growing hierarchies.[[3]](https://link.aps.org/doi/10.1103/PhysRevE.83.036117)[[4]](https://schmiste.github.io/netscicom14.pdf) In small/rural areas, distributions are exponential (β → ∞ effectively); urban scaling emerges with size.[[5]](https://link.springer.com/article/10.1140/epjb/e2015-60232-1)

**Network topology:**  
Topology strongly influences parameters via routing and connectivity:  
- **Hierarchical networks** (common in large cities: local roads → arterials → highways): Induce power-law tails; models show exponent β decreases (e.g., 3.11 → 1.63) as hierarchy ratio r (child/parent cell size) rises from 1 (flat) to 2 (branched), matching empirical β ~1.5–2.[[3]](https://link.aps.org/doi/10.1103/PhysRevE.83.036117)  
- **Regular grids/lattices**: Closer to exponential or truncated power-laws (steeper β), shorter tails due to uniform paths.[[3]](https://link.aps.org/doi/10.1103/PhysRevE.83.036117)  
- **Scale-free/random networks**: Fatter tails (smaller α ~1–2) from hubs enabling shortcuts.[[6]](https://royalsocietypublishing.org/rsif/article/16/154/20190041/87077/Travel-in-city-road-networks-follows-similar) Transport mode decomposition (walk/bus/car) also tunes α via speed/distance biases.[[7]](https://www.nature.com/articles/srep09136) Real cities optimize trade-offs, yielding similar exponents despite topology variance.[[6]](https://royalsocietypublishing.org/rsif/article/16/154/20190041/87077/Travel-in-city-road-networks-follows-similar)

**Overall evolution:** As cities scale up, networks become more hierarchical/scale-free, shifting from exponential (small scales) to power-law with decreasing β (longer-range mobility). Exponents stabilize ~1.6–2 in megacities; cutoffs/pre-factors grow with size.[[5]](https://link.springer.com/article/10.1140/epjb/e2015-60232-1)[[8]](https://arxiv.org/abs/2110.06784) These patterns arise from exploration-exploitation and spatial hierarchies, validated in taxi/GPS data.[[1]](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0037027)

## Annotations (Inline Citations)
Citation [1] (Pos: 277-357): [Web] https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0037027
Citation [2] (Pos: 357-505): [Web] https://transportation.northwestern.edu/docs/research/core-topics/transportation-demand-economics-and-forecasting/Brockmann_TheScalingLaw.pdf
Citation [1] (Pos: 725-805): [Web] https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0037027
Citation [1] (Pos: 1070-1150): [Web] https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0037027
Citation [3] (Pos: 1393-1451): [Web] https://link.aps.org/doi/10.1103/PhysRevE.83.036117
Citation [4] (Pos: 1451-1500): [Web] https://schmiste.github.io/netscicom14.pdf
Citation [5] (Pos: 1606-1673): [Web] https://link.springer.com/article/10.1140/epjb/e2015-60232-1
Citation [3] (Pos: 2049-2107): [Web] https://link.aps.org/doi/10.1103/PhysRevE.83.036117
Citation [3] (Pos: 2234-2292): [Web] https://link.aps.org/doi/10.1103/PhysRevE.83.036117
Citation [6] (Pos: 2388-2509): [Web] https://royalsocietypublishing.org/rsif/article/16/154/20190041/87077/Travel-in-city-road-networks-follows-similar
Citation [7] (Pos: 2593-2641): [Web] https://www.nature.com/articles/srep09136
Citation [6] (Pos: 2728-2849): [Web] https://royalsocietypublishing.org/rsif/article/16/154/20190041/87077/Travel-in-city-road-networks-follows-similar
Citation [5] (Pos: 3114-3181): [Web] https://link.springer.com/article/10.1140/epjb/e2015-60232-1
Citation [8] (Pos: 3181-3220): [Web] https://arxiv.org/abs/2110.06784
Citation [1] (Pos: 3324-3404): [Web] https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0037027


## Sources
[1] https://scispace.com/pdf/the-scaling-laws-of-human-travel-49922jssif.pdf
[2] https://en.wikipedia.org/wiki/Power_law
[3] https://link.springer.com/article/10.1140/epjds/s13688-023-00438-x
[4] https://fi.ee.tsinghua.edu.cn/public/publications/cea79694-c5c8-11ec-93d7-0242ac120006.pdf
[5] https://www.nature.com/articles/srep09136
[6] https://arxiv.org/pdf/0809.5001
[7] https://en.wikipedia.org/wiki/Scale-free_network
[8] https://scholargps.com/scholars/92847468890249/ying-hsing-chen
[9] https://www.researchgate.net/publication/283531782_A_scaling_approach_to_evaluating_the_distance_exponent_of_urban_gravity_model
[10] https://www.pnas.org/doi/10.1073/pnas.0901898106
[11] https://www.pnas.org/doi/10.1073/pnas.1913014117
[12] https://arxiv.org/html/2305.15665v2
[13] https://www.sciencedirect.com/science/article/abs/pii/S0378437112000210
[14] https://michael.szell.net/downloads/alessandretti2025um.pdf
[15] https://pmc.ncbi.nlm.nih.gov/articles/PMC12062502
[16] https://royalsocietypublishing.org/rsif/article/16/154/20190041/87077/Travel-in-city-road-networks-follows-similar
[17] https://arxiv.org/pdf/2207.05346
[18] https://www.sciencedirect.com/science/article/abs/pii/S0965856416000501
[19] https://pages.stern.nyu.edu/~xgabaix/papers/evolution.pdf
[20] https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0037027
[21] https://link.aps.org/doi/10.1103/PhysRevE.100.032306
[22] https://royalsocietypublishing.org/rsif/article/12/102/20141089/35380/Quantifying-long-term-evolution-of-intra-urban
[23] https://pmc.ncbi.nlm.nih.gov/articles/PMC2732869
[24] https://ui.adsabs.harvard.edu/abs/2015EPJB...88..117L/abstract
[25] https://www.seas.upenn.edu/~tesmith/MORI_HSU_2019.pdf
[26] https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0037027
[27] https://math.uchicago.edu/~shmuel/Modeling/The%20Origins%20of%20Scaling%20in%20Cities%20(Bettencourt).pdf
[28] https://arxiv.org/html/2405.02129v1
[29] https://epjb.epj.org/articles/epjb/abs/2015/05/b150232/b150232.html?mb=0
[30] https://ppms.cit.cmu.edu/media/project_files/final_report_-_180.pdf
[31] http://humnetlab.berkeley.edu/wp-content/uploads/2023/07/urban_dynamics_lens_mobility_SI.pdf
[32] https://epjds.epj.org/articles/epjdata/abs/2023/01/13688_2023_Article_438/13688_2023_Article_438.html?mb=0
[33] https://www.researchgate.net/publication/327131215_Power-law_distribution_in_an_urban_traffic_flow_simulation
[34] https://www.nature.com/articles/s41467-025-58286-4
[35] https://pmc.ncbi.nlm.nih.gov/articles/PMC8553837
[36] https://www.cis.upenn.edu/~mkearns/teaching/NetworkedLife/power-internet.pdf
[37] https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2022.879218/full
[38] https://royalsocietypublishing.org/rsif/article/18/176/20200705/89875/How-the-geometry-of-cities-determines-urban
[39] https://onlinelibrary.wiley.com/doi/full/10.1111/gean.12348
[40] https://www.sciencedirect.com/science/article/pii/S1569843225006685
[41] https://www.nber.org/system/files/working_papers/w15409/w15409.pdf
[42] https://www.researchgate.net/publication/264979769_Explaining_the_Power-law_Distribution_of_Human_Mobility_Through_Transportation_Modality_Decomposition
[43] https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0218028
[44] https://link.springer.com/article/10.1007/s42001-018-0028-7
[45] https://arxiv.org/html/2509.01699
[46] https://link.aps.org/doi/10.1103/PhysRevE.83.036117
[47] https://link.springer.com/content/pdf/10.1140/epjb/e2015-60232-1.pdf
[48] https://arxiv.org/html/2505.20590v1
[49] https://senseable.mit.edu/papers/pdf/20210527_Schlapfer-etal_UniversalVisitation_Nature.pdf
[50] https://arxiv.org/pdf/1401.0207
[51] https://pmc.ncbi.nlm.nih.gov/articles/PMC6553773
[52] https://arxiv.org/abs/2110.06784
[53] https://arxiv.org/abs/2002.06070
[54] https://transportation.northwestern.edu/docs/research/core-topics/transportation-demand-economics-and-forecasting/Brockmann_TheScalingLaw.pdf
[55] https://link.springer.com/article/10.1140/epjb/e2015-60232-1
[56] https://schmiste.github.io/netscicom14.pdf
[57] https://networksciencebook.com/chapter/4
[58] https://www.nature.com/articles/s41598-019-46208-6
[59] https://iopscience.iop.org/article/10.1088/2632-072X/adaa45
[60] https://www.sciencedirect.com/science/article/abs/pii/S0378437106000938
[61] https://acris.aalto.fi/ws/portalfiles/portal/35142578/journal.pone.0218028.pdf
[62] https://www.atlantis-press.com/article/25877804.pdf
[63] https://www.seas.upenn.edu/~tesmith/PAPER_with_MORI_HSU.pdf
[64] https://arxiv.org/pdf/1907.12289
[65] https://www.researchgate.net/publication/258055721_Unraveling_the_origin_of_exponential_law_in_intra-urban_human_mobility
[66] https://www.semanticscholar.org/paper/Unraveling-the-origin-of-exponential-law-in-human-Liang-Zhao/eac36448521bde6128f6fc38b92a438d348d59f2
[67] https://onlinelibrary.wiley.com/doi/full/10.1155/2012/291965
[68] https://www.connectedpapers.com/main/fb50816482882a690e17e82e08b6c302db46f657
[69] https://pmc.ncbi.nlm.nih.gov/articles/PMC12744654
[70] https://www.sciencedirect.com/science/article/pii/S2667325824004394
[71] https://journals.aps.org/prxenergy/abstract/10.1103/kysp-hgxt
[72] https://arxiv.org/html/2404.02642v1
[73] https://ar5iv.labs.arxiv.org/html/1212.6331
