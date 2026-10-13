# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 469308fc | **Time:** 395.88s | **Cost:** $2.37933
--------------------------------------------------------------------------------

# The Privacy-Utility Frontier in P2P Credit Scoring: Federated Learning, Gradient Leakage, and the Limits of Behavioral Confidentiality

### Key Points
*   **The Optimization Gap:** Current Peer-to-Peer (P2P) credit scoring algorithms do not yet achieve an optimal balance between default prediction and privacy; they exist on a Pareto frontier where increasing one variable typically degrades the other.
*   **Federated Learning (FL) Adoption:** Major financial entities (e.g., WeBank, and increasingly P2P platforms) are adopting Federated Learning to train risk models across decentralized data silos without sharing raw borrower data, driven by regulations like GDPR and CCPA.
*   **The Reality of Leakage:** Research confirms that gradient aggregation is not perfectly private. Sophisticated attacks, particularly **TabLeak** and optimization-based gradient inversion, can reconstruct tabular financial data and behavioral patterns (e.g., transaction histories) from shared model updates.
*   **Behavioral Pattern Exposure:** While FL prevents direct data access, "behavioral patterns" are inevitably encoded in gradients to improve prediction accuracy. Adversaries can exploit this to infer sensitive attributes (e.g., spending habits, financial distress indicators) unless rigorous, utility-damaging defenses like Differential Privacy are applied.

### Executive Summary
The digitization of financial services has compelled Peer-to-Peer (P2P) lending platforms to transition from traditional logistic regression models to complex machine learning architectures (e.g., XGBoost, Neural Networks) to minimize default rates. Simultaneously, regulatory frameworks such as the General Data Protection Regulation (GDPR) and the California Consumer Privacy Act (CCPA) have imposed strict constraints on data centralization. Federated Learning (FL) has emerged as the primary architectural solution, promising to train robust credit scoring models while keeping sensitive data localized on client devices or institutional silos.

However, the premise that FL provides a "firewall" for privacy is increasingly challenged by adversarial machine learning research. Evidence suggests that the gradients—the numerical updates shared during FL training—carry sufficient information to reconstruct the underlying training data. In the context of credit scoring, which relies heavily on tabular data (financial records, demographics) and behavioral sequences (transaction histories), specific attacks like **TabLeak** have demonstrated high success rates in recovering private information. Consequently, the current state of P2P credit scoring represents a trade-off rather than an optimal balance: while FL mitigates the risk of massive centralized data breaches, it introduces a new vector of "gradient leakage" where behavioral patterns can be inferred, rendering the privacy protection incomplete without sacrificing the predictive accuracy essential for platform stability.

---

## 1. Introduction: The Dual Mandate of P2P Lending

Peer-to-Peer (P2P) lending platforms operate in a high-risk environment characterized by information asymmetry. Unlike traditional banks, which often hold long-term relationships and collateral, P2P platforms must assess the creditworthiness of borrowers—often "credit invisible" or high-risk individuals—using available data points to predict the likelihood of default [cite: 1, 2]. The stability of these platforms hinges on the accuracy of their default prediction models; even marginal improvements in predictive performance can significantly reduce financial exposure and enhance platform sustainability [cite: 3].

### 1.1 The Evolution of Credit Scoring Algorithms
Historically, credit evaluation relied on statistical techniques such as Logistic Regression (LR) and Linear Discriminant Analysis (LDA) [cite: 1, 3]. However, the assumption of linear relationships in these models limited their effectiveness in capturing complex financial behaviors. Modern P2P platforms have shifted toward advanced Artificial Intelligence (AI) and Machine Learning (ML) models.
*   **Ensemble Methods:** Algorithms like Random Forest, XGBoost, and LightGBM are now standard, offering superior performance in handling non-linear relationships and high-dimensional data [cite: 1, 3, 4].
*   **Deep Learning:** Neural networks, including Multilayer Perceptrons (MLP) and Long Short-Term Memory (LSTM) networks, are increasingly used to analyze sequential data, such as transaction histories and behavioral footprints [cite: 5, 6, 7].

### 1.2 The Privacy Imperative
As algorithms become more data-hungry, privacy concerns have escalated. P2P platforms utilize not only traditional financial data but also "alternative data" including social media activity, digital footprints, and mobile device usage to assess risk [cite: 8, 9, 10]. This accumulation of sensitive Personal Identifiable Information (PII) creates significant liability under privacy laws.
*   **Regulatory Pressure:** The GDPR in Europe and CCPA in California mandate data minimization and restrict the cross-border or cross-institution pooling of data [cite: 11, 12, 13].
*   **The Data Silo Problem:** Financial institutions and data providers are often legally or competitively barred from sharing the raw data necessary to train comprehensive risk models, leading to "data islands" that hinder model accuracy [cite: 14, 15].

To resolve the conflict between the need for massive datasets to train accurate models and the legal requirement to protect data privacy, the financial industry is turning to Federated Learning.

---

## 2. Federated Learning in Financial Risk Management

Federated Learning (FL) is a distributed machine learning paradigm that enables collaborative model training without exchanging raw data. Instead of centralizing data, the model travels to the data.

