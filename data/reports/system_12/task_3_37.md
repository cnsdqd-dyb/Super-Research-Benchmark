# Deep Research Report: grok-4-1-fast-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 870b098b | **Time:** 39.33s | **Cost:** $0.00567
--------------------------------------------------------------------------------

**Under random arrival patterns (e.g., Poisson-distributed vehicle arrivals), green wave phase offsets—used in signal coordination to create progression bands—have a notable but indirect effect on intersection capacity distribution, primarily by influencing arrival patterns, queuing variability, and effective throughput rather than altering the deterministic saturation flow rate.[[1]](https://www.fhwa.dot.gov/publications/research/operations/tft/chap9.pdf)**

### Key Effects:
- **Reduction in Arrival Variability**: Random upstream arrivals are filtered by signals, creating some platooning in departures. Optimal phase offsets align these arrivals more uniformly with downstream green phases, reducing variability (e.g., via platoon dispersion indices). This smoothing decreases random delays, overflow queues, and queue variability compared to random or poor offsets.[[1]](https://www.fhwa.dot.gov/publications/research/operations/tft/chap9.pdf)[[2]](https://onlinepubs.trb.org/Onlinepubs/trr/1994/1457/1457-023.pdf)

- **Impact on Effective Capacity**: Basic capacity (saturation flow rate × green ratio) is unchanged, but **effective capacity increases** due to lower queuing and fewer stops/delays. Coordination via proper offsets boosts progression factors (PF), improving level of service (LOS) and allowing higher sustainable flows before breakdown.[[1]](https://www.fhwa.dot.gov/publications/research/operations/tft/chap9.pdf)

- **Capacity Distribution**: Stochastic models show the distribution of per-cycle capacity (vehicles discharged) or queues narrows under optimal offsets. Random arrivals yield wider variance in throughput/delays (e.g., via shifted negative exponential headways). Coordinated offsets mitigate platoon diffusion and filtering effects, concentrating the distribution around higher mean values with lower variance—unlike uncoordinated random offsets, which amplify stochastic overflow.[[1]](https://www.fhwa.dot.gov/publications/research/operations/tft/chap9.pdf)[[2]](https://onlinepubs.trb.org/Onlinepubs/trr/1994/1457/1457-023.pdf)

### Comparison to Platooned Arrivals:
While green waves excel under platooned flows (maximizing bandwidth), they still benefit random arrivals by countering dispersion and reducing variability, though gains are smaller (e.g., TRANSYT/Miller models quantify this via offset optimization).[[1]](https://www.fhwa.dot.gov/publications/research/operations/tft/chap9.pdf)

No sources directly quantify "capacity distribution" shifts (e.g., variance metrics) for offsets under Poisson arrivals, but Traffic Flow Theory synthesizes that coordination narrows performance distributions overall.[[1]](https://www.fhwa.dot.gov/publications/research/operations/tft/chap9.pdf)

## Annotations (Inline Citations)
Citation [1] (Pos: 382-460): [Web] https://www.fhwa.dot.gov/publications/research/operations/tft/chap9.pdf
Citation [1] (Pos: 874-952): [Web] https://www.fhwa.dot.gov/publications/research/operations/tft/chap9.pdf
Citation [2] (Pos: 952-1023): [Web] https://onlinepubs.trb.org/Onlinepubs/trr/1994/1457/1457-023.pdf
Citation [1] (Pos: 1362-1440): [Web] https://www.fhwa.dot.gov/publications/research/operations/tft/chap9.pdf
Citation [1] (Pos: 1923-2001): [Web] https://www.fhwa.dot.gov/publications/research/operations/tft/chap9.pdf
Citation [2] (Pos: 2001-2072): [Web] https://onlinepubs.trb.org/Onlinepubs/trr/1994/1457/1457-023.pdf
Citation [1] (Pos: 2361-2439): [Web] https://www.fhwa.dot.gov/publications/research/operations/tft/chap9.pdf
Citation [1] (Pos: 2658-2736): [Web] https://www.fhwa.dot.gov/publications/research/operations/tft/chap9.pdf


## Sources
[1] https://www.mdpi.com/2076-3417/14/14/6151
[2] https://en.wikipedia.org/wiki/Green_wave
[3] https://www.researchgate.net/figure/Flow-chart-of-offset-of-the-arterial-green-wave_fig3_345456188
[4] https://www.emerald.com/jtran/article/doi/10.1680/jtran.24.00139/1270119/A-modified-model-for-signal-intersection-capacity
[5] https://actionlab.uta.edu/assets/files/0361198120918869.pdf
[6] https://pdfs.semanticscholar.org/9d86/70a22f043bcabda8293dc552e098a40daaab.pdf
[7] https://www.sciencedirect.com/science/article/pii/S2096232020300457
[8] https://papers.ssrn.com/sol3/Delivery.cfm/7ff66055-0337-4883-98b7-1365e2dd63a2-MECA.pdf?abstractid=4973350&mirid=1
[9] https://ris.utwente.nl/ws/files/25685424/memo2062.pdf
[10] https://onlinelibrary.wiley.com/doi/10.1155/atr/5857923
[11] https://www.sciencedirect.com/science/article/pii/S2590198222001750
[12] https://journals.sagepub.com/doi/10.1177/03611981231170129
[13] https://horowitz.me.berkeley.edu/Publications_files/All_papers_numbered/Mehr_Bandwidth_Maximization_Multiple_Routes_ACC2018.pdf
[14] https://www.tac-atc.ca/wp-content/uploads/shiravi.pdf
[15] https://www.mhaplus.org.uk/wp-content/uploads/filebase/professional_services/Presentation-content/Introduction-to-Traffic-Signals-Bitesize-Read-Onlyc.pdf
[16] https://www.sciencedirect.com/science/article/pii/S2046043021000551
[17] https://onlinelibrary.wiley.com/doi/10.1155/2024/4279649
[18] https://onlinelibrary.wiley.com/doi/10.1111/mice.13364
[19] https://pmc.ncbi.nlm.nih.gov/articles/PMC11991238
[20] https://static.tti.tamu.edu/tti.tamu.edu/documents/TTI-1999-ID15578.pdf
[21] https://bayen.berkeley.edu/sites/default/files/anderson_phd_thesis.pdf
[22] https://scienceworldjournal.org/article/view/18067/11685
[23] https://www.mdpi.com/2071-1050/11/14/3882
[24] https://dl.acm.org/doi/fullHtml/10.1145/3495018.3495039
[25] https://backend.orbit.dtu.dk/ws/portalfiles/portal/3050157/tr08_01.pdf
[26] https://www.researchgate.net/publication/316179873_Estimating_traffic_volumes_for_signalized_intersections_using_connected_vehicle_data
[27] https://ieeexplore.ieee.org/iel7/6287639/8948470/09264154.pdf
[28] https://arxiv.org/pdf/1402.0197
[29] https://www.civil.iitb.ac.in/tvm/ce774/2022/rblecnotes/16-HCM-2000-Ch-16-Singlized-Intersection_Read-p-1-to-47.pdf
[30] https://www.researchgate.net/publication/276497476_Green-Wave_Traffic_Theory_Optimization_and_Analysis
[31] https://vtechworks.lib.vt.edu/bitstreams/6483d800-8f0d-4a62-bb8c-6d8fd5d16619/download
[32] https://www.fhwa.dot.gov/publications/research/operations/tft/chap9.pdf
[33] https://onlinepubs.trb.org/Onlinepubs/trr/1994/1457/1457-023.pdf
[34] https://www.sciencedirect.com/science/article/pii/S2046043018300339
[35] https://www.mdpi.com/2079-9292/13/15/2939
