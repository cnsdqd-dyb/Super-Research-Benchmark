# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 3/5 | **Run ID:** a62bacce | **Time:** 300.16s | **Cost:** $0.21398
--------------------------------------------------------------------------------

# Do Open Banking API Standards Balance Data Security and Interoperability, or Does OAuth 2.0 Token Management Increase the Risk of Permission Leakage?

## A Technical Security Analysis

---

## Abstract

Open banking API standards represent a fundamental transformation in financial services infrastructure, enabling secure data sharing between financial institutions, third-party providers (TPPs), and consumers. This research report examines the critical question of whether current open banking API frameworks successfully balance the competing demands of data security and interoperability, or whether the predominant OAuth 2.0 token management mechanisms introduce significant risks of permission leakage. Through analysis of regulatory frameworks, technical specifications, and security implementations across multiple jurisdictions—including the European Union's PSD2/NextGenPSD2 standards, the United Kingdom's Open Banking Implementation Entity (OBIE) specifications, and emerging global frameworks—this report provides a comprehensive assessment of the security landscape. The analysis reveals that while modern open banking standards incorporate robust security mechanisms including PKCE (Proof Key for Code Exchange), Token Binding protocols, and Financial-grade API (FAPI) requirements, significant vulnerabilities persist in OAuth 2.0 token management, particularly around authorization code interception, redirect URI manipulation, and third-party risk exposure. The findings indicate that the balance between security and interoperability remains imperfect, with token leakage risks representing a substantial concern that requires ongoing mitigation through enhanced monitoring, governance frameworks, and technical controls.

---

## 1. Introduction

### 1.1 Background and Context

The global open banking ecosystem has experienced unprecedented growth, with API call volumes projected to surge from 137 billion in 2025 to 720 billion globally by 2029, representing a 427% increase that underscores the transformative scale of standardized financial data sharing [1]. This expansion is driven by regulatory mandates and market forces that have fundamentally reshaped how financial institutions, third-party providers, and consumers interact with financial data. The European Union's Payment Services Directive 2 (PSD2), the United Kingdom's Open Banking Implementation Entity standards, and emerging frameworks such as the US Financial Data Exchange (FDX) have created a global infrastructure capable of supporting the next generation of financial services [1].

Open banking API standards are the technical specifications, protocols, and governance frameworks that enable secure, standardized communication between financial institutions, third-party providers, and customers [1]. These standards ensure that different financial systems can interoperate seamlessly, allowing customers to share their financial data with authorized parties and initiate transactions across multiple platforms. However, this increased connectivity and data accessibility introduces substantial security challenges that must be carefully managed to protect sensitive financial information and maintain consumer trust.

### 1.2 Research Objectives

This report addresses the central research question: Do open banking API standards successfully balance data security and interoperability, or does OAuth 2.0 token management increase the risk of permission leakage? To answer this question, the analysis examines several interconnected dimensions. First, it evaluates the technical security mechanisms embedded within major open banking API frameworks, including authentication protocols, authorization flows, and token management practices. Second, it assesses the interoperability implications of security requirements across different regulatory jurisdictions and implementation contexts. Third, it identifies specific vulnerabilities in OAuth 2.0 token management that may lead to permission leakage and data exposure. Finally, it examines governance frameworks, monitoring capabilities, and mitigation strategies that can address identified risks.

### 1.3 Scope and Methodology

This analysis is based on examination of regulatory technical standards, industry specifications, academic research, and security documentation from authoritative sources. The primary frameworks examined include the Berlin Group NextGenPSD2 standard, the UK Open Banking Standard developed by OBIE, the Financial-grade API (FAPI) specifications, and various national implementations of PSD2 requirements. The analysis focuses specifically on OAuth 2.0-based authentication and authorization mechanisms, which form the foundation of most open banking security implementations, while considering the broader ecosystem of complementary security controls and governance requirements.

---

## 2. Open Banking API Standards and Security Architecture

### 2.1 Foundational Security Framework

