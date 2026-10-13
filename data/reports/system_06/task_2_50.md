# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** c11e1f18 | **Time:** 1600.23s | **Cost:** $0.12540
--------------------------------------------------------------------------------

# In ESG Portfolios: Can Factor Model Construction Balance Risk Quantification and Responsibility Standardization, or Does Weighting in Multi-Criteria Analysis Introduce Subjective Bias?

## Abstract

The integration of Environmental, Social, and Governance (ESG) factors into quantitative portfolio construction represents one of the most significant methodological challenges facing modern investment management. This research report examines the fundamental tension between the mathematical rigor demanded by factor model construction and the normative dimensions inherent in responsibility standardization within ESG investing. Through analysis of contemporary portfolio optimization frameworks, multi-criteria decision methodologies, and the documented divergences across ESG rating providers, this report investigates whether factor-based approaches can achieve genuine objectivity in risk quantification while simultaneously standardizing responsibility metrics, or whether the weighting decisions embedded in multi-criteria analysis inevitably introduce subjective biases that undermine the purported objectivity of quantitative ESG portfolios. The findings suggest that while factor models provide powerful frameworks for organizing ESG information and optimizing portfolios across multiple objectives, the fundamental absence of a universal numeraire for non-financial performance means that weighting decisions necessarily reflect subjective value judgments, even when executed through sophisticated mathematical procedures.

## 1. Introduction

The proliferation of ESG investing has fundamentally transformed contemporary portfolio management, with assets under management in ESG-focused strategies reaching unprecedented levels globally. This growth has been accompanied by the development of increasingly sophisticated quantitative frameworks designed to incorporate non-pecuniary ESG preferences into conventional portfolio optimization models [1]. The central promise of these approaches lies in their potential to systematize what has traditionally been considered a subjective and values-based investment philosophy, thereby enabling investors to construct portfolios that simultaneously pursue financial returns and sustainability objectives through rigorous, reproducible methodologies.

However, this promise confronts a fundamental paradox at the heart of ESG portfolio construction. Factor models, which form the mathematical backbone of modern portfolio optimization, derive their analytical power from their ability to reduce complex multidimensional problems to tractable representations amenable to quantitative analysis. Yet ESG factors inherently embody normative judgments about what constitutes responsible corporate behavior, sustainable practices, and good governance—judgments that cannot be reduced to purely technical parameters without losing their essential meaning [2]. The question thus arises: can factor model construction genuinely balance the competing demands of mathematical rigor in risk quantification with the standardization required for meaningful responsibility assessment, or does the weighting process in multi-criteria analysis merely mask subjective biases behind a veneer of quantitative sophistication?

This report addresses this question through systematic examination of three interconnected dimensions of the ESG portfolio construction problem. First, we analyze the methodological foundations of factor-based ESG integration, examining how different approaches to factor model specification affect the resulting portfolio characteristics and performance profiles. Second, we investigate the documented divergences among ESG rating providers and their implications for the standardization of responsibility metrics across different analytical frameworks. Third, we critically evaluate the weighting methodologies employed in multi-criteria decision analysis, assessing the extent to which these procedures introduce subjective biases that may undermine the objectivity claims of quantitative ESG investing.

## 2. Theoretical Framework: Factor Models in ESG Portfolio Construction

### 2.1 The Markowitz Foundation and Its ESG Extensions

The theoretical foundation for quantitative portfolio construction rests upon Harry Markowitz's seminal work on portfolio selection and efficient diversification, which established mean-variance optimization as the central paradigm for investment decision-making under uncertainty [3]. In the traditional Markowitz framework, investors seek to maximize expected utility by selecting portfolios that offer the highest expected return for a given level of risk, or equivalently, the lowest risk for a given level of expected return. The mathematical formulation of this optimization problem yields the familiar efficient frontier, representing the set of non-dominated portfolios that cannot be improved upon in terms of return without accepting additional risk.

The extension of mean-variance optimization to incorporate ESG considerations has proceeded along several distinct methodological paths. The most straightforward approach involves treating ESG scores as additional inputs to the optimization problem, alongside expected returns and volatilities, thereby expanding the dimensionality of the efficient frontier from a curve to a surface [4]. In this tri-criterion Mean-Variance optimization framework, assets are assigned ESG scores in addition to their financial characteristics, and efficient portfolios are identified as those lying on a non-dominated surface rather than the traditional linear efficient frontier. This approach, grounded in Von Neumann-Morgenstern utility theory, allows investors to express preferences over both financial and sustainability dimensions through appropriate utility functions.

