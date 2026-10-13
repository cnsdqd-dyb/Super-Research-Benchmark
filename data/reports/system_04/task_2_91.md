# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 774cff6e | **Time:** 259.61s | **Cost:** $1.31991
--------------------------------------------------------------------------------

# Strategic Node Selection in Word-of-Mouth Propagation Networks

### Key Points
*   **Influence Maximization (IM) is the core algorithmic challenge:** The fundamental problem is identifying a set of $k$ seed nodes that maximizes the expected spread of information or adoption across a network, a problem proven to be NP-hard [cite: 1, 2].
*   **Centrality measures serve as primary heuristics:** Marketers utilize metrics such as Degree Centrality (reach), Betweenness Centrality (bridging communities), and Eigenvector Centrality (connection to other influencers) to approximate optimal seed sets [cite: 3, 4, 5].
*   **The "Strong vs. Weak Ties" paradox dictates strategy:** While weak ties (acquaintances) are superior for disseminating novel information across diverse groups, strong ties (close friends) are significantly more effective for driving behavioral adoption and conversion [cite: 6, 7].
*   **Portfolio strategies optimize ROI:** Modern strategies reject a binary choice between "Macro" (high reach) and "Micro" (high engagement) influencers, instead favoring a portfolio approach that balances mass awareness with niche trust [cite: 8].
*   **Graph Neural Networks (GNNs) represent the frontier:** Advanced methods now employ deep learning and GNNs to predict node influence based on topology and attributes, overcoming the computational inefficiency of traditional Monte Carlo simulations [cite: 9, 10].

### Introduction
The selection of marketing nodes—often referred to as seed nodes or influencers—within word-of-mouth (WOM) propagation networks is a complex optimization problem that bridges graph theory, sociology, and consumer psychology. In the digital era, where peer-to-peer communication often supersedes traditional advertising in efficacy, the ability to engineer viral cascades is a critical competitive advantage. The objective is to identify a subset of individuals who, once activated (e.g., through product seeding or incentives), will trigger the largest possible cascade of adoption through the network [cite: 1, 11].

This report provides an exhaustive analysis of the strategies guiding this selection process. It moves from the mathematical foundations of Influence Maximization (IM) and network topology to the application of advanced machine learning techniques, and finally to the strategic deployment of influencer tiers based on product characteristics and campaign goals.

---

## 1. Theoretical Foundations: The Influence Maximization Problem

The academic backbone of marketing node selection is the **Influence Maximization (IM)** problem. First formalized in the context of viral marketing by Kempe, Kleinberg, and Tardos, IM seeks to distinguish the most influential nodes in a social network to maximize the spread of influence [cite: 1, 2].

### 1.1 Mathematical Formulation
Given a social network modeled as a graph $G = (V, E)$, where $V$ represents users and $E$ represents relationships, the goal is to select a seed set $S \subseteq V$ of size $k$ (the budget constraint) such that the expected influence spread $\sigma(S)$ is maximized.

\[ S^* = \underset{S \subseteq V, |S| = k}{\arg\max} \sigma(S) \]

The function $\sigma(S)$ represents the expected number of active nodes at the end of the diffusion process. This problem is NP-hard, meaning that finding the exact optimal solution is computationally intractable for large networks [cite: 2, 12].

### 1.2 Diffusion Models
To calculate $\sigma(S)$, one must assume a model of how influence propagates. Two primary stochastic models dominate the literature:

1.  **Independent Cascade (IC) Model:** When a node $u$ becomes active, it has a single chance to activate each currently inactive neighbor $v$ with a probability $p_{uv}$. If the attempt succeeds, $v$ becomes active in the next time step. This model simulates viral contagion or "chance" encounters [cite: 13, 14].
2.  **Linear Threshold (LT) Model:** A node $v$ becomes active only if the weighted sum of its active neighbors exceeds a specific threshold $\theta_v$. This model captures social pressure and the "tipping point" behavior often seen in the adoption of new technologies or costly products [cite: 2, 14].

### 1.3 Submodularity and the Greedy Algorithm
A critical property of the influence function $\sigma(S)$ in these models is **submodularity** (diminishing returns). Formally, for any sets $S \subseteq T \subseteq V$ and any node $v \notin T$:

\[ \sigma(S \cup \{v\}) - \sigma(S) \ge \sigma(T \cup \{v\}) - \sigma(T) \]

Because of this property, a "greedy" strategy—which iteratively selects the node providing the highest marginal gain—guarantees a solution that is at least $(1 - 1/e) \approx 63\%$ of the optimal solution [cite: 2, 14]. While theoretically sound, the greedy algorithm requires running thousands of Monte Carlo simulations to estimate marginal gains, making it too slow for massive, real-time social networks [cite: 13, 15].

---

## 2. Network Topology and Centrality Measures

Due to the computational cost of the greedy algorithm, marketers and network analysts often rely on **centrality measures**. These are heuristic strategies that select nodes based on their structural position within the network graph rather than simulating propagation dynamics directly [cite: 3, 5].

### 2.1 Degree Centrality (The "Hub" Strategy)
Degree centrality measures the number of direct connections a node has. In directed networks, this is split into in-degree (popularity) and out-degree (gregariousness).
*   **Strategy:** Select nodes with the highest number of followers.
*   **Rationale:** High-degree nodes, or "hubs," have immediate access to a large audience. This is the logic behind celebrity endorsements.
*   **Limitation:** It ignores the network structure beyond the immediate neighborhood. A hub might be connected to a cluster of nodes that are already connected to each other, leading to redundant influence [cite: 3, 4, 16].

### 2.2 Betweenness Centrality (The "Bridge" Strategy)
Betweenness centrality quantifies how often a node acts as a bridge along the shortest path between two other nodes.
*   **Strategy:** Select nodes that connect disparate communities or clusters.
*   **Rationale:** These "brokers" control the flow of information between groups that would otherwise be disconnected. They are critical for diffusing information from a niche group to the wider population [cite: 4, 16, 17].
*   **Application:** Essential for cross-cultural marketing or expanding a product from early adopters to the early majority.

### 2.3 Closeness and Efficiency Centrality
Closeness centrality measures the average length of the shortest paths from a node to all other nodes.
*   **Strategy:** Select nodes that can reach the entire network in the fewest steps.
*   **Rationale:** These nodes are efficient spreaders, ensuring the message disseminates quickly [cite: 4, 18].
*   **Efficiency Centrality:** A refinement that measures the average reciprocal of shortest path lengths, often considered more effective for identifying spreaders in complex networks [cite: 19].

### 2.4 Eigenvector and PageRank Centrality
These measures define a node's importance based on the importance of its neighbors.
*   **Strategy:** Select nodes connected to other influential nodes.
*   **Rationale:** It is not just about *how many* people you know, but *who* you know. A node with fewer connections to high-power nodes may be more influential than a node with many connections to peripheral nodes [cite: 5, 18].

### Table 1: Comparative Analysis of Centrality Strategies

| Centrality Measure | Strategic Focus | Best Use Case | Limitation |
| :--- | :--- | :--- | :--- |
| **Degree** | Immediate Reach | Mass awareness; Simple product launches | Redundancy; Low conversion in high-risk products |
| **Betweenness** | Information Control | Bridging distinct market segments | Can be bypassed by alternative paths |
| **Closeness** | Speed of Diffusion | Time-sensitive campaigns (e.g., flash sales) | Sensitive to network periphery effects |
| **Eigenvector** | Quality of Influence | B2B marketing; High-status luxury goods | Computationally intensive on dynamic graphs |

---

## 3. Advanced Computational Approaches: AI and Graph Neural Networks

The field is currently shifting from static centrality heuristics to dynamic, learning-based approaches. Traditional methods often fail to capture the temporal evolution of networks or the rich attribute data (user interests, demographics) available in modern social media [cite: 9, 10].

### 3.1 Graph Neural Networks (GNNs)
GNNs are deep learning models designed to process data represented as graphs. In the context of viral marketing, GNNs are used to predict the potential influence of a node without running expensive simulations.
*   **Mechanism:** GNNs aggregate information from a node's neighbors to create a "node embedding"—a vector representation of the node's structural role and features.
*   **Application:** Models like **Dynamic Gradient Influencing (DGI)** use GNNs to model adoption probabilities based on both topology and node attributes. They can identify optimal perturbations (changes) to the network or seed sets to maximize spread [cite: 9, 20].
*   **Performance:** Research indicates that GNN-based predictors can achieve up to 90% accuracy in identifying influential nodes while significantly reducing computational overhead compared to traditional simulation methods [cite: 10].

### 3.2 Deep Learning and Regression Frameworks
Recent studies have reframed Influence Maximization as a regression problem.
*   **Methodology:** Algorithms integrate network-level attributes (topology) and centrality metrics into a feature vector. A Convolutional Neural Network (CNN) or GNN is then trained to predict the "influence spread" (label) of a node [cite: 21].
*   **Struc2vec:** This embedding technique is used to capture the structural identity of nodes (e.g., identifying all "hub-like" nodes regardless of their location). These embeddings are fed into regressors to predict influence under models like SIR or IC [cite: 22].

### 3.3 Genetic Algorithms
Genetic algorithms (GA) mimic natural selection to optimize seed sets.
*   **Process:** The algorithm maintains a population of potential seed sets. It iteratively applies "crossover" (combining sets) and "mutation" (swapping nodes) to evolve better solutions.
*   **Hybrid Models:** Recent innovations combine PageRank for initial screening with Genetic Algorithms for optimization, and GNNs for evaluation, creating a robust pipeline for precision marketing [cite: 23].

---

## 4. Sociological Strategies: The Strength of Ties

While algorithms identify *structural* importance, sociological theory guides the *content* and *context* of the selection strategy. The debate centers on the "Strength of Weak Ties" theory proposed by Granovetter versus the efficacy of strong ties for behavioral change.

### 4.1 The Strength of Weak Ties (Information Diffusion)
Weak ties represent acquaintances or distant connections. They often act as "local bridges" between tightly knit clusters.
*   **Strategic Value:** Weak ties are superior for spreading **novel information** (awareness) across the network. Because strong ties (close friends) tend to possess the same information, weak ties provide access to new, non-redundant social circles [cite: 6, 7, 24].
*   **Marketing Application:** When the goal is **Brand Awareness** or global reach, the strategy should prioritize nodes with high Betweenness Centrality—those who connect different groups—even if the emotional bond is weak [cite: 25, 26].

### 4.2 The Strength of Strong Ties (Behavioral Adoption)
Strong ties represent close friends and family. They are characterized by frequent interaction, emotional intensity, and trust.
*   **Strategic Value:** Research refutes the idea that weak ties are always better. For **product adoption** (conversion), strong ties are more effective. The "complex contagion" theory suggests that adopting a new behavior (buying a product) often requires reinforcement from multiple trusted sources [cite: 6, 7].
*   **Marketing Application:** When the goal is **Conversion** or high-involvement product adoption, the strategy should focus on cohesive clusters where nodes have strong mutual connections, facilitating trust and social proof [cite: 6].

---

## 5. Strategic Implementation: Influencer Tiers and Portfolio Management

The theoretical distinction between reach (weak ties/hubs) and trust (strong ties) manifests in the practical selection of influencers. The modern consensus advocates for a **portfolio approach**, diversifying investments across different influencer tiers [cite: 8].

### 5.1 Macro-Influencers (The Awareness Engine)
*   **Definition:** Creators with 100,000 to 1M+ followers.
*   **Role:** They function as network "hubs." They provide massive reach and "social signaling" (prestige).
*   **Metrics:** High impressions, lower engagement rates (typically 1-2%).
*   **Strategy:** Use for top-of-funnel objectives: Brand Awareness, Product Launches, and establishing "cool factor" [cite: 27, 28, 29].

### 5.2 Micro-Influencers (The Conversion Engine)
*   **Definition:** Creators with 10,000 to 100,000 followers.
*   **Role:** They function as trusted peers or domain experts. They hold "strong tie" influence over their audience.
*   **Metrics:** Lower reach, but significantly higher engagement (up to 60% higher than macros) and conversion rates (20% higher).
*   **Strategy:** Use for mid-to-bottom-of-funnel objectives: Trust building, detailed product reviews, and driving direct sales [cite: 8, 30, 31].

### 5.3 The Portfolio Strategy
Rather than selecting a single node type, effective strategies employ a mix:
1.  **Seeding:** Use Macro-influencers to create a "blast" of awareness.
2.  **Sustaining:** Use Micro-influencers to deepen the conversation, provide social proof, and drive specific conversions through trusted recommendations.
3.  **Retargeting:** Use the content generated by Micro-influencers (User Generated Content - UGC) in paid ads to target the audiences of Macro-influencers [cite: 28, 31].

---

## 6. Contextual Factors in Node Selection

The optimal node selection strategy is not static; it depends heavily on the product type and the market environment.

### 6.1 Product Involvement: High vs. Low
*   **Low-Involvement Products (e.g., snacks, toiletries):** These carry low risk.
    *   **Strategy:** Focus on **Hubs** and **Weak Ties**. The goal is simple awareness. If a consumer sees a celebrity with a soda, that is often enough to trigger a low-risk purchase [cite: 32, 33].
*   **High-Involvement Products (e.g., cars, luxury tech):** These carry high financial or social risk.
    *   **Strategy:** Focus on **Strong Ties** and **Micro-Influencers**. Consumers require detailed information and trusted validation before purchasing. A "bridge" node (weak tie) is insufficient to trigger adoption for high-risk items [cite: 32, 34, 35].

### 6.2 Negative Word-of-Mouth and Product Quality
Seeding strategies must account for the risk of negative propagation.
*   **Social Hubs Risk:** While hubs spread positive info fast, they also spread negative info equally fast. If a product is low quality or controversial, seeding to hubs can backfire spectacularly [cite: 36].
*   **Early Adopters vs. Hubs:** Research using agent-based modeling suggests that for new product launches, seeding **Early Adopters** (who may not be the biggest hubs but are open to innovation) often generates higher profit and penetration than seeding social hubs, especially when negative WOM is a possibility [cite: 36].

### 6.3 Target Marketing (Labeled IM)
In real-world scenarios, maximizing influence over the *entire* network is rarely the goal. Marketers target specific demographics.
*   **Labeled Influence Maximization:** This strategy modifies the IM problem to maximize influence only on nodes with specific labels (e.g., "female," "gamer," "aged 18-24").
*   **Algorithm:** Algorithms must weigh the value of a seed node not just by its total reach, but by its proximity and influence probability specifically regarding the target label set [cite: 37, 38, 39].

---

## 7. Conclusion

The strategy for marketing node selection in word-of-mouth networks has evolved from simple heuristics to a sophisticated, multi-dimensional discipline. There is no single "best" node; rather, the optimal selection depends on the specific objective function of the campaign.

1.  **For Maximum Reach:** Select **Hubs** (Degree Centrality) and **Macro-Influencers**. This exploits the "Small World" property of networks to broadcast messages rapidly.
2.  **For Maximum Conversion:** Select **Micro-Influencers** and nodes within cohesive clusters (Strong Ties). This leverages trust and social reinforcement to overcome adoption thresholds.
3.  **For Bridging Markets:** Select **Brokers** (Betweenness Centrality). These nodes are essential for crossing the chasm between early adopters and the mass market.
4.  **For Efficiency:** Employ **GNN-based predictors** to identify these nodes dynamically without the computational cost of simulation.

Ultimately, the most robust strategy is a **hybrid portfolio approach**: leveraging the broad visibility of hubs to seed the message, while simultaneously activating the trusted networks of micro-influencers to nurture adoption, all guided by the rigorous predictive capabilities of modern graph neural networks.

---

