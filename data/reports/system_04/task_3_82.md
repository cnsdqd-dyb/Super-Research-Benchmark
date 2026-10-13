# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 8a17d74f | **Time:** 197.51s | **Cost:** $0.63697
--------------------------------------------------------------------------------

# Defining Boundary Conditions for Information Disclosure in Multi-Party Data Sharing

**Key Points**
*   **Multidimensional Boundaries:** Boundary conditions in multi-party data sharing are not singular but comprise a complex interplay of legal frameworks, cryptographic protocols, and game-theoretic equilibria.
*   **Legal and Contractual Limits:** Data Sharing Agreements (DSAs) and Non-Disclosure Agreements (NDAs) serve as the primary legal boundaries, defining purpose, temporal limits, and liability, often acting as "boundary objects" that facilitate coordination across organizational divides.
*   **Cryptographic Hard Boundaries:** Technologies like Secure Multi-Party Computation (SMPC) create technical boundaries where data is computed upon without ever being revealed in its raw form, ensuring input privacy while allowing output utility.
*   **Game-Theoretic Equilibria:** Theoretical boundary conditions are defined by Nash equilibria where the incentives to share outweigh the risks of leakage; these boundaries shift based on penalty mechanisms, data valuation, and the number of participants.
*   **Contextual Variability:** The definition of a boundary varies significantly by sector, with healthcare requiring strict privacy-preserving analysis of unstructured text, while financial models focus on fraud detection through encrypted collaboration.

## Introduction

The digital economy has transformed data from a static asset into a fluid resource that generates value primarily through exchange and collaborative analysis. However, the movement of data between organizations—whether for medical research, financial fraud detection, or supply chain optimization—introduces profound risks regarding privacy, intellectual property, and regulatory compliance. Consequently, the "boundary conditions" for information disclosure are no longer simple perimeter defenses (firewalls) but sophisticated, multi-layered constructs. These conditions define the precise circumstances, technical constraints, and legal frameworks under which information may cross the threshold from one entity to another.

In the context of multi-party data sharing, a boundary condition is defined as the set of constraints that must be satisfied for a disclosure to be considered valid, secure, and lawful. These conditions operate on three distinct planes: the **legal plane**, where contracts and regulations dictate permissible use; the **technical plane**, where cryptographic protocols enforce privacy by design; and the **theoretical plane**, where mathematical models determine the economic and strategic rationality of sharing. This report provides an exhaustive analysis of these boundary conditions, synthesizing legal scholarship, cryptographic research, and game theory to delineate how modern organizations define the limits of information disclosure.

## Legal and Contractual Boundary Conditions

The most visible boundary conditions in multi-party data sharing are those established by law and contract. These "soft" boundaries rely on the threat of litigation and regulatory penalty to enforce compliance, creating a framework of trust and accountability between disparate entities.

### Data Sharing Agreements (DSAs) as Governance Frameworks
The Data Sharing Agreement (DSA) is the foundational instrument for defining boundary conditions in collaborative environments. A DSA is a formal contract that outlines the purpose, scope, and technical standards for data exchange between two or more controllers [cite: 1, 2]. Unlike simple transfer protocols, DSAs are governance tools that establish the "rules of the road" for the entire lifecycle of the shared data.

**Purpose Limitation and Scope**
A critical boundary condition within a DSA is the definition of purpose. Data cannot be shared for "general business purposes"; it must be restricted to specific, legitimate objectives, such as a defined research project or a contractual obligation [cite: 3, 4]. This boundary prevents "scope creep," where data shared for one reason (e.g., patient care) is utilized for another (e.g., marketing) without authorization. The agreement must specify the data types (e.g., personal, anonymized, aggregated) and explicitly state what is excluded from the share to prevent accidental over-disclosure [cite: 5].

**Temporal Boundaries and Revocability**
Information disclosure is rarely perpetual. DSAs must define temporal boundary conditions, specifying the duration for which data access is granted and the protocols for data destruction or return upon termination [cite: 5, 6]. Research indicates that indefinite agreements pose significant risks as social standards and organizational missions evolve. Therefore, effective boundary conditions include fixed expiration dates and clauses that allow data providers to revoke access if the recipient violates the terms or if the ethical landscape shifts [cite: 6, 7].

**Liability and Indemnification**
The boundary of responsibility is defined through liability and indemnification clauses. These provisions determine which party bears the burden in the event of a data breach or misuse. A well-drafted DSA outlines the specific steps required in a data incident, including reporting timelines and mitigation actions, thereby transforming security from an assumption into an enforceable legal obligation [cite: 4, 5].

### Regulatory Compliance as a Hard Constraint
Superimposed on contractual boundaries are the rigid constraints of legislation such as the General Data Protection Regulation (GDPR) and the Data Protection Act 2018 (DPA 2018). These laws define the "lawful basis" for sharing, which acts as a non-negotiable boundary condition.

**Consent and Transparency**
For personal data, the boundary of disclosure is often the individual's consent. Organizations must obtain explicit, informed consent before sharing data with third parties [cite: 4]. If consent is the lawful basis, the DSA must include mechanisms for managing the retraction of consent, effectively creating a dynamic boundary that can close at the data subject's request [cite: 8]. Transparency is equally critical; individuals must be aware of who holds their data and for what purpose, ensuring that the boundary of disclosure is visible to the data subject [cite: 3].

**Cross-Border Transfers**
Geographical boundaries impose strict conditions on data flow. Under frameworks like the UK GDPR, data cannot flow freely to countries deemed to have inadequate data protection standards unless specific safeguards, such as Standard Contractual Clauses (SCCs) and transfer risk assessments, are in place [cite: 3]. This creates a jurisdictional boundary condition where the legal adequacy of the destination country determines the permissibility of the disclosure.

### Contracts as "Boundary Objects"
Beyond their legal function, contracts and DSAs act as "boundary objects" in organizational theory. They serve as translation devices that bridge the gap between different social worlds (e.g., public health agencies vs. private pharmaceutical companies) [cite: 9, 10].
*   **Interpretive Flexibility:** As boundary objects, contracts allow different parties to maintain their own interpretations of the collaboration while agreeing on a shared structure for action. They align divergent timelines and processes, facilitating coordination across organizational boundaries [cite: 11, 12].
*   **Information Processing:** The contract itself becomes a mechanism for information processing, helping parties resolve equivocality and build a shared understanding of rules and assumptions. This "soft" boundary condition is crucial for maintaining trust and reducing information asymmetry in complex public-private partnerships [cite: 9].

## Technical and Cryptographic Boundary Conditions

While legal boundaries rely on remediation after a breach, technical boundary conditions aim to make unauthorized disclosure computationally impossible. These "hard" boundaries are defined by cryptographic protocols that allow for the utilization of data without its exposure.

### Secure Multi-Party Computation (SMPC)
Secure Multi-Party Computation (SMPC or MPC) represents the pinnacle of technical boundary definition. It allows a group of parties to jointly compute a function over their inputs while keeping those inputs private [cite: 13, 14]. The boundary condition here is absolute: no party ever sees the raw data of another; they only see the output of the computation.

**The "Ideal World" Paradigm**
SMPC is theoretically defined by the "Real World/Ideal World" paradigm. A protocol is secure if the information learned by parties in the real world (exchanging cryptographic messages) is no more than what they would learn in an "ideal world" where a trusted third party receives all inputs, computes the function, and returns the result [cite: 14]. This definition sets a rigorous boundary condition: the only information disclosed is that which is inherent in the output itself [cite: 14, 15].

**Mechanisms of Secrecy**
*   **Secret Sharing:** Data is split into fragments (shares) and distributed among parties. No single share reveals any information about the original data. The boundary is maintained because reconstruction requires a quorum of honest parties [cite: 16].
*   **Garbled Circuits:** Functions are encoded as Boolean circuits where the logic gates are encrypted. Parties evaluate the circuit without learning the values on the wires, ensuring that the computation process itself does not leak information [cite: 17, 18].
*   **Input vs. Output Privacy:** SMPC guarantees *input privacy* (raw data is hidden). However, it does not inherently guarantee *output privacy* (the result might reveal something about the inputs). Therefore, SMPC is often combined with Differential Privacy to bound the information leakage of the result, creating a composite boundary condition [cite: 19].

### Homomorphic Encryption and Zero-Knowledge Proofs
Other cryptographic technologies define different types of boundary conditions:
*   **Homomorphic Encryption (HE):** Allows computation on encrypted data. The boundary condition is that the data remains encrypted at all times—in transit, at rest, and *during processing*. This enables outsourcing computation to untrusted third parties (like cloud providers) without expanding the trust boundary [cite: 15, 20].
*   **Zero-Knowledge Proofs:** Allow a party to prove they possess certain information (e.g., "I am over 18") without revealing the information itself (e.g., the date of birth). This minimizes data minimization, a key regulatory boundary condition [cite: 14].

### Differential Privacy
Differential Privacy (DP) addresses the boundary of *inference*. Even if direct identifiers are removed, statistical analysis can sometimes reconstruct sensitive data. DP introduces a mathematical boundary condition: the output of a query should be substantially the same whether or not any single individual's record is included in the dataset [cite: 18, 21].
*   **Noise Injection:** DP mechanisms add calibrated noise (e.g., Laplacian or Gaussian) to the data or the query result. The "boundary" is defined by the privacy budget ($\epsilon$), which quantifies the maximum allowable information leakage [cite: 21].
*   **Trade-off:** There is an inherent trade-off between the strictness of the boundary (privacy) and the utility of the data. Tighter boundaries result in noisier, less accurate data [cite: 20].

