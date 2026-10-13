# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 43002385 | **Time:** 130.35s | **Cost:** $0.16499
--------------------------------------------------------------------------------

# How Does Scenario Design in Environmental Risk Stress Testing Affect Capital Adequacy Calibration?

## Abstract

This research report examines the intricate relationship between scenario design in environmental risk stress testing and its subsequent effects on capital adequacy calibration within the banking sector. Drawing upon recent regulatory guidelines from the European Banking Authority, the European Central Bank, and the Network for Greening the Financial System, this analysis explores how the methodological choices in scenario construction—encompassing physical and transition risk modeling, time horizon selection, and shock calibration—fundamentally influence the determination of capital buffers required to maintain financial stability. The report synthesizes theoretical frameworks from stress testing literature with practical regulatory expectations to provide a comprehensive understanding of how scenario design choices propagate through to capital adequacy outcomes.

---

## 1. Introduction

The integration of environmental, social, and governance (ESG) considerations into prudential supervision represents one of the most significant developments in banking regulation over the past decade. Environmental risks, particularly those associated with climate change, have emerged as material threats to the stability of financial institutions and the broader financial system. This recognition has prompted regulatory bodies across jurisdictions to develop comprehensive frameworks for assessing and managing these risks, with stress testing serving as a central tool in this endeavor.

The European Banking Authority's Guidelines on Environmental Scenario Analysis explicitly mandate that institutions integrate environmental risk factors, identified following the EBA Guidelines on the management of ESG risks, within their stress testing models and consider the results of these stress tests when assessing capital and liquidity adequacy as part of their Internal Capital Adequacy Assessment Process (ICAAP) and Internal Liquidity Adequacy Assessment Process (ILAAP) processes [1]. This regulatory expectation underscores the direct link between environmental stress testing outcomes and capital adequacy determinations.

The fundamental question this report addresses is how the design choices made during the construction of environmental risk scenarios—including the selection of risk types, the calibration of shock intensities, the determination of time horizons, and the specification of transmission channels—ultimately affect the calibration of capital requirements for financial institutions. Understanding this relationship is essential for both regulators seeking to design effective supervisory frameworks and financial institutions aiming to develop robust internal stress testing capabilities.

The significance of this inquiry extends beyond mere academic interest. As the Basel Committee on Banking Supervision has emphasized, stress testing principles require institutions to determine the impact on overall risk profiles, identify relevant climate-related risk factors, measure vulnerability to climate-related risks, and estimate exposures and potential losses [2]. Each of these elements involves design choices that directly influence the resulting capital adequacy assessment. The ECB's 2022 climate stress test further highlighted persistent data and methodology gaps—including coverage of physical risks, treatment of tail events, limited spatial granularity, and weak links from narratives to quantitative outputs [3]—indicating that scenario design remains a critical area requiring careful attention.

---

## 2. Theoretical Framework: Stress Testing and Capital Adequacy

### 2.1 The Mechanics of Stress Testing in Prudential Supervision

Stress testing in the banking context serves as a forward-looking risk assessment tool designed to evaluate the resilience of financial institutions to adverse economic conditions. Unlike backward-looking Value-at-Risk measures, stress tests attempt to quantify the potential impact of hypothetical scenarios on an institution's financial position, thereby informing decisions about appropriate capital buffers. The theoretical foundation for stress testing rests on the recognition that extreme but plausible events—while potentially rare—can have catastrophic consequences that threaten institutional solvency.

The relationship between stress testing and capital adequacy is formalized through regulatory frameworks such as the Capital Requirements Directive and Regulation. Article 177(2a) of Regulation (EU) No 575/2013 specifically requires institutions using internal ratings-based approaches to define and use stress test scenarios that include environmental risk drivers, particularly physical risk and transition risk drivers arising from climate change, as part of their stress testing programmes on credit risk [1]. This regulatory requirement creates a direct conduit through which scenario design choices influence capital adequacy determinations.

From a theoretical perspective, the optimal design of stress test scenarios has been analyzed in the academic literature. Research by Parlatore Sicking and Philippon demonstrates that the scenario design problem can be conceptualized as choosing an information point in a feasible set determined by the Kalman filter, where perfect learning is not feasible because the budget set does not include a posterior variance of zero [4]. This constraint arises because choosing a more extreme scenario has two countervailing effects: on one hand, a higher stress level increases the weight that the stress test results place on the bank's exposure to a particular risk factor; on the other hand, more extreme scenarios increase the noise in the stress test results.

