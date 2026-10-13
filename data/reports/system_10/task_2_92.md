# Deep Research Report: perplexity/sonar-deep-research
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 351046eb | **Time:** 95.49s | **Cost:** $1.21622
--------------------------------------------------------------------------------

# Understanding Authentication Intensity Hierarchies: Determinants of Account Security Protection Strength

**The authentication intensity hierarchy represents a structured progression of verification methods and security mechanisms that organizations implement to protect digital accounts and systems, with the appropriate level determined by a complex interplay of risk factors, regulatory requirements, user characteristics, and organizational threat models. This report explores the foundational frameworks—including NIST Authenticator Assurance Levels, the Consumer Authentication Strength Maturity Model, and risk-based authentication approaches—along with the critical determinants that guide organizations in selecting the proper authentication strength for their specific security contexts, balancing the competing demands of robust protection and user accessibility.**

## Foundational Frameworks Defining Authentication Intensity Levels

### The NIST Authenticator Assurance Level Framework

The National Institute of Standards and Technology has established a widely-adopted framework through Special Publication 800-63 that defines three distinct Authenticator Assurance Levels (AALs), each representing progressively stronger confidence in user identity verification[6][9][58]. At the foundational level, AAL1 provides basic confidence that a claimant controls an authenticator bound to their account, requiring either single-factor or multi-factor authentication using a diverse range of available authentication technologies[18][19]. Common authenticators at this level include memorized secrets, one-time passwords from devices, or physical authenticators, with the defining characteristic being that a single authentication factor typically suffices, though organizations may encourage users to employ multiple factors even at this level[6][12]. The authentication protocol must be secure, but the diversity of acceptable authenticator types reflects the relative accessibility and lower security requirements of AAL1 applications[18][19].

AAL2 represents a significant step upward in the authentication intensity hierarchy, requiring high confidence that the claimant controls one or more authenticators bound to their subscriber account[9][58]. This level mandates proof of possession and control of two distinct authentication factors through secure authentication protocols, with approved cryptographic techniques becoming a requirement[9][58]. Organizations may satisfy AAL2 through either a multi-factor authenticator—a single device requiring two factors to operate, such as a cryptographic card with an integrated biometric sensor—or through a combination of two independent authenticators, such as a password paired with a hardware token or a physical authenticator combined with biometric verification[6][12]. Importantly, at AAL2 and above, at least one authenticator must be replay-resistant, meaning its output can only be used once for authentication, and at least one should demonstrate authentication intent through the user's deliberate action[9][58]. Federal agencies are now required to offer at least one phishing-resistant authentication option at AAL2, acknowledging the severe threat posed by phishing attacks[9].

AAL3 stands as the highest level in the NIST framework, providing very high confidence that the claimant controls authenticators registered to their account through proof of possession of a key via cryptographic protocol[9][58]. The most significant distinguishing requirement at AAL3 is the mandatory use of hardware-based authenticators that provide verifier impersonation resistance, meaning they cryptographically bind authentication output to a specific authenticated session, preventing phishing attacks even when the user is directed to a fraudulent website[6][9][58]. AAL3 authenticators must use public-key cryptography with non-exportable private keys and must be validated to FIPS 140 Level 1 or higher security standards[9]. Communication between claimant and verifier must occur via authenticated protected channels, and every authentication event at AAL3 must demonstrate authentication intent[9].

### The Consumer Authentication Strength Maturity Model

A complementary framework, the Consumer Authentication Strength Maturity Model (CASMM), provides an eight-level progression designed specifically for everyday internet users and those advising them on security improvements[1]. This model acknowledges that perfect security should not be the enemy of better security, recognizing that even modest improvements in authentication practices provide meaningful protection gains[1][47]. The lower levels of CASMM (Levels 1-3) represent the current state of many non-savvy internet users, characterized by reused passwords, no password managers, and absent multi-factor authentication[1].

The critical transition point in CASMM occurs at Level 4, where users begin adopting a password manager to generate and store unique, strong passwords for their major accounts[1][47]. Research demonstrates that the migration from password-only authentication at Level 3 or below to strong, unique passwords managed at Level 4 provides the single most significant security improvement for average users[1]. The next major advancement occurs between Levels 4 and 5, representing the transition from password-only authentication to multi-factor authentication, which represents an enormous improvement in security posture[1][47].

Importantly, Level 5 in CASMM (text/SMS-based MFA) is deliberately positioned as the weakest form of MFA, recognizing that while it provides protection against credential stuffing and simple password guessing, it remains vulnerable to advanced attacks including SIM swapping and phishing[1]. Levels 6 and 7 represent authentication app-based methods, where no authentication code is transmitted to the user, thus eliminating the phishability of intercepted codes[1]. The uppermost Level 8 achieves authentication through cryptographically secure methods like WebAuthn, where no codes are sent to users and authentication requests are cryptographically bound to specific registered URLs, providing comprehensive phishing resistance[1][47].

## Critical Determinants of Authentication Intensity Selection

