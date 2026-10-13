# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** c5e1344b | **Time:** 274.55s | **Cost:** $1.19103
--------------------------------------------------------------------------------

# Authentication Intensity Hierarchy in Account Security Protection

**Key Points**
*   **Standardized Frameworks:** The hierarchy of authentication intensity is primarily codified by international standards, most notably **NIST SP 800-63B** (Authenticator Assurance Levels 1-3), **ISO/IEC 29115** (Levels of Assurance 1-4), and the EU’s **eIDAS** regulation (Low, Substantial, High).
*   **Determinant Factors:** Intensity is determined by the number of authentication factors (knowledge, possession, inherence), the cryptographic strength of the credential, and the resistance to specific threats such as phishing, replay attacks, and verifier compromise.
*   **Dynamic Adaptation:** Modern hierarchies are not static; they utilize **Risk-Based Authentication (RBA)** and **Step-Up Authentication**, driven by real-time contextual signals (location, device reputation, behavior) to dynamically adjust the required intensity.
*   **Algorithmic Governance:** Advanced systems employ machine learning models, such as **Random Forest** classifiers and **Edge Large Language Models (LLMs)**, to calculate risk scores and determine the necessary authentication strength in real-time, particularly in IoT and vehicular networks.
*   **Identity Proofing Dependency:** The strength of an authentication event is intrinsically linked to the rigor of the initial identity proofing (Identity Assurance Level), ensuring that the digital credential is bound to a verified real-world entity.

## Introduction

The concept of "authentication intensity" refers to the degree of confidence a system can assert regarding the validity of a user's identity claim during a digital interaction [cite: 1]. It is not a binary state of being "logged in" or "logged out," but rather a sophisticated hierarchy of security postures designed to balance risk, usability, and cost. This hierarchy is determined by a complex interplay of static credential characteristics, dynamic contextual analysis, and rigorous regulatory frameworks.

In the nascent stages of digital security, authentication intensity was largely synonymous with password complexity. However, the proliferation of sophisticated cyber threats, including phishing, man-in-the-middle attacks, and credential stuffing, has necessitated a shift toward multi-dimensional hierarchies. Today, the determination of authentication intensity involves evaluating the "strength" of the authentication mechanism itself (e.g., cryptographic hardware vs. memorized secrets) and the "assurance" of the process (e.g., resistance to impersonation).

This report provides an exhaustive analysis of the determinants of the authentication intensity hierarchy. It examines the global standards that define these levels, the technological factors that differentiate them, and the emerging role of artificial intelligence and blockchain in dynamically governing authentication strength.

## Theoretical Frameworks and Regulatory Standards

The hierarchy of authentication intensity is formally defined by several major international standards bodies. These frameworks provide the taxonomy and requirements that organizations use to classify authentication strength.

### NIST Special Publication 800-63B: Authenticator Assurance Levels (AAL)

The National Institute of Standards and Technology (NIST) provides one of the most widely cited frameworks for digital identity. NIST SP 800-63B defines three **Authenticator Assurance Levels (AALs)**, which represent an ascending hierarchy of authentication strength and confidence [cite: 2, 3].

#### AAL1: Low Confidence
AAL1 represents the baseline of the hierarchy. It provides "some assurance" that the claimant controls an authenticator bound to the subscriber's account [cite: 4, 5].
*   **Determinants:** AAL1 permits single-factor authentication (SFA). The most common determinant is a **memorized secret** (password or PIN), though physical authenticators are also permitted [cite: 6].
*   **Security Posture:** This level offers little to no protection against phishing or eavesdropping. It is suitable only for low-risk applications where unauthorized access would cause limited harm [cite: 2, 3].
*   **Cryptographic Requirements:** While credentials must be transmitted securely (e.g., over TLS), the authenticator itself does not necessarily require cryptographic proof of possession for every transaction [cite: 3].

#### AAL2: Moderate Confidence
AAL2 introduces the requirement for **Multi-Factor Authentication (MFA)**, significantly elevating the intensity of the verification process.
*   **Determinants:** Proof of possession and control of two distinct authentication factors is required. This typically combines "something you know" (password) with "something you have" (OTP device, software token) or "something you are" (biometric) [cite: 5, 7].
*   **Cryptographic Requirements:** Approved cryptographic techniques are required at AAL2. For example, if a biometric is used, it must be strongly bound to a physical authenticator [cite: 6].
*   **Reauthentication:** AAL2 mandates stricter session management, requiring reauthentication at least once every 12 hours during extended sessions, or after 30 minutes of inactivity [cite: 7, 8].

#### AAL3: High Confidence
AAL3 represents the pinnacle of the NIST hierarchy, providing "very high confidence" in the user's identity.
*   **Determinants:** This level requires a **hardware-based authenticator** and a mechanism that provides **verifier impersonation resistance** (phishing resistance) [cite: 7, 9].
*   **Cryptographic Requirements:** Authenticators must be FIPS 140 Level 2 (or higher) validated hardware cryptographic modules. The authentication protocol must prove possession of a key through a cryptographic protocol, ensuring that the secret key never leaves the device [cite: 4, 7].
*   **Use Case:** AAL3 is reserved for accessing high-value, sensitive data or performing critical actions where the risk of compromise is unacceptable [cite: 10].

### ISO/IEC 29115: Entity Authentication Assurance Framework

The International Organization for Standardization (ISO) defines a four-level hierarchy known as **Levels of Assurance (LoA)** in standard ISO/IEC 29115 [cite: 11, 12].

*   **LoA 1 (Low):** Minimal confidence. Suitable for low-risk applications where the risk of false claims is acceptable.
*   **LoA 2 (Medium):** Moderate confidence. Requires more robust methods than LoA 1, often involving passwords or simple tokens.
*   **LoA 3 (High):** Strong confidence. Requires MFA and is designed to prevent substantial risks.
*   **LoA 4 (Very High):** The highest level of trust. Requires robust cryptographic techniques, hardware tokens, and often in-person identity proofing. It is used for critical systems like national defense or high-value banking [cite: 11, 12].

### eIDAS Regulation (EU)

In the European Union, the **eIDAS** regulation (Electronic Identification, Authentication and Trust Services) defines three assurance levels: **Low**, **Substantial**, and **High** [cite: 13, 14].

*   **Low:** Self-registration is permitted without identity verification. Authentication may be single-factor [cite: 14, 15].
*   **Substantial:** Requires verified identity information and at least two authentication factors (e.g., password + SMS OTP). This aligns roughly with ISO LoA 3 [cite: 13, 16].
*   **High:** Requires face-to-face enrollment (or equivalent remote reliability) and the use of a smart card or hardware token (e.g., National ID card). This aligns with ISO LoA 4 [cite: 13, 15].

### Comparative Mapping of Hierarchies

Research indicates a functional mapping between these standards, although differences in identity proofing requirements exist.
*   **NIST AAL1** $\approx$ **eIDAS Low** $\approx$ **ISO LoA 2** (Single Factor).
*   **NIST AAL2** $\approx$ **eIDAS Substantial** $\approx$ **ISO LoA 3** (Standard MFA).
*   **NIST AAL3** $\approx$ **eIDAS High** $\approx$ **ISO LoA 4** (Hardware-backed, Phishing-Resistant MFA) [cite: 13, 17].

## The Determinants of Authentication Intensity

The hierarchy is not arbitrary; it is determined by specific attributes of the authentication factors and the protocols used to transmit them.

### 1. The Factor Categories
The fundamental building blocks of authentication intensity are the "factors." The strength of an authentication event is determined by the number and independence of these factors [cite: 18, 19].

*   **Knowledge Factor (Something You Know):** Passwords, PINs, and security questions. These are generally considered the weakest determinants due to their susceptibility to social engineering, reuse, and brute-force attacks [cite: 18, 20].
*   **Possession Factor (Something You Have):** Physical objects like smart cards, hardware tokens (YubiKey), or mobile phones (for OTPs). Hardware-based possession factors significantly increase intensity by requiring physical theft for compromise [cite: 21, 22].
*   **Inherence Factor (Something You Are):** Biometrics (fingerprint, face, iris). These provide high convenience and strong binding to the user. However, their intensity depends on the "distinctiveness" of the trait and the robustness of the sensor (e.g., liveness detection) [cite: 23, 24].
*   **Contextual Factors:** Emerging hierarchies include "Somewhere You Are" (Location) and "Something You Do" (Behavioral biometrics like keystroke dynamics) as supplementary determinants that can elevate assurance levels without user friction [cite: 22].