### 2.2 Capital Adequacy Calibration in the Context of Environmental Risks

Capital adequacy calibration for environmental risks presents unique challenges compared to traditional risk categories. The time horizons over which climate risks materialize extend far beyond the typical business cycle, creating difficulties for models designed to assess short-run divergences from long-run equilibria [5]. Furthermore, the non-linear and potentially irreversible nature of climate impacts means that standard statistical approaches based on historical data may underestimate tail risks.

The ECB's Guide on climate-related and environmental risks sets explicit expectations to embed climate drivers into business strategy, governance and risk-appetite frameworks, risk management across risk types, credit underwriting and monitoring, market and operational and liquidity risk management, and disclosures [3]. These expectations create a comprehensive framework within which capital adequacy must be assessed, requiring institutions to consider how environmental risks affect multiple dimensions of their risk profile simultaneously.

The integration of climate risk into capital adequacy assessment is further complicated by the dual nature of climate risks: physical risks arising from climate-related events and transition risks associated with the economic adjustment to a lower-carbon economy. As noted by the Basel Committee, a comprehensive stress testing scenario would ideally reflect both types of risks, including all physical and transition risks that may generate potentially material losses for banks [2]. The scenarios need to take into account cumulative and feedback effects arising from both sets of risks and their economic impacts.

---

## 3. Scenario Design Dimensions and Their Impact on Capital Calibration

### 3.1 Physical Versus Transition Risk Scenarios

One of the most fundamental design choices in environmental stress testing involves the selection of risk types to be modeled. Physical risks encompass the direct impacts of climate change, including acute events such as floods, storms, and wildfires, as well as chronic risks such as sea-level rise and sustained temperature increases. Transition risks, by contrast, arise from the economic and financial adjustments required to mitigate climate change, including policy changes, technological innovations, and shifts in market preferences.

The Network for Greening the Financial System (NGFS) has developed a comprehensive scenario framework that distinguishes between "orderly," "disorderly," and "hot house world" scenarios [6]. In orderly scenarios, the carbon price increases relatively early and gradually, allowing for an orderly transition that minimizes economic disruption while achieving climate targets. Disorderly scenarios involve delayed policy action followed by abrupt and potentially more costly adjustments. Hot house world scenarios assume continued high emissions, resulting in significant physical damage but minimal transition costs.

The choice among these scenario types has direct implications for capital adequacy calibration. In orderly transition scenarios, carbon prices increase gradually, allowing financial institutions and their counterparties time to adjust their business models and risk exposures. The resulting credit losses, while potentially significant, are spread over an extended period, potentially reducing the immediate capital adequacy impact. Disorderly transitions, however, involve sudden and severe price shocks that can trigger cascading defaults and asset value declines, potentially requiring substantially higher capital buffers to maintain solvency.

Research by Ikeda and Monnin emphasizes that climate risks will materialize through complex interactions that can amplify initial shocks [7]. This suggests that scenarios incorporating both physical and transition risks may generate larger capital impacts than scenarios focusing on either risk type in isolation. The challenge for scenario designers lies in capturing these interaction effects while maintaining analytical tractability.

### 3.2 Time Horizon Selection and Its Effects on Capital Buffers

The selection of appropriate time horizons for environmental stress testing represents a critical design decision with significant implications for capital adequacy calibration. Traditional stress tests typically focus on horizons of two to three years, aligned with the business cycle and regulatory capital planning cycles. Climate risks, however, operate on substantially longer time scales, with material impacts potentially extending decades into the future.

The NGFS guide on scenario analysis notes that economic models typically used by central banks have modeling horizons that do not extend much further than the business cycle [5]. This limitation creates a fundamental tension between the long-term nature of climate risks and the short-term focus of traditional stress testing frameworks. The Basel Committee acknowledges that effective risk management may necessitate assessments that reflect longer time horizons to understand the risks associated with business and portfolio strategies and to evaluate the timing of potential risk mitigation options [2].

The mathematical implications of time horizon selection can be illustrated through the lens of discounted loss projections. If we denote the projected loss at time $t$ under a stress scenario as $L_t$, and the discount rate as $r$, then the present value of losses over a horizon $T$ is given by:

$$PV(L) = \sum_{t=0}^{T} \frac{L_t}{(1+r)^t}$$

Extending the time horizon $T$ captures additional loss realizations but also subjects these losses to greater uncertainty. The variance of projected losses typically increases with the time horizon, reflecting uncertainty about future economic conditions, technological developments, and policy responses. This increased uncertainty must be reflected in capital adequacy calculations, potentially requiring higher capital buffers to maintain specified confidence levels.

The ECB's 2022 climate stress test employed scenarios extending to 2050, recognizing the long-term nature of climate risks [6]. This extended horizon allows for the capture of physical damage scenarios that unfold gradually over time but also introduces substantial uncertainty into loss projections. The calibration of capital buffers based on these extended-horizon scenarios must therefore account for both the expected path of losses and the uncertainty surrounding that path.

### 3.3 Scenario Granularity and Transmission Channel Specification

The level of granularity in scenario design—encompassing both sectoral and geographic dimensions—significantly affects the precision of capital adequacy assessments. The ECB's qualitative assessment framework for climate stress testing examined the extent to which banks incorporate climate risk into their business strategies, with particular attention to how risks are transmitted through various channels [3].

The EBA Guidelines on Environmental Scenario Analysis require institutions to identify and model the most relevant transmission channels through which environmental risk drivers could impact their current and future financial position [1]. This requirement acknowledges that the pathway from climate hazards to financial losses is mediated by numerous factors, including the geographic distribution of exposures, the sectoral composition of loan portfolios, and the vulnerability of individual borrowers to climate-related impacts.

Mathematical models of climate risk transmission typically incorporate multiple risk factors and their interactions. As described in the BIS working paper on climate risk modeling, the probability of default for a borrower under climate risk can be expressed as a function of both physical and transition risk factors [8]:

$$PD_{climate} = f(PD_{base}, PD_{physical}, PD_{transition})$$

where $PD_{base}$ represents the baseline probability of default without climate considerations, $PD_{physical}$ captures the additional default risk arising from physical climate impacts, and $PD_{transition}$ reflects transition risk effects. The functional form and parameters of this relationship depend critically on scenario design choices, including the specification of physical risk drivers (such as flood frequency and severity) and transition risk drivers (such as carbon prices and technology costs).

The spatial disaggregation of scenarios enhances interpretability for ICAAP and Pillar 2 capital planning [3]. By modeling risks at the regional or sectoral level, institutions can more precisely assess the concentration of exposures and the potential for correlated defaults. This granularity comes at the cost of increased data requirements and model complexity, but enables more accurate capital adequacy assessments by capturing heterogeneity in risk exposures.

---

## 4. Methodological Considerations in Scenario Calibration

### 4.1 Calibration Approaches and Their Implications

The calibration of environmental stress test scenarios involves translating narrative descriptions of future climate and economic conditions into quantitative parameters that can be used in financial models. This process is inherently uncertain, as it requires projecting decades of climate, economic, and policy developments under conditions that have no historical precedent.

The NGFS scenarios provide a standardized framework for scenario calibration, with carbon prices serving as a key calibration parameter [6]. In the orderly scenario, carbon prices are already relatively high by 2030 and increase further until 2050 to achieve emissions targets consistent with 1.5°C of warming. The disorderly scenario delays this price increase, resulting in higher prices in later years to achieve the same cumulative emissions reduction. The hot house world scenario assumes no carbon price increases, with physical damages serving as the primary source of financial risk.

The mathematical relationship between carbon price trajectories and financial losses can be expressed through the impact on corporate earnings and asset values. Research by Le Guenedal and Tankov employs a Bayesian approach to account for uncertainty in scenarios that differ in the frequency of climate risk-driven events [8]. This approach recognizes that scenario calibration involves not only point estimates of key parameters but also assessments of uncertainty that should be reflected in capital adequacy calculations.

The calibration of physical risk scenarios presents additional challenges due to the limited historical data on extreme climate events and their economic impacts. The ECB's 2022 climate stress test identified coverage of physical risks as a significant gap in banks' stress testing capabilities [3]. Without robust historical data, calibration must rely on climate model projections, which themselves involve substantial uncertainty. This uncertainty propagates through to capital adequacy assessments, potentially requiring additional conservative buffers.