### 2.1 The Mechanics of FL in Credit Scoring
In a typical FL setup for credit scoring (often referred to as "Federated Credit Scoring"), the process follows these steps:
1.  **Initialization:** A central server (e.g., the P2P platform or a credit bureau) initializes a global credit scoring model [cite: 16].
2.  **Local Training:** Participating nodes (e.g., individual borrowers' devices, partner banks, or data furnishers) download the model and train it locally using their private financial data [cite: 17, 18].
3.  **Gradient/Update Sharing:** Instead of sending data, clients compute "gradients" (directions in which the model parameters should change to reduce error) or model weight updates. These updates are encrypted and sent to the central server [cite: 16, 18].
4.  **Aggregation:** The server aggregates these updates (e.g., using Federated Averaging or FedAvg) to improve the global model, which is then redistributed to clients [cite: 16, 19].

### 2.2 Adoption and Real-World Implementation
The adoption of FL in the financial sector is moving from theoretical exploration to production, driven by the need to leverage data silos.
*   **WeBank's FATE:** WeBank, a digital bank in China, has pioneered the industrial application of FL through its "Federated AI Technology Enabler" (FATE) framework. They use FL to collaborate with invoice centers and other banks to assess the credit risk of small and micro-enterprises. This approach reportedly increased the effectiveness of their risk control model by 12% and reduced costs significantly [cite: 14, 15, 20].
*   **Cross-Silo Collaboration:** FL allows P2P platforms to collaborate with other financial institutions. For instance, a P2P lender could train a model on data held by a traditional bank without ever seeing the bank's customer list, thereby overcoming the "cold start" problem for new borrowers [cite: 14].
*   **Vertical vs. Horizontal FL:**
    *   *Horizontal FL:* Entities with the same data features but different users (e.g., two regional banks) collaborate to increase sample size [cite: 21].
    *   *Vertical FL:* Entities with the same users but different data features (e.g., a bank and an e-commerce platform) collaborate to enrich the feature set for credit scoring [cite: 21, 22].

---

## 3. The Vulnerability: Gradient Leakage and Behavioral Inference

The central premise of the user's query is whether FL *inevitably* leaks behavioral patterns. While FL eliminates the transfer of raw data, research into "Gradient Inversion Attacks" (GIAs) demonstrates that the gradients themselves contain deep imprints of the training data.

### 3.1 The Mechanics of Gradient Leakage
Gradient leakage attacks exploit the relationship between the model's input data and the resulting gradient updates.
*   **Optimization-Based Attacks:** Attacks like Deep Leakage from Gradients (DLG) formulate data reconstruction as an optimization problem. The attacker (often a malicious or honest-but-curious server) starts with "dummy" data and iteratively adjusts it until the gradients produced by the dummy data match the gradients received from the victim client [cite: 18, 23].
*   **Analytical Attacks:** In some cases, specifically with fully connected layers common in the initial stages of neural networks, inputs can be mathematically recovered from gradients using closed-form solutions, without the need for iterative optimization [cite: 24].

### 3.2 TabLeak: The Specific Threat to Financial Data
Most early research on gradient leakage focused on images. However, credit scoring relies on **tabular data** (categorical and continuous variables mixed together). Reconstructing tabular data is uniquely challenging due to the mix of discrete (e.g., loan purpose, zip code) and continuous (e.g., income, debt-to-income ratio) features.
*   **The TabLeak Attack:** Recent research has introduced **TabLeak**, a comprehensive reconstruction attack specifically designed for tabular data in FL. It utilizes a softmax relaxation to handle discrete variables and a pooled ensembling scheme to reduce variance.
*   **Efficacy:** Experiments on standard datasets (like the "Adult" census dataset used for income prediction) show that TabLeak can extract large subsets of private data with **>90% accuracy**, even at batch sizes as large as 128 [cite: 25, 26, 27].
*   **Implication:** This directly contradicts the assumption that aggregating updates over a "batch" of users protects individual privacy. For P2P platforms, this means a server could potentially reconstruct the exact financial profile of a borrower from the model updates sent during training.

### 3.3 Leaking Behavioral Patterns and Transaction Histories
The query specifically asks about "behavioral patterns." In modern credit scoring, this often refers to transaction sequences or time-series data processed by Recurrent Neural Networks (RNNs) or LSTMs [cite: 5, 6].
*   **Reconstructing Sequences:** Research indicates that gradients from sequential models (like those used to analyze transaction histories) can also be inverted. If a user's transaction history is used to update an RNN, the gradients of the recurrent layers capture the temporal dependencies of that history [cite: 28, 29].
*   **Linear Inverse Problems:** Independent research has shown that individual item prices and spending habits can be recovered from aggregate transaction metrics (sums) through linear inverse problems. This is analogous to recovering individual gradient contributions from an aggregated update [cite: 30, 31].
*   **Inference of Attributes:** Even if full reconstruction fails, "property inference attacks" can determine whether a specific behavioral pattern (e.g., "frequent gambling transactions" or "high medical expenses") was present in the training data [cite: 18, 32].

### 3.4 The Malicious Server Threat
The threat model is exacerbated if the P2P platform (the server) is malicious. A malicious server can manipulate the global model sent to clients—for example, by modifying the architecture or parameters—to force the client's local training to produce gradients that are easier to invert. This allows the server to bypass protections like secure aggregation or large batch sizes [cite: 18, 24].

---

## 4. The Privacy-Utility Trade-off: Is an Optimal Balance Possible?

The "No Free Lunch" (NFL) theorem for federated learning posits that it is unrealistic to expect an algorithm to simultaneously provide excellent privacy, utility (accuracy), and efficiency [cite: 33].

### 4.1 Differential Privacy (DP) as a Double-Edged Sword
To prevent gradient leakage, platforms can employ Differential Privacy (DP). DP involves clipping gradients and adding Gaussian noise to the updates before they are shared [cite: 34, 35].
*   **The Trade-off:** While DP provides a theoretical guarantee against data reconstruction, it directly degrades the accuracy of the default prediction model.
    *   **High Noise (Strong Privacy):** Prevents TabLeak and other attacks but renders the credit score less predictive, potentially destabilizing the P2P platform by failing to identify defaulters [cite: 35].
    *   **Low Noise (High Utility):** Preserves the accuracy of models like XGBoost or LightGBM but leaves the system vulnerable to reconstruction attacks [cite: 34, 36].
*   **Impact on Fairness:** Research indicates that applying DP can disproportionately affect the accuracy of the model for minority groups (e.g., "thin-file" borrowers), exacerbating fairness issues in credit scoring [cite: 37, 38, 39].

### 4.2 Secure Multi-Party Computation (SMPC)
SMPC allows the server to aggregate gradients without ever seeing the individual updates (only the final sum).
*   **Limitations:** While SMPC protects against the server seeing *individual* gradients, it does not prevent the *aggregated* model from memorizing and leaking data, nor does it prevent inference attacks if the server colludes with other participants or if the aggregate itself leaks information about the distribution [cite: 22, 40]. Furthermore, SMPC is computationally expensive and complex to implement for high-frequency lending platforms [cite: 38].

### 4.3 The "Optimal" Balance
Current research suggests that an "optimal" balance is not a static point but a frontier.
*   **Pareto Frontier:** There is a "privacy-utility frontier." For a given level of default prediction accuracy (e.g., AUC of 0.85), there is a maximum level of privacy protection achievable. Moving beyond this requires sacrificing revenue (due to defaults) or accepting higher privacy risks [cite: 33, 36].
*   **Current State:** Most industrial implementations (like WeBank's FATE) prioritize utility and efficiency, using encryption (Homomorphic Encryption) to protect transit but relying on the assumption that gradients are "safe enough" from reconstruction. However, the emergence of attacks like TabLeak suggests that this assumption is flawed for tabular financial data [cite: 15, 25].

---

## 5. Regulatory and Ethical Implications

The tension between default prediction and privacy is not just technical but legal.

### 5.1 GDPR and the "Personal Data" Debate
Under GDPR, if gradients can be used to reconstruct the original data (as shown by TabLeak), they may be classified as "personal data." This would mean that even FL systems are processing personal data and must comply with strict consent and minimization rules [cite: 41].
*   **The Regulator's Paradox:** Regulators demand **fairness** (which often requires more data to ensure models work for all demographics), **privacy** (data minimization), and **accuracy** (safety and soundness of the financial system). Achieving all three simultaneously in a federated setting is mathematically difficult [cite: 42].

### 5.2 CCPA and Data Sales
The CCPA restricts the "sale" of data. If a P2P platform uses FL to train a model on a partner's data, and that model "leaks" information back to the platform (which improves its own commercial product), this could be construed as a data sale or transfer, triggering opt-out rights [cite: 12, 13].

---

## 6. Conclusion

Does the credit scoring algorithm of P2P platforms achieve an optimal balance? **No.** The current landscape is defined by a necessary but imperfect compromise.

1.  **Default Prediction vs. Privacy:** P2P platforms have successfully leveraged AI (XGBoost, Neural Networks) to improve default prediction. Federated Learning has allowed them to expand this capability across data silos without direct data sharing. However, this utility comes at the cost of residual privacy risks.
2.  **Inevitability of Leakage:** The leakage of behavioral patterns via gradient aggregation is **effectively inevitable** in the absence of aggressive Differential Privacy.
    *   Financial data (tabular, high-dimensional) is susceptible to reconstruction attacks like **TabLeak**.
    *   Behavioral patterns (transaction sequences) are embedded in the gradients of RNNs/LSTMs and can be recovered by optimization-based attacks.
    *   While defenses exist (DP, SMPC), they impose a "tax" on accuracy that many platforms may find unacceptable given the thin margins and high risks of P2P lending.

**Final Verdict:** The industry is currently in a phase of "security through obscurity" regarding gradient leakage. While FL is a significant improvement over centralized data pooling, it does not provide an impermeable shield. As attack methods mature, P2P platforms will likely be forced to adopt stricter Differential Privacy measures, accepting lower predictive accuracy as the price for genuine behavioral confidentiality.

---

## References

*   **[cite: 3]** *Benchmarking Bayesian Optimization Frameworks for Credit Risk Prediction.* (Source 1)
*   **[cite: 1]** *P2P Lending Default Prediction Based on AI and Statistical Models.* (Source 2)
*   **[cite: 43]** *Fast Gradient Leakage (FGL) in Federated Learning.* (Source 4)
*   **[cite: 8]** *P2P Lending Default Prediction Model with Social Media Data.* (Source 5)
*   **[cite: 17]** *Federated Learning for Privacy-Preserving AI.* (Source 10)
*   **[cite: 22]** *Federated Learning for Privacy-Preserving AI (CACM).* (Source 12)
*   **[cite: 18]** *Gradient Inversion Attacks in Federated Learning.* (Source 15)
*   **[cite: 34]** *Gradient-Leakage Resilient Federated Learning.* (Source 18)
*   **[cite: 25]** *TabLeak: Tabular Data Leakage in Federated Learning.* (Source 21)
*   **[cite: 26]** *TabLeak: Challenges in Tabular Data Reconstruction.* (Source 23)
*   **[cite: 33]** *No-Free-Lunch Theorem for Federated Learning.* (Source 25)
*   **[cite: 16]** *Federated Credit Scoring (OpenMined).* (Source 30)
*   **[cite: 5]** *Federated Learning for Credit Card Fraud Detection.* (Source 31)
*   **[cite: 30]** *Recovering Item Prices from Transaction Histories.* (Source 35)
*   **[cite: 14]** *WeBank and Federated Learning.* (Source 49)
*   **[cite: 44]** *FATE: Federated AI Technology Enabler.* (Source 50)
*   **[cite: 41]** *Benefits and Challenges of FL under GDPR.* (Source 63)
*   **[cite: 42]** *Evaluating Credit Records with Federated Learning.* (Source 65)
*   **[cite: 24]** *Malicious Server Attacks in Federated Learning.* (Source 74)
*   **[cite: 27]** *TabLeak: Comprehensive Reconstruction Attack.* (Source 81)
*   **[cite: 45]** *WeBank's Credit Risk Management.* (Source 85)
*   **[cite: 38]** *Differential Privacy vs. Fairness in FL.* (Source 90)
*   **[cite: 35]** *Differential Privacy in Federated Models.* (Source 92)
*   **[cite: 26]** *TabLeak Accuracy on Financial Data.* (Source 102)

**Sources:**
1. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHCS8vryIZ-c2Ku_iJ7sMCj34CmIKp-rQcvgcxnJs91QDTltIdgeYCXo65CW35eWPOgD0NEP3Hlcy_iJsKb3VLta7Sughz0IEd_4xX0VjMIM9_p4dASde4Aj9TtQ==)
2. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHQBiT9qkOHutVcu8aquK7AcrOJMJRjkHNJFTsAcm-17DiTR3YrkmuzHQNOpFXAever52iZ-_Thfxi-0fx2HaJceM9DwH0DHMYC7slHpDYdRFmZoTNwwKrZagL6l-dVsdftO6lAARzvIKKVrdS1Qn3)
3. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMjwfoT3M22i3YwlWYj6zEXQhJB_jUfv2yLmldR9mToO4J8EwJ15VnkZzUjWaostY9iRNZe0J7ursHFENqPOgr2uquUTH1y89ckQRGyYt6ksLuPTYweXhgb5E=)
4. [aimspress.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaONxXFbz9YRN38c0-XkcWr69SGHu1N6g0G1NeSRjASCrC83WvdBTwswEuee6-86fPFpIufvlL9Ftp2kxjKuYLad9_Ye-yFl_4B5kCp6aSRlV7hBC5ueDZNrLuWzKEqHdjqWclKT0M1nPdif-3RchCclE=)
5. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8G5rLEt202R4DfjVjZf-lv7_ZGKyG0So5Jz00nzg1vlszqaGU0Q0-M9I533LLYd83WsH8hH4auSyue3_HuOAXiWRT4mNf5pKBrKU917zw1M7fFS73t3cf3RfM2Jw=)
6. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzS70uLxP__VxkVtRhMtg7N7Qcc_V5UQecLScS3Gk0Om_R8_TlCHgFJE85yxxYPhXWB0H9VqPSsQOJaVitFFNwPPDOjUn3YCfsVok6HzvHtICUzEoUvtcg)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpVDD-EKACFn4SEmW6vf2ojqN1yIC9xJlm-HYckA_cr9PdMYvNw1mBkiAHxL8qqI725XouGzu2Rhcndq3VCgDexQFg0-HxYHPvvkrpR9fC3YZiS7kJPfZR-4CmG2fD2daO3TOji31ZfbiglqyXRPbTrp0jL0zsX9O_7tu0DqU51a1m5mEOyllXmP0PcTL63SZYC8VL4_JLZA4lqleALk4Y_2cOYIYytii9kvGot-FNycim0zM=)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5MsfbTajvB1fM6rB579px-gQUQfVacseXtP_cpM18Dyq-fvgRHN-Qn6ehemMpiKGe7fRf7YpSD2vmN4hFVDWbg2j0_ToHTNLBPPqTSzwT_fnOv2MxvCAl5JO2WMG3XwyygPwqDaIgWlUmc_hS35wnw84DalLjlYmkYIcO13fbmlCy0P-VTH27MVgdjJUJH2Eu3iwegA458-w-0rknsK5OuZ0rfToIQ9CFUlAOIR5IFrHqQwPy13zQPdhqJ6WbWkRFuLzWokoteLmWlg==)
9. [ed.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlJihxFTYrgI2niT34zMx6ko7Dd7a2IksFl9RrRSCrHvqlyK_eEIfnlvoHfupHXCXG0s9oAJYprordVTitmLhoGsNCaspcqVk24tvJzANb7wBwhSEwUHhHqf4iXkFyrsGjOYhang==)
10. [fdic.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAOPJDaI-Sig4bfgnNPpZr-D_VZG00MIr8SB71tCt4PmCFTBlK7CPMYWBDDqQbTucSWMUMRQ_t9CCRnLBdJlxIBwaWOmBoI_BrUimmLMNdMytnpRqqfs-f_d914EdvpGNOnJaIeNULQUAT4WeiphKG)
11. [brankas.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgxRk9q46Yu7MijAXJ7MZ2xeJoPXZf7Y28xmrHLvNB8HO3mjwdWnI4pPXWCsNYUGJFEyyWSY92McwAVSxOpjcAVlNxPfjgPTK1KJPsDOBgJMInZ41yUKGgE-l6DO7tkiLGck1LbMNobUGNMvYsEjKPCczmrYeSbf56r3mL1X-0X3r-)
12. [udig.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBGFe4RMcS4_AR4isnsVEswVN0vvAChx7detTUW_Hl-OHJ13B3gSr4fYYuv3C6kzjh3EHDGjvjvDAQUPg7c8d4TUbGS97gNDGO3Kcl0LMMMkutRsRmz5QEbEMktdsl7KGDp_DWhyVWMHcyestUlv-sYaDZNb-14w==)
13. [aeaweb.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXBS5chaX9Iu8nLLwX-dhlUtJXLBnzg62yuH7iIFU9_iCfCVRI_1crCrKfPg8OKSlrQlX8wbsG9jjoDDsPZNGm7Wk5PKT69dzYb0tCcw8Lp6QofXWNXVZYpyEMx1ASiXg32MkprwIgqu4TNZEeveJ4lp4=)
14. [digfingroup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdEbKgq-N9tTpnZXz5CQOpJM8ePv2AJVt4cWNEylU6geVUHvZq9-B44iXqGgN2-QxzO0z-idl3IPOZL8Vbs0xvCaJxM0TOuzl0Smktek2O6NDle0GvdKrk5xLTZZp1akY=)
15. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIKR4xrm61aXTkAlboFROHU2iIhpwvBaQp1ZGjd27YMMYTohpwDMOcF3j8MP-XPyc4B7_SRYW4SjqmRgZfH7T74aF1tZOCSUA9SlL1H7yBGCFTxOETKddIwGtXYMQMOpU1nhOBMJwBsURJWH-vufcz4VtBS-BAhogyEDXqB7DpaegZSAa-thm906SuEzQHeZC5A05NPYWlGAuLGqvIRaAtFSyovZzpmUA13j7KyIeV)
16. [openmined.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElqfYKU81GBAg1K3BEZ0Mqx4grkNP3x_tCP0lSXCZA_TsQosMbyxh9JyLVSeZ-jJFdQVFzBBHDpN14DLWZYP5rm2rgJhxDkFi4RnV9YsDEH4sQC92zYfMm2cNeVgjOn-6dxcxdhRg-7a0=)
17. [datascience.salon](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxNT26BfE876CexgMND0vLo8e20-XiQcnKu3G9P9nxjcXdFl44fwNaUuwCLGohuUn4s-dS5X_z3f_WAH02t5pfaUbJselH_SEaAq5kqJGQpjM3wLoTBbPhC5RvcQ5K4VS-ziT6ztvqKWhE-T7ZyPeYLVEyRmOYWMO6_Nx98q7wQ2RtRBjSe0yYHQrPqKKF6DmNksZBRADs5ybVdlRlEg==)
18. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErZHGTcSqqbne24zbFulRFYz14B95024JLz9T2XDVc9r9z6sab6R0FXVS6ibMAcnlk9bOkNtL9LPG-LI6uzgqPoG1FfUh9AJMSsRWZPt-mychZSHFtj8-d)
19. [itm-conferences.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8-q55DlfUW6ESOyH6M6a3gs5n_sjV1JSbxWicXX0BqFwZpq1DzwwGiJOOBGHODyZSRa6JbE4CXNI1YebWe8BHa7865f4JXWzRpM3OkLMgHv7gk69ylzVokw11kvaY6fnZ6o8qpzNJX2mPUd-z205Xt4bN1s8NP6UikC4Kp3wxIQJixFx0Wrf0soga52H8imBWe64X7l5YEApy005ibSFNDHY=)
20. [intel.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFMfD1XW-MxM9MkqOEgRwu47Z90k9W2bbBB5vNPA2QTKgOEhA2NEQwFhhu2VN_x_QbE7aPneHxcic_x3r2-pLrJqtzT2pnXJRWbzoXGv9A5PxeoAtZvxLvgWOk0TBe541gS98eBLungzKndzFtiC9nTwopnJ3CxRFriTWlgcKFabHkP9zkoE8ZzRVjWquc_FliXy60t7F10AYhZqOio9vdeFDzVWD4CblGNA==)
21. [openmined.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEx22aXE97pKoOii9IBPRxQ2TRJ6XYUE2OrwOCxIXHnplIBtMacY80-G9LNH3PcqwsdROFrWe8-XD00jxjHX7gDhwmgqaZ3n-OWYkU1ukxmTdYitebUArH_nM5iit_Zew_X4EABaebzRIg=)
22. [acm.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpSjI10E-RMxEtmjX4WUH1XSdZiNvPUTXpModd-bAOLoqv1cyID08v5cvUG8lOEUpEHCRi-Pm-MlemOivUbC8QOnMgMS_i4enbx94MjKdz58lA65ensr1xnxJ_8z4b0bNoR9ZB1_7j4KNGPky15oAn0kHHnv-iiH1s_cr25Eno)
23. [toronto.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0VX0jiqtYKbxoUeZjD5BI4qy4lUDYTIj1zgF-N6H6N92qiptaICdkxc4HARaa2W4ODE9Pjc0zXGVX1IDJGyK_N1GbSpa1gvQTUnqS4uB_q_QCTJEK7XtqoR6q8WE6XjAAj5kKp4zy0fbEjGxJ1p0Poxe_NljIQInOsol1xB1VvtH_)
24. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJNy6Wr-3xcPqXI_yteys1dDd_YdH5qUYVQraj3_q3G7XglGLdKbTNHPN4_N7NRa3-0LPXaPVdOhrDgsw-MOpWaRp4fNvrSMmcBDD65ZHk6N7f8UYNkryk)
25. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOoL5dQwVFjdqZ-IA4StM7znDlnWG4qte2FWGyzUF1JbJn7AWOtSl1B-30sD4zIqXAu842kjPZm7kKE6x5n3FU-J0ht2cxb1dtZ3TyzbnB40fuEbD0A4i7nYvOnsw4cEhC5KllqSdusD9X6rIjjMXemF3AXfoMK091ihNMUTddb4rkRNlVmghvzMtoNtAzHUwO8w==)
26. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGocOFrdK_fqoWPNBVX4D9nUyEJKMn6AhIpiBeNn4YFlUKifu0G2D1TMr8BoOcAreL6x7_F_uGsfH5cml0pIMwsk_g7_2mnoh1QTk1-4okd4Lx9_rbX)
27. [mlr.press](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwpPGpZ2fpHjCjZ4cm8ttN6_LOohA96fPN2T3G5nkX4U6r5ERX2L2LWgs8c9VoOYqmVSmzwHRWshwJDsB5Li6T-O_LtZkHuv69KiP0RjorPDRNyH91iipLthnMaocuKtmBwfe-5oowvzYDuQ==)
28. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQED5ZRAHpIKs9WAcKzSX-_t_qWa1kyYBpyBBDW1ym1Sk_-pzeASeGj9-ThVn_Kl5ptI7WU9opiIxAdo7g8_vZnFQMDclClY18sOzhqPRuXBVdaHE_wO)
29. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI9zyIKoK6uP4km2p0qXy10Rc0LY8Ry21hpeuWs4_yO68H37nBaAewd4D_TfEnFUGNzQIFvjTPE-N-PcTtM0Iokqb1jrqLQ9N5Qr4s1rDirKWMAcnEPCxH9u53m7tyNa6kfi2bnhdnhkpENZiAx2MBXrt9Tera65fKTE6CE05lQqRg8pu9Oe3YGWBo6dOEA_WSP4ltLwgXmINC6WyCA-R0Oy58FsZMESvylju52XsfXTFGXxXvttPlyewIDr835w-3vg==)
30. [mlr.press](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvCXTxr8Gc-oi5X-ldcbWiN1z7bePGp8c9baur5rTriMrJudOhuKh0r0tig-ov-JkTJfQ9A2P0B9N1ruyJYboRLvVyWJpZlS2UXwInN_vKcjQiCyxVmF52MPxegi4_52yslDEszfwtVA==)
31. [neurips.cc](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHHb0-TUxE48NtD3L4_XYcoJDvgLL6eK6kYwA68PkeiuwZSikhy86lWnZH0Rf-C3CHllfl5tDaiYe__bYMgAZnfm8n_95LuC41UqN8A0gMDV6GOrx0ioDLJQbRTfAVc_07IlZ0Pg9C2oWweh4vpaJp)
32. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENHfAlD2H9Zzz94Tj8RJsEu_Qk27o7anqqUJPIAyzv_C7zTsLOBalOMKLDeRZi1VHjiTo4OFPewbTcM_UwZk-GcCucqZugfvSZWLq6P-3cuWzSgNkifLI5)
33. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRG-Bqx4Ygp46l1hkmLhb5noi3L7eO5Hcua9MEeUUnFC7Qivt4mBu-SUxSJXCyHZG5fVmuMMWPaXXME71jleVgCSyz1VVuYGm-ZLNAi-r-aFn7tKNR)
34. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIBQ729ZDwsRlvPDP44rif_xBSbN0Wzaotdc5AQZLvEgJNa9nWgXah0bIjpzAoW6n_ntC486JOuaKEUmpk5ELGFP86MJb_t2Kykbd-WZztg31VDrf0VbRp4PVD2heLC-8XkfwxAHnwZtuc_0bQ7aDmxp9YwFojE0byYHDu9ucu5T8P_CBR7A9F770LSTB_Mc_-3-4atQ==)
35. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6AZKk5UTu3qAUYkyzcZwpNxxji6emTNNZd61slOEensVDlPjpfKfZ8xOymjdIzieYRv7ZqEHst5YRLrqEzFOJ_nNYVslw8o5M7MJciJA8EHGXvLk6ggtqGSfNnamepyswplrMAuLNhBWsPjVWJNsGaiM0SzjhQI4m9cyY4l19CeCeNEkbsSG8sJlG4SoP)
36. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6dHXCs1c2AUVy2Cg-KFWLUjLU6XL5GgPl_MAcbuXXfpRpOGxoz00suhUUMnX4j5ByLKw52b47Uv7Okg9dQQ8LRMew9w9Sp57wSLjUm8F5ScLBGL0rNhEpYH04W87PZNc=)
37. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEw2wpdlYnu48qngO80jwzBOMkNnMnITmes_znje58ML1wDCTjkY-xjRV4Kvc5lvvbS5x8CiMTmkGUpyEc1Whb1DELlyeFZnIiJaMrh0ZOQraPd1aOnrSdw71598NGWLcYEN2lhmI1zZFEq8daLMvZeUCDjPg1DQ82tgdCYoZ18Rg8Gfqx4lI4snMMCeH0HAMJ1SiZQ-5Hf0SvPEpFwqvVaoGb3kPtENO1UgYToibOiO3-iG0RMfLMZ)
38. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWkcecFMooFYLmqfHl55RWp657_1fc2laD3bnKz3gmIzT8y_QNJV74AOKvPh2PgVbLcjJy563hC5hUDMzpg5EW6EwFF7avc7OMVj8JxyAV0r-i0M2R79F5)
39. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9povHOSDkWw_6AHNuPZI9dwdSqqy6efZthxBplXkT4QrOsNbv0xRgw5xaldizoKwOKmFqUIe4D-lO_R2v72M624cAShSxtryRonXbR6XBzVdfQXnYcrNheYqpkff7JUsbKSb2tZH9qngx5TU0YdUSEOpke39q9S_an5h7QiHu0NKaM1CnhCavirxvqfThjNsQc9gZX1wsoyyTTMiiXCNgNeBc2r5OZxQ-zgXY)
40. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwr56DVbAZeWTiIdAucdrSQT8yvzQGUVr_CHqnKhZJoS1dUkmUq9weUjXGR70GrH4rkMkNdYJEnSKx33PTIVYgwpKb7TVeozPmFHF8LGUqRIsf5_tH)
41. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjFFm67bBkVSFWkWhZapwFHrZuuonNLFDHThgGUJRoxDLZBhwixzstH7a_UMQ-zMPY8cuZz8FpBMedM-gY_DQLhzm2zW9lPZtR3WREo8E82oGAjSpiSISt9sgaHeM9W2QKvYTro8tTJj7hderWM0LuYbfb4Dm-KaSEKI1ja_ejE3n0by67ir3CLpBbKS7iJoG-QhNthjZa88Gc0MOFEspJ)
42. [towardsdatascience.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzkgAsaDLb1uFP5nalxB980mle7idwS2Lw7SxyLL6L2cNq46dNrxs1DnH_q7X0n-j5TfFJMb12rzM6QN4berkkOJJHbVb_UsSrvXA21V3hNGXMXiekF5bMoZl2CaqUeGrn550M_oZnWUSJ7M8_L4yiYQKdboJojSfDggGxooKY5r1RFdGTRZjkXajc6LI2V-qDTd-ipDcgJ06u9uO1uA9xFQgyXWQtJ_lS)
43. [openreview.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHe7hQ6H_t6M59l_9O-oqqogEcAVeWMQG-qrsOfAr_EfjaX18f6lHmwdb9mUUgT-yFeEK1ApyAI8t-rdY7_8fpvO6ElHGJEvDVJ9Kcw_ICNQJXxZpAQot0NtjvmdSA9Lw==)
44. [linuxfoundation.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL6FC2fhCc-rv7lCXHt9p9BuMVsVODyykexlxUTCIfZMkyJJuM5xMq3TIWeo_fk3rTwlUXDYpBTndE341F4M2F31yq1owasqLq33FXh57KfK9odh5bmmo-9l_oAOs1bx9mZr0M1JCB-8uo-nSjsLj0hSs7wOFVst8e0YgmNcLhkIbgvSKS3mcdJwEgodEooQ0LOLNteANWzkGeoi2KziVxzA-gHdm_L3MIZIMkAHztCRKempq1zNCdO47tm_CXkGkUrphrlPo=)
45. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3XjfRt0OSQQSkll8OoQqGvRct3_Er4M8pdjOhuE2UXHxhPb2fNMYvf8H8sej18ztlE2C0E-OStimMlTh9QVm8h7luRQZA9ViiGT2LT-vThYqvHUATQIXUhaUm2xjb3oPcRYItMeFfveVAJXsACrCpypCjlaTxt5kcA5yioXOLOwZO9rAucoB-sdWNOvxote9TSXDwSo2gtz52SkTF5ZGwDNt27Qng1R6y)


