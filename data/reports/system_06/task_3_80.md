# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 09638f8f | **Time:** 187.06s | **Cost:** $0.08335
--------------------------------------------------------------------------------

# How Qualification Requirement Standards Are Determined in Merchant Onboarding Audits

## Executive Summary

Merchant onboarding audits represent a critical control mechanism within the global payments ecosystem, serving as the primary gatekeeping function through which payment service providers (PSPs) evaluate prospective merchants before establishing business relationships. The determination of qualification requirement standards within these audits is a multifaceted process that integrates regulatory mandates, risk-based assessments, technological capabilities, and industry-specific considerations. This report examines the systematic framework through which qualification standards are established, calibrated, and enforced across the merchant onboarding lifecycle.

The findings indicate that qualification requirement standards are not static thresholds but rather dynamic constructs that evolve in response to regulatory developments, emerging risk vectors, and technological advancements. Modern merchant onboarding increasingly relies on quantitative risk scoring methodologies, automated verification systems, and continuous monitoring frameworks to ensure that qualification standards remain both effective and operationally efficient. The integration of Know Your Customer (KYC), Know Your Business (KYB), and Anti-Money Laundering (AML) protocols forms the foundational architecture upon which qualification determinations are made, while Merchant Category Codes (MCCs) provide the taxonomic framework necessary for consistent classification and risk stratification.

---

## 1. Introduction and Contextual Framework

### 1.1 The Evolution of Merchant Onboarding Standards

The merchant onboarding process has undergone substantial transformation over the past decade, evolving from relatively rudimentary verification procedures to sophisticated, multi-layered compliance frameworks. This evolution reflects the increasing complexity of the global payments landscape, the proliferation of digital commerce channels, and the intensifying regulatory scrutiny surrounding financial crime prevention. Qualification requirement standards—the specific criteria and thresholds that determine whether a prospective merchant meets the minimum requirements for onboarding—must therefore be understood within this broader context of regulatory evolution and operational innovation.

Merchant onboarding constitutes a comprehensive set of processes that payment service providers undertake to vet merchants before doing business with them [1]. The process encompasses multiple dimensions of due diligence, including identity verification, financial assessment, regulatory compliance verification, and ongoing monitoring. The determination of qualification standards within this framework requires careful balancing of multiple competing considerations: regulatory compliance, operational efficiency, risk mitigation, and customer experience. As one industry source notes, the objective is to establish robust defenses against financial crime without impeding legitimate business development [2].

### 1.2 Regulatory Drivers and Compliance Imperatives

The determination of qualification requirement standards is fundamentally shaped by the regulatory environment in which PSPs operate. Different jurisdictions impose varying obligations on payment service providers, creating a complex patchwork of requirements that must be navigated during the onboarding process. In the European Union, for example, regulations such as PSD2 and AMLD6 establish baseline requirements that must be integrated into onboarding workflows [3]. In the United States, FinCEN regulations and state-level money transmission requirements impose additional obligations, while sector-specific frameworks such as the Payment Card Industry Data Security Standard (PCI DSS) provide technical requirements for merchants handling card payments [4].

The regulatory landscape continues to evolve, with jurisdictions worldwide implementing new frameworks and strengthening existing requirements. Australia's ongoing payment system reform exemplifies this trend, establishing new licensing obligations for PSPs under a unified regulatory framework and defining core concepts and activities that fall within the regulated perimeter, including payment initiation, facilitation, and stored-value services [5]. These developments underscore the dynamic nature of qualification requirement standards and the need for PSPs to maintain continuous awareness of regulatory developments.

---

## 2. Regulatory Threshold Determination

### 2.1 Transaction-Based Threshold Frameworks

One of the most visible elements of qualification requirement standards is the establishment of transaction-based thresholds that trigger enhanced verification obligations. These thresholds are typically calibrated based on the perceived risk associated with different transaction types and the regulatory frameworks governing specific payment categories. Recent regulatory updates have demonstrated a trend toward lowering thresholds for certain high-risk transaction categories while maintaining higher thresholds for lower-risk activities.

Current frameworks establish distinct thresholds for different transaction categories. For electronic funds transfers (EFTs), remittances, and virtual currency transfers, identity verification must occur at the $1,000 threshold [6]. This relatively low threshold reflects the heightened regulatory concern surrounding these transaction types, particularly in light of the anonymity features inherent in certain virtual currency systems and the cross-border nature of remittance services. For foreign exchange transactions, cheque cashing, and negotiable instruments, the threshold rises to $3,000, reflecting a somewhat different risk profile [6]. The highest threshold of $10,000 applies to large cash or large virtual currency transactions, with the latter category subject to a 24-hour rule that imposes additional reporting and verification requirements [6].

