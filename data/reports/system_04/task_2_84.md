# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 5b844dfa | **Time:** 280.57s | **Cost:** $1.69287
--------------------------------------------------------------------------------

# Does Inventory Positioning Robustness Decline Nonlinearly with Increasing Network Complexity?

### Key Points
*   **Nonlinear Relationship Confirmed:** Research strongly indicates that the relationship between inventory positioning robustness and network complexity is nonlinear. It often follows an **inverted U-shaped trajectory** or exhibits **threshold effects**, where robustness initially improves with added complexity (redundancy/options) but declines precipitously beyond a specific tipping point due to unmanageable interdependencies.
*   **The "Precipice" of Fragility:** Highly complex supply networks often operate on a "precipice" where they appear stable under normal conditions but suffer discontinuous, catastrophic drops in output and service levels when subjected to idiosyncratic shocks. This is driven by the tight coupling of interdependent nodes where inventory buffers fail to arrest cascading disruptions.
*   **Settling Capacity Thresholds:** In inventory positioning, capacity constraints introduce significant nonlinearities. If available capacity falls below a mathematically defined "settling capacity," standard linear inventory policies fail, causing exponential increases in inventory variability (bullwhip effect) and sharp declines in fill rates.
*   **Bounded Rationality and Control:** As network complexity increases (more nodes, tiers, and SKUs), the cognitive and computational burden of optimizing inventory positioning grows. Beyond a certain level of complexity, the ability to optimally position safety stock degrades, leading to a "dark side of complexity" where theoretical robustness cannot be realized in practice.

### Executive Summary
The robustness of inventory positioning—the strategic placement of safety stock and buffers across a supply chain—does not decline in a linear fashion as network complexity increases. Instead, the relationship is governed by complex, nonlinear dynamics. Initially, increasing structural complexity (adding nodes, alternative routes, and backup suppliers) enhances robustness by providing options and redundancy. However, as the network grows in connectivity and scale, it encounters "tipping points."

Research identifies two primary forms of nonlinear decline: the **inverted U-shape**, where performance peaks at moderate complexity and then degrades, and **threshold-based fragility**, where networks maintain stability until a critical shock magnitude or complexity level causes a systemic collapse. Key drivers of this nonlinearity include the breakdown of risk pooling benefits due to correlation, the amplification of shocks in tightly coupled systems (Normal Accident Theory), and capacity constraints that create bottlenecks which inventory positioning alone cannot mitigate. Consequently, while some complexity is required to achieve robustness, excessive or unmanaged complexity leads to a disproportionate loss of inventory efficacy and service reliability.

---

## 1. Introduction: The Nexus of Complexity and Inventory Robustness

The strategic positioning of inventory is a fundamental lever in supply chain management, serving as the primary buffer against demand uncertainty and supply variability. In simple, linear supply chains, the relationship between inventory levels and service robustness is well-understood and often linear or convex. However, modern supply networks have evolved into intricate, multi-echelon systems characterized by high structural and dynamic complexity. The central question addressed in this report is whether the robustness of inventory positioning declines nonlinearly as this network complexity increases.

### 1.1 Defining the Core Constructs
To address the query, we must operationalize the key terms based on the literature:
*   **Inventory Positioning:** The decision-making process regarding where in the supply chain to hold inventory (e.g., central distribution centers vs. regional warehouses), how much to hold (safety stock levels), and in what form (raw material, WIP, finished goods) [cite: 1, 2].
*   **Network Complexity:** This encompasses **structural complexity** (number of nodes, tiers, and links), **dynamic complexity** (uncertainty in lead times and demand), and **flow complexity** (interactions between material and information flows) [cite: 3, 4, 5].
*   **Robustness:** The capacity of the supply chain to maintain its function (service levels, fill rates) and preserve its structure despite internal or external perturbations [cite: 6, 7].
*   **Nonlinear Decline:** A degradation in performance that accelerates disproportionately relative to the increase in complexity, often manifesting as exponential decay, threshold failures, or regime shifts [cite: 8, 9].

### 1.2 The Shift from Linear to Nonlinear Thinking
Traditional inventory models often assume infinite capacity and linear relationships between nodes. However, recent literature challenges these assumptions, suggesting that real-world constraints and interdependencies create nonlinear behaviors. For instance, the "bullwhip effect" is a classic manifestation of nonlinear instability where small downstream fluctuations create massive upstream volatility [cite: 8]. Understanding these nonlinearities is critical because linear approximations may severely underestimate the risk of stockouts and systemic failure in complex networks.

---

## 2. Theoretical Frameworks of Nonlinearity in Supply Networks

The assertion that inventory robustness declines nonlinearly is supported by several theoretical frameworks that describe how complex systems behave under stress.

### 2.1 Normal Accident Theory (NAT) and Tight Coupling
Normal Accident Theory (NAT) posits that systems which are both **complex** and **tightly coupled** are prone to inevitable, systemic failures.
*   **Complexity:** In a supply chain context, this refers to unplanned and unanticipated interactions between components (e.g., a delay in a Tier 2 supplier affecting a Tier 1 inventory position in an unforeseen way).
*   **Tight Coupling:** This refers to the absence of slack or buffers. While inventory is a form of slack, "lean" practices often reduce these buffers.
*   **Nonlinear Outcome:** Research applying NAT to supply chains suggests that as complexity increases, the potential for "cascading failures" grows nonlinearly. A minor incident in a complex, tightly coupled network does not result in a minor loss of robustness; rather, it can trigger a total collapse of service levels because the interactions propagate the disruption faster than intervention can occur [cite: 10, 11].

### 2.2 The "Precipice" of Fragility
Economic modeling of production networks reveals a phenomenon described as the "precipice" of fragility.
*   **The Mechanism:** Firms in a network source multiple essential inputs. To protect against idiosyncratic failure, they invest in relationship strength (robustness).
*   **The Nonlinear Effect:** Equilibrium models show that supply networks often settle in a state of "intermediate productivity" that is fragile. In this state, the network is highly sensitive to small shocks. A marginal increase in complexity (or a marginal decrease in relationship strength) does not lead to a marginal decline in output; instead, it causes a discontinuous, precipitous drop in aggregate production [cite: 9, 12, 13].
*   **Implication for Inventory:** This suggests that inventory positioning strategies that work well in a moderately complex network may fail completely, rather than gradually, once complexity crosses a critical threshold.

### 2.3 Complex Adaptive Systems (CAS)
Supply chains are viewed as Complex Adaptive Systems, where agents (firms, nodes) interact dynamically.
*   **Emergent Behavior:** In CAS, the aggregate behavior of the system cannot be predicted by summing the behaviors of individual nodes. Nonlinearities arise from feedback loops (e.g., panic ordering) and threshold effects.
*   **Robustness vs. Complexity:** The literature suggests that while some complexity (diversity of suppliers) enhances resilience, "flow complexity" (the number of potential paths) can become a liability if not managed, leading to a nonlinear degradation of control and robustness [cite: 14, 15].

---

## 3. The Mechanics of Nonlinear Decline in Inventory Robustness

Specific mechanisms within inventory management theory explain *why* robustness declines nonlinearly as complexity scales.

### 3.1 Capacity Constraints and "Settling Capacity"
One of the most mathematically rigorous demonstrations of nonlinearity in inventory systems comes from the analysis of capacity constraints.
*   **The Linear Assumption:** Standard inventory models (like the Order-Up-To policy) often assume linear responses to demand signals.
*   **The Nonlinear Reality:** When production or transport capacity is finite, the system becomes nonlinear. Research introduces the concept of **"settling capacity"**—a threshold below which linear approximations fail.
*   **Impact:** If available capacity is below this settling capacity, the system exhibits highly nonlinear behavior. The "bullwhip effect" (inventory variance) does not just increase; it can become unstable. The fill rate (robustness) drops significantly and nonlinearly as capacity tightens or as demand volatility interacts with complex network structures [cite: 8, 16].
*   **Inventory Positioning:** In a complex network with multiple capacity-constrained nodes, the optimal placement of safety stock becomes a non-convex optimization problem. A slight increase in network complexity (e.g., adding a constrained node) can render a previously robust inventory position ineffective [cite: 17].

### 3.2 The Breakdown of Risk Pooling
Inventory pooling (centralization) is a standard strategy to improve robustness. The "Square Root Law" suggests that safety stock increases with the square root of the number of locations (a nonlinear relationship itself).
*   **Complexity's Impact:** As network complexity increases, the assumptions behind effective pooling (independent demand, negligible lead time variance) often break down.
*   **Nonlinear Cost/Risk:** In complex networks, demand streams often become correlated, and lead times become state-dependent (e.g., congestion). This destroys the pooling benefit. The cost to maintain a target robustness level does not rise linearly; it can rise exponentially as the network becomes more complex and the "pooling effect" diminishes [cite: 18, 19, 20].
*   **Inventory Positioning:** Consequently, the robustness provided by a centralized inventory position declines nonlinearly as the network complexity (specifically, the heterogeneity and correlation of demand) increases [cite: 21].

### 3.3 Propagation of Disruptions (The Ripple Effect)
In complex networks, the "ripple effect" describes how a disruption propagates.
*   **Structural Topology:** Research on network topology shows that "scale-free" networks (with hub firms) are robust to random failures but fragile to targeted attacks (or failures of hubs).
*   **Nonlinear Impact:** The loss of a critical node in a complex network does not result in a proportional loss of supply; it can lead to a total cessation of flow to large segments of the network. Inventory positioned downstream becomes useless if the upstream flow is severed, and inventory positioned upstream cannot reach customers if the distribution links fail. The decline in service level is abrupt (nonlinear) rather than gradual [cite: 5, 7].

---

## 4. The Inverted U-Shaped Relationship

