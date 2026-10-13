# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** ba157db7 | **Time:** 311.08s | **Cost:** $1.27060
--------------------------------------------------------------------------------

# Hierarchical Optimization vs. Distributed Coordination: Balancing Information Entropy and Decision Efficiency in Financial Systems

### Key Points
*   **Hierarchical Efficiency via Structural Entropy Minimization:** Recent advancements in reinforcement learning, specifically the Structural Information principles-based Decision Making (SIDM) framework, demonstrate that hierarchical algorithms can optimally balance information processing and decision efficiency. By minimizing structural entropy to create optimal encoding trees, these systems can improve convergence speed by over 60% compared to non-hierarchical baselines, effectively compressing complex state spaces into actionable abstractions.
*   **The Inevitability of Coordination Costs in Distributed Networks:** Theoretical and empirical evidence from Transaction Cost Economics (TCE) confirms that distributed networks (including blockchain and decentralized autonomous organizations) inherently incur higher coordination costs than centralized hierarchies. While distributed ledgers reduce verification costs, they increase the "metering" and consensus overhead required to align autonomous agents, particularly when asset specificity and uncertainty are high.
*   **Entropy as a Dual Indicator:** In financial markets, entropy plays a dual role. High structural entropy correlates with market instability and crisis (disorder), while maximum entropy principles in portfolio construction are used to minimize bias and maximize diversification. The "optimal balance" involves maximizing information entropy for robust modeling while minimizing structural entropy for efficient execution.
*   **Hybrid Governance as the Solution:** Purely distributed systems struggle with latency and coordination friction, while rigid hierarchies risk information bottlenecks. The literature suggests that "hybrid" governance structures—which utilize hierarchical decision-making for execution efficiency but leverage distributed networks for information gathering and verification—offer the most viable path to balancing entropy maximization (information richness) with decision efficiency.

---

## 1. Introduction

The architectural design of financial organizations and algorithmic trading systems is defined by a fundamental tension: the trade-off between the maximization of information intake (entropy) and the efficiency of decision execution. In the era of high-frequency trading, decentralized finance (DeFi), and complex adaptive systems, this trade-off has moved from a theoretical concern to a critical engineering challenge. The central inquiry of this report is whether hierarchical optimization algorithms can optimally balance these competing forces, or if the shift toward distributed networks inevitably imposes prohibitive coordination costs.

Current research indicates a bifurcation in how these systems are optimized. On one hand, hierarchical reinforcement learning (HRL) and structural information principles suggest that imposing a hierarchical structure on data—effectively minimizing structural entropy—is essential for rapid skill acquisition and decision convergence [cite: 1]. On the other hand, the rise of distributed ledger technologies (DLT) and decentralized autonomous organizations (DAOs) champions a network-based approach, which, while robust against single points of failure, faces significant theoretical and practical limits regarding coordination costs as defined by Transaction Cost Economics (TCE) [cite: 2].

This report synthesizes findings from computational finance, information theory, and organizational economics to provide a comprehensive analysis of this dichotomy. It explores how structural entropy serves as a metric for both market stability and algorithmic efficiency, and why the "coordination tax" of distributed systems remains a persistent barrier to displacing hierarchical efficiency in time-sensitive financial environments.

---

## 2. Hierarchical Optimization and Structural Information Principles

The efficiency of decision-making in complex financial environments relies heavily on the agent's ability to abstract relevant information from a noisy background. Recent breakthroughs in hierarchical reinforcement learning (HRL) provide a mathematical framework for understanding how hierarchies can optimize the balance between information entropy and decision speed.

### 2.1 The SIDM Framework: Minimizing Structural Entropy for Efficiency
The most compelling evidence for the efficacy of hierarchical optimization comes from the development of the Structural Information principles-based Decision Making (SIDM) framework. Financial environments are characterized by high-dimensional state spaces and stochastic transitions. Standard reinforcement learning (RL) algorithms often struggle in these settings due to the "curse of dimensionality."

The SIDM framework addresses this by utilizing **structural information principles** to construct an optimal encoding tree. This process involves:
1.  **Unsupervised Partitioning:** Grouping states and actions based on feature similarity into communities.
2.  **Structural Entropy Minimization:** The algorithm constructs a directed, weighted transition graph of these abstract states. It then minimizes the high-dimensional structural entropy of this graph to generate an optimal hierarchy [cite: 3, 4].

The minimization of structural entropy is not merely a data compression technique; it is a method of discovering the "natural" hierarchy of the decision space. By minimizing the uncertainty (entropy) in the transition dynamics between abstract states, the algorithm identifies "skills" or "roles" that capture key transition patterns [cite: 5].

**Empirical Results on Efficiency:**
Research indicates that this hierarchical approach yields substantial efficiency gains. In comparative benchmarks against state-of-the-art (SOTA) baselines, the SIDM framework demonstrated:
*   **Convergence Speed:** An improvement in convergence timesteps by up to **64.86%** [cite: 1].
*   **Stability:** A reduction in the standard deviation of rewards (stability) by up to **88.26%** [cite: 3].
*   **Policy Quality:** An improvement in average rewards by up to **32.70%** [cite: 4].

These metrics suggest that hierarchical structures are not just organizational conveniences but are mathematically optimal for reducing the computational cost of decision-making in complex environments. By compressing the state space through entropy minimization, the hierarchy allows the system to ignore irrelevant noise (high entropy) and focus on the structural dynamics that drive value.

### 2.2 Structural Entropy as a Metric of Complexity
The concept of structural entropy extends beyond algorithm design into the analysis of the financial networks themselves. Structural entropy quantifies the dynamic uncertainty in complex graph structures, measuring the minimum number of bits required to identify an accessible vertex in a random walk [cite: 1].

In the context of SIDM and similar algorithms, a **low structural entropy** signals a clear, efficient hierarchical organization. This implies greater functional coherence and robustness. Conversely, **high structural entropy** indicates a system that is difficult to decompose, approaching the behavior of a random graph, which is computationally expensive to navigate [cite: 6].

Therefore, the "optimal balance" in a hierarchical algorithm is achieved when the system minimizes the structural entropy of its internal representation (the encoding tree) while maximizing its ability to process the high-entropy input from the market. This internal reduction of entropy is precisely what allows for the rapid decision efficiency observed in the research.

---

## 3. Information Entropy in Financial Markets and Portfolios

While hierarchical algorithms seek to *minimize* structural entropy to aid decision-making, financial theory often seeks to *maximize* information entropy to manage risk and construct robust portfolios. This section explores the dual nature of entropy in finance.

### 3.1 The Principle of Maximum Entropy (MEP) in Portfolio Optimization
In portfolio theory, entropy is treated as a measure of diversity and a guard against bias. The **Principle of Maximum Entropy (MEP)** posits that, among all probability distributions consistent with known constraints (e.g., expected returns), the one with the maximum entropy represents the most "neutral" or unbiased description of the system [cite: 7].