The mathematical formulation of this extended optimization problem can be expressed as follows. Given a universe of n assets with expected return vector $\mu$, covariance matrix $\Sigma$, and ESG score vector $e$, the investor's problem is to maximize a utility function $U(\mu_p, \sigma_p, e_p)$ subject to portfolio constraints, where $\mu_p = w^T\mu$, $\sigma_p = \sqrt{w^T\Sigma w}$, and $e_p = w^T e$ represent the portfolio's expected return, risk, and ESG score respectively, with $w$ denoting the weight vector. The solution to this optimization problem yields a set of portfolios that trade off financial performance against ESG performance according to the investor's revealed preferences.

### 2.2 Factor Model Representation and Computational Advantages

The practical implementation of ESG-integrated portfolio optimization confronts the well-known computational challenges associated with high-dimensional covariance matrix estimation, particularly when the number of assets approaches or exceeds the number of observation periods. Factor models offer a powerful solution to this problem by decomposing asset returns into systematic factor exposures and idiosyncratic components, thereby reducing the dimensionality of the estimation problem and accelerating computational performance [1].

In the factor model framework, the return of asset $i$ at time $t$ is expressed as:

$$r_{it} = \alpha_i + \sum_{k=1}^{K} \beta_{ik} F_{kt} + \epsilon_{it}$$

where $F_{kt}$ represents the realization of factor $k$ at time $t$, $\beta_{ik}$ denotes asset $i$'s sensitivity to factor $k$, $\alpha_i$ is the asset-specific intercept, and $\epsilon_{it}$ represents the idiosyncratic return component. When applied to ESG integration, this framework can be extended to include ESG-related factors alongside traditional factors such as market beta, size, value, and momentum.

The computational advantages of factor model-based optimization are substantial. By reducing the problem from estimating an $n \times n$ covariance matrix to estimating $K$ factor loadings and a diagonal idiosyncratic covariance matrix, factor models dramatically reduce input requirements while facilitating understanding and allowing easy adjustment to changing conditions [1]. This tractability advantage has made factor-based approaches particularly attractive for ESG portfolio construction, where the additional dimensionality introduced by sustainability considerations would otherwise render full covariance estimation computationally prohibitive for large asset universes.

### 2.3 Multi-Objective Optimization and Pareto Efficiency

The incorporation of ESG factors into portfolio optimization inherently transforms the problem from a single-objective to a multi-objective optimization problem, where investors must trade off competing goals such as expected return, risk mitigation, and ESG performance. The solution to such problems is not a single optimal portfolio but rather a set of Pareto-efficient portfolios, none of which can be improved in one dimension without sacrificing performance in another [5].

Multi-criteria decision analysis (MCDA) provides the methodological framework for navigating these trade-offs. MCDA approaches to ESG portfolio construction typically employ techniques such as the Analytic Hierarchy Process (AHP) or goal programming to aggregate multiple objectives into a single composite criterion that can be optimized within the standard framework [6]. In the AHP methodology, investors specify pairwise comparisons between objectives, from which relative importance weights are derived through eigenvector decomposition. These weights then parameterize a utility function that combines the various objectives into a single optimization criterion.

The flexibility of MCDA approaches has been recognized as a key advantage for accommodating the heterogeneous preferences of different investor types. Research has demonstrated that the strength of non-pecuniary desires, along with both pecuniary expectations and risk preferences, are important determinants of the optimal portfolio choice, suggesting that no single weighting scheme can serve all investors equally well [1]. This observation has motivated the development of customizable optimization frameworks that allow investors to express their individual preferences through adjustable parameters.

## 3. The Standardization Challenge: Divergence in ESG Ratings

### 3.1 Sources of Rating Divergence

The practical implementation of factor-based ESG portfolio construction confronts a fundamental obstacle: the absence of standardized ESG measurements. Research has extensively documented that different ESG rating providers assign substantially different scores to the same companies, raising profound questions about the meaning and comparability of ESG ratings [2]. This divergence is not merely a matter of minor methodological differences but reflects fundamental disagreements about what ESG performance means, how it should be measured, and what dimensions of corporate behavior are most material.

