# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** ab318d5f | **Time:** 898.17s | **Cost:** $0.91745
--------------------------------------------------------------------------------

# Open Banking API Standards: The Dialectic of Data Security, Interoperability, and OAuth 2.0 Token Management

### Key Points
*   **The Security-Interoperability Nexus:** Open Banking standards, particularly the Financial-grade API (FAPI) profile, are designed specifically to resolve the tension between data security and ecosystem interoperability. While "vanilla" OAuth 2.0 implementations pose significant risks of permission leakage and token theft, FAPI "hardens" the protocol to balance these competing needs.
*   **OAuth 2.0 Vulnerabilities:** Standard OAuth 2.0 token management, if implemented without strict constraints, increases the risk of permission leakage through mechanisms such as bearer token theft, open redirection attacks, and scope creep. The "bearer" nature of standard access tokens means possession equals authority, a critical flaw in high-value financial contexts.
*   **Mitigation via Standardization:** Advanced standards like FAPI 1.0 Advanced and FAPI 2.0 mitigate these risks by enforcing **sender-constrained tokens** (via mTLS or DPoP), **Pushed Authorization Requests (PAR)**, and **Proof Key for Code Exchange (PKCE)**. These mechanisms ensure that stolen tokens cannot be used by unauthorized parties and that authorization parameters cannot be tampered with during the flow.
*   **Granular Consent:** To address permission leakage at the logic level, modern standards are moving toward Rich Authorization Requests (RAR) and granular consent models. This shifts the paradigm from binary "all-or-nothing" access to fine-grained, user-controlled data sharing, reducing the attack surface and ensuring compliance with data minimization principles.

---

## 1. Introduction

The global proliferation of Open Banking has fundamentally restructured the financial services landscape, transitioning from closed, monolithic banking systems to distributed ecosystems driven by Application Programming Interfaces (APIs). This paradigm shift mandates that Third-Party Providers (TPPs) be granted access to sensitive customer financial data held by Account Servicing Payment Service Providers (ASPSPs), typically banks. The success of this ecosystem hinges on two critical, often opposing, pillars: **interoperability**, which allows diverse systems to communicate seamlessly without bespoke integrations, and **data security**, which ensures that this openness does not compromise the integrity or confidentiality of financial assets [cite: 1, 2].

At the technical core of this ecosystem lies the OAuth 2.0 authorization framework. While OAuth 2.0 has become the de facto standard for delegation, its flexibility creates a "double-edged sword." In its unconstrained form, OAuth 2.0 introduces significant risks regarding token management and permission leakage, potentially exposing the ecosystem to systemic vulnerabilities [cite: 3, 4]. Consequently, the industry has coalesced around "profiling" OAuth 2.0—most notably through the Financial-grade API (FAPI) working group—to constrain these options and enforce rigorous security controls [cite: 5, 6].

This report provides an exhaustive analysis of whether Open Banking API standards successfully balance security and interoperability. It critically examines the mechanics of OAuth 2.0 token management, the specific risks of permission leakage, and the efficacy of FAPI standards in mitigating these threats while maintaining a functional, interoperable ecosystem.

---

## 2. The Role of OAuth 2.0 in Open Banking Architecture

To understand the risks of permission leakage, one must first analyze the architectural reliance on OAuth 2.0 within Open Banking. OAuth 2.0 is not an authentication protocol but an **authorization framework** that enables a third-party application to obtain limited access to an HTTP service on behalf of a resource owner [cite: 4, 7].

### 2.1 The Delegation Model
In the context of Open Banking, OAuth 2.0 functions as a digital "valet key." Just as a valet key allows a parking attendant to drive a car but not open the glove box or trunk, OAuth 2.0 allows TPPs to access specific financial data (e.g., transaction history) without handling the user's banking credentials (username/password) [cite: 8, 9]. This separation of roles is critical for security, as it eliminates the insecure practice of "screen scraping," where TPPs would store user credentials to impersonate them [cite: 10].

### 2.2 The Token Economy
The framework operates through the issuance of tokens:
*   **Access Tokens:** Short-lived credentials used to access protected resources (APIs).
*   **Refresh Tokens:** Long-lived credentials used to obtain new access tokens when the current one expires.
*   **Authorization Codes:** Temporary codes exchanged for tokens [cite: 11, 12].

While this model facilitates interoperability by providing a standard mechanism for authorization, the management of these tokens introduces the primary vector for risk. If an access token is a "bearer" token, any party in possession of it can access the user's data, regardless of whether they are the legitimate TPP [cite: 11, 12].

---

## 3. Risks of Permission Leakage and Token Mismanagement

The user's query posits a critical concern: *Does OAuth 2.0 token management increase the risk of permission leakage?* The academic and technical consensus is that "vanilla" or poorly implemented OAuth 2.0 indeed exacerbates these risks. Permission leakage in this context manifests in two primary forms: **technical leakage** (token theft) and **logical leakage** (scope creep).

### 3.1 Bearer Token Vulnerabilities
The default state of OAuth 2.0 access tokens is often "bearer" tokens. This creates a high-risk environment where possession of the token is synonymous with authorization.
*   **Token Hijacking:** Attackers can intercept tokens via unsecured networks, malicious browser extensions, or compromised logs. Once stolen, a bearer token can be replayed against the bank's API to exfiltrate data until the token expires [cite: 11, 13].
*   **Leakage via Referer Headers:** If an authorization server or client inadvertently includes the authorization code or token in the URL, it can be leaked to third-party analytics scripts via the HTTP `Referer` header [cite: 14].
*   **Browser History Exposure:** Tokens passed in URL fragments (common in the now-deprecated Implicit Grant flow) remain in browser history, accessible to anyone with physical access to the device or malware installed on it [cite: 14].

### 3.2 The "Open Redirect" and Injection Attacks
OAuth 2.0 relies heavily on redirects to pass control between the TPP, the user's browser, and the bank.
*   **Open Redirectors:** If the bank's authorization server does not strictly validate the `redirect_uri` parameter, an attacker can manipulate the flow to redirect the authorization code or token to a malicious server under their control [cite: 13, 15].
*   **Authorization Code Injection:** An attacker can inject a stolen authorization code into a legitimate user's session. If the client application does not verify that the code was issued in response to its own request (e.g., via PKCE), the attacker can trick the victim into binding their account to the attacker's resources [cite: 14, 16].

### 3.3 Scope Creep and Excessive Permissions
Permission leakage also occurs when the scope of access granted exceeds what is necessary for the service.
*   **Coarse-Grained Scopes:** Traditional OAuth 2.0 implementations often use broad scopes like `read_accounts`. A TPP needing only the balance of a single savings account might inadvertently be granted access to transaction histories of all checking, savings, and credit accounts. This violates the principle of least privilege [cite: 3, 17].
*   **Scope Upgrade:** Vulnerabilities in the OAuth server can allow a malicious client to request a low-privilege token but manipulate the request to "upgrade" the scope without the user's explicit consent [cite: 18].

---

## 4. The Financial-grade API (FAPI): Balancing Security and Interoperability

To address the inherent weaknesses of OAuth 2.0 in high-stakes financial environments, the OpenID Foundation developed the **Financial-grade API (FAPI)** profile. FAPI is not a replacement for OAuth 2.0 but a strict "profiling" of it—essentially a configuration guide that mandates specific security features while forbidding insecure options [cite: 3, 6, 19]. FAPI is the industry's primary mechanism for balancing data security with interoperability.

### 4.1 Constraining OAuth 2.0 for Security
FAPI "hardens" OAuth 2.0 by enforcing constraints that mitigate the risks of token leakage and mismanagement.

#### 4.1.1 Sender-Constrained Tokens (mTLS and DPoP)
To neutralize the risk of bearer token theft, FAPI mandates the use of **sender-constrained tokens**. This ensures that a token is cryptographically bound to the client that requested it.
*   **Mutual TLS (mTLS):** The access token is bound to the client's X.509 certificate. If an attacker steals the token but does not possess the client's private key (used for the TLS connection), the token is useless [cite: 1, 16, 20].
*   **Demonstrating Proof-of-Possession (DPoP):** An application-layer mechanism where the client signs the HTTP request with a private key. The token is bound to the public key, preventing replay attacks by unauthorized parties [cite: 16, 20].
*   **Impact:** This directly answers the user's concern about token management risks. By moving from bearer tokens to sender-constrained tokens, FAPI decouples "possession" from "authority," significantly reducing the risk of permission leakage via theft [cite: 21].

#### 4.1.2 Pushed Authorization Requests (PAR)
In standard OAuth 2.0, authorization parameters (scopes, redirect URIs) are sent via the browser URL (front-channel). This makes them susceptible to interception and tampering.
*   **The Mechanism:** FAPI 2.0 mandates PAR (RFC 9126), where the client sends the authorization parameters directly to the bank's server via a secure back-channel API call *before* redirecting the user. The bank returns a `request_uri` reference.
*   **The Benefit:** This prevents attackers from tampering with the scope (e.g., adding `payment_initiation` to a read-only request) or the redirect URI in the user's browser. It ensures the integrity of the authorization request [cite: 16, 20, 22].

