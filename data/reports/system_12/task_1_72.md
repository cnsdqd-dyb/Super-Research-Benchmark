# Deep Research Report: grok-4-1-fast-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 5c110486 | **Time:** 49.05s | **Cost:** $0.00607
--------------------------------------------------------------------------------

**Scenario design is a critical component of environmental risk stress testing (particularly for climate-related physical and transition risks), as it directly shapes the quantification of potential losses, resilience assessments, and the resulting calibration of capital adequacy ratios like CET1 under frameworks such as Basel/CRR, ICAAP, and Pillar 2 requirements.[[1]](https://www.eba.europa.eu/sites/default/files/2025-11/170da4c8-9b56-4fb0-ad60-94d433b7e866/Guidelines%20on%20environmental%20scenario%20analysis.pdf)[[2]](https://www.ngfs.net/system/files/import/ngfs/medias/documents/ngfs_guide_scenario_analysis_final.pdf)**

### Key Ways Scenario Design Influences Capital Adequacy Calibration

1. **Severity, Plausibility, and Tail Risk Calibration**:
   - Adverse scenarios are calibrated as severe but plausible "tail events" (e.g., disorderly transitions with abrupt carbon pricing or acute physical shocks like floods), which amplify projected credit losses via higher probability of default (PD), loss given default (LGD), and risk-weighted assets (RWAs). Milder baseline or reference scenarios (continuing current trends) show minimal impacts, while aggressive designs reveal vulnerabilities, prompting higher capital buffers to maintain adequacy post-stress (e.g., ensuring CET1 above 8-10% hurdles).[[1]](https://www.eba.europa.eu/sites/default/files/2025-11/170da4c8-9b56-4fb0-ad60-94d433b7e866/Guidelines%20on%20environmental%20scenario%20analysis.pdf)[[3]](https://www.ecb.europa.eu/press/financial-stability-publications/macroprudential-bulletin/html/ecb.mpbu202511_04.en.html)
   - Overly conservative calibration risks over-capitalization (inefficient), while underestimation (e.g., ignoring tipping points) leads to insufficient buffers, as seen in models where scenario magnitude affects posterior risk beliefs and optimal capital via Kalman-filter-like learning.[[4]](https://pages.stern.nyu.edu/~tphilipp/papers/Parlatore_Philippon_Stress_Tests.pdf)

2. **Inclusion of Risk Types, Drivers, and Transmission Channels**:
   - Designs incorporating both physical (acute/chronic) and transition risks (policy, tech, market), plus compound effects (e.g., recession + floods), propagate shocks through micro (firm-level asset stranding) and macro channels (GDP drags), increasing loss estimates and necessitating recalibration. Omitting value chains or non-climate environmental risks (e.g., biodiversity) understates systemic exposures.[[1]](https://www.eba.europa.eu/sites/default/files/2025-11/170da4c8-9b56-4fb0-ad60-94d433b7e866/Guidelines%20on%20environmental%20scenario%20analysis.pdf)[[2]](https://www.ngfs.net/system/files/import/ngfs/medias/documents/ngfs_guide_scenario_analysis_final.pdf)
   - NGFS pathways matter: "Orderly" (early action, 1.5-2°C) implies gradual adjustments with lower capital strain; "disorderly/hot house" (delayed policy, 3°C+) spikes losses, informing higher Pillar 2 add-ons.[[2]](https://www.ngfs.net/system/files/import/ngfs/medias/documents/ngfs_guide_scenario_analysis_final.pdf)

3. **Horizons, Dynamics, and Granularity**:
   - Short-term climate stress tests (CST, <5 years) focus on capital depletion under constant/dynamic balance sheets, directly calibrating short-term adequacy. Long-term resilience analysis (CRA, >10 years) tests business models, indirectly affecting strategic capital planning.[[1]](https://www.eba.europa.eu/sites/default/files/2025-11/170da4c8-9b56-4fb0-ad60-94d433b7e866/Guidelines%20on%20environmental%20scenario%20analysis.pdf)
   - Granular, portfolio-tailored designs (e.g., sector-specific energy shifts) yield precise impacts versus generic ones, enhancing ICAAP/SREP inputs for calibrated requirements.[[3]](https://www.ecb.europa.eu/press/financial-stability-publications/macroprudential-bulletin/html/ecb.mpbu202511_04.en.html)

### Regulatory Examples
- **EBA Guidelines (2025)**: Institutions must embed environmental scenarios in IRB stress tests and ICAAP, using sources like NGFS/IPCC; results challenge capital adequacy, with proportionality for smaller firms. Poor design risks unreliable quantification, adjusted via expert judgment.[[1]](https://www.eba.europa.eu/sites/default/files/2025-11/170da4c8-9b56-4fb0-ad60-94d433b7e866/Guidelines%20on%20environmental%20scenario%20analysis.pdf)
- **ECB 2025 EU-wide Stress Test**: Adverse scenario + NGFS NDCs adds 74bps (transition) + 77bps (physical floods) CET1 depletion system-wide (total 487bps vs. baseline adverse), highlighting design-driven heterogeneity—e.g., energy-intensive exposures amplify losses, aiding targeted calibration.[[3]](https://www.ecb.europa.eu/press/financial-stability-publications/macroprudential-bulletin/html/ecb.mpbu202511_04.en.html)

### Challenges and Best Practices
- **Challenges**: Data gaps, model uncertainties (e.g., feedback loops), and assumption sensitivity can distort outputs, leading to cautious (non-binding) use in calibration currently (many tests exploratory).[[2]](https://www.ngfs.net/system/files/import/ngfs/medias/documents/ngfs_guide_scenario_analysis_final.pdf)
- **Best Practices**: Multiple coherent scenarios, sensitivity tests, external benchmarking (e.g., NGFS), and forward-looking calibration ensure robust integration into capital frameworks, evolving toward binding requirements (e.g., ECB partial from 2027).[[1]](https://www.eba.europa.eu/sites/default/files/2025-11/170da4c8-9b56-4fb0-ad60-94d433b7e866/Guidelines%20on%20environmental%20scenario%20analysis.pdf)

In summary, robust scenario design enhances the credibility of stress test results, enabling precise calibration that aligns capital with environmental risk materiality, while flawed design risks miscalibration and financial instability.[[4]](https://pages.stern.nyu.edu/~tphilipp/papers/Parlatore_Philippon_Stress_Tests.pdf)

## Annotations (Inline Citations)
Citation [1] (Pos: 367-522): [Web] https://www.eba.europa.eu/sites/default/files/2025-11/170da4c8-9b56-4fb0-ad60-94d433b7e866/Guidelines%20on%20environmental%20scenario%20analysis.pdf
Citation [2] (Pos: 522-630): [Web] https://www.ngfs.net/system/files/import/ngfs/medias/documents/ngfs_guide_scenario_analysis_final.pdf
Citation [1] (Pos: 1317-1472): [Web] https://www.eba.europa.eu/sites/default/files/2025-11/170da4c8-9b56-4fb0-ad60-94d433b7e866/Guidelines%20on%20environmental%20scenario%20analysis.pdf
Citation [3] (Pos: 1472-1599): [Web] https://www.ecb.europa.eu/press/financial-stability-publications/macroprudential-bulletin/html/ecb.mpbu202511_04.en.html
Citation [4] (Pos: 1889-1977): [Web] https://pages.stern.nyu.edu/~tphilipp/papers/Parlatore_Philippon_Stress_Tests.pdf
Citation [1] (Pos: 2459-2614): [Web] https://www.eba.europa.eu/sites/default/files/2025-11/170da4c8-9b56-4fb0-ad60-94d433b7e866/Guidelines%20on%20environmental%20scenario%20analysis.pdf
Citation [2] (Pos: 2614-2722): [Web] https://www.ngfs.net/system/files/import/ngfs/medias/documents/ngfs_guide_scenario_analysis_final.pdf
Citation [2] (Pos: 2934-3042): [Web] https://www.ngfs.net/system/files/import/ngfs/medias/documents/ngfs_guide_scenario_analysis_final.pdf
Citation [1] (Pos: 3367-3522): [Web] https://www.eba.europa.eu/sites/default/files/2025-11/170da4c8-9b56-4fb0-ad60-94d433b7e866/Guidelines%20on%20environmental%20scenario%20analysis.pdf
Citation [3] (Pos: 3702-3829): [Web] https://www.ecb.europa.eu/press/financial-stability-publications/macroprudential-bulletin/html/ecb.mpbu202511_04.en.html
Citation [1] (Pos: 4143-4298): [Web] https://www.eba.europa.eu/sites/default/files/2025-11/170da4c8-9b56-4fb0-ad60-94d433b7e866/Guidelines%20on%20environmental%20scenario%20analysis.pdf
Citation [3] (Pos: 4596-4723): [Web] https://www.ecb.europa.eu/press/financial-stability-publications/macroprudential-bulletin/html/ecb.mpbu202511_04.en.html
Citation [2] (Pos: 4968-5076): [Web] https://www.ngfs.net/system/files/import/ngfs/medias/documents/ngfs_guide_scenario_analysis_final.pdf
Citation [1] (Pos: 5333-5488): [Web] https://www.eba.europa.eu/sites/default/files/2025-11/170da4c8-9b56-4fb0-ad60-94d433b7e866/Guidelines%20on%20environmental%20scenario%20analysis.pdf
Citation [4] (Pos: 5727-5815): [Web] https://pages.stern.nyu.edu/~tphilipp/papers/Parlatore_Philippon_Stress_Tests.pdf


## Sources
[1] https://www.ecb.europa.eu/press/financial-stability-publications/macroprudential-bulletin/html/ecb.mpbu202511_04.en.html
[2] https://www.unepfi.org/wordpress/wp-content/uploads/2025/06/APAC_Policy-brief_climate-risks-financial-regulation.pdf
[3] https://www.bankofengland.co.uk/stress-testing
[4] https://www.suerf.org/wp-content/uploads/2023/11/f_4515167f9a463006c21cd66f2ab2cd73_63709_suerf.pdf
[5] https://en.ccb.com/eng/attachDir/2022/11/2022111821143318876.pdf
[6] https://www.federalreserve.gov/publications/2025-stress-test-scenarios.htm
[7] https://pmc.ncbi.nlm.nih.gov/articles/PMC9703411
[8] https://www.afme.eu/media/mmvhzvzo/afmeclimaterisk202309.pdf
[9] https://www.ecb.europa.eu/pub/pdf/other/ecb.report_fit-for-55_stress_test_exercise~7fec18f3a8.en.pdf
[10] https://zandersgroup.com/en/insights/blog/roundtable-climate-scenario-design-stress-testing-recap
[11] https://www.eba.europa.eu/sites/default/files/2025-11/170da4c8-9b56-4fb0-ad60-94d433b7e866/Guidelines%20on%20environmental%20scenario%20analysis.pdf
[12] https://www.moodys.com/web/en/us/insights/resources/addressing-physical-risk-impacts-in-risk-management-practices.pdf
[13] https://www.unepfi.org/wordpress/wp-content/uploads/2021/12/Good-Practice-Guide-to-Climate-Stress-Testing.pdf
[14] https://www.ngfs.net/system/files/2025-11/Guide%20to%20climate%20scenario%20analysis%20for%20central%20banks%20and%20supervisors%20%E2%80%93%20Update_0.pdf
[15] https://bpi.com/challenges-in-stress-testing-and-climate-change
[16] https://www.fsb.org/uploads/P131022-1.pdf
[17] https://www.bankofengland.co.uk/stress-testing/2022/results-of-the-2021-climate-biennial-exploratory-scenario
[18] https://pages.stern.nyu.edu/jstroebe/PDF/ABEJSZZ_ClimateStressTest.pdf
[19] https://www.ngfs.net/system/files/import/ngfs/medias/documents/ngfs_guide_scenario_analysis_final.pdf
[20] https://www.linkedin.com/pulse/esg-stress-testing-current-state-dr-sunando-roy-smjzf
[21] https://www.bankingsupervision.europa.eu/ecb/pub/pdf/ssm.climate_stress_test_report.20220708~2e3cc0999f.en.pdf
[22] https://connect.cefpro.com/article/view/eba-orders-banks-to-embed-climate-risk-scenario-analysis
[23] https://zandersgroup.com/en/insights/blog/the-ecb-published-the-results-of-its-climate-risk-stress-test
[24] https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr1059.pdf
[25] https://www.bis.org/fsi/publ/insights34.pdf
[26] https://www.isda.org/a/boogE/A-Conceptual-Framework-for-Climate-Scenario-Analysis-in-the-Trading-Book.pdf
[27] https://www.bis.org/bcbs/publ/d572.pdf
[28] https://www.nber.org/system/files/working_papers/w29901/w29901.pdf
[29] https://www.finance-watch.org/policy-portal/sustainable-finance/a-safer-use-of-climate-scenario-analysis-by-banks
[30] https://pages.stern.nyu.edu/~tphilipp/papers/Parlatore_Philippon_Stress_Tests.pdf
[31] https://finance-climact.eu/wp-content/uploads/2021/08/ADEME-2021-Scenario-based-climate-stress-testing-from-risk-analysis-to-modeling.pdf
[32] https://www.dbresearch.com/PROD/RPS_EN-PROD/PROD0000000000526206/Climate_stress_tests:_Are_banks_fit_for_the_green_.PDF
