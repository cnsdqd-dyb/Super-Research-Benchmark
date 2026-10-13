# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 6d1bd1c1 | **Time:** 184.46s | **Cost:** $0.54350
--------------------------------------------------------------------------------

# The Interplay of Effective Population Size, Genetic Load, and Range Contraction Under Climate Change

### Key Points
*   **Inverse Relationship:** There is a fundamental inverse relationship between effective population size ($N_e$) and the accumulation of genetic load; as $N_e$ declines due to range contraction, the efficacy of natural selection decreases, allowing deleterious mutations to drift to higher frequencies.
*   **Type of Load Matters:** Small, contracting populations often purge highly deleterious recessive alleles (reducing inbreeding load) but accumulate slightly deleterious mutations (increasing drift load) that become fixed, potentially leading to a gradual decline in fitness.
*   **Spatial Dynamics:** Range contraction is not uniform. "Trailing edge" populations often suffer from genetic erosion and isolation, while "leading edge" populations may experience "expansion load" (mutation surfing), where deleterious alleles ride the wave of expansion into new territories.
*   **Contraction Patterns:** The geometric pattern of range loss—fragmentation, shrinkage, or amputation—significantly alters genetic outcomes. Fragmentation typically results in the most severe reduction in $N_e$ and the highest accumulation of realized genetic load compared to contiguous shrinkage.
*   **Genomic Vulnerability:** Climate change creates a "genomic offset," a mismatch between current genetic variation and future environmental optima. Populations with low $N_e$ lack the standing genetic variation required to bridge this gap, increasing the risk of mutational meltdown and extinction.

---

### Introduction

The rapid alteration of global climate systems is forcing species to shift, contract, or fragment their geographic ranges. These demographic changes have profound consequences for the genetic health of populations, specifically regarding **effective population size ($N_e$)** and **genetic load**. Genetic load refers to the burden of deleterious mutations carried by a population that reduces its mean fitness relative to a theoretical optimum. The interaction between $N_e$ and genetic load is a central determinant of whether a species will adapt to new climatic conditions or spiral toward extinction.

Research indicates that as range contraction reduces $N_e$, the balance of evolutionary forces shifts from natural selection toward genetic drift. This shift compromises the population's ability to remove harmful mutations and retain adaptive variation. However, the dynamic is complex: while small populations may accumulate mildly deleterious mutations (drift load), they may simultaneously purge lethal recessive alleles through inbreeding. This report synthesizes current genomic research to explain how $N_e$ influences genetic load during climate-induced range contraction, examining the mechanisms of mutation accumulation, the spatial nuances of range shifts, and the ultimate consequences for species persistence.

---

## 1. Theoretical Foundations: $N_e$ and Selection Efficacy

To understand the impact of range contraction, one must first establish the theoretical relationship between population size and the efficiency of natural selection.

### 1.1 The Drift Barrier and Selection Efficiency
The effective population size ($N_e$) is the size of an idealized population that would experience the same rate of genetic drift as the observed population [cite: 1]. It is almost always smaller than the census size ($N$) due to factors such as unequal sex ratios, variance in reproductive success, and population fluctuations [cite: 1, 2].

The efficacy of natural selection in removing deleterious mutations or fixing beneficial ones is governed by the relationship between the selection coefficient ($s$) and $N_e$. According to population genetic theory, selection is effective only when:
\[ N_e s > 1 \]
When $N_e$ is large, selection can "see" and act upon mutations with very small effects on fitness. However, as $N_e$ declines during range contraction, the threshold for selection rises. Mutations that are slightly deleterious (weakly selected) behave as if they are neutral [cite: 3, 4]. Consequently, natural selection fails to purge these variants, and they are subject to stochastic changes in frequency driven by genetic drift [cite: 3, 5].

### 1.2 Components of Genetic Load
Genetic load is not a monolithic entity; it manifests in different forms that respond differently to population contraction:

1.  **Drift Load (Fixed Load):** This consists of slightly deleterious mutations that rise to high frequency or fixation purely by chance due to strong genetic drift in small populations [cite: 4]. This is the primary threat to populations undergoing long-term contraction, as the accumulation of many mild defects can permanently lower population fitness [cite: 6].
2.  **Inbreeding Load (Segregating Load):** This refers to recessive deleterious alleles that segregate in a population. In large, panmictic populations, these are typically masked in the heterozygous state. During range contraction, increased inbreeding converts these heterozygotes to homozygotes, exposing the deleterious alleles and causing inbreeding depression [cite: 6, 7].
3.  **Expansion Load:** Occurs at the leading edge of a range shift, where repeated founder effects allow deleterious mutations to "surf" to high frequencies, accumulating at the expansion front [cite: 5].

---

## 2. Mechanisms of Load Accumulation During Range Contraction

Climate change-induced range contraction triggers specific genomic mechanisms that alter the composition of genetic load.

### 2.1 The Purging vs. Accumulation Trade-off
A critical finding in recent genomic studies is the trade-off between purging and accumulation. In large populations, highly deleterious recessive mutations are maintained at low frequencies (mutation-selection balance). When range contraction forces a population bottleneck, inbreeding increases.

*   **Purging of Lethals:** The increased homozygosity exposes highly deleterious recessive alleles to selection. If the population does not go extinct immediately, these lethal alleles are often purged from the gene pool. Consequently, small, isolated populations often carry *fewer* strongly deleterious segregating variants than large populations [cite: 3, 6]. For example, genomic analysis of the Montezuma Quail (*Cyrtonyx montezumae*) revealed that the smaller, isolated Texas population had purged strongly deleterious variants compared to the larger Arizona population [cite: 3, 6].
*   **Accumulation of Mild Defects:** Conversely, while lethals are purged, slightly deleterious mutations (which are essentially invisible to selection in low $N_e$ conditions) accumulate due to drift. The same Montezuma Quail study found that the small population had a higher frequency of fixed, slightly deleterious mutations [cite: 6].

### 2.2 Realized vs. Masked Load
The distinction between "masked" and "realized" load is vital for understanding extinction risk.
*   **Masked Load:** Potential genetic load hidden in heterozygotes. Large populations typically have high masked load [cite: 7].
*   **Realized Load:** The expressed reduction in fitness due to homozygous deleterious alleles.
Range contraction converts masked load into realized load. Even if the absolute number of deleterious alleles decreases (due to purging), the *realized* load may increase because the remaining deleterious alleles are far more likely to be homozygous [cite: 6, 7]. This transition is a primary driver of fitness decline in contracting populations.

### 2.3 Mutational Meltdown
If $N_e$ remains low for an extended period, the population may enter a feedback loop known as mutational meltdown [cite: 8, 9].
1.  Small $N_e$ leads to the accumulation of deleterious mutations (drift load).
2.  These mutations reduce the mean fitness of the population (e.g., lower fertility, survival).
3.  Reduced fitness leads to a further decrease in population size ($N$).
4.  Lower $N$ further reduces $N_e$, accelerating the accumulation of mutations.
This cycle continues until the population becomes extinct. Models suggest that the deleterious mutation rate and the efficacy of selection are the strongest predictors of the time to meltdown [cite: 9].

---

## 3. Spatial Dynamics: Leading vs. Trailing Edges

Climate change does not shrink ranges symmetrically; it typically causes contraction at the "trailing edge" (usually the equator-ward or lower-elevation limit) and potential expansion at the "leading edge" (poleward or higher elevation). $N_e$ and genetic load behave differently in these zones.

