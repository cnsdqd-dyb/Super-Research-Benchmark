# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 34f5ebfd | **Time:** 357.23s | **Cost:** $0.03495
--------------------------------------------------------------------------------

# Do CBDC Smart Contract Policy Tools Balance Money Supply Control and Risk Isolation, or Does Programmable Money Logic Risk Amplifying Policy Accidents?

## Executive Summary

Central Bank Digital Currencies represent a fundamental transformation in monetary infrastructure, introducing programmability as a defining characteristic that distinguishes digital fiat from physical cash. This capability enables sophisticated policy tools through smart contracts, allowing central banks and governments to implement targeted interventions with unprecedented precision. However, the integration of programmable logic into monetary systems raises profound questions about the equilibrium between enhanced policy control and systemic risk exposure.

This analysis examines whether CBDC smart contract capabilities achieve a sustainable balance between money supply management and risk isolation, or whether the inherent logic of programmable money creates conditions that could amplify policy errors. The evidence suggests that programmability offers substantial benefits for targeted policy implementation, including automated compliance, real-time monitoring, and enhanced transmission of monetary impulses. Yet these advantages are counterbalanced by significant operational risks, privacy concerns, and the potential for cascading failures when programmed logic encounters unprecedented economic conditions.

The central finding is that programmability itself is neither inherently stabilizing nor destabilizing—its impact depends critically on design choices, governance frameworks, and the degree to which monetary authorities maintain flexibility in policy execution. The most prudent approach involves treating programmability as a policy tool rather than a fundamental redesign of monetary architecture, ensuring that money retains its fungible character while leveraging smart contracts for specific, bounded objectives such as welfare distribution and compliance automation.

---

## 1. Introduction

The emergence of Central Bank Digital Currencies marks a pivotal moment in the evolution of monetary systems. Unlike traditional forms of central bank money—physical cash and commercial bank reserves—CBDCs introduce a new dimension to legal tender: programmability. This capability, enabled by underlying distributed ledger technology or centralized digital infrastructure, allows monetary authorities to embed logic into transactions, creating what practitioners term "programmable money" or "smart contracts on central bank money" [1][2].

The implications of this technological advancement extend far beyond mere digitization of existing monetary forms. Programmability transforms money from a passive medium of exchange into an active instrument capable of enforcing conditions, automating compliance, and executing policy directives without intermediary intervention. This shift fundamentally alters the relationship between monetary authorities, financial institutions, and end-users, creating both unprecedented opportunities for policy effectiveness and novel vectors for systemic risk.

The central question this report addresses concerns the equilibrium between control and risk. On one hand, programmable CBDCs offer central banks enhanced tools for money supply management, allowing precise targeting of monetary impulses and sophisticated implementation of capital flow management measures. On the other hand, embedding policy logic into the monetary infrastructure creates dependencies, vulnerabilities, and potential amplification mechanisms that could transform localized policy errors into systemic disruptions [3][4].

This analysis proceeds through several interconnected dimensions. First, it examines the theoretical and practical foundations of CBDC programmability, establishing the technical and economic parameters within which smart contract capabilities operate. Second, it evaluates the mechanisms through which programmability enhances money supply control, including targeted distribution, automated compliance, and real-time policy transmission. Third, it analyzes the risk isolation challenges posed by programmable money, examining operational, systemic, and governance vulnerabilities. Fourth, it investigates the conditions under which programmable logic might amplify policy accidents, creating cascading failures across the financial system. Finally, it synthesizes these analyses to identify design principles and governance frameworks that optimize the balance between control and safety.

---

## 2. The Architecture of Programmable CBDC Money

### 2.1 Technical Foundations and Design Options

The programmability of CBDCs derives from the underlying technology infrastructure, which may be based on distributed ledger technology or conventional centralized systems. The Bank for International Settlements distinguishes between "programmable platforms"—technology-agnostic systems that include a Turing machine with an execution environment and ledger—and "smart contracts," which are self-executing applications that trigger actions when pre-specified conditions are met [5]. This technical distinction carries significant policy implications, as the choice of infrastructure determines the range of possible programmable features and the associated risk profile.

