# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 52032210 | **Time:** 344.42s | **Cost:** $1.58038
--------------------------------------------------------------------------------

# Algorithmic Trade-offs in Social Network Dynamics: Brand Authenticity, Diffusion Speed, and the Mechanics of Rumor Propagation

**Key Points**
*   **The Authenticity-Speed Paradox:** Social network algorithms create a fundamental trade-off for brands; optimizing for high-speed diffusion and algorithmic visibility often correlates with a measurable decline in perceived authenticity, a phenomenon quantified as the "Authenticity Decay Curve."
*   **Rumor Advantage:** Research indicates that rumors spread faster, farther, and deeper than authentic news, largely because they exploit the same algorithmic preference for high-arousal content (novelty, fear, surprise) that brands attempt to harness for engagement.
*   **Node Weight Decay and Rumors:** In graph models, "node weight decay" functions as a double-edged sword. While temporal decay of influence generally suppresses long-term rumor persistence, the lack of decay (or slow decay) in heavy-tailed networks allows rumors to reach "ultra-fast" saturation before corrective mechanisms (truth) can intervene.
*   **Algorithmic Mediation:** Current algorithms prioritize engagement over veracity, meaning that without specific interventions (like location-aware weighted models or timely refutation), the natural topology of social graphs facilitates the spread of misinformation over complex, authentic narratives.

## 1. Introduction: The Algorithmic Ecosystem of Influence

The contemporary digital landscape is defined by a complex interplay between algorithmic curation, information diffusion, and user perception. For brands and organizations, social networks represent a high-stakes environment where the goal of maximizing reach (diffusion speed) often conflicts with the imperative of maintaining trust (authenticity). Simultaneously, these same algorithmic mechanisms that brands utilize to amplify their messages serve as the infrastructure for the rapid propagation of rumors and misinformation.

The central inquiry of this report addresses two interlinked phenomena: the capacity of social network algorithms to balance diffusion speed with brand authenticity, and the specific role of graph theoretical mechanisms—specifically node weight decay—in the facilitation or suppression of rumors.

Research suggests that the architecture of social platforms, which evolved from chronological feeds to engagement-based algorithmic ranking, has fundamentally altered the nature of influence [cite: 1]. In this environment, "authenticity" is no longer a static attribute but a dynamic variable that degrades as reach expands—a concept identified as the "Authenticity Decay Curve" [cite: 2]. Concurrently, the mechanics of information spreading, modeled through complex networks and diffusion equations, reveal that rumors possess structural advantages over authentic truth, often exploiting heavy-tailed node distributions to achieve saturation before verification can occur [cite: 3, 4].

This report synthesizes findings from network science, marketing theory, and computational social science to provide a comprehensive analysis of these dynamics. It explores how the mathematical properties of graph models—such as the temporal decay of node influence—interact with human behavioral psychology to shape the flow of information, whether that information is a brand narrative or a viral falsehood.

## 2. The Trade-off Between Diffusion Speed and Brand Authenticity

The digital marketplace operates on an economy of attention where algorithms act as the primary gatekeepers. For brands, the pursuit of visibility necessitates an alignment with algorithmic preferences, yet this alignment often comes at the cost of perceived authenticity.

### 2.1. The Shift from Chronological to Algorithmic Feeds
Historically, social media feeds displayed content chronologically, a neutral distribution method that favored recency. As platforms scaled, this became inefficient, leading to the adoption of algorithmic feeds designed to maximize user time-on-site through engagement metrics (likes, comments, shares) [cite: 1].
*   **Engagement Optimization:** Algorithms prioritize content that generates immediate reactions. This creates a "survival of the fastest" environment where content must provoke a visceral response to be seen [cite: 5].
*   **The Visibility Cost:** Organic reach has declined significantly, forcing brands to rely on paid promotion or "viral-ready" content strategies. This shift forces a dichotomy: brands must often choose between nuanced, authentic storytelling (which may have lower immediate engagement) and sensationalized content optimized for algorithmic pickup [cite: 1, 6].

### 2.2. The Authenticity Decay Curve
A critical concept in understanding this trade-off is the "Authenticity Decay Curve." This theoretical framework describes the inverse relationship between an influencer or brand's scale of reach and their perceived genuineness.
*   **Definition:** The Authenticity Decay Curve is defined as the measurable decline in perceived authenticity that occurs as an entity's reach, partnerships, or visibility expand over time [cite: 2].
*   **Mechanism:** As audiences grow, the intimacy of the "para-social" relationship fractures. Content that feels organic at 10,000 followers appears manufactured or "sold out" at 1 million followers. Research indicates that 63% of consumers believe influencers become "less relatable" as their following grows [cite: 2].
*   **Algorithmic Acceleration:** Algorithms accelerate this decay by amplifying content that fits specific viral templates, stripping away the unique context that signals authenticity. When brands chase algorithmic trends (e.g., using trending audio, participating in generic challenges), they sacrifice distinctiveness for diffusion speed [cite: 7].

### 2.3. Algorithmic Mediation of Perception
In the current ecosystem, algorithms control brand perception more than brand managers do. The "algorithmic mediation" of content means that a brand's narrative is often constructed by the platform's selection of user-generated content (UGC) rather than the brand's own communications [cite: 8].
*   **Peer vs. Brand Content:** Algorithms prioritize authentic peer content (reviews, unboxing, complaints) over branded communications because engagement data shows consumers trust peer content more. Consequently, a brand's "authenticity" is often defined by third-party creators whom the algorithm selects to amplify [cite: 8].
*   **The Trust Deficit:** There is a growing consumer demand for "realness." Studies show that 76% of consumers prioritize authentic content, and 67% have little trust in overly promotional posts [cite: 9]. This creates a paradox: to be favored by the algorithm (which likes high engagement), brands often adopt tactics that erode the very trust required for long-term loyalty [cite: 6].

## 3. Graph Theoretic Foundations of Information Diffusion

To understand why rumors spread or how authenticity decays, one must examine the underlying mathematical models used to simulate and analyze social networks. These models represent users as nodes and relationships as edges, with various parameters dictating the flow of information.

### 3.1. Classical Diffusion Models
*   **Independent Cascade (IC) Model:** In this model, an active node has a single chance to activate its neighbors with a probability $p$. This models "viral" spreading where infection is probabilistic [cite: 10, 11].
*   **Linear Threshold (LT) Model:** A node becomes active only if a weighted fraction of its neighbors are active. This models "complex contagion," where social reinforcement is needed (e.g., adopting a new technology or believing a controversial idea) [cite: 12].
*   **Deficiencies in Classical Models:** Traditional IC and LT models often assume static networks and ignore the *temporal decay* of information value. They assume that once a node is influenced, it remains a potential spreader indefinitely, or until a specific recovery step, which overestimates the speed and scale of spread in real-world scenarios [cite: 13].

### 3.2. Graph Neural Networks (GNNs) and Representation Learning
Modern approaches utilize Graph Neural Networks (GNNs) to detect rumors and model diffusion.
*   **GraphSAGE:** A framework that generates node embeddings by sampling and aggregating features from a node's local neighborhood. It allows for inductive learning on large graphs [cite: 14].
*   **Location-Aware Models (GSMA):** Recent advancements, such as the GSMA model, introduce attention mechanisms and position encoding. Unlike simple mean-aggregation in standard GraphSAGE, these models weigh neighboring nodes differently based on their structural importance and relative position, significantly improving rumor detection accuracy (up to 97.55% on Weibo datasets) [cite: 14, 15].

### 3.3. Node Weight and Heavy-Tailed Distributions
The "weight" of a node can refer to its centrality (influence) or a learned parameter in a neural network.
*   **Heavy-Tailed Distributions:** Social networks exhibit power-law degree distributions (scale-free networks). A small number of "hub" nodes have a massive number of connections. Research shows that in such networks, rumors can spread "ultra-fast" because the probability of hitting a hub is high, and hubs act as super-spreaders [cite: 3].
*   **The Role of Hubs:** If the distribution of node weights (influence) has a heavy enough tail, rumors spread rapidly regardless of geometric penalties (distance). This "ultra-fast" spreading phase makes containment difficult [cite: 3].

