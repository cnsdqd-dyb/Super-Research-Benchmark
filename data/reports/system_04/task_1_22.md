# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 42927f62 | **Time:** 453.31s | **Cost:** $1.52293
--------------------------------------------------------------------------------

# Behavioral Game Theory in Investment: Rational Equilibrium, Bias Correction, and Prospect Theory Parameterization

### Key Points
*   **Behavioral Game Theory (BGT) as a Synthesis:** BGT does not strictly choose between rational equilibrium and bias; rather, it integrates them. Models like the **Quantal Response Equilibrium (QRE)** mathematically balance rational payoff maximization with stochastic error, effectively modeling "better responses" rather than perfect "best responses."
*   **Prospect Theory’s Dominance:** In investment contexts, Prospect Theory (PT) parameterization—specifically the loss aversion coefficient ($\lambda$)—often overrides rational equilibrium predictions. Research indicates that high stakes and stress can **amplify** loss aversion, making the deviation from rationality more pronounced rather than corrected.
*   **Ambiguity of "Bias Correction":** The term "bias correction" functions on two levels:
    *   **Market Level:** "Limits to arbitrage" suggest that rational investors often cannot correct the price distortions caused by biased traders due to risk and cost, allowing anomalies to persist.
    *   **Model Level:** Econometric techniques (e.g., bias-corrected AIC) are used by researchers to accurately estimate behavioral parameters, but this is a statistical tool, not a behavioral mechanism of the investor.
*   **Conclusion:** The evidence suggests that while BGT models attempt to structure a balance via stochastic equilibrium, the **parameterization of Prospect Theory tends to amplify loss aversion effects** in real-world financial scenarios, often preventing convergence to a purely rational equilibrium.

---

## 1. Introduction: The Conflict Between Rationality and Behavior

The study of investment decision-making has traditionally been dominated by the efficient market hypothesis and classical game theory, which posit that agents are rational utility maximizers who form **Rational Expectations Equilibria (REE)** [cite: 1, 2]. In this framework, any deviation from fundamental value is swiftly corrected by arbitrageurs, and agents update their beliefs using Bayes' rule to reach a Nash Equilibrium [cite: 3, 4].

However, persistent market anomalies—such as bubbles, excessive volatility, and the equity premium puzzle—have necessitated the rise of **Behavioral Game Theory (BGT)**. BGT extends classical theory by incorporating psychological regularities, such as bounded rationality, social preferences, and cognitive biases [cite: 1, 5]. The central tension in this field lies between models that attempt to preserve equilibrium through "noisy" rationality (balancing optimization with error) and models that emphasize systematic psychological distortions, particularly **Prospect Theory (PT)**.

This report investigates whether BGT models successfully balance rational equilibrium with bias correction mechanisms or if the parameterization of Prospect Theory reveals a systematic amplification of loss aversion that precludes such balance.

---

## 2. Behavioral Game Theory and the Modeling of Equilibrium

To understand if BGT "balances" rationality and bias, one must examine how it modifies the concept of equilibrium. Unlike traditional theory, which assumes perfect foresight and execution, BGT introduces stochastic elements and cognitive limits.

### 2.1 Quantal Response Equilibrium (QRE): Balancing Rationality and Noise
The most prominent attempt to balance rational equilibrium with behavioral error is the **Quantal Response Equilibrium (QRE)**.
*   **Concept:** QRE generalizes Nash Equilibrium by assuming that players are "better responders" rather than "best responders." Agents calculate expected payoffs but make errors in strategy selection due to bounded rationality or unobserved preference shocks [cite: 6, 7].
*   **The Balance:** QRE introduces a precision parameter (often denoted as $\lambda$ or $\beta$ in logit models). As this parameter approaches infinity, behavior converges to a rational Nash Equilibrium. As it approaches zero, behavior becomes random [cite: 7, 8].
*   **Implication:** QRE provides a structural "balance" by modeling bias as stochastic noise around a rational core. It acknowledges that investors seek higher returns but consistently make errors, allowing the model to fit empirical data where strict rationality fails [cite: 7, 9].

### 2.2 Cognitive Hierarchy and Level-k Models
Another approach to balancing rationality is the **Cognitive Hierarchy (CH)** or Level-k model.
*   **Structure:** These models assume a hierarchy of strategic sophistication. Level-0 players act randomly or non-strategically. Level-1 players best-respond to Level-0, Level-2 to Level-1, and so on [cite: 5, 10].
*   **Bias vs. Correction:** These models do not assume a single equilibrium where beliefs are mutually consistent (as in Nash Equilibrium). Instead, they model a **failure of belief correction**. High-level players attempt to "correct" for the bounded rationality of lower-level players, but the system itself does not necessarily converge to a rational equilibrium unless the population is dominated by infinitely sophisticated agents [cite: 8, 11].

### 2.3 Learning Dynamics and Bias Correction
In dynamic investment games, BGT examines whether agents "learn" their way to equilibrium.
*   **Adaptive Expectations:** Research into "Learning to Forecast" experiments shows that agents often use adaptive rules (looking at past trends) rather than rational expectations.
*   **Failure to Converge:** In environments with positive feedback (e.g., momentum trading), adaptive expectations can lead to persistent deviations from fundamental value. Agents may attempt to correct forecast errors, but without strong negative feedback (mean reversion), these corrections fail to achieve rational equilibrium [cite: 12, 13].

---

## 3. Prospect Theory Parameterization and the Amplification of Loss Aversion

While QRE models bias as "noise," **Prospect Theory (PT)** models bias as a systematic, structural feature of human preference. The query asks if PT parameterization *amplifies* loss aversion effects. The literature strongly supports this, particularly in investment contexts.

### 3.1 The Mechanics of Prospect Theory in Finance
Prospect Theory, developed by Kahneman and Tversky, modifies the utility function in three critical ways [cite: 14, 15, 16]:
1.  **Reference Dependence:** Utility is derived from gains and losses relative to a reference point (e.g., purchase price), not final wealth states.
2.  **Loss Aversion ($\lambda$):** The value function is steeper for losses than for gains. The parameter $\lambda$ typically ranges between 2.0 and 2.5, meaning a loss hurts more than twice as much as an equivalent gain pleases [cite: 14, 17, 18].
3.  **Diminishing Sensitivity ($\alpha$):** The value function is concave for gains (risk aversion) and convex for losses (risk seeking), creating an S-shape [cite: 14, 15].

### 3.2 Amplification Mechanisms
Research indicates that the parameterization of PT is not static; specific conditions in investment decision-making **amplify** the effects of loss aversion, effectively overpowering rational correction.