**Applications of MEP:**
*   **Risk Management:** Maximizing the Shannon entropy of portfolio weights ensures that the portfolio is as dispersed as possible, avoiding concentration risk. A portfolio concentrated on a single asset has an entropy of 0 (or 1 depending on normalization), while an equally weighted portfolio ($1/N$) achieves maximum entropy [cite: 8, 9].
*   **Performance:** Studies comparing Return-Entropy Portfolio Optimization (REPO) against traditional Mean-Variance (Markowitz) optimization have found that entropy-based models often outperform by generating higher mean returns at minimum risk levels [cite: 10]. For instance, an entropy-fuzzy TOPSIS model applied to the Dow Jones Industrial Average generated a higher mean return (0.0225) than the benchmark index (0.0095) [cite: 11, 12].
*   **Algorithmic Trading:** Entropy is also used as a filtering mechanism. High entropy in price action indicates randomness and uncertainty (choppy markets), while low entropy suggests structured, directional trends. Algorithms using Shannon entropy to filter trading signals have been shown to improve profitability by avoiding entries during high-entropy noise periods [cite: 13, 14].

### 3.2 Structural Entropy and Market Stability
While maximizing entropy is beneficial for portfolio diversification, **high structural entropy** in the market network itself is a strong predictor of instability and systemic risk.

**Market Crisis Indicators:**
Research analyzing correlation-based networks of stock markets (e.g., S&P 500, NIKKEI 225) reveals a high linear correlation between structural entropy and volatility.
*   **Crisis Periods:** During major financial crises (e.g., the 2008 Global Financial Crisis, the COVID-19 pandemic), structural entropy peaks. This reflects a "disordered" market where asset correlations become complex, unpredictable, and globally interconnected [cite: 15, 16, 17].
*   **Stable Periods:** During periods of market stability, structural entropy drops, indicating a more centralized or modular network structure where influence is concentrated in key nodes or sectors [cite: 17].

**The Stability-Efficiency Paradox:**
This creates a paradox for financial organizations. To be robust (portfolio level), they must maximize the entropy of their holdings. However, to be efficient and stable (market level), the system requires low structural entropy. Hierarchical algorithms like SIDM resolve this by creating a low-entropy *internal* structure (the decision hierarchy) to navigate a high-entropy *external* environment (the market).

---

## 4. Distributed Networks vs. Hierarchies: The Coordination Cost Dilemma

The user's query asks whether distributed networks "inevitably incur coordination costs." The literature on Transaction Cost Economics (TCE) and distributed systems provides a definitive affirmative answer, particularly when compared to the efficiency of hierarchies.

### 4.1 Transaction Cost Economics (TCE) Perspective
TCE, pioneered by Coase and Williamson, explains organizational structures based on the costs of transacting. It posits that firms (hierarchies) emerge when the costs of coordinating transactions in the open market exceed the costs of organizing them internally [cite: 2, 18].

**Sources of Coordination Costs:**
*   **Search and Negotiation:** Finding partners and agreeing on terms.
*   **Enforcement:** Ensuring parties stick to the agreement.
*   **Metering:** Measuring performance and output.

**Hierarchies:** Hierarchies reduce these costs through "fiat" (centralized command), bundling tasks, and internal monitoring. They are particularly efficient when asset specificity is high (specialized tasks) and uncertainty is high, as they prevent "hold-up" problems and allow for adaptive execution without renegotiating contracts [cite: 2].

**Distributed Networks (Markets/DAOs):** Distributed systems, such as Decentralized Autonomous Organizations (DAOs) or blockchain-based networks, aim to replace hierarchical trust with cryptographic verification. While this reduces *verification* costs, it often increases *coordination* costs.
*   **Consensus Overhead:** In a distributed system, decisions often require consensus among nodes (e.g., Proof of Work, voting in a DAO). This introduces latency and computational expense that does not exist in a centralized hierarchy [cite: 19, 20].
*   **Metering Challenges:** Decentralized communities face "metering costs"—the difficulty of measuring individual contributions to a collective output without a central monitor. This can lead to free-riding or inefficient resource allocation [cite: 2].

### 4.2 The "Coordination Tax" of Distributed Systems
Empirical studies in network management and digital platforms reinforce the TCE predictions.
*   **Latency and Replication:** Distributed networks require data replication and coordination among multiple servers/nodes. Any interruption in this synchronization causes service disruptions. Centralized systems, by contrast, act in unison with less complexity [cite: 20, 21].
*   **Decision Latency:** In urgent tasks, centralized networks lead to more positive member perception and higher efficiency because they can quickly coordinate resources. Distributed networks are preferred only when task urgency is weak [cite: 22].
*   **The "Scale-Intensive" Reality:** In the digital economy, "scale-intensive" development models (often centralized) tend to prioritize innovation hubs and efficiency, whereas "equity-focused" (distributed) models prioritize access but face higher coordination challenges due to uneven capabilities [cite: 23].

**Blockchain Specifics:**
While blockchain reduces information asymmetry and verification costs, it raises coordination costs in decentralized settings. The "trustless" nature of the ledger means that every transaction must be validated by the network, creating a bottleneck that centralized hierarchies do not suffer from. TCE analysis suggests that for high-specificity transactions (e.g., complex financial derivatives or public procurement), corporate hierarchies remain more efficient than decentralized communities because they internalize these coordination frictions [cite: 2].

---

## 5. Synthesis: Optimally Balancing Entropy and Efficiency

The synthesis of the research results leads to a nuanced conclusion regarding the possibility of balancing these factors.

### 5.1 The Hierarchical Advantage
Hierarchical optimization algorithms appear to be the superior mechanism for balancing entropy and efficiency.
*   **Mechanism:** By minimizing *structural* entropy (optimizing the topology of the decision tree), hierarchies reduce the "search space" for the algorithm. This allows the system to handle high *information* entropy (market data) without becoming overwhelmed.
*   **Evidence:** The SIDM framework's ability to improve convergence by ~65% while maintaining high policy quality proves that hierarchies can "compress" the complexity of the environment into efficient decision paths [cite: 1].
*   **Contrast:** Distributed networks, by their nature, maintain high structural entropy (flat, mesh-like connections). While this makes them resilient, it prevents the kind of optimization that SIDM achieves. A distributed network cannot easily "prune" itself to form an optimal encoding tree without becoming a hierarchy.

### 5.2 The Role of Distributed Systems
Distributed networks are not "inefficient" in an absolute sense; they optimize for a different variable: **resilience and trust minimization**.
*   **Trade-off:** They incur coordination costs (the price of consensus) to buy robustness against censorship and single-point failure.
*   **Hybrid Future:** The literature suggests that the future of financial organizations is likely **hybrid**. "Federated" or "hybrid" governance structures can use distributed ledgers for transparent record-keeping (lowering verification costs) while retaining hierarchical structures for execution and decision-making (lowering coordination costs) [cite: 2, 24].