A dominant theme in the empirical literature is the **inverted U-shaped relationship** between complexity/inventory practices and performance. This contradicts the idea of a simple monotonic decline, suggesting a more nuanced nonlinear interaction.

### 4.1 Complexity: The "Too Much of a Good Thing" Effect
Research indicates that complexity is not inherently bad; in fact, a certain level of complexity is **required** to achieve robustness.
*   **The Upward Slope (Beneficial Complexity):** Initially, adding complexity in the form of alternative suppliers, backup inventory locations, and multi-modal transport increases robustness. It provides options to hedge against disruption [cite: 22, 23].
*   **The Turning Point:** However, there is a threshold. Beyond this point, the marginal benefit of added complexity is outweighed by the costs of coordination, lack of visibility, and increased probability of error.
*   **The Downward Slope (Detrimental Complexity):** At high levels of complexity, robustness declines. This decline is often nonlinear because the number of interactions grows combinatorially (e.g., adding one node creates multiple new links and feedback loops). Empirical studies confirm this inverted U-shape in contexts ranging from lean inventory practices to financial performance and innovation [cite: 24, 25, 26, 27].

### 4.2 Inventory Leanness and Robustness
The relationship between "lean" inventory (low buffers) and robustness is also nonlinear.
*   **Optimal Leanness:** Moderate leanness improves efficiency without sacrificing much robustness.
*   **Excessive Leanness:** Pushing inventory too low (high leanness) in a complex environment leads to a sharp (nonlinear) increase in fragility. The system loses the ability to absorb even minor shocks. This is described as a curvilinear relationship where performance improves up to a point and then drastically deteriorates [cite: 28, 29].

### 4.3 Bounded Rationality and Management Capacity
The nonlinear decline is also driven by human and organizational limitations.
*   **Cognitive Overload:** Managers have bounded rationality. As supply chain complexity increases linearly, the cognitive load required to manage inventory positioning increases exponentially.
*   **Decision Quality:** When complexity exceeds the "channel capacity" of management (or even standard algorithms), decision quality plummets. This leads to suboptimal inventory positioning (e.g., the "bullwhip effect" caused by panic ordering), resulting in a nonlinear decline in actual robustness compared to theoretical maximums [cite: 25, 30].

---

## 5. Empirical Evidence and Simulation Results

Various studies provide empirical and simulation-based evidence of these nonlinear dynamics.

### 5.1 Simulation of Capacity Constraints
Simulations of capacity-constrained supply chains show that when capacity is tight (high complexity/constraint), the **fill rate** (a measure of robustness) drops nonlinearly.
*   **Findings:** A study comparing linear vs. nonlinear models found that ignoring capacity constraints leads to significant errors. The "settling capacity" acts as a boundary; crossing it triggers a regime shift in inventory performance [cite: 8].
*   **Inventory Variance:** The variance of inventory levels (instability) increases disproportionately as the system approaches its capacity limits [cite: 31].

### 5.2 Network Topology and Disruption
Studies using graph theory and simulation to assess robustness against link failures reveal:
*   **Flow Complexity:** The number of potential transportation links (flow complexity) is the most influential factor. While diversification (complexity) generally helps, the interaction is complex.
*   **Service Level Drop:** In scenarios of targeted attacks on hubs in complex networks, service levels drop sharply (nonlinearly) compared to random failures. This confirms that robustness is highly sensitive to the specific structure of complexity [cite: 5, 7].

### 5.3 The "Dark Side" of Complexity
Empirical research on manufacturing plant performance shows that upstream, internal, and downstream complexity all have negative impacts.
*   **Dynamic vs. Detail Complexity:** Dynamic complexity (variability) has a greater negative impact than detail complexity (number of parts). The interaction of these complexities creates a "dark side" where performance declines are exacerbated [cite: 30, 32].
*   **Inverted U-Shape Validation:** Studies on inventory stickiness and productivity confirm the inverted U-shape, suggesting that deviations from optimal inventory levels in complex environments lead to disproportionate performance penalties [cite: 26, 29].

---

## 6. Managerial Implications: Navigating Nonlinearity

Understanding that the decline in robustness is nonlinear has profound implications for supply chain design and management.

### 6.1 Stress Testing and Threshold Identification
Because the decline is nonlinear, "average" case planning is dangerous.
*   **Stress Testing:** Firms must use "stress testing" (similar to banking) to identify the "precipice" or "settling capacity" of their networks. Measures like "Time to Survive" and "Time to Recover" are critical [cite: 33].
*   **Identifying Tipping Points:** Managers need to identify the complexity threshold where the inverted U-shape turns downward. This requires advanced analytics and digital twins to simulate behavior at the edges of stability [cite: 34, 35].

### 6.2 Managing the Trade-off
*   **Complexity as a Necessity:** Managers should not simply "reduce complexity." Some complexity (redundancy) is required for robustness [cite: 22, 23]. The goal is to optimize complexity to stay at the peak of the inverted U-curve.
*   **Decoupling:** To prevent nonlinear propagation of disruptions (cascading failures), firms should employ "decoupling" strategies—using inventory buffers to isolate distinct sections of the complex network [cite: 6].

### 6.3 Algorithmic Approaches
*   **Nonlinear Programming:** Linear optimization models are insufficient for complex inventory positioning. Mixed-Integer Nonlinear Programming (MINLP) and AI-driven approaches (Reinforcement Learning) are necessary to capture the nonlinear trade-offs between pooling, capacity, and service levels [cite: 18, 36, 37, 38].
*   **Robust Optimization:** Robust optimization techniques that account for "worst-case" scenarios (adversarial nature) tend to favor more uniform inventory distributions, which can be more robust than skewed, cost-optimized distributions in complex networks [cite: 39].

---

## 7. Conclusion

The research results provide a definitive answer: **Yes, inventory positioning robustness declines nonlinearly with increasing network complexity.**

This nonlinearity manifests in three distinct ways:
1.  **Threshold Effects:** Systems remain robust up to a certain level of complexity or constraint (e.g., "settling capacity"), beyond which performance collapses.
2.  **Inverted U-Shaped Trajectory:** Complexity initially aids robustness through redundancy but eventually degrades it through unmanageable interdependencies and cognitive overload.
3.  **Cascading Fragility:** In tightly coupled, complex networks, small shocks can propagate nonlinearly, rendering inventory buffers ineffective and causing systemic failure.

The implication for academia and industry is that linear models and heuristics are increasingly dangerous in modern, high-complexity supply chains. Robustness cannot be assumed to degrade gracefully; it is liable to fail catastrophically if the nonlinear dynamics of the network are not explicitly modeled and managed.

---

## 8. Detailed Analysis of Key Research Findings

### 8.1 The Role of Capacity Constraints in Nonlinearity
A critical finding in the literature is the role of capacity constraints in driving nonlinear behavior. Ponte et al. [cite: 8] demonstrate that the "settling capacity" is a fundamental boundary.
*   **Below Settling Capacity:** The system behaves linearly. Inventory positioning decisions have predictable outcomes.
*   **Above Settling Capacity:** The system enters a nonlinear regime. The "bullwhip effect" is dampened (production smoothing), but **inventory variability** increases. This trade-off is nonlinear; a small reduction in capacity can lead to a massive increase in the stock required to maintain service levels, or a massive drop in service levels if stock is fixed.
*   **Implication:** As network complexity often implies more constrained nodes (bottlenecks), the likelihood of crossing this "settling capacity" threshold increases, driving nonlinear robustness decline.

### 8.2 The "Square Root Law" and Its Limits
The "Square Root Law" of inventory pooling is a foundational concept that describes a nonlinear benefit: $Inventory \propto \sqrt{N}$.
*   **Deviation in Complex Networks:** Research shows that this law holds only under strict assumptions (independence, identical distributions). In complex networks, these assumptions fail.
*   **Nonlinear Cost Escalation:** When demands are correlated (common in complex networks due to common drivers) or when diseconomies of scale exist (congestion), the benefits of pooling diminish nonlinearly. The inventory required to maintain robustness may scale linearly or even super-linearly with complexity, rather than with the square root, representing a relative decline in robustness efficiency [cite: 18, 20].

### 8.3 Structural vs. Dynamic Complexity
It is vital to distinguish between structural and dynamic complexity.
*   **Structural Complexity:** (Number of nodes/links). This has a mixed effect. It can provide robustness (redundancy) but increases management cost [cite: 36, 40].
*   **Dynamic Complexity:** (Variability, uncertainty). This has a uniformly negative, nonlinear impact on robustness. High dynamic complexity makes it exponentially harder to forecast and position inventory correctly [cite: 4, 32].
*   **Interaction:** The interaction of high structural complexity and high dynamic complexity creates the most severe nonlinear declines in robustness (the "dark side" of complexity) [cite: 30].

### 8.4 The "Inverted U" in Financial and Operational Performance
Multiple studies [cite: 25, 26, 29] identify an inverted U-shaped relationship between inventory leanness/complexity and performance.
*   **Mechanism:**
    *   *Low Complexity/High Leanness:* High risk of stockouts, low robustness.
    *   *Moderate Complexity/Leanness:* Optimal balance. Redundancy exists but is manageable.
    *   *High Complexity/Low Leanness:* "Chaos." The system is too complex to manage; inventory is misplaced; robustness declines.
*   **Robustness Check:** This relationship holds across various industries and metrics (productivity, credit ratings, innovation), suggesting it is a fundamental property of complex supply chain systems.