#### 3.2.1 The Stake Effect
Contrary to the assumption that high stakes force investors to be more rational, empirical studies suggest that **high stakes amplify loss aversion**.
*   **Evidence:** In experiments comparing medium and high stakes, participants exhibited significantly higher loss aversion ($\lambda$) in high-stake scenarios [cite: 19].
*   **Mechanism:** Large absolute outcomes increase the psychological salience of potential losses, causing the loss aversion parameter to increase. This contradicts the "peanut effect" (where people are risk-seeking for small stakes) and suggests that in serious financial decisions, bias is magnified, not corrected [cite: 19].

#### 3.2.2 Stress and Neuroendocrine Amplification
Investment decisions are often made under stress. Neuroeconomic research links the "salience of losses" to stress neuromodulators.
*   **Cortisol and Noradrenaline:** The "salience of losses" hypothesis postulates that stress hormones amplify loss aversion by boosting neural functioning in the amygdala and insula, regions associated with fear and risk processing [cite: 20, 21].
*   **Implication:** During market volatility (high stress), the biological parameterization of loss aversion increases, leading to panic selling or irrational risk-avoidance that diverges further from rational equilibrium [cite: 20].

#### 3.2.3 Contextual and Framing Amplification
The environment in which decisions are made can manipulate PT parameters.
*   **Cyber Security and Risk:** Contexts involving security or "protection" (like insurance or cyber defense) tend to amplify loss aversion due to the framing of "safety" vs. "breach" [cite: 19].
*   **Commercial Exploitation:** Companies (e.g., Apple, Tesla) utilize "active frame construction" to leverage loss aversion. By framing non-purchase as a potential loss (e.g., high repair costs without warranty), they amplify the perceived $\lambda$ to drive consumer behavior, effectively monetizing the bias [cite: 17].

### 3.3 Parameterization Mismatch
A critical finding in BGT is that applying standard experimental parameters (e.g., $\lambda = 2.25$) to market data may actually **understate** the role of Prospect Theory.
*   **Market Data vs. Lab Data:** Research analyzing mutual fund flows suggests that real-world investors exhibit distinct loss aversion and risk-seeking behavior over losses that may differ from lab settings. When parameters are estimated directly from market data, the explanatory power of PT outperforms standard rational asset pricing models [cite: 22, 23].
*   **The Disposition Effect:** The tendency to sell winners too early and hold losers too long is a direct manifestation of PT parameters (convexity in losses, concavity in gains). Standard rational models cannot explain this without assuming implausible friction costs [cite: 24, 25].

---

## 4. Bias Correction: Mechanisms and Failures

The query asks if the model "balances" equilibrium with bias correction. We must distinguish between the *investor's* ability to correct bias and the *market's* ability to correct bias.

### 4.1 Cognitive Bias Correction (The Investor)
Do investors correct their own biases?
*   **Naive Theories of Bias:** The **Flexible Correction Model** suggests that people attempt to correct for biases if they are aware of them. However, this correction is often driven by "naive theories" of how the bias works, leading to either under-correction or over-correction [cite: 26].
*   **Failure in Groups:** In strategic settings, group decision-making does not necessarily correct individual biases. In fact, group dynamics can exacerbate biases like the "better-than-average" effect or trust overestimation, rather than attenuating them [cite: 27].
*   **Forecasting Errors:** In "Learning to Forecast" experiments, agents consistently failed to correct systematic errors in trending markets, leading to collective irrationality rather than rational equilibrium [cite: 12].

### 4.2 Limits to Arbitrage (The Market)
In a rational equilibrium, "smart money" (arbitrageurs) should correct the biases of "noise traders." BGT and behavioral finance argue that this correction mechanism is fundamentally broken due to **Limits to Arbitrage**.
*   **Risky Arbitrage:** Correcting mispricing (e.g., shorting an overvalued stock driven by loss-averse investors) is risky. Prices can diverge further before they converge, forcing arbitrageurs to liquidate at a loss [cite: 2, 4, 28].
*   **Cost-Based Limits:** Transaction costs and short-selling constraints prevent rational agents from fully correcting behavioral anomalies [cite: 29].
*   **Equilibrium of Mispricing:** Consequently, mispricing is not a fleeting disequilibrium but can be a stable **equilibrium outcome** where rational arbitrageurs are constrained, and behavioral biases (amplified by PT parameters) persist [cite: 28, 29].

### 4.3 Statistical Bias Correction (The Researcher)
It is important to note that "bias correction" in the literature often refers to **econometric techniques** used by researchers to estimate BGT models, not the behavior of the agents.
*   **Estimation Bias:** When estimating parameters for QRE or PT, standard maximum likelihood estimators can be biased, especially with small samples. Researchers use methods like **bias-corrected AIC (AICC)** or bootstrap bias correction to accurately recover the "true" behavioral parameters [cite: 8, 30, 31].
*   **Relevance:** This confirms that BGT is rigorous in *measuring* bias, but this statistical correction does not imply that the agents themselves are correcting their behavior.

---

## 5. Synthesis: Balance or Amplification?

The interaction between Rational Equilibrium and Prospect Theory in investment models can be summarized as follows:

### 5.1 The Failure of "Balance"
The idea that BGT "balances" rational equilibrium with bias correction is only partially true in a structural sense (e.g., QRE). However, in terms of *outcomes*, the balance is often lost.
*   **Dominance of Loss Aversion:** In investment contexts, the **amplification** of loss aversion (via stakes, stress, and framing) often overwhelms the rational incentives to converge to equilibrium. The "pull" of the $\lambda$ parameter is stronger than the "pull" of the rational equilibrium, especially when limits to arbitrage prevent market correction [cite: 20, 24, 32].
*   **Asymmetry:** The correction mechanisms (arbitrage, learning) are slow and constrained, while the amplification mechanisms (panic, stress, high stakes) are fast and potent.

### 5.2 The Role of Parameterization
The parameterization of PT is the key driver of this imbalance.
*   **$\lambda > 1$:** The very existence of $\lambda > 1$ ensures that the equilibrium will shift away from the rational benchmark.
*   **Dynamic Parameters:** Because $\lambda$ is not fixed but responds to environmental factors (stress, stakes), investment models that assume a static "balance" fail to predict market crashes or bubbles. Advanced BGT models now attempt to incorporate these dynamic parameters to better explain why "rational" correction fails during crises [cite: 2, 20].

---

## 6. Conclusion

The behavioral game theory model in investment decision-making does **not** successfully balance rational equilibrium with bias correction in the sense of neutralizing the bias. Instead, the evidence overwhelmingly supports the second part of the user's query: **Prospect Theory parameterization amplifies loss aversion effects**, creating persistent deviations from rational equilibrium.

While models like **Quantal Response Equilibrium** provide a mathematical framework to *contain* these deviations within a stochastic equilibrium, the empirical reality of investment—characterized by high stakes, stress, and limits to arbitrage—ensures that loss aversion remains a dominant, amplified force. "Bias correction" exists primarily as a theoretical ideal or a statistical tool for researchers, rather than an effective market mechanism that restores rationality.