### 2. Cryptographic Strength and Protocol Security
The intensity is heavily determined by *how* the factor is verified.
*   **Phishing Resistance:** A critical determinant for high-intensity levels (NIST AAL3). Protocols like FIDO2/WebAuthn use public-key cryptography where the private key never leaves the user's device. This prevents attackers from harvesting credentials via fake login sites, a vulnerability present in AAL1 and some AAL2 methods (like SMS OTP) [cite: 2, 25].
*   **Verifier Compromise Resistance:** High-intensity levels require that if the authentication server is breached, the attacker cannot impersonate the user. This is achieved through asymmetric cryptography (used in AAL3) rather than shared secrets (passwords) [cite: 7].
*   **Channel Security:** The use of "Out-of-Band" (OOB) authentication (e.g., push notification to a separate device) increases intensity by requiring an attacker to compromise two distinct communication channels [cite: 26].

### 3. Identity Proofing Dependency (IAL vs. AAL)
Authentication intensity cannot be decoupled from **Identity Assurance Level (IAL)**. The IAL determines how rigorously the user's real-world identity was verified during enrollment (e.g., checking a passport vs. email verification).
*   **Binding Requirement:** High authentication intensity (AAL3) is often required to bind to a high-assurance identity (IAL2/3). For example, it is illogical to protect a self-asserted email account (IAL1) with a hardware crypto-token (AAL3), though technically possible. Conversely, a high-value identity (IAL3) *must* be protected by high-intensity authentication to prevent account takeover [cite: 7, 27].
*   **Enrollment Rigor:** The eIDAS "High" level explicitly mandates face-to-face registration, linking the authentication intensity directly to the enrollment process [cite: 14].

## Dynamic and Adaptive Authentication Mechanisms

Modern security architectures have moved beyond static hierarchies to **Risk-Based Authentication (RBA)** and **Step-Up Authentication**. In these models, the required authentication intensity is determined dynamically at the moment of access.

### Risk-Based Authentication (RBA)
RBA evaluates the context of a login attempt to calculate a risk score. The authentication intensity is adjusted in real-time based on this score [cite: 28, 29].
*   **Contextual Signals:**
    *   **Device Reputation:** Is this a known, trusted device? (Low Risk) or a new, unknown device? (High Risk) [cite: 30, 31].
    *   **Geolocation:** Is the user in their usual city? Or is there an "impossible travel" anomaly (e.g., logging in from London and Tokyo within an hour)? [cite: 31, 32].
    *   **Network Environment:** Is the request coming from a corporate VPN (Low Risk) or a Tor exit node (High Risk)? [cite: 28].
*   **Intensity Adjustment:**
    *   **Low Risk:** The system may allow access with just a password (AAL1) or even "passwordless" entry if the device is trusted.
    *   **High Risk:** The system triggers a "step-up" challenge, requiring an additional factor (e.g., biometric or hardware token) to proceed [cite: 30, 33].

### Step-Up Authentication
Step-up authentication is a specific implementation of RBA where the intensity hierarchy is traversed within a single session.
*   **Resource Sensitivity:** A user may log in with a password (AAL1) to view a dashboard. However, if they attempt to transfer funds or change their email address (High-Value Actions), the system demands a second factor (AAL2/3) [cite: 33, 34].
*   **Friction Reduction:** This approach minimizes user friction by reserving high-intensity authentication only for critical moments, rather than enforcing it at the front door for every session [cite: 35].

## Advanced Algorithmic Determinants

The determination of "risk" and the subsequent requirement for authentication intensity are increasingly governed by sophisticated algorithms and artificial intelligence.

### Machine Learning in Risk Scoring
Machine learning models are used to classify authentication attempts as "normal," "suspicious," or "malicious" with high precision.
*   **Random Forest Classifiers:** Research has demonstrated that Random Forest algorithms are highly effective in risk scoring for authentication. They can process numerical metadata (time, frequency, location) to classify transactions or login attempts.
    *   *Performance:* Studies show Random Forest models achieving over 99% accuracy in distinguishing weak vs. strong passwords and legitimate vs. malicious login attempts [cite: 36, 37].
    *   *Application:* In vehicular networks (V2X), Random Forest classifiers process metadata to dynamically adjust the cryptographic authentication intensity, ensuring low latency for critical safety messages while maintaining security [cite: 38].
*   **Edge Large Language Models (LLMs):** Emerging architectures integrate Edge LLMs to perform semantic analysis of transaction contexts.
    *   *Contextual Understanding:* While Random Forest handles numerical data, Edge LLMs analyze the *semantics* of the interaction (e.g., the intent behind a command). This allows for a more nuanced determination of whether a transaction is "sensitive" or "critical," triggering the appropriate authentication intensity [cite: 38, 39].
    *   *Privacy:* Deploying these models at the edge (on-device) preserves privacy by keeping sensitive data local [cite: 40].

### Blockchain for Decentralized Integrity
In decentralized environments (like IoT or V2X), the authentication intensity hierarchy is reinforced by blockchain technology.
*   **Trust Scores:** Blockchain can store immutable trust scores for devices. An authentication request is evaluated against this decentralized ledger. If a device's trust score drops (due to anomalous behavior), the network demands a higher intensity of authentication (e.g., a more complex cryptographic puzzle) [cite: 39, 41].
*   **Decentralized PKI:** Blockchain eliminates the single point of failure in traditional Public Key Infrastructure (PKI), allowing for a distributed determination of credential validity [cite: 20].

## Biometric Intensity and Evaluation

Biometrics represent a unique category where intensity is determined by the statistical accuracy of the technology.

### Biometric Modality Hierarchy
Not all biometrics provide equal intensity.
*   **High Intensity:** Iris and Retina scans are considered to have the highest distinctiveness and accuracy, making them suitable for high-security environments (AAL3 equivalent when combined with hardware) [cite: 24].
*   **Medium Intensity:** Fingerprint and 3D Face recognition.
*   **Low Intensity:** 2D Face recognition (susceptible to photo spoofing) or Voice recognition (susceptible to replay).

### Performance Metrics
The intensity of a biometric system is mathematically determined by:
*   **False Acceptance Rate (FAR):** The probability that the system incorrectly authorizes a non-authorized person. High-intensity systems must have a near-zero FAR [cite: 6].
*   **False Rejection Rate (FRR):** The probability that the system rejects a valid user.
*   **Threshold Tuning:** Administrators can adjust the "matching threshold" (T). Setting a lower T increases convenience (lower FRR) but decreases authentication intensity (higher FAR). Setting a higher T increases intensity but may frustrate users. This tuning is a direct determinant of the effective security level [cite: 42].

## Conclusion

The authentication intensity hierarchy is determined by a convergence of **regulatory standards**, **cryptographic capabilities**, **contextual risk assessment**, and **algorithmic intelligence**.

1.  **Static Foundation:** The baseline is set by the *type* of credential used, categorized by frameworks like NIST SP 800-63B (AAL1/2/3) and ISO 29115. Hardware-backed, phishing-resistant credentials (AAL3) sit at the top of this static hierarchy.
2.  **Dynamic Adjustment:** The effective intensity is modulated in real-time by Risk-Based Authentication engines. These engines use factors like device reputation, geolocation, and behavioral anomalies to "step up" requirements when risk is elevated.
3.  **Algorithmic Governance:** The decision to escalate intensity is increasingly driven by ML models (Random Forest) and Edge LLMs, which process vast amounts of contextual data to make millisecond-level security decisions.
4.  **Identity Binding:** Ultimately, the intensity of authentication is limited by the assurance level of the underlying identity proofing (IAL). A strong lock is useless on a door with a weak hinge; similarly, strong authentication requires verified identity enrollment.

As digital ecosystems evolve, the hierarchy is moving away from rigid, static levels toward fluid, continuous authentication models where intensity is a variable function of risk, trust, and context.