Digital wallets serve as the primary interface between users and programmable CBDC functionality. These "smart wallets," typically implemented as smartphone applications, provide secure storage for central bank-issued digital tokens while offering enhanced features including conditional payment execution, identity verification, and policy compliance automation [1]. The wallet architecture determines where programmability logic resides—whether in the central bank infrastructure, the wallet application, or distributed across multiple nodes—and this distribution of functionality has direct implications for resilience, privacy, and control.

A crucial design consideration concerns the relationship between CBDC and programmability. As the Bank for International Settlements explicitly notes, "A CBDC does not necessarily equal programmable money. This would be a policy/design choice to be made by each jurisdiction" [5]. This distinction is fundamental to understanding the risk profile of programmable CBDCs. Jurisdictions may choose to implement CBDCs with minimal programmability, preserving the unconditional nature of legal tender, or they may embrace comprehensive programmable features that embed policy logic throughout the monetary infrastructure.

### 2.2 The Fungibility Question

The fungibility of money—its property of being interchangeable such that any unit is equivalent to any other—represents a foundational principle of monetary systems. Physical cash embodies this property inherently: a ten-dollar bill is functionally identical to any other ten-dollar bill, regardless of its transaction history or the characteristics of its previous holders. This fungibility provides privacy, prevents discrimination, and ensures that money can circulate freely without tracking or restriction.

Programmable CBDCs introduce complexity to this established principle. When money carries embedded logic—restrictions on use, conditions on transfer, or requirements for compliance—the resulting tokens are no longer perfectly fungible. A CBDC unit programmed for energy subsidies cannot be used for general purchases, creating distinct categories of money with different properties and restrictions. This raises fundamental questions about the nature of legal tender and the rights of money holders.

The International Monetary Fund addresses this challenge by distinguishing between "programmability of CBDC transactions" and "programmability of CBDC itself," arguing that "money must remain fungible" [3]. Under this framework, programmability operates at the transaction level rather than the token level, allowing conditions to be attached to specific payments without creating distinct categories of money. This design choice preserves fungibility while enabling targeted policy implementation—a balance that appears essential for maintaining the fundamental properties of money while leveraging programmable capabilities.

---

## 3. Programmable Money as a Policy Tool: Enhancing Money Supply Control

### 3.1 Targeted Monetary Policy Implementation

The programmability of CBDCs offers central banks unprecedented precision in implementing monetary policy. Traditional monetary transmission operates through indirect mechanisms: central banks adjust policy rates, which influence commercial bank behavior, which in turn affects lending, spending, and investment decisions by households and businesses. This chain of transmission is subject to frictions, lags, and leakage that can dilute policy effectiveness.

Programmable CBDCs enable a more direct transmission of monetary impulses. Central banks can set interest rates on CBDC holdings, vary the supply of CBDCs under specific conditions, or implement targeted stimulus programs that direct funds toward particular sectors or purposes [6]. The World Economic Forum notes that CBDCs could be used as tools to achieve policy objectives including "improved safety and resilience in payments systems; increased efficiency, access and competitiveness of payments systems; better data transmission and reporting to central banks; and financial inclusion" [7].

Direct-to-person payments represent a particularly powerful application of programmable policy. Government authorities could use CBDC programmability to issue energy subsidies, activate rights to childcare services, or implement conditional cash transfer programs with automated eligibility verification and compliance monitoring [1]. This capability transforms social welfare distribution from a complex, multi-step process involving multiple intermediaries into a direct, automated mechanism that reduces leakage, lowers transaction costs, and accelerates the delivery of public benefits.

### 3.2 Automated Compliance and Capital Flow Management

Capital flow management measures (CFMs) represent another domain where CBDC programmability offers significant advantages. The International Monetary Fund argues that "the digitalization of information and programmability of transactions—leading to the automation of compliance checks—could bring efficiency gains compared to today's implementation of CFMs" [3]. By embedding compliance logic into the payment infrastructure, jurisdictions can implement capital restrictions with greater precision and lower administrative burden.

