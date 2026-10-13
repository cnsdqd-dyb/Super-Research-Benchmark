# Deep Research Report: perplexity/sonar-deep-research
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** bf8798a3 | **Time:** 96.46s | **Cost:** $1.16577
--------------------------------------------------------------------------------

# The Temporal Function of Rating Correction in Seller Reputation Systems: Mathematical Models and Practical Implementation

The temporal dimension of seller reputation systems represents one of the most critical yet often overlooked aspects of online marketplace design. Rather than treating all seller feedback as equally valuable regardless of when it was generated, modern reputation systems employ sophisticated temporal functions that systematically adjust the weight and impact of ratings based on their age. This comprehensive analysis examines how temporal functions determine rating correction across diverse e-commerce platforms, the mathematical foundations underlying these systems, and the profound implications for market efficiency and seller behavior.

## The Mathematical Foundations of Temporal Rating Adjustment

### Exponential Decay Functions and Half-Life Models

The most prevalent approach to temporal rating correction employs **exponential decay functions**, which dramatically reduce the weight of older ratings while preserving the influence of recent feedback[2][5][30]. The fundamental mathematical principle underlying these systems can be expressed through the formula \( \text{Credit}(t) = e^{-kt} \)[2], where t represents time elapsed since the rating was submitted and k represents the decay constant that determines the rate at which credit diminishes[5]. This exponential decay model reflects a psychological principle known as **recency bias**, wherein humans naturally weight recent experiences more heavily than distant historical events[16][21].

The concept of "half-life" provides a more intuitive measure of how temporal correction functions operate in practice[2][5]. A half-life represents the time period required for a rating's contribution to decline to exactly 50% of its original weight[2][5]. For instance, Google Analytics implements a default 7-day half-life in its time decay attribution model[2], meaning that a rating provided seven days ago retains only half the influence it would have had if submitted immediately before a conversion event. This half-life approach translates the abstract exponential decay mathematics into practical, measurable terms that platform designers can calibrate to match their specific business cycles and customer behaviors[2].

The mathematical relationship between half-life and decay is governed by the formula that connects these two concepts[5][30]. If we denote the half-life as h, then the decay constant k can be calculated as k equals the natural logarithm of 2 divided by h. This means that platforms can easily switch between thinking about decay in terms of abstract decay constants and intuitive half-life periods. Different industries standardize on different half-life periods: B2B SaaS platforms typically employ 14- to 30-day half-lives to reflect extended evaluation cycles[2][30], while e-commerce platforms generally use 3- to 7-day windows to match rapid consumer purchase decisions[2][30]. Luxury goods and high-consideration purchases often stretch to 45- to 60-day half-lives[2][30].

### Fixed Time Windows and Lookback Periods

Beyond exponential decay functions, many platforms employ simpler temporal correction mechanisms using fixed time windows or "lookback periods." eBay explicitly calculates seller feedback based only on the preceding 12 months, completely excluding all older feedback from the calculation of overall feedback percentages[32][35]. Under this system, a seller with 100 positive ratings from the past year and 10 from before that period would have a feedback score calculated using only the 100 recent positives, effectively zeroing out the historical record outside the window[32]. This creates a discontinuous temporal correction where ratings suddenly cease to influence the metric once they exceed the threshold age.

Similarly, Taobao's Dynamic Score Rating (DSR) system uses a 180-day weighted average across three key dimensions: consistency with product descriptions, seller service attitude, and logistics service quality[33]. All scores derive from a weighted average calculated across this fixed half-year window[33]. The advantage of fixed time windows lies in their simplicity and computational efficiency. They provide clear temporal boundaries that sellers can understand and predict. However, they create artificial discontinuities at the window boundary—a rating that falls outside the window discontinuously drops to zero weight, whereas under continuous exponential decay, older ratings gradually fade into insignificance[5].

## Platform-Specific Temporal Rating Correction Mechanisms

### eBay's Reputation Dynamics and Temporal Thresholding

eBay's reputation system provides a foundational case study in how temporal functions determine rating correction. The platform divides feedback into three categories—positive, negative, and neutral—and calculates an overall percentage based exclusively on transactions from the preceding 12 months[32]. When eBay receives feedback for a seller, the system immediately updates the seller's reputation score by adding or subtracting to their feedback count within the current time window[32]. However, this system creates interesting temporal dynamics because the feedback percentage automatically improves over time as older negative ratings age beyond the 12-month threshold[32].