### Risk Assessment and Threat Model Definition

The foundational determinant of appropriate authentication intensity is the organization's comprehensive risk assessment, which establishes the threat model specific to the application or system requiring protection[11][22][49]. Organizations must determine the likelihood and impact of different attack scenarios, considering both the probability that an authenticator could be compromised and the consequences of such compromise to the individual, organization, and broader ecosystem[11][22]. The Digital Identity Risk Assessment (DIRA) process, developed collaboratively by NIST and federal agencies, provides structured methodology for this evaluation[11][22].

Within the DIRA framework, organizations identify user groups, transactions, and roles to understand their specific risk environment[11][22]. Different transaction types carry inherently different risk profiles—accessing an informational website presents far lower risk than accessing financial systems or sensitive government information[8][11]. The assessment process explicitly evaluates both the likelihood of attack and the impact of successful compromise, with the resulting impact level determination (low, moderate, or high) driving the initial selection of appropriate authentication assurance levels[11][49].

Importantly, the threat model must consider not only external attackers but also insider threats, careless users, and the organization's existing security capabilities[11][49]. An application protecting sensitive personal information from sophisticated organized crime syndicates faces a fundamentally different threat model than a system protecting public information from casual unauthorized access[49]. The threat model also incorporates assumptions about attacker capabilities and resources, distinguishing between online attacks (where attackers attempt login by guessing) and offline attacks (where attackers have obtained database files and can attempt unlimited verification attempts against password hashes)[9][57].

### Impact Level Assessment and Consequence Evaluation

The potential impact of authentication failure serves as a primary driver of authentication intensity hierarchy decisions[8][11][49]. Organizations evaluate impact across multiple dimensions, including financial impact (direct monetary loss from unauthorized transactions or fraud), operational impact (service disruption or business continuity failure), privacy impact (disclosure of sensitive personal or health information), and reputational impact (damage to brand trust and customer confidence)[8][11][49][53]. The OMB provides specific impact guidance distinguishing low-impact applications (causing minimal harm), moderate-impact applications (causing significant harm or disruption), and high-impact applications (capable of causing severe harm, major incidents, or national security implications)[8][11].

For financial systems, the impact assessment must account for the transaction value and the number of potentially affected users[4][53][56]. A banking application where unauthorized access could result in fraudulent transactions affecting thousands of customers faces substantially higher impact than an internal portal containing routine business communications[11][49]. Healthcare applications present unique impact considerations, where unauthorized access to patient records not only violates privacy but could directly endanger patient safety if clinical decisions are made based on altered records[60]. Government applications handling classified information must assess impact through national security frameworks, recognizing that compromise could affect military operations or intelligence collection[11].

The impact assessment process also considers second-order consequences, such as regulatory fines for compliance failures (HIPAA violations can result in fines exceeding $71,000 per incident; GDPR violations can reach 4% of annual revenue)[37][40], mandatory breach notification requirements and associated costs, and potential criminal liability for individuals responsible for security failures[44]. This comprehensive impact evaluation ensures that authentication intensity requirements reflect genuine business risk rather than arbitrary security preferences[49].

### Regulatory and Compliance Requirements

Regulatory mandates represent explicit determinants of authentication intensity in regulated industries[37][40][61][63]. The Payment Card Industry Data Security Standard (PCI DSS) requires specific access control and authentication measures for anyone handling cardholder data, with version 4.0.1 establishing updated requirements[40]. HIPAA requires healthcare organizations to implement access controls and authentication measures to protect patient health information, with the Security Rule explicitly addressing identification and authentication requirements[37][40][60]. The Health Insurance Portability and Accountability Act's enforcement has resulted in substantial penalties for organizations that failed to implement adequate authentication controls, with these regulatory pressures directly driving adoption of stronger multi-factor authentication[40][60].

Financial regulations including the Sarbanes-Oxley (SOX) Act and the Gramm-Leach-Billey Act (GLBA) do not explicitly mandate specific authentication methods but establish requirements for strong internal controls and safeguards that implicitly necessitate robust authentication[63]. Similarly, the New York Department of Financial Services Cybersecurity Regulation (NYDFS) establishes requirements for financial institutions operating in New York State, including mandatory multifactor authentication for accessing critical systems[37].

Government agencies operate under explicit federal requirements mandating multifactor authentication for accessing federal information systems and personal information[9]. The Cybersecurity Maturity Model Certification (CMMC) framework establishes three levels of cybersecurity requirements for federal contractors, with authentication becoming progressively more stringent as the level increases[40]. International regulations including the General Data Protection Regulation (GDPR) in Europe establish requirements for appropriate technical and organizational measures to protect personal data, which often necessitate authentication strength aligned with NIST AAL2 or higher standards[37][40].

### User Population Characteristics and Capabilities