Open banking API security rests upon a layered architecture that combines transport-layer security, authentication protocols, authorization mechanisms, and ongoing monitoring capabilities. The fundamental security requirements across major frameworks emphasize strict authentication policies using industry standards such as OAuth 2.0, mutual TLS, and other strong protocols to authenticate API users and prevent unauthorized access [2]. This multi-layered approach recognizes that no single security mechanism provides complete protection, and that defense-in-depth strategies are essential for protecting sensitive financial data in distributed architectures.

The Regulatory Technical Standards (RTS) on Strong Customer Authentication (SCA) and Common and Secure Communication (CSC), developed by the European Banking Authority to meet PSD2 objectives, establish baseline security requirements for interfaces provided to Third Party Providers [3]. These requirements mandate that messages exchanged via dedicated interfaces should be structured according to the ISO 20022 standard, though implementation approaches vary significantly across institutions and jurisdictions. The RTS requirements emphasize that banks are free to design their own PSD2-compliant APIs, provided they meet various security requirements and provide free technical documentation to any service provider [4].

### 2.2 OAuth 2.0 Authorization Framework

OAuth 2.0 serves as the primary authorization framework for open banking implementations, providing the mechanism through which third-party applications obtain limited access to user accounts. The authorization code flow, particularly when enhanced with Proof Key for Code Exchange (PKCE), represents the recommended approach for open banking scenarios. In this flow, the authorization code obtained is sent to the token endpoint with a "code verifier," and the Authorization Server compares it with the previously received request code to perform proof of possession of the code verifier by the Data Recipient [5]. This mechanism works as a mitigation because an attacker would not know this one-time key, since it is sent over TLS and cannot be intercepted [5].

The evolution from implicit grant to authorization code flow with PKCE represents a significant security improvement for open banking applications. The implicit grant (response type "token") and other response types causing the authorization server to issue access tokens in the authorization response are vulnerable to access token leakage and access token replay [6]. Moreover, no standardized method for sender-constraining exists to bind access tokens to a specific client when the access tokens are issued in the authorization response, meaning that an attacker can use a leaked or stolen access token at a resource endpoint [6]. The transition away from implicit flows addresses these vulnerabilities but introduces new considerations around token storage and management that must be carefully addressed.

### 2.3 Token Binding and Cryptographic Protections

The Token Binding protocol, as defined in RFC 8471, allows client/server applications to create long-lived, uniquely identifiable TLS bindings spanning multiple TLS sessions and connections [5]. This capability enables applications to cryptographically bind security tokens to the TLS layer, preventing token export and replay attacks. To protect privacy, the Token Binding identifiers are only conveyed over TLS and can be reset by the user at any time [5]. The draft-ietf-oauth-token-binding-08 RFC further defines an implementation of Token Binding for OAuth 2.0 to apply Token Binding to Access Tokens, Authorization Codes, Refresh Tokens, JWT Authorization Grants, and JWT Client Authentication [5].

These cryptographic binding mechanisms provide strong guarantees about token provenance and prevent certain categories of attacks where tokens are intercepted and replayed across different contexts. However, the complexity of implementing Token Binding correctly, combined with limited adoption across some open banking implementations, means that these protections are not universally available. The effectiveness of Token Binding depends on consistent implementation across all components of the authorization infrastructure, including authorization servers, resource servers, and client applications.

### 2.4 Financial-Grade API (FAPI) Requirements

The Financial-grade API (FAPI) specification, developed by the Financial-grade API Working Group of the OpenID Foundation, builds upon OAuth 2.0 and OpenID Connect (OIDC) to define additional technical requirements for the financial industry and other industries that require higher API security [7]. FAPI requirements address gaps in baseline OAuth 2.0 implementations that are insufficient for high-value financial transactions, including requirements for sender-constrained access tokens, explicit audience restrictions, and enhanced client authentication mechanisms.

The UK Open Banking Implementation Entity framework requires the nine largest UK banks (CMA9) to provide standardized APIs for account access and payment initiation, with the UK model emphasizing strong customer authentication (SCA) through OAuth 2.0 and OpenID Connect protocols [1]. This framework has achieved remarkable adoption, with 13.3 million active users as of March 2025, representing a 40% year-over-year increase [1]. The success of the UK implementation demonstrates that robust security requirements can be implemented at scale, though it also highlights the ongoing challenges of maintaining security as ecosystem complexity grows.