## Annotations
Annotation(end_index=3419, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHQBiT9qkOHutVcu8aquK7AcrOJMJRjkHNJFTsAcm-17DiTR3YrkmuzHQNOpFXAever52iZ-_Thfxi-0fx2HaJceM9DwH0DHMYC7slHpDYdRFmZoTNwwKrZagL6l-dVsdftO6lAARzvIKKVrdS1Qn3', start_index=3407)
Annotation(end_index=3419, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHCS8vryIZ-c2Ku_iJ7sMCj34CmIKp-rQcvgcxnJs91QDTltIdgeYCXo65CW35eWPOgD0NEP3Hlcy_iJsKb3VLta7Sughz0IEd_4xX0VjMIM9_p4dASde4Aj9TtQ==', start_index=3407)
Annotation(end_index=3655, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMjwfoT3M22i3YwlWYj6zEXQhJB_jUfv2yLmldR9mToO4J8EwJ15VnkZzUjWaostY9iRNZe0J7ursHFENqPOgr2uquUTH1y89ckQRGyYt6ksLuPTYweXhgb5E=', start_index=3646)
Annotation(end_index=3858, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHCS8vryIZ-c2Ku_iJ7sMCj34CmIKp-rQcvgcxnJs91QDTltIdgeYCXo65CW35eWPOgD0NEP3Hlcy_iJsKb3VLta7Sughz0IEd_4xX0VjMIM9_p4dASde4Aj9TtQ==', start_index=3846)
Annotation(end_index=3858, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMjwfoT3M22i3YwlWYj6zEXQhJB_jUfv2yLmldR9mToO4J8EwJ15VnkZzUjWaostY9iRNZe0J7ursHFENqPOgr2uquUTH1y89ckQRGyYt6ksLuPTYweXhgb5E=', start_index=3846)
Annotation(end_index=4312, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEaONxXFbz9YRN38c0-XkcWr69SGHu1N6g0G1NeSRjASCrC83WvdBTwswEuee6-86fPFpIufvlL9Ftp2kxjKuYLad9_Ye-yFl_4B5kCp6aSRlV7hBC5ueDZNrLuWzKEqHdjqWclKT0M1nPdif-3RchCclE=', start_index=4297)
Annotation(end_index=4312, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHCS8vryIZ-c2Ku_iJ7sMCj34CmIKp-rQcvgcxnJs91QDTltIdgeYCXo65CW35eWPOgD0NEP3Hlcy_iJsKb3VLta7Sughz0IEd_4xX0VjMIM9_p4dASde4Aj9TtQ==', start_index=4297)
Annotation(end_index=4312, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMjwfoT3M22i3YwlWYj6zEXQhJB_jUfv2yLmldR9mToO4J8EwJ15VnkZzUjWaostY9iRNZe0J7ursHFENqPOgr2uquUTH1y89ckQRGyYt6ksLuPTYweXhgb5E=', start_index=4297)
Annotation(end_index=4558, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8G5rLEt202R4DfjVjZf-lv7_ZGKyG0So5Jz00nzg1vlszqaGU0Q0-M9I533LLYd83WsH8hH4auSyue3_HuOAXiWRT4mNf5pKBrKU917zw1M7fFS73t3cf3RfM2Jw=', start_index=4543)
Annotation(end_index=4558, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFpVDD-EKACFn4SEmW6vf2ojqN1yIC9xJlm-HYckA_cr9PdMYvNw1mBkiAHxL8qqI725XouGzu2Rhcndq3VCgDexQFg0-HxYHPvvkrpR9fC3YZiS7kJPfZR-4CmG2fD2daO3TOji31ZfbiglqyXRPbTrp0jL0zsX9O_7tu0DqU51a1m5mEOyllXmP0PcTL63SZYC8VL4_JLZA4lqleALk4Y_2cOYIYytii9kvGot-FNycim0zM=', start_index=4543)
Annotation(end_index=4558, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzS70uLxP__VxkVtRhMtg7N7Qcc_V5UQecLScS3Gk0Om_R8_TlCHgFJE85yxxYPhXWB0H9VqPSsQOJaVitFFNwPPDOjUn3YCfsVok6HzvHtICUzEoUvtcg', start_index=4543)
Annotation(end_index=4858, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5MsfbTajvB1fM6rB579px-gQUQfVacseXtP_cpM18Dyq-fvgRHN-Qn6ehemMpiKGe7fRf7YpSD2vmN4hFVDWbg2j0_ToHTNLBPPqTSzwT_fnOv2MxvCAl5JO2WMG3XwyygPwqDaIgWlUmc_hS35wnw84DalLjlYmkYIcO13fbmlCy0P-VTH27MVgdjJUJH2Eu3iwegA458-w-0rknsK5OuZ0rfToIQ9CFUlAOIR5IFrHqQwPy13zQPdhqJ6WbWkRFuLzWokoteLmWlg==', start_index=4842)
Annotation(end_index=4858, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAOPJDaI-Sig4bfgnNPpZr-D_VZG00MIr8SB71tCt4PmCFTBlK7CPMYWBDDqQbTucSWMUMRQ_t9CCRnLBdJlxIBwaWOmBoI_BrUimmLMNdMytnpRqqfs-f_d914EdvpGNOnJaIeNULQUAT4WeiphKG', start_index=4842)
Annotation(end_index=4858, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlJihxFTYrgI2niT34zMx6ko7Dd7a2IksFl9RrRSCrHvqlyK_eEIfnlvoHfupHXCXG0s9oAJYprordVTitmLhoGsNCaspcqVk24tvJzANb7wBwhSEwUHhHqf4iXkFyrsGjOYhang==', start_index=4842)
Annotation(end_index=5163, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBGFe4RMcS4_AR4isnsVEswVN0vvAChx7detTUW_Hl-OHJ13B3gSr4fYYuv3C6kzjh3EHDGjvjvDAQUPg7c8d4TUbGS97gNDGO3Kcl0LMMMkutRsRmz5QEbEMktdsl7KGDp_DWhyVWMHcyestUlv-sYaDZNb-14w==', start_index=5145)
Annotation(end_index=5163, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgxRk9q46Yu7MijAXJ7MZ2xeJoPXZf7Y28xmrHLvNB8HO3mjwdWnI4pPXWCsNYUGJFEyyWSY92McwAVSxOpjcAVlNxPfjgPTK1KJPsDOBgJMInZ41yUKGgE-l6DO7tkiLGck1LbMNobUGNMvYsEjKPCczmrYeSbf56r3mL1X-0X3r-', start_index=5145)
Annotation(end_index=5163, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXBS5chaX9Iu8nLLwX-dhlUtJXLBnzg62yuH7iIFU9_iCfCVRI_1crCrKfPg8OKSlrQlX8wbsG9jjoDDsPZNGm7Wk5PKT69dzYb0tCcw8Lp6QofXWNXVZYpyEMx1ASiXg32MkprwIgqu4TNZEeveJ4lp4=', start_index=5145)
Annotation(end_index=5419, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIKR4xrm61aXTkAlboFROHU2iIhpwvBaQp1ZGjd27YMMYTohpwDMOcF3j8MP-XPyc4B7_SRYW4SjqmRgZfH7T74aF1tZOCSUA9SlL1H7yBGCFTxOETKddIwGtXYMQMOpU1nhOBMJwBsURJWH-vufcz4VtBS-BAhogyEDXqB7DpaegZSAa-thm906SuEzQHeZC5A05NPYWlGAuLGqvIRaAtFSyovZzpmUA13j7KyIeV', start_index=5405)
Annotation(end_index=5419, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdEbKgq-N9tTpnZXz5CQOpJM8ePv2AJVt4cWNEylU6geVUHvZq9-B44iXqGgN2-QxzO0z-idl3IPOZL8Vbs0xvCaJxM0TOuzl0Smktek2O6NDle0GvdKrk5xLTZZp1akY=', start_index=5405)
Annotation(end_index=6186, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElqfYKU81GBAg1K3BEZ0Mqx4grkNP3x_tCP0lSXCZA_TsQosMbyxh9JyLVSeZ-jJFdQVFzBBHDpN14DLWZYP5rm2rgJhxDkFi4RnV9YsDEH4sQC92zYfMm2cNeVgjOn-6dxcxdhRg-7a0=', start_index=6176)
Annotation(end_index=6394, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErZHGTcSqqbne24zbFulRFYz14B95024JLz9T2XDVc9r9z6sab6R0FXVS6ibMAcnlk9bOkNtL9LPG-LI6uzgqPoG1FfUh9AJMSsRWZPt-mychZSHFtj8-d', start_index=6380)
Annotation(end_index=6394, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxNT26BfE876CexgMND0vLo8e20-XiQcnKu3G9P9nxjcXdFl44fwNaUuwCLGohuUn4s-dS5X_z3f_WAH02t5pfaUbJselH_SEaAq5kqJGQpjM3wLoTBbPhC5RvcQ5K4VS-ziT6ztvqKWhE-T7ZyPeYLVEyRmOYWMO6_Nx98q7wQ2RtRBjSe0yYHQrPqKKF6DmNksZBRADs5ybVdlRlEg==', start_index=6380)
Annotation(end_index=6653, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElqfYKU81GBAg1K3BEZ0Mqx4grkNP3x_tCP0lSXCZA_TsQosMbyxh9JyLVSeZ-jJFdQVFzBBHDpN14DLWZYP5rm2rgJhxDkFi4RnV9YsDEH4sQC92zYfMm2cNeVgjOn-6dxcxdhRg-7a0=', start_index=6639)
Annotation(end_index=6653, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErZHGTcSqqbne24zbFulRFYz14B95024JLz9T2XDVc9r9z6sab6R0FXVS6ibMAcnlk9bOkNtL9LPG-LI6uzgqPoG1FfUh9AJMSsRWZPt-mychZSHFtj8-d', start_index=6639)
Annotation(end_index=6838, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8-q55DlfUW6ESOyH6M6a3gs5n_sjV1JSbxWicXX0BqFwZpq1DzwwGiJOOBGHODyZSRa6JbE4CXNI1YebWe8BHa7865f4JXWzRpM3OkLMgHv7gk69ylzVokw11kvaY6fnZ6o8qpzNJX2mPUd-z205Xt4bN1s8NP6UikC4Kp3wxIQJixFx0Wrf0soga52H8imBWe64X7l5YEApy005ibSFNDHY=', start_index=6824)
Annotation(end_index=6838, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElqfYKU81GBAg1K3BEZ0Mqx4grkNP3x_tCP0lSXCZA_TsQosMbyxh9JyLVSeZ-jJFdQVFzBBHDpN14DLWZYP5rm2rgJhxDkFi4RnV9YsDEH4sQC92zYfMm2cNeVgjOn-6dxcxdhRg-7a0=', start_index=6824)
Annotation(end_index=7455, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIKR4xrm61aXTkAlboFROHU2iIhpwvBaQp1ZGjd27YMMYTohpwDMOcF3j8MP-XPyc4B7_SRYW4SjqmRgZfH7T74aF1tZOCSUA9SlL1H7yBGCFTxOETKddIwGtXYMQMOpU1nhOBMJwBsURJWH-vufcz4VtBS-BAhogyEDXqB7DpaegZSAa-thm906SuEzQHeZC5A05NPYWlGAuLGqvIRaAtFSyovZzpmUA13j7KyIeV', start_index=7437)
Annotation(end_index=7455, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdEbKgq-N9tTpnZXz5CQOpJM8ePv2AJVt4cWNEylU6geVUHvZq9-B44iXqGgN2-QxzO0z-idl3IPOZL8Vbs0xvCaJxM0TOuzl0Smktek2O6NDle0GvdKrk5xLTZZp1akY=', start_index=7437)
Annotation(end_index=7455, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHFMfD1XW-MxM9MkqOEgRwu47Z90k9W2bbBB5vNPA2QTKgOEhA2NEQwFhhu2VN_x_QbE7aPneHxcic_x3r2-pLrJqtzT2pnXJRWbzoXGv9A5PxeoAtZvxLvgWOk0TBe541gS98eBLungzKndzFtiC9nTwopnJ3CxRFriTWlgcKFabHkP9zkoE8ZzRVjWquc_FliXy60t7F10AYhZqOio9vdeFDzVWD4CblGNA==', start_index=7437)
Annotation(end_index=7765, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdEbKgq-N9tTpnZXz5CQOpJM8ePv2AJVt4cWNEylU6geVUHvZq9-B44iXqGgN2-QxzO0z-idl3IPOZL8Vbs0xvCaJxM0TOuzl0Smktek2O6NDle0GvdKrk5xLTZZp1akY=', start_index=7755)
Annotation(end_index=7958, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEx22aXE97pKoOii9IBPRxQ2TRJ6XYUE2OrwOCxIXHnplIBtMacY80-G9LNH3PcqwsdROFrWe8-XD00jxjHX7gDhwmgqaZ3n-OWYkU1ukxmTdYitebUArH_nM5iit_Zew_X4EABaebzRIg=', start_index=7948)
Annotation(end_index=8153, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEx22aXE97pKoOii9IBPRxQ2TRJ6XYUE2OrwOCxIXHnplIBtMacY80-G9LNH3PcqwsdROFrWe8-XD00jxjHX7gDhwmgqaZ3n-OWYkU1ukxmTdYitebUArH_nM5iit_Zew_X4EABaebzRIg=', start_index=8139)
Annotation(end_index=8153, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpSjI10E-RMxEtmjX4WUH1XSdZiNvPUTXpModd-bAOLoqv1cyID08v5cvUG8lOEUpEHCRi-Pm-MlemOivUbC8QOnMgMS_i4enbx94MjKdz58lA65ensr1xnxJ_8z4b0bNoR9ZB1_7j4KNGPky15oAn0kHHnv-iiH1s_cr25Eno', start_index=8139)
Annotation(end_index=9034, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErZHGTcSqqbne24zbFulRFYz14B95024JLz9T2XDVc9r9z6sab6R0FXVS6ibMAcnlk9bOkNtL9LPG-LI6uzgqPoG1FfUh9AJMSsRWZPt-mychZSHFtj8-d', start_index=9020)
Annotation(end_index=9034, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0VX0jiqtYKbxoUeZjD5BI4qy4lUDYTIj1zgF-N6H6N92qiptaICdkxc4HARaa2W4ODE9Pjc0zXGVX1IDJGyK_N1GbSpa1gvQTUnqS4uB_q_QCTJEK7XtqoR6q8WE6XjAAj5kKp4zy0fbEjGxJ1p0Poxe_NljIQInOsol1xB1VvtH_', start_index=9020)
Annotation(end_index=9306, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJNy6Wr-3xcPqXI_yteys1dDd_YdH5qUYVQraj3_q3G7XglGLdKbTNHPN4_N7NRa3-0LPXaPVdOhrDgsw-MOpWaRp4fNvrSMmcBDD65ZHk6N7f8UYNkryk', start_index=9296)
Annotation(end_index=10220, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwpPGpZ2fpHjCjZ4cm8ttN6_LOohA96fPN2T3G5nkX4U6r5ERX2L2LWgs8c9VoOYqmVSmzwHRWshwJDsB5Li6T-O_LtZkHuv69KiP0RjorPDRNyH91iipLthnMaocuKtmBwfe-5oowvzYDuQ==', start_index=10202)
Annotation(end_index=10220, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOoL5dQwVFjdqZ-IA4StM7znDlnWG4qte2FWGyzUF1JbJn7AWOtSl1B-30sD4zIqXAu842kjPZm7kKE6x5n3FU-J0ht2cxb1dtZ3TyzbnB40fuEbD0A4i7nYvOnsw4cEhC5KllqSdusD9X6rIjjMXemF3AXfoMK091ihNMUTddb4rkRNlVmghvzMtoNtAzHUwO8w==', start_index=10202)
Annotation(end_index=10220, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGocOFrdK_fqoWPNBVX4D9nUyEJKMn6AhIpiBeNn4YFlUKifu0G2D1TMr8BoOcAreL6x7_F_uGsfH5cml0pIMwsk_g7_2mnoh1QTk1-4okd4Lx9_rbX', start_index=10202)
Annotation(end_index=10794, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8G5rLEt202R4DfjVjZf-lv7_ZGKyG0So5Jz00nzg1vlszqaGU0Q0-M9I533LLYd83WsH8hH4auSyue3_HuOAXiWRT4mNf5pKBrKU917zw1M7fFS73t3cf3RfM2Jw=', start_index=10782)
Annotation(end_index=10794, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGzS70uLxP__VxkVtRhMtg7N7Qcc_V5UQecLScS3Gk0Om_R8_TlCHgFJE85yxxYPhXWB0H9VqPSsQOJaVitFFNwPPDOjUn3YCfsVok6HzvHtICUzEoUvtcg', start_index=10782)
Annotation(end_index=11120, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQED5ZRAHpIKs9WAcKzSX-_t_qWa1kyYBpyBBDW1ym1Sk_-pzeASeGj9-ThVn_Kl5ptI7WU9opiIxAdo7g8_vZnFQMDclClY18sOzhqPRuXBVdaHE_wO', start_index=11106)
Annotation(end_index=11120, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEI9zyIKoK6uP4km2p0qXy10Rc0LY8Ry21hpeuWs4_yO68H37nBaAewd4D_TfEnFUGNzQIFvjTPE-N-PcTtM0Iokqb1jrqLQ9N5Qr4s1rDirKWMAcnEPCxH9u53m7tyNa6kfi2bnhdnhkpENZiAx2MBXrt9Tera65fKTE6CE05lQqRg8pu9Oe3YGWBo6dOEA_WSP4ltLwgXmINC6WyCA-R0Oy58FsZMESvylju52XsfXTFGXxXvttPlyewIDr835w-3vg==', start_index=11106)
Annotation(end_index=11432, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvCXTxr8Gc-oi5X-ldcbWiN1z7bePGp8c9baur5rTriMrJudOhuKh0r0tig-ov-JkTJfQ9A2P0B9N1ruyJYboRLvVyWJpZlS2UXwInN_vKcjQiCyxVmF52MPxegi4_52yslDEszfwtVA==', start_index=11418)
Annotation(end_index=11432, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHHb0-TUxE48NtD3L4_XYcoJDvgLL6eK6kYwA68PkeiuwZSikhy86lWnZH0Rf-C3CHllfl5tDaiYe__bYMgAZnfm8n_95LuC41UqN8A0gMDV6GOrx0ioDLJQbRTfAVc_07IlZ0Pg9C2oWweh4vpaJp', start_index=11418)
Annotation(end_index=11698, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENHfAlD2H9Zzz94Tj8RJsEu_Qk27o7anqqUJPIAyzv_C7zTsLOBalOMKLDeRZi1VHjiTo4OFPewbTcM_UwZk-GcCucqZugfvSZWLq6P-3cuWzSgNkifLI5', start_index=11684)
Annotation(end_index=11698, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErZHGTcSqqbne24zbFulRFYz14B95024JLz9T2XDVc9r9z6sab6R0FXVS6ibMAcnlk9bOkNtL9LPG-LI6uzgqPoG1FfUh9AJMSsRWZPt-mychZSHFtj8-d', start_index=11684)
Annotation(end_index=12133, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErZHGTcSqqbne24zbFulRFYz14B95024JLz9T2XDVc9r9z6sab6R0FXVS6ibMAcnlk9bOkNtL9LPG-LI6uzgqPoG1FfUh9AJMSsRWZPt-mychZSHFtj8-d', start_index=12119)
Annotation(end_index=12133, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJNy6Wr-3xcPqXI_yteys1dDd_YdH5qUYVQraj3_q3G7XglGLdKbTNHPN4_N7NRa3-0LPXaPVdOhrDgsw-MOpWaRp4fNvrSMmcBDD65ZHk6N7f8UYNkryk', start_index=12119)
Annotation(end_index=12411, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRG-Bqx4Ygp46l1hkmLhb5noi3L7eO5Hcua9MEeUUnFC7Qivt4mBu-SUxSJXCyHZG5fVmuMMWPaXXME71jleVgCSyz1VVuYGm-ZLNAi-r-aFn7tKNR', start_index=12401)
Annotation(end_index=12658, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6AZKk5UTu3qAUYkyzcZwpNxxji6emTNNZd61slOEensVDlPjpfKfZ8xOymjdIzieYRv7ZqEHst5YRLrqEzFOJ_nNYVslw8o5M7MJciJA8EHGXvLk6ggtqGSfNnamepyswplrMAuLNhBWsPjVWJNsGaiM0SzjhQI4m9cyY4l19CeCeNEkbsSG8sJlG4SoP', start_index=12644)
Annotation(end_index=12658, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIBQ729ZDwsRlvPDP44rif_xBSbN0Wzaotdc5AQZLvEgJNa9nWgXah0bIjpzAoW6n_ntC486JOuaKEUmpk5ELGFP86MJb_t2Kykbd-WZztg31VDrf0VbRp4PVD2heLC-8XkfwxAHnwZtuc_0bQ7aDmxp9YwFojE0byYHDu9ucu5T8P_CBR7A9F770LSTB_Mc_-3-4atQ==', start_index=12644)
Annotation(end_index=13030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6AZKk5UTu3qAUYkyzcZwpNxxji6emTNNZd61slOEensVDlPjpfKfZ8xOymjdIzieYRv7ZqEHst5YRLrqEzFOJ_nNYVslw8o5M7MJciJA8EHGXvLk6ggtqGSfNnamepyswplrMAuLNhBWsPjVWJNsGaiM0SzjhQI4m9cyY4l19CeCeNEkbsSG8sJlG4SoP', start_index=13020)
Annotation(end_index=13201, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIBQ729ZDwsRlvPDP44rif_xBSbN0Wzaotdc5AQZLvEgJNa9nWgXah0bIjpzAoW6n_ntC486JOuaKEUmpk5ELGFP86MJb_t2Kykbd-WZztg31VDrf0VbRp4PVD2heLC-8XkfwxAHnwZtuc_0bQ7aDmxp9YwFojE0byYHDu9ucu5T8P_CBR7A9F770LSTB_Mc_-3-4atQ==', start_index=13187)
Annotation(end_index=13201, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6dHXCs1c2AUVy2Cg-KFWLUjLU6XL5GgPl_MAcbuXXfpRpOGxoz00suhUUMnX4j5ByLKw52b47Uv7Okg9dQQ8LRMew9w9Sp57wSLjUm8F5ScLBGL0rNhEpYH04W87PZNc=', start_index=13187)
Annotation(end_index=13439, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWkcecFMooFYLmqfHl55RWp657_1fc2laD3bnKz3gmIzT8y_QNJV74AOKvPh2PgVbLcjJy563hC5hUDMzpg5EW6EwFF7avc7OMVj8JxyAV0r-i0M2R79F5', start_index=13421)
Annotation(end_index=13439, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEw2wpdlYnu48qngO80jwzBOMkNnMnITmes_znje58ML1wDCTjkY-xjRV4Kvc5lvvbS5x8CiMTmkGUpyEc1Whb1DELlyeFZnIiJaMrh0ZOQraPd1aOnrSdw71598NGWLcYEN2lhmI1zZFEq8daLMvZeUCDjPg1DQ82tgdCYoZ18Rg8Gfqx4lI4snMMCeH0HAMJ1SiZQ-5Hf0SvPEpFwqvVaoGb3kPtENO1UgYToibOiO3-iG0RMfLMZ', start_index=13421)
Annotation(end_index=13439, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9povHOSDkWw_6AHNuPZI9dwdSqqy6efZthxBplXkT4QrOsNbv0xRgw5xaldizoKwOKmFqUIe4D-lO_R2v72M624cAShSxtryRonXbR6XBzVdfQXnYcrNheYqpkff7JUsbKSb2tZH9qngx5TU0YdUSEOpke39q9S_an5h7QiHu0NKaM1CnhCavirxvqfThjNsQc9gZX1wsoyyTTMiiXCNgNeBc2r5OZxQ-zgXY', start_index=13421)
Annotation(end_index=13934, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwr56DVbAZeWTiIdAucdrSQT8yvzQGUVr_CHqnKhZJoS1dUkmUq9weUjXGR70GrH4rkMkNdYJEnSKx33PTIVYgwpKb7TVeozPmFHF8LGUqRIsf5_tH', start_index=13920)
Annotation(end_index=13934, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpSjI10E-RMxEtmjX4WUH1XSdZiNvPUTXpModd-bAOLoqv1cyID08v5cvUG8lOEUpEHCRi-Pm-MlemOivUbC8QOnMgMS_i4enbx94MjKdz58lA65ensr1xnxJ_8z4b0bNoR9ZB1_7j4KNGPky15oAn0kHHnv-iiH1s_cr25Eno', start_index=13920)
Annotation(end_index=14055, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWkcecFMooFYLmqfHl55RWp657_1fc2laD3bnKz3gmIzT8y_QNJV74AOKvPh2PgVbLcjJy563hC5hUDMzpg5EW6EwFF7avc7OMVj8JxyAV0r-i0M2R79F5', start_index=14045)
Annotation(end_index=14485, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRG-Bqx4Ygp46l1hkmLhb5noi3L7eO5Hcua9MEeUUnFC7Qivt4mBu-SUxSJXCyHZG5fVmuMMWPaXXME71jleVgCSyz1VVuYGm-ZLNAi-r-aFn7tKNR', start_index=14471)
Annotation(end_index=14485, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6dHXCs1c2AUVy2Cg-KFWLUjLU6XL5GgPl_MAcbuXXfpRpOGxoz00suhUUMnX4j5ByLKw52b47Uv7Okg9dQQ8LRMew9w9Sp57wSLjUm8F5ScLBGL0rNhEpYH04W87PZNc=', start_index=14471)
Annotation(end_index=14871, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIKR4xrm61aXTkAlboFROHU2iIhpwvBaQp1ZGjd27YMMYTohpwDMOcF3j8MP-XPyc4B7_SRYW4SjqmRgZfH7T74aF1tZOCSUA9SlL1H7yBGCFTxOETKddIwGtXYMQMOpU1nhOBMJwBsURJWH-vufcz4VtBS-BAhogyEDXqB7DpaegZSAa-thm906SuEzQHeZC5A05NPYWlGAuLGqvIRaAtFSyovZzpmUA13j7KyIeV', start_index=14857)
Annotation(end_index=14871, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOoL5dQwVFjdqZ-IA4StM7znDlnWG4qte2FWGyzUF1JbJn7AWOtSl1B-30sD4zIqXAu842kjPZm7kKE6x5n3FU-J0ht2cxb1dtZ3TyzbnB40fuEbD0A4i7nYvOnsw4cEhC5KllqSdusD9X6rIjjMXemF3AXfoMK091ihNMUTddb4rkRNlVmghvzMtoNtAzHUwO8w==', start_index=14857)
Annotation(end_index=15322, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjFFm67bBkVSFWkWhZapwFHrZuuonNLFDHThgGUJRoxDLZBhwixzstH7a_UMQ-zMPY8cuZz8FpBMedM-gY_DQLhzm2zW9lPZtR3WREo8E82oGAjSpiSISt9sgaHeM9W2QKvYTro8tTJj7hderWM0LuYbfb4Dm-KaSEKI1ja_ejE3n0by67ir3CLpBbKS7iJoG-QhNthjZa88Gc0MOFEspJ', start_index=15312)
Annotation(end_index=15659, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzkgAsaDLb1uFP5nalxB980mle7idwS2Lw7SxyLL6L2cNq46dNrxs1DnH_q7X0n-j5TfFJMb12rzM6QN4berkkOJJHbVb_UsSrvXA21V3hNGXMXiekF5bMoZl2CaqUeGrn550M_oZnWUSJ7M8_L4yiYQKdboJojSfDggGxooKY5r1RFdGTRZjkXajc6LI2V-qDTd-ipDcgJ06u9uO1uA9xFQgyXWQtJ_lS', start_index=15649)
Annotation(end_index=15986, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBGFe4RMcS4_AR4isnsVEswVN0vvAChx7detTUW_Hl-OHJ13B3gSr4fYYuv3C6kzjh3EHDGjvjvDAQUPg7c8d4TUbGS97gNDGO3Kcl0LMMMkutRsRmz5QEbEMktdsl7KGDp_DWhyVWMHcyestUlv-sYaDZNb-14w==', start_index=15972)
Annotation(end_index=15986, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHXBS5chaX9Iu8nLLwX-dhlUtJXLBnzg62yuH7iIFU9_iCfCVRI_1crCrKfPg8OKSlrQlX8wbsG9jjoDDsPZNGm7Wk5PKT69dzYb0tCcw8Lp6QofXWNXVZYpyEMx1ASiXg32MkprwIgqu4TNZEeveJ4lp4=', start_index=15972)
Annotation(end_index=17560, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMjwfoT3M22i3YwlWYj6zEXQhJB_jUfv2yLmldR9mToO4J8EwJ15VnkZzUjWaostY9iRNZe0J7ursHFENqPOgr2uquUTH1y89ckQRGyYt6ksLuPTYweXhgb5E=', start_index=17551)
Annotation(end_index=17665, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHCS8vryIZ-c2Ku_iJ7sMCj34CmIKp-rQcvgcxnJs91QDTltIdgeYCXo65CW35eWPOgD0NEP3Hlcy_iJsKb3VLta7Sughz0IEd_4xX0VjMIM9_p4dASde4Aj9TtQ==', start_index=17656)
Annotation(end_index=17764, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHe7hQ6H_t6M59l_9O-oqqogEcAVeWMQG-qrsOfAr_EfjaX18f6lHmwdb9mUUgT-yFeEK1ApyAI8t-rdY7_8fpvO6ElHGJEvDVJ9Kcw_ICNQJXxZpAQot0NtjvmdSA9Lw==', start_index=17754)
Annotation(end_index=17846, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE5MsfbTajvB1fM6rB579px-gQUQfVacseXtP_cpM18Dyq-fvgRHN-Qn6ehemMpiKGe7fRf7YpSD2vmN4hFVDWbg2j0_ToHTNLBPPqTSzwT_fnOv2MxvCAl5JO2WMG3XwyygPwqDaIgWlUmc_hS35wnw84DalLjlYmkYIcO13fbmlCy0P-VTH27MVgdjJUJH2Eu3iwegA458-w-0rknsK5OuZ0rfToIQ9CFUlAOIR5IFrHqQwPy13zQPdhqJ6WbWkRFuLzWokoteLmWlg==', start_index=17837)
Annotation(end_index=17939, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxNT26BfE876CexgMND0vLo8e20-XiQcnKu3G9P9nxjcXdFl44fwNaUuwCLGohuUn4s-dS5X_z3f_WAH02t5pfaUbJselH_SEaAq5kqJGQpjM3wLoTBbPhC5RvcQ5K4VS-ziT6ztvqKWhE-T7ZyPeYLVEyRmOYWMO6_Nx98q7wQ2RtRBjSe0yYHQrPqKKF6DmNksZBRADs5ybVdlRlEg==', start_index=17929)
Annotation(end_index=18018, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpSjI10E-RMxEtmjX4WUH1XSdZiNvPUTXpModd-bAOLoqv1cyID08v5cvUG8lOEUpEHCRi-Pm-MlemOivUbC8QOnMgMS_i4enbx94MjKdz58lA65ensr1xnxJ_8z4b0bNoR9ZB1_7j4KNGPky15oAn0kHHnv-iiH1s_cr25Eno', start_index=18008)
Annotation(end_index=18104, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErZHGTcSqqbne24zbFulRFYz14B95024JLz9T2XDVc9r9z6sab6R0FXVS6ibMAcnlk9bOkNtL9LPG-LI6uzgqPoG1FfUh9AJMSsRWZPt-mychZSHFtj8-d', start_index=18094)
Annotation(end_index=18187, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIBQ729ZDwsRlvPDP44rif_xBSbN0Wzaotdc5AQZLvEgJNa9nWgXah0bIjpzAoW6n_ntC486JOuaKEUmpk5ELGFP86MJb_t2Kykbd-WZztg31VDrf0VbRp4PVD2heLC-8XkfwxAHnwZtuc_0bQ7aDmxp9YwFojE0byYHDu9ucu5T8P_CBR7A9F770LSTB_Mc_-3-4atQ==', start_index=18177)
Annotation(end_index=18267, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOoL5dQwVFjdqZ-IA4StM7znDlnWG4qte2FWGyzUF1JbJn7AWOtSl1B-30sD4zIqXAu842kjPZm7kKE6x5n3FU-J0ht2cxb1dtZ3TyzbnB40fuEbD0A4i7nYvOnsw4cEhC5KllqSdusD9X6rIjjMXemF3AXfoMK091ihNMUTddb4rkRNlVmghvzMtoNtAzHUwO8w==', start_index=18257)
Annotation(end_index=18353, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGocOFrdK_fqoWPNBVX4D9nUyEJKMn6AhIpiBeNn4YFlUKifu0G2D1TMr8BoOcAreL6x7_F_uGsfH5cml0pIMwsk_g7_2mnoh1QTk1-4okd4Lx9_rbX', start_index=18343)
Annotation(end_index=18438, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRG-Bqx4Ygp46l1hkmLhb5noi3L7eO5Hcua9MEeUUnFC7Qivt4mBu-SUxSJXCyHZG5fVmuMMWPaXXME71jleVgCSyz1VVuYGm-ZLNAi-r-aFn7tKNR', start_index=18428)
Annotation(end_index=18517, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElqfYKU81GBAg1K3BEZ0Mqx4grkNP3x_tCP0lSXCZA_TsQosMbyxh9JyLVSeZ-jJFdQVFzBBHDpN14DLWZYP5rm2rgJhxDkFi4RnV9YsDEH4sQC92zYfMm2cNeVgjOn-6dxcxdhRg-7a0=', start_index=18507)
Annotation(end_index=18587, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8G5rLEt202R4DfjVjZf-lv7_ZGKyG0So5Jz00nzg1vlszqaGU0Q0-M9I533LLYd83WsH8hH4auSyue3_HuOAXiWRT4mNf5pKBrKU917zw1M7fFS73t3cf3RfM2Jw=', start_index=18578)
Annotation(end_index=18672, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvCXTxr8Gc-oi5X-ldcbWiN1z7bePGp8c9baur5rTriMrJudOhuKh0r0tig-ov-JkTJfQ9A2P0B9N1ruyJYboRLvVyWJpZlS2UXwInN_vKcjQiCyxVmF52MPxegi4_52yslDEszfwtVA==', start_index=18662)
Annotation(end_index=18756, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGdEbKgq-N9tTpnZXz5CQOpJM8ePv2AJVt4cWNEylU6geVUHvZq9-B44iXqGgN2-QxzO0z-idl3IPOZL8Vbs0xvCaJxM0TOuzl0Smktek2O6NDle0GvdKrk5xLTZZp1akY=', start_index=18746)
Annotation(end_index=18820, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGL6FC2fhCc-rv7lCXHt9p9BuMVsVODyykexlxUTCIfZMkyJJuM5xMq3TIWeo_fk3rTwlUXDYpBTndE341F4M2F31yq1owasqLq33FXh57KfK9odh5bmmo-9l_oAOs1bx9mZr0M1JCB-8uo-nSjsLj0hSs7wOFVst8e0YgmNcLhkIbgvSKS3mcdJwEgodEooQ0LOLNteANWzkGeoi2KziVxzA-gHdm_L3MIZIMkAHztCRKempq1zNCdO47tm_CXkGkUrphrlPo=', start_index=18810)
Annotation(end_index=18892, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjFFm67bBkVSFWkWhZapwFHrZuuonNLFDHThgGUJRoxDLZBhwixzstH7a_UMQ-zMPY8cuZz8FpBMedM-gY_DQLhzm2zW9lPZtR3WREo8E82oGAjSpiSISt9sgaHeM9W2QKvYTro8tTJj7hderWM0LuYbfb4Dm-KaSEKI1ja_ejE3n0by67ir3CLpBbKS7iJoG-QhNthjZa88Gc0MOFEspJ', start_index=18882)
Annotation(end_index=18967, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzkgAsaDLb1uFP5nalxB980mle7idwS2Lw7SxyLL6L2cNq46dNrxs1DnH_q7X0n-j5TfFJMb12rzM6QN4berkkOJJHbVb_UsSrvXA21V3hNGXMXiekF5bMoZl2CaqUeGrn550M_oZnWUSJ7M8_L4yiYQKdboJojSfDggGxooKY5r1RFdGTRZjkXajc6LI2V-qDTd-ipDcgJ06u9uO1uA9xFQgyXWQtJ_lS', start_index=18957)
Annotation(end_index=19051, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJNy6Wr-3xcPqXI_yteys1dDd_YdH5qUYVQraj3_q3G7XglGLdKbTNHPN4_N7NRa3-0LPXaPVdOhrDgsw-MOpWaRp4fNvrSMmcBDD65ZHk6N7f8UYNkryk', start_index=19041)
Annotation(end_index=19132, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwpPGpZ2fpHjCjZ4cm8ttN6_LOohA96fPN2T3G5nkX4U6r5ERX2L2LWgs8c9VoOYqmVSmzwHRWshwJDsB5Li6T-O_LtZkHuv69KiP0RjorPDRNyH91iipLthnMaocuKtmBwfe-5oowvzYDuQ==', start_index=19122)
Annotation(end_index=19211, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3XjfRt0OSQQSkll8OoQqGvRct3_Er4M8pdjOhuE2UXHxhPb2fNMYvf8H8sej18ztlE2C0E-OStimMlTh9QVm8h7luRQZA9ViiGT2LT-vThYqvHUATQIXUhaUm2xjb3oPcRYItMeFfveVAJXsACrCpypCjlaTxt5kcA5yioXOLOwZO9rAucoB-sdWNOvxote9TSXDwSo2gtz52SkTF5ZGwDNt27Qng1R6y', start_index=19201)
Annotation(end_index=19277, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWkcecFMooFYLmqfHl55RWp657_1fc2laD3bnKz3gmIzT8y_QNJV74AOKvPh2PgVbLcjJy563hC5hUDMzpg5EW6EwFF7avc7OMVj8JxyAV0r-i0M2R79F5', start_index=19267)
Annotation(end_index=19351, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6AZKk5UTu3qAUYkyzcZwpNxxji6emTNNZd61slOEensVDlPjpfKfZ8xOymjdIzieYRv7ZqEHst5YRLrqEzFOJ_nNYVslw8o5M7MJciJA8EHGXvLk6ggtqGSfNnamepyswplrMAuLNhBWsPjVWJNsGaiM0SzjhQI4m9cyY4l19CeCeNEkbsSG8sJlG4SoP', start_index=19341)
Annotation(end_index=19426, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGocOFrdK_fqoWPNBVX4D9nUyEJKMn6AhIpiBeNn4YFlUKifu0G2D1TMr8BoOcAreL6x7_F_uGsfH5cml0pIMwsk_g7_2mnoh1QTk1-4okd4Lx9_rbX', start_index=19416)

## Sources