The sources of this divergence can be categorized into three primary dimensions. First, differences in objectives lead providers to measure fundamentally different concepts: some focus on the ESG impact or performance of a company, while others measure the financial materiality of ESG issues for the company [7]. These different conceptual foundations produce ratings that are not merely scaled differently but actually capture distinct aspects of corporate behavior. Second, differences in methodologies, including the choice of specific indicators, the treatment of missing data, and the functional forms used to aggregate individual metrics into overall scores, introduce additional variation [8]. Third, differences in data sources and treatment, including the integration of qualitative assessments and the handling of controversial events, contribute to rating divergence even when providers share similar conceptual frameworks.

The empirical magnitude of this divergence is striking. Studies have shown that the correlation between ESG scores assigned by different providers to the same companies can be remarkably low, sometimes approaching zero for certain dimensions [2]. This low correlation implies that portfolios constructed using different ESG data providers can exhibit dramatically different characteristics, even when constructed using identical optimization algorithms and stated preference parameters. The implications for standardization are severe: if the same company can receive high scores from one provider and low scores from another, the concept of a standardized ESG rating becomes problematic.

### 3.2 Implications for Portfolio Construction

The divergence among ESG rating providers has direct and consequential implications for factor-based portfolio construction. When different providers produce inconsistent ratings, the factor loadings derived from ESG scores will depend critically on which provider's data is used, leading to different optimal portfolios with different risk and return characteristics [2]. This dependence introduces an additional layer of subjectivity into the portfolio construction process, as the choice of data provider effectively becomes a normative judgment about what ESG performance means.

The problem is compounded by the lack of a clear theoretical basis for preferring one provider's methodology over another. Unlike financial data, which can be validated against realized outcomes such as stock returns or default events, ESG ratings lack such objective validation criteria. The "good" ESG company according to one provider may be the "bad" company according to another, and there is no external standard against which to adjudicate these disagreements [7]. This absence of ground truth means that the choice of ESG data provider is essentially arbitrary from a purely technical standpoint, reflecting the user's implicit value judgments rather than objective measurement.

Research has attempted to address this problem through ensemble approaches that combine ratings from multiple providers. These methods assign weights to different providers' scores and aggregate them into composite ESG measures, thereby reducing dependence on any single provider's methodology [9]. However, the weighting of different providers again introduces subjective judgments: should providers be weighted equally, or should more reputable or more widely-used providers receive higher weights? The ensemble approach thus shifts the locus of subjectivity rather than eliminating it.

### 3.3 Materiality and Context Dependence

A further challenge to standardization arises from the materiality of ESG issues, which varies substantially across industries and contexts. The Sustainability Accounting Standards Board (SASB) has developed industry-specific standards that identify the ESG issues most financially material to companies in each sector, recognizing that environmental issues material to extractive industries may be irrelevant to software companies, and that governance structures appropriate for controlled companies differ from those suitable for widely-held corporations [10].

This materiality dependence complicates factor model construction in several ways. First, it implies that ESG factors cannot be treated as universally comparable across the asset universe; a company with strong environmental performance in a non-material dimension may be appropriately rated lower than a company with weaker environmental performance in a material dimension. Second, it suggests that simple aggregation of ESG scores across dimensions may obscure important information about the specific sustainability issues most relevant to each company. Third, it raises questions about the appropriate treatment of ESG performance in portfolio construction: should investors reward companies for strong performance on material issues, or should they consider performance across all ESG dimensions regardless of materiality?

The empirical evidence on materiality and ESG performance is mixed. Research has found that firms with good scores on material ESG items had an average excess return of 1.7% during the following year, while firms with bad scores had an average negative excess return of -1.4% [10]. However, these differences were not statistically significant in some analyses, and firms with neutral scores sometimes exhibited even higher average excess returns than those with good scores. These findings suggest that the relationship between ESG scores and financial performance is complex and context-dependent, further complicating the standardization of responsibility metrics.

## 4. Weighting Methodologies in Multi-Criteria Analysis

### 4.1 The Problem of Weight Determination

The weighting of criteria in multi-criteria ESG portfolio optimization represents perhaps the most significant source of subjective bias in the construction process. Whether weights are derived through stated preference methods such as surveys and pairwise comparisons, revealed preference methods such as historical optimization, or purely technical methods such as entropy weighting, they inevitably reflect value judgments about the relative importance of different ESG dimensions and their relationship to financial objectives [6].