---

## 3. OAuth 2.0 Token Management Vulnerabilities

### 3.1 Authorization Code Interception Attacks

One of the most significant vulnerabilities in OAuth 2.0 implementations involves the potential for authorization code interception during the authorization response. Leakage from the OAuth client requires that the client, as a result of a successful authorization request, renders a page that contains links to other pages under the attacker's control and a user clicks on such a link, or includes third-party content such as advertisements in iframes, images, or user-generated content [6]. As soon as the browser navigates to the attacker's page or loads the third-party content, the attacker receives the authorization response URL and can extract the authorization code, state, and potentially the access token [6].

This vulnerability is particularly concerning in open banking contexts where the authorization response may contain sensitive authorization codes that can be exchanged for access tokens with broad permissions. The attack surface is expanded by the complexity of modern web applications that frequently incorporate third-party content, analytics, advertising networks, and social media integrations. Each of these integration points represents a potential vector for authorization code exfiltration if not carefully isolated and controlled.

### 3.2 Redirect URI Manipulation

The validation of redirect URIs represents a critical security control in OAuth 2.0 implementations, but one that introduces significant complexity in open banking scenarios. Clients MUST check that the authorization response was received from the correct issuer by comparing the distinct redirect URI for the issuer to the URI where the authorization response was received on [6]. If there is a mismatch, the client MUST abort the flow [6]. However, this defense builds upon existing OAuth functionality and cannot be used in scenarios where clients only register once for the use of many different issuers, as in some open banking schemes, and due to the tight integration with the client registration, it is harder to deploy automatically [6].

The redirect URI validation challenge is amplified in open banking by the diversity of TPPs seeking access to multiple financial institutions. Each TPP may need to register redirect URIs with numerous authorization servers, creating administrative complexity and potential for misconfiguration. Additionally, the dynamic nature of modern web applications, which may generate redirect URIs programmatically or use universal redirect URIs across multiple applications, complicates the validation process and may introduce vulnerabilities if not implemented correctly.

### 3.3 Token Storage and Management Risks

Once access tokens are obtained through the authorization code flow, they must be stored and managed securely by client applications. The transition from implicit flow to authorization code flow with PKCE does completely protect the application from the attack where an authorization code is stolen in transit back to the application [8]. However, once the JavaScript application has obtained an access token, it will still have to store it somewhere in order to use it, and how it stores the access token will be the same whether the application used the implicit flow or PKCE to obtain it [8]. Applications must ensure they have good Content Security Policy and are aware of any third-party libraries being used [8].

The token storage challenge is particularly acute for mobile and web applications that may have limited options for secure storage. Access tokens stored in local storage or session storage are vulnerable to cross-site scripting (XSS) attacks, while tokens stored in memory may be accessible through browser extensions or other mechanisms. Native applications face different challenges around secure enclave storage and preventing token extraction through reverse engineering. The diversity of client application types in the open banking ecosystem means that security controls must be adapted to each platform while maintaining consistent security properties.

### 3.4 Refresh Token Compromise

Refresh tokens, which enable applications to obtain new access tokens without requiring repeated user authentication, represent a high-value target for attackers. While the implicit flow has always been seen as a compromise compared to the authorization code flow, with the specification providing no mechanism to return a refresh token in the implicit flow as it was seen as too insecure to allow that [8], authorization code flows may issue refresh tokens that provide extended access to user accounts. The compromise of a refresh token can provide attackers with persistent access to financial data until the token is revoked, potentially resulting in significant privacy violations and financial harm.

The risk of refresh token compromise is heightened in open banking scenarios where TPPs may maintain long-lived relationships with users and accumulate refresh tokens across multiple financial institutions. The attack surface for refresh token theft includes network interception, client-side storage vulnerabilities, and server-side breaches. Additionally, the complexity of refresh token revocation across distributed systems means that compromised tokens may remain valid for extended periods even after detection of the compromise.

---

