# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** fd9008cf | **Time:** 351.33s | **Cost:** $1.97267
--------------------------------------------------------------------------------

# Determination of Qualification Requirement Standards in Merchant Onboarding Audits

### Key Points
*   **Regulatory and Network Mandates:** Qualification standards are primarily derived from external mandates set by card networks (Visa, Mastercard) and government regulators (OCC, FinCEN). These entities establish baseline thresholds for fraud ratios (e.g., Visa’s 0.9% standard) and anti-money laundering (AML) compliance.
*   **Risk Appetite Frameworks:** Financial institutions determine their specific internal standards based on their "risk appetite"—a strategic calculation of how much risk they are willing to absorb in pursuit of profit. This involves setting minimum credit scores (often 670+ for owners) and Debt Service Coverage Ratios (typically 1.25x).
*   **Dynamic vs. Static Standards:** While historical standards were static checklists, modern standards are increasingly dynamic, utilizing AI and machine learning to adjust qualification requirements in real-time based on transaction monitoring and behavioral analysis.
*   **Industry-Specific Calibration:** Standards are not uniform; they are heavily weighted by industry. High-risk sectors (e.g., gambling, adult entertainment) face "Enhanced Due Diligence" (EDD) with significantly stricter qualification benchmarks compared to low-risk retail.

---

### Introduction
The determination of qualification requirement standards in merchant onboarding audits is a complex, multi-layered process governed by the intersection of regulatory compliance, financial risk management, and strategic business objectives. Merchant onboarding is the gatekeeping mechanism through which Payment Service Providers (PSPs), acquiring banks, and Independent Sales Organizations (ISOs) assess the legitimacy and financial viability of a business before granting access to the electronic payments ecosystem [cite: 1, 2].

The "audit" in this context refers to the underwriting and due diligence process—a systematic review of a merchant's identity, financial health, and operational model. The standards used to qualify or disqualify a merchant are not arbitrary; they are rigorously determined by a hierarchy of authority starting with federal regulations (such as the Bank Secrecy Act), filtering down through card network rules (Visa and Mastercard), and finally refined by the internal risk policies of the acquiring institution [cite: 3, 4].

This report examines the methodology behind establishing these standards, analyzing how quantitative metrics (like chargeback ratios and credit scores) and qualitative assessments (like reputational risk) are synthesized to create a qualification framework.

---

## 1. The Regulatory and Governance Framework
The foundational layer of qualification standards is established by government bodies and financial regulators. These entities do not typically set specific numerical thresholds for every metric (e.g., they may not mandate a specific credit score), but they legally require institutions to have a documented, risk-based program for determining those standards.

### 1.1 Office of the Comptroller of the Currency (OCC) Guidelines
In the United States, the OCC provides explicit guidance for national banks regarding merchant processing. The OCC views merchant processing as a high-volume, low-margin business that carries significant off-balance-sheet liability [cite: 4].
*   **Risk Management Systems:** The OCC mandates that banks must identify, measure, monitor, and control risks. Consequently, qualification standards are determined by the bank's need to demonstrate to examiners that they are mitigating credit, operational, and compliance risks [cite: 5].
*   **Policy Requirements:** Banks are required to establish policies that define "markets, merchant types, and risk levels the bank is and is not willing to accept" [cite: 3]. This means the qualification standard is often a direct reflection of the bank's regulatory charter and its capital adequacy to absorb potential losses.
*   **Third-Party Oversight:** The OCC requires banks to perform due diligence on third-party organizations (like ISOs). Therefore, the qualification standards an ISO applies to a merchant are often inherited directly from the sponsoring bank's regulatory obligations [cite: 6, 7].

### 1.2 Anti-Money Laundering (AML) and KYC Mandates
Qualification standards regarding identity are determined by the Bank Secrecy Act (BSA) and the USA PATRIOT Act.
*   **Customer Identification Program (CIP):** The standard for "who" can be onboarded is absolute: the institution must form a reasonable belief that it knows the true identity of the customer. This determines the requirement for government-issued IDs, Taxpayer Identification Numbers (TINs), and beneficial ownership information [cite: 8].
*   **Beneficial Ownership:** The standard for qualifying a corporate entity involves identifying the Ultimate Beneficial Owners (UBOs)—typically defined as individuals owning 25% or more of the equity interests. This 25% threshold is a standard determined by FinCEN regulations, though institutions may lower this threshold (e.g., to 10%) based on their own risk appetite [cite: 9, 10].

---

## 2. Card Network Rules and Thresholds
While regulators set the legal framework, the global card networks (Visa and Mastercard) determine the operational performance standards that merchants must meet to maintain their processing privileges. These standards act as the "upper limits" of risk; if a merchant exceeds them, they are disqualified or penalized.

### 2.1 Visa Acquirer Monitoring Program (VAMP)
Visa determines qualification and retention standards through its monitoring programs. As of 2025, Visa has consolidated its fraud and dispute programs into the Visa Acquirer Monitoring Program (VAMP).
*   **The VAMP Ratio:** The standard is determined by a ratio calculation: *(Fraud Reports [TC40] + Disputes [TC15]) / Total Settled Transactions*.
*   **Threshold Determination:** Visa sets specific basis point (bps) thresholds that distinguish "standard" merchants from "excessive" risk merchants.
    *   **Acquirer Thresholds:** Effective 2025/2026, acquirers are held to a strict standard, with "Above Standard" defined as exceeding 50 bps (0.5%) and "Excessive" as exceeding 70 bps (0.7%) [cite: 11, 12].
    *   **Merchant Thresholds:** For individual merchants, the "Excessive" threshold is set at 150 bps (1.5%) through March 2026, after which it tightens to 90 bps (0.9%) [cite: 13, 14].
*   **Impact on Onboarding:** Because acquirers are penalized if their portfolio average exceeds 0.5%, they often determine *stricter* onboarding standards for new merchants (e.g., rejecting applicants with a predicted dispute rate over 0.3%) to create a safety buffer [cite: 15, 16].

### 2.2 Mastercard Excessive Chargeback Program (ECP)
Mastercard determines its standards through a tiered system based on chargeback frequency and ratio.
*   **Standard Threshold:** A merchant is flagged if they have a chargeback ratio greater than 1.0% and more than 100 chargebacks per month [cite: 17, 18].
*   **Excessive Chargeback Merchant (ECM):** The qualification standard for remaining in good standing is breached if the ratio exceeds 1.5% for two consecutive months [cite: 19, 20].
*   **High Excessive (HECM):** The standard for "High Excessive" classification is a ratio of 3.0% or higher and 300+ chargebacks [cite: 17, 21].
*   **Determination Logic:** These standards are determined by Mastercard’s analysis of network-wide fraud data. They serve as a global baseline; acquirers cannot set looser standards, but they can (and often do) set tighter internal standards (e.g., terminating a merchant at 0.8%) to avoid network fines [cite: 22, 23].

---

## 3. Internal Risk Appetite and Financial Standards
Beyond external mandates, qualification standards are determined by the acquiring institution's "Risk Appetite"—the amount and type of risk an organization is willing to pursue or retain [cite: 24].

### 3.1 Financial Stability Metrics
Auditors evaluate whether a merchant is financially stable enough to cover potential chargebacks (which are essentially unsecured loans from the acquirer to the merchant).
*   **Debt Service Coverage Ratio (DSCR):** This standard measures a company's ability to pay its debts.
    *   **Determination:** While there is no federal law setting a DSCR for merchant accounts, the banking industry standard is typically a minimum of **1.25x**. This means the business generates $1.25 in net operating income for every $1.00 of debt service [cite: 25, 26].
    *   **Variability:** Lenders with a higher risk tolerance may accept a DSCR of 1.15x, while conservative banks may require 1.35x or higher [cite: 27].
*   **Credit Score Thresholds:**
    *   **Personal Credit:** For small businesses (SMBs), the owner's personal credit is a proxy for business reliability. The standard "good" threshold is often determined to be **670+** FICO. Scores below 600 may trigger disqualification or requirements for a cash reserve [cite: 28, 29].
    *   **Business Credit:** For established entities, a Paydex score (Dun & Bradstreet) of 75-80 is the typical qualification standard [cite: 30].