### 5.3 The "Optimal Balance" Defined
The optimal balance in a financial organization is dynamic:
1.  **Input Layer (High Entropy):** The system must ingest maximum entropy data (diverse signals, broad market view) to avoid bias (MEP).
2.  **Processing Layer (Hierarchical Optimization):** The system must process this data through a hierarchy that minimizes structural entropy (SIDM), converting noise into signal and compressing state spaces.
3.  **Execution Layer (Low Coordination Cost):** The decision must be executed via a mechanism that minimizes coordination friction—typically a centralized or hierarchical channel rather than a distributed consensus mechanism, especially for high-frequency actions.

---

## 6. Conclusion

The research strongly supports the conclusion that **hierarchical optimization algorithms are uniquely capable of optimally balancing information entropy maximization and decision efficiency**, a feat that purely distributed networks struggle to match due to inherent coordination costs.

The **SIDM framework** serves as the primary proof of concept, demonstrating that by minimizing the structural entropy of the decision-making architecture, an organization can achieve significant gains in convergence speed (efficiency) and stability. This hierarchical structuring allows the system to ingest high-entropy information (maximizing diversity) while executing decisions with low-entropy precision.

Conversely, **distributed networks inevitably incur coordination costs**. Transaction Cost Economics and network theory confirm that the redundancy, consensus mechanisms, and metering challenges inherent in decentralized systems create a "coordination tax." While distributed systems offer superior resilience and reduced verification costs, they cannot compete with hierarchies in terms of pure decision efficiency and speed, particularly in high-urgency financial contexts.

Therefore, the optimal architectural strategy for financial organizations is not to abandon hierarchy for decentralization, but to employ **hierarchical optimization** to manage the complexity of the market, potentially utilizing distributed layers only where trust and verification are more critical than execution speed.

---

### References

*   **[cite: 1]** Zeng, X., Peng, H., Su, D., & Li, A. (2025). *Effective Reinforcement Learning Based on Structural Information Principles*. Journal of Machine Learning Research.
*   **[cite: 11, 12]** Research on Entropy-Fuzzy TOPSIS Model for Portfolio Investment. (2023).
*   **[cite: 10]** *An Entropy-Based Approach to Portfolio Optimization*. (2020).
*   **[cite: 8]** Bera, A. K., & Park, S. Y. (2005). *Optimal Portfolio Diversification Using the Maximum Entropy Principle*.
*   **[cite: 2]** Pajo, P. (2025). *Hierarchical Corporations versus Decentralized Communities: Transaction Cost Economics Perspectives*.
*   **[cite: 15]** Almog, A., & Shmueli, E. (2019). *Structural Entropy: Monitoring Correlation-Based Networks Over Time With Application To Financial Markets*. Scientific Reports.
*   **[cite: 6]** *Hierarchical state abstraction based on structural information principles*. IJCAI Proceedings (2025).
*   **[cite: 7]** *Principle of Maximum Entropy*. Grokipedia.
*   **[cite: 13, 14]** *Enhancing Algorithmic Trading Strategies with Shannon Entropy*. (2025).
*   **[cite: 19]** *Distributed Ledger Technology and Coordination*. (2024).
*   **[cite: 18]** Rindfleisch, A. (2019). *Transaction cost theory: past, present and future*.
*   **[cite: 23]** *Transaction Cost Economics in Digital Contexts*. (2024).
*   **[cite: 17]** *Structural entropy as a key metric for monitoring market stability*. PLOS ONE (2025).
*   **[cite: 3, 4, 5]** Zeng, X., et al. (2024). *SIDM: A Structural Information principles-based framework for hierarchical Decision Making*. arXiv.
*   **[cite: 20]** *Centralized vs. Distributed Network Management*. ZPE Systems.
*   **[cite: 22]** *Organizational structure and project success*. MDPI (2024).