### 8.5 Algorithmic Complexity and Solution Quality
As network complexity increases, the computational complexity of solving the inventory positioning problem (finding the optimal $S_i$ for all nodes $i$) increases nonlinearly (often NP-hard).
*   **Heuristics vs. Optimization:** For simple networks, exact algorithms exist [cite: 1]. For complex networks, firms must rely on heuristics or approximations.
*   **The Gap:** The gap between the *optimal* robust solution and the *implemented* solution grows with complexity. This "optimality gap" represents a nonlinear decline in realized robustness [cite: 1].

---

## 9. Conclusion and Future Directions

The body of research confirms that the relationship between inventory positioning robustness and network complexity is governed by nonlinear dynamics. The "linear intuition" that slightly more complexity leads to slightly less robustness is incorrect and potentially hazardous. Instead, supply chains exhibit **regime shifts**—moving from stable, robust operations to fragile, chaotic states as complexity crosses critical thresholds (settling capacity, cognitive limits, coupling density).

**Future Research Directions:**
*   **Quantifying Thresholds:** More empirical work is needed to quantify the specific "tipping points" for different industries. At what node count or variability level does the inverted U-shape turn downward?
*   **AI and Nonlinear Control:** How can AI and Reinforcement Learning [cite: 37] be used to manage these nonlinearities in real-time, effectively shifting the "settling capacity" curve?
*   **Entropic Measures:** The use of entropy as a measure of supply chain complexity [cite: 41, 42] offers a promising avenue for mathematically modeling the nonlinear decline in robustness.

In summary, inventory positioning robustness declines nonlinearly with increasing network complexity due to the compounding effects of capacity constraints, correlation, cascading failure modes, and bounded rationality.