#### 4.1.3 PKCE and the Prohibition of Implicit Grant
FAPI explicitly forbids the insecure "Implicit Grant" flow (which returns tokens in the URL) and mandates the **Authorization Code Grant** with **Proof Key for Code Exchange (PKCE)**.
*   **PKCE:** Adds a cryptographic challenge-response to the flow, ensuring that the party exchanging the authorization code for the token is the same party that initiated the request. This prevents authorization code injection attacks [cite: 4, 16, 23].

### 4.2 Enhancing Interoperability through Standardization
While FAPI's primary goal is security, it is also the linchpin of interoperability.
*   **Reducing Optionality:** OAuth 2.0 is a framework with many options (different grant types, signing algorithms, token formats). If Bank A uses Implicit Grant and Bank B uses Code Grant, a TPP cannot easily connect to both. FAPI standardizes the configuration (e.g., "You MUST use Code Grant with ES256 signing"), allowing TPPs to build a single integration pattern that works across all FAPI-compliant banks [cite: 3, 5, 6].
*   **Global Adoption:** FAPI has been adopted as the basis for Open Banking standards in the UK (OBIE), Brazil (Open Finance), Australia (CDR), and North America (FDX). This convergence suggests that FAPI is successfully functioning as the global interoperability standard [cite: 6, 24].

---

## 5. The Tension: Complexity vs. Adoption

While FAPI provides a robust technical solution, the "balance" is not without friction. The complexity of implementing FAPI creates a barrier to entry, potentially hindering the "interoperability" goal by slowing adoption.

### 5.1 The Complexity Barrier
Implementing FAPI—specifically requirements like mTLS, JARM (JWT Secured Authorization Response Mode), and strict certificate management—is technically demanding.
*   **Implementation Costs:** Banks and TPPs face significant infrastructure costs to support these standards. Smaller institutions may struggle with the technical overhead, leading to uneven implementation and "fragmented" interoperability [cite: 25, 26].
*   **Regulatory Divergence:** While FAPI is the baseline, regions often add "local flavors." For instance, the UK OBIE profile is based on an older FAPI draft compared to Brazil's Open Finance (based on FAPI 1.0 Advanced/FAPI 2.0). This versioning mismatch means that "global" interoperability is still aspirational rather than fully realized [cite: 6, 24].

### 5.2 FAPI 2.0: Simplifying for Security
Recognizing that complexity hinders security (misconfiguration is a major risk), the OpenID Foundation developed **FAPI 2.0**.
*   **Attacker Model:** FAPI 2.0 is defined by an explicit "Attacker Model" rather than just a list of requirements. It aims to simplify the profile by removing older, complex features (like the Hybrid Flow) and relying on modern, cleaner standards like PAR and PKCE [cite: 21, 27, 28].
*   **Interoperability Focus:** By reducing the number of optional configurations and aligning with the latest OAuth Security Best Current Practice (BCP), FAPI 2.0 aims to lower the implementation barrier while maintaining or exceeding the security of FAPI 1.0 [cite: 16, 22].

---

## 6. Addressing Permission Leakage: Granular Consent and Scope Management

Beyond the technical security of tokens, "permission leakage" also encompasses the *scope* of data shared. If a user cannot limit what data is shared, their privacy is compromised even if the token is secure.

### 6.1 The Shift to Granular Consent
Early Open Banking implementations often forced a binary choice: share *all* account data or *none*. This led to excessive data exposure.
*   **Granularity:** Modern standards (driven by regulations like GDPR and CDR) require granular consent. Users must be able to select specific data clusters (e.g., "Account Balance" but not "Transaction Details") and specific accounts [cite: 17, 29].
*   **Rich Authorization Requests (RAR):** FAPI 2.0 and advanced Open Banking profiles recommend the use of RFC 9396 (RAR). RAR allows clients to request fine-grained authorization details in a structured JSON format (e.g., "authorize payment of $100 to Merchant X") rather than opaque scope strings. This ensures that the token issued is strictly limited to the user's explicit consent, mitigating scope creep [cite: 16, 20, 24].

### 6.2 Dynamic Client Registration (DCR)
To prevent unauthorized entities from even requesting tokens, Open Banking standards utilize Dynamic Client Registration.
*   **Vetting:** TPPs must register with the ASPSP (Bank), often proving their identity via a software statement asserted by a central directory (like the OBIE Directory in the UK).
*   **Metadata Validation:** DCR ensures that the TPP's redirect URIs and encryption keys are pre-registered and validated. If a token is leaked, it cannot be used by an unregistered client, and the redirect URI validation prevents the initial leakage [cite: 30, 31].

---

## 7. Conclusion

The research decisively indicates that **Open Banking API standards, specifically the Financial-grade API (FAPI) profile, successfully balance data security and interoperability**, provided they are correctly implemented.

Addressing the user's specific dichotomy:
1.  **Does OAuth 2.0 token management increase risk?**
    *   **Yes, in its "vanilla" form.** Standard OAuth 2.0 bearer tokens are susceptible to theft, replay, and leakage, posing a severe risk in financial contexts.
    *   **No, when constrained by FAPI.** By mandating **sender-constrained tokens** (mTLS/DPoP), **PKCE**, and **PAR**, FAPI neutralizes the inherent risks of OAuth 2.0 token management. The token is no longer a "bearer" instrument but a cryptographically bound credential.

2.  **Do standards balance security and interoperability?**
    *   **Yes.** FAPI creates a unified "high-security" target. It enables interoperability by ensuring that all participants speak the same secure dialect of OAuth 2.0. Without such standards, security would be ad-hoc (creating vulnerabilities) or interoperability would be impossible (due to fragmentation).
    *   **Caveat:** The complexity of these standards remains a challenge. The industry's move toward **FAPI 2.0** represents an acknowledgment of this friction, aiming to simplify implementation without compromising the rigorous security model required to prevent permission leakage.

In summary, the risk of permission leakage is not a flaw of the Open Banking concept but a characteristic of unhardened OAuth 2.0. The adoption of FAPI standards is the necessary corrective measure that transforms OAuth 2.0 from a general-purpose framework into a secure, interoperable foundation for the financial economy.

---

## 8. Detailed Analysis of Key Technologies

### Table 1: Comparison of OAuth 2.0 Vulnerabilities and FAPI Mitigations

| OAuth 2.0 Vulnerability | Description | FAPI Mitigation | Mechanism |
| :--- | :--- | :--- | :--- |
| **Bearer Token Theft** | Stolen tokens can be used by anyone. | **Sender-Constrained Tokens** | Tokens are bound to the client's mTLS certificate or DPoP key. Stolen tokens are useless without the private key [cite: 16, 20]. |
| **Authorization Code Injection** | Attacker injects a stolen code into a victim's session. | **PKCE (Proof Key for Code Exchange)** | Cryptographically binds the authorization code to the client instance that requested it [cite: 16, 23]. |
| **Open Redirect** | Attacker redirects user to a malicious site to steal codes. | **Strict Redirect URI Matching & PAR** | FAPI mandates exact string matching for redirect URIs and PAR prevents URI tampering [cite: 14, 16]. |
| **Scope Creep / Tampering** | Attacker modifies the request to ask for more permissions. | **Pushed Authorization Requests (PAR)** | Authorization parameters are sent via back-channel and signed/authenticated, preventing front-channel tampering [cite: 20, 22]. |
| **CSRF (Cross-Site Request Forgery)** | Attacker tricks user into authorizing a transaction. | **PKCE & State/Nonce** | PKCE and OIDC Nonce parameters provide robust CSRF protection, validating the origin of the request [cite: 14, 16]. |

### Table 2: Evolution of FAPI Standards

| Feature | FAPI 1.0 Advanced | FAPI 2.0 Security Profile | Benefit of FAPI 2.0 |
| :--- | :--- | :--- | :--- |
| **Grant Type** | Code, Hybrid, Implicit (deprecated) | **Authorization Code Only** | Removes complexity of Hybrid flow; eliminates Implicit flow risks [cite: 6, 16]. |
| **Request Object** | JWT (signed request object) | **PAR (Pushed Authorization Request)** | PAR is simpler to implement than signing complex JWTs and provides better privacy (data not in URL) [cite: 6, 16]. |
| **Token Binding** | mTLS primarily | **mTLS or DPoP** | DPoP allows sender-constraining at the application layer, easier for environments where mTLS is difficult (e.g., SPAs) [cite: 6, 16]. |
| **Compliance Model** | Checklist-based | **Attacker Model-based** | Focuses on preventing specific threats rather than just ticking boxes, ensuring a more holistic security posture [cite: 27, 28]. |

