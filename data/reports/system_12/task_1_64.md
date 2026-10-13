# Deep Research Report: grok-4-1-fast-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** f1e077af | **Time:** 53.52s | **Cost:** $0.00958
--------------------------------------------------------------------------------

**Stability boundaries in signal coordination refer to the critical limits of traffic demand that coordinated traffic signal systems can handle while maintaining stable queue lengths across a network, preventing unbounded growth and gridlock.**

### Key Concepts
- **Signal Coordination and Stability Regions**: In urban traffic networks, signal coordination synchronizes timings across intersections (e.g., via offsets for green waves on arterials or adaptive policies like max-pressure/backpressure control). This is modeled using queueing networks (e.g., store-and-forward models), where the **stability region** is the set of average arrival rate vectors λ for which a control policy exists that keeps all link queues bounded in expectation.[[1]](https://www.sciencedirect.com/science/article/abs/pii/S0968090X14003325)[[2]](https://arxiv.org/pdf/2211.14426)
  - Coordinated policies (e.g., decentralized max-pressure) achieve the **maximal stability region**, matching the network's capacity region defined by possible signal splits and turning proportions.[[3]](https://ieeexplore.ieee.org/iel8/6287639/10380310/10659908.pdf)
  - Boundaries are determined by critical demand thresholds where the spectral radius of the routing matrix or demand exceeds capacity.

- **Crossing Stability Boundaries**:
  | Regime | Effect on Queues | Congestion Propagation |
  |--------|------------------|------------------------|
  | **Inside** (λ within region) | Bounded queues; transients dissipate. | Local shocks (e.g., incidents) resolve locally; no network spread due to dissipation via coordination.[[4]](https://www.mdpi.com/2076-3417/14/5/1891) |
  | **On/Near Boundary** | Oscillatory queues; marginal stability. | Waves/platoons propagate along corridors but dampen network-wide; risk of hysteresis.[[5]](https://www.sciencedirect.com/science/article/abs/pii/S0191261512000641) |
  | **Outside** (λ exceeds region) | Queues grow unbounded (linearly with time). | Spillback blocks upstream signals, cascades via routing (e.g., shockwaves at ~15-20 km/h backward), leading to system-wide gridlock.[[5]](https://www.sciencedirect.com/science/article/abs/pii/S0191261512000641) |

### Impacts on System-Level Congestion Propagation
- **Containment Within Boundaries**: Coordination creates "green bands" or prioritizes critical movements, damping perturbations. Local congestion (e.g., from demand spikes) dissipates as excess flow reroutes or clears via unused capacity, preventing macroscopic fundamental diagram (MFD) collapse.[[5]](https://www.sciencedirect.com/science/article/abs/pii/S0191261512000641)
- **Amplification Beyond Boundaries**: Demand overload causes queue spillovers, propagating upstream (shockwave theory) and downstream via turning movements. In networks, this triggers **congestion percolation**—small pockets merge into gridlock, reducing overall capacity by 20-50%.[[6]](https://www.sciencedirect.com/science/article/abs/pii/S0968090X22003357) Uncoordinated signals exacerbate this; coordination delays but doesn't prevent if demand exceeds.
- **Mitigation Strategies**: Policies like perimeter control expand effective stability regions by gating inflows, reducing propagation risk.[[5]](https://www.sciencedirect.com/science/article/abs/pii/S0191261512000641) Adaptive coordination (MPC, RL) dynamically adjusts to stay inside.

In essence, these boundaries act as a "phase transition": inside, coordination ensures resilience; outside, it accelerates system-wide propagation, emphasizing demand management alongside signals.[[7]](https://escholarship.org/content/qt1qm8390f/qt1qm8390f.pdf)

## Annotations (Inline Citations)
Citation [1] (Pos: 745-823): [Web] https://www.sciencedirect.com/science/article/abs/pii/S0968090X14003325
Citation [2] (Pos: 823-862): [Web] https://arxiv.org/pdf/2211.14426
Citation [3] (Pos: 1062-1131): [Web] https://ieeexplore.ieee.org/iel8/6287639/10380310/10659908.pdf
Citation [4] (Pos: 1597-1644): [Web] https://www.mdpi.com/2076-3417/14/5/1891
Citation [5] (Pos: 1801-1879): [Web] https://www.sciencedirect.com/science/article/abs/pii/S0191261512000641
Citation [5] (Pos: 2097-2175): [Web] https://www.sciencedirect.com/science/article/abs/pii/S0191261512000641
Citation [5] (Pos: 2528-2606): [Web] https://www.sciencedirect.com/science/article/abs/pii/S0191261512000641
Citation [6] (Pos: 2890-2968): [Web] https://www.sciencedirect.com/science/article/abs/pii/S0968090X22003357
Citation [5] (Pos: 3208-3286): [Web] https://www.sciencedirect.com/science/article/abs/pii/S0191261512000641
Citation [7] (Pos: 3552-3617): [Web] https://escholarship.org/content/qt1qm8390f/qt1qm8390f.pdf


## Sources
[1] https://www.nature.com/articles/s41467-023-43591-7
[2] https://ops.fhwa.dot.gov/publications/fhwahop11027/sec_d.htm
[3] https://ops.fhwa.dot.gov/publications/fhwahop08024/chapter3.htm
[4] https://onlinelibrary.wiley.com/doi/10.1155/2022/4934723
[5] https://www.lamar.edu/engineering/civil/research/proactive-traffic-timing.html
[6] https://www.mdpi.com/2076-3417/14/5/1891
[7] https://escholarship.org/content/qt1qm8390f/qt1qm8390f.pdf
[8] https://www.researchgate.net/figure/Stability-boundary-of-the-4WS-system_fig11_356431079
[9] https://par.nsf.gov/servlets/purl/10158009
[10] https://nemo.fh-hagenberg.at/wp-content/uploads/2019/09/A-Microscopic-Framework-for-Modeling-and-Simulating-Human-and-Automated-Driving.pdf
[11] https://www.sciencedirect.com/science/article/abs/pii/S0968090X22003357
[12] https://rosap.ntl.bts.gov/view/dot/72979/dot_72979_DS1.pdf
[13] https://www.sciencedirect.com/science/article/abs/pii/S0191261512000641
[14] https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID2960224_code1222176.pdf?abstractid=2960224&mirid=1&type=2
[15] https://link.aps.org/doi/10.1103/PhysRevLett.132.137401
[16] https://www.sciencedirect.com/science/article/abs/pii/S0191261522000911
[17] https://onlinelibrary.wiley.com/doi/10.1111/mice.13362
[18] https://www.mdpi.com/1424-8220/25/3/727
[19] https://www.researchgate.net/publication/359593918_Equilibrium_Stability_for_Multi-Modal_Traffic_in_an_Urban_Zone
[20] https://pmc.ncbi.nlm.nih.gov/articles/PMC8608825
[21] https://www.tandfonline.com/doi/full/10.1080/00423114.2025.2542851?src=
[22] https://www.nature.com/articles/s41598-021-01947-3.pdf
[23] https://www.nature.com/articles/s41598-021-01947-3
[24] https://www.researchgate.net/publication/396954968_A_Review_of_Research_on_Coordinated_Control_of_Traffic_Signals_at_Urban_Road_Intersection_Groups
[25] https://onlinelibrary.wiley.com/doi/10.1155/2022/4879049
[26] https://arxiv.org/pdf/2105.11790
[27] https://www.sciencedirect.com/science/article/abs/pii/S0968090X14003325
[28] https://mtreiber.de/Vkmod_Skript/Chap16_StabilityAnalysis.pdf
[29] https://rosap.ntl.bts.gov/view/dot/2625/dot_2625_DS1.pdf
[30] https://static.tti.tamu.edu/tti.tamu.edu/documents/TTI-1999-ID15578.pdf
[31] https://pubsonline.informs.org/doi/10.1287/trsc.2017.0754
[32] https://www.mdpi.com/2226-4310/12/6/529
[33] https://www.researchgate.net/publication/383596185_Coordinated_Model_Predictive_Controllers_with_Stabilizing_Reference_for_Traffic_Signals_in_Urban_Road_Network
[34] https://archiv.soms.ethz.ch/teaching/TrafficFlowFall09/fullbook.pdf
[35] https://pdfs.semanticscholar.org/a1ef/9af1f71ed3ee6b486e9c07eeb574fbdfe3b2.pdf
[36] https://ieeexplore.ieee.org/iel8/6287639/10380310/10659908.pdf
[37] https://www.sciencedirect.com/science/article/abs/pii/S0016003222003222
[38] https://tamasmolnar.com/publication/2023_Guo-et-al_CCTC%20for%20pairs%20of%20CAVs_IEEE_ITS.pdf
[39] https://ieeexplore.ieee.org/iel8/6287639/10820123/10833632.pdf
[40] https://journals.sagepub.com/doi/pdf/10.1177/0954406214532908?download=true
[41] https://hrcak.srce.hr/file/207770
[42] https://www.sciencedirect.com/science/article/pii/S2590123025023886
[43] https://link.aps.org/doi/10.1103/PhysRevE.86.056114
[44] https://www.sciencedirect.com/science/article/abs/pii/S0378437122002072
[45] https://dot.ca.gov/-/media/dot-media/programs/research-innovation-system-information/documents/f0017242-prr-2010-07-final-report.pdf
[46] https://arxiv.org/pdf/2508.20102
[47] https://rccao.com/research/files/RCCAO_Apr2013_CongestionManagement_LOWRES.pdf
[48] https://www.mdpi.com/2071-1050/17/11/4790
[49] https://www.tandfonline.com/doi/full/10.1080/15481603.2025.2547126
[50] https://rosap.ntl.bts.gov/view/dot/35439/dot_35439_DS1.pdf
[51] https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0337201
[52] https://arxiv.org/pdf/2204.11177
[53] https://www.online-pdh.com/pluginfile.php/79524/mod_resource/content/2/Transportation%20Engineering%20Traffic%20Flow%20Analysis.pdf
[54] https://aimspress.com/article/doi/10.3934/nhm.2018011?viewType=HTML
[55] https://escholarship.org/content/qt0fg4x79k/qt0fg4x79k_noSplash_9423f4cd70c49a311e7c42ca16209c12.pdf
[56] https://ir.cwi.nl/pub/27370/27370.pdf
[57] https://onlinelibrary.wiley.com/doi/10.1111/mice.13364
[58] https://www.mdpi.com/2227-7390/13/21/3386
[59] https://www.mdpi.com/2032-6653/16/3/163
[60] https://journals.sagepub.com/doi/10.1177/09544070241299144
[61] https://www.akesting.de/download/ThesisArneKesting.pdf
[62] https://arxiv.org/pdf/2101.07865
[63] https://arxiv.org/pdf/2211.14426
[64] https://pubs.aip.org/aip/cha/article/31/11/113120/342175/Obscuring-digital-route-choice-information
[65] https://www.researchgate.net/publication/375453895_Overtaking-Enabled_Eco-Approach_Control_at_Signalized_Intersections_for_Connected_and_Automated_Vehicles
[66] https://rosap.ntl.bts.gov/view/dot/35494/dot_35494_DS1.pdf
[67] https://www.sciencedirect.com/science/article/pii/S0142061522007797
[68] https://www.sciencedirect.com/science/article/abs/pii/S0191261525000682