Research on eBay's dynamics reveals the profound behavioral implications of this temporal structure. When sellers receive their first negative rating, their reputation decreases substantially, and empirical evidence demonstrates that this immediately triggers a decline in seller effort[1][17]. Following the receipt of a first negative feedback, seller transaction growth rates plummet from approximately positive 7% per week to negative 7% per week[1]. Moreover, the rate at which subsequent negative feedback arrives approximately doubles following an initial negative rating[1]. This creates a self-reinforcing negative dynamic where temporal reputation correction interacts with seller behavioral response.

The temporal dimension of eBay's system creates strategic incentives around reputation building. Empirical findings indicate that a 10-fold increase in a seller's transaction record length correlates with an 18 to 27% lower probability of exit from the platform[1]. However, the temporal aspect of the 12-month lookback window means that sellers can theoretically recover from temporary performance declines if they can improve sufficiently to wash out the old negative ratings. This temporal structure provides what economists call an "incentive compatibility" condition—it rewards recent good behavior while not permanently punishing ancient mistakes[3].

### Amazon's Machine Learning Temporal Weighting

Amazon employs a considerably more sophisticated temporal correction mechanism than simple fixed time windows. Rather than explicitly disclosing its algorithm, Amazon states that it assigns more significance to recent reviews to reflect the current state of products[31][34]. Analysis of Amazon's algorithm suggests that the platform uses a machine learning model that incorporates multiple factors including review age, whether ratings come from verified purchasers, reviewer trustworthiness, and other undisclosed factors[34]. The temporal component appears to implement an exponential decay function, though the exact decay rate remains proprietary[31].

Empirically, sellers report observing dramatic differences in how negative reviews impact overall ratings depending on review recency[31]. Older negative reviews appear to contribute progressively less to the overall rating as they age, while newer negative reviews can cause sharp rating declines[31]. One documented case illustrates this dynamic: a product with a 4.3 rating for years suddenly dropped to 4.2 when hit with a burst of negative reviews, suggesting that the temporal correction function amplifies the impact of recent negative feedback[31][34].

Amazon's approach also reveals an important principle: negative reviews appear to have asymmetrically greater weight in the temporal correction than positive reviews[31]. One seller reported that a single 1-star review without even a written explanation dropped their rating by 0.3 points, while four subsequent 5-star verified reviews with detailed explanations failed to restore that 0.3-point loss[34]. This asymmetry suggests that Amazon's temporal correction function may implement different decay rates or initial weight multipliers for negative versus positive feedback, prioritizing the platform's goal of identifying problematic products.

### Airbnb's Temporal Trust Metrics and Recency Prioritization

Airbnb implements what can be understood as a "temporal trust metric" system that explicitly prioritizes recency in its algorithmic ranking[19]. According to detailed analysis of Airbnb's algorithm, the platform weights recent reviews and ratings much more heavily than historical performance[19]. The concept of "temporal trust metrics," which are described as "much more fast spinning" than longer-term metrics[19], suggests that Airbnb implements a decay function with a relatively steep gradient—recent performance changes rapidly affect trust signals.

This temporal approach interacts with Airbnb's broader algorithmic philosophy around "right fitting," which emphasizes matching guests to the precise property that best suits their needs rather than simply promoting the highest-rated properties[19]. The temporal correction function enables this goal by ensuring that a property that has deteriorated in quality will quickly lose algorithmic visibility as its recent reviews reflect lower satisfaction. Conversely, a property that has recently improved under new management can quickly regain visibility as positive recent ratings accumulate[19].

### Taobao's 180-Day Rolling Window with Dimensional Weighting

Taobao's DSR system employs a fixed 180-day rolling window, but adds sophistication through dimensional weighting[33]. The three core dimensions—consistency with product descriptions, seller service attitude, and logistics service quality—are derived as weighted averages across all real transactions in the preceding 180 days[33]. Critically, these scores are immutable even if sellers delete product links, ensuring that historical performance data persists in system calculations to maintain objectivity[33]. This creates a temporal correction function that operates within a defined window but preserves complete historical continuity within that window.

Research on Taobao's system reveals that sellers with scores below 4.9 warrant particular scrutiny, but more importantly, deviations from industry averages within each dimension signal systemic issues[33]. A seller whose consistency with product descriptions indicator falls 20 percentage points below industry average may indicate authentication or quality control problems[33]. The temporal correction function in Taobao's system thus operates at two levels: within the 180-day window, all transactions receive equal treatment in the weighted average calculation, but the system highlights how temporal patterns in performance relative to peer benchmarks reveal quality trends[33].

## The Behavioral Mechanisms Connecting Temporal Correction to Seller Performance

### End-Game Effects and Reputation Milking