### 4.2 The Role of Scenario Severity in Capital Determination

The severity of stress test scenarios directly affects the resulting capital adequacy determinations. More severe scenarios generate larger projected losses, potentially requiring higher capital buffers to maintain solvency under adverse conditions. However, the relationship between scenario severity and capital requirements is not linear, as extremely severe scenarios may produce losses that exceed any plausible capital buffer.

The theoretical literature on stress test design addresses this trade-off between scenario informativeness and capital impact. Parlatore Sicking and Philippon demonstrate that the optimal intervention, and hence the optimal learning from stress tests, depends on the regulator's prior beliefs and the correlation of risk exposures within and across banks [4]. A higher expected exposure increases the likelihood of intervention, suggesting that scenarios calibrated to reflect higher expected losses will more frequently trigger capital requirements.

The mechanical link between stress test results and capital requirements in regulatory practice creates a direct channel through which scenario design affects capital adequacy. In many jurisdictions, banks must demonstrate that their capital ratios remain above specified thresholds under adverse scenarios. The choice of adverse scenario therefore determines the binding constraint on capital adequacy. As noted in the NBER working paper, this mechanical link conflates two conceptually separate issues—learning and intervention—and may not be appropriate for all regulatory objectives [9].

The calibration of scenario severity must balance the need to test resilience against extreme but plausible events against the risk of requiring prohibitively high capital buffers. The Basel Committee's principles for effective risk management emphasize that stress testing should consider a range of scenarios, including both severe but plausible adverse conditions and more moderate stress situations [2]. This multi-scenario approach allows regulators and institutions to assess capital adequacy across a range of potential futures rather than relying on a single threshold.

---

## 5. Integration with Regulatory Capital Frameworks

### 5.1 Pillar 1 and Pillar 2 Interactions

The integration of environmental stress testing into regulatory capital frameworks occurs through both Pillar 1 minimum capital requirements and Pillar 2 supervisory processes. The EBA Guidelines on Environmental Scenario Analysis specify how environmental risk drivers should be taken into account in the scenarios used for credit risk internal stress testing, fulfilling the mandate of Article 177(2a) of the Capital Requirements Regulation [1].

Under Pillar 1, institutions using internal model approaches are required to use environmental stress test scenarios as "challenger models" to validate their internal estimates of capital requirements. This requirement creates a direct link between scenario design and regulatory capital, as discrepancies between internal model outputs and stress test results may trigger supervisory attention and potential adjustments to capital requirements.

Pillar 2 provides an additional layer of capital assessment through the supervisory evaluation process. The ECB's Pillar 2 Guidance indicates the level of capital that the ECB expects banks to maintain in addition to their binding capital requirements, serving as a buffer for banks to withstand stress [6]. Climate stress test results inform this supervisory assessment by providing forward-looking information about potential capital impacts under various environmental scenarios.

The interaction between Pillar 1 and Pillar 2 requirements creates a multi-layered framework for capital adequacy calibration. Scenario design choices affect both layers: Pillar 1 challenger model requirements and Pillar 2 supervisory assessments. The ECB's 2022 climate stress test findings inform Pillar 2 Guidance by identifying banks with insufficient climate risk management capabilities or potentially inadequate capital buffers [3].

### 5.2 ICAAP Integration and Internal Capital Planning

The Internal Capital Adequacy Assessment Process (ICAAP) provides the primary mechanism through which institutions integrate environmental stress testing into their internal capital planning. The EBA Guidelines require institutions to consider the results of environmental stress tests when assessing capital and liquidity adequacy as part of their ICAAP and ILAAP processes [1].

The integration of climate scenario analysis into ICAAP requires institutions to translate scenario-specific projections into capital adequacy metrics. This translation involves several steps: mapping climate hazards to credit risk parameters (such as probability of default and loss given default), projecting the impact on market risk exposures, and assessing operational and liquidity risks arising from environmental factors. Each of these steps involves design choices that affect the resulting capital adequacy assessment.

Research on climate risk quantification has developed specialized metrics for this purpose. The Conditional Expected Shortfall (CES) provides a solvency-oriented capital-at-risk threshold, while measures of tail severity support stress-test calibration and buffer sizing [3]. The formal definition of CES as the expected loss beyond the conditional quantile, given a climate information set, provides a theoretically grounded basis for capital adequacy assessment under environmental stress scenarios.

