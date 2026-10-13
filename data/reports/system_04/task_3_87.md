# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 0e9d9c12 | **Time:** 246.76s | **Cost:** $0.84735
--------------------------------------------------------------------------------

# Optimizing the Knowledge-Fatigue Balance in Multi-Site Heritage Route Planning: A Neuro-Symbolic and Algorithmic Approach

### Key Points
*   **The Core Tension:** Route planning in heritage tourism involves a fundamental trade-off between maximizing "profit" (knowledge gain, satisfaction, and site visits) and minimizing "cost" (physical exhaustion, cognitive overload, and aesthetic fatigue).
*   **Algorithmic Solutions:** The "Tourist Trip Design Problem with Fatigue" (TTDPF) extends traditional orienteering problems by introducing fatigue accumulation as a dynamic constraint. Algorithms like Iterated Local Search (ILS) and Genetic Algorithms (GA) are used to penalize routes that cluster too many similar sites or fail to schedule adequate rest, ensuring itineraries remain physically feasible.
*   **Cognitive Optimization:** The SAGITTARIUS project demonstrates that connecting sites through "interrelated content segments" reduces Extraneous Cognitive Load. By standardizing narrative structures (e.g., limiting interpretive units to 120 words) and linking sites via a cohesive story, working memory is freed, allowing for higher knowledge retention (Germane Load) without inducing mental exhaustion.
*   **Aesthetic Regulation:** To prevent "aesthetic fatigue" (boredom arising from visual or thematic monotony), optimized routing algorithms enforce diversity constraints, ensuring a mix of site categories (e.g., alternating between museums, nature, and architecture) to maintain engagement levels throughout the multi-site journey.

---

## 1. Introduction

The planning of itineraries for multi-site heritage tourism is a complex combinatorial optimization problem that transcends mere logistics. While traditional route planning focuses on minimizing distance or travel time, heritage route planning must address the human dimensions of the traveler: their capacity to absorb information (knowledge) and their physical and mental endurance (fatigue). This challenge is formally recognized in operations research as the Tourist Trip Design Problem (TTDP) [cite: 1, 2]. However, recent advancements have highlighted that maximizing the number of Points of Interest (POIs) visited often leads to suboptimal experiences due to the onset of fatigue—physical, cognitive, and aesthetic [cite: 1, 3].

Connecting multi-site heritage effectively requires a dual optimization strategy. First, it requires a mathematical modeling of fatigue accumulation to ensure physical feasibility, known as the Tourist Trip Design Problem with Fatigue (TTDPF) [cite: 1, 4]. Second, it requires a cognitive structuring of information, as pioneered by projects like SAGITTARIUS, which utilizes "interrelated content segments" to manage the working memory load of visitors [cite: 5]. By treating a multi-site route not as a collection of isolated stops but as a cohesive narrative and logistical ecosystem, planners can optimize the balance between the depth of knowledge acquired and the fatigue incurred.

This report provides an exhaustive analysis of how connecting multi-site heritage optimizes this balance. It explores the algorithmic foundations of fatigue management, the cognitive science of heritage interpretation, and the technological frameworks—such as knowledge graphs and digital twins—that enable these sophisticated planning systems.

---

## 2. The Theoretical Framework of Tourism Fatigue

To understand how route planning optimizes the knowledge-fatigue balance, one must first deconstruct the multidimensional nature of "fatigue" in a tourism context. It is not a singular variable but a dynamic system involving physical, motivational, emotional, and cognitive states [cite: 6].

### 2.1 Physical Fatigue and the TTDP
The traditional Tourist Trip Design Problem (TTDP) models the itinerary as an Orienteering Problem (OP), where the goal is to maximize the total score (utility) of visited sites within a time budget [cite: 2, 7]. However, this approach often fails to account for the degradation of the tourist's physical state. Physical fatigue accumulates as a function of travel time, walking distance, and the duration of visits. Without factoring in fatigue, the "optimal" route mathematically may be physically impossible or highly unpleasant for the tourist [cite: 1].

Research indicates that fatigue sensitivity varies among individuals. For a person with low fatigue sensitivity, a dense itinerary is logical; for others, the onset of tiredness necessitates changes in trip plans, often leading to the abandonment of the latter parts of a route [cite: 1]. Therefore, connecting sites requires a route structure that accounts for energy expenditure, integrating rest periods or "break nodes" as essential components of the graph rather than mere pauses [cite: 1].

### 2.2 Cognitive Fatigue and Information Overload
In the digital era, tourists are bombarded with massive, fragmented information regarding POIs, transport, and historical context. This abundance causes "decision fatigue" and severe cognitive overload [cite: 8]. In a multi-site heritage context, the cognitive load is exacerbated. Each new site typically requires the visitor to establish a new context (historical period, architectural style, cultural significance). If these sites are unconnected narratively, the brain must "reset" its context repeatedly, consuming high amounts of Working Memory (WM) resources [cite: 5].

Cognitive fatigue in route planning is thus a function of the *discontinuity* of information. When sites are connected through a "cognitive driven communication pattern," the route acts as a scaffold, allowing new information to be attached to prior knowledge (schema construction), thereby reducing the cognitive effort required to understand subsequent sites [cite: 5].

### 2.3 Aesthetic Fatigue and Monotony
A specific and critical form of fatigue in heritage tourism is "aesthetic fatigue." This occurs when a tourist visits multiple sites of a similar category (e.g., three traditional gardens or four baroque churches) in succession. Research using electroencephalogram (EEG) analysis on visitors to Chinese traditional gardens demonstrated that as landscape playbacks and visits increased, attention levels declined, and the perceived attractiveness of the sites weakened [cite: 1].

Aesthetic fatigue leads to a loss of utility value; the third garden visited provides significantly less satisfaction than the first, even if it is objectively just as beautiful. Consequently, route planning that fails to diversify the *types* of heritage sites connected in a sequence will result in diminishing returns on knowledge gain and satisfaction [cite: 3, 9].

---

## 3. Algorithmic Optimization: The Tourist Trip Design Problem with Fatigue (TTDPF)

The mathematical solution to balancing knowledge (utility) and fatigue is the Tourist Trip Design Problem with Fatigue (TTDPF). This model extends the standard TTDP by introducing fatigue as a constraint or a penalty function within the optimization algorithm.

### 3.1 Modeling Fatigue Constraints
In the TTDPF, the objective function is not merely to maximize the sum of scores of visited POIs. Instead, it maximizes satisfaction subject to fatigue accumulation. The model introduces variables for "fatigue level" which increase with activity (walking, visiting) and decrease with rest [cite: 1].

*   **Fatigue Sensitivity:** The model incorporates a parameter for fatigue sensitivity. For tourists with high sensitivity, the algorithm prioritizes routes with shorter intervals between breaks or shorter total travel distances.
*   **Recovery Functions:** The connection between sites is optimized by calculating the necessary recovery time. If the travel time between Site A and Site B acts as a rest period (e.g., a comfortable train ride), the algorithm may favor this connection over a short walk that adds to physical load [cite: 1].
*   **Penalty Functions:** Algorithms utilize penalty functions to evaluate the feasibility of a route. If the accumulated fatigue exceeds a certain threshold, the route is penalized or discarded, ensuring that the generated itinerary is realistic [cite: 3].

### 3.2 Heuristic Approaches: ILS and Genetic Algorithms
Because the TTDPF is an NP-hard problem (computationally difficult to solve perfectly), heuristic algorithms are employed to find near-optimal solutions efficiently.

*   **Iterated Local Search (ILS):** This method starts with a candidate route and iteratively improves it. In the context of fatigue, the ILS might "shake" the solution by inserting a rest stop or swapping a high-fatigue site for a low-fatigue one to see if the overall satisfaction improves [cite: 1].
*   **Genetic Algorithms (GA):** GAs simulate natural selection to evolve better routes. In addressing aesthetic fatigue, a hybrid heuristic algorithm (combining GA with Differential Evolution) has been proposed. This algorithm evaluates routes based on the diversity of scenic categories. If a route contains too many similar sites (e.g., "museum, museum, museum"), the algorithm lowers its fitness score, pushing the evolution toward routes with higher variety (e.g., "museum, park, market") [cite: 2, 10].

### 3.3 Diversity as an Optimization Metric
To combat aesthetic fatigue, the optimization logic includes "diversity rewards." The Comprehensive Satisfaction Score (CSS) of a route is calculated not just by the popularity of the sites, but by the diversity of categories included.
\[ CSS = TUS \times ISAS \times FS + R_{div} \]
Where:
*   **TUS:** Time Utilization Score (efficiency).
*   **ISAS:** Scenic Spot Attractiveness Score.
*   **FS:** Feasibility Score (adherence to time windows).
*   **R_div:** Reward based on Scenic Category Diversity [cite: 3].

By mathematically rewarding diversity, the route planner ensures that the visitor remains mentally stimulated, thereby optimizing the "knowledge" component by maintaining high attention levels throughout the trip.

---

## 4. Cognitive Load Theory and Knowledge Optimization

While algorithms manage the physical and aesthetic logistics, the optimization of *knowledge acquisition* relies on Cognitive Load Theory (CLT). The SAGITTARIUS project provides a definitive framework for how connecting multi-site heritage can optimize knowledge transfer by managing the visitor's mental resources [cite: 5, 11].

### 4.1 The Architecture of Cognitive Load
CLT posits that human Working Memory (WM) is limited, while Long-Term Memory (LTM) is effectively unlimited. Learning (knowledge gain) occurs when information is processed in WM and transferred to LTM as schemas. In heritage tourism, three types of load are critical:
1.  **Intrinsic Cognitive Load (ICL):** The inherent complexity of the heritage site (e.g., the complex genealogy of a royal family). This cannot be easily altered [cite: 5].
2.  **Extraneous Cognitive Load (ECL):** The load generated by *how* the information is presented. Poorly connected sites, confusing maps, or disjointed narratives increase ECL, consuming WM resources that could otherwise be used for learning [cite: 5].
3.  **Germane Cognitive Load (GCL):** The mental effort dedicated to processing and understanding the information (schema construction). The goal of route planning is to maximize GCL by minimizing ECL [cite: 5].

### 4.2 Interrelated Content Segments
The SAGITTARIUS project developed a "cognitive driven communication pattern" to connect multi-site heritage. The core strategy is the use of **interrelated content segments**. Instead of treating each site as a standalone entity, the route is designed so that information from Site A provides the "prior knowledge" required for Site B [cite: 5].

*   **Freeing Working Memory:** By relating new content to prior knowledge established earlier in the route, the system frees up WM capacity. The visitor does not need to relearn the context; they only need to process the *new* specific details of the current site [cite: 5, 12].
*   **Chunking:** Information is "chunked" into manageable units. The project guidelines suggest a maximum of three novel concepts per unit and limiting text segments to 120 words, with a total narrative per asset not exceeding 300 words [cite: 5]. This strict structuring ensures that the visitor's cognitive limits are respected, preventing the "museum fatigue" often caused by reading lengthy, dense text.