The temporal structure of reputation correction systems creates what economists call "end-game effects," wherein sellers anticipate their departure from a platform and deliberately reduce effort to exploit accumulated reputation before exiting[4]. These dynamics become particularly acute when sellers can see temporal correction approaching its boundaries. For instance, if a seller knows their performance is declining and anticipates future negative ratings, the temporal structure of the reputation system creates incentives to "milk" their reputation—deliberately providing low-quality service to reduce costs while the reputation penalty from recent transactions is not yet visible due to the temporal correction delay[4].

Research examining housing platform regulations exploited an exogenous shock to test for end-game effects[4]. The implementation of housing regulations created a temporary increase in platform exits, allowing researchers to compare the behavior of sellers who anticipated departure versus those who did not. Findings indicated that sellers who could anticipate their exit were significantly more likely to reduce effort and quality, thereby receiving more negative ratings[4]. This pattern demonstrates that temporal correction mechanisms do not simply measure past performance—they actively shape present seller behavior by creating incentives around the timing of negative feedback[4].

The mechanism works as follows: a seller facing imminent exit recognizes that any negative feedback they receive now will eventually age beyond the temporal correction window. If the seller exits before sufficient time passes for the reputation to recover through positive transactions, the temporary reputation damage becomes essentially irrelevant to their next identity or platform. This converts the temporal correction function from an incentive device promoting long-term quality into a perverse incentive for short-term exploitation when sellers anticipate platform exit[4].

### Recency Bias and Psychological Distance Effects

The temporal correction function in reputation systems interacts with fundamental cognitive biases in how consumers evaluate products and sellers. **Recency bias** describes the psychological tendency to weight recent events more heavily than distant events when making judgments[16][21]. This bias operates at multiple levels: consumers naturally focus more on recent reviews when reading feedback[16], managers conducting performance reviews systematically overweight recent events[21][24], and survey respondents give more credence to recent information[21].

Research measuring temporal weighting functions across choice domains found remarkably consistent patterns where people display strong recency bias and modest primacy bias[16]. This cognitive reality provides justification for temporal correction functions that exponentially weight recent ratings. However, the research also reveals individual differences in temporal weighting—some people show stronger recency effects than others, creating potential concerns about whether platform-wide temporal corrections truly match user preferences[16].

The psychological effect of temporal distance extends beyond simple recency bias. Construal Level Theory suggests that events at greater temporal distance are processed at higher, more abstract levels, while proximal events engage concrete processing[53]. In the context of e-commerce, this predicts that consumers will rate recent delivery failures more harshly than identical failures that occurred in the distant past, even if the products themselves performed identically[53]. Empirical evidence from e-commerce delivery research confirms this prediction: late deliveries are rated more negatively when the temporal distance between delivery and review posting is small, with the effect diminishing substantially as temporal distance increases[53].

## Dynamic Adjustment and Adaptive Decay Mechanisms

### Information Decay and Predictive Modeling

Beyond simple exponential decay, advanced reputation systems employ "information decay" functions that track not just the age of ratings but the evolving relevance of information they contain[44]. Information decay recognizes that older information about seller quality becomes systematically less predictive of current quality as operational circumstances change. A seller's performance from two years ago may have low relevance if the seller has since restructured operations, changed logistics providers, or modified sourcing[44].

Research on information decay in predictive modeling demonstrates that incorporating temporal decay functions substantially improves forecast accuracy for future seller behavior[44]. Decision tree classifiers built using information decay techniques outperform those built without temporal adjustments, with improvements in precision and recall metrics[44]. This suggests that the temporal correction function should ideally weight recent data not just because consumers psychologically prefer recency, but because recent data truly contains more predictive signal about future performance[44].

### Adaptive Temporal Priors in Bayesian Systems

Sophisticated reputation systems employ Bayesian frameworks that implement temporal corrections through prior specifications[26][37]. In these systems, the prior represents initial beliefs about seller quality before observing any current ratings, while subsequent ratings update these beliefs through Bayes' rule. The strength of the prior—how much initial belief persists against new evidence—directly determines the temporal correction function's characteristics[26][37].

A stronger prior leads to more modest posterior updates when new ratings arrive, effectively downweighting recent feedback relative to the prior belief[26][37]. This creates a form of temporal correction where older beliefs (encoded in the prior) receive more weight, slowing the system's response to recent changes. Conversely, a weaker prior with lower prior strength allows recent ratings to dramatically shift overall quality assessments, implementing a form of temporal correction that emphasizes recency[26][37].

Through calibrated simulations on 19 real-world datasets from large online platforms, researchers demonstrated that prior strength directly mediates the trade-off between **efficiency** (how quickly the system learns true quality) and **producer fairness** (how much variance exists in outcomes for producers of similar quality)[26][37]. Stronger priors reduce variance in producer outcomes by making it difficult for noisy early ratings to dramatically affect quality estimates, thereby increasing fairness[26][37]. However, this comes at the cost of efficiency—the platform learns true quality more slowly, and high-quality products cannot as quickly achieve visibility[26][37].