### 3.2 Operational and Industry Risk
The determination of standards is heavily weighted by the merchant's Merchant Category Code (MCC).
*   **High-Risk vs. Low-Risk:** Standards are bifurcated. A "Low-Risk" merchant (e.g., a coffee shop) faces a simplified qualification standard (Card-Present, low ticket size). A "High-Risk" merchant (e.g., online gambling, nutraceuticals) faces Enhanced Due Diligence (EDD) [cite: 31, 32].
*   **TMF/MATCH List:** A binary qualification standard exists regarding the Terminated Merchant File (TMF) or MATCH list. If a merchant or its principal appears on this list (due to previous fraud or excessive chargebacks), they are almost universally disqualified by standard acquirers [cite: 3, 31].

---

## 4. The Audit Process: Applying the Standards
The actual application of these standards occurs during the underwriting audit. This process has evolved from manual checklists to automated workflows.

### 4.1 The Onboarding Checklist
The audit verifies compliance with the determined standards through a rigorous checklist.
*   **Identity Verification:** Collection of passports, driver's licenses, and utility bills to verify address and identity [cite: 33].
*   **Business Legitimacy:** Verification of Articles of Incorporation, EIN/TIN matching, and website content analysis (checking for refund policies, terms of service) [cite: 34, 35].
*   **Bank Verification:** Confirmation that the settlement account is a valid business account, often verified via voided checks or bank letters [cite: 34].

### 4.2 Automated vs. Manual Underwriting
*   **Automated Scoring:** For low-risk, low-volume merchants (micro-merchants), standards are determined by algorithmic scorecards. If the data points (credit score, industry risk, identity match) produce a composite score above a certain threshold, the merchant is auto-approved [cite: 36].
*   **Manual Review:** For high-risk or high-volume applicants, a human underwriter applies the standards subjectively. They analyze business plans, processing history, and financial statements to make a determination based on the institution's credit policy [cite: 1, 37].

---

## 5. Technological Evolution of Standards
The determination of standards is shifting from static rules to dynamic, AI-driven models.

### 5.1 Dynamic Risk Scoring
Modern underwriting uses AI to determine qualification based on predictive modeling rather than just historical data.
*   **Generative AI and Synthetic Data:** Institutions are beginning to use generative models to simulate merchant behaviors and test underwriting systems. This allows for the determination of more nuanced risk standards that can distinguish between a legitimate high-growth startup and a "bust-out" fraud scheme [cite: 38].
*   **Behavioral Biometrics:** Qualification standards now often include "passive" checks, such as analyzing how an applicant interacts with the application form (e.g., typing speed, copy-paste behavior) to detect bot activity [cite: 9].

### 5.2 Continuous Monitoring (The Ongoing Audit)
Qualification is no longer a one-time event. The standards for *retaining* a merchant account are applied continuously.
*   **Trigger-Based Audits:** If a merchant's monthly volume spikes unexpectedly or their chargeback ratio creeps up, automated systems trigger a re-underwriting process. The standard for "abnormal behavior" is determined by the merchant's historical baseline and peer group analysis [cite: 39, 40].

---

## 6. Conclusion
The qualification requirement standards in merchant onboarding audits are not static numbers pulled from thin air. They are the result of a rigorous determination process that balances **regulatory compliance** (OCC, AML), **network integrity** (Visa/Mastercard thresholds), and **financial prudence** (DSCR, credit scores).

*   **External Determinants:** Visa's 0.9% dispute threshold and government AML laws set the "floor" and "ceiling" for acceptable risk.
*   **Internal Determinants:** An acquirer's capital reserves and strategic focus determine where they operate within those boundaries—whether they are conservative (requiring high credit scores and low risk) or aggressive (accepting high-risk verticals for higher fees).
*   **Technological Determinants:** As AI and automation evolve, standards are becoming more personalized and dynamic, moving away from rigid "pass/fail" criteria toward continuous, risk-based scoring.

Ultimately, the goal of these standards is to maintain the integrity of the payments ecosystem, ensuring that only legitimate, financially stable businesses can process transactions while filtering out bad actors who threaten the system with fraud and insolvency.

---

### References
**[cite: 1]** Ramp. (2025). *Merchant Underwriting*.
**[cite: 2]** MVSI. (2025). *Understanding Merchant Underwriting: A Guide for Payment Providers*.
**[cite: 33]** Fenergo. (2024). *Merchant Onboarding Compliance*.
**[cite: 9]** Smile ID. (2025). *Merchant Onboarding Guide*.
**[cite: 39]** Trulioo. (2021). *Best Practices in Merchant Onboarding*.
**[cite: 22]** Chargeback Gurus. (2021). *Chargeback Threshold Mandates*.
**[cite: 31]** Stream Payments. (2025). *Merchant Exposure is Structural*.
**[cite: 3]** FDIC. *Risk Management Manual: Credit Card Related Merchant Activities*.
**[cite: 6]** OCC. *Comptroller's Handbook: Merchant Processing*.
**[cite: 4]** OCC. *Merchant Processing Booklet*.
**[cite: 5]** JD Supra. (2014). *Sleeping Giant: OCC Wakes Up to New Focus*.
**[cite: 41]** Fi911. (2023). *What are Visa & Mastercard Chargeback Thresholds?*
**[cite: 11]** Ravelin. (2025). *Visa VAMP Changes Chargeback Disputes*.
**[cite: 15]** Solidgate. (2025). *Visa Announces New Change to VAMP Rules*.
**[cite: 38]** Medium. (2025). *AI in Risk Management: AI-Driven Enhancements in Merchant Onboarding*.
**[cite: 13]** Chargeback Gurus. (2025). *Visa Announces Even More VAMP Changes*.
**[cite: 17]** Chargeflow. (2025). *Mastercard Chargeback Survival Guide*.
**[cite: 25]** Clearly Acquired. (2025). *Ultimate Guide to DSCR in LBOs*.
**[cite: 28]** Rho. (2025). *Minimum Credit Score*.