**Sources:**
1. [mit.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJSADzzIL_uaVKekTnddMP0imMGNq5KdRJWuap4D-pxSU52wi6KfhHxlszBsUngo1QnlFiEGTGsj1xQyUE4xbxcMW0kJbyHSLEMkdUd9CwoXZ8X-J-NcZ6xZKL6wiZqR7ziMtLaDvbzrotQ1bnWaMFThhYQxZqhunS0wT-14NZHx718a1jT_pWNH5uchgR9Plo2PaPpA==)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcLlz6_cJnXBnkwboYRhS0p_CDkx3laV6Dlxp8c8drsx2CdufR-qj8mxNDOCVcemSNrquXdQuxuPdQgYpsC8cYcPDfypFZ52Xc61n3SJh8DA-saYG1rDqneJV6weBCv7EZOWjjoOsnIvg7WD_ejUfUFiOVW4NlqK-6KeJeLH5UHl51p8G2Rb3BzVJCtZFMg5QIGRinu6W43aUMrXQ13EPQWdnjeYDwhVXuRdbzczA1barK)
3. [qmul.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGy4t6PK6J5uJKpjzxaL3YG5hurqVJn361vkUoig0lLEK_YK6_Ave0_v78bgJu3ctVJ7zTVKn1hA_4zgJdmpDo5Y2rt3Q6dDdGHImlilflctkjXn7yafrke7mLdKTXwMmhIvq0DLC-8E6uUeitr47iYXFhN7XTwj_8GGWs73Dgq9ppEdDZ1pjQoISH881LKidmYWkpUZ13T1plE3mC1EhW_y3_1Yo2fsOpnI0MHrjKhvY_yUj4dR7NL)
4. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGK5ace_5ZYIyecMNgqzZCRrugN1_n5HBeg63wGvQiQK_cAJuVatpQhRcce6_f9Z3AOUc9mPikEm-dYiDSqvdn-qdW5BBQBCYqxCuqdNYAZVC0tG2-2AgLjP4HB4NW5j6Wd8JIfG0nBD9952_Q-Le22BmWzGw4f6ofVSbNjbOYfiNaMnz2GLaNzf35f85IkRCCX7Q==)
5. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpPweh1EOPDnjxdz1HjBH4jeI59IJZFfPF-I9jmWAmUiuO43Ocq-2pVKVLeWIL5PMx4vxuIgGlvPdpv3QPEtafF0oLcQW6vY3M_XQE9fokcQARupcZcU46nkTi0DAKVPkm3_kFcrQCPiosXLkJHORSkzWbnJQxMVwmDOj4DsnOjljXynEheLFCL-beITuZamo=)
6. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfFIwXW8ipGRDY_laBvw5O99exBOcErloCu2xSrWD8cWoS1J7JUr_fi8D2HAVjKFTXqCYIMVVemArx3XG2IYI2g9P10zhz_PgEQ4S31TE18Z_nNVoyjtRiReDzj4ETEDBnQGKtRs9fARW37xx7JcIFUfZfKUN2fih48fhxit9EU8E-ZjoeWIwZh07u0o09x6he22MxwzaiL8a_y3YL0w==)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcKp2zdAckz2ur9vIrjsWL3XT6emjIZcwG4n6Gn_9CnQKGwVIfcUhM4zHn6vuKgf8tN50ZjdVq3DLZ-6XwzCWNZ_qXPtflqKyZ9HodxYw7aQxFlK98u-izXVnXPrgMTkMrNA2GxhmXABYrDI1nOXgs02DSGyPcFLoBOPcmUwjf3QsBbXBn1nve-JMeVntoBVjlMNZIN2IAg0h_nA==)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIF2xRxANbmmzfVcd6-iytF1b6-hAbD-kXsz5WZjq0NbN_Yto00xoggC0ydKyNqlPcM9UtY5YK0iXfevS26336rvU16n5b0IJMH46HUoEogtoIHez5UMGX2khpWMH8Z0zNrAI4-C_Io_2ZcTBwmnvghmn56JAg9xfpG2QyR3G7mlZuGmH1YnByMRYLuTi9qa3XJGlTt2C19nT5uc-vQsf2ixPrRI9-v7rD1vWlHxT_)
9. [bengolub.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDufxw4NUJmjmzHkv-yYqn3Or8ewVTOY0Fw-og0gdY-0U5zCqYe7cItOcCmjLNeYgxREjAIq81lk-xfPYTAdOJVKg50Gt35YSgcEkgdc7A5piQssTasJ2uke2cpzbLerc6JVko-9eerRKAkC_sXg==)
10. [ijbms.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGGAe8XRTveX82aULAsfC8Hy9408l6G6fnK6aFYSlPvx-v2ErHijNffUFu396c3jpPOYMHv4Sa7RKqUM_fhXhnkDKvV660Ja9QGnFOdycZkX57vvj3eg34RSYckRG14yTIyZI=)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFT-2ypMMTzrHIDkDUUlHjHf-D5X6Ua86I_knm02uY9Eq5i_ifNBHUzkwxbq52BXmcBwyQnyJEATeyud30FEymkZ1txFEc3XYuTeBdszWmgpfFFtp0I-GMr1DG9dB2skGFOd1dr6bEyr-uafxXuqEGwk4vgAzcpN-MnA7TF158_Ehz9JKfV3WT88I1_dWaKP8xv24IG_VWorwulgretXWZyjUdm4VwWvbrrkB4=)
12. [aeaweb.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZ2KFGXO9SnXvyN_XCjIUsNwADg5GQ2k_s2XOuurovn19Seuj067MMSEk6DhOXz-neQrCef9suVy9rGyuhkHvwDQGVI7zmzLMRhbuhkr08rm_dQtkFLXSdJ7U8HlJf6K8dUGeznZp7AY3k4WK5)
13. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFToi8EMHggE-ZK2Obda1523QMBED928-J8Ly86FFAO5g7d3W9zLgzhdwEJzkD6fsxT_p0lKLwid8DLKpF6w7MRTN11DqSu9b4-L9a9Ffa91_itCllsFNMB56iPtrr6HVDhGwT-bvyjtkvYbE_0v8kGUW-AMXU47DfTKFtmqkznDQuu1NK7x65-TArwxVstZg==)
14. [emerald.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1WLXGaOUjDhQGj4R5pxOWOm9eK0FeUF8ZodDvCwlQ58f7625MyC3-YiRakUNS1WjshPG79g6X7UBLESH32lAW6wYi3r19_RpbBmsFi8UttGro2I8XGqI7qE6qNO2uCrCozHzqXFy22E0TLszPAvPy75x1fW0w_9uC-HRzk48hFvL4A4T4ocEWAGoFGhWq8gZMTsXLMg==)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEpBobbCQge86xG8dPnCnkmmshSkKoyF_oRLAB6xNdptHbfg1qR69aUMb5KU2InVPcNMdKAQFG5omDzv-95oQkSmtoB1gvJk8FQEliRjJ4P1bxPj_wS5vbjnnttvUIUTVzlimADo3bieal4dkAVh4_Bs6Kugpzv2zFpj1V69-casYmbyrRgOURTr9AynxltMVHRmwifpFzC6LPfyxFBlxFh8c=)
16. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESMOh71oafkUTNnrxZ1opZbfzcxFDyihuEzbLGyq9pLyfBQ0leL_47jCnOJlhv-ro3ttWCUUq-DXR64xup7uIB39OMeVfXc5dfXYxKupKC0S4L5DlBWUAsk5IAPkN5jF0UoynmWfokojQygMfORAvGSiKe2-xn7A==)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTMH1t0Wi2gjWxCkR4xscU-zuCv7-OUVYUm9kpiW7wP2HpREAde9IwxPk01lS4FWgI_WHgaRGlbTWMaiUM-sTrgO1_5iIn_qjeVuOj44H-_LKvqFERTrFjGbnOAd_RgaP4z56s3v7QPws7F2tOXm9gMXCxPmMG7y13jLyNj4ep8URn39c_M5qEvoEpHXPSU4cDHq-K8VPK-nnSAo7TeIRWMnwcWgf7AW_3uE-tD-e4dnjTB9Bp7uX36HjjFHzawYsxuwQ4Bs7-dlO73c_zhIhU1pg8-RV7lHHl8ORD4nEdIaPvEv4=)
18. [mit.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP6JliolPSgTGrBZYcPzv0JkbmQRemTF9nartV4PpfzRVSVbQ4zIT8dxPI5KQbKWS-DG-sGmGUGsdZZ9QL6iuWBMsmTYMIZnEDHb-4n83bFyQ5abEX8UIaIvWBZw3dYsBmzGSR15T20uL2zAi-0C9S4WQaIEGL-98pDL5OMNFa1KWL5GELkO_mGkEiNw6mZGYHAN_UR4isQth4N23ZcrqgfNif_zeroSLXS3FjmsXPIlA=)
19. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5wrXDzzCLDkA_cFNavTD2OnhuoyxJ-kOhWeZqK4XgwSDukkzTfju3ftQmrAILYKGbaBSpCB2SKSCBj_NlTkSuzeoMczwTLB6b2w8dGA5JA6sYVgIKOKaHjBZqgEvhefMV_6ZrQjPywXV1h7HVNWQ_rDjD0JrbliY=)
20. [mit.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFb4X0e7DLtKbN4c-zrI5hQ8iNJjGs6SH414z887-vo3A_3FL5wFr0Wentioj9X9TMya0WFAUeexfmgvS_kww91sJqzFUtG0gTiO8tnofPDmuCb6tZUIlpn-vQ7szvR_ljRcbbb4xmxLMkRfzMWZGJqvP2_ZgKYyFMpgFiNVfitXiSkUx5ye7bAIMHjUxdgKZQw5WqkaEdd5Vio6A-uffexaJUMJzgvoqRU-YuQb_DkUfzlq3NYdm14JbL0Z017sCfQfLOk5kSS4TFZUw6JqrDMsWRLtikJFwGIzORVqhXwTlxHb9Xglhvs3ogCjoSuVCRX)
21. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsAaBg5WGDAXFO6Or-UoSwRPqyHsHR3mCedVqcBKFdLlPuwWUirHdz2KQ1RRmCZJ-6Xl9UifRxBlNtioT6H3hrvwx_ESZDV_TYX5ZQ0GcESBE8RpIHCFkpUK5z5Jc=)
22. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWd_Q4yKaVEIzf9SOr6klkhPiSX8zsU_t_HlXf9H5zgBa85RX-gsEfIk8F9WLXDgacZeKYCBOf033i6ygSdSstkCfnqYpG_6stOWmi7sg6W9Lmw1-SfuEP8URh2M9qeAbpPlNogMnUWY3zRneqMvscUwGBATTZZ2oZn2-5aZtJ-ebpThQULCg1v96WHEj9gNlo8I-O89SPcjANfev9PG4br6iSJiMW2JkrGAplvyoTSkcyaJNCV8fg9qC75x9yhl8El-5SRA==)
23. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCPbhoS_z2KIbDPGnpfX8UyNeqgZDN3gwIrb5VHK00IShFAJo3_FYQcGvXS1laqgyc0DusfFQnX8p3sxCgbosszm3Cs0g3yTyg5lojWTgnuZAGWDKdNRrwjA9qbAkPzV_0tVBsVkC4TAQTnFc_29n_mAkzGeyxkQ==)
24. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfnBY8Els_ev8YHwC6MpstZ6_aRpkuVfO_YGXyWNTNjOpNXxZbDwbYOKd_LulHXmcERIbO_PkGji1a0dHV1qSAdT6cKBPEINGnBysSvbvpuLF7I2uH88rJkuHCiPjqJku57E1iYuXCa6wqdnkQ-YEsSaoz3YnfZnZHTN4z8HE01r6TuO-HIW7ME2wMFtmF)
25. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTHMMsWMKowCDZk3WYlTJwLyR2_FVjE0JBcqa3jkQOyv0rZ6yDzZo-7Fioz0pApuafuKY1PWLn7uZwohkcAakCwCFRdNcSR_gim5A3UtkBDwU3_dt_bliOzGbt-apSR12bKybXT2NMIA==)
26. [ktu.lt](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiRc8jkJMv5jdkInvZcWTPlk5Cjw59Tkmo224cbwr2o5AeQHG2Kpg78ieNr9R8aZpPNr-I3uCKnaX68TlewdfevkFeg3hIyQNMIoM2QwhK4N3IWWlxFH1sWk3YyjvqZ4DZ8FmkX7ARcqfzKqRes75WxA==)
27. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENBei8GZdpYCzBtowDBpSyWBmHMs8hSU8vO3anEr9oOFcPE-70cewX4cyr--9fZOwbd0F06BsLk895-CUZtupLFV9VRnvwlySLIed2lDtMMKmsg1Mt8pQu7laE23kXWn_YE8oMklfWX42IMB7_Hzi9fD6ACCmDdrtEFhMMZy1P3SYKLFnFHdOHiYC9h54ivCXeu5mQJvCtsg==)
28. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGl9BEPGO2D0WKMdFurHlSPwSo4-WOY0cssEeOXvYDuwrP7wqles0PKzsb36pNQqouVfpDRw-FNDrxHsYpWfxAtiiIhF6hugfowHrrUKYUOqCkR7DUAKrAfp_YUedPmKw==)
29. [emerald.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEo27Penpy7EMo9wtePWs7mmu3VryokXrPddWs1A_XJ9daKHtMrhhI0u-dfdvyZogrvnCzEce-BKe4yV-CA67xR9kFKTOTYXQgj4wZC_U0vHfWoohoZV8TOYtiNh2vdxBrQa6qFPmqTBo1d1MPegdlbBy0akSqn5HnQ7mljJleSvryfMBpRe21jwvbFiuV6ze2NQyywSfqzWg6Zvp8QFKEOGvasTdzFIbn22A==)
30. [aom.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVSFmh064X6LTDIGcghm6xmzN-CWeJrW62N3Onc4Bhfa-mMPv02gBLTwZLMop3mAruXLOPvg9aaF-bLoMZGbVRHZEhvA0Iql8louyyKd4quRac5_9DzzGVIgiwezdr6JiKzSlGWLTK4g==)
31. [exeter.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUf7-sEtOb1XwF3CVpcDNIAncvVdUBlPHWFYe44r4rhLpGee5GQx6hzmoSDX-Cu696MS6wN22Eq9gpZayjT4Dh7l94PEOXQH_Lq7KgSyVqZ404w57Ro5xaBz17xI1cYut5HCrNm6waZ3s=)
32. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsAVhKRkIbTcUz1bTNVCkUbfy-Hv2tJU_iLdbs37eADmNKmAqg8wlFYdTnND4zLHgjgwmAWqmzLmy_y241edMdOR6nKJcpNOfWe-HTgOP2w_JCX-ud6e8Rxw2z_wNCwIrCv1qrNOaBIzlX2OkEYQsWP05mxSj_68cRcszdhWlWjWsDXOwqG7zUFKORV5LZ9_r8RuUrXkf5zIPHg6KGmIFjG5WYRErVXTYeE8UwqJrgUGk=)
33. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBtMVlAcSCxORYLshvW4hKfW-HJM7tLUUErBB3EhaBYXU4883noDentiXsL8GIVJrdqbXLlKfoVAkyMzm4DpUyDvvsS40Xb45Yb3iHjP8KpFUF7mVBfENhCW2y916Jx9bnsAsxGCAXEfFPLtlQYnf6mpY1hbo4BnI=)
34. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF49zTPsTI4ZsVMJ-Ek6Q-sWHamCP-avPn-qVKC7dQz_DJBVrTKtPDl2IQyeOPOiR3VYIyG22AVDuph16MRkIk5ISgUX_A5ntoL9wTCw334TWqJp-PCElgp_ICzAQ5GcDYE0-F8Srr9fZRPcQ087Euz5RoXENnRB4eBl3jpznZe5EYMAKsCXVQPnPIReUYzbwr1s4AVUiUv1K1GQJH2QVLtZ2ExIFuipg-lMXQ=)
35. [cargoai.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHM0vr3qDX0UqWb8BYWHUoWVz5WB3PScy2FDog_XTphBkMtugXpg1YLimYGLy12UNA05kzuPAR4StSLMSsMaWZ3gEKQTyV3ZBeH6Cm7x6EiBKedQlsJ5nuq0U8EdIDOYLfr126u1g==)
36. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyfMFm0XA2pZD3Zv4uI79AdCJdtMyGUPq8DBEm2mWSK95IZYM42f65cJcSrgM2qSJDWtQLOIqQkHtQqHFx2gTGpaBURVoN44c4ZOwUI6FWkOA5J2LBZ4IQoyNBa0TqXWYWONkkZXJuQcqxJojsFg5izdFUH8SwhIGjBfFwO57kd-0CH4xFFFKhpPXN9K8dCN--vVHLWV_jf4dfcy7hFdUJyL4ynXMFtyFRpbmymGX-hI2J7Gfm3QK2tQFIl4z-)
37. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxBQYt1bBjXGXBexED4z1lK08JrMHYqQTDyWw1s0uuhEpL54TTITpZ1Wo6QdUO3QUGbn3O9PfLyk_yj_XmmLCq3bgAeuFUcBApDANFYxv6Q--IEtV_w21oCKoCqO9v8xtlgWFNYABokf4UQXi4LQbe5S7nG0mhehF7Fs_FSlKyvuBQcGmRNxs9rWrv9J1GRefQTXTntInZB4PuJT48gc4Q-zlhxXPnScPF7GkFvBA2A-aKGuMzBN3O8TaBLNRjFR9S7eA6ujTGPj6YLAIJVbdU3lw=)
38. [hilarispublisher.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFahBFjomkOk-PKTSEiDvoj_bq3bAZzQAjQLlwcoie1ziqkvPYU0soRfiiZmjAjF-k51SbDC94pZrI76oXNjSV76QARvcr22mDRvvZ7LybB_gm3XA6o3sSKp36AXzoZatVLWBCeJDWS-WQqyXB3-JK6wHGJsgyE93d1RCgHTDzVPVH4ElxqCzmor2t9Qa9zmTbZ5Ty5NBI7GW6pvZNNs34p6Sz82dw=)
39. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHf-53juUVyml_-VMfiMuo9mQ12aIBRSq7mJrLJ2MIbooxTux5wNHX-0MP2vm46JkOVfZwUTo-xmsiiSIp9ZvroIhTGlTHf7vUJqrsHDkaOlLBTEioMUQ==)
40. [emerald.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRwGVQZCZcj654fKkrju-2_1l6UYI-QJg5H01Iwhfmhf84GXx9_Fb1cO2lkNYxMAphLGzhGQHjmShCUCT3bo-kqQixVOlgNyoXZS9uJfvxpfh9C0tmGR-D0niRtfIaijHp3IPisuz_XYHpBwNGkWr-XV2vc2K-sKi7hOl6lxxik-bWJkdIlhioHw2IuMsfSGNER51lRrNBGqS7)
41. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoAH0KH-Gml_wAvfLP3GcM40x7iGuGysCZ6qRDQ9puwx-6CFI6Tyjt98X00g7vp2PHBiwEDTFcqNDx7qIadeZ1wWv5xL9Pk7qcAAFtiVcRNaidWvUGPbpYmGWxgMo=)
42. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbH34Xtyol1zRga_F-5f0sSrG-XjDaVsZDXPNBmJzQSkqUZyi21yasCeVqyrYmVAHRNXVCMcUgktaZiY1D-9DYfyGa8Q77kaf_zAKSANnZbSJsZEG5lFuGKqL5DA==)