**Sources:**
1. [scalablesolutions.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuWvxl5_Oq1RRuv-f2rHtp394MXwt_LqSOMBWniU78VFyKPrvlT25zp6HQOypJjTbD8YZHBwyQ4_AXFcxq4px8kUoey0cPwEPwOxXUDTemhsHqXC6PwGEGoQD8j_sEkAp5_ZatV8RGnq66E6W7DnLHQQIZMXnO2Vc=)
2. [samlink.fi](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQfIbRhkCmMHBYpPPkige3rko2S8I0NS-toFRwfJGbaH1s357JoKFIIjffFj2wkanAv0iWhK-72cE3o29FjZQeEnpsR-SCNdWI9_fZqY5RYO4zIyosPTHNOZ2o4FUuuJQtreHaS04Rmkj1i1pvzZwgCkqOm4kyybKJXh1tO05igx6LXaNompLNZde4)
3. [atlassian.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKofV6Z1eYRtj0PC2MiMLbGpfWrcjW7akRd6EeWzrIxR88O0PG7cuguWomoQ5tG9X1c-oCiKMOpNog0BBvLKDClDRx5zd33Nh9crDxngoENN5yXe4qW-SP-tJ_j2VpoLv7RRzajIkZ_5QCv23JsLUWzkEZHS6TheKL0-Zr5cmjv62-vYNi5EMywM08fS9LqwlBbeVqJX-8HK0E4J5IoOgVwrHD2fyeHx5jwxAXfzF-bg==)
4. [apisec.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEeOvdScDmIoFYdqEJ7Zt70NIRyV8nmFwszwihjInlqgBlrwl9zY7EJfWa4xo1PBLV7e_HpE6i_WPTybj-693Gxs-Qt_ZZqsNlzhJ37KQzid-i7MgmJiO8RbM72lz6h7YiNdjq8gBhT6G3FWPUncm-a)
5. [globalbankingandfinance.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZn7Bkq_fv14fl_n6H2GCZLhHX0R6oT2EwLuyvBBa7o5vFmlcmh-YouaM2EfuSIdYcbFoxS_Crlsn4rlostLs8P5IOkecJL77ToEwNdwEYsjRR6BlhIbBDNoXrdPIgkxRJiVkHKrGm7LyMszQaQUCe_ry1f7QiQD2KUbryr1pSwqKZ4Uv2RV1h10_evGPkZx8VUZAzThh7I5ZkmI_K2mBH46mQ8zYo-_Kh5Q==)
6. [openid.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFU_p0TPtB_HP2LsW0wyr2X5MLT1lTEtZ-jGT7zDz8AwNTpyRrtSrwCT542B3nwKX0iZ-aBfTpyUHJHbMM8S_xxcZLoUB2hfTNeTECjp4swIKbEmmZXngtw9ubOvfQ9pKBBIOU7qv5KM7tQQUItA_CnwZzWRQpRpRDBuj615ZnZdAQnSiibhE-7wZduGzg8n-o3w-pBirwPqQ==)
7. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFM6TUSdMC5_P_rpTIEBcgk9VPEPwpkLTM3-SG9AG2G41rvZfeyLvOeebNA4ZrVKjhMkFvYRhgqzyxHVCO58yW6wrso6PGYpCJlbE4mf8sKe-zvNGn7ZASAauLiHuzZBoNYJ80IpkPVan2xm2L7IMNVI5OiPCAu1D0vTP7ajd44idvGz6cxb9AK73Q5YiQvxDhhlBa3UfMT5_848F4sc8npK0OdpGrrAK3lrsfHO5Mt)
8. [flinks.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbeJbcPEwuo5r-HNEWEqvJsQFRnUOTkRXx2tAwY7QUfRyK55LkFzP_xdP2_mqo1281IDfdH608p2qrji_rg1Pb5wjiNmLNEfTUKQq2yuyBiALTRVOlY2pRSpp8EU36v0xFuBDpiRZqrC9EXJN7Aw==)
9. [digitalapi.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjOCd9zEF-WsiuhSE7eI_2qERf8CyiJNThCCdTnCT0jYXAI53Urp51DvBctOWIKy4lQn8TcfC2-XrkhC8sjDmY4srbTDPmW6QMa10UfBawqN55LKH7Pn6AMICxbz9B0SLFT_Q4y0mHFo6R5A==)
10. [mx.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTYLh0jfiNIYbP1Cexasrd4mRfVAZjkDxrntxcmkH8QAm3NKHMt9piJmWP3nfhO387_GWpcwksa47MpAY357q-Zzu53gCLsJfq-HULyawykgiXZJUa3wGaSwjQwza2_rIVlmHnnMU3LLtznA==)
11. [clutchevents.co](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnwL8SmZChNr-vhaiVSHii5bRLpc3ouLr53vGFbG3sciIDyiaZQBMUn4FDLKAwvr4FJ18OwzSinHSpfnoAnlZcgqYfMb8hVkpYsMrfC8dhH8j7llBjjKU3nF3XgULJIEmuNHwyDzd_8QxyuSlJ04Ukf27dQO430LmKcfuNE0VB6uFfgXkba3p48jPbLJ0bMi9w8XYMpsxoI1MDQy0f2YoomeAVfS8f44L2Wj81JUQT9I-khQ==)
12. [securityboulevard.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHu16WwmDWYVZDXkLikD8clo0LuYXBpoS_VUSlg4eduCVOpybTJNxMi1PT8SLlOW15jDCC9OyRN-aOA0Ku9tn9_grdidcVHPWUezf3iQxxehDJBsxT6dX0GBqR92TkqmT3dtm5bJkWgKtbwE7fX0l3wqzKZbo8LFWh9onTGsbn7yKIweVe4MvM9W0Y2OJoZMCCgQl9OZ6l4mzYkiGfJdu965nSkDcLI)
13. [cybershots.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFblqWsU45XPye8BFpgxcS48xHGviT7X4qu1iNhVXlyiWHCe40EOHGyeaG-qcmH31nTHsHgrWhj6Uk-JkNmzqyhVkR9mf3X1ximHKw9hybBtdGcvA6zIaQwkRZrsGfZrJskQJsrd1Hewvvr7xIM0JyHx6barHdde-fq-oJxjk63hJY=)
14. [ietf.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLUQS7QkmNbCUDwBBVvKVM24ViLmE4tousosujPOJYgXmqF6LpTXwtB0BXrHr1lh27SRERmuZPzSgy1wCDN0HRygTOUQpUyENGLZFl20SZ98jA3f0QKCd1uChfoBsQloxaD5hdswVYRoBduqYHLFIRqVSicpUjHbj3yUlzq0E=)
15. [securityboulevard.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTr3T1WgcqPlL0dTFev_P2DNB3Y11u-u8EgUNvTH0WfEHg5x_p7lwplSey_fifU6MJi53r5RWid2GfjGCDXWvs2tqHQxn1K2cq2SuHlCAugJJjY05uChIMicPhxB_tYGED4Z72qTeT2jkKPGlR8iadn1GIKFJOzep3hm1Zb5prfeq-Md603dVDuESarbjzvCfLr1z6kRzEHKUpkPhqjg==)
16. [openid.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKGTTng3Fof0UBhXZPzJz5wb6SNz5kzpTS3ayAr0Qi3MMUIcRKD9IX0k8CIBB4qMSoHgcKIuyApOkNjY_cD58t2hZyyU4MHV7Q1Gk93j5JACO2G16te0V9lHzNqouEflRHuGjFnpbrF0lcznMP5SNDR8tD)
17. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiT0b7bIZBdU3NtF7eQs84Z6nAKY2orp0jv9rWzzvvUtAs1Z8oX-x6MOS0FXxaIfQCL050UTFrvNm78RQqaD7kUpK7MdGeqAAlF8ETpwW0YWizb3z8oXrBI_EhQ-V0m9mxrOyNbSea-4XO_ztBJooTng20maq6-L5lJHelA4Ht5Toa9TWG8htRhC9V3dsa_VcpDFhprW1-54P3aFmHjTYyrzrrbLTasAJ5fF2RN_a4ZkfwXc0eBLkdBMlxT0FC3hz_)
18. [vaadata.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0TmsH-vQxuln28xqs6w2jURwKizUOzrBbDA5Pl4uFMQCIcg_ufY3rRKtulSmCO--5tizAFR3avNIjz3uZLA370LcjcKIc01nT51pYZUxs8hhpr9yY3fjIj-gNAhiXYHpr9MJvNphxu8PBhQk228YBRjRCbEDAxgi64w-oeSPbzrUQPZjq8lSe-ac=)
19. [curity.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeR8bU4W0RzkG9o7FzLzRBG8JWujknfDeQToqPfuSF3CPSA-IUEzHsFvQxLMG5BHK1ya9Ky_jh8Vkos3feXCGZFLDVwD3YZ4g5KgcVNx42WKABYD6gd8wy9bpco-FjodynoXNcT-O9gfmdGcNwPlZv)
20. [openid.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_RP_nm-DFesiCbduL2xkVQ1ONeUk3kxjuKIHd4m07e8BqsIiSQtnk5WOqP9u9q1mnqidNCEvhTq9CONJhRiY8RaiN-2KjVuw6O4iv_B1DofBt4Pl70l4BD6lFZPpTV_o7DbGELqU4kw==)
21. [secureauth.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0aIE_9c9BojL_rEKT6rMO0f-BHfs7FrhGwdfdxILE5rg3HicIhSIPy-jKy1TNPDed0NCBxigouEHQp3k06q_-b_KlkI2iHMSrH9GbziRhuxPdY28XROMKdazFYYy8HqO0R-AYvZx3dFUo9-EMxfpHNArH-jomqBFtN5hJM9l1FoMqI2XlVSM=)
22. [hackmanit.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7uJ78WNuos5GR7DC-_bDYxDD5JrS1L6Tg9X_v8SmR0bXb97lgYSSjZHbKrJzBIKxCcZemX3cTKn1xipilJ5hLf0B6QyqRh7Ll7JN0KxjtyiPL8kO27EZyf1DrcBo0lB_Hr58CIkN60iIcGBx3E5aP)
23. [owasp.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZM6xOcaJPCbHq2zww1f7zMtI2WpyeFzCQq77QzBq6eOln4yzXUJIFVMWoK-d8qHLjBunC0IV5L06fmzewHdX5q2n6yzieZn79njxWo-T7m5WCgf0otoJeUuEgKKwcoE364JMpZSt8_hJmiGZQBk1t2_EqDajaQ0cxKGoq_1u3nM8z1TYerxclFm17WgZQI3mgb-lO7K_WdnaXUM1YUA==)
24. [openid.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZwCNB9l3H_3Ze56HnqVxlpiZz4kpcORboJH7eJdWy9uONgaABhWOgGeI45ggrLhA6TLiaHQIPEUrZZFOSDezuxgN6zm0UW1X_cUyUb5JeLpcH_17wUiJW_tjsc1BL6OU4u9QbwOlWogMTk1RJY87r_CfJ8dLGBBOKUjaSRew1Tu5neb_SgCFa-76pkC2M06JWONuBWp4ZtdIWWzXzn5sMVzJEpOJ5B3XEu7vZtAVnooQKlwKoq1A=)
25. [thepaymentsassociation.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnvgxrGdiSRcHBtI08HSfEIP-cncwShGtiLzACNjcYGPrn-DUE0pdz0BZfaGuHbzC35ZYe2YDAkomEAmt9Be0381aj3gpyI1AjjFwgNYVXh26PQHOubzBlX8P2MpOWLO45g2dwtKkNR9wU377NXChVYmrBvqfTA6UJhrZwBIbxRKsFOrzk0NyK0ed3RT8hT5UeUImzqYHtbtQf2SfE9h_hbU7CLFEkilAl-WqdfVvhw34e__RPVN1gq83iQV0=)
26. [kitrum.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEmPsOdhk4gg8RrhCiMULD3t-EQiKeM7cIsvFx2M3zf-s34YZLTJ4l7oW9yool1OOq6pOaXN13fesaefD7MYBmHMhrXazixkLlz1XtIMie5yMAA-wxMXyvTPPeLpXLB_7uxb0aX2S6282bw7DnDh0_ndydn9wrblyQ)
27. [secureauth.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7tdAOeZv01JIRRqI20hVyQIUx0vLjEBp5cC8Bkyl5dZgqv0CQkPCk0jn6tO709bNnSCl5X1zs_kKutk06sA1mRvgOS3vFYON5TepXZ6ucZq2jpTgK2lOqhwATB61ErEpZxpmxlQ2YvASfynn4jRUmV9RJsGWKL1anUH_cqxSkSOY-AHxnMIp9DtsLrA==)
28. [curity.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEuXEBxy7nEqjlFIq-Su4m3I_U4PMx7RNj3rMmRibDeZ8u5CLNZ7-LHKNStpx3xZmddbRhSPJFjvwhCGO-OH-D96kwcdnOhpBEg78vVSscTJBbpoqcJd3316_IsBSjpzxn)
29. [syrenis.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBQgCMxHg1JdnqvzGzb42NqQEBZFIOjVm-UaOX4TUkqKX4bS1C2t8Vv_j58wMNlYvi7tfoXgPKyKpc9HN0veTuoQ76OUjsFT_BmFFDXN0haWh7sipHdVNxo7oLhVkbNJI5PbvxmRP12RKow7U_dy_03_jfGwJMyXA5kg==)
30. [wso2.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEK2SjnMQ7ZKA5On7Xi_9t5U-IPmYMjXtJjLFjt2zL0GQsrecZoL6q99LSx_F9UiHsymfzXHpN_WlrDHgJ6Ksf36jsQdSud-qWT7sPzxxLXfnj2bLJbCiY-iCs8LJ9Gaw8YH5aqGZkGac22CrtM2vpqfCP-ro0MRiYOK6Y=)
31. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvbYN76pts5Y2b_pLoH3e-SfM3GAOL6pPpKkUkM6oREctZB2T-NslVq2XFCViNfFD00xA_WHLbRi_ofUM3yJL120i7DLyyZDT6L3VfRqxsu_KnpicxmM_2VWDJEkTPIsnXz910j2vOsU_KngF1sKbetyO0qPa_IkPMhnvzbCYC20ROf7f3HlwwTZkGeV1QrF2ZfDXd7YDkwAnzApwqyXyX0G1_g1-SanDOTkfkh9F8aUqo)