## Integration with Multi-Dimensional Rating Architectures

### Weighted Multi-Criteria Systems and Temporal Weighting

Modern marketplace reputation systems rarely employ single-dimensional ratings. Instead, they implement multi-dimensional rating structures where different aspects of seller performance—communication speed, product quality, shipping speed, etc.—receive separate ratings that combine into an overall quality assessment. The temporal correction function must operate coherently across all these dimensions.

G2's research scoring methodology provides a sophisticated example of this multidimensional approach[20][59]. G2 calculates overall satisfaction scores using weighted combinations that incorporate review recency, the amount of feedback provided in each review, reviewer attribution, verification status, and community engagement metrics[20][59]. The recency weighting applies not uniformly but proportionally to each review's contribution, with more recent reviews receiving substantially higher weights[20][59].

When platforms employ truly granular feedback systems—such as five-point scales rather than binary feedback—the temporal correction function must account for how information granularity evolves over time[18]. Research on feedback aggregation and prediction demonstrates that as feedback granularity increases, sophisticated aggregation methods that go beyond simple averaging become increasingly valuable for predicting population-level distributions[18]. Temporal functions interact with this granularity effect: a temporal correction function appropriate for binary feedback may not optimally weight five-point scale feedback where individual raters employ different calibration strategies[18].

### Time-Aware Recommendation and Collaborative Filtering

When reputation data feeds into collaborative filtering or recommendation algorithms, the temporal correction function determines how historical user preferences influence current predictions. Time-aware collaborative filtering systems typically incorporate temporal recency through decay functions applied either in the neighborhood determination phase (which user-user similarities to consider) or in the rating aggregation phase (how much weight to give past ratings)[38]. Research comparing these approaches found that temporal recency often improves recommendation accuracy, with optimal time decay functions varying by dataset and application[7][10][15][27].

The mathematics of time-aware collaborative filtering illustrates how temporal correction propagates through complex algorithmic systems[38]. When predicting user A's rating for item i, systems consider historically similar users' ratings weighted by both their similarity to user A and the temporal recency of those ratings. The temporal weighting typically follows exponential decay: \( w_{\text{temporal}}(t) = e^{-\lambda t} \) where t is time elapsed and λ is the decay parameter[38]. Combining temporal and similarity weighting creates interactions where very recent ratings from dissimilar users may receive more weight than older ratings from highly similar users, fundamentally altering what the collaborative filtering system learns about quality[38].

## Dealing with Rating System Pathologies and Temporal Manipulation

### Reputation Inflation and Temporal Dynamics

Detailed empirical analysis across five online marketplaces reveals systematic increases in average feedback scores over time, what researchers term "reputation inflation"[60]. In one focal marketplace—an online labor platform—the fraction of workers receiving perfect 5-star ratings increased from 33% to 85% over a six-year period[60]. This represents not improved quality (which would be difficult for 52 percentage points of workers to simultaneously achieve) but rather systematic changes in how raters assign scores[60].

The temporal dynamics of reputation inflation deserve careful attention. The inflation appears to accelerate in periods where the temporal correction function most rewards recent ratings[60]. When newer ratings dominate quality assessments through strong temporal correction functions, raters may gradually learn to assign higher ratings as social norms shift. What was once considered "good enough" for a 4-star rating becomes normalized as 3-star territory[60].

### Review Verification and Temporal Authenticity

To combat temporal manipulation of reputation systems, platforms increasingly implement review verification mechanisms that interact with temporal corrections[51]. Systems that restrict review posting to narrow time windows following purchase—typically 7 to 30 days post-service—prevent raters from posting reviews months or years later when they might have forgotten specific details[51]. These time windows create a form of temporal correction at the input stage, ensuring that ratings reflect relatively fresh memories[51].

The temporal structure of review authenticity interacts with decay functions in complex ways. Research on delivery performance and review timing demonstrated that the temporal distance between delivery and review posting significantly affects the rating provided[53]. Late deliveries receive progressively less harsh ratings as temporal distance increases, suggesting that memory decay and psychological adjustment reduce the sting of past problems[53]. This creates a temporal correction function operating through psychological mechanisms: the same late delivery receives more negative reviews when assessed immediately versus weeks later[53].

### Temporal Markers and Persuasion Effects