### 4.3 The Narrative Route as a Cognitive Scaffold
Connecting sites through a unified narrative acts as a cognitive scaffold. For example, a route might be themed around "The Rise of the Tobacco Industry" (as seen in the Greek Pilot Project of ALECTOR/SAGITTARIUS) [cite: 13].
*   **Site 1:** Introduces the cultivation of tobacco (Context).
*   **Site 2:** Shows the processing factories (Process).
*   **Site 3:** Shows the mansions of the tobacco merchants (Consequence).

Because the "tobacco context" is established at Site 1, the visitor at Site 3 does not need to expend mental energy understanding *why* the merchants were rich; they can focus immediately on the architectural details. This sequencing optimizes knowledge gain by ensuring that the visitor's mental energy is focused on *elaboration* (Germane load) rather than *orientation* (Extraneous load) [cite: 5].

---

## 5. Multi-Site Connectivity and Narrative Cohesion

The optimization of the knowledge-fatigue balance is further achieved through the structural connectivity of the heritage sites. This involves not just the intellectual connection (narrative) but the logistical and interpretive cohesion.

### 5.1 The Roving Museum Concept
The "Roving Museum" (RM) model, implemented in South East Europe, exemplifies this connectivity. It operates across seven countries, connecting 110 cultural heritage narratives via a unified infrastructure (QR codes, mobile apps) [cite: 5].
*   **Standardization:** The RM uses a standardized "cognitive driven communication pattern." Whether the tourist is in Italy or Greece, the format of the information (headings, word counts, transition styles) remains consistent. This consistency reduces the cognitive load required to "learn how to learn" at each new site [cite: 5].
*   **Transitions:** The narrative structure explicitly uses transitions to link sub-units. The title of one sub-unit forms the transition to the next, ensuring a seamless flow of information that maintains the "story" without abrupt cognitive jumps [cite: 5].

### 5.2 Multi-Site Passes and Economic/Logistical Optimization
Connecting sites also optimizes the "fatigue" associated with transaction costs and logistics. Multi-site heritage passes (e.g., in Malta) allow access to multiple temples and museums with a single ticket [cite: 14, 15].
*   **Reduction of Decision Fatigue:** Tourists do not need to make purchase decisions at every gate. The "bundle" simplifies the process, reducing the friction and stress (a form of psychological fatigue) associated with travel logistics [cite: 14].
*   **Logistical Efficiency:** Route mapping software, often used in logistics, can be applied to tourism to optimize the physical path. By grouping sites geographically and temporally, travel time is minimized, directly reducing physical fatigue [cite: 16, 17].

---

## 6. Technological Enablers: Knowledge Graphs and Digital Twins

The sophisticated balancing of knowledge and fatigue in modern route planning is increasingly reliant on advanced technologies that can model the complex relationships between sites and the user's state.

### 6.1 Knowledge Graphs for Semantic Connectivity
Knowledge graphs provide a structured way to manage the vast datasets associated with multi-site heritage. They create an interconnected web of information, linking historical records, material properties, and environmental data [cite: 18].
*   **Dynamic Querying:** A knowledge graph can support complex queries, such as finding a route that connects "Baroque architecture" sites but ensures they are within "500 meters" of each other to minimize fatigue.
*   **Contextual Linking:** By mapping the semantic relationships between sites (e.g., "Site A was built by the father of the architect of Site B"), the knowledge graph enables the generation of the "interrelated content segments" that reduce cognitive load [cite: 18].

### 6.2 Digital Twins and Real-Time Monitoring
Digital twins—virtual replicas of physical sites—can be integrated with knowledge graphs via APIs to provide real-time data [cite: 18].
*   **Environmental Monitoring:** Sensors can monitor temperature and humidity. If a site is experiencing extreme heat (which increases physical fatigue), the route planning system can dynamically reroute the tourist to an indoor, air-conditioned site, thereby actively managing the fatigue factor [cite: 1, 18].
*   **Crowd Management:** Real-time data on congestion can prevent the stress and fatigue associated with overcrowding. The system can suggest visiting a popular site during a lull, optimizing the experience [cite: 19].

### 6.3 Neuro-Symbolic Planning
Recent research into "neuro-symbolic" planning combines the generative capabilities of Large Language Models (LLMs) with the logical rigor of symbolic planners. While LLMs can generate rich narratives (knowledge), they often fail at strict constraint satisfaction (fatigue limits, time windows). Neuro-symbolic approaches use LLMs to interpret user intent and symbolic planners to enforce the hard constraints of the TTDPF, ensuring the generated route is both informative and feasible [cite: 8].

---

## 7. Aesthetic Fatigue and Route Diversity

A critical component of the "knowledge vs. fatigue" balance is the specific management of aesthetic fatigue. As established, viewing similar stimuli repeatedly degrades attention and satisfaction [cite: 1, 6].

### 7.1 The Mechanism of Aesthetic Fatigue
Aesthetic fatigue is a psychological phenomenon where the marginal utility of a specific type of sensory input diminishes rapidly. In the context of Chinese traditional gardens, EEG studies showed that "novelty," "scene abundance," and "color sensitivity" are positively correlated with attention. As these factors become repetitive, attention (and thus knowledge retention) plummets [cite: 1].

### 7.2 Diversity-Oriented Route Planning
To optimize against this, route planning algorithms must incorporate diversity as a core objective.
*   **Category Interleaving:** Instead of visiting three temples in a row, an optimized route might sequence them as: Temple $\rightarrow$ Local Market $\rightarrow$ Museum $\rightarrow$ Park. This interleaving allows the sensory and cognitive faculties used for one type of experience to rest while others are engaged [cite: 3].
*   **Algorithmic Implementation:** The "Reward Based on Scenic Category Diversity" ($R_{div}$) in the optimization function explicitly adds value to the itinerary for every new category introduced and penalizes the absence of user-preferred categories [cite: 3]. This ensures that the "knowledge" gained is broad and that the visitor remains fresh and engaged.

---

## 8. Practical Implications: Serious Games and Personalized Itineraries

The theoretical and algorithmic concepts discussed manifest in practical applications that directly enhance the tourist experience.

### 8.1 Serious Games and Gamification
Serious games (SGs) and gamification strategies are powerful tools for managing fatigue and enhancing knowledge.
*   **Motivation as Fatigue Countermeasure:** Gamification elements (points, challenges, narratives) can increase motivation. According to the fatigue model, high motivation can counteract the perception of physical tiredness [cite: 6, 20].
*   **Puzzle-Based Learning:** Games that use jigsaw puzzles or interactive narratives to teach cultural heritage have been shown to improve pattern recognition and retention compared to passive video watching. The active engagement required by the game maintains cognitive alertness (Germane load) and prevents the "zoning out" associated with passive consumption [cite: 20, 21].
*   **Augmented Reality (AR):** AR applications can overlay historical characters or reconstructions onto the physical site. This "embodied" experience connects the visitor to the history in a visceral way, often making the walk between sites part of the game (e.g., a treasure hunt), thereby transforming the "cost" of travel into a "profit" of entertainment [cite: 22].

### 8.2 Personalized Route Recommendation Systems
Modern recommendation systems are moving beyond static maps to dynamic, personalized agents.
*   **Fatigue-Aware Routing:** Apps can now ask users for their "fatigue sensitivity" or physical condition (e.g., elderly travelers, families with children) and generate routes with appropriate pacing and rest stops [cite: 1, 23].
*   **Package Tours for Families:** For multi-generational groups, package tours optimize the balance by handling the logistics (reducing cognitive/decision fatigue for parents) and pacing the itinerary to accommodate the physical limits of children and grandparents [cite: 23].

---

## 9. Conclusion

Connecting multi-site heritage is not merely a matter of drawing lines on a map; it is a sophisticated exercise in human-centric optimization. The integration of multi-site heritage optimizes the balance between knowledge and fatigue through three primary mechanisms:

1.  **Algorithmic Regulation (TTDPF):** By mathematically modeling fatigue as a constraint and diversity as a reward, algorithms ensure that itineraries remain within the physical and aesthetic limits of the tourist, preventing exhaustion and boredom [cite: 1, 3].
2.  **Cognitive Structuring (SAGITTARIUS):** By connecting sites through interrelated content segments and standardized narratives, the system minimizes extraneous cognitive load. This frees up working memory, allowing for deeper knowledge acquisition without mental burnout [cite: 5].
3.  **Technological Integration:** Knowledge graphs and digital twins enable the real-time, semantic linking of sites, allowing for dynamic rerouting based on environmental conditions and the creation of cohesive, story-driven experiences that act as cognitive scaffolds [cite: 18].

Ultimately, the optimized route is one that treats the visitor's energy—both physical and mental—as a finite resource to be conserved and strategically deployed, ensuring that every step taken contributes to a meaningful and lasting engagement with cultural heritage.

---

### References
*   **[cite: 16]** FarEye. (2024). Importance of Route Mapping Driver Management.
*   **[cite: 24]** Maptive. (2026). Route Optimization Reduces Travel Time.
*   **[cite: 17]** Routific. (2023). Route Planning vs Route Optimization.
*   **[cite: 8]** MDPI. (2024). Neuro-symbolic planning for travel.
*   **[cite: 5]** Papathanasiou-Zuhrt, D. (2015). Cognitive Load Management of Cultural Heritage Information: An Application Multi-Mix for Recreational Learners.
*   **[cite: 1, 4, 25]** Ko, T., et al. (2020). Tourist Trip Design Problem considering Fatigue.
*   **[cite: 19]** CAD Journal. (2024). Virtual tourism and route planning.
*   **[cite: 14]** TakeYourBackpack. (2025). Backpacking in Malta.
*   **[cite: 15]** RNARS. (2012). Heritage Pass details.
*   **[cite: 22]** Holloway-Attaway, L. (2020). Multi-site heritage project and AR.
*   **[cite: 2, 26]** Gavalas, D., et al. (2022). A systematic literature review for the tourist trip design problem.
*   **[cite: 27, 28]** MDPI. (2025). Multi-Objective Fuzzy Tourist Trip Design Problem.
*   **[cite: 7]** IDUS. (2024). Route design model with scenic value.
*   **[cite: 21]** Halac, H.H., et al. (2025). Teaching Cultural Heritage through a Narrative-based Game.
*   **[cite: 20]** ResearchGate. (2021). Enhancing Learning Performance and Motivation of Cultural Heritage Using Serious Games.
*   **[cite: 12]** ResearchGate. (2015). The role of gamification in material and immaterial cultural heritage.
*   **[cite: 13]** ALECTOR Network. (2016). Cognitive driven communication pattern.
*   **[cite: 11]** Papathanasiou-Zuhrt, D. (2025). Cognitive Processing of Information with Visitor Value.
*   **[cite: 18]** MDPI. (2024). Knowledge Graphs and Digital Twins in Heritage.
*   **[cite: 23]** TripCosmos. (2026). Families Choose Package Tours for Temple Travel.
*   **[cite: 3]** MDPI. (2024). Aesthetic fatigue and tourist route planning.
*   **[cite: 6]** Tourism Management. (2020). Tourist aesthetic fatigue conceptual model.
*   **[cite: 9]** Taylor & Francis. (2022). Route recommendation and aesthetic fatigue.
*   **[cite: 10]** Tourism Management. (2017). Tourist recommendation system with consideration for aesthetic fatigue.
*   **[cite: 1]** ResearchGate. (2018). Electroencephalogram Experiment Based Analysis of Aesthetic Fatigue.