### 3.1 Trailing Edge: Genetic Erosion
Populations at the trailing edge often represent the historical core of the species' range and may harbor high levels of unique genetic diversity [cite: 10]. However, as the climate becomes unsuitable, these populations experience:
*   **Demographic Decline:** Census size drops, reducing $N_e$.
*   **Isolation:** Connectivity to the core range is severed, preventing gene flow that could otherwise buffer against drift (genetic rescue) [cite: 11].
*   **Erosion:** High historical diversity is lost through drift. Studies on bats (*Plecotus austriacus*) show that trailing edge populations can suffer severe declines in $N_e$ (up to 30-fold), leading to a loss of unique haplotypes and adaptive potential [cite: 10, 12].

### 3.2 Leading Edge: Expansion Load and Mutation Surfing
At the leading edge, where species track shifting isotherms, $N_e$ is often reduced due to the "founder effect." Only a small subset of individuals colonize the new territory.
*   **Mutation Surfing:** Deleterious mutations present in the founders can rise to high frequency simply because they are at the wave front of expansion. This phenomenon, known as "mutation surfing," creates a gradient where genetic load is higher at the range edge than in the core [cite: 5].
*   **Case Study (Vitis arizonica):** Research on the wild grape *Vitis arizonica* demonstrated that populations at the leading edge of range expansion harbored higher mutational load and fewer putatively adaptive alleles compared to core populations [cite: 5]. This "expansion load" can hinder the species' ability to continue tracking climate change.

### 3.3 Asymmetric Persistence
Theoretical models suggest that $N_e$ declines toward both range limits, but the persistence of mutations differs. At the leading edge, reduced gene flow and strong drift allow mutations to persist longer than expected, while at the trailing edge, habitat degradation accelerates the loss of lineages [cite: 11].

---

## 4. Patterns of Range Contraction: Fragmentation vs. Shrinkage

The geometric manner in which a range contracts significantly influences $N_e$ and genetic load. Recent simulations define three distinct patterns: **Shrinkage**, **Amputation**, and **Fragmentation** [cite: 13, 14].

### 4.1 Fragmentation
Fragmentation occurs when a continuous range is broken into disjunct, isolated patches.
*   **Impact on $N_e$:** Fragmentation causes the most severe reduction in global $N_e$ because it subdivides the population into non-communicating demes, each subject to intense drift [cite: 13].
*   **Genetic Consequences:** Simulations show that fragmentation results in the strongest decline in nucleotide diversity and the highest increase in relatedness (inbreeding) [cite: 13, 14]. This structure prevents the flow of beneficial alleles and fixes deleterious ones within patches, maximizing the drift load.

### 4.2 Shrinkage and Amputation
*   **Shrinkage:** The range contracts from the periphery toward the core (melting range). This preserves the core population's $N_e$ for longer, maintaining higher genetic diversity than fragmentation [cite: 13].
*   **Amputation:** A large section of the range is lost (e.g., due to a catastrophic event or rapid climate shift). While $N$ drops, the remaining population may remain contiguous, preserving a larger effective size than if it were fragmented [cite: 14].

### 4.3 Speed of Contraction
Counter-intuitively, some models suggest that **fast** range contractions might preserve higher levels of genetic diversity in refugia than slow contractions [cite: 15, 16].
*   **Mechanism:** In a slow contraction, populations at the margins dwindle slowly, losing diversity via drift before they go extinct or migrate. In a fast contraction, individuals may be forced to migrate rapidly to refugia, bringing their genetic variation with them before it is eroded by drift in the marginal habitat [cite: 15].

---

## 5. Genomic Vulnerability and Climate Mismatch

The concept of **Genomic Offset** (or Genomic Vulnerability) quantifies the disruption caused by the interaction of climate change and genetic load.

### 5.1 Defining Genomic Offset
Genomic offset measures the mismatch between the current genetic composition of a population and the genetic composition required to be adapted to future climatic conditions [cite: 17, 18].
*   **High Offset:** Indicates that the population requires a significant evolutionary change to adapt to the new environment.
*   **Role of $N_e$:** Populations with low $N_e$ have low standing genetic variation. Therefore, they are less likely to possess the specific alleles required to adapt to the future climate. A high genomic offset combined with low $N_e$ is a predictor of high extinction risk [cite: 18].

### 5.2 Case Study: Ptarmigan (*Lagopus* spp.)
Studies on Rock Ptarmigan (*Lagopus muta*) and Willow Ptarmigan (*Lagopus lagopus*) illustrate this dynamic.
*   **Observation:** Populations in isolated regions (e.g., East Greenland, Svalbard) showed reduced nucleotide diversity, high inbreeding, and high mutation load due to historical $N_e$ declines [cite: 18].
*   **Prediction:** These small, loaded populations showed the highest genomic vulnerability. They lack the adaptive variation to respond to the predicted mismatch between their current adaptations and future climate scenarios [cite: 18].

### 5.3 Adaptive Capacity vs. Load
The ability of a population to undergo **Evolutionary Rescue**—adapting fast enough to avoid extinction—depends on the balance between standing variation and genetic load.
*   **Standing Variation:** Adaptation from existing variation is faster than waiting for new mutations. Small $N_e$ depletes this variation [cite: 19].
*   **Load as a Brake:** High genetic load can depress the population growth rate, making the population more vulnerable to stochastic extinction before adaptation can occur [cite: 20]. Experimental evolution studies in *Tribolium* beetles show that while adaptation can rescue populations, the accumulation of drift load in small populations can overwhelm the benefits of adaptation, leading to eventual decline [cite: 20].

---

## 6. Conservation Implications: Managing $N_e$ and Load

Understanding the mechanics of $N_e$ and load offers specific strategies for conservation in the face of climate change.

### 6.1 Genetic Rescue
Genetic rescue involves introducing individuals from a different population to increase $N_e$ and reduce genetic load.
*   **Mechanism:** Immigrants introduce new alleles, masking deleterious recessives (heterosis) and increasing the efficacy of selection [cite: 21].
*   **Application:** For populations suffering from inbreeding depression (realized load), genetic rescue is highly effective. However, if the donor population is adapted to a different climate, there is a risk of outbreeding depression or swamping local adaptations [cite: 21, 22].

### 6.2 Assisted Migration and Predictive Provenancing
Given that trailing edge populations are eroding and leading edge populations are accumulating expansion load:
*   **Strategy:** Conservationists can facilitate gene flow by moving individuals from the core or trailing edge (high diversity) to the leading edge. This "pushes" diversity forward, counteracting the founder effects and mutation surfing that characterize range expansions [cite: 23].
*   **Targeting:** Genomic offset analysis can identify which populations are most vulnerable and which source populations have the pre-adapted alleles necessary for the future climate [cite: 19, 23].

### 6.3 Maintaining Connectivity
Since fragmentation is the most damaging pattern of contraction for $N_e$ [cite: 13], maintaining corridors is critical. Connectivity increases the effective size of the metapopulation, allowing selection to operate more efficiently and preventing the fixation of drift load [cite: 22].

---

## Conclusion

Effective population size is the master variable governing the genetic health of species facing climate change. As ranges contract, the reduction in $N_e$ fundamentally alters the evolutionary landscape: natural selection loses its precision, allowing slightly deleterious mutations to accumulate (drift load) while inbreeding exposes recessive lethals (realized load).

The interaction is spatially heterogeneous. Trailing edge populations face genetic erosion, while leading edge populations face expansion load. The geometric pattern of contraction matters, with fragmentation posing the greatest threat to genetic integrity. Ultimately, the survival of species depends on whether their rate of adaptation—constrained by $N_e$ and burdened by load—can outpace the velocity of climate change. Conservation strategies must therefore move beyond simple census counts to actively manage $N_e$, facilitate gene flow, and mitigate the genomic offsets created by a warming world.