Recent research on how temporal context influences persuasion reveals that consumers discount the persuasive impact of reviews based on how long ago they were posted[12]. The same review presented as "posted yesterday" versus "posted six months ago" produces systematically different persuasion effects, with older reviews losing influence not just through algorithmic weighting but through reduced cognitive impact on readers[12]. This suggests that temporal correction functions in reputation systems align with actual user information processing rather than imposing arbitrary weighting.

## Emerging Temporal Correction Mechanisms and Future Directions

### Trust Decay Functions in Dynamic Environments

Next-generation reputation systems employ "trust decay-based temporal learning" frameworks that adaptively update decay rates in response to changing marketplace conditions[47]. Rather than fixed decay constants or half-lives, these systems learn decay parameters from data, recognizing that different seller types, product categories, or market phases may require different temporal correction functions[47]. A new seller entering the market might warrant slower decay—giving them more time to prove themselves—while established sellers with sudden performance drops might require rapid temporal adjustment to reflect likely quality deterioration.

### Algorithmic Bias in Temporal Corrections

The deployment of temporal correction functions raises important concerns about algorithmic bias in reputation systems[45][46]. When algorithms automatically weight recent information more heavily, they may systematically disadvantage sellers or workers who face temporary adverse circumstances. A seller experiencing one week of shipment delays due to logistics partner failure might see their reputation damaged persistently if the temporal correction function implements the wrong decay parameters[45]. Similarly, performance review algorithms that overweight recent events systematically penalize individuals experiencing temporary performance dips while rewarding those whose trajectories are trending upward[21][24][46].

Advanced bias detection systems analyze performance ratings across demographic groups to identify potential systematic differences that may reflect algorithmic bias rather than real performance differences[46]. When temporal correction functions produce significantly different rating trajectories across demographic groups, this may indicate temporal weighting parameters that require adjustment. For instance, if ratings for sellers in certain regions systematically decline faster under the temporal correction function, this might reveal bias in the decay parameters[46].

## Synthesis and Strategic Implications

The temporal function determining rating correction in seller reputation systems represents far more than a technical implementation detail. These functions embody fundamental choices about how to balance multiple competing objectives: rewarding recent good behavior versus providing long-term incentive stability, enabling rapid market learning about quality changes versus protecting sellers from temporary adverse events, and promoting consumer information needs for current quality signals versus maintaining reputation fairness for all sellers.

The mathematical sophistication ranges from simple fixed time windows—where ratings older than 12 months completely cease influencing assessments—through exponential decay functions that gradually reduce older ratings' influence, to Bayesian prior systems where decay parameters adapt to marketplace conditions. Each approach creates different incentive structures for seller behavior, different fairness implications for rating outcomes, and different information properties for quality learning[1][2][3][4][26][37].

Empirical research demonstrates that temporal correction functions powerfully shape marketplace equilibrium outcomes. When sellers receive first negative ratings, the temporal dynamics of reputation systems determine whether they persist in quality provision or exit the platform entirely[1]. When platforms employ strong temporal correction emphasizing very recent ratings, the system accelerates its ability to identify quality changes but increases variance in seller outcomes, potentially unfairly penalizing good sellers experiencing temporary difficulties[26][37]. When platforms employ weak temporal correction with strong priors, the system provides greater stability and fairness but at the cost of slower learning about true quality changes[26][37].

The optimal temporal correction function depends fundamentally on market context. Fast-moving e-commerce with 3- to 7-day purchase decision cycles requires different temporal functions than enterprise software with 6- to 18-month sales cycles[2][5]. Labor markets where workers complete discrete projects require different temporal functions than long-term employee relationships[16][60]. The temporal function must align with the actual time scale of the market process being supported.

Future reputation system design must contend with increasingly sophisticated temporal manipulation attempts, algorithmic bias in temporal weighting, and the psychological reality of recency bias in both consumer decision-making and system design. As artificial intelligence increasingly structures these systems, the temporal correction function becomes an important point of intervention for ensuring fairness, efficiency, and alignment with consumer welfare—not merely a mathematical convenience but a critical determinant of marketplace outcomes.