**Sources:**
1. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRSMZPdzHFLOvzYDLpyj7Kc-mrn4X09_eaIxCiHr1BahDMA-AZsdq-quLzNhKMrNcXCwJgWHHk22E1yADSwG0POFlHvvYvjNg3OmRwIZwqnDnyCXoNHhtzMSyn26IYP4ghKwT8PjoCszzj0cX0y1UFVQXJ_5IPr6ODseDjKLS3D6bms7a3IHXhSFwINtY-rf4ITOMmnVmmPw==)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHogUcFDyPpYLOygQUQThL6sSybH09IiQP4LmpEb0IBrDJGmBDmkYkl4YpDLsgOiuk1uyMFTYXZwg7joYCOjFJizKEHLZst35Op8giabTeqw3hf9P9ACGwmXQxluIAt5Ri8NaZo5a3s29i5jlojXfT1S_Vt9PAlLgYEMOW_p-Isrgxq55Jf56m9BP2qCJYZGXee6Gs0Rnd4-hOvdZVWPLaCjurT9yOEA8UaWFZjp-GJOb5ckupPgIl33qzdxDnA76H284AIM3ag-9ACqmSwuQjzYazdyuRxaa2d2As2HVakCnG_GsyC)
3. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4tqEk9wS2Gk-kiEbOIeCJnFcr-pm7jNo1jAOptaqXRLbVzsWfaSNc4jFDSVmtGl54gmhrsliIWamX2VRON51lwqoIx9hFxSGP8ygRzzvf5KYRRLHh6A5VPBwVMUkxeA==)
4. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEajG4irs-cNNvwPOnWzNGc0NwsbnvdGPqKpp92gHnHsIek-_f5JTQjx09xH9n5CgPszrtUBEa5yN6fZ6M7_3pQfQ33HCXbg98UszkMB7Gz-Y2bMABHGGUTyVH1l9s_Rfnw071VVFSONkeIC0HnNbwql71rU76xmyYdMp028WunEJcDhiDmNlbSzBwM8__fbeip_4dc-0dXvlu5sSy4VuvpnKcja37NCfl3l70fq35wHuVpN2nn1yJTk0VS2zXuKgHqj3CFddI2p4PlEN3CU87h)
5. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBoE1QCAUVALgrZwZzPFwB5qwNoskFEChBZ3YbC6JZ62l_4xe5-V3VGJnBBYfwvv-Z3F8_1SUfrlrNX-jfn_bMSpq3lzGEc6xJLO8SAGtAU4a5uz4j7VcmbWeKxV1YxOOaXabHIa6-Kh38Z-sli-FLoedK0Rc5q_MsdkdkFBHg6aVU0Q3Q24OpQxUpuAOupEWrgTTVBdo0wk9S3mAtsVJM_TgSuuCUv9FwK2QH5blKIIrtv1ILSCuuteobaTZvuacjX6WE7nJ9He8eYDvc96KMe5j6zbTKXA==)
6. [nscpolteksby.ac.id](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLIkME6Dn-Oc0m_8u6EykXhr8_nFQ6UGLATWvrMYhuAJRh_HyUPdIS8_gO7Lt_uNeOH1oS4DjhTjvVAmNurZdKCw8V2eXjP3JNARaFSqzBWsxN8WyLd2A4pq9leGQdD6lxmjONoh2t9-ElgtvPu3JdaoVRPg9GS6C9zJcbSAlVOIj9MNzRXYGLr1qQzCcTmDPgT6Ty6WnMBiuN5bttHBEvbdzxVmswBhcSDPJxTv9SXEEYbiI84NCnchFlLkt5a1RqejXhjpda3pWCjpxmUsg_U0A=)
7. [us.es](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKS2RCqP_Dmqiw5nhM0QC-rzAMva0PhusQ1DZUXcvj-mXV0gssdIfBfc4Tw8K3F5GuNkhQz5udtBk9cztIt8wb_vS-2BPvXw46UwBkIcYxAXOeUw4q7SAMpj_sjF6-DPKB_1RJsCdJujpDQhlTNgdkGQMuwxZhQJ8FJODqET2mkeU=)
8. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOhgp-luc9D5kV0MYflxw0_1JEtlUDhEbKy4l7HRHFMYlipfvowygoQVcrF_jWn3Sal_ULCIQkUO1_ME9J8N-VBTYDs4TVr43AF5_5xC9bTjxycTMntnmG0JDjOsc=)
9. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKVnsy6ZJVkmw49wlNd3iIPnTy1QMbVkjxGVu59eUbewf1EQ7x9KeUvuRwLkDbw1DFJIA9YtXV0aQIe9q8dT_XcHxWHJvWwkgoDAp39HMi7bCdSm2jG17dYZFxceBcPZk9SoM9cBOsB0mDpEzGRWNfkdjQT1M61Yg=)
10. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmWo4mAtyTjyRVeJFx38mTmeD8P4Bp9zcyzobKvUx11ldmBio5XJlDiEg0lSm0_17ypDSjklU0BeXczcNWhd48erg_bZB2Cs3SvdKsvSzqfIiFZiFT_nf4nefvwsxVyC5doqRpbI4caiBm5_Qg7lUIOdM=)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEX_PzxQCiEI06WADlEPmlp_3NTumwsWj0bNkBeUVE42vnVSfqN6gQrmpNBNDjIPu9SG8HtacZkCSxZJOpkCdoUwBBTosmq8VKfKH_pg-iRMtbi9dgdSlO8AXTda1v3HarbB8eYLiWCujcVNW-XXFlKRK9cX-1Iq3R9JTcuiTIy5K8yFKoZcesMBwPaZ9rXBKj2C_yGpBpKAEBY8zZcxLoLYM56l3G06n3Xr5MCA-XLgo8_4Xhh8C_PFC-jCyBJsS9w2SnKqq_dCqufHsCEY7a1ZgInDt_ua1Cgvpys52700cDSKyb38bPUKqBSN3lK5H0=)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8DIieTKdAjCK835Ck6lAX66uxe3vmGThO9204bPVSS0g1MkZ8ta3xQA1Txq32SnD8b9hqd6zkdaXJPGKha3DW5zxS6V8Ijz4Al_J1XFrQxKL1omnaNyMINnGex8oiJDTOiWippKC8DIaEqOTFfyclvxr6MmBMhlh12AyI_0DKBm6ojCO8MnVP-Izp-xedrOOsn4DFE57UHwBFIu4k6-4Ird_nhXIATv-p-4n_uSY=)
13. [blogspot.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBu7n5Zmw2MR0jxBBTXuZ-q-I0Aqa-a9cdmBURlnmnNyXe8TEAdezYy0RkPc-QZmxBbY3x92BAnhxYyk8tTjUz-SuXRs-serNpN_eCHaJvpF_WigCFubflHw==)
14. [takeyourbackpack.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRbB8UyfqdurZFK0F0dafpM05e6ljwFXt9CKGJc236iW9dk-_0ezoOe-KjUzMOhZElJ5ae5VLy0jaY-xElq5LuPj_wGzI0JtEV2vBZLvwJEuWSPw0Pow2aMw9T01wLtxTwjb1elOjWSFgFI0Y=)
15. [rnars.org.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHDPCp6jwVkZaXtiueKmwA8-vW7Dc_UKqAHuX5tMKyVwHd9nmLHYR-uEwTbq1iho-Ld7mEReJ5eKZoi7TSwqzfmjT3LwkKmUUj0mcA02rjqTdJIXqB3i21RQ79cdYQ0QhNDl8Kru7pSclmHPQ=)
16. [fareye.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEz30VxaHRfV_0dQvxYHLQK5PwUkZpGM3GqT38n_BuWCQFlx3yeaS-sjtKXp55sfyEaRBDQ7ZkJNbAIyK-B_oqLPzfW5pgCm21O752nny6ceLEf278BEWDwmxh9zJ3mYp3FfEpdC6n1ScSBFIIYgy7q2mWWPWnvP4cvglaKuUrT4HnHmcORWA==)
17. [routific.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIYXhn8RTBFuKOTZo4c9TG5oFIMmyoa7QOIUxtgLlxwxWCCWRR4Xe1tbQsTAbQxVsPlOGiCuAsNQ0NJNrfF_yfgdhltlbBf_YqbhXaLy71p-4LyX7Wa2xwwhoKji6-wY0nC7EXZ3qL2fPKAy-tBM8gBfXT1fQEhKo=)
18. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcoqPrc6h7L9kT_EhrAiU27848UeHXugPY0oR0sTnVvDSgiB0LJXqdgdZomPbWiPhoC7mDlIwCW-zbmIFSz2vNyDIMBmA77a_EbtWrygg12RA3_Wcgi2uBOojpfw==)
19. [cad-journal.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtJsbjcautYDgOYd9qUgc0wM3t66tDMwSRFcVor9-8Un2iFxNW1l-hMhfElFWag1MNc7Fuo9o6gl-XWt3TEVMT9hu8iP56S38L64TXqgNXzqVjWts6UXxCf0F4KhwRKEEQwszZd8VEXftqzvVBeatyGHRUPCJaRJTFazY=)
20. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3vTAZ7OAmTpDGEUAHbUXH4iVLYFaixxEdYaRZZ3mCdtu3XV1uqQ9qFFxFDyxMQcHzyFWWCOCHLADbNiq4xNHJRooS6z4ynB5JfMgrixX-vcN_cwkTefEX8kHxj3Db71WuI11FJrcPzTjzwJ7H_twh-njpgOvQUr_SILU4XkubhbDODXE33k2kDKeDcUeTi8xN-Nn2YAFFW2ZLyPRqKMEYfj7NnW6qLmRrWAlseZD9lXxHD8xPm3iunq5_hiN3D0w=)
21. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzxlf2nc-zXsgWduj6Frdm6ztQAipwkZApC_MnZeBbuL-6GUvyE3C54GqOsNe3Wdcaizz6W2TW4jZnB50rMkvbvLncyDOzptsOJihGdHRoRmlY-5XKRbE-onkSDklIgB8Sr4kZh-5aaftdAPdDgptJYnciBPYegu4qsCh4HI-71lieWH2NVwFNZaK7FxvIiioDnJnM0IIdDoHFrCB-546fb3k=)
22. [diva-portal.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfYzIS83uJB6G0ohtNHqgQIOJkGnxtESs28iyKzcEHAKr4-y3C4KZ8rkZfwWKzXm2mQmOfP4m4UB0UsKp2RDtnE0d-iEZYEuNDu8KUqS4d6cO51V41lCWqeckcNI5UN4e5sp9qOvlT-scom-q6_M8dMI2P7_bkKc8=)
23. [tripcosmos.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJKvy46iQXo2Wh98EyzeLrxM0T0HaHDtR0B-RyZ5COnpFXoq7gXUNmjBe2Pz0FiQuftO9a2AOjWJ6mPwCKj_DhacWpj3N9ypSYgssBMmM132yYPcRe04r41gQW4BQUTUt0IEvo2OkvNBXiRYrChoesxfGCZTpsd3Lf2rhUMHQ9vA==)
24. [maptive.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFv9rI-f4RcL3k3hr2HtqxvCKQOMnxtUr9C8o6es84rv4UTfv_mH34PNV5zpt6yCcinZ6_M88ufzO55Yho7K4yF-Zxkoc0bCMMF7-ZfXQowPNsezkU9sChHhMok1NUgfT5nnga2rIbm5sNJxywzodCfqJCbqN8=)
25. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnWVgQLONjroUL0HvHihU1DxOZ0baoTfV1_oEj4n3O7ZKna5OkV4t1FbGNcwb8SWOKZPshgv2BVc_KB5vxuGvpfC0XzwydSjXBY6txYxkBSzXEB5CA1fIV7FRrR1hM28Lkdh9ySVBchTrWd56QApTMHWo9_xK-Y_bJfZBcW918cgJeXPs=)
26. [econstor.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-H7TEpkJtvu0khJuaS3A06BeVfH71nfcP7i6OvWE6z3-WEugk0aRL1SW6OUzRC0VMGf5VTYLUNRbZ2f7L4DDLVU1RD6PY56j6xLSOs_3JQ0NAMa-0sH_y_7E36L-tpjvKNwXGQO_0xCqRBJvspKc9UMId1vCWQBCDk64m)
27. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHiTwQ-v46AsHjtRDfaUuOBxxmzSeES2M5W39XS1Ey3734JHKQRLfxhekCHeDab5X9hmxD_ZB0kY3HfKq2c2RAq57OYF3HMw1cvNLl2fZ9dYc_llkln6WEKh3PT7OTDvg==)
28. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENcZh0WXmWbHBBLLDo-MZPcu3ipFLbjDQO77xonqWk6gHBzxqDmKWH2oCoxkvohQxeFdWo10zXtoYwt_EAPRefnKpijyUIQRuSU0JOi-pOTaR1LxX29I3pUiLv1zR6iB0eggHn2Uz9Dv4T1YOLV7_6Y-QZBZjNvwPZ-fJ384wJYU_lhdxR_-bub17DXiXcDBLe5LcCUVuMQ2E40PcX6fYLsGbyyTAX3UC6Cq_gI5Fy3sZHxJu9mE1DMRFuLE1VrN-SrI-wmOmW3B_IbpbDJxaRfIOO7kxP)