**Sources:**
1. [ramp.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEokehyfdeVti2lemHyIKqF_0pL3aReFDPdE2b9vPf6T10ZvMdh3DXa5ZO4NbGGYZiuFR58o4eurXPINBB8po2cE1KZ8_8Qexoaxyx6uObY9A5v5A6hvSUrR5hcCJKNHH7t)
2. [mvsi-onboard.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5iOpGBCbGaG8DgNvqvsASCy09XkMrwTIXCfSsX7OKL8UqY24BiKCugxyK6GlR4T9K7KoYOZHUdLACpGHK0BbAmWm6CLtk8AMyjVbBDgGRovwsT_eCobgjChpg__3IJVxOtyO03yWRsex985HXQoXC4o9ThKjZPkXuk7oUBjqlaH8eCGJs-Gp3uXewJ_3I_Wl4pLBDgx-zEXc=)
3. [fdic.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1CD-uH0LkayOC6-JtsMuKLj6wocvvlPuh0QBR5NjLD8iBog1iCSTCgsfg7_dXAVNmyUw0nKOExPIz6zGrC_CUGRpVItur-bBai6ta3U1W8Dq81kZSq24ySdmIExj-mZTwsSJGnPiG7FjHv_t3Rk8QLGwq_yzHI0BGthzodTRk63rHNA==)
4. [treas.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEahCNz1GBbZCp87BLSph8yBpw18RBNAAA2MrtfElSnCf6QWv6aourSAHQVO4Lop3vcT81cLLoFYxPZB-9z6QLS0unWde4egpHHV6uYZBLdEZJxVXVKkT6AP5oZd7OpERl9hXu_H31WiTxe6_zdgU41mv1fLlqPc3Se7sU471CaJa76dAYiJbtV1z-QihHQ2RbMGKb5L-aWtkPTQVmeTbNIsDIyUnRpFkCW0ooCOHsRJuzYzQfPK6t1KDgxFx-RKaEwcTPPDov7)
5. [jdsupra.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIn4y7G2t203ve7Ag3QUWBaxkBKPTBu8eO3sXWIkXTHsATgBoKbr8k5vB30KQ0tcKMyVHeXHvrVAekS2b89RRbSsfeXyE52UwEKiXvuAeh-I62sxWFJ1pysgm4bRwcOhSDYzB5Vgepco7D2NhnVteMrEQq2qQgvyPEqeXQ4aYpYcfhyG1DNg==)
6. [treas.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGROj_MKmFCzbn79DJ9mlSZZFyeVPEX7RVXLIjndEJDUq61Ta2DgF40SKLN4wOUqNceTCQvKPOadx1VqWZcC28uQSGUy4vtDlOFXTcSo5tasItLpwYve_rZ88RDeD7NE7hvMAylp615HThBr7LF7MIZIz-GAjnJUcWeDEGlaCRE1LhlmNW4ljtBL_LeHxm5pzOr4R8GjD-L-NqBExwI-OOhzxObJOxJYCKCAA9AMeGNrQ-KCd-FFazsUp6WVBDz8JGPoF50PC9ReYC3L5rlhsrr)
7. [occ.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFd1w680kJKbnW1sXRV740Gnoi8LLQtP_Hp3czVqXs_QjSyJjpzUj37a9SsxGQV4NFXSnP-wABC16OKY-3Pr3clrANXueCwt7uEgRidhIB-1rDcS3z44Ubhp4rDcJ76Jm6olFTd4wDjtPvz3ul7Z0cHNlTjpre1DikAAi0e_A==)
8. [chartergroupadmin.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcS8iYHbH-6tXY9h9yJJS_g9sNPHJ9xApWL6o5trFJpaHvy4TJw5wwDCH25wxiet3jPco5L2DQe7Z9xcD7kVen865vHdIfrlxEKxumk6xY7mnAi34jVowISDLg1unqn9ZOURvuGmy0eqfGEN5CXU-hna8m5g5Yp2XSb9StH-TfK4paLdEPsEILwSG7xAzpax7L)
9. [usesmileid.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_VjkDxxho1tbAAgNtk94Ysxb-mfEpL2sTNyL-fmd6_UcgF4l1rRNunIV0C-TcbNkrnLRTM_p8DHd62rDr4JjhtlQWD1D3gQyesveog6iuKbTACteWYMQm6vOayMGbfiftWONPexihsiGNdA==)
10. [middesk.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMlsccH7cXs6E9o_1doDS3wX1Ayygy4VD2owrtGZCOyk5t__aS5_ipzCPqT-eivysEqs0PXJRVnQWH7jsCn8GQh6x8155bRl6QnfYxcQWM659GTvbmYy_4VVV9UuIBSrn0ycYmVTfVpUcjLdnks0-nlVHlIJA=)
11. [ravelin.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEq2PhaYeS5Q8f0udjxbYd5bW0IPLMdg_QcE_7sgbep2QyCSERuX868awsALQ5ZSvn0Ybt5hpZ_1qjWlZb_XmByKF73HESakxMzfx7CtPa6Fw0SWL2wUVgvfzhhuiMPa7IJwBRoj7L9LeiObhg30eYax9ye-jMuBdU=)
12. [austreme.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEg4A6smlwmMY4y1RoQAyPBD04Q12mTNBT4Wlkk86qUxefGRM89qrZmzU1psDYW1PBbzPZUNvcosjH_IbbyOcVI4Xa_MAF_R2tkE_RcwjY_a99LSrxZJxSJgTnnVfVYYeveeUwzhtoH28bbC7Y_kho=)
13. [chargebackgurus.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHcjPnzpbYhyvUi5GudUSJHhYks83sP_GSNh0LptlK1uTO7AybGHJ0FeiXtz-nNHGOyBtdrxyRuvN-jJaZqMfc55QCasRq2aVnaXRp5JBL38YMHXQwDIo53MES2_h5BZU1o22j1EiH5-UL5AuE0GG8apCKltT_tUWYn2ujsyWg_A==)
14. [basistheory.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpZBK92b14RA5Xtyj_HXYxF_G5GkedNqbZBFT9R9lJ6zXXdEl4cHpO5J9AKtEKwk-FDSZBvargK0nRBOHrX9bshzPjnTnRpk-0rYjYvUeNGX7sZ1kYsuXm4lrO3KvXJQA-vx20a--CxQaXqo71fxzKax3_)
15. [solidgate.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtrPHNuPz_bDbBA_yltizu5CNThTWi6C4EJANdpaLDx5wfVyHBeb_5wmGC9BIfbPe8QtGXO3ik4xfKt4e_uW0FPAoN1x0jFwZul7vOTwJ5yPzGoxQdtju5-d0UFm5vX647_vwgZoqoN2Qo610WqbMH7WUd5DtKnPq-)
16. [chargebackgurus.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6nnyXZ5lc-m12OuuWOUttMzIUBoGEUYzGgWacoOE6AnVx4yjkcbZIUSpJAPXFg7dwN3nimwqpRijSTEC8xkA1TfhXIKnoX19YPono4mhluU6qPac6pHhzSjUGX_DF46dryVaANYcgo4kmptX1M3BGmD7z23z4tXARYZo=)
17. [chargeflow.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH60GDpj5-Ah_y5I9LynknF9IGym7KMbOW3rZiOETz-SyDUdF-ly9L9yiTp00cpBsunU7GMPnIEGaH4D7Cs08sDTFa9VqgNSsrk6pJrsXPO72FDzFpSfUY1FLqISA55zaaCS65cUtZeFxNnU4nZkkqX9Z6P6jbXRZCq)
18. [kount.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxmTnNKZ48U6RpibMLwcZAyymnHVjllKVxlW-FzflM1dBjPKYxc3rqvRndCsHivGiqyLDc6dpWMoShag-h3gIvLX_iI662zlTFkkqIykt4Ll5BxsYifXNMO4FYQQ4mbEPaPthmH-Glv4A9TkaK9Gi4jOSA0ggZ7mOy74A=)
19. [kount.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpiCVQ9aWM-A1Zj7r5w5nZISPc3s5J0_EKoZMw24GcCYx0Z4y4XRpNJb4qwNGoK0Tya1dQCbBFjk3sTDJSCIutju2BXWdITOSba7IjpTh-aGeSWxUS1ZeKneaVK-Q2tpfCled9KYXyGRuTq5dWQs_mEHacOKs5dp4=)
20. [jpmorgan.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTFbi799GktXWpgHL0qSqcNHs36yTQzZXWAnqun8921vt1LIhG1B_8i3qw9BctY9fjrvcenTKPDkQzHiVTkCDvrAa8mmD-eYuV2VnDrryz6LSUWIN4CzO9rvgDHvQJvzaD3QpmgY5Xv5z-Es-ezlvk5ipCwUakYrNuwWUN0stRaH2Z0iztwSnaj47wlHlZuslgX2DfJgxBbUggh6ax6h2JhvJtHH7a_0uh5bSIlRm7PInZMAZv009emWV8dJxYACx-6Th5eA==)
21. [chargebackgurus.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfB04j2H9bY7lblB8igjRI8KCxN7r4P0qzun7K20rXRip-JGRMptRxLa8vf2g-8HNGwe3NCaVqIg0YwGyf5AUuxaD3kF_Eb3yLHlYCs3oI3Mxhwm7dU24cs6YopyQ8Ti3GENDA71ijHwF9sjAbpnde5C4MCHVp7mYTipvwljEt4Msv)
22. [chargebackgurus.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHo8DhYVEtUkPPPggz7H9voc6z_ewjslmKPsl1stmozpTLJ0m-mGiXZIt8tASCzY--PMPwoBPuGtIi28BbmkxZ9gL_9YvMNSdbYfakyZ_eZsj53mLGnb4WzmU8p7RCS6q9YhUaC5VPJLIatnimboVOMeepbyKVHrIA=)
23. [chargebacks911.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQY-OjHUpn6r7gl6CHjyqSj0dVxeBQMn2Rib-QJsfqB3WpQeKlKl740RsN5QILlwxZniN6zCzoCdyBdUbrLs1eTaK_P0Z-HGAuMpvx9P51LBcSlas2xo9BGWQ-AQ_BKwokywfTBlWcvFEElg==)
24. [pecb.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAVSm93CEfflpgEs_DTMOd8S1gLW9gbRGB0vGZvccpVeAf8Vl2_5-I2nYCCF3vyqRWa1uug-zxGrM126k79rSk516elpq6IQnJG3w9MJVU3JRCcMIZxWph327E1L_ATW2RZ3o1hGDKPlCp63h9qVa6l1l6YiYUm4TMSiJ5Qs5uIVrYsY8ASjFwH4S8rtUq9JKfVLwq)
25. [clearlyacquired.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_ghrxcja5PnD9MwDLeCttMg4ouFP_tqj3Ff-veY7_6wTgBfNvODetKhBRHZzVw_KpaBJoioV1teSsMY3z1LaVy3J7uWy6OGowoKUyf5ZyVDUuDyb-K-Py4y8hEI_WOsozuJSks3oH9YUFKqrm2FCJY54wcVX41T_4)
26. [merchantmaverick.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhBuVO-T70NDqMYiu4qZz481Spt3CS9UkVpq7dPY3D2xgGBQGnrLB8QyINYyq56PVuuDXCnvm1ped_PTLyDovN8_IR7qODTTnjS1XD1O-HejN1OEYnEbu3pGeWwj2tjoFun7lu_KI3TMXcxQ4iNeA9CM5gDCf0g627lM3Bbw==)
27. [ampadvance.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1X9vUPP3ArelMegfQKNIph981VPJWdSupC9zSGu24JtksUn_RD1Vs5BUW1FGAI-XTiJ7SfSRXF73jmerfgmCVDgv_Zjezu7BXNPYp6YuK80UK6gRR4GCinYMD28Y0XYKYmg==)
28. [rho.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeFcJqsStDvQZVkI0OpAFflCG0p4eztldg3OC3d0Jg_45qBKG4KKhjaD8ebaB8aeGGzvLBOKFE022gV1vzqxrU5Cc2zQ4HGNx8gN4GFUjf3j4dp-fACfv4N8z3AqtemE_cKQ==)
29. [bankrate.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcHOWGS6Fm02Gg6KgeMIO5FDBl5mHj8lc1t_CQ_o0hIqB3KURga_d0Xup2k5iH9EgtTmJbVMAwO_TnSkg4E8c2_Yu01f2wDli24fA0UMLsMEycYLSgk1DAxXx9t1G1ojcyy9AcBGC3acSs4Qg37qNb_5XNS4njIOcxX32hDTtR)
30. [capitalontap.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyYDTKrgsHx-GE_58zzgFKE1pYwlZ-UlnqMXuIfNMUgIWw4KFCjX_39qqvoGA8qgyuSaciJb45duMUDJK8W738roFpqs24-L_XekV2PcajKr83hquMWEQlqMgRS9XeCgFQbmG_uUc8TfmOciowE8PE0eMCPN0vPcl7BrCkFOkSxE3Azw==)
31. [streampayments.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHVx95OfIHbzzRuIxbecg279J96Wq_dx2oA5dg-qKWg64K4t8LxCfsNAYNNyhVFiC2xeTvVrbQYDYh9LyUi5w4ptCFxDRp5Y1oHsSE7HYqBatF2WJnFpReyqb57OsyM-8CX_Pn6Wv4duBY24a28KYCssw2Bh-empTv)
32. [signaturepayments.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHumVlOnP8y9jf9Oc8Xmh6QhTHNhipeIDwbNAlSlP13d_2Js2uwibRbiCcC9xHLGIsEVhuKVJu9KGvSN8rZRE5hn__ieZWwfRHtfyjfuwzubNFr2bzHqXikF1GAOT3WXGh4BecIWiSfntvV4DBqkXwSirxenyQnuL1lWoTF9rdHAug3GQA=)
33. [fenergo.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEK3G8LKPVWGQAwkWnoWpNPH-sAcRNi7El9lK0RSMTX_ueeipgIA7bxrcuZAJyeLcGAw2g0mXJ4MVVrnGlgj8rw5V68kA9-MziM0F46ufPzALGfZrOryigvYGRgCKZV9dzvBLBug4kqWskDJLDDaEmHJU9cloEv1iE=)
34. [clustdoc.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhQU5nyZbxHzx1eoQOKHXbuCNk6dRypamtOZo2SxfyCKaQkI8rFOrSB9uD0qkd_jtDXzLeLkvs1zeK_pOohGuhfgKPIBdGX9vOYOODv3Ez0yHFR5FMQGw_85QqdmL9K0-tbQEPq-AalhNComnpKw==)
35. [stripe.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHiPlgsP8Y377WEy8npO-mTeN_wzR2tRnfPF-d2a8cMYTlNt9PYuiNQRHQZAaUZ2Wmf1HNApicYtmh8MSFUN7-X6iKmZrJA0NDJsk7S7vUn_iQZgmZCRnp3Pv177ZS3wU3O1nSj0LvGCPO9NH6zDQrdBjn6fMQ=)
36. [mastercardservices.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBbTyux3kKwzP9MV-7B-BFZOVBSXPxa7UPpbri0DaFAAuEBc1XTGNLVWjKoUzGYCIfqHqiWWJdyWIf86AtJzTGygQyjeYF8Q3pkeJo8ocTiJNTtEyMHQg5ulVRMk_Bc0MyEAEiL0Ojz6d12rgBJMSL6k63xBqVROGEC60HA9dkQDhfKMZaqzT7bin6bP13BUYe2IKyyBQzndSZMdWw)
37. [nmi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtS_Vl_rIzNesC5TnPaw9qbtVaaBo6fOooyMtsrL6wzZAmTWcoVh1qP_vNMcxnqNZOHxaP5sD0WiMN35bIu_o0DscqgFoOn5qis52R6Howx87NyNnsFGZiyRWXu_Ul8V_0zm4cJUPXCcdlPi5uS1OMlxzNYdoTDOEawkjRo9lQGe82x17HU4g=)
38. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlGf71HaWFTR-F1bwzXipdzsnh2Q_3r4LtBaB7nVGaNyqe-KALR_RuN5E4Y-4ebiSh9zjAjyeSD53hnuVtkQUihXW2GmRCe2TxDDkfK4K2T3LEvusPCWTJn_DHZ2k6F4nZAYd94oPL6wNZz5OZR8GgQXZBicf3HLKHzS12lwSGZbezYTf9rFkzTYvh3mvMs1TBbDNTXI6Uc7iVtgrflUG_lR9GBM5hlvIn39j0RQbVZSBjxNt2Lj-Y)
39. [trulioo.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4fB-RjfBhGLjtVVIdfMCzzTuh0G0MjhdEdGYqyo-XkG5ftRSMvxC2Ld8KGeYAJzvjgl5SareM4w_NDMlVb6rqvMW7FfL6qjxF8HJUUqzkdVwigQNAyvL_8Os0tIJXm6v2TwB9yI9o7XyV_mKKvYQDV_uiTuFUgn5jdm11JSfy4L7-gcEI-hWG3L4p)
40. [gratifypay.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGPjqiz1IjtYj3thnO8ztfi0DdfBoWCI4tA4to7WYxlrbPGxFWMgoAJKUdkuGGhLesCAC4jUtt3CLBSLPky9RIKnOtREizX_5r4tHrj0KXs75GV4Vq0LMAuBZDMk7MPgmo6wigF7bpwQrbSwY6_n_vJ6ruGGP5-_phj-R68jm4ZGN231sleTQULJnCGhPi3Q32XoB3ZpUhWA==)
41. [fi911.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJdY0T196J59QTuhBcUSn9pK_FvxwPb5F9lQUsm1zpJmpAwXSM5vhd6VD1ExNDtCAkXd3HmQihiAojhSYa9NlujHRV2NOXQdrepDilrnJfJRFjdsExPXlDbHbRBX-ziNhKARGA0NU-3g7LWzO6Vv4lyNnRRS4Xwcm1b8Q6)


