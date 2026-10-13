# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 67397825 | **Time:** 409.89s | **Cost:** $2.20150
--------------------------------------------------------------------------------

# Performance Boundary Determination for Supplier Promotion in Admission Stratification Systems

### Key Points
*   **Contextual Definition:** In supply chain and marketplace management, "admission stratification" refers to the segmentation of suppliers into hierarchical tiers (e.g., Bronze, Silver, Gold or Approved, Preferred, Strategic). "Supplier promotion" is the upward movement across these tiers based on meeting specific criteria.
*   **Boundary Determination Mechanisms:** Performance boundaries are determined using a mix of **absolute thresholds** (fixed KPI targets), **relative benchmarking** (ranking against peers), and **mathematical modeling** (such as Data Envelopment Analysis to identify efficient frontiers).
*   **Key Metrics:** The boundaries are defined by quantitative metrics including **On-Time Delivery (OTD)**, **Defect Rates**, **Cost Competitiveness**, and **Sales Volume**, as well as qualitative factors like innovation and responsiveness.
*   **E-Commerce vs. Traditional B2B:** E-commerce platforms (e.g., Flipkart, AliExpress) typically use automated, rigid performance boundaries based on sales velocity and customer ratings for seller tiering. Traditional B2B procurement uses more complex, multi-criteria scorecards involving risk and strategic value.
*   **Terminology Note:** The term "admission stratification" is also widely used in healthcare to describe patient risk profiling for hospital admission. While distinct, the statistical principles of risk stratification (predictive modeling) share methodological similarities with supplier risk stratification.

---

## 1. Introduction

The determination of performance boundaries for supplier promotion within admission stratification systems is a critical governance mechanism in modern Supply Chain Management (SCM) and electronic marketplaces. Stratification systems serve to categorize suppliers based on their value, risk, and performance, creating a hierarchy that dictates resource allocation, relationship depth, and benefits. "Admission" in this context refers to the entry into a specific tier, while "promotion" denotes the graduation from a lower tier (e.g., transactional or probationary) to a higher tier (e.g., strategic or preferred).

The "performance boundary" represents the specific cut-off point or threshold that separates these tiers. Determining this boundary is not merely an administrative task but a strategic decision that influences supplier behavior, supply chain resilience, and overall operational efficiency. If boundaries are set too low, the organization dilutes the value of its strategic tier; if set too high, it may alienate capable suppliers and reduce competitive tension.

This report examines the methodologies, metrics, and systemic frameworks used to determine these boundaries. It contrasts the automated, high-volume approaches of e-commerce seller tiering with the qualitative, relationship-heavy approaches of B2B Supplier Relationship Management (SRM).

## 2. Conceptual Framework of Supplier Stratification

Supplier stratification is the process of classifying a supplier base into distinct segments to tailor management strategies appropriate for each segment. This segmentation allows organizations to prioritize resources, focusing intensive management efforts on suppliers that drive the most value or pose the highest risk.

### 2.1 The Hierarchy of Tiers
Most stratification systems follow a pyramidal structure. The performance boundaries act as the "gates" between these levels:
*   **Strategic/Alliance Partners (Top Tier):** Suppliers critical to competitive advantage. Promotion to this level requires crossing boundaries related to innovation contribution, long-term alignment, and financial integration.
*   **Preferred/Key Suppliers (Middle Tier):** Suppliers with high performance and significant spend. The boundary here is often defined by consistent operational excellence (quality, delivery) and cost competitiveness.
*   **Transactional/Approved Suppliers (Base Tier):** The largest volume of suppliers, managed for efficiency. Admission to this tier requires meeting basic compliance and qualification boundaries [cite: 1, 2, 3].

### 2.2 The Concept of the Performance Boundary
A performance boundary is a quantitative or qualitative limit that defines the "efficient frontier" or the minimum acceptable standard for a specific status.
*   **Static Boundaries:** Fixed values (e.g., "98% On-Time Delivery") that remain constant over a defined period.
*   **Dynamic Boundaries:** Relative values based on the performance distribution of the entire supplier pool (e.g., "Top 10% of suppliers by revenue").
*   **The Efficient Frontier:** In advanced economic modeling, specifically Data Envelopment Analysis (DEA), the performance boundary is not a single number but a curve representing the maximum possible output for a given level of input. Suppliers on the curve are "efficient," while those below are not [cite: 4, 5].

## 3. Methodologies for Determining Performance Boundaries

The determination of where to draw the line for supplier promotion involves several methodological approaches, ranging from simple heuristics to complex statistical analyses.

### 3.1 Absolute Threshold Determination (Scorecarding)
The most common method in B2B environments is the **Balanced Scorecard**. Organizations define specific Key Performance Indicators (KPIs) and assign weights to them. The performance boundary is a composite score.
*   **Mechanism:** A supplier receives a score out of 100 based on weighted metrics (e.g., 40% Quality, 30% Delivery, 20% Cost, 10% Innovation).
*   **Boundary Setting:**
    *   *Promotion to Gold:* Score > 90.
    *   *Promotion to Silver:* Score > 80.
    *   *Probation/Demotion:* Score < 70.
*   **Determination Logic:** These boundaries are typically determined by historical performance analysis (e.g., "What score did our best suppliers achieve last year?") and strategic goals (e.g., "We need to raise the bar to 95% to meet customer demands") [cite: 1, 6, 7].

### 3.2 Relative Ranking and Bell Curve Stratification
In competitive marketplaces (e.g., Flipkart, Amazon) or large supply bases, boundaries are determined relatively.
*   **Mechanism:** Suppliers are ranked against each other based on a specific metric, such as sales volume or defect rate.
*   **Boundary Determination:** The boundary is defined by percentiles.
    *   *Tier 1:* Top 5% of sellers.
    *   *Tier 2:* Next 15% of sellers.
*   **Implication:** The absolute performance required to cross the boundary changes constantly. If the peer group improves, the boundary for promotion rises, forcing continuous improvement (a "Red Queen" effect) [cite: 8, 9].

### 3.3 Data Envelopment Analysis (DEA) and Efficient Frontiers
For complex industrial systems, the performance boundary is determined mathematically using **Data Envelopment Analysis (DEA)**.
*   **Methodology:** DEA is a non-parametric method that uses linear programming to construct a "production possibility frontier" or "efficient frontier."
*   **Boundary Definition:** The frontier itself is the boundary. Suppliers located on the frontier have an efficiency score of 1 (or 100%). Suppliers inside the frontier have scores less than 1.
*   **Promotion Criteria:** Promotion might be contingent on moving closer to the frontier (reducing the "slack" variables). This method is particularly useful when comparing suppliers with different mixes of inputs and outputs, as it does not require pre-assigned weights for every metric [cite: 4, 5].

### 3.4 The Matrix Approach (Kraljic Matrix)
Boundaries are also determined by the intersection of two dimensions, typically **Profit Impact** and **Supply Risk**.
*   **Stratification:**
    *   *Strategic:* High Risk / High Profit Impact.
    *   *Bottleneck:* High Risk / Low Profit Impact.
    *   *Leverage:* Low Risk / High Profit Impact.
    *   *Non-Critical:* Low Risk / Low Profit Impact.