## 4. Interoperability Challenges and Security Trade-offs

### 4.1 Regional Standardization Variations

Open banking is not defined by a single, universal framework; instead, it is a global concept that is interpreted and applied differently across regions [9]. Each jurisdiction establishes its own regulatory structures, technical specifications, and enforcement mechanisms, influenced by local market maturity, consumer protection priorities, and national innovation agendas [9]. This fragmentation creates significant interoperability challenges, as TPPs operating across multiple jurisdictions must implement and maintain compliance with different security requirements, API specifications, and certification processes.

Implementation varies by member state in Europe, with common standards like Berlin Group specs improving interoperability but inconsistencies remaining [9]. The UK CMA9 banks are required to comply with OBIE API specifications with uniform security mandates such as mutual TLS, OAuth 2.0, and OpenID Connect [9]. In Australia, data recipients must undergo rigorous accreditation and demonstrate compliance with API and data handling security requirements [9]. The Middle East models API security frameworks after PSD2 and OBIE standards but adapts them for local context [9]. These variations mean that TPPs cannot implement a single security architecture but must instead maintain multiple implementations adapted to each jurisdiction's requirements.

### 4.2 Security Requirements vs. Developer Experience

The tension between security requirements and developer experience represents a significant challenge for open banking adoption. The challenges of ISO 20022 API development have been highlighted by developers responding to the EBA's draft RTS, who have pointed out that ISO 20022 does not fit well with the mainstream of API development [4]. No open banking APIs currently exposed by the banks directly use ISO 20022 messages or elements, with most existing interfaces being RESTful and using the transport protocol to convey semantic value, while ISO 20022 makes no provision for that [4]. Additionally, most APIs use JSON for syntax of requests and responses, but ISO 20022 currently does not define JSON syntax and is usually implemented in XML [4].

This technical mismatch creates friction in the development process and may lead to security vulnerabilities when developers implement workarounds or custom solutions to address compatibility issues. The basic problem with ISO 20022 is that it allows for any amount of variation and development, with multiple variant forms of a given message such as Payment Initiation requests [4]. This flexibility, while supporting diverse business requirements, complicates security validation and may lead to inconsistent security implementations across the ecosystem.

### 4.3 Third-Party Risk and Ecosystem Complexity

The open banking ecosystem introduces significant third-party risks that affect both security and interoperability. This process poses several security risks, such as data breaches and limited visibility into how consumer data can then be used by the third-party provider [10]. In many cases, these third-parties are not required to comply with the same federal regulations as banks, meaning that they also cannot offer consumers the same level of protection over their data in the instance of a breach [10]. This regulatory asymmetry creates potential security gaps where TPPs may have weaker security controls than the financial institutions they connect to.

The complexity of managing third-party risk is compounded by the interconnected nature of the open banking ecosystem. A TPP may integrate with multiple financial institutions, each with different security requirements and monitoring capabilities. Conversely, a financial institution may need to monitor and manage relationships with hundreds or thousands of TPPs, each with different security postures and risk profiles. This complexity makes it difficult to maintain consistent security standards across the ecosystem and may create vulnerabilities at integration points where different security frameworks intersect.

---

## 5. Empirical Evidence of Security Vulnerabilities

### 5.1 Documented Attack Patterns

Empirical evidence demonstrates that attacks on financial APIs can lead to large-scale privacy violations, compromising personally identifiable information (PII), financial records, and critical infrastructure [11]. These documented attacks highlight the real-world consequences of security vulnerabilities in open banking systems and underscore the importance of robust security controls. The frequency and severity of these attacks indicate that current security measures, while representing significant improvements over legacy systems, remain insufficient to address the full range of threats facing open banking infrastructure.

The attack patterns observed include authorization code interception, token replay attacks, injection attacks, broken object-level authorization (BOLA), and improper authentication [2]. Insufficiently protected APIs can allow attackers to intercept or steal sensitive data, while exploits like BOLA or improper authentication can grant unauthorized parties access to customer accounts or financial systems [2]. These attack vectors exploit both implementation vulnerabilities in individual components and systemic weaknesses in the overall security architecture.