## 4. Node Weight Decay: Facilitator or Inhibitor of Rumors?

The concept of "node weight decay" is pivotal and carries dual meanings in this context: the *temporal decay* of a node's influence/activity, and the *regularization* of weights in predictive models.

### 4.1. Temporal Decay of Influence (Information Aging)
In diffusion dynamics, "decay" refers to the reduction of a node's probability to transmit information over time, or the reduction of the information's value itself.
*   **Inhibiting Rumors:** Research demonstrates that introducing a temporal decay factor (where interest or influence fades over time) is crucial for realistic modeling. If the decay rate is high (information ages quickly), rumors are suppressed because they cannot sustain the momentum needed to bridge structural gaps in the network [cite: 16, 17].
    *   *Mechanism:* As the decay rate increases, the time to reach a stable state shortens, and the final number of "stiflers" (those who stop spreading) increases. Rapid decay mimics the loss of novelty or the effectiveness of early debunking [cite: 17].
*   **Facilitating Rumors (The Absence of Decay):** Conversely, models that *lack* temporal decay (assuming exposures accumulate indefinitely) overestimate rumor spread. In real-world scenarios, if the decay is too slow—or if the "authenticity decay" of the truth is faster than the "interest decay" of the rumor—the rumor prevails [cite: 13].
*   **The "Stretched Exponential" Effect:** On platforms like Twitter, information diffusion follows a "stretched exponential" decay rather than a simple exponential one. This implies that while most content dies quickly, some content (often rumors) enters a regime of slower decay, allowing it to persist longer than expected [cite: 18].

### 4.2. Weight Decay in Graph Neural Networks (Regularization)
In the context of *detecting* rumors using AI (e.g., GNNs), "weight decay" refers to L2 regularization applied to the model's parameters.
*   **Function:** This technique penalizes large weights in the neural network, forcing the model to learn smoother, simpler functions and preventing overfitting to training data [cite: 19].
*   **Impact on Rumors:** By preventing overfitting, weight decay helps detection models generalize better to new, unseen rumors. Therefore, in the context of *detection algorithms*, weight decay hinders the spread of rumors by making automated identification systems more robust [cite: 19, 20].

### 4.3. The "Survival of the Fastest"
The interaction between node weight and temporal dynamics creates a "survival of the fastest" ecosystem.
*   **Speed-Accuracy Trade-off:** Theoretical bounds show a trade-off between the speed of diffusion and the accuracy of information. Faster diffusion dynamics (high entropy production) are often associated with lower accuracy. Rumors, which are unencumbered by the verification processes that slow down truth, exploit this by maximizing speed at the expense of accuracy [cite: 5, 21].
*   **Saturation:** In heavy-tailed networks without significant decay penalties for long-distance edges, rumors can saturate the network (reach the majority) before the "truth" (which might start later or spread slower) can catch up [cite: 3].

## 5. Comparative Dynamics: Rumors vs. Authentic Truth

The research overwhelmingly supports the conclusion that current algorithmic environments favor the kinetics of rumors over the kinetics of authentic truth.

### 5.1. Differential Spreading Patterns
*   **Speed and Reach:** Empirical studies on massive datasets (e.g., Twitter cascades) confirm that false rumors spread "farther, faster, deeper, and more broadly" than the truth [cite: 4, 22].
*   **Structural Virality:** False rumors often exhibit higher structural virality, meaning they branch out into multiple generations of reshares more aggressively than truth, which often spreads in smaller, disconnected clusters [cite: 23].

### 5.2. Emotional and Semantic Drivers
The "weight" of a rumor node is often amplified by its emotional payload.
*   **Sentiment Analysis:** False rumors are more likely to go viral if they convey high-arousal emotions such as **disgust**, **fear**, or **surprise**. They also tend to use more positive sentiment words (potentially to feign helpfulness or authority) compared to the truth [cite: 23, 24].
*   **Novelty:** Rumors are often more novel than the truth. Since algorithms are designed to surface novel, engaging content, they systematically upweight rumors [cite: 25].

### 5.3. The Stifling of Truth
*   **Verification Latency:** Truthful information often requires verification, introducing a time lag. In a "survival of the fastest" environment, this latency is fatal. By the time the truth starts spreading, the rumor has often already established a dominant position in the network [cite: 26].
*   **Refutation Decay:** The effectiveness of refuting rumors decays rapidly. Research indicates that refutation is most effective within 72 hours. After this window, the "information value" of the correction diminishes, and the rumor may have already become entrenched in the user's belief system (echo chambers) [cite: 27].

## 6. Balancing the Equation: Algorithmic and Strategic Interventions

Can the balance be restored? The research points to specific algorithmic and strategic adjustments.

### 6.1. Location-Aware and Weighted Graph Models
To combat rumors without destroying legitimate brand communication, algorithms must move beyond simple topology.
*   **GSMA Implementation:** Implementing location-aware weighted GraphSAGE models allows platforms to detect rumors by analyzing the *structure* of the propagation tree, not just the text. These models can identify the "anomalous" spreading patterns of rumors (e.g., unnatural speed or lack of trusted hubs) [cite: 14, 15].
*   **Dynamic Attention:** Using attention mechanisms to assign different weights to neighbors allows the algorithm to "listen" to trusted nodes more than random spreaders, effectively re-weighting the graph to favor authenticity [cite: 15].

### 6.2. Managing the Authenticity Decay
For brands, the solution lies in managing the Authenticity Decay Curve.
*   **Hybrid Strategies:** Brands must balance "algorithmic" content (optimized for reach) with "authentic" content (optimized for trust). Over-reliance on paid or algorithmic-optimized posts accelerates decay [cite: 1, 6].
*   **Cultural EQ:** Successful brands in 2025 are those that use "Cultural EQ" (Emotional Intelligence) to create content that feels personal and unpolished, bypassing the "commercial" filters that trigger consumer cynicism [cite: 28].

### 6.3. Temporal Interventions
*   **Accelerating Rumor Decay:** Algorithms can be tuned to artificially increase the "decay rate" of unverified high-velocity information. By dampening the reach of content that spreads "too fast" (exceeding a speed-accuracy threshold), platforms can create a window for verification [cite: 16, 21].
*   **Timely Refutation:** Government and platform interventions must occur during the "rapid decay" phase (t=6 to t=15 in simulation models). Interventions after this period face diminishing returns due to the stabilization of public opinion [cite: 16].

## 7. Conclusion

The query asks whether social network algorithms can balance diffusion speed and authenticity, or if node weight decay facilitates rumors. The evidence suggests a complex reality:

1.  **Current Imbalance:** Current algorithms, optimized for engagement and speed, inherently disadvantage authenticity. They create an "Authenticity Decay Curve" for brands and a "super-highway" for rumors, which exploit the system's preference for novelty and emotional arousal.
2.  **Role of Node Weight Decay:**
    *   **Temporal Decay:** The *natural* decay of interest helps suppress rumors, but only if the decay is fast enough. In heavy-tailed networks (the real world), the lack of sufficient decay mechanisms allows rumors to spread "ultra-fast."
    *   **Algorithmic Decay:** Implementing *artificial* decay (dampening) on high-velocity, unverified information is a potential solution.
    *   **Regularization:** Weight decay in AI models helps *detect* rumors by preventing overfitting, serving as a technical countermeasure.
3.  **The Path Forward:** Balancing this equation requires a shift from "engagement-blind" diffusion models to "location-aware" and "time-sensitive" models (like GSMA). For brands, it requires accepting that maximum speed often equals minimum authenticity, necessitating a strategic decoupling of reach and trust-building activities.

Ultimately, the "survival of the fastest" dynamic currently favors rumors. Reversing this requires algorithmic architectures that explicitly value the *provenance* and *veracity* of a node (authenticity) over its mere *connectivity* and *activity* (speed).