### References
[cite: 3] *MDPI, 2023* [cite: 3]
[cite: 18] *IEM Journal, 2022* [cite: 18]
[cite: 4] *Visible Network Labs, 2024* [cite: 4]
[cite: 17] *Medium, 2022* [cite: 17]
[cite: 37] *IEEE, 2011* [cite: 37]
[cite: 1] *ISI, 2024* [cite: 1]
[cite: 40] *ResearchGate, 2022* [cite: 40]
[cite: 13] *Google Research, 2011* [cite: 13]
[cite: 41] *Arxiv, 2023* [cite: 41]
[cite: 42] *HKUST, Technical Report* [cite: 42]
[cite: 6] *Cornell University, 2021* [cite: 6]
[cite: 25] *Murray Dare, Marketing Theory* [cite: 25]
[cite: 43] *Kleos Advisory, 2024* [cite: 43]
[cite: 7] *Cornell University, 2022* [cite: 7]
[cite: 44] *ServerFault, 2011* [cite: 44]
[cite: 45] *Quora, 2024* [cite: 45]
[cite: 46] *Global Knowledge* [cite: 46]
[cite: 12] *ResearchGate, 2019* [cite: 12]
[cite: 47] *PMC, 2022* [cite: 47]
[cite: 9] *Arxiv, 2024* [cite: 9]
[cite: 21] *MDPI, 2024* [cite: 21]
[cite: 20] *OpenReview, 2024* [cite: 20]
[cite: 10] *Arxiv, 2025* [cite: 10]
[cite: 48] *OpenReview, 2018* [cite: 48]
[cite: 49] *PartnerCentric, 2025* [cite: 49]
[cite: 32] *Toronto Metropolitan University* [cite: 32]
[cite: 34] *Medium, 2022* [cite: 34]
[cite: 33] *Washington State University* [cite: 33]
[cite: 50] *BC Campus* [cite: 50]
[cite: 35] *Lumen Learning* [cite: 35]
[cite: 27] *MarketingProfs, 2024* [cite: 27]
[cite: 8] *Impact.com* [cite: 8]
[cite: 28] *Elite Digital Agency, 2025* [cite: 28]
[cite: 30] *Digimind, 2018* [cite: 30]
[cite: 51] *Peer to Peer Marketing, 2025* [cite: 51]
[cite: 52] *PMC, 2018* [cite: 52]
[cite: 36] *ResearchGate, 2018* [cite: 36]
[cite: 53] *AMA, 2019* [cite: 53]
[cite: 11] *Elsevier, 2018* [cite: 11]
[cite: 5] *Wikipedia* [cite: 5]
[cite: 16] *YouTube, 2025* [cite: 16]
[cite: 19] *ResearchGate, 2016* [cite: 19]
[cite: 38] *ResearchGate, 2011* [cite: 38]
[cite: 39] *IEEE, 2011* [cite: 39]
[cite: 2] *Cornell University, 2003* [cite: 2]
[cite: 7] *Cornell University, 2022* [cite: 7]
[cite: 6] *Cornell University, 2021* [cite: 6]
[cite: 26] *Branding Strategy Insider, 2012* [cite: 26]
[cite: 24] *Fizz, 2025* [cite: 24]
[cite: 15] *MDPI, 2022* [cite: 15]
[cite: 29] *SFGate, 2024* [cite: 29]
[cite: 28] *Elite Digital Agency, 2025* [cite: 28]
[cite: 31] *Stack Influence, 2025* [cite: 31]
[cite: 8] *Impact.com* [cite: 8]
[cite: 54] *Saral, 2025* [cite: 54]
[cite: 10] *Arxiv, 2025* [cite: 10]
[cite: 21] *MDPI, 2024* [cite: 21]
[cite: 23] *IEEE, 2025* [cite: 23]
[cite: 14] *GNN Learning* [cite: 14]
[cite: 22] *ResearchGate, 2025* [cite: 22]

**Sources:**
1. [isi.it](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8ft_rg29dzEYh41E9fAf8_cylnXjsO5J_PRXYKVdhokFEalaJ6-UBh5dEVYHjpRqu6xTYMx59JlJ1kjT4sba_8ETF1FeMx10ja4lgat5D0bP6NPkIxYbm8jtYC2UnTfBOk5d6vk8jFNoPUUHs0OXZRjPmgf7P7ftem2BHXJd3LCR-heAELgO-YWX1sAQhoyTnx2_GKhUmTUNH5Z_cIB4Hy2o3)
2. [cornell.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxUI_nBfBa1qX0SowroChHcPptJYlNyQhJSfKAw05GV0BP8s22akrqY_Amw2fQgjtOvvrkQSCCVEUpRSPgFWlr1clnpYYWWB4Dlqp0UxKqH5gdR2lwnNtaRyIiWPdPIuXo6vCQU-5PWzEJETs=)
3. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_Mx4V7sFsig-WP9CAiKQmIskvPeklAJIFCwmS0_88MpKzq8SXAZ3T212qUG-0r0O2YP6WV9BbXPDLcN-S2dyGHA0CDN1MU9sYy7g8AigTSadpGSF9f9kciwBIt4Kaxg==)
4. [visiblenetworklabs.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFX91yBqhrNKgN08jrUwMlLJQ8_2C7CgiuJdvP6gyw9miEtB9NcWPJ8r3tVVST7-qtLCST3D-egCxA0wPC5vsxLfU83fQHdBdjxs7sHMwbpJXMDUthCZuQg_b_I7g_eGjDusL4Y3A2JyihkswrQlgS2hRyHnoLF3G9KaX8b1ronNIQPFdQHoj2wm2mo5bJcXzfXGUo=)
5. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpBP26R79CsIgEAjzpspzDtb1BHmBi7tghmz7TGLfBU2d2KEXEwTmvrgKpPdIC21mUnpp870eeEX6aguwj1NX-5rVlZzKUSzqEXjUL4YPeIPWOrdooS1oLaSIk3kkR)
6. [cornell.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI4vPeILmolzoADTrwIKs1sglU5uI2lWLhFNDX0cF39nVZbmXu7PjMYETtHgnZO5bKvVU-AEmYnPdRpomCw4TDFsV7-Mpve7ixiMlRrbGH7b4b4eHJcoZQ6yRqdIeg3kdwwkiisICIynkXjM6tjISiKQ3Im-13r0rEJ02Ian3z_ecb_rAh8rflRI0b_Gm5)
7. [cornell.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErON8RS17GYA0V89Yy2xK4B_2JJ5i3T28d4MWZx4PWHGfJJMqtvcm0tQ-rF8IE3SS8yWt8-fTdA-C8f0WzbZFAlteatcGo9E0DqzwijbYa_AmPQfLW6V9VypJRRhAjj20eTBX3_GoOV9qDpkbKrsOFSc_l10eIYDovFSqAe989ktZT1tE0H3Gq405LxPLJD8qe1Dhx5MHr)
8. [impact.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_2LpqRXLqHUgim8Y8gfdII2SidKXlgflUXMQMDGWZQYvBPvkasSZnOB1lK4vwX9lIIe5v44sOEwCGseplNmP9yS3t1shtBuSb6Dq9rMzWBWiO8S8kJ-vivu-eQ26JX_BUCzmO-icischCUBvF7ok=)
9. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4m7YaMp8vkspFJB2aRT7T3mPHwVSQTqAmlRRk8gr67JIxC4tQbN0jRYhVow9sqYpALNjCFkzVY9zLhS9Q_MmcisNZdW6qzxGrfsUYMml1IGDAXJXk3w==)
10. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJllGj0D-cUurKBADv_Yqd2nOoNFPg-T8m_IysO858P0degoSjzzcDjnGOmywaNvkJ-SElhvnW2uEGZz-MA-QKX_h8SA_wPHjKJX_uG0zI5QgsB8RN6w==)
11. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGmymSANrjFOpodcoUAUC530UXpJwhFBG4wmYm-kkOHZrKGD2RIcL0Vzj_Sz_5LliW6D9oovrmPOx1Qe80AHRL6AkV-YasKdGczFqpYJPU1LyK51xPVij5f_AZn4jATddUlv7dIjydqprmn4BwrZ63)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3_SKEt0m7PYn4tBXWgcVrqM8aBDcW-cgnAdoUdPmlqkjwUVGPc22smUgbcmNG7nRa1zCsaonC16ELhwElvAU2xf7AfamgRXBdr2CYHkdcIg2Yeg_ePkIf5pvEcLRBWmcJ_mQgWXeyH82QjTd6RaDMlMVOYGdsfCI6K4gAu_3QDkSyKgSPVgy10HsTgrwDLpMXTf4WpHKj)
13. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEGw6jIF8OkWQb0R18itqt2zHG24H49bW6XxJbOSGH490oAahCIsZ9uJzDAQDLV0CPTdeTxFSsKtybXMXEJBDaUhnP-KOPJ47fQTMCW7Fph1hiVa8SC8EETrQ9yygc_Axj9vqblABSiA==)
14. [readthedocs.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ1UoPZ0kvsakR0YIffiCXZSjxLZwTmrF-KAcEF3_3m2b1WYC3IvQjkNj5A8GLRLgKyFcxN_tUyh2nBf7IeCZ13w4hEsUEdd-hMgbOD_BKt3bpWwcfpfPymnEtRBVF9nfTOFsCAjxixhmlU5cd0LlVNfgeV2C74bRPjMZfBbXSAg==)
15. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZZmu6loHVSVKK2myw8jBdSuhfh78SE306OIgmhKC4i99QxdYMrt5TL69c1RvfSFs9tycfT2IbSkuuKpXLOIw9R3u-GH5nlsQMakQQ3ANRaJb2hxfanapIfcfmd6g=)
16. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH98BdbcFU1U4DGRiRzlPxIsjKJjYVFBA8aTt4z-W7OeIQbiAp7ta7Cv5nXlZBh2-m57koOdvMEHISevLjTX5KCjhKFQ0_7QBf5N3tN7BAIzqMaY4rC1tC-CpB0_iStwGmV)
17. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkBYTIiEkuSSMi0nsJMMUig1O9o-BlE2wztgUVuN1TyZDZY8C3zIkqxYGTWbmZV0S2j6JF1w336rTTYaaMyLuAdMlep5h6PUTCHpbpO1jZPvttKrpZjNkxX4HWwbQ2KrkX0oyvWT8Pus6xVaDASAIl7FotOoMzhk44KpyrYpjprgim_u9DipTWj1Z8xUa7yQiLwWtmZ_TBys12eNJTw0eHV2Kn_9Co_6e57wt1-dyXN-IDQFvtM5yrPJGy)
18. [iemjournal.com.my](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5ZYVT1Ve2RGL89sL7kF28A4Kjv-t14eLAtenU68zzEntGYastFseY2Sh8F8-CCHB1rw3JCT-FutWoEA5IUnqCyJ2A2pGGpJKGoM1ZdJUI1StUjOcAc6gopvcP1KAmx-qw6u9WtAz9JHtWz4_D9U_S8P2q-p0=)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsRB8VLHvGNvTAdCcUth0RMTclURM-K-2biisvQ4kx2NN-apVeBINxp5Uybb0QBxVrsJZ1asn8ETe-hA1vEjXcYONYyNrNyqkaERjIBKCMNwX3wjYeWrNrWrf-y68pZ44v6pxHkG6Lv6MsqUfAFH1ILoXwPKIRAPrmO4RZIiwdOLfUNDIS2Fr2jsXhHsQPTs-Jt4h0Fgjztrp3Zuzrz2BjF6QNjtllJ4JPx12nPQ==)
20. [openreview.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpnvvPJOX7DODE-RKiZlSDf-A4VSIpaPSFE1wQrzSxRj7J4eYSgJxo-0viMCL3Wi9GDrQMezzB3-SwguJilgKsSszz6Kveasqf6nIeyxroENzt7YKgng9qSgowpwxTwx2chtSKcgli5XzeOClQysMIm1x98pSvhgkda_E9hA==)
21. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjcRDGMaoFw7jJPqLmMbVss-dAFgN0lbo1RzkERl9aZQQ3uR9IYQr4SfqF9OenckwEpyRhDwnqMNCEM2-2xYyY-qa2XEziYnSvd6H48E0FlXxEfBpVsRM8cpXJHwXaKQ==)
22. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtru73R8JMYVlFkj2QUhjBXy4LNS4MVxL3hYjyd9PQ6xmM07Mxsz4VzN6N_IAIneYVzbOtsFiEtW6-sKphtMjR2sDRk2M7amZC6vZ5DWelsoFjsSCU4NGrnixdbB88FH0VwuzYIUQuZenXROSSAgHeOFQSF3nrshaXQWcZ_s5l9sBB9eiWVB0M-RARMgFXPmRUR3K_zrm6K4b3BDOP46grPLI7fBDeihjRAWkdnrgtPb9vzox_bOSpexeUy2E94EgLHw==)
23. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtFqlknLJQJcLuBj5OdKdqedTvuIR--3wfi-AhODtjgmQFyE7eIhqj0tEzcnId7gvvQGQOwmRiOtAUDRPGMPmCsbXCMvoVrNGnLEj11ofUm3hUERv5HuuOBHnoAwpR8Lg2gwgm)
24. [fizz.co.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2a5r7sHtuegEy67qe-HZ8RS9uP4bHAztFDkhjyR9Hs4NzIFoj4k4uX-Mc9UXfEZ5MadeAhBfVDIyOVAICB79awru_eYEx8ffSik_TWzW1D4Jmk7NDdjRA9p2KGdwdiE55KL2x3CDl9V0tufZARzuaZRImHHsC334syXs=)
25. [murraydare.co.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZjWFM8QXGmPuw9fW_g0BJn-w8rynPCA5fq04p0IDU6rooDcCHVNC-b-8ijDntS7l-LNtJjnekvFJihsJlkMPpQuDEoiQfAoKC_HVQt88m6Gx7My42SeJBzFn3wJWCJuMtT0lottDNyGYRvuGvxT2X)
26. [brandingstrategyinsider.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNeNsPQ6L4JgI6nBw3DMZSfXBCM2taHIzSg1FvtcD2EMHJeYiVkWxr96mZrUPLSeVNahg1tMH4Y6E48gEFPmBan2b4CChnzX4UWynwggJQUOBeGOxcL9b8DBc535ScH3cGgQKrLqYLsyJWzx4Q6VuCs21VLtRkphqBYLcINsPfeMBz6OKmkRSje64=)
27. [marketingprofs.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUGE14oIBIAlGdPCkmV2Bn-Ug2SHj0HVorIGNQH8RwM0GMnrZ_V8uIW-dsssCIp2zWXWfSdR9pV471xuAuditx0vZjXRck27HEobgqIB2zjrrP2TwTIhf5neNJnnqz7Pg-PctQ6P9EBhtmCUq0mR_VvfDKl9e8OoorDqhFvO9HoJfLHXSQSh1L4Oe4C6MDJaLSyCrcoXGptxi_---zvw==)
28. [elitedigitalagency.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHb2GPhpwsZyoJVJ7Vd7ne1VX17-SVUkzAHnRBF_4gfidcy_xVmjXejLusEXvlKDZd-1l8fqr7FWiZRDXsC-uK2qG3Nm3kNZmwkAPXycySzyNhki-Jdxx2ECufpi5CZv3SfGouYYsxd7-Y_CTN8rSM_1pkDaj2C4kevX4iYM1lf1cdwEKiiczVMt9vfKbIg2GeRVt3i8A==)
29. [sfgate.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdXecv_PBzWIloUe6bSeMoPY16WAEKEbiEYH0KYZHvgGkEoCZtz0jvFvqF07jqKky4NEi_OIDFKSGeQ2CLfb9ihyKVu8KyhULH6hBrYbJU4Ly9LuH8Ga5eClvEyx3BcCS7oVO09bgmHZcVTWpKdv_Lwu4=)
30. [digimind.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKY7x-j-H2NN-5J-Vp_c1fzxrcm_nfIZW8UXIiHWL35bYy_ijKgXuF9JZC3SgUSRUXuzpkUdhI66kRrbEez92cLQSoKR09uwtUW3qy2yYBPdhdC0xMLc4BYxLM4-22YdNSQciPtjbB2Ed_dRxHXiakT3SiaYLDriTHn8YhxwE_BmeYKI4CPGG-8H-Ppz1xf_rKr5NnuEbAXhMa-3ZT7laePRKq)
31. [stackinfluence.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXysyhW4XoMaH9zlJ19srk2il3EHfBaHFaelt8RkTh5_PJJLc1DQGbUpLLqSFokdSTXSggWeN2pqj8dWl7eXfndf6TT1Y-OYig1Nq81YAqhdzl5jXUqOobKLb7grRhrBvzCICeH-5idpYgZl7QVFWUSvEq3CXRm4xpEUUmD1ja)
32. [torontomu.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEXImDiWGmRZEXvLA85_VGaXRssM6k0bfDgfzgUHJaVwKRju6JzHzh70DNLynjClH1MYl58LrekPAuYou8tbLLj1eAFFUvG4SGSbQ2jhX9NzAEVXdxLi6RW1e4xK4Q1MZtn3u0Wa5ECnOXly1_ddD2ymrkijwW-L-5OxOj1qFKii9g1pLCq9Jou4LqJR7jvr1h0_O1utL3eg9UNCtACJOEhkq9JzxLBr8eaANh3g==)
33. [wsu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9e74ixhfBs-ZQAh7BvMqoVvmTPOGZxFPHVihmY2uBIMwK6MBkFyDOYGnrQKjVkcQAxNbnnoi2czWAnRUqdKolOsNuNP8DwucU6PXuCkGeA3WWCh0wEbKuFhXI5W8Xi6_c9Kn4BXMjzzpzpKMfuUhsIGGBnm9EU3_V4JZCwgMkcadVM4xfJdY1c1V7BLLH2xbH_1DnltyV0rlSvZD6V6K9dIv8F-EHubKpLFNkVHZmzffdHLks10OADDxZ0yAFYVIbYSLN2E0_)
34. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQpLbD6fys-6Wi6eW8fLvcAyetjjaueirsb5YmHI81uNYGrvH0T390Fss5yrmPQV1f_OVQfvFEvGwxybf69x0hbt_AoEWjzZcwRKDD1t3o9oXloYKXdVPiGmq0YmrFH_vYldkEUsTzzRnBwgEyNZ1WyOakQL40hlQMvz519rOaVosgFo1W8l5IsMgHiMDR_6enrRO5q8S5LTqSks8wWuWbzUU5xADzJ1kS_A9RrV48KlJIMh-ff8tJRBA=)
35. [lumenlearning.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVTNnCnCzZwKJrvaqZsm1zSK5LKlr60YdGmvdgqfKE6GEnGMfWX3rpau9DK1s-_cfwe50L_6-uO62U9H3D1_pBDEqEVz2IpYs1fCuGfCz-nh3HiakoEnDSbKPCl8Ov0P2eb9HI3p4_YQzCE-1cGssdtwIojenfJYVkOQna-esxABTmtL3PQVr8UtBjpjo-ldpMTyBkBdtrVsCO7kmApx8Nhi5zaTFeZWA=)
36. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-sILSyQSytnHAXFa9Zs2hS44MJsNC3t7Qyg90qZI7SKYmUxTCUC3bIlYfegovuQnGcXeuAv8D3gCg3-_jp8Y3KudWftvGXbgunQrk_EoTldx3KrunTzwFS2GIe9rUSnCeCSyDsDBwypqdIyOh26AfD8Xemoak3EVjqALn7nABglgsbFE4-niGAXg-84491fvkF8kN0xxKLRAlXB5wOuSGuca951avPosBFXdczJ5_dP8G9gxo)
37. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPOE2UMFcxHZ5k8bhGVc5FfjldAA3aUMw8Ym2_VaXvI8ICYPqZMzFr8k8Wb4KkL_cr-DIX_EpvztEDEnG6PrB4Bycd5zL6Y4GPZ_JeAezmwO2Q-mFZ7CY0M5bzjc4IGRjKwPw=)
38. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYM49SfP2g9MN44BBGujpZekgf24U1NwQpbfKFoJXGj467mysQ8Puz6lhNMtuTPU2oSx3p0MuQirj7YNKEeHHglWRYPzETzX3TxHpIgs2914-vcf2h6pFyEmL-w1brYatNsLfV_TRAf0ubNjTvJb_tkqqQjLcxLMB04p7Rs3Qj2G48qLimyNXZfu39qnSK80e0f7fyiTYW-7yWFX0lFRzjC8I0tzMlOTVYayde3o_J)
39. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkjYnIbzWbyHlWn_9Br8HZ1Bvl5yQ15nyzIGv22SaXjNNkjiyiSa9JqU07eh0UGXDbobFHUS1riEss_LXOK8LvpAO35NnPHoACS6bAqN3anhCuOxjeUwwHssDhrrVava2CFhwn6KoPfbsJl1wPko1pVUVY)
40. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVkHYiAijGKgwCyq7WcH0M92aCk5uDRYCkWAI6v5YwBdn0q47jkASPRnBOeWDo7YaeXrWPbIg-f9xUw3WhnOLCuBx59HHfFrofUD8d8AQ07k4oSXMgbRyKnBDaru-Kz9LFUDZvN50CgZz2nIbFD4SHJm6j-xvfbl2tMXgAHCghOpC7CyxmS8wU8yltjcf4-sZR-ojJWSXLziIRVk__A-03qq2h6ps0OnxIwJyClrdVHyQB)
41. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzJAUWSRQ9ERKV6-zVf3elVum7wNnDH-0oU3NOZuPnLk8aNc-k6_n2Kw5mMbzizQyLefEWtT3utT6e9CZN2DADumfZDbeVOYas6MISYB4y3STb0oEQ1A==)
42. [hkust.edu.hk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHn-tVWDmTS1BMhCM9ZEVEqZDXsLDofInUQ4Ah1p35qyD6GD8dgmGkLy6mnigdeX97eImwKw7AyXgZ2RRUWo28ZmXQIF5sEmCFHO-EPc9rvKchJ0DWrP9sNEYqHuSoBEs75sYHj9uDU6EJgVvjdwVW8r-s0vBZ5)
43. [kleosadvisory.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErBW4uVd_NBTpuDcWBbA7cWJjBEMAAAOYmw_TkjEik3hLo3Cal_twrUub54CioxZbolRkL2J7X-I5eTxRkF6FkLzK1KareRbwq_zKWAZssufKs-WtSEUpgjL7XcgTzaNHA0yTSLjLIPM-zXCm-z3Kb9dErbnoU6IBaV0O48CBNMAf8BHP8hFXAyMgraRIeQ9_OT2cEad71tDw=)
44. [serverfault.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfALZQBzroVhToedH1XZGs0e-5EoifLDEyI8-Ic7IInDNAQvw9wvPjx6jIpA6gvLED1N4sg1xSn-L60hpsJkK--j6wbz8-3e622bXiQdT5DTH_AbGh1keQP93M2Nrr1S1mYFkm_DMbTRE2FrG80qoIFIcH_M4qaS_7PMNI1t8IbPRAwlk=)
45. [quora.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6dpXbhdrBDNvXWXiBcGjRjnPSg5NJfs_2SBA2Xl0X35Vf6lv_OjO-1oRgo0R7tJJmz605NO8Xxkf5GAhpWyF8HwSO1xcwpXSjMgK6ZN0MxCZSrljpgMjdK54XHZgUWtl6EzOEghc-yIj2B-mG7k59MGKQgwFhA0acr-M020fv7vn1RPLw7rYOjx0fy1_j4_4GSINcDiKMFX5XMtT2j7Cpo5xQ3V6MOidQShk8YBp_HJk6LXgEMDiuV7agCcM=)
46. [globalknowledge.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5NXWHgGs_1Esd2ZXQON3EnIAPX5Qaz50qWI3zDGTLmepXJDZcDbpiX2P98BgD9b64Ho_Ics2xYU_h15Hr1446nIaEQvIhwhPtqqAEbqW5cIE371b0OxAHmLGrDzFddQNFLcq8gb4IwjQHj-nv5HJlP6npA3__LvdEE0cbArLM-a-RydFVmdR8zlhlaRpUR-w3WOdXHciFnpvYTaEXbCwwNsf3U3srDbBkN6g-G7Zumz0_NRc=)
47. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlpAriAv5Xf1X1YIkCLXCXMKymtwzjxaDSM91bGKN6Lp1oWupz7F1Bu-kwCoGSXmCmeRz3h3PaXzJydrE7fUgggFNitZAhm07_rLRaBjUvsj_k2rm_UlVdUUKJgbhMSSy-zjsAP0Ms)
48. [openreview.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTuXjeOl3henv6D-ChZyibbJnHHwbiPnJ8Fk0cFvbOdz3o3ybgemOwQ1D_XHUI3_p1R5EdgMnRqI_mu6Q-Hm4Aigh2AFko8b06pJ-dTgW22Q96c4J88xM9lqmSRTZDctptj8EFhlZB2odYkIzl3fERpNnXE4eqFtxaxEEdnA==)
49. [partnercentric.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEh0TTmLcbdlGUYxD62rWelU1ihp6wZeOIMrmjGVQquaek8v4FC8XQyRzUv0TCHe3RQ-vQeGnrshLLq4kYGfycbKXXlocSiKjXVpdsHZWIUEjmcQ1ukbhnX3NtFp9QLWl757ryUoUdpwcgqbh5Q4So9lrkL0Nj3URabKLa3krN7aw==)
50. [opentextbc.ca](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBevmDxJKsMmN5YRzqhVRd8wW1fc8JG7ifXesbyeeVfVBm7bAflES3yJYsj_IRrYKvrDZFNSCaP-CkI1To_RKXABKVbN0aN_KA3nzPtfij06tgfUIhO9BwASNwS1ihUJ9hlBVuZ0BPBbz44U50rQB7QIcpdLo-mbIvj96JNGgnQLZ5BxBwPp2sU40WX2QwkcSuGVDO_b4LKDQaupRbSuq8cSQniOXfZcVBW5nnUDLonlw6EDqlRCcOv81-oro5PLNXYqhi8OS5_u-lm3G-m_zoig==)
51. [peertopeermarketing.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8QXmehkekI5n0v8iQsGkiTI17Y3K7M9F2eyk9U9jMNm2ix_x0AjM8H-GW3Wg2TMjJYEemPNts_K0JjekK6OZUQWMAB5qnJWp-sCqYcq-07W6q3p8d0f98QosY7IIL09K49TSyO5dyjN9FCf8dcfB1)
52. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOATNpK1OmMqcqBjSr2OdHdKpMZZAZcC1qQQzy_x1wyeBTmnNH52RywZTYJ-91dtJmqH_yI-Wn5--ecUV0A3vfJg3Pj6K3HLKi6-YnzvuJULcU7eCu-Pa9aEvesFFapp39ZSXuL3_S)
53. [ama.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4RfB39vRahif7QxH4eNQifyuYyIU-JLMRhhqfE4W_IdHZVVf2rFNjYh6xElWzXnmE4qyVN_8_8xZ35UDv6rB_qN6eIFWIpZ3RVq27iWSNxF3k4sfaWECX4rGCKe7KBmMaBbLC2VBbMLHUNvCF-Id0t7bRG34YsEk9C7dFcvGqAxjOWg_9hy0j1Z017EKJ5qgJJoBwt-QAYZq9)
54. [getsaral.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFy1Y4-Hr5WdLOgQg0d6uS54rlXRXZDFDSDe8OAINoa0sL_0Ui4U3xA5pMmpHQV7DI3gUgiMeunxEZapxkVMAlDbE3tjX-LqfY2xb3e8g4_HKjKTOPnL8Xse5kX_eRzo-iooI0avHKM3Xku8zxGHI_otyihxWZTUs090-yA8E2-4WDFLFyIBLYXN3sNt9O3uPINnO1ak0AyBA101A==)