### References
[cite: 3, 6] Montezuma Quail genomics and load dynamics.
[cite: 5] Vitis arizonica and expansion load/mutation surfing.
[cite: 4, 8] General theory of genetic load, drift, and mutational meltdown.
[cite: 1] Definitions and theory of Effective Population Size ($N_e$).
[cite: 11, 12] Range shifts, trailing edges, and genetic erosion.
[cite: 18] Ptarmigan genomic vulnerability and climate offset.
[cite: 13] Patterns of range contraction (fragmentation vs. shrinkage).
[cite: 17, 24] Genomic offset statistics and theory.
[cite: 19, 23] Assisted migration and standing genetic variation.
[cite: 9] Mutational meltdown models.
[cite: 20, 21] Evolutionary rescue and genetic rescue.
[cite: 14, 25] Simulation of range contraction patterns.
[cite: 10] Bat populations and trailing edge diversity.
[cite: 7] Inbreeding load vs. drift load mechanisms.
[cite: 15, 16] Speed of range contraction and diversity retention.
[cite: 18] Genomic vulnerability in Ptarmigan.

**Sources:**
1. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpAACHpX2Qi5H9NC_-7Y0Lh3Sils_5IxUB-cK4HL31V6OzRa8-azZGVakI98TePgmLzT-2OBmar9HqJXsLgw0hwVot5xQMBI5MPGVFPFZDEci3O9CIn9gfK6W2XeCCCwEsexAHt1PaHu6gp1OO)
2. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFaDOyPE9xbDsHSw7Ofzz8tJXwB8qdyrU6vdI9TIk0RulhGW0lQf3ZXBRDrkIDLpRTnLW9lxox9GhdS91gvxrRVhOpjyTVZsZMgKsA7cuOGYhAg_Giwh8HSXrolpanwGXz6Ti_pf-Psog==)
3. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2MENI04kg1HbZVlmm_8C45S7WQ7C0iR8d8ar0WZyBvRtnOald1Epou_W_X-108JOEgM0Ws8-oACLWS6gqg8tx0XD8dpb9hBHJ4VRdGaJgeeQmDn5D-MMvh5dO7zCdNKAfbvrsUhPgQp0gmqzbcw==)
4. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyQ9qksHQiVz7RaF4-gVUp7cVDP32x2nNphBwAA46DAnPoowO9-XsZrr9jf-NgwSOOm70GEAbtFeUbI9SP3X-jMn456T-C2-M1vhxn2XavZVsCT8J2Xl2RTInqIzpfZeHrbacqWE4d)
5. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGweOJa9d1GVF9mcOD_HNWOH4Vcw0aPbFO9mPs6Rqh-OuE-cDIG7imhM93RSfueJ9h6qs6_9FVJ-UCDZCXYD099xG7-A04UcbFQ3Obwy8hZ9fyIdBpWgR7p8ag1fPRApeZpGUeL7x7VbA==)
6. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoG0OQlZcZ5pK3kVkUsCi04se_s6lX0MTgM_i3KpgDC2VjF3VyjJ7zvDKA5qKDfiCWy8GoD9uV0CiFEz3Grhu4oINXeenVqpJQLR0qvd64JsZT42meNUMhnJCMXPRWXBU0xQDnF15M)
7. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3okxJWsGv0GjNFRmhJy40a8je9Z5ywThDEpEaVR-TTdXw0B1hzwTKNI5pUBtwLYLGxcDpObrHouDkS5tDsIqNZ7lckVoFbiSs4EOnQx9kl9J4pSGdjnmS6X60XtEGo7V52mu6V3xPDw==)
8. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHW1fFBbuC9PfgdgjyUkwbQJx98u59A1BthxXByFLxqhzzeZsDPdB9DtEJbcbHllP8LZccObWAA341bxpbFyjR7FPCXEVZfMfXYyVzS2ojXCTnmvdEYObzDrlF7dF6IURw=)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHibQa6UtTK4GM-Dbymqc7K-svNiLzajZk0m5FyFnQq4xhOdkPQ_PIFgKM1DjyA21vf0UBXarcIyD1JD98ZArl4be0MY-8za0goXZgCoMBhdcQUbkESbtmdXq8noWmCWYi2l--CFSdq)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFetTpgSMKznQde7SNMlC8Xjjy2HUqBzKHVU6U6-o-THl_b_oAqI8bSC2LrnAfrz3KAaGW3OjkXXd7_MFw5_kpO_u1FPtA7MEulDP6PxfHECrOLrTq2vOFExDXpwt9-2FcNu0VWZQYx_u-G4K1mIEYz9ZQkOV0XlKeIh6JpSaqZstls6xa1Xpjq7KYPgD-2KEF0SUJje1nZG_0_lA8PSwjfrfMbO6JLB4GcUfMsO4VZypUtS0_oiIJYWUUaygkuV95R6WCeg9O7R1BblPI=)
11. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy9BimpS20-UdZ1MsSmtVaoGLVPO4SLYasVto93TUEWc7M8ApXgZmTGQr3maH8OhzBsbcU3_FK2UAr2ise4w3GkQ5d3EKU7aPe1Bd9Ty1EoqqSt3YvimUNKrIuTPoU3o7abNRed86q)
12. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL9raxY-KIckJIHwq2F0g-TRg3pQlJTUP0WBxljgA6dWqGAJRxcfOOwY2t-OczjV1ZaYoKzLy_iKsJgqig_265L7MZd6Cl_D-v1fM55GveGHK12uQrOasQ5qy9sGnphX64aVCCrIV2)
13. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQ8ORaHw1dtMCyrlp9HVtRv1swrrcJ4nW7bKwFRWJT7f0ePaNIrFMIaatMnQCK2UJCXeNXVKQ79UkhFNMo9TbYo2sobCZZnT9urkoGfJHabYfYP5K3DCR_bLPIQohm42P9YZnLczNR)
14. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3Ql1lq_7tMucj9V0nvfl1h-eb264tGylchm8c5IUp5E0xz_pXnbiL4ycneemRqex1pvS1JhYeaAp4QNVxToYFYKnPtITdHQqGc_2AjICiy5oGD-jz4fClSG1YSsCj5m7MrTVL13qIwJVg0EcDcW0MpQ3Yuy1G4lAvbYd2qe5bGMGpZOQqE-8IInmFZXffhYnSABVhU9ajQNbNlw0mWDdbjBr40nVWI0FsIqSmkiwaZlNuyeTlfXy2RJYZMFyiuKXVRpq3vYL1fUBaqw==)
15. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoeFAbUP468bqBVTX6j2ukO7yhUDzSGoeUEwbCpsOkPG5jD8I-nWIMsXNvA-aB07EOf0VPrPT4EusStKs5uSfFO6Y8Jl-6xiflQeLxECTohDjUq7h2F9aIb_LEOKe3sw==)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrfTqaR8dRLl4cB4spkRtZUxE1axO9Vy8tBcHkMWNCyu7Sxx2HEYaIf4Hg8zMtaYziDHtf--C4dx4KOBglboy44BNiypolwHx6g9Uywua5JvZILv1_CuX77VBy8eqga06QIoXKePsPF2iDIuewII_IRRL8BZNSp12G1BfSswajCmclcJFZIf0CFtdwENidcv1raHbnRccNiPaCsMw5vqvi3IXP4sTsf_otwL1LDJ-3jBVj)
17. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGV7z-Ah252htZ1PnQLyo0phQ9IzIS2Ptb8X_TfVeLKk5hL-OC8mgt5D1rQCPO9AguqfKxfk4kPG4zMQVxe0LsIxkGNVAeOsmeEW49ZBwV5X_IJWFMJuvnePqe1amOyvMW3yhBHPJxT_Q==)
18. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEe6svuks3flrhZrJGhYIHZU5rBBbiTtWBcxKwmDz8bYH8T_Ooc-jWhpBZXrDwuSvVzj3FdJVXAxhD2T1YQlmMLwOY2Qx9uCNLm4ien2jILPyXle4hq4IK7bE0E1PP6ULFx7M8EL7o-Vai3dmk5-TEXSs2wKNU5XV5STHQ=)
19. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmDJwGITjarF22i5hIBs5IAmh3szcxnf4wXyCyqPzq8upaLQk3F_dFEsL4PhcFwpn7EIJIyOJmNIPmWUEj9N-KjkI58dTzSFkyOu8SRptBXFsAEeLEf4-JNDiQQqhyWC4k-ehc5lPvvg==)
20. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYGQeUyspSXf9-ounaDSiIbO2v7FQnbOvARVNqGfDC0eVrRLYZCybSsIN6iVsFN6uJ-P2-5mAwlFOhXydRftjBguVLxYSVVDH7VM-J7uGJsBz4HNfqxZT3FkfqR2Gs2buqDT0w-Ip3)
21. [biorxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE91nLTuwbTSekPDvpc2bH_NfgW0f4sSbmTsVZ6cBrBWy8phUsNJkK57Wu5U87kIjPfZ-_R-hsQMFD773_Dk2F-HoDx2ZICrW32Gduu8E7U6_giHnRfeFbQKpcDkIMMxYd4ciBRVYYLmjp9G8r7v_1yfPffk9NyHEp4fAg=)
22. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHe9dBM9jTjdVGw0FudfhUtVQ6SvsVjOZCXzJ9SQgKwEenc7imoCH0kpDUbVkyW0TYGY8tvt-sjWMtbrfdppJvQp9_YFLL8U2L9Im-pDXDlnm1hqInn3ow-zmGhGrx_Uf0fCi2ZJbn_)
23. [pnas.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgbx77fQhNk9mAc81KEq1UXoF9Fdy7_ZhV77b6AZ0YniS60oJgn0K7bhUOFIm9-4BdbAhVSp3z1XwAOdOL6BLHw5-_CM2V3WD3LbkHMSqAHbeNavxGd_YTAqgylDkYAF0LGr3Flzs=)
24. [cirad.fr](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqBswU-RopMYwxIYfzLa1Sg1uKLaETB7PQz4UHIPCXN6m46ZW42k5Vt-ULSASEMODSyeyq8x_3-MN2LQiS6aCH43mgP24nb9vrcJo2x5pGpIGQzKjiu2ufmlkazY_C1803sk5ZynCQ5izsKZ8wyEVRL5QU7Kct-_Xemj5piTD1HnKjZz1wI9siL-7qQmaXc0_QJ7Zjw24tSmowzK9gH7n11-xcFBGxdWydFi2H-8KD)
25. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3xAm6qdS2dOvdEEp0vOamRrWhL73iweCrPNfYu1RX_TFR7T2WPKfz7CGEcEHKmdlQGxAd_PoxgrWBLZJeTvsK9TfdgUd7VZuK_6UbPTNUSW8ImxSJf8c5Wv93eAG6wA9csIdxzDiAF7mK8TnMgfUfwomkX0ulGn0SsJ2w3pyHPBvhMt3JiUJw4Xk1-QA7JGsYpTPj2RX8CJh_cbkAeW7W23ow_5qvkgutfA32rJ7zVOSb885BgiiGAfE4gEHSiw==)