### 5.2 Vulnerability Metrics and Assessment

Security metrics provide quantitative frameworks for assessing the security posture of open banking implementations. The Requirement Metric (RM) is a quantitative measurement of the sum of fulfillment levels for a set of requirements, each weighted according to their security requirement importance [12]. This approach enables organizations to assess their security compliance and identify areas requiring improvement. The Common Vulnerability Scoring System (CVSS) provides a standardized framework for characterizing and prioritizing vulnerabilities based on their severity and potential impact [12].

The application of these metrics to open banking contexts reveals significant variation in security implementation quality across the ecosystem. While some financial institutions and TPPs have implemented robust security controls meeting or exceeding regulatory requirements, others have significant gaps that could be exploited by attackers. The lack of consistent security metrics across jurisdictions and the complexity of assessing security across distributed systems make it difficult to obtain a comprehensive view of ecosystem security posture.

### 5.3 Incident Response and Detection Capabilities

The effectiveness of security controls depends not only on their initial implementation but also on the ability to detect and respond to security incidents. Real-time monitoring solutions that identify irregular API activity or potential abuse before they escalate represent essential components of a comprehensive security strategy [2]. Organizations should consider solutions with code-based and traffic-based discovery and inspection, and external attack surface assessment including domain scanning [2]. These capabilities enable rapid detection of attacks and facilitate timely response to limit potential damage.

The mean time to detect and contain partner-driven abuse without broad customer impact represents a critical metric for open banking security [13]. When these indicators are weak, strategic ambition may still be achievable, but only with different sequencing: narrower initial scopes, stronger platform controls, and targeted capability uplift before ecosystem expansion [13]. This recognition that security capabilities must be developed incrementally alongside ecosystem growth highlights the importance of phased approaches to open banking implementation.

---

## 6. Governance and Compliance Frameworks

### 6.1 Consent Management and Data Minimization

Effective consent management represents a critical control for balancing data security with the interoperability goals of open banking. Banks have an opportunity to improve practices by working alongside regulators to introduce new open banking standards, such as developing new consent management tools that give customers the option to determine which data they would like to share, with whom, and for how long [10]. These tools enable customers to exercise meaningful control over their data while limiting the exposure of sensitive information to authorized recipients.

Data minimization principles complement consent management by ensuring that only the minimum necessary data is shared for each specific purpose. Beyond consent: how data minimization can actually work in open banking requires technical mechanisms that enforce data sharing limits and prevent excessive data collection [14]. The combination of informed consent and technical data minimization provides defense-in-depth against both unauthorized access and inappropriate data use by authorized parties.

### 6.2 API Governance and Inventory Management

Governance frameworks must address the complexity of managing APIs across large financial institutions and TPP ecosystems. Solutions that help with API inventory management, including easily adding newly discovered APIs to inventory, represent essential capabilities [2]. Organizations must incorporate API compliance analysis and better track compliance posture changes via automatic alerts [2]. These governance capabilities enable organizations to maintain visibility into their API landscape and ensure that security controls are consistently applied.

Coverage of standardized security patterns across all exposed APIs and partner types represents a key governance indicator [13]. Consent lifecycle performance, including revocation propagation time and audit evidence completeness, provides insight into the effectiveness of consent management controls [13]. Standards conformance and versioning hygiene, including deprecation compliance and partner upgrade rates, indicate the maturity of the organization's API management practices [13]. These governance metrics enable organizations to assess their readiness for open banking participation and identify areas requiring improvement.

### 6.3 Security KPIs and Monitoring

The top three security KPIs banks should track are: successful authentication of customers, which shows how effective the authentication process is and highlights potential fraud cases; successful authentication of technical-service providers, which allows identification of potential fraud cases and understanding of technical challenges; and the number of fraudulent transactions, which helps banks account for the value saved by understanding how many fraudulent transactions have been stopped [15]. These metrics provide insight into the effectiveness of security controls and enable continuous improvement of security posture.