The technical sophistication, device access, and user preferences of the target population represent important practical determinants of authentication intensity hierarchy implementation[4][36][39][42][45]. An organization cannot practically enforce AAL3 requirements on a population lacking access to hardware security keys or capable devices, nor can it demand authenticator app-based multi-factor authentication from users without smartphones[4][36][42]. The usability research literature demonstrates a clear inverse relationship between authentication complexity and user adoption and compliance rates, with overly stringent requirements leading to workarounds, exception requests, and ultimately reduced security[36][42].

Biometric authentication emerged in usability research as the most preferred authentication method among both novice and experienced users, receiving high satisfaction ratings from diverse user populations due to its balance between ease of use and security[36]. Password-only authentication, while fastest to complete, was perceived as inadequate for protecting sensitive data, while multi-factor authentication offered stronger protection but posed usability challenges, particularly for novice users who experienced higher error rates and longer task completion times[36]. Research on public sector organizations implementing flexible authentication demonstrates that providing users multiple authentication pathway options—such as facial recognition on workstations, external cameras in secure areas, or smartphones—substantially improves both adoption and compliance rates[42].

The authentication intensity hierarchy must therefore accommodate diverse user capabilities while maintaining minimum security requirements[4][36][45]. Organizations increasingly employ adaptive authentication that adjusts requirements based on user context rather than applying uniform policies, recognizing that a trusted user accessing systems from a known device in expected circumstances requires less intensive authentication than an unfamiliar user accessing from unknown locations with untrusted devices[2][4][13]. This contextual approach allows organizations to maintain high security for high-risk scenarios while reducing friction for routine, low-risk access patterns[2][5][13].

### Sensitivity and Criticality of Protected Resources

The criticality and sensitivity of information or systems requiring protection directly determines appropriate authentication intensity[7][8][11][35][49]. Resources containing publicly available information require minimal authentication protection, while systems containing personal identifiable information, financial data, health records, or classified information demand progressively stronger authentication[35][49]. An information portal accessible to the general public might appropriately employ AAL1 authentication with basic password-only login, while the same organization's health record system containing protected health information might require AAL2 with multifactor authentication, and administrative access to core financial systems might require AAL3 with hardware-based cryptographic authentication[8][11][49].

Sensitive data classification frameworks help organizations systematically evaluate resource sensitivity[35]. Public information requires minimal access controls, while internal information intended for organizational use only necessitates moderate authentication. Confidential information where unauthorized access causes business disruption or regulatory implications requires strong authentication controls, and restricted information classified as highly sensitive, containing trade secrets or regulated personal data, demands the most stringent authentication intensity[35][38].

The sensitivity evaluation must also account for temporal factors—data considered public today might become sensitive tomorrow if circumstances change, requiring reassessment of authentication requirements[35][49]. Similarly, the sensitivity of administrative functions must be evaluated separately from data sensitivity; administrative access allowing users to modify security settings or delete records warrants stronger authentication than read-only access regardless of the underlying data sensitivity[49].

### Resource Value and Attacker Motivation

The economic value of protected resources and their attractiveness to potential attackers represents an implicit determinant of authentication intensity hierarchy decisions[1][2][5][13]. Systems containing financial data, high-value intellectual property, or credentials enabling access to valuable systems attract sophisticated, well-resourced attackers willing to invest significant effort in compromise[26][27][28]. Such systems typically require authentication methods resistant to advanced attacks, including phishing, social engineering, and token interception[26][27][28].

Conversely, systems protecting routine operational data of limited intrinsic value may attract only opportunistic attackers employing basic credential stuffing or password spraying attacks[4][26]. These attack patterns can be effectively mitigated by AAL1 authentication with rate limiting and blocklist-based protection against known compromised passwords, without necessitating the complexity and cost of higher assurance levels[4]. This risk-proportionate approach to authentication intensity allocation allows organizations to optimize security investments by concentrating stronger protections where attacker motivation and capability justify such investment[2][5][13].

### Device Trust and Endpoint Security Posture

The trust status of devices accessing protected systems substantially influences required authentication intensity, particularly in organizational contexts where employees access systems from both managed corporate devices and unmanaged personal devices[5][7][10][42][46]. A user accessing email from a corporate laptop provisioned by IT security with current patches, endpoint protection, and configuration management requires less intensive authentication than the same user accessing the system from a personal device of unknown security posture[7][10][46].

Risk-based authentication systems automatically adjust authentication requirements based on device recognition, with known trusted devices potentially satisfying lower authentication intensity requirements while unknown or unmanaged devices trigger elevated authentication challenges[2][5][13]. Microsoft Entra's Conditional Access authentication strengths implement this principle, allowing organizations to require phishing-resistant authentication methods when accessing sensitive resources from unmanaged devices while permitting less intensive authentication from known managed devices[7][10].

Device health signals including operating system patch status, endpoint protection agent status, disk encryption status, and firewall enablement can inform authentication intensity decisions[5][7][10]. Organizations might require AAL1 authentication for compliant managed devices while requiring AAL2 or AAL3 for unmanaged or non-compliant devices accessing the same systems[7][10][46]. This contextual approach encourages device management compliance by making compliant devices more convenient for users while maintaining security for all access patterns[7][10].