### 2.2 Beneficiary Verification Requirements

Beyond transaction-based thresholds, qualification requirement standards increasingly incorporate explicit requirements to verify beneficiary identities for specific transaction categories. International EFTs and virtual currency remittances of $1,000 or more now trigger mandatory beneficiary verification obligations [6]. This requirement represents a significant expansion of the traditional focus on originator verification and reflects the growing recognition that the complete transaction chain—from originator to beneficiary—must be scrutinized to effectively prevent financial crime.

The determination of these beneficiary verification requirements follows a risk-based logic that considers factors such as the geographic corridors involved, the nature of the beneficiary institution, and the historical transaction patterns between originators and beneficiaries. Jurisdictions characterized by inadequate AML controls, political instability, or financial opacity raise immediate concerns for compliance officers and typically trigger enhanced verification requirements [7]. The objective is to calibrate due diligence efforts proportionally to risk exposure, neither excessive nor insufficient [7].

### 2.3 Scope Expansion and Category Inclusion

Qualification requirement standards are also determined through the explicit expansion of the categories of entities subject to onboarding requirements. Recent regulatory developments have brought previously ambiguous or excluded categories within the scope of mandatory onboarding procedures. Crowdfunding platforms, transport services, and acquirer services for private ATMs are now explicitly covered under updated frameworks [6]. This expansion reflects the regulatory recognition that these business models can present money laundering vulnerabilities that were not adequately addressed under previous frameworks.

The determination of which categories to include within the onboarding scope follows a systematic assessment of risk factors associated with each category. Industries known for being cash-heavy or vulnerable to money laundering, like casinos, real estate, cryptocurrencies, or adult services, inherently carry higher risk and are therefore subject to more stringent qualification requirements [7]. The expansion of scope thus represents a calibration of the regulatory perimeter to better align with the actual risk landscape.

---

## 3. Risk-Based Classification Systems

### 3.1 The Foundation of Risk Assessment

At the core of qualification requirement standards lies the risk assessment framework through which prospective merchants are evaluated and classified. The determination of qualification standards must therefore begin with an understanding of how risk is conceptualized, measured, and stratified within the onboarding process. Risk assessment in merchant onboarding involves evaluating multiple dimensions of potential exposure, including financial risk, compliance risk, operational risk, and reputational risk.

In order to assess how much risk a merchant might pose, PSPs need to collect various pieces of information and documentation [1]. At a minimum, most PSPs design their merchant onboarding processes to comply with Anti-Money Laundering and Know Your Business laws and regulations. Then, they often layer in additional requirements to account for their own risk tolerance [1]. This layered approach—combining mandatory regulatory requirements with discretionary risk-based enhancements—characterizes the contemporary approach to qualification standard determination.

### 3.2 Quantitative Versus Qualitative Assessment Methodologies

Research indicates significant variation in the methodologies employed for risk classification within merchant onboarding. Studies show that 68% of organizations still use qualitative risk assessments (classified as "high," "medium," or "low") for vendor evaluation, yet these same companies experience 2.3 times more vendor-related incidents than those using quantitative scoring systems [8]. This finding has significant implications for the determination of qualification requirement standards, suggesting that the methodology employed for risk classification directly impacts the effectiveness of the overall onboarding framework.

Companies implementing numerical risk scores reduce vendor onboarding time by 45% while improving risk detection accuracy by 62% [8]. These efficiency and effectiveness gains derive from the greater objectivity and consistency inherent in quantitative methodologies. A global financial services firm discovered this gap when its "low-risk" email marketing vendor suffered a breach, exposing 180,000 customer records. Their qualitative assessment missed the vendor's outdated encryption practices and lack of incident response procedures—issues that would have generated a failing quantitative score of 23/100 [8].

### 3.3 Determinants of Risk Classification

The definition and measurement of risk vary across financial institutions, but several common factors typically inform risk evaluation frameworks [7]. These determinants form the basis upon which qualification requirement standards are calibrated for different merchant categories.