## Annotations
Annotation(end_index=2086, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRSMZPdzHFLOvzYDLpyj7Kc-mrn4X09_eaIxCiHr1BahDMA-AZsdq-quLzNhKMrNcXCwJgWHHk22E1yADSwG0POFlHvvYvjNg3OmRwIZwqnDnyCXoNHhtzMSyn26IYP4ghKwT8PjoCszzj0cX0y1UFVQXJ_5IPr6ODseDjKLS3D6bms7a3IHXhSFwINtY-rf4ITOMmnVmmPw==', start_index=2074)
Annotation(end_index=2086, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHogUcFDyPpYLOygQUQThL6sSybH09IiQP4LmpEb0IBrDJGmBDmkYkl4YpDLsgOiuk1uyMFTYXZwg7joYCOjFJizKEHLZst35Op8giabTeqw3hf9P9ACGwmXQxluIAt5Ri8NaZo5a3s29i5jlojXfT1S_Vt9PAlLgYEMOW_p-Isrgxq55Jf56m9BP2qCJYZGXee6Gs0Rnd4-hOvdZVWPLaCjurT9yOEA8UaWFZjp-GJOb5ckupPgIl33qzdxDnA76H284AIM3ag-9ACqmSwuQjzYazdyuRxaa2d2As2HVakCnG_GsyC', start_index=2074)
Annotation(end_index=2313, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRSMZPdzHFLOvzYDLpyj7Kc-mrn4X09_eaIxCiHr1BahDMA-AZsdq-quLzNhKMrNcXCwJgWHHk22E1yADSwG0POFlHvvYvjNg3OmRwIZwqnDnyCXoNHhtzMSyn26IYP4ghKwT8PjoCszzj0cX0y1UFVQXJ_5IPr6ODseDjKLS3D6bms7a3IHXhSFwINtY-rf4ITOMmnVmmPw==', start_index=2301)
Annotation(end_index=2313, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4tqEk9wS2Gk-kiEbOIeCJnFcr-pm7jNo1jAOptaqXRLbVzsWfaSNc4jFDSVmtGl54gmhrsliIWamX2VRON51lwqoIx9hFxSGP8ygRzzvf5KYRRLHh6A5VPBwVMUkxeA==', start_index=2301)
Annotation(end_index=2571, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEajG4irs-cNNvwPOnWzNGc0NwsbnvdGPqKpp92gHnHsIek-_f5JTQjx09xH9n5CgPszrtUBEa5yN6fZ6M7_3pQfQ33HCXbg98UszkMB7Gz-Y2bMABHGGUTyVH1l9s_Rfnw071VVFSONkeIC0HnNbwql71rU76xmyYdMp028WunEJcDhiDmNlbSzBwM8__fbeip_4dc-0dXvlu5sSy4VuvpnKcja37NCfl3l70fq35wHuVpN2nn1yJTk0VS2zXuKgHqj3CFddI2p4PlEN3CU87h', start_index=2559)
Annotation(end_index=2571, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRSMZPdzHFLOvzYDLpyj7Kc-mrn4X09_eaIxCiHr1BahDMA-AZsdq-quLzNhKMrNcXCwJgWHHk22E1yADSwG0POFlHvvYvjNg3OmRwIZwqnDnyCXoNHhtzMSyn26IYP4ghKwT8PjoCszzj0cX0y1UFVQXJ_5IPr6ODseDjKLS3D6bms7a3IHXhSFwINtY-rf4ITOMmnVmmPw==', start_index=2559)
Annotation(end_index=2778, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBoE1QCAUVALgrZwZzPFwB5qwNoskFEChBZ3YbC6JZ62l_4xe5-V3VGJnBBYfwvv-Z3F8_1SUfrlrNX-jfn_bMSpq3lzGEc6xJLO8SAGtAU4a5uz4j7VcmbWeKxV1YxOOaXabHIa6-Kh38Z-sli-FLoedK0Rc5q_MsdkdkFBHg6aVU0Q3Q24OpQxUpuAOupEWrgTTVBdo0wk9S3mAtsVJM_TgSuuCUv9FwK2QH5blKIIrtv1ILSCuuteobaTZvuacjX6WE7nJ9He8eYDvc96KMe5j6zbTKXA==', start_index=2769)
Annotation(end_index=3701, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLIkME6Dn-Oc0m_8u6EykXhr8_nFQ6UGLATWvrMYhuAJRh_HyUPdIS8_gO7Lt_uNeOH1oS4DjhTjvVAmNurZdKCw8V2eXjP3JNARaFSqzBWsxN8WyLd2A4pq9leGQdD6lxmjONoh2t9-ElgtvPu3JdaoVRPg9GS6C9zJcbSAlVOIj9MNzRXYGLr1qQzCcTmDPgT6Ty6WnMBiuN5bttHBEvbdzxVmswBhcSDPJxTv9SXEEYbiI84NCnchFlLkt5a1RqejXhjpda3pWCjpxmUsg_U0A=', start_index=3692)
Annotation(end_index=3953, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKS2RCqP_Dmqiw5nhM0QC-rzAMva0PhusQ1DZUXcvj-mXV0gssdIfBfc4Tw8K3F5GuNkhQz5udtBk9cztIt8wb_vS-2BPvXw46UwBkIcYxAXOeUw4q7SAMpj_sjF6-DPKB_1RJsCdJujpDQhlTNgdkGQMuwxZhQJ8FJODqET2mkeU=', start_index=3941)
Annotation(end_index=3953, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHogUcFDyPpYLOygQUQThL6sSybH09IiQP4LmpEb0IBrDJGmBDmkYkl4YpDLsgOiuk1uyMFTYXZwg7joYCOjFJizKEHLZst35Op8giabTeqw3hf9P9ACGwmXQxluIAt5Ri8NaZo5a3s29i5jlojXfT1S_Vt9PAlLgYEMOW_p-Isrgxq55Jf56m9BP2qCJYZGXee6Gs0Rnd4-hOvdZVWPLaCjurT9yOEA8UaWFZjp-GJOb5ckupPgIl33qzdxDnA76H284AIM3ag-9ACqmSwuQjzYazdyuRxaa2d2As2HVakCnG_GsyC', start_index=3941)
Annotation(end_index=4299, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRSMZPdzHFLOvzYDLpyj7Kc-mrn4X09_eaIxCiHr1BahDMA-AZsdq-quLzNhKMrNcXCwJgWHHk22E1yADSwG0POFlHvvYvjNg3OmRwIZwqnDnyCXoNHhtzMSyn26IYP4ghKwT8PjoCszzj0cX0y1UFVQXJ_5IPr6ODseDjKLS3D6bms7a3IHXhSFwINtY-rf4ITOMmnVmmPw==', start_index=4290)
Annotation(end_index=4589, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRSMZPdzHFLOvzYDLpyj7Kc-mrn4X09_eaIxCiHr1BahDMA-AZsdq-quLzNhKMrNcXCwJgWHHk22E1yADSwG0POFlHvvYvjNg3OmRwIZwqnDnyCXoNHhtzMSyn26IYP4ghKwT8PjoCszzj0cX0y1UFVQXJ_5IPr6ODseDjKLS3D6bms7a3IHXhSFwINtY-rf4ITOMmnVmmPw==', start_index=4580)
Annotation(end_index=4796, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRSMZPdzHFLOvzYDLpyj7Kc-mrn4X09_eaIxCiHr1BahDMA-AZsdq-quLzNhKMrNcXCwJgWHHk22E1yADSwG0POFlHvvYvjNg3OmRwIZwqnDnyCXoNHhtzMSyn26IYP4ghKwT8PjoCszzj0cX0y1UFVQXJ_5IPr6ODseDjKLS3D6bms7a3IHXhSFwINtY-rf4ITOMmnVmmPw==', start_index=4787)
Annotation(end_index=5061, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOhgp-luc9D5kV0MYflxw0_1JEtlUDhEbKy4l7HRHFMYlipfvowygoQVcrF_jWn3Sal_ULCIQkUO1_ME9J8N-VBTYDs4TVr43AF5_5xC9bTjxycTMntnmG0JDjOsc=', start_index=5052)
Annotation(end_index=5425, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBoE1QCAUVALgrZwZzPFwB5qwNoskFEChBZ3YbC6JZ62l_4xe5-V3VGJnBBYfwvv-Z3F8_1SUfrlrNX-jfn_bMSpq3lzGEc6xJLO8SAGtAU4a5uz4j7VcmbWeKxV1YxOOaXabHIa6-Kh38Z-sli-FLoedK0Rc5q_MsdkdkFBHg6aVU0Q3Q24OpQxUpuAOupEWrgTTVBdo0wk9S3mAtsVJM_TgSuuCUv9FwK2QH5blKIIrtv1ILSCuuteobaTZvuacjX6WE7nJ9He8eYDvc96KMe5j6zbTKXA==', start_index=5416)
Annotation(end_index=5798, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBoE1QCAUVALgrZwZzPFwB5qwNoskFEChBZ3YbC6JZ62l_4xe5-V3VGJnBBYfwvv-Z3F8_1SUfrlrNX-jfn_bMSpq3lzGEc6xJLO8SAGtAU4a5uz4j7VcmbWeKxV1YxOOaXabHIa6-Kh38Z-sli-FLoedK0Rc5q_MsdkdkFBHg6aVU0Q3Q24OpQxUpuAOupEWrgTTVBdo0wk9S3mAtsVJM_TgSuuCUv9FwK2QH5blKIIrtv1ILSCuuteobaTZvuacjX6WE7nJ9He8eYDvc96KMe5j6zbTKXA==', start_index=5789)
Annotation(end_index=6317, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRSMZPdzHFLOvzYDLpyj7Kc-mrn4X09_eaIxCiHr1BahDMA-AZsdq-quLzNhKMrNcXCwJgWHHk22E1yADSwG0POFlHvvYvjNg3OmRwIZwqnDnyCXoNHhtzMSyn26IYP4ghKwT8PjoCszzj0cX0y1UFVQXJ_5IPr6ODseDjKLS3D6bms7a3IHXhSFwINtY-rf4ITOMmnVmmPw==', start_index=6308)
Annotation(end_index=6688, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKVnsy6ZJVkmw49wlNd3iIPnTy1QMbVkjxGVu59eUbewf1EQ7x9KeUvuRwLkDbw1DFJIA9YtXV0aQIe9q8dT_XcHxWHJvWwkgoDAp39HMi7bCdSm2jG17dYZFxceBcPZk9SoM9cBOsB0mDpEzGRWNfkdjQT1M61Yg=', start_index=6676)
Annotation(end_index=6688, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4tqEk9wS2Gk-kiEbOIeCJnFcr-pm7jNo1jAOptaqXRLbVzsWfaSNc4jFDSVmtGl54gmhrsliIWamX2VRON51lwqoIx9hFxSGP8ygRzzvf5KYRRLHh6A5VPBwVMUkxeA==', start_index=6676)
Annotation(end_index=7379, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRSMZPdzHFLOvzYDLpyj7Kc-mrn4X09_eaIxCiHr1BahDMA-AZsdq-quLzNhKMrNcXCwJgWHHk22E1yADSwG0POFlHvvYvjNg3OmRwIZwqnDnyCXoNHhtzMSyn26IYP4ghKwT8PjoCszzj0cX0y1UFVQXJ_5IPr6ODseDjKLS3D6bms7a3IHXhSFwINtY-rf4ITOMmnVmmPw==', start_index=7370)
Annotation(end_index=7922, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRSMZPdzHFLOvzYDLpyj7Kc-mrn4X09_eaIxCiHr1BahDMA-AZsdq-quLzNhKMrNcXCwJgWHHk22E1yADSwG0POFlHvvYvjNg3OmRwIZwqnDnyCXoNHhtzMSyn26IYP4ghKwT8PjoCszzj0cX0y1UFVQXJ_5IPr6ODseDjKLS3D6bms7a3IHXhSFwINtY-rf4ITOMmnVmmPw==', start_index=7913)
Annotation(end_index=8181, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4tqEk9wS2Gk-kiEbOIeCJnFcr-pm7jNo1jAOptaqXRLbVzsWfaSNc4jFDSVmtGl54gmhrsliIWamX2VRON51lwqoIx9hFxSGP8ygRzzvf5KYRRLHh6A5VPBwVMUkxeA==', start_index=8172)
Annotation(end_index=8710, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRSMZPdzHFLOvzYDLpyj7Kc-mrn4X09_eaIxCiHr1BahDMA-AZsdq-quLzNhKMrNcXCwJgWHHk22E1yADSwG0POFlHvvYvjNg3OmRwIZwqnDnyCXoNHhtzMSyn26IYP4ghKwT8PjoCszzj0cX0y1UFVQXJ_5IPr6ODseDjKLS3D6bms7a3IHXhSFwINtY-rf4ITOMmnVmmPw==', start_index=8701)
Annotation(end_index=9219, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmWo4mAtyTjyRVeJFx38mTmeD8P4Bp9zcyzobKvUx11ldmBio5XJlDiEg0lSm0_17ypDSjklU0BeXczcNWhd48erg_bZB2Cs3SvdKsvSzqfIiFZiFT_nf4nefvwsxVyC5doqRpbI4caiBm5_Qg7lUIOdM=', start_index=9206)
Annotation(end_index=9219, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHogUcFDyPpYLOygQUQThL6sSybH09IiQP4LmpEb0IBrDJGmBDmkYkl4YpDLsgOiuk1uyMFTYXZwg7joYCOjFJizKEHLZst35Op8giabTeqw3hf9P9ACGwmXQxluIAt5Ri8NaZo5a3s29i5jlojXfT1S_Vt9PAlLgYEMOW_p-Isrgxq55Jf56m9BP2qCJYZGXee6Gs0Rnd4-hOvdZVWPLaCjurT9yOEA8UaWFZjp-GJOb5ckupPgIl33qzdxDnA76H284AIM3ag-9ACqmSwuQjzYazdyuRxaa2d2As2HVakCnG_GsyC', start_index=9206)
Annotation(end_index=9780, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4tqEk9wS2Gk-kiEbOIeCJnFcr-pm7jNo1jAOptaqXRLbVzsWfaSNc4jFDSVmtGl54gmhrsliIWamX2VRON51lwqoIx9hFxSGP8ygRzzvf5KYRRLHh6A5VPBwVMUkxeA==', start_index=9771)
Annotation(end_index=10387, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBoE1QCAUVALgrZwZzPFwB5qwNoskFEChBZ3YbC6JZ62l_4xe5-V3VGJnBBYfwvv-Z3F8_1SUfrlrNX-jfn_bMSpq3lzGEc6xJLO8SAGtAU4a5uz4j7VcmbWeKxV1YxOOaXabHIa6-Kh38Z-sli-FLoedK0Rc5q_MsdkdkFBHg6aVU0Q3Q24OpQxUpuAOupEWrgTTVBdo0wk9S3mAtsVJM_TgSuuCUv9FwK2QH5blKIIrtv1ILSCuuteobaTZvuacjX6WE7nJ9He8eYDvc96KMe5j6zbTKXA==', start_index=10374)
Annotation(end_index=10387, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEX_PzxQCiEI06WADlEPmlp_3NTumwsWj0bNkBeUVE42vnVSfqN6gQrmpNBNDjIPu9SG8HtacZkCSxZJOpkCdoUwBBTosmq8VKfKH_pg-iRMtbi9dgdSlO8AXTda1v3HarbB8eYLiWCujcVNW-XXFlKRK9cX-1Iq3R9JTcuiTIy5K8yFKoZcesMBwPaZ9rXBKj2C_yGpBpKAEBY8zZcxLoLYM56l3G06n3Xr5MCA-XLgo8_4Xhh8C_PFC-jCyBJsS9w2SnKqq_dCqufHsCEY7a1ZgInDt_ua1Cgvpys52700cDSKyb38bPUKqBSN3lK5H0=', start_index=10374)
Annotation(end_index=10874, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBoE1QCAUVALgrZwZzPFwB5qwNoskFEChBZ3YbC6JZ62l_4xe5-V3VGJnBBYfwvv-Z3F8_1SUfrlrNX-jfn_bMSpq3lzGEc6xJLO8SAGtAU4a5uz4j7VcmbWeKxV1YxOOaXabHIa6-Kh38Z-sli-FLoedK0Rc5q_MsdkdkFBHg6aVU0Q3Q24OpQxUpuAOupEWrgTTVBdo0wk9S3mAtsVJM_TgSuuCUv9FwK2QH5blKIIrtv1ILSCuuteobaTZvuacjX6WE7nJ9He8eYDvc96KMe5j6zbTKXA==', start_index=10865)
Annotation(end_index=11128, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBoE1QCAUVALgrZwZzPFwB5qwNoskFEChBZ3YbC6JZ62l_4xe5-V3VGJnBBYfwvv-Z3F8_1SUfrlrNX-jfn_bMSpq3lzGEc6xJLO8SAGtAU4a5uz4j7VcmbWeKxV1YxOOaXabHIa6-Kh38Z-sli-FLoedK0Rc5q_MsdkdkFBHg6aVU0Q3Q24OpQxUpuAOupEWrgTTVBdo0wk9S3mAtsVJM_TgSuuCUv9FwK2QH5blKIIrtv1ILSCuuteobaTZvuacjX6WE7nJ9He8eYDvc96KMe5j6zbTKXA==', start_index=11119)
Annotation(end_index=11340, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBoE1QCAUVALgrZwZzPFwB5qwNoskFEChBZ3YbC6JZ62l_4xe5-V3VGJnBBYfwvv-Z3F8_1SUfrlrNX-jfn_bMSpq3lzGEc6xJLO8SAGtAU4a5uz4j7VcmbWeKxV1YxOOaXabHIa6-Kh38Z-sli-FLoedK0Rc5q_MsdkdkFBHg6aVU0Q3Q24OpQxUpuAOupEWrgTTVBdo0wk9S3mAtsVJM_TgSuuCUv9FwK2QH5blKIIrtv1ILSCuuteobaTZvuacjX6WE7nJ9He8eYDvc96KMe5j6zbTKXA==', start_index=11331)
Annotation(end_index=11725, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBoE1QCAUVALgrZwZzPFwB5qwNoskFEChBZ3YbC6JZ62l_4xe5-V3VGJnBBYfwvv-Z3F8_1SUfrlrNX-jfn_bMSpq3lzGEc6xJLO8SAGtAU4a5uz4j7VcmbWeKxV1YxOOaXabHIa6-Kh38Z-sli-FLoedK0Rc5q_MsdkdkFBHg6aVU0Q3Q24OpQxUpuAOupEWrgTTVBdo0wk9S3mAtsVJM_TgSuuCUv9FwK2QH5blKIIrtv1ILSCuuteobaTZvuacjX6WE7nJ9He8eYDvc96KMe5j6zbTKXA==', start_index=11716)
Annotation(end_index=12006, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8DIieTKdAjCK835Ck6lAX66uxe3vmGThO9204bPVSS0g1MkZ8ta3xQA1Txq32SnD8b9hqd6zkdaXJPGKha3DW5zxS6V8Ijz4Al_J1XFrQxKL1omnaNyMINnGex8oiJDTOiWippKC8DIaEqOTFfyclvxr6MmBMhlh12AyI_0DKBm6ojCO8MnVP-Izp-xedrOOsn4DFE57UHwBFIu4k6-4Ird_nhXIATv-p-4n_uSY=', start_index=11993)
Annotation(end_index=12006, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBoE1QCAUVALgrZwZzPFwB5qwNoskFEChBZ3YbC6JZ62l_4xe5-V3VGJnBBYfwvv-Z3F8_1SUfrlrNX-jfn_bMSpq3lzGEc6xJLO8SAGtAU4a5uz4j7VcmbWeKxV1YxOOaXabHIa6-Kh38Z-sli-FLoedK0Rc5q_MsdkdkFBHg6aVU0Q3Q24OpQxUpuAOupEWrgTTVBdo0wk9S3mAtsVJM_TgSuuCUv9FwK2QH5blKIIrtv1ILSCuuteobaTZvuacjX6WE7nJ9He8eYDvc96KMe5j6zbTKXA==', start_index=11993)
Annotation(end_index=12255, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBoE1QCAUVALgrZwZzPFwB5qwNoskFEChBZ3YbC6JZ62l_4xe5-V3VGJnBBYfwvv-Z3F8_1SUfrlrNX-jfn_bMSpq3lzGEc6xJLO8SAGtAU4a5uz4j7VcmbWeKxV1YxOOaXabHIa6-Kh38Z-sli-FLoedK0Rc5q_MsdkdkFBHg6aVU0Q3Q24OpQxUpuAOupEWrgTTVBdo0wk9S3mAtsVJM_TgSuuCUv9FwK2QH5blKIIrtv1ILSCuuteobaTZvuacjX6WE7nJ9He8eYDvc96KMe5j6zbTKXA==', start_index=12246)
Annotation(end_index=12694, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBu7n5Zmw2MR0jxBBTXuZ-q-I0Aqa-a9cdmBURlnmnNyXe8TEAdezYy0RkPc-QZmxBbY3x92BAnhxYyk8tTjUz-SuXRs-serNpN_eCHaJvpF_WigCFubflHw==', start_index=12684)
Annotation(end_index=13295, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBoE1QCAUVALgrZwZzPFwB5qwNoskFEChBZ3YbC6JZ62l_4xe5-V3VGJnBBYfwvv-Z3F8_1SUfrlrNX-jfn_bMSpq3lzGEc6xJLO8SAGtAU4a5uz4j7VcmbWeKxV1YxOOaXabHIa6-Kh38Z-sli-FLoedK0Rc5q_MsdkdkFBHg6aVU0Q3Q24OpQxUpuAOupEWrgTTVBdo0wk9S3mAtsVJM_TgSuuCUv9FwK2QH5blKIIrtv1ILSCuuteobaTZvuacjX6WE7nJ9He8eYDvc96KMe5j6zbTKXA==', start_index=13286)
Annotation(end_index=13869, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBoE1QCAUVALgrZwZzPFwB5qwNoskFEChBZ3YbC6JZ62l_4xe5-V3VGJnBBYfwvv-Z3F8_1SUfrlrNX-jfn_bMSpq3lzGEc6xJLO8SAGtAU4a5uz4j7VcmbWeKxV1YxOOaXabHIa6-Kh38Z-sli-FLoedK0Rc5q_MsdkdkFBHg6aVU0Q3Q24OpQxUpuAOupEWrgTTVBdo0wk9S3mAtsVJM_TgSuuCUv9FwK2QH5blKIIrtv1ILSCuuteobaTZvuacjX6WE7nJ9He8eYDvc96KMe5j6zbTKXA==', start_index=13860)
Annotation(end_index=14204, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBoE1QCAUVALgrZwZzPFwB5qwNoskFEChBZ3YbC6JZ62l_4xe5-V3VGJnBBYfwvv-Z3F8_1SUfrlrNX-jfn_bMSpq3lzGEc6xJLO8SAGtAU4a5uz4j7VcmbWeKxV1YxOOaXabHIa6-Kh38Z-sli-FLoedK0Rc5q_MsdkdkFBHg6aVU0Q3Q24OpQxUpuAOupEWrgTTVBdo0wk9S3mAtsVJM_TgSuuCUv9FwK2QH5blKIIrtv1ILSCuuteobaTZvuacjX6WE7nJ9He8eYDvc96KMe5j6zbTKXA==', start_index=14195)
Annotation(end_index=14465, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBoE1QCAUVALgrZwZzPFwB5qwNoskFEChBZ3YbC6JZ62l_4xe5-V3VGJnBBYfwvv-Z3F8_1SUfrlrNX-jfn_bMSpq3lzGEc6xJLO8SAGtAU4a5uz4j7VcmbWeKxV1YxOOaXabHIa6-Kh38Z-sli-FLoedK0Rc5q_MsdkdkFBHg6aVU0Q3Q24OpQxUpuAOupEWrgTTVBdo0wk9S3mAtsVJM_TgSuuCUv9FwK2QH5blKIIrtv1ILSCuuteobaTZvuacjX6WE7nJ9He8eYDvc96KMe5j6zbTKXA==', start_index=14456)
Annotation(end_index=14750, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRbB8UyfqdurZFK0F0dafpM05e6ljwFXt9CKGJc236iW9dk-_0ezoOe-KjUzMOhZElJ5ae5VLy0jaY-xElq5LuPj_wGzI0JtEV2vBZLvwJEuWSPw0Pow2aMw9T01wLtxTwjb1elOjWSFgFI0Y=', start_index=14736)
Annotation(end_index=14750, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHDPCp6jwVkZaXtiueKmwA8-vW7Dc_UKqAHuX5tMKyVwHd9nmLHYR-uEwTbq1iho-Ld7mEReJ5eKZoi7TSwqzfmjT3LwkKmUUj0mcA02rjqTdJIXqB3i21RQ79cdYQ0QhNDl8Kru7pSclmHPQ=', start_index=14736)
Annotation(end_index=15001, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRbB8UyfqdurZFK0F0dafpM05e6ljwFXt9CKGJc236iW9dk-_0ezoOe-KjUzMOhZElJ5ae5VLy0jaY-xElq5LuPj_wGzI0JtEV2vBZLvwJEuWSPw0Pow2aMw9T01wLtxTwjb1elOjWSFgFI0Y=', start_index=14991)
Annotation(end_index=15264, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEz30VxaHRfV_0dQvxYHLQK5PwUkZpGM3GqT38n_BuWCQFlx3yeaS-sjtKXp55sfyEaRBDQ7ZkJNbAIyK-B_oqLPzfW5pgCm21O752nny6ceLEf278BEWDwmxh9zJ3mYp3FfEpdC6n1ScSBFIIYgy7q2mWWPWnvP4cvglaKuUrT4HnHmcORWA==', start_index=15250)
Annotation(end_index=15264, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIYXhn8RTBFuKOTZo4c9TG5oFIMmyoa7QOIUxtgLlxwxWCCWRR4Xe1tbQsTAbQxVsPlOGiCuAsNQ0NJNrfF_yfgdhltlbBf_YqbhXaLy71p-4LyX7Wa2xwwhoKji6-wY0nC7EXZ3qL2fPKAy-tBM8gBfXT1fQEhKo=', start_index=15250)
Annotation(end_index=15833, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcoqPrc6h7L9kT_EhrAiU27848UeHXugPY0oR0sTnVvDSgiB0LJXqdgdZomPbWiPhoC7mDlIwCW-zbmIFSz2vNyDIMBmA77a_EbtWrygg12RA3_Wcgi2uBOojpfw==', start_index=15823)
Annotation(end_index=16319, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcoqPrc6h7L9kT_EhrAiU27848UeHXugPY0oR0sTnVvDSgiB0LJXqdgdZomPbWiPhoC7mDlIwCW-zbmIFSz2vNyDIMBmA77a_EbtWrygg12RA3_Wcgi2uBOojpfw==', start_index=16309)
Annotation(end_index=16507, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcoqPrc6h7L9kT_EhrAiU27848UeHXugPY0oR0sTnVvDSgiB0LJXqdgdZomPbWiPhoC7mDlIwCW-zbmIFSz2vNyDIMBmA77a_EbtWrygg12RA3_Wcgi2uBOojpfw==', start_index=16497)
Annotation(end_index=16820, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcoqPrc6h7L9kT_EhrAiU27848UeHXugPY0oR0sTnVvDSgiB0LJXqdgdZomPbWiPhoC7mDlIwCW-zbmIFSz2vNyDIMBmA77a_EbtWrygg12RA3_Wcgi2uBOojpfw==', start_index=16807)
Annotation(end_index=16820, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRSMZPdzHFLOvzYDLpyj7Kc-mrn4X09_eaIxCiHr1BahDMA-AZsdq-quLzNhKMrNcXCwJgWHHk22E1yADSwG0POFlHvvYvjNg3OmRwIZwqnDnyCXoNHhtzMSyn26IYP4ghKwT8PjoCszzj0cX0y1UFVQXJ_5IPr6ODseDjKLS3D6bms7a3IHXhSFwINtY-rf4ITOMmnVmmPw==', start_index=16807)
Annotation(end_index=17040, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtJsbjcautYDgOYd9qUgc0wM3t66tDMwSRFcVor9-8Un2iFxNW1l-hMhfElFWag1MNc7Fuo9o6gl-XWt3TEVMT9hu8iP56S38L64TXqgNXzqVjWts6UXxCf0F4KhwRKEEQwszZd8VEXftqzvVBeatyGHRUPCJaRJTFazY=', start_index=17030)
Annotation(end_index=17570, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOhgp-luc9D5kV0MYflxw0_1JEtlUDhEbKy4l7HRHFMYlipfvowygoQVcrF_jWn3Sal_ULCIQkUO1_ME9J8N-VBTYDs4TVr43AF5_5xC9bTjxycTMntnmG0JDjOsc=', start_index=17561)
Annotation(end_index=17831, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRSMZPdzHFLOvzYDLpyj7Kc-mrn4X09_eaIxCiHr1BahDMA-AZsdq-quLzNhKMrNcXCwJgWHHk22E1yADSwG0POFlHvvYvjNg3OmRwIZwqnDnyCXoNHhtzMSyn26IYP4ghKwT8PjoCszzj0cX0y1UFVQXJ_5IPr6ODseDjKLS3D6bms7a3IHXhSFwINtY-rf4ITOMmnVmmPw==', start_index=17819)
Annotation(end_index=17831, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLIkME6Dn-Oc0m_8u6EykXhr8_nFQ6UGLATWvrMYhuAJRh_HyUPdIS8_gO7Lt_uNeOH1oS4DjhTjvVAmNurZdKCw8V2eXjP3JNARaFSqzBWsxN8WyLd2A4pq9leGQdD6lxmjONoh2t9-ElgtvPu3JdaoVRPg9GS6C9zJcbSAlVOIj9MNzRXYGLr1qQzCcTmDPgT6Ty6WnMBiuN5bttHBEvbdzxVmswBhcSDPJxTv9SXEEYbiI84NCnchFlLkt5a1RqejXhjpda3pWCjpxmUsg_U0A=', start_index=17819)
Annotation(end_index=18270, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRSMZPdzHFLOvzYDLpyj7Kc-mrn4X09_eaIxCiHr1BahDMA-AZsdq-quLzNhKMrNcXCwJgWHHk22E1yADSwG0POFlHvvYvjNg3OmRwIZwqnDnyCXoNHhtzMSyn26IYP4ghKwT8PjoCszzj0cX0y1UFVQXJ_5IPr6ODseDjKLS3D6bms7a3IHXhSFwINtY-rf4ITOMmnVmmPw==', start_index=18261)
Annotation(end_index=18743, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4tqEk9wS2Gk-kiEbOIeCJnFcr-pm7jNo1jAOptaqXRLbVzsWfaSNc4jFDSVmtGl54gmhrsliIWamX2VRON51lwqoIx9hFxSGP8ygRzzvf5KYRRLHh6A5VPBwVMUkxeA==', start_index=18734)
Annotation(end_index=19007, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4tqEk9wS2Gk-kiEbOIeCJnFcr-pm7jNo1jAOptaqXRLbVzsWfaSNc4jFDSVmtGl54gmhrsliIWamX2VRON51lwqoIx9hFxSGP8ygRzzvf5KYRRLHh6A5VPBwVMUkxeA==', start_index=18998)
Annotation(end_index=19711, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3vTAZ7OAmTpDGEUAHbUXH4iVLYFaixxEdYaRZZ3mCdtu3XV1uqQ9qFFxFDyxMQcHzyFWWCOCHLADbNiq4xNHJRooS6z4ynB5JfMgrixX-vcN_cwkTefEX8kHxj3Db71WuI11FJrcPzTjzwJ7H_twh-njpgOvQUr_SILU4XkubhbDODXE33k2kDKeDcUeTi8xN-Nn2YAFFW2ZLyPRqKMEYfj7NnW6qLmRrWAlseZD9lXxHD8xPm3iunq5_hiN3D0w=', start_index=19698)
Annotation(end_index=19711, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLIkME6Dn-Oc0m_8u6EykXhr8_nFQ6UGLATWvrMYhuAJRh_HyUPdIS8_gO7Lt_uNeOH1oS4DjhTjvVAmNurZdKCw8V2eXjP3JNARaFSqzBWsxN8WyLd2A4pq9leGQdD6lxmjONoh2t9-ElgtvPu3JdaoVRPg9GS6C9zJcbSAlVOIj9MNzRXYGLr1qQzCcTmDPgT6Ty6WnMBiuN5bttHBEvbdzxVmswBhcSDPJxTv9SXEEYbiI84NCnchFlLkt5a1RqejXhjpda3pWCjpxmUsg_U0A=', start_index=19698)
Annotation(end_index=20092, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzxlf2nc-zXsgWduj6Frdm6ztQAipwkZApC_MnZeBbuL-6GUvyE3C54GqOsNe3Wdcaizz6W2TW4jZnB50rMkvbvLncyDOzptsOJihGdHRoRmlY-5XKRbE-onkSDklIgB8Sr4kZh-5aaftdAPdDgptJYnciBPYegu4qsCh4HI-71lieWH2NVwFNZaK7FxvIiioDnJnM0IIdDoHFrCB-546fb3k=', start_index=20078)
Annotation(end_index=20092, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3vTAZ7OAmTpDGEUAHbUXH4iVLYFaixxEdYaRZZ3mCdtu3XV1uqQ9qFFxFDyxMQcHzyFWWCOCHLADbNiq4xNHJRooS6z4ynB5JfMgrixX-vcN_cwkTefEX8kHxj3Db71WuI11FJrcPzTjzwJ7H_twh-njpgOvQUr_SILU4XkubhbDODXE33k2kDKeDcUeTi8xN-Nn2YAFFW2ZLyPRqKMEYfj7NnW6qLmRrWAlseZD9lXxHD8xPm3iunq5_hiN3D0w=', start_index=20078)
Annotation(end_index=20464, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfYzIS83uJB6G0ohtNHqgQIOJkGnxtESs28iyKzcEHAKr4-y3C4KZ8rkZfwWKzXm2mQmOfP4m4UB0UsKp2RDtnE0d-iEZYEuNDu8KUqS4d6cO51V41lCWqeckcNI5UN4e5sp9qOvlT-scom-q6_M8dMI2P7_bkKc8=', start_index=20454)
Annotation(end_index=20840, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRSMZPdzHFLOvzYDLpyj7Kc-mrn4X09_eaIxCiHr1BahDMA-AZsdq-quLzNhKMrNcXCwJgWHHk22E1yADSwG0POFlHvvYvjNg3OmRwIZwqnDnyCXoNHhtzMSyn26IYP4ghKwT8PjoCszzj0cX0y1UFVQXJ_5IPr6ODseDjKLS3D6bms7a3IHXhSFwINtY-rf4ITOMmnVmmPw==', start_index=20827)
Annotation(end_index=20840, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJKvy46iQXo2Wh98EyzeLrxM0T0HaHDtR0B-RyZ5COnpFXoq7gXUNmjBe2Pz0FiQuftO9a2AOjWJ6mPwCKj_DhacWpj3N9ypSYgssBMmM132yYPcRe04r41gQW4BQUTUt0IEvo2OkvNBXiRYrChoesxfGCZTpsd3Lf2rhUMHQ9vA==', start_index=20827)
Annotation(end_index=21119, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJKvy46iQXo2Wh98EyzeLrxM0T0HaHDtR0B-RyZ5COnpFXoq7gXUNmjBe2Pz0FiQuftO9a2AOjWJ6mPwCKj_DhacWpj3N9ypSYgssBMmM132yYPcRe04r41gQW4BQUTUt0IEvo2OkvNBXiRYrChoesxfGCZTpsd3Lf2rhUMHQ9vA==', start_index=21109)
Annotation(end_index=21677, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRSMZPdzHFLOvzYDLpyj7Kc-mrn4X09_eaIxCiHr1BahDMA-AZsdq-quLzNhKMrNcXCwJgWHHk22E1yADSwG0POFlHvvYvjNg3OmRwIZwqnDnyCXoNHhtzMSyn26IYP4ghKwT8PjoCszzj0cX0y1UFVQXJ_5IPr6ODseDjKLS3D6bms7a3IHXhSFwINtY-rf4ITOMmnVmmPw==', start_index=21665)
Annotation(end_index=21677, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4tqEk9wS2Gk-kiEbOIeCJnFcr-pm7jNo1jAOptaqXRLbVzsWfaSNc4jFDSVmtGl54gmhrsliIWamX2VRON51lwqoIx9hFxSGP8ygRzzvf5KYRRLHh6A5VPBwVMUkxeA==', start_index=21665)
Annotation(end_index=21963, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBoE1QCAUVALgrZwZzPFwB5qwNoskFEChBZ3YbC6JZ62l_4xe5-V3VGJnBBYfwvv-Z3F8_1SUfrlrNX-jfn_bMSpq3lzGEc6xJLO8SAGtAU4a5uz4j7VcmbWeKxV1YxOOaXabHIa6-Kh38Z-sli-FLoedK0Rc5q_MsdkdkFBHg6aVU0Q3Q24OpQxUpuAOupEWrgTTVBdo0wk9S3mAtsVJM_TgSuuCUv9FwK2QH5blKIIrtv1ILSCuuteobaTZvuacjX6WE7nJ9He8eYDvc96KMe5j6zbTKXA==', start_index=21954)
Annotation(end_index=22246, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcoqPrc6h7L9kT_EhrAiU27848UeHXugPY0oR0sTnVvDSgiB0LJXqdgdZomPbWiPhoC7mDlIwCW-zbmIFSz2vNyDIMBmA77a_EbtWrygg12RA3_Wcgi2uBOojpfw==', start_index=22236)
Annotation(end_index=22558, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEz30VxaHRfV_0dQvxYHLQK5PwUkZpGM3GqT38n_BuWCQFlx3yeaS-sjtKXp55sfyEaRBDQ7ZkJNbAIyK-B_oqLPzfW5pgCm21O752nny6ceLEf278BEWDwmxh9zJ3mYp3FfEpdC6n1ScSBFIIYgy7q2mWWPWnvP4cvglaKuUrT4HnHmcORWA==', start_index=22548)
Annotation(end_index=22640, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFv9rI-f4RcL3k3hr2HtqxvCKQOMnxtUr9C8o6es84rv4UTfv_mH34PNV5zpt6yCcinZ6_M88ufzO55Yho7K4yF-Zxkoc0bCMMF7-ZfXQowPNsezkU9sChHhMok1NUgfT5nnga2rIbm5sNJxywzodCfqJCbqN8=', start_index=22630)
Annotation(end_index=22716, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIYXhn8RTBFuKOTZo4c9TG5oFIMmyoa7QOIUxtgLlxwxWCCWRR4Xe1tbQsTAbQxVsPlOGiCuAsNQ0NJNrfF_yfgdhltlbBf_YqbhXaLy71p-4LyX7Wa2xwwhoKji6-wY0nC7EXZ3qL2fPKAy-tBM8gBfXT1fQEhKo=', start_index=22706)
Annotation(end_index=22790, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGOhgp-luc9D5kV0MYflxw0_1JEtlUDhEbKy4l7HRHFMYlipfvowygoQVcrF_jWn3Sal_ULCIQkUO1_ME9J8N-VBTYDs4TVr43AF5_5xC9bTjxycTMntnmG0JDjOsc=', start_index=22781)
Annotation(end_index=22858, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBoE1QCAUVALgrZwZzPFwB5qwNoskFEChBZ3YbC6JZ62l_4xe5-V3VGJnBBYfwvv-Z3F8_1SUfrlrNX-jfn_bMSpq3lzGEc6xJLO8SAGtAU4a5uz4j7VcmbWeKxV1YxOOaXabHIa6-Kh38Z-sli-FLoedK0Rc5q_MsdkdkFBHg6aVU0Q3Q24OpQxUpuAOupEWrgTTVBdo0wk9S3mAtsVJM_TgSuuCUv9FwK2QH5blKIIrtv1ILSCuuteobaTZvuacjX6WE7nJ9He8eYDvc96KMe5j6zbTKXA==', start_index=22849)
Annotation(end_index=23027, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEajG4irs-cNNvwPOnWzNGc0NwsbnvdGPqKpp92gHnHsIek-_f5JTQjx09xH9n5CgPszrtUBEa5yN6fZ6M7_3pQfQ33HCXbg98UszkMB7Gz-Y2bMABHGGUTyVH1l9s_Rfnw071VVFSONkeIC0HnNbwql71rU76xmyYdMp028WunEJcDhiDmNlbSzBwM8__fbeip_4dc-0dXvlu5sSy4VuvpnKcja37NCfl3l70fq35wHuVpN2nn1yJTk0VS2zXuKgHqj3CFddI2p4PlEN3CU87h', start_index=23011)
Annotation(end_index=23027, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnWVgQLONjroUL0HvHihU1DxOZ0baoTfV1_oEj4n3O7ZKna5OkV4t1FbGNcwb8SWOKZPshgv2BVc_KB5vxuGvpfC0XzwydSjXBY6txYxkBSzXEB5CA1fIV7FRrR1hM28Lkdh9ySVBchTrWd56QApTMHWo9_xK-Y_bJfZBcW918cgJeXPs=', start_index=23011)
Annotation(end_index=23027, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRSMZPdzHFLOvzYDLpyj7Kc-mrn4X09_eaIxCiHr1BahDMA-AZsdq-quLzNhKMrNcXCwJgWHHk22E1yADSwG0POFlHvvYvjNg3OmRwIZwqnDnyCXoNHhtzMSyn26IYP4ghKwT8PjoCszzj0cX0y1UFVQXJ_5IPr6ODseDjKLS3D6bms7a3IHXhSFwINtY-rf4ITOMmnVmmPw==', start_index=23011)
Annotation(end_index=23118, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtJsbjcautYDgOYd9qUgc0wM3t66tDMwSRFcVor9-8Un2iFxNW1l-hMhfElFWag1MNc7Fuo9o6gl-XWt3TEVMT9hu8iP56S38L64TXqgNXzqVjWts6UXxCf0F4KhwRKEEQwszZd8VEXftqzvVBeatyGHRUPCJaRJTFazY=', start_index=23108)
Annotation(end_index=23194, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRbB8UyfqdurZFK0F0dafpM05e6ljwFXt9CKGJc236iW9dk-_0ezoOe-KjUzMOhZElJ5ae5VLy0jaY-xElq5LuPj_wGzI0JtEV2vBZLvwJEuWSPw0Pow2aMw9T01wLtxTwjb1elOjWSFgFI0Y=', start_index=23184)
Annotation(end_index=23261, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHDPCp6jwVkZaXtiueKmwA8-vW7Dc_UKqAHuX5tMKyVwHd9nmLHYR-uEwTbq1iho-Ld7mEReJ5eKZoi7TSwqzfmjT3LwkKmUUj0mcA02rjqTdJIXqB3i21RQ79cdYQ0QhNDl8Kru7pSclmHPQ=', start_index=23251)
Annotation(end_index=23318, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfYzIS83uJB6G0ohtNHqgQIOJkGnxtESs28iyKzcEHAKr4-y3C4KZ8rkZfwWKzXm2mQmOfP4m4UB0UsKp2RDtnE0d-iEZYEuNDu8KUqS4d6cO51V41lCWqeckcNI5UN4e5sp9qOvlT-scom-q6_M8dMI2P7_bkKc8=', start_index=23308)
Annotation(end_index=23405, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-H7TEpkJtvu0khJuaS3A06BeVfH71nfcP7i6OvWE6z3-WEugk0aRL1SW6OUzRC0VMGf5VTYLUNRbZ2f7L4DDLVU1RD6PY56j6xLSOs_3JQ0NAMa-0sH_y_7E36L-tpjvKNwXGQO_0xCqRBJvspKc9UMId1vCWQBCDk64m', start_index=23392)
Annotation(end_index=23405, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHogUcFDyPpYLOygQUQThL6sSybH09IiQP4LmpEb0IBrDJGmBDmkYkl4YpDLsgOiuk1uyMFTYXZwg7joYCOjFJizKEHLZst35Op8giabTeqw3hf9P9ACGwmXQxluIAt5Ri8NaZo5a3s29i5jlojXfT1S_Vt9PAlLgYEMOW_p-Isrgxq55Jf56m9BP2qCJYZGXee6Gs0Rnd4-hOvdZVWPLaCjurT9yOEA8UaWFZjp-GJOb5ckupPgIl33qzdxDnA76H284AIM3ag-9ACqmSwuQjzYazdyuRxaa2d2As2HVakCnG_GsyC', start_index=23392)
Annotation(end_index=23524, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENcZh0WXmWbHBBLLDo-MZPcu3ipFLbjDQO77xonqWk6gHBzxqDmKWH2oCoxkvohQxeFdWo10zXtoYwt_EAPRefnKpijyUIQRuSU0JOi-pOTaR1LxX29I3pUiLv1zR6iB0eggHn2Uz9Dv4T1YOLV7_6Y-QZBZjNvwPZ-fJ384wJYU_lhdxR_-bub17DXiXcDBLe5LcCUVuMQ2E40PcX6fYLsGbyyTAX3UC6Cq_gI5Fy3sZHxJu9mE1DMRFuLE1VrN-SrI-wmOmW3B_IbpbDJxaRfIOO7kxP', start_index=23510)
Annotation(end_index=23524, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHiTwQ-v46AsHjtRDfaUuOBxxmzSeES2M5W39XS1Ey3734JHKQRLfxhekCHeDab5X9hmxD_ZB0kY3HfKq2c2RAq57OYF3HMw1cvNLl2fZ9dYc_llkln6WEKh3PT7OTDvg==', start_index=23510)
Annotation(end_index=23607, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHKS2RCqP_Dmqiw5nhM0QC-rzAMva0PhusQ1DZUXcvj-mXV0gssdIfBfc4Tw8K3F5GuNkhQz5udtBk9cztIt8wb_vS-2BPvXw46UwBkIcYxAXOeUw4q7SAMpj_sjF6-DPKB_1RJsCdJujpDQhlTNgdkGQMuwxZhQJ8FJODqET2mkeU=', start_index=23598)
Annotation(end_index=23678, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzxlf2nc-zXsgWduj6Frdm6ztQAipwkZApC_MnZeBbuL-6GUvyE3C54GqOsNe3Wdcaizz6W2TW4jZnB50rMkvbvLncyDOzptsOJihGdHRoRmlY-5XKRbE-onkSDklIgB8Sr4kZh-5aaftdAPdDgptJYnciBPYegu4qsCh4HI-71lieWH2NVwFNZaK7FxvIiioDnJnM0IIdDoHFrCB-546fb3k=', start_index=23668)
Annotation(end_index=23784, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3vTAZ7OAmTpDGEUAHbUXH4iVLYFaixxEdYaRZZ3mCdtu3XV1uqQ9qFFxFDyxMQcHzyFWWCOCHLADbNiq4xNHJRooS6z4ynB5JfMgrixX-vcN_cwkTefEX8kHxj3Db71WuI11FJrcPzTjzwJ7H_twh-njpgOvQUr_SILU4XkubhbDODXE33k2kDKeDcUeTi8xN-Nn2YAFFW2ZLyPRqKMEYfj7NnW6qLmRrWAlseZD9lXxHD8xPm3iunq5_hiN3D0w=', start_index=23774)
Annotation(end_index=23913, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8DIieTKdAjCK835Ck6lAX66uxe3vmGThO9204bPVSS0g1MkZ8ta3xQA1Txq32SnD8b9hqd6zkdaXJPGKha3DW5zxS6V8Ijz4Al_J1XFrQxKL1omnaNyMINnGex8oiJDTOiWippKC8DIaEqOTFfyclvxr6MmBMhlh12AyI_0DKBm6ojCO8MnVP-Izp-xedrOOsn4DFE57UHwBFIu4k6-4Ird_nhXIATv-p-4n_uSY=', start_index=23903)
Annotation(end_index=24025, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBu7n5Zmw2MR0jxBBTXuZ-q-I0Aqa-a9cdmBURlnmnNyXe8TEAdezYy0RkPc-QZmxBbY3x92BAnhxYyk8tTjUz-SuXRs-serNpN_eCHaJvpF_WigCFubflHw==', start_index=24015)
Annotation(end_index=24109, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEX_PzxQCiEI06WADlEPmlp_3NTumwsWj0bNkBeUVE42vnVSfqN6gQrmpNBNDjIPu9SG8HtacZkCSxZJOpkCdoUwBBTosmq8VKfKH_pg-iRMtbi9dgdSlO8AXTda1v3HarbB8eYLiWCujcVNW-XXFlKRK9cX-1Iq3R9JTcuiTIy5K8yFKoZcesMBwPaZ9rXBKj2C_yGpBpKAEBY8zZcxLoLYM56l3G06n3Xr5MCA-XLgo8_4Xhh8C_PFC-jCyBJsS9w2SnKqq_dCqufHsCEY7a1ZgInDt_ua1Cgvpys52700cDSKyb38bPUKqBSN3lK5H0=', start_index=24099)
Annotation(end_index=24216, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcoqPrc6h7L9kT_EhrAiU27848UeHXugPY0oR0sTnVvDSgiB0LJXqdgdZomPbWiPhoC7mDlIwCW-zbmIFSz2vNyDIMBmA77a_EbtWrygg12RA3_Wcgi2uBOojpfw==', start_index=24206)
Annotation(end_index=24297, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJKvy46iQXo2Wh98EyzeLrxM0T0HaHDtR0B-RyZ5COnpFXoq7gXUNmjBe2Pz0FiQuftO9a2AOjWJ6mPwCKj_DhacWpj3N9ypSYgssBMmM132yYPcRe04r41gQW4BQUTUt0IEvo2OkvNBXiRYrChoesxfGCZTpsd3Lf2rhUMHQ9vA==', start_index=24287)
Annotation(end_index=24384, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4tqEk9wS2Gk-kiEbOIeCJnFcr-pm7jNo1jAOptaqXRLbVzsWfaSNc4jFDSVmtGl54gmhrsliIWamX2VRON51lwqoIx9hFxSGP8ygRzzvf5KYRRLHh6A5VPBwVMUkxeA==', start_index=24375)
Annotation(end_index=24462, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLIkME6Dn-Oc0m_8u6EykXhr8_nFQ6UGLATWvrMYhuAJRh_HyUPdIS8_gO7Lt_uNeOH1oS4DjhTjvVAmNurZdKCw8V2eXjP3JNARaFSqzBWsxN8WyLd2A4pq9leGQdD6lxmjONoh2t9-ElgtvPu3JdaoVRPg9GS6C9zJcbSAlVOIj9MNzRXYGLr1qQzCcTmDPgT6Ty6WnMBiuN5bttHBEvbdzxVmswBhcSDPJxTv9SXEEYbiI84NCnchFlLkt5a1RqejXhjpda3pWCjpxmUsg_U0A=', start_index=24453)
Annotation(end_index=24552, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKVnsy6ZJVkmw49wlNd3iIPnTy1QMbVkjxGVu59eUbewf1EQ7x9KeUvuRwLkDbw1DFJIA9YtXV0aQIe9q8dT_XcHxWHJvWwkgoDAp39HMi7bCdSm2jG17dYZFxceBcPZk9SoM9cBOsB0mDpEzGRWNfkdjQT1M61Yg=', start_index=24543)
Annotation(end_index=24641, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmWo4mAtyTjyRVeJFx38mTmeD8P4Bp9zcyzobKvUx11ldmBio5XJlDiEg0lSm0_17ypDSjklU0BeXczcNWhd48erg_bZB2Cs3SvdKsvSzqfIiFZiFT_nf4nefvwsxVyC5doqRpbI4caiBm5_Qg7lUIOdM=', start_index=24631)
Annotation(end_index=24759, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRSMZPdzHFLOvzYDLpyj7Kc-mrn4X09_eaIxCiHr1BahDMA-AZsdq-quLzNhKMrNcXCwJgWHHk22E1yADSwG0POFlHvvYvjNg3OmRwIZwqnDnyCXoNHhtzMSyn26IYP4ghKwT8PjoCszzj0cX0y1UFVQXJ_5IPr6ODseDjKLS3D6bms7a3IHXhSFwINtY-rf4ITOMmnVmmPw==', start_index=24750)

## Sources