## Annotations
Annotation(end_index=1877, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEokehyfdeVti2lemHyIKqF_0pL3aReFDPdE2b9vPf6T10ZvMdh3DXa5ZO4NbGGYZiuFR58o4eurXPINBB8po2cE1KZ8_8Qexoaxyx6uObY9A5v5A6hvSUrR5hcCJKNHH7t', start_index=1865)
Annotation(end_index=1877, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5iOpGBCbGaG8DgNvqvsASCy09XkMrwTIXCfSsX7OKL8UqY24BiKCugxyK6GlR4T9K7KoYOZHUdLACpGHK0BbAmWm6CLtk8AMyjVbBDgGRovwsT_eCobgjChpg__3IJVxOtyO03yWRsex985HXQoXC4o9ThKjZPkXuk7oUBjqlaH8eCGJs-Gp3uXewJ_3I_Wl4pLBDgx-zEXc=', start_index=1865)
Annotation(end_index=2405, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEahCNz1GBbZCp87BLSph8yBpw18RBNAAA2MrtfElSnCf6QWv6aourSAHQVO4Lop3vcT81cLLoFYxPZB-9z6QLS0unWde4egpHHV6uYZBLdEZJxVXVKkT6AP5oZd7OpERl9hXu_H31WiTxe6_zdgU41mv1fLlqPc3Se7sU471CaJa76dAYiJbtV1z-QihHQ2RbMGKb5L-aWtkPTQVmeTbNIsDIyUnRpFkCW0ooCOHsRJuzYzQfPK6t1KDgxFx-RKaEwcTPPDov7', start_index=2393)
Annotation(end_index=2405, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1CD-uH0LkayOC6-JtsMuKLj6wocvvlPuh0QBR5NjLD8iBog1iCSTCgsfg7_dXAVNmyUw0nKOExPIz6zGrC_CUGRpVItur-bBai6ta3U1W8Dq81kZSq24ySdmIExj-mZTwsSJGnPiG7FjHv_t3Rk8QLGwq_yzHI0BGthzodTRk63rHNA==', start_index=2393)
Annotation(end_index=3388, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEahCNz1GBbZCp87BLSph8yBpw18RBNAAA2MrtfElSnCf6QWv6aourSAHQVO4Lop3vcT81cLLoFYxPZB-9z6QLS0unWde4egpHHV6uYZBLdEZJxVXVKkT6AP5oZd7OpERl9hXu_H31WiTxe6_zdgU41mv1fLlqPc3Se7sU471CaJa76dAYiJbtV1z-QihHQ2RbMGKb5L-aWtkPTQVmeTbNIsDIyUnRpFkCW0ooCOHsRJuzYzQfPK6t1KDgxFx-RKaEwcTPPDov7', start_index=3379)
Annotation(end_index=3679, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIn4y7G2t203ve7Ag3QUWBaxkBKPTBu8eO3sXWIkXTHsATgBoKbr8k5vB30KQ0tcKMyVHeXHvrVAekS2b89RRbSsfeXyE52UwEKiXvuAeh-I62sxWFJ1pysgm4bRwcOhSDYzB5Vgepco7D2NhnVteMrEQq2qQgvyPEqeXQ4aYpYcfhyG1DNg==', start_index=3670)
Annotation(end_index=3856, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1CD-uH0LkayOC6-JtsMuKLj6wocvvlPuh0QBR5NjLD8iBog1iCSTCgsfg7_dXAVNmyUw0nKOExPIz6zGrC_CUGRpVItur-bBai6ta3U1W8Dq81kZSq24ySdmIExj-mZTwsSJGnPiG7FjHv_t3Rk8QLGwq_yzHI0BGthzodTRk63rHNA==', start_index=3847)
Annotation(end_index=4291, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFd1w680kJKbnW1sXRV740Gnoi8LLQtP_Hp3czVqXs_QjSyJjpzUj37a9SsxGQV4NFXSnP-wABC16OKY-3Pr3clrANXueCwt7uEgRidhIB-1rDcS3z44Ubhp4rDcJ76Jm6olFTd4wDjtPvz3ul7Z0cHNlTjpre1DikAAi0e_A==', start_index=4279)
Annotation(end_index=4291, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGROj_MKmFCzbn79DJ9mlSZZFyeVPEX7RVXLIjndEJDUq61Ta2DgF40SKLN4wOUqNceTCQvKPOadx1VqWZcC28uQSGUy4vtDlOFXTcSo5tasItLpwYve_rZ88RDeD7NE7hvMAylp615HThBr7LF7MIZIz-GAjnJUcWeDEGlaCRE1LhlmNW4ljtBL_LeHxm5pzOr4R8GjD-L-NqBExwI-OOhzxObJOxJYCKCAA9AMeGNrQ-KCd-FFazsUp6WVBDz8JGPoF50PC9ReYC3L5rlhsrr', start_index=4279)
Annotation(end_index=4800, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcS8iYHbH-6tXY9h9yJJS_g9sNPHJ9xApWL6o5trFJpaHvy4TJw5wwDCH25wxiet3jPco5L2DQe7Z9xcD7kVen865vHdIfrlxEKxumk6xY7mnAi34jVowISDLg1unqn9ZOURvuGmy0eqfGEN5CXU-hna8m5g5Yp2XSb9StH-TfK4paLdEPsEILwSG7xAzpax7L', start_index=4791)
Annotation(end_index=5190, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFMlsccH7cXs6E9o_1doDS3wX1Ayygy4VD2owrtGZCOyk5t__aS5_ipzCPqT-eivysEqs0PXJRVnQWH7jsCn8GQh6x8155bRl6QnfYxcQWM659GTvbmYy_4VVV9UuIBSrn0ycYmVTfVpUcjLdnks0-nlVHlIJA=', start_index=5177)
Annotation(end_index=5190, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_VjkDxxho1tbAAgNtk94Ysxb-mfEpL2sTNyL-fmd6_UcgF4l1rRNunIV0C-TcbNkrnLRTM_p8DHd62rDr4JjhtlQWD1D3gQyesveog6iuKbTACteWYMQm6vOayMGbfiftWONPexihsiGNdA==', start_index=5177)
Annotation(end_index=6316, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEg4A6smlwmMY4y1RoQAyPBD04Q12mTNBT4Wlkk86qUxefGRM89qrZmzU1psDYW1PBbzPZUNvcosjH_IbbyOcVI4Xa_MAF_R2tkE_RcwjY_a99LSrxZJxSJgTnnVfVYYeveeUwzhtoH28bbC7Y_kho=', start_index=6302)
Annotation(end_index=6316, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEq2PhaYeS5Q8f0udjxbYd5bW0IPLMdg_QcE_7sgbep2QyCSERuX868awsALQ5ZSvn0Ybt5hpZ_1qjWlZb_XmByKF73HESakxMzfx7CtPa6Fw0SWL2wUVgvfzhhuiMPa7IJwBRoj7L9LeiObhg30eYax9ye-jMuBdU=', start_index=6302)
Annotation(end_index=6503, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHcjPnzpbYhyvUi5GudUSJHhYks83sP_GSNh0LptlK1uTO7AybGHJ0FeiXtz-nNHGOyBtdrxyRuvN-jJaZqMfc55QCasRq2aVnaXRp5JBL38YMHXQwDIo53MES2_h5BZU1o22j1EiH5-UL5AuE0GG8apCKltT_tUWYn2ujsyWg_A==', start_index=6489)
Annotation(end_index=6503, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpZBK92b14RA5Xtyj_HXYxF_G5GkedNqbZBFT9R9lJ6zXXdEl4cHpO5J9AKtEKwk-FDSZBvargK0nRBOHrX9bshzPjnTnRpk-0rYjYvUeNGX7sZ1kYsuXm4lrO3KvXJQA-vx20a--CxQaXqo71fxzKax3_', start_index=6489)
Annotation(end_index=6788, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6nnyXZ5lc-m12OuuWOUttMzIUBoGEUYzGgWacoOE6AnVx4yjkcbZIUSpJAPXFg7dwN3nimwqpRijSTEC8xkA1TfhXIKnoX19YPono4mhluU6qPac6pHhzSjUGX_DF46dryVaANYcgo4kmptX1M3BGmD7z23z4tXARYZo=', start_index=6774)
Annotation(end_index=6788, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtrPHNuPz_bDbBA_yltizu5CNThTWi6C4EJANdpaLDx5wfVyHBeb_5wmGC9BIfbPe8QtGXO3ik4xfKt4e_uW0FPAoN1x0jFwZul7vOTwJ5yPzGoxQdtju5-d0UFm5vX647_vwgZoqoN2Qo610WqbMH7WUd5DtKnPq-', start_index=6774)
Annotation(end_index=7100, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH60GDpj5-Ah_y5I9LynknF9IGym7KMbOW3rZiOETz-SyDUdF-ly9L9yiTp00cpBsunU7GMPnIEGaH4D7Cs08sDTFa9VqgNSsrk6pJrsXPO72FDzFpSfUY1FLqISA55zaaCS65cUtZeFxNnU4nZkkqX9Z6P6jbXRZCq', start_index=7086)
Annotation(end_index=7100, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxmTnNKZ48U6RpibMLwcZAyymnHVjllKVxlW-FzflM1dBjPKYxc3rqvRndCsHivGiqyLDc6dpWMoShag-h3gIvLX_iI662zlTFkkqIykt4Ll5BxsYifXNMO4FYQQ4mbEPaPthmH-Glv4A9TkaK9Gi4jOSA0ggZ7mOy74A=', start_index=7086)
Annotation(end_index=7284, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpiCVQ9aWM-A1Zj7r5w5nZISPc3s5J0_EKoZMw24GcCYx0Z4y4XRpNJb4qwNGoK0Tya1dQCbBFjk3sTDJSCIutju2BXWdITOSba7IjpTh-aGeSWxUS1ZeKneaVK-Q2tpfCled9KYXyGRuTq5dWQs_mEHacOKs5dp4=', start_index=7270)
Annotation(end_index=7284, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTFbi799GktXWpgHL0qSqcNHs36yTQzZXWAnqun8921vt1LIhG1B_8i3qw9BctY9fjrvcenTKPDkQzHiVTkCDvrAa8mmD-eYuV2VnDrryz6LSUWIN4CzO9rvgDHvQJvzaD3QpmgY5Xv5z-Es-ezlvk5ipCwUakYrNuwWUN0stRaH2Z0iztwSnaj47wlHlZuslgX2DfJgxBbUggh6ax6h2JhvJtHH7a_0uh5bSIlRm7PInZMAZv009emWV8dJxYACx-6Th5eA==', start_index=7270)
Annotation(end_index=7430, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH60GDpj5-Ah_y5I9LynknF9IGym7KMbOW3rZiOETz-SyDUdF-ly9L9yiTp00cpBsunU7GMPnIEGaH4D7Cs08sDTFa9VqgNSsrk6pJrsXPO72FDzFpSfUY1FLqISA55zaaCS65cUtZeFxNnU4nZkkqX9Z6P6jbXRZCq', start_index=7416)
Annotation(end_index=7430, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfB04j2H9bY7lblB8igjRI8KCxN7r4P0qzun7K20rXRip-JGRMptRxLa8vf2g-8HNGwe3NCaVqIg0YwGyf5AUuxaD3kF_Eb3yLHlYCs3oI3Mxhwm7dU24cs6YopyQ8Ti3GENDA71ijHwF9sjAbpnde5C4MCHVp7mYTipvwljEt4Msv', start_index=7416)
Annotation(end_index=7754, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQY-OjHUpn6r7gl6CHjyqSj0dVxeBQMn2Rib-QJsfqB3WpQeKlKl740RsN5QILlwxZniN6zCzoCdyBdUbrLs1eTaK_P0Z-HGAuMpvx9P51LBcSlas2xo9BGWQ-AQ_BKwokywfTBlWcvFEElg==', start_index=7740)
Annotation(end_index=7754, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHo8DhYVEtUkPPPggz7H9voc6z_ewjslmKPsl1stmozpTLJ0m-mGiXZIt8tASCzY--PMPwoBPuGtIi28BbmkxZ9gL_9YvMNSdbYfakyZ_eZsj53mLGnb4WzmU8p7RCS6q9YhUaC5VPJLIatnimboVOMeepbyKVHrIA=', start_index=7740)
Annotation(end_index=8014, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAVSm93CEfflpgEs_DTMOd8S1gLW9gbRGB0vGZvccpVeAf8Vl2_5-I2nYCCF3vyqRWa1uug-zxGrM126k79rSk516elpq6IQnJG3w9MJVU3JRCcMIZxWph327E1L_ATW2RZ3o1hGDKPlCp63h9qVa6l1l6YiYUm4TMSiJ5Qs5uIVrYsY8ASjFwH4S8rtUq9JKfVLwq', start_index=8004)
Annotation(end_index=8602, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_ghrxcja5PnD9MwDLeCttMg4ouFP_tqj3Ff-veY7_6wTgBfNvODetKhBRHZzVw_KpaBJoioV1teSsMY3z1LaVy3J7uWy6OGowoKUyf5ZyVDUuDyb-K-Py4y8hEI_WOsozuJSks3oH9YUFKqrm2FCJY54wcVX41T_4', start_index=8588)
Annotation(end_index=8602, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhBuVO-T70NDqMYiu4qZz481Spt3CS9UkVpq7dPY3D2xgGBQGnrLB8QyINYyq56PVuuDXCnvm1ped_PTLyDovN8_IR7qODTTnjS1XD1O-HejN1OEYnEbu3pGeWwj2tjoFun7lu_KI3TMXcxQ4iNeA9CM5gDCf0g627lM3Bbw==', start_index=8588)
Annotation(end_index=8757, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1X9vUPP3ArelMegfQKNIph981VPJWdSupC9zSGu24JtksUn_RD1Vs5BUW1FGAI-XTiJ7SfSRXF73jmerfgmCVDgv_Zjezu7BXNPYp6YuK80UK6gRR4GCinYMD28Y0XYKYmg==', start_index=8747)
Annotation(end_index=9081, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeFcJqsStDvQZVkI0OpAFflCG0p4eztldg3OC3d0Jg_45qBKG4KKhjaD8ebaB8aeGGzvLBOKFE022gV1vzqxrU5Cc2zQ4HGNx8gN4GFUjf3j4dp-fACfv4N8z3AqtemE_cKQ==', start_index=9067)
Annotation(end_index=9081, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHcHOWGS6Fm02Gg6KgeMIO5FDBl5mHj8lc1t_CQ_o0hIqB3KURga_d0Xup2k5iH9EgtTmJbVMAwO_TnSkg4E8c2_Yu01f2wDli24fA0UMLsMEycYLSgk1DAxXx9t1G1ojcyy9AcBGC3acSs4Qg37qNb_5XNS4njIOcxX32hDTtR', start_index=9067)
Annotation(end_index=9229, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyYDTKrgsHx-GE_58zzgFKE1pYwlZ-UlnqMXuIfNMUgIWw4KFCjX_39qqvoGA8qgyuSaciJb45duMUDJK8W738roFpqs24-L_XekV2PcajKr83hquMWEQlqMgRS9XeCgFQbmG_uUc8TfmOciowE8PE0eMCPN0vPcl7BrCkFOkSxE3Azw==', start_index=9219)
Annotation(end_index=9658, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHVx95OfIHbzzRuIxbecg279J96Wq_dx2oA5dg-qKWg64K4t8LxCfsNAYNNyhVFiC2xeTvVrbQYDYh9LyUi5w4ptCFxDRp5Y1oHsSE7HYqBatF2WJnFpReyqb57OsyM-8CX_Pn6Wv4duBY24a28KYCssw2Bh-empTv', start_index=9644)
Annotation(end_index=9658, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHumVlOnP8y9jf9Oc8Xmh6QhTHNhipeIDwbNAlSlP13d_2Js2uwibRbiCcC9xHLGIsEVhuKVJu9KGvSN8rZRE5hn__ieZWwfRHtfyjfuwzubNFr2bzHqXikF1GAOT3WXGh4BecIWiSfntvV4DBqkXwSirxenyQnuL1lWoTF9rdHAug3GQA=', start_index=9644)
Annotation(end_index=9961, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHVx95OfIHbzzRuIxbecg279J96Wq_dx2oA5dg-qKWg64K4t8LxCfsNAYNNyhVFiC2xeTvVrbQYDYh9LyUi5w4ptCFxDRp5Y1oHsSE7HYqBatF2WJnFpReyqb57OsyM-8CX_Pn6Wv4duBY24a28KYCssw2Bh-empTv', start_index=9948)
Annotation(end_index=9961, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1CD-uH0LkayOC6-JtsMuKLj6wocvvlPuh0QBR5NjLD8iBog1iCSTCgsfg7_dXAVNmyUw0nKOExPIz6zGrC_CUGRpVItur-bBai6ta3U1W8Dq81kZSq24ySdmIExj-mZTwsSJGnPiG7FjHv_t3Rk8QLGwq_yzHI0BGthzodTRk63rHNA==', start_index=9948)
Annotation(end_index=10427, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEK3G8LKPVWGQAwkWnoWpNPH-sAcRNi7El9lK0RSMTX_ueeipgIA7bxrcuZAJyeLcGAw2g0mXJ4MVVrnGlgj8rw5V68kA9-MziM0F46ufPzALGfZrOryigvYGRgCKZV9dzvBLBug4kqWskDJLDDaEmHJU9cloEv1iE=', start_index=10417)
Annotation(end_index=10611, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhQU5nyZbxHzx1eoQOKHXbuCNk6dRypamtOZo2SxfyCKaQkI8rFOrSB9uD0qkd_jtDXzLeLkvs1zeK_pOohGuhfgKPIBdGX9vOYOODv3Ez0yHFR5FMQGw_85QqdmL9K0-tbQEPq-AalhNComnpKw==', start_index=10597)
Annotation(end_index=10611, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHiPlgsP8Y377WEy8npO-mTeN_wzR2tRnfPF-d2a8cMYTlNt9PYuiNQRHQZAaUZ2Wmf1HNApicYtmh8MSFUN7-X6iKmZrJA0NDJsk7S7vUn_iQZgmZCRnp3Pv177ZS3wU3O1nSj0LvGCPO9NH6zDQrdBjn6fMQ=', start_index=10597)
Annotation(end_index=10769, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhQU5nyZbxHzx1eoQOKHXbuCNk6dRypamtOZo2SxfyCKaQkI8rFOrSB9uD0qkd_jtDXzLeLkvs1zeK_pOohGuhfgKPIBdGX9vOYOODv3Ez0yHFR5FMQGw_85QqdmL9K0-tbQEPq-AalhNComnpKw==', start_index=10759)
Annotation(end_index=11105, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBbTyux3kKwzP9MV-7B-BFZOVBSXPxa7UPpbri0DaFAAuEBc1XTGNLVWjKoUzGYCIfqHqiWWJdyWIf86AtJzTGygQyjeYF8Q3pkeJo8ocTiJNTtEyMHQg5ulVRMk_Bc0MyEAEiL0Ojz6d12rgBJMSL6k63xBqVROGEC60HA9dkQDhfKMZaqzT7bin6bP13BUYe2IKyyBQzndSZMdWw', start_index=11095)
Annotation(end_index=11379, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEokehyfdeVti2lemHyIKqF_0pL3aReFDPdE2b9vPf6T10ZvMdh3DXa5ZO4NbGGYZiuFR58o4eurXPINBB8po2cE1KZ8_8Qexoaxyx6uObY9A5v5A6hvSUrR5hcCJKNHH7t', start_index=11366)
Annotation(end_index=11379, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtS_Vl_rIzNesC5TnPaw9qbtVaaBo6fOooyMtsrL6wzZAmTWcoVh1qP_vNMcxnqNZOHxaP5sD0WiMN35bIu_o0DscqgFoOn5qis52R6Howx87NyNnsFGZiyRWXu_Ul8V_0zm4cJUPXCcdlPi5uS1OMlxzNYdoTDOEawkjRo9lQGe82x17HU4g=', start_index=11366)
Annotation(end_index=11992, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlGf71HaWFTR-F1bwzXipdzsnh2Q_3r4LtBaB7nVGaNyqe-KALR_RuN5E4Y-4ebiSh9zjAjyeSD53hnuVtkQUihXW2GmRCe2TxDDkfK4K2T3LEvusPCWTJn_DHZ2k6F4nZAYd94oPL6wNZz5OZR8GgQXZBicf3HLKHzS12lwSGZbezYTf9rFkzTYvh3mvMs1TBbDNTXI6Uc7iVtgrflUG_lR9GBM5hlvIn39j0RQbVZSBjxNt2Lj-Y', start_index=11982)
Annotation(end_index=12230, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_VjkDxxho1tbAAgNtk94Ysxb-mfEpL2sTNyL-fmd6_UcgF4l1rRNunIV0C-TcbNkrnLRTM_p8DHd62rDr4JjhtlQWD1D3gQyesveog6iuKbTACteWYMQm6vOayMGbfiftWONPexihsiGNdA==', start_index=12221)
Annotation(end_index=12701, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGPjqiz1IjtYj3thnO8ztfi0DdfBoWCI4tA4to7WYxlrbPGxFWMgoAJKUdkuGGhLesCAC4jUtt3CLBSLPky9RIKnOtREizX_5r4tHrj0KXs75GV4Vq0LMAuBZDMk7MPgmo6wigF7bpwQrbSwY6_n_vJ6ruGGP5-_phj-R68jm4ZGN231sleTQULJnCGhPi3Q32XoB3ZpUhWA==', start_index=12687)
Annotation(end_index=12701, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4fB-RjfBhGLjtVVIdfMCzzTuh0G0MjhdEdGYqyo-XkG5ftRSMvxC2Ld8KGeYAJzvjgl5SareM4w_NDMlVb6rqvMW7FfL6qjxF8HJUUqzkdVwigQNAyvL_8Os0tIJXm6v2TwB9yI9o7XyV_mKKvYQDV_uiTuFUgn5jdm11JSfy4L7-gcEI-hWG3L4p', start_index=12687)
Annotation(end_index=13961, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEokehyfdeVti2lemHyIKqF_0pL3aReFDPdE2b9vPf6T10ZvMdh3DXa5ZO4NbGGYZiuFR58o4eurXPINBB8po2cE1KZ8_8Qexoaxyx6uObY9A5v5A6hvSUrR5hcCJKNHH7t', start_index=13952)
Annotation(end_index=14014, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5iOpGBCbGaG8DgNvqvsASCy09XkMrwTIXCfSsX7OKL8UqY24BiKCugxyK6GlR4T9K7KoYOZHUdLACpGHK0BbAmWm6CLtk8AMyjVbBDgGRovwsT_eCobgjChpg__3IJVxOtyO03yWRsex985HXQoXC4o9ThKjZPkXuk7oUBjqlaH8eCGJs-Gp3uXewJ_3I_Wl4pLBDgx-zEXc=', start_index=14005)
Annotation(end_index=14113, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEK3G8LKPVWGQAwkWnoWpNPH-sAcRNi7El9lK0RSMTX_ueeipgIA7bxrcuZAJyeLcGAw2g0mXJ4MVVrnGlgj8rw5V68kA9-MziM0F46ufPzALGfZrOryigvYGRgCKZV9dzvBLBug4kqWskDJLDDaEmHJU9cloEv1iE=', start_index=14103)
Annotation(end_index=14178, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_VjkDxxho1tbAAgNtk94Ysxb-mfEpL2sTNyL-fmd6_UcgF4l1rRNunIV0C-TcbNkrnLRTM_p8DHd62rDr4JjhtlQWD1D3gQyesveog6iuKbTACteWYMQm6vOayMGbfiftWONPexihsiGNdA==', start_index=14169)
Annotation(end_index=14240, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG4fB-RjfBhGLjtVVIdfMCzzTuh0G0MjhdEdGYqyo-XkG5ftRSMvxC2Ld8KGeYAJzvjgl5SareM4w_NDMlVb6rqvMW7FfL6qjxF8HJUUqzkdVwigQNAyvL_8Os0tIJXm6v2TwB9yI9o7XyV_mKKvYQDV_uiTuFUgn5jdm11JSfy4L7-gcEI-hWG3L4p', start_index=14230)
Annotation(end_index=14313, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHo8DhYVEtUkPPPggz7H9voc6z_ewjslmKPsl1stmozpTLJ0m-mGiXZIt8tASCzY--PMPwoBPuGtIi28BbmkxZ9gL_9YvMNSdbYfakyZ_eZsj53mLGnb4WzmU8p7RCS6q9YhUaC5VPJLIatnimboVOMeepbyKVHrIA=', start_index=14303)
Annotation(end_index=14387, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHVx95OfIHbzzRuIxbecg279J96Wq_dx2oA5dg-qKWg64K4t8LxCfsNAYNNyhVFiC2xeTvVrbQYDYh9LyUi5w4ptCFxDRp5Y1oHsSE7HYqBatF2WJnFpReyqb57OsyM-8CX_Pn6Wv4duBY24a28KYCssw2Bh-empTv', start_index=14377)
Annotation(end_index=14461, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1CD-uH0LkayOC6-JtsMuKLj6wocvvlPuh0QBR5NjLD8iBog1iCSTCgsfg7_dXAVNmyUw0nKOExPIz6zGrC_CUGRpVItur-bBai6ta3U1W8Dq81kZSq24ySdmIExj-mZTwsSJGnPiG7FjHv_t3Rk8QLGwq_yzHI0BGthzodTRk63rHNA==', start_index=14452)
Annotation(end_index=14548, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGROj_MKmFCzbn79DJ9mlSZZFyeVPEX7RVXLIjndEJDUq61Ta2DgF40SKLN4wOUqNceTCQvKPOadx1VqWZcC28uQSGUy4vtDlOFXTcSo5tasItLpwYve_rZ88RDeD7NE7hvMAylp615HThBr7LF7MIZIz-GAjnJUcWeDEGlaCRE1LhlmNW4ljtBL_LeHxm5pzOr4R8GjD-L-NqBExwI-OOhzxObJOxJYCKCAA9AMeGNrQ-KCd-FFazsUp6WVBDz8JGPoF50PC9ReYC3L5rlhsrr', start_index=14539)
Annotation(end_index=14614, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEahCNz1GBbZCp87BLSph8yBpw18RBNAAA2MrtfElSnCf6QWv6aourSAHQVO4Lop3vcT81cLLoFYxPZB-9z6QLS0unWde4egpHHV6uYZBLdEZJxVXVKkT6AP5oZd7OpERl9hXu_H31WiTxe6_zdgU41mv1fLlqPc3Se7sU471CaJa76dAYiJbtV1z-QihHQ2RbMGKb5L-aWtkPTQVmeTbNIsDIyUnRpFkCW0ooCOHsRJuzYzQfPK6t1KDgxFx-RKaEwcTPPDov7', start_index=14605)
Annotation(end_index=14664, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIn4y7G2t203ve7Ag3QUWBaxkBKPTBu8eO3sXWIkXTHsATgBoKbr8k5vB30KQ0tcKMyVHeXHvrVAekS2b89RRbSsfeXyE52UwEKiXvuAeh-I62sxWFJ1pysgm4bRwcOhSDYzB5Vgepco7D2NhnVteMrEQq2qQgvyPEqeXQ4aYpYcfhyG1DNg==', start_index=14655)
Annotation(end_index=14742, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJdY0T196J59QTuhBcUSn9pK_FvxwPb5F9lQUsm1zpJmpAwXSM5vhd6VD1ExNDtCAkXd3HmQihiAojhSYa9NlujHRV2NOXQdrepDilrnJfJRFjdsExPXlDbHbRBX-ziNhKARGA0NU-3g7LWzO6Vv4lyNnRRS4Xwcm1b8Q6', start_index=14732)
Annotation(end_index=14824, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEq2PhaYeS5Q8f0udjxbYd5bW0IPLMdg_QcE_7sgbep2QyCSERuX868awsALQ5ZSvn0Ybt5hpZ_1qjWlZb_XmByKF73HESakxMzfx7CtPa6Fw0SWL2wUVgvfzhhuiMPa7IJwBRoj7L9LeiObhg30eYax9ye-jMuBdU=', start_index=14814)
Annotation(end_index=14897, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtrPHNuPz_bDbBA_yltizu5CNThTWi6C4EJANdpaLDx5wfVyHBeb_5wmGC9BIfbPe8QtGXO3ik4xfKt4e_uW0FPAoN1x0jFwZul7vOTwJ5yPzGoxQdtju5-d0UFm5vX647_vwgZoqoN2Qo610WqbMH7WUd5DtKnPq-', start_index=14887)
Annotation(end_index=14974, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlGf71HaWFTR-F1bwzXipdzsnh2Q_3r4LtBaB7nVGaNyqe-KALR_RuN5E4Y-4ebiSh9zjAjyeSD53hnuVtkQUihXW2GmRCe2TxDDkfK4K2T3LEvusPCWTJn_DHZ2k6F4nZAYd94oPL6wNZz5OZR8GgQXZBicf3HLKHzS12lwSGZbezYTf9rFkzTYvh3mvMs1TBbDNTXI6Uc7iVtgrflUG_lR9GBM5hlvIn39j0RQbVZSBjxNt2Lj-Y', start_index=14964)
Annotation(end_index=15077, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHcjPnzpbYhyvUi5GudUSJHhYks83sP_GSNh0LptlK1uTO7AybGHJ0FeiXtz-nNHGOyBtdrxyRuvN-jJaZqMfc55QCasRq2aVnaXRp5JBL38YMHXQwDIo53MES2_h5BZU1o22j1EiH5-UL5AuE0GG8apCKltT_tUWYn2ujsyWg_A==', start_index=15067)
Annotation(end_index=15159, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH60GDpj5-Ah_y5I9LynknF9IGym7KMbOW3rZiOETz-SyDUdF-ly9L9yiTp00cpBsunU7GMPnIEGaH4D7Cs08sDTFa9VqgNSsrk6pJrsXPO72FDzFpSfUY1FLqISA55zaaCS65cUtZeFxNnU4nZkkqX9Z6P6jbXRZCq', start_index=15149)
Annotation(end_index=15234, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_ghrxcja5PnD9MwDLeCttMg4ouFP_tqj3Ff-veY7_6wTgBfNvODetKhBRHZzVw_KpaBJoioV1teSsMY3z1LaVy3J7uWy6OGowoKUyf5ZyVDUuDyb-K-Py4y8hEI_WOsozuJSks3oH9YUFKqrm2FCJY54wcVX41T_4', start_index=15224)
Annotation(end_index=15309, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeFcJqsStDvQZVkI0OpAFflCG0p4eztldg3OC3d0Jg_45qBKG4KKhjaD8ebaB8aeGGzvLBOKFE022gV1vzqxrU5Cc2zQ4HGNx8gN4GFUjf3j4dp-fACfv4N8z3AqtemE_cKQ==', start_index=15299)

## Sources