The mathematical formulation of multi-criteria optimization typically involves a weighted sum of the various objectives. Let $f_1(w)$, $f_2(w)$, ..., $f_m(w)$ represent the $m$ objectives to be optimized (such as expected return, variance, and ESG score), with associated weights $w_1, w_2, ..., w_m$ satisfying $\sum_{i=1}^{m} w_i = 1$. The composite objective function is then:

$$F(w) = \sum_{i=1}^{m} w_i f_i(w)$$

The choice of weights $w_i$ determines the relative emphasis placed on each objective and thus the characteristics of the optimal portfolio. Different weight vectors yield different points on the efficient surface, and there is no objective basis for selecting one weight vector over another; the appropriate weights depend on the investor's individual preferences, which cannot be derived from market data or statistical analysis alone.

This subjectivity is acknowledged in the literature, with researchers noting that "the assignment of weights to ESG factors is somewhat subjective" and that future research should explore different weight configurations to understand their impact on portfolio performance [11]. The challenge is not merely practical but fundamental: the weights represent the investor's value system, which is inherently personal and cannot be reduced to technical parameters.

### 4.2 Analytical Hierarchy Process and Expert Judgment

The Analytic Hierarchy Process (AHP) has been widely applied to ESG portfolio construction as a method for deriving weights from structured pairwise comparisons between criteria [6]. In the AHP framework, investors compare criteria in pairs, indicating which is more important and by how much, using a standardized scale typically ranging from 1 (equal importance) to 9 (extreme importance). These pairwise comparisons are organized into a matrix, from which weights are derived through eigenvector calculation.

The AHP methodology offers several advantages for ESG portfolio construction. It provides a structured and transparent process for eliciting preferences, reduces complex decisions to a series of simpler pairwise comparisons, and yields weights that can be tested for consistency. However, the methodology also introduces potential biases. The choice of comparison scale affects the resulting weights, and research has shown that different scaling approaches can yield substantially different results. Furthermore, the requirement that investors articulate their preferences through explicit comparisons may force artificial precision onto preferences that are inherently vague or uncertain.

The application of AHP to ESG portfolio construction has been extended through the integration of fuzzy set theory, which allows for the representation of imprecise or uncertain judgments [6]. In fuzzy AHP, the pairwise comparisons are represented as fuzzy numbers rather than precise values, reflecting the uncertainty inherent in preference elicitation. The defuzzification process then yields crisp weights that can be used in optimization. While this approach addresses some limitations of classical AHP, it introduces additional parameters and methodological choices that further complicate the analysis.

### 4.3 Machine Learning Approaches to Weight Estimation

Recent research has explored the use of machine learning techniques, particularly artificial neural networks, for estimating optimal portfolio weights in ESG contexts [5]. These approaches treat the weight determination problem as a supervised learning task, where the goal is to learn the relationship between input variables (such as asset characteristics) and output variables (such as optimal portfolio weights) from historical data.

The K4-RANN (Kernel Radial Basis Function Neural Network) represents one such approach, which minimizes a modified sum of squared errors cost function to extract optimal weighting values from training data [5]. The supervised learning function can be expressed as $y = f(x)$, where $y$ is the output vector (optimal weights) and $x$ is the input vector (asset characteristics), with the function approximated through a linear combination of basis functions:

$$f(x) = \sum_{j=1}^{m} w_j h_j(x)$$

where $m$ is the number of basis functions, $h_j$ represents the basis functions, and $w_j$ are the learned weights.

Machine learning approaches offer the potential to discover complex, nonlinear relationships between asset characteristics and optimal portfolio weights that may not be captured by simpler linear models. However, they also introduce new sources of subjectivity, including the choice of network architecture, the selection of training data, and the specification of regularization parameters. Furthermore, the "black box" nature of many machine learning models may obscure the reasoning behind particular weight assignments, reducing the transparency and interpretability of the portfolio construction process.

## 5. The Subjectivity Question: Can Quantitative Methods Achieve Objectivity?

### 5.1 The Illusion of Objectivity

The fundamental tension in ESG portfolio construction arises from the conflation of quantitative rigor with normative objectivity. Factor models and multi-criteria optimization techniques are powerful mathematical tools that can organize complex information, identify efficient portfolios, and facilitate reproducible decision-making. However, the outputs of these models are only as objective as their inputs and assumptions, which inevitably reflect subjective judgments about what factors to include, how to measure them, and how to weight them relative to one another.

