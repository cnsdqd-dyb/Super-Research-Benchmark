# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** e30baa97 | **Time:** 374.89s | **Cost:** $2.44090
--------------------------------------------------------------------------------

# The Economic Impact of Partition Coefficients on Solvent Extraction in Urban Mining Recovery

### Key Points
*   **Direct Economic Correlation:** Partition coefficients ($K_D$ or $D$) and separation factors ($\beta$) are the primary determinants of capital expenditure (CAPEX) and operational expenditure (OPEX) in solvent extraction facilities. A low separation factor necessitates an exponential increase in mixer-settler stages, directly inflating plant footprint and equipment costs.
*   **Urban Mining Specificity:** In the context of urban mining (e.g., e-waste, spent lithium-ion batteries), feedstocks are often dilute and chemically complex. High partition coefficients are critical to minimize solvent-to-feed ratios; otherwise, the cost of handling large volumes of organic solvents renders recovery economically unviable compared to primary mining.
*   **The "Stage Number" Cost Driver:** Research indicates that for difficult separations like Rare Earth Elements (REEs), low separation factors can require hundreds of extraction stages. Specific modeling suggests that separating heavy and medium REEs can account for up to 61% of the total separation stages, representing a disproportionate share of the processing cost.
*   **Reagent Consumption Sensitivity:** Economic feasibility is highly sensitive to reagent consumption (acid/base for stripping and scrubbing). Partition coefficients determine the chemical equilibrium, thereby dictating the volume of reagents required to strip metals from the organic phase. Inefficient stripping due to poor coefficients leads to metal loss and increased chemical costs.

### Executive Summary
The economic feasibility of urban mining—specifically the recovery of critical metals from secondary sources such as electronic waste (e-waste), spent batteries, and permanent magnets—is fundamentally governed by the thermodynamic parameters of the separation process. Among these, the **partition coefficient** (also known as the distribution coefficient or distribution ratio, $D$) and the derived **separation factor** ($\beta$) in solvent extraction are the most critical variables. These coefficients dictate the number of theoretical and actual stages required to achieve market-grade purity, the volume of organic solvent inventory needed, and the consumption rates of chemical reagents.

In urban mining, where metal concentrations can be lower or more complex than in high-grade primary ores, the margin for economic viability is narrow. A favorable partition coefficient ($D > 1$ for extraction, $D < 1$ for stripping) allows for lower solvent-to-feed ratios and smaller equipment sizes. Conversely, low separation factors between chemically similar elements (e.g., adjacent lanthanides in e-waste magnets or Cobalt/Nickel in batteries) force the implementation of extensive mixer-settler cascades, sometimes exceeding hundreds of stages. This report provides an exhaustive analysis of how these physicochemical parameters translate directly into financial metrics, influencing the techno-economic viability of circular economy supply chains.

---

## 1. Theoretical Framework: Partition Coefficients and Separation Factors

To understand the economic implications, one must first establish the physicochemical principles that link partition coefficients to process engineering requirements.

### 1.1 The Partition Coefficient ($D$)
The partition coefficient, often denoted as $K_D$ or $D$, is the equilibrium ratio of the concentration of a solute in the organic phase to its concentration in the aqueous phase [cite: 1, 2].
\[ D = \frac{[C]_{org}}{[C]_{aq}} \]
*   **Economic Implication:** A value of $D$ significantly greater than 1 indicates that the metal prefers the organic phase, allowing for efficient extraction with a smaller volume of solvent. If $D$ is low, large volumes of solvent are required to achieve high recovery, increasing the size of mixer-settlers (CAPEX) and the solvent inventory costs (OPEX) [cite: 1, 3].
*   **Extraction Efficiency ($E$):** The percentage of metal extracted in a single stage is a function of $D$ and the phase volume ratio ($V_{aq}/V_{org}$):
    \[ E\% = \frac{100 \cdot D}{D + \frac{V_{aq}}{V_{org}}} \]
    To achieve quantitative extraction ($>99.9\%$) in a single stage with equal phase volumes, $D$ must be greater than 1000. If $D$ is low (e.g., $<10$), multiple stages are required to reach the same recovery rate, linearly increasing equipment costs [cite: 1, 4].

### 1.2 The Separation Factor ($\beta$)
In urban mining, the goal is rarely just extraction; it is **separation** (e.g., separating Neodymium from Dysprosium in magnet recycling). The separation factor $\beta$ is the ratio of the partition coefficients of two elements, A and B:
\[ \beta_{A/B} = \frac{D_A}{D_B} \]
*   **Economic Implication:** The separation factor determines the difficulty of separating two metals. A high $\beta$ allows for separation in few stages. A low $\beta$ (close to 1) requires many counter-current stages to achieve high purity. For adjacent rare earth elements (REEs), $\beta$ is often very small (e.g., < 2.5), necessitating dozens to hundreds of stages [cite: 5, 6, 7].
*   **Rule of Thumb:** For a simple quantitative separation in one stage, $\beta$ should ideally be $\ge 10^5$. Since this is rarely achievable in hydrometallurgy, multistage systems are mandatory, and the number of stages ($N$) scales inversely with $\log(\beta)$ [cite: 7].

---

## 2. Economic Drivers in Urban Mining Recovery

Urban mining differs from primary mining in feedstock composition, variability, and scale. These factors amplify the economic sensitivity to partition coefficients.

### 2.1 Capital Expenditure (CAPEX)
CAPEX in solvent extraction plants is dominated by the cost of mixer-settlers or extraction columns, solvent inventory, and peripheral infrastructure.
*   **Stage Count Dependency:** The number of stages required is mathematically determined by the separation factor and the desired purity. For REE separation, where separation factors are low, plants often require 200–300 stages [cite: 8]. Each additional stage adds to the capital cost of tanks, mixers, pumps, and piping [cite: 9].
*   **Equipment Sizing:** The physical size of each mixer-settler is determined by the total flow rate. Low partition coefficients require higher organic-to-aqueous (O/A) ratios to achieve extraction, effectively increasing the total volumetric flow and necessitating larger, more expensive vessels [cite: 10, 11].

### 2.2 Operational Expenditure (OPEX)
OPEX is often the deciding factor in the long-term feasibility of urban mining projects.
*   **Reagent Consumption:** This is frequently the largest cost component [cite: 12, 13]. The consumption of acids and bases for pH adjustment (saponification) and stripping is directly linked to the distribution equilibria. Inefficient stripping (high $D$ during the strip phase) requires higher acid concentrations or more strip stages, increasing chemical costs [cite: 6, 14].
*   **Solvent Losses:** Organic solvents are expensive. Losses occur via entrainment (droplets carried away in the aqueous phase) and solubility. Systems with high throughputs (necessitated by low $D$) experience higher absolute solvent losses, a significant recurring cost [cite: 15, 16].
*   **Energy Consumption:** The solvent extraction step can consume more than 50% of the energy required to produce one ton of rare earth metal, primarily for pumping and mixing viscous organic phases [cite: 15].

---

## 3. Case Study: Rare Earth Element (REE) Recovery

The recovery of REEs from e-waste (e.g., NdFeB magnets, phosphors) provides the clearest evidence of how partition coefficients dictate economics.

### 3.1 The "Art versus Science" (AvsS) Economic Model
A pivotal study by Yunus et al. (2018) proposed a quantitative rule-based framework termed "Art versus Science" to assess the economic potential of REE extraction. This model explicitly links separation factors to economic viability [cite: 5, 17].
*   **The "61%" Problem:** The study found that separating Medium REEs (MREE) and Heavy REEs (HREE) is significantly more expensive than Light REEs (LREE). In a modeled separation of a 1-tonne feed using HDEHP extractant, the separation of MREE and HREE accounted for **236 stages**, which was **61% of the total separation stages** (384 total) [cite: 5].
*   **Revenue Index:** Despite the high market value of HREEs, the sheer number of stages required (due to low separation factors) dilutes the profit margin. The study calculated a revenue index of 38 for the full separation route, but noted that separating LREE alone required only 95 stages (25% of total), suggesting that for some feedstocks, full separation might not be economically optimal due to CAPEX/OPEX scaling [cite: 5].