### Summary Table: Rational Equilibrium vs. Prospect Theory Amplification

| Feature | Rational Equilibrium / Traditional GT | Behavioral Game Theory / Prospect Theory | Outcome in Investment |
| :--- | :--- | :--- | :--- |
| **Core Assumption** | Utility Maximization (Rational Expectations) | Bounded Rationality, Reference Dependence | Persistent Anomalies (Bubbles, Premium Puzzle) |
| **Equilibrium Concept** | Nash Equilibrium (Best Response) | Quantal Response Equilibrium (Better Response) | Stochastic Equilibrium with Systematic Error |
| **Loss Perception** | Symmetrical (Risk Aversion based on wealth) | Asymmetrical (Loss Aversion $\lambda \approx 2.25$) | **Amplified** sensitivity to losses (Panic selling) |
| **Impact of Stakes** | High stakes induce rationality | High stakes **amplify** loss aversion | Deviation from rationality increases with portfolio size |
| **Correction Mechanism** | Arbitrage (Swift and Complete) | Limits to Arbitrage (Costly and Risky) | Mispricing persists as an equilibrium state |

**Final Verdict:** The BGT model serves to **quantify the amplification** of bias (via PT parameterization) rather than to demonstrate a successful balance with rational equilibrium. The "balance" is structural, but the *weight* is heavily tipped toward behavioral bias.