## Annotations
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] The Dynamics of Seller Reputation: Theory and Evidence from eBay', 'url': 'https://www.nber.org/system/files/working_papers/w10363/w10363.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Time Decay Attribution Model: How it Works & Is it for you? - RedTrack', 'url': 'https://www.redtrack.io/blog/time-decay-attribution-model/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Reputation, Feedback, and Trust in Online Platforms (Chapter 5)', 'url': 'https://www.cambridge.org/core/books/reengineering-the-sharing-economy/reputation-feedback-and-trust-in-online-platforms/6C1EB222CAE385076434293D2680EC13'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Rating Systems and the End-Game Effect: When Reputation Works ...', 'url': 'https://www.econstor.eu/bitstream/10419/302738/1/cesifo1_wp11253.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Understanding How Time Decay Attribution Model Works - Ingest Labs', 'url': 'https://ingestlabs.com/time-decay-attribution-model-explained/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Trust, reputation, and the value of promises in online auctions of ...', 'url': 'https://journals.sagepub.com/doi/10.1177/10434631231170342'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Exponential Decay Function-Based Time-Aware Recommender ...', 'url': 'https://thesai.org/Downloads/Volume13No10/Paper_71-Exponential_Decay_Function_Based_Time_Aware_Recommender_System.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Exponential Decay - Math Steps, Examples & Questions', 'url': 'https://thirdspacelearning.com/us/math-resources/topic-guides/ratio-and-proportion/exponential-decay/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Balancing Producer Fairness and Efficiency via Prior-Weighted ...', 'url': 'https://arxiv.org/html/2207.04369v6'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Application of Time Decay Functions and the Elo System in Student ...', 'url': 'https://www.fi.muni.cz/~xpelanek/publications/decay-elo.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Exponential Growth and Decay: Graph, Formula, Examples - Turito', 'url': 'https://www.turito.com/learn/math/exponential-growth-and-decay'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'When Did They Post It? How Temporal Markers Influence the ...', 'url': 'https://onlinelibrary.wiley.com/doi/full/10.1002/mar.22163'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A Simple Recency Prior and the Limits of Heuristic Trend Detection', 'url': 'https://arxiv.org/html/2509.19376v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Dynamic Reputation Modeling - Emergent Mind', 'url': 'https://www.emergentmind.com/topics/dynamic-reputation-modeling'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Exponential Decay Function-Based Time-Aware Recommender ...', 'url': 'https://thesai.org/Downloads/Volume13No10/Paper_71-Exponential_Decay_Function_Based_Time_Aware_Recommender_System.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'People display consistent recency and primacy effects in behavior ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC12356758/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] The Dynamics of Seller Reputation: Theory and Evidence from eBay', 'url': 'https://www.nber.org/system/files/working_papers/w10363/w10363.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Granular feedback merits sophisticated aggregation - arXiv', 'url': 'https://arxiv.org/html/2507.12041v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': "The Airbnb Algorithm Changed! Here's the Entire 2026 Algo in 11 ...", 'url': 'https://www.youtube.com/watch?v=6rX3pUWTBGk'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Research Scoring Methodologies - G2 Documentation', 'url': 'https://documentation.g2.com/docs/research-scoring-methodologies'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Types of performance review biases & how to avoid them', 'url': 'https://www.cultureamp.com/blog/performance-review-bias'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': "The platform's algorithm affecting the overall rating of several listings", 'url': 'https://community.withairbnb.com/t5/Help-with-your-business/The-platform-s-algorithm-affecting-the-overall-rating-of-several/m-p/2086691'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Designing Better Online Review Systems - Harvard Business Review', 'url': 'https://hbr.org/2019/11/designing-better-online-review-systems'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Common Performance Review Biases: How to Spot and Counter ...', 'url': 'https://blog.pragmaticengineer.com/performance-review-biases/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'How Algorithms Keep Workers Under Their Control - Kellogg Insight', 'url': 'https://insight.kellogg.northwestern.edu/article/hatim-rahman-book-excerpt'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Balancing Producer Fairness and Efficiency via Prior-Weighted ...', 'url': 'https://arxiv.org/html/2207.04369v6'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Exponential Decay Function-Based Time-Aware Recommender ...', 'url': 'https://thesai.org/Downloads/Volume13No10/Paper_71-Exponential_Decay_Function_Based_Time_Aware_Recommender_System.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Better Feeds: Algorithms That Put People First', 'url': 'https://kgi.georgetown.edu/wp-content/uploads/2025/02/Better-Feeds_-Algorithms-That-Put-People-First.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Performance Evaluation Modeling eBay-like reputation systems', 'url': 'https://www.cse.cuhk.edu.hk/~cslui/PUBLICATION/PE_ebay.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Time Decay Attribution Model: How it Works & Is it for you? - RedTrack', 'url': 'https://www.redtrack.io/blog/time-decay-attribution-model/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Understanding the Amazon Review Algorithm - eCom Triage', 'url': 'https://ecomtriage.com/understanding-the-amazon-review-algorithm/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'How is feedback calculated? - The eBay Community', 'url': 'https://community.ebay.com/t5/Selling/How-is-feedback-calculated/td-p/28102336'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Research on Methodologies for Assessing the Reliability of Taobao ...', 'url': 'https://www.oreateai.com/blog/research-on-methodologies-for-assessing-the-reliability-of-taobao-purchasing-agents/aa1e0fdc74fa3f2bb38f796f82a25831'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The way Amazon weighs product reviews DOES NOT MAKE SENSE', 'url': 'https://sellercentral.amazon.com/seller-forums/discussions/t/5a005cb7-77e3-45b1-9c99-9c08802f15da'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Feedback calculation - The eBay Community', 'url': 'https://community.ebay.com/t5/Ask-a-Mentor/Feedback-calculation/td-p/33544955'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Taobao Merchant Rating-WorldPostOnline Taobao Malaysia & 1688 ...', 'url': 'https://www.worldpostonline.com/content-81.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Balancing Producer Fairness and Efficiency via Prior-Weighted ...', 'url': 'https://arxiv.org/html/2207.04369v6'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Time-Aware Neighbourhood-Based Collaborative Filtering', 'url': 'https://vu-business-analytics.github.io/internship-office/papers/paper-zwart.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] SPRS Evaluation Criteria Manual', 'url': 'https://www.sprs.csd.disa.mil/pdf/SPRS_DataEvaluationCriteria.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A Bayesian Rating System for Players of Time-Varying Strength', 'url': 'https://www.remi-coulom.fr/WHR/WHR.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Review-Aware Recommender Systems (RARSs): Recent Advances ...', 'url': 'https://dl.acm.org/doi/10.1145/3744661'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Methodology Guide | CRSP', 'url': 'https://www.crsp.org/wp-content/uploads/guides/CRSP_Market_Indexes_Methodology_Guide.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Rating Scales in UX Research: The Ultimate Guide | IxDF', 'url': 'https://www.interaction-design.org/literature/article/rating-scales-for-ux-research'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Information Decay in Building Predictive Models Using Temporal Data', 'url': 'https://www.jsoftware.us/vol7/jsw0702-30.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The Biases and Blind Spots of Risk Scoring Algorithms', 'url': 'https://www.flagright.com/post/the-biases-and-blind-spots-of-risk-scoring-algorithms'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Performance Management: Overcoming Assessment Bias With Shyft', 'url': 'https://www.myshyft.com/blog/bias-in-performance-assessment/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Trust Decay-Based Temporal Learning for Dynamic Recommender ...', 'url': 'https://ui.adsabs.harvard.edu/abs/2025IEEEA..13k0955H/abstract'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Algorithmic platform management and risk-taking behavior ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC12756581/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The Weighted Pipeline: A Simple Sales Forecasting Method', 'url': 'https://forecastio.ai/blog/weighted-pipeline'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Temporal-Aware and Aspect Sentiment Driven Recommender ...', 'url': 'https://dl.acm.org/doi/10.1145/3748825.3748901'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Quality Control And Rating Systems for Service Marketplaces', 'url': 'https://xgenious.com/quality-control-and-rating-systems-service-marketplaces/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Supporting Market Conditions Adjustments - Appraisal Buzz', 'url': 'https://appraisalbuzz.com/supporting-market-conditions-adjustments-a-comprehensive-guide-for-appraisers/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Impact of delivery performance on online review ratings - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9115748/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Market Performance and Review System Informativeness', 'url': 'https://pages.aueb.gr/conferences/Crete2025/papers/Louis.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Exponential Decay Function-Based Time-Aware Recommender ...', 'url': 'https://thesai.org/Downloads/Volume13No10/Paper_71-Exponential_Decay_Function_Based_Time_Aware_Recommender_System.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Ratings Explanation - Hansen Ratings', 'url': 'https://hansenratings.github.io/Ratings%20Explanation.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': "Amazon's A9 Algorithm Explained: What Really Matters for Rankings ...", 'url': 'https://canopymanagement.com/amazons-a9-algorithm-explained-for-rankings/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Adaptive Decay Mechanism - Emergent Mind', 'url': 'https://www.emergentmind.com/topics/adaptive-decay-mechanism'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Research Scoring Methodologies - G2 Documentation', 'url': 'https://documentation.g2.com/docs/research-scoring-methodologies'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Reputation Inflation∗ - Apostolos Filippas', 'url': 'https://www.apostolos-filippas.com/papers/inflation.pdf'}}