The bootstrap-validated confidence intervals recommended for climate stress testing provide transparency for disclosure and market discipline [3]. By quantifying the uncertainty in capital adequacy estimates, institutions and supervisors can make more informed decisions about appropriate buffer levels. This approach acknowledges the inherent uncertainty in climate projections while still providing actionable guidance for capital planning.

---

## 6. Challenges and Implications for Capital Adequacy

### 6.1 Data Limitations and Their Impact on Scenario Design

The quality and availability of data represent fundamental constraints on environmental stress testing and, consequently, on capital adequacy calibration. The ECB's 2022 climate stress test identified data availability and usage as significant challenges for banks' climate stress testing capabilities [3]. Without adequate data, scenario design must rely on approximations and assumptions that may not accurately reflect actual risk exposures.

The NGFS guide on scenario analysis acknowledges that the lack of available data and research to calibrate the scenarios and assess impacts remains a significant challenge [5]. This data gap affects multiple dimensions of scenario design: the calibration of physical risk frequencies and severities, the estimation of transition risk impacts on specific sectors and regions, and the assessment of second-round effects through the financial system.

The mathematical implications of data limitations can be understood through the lens of estimation uncertainty. If we denote the true but unknown parameter governing climate risk impacts as $\theta$, and our estimate based on available data as $\hat{\theta}$, then the uncertainty in capital adequacy estimates can be expressed as a function of the estimation error $\theta - \hat{\theta}$. Limited data increases the variance of $\hat{\theta}$, which propagates through to uncertainty in projected losses and required capital buffers.

Addressing data limitations requires both improvements in data collection and the development of robust analytical methods that can accommodate uncertainty. The EBA Guidelines emphasize the need for institutions to develop appropriate methodologies for integrating environmental risks into their stress testing frameworks, even in the presence of data constraints [1]. This requirement acknowledges that perfect data is not available but still expects institutions to make reasonable efforts to assess and manage environmental risks.

### 6.2 Model Risk and Scenario Uncertainty

The use of models to translate scenario assumptions into capital adequacy estimates introduces model risk—the possibility that model outputs are inaccurate or misleading. Environmental stress testing involves multiple layers of modeling, from climate projection models to economic impact models to financial exposure models. Each layer introduces potential errors that compound through the analysis chain.

The BIS insights on climate risk stress testing note that the design of scenarios and the modeling and calibration of shocks involve specific complexities [2]. Unlike traditional stress testing, where scenarios can be based on historical crisis episodes, environmental stress testing must project novel future conditions that have no direct historical precedent. This limitation means that model validation based on backtesting against historical data is not possible to the same extent as for traditional risk measures.

The mathematical treatment of model risk in environmental stress testing typically involves scenario uncertainty analysis. Rather than relying on a single scenario projection, institutions and supervisors should consider a range of plausible scenarios and assess how capital adequacy varies across this range. This approach acknowledges that the "true" future trajectory of climate and economic conditions is uncertain and that capital adequacy assessments should be robust to this uncertainty.

The integration of physical risk, transition risk, and macro-financial transmission channels remains a methodological challenge [5]. Current models often treat these risk categories separately, potentially missing important interactions and feedback effects. As models become more sophisticated and better capture these interactions, capital adequacy estimates may change, requiring ongoing refinement of stress testing frameworks and capital buffers.

---

## 7. Implications for Regulatory Practice and Future Directions

### 7.1 Supervisory Convergence and Scenario Standardization

The development of common standards for environmental stress testing represents a key regulatory objective. The EBA Guidelines aim to ensure consistency, long-term considerations, and common standards for assessment methodologies throughout the EU and across sectors [1]. This standardization effort directly addresses the challenge of scenario design by providing frameworks that promote comparability and reduce arbitrariness in capital adequacy determinations.

The NGFS scenario framework serves as a foundation for international convergence in environmental stress testing [5]. By providing standardized scenarios that can be adapted to national contexts, the NGFS facilitates comparison across jurisdictions and reduces the potential for regulatory arbitrage. The ECB's adoption of NGFS scenarios in its climate stress test demonstrates the practical application of this framework [6].