### Session Context and Access Location

The geographic location, network characteristics, and session context from which access attempts originate represent dynamic determinants of authentication intensity in modern risk-based authentication systems[2][5][13][46]. A user accessing systems from their regular office location with a known IP address and during business hours represents a lower-risk scenario than access from an unexpected geographic location, particularly if the location is inconsistent with user travel patterns[2][5][13]. Impossible travel scenarios—where a user accesses systems from geographically distant locations with insufficient time for physical travel—represent high-confidence fraud indicators triggering elevated authentication challenges[16][46].

Network characteristic analysis contributes to authentication intensity decisions through examination of IP address reputation, ASN (Autonomous System Number) analysis, WiFi fingerprinting, and VPN usage detection[5][13]. Connections from known anonymizing services, proxy networks, or IP addresses associated with prior fraud attempts typically trigger elevated authentication challenges[26][46]. Risk-based authentication systems maintain historical activity profiles for each user, identifying deviations from established patterns and adjusting authentication intensity accordingly[2][5][13].

Time-of-access analysis also influences authentication intensity, with access outside an individual's normal working hours potentially triggering additional verification[5][13]. A user typically accessing systems between 9 AM and 5 PM weekdays might encounter elevated authentication requirements for 2 AM weekend access attempts, particularly if accessing sensitive resources[5][13]. This temporal analysis, while simple, effectively identifies many compromised account scenarios where attackers operate outside victim working hours[5][13].

### Transaction Sensitivity and High-Value Actions

Within applications providing multiple functions, authentication intensity can be differentiated based on the specific transaction type or action being requested, with higher-risk or higher-value actions triggering step-up authentication requiring additional verification factors[43][46]. A user authenticated with AAL2 credentials for email access might encounter a step-up authentication requirement requesting AAL3-level verification when initiating a high-value fund transfer or accessing sensitive administrative functions[43][46].

Step-up authentication represents a hybrid approach to authentication intensity hierarchy, where the baseline authentication level for system access differs from the authentication intensity required for sensitive operations within that system[43][46]. This architecture maximizes usability by not requiring the highest security levels for routine access while maintaining necessary protection for critical transactions[43][46]. Financial systems commonly employ this approach, allowing users to browse account information with basic multi-factor authentication but requiring additional verification including manager approval workflows for large transfers[43].

### Authentication Factor Strength and Phishing Resistance

The inherent security characteristics of different authentication factors drive authentication intensity hierarchy design, with factors varying dramatically in resistance to common attack patterns[1][26][27][28][30][31]. SMS-based one-time passwords, while providing some protection against credential stuffing, remain vulnerable to phishing attacks where users can be tricked into revealing codes, SIM swapping attacks where attackers transfer phone numbers to attacker-controlled devices, and intercepted message attacks[1][26][27][28].

Phishing-resistant authentication methods including FIDO2 security keys, Windows Hello for Business, and platform credentials employ public-key cryptography to cryptographically bind authentication to specific verified domains, preventing phishing attacks even when users are directed to fraudulent sites[26][27][28][30][31][51]. These methods, defined by NIST as offering verifier impersonation resistance, provide authentication that cannot be fooled through social engineering alone, regardless of attacker sophistication[26][27][31].

Recent research demonstrates sophisticated synchronization between phishing toolkits and live voice-based social engineering (vishing) attacks, where attackers simultaneously control fraudulent web interfaces and call victims, dynamically adapting phishing pages and challenges to match victim security configurations and coaching victims through fraudulent authentication steps[26][27][28]. This evolution in phishing capability has accelerated industry adoption of phishing-resistant authentication as the only reliable defense against coordinated social engineering and technical deception[26][27][28].

## Implementation Patterns: Translating Determinants into Authentication Intensity Decisions

### Impact Level Mapping to Initial Assurance Levels

Organizations systematically translate determinants into specific authentication intensity requirements through standardized mapping processes[11][49]. The NIST framework and Digital Identity Risk Assessment guidance establish explicit mappings between impact levels and authentication assurance levels: low-impact applications typically map to AAL1, moderate-impact applications to AAL2, and high-impact applications to AAL2 or AAL3[8][11][49]. This systematic approach ensures consistent application of authentication intensity principles across diverse applications and user groups[11][49].

The mapping process recognizes that different authentication functions (identity proofing, authentication, and federation) may require different assurance levels for the same application[11][49]. An application might require AAL1 authentication for basic user logins but IAL2 identity proofing (verified identity) when users first establish accounts, recognizing that preventing fraud during enrollment requires more rigorous identity verification than authentication during normal operations[49]. This flexibility enables organizations to implement proportionate security without over-engineering authentication for low-risk functions[49].

### Phased Authentication Intensity Enhancement