**Geographical considerations** represent a primary determinant of risk classification. A client's location and operational territories significantly influence risk categorization [7]. Jurisdictions characterized by inadequate AML controls, political instability, or financial opacity raise immediate concerns for compliance officers and typically trigger enhanced qualification requirements. The determination of geographic risk factors incorporates assessments of regulatory quality, enforcement intensity, and the overall integrity of the financial system in the merchant's operating jurisdictions.

**Customer type** constitutes another critical determinant. Certain client categories inherently demand heightened attention, including politically exposed persons (PEPs), non-resident entities, organizations with intricate ownership structures, and shell companies with limited operational footprints [7]. For each of these categories, qualification requirement standards are calibrated to reflect the elevated risk profile and the corresponding need for enhanced due diligence.

**Nature of business** provides a third determinant, with industries known for elevated risk profiles subject to more stringent qualification requirements. The determination of business-related risk factors considers factors such as the cash-intensity of the business model, the complexity of the supply chain, the regulatory environment governing the specific industry, and the historical association of the industry with financial crime.

---

## 4. Verification and Due Diligence Protocols

### 4.1 Multi-Type Verification Frameworks

The determination of qualification requirement standards extends beyond the classification of risk categories to encompass the specific verification protocols employed during the onboarding process. Best practices in merchant onboarding emphasize the importance of leveraging multiple types of verification when designing KYB and KYC processes [1]. This multi-type approach typically involves a combination of document verification, database verification, and government ID verification, with the specific combination calibrated to the risk profile of the prospective merchant.

When designing KYB and KYC processes, it is usually a good idea to leverage multiple types of verification—this will surface more risk signals to help determine whether the PSP should do business with a merchant [1]. The multi-type approach enables PSPs to cross-validate information from independent sources, increasing confidence in the accuracy of the verification results and reducing the likelihood that fraudulent or misleading information will go undetected.

### 4.2 Financial History and Credit Assessment

Another critical element of qualification requirement standards involves the assessment of merchant financial history. During this step, the PSP typically conducts credit checks on the business as well as all ultimate beneficial owners (UBOs) and key stakeholders [1]. The PSP also reviews the merchant's payment processing history to get a sense of typical transaction volumes and chargeback rates, analyzing the merchant's financial statements to determine whether the business is on solid footing or at risk of failure [1].

The determination of qualification standards related to financial history assessment considers multiple factors, including the merchant's credit score and credit history, the stability and consistency of transaction volumes, the nature and frequency of chargebacks, and the overall financial health of the business as reflected in financial statements. Merchants with concerning financial histories may be subject to enhanced monitoring requirements, collateral requirements, or outright rejection depending on the severity of the risk indicators identified.

### 4.3 Enhanced Due Diligence for High-Risk Categories

For merchants classified as high-risk, qualification requirement standards typically mandate enhanced due diligence (EDD) procedures that go beyond the standard verification protocols. High-risk relationships require enhanced due diligence, including an intensified monitoring regime [7]. The objective is to ensure that the additional risk associated with these relationships is adequately mitigated through more comprehensive verification and ongoing oversight.

The determination of when EDD is required follows a graduated approach based on the merchant's risk classification. Low-risk clients can proceed through streamlined onboarding protocols. Medium-risk clients typically require additional documentation and verification steps. High-risk relationships require enhanced due diligence [7]. This graduated approach ensures that compliance resources concentrate where they deliver maximum protective value, without creating unnecessary friction for lower-risk users.

---

## 5. Merchant Category Code Integration

### 5.1 The Role of MCCs in Qualification Standards

Merchant Category Codes (MCCs) play a central role in the determination of qualification requirement standards, providing a standardized taxonomy through which merchants are classified for purposes of risk assessment, fee calculation, and regulatory compliance. MCCs are four-digit numbers assigned to merchants based on their primary business type, transaction nature, and services provided [9]. These codes adhere to ISO standards, which offer a consistent list of MCCs along with their corresponding descriptions [9].

The assignment of MCCs directly influences qualification requirement standards in multiple ways. First, MCCs determine the regulatory requirements applicable to specific merchant categories, with certain MCCs associated with enhanced reporting or verification obligations. Second, MCCs influence the risk profile assigned to merchants, with high-risk MCCs triggering enhanced due diligence requirements. Third, MCCs affect the fee structure and interchange qualifications applicable to merchant transactions [10].

### 5.2 MCC Assignment and Classification Challenges

The determination of appropriate MCCs for merchants with complex business models presents significant challenges for qualification standard implementation. Merchants with multiple lines of business in the same location must use separate MCCs for each distinct business area, with each business having its business name and type clearly shown to customers and each business having its own points of sale [11]. This requirement ensures that transactions are accurately categorized based on the specific goods or services provided.