**Sources:**
1. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHKSIC6K2PAwCHB4gYnXrcLIx0H1_-KFIMKm4rQC1e-aycR9k5GsfhA214HwkNYNIRppwIuh8thAPrhcrARDCnCwSN8KHwoL7R-_-syhPh1XKpapnr-kHCZxwVwOLaNXCY97dexXPSohZojWL7VG21xw79lMKgIB2KDqGN_y0ljgU7mFIcypLn_0y71udrEN3dGIx3uiA1cok=)
2. [beyondidentity.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuXJ8TKnIgXQ7HJOXQN8x4MhBqUHKd2bevVprYXC_fjCBwYp-f9CHv6GPXoVgnzRU0B3bHQ1sFZr0IsjGEn9evlBZMefpR2P7KrwARBv7F4Tg85DZh92OqRCvL2QsUQIYD4MRa7PF40PhY7dPtG73pG21ishl5HMLlTsvwoQmdRg==)
3. [manageengine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDxwH5O3ZNRfsVtDQAXtx8RHqAIu7t4zrwxbbHgSefJxPYo1vzgYi-pEzBDq7ixPcU24SN9G3ctu3FpoP8G4Zd-rGbLG6ic6GHz3mMONXVahtwRR0HWATLV7_XK9wnj7PHrcrqGI_KyBEES5Jse7b2jtWhGvcudOAaJTt-VPuG4RJXkfhxH0G9KXlfII98h6Nh5IimjseeG3hzIyQr8a3MuXQLCem6DM-5UPc4XjE=)
4. [intercede.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOdaRnjt4Bwt8uibbx_0scbbtpKaIn9TEXOsFDlVExYZmjiGI0uN43bYD1asYxK7fRQ9aaeZRL1hK6DceVk_nH8WsTEX6DDjpRuGrpHvavZ8QtkVUU2ab7AXe2PRA4ozoqzJ4-ZdsEWu8x5QeqlNkuelnK6tCH4dNRO4K21v8Hq7T5kCFmnAO0BeqL3gewZyrlY-hFcvMmXfXhU4DGqDBE_JVpu19ZEjnI)
5. [nist.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3TMa6yQaYoRNltSgX0g78BmJTwW6_IlI29zZfKoI0xZaROB_nYfnxQlFuJvhaXEz9QIeoNUWJyEy_0E-F48T5gdikBepLmPeNccBrmd_5qeTMfB3CiGCTiqdyBIGPzTmKYzly4w==)
6. [nist.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvcBjNh7dQhxoyWkv-v2n304nphWkB4wZuPTPhBEsUkjiQGVddILo0IDQZPdH6fe5F9tUKUxmmjls3CZP3o9D2G_zlHFNMGtYrl1YidHJal0DDYi2uEfkcbbzZpQGMgoMPm9QAtUmx5NGb1N6BSuIpINJ5Yf_lHA==)
7. [nist.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSYp0wTqMDe4knkGTb_lFSb91Msde2G8fE-hn8rWy14MV44FR0bWOdotEgvvUXCVO_lon4Zs07WhCHqZXDzTBTEcp-RRl-glCvf4iLS9hAj6mJXYjjts903UPAt9rZ3UUOZaXF)
8. [sailpoint.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAYT4ki1WGb6eS6YqcPRGfQOEIEqQE5hvyB4tvRMEiX6xJE0DPfbfMTv2stf2PhJwqjtAqfzQQNTDA_hJo-Q89ZRnvhsF6ZbxC6CFdgr_enS_IwQrJIXHa8UDJjJlVmNQv1h99dxj26ZwDwn4h)
9. [legmt.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEEW7_Ir11uJtPFA5rfPub0Kg_1ytUhdlW5fKLBNJxc3kO5fWFeudEimgibljBHA-2M3I5ETbaFg2_Ptp04UMLY8JliAVRs7Ak2zg92BzgU36WHNuwumXVDNx11JrzM_CVwD1KGTMXiIGPKc7ntxK84-scy8rJ08NC8LtCJqdFJ-sWLCdlvmbL8qFbgouZX_za8GDgkw8bXfgv7N8fY3kBsqOhdP4aXsWVAAAxnYOr3aAWOOup25ZrwqfBxy39PhHLuKkjDHvHotH3PiY=)
10. [octatco.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHW4WiAnt105y3DhaZ3Fnlr_fKTYySbCMpF-c1mfytPM_B7im5VXayIstU7yKDlsw_ayNqZo97xN0TNVdDfIMV4UkePxe1M6NZ5N7mGPcimWddA)
11. [cfecert.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5CpoCKhX2UQ6mVZL5QJR1Y2E0wJ-UP0y2waXWHZyBaYaUh4LDcGMNIdp1Teo21U3loZGt4kMVVmtRgh1Xgfmt4s13gVA2P2Tk_3JLMEMg0cNJcQ8HD7CI93TTaL-QPaJVUwkqrbsZevFj25_fK7AcfCrrYtQ=)
12. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4WXSJpUxP9NABf1A72CKQOWQFsUO17RDF5InWjoO2HQo1Avan7bnTu2aGnDov1913xbl839sXA1Iz7dnRgxcb73L8W6Pn3wQM8RBaLxisz5cmu-DXOqT5VaLfeNLz4iNZemTHLWBV3S6zgXO-4e9vNYFFE-jG5DNVw0ObkEZL2CV3Efu34JezBI78EdbKnBwOgEbDhy9HH3gYr6tk-c3VAw==)
13. [methics.fi](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF89Egp866hFze3N8V7jnLV-rCe3QJqhORs-B3QTQ1OYiABK6PUP1M80GivUUcqoqsc4qwp1KM48kdlSWlZ63n5flPj3V03w8F3VzSMmLYXbE0PZ_v8gcjeYQ4hilZCgTZK25t9PnU1X4YwJatg79AZUQcImg==)
14. [europa.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyEcQci0OiyRAMd1S0XVcDGGeGZSWdJCjp2rIJ7cqlqXLWi5AHXu4iF3aDtP9SX6srSzgHOjOzisfS8g05faivs7Fn4YFxHtNsQniin8PFQkGV2GUGmJPDlMiNREmg4G260FqV77MviroSERNj6R0S3V_aojr4SlUPtI_NL5m8m6SOQmqfcRk_I8GhBq4kCFJyz4g6xkvvLJ0fvKGzBJV0qA==)
15. [hightrust.id](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXJ2ZhWPAcUZ2Gh-u0Zk8YjnRV-I_KUM0P4clikOPxBhf2QplDPwQMMGPP3pV4AEnZdAKtVOIOWlU0PFbehaKzLN3W1MhsI2A_mh0L4z7fW0UwTLRyaeT1XrQbl_Eoj08wBsaJyzC5rcjOXUl7uoPi1UX-madDFvZVnXQWArn3uu2Pdw==)
16. [idura.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9p5ZCD-tAeWzIlVDW_nvIUe8-xctapiajpoMgZ7nqvvM02zmSVQElyN_jygMiB_JjHbnwRhTOYJebux5Gpu9qqTKBFTlIW1_ZhUTMv-uT8kjzMJBfXDXkQ-StTH4lvWIT1rZLRw==)
17. [methics.fi](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQEpVQXGEDbcvhftfyVG4sFzHH0bDm3T2NE0HHyG7YD3tztL0CFxZS-mSQ72uDNXa_CdMcplgv00sV88-mBOqpE-U8Tprc3XyhdZojF1SZv2QCcW-T12yVQd0olPsdAXherG5yQ-9udD5ue-t7YPVj4DkMjrggEy0ysxE=)
18. [rublon.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEykLU7IXaYAd3aHcAd-Eoi3_kQ3zqcTgb7VYsGpNWdURDpsMqQ0bmrkDrpYDzRoS96MVu8o6d7x9kuD4w68aqgLMxNlnhILdVxi6UMp2WwWERVioRX-QokI4Lkfh67HPR2dAjyR9RsKSADTpbgXNSXll_4aTSD3Wc=)
19. [redkeysolutions.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1HfTpnl84T7RpdDYP9FLXdwxmw5UsAja7dtIFXSO41d6fdRpKEFKdT_92pm4-DTDumxnPTfhDsmp0cvZk-vPxwP5oSLo5zBiicq8jM_MeY-sh6JcvXalVm2W2PUig33vkblUGwVkLudUORx4vNT8VzON-nCtr3dZxNhu_M-qcF6ZDgO4QgLgpJs4iArUWMS-2iDFvyOBi-nRqwPT9P9tO5IM=)
20. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2ynTPu5Lw9iFQ0EwrGisQL5IrCZfob5_kXCab5rZnIlKItgXLGOggS5cUaJItPuhnuAMWPj8pJM8fjY65cR-VtH3vDVJzdgl0HrHMNQrfSfTNahoG8N8qMLLlzQ==)
21. [jalaxy.com.tw](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoOwf5iU9aQY1z_v5sbQQMYpfmdG3ZxQ6CRcUB8aWg_tVvdlqN-EwrGhVaDlh-Vb7pZshiMvzVSwJ8KHpQLx8vuzTtaHiDts05QfAHUXKzwcPNNNYe-ZewFFmz2llcJetWalxlmlcKQG2cQlvyJmwF58ATrPhfk1eqV0CRuaJJre7o)
22. [aratek.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYLgnhcfSVCHwIpAiVgSrqfnBuixTPAf6Oqyel9WlnyUawB1l4YuwE5wToheQ_3DocNmHy_tuXipIDOJupYkK8wg2eUuMYBC8QIxaZePT61BAKOHw2fCF4gz0snQ9ON-V_8UEdp5Alt_DApqWcPZPFAv1pl0eAytAx4myqc7ec8cHKbLyG0aUl_hV0oRuK)
23. [nist.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4ktbR89FuUXkz-Ou8xjNp1zWColWCajtiIVsbVyZ6yxJ4HTphRx3S-tLfbS5CNOyUl9DzgHnXjPcjQ5XjsxViFU9pNNkssLByExA0U-QSR9elxBS2lUE5D-MQwaE5WKoBvqj0f3NrlRLgOdrikMwxsXAyxULtkx_c41PCKWKMnTqMK1sLyX0Uy08=)
24. [oaji.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0QFQicSUdOnhf9lTc-qZJ7zV7lRLMfrzB91-VFHldBogrq1lCbuA3iwU56jY4S7GXil2Q2zPM0RPq27L2TaeIO5yAY_xZbdxCVS3eix1Od9eZ-1SIKpefYL9XtO_GS1b9hEldJU3qk2B8)
25. [redmondmag.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGeRcpFGUbGx--HB3EBtPs57rb_eb0uvCnuEaeewsfJQzONE1KNt8X3DOxlhfthBIxftPmFKOnYFeuFYp5sKutqiojIn6hd-KoEjjBHQhUEWl0EI2SttnRA39VNYB1fkiQ2HHrI2uaCeFqB38f8GL2nQmACOJ5jMYsVsO_BGHLDVVb2h3BtBFHFnqP2O781)
26. [pkhenterprises.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzHnGD-RaL2e96gFplKShNmjK5bwqi2-TAURdrxwRU-HdmQH8wH6YEGX5eU4KtWqvtVltFVfUkNq5L6OeSdDefXlna9cd9qcJMy5DDOojiRn3_VRVhpyegEsvd70yU0PrlWfZXVDI1h2DqYgOWDMOQt-FQ1H5uSdgqe5Na4joCjLGsGEY1Nie-M_gd9qDLHjD3lV8=)
27. [worldbank.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFFvasDdS4S1_Tj3CxPAYzWMKJf-IBz37MAkot1vTSZ0jTM59CYE3xBqOZs6sO9kH6kSdCpsu3sJswmIlWrB2c6RhB7VHJJOyJGa3Cfffe2us7DQGqSFLyBgX0bZhxvtJH_-Y0yE7Pup9HNoA=)
28. [motoki.co.jp](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPePYQhNs--IkgdiIx0-_j-vn9qv_GB1bi30XQbxjBMy4Rl8d_66la4gqJxGowMPUXAmZ0_CaiAe1iXZ9CnRuZ587Gbr9FycKZL307AQt9-QhQ3vAJ1cg=)
29. [forbes.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoFYR4I7VKC6YyEBH7YfY3-ZgiRvSK_nlyCokWAaNkGCnu5wzq4lrH0a2h27mn3o7K2AGr20td63_dWFrS_M3HlkjCNNBPXeECj2S_PFsC5W7WerTZao1SEfOC5Njy5VHIyzX0ys0BNUQka91s75fensyBw5ZLz--hcxqOdKGNbnbLjJTeH9jrudmOHqi8rQu45XdFt5KgAqF3l0U2MbL2AX16IzqsL31whO-Yo8Y6qzJ_tpqBDIPiWwfnti47Yguqn1vdWOjLlcOW_Mj8bZrKVjQy9c3orA==)
30. [entrust.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyyY5NTsuIKJDcoqmx0WniMUcERopFJDxCD8OOZZ57m49FHfK6PBkpJZjflZC8Sxd8uC5A5mgrtfpmJnaYRiPGh6Ol9JvE1Gal4UNIJXDxJZqTV1lVTF36gJCThqkORUw0ZVn4z5ly8Yvy-HQnLtHcSPPt2w==)
31. [onelogin.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdQ190pVooHSMxxn07r9cY3i9Yr5d_V4B-8E2uT8o0ePGtR2wwi6oJnaoIL78FtVN4tfxSkwFB4BBiYXTui23R0BnYYErg75k1AsGuL_rSAsA2lYzJsryMuCG2Dr0FoV0aWXXJnxGOt_rMWA==)
32. [okta.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGT4dE2f7ZeuxWtHD3RrK8i3Fu7ei5L_zp_oixGtfVM4wtSkKqpD2KKvpLoSjmsXsBes_vrN36fgtTJcGQdZIAX4sDpNpzDfD8UybvJPllSTf4gnoDZGXcDf7-QqE-Yy08RBM04KKYEnfZzjEW1bw-L_an4pTKd9RBW63TMuRcxli1Z4jlMvQ==)
33. [frontegg.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGALFbQLaGf2O5QIQkWsddgWHQ6hdpReiVTsBvbzLbh4MinbNgVjSeoMAGPFSb5KfH-OSfE6lIpkrXRnZR-GoMbPUOy9V3efYiijg_Jmzg7WVWgjbyNgJTGBEQ5h7025tExcplHxI=)
34. [descope.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH93TYdfzPhYe_1y69D29Ty2xr8RDp1M_uZ1GonprfINiV_XrqmXgDr1fGd01tM9igqXABjwSjzf66DQsxCguRegalHG85sEHclQRigy1fWVUchLMDTDIrWlLl_gM8IeBUH2_HNlIx8N9rQLr6R2mY=)
35. [auth0.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_fSFPTaIk55y3RQo9QN55W2iTaQNAYWAqJL7CUF8DaFXReJL26yGu1vR7Wpw6qFskRLk1MdRAdONgSqFjNga-g-vXWeSyexTEdUVz94DdrX4un-j_1EKjZRzZdsAWoC5qkcrBHOVX3xbKSXEcqZKvNoaxx7lJT2bB4II=)
36. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6qsSCkcBLzyO4fNCcQm8WjiWf38FAHqQGjjJpww_HzHZ13UrkOmzgy53TMCZq2_9NNz7JWct3aDT1W0QClqhrOCuTJwFwPnw7RjL0HUazG4gzFmzGKQ==)
37. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGf51rOoINAmSTuWFKeL6r43yVEzJoZIFA0rkAmZZI4dRNuNe5mJayeb-JJuG-DOmruxed7CTuwOWDj5RqN25syJzre1yLjcINsfoIbGR-ZFpN3WkHCibYVeiTu1sq1FLq1fDuLdrjcUD620vIP0TiYkjjPXQ==)
38. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjPSc71iQjTK4k5jjB1MG2Cd4ZJMpTx7u26Q9d76DcZuqSoQ4OoeoyM5fcw5ug_WeVe7hayhjgIFdMNA229IdiUyLZMlL_FE8uCAkb57WrT7ww9a_CKtYwGdQe3Ept3avI0WnE)
39. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrp32xjbJIyr6y4x33Eb00nC8TuLt__ylvkP8D_gmV4dqZFxDp6-1qWOOpaPLdvQ0VnGTFMm045rg4uTsYv8vLQ6h4GxYick4BWSUDIh2fje3kTTF5h2x5yzLZqCugW_tdkzOOLNqLVVVylJIqqSeeKrfr)
40. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrX8oo6qOrHkxHaX3UqTnGDpApxyMrDnBoJS-B75Q1StPqn1w74tgDzGGzuy-T9tXBsW999K90pO5pL-3AH8Rsz9-9JxyQunihzzg7--006NJaMbQ6Cs6Yc2_ri3v6bzojtggM-fGBmCETb0m_LdOtem1-fQ==)
41. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPOPENEPc3Luf65mB8uLfgQXYjrq3MJLShdwZq99cy8DXLwG9ZTW6r_zoucNF5osR5xD41g05nUHn4_w1VTC91vn9WyR6RGBZHIkxccS6iHmkrEly_-zbljMLOwtIXY5Ssu-qJETLY7SRkCa8IABXUgOpLaI-v28J7MYH1FoTuBpr8mWUfn3NkPJlozBz1syqsKjp_kIk_KrfEjM8xxDNuzA22Gv-rY-Lo2Y_pP_sWcgp2wu_6IyyfxzfXVTGFTN93MHYIUHU0vcJ7NxGnk6AGndORpvaqmq90_bawYw==)
42. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEbWb0iYlCskqwiVf0LPfV8hvbVjJGPgVLbaFUbEx8Z54lDhL4ralpNDhtoLq62jl9m4TVAFgga2csCrIWZ57ODe6SK83ISJ4wsw-nSuAMBpHoSfgv2I_4WE-SO8CCxg==)