## Annotations
Annotation(end_index=338, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8ft_rg29dzEYh41E9fAf8_cylnXjsO5J_PRXYKVdhokFEalaJ6-UBh5dEVYHjpRqu6xTYMx59JlJ1kjT4sba_8ETF1FeMx10ja4lgat5D0bP6NPkIxYbm8jtYC2UnTfBOk5d6vk8jFNoPUUHs0OXZRjPmgf7P7ftem2BHXJd3LCR-heAELgO-YWX1sAQhoyTnx2_GKhUmTUNH5Z_cIB4Hy2o3', start_index=326)
Annotation(end_index=338, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxUI_nBfBa1qX0SowroChHcPptJYlNyQhJSfKAw05GV0BP8s22akrqY_Amw2fQgjtOvvrkQSCCVEUpRSPgFWlr1clnpYYWWB4Dlqp0UxKqH5gdR2lwnNtaRyIiWPdPIuXo6vCQU-5PWzEJETs=', start_index=326)
Annotation(end_index=614, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFX91yBqhrNKgN08jrUwMlLJQ8_2C7CgiuJdvP6gyw9miEtB9NcWPJ8r3tVVST7-qtLCST3D-egCxA0wPC5vsxLfU83fQHdBdjxs7sHMwbpJXMDUthCZuQg_b_I7g_eGjDusL4Y3A2JyihkswrQlgS2hRyHnoLF3G9KaX8b1ronNIQPFdQHoj2wm2mo5bJcXzfXGUo=', start_index=599)
Annotation(end_index=614, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_Mx4V7sFsig-WP9CAiKQmIskvPeklAJIFCwmS0_88MpKzq8SXAZ3T212qUG-0r0O2YP6WV9BbXPDLcN-S2dyGHA0CDN1MU9sYy7g8AigTSadpGSF9f9kciwBIt4Kaxg==', start_index=599)
Annotation(end_index=614, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpBP26R79CsIgEAjzpspzDtb1BHmBi7tghmz7TGLfBU2d2KEXEwTmvrgKpPdIC21mUnpp870eeEX6aguwj1NX-5rVlZzKUSzqEXjUL4YPeIPWOrdooS1oLaSIk3kkR', start_index=599)
Annotation(end_index=902, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI4vPeILmolzoADTrwIKs1sglU5uI2lWLhFNDX0cF39nVZbmXu7PjMYETtHgnZO5bKvVU-AEmYnPdRpomCw4TDFsV7-Mpve7ixiMlRrbGH7b4b4eHJcoZQ6yRqdIeg3kdwwkiisICIynkXjM6tjISiKQ3Im-13r0rEJ02Ian3z_ecb_rAh8rflRI0b_Gm5', start_index=890)
Annotation(end_index=902, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErON8RS17GYA0V89Yy2xK4B_2JJ5i3T28d4MWZx4PWHGfJJMqtvcm0tQ-rF8IE3SS8yWt8-fTdA-C8f0WzbZFAlteatcGo9E0DqzwijbYa_AmPQfLW6V9VypJRRhAjj20eTBX3_GoOV9qDpkbKrsOFSc_l10eIYDovFSqAe989ktZT1tE0H3Gq405LxPLJD8qe1Dhx5MHr', start_index=890)
Annotation(end_index=1153, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_2LpqRXLqHUgim8Y8gfdII2SidKXlgflUXMQMDGWZQYvBPvkasSZnOB1lK4vwX9lIIe5v44sOEwCGseplNmP9yS3t1shtBuSb6Dq9rMzWBWiO8S8kJ-vivu-eQ26JX_BUCzmO-icischCUBvF7ok=', start_index=1144)
Annotation(end_index=1421, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJllGj0D-cUurKBADv_Yqd2nOoNFPg-T8m_IysO858P0degoSjzzcDjnGOmywaNvkJ-SElhvnW2uEGZz-MA-QKX_h8SA_wPHjKJX_uG0zI5QgsB8RN6w==', start_index=1408)
Annotation(end_index=1421, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4m7YaMp8vkspFJB2aRT7T3mPHwVSQTqAmlRRk8gr67JIxC4tQbN0jRYhVow9sqYpALNjCFkzVY9zLhS9Q_MmcisNZdW6qzxGrfsUYMml1IGDAXJXk3w==', start_index=1408)
Annotation(end_index=2060, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8ft_rg29dzEYh41E9fAf8_cylnXjsO5J_PRXYKVdhokFEalaJ6-UBh5dEVYHjpRqu6xTYMx59JlJ1kjT4sba_8ETF1FeMx10ja4lgat5D0bP6NPkIxYbm8jtYC2UnTfBOk5d6vk8jFNoPUUHs0OXZRjPmgf7P7ftem2BHXJd3LCR-heAELgO-YWX1sAQhoyTnx2_GKhUmTUNH5Z_cIB4Hy2o3', start_index=2047)
Annotation(end_index=2060, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGmymSANrjFOpodcoUAUC530UXpJwhFBG4wmYm-kkOHZrKGD2RIcL0Vzj_Sz_5LliW6D9oovrmPOx1Qe80AHRL6AkV-YasKdGczFqpYJPU1LyK51xPVij5f_AZn4jATddUlv7dIjydqprmn4BwrZ63', start_index=2047)
Annotation(end_index=2799, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8ft_rg29dzEYh41E9fAf8_cylnXjsO5J_PRXYKVdhokFEalaJ6-UBh5dEVYHjpRqu6xTYMx59JlJ1kjT4sba_8ETF1FeMx10ja4lgat5D0bP6NPkIxYbm8jtYC2UnTfBOk5d6vk8jFNoPUUHs0OXZRjPmgf7P7ftem2BHXJd3LCR-heAELgO-YWX1sAQhoyTnx2_GKhUmTUNH5Z_cIB4Hy2o3', start_index=2787)
Annotation(end_index=2799, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxUI_nBfBa1qX0SowroChHcPptJYlNyQhJSfKAw05GV0BP8s22akrqY_Amw2fQgjtOvvrkQSCCVEUpRSPgFWlr1clnpYYWWB4Dlqp0UxKqH5gdR2lwnNtaRyIiWPdPIuXo6vCQU-5PWzEJETs=', start_index=2787)
Annotation(end_index=3416, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3_SKEt0m7PYn4tBXWgcVrqM8aBDcW-cgnAdoUdPmlqkjwUVGPc22smUgbcmNG7nRa1zCsaonC16ELhwElvAU2xf7AfamgRXBdr2CYHkdcIg2Yeg_ePkIf5pvEcLRBWmcJ_mQgWXeyH82QjTd6RaDMlMVOYGdsfCI6K4gAu_3QDkSyKgSPVgy10HsTgrwDLpMXTf4WpHKj', start_index=3403)
Annotation(end_index=3416, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxUI_nBfBa1qX0SowroChHcPptJYlNyQhJSfKAw05GV0BP8s22akrqY_Amw2fQgjtOvvrkQSCCVEUpRSPgFWlr1clnpYYWWB4Dlqp0UxKqH5gdR2lwnNtaRyIiWPdPIuXo6vCQU-5PWzEJETs=', start_index=3403)
Annotation(end_index=3893, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEGw6jIF8OkWQb0R18itqt2zHG24H49bW6XxJbOSGH490oAahCIsZ9uJzDAQDLV0CPTdeTxFSsKtybXMXEJBDaUhnP-KOPJ47fQTMCW7Fph1hiVa8SC8EETrQ9yygc_Axj9vqblABSiA==', start_index=3879)
Annotation(end_index=3893, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ1UoPZ0kvsakR0YIffiCXZSjxLZwTmrF-KAcEF3_3m2b1WYC3IvQjkNj5A8GLRLgKyFcxN_tUyh2nBf7IeCZ13w4hEsUEdd-hMgbOD_BKt3bpWwcfpfPymnEtRBVF9nfTOFsCAjxixhmlU5cd0LlVNfgeV2C74bRPjMZfBbXSAg==', start_index=3879)
Annotation(end_index=4196, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ1UoPZ0kvsakR0YIffiCXZSjxLZwTmrF-KAcEF3_3m2b1WYC3IvQjkNj5A8GLRLgKyFcxN_tUyh2nBf7IeCZ13w4hEsUEdd-hMgbOD_BKt3bpWwcfpfPymnEtRBVF9nfTOFsCAjxixhmlU5cd0LlVNfgeV2C74bRPjMZfBbXSAg==', start_index=4183)
Annotation(end_index=4196, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxUI_nBfBa1qX0SowroChHcPptJYlNyQhJSfKAw05GV0BP8s22akrqY_Amw2fQgjtOvvrkQSCCVEUpRSPgFWlr1clnpYYWWB4Dlqp0UxKqH5gdR2lwnNtaRyIiWPdPIuXo6vCQU-5PWzEJETs=', start_index=4183)
Annotation(end_index=4742, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ1UoPZ0kvsakR0YIffiCXZSjxLZwTmrF-KAcEF3_3m2b1WYC3IvQjkNj5A8GLRLgKyFcxN_tUyh2nBf7IeCZ13w4hEsUEdd-hMgbOD_BKt3bpWwcfpfPymnEtRBVF9nfTOFsCAjxixhmlU5cd0LlVNfgeV2C74bRPjMZfBbXSAg==', start_index=4729)
Annotation(end_index=4742, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxUI_nBfBa1qX0SowroChHcPptJYlNyQhJSfKAw05GV0BP8s22akrqY_Amw2fQgjtOvvrkQSCCVEUpRSPgFWlr1clnpYYWWB4Dlqp0UxKqH5gdR2lwnNtaRyIiWPdPIuXo6vCQU-5PWzEJETs=', start_index=4729)
Annotation(end_index=4946, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZZmu6loHVSVKK2myw8jBdSuhfh78SE306OIgmhKC4i99QxdYMrt5TL69c1RvfSFs9tycfT2IbSkuuKpXLOIw9R3u-GH5nlsQMakQQ3ANRaJb2hxfanapIfcfmd6g=', start_index=4932)
Annotation(end_index=4946, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEGw6jIF8OkWQb0R18itqt2zHG24H49bW6XxJbOSGH490oAahCIsZ9uJzDAQDLV0CPTdeTxFSsKtybXMXEJBDaUhnP-KOPJ47fQTMCW7Fph1hiVa8SC8EETrQ9yygc_Axj9vqblABSiA==', start_index=4932)
Annotation(end_index=5301, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_Mx4V7sFsig-WP9CAiKQmIskvPeklAJIFCwmS0_88MpKzq8SXAZ3T212qUG-0r0O2YP6WV9BbXPDLcN-S2dyGHA0CDN1MU9sYy7g8AigTSadpGSF9f9kciwBIt4Kaxg==', start_index=5289)
Annotation(end_index=5301, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpBP26R79CsIgEAjzpspzDtb1BHmBi7tghmz7TGLfBU2d2KEXEwTmvrgKpPdIC21mUnpp870eeEX6aguwj1NX-5rVlZzKUSzqEXjUL4YPeIPWOrdooS1oLaSIk3kkR', start_index=5289)
Annotation(end_index=5954, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFX91yBqhrNKgN08jrUwMlLJQ8_2C7CgiuJdvP6gyw9miEtB9NcWPJ8r3tVVST7-qtLCST3D-egCxA0wPC5vsxLfU83fQHdBdjxs7sHMwbpJXMDUthCZuQg_b_I7g_eGjDusL4Y3A2JyihkswrQlgS2hRyHnoLF3G9KaX8b1ronNIQPFdQHoj2wm2mo5bJcXzfXGUo=', start_index=5938)
Annotation(end_index=5954, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_Mx4V7sFsig-WP9CAiKQmIskvPeklAJIFCwmS0_88MpKzq8SXAZ3T212qUG-0r0O2YP6WV9BbXPDLcN-S2dyGHA0CDN1MU9sYy7g8AigTSadpGSF9f9kciwBIt4Kaxg==', start_index=5938)
Annotation(end_index=5954, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH98BdbcFU1U4DGRiRzlPxIsjKJjYVFBA8aTt4z-W7OeIQbiAp7ta7Cv5nXlZBh2-m57koOdvMEHISevLjTX5KCjhKFQ0_7QBf5N3tN7BAIzqMaY4rC1tC-CpB0_iStwGmV', start_index=5938)
Annotation(end_index=6432, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFX91yBqhrNKgN08jrUwMlLJQ8_2C7CgiuJdvP6gyw9miEtB9NcWPJ8r3tVVST7-qtLCST3D-egCxA0wPC5vsxLfU83fQHdBdjxs7sHMwbpJXMDUthCZuQg_b_I7g_eGjDusL4Y3A2JyihkswrQlgS2hRyHnoLF3G9KaX8b1ronNIQPFdQHoj2wm2mo5bJcXzfXGUo=', start_index=6415)
Annotation(end_index=6432, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkBYTIiEkuSSMi0nsJMMUig1O9o-BlE2wztgUVuN1TyZDZY8C3zIkqxYGTWbmZV0S2j6JF1w336rTTYaaMyLuAdMlep5h6PUTCHpbpO1jZPvttKrpZjNkxX4HWwbQ2KrkX0oyvWT8Pus6xVaDASAIl7FotOoMzhk44KpyrYpjprgim_u9DipTWj1Z8xUa7yQiLwWtmZ_TBys12eNJTw0eHV2Kn_9Co_6e57wt1-dyXN-IDQFvtM5yrPJGy', start_index=6415)
Annotation(end_index=6432, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH98BdbcFU1U4DGRiRzlPxIsjKJjYVFBA8aTt4z-W7OeIQbiAp7ta7Cv5nXlZBh2-m57koOdvMEHISevLjTX5KCjhKFQ0_7QBf5N3tN7BAIzqMaY4rC1tC-CpB0_iStwGmV', start_index=6415)
Annotation(end_index=6905, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFX91yBqhrNKgN08jrUwMlLJQ8_2C7CgiuJdvP6gyw9miEtB9NcWPJ8r3tVVST7-qtLCST3D-egCxA0wPC5vsxLfU83fQHdBdjxs7sHMwbpJXMDUthCZuQg_b_I7g_eGjDusL4Y3A2JyihkswrQlgS2hRyHnoLF3G9KaX8b1ronNIQPFdQHoj2wm2mo5bJcXzfXGUo=', start_index=6892)
Annotation(end_index=6905, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5ZYVT1Ve2RGL89sL7kF28A4Kjv-t14eLAtenU68zzEntGYastFseY2Sh8F8-CCHB1rw3JCT-FutWoEA5IUnqCyJ2A2pGGpJKGoM1ZdJUI1StUjOcAc6gopvcP1KAmx-qw6u9WtAz9JHtWz4_D9U_S8P2q-p0=', start_index=6892)
Annotation(end_index=7102, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsRB8VLHvGNvTAdCcUth0RMTclURM-K-2biisvQ4kx2NN-apVeBINxp5Uybb0QBxVrsJZ1asn8ETe-hA1vEjXcYONYyNrNyqkaERjIBKCMNwX3wjYeWrNrWrf-y68pZ44v6pxHkG6Lv6MsqUfAFH1ILoXwPKIRAPrmO4RZIiwdOLfUNDIS2Fr2jsXhHsQPTs-Jt4h0Fgjztrp3Zuzrz2BjF6QNjtllJ4JPx12nPQ==', start_index=7092)
Annotation(end_index=7531, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpBP26R79CsIgEAjzpspzDtb1BHmBi7tghmz7TGLfBU2d2KEXEwTmvrgKpPdIC21mUnpp870eeEX6aguwj1NX-5rVlZzKUSzqEXjUL4YPeIPWOrdooS1oLaSIk3kkR', start_index=7518)
Annotation(end_index=7531, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5ZYVT1Ve2RGL89sL7kF28A4Kjv-t14eLAtenU68zzEntGYastFseY2Sh8F8-CCHB1rw3JCT-FutWoEA5IUnqCyJ2A2pGGpJKGoM1ZdJUI1StUjOcAc6gopvcP1KAmx-qw6u9WtAz9JHtWz4_D9U_S8P2q-p0=', start_index=7518)
Annotation(end_index=8558, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJllGj0D-cUurKBADv_Yqd2nOoNFPg-T8m_IysO858P0degoSjzzcDjnGOmywaNvkJ-SElhvnW2uEGZz-MA-QKX_h8SA_wPHjKJX_uG0zI5QgsB8RN6w==', start_index=8545)
Annotation(end_index=8558, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4m7YaMp8vkspFJB2aRT7T3mPHwVSQTqAmlRRk8gr67JIxC4tQbN0jRYhVow9sqYpALNjCFkzVY9zLhS9Q_MmcisNZdW6qzxGrfsUYMml1IGDAXJXk3w==', start_index=8545)
Annotation(end_index=9245, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpnvvPJOX7DODE-RKiZlSDf-A4VSIpaPSFE1wQrzSxRj7J4eYSgJxo-0viMCL3Wi9GDrQMezzB3-SwguJilgKsSszz6Kveasqf6nIeyxroENzt7YKgng9qSgowpwxTwx2chtSKcgli5XzeOClQysMIm1x98pSvhgkda_E9hA==', start_index=9232)
Annotation(end_index=9245, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4m7YaMp8vkspFJB2aRT7T3mPHwVSQTqAmlRRk8gr67JIxC4tQbN0jRYhVow9sqYpALNjCFkzVY9zLhS9Q_MmcisNZdW6qzxGrfsUYMml1IGDAXJXk3w==', start_index=9232)
Annotation(end_index=9482, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJllGj0D-cUurKBADv_Yqd2nOoNFPg-T8m_IysO858P0degoSjzzcDjnGOmywaNvkJ-SElhvnW2uEGZz-MA-QKX_h8SA_wPHjKJX_uG0zI5QgsB8RN6w==', start_index=9472)
Annotation(end_index=9856, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjcRDGMaoFw7jJPqLmMbVss-dAFgN0lbo1RzkERl9aZQQ3uR9IYQr4SfqF9OenckwEpyRhDwnqMNCEM2-2xYyY-qa2XEziYnSvd6H48E0FlXxEfBpVsRM8cpXJHwXaKQ==', start_index=9846)
Annotation(end_index=10125, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtru73R8JMYVlFkj2QUhjBXy4LNS4MVxL3hYjyd9PQ6xmM07Mxsz4VzN6N_IAIneYVzbOtsFiEtW6-sKphtMjR2sDRk2M7amZC6vZ5DWelsoFjsSCU4NGrnixdbB88FH0VwuzYIUQuZenXROSSAgHeOFQSF3nrshaXQWcZ_s5l9sBB9eiWVB0M-RARMgFXPmRUR3K_zrm6K4b3BDOP46grPLI7fBDeihjRAWkdnrgtPb9vzox_bOSpexeUy2E94EgLHw==', start_index=10115)
Annotation(end_index=10625, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtFqlknLJQJcLuBj5OdKdqedTvuIR--3wfi-AhODtjgmQFyE7eIhqj0tEzcnId7gvvQGQOwmRiOtAUDRPGMPmCsbXCMvoVrNGnLEj11ofUm3hUERv5HuuOBHnoAwpR8Lg2gwgm', start_index=10615)
Annotation(end_index=11408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI4vPeILmolzoADTrwIKs1sglU5uI2lWLhFNDX0cF39nVZbmXu7PjMYETtHgnZO5bKvVU-AEmYnPdRpomCw4TDFsV7-Mpve7ixiMlRrbGH7b4b4eHJcoZQ6yRqdIeg3kdwwkiisICIynkXjM6tjISiKQ3Im-13r0rEJ02Ian3z_ecb_rAh8rflRI0b_Gm5', start_index=11392)
Annotation(end_index=11408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErON8RS17GYA0V89Yy2xK4B_2JJ5i3T28d4MWZx4PWHGfJJMqtvcm0tQ-rF8IE3SS8yWt8-fTdA-C8f0WzbZFAlteatcGo9E0DqzwijbYa_AmPQfLW6V9VypJRRhAjj20eTBX3_GoOV9qDpkbKrsOFSc_l10eIYDovFSqAe989ktZT1tE0H3Gq405LxPLJD8qe1Dhx5MHr', start_index=11392)
Annotation(end_index=11408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2a5r7sHtuegEy67qe-HZ8RS9uP4bHAztFDkhjyR9Hs4NzIFoj4k4uX-Mc9UXfEZ5MadeAhBfVDIyOVAICB79awru_eYEx8ffSik_TWzW1D4Jmk7NDdjRA9p2KGdwdiE55KL2x3CDl9V0tufZARzuaZRImHHsC334syXs=', start_index=11392)
Annotation(end_index=11653, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZjWFM8QXGmPuw9fW_g0BJn-w8rynPCA5fq04p0IDU6rooDcCHVNC-b-8ijDntS7l-LNtJjnekvFJihsJlkMPpQuDEoiQfAoKC_HVQt88m6Gx7My42SeJBzFn3wJWCJuMtT0lottDNyGYRvuGvxT2X', start_index=11639)
Annotation(end_index=11653, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNeNsPQ6L4JgI6nBw3DMZSfXBCM2taHIzSg1FvtcD2EMHJeYiVkWxr96mZrUPLSeVNahg1tMH4Y6E48gEFPmBan2b4CChnzX4UWynwggJQUOBeGOxcL9b8DBc535ScH3cGgQKrLqYLsyJWzx4Q6VuCs21VLtRkphqBYLcINsPfeMBz6OKmkRSje64=', start_index=11639)
Annotation(end_index=12157, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI4vPeILmolzoADTrwIKs1sglU5uI2lWLhFNDX0cF39nVZbmXu7PjMYETtHgnZO5bKvVU-AEmYnPdRpomCw4TDFsV7-Mpve7ixiMlRrbGH7b4b4eHJcoZQ6yRqdIeg3kdwwkiisICIynkXjM6tjISiKQ3Im-13r0rEJ02Ian3z_ecb_rAh8rflRI0b_Gm5', start_index=12145)
Annotation(end_index=12157, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErON8RS17GYA0V89Yy2xK4B_2JJ5i3T28d4MWZx4PWHGfJJMqtvcm0tQ-rF8IE3SS8yWt8-fTdA-C8f0WzbZFAlteatcGo9E0DqzwijbYa_AmPQfLW6V9VypJRRhAjj20eTBX3_GoOV9qDpkbKrsOFSc_l10eIYDovFSqAe989ktZT1tE0H3Gq405LxPLJD8qe1Dhx5MHr', start_index=12145)
Annotation(end_index=12396, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI4vPeILmolzoADTrwIKs1sglU5uI2lWLhFNDX0cF39nVZbmXu7PjMYETtHgnZO5bKvVU-AEmYnPdRpomCw4TDFsV7-Mpve7ixiMlRrbGH7b4b4eHJcoZQ6yRqdIeg3kdwwkiisICIynkXjM6tjISiKQ3Im-13r0rEJ02Ian3z_ecb_rAh8rflRI0b_Gm5', start_index=12387)
Annotation(end_index=12744, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_2LpqRXLqHUgim8Y8gfdII2SidKXlgflUXMQMDGWZQYvBPvkasSZnOB1lK4vwX9lIIe5v44sOEwCGseplNmP9yS3t1shtBuSb6Dq9rMzWBWiO8S8kJ-vivu-eQ26JX_BUCzmO-icischCUBvF7ok=', start_index=12735)
Annotation(end_index=13177, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdXecv_PBzWIloUe6bSeMoPY16WAEKEbiEYH0KYZHvgGkEoCZtz0jvFvqF07jqKky4NEi_OIDFKSGeQ2CLfb9ihyKVu8KyhULH6hBrYbJU4Ly9LuH8Ga5eClvEyx3BcCS7oVO09bgmHZcVTWpKdv_Lwu4=', start_index=13159)
Annotation(end_index=13177, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUGE14oIBIAlGdPCkmV2Bn-Ug2SHj0HVorIGNQH8RwM0GMnrZ_V8uIW-dsssCIp2zWXWfSdR9pV471xuAuditx0vZjXRck27HEobgqIB2zjrrP2TwTIhf5neNJnnqz7Pg-PctQ6P9EBhtmCUq0mR_VvfDKl9e8OoorDqhFvO9HoJfLHXSQSh1L4Oe4C6MDJaLSyCrcoXGptxi_---zvw==', start_index=13159)
Annotation(end_index=13177, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHb2GPhpwsZyoJVJ7Vd7ne1VX17-SVUkzAHnRBF_4gfidcy_xVmjXejLusEXvlKDZd-1l8fqr7FWiZRDXsC-uK2qG3Nm3kNZmwkAPXycySzyNhki-Jdxx2ECufpi5CZv3SfGouYYsxd7-Y_CTN8rSM_1pkDaj2C4kevX4iYM1lf1cdwEKiiczVMt9vfKbIg2GeRVt3i8A==', start_index=13159)
Annotation(end_index=13689, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXysyhW4XoMaH9zlJ19srk2il3EHfBaHFaelt8RkTh5_PJJLc1DQGbUpLLqSFokdSTXSggWeN2pqj8dWl7eXfndf6TT1Y-OYig1Nq81YAqhdzl5jXUqOobKLb7grRhrBvzCICeH-5idpYgZl7QVFWUSvEq3CXRm4xpEUUmD1ja', start_index=13672)
Annotation(end_index=13689, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKY7x-j-H2NN-5J-Vp_c1fzxrcm_nfIZW8UXIiHWL35bYy_ijKgXuF9JZC3SgUSRUXuzpkUdhI66kRrbEez92cLQSoKR09uwtUW3qy2yYBPdhdC0xMLc4BYxLM4-22YdNSQciPtjbB2Ed_dRxHXiakT3SiaYLDriTHn8YhxwE_BmeYKI4CPGG-8H-Ppz1xf_rKr5NnuEbAXhMa-3ZT7laePRKq', start_index=13672)
Annotation(end_index=13689, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_2LpqRXLqHUgim8Y8gfdII2SidKXlgflUXMQMDGWZQYvBPvkasSZnOB1lK4vwX9lIIe5v44sOEwCGseplNmP9yS3t1shtBuSb6Dq9rMzWBWiO8S8kJ-vivu-eQ26JX_BUCzmO-icischCUBvF7ok=', start_index=13672)
Annotation(end_index=14199, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXysyhW4XoMaH9zlJ19srk2il3EHfBaHFaelt8RkTh5_PJJLc1DQGbUpLLqSFokdSTXSggWeN2pqj8dWl7eXfndf6TT1Y-OYig1Nq81YAqhdzl5jXUqOobKLb7grRhrBvzCICeH-5idpYgZl7QVFWUSvEq3CXRm4xpEUUmD1ja', start_index=14185)
Annotation(end_index=14199, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHb2GPhpwsZyoJVJ7Vd7ne1VX17-SVUkzAHnRBF_4gfidcy_xVmjXejLusEXvlKDZd-1l8fqr7FWiZRDXsC-uK2qG3Nm3kNZmwkAPXycySzyNhki-Jdxx2ECufpi5CZv3SfGouYYsxd7-Y_CTN8rSM_1pkDaj2C4kevX4iYM1lf1cdwEKiiczVMt9vfKbIg2GeRVt3i8A==', start_index=14185)
Annotation(end_index=14694, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9e74ixhfBs-ZQAh7BvMqoVvmTPOGZxFPHVihmY2uBIMwK6MBkFyDOYGnrQKjVkcQAxNbnnoi2czWAnRUqdKolOsNuNP8DwucU6PXuCkGeA3WWCh0wEbKuFhXI5W8Xi6_c9Kn4BXMjzzpzpKMfuUhsIGGBnm9EU3_V4JZCwgMkcadVM4xfJdY1c1V7BLLH2xbH_1DnltyV0rlSvZD6V6K9dIv8F-EHubKpLFNkVHZmzffdHLks10OADDxZ0yAFYVIbYSLN2E0_', start_index=14680)
Annotation(end_index=14694, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEXImDiWGmRZEXvLA85_VGaXRssM6k0bfDgfzgUHJaVwKRju6JzHzh70DNLynjClH1MYl58LrekPAuYou8tbLLj1eAFFUvG4SGSbQ2jhX9NzAEVXdxLi6RW1e4xK4Q1MZtn3u0Wa5ECnOXly1_ddD2ymrkijwW-L-5OxOj1qFKii9g1pLCq9Jou4LqJR7jvr1h0_O1utL3eg9UNCtACJOEhkq9JzxLBr8eaANh3g==', start_index=14680)
Annotation(end_index=15056, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVTNnCnCzZwKJrvaqZsm1zSK5LKlr60YdGmvdgqfKE6GEnGMfWX3rpau9DK1s-_cfwe50L_6-uO62U9H3D1_pBDEqEVz2IpYs1fCuGfCz-nh3HiakoEnDSbKPCl8Ov0P2eb9HI3p4_YQzCE-1cGssdtwIojenfJYVkOQna-esxABTmtL3PQVr8UtBjpjo-ldpMTyBkBdtrVsCO7kmApx8Nhi5zaTFeZWA=', start_index=15038)
Annotation(end_index=15056, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEXImDiWGmRZEXvLA85_VGaXRssM6k0bfDgfzgUHJaVwKRju6JzHzh70DNLynjClH1MYl58LrekPAuYou8tbLLj1eAFFUvG4SGSbQ2jhX9NzAEVXdxLi6RW1e4xK4Q1MZtn3u0Wa5ECnOXly1_ddD2ymrkijwW-L-5OxOj1qFKii9g1pLCq9Jou4LqJR7jvr1h0_O1utL3eg9UNCtACJOEhkq9JzxLBr8eaANh3g==', start_index=15038)
Annotation(end_index=15056, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQpLbD6fys-6Wi6eW8fLvcAyetjjaueirsb5YmHI81uNYGrvH0T390Fss5yrmPQV1f_OVQfvFEvGwxybf69x0hbt_AoEWjzZcwRKDD1t3o9oXloYKXdVPiGmq0YmrFH_vYldkEUsTzzRnBwgEyNZ1WyOakQL40hlQMvz519rOaVosgFo1W8l5IsMgHiMDR_6enrRO5q8S5LTqSks8wWuWbzUU5xADzJ1kS_A9RrV48KlJIMh-ff8tJRBA=', start_index=15038)
Annotation(end_index=15388, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-sILSyQSytnHAXFa9Zs2hS44MJsNC3t7Qyg90qZI7SKYmUxTCUC3bIlYfegovuQnGcXeuAv8D3gCg3-_jp8Y3KudWftvGXbgunQrk_EoTldx3KrunTzwFS2GIe9rUSnCeCSyDsDBwypqdIyOh26AfD8Xemoak3EVjqALn7nABglgsbFE4-niGAXg-84491fvkF8kN0xxKLRAlXB5wOuSGuca951avPosBFXdczJ5_dP8G9gxo', start_index=15378)
Annotation(end_index=15715, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-sILSyQSytnHAXFa9Zs2hS44MJsNC3t7Qyg90qZI7SKYmUxTCUC3bIlYfegovuQnGcXeuAv8D3gCg3-_jp8Y3KudWftvGXbgunQrk_EoTldx3KrunTzwFS2GIe9rUSnCeCSyDsDBwypqdIyOh26AfD8Xemoak3EVjqALn7nABglgsbFE4-niGAXg-84491fvkF8kN0xxKLRAlXB5wOuSGuca951avPosBFXdczJ5_dP8G9gxo', start_index=15705)
Annotation(end_index=16268, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPOE2UMFcxHZ5k8bhGVc5FfjldAA3aUMw8Ym2_VaXvI8ICYPqZMzFr8k8Wb4KkL_cr-DIX_EpvztEDEnG6PrB4Bycd5zL6Y4GPZ_JeAezmwO2Q-mFZ7CY0M5bzjc4IGRjKwPw=', start_index=16250)
Annotation(end_index=16268, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkjYnIbzWbyHlWn_9Br8HZ1Bvl5yQ15nyzIGv22SaXjNNkjiyiSa9JqU07eh0UGXDbobFHUS1riEss_LXOK8LvpAO35NnPHoACS6bAqN3anhCuOxjeUwwHssDhrrVava2CFhwn6KoPfbsJl1wPko1pVUVY', start_index=16250)
Annotation(end_index=16268, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYM49SfP2g9MN44BBGujpZekgf24U1NwQpbfKFoJXGj467mysQ8Puz6lhNMtuTPU2oSx3p0MuQirj7YNKEeHHglWRYPzETzX3TxHpIgs2914-vcf2h6pFyEmL-w1brYatNsLfV_TRAf0ubNjTvJb_tkqqQjLcxLMB04p7Rs3Qj2G48qLimyNXZfu39qnSK80e0f7fyiTYW-7yWFX0lFRzjC8I0tzMlOTVYayde3o_J', start_index=16250)
Annotation(end_index=17584, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_Mx4V7sFsig-WP9CAiKQmIskvPeklAJIFCwmS0_88MpKzq8SXAZ3T212qUG-0r0O2YP6WV9BbXPDLcN-S2dyGHA0CDN1MU9sYy7g8AigTSadpGSF9f9kciwBIt4Kaxg==', start_index=17575)
Annotation(end_index=17607, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_Mx4V7sFsig-WP9CAiKQmIskvPeklAJIFCwmS0_88MpKzq8SXAZ3T212qUG-0r0O2YP6WV9BbXPDLcN-S2dyGHA0CDN1MU9sYy7g8AigTSadpGSF9f9kciwBIt4Kaxg==', start_index=17598)
Annotation(end_index=17618, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5ZYVT1Ve2RGL89sL7kF28A4Kjv-t14eLAtenU68zzEntGYastFseY2Sh8F8-CCHB1rw3JCT-FutWoEA5IUnqCyJ2A2pGGpJKGoM1ZdJUI1StUjOcAc6gopvcP1KAmx-qw6u9WtAz9JHtWz4_D9U_S8P2q-p0=', start_index=17608)
Annotation(end_index=17649, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5ZYVT1Ve2RGL89sL7kF28A4Kjv-t14eLAtenU68zzEntGYastFseY2Sh8F8-CCHB1rw3JCT-FutWoEA5IUnqCyJ2A2pGGpJKGoM1ZdJUI1StUjOcAc6gopvcP1KAmx-qw6u9WtAz9JHtWz4_D9U_S8P2q-p0=', start_index=17639)
Annotation(end_index=17659, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFX91yBqhrNKgN08jrUwMlLJQ8_2C7CgiuJdvP6gyw9miEtB9NcWPJ8r3tVVST7-qtLCST3D-egCxA0wPC5vsxLfU83fQHdBdjxs7sHMwbpJXMDUthCZuQg_b_I7g_eGjDusL4Y3A2JyihkswrQlgS2hRyHnoLF3G9KaX8b1ronNIQPFdQHoj2wm2mo5bJcXzfXGUo=', start_index=17650)
Annotation(end_index=17698, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFX91yBqhrNKgN08jrUwMlLJQ8_2C7CgiuJdvP6gyw9miEtB9NcWPJ8r3tVVST7-qtLCST3D-egCxA0wPC5vsxLfU83fQHdBdjxs7sHMwbpJXMDUthCZuQg_b_I7g_eGjDusL4Y3A2JyihkswrQlgS2hRyHnoLF3G9KaX8b1ronNIQPFdQHoj2wm2mo5bJcXzfXGUo=', start_index=17689)
Annotation(end_index=17709, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkBYTIiEkuSSMi0nsJMMUig1O9o-BlE2wztgUVuN1TyZDZY8C3zIkqxYGTWbmZV0S2j6JF1w336rTTYaaMyLuAdMlep5h6PUTCHpbpO1jZPvttKrpZjNkxX4HWwbQ2KrkX0oyvWT8Pus6xVaDASAIl7FotOoMzhk44KpyrYpjprgim_u9DipTWj1Z8xUa7yQiLwWtmZ_TBys12eNJTw0eHV2Kn_9Co_6e57wt1-dyXN-IDQFvtM5yrPJGy', start_index=17699)
Annotation(end_index=17735, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkBYTIiEkuSSMi0nsJMMUig1O9o-BlE2wztgUVuN1TyZDZY8C3zIkqxYGTWbmZV0S2j6JF1w336rTTYaaMyLuAdMlep5h6PUTCHpbpO1jZPvttKrpZjNkxX4HWwbQ2KrkX0oyvWT8Pus6xVaDASAIl7FotOoMzhk44KpyrYpjprgim_u9DipTWj1Z8xUa7yQiLwWtmZ_TBys12eNJTw0eHV2Kn_9Co_6e57wt1-dyXN-IDQFvtM5yrPJGy', start_index=17725)
Annotation(end_index=17746, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPOE2UMFcxHZ5k8bhGVc5FfjldAA3aUMw8Ym2_VaXvI8ICYPqZMzFr8k8Wb4KkL_cr-DIX_EpvztEDEnG6PrB4Bycd5zL6Y4GPZ_JeAezmwO2Q-mFZ7CY0M5bzjc4IGRjKwPw=', start_index=17736)
Annotation(end_index=17770, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFPOE2UMFcxHZ5k8bhGVc5FfjldAA3aUMw8Ym2_VaXvI8ICYPqZMzFr8k8Wb4KkL_cr-DIX_EpvztEDEnG6PrB4Bycd5zL6Y4GPZ_JeAezmwO2Q-mFZ7CY0M5bzjc4IGRjKwPw=', start_index=17760)
Annotation(end_index=17780, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8ft_rg29dzEYh41E9fAf8_cylnXjsO5J_PRXYKVdhokFEalaJ6-UBh5dEVYHjpRqu6xTYMx59JlJ1kjT4sba_8ETF1FeMx10ja4lgat5D0bP6NPkIxYbm8jtYC2UnTfBOk5d6vk8jFNoPUUHs0OXZRjPmgf7P7ftem2BHXJd3LCR-heAELgO-YWX1sAQhoyTnx2_GKhUmTUNH5Z_cIB4Hy2o3', start_index=17771)
Annotation(end_index=17802, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8ft_rg29dzEYh41E9fAf8_cylnXjsO5J_PRXYKVdhokFEalaJ6-UBh5dEVYHjpRqu6xTYMx59JlJ1kjT4sba_8ETF1FeMx10ja4lgat5D0bP6NPkIxYbm8jtYC2UnTfBOk5d6vk8jFNoPUUHs0OXZRjPmgf7P7ftem2BHXJd3LCR-heAELgO-YWX1sAQhoyTnx2_GKhUmTUNH5Z_cIB4Hy2o3', start_index=17793)
Annotation(end_index=17813, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVkHYiAijGKgwCyq7WcH0M92aCk5uDRYCkWAI6v5YwBdn0q47jkASPRnBOeWDo7YaeXrWPbIg-f9xUw3WhnOLCuBx59HHfFrofUD8d8AQ07k4oSXMgbRyKnBDaru-Kz9LFUDZvN50CgZz2nIbFD4SHJm6j-xvfbl2tMXgAHCghOpC7CyxmS8wU8yltjcf4-sZR-ojJWSXLziIRVk__A-03qq2h6ps0OnxIwJyClrdVHyQB', start_index=17803)
Annotation(end_index=17845, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVkHYiAijGKgwCyq7WcH0M92aCk5uDRYCkWAI6v5YwBdn0q47jkASPRnBOeWDo7YaeXrWPbIg-f9xUw3WhnOLCuBx59HHfFrofUD8d8AQ07k4oSXMgbRyKnBDaru-Kz9LFUDZvN50CgZz2nIbFD4SHJm6j-xvfbl2tMXgAHCghOpC7CyxmS8wU8yltjcf4-sZR-ojJWSXLziIRVk__A-03qq2h6ps0OnxIwJyClrdVHyQB', start_index=17835)
Annotation(end_index=17856, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEGw6jIF8OkWQb0R18itqt2zHG24H49bW6XxJbOSGH490oAahCIsZ9uJzDAQDLV0CPTdeTxFSsKtybXMXEJBDaUhnP-KOPJ47fQTMCW7Fph1hiVa8SC8EETrQ9yygc_Axj9vqblABSiA==', start_index=17846)
Annotation(end_index=17891, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEGw6jIF8OkWQb0R18itqt2zHG24H49bW6XxJbOSGH490oAahCIsZ9uJzDAQDLV0CPTdeTxFSsKtybXMXEJBDaUhnP-KOPJ47fQTMCW7Fph1hiVa8SC8EETrQ9yygc_Axj9vqblABSiA==', start_index=17881)
Annotation(end_index=17902, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzJAUWSRQ9ERKV6-zVf3elVum7wNnDH-0oU3NOZuPnLk8aNc-k6_n2Kw5mMbzizQyLefEWtT3utT6e9CZN2DADumfZDbeVOYas6MISYB4y3STb0oEQ1A==', start_index=17892)
Annotation(end_index=17927, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzJAUWSRQ9ERKV6-zVf3elVum7wNnDH-0oU3NOZuPnLk8aNc-k6_n2Kw5mMbzizQyLefEWtT3utT6e9CZN2DADumfZDbeVOYas6MISYB4y3STb0oEQ1A==', start_index=17917)
Annotation(end_index=17938, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHn-tVWDmTS1BMhCM9ZEVEqZDXsLDofInUQ4Ah1p35qyD6GD8dgmGkLy6mnigdeX97eImwKw7AyXgZ2RRUWo28ZmXQIF5sEmCFHO-EPc9rvKchJ0DWrP9sNEYqHuSoBEs75sYHj9uDU6EJgVvjdwVW8r-s0vBZ5', start_index=17928)
Annotation(end_index=17975, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHn-tVWDmTS1BMhCM9ZEVEqZDXsLDofInUQ4Ah1p35qyD6GD8dgmGkLy6mnigdeX97eImwKw7AyXgZ2RRUWo28ZmXQIF5sEmCFHO-EPc9rvKchJ0DWrP9sNEYqHuSoBEs75sYHj9uDU6EJgVvjdwVW8r-s0vBZ5', start_index=17965)
Annotation(end_index=17985, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI4vPeILmolzoADTrwIKs1sglU5uI2lWLhFNDX0cF39nVZbmXu7PjMYETtHgnZO5bKvVU-AEmYnPdRpomCw4TDFsV7-Mpve7ixiMlRrbGH7b4b4eHJcoZQ6yRqdIeg3kdwwkiisICIynkXjM6tjISiKQ3Im-13r0rEJ02Ian3z_ecb_rAh8rflRI0b_Gm5', start_index=17976)
Annotation(end_index=18022, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI4vPeILmolzoADTrwIKs1sglU5uI2lWLhFNDX0cF39nVZbmXu7PjMYETtHgnZO5bKvVU-AEmYnPdRpomCw4TDFsV7-Mpve7ixiMlRrbGH7b4b4eHJcoZQ6yRqdIeg3kdwwkiisICIynkXjM6tjISiKQ3Im-13r0rEJ02Ian3z_ecb_rAh8rflRI0b_Gm5', start_index=18013)
Annotation(end_index=18033, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZjWFM8QXGmPuw9fW_g0BJn-w8rynPCA5fq04p0IDU6rooDcCHVNC-b-8ijDntS7l-LNtJjnekvFJihsJlkMPpQuDEoiQfAoKC_HVQt88m6Gx7My42SeJBzFn3wJWCJuMtT0lottDNyGYRvuGvxT2X', start_index=18023)
Annotation(end_index=18076, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZjWFM8QXGmPuw9fW_g0BJn-w8rynPCA5fq04p0IDU6rooDcCHVNC-b-8ijDntS7l-LNtJjnekvFJihsJlkMPpQuDEoiQfAoKC_HVQt88m6Gx7My42SeJBzFn3wJWCJuMtT0lottDNyGYRvuGvxT2X', start_index=18066)
Annotation(end_index=18087, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErBW4uVd_NBTpuDcWBbA7cWJjBEMAAAOYmw_TkjEik3hLo3Cal_twrUub54CioxZbolRkL2J7X-I5eTxRkF6FkLzK1KareRbwq_zKWAZssufKs-WtSEUpgjL7XcgTzaNHA0yTSLjLIPM-zXCm-z3Kb9dErbnoU6IBaV0O48CBNMAf8BHP8hFXAyMgraRIeQ9_OT2cEad71tDw=', start_index=18077)
Annotation(end_index=18121, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErBW4uVd_NBTpuDcWBbA7cWJjBEMAAAOYmw_TkjEik3hLo3Cal_twrUub54CioxZbolRkL2J7X-I5eTxRkF6FkLzK1KareRbwq_zKWAZssufKs-WtSEUpgjL7XcgTzaNHA0yTSLjLIPM-zXCm-z3Kb9dErbnoU6IBaV0O48CBNMAf8BHP8hFXAyMgraRIeQ9_OT2cEad71tDw=', start_index=18111)
Annotation(end_index=18131, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErON8RS17GYA0V89Yy2xK4B_2JJ5i3T28d4MWZx4PWHGfJJMqtvcm0tQ-rF8IE3SS8yWt8-fTdA-C8f0WzbZFAlteatcGo9E0DqzwijbYa_AmPQfLW6V9VypJRRhAjj20eTBX3_GoOV9qDpkbKrsOFSc_l10eIYDovFSqAe989ktZT1tE0H3Gq405LxPLJD8qe1Dhx5MHr', start_index=18122)
Annotation(end_index=18168, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErON8RS17GYA0V89Yy2xK4B_2JJ5i3T28d4MWZx4PWHGfJJMqtvcm0tQ-rF8IE3SS8yWt8-fTdA-C8f0WzbZFAlteatcGo9E0DqzwijbYa_AmPQfLW6V9VypJRRhAjj20eTBX3_GoOV9qDpkbKrsOFSc_l10eIYDovFSqAe989ktZT1tE0H3Gq405LxPLJD8qe1Dhx5MHr', start_index=18159)
Annotation(end_index=18179, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfALZQBzroVhToedH1XZGs0e-5EoifLDEyI8-Ic7IInDNAQvw9wvPjx6jIpA6gvLED1N4sg1xSn-L60hpsJkK--j6wbz8-3e622bXiQdT5DTH_AbGh1keQP93M2Nrr1S1mYFkm_DMbTRE2FrG80qoIFIcH_M4qaS_7PMNI1t8IbPRAwlk=', start_index=18169)
Annotation(end_index=18210, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfALZQBzroVhToedH1XZGs0e-5EoifLDEyI8-Ic7IInDNAQvw9wvPjx6jIpA6gvLED1N4sg1xSn-L60hpsJkK--j6wbz8-3e622bXiQdT5DTH_AbGh1keQP93M2Nrr1S1mYFkm_DMbTRE2FrG80qoIFIcH_M4qaS_7PMNI1t8IbPRAwlk=', start_index=18200)
Annotation(end_index=18221, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6dpXbhdrBDNvXWXiBcGjRjnPSg5NJfs_2SBA2Xl0X35Vf6lv_OjO-1oRgo0R7tJJmz605NO8Xxkf5GAhpWyF8HwSO1xcwpXSjMgK6ZN0MxCZSrljpgMjdK54XHZgUWtl6EzOEghc-yIj2B-mG7k59MGKQgwFhA0acr-M020fv7vn1RPLw7rYOjx0fy1_j4_4GSINcDiKMFX5XMtT2j7Cpo5xQ3V6MOidQShk8YBp_HJk6LXgEMDiuV7agCcM=', start_index=18211)
Annotation(end_index=18246, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6dpXbhdrBDNvXWXiBcGjRjnPSg5NJfs_2SBA2Xl0X35Vf6lv_OjO-1oRgo0R7tJJmz605NO8Xxkf5GAhpWyF8HwSO1xcwpXSjMgK6ZN0MxCZSrljpgMjdK54XHZgUWtl6EzOEghc-yIj2B-mG7k59MGKQgwFhA0acr-M020fv7vn1RPLw7rYOjx0fy1_j4_4GSINcDiKMFX5XMtT2j7Cpo5xQ3V6MOidQShk8YBp_HJk6LXgEMDiuV7agCcM=', start_index=18236)
Annotation(end_index=18257, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5NXWHgGs_1Esd2ZXQON3EnIAPX5Qaz50qWI3zDGTLmepXJDZcDbpiX2P98BgD9b64Ho_Ics2xYU_h15Hr1446nIaEQvIhwhPtqqAEbqW5cIE371b0OxAHmLGrDzFddQNFLcq8gb4IwjQHj-nv5HJlP6npA3__LvdEE0cbArLM-a-RydFVmdR8zlhlaRpUR-w3WOdXHciFnpvYTaEXbCwwNsf3U3srDbBkN6g-G7Zumz0_NRc=', start_index=18247)
Annotation(end_index=18287, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5NXWHgGs_1Esd2ZXQON3EnIAPX5Qaz50qWI3zDGTLmepXJDZcDbpiX2P98BgD9b64Ho_Ics2xYU_h15Hr1446nIaEQvIhwhPtqqAEbqW5cIE371b0OxAHmLGrDzFddQNFLcq8gb4IwjQHj-nv5HJlP6npA3__LvdEE0cbArLM-a-RydFVmdR8zlhlaRpUR-w3WOdXHciFnpvYTaEXbCwwNsf3U3srDbBkN6g-G7Zumz0_NRc=', start_index=18277)
Annotation(end_index=18298, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3_SKEt0m7PYn4tBXWgcVrqM8aBDcW-cgnAdoUdPmlqkjwUVGPc22smUgbcmNG7nRa1zCsaonC16ELhwElvAU2xf7AfamgRXBdr2CYHkdcIg2Yeg_ePkIf5pvEcLRBWmcJ_mQgWXeyH82QjTd6RaDMlMVOYGdsfCI6K4gAu_3QDkSyKgSPVgy10HsTgrwDLpMXTf4WpHKj', start_index=18288)
Annotation(end_index=18330, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3_SKEt0m7PYn4tBXWgcVrqM8aBDcW-cgnAdoUdPmlqkjwUVGPc22smUgbcmNG7nRa1zCsaonC16ELhwElvAU2xf7AfamgRXBdr2CYHkdcIg2Yeg_ePkIf5pvEcLRBWmcJ_mQgWXeyH82QjTd6RaDMlMVOYGdsfCI6K4gAu_3QDkSyKgSPVgy10HsTgrwDLpMXTf4WpHKj', start_index=18320)
Annotation(end_index=18341, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlpAriAv5Xf1X1YIkCLXCXMKymtwzjxaDSM91bGKN6Lp1oWupz7F1Bu-kwCoGSXmCmeRz3h3PaXzJydrE7fUgggFNitZAhm07_rLRaBjUvsj_k2rm_UlVdUUKJgbhMSSy-zjsAP0Ms', start_index=18331)
Annotation(end_index=18364, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlpAriAv5Xf1X1YIkCLXCXMKymtwzjxaDSM91bGKN6Lp1oWupz7F1Bu-kwCoGSXmCmeRz3h3PaXzJydrE7fUgggFNitZAhm07_rLRaBjUvsj_k2rm_UlVdUUKJgbhMSSy-zjsAP0Ms', start_index=18354)
Annotation(end_index=18374, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4m7YaMp8vkspFJB2aRT7T3mPHwVSQTqAmlRRk8gr67JIxC4tQbN0jRYhVow9sqYpALNjCFkzVY9zLhS9Q_MmcisNZdW6qzxGrfsUYMml1IGDAXJXk3w==', start_index=18365)
Annotation(end_index=18398, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4m7YaMp8vkspFJB2aRT7T3mPHwVSQTqAmlRRk8gr67JIxC4tQbN0jRYhVow9sqYpALNjCFkzVY9zLhS9Q_MmcisNZdW6qzxGrfsUYMml1IGDAXJXk3w==', start_index=18389)
Annotation(end_index=18409, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjcRDGMaoFw7jJPqLmMbVss-dAFgN0lbo1RzkERl9aZQQ3uR9IYQr4SfqF9OenckwEpyRhDwnqMNCEM2-2xYyY-qa2XEziYnSvd6H48E0FlXxEfBpVsRM8cpXJHwXaKQ==', start_index=18399)
Annotation(end_index=18433, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjcRDGMaoFw7jJPqLmMbVss-dAFgN0lbo1RzkERl9aZQQ3uR9IYQr4SfqF9OenckwEpyRhDwnqMNCEM2-2xYyY-qa2XEziYnSvd6H48E0FlXxEfBpVsRM8cpXJHwXaKQ==', start_index=18423)
Annotation(end_index=18444, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpnvvPJOX7DODE-RKiZlSDf-A4VSIpaPSFE1wQrzSxRj7J4eYSgJxo-0viMCL3Wi9GDrQMezzB3-SwguJilgKsSszz6Kveasqf6nIeyxroENzt7YKgng9qSgowpwxTwx2chtSKcgli5XzeOClQysMIm1x98pSvhgkda_E9hA==', start_index=18434)
Annotation(end_index=18474, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpnvvPJOX7DODE-RKiZlSDf-A4VSIpaPSFE1wQrzSxRj7J4eYSgJxo-0viMCL3Wi9GDrQMezzB3-SwguJilgKsSszz6Kveasqf6nIeyxroENzt7YKgng9qSgowpwxTwx2chtSKcgli5XzeOClQysMIm1x98pSvhgkda_E9hA==', start_index=18464)
Annotation(end_index=18485, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJllGj0D-cUurKBADv_Yqd2nOoNFPg-T8m_IysO858P0degoSjzzcDjnGOmywaNvkJ-SElhvnW2uEGZz-MA-QKX_h8SA_wPHjKJX_uG0zI5QgsB8RN6w==', start_index=18475)
Annotation(end_index=18510, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJllGj0D-cUurKBADv_Yqd2nOoNFPg-T8m_IysO858P0degoSjzzcDjnGOmywaNvkJ-SElhvnW2uEGZz-MA-QKX_h8SA_wPHjKJX_uG0zI5QgsB8RN6w==', start_index=18500)
Annotation(end_index=18521, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTuXjeOl3henv6D-ChZyibbJnHHwbiPnJ8Fk0cFvbOdz3o3ybgemOwQ1D_XHUI3_p1R5EdgMnRqI_mu6Q-Hm4Aigh2AFko8b06pJ-dTgW22Q96c4J88xM9lqmSRTZDctptj8EFhlZB2odYkIzl3fERpNnXE4eqFtxaxEEdnA==', start_index=18511)
Annotation(end_index=18551, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTuXjeOl3henv6D-ChZyibbJnHHwbiPnJ8Fk0cFvbOdz3o3ybgemOwQ1D_XHUI3_p1R5EdgMnRqI_mu6Q-Hm4Aigh2AFko8b06pJ-dTgW22Q96c4J88xM9lqmSRTZDctptj8EFhlZB2odYkIzl3fERpNnXE4eqFtxaxEEdnA==', start_index=18541)
Annotation(end_index=18562, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEh0TTmLcbdlGUYxD62rWelU1ihp6wZeOIMrmjGVQquaek8v4FC8XQyRzUv0TCHe3RQ-vQeGnrshLLq4kYGfycbKXXlocSiKjXVpdsHZWIUEjmcQ1ukbhnX3NtFp9QLWl757ryUoUdpwcgqbh5Q4So9lrkL0Nj3URabKLa3krN7aw==', start_index=18552)
Annotation(end_index=18596, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEh0TTmLcbdlGUYxD62rWelU1ihp6wZeOIMrmjGVQquaek8v4FC8XQyRzUv0TCHe3RQ-vQeGnrshLLq4kYGfycbKXXlocSiKjXVpdsHZWIUEjmcQ1ukbhnX3NtFp9QLWl757ryUoUdpwcgqbh5Q4So9lrkL0Nj3URabKLa3krN7aw==', start_index=18586)
Annotation(end_index=18607, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEXImDiWGmRZEXvLA85_VGaXRssM6k0bfDgfzgUHJaVwKRju6JzHzh70DNLynjClH1MYl58LrekPAuYou8tbLLj1eAFFUvG4SGSbQ2jhX9NzAEVXdxLi6RW1e4xK4Q1MZtn3u0Wa5ECnOXly1_ddD2ymrkijwW-L-5OxOj1qFKii9g1pLCq9Jou4LqJR7jvr1h0_O1utL3eg9UNCtACJOEhkq9JzxLBr8eaANh3g==', start_index=18597)
Annotation(end_index=18652, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEXImDiWGmRZEXvLA85_VGaXRssM6k0bfDgfzgUHJaVwKRju6JzHzh70DNLynjClH1MYl58LrekPAuYou8tbLLj1eAFFUvG4SGSbQ2jhX9NzAEVXdxLi6RW1e4xK4Q1MZtn3u0Wa5ECnOXly1_ddD2ymrkijwW-L-5OxOj1qFKii9g1pLCq9Jou4LqJR7jvr1h0_O1utL3eg9UNCtACJOEhkq9JzxLBr8eaANh3g==', start_index=18642)
Annotation(end_index=18663, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQpLbD6fys-6Wi6eW8fLvcAyetjjaueirsb5YmHI81uNYGrvH0T390Fss5yrmPQV1f_OVQfvFEvGwxybf69x0hbt_AoEWjzZcwRKDD1t3o9oXloYKXdVPiGmq0YmrFH_vYldkEUsTzzRnBwgEyNZ1WyOakQL40hlQMvz519rOaVosgFo1W8l5IsMgHiMDR_6enrRO5q8S5LTqSks8wWuWbzUU5xADzJ1kS_A9RrV48KlJIMh-ff8tJRBA=', start_index=18653)
Annotation(end_index=18689, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQpLbD6fys-6Wi6eW8fLvcAyetjjaueirsb5YmHI81uNYGrvH0T390Fss5yrmPQV1f_OVQfvFEvGwxybf69x0hbt_AoEWjzZcwRKDD1t3o9oXloYKXdVPiGmq0YmrFH_vYldkEUsTzzRnBwgEyNZ1WyOakQL40hlQMvz519rOaVosgFo1W8l5IsMgHiMDR_6enrRO5q8S5LTqSks8wWuWbzUU5xADzJ1kS_A9RrV48KlJIMh-ff8tJRBA=', start_index=18679)
Annotation(end_index=18700, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9e74ixhfBs-ZQAh7BvMqoVvmTPOGZxFPHVihmY2uBIMwK6MBkFyDOYGnrQKjVkcQAxNbnnoi2czWAnRUqdKolOsNuNP8DwucU6PXuCkGeA3WWCh0wEbKuFhXI5W8Xi6_c9Kn4BXMjzzpzpKMfuUhsIGGBnm9EU3_V4JZCwgMkcadVM4xfJdY1c1V7BLLH2xbH_1DnltyV0rlSvZD6V6K9dIv8F-EHubKpLFNkVHZmzffdHLks10OADDxZ0yAFYVIbYSLN2E0_', start_index=18690)
Annotation(end_index=18741, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9e74ixhfBs-ZQAh7BvMqoVvmTPOGZxFPHVihmY2uBIMwK6MBkFyDOYGnrQKjVkcQAxNbnnoi2czWAnRUqdKolOsNuNP8DwucU6PXuCkGeA3WWCh0wEbKuFhXI5W8Xi6_c9Kn4BXMjzzpzpKMfuUhsIGGBnm9EU3_V4JZCwgMkcadVM4xfJdY1c1V7BLLH2xbH_1DnltyV0rlSvZD6V6K9dIv8F-EHubKpLFNkVHZmzffdHLks10OADDxZ0yAFYVIbYSLN2E0_', start_index=18731)
Annotation(end_index=18752, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBevmDxJKsMmN5YRzqhVRd8wW1fc8JG7ifXesbyeeVfVBm7bAflES3yJYsj_IRrYKvrDZFNSCaP-CkI1To_RKXABKVbN0aN_KA3nzPtfij06tgfUIhO9BwASNwS1ihUJ9hlBVuZ0BPBbz44U50rQB7QIcpdLo-mbIvj96JNGgnQLZ5BxBwPp2sU40WX2QwkcSuGVDO_b4LKDQaupRbSuq8cSQniOXfZcVBW5nnUDLonlw6EDqlRCcOv81-oro5PLNXYqhi8OS5_u-lm3G-m_zoig==', start_index=18742)
Annotation(end_index=18775, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBevmDxJKsMmN5YRzqhVRd8wW1fc8JG7ifXesbyeeVfVBm7bAflES3yJYsj_IRrYKvrDZFNSCaP-CkI1To_RKXABKVbN0aN_KA3nzPtfij06tgfUIhO9BwASNwS1ihUJ9hlBVuZ0BPBbz44U50rQB7QIcpdLo-mbIvj96JNGgnQLZ5BxBwPp2sU40WX2QwkcSuGVDO_b4LKDQaupRbSuq8cSQniOXfZcVBW5nnUDLonlw6EDqlRCcOv81-oro5PLNXYqhi8OS5_u-lm3G-m_zoig==', start_index=18765)
Annotation(end_index=18786, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVTNnCnCzZwKJrvaqZsm1zSK5LKlr60YdGmvdgqfKE6GEnGMfWX3rpau9DK1s-_cfwe50L_6-uO62U9H3D1_pBDEqEVz2IpYs1fCuGfCz-nh3HiakoEnDSbKPCl8Ov0P2eb9HI3p4_YQzCE-1cGssdtwIojenfJYVkOQna-esxABTmtL3PQVr8UtBjpjo-ldpMTyBkBdtrVsCO7kmApx8Nhi5zaTFeZWA=', start_index=18776)
Annotation(end_index=18814, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEVTNnCnCzZwKJrvaqZsm1zSK5LKlr60YdGmvdgqfKE6GEnGMfWX3rpau9DK1s-_cfwe50L_6-uO62U9H3D1_pBDEqEVz2IpYs1fCuGfCz-nh3HiakoEnDSbKPCl8Ov0P2eb9HI3p4_YQzCE-1cGssdtwIojenfJYVkOQna-esxABTmtL3PQVr8UtBjpjo-ldpMTyBkBdtrVsCO7kmApx8Nhi5zaTFeZWA=', start_index=18804)
Annotation(end_index=18825, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUGE14oIBIAlGdPCkmV2Bn-Ug2SHj0HVorIGNQH8RwM0GMnrZ_V8uIW-dsssCIp2zWXWfSdR9pV471xuAuditx0vZjXRck27HEobgqIB2zjrrP2TwTIhf5neNJnnqz7Pg-PctQ6P9EBhtmCUq0mR_VvfDKl9e8OoorDqhFvO9HoJfLHXSQSh1L4Oe4C6MDJaLSyCrcoXGptxi_---zvw==', start_index=18815)
Annotation(end_index=18859, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUGE14oIBIAlGdPCkmV2Bn-Ug2SHj0HVorIGNQH8RwM0GMnrZ_V8uIW-dsssCIp2zWXWfSdR9pV471xuAuditx0vZjXRck27HEobgqIB2zjrrP2TwTIhf5neNJnnqz7Pg-PctQ6P9EBhtmCUq0mR_VvfDKl9e8OoorDqhFvO9HoJfLHXSQSh1L4Oe4C6MDJaLSyCrcoXGptxi_---zvw==', start_index=18849)
Annotation(end_index=18869, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_2LpqRXLqHUgim8Y8gfdII2SidKXlgflUXMQMDGWZQYvBPvkasSZnOB1lK4vwX9lIIe5v44sOEwCGseplNmP9yS3t1shtBuSb6Dq9rMzWBWiO8S8kJ-vivu-eQ26JX_BUCzmO-icischCUBvF7ok=', start_index=18860)
Annotation(end_index=18892, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_2LpqRXLqHUgim8Y8gfdII2SidKXlgflUXMQMDGWZQYvBPvkasSZnOB1lK4vwX9lIIe5v44sOEwCGseplNmP9yS3t1shtBuSb6Dq9rMzWBWiO8S8kJ-vivu-eQ26JX_BUCzmO-icischCUBvF7ok=', start_index=18883)
Annotation(end_index=18903, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHb2GPhpwsZyoJVJ7Vd7ne1VX17-SVUkzAHnRBF_4gfidcy_xVmjXejLusEXvlKDZd-1l8fqr7FWiZRDXsC-uK2qG3Nm3kNZmwkAPXycySzyNhki-Jdxx2ECufpi5CZv3SfGouYYsxd7-Y_CTN8rSM_1pkDaj2C4kevX4iYM1lf1cdwEKiiczVMt9vfKbIg2GeRVt3i8A==', start_index=18893)
Annotation(end_index=18943, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHb2GPhpwsZyoJVJ7Vd7ne1VX17-SVUkzAHnRBF_4gfidcy_xVmjXejLusEXvlKDZd-1l8fqr7FWiZRDXsC-uK2qG3Nm3kNZmwkAPXycySzyNhki-Jdxx2ECufpi5CZv3SfGouYYsxd7-Y_CTN8rSM_1pkDaj2C4kevX4iYM1lf1cdwEKiiczVMt9vfKbIg2GeRVt3i8A==', start_index=18933)
Annotation(end_index=18954, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKY7x-j-H2NN-5J-Vp_c1fzxrcm_nfIZW8UXIiHWL35bYy_ijKgXuF9JZC3SgUSRUXuzpkUdhI66kRrbEez92cLQSoKR09uwtUW3qy2yYBPdhdC0xMLc4BYxLM4-22YdNSQciPtjbB2Ed_dRxHXiakT3SiaYLDriTHn8YhxwE_BmeYKI4CPGG-8H-Ppz1xf_rKr5NnuEbAXhMa-3ZT7laePRKq', start_index=18944)
Annotation(end_index=18982, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKY7x-j-H2NN-5J-Vp_c1fzxrcm_nfIZW8UXIiHWL35bYy_ijKgXuF9JZC3SgUSRUXuzpkUdhI66kRrbEez92cLQSoKR09uwtUW3qy2yYBPdhdC0xMLc4BYxLM4-22YdNSQciPtjbB2Ed_dRxHXiakT3SiaYLDriTHn8YhxwE_BmeYKI4CPGG-8H-Ppz1xf_rKr5NnuEbAXhMa-3ZT7laePRKq', start_index=18972)
Annotation(end_index=18993, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8QXmehkekI5n0v8iQsGkiTI17Y3K7M9F2eyk9U9jMNm2ix_x0AjM8H-GW3Wg2TMjJYEemPNts_K0JjekK6OZUQWMAB5qnJWp-sCqYcq-07W6q3p8d0f98QosY7IIL09K49TSyO5dyjN9FCf8dcfB1', start_index=18983)
Annotation(end_index=19035, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8QXmehkekI5n0v8iQsGkiTI17Y3K7M9F2eyk9U9jMNm2ix_x0AjM8H-GW3Wg2TMjJYEemPNts_K0JjekK6OZUQWMAB5qnJWp-sCqYcq-07W6q3p8d0f98QosY7IIL09K49TSyO5dyjN9FCf8dcfB1', start_index=19025)
Annotation(end_index=19046, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOATNpK1OmMqcqBjSr2OdHdKpMZZAZcC1qQQzy_x1wyeBTmnNH52RywZTYJ-91dtJmqH_yI-Wn5--ecUV0A3vfJg3Pj6K3HLKi6-YnzvuJULcU7eCu-Pa9aEvesFFapp39ZSXuL3_S', start_index=19036)
Annotation(end_index=19069, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOATNpK1OmMqcqBjSr2OdHdKpMZZAZcC1qQQzy_x1wyeBTmnNH52RywZTYJ-91dtJmqH_yI-Wn5--ecUV0A3vfJg3Pj6K3HLKi6-YnzvuJULcU7eCu-Pa9aEvesFFapp39ZSXuL3_S', start_index=19059)
Annotation(end_index=19080, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-sILSyQSytnHAXFa9Zs2hS44MJsNC3t7Qyg90qZI7SKYmUxTCUC3bIlYfegovuQnGcXeuAv8D3gCg3-_jp8Y3KudWftvGXbgunQrk_EoTldx3KrunTzwFS2GIe9rUSnCeCSyDsDBwypqdIyOh26AfD8Xemoak3EVjqALn7nABglgsbFE4-niGAXg-84491fvkF8kN0xxKLRAlXB5wOuSGuca951avPosBFXdczJ5_dP8G9gxo', start_index=19070)
Annotation(end_index=19112, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-sILSyQSytnHAXFa9Zs2hS44MJsNC3t7Qyg90qZI7SKYmUxTCUC3bIlYfegovuQnGcXeuAv8D3gCg3-_jp8Y3KudWftvGXbgunQrk_EoTldx3KrunTzwFS2GIe9rUSnCeCSyDsDBwypqdIyOh26AfD8Xemoak3EVjqALn7nABglgsbFE4-niGAXg-84491fvkF8kN0xxKLRAlXB5wOuSGuca951avPosBFXdczJ5_dP8G9gxo', start_index=19102)
Annotation(end_index=19123, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4RfB39vRahif7QxH4eNQifyuYyIU-JLMRhhqfE4W_IdHZVVf2rFNjYh6xElWzXnmE4qyVN_8_8xZ35UDv6rB_qN6eIFWIpZ3RVq27iWSNxF3k4sfaWECX4rGCKe7KBmMaBbLC2VBbMLHUNvCF-Id0t7bRG34YsEk9C7dFcvGqAxjOWg_9hy0j1Z017EKJ5qgJJoBwt-QAYZq9', start_index=19113)
Annotation(end_index=19146, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4RfB39vRahif7QxH4eNQifyuYyIU-JLMRhhqfE4W_IdHZVVf2rFNjYh6xElWzXnmE4qyVN_8_8xZ35UDv6rB_qN6eIFWIpZ3RVq27iWSNxF3k4sfaWECX4rGCKe7KBmMaBbLC2VBbMLHUNvCF-Id0t7bRG34YsEk9C7dFcvGqAxjOWg_9hy0j1Z017EKJ5qgJJoBwt-QAYZq9', start_index=19136)
Annotation(end_index=19157, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGmymSANrjFOpodcoUAUC530UXpJwhFBG4wmYm-kkOHZrKGD2RIcL0Vzj_Sz_5LliW6D9oovrmPOx1Qe80AHRL6AkV-YasKdGczFqpYJPU1LyK51xPVij5f_AZn4jATddUlv7dIjydqprmn4BwrZ63', start_index=19147)
Annotation(end_index=19185, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHGmymSANrjFOpodcoUAUC530UXpJwhFBG4wmYm-kkOHZrKGD2RIcL0Vzj_Sz_5LliW6D9oovrmPOx1Qe80AHRL6AkV-YasKdGczFqpYJPU1LyK51xPVij5f_AZn4jATddUlv7dIjydqprmn4BwrZ63', start_index=19175)
Annotation(end_index=19195, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpBP26R79CsIgEAjzpspzDtb1BHmBi7tghmz7TGLfBU2d2KEXEwTmvrgKpPdIC21mUnpp870eeEX6aguwj1NX-5rVlZzKUSzqEXjUL4YPeIPWOrdooS1oLaSIk3kkR', start_index=19186)
Annotation(end_index=19217, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpBP26R79CsIgEAjzpspzDtb1BHmBi7tghmz7TGLfBU2d2KEXEwTmvrgKpPdIC21mUnpp870eeEX6aguwj1NX-5rVlZzKUSzqEXjUL4YPeIPWOrdooS1oLaSIk3kkR', start_index=19208)
Annotation(end_index=19228, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH98BdbcFU1U4DGRiRzlPxIsjKJjYVFBA8aTt4z-W7OeIQbiAp7ta7Cv5nXlZBh2-m57koOdvMEHISevLjTX5KCjhKFQ0_7QBf5N3tN7BAIzqMaY4rC1tC-CpB0_iStwGmV', start_index=19218)
Annotation(end_index=19255, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH98BdbcFU1U4DGRiRzlPxIsjKJjYVFBA8aTt4z-W7OeIQbiAp7ta7Cv5nXlZBh2-m57koOdvMEHISevLjTX5KCjhKFQ0_7QBf5N3tN7BAIzqMaY4rC1tC-CpB0_iStwGmV', start_index=19245)
Annotation(end_index=19266, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsRB8VLHvGNvTAdCcUth0RMTclURM-K-2biisvQ4kx2NN-apVeBINxp5Uybb0QBxVrsJZ1asn8ETe-hA1vEjXcYONYyNrNyqkaERjIBKCMNwX3wjYeWrNrWrf-y68pZ44v6pxHkG6Lv6MsqUfAFH1ILoXwPKIRAPrmO4RZIiwdOLfUNDIS2Fr2jsXhHsQPTs-Jt4h0Fgjztrp3Zuzrz2BjF6QNjtllJ4JPx12nPQ==', start_index=19256)
Annotation(end_index=19298, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsRB8VLHvGNvTAdCcUth0RMTclURM-K-2biisvQ4kx2NN-apVeBINxp5Uybb0QBxVrsJZ1asn8ETe-hA1vEjXcYONYyNrNyqkaERjIBKCMNwX3wjYeWrNrWrf-y68pZ44v6pxHkG6Lv6MsqUfAFH1ILoXwPKIRAPrmO4RZIiwdOLfUNDIS2Fr2jsXhHsQPTs-Jt4h0Fgjztrp3Zuzrz2BjF6QNjtllJ4JPx12nPQ==', start_index=19288)
Annotation(end_index=19309, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYM49SfP2g9MN44BBGujpZekgf24U1NwQpbfKFoJXGj467mysQ8Puz6lhNMtuTPU2oSx3p0MuQirj7YNKEeHHglWRYPzETzX3TxHpIgs2914-vcf2h6pFyEmL-w1brYatNsLfV_TRAf0ubNjTvJb_tkqqQjLcxLMB04p7Rs3Qj2G48qLimyNXZfu39qnSK80e0f7fyiTYW-7yWFX0lFRzjC8I0tzMlOTVYayde3o_J', start_index=19299)
Annotation(end_index=19341, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYM49SfP2g9MN44BBGujpZekgf24U1NwQpbfKFoJXGj467mysQ8Puz6lhNMtuTPU2oSx3p0MuQirj7YNKEeHHglWRYPzETzX3TxHpIgs2914-vcf2h6pFyEmL-w1brYatNsLfV_TRAf0ubNjTvJb_tkqqQjLcxLMB04p7Rs3Qj2G48qLimyNXZfu39qnSK80e0f7fyiTYW-7yWFX0lFRzjC8I0tzMlOTVYayde3o_J', start_index=19331)
Annotation(end_index=19352, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkjYnIbzWbyHlWn_9Br8HZ1Bvl5yQ15nyzIGv22SaXjNNkjiyiSa9JqU07eh0UGXDbobFHUS1riEss_LXOK8LvpAO35NnPHoACS6bAqN3anhCuOxjeUwwHssDhrrVava2CFhwn6KoPfbsJl1wPko1pVUVY', start_index=19342)
Annotation(end_index=19376, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkjYnIbzWbyHlWn_9Br8HZ1Bvl5yQ15nyzIGv22SaXjNNkjiyiSa9JqU07eh0UGXDbobFHUS1riEss_LXOK8LvpAO35NnPHoACS6bAqN3anhCuOxjeUwwHssDhrrVava2CFhwn6KoPfbsJl1wPko1pVUVY', start_index=19366)
Annotation(end_index=19386, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxUI_nBfBa1qX0SowroChHcPptJYlNyQhJSfKAw05GV0BP8s22akrqY_Amw2fQgjtOvvrkQSCCVEUpRSPgFWlr1clnpYYWWB4Dlqp0UxKqH5gdR2lwnNtaRyIiWPdPIuXo6vCQU-5PWzEJETs=', start_index=19377)
Annotation(end_index=19423, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxUI_nBfBa1qX0SowroChHcPptJYlNyQhJSfKAw05GV0BP8s22akrqY_Amw2fQgjtOvvrkQSCCVEUpRSPgFWlr1clnpYYWWB4Dlqp0UxKqH5gdR2lwnNtaRyIiWPdPIuXo6vCQU-5PWzEJETs=', start_index=19414)
Annotation(end_index=19433, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErON8RS17GYA0V89Yy2xK4B_2JJ5i3T28d4MWZx4PWHGfJJMqtvcm0tQ-rF8IE3SS8yWt8-fTdA-C8f0WzbZFAlteatcGo9E0DqzwijbYa_AmPQfLW6V9VypJRRhAjj20eTBX3_GoOV9qDpkbKrsOFSc_l10eIYDovFSqAe989ktZT1tE0H3Gq405LxPLJD8qe1Dhx5MHr', start_index=19424)
Annotation(end_index=19470, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErON8RS17GYA0V89Yy2xK4B_2JJ5i3T28d4MWZx4PWHGfJJMqtvcm0tQ-rF8IE3SS8yWt8-fTdA-C8f0WzbZFAlteatcGo9E0DqzwijbYa_AmPQfLW6V9VypJRRhAjj20eTBX3_GoOV9qDpkbKrsOFSc_l10eIYDovFSqAe989ktZT1tE0H3Gq405LxPLJD8qe1Dhx5MHr', start_index=19461)
Annotation(end_index=19480, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI4vPeILmolzoADTrwIKs1sglU5uI2lWLhFNDX0cF39nVZbmXu7PjMYETtHgnZO5bKvVU-AEmYnPdRpomCw4TDFsV7-Mpve7ixiMlRrbGH7b4b4eHJcoZQ6yRqdIeg3kdwwkiisICIynkXjM6tjISiKQ3Im-13r0rEJ02Ian3z_ecb_rAh8rflRI0b_Gm5', start_index=19471)
Annotation(end_index=19517, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI4vPeILmolzoADTrwIKs1sglU5uI2lWLhFNDX0cF39nVZbmXu7PjMYETtHgnZO5bKvVU-AEmYnPdRpomCw4TDFsV7-Mpve7ixiMlRrbGH7b4b4eHJcoZQ6yRqdIeg3kdwwkiisICIynkXjM6tjISiKQ3Im-13r0rEJ02Ian3z_ecb_rAh8rflRI0b_Gm5', start_index=19508)
Annotation(end_index=19528, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNeNsPQ6L4JgI6nBw3DMZSfXBCM2taHIzSg1FvtcD2EMHJeYiVkWxr96mZrUPLSeVNahg1tMH4Y6E48gEFPmBan2b4CChnzX4UWynwggJQUOBeGOxcL9b8DBc535ScH3cGgQKrLqYLsyJWzx4Q6VuCs21VLtRkphqBYLcINsPfeMBz6OKmkRSje64=', start_index=19518)
Annotation(end_index=19573, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNeNsPQ6L4JgI6nBw3DMZSfXBCM2taHIzSg1FvtcD2EMHJeYiVkWxr96mZrUPLSeVNahg1tMH4Y6E48gEFPmBan2b4CChnzX4UWynwggJQUOBeGOxcL9b8DBc535ScH3cGgQKrLqYLsyJWzx4Q6VuCs21VLtRkphqBYLcINsPfeMBz6OKmkRSje64=', start_index=19563)
Annotation(end_index=19584, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2a5r7sHtuegEy67qe-HZ8RS9uP4bHAztFDkhjyR9Hs4NzIFoj4k4uX-Mc9UXfEZ5MadeAhBfVDIyOVAICB79awru_eYEx8ffSik_TWzW1D4Jmk7NDdjRA9p2KGdwdiE55KL2x3CDl9V0tufZARzuaZRImHHsC334syXs=', start_index=19574)
Annotation(end_index=19608, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2a5r7sHtuegEy67qe-HZ8RS9uP4bHAztFDkhjyR9Hs4NzIFoj4k4uX-Mc9UXfEZ5MadeAhBfVDIyOVAICB79awru_eYEx8ffSik_TWzW1D4Jmk7NDdjRA9p2KGdwdiE55KL2x3CDl9V0tufZARzuaZRImHHsC334syXs=', start_index=19598)
Annotation(end_index=19619, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZZmu6loHVSVKK2myw8jBdSuhfh78SE306OIgmhKC4i99QxdYMrt5TL69c1RvfSFs9tycfT2IbSkuuKpXLOIw9R3u-GH5nlsQMakQQ3ANRaJb2hxfanapIfcfmd6g=', start_index=19609)
Annotation(end_index=19643, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZZmu6loHVSVKK2myw8jBdSuhfh78SE306OIgmhKC4i99QxdYMrt5TL69c1RvfSFs9tycfT2IbSkuuKpXLOIw9R3u-GH5nlsQMakQQ3ANRaJb2hxfanapIfcfmd6g=', start_index=19633)
Annotation(end_index=19654, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdXecv_PBzWIloUe6bSeMoPY16WAEKEbiEYH0KYZHvgGkEoCZtz0jvFvqF07jqKky4NEi_OIDFKSGeQ2CLfb9ihyKVu8KyhULH6hBrYbJU4Ly9LuH8Ga5eClvEyx3BcCS7oVO09bgmHZcVTWpKdv_Lwu4=', start_index=19644)
Annotation(end_index=19680, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdXecv_PBzWIloUe6bSeMoPY16WAEKEbiEYH0KYZHvgGkEoCZtz0jvFvqF07jqKky4NEi_OIDFKSGeQ2CLfb9ihyKVu8KyhULH6hBrYbJU4Ly9LuH8Ga5eClvEyx3BcCS7oVO09bgmHZcVTWpKdv_Lwu4=', start_index=19670)
Annotation(end_index=19691, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHb2GPhpwsZyoJVJ7Vd7ne1VX17-SVUkzAHnRBF_4gfidcy_xVmjXejLusEXvlKDZd-1l8fqr7FWiZRDXsC-uK2qG3Nm3kNZmwkAPXycySzyNhki-Jdxx2ECufpi5CZv3SfGouYYsxd7-Y_CTN8rSM_1pkDaj2C4kevX4iYM1lf1cdwEKiiczVMt9vfKbIg2GeRVt3i8A==', start_index=19681)
Annotation(end_index=19731, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHb2GPhpwsZyoJVJ7Vd7ne1VX17-SVUkzAHnRBF_4gfidcy_xVmjXejLusEXvlKDZd-1l8fqr7FWiZRDXsC-uK2qG3Nm3kNZmwkAPXycySzyNhki-Jdxx2ECufpi5CZv3SfGouYYsxd7-Y_CTN8rSM_1pkDaj2C4kevX4iYM1lf1cdwEKiiczVMt9vfKbIg2GeRVt3i8A==', start_index=19721)
Annotation(end_index=19742, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXysyhW4XoMaH9zlJ19srk2il3EHfBaHFaelt8RkTh5_PJJLc1DQGbUpLLqSFokdSTXSggWeN2pqj8dWl7eXfndf6TT1Y-OYig1Nq81YAqhdzl5jXUqOobKLb7grRhrBvzCICeH-5idpYgZl7QVFWUSvEq3CXRm4xpEUUmD1ja', start_index=19732)
Annotation(end_index=19777, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXysyhW4XoMaH9zlJ19srk2il3EHfBaHFaelt8RkTh5_PJJLc1DQGbUpLLqSFokdSTXSggWeN2pqj8dWl7eXfndf6TT1Y-OYig1Nq81YAqhdzl5jXUqOobKLb7grRhrBvzCICeH-5idpYgZl7QVFWUSvEq3CXRm4xpEUUmD1ja', start_index=19767)
Annotation(end_index=19787, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_2LpqRXLqHUgim8Y8gfdII2SidKXlgflUXMQMDGWZQYvBPvkasSZnOB1lK4vwX9lIIe5v44sOEwCGseplNmP9yS3t1shtBuSb6Dq9rMzWBWiO8S8kJ-vivu-eQ26JX_BUCzmO-icischCUBvF7ok=', start_index=19778)
Annotation(end_index=19810, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_2LpqRXLqHUgim8Y8gfdII2SidKXlgflUXMQMDGWZQYvBPvkasSZnOB1lK4vwX9lIIe5v44sOEwCGseplNmP9yS3t1shtBuSb6Dq9rMzWBWiO8S8kJ-vivu-eQ26JX_BUCzmO-icischCUBvF7ok=', start_index=19801)
Annotation(end_index=19821, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFy1Y4-Hr5WdLOgQg0d6uS54rlXRXZDFDSDe8OAINoa0sL_0Ui4U3xA5pMmpHQV7DI3gUgiMeunxEZapxkVMAlDbE3tjX-LqfY2xb3e8g4_HKjKTOPnL8Xse5kX_eRzo-iooI0avHKM3Xku8zxGHI_otyihxWZTUs090-yA8E2-4WDFLFyIBLYXN3sNt9O3uPINnO1ak0AyBA101A==', start_index=19811)
Annotation(end_index=19846, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFy1Y4-Hr5WdLOgQg0d6uS54rlXRXZDFDSDe8OAINoa0sL_0Ui4U3xA5pMmpHQV7DI3gUgiMeunxEZapxkVMAlDbE3tjX-LqfY2xb3e8g4_HKjKTOPnL8Xse5kX_eRzo-iooI0avHKM3Xku8zxGHI_otyihxWZTUs090-yA8E2-4WDFLFyIBLYXN3sNt9O3uPINnO1ak0AyBA101A==', start_index=19836)
Annotation(end_index=19857, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJllGj0D-cUurKBADv_Yqd2nOoNFPg-T8m_IysO858P0degoSjzzcDjnGOmywaNvkJ-SElhvnW2uEGZz-MA-QKX_h8SA_wPHjKJX_uG0zI5QgsB8RN6w==', start_index=19847)
Annotation(end_index=19882, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJllGj0D-cUurKBADv_Yqd2nOoNFPg-T8m_IysO858P0degoSjzzcDjnGOmywaNvkJ-SElhvnW2uEGZz-MA-QKX_h8SA_wPHjKJX_uG0zI5QgsB8RN6w==', start_index=19872)
Annotation(end_index=19893, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjcRDGMaoFw7jJPqLmMbVss-dAFgN0lbo1RzkERl9aZQQ3uR9IYQr4SfqF9OenckwEpyRhDwnqMNCEM2-2xYyY-qa2XEziYnSvd6H48E0FlXxEfBpVsRM8cpXJHwXaKQ==', start_index=19883)
Annotation(end_index=19917, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjcRDGMaoFw7jJPqLmMbVss-dAFgN0lbo1RzkERl9aZQQ3uR9IYQr4SfqF9OenckwEpyRhDwnqMNCEM2-2xYyY-qa2XEziYnSvd6H48E0FlXxEfBpVsRM8cpXJHwXaKQ==', start_index=19907)
Annotation(end_index=19928, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtFqlknLJQJcLuBj5OdKdqedTvuIR--3wfi-AhODtjgmQFyE7eIhqj0tEzcnId7gvvQGQOwmRiOtAUDRPGMPmCsbXCMvoVrNGnLEj11ofUm3hUERv5HuuOBHnoAwpR8Lg2gwgm', start_index=19918)
Annotation(end_index=19952, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtFqlknLJQJcLuBj5OdKdqedTvuIR--3wfi-AhODtjgmQFyE7eIhqj0tEzcnId7gvvQGQOwmRiOtAUDRPGMPmCsbXCMvoVrNGnLEj11ofUm3hUERv5HuuOBHnoAwpR8Lg2gwgm', start_index=19942)
Annotation(end_index=19963, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ1UoPZ0kvsakR0YIffiCXZSjxLZwTmrF-KAcEF3_3m2b1WYC3IvQjkNj5A8GLRLgKyFcxN_tUyh2nBf7IeCZ13w4hEsUEdd-hMgbOD_BKt3bpWwcfpfPymnEtRBVF9nfTOFsCAjxixhmlU5cd0LlVNfgeV2C74bRPjMZfBbXSAg==', start_index=19953)
Annotation(end_index=19989, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJ1UoPZ0kvsakR0YIffiCXZSjxLZwTmrF-KAcEF3_3m2b1WYC3IvQjkNj5A8GLRLgKyFcxN_tUyh2nBf7IeCZ13w4hEsUEdd-hMgbOD_BKt3bpWwcfpfPymnEtRBVF9nfTOFsCAjxixhmlU5cd0LlVNfgeV2C74bRPjMZfBbXSAg==', start_index=19979)
Annotation(end_index=20000, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtru73R8JMYVlFkj2QUhjBXy4LNS4MVxL3hYjyd9PQ6xmM07Mxsz4VzN6N_IAIneYVzbOtsFiEtW6-sKphtMjR2sDRk2M7amZC6vZ5DWelsoFjsSCU4NGrnixdbB88FH0VwuzYIUQuZenXROSSAgHeOFQSF3nrshaXQWcZ_s5l9sBB9eiWVB0M-RARMgFXPmRUR3K_zrm6K4b3BDOP46grPLI7fBDeihjRAWkdnrgtPb9vzox_bOSpexeUy2E94EgLHw==', start_index=19990)
Annotation(end_index=20032, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtru73R8JMYVlFkj2QUhjBXy4LNS4MVxL3hYjyd9PQ6xmM07Mxsz4VzN6N_IAIneYVzbOtsFiEtW6-sKphtMjR2sDRk2M7amZC6vZ5DWelsoFjsSCU4NGrnixdbB88FH0VwuzYIUQuZenXROSSAgHeOFQSF3nrshaXQWcZ_s5l9sBB9eiWVB0M-RARMgFXPmRUR3K_zrm6K4b3BDOP46grPLI7fBDeihjRAWkdnrgtPb9vzox_bOSpexeUy2E94EgLHw==', start_index=20022)

## Sources