*   **Promotion Boundary:** Moving from "Leverage" to "Strategic" involves crossing a boundary of *relationship integration* rather than just operational performance. The determination here is often qualitative, based on the supplier's willingness to enter joint ventures or share intellectual property [cite: 3, 10].

## 4. Key Performance Indicators (KPIs) Defining the Boundaries

The specific metrics used to calculate whether a supplier has crossed a performance boundary vary by industry, but generally fall into four categories.

### 4.1 Operational Efficiency Metrics
These are the "hard" metrics that form the baseline for any admission or promotion.
*   **On-Time Delivery (OTD):** The percentage of orders delivered by the promised date. A typical boundary for "Preferred" status is often >98% [cite: 6, 7].
*   **Quality Defect Rate:** Measured in Parts Per Million (PPM). Promotion boundaries are often set at specific PPM thresholds (e.g., <50 PPM for automotive Tier 1).
*   **Lead Time Variance:** The consistency of delivery times.

### 4.2 Financial and Commercial Metrics
*   **Cost Competitiveness:** Often measured against market benchmarks. A supplier might need to be within 5% of the lowest market price to be eligible for promotion.
*   **Spend Volume:** In e-commerce, "Seller Tiering" is heavily dependent on Gross Merchandise Value (GMV) or number of units sold. For example, Flipkart's Gold tier requires meeting specific sales benchmarks over a 3-month period [cite: 8, 9].
*   **Payment Terms:** Willingness to accept extended payment terms can sometimes be a gatekeeper for admission to preferred tiers.

### 4.3 Risk and Compliance Metrics
*   **Financial Health:** A Z-score or credit rating threshold acts as a hard boundary for admission to the Strategic tier.
*   **Sustainability/ESG:** Increasingly, suppliers must meet specific environmental or social governance scores (e.g., Carbon footprint reduction) to cross the boundary into "Sustainable Supplier" tiers [cite: 11, 12].

### 4.4 Relational and Innovation Metrics
*   **Responsiveness:** Speed of response to RFQs or issues.
*   **Innovation Contribution:** Number of new ideas or patents shared. This is often a "soft" boundary determined by qualitative review from engineering or R&D stakeholders [cite: 10, 13].

## 5. Industry-Specific Systems

### 5.1 E-Commerce Marketplaces (Seller Tiering)
Platforms like Flipkart and AliExpress utilize automated stratification systems where performance boundaries are rigid and transparent.
*   **System:** Flipkart uses a "Seller Tiering" system (Gold, Silver, Bronze).
*   **Determination:** The boundaries are determined by a combination of:
    *   *Tenure:* How long the seller has been active.
    *   *Performance:* Breaches of seller policies, return rates, and cancellation rates.
    *   *Volume:* Number of successful transactions.
*   **Promotion Mechanism:** The system evaluates performance over a set period (e.g., 90 days). If a seller crosses the boundary (e.g., <1% cancellation rate AND >500 units sold), they are automatically promoted. This promotion unlocks benefits like lower shipping fees, faster payments, and better visibility [cite: 8, 9, 14].

### 5.2 Industrial Manufacturing (Strategic Sourcing)
In industries like automotive or aerospace, the boundaries are less automated and more negotiated.
*   **System:** Supplier Relationship Management (SRM) frameworks.
*   **Determination:** Boundaries are determined by cross-functional teams (Procurement, Quality, Engineering).
*   **Promotion Mechanism:** A supplier might meet the operational KPIs (OTD, Quality) but fail to cross the "Strategic" boundary because they lack global footprint or design capabilities. Here, the boundary is multidimensional and strategic [cite: 1, 11, 15].

## 6. The "Admission" Process in Stratification

While "promotion" deals with upward movement, "admission" deals with the initial entry into the system.
*   **Entry Stratification:** When a supplier is first onboarded, they are often placed in a "Probationary" or "New" tier. The boundary for admission to the active supplier list typically involves:
    *   *Legal Compliance:* Tax IDs, insurance, certifications (ISO 9001).
    *   *Financial Vetting:* Solvency checks.
    *   *Capability Audit:* On-site verification of production capacity [cite: 11, 16].
*   **Differentiation from Healthcare:** It is important to note that "admission stratification" is a dominant term in healthcare research, referring to stratifying patients based on their risk of hospital admission (e.g., using the CURB-65 score for pneumonia or CHADS2 for atrial fibrillation) [cite: 17, 18, 19, 20, 21]. In that context, the "performance boundary" is a clinical score (e.g., Score > 2 implies high risk). While the domain is different, the statistical logic—using predictive variables to segment a population into risk tiers—is remarkably similar to supplier risk stratification.

## 7. Challenges in Boundary Determination

### 7.1 Data Quality and Availability
Determining accurate boundaries requires reliable data. If data on "innovation" or "responsiveness" is missing or subjective, the boundary becomes fuzzy, leading to disputes over promotion [cite: 1, 12].

### 7.2 Dynamic Environments
A static boundary can become obsolete quickly. For instance, during a supply chain crisis (like COVID-19), the boundary for "On-Time Delivery" might need to be lowered to reflect global realities, otherwise, no supplier would qualify for the top tier. Conversely, in a surplus market, the boundary might be raised to filter for only the absolute best [cite: 13, 22].

### 7.3 Behavioral Gaming
When boundaries are explicit (e.g., "Sell 100 units to reach Gold"), suppliers may engage in gaming behavior, such as splitting orders or creating fake transactions (brushing) to cross the threshold. E-commerce platforms often have to adjust boundaries or add "integrity" metrics to counter this [cite: 14].

## 8. Conclusion

The determination of performance boundaries for supplier promotion is a complex exercise in balancing quantitative rigor with strategic intent. Whether through the automated algorithms of e-commerce platforms or the nuanced scorecards of industrial procurement, these boundaries define the incentives that drive supplier behavior. Effective systems do not just set arbitrary numbers; they use methodologies like DEA and relative benchmarking to ensure that the boundaries reflect true efficiency and value, thereby fostering a competitive and high-performing supply base.

## References
*   **[cite: 8, 9]** Flipkart Seller Tiering and performance criteria.
*   **[cite: 14]** AliExpress seller tiering and review thresholds.
*   **[cite: 1, 2, 3]** Supplier stratification definitions, criteria, and scorecarding.
*   **[cite: 4, 5]** Data Envelopment Analysis (DEA) and performance boundaries (efficient frontiers).
*   **[cite: 10, 13]** Buyer-supplier interaction, innovation, and relationship value.
*   **[cite: 11, 15]** Supplier handbooks, compliance, and strategic alignment.
*   **[cite: 6, 7, 23]** KPIs for supplier performance evaluation (OTD, Quality, Cost).
*   **[cite: 17, 18, 19]** Healthcare admission stratification (distinction provided).