For electronic commerce merchants, the MCC assignment becomes particularly complex when merchants operate multiple websites offering distinct goods or services. In such cases, each website must be assigned its own Merchant Category Code based on the specific goods or services offered [11]. The determination of appropriate MCCs in these scenarios requires careful analysis of the merchant's business model and the specific products or services offered through each channel.

### 5.3 MCC-Driven Risk Stratification

The integration of MCCs into qualification requirement standards enables PSPs to implement risk-based stratification at the category level. Some business types may need to pay more to payment processors, while others might be allowed to charge customers for using certain payment forms [10]. These differential treatments reflect the underlying risk profiles associated with different MCC categories and the corresponding cost of providing payment processing services.

The determination of risk-based qualification standards by MCC category considers factors such as the historical chargeback rates associated with each category, the regulatory scrutiny applicable to the category, the complexity of the merchant's business model, and the prevalence of fraud within the category. High-risk MCCs may be subject to enhanced qualification requirements, including additional documentation requirements, higher reserve requirements, or more intensive ongoing monitoring.

---

## 6. Technological Enablers and Automation

### 6.1 Digital-Native Onboarding Infrastructure

The determination of qualification requirement standards increasingly incorporates considerations of technological feasibility and operational efficiency. Digital-native onboarding has emerged as a natural fit for compliance-era requirements, offering capabilities that align well with the documentation and verification demands of modern regulatory frameworks [12]. The ability to produce timestamped logs of every decision, maintain evidence trails for compliance audits, enforce consent gating for data flows, and apply role-based access and minimization controls makes digital-native platforms particularly well-suited to complex qualification requirements [12].

Manual onboarding processes are often time-consuming, error-prone, and costly. Automation reduces these inefficiencies by offering a faster, smoother, and more reliable experience for both merchants and PSPs [3]. The determination of qualification requirement standards must therefore consider the capabilities of available technological infrastructure and the extent to which automation can be leveraged to implement complex verification requirements efficiently.

### 6.2 Real-Time Verification and Pre-Validation

The evolution of qualification requirement standards has been accompanied by the development of real-time verification capabilities that enable immediate assessment of merchant eligibility. The integration of pre-validation APIs for real-time payment checks represents a significant advancement in this direction [5]. These capabilities enable PSPs to verify merchant qualifications at the point of transaction initiation, rather than relying solely on batch processes that may introduce delays and gaps in verification coverage.

The determination of qualification standards for real-time verification requires careful calibration to balance thoroughness with speed. The objective is to implement sufficient verification to maintain compliance with regulatory requirements while avoiding delays that could impair the merchant experience or create operational bottlenecks. This balance is achieved through risk-based approaches that apply more intensive verification to higher-risk transactions while enabling streamlined processing for lower-risk categories.

### 6.3 Continuous Monitoring and Dynamic Reassessment

Qualification requirement standards are not limited to the initial onboarding assessment but extend throughout the merchant relationship through continuous monitoring and dynamic reassessment. A merchant's risk posture evolves over time, and platforms must maintain engagement and transparency to ensure long-term compliance and stability [13]. This ongoing monitoring ensures that qualification standards remain relevant as merchant risk profiles change and new risk factors emerge.

Real-time monitoring flags anomalies and irregular patterns that may indicate financial crime [12]. The determination of qualification standards for ongoing monitoring considers factors such as the expected transaction behavior for the merchant category, the historical patterns established during the initial onboarding period, and the emerging risk indicators that may signal changes in the merchant's risk profile. Deviations from established patterns may signal suspicious behavior warranting investigation [7].

---

## 7. Regulatory Alignment and International Standards

### 7.1 Harmonization with Global Frameworks

The determination of qualification requirement standards increasingly reflects the influence of international regulatory frameworks and the push toward global harmonization. The Financial Action Task Force (FATF) Travel Rule and Financial Stability Board (FSB) level-playing-field guidance represent key reference points for PSPs operating across multiple jurisdictions [5]. The alignment of domestic qualification standards with these international frameworks enables more consistent treatment of merchants across jurisdictions and reduces the compliance burden for PSPs operating internationally.

The implementation of harmonized ISO 20022 messaging standards represents another dimension of international alignment [5]. These standards provide a common framework for the exchange of payment-related information, enabling more consistent verification and due diligence procedures across different payment systems and jurisdictions. The determination of qualification requirement standards must therefore consider not only domestic regulatory requirements but also the international frameworks that influence the broader payments ecosystem.