## Annotations
Annotation(end_index=3416, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpAACHpX2Qi5H9NC_-7Y0Lh3Sils_5IxUB-cK4HL31V6OzRa8-azZGVakI98TePgmLzT-2OBmar9HqJXsLgw0hwVot5xQMBI5MPGVFPFZDEci3O9CIn9gfK6W2XeCCCwEsexAHt1PaHu6gp1OO', start_index=3407)
Annotation(end_index=3590, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpAACHpX2Qi5H9NC_-7Y0Lh3Sils_5IxUB-cK4HL31V6OzRa8-azZGVakI98TePgmLzT-2OBmar9HqJXsLgw0hwVot5xQMBI5MPGVFPFZDEci3O9CIn9gfK6W2XeCCCwEsexAHt1PaHu6gp1OO', start_index=3578)
Annotation(end_index=3590, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFaDOyPE9xbDsHSw7Ofzz8tJXwB8qdyrU6vdI9TIk0RulhGW0lQf3ZXBRDrkIDLpRTnLW9lxox9GhdS91gvxrRVhOpjyTVZsZMgKsA7cuOGYhAg_Giwh8HSXrolpanwGXz6Ti_pf-Psog==', start_index=3578)
Annotation(end_index=4148, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2MENI04kg1HbZVlmm_8C45S7WQ7C0iR8d8ar0WZyBvRtnOald1Epou_W_X-108JOEgM0Ws8-oACLWS6gqg8tx0XD8dpb9hBHJ4VRdGaJgeeQmDn5D-MMvh5dO7zCdNKAfbvrsUhPgQp0gmqzbcw==', start_index=4136)
Annotation(end_index=4148, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyQ9qksHQiVz7RaF4-gVUp7cVDP32x2nNphBwAA46DAnPoowO9-XsZrr9jf-NgwSOOm70GEAbtFeUbI9SP3X-jMn456T-C2-M1vhxn2XavZVsCT8J2Xl2RTInqIzpfZeHrbacqWE4d', start_index=4136)
Annotation(end_index=4305, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2MENI04kg1HbZVlmm_8C45S7WQ7C0iR8d8ar0WZyBvRtnOald1Epou_W_X-108JOEgM0Ws8-oACLWS6gqg8tx0XD8dpb9hBHJ4VRdGaJgeeQmDn5D-MMvh5dO7zCdNKAfbvrsUhPgQp0gmqzbcw==', start_index=4293)
Annotation(end_index=4305, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGweOJa9d1GVF9mcOD_HNWOH4Vcw0aPbFO9mPs6Rqh-OuE-cDIG7imhM93RSfueJ9h6qs6_9FVJ-UCDZCXYD099xG7-A04UcbFQ3Obwy8hZ9fyIdBpWgR7p8ag1fPRApeZpGUeL7x7VbA==', start_index=4293)
Annotation(end_index=4665, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyQ9qksHQiVz7RaF4-gVUp7cVDP32x2nNphBwAA46DAnPoowO9-XsZrr9jf-NgwSOOm70GEAbtFeUbI9SP3X-jMn456T-C2-M1vhxn2XavZVsCT8J2Xl2RTInqIzpfZeHrbacqWE4d', start_index=4656)
Annotation(end_index=4834, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoG0OQlZcZ5pK3kVkUsCi04se_s6lX0MTgM_i3KpgDC2VjF3VyjJ7zvDKA5qKDfiCWy8GoD9uV0CiFEz3Grhu4oINXeenVqpJQLR0qvd64JsZT42meNUMhnJCMXPRWXBU0xQDnF15M', start_index=4825)
Annotation(end_index=5215, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3okxJWsGv0GjNFRmhJy40a8je9Z5ywThDEpEaVR-TTdXw0B1hzwTKNI5pUBtwLYLGxcDpObrHouDkS5tDsIqNZ7lckVoFbiSs4EOnQx9kl9J4pSGdjnmS6X60XtEGo7V52mu6V3xPDw==', start_index=5203)
Annotation(end_index=5215, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoG0OQlZcZ5pK3kVkUsCi04se_s6lX0MTgM_i3KpgDC2VjF3VyjJ7zvDKA5qKDfiCWy8GoD9uV0CiFEz3Grhu4oINXeenVqpJQLR0qvd64JsZT42meNUMhnJCMXPRWXBU0xQDnF15M', start_index=5203)
Annotation(end_index=5421, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGweOJa9d1GVF9mcOD_HNWOH4Vcw0aPbFO9mPs6Rqh-OuE-cDIG7imhM93RSfueJ9h6qs6_9FVJ-UCDZCXYD099xG7-A04UcbFQ3Obwy8hZ9fyIdBpWgR7p8ag1fPRApeZpGUeL7x7VbA==', start_index=5412)
Annotation(end_index=6324, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2MENI04kg1HbZVlmm_8C45S7WQ7C0iR8d8ar0WZyBvRtnOald1Epou_W_X-108JOEgM0Ws8-oACLWS6gqg8tx0XD8dpb9hBHJ4VRdGaJgeeQmDn5D-MMvh5dO7zCdNKAfbvrsUhPgQp0gmqzbcw==', start_index=6312)
Annotation(end_index=6324, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoG0OQlZcZ5pK3kVkUsCi04se_s6lX0MTgM_i3KpgDC2VjF3VyjJ7zvDKA5qKDfiCWy8GoD9uV0CiFEz3Grhu4oINXeenVqpJQLR0qvd64JsZT42meNUMhnJCMXPRWXBU0xQDnF15M', start_index=6312)
Annotation(end_index=6551, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2MENI04kg1HbZVlmm_8C45S7WQ7C0iR8d8ar0WZyBvRtnOald1Epou_W_X-108JOEgM0Ws8-oACLWS6gqg8tx0XD8dpb9hBHJ4VRdGaJgeeQmDn5D-MMvh5dO7zCdNKAfbvrsUhPgQp0gmqzbcw==', start_index=6539)
Annotation(end_index=6551, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoG0OQlZcZ5pK3kVkUsCi04se_s6lX0MTgM_i3KpgDC2VjF3VyjJ7zvDKA5qKDfiCWy8GoD9uV0CiFEz3Grhu4oINXeenVqpJQLR0qvd64JsZT42meNUMhnJCMXPRWXBU0xQDnF15M', start_index=6539)
Annotation(end_index=6892, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoG0OQlZcZ5pK3kVkUsCi04se_s6lX0MTgM_i3KpgDC2VjF3VyjJ7zvDKA5qKDfiCWy8GoD9uV0CiFEz3Grhu4oINXeenVqpJQLR0qvd64JsZT42meNUMhnJCMXPRWXBU0xQDnF15M', start_index=6883)
Annotation(end_index=7153, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3okxJWsGv0GjNFRmhJy40a8je9Z5ywThDEpEaVR-TTdXw0B1hzwTKNI5pUBtwLYLGxcDpObrHouDkS5tDsIqNZ7lckVoFbiSs4EOnQx9kl9J4pSGdjnmS6X60XtEGo7V52mu6V3xPDw==', start_index=7144)
Annotation(end_index=7514, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3okxJWsGv0GjNFRmhJy40a8je9Z5ywThDEpEaVR-TTdXw0B1hzwTKNI5pUBtwLYLGxcDpObrHouDkS5tDsIqNZ7lckVoFbiSs4EOnQx9kl9J4pSGdjnmS6X60XtEGo7V52mu6V3xPDw==', start_index=7502)
Annotation(end_index=7514, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoG0OQlZcZ5pK3kVkUsCi04se_s6lX0MTgM_i3KpgDC2VjF3VyjJ7zvDKA5qKDfiCWy8GoD9uV0CiFEz3Grhu4oINXeenVqpJQLR0qvd64JsZT42meNUMhnJCMXPRWXBU0xQDnF15M', start_index=7502)
Annotation(end_index=7755, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHW1fFBbuC9PfgdgjyUkwbQJx98u59A1BthxXByFLxqhzzeZsDPdB9DtEJbcbHllP8LZccObWAA341bxpbFyjR7FPCXEVZfMfXYyVzS2ojXCTnmvdEYObzDrlF7dF6IURw=', start_index=7743)
Annotation(end_index=7755, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHibQa6UtTK4GM-Dbymqc7K-svNiLzajZk0m5FyFnQq4xhOdkPQ_PIFgKM1DjyA21vf0UBXarcIyD1JD98ZArl4be0MY-8za0goXZgCoMBhdcQUbkESbtmdXq8noWmCWYi2l--CFSdq', start_index=7743)
Annotation(end_index=8291, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHibQa6UtTK4GM-Dbymqc7K-svNiLzajZk0m5FyFnQq4xhOdkPQ_PIFgKM1DjyA21vf0UBXarcIyD1JD98ZArl4be0MY-8za0goXZgCoMBhdcQUbkESbtmdXq8noWmCWYi2l--CFSdq', start_index=8282)
Annotation(end_index=8843, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFetTpgSMKznQde7SNMlC8Xjjy2HUqBzKHVU6U6-o-THl_b_oAqI8bSC2LrnAfrz3KAaGW3OjkXXd7_MFw5_kpO_u1FPtA7MEulDP6PxfHECrOLrTq2vOFExDXpwt9-2FcNu0VWZQYx_u-G4K1mIEYz9ZQkOV0XlKeIh6JpSaqZstls6xa1Xpjq7KYPgD-2KEF0SUJje1nZG_0_lA8PSwjfrfMbO6JLB4GcUfMsO4VZypUtS0_oiIJYWUUaygkuV95R6WCeg9O7R1BblPI=', start_index=8833)
Annotation(end_index=9135, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy9BimpS20-UdZ1MsSmtVaoGLVPO4SLYasVto93TUEWc7M8ApXgZmTGQr3maH8OhzBsbcU3_FK2UAr2ise4w3GkQ5d3EKU7aPe1Bd9Ty1EoqqSt3YvimUNKrIuTPoU3o7abNRed86q', start_index=9125)
Annotation(end_index=9408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFetTpgSMKznQde7SNMlC8Xjjy2HUqBzKHVU6U6-o-THl_b_oAqI8bSC2LrnAfrz3KAaGW3OjkXXd7_MFw5_kpO_u1FPtA7MEulDP6PxfHECrOLrTq2vOFExDXpwt9-2FcNu0VWZQYx_u-G4K1mIEYz9ZQkOV0XlKeIh6JpSaqZstls6xa1Xpjq7KYPgD-2KEF0SUJje1nZG_0_lA8PSwjfrfMbO6JLB4GcUfMsO4VZypUtS0_oiIJYWUUaygkuV95R6WCeg9O7R1BblPI=', start_index=9394)
Annotation(end_index=9408, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL9raxY-KIckJIHwq2F0g-TRg3pQlJTUP0WBxljgA6dWqGAJRxcfOOwY2t-OczjV1ZaYoKzLy_iKsJgqig_265L7MZd6Cl_D-v1fM55GveGHK12uQrOasQ5qy9sGnphX64aVCCrIV2', start_index=9394)
Annotation(end_index=9938, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGweOJa9d1GVF9mcOD_HNWOH4Vcw0aPbFO9mPs6Rqh-OuE-cDIG7imhM93RSfueJ9h6qs6_9FVJ-UCDZCXYD099xG7-A04UcbFQ3Obwy8hZ9fyIdBpWgR7p8ag1fPRApeZpGUeL7x7VbA==', start_index=9929)
Annotation(end_index=10200, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGweOJa9d1GVF9mcOD_HNWOH4Vcw0aPbFO9mPs6Rqh-OuE-cDIG7imhM93RSfueJ9h6qs6_9FVJ-UCDZCXYD099xG7-A04UcbFQ3Obwy8hZ9fyIdBpWgR7p8ag1fPRApeZpGUeL7x7VbA==', start_index=10191)
Annotation(end_index=10636, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy9BimpS20-UdZ1MsSmtVaoGLVPO4SLYasVto93TUEWc7M8ApXgZmTGQr3maH8OhzBsbcU3_FK2UAr2ise4w3GkQ5d3EKU7aPe1Bd9Ty1EoqqSt3YvimUNKrIuTPoU3o7abNRed86q', start_index=10626)
Annotation(end_index=10925, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3Ql1lq_7tMucj9V0nvfl1h-eb264tGylchm8c5IUp5E0xz_pXnbiL4ycneemRqex1pvS1JhYeaAp4QNVxToYFYKnPtITdHQqGc_2AjICiy5oGD-jz4fClSG1YSsCj5m7MrTVL13qIwJVg0EcDcW0MpQ3Yuy1G4lAvbYd2qe5bGMGpZOQqE-8IInmFZXffhYnSABVhU9ajQNbNlw0mWDdbjBr40nVWI0FsIqSmkiwaZlNuyeTlfXy2RJYZMFyiuKXVRpq3vYL1fUBaqw==', start_index=10911)
Annotation(end_index=10925, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQ8ORaHw1dtMCyrlp9HVtRv1swrrcJ4nW7bKwFRWJT7f0ePaNIrFMIaatMnQCK2UJCXeNXVKQ79UkhFNMo9TbYo2sobCZZnT9urkoGfJHabYfYP5K3DCR_bLPIQohm42P9YZnLczNR', start_index=10911)
Annotation(end_index=11233, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQ8ORaHw1dtMCyrlp9HVtRv1swrrcJ4nW7bKwFRWJT7f0ePaNIrFMIaatMnQCK2UJCXeNXVKQ79UkhFNMo9TbYo2sobCZZnT9urkoGfJHabYfYP5K3DCR_bLPIQohm42P9YZnLczNR', start_index=11223)
Annotation(end_index=11425, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3Ql1lq_7tMucj9V0nvfl1h-eb264tGylchm8c5IUp5E0xz_pXnbiL4ycneemRqex1pvS1JhYeaAp4QNVxToYFYKnPtITdHQqGc_2AjICiy5oGD-jz4fClSG1YSsCj5m7MrTVL13qIwJVg0EcDcW0MpQ3Yuy1G4lAvbYd2qe5bGMGpZOQqE-8IInmFZXffhYnSABVhU9ajQNbNlw0mWDdbjBr40nVWI0FsIqSmkiwaZlNuyeTlfXy2RJYZMFyiuKXVRpq3vYL1fUBaqw==', start_index=11411)
Annotation(end_index=11425, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQ8ORaHw1dtMCyrlp9HVtRv1swrrcJ4nW7bKwFRWJT7f0ePaNIrFMIaatMnQCK2UJCXeNXVKQ79UkhFNMo9TbYo2sobCZZnT9urkoGfJHabYfYP5K3DCR_bLPIQohm42P9YZnLczNR', start_index=11411)
Annotation(end_index=11798, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQ8ORaHw1dtMCyrlp9HVtRv1swrrcJ4nW7bKwFRWJT7f0ePaNIrFMIaatMnQCK2UJCXeNXVKQ79UkhFNMo9TbYo2sobCZZnT9urkoGfJHabYfYP5K3DCR_bLPIQohm42P9YZnLczNR', start_index=11788)
Annotation(end_index=12054, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3Ql1lq_7tMucj9V0nvfl1h-eb264tGylchm8c5IUp5E0xz_pXnbiL4ycneemRqex1pvS1JhYeaAp4QNVxToYFYKnPtITdHQqGc_2AjICiy5oGD-jz4fClSG1YSsCj5m7MrTVL13qIwJVg0EcDcW0MpQ3Yuy1G4lAvbYd2qe5bGMGpZOQqE-8IInmFZXffhYnSABVhU9ajQNbNlw0mWDdbjBr40nVWI0FsIqSmkiwaZlNuyeTlfXy2RJYZMFyiuKXVRpq3vYL1fUBaqw==', start_index=12044)
Annotation(end_index=12258, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoeFAbUP468bqBVTX6j2ukO7yhUDzSGoeUEwbCpsOkPG5jD8I-nWIMsXNvA-aB07EOf0VPrPT4EusStKs5uSfFO6Y8Jl-6xiflQeLxECTohDjUq7h2F9aIb_LEOKe3sw==', start_index=12244)
Annotation(end_index=12258, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrfTqaR8dRLl4cB4spkRtZUxE1axO9Vy8tBcHkMWNCyu7Sxx2HEYaIf4Hg8zMtaYziDHtf--C4dx4KOBglboy44BNiypolwHx6g9Uywua5JvZILv1_CuX77VBy8eqga06QIoXKePsPF2iDIuewII_IRRL8BZNSp12G1BfSswajCmclcJFZIf0CFtdwENidcv1raHbnRccNiPaCsMw5vqvi3IXP4sTsf_otwL1LDJ-3jBVj', start_index=12244)
Annotation(end_index=12593, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoeFAbUP468bqBVTX6j2ukO7yhUDzSGoeUEwbCpsOkPG5jD8I-nWIMsXNvA-aB07EOf0VPrPT4EusStKs5uSfFO6Y8Jl-6xiflQeLxECTohDjUq7h2F9aIb_LEOKe3sw==', start_index=12583)
Annotation(end_index=13021, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEe6svuks3flrhZrJGhYIHZU5rBBbiTtWBcxKwmDz8bYH8T_Ooc-jWhpBZXrDwuSvVzj3FdJVXAxhD2T1YQlmMLwOY2Qx9uCNLm4ien2jILPyXle4hq4IK7bE0E1PP6ULFx7M8EL7o-Vai3dmk5-TEXSs2wKNU5XV5STHQ=', start_index=13007)
Annotation(end_index=13021, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGV7z-Ah252htZ1PnQLyo0phQ9IzIS2Ptb8X_TfVeLKk5hL-OC8mgt5D1rQCPO9AguqfKxfk4kPG4zMQVxe0LsIxkGNVAeOsmeEW49ZBwV5X_IJWFMJuvnePqe1amOyvMW3yhBHPJxT_Q==', start_index=13007)
Annotation(end_index=13437, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEe6svuks3flrhZrJGhYIHZU5rBBbiTtWBcxKwmDz8bYH8T_Ooc-jWhpBZXrDwuSvVzj3FdJVXAxhD2T1YQlmMLwOY2Qx9uCNLm4ien2jILPyXle4hq4IK7bE0E1PP6ULFx7M8EL7o-Vai3dmk5-TEXSs2wKNU5XV5STHQ=', start_index=13427)
Annotation(end_index=13802, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEe6svuks3flrhZrJGhYIHZU5rBBbiTtWBcxKwmDz8bYH8T_Ooc-jWhpBZXrDwuSvVzj3FdJVXAxhD2T1YQlmMLwOY2Qx9uCNLm4ien2jILPyXle4hq4IK7bE0E1PP6ULFx7M8EL7o-Vai3dmk5-TEXSs2wKNU5XV5STHQ=', start_index=13792)
Annotation(end_index=14041, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEe6svuks3flrhZrJGhYIHZU5rBBbiTtWBcxKwmDz8bYH8T_Ooc-jWhpBZXrDwuSvVzj3FdJVXAxhD2T1YQlmMLwOY2Qx9uCNLm4ien2jILPyXle4hq4IK7bE0E1PP6ULFx7M8EL7o-Vai3dmk5-TEXSs2wKNU5XV5STHQ=', start_index=14031)
Annotation(end_index=14406, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmDJwGITjarF22i5hIBs5IAmh3szcxnf4wXyCyqPzq8upaLQk3F_dFEsL4PhcFwpn7EIJIyOJmNIPmWUEj9N-KjkI58dTzSFkyOu8SRptBXFsAEeLEf4-JNDiQQqhyWC4k-ehc5lPvvg==', start_index=14396)
Annotation(end_index=14592, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYGQeUyspSXf9-ounaDSiIbO2v7FQnbOvARVNqGfDC0eVrRLYZCybSsIN6iVsFN6uJ-P2-5mAwlFOhXydRftjBguVLxYSVVDH7VM-J7uGJsBz4HNfqxZT3FkfqR2Gs2buqDT0w-Ip3', start_index=14582)
Annotation(end_index=14831, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYGQeUyspSXf9-ounaDSiIbO2v7FQnbOvARVNqGfDC0eVrRLYZCybSsIN6iVsFN6uJ-P2-5mAwlFOhXydRftjBguVLxYSVVDH7VM-J7uGJsBz4HNfqxZT3FkfqR2Gs2buqDT0w-Ip3', start_index=14821)
Annotation(end_index=15308, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE91nLTuwbTSekPDvpc2bH_NfgW0f4sSbmTsVZ6cBrBWy8phUsNJkK57Wu5U87kIjPfZ-_R-hsQMFD773_Dk2F-HoDx2ZICrW32Gduu8E7U6_giHnRfeFbQKpcDkIMMxYd4ciBRVYYLmjp9G8r7v_1yfPffk9NyHEp4fAg=', start_index=15298)
Annotation(end_index=15591, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE91nLTuwbTSekPDvpc2bH_NfgW0f4sSbmTsVZ6cBrBWy8phUsNJkK57Wu5U87kIjPfZ-_R-hsQMFD773_Dk2F-HoDx2ZICrW32Gduu8E7U6_giHnRfeFbQKpcDkIMMxYd4ciBRVYYLmjp9G8r7v_1yfPffk9NyHEp4fAg=', start_index=15577)
Annotation(end_index=15591, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHe9dBM9jTjdVGw0FudfhUtVQ6SvsVjOZCXzJ9SQgKwEenc7imoCH0kpDUbVkyW0TYGY8tvt-sjWMtbrfdppJvQp9_YFLL8U2L9Im-pDXDlnm1hqInn3ow-zmGhGrx_Uf0fCi2ZJbn_', start_index=15577)
Annotation(end_index=16044, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgbx77fQhNk9mAc81KEq1UXoF9Fdy7_ZhV77b6AZ0YniS60oJgn0K7bhUOFIm9-4BdbAhVSp3z1XwAOdOL6BLHw5-_CM2V3WD3LbkHMSqAHbeNavxGd_YTAqgylDkYAF0LGr3Flzs=', start_index=16034)
Annotation(end_index=16245, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmDJwGITjarF22i5hIBs5IAmh3szcxnf4wXyCyqPzq8upaLQk3F_dFEsL4PhcFwpn7EIJIyOJmNIPmWUEj9N-KjkI58dTzSFkyOu8SRptBXFsAEeLEf4-JNDiQQqhyWC4k-ehc5lPvvg==', start_index=16231)
Annotation(end_index=16245, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgbx77fQhNk9mAc81KEq1UXoF9Fdy7_ZhV77b6AZ0YniS60oJgn0K7bhUOFIm9-4BdbAhVSp3z1XwAOdOL6BLHw5-_CM2V3WD3LbkHMSqAHbeNavxGd_YTAqgylDkYAF0LGr3Flzs=', start_index=16231)
Annotation(end_index=16365, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQ8ORaHw1dtMCyrlp9HVtRv1swrrcJ4nW7bKwFRWJT7f0ePaNIrFMIaatMnQCK2UJCXeNXVKQ79UkhFNMo9TbYo2sobCZZnT9urkoGfJHabYfYP5K3DCR_bLPIQohm42P9YZnLczNR', start_index=16355)
Annotation(end_index=16566, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHe9dBM9jTjdVGw0FudfhUtVQ6SvsVjOZCXzJ9SQgKwEenc7imoCH0kpDUbVkyW0TYGY8tvt-sjWMtbrfdppJvQp9_YFLL8U2L9Im-pDXDlnm1hqInn3ow-zmGhGrx_Uf0fCi2ZJbn_', start_index=16556)
Annotation(end_index=17597, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2MENI04kg1HbZVlmm_8C45S7WQ7C0iR8d8ar0WZyBvRtnOald1Epou_W_X-108JOEgM0Ws8-oACLWS6gqg8tx0XD8dpb9hBHJ4VRdGaJgeeQmDn5D-MMvh5dO7zCdNKAfbvrsUhPgQp0gmqzbcw==', start_index=17585)
Annotation(end_index=17597, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoG0OQlZcZ5pK3kVkUsCi04se_s6lX0MTgM_i3KpgDC2VjF3VyjJ7zvDKA5qKDfiCWy8GoD9uV0CiFEz3Grhu4oINXeenVqpJQLR0qvd64JsZT42meNUMhnJCMXPRWXBU0xQDnF15M', start_index=17585)
Annotation(end_index=17651, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGweOJa9d1GVF9mcOD_HNWOH4Vcw0aPbFO9mPs6Rqh-OuE-cDIG7imhM93RSfueJ9h6qs6_9FVJ-UCDZCXYD099xG7-A04UcbFQ3Obwy8hZ9fyIdBpWgR7p8ag1fPRApeZpGUeL7x7VbA==', start_index=17642)
Annotation(end_index=17717, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHW1fFBbuC9PfgdgjyUkwbQJx98u59A1BthxXByFLxqhzzeZsDPdB9DtEJbcbHllP8LZccObWAA341bxpbFyjR7FPCXEVZfMfXYyVzS2ojXCTnmvdEYObzDrlF7dF6IURw=', start_index=17705)
Annotation(end_index=17717, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyQ9qksHQiVz7RaF4-gVUp7cVDP32x2nNphBwAA46DAnPoowO9-XsZrr9jf-NgwSOOm70GEAbtFeUbI9SP3X-jMn456T-C2-M1vhxn2XavZVsCT8J2Xl2RTInqIzpfZeHrbacqWE4d', start_index=17705)
Annotation(end_index=17791, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEpAACHpX2Qi5H9NC_-7Y0Lh3Sils_5IxUB-cK4HL31V6OzRa8-azZGVakI98TePgmLzT-2OBmar9HqJXsLgw0hwVot5xQMBI5MPGVFPFZDEci3O9CIn9gfK6W2XeCCCwEsexAHt1PaHu6gp1OO', start_index=17782)
Annotation(end_index=17867, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEy9BimpS20-UdZ1MsSmtVaoGLVPO4SLYasVto93TUEWc7M8ApXgZmTGQr3maH8OhzBsbcU3_FK2UAr2ise4w3GkQ5d3EKU7aPe1Bd9Ty1EoqqSt3YvimUNKrIuTPoU3o7abNRed86q', start_index=17853)
Annotation(end_index=17867, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL9raxY-KIckJIHwq2F0g-TRg3pQlJTUP0WBxljgA6dWqGAJRxcfOOwY2t-OczjV1ZaYoKzLy_iKsJgqig_265L7MZd6Cl_D-v1fM55GveGHK12uQrOasQ5qy9sGnphX64aVCCrIV2', start_index=17853)
Annotation(end_index=17929, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEe6svuks3flrhZrJGhYIHZU5rBBbiTtWBcxKwmDz8bYH8T_Ooc-jWhpBZXrDwuSvVzj3FdJVXAxhD2T1YQlmMLwOY2Qx9uCNLm4ien2jILPyXle4hq4IK7bE0E1PP6ULFx7M8EL7o-Vai3dmk5-TEXSs2wKNU5XV5STHQ=', start_index=17919)
Annotation(end_index=17992, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQ8ORaHw1dtMCyrlp9HVtRv1swrrcJ4nW7bKwFRWJT7f0ePaNIrFMIaatMnQCK2UJCXeNXVKQ79UkhFNMo9TbYo2sobCZZnT9urkoGfJHabYfYP5K3DCR_bLPIQohm42P9YZnLczNR', start_index=17982)
Annotation(end_index=18068, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGV7z-Ah252htZ1PnQLyo0phQ9IzIS2Ptb8X_TfVeLKk5hL-OC8mgt5D1rQCPO9AguqfKxfk4kPG4zMQVxe0LsIxkGNVAeOsmeEW49ZBwV5X_IJWFMJuvnePqe1amOyvMW3yhBHPJxT_Q==', start_index=18054)
Annotation(end_index=18068, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqBswU-RopMYwxIYfzLa1Sg1uKLaETB7PQz4UHIPCXN6m46ZW42k5Vt-ULSASEMODSyeyq8x_3-MN2LQiS6aCH43mgP24nb9vrcJo2x5pGpIGQzKjiu2ufmlkazY_C1803sk5ZynCQ5izsKZ8wyEVRL5QU7Kct-_Xemj5piTD1HnKjZz1wI9siL-7qQmaXc0_QJ7Zjw24tSmowzK9gH7n11-xcFBGxdWydFi2H-8KD', start_index=18054)
Annotation(end_index=18121, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmDJwGITjarF22i5hIBs5IAmh3szcxnf4wXyCyqPzq8upaLQk3F_dFEsL4PhcFwpn7EIJIyOJmNIPmWUEj9N-KjkI58dTzSFkyOu8SRptBXFsAEeLEf4-JNDiQQqhyWC4k-ehc5lPvvg==', start_index=18107)
Annotation(end_index=18121, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGgbx77fQhNk9mAc81KEq1UXoF9Fdy7_ZhV77b6AZ0YniS60oJgn0K7bhUOFIm9-4BdbAhVSp3z1XwAOdOL6BLHw5-_CM2V3WD3LbkHMSqAHbeNavxGd_YTAqgylDkYAF0LGr3Flzs=', start_index=18107)
Annotation(end_index=18182, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHibQa6UtTK4GM-Dbymqc7K-svNiLzajZk0m5FyFnQq4xhOdkPQ_PIFgKM1DjyA21vf0UBXarcIyD1JD98ZArl4be0MY-8za0goXZgCoMBhdcQUbkESbtmdXq8noWmCWYi2l--CFSdq', start_index=18173)
Annotation(end_index=18225, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE91nLTuwbTSekPDvpc2bH_NfgW0f4sSbmTsVZ6cBrBWy8phUsNJkK57Wu5U87kIjPfZ-_R-hsQMFD773_Dk2F-HoDx2ZICrW32Gduu8E7U6_giHnRfeFbQKpcDkIMMxYd4ciBRVYYLmjp9G8r7v_1yfPffk9NyHEp4fAg=', start_index=18211)
Annotation(end_index=18225, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYGQeUyspSXf9-ounaDSiIbO2v7FQnbOvARVNqGfDC0eVrRLYZCybSsIN6iVsFN6uJ-P2-5mAwlFOhXydRftjBguVLxYSVVDH7VM-J7uGJsBz4HNfqxZT3FkfqR2Gs2buqDT0w-Ip3', start_index=18211)
Annotation(end_index=18280, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3xAm6qdS2dOvdEEp0vOamRrWhL73iweCrPNfYu1RX_TFR7T2WPKfz7CGEcEHKmdlQGxAd_PoxgrWBLZJeTvsK9TfdgUd7VZuK_6UbPTNUSW8ImxSJf8c5Wv93eAG6wA9csIdxzDiAF7mK8TnMgfUfwomkX0ulGn0SsJ2w3pyHPBvhMt3JiUJw4Xk1-QA7JGsYpTPj2RX8CJh_cbkAeW7W23ow_5qvkgutfA32rJ7zVOSb885BgiiGAfE4gEHSiw==', start_index=18266)
Annotation(end_index=18280, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3Ql1lq_7tMucj9V0nvfl1h-eb264tGylchm8c5IUp5E0xz_pXnbiL4ycneemRqex1pvS1JhYeaAp4QNVxToYFYKnPtITdHQqGc_2AjICiy5oGD-jz4fClSG1YSsCj5m7MrTVL13qIwJVg0EcDcW0MpQ3Yuy1G4lAvbYd2qe5bGMGpZOQqE-8IInmFZXffhYnSABVhU9ajQNbNlw0mWDdbjBr40nVWI0FsIqSmkiwaZlNuyeTlfXy2RJYZMFyiuKXVRpq3vYL1fUBaqw==', start_index=18266)
Annotation(end_index=18333, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFetTpgSMKznQde7SNMlC8Xjjy2HUqBzKHVU6U6-o-THl_b_oAqI8bSC2LrnAfrz3KAaGW3OjkXXd7_MFw5_kpO_u1FPtA7MEulDP6PxfHECrOLrTq2vOFExDXpwt9-2FcNu0VWZQYx_u-G4K1mIEYz9ZQkOV0XlKeIh6JpSaqZstls6xa1Xpjq7KYPgD-2KEF0SUJje1nZG_0_lA8PSwjfrfMbO6JLB4GcUfMsO4VZypUtS0_oiIJYWUUaygkuV95R6WCeg9O7R1BblPI=', start_index=18323)
Annotation(end_index=18388, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3okxJWsGv0GjNFRmhJy40a8je9Z5ywThDEpEaVR-TTdXw0B1hzwTKNI5pUBtwLYLGxcDpObrHouDkS5tDsIqNZ7lckVoFbiSs4EOnQx9kl9J4pSGdjnmS6X60XtEGo7V52mu6V3xPDw==', start_index=18379)
Annotation(end_index=18446, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoeFAbUP468bqBVTX6j2ukO7yhUDzSGoeUEwbCpsOkPG5jD8I-nWIMsXNvA-aB07EOf0VPrPT4EusStKs5uSfFO6Y8Jl-6xiflQeLxECTohDjUq7h2F9aIb_LEOKe3sw==', start_index=18432)
Annotation(end_index=18446, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrfTqaR8dRLl4cB4spkRtZUxE1axO9Vy8tBcHkMWNCyu7Sxx2HEYaIf4Hg8zMtaYziDHtf--C4dx4KOBglboy44BNiypolwHx6g9Uywua5JvZILv1_CuX77VBy8eqga06QIoXKePsPF2iDIuewII_IRRL8BZNSp12G1BfSswajCmclcJFZIf0CFtdwENidcv1raHbnRccNiPaCsMw5vqvi3IXP4sTsf_otwL1LDJ-3jBVj', start_index=18432)
Annotation(end_index=18509, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEe6svuks3flrhZrJGhYIHZU5rBBbiTtWBcxKwmDz8bYH8T_Ooc-jWhpBZXrDwuSvVzj3FdJVXAxhD2T1YQlmMLwOY2Qx9uCNLm4ien2jILPyXle4hq4IK7bE0E1PP6ULFx7M8EL7o-Vai3dmk5-TEXSs2wKNU5XV5STHQ=', start_index=18499)

## Sources