## Theoretical and Game-Theoretic Boundary Conditions

Beyond laws and code, the decision to disclose information is often governed by strategic interactions. Game theory provides a framework for understanding the "equilibrium boundary conditions"—the states where rational actors choose to share or withhold data based on incentives and risks.

### Nash Equilibrium in Data Sharing
In a multi-party setting, organizations face a "prisoner's dilemma": sharing data creates collective value, but withholding data (while others share) might yield a competitive advantage or avoid leakage risks. A Nash equilibrium represents a stable boundary condition where no player has an incentive to deviate from their strategy [cite: 22, 23].
*   **The Payoff Matrix:** The decision to share depends on the "payment matrix," which includes the value of the shared insight, the cost of sharing (technical/legal), and the potential penalty for leakage. Equilibrium boundary conditions are met when the parameters (e.g., penalty levels, technology levels) align such that cooperation is the dominant strategy [cite: 22].
*   **Penalty Mechanisms:** Research suggests that if parameters satisfy specific boundary conditions (e.g., penalties for leakage are sufficiently high relative to the benefits of defection), companies lose the incentive to leak data. If these conditions are not met, the system devolves into non-cooperation or active data leakage [cite: 22, 24].

### Information Pricing and Market Dynamics
The value of data acts as a boundary condition for its exchange. In game-theoretic models, the price of information emerges from strategic competition.
*   **Strategic Complementarity vs. Substitutability:** If data from different parties is complementary (combining them creates new value), the boundary for sharing is lower. If data is substitutable (competitors hold similar data), the boundary is higher, as sharing erodes informational advantage [cite: 25].
*   **Symbiotic Regimes:** Theoretical models identify "symbiotic regimes" where a seller might share data for free to improve overall payoffs, effectively removing the financial boundary to disclosure to achieve a higher-order strategic goal [cite: 25].

### Incentives and Reputation
In repeated games (long-term partnerships), the "shadow of the future" acts as a boundary condition. The threat of future punishment (e.g., exclusion from the data consortium) enforces compliance in the present. However, in one-off interactions, this boundary weakens, necessitating stronger immediate penalties or technical constraints [cite: 23, 24].

## Organizational and Sector-Specific Boundaries

The abstract definitions of boundaries manifest differently across various sectors, influenced by the specific sensitivity of the data and the culture of the organizations involved.