The Bank for International Settlements describes how "control measures that restrict the circulation of CBDC under certain conditions can be programmed into the technology or a payments platform" [5]. These tools could enable central banks to broaden access to digital currency while mitigating macro-financial vulnerabilities. A design option proposed involves "embed[ding] policy measures (eg capital flow management, macroprudential, AML/CFT) into smart contracts governing CBDC in a common protocol layer," which could "ease the general policy and regulatory compliance burden by automating compliance procedures, providing real-time transaction monitoring, and increasing transparency and visibility around country-specific policies" [5].

This automation provides both efficiency and effectiveness benefits. Real-time monitoring enables immediate detection of policy violations, while automated enforcement ensures consistent application of regulatory requirements. The reduction in human intervention decreases opportunities for corruption and error while accelerating the pace at which compliance can be verified and enforced.

### 3.3 Sustainability and Behavioral Policy Tools

Programmable CBDCs enable novel approaches to behavioral policy, particularly in domains such as environmental sustainability. The German Institute for Economic Research describes how "CBDC smart wallets could be used to promote policies that help meet sustainability objectives, e.g. by issuing a 'green' wallet that would be a stimulus for consumers to buy environmentally friendly products and services" [1]. This application represents a fundamental shift from incentive-based to architecture-based behavioral policy.

Rather than relying on tax incentives or subsidies that require recipients to take additional actions, programmable money embeds behavioral guidance directly into the payment medium. A "green" wallet could automatically restrict or discourage purchases of carbon-intensive products while facilitating transactions in environmentally friendly categories. While such mechanisms raise significant autonomy concerns, they also demonstrate the potential for programmability to achieve policy objectives with unprecedented precision and directness.

---

## 4. Risk Isolation Challenges in Programmable CBDC Systems

### 4.1 Operational and Technical Vulnerabilities

The introduction of programmability into monetary systems expands the attack surface and creates novel operational risks. The Bank for International Settlements' Consultative Group on Risk Management identified multiple categories of risk associated with CBDC issuance, many of which are amplified by programmability features [2]. Technology failures at the hardware, software, network, or consensus layers can affect CBDC operation and availability, leading to legal and reputational impacts for central banks. Implementation, operation, or maintenance mistakes may lead to incorrect balances or missed payments, creating potential for fraud and economic loss.

The complexity of programmable systems creates particular challenges for risk management. Smart contracts, while automated, require precise specification of conditions and logic that must account for all possible states and contingencies. Errors in contract specification can lead to unintended behavior that may be difficult to reverse once deployed. The immutable nature of some distributed ledger implementations means that programming errors cannot be corrected without significant intervention, potentially locking in flawed policy logic indefinitely.

Cyber security risks represent a particularly acute concern for programmable CBDCs. The Global Legal Entity Identifier Foundation notes that "bulletproof security measures, such as multi-factor authentication and private/public key management, are essential to protect and engender users' trust" [8]. However, the sophistication of programmable systems creates additional attack vectors that may not be adequately addressed by conventional security measures. Malicious actors could potentially exploit vulnerabilities in smart contract code to divert funds, disrupt service, or manipulate policy implementation.

### 4.2 Third-Party Dependencies and Vendor Lock-In

Programmable CBDC systems typically involve multiple participants, including technology providers, payment processors, and financial institutions. This distribution of functionality creates dependencies that can introduce operational risk and reduce central bank control over the monetary infrastructure. The Bank for International Settlements identifies "over dependency on a single technology vendor" as a source of "exit strategy risk" or "vendor lock-in risk," which could lead to "operational disruption, reputational loss, and economic loss" [2].

The integration of third-party systems also creates information asymmetries and coordination challenges. Central banks may not have full visibility into the operations of external providers, and information may not be gathered from third parties on time to enable effective risk monitoring. Different operational risk standards across participants can create gaps in the overall risk management framework, while intellectual property disputes with technology providers can threaten system continuity.

### 4.3 Systemic Risk Considerations