Monitoring capabilities must extend beyond individual institutions to encompass the broader ecosystem. The number of TPPs within the bank's ecosystem measures how successful the bank has been at attracting PSPs and offering innovative services to customers [16]. The number of TPPs using each API provides insight into which APIs are most common within the ecosystem [16]. The number of transactions generated per TPP gives a view of how valuable each TPP is for generating transactions [16]. These ecosystem-level metrics enable financial institutions to assess the health and security of their open banking programs.

---

## 7. Mitigation Strategies and Best Practices

### 7.1 Enhanced Authentication Controls

Strict authentication policies using industry standards such as OAuth 2.0, mutual TLS, or other strong protocols to authenticate API users and prevent unauthorized access represent foundational security controls [2]. Financial institutions need to place security at the forefront to manage these risks effectively and establish a robust basis for open finance [2]. Stronger encryption, stricter authentication, and more granular access control help protect personal information and limit the potential impact of security breaches.

The implementation of mutual TLS (mTLS) provides strong authentication of both clients and servers, preventing man-in-the-middle attacks and ensuring that API communications are with legitimate parties. Combined with OAuth 2.0 authentication, mTLS creates multiple layers of authentication that significantly increase the difficulty of successful attacks. However, the complexity of managing certificates and the operational overhead of mTLS implementation can be barriers to adoption, particularly for smaller TPPs.

### 7.2 Token Security Enhancements

Organizations should implement Token Binding as defined in RFC 8471 to create long-lived, uniquely identifiable TLS bindings spanning multiple TLS sessions and connections [5]. This cryptographic binding prevents token export and replay attacks by ensuring that tokens can only be used in the context of the specific TLS connection on which they were issued. The privacy protections built into Token Binding, where identifiers are only conveyed over TLS and can be reset by the user at any time, address potential concerns about tracking and surveillance.

Sender-constrained access tokens provide an alternative approach to token security that binds tokens to specific clients without requiring the full complexity of Token Binding. These mechanisms ensure that stolen tokens cannot be used by attackers on different clients, limiting the impact of token theft. The FAPI specification mandates sender-constrained tokens for financial-grade implementations, reflecting the importance of this control for protecting high-value transactions.

### 7.3 Monitoring and Incident Response

Real-time monitoring solutions that identify irregular API activity or potential abuse before they escalate represent essential components of a comprehensive security strategy [2]. Organizations should consider solutions with code-based and traffic-based discovery and inspection, and external attack surface assessment including domain scanning [2]. These capabilities enable rapid detection of attacks and facilitate timely response to limit potential damage.

The number of developers using the sandbox indicates strong developer engagement and a positive experience, which may lead to the introduction of new services to customers [16]. The proportion of developers launching live products improves as technical capabilities, documentation, and integration improve [16]. Understanding how long it takes for the developer community to launch products into the market, often measured as "time to first Hello World," supports security validation by ensuring that developers understand and can correctly implement security requirements [16].

---

## 8. Conclusion

### 8.1 Assessment of Security-Interoperability Balance

The analysis presented in this report reveals that open banking API standards have made substantial progress in balancing data security and interoperability, but significant challenges remain. The adoption of OAuth 2.0 with PKCE, Token Binding protocols, and FAPI requirements represents meaningful advancement over legacy authentication mechanisms. Regional frameworks including the UK OBIE specifications, Berlin Group NextGenPSD2, and national PSD2 implementations have established security baselines that protect consumer data while enabling authorized data sharing.

However, the balance between security and interoperability remains imperfect. The diversity of regulatory requirements across jurisdictions creates complexity that can lead to security gaps, particularly for TPPs operating across multiple markets. The tension between security requirements and developer experience introduces friction that may result in insecure workarounds. The complexity of OAuth 2.0 token management creates multiple attack vectors that, while mitigated by best practices, cannot be completely eliminated.

### 8.2 Token Management Risk Assessment

OAuth 2.0 token management does introduce measurable risks of permission leakage that must be actively managed. Authorization code interception, redirect URI manipulation, token storage vulnerabilities, and refresh token compromise represent concrete attack vectors that have been observed in practice. The empirical evidence of attacks leading to large-scale privacy violations confirms that these are not theoretical risks but real-world concerns requiring ongoing attention.