However, achieving full standardization faces practical challenges. Different jurisdictions have different risk profiles, financial system structures, and regulatory frameworks. The ECB conference paper on regulatory arbitrage highlights how uneven application of regulation can drive international capital flows [10]. Environmental stress testing frameworks must balance the need for standardization against the recognition that some adaptation to local conditions is necessary.

### 7.2 Evolution of Methodologies and Capital Calibration

The methodologies for environmental stress testing continue to evolve as understanding of climate risks improves and data availability increases. The EBA Guidelines acknowledge that the development of relevant regulation, disclosure frameworks, practices, as well as models and data is more advanced for environmental risks, especially linked to climate, than for other ESG factors [1]. This relative maturity of climate risk methodologies has enabled the development of detailed guidelines for climate stress testing, while social and governance factors remain subjects of ongoing development.

Future revisions of environmental stress testing guidelines may incorporate more sophisticated approaches to scenario design and capital calibration. The Management Solutions summary of EBA guidelines notes that the application date for all entities is January 1, 2027 [11], providing a timeline for institutions to develop and implement appropriate frameworks. This deadline creates incentives for continued methodological development and refinement.

The integration of compound risks into climate scenario analysis represents an important direction for future development [2]. Compound risks—arising from the simultaneous or sequential occurrence of multiple adverse events—may generate losses that exceed the sum of individual risk impacts. Capturing these compound effects in scenario design could significantly affect capital adequacy calibration, potentially requiring higher buffers to account for tail dependencies between risk categories.

---

## 8. Conclusion

The design of scenarios in environmental risk stress testing exerts a profound influence on capital adequacy calibration through multiple interconnected channels. The selection of risk types—whether focusing on physical risks, transition risks, or their combination—determines the nature and magnitude of projected losses. Time horizon choices affect both the scope of risks captured and the uncertainty surrounding loss projections. Scenario granularity and transmission channel specification influence the precision of capital adequacy estimates and the ability to identify concentration risks.

The theoretical framework underlying stress test design reveals fundamental trade-offs that must be navigated in practice. More extreme scenarios provide greater information about institutional resilience but also increase noise in stress test results. Longer time horizons capture long-term climate impacts but introduce greater uncertainty. Greater granularity improves the precision of assessments but requires data and modeling capabilities that may not yet be fully developed.

The integration of environmental stress testing into regulatory capital frameworks through Pillar 1 and Pillar 2 processes creates direct channels through which scenario design choices affect capital requirements. The ICAAP provides the primary mechanism for institutions to translate scenario analysis into internal capital planning, while supervisory processes use stress test results to inform assessments of capital adequacy and potential supervisory actions.

Looking forward, the continued evolution of environmental stress testing methodologies will further refine the relationship between scenario design and capital calibration. The development of more sophisticated models capturing physical and transition risk interactions, improvements in data availability and quality, and international convergence on scenario standards will all contribute to more robust capital adequacy assessments. However, inherent uncertainties in climate projections and economic modeling will continue to require judgment and conservatism in capital calibration, ensuring that financial institutions maintain adequate buffers to withstand environmental risks across a range of plausible futures.

---

## References

[1] European Banking Authority, "Guidelines on Environmental Scenario Analysis," EBA/GL/2025/XX, 2025.

[2] Basel Committee on Banking Supervision, "Principles for the Effective Management and Supervision of Climate-Related Financial Risks," Basel III Final Framework, 2022.

[3] European Central Bank, "2022 Climate Risk Stress Test – Methodology, Scenarios and Quality Assurance," Banking Supervision, July 2022.

[4] Parlatore Sicking, C. and T. Philippon, "Stress Tests," Working Paper, New York University Stern School of Business, 2024.

[5] Network for Greening the Financial System, "NGFS Guide to Scenario Analysis," NGFS Technical Document, 2023.

[6] European Central Bank, "ECB 2022 Climate Stress Test Report," Banking Supervision, 2022.

[7] Ikeda, T. and P. Monnin, "Principles for Addressing Climate Systemic Risks," CEPWEB Working Paper, 2024.

[8] Bank for International Settlements, "Climate-Related Risk and Financial Stability," BIS Working Papers, No. 1274, 2024.

