# Deep Research Report: grok-4-1-fast-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 7a6d32cf | **Time:** 45.54s | **Cost:** $0.00706
--------------------------------------------------------------------------------

**Qualification requirement standards in merchant onboarding audits—often referred to as merchant underwriting or due diligence—are primarily determined by the rules and guidelines established by major card networks like Visa and Mastercard, with acquirers (banks or payment processors) responsible for implementation and enforcement.[[1]](https://usa.visa.com/content/dam/VCOM/regional/na/us/partner-with-us/documents/visa-payment-facilitator-and-marketplace-risk-guide.pdf)[[2]](https://usa.visa.com/dam/VCOM/download/merchants/visa-acceptance-risk-standards.pdf)[[3]](https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/interlink-operating-regulations.pdf)**

These standards aim to mitigate risks such as fraud, chargebacks, money laundering, and brand damage by ensuring merchants are legitimate, financially stable, compliant, and not engaged in prohibited activities.[[4]](https://www.nmi.com/blog/merchant-underwriting-101-from-the-basics-to-automation)[[2]](https://usa.visa.com/dam/VCOM/download/merchants/visa-acceptance-risk-standards.pdf)

### Key Sources of Standards
1. **Card Network Rules**:
   - **Visa**: Defines explicit "Merchant Qualification Standards" in documents like the Visa Core Rules, Interlink Operating Regulations, Visa Acceptance Risk Standards (VARS), Global Acquiring Risk Standards (GARS), and Payment Facilitator/Marketplace Risk Guide. Acquirers must verify merchants meet these before signing agreements.[[1]](https://usa.visa.com/content/dam/VCOM/regional/na/us/partner-with-us/documents/visa-payment-facilitator-and-marketplace-risk-guide.pdf)[[2]](https://usa.visa.com/dam/VCOM/download/merchants/visa-acceptance-risk-standards.pdf)[[3]](https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/interlink-operating-regulations.pdf)
     - Core criteria include: financial responsibility (e.g., creditworthiness, no undue risk), no harm to the payment system (e.g., no illegal/fraudulent practices), operation in permitted jurisdictions, and accurate outlet/location representation.[[3]](https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/interlink-operating-regulations.pdf)
     - Prohibited/restricted: High-brand risk categories (e.g., telemarketing MCC 5966/5967, betting MCC 7995, crypto MCC 6051), transaction laundering, or entities like outbound telemarketers for payment facilitators.[[1]](https://usa.visa.com/content/dam/VCOM/regional/na/us/partner-with-us/documents/visa-payment-facilitator-and-marketplace-risk-guide.pdf)
   - **Mastercard**: Similar requirements via its rules, compliance programs (e.g., Customer Compliance Program), and monitoring standards, though less explicitly termed "qualification standards." Acquirers must align with Mastercard's risk frameworks, including enhanced monitoring from 2026.[[5]](https://www.mastercard.com/us/en/business/support/rules.html)[[6]](https://g2risksolutions.com/mastercards-new-merchant-monitoring-requirements)

2. **Acquirer Risk Policies**: Acquirers set internal, risk-based thresholds exceeding network minimums, segmenting merchants by risk (low/medium/high) based on factors like MCC, volume, and history. Policies require board approval and periodic review.[[2]](https://usa.visa.com/dam/VCOM/download/merchants/visa-acceptance-risk-standards.pdf)

3. **Regulations and Best Practices**: Influenced by laws (e.g., AML/KYC under BSA, PCI DSS for data security) and tools like sanctions screening or negative files (e.g., Visa's VMSS/TMF, Mastercard equivalents).[[2]](https://usa.visa.com/dam/VCOM/download/merchants/visa-acceptance-risk-standards.pdf)

### How Standards Are Applied in Onboarding Audits
Onboarding audits (underwriting/due diligence) are risk-based processes conducted by acquirers or processors:
- **Data Collection/Verification (KYC/KYB)**: Business docs, principals' IDs, ownership, licenses, URLs, financials.[[2]](https://usa.visa.com/dam/VCOM/download/merchants/visa-acceptance-risk-standards.pdf)
- **Risk Screening**: Check VMSS/MATCH lists, credit reports, sanctions, negative news; site visits for high-risk.[[1]](https://usa.visa.com/content/dam/VCOM/regional/na/us/partner-with-us/documents/visa-payment-facilitator-and-marketplace-risk-guide.pdf)
- **Compliance Checks**: PCI DSS path, correct MCC assignment, no prohibited activities; fraud tools (e.g., velocity checks, AVS).[[2]](https://usa.visa.com/dam/VCOM/download/merchants/visa-acceptance-risk-standards.pdf)
- **Approval**: Automated/manual models; reserves/holds for high-risk; registration for special types (e.g., marketplaces).[[1]](https://usa.visa.com/content/dam/VCOM/regional/na/us/partner-with-us/documents/visa-payment-facilitator-and-marketplace-risk-guide.pdf)

Ongoing audits/monitoring ensure sustained compliance, with termination for violations.[[2]](https://usa.visa.com/dam/VCOM/download/merchants/visa-acceptance-risk-standards.pdf)

These evolve via network updates (e.g., new MCCs, risk programs) and acquirer adaptations to fraud trends.[[7]](https://usa.visa.com/content/dam/VCOM/download/merchants/visa-merchant-data-standards-manual.pdf)

## Annotations (Inline Citations)
Citation [1] (Pos: 334-475): [Web] https://usa.visa.com/content/dam/VCOM/regional/na/us/partner-with-us/documents/visa-payment-facilitator-and-marketplace-risk-guide.pdf
Citation [2] (Pos: 475-565): [Web] https://usa.visa.com/dam/VCOM/download/merchants/visa-acceptance-risk-standards.pdf
Citation [3] (Pos: 565-684): [Web] https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/interlink-operating-regulations.pdf
Citation [4] (Pos: 899-986): [Web] https://www.nmi.com/blog/merchant-underwriting-101-from-the-basics-to-automation
Citation [2] (Pos: 986-1076): [Web] https://usa.visa.com/dam/VCOM/download/merchants/visa-acceptance-risk-standards.pdf
Citation [1] (Pos: 1469-1610): [Web] https://usa.visa.com/content/dam/VCOM/regional/na/us/partner-with-us/documents/visa-payment-facilitator-and-marketplace-risk-guide.pdf
Citation [2] (Pos: 1610-1700): [Web] https://usa.visa.com/dam/VCOM/download/merchants/visa-acceptance-risk-standards.pdf
Citation [3] (Pos: 1700-1819): [Web] https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/interlink-operating-regulations.pdf
Citation [3] (Pos: 2069-2188): [Web] https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/interlink-operating-regulations.pdf
Citation [1] (Pos: 2407-2548): [Web] https://usa.visa.com/content/dam/VCOM/regional/na/us/partner-with-us/documents/visa-payment-facilitator-and-marketplace-risk-guide.pdf
Citation [5] (Pos: 2842-2909): [Web] https://www.mastercard.com/us/en/business/support/rules.html
Citation [6] (Pos: 2909-2992): [Web] https://g2risksolutions.com/mastercards-new-merchant-monitoring-requirements
Citation [2] (Pos: 3246-3336): [Web] https://usa.visa.com/dam/VCOM/download/merchants/visa-acceptance-risk-standards.pdf
Citation [2] (Pos: 3550-3640): [Web] https://usa.visa.com/dam/VCOM/download/merchants/visa-acceptance-risk-standards.pdf
Citation [2] (Pos: 3919-4009): [Web] https://usa.visa.com/dam/VCOM/download/merchants/visa-acceptance-risk-standards.pdf
Citation [1] (Pos: 4124-4265): [Web] https://usa.visa.com/content/dam/VCOM/regional/na/us/partner-with-us/documents/visa-payment-facilitator-and-marketplace-risk-guide.pdf
Citation [2] (Pos: 4396-4486): [Web] https://usa.visa.com/dam/VCOM/download/merchants/visa-acceptance-risk-standards.pdf
Citation [1] (Pos: 4610-4751): [Web] https://usa.visa.com/content/dam/VCOM/regional/na/us/partner-with-us/documents/visa-payment-facilitator-and-marketplace-risk-guide.pdf
Citation [2] (Pos: 4840-4930): [Web] https://usa.visa.com/dam/VCOM/download/merchants/visa-acceptance-risk-standards.pdf
Citation [7] (Pos: 5038-5141): [Web] https://usa.visa.com/content/dam/VCOM/download/merchants/visa-merchant-data-standards-manual.pdf


## Sources
[1] https://pcipolicyportal.com/what-is-pci/merchants
[2] https://www.pcisecuritystandards.org/documents/QSA_Qualification_Requirements_v3_0.pdf
[3] https://usa.visa.com/content/dam/VCOM/regional/na/us/partner-with-us/documents/visa-payment-facilitator-and-marketplace-risk-guide.pdf
[4] https://www.occ.treas.gov/publications-and-resources/publications/comptrollers-handbook/files/merchant-processing/pub-ch-merchant-processing.pdf
[5] https://www.mvsi-onboard.com/blog/understanding-merchant-underwriting-a-guide-for-payment-providers
[6] https://www.zengrc.com/blog/what-are-the-pci-audit-requirements
[7] https://www.mastercard.com/mc_us/wallet/guides/sp/bmu/index.html
[8] https://www.linkedin.com/posts/jackvoice_mastercards-new-merchant-monitoring-requirements-activity-7376217220244246528-yMxl
[9] https://www.mastercard.us/content/dam/public/mastercardcom/na/us/en/documents/mastercard-click-to-pay-program-requirements.pdf
[10] https://www.researchgate.net/publication/397973333_Centralized_Metadata_Management_Practices_for_Merchant_Onboarding_Workflows_in_Mixed_Industry_Settings
[11] https://boxopay.com/blog/acquirer-licensing-process
[12] https://www.nmi.com/blog/merchant-underwriting-101-from-the-basics-to-automation
[13] https://corporate.visa.com/en/supporting-info/security-compliance/merchant-qualifications.html
[14] https://usa.visa.com/content/dam/VCOM/download/merchants/visa-merchant-data-standards-manual.pdf
[15] https://www.mastercardservices.com/en/advisors/payments-consulting/insights/digital-merchant-onboarding
[16] https://www.versapay.com/resources/what-is-merchant-underwriting
[17] https://staxpayments.com/blog/merchant-underwriting
[18] https://cdn2.hubspot.net/hubfs/5419069/FastTransact_February2019/PDF/visa-rules-public-10.2017.pdf
[19] https://usa.visa.com/dam/VCOM/download/merchants/visa-acceptance-risk-standards.pdf?utm_source=chatgpt.com
[20] https://www.npstx.com/scaling-offline-acquiring-the-power-of-managed-merchant-services
[21] https://g2risksolutions.com/mastercards-new-merchant-monitoring-requirements
[22] https://usesmileid.com/blog/merchant-onboarding-guide
[23] https://developer.mastercard.com/open-finance-europe/documentation/unlicensed/use-cases/merchant-onboarding
[24] https://www.scribd.com/document/862497358/To
[25] https://withpersona.com/blog/merchant-onboarding-best-practices
[26] https://www.signzy.com/blogs/end-to-end-guide-to-merchant-credit
[27] https://www.mastercard.com/mc_us/wallet/guides/merchant/sp/merchantbymerchant/index.html
[28] https://corefy.com/blog/merchant-onboarding-explained
[29] https://usa.visa.com/dam/VCOM/download/merchants/visa-acceptance-risk-standards.pdf
[30] https://pciguru.wordpress.com/2019/12/08/are-you-a-level-2-merchant-beware-the-mastercard-trap
[31] https://www.pcisecuritystandards.org/documents/ASV_Qualification_Requirements_v3.0.pdf
[32] https://www.mastercard.com.au/en-au/business/merchants/safety-and-security/security-recommendations/merchants-need-to-know.html
[33] https://merchantpros.ai/merchant-services/underwriting-scanx
[34] https://paydiverse.com/a-step-by-step-guide-on-merchant-account-underwriting-process
[35] https://www.linkedin.com/posts/streampayments_payments-merchantonboarding-compliance-activity-7348614419561480192-AiFU
[36] https://unipaygateway.com/become-a-payment-facilitator
[37] https://optimizedpayments.com/insights/industry-news/what-merchants-need-to-know-about-the-new-visa-mastercard-interchange-settlement
[38] https://chargebacks911.com/glossary/merchant-qualification-standards
[39] https://camspay.com/assets/pdf/camspay-merchant-onboarding-policy-v-1-8.pdf
[40] https://chargeafter.com/chargeafters-lending-hub-embedded-customer-centric-lending
[41] https://www.idfy.com/blog/digital-merchant-onboarding-a-complete-guide-2026
[42] https://durangomerchantservices.com/payment-processing-underwriting-understanding-how-merchants-isos-and-banks-interact
[43] https://www.mastercard.com/us/en/business/support/rules.html
[44] https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/interlink-operating-regulations.pdf
[45] https://s27.q4cdn.com/572064924/files/doc_financials/2023/q4/f9969259-3407-4da0-b900-1bd5ec143135.pdf
[46] https://solidgate.com/glossary/underwriting
[47] https://aerissecure.com/blog/mastercard-requires-qsa-or-isa-for-level-two-merchants