The good news is that effective mitigation strategies exist for each of these vulnerability categories. Organizations implementing PKCE, Token Binding, sender-constrained tokens, robust redirect URI validation, and secure token storage practices can significantly reduce their risk exposure. The key challenge is ensuring consistent implementation across the diverse components of open banking ecosystems, where security depends on the weakest link in the chain.

### 8.3 Recommendations

Financial institutions and TPPs participating in open banking ecosystems should prioritize several areas for security improvement. First, they should implement authorization code flows with PKCE as the minimum acceptable authentication mechanism, eliminating implicit flows entirely. Second, they should adopt Token Binding or sender-constrained tokens to prevent token replay attacks. Third, they should implement comprehensive monitoring capabilities that enable rapid detection of irregular API activity. Fourth, they should establish robust governance frameworks that maintain visibility into API inventory, consent management, and third-party risk.

Regulators and standards bodies should continue to evolve security requirements to address emerging threats while working toward greater harmonization across jurisdictions. The development of global standards that maintain strong security properties while enabling cross-border interoperability represents a critical priority for the continued growth of open banking. The investment in security infrastructure required to achieve these goals is substantial but necessary to maintain consumer trust and enable the full potential of open financial services.

### 8.4 Future Outlook

The open banking ecosystem will continue to evolve rapidly, with API call volumes projected to grow dramatically over the coming years. This growth will expand the attack surface and increase the potential impact of security vulnerabilities. However, it will also drive investment in security capabilities and create incentives for continued improvement in security practices.

The emergence of open finance, which extends open banking principles to a broader range of financial products and services, will introduce additional complexity and security challenges. The lessons learned from open banking implementation will provide valuable guidance for these expanded initiatives, but will also require adaptation to address new threat vectors and regulatory requirements. The ongoing commitment to security by all ecosystem participants will be essential to realizing the benefits of open finance while protecting consumer interests.

---

## References

[1] Scalable Solutions. "Open Banking API Standards." 2025. https://scalablesolutions.io/blog/posts/open-banking-api-standards

[2] F5. "Securing Open Finance in 2025." https://www.f5.com/company/blog/securing-open-finance-in-2025

[3] OneSpan. "Open Banking APIs Under PSD2." 2019. https://www.onespan.com/sites/default/files/2019-07/OneSpan-Whitepaper-Open-Banking-APIs-Under-PSD2.pdf

[4] Trace Financial. "PSD2 Meets ISO 20022." 2021. https://www.tracefinancial.com/wp-content/uploads/2021/04/PSD2-meets-ISO-20022.pdf

[5] Magendanz. MIT EECS Thesis. 2024. https://dspace.mit.edu/bitstream/handle/1721.1/153900/magendanz-qpm3-meng-eecs-2024-thesis.pdf

[6] IETF. "OAuth 2.0 Security Topics." draft-ietf-oauth-security-topics-29. https://www.ietf.org/archive/id/draft-ietf-oauth-security-topics-29.html

[7] This Week in Fintech. "UK Open Banking API Performance 2021-2022." https://www.thisweekinfintech.com/content/files/finextra-downloads/research/documents/262/uk-open-banking-api-performance-2021-2022.pdf

[8] Okta Developer Blog. "Is the OAuth Implicit Flow Dead?" 2019. https://developer.okta.com/blog/2019/05/01/is-the-oauth-implicit-flow-dead

[9] Wallarm. "Open Banking Regulations and API Security." https://hubspot.wallarm.com/hubfs/Open%20Banking%20Regulations%20and%20API%20Security.pdf

[10] American Bankers Association. "Open Banking: Balancing Risks and Rewards." https://www.aba.com/news-research/analysis-guides/open-banking-balancing-risks-rewards

[11] ScienceDirect. "Privacy Violations in Financial APIs." 2025. https://www.sciencedirect.com/science/article/pii/S1110016825008774

[12] LiU DIVA Portal. "Security Metrics for Open Banking." https://liu.diva-portal.org/smash/get/diva2%3A1974124/FULLTEXT01.pdf