Research on CBDCs and systemic risk reveals complex and potentially contradictory effects. A study published in the Journal of International Financial Markets, Institutions and Money found that "CBDC-related news has a significant negative association with systemic risk in the long run, indicating a positive reception by the global financial sector" [9]. However, the same study found that "countries in the advanced stages of CBDC development show a significant positive association between CBDC-related news and systemic risk warranting the utmost care in implementing CBDC initiatives" [9].

This finding suggests that the development and deployment of programmable CBDC capabilities may introduce systemic risks that are not apparent in earlier stages. As systems become more sophisticated and integrated, and as policy tools become more deeply embedded in the monetary infrastructure, the potential for cascading failures may increase. The concentration of policy logic in programmable systems could create single points of failure that, if triggered, could propagate rapidly through the financial system.

### 4.4 Privacy and Surveillance Concerns

Programmability enables unprecedented visibility into financial transactions, creating tension between policy objectives and privacy rights. CBDCs allow for a "digital trail" of data to be accessed, collected, processed, and stored, which "may have economic value and could help central banks achieve policy objectives" [3]. However, using that data "could contravene privacy and undermine trust in CBDC."

The World Economic Forum emphasizes that "user data privacy should be a priority, not only to protect citizens from the risks of potential state-level surveillance but also to reduce vulnerabilities to external cyberattacks by domestic or foreign parties" [7]. The design of programmable CBDC systems must balance the policy benefits of transaction visibility against the risks of surveillance and the erosion of trust that such surveillance could create.

The programmability of CBDCs raises particular concerns about the potential for governments to monitor and control individual spending behavior. If money can be programmed with restrictions and conditions, the distinction between policy implementation and surveillance becomes blurred. The University of Pennsylvania Journal of International Law notes that one viewpoint holds that "programmable money is unacceptable because it may interfere with individuals' payment autonomy" and that "CBDC is intended to be a digital equal of physical cash, such as paper money and coins, which are widely accepted as unconditional forms of payment, rather than being programmed to restrict" [10].

---

## 5. Does Programmable Logic Amplify Policy Accidents?

### 5.1 The Mechanics of Amplification

The central risk of programmable money is that embedded policy logic, once deployed, operates automatically and at scale. This automation, while efficient under normal conditions, can amplify policy errors by propagating flawed logic across the entire monetary system without the friction and feedback that would normally slow and correct such errors.

Consider a scenario in which a central bank implements a programmable CBDC with embedded macroprudential restrictions designed to moderate credit growth. If the programmed conditions are calibrated incorrectly—perhaps too sensitively to certain indicators—the automatic enforcement mechanism could amplify economic fluctuations rather than moderating them. A moderate increase in credit growth could trigger widespread restrictions, slowing economic activity more than intended, which in turn could trigger additional programmed responses, creating a self-reinforcing contraction.

This amplification risk is particularly acute because programmable systems operate with less human oversight than conventional policy implementation. The automation that provides efficiency and consistency also reduces the opportunities for judgment, discretion, and course correction that characterize traditional monetary policy. Errors in system design or programming become embedded in the infrastructure and may be difficult to identify and correct before they cause significant harm.

### 5.2 Complexity and Unforeseen Interactions

Programmable CBDC systems can develop complexity that exceeds the capacity of designers to fully understand and predict. Smart contracts may interact in unforeseen ways, creating emergent behavior that was not anticipated by any individual component designer. The combination of multiple programmable features—each designed with specific policy objectives—can produce system-wide dynamics that differ qualitatively from the sum of individual components.

The International Monetary Fund notes that "technical, regulatory, and financial risks introduced by new capabilities like smart contracts need to be understood and addressed" [11]. However, the complexity of modern financial systems and the novel interactions enabled by programmability may exceed the analytical capabilities of existing risk management frameworks. Traditional stress testing and scenario analysis may be inadequate for identifying vulnerabilities in programmable systems, particularly those that arise from interactions between multiple policy mechanisms.

### 5.3 The Challenge of Reversibility

Physical cash and traditional electronic payment systems are relatively simple to understand and, when necessary, to modify or reverse. Programmable CBDC systems, particularly those implemented on distributed ledger infrastructure, may be significantly less flexible. The very features that provide programmability—automated execution, immutable recording, distributed validation—can also impede rapid response to policy errors or unintended consequences.