## Annotations
Annotation(end_index=4052, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJSADzzIL_uaVKekTnddMP0imMGNq5KdRJWuap4D-pxSU52wi6KfhHxlszBsUngo1QnlFiEGTGsj1xQyUE4xbxcMW0kJbyHSLEMkdUd9CwoXZ8X-J-NcZ6xZKL6wiZqR7ziMtLaDvbzrotQ1bnWaMFThhYQxZqhunS0wT-14NZHx718a1jT_pWNH5uchgR9Plo2PaPpA==', start_index=4040)
Annotation(end_index=4052, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcLlz6_cJnXBnkwboYRhS0p_CDkx3laV6Dlxp8c8drsx2CdufR-qj8mxNDOCVcemSNrquXdQuxuPdQgYpsC8cYcPDfypFZ52Xc61n3SJh8DA-saYG1rDqneJV6weBCv7EZOWjjoOsnIvg7WD_ejUfUFiOVW4NlqK-6KeJeLH5UHl51p8G2Rb3BzVJCtZFMg5QIGRinu6W43aUMrXQ13EPQWdnjeYDwhVXuRdbzczA1barK', start_index=4040)
Annotation(end_index=4318, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpPweh1EOPDnjxdz1HjBH4jeI59IJZFfPF-I9jmWAmUiuO43Ocq-2pVKVLeWIL5PMx4vxuIgGlvPdpv3QPEtafF0oLcQW6vY3M_XQE9fokcQARupcZcU46nkTi0DAKVPkm3_kFcrQCPiosXLkJHORSkzWbnJQxMVwmDOj4DsnOjljXynEheLFCL-beITuZamo=', start_index=4303)
Annotation(end_index=4318, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGK5ace_5ZYIyecMNgqzZCRrugN1_n5HBeg63wGvQiQK_cAJuVatpQhRcce6_f9Z3AOUc9mPikEm-dYiDSqvdn-qdW5BBQBCYqxCuqdNYAZVC0tG2-2AgLjP4HB4NW5j6Wd8JIfG0nBD9952_Q-Le22BmWzGw4f6ofVSbNjbOYfiNaMnz2GLaNzf35f85IkRCCX7Q==', start_index=4303)
Annotation(end_index=4318, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGy4t6PK6J5uJKpjzxaL3YG5hurqVJn361vkUoig0lLEK_YK6_Ave0_v78bgJu3ctVJ7zTVKn1hA_4zgJdmpDo5Y2rt3Q6dDdGHImlilflctkjXn7yafrke7mLdKTXwMmhIvq0DLC-8E6uUeitr47iYXFhN7XTwj_8GGWs73Dgq9ppEdDZ1pjQoISH881LKidmYWkpUZ13T1plE3mC1EhW_y3_1Yo2fsOpnI0MHrjKhvY_yUj4dR7NL', start_index=4303)
Annotation(end_index=4509, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfFIwXW8ipGRDY_laBvw5O99exBOcErloCu2xSrWD8cWoS1J7JUr_fi8D2HAVjKFTXqCYIMVVemArx3XG2IYI2g9P10zhz_PgEQ4S31TE18Z_nNVoyjtRiReDzj4ETEDBnQGKtRs9fARW37xx7JcIFUfZfKUN2fih48fhxit9EU8E-ZjoeWIwZh07u0o09x6he22MxwzaiL8a_y3YL0w==', start_index=4497)
Annotation(end_index=4509, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcKp2zdAckz2ur9vIrjsWL3XT6emjIZcwG4n6Gn_9CnQKGwVIfcUhM4zHn6vuKgf8tN50ZjdVq3DLZ-6XwzCWNZ_qXPtflqKyZ9HodxYw7aQxFlK98u-izXVnXPrgMTkMrNA2GxhmXABYrDI1nOXgs02DSGyPcFLoBOPcmUwjf3QsBbXBn1nve-JMeVntoBVjlMNZIN2IAg0h_nA==', start_index=4497)
Annotation(end_index=4732, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDufxw4NUJmjmzHkv-yYqn3Or8ewVTOY0Fw-og0gdY-0U5zCqYe7cItOcCmjLNeYgxREjAIq81lk-xfPYTAdOJVKg50Gt35YSgcEkgdc7A5piQssTasJ2uke2cpzbLerc6JVko-9eerRKAkC_sXg==', start_index=4720)
Annotation(end_index=4732, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIF2xRxANbmmzfVcd6-iytF1b6-hAbD-kXsz5WZjq0NbN_Yto00xoggC0ydKyNqlPcM9UtY5YK0iXfevS26336rvU16n5b0IJMH46HUoEogtoIHez5UMGX2khpWMH8Z0zNrAI4-C_Io_2ZcTBwmnvghmn56JAg9xfpG2QyR3G7mlZuGmH1YnByMRYLuTi9qa3XJGlTt2C19nT5uc-vQsf2ixPrRI9-v7rD1vWlHxT_', start_index=4720)
Annotation(end_index=5201, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIF2xRxANbmmzfVcd6-iytF1b6-hAbD-kXsz5WZjq0NbN_Yto00xoggC0ydKyNqlPcM9UtY5YK0iXfevS26336rvU16n5b0IJMH46HUoEogtoIHez5UMGX2khpWMH8Z0zNrAI4-C_Io_2ZcTBwmnvghmn56JAg9xfpG2QyR3G7mlZuGmH1YnByMRYLuTi9qa3XJGlTt2C19nT5uc-vQsf2ixPrRI9-v7rD1vWlHxT_', start_index=5192)
Annotation(end_index=6600, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGGAe8XRTveX82aULAsfC8Hy9408l6G6fnK6aFYSlPvx-v2ErHijNffUFu396c3jpPOYMHv4Sa7RKqUM_fhXhnkDKvV660Ja9QGnFOdycZkX57vvj3eg34RSYckRG14yTIyZI=', start_index=6586)
Annotation(end_index=6600, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFT-2ypMMTzrHIDkDUUlHjHf-D5X6Ua86I_knm02uY9Eq5i_ifNBHUzkwxbq52BXmcBwyQnyJEATeyud30FEymkZ1txFEc3XYuTeBdszWmgpfFFtp0I-GMr1DG9dB2skGFOd1dr6bEyr-uafxXuqEGwk4vgAzcpN-MnA7TF158_Ehz9JKfV3WT88I1_dWaKP8xv24IG_VWorwulgretXWZyjUdm4VwWvbrrkB4=', start_index=6586)
Annotation(end_index=7350, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDufxw4NUJmjmzHkv-yYqn3Or8ewVTOY0Fw-og0gdY-0U5zCqYe7cItOcCmjLNeYgxREjAIq81lk-xfPYTAdOJVKg50Gt35YSgcEkgdc7A5piQssTasJ2uke2cpzbLerc6JVko-9eerRKAkC_sXg==', start_index=7333)
Annotation(end_index=7350, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFToi8EMHggE-ZK2Obda1523QMBED928-J8Ly86FFAO5g7d3W9zLgzhdwEJzkD6fsxT_p0lKLwid8DLKpF6w7MRTN11DqSu9b4-L9a9Ffa91_itCllsFNMB56iPtrr6HVDhGwT-bvyjtkvYbE_0v8kGUW-AMXU47DfTKFtmqkznDQuu1NK7x65-TArwxVstZg==', start_index=7333)
Annotation(end_index=7350, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFZ2KFGXO9SnXvyN_XCjIUsNwADg5GQ2k_s2XOuurovn19Seuj067MMSEk6DhOXz-neQrCef9suVy9rGyuhkHvwDQGVI7zmzLMRhbuhkr08rm_dQtkFLXSdJ7U8HlJf6K8dUGeznZp7AY3k4WK5', start_index=7333)
Annotation(end_index=8241, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1WLXGaOUjDhQGj4R5pxOWOm9eK0FeUF8ZodDvCwlQ58f7625MyC3-YiRakUNS1WjshPG79g6X7UBLESH32lAW6wYi3r19_RpbBmsFi8UttGro2I8XGqI7qE6qNO2uCrCozHzqXFy22E0TLszPAvPy75x1fW0w_9uC-HRzk48hFvL4A4T4ocEWAGoFGhWq8gZMTsXLMg==', start_index=8227)
Annotation(end_index=8241, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEpBobbCQge86xG8dPnCnkmmshSkKoyF_oRLAB6xNdptHbfg1qR69aUMb5KU2InVPcNMdKAQFG5omDzv-95oQkSmtoB1gvJk8FQEliRjJ4P1bxPj_wS5vbjnnttvUIUTVzlimADo3bieal4dkAVh4_Bs6Kugpzv2zFpj1V69-casYmbyrRgOURTr9AynxltMVHRmwifpFzC6LPfyxFBlxFh8c=', start_index=8227)
Annotation(end_index=9364, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIF2xRxANbmmzfVcd6-iytF1b6-hAbD-kXsz5WZjq0NbN_Yto00xoggC0ydKyNqlPcM9UtY5YK0iXfevS26336rvU16n5b0IJMH46HUoEogtoIHez5UMGX2khpWMH8Z0zNrAI4-C_Io_2ZcTBwmnvghmn56JAg9xfpG2QyR3G7mlZuGmH1YnByMRYLuTi9qa3XJGlTt2C19nT5uc-vQsf2ixPrRI9-v7rD1vWlHxT_', start_index=9351)
Annotation(end_index=9364, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQESMOh71oafkUTNnrxZ1opZbfzcxFDyihuEzbLGyq9pLyfBQ0leL_47jCnOJlhv-ro3ttWCUUq-DXR64xup7uIB39OMeVfXc5dfXYxKupKC0S4L5DlBWUAsk5IAPkN5jF0UoynmWfokojQygMfORAvGSiKe2-xn7A==', start_index=9351)
Annotation(end_index=9687, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTMH1t0Wi2gjWxCkR4xscU-zuCv7-OUVYUm9kpiW7wP2HpREAde9IwxPk01lS4FWgI_WHgaRGlbTWMaiUM-sTrgO1_5iIn_qjeVuOj44H-_LKvqFERTrFjGbnOAd_RgaP4z56s3v7QPws7F2tOXm9gMXCxPmMG7y13jLyNj4ep8URn39c_M5qEvoEpHXPSU4cDHq-K8VPK-nnSAo7TeIRWMnwcWgf7AW_3uE-tD-e4dnjTB9Bp7uX36HjjFHzawYsxuwQ4Bs7-dlO73c_zhIhU1pg8-RV7lHHl8ORD4nEdIaPvEv4=', start_index=9677)
Annotation(end_index=10494, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5wrXDzzCLDkA_cFNavTD2OnhuoyxJ-kOhWeZqK4XgwSDukkzTfju3ftQmrAILYKGbaBSpCB2SKSCBj_NlTkSuzeoMczwTLB6b2w8dGA5JA6sYVgIKOKaHjBZqgEvhefMV_6ZrQjPywXV1h7HVNWQ_rDjD0JrbliY=', start_index=10476)
Annotation(end_index=10494, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFb4X0e7DLtKbN4c-zrI5hQ8iNJjGs6SH414z887-vo3A_3FL5wFr0Wentioj9X9TMya0WFAUeexfmgvS_kww91sJqzFUtG0gTiO8tnofPDmuCb6tZUIlpn-vQ7szvR_ljRcbbb4xmxLMkRfzMWZGJqvP2_ZgKYyFMpgFiNVfitXiSkUx5ye7bAIMHjUxdgKZQw5WqkaEdd5Vio6A-uffexaJUMJzgvoqRU-YuQb_DkUfzlq3NYdm14JbL0Z017sCfQfLOk5kSS4TFZUw6JqrDMsWRLtikJFwGIzORVqhXwTlxHb9Xglhvs3ogCjoSuVCRX', start_index=10476)
Annotation(end_index=10494, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP6JliolPSgTGrBZYcPzv0JkbmQRemTF9nartV4PpfzRVSVbQ4zIT8dxPI5KQbKWS-DG-sGmGUGsdZZ9QL6iuWBMsmTYMIZnEDHb-4n83bFyQ5abEX8UIaIvWBZw3dYsBmzGSR15T20uL2zAi-0C9S4WQaIEGL-98pDL5OMNFa1KWL5GELkO_mGkEiNw6mZGYHAN_UR4isQth4N23ZcrqgfNif_zeroSLXS3FjmsXPIlA=', start_index=10476)
Annotation(end_index=10728, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGsAaBg5WGDAXFO6Or-UoSwRPqyHsHR3mCedVqcBKFdLlPuwWUirHdz2KQ1RRmCZJ-6Xl9UifRxBlNtioT6H3hrvwx_ESZDV_TYX5ZQ0GcESBE8RpIHCFkpUK5z5Jc=', start_index=10718)
Annotation(end_index=11512, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpPweh1EOPDnjxdz1HjBH4jeI59IJZFfPF-I9jmWAmUiuO43Ocq-2pVKVLeWIL5PMx4vxuIgGlvPdpv3QPEtafF0oLcQW6vY3M_XQE9fokcQARupcZcU46nkTi0DAKVPkm3_kFcrQCPiosXLkJHORSkzWbnJQxMVwmDOj4DsnOjljXynEheLFCL-beITuZamo=', start_index=11500)
Annotation(end_index=11512, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcKp2zdAckz2ur9vIrjsWL3XT6emjIZcwG4n6Gn_9CnQKGwVIfcUhM4zHn6vuKgf8tN50ZjdVq3DLZ-6XwzCWNZ_qXPtflqKyZ9HodxYw7aQxFlK98u-izXVnXPrgMTkMrNA2GxhmXABYrDI1nOXgs02DSGyPcFLoBOPcmUwjf3QsBbXBn1nve-JMeVntoBVjlMNZIN2IAg0h_nA==', start_index=11500)
Annotation(end_index=12261, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCPbhoS_z2KIbDPGnpfX8UyNeqgZDN3gwIrb5VHK00IShFAJo3_FYQcGvXS1laqgyc0DusfFQnX8p3sxCgbosszm3Cs0g3yTyg5lojWTgnuZAGWDKdNRrwjA9qbAkPzV_0tVBsVkC4TAQTnFc_29n_mAkzGeyxkQ==', start_index=12247)
Annotation(end_index=12261, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWd_Q4yKaVEIzf9SOr6klkhPiSX8zsU_t_HlXf9H5zgBa85RX-gsEfIk8F9WLXDgacZeKYCBOf033i6ygSdSstkCfnqYpG_6stOWmi7sg6W9Lmw1-SfuEP8URh2M9qeAbpPlNogMnUWY3zRneqMvscUwGBATTZZ2oZn2-5aZtJ-ebpThQULCg1v96WHEj9gNlo8I-O89SPcjANfev9PG4br6iSJiMW2JkrGAplvyoTSkcyaJNCV8fg9qC75x9yhl8El-5SRA==', start_index=12247)
Annotation(end_index=12905, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENBei8GZdpYCzBtowDBpSyWBmHMs8hSU8vO3anEr9oOFcPE-70cewX4cyr--9fZOwbd0F06BsLk895-CUZtupLFV9VRnvwlySLIed2lDtMMKmsg1Mt8pQu7laE23kXWn_YE8oMklfWX42IMB7_Hzi9fD6ACCmDdrtEFhMMZy1P3SYKLFnFHdOHiYC9h54ivCXeu5mQJvCtsg==', start_index=12883)
Annotation(end_index=12905, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfnBY8Els_ev8YHwC6MpstZ6_aRpkuVfO_YGXyWNTNjOpNXxZbDwbYOKd_LulHXmcERIbO_PkGji1a0dHV1qSAdT6cKBPEINGnBysSvbvpuLF7I2uH88rJkuHCiPjqJku57E1iYuXCa6wqdnkQ-YEsSaoz3YnfZnZHTN4z8HE01r6TuO-HIW7ME2wMFtmF', start_index=12883)
Annotation(end_index=12905, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiRc8jkJMv5jdkInvZcWTPlk5Cjw59Tkmo224cbwr2o5AeQHG2Kpg78ieNr9R8aZpPNr-I3uCKnaX68TlewdfevkFeg3hIyQNMIoM2QwhK4N3IWWlxFH1sWk3YyjvqZ4DZ8FmkX7ARcqfzKqRes75WxA==', start_index=12883)
Annotation(end_index=12905, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTHMMsWMKowCDZk3WYlTJwLyR2_FVjE0JBcqa3jkQOyv0rZ6yDzZo-7Fioz0pApuafuKY1PWLn7uZwohkcAakCwCFRdNcSR_gim5A3UtkBDwU3_dt_bliOzGbt-apSR12bKybXT2NMIA==', start_index=12883)
Annotation(end_index=13483, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEo27Penpy7EMo9wtePWs7mmu3VryokXrPddWs1A_XJ9daKHtMrhhI0u-dfdvyZogrvnCzEce-BKe4yV-CA67xR9kFKTOTYXQgj4wZC_U0vHfWoohoZV8TOYtiNh2vdxBrQa6qFPmqTBo1d1MPegdlbBy0akSqn5HnQ7mljJleSvryfMBpRe21jwvbFiuV6ze2NQyywSfqzWg6Zvp8QFKEOGvasTdzFIbn22A==', start_index=13469)
Annotation(end_index=13483, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGl9BEPGO2D0WKMdFurHlSPwSo4-WOY0cssEeOXvYDuwrP7wqles0PKzsb36pNQqouVfpDRw-FNDrxHsYpWfxAtiiIhF6hugfowHrrUKYUOqCkR7DUAKrAfp_YUedPmKw==', start_index=13469)
Annotation(end_index=14160, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTHMMsWMKowCDZk3WYlTJwLyR2_FVjE0JBcqa3jkQOyv0rZ6yDzZo-7Fioz0pApuafuKY1PWLn7uZwohkcAakCwCFRdNcSR_gim5A3UtkBDwU3_dt_bliOzGbt-apSR12bKybXT2NMIA==', start_index=14146)
Annotation(end_index=14160, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVSFmh064X6LTDIGcghm6xmzN-CWeJrW62N3Onc4Bhfa-mMPv02gBLTwZLMop3mAruXLOPvg9aaF-bLoMZGbVRHZEhvA0Iql8louyyKd4quRac5_9DzzGVIgiwezdr6JiKzSlGWLTK4g==', start_index=14146)
Annotation(end_index=14778, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIF2xRxANbmmzfVcd6-iytF1b6-hAbD-kXsz5WZjq0NbN_Yto00xoggC0ydKyNqlPcM9UtY5YK0iXfevS26336rvU16n5b0IJMH46HUoEogtoIHez5UMGX2khpWMH8Z0zNrAI4-C_Io_2ZcTBwmnvghmn56JAg9xfpG2QyR3G7mlZuGmH1YnByMRYLuTi9qa3XJGlTt2C19nT5uc-vQsf2ixPrRI9-v7rD1vWlHxT_', start_index=14769)
Annotation(end_index=14939, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEUf7-sEtOb1XwF3CVpcDNIAncvVdUBlPHWFYe44r4rhLpGee5GQx6hzmoSDX-Cu696MS6wN22Eq9gpZayjT4Dh7l94PEOXQH_Lq7KgSyVqZ404w57Ro5xaBz17xI1cYut5HCrNm6waZ3s=', start_index=14929)
Annotation(end_index=15538, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpPweh1EOPDnjxdz1HjBH4jeI59IJZFfPF-I9jmWAmUiuO43Ocq-2pVKVLeWIL5PMx4vxuIgGlvPdpv3QPEtafF0oLcQW6vY3M_XQE9fokcQARupcZcU46nkTi0DAKVPkm3_kFcrQCPiosXLkJHORSkzWbnJQxMVwmDOj4DsnOjljXynEheLFCL-beITuZamo=', start_index=15526)
Annotation(end_index=15538, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcKp2zdAckz2ur9vIrjsWL3XT6emjIZcwG4n6Gn_9CnQKGwVIfcUhM4zHn6vuKgf8tN50ZjdVq3DLZ-6XwzCWNZ_qXPtflqKyZ9HodxYw7aQxFlK98u-izXVnXPrgMTkMrNA2GxhmXABYrDI1nOXgs02DSGyPcFLoBOPcmUwjf3QsBbXBn1nve-JMeVntoBVjlMNZIN2IAg0h_nA==', start_index=15526)
Annotation(end_index=15978, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsAVhKRkIbTcUz1bTNVCkUbfy-Hv2tJU_iLdbs37eADmNKmAqg8wlFYdTnND4zLHgjgwmAWqmzLmy_y241edMdOR6nKJcpNOfWe-HTgOP2w_JCX-ud6e8Rxw2z_wNCwIrCv1qrNOaBIzlX2OkEYQsWP05mxSj_68cRcszdhWlWjWsDXOwqG7zUFKORV5LZ9_r8RuUrXkf5zIPHg6KGmIFjG5WYRErVXTYeE8UwqJrgUGk=', start_index=15964)
Annotation(end_index=15978, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVSFmh064X6LTDIGcghm6xmzN-CWeJrW62N3Onc4Bhfa-mMPv02gBLTwZLMop3mAruXLOPvg9aaF-bLoMZGbVRHZEhvA0Iql8louyyKd4quRac5_9DzzGVIgiwezdr6JiKzSlGWLTK4g==', start_index=15964)
Annotation(end_index=16238, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiRc8jkJMv5jdkInvZcWTPlk5Cjw59Tkmo224cbwr2o5AeQHG2Kpg78ieNr9R8aZpPNr-I3uCKnaX68TlewdfevkFeg3hIyQNMIoM2QwhK4N3IWWlxFH1sWk3YyjvqZ4DZ8FmkX7ARcqfzKqRes75WxA==', start_index=16224)
Annotation(end_index=16238, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEo27Penpy7EMo9wtePWs7mmu3VryokXrPddWs1A_XJ9daKHtMrhhI0u-dfdvyZogrvnCzEce-BKe4yV-CA67xR9kFKTOTYXQgj4wZC_U0vHfWoohoZV8TOYtiNh2vdxBrQa6qFPmqTBo1d1MPegdlbBy0akSqn5HnQ7mljJleSvryfMBpRe21jwvbFiuV6ze2NQyywSfqzWg6Zvp8QFKEOGvasTdzFIbn22A==', start_index=16224)
Annotation(end_index=16775, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBtMVlAcSCxORYLshvW4hKfW-HJM7tLUUErBB3EhaBYXU4883noDentiXsL8GIVJrdqbXLlKfoVAkyMzm4DpUyDvvsS40Xb45Yb3iHjP8KpFUF7mVBfENhCW2y916Jx9bnsAsxGCAXEfFPLtlQYnf6mpY1hbo4BnI=', start_index=16765)
Annotation(end_index=17019, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF49zTPsTI4ZsVMJ-Ek6Q-sWHamCP-avPn-qVKC7dQz_DJBVrTKtPDl2IQyeOPOiR3VYIyG22AVDuph16MRkIk5ISgUX_A5ntoL9wTCw334TWqJp-PCElgp_ICzAQ5GcDYE0-F8Srr9fZRPcQ087Euz5RoXENnRB4eBl3jpznZe5EYMAKsCXVQPnPIReUYzbwr1s4AVUiUv1K1GQJH2QVLtZ2ExIFuipg-lMXQ=', start_index=17005)
Annotation(end_index=17019, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHM0vr3qDX0UqWb8BYWHUoWVz5WB3PScy2FDog_XTphBkMtugXpg1YLimYGLy12UNA05kzuPAR4StSLMSsMaWZ3gEKQTyV3ZBeH6Cm7x6EiBKedQlsJ5nuq0U8EdIDOYLfr126u1g==', start_index=17005)
Annotation(end_index=17206, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFCPbhoS_z2KIbDPGnpfX8UyNeqgZDN3gwIrb5VHK00IShFAJo3_FYQcGvXS1laqgyc0DusfFQnX8p3sxCgbosszm3Cs0g3yTyg5lojWTgnuZAGWDKdNRrwjA9qbAkPzV_0tVBsVkC4TAQTnFc_29n_mAkzGeyxkQ==', start_index=17192)
Annotation(end_index=17206, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGWd_Q4yKaVEIzf9SOr6klkhPiSX8zsU_t_HlXf9H5zgBa85RX-gsEfIk8F9WLXDgacZeKYCBOf033i6ygSdSstkCfnqYpG_6stOWmi7sg6W9Lmw1-SfuEP8URh2M9qeAbpPlNogMnUWY3zRneqMvscUwGBATTZZ2oZn2-5aZtJ-ebpThQULCg1v96WHEj9gNlo8I-O89SPcjANfev9PG4br6iSJiMW2JkrGAplvyoTSkcyaJNCV8fg9qC75x9yhl8El-5SRA==', start_index=17192)
Annotation(end_index=17509, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfFIwXW8ipGRDY_laBvw5O99exBOcErloCu2xSrWD8cWoS1J7JUr_fi8D2HAVjKFTXqCYIMVVemArx3XG2IYI2g9P10zhz_PgEQ4S31TE18Z_nNVoyjtRiReDzj4ETEDBnQGKtRs9fARW37xx7JcIFUfZfKUN2fih48fhxit9EU8E-ZjoeWIwZh07u0o09x6he22MxwzaiL8a_y3YL0w==', start_index=17500)
Annotation(end_index=17865, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyfMFm0XA2pZD3Zv4uI79AdCJdtMyGUPq8DBEm2mWSK95IZYM42f65cJcSrgM2qSJDWtQLOIqQkHtQqHFx2gTGpaBURVoN44c4ZOwUI6FWkOA5J2LBZ4IQoyNBa0TqXWYWONkkZXJuQcqxJojsFg5izdFUH8SwhIGjBfFwO57kd-0CH4xFFFKhpPXN9K8dCN--vVHLWV_jf4dfcy7hFdUJyL4ynXMFtyFRpbmymGX-hI2J7Gfm3QK2tQFIl4z-', start_index=17843)
Annotation(end_index=17865, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFahBFjomkOk-PKTSEiDvoj_bq3bAZzQAjQLlwcoie1ziqkvPYU0soRfiiZmjAjF-k51SbDC94pZrI76oXNjSV76QARvcr22mDRvvZ7LybB_gm3XA6o3sSKp36AXzoZatVLWBCeJDWS-WQqyXB3-JK6wHGJsgyE93d1RCgHTDzVPVH4ElxqCzmor2t9Qa9zmTbZ5Ty5NBI7GW6pvZNNs34p6Sz82dw=', start_index=17843)
Annotation(end_index=17865, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP6JliolPSgTGrBZYcPzv0JkbmQRemTF9nartV4PpfzRVSVbQ4zIT8dxPI5KQbKWS-DG-sGmGUGsdZZ9QL6iuWBMsmTYMIZnEDHb-4n83bFyQ5abEX8UIaIvWBZw3dYsBmzGSR15T20uL2zAi-0C9S4WQaIEGL-98pDL5OMNFa1KWL5GELkO_mGkEiNw6mZGYHAN_UR4isQth4N23ZcrqgfNif_zeroSLXS3FjmsXPIlA=', start_index=17843)
Annotation(end_index=17865, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxBQYt1bBjXGXBexED4z1lK08JrMHYqQTDyWw1s0uuhEpL54TTITpZ1Wo6QdUO3QUGbn3O9PfLyk_yj_XmmLCq3bgAeuFUcBApDANFYxv6Q--IEtV_w21oCKoCqO9v8xtlgWFNYABokf4UQXi4LQbe5S7nG0mhehF7Fs_FSlKyvuBQcGmRNxs9rWrv9J1GRefQTXTntInZB4PuJT48gc4Q-zlhxXPnScPF7GkFvBA2A-aKGuMzBN3O8TaBLNRjFR9S7eA6ujTGPj6YLAIJVbdU3lw=', start_index=17843)
Annotation(end_index=18137, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHf-53juUVyml_-VMfiMuo9mQ12aIBRSq7mJrLJ2MIbooxTux5wNHX-0MP2vm46JkOVfZwUTo-xmsiiSIp9ZvroIhTGlTHf7vUJqrsHDkaOlLBTEioMUQ==', start_index=18127)
Annotation(end_index=19449, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIF2xRxANbmmzfVcd6-iytF1b6-hAbD-kXsz5WZjq0NbN_Yto00xoggC0ydKyNqlPcM9UtY5YK0iXfevS26336rvU16n5b0IJMH46HUoEogtoIHez5UMGX2khpWMH8Z0zNrAI4-C_Io_2ZcTBwmnvghmn56JAg9xfpG2QyR3G7mlZuGmH1YnByMRYLuTi9qa3XJGlTt2C19nT5uc-vQsf2ixPrRI9-v7rD1vWlHxT_', start_index=19440)
Annotation(end_index=21001, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFb4X0e7DLtKbN4c-zrI5hQ8iNJjGs6SH414z887-vo3A_3FL5wFr0Wentioj9X9TMya0WFAUeexfmgvS_kww91sJqzFUtG0gTiO8tnofPDmuCb6tZUIlpn-vQ7szvR_ljRcbbb4xmxLMkRfzMWZGJqvP2_ZgKYyFMpgFiNVfitXiSkUx5ye7bAIMHjUxdgKZQw5WqkaEdd5Vio6A-uffexaJUMJzgvoqRU-YuQb_DkUfzlq3NYdm14JbL0Z017sCfQfLOk5kSS4TFZUw6JqrDMsWRLtikJFwGIzORVqhXwTlxHb9Xglhvs3ogCjoSuVCRX', start_index=20987)
Annotation(end_index=21001, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP6JliolPSgTGrBZYcPzv0JkbmQRemTF9nartV4PpfzRVSVbQ4zIT8dxPI5KQbKWS-DG-sGmGUGsdZZ9QL6iuWBMsmTYMIZnEDHb-4n83bFyQ5abEX8UIaIvWBZw3dYsBmzGSR15T20uL2zAi-0C9S4WQaIEGL-98pDL5OMNFa1KWL5GELkO_mGkEiNw6mZGYHAN_UR4isQth4N23ZcrqgfNif_zeroSLXS3FjmsXPIlA=', start_index=20987)
Annotation(end_index=21280, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyfMFm0XA2pZD3Zv4uI79AdCJdtMyGUPq8DBEm2mWSK95IZYM42f65cJcSrgM2qSJDWtQLOIqQkHtQqHFx2gTGpaBURVoN44c4ZOwUI6FWkOA5J2LBZ4IQoyNBa0TqXWYWONkkZXJuQcqxJojsFg5izdFUH8SwhIGjBfFwO57kd-0CH4xFFFKhpPXN9K8dCN--vVHLWV_jf4dfcy7hFdUJyL4ynXMFtyFRpbmymGX-hI2J7Gfm3QK2tQFIl4z-', start_index=21266)
Annotation(end_index=21280, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRwGVQZCZcj654fKkrju-2_1l6UYI-QJg5H01Iwhfmhf84GXx9_Fb1cO2lkNYxMAphLGzhGQHjmShCUCT3bo-kqQixVOlgNyoXZS9uJfvxpfh9C0tmGR-D0niRtfIaijHp3IPisuz_XYHpBwNGkWr-XV2vc2K-sKi7hOl6lxxik-bWJkdIlhioHw2IuMsfSGNER51lRrNBGqS7', start_index=21266)
Annotation(end_index=21513, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsAVhKRkIbTcUz1bTNVCkUbfy-Hv2tJU_iLdbs37eADmNKmAqg8wlFYdTnND4zLHgjgwmAWqmzLmy_y241edMdOR6nKJcpNOfWe-HTgOP2w_JCX-ud6e8Rxw2z_wNCwIrCv1qrNOaBIzlX2OkEYQsWP05mxSj_68cRcszdhWlWjWsDXOwqG7zUFKORV5LZ9_r8RuUrXkf5zIPHg6KGmIFjG5WYRErVXTYeE8UwqJrgUGk=', start_index=21500)
Annotation(end_index=21513, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGK5ace_5ZYIyecMNgqzZCRrugN1_n5HBeg63wGvQiQK_cAJuVatpQhRcce6_f9Z3AOUc9mPikEm-dYiDSqvdn-qdW5BBQBCYqxCuqdNYAZVC0tG2-2AgLjP4HB4NW5j6Wd8JIfG0nBD9952_Q-Le22BmWzGw4f6ofVSbNjbOYfiNaMnz2GLaNzf35f85IkRCCX7Q==', start_index=21500)
Annotation(end_index=21709, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHVSFmh064X6LTDIGcghm6xmzN-CWeJrW62N3Onc4Bhfa-mMPv02gBLTwZLMop3mAruXLOPvg9aaF-bLoMZGbVRHZEhvA0Iql8louyyKd4quRac5_9DzzGVIgiwezdr6JiKzSlGWLTK4g==', start_index=21699)
Annotation(end_index=21813, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiRc8jkJMv5jdkInvZcWTPlk5Cjw59Tkmo224cbwr2o5AeQHG2Kpg78ieNr9R8aZpPNr-I3uCKnaX68TlewdfevkFeg3hIyQNMIoM2QwhK4N3IWWlxFH1sWk3YyjvqZ4DZ8FmkX7ARcqfzKqRes75WxA==', start_index=21795)
Annotation(end_index=21813, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEo27Penpy7EMo9wtePWs7mmu3VryokXrPddWs1A_XJ9daKHtMrhhI0u-dfdvyZogrvnCzEce-BKe4yV-CA67xR9kFKTOTYXQgj4wZC_U0vHfWoohoZV8TOYtiNh2vdxBrQa6qFPmqTBo1d1MPegdlbBy0akSqn5HnQ7mljJleSvryfMBpRe21jwvbFiuV6ze2NQyywSfqzWg6Zvp8QFKEOGvasTdzFIbn22A==', start_index=21795)
Annotation(end_index=21813, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTHMMsWMKowCDZk3WYlTJwLyR2_FVjE0JBcqa3jkQOyv0rZ6yDzZo-7Fioz0pApuafuKY1PWLn7uZwohkcAakCwCFRdNcSR_gim5A3UtkBDwU3_dt_bliOzGbt-apSR12bKybXT2NMIA==', start_index=21795)
Annotation(end_index=22776, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJSADzzIL_uaVKekTnddMP0imMGNq5KdRJWuap4D-pxSU52wi6KfhHxlszBsUngo1QnlFiEGTGsj1xQyUE4xbxcMW0kJbyHSLEMkdUd9CwoXZ8X-J-NcZ6xZKL6wiZqR7ziMtLaDvbzrotQ1bnWaMFThhYQxZqhunS0wT-14NZHx718a1jT_pWNH5uchgR9Plo2PaPpA==', start_index=22767)
Annotation(end_index=23051, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJSADzzIL_uaVKekTnddMP0imMGNq5KdRJWuap4D-pxSU52wi6KfhHxlszBsUngo1QnlFiEGTGsj1xQyUE4xbxcMW0kJbyHSLEMkdUd9CwoXZ8X-J-NcZ6xZKL6wiZqR7ziMtLaDvbzrotQ1bnWaMFThhYQxZqhunS0wT-14NZHx718a1jT_pWNH5uchgR9Plo2PaPpA==', start_index=23042)
Annotation(end_index=23918, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxBQYt1bBjXGXBexED4z1lK08JrMHYqQTDyWw1s0uuhEpL54TTITpZ1Wo6QdUO3QUGbn3O9PfLyk_yj_XmmLCq3bgAeuFUcBApDANFYxv6Q--IEtV_w21oCKoCqO9v8xtlgWFNYABokf4UQXi4LQbe5S7nG0mhehF7Fs_FSlKyvuBQcGmRNxs9rWrv9J1GRefQTXTntInZB4PuJT48gc4Q-zlhxXPnScPF7GkFvBA2A-aKGuMzBN3O8TaBLNRjFR9S7eA6ujTGPj6YLAIJVbdU3lw=', start_index=23908)
Annotation(end_index=24124, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoAH0KH-Gml_wAvfLP3GcM40x7iGuGysCZ6qRDQ9puwx-6CFI6Tyjt98X00g7vp2PHBiwEDTFcqNDx7qIadeZ1wWv5xL9Pk7qcAAFtiVcRNaidWvUGPbpYmGWxgMo=', start_index=24110)
Annotation(end_index=24124, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbH34Xtyol1zRga_F-5f0sSrG-XjDaVsZDXPNBmJzQSkqUZyi21yasCeVqyrYmVAHRNXVCMcUgktaZiY1D-9DYfyGa8Q77kaf_zAKSANnZbSJsZEG5lFuGKqL5DA==', start_index=24110)

## Sources