This subjectivity is particularly pronounced in the ESG context because the very concept of "responsibility" or "sustainability" is inherently normative. Unlike financial returns, which can be measured in currency and compared across assets using market prices, ESG performance lacks a universal numeraire that would enable objective comparison [7]. When we say that one company has better ESG performance than another, we are making a value judgment that certain corporate behaviors are more desirable than others, and these judgments cannot be derived from data alone but must be specified exogenously by the analyst or investor.

The averaging of ESG scores across portfolio constituents exemplifies this problem. While portfolio-level investment performance can be computed as the arithmetic sum of constituent-level performance, there is no objective exchange value for non-financial performance that would justify averaging constituent ESG scores to represent portfolio-level ESG performance [7]. The choice to average, and the choice of weighting scheme for that averaging, are subjective decisions that reflect the analyst's implicit value system.

### 5.2 The Case for Methodological Transparency

Given the inherent subjectivity in ESG portfolio construction, the most honest and defensible approach may be to embrace transparency rather than to claim false objectivity. This involves clearly documenting all methodological choices, including the selection of ESG data providers, the specification of factor models, the derivation of weights, and the optimization procedures employed. By making these choices explicit, analysts enable investors to understand the normative assumptions embedded in their portfolios and to evaluate whether these assumptions align with their own values.

The Task Force on Climate-related Financial Disclosures (TCFD) framework represents one effort to standardize disclosure practices and enhance transparency in ESG-related information [12]. By adopting TCFD recommendations, companies can provide investors with the information needed to assess climate-related risks and opportunities in their investment decisions. However, standardization of disclosure does not imply standardization of interpretation; different investors may draw different conclusions from the same disclosed information based on their individual preferences and risk tolerances.

Research has proposed frameworks that explicitly acknowledge the subjective dimensions of ESG portfolio construction while providing tools for investors to express their individual preferences. The parameter $\lambda$ in ensemble ESG scoring models represents one such approach, where higher values of $\lambda$ indicate greater emphasis on ESG objectives relative to financial returns [9]. By making this parameter explicit and adjustable, the framework allows investors to tailor portfolio construction to their individual preferences while acknowledging that there is no objectively correct setting.

### 5.3 Limitations of Quantitative Approaches

The limitations of purely quantitative approaches to ESG portfolio construction extend beyond the weighting problem to encompass fundamental challenges in ESG measurement and analysis. ESG data quality remains a significant concern, with gaps, inconsistencies, and inaccuracies in company-reported information creating noise that can obscure true differences in corporate sustainability performance [13]. Companies may report incomplete or non-standardized information, making cross-company comparison difficult and potentially introducing survivorship bias into ESG databases.

The temporal dimension of ESG performance presents additional challenges. Some ESG ratings may not adequately capture long-term sustainability trends or risks, as they rely on historical data or focus on near-term metrics [13]. This short-term focus can lead to portfolios that appear ESG-compliant in the short run but fail to address long-term sustainability challenges. The development of forward-looking ESG indicators, incorporating scenario analysis and trend extrapolation, represents an active area of research but remains methodologically challenging.

Finally, the relationship between ESG factors and financial performance remains contested. While some studies have found significant positive relationships between ESG scores and risk-adjusted returns, others have found weak or insignificant relationships [10]. The mixed evidence suggests that ESG integration may enhance portfolio performance under certain conditions but not others, and that the benefits of ESG integration may depend on market conditions, factor exposures, and the specific ESG metrics employed.

## 6. Practical Implications for Portfolio Construction

### 6.1 Balancing Rigor and Responsibility

The evidence reviewed in this report suggests that factor model construction cannot fully eliminate subjective bias from ESG portfolio construction; rather, it can only relocate and potentially obscure such bias through technical procedures. The weighting decisions inherent in multi-criteria analysis necessarily reflect value judgments about the relative importance of different ESG dimensions and their relationship to financial objectives. However, this does not imply that quantitative approaches are worthless or that ESG portfolio construction is purely arbitrary.

The value of factor-based approaches lies in their ability to organize complex multidimensional information in a tractable and transparent framework. By making explicit the trade-offs between financial and sustainability objectives, these approaches enable investors to understand the implications of their choices and to select portfolios that align with their preferences. The mathematical rigor of factor models does not guarantee objectivity, but it does provide a common language for discussing portfolio construction decisions and comparing alternative approaches.