The University of Pennsylvania analysis notes that "the baseline of programmable money design is that it does not add to existing payment and spending conditions on legal tender, but rather facilitates the implementation of welfare programs" [10]. This principle suggests that programmability should be used to enhance existing policy mechanisms rather than to create entirely new monetary architectures. By maintaining continuity with established frameworks, jurisdictions can preserve the reversibility and flexibility that enable policy correction when errors occur.

### 5.4 Coordination and Governance Risks

Programmable CBDCs require sophisticated governance frameworks that specify how policy logic is determined, implemented, and modified. These governance requirements create coordination challenges that can themselves become sources of risk. The Global Legal Entity Identifier Foundation notes that "central banks, government agencies, and regulators determine CBDC rules, policies, directives, rights, responsibilities, and legal frameworks" [8], but the complexity of programmable systems may exceed the capacity of existing governance structures.

The World Economic Forum emphasizes that "communication about CBDCs is crucial and a strategy to guide engagement with stakeholders should be developed early" [7]. However, the technical complexity of programmable systems may make meaningful stakeholder engagement difficult. Citizens, businesses, and even policymakers may lack the technical understanding to evaluate proposed programmable features, creating information asymmetries that could enable the deployment of problematic policy logic without adequate scrutiny.

---

## 6. Balancing Mechanisms: Design Principles for Safe Programmable CBDCs

### 6.1 Preserving Fungibility and Unconditionality

The most fundamental design principle for safe programmable CBDCs is the preservation of money's fungible and unconditional character. As the International Monetary Fund emphasizes, programmability should operate at the transaction level rather than the token level, ensuring that "money must remain fungible" [3]. This approach allows policy tools to be implemented through conditional transactions without creating distinct categories of money that could be discriminated against or tracked.

The University of Pennsylvania analysis supports this approach, noting that the baseline for programmable money design is that it "does not add to existing payment and spending conditions on legal tender, but rather facilitates the implementation of welfare programs" [10]. By treating programmability as a tool for specific, bounded objectives rather than a fundamental redesign of monetary architecture, jurisdictions can capture the benefits of programmable policy while preserving the essential properties of money.

### 6.2 Layered Architecture and Modularity

The technical architecture of programmable CBDC systems should incorporate layering and modularity to contain the impact of errors and facilitate rapid correction. The Bank for International Settlements describes a "common protocol layer" for embedding policy measures [5], but this layer should be designed to isolate policy logic from core payment functionality. If policy mechanisms fail or produce unintended consequences, the underlying payment system should continue to function, allowing authorities to correct course without disrupting monetary circulation.

Modular design also supports the evolution of policy tools over time. Rather than embedding permanent policy logic in immutable smart contracts, jurisdictions should maintain the ability to modify, suspend, or replace programmable features as circumstances change. This flexibility is essential for managing the risks associated with policy experimentation and for adapting to new information about the effects of programmable mechanisms.

### 6.3 Robust Governance and Oversight

Effective governance is essential for managing the risks of programmable CBDCs. The Bank for International Settlements emphasizes that "risk management is applied throughout the lifecycle of a CBDC, from the research and design stages to implementation and operations" [2]. This lifecycle approach requires ongoing identification, assessment, monitoring, and reporting of risks, with mitigation strategies aligned to the institution's risk appetite.

Governance frameworks should incorporate multiple layers of oversight for programmable policy tools. Technical specifications should be subject to expert review, policy objectives should be validated against clear mandates, and implementation should be monitored for unintended consequences. The complexity of programmable systems argues for conservative deployment, with new features introduced gradually and evaluated extensively before full implementation.

### 6.4 Privacy-Enhancing Design

Addressing privacy concerns is essential for maintaining public trust in programmable CBDCs. The World Economic Forum recommends that CBDCs "be designed with as much anonymity as possible, taking into consideration AML/CFT regulations and security policies" [7]. This design principle supports both individual rights and system security, as excessive data collection creates vulnerabilities that could be exploited by malicious actors.

