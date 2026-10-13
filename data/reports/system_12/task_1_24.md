# Deep Research Report: grok-4-1-fast-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 3fdf836c | **Time:** 24.66s | **Cost:** $0.00368
--------------------------------------------------------------------------------

**The second statement is more accurate: historical simulation window selection in VaR models leads to estimation bias under non-stationary distributions.[[1]](https://rady.ucsd.edu/_files/faculty-research/timmermann/estimation-window.pdf)[[2]](https://arxiv.org/pdf/2505.05646)**

Historical simulation (HS) for Value at Risk (VaR) relies on ranking past returns from a fixed lookback window (e.g., 250–500 days) to estimate the loss percentile at a given confidence level (e.g., 99%). This non-parametric method excels at capturing empirical tail risks without distributional assumptions, unlike parametric variance-covariance approaches that assume normality and underperform in fat-tailed markets.[[3]](https://analystprep.com/study-notes/cfa-level-2/compare-the-parametric-variance-covariance-historical-simulation-and-monte-carlo-simulation-methods-for-estimating-var)

However, **window selection creates a classic bias-variance trade-off exacerbated by non-stationarity** (e.g., structural breaks from regime shifts like crises or policy changes):

- **Shorter windows** (e.g., 100–250 days): More responsive to recent dynamics, reducing bias from outdated data, but higher variance/noise and poor tail event capture due to insufficient extremes.[[2]](https://arxiv.org/pdf/2505.05646)[[4]](https://lup.lub.lu.se/student-papers/record/1436974/file/1646978.pdf)
- **Longer windows** (e.g., 500+ days): Smoother estimates (lower variance, better efficiency), but bias from including "stale" pre-break data, underestimating current tail risks in volatile regimes.[[1]](https://rady.ucsd.edu/_files/faculty-research/timmermann/estimation-window.pdf)[[5]](https://www.researchgate.net/publication/222545375_The_Hidden_Dangers_of_Historical_Simulation)

Under non-stationary distributions—common in financial returns—this leads to systematic **estimation bias**, as full historical data contaminates forecasts with irrelevant regimes, causing poor out-of-sample performance (e.g., VaR exceptions clustering).[[6]](https://pdfs.semanticscholar.org/89a3/4524d1de97143cda53772c3740102c72d730.pdf) Studies propose adaptive windows or methods like filtered HS (FHS) with GARCH to mitigate this, but fixed windows remain prone to "lookback bias."[[7]](https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID3037099_code536338.pdf?abstractid=3037099)[[8]](https://arxiv.org/html/2505.05646v1)

The first claim—"optimizing efficiency vs. tail risk capture"—better describes **parametric vs. HS trade-offs** overall: parametric methods are computationally efficient but tail-blind; HS prioritizes tails at efficiency cost. HS itself doesn't inherently "optimize" this via window choice; instead, poor selection amplifies issues.[[9]](https://www.newyorkfed.org/medialibrary/media/research/epr/96v02n1/9604hend.pdf) No sources directly support HS windows as an optimization for that trade-off.[[10]](https://www.sciencedirect.com/science/article/pii/S0377042718306472)

## Annotations (Inline Citations)
Citation [1] (Pos: 154-239): [Web] https://rady.ucsd.edu/_files/faculty-research/timmermann/estimation-window.pdf
Citation [2] (Pos: 239-278): [Web] https://arxiv.org/pdf/2505.05646
Citation [3] (Pos: 701-874): [Web] https://analystprep.com/study-notes/cfa-level-2/compare-the-parametric-variance-covariance-historical-simulation-and-monte-carlo-simulation-methods-for-estimating-var
Citation [2] (Pos: 1254-1293): [Web] https://arxiv.org/pdf/2505.05646
Citation [4] (Pos: 1293-1368): [Web] https://lup.lub.lu.se/student-papers/record/1436974/file/1646978.pdf
Citation [1] (Pos: 1568-1653): [Web] https://rady.ucsd.edu/_files/faculty-research/timmermann/estimation-window.pdf
Citation [5] (Pos: 1653-1754): [Web] https://www.researchgate.net/publication/222545375_The_Hidden_Dangers_of_Historical_Simulation
Citation [6] (Pos: 2010-2095): [Web] https://pdfs.semanticscholar.org/89a3/4524d1de97143cda53772c3740102c72d730.pdf
Citation [7] (Pos: 2242-2339): [Web] https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID3037099_code536338.pdf?abstractid=3037099
Citation [8] (Pos: 2339-2381): [Web] https://arxiv.org/html/2505.05646v1
Citation [9] (Pos: 2715-2801): [Web] https://www.newyorkfed.org/medialibrary/media/research/epr/96v02n1/9604hend.pdf
Citation [10] (Pos: 2879-2954): [Web] https://www.sciencedirect.com/science/article/pii/S0377042718306472


## Sources
[1] https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID3037099_code536338.pdf?abstractid=3037099
[2] https://www.researchgate.net/publication/45137968_Hybrid_Historical_Simulation_VaR_and_ES_Performance_in_Developed_and_Emerging_Markets
[3] https://pmc.ncbi.nlm.nih.gov/articles/PMC11214728
[4] https://www.linkedin.com/pulse/value-risk-var-models-calculations-aakanksha-khare-csm-cspo-dpkkf
[5] https://arxiv.org/pdf/2505.05646
[6] https://arxiv.org/html/2505.05646v1
[7] https://www.researchgate.net/publication/222545375_The_Hidden_Dangers_of_Historical_Simulation
[8] https://analystprep.com/study-notes/cfa-level-2/compare-the-parametric-variance-covariance-historical-simulation-and-monte-carlo-simulation-methods-for-estimating-var
[9] https://msbfile03.usc.edu/digitalmeasures/kenneth.ahern/intellcont/Ahern.SSESE-1.pdf
[10] https://papers.ssrn.com/sol3/Delivery.cfm/5404454.pdf?abstractid=5404454&mirid=1
[11] https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/VAR.pdf
[12] http://arno.uvt.nl/show.cgi?fid=183844
[13] https://pmc.ncbi.nlm.nih.gov/articles/PMC12595044
[14] https://www.mathworks.com/help/risk/value-at-risk-estimation-and-backtesting.html
[15] https://www.thefinanalytics.com/post/introduction-to-value-at-risk-different-methodologies-assumptions-and-limitations
[16] https://www.sciencedirect.com/science/article/abs/pii/S0304407606000418
[17] https://fiveable.me/financial-mathematics/unit-7/risk-var/study-guide/LhDX90LnbjjjCPC3
[18] https://www.nature.com/articles/s41599-024-04221-9
[19] https://pdfs.semanticscholar.org/89a3/4524d1de97143cda53772c3740102c72d730.pdf
[20] https://blog.edda.co/2024/02/22/understanding-value-at-risk-var-models
[21] https://www.crei.cat/wp-content/uploads/users/working-papers/InoueLuRossi.pdf
[22] https://pages.stern.nyu.edu/~rwhitela/papers/hybrid%20risk98.pdf
[23] https://www.sciencedirect.com/science/article/pii/S0377042718306472
[24] https://www.thefinanalytics.com/post/historical-simulation-method-does-it-really-help
[25] https://epublications.vu.lt/object/elaba:229582423/229582423.pdf
[26] https://lup.lub.lu.se/student-papers/record/1436974/file/1646978.pdf
[27] https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID2042594_code1436450.pdf?abstractid=2042594
[28] https://www.tandfonline.com/doi/full/10.1080/10293523.2025.2552592
[29] https://www.newyorkfed.org/medialibrary/media/research/epr/96v02n1/9604hend.pdf
[30] https://edoc.hu-berlin.de/bitstreams/e05b3a27-7667-4251-825b-fda76bc847d7/download
[31] https://web.stanford.edu/class/msande444/2012/MS&E444_2012_Group2a.pdf
[32] https://arxiv.org/html/2505.06383v1
[33] https://www-2.rotman.utoronto.ca/~hull/downloadablepublications/VaR_VolUpdating.pdf
[34] https://www.econstor.eu/bitstream/10419/55232/1/684931540.pdf
[35] https://rady.ucsd.edu/_files/faculty-research/timmermann/estimation-window.pdf
[36] https://www.investopedia.com/terms/v/var.asp
[37] https://www.cryptodatadownload.com/blog/posts/pros-cons-var-lookback-window-length