**Sources:**
1. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGl9lpWSJ5koIkw_J6-oFuQIiNaxhS35gzrORxZo2cVTtoYu32IoUl9NPbIvOj0BIcs-nJxNlrNmBmdabq3C7rs2-4_Z_lDqaLQUYn9DsSkeN69jn7egzRJeC6blKk0HrZlbwoszFLHDXk=)
2. [ijame.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTsPtGHLVvY0E44relJYmUEldeZqENQCyb2Np0VIkmcdyu2LWffTKSiSmPTmupIff_Gx7ceHAJmwsj0I5C7OEA5fAYKXqyaBWhfSA-3jwQYkWU9Oiki9JBXl8IdOjnCcw5OwrWdwVTW10utIhKhmk=)
3. [ucsd.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHERSNJqVltzI-k4ynnyp2WGiYyg1WIi2HQUPd3XJCYWk88gs79UUx4LpbEPmvg2mWlA-v8jTtO2ro6Noi1yuUsnuPn7GQNlgoFOLxcqFJWHg5UG7lmfHSYzhAOKfj684aWkEIqowGT8wNFxANBRON3bz6SlK5oOugFvi0=)
4. [polyu.edu.hk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcv3a9MTjYN7WzMm2ogR631_xik5Wxna-RuwgkQ-yh4JfRsRXLcGeEbhOFMFfCdsFZZoTyuPPAFwfm7maIyrhVxjbmTU31SMn-P_eR1hwMADgrebvGIRR-_5i4TQ57UbyU5HJvF8gqfvKnxp3FfOMmI9WjJHmZPlW9M_ig8_-w)
5. [grokipedia.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPIfIpK40pgemdqscfWFC1-uRmjHa3t4qwrXJYE3uiM_-sHLplFj50wNexDog4H-_qDAWEq8rvES6fxQK2VM3riwuLcqqWqae7zZRuD3WXjicEmoFP1LLA9wEg-83i05lj8401nqni)
6. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOVt5pFaX8z348T_sAktwyOeWN8TdjOsxgNbp_8bDRNPHT0_wJdP9y2j2KR96znwmb6YHSMdhRZDlkjqBGXyvgIG6Fs9BaYowpFC7qxxSi18GO-uxqlhwA2lH186vPKMvA5vf-1uC43IKnxRU7Ej1KINNDM6wvO6ReZyPO5LWjWb4a_C7bEW9RUhCwa_t4HurC3xikMXNNr0vEmzBKwdUQM1OXQ1PMn_K1MUfG)
7. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwFKlOGagluWnrlyTNEaCgGwSK1QlJLpVom7oYhXaBx7KgVxTovCTIRkYxBcFZEaMn6EgB2UVINJTOvKqsFlRuVj4JP4f4PvJv0EHPp_u_kt5NS1kjLNPofhJM83fdmoDmIn1IvcIgUtANjIu1ie0jwPwA)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhNqSnOXpwdPn3QYBnMc7hSUiv4-2H2kLqt_g1mQwCM3j0dDHzXKS8wQHlEFrrQuo4XlpitCNd0hlcghVHw5SDiJOissZ8N7iYlZoOlhh6b98ymCrHmjQVphsKoKwTnQwfDFOrG6Cx5v5IclPgQ2IY9P-V-IGQwJ7KE-bTvQEQCAF1r5JyNHlFRAivdjVMhVWR7bh-C7FCU9u0lj33sco5qhWPyGcGUw==)
9. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFE5GZIcGAp3sch6EeuzHyIL9CJYoi2bWVcImZ5TJUBDgVo-X8BduFNO6yZ9k3FQqRQGSNczrxs3WFEvcLjNp3adgXyZzmZJvmmAKDJc5rMqoRBonsk)
10. [econstor.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFGPnBh84-B5DYT8PkrAh3XAjTHfvCFewT6lHS8Hh9iLhg8ESIVw4_3-orv_rNe-hnJjccA_gdQgv5Rf6D4kOP-aFhvG_RC5W5S0H696QVP2bK4pjnLp-jup3bPFtEgFTZ_4Ojts0UtsB_KHMGIGgyhA==)
11. [arizona.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9QR1w_lE7UATaSri0U7CR9jt-kpaIX6a-HEbJaaWf2FobacXDHzE3Xx7g3e6iR2SL8lss4yiOT0_FoHgBze41SXeIn0Oc_w9MfUC1D7fcLgqlPN7G0Y0eayHu7hiUiK-nQ2dMA9HY94pwaBXmW5ZUmkavDFFxHpSRqkSiGXP4MwnRpmNnbij1jSQyz0OrhbE=)
12. [univpm.it](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1i2sJsTPT9VEnQW9R0ATXQeX-KleZCldnk-ZPJsODiS-Yf8i0dx2t4ZPnPZQnWeUHuBEr8RcJ5EbRi7Lm2NvmE_3xnoo7n9niO0ktgEMboQGxkZJTsE-EolWn-uJGPAEyFat1BIT-L2Y=)
13. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHytjl9BMD-tVmsEOMenjePEHZXD2R2yNe7TEmjAe2pM249DIBqlo7fE18E6eFgK4PTiKfk_ptsfd7al290gj3J3abh8zp4DL5V9iNtLK9A6qLeBkrSv5hD5sJ9M5GOafCLK-oNL92Kp9_OVLm-tKhgbarZRX3MXojIlrQw1iiuS15qk4ydL4KYYbK0e5FZTaiWV-cnRNz6199T9fSpnJo6ucfTubpQkl4=)
14. [diva-portal.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9j6JTSrpTqHzOkUnt69k0zn8uhO8ZybZGM9zm_1dQ2ersAsV53AQBSY0iuonRNZTSVmW-fduxLjthCOAN03aS2EKC6BrOldz9Q1ZELDUJs_3E69qMhrG4MX0gjbKywGJRNu7_Y8Wj3ary4Bs2fwqNZ46ZxLjr)
15. [thedecisionlab.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETkwzDQF5aYxub4WGS3Iuw5rU323Fmnr3O0CifuRfNVuElU_uctuaNYEA4VsIY65nk6kIjnnBfwTETtmnTm30m6SkUjQXF0Z7GbYNiDEFqKaFz2oKMoFri3gmfeRhFtRcSihiKxx_BnTpbimMBRqliQH7XgGdiz9fQ)
16. [investopedia.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZdH8LBZGJdUR566vm5QbkRBkKYXdga3DQRVGFyZUjgqdgsQShTAazCRoeJ2mVQmvME76GX9ZV4Y7KiKE9AyMhy1i7P7TlaLdEUkYvKnkVMs4BE0WvtiEzNf9yCRytMcJferTQwBygIlR-Cao=)
17. [ewadirect.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEj1EfmxLgVp_FimenHW0nuLdo-gkZxKLImXXEIymnEWmmhB3Ua8n2nQlcyf1jECHXT-41sTyN7VeL9Ti9eaB_V9R0iwi7CH_nrJiIXCCKt_9H0pYSGL3EqDWL07kTA71EPdvOYR6b4F_TjNW8k7TthxUMe)
18. [firstsentierinvestors.com.au](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL9ZWd01WMB1GJjht5M3OsjIUtSuH3qk5-wiUSfRYZw7h272AvzAazsKz1gmcUfHyObHNEj3XD57ftPc1a6VLWE8D6KC0hCG-rQJwCf-i8al8axV4qxLwGnXqysIl8YtfnylZZ1pRvHGxYKLUhFSL-LOF_E9mcW3an0TvlpG3sqjruUMnOuTqHNt-49cnAFJqGwxtR90J_9ORzuGUApOYMUXhNjIcEdyE8xp44tV2_nyhS6a_w_mMy6pQm6qDB08jchmEaZw==)
19. [hawaii.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN5pyjJ6Ucocd7LtyUY3FOcJmm6Uf6dQMyQ7jz8IeaP861bh_ZmG7gajs_cGql2mqtq3pqoIqlKn3RdSQgaO0yPnf2DFsaszbV45UNJIzoZne2Lwjte2bErhCH4v9vNSSXH6HAOJJuMQLC7GbM2AT_frFiLkcvOWPtAnhmyKwsmVRlQWciKRQgjN2NXL2OJE2nki8=)
20. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFnJzFgu0aSwyUyNod5Hv0SZhBUsQXjLxpQfyf1PuvYbXNirUcFY22J24X1Ux9Rlw64SUB7UCxCVGKaEkI_KKO5T1eZ4SBlmKpjO7flEUiG71h5rd0OQYCu8B2V5UL7Hu22XkRHIE=)
21. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-kxyAfTeMZ11geQaDkffWBzG45xBh6I_hck4iK4W2-Duw7Wb70bGD7CZZmQyADF8ly1TE_UhP4bwmtkjiXUEAZAxpsiN1-otZq4ir3KohqwQD0TuxonpphG5ba4LJLYjj7gQyTzyp1fge1Rc2kRPJzudvD1cTqjvhf0KYpTg9yEQqnmIuK6XmOl6YEdHNpuI7KFGw-2loZ7cYOVID7wsSMtgHBLxJM-1cnhrJUfS8o_ScAXo=)
22. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2Ke1RfuqET2b-dO0Nznx-nN2awR4yx2-fbCacc2_yWeVSQ8-JbmjiDIiwL5XuXOZRxwnNgs0o-EQUFZfiwHIyt6d25JRz_t4kaWKMbKpvQFP4EcC9ODiT0xahcidUuBRcmkwU3GNJVhzZoT1S4O1corRPkjRs)
23. [aueb.gr](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSrYkG0nfbuyfaTYspXZp0EMj7wtbgla43_TiONMJs3NayyIrwtbOVsNaac58ZYRTlDeJwbifLpdRzJlKCl5L38C6CXL_fq71N8G-ns9wv76XuC0U4oJ_8ZEkI5eBfjELYkAulroUCmDzr27iq8OF1t-e9Fw==)
24. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdAcsqrTw2QozsYGRzvDoIJl-GXZQO3FXVFHEic2y_i4zKnsa0D62Um9dzExzpGnAJkqqPjnoSCYpNZb8qo5QNWN2RJVVwnZ9OREeTE-LWcc6Uq7Zceq_BBoVR)
25. [aalto.fi](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhM-YFbobjEVkcbG6kfXqhw8F-HAVNWTsbmPcy1TritpNLWYsuN9mx64HhoHcGSeo4zuILws4cxUrIEJAFe2J5f36sUnInhdBK47JN4EibGKuVj_FrPJoatXGDukl-lxzLdSjRj6430PPTGXZetthEv28KpsHcxidwpxq00KXlnvyHOTc4MqlWtY_IavAr_kk=)
26. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXmOb1d_NwWgvulIXAcnwsFbBXj1YFtHC8n3F-P1RX5SQ-zJw2NPEVlvhAnzfjB1cc11zf2ej_Bf3c96vrgfD74r1NbacU9p2vltx_RObi6sxlbtjp0LQ3qsUG5Rir4tF9gCL0ijCfnPyN9dN54bIyKUUZbqHLa706oj1YseWBQyT9oqQZFDf18qmXp6YWGzFJkxOLH1iAiAhOxVVah_k4T7wAUESpk9KFE9vGC1fO4KZB1J_lbV6TH9ZDYYPkT_eCxSTfuLw=)
27. [kyoto-su.ac.jp](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjyzm5YUr7hdQ2GdWlUg3dHCJpIQPAF6JIs5Z7URArH9vPOLPuSIeKS4JVDJMXlorcDO2iUAohfd_lXeCNgBYsqaDOCLQbPVANDum9eYH5QAe7ugcQG0uMda5INRCOT8dXE44J1MRfbaGwAb3XggK6llxYgQnUA0U=)
28. [nber.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs5-zOjnojJXmep_sBExJVY26CFgy-Pt_NI5Qr3TGnHtrbtnjqImf1n0zP_ABkjGE0LOLDYc5uciDvk5pN-hErMv6BUw6N3ZCidXDJRAAKwxND0_0vYFAQt7U_2JwgEJHvHyV5I3AYvgUmeFzwMdHIIojAQOe67Q==)
29. [anu.edu.au](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEc-zE359Xp-E5mzKv4TNKJR2M9W7iZOtk6AaTGKQsLFwWz8nGqPCyRag88LLjvP-JyR_ML3iLb3zBWCyssmEl0Za3h7fvhMJzySF7HAmc9ToAM_jTtVhzcZqN2O2ZpFPlWqn9PdLdK85SVN3yzHxl0-7AGeaQc9MY2lj8b07ButCC9PjYDgyiN2XDDJsK49uAhtrWlxr1ZZg==)
30. [nus.edu.sg](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-MTNXSwpjMSBIWv8DuVNt2ELS1cOm_B0CogZ9rULHJEbkAcVHkyMrIkWQqhVOhnDIrCp2wB6RqgyDPFfbX5xkv49bjIZ_5S6dHtEakygQ0f1Z2OfnofcAu_sqJUm4sC4mvfsa-dlujqsMcMFTiHcHJfWZmdzvDiLBnWoa-ZKNgA==)
31. [mit.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNckEEN-P1ZLlRpF_DUmZ9YXJ1pUHPhx4akBr7k6pJr9fybYCgghg9j4a1js7RppsABz9FcztCWxoSNhZ9F-Lx73xrSq8Nrv67Yc_X2yKhHnvGcmURP2ao7jbB9bYOytbcTE9o_4hRSeFXB_ODnm-LwcSElrJCvvBMX-5RK7AIAcsQA5s97eMDhxVkynhwQ6IhXA==)
32. [tucl.edu.np](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIGwL9Y6cl8ezZh9Cjg6Gx4zUd6cZIeneec3VT0oSQurX7NVVaDRbjPf8MritjNjbY5T7iHapF8n0FcfESEZzcTK6YhGla17H-0tgb81i0Pio2OCu90BZCZifbahYevVoNWjTIFWu3dro2RWfhSY2JflSVa_TZUT4H3sC0HWxSe8gqwr18k8jGlrQ=)