## References
[cite: 1, 8] - Algorithmic impact on brand visibility and perception.
[cite: 9, 29] - Consumer demand for authenticity and distrust of polished content.
[cite: 2] - The Authenticity Decay Curve.
[cite: 6, 7] - Strategies for balancing algorithmic optimization and creativity.
[cite: 14, 15] - GraphSAGE, GSMA, and location-aware rumor detection models.
[cite: 3] - Heavy-tailed distributions and "ultra-fast" rumor spreading.
[cite: 19] - Weight decay as L2 regularization in neural networks.
[cite: 5, 21] - Speed-accuracy trade-offs and "survival of the fastest."
[cite: 10, 11] - Classical diffusion models (IC, LT).
[cite: 4, 22] - Empirical evidence of rumors spreading faster than truth.
[cite: 23, 24] - Emotional drivers (sentiment, fear, disgust) of rumor virality.
[cite: 27] - Effectiveness and decay of rumor refutation (72h window).
[cite: 16, 17] - Temporal decay of information value and its role in suppressing rumors.
[cite: 13] - Impact of infinite memory vs. temporal decay in diffusion models.

**Sources:**
1. [bostoninstituteofanalytics.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcJwL8WHwtubLOIsREhojpwAADztDkkT0jwnRKCnD3hIV8qkUP4bZw0Wm4RwspuMa2DLmo7l31eijf7kfPnD2mmRGTzu52CoUeoBxYZYssSEAPdvSc2lrDBIfTcu30Knmw2SRN-uzPj2LPQdzVQHv5yCoyrEf9c1i9pOL3w9RlVaLvxJku3Vh_ZhYZCc1Uv6L8YNeflJ9fmXE=)
2. [pictelate.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwnZYCNbRM58W_tI3jc9l_V9oaYnn0pldAtUg-KtEHVpVxFKqOi0lObKHYpqepvtzaTdROZfPjArjkhvph--26tAvKUFX1OzraineHahI15Wpt2ZYixpZiz64WZtcL84E86-7w3iNrUWVTZ2v6EP2IwllJKFHY3d3SN5dsrBJ4_-m2LNhg6PNHLA==)
3. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmPkBVi4f8sssGrnNcz30tvx_MTiHNQk7Np3pN6MzDBZJqvcGbkWLGaXTJ3hOE5OblQ2Q500FnFYrut3jrAIky0KfbGv7m1EYA2v7asdJv5UkZu5SU)
4. [china-ces.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfDLxBJwc94NF37CT4i__vdsiXc2Zr_2i3Nn5WLy5klcAiECMmOazLjoOwgwYK7H-fUsUoOu2Jqg1Q7CRTmlIa9w1AiGboJ-SFVu_jZkEz3hq4Ab5fPj1RTKCASCxBMpsn6Z2QqoPvSoiD3Oo0K-nxbkCqwjtcbU0=)
5. [earlygame.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyLt6PkLJNPhZacRHk6K0nh2cZl0Kw0QN2_3B1WjNOIKDkqUU33Lk-5j3swm3Vcer2xDBc5Bft0LTXHxGlS_4DB4wNQmNhyFJVoH6vezrIpZgZcrNivkVOkQVa1O6mfwdT4bJ3PV1qHDKUqekAa4ugxoXGHDzKobL4i6HwS6JgBjaH62msBr3Qu3e3W578XWALsYByhCd0zWpAdjTp91BE7EsAoWkaL5lvO9L2sWQuP0ijWE9VTXO_3Q==)
6. [phable.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBLZaKq4GrdbNbTLsNZMirw2ud_LUyXspdQKvhjayP1oZFKYnDmfi97H0LqgE66DeVAfkSYIcDsCPhgFs19h8uice1Vl6yT93Tv9ymSzHrViMLIdyo5wsHV4IxfMFn-Sobp1zYryPfRB2scDzeCF9-97loGLi617Iym8mSwzRu3w==)
7. [cavesocial.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5K9Cbt9CHfS-RmFtBmBhCiTyzqDKKFGwG6b66GkkqpGTJzkmaNmyAmpEkuy1xNl-Ftt-FJaFK1TREflz4wd6-R7TFb3wm6QKR9cZW34f9G4G8xoNAucln1_WuRU8TbMRCYpeZGdfOudR44rByGIj05LOtyEIkSSJNlRFCiWBkr4IQMU0hLVcpDEM=)
8. [cooperativecomputing.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3Up_db33VQLO3L6R1SrA0Et8sTFpQ7m1LNClwMRQI0wR3lWw8Cw6JtVGA98G2zDv9rL0MC3_EbXdzZ-QhINDXw6djvrnBE6Y1dO-ogFOCoXMm2vLM_2grPdKdLnQIGxC1qRlhAuBmLkysZWoWi4Ce5LUMZf3X9fi3QfoskScAI616tpRPLxSkZDu6RwQ1EKq9I8xihcGKK1Q=)
9. [luxuriousmagazine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEk_WvVHiujr5KnH-YlceIP11Ariz3-_bdo52v7SQsbruLPstdB0h2i6QINTHwY3tR7APeLAa6EMlvl50Mdva4CL_QLhIEwUUOt3zfiIOnIZvjosqrCDpw2Kcnb2dZt1vuAY2odHCpCMBYkJX71U6CPSIn8D8N49XK8QRCxWSo=)
10. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAi5q0cP3WEvgpZat9HAia72LZM0_Udft5ymRDMGdiAsRKYgAXYBfPU85ftQS5bjm6U9QUE33wjvM-6qdurR_Vb7poTdVaofWuKICuuo4pRdtib8ybLff_6TfNFl-YweRiwklWctAr)
11. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLC-GgCzVnt8L1iOhGizUKNkvpso_y8utDvMrNpYYFbGZE2FSaefLf4WnBxQYCt7EgS9uFhFtig6dfNPUWEiFR-WjhlkJ6RakdNB0Kpn4QKHi78DInTM_GnmQmUTvEHCk=)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAZFbIoKclmX93b63IBxywS9Rb4X6zBNfFtzcUTCdhI2oePtoOmTvKOF97BPP83wV9Gn4nhwwZsa8uZtwrgU6ObprW-3vzYvh4zXIf9x3DKon2H5dnpaYQmmNMtAnyCV4v7OktVx6Qv7ROVa3nEOezaVSB_-AZ8ooIezlT0PD04L6x1Al-pW0Z9MOvb-WP97Zw465lZ7PE)
13. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEutMMF9Mj3kyagaapTcLNR2XuIRBBa6KL0_ZqVUgAeNjb67YcTAX7_SoOjxCeSr8OC1FN7G8NEwAcTfeJGd14lhxFQg4MNLAoKdtv6HsXPUnr6UPy1eHvL)
14. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGiqrdIGkUMLq59DXixmiip_vmJfv3t33Yts3MLA29HMc_5gyINFxpCLNzZaa37B97eGOsvPsu2mtUnCJ9PCPR2aYhyEFPd3yQtC_Cj_scATy7abU4IspeBzhqMvneXZMCNK5IE15eN)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnkH3NJuWXqpY3Du_5FvMRiQJ_g1vJH1VE7dVBwsWgEjAeMEetIDWPZHIPSEAM_CUsNMwpLAw_HSVAeeJhQqnSma2c1QL1M416wGTv1TDXycAEVkV_JztT0PySJOHRARsSklJZX6aafvBx46klKJ-34pxh915LV2b6lWaiwTtxZH9GgNCDy1gTp15KifmFaBjMocCnoxnNpy3WgpcpHHxsddoEr_5fe9NfuzjZ1CZf)
16. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSA_utGT6gZ8x-G13RkoKrAgUj_kAm3NdtFR9n35qL_7Z5LBsFNq34hITdj2lkWvD8-QYs09XQxsK1IT3yg9MDZvAdMqJ6-TVaX5yp7U6OHvPmO0dYzSzSmH4Tjg==)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERftMNlofkuc0NhGDpiqX-tOHws3IQc_dyxw9W8SyO9LXXLCeoNXjxEuaVWW_M_NvF8GLHmwRt6nnNdaj7F4d0qKupIYGj4X7P3pX99nlRCn8kEAKHNCRyICOGOEwfWbst80BIqLC3w28BEXLa7ysk5qB0ago2Fz_Cb8c95B3fzgBCwUb1xe9oHwgjAIQEiqKpRYqtew-sNxhIbZtGP1fPAPBsITcWvgTlFTTjousEV3YWnXbF9YT2YlT3bXcR9dZVgkmlFpQ=)
18. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiA2Ok9-8BNuFHPY11dkq8WTn5YBmwVazJZm_PKzXykHC6NlDSzVr_8Uas9iRKPW4Z2tlYXIkqBOjEVksYXovUKQNr1DWpjrbhlgGTAkDrsJgpngsj_nJmZv6-zw==)
19. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrnHjAYtImo8D-l_foXBdjMb01qkZSjOrORCkERguzAbzWxkSydhXagnm2Xv9yp3vv9afZu2kgDbbI3w6-SP6gmNA9L2NBESNn358mIy63AEAhmkqPPacF-i7HPCaImJrDXwLh1x4tjYdbtejymP7DrEF3n73BgFVgX65PdOCgNbD2JegnqQM=)
20. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2r_Dq8KWSutcgxwxW8CkXD_VN2w-eoVWMH6c21-un5QRgirFxWXcb1w-9GpZlpa86USOwDmARCcoQfYpBBQ7Z4aH6MWp9_KRTNCVgEUpcr3AOeJZ6fs1c)
21. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEj46uNt-zlYpUsQbSDMBFh78od-ErX8PnSljJoV0qMTXNLtm40SvOmHLPLUsl0HqtgDGOAwhji3cgjXnzxRzOJubKoRmPMCUBtMn9ONp8pm8vpbiF3AIwg)
22. [hawaii.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZwc14HvgbogMctsSklER63DnNjxU4VtO4qnloXwF3QmhxHNxmWDBwq4LsMMKy_O0ZYSt2TxCPAqLUhFqAwcUFWDuP3D8gaCRLfR4qrNrFc5rsfNUn0Jme3hMWLKxBdQKrxpJDIXM1amO4qgezquR7RKy36yndkLMkncAiJ5qfGM-ttKWU66TQNwjz1nuK2lofzBo=)
23. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjFbtk2_8xsFEIU0aEuKHOiD1pTlLfZuYwTfRJW5n5kJHZcJLhsHDEAm9b7YVojvbXwkLARQRr2kSzHZ_iJh0ewJbwwYJ0PFVtKZzzSoiQ4PUFYouv8u47zX7oiL_wlk8M1T0U4GGcF0EMvhtzSFmmxbrccDRbf36PC_bCFKetavg3ClRynVidPdOuOAt6WaVLY0mU01w6zktxVNxdR78JG1EirVTMd7IGTIWuY4op5pEIRzNlnbywx9pT)
24. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxlOQXiOTHPbRFCSVOjDF3dlnPKBX4RM3vxotJXFl7PWJ2WntVGtgkPukhxIN1HaS5egKE9i-rbQa6x9dvyZdnZozh_T4PUwIy7Yrj6jr74gipgmQ-weUoHAU3mg31)
25. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwDe2vrljTXjIPZDmY6CsMMls4rK36b7GX435NGacp78_1EAUqWYujf_akbT_OEx7_GZ5FL0kwYXiBp--_n11NhT1IKij0z3kj-bkjcsx3npgx0ay6le141jd2PPh58oo1YjP5nXHRq4dfMU5TMNC9e8sAuaqACTswwBth6UUaE6Lr3JR_NAyYj1YRh36Jvm6Aq7ewGU6wk2ip--CLTr8-s9jkAAkJ7t8t4npTfbdiIbinoEmv-w5PPwPPXA==)
26. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtDnQq4nwwg1yITWIMZQ6XfIZOBh6WvJqa99USqT4C26aLhXxzraSbhSvir32MdX-XFCIkUvmvM7noRVlkX4O_HsKXIHX-n0VfbiTjYrkOj-b2KLBOVudV)
27. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH03nipZVxPtMMZVBvSFmUbY0_VCeV8JGtNW2S9zo4Esk7nO1UX5-ZdvghaV70y89qClctVRKrJJD8KFW4KtdWmsFTr72LnNQzVYLyPo89cxSRPGrGXrtxbW7A3oATx_psvR1m8THs=)
28. [carat.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4KATkxiafHUkPwL-kURVJ6FGhYq9nEVgvNgur-LOXn0AxPqvN6QVPOwgA16umo4_f3Fr84JJ-NEXmLRfmYkzdce4xQGLX-ENIb-YLLIXoIucUnPG2mH48duLOwckJ8jg9TF7cNGttRB1_6y5yCXvNbuP2huTisE6Edk6RAoUC0rTlkfDFfxPqyrKj5tj2Mdli-w==)
29. [searchenginejournal.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMVe_N5oEkY0y4VCftL9NThDUlAw4sbptlVOguiZjZfvBYE9zRA6pnbnojzTpoV86Ya4s6nnmRjKeUVfObQbY9Qf_5sU1bmqC_Vm9_Uzenb007cS1Wgxhh0we2KnMfyc06jfExt8DWw6oWdnSp9eVoGjOdMIAwU0yTm3hWN9drqzbzfNE-Wg9Ja0Zjv_I_F2-R5QqUXONAuB7TwmZW)