### 7.2 Cross-Sectoral Considerations

The determination of qualification requirement standards must also consider the broader context of cross-sectoral financial regulation and the potential for regulatory arbitrage across different sectors. The IOSCO research on cross-sectoral capital requirements highlights the importance of understanding how different regulatory frameworks interact and how businesses may structure their activities to optimize across regulatory boundaries [14]. While merchant onboarding is not directly addressed in this research, the underlying principles of regulatory consistency and level playing fields are highly relevant.

The determination of qualification requirement standards must consider whether the standards create appropriate incentives for risk management and compliance across different merchant categories and business models. If qualification standards are significantly more stringent for certain categories, merchants may have incentives to structure their activities to fall within less stringent categories, potentially undermining the effectiveness of the overall framework.

---

## 8. Documentation, Audit Trails, and Compliance Evidence

### 8.1 Evidence Requirements for Qualification Determinations

The determination of qualification requirement standards must be supported by comprehensive documentation and audit trail capabilities. Compliance reporting and regulatory conformance require that suspicious transaction reports, risk logs, and AML records are maintained for audits and regulators [12]. The ability to demonstrate that appropriate qualification procedures were followed and that qualification decisions were based on adequate evidence is essential for regulatory compliance and for defending against potential challenges.

Maintaining organized records is extremely important when onboarding new merchants and throughout their tenure [15]. With appropriate systems, these documents—and everything else that needs to be kept on file—are easily accessible by compliance teams, auditors, and regulators. The determination of qualification requirement standards must therefore consider the documentation requirements that will apply to each element of the qualification process and ensure that systems are in place to capture and retain the necessary evidence.

### 8.2 Audit Readiness and Continuous Improvement

The effectiveness of qualification requirement standards depends not only on their initial determination but also on ongoing assessment and improvement. One of the best ways to ensure compliance is to complete regular audits of processes [15]. At least once or twice per year, compliance teams should review the onboarding process to ensure it remains compliant and to prepare ahead of time for any changing laws or regulations [15].

The determination of qualification requirement standards should therefore incorporate mechanisms for ongoing review and improvement. These mechanisms should include regular audits of the qualification process, analysis of outcomes to identify potential gaps or inefficiencies, and updates to qualification standards in response to regulatory changes, emerging risks, and operational experience. Completing these audits helps protect the organization from potential legal repercussions while ensuring that qualification standards remain effective and current [15].

---

## 9. Conclusion

The determination of qualification requirement standards in merchant onboarding audits represents a complex, multi-dimensional challenge that requires integration of regulatory requirements, risk assessment methodologies, technological capabilities, and operational considerations. These standards are not static thresholds but dynamic constructs that must evolve in response to changes in the regulatory environment, emerging risk vectors, and technological capabilities.

The analysis presented in this report reveals several key principles that should guide the determination of qualification requirement standards. First, standards should be risk-based, with more stringent requirements applied to higher-risk merchant categories and transaction types. Second, standards should incorporate multiple verification types to ensure robust validation of merchant information. Third, standards should leverage quantitative methodologies where possible to improve consistency and effectiveness. Fourth, standards should be supported by comprehensive documentation and audit trail capabilities. Fifth, standards should be subject to ongoing review and improvement to ensure continued effectiveness.

The integration of MCC-based classification, real-time verification capabilities, and continuous monitoring frameworks provides the technological infrastructure necessary to implement complex qualification requirements efficiently. However, the effectiveness of these systems ultimately depends on the quality of the underlying qualification standards and the rigor with which they are applied. As the regulatory environment continues to evolve and new risk factors emerge, PSPs must maintain continuous attention to the determination and implementation of qualification requirement standards to ensure ongoing compliance and effective risk management.

---

## References

[1] Persona. "Best practices for merchant onboarding." December 2024. https://withpersona.com/blog/merchant-onboarding-best-practices/

[2] Dotfile. "Risk evaluation in client onboarding: A guide for payment institutions." https://www.dotfile.com/blog-articles/risk-evaluation-in-client-onboarding-a-guide-for-payment-institutions

[3] Smile ID. "Merchant onboarding guide." https://usesmileid.com/blog/merchant-onboarding-guide

[4] Fonepay. "Merchant Onboarding Best Practices." https://fonepay.com/files/publications/1752402123_MerchantOnboardingBestPractices.pdf