## Annotations
Annotation(end_index=2474, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGQfIbRhkCmMHBYpPPkige3rko2S8I0NS-toFRwfJGbaH1s357JoKFIIjffFj2wkanAv0iWhK-72cE3o29FjZQeEnpsR-SCNdWI9_fZqY5RYO4zIyosPTHNOZ2o4FUuuJQtreHaS04Rmkj1i1pvzZwgCkqOm4kyybKJXh1tO05igx6LXaNompLNZde4', start_index=2462)
Annotation(end_index=2474, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuWvxl5_Oq1RRuv-f2rHtp394MXwt_LqSOMBWniU78VFyKPrvlT25zp6HQOypJjTbD8YZHBwyQ4_AXFcxq4px8kUoey0cPwEPwOxXUDTemhsHqXC6PwGEGoQD8j_sEkAp5_ZatV8RGnq66E6W7DnLHQQIZMXnO2Vc=', start_index=2462)
Annotation(end_index=2866, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEeOvdScDmIoFYdqEJ7Zt70NIRyV8nmFwszwihjInlqgBlrwl9zY7EJfWa4xo1PBLV7e_HpE6i_WPTybj-693Gxs-Qt_ZZqsNlzhJ37KQzid-i7MgmJiO8RbM72lz6h7YiNdjq8gBhT6G3FWPUncm-a', start_index=2854)
Annotation(end_index=2866, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKofV6Z1eYRtj0PC2MiMLbGpfWrcjW7akRd6EeWzrIxR88O0PG7cuguWomoQ5tG9X1c-oCiKMOpNog0BBvLKDClDRx5zd33Nh9crDxngoENN5yXe4qW-SP-tJ_j2VpoLv7RRzajIkZ_5QCv23JsLUWzkEZHS6TheKL0-Zr5cmjv62-vYNi5EMywM08fS9LqwlBbeVqJX-8HK0E4J5IoOgVwrHD2fyeHx5jwxAXfzF-bg==', start_index=2854)
Annotation(end_index=3086, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFU_p0TPtB_HP2LsW0wyr2X5MLT1lTEtZ-jGT7zDz8AwNTpyRrtSrwCT542B3nwKX0iZ-aBfTpyUHJHbMM8S_xxcZLoUB2hfTNeTECjp4swIKbEmmZXngtw9ubOvfQ9pKBBIOU7qv5KM7tQQUItA_CnwZzWRQpRpRDBuj615ZnZdAQnSiibhE-7wZduGzg8n-o3w-pBirwPqQ==', start_index=3074)
Annotation(end_index=3086, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZn7Bkq_fv14fl_n6H2GCZLhHX0R6oT2EwLuyvBBa7o5vFmlcmh-YouaM2EfuSIdYcbFoxS_Crlsn4rlostLs8P5IOkecJL77ToEwNdwEYsjRR6BlhIbBDNoXrdPIgkxRJiVkHKrGm7LyMszQaQUCe_ry1f7QiQD2KUbryr1pSwqKZ4Uv2RV1h10_evGPkZx8VUZAzThh7I5ZkmI_K2mBH46mQ8zYo-_Kh5Q==', start_index=3074)
Annotation(end_index=3852, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEeOvdScDmIoFYdqEJ7Zt70NIRyV8nmFwszwihjInlqgBlrwl9zY7EJfWa4xo1PBLV7e_HpE6i_WPTybj-693Gxs-Qt_ZZqsNlzhJ37KQzid-i7MgmJiO8RbM72lz6h7YiNdjq8gBhT6G3FWPUncm-a', start_index=3840)
Annotation(end_index=3852, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFM6TUSdMC5_P_rpTIEBcgk9VPEPwpkLTM3-SG9AG2G41rvZfeyLvOeebNA4ZrVKjhMkFvYRhgqzyxHVCO58yW6wrso6PGYpCJlbE4mf8sKe-zvNGn7ZASAauLiHuzZBoNYJ80IpkPVan2xm2L7IMNVI5OiPCAu1D0vTP7ajd44idvGz6cxb9AK73Q5YiQvxDhhlBa3UfMT5_848F4sc8npK0OdpGrrAK3lrsfHO5Mt', start_index=3840)
Annotation(end_index=4225, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbeJbcPEwuo5r-HNEWEqvJsQFRnUOTkRXx2tAwY7QUfRyK55LkFzP_xdP2_mqo1281IDfdH608p2qrji_rg1Pb5wjiNmLNEfTUKQq2yuyBiALTRVOlY2pRSpp8EU36v0xFuBDpiRZqrC9EXJN7Aw==', start_index=4213)
Annotation(end_index=4225, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjOCd9zEF-WsiuhSE7eI_2qERf8CyiJNThCCdTnCT0jYXAI53Urp51DvBctOWIKy4lQn8TcfC2-XrkhC8sjDmY4srbTDPmW6QMa10UfBawqN55LKH7Pn6AMICxbz9B0SLFT_Q4y0mHFo6R5A==', start_index=4213)
Annotation(end_index=4409, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTYLh0jfiNIYbP1Cexasrd4mRfVAZjkDxrntxcmkH8QAm3NKHMt9piJmWP3nfhO387_GWpcwksa47MpAY357q-Zzu53gCLsJfq-HULyawykgiXZJUa3wGaSwjQwza2_rIVlmHnnMU3LLtznA==', start_index=4399)
Annotation(end_index=4773, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnwL8SmZChNr-vhaiVSHii5bRLpc3ouLr53vGFbG3sciIDyiaZQBMUn4FDLKAwvr4FJ18OwzSinHSpfnoAnlZcgqYfMb8hVkpYsMrfC8dhH8j7llBjjKU3nF3XgULJIEmuNHwyDzd_8QxyuSlJ04Ukf27dQO430LmKcfuNE0VB6uFfgXkba3p48jPbLJ0bMi9w8XYMpsxoI1MDQy0f2YoomeAVfS8f44L2Wj81JUQT9I-khQ==', start_index=4759)
Annotation(end_index=4773, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHu16WwmDWYVZDXkLikD8clo0LuYXBpoS_VUSlg4eduCVOpybTJNxMi1PT8SLlOW15jDCC9OyRN-aOA0Ku9tn9_grdidcVHPWUezf3iQxxehDJBsxT6dX0GBqR92TkqmT3dtm5bJkWgKtbwE7fX0l3wqzKZbo8LFWh9onTGsbn7yKIweVe4MvM9W0Y2OJoZMCCgQl9OZ6l4mzYkiGfJdu965nSkDcLI', start_index=4759)
Annotation(end_index=5108, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnwL8SmZChNr-vhaiVSHii5bRLpc3ouLr53vGFbG3sciIDyiaZQBMUn4FDLKAwvr4FJ18OwzSinHSpfnoAnlZcgqYfMb8hVkpYsMrfC8dhH8j7llBjjKU3nF3XgULJIEmuNHwyDzd_8QxyuSlJ04Ukf27dQO430LmKcfuNE0VB6uFfgXkba3p48jPbLJ0bMi9w8XYMpsxoI1MDQy0f2YoomeAVfS8f44L2Wj81JUQT9I-khQ==', start_index=5094)
Annotation(end_index=5108, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHu16WwmDWYVZDXkLikD8clo0LuYXBpoS_VUSlg4eduCVOpybTJNxMi1PT8SLlOW15jDCC9OyRN-aOA0Ku9tn9_grdidcVHPWUezf3iQxxehDJBsxT6dX0GBqR92TkqmT3dtm5bJkWgKtbwE7fX0l3wqzKZbo8LFWh9onTGsbn7yKIweVe4MvM9W0Y2OJoZMCCgQl9OZ6l4mzYkiGfJdu965nSkDcLI', start_index=5094)
Annotation(end_index=6020, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFblqWsU45XPye8BFpgxcS48xHGviT7X4qu1iNhVXlyiWHCe40EOHGyeaG-qcmH31nTHsHgrWhj6Uk-JkNmzqyhVkR9mf3X1ximHKw9hybBtdGcvA6zIaQwkRZrsGfZrJskQJsrd1Hewvvr7xIM0JyHx6barHdde-fq-oJxjk63hJY=', start_index=6006)
Annotation(end_index=6020, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGnwL8SmZChNr-vhaiVSHii5bRLpc3ouLr53vGFbG3sciIDyiaZQBMUn4FDLKAwvr4FJ18OwzSinHSpfnoAnlZcgqYfMb8hVkpYsMrfC8dhH8j7llBjjKU3nF3XgULJIEmuNHwyDzd_8QxyuSlJ04Ukf27dQO430LmKcfuNE0VB6uFfgXkba3p48jPbLJ0bMi9w8XYMpsxoI1MDQy0f2YoomeAVfS8f44L2Wj81JUQT9I-khQ==', start_index=6006)
Annotation(end_index=6253, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLUQS7QkmNbCUDwBBVvKVM24ViLmE4tousosujPOJYgXmqF6LpTXwtB0BXrHr1lh27SRERmuZPzSgy1wCDN0HRygTOUQpUyENGLZFl20SZ98jA3f0QKCd1uChfoBsQloxaD5hdswVYRoBduqYHLFIRqVSicpUjHbj3yUlzq0E=', start_index=6243)
Annotation(end_index=6491, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLUQS7QkmNbCUDwBBVvKVM24ViLmE4tousosujPOJYgXmqF6LpTXwtB0BXrHr1lh27SRERmuZPzSgy1wCDN0HRygTOUQpUyENGLZFl20SZ98jA3f0QKCd1uChfoBsQloxaD5hdswVYRoBduqYHLFIRqVSicpUjHbj3yUlzq0E=', start_index=6481)
Annotation(end_index=6903, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFblqWsU45XPye8BFpgxcS48xHGviT7X4qu1iNhVXlyiWHCe40EOHGyeaG-qcmH31nTHsHgrWhj6Uk-JkNmzqyhVkR9mf3X1ximHKw9hybBtdGcvA6zIaQwkRZrsGfZrJskQJsrd1Hewvvr7xIM0JyHx6barHdde-fq-oJxjk63hJY=', start_index=6889)
Annotation(end_index=6903, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTr3T1WgcqPlL0dTFev_P2DNB3Y11u-u8EgUNvTH0WfEHg5x_p7lwplSey_fifU6MJi53r5RWid2GfjGCDXWvs2tqHQxn1K2cq2SuHlCAugJJjY05uChIMicPhxB_tYGED4Z72qTeT2jkKPGlR8iadn1GIKFJOzep3hm1Zb5prfeq-Md603dVDuESarbjzvCfLr1z6kRzEHKUpkPhqjg==', start_index=6889)
Annotation(end_index=7247, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKGTTng3Fof0UBhXZPzJz5wb6SNz5kzpTS3ayAr0Qi3MMUIcRKD9IX0k8CIBB4qMSoHgcKIuyApOkNjY_cD58t2hZyyU4MHV7Q1Gk93j5JACO2G16te0V9lHzNqouEflRHuGjFnpbrF0lcznMP5SNDR8tD', start_index=7233)
Annotation(end_index=7247, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLUQS7QkmNbCUDwBBVvKVM24ViLmE4tousosujPOJYgXmqF6LpTXwtB0BXrHr1lh27SRERmuZPzSgy1wCDN0HRygTOUQpUyENGLZFl20SZ98jA3f0QKCd1uChfoBsQloxaD5hdswVYRoBduqYHLFIRqVSicpUjHbj3yUlzq0E=', start_index=7233)
Annotation(end_index=7746, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiT0b7bIZBdU3NtF7eQs84Z6nAKY2orp0jv9rWzzvvUtAs1Z8oX-x6MOS0FXxaIfQCL050UTFrvNm78RQqaD7kUpK7MdGeqAAlF8ETpwW0YWizb3z8oXrBI_EhQ-V0m9mxrOyNbSea-4XO_ztBJooTng20maq6-L5lJHelA4Ht5Toa9TWG8htRhC9V3dsa_VcpDFhprW1-54P3aFmHjTYyrzrrbLTasAJ5fF2RN_a4ZkfwXc0eBLkdBMlxT0FC3hz_', start_index=7733)
Annotation(end_index=7746, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKofV6Z1eYRtj0PC2MiMLbGpfWrcjW7akRd6EeWzrIxR88O0PG7cuguWomoQ5tG9X1c-oCiKMOpNog0BBvLKDClDRx5zd33Nh9crDxngoENN5yXe4qW-SP-tJ_j2VpoLv7RRzajIkZ_5QCv23JsLUWzkEZHS6TheKL0-Zr5cmjv62-vYNi5EMywM08fS9LqwlBbeVqJX-8HK0E4J5IoOgVwrHD2fyeHx5jwxAXfzF-bg==', start_index=7733)
Annotation(end_index=7965, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0TmsH-vQxuln28xqs6w2jURwKizUOzrBbDA5Pl4uFMQCIcg_ufY3rRKtulSmCO--5tizAFR3avNIjz3uZLA370LcjcKIc01nT51pYZUxs8hhpr9yY3fjIj-gNAhiXYHpr9MJvNphxu8PBhQk228YBRjRCbEDAxgi64w-oeSPbzrUQPZjq8lSe-ac=', start_index=7955)
Annotation(end_index=8413, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFU_p0TPtB_HP2LsW0wyr2X5MLT1lTEtZ-jGT7zDz8AwNTpyRrtSrwCT542B3nwKX0iZ-aBfTpyUHJHbMM8S_xxcZLoUB2hfTNeTECjp4swIKbEmmZXngtw9ubOvfQ9pKBBIOU7qv5KM7tQQUItA_CnwZzWRQpRpRDBuj615ZnZdAQnSiibhE-7wZduGzg8n-o3w-pBirwPqQ==', start_index=8397)
Annotation(end_index=8413, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKofV6Z1eYRtj0PC2MiMLbGpfWrcjW7akRd6EeWzrIxR88O0PG7cuguWomoQ5tG9X1c-oCiKMOpNog0BBvLKDClDRx5zd33Nh9crDxngoENN5yXe4qW-SP-tJ_j2VpoLv7RRzajIkZ_5QCv23JsLUWzkEZHS6TheKL0-Zr5cmjv62-vYNi5EMywM08fS9LqwlBbeVqJX-8HK0E4J5IoOgVwrHD2fyeHx5jwxAXfzF-bg==', start_index=8397)
Annotation(end_index=8413, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeR8bU4W0RzkG9o7FzLzRBG8JWujknfDeQToqPfuSF3CPSA-IUEzHsFvQxLMG5BHK1ya9Ky_jh8Vkos3feXCGZFLDVwD3YZ4g5KgcVNx42WKABYD6gd8wy9bpco-FjodynoXNcT-O9gfmdGcNwPlZv', start_index=8397)
Annotation(end_index=9139, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKGTTng3Fof0UBhXZPzJz5wb6SNz5kzpTS3ayAr0Qi3MMUIcRKD9IX0k8CIBB4qMSoHgcKIuyApOkNjY_cD58t2hZyyU4MHV7Q1Gk93j5JACO2G16te0V9lHzNqouEflRHuGjFnpbrF0lcznMP5SNDR8tD', start_index=9122)
Annotation(end_index=9139, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuWvxl5_Oq1RRuv-f2rHtp394MXwt_LqSOMBWniU78VFyKPrvlT25zp6HQOypJjTbD8YZHBwyQ4_AXFcxq4px8kUoey0cPwEPwOxXUDTemhsHqXC6PwGEGoQD8j_sEkAp5_ZatV8RGnq66E6W7DnLHQQIZMXnO2Vc=', start_index=9122)
Annotation(end_index=9139, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_RP_nm-DFesiCbduL2xkVQ1ONeUk3kxjuKIHd4m07e8BqsIiSQtnk5WOqP9u9q1mnqidNCEvhTq9CONJhRiY8RaiN-2KjVuw6O4iv_B1DofBt4Pl70l4BD6lFZPpTV_o7DbGELqU4kw==', start_index=9122)
Annotation(end_index=9384, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKGTTng3Fof0UBhXZPzJz5wb6SNz5kzpTS3ayAr0Qi3MMUIcRKD9IX0k8CIBB4qMSoHgcKIuyApOkNjY_cD58t2hZyyU4MHV7Q1Gk93j5JACO2G16te0V9lHzNqouEflRHuGjFnpbrF0lcznMP5SNDR8tD', start_index=9370)
Annotation(end_index=9384, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_RP_nm-DFesiCbduL2xkVQ1ONeUk3kxjuKIHd4m07e8BqsIiSQtnk5WOqP9u9q1mnqidNCEvhTq9CONJhRiY8RaiN-2KjVuw6O4iv_B1DofBt4Pl70l4BD6lFZPpTV_o7DbGELqU4kw==', start_index=9370)
Annotation(end_index=9652, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0aIE_9c9BojL_rEKT6rMO0f-BHfs7FrhGwdfdxILE5rg3HicIhSIPy-jKy1TNPDed0NCBxigouEHQp3k06q_-b_KlkI2iHMSrH9GbziRhuxPdY28XROMKdazFYYy8HqO0R-AYvZx3dFUo9-EMxfpHNArH-jomqBFtN5hJM9l1FoMqI2XlVSM=', start_index=9642)
Annotation(end_index=10377, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7uJ78WNuos5GR7DC-_bDYxDD5JrS1L6Tg9X_v8SmR0bXb97lgYSSjZHbKrJzBIKxCcZemX3cTKn1xipilJ5hLf0B6QyqRh7Ll7JN0KxjtyiPL8kO27EZyf1DrcBo0lB_Hr58CIkN60iIcGBx3E5aP', start_index=10359)
Annotation(end_index=10377, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKGTTng3Fof0UBhXZPzJz5wb6SNz5kzpTS3ayAr0Qi3MMUIcRKD9IX0k8CIBB4qMSoHgcKIuyApOkNjY_cD58t2hZyyU4MHV7Q1Gk93j5JACO2G16te0V9lHzNqouEflRHuGjFnpbrF0lcznMP5SNDR8tD', start_index=10359)
Annotation(end_index=10377, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_RP_nm-DFesiCbduL2xkVQ1ONeUk3kxjuKIHd4m07e8BqsIiSQtnk5WOqP9u9q1mnqidNCEvhTq9CONJhRiY8RaiN-2KjVuw6O4iv_B1DofBt4Pl70l4BD6lFZPpTV_o7DbGELqU4kw==', start_index=10359)
Annotation(end_index=10871, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZM6xOcaJPCbHq2zww1f7zMtI2WpyeFzCQq77QzBq6eOln4yzXUJIFVMWoK-d8qHLjBunC0IV5L06fmzewHdX5q2n6yzieZn79njxWo-T7m5WCgf0otoJeUuEgKKwcoE364JMpZSt8_hJmiGZQBk1t2_EqDajaQ0cxKGoq_1u3nM8z1TYerxclFm17WgZQI3mgb-lO7K_WdnaXUM1YUA==', start_index=10854)
Annotation(end_index=10871, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEeOvdScDmIoFYdqEJ7Zt70NIRyV8nmFwszwihjInlqgBlrwl9zY7EJfWa4xo1PBLV7e_HpE6i_WPTybj-693Gxs-Qt_ZZqsNlzhJ37KQzid-i7MgmJiO8RbM72lz6h7YiNdjq8gBhT6G3FWPUncm-a', start_index=10854)
Annotation(end_index=10871, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKGTTng3Fof0UBhXZPzJz5wb6SNz5kzpTS3ayAr0Qi3MMUIcRKD9IX0k8CIBB4qMSoHgcKIuyApOkNjY_cD58t2hZyyU4MHV7Q1Gk93j5JACO2G16te0V9lHzNqouEflRHuGjFnpbrF0lcznMP5SNDR8tD', start_index=10854)
Annotation(end_index=11445, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFU_p0TPtB_HP2LsW0wyr2X5MLT1lTEtZ-jGT7zDz8AwNTpyRrtSrwCT542B3nwKX0iZ-aBfTpyUHJHbMM8S_xxcZLoUB2hfTNeTECjp4swIKbEmmZXngtw9ubOvfQ9pKBBIOU7qv5KM7tQQUItA_CnwZzWRQpRpRDBuj615ZnZdAQnSiibhE-7wZduGzg8n-o3w-pBirwPqQ==', start_index=11430)
Annotation(end_index=11445, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGKofV6Z1eYRtj0PC2MiMLbGpfWrcjW7akRd6EeWzrIxR88O0PG7cuguWomoQ5tG9X1c-oCiKMOpNog0BBvLKDClDRx5zd33Nh9crDxngoENN5yXe4qW-SP-tJ_j2VpoLv7RRzajIkZ_5QCv23JsLUWzkEZHS6TheKL0-Zr5cmjv62-vYNi5EMywM08fS9LqwlBbeVqJX-8HK0E4J5IoOgVwrHD2fyeHx5jwxAXfzF-bg==', start_index=11430)
Annotation(end_index=11445, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZn7Bkq_fv14fl_n6H2GCZLhHX0R6oT2EwLuyvBBa7o5vFmlcmh-YouaM2EfuSIdYcbFoxS_Crlsn4rlostLs8P5IOkecJL77ToEwNdwEYsjRR6BlhIbBDNoXrdPIgkxRJiVkHKrGm7LyMszQaQUCe_ry1f7QiQD2KUbryr1pSwqKZ4Uv2RV1h10_evGPkZx8VUZAzThh7I5ZkmI_K2mBH46mQ8zYo-_Kh5Q==', start_index=11430)
Annotation(end_index=11734, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZwCNB9l3H_3Ze56HnqVxlpiZz4kpcORboJH7eJdWy9uONgaABhWOgGeI45ggrLhA6TLiaHQIPEUrZZFOSDezuxgN6zm0UW1X_cUyUb5JeLpcH_17wUiJW_tjsc1BL6OU4u9QbwOlWogMTk1RJY87r_CfJ8dLGBBOKUjaSRew1Tu5neb_SgCFa-76pkC2M06JWONuBWp4ZtdIWWzXzn5sMVzJEpOJ5B3XEu7vZtAVnooQKlwKoq1A=', start_index=11721)
Annotation(end_index=11734, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFU_p0TPtB_HP2LsW0wyr2X5MLT1lTEtZ-jGT7zDz8AwNTpyRrtSrwCT542B3nwKX0iZ-aBfTpyUHJHbMM8S_xxcZLoUB2hfTNeTECjp4swIKbEmmZXngtw9ubOvfQ9pKBBIOU7qv5KM7tQQUItA_CnwZzWRQpRpRDBuj615ZnZdAQnSiibhE-7wZduGzg8n-o3w-pBirwPqQ==', start_index=11721)
Annotation(end_index=12463, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFnvgxrGdiSRcHBtI08HSfEIP-cncwShGtiLzACNjcYGPrn-DUE0pdz0BZfaGuHbzC35ZYe2YDAkomEAmt9Be0381aj3gpyI1AjjFwgNYVXh26PQHOubzBlX8P2MpOWLO45g2dwtKkNR9wU377NXChVYmrBvqfTA6UJhrZwBIbxRKsFOrzk0NyK0ed3RT8hT5UeUImzqYHtbtQf2SfE9h_hbU7CLFEkilAl-WqdfVvhw34e__RPVN1gq83iQV0=', start_index=12449)
Annotation(end_index=12463, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEmPsOdhk4gg8RrhCiMULD3t-EQiKeM7cIsvFx2M3zf-s34YZLTJ4l7oW9yool1OOq6pOaXN13fesaefD7MYBmHMhrXazixkLlz1XtIMie5yMAA-wxMXyvTPPeLpXLB_7uxb0aX2S6282bw7DnDh0_ndydn9wrblyQ', start_index=12449)
Annotation(end_index=12822, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZwCNB9l3H_3Ze56HnqVxlpiZz4kpcORboJH7eJdWy9uONgaABhWOgGeI45ggrLhA6TLiaHQIPEUrZZFOSDezuxgN6zm0UW1X_cUyUb5JeLpcH_17wUiJW_tjsc1BL6OU4u9QbwOlWogMTk1RJY87r_CfJ8dLGBBOKUjaSRew1Tu5neb_SgCFa-76pkC2M06JWONuBWp4ZtdIWWzXzn5sMVzJEpOJ5B3XEu7vZtAVnooQKlwKoq1A=', start_index=12809)
Annotation(end_index=12822, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFU_p0TPtB_HP2LsW0wyr2X5MLT1lTEtZ-jGT7zDz8AwNTpyRrtSrwCT542B3nwKX0iZ-aBfTpyUHJHbMM8S_xxcZLoUB2hfTNeTECjp4swIKbEmmZXngtw9ubOvfQ9pKBBIOU7qv5KM7tQQUItA_CnwZzWRQpRpRDBuj615ZnZdAQnSiibhE-7wZduGzg8n-o3w-pBirwPqQ==', start_index=12809)
Annotation(end_index=13280, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0aIE_9c9BojL_rEKT6rMO0f-BHfs7FrhGwdfdxILE5rg3HicIhSIPy-jKy1TNPDed0NCBxigouEHQp3k06q_-b_KlkI2iHMSrH9GbziRhuxPdY28XROMKdazFYYy8HqO0R-AYvZx3dFUo9-EMxfpHNArH-jomqBFtN5hJM9l1FoMqI2XlVSM=', start_index=13262)
Annotation(end_index=13280, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7tdAOeZv01JIRRqI20hVyQIUx0vLjEBp5cC8Bkyl5dZgqv0CQkPCk0jn6tO709bNnSCl5X1zs_kKutk06sA1mRvgOS3vFYON5TepXZ6ucZq2jpTgK2lOqhwATB61ErEpZxpmxlQ2YvASfynn4jRUmV9RJsGWKL1anUH_cqxSkSOY-AHxnMIp9DtsLrA==', start_index=13262)
Annotation(end_index=13280, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEuXEBxy7nEqjlFIq-Su4m3I_U4PMx7RNj3rMmRibDeZ8u5CLNZ7-LHKNStpx3xZmddbRhSPJFjvwhCGO-OH-D96kwcdnOhpBEg78vVSscTJBbpoqcJd3316_IsBSjpzxn', start_index=13262)
Annotation(end_index=13557, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7uJ78WNuos5GR7DC-_bDYxDD5JrS1L6Tg9X_v8SmR0bXb97lgYSSjZHbKrJzBIKxCcZemX3cTKn1xipilJ5hLf0B6QyqRh7Ll7JN0KxjtyiPL8kO27EZyf1DrcBo0lB_Hr58CIkN60iIcGBx3E5aP', start_index=13543)
Annotation(end_index=13557, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKGTTng3Fof0UBhXZPzJz5wb6SNz5kzpTS3ayAr0Qi3MMUIcRKD9IX0k8CIBB4qMSoHgcKIuyApOkNjY_cD58t2hZyyU4MHV7Q1Gk93j5JACO2G16te0V9lHzNqouEflRHuGjFnpbrF0lcznMP5SNDR8tD', start_index=13543)
Annotation(end_index=14277, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEiT0b7bIZBdU3NtF7eQs84Z6nAKY2orp0jv9rWzzvvUtAs1Z8oX-x6MOS0FXxaIfQCL050UTFrvNm78RQqaD7kUpK7MdGeqAAlF8ETpwW0YWizb3z8oXrBI_EhQ-V0m9mxrOyNbSea-4XO_ztBJooTng20maq6-L5lJHelA4Ht5Toa9TWG8htRhC9V3dsa_VcpDFhprW1-54P3aFmHjTYyrzrrbLTasAJ5fF2RN_a4ZkfwXc0eBLkdBMlxT0FC3hz_', start_index=14263)
Annotation(end_index=14277, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBQgCMxHg1JdnqvzGzb42NqQEBZFIOjVm-UaOX4TUkqKX4bS1C2t8Vv_j58wMNlYvi7tfoXgPKyKpc9HN0veTuoQ76OUjsFT_BmFFDXN0haWh7sipHdVNxo7oLhVkbNJI5PbvxmRP12RKow7U_dy_03_jfGwJMyXA5kg==', start_index=14263)
Annotation(end_index=14708, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZwCNB9l3H_3Ze56HnqVxlpiZz4kpcORboJH7eJdWy9uONgaABhWOgGeI45ggrLhA6TLiaHQIPEUrZZFOSDezuxgN6zm0UW1X_cUyUb5JeLpcH_17wUiJW_tjsc1BL6OU4u9QbwOlWogMTk1RJY87r_CfJ8dLGBBOKUjaSRew1Tu5neb_SgCFa-76pkC2M06JWONuBWp4ZtdIWWzXzn5sMVzJEpOJ5B3XEu7vZtAVnooQKlwKoq1A=', start_index=14690)
Annotation(end_index=14708, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKGTTng3Fof0UBhXZPzJz5wb6SNz5kzpTS3ayAr0Qi3MMUIcRKD9IX0k8CIBB4qMSoHgcKIuyApOkNjY_cD58t2hZyyU4MHV7Q1Gk93j5JACO2G16te0V9lHzNqouEflRHuGjFnpbrF0lcznMP5SNDR8tD', start_index=14690)
Annotation(end_index=14708, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_RP_nm-DFesiCbduL2xkVQ1ONeUk3kxjuKIHd4m07e8BqsIiSQtnk5WOqP9u9q1mnqidNCEvhTq9CONJhRiY8RaiN-2KjVuw6O4iv_B1DofBt4Pl70l4BD6lFZPpTV_o7DbGELqU4kw==', start_index=14690)
Annotation(end_index=15323, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEK2SjnMQ7ZKA5On7Xi_9t5U-IPmYMjXtJjLFjt2zL0GQsrecZoL6q99LSx_F9UiHsymfzXHpN_WlrDHgJ6Ksf36jsQdSud-qWT7sPzxxLXfnj2bLJbCiY-iCs8LJ9Gaw8YH5aqGZkGac22CrtM2vpqfCP-ro0MRiYOK6Y=', start_index=15309)
Annotation(end_index=15323, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvbYN76pts5Y2b_pLoH3e-SfM3GAOL6pPpKkUkM6oREctZB2T-NslVq2XFCViNfFD00xA_WHLbRi_ofUM3yJL120i7DLyyZDT6L3VfRqxsu_KnpicxmM_2VWDJEkTPIsnXz910j2vOsU_KngF1sKbetyO0qPa_IkPMhnvzbCYC20ROf7f3HlwwTZkGeV1QrF2ZfDXd7YDkwAnzApwqyXyX0G1_g1-SanDOTkfkh9F8aUqo', start_index=15309)
Annotation(end_index=17542, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKGTTng3Fof0UBhXZPzJz5wb6SNz5kzpTS3ayAr0Qi3MMUIcRKD9IX0k8CIBB4qMSoHgcKIuyApOkNjY_cD58t2hZyyU4MHV7Q1Gk93j5JACO2G16te0V9lHzNqouEflRHuGjFnpbrF0lcznMP5SNDR8tD', start_index=17528)
Annotation(end_index=17542, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_RP_nm-DFesiCbduL2xkVQ1ONeUk3kxjuKIHd4m07e8BqsIiSQtnk5WOqP9u9q1mnqidNCEvhTq9CONJhRiY8RaiN-2KjVuw6O4iv_B1DofBt4Pl70l4BD6lFZPpTV_o7DbGELqU4kw==', start_index=17528)
Annotation(end_index=17784, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZM6xOcaJPCbHq2zww1f7zMtI2WpyeFzCQq77QzBq6eOln4yzXUJIFVMWoK-d8qHLjBunC0IV5L06fmzewHdX5q2n6yzieZn79njxWo-T7m5WCgf0otoJeUuEgKKwcoE364JMpZSt8_hJmiGZQBk1t2_EqDajaQ0cxKGoq_1u3nM8z1TYerxclFm17WgZQI3mgb-lO7K_WdnaXUM1YUA==', start_index=17770)
Annotation(end_index=17784, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKGTTng3Fof0UBhXZPzJz5wb6SNz5kzpTS3ayAr0Qi3MMUIcRKD9IX0k8CIBB4qMSoHgcKIuyApOkNjY_cD58t2hZyyU4MHV7Q1Gk93j5JACO2G16te0V9lHzNqouEflRHuGjFnpbrF0lcznMP5SNDR8tD', start_index=17770)
Annotation(end_index=18012, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKGTTng3Fof0UBhXZPzJz5wb6SNz5kzpTS3ayAr0Qi3MMUIcRKD9IX0k8CIBB4qMSoHgcKIuyApOkNjY_cD58t2hZyyU4MHV7Q1Gk93j5JACO2G16te0V9lHzNqouEflRHuGjFnpbrF0lcznMP5SNDR8tD', start_index=17998)
Annotation(end_index=18012, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLUQS7QkmNbCUDwBBVvKVM24ViLmE4tousosujPOJYgXmqF6LpTXwtB0BXrHr1lh27SRERmuZPzSgy1wCDN0HRygTOUQpUyENGLZFl20SZ98jA3f0QKCd1uChfoBsQloxaD5hdswVYRoBduqYHLFIRqVSicpUjHbj3yUlzq0E=', start_index=17998)
Annotation(end_index=18277, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7uJ78WNuos5GR7DC-_bDYxDD5JrS1L6Tg9X_v8SmR0bXb97lgYSSjZHbKrJzBIKxCcZemX3cTKn1xipilJ5hLf0B6QyqRh7Ll7JN0KxjtyiPL8kO27EZyf1DrcBo0lB_Hr58CIkN60iIcGBx3E5aP', start_index=18263)
Annotation(end_index=18277, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_RP_nm-DFesiCbduL2xkVQ1ONeUk3kxjuKIHd4m07e8BqsIiSQtnk5WOqP9u9q1mnqidNCEvhTq9CONJhRiY8RaiN-2KjVuw6O4iv_B1DofBt4Pl70l4BD6lFZPpTV_o7DbGELqU4kw==', start_index=18263)
Annotation(end_index=18517, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKGTTng3Fof0UBhXZPzJz5wb6SNz5kzpTS3ayAr0Qi3MMUIcRKD9IX0k8CIBB4qMSoHgcKIuyApOkNjY_cD58t2hZyyU4MHV7Q1Gk93j5JACO2G16te0V9lHzNqouEflRHuGjFnpbrF0lcznMP5SNDR8tD', start_index=18503)
Annotation(end_index=18517, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGLUQS7QkmNbCUDwBBVvKVM24ViLmE4tousosujPOJYgXmqF6LpTXwtB0BXrHr1lh27SRERmuZPzSgy1wCDN0HRygTOUQpUyENGLZFl20SZ98jA3f0QKCd1uChfoBsQloxaD5hdswVYRoBduqYHLFIRqVSicpUjHbj3yUlzq0E=', start_index=18503)
Annotation(end_index=18842, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKGTTng3Fof0UBhXZPzJz5wb6SNz5kzpTS3ayAr0Qi3MMUIcRKD9IX0k8CIBB4qMSoHgcKIuyApOkNjY_cD58t2hZyyU4MHV7Q1Gk93j5JACO2G16te0V9lHzNqouEflRHuGjFnpbrF0lcznMP5SNDR8tD', start_index=18829)
Annotation(end_index=18842, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFU_p0TPtB_HP2LsW0wyr2X5MLT1lTEtZ-jGT7zDz8AwNTpyRrtSrwCT542B3nwKX0iZ-aBfTpyUHJHbMM8S_xxcZLoUB2hfTNeTECjp4swIKbEmmZXngtw9ubOvfQ9pKBBIOU7qv5KM7tQQUItA_CnwZzWRQpRpRDBuj615ZnZdAQnSiibhE-7wZduGzg8n-o3w-pBirwPqQ==', start_index=18829)
Annotation(end_index=19053, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKGTTng3Fof0UBhXZPzJz5wb6SNz5kzpTS3ayAr0Qi3MMUIcRKD9IX0k8CIBB4qMSoHgcKIuyApOkNjY_cD58t2hZyyU4MHV7Q1Gk93j5JACO2G16te0V9lHzNqouEflRHuGjFnpbrF0lcznMP5SNDR8tD', start_index=19040)
Annotation(end_index=19053, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFU_p0TPtB_HP2LsW0wyr2X5MLT1lTEtZ-jGT7zDz8AwNTpyRrtSrwCT542B3nwKX0iZ-aBfTpyUHJHbMM8S_xxcZLoUB2hfTNeTECjp4swIKbEmmZXngtw9ubOvfQ9pKBBIOU7qv5KM7tQQUItA_CnwZzWRQpRpRDBuj615ZnZdAQnSiibhE-7wZduGzg8n-o3w-pBirwPqQ==', start_index=19040)
Annotation(end_index=19247, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKGTTng3Fof0UBhXZPzJz5wb6SNz5kzpTS3ayAr0Qi3MMUIcRKD9IX0k8CIBB4qMSoHgcKIuyApOkNjY_cD58t2hZyyU4MHV7Q1Gk93j5JACO2G16te0V9lHzNqouEflRHuGjFnpbrF0lcznMP5SNDR8tD', start_index=19234)
Annotation(end_index=19247, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFU_p0TPtB_HP2LsW0wyr2X5MLT1lTEtZ-jGT7zDz8AwNTpyRrtSrwCT542B3nwKX0iZ-aBfTpyUHJHbMM8S_xxcZLoUB2hfTNeTECjp4swIKbEmmZXngtw9ubOvfQ9pKBBIOU7qv5KM7tQQUItA_CnwZzWRQpRpRDBuj615ZnZdAQnSiibhE-7wZduGzg8n-o3w-pBirwPqQ==', start_index=19234)
Annotation(end_index=19448, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7tdAOeZv01JIRRqI20hVyQIUx0vLjEBp5cC8Bkyl5dZgqv0CQkPCk0jn6tO709bNnSCl5X1zs_kKutk06sA1mRvgOS3vFYON5TepXZ6ucZq2jpTgK2lOqhwATB61ErEpZxpmxlQ2YvASfynn4jRUmV9RJsGWKL1anUH_cqxSkSOY-AHxnMIp9DtsLrA==', start_index=19434)
Annotation(end_index=19448, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEuXEBxy7nEqjlFIq-Su4m3I_U4PMx7RNj3rMmRibDeZ8u5CLNZ7-LHKNStpx3xZmddbRhSPJFjvwhCGO-OH-D96kwcdnOhpBEg78vVSscTJBbpoqcJd3316_IsBSjpzxn', start_index=19434)

## Sources