**Sources:**
1. [jmlr.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmWBKKcaQ13CkeQIdaLdcfHQHj4OOZuoNdvo8Piotp7yZJ11-lZecM6g_9y3sdGSdCqCUgvS6BssVU4WfYffpzqNSgsdBs9KPwN8QmHkqXozsmjUHLDH2ssHcGBu4MekRX3Pc7obvxp-Xdx--wyQ==)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1tLhDdVy03naFhmijLijuvxCuixPh2tf-M1U6njPLG17M6CPlKvyqFFcQdRoC4Dger6bZM_G2DNn8ArajKSkdA9f3j5QSRcn7dOE6OomNXuTmeMmvjqmfV1HoS4MiaUNCNcQLnlvQt2HuLPSA6ytAE8aVDEeri4MfPKxgphqysni5LqQt3OpBsbJteVtf3LthmZd_5i8U2z8PRE9LxcbKGCwfvnXd3ZWhXhDeWVB9DIkjguHgNs1hB0gztYtlOCokCHuFVGk49JN1RU_ifzN3MGu8Mwa1L3g2ejhFrd6g_upgaz8F7HxNuBc8iEohaVWXggHZ8LP5CK4rgCS9oYtGgQhp66hNKAMLrYuBJig=)
3. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuW39n5ZCgw_egpKZ9LXuh4SJQoAKF-CRusjuVoNSUfMS09VIgS-yJYDWeQcSCSIJuxQKa4epYYi7WhEH0-xlp54YMeelr4s5uDY_u471YEMj6SD1zfkd62A==)
4. [scribd.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZUVrsC4vM9M7mjc11Y25_glRqLoQ9xsGzHYW-EoWnS2U84J96_WcEFbmKEyCrK_6jtpe2CZ1MAcCri-n4EVaZ9ZqLZLXC8i_aHRuxfoPPjN4VVvSe_M2ayP080Qo0hQQ7DFblP4Iz0PMhemU=)
5. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIZIAEgWCir1kuFUI00BU3B1IlY4Z9rICJTIyArnF94xRAgFskIZ-JBaH9-01GWBJGToM10G2W5ukb__dSoLkYl7UWOCzfdXmffGMO9Y9unu2Fw_AJHA==)
6. [ijcai.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcBOhtc1FiBwQdoE66HoYi1qwGnNqrKsPYfCXITgZAyMhLKt0UzQNbVOv23O_hKPnoyGtwgbjfAMNu5xFl6fT8EWaEeOx98LfxEBOn4BBANHkWDAYWE9UvEK4t83O9Eab1dNdGrA==)
7. [grokipedia.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUrtu3N-5S4IEJl95M81fWzWpij6jlMSXuhvoE01q13vliLH_90ehsx1vfCyVxdbj0f1qj9QOhYw576b8MVSNKhjSc321nSfEh7rsz28mW_Pea2S1Ztdh4MF8K4sCsmAeHt28bpdUMC-orD6pCBw==)
8. [core.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxlsHlVo_geVm3G29EL8hm4Ue3auTfLWGyTU7Wv0Wkpl89_a667wbito9oz6BJdch0y93fVwLQHLx0DBrv-FC-aMmqbMFAgg5i4sZW1MaReaC4m8ytJBtw_5gSl052bzKjcQ==)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpuLbexn-ILwJlNy8ksOjChnM5bZh497MExGOgk5hngC64bhdwpsWkzKSeoCXygXtl5W1Qcp635D_CRCzeYoipuqFvfvSAlLT1OKAPFulBQ3HwEEWg9wG92fE09ng-bRBJU7OeyT1B)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3ZUxeB8Y8lk9M8e5_9e4T0YU0RhJin8P6n_r7Mxw8tUXS40lpxI_7tQGqYHTIluPBHVkcTCjDhKbtjZgEVUA6dO3R_-XMyVVaDDB9vYaaQh0FFoDKTye4fDZhULpGx4KhsoS0Y1I1RsJkjPwzpDIIvQf1UldiyrRfrrdOW7tB5RZgfWAJMXTU90DWn83UpQxV-wZj-sKbCGh1SrQ=)
11. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXdpwtxpKQ6JuDKRk8CiPwvF1fUJRbIIl8dSwnZ0esNl_2EmoK_j3RLetRpgzV-pvygu3EO7vVhpDDlylTwt9cpPnca_u8Sm90-wjiTNlo7wM3IfAD6b4Usho3884=)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5N32gLnJLa82zPgOQWnrSesYSfootJxT4Y9b-CxBNUof5ocRWJflzk2o0Tmxpuj16amIDzzFWJhYwtuAnPKhK7YBABa7MbBDTCRLsGMkALs9MbsALqq6x1bMsGAfDXp9WQ6MVxZPWGjTumLglg8klswlLF4unaQYbMG5lH_tT2LP7bjYxC7BEL_QH7jQvDjeKNb6BYop5zR_foJrdNGM114Fm1OSmD44LU744MSlocetPdTxz-0APZCHQsR4_Awp4Hkyu5qC7uZJz9GpO7nmBTg==)
13. [preprints.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZuazXhIO7vTgR0-aSIFEZnVNcxcOWxx2s3dcQOv8kJbujebCdbARxpyFWz_IgEQEv4MPe4Hd2gqm8Mtg4CJYL9SJYkXHFG7aZ2hCvUTK_hmhTQdF_FXfXQPXaGi7L50FBdvK4Wto=)
14. [preprints.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_ROehF36Qdv-kvRGdK6DZVsEit4yN6ZIiyrZNo4PFfPH8jEKClaBy7uSpfEO66PCTXd2ZFUcAp-_tObU7dvNUwuwi2rTDR5hJQ_5p5DGz8FAmWVQv8SJUHzygkR7O3kK3JRic1__qN80=)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIyLVmDKqFRonlRenSclR1TWxbTT4tYJmmSjRyr7_-eoAXFVSJxPPPojJEy38M_VdJhNjFvb8ICPdWJuxSFaTNc7u6Y2W5gC4E0W66l2daXsiw4mEIII3tZPvcTyJlnPfuz0SpKTt0jWEE2EKOhEWvNXXaQTCieIXFRRqSE05rk0CvVMUbeopf-BUFTcJWi9Y5LhSHuKf40dsWMxULa9b1vGHF7JFhJcruR7-CSrQCEWFwkRI9-kecN6tGeKB-6r1TGj4fnGUpOJl3AffmcSU6adQ=)
16. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEigztUeUtWc00__1A_dYm0kp8VuqEsnHTvfM_vcnin-mDLW4NZBtkC7wrt5wUpUDx9MnGb4wB4d4b7xJgNHqCWi1zfnSL7hyDw0q-r3l5C2C_6-xOhYEd7Z7Mfq6Y9CcO3cZNIvtGsKg==)
17. [plos.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTg4ta949ePhIQ76nA676Dbh1X_xw-n7KEsaX62NlWi37Cdp5PhGC71xVH_Xoq5UiRLI2WoClbTEkOXwPqcES1_WcGktrO0VhYB6X8KxHIRzs-RR_P29aRjtwml9w25QkVEf7tAfTEttKaeepyvzp5_9chXPaVjvhdrI-G15xE)
18. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmIbcPw1A6LvKk7Fxy7phid8OA_2tNyIet7v2fNMMVmyOYGT2qkZW3hM2t6cIKhV6c_a-VhSe20WGoWK4lz6IYeb1FqmirzGg9BZ5CEQL1X8HaXjZ_LfxYHzRBghkKDIjrLsJIukcMVyNveKsDe_dQBl9BCMzZgUC42I571zRJZyixgUKspBxE4REXdDKlTZClI6upolUtnQ==)
19. [econstor.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYCH8_-HekccU7ceQWJGRQ4DTJNvMD_a5oDcAkuOHZQ6qoY74cJSP-xkZl1qt5v1_DtWSC8FNBcEpnoR3FB_2ZL5Pdiao7pQ2ZWdoP2EjbgGAIf3mew93g78721121ay5836WkcJheu68yyBzLyXgxCEtVp4t7jMnQALL_KXrdW_E=)
20. [zpesystems.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvg4RhKo3PLdxGFt5jzQrURJHXojafa4Q0wTSmgu9KByKhi2fhdQY8q9ANYNeMxiUTL4Uh2u_MH7AwtzOIGYOKovuFLhbBNYPxpl0Nk54PxvOD_OQ2Q_Y8JKMS6UAf2C1fnOwZ_z-qPG0Lx6NTXLA1cWhS780_SM8i5xn-4e0=)
21. [liveaction.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH19L5MnAJAeXtnj4o4OLlqZOwZykcNxwnTo60RVZTKBAZ497QcaxLHZ6GRZjTEy_NoI_lqgycXpmeIGhwGsKayvOPBzrHSZWZwf7XcTQYlhupmgJQ-0Kb3EY7yPJ7EAFQ_3rGpGAjUjNuXum_6BltMaZVJO2Szo-HTW63o7G5HzuBFzy2qlLsb4Xq-piTvl2mYvD_Ib4iUHHUZhy53l_kINs_YmUcvSs1behfRtA==)
22. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyeYlJqffwyI-ATMMQX1tPZ-Bt2qqDsCQotaKyuDk3InN3ppQxZZmKl5Diw5dDKEQu8DuAeay2HQWXzF0E8_dwTODNB5K4ZS-gpaJtcrYmmTNbLuUok9266PJ4NAs=)
23. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIHA4yJS7da030bwh8ej5Z7OR5pLli3jfP3v3dpzGR0fXYiTBU9IA85qT5QQ-W8gLm81XI5UDhkOfg_rurNSnBXQvh3wGLbRrvyl6dOUcMg5JBBMTrv0yDFEVfElQ=)
24. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvqhPGP8myQuImEauomcb3MLgOF30pczSa90O3fiXO6UMlsemOFhB961B_pvnfxIv-zPtzRW_K6Ot0UIRbrHqlfNmLGk9sYMXha9fZBDe2QIA5jUhUrA4ZAy73NVqVZ8-lVoFbzCYj8NmzZKh7s_jF8GrCudpKp608OXo=)