Privacy-preserving technologies, including zero-knowledge proofs and secure multi-party computation, may enable some programmable features while protecting transaction privacy. These approaches allow conditions to be verified without revealing the details of transactions to third parties, preserving the confidentiality of financial information while enabling automated compliance checking. Investment in privacy-enhancing technologies should be a priority for jurisdictions pursuing programmable CBDC development.

### 6.5 International Coordination and Interoperability

The cross-border dimensions of CBDC programmability require international coordination to manage systemic risks and ensure interoperability. The Bank for International Settlements notes that "a crucial prerequisite for obtaining the greatest benefits from cross-border CBDC arrangements is the need for cooperation between jurisdictions" [5]. Coordination should address technical standards, legal frameworks, and policy consistency to prevent regulatory arbitrage and ensure that programmable features operate consistently across borders.

The World Economic Forum emphasizes that "CBDC analysis must be conducted on a country-by-country basis with consideration of the best solutions for the country's specific needs" [7]. However, this national focus should not preclude international coordination on common standards and best practices. The interconnected nature of global financial systems means that vulnerabilities in any major CBDC system could propagate across borders, making collective action essential for systemic stability.

---

## 7. Conclusions and Recommendations

The analysis presented in this report supports a nuanced conclusion regarding the balance between money supply control and risk isolation in programmable CBDC systems. Programmability offers substantial benefits for policy implementation, including targeted distribution of government payments, automated compliance with regulatory requirements, enhanced transmission of monetary impulses, and novel tools for behavioral policy. These capabilities could significantly improve the effectiveness of monetary and fiscal policy, reducing leakage, lowering transaction costs, and accelerating the delivery of public benefits.

However, these benefits come with significant risks that must be carefully managed. The automation and scale of programmable systems can amplify policy errors, propagating flawed logic across the financial system without the friction and feedback that would normally enable correction. Technical complexity creates vulnerabilities that may exceed the capacity of existing risk management frameworks, while third-party dependencies and governance challenges introduce additional vectors for failure. Privacy concerns and the potential for surveillance raise fundamental questions about the appropriate scope of programmable features.

The central finding is that the risks of programmable CBDCs are not inherent to the technology but rather depend on design choices and governance frameworks. Jurisdictions that approach programmability as a tool for specific, bounded objectives—rather than a fundamental redesign of monetary architecture—are more likely to capture benefits while managing risks. The preservation of money's fungible and unconditional character should be a foundational principle, with programmability operating at the transaction level rather than the token level.

Based on this analysis, several recommendations emerge for central banks and policymakers considering programmable CBDC features:

**First**, jurisdictions should clearly establish the policy objectives of programmability before designing technical systems. Programmable features should be developed in response to specific policy needs rather than as general-purpose capabilities that may be applied to unanticipated purposes. This objective-oriented approach helps ensure that programmability serves clearly defined purposes and that the associated risks are justified by concrete benefits.

**Second**, central banks should adopt a risk management approach that spans the entire CBDC lifecycle, from research and design through implementation and operation. Risk assessment should be ongoing and iterative, adapting to new information about system behavior and emerging vulnerabilities. The complexity of programmable systems argues for conservative deployment, with features introduced gradually and evaluated extensively before full implementation.

**Third**, technical architecture should incorporate layering and modularity to contain the impact of errors and preserve reversibility. Policy logic should be isolated from core payment functionality, and jurisdictions should maintain the ability to modify, suspend, or replace programmable features as circumstances change. This flexibility is essential for managing the risks associated with policy experimentation.

**Fourth**, governance frameworks should incorporate multiple layers of oversight for programmable policy tools, including technical review, policy validation, and behavioral monitoring. The complexity of programmable systems argues for meaningful stakeholder engagement, with clear communication about the capabilities, limitations, and risks of programmable features.

**Finally**, international coordination should address technical standards, legal frameworks, and policy consistency to ensure interoperability and prevent regulatory arbitrage. The global nature of financial systems means that vulnerabilities in any major CBDC system could have cross-border implications, making collective action essential for systemic stability.