Practitioners should approach ESG portfolio construction with an awareness of its inherent limitations and an commitment to transparency about methodological choices. This includes clear documentation of data sources, factor specifications, weighting methodologies, and optimization procedures. It also includes acknowledgment of the uncertainty surrounding ESG measurements and the sensitivity of results to methodological choices.

### 6.2 Recommendations for Practice

Based on the analysis presented in this report, several recommendations can be offered for practitioners engaged in ESG portfolio construction. First, practitioners should recognize that the choice of ESG data provider is a consequential normative decision that will significantly affect portfolio characteristics. Different providers use different methodologies and produce different ratings, and practitioners should understand the implications of their provider choice for portfolio composition.

Second, practitioners should employ sensitivity analysis to assess how portfolio characteristics vary with different weighting assumptions. By examining how optimal portfolios change as weights on ESG factors are varied, practitioners can gain insight into the robustness of their portfolios to methodological choices and can identify threshold values at which portfolio composition changes substantially.

Third, practitioners should consider ensemble approaches that combine ratings from multiple providers, thereby reducing dependence on any single provider's methodology. While ensemble approaches do not eliminate subjectivity—they merely shift it to the weighting of different providers—they can produce more stable and diversified ESG portfolios.

Fourth, practitioners should maintain awareness of the limitations of ESG data, including measurement gaps, rating divergence, and short-term focus. ESG ratings are imperfect proxies for corporate sustainability performance, and portfolios constructed using these ratings will inherit these imperfections.

## 7. Conclusion

The question of whether factor model construction can balance risk quantification and responsibility standardization in ESG portfolios admits no simple affirmative or negative answer. Factor models and multi-criteria optimization techniques provide powerful frameworks for organizing ESG information and identifying portfolios that trade off financial and sustainability objectives according to specified preferences. These approaches offer computational tractability, analytical transparency, and the potential for reproducible decision-making that purely qualitative approaches cannot match.

However, the fundamental absence of a universal numeraire for non-financial performance means that weighting decisions in multi-criteria analysis inevitably reflect subjective value judgments, even when executed through sophisticated mathematical procedures. The divergence among ESG rating providers further complicates standardization, as different providers measure fundamentally different concepts using different methodologies. The choice of data provider, the specification of factor models, and the determination of weights all represent normative decisions that cannot be resolved through technical analysis alone.

The most defensible approach to ESG portfolio construction is therefore one that embraces transparency about methodological choices and acknowledges the inherent subjectivity of the enterprise. Rather than claiming false objectivity, practitioners should recognize that quantitative methods are tools for implementing value-based decisions, not substitutes for them. Factor models can help investors understand the implications of their values and select portfolios that align with their preferences, but they cannot determine what those preferences should be.

The integration of ESG factors into portfolio construction represents a genuine advance in investment practice, enabling investors to pursue sustainability objectives alongside financial returns through systematic and transparent methodologies. However, this advance should not be confused with the achievement of objective measurement or standardized responsibility metrics. The responsibility dimension of ESG investing remains fundamentally normative, and any attempt to reduce it to purely technical procedures will necessarily obscure rather than eliminate the value judgments at its core.

---

## References

[1] Quantpedia. "ESG Factor Investing Strategy." https://quantpedia.com/strategies/esg-factor-investing-strategy

[2] Research Affiliates. "What a Difference an ESG Ratings Provider Makes." https://www.researchaffiliates.com/content/dam/ra/publications/pdf/770-what-a-difference-an-esg-ratings-provider-makes.pdf

[3] Markowitz, H. M. (1959). Portfolio Selection: Efficient Diversification of Investments. New Jersey: Wiley.

[4] Utz, S., et al. (2014). Tri-criterion Mean-Variance Optimization Approach. In Zuber (2017) CSP Thesis.

[5] Dash, M., Kajiji, N. "Multiobjective Behavioral Portfolio Selection with Efficient ESG Factors and Learning Network Estimation of Asset Returns." http://wp.lancs.ac.uk/fofi2020/files/2020/04/FoFI-2020-123-Gordon-Dash-Jr.pdf

[6] Nature. "Multi-criteria Optimization with Fuzzy Sets and AHP." https://www.nature.com/articles/s41598-025-24242-x