## Annotations
Annotation(end_index=1684, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFHKSIC6K2PAwCHB4gYnXrcLIx0H1_-KFIMKm4rQC1e-aycR9k5GsfhA214HwkNYNIRppwIuh8thAPrhcrARDCnCwSN8KHwoL7R-_-syhPh1XKpapnr-kHCZxwVwOLaNXCY97dexXPSohZojWL7VG21xw79lMKgIB2KDqGN_y0ljgU7mFIcypLn_0y71udrEN3dGIx3uiA1cok=', start_index=1675)
Annotation(end_index=3556, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDxwH5O3ZNRfsVtDQAXtx8RHqAIu7t4zrwxbbHgSefJxPYo1vzgYi-pEzBDq7ixPcU24SN9G3ctu3FpoP8G4Zd-rGbLG6ic6GHz3mMONXVahtwRR0HWATLV7_XK9wnj7PHrcrqGI_KyBEES5Jse7b2jtWhGvcudOAaJTt-VPuG4RJXkfhxH0G9KXlfII98h6Nh5IimjseeG3hzIyQr8a3MuXQLCem6DM-5UPc4XjE=', start_index=3544)
Annotation(end_index=3556, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuXJ8TKnIgXQ7HJOXQN8x4MhBqUHKd2bevVprYXC_fjCBwYp-f9CHv6GPXoVgnzRU0B3bHQ1sFZr0IsjGEn9evlBZMefpR2P7KrwARBv7F4Tg85DZh92OqRCvL2QsUQIYD4MRa7PF40PhY7dPtG73pG21ishl5HMLlTsvwoQmdRg==', start_index=3544)
Annotation(end_index=3751, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3TMa6yQaYoRNltSgX0g78BmJTwW6_IlI29zZfKoI0xZaROB_nYfnxQlFuJvhaXEz9QIeoNUWJyEy_0E-F48T5gdikBepLmPeNccBrmd_5qeTMfB3CiGCTiqdyBIGPzTmKYzly4w==', start_index=3739)
Annotation(end_index=3751, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOdaRnjt4Bwt8uibbx_0scbbtpKaIn9TEXOsFDlVExYZmjiGI0uN43bYD1asYxK7fRQ9aaeZRL1hK6DceVk_nH8WsTEX6DDjpRuGrpHvavZ8QtkVUU2ab7AXe2PRA4ozoqzJ4-ZdsEWu8x5QeqlNkuelnK6tCH4dNRO4K21v8Hq7T5kCFmnAO0BeqL3gewZyrlY-hFcvMmXfXhU4DGqDBE_JVpu19ZEjnI', start_index=3739)
Annotation(end_index=3956, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvcBjNh7dQhxoyWkv-v2n304nphWkB4wZuPTPhBEsUkjiQGVddILo0IDQZPdH6fe5F9tUKUxmmjls3CZP3o9D2G_zlHFNMGtYrl1YidHJal0DDYi2uEfkcbbzZpQGMgoMPm9QAtUmx5NGb1N6BSuIpINJ5Yf_lHA==', start_index=3947)
Annotation(end_index=4170, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDxwH5O3ZNRfsVtDQAXtx8RHqAIu7t4zrwxbbHgSefJxPYo1vzgYi-pEzBDq7ixPcU24SN9G3ctu3FpoP8G4Zd-rGbLG6ic6GHz3mMONXVahtwRR0HWATLV7_XK9wnj7PHrcrqGI_KyBEES5Jse7b2jtWhGvcudOAaJTt-VPuG4RJXkfhxH0G9KXlfII98h6Nh5IimjseeG3hzIyQr8a3MuXQLCem6DM-5UPc4XjE=', start_index=4158)
Annotation(end_index=4170, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuXJ8TKnIgXQ7HJOXQN8x4MhBqUHKd2bevVprYXC_fjCBwYp-f9CHv6GPXoVgnzRU0B3bHQ1sFZr0IsjGEn9evlBZMefpR2P7KrwARBv7F4Tg85DZh92OqRCvL2QsUQIYD4MRa7PF40PhY7dPtG73pG21ishl5HMLlTsvwoQmdRg==', start_index=4158)
Annotation(end_index=4392, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEDxwH5O3ZNRfsVtDQAXtx8RHqAIu7t4zrwxbbHgSefJxPYo1vzgYi-pEzBDq7ixPcU24SN9G3ctu3FpoP8G4Zd-rGbLG6ic6GHz3mMONXVahtwRR0HWATLV7_XK9wnj7PHrcrqGI_KyBEES5Jse7b2jtWhGvcudOAaJTt-VPuG4RJXkfhxH0G9KXlfII98h6Nh5IimjseeG3hzIyQr8a3MuXQLCem6DM-5UPc4XjE=', start_index=4383)
Annotation(end_index=4832, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3TMa6yQaYoRNltSgX0g78BmJTwW6_IlI29zZfKoI0xZaROB_nYfnxQlFuJvhaXEz9QIeoNUWJyEy_0E-F48T5gdikBepLmPeNccBrmd_5qeTMfB3CiGCTiqdyBIGPzTmKYzly4w==', start_index=4820)
Annotation(end_index=4832, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSYp0wTqMDe4knkGTb_lFSb91Msde2G8fE-hn8rWy14MV44FR0bWOdotEgvvUXCVO_lon4Zs07WhCHqZXDzTBTEcp-RRl-glCvf4iLS9hAj6mJXYjjts903UPAt9rZ3UUOZaXF', start_index=4820)
Annotation(end_index=5026, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvcBjNh7dQhxoyWkv-v2n304nphWkB4wZuPTPhBEsUkjiQGVddILo0IDQZPdH6fe5F9tUKUxmmjls3CZP3o9D2G_zlHFNMGtYrl1YidHJal0DDYi2uEfkcbbzZpQGMgoMPm9QAtUmx5NGb1N6BSuIpINJ5Yf_lHA==', start_index=5017)
Annotation(end_index=5225, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAYT4ki1WGb6eS6YqcPRGfQOEIEqQE5hvyB4tvRMEiX6xJE0DPfbfMTv2stf2PhJwqjtAqfzQQNTDA_hJo-Q89ZRnvhsF6ZbxC6CFdgr_enS_IwQrJIXHa8UDJjJlVmNQv1h99dxj26ZwDwn4h', start_index=5213)
Annotation(end_index=5225, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSYp0wTqMDe4knkGTb_lFSb91Msde2G8fE-hn8rWy14MV44FR0bWOdotEgvvUXCVO_lon4Zs07WhCHqZXDzTBTEcp-RRl-glCvf4iLS9hAj6mJXYjjts903UPAt9rZ3UUOZaXF', start_index=5213)
Annotation(end_index=5543, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEEW7_Ir11uJtPFA5rfPub0Kg_1ytUhdlW5fKLBNJxc3kO5fWFeudEimgibljBHA-2M3I5ETbaFg2_Ptp04UMLY8JliAVRs7Ak2zg92BzgU36WHNuwumXVDNx11JrzM_CVwD1KGTMXiIGPKc7ntxK84-scy8rJ08NC8LtCJqdFJ-sWLCdlvmbL8qFbgouZX_za8GDgkw8bXfgv7N8fY3kBsqOhdP4aXsWVAAAxnYOr3aAWOOup25ZrwqfBxy39PhHLuKkjDHvHotH3PiY=', start_index=5531)
Annotation(end_index=5543, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSYp0wTqMDe4knkGTb_lFSb91Msde2G8fE-hn8rWy14MV44FR0bWOdotEgvvUXCVO_lon4Zs07WhCHqZXDzTBTEcp-RRl-glCvf4iLS9hAj6mJXYjjts903UPAt9rZ3UUOZaXF', start_index=5531)
Annotation(end_index=5833, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOdaRnjt4Bwt8uibbx_0scbbtpKaIn9TEXOsFDlVExYZmjiGI0uN43bYD1asYxK7fRQ9aaeZRL1hK6DceVk_nH8WsTEX6DDjpRuGrpHvavZ8QtkVUU2ab7AXe2PRA4ozoqzJ4-ZdsEWu8x5QeqlNkuelnK6tCH4dNRO4K21v8Hq7T5kCFmnAO0BeqL3gewZyrlY-hFcvMmXfXhU4DGqDBE_JVpu19ZEjnI', start_index=5821)
Annotation(end_index=5833, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSYp0wTqMDe4knkGTb_lFSb91Msde2G8fE-hn8rWy14MV44FR0bWOdotEgvvUXCVO_lon4Zs07WhCHqZXDzTBTEcp-RRl-glCvf4iLS9hAj6mJXYjjts903UPAt9rZ3UUOZaXF', start_index=5821)
Annotation(end_index=5997, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHW4WiAnt105y3DhaZ3Fnlr_fKTYySbCMpF-c1mfytPM_B7im5VXayIstU7yKDlsw_ayNqZo97xN0TNVdDfIMV4UkePxe1M6NZ5N7mGPcimWddA', start_index=5987)
Annotation(end_index=6229, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4WXSJpUxP9NABf1A72CKQOWQFsUO17RDF5InWjoO2HQo1Avan7bnTu2aGnDov1913xbl839sXA1Iz7dnRgxcb73L8W6Pn3wQM8RBaLxisz5cmu-DXOqT5VaLfeNLz4iNZemTHLWBV3S6zgXO-4e9vNYFFE-jG5DNVw0ObkEZL2CV3Efu34JezBI78EdbKnBwOgEbDhy9HH3gYr6tk-c3VAw==', start_index=6215)
Annotation(end_index=6229, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5CpoCKhX2UQ6mVZL5QJR1Y2E0wJ-UP0y2waXWHZyBaYaUh4LDcGMNIdp1Teo21U3loZGt4kMVVmtRgh1Xgfmt4s13gVA2P2Tk_3JLMEMg0cNJcQ8HD7CI93TTaL-QPaJVUwkqrbsZevFj25_fK7AcfCrrYtQ=', start_index=6215)
Annotation(end_index=6827, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4WXSJpUxP9NABf1A72CKQOWQFsUO17RDF5InWjoO2HQo1Avan7bnTu2aGnDov1913xbl839sXA1Iz7dnRgxcb73L8W6Pn3wQM8RBaLxisz5cmu-DXOqT5VaLfeNLz4iNZemTHLWBV3S6zgXO-4e9vNYFFE-jG5DNVw0ObkEZL2CV3Efu34JezBI78EdbKnBwOgEbDhy9HH3gYr6tk-c3VAw==', start_index=6813)
Annotation(end_index=6827, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5CpoCKhX2UQ6mVZL5QJR1Y2E0wJ-UP0y2waXWHZyBaYaUh4LDcGMNIdp1Teo21U3loZGt4kMVVmtRgh1Xgfmt4s13gVA2P2Tk_3JLMEMg0cNJcQ8HD7CI93TTaL-QPaJVUwkqrbsZevFj25_fK7AcfCrrYtQ=', start_index=6813)
Annotation(end_index=7053, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF89Egp866hFze3N8V7jnLV-rCe3QJqhORs-B3QTQ1OYiABK6PUP1M80GivUUcqoqsc4qwp1KM48kdlSWlZ63n5flPj3V03w8F3VzSMmLYXbE0PZ_v8gcjeYQ4hilZCgTZK25t9PnU1X4YwJatg79AZUQcImg==', start_index=7039)
Annotation(end_index=7053, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyEcQci0OiyRAMd1S0XVcDGGeGZSWdJCjp2rIJ7cqlqXLWi5AHXu4iF3aDtP9SX6srSzgHOjOzisfS8g05faivs7Fn4YFxHtNsQniin8PFQkGV2GUGmJPDlMiNREmg4G260FqV77MviroSERNj6R0S3V_aojr4SlUPtI_NL5m8m6SOQmqfcRk_I8GhBq4kCFJyz4g6xkvvLJ0fvKGzBJV0qA==', start_index=7039)
Annotation(end_index=7181, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXJ2ZhWPAcUZ2Gh-u0Zk8YjnRV-I_KUM0P4clikOPxBhf2QplDPwQMMGPP3pV4AEnZdAKtVOIOWlU0PFbehaKzLN3W1MhsI2A_mh0L4z7fW0UwTLRyaeT1XrQbl_Eoj08wBsaJyzC5rcjOXUl7uoPi1UX-madDFvZVnXQWArn3uu2Pdw==', start_index=7167)
Annotation(end_index=7181, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyEcQci0OiyRAMd1S0XVcDGGeGZSWdJCjp2rIJ7cqlqXLWi5AHXu4iF3aDtP9SX6srSzgHOjOzisfS8g05faivs7Fn4YFxHtNsQniin8PFQkGV2GUGmJPDlMiNREmg4G260FqV77MviroSERNj6R0S3V_aojr4SlUPtI_NL5m8m6SOQmqfcRk_I8GhBq4kCFJyz4g6xkvvLJ0fvKGzBJV0qA==', start_index=7167)
Annotation(end_index=7360, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF89Egp866hFze3N8V7jnLV-rCe3QJqhORs-B3QTQ1OYiABK6PUP1M80GivUUcqoqsc4qwp1KM48kdlSWlZ63n5flPj3V03w8F3VzSMmLYXbE0PZ_v8gcjeYQ4hilZCgTZK25t9PnU1X4YwJatg79AZUQcImg==', start_index=7346)
Annotation(end_index=7360, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9p5ZCD-tAeWzIlVDW_nvIUe8-xctapiajpoMgZ7nqvvM02zmSVQElyN_jygMiB_JjHbnwRhTOYJebux5Gpu9qqTKBFTlIW1_ZhUTMv-uT8kjzMJBfXDXkQ-StTH4lvWIT1rZLRw==', start_index=7346)
Annotation(end_index=7557, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXJ2ZhWPAcUZ2Gh-u0Zk8YjnRV-I_KUM0P4clikOPxBhf2QplDPwQMMGPP3pV4AEnZdAKtVOIOWlU0PFbehaKzLN3W1MhsI2A_mh0L4z7fW0UwTLRyaeT1XrQbl_Eoj08wBsaJyzC5rcjOXUl7uoPi1UX-madDFvZVnXQWArn3uu2Pdw==', start_index=7543)
Annotation(end_index=7557, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF89Egp866hFze3N8V7jnLV-rCe3QJqhORs-B3QTQ1OYiABK6PUP1M80GivUUcqoqsc4qwp1KM48kdlSWlZ63n5flPj3V03w8F3VzSMmLYXbE0PZ_v8gcjeYQ4hilZCgTZK25t9PnU1X4YwJatg79AZUQcImg==', start_index=7543)
Annotation(end_index=8023, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF89Egp866hFze3N8V7jnLV-rCe3QJqhORs-B3QTQ1OYiABK6PUP1M80GivUUcqoqsc4qwp1KM48kdlSWlZ63n5flPj3V03w8F3VzSMmLYXbE0PZ_v8gcjeYQ4hilZCgTZK25t9PnU1X4YwJatg79AZUQcImg==', start_index=8009)
Annotation(end_index=8023, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHQEpVQXGEDbcvhftfyVG4sFzHH0bDm3T2NE0HHyG7YD3tztL0CFxZS-mSQ72uDNXa_CdMcplgv00sV88-mBOqpE-U8Tprc3XyhdZojF1SZv2QCcW-T12yVQd0olPsdAXherG5yQ-9udD5ue-t7YPVj4DkMjrggEy0ysxE=', start_index=8009)
Annotation(end_index=8443, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEykLU7IXaYAd3aHcAd-Eoi3_kQ3zqcTgb7VYsGpNWdURDpsMqQ0bmrkDrpYDzRoS96MVu8o6d7x9kuD4w68aqgLMxNlnhILdVxi6UMp2WwWERVioRX-QokI4Lkfh67HPR2dAjyR9RsKSADTpbgXNSXll_4aTSD3Wc=', start_index=8429)
Annotation(end_index=8443, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1HfTpnl84T7RpdDYP9FLXdwxmw5UsAja7dtIFXSO41d6fdRpKEFKdT_92pm4-DTDumxnPTfhDsmp0cvZk-vPxwP5oSLo5zBiicq8jM_MeY-sh6JcvXalVm2W2PUig33vkblUGwVkLudUORx4vNT8VzON-nCtr3dZxNhu_M-qcF6ZDgO4QgLgpJs4iArUWMS-2iDFvyOBi-nRqwPT9P9tO5IM=', start_index=8429)
Annotation(end_index=8686, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEykLU7IXaYAd3aHcAd-Eoi3_kQ3zqcTgb7VYsGpNWdURDpsMqQ0bmrkDrpYDzRoS96MVu8o6d7x9kuD4w68aqgLMxNlnhILdVxi6UMp2WwWERVioRX-QokI4Lkfh67HPR2dAjyR9RsKSADTpbgXNSXll_4aTSD3Wc=', start_index=8672)
Annotation(end_index=8686, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2ynTPu5Lw9iFQ0EwrGisQL5IrCZfob5_kXCab5rZnIlKItgXLGOggS5cUaJItPuhnuAMWPj8pJM8fjY65cR-VtH3vDVJzdgl0HrHMNQrfSfTNahoG8N8qMLLlzQ==', start_index=8672)
Annotation(end_index=8951, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoOwf5iU9aQY1z_v5sbQQMYpfmdG3ZxQ6CRcUB8aWg_tVvdlqN-EwrGhVaDlh-Vb7pZshiMvzVSwJ8KHpQLx8vuzTtaHiDts05QfAHUXKzwcPNNNYe-ZewFFmz2llcJetWalxlmlcKQG2cQlvyJmwF58ATrPhfk1eqV0CRuaJJre7o', start_index=8937)
Annotation(end_index=8951, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYLgnhcfSVCHwIpAiVgSrqfnBuixTPAf6Oqyel9WlnyUawB1l4YuwE5wToheQ_3DocNmHy_tuXipIDOJupYkK8wg2eUuMYBC8QIxaZePT61BAKOHw2fCF4gz0snQ9ON-V_8UEdp5Alt_DApqWcPZPFAv1pl0eAytAx4myqc7ec8cHKbLyG0aUl_hV0oRuK', start_index=8937)
Annotation(end_index=9245, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4ktbR89FuUXkz-Ou8xjNp1zWColWCajtiIVsbVyZ6yxJ4HTphRx3S-tLfbS5CNOyUl9DzgHnXjPcjQ5XjsxViFU9pNNkssLByExA0U-QSR9elxBS2lUE5D-MQwaE5WKoBvqj0f3NrlRLgOdrikMwxsXAyxULtkx_c41PCKWKMnTqMK1sLyX0Uy08=', start_index=9231)
Annotation(end_index=9245, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0QFQicSUdOnhf9lTc-qZJ7zV7lRLMfrzB91-VFHldBogrq1lCbuA3iwU56jY4S7GXil2Q2zPM0RPq27L2TaeIO5yAY_xZbdxCVS3eix1Od9eZ-1SIKpefYL9XtO_GS1b9hEldJU3qk2B8', start_index=9231)
Annotation(end_index=9502, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYLgnhcfSVCHwIpAiVgSrqfnBuixTPAf6Oqyel9WlnyUawB1l4YuwE5wToheQ_3DocNmHy_tuXipIDOJupYkK8wg2eUuMYBC8QIxaZePT61BAKOHw2fCF4gz0snQ9ON-V_8UEdp5Alt_DApqWcPZPFAv1pl0eAytAx4myqc7ec8cHKbLyG0aUl_hV0oRuK', start_index=9492)
Annotation(end_index=9985, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGeRcpFGUbGx--HB3EBtPs57rb_eb0uvCnuEaeewsfJQzONE1KNt8X3DOxlhfthBIxftPmFKOnYFeuFYp5sKutqiojIn6hd-KoEjjBHQhUEWl0EI2SttnRA39VNYB1fkiQ2HHrI2uaCeFqB38f8GL2nQmACOJ5jMYsVsO_BGHLDVVb2h3BtBFHFnqP2O781', start_index=9972)
Annotation(end_index=9985, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuXJ8TKnIgXQ7HJOXQN8x4MhBqUHKd2bevVprYXC_fjCBwYp-f9CHv6GPXoVgnzRU0B3bHQ1sFZr0IsjGEn9evlBZMefpR2P7KrwARBv7F4Tg85DZh92OqRCvL2QsUQIYD4MRa7PF40PhY7dPtG73pG21ishl5HMLlTsvwoQmdRg==', start_index=9972)
Annotation(end_index=10258, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSYp0wTqMDe4knkGTb_lFSb91Msde2G8fE-hn8rWy14MV44FR0bWOdotEgvvUXCVO_lon4Zs07WhCHqZXDzTBTEcp-RRl-glCvf4iLS9hAj6mJXYjjts903UPAt9rZ3UUOZaXF', start_index=10249)
Annotation(end_index=10484, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzHnGD-RaL2e96gFplKShNmjK5bwqi2-TAURdrxwRU-HdmQH8wH6YEGX5eU4KtWqvtVltFVfUkNq5L6OeSdDefXlna9cd9qcJMy5DDOojiRn3_VRVhpyegEsvd70yU0PrlWfZXVDI1h2DqYgOWDMOQt-FQ1H5uSdgqe5Na4joCjLGsGEY1Nie-M_gd9qDLHjD3lV8=', start_index=10474)
Annotation(end_index=11180, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFFvasDdS4S1_Tj3CxPAYzWMKJf-IBz37MAkot1vTSZ0jTM59CYE3xBqOZs6sO9kH6kSdCpsu3sJswmIlWrB2c6RhB7VHJJOyJGa3Cfffe2us7DQGqSFLyBgX0bZhxvtJH_-Y0yE7Pup9HNoA=', start_index=11167)
Annotation(end_index=11180, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHSYp0wTqMDe4knkGTb_lFSb91Msde2G8fE-hn8rWy14MV44FR0bWOdotEgvvUXCVO_lon4Zs07WhCHqZXDzTBTEcp-RRl-glCvf4iLS9hAj6mJXYjjts903UPAt9rZ3UUOZaXF', start_index=11167)
Annotation(end_index=11360, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyEcQci0OiyRAMd1S0XVcDGGeGZSWdJCjp2rIJ7cqlqXLWi5AHXu4iF3aDtP9SX6srSzgHOjOzisfS8g05faivs7Fn4YFxHtNsQniin8PFQkGV2GUGmJPDlMiNREmg4G260FqV77MviroSERNj6R0S3V_aojr4SlUPtI_NL5m8m6SOQmqfcRk_I8GhBq4kCFJyz4g6xkvvLJ0fvKGzBJV0qA==', start_index=11350)
Annotation(end_index=11855, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoFYR4I7VKC6YyEBH7YfY3-ZgiRvSK_nlyCokWAaNkGCnu5wzq4lrH0a2h27mn3o7K2AGr20td63_dWFrS_M3HlkjCNNBPXeECj2S_PFsC5W7WerTZao1SEfOC5Njy5VHIyzX0ys0BNUQka91s75fensyBw5ZLz--hcxqOdKGNbnbLjJTeH9jrudmOHqi8rQu45XdFt5KgAqF3l0U2MbL2AX16IzqsL31whO-Yo8Y6qzJ_tpqBDIPiWwfnti47Yguqn1vdWOjLlcOW_Mj8bZrKVjQy9c3orA==', start_index=11841)
Annotation(end_index=11855, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPePYQhNs--IkgdiIx0-_j-vn9qv_GB1bi30XQbxjBMy4Rl8d_66la4gqJxGowMPUXAmZ0_CaiAe1iXZ9CnRuZ587Gbr9FycKZL307AQt9-QhQ3vAJ1cg=', start_index=11841)
Annotation(end_index=12012, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdQ190pVooHSMxxn07r9cY3i9Yr5d_V4B-8E2uT8o0ePGtR2wwi6oJnaoIL78FtVN4tfxSkwFB4BBiYXTui23R0BnYYErg75k1AsGuL_rSAsA2lYzJsryMuCG2Dr0FoV0aWXXJnxGOt_rMWA==', start_index=11998)
Annotation(end_index=12012, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyyY5NTsuIKJDcoqmx0WniMUcERopFJDxCD8OOZZ57m49FHfK6PBkpJZjflZC8Sxd8uC5A5mgrtfpmJnaYRiPGh6Ol9JvE1Gal4UNIJXDxJZqTV1lVTF36gJCThqkORUw0ZVn4z5ly8Yvy-HQnLtHcSPPt2w==', start_index=11998)
Annotation(end_index=12186, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdQ190pVooHSMxxn07r9cY3i9Yr5d_V4B-8E2uT8o0ePGtR2wwi6oJnaoIL78FtVN4tfxSkwFB4BBiYXTui23R0BnYYErg75k1AsGuL_rSAsA2lYzJsryMuCG2Dr0FoV0aWXXJnxGOt_rMWA==', start_index=12172)
Annotation(end_index=12186, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGT4dE2f7ZeuxWtHD3RrK8i3Fu7ei5L_zp_oixGtfVM4wtSkKqpD2KKvpLoSjmsXsBes_vrN36fgtTJcGQdZIAX4sDpNpzDfD8UybvJPllSTf4gnoDZGXcDf7-QqE-Yy08RBM04KKYEnfZzjEW1bw-L_an4pTKd9RBW63TMuRcxli1Z4jlMvQ==', start_index=12172)
Annotation(end_index=12317, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPePYQhNs--IkgdiIx0-_j-vn9qv_GB1bi30XQbxjBMy4Rl8d_66la4gqJxGowMPUXAmZ0_CaiAe1iXZ9CnRuZ587Gbr9FycKZL307AQt9-QhQ3vAJ1cg=', start_index=12307)
Annotation(end_index=12640, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGALFbQLaGf2O5QIQkWsddgWHQ6hdpReiVTsBvbzLbh4MinbNgVjSeoMAGPFSb5KfH-OSfE6lIpkrXRnZR-GoMbPUOy9V3efYiijg_Jmzg7WVWgjbyNgJTGBEQ5h7025tExcplHxI=', start_index=12626)
Annotation(end_index=12640, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGyyY5NTsuIKJDcoqmx0WniMUcERopFJDxCD8OOZZ57m49FHfK6PBkpJZjflZC8Sxd8uC5A5mgrtfpmJnaYRiPGh6Ol9JvE1Gal4UNIJXDxJZqTV1lVTF36gJCThqkORUw0ZVn4z5ly8Yvy-HQnLtHcSPPt2w==', start_index=12626)
Annotation(end_index=13042, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGALFbQLaGf2O5QIQkWsddgWHQ6hdpReiVTsBvbzLbh4MinbNgVjSeoMAGPFSb5KfH-OSfE6lIpkrXRnZR-GoMbPUOy9V3efYiijg_Jmzg7WVWgjbyNgJTGBEQ5h7025tExcplHxI=', start_index=13028)
Annotation(end_index=13042, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH93TYdfzPhYe_1y69D29Ty2xr8RDp1M_uZ1GonprfINiV_XrqmXgDr1fGd01tM9igqXABjwSjzf66DQsxCguRegalHG85sEHclQRigy1fWVUchLMDTDIrWlLl_gM8IeBUH2_HNlIx8N9rQLr6R2mY=', start_index=13028)
Annotation(end_index=13251, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_fSFPTaIk55y3RQo9QN55W2iTaQNAYWAqJL7CUF8DaFXReJL26yGu1vR7Wpw6qFskRLk1MdRAdONgSqFjNga-g-vXWeSyexTEdUVz94DdrX4un-j_1EKjZRzZdsAWoC5qkcrBHOVX3xbKSXEcqZKvNoaxx7lJT2bB4II=', start_index=13241)
Annotation(end_index=14076, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGf51rOoINAmSTuWFKeL6r43yVEzJoZIFA0rkAmZZI4dRNuNe5mJayeb-JJuG-DOmruxed7CTuwOWDj5RqN25syJzre1yLjcINsfoIbGR-ZFpN3WkHCibYVeiTu1sq1FLq1fDuLdrjcUD620vIP0TiYkjjPXQ==', start_index=14062)
Annotation(end_index=14076, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH6qsSCkcBLzyO4fNCcQm8WjiWf38FAHqQGjjJpww_HzHZ13UrkOmzgy53TMCZq2_9NNz7JWct3aDT1W0QClqhrOCuTJwFwPnw7RjL0HUazG4gzFmzGKQ==', start_index=14062)
Annotation(end_index=14326, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjPSc71iQjTK4k5jjB1MG2Cd4ZJMpTx7u26Q9d76DcZuqSoQ4OoeoyM5fcw5ug_WeVe7hayhjgIFdMNA229IdiUyLZMlL_FE8uCAkb57WrT7ww9a_CKtYwGdQe3Ept3avI0WnE', start_index=14316)
Annotation(end_index=14804, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjPSc71iQjTK4k5jjB1MG2Cd4ZJMpTx7u26Q9d76DcZuqSoQ4OoeoyM5fcw5ug_WeVe7hayhjgIFdMNA229IdiUyLZMlL_FE8uCAkb57WrT7ww9a_CKtYwGdQe3Ept3avI0WnE', start_index=14790)
Annotation(end_index=14804, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrp32xjbJIyr6y4x33Eb00nC8TuLt__ylvkP8D_gmV4dqZFxDp6-1qWOOpaPLdvQ0VnGTFMm045rg4uTsYv8vLQ6h4GxYick4BWSUDIh2fje3kTTF5h2x5yzLZqCugW_tdkzOOLNqLVVVylJIqqSeeKrfr', start_index=14790)
Annotation(end_index=14932, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrX8oo6qOrHkxHaX3UqTnGDpApxyMrDnBoJS-B75Q1StPqn1w74tgDzGGzuy-T9tXBsW999K90pO5pL-3AH8Rsz9-9JxyQunihzzg7--006NJaMbQ6Cs6Yc2_ri3v6bzojtggM-fGBmCETb0m_LdOtem1-fQ==', start_index=14922)
Annotation(end_index=15435, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEPOPENEPc3Luf65mB8uLfgQXYjrq3MJLShdwZq99cy8DXLwG9ZTW6r_zoucNF5osR5xD41g05nUHn4_w1VTC91vn9WyR6RGBZHIkxccS6iHmkrEly_-zbljMLOwtIXY5Ssu-qJETLY7SRkCa8IABXUgOpLaI-v28J7MYH1FoTuBpr8mWUfn3NkPJlozBz1syqsKjp_kIk_KrfEjM8xxDNuzA22Gv-rY-Lo2Y_pP_sWcgp2wu_6IyyfxzfXVTGFTN93MHYIUHU0vcJ7NxGnk6AGndORpvaqmq90_bawYw==', start_index=15421)
Annotation(end_index=15435, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrp32xjbJIyr6y4x33Eb00nC8TuLt__ylvkP8D_gmV4dqZFxDp6-1qWOOpaPLdvQ0VnGTFMm045rg4uTsYv8vLQ6h4GxYick4BWSUDIh2fje3kTTF5h2x5yzLZqCugW_tdkzOOLNqLVVVylJIqqSeeKrfr', start_index=15421)
Annotation(end_index=15636, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2ynTPu5Lw9iFQ0EwrGisQL5IrCZfob5_kXCab5rZnIlKItgXLGOggS5cUaJItPuhnuAMWPj8pJM8fjY65cR-VtH3vDVJzdgl0HrHMNQrfSfTNahoG8N8qMLLlzQ==', start_index=15626)
Annotation(end_index=16091, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0QFQicSUdOnhf9lTc-qZJ7zV7lRLMfrzB91-VFHldBogrq1lCbuA3iwU56jY4S7GXil2Q2zPM0RPq27L2TaeIO5yAY_xZbdxCVS3eix1Od9eZ-1SIKpefYL9XtO_GS1b9hEldJU3qk2B8', start_index=16081)
Annotation(end_index=16546, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvcBjNh7dQhxoyWkv-v2n304nphWkB4wZuPTPhBEsUkjiQGVddILo0IDQZPdH6fe5F9tUKUxmmjls3CZP3o9D2G_zlHFNMGtYrl1YidHJal0DDYi2uEfkcbbzZpQGMgoMPm9QAtUmx5NGb1N6BSuIpINJ5Yf_lHA==', start_index=16537)
Annotation(end_index=16967, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEbWb0iYlCskqwiVf0LPfV8hvbVjJGPgVLbaFUbEx8Z54lDhL4ralpNDhtoLq62jl9m4TVAFgga2csCrIWZ57ODe6SK83ISJ4wsw-nSuAMBpHoSfgv2I_4WE-SO8CCxg==', start_index=16957)

## Sources