Organizations commonly implement authentication intensity hierarchies through phased deployments, beginning with highest-value or highest-risk systems and progressively extending to broader user populations and applications[61][64]. Initial deployment often focuses on administrative accounts and sensitive functions where compromise would cause the greatest harm, recognizing that resource-constrained organizations must prioritize protection[61]. Subsequent waves extend multi-factor authentication to additional user groups, with organizations often beginning with privileged users before mandating requirements for general user populations[61].

This phased approach provides multiple practical advantages including allowing organizations to identify implementation challenges and user support requirements with limited user populations before organization-wide deployment, enabling help desk teams to develop expertise and support procedures, and providing time for users to adapt to new authentication methods[61]. Organizations report that awareness campaigns explaining security benefits and user training on new authentication methods deployed ahead of enforcement significantly improve adoption rates and reduce resistance[61].

### Adaptive Authentication Implementation

Modern implementations increasingly employ adaptive or risk-based authentication approaches that dynamically adjust authentication intensity based on transaction context[2][4][5][13][45][49]. Rather than applying fixed authentication intensity to all users accessing a system, adaptive authentication analyzes multiple contextual signals—user location, device trust, time of access, transaction type, and historical behavior—to calculate real-time risk scores and adjust authentication requirements accordingly[2][4][5][13].

Low-risk scenarios satisfying all contextual indicators (known device, expected location, known user, routine transaction) permit streamlined authentication with minimal friction, potentially requiring only a single authentication factor[2][5][13]. Medium-risk scenarios (unfamiliar device, unexpected location, high-value transaction) trigger elevation to multi-factor authentication[2][5][13]. High-risk scenarios (impossible travel, anomalous behavioral patterns, suspicious transaction characteristics) can trigger step-up authentication requiring the highest available security levels or transaction denial with investigation[2][5][13][46].

Research demonstrates that adaptive authentication significantly improves both security outcomes and user experience by concentrating authentication friction on genuinely risky scenarios while removing unnecessary barriers from routine, low-risk access[2][5][13]. Users experience friction reduction as unnecessary authentication steps disappear from normal workflows, while security improves as attackers encounter elevated barriers precisely when attempting unusual access patterns[2][5][13].

## Balancing Authentication Intensity with Usability and Compliance

### The Security-Usability Tradeoff

The tension between authentication security and usability represents a fundamental constraint in authentication intensity hierarchy design, with overly stringent authentication requirements causing user frustration, abandoned transactions, help desk burden, and creative circumvention attempts that ultimately reduce security[36][39][42][45]. Conversely, excessively relaxed authentication intensity creates genuine security vulnerabilities enabling fraud, unauthorized access, and data breach[4][36][41][56].

Research on authentication user experience demonstrates that the tradeoff between security and usability, while real, is not absolute—well-designed authentication systems can achieve both security and usability through appropriate technology selection and contextual implementation[36][42]. Biometric authentication methods utilizing fingerprint, facial recognition, and behavioral biometrics consistently rank highest in user satisfaction while providing strong security properties[36]. Passkey-based authentication (FIDO2) approaches demonstrate 20% improvement in successful sign-in rates compared to password authentication while simultaneously providing superior security[51][33].

Organizations successfully balancing security and usability often employ multiple authentication pathways, allowing users to select methods matching their circumstances and capabilities[42][45]. Staff might authenticate using facial recognition on workstations, badge-based proximity detection in secure areas, or smartphone-based authentication when working remotely, with the organization maintaining consistent security policies while accommodating diverse user needs[42]. This flexible approach dramatically improves compliance rates and user satisfaction compared to mandated single authentication methods[42].

### Continuous Improvement and Evolution

Authentication intensity hierarchies require ongoing reassessment and evolution in response to changing threat landscapes, technological advancement, and organizational growth[49][61]. Annual reassessment of Digital Identity Risk Assessments ensures that authentication intensity requirements remain aligned with current risk environments, recognizing that new attack techniques, emerging threats to particular industries, or changes in organizational mission and data handling require corresponding adjustments to authentication requirements[11][22][49].

As new authentication technologies emerge providing superior security properties—such as the evolution from SMS-based multi-factor authentication through authenticator apps to phishing-resistant FIDO2 implementations—organizations should progressively upgrade users to more advanced methods[1][9][61]. Regulatory requirements often mandate such evolution, with government agencies now requiring phishing-resistant authentication at AAL2 and higher assurance levels[9].

## Conclusion: Synthesis and Future Directions

The authentication intensity hierarchy emerges from systematic integration of multiple distinct determinants including formal risk assessments, impact level evaluations, regulatory compliance requirements, user population capabilities, resource sensitivity, attacker motivation, device trust status, session context, transaction sensitivity, and authentication factor characteristics. No single factor deterministically establishes required authentication intensity; rather, organizations must holistically consider all relevant factors within their specific context to select proportionate security measures.