[13] Dunnixer. "API Strategy as a Feasibility Test for Open Banking Data Sharing." https://www.dunnixer.com/insights/information/banking/us/api-strategy-as-a-feasibility-test-for-open-banking-data-sharing

[14] HackerNoon. "Beyond Consent: How Data Minimization Can Actually Work in Open Banking." https://hackernoon.com/beyond-consent-how-data-minimization-can-actually-work-in-open-banking

[15] Accenture Banking Blog. "Open Banking: The Right KPIs for Business Value." https://bankingblog.accenture.com/open-banking-right-kpis-for-business-value

[16] Accenture Banking Blog. "Open Banking KPIs for the Right Ecosystem." https://bankingblog.accenture.com/open-banking-kpis-for-right-ecosystem

## Annotations


## Sources
[1] https://bankingblog.accenture.com/open-banking-kpis-for-right-ecosystem
[2] https://bankingblog.accenture.com/open-banking-right-kpis-for-business-value
[3] https://developer.okta.com/blog/2019/05/01/is-the-oauth-implicit-flow-dead
[4] https://docs.secureauth.com/ciam/en/oauth,-consent,-and-payment-initiation-apis-for-open-banking-compliance.html
[5] https://dspace.mit.edu/bitstream/handle/1721.1/153900/magendanz-qpm3-meng-eecs-2024-thesis.pdf?sequence=1&isAllowed=y
[6] https://duendesoftware.com/learn/7-common-security-pitfalls-oauth-2-0-implementations
[7] https://frontegg.com/blog/oauth-flows
[8] https://hackernoon.com/beyond-consent-how-data-minimization-can-actually-work-in-open-banking
[9] https://hubspot.wallarm.com/hubfs/Open%20Banking%20Regulations%20and%20API%20Security.pdf
[10] https://ideas.repec.org/a/aza/jdb000/y2025v9i4p373-382.html
[11] https://liu.diva-portal.org/smash/get/diva2%3A1974124/FULLTEXT01.pdf
[12] https://papers.ssrn.com/sol3/Delivery.cfm/3403ad99-89df-4170-a467-b785fb885075-MECA.pdf?abstractid=5674650
[13] https://pmc.ncbi.nlm.nih.gov/articles/PMC12453829/
[14] https://portswigger.net/web-security/oauth
[15] https://scalablesolutions.io/blog/posts/open-banking-api-standards
[16] https://www.aba.com/news-research/analysis-guides/open-banking-balancing-risks-rewards
[17] https://www.dunnixer.com/insights/information/banking/us/api-strategy-as-a-feasibility-test-for-open-banking-data-sharing
[18] https://www.f5.com/company/blog/securing-open-finance-in-2025
[19] https://www.ietf.org/archive/id/draft-ietf-oauth-security-topics-29.html
[20] https://www.ijprems.com/ijprems-paper/balancing-innovation-and-security-data-privacy-challenges-in-open-banking-and-api-driven-financial-services
[21] https://www.jbs.cam.ac.uk/wp-content/uploads/2024/11/2024-ccaf-the-global-state-of-open-banking-and-open-finance.pdf
[22] https://www.linkedin.com/pulse/implementing-oauth-20-secure-banking-apis-best-practices-vartul-goyal-gv4zc
[23] https://www.mollie.com/growth/open-banking-vs-psd2-explained
[24] https://www.onespan.com/sites/default/files/2019-07/OneSpan-Whitepaper-Open-Banking-APIs-Under-PSD2.pdf
[25] https://www.sciencedirect.com/science/article/pii/S0048733323000446
[26] https://www.sciencedirect.com/science/article/pii/S1110016825008774
[27] https://www.thisweekinfintech.com/content/files/finextra-downloads/research/documents/262/uk-open-banking-api-performance-2021-2022.pdf
[28] https://www.tracefinancial.com/wp-content/uploads/2021/04/PSD2-meets-ISO-20022.pdf
[29] https://www.usenix.org/system/files/usenixsecurity25-luo-kaixuan.pdf
[30] https://www.w3.org/2020/Talks/ketels-20200402.pdf