## Annotations
Annotation(end_index=2470, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcJwL8WHwtubLOIsREhojpwAADztDkkT0jwnRKCnD3hIV8qkUP4bZw0Wm4RwspuMa2DLmo7l31eijf7kfPnD2mmRGTzu52CoUeoBxYZYssSEAPdvSc2lrDBIfTcu30Knmw2SRN-uzPj2LPQdzVQHv5yCoyrEf9c1i9pOL3w9RlVaLvxJku3Vh_ZhYZCc1Uv6L8YNeflJ9fmXE=', start_index=2461)
Annotation(end_index=2660, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwnZYCNbRM58W_tI3jc9l_V9oaYnn0pldAtUg-KtEHVpVxFKqOi0lObKHYpqepvtzaTdROZfPjArjkhvph--26tAvKUFX1OzraineHahI15Wpt2ZYixpZiz64WZtcL84E86-7w3iNrUWVTZ2v6EP2IwllJKFHY3d3SN5dsrBJ4_-m2LNhg6PNHLA==', start_index=2651)
Annotation(end_index=2958, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfDLxBJwc94NF37CT4i__vdsiXc2Zr_2i3Nn5WLy5klcAiECMmOazLjoOwgwYK7H-fUsUoOu2Jqg1Q7CRTmlIa9w1AiGboJ-SFVu_jZkEz3hq4Ab5fPj1RTKCASCxBMpsn6Z2QqoPvSoiD3Oo0K-nxbkCqwjtcbU0=', start_index=2946)
Annotation(end_index=2958, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmPkBVi4f8sssGrnNcz30tvx_MTiHNQk7Np3pN6MzDBZJqvcGbkWLGaXTJ3hOE5OblQ2Q500FnFYrut3jrAIky0KfbGv7m1EYA2v7asdJv5UkZu5SU', start_index=2946)
Annotation(end_index=4089, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcJwL8WHwtubLOIsREhojpwAADztDkkT0jwnRKCnD3hIV8qkUP4bZw0Wm4RwspuMa2DLmo7l31eijf7kfPnD2mmRGTzu52CoUeoBxYZYssSEAPdvSc2lrDBIfTcu30Knmw2SRN-uzPj2LPQdzVQHv5yCoyrEf9c1i9pOL3w9RlVaLvxJku3Vh_ZhYZCc1Uv6L8YNeflJ9fmXE=', start_index=4080)
Annotation(end_index=4310, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyLt6PkLJNPhZacRHk6K0nh2cZl0Kw0QN2_3B1WjNOIKDkqUU33Lk-5j3swm3Vcer2xDBc5Bft0LTXHxGlS_4DB4wNQmNhyFJVoH6vezrIpZgZcrNivkVOkQVa1O6mfwdT4bJ3PV1qHDKUqekAa4ugxoXGHDzKobL4i6HwS6JgBjaH62msBr3Qu3e3W578XWALsYByhCd0zWpAdjTp91BE7EsAoWkaL5lvO9L2sWQuP0ijWE9VTXO_3Q==', start_index=4301)
Annotation(end_index=4674, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBLZaKq4GrdbNbTLsNZMirw2ud_LUyXspdQKvhjayP1oZFKYnDmfi97H0LqgE66DeVAfkSYIcDsCPhgFs19h8uice1Vl6yT93Tv9ymSzHrViMLIdyo5wsHV4IxfMFn-Sobp1zYryPfRB2scDzeCF9-97loGLi617Iym8mSwzRu3w==', start_index=4662)
Annotation(end_index=4674, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcJwL8WHwtubLOIsREhojpwAADztDkkT0jwnRKCnD3hIV8qkUP4bZw0Wm4RwspuMa2DLmo7l31eijf7kfPnD2mmRGTzu52CoUeoBxYZYssSEAPdvSc2lrDBIfTcu30Knmw2SRN-uzPj2LPQdzVQHv5yCoyrEf9c1i9pOL3w9RlVaLvxJku3Vh_ZhYZCc1Uv6L8YNeflJ9fmXE=', start_index=4662)
Annotation(end_index=5144, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwnZYCNbRM58W_tI3jc9l_V9oaYnn0pldAtUg-KtEHVpVxFKqOi0lObKHYpqepvtzaTdROZfPjArjkhvph--26tAvKUFX1OzraineHahI15Wpt2ZYixpZiz64WZtcL84E86-7w3iNrUWVTZ2v6EP2IwllJKFHY3d3SN5dsrBJ4_-m2LNhg6PNHLA==', start_index=5135)
Annotation(end_index=5467, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwnZYCNbRM58W_tI3jc9l_V9oaYnn0pldAtUg-KtEHVpVxFKqOi0lObKHYpqepvtzaTdROZfPjArjkhvph--26tAvKUFX1OzraineHahI15Wpt2ZYixpZiz64WZtcL84E86-7w3iNrUWVTZ2v6EP2IwllJKFHY3d3SN5dsrBJ4_-m2LNhg6PNHLA==', start_index=5458)
Annotation(end_index=5819, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5K9Cbt9CHfS-RmFtBmBhCiTyzqDKKFGwG6b66GkkqpGTJzkmaNmyAmpEkuy1xNl-Ftt-FJaFK1TREflz4wd6-R7TFb3wm6QKR9cZW34f9G4G8xoNAucln1_WuRU8TbMRCYpeZGdfOudR44rByGIj05LOtyEIkSSJNlRFCiWBkr4IQMU0hLVcpDEM=', start_index=5810)
Annotation(end_index=6161, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3Up_db33VQLO3L6R1SrA0Et8sTFpQ7m1LNClwMRQI0wR3lWw8Cw6JtVGA98G2zDv9rL0MC3_EbXdzZ-QhINDXw6djvrnBE6Y1dO-ogFOCoXMm2vLM_2grPdKdLnQIGxC1qRlhAuBmLkysZWoWi4Ce5LUMZf3X9fi3QfoskScAI616tpRPLxSkZDu6RwQ1EKq9I8xihcGKK1Q=', start_index=6152)
Annotation(end_index=6492, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3Up_db33VQLO3L6R1SrA0Et8sTFpQ7m1LNClwMRQI0wR3lWw8Cw6JtVGA98G2zDv9rL0MC3_EbXdzZ-QhINDXw6djvrnBE6Y1dO-ogFOCoXMm2vLM_2grPdKdLnQIGxC1qRlhAuBmLkysZWoWi4Ce5LUMZf3X9fi3QfoskScAI616tpRPLxSkZDu6RwQ1EKq9I8xihcGKK1Q=', start_index=6483)
Annotation(end_index=6700, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEk_WvVHiujr5KnH-YlceIP11Ariz3-_bdo52v7SQsbruLPstdB0h2i6QINTHwY3tR7APeLAa6EMlvl50Mdva4CL_QLhIEwUUOt3zfiIOnIZvjosqrCDpw2Kcnb2dZt1vuAY2odHCpCMBYkJX71U6CPSIn8D8N49XK8QRCxWSo=', start_index=6691)
Annotation(end_index=6881, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBLZaKq4GrdbNbTLsNZMirw2ud_LUyXspdQKvhjayP1oZFKYnDmfi97H0LqgE66DeVAfkSYIcDsCPhgFs19h8uice1Vl6yT93Tv9ymSzHrViMLIdyo5wsHV4IxfMFn-Sobp1zYryPfRB2scDzeCF9-97loGLi617Iym8mSwzRu3w==', start_index=6872)
Annotation(end_index=7481, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAi5q0cP3WEvgpZat9HAia72LZM0_Udft5ymRDMGdiAsRKYgAXYBfPU85ftQS5bjm6U9QUE33wjvM-6qdurR_Vb7poTdVaofWuKICuuo4pRdtib8ybLff_6TfNFl-YweRiwklWctAr', start_index=7467)
Annotation(end_index=7481, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLC-GgCzVnt8L1iOhGizUKNkvpso_y8utDvMrNpYYFbGZE2FSaefLf4WnBxQYCt7EgS9uFhFtig6dfNPUWEiFR-WjhlkJ6RakdNB0Kpn4QKHi78DInTM_GnmQmUTvEHCk=', start_index=7467)
Annotation(end_index=7747, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAZFbIoKclmX93b63IBxywS9Rb4X6zBNfFtzcUTCdhI2oePtoOmTvKOF97BPP83wV9Gn4nhwwZsa8uZtwrgU6ObprW-3vzYvh4zXIf9x3DKon2H5dnpaYQmmNMtAnyCV4v7OktVx6Qv7ROVa3nEOezaVSB_-AZ8ooIezlT0PD04L6x1Al-pW0Z9MOvb-WP97Zw465lZ7PE', start_index=7737)
Annotation(end_index=8112, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEutMMF9Mj3kyagaapTcLNR2XuIRBBa6KL0_ZqVUgAeNjb67YcTAX7_SoOjxCeSr8OC1FN7G8NEwAcTfeJGd14lhxFQg4MNLAoKdtv6HsXPUnr6UPy1eHvL', start_index=8102)
Annotation(end_index=8466, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGiqrdIGkUMLq59DXixmiip_vmJfv3t33Yts3MLA29HMc_5gyINFxpCLNzZaa37B97eGOsvPsu2mtUnCJ9PCPR2aYhyEFPd3yQtC_Cj_scATy7abU4IspeBzhqMvneXZMCNK5IE15eN', start_index=8456)
Annotation(end_index=8864, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnkH3NJuWXqpY3Du_5FvMRiQJ_g1vJH1VE7dVBwsWgEjAeMEetIDWPZHIPSEAM_CUsNMwpLAw_HSVAeeJhQqnSma2c1QL1M416wGTv1TDXycAEVkV_JztT0PySJOHRARsSklJZX6aafvBx46klKJ-34pxh915LV2b6lWaiwTtxZH9GgNCDy1gTp15KifmFaBjMocCnoxnNpy3WgpcpHHxsddoEr_5fe9NfuzjZ1CZf', start_index=8850)
Annotation(end_index=8864, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGiqrdIGkUMLq59DXixmiip_vmJfv3t33Yts3MLA29HMc_5gyINFxpCLNzZaa37B97eGOsvPsu2mtUnCJ9PCPR2aYhyEFPd3yQtC_Cj_scATy7abU4IspeBzhqMvneXZMCNK5IE15eN', start_index=8850)
Annotation(end_index=9368, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmPkBVi4f8sssGrnNcz30tvx_MTiHNQk7Np3pN6MzDBZJqvcGbkWLGaXTJ3hOE5OblQ2Q500FnFYrut3jrAIky0KfbGv7m1EYA2v7asdJv5UkZu5SU', start_index=9359)
Annotation(end_index=9608, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmPkBVi4f8sssGrnNcz30tvx_MTiHNQk7Np3pN6MzDBZJqvcGbkWLGaXTJ3hOE5OblQ2Q500FnFYrut3jrAIky0KfbGv7m1EYA2v7asdJv5UkZu5SU', start_index=9599)
Annotation(end_index=10447, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERftMNlofkuc0NhGDpiqX-tOHws3IQc_dyxw9W8SyO9LXXLCeoNXjxEuaVWW_M_NvF8GLHmwRt6nnNdaj7F4d0qKupIYGj4X7P3pX99nlRCn8kEAKHNCRyICOGOEwfWbst80BIqLC3w28BEXLa7ysk5qB0ago2Fz_Cb8c95B3fzgBCwUb1xe9oHwgjAIQEiqKpRYqtew-sNxhIbZtGP1fPAPBsITcWvgTlFTTjousEV3YWnXbF9YT2YlT3bXcR9dZVgkmlFpQ=', start_index=10433)
Annotation(end_index=10447, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSA_utGT6gZ8x-G13RkoKrAgUj_kAm3NdtFR9n35qL_7Z5LBsFNq34hITdj2lkWvD8-QYs09XQxsK1IT3yg9MDZvAdMqJ6-TVaX5yp7U6OHvPmO0dYzSzSmH4Tjg==', start_index=10433)
Annotation(end_index=10704, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERftMNlofkuc0NhGDpiqX-tOHws3IQc_dyxw9W8SyO9LXXLCeoNXjxEuaVWW_M_NvF8GLHmwRt6nnNdaj7F4d0qKupIYGj4X7P3pX99nlRCn8kEAKHNCRyICOGOEwfWbst80BIqLC3w28BEXLa7ysk5qB0ago2Fz_Cb8c95B3fzgBCwUb1xe9oHwgjAIQEiqKpRYqtew-sNxhIbZtGP1fPAPBsITcWvgTlFTTjousEV3YWnXbF9YT2YlT3bXcR9dZVgkmlFpQ=', start_index=10694)
Annotation(end_index=11052, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEutMMF9Mj3kyagaapTcLNR2XuIRBBa6KL0_ZqVUgAeNjb67YcTAX7_SoOjxCeSr8OC1FN7G8NEwAcTfeJGd14lhxFQg4MNLAoKdtv6HsXPUnr6UPy1eHvL', start_index=11042)
Annotation(end_index=11391, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiA2Ok9-8BNuFHPY11dkq8WTn5YBmwVazJZm_PKzXykHC6NlDSzVr_8Uas9iRKPW4Z2tlYXIkqBOjEVksYXovUKQNr1DWpjrbhlgGTAkDrsJgpngsj_nJmZv6-zw==', start_index=11381)
Annotation(end_index=11785, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrnHjAYtImo8D-l_foXBdjMb01qkZSjOrORCkERguzAbzWxkSydhXagnm2Xv9yp3vv9afZu2kgDbbI3w6-SP6gmNA9L2NBESNn358mIy63AEAhmkqPPacF-i7HPCaImJrDXwLh1x4tjYdbtejymP7DrEF3n73BgFVgX65PdOCgNbD2JegnqQM=', start_index=11775)
Annotation(end_index=12081, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrnHjAYtImo8D-l_foXBdjMb01qkZSjOrORCkERguzAbzWxkSydhXagnm2Xv9yp3vv9afZu2kgDbbI3w6-SP6gmNA9L2NBESNn358mIy63AEAhmkqPPacF-i7HPCaImJrDXwLh1x4tjYdbtejymP7DrEF3n73BgFVgX65PdOCgNbD2JegnqQM=', start_index=12067)
Annotation(end_index=12081, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2r_Dq8KWSutcgxwxW8CkXD_VN2w-eoVWMH6c21-un5QRgirFxWXcb1w-9GpZlpa86USOwDmARCcoQfYpBBQ7Z4aH6MWp9_KRTNCVgEUpcr3AOeJZ6fs1c', start_index=12067)
Annotation(end_index=12612, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEj46uNt-zlYpUsQbSDMBFh78od-ErX8PnSljJoV0qMTXNLtm40SvOmHLPLUsl0HqtgDGOAwhji3cgjXnzxRzOJubKoRmPMCUBtMn9ONp8pm8vpbiF3AIwg', start_index=12599)
Annotation(end_index=12612, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyLt6PkLJNPhZacRHk6K0nh2cZl0Kw0QN2_3B1WjNOIKDkqUU33Lk-5j3swm3Vcer2xDBc5Bft0LTXHxGlS_4DB4wNQmNhyFJVoH6vezrIpZgZcrNivkVOkQVa1O6mfwdT4bJ3PV1qHDKUqekAa4ugxoXGHDzKobL4i6HwS6JgBjaH62msBr3Qu3e3W578XWALsYByhCd0zWpAdjTp91BE7EsAoWkaL5lvO9L2sWQuP0ijWE9VTXO_3Q==', start_index=12599)
Annotation(end_index=12857, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmPkBVi4f8sssGrnNcz30tvx_MTiHNQk7Np3pN6MzDBZJqvcGbkWLGaXTJ3hOE5OblQ2Q500FnFYrut3jrAIky0KfbGv7m1EYA2v7asdJv5UkZu5SU', start_index=12848)
Annotation(end_index=13308, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZwc14HvgbogMctsSklER63DnNjxU4VtO4qnloXwF3QmhxHNxmWDBwq4LsMMKy_O0ZYSt2TxCPAqLUhFqAwcUFWDuP3D8gaCRLfR4qrNrFc5rsfNUn0Jme3hMWLKxBdQKrxpJDIXM1amO4qgezquR7RKy36yndkLMkncAiJ5qfGM-ttKWU66TQNwjz1nuK2lofzBo=', start_index=13295)
Annotation(end_index=13308, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfDLxBJwc94NF37CT4i__vdsiXc2Zr_2i3Nn5WLy5klcAiECMmOazLjoOwgwYK7H-fUsUoOu2Jqg1Q7CRTmlIa9w1AiGboJ-SFVu_jZkEz3hq4Ab5fPj1RTKCASCxBMpsn6Z2QqoPvSoiD3Oo0K-nxbkCqwjtcbU0=', start_index=13295)
Annotation(end_index=13550, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjFbtk2_8xsFEIU0aEuKHOiD1pTlLfZuYwTfRJW5n5kJHZcJLhsHDEAm9b7YVojvbXwkLARQRr2kSzHZ_iJh0ewJbwwYJ0PFVtKZzzSoiQ4PUFYouv8u47zX7oiL_wlk8M1T0U4GGcF0EMvhtzSFmmxbrccDRbf36PC_bCFKetavg3ClRynVidPdOuOAt6WaVLY0mU01w6zktxVNxdR78JG1EirVTMd7IGTIWuY4op5pEIRzNlnbywx9pT', start_index=13540)
Annotation(end_index=13957, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjFbtk2_8xsFEIU0aEuKHOiD1pTlLfZuYwTfRJW5n5kJHZcJLhsHDEAm9b7YVojvbXwkLARQRr2kSzHZ_iJh0ewJbwwYJ0PFVtKZzzSoiQ4PUFYouv8u47zX7oiL_wlk8M1T0U4GGcF0EMvhtzSFmmxbrccDRbf36PC_bCFKetavg3ClRynVidPdOuOAt6WaVLY0mU01w6zktxVNxdR78JG1EirVTMd7IGTIWuY4op5pEIRzNlnbywx9pT', start_index=13943)
Annotation(end_index=13957, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxlOQXiOTHPbRFCSVOjDF3dlnPKBX4RM3vxotJXFl7PWJ2WntVGtgkPukhxIN1HaS5egKE9i-rbQa6x9dvyZdnZozh_T4PUwIy7Yrj6jr74gipgmQ-weUoHAU3mg31', start_index=13943)
Annotation(end_index=14132, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwDe2vrljTXjIPZDmY6CsMMls4rK36b7GX435NGacp78_1EAUqWYujf_akbT_OEx7_GZ5FL0kwYXiBp--_n11NhT1IKij0z3kj-bkjcsx3npgx0ay6le141jd2PPh58oo1YjP5nXHRq4dfMU5TMNC9e8sAuaqACTswwBth6UUaE6Lr3JR_NAyYj1YRh36Jvm6Aq7ewGU6wk2ip--CLTr8-s9jkAAkJ7t8t4npTfbdiIbinoEmv-w5PPwPPXA==', start_index=14122)
Annotation(end_index=14462, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtDnQq4nwwg1yITWIMZQ6XfIZOBh6WvJqa99USqT4C26aLhXxzraSbhSvir32MdX-XFCIkUvmvM7noRVlkX4O_HsKXIHX-n0VfbiTjYrkOj-b2KLBOVudV', start_index=14452)
Annotation(end_index=14789, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH03nipZVxPtMMZVBvSFmUbY0_VCeV8JGtNW2S9zo4Esk7nO1UX5-ZdvghaV70y89qClctVRKrJJD8KFW4KtdWmsFTr72LnNQzVYLyPo89cxSRPGrGXrtxbW7A3oATx_psvR1m8THs=', start_index=14779)
Annotation(end_index=15450, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnkH3NJuWXqpY3Du_5FvMRiQJ_g1vJH1VE7dVBwsWgEjAeMEetIDWPZHIPSEAM_CUsNMwpLAw_HSVAeeJhQqnSma2c1QL1M416wGTv1TDXycAEVkV_JztT0PySJOHRARsSklJZX6aafvBx46klKJ-34pxh915LV2b6lWaiwTtxZH9GgNCDy1gTp15KifmFaBjMocCnoxnNpy3WgpcpHHxsddoEr_5fe9NfuzjZ1CZf', start_index=15436)
Annotation(end_index=15450, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGiqrdIGkUMLq59DXixmiip_vmJfv3t33Yts3MLA29HMc_5gyINFxpCLNzZaa37B97eGOsvPsu2mtUnCJ9PCPR2aYhyEFPd3yQtC_Cj_scATy7abU4IspeBzhqMvneXZMCNK5IE15eN', start_index=15436)
Annotation(end_index=15692, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnkH3NJuWXqpY3Du_5FvMRiQJ_g1vJH1VE7dVBwsWgEjAeMEetIDWPZHIPSEAM_CUsNMwpLAw_HSVAeeJhQqnSma2c1QL1M416wGTv1TDXycAEVkV_JztT0PySJOHRARsSklJZX6aafvBx46klKJ-34pxh915LV2b6lWaiwTtxZH9GgNCDy1gTp15KifmFaBjMocCnoxnNpy3WgpcpHHxsddoEr_5fe9NfuzjZ1CZf', start_index=15682)
Annotation(end_index=16030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBLZaKq4GrdbNbTLsNZMirw2ud_LUyXspdQKvhjayP1oZFKYnDmfi97H0LqgE66DeVAfkSYIcDsCPhgFs19h8uice1Vl6yT93Tv9ymSzHrViMLIdyo5wsHV4IxfMFn-Sobp1zYryPfRB2scDzeCF9-97loGLi617Iym8mSwzRu3w==', start_index=16018)
Annotation(end_index=16030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcJwL8WHwtubLOIsREhojpwAADztDkkT0jwnRKCnD3hIV8qkUP4bZw0Wm4RwspuMa2DLmo7l31eijf7kfPnD2mmRGTzu52CoUeoBxYZYssSEAPdvSc2lrDBIfTcu30Knmw2SRN-uzPj2LPQdzVQHv5yCoyrEf9c1i9pOL3w9RlVaLvxJku3Vh_ZhYZCc1Uv6L8YNeflJ9fmXE=', start_index=16018)
Annotation(end_index=16267, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4KATkxiafHUkPwL-kURVJ6FGhYq9nEVgvNgur-LOXn0AxPqvN6QVPOwgA16umo4_f3Fr84JJ-NEXmLRfmYkzdce4xQGLX-ENIb-YLLIXoIucUnPG2mH48duLOwckJ8jg9TF7cNGttRB1_6y5yCXvNbuP2huTisE6Edk6RAoUC0rTlkfDFfxPqyrKj5tj2Mdli-w==', start_index=16257)
Annotation(end_index=16602, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEj46uNt-zlYpUsQbSDMBFh78od-ErX8PnSljJoV0qMTXNLtm40SvOmHLPLUsl0HqtgDGOAwhji3cgjXnzxRzOJubKoRmPMCUBtMn9ONp8pm8vpbiF3AIwg', start_index=16588)
Annotation(end_index=16602, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSA_utGT6gZ8x-G13RkoKrAgUj_kAm3NdtFR9n35qL_7Z5LBsFNq34hITdj2lkWvD8-QYs09XQxsK1IT3yg9MDZvAdMqJ6-TVaX5yp7U6OHvPmO0dYzSzSmH4Tjg==', start_index=16588)
Annotation(end_index=16857, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSA_utGT6gZ8x-G13RkoKrAgUj_kAm3NdtFR9n35qL_7Z5LBsFNq34hITdj2lkWvD8-QYs09XQxsK1IT3yg9MDZvAdMqJ6-TVaX5yp7U6OHvPmO0dYzSzSmH4Tjg==', start_index=16847)
Annotation(end_index=18519, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcJwL8WHwtubLOIsREhojpwAADztDkkT0jwnRKCnD3hIV8qkUP4bZw0Wm4RwspuMa2DLmo7l31eijf7kfPnD2mmRGTzu52CoUeoBxYZYssSEAPdvSc2lrDBIfTcu30Knmw2SRN-uzPj2LPQdzVQHv5yCoyrEf9c1i9pOL3w9RlVaLvxJku3Vh_ZhYZCc1Uv6L8YNeflJ9fmXE=', start_index=18507)
Annotation(end_index=18519, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3Up_db33VQLO3L6R1SrA0Et8sTFpQ7m1LNClwMRQI0wR3lWw8Cw6JtVGA98G2zDv9rL0MC3_EbXdzZ-QhINDXw6djvrnBE6Y1dO-ogFOCoXMm2vLM_2grPdKdLnQIGxC1qRlhAuBmLkysZWoWi4Ce5LUMZf3X9fi3QfoskScAI616tpRPLxSkZDu6RwQ1EKq9I8xihcGKK1Q=', start_index=18507)
Annotation(end_index=18590, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEk_WvVHiujr5KnH-YlceIP11Ariz3-_bdo52v7SQsbruLPstdB0h2i6QINTHwY3tR7APeLAa6EMlvl50Mdva4CL_QLhIEwUUOt3zfiIOnIZvjosqrCDpw2Kcnb2dZt1vuAY2odHCpCMBYkJX71U6CPSIn8D8N49XK8QRCxWSo=', start_index=18577)
Annotation(end_index=18590, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMVe_N5oEkY0y4VCftL9NThDUlAw4sbptlVOguiZjZfvBYE9zRA6pnbnojzTpoV86Ya4s6nnmRjKeUVfObQbY9Qf_5sU1bmqC_Vm9_Uzenb007cS1Wgxhh0we2KnMfyc06jfExt8DWw6oWdnSp9eVoGjOdMIAwU0yTm3hWN9drqzbzfNE-Wg9Ja0Zjv_I_F2-R5QqUXONAuB7TwmZW', start_index=18577)
Annotation(end_index=18669, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwnZYCNbRM58W_tI3jc9l_V9oaYnn0pldAtUg-KtEHVpVxFKqOi0lObKHYpqepvtzaTdROZfPjArjkhvph--26tAvKUFX1OzraineHahI15Wpt2ZYixpZiz64WZtcL84E86-7w3iNrUWVTZ2v6EP2IwllJKFHY3d3SN5dsrBJ4_-m2LNhg6PNHLA==', start_index=18660)
Annotation(end_index=18714, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5K9Cbt9CHfS-RmFtBmBhCiTyzqDKKFGwG6b66GkkqpGTJzkmaNmyAmpEkuy1xNl-Ftt-FJaFK1TREflz4wd6-R7TFb3wm6QKR9cZW34f9G4G8xoNAucln1_WuRU8TbMRCYpeZGdfOudR44rByGIj05LOtyEIkSSJNlRFCiWBkr4IQMU0hLVcpDEM=', start_index=18702)
Annotation(end_index=18714, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBLZaKq4GrdbNbTLsNZMirw2ud_LUyXspdQKvhjayP1oZFKYnDmfi97H0LqgE66DeVAfkSYIcDsCPhgFs19h8uice1Vl6yT93Tv9ymSzHrViMLIdyo5wsHV4IxfMFn-Sobp1zYryPfRB2scDzeCF9-97loGLi617Iym8mSwzRu3w==', start_index=18702)
Annotation(end_index=18797, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnkH3NJuWXqpY3Du_5FvMRiQJ_g1vJH1VE7dVBwsWgEjAeMEetIDWPZHIPSEAM_CUsNMwpLAw_HSVAeeJhQqnSma2c1QL1M416wGTv1TDXycAEVkV_JztT0PySJOHRARsSklJZX6aafvBx46klKJ-34pxh915LV2b6lWaiwTtxZH9GgNCDy1gTp15KifmFaBjMocCnoxnNpy3WgpcpHHxsddoEr_5fe9NfuzjZ1CZf', start_index=18783)
Annotation(end_index=18797, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGiqrdIGkUMLq59DXixmiip_vmJfv3t33Yts3MLA29HMc_5gyINFxpCLNzZaa37B97eGOsvPsu2mtUnCJ9PCPR2aYhyEFPd3yQtC_Cj_scATy7abU4IspeBzhqMvneXZMCNK5IE15eN', start_index=18783)
Annotation(end_index=18869, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmPkBVi4f8sssGrnNcz30tvx_MTiHNQk7Np3pN6MzDBZJqvcGbkWLGaXTJ3hOE5OblQ2Q500FnFYrut3jrAIky0KfbGv7m1EYA2v7asdJv5UkZu5SU', start_index=18860)
Annotation(end_index=18943, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrnHjAYtImo8D-l_foXBdjMb01qkZSjOrORCkERguzAbzWxkSydhXagnm2Xv9yp3vv9afZu2kgDbbI3w6-SP6gmNA9L2NBESNn358mIy63AEAhmkqPPacF-i7HPCaImJrDXwLh1x4tjYdbtejymP7DrEF3n73BgFVgX65PdOCgNbD2JegnqQM=', start_index=18933)
Annotation(end_index=19013, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEj46uNt-zlYpUsQbSDMBFh78od-ErX8PnSljJoV0qMTXNLtm40SvOmHLPLUsl0HqtgDGOAwhji3cgjXnzxRzOJubKoRmPMCUBtMn9ONp8pm8vpbiF3AIwg', start_index=19000)
Annotation(end_index=19013, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyLt6PkLJNPhZacRHk6K0nh2cZl0Kw0QN2_3B1WjNOIKDkqUU33Lk-5j3swm3Vcer2xDBc5Bft0LTXHxGlS_4DB4wNQmNhyFJVoH6vezrIpZgZcrNivkVOkQVa1O6mfwdT4bJ3PV1qHDKUqekAa4ugxoXGHDzKobL4i6HwS6JgBjaH62msBr3Qu3e3W578XWALsYByhCd0zWpAdjTp91BE7EsAoWkaL5lvO9L2sWQuP0ijWE9VTXO_3Q==', start_index=19000)
Annotation(end_index=19087, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAi5q0cP3WEvgpZat9HAia72LZM0_Udft5ymRDMGdiAsRKYgAXYBfPU85ftQS5bjm6U9QUE33wjvM-6qdurR_Vb7poTdVaofWuKICuuo4pRdtib8ybLff_6TfNFl-YweRiwklWctAr', start_index=19073)
Annotation(end_index=19087, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLC-GgCzVnt8L1iOhGizUKNkvpso_y8utDvMrNpYYFbGZE2FSaefLf4WnBxQYCt7EgS9uFhFtig6dfNPUWEiFR-WjhlkJ6RakdNB0Kpn4QKHi78DInTM_GnmQmUTvEHCk=', start_index=19073)
Annotation(end_index=19140, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZwc14HvgbogMctsSklER63DnNjxU4VtO4qnloXwF3QmhxHNxmWDBwq4LsMMKy_O0ZYSt2TxCPAqLUhFqAwcUFWDuP3D8gaCRLfR4qrNrFc5rsfNUn0Jme3hMWLKxBdQKrxpJDIXM1amO4qgezquR7RKy36yndkLMkncAiJ5qfGM-ttKWU66TQNwjz1nuK2lofzBo=', start_index=19127)
Annotation(end_index=19140, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfDLxBJwc94NF37CT4i__vdsiXc2Zr_2i3Nn5WLy5klcAiECMmOazLjoOwgwYK7H-fUsUoOu2Jqg1Q7CRTmlIa9w1AiGboJ-SFVu_jZkEz3hq4Ab5fPj1RTKCASCxBMpsn6Z2QqoPvSoiD3Oo0K-nxbkCqwjtcbU0=', start_index=19127)
Annotation(end_index=19215, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjFbtk2_8xsFEIU0aEuKHOiD1pTlLfZuYwTfRJW5n5kJHZcJLhsHDEAm9b7YVojvbXwkLARQRr2kSzHZ_iJh0ewJbwwYJ0PFVtKZzzSoiQ4PUFYouv8u47zX7oiL_wlk8M1T0U4GGcF0EMvhtzSFmmxbrccDRbf36PC_bCFKetavg3ClRynVidPdOuOAt6WaVLY0mU01w6zktxVNxdR78JG1EirVTMd7IGTIWuY4op5pEIRzNlnbywx9pT', start_index=19201)
Annotation(end_index=19215, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxlOQXiOTHPbRFCSVOjDF3dlnPKBX4RM3vxotJXFl7PWJ2WntVGtgkPukhxIN1HaS5egKE9i-rbQa6x9dvyZdnZozh_T4PUwIy7Yrj6jr74gipgmQ-weUoHAU3mg31', start_index=19201)
Annotation(end_index=19292, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH03nipZVxPtMMZVBvSFmUbY0_VCeV8JGtNW2S9zo4Esk7nO1UX5-ZdvghaV70y89qClctVRKrJJD8KFW4KtdWmsFTr72LnNQzVYLyPo89cxSRPGrGXrtxbW7A3oATx_psvR1m8THs=', start_index=19282)
Annotation(end_index=19367, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERftMNlofkuc0NhGDpiqX-tOHws3IQc_dyxw9W8SyO9LXXLCeoNXjxEuaVWW_M_NvF8GLHmwRt6nnNdaj7F4d0qKupIYGj4X7P3pX99nlRCn8kEAKHNCRyICOGOEwfWbst80BIqLC3w28BEXLa7ysk5qB0ago2Fz_Cb8c95B3fzgBCwUb1xe9oHwgjAIQEiqKpRYqtew-sNxhIbZtGP1fPAPBsITcWvgTlFTTjousEV3YWnXbF9YT2YlT3bXcR9dZVgkmlFpQ=', start_index=19353)
Annotation(end_index=19367, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSA_utGT6gZ8x-G13RkoKrAgUj_kAm3NdtFR9n35qL_7Z5LBsFNq34hITdj2lkWvD8-QYs09XQxsK1IT3yg9MDZvAdMqJ6-TVaX5yp7U6OHvPmO0dYzSzSmH4Tjg==', start_index=19353)
Annotation(end_index=19452, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEutMMF9Mj3kyagaapTcLNR2XuIRBBa6KL0_ZqVUgAeNjb67YcTAX7_SoOjxCeSr8OC1FN7G8NEwAcTfeJGd14lhxFQg4MNLAoKdtv6HsXPUnr6UPy1eHvL', start_index=19442)

## Sources