NIST's Authenticator Assurance Level framework and the Consumer Authentication Strength Maturity Model provide standardized language and structure for implementing authentication intensity hierarchies, enabling consistent decision-making across diverse applications and populations. The DIRA process operationalizes risk assessment methodology, providing organizations concrete procedures for systematically evaluating impact and selecting appropriate assurance levels. Adaptive authentication approaches represent the modern evolution of authentication intensity concepts, enabling organizations to dynamically adjust security requirements based on real-time contextual signals, optimizing both security and usability.

Organizations successfully implementing authentication intensity hierarchies recognize that authentication security must align with legitimate business requirements and user capabilities rather than pursuing absolute security at all costs[36][42][45][61]. The most secure authentication system remains one that users reliably employ, while the most usable system without adequate security provides false confidence in protection. Future authentication intensity implementations will increasingly employ adaptive approaches, phishing-resistant cryptographic methods, and context-aware authentication adjustments that deliver security appropriate to actual risk while minimizing unnecessary friction, ultimately creating systems that users actively adopt and consistently utilize rather than circumvent or abandon[36][42][45][51].

## Annotations
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The Consumer Authentication Strength Maturity Model (CASMM) V6', 'url': 'https://danielmiessler.com/blog/casmm-consumer-authentication-security-maturity-model'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Risk-based authentication - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Risk-based_authentication'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Advanced Topic: Authenticator Assurance Levels - Beyond Identity', 'url': 'https://www.beyondidentity.com/phishing-101/authenticator-assurance-levels'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Types Of Authentication: Your Network Security Options', 'url': 'https://supertokens.com/blog/types-of-authentication'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Duo Risk-Based Authentication', 'url': 'https://duo.com/docs/risk-based-auth'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Authenticator Assurance Levels - NIST Pages', 'url': 'https://pages.nist.gov/800-63-3-Implementation-Resources/63B/AAL/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Overview of Conditional Access Authentication Strengths', 'url': 'https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Determining your assurance level - Login.gov', 'url': 'https://www.login.gov/partners/determining-your-assurance-level/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Authentication Assurance Levels', 'url': 'https://pages.nist.gov/800-63-4/sp800-63b/aal/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'How Authentication Strengths Work in a Conditional Access Policy', 'url': 'https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strength-how-it-works'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Digital Identity Risk Assessment Playbook - IDManagement.gov', 'url': 'https://www.idmanagement.gov/playbooks/dira/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Authenticator Assurance Levels - NIST Pages', 'url': 'https://pages.nist.gov/800-63-3-Implementation-Resources/63B/AAL/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Risk-Based Authentication: What You Need to Consider | Okta', 'url': 'https://www.okta.com/identity-101/risk-based-authentication/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Authentication - Microsoft Threat Modeling Tool - Azure', 'url': 'https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-authentication'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Assurance Levels Overview and Recommendations', 'url': 'https://www.securetechalliance.org/publications-assurance-levels-overview-and-recommendations/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'What are risk detections? - Microsoft Entra ID Protection', 'url': 'https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Threat Modeling Process - OWASP Foundation', 'url': 'https://owasp.org/www-community/Threat_Modeling_Process'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'NIST Special Publication 800-63-3', 'url': 'https://pages.nist.gov/800-63-3/sp800-63-3.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'NIST Special Publication 800-63-3', 'url': 'https://pages.nist.gov/800-63-3/sp800-63-3.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'NIST Special Publication 800-63-4', 'url': 'https://pages.nist.gov/800-63-4/sp800-63.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Authenticator Assurance Levels - NIST Pages', 'url': 'https://pages.nist.gov/800-63-3-Implementation-Resources/63B/AAL/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Digital Identity Risk Assessment Playbook - IDManagement.gov', 'url': 'https://www.idmanagement.gov/playbooks/dira/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'NIST Special Publication 800-63A', 'url': 'https://pages.nist.gov/800-63-3/sp800-63a.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Understanding Success Criterion 2.2.5: Re-authenticating | WAI - W3C', 'url': 'https://www.w3.org/WAI/WCAG22/Understanding/re-authenticating.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '1Password Adds Second Phishing Defense to Browser Extension', 'url': 'https://www.findarticles.com/1password-adds-second-phishing-defense-to-browser-extension/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Phishing Kits Now Sync With Live Phone Scammers to Defeat Multifactor Authentication', 'url': 'https://thecyberexpress.com/phishing-toolkits-to-defeat-mfa/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'New Phishing Kit As-a-service Attacking Google, Microsoft, and Okta Users', 'url': 'https://cybersecuritynews.com/new-phishing-kit-as-a-service-attacking/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Your MFA is no longer enough: Phishing kits bypass multi-factor authentication', 'url': 'https://www.redhotcyber.com/en/post/your-mfa-is-no-longer-enough-phishing-kits-bypass-multi-factor-authentication/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'New PhaaS Kits Use Voice to Bypass MFA at Google, Microsoft, and Okta', 'url': 'https://gbhackers.com/phaas-kits/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Why Phishing-Resistant MFA Is The Future of Secure Authentication', 'url': 'https://www.tokenring.com/learn/phishing-resistant-mfa'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Advanced Topic: Verifier Impersonation Resistance - Beyond Identity', 'url': 'https://www.beyondidentity.com/phishing-101/verifier-impersonation-resistance'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'What Are the Three Authentication Factors? - Rublon', 'url': 'https://rublon.com/blog/what-are-the-three-authentication-factors/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Get started with a phishing-resistant passwordless authentication ...', 'url': 'https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-plan-prerequisites-phishing-resistant-passwordless-authentication'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Authenticators - NIST Pages', 'url': 'https://pages.nist.gov/800-63-3-Implementation-Resources/63B/Authenticators/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Sensitive Data Classification Explained: A Security and Compliance ...', 'url': 'https://www.forcepoint.com/blog/insights/sensitive-data-classification%E2%80%AF'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Usability and security in online authentication systems', 'url': 'https://www.science-gate.com/IJAAS/Articles/2025/2025-12-06/1021833ijaas202506001.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '2026 Identity & IAM compliance regulations and requirements', 'url': 'https://www.strata.io/blog/governance-standards/guide-compliance-regulations-identity/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Learn about sensitivity labels', 'url': 'https://learn.microsoft.com/en-us/purview/sensitivity-labels'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The Psychology of Security: Why Users Resist Better Authentication', 'url': 'https://guptadeepak.com/the-psychology-of-security-why-users-resist-better-authentication/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The 7 Compliance Standards and Cybersecurity Measures All SMBs ...', 'url': 'https://warrenaverett.com/insights/compliance-standards-and-cybersecurity-measures/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Unauthorized Access: Risks, Cases, and Defenses - Bright Security', 'url': 'https://brightsec.com/blog/unauthorized-access-risks-examples-and-6-defensive-measures/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Security vs Usability: End the Trade-Off - Proximia', 'url': 'https://proximia.com/blog/security-vs-usability-end-the-trade-off/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Flag sensitive transactions for step-up authentication - Okta', 'url': 'https://www.okta.com/sites/default/files/2024-04/Step-up%20Authentication.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'How Does Financial Privacy Impact Unauthorized Access Cases in ...', 'url': 'https://leppardlaw.com/federal/computer-crimes/how-does-financial-privacy-impact-unauthorized-access-cases-in-the-us/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Guide to Authentication Methods & Choosing the Right One', 'url': 'https://www.loginradius.com/blog/identity/how-to-choose-authentication'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Require step-up authentication (authentication context) upon risky ...', 'url': 'https://learn.microsoft.com/en-us/defender-cloud-apps/tutorial-step-up-authentication'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The Consumer Authentication Strength Maturity Model (CASMM) V6', 'url': 'https://danielmiessler.com/blog/casmm-consumer-authentication-security-maturity-model'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'WebAuthn, Passwordless and FIDO2 Explained | Duo Security', 'url': 'https://duo.com/blog/webauthn-passwordless-fido2-explained-componens-passwordless-architecture'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Digital Identity Risk Management - NIST Pages', 'url': 'https://pages.nist.gov/800-63-4/sp800-63/dirm/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Introducing the Identity Maturity Framework - Auth0', 'url': 'https://auth0.com/blog/introducing-the-identity-maturity-framework/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'FIDO Passkeys: Passwordless Authentication', 'url': 'https://fidoalliance.org/passkeys/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '5 Key Steps of Effective Digital Identity Risk Management', 'url': 'https://www.asisonline.org/security-management-magazine/monthly-issues/security-technology/archive/2025/october/five-key-steps-of-effective-digital-identity-risk-management/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Account Takeover Risk Assessment: How It Works & Best Practices', 'url': 'https://seon.io/resources/account-takeover-risk-assessment/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Password strength - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Password_strength'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Authenticator Assurance Levels - NIST Pages', 'url': 'https://pages.nist.gov/800-63-3-Implementation-Resources/63B/AAL/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Account Takeover Scenarios: Is Your Business Prepared?', 'url': 'https://www.arkoselabs.com/blog/account-takeover-scenarios/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Strength of Passwords - NIST Pages', 'url': 'https://pages.nist.gov/800-63-4/sp800-63b/passwords/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Authentication Assurance Levels', 'url': 'https://pages.nist.gov/800-63-4/sp800-63b/aal/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': "Understanding NIST's Authenticator Assurance Levels", 'url': 'https://www.manageengine.com/products/self-service-password/blog/understanding-nists-authenticator-assurance-levels.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'How Industry-Specific IAM Solutions Transform Healthcare - Avatier', 'url': 'https://www.avatier.com/blog/specific-iam-solutions-healthcare/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Steps for effectively deploying multi-factor authentication (MFA)', 'url': 'https://www.cyber.gc.ca/en/guidance/steps-effectively-deploying-multi-factor-authentication-mfa-itsap00105'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'NIST Special Publication 800-63-3', 'url': 'https://pages.nist.gov/800-63-3/sp800-63-3.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Which Industries Require Two-Factor Authentication? - Okta', 'url': 'https://www.okta.com/identity-101/which-industries-require-2fa/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Plan a Microsoft Entra multifactor authentication deployment', 'url': 'https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-getstarted'}}