### Healthcare and Genomics
In healthcare, the boundary conditions are extremely tight due to the sensitivity of Protected Health Information (PHI).
*   **Unstructured Data:** Traditional anonymization fails with unstructured text (e.g., doctor's notes). New boundary conditions involve privacy-preserving classification schemes that allow analysis of unstructured text without revealing patient identities [cite: 26].
*   **Genomic Privacy:** SMPC is used to derive genomic diagnoses without revealing patient genomes. The boundary here is biological; since a genome is a unique identifier, it cannot be "anonymized" in the traditional sense, requiring cryptographic isolation [cite: 18].

### Financial Services
Financial institutions use boundary conditions to balance fraud detection with banking secrecy laws.
*   **Fraud Detection:** Banks want to share transaction data to identify money laundering rings but cannot reveal customer details to competitors. SMPC allows them to compute the intersection of their "suspicious activity" lists without revealing the lists themselves [cite: 27].
*   **Competitive Boundaries:** The boundary condition is often "competitive neutrality"—sharing is permitted only if it does not reveal proprietary trading strategies or client lists [cite: 15].

### Public Sector and Administrative Data
Government agencies face statutory boundary conditions regarding "administrative data."
*   **Silos and Integration:** Legal mandates often trap data in agency silos. DSAs in the public sector must navigate complex webs of regulations (e.g., tax laws vs. health laws). The boundary condition is often the "public interest"—disclosure is permitted only if it serves a clearly defined public good [cite: 28, 29].
*   **Trusted Research Environments (TREs):** The public sector increasingly uses TREs (or Data Safe Havens) as a physical/digital boundary. Data never leaves the secure environment; researchers only access it remotely under strict supervision, and only aggregated results are allowed to cross the boundary out [cite: 28].

## Emerging Challenges and Future Directions

The definition of boundary conditions is not static; it evolves with technology and the threat landscape.

### AI and Federated Learning
Federated Learning (FL) introduces a new boundary paradigm: "move the model, not the data." Instead of centralizing data, the algorithm travels to the local data stores, learns, and returns only the updated parameters.
*   **Gradient Leakage:** However, research shows that even model updates (gradients) can leak information about the training data. This requires new boundary conditions, such as adding noise to gradients (Differential Privacy) or encrypting the aggregation process (Secure Aggregation) [cite: 20, 30].

### Quantum Threats
Current cryptographic boundaries (like RSA or Elliptic Curve Cryptography used in some MPC protocols) are vulnerable to future quantum computers. The definition of a "secure" boundary is shifting towards Post-Quantum Cryptography (PQC) to ensure long-term data protection [cite: 31].

### The Human Element
Ultimately, boundary conditions are enforced by people. "Social engineering" or insider threats can bypass technical and legal boundaries. Therefore, training and organizational culture are critical components of the boundary framework. The "boundary" is only as strong as the employee's understanding of their obligations [cite: 32].

## Conclusion

Defining boundary conditions for information disclosure in multi-party data sharing is a complex exercise in risk management. It requires the alignment of **legal instruments** (to define rights and liabilities), **cryptographic protocols** (to enforce technical secrecy), and **economic incentives** (to ensure rational cooperation).

A robust data sharing ecosystem does not rely on a single boundary but on a "defense in depth" strategy. A Data Sharing Agreement provides the mandate; Secure Multi-Party Computation provides the mechanism; and Game Theoretic equilibrium provides the sustainability. As data becomes increasingly vital to solving global challenges—from pandemics to financial crime—the ability to precisely define and enforce these boundary conditions will determine the success of the digital economy.

## References

*   **[cite: 4]** Dataversity. (2023). *What Are Data Sharing Agreements and Why Are They Important?*
*   **[cite: 3]** University of Cambridge. *Guidance on Data Sharing.*
*   **[cite: 8]** ICO. *Data Sharing Agreements Code of Practice.*
*   **[cite: 5]** Partisia. (2025). *Data Sharing Agreement Best Practices.*
*   **[cite: 1]** Information Governance Services. (2026). *Everything You Need to Know About Data Sharing Agreements.*
*   **[cite: 31]** GeeksforGeeks. (2025). *What is Secure Multiparty Computation?*
*   **[cite: 13]** Merino, L.-H., & Cabrero-Holgueras, J. *Secure Multi-Party Computation.*
*   **[cite: 14]** Wikipedia. *Secure Multi-Party Computation.*
*   **[cite: 17]** TechTarget. (2024). *What is Secure Multiparty Computation (SMPC)?*
*   **[cite: 27]** EDPS. (2025). *Secure Multi-Party Computation: Powering Privacy Through Collaboration.*
*   **[cite: 28]** MIT. *Administrative Data Handbook: Data Use Agreements.*
*   **[cite: 19]** Emergent Mind. (2026). *Privacy-Preserving Data Processing.*
*   **[cite: 15]** ISACA. (2021). *Privacy-Preserving Analytics and Secure Multiparty Computation.*
*   **[cite: 26]** IEEE. (2024). *Privacy-Preserving Multiparty Scheme for Unstructured Text.*
*   **[cite: 18]** Medium. (2018). *Overview of Privacy-Preserving Software Methods.*
*   **[cite: 20]** Dialzara. (2024). *Privacy-Preserving Data Sharing Guide for Edge Networks.*
*   **[cite: 30]** ResearchGate. (2025). *Privacy-Preserving and Federated Learning for Regulated Data Ecosystems.*
*   **[cite: 21]** Acs, G., et al. (2014). *Differential Privacy in Data Analysis.*
*   **[cite: 6]** JAMIA. (2020). *Limited Agreements and Temporal Boundaries.*
*   **[cite: 22]** MDPI. (2021). *Game Theory Model of Data Sharing and Leakage.*
*   **[cite: 9]** TandF Online. (2022). *Contracts as Boundary Objects.*
*   **[cite: 16]** AEPD. (2022). *Privacy by Design: Secure Multi-Party Computation.*
*   **[cite: 4]** Dataversity. (2023). *Purpose of Data Sharing Agreements.*
*   **[cite: 2]** ResearchGate. (2025). *A Design Phase for Data Sharing Agreements.*
*   **[cite: 7]** FPF. (2020). *Contract Guidelines for Data Sharing.*
*   **[cite: 11]** ResearchGate. (2023). *The Contract and Boundary Objects Nested Within.*
*   **[cite: 12]** TandF Online. (2022). *Information Sharing in Public-Private Relationships.*
*   **[cite: 10]** WorldCC. (2019). *Contracts as Boundary Objects.*
*   **[cite: 24]** TandF Online. (2021). *Game Theory and Environmental Standards.*
*   **[cite: 23]** Arxiv. (2009). *Game Theoretic Approach to P2P Systems.*
*   **[cite: 25]** Arxiv. (2025). *Game Theoretic Approach to Information Pricing.*
*   **[cite: 33]** PubMed. (2021). *Privacy Disclosure Risks in Multiple Records per Person.*

**Sources:**
1. [informationgovernanceservices.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5NC3P13SB385hmunfrgowexv3Q8IRkr19izqEDzw8zlULXkkg5lRzwJgsFfShD9J_GlKIn0KJ9sPSI9RernDKbEheQFQDcr5YImx2ucFABtm7xFfm64NaiJfw75J7DrbNQDiTFWYdOhZ8KyrmfYJa6uy3FN0Qv4bnMjupP1qQH2w2g1zha8qqtbWv96QluupeXi3ZS1E8p-nwKoGN3owMv6NE3zcQ)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdtwWie29oBz93UTBjhgHfDUPsrBQDHmJf4YyHlIJUkDcYQ6PO03vooQKy4PK0ke00yOZzm0Mb51Iv2-Sc7k2f8iDkKROJm1d9R3CxDbl4S6J_0ZVXIT4a4q8DaR1GvN-BgLl3YT_-VzN9os7W9vBOD4nvBW63MqT-z7adfRUuSIdDkMDNri__HLspicKqII-8vQ==)
3. [cam.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtbXEkt3E7tEx-Boi5WKp1vzJaTw8jZAAGMvnnWbXAyb7OjmQL8pR2-TOnqZSE1gIzXMGPcJnY9gRLXpiBCf9xGBaM5dMXQC6WeHVYkVgR-oIhH7tDR0DQvW451DZ3Kzk4zqDNTOf9LEcb1UnHM8V5b9qDCgvpVKZY4YugymDVuhYYfyaQB2AizUymqrI=)
4. [dataversity.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqltRIg-oMU1xhIoxvU9gPJMA3pp63Vo5WnDjn8-CrSFAPI-RBIFVR7AQlRaOHaSq310fehgaiMqk1Z9Fq4TU4fti1Q_yTll1trD7wYlhuusdpkSDio9tr0SqQuqfrC50Yw1Gl0C_RVb6J9I4R93c6J3OZVSRUjS5q5SA3iw91VgIIyrxITzXR1lshCMoqSl3N2YvFu5s=)
5. [partisia.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5a0y9xhUXfY9s5F32I2DkJtt9zZcxnK6fockAhjHUVpfEiRGdsT1Fnr7lseTS_qPi-AD6Iui3gBlQs7nqwMOGV7NSW2HPbyAMQlfThvowWMqLSJT0u4gzLIXwJKTZUEkQpCcICXC17Ig=)
6. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4z9KqiBrJAJlj5lHxDZDK-mQvX-5Y1cdmXD_Pq9uLOgKRxOq7fiWsQQX7_QX82iMSNkDB-pBRwGKavuejM9y5qw5Mqzmnbvlw1Muzr3Qj5Hpp1x7sIF8H097M_LeVRLWtWNDFu-0Z8GiiFPQ=)
7. [fpf.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHn8krHa90-Z54Zo5rw-lw5gwtbwBtba74sQ5Ch3ldS79Di8nlLU-fE2ju5edcUkErwmU9LUle1Wgimt46VD2f7yyIdvBDYqurkyhTB9kDhRf5VzlVkvmUNw2q144EhNxaONVjQsm0srYxEUrQvs5mtGdQ09Z9lxMFS08M-lM=)
8. [ico.org.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpF6Swi3dkUoi2ONQGh1WnQ4Zf2pNdN4z_rKLEQ2tiHwB9O47dD9EoosFzIvaHOphF-PhitdQZ0kk-Ke0G_bn1uJylsQzA8-CSz0zNhxG7x9i6tQJBd4txJ6GcCftx7z0aZluDNy_7wx7TMBKp6qOjAXfj6guFSFr2C9CwqSDxnlkShq0IbsmY5eRlj374jiiwK6iRHkv1gZ4TC4KkrqC8WbVTLOAJtIQ5jRqTOVtEZ1fGrotWW-ArmyW_bGB6gQ==)
9. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9uKiTgEKJfMmEBztbMoh8Yh1BIMPmadbFnK-DHM0lmnP041nMvwdecVtv0LgJqJ0fWY89Qt3K-qxlb3h1_-V_2u26Mo9O21CJnnXCURCVuS5jpinFDP0_4bPEwMG7jOpHqxYPpNG5Ddxm3EOf9zOCGKmQiV8qgg==)
10. [worldcc.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqewVTr719iY_AUc8e4qCfavdWX9Moguvz4sJKnIlAW8VHHJYCYK8mkBaw4u8aUG8RpjS6CzLZJfFVQbuLXd08LHCY384k_U00mWgVDZNLrbzXjSe2ZYv0V7vaay-WMlMS21Cti2CQGxx7hP34RtRfa3BVIlJY6_dg7lcHUwPfWYRJ3AGUT_b5LcGFJJPBuxlloXTmKDRKGWcRs-Jy)
11. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7fegUmh3dGVC2ONbOcP-yEzDNBuP4h1Jpq5ZTiPov8c-oagCsZVrD07bdteKPf6nUeIo-qrrezWwvavm9t89zl4NHsjLHNTLzxSuII4NnuW-WG9GG8fFhkqi2rh0YKjZTq7ECFyAdHN1jyGrhfB23dmdKf6eXKzpLJwnsitJdSYcjd3gGPi9wpUqdG1ikUTdk-S4PhYrr)
12. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2kdZOKqV2joV88KsOXONwXIdAmPrGAyklZlXTmMXdpD9CGHEo9Vl9IqPK4s0nNk5AY4mVSkV_9rPqBs9ZkVdt4kV7AhJeJgsM1ZnjFNhCwXsSfhSsPF3lkGFyPZLreq78j8ChWuk61_OFQuPmXyttf5TiLhFq)
13. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKCaPmyjNf4j1pHdBziscVdWTIQaTVkpLn4DKIuUzWzGBZYAf-QdftrUm6A5iaKldqWOBLIQAcDHcVI-dRHeX5Gq39POc4g3BjqFw4qtmREV9Blx8QkgvIEC9bMBGKkkSC5VGQOU0CUJf4wz_K7eUgLhW1JokQZzB1hWohFavGzsvfRPtlPQ==)
14. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPrPEGEsJfVkhlLY0xjIQehr5OquTdkE280ObnPNJzPV0pO4R_NKIFso5_6CHSGSL_5OGVzb31z5EbJ7ldjgQlHkdoifTVy-j3rIxLOONjSFK3Xdn14PpZ69XnDEl-BjNUX7_ElfEz9h-w0sUu-ovE7Q==)
15. [isaca.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeCQnK59Lk33qMmYNo2jLp-2KseVM6K8rc0g77nCrfjZHh0LV9i_6MD7w0JQCCfL1Odhtd2DyCMydcOAL8G_zfWQXw6wpwtGrGM8k7ybXJbLwnPCwhYHK96HvBVNKiAtu31aT1vKey7JMjrbxF0X8vtPcbQUQKH7J90h45hkv49KhWQ_E8qQKjXcul1_nVfQnPvPnqPClrgtCi_46XZLoJ868n5WYSY0ftU6PPb78yeGtQ7nX3Ljo=)
16. [aepd.es](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcJL9Y3mQ_Y-MORDKYeAy9xaiwuKf4yCTTi4uBss0P4SMfPmnca3FFl8k7sxbu_BnqQ6Dq4uEWoOdtCpAi37hHA9g-fD4wbGgd-DWYbVS9vT0X42ORwg5Li8mri_ua66ECiinqTX0nw4kqX44V6EIHbiowaLdHRKAwehUV3-G1f75sTHtHWKoZqed4TMNnn5tQBoctKCDTiDRi-Eg-gxFoU5MxaOv_8dyoF8u2a3BG)
17. [techtarget.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4mjp7vgHKfE0DS7svcNnN00aokvTvjUc8AtjGDwfdAPcQ8iFYS2BCGD0nEiFqh46_K9CsGjEz2l95Cs7BgCYL_KKLmk2eAB9GduAQSLEYVz1h04-8moznTGzt-dQnxlDU4Q8J6IAQVBQ50oZ0nnG4Nsw2kXPHw9G0_mZCf4QDk4cq89rz4OYA7Nai1w==)
18. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErxpcYaEkOwtGCwq_TBk02JquyGG9yody5_4P5eVDSg159Jl1KB3ro34N0L8DlPQI8hWT8lcHrR4D5XRn7CWSoYiGki-5gzgRIysU3KMT9oeeQWNH0S-_3vxFc1ShCk-iIEXyMMbQImF3kLNhOcRLIaV3tabLiGhBpPNFG1PqsRONMmoxR3IA2XOgkxqSzaLo1tDUdJgd3ZBu5int3vZbG1SmcfE15y2rx42-X8uBHc2j9dmzkjl-Pv22QhvvObxGC)
19. [emergentmind.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGN8MlEp7_GrcXF9YaSLko0s1Hyuxcag9fRogWm9N8YAAxRHroSJO7z3zpo9208Oil_V5HyjsG1lsBZo-U8UbDUAl_H7vc9mmeMIyBYRfaqykCEoX3E5WGNHzPd3ES6iJ8EBs7T9Xdz4r1p0-uqvkOe-DuqPPq9_ktSIW0=)
20. [dialzara.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFu2gMyMGacW88WC8nTv9LoWefY97tGeMllx6Dd-R2-ZtVYP958bIaJY2YjvjYNAqTgPJjke-mNQ6NzMWnu7eVVG5jRBzM5xUC4GQjnJnms0gFsAOr5LchvCqj7rcAGjtAM_P4iIE3rOl1n_OFZJmDjLAjjhOF5bxdZV1ACRFWOFXdpTyPiQ==)
21. [crysys.hu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAIsDjdSq3Tkh1QJQl6pAJfbWQDBpoir1SKaHvRvZn2klMAIsudxZicQYL2hnrWqK-_5bUrWx6dtBcgN7zsBDJJMgbwAriyn5TjNyPlCS2JZ7spMDxBePvSR1iLIwo5bHMUtBlEvn3-F_C)
22. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHowJ9ZOusYcmT2iP4bzX_O_oGQJXBBPl4E9HDb73DXH5HDVmgZakl2IAEH_rBVdGC0tGbb2p5EnwNwKuBeoksOtP8ar9U8xPMQC2wvrKWyvLOzxPnXkOPsD4Tkw==)
23. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkK1d6tFcpvpbgPvBlu0wHCT45Ch0G5EDaoHUatYmqUJalE3vOx0MKwEIM1xOCICRgagREFBHQPGGLIcckwOf3Ro_rZiZlHWA7zFLrKwLfSl_VQsk=)
24. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEn-ycWnguyhSgDm7EV0kub1xq0du3i0oE7W7bSVRnVVIY9sN1ZOa2HifxYbZnPOVYnP9UABAjKm8UW902HMfGNGeC-fx0mrLVw4g8j6OZf8Vppf1doIEFYx5dGIEmtP2hFALJlHW5quU6Q2gkFJyIYhYEKH7snuA==)
25. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6YKw4NGvoD207P_HJvdYKJFkVJDDQBlINDmkYOsMeDefLQn5MEFsxdWqUzkPTMAoTTZJ7B_WZr5eT7BrhOHwDaNDGYKCkDur4I7ib0WWnxIRoxi_n)
26. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_zrCVIkGXE8-66B-yf2s77cIhs0Reb9M-B0ZwvMVdVoXZoGB_Wr_ZrgGperMhKlmf6OXeT7cmyn5dYmss0HC3vxXkVFJJ5g-TmHdUzHTqiQp4tp1ewRg_6BaY0pnQe3Ek5bk=)
27. [europa.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGK_lmRftF4FNw4SlckUiHATf6er09pwUywP9lJ6OCgHtOCZw0-lKI4ko_c0sIct5b6xKywNFS7UtBjd0wjRyFS5Q62v0X9XBCVOyiH4_bPj7aOVLMFB0T4eXdya3Srhpxhh-A7Ob9Au3bSBhNQp25KbfTYcVdfMyVd-Evsjk1SoA6pdLYZ8-MX8kdzfkcnkaRy8YqjInG6Q0QmVzAQpQyVVvgAc2tyom_QxMJkOGHXEfUn0nOX4mlL7zo6cg==)
28. [mit.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEisTnRgX9Kd9cB70OSJBxYlH6qGceObGojf1GeLceog7dvSpHJqo0KuIxcDzlbOmepKG41BXiacP8rHdcqNtHlxB2XhyX2AJbdqMAdtu-AwlSd1ao7FeNoWup_WXKh1TMkSD73R8uS4wfGA6p)
29. [csg.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_emR96JoLd0KTfOtXyh5ykeFdYbWb0rB9_uAIUpNed2BvhPv4WCZKyBLyeTQ5nLK9grwGQdgXAOB0RgiyYEtwlwaiTURiPLOFrjllg0rS7UEmxwYZ7sOGptiiryUR8rd4lw2U2C9abigxHZ2XtGOOaU3wXTpC_9MdufDRxndQNhFl3zO6VeIBPuMIR_l2g_e1Cb-zt2iITw==)
30. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAr5sxDATjiAgYuzyFJhJ2eU5e6LT1Ll8JcDtmzfgvpps-bAveIZuHuPf14eOdJQUB2zcwai2bJtgXyzHUc6KlK6YKiQliCHxKHPgwDVwSBU_w9oFz4DzQgH77x9YbGKhwze1BytFOxCZlK5HhvSBiMZYM5l5T1j52nhybAeuH8aj_bWn9Yp1BIo8fwtU1ky5enNF5PVpEi-rVYgtiMWadu4tnkoFuLy9dtau6LBpa)
31. [geeksforgeeks.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOefl0Nut_tPt3FL7KsHOUGsybEZ6Hb74nBYBS2AYOMZzaOD_3eARdVdnri2I33aJzXz2E1DEj_CTimPuhrzxmD_270l9hSjg3t29UBrx63TaU5ybMSG9hOcgVzmmmX-CUf9_Pu3SxtpA3JokLohAOCIsLTRi8CnBNes9-EE3-)
32. [connectedautomateddriving.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHq-qhtZ1sob2HpbjWKImOWGi-z5VyaZzfiM3qqu_w0kG_kd1v_JRZXVIjfCjDfwLEWRxBx_sxNP96O6TZex1MYOEn8ushukVhE1-L6NvNXX4D4Yp9Xl1ANIkDDTVflUbsus7-FSFu3lvlAhUJqGz7m7gFolsKUZFhLn4TXB6rOn_7BMSs2x8xRNXSJhnqf)
33. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH86X40YfwD332Dk083pWKV1zbnM0RIsvYAe3zS76Tu43WU409sJQ2XR3VDgt6-SuEx4wozj-jO2NrNVXpdrhDAlqhvDfLw0-yUARnhPAjVbjnK785eng7ayvRB16fj)