[7] Castle Hall Diligence. "Scoring Against ESG: Avoiding Pitfalls in ESG Scores." https://www.castlehalldiligence.com/hubfs/scoring-against-esg-avoiding-pitfalls-esg-scores.pdf

[8] Carbon Collective. "Sustainable Investing: ESG Portfolio." https://www.carboncollective.co/sustainable-investing/esg-portfolio

[9] arXiv. "Ensemble Strategies for ESG Scores." https://arxiv.org/html/2310.02163v3

[10] PGIM Quantitative Analysis. "Integrating ESG in Portfolio Construction." https://cdn.pficdn.com/cms/pgimquantsolutions/sites/default/files/static_files/pdf/QMA_Integrating_ESG_in_Portfolio_Construction.pdf

[11] Scitepress. "ESG Factors in Portfolio Optimization." https://www.scitepress.org/Papers/2024/132692/132692.pdf

[12] TCFD. "Task Force on Climate-related Financial Disclosures Recommendations."

[13] University of Zurich. "ESG Integration in Portfolio Optimization." https://www.sustainablefinance.uzh.ch/dam/jcr:6ed587e5-dcfc-47d7-a638-c44f33ee0ce2/Zuber_2017_CSPThesis_23.pdf

## Annotations


## Sources
[1] http://wp.lancs.ac.uk/fofi2020/files/2020/04/FoFI-2020-123-Gordon-Dash-Jr.pdf
[2] https://arxiv.org/html/2310.02163v3
[3] https://cdn.pficdn.com/cms/pgimquantsolutions/sites/default/files/static_files/pdf/QMA_Integrating_ESG_in_Portfolio_Construction.pdf
[4] https://colchesterglobal.com/wp-content/uploads/Guidance-and-Case-Studies-for-ESG-integration-Equities-and-Fixed-Income.pdf
[5] https://portal.s1.spglobal.com/survey/documents/spglobal_esg_scores_methodology.pdf
[6] https://quantpedia.com/strategies/esg-factor-investing-strategy
[7] https://www.carboncollective.co/sustainable-investing/esg-portfolio
[8] https://www.castlehalldiligence.com/hubfs/scoring-against-esg-avoiding-pitfalls-esg-scores.pdf
[9] https://www.cibcassetmanagement.com/email/assets/documents/pdfs/Integrating-ESG-Risk-Analysis_en.pdf
[10] https://www.financialplanningassociation.org/learning/publications/journal/JUN24-how-incorporate-esg-investing-your-practice-OPEN
[11] https://www.invesco.com/content/dam/invesco/apac/en/pdf/insights/2021/december/The-Influence-of-ESG-on-FI-Portfolio-Manager-Behavior.pdf
[12] https://www.lseg.com/content/dam/data-analytics/en_us/documents/methodology/lseg-esg-factor-in-methodology.pdf
[13] https://www.lseg.com/content/dam/lseg/en_us/documents/sustainability/lseg-esg-journal-article-made-to-measure.pdf
[14] https://www.metzler.com/downloads/Metzler/Download-Dokumente-MAM/Nachhaltigkeit/MAM-MSCI-ESG-Corporate-Ratings-Methodology-202306.pdf
[15] https://www.nature.com/articles/s41598-025-24242-x
[16] https://www.oecd.org/content/dam/oecd/en/publications/reports/2020/09/esg-investing_c93cbb7b/5504598c-en.pdf
[17] https://www.researchaffiliates.com/content/dam/ra/publications/pdf/770-what-a-difference-an-esg-ratings-provider-makes.pdf
[18] https://www.sbs.ox.ac.uk/sites/default/files/2023-01/ESG_Modelling_Framework_Working_Paper.pdf
[19] https://www.scitepress.org/Papers/2024/132692/132692.pdf
[20] https://www.shs-conferences.org/articles/shsconf/pdf/2025/16/shsconf_icfmde2025_03026.pdf
[21] https://www.sustainablefinance.uzh.ch/dam/jcr:6ed587e5-dcfc-47d7-a638-c44f33ee0ce2/Zuber_2017_CSPThesis_23.pdf
[22] https://www.theeconomicsjournal.com/article/view/434/7-2-123
[23] https://www.top1000funds.com/wp-content/uploads/2013/01/Optimizing-ESG-Factors-in-Portfolio-Construction.pdf