### 3.2 Impact of Extractant Choice on Coefficients and Cost
The choice of extractant fundamentally alters $D$ and $\beta$, thereby changing the economic landscape.
*   **PC88A vs. Cyanex 572:** The industry standard extractant PC88A requires significant acid for stripping. A newer extractant, Cyanex 572, was developed specifically to have lower metal-ligand complex strength (lower $D$ during stripping) while maintaining similar selectivity ($\beta$). This modification allows for stripping at lower acid concentrations, reducing acid consumption by **30%** [cite: 6].
*   **Economic Impact:** Since reagent costs are a major OPEX driver, this shift in partition coefficient behavior (specifically facilitating easier stripping) directly improves the project's Internal Rate of Return (IRR) [cite: 6].

### 3.3 The "Hundreds of Stages" Reality
Conventional solvent extraction for high-purity REEs (e.g., >99.5% for magnet manufacturing) exploits subtle differences in basicity. Because the separation factors between adjacent lanthanides are so low (often < 2.5), plants must operate cascades of **hundreds of mixer-settler stages** [cite: 8, 18].
*   **Urban Mining Consequence:** For a primary mine with a 20-year life, this high CAPEX is amortizable. For an urban miner processing smaller, variable batches of e-waste, the CAPEX of a 300-stage plant is often prohibitive. This forces urban miners to either produce lower-purity mixed oxides (lower revenue) or develop novel technologies with higher $\beta$ [cite: 18].

---

## 4. Case Study: Lithium-Ion Battery (LIB) Recycling

The recycling of LIBs focuses on Cobalt (Co), Nickel (Ni), Manganese (Mn), and Lithium (Li). The economics here are driven by the separation of Co and Ni, which are chemically similar.

### 4.1 Cobalt/Nickel Separation Factors
*   **Extractant Selectivity:** The separation of Co and Ni is a classic hydrometallurgical challenge. The extractant Cyanex 272 is preferred industrially because it offers a Co/Ni separation factor of ~7000, compared to only ~14 for D2EHPA and ~280 for PC88A [cite: 19].
*   **Economic Trade-off:** While D2EHPA is cheaper, its low separation factor (14) would require many more stages to achieve battery-grade purity. Cyanex 272, despite being more expensive per liter, reduces the number of stages and ensures high purity, which commands a premium price in the battery supply chain. The high $\beta$ essentially "saves" the project by reducing CAPEX to manageable levels [cite: 19].

### 4.2 Lithium Recovery Challenges
Lithium is often left in the raffinate (aqueous phase) after other metals are extracted.
*   **Low Partition Coefficients:** Lithium typically has very low partition coefficients in standard acidic extractants compared to transition metals. This makes it difficult to extract lithium into the organic phase without co-extracting impurities [cite: 20, 21].
*   **Cost Sensitivity:** Techno-economic analyses of battery recycling show that lithium recovery is often the marginal revenue stream that determines profitability. If the extraction process for Li requires excessive energy (e.g., evaporation) or expensive reagents due to poor selectivity, it is often left in the slag or wastewater, representing a lost economic opportunity [cite: 20, 22].

---

## 5. Techno-Economic Analysis (TEA) and Sensitivity

Techno-economic models quantify the relationship between partition coefficients and financial viability.

### 5.1 Sensitivity to Separation Efficiency
Sensitivity analyses in TEA studies consistently show that process efficiency (driven by $D$ and $\beta$) is a top-tier variable affecting profitability.
*   **Reagent Cost Dominance:** In bioleaching and solvent extraction TEAs, glucose (for bio-lixiviant) or mineral acids (for SX) can constitute >40% of total costs [cite: 12]. A process with a poor partition coefficient requires more cycles or higher reagent concentrations, directly inflating this cost center.
*   **Yield vs. Purity:** There is often a trade-off. High recovery (high yield) might require aggressive extraction conditions that lower selectivity (lower purity). TEA models show that for high-value products like battery-grade sulfates, purity is non-negotiable. Therefore, the system must operate at conditions that maximize $\beta$, even if it means higher CAPEX [cite: 20, 22].

### 5.2 Impact of Feed Variability
Urban mining feedstocks are inconsistent. A solvent extraction plant designed for a specific feed composition (relying on specific $D$ values) may fail economically if the feed changes.
*   **Impurity Interference:** If the feedstock contains high levels of impurities (e.g., Iron or Aluminum in e-waste), and the partition coefficient for these impurities is non-zero ($D_{imp} > 0$), they will co-extract. Scrubbing these impurities requires additional stages and reagents. If $\beta_{Target/Impurity}$ is not sufficiently high, the cost of scrubbing can outweigh the value of the recovered metal [cite: 19, 23].

---

## 6. Advanced Technologies to Improve Economics

Given the economic constraints imposed by intrinsic partition coefficients, research focuses on engineering solutions to artificially enhance these values or bypass the limitations.

### 6.1 Synergistic Extraction
Mixing two extractants can create a synergistic effect where the combined $D$ or $\beta$ is higher than either alone.
*   **Example:** The use of mixtures like HDEHP + EHEHPA or Aliquat 336 + TBP can enhance separation factors for specific REE pairs [cite: 5, 24].
*   **Economic Benefit:** Higher separation factors reduce the number of required stages. For example, increasing a separation factor from 1.5 to 2.5 can significantly reduce the length of the extraction cascade, lowering CAPEX [cite: 25].

### 6.2 Membrane Solvent Extraction
This technique immobilizes the organic phase in a porous membrane, increasing the interfacial area.
*   **Efficiency:** Studies have shown that membrane solvent extraction can achieve high purity (e.g., 100% Dy) in fewer stages (e.g., 3 stages) compared to conventional mixer-settlers, with cumulative recoveries of ~61% in early stages [cite: 26].
*   **Economic Potential:** By drastically reducing the number of stages and solvent inventory, membrane systems offer a potential pathway to make small-scale urban mining economically feasible [cite: 26].

### 6.3 Alternative Lixiviants (Bio-based)
Using proteins like Lanmodulin or other bio-sorbents can offer separation factors orders of magnitude higher than traditional solvents (e.g., $10^8$ selectivity for REEs over non-REEs) [cite: 14, 27].
*   **Cost Structure:** While the "extractant" (protein) is expensive, the extreme selectivity allows for simple, single-stage separation columns rather than 300-stage cascades. TEA suggests this can be cost-competitive ($24/kg REO) with traditional solvent extraction ($18–97/kg REO) by trading high CAPEX (stages) for high-tech OPEX (proteins) [cite: 14].

---

## 7. Conclusion

The partition coefficient is not merely a thermodynamic constant; it is a fundamental economic lever in the urban mining industry. The evidence confirms that partition coefficients affect economic feasibility through three primary mechanisms:

1.  **CAPEX Scaling:** The separation factor ($\beta$), derived from partition coefficients, dictates the number of mixer-settler stages. In REE recycling, low $\beta$ values necessitate hundreds of stages, creating a high barrier to entry and high capital costs.
2.  **OPEX Intensity:** The magnitude of the partition coefficient ($D$) determines the volume of solvent and the amount of chemical reagents (acid/base) required for scrubbing and stripping. Reagent costs are a dominant operational expense, making the process highly sensitive to these values.
3.  **Purity-Yield Trade-offs:** In the complex, impurity-laden feedstocks typical of urban mining, high partition coefficients for target metals relative to impurities are essential to produce market-grade materials without excessive purification costs.

Therefore, the economic feasibility of recovering metals from urban waste is inextricably linked to the ability to manipulate and optimize partition coefficients. Innovations that enhance these coefficients—such as synergistic solvent systems, novel extractants like Cyanex 572, or alternative separation technologies—are the most direct path to reducing costs and enabling a sustainable circular economy.

### References
[cite: 5, 17] Yunus et al. (2018). Economic potential assessment of rare earth extraction sequence based on rule-based framework.
[cite: 15] Comparison of environmental and economic impacts of solvent extraction.
[cite: 1, 2, 4, 28] Principles of partition coefficients and distribution ratios.
[cite: 12] Techno-economic analysis of bioleaching REEs.
[cite: 9, 11] Mixer-settler design and cost constraints.
[cite: 20, 22] Techno-economic analysis of Lithium-ion battery recycling.
[cite: 6] Comparison of PC88A and Cyanex 572 in REE separation.
[cite: 14] Biobased separation economics vs. solvent extraction.
[cite: 7, 25] Separation factors and stage requirements.
[cite: 8, 18] Challenges of "hundreds of stages" in REE separation.
[cite: 26] Membrane solvent extraction efficiency.
[cite: 16, 19] Cobalt/Nickel separation and reagent costs.
[cite: 13] Economic assessment of recovering REEs from acid mine drainage.