## Annotations
Annotation(end_index=3535, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdtwWie29oBz93UTBjhgHfDUPsrBQDHmJf4YyHlIJUkDcYQ6PO03vooQKy4PK0ke00yOZzm0Mb51Iv2-Sc7k2f8iDkKROJm1d9R3CxDbl4S6J_0ZVXIT4a4q8DaR1GvN-BgLl3YT_-VzN9os7W9vBOD4nvBW63MqT-z7adfRUuSIdDkMDNri__HLspicKqII-8vQ==', start_index=3523)
Annotation(end_index=3535, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5NC3P13SB385hmunfrgowexv3Q8IRkr19izqEDzw8zlULXkkg5lRzwJgsFfShD9J_GlKIn0KJ9sPSI9RernDKbEheQFQDcr5YImx2ucFABtm7xFfm64NaiJfw75J7DrbNQDiTFWYdOhZ8KyrmfYJa6uy3FN0Qv4bnMjupP1qQH2w2g1zha8qqtbWv96QluupeXi3ZS1E8p-nwKoGN3owMv6NE3zcQ', start_index=3523)
Annotation(end_index=3976, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtbXEkt3E7tEx-Boi5WKp1vzJaTw8jZAAGMvnnWbXAyb7OjmQL8pR2-TOnqZSE1gIzXMGPcJnY9gRLXpiBCf9xGBaM5dMXQC6WeHVYkVgR-oIhH7tDR0DQvW451DZ3Kzk4zqDNTOf9LEcb1UnHM8V5b9qDCgvpVKZY4YugymDVuhYYfyaQB2AizUymqrI=', start_index=3964)
Annotation(end_index=3976, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqltRIg-oMU1xhIoxvU9gPJMA3pp63Vo5WnDjn8-CrSFAPI-RBIFVR7AQlRaOHaSq310fehgaiMqk1Z9Fq4TU4fti1Q_yTll1trD7wYlhuusdpkSDio9tr0SqQuqfrC50Yw1Gl0C_RVb6J9I4R93c6J3OZVSRUjS5q5SA3iw91VgIIyrxITzXR1lshCMoqSl3N2YvFu5s=', start_index=3964)
Annotation(end_index=4318, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5a0y9xhUXfY9s5F32I2DkJtt9zZcxnK6fockAhjHUVpfEiRGdsT1Fnr7lseTS_qPi-AD6Iui3gBlQs7nqwMOGV7NSW2HPbyAMQlfThvowWMqLSJT0u4gzLIXwJKTZUEkQpCcICXC17Ig=', start_index=4309)
Annotation(end_index=4588, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4z9KqiBrJAJlj5lHxDZDK-mQvX-5Y1cdmXD_Pq9uLOgKRxOq7fiWsQQX7_QX82iMSNkDB-pBRwGKavuejM9y5qw5Mqzmnbvlw1Muzr3Qj5Hpp1x7sIF8H097M_LeVRLWtWNDFu-0Z8GiiFPQ=', start_index=4576)
Annotation(end_index=4588, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5a0y9xhUXfY9s5F32I2DkJtt9zZcxnK6fockAhjHUVpfEiRGdsT1Fnr7lseTS_qPi-AD6Iui3gBlQs7nqwMOGV7NSW2HPbyAMQlfThvowWMqLSJT0u4gzLIXwJKTZUEkQpCcICXC17Ig=', start_index=4576)
Annotation(end_index=4925, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4z9KqiBrJAJlj5lHxDZDK-mQvX-5Y1cdmXD_Pq9uLOgKRxOq7fiWsQQX7_QX82iMSNkDB-pBRwGKavuejM9y5qw5Mqzmnbvlw1Muzr3Qj5Hpp1x7sIF8H097M_LeVRLWtWNDFu-0Z8GiiFPQ=', start_index=4913)
Annotation(end_index=4925, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHn8krHa90-Z54Zo5rw-lw5gwtbwBtba74sQ5Ch3ldS79Di8nlLU-fE2ju5edcUkErwmU9LUle1Wgimt46VD2f7yyIdvBDYqurkyhTB9kDhRf5VzlVkvmUNw2q144EhNxaONVjQsm0srYxEUrQvs5mtGdQ09Z9lxMFS08M-lM=', start_index=4913)
Annotation(end_index=5376, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqltRIg-oMU1xhIoxvU9gPJMA3pp63Vo5WnDjn8-CrSFAPI-RBIFVR7AQlRaOHaSq310fehgaiMqk1Z9Fq4TU4fti1Q_yTll1trD7wYlhuusdpkSDio9tr0SqQuqfrC50Yw1Gl0C_RVb6J9I4R93c6J3OZVSRUjS5q5SA3iw91VgIIyrxITzXR1lshCMoqSl3N2YvFu5s=', start_index=5364)
Annotation(end_index=5376, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5a0y9xhUXfY9s5F32I2DkJtt9zZcxnK6fockAhjHUVpfEiRGdsT1Fnr7lseTS_qPi-AD6Iui3gBlQs7nqwMOGV7NSW2HPbyAMQlfThvowWMqLSJT0u4gzLIXwJKTZUEkQpCcICXC17Ig=', start_index=5364)
Annotation(end_index=5918, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqltRIg-oMU1xhIoxvU9gPJMA3pp63Vo5WnDjn8-CrSFAPI-RBIFVR7AQlRaOHaSq310fehgaiMqk1Z9Fq4TU4fti1Q_yTll1trD7wYlhuusdpkSDio9tr0SqQuqfrC50Yw1Gl0C_RVb6J9I4R93c6J3OZVSRUjS5q5SA3iw91VgIIyrxITzXR1lshCMoqSl3N2YvFu5s=', start_index=5909)
Annotation(end_index=6118, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpF6Swi3dkUoi2ONQGh1WnQ4Zf2pNdN4z_rKLEQ2tiHwB9O47dD9EoosFzIvaHOphF-PhitdQZ0kk-Ke0G_bn1uJylsQzA8-CSz0zNhxG7x9i6tQJBd4txJ6GcCftx7z0aZluDNy_7wx7TMBKp6qOjAXfj6guFSFr2C9CwqSDxnlkShq0IbsmY5eRlj374jiiwK6iRHkv1gZ4TC4KkrqC8WbVTLOAJtIQ5jRqTOVtEZ1fGrotWW-ArmyW_bGB6gQ==', start_index=6109)
Annotation(end_index=6307, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtbXEkt3E7tEx-Boi5WKp1vzJaTw8jZAAGMvnnWbXAyb7OjmQL8pR2-TOnqZSE1gIzXMGPcJnY9gRLXpiBCf9xGBaM5dMXQC6WeHVYkVgR-oIhH7tDR0DQvW451DZ3Kzk4zqDNTOf9LEcb1UnHM8V5b9qDCgvpVKZY4YugymDVuhYYfyaQB2AizUymqrI=', start_index=6298)
Annotation(end_index=6649, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtbXEkt3E7tEx-Boi5WKp1vzJaTw8jZAAGMvnnWbXAyb7OjmQL8pR2-TOnqZSE1gIzXMGPcJnY9gRLXpiBCf9xGBaM5dMXQC6WeHVYkVgR-oIhH7tDR0DQvW451DZ3Kzk4zqDNTOf9LEcb1UnHM8V5b9qDCgvpVKZY4YugymDVuhYYfyaQB2AizUymqrI=', start_index=6640)
Annotation(end_index=7105, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqewVTr719iY_AUc8e4qCfavdWX9Moguvz4sJKnIlAW8VHHJYCYK8mkBaw4u8aUG8RpjS6CzLZJfFVQbuLXd08LHCY384k_U00mWgVDZNLrbzXjSe2ZYv0V7vaay-WMlMS21Cti2CQGxx7hP34RtRfa3BVIlJY6_dg7lcHUwPfWYRJ3AGUT_b5LcGFJJPBuxlloXTmKDRKGWcRs-Jy', start_index=7092)
Annotation(end_index=7105, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9uKiTgEKJfMmEBztbMoh8Yh1BIMPmadbFnK-DHM0lmnP041nMvwdecVtv0LgJqJ0fWY89Qt3K-qxlb3h1_-V_2u26Mo9O21CJnnXCURCVuS5jpinFDP0_4bPEwMG7jOpHqxYPpNG5Ddxm3EOf9zOCGKmQiV8qgg==', start_index=7092)
Annotation(end_index=7423, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7fegUmh3dGVC2ONbOcP-yEzDNBuP4h1Jpq5ZTiPov8c-oagCsZVrD07bdteKPf6nUeIo-qrrezWwvavm9t89zl4NHsjLHNTLzxSuII4NnuW-WG9GG8fFhkqi2rh0YKjZTq7ECFyAdHN1jyGrhfB23dmdKf6eXKzpLJwnsitJdSYcjd3gGPi9wpUqdG1ikUTdk-S4PhYrr', start_index=7409)
Annotation(end_index=7423, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2kdZOKqV2joV88KsOXONwXIdAmPrGAyklZlXTmMXdpD9CGHEo9Vl9IqPK4s0nNk5AY4mVSkV_9rPqBs9ZkVdt4kV7AhJeJgsM1ZnjFNhCwXsSfhSsPF3lkGFyPZLreq78j8ChWuk61_OFQuPmXyttf5TiLhFq', start_index=7409)
Annotation(end_index=7768, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9uKiTgEKJfMmEBztbMoh8Yh1BIMPmadbFnK-DHM0lmnP041nMvwdecVtv0LgJqJ0fWY89Qt3K-qxlb3h1_-V_2u26Mo9O21CJnnXCURCVuS5jpinFDP0_4bPEwMG7jOpHqxYPpNG5Ddxm3EOf9zOCGKmQiV8qgg==', start_index=7759)
Annotation(end_index=8372, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKCaPmyjNf4j1pHdBziscVdWTIQaTVkpLn4DKIuUzWzGBZYAf-QdftrUm6A5iaKldqWOBLIQAcDHcVI-dRHeX5Gq39POc4g3BjqFw4qtmREV9Blx8QkgvIEC9bMBGKkkSC5VGQOU0CUJf4wz_K7eUgLhW1JokQZzB1hWohFavGzsvfRPtlPQ==', start_index=8358)
Annotation(end_index=8372, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPrPEGEsJfVkhlLY0xjIQehr5OquTdkE280ObnPNJzPV0pO4R_NKIFso5_6CHSGSL_5OGVzb31z5EbJ7ldjgQlHkdoifTVy-j3rIxLOONjSFK3Xdn14PpZ69XnDEl-BjNUX7_ElfEz9h-w0sUu-ovE7Q==', start_index=8358)
Annotation(end_index=8884, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPrPEGEsJfVkhlLY0xjIQehr5OquTdkE280ObnPNJzPV0pO4R_NKIFso5_6CHSGSL_5OGVzb31z5EbJ7ldjgQlHkdoifTVy-j3rIxLOONjSFK3Xdn14PpZ69XnDEl-BjNUX7_ElfEz9h-w0sUu-ovE7Q==', start_index=8874)
Annotation(end_index=9030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeCQnK59Lk33qMmYNo2jLp-2KseVM6K8rc0g77nCrfjZHh0LV9i_6MD7w0JQCCfL1Odhtd2DyCMydcOAL8G_zfWQXw6wpwtGrGM8k7ybXJbLwnPCwhYHK96HvBVNKiAtu31aT1vKey7JMjrbxF0X8vtPcbQUQKH7J90h45hkv49KhWQ_E8qQKjXcul1_nVfQnPvPnqPClrgtCi_46XZLoJ868n5WYSY0ftU6PPb78yeGtQ7nX3Ljo=', start_index=9016)
Annotation(end_index=9030, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPrPEGEsJfVkhlLY0xjIQehr5OquTdkE280ObnPNJzPV0pO4R_NKIFso5_6CHSGSL_5OGVzb31z5EbJ7ldjgQlHkdoifTVy-j3rIxLOONjSFK3Xdn14PpZ69XnDEl-BjNUX7_ElfEz9h-w0sUu-ovE7Q==', start_index=9016)
Annotation(end_index=9313, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcJL9Y3mQ_Y-MORDKYeAy9xaiwuKf4yCTTi4uBss0P4SMfPmnca3FFl8k7sxbu_BnqQ6Dq4uEWoOdtCpAi37hHA9g-fD4wbGgd-DWYbVS9vT0X42ORwg5Li8mri_ua66ECiinqTX0nw4kqX44V6EIHbiowaLdHRKAwehUV3-G1f75sTHtHWKoZqed4TMNnn5tQBoctKCDTiDRi-Eg-gxFoU5MxaOv_8dyoF8u2a3BG', start_index=9303)
Annotation(end_index=9576, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErxpcYaEkOwtGCwq_TBk02JquyGG9yody5_4P5eVDSg159Jl1KB3ro34N0L8DlPQI8hWT8lcHrR4D5XRn7CWSoYiGki-5gzgRIysU3KMT9oeeQWNH0S-_3vxFc1ShCk-iIEXyMMbQImF3kLNhOcRLIaV3tabLiGhBpPNFG1PqsRONMmoxR3IA2XOgkxqSzaLo1tDUdJgd3ZBu5int3vZbG1SmcfE15y2rx42-X8uBHc2j9dmzkjl-Pv22QhvvObxGC', start_index=9562)
Annotation(end_index=9576, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4mjp7vgHKfE0DS7svcNnN00aokvTvjUc8AtjGDwfdAPcQ8iFYS2BCGD0nEiFqh46_K9CsGjEz2l95Cs7BgCYL_KKLmk2eAB9GduAQSLEYVz1h04-8moznTGzt-dQnxlDU4Q8J6IAQVBQ50oZ0nnG4Nsw2kXPHw9G0_mZCf4QDk4cq89rz4OYA7Nai1w==', start_index=9562)
Annotation(end_index=9937, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGN8MlEp7_GrcXF9YaSLko0s1Hyuxcag9fRogWm9N8YAAxRHroSJO7z3zpo9208Oil_V5HyjsG1lsBZo-U8UbDUAl_H7vc9mmeMIyBYRfaqykCEoX3E5WGNHzPd3ES6iJ8EBs7T9Xdz4r1p0-uqvkOe-DuqPPq9_ktSIW0=', start_index=9927)
Annotation(end_index=10405, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeCQnK59Lk33qMmYNo2jLp-2KseVM6K8rc0g77nCrfjZHh0LV9i_6MD7w0JQCCfL1Odhtd2DyCMydcOAL8G_zfWQXw6wpwtGrGM8k7ybXJbLwnPCwhYHK96HvBVNKiAtu31aT1vKey7JMjrbxF0X8vtPcbQUQKH7J90h45hkv49KhWQ_E8qQKjXcul1_nVfQnPvPnqPClrgtCi_46XZLoJ868n5WYSY0ftU6PPb78yeGtQ7nX3Ljo=', start_index=10391)
Annotation(end_index=10405, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFu2gMyMGacW88WC8nTv9LoWefY97tGeMllx6Dd-R2-ZtVYP958bIaJY2YjvjYNAqTgPJjke-mNQ6NzMWnu7eVVG5jRBzM5xUC4GQjnJnms0gFsAOr5LchvCqj7rcAGjtAM_P4iIE3rOl1n_OFZJmDjLAjjhOF5bxdZV1ACRFWOFXdpTyPiQ==', start_index=10391)
Annotation(end_index=10665, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPrPEGEsJfVkhlLY0xjIQehr5OquTdkE280ObnPNJzPV0pO4R_NKIFso5_6CHSGSL_5OGVzb31z5EbJ7ldjgQlHkdoifTVy-j3rIxLOONjSFK3Xdn14PpZ69XnDEl-BjNUX7_ElfEz9h-w0sUu-ovE7Q==', start_index=10655)
Annotation(end_index=11052, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErxpcYaEkOwtGCwq_TBk02JquyGG9yody5_4P5eVDSg159Jl1KB3ro34N0L8DlPQI8hWT8lcHrR4D5XRn7CWSoYiGki-5gzgRIysU3KMT9oeeQWNH0S-_3vxFc1ShCk-iIEXyMMbQImF3kLNhOcRLIaV3tabLiGhBpPNFG1PqsRONMmoxR3IA2XOgkxqSzaLo1tDUdJgd3ZBu5int3vZbG1SmcfE15y2rx42-X8uBHc2j9dmzkjl-Pv22QhvvObxGC', start_index=11038)
Annotation(end_index=11052, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAIsDjdSq3Tkh1QJQl6pAJfbWQDBpoir1SKaHvRvZn2klMAIsudxZicQYL2hnrWqK-_5bUrWx6dtBcgN7zsBDJJMgbwAriyn5TjNyPlCS2JZ7spMDxBePvSR1iLIwo5bHMUtBlEvn3-F_C', start_index=11038)
Annotation(end_index=11308, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAIsDjdSq3Tkh1QJQl6pAJfbWQDBpoir1SKaHvRvZn2klMAIsudxZicQYL2hnrWqK-_5bUrWx6dtBcgN7zsBDJJMgbwAriyn5TjNyPlCS2JZ7spMDxBePvSR1iLIwo5bHMUtBlEvn3-F_C', start_index=11298)
Annotation(end_index=11505, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFu2gMyMGacW88WC8nTv9LoWefY97tGeMllx6Dd-R2-ZtVYP958bIaJY2YjvjYNAqTgPJjke-mNQ6NzMWnu7eVVG5jRBzM5xUC4GQjnJnms0gFsAOr5LchvCqj7rcAGjtAM_P4iIE3rOl1n_OFZJmDjLAjjhOF5bxdZV1ACRFWOFXdpTyPiQ==', start_index=11495)
Annotation(end_index=12239, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkK1d6tFcpvpbgPvBlu0wHCT45Ch0G5EDaoHUatYmqUJalE3vOx0MKwEIM1xOCICRgagREFBHQPGGLIcckwOf3Ro_rZiZlHWA7zFLrKwLfSl_VQsk=', start_index=12225)
Annotation(end_index=12239, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHowJ9ZOusYcmT2iP4bzX_O_oGQJXBBPl4E9HDb73DXH5HDVmgZakl2IAEH_rBVdGC0tGbb2p5EnwNwKuBeoksOtP8ar9U8xPMQC2wvrKWyvLOzxPnXkOPsD4Tkw==', start_index=12225)
Annotation(end_index=12614, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHowJ9ZOusYcmT2iP4bzX_O_oGQJXBBPl4E9HDb73DXH5HDVmgZakl2IAEH_rBVdGC0tGbb2p5EnwNwKuBeoksOtP8ar9U8xPMQC2wvrKWyvLOzxPnXkOPsD4Tkw==', start_index=12604)
Annotation(end_index=12963, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEn-ycWnguyhSgDm7EV0kub1xq0du3i0oE7W7bSVRnVVIY9sN1ZOa2HifxYbZnPOVYnP9UABAjKm8UW902HMfGNGeC-fx0mrLVw4g8j6OZf8Vppf1doIEFYx5dGIEmtP2hFALJlHW5quU6Q2gkFJyIYhYEKH7snuA==', start_index=12949)
Annotation(end_index=12963, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHowJ9ZOusYcmT2iP4bzX_O_oGQJXBBPl4E9HDb73DXH5HDVmgZakl2IAEH_rBVdGC0tGbb2p5EnwNwKuBeoksOtP8ar9U8xPMQC2wvrKWyvLOzxPnXkOPsD4Tkw==', start_index=12949)
Annotation(end_index=13471, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6YKw4NGvoD207P_HJvdYKJFkVJDDQBlINDmkYOsMeDefLQn5MEFsxdWqUzkPTMAoTTZJ7B_WZr5eT7BrhOHwDaNDGYKCkDur4I7ib0WWnxIRoxi_n', start_index=13461)
Annotation(end_index=13726, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6YKw4NGvoD207P_HJvdYKJFkVJDDQBlINDmkYOsMeDefLQn5MEFsxdWqUzkPTMAoTTZJ7B_WZr5eT7BrhOHwDaNDGYKCkDur4I7ib0WWnxIRoxi_n', start_index=13716)
Annotation(end_index=14110, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEn-ycWnguyhSgDm7EV0kub1xq0du3i0oE7W7bSVRnVVIY9sN1ZOa2HifxYbZnPOVYnP9UABAjKm8UW902HMfGNGeC-fx0mrLVw4g8j6OZf8Vppf1doIEFYx5dGIEmtP2hFALJlHW5quU6Q2gkFJyIYhYEKH7snuA==', start_index=14096)
Annotation(end_index=14110, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkK1d6tFcpvpbgPvBlu0wHCT45Ch0G5EDaoHUatYmqUJalE3vOx0MKwEIM1xOCICRgagREFBHQPGGLIcckwOf3Ro_rZiZlHWA7zFLrKwLfSl_VQsk=', start_index=14096)
Annotation(end_index=14763, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_zrCVIkGXE8-66B-yf2s77cIhs0Reb9M-B0ZwvMVdVoXZoGB_Wr_ZrgGperMhKlmf6OXeT7cmyn5dYmss0HC3vxXkVFJJ5g-TmHdUzHTqiQp4tp1ewRg_6BaY0pnQe3Ek5bk=', start_index=14753)
Annotation(end_index=15034, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErxpcYaEkOwtGCwq_TBk02JquyGG9yody5_4P5eVDSg159Jl1KB3ro34N0L8DlPQI8hWT8lcHrR4D5XRn7CWSoYiGki-5gzgRIysU3KMT9oeeQWNH0S-_3vxFc1ShCk-iIEXyMMbQImF3kLNhOcRLIaV3tabLiGhBpPNFG1PqsRONMmoxR3IA2XOgkxqSzaLo1tDUdJgd3ZBu5int3vZbG1SmcfE15y2rx42-X8uBHc2j9dmzkjl-Pv22QhvvObxGC', start_index=15024)
Annotation(end_index=15440, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGK_lmRftF4FNw4SlckUiHATf6er09pwUywP9lJ6OCgHtOCZw0-lKI4ko_c0sIct5b6xKywNFS7UtBjd0wjRyFS5Q62v0X9XBCVOyiH4_bPj7aOVLMFB0T4eXdya3Srhpxhh-A7Ob9Au3bSBhNQp25KbfTYcVdfMyVd-Evsjk1SoA6pdLYZ8-MX8kdzfkcnkaRy8YqjInG6Q0QmVzAQpQyVVvgAc2tyom_QxMJkOGHXEfUn0nOX4mlL7zo6cg==', start_index=15430)
Annotation(end_index=15638, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeCQnK59Lk33qMmYNo2jLp-2KseVM6K8rc0g77nCrfjZHh0LV9i_6MD7w0JQCCfL1Odhtd2DyCMydcOAL8G_zfWQXw6wpwtGrGM8k7ybXJbLwnPCwhYHK96HvBVNKiAtu31aT1vKey7JMjrbxF0X8vtPcbQUQKH7J90h45hkv49KhWQ_E8qQKjXcul1_nVfQnPvPnqPClrgtCi_46XZLoJ868n5WYSY0ftU6PPb78yeGtQ7nX3Ljo=', start_index=15628)
Annotation(end_index=16094, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEisTnRgX9Kd9cB70OSJBxYlH6qGceObGojf1GeLceog7dvSpHJqo0KuIxcDzlbOmepKG41BXiacP8rHdcqNtHlxB2XhyX2AJbdqMAdtu-AwlSd1ao7FeNoWup_WXKh1TMkSD73R8uS4wfGA6p', start_index=16080)
Annotation(end_index=16094, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_emR96JoLd0KTfOtXyh5ykeFdYbWb0rB9_uAIUpNed2BvhPv4WCZKyBLyeTQ5nLK9grwGQdgXAOB0RgiyYEtwlwaiTURiPLOFrjllg0rS7UEmxwYZ7sOGptiiryUR8rd4lw2U2C9abigxHZ2XtGOOaU3wXTpC_9MdufDRxndQNhFl3zO6VeIBPuMIR_l2g_e1Cb-zt2iITw==', start_index=16080)
Annotation(end_index=16417, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEisTnRgX9Kd9cB70OSJBxYlH6qGceObGojf1GeLceog7dvSpHJqo0KuIxcDzlbOmepKG41BXiacP8rHdcqNtHlxB2XhyX2AJbdqMAdtu-AwlSd1ao7FeNoWup_WXKh1TMkSD73R8uS4wfGA6p', start_index=16407)
Annotation(end_index=17123, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFu2gMyMGacW88WC8nTv9LoWefY97tGeMllx6Dd-R2-ZtVYP958bIaJY2YjvjYNAqTgPJjke-mNQ6NzMWnu7eVVG5jRBzM5xUC4GQjnJnms0gFsAOr5LchvCqj7rcAGjtAM_P4iIE3rOl1n_OFZJmDjLAjjhOF5bxdZV1ACRFWOFXdpTyPiQ==', start_index=17109)
Annotation(end_index=17123, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAr5sxDATjiAgYuzyFJhJ2eU5e6LT1Ll8JcDtmzfgvpps-bAveIZuHuPf14eOdJQUB2zcwai2bJtgXyzHUc6KlK6YKiQliCHxKHPgwDVwSBU_w9oFz4DzQgH77x9YbGKhwze1BytFOxCZlK5HhvSBiMZYM5l5T1j52nhybAeuH8aj_bWn9Yp1BIo8fwtU1ky5enNF5PVpEi-rVYgtiMWadu4tnkoFuLy9dtau6LBpa', start_index=17109)
Annotation(end_index=17428, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOefl0Nut_tPt3FL7KsHOUGsybEZ6Hb74nBYBS2AYOMZzaOD_3eARdVdnri2I33aJzXz2E1DEj_CTimPuhrzxmD_270l9hSjg3t29UBrx63TaU5ybMSG9hOcgVzmmmX-CUf9_Pu3SxtpA3JokLohAOCIsLTRi8CnBNes9-EE3-', start_index=17418)
Annotation(end_index=17786, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHq-qhtZ1sob2HpbjWKImOWGi-z5VyaZzfiM3qqu_w0kG_kd1v_JRZXVIjfCjDfwLEWRxBx_sxNP96O6TZex1MYOEn8ushukVhE1-L6NvNXX4D4Yp9Xl1ANIkDDTVflUbsus7-FSFu3lvlAhUJqGz7m7gFolsKUZFhLn4TXB6rOn_7BMSs2x8xRNXSJhnqf', start_index=17776)
Annotation(end_index=18661, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqltRIg-oMU1xhIoxvU9gPJMA3pp63Vo5WnDjn8-CrSFAPI-RBIFVR7AQlRaOHaSq310fehgaiMqk1Z9Fq4TU4fti1Q_yTll1trD7wYlhuusdpkSDio9tr0SqQuqfrC50Yw1Gl0C_RVb6J9I4R93c6J3OZVSRUjS5q5SA3iw91VgIIyrxITzXR1lshCMoqSl3N2YvFu5s=', start_index=18652)
Annotation(end_index=18763, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEtbXEkt3E7tEx-Boi5WKp1vzJaTw8jZAAGMvnnWbXAyb7OjmQL8pR2-TOnqZSE1gIzXMGPcJnY9gRLXpiBCf9xGBaM5dMXQC6WeHVYkVgR-oIhH7tDR0DQvW451DZ3Kzk4zqDNTOf9LEcb1UnHM8V5b9qDCgvpVKZY4YugymDVuhYYfyaQB2AizUymqrI=', start_index=18754)
Annotation(end_index=18834, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpF6Swi3dkUoi2ONQGh1WnQ4Zf2pNdN4z_rKLEQ2tiHwB9O47dD9EoosFzIvaHOphF-PhitdQZ0kk-Ke0G_bn1uJylsQzA8-CSz0zNhxG7x9i6tQJBd4txJ6GcCftx7z0aZluDNy_7wx7TMBKp6qOjAXfj6guFSFr2C9CwqSDxnlkShq0IbsmY5eRlj374jiiwK6iRHkv1gZ4TC4KkrqC8WbVTLOAJtIQ5jRqTOVtEZ1fGrotWW-ArmyW_bGB6gQ==', start_index=18825)
Annotation(end_index=18901, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5a0y9xhUXfY9s5F32I2DkJtt9zZcxnK6fockAhjHUVpfEiRGdsT1Fnr7lseTS_qPi-AD6Iui3gBlQs7nqwMOGV7NSW2HPbyAMQlfThvowWMqLSJT0u4gzLIXwJKTZUEkQpCcICXC17Ig=', start_index=18892)
Annotation(end_index=18978, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5NC3P13SB385hmunfrgowexv3Q8IRkr19izqEDzw8zlULXkkg5lRzwJgsFfShD9J_GlKIn0KJ9sPSI9RernDKbEheQFQDcr5YImx2ucFABtm7xFfm64NaiJfw75J7DrbNQDiTFWYdOhZ8KyrmfYJa6uy3FN0Qv4bnMjupP1qQH2w2g1zha8qqtbWv96QluupeXi3ZS1E8p-nwKoGN3owMv6NE3zcQ', start_index=18969)
Annotation(end_index=19099, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOefl0Nut_tPt3FL7KsHOUGsybEZ6Hb74nBYBS2AYOMZzaOD_3eARdVdnri2I33aJzXz2E1DEj_CTimPuhrzxmD_270l9hSjg3t29UBrx63TaU5ybMSG9hOcgVzmmmX-CUf9_Pu3SxtpA3JokLohAOCIsLTRi8CnBNes9-EE3-', start_index=19089)
Annotation(end_index=19182, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKCaPmyjNf4j1pHdBziscVdWTIQaTVkpLn4DKIuUzWzGBZYAf-QdftrUm6A5iaKldqWOBLIQAcDHcVI-dRHeX5Gq39POc4g3BjqFw4qtmREV9Blx8QkgvIEC9bMBGKkkSC5VGQOU0CUJf4wz_K7eUgLhW1JokQZzB1hWohFavGzsvfRPtlPQ==', start_index=19172)
Annotation(end_index=19274, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPrPEGEsJfVkhlLY0xjIQehr5OquTdkE280ObnPNJzPV0pO4R_NKIFso5_6CHSGSL_5OGVzb31z5EbJ7ldjgQlHkdoifTVy-j3rIxLOONjSFK3Xdn14PpZ69XnDEl-BjNUX7_ElfEz9h-w0sUu-ovE7Q==', start_index=19264)
Annotation(end_index=19338, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4mjp7vgHKfE0DS7svcNnN00aokvTvjUc8AtjGDwfdAPcQ8iFYS2BCGD0nEiFqh46_K9CsGjEz2l95Cs7BgCYL_KKLmk2eAB9GduAQSLEYVz1h04-8moznTGzt-dQnxlDU4Q8J6IAQVBQ50oZ0nnG4Nsw2kXPHw9G0_mZCf4QDk4cq89rz4OYA7Nai1w==', start_index=19328)
Annotation(end_index=19425, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGK_lmRftF4FNw4SlckUiHATf6er09pwUywP9lJ6OCgHtOCZw0-lKI4ko_c0sIct5b6xKywNFS7UtBjd0wjRyFS5Q62v0X9XBCVOyiH4_bPj7aOVLMFB0T4eXdya3Srhpxhh-A7Ob9Au3bSBhNQp25KbfTYcVdfMyVd-Evsjk1SoA6pdLYZ8-MX8kdzfkcnkaRy8YqjInG6Q0QmVzAQpQyVVvgAc2tyom_QxMJkOGHXEfUn0nOX4mlL7zo6cg==', start_index=19415)
Annotation(end_index=19532, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEisTnRgX9Kd9cB70OSJBxYlH6qGceObGojf1GeLceog7dvSpHJqo0KuIxcDzlbOmepKG41BXiacP8rHdcqNtHlxB2XhyX2AJbdqMAdtu-AwlSd1ao7FeNoWup_WXKh1TMkSD73R8uS4wfGA6p', start_index=19522)
Annotation(end_index=19609, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGN8MlEp7_GrcXF9YaSLko0s1Hyuxcag9fRogWm9N8YAAxRHroSJO7z3zpo9208Oil_V5HyjsG1lsBZo-U8UbDUAl_H7vc9mmeMIyBYRfaqykCEoX3E5WGNHzPd3ES6iJ8EBs7T9Xdz4r1p0-uqvkOe-DuqPPq9_ktSIW0=', start_index=19599)
Annotation(end_index=19689, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFeCQnK59Lk33qMmYNo2jLp-2KseVM6K8rc0g77nCrfjZHh0LV9i_6MD7w0JQCCfL1Odhtd2DyCMydcOAL8G_zfWQXw6wpwtGrGM8k7ybXJbLwnPCwhYHK96HvBVNKiAtu31aT1vKey7JMjrbxF0X8vtPcbQUQKH7J90h45hkv49KhWQ_E8qQKjXcul1_nVfQnPvPnqPClrgtCi_46XZLoJ868n5WYSY0ftU6PPb78yeGtQ7nX3Ljo=', start_index=19679)
Annotation(end_index=19789, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_zrCVIkGXE8-66B-yf2s77cIhs0Reb9M-B0ZwvMVdVoXZoGB_Wr_ZrgGperMhKlmf6OXeT7cmyn5dYmss0HC3vxXkVFJJ5g-TmHdUzHTqiQp4tp1ewRg_6BaY0pnQe3Ek5bk=', start_index=19779)
Annotation(end_index=19884, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErxpcYaEkOwtGCwq_TBk02JquyGG9yody5_4P5eVDSg159Jl1KB3ro34N0L8DlPQI8hWT8lcHrR4D5XRn7CWSoYiGki-5gzgRIysU3KMT9oeeQWNH0S-_3vxFc1ShCk-iIEXyMMbQImF3kLNhOcRLIaV3tabLiGhBpPNFG1PqsRONMmoxR3IA2XOgkxqSzaLo1tDUdJgd3ZBu5int3vZbG1SmcfE15y2rx42-X8uBHc2j9dmzkjl-Pv22QhvvObxGC', start_index=19874)
Annotation(end_index=19970, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFu2gMyMGacW88WC8nTv9LoWefY97tGeMllx6Dd-R2-ZtVYP958bIaJY2YjvjYNAqTgPJjke-mNQ6NzMWnu7eVVG5jRBzM5xUC4GQjnJnms0gFsAOr5LchvCqj7rcAGjtAM_P4iIE3rOl1n_OFZJmDjLAjjhOF5bxdZV1ACRFWOFXdpTyPiQ==', start_index=19960)
Annotation(end_index=20066, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAr5sxDATjiAgYuzyFJhJ2eU5e6LT1Ll8JcDtmzfgvpps-bAveIZuHuPf14eOdJQUB2zcwai2bJtgXyzHUc6KlK6YKiQliCHxKHPgwDVwSBU_w9oFz4DzQgH77x9YbGKhwze1BytFOxCZlK5HhvSBiMZYM5l5T1j52nhybAeuH8aj_bWn9Yp1BIo8fwtU1ky5enNF5PVpEi-rVYgtiMWadu4tnkoFuLy9dtau6LBpa', start_index=20056)
Annotation(end_index=20182, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAIsDjdSq3Tkh1QJQl6pAJfbWQDBpoir1SKaHvRvZn2klMAIsudxZicQYL2hnrWqK-_5bUrWx6dtBcgN7zsBDJJMgbwAriyn5TjNyPlCS2JZ7spMDxBePvSR1iLIwo5bHMUtBlEvn3-F_C', start_index=20172)
Annotation(end_index=20265, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4z9KqiBrJAJlj5lHxDZDK-mQvX-5Y1cdmXD_Pq9uLOgKRxOq7fiWsQQX7_QX82iMSNkDB-pBRwGKavuejM9y5qw5Mqzmnbvlw1Muzr3Qj5Hpp1x7sIF8H097M_LeVRLWtWNDFu-0Z8GiiFPQ=', start_index=20256)
Annotation(end_index=20345, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHowJ9ZOusYcmT2iP4bzX_O_oGQJXBBPl4E9HDb73DXH5HDVmgZakl2IAEH_rBVdGC0tGbb2p5EnwNwKuBeoksOtP8ar9U8xPMQC2wvrKWyvLOzxPnXkOPsD4Tkw==', start_index=20335)
Annotation(end_index=20426, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9uKiTgEKJfMmEBztbMoh8Yh1BIMPmadbFnK-DHM0lmnP041nMvwdecVtv0LgJqJ0fWY89Qt3K-qxlb3h1_-V_2u26Mo9O21CJnnXCURCVuS5jpinFDP0_4bPEwMG7jOpHqxYPpNG5Ddxm3EOf9zOCGKmQiV8qgg==', start_index=20417)
Annotation(end_index=20500, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcJL9Y3mQ_Y-MORDKYeAy9xaiwuKf4yCTTi4uBss0P4SMfPmnca3FFl8k7sxbu_BnqQ6Dq4uEWoOdtCpAi37hHA9g-fD4wbGgd-DWYbVS9vT0X42ORwg5Li8mri_ua66ECiinqTX0nw4kqX44V6EIHbiowaLdHRKAwehUV3-G1f75sTHtHWKoZqed4TMNnn5tQBoctKCDTiDRi-Eg-gxFoU5MxaOv_8dyoF8u2a3BG', start_index=20490)
Annotation(end_index=20585, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFqltRIg-oMU1xhIoxvU9gPJMA3pp63Vo5WnDjn8-CrSFAPI-RBIFVR7AQlRaOHaSq310fehgaiMqk1Z9Fq4TU4fti1Q_yTll1trD7wYlhuusdpkSDio9tr0SqQuqfrC50Yw1Gl0C_RVb6J9I4R93c6J3OZVSRUjS5q5SA3iw91VgIIyrxITzXR1lshCMoqSl3N2YvFu5s=', start_index=20576)
Annotation(end_index=20662, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEdtwWie29oBz93UTBjhgHfDUPsrBQDHmJf4YyHlIJUkDcYQ6PO03vooQKy4PK0ke00yOZzm0Mb51Iv2-Sc7k2f8iDkKROJm1d9R3CxDbl4S6J_0ZVXIT4a4q8DaR1GvN-BgLl3YT_-VzN9os7W9vBOD4nvBW63MqT-z7adfRUuSIdDkMDNri__HLspicKqII-8vQ==', start_index=20653)
Annotation(end_index=20748, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHHn8krHa90-Z54Zo5rw-lw5gwtbwBtba74sQ5Ch3ldS79Di8nlLU-fE2ju5edcUkErwmU9LUle1Wgimt46VD2f7yyIdvBDYqurkyhTB9kDhRf5VzlVkvmUNw2q144EhNxaONVjQsm0srYxEUrQvs5mtGdQ09Z9lxMFS08M-lM=', start_index=20739)
Annotation(end_index=20820, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7fegUmh3dGVC2ONbOcP-yEzDNBuP4h1Jpq5ZTiPov8c-oagCsZVrD07bdteKPf6nUeIo-qrrezWwvavm9t89zl4NHsjLHNTLzxSuII4NnuW-WG9GG8fFhkqi2rh0YKjZTq7ECFyAdHN1jyGrhfB23dmdKf6eXKzpLJwnsitJdSYcjd3gGPi9wpUqdG1ikUTdk-S4PhYrr', start_index=20810)
Annotation(end_index=20912, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2kdZOKqV2joV88KsOXONwXIdAmPrGAyklZlXTmMXdpD9CGHEo9Vl9IqPK4s0nNk5AY4mVSkV_9rPqBs9ZkVdt4kV7AhJeJgsM1ZnjFNhCwXsSfhSsPF3lkGFyPZLreq78j8ChWuk61_OFQuPmXyttf5TiLhFq', start_index=20902)
Annotation(end_index=21008, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqewVTr719iY_AUc8e4qCfavdWX9Moguvz4sJKnIlAW8VHHJYCYK8mkBaw4u8aUG8RpjS6CzLZJfFVQbuLXd08LHCY384k_U00mWgVDZNLrbzXjSe2ZYv0V7vaay-WMlMS21Cti2CQGxx7hP34RtRfa3BVIlJY6_dg7lcHUwPfWYRJ3AGUT_b5LcGFJJPBuxlloXTmKDRKGWcRs-Jy', start_index=20998)
Annotation(end_index=21077, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEn-ycWnguyhSgDm7EV0kub1xq0du3i0oE7W7bSVRnVVIY9sN1ZOa2HifxYbZnPOVYnP9UABAjKm8UW902HMfGNGeC-fx0mrLVw4g8j6OZf8Vppf1doIEFYx5dGIEmtP2hFALJlHW5quU6Q2gkFJyIYhYEKH7snuA==', start_index=21067)
Annotation(end_index=21161, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkK1d6tFcpvpbgPvBlu0wHCT45Ch0G5EDaoHUatYmqUJalE3vOx0MKwEIM1xOCICRgagREFBHQPGGLIcckwOf3Ro_rZiZlHWA7zFLrKwLfSl_VQsk=', start_index=21151)
Annotation(end_index=21237, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6YKw4NGvoD207P_HJvdYKJFkVJDDQBlINDmkYOsMeDefLQn5MEFsxdWqUzkPTMAoTTZJ7B_WZr5eT7BrhOHwDaNDGYKCkDur4I7ib0WWnxIRoxi_n', start_index=21227)
Annotation(end_index=21321, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH86X40YfwD332Dk083pWKV1zbnM0RIsvYAe3zS76Tu43WU409sJQ2XR3VDgt6-SuEx4wozj-jO2NrNVXpdrhDAlqhvDfLw0-yUARnhPAjVbjnK785eng7ayvRB16fj', start_index=21311)

## Sources