## Sources
https://www.nber.org/system/files/working_papers/w10363/w10363.pdf
https://www.redtrack.io/blog/time-decay-attribution-model/
https://www.cambridge.org/core/books/reengineering-the-sharing-economy/reputation-feedback-and-trust-in-online-platforms/6C1EB222CAE385076434293D2680EC13
https://www.econstor.eu/bitstream/10419/302738/1/cesifo1_wp11253.pdf
https://ingestlabs.com/time-decay-attribution-model-explained/
https://journals.sagepub.com/doi/10.1177/10434631231170342
https://thesai.org/Downloads/Volume13No10/Paper_71-Exponential_Decay_Function_Based_Time_Aware_Recommender_System.pdf
https://thirdspacelearning.com/us/math-resources/topic-guides/ratio-and-proportion/exponential-decay/
https://arxiv.org/html/2207.04369v6
https://www.fi.muni.cz/~xpelanek/publications/decay-elo.pdf
https://www.turito.com/learn/math/exponential-growth-and-decay
https://onlinelibrary.wiley.com/doi/full/10.1002/mar.22163
https://arxiv.org/html/2509.19376v1
https://www.emergentmind.com/topics/dynamic-reputation-modeling
https://thesai.org/Downloads/Volume13No10/Paper_71-Exponential_Decay_Function_Based_Time_Aware_Recommender_System.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC12356758/
https://www.nber.org/system/files/working_papers/w10363/w10363.pdf
https://arxiv.org/html/2507.12041v1
https://www.youtube.com/watch?v=6rX3pUWTBGk
https://documentation.g2.com/docs/research-scoring-methodologies
https://www.cultureamp.com/blog/performance-review-bias
https://community.withairbnb.com/t5/Help-with-your-business/The-platform-s-algorithm-affecting-the-overall-rating-of-several/m-p/2086691
https://hbr.org/2019/11/designing-better-online-review-systems
https://blog.pragmaticengineer.com/performance-review-biases/
https://insight.kellogg.northwestern.edu/article/hatim-rahman-book-excerpt
https://arxiv.org/html/2207.04369v6
https://thesai.org/Downloads/Volume13No10/Paper_71-Exponential_Decay_Function_Based_Time_Aware_Recommender_System.pdf
https://kgi.georgetown.edu/wp-content/uploads/2025/02/Better-Feeds_-Algorithms-That-Put-People-First.pdf
https://www.cse.cuhk.edu.hk/~cslui/PUBLICATION/PE_ebay.pdf
https://www.redtrack.io/blog/time-decay-attribution-model/
https://ecomtriage.com/understanding-the-amazon-review-algorithm/
https://community.ebay.com/t5/Selling/How-is-feedback-calculated/td-p/28102336
https://www.oreateai.com/blog/research-on-methodologies-for-assessing-the-reliability-of-taobao-purchasing-agents/aa1e0fdc74fa3f2bb38f796f82a25831
https://sellercentral.amazon.com/seller-forums/discussions/t/5a005cb7-77e3-45b1-9c99-9c08802f15da
https://community.ebay.com/t5/Ask-a-Mentor/Feedback-calculation/td-p/33544955
https://www.worldpostonline.com/content-81.html
https://arxiv.org/html/2207.04369v6
https://vu-business-analytics.github.io/internship-office/papers/paper-zwart.pdf
https://www.sprs.csd.disa.mil/pdf/SPRS_DataEvaluationCriteria.pdf
https://www.remi-coulom.fr/WHR/WHR.pdf
https://dl.acm.org/doi/10.1145/3744661
https://www.crsp.org/wp-content/uploads/guides/CRSP_Market_Indexes_Methodology_Guide.pdf
https://www.interaction-design.org/literature/article/rating-scales-for-ux-research
https://www.jsoftware.us/vol7/jsw0702-30.pdf
https://www.flagright.com/post/the-biases-and-blind-spots-of-risk-scoring-algorithms
https://www.myshyft.com/blog/bias-in-performance-assessment/
https://ui.adsabs.harvard.edu/abs/2025IEEEA..13k0955H/abstract
https://pmc.ncbi.nlm.nih.gov/articles/PMC12756581/
https://forecastio.ai/blog/weighted-pipeline
https://dl.acm.org/doi/10.1145/3748825.3748901
https://xgenious.com/quality-control-and-rating-systems-service-marketplaces/
https://appraisalbuzz.com/supporting-market-conditions-adjustments-a-comprehensive-guide-for-appraisers/
https://pmc.ncbi.nlm.nih.gov/articles/PMC9115748/
https://pages.aueb.gr/conferences/Crete2025/papers/Louis.pdf
https://thesai.org/Downloads/Volume13No10/Paper_71-Exponential_Decay_Function_Based_Time_Aware_Recommender_System.pdf
https://hansenratings.github.io/Ratings%20Explanation.html
https://canopymanagement.com/amazons-a9-algorithm-explained-for-rankings/
https://www.emergentmind.com/topics/adaptive-decay-mechanism
https://documentation.g2.com/docs/research-scoring-methodologies
https://www.apostolos-filippas.com/papers/inflation.pdf