**Sources:**
1. [goalparacollege.ac.in](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBzgQzty_PRQsUs5N0GsyDTUROdnmDP-qrzts6TlPDzWNLgpy_4qy0APA8klX8FapepoIuMhSck5IcJA3CAeyYYfBab-6KmqikY9QtjkPEL0AwgYTcQmAj8yHs7uGCZwAw2YZyrKP3E_EB0vWqcXl9RR973aJPqfgava6u5SPisGSdt6I=)
2. [patsnap.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6NChLJIui82PGVIEhAAd0IDnvi1IF9Df7Y0pfEkpIOcWWTY86V1hiT3AtXhwyib70IRuuQncHyz1vxXSz9B_NJch2YRkfMK7hSQgSWrbBhejdqw87ZMWFsHgZLGTifRWU3NgloMTvUi94L9IorTjfAKMjoknF3VW5z6Gez3awwF9P2UaaYo5ku9fdMfrIC11-ZdtmdVoNwnh6vg==)
3. [libretexts.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLCh291NGf2QZ_y2jar4i5DYEnJkED4l2bV_ySlsoIB6Wep0Vz986rpp0Qfz6tm77SuTl6GhE1UOAcO0hfl84QbCH0PLrsQ_OL0D3p6rl1a0hkALhGrZn8BWczxoEB0lDo65OxtsAHaBomWBl_TCPeAyZKbCTAdDG6CrqFURlNyUdqqodRyP3QrVQYvX2-qYPfG1GVsB8QFD5J9ZLIM49dvaHP6oI33hxJ59Gvu7vQbDo-uDpR4x51eHmBCBT450ckx6_7U9pMv4s_mkCBv5XFSKobp16KWNR7cROuklBULZx_PuK2CyoqGg==)
4. [bhu.ac.in](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtYPVB8QRWUxTIgGGLA2g7-WBeRALPChQL6evkL1ZpLvsYUSjsRDMuK8szMBWrufgbgggOJkcmRk5YASN1eXvP5nlHlIPri4WH8z-ZKwL_YpEpiapDdLpSY3aQ8JBs3eVJO4ymzVhDSK9hN8aoPztWnZxGew5YlsiT73A=)
5. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdD1WLHnQhrGhatcFN6a2uTJJH-usWBvd9wbkhMhDhxNxEZ1d_M-rgYpta9AVfNUvNlfYbhOBGynfMEV-UCZ7wKDU7bx1FnHaSYXpMTicMSc3DdnosvtSxCXBx-1ObIUIWTXv3Ypvy7jULzRPRhREGfS15dhHQ86blYhwAbhu9I4YSZCznNB3SHY-efvj_WguxCfk=)
6. [osti.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWs5gHqRS1SV_WGjJR5aZ5SB6cZ6YJyaSxye4w6oT92Oiq9Ey7ifbz-jYuQFVtMWxVQjU8DfEkmQKLx3zWIr5nMpAuDwXvVMHzqzIo2fEOKlzb82qb_Af-aVBx87BI_Q==)
7. [jsscacs.edu.in](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHrB4qviI6GazOmiuEMlMvleXwFSpj0l15uCP_DKp9SBioOXTJzZN0EQ_ZRBWEhXKkaL3YxqaggeZaf4Bz2PUnYPax0tnIat1cQdJwWAO5rpdnd6gjqUXX-eKaogTnj-Xp4BCI3viH82wfpaNUK-r8nPdDRpWuBmxJ8JtFai4P777nsBs0b9zsi2qNiuDQeRxo9i9d6I4YJ88f0mwAmUFtJo39)
8. [discoveryalert.com.au](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4ypognv7gvgXCiX7_ft9NWHTJDH78wWZG1GdK-xd-C8mFcJBXyu2W-2BqtYvvO0ohs2DaCDmNczM3R_pwjrYlqLzsMUVh1U_1xyAlTfSqTFHA40C-eM1pY3CkWZaLEpSSWrzQyxXlNM4DJLkCbxtVzrYKV0s6Td6KPlS5lWes8qabCojnHO5W3Zw=)
9. [ddpsinc.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEk7RrgwOaMW9kyxtFzWnyqE7q3S3W9w33O6dtMOIWLMiqM4T3Qy-9mFB7EBt31X9mAeCtQdQ0jTawrksxLDmmnb1xGpkGP3GaIH5Jj7mDwh3TFMX1DQUV9s6TIfy6sqh1s69PA2dYgfkF0P0e8X-NarguDHXUm0ZpKZABTiGtX59sNCC2TrzU_70BrLjW5k-m8tJaE)
10. [proseaworld.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFweU0IrNcM5NGBFwR0uL8VSNoAJ5dQDZV_TZ8QieGt2JkeU9td_aeT43HxDdtS9rGaSCgFokutoFNkR89RFQj2A_rkFpwLGPMtUhLNKNrQwvNblHD5uHbe5ofJ2sigB4xDzvfwog==)
11. [pressbooks.pub](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGu2ZPVMmP_XPPeUrI24uMw7cIUXA5VuiSqF_ZOShaGtySdFv76VEjFXOULAX4UDIo7V9_obHN1QDFRMEdUpYE5vHlhZKj02k63ZLT_7ZcP2AgcT4IpcKNDT8D7gMx-q_DYtiLTsf0GP_gugZS8nuzmm6vV8BA2wMzATuARS_W_o8qyUz20n4yK3q1b1Z0BxoNI0R9cuws=)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElflJ6eiWQ9ZEa04Ni7yvoKP-IRRjb2upvMw-jzyWOv0YFw-efR1brG2tFIj0RUlHnEnWF8_MX6g2Hd70W9ComWCUNK4miGuBJjKqVxQ7Rxw8rNOlIPH3x0lpB993d5mLxj3_70vZ01GZNeQbveOu59BnbRc2zVlRScWJxwQSIQNoxNAk5yHsONTYIQp1KXBdGPNYQ0apmiThb9sawnskn64PXrpE6yegJhNq4Bzf98ZYKR0F9VUOE9q7pWagAHK73ZRhDSGXn2uk=)
13. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0rbr78iiIVVEmxpgRQcVmdeCAqPd-UdQvUBt6tU_Wh63EusT7AYkgSftoG4cclreBa-X_hjP9yax6MsCXcPEHbXZ457mva5tdxoTOduluYc4dX3QAqNvZAjNmND1BvBbILZy6kjXCK68dagkizkyMf2eyvxPOlTds6Kz4ckY-MxfvSscDX2LypTaxCFEn9tol-pr3FJoygab5wJsePn5Dr3bcl3hQXsmJ-bgc3Y3D0ajVO3Rgm6K0oOI4q2b9lCy-QhgVXg-ar1-btHBOAhllQCvx-Jppk0xpnTPO9DOUinBAUVvd_Yeh0RyG13Nz-T_PJrdBf-sC6AkKHhw=)
14. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErpdL7OL1_rH_o_Ia7kGTyN25hwr2pc15CZUK9CB9Fnu9Kw5mKecsVCqYfCk9cWz4MoOqSmb5fPspbYXbHyWTHmPd48We3gl0khJ-HOvjY-Ni4TV35gA8GAf60mpzegfrSd0epuA==)
15. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNdwQ32_OSz7cpAEQndQmJDf4NuNorRXByG-btCNNTP6Fw9YVm4VgriwQ2GI_gyt8Uklssm78KePHoFK-tCmqwPHOeFIw0I6MhIVAvc9OwaAnEIln7wJ8jk-rq)
16. [911metallurgist.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBcNw6xYH9HqW6P0X7Ow1vCa6nqWOYIrU4yfa6o3vg0d8I_iwsC8uVx0VWZ9UttGYM7g1MH6WQFa-7VRcyNjtnzh7g-NcAdDICW-m5vZbhl5nc_aRix-GGRp6asj7jJ_NcQEWv6aGz7LNfkyeMB4UDG-Sz9Fyc9xgHguLKncYwePUUgU0ftuBJ4FM1zA==)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxmqnEz4gmwgw727R8ycvHoD1nafzyq1X7gzA4KQiuMizuJ5mSxNBndjqd87oYAw1JA4cD0BUqJ557BuiAAKPz3EeBh-eR-u4Eyx-mwdIdC44H0UON7NzYUw2rHPCsHRHYLG_RsaTryj27VfDFH0_AWEg5HYZtV9SdFhZjLWgkgwubqgzrA6JTiDMBmCPhlg-hgsGEuYVxOH0BqQ3JE6hJXjBpyP4jbHllDZVwatdFtGuGYgq5iDkNf0vYLUa8tfi8xd60QQI=)
18. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENuV6fM-p0HktmjLzwyRpTlZcdOG-S3DeH1Eeo4IpMaNSTixuBSlb3YSvnSgS2s_wTKuldwE69bveV1zUPkOsDIskXpt3rArVXXiA5z9K6zNh1BDvki7BgdelQD3mrqqJx_cvTvuuCbQ==)
19. [uliege.be](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2KAjheZg_TfiomXzWKAJGH8xp7jarOi3PEaaLW_1gdKEvQr0PHBm5_xvZDAwABZ2N6Kx3v2b6-ImVi5cCiC-dmCk8VMMoLTiyww0M8tnWqlLRHTM2MICUBVdT7ywpwYr0TXTkiLy5A6p-dzs0lUV1uB8t0ilOj7_XuBdtRMyr9hwV4WFbh6MR5EIhkveOSxfs3I4eGnVSD10ks7vnxg==)
20. [tennessee.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIIgfct3r1d7ZNAMKJva-9spAV5KMqc57Byt78Md5AsoNgWqrYJVWhbTeu0Z6GugF5Tz4zgXjHLB9v7gau8W_0t1KKLpYXT7Wwrr4YcI0IjXXfJk0QVsjwXsShzuOVNXY9L-hKBawnsJIoRSAtHV1wQETCGwAGEGbJysWd8VZVzGYXaTgu5eeWtOY=)
21. [nrel.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_vWDt08xdPMhHKTbZ3rEP7NYpsupYiH1uXVJMVAywY6FHVeJq2LefRgqATeD8KeTbQ3E1fPqTcaaQ-oH_7Cp2HHArtEfeP7chM_WAKtZu6O-5yl02pBjLqEhOtmKQ_y-Ppw==)
22. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLEB4ThYXHYp_qV1wj6rRVWaUhTkiPzf4QgVwT1ozFwkNxGDKA09ZOnOWPKJ1i1xhxIE7suI-NneDT4CHlGXfJJICyGDkE_LaHAVQZCuXSAnvcRiaZw5woW9YLby4E)
23. [core.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwDsvd1icA8CJtU7R-RiRFJjrQr-FPrqZol49yZ7DIFzGlU448wGNVsyvzYPut2an6dhBFDJ7SXGLS0DzsvIjNRzU4SQNEaVwnqlwCDNsgXJnhb3lUwWpuY05fciNaH7CmQA==)
24. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBMXyv10mvLMLes6rjxwD_xLLD5s-9NfJyPdyvBkB_8kU4ijeU5jvWiZ4e451HQUzC527UZ-uikQfC3CujHsBUdWIFQs14VjkhGMP_MV4whirD-StWQH5-4bToqH7b7HKM7eSnp57e30qI3nFt-JINlXeb_R2Z2JwO3sSqttqvmIm_j0sHXjqez7dzgJ6ysUBk_rIxgC5Ng2d2QKKb9dngdMAcbKmpBPWagXIuNjsSuJI8KP5oP73ZreolFRxkw-TKV6QfwvPxfbXvbXDX55lDXYsPI3Qakf0tA6DqW6dg-F8Rwzi_2ce1da2WJHhjTXVJljl7gH4Yj3b_Lss=)
25. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEOBzGSnh4rIYegPAkOYsjd-OC097s1V-g0PndEhh-B0DUhE7cVZFWld6Ae0kHv2mQr9niVCf_rkoO96yXeHLCRVM3KWkHDCntmHx2F6EPeE7Db608p5TjMPChfLpEg9gEy2GGDKVxRbG6wX1VP6yqCezwOps9mIMWBVeLcmMhvCKMIc8dWSK75thAKvSil7UJtKq9AnfWkDHcBYPnvLwN7MSr4dy_dCXAV3yriUdVbwUrhLwwigYPU0HTuZAUT9vPl)
26. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLDtN8Inwy_PlOTiKMTaOsSWFcmeVo0ppjSSnUSnn-boM7EnOlqfjt5LJeqa1yRwchfLZ81U0QXAdfXTej8RrvbrEB6hPa-80-dAZLMajn0-nyhTvIemTJuHtUouSimpJXgjvPKSI=)
27. [llnl.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6l5s0eeqkg_FsiUe8iXVgCToBBXrE6S8nP1jtAjRDm5AhK_uV-PiugNTHLiHRRzI0SKOoN-b7Wv_AYGWst0nDylSW9G8mkf5-fs9yCnXwvs9jR0HwTICOGViVUHSG5O2324xsM4DfVeJVRNUMb9DVL2jQjqjv4YLkfP9_cHR49HIH4P0HKsxFnJAvEyc5yTXXIBKLGsGBz3WnHiU2wpuxFU9nx1AiOA0=)
28. [ksu.edu.sa](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTrG31jc8rKn1tun-RjuA-B9uXGJyN53Y7S_Bzq_wTpmEzm_XBRZOrL6l4e_fn1gp7oSW7p0q5zUkHTGx37o-tdjVgzRdKZ8nEq7ApiX7ZDFlKtwpfU88rRpwy4BvmQW5uhr9zqDTlTDkBiUY9dxO4E7AGCyYOA0uRt2Cv198=)