## Sources
https://danielmiessler.com/blog/casmm-consumer-authentication-security-maturity-model
https://en.wikipedia.org/wiki/Risk-based_authentication
https://www.beyondidentity.com/phishing-101/authenticator-assurance-levels
https://supertokens.com/blog/types-of-authentication
https://duo.com/docs/risk-based-auth
https://pages.nist.gov/800-63-3-Implementation-Resources/63B/AAL/
https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths
https://www.login.gov/partners/determining-your-assurance-level/
https://pages.nist.gov/800-63-4/sp800-63b/aal/
https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strength-how-it-works
https://www.idmanagement.gov/playbooks/dira/
https://pages.nist.gov/800-63-3-Implementation-Resources/63B/AAL/
https://www.okta.com/identity-101/risk-based-authentication/
https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-authentication
https://www.securetechalliance.org/publications-assurance-levels-overview-and-recommendations/
https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks
https://owasp.org/www-community/Threat_Modeling_Process
https://pages.nist.gov/800-63-3/sp800-63-3.html
https://pages.nist.gov/800-63-3/sp800-63-3.html
https://pages.nist.gov/800-63-4/sp800-63.html
https://pages.nist.gov/800-63-3-Implementation-Resources/63B/AAL/
https://www.idmanagement.gov/playbooks/dira/
https://pages.nist.gov/800-63-3/sp800-63a.html
https://www.w3.org/WAI/WCAG22/Understanding/re-authenticating.html
https://www.findarticles.com/1password-adds-second-phishing-defense-to-browser-extension/
https://thecyberexpress.com/phishing-toolkits-to-defeat-mfa/
https://cybersecuritynews.com/new-phishing-kit-as-a-service-attacking/
https://www.redhotcyber.com/en/post/your-mfa-is-no-longer-enough-phishing-kits-bypass-multi-factor-authentication/
https://gbhackers.com/phaas-kits/
https://www.tokenring.com/learn/phishing-resistant-mfa
https://www.beyondidentity.com/phishing-101/verifier-impersonation-resistance
https://rublon.com/blog/what-are-the-three-authentication-factors/
https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-plan-prerequisites-phishing-resistant-passwordless-authentication
https://pages.nist.gov/800-63-3-Implementation-Resources/63B/Authenticators/
https://www.forcepoint.com/blog/insights/sensitive-data-classification%E2%80%AF
https://www.science-gate.com/IJAAS/Articles/2025/2025-12-06/1021833ijaas202506001.pdf
https://www.strata.io/blog/governance-standards/guide-compliance-regulations-identity/
https://learn.microsoft.com/en-us/purview/sensitivity-labels
https://guptadeepak.com/the-psychology-of-security-why-users-resist-better-authentication/
https://warrenaverett.com/insights/compliance-standards-and-cybersecurity-measures/
https://brightsec.com/blog/unauthorized-access-risks-examples-and-6-defensive-measures/
https://proximia.com/blog/security-vs-usability-end-the-trade-off/
https://www.okta.com/sites/default/files/2024-04/Step-up%20Authentication.pdf
https://leppardlaw.com/federal/computer-crimes/how-does-financial-privacy-impact-unauthorized-access-cases-in-the-us/
https://www.loginradius.com/blog/identity/how-to-choose-authentication
https://learn.microsoft.com/en-us/defender-cloud-apps/tutorial-step-up-authentication
https://danielmiessler.com/blog/casmm-consumer-authentication-security-maturity-model
https://duo.com/blog/webauthn-passwordless-fido2-explained-componens-passwordless-architecture
https://pages.nist.gov/800-63-4/sp800-63/dirm/
https://auth0.com/blog/introducing-the-identity-maturity-framework/
https://fidoalliance.org/passkeys/
https://www.asisonline.org/security-management-magazine/monthly-issues/security-technology/archive/2025/october/five-key-steps-of-effective-digital-identity-risk-management/
https://seon.io/resources/account-takeover-risk-assessment/
https://en.wikipedia.org/wiki/Password_strength
https://pages.nist.gov/800-63-3-Implementation-Resources/63B/AAL/
https://www.arkoselabs.com/blog/account-takeover-scenarios/
https://pages.nist.gov/800-63-4/sp800-63b/passwords/
https://pages.nist.gov/800-63-4/sp800-63b/aal/
https://www.manageengine.com/products/self-service-password/blog/understanding-nists-authenticator-assurance-levels.html
https://www.avatier.com/blog/specific-iam-solutions-healthcare/
https://www.cyber.gc.ca/en/guidance/steps-effectively-deploying-multi-factor-authentication-mfa-itsap00105
https://pages.nist.gov/800-63-3/sp800-63-3.html
https://www.okta.com/identity-101/which-industries-require-2fa/
https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-getstarted