In conclusion, programmable CBDC money represents a powerful tool that can enhance the effectiveness of monetary policy and government program implementation. However, this power carries corresponding responsibilities for careful design, robust governance, and ongoing risk management. The question is not whether programmability is inherently stabilizing or destabilizing, but rather whether jurisdictions can develop the institutional capacity to harness its benefits while containing its risks. The evidence suggests that this balance is achievable, but only through deliberate effort and sustained commitment to the principles outlined above.

---

## References

[1] German Institute for Economic Research. "CBDCs: Making Payments Programmable." https://www.gi-de.com/en/spotlight/currency-technology/cbdcs-making-payments-programmable

[2] Bank for International Settlements. "Central Bank Digital Currencies: Financial Sector Implications and Cross-Border Considerations." OTHP 81. https://www.bis.org/publ/othp81.pdf

[3] International Monetary Fund. "Central Bank Digital Currency Virtual Handbook." https://www.imf.org/en/topics/digital-payments-and-finance/central-bank-digital-currency/virtual-handbook

[4] Global Legal Entity Identifier Foundation. "Central Bank Digital Currency: Opportunities, Challenges, and Design." https://www.gleif.org/lei-solutions/regulatory-use-of-the-lei/consultation-responses/central-bank-digital-currency-opportunities-challenges-and-design_clean.pdf

[5] Bank for International Settlements. "Central Bank Digital Currencies: Policy Principles." OTHP 73. https://www.bis.org/publ/othp73.pdf

[6] eco.com. "What is a CBDC? Understanding Central Bank Digital Currencies in 2025." https://eco.com/support/en/articles/12005811-what-is-a-cbdc-understanding-central-bank-digital-currencies-in-2025

[7] World Economic Forum. "Central Bank Digital Currency Policy-Maker Toolkit." https://www3.weforum.org/docs/WEF_CBDC_Policymaker_Toolkit.pdf

[8] MDPI. "Central Bank Digital Currency: A Systematic Review." Risks 12(1):19. https://www.mdpi.com/2227-7072/12/1/19

[9] Journal of International Financial Markets, Institutions and Money. "Central bank digital currency and systemic risk." Volume 99, March 2025, 102104. https://www.sciencedirect.com/science/article/pii/S1042443124001707

[10] University of Pennsylvania Journal of International Law. "Programmable Money and the Future of Central Bank Digital Currency." https://scholarship.law.upenn.edu/cgi/viewcontent.cgi?article=2106&context=jil

[11] International Monetary Fund. "Programmable Payments and Settlement: Policy Implications of New Technologies." Working Paper 2024/177. https://www.imf.org/-/media/files/publications/wp/2024/english/wpiea2024177-print-pdf.pdf

## Annotations


## Sources
[1] https://eco.com/support/en/articles/12005811-what-is-a-cbdc-understanding-central-bank-digital-currencies-in-2025
[2] https://scholarship.law.upenn.edu/cgi/viewcontent.cgi?article=2106&context=jil
[3] https://www.bis.org/publ/othp73.pdf
[4] https://www.bis.org/publ/othp81.pdf
[5] https://www.dhs.gov/sites/default/files/2024-09/2024aepphaselllcombattingillicitactivityutilizingfinancial.pdf
[6] https://www.gfma.org/wp-content/uploads/2022/02/central-bank-digital-currencies-a-global-capital-markets-perspective-full-report-feb-2022-final.pdf
[7] https://www.gi-de.com/en/spotlight/currency-technology/cbdcs-making-payments-programmable
[8] https://www.gleif.org/lei-solutions/regulatory-use-of-the-lei/consultation-responses/central-bank-digital-currency-opportunities-challenges-and-design_clean.pdf
[9] https://www.imf.org/-/media/files/publications/wp/2024/english/wpiea2024177-print-pdf.pdf
[10] https://www.imf.org/en/topics/digital-payments-and-finance/central-bank-digital-currency/virtual-handbook
[11] https://www.mdpi.com/2227-7072/12/1/19
[12] https://www.sciencedirect.com/science/article/pii/S1042443124001707
[13] https://www3.weforum.org/docs/WEF_CBDC_Policymaker_Toolkit.pdf