## Annotations
Annotation(end_index=3165, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmWBKKcaQ13CkeQIdaLdcfHQHj4OOZuoNdvo8Piotp7yZJ11-lZecM6g_9y3sdGSdCqCUgvS6BssVU4WfYffpzqNSgsdBs9KPwN8QmHkqXozsmjUHLDH2ssHcGBu4MekRX3Pc7obvxp-Xdx--wyQ==', start_index=3156)
Annotation(end_index=3512, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1tLhDdVy03naFhmijLijuvxCuixPh2tf-M1U6njPLG17M6CPlKvyqFFcQdRoC4Dger6bZM_G2DNn8ArajKSkdA9f3j5QSRcn7dOE6OomNXuTmeMmvjqmfV1HoS4MiaUNCNcQLnlvQt2HuLPSA6ytAE8aVDEeri4MfPKxgphqysni5LqQt3OpBsbJteVtf3LthmZd_5i8U2z8PRE9LxcbKGCwfvnXd3ZWhXhDeWVB9DIkjguHgNs1hB0gztYtlOCokCHuFVGk49JN1RU_ifzN3MGu8Mwa1L3g2ejhFrd6g_upgaz8F7HxNuBc8iEohaVWXggHZ8LP5CK4rgCS9oYtGgQhp66hNKAMLrYuBJig=', start_index=3503)
Annotation(end_index=5380, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuW39n5ZCgw_egpKZ9LXuh4SJQoAKF-CRusjuVoNSUfMS09VIgS-yJYDWeQcSCSIJuxQKa4epYYi7WhEH0-xlp54YMeelr4s5uDY_u471YEMj6SD1zfkd62A==', start_index=5368)
Annotation(end_index=5380, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZUVrsC4vM9M7mjc11Y25_glRqLoQ9xsGzHYW-EoWnS2U84J96_WcEFbmKEyCrK_6jtpe2CZ1MAcCri-n4EVaZ9ZqLZLXC8i_aHRuxfoPPjN4VVvSe_M2ayP080Qo0hQQ7DFblP4Iz0PMhemU=', start_index=5368)
Annotation(end_index=5726, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIZIAEgWCir1kuFUI00BU3B1IlY4Z9rICJTIyArnF94xRAgFskIZ-JBaH9-01GWBJGToM10G2W5ukb__dSoLkYl7UWOCzfdXmffGMO9Y9unu2Fw_AJHA==', start_index=5717)
Annotation(end_index=6052, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmWBKKcaQ13CkeQIdaLdcfHQHj4OOZuoNdvo8Piotp7yZJ11-lZecM6g_9y3sdGSdCqCUgvS6BssVU4WfYffpzqNSgsdBs9KPwN8QmHkqXozsmjUHLDH2ssHcGBu4MekRX3Pc7obvxp-Xdx--wyQ==', start_index=6043)
Annotation(end_index=6163, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuW39n5ZCgw_egpKZ9LXuh4SJQoAKF-CRusjuVoNSUfMS09VIgS-yJYDWeQcSCSIJuxQKa4epYYi7WhEH0-xlp54YMeelr4s5uDY_u471YEMj6SD1zfkd62A==', start_index=6154)
Annotation(end_index=6252, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZUVrsC4vM9M7mjc11Y25_glRqLoQ9xsGzHYW-EoWnS2U84J96_WcEFbmKEyCrK_6jtpe2CZ1MAcCri-n4EVaZ9ZqLZLXC8i_aHRuxfoPPjN4VVvSe_M2ayP080Qo0hQQ7DFblP4Iz0PMhemU=', start_index=6243)
Annotation(end_index=7012, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmWBKKcaQ13CkeQIdaLdcfHQHj4OOZuoNdvo8Piotp7yZJ11-lZecM6g_9y3sdGSdCqCUgvS6BssVU4WfYffpzqNSgsdBs9KPwN8QmHkqXozsmjUHLDH2ssHcGBu4MekRX3Pc7obvxp-Xdx--wyQ==', start_index=7003)
Annotation(end_index=7394, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcBOhtc1FiBwQdoE66HoYi1qwGnNqrKsPYfCXITgZAyMhLKt0UzQNbVOv23O_hKPnoyGtwgbjfAMNu5xFl6fT8EWaEeOx98LfxEBOn4BBANHkWDAYWE9UvEK4t83O9Eab1dNdGrA==', start_index=7385)
Annotation(end_index=8531, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUrtu3N-5S4IEJl95M81fWzWpij6jlMSXuhvoE01q13vliLH_90ehsx1vfCyVxdbj0f1qj9QOhYw576b8MVSNKhjSc321nSfEh7rsz28mW_Pea2S1Ztdh4MF8K4sCsmAeHt28bpdUMC-orD6pCBw==', start_index=8522)
Annotation(end_index=8900, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpuLbexn-ILwJlNy8ksOjChnM5bZh497MExGOgk5hngC64bhdwpsWkzKSeoCXygXtl5W1Qcp635D_CRCzeYoipuqFvfvSAlLT1OKAPFulBQ3HwEEWg9wG92fE09ng-bRBJU7OeyT1B', start_index=8888)
Annotation(end_index=8900, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxlsHlVo_geVm3G29EL8hm4Ue3auTfLWGyTU7Wv0Wkpl89_a667wbito9oz6BJdch0y93fVwLQHLx0DBrv-FC-aMmqbMFAgg5i4sZW1MaReaC4m8ytJBtw_5gSl052bzKjcQ==', start_index=8888)
Annotation(end_index=9166, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3ZUxeB8Y8lk9M8e5_9e4T0YU0RhJin8P6n_r7Mxw8tUXS40lpxI_7tQGqYHTIluPBHVkcTCjDhKbtjZgEVUA6dO3R_-XMyVVaDDB9vYaaQh0FFoDKTye4fDZhULpGx4KhsoS0Y1I1RsJkjPwzpDIIvQf1UldiyrRfrrdOW7tB5RZgfWAJMXTU90DWn83UpQxV-wZj-sKbCGh1SrQ=', start_index=9156)
Annotation(end_index=9344, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5N32gLnJLa82zPgOQWnrSesYSfootJxT4Y9b-CxBNUof5ocRWJflzk2o0Tmxpuj16amIDzzFWJhYwtuAnPKhK7YBABa7MbBDTCRLsGMkALs9MbsALqq6x1bMsGAfDXp9WQ6MVxZPWGjTumLglg8klswlLF4unaQYbMG5lH_tT2LP7bjYxC7BEL_QH7jQvDjeKNb6BYop5zR_foJrdNGM114Fm1OSmD44LU744MSlocetPdTxz-0APZCHQsR4_Awp4Hkyu5qC7uZJz9GpO7nmBTg==', start_index=9330)
Annotation(end_index=9344, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXdpwtxpKQ6JuDKRk8CiPwvF1fUJRbIIl8dSwnZ0esNl_2EmoK_j3RLetRpgzV-pvygu3EO7vVhpDDlylTwt9cpPnca_u8Sm90-wjiTNlo7wM3IfAD6b4Usho3884=', start_index=9330)
Annotation(end_index=9733, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZuazXhIO7vTgR0-aSIFEZnVNcxcOWxx2s3dcQOv8kJbujebCdbARxpyFWz_IgEQEv4MPe4Hd2gqm8Mtg4CJYL9SJYkXHFG7aZ2hCvUTK_hmhTQdF_FXfXQPXaGi7L50FBdvK4Wto=', start_index=9719)
Annotation(end_index=9733, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_ROehF36Qdv-kvRGdK6DZVsEit4yN6ZIiyrZNo4PFfPH8jEKClaBy7uSpfEO66PCTXd2ZFUcAp-_tObU7dvNUwuwi2rTDR5hJQ_5p5DGz8FAmWVQv8SJUHzygkR7O3kK3JRic1__qN80=', start_index=9719)
Annotation(end_index=10449, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEigztUeUtWc00__1A_dYm0kp8VuqEsnHTvfM_vcnin-mDLW4NZBtkC7wrt5wUpUDx9MnGb4wB4d4b7xJgNHqCWi1zfnSL7hyDw0q-r3l5C2C_6-xOhYEd7Z7Mfq6Y9CcO3cZNIvtGsKg==', start_index=10431)
Annotation(end_index=10449, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIyLVmDKqFRonlRenSclR1TWxbTT4tYJmmSjRyr7_-eoAXFVSJxPPPojJEy38M_VdJhNjFvb8ICPdWJuxSFaTNc7u6Y2W5gC4E0W66l2daXsiw4mEIII3tZPvcTyJlnPfuz0SpKTt0jWEE2EKOhEWvNXXaQTCieIXFRRqSE05rk0CvVMUbeopf-BUFTcJWi9Y5LhSHuKf40dsWMxULa9b1vGHF7JFhJcruR7-CSrQCEWFwkRI9-kecN6tGeKB-6r1TGj4fnGUpOJl3AffmcSU6adQ=', start_index=10431)
Annotation(end_index=10449, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTg4ta949ePhIQ76nA676Dbh1X_xw-n7KEsaX62NlWi37Cdp5PhGC71xVH_Xoq5UiRLI2WoClbTEkOXwPqcES1_WcGktrO0VhYB6X8KxHIRzs-RR_P29aRjtwml9w25QkVEf7tAfTEttKaeepyvzp5_9chXPaVjvhdrI-G15xE', start_index=10431)
Annotation(end_index=10662, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTg4ta949ePhIQ76nA676Dbh1X_xw-n7KEsaX62NlWi37Cdp5PhGC71xVH_Xoq5UiRLI2WoClbTEkOXwPqcES1_WcGktrO0VhYB6X8KxHIRzs-RR_P29aRjtwml9w25QkVEf7tAfTEttKaeepyvzp5_9chXPaVjvhdrI-G15xE', start_index=10652)
Annotation(end_index=11794, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmIbcPw1A6LvKk7Fxy7phid8OA_2tNyIet7v2fNMMVmyOYGT2qkZW3hM2t6cIKhV6c_a-VhSe20WGoWK4lz6IYeb1FqmirzGg9BZ5CEQL1X8HaXjZ_LfxYHzRBghkKDIjrLsJIukcMVyNveKsDe_dQBl9BCMzZgUC42I571zRJZyixgUKspBxE4REXdDKlTZClI6upolUtnQ==', start_index=11781)
Annotation(end_index=11794, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1tLhDdVy03naFhmijLijuvxCuixPh2tf-M1U6njPLG17M6CPlKvyqFFcQdRoC4Dger6bZM_G2DNn8ArajKSkdA9f3j5QSRcn7dOE6OomNXuTmeMmvjqmfV1HoS4MiaUNCNcQLnlvQt2HuLPSA6ytAE8aVDEeri4MfPKxgphqysni5LqQt3OpBsbJteVtf3LthmZd_5i8U2z8PRE9LxcbKGCwfvnXd3ZWhXhDeWVB9DIkjguHgNs1hB0gztYtlOCokCHuFVGk49JN1RU_ifzN3MGu8Mwa1L3g2ejhFrd6g_upgaz8F7HxNuBc8iEohaVWXggHZ8LP5CK4rgCS9oYtGgQhp66hNKAMLrYuBJig=', start_index=11781)
Annotation(end_index=12363, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1tLhDdVy03naFhmijLijuvxCuixPh2tf-M1U6njPLG17M6CPlKvyqFFcQdRoC4Dger6bZM_G2DNn8ArajKSkdA9f3j5QSRcn7dOE6OomNXuTmeMmvjqmfV1HoS4MiaUNCNcQLnlvQt2HuLPSA6ytAE8aVDEeri4MfPKxgphqysni5LqQt3OpBsbJteVtf3LthmZd_5i8U2z8PRE9LxcbKGCwfvnXd3ZWhXhDeWVB9DIkjguHgNs1hB0gztYtlOCokCHuFVGk49JN1RU_ifzN3MGu8Mwa1L3g2ejhFrd6g_upgaz8F7HxNuBc8iEohaVWXggHZ8LP5CK4rgCS9oYtGgQhp66hNKAMLrYuBJig=', start_index=12354)
Annotation(end_index=12911, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYCH8_-HekccU7ceQWJGRQ4DTJNvMD_a5oDcAkuOHZQ6qoY74cJSP-xkZl1qt5v1_DtWSC8FNBcEpnoR3FB_2ZL5Pdiao7pQ2ZWdoP2EjbgGAIf3mew93g78721121ay5836WkcJheu68yyBzLyXgxCEtVp4t7jMnQALL_KXrdW_E=', start_index=12897)
Annotation(end_index=12911, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvg4RhKo3PLdxGFt5jzQrURJHXojafa4Q0wTSmgu9KByKhi2fhdQY8q9ANYNeMxiUTL4Uh2u_MH7AwtzOIGYOKovuFLhbBNYPxpl0Nk54PxvOD_OQ2Q_Y8JKMS6UAf2C1fnOwZ_z-qPG0Lx6NTXLA1cWhS780_SM8i5xn-4e0=', start_index=12897)
Annotation(end_index=13168, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1tLhDdVy03naFhmijLijuvxCuixPh2tf-M1U6njPLG17M6CPlKvyqFFcQdRoC4Dger6bZM_G2DNn8ArajKSkdA9f3j5QSRcn7dOE6OomNXuTmeMmvjqmfV1HoS4MiaUNCNcQLnlvQt2HuLPSA6ytAE8aVDEeri4MfPKxgphqysni5LqQt3OpBsbJteVtf3LthmZd_5i8U2z8PRE9LxcbKGCwfvnXd3ZWhXhDeWVB9DIkjguHgNs1hB0gztYtlOCokCHuFVGk49JN1RU_ifzN3MGu8Mwa1L3g2ejhFrd6g_upgaz8F7HxNuBc8iEohaVWXggHZ8LP5CK4rgCS9oYtGgQhp66hNKAMLrYuBJig=', start_index=13159)
Annotation(end_index=13596, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH19L5MnAJAeXtnj4o4OLlqZOwZykcNxwnTo60RVZTKBAZ497QcaxLHZ6GRZjTEy_NoI_lqgycXpmeIGhwGsKayvOPBzrHSZWZwf7XcTQYlhupmgJQ-0Kb3EY7yPJ7EAFQ_3rGpGAjUjNuXum_6BltMaZVJO2Szo-HTW63o7G5HzuBFzy2qlLsb4Xq-piTvl2mYvD_Ib4iUHHUZhy53l_kINs_YmUcvSs1behfRtA==', start_index=13582)
Annotation(end_index=13596, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvg4RhKo3PLdxGFt5jzQrURJHXojafa4Q0wTSmgu9KByKhi2fhdQY8q9ANYNeMxiUTL4Uh2u_MH7AwtzOIGYOKovuFLhbBNYPxpl0Nk54PxvOD_OQ2Q_Y8JKMS6UAf2C1fnOwZ_z-qPG0Lx6NTXLA1cWhS780_SM8i5xn-4e0=', start_index=13582)
Annotation(end_index=13847, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyeYlJqffwyI-ATMMQX1tPZ-Bt2qqDsCQotaKyuDk3InN3ppQxZZmKl5Diw5dDKEQu8DuAeay2HQWXzF0E8_dwTODNB5K4ZS-gpaJtcrYmmTNbLuUok9266PJ4NAs=', start_index=13837)
Annotation(end_index=14161, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIHA4yJS7da030bwh8ej5Z7OR5pLli3jfP3v3dpzGR0fXYiTBU9IA85qT5QQ-W8gLm81XI5UDhkOfg_rurNSnBXQvh3wGLbRrvyl6dOUcMg5JBBMTrv0yDFEVfElQ=', start_index=14151)
Annotation(end_index=14748, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1tLhDdVy03naFhmijLijuvxCuixPh2tf-M1U6njPLG17M6CPlKvyqFFcQdRoC4Dger6bZM_G2DNn8ArajKSkdA9f3j5QSRcn7dOE6OomNXuTmeMmvjqmfV1HoS4MiaUNCNcQLnlvQt2HuLPSA6ytAE8aVDEeri4MfPKxgphqysni5LqQt3OpBsbJteVtf3LthmZd_5i8U2z8PRE9LxcbKGCwfvnXd3ZWhXhDeWVB9DIkjguHgNs1hB0gztYtlOCokCHuFVGk49JN1RU_ifzN3MGu8Mwa1L3g2ejhFrd6g_upgaz8F7HxNuBc8iEohaVWXggHZ8LP5CK4rgCS9oYtGgQhp66hNKAMLrYuBJig=', start_index=14739)
Annotation(end_index=15577, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmWBKKcaQ13CkeQIdaLdcfHQHj4OOZuoNdvo8Piotp7yZJ11-lZecM6g_9y3sdGSdCqCUgvS6BssVU4WfYffpzqNSgsdBs9KPwN8QmHkqXozsmjUHLDH2ssHcGBu4MekRX3Pc7obvxp-Xdx--wyQ==', start_index=15568)
Annotation(end_index=16590, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvqhPGP8myQuImEauomcb3MLgOF30pczSa90O3fiXO6UMlsemOFhB961B_pvnfxIv-zPtzRW_K6Ot0UIRbrHqlfNmLGk9sYMXha9fZBDe2QIA5jUhUrA4ZAy73NVqVZ8-lVoFbzCYj8NmzZKh7s_jF8GrCudpKp608OXo=', start_index=16577)
Annotation(end_index=16590, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1tLhDdVy03naFhmijLijuvxCuixPh2tf-M1U6njPLG17M6CPlKvyqFFcQdRoC4Dger6bZM_G2DNn8ArajKSkdA9f3j5QSRcn7dOE6OomNXuTmeMmvjqmfV1HoS4MiaUNCNcQLnlvQt2HuLPSA6ytAE8aVDEeri4MfPKxgphqysni5LqQt3OpBsbJteVtf3LthmZd_5i8U2z8PRE9LxcbKGCwfvnXd3ZWhXhDeWVB9DIkjguHgNs1hB0gztYtlOCokCHuFVGk49JN1RU_ifzN3MGu8Mwa1L3g2ejhFrd6g_upgaz8F7HxNuBc8iEohaVWXggHZ8LP5CK4rgCS9oYtGgQhp66hNKAMLrYuBJig=', start_index=16577)
Annotation(end_index=18868, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmWBKKcaQ13CkeQIdaLdcfHQHj4OOZuoNdvo8Piotp7yZJ11-lZecM6g_9y3sdGSdCqCUgvS6BssVU4WfYffpzqNSgsdBs9KPwN8QmHkqXozsmjUHLDH2ssHcGBu4MekRX3Pc7obvxp-Xdx--wyQ==', start_index=18859)
Annotation(end_index=19053, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5N32gLnJLa82zPgOQWnrSesYSfootJxT4Y9b-CxBNUof5ocRWJflzk2o0Tmxpuj16amIDzzFWJhYwtuAnPKhK7YBABa7MbBDTCRLsGMkALs9MbsALqq6x1bMsGAfDXp9WQ6MVxZPWGjTumLglg8klswlLF4unaQYbMG5lH_tT2LP7bjYxC7BEL_QH7jQvDjeKNb6BYop5zR_foJrdNGM114Fm1OSmD44LU744MSlocetPdTxz-0APZCHQsR4_Awp4Hkyu5qC7uZJz9GpO7nmBTg==', start_index=19039)
Annotation(end_index=19053, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFXdpwtxpKQ6JuDKRk8CiPwvF1fUJRbIIl8dSwnZ0esNl_2EmoK_j3RLetRpgzV-pvygu3EO7vVhpDDlylTwt9cpPnca_u8Sm90-wjiTNlo7wM3IfAD6b4Usho3884=', start_index=19039)
Annotation(end_index=19145, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3ZUxeB8Y8lk9M8e5_9e4T0YU0RhJin8P6n_r7Mxw8tUXS40lpxI_7tQGqYHTIluPBHVkcTCjDhKbtjZgEVUA6dO3R_-XMyVVaDDB9vYaaQh0FFoDKTye4fDZhULpGx4KhsoS0Y1I1RsJkjPwzpDIIvQf1UldiyrRfrrdOW7tB5RZgfWAJMXTU90DWn83UpQxV-wZj-sKbCGh1SrQ=', start_index=19135)
Annotation(end_index=19226, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxlsHlVo_geVm3G29EL8hm4Ue3auTfLWGyTU7Wv0Wkpl89_a667wbito9oz6BJdch0y93fVwLQHLx0DBrv-FC-aMmqbMFAgg5i4sZW1MaReaC4m8ytJBtw_5gSl052bzKjcQ==', start_index=19217)
Annotation(end_index=19352, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH1tLhDdVy03naFhmijLijuvxCuixPh2tf-M1U6njPLG17M6CPlKvyqFFcQdRoC4Dger6bZM_G2DNn8ArajKSkdA9f3j5QSRcn7dOE6OomNXuTmeMmvjqmfV1HoS4MiaUNCNcQLnlvQt2HuLPSA6ytAE8aVDEeri4MfPKxgphqysni5LqQt3OpBsbJteVtf3LthmZd_5i8U2z8PRE9LxcbKGCwfvnXd3ZWhXhDeWVB9DIkjguHgNs1hB0gztYtlOCokCHuFVGk49JN1RU_ifzN3MGu8Mwa1L3g2ejhFrd6g_upgaz8F7HxNuBc8iEohaVWXggHZ8LP5CK4rgCS9oYtGgQhp66hNKAMLrYuBJig=', start_index=19343)
Annotation(end_index=19491, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIyLVmDKqFRonlRenSclR1TWxbTT4tYJmmSjRyr7_-eoAXFVSJxPPPojJEy38M_VdJhNjFvb8ICPdWJuxSFaTNc7u6Y2W5gC4E0W66l2daXsiw4mEIII3tZPvcTyJlnPfuz0SpKTt0jWEE2EKOhEWvNXXaQTCieIXFRRqSE05rk0CvVMUbeopf-BUFTcJWi9Y5LhSHuKf40dsWMxULa9b1vGHF7JFhJcruR7-CSrQCEWFwkRI9-kecN6tGeKB-6r1TGj4fnGUpOJl3AffmcSU6adQ=', start_index=19481)
Annotation(end_index=19671, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcBOhtc1FiBwQdoE66HoYi1qwGnNqrKsPYfCXITgZAyMhLKt0UzQNbVOv23O_hKPnoyGtwgbjfAMNu5xFl6fT8EWaEeOx98LfxEBOn4BBANHkWDAYWE9UvEK4t83O9Eab1dNdGrA==', start_index=19662)
Annotation(end_index=19792, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUrtu3N-5S4IEJl95M81fWzWpij6jlMSXuhvoE01q13vliLH_90ehsx1vfCyVxdbj0f1qj9QOhYw576b8MVSNKhjSc321nSfEh7rsz28mW_Pea2S1Ztdh4MF8K4sCsmAeHt28bpdUMC-orD6pCBw==', start_index=19783)
Annotation(end_index=19859, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZuazXhIO7vTgR0-aSIFEZnVNcxcOWxx2s3dcQOv8kJbujebCdbARxpyFWz_IgEQEv4MPe4Hd2gqm8Mtg4CJYL9SJYkXHFG7aZ2hCvUTK_hmhTQdF_FXfXQPXaGi7L50FBdvK4Wto=', start_index=19845)
Annotation(end_index=19859, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_ROehF36Qdv-kvRGdK6DZVsEit4yN6ZIiyrZNo4PFfPH8jEKClaBy7uSpfEO66PCTXd2ZFUcAp-_tObU7dvNUwuwi2rTDR5hJQ_5p5DGz8FAmWVQv8SJUHzygkR7O3kK3JRic1__qN80=', start_index=19845)
Annotation(end_index=19951, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYCH8_-HekccU7ceQWJGRQ4DTJNvMD_a5oDcAkuOHZQ6qoY74cJSP-xkZl1qt5v1_DtWSC8FNBcEpnoR3FB_2ZL5Pdiao7pQ2ZWdoP2EjbgGAIf3mew93g78721121ay5836WkcJheu68yyBzLyXgxCEtVp4t7jMnQALL_KXrdW_E=', start_index=19941)
Annotation(end_index=20028, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmIbcPw1A6LvKk7Fxy7phid8OA_2tNyIet7v2fNMMVmyOYGT2qkZW3hM2t6cIKhV6c_a-VhSe20WGoWK4lz6IYeb1FqmirzGg9BZ5CEQL1X8HaXjZ_LfxYHzRBghkKDIjrLsJIukcMVyNveKsDe_dQBl9BCMzZgUC42I571zRJZyixgUKspBxE4REXdDKlTZClI6upolUtnQ==', start_index=20018)
Annotation(end_index=20124, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIHA4yJS7da030bwh8ej5Z7OR5pLli3jfP3v3dpzGR0fXYiTBU9IA85qT5QQ-W8gLm81XI5UDhkOfg_rurNSnBXQvh3wGLbRrvyl6dOUcMg5JBBMTrv0yDFEVfElQ=', start_index=20114)
Annotation(end_index=20201, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTg4ta949ePhIQ76nA676Dbh1X_xw-n7KEsaX62NlWi37Cdp5PhGC71xVH_Xoq5UiRLI2WoClbTEkOXwPqcES1_WcGktrO0VhYB6X8KxHIRzs-RR_P29aRjtwml9w25QkVEf7tAfTEttKaeepyvzp5_9chXPaVjvhdrI-G15xE', start_index=20191)
Annotation(end_index=20312, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIZIAEgWCir1kuFUI00BU3B1IlY4Z9rICJTIyArnF94xRAgFskIZ-JBaH9-01GWBJGToM10G2W5ukb__dSoLkYl7UWOCzfdXmffGMO9Y9unu2Fw_AJHA==', start_index=20297)
Annotation(end_index=20312, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuW39n5ZCgw_egpKZ9LXuh4SJQoAKF-CRusjuVoNSUfMS09VIgS-yJYDWeQcSCSIJuxQKa4epYYi7WhEH0-xlp54YMeelr4s5uDY_u471YEMj6SD1zfkd62A==', start_index=20297)
Annotation(end_index=20312, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZUVrsC4vM9M7mjc11Y25_glRqLoQ9xsGzHYW-EoWnS2U84J96_WcEFbmKEyCrK_6jtpe2CZ1MAcCri-n4EVaZ9ZqLZLXC8i_aHRuxfoPPjN4VVvSe_M2ayP080Qo0hQQ7DFblP4Iz0PMhemU=', start_index=20297)
Annotation(end_index=20457, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHvg4RhKo3PLdxGFt5jzQrURJHXojafa4Q0wTSmgu9KByKhi2fhdQY8q9ANYNeMxiUTL4Uh2u_MH7AwtzOIGYOKovuFLhbBNYPxpl0Nk54PxvOD_OQ2Q_Y8JKMS6UAf2C1fnOwZ_z-qPG0Lx6NTXLA1cWhS780_SM8i5xn-4e0=', start_index=20447)
Annotation(end_index=20539, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyeYlJqffwyI-ATMMQX1tPZ-Bt2qqDsCQotaKyuDk3InN3ppQxZZmKl5Diw5dDKEQu8DuAeay2HQWXzF0E8_dwTODNB5K4ZS-gpaJtcrYmmTNbLuUok9266PJ4NAs=', start_index=20529)

## Sources