## Annotations
Annotation(end_index=3590, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6NChLJIui82PGVIEhAAd0IDnvi1IF9Df7Y0pfEkpIOcWWTY86V1hiT3AtXhwyib70IRuuQncHyz1vxXSz9B_NJch2YRkfMK7hSQgSWrbBhejdqw87ZMWFsHgZLGTifRWU3NgloMTvUi94L9IorTjfAKMjoknF3VW5z6Gez3awwF9P2UaaYo5ku9fdMfrIC11-ZdtmdVoNwnh6vg==', start_index=3578)
Annotation(end_index=3590, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBzgQzty_PRQsUs5N0GsyDTUROdnmDP-qrzts6TlPDzWNLgpy_4qy0APA8klX8FapepoIuMhSck5IcJA3CAeyYYfBab-6KmqikY9QtjkPEL0AwgYTcQmAj8yHs7uGCZwAw2YZyrKP3E_EB0vWqcXl9RR973aJPqfgava6u5SPisGSdt6I=', start_index=3578)
Annotation(end_index=3999, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLCh291NGf2QZ_y2jar4i5DYEnJkED4l2bV_ySlsoIB6Wep0Vz986rpp0Qfz6tm77SuTl6GhE1UOAcO0hfl84QbCH0PLrsQ_OL0D3p6rl1a0hkALhGrZn8BWczxoEB0lDo65OxtsAHaBomWBl_TCPeAyZKbCTAdDG6CrqFURlNyUdqqodRyP3QrVQYvX2-qYPfG1GVsB8QFD5J9ZLIM49dvaHP6oI33hxJ59Gvu7vQbDo-uDpR4x51eHmBCBT450ckx6_7U9pMv4s_mkCBv5XFSKobp16KWNR7cROuklBULZx_PuK2CyoqGg==', start_index=3987)
Annotation(end_index=3999, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBzgQzty_PRQsUs5N0GsyDTUROdnmDP-qrzts6TlPDzWNLgpy_4qy0APA8klX8FapepoIuMhSck5IcJA3CAeyYYfBab-6KmqikY9QtjkPEL0AwgYTcQmAj8yHs7uGCZwAw2YZyrKP3E_EB0vWqcXl9RR973aJPqfgava6u5SPisGSdt6I=', start_index=3987)
Annotation(end_index=4486, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtYPVB8QRWUxTIgGGLA2g7-WBeRALPChQL6evkL1ZpLvsYUSjsRDMuK8szMBWrufgbgggOJkcmRk5YASN1eXvP5nlHlIPri4WH8z-ZKwL_YpEpiapDdLpSY3aQ8JBs3eVJO4ymzVhDSK9hN8aoPztWnZxGew5YlsiT73A=', start_index=4474)
Annotation(end_index=4486, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBzgQzty_PRQsUs5N0GsyDTUROdnmDP-qrzts6TlPDzWNLgpy_4qy0APA8klX8FapepoIuMhSck5IcJA3CAeyYYfBab-6KmqikY9QtjkPEL0AwgYTcQmAj8yHs7uGCZwAw2YZyrKP3E_EB0vWqcXl9RR973aJPqfgava6u5SPisGSdt6I=', start_index=4474)
Annotation(end_index=5190, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWs5gHqRS1SV_WGjJR5aZ5SB6cZ6YJyaSxye4w6oT92Oiq9Ey7ifbz-jYuQFVtMWxVQjU8DfEkmQKLx3zWIr5nMpAuDwXvVMHzqzIo2fEOKlzb82qb_Af-aVBx87BI_Q==', start_index=5175)
Annotation(end_index=5190, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdD1WLHnQhrGhatcFN6a2uTJJH-usWBvd9wbkhMhDhxNxEZ1d_M-rgYpta9AVfNUvNlfYbhOBGynfMEV-UCZ7wKDU7bx1FnHaSYXpMTicMSc3DdnosvtSxCXBx-1ObIUIWTXv3Ypvy7jULzRPRhREGfS15dhHQ86blYhwAbhu9I4YSZCznNB3SHY-efvj_WguxCfk=', start_index=5175)
Annotation(end_index=5190, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHrB4qviI6GazOmiuEMlMvleXwFSpj0l15uCP_DKp9SBioOXTJzZN0EQ_ZRBWEhXKkaL3YxqaggeZaf4Bz2PUnYPax0tnIat1cQdJwWAO5rpdnd6gjqUXX-eKaogTnj-Xp4BCI3viH82wfpaNUK-r8nPdDRpWuBmxJ8JtFai4P777nsBs0b9zsi2qNiuDQeRxo9i9d6I4YJ88f0mwAmUFtJo39', start_index=5175)
Annotation(end_index=5466, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHrB4qviI6GazOmiuEMlMvleXwFSpj0l15uCP_DKp9SBioOXTJzZN0EQ_ZRBWEhXKkaL3YxqaggeZaf4Bz2PUnYPax0tnIat1cQdJwWAO5rpdnd6gjqUXX-eKaogTnj-Xp4BCI3viH82wfpaNUK-r8nPdDRpWuBmxJ8JtFai4P777nsBs0b9zsi2qNiuDQeRxo9i9d6I4YJ88f0mwAmUFtJo39', start_index=5457)
Annotation(end_index=6117, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4ypognv7gvgXCiX7_ft9NWHTJDH78wWZG1GdK-xd-C8mFcJBXyu2W-2BqtYvvO0ohs2DaCDmNczM3R_pwjrYlqLzsMUVh1U_1xyAlTfSqTFHA40C-eM1pY3CkWZaLEpSSWrzQyxXlNM4DJLkCbxtVzrYKV0s6Td6KPlS5lWes8qabCojnHO5W3Zw=', start_index=6108)
Annotation(end_index=6211, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEk7RrgwOaMW9kyxtFzWnyqE7q3S3W9w33O6dtMOIWLMiqM4T3Qy-9mFB7EBt31X9mAeCtQdQ0jTawrksxLDmmnb1xGpkGP3GaIH5Jj7mDwh3TFMX1DQUV9s6TIfy6sqh1s69PA2dYgfkF0P0e8X-NarguDHXUm0ZpKZABTiGtX59sNCC2TrzU_70BrLjW5k-m8tJaE', start_index=6202)
Annotation(end_index=6526, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFweU0IrNcM5NGBFwR0uL8VSNoAJ5dQDZV_TZ8QieGt2JkeU9td_aeT43HxDdtS9rGaSCgFokutoFNkR89RFQj2A_rkFpwLGPMtUhLNKNrQwvNblHD5uHbe5ofJ2sigB4xDzvfwog==', start_index=6512)
Annotation(end_index=6526, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGu2ZPVMmP_XPPeUrI24uMw7cIUXA5VuiSqF_ZOShaGtySdFv76VEjFXOULAX4UDIo7V9_obHN1QDFRMEdUpYE5vHlhZKj02k63ZLT_7ZcP2AgcT4IpcKNDT8D7gMx-q_DYtiLTsf0GP_gugZS8nuzmm6vV8BA2wMzATuARS_W_o8qyUz20n4yK3q1b1Z0BxoNI0R9cuws=', start_index=6512)
Annotation(end_index=6746, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElflJ6eiWQ9ZEa04Ni7yvoKP-IRRjb2upvMw-jzyWOv0YFw-efR1brG2tFIj0RUlHnEnWF8_MX6g2Hd70W9ComWCUNK4miGuBJjKqVxQ7Rxw8rNOlIPH3x0lpB993d5mLxj3_70vZ01GZNeQbveOu59BnbRc2zVlRScWJxwQSIQNoxNAk5yHsONTYIQp1KXBdGPNYQ0apmiThb9sawnskn64PXrpE6yegJhNq4Bzf98ZYKR0F9VUOE9q7pWagAHK73ZRhDSGXn2uk=', start_index=6732)
Annotation(end_index=6746, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0rbr78iiIVVEmxpgRQcVmdeCAqPd-UdQvUBt6tU_Wh63EusT7AYkgSftoG4cclreBa-X_hjP9yax6MsCXcPEHbXZ457mva5tdxoTOduluYc4dX3QAqNvZAjNmND1BvBbILZy6kjXCK68dagkizkyMf2eyvxPOlTds6Kz4ckY-MxfvSscDX2LypTaxCFEn9tol-pr3FJoygab5wJsePn5Dr3bcl3hQXsmJ-bgc3Y3D0ajVO3Rgm6K0oOI4q2b9lCy-QhgVXg-ar1-btHBOAhllQCvx-Jppk0xpnTPO9DOUinBAUVvd_Yeh0RyG13Nz-T_PJrdBf-sC6AkKHhw=', start_index=6732)
Annotation(end_index=7036, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWs5gHqRS1SV_WGjJR5aZ5SB6cZ6YJyaSxye4w6oT92Oiq9Ey7ifbz-jYuQFVtMWxVQjU8DfEkmQKLx3zWIr5nMpAuDwXvVMHzqzIo2fEOKlzb82qb_Af-aVBx87BI_Q==', start_index=7023)
Annotation(end_index=7036, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErpdL7OL1_rH_o_Ia7kGTyN25hwr2pc15CZUK9CB9Fnu9Kw5mKecsVCqYfCk9cWz4MoOqSmb5fPspbYXbHyWTHmPd48We3gl0khJ-HOvjY-Ni4TV35gA8GAf60mpzegfrSd0epuA==', start_index=7023)
Annotation(end_index=7326, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNdwQ32_OSz7cpAEQndQmJDf4NuNorRXByG-btCNNTP6Fw9YVm4VgriwQ2GI_gyt8Uklssm78KePHoFK-tCmqwPHOeFIw0I6MhIVAvc9OwaAnEIln7wJ8jk-rq', start_index=7312)
Annotation(end_index=7326, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBcNw6xYH9HqW6P0X7Ow1vCa6nqWOYIrU4yfa6o3vg0d8I_iwsC8uVx0VWZ9UttGYM7g1MH6WQFa-7VRcyNjtnzh7g-NcAdDICW-m5vZbhl5nc_aRix-GGRp6asj7jJ_NcQEWv6aGz7LNfkyeMB4UDG-Sz9Fyc9xgHguLKncYwePUUgU0ftuBJ4FM1zA==', start_index=7312)
Annotation(end_index=7539, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNdwQ32_OSz7cpAEQndQmJDf4NuNorRXByG-btCNNTP6Fw9YVm4VgriwQ2GI_gyt8Uklssm78KePHoFK-tCmqwPHOeFIw0I6MhIVAvc9OwaAnEIln7wJ8jk-rq', start_index=7529)
Annotation(end_index=8049, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdD1WLHnQhrGhatcFN6a2uTJJH-usWBvd9wbkhMhDhxNxEZ1d_M-rgYpta9AVfNUvNlfYbhOBGynfMEV-UCZ7wKDU7bx1FnHaSYXpMTicMSc3DdnosvtSxCXBx-1ObIUIWTXv3Ypvy7jULzRPRhREGfS15dhHQ86blYhwAbhu9I4YSZCznNB3SHY-efvj_WguxCfk=', start_index=8036)
Annotation(end_index=8049, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxmqnEz4gmwgw727R8ycvHoD1nafzyq1X7gzA4KQiuMizuJ5mSxNBndjqd87oYAw1JA4cD0BUqJ557BuiAAKPz3EeBh-eR-u4Eyx-mwdIdC44H0UON7NzYUw2rHPCsHRHYLG_RsaTryj27VfDFH0_AWEg5HYZtV9SdFhZjLWgkgwubqgzrA6JTiDMBmCPhlg-hgsGEuYVxOH0BqQ3JE6hJXjBpyP4jbHllDZVwatdFtGuGYgq5iDkNf0vYLUa8tfi8xd60QQI=', start_index=8036)
Annotation(end_index=8405, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdD1WLHnQhrGhatcFN6a2uTJJH-usWBvd9wbkhMhDhxNxEZ1d_M-rgYpta9AVfNUvNlfYbhOBGynfMEV-UCZ7wKDU7bx1FnHaSYXpMTicMSc3DdnosvtSxCXBx-1ObIUIWTXv3Ypvy7jULzRPRhREGfS15dhHQ86blYhwAbhu9I4YSZCznNB3SHY-efvj_WguxCfk=', start_index=8396)
Annotation(end_index=8838, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdD1WLHnQhrGhatcFN6a2uTJJH-usWBvd9wbkhMhDhxNxEZ1d_M-rgYpta9AVfNUvNlfYbhOBGynfMEV-UCZ7wKDU7bx1FnHaSYXpMTicMSc3DdnosvtSxCXBx-1ObIUIWTXv3Ypvy7jULzRPRhREGfS15dhHQ86blYhwAbhu9I4YSZCznNB3SHY-efvj_WguxCfk=', start_index=8829)
Annotation(end_index=9412, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWs5gHqRS1SV_WGjJR5aZ5SB6cZ6YJyaSxye4w6oT92Oiq9Ey7ifbz-jYuQFVtMWxVQjU8DfEkmQKLx3zWIr5nMpAuDwXvVMHzqzIo2fEOKlzb82qb_Af-aVBx87BI_Q==', start_index=9403)
Annotation(end_index=9645, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWs5gHqRS1SV_WGjJR5aZ5SB6cZ6YJyaSxye4w6oT92Oiq9Ey7ifbz-jYuQFVtMWxVQjU8DfEkmQKLx3zWIr5nMpAuDwXvVMHzqzIo2fEOKlzb82qb_Af-aVBx87BI_Q==', start_index=9636)
Annotation(end_index=9991, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENuV6fM-p0HktmjLzwyRpTlZcdOG-S3DeH1Eeo4IpMaNSTixuBSlb3YSvnSgS2s_wTKuldwE69bveV1zUPkOsDIskXpt3rArVXXiA5z9K6zNh1BDvki7BgdelQD3mrqqJx_cvTvuuCbQ==', start_index=9978)
Annotation(end_index=9991, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4ypognv7gvgXCiX7_ft9NWHTJDH78wWZG1GdK-xd-C8mFcJBXyu2W-2BqtYvvO0ohs2DaCDmNczM3R_pwjrYlqLzsMUVh1U_1xyAlTfSqTFHA40C-eM1pY3CkWZaLEpSSWrzQyxXlNM4DJLkCbxtVzrYKV0s6Td6KPlS5lWes8qabCojnHO5W3Zw=', start_index=9978)
Annotation(end_index=10365, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENuV6fM-p0HktmjLzwyRpTlZcdOG-S3DeH1Eeo4IpMaNSTixuBSlb3YSvnSgS2s_wTKuldwE69bveV1zUPkOsDIskXpt3rArVXXiA5z9K6zNh1BDvki7BgdelQD3mrqqJx_cvTvuuCbQ==', start_index=10355)
Annotation(end_index=10925, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2KAjheZg_TfiomXzWKAJGH8xp7jarOi3PEaaLW_1gdKEvQr0PHBm5_xvZDAwABZ2N6Kx3v2b6-ImVi5cCiC-dmCk8VMMoLTiyww0M8tnWqlLRHTM2MICUBVdT7ywpwYr0TXTkiLy5A6p-dzs0lUV1uB8t0ilOj7_XuBdtRMyr9hwV4WFbh6MR5EIhkveOSxfs3I4eGnVSD10ks7vnxg==', start_index=10915)
Annotation(end_index=11339, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2KAjheZg_TfiomXzWKAJGH8xp7jarOi3PEaaLW_1gdKEvQr0PHBm5_xvZDAwABZ2N6Kx3v2b6-ImVi5cCiC-dmCk8VMMoLTiyww0M8tnWqlLRHTM2MICUBVdT7ywpwYr0TXTkiLy5A6p-dzs0lUV1uB8t0ilOj7_XuBdtRMyr9hwV4WFbh6MR5EIhkveOSxfs3I4eGnVSD10ks7vnxg==', start_index=11329)
Annotation(end_index=11732, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_vWDt08xdPMhHKTbZ3rEP7NYpsupYiH1uXVJMVAywY6FHVeJq2LefRgqATeD8KeTbQ3E1fPqTcaaQ-oH_7Cp2HHArtEfeP7chM_WAKtZu6O-5yl02pBjLqEhOtmKQ_y-Ppw==', start_index=11718)
Annotation(end_index=11732, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIIgfct3r1d7ZNAMKJva-9spAV5KMqc57Byt78Md5AsoNgWqrYJVWhbTeu0Z6GugF5Tz4zgXjHLB9v7gau8W_0t1KKLpYXT7Wwrr4YcI0IjXXfJk0QVsjwXsShzuOVNXY9L-hKBawnsJIoRSAtHV1wQETCGwAGEGbJysWd8VZVzGYXaTgu5eeWtOY=', start_index=11718)
Annotation(end_index=12126, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIIgfct3r1d7ZNAMKJva-9spAV5KMqc57Byt78Md5AsoNgWqrYJVWhbTeu0Z6GugF5Tz4zgXjHLB9v7gau8W_0t1KKLpYXT7Wwrr4YcI0IjXXfJk0QVsjwXsShzuOVNXY9L-hKBawnsJIoRSAtHV1wQETCGwAGEGbJysWd8VZVzGYXaTgu5eeWtOY=', start_index=12112)
Annotation(end_index=12126, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLEB4ThYXHYp_qV1wj6rRVWaUhTkiPzf4QgVwT1ozFwkNxGDKA09ZOnOWPKJ1i1xhxIE7suI-NneDT4CHlGXfJJICyGDkE_LaHAVQZCuXSAnvcRiaZw5woW9YLby4E', start_index=12112)
Annotation(end_index=12668, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElflJ6eiWQ9ZEa04Ni7yvoKP-IRRjb2upvMw-jzyWOv0YFw-efR1brG2tFIj0RUlHnEnWF8_MX6g2Hd70W9ComWCUNK4miGuBJjKqVxQ7Rxw8rNOlIPH3x0lpB993d5mLxj3_70vZ01GZNeQbveOu59BnbRc2zVlRScWJxwQSIQNoxNAk5yHsONTYIQp1KXBdGPNYQ0apmiThb9sawnskn64PXrpE6yegJhNq4Bzf98ZYKR0F9VUOE9q7pWagAHK73ZRhDSGXn2uk=', start_index=12658)
Annotation(end_index=13189, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIIgfct3r1d7ZNAMKJva-9spAV5KMqc57Byt78Md5AsoNgWqrYJVWhbTeu0Z6GugF5Tz4zgXjHLB9v7gau8W_0t1KKLpYXT7Wwrr4YcI0IjXXfJk0QVsjwXsShzuOVNXY9L-hKBawnsJIoRSAtHV1wQETCGwAGEGbJysWd8VZVzGYXaTgu5eeWtOY=', start_index=13175)
Annotation(end_index=13189, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLEB4ThYXHYp_qV1wj6rRVWaUhTkiPzf4QgVwT1ozFwkNxGDKA09ZOnOWPKJ1i1xhxIE7suI-NneDT4CHlGXfJJICyGDkE_LaHAVQZCuXSAnvcRiaZw5woW9YLby4E', start_index=13175)
Annotation(end_index=13840, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwDsvd1icA8CJtU7R-RiRFJjrQr-FPrqZol49yZ7DIFzGlU448wGNVsyvzYPut2an6dhBFDJ7SXGLS0DzsvIjNRzU4SQNEaVwnqlwCDNsgXJnhb3lUwWpuY05fciNaH7CmQA==', start_index=13826)
Annotation(end_index=13840, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2KAjheZg_TfiomXzWKAJGH8xp7jarOi3PEaaLW_1gdKEvQr0PHBm5_xvZDAwABZ2N6Kx3v2b6-ImVi5cCiC-dmCk8VMMoLTiyww0M8tnWqlLRHTM2MICUBVdT7ywpwYr0TXTkiLy5A6p-dzs0lUV1uB8t0ilOj7_XuBdtRMyr9hwV4WFbh6MR5EIhkveOSxfs3I4eGnVSD10ks7vnxg==', start_index=13826)
Annotation(end_index=14375, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBMXyv10mvLMLes6rjxwD_xLLD5s-9NfJyPdyvBkB_8kU4ijeU5jvWiZ4e451HQUzC527UZ-uikQfC3CujHsBUdWIFQs14VjkhGMP_MV4whirD-StWQH5-4bToqH7b7HKM7eSnp57e30qI3nFt-JINlXeb_R2Z2JwO3sSqttqvmIm_j0sHXjqez7dzgJ6ysUBk_rIxgC5Ng2d2QKKb9dngdMAcbKmpBPWagXIuNjsSuJI8KP5oP73ZreolFRxkw-TKV6QfwvPxfbXvbXDX55lDXYsPI3Qakf0tA6DqW6dg-F8Rwzi_2ce1da2WJHhjTXVJljl7gH4Yj3b_Lss=', start_index=14362)
Annotation(end_index=14375, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdD1WLHnQhrGhatcFN6a2uTJJH-usWBvd9wbkhMhDhxNxEZ1d_M-rgYpta9AVfNUvNlfYbhOBGynfMEV-UCZ7wKDU7bx1FnHaSYXpMTicMSc3DdnosvtSxCXBx-1ObIUIWTXv3Ypvy7jULzRPRhREGfS15dhHQ86blYhwAbhu9I4YSZCznNB3SHY-efvj_WguxCfk=', start_index=14362)
Annotation(end_index=14615, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEOBzGSnh4rIYegPAkOYsjd-OC097s1V-g0PndEhh-B0DUhE7cVZFWld6Ae0kHv2mQr9niVCf_rkoO96yXeHLCRVM3KWkHDCntmHx2F6EPeE7Db608p5TjMPChfLpEg9gEy2GGDKVxRbG6wX1VP6yqCezwOps9mIMWBVeLcmMhvCKMIc8dWSK75thAKvSil7UJtKq9AnfWkDHcBYPnvLwN7MSr4dy_dCXAV3yriUdVbwUrhLwwigYPU0HTuZAUT9vPl', start_index=14605)
Annotation(end_index=15001, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLDtN8Inwy_PlOTiKMTaOsSWFcmeVo0ppjSSnUSnn-boM7EnOlqfjt5LJeqa1yRwchfLZ81U0QXAdfXTej8RrvbrEB6hPa-80-dAZLMajn0-nyhTvIemTJuHtUouSimpJXgjvPKSI=', start_index=14991)
Annotation(end_index=15207, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLDtN8Inwy_PlOTiKMTaOsSWFcmeVo0ppjSSnUSnn-boM7EnOlqfjt5LJeqa1yRwchfLZ81U0QXAdfXTej8RrvbrEB6hPa-80-dAZLMajn0-nyhTvIemTJuHtUouSimpJXgjvPKSI=', start_index=15197)
Annotation(end_index=15452, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErpdL7OL1_rH_o_Ia7kGTyN25hwr2pc15CZUK9CB9Fnu9Kw5mKecsVCqYfCk9cWz4MoOqSmb5fPspbYXbHyWTHmPd48We3gl0khJ-HOvjY-Ni4TV35gA8GAf60mpzegfrSd0epuA==', start_index=15438)
Annotation(end_index=15452, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6l5s0eeqkg_FsiUe8iXVgCToBBXrE6S8nP1jtAjRDm5AhK_uV-PiugNTHLiHRRzI0SKOoN-b7Wv_AYGWst0nDylSW9G8mkf5-fs9yCnXwvs9jR0HwTICOGViVUHSG5O2324xsM4DfVeJVRNUMb9DVL2jQjqjv4YLkfP9_cHR49HIH4P0HKsxFnJAvEyc5yTXXIBKLGsGBz3WnHiU2wpuxFU9nx1AiOA0=', start_index=15438)
Annotation(end_index=15812, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErpdL7OL1_rH_o_Ia7kGTyN25hwr2pc15CZUK9CB9Fnu9Kw5mKecsVCqYfCk9cWz4MoOqSmb5fPspbYXbHyWTHmPd48We3gl0khJ-HOvjY-Ni4TV35gA8GAf60mpzegfrSd0epuA==', start_index=15802)
Annotation(end_index=17336, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdD1WLHnQhrGhatcFN6a2uTJJH-usWBvd9wbkhMhDhxNxEZ1d_M-rgYpta9AVfNUvNlfYbhOBGynfMEV-UCZ7wKDU7bx1FnHaSYXpMTicMSc3DdnosvtSxCXBx-1ObIUIWTXv3Ypvy7jULzRPRhREGfS15dhHQ86blYhwAbhu9I4YSZCznNB3SHY-efvj_WguxCfk=', start_index=17323)
Annotation(end_index=17336, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxmqnEz4gmwgw727R8ycvHoD1nafzyq1X7gzA4KQiuMizuJ5mSxNBndjqd87oYAw1JA4cD0BUqJ557BuiAAKPz3EeBh-eR-u4Eyx-mwdIdC44H0UON7NzYUw2rHPCsHRHYLG_RsaTryj27VfDFH0_AWEg5HYZtV9SdFhZjLWgkgwubqgzrA6JTiDMBmCPhlg-hgsGEuYVxOH0BqQ3JE6hJXjBpyP4jbHllDZVwatdFtGuGYgq5iDkNf0vYLUa8tfi8xd60QQI=', start_index=17323)
Annotation(end_index=17463, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFNdwQ32_OSz7cpAEQndQmJDf4NuNorRXByG-btCNNTP6Fw9YVm4VgriwQ2GI_gyt8Uklssm78KePHoFK-tCmqwPHOeFIw0I6MhIVAvc9OwaAnEIln7wJ8jk-rq', start_index=17453)
Annotation(end_index=17555, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtYPVB8QRWUxTIgGGLA2g7-WBeRALPChQL6evkL1ZpLvsYUSjsRDMuK8szMBWrufgbgggOJkcmRk5YASN1eXvP5nlHlIPri4WH8z-ZKwL_YpEpiapDdLpSY3aQ8JBs3eVJO4ymzVhDSK9hN8aoPztWnZxGew5YlsiT73A=', start_index=17536)
Annotation(end_index=17555, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6NChLJIui82PGVIEhAAd0IDnvi1IF9Df7Y0pfEkpIOcWWTY86V1hiT3AtXhwyib70IRuuQncHyz1vxXSz9B_NJch2YRkfMK7hSQgSWrbBhejdqw87ZMWFsHgZLGTifRWU3NgloMTvUi94L9IorTjfAKMjoknF3VW5z6Gez3awwF9P2UaaYo5ku9fdMfrIC11-ZdtmdVoNwnh6vg==', start_index=17536)
Annotation(end_index=17555, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTrG31jc8rKn1tun-RjuA-B9uXGJyN53Y7S_Bzq_wTpmEzm_XBRZOrL6l4e_fn1gp7oSW7p0q5zUkHTGx37o-tdjVgzRdKZ8nEq7ApiX7ZDFlKtwpfU88rRpwy4BvmQW5uhr9zqDTlTDkBiUY9dxO4E7AGCyYOA0uRt2Cv198=', start_index=17536)
Annotation(end_index=17555, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBzgQzty_PRQsUs5N0GsyDTUROdnmDP-qrzts6TlPDzWNLgpy_4qy0APA8klX8FapepoIuMhSck5IcJA3CAeyYYfBab-6KmqikY9QtjkPEL0AwgYTcQmAj8yHs7uGCZwAw2YZyrKP3E_EB0vWqcXl9RR973aJPqfgava6u5SPisGSdt6I=', start_index=17536)
Annotation(end_index=17628, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElflJ6eiWQ9ZEa04Ni7yvoKP-IRRjb2upvMw-jzyWOv0YFw-efR1brG2tFIj0RUlHnEnWF8_MX6g2Hd70W9ComWCUNK4miGuBJjKqVxQ7Rxw8rNOlIPH3x0lpB993d5mLxj3_70vZ01GZNeQbveOu59BnbRc2zVlRScWJxwQSIQNoxNAk5yHsONTYIQp1KXBdGPNYQ0apmiThb9sawnskn64PXrpE6yegJhNq4Bzf98ZYKR0F9VUOE9q7pWagAHK73ZRhDSGXn2uk=', start_index=17618)
Annotation(end_index=17688, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEk7RrgwOaMW9kyxtFzWnyqE7q3S3W9w33O6dtMOIWLMiqM4T3Qy-9mFB7EBt31X9mAeCtQdQ0jTawrksxLDmmnb1xGpkGP3GaIH5Jj7mDwh3TFMX1DQUV9s6TIfy6sqh1s69PA2dYgfkF0P0e8X-NarguDHXUm0ZpKZABTiGtX59sNCC2TrzU_70BrLjW5k-m8tJaE', start_index=17675)
Annotation(end_index=17688, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGu2ZPVMmP_XPPeUrI24uMw7cIUXA5VuiSqF_ZOShaGtySdFv76VEjFXOULAX4UDIo7V9_obHN1QDFRMEdUpYE5vHlhZKj02k63ZLT_7ZcP2AgcT4IpcKNDT8D7gMx-q_DYtiLTsf0GP_gugZS8nuzmm6vV8BA2wMzATuARS_W_o8qyUz20n4yK3q1b1Z0BxoNI0R9cuws=', start_index=17675)
Annotation(end_index=17746, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIIgfct3r1d7ZNAMKJva-9spAV5KMqc57Byt78Md5AsoNgWqrYJVWhbTeu0Z6GugF5Tz4zgXjHLB9v7gau8W_0t1KKLpYXT7Wwrr4YcI0IjXXfJk0QVsjwXsShzuOVNXY9L-hKBawnsJIoRSAtHV1wQETCGwAGEGbJysWd8VZVzGYXaTgu5eeWtOY=', start_index=17732)
Annotation(end_index=17746, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLEB4ThYXHYp_qV1wj6rRVWaUhTkiPzf4QgVwT1ozFwkNxGDKA09ZOnOWPKJ1i1xhxIE7suI-NneDT4CHlGXfJJICyGDkE_LaHAVQZCuXSAnvcRiaZw5woW9YLby4E', start_index=17732)
Annotation(end_index=17815, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWs5gHqRS1SV_WGjJR5aZ5SB6cZ6YJyaSxye4w6oT92Oiq9Ey7ifbz-jYuQFVtMWxVQjU8DfEkmQKLx3zWIr5nMpAuDwXvVMHzqzIo2fEOKlzb82qb_Af-aVBx87BI_Q==', start_index=17806)
Annotation(end_index=17880, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErpdL7OL1_rH_o_Ia7kGTyN25hwr2pc15CZUK9CB9Fnu9Kw5mKecsVCqYfCk9cWz4MoOqSmb5fPspbYXbHyWTHmPd48We3gl0khJ-HOvjY-Ni4TV35gA8GAf60mpzegfrSd0epuA==', start_index=17870)
Annotation(end_index=17948, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEOBzGSnh4rIYegPAkOYsjd-OC097s1V-g0PndEhh-B0DUhE7cVZFWld6Ae0kHv2mQr9niVCf_rkoO96yXeHLCRVM3KWkHDCntmHx2F6EPeE7Db608p5TjMPChfLpEg9gEy2GGDKVxRbG6wX1VP6yqCezwOps9mIMWBVeLcmMhvCKMIc8dWSK75thAKvSil7UJtKq9AnfWkDHcBYPnvLwN7MSr4dy_dCXAV3yriUdVbwUrhLwwigYPU0HTuZAUT9vPl', start_index=17935)
Annotation(end_index=17948, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHrB4qviI6GazOmiuEMlMvleXwFSpj0l15uCP_DKp9SBioOXTJzZN0EQ_ZRBWEhXKkaL3YxqaggeZaf4Bz2PUnYPax0tnIat1cQdJwWAO5rpdnd6gjqUXX-eKaogTnj-Xp4BCI3viH82wfpaNUK-r8nPdDRpWuBmxJ8JtFai4P777nsBs0b9zsi2qNiuDQeRxo9i9d6I4YJ88f0mwAmUFtJo39', start_index=17935)
Annotation(end_index=18005, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENuV6fM-p0HktmjLzwyRpTlZcdOG-S3DeH1Eeo4IpMaNSTixuBSlb3YSvnSgS2s_wTKuldwE69bveV1zUPkOsDIskXpt3rArVXXiA5z9K6zNh1BDvki7BgdelQD3mrqqJx_cvTvuuCbQ==', start_index=17992)
Annotation(end_index=18005, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4ypognv7gvgXCiX7_ft9NWHTJDH78wWZG1GdK-xd-C8mFcJBXyu2W-2BqtYvvO0ohs2DaCDmNczM3R_pwjrYlqLzsMUVh1U_1xyAlTfSqTFHA40C-eM1pY3CkWZaLEpSSWrzQyxXlNM4DJLkCbxtVzrYKV0s6Td6KPlS5lWes8qabCojnHO5W3Zw=', start_index=17992)
Annotation(end_index=18070, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLDtN8Inwy_PlOTiKMTaOsSWFcmeVo0ppjSSnUSnn-boM7EnOlqfjt5LJeqa1yRwchfLZ81U0QXAdfXTej8RrvbrEB6hPa-80-dAZLMajn0-nyhTvIemTJuHtUouSimpJXgjvPKSI=', start_index=18060)
Annotation(end_index=18125, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2KAjheZg_TfiomXzWKAJGH8xp7jarOi3PEaaLW_1gdKEvQr0PHBm5_xvZDAwABZ2N6Kx3v2b6-ImVi5cCiC-dmCk8VMMoLTiyww0M8tnWqlLRHTM2MICUBVdT7ywpwYr0TXTkiLy5A6p-dzs0lUV1uB8t0ilOj7_XuBdtRMyr9hwV4WFbh6MR5EIhkveOSxfs3I4eGnVSD10ks7vnxg==', start_index=18111)
Annotation(end_index=18125, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBcNw6xYH9HqW6P0X7Ow1vCa6nqWOYIrU4yfa6o3vg0d8I_iwsC8uVx0VWZ9UttGYM7g1MH6WQFa-7VRcyNjtnzh7g-NcAdDICW-m5vZbhl5nc_aRix-GGRp6asj7jJ_NcQEWv6aGz7LNfkyeMB4UDG-Sz9Fyc9xgHguLKncYwePUUgU0ftuBJ4FM1zA==', start_index=18111)
Annotation(end_index=18180, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0rbr78iiIVVEmxpgRQcVmdeCAqPd-UdQvUBt6tU_Wh63EusT7AYkgSftoG4cclreBa-X_hjP9yax6MsCXcPEHbXZ457mva5tdxoTOduluYc4dX3QAqNvZAjNmND1BvBbILZy6kjXCK68dagkizkyMf2eyvxPOlTds6Kz4ckY-MxfvSscDX2LypTaxCFEn9tol-pr3FJoygab5wJsePn5Dr3bcl3hQXsmJ-bgc3Y3D0ajVO3Rgm6K0oOI4q2b9lCy-QhgVXg-ar1-btHBOAhllQCvx-Jppk0xpnTPO9DOUinBAUVvd_Yeh0RyG13Nz-T_PJrdBf-sC6AkKHhw=', start_index=18170)

## Sources