## Annotations
Annotation(end_index=2000, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGl9lpWSJ5koIkw_J6-oFuQIiNaxhS35gzrORxZo2cVTtoYu32IoUl9NPbIvOj0BIcs-nJxNlrNmBmdabq3C7rs2-4_Z_lDqaLQUYn9DsSkeN69jn7egzRJeC6blKk0HrZlbwoszFLHDXk=', start_index=1988)
Annotation(end_index=2000, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTsPtGHLVvY0E44relJYmUEldeZqENQCyb2Np0VIkmcdyu2LWffTKSiSmPTmupIff_Gx7ceHAJmwsj0I5C7OEA5fAYKXqyaBWhfSA-3jwQYkWU9Oiki9JBXl8IdOjnCcw5OwrWdwVTW10utIhKhmk=', start_index=1988)
Annotation(end_index=2186, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcv3a9MTjYN7WzMm2ogR631_xik5Wxna-RuwgkQ-yh4JfRsRXLcGeEbhOFMFfCdsFZZoTyuPPAFwfm7maIyrhVxjbmTU31SMn-P_eR1hwMADgrebvGIRR-_5i4TQ57UbyU5HJvF8gqfvKnxp3FfOMmI9WjJHmZPlW9M_ig8_-w', start_index=2174)
Annotation(end_index=2186, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHERSNJqVltzI-k4ynnyp2WGiYyg1WIi2HQUPd3XJCYWk88gs79UUx4LpbEPmvg2mWlA-v8jTtO2ro6Noi1yuUsnuPn7GQNlgoFOLxcqFJWHg5UG7lmfHSYzhAOKfj684aWkEIqowGT8wNFxANBRON3bz6SlK5oOugFvi0=', start_index=2174)
Annotation(end_index=2519, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGl9lpWSJ5koIkw_J6-oFuQIiNaxhS35gzrORxZo2cVTtoYu32IoUl9NPbIvOj0BIcs-nJxNlrNmBmdabq3C7rs2-4_Z_lDqaLQUYn9DsSkeN69jn7egzRJeC6blKk0HrZlbwoszFLHDXk=', start_index=2507)
Annotation(end_index=2519, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPIfIpK40pgemdqscfWFC1-uRmjHa3t4qwrXJYE3uiM_-sHLplFj50wNexDog4H-_qDAWEq8rvES6fxQK2VM3riwuLcqqWqae7zZRuD3WXjicEmoFP1LLA9wEg-83i05lj8401nqni', start_index=2507)
Annotation(end_index=3817, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOVt5pFaX8z348T_sAktwyOeWN8TdjOsxgNbp_8bDRNPHT0_wJdP9y2j2KR96znwmb6YHSMdhRZDlkjqBGXyvgIG6Fs9BaYowpFC7qxxSi18GO-uxqlhwA2lH186vPKMvA5vf-1uC43IKnxRU7Ej1KINNDM6wvO6ReZyPO5LWjWb4a_C7bEW9RUhCwa_t4HurC3xikMXNNr0vEmzBKwdUQM1OXQ1PMn_K1MUfG', start_index=3805)
Annotation(end_index=3817, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwFKlOGagluWnrlyTNEaCgGwSK1QlJLpVom7oYhXaBx7KgVxTovCTIRkYxBcFZEaMn6EgB2UVINJTOvKqsFlRuVj4JP4f4PvJv0EHPp_u_kt5NS1kjLNPofhJM83fdmoDmIn1IvcIgUtANjIu1ie0jwPwA', start_index=3805)
Annotation(end_index=4083, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhNqSnOXpwdPn3QYBnMc7hSUiv4-2H2kLqt_g1mQwCM3j0dDHzXKS8wQHlEFrrQuo4XlpitCNd0hlcghVHw5SDiJOissZ8N7iYlZoOlhh6b98ymCrHmjQVphsKoKwTnQwfDFOrG6Cx5v5IclPgQ2IY9P-V-IGQwJ7KE-bTvQEQCAF1r5JyNHlFRAivdjVMhVWR7bh-C7FCU9u0lj33sco5qhWPyGcGUw==', start_index=4071)
Annotation(end_index=4083, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwFKlOGagluWnrlyTNEaCgGwSK1QlJLpVom7oYhXaBx7KgVxTovCTIRkYxBcFZEaMn6EgB2UVINJTOvKqsFlRuVj4JP4f4PvJv0EHPp_u_kt5NS1kjLNPofhJM83fdmoDmIn1IvcIgUtANjIu1ie0jwPwA', start_index=4071)
Annotation(end_index=4368, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFE5GZIcGAp3sch6EeuzHyIL9CJYoi2bWVcImZ5TJUBDgVo-X8BduFNO6yZ9k3FQqRQGSNczrxs3WFEvcLjNp3adgXyZzmZJvmmAKDJc5rMqoRBonsk', start_index=4356)
Annotation(end_index=4368, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwFKlOGagluWnrlyTNEaCgGwSK1QlJLpVom7oYhXaBx7KgVxTovCTIRkYxBcFZEaMn6EgB2UVINJTOvKqsFlRuVj4JP4f4PvJv0EHPp_u_kt5NS1kjLNPofhJM83fdmoDmIn1IvcIgUtANjIu1ie0jwPwA', start_index=4356)
Annotation(end_index=4729, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFGPnBh84-B5DYT8PkrAh3XAjTHfvCFewT6lHS8Hh9iLhg8ESIVw4_3-orv_rNe-hnJjccA_gdQgv5Rf6D4kOP-aFhvG_RC5W5S0H696QVP2bK4pjnLp-jup3bPFtEgFTZ_4Ojts0UtsB_KHMGIGgyhA==', start_index=4716)
Annotation(end_index=4729, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPIfIpK40pgemdqscfWFC1-uRmjHa3t4qwrXJYE3uiM_-sHLplFj50wNexDog4H-_qDAWEq8rvES6fxQK2VM3riwuLcqqWqae7zZRuD3WXjicEmoFP1LLA9wEg-83i05lj8401nqni', start_index=4716)
Annotation(end_index=5181, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9QR1w_lE7UATaSri0U7CR9jt-kpaIX6a-HEbJaaWf2FobacXDHzE3Xx7g3e6iR2SL8lss4yiOT0_FoHgBze41SXeIn0Oc_w9MfUC1D7fcLgqlPN7G0Y0eayHu7hiUiK-nQ2dMA9HY94pwaBXmW5ZUmkavDFFxHpSRqkSiGXP4MwnRpmNnbij1jSQyz0OrhbE=', start_index=5168)
Annotation(end_index=5181, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhNqSnOXpwdPn3QYBnMc7hSUiv4-2H2kLqt_g1mQwCM3j0dDHzXKS8wQHlEFrrQuo4XlpitCNd0hlcghVHw5SDiJOissZ8N7iYlZoOlhh6b98ymCrHmjQVphsKoKwTnQwfDFOrG6Cx5v5IclPgQ2IY9P-V-IGQwJ7KE-bTvQEQCAF1r5JyNHlFRAivdjVMhVWR7bh-C7FCU9u0lj33sco5qhWPyGcGUw==', start_index=5168)
Annotation(end_index=5849, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1i2sJsTPT9VEnQW9R0ATXQeX-KleZCldnk-ZPJsODiS-Yf8i0dx2t4ZPnPZQnWeUHuBEr8RcJ5EbRi7Lm2NvmE_3xnoo7n9niO0ktgEMboQGxkZJTsE-EolWn-uJGPAEyFat1BIT-L2Y=', start_index=5835)
Annotation(end_index=5849, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHytjl9BMD-tVmsEOMenjePEHZXD2R2yNe7TEmjAe2pM249DIBqlo7fE18E6eFgK4PTiKfk_ptsfd7al290gj3J3abh8zp4DL5V9iNtLK9A6qLeBkrSv5hD5sJ9M5GOafCLK-oNL92Kp9_OVLm-tKhgbarZRX3MXojIlrQw1iiuS15qk4ydL4KYYbK0e5FZTaiWV-cnRNz6199T9fSpnJo6ucfTubpQkl4=', start_index=5835)
Annotation(end_index=6389, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9j6JTSrpTqHzOkUnt69k0zn8uhO8ZybZGM9zm_1dQ2ersAsV53AQBSY0iuonRNZTSVmW-fduxLjthCOAN03aS2EKC6BrOldz9Q1ZELDUJs_3E69qMhrG4MX0gjbKywGJRNu7_Y8Wj3ary4Bs2fwqNZ46ZxLjr', start_index=6371)
Annotation(end_index=6389, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETkwzDQF5aYxub4WGS3Iuw5rU323Fmnr3O0CifuRfNVuElU_uctuaNYEA4VsIY65nk6kIjnnBfwTETtmnTm30m6SkUjQXF0Z7GbYNiDEFqKaFz2oKMoFri3gmfeRhFtRcSihiKxx_BnTpbimMBRqliQH7XgGdiz9fQ', start_index=6371)
Annotation(end_index=6389, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZdH8LBZGJdUR566vm5QbkRBkKYXdga3DQRVGFyZUjgqdgsQShTAazCRoeJ2mVQmvME76GX9ZV4Y7KiKE9AyMhy1i7P7TlaLdEUkYvKnkVMs4BE0WvtiEzNf9yCRytMcJferTQwBygIlR-Cao=', start_index=6371)
Annotation(end_index=6788, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9j6JTSrpTqHzOkUnt69k0zn8uhO8ZybZGM9zm_1dQ2ersAsV53AQBSY0iuonRNZTSVmW-fduxLjthCOAN03aS2EKC6BrOldz9Q1ZELDUJs_3E69qMhrG4MX0gjbKywGJRNu7_Y8Wj3ary4Bs2fwqNZ46ZxLjr', start_index=6770)
Annotation(end_index=6788, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEj1EfmxLgVp_FimenHW0nuLdo-gkZxKLImXXEIymnEWmmhB3Ua8n2nQlcyf1jECHXT-41sTyN7VeL9Ti9eaB_V9R0iwi7CH_nrJiIXCCKt_9H0pYSGL3EqDWL07kTA71EPdvOYR6b4F_TjNW8k7TthxUMe', start_index=6770)
Annotation(end_index=6788, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL9ZWd01WMB1GJjht5M3OsjIUtSuH3qk5-wiUSfRYZw7h272AvzAazsKz1gmcUfHyObHNEj3XD57ftPc1a6VLWE8D6KC0hCG-rQJwCf-i8al8axV4qxLwGnXqysIl8YtfnylZZ1pRvHGxYKLUhFSL-LOF_E9mcW3an0TvlpG3sqjruUMnOuTqHNt-49cnAFJqGwxtR90J_9ORzuGUApOYMUXhNjIcEdyE8xp44tV2_nyhS6a_w_mMy6pQm6qDB08jchmEaZw==', start_index=6770)
Annotation(end_index=6962, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9j6JTSrpTqHzOkUnt69k0zn8uhO8ZybZGM9zm_1dQ2ersAsV53AQBSY0iuonRNZTSVmW-fduxLjthCOAN03aS2EKC6BrOldz9Q1ZELDUJs_3E69qMhrG4MX0gjbKywGJRNu7_Y8Wj3ary4Bs2fwqNZ46ZxLjr', start_index=6948)
Annotation(end_index=6962, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETkwzDQF5aYxub4WGS3Iuw5rU323Fmnr3O0CifuRfNVuElU_uctuaNYEA4VsIY65nk6kIjnnBfwTETtmnTm30m6SkUjQXF0Z7GbYNiDEFqKaFz2oKMoFri3gmfeRhFtRcSihiKxx_BnTpbimMBRqliQH7XgGdiz9fQ', start_index=6948)
Annotation(end_index=7553, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN5pyjJ6Ucocd7LtyUY3FOcJmm6Uf6dQMyQ7jz8IeaP861bh_ZmG7gajs_cGql2mqtq3pqoIqlKn3RdSQgaO0yPnf2DFsaszbV45UNJIzoZne2Lwjte2bErhCH4v9vNSSXH6HAOJJuMQLC7GbM2AT_frFiLkcvOWPtAnhmyKwsmVRlQWciKRQgjN2NXL2OJE2nki8=', start_index=7543)
Annotation(end_index=7883, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN5pyjJ6Ucocd7LtyUY3FOcJmm6Uf6dQMyQ7jz8IeaP861bh_ZmG7gajs_cGql2mqtq3pqoIqlKn3RdSQgaO0yPnf2DFsaszbV45UNJIzoZne2Lwjte2bErhCH4v9vNSSXH6HAOJJuMQLC7GbM2AT_frFiLkcvOWPtAnhmyKwsmVRlQWciKRQgjN2NXL2OJE2nki8=', start_index=7873)
Annotation(end_index=8316, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-kxyAfTeMZ11geQaDkffWBzG45xBh6I_hck4iK4W2-Duw7Wb70bGD7CZZmQyADF8ly1TE_UhP4bwmtkjiXUEAZAxpsiN1-otZq4ir3KohqwQD0TuxonpphG5ba4LJLYjj7gQyTzyp1fge1Rc2kRPJzudvD1cTqjvhf0KYpTg9yEQqnmIuK6XmOl6YEdHNpuI7KFGw-2loZ7cYOVID7wsSMtgHBLxJM-1cnhrJUfS8o_ScAXo=', start_index=8302)
Annotation(end_index=8316, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFnJzFgu0aSwyUyNod5Hv0SZhBUsQXjLxpQfyf1PuvYbXNirUcFY22J24X1Ux9Rlw64SUB7UCxCVGKaEkI_KKO5T1eZ4SBlmKpjO7flEUiG71h5rd0OQYCu8B2V5UL7Hu22XkRHIE=', start_index=8302)
Annotation(end_index=8551, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFnJzFgu0aSwyUyNod5Hv0SZhBUsQXjLxpQfyf1PuvYbXNirUcFY22J24X1Ux9Rlw64SUB7UCxCVGKaEkI_KKO5T1eZ4SBlmKpjO7flEUiG71h5rd0OQYCu8B2V5UL7Hu22XkRHIE=', start_index=8541)
Annotation(end_index=8871, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN5pyjJ6Ucocd7LtyUY3FOcJmm6Uf6dQMyQ7jz8IeaP861bh_ZmG7gajs_cGql2mqtq3pqoIqlKn3RdSQgaO0yPnf2DFsaszbV45UNJIzoZne2Lwjte2bErhCH4v9vNSSXH6HAOJJuMQLC7GbM2AT_frFiLkcvOWPtAnhmyKwsmVRlQWciKRQgjN2NXL2OJE2nki8=', start_index=8861)
Annotation(end_index=9195, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEj1EfmxLgVp_FimenHW0nuLdo-gkZxKLImXXEIymnEWmmhB3Ua8n2nQlcyf1jECHXT-41sTyN7VeL9Ti9eaB_V9R0iwi7CH_nrJiIXCCKt_9H0pYSGL3EqDWL07kTA71EPdvOYR6b4F_TjNW8k7TthxUMe', start_index=9185)
Annotation(end_index=9765, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2Ke1RfuqET2b-dO0Nznx-nN2awR4yx2-fbCacc2_yWeVSQ8-JbmjiDIiwL5XuXOZRxwnNgs0o-EQUFZfiwHIyt6d25JRz_t4kaWKMbKpvQFP4EcC9ODiT0xahcidUuBRcmkwU3GNJVhzZoT1S4O1corRPkjRs', start_index=9751)
Annotation(end_index=9765, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSrYkG0nfbuyfaTYspXZp0EMj7wtbgla43_TiONMJs3NayyIrwtbOVsNaac58ZYRTlDeJwbifLpdRzJlKCl5L38C6CXL_fq71N8G-ns9wv76XuC0U4oJ_8ZEkI5eBfjELYkAulroUCmDzr27iq8OF1t-e9Fw==', start_index=9751)
Annotation(end_index=10052, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdAcsqrTw2QozsYGRzvDoIJl-GXZQO3FXVFHEic2y_i4zKnsa0D62Um9dzExzpGnAJkqqPjnoSCYpNZb8qo5QNWN2RJVVwnZ9OREeTE-LWcc6Uq7Zceq_BBoVR', start_index=10038)
Annotation(end_index=10052, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhM-YFbobjEVkcbG6kfXqhw8F-HAVNWTsbmPcy1TritpNLWYsuN9mx64HhoHcGSeo4zuILws4cxUrIEJAFe2J5f36sUnInhdBK47JN4EibGKuVj_FrPJoatXGDukl-lxzLdSjRj6430PPTGXZetthEv28KpsHcxidwpxq00KXlnvyHOTc4MqlWtY_IavAr_kk=', start_index=10038)
Annotation(end_index=10675, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXmOb1d_NwWgvulIXAcnwsFbBXj1YFtHC8n3F-P1RX5SQ-zJw2NPEVlvhAnzfjB1cc11zf2ej_Bf3c96vrgfD74r1NbacU9p2vltx_RObi6sxlbtjp0LQ3qsUG5Rir4tF9gCL0ijCfnPyN9dN54bIyKUUZbqHLa706oj1YseWBQyT9oqQZFDf18qmXp6YWGzFJkxOLH1iAiAhOxVVah_k4T7wAUESpk9KFE9vGC1fO4KZB1J_lbV6TH9ZDYYPkT_eCxSTfuLw=', start_index=10665)
Annotation(end_index=10945, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjyzm5YUr7hdQ2GdWlUg3dHCJpIQPAF6JIs5Z7URArH9vPOLPuSIeKS4JVDJMXlorcDO2iUAohfd_lXeCNgBYsqaDOCLQbPVANDum9eYH5QAe7ugcQG0uMda5INRCOT8dXE44J1MRfbaGwAb3XggK6llxYgQnUA0U=', start_index=10935)
Annotation(end_index=11170, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1i2sJsTPT9VEnQW9R0ATXQeX-KleZCldnk-ZPJsODiS-Yf8i0dx2t4ZPnPZQnWeUHuBEr8RcJ5EbRi7Lm2NvmE_3xnoo7n9niO0ktgEMboQGxkZJTsE-EolWn-uJGPAEyFat1BIT-L2Y=', start_index=11160)
Annotation(end_index=11671, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcv3a9MTjYN7WzMm2ogR631_xik5Wxna-RuwgkQ-yh4JfRsRXLcGeEbhOFMFfCdsFZZoTyuPPAFwfm7maIyrhVxjbmTU31SMn-P_eR1hwMADgrebvGIRR-_5i4TQ57UbyU5HJvF8gqfvKnxp3FfOMmI9WjJHmZPlW9M_ig8_-w', start_index=11655)
Annotation(end_index=11671, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs5-zOjnojJXmep_sBExJVY26CFgy-Pt_NI5Qr3TGnHtrbtnjqImf1n0zP_ABkjGE0LOLDYc5uciDvk5pN-hErMv6BUw6N3ZCidXDJRAAKwxND0_0vYFAQt7U_2JwgEJHvHyV5I3AYvgUmeFzwMdHIIojAQOe67Q==', start_index=11655)
Annotation(end_index=11671, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTsPtGHLVvY0E44relJYmUEldeZqENQCyb2Np0VIkmcdyu2LWffTKSiSmPTmupIff_Gx7ceHAJmwsj0I5C7OEA5fAYKXqyaBWhfSA-3jwQYkWU9Oiki9JBXl8IdOjnCcw5OwrWdwVTW10utIhKhmk=', start_index=11655)
Annotation(end_index=11825, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEc-zE359Xp-E5mzKv4TNKJR2M9W7iZOtk6AaTGKQsLFwWz8nGqPCyRag88LLjvP-JyR_ML3iLb3zBWCyssmEl0Za3h7fvhMJzySF7HAmc9ToAM_jTtVhzcZqN2O2ZpFPlWqn9PdLdK85SVN3yzHxl0-7AGeaQc9MY2lj8b07ButCC9PjYDgyiN2XDDJsK49uAhtrWlxr1ZZg==', start_index=11815)
Annotation(end_index=12082, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEc-zE359Xp-E5mzKv4TNKJR2M9W7iZOtk6AaTGKQsLFwWz8nGqPCyRag88LLjvP-JyR_ML3iLb3zBWCyssmEl0Za3h7fvhMJzySF7HAmc9ToAM_jTtVhzcZqN2O2ZpFPlWqn9PdLdK85SVN3yzHxl0-7AGeaQc9MY2lj8b07ButCC9PjYDgyiN2XDDJsK49uAhtrWlxr1ZZg==', start_index=12068)
Annotation(end_index=12082, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGs5-zOjnojJXmep_sBExJVY26CFgy-Pt_NI5Qr3TGnHtrbtnjqImf1n0zP_ABkjGE0LOLDYc5uciDvk5pN-hErMv6BUw6N3ZCidXDJRAAKwxND0_0vYFAQt7U_2JwgEJHvHyV5I3AYvgUmeFzwMdHIIojAQOe67Q==', start_index=12068)
Annotation(end_index=12634, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhNqSnOXpwdPn3QYBnMc7hSUiv4-2H2kLqt_g1mQwCM3j0dDHzXKS8wQHlEFrrQuo4XlpitCNd0hlcghVHw5SDiJOissZ8N7iYlZoOlhh6b98ymCrHmjQVphsKoKwTnQwfDFOrG6Cx5v5IclPgQ2IY9P-V-IGQwJ7KE-bTvQEQCAF1r5JyNHlFRAivdjVMhVWR7bh-C7FCU9u0lj33sco5qhWPyGcGUw==', start_index=12617)
Annotation(end_index=12634, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNckEEN-P1ZLlRpF_DUmZ9YXJ1pUHPhx4akBr7k6pJr9fybYCgghg9j4a1js7RppsABz9FcztCWxoSNhZ9F-Lx73xrSq8Nrv67Yc_X2yKhHnvGcmURP2ao7jbB9bYOytbcTE9o_4hRSeFXB_ODnm-LwcSElrJCvvBMX-5RK7AIAcsQA5s97eMDhxVkynhwQ6IhXA==', start_index=12617)
Annotation(end_index=12634, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-MTNXSwpjMSBIWv8DuVNt2ELS1cOm_B0CogZ9rULHJEbkAcVHkyMrIkWQqhVOhnDIrCp2wB6RqgyDPFfbX5xkv49bjIZ_5S6dHtEakygQ0f1Z2OfnofcAu_sqJUm4sC4mvfsa-dlujqsMcMFTiHcHJfWZmdzvDiLBnWoa-ZKNgA==', start_index=12617)
Annotation(end_index=13582, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFnJzFgu0aSwyUyNod5Hv0SZhBUsQXjLxpQfyf1PuvYbXNirUcFY22J24X1Ux9Rlw64SUB7UCxCVGKaEkI_KKO5T1eZ4SBlmKpjO7flEUiG71h5rd0OQYCu8B2V5UL7Hu22XkRHIE=', start_index=13564)
Annotation(end_index=13582, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdAcsqrTw2QozsYGRzvDoIJl-GXZQO3FXVFHEic2y_i4zKnsa0D62Um9dzExzpGnAJkqqPjnoSCYpNZb8qo5QNWN2RJVVwnZ9OREeTE-LWcc6Uq7Zceq_BBoVR', start_index=13564)
Annotation(end_index=13582, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIGwL9Y6cl8ezZh9Cjg6Gx4zUd6cZIeneec3VT0oSQurX7NVVaDRbjPf8MritjNjbY5T7iHapF8n0FcfESEZzcTK6YhGla17H-0tgb81i0Pio2OCu90BZCZifbahYevVoNWjTIFWu3dro2RWfhSY2JflSVa_TZUT4H3sC0HWxSe8gqwr18k8jGlrQ=', start_index=13564)
Annotation(end_index=14353, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFnJzFgu0aSwyUyNod5Hv0SZhBUsQXjLxpQfyf1PuvYbXNirUcFY22J24X1Ux9Rlw64SUB7UCxCVGKaEkI_KKO5T1eZ4SBlmKpjO7flEUiG71h5rd0OQYCu8B2V5UL7Hu22XkRHIE=', start_index=14340)
Annotation(end_index=14353, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHTsPtGHLVvY0E44relJYmUEldeZqENQCyb2Np0VIkmcdyu2LWffTKSiSmPTmupIff_Gx7ceHAJmwsj0I5C7OEA5fAYKXqyaBWhfSA-3jwQYkWU9Oiki9JBXl8IdOjnCcw5OwrWdwVTW10utIhKhmk=', start_index=14340)

## Sources