[9] Faria-e-Castro, M., et al., "Optimal Stress Test Design," NBER Working Paper No. 29901, 2024.

[10] Reinhardt, C. and R. Sowerbutts, "Regulatory Arbitrage and Cross-Border Banking," ECB Conference Paper, November 2015.

[11] Management Solutions, "Guidelines on Environmental Scenario Analysis – Summary," EBA Guidelines Analysis, 2025.

## Annotations


## Sources
[1] http://www.actuarialstandardsboard.org/wp-content/uploads/2019/06/asop055_194.pdf
[2] https://climatex.substack.com/p/climate-stress-test-regulations-tips
[3] https://documents1.worldbank.org/curated/en/760481644944260441/pdf/Assessing-Financial-Risks-from-Physical-Climate-Shocks-A-Framework-for-Scenario-Generation.pdf
[4] https://finance-climact.eu/wp-content/uploads/2021/08/ADEME-2021-Scenario-based-climate-stress-testing-from-risk-analysis-to-modeling.pdf
[5] https://pages.stern.nyu.edu/~tphilipp/papers/Parlatore_Philippon_Stress_Tests.pdf
[6] https://www.bankingsupervision.europa.eu/ecb/pub/pdf/ssm.climate_stress_test_report.20220708~2e3cc0999f.en.pdf
[7] https://www.bankingsupervision.europa.eu/ecb/pub/pdf/ssm.climateriskstresstest2021~a4de107198.en.pdf
[8] https://www.bis.org/bcbs/publ/d427.pdf
[9] https://www.bis.org/bcbs/publ/d572.pdf
[10] https://www.bis.org/fsi/publ/insights34.pdf
[11] https://www.bis.org/publ/work1274.pdf
[12] https://www.cepweb.org/wp-content/uploads/2024/10/Ikeda-Monnin-2024.-Principles-for-addressing-climate-systemic-risks-with.pdf
[13] https://www.eba.europa.eu/sites/default/files/2025-11/170da4c8-9b56-4fb0-ad60-94d433b7e866/Guidelines%20on%20environmental%20scenario%20analysis.pdf
[14] https://www.eba.europa.eu/sites/default/files/2026-01/60ba0389-2d7a-46b7-96e8-9072c481d8ce/EIOPA-BoS-25-602%20-%20ESAs%20Final%20Report%20-%20Joint%20Guidelines%20on%20ESG%20Stress%20Testing.pdf
[15] https://www.ebf.eu/wp-content/uploads/2023/02/The-EU-banking-regulatory-framework-and-its-impact-on-banks-and-the-economy_30Jan-1.pdf
[16] https://www.ecb.europa.eu/press/conferences/shared/pdf/20151104_mp_policy_research/2-4_Reinhardt_Sowerbutts.pdf
[17] https://www.ecb.europa.eu/pub/pdf/scpwps/ecb.wp2910~c4d2c82f8c.en.pdf
[18] https://www.federalreserve.gov/frrs/guidance/interagency-supervisory-guidance-on-stress-testing-for-banking-organizations-with-total-consolidated-assets-of-more-than-10.htm
[19] https://www.iais.org/uploads/2023/06/Draft-Revised-ICP-17.pdf
[20] https://www.managementsolutions.com/sites/default/files/publicaciones/eng/guidelines-on-environmental-scenario-analysis.pdf
[21] https://www.mdpi.com/1911-8074/19/1/48
[22] https://www.nber.org/system/files/working_papers/w29901/w29901.pdf
[23] https://www.ngfs.net/system/files/import/ngfs/medias/documents/ngfs_guide_scenario_analysis_final.pdf
[24] https://www.osfi-bsif.gc.ca/en/guidance/guidance-library/capital-adequacy-requirements-car-guideline-2024
[25] https://www.tcfdhub.org/Downloads/pdfs/E06%20-%20Climate%20related%20risks%20and%20opportunities.pdf
[26] https://www.theiia.org/globalassets/site/content/guidance/recommended/supplemental/practice-guides/global-practice-guide-auditing-capital-adequacy-and-stress-testing-for-banks/gpg_auditing_capital_adequacy_and_stress_testing_for_banks_3rd_edition.pdf
[27] https://www.unepfi.org/wordpress/wp-content/uploads/2021/12/Good-Practice-Guide-to-Climate-Stress-Testing.pdf