[5] MVSI-Onboard. "Merchant onboarding global updates - October 2025." https://www.mvsi-onboard.com/blog/merchant-onboarding-global-updates---october-2025

[6] MVSI/WDZC. "Merchant onboarding global updates - September 2025." https://www.linkedin.com/pulse/merchant-onboarding-global-updates-september-2025-mvsi-wdszc

[7] Dotfile. "Risk evaluation in client onboarding: A guide for payment institutions." https://www.dotfile.com/blog-articles/risk-evaluation-in-client-onboarding-a-guide-for-payment-institutions

[8] DSAlta. "Vendor risk scoring - September 2025." https://www.dsalta.com/resources/articles/vendor-risk-scoring-september-2025

[9] Fonepay. "Merchant Onboarding Best Practices." https://fonepay.com/files/publications/1752402123_MerchantOnboardingBestPractices.pdf

[10] Revolv3. "A comprehensive guide to merchant category codes (MCC)." https://www.revolv3.com/resources/a-comprehensive-guide-to-merchant-category-codes-mcc

[11] Visa. "Visa merchant data standards manual." https://usa.visa.com/content/dam/VCOM/download/merchants/visa-merchant-data-standards-manual.pdf

[12] Idfy. "Digital merchant onboarding: A complete guide - 2026." https://www.idfy.com/blog/digital-merchant-onboarding-a-complete-guide-2026/

[13] Idfy. "Digital merchant onboarding: A complete guide - 2026." https://www.idfy.com/blog/digital-merchant-onboarding-a-complete-guide-2026/

[14] IOSCO. "Joint Forum paper on capital adequacy." https://www.iosco.org/library/pubdocs/pdf/IOSCOPD215.pdf

[15] ClearCompany. "Best practices for onboarding compliance." https://blog.clearcompany.com/best-practices-for-onboarding-compliance

## Annotations


## Sources
[1] http://www.dotfile.com/blog-articles/risk-evaluation-in-client-onboarding-a-guide-for-payment-institutions
[2] https://blog.clearcompany.com/best-practices-for-onboarding-compliance
[3] https://censinet.com/perspectives/ultimate-guide-to-vendor-risk-scoring-2025
[4] https://corefy.com/blog/merchant-onboarding-explained
[5] https://fonepay.com/files/publications/1752402123_MerchantOnboardingBestPractices.pdf
[6] https://getsiteware.com/onboarding-site-teams-best-practices-for-audit-adoption/
[7] https://stripe.com/resources/more/merchant-onboarding-explained
[8] https://usa.visa.com/content/dam/VCOM/download/merchants/visa-merchant-data-standards-manual.pdf
[9] https://usa.visa.com/content/dam/VCOM/regional/na/us/partner-with-us/documents/visa-payment-facilitator-and-marketplace-risk-guide.pdf
[10] https://usesmileid.com/blog/merchant-onboarding-guide
[11] https://withpersona.com/blog/merchant-onboarding-best-practices/
[12] https://www.atlassystems.com/blog/vendor-onboarding
[13] https://www.chargebackgurus.com/blog/merchant-discount-rate
[14] https://www.dsalta.com/resources/articles/vendor-risk-scoring-september-2025
[15] https://www.flagright.com/post/how-to-do-risk-scoring
[16] https://www.getkard.com/blog/demystifying-merchant-categorization
[17] https://www.idfy.com/blog/digital-merchant-onboarding-a-complete-guide-2026/
[18] https://www.iosco.org/library/pubdocs/pdf/IOSCOPD215.pdf
[19] https://www.linkedin.com/pulse/merchant-onboarding-global-updates-september-2025-mvsi-wdszc
[20] https://www.middesk.com/blog/merchant-onboarding-best-practices
[21] https://www.mvsi-onboard.com/blog/merchant-onboarding-global-updates---october-2025
[22] https://www.occ.treas.gov/publications-and-resources/publications/comptrollers-handbook/files/merchant-processing/pub-ch-merchant-processing.pdf
[23] https://www.onblick.com/blogs/avoid-onboarding-mistakes-that-lead-to-legal-issues
[24] https://www.proteus.co/insights/view/1898-audit-your-b2b-customer-onboarding
[25] https://www.revolv3.com/resources/a-comprehensive-guide-to-merchant-category-codes-mcc
[26] https://www.usecollect.com/blog/10-steps-for-standardizing-client-onboarding