**Sources:**
1. [inddist.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXnx5WvH-O0b2R3DRnBUr1vwSYxHQ2JAMN6ch6lijL-1P5x9N96sl_tqhPLWehqQ2Cl_h-_zQXXJT94lYmLt8Ymq_jB7z5cJ0LG4FhMCQlMGArHgWcu5NmLjKPQWIGkHuBCy2hr-nNqQmKE4ZUS9q6yyMinZ-yTDfLlnHSi7-x0j9a1v12hiOdAzMEG93TFm_fI5VuW9TCLwZK3HsvJKZJpATOKek=)
2. [strategicsourceror.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRe_QYauKbSAhfRVcTdgla2kwm2qzkdPSDdZeqQ96RTaAruRGtCFXZvaZIJ7ZnVtpeU_kG3mODMhv7-AxoTf57tqym64G3UP177hIBOYora6Fi-rhLcxhOzeGAjyHzlFNFv34D6IuGOoFcBsJoSPXwl7XepfS-M1j0yOxdvUIFX7pGXe8Toe4SOfvJ)
3. [inderscienceonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkIx-cGXXXdTOCDgfiJqOizfvo7poM-Vcghvq0B9RX7X7qWxLA0mo74lJyA-z7ExBg2ijXnzxZpok355vDbcpbAyKGWbLGyKyB6A9Ztv_5b-ui1h7BbSzsq45fqFJfqUiqU3TpAArpX6wtFBRoWcU1UqzMY1zxaVGr)
4. [buscompress.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFannRF2EmHrO5L5kHGRgBxc8YEnR04rB08eCUjtbz_lttqYn5E-OLBAiGpwRipEpqmOCbFBvz0UqYRGhrtZdB8l5Cyd80zZVKfZpZvAReGsuH8fRHnX9iXUjfOMu5odJipv7gEknPyEut0f01trf_eATdvBrOzLDKJEdGrU8d5jxhUlUw6vgQ=)
5. [aip.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxK-c0Ez3kSkDdPROl2F705r8s_ULh0magEDC7rqvmjl-D-KMrZouP9mkMb6wNRoKSRkZDK1F-TijYx-YuY-zRTEJ6nNADD1WX1Q_uRP8_L1xT7ld-c2OzXPjdbjdLegPpMG1jgv4JE906tLSfa__Lo1R5OE5WXXSXI82tcCLKskBoVQDgWP88JxW3ZgCZsYNnES8M0c0d9qKdPBg=)
6. [graphiteconnect.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3EB9l-JdSh8yzuyjb4aN3-VAZqOyTzNVBxJ9EFfY1t3hnLrqdA-UpE_ghhjLklU_q1OXKBklYLjA3jgMwVYfRvcLuXP3524ztuCMrWK1EdaAxPEkrw7sckMiwSwv5sG__Vcr717Aq7JOOyhcQ-pwjgvf9_CFiaHVbRQzu_0P-7H9TGxSV9NMv1GT_yHZSF7TbVB05MA==)
7. [insight7.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1mnBPx_3HADRK6LgS9uYvemXkcgE3z1wMzifQhCduXOK6DFS-unkMB2B2aLGRn_5RCiInL8YEU07CFedPBNkuJc02IN4GY2ADKqemkOolcw4yJMI37AkuqZEKbVa2H6KhBTwntp3QYMEfd-Z0sos0FFu__m-rvgQ=)
8. [quora.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAgQr1uWBZXt5dONEN26n1So6_JkX3BzGP7kmDf9WNiPuRNfEkzKLQBJF4Y-EIutIsJOz0dfRDJ7VFcTAbJGgdSZXqoDwfvqutj7HmQaoq3F991zJbJ1J4sRoCfroNPD0WHLvMCQzwnFFwPKT3bdxrNzKhjZC1hrKHCpx08vJX3KXyibiEnyuhPr8jc_157N5avDKcglRpCIYxnqKYJPN8Z7JEdQZYUg==)
9. [quora.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaIhC_FVJnPmeKxW_Re03buVaFCWJbgv5UIJ4qIDoZi8Q8AQN5kxoViHqnd1rVKf-Z9nDVh2DarrLTyt-O5Q1YBaQOtrqdbqgeS0KVAZ68zuXm7327fx6XGBa9RVvU7rjrsgO4pdtubgh0axAK5qLaoNVzMTwuShJubl41L7cj4_XcjZaqcUb5cIb1FI6dc56983safQW0Wx94OYJ4DqI=)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFigUB_F9JDGZz21DhPXcYEz1i211qnOC9I3MLhPrdUZh2vfvf4udd9lO1i3y8Bl8lguknzO8_yRk6egWPs5bYaCyGclm_qQCgAmL8fvlaVlm0rw7BdNo_TpsxhapTHSE29mma8BC7YyVxeHX4QuIMwfgIIdJy3P8J-6M5RS97FedXC2DD-nH77kMJyXjVwb7OvVbhdC2k1gFz_PUaRqhYSWu0_fh0aCTG_z3tbxeU_gOA2F18d_aKmTk9lDRcsmlmImfkNfFYW6t7v9LE53Ld-klCaRvM=)
11. [abb.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFmYu-N4AA1ixFc5fezBqB5x0zq6JYAaKoK0iiKuolI0k3v-9BjS8c0kS-77ClHh_V_FMdIXqhin9sSpjeuUplsWTF48AU1dKBosdWzwFkNM3nTTQMRVzors7EGvJhrC-dDOipwxR9rv_iVbvcvOtYV5z8xwftmWLyvycgSdUFlIrkRA-i7IfP-0a6BOmTlg0xF4o-9R6oUneD7gHbXQ==)
12. [sustainability-directory.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFu265fCEkhmD5MwuZyGc-89wAbEv9k03i8stZUhR135WNqhDa9uvmFuGFq1x3BL8omNBSOn2V9O5-Z2XUW0LVkGChhJWJd3-InxzNS-ihvm1LXnxbQWL43Fr72cEsSfuFfgp_193mpUD_U6LpJmZ3wiyLGbbbv7G_JPXiIa9kMrNE=)
13. [emerald.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP129u8Dd_t6LQBcAS2t-g9k2bPXQeQonp2SwXFU5du7X1V7Uy1YFLSiVFd43aNbJLmMuOk2w2ulC05MjVI1O0rIBew1BHwxb3Cjpkst-oALpZfA-tF31ZqbhbO0x0RI8fol5EemhxyLV9K-6hc9YUIeUxGiMnW5UNGoEyHYzCm2CM5FEEl6axpid4T3-uF82TYUfkyhOIwhoY1aI=)
14. [aliexpress.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhRC8Zphmp8rMQmYv8hM9kxWHVrNVVPp4KjDwuucui8OxyG85fdlkJ-vTcC-F-6vCoHeufGt8vMbpa4nIoQSMckkGAqIvDWQN-oA9dD_XQdqNMNb6xI8_D1Xa6_wSCAC0Yrsnu4LgPS3WIlhFmHuaGXU7M4lMUeA1PPK4=)
15. [scribd.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSjbReuzQdJ5gqjVNu0j8mMmo1OdjwZ1hTwi2Pv4aZ-bxu3vrasVQzXIAOos13T22dZesSeWJ2NGP_ODgSWKOhsX_3wtOgmK9l9U7WFPq9f6Rn4qhlDP9rYM5dYDn0O19EHR86UYNqLR7Gi20oVHzdqif7pcsxihcospr-xvR5RftH4wSxRtH2jbnbC8Eg4WAsG0T9YXjvXU1uXFbD0-3QbFswPSnsp7r8QRapkam3i0yXodTuejCwRNRORZx85vJ2)
16. [ivalua.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0t7H9X8vq5GDD1VKe6KW34s_ZvrUTASwcEHrtDObb3Q8rdiFm9L1uRAWk7fyTXu1sV02lILmFVgxIZEyMxHZqUl-7fIZbSeYa2NYWdSmrHoow6iQSrRQnK-GQy-iOwuNgxsF_JaiVu2IwXrmEy57-zd0KJwAswBYtHRu5q714zqg1wTSYRCCflyddC9U=)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcA6PnLaE3_vE2XVQQVTkHgHJISzkMMtGRoKitEpTkJfLmem6cLrStv485W61gvj5jert1AJLSG90Mek6NCgLQZo8azQsKrz7hwqU58vNiJhfvQSlnyB495SGbwzstXoY3pm3-Ca230-ivoDFIMyE94wDSrHogeI-y9nVXmeLVRMDVhT2dCJgdlIDXDbUsEI1tmcAGwFko4QoEw6imEup2bBPzAgK1vTSAaAUKJZSSKepoO9nlMsGtE53HGUeaKlXLbORUo13I_94hyfNT-3Nr6FgVjg==)
18. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHh81-MMoA2iSJU-glTCbr7ioFHvScq_CX5iJfdqfrzGnWygukJtI-VBhrTCCZcuKmbTmGT6CVe0G1kSEO8Mthg295HD-FL6XCmbbJN20GHpRF7XXTJAb64G2ufFnaUSFiy5N8irK57)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1coWbRS_7YliaUqEXZWDFKeYhngxzpybx2RNJzJ1m6lpozj_HGeLdGwvGAXfrL7fmlLrDFWhiqSDiV7LXsp6YCNjnAJgiJF0YhzOQ5_JiJ2hokXjkur2FUp578ppGYxUBzHPOFX8w2zQP_dgONz5L8UprioILix8rKj8xniiM1eh-Wfp8rZ8idH4t8yYMt571LrBIDkwauoRO_KeFdZI9jH3ZIszWDK44lmZr_72fXKEFYyWAopc7CRa4SeBzPkbs0xnRwi2wP4N8_P71gPCkRYT5-OkMdV-Wa95Wf7HXU7xxV8ZuEOwr5XOsiQg6fqUdyzxweFOSwfws)
20. [signavitae.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfNZJKRtSDKOLbxsH1nK3mCflbtllCi6dMrruy76ShYtFve0_pl9CgYuGxGrTt422zAIRnJTmlwOPtvqTswwUxT6Dv01W4sPQJwQ4XtSYgAbsDm4OCJzyefUX3IJoRdxIb1RMZAIbtsZDnoTcaZjMMYg==)
21. [ahajournals.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERwxNE6fyl-_j5AWGqnuINNRsZcioBfXMPqBlBd4eHkqAwHbZ4TIxX8qOtU8syVq0U-lqlr7yceAMz8FEfQJhwT3NaPq8VS6qsDuyCBSPDHnDDXMBBisBkccRmnEpXapzHF4nLdu9Yccnn9EJYSo6HKWQK4nK-IQ==)
22. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSNx6xWgP-ang_8SvGAoDEp25qauSkq5y0TCTDJwnHmaAWzr8ecBFXq0qEHBZ9IgWyPwrYNhwz-xV7swUeY53hhYvGYs1nln1vi1msPO_RCDLuijkYdpUTfaY6a7rDWMOWFyd_vVzIoYRosQg8u5b4nFcPYVD0tWTMAtID2-Fohm_ayXEMmdGUgMFsqD-lkRbSFv7adbgQa6tOXT7KnjSAa15N-Sumn0NyVYxvdQy2xDR6lgGE)
23. [procol.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsJXOsy77nct0K5g0hek3-42vDgAqdf9RFYo17XwIYY4W54ttUpyWSigZV3ui80SCIvipFaeAJV1OCubuS5qo7YdjQrKCIzJWVrPFbgtChvaoW6hMzwRO8OYAiW288tr2auszLoOuufBi6vYF0p3lJ5A==)


## Annotations
Annotation(end_index=4196, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRe_QYauKbSAhfRVcTdgla2kwm2qzkdPSDdZeqQ96RTaAruRGtCFXZvaZIJ7ZnVtpeU_kG3mODMhv7-AxoTf57tqym64G3UP177hIBOYora6Fi-rhLcxhOzeGAjyHzlFNFv34D6IuGOoFcBsJoSPXwl7XepfS-M1j0yOxdvUIFX7pGXe8Toe4SOfvJ', start_index=4181)
Annotation(end_index=4196, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXnx5WvH-O0b2R3DRnBUr1vwSYxHQ2JAMN6ch6lijL-1P5x9N96sl_tqhPLWehqQ2Cl_h-_zQXXJT94lYmLt8Ymq_jB7z5cJ0LG4FhMCQlMGArHgWcu5NmLjKPQWIGkHuBCy2hr-nNqQmKE4ZUS9q6yyMinZ-yTDfLlnHSi7-x0j9a1v12hiOdAzMEG93TFm_fI5VuW9TCLwZK3HsvJKZJpATOKek=', start_index=4181)
Annotation(end_index=4196, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkIx-cGXXXdTOCDgfiJqOizfvo7poM-Vcghvq0B9RX7X7qWxLA0mo74lJyA-z7ExBg2ijXnzxZpok355vDbcpbAyKGWbLGyKyB6A9Ztv_5b-ui1h7BbSzsq45fqFJfqUiqU3TpAArpX6wtFBRoWcU1UqzMY1zxaVGr', start_index=4181)
Annotation(end_index=4989, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFannRF2EmHrO5L5kHGRgBxc8YEnR04rB08eCUjtbz_lttqYn5E-OLBAiGpwRipEpqmOCbFBvz0UqYRGhrtZdB8l5Cyd80zZVKfZpZvAReGsuH8fRHnX9iXUjfOMu5odJipv7gEknPyEut0f01trf_eATdvBrOzLDKJEdGrU8d5jxhUlUw6vgQ=', start_index=4977)
Annotation(end_index=4989, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxK-c0Ez3kSkDdPROl2F705r8s_ULh0magEDC7rqvmjl-D-KMrZouP9mkMb6wNRoKSRkZDK1F-TijYx-YuY-zRTEJ6nNADD1WX1Q_uRP8_L1xT7ld-c2OzXPjdbjdLegPpMG1jgv4JE906tLSfa__Lo1R5OE5WXXSXI82tcCLKskBoVQDgWP88JxW3ZgCZsYNnES8M0c0d9qKdPBg=', start_index=4977)
Annotation(end_index=6065, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1mnBPx_3HADRK6LgS9uYvemXkcgE3z1wMzifQhCduXOK6DFS-unkMB2B2aLGRn_5RCiInL8YEU07CFedPBNkuJc02IN4GY2ADKqemkOolcw4yJMI37AkuqZEKbVa2H6KhBTwntp3QYMEfd-Z0sos0FFu__m-rvgQ=', start_index=6050)
Annotation(end_index=6065, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3EB9l-JdSh8yzuyjb4aN3-VAZqOyTzNVBxJ9EFfY1t3hnLrqdA-UpE_ghhjLklU_q1OXKBklYLjA3jgMwVYfRvcLuXP3524ztuCMrWK1EdaAxPEkrw7sckMiwSwv5sG__Vcr717Aq7JOOyhcQ-pwjgvf9_CFiaHVbRQzu_0P-7H9TGxSV9NMv1GT_yHZSF7TbVB05MA==', start_index=6050)
Annotation(end_index=6065, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXnx5WvH-O0b2R3DRnBUr1vwSYxHQ2JAMN6ch6lijL-1P5x9N96sl_tqhPLWehqQ2Cl_h-_zQXXJT94lYmLt8Ymq_jB7z5cJ0LG4FhMCQlMGArHgWcu5NmLjKPQWIGkHuBCy2hr-nNqQmKE4ZUS9q6yyMinZ-yTDfLlnHSi7-x0j9a1v12hiOdAzMEG93TFm_fI5VuW9TCLwZK3HsvJKZJpATOKek=', start_index=6050)
Annotation(end_index=6734, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAgQr1uWBZXt5dONEN26n1So6_JkX3BzGP7kmDf9WNiPuRNfEkzKLQBJF4Y-EIutIsJOz0dfRDJ7VFcTAbJGgdSZXqoDwfvqutj7HmQaoq3F991zJbJ1J4sRoCfroNPD0WHLvMCQzwnFFwPKT3bdxrNzKhjZC1hrKHCpx08vJX3KXyibiEnyuhPr8jc_157N5avDKcglRpCIYxnqKYJPN8Z7JEdQZYUg==', start_index=6722)
Annotation(end_index=6734, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaIhC_FVJnPmeKxW_Re03buVaFCWJbgv5UIJ4qIDoZi8Q8AQN5kxoViHqnd1rVKf-Z9nDVh2DarrLTyt-O5Q1YBaQOtrqdbqgeS0KVAZ68zuXm7327fx6XGBa9RVvU7rjrsgO4pdtubgh0axAK5qLaoNVzMTwuShJubl41L7cj4_XcjZaqcUb5cIb1FI6dc56983safQW0Wx94OYJ4DqI=', start_index=6722)
Annotation(end_index=7583, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFannRF2EmHrO5L5kHGRgBxc8YEnR04rB08eCUjtbz_lttqYn5E-OLBAiGpwRipEpqmOCbFBvz0UqYRGhrtZdB8l5Cyd80zZVKfZpZvAReGsuH8fRHnX9iXUjfOMu5odJipv7gEknPyEut0f01trf_eATdvBrOzLDKJEdGrU8d5jxhUlUw6vgQ=', start_index=7571)
Annotation(end_index=7583, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxK-c0Ez3kSkDdPROl2F705r8s_ULh0magEDC7rqvmjl-D-KMrZouP9mkMb6wNRoKSRkZDK1F-TijYx-YuY-zRTEJ6nNADD1WX1Q_uRP8_L1xT7ld-c2OzXPjdbjdLegPpMG1jgv4JE906tLSfa__Lo1R5OE5WXXSXI82tcCLKskBoVQDgWP88JxW3ZgCZsYNnES8M0c0d9qKdPBg=', start_index=7571)
Annotation(end_index=8301, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFigUB_F9JDGZz21DhPXcYEz1i211qnOC9I3MLhPrdUZh2vfvf4udd9lO1i3y8Bl8lguknzO8_yRk6egWPs5bYaCyGclm_qQCgAmL8fvlaVlm0rw7BdNo_TpsxhapTHSE29mma8BC7YyVxeHX4QuIMwfgIIdJy3P8J-6M5RS97FedXC2DD-nH77kMJyXjVwb7OvVbhdC2k1gFz_PUaRqhYSWu0_fh0aCTG_z3tbxeU_gOA2F18d_aKmTk9lDRcsmlmImfkNfFYW6t7v9LE53Ld-klCaRvM=', start_index=8288)
Annotation(end_index=8301, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkIx-cGXXXdTOCDgfiJqOizfvo7poM-Vcghvq0B9RX7X7qWxLA0mo74lJyA-z7ExBg2ijXnzxZpok355vDbcpbAyKGWbLGyKyB6A9Ztv_5b-ui1h7BbSzsq45fqFJfqUiqU3TpAArpX6wtFBRoWcU1UqzMY1zxaVGr', start_index=8288)
Annotation(end_index=8802, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1mnBPx_3HADRK6LgS9uYvemXkcgE3z1wMzifQhCduXOK6DFS-unkMB2B2aLGRn_5RCiInL8YEU07CFedPBNkuJc02IN4GY2ADKqemkOolcw4yJMI37AkuqZEKbVa2H6KhBTwntp3QYMEfd-Z0sos0FFu__m-rvgQ=', start_index=8790)
Annotation(end_index=8802, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3EB9l-JdSh8yzuyjb4aN3-VAZqOyTzNVBxJ9EFfY1t3hnLrqdA-UpE_ghhjLklU_q1OXKBklYLjA3jgMwVYfRvcLuXP3524ztuCMrWK1EdaAxPEkrw7sckMiwSwv5sG__Vcr717Aq7JOOyhcQ-pwjgvf9_CFiaHVbRQzu_0P-7H9TGxSV9NMv1GT_yHZSF7TbVB05MA==', start_index=8790)
Annotation(end_index=9487, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAgQr1uWBZXt5dONEN26n1So6_JkX3BzGP7kmDf9WNiPuRNfEkzKLQBJF4Y-EIutIsJOz0dfRDJ7VFcTAbJGgdSZXqoDwfvqutj7HmQaoq3F991zJbJ1J4sRoCfroNPD0WHLvMCQzwnFFwPKT3bdxrNzKhjZC1hrKHCpx08vJX3KXyibiEnyuhPr8jc_157N5avDKcglRpCIYxnqKYJPN8Z7JEdQZYUg==', start_index=9475)
Annotation(end_index=9487, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaIhC_FVJnPmeKxW_Re03buVaFCWJbgv5UIJ4qIDoZi8Q8AQN5kxoViHqnd1rVKf-Z9nDVh2DarrLTyt-O5Q1YBaQOtrqdbqgeS0KVAZ68zuXm7327fx6XGBa9RVvU7rjrsgO4pdtubgh0axAK5qLaoNVzMTwuShJubl41L7cj4_XcjZaqcUb5cIb1FI6dc56983safQW0Wx94OYJ4DqI=', start_index=9475)
Annotation(end_index=10000, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFmYu-N4AA1ixFc5fezBqB5x0zq6JYAaKoK0iiKuolI0k3v-9BjS8c0kS-77ClHh_V_FMdIXqhin9sSpjeuUplsWTF48AU1dKBosdWzwFkNM3nTTQMRVzors7EGvJhrC-dDOipwxR9rv_iVbvcvOtYV5z8xwftmWLyvycgSdUFlIrkRA-i7IfP-0a6BOmTlg0xF4o-9R6oUneD7gHbXQ==', start_index=9986)
Annotation(end_index=10000, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFu265fCEkhmD5MwuZyGc-89wAbEv9k03i8stZUhR135WNqhDa9uvmFuGFq1x3BL8omNBSOn2V9O5-Z2XUW0LVkGChhJWJd3-InxzNS-ihvm1LXnxbQWL43Fr72cEsSfuFfgp_193mpUD_U6LpJmZ3wiyLGbbbv7G_JPXiIa9kMrNE=', start_index=9986)
Annotation(end_index=10294, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFigUB_F9JDGZz21DhPXcYEz1i211qnOC9I3MLhPrdUZh2vfvf4udd9lO1i3y8Bl8lguknzO8_yRk6egWPs5bYaCyGclm_qQCgAmL8fvlaVlm0rw7BdNo_TpsxhapTHSE29mma8BC7YyVxeHX4QuIMwfgIIdJy3P8J-6M5RS97FedXC2DD-nH77kMJyXjVwb7OvVbhdC2k1gFz_PUaRqhYSWu0_fh0aCTG_z3tbxeU_gOA2F18d_aKmTk9lDRcsmlmImfkNfFYW6t7v9LE53Ld-klCaRvM=', start_index=10280)
Annotation(end_index=10294, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP129u8Dd_t6LQBcAS2t-g9k2bPXQeQonp2SwXFU5du7X1V7Uy1YFLSiVFd43aNbJLmMuOk2w2ulC05MjVI1O0rIBew1BHwxb3Cjpkst-oALpZfA-tF31ZqbhbO0x0RI8fol5EemhxyLV9K-6hc9YUIeUxGiMnW5UNGoEyHYzCm2CM5FEEl6axpid4T3-uF82TYUfkyhOIwhoY1aI=', start_index=10280)
Annotation(end_index=11194, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhRC8Zphmp8rMQmYv8hM9kxWHVrNVVPp4KjDwuucui8OxyG85fdlkJ-vTcC-F-6vCoHeufGt8vMbpa4nIoQSMckkGAqIvDWQN-oA9dD_XQdqNMNb6xI8_D1Xa6_wSCAC0Yrsnu4LgPS3WIlhFmHuaGXU7M4lMUeA1PPK4=', start_index=11178)
Annotation(end_index=11194, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAgQr1uWBZXt5dONEN26n1So6_JkX3BzGP7kmDf9WNiPuRNfEkzKLQBJF4Y-EIutIsJOz0dfRDJ7VFcTAbJGgdSZXqoDwfvqutj7HmQaoq3F991zJbJ1J4sRoCfroNPD0WHLvMCQzwnFFwPKT3bdxrNzKhjZC1hrKHCpx08vJX3KXyibiEnyuhPr8jc_157N5avDKcglRpCIYxnqKYJPN8Z7JEdQZYUg==', start_index=11178)
Annotation(end_index=11194, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaIhC_FVJnPmeKxW_Re03buVaFCWJbgv5UIJ4qIDoZi8Q8AQN5kxoViHqnd1rVKf-Z9nDVh2DarrLTyt-O5Q1YBaQOtrqdbqgeS0KVAZ68zuXm7327fx6XGBa9RVvU7rjrsgO4pdtubgh0axAK5qLaoNVzMTwuShJubl41L7cj4_XcjZaqcUb5cIb1FI6dc56983safQW0Wx94OYJ4DqI=', start_index=11178)
Annotation(end_index=11788, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFmYu-N4AA1ixFc5fezBqB5x0zq6JYAaKoK0iiKuolI0k3v-9BjS8c0kS-77ClHh_V_FMdIXqhin9sSpjeuUplsWTF48AU1dKBosdWzwFkNM3nTTQMRVzors7EGvJhrC-dDOipwxR9rv_iVbvcvOtYV5z8xwftmWLyvycgSdUFlIrkRA-i7IfP-0a6BOmTlg0xF4o-9R6oUneD7gHbXQ==', start_index=11771)
Annotation(end_index=11788, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSjbReuzQdJ5gqjVNu0j8mMmo1OdjwZ1hTwi2Pv4aZ-bxu3vrasVQzXIAOos13T22dZesSeWJ2NGP_ODgSWKOhsX_3wtOgmK9l9U7WFPq9f6Rn4qhlDP9rYM5dYDn0O19EHR86UYNqLR7Gi20oVHzdqif7pcsxihcospr-xvR5RftH4wSxRtH2jbnbC8Eg4WAsG0T9YXjvXU1uXFbD0-3QbFswPSnsp7r8QRapkam3i0yXodTuejCwRNRORZx85vJ2', start_index=11771)
Annotation(end_index=11788, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXnx5WvH-O0b2R3DRnBUr1vwSYxHQ2JAMN6ch6lijL-1P5x9N96sl_tqhPLWehqQ2Cl_h-_zQXXJT94lYmLt8Ymq_jB7z5cJ0LG4FhMCQlMGArHgWcu5NmLjKPQWIGkHuBCy2hr-nNqQmKE4ZUS9q6yyMinZ-yTDfLlnHSi7-x0j9a1v12hiOdAzMEG93TFm_fI5VuW9TCLwZK3HsvJKZJpATOKek=', start_index=11771)
Annotation(end_index=12349, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFmYu-N4AA1ixFc5fezBqB5x0zq6JYAaKoK0iiKuolI0k3v-9BjS8c0kS-77ClHh_V_FMdIXqhin9sSpjeuUplsWTF48AU1dKBosdWzwFkNM3nTTQMRVzors7EGvJhrC-dDOipwxR9rv_iVbvcvOtYV5z8xwftmWLyvycgSdUFlIrkRA-i7IfP-0a6BOmTlg0xF4o-9R6oUneD7gHbXQ==', start_index=12335)
Annotation(end_index=12349, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0t7H9X8vq5GDD1VKe6KW34s_ZvrUTASwcEHrtDObb3Q8rdiFm9L1uRAWk7fyTXu1sV02lILmFVgxIZEyMxHZqUl-7fIZbSeYa2NYWdSmrHoow6iQSrRQnK-GQy-iOwuNgxsF_JaiVu2IwXrmEy57-zd0KJwAswBYtHRu5q714zqg1wTSYRCCflyddC9U=', start_index=12335)
Annotation(end_index=12673, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1coWbRS_7YliaUqEXZWDFKeYhngxzpybx2RNJzJ1m6lpozj_HGeLdGwvGAXfrL7fmlLrDFWhiqSDiV7LXsp6YCNjnAJgiJF0YhzOQ5_JiJ2hokXjkur2FUp578ppGYxUBzHPOFX8w2zQP_dgONz5L8UprioILix8rKj8xniiM1eh-Wfp8rZ8idH4t8yYMt571LrBIDkwauoRO_KeFdZI9jH3ZIszWDK44lmZr_72fXKEFYyWAopc7CRa4SeBzPkbs0xnRwi2wP4N8_P71gPCkRYT5-OkMdV-Wa95Wf7HXU7xxV8ZuEOwr5XOsiQg6fqUdyzxweFOSwfws', start_index=12647)
Annotation(end_index=12673, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERwxNE6fyl-_j5AWGqnuINNRsZcioBfXMPqBlBd4eHkqAwHbZ4TIxX8qOtU8syVq0U-lqlr7yceAMz8FEfQJhwT3NaPq8VS6qsDuyCBSPDHnDDXMBBisBkccRmnEpXapzHF4nLdu9Yccnn9EJYSo6HKWQK4nK-IQ==', start_index=12647)
Annotation(end_index=12673, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcA6PnLaE3_vE2XVQQVTkHgHJISzkMMtGRoKitEpTkJfLmem6cLrStv485W61gvj5jert1AJLSG90Mek6NCgLQZo8azQsKrz7hwqU58vNiJhfvQSlnyB495SGbwzstXoY3pm3-Ca230-ivoDFIMyE94wDSrHogeI-y9nVXmeLVRMDVhT2dCJgdlIDXDbUsEI1tmcAGwFko4QoEw6imEup2bBPzAgK1vTSAaAUKJZSSKepoO9nlMsGtE53HGUeaKlXLbORUo13I_94hyfNT-3Nr6FgVjg==', start_index=12647)
Annotation(end_index=12673, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfNZJKRtSDKOLbxsH1nK3mCflbtllCi6dMrruy76ShYtFve0_pl9CgYuGxGrTt422zAIRnJTmlwOPtvqTswwUxT6Dv01W4sPQJwQ4XtSYgAbsDm4OCJzyefUX3IJoRdxIb1RMZAIbtsZDnoTcaZjMMYg==', start_index=12647)
Annotation(end_index=12673, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHh81-MMoA2iSJU-glTCbr7ioFHvScq_CX5iJfdqfrzGnWygukJtI-VBhrTCCZcuKmbTmGT6CVe0G1kSEO8Mthg295HD-FL6XCmbbJN20GHpRF7XXTJAb64G2ufFnaUSFiy5N8irK57', start_index=12647)
Annotation(end_index=13240, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFu265fCEkhmD5MwuZyGc-89wAbEv9k03i8stZUhR135WNqhDa9uvmFuGFq1x3BL8omNBSOn2V9O5-Z2XUW0LVkGChhJWJd3-InxzNS-ihvm1LXnxbQWL43Fr72cEsSfuFfgp_193mpUD_U6LpJmZ3wiyLGbbbv7G_JPXiIa9kMrNE=', start_index=13227)
Annotation(end_index=13240, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXnx5WvH-O0b2R3DRnBUr1vwSYxHQ2JAMN6ch6lijL-1P5x9N96sl_tqhPLWehqQ2Cl_h-_zQXXJT94lYmLt8Ymq_jB7z5cJ0LG4FhMCQlMGArHgWcu5NmLjKPQWIGkHuBCy2hr-nNqQmKE4ZUS9q6yyMinZ-yTDfLlnHSi7-x0j9a1v12hiOdAzMEG93TFm_fI5VuW9TCLwZK3HsvJKZJpATOKek=', start_index=13227)
Annotation(end_index=13637, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP129u8Dd_t6LQBcAS2t-g9k2bPXQeQonp2SwXFU5du7X1V7Uy1YFLSiVFd43aNbJLmMuOk2w2ulC05MjVI1O0rIBew1BHwxb3Cjpkst-oALpZfA-tF31ZqbhbO0x0RI8fol5EemhxyLV9K-6hc9YUIeUxGiMnW5UNGoEyHYzCm2CM5FEEl6axpid4T3-uF82TYUfkyhOIwhoY1aI=', start_index=13623)
Annotation(end_index=13637, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSNx6xWgP-ang_8SvGAoDEp25qauSkq5y0TCTDJwnHmaAWzr8ecBFXq0qEHBZ9IgWyPwrYNhwz-xV7swUeY53hhYvGYs1nln1vi1msPO_RCDLuijkYdpUTfaY6a7rDWMOWFyd_vVzIoYRosQg8u5b4nFcPYVD0tWTMAtID2-Fohm_ayXEMmdGUgMFsqD-lkRbSFv7adbgQa6tOXT7KnjSAa15N-Sumn0NyVYxvdQy2xDR6lgGE', start_index=13623)
Annotation(end_index=13972, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhRC8Zphmp8rMQmYv8hM9kxWHVrNVVPp4KjDwuucui8OxyG85fdlkJ-vTcC-F-6vCoHeufGt8vMbpa4nIoQSMckkGAqIvDWQN-oA9dD_XQdqNMNb6xI8_D1Xa6_wSCAC0Yrsnu4LgPS3WIlhFmHuaGXU7M4lMUeA1PPK4=', start_index=13962)
Annotation(end_index=14598, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAgQr1uWBZXt5dONEN26n1So6_JkX3BzGP7kmDf9WNiPuRNfEkzKLQBJF4Y-EIutIsJOz0dfRDJ7VFcTAbJGgdSZXqoDwfvqutj7HmQaoq3F991zJbJ1J4sRoCfroNPD0WHLvMCQzwnFFwPKT3bdxrNzKhjZC1hrKHCpx08vJX3KXyibiEnyuhPr8jc_157N5avDKcglRpCIYxnqKYJPN8Z7JEdQZYUg==', start_index=14586)
Annotation(end_index=14598, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHaIhC_FVJnPmeKxW_Re03buVaFCWJbgv5UIJ4qIDoZi8Q8AQN5kxoViHqnd1rVKf-Z9nDVh2DarrLTyt-O5Q1YBaQOtrqdbqgeS0KVAZ68zuXm7327fx6XGBa9RVvU7rjrsgO4pdtubgh0axAK5qLaoNVzMTwuShJubl41L7cj4_XcjZaqcUb5cIb1FI6dc56983safQW0Wx94OYJ4DqI=', start_index=14586)
Annotation(end_index=14667, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEhRC8Zphmp8rMQmYv8hM9kxWHVrNVVPp4KjDwuucui8OxyG85fdlkJ-vTcC-F-6vCoHeufGt8vMbpa4nIoQSMckkGAqIvDWQN-oA9dD_XQdqNMNb6xI8_D1Xa6_wSCAC0Yrsnu4LgPS3WIlhFmHuaGXU7M4lMUeA1PPK4=', start_index=14657)
Annotation(end_index=14740, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGRe_QYauKbSAhfRVcTdgla2kwm2qzkdPSDdZeqQ96RTaAruRGtCFXZvaZIJ7ZnVtpeU_kG3mODMhv7-AxoTf57tqym64G3UP177hIBOYora6Fi-rhLcxhOzeGAjyHzlFNFv34D6IuGOoFcBsJoSPXwl7XepfS-M1j0yOxdvUIFX7pGXe8Toe4SOfvJ', start_index=14725)
Annotation(end_index=14740, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXnx5WvH-O0b2R3DRnBUr1vwSYxHQ2JAMN6ch6lijL-1P5x9N96sl_tqhPLWehqQ2Cl_h-_zQXXJT94lYmLt8Ymq_jB7z5cJ0LG4FhMCQlMGArHgWcu5NmLjKPQWIGkHuBCy2hr-nNqQmKE4ZUS9q6yyMinZ-yTDfLlnHSi7-x0j9a1v12hiOdAzMEG93TFm_fI5VuW9TCLwZK3HsvJKZJpATOKek=', start_index=14725)
Annotation(end_index=14740, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkIx-cGXXXdTOCDgfiJqOizfvo7poM-Vcghvq0B9RX7X7qWxLA0mo74lJyA-z7ExBg2ijXnzxZpok355vDbcpbAyKGWbLGyKyB6A9Ztv_5b-ui1h7BbSzsq45fqFJfqUiqU3TpAArpX6wtFBRoWcU1UqzMY1zxaVGr', start_index=14725)
Annotation(end_index=14826, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFannRF2EmHrO5L5kHGRgBxc8YEnR04rB08eCUjtbz_lttqYn5E-OLBAiGpwRipEpqmOCbFBvz0UqYRGhrtZdB8l5Cyd80zZVKfZpZvAReGsuH8fRHnX9iXUjfOMu5odJipv7gEknPyEut0f01trf_eATdvBrOzLDKJEdGrU8d5jxhUlUw6vgQ=', start_index=14814)
Annotation(end_index=14826, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxK-c0Ez3kSkDdPROl2F705r8s_ULh0magEDC7rqvmjl-D-KMrZouP9mkMb6wNRoKSRkZDK1F-TijYx-YuY-zRTEJ6nNADD1WX1Q_uRP8_L1xT7ld-c2OzXPjdbjdLegPpMG1jgv4JE906tLSfa__Lo1R5OE5WXXSXI82tcCLKskBoVQDgWP88JxW3ZgCZsYNnES8M0c0d9qKdPBg=', start_index=14814)
Annotation(end_index=14931, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFigUB_F9JDGZz21DhPXcYEz1i211qnOC9I3MLhPrdUZh2vfvf4udd9lO1i3y8Bl8lguknzO8_yRk6egWPs5bYaCyGclm_qQCgAmL8fvlaVlm0rw7BdNo_TpsxhapTHSE29mma8BC7YyVxeHX4QuIMwfgIIdJy3P8J-6M5RS97FedXC2DD-nH77kMJyXjVwb7OvVbhdC2k1gFz_PUaRqhYSWu0_fh0aCTG_z3tbxeU_gOA2F18d_aKmTk9lDRcsmlmImfkNfFYW6t7v9LE53Ld-klCaRvM=', start_index=14917)
Annotation(end_index=14931, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGP129u8Dd_t6LQBcAS2t-g9k2bPXQeQonp2SwXFU5du7X1V7Uy1YFLSiVFd43aNbJLmMuOk2w2ulC05MjVI1O0rIBew1BHwxb3Cjpkst-oALpZfA-tF31ZqbhbO0x0RI8fol5EemhxyLV9K-6hc9YUIeUxGiMnW5UNGoEyHYzCm2CM5FEEl6axpid4T3-uF82TYUfkyhOIwhoY1aI=', start_index=14917)
Annotation(end_index=15018, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFmYu-N4AA1ixFc5fezBqB5x0zq6JYAaKoK0iiKuolI0k3v-9BjS8c0kS-77ClHh_V_FMdIXqhin9sSpjeuUplsWTF48AU1dKBosdWzwFkNM3nTTQMRVzors7EGvJhrC-dDOipwxR9rv_iVbvcvOtYV5z8xwftmWLyvycgSdUFlIrkRA-i7IfP-0a6BOmTlg0xF4o-9R6oUneD7gHbXQ==', start_index=15004)
Annotation(end_index=15018, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSjbReuzQdJ5gqjVNu0j8mMmo1OdjwZ1hTwi2Pv4aZ-bxu3vrasVQzXIAOos13T22dZesSeWJ2NGP_ODgSWKOhsX_3wtOgmK9l9U7WFPq9f6Rn4qhlDP9rYM5dYDn0O19EHR86UYNqLR7Gi20oVHzdqif7pcsxihcospr-xvR5RftH4wSxRtH2jbnbC8Eg4WAsG0T9YXjvXU1uXFbD0-3QbFswPSnsp7r8QRapkam3i0yXodTuejCwRNRORZx85vJ2', start_index=15004)
Annotation(end_index=15100, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsJXOsy77nct0K5g0hek3-42vDgAqdf9RFYo17XwIYY4W54ttUpyWSigZV3ui80SCIvipFaeAJV1OCubuS5qo7YdjQrKCIzJWVrPFbgtChvaoW6hMzwRO8OYAiW288tr2auszLoOuufBi6vYF0p3lJ5A==', start_index=15084)
Annotation(end_index=15100, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1mnBPx_3HADRK6LgS9uYvemXkcgE3z1wMzifQhCduXOK6DFS-unkMB2B2aLGRn_5RCiInL8YEU07CFedPBNkuJc02IN4GY2ADKqemkOolcw4yJMI37AkuqZEKbVa2H6KhBTwntp3QYMEfd-Z0sos0FFu__m-rvgQ=', start_index=15084)
Annotation(end_index=15100, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3EB9l-JdSh8yzuyjb4aN3-VAZqOyTzNVBxJ9EFfY1t3hnLrqdA-UpE_ghhjLklU_q1OXKBklYLjA3jgMwVYfRvcLuXP3524ztuCMrWK1EdaAxPEkrw7sckMiwSwv5sG__Vcr717Aq7JOOyhcQ-pwjgvf9_CFiaHVbRQzu_0P-7H9TGxSV9NMv1GT_yHZSF7TbVB05MA==', start_index=15084)
Annotation(end_index=15190, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1coWbRS_7YliaUqEXZWDFKeYhngxzpybx2RNJzJ1m6lpozj_HGeLdGwvGAXfrL7fmlLrDFWhiqSDiV7LXsp6YCNjnAJgiJF0YhzOQ5_JiJ2hokXjkur2FUp578ppGYxUBzHPOFX8w2zQP_dgONz5L8UprioILix8rKj8xniiM1eh-Wfp8rZ8idH4t8yYMt571LrBIDkwauoRO_KeFdZI9jH3ZIszWDK44lmZr_72fXKEFYyWAopc7CRa4SeBzPkbs0xnRwi2wP4N8_P71gPCkRYT5-OkMdV-Wa95Wf7HXU7xxV8ZuEOwr5XOsiQg6fqUdyzxweFOSwfws', start_index=15172)
Annotation(end_index=15190, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcA6PnLaE3_vE2XVQQVTkHgHJISzkMMtGRoKitEpTkJfLmem6cLrStv485W61gvj5jert1AJLSG90Mek6NCgLQZo8azQsKrz7hwqU58vNiJhfvQSlnyB495SGbwzstXoY3pm3-Ca230-ivoDFIMyE94wDSrHogeI-y9nVXmeLVRMDVhT2dCJgdlIDXDbUsEI1tmcAGwFko4QoEw6imEup2bBPzAgK1vTSAaAUKJZSSKepoO9nlMsGtE53HGUeaKlXLbORUo13I_94hyfNT-3Nr6FgVjg==', start_index=15172)
Annotation(end_index=15190, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHh81-MMoA2iSJU-glTCbr7ioFHvScq_CX5iJfdqfrzGnWygukJtI-VBhrTCCZcuKmbTmGT6CVe0G1kSEO8Mthg295HD-FL6XCmbbJN20GHpRF7XXTJAb64G2ufFnaUSFiy5N8irK57', start_index=15172)

## Sources
