# Deep Research Report: perplexity/sonar-deep-research
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** d80f372c | **Time:** 93.30s | **Cost:** $1.14206
--------------------------------------------------------------------------------

# The Temporal Discount Function of Rating Contributions in Review Systems: Determinants, Models, and Mechanisms

This report provides a comprehensive examination of the temporal discount function that governs how rating contributions from individual reviews decline in value over time within e-commerce and product rating systems. Through analysis of consumer behavior, mathematical modeling approaches, and system design principles, this report reveals that the temporal discount function is determined by a complex interplay of psychological factors, system objectives, product characteristics, and market dynamics. The fundamental principle underlying these functions is that recent reviews carry substantially greater weight in influencing consumer purchasing decisions than older reviews, with this weight declining according to exponential or hyperbolic patterns depending on product category and market context.

## The Foundational Psychology of Temporal Discounting in Review Systems

The temporal discount function of review contributions fundamentally emerges from human psychological principles that govern how individuals evaluate and process information over time. **Temporal discounting**, the psychological phenomenon wherein individuals assign lower subjective value to future or past events compared to present events, directly shapes how consumers and platforms weight review contributions[4][10]. This principle extends naturally to review systems, where the recency of feedback becomes a critical factor in determining its influence on purchasing decisions and product visibility.

Consumer research demonstrates the profound importance of review recency in decision-making processes. An overwhelming majority of consumers, approximately 88-90%, report that they regularly or at least somewhat regularly consider how recently a review was written when evaluating products for purchase[3][34][58]. More striking still is the finding that 60% of consumers would prefer a product with fewer but more recent reviews compared to one with a higher volume of older reviews[3][34][58]. This behavioral pattern reflects what psychologists call the **recency effect**—the tendency for individuals to give disproportionate weight to recent information when making judgments[5]. The recency effect operates because recent reviews are perceived as more relevant to current product quality, manufacturing standards, and customer service performance, whereas older reviews may reflect obsolete conditions, discontinued product batches, or outdated business practices.

The psychological basis for temporal discounting in reviews rests on several interconnected cognitive mechanisms. First, consumers recognize that businesses evolve and change over time. New management, staff training programs, product improvements, and service enhancements can substantially alter the quality of customer experiences. An older review, regardless of its original sentiment, may not accurately reflect the current state of a product or service[55]. Second, consumers understand that their own expectations and preferences evolve. What was considered acceptable service or product quality five years ago may not meet contemporary standards. Third, consumers perceive older reviews as potentially less authentic or reliable due to the possibility of manipulation, fraudulent activity, or incentivization practices that may have changed over time[55]. These psychological foundations explain why temporal discounting of review contributions is not merely a technical feature but rather a reflection of rational consumer behavior and legitimate concerns about information currency.

## Consumer Demographics and Temporal Weighting Preferences

Temporal discount functions in review systems exhibit meaningful variation across different demographic segments, revealing that the importance of review recency is not uniformly distributed across the consumer population. Younger consumers, particularly Millennials and Generation Z, demonstrate significantly stronger preferences for abundant recent reviews compared to older generations[3][34][58]. Over 78% of Millennials and Gen Z report that they are more likely to purchase products with 1,000 reviews, whereas only 45% of Baby Boomers express the same preference, suggesting that younger cohorts place greater emphasis on both review volume and implicitly on the currency of that feedback[34][58].

Socioeconomic status emerges as another critical determinant of temporal weighting preferences. Consumers with the lowest incomes, those earning under $10,000 annually, are most likely to emphasize review quantity when making purchase decisions, suggesting that lower-income shoppers adopt more conservative approaches to product evaluation that incorporate temporal considerations along with volume assessment[3][34][58]. This pattern likely reflects risk aversion—lower-income consumers cannot afford poor purchases and therefore require more extensive evidence, including recent validation of product quality, before committing resources.

Brand familiarity significantly modulates the temporal importance assigned to reviews. Eighty percent of consumers report that review recency becomes more important when considering unknown or unfamiliar brands[34][55][58]. This context-dependent weighting reflects a rational response to uncertainty: when consumers lack prior brand knowledge or trust, they rely more heavily on current market feedback to gauge product reliability. Conversely, with established and trusted brands, consumers may weight recent reviews less heavily because they possess greater confidence in brand consistency and quality standards. Product category also determines temporal discounting patterns. Consumer Electronics and Appliances (84%) and Health & Beauty (82%) represent categories where review recency is especially critical, likely because these product categories experience more rapid technological evolution, seasonal variations in performance, or changes in formula and composition[34][58].

## Mathematical Models of Temporal Decay in Review Systems

The temporal discount function of review contributions can be formally expressed through mathematical models that capture how review value diminishes over time. The most widely adopted model employs exponential decay, wherein the weight or credit assigned to a review decays exponentially as temporal distance from the present increases[2][5][43][46]. The fundamental exponential decay formula used in temporal attribution systems can be expressed as follows:

\[ \text{Credit}(t) = e^{-kt} \]

Where \( t \) represents the time elapsed since the review was posted, \( k \) is a decay constant that determines the rate at which credit diminishes, and \( e \) is Euler's mathematical constant (approximately 2.718)[5][46]. This formulation ensures that touchpoints closer to the present moment receive substantially more weight, while older touchpoints asymptotically approach zero weight but never completely disappear from the calculation. The exponential decay model has particular mathematical advantages because its derivative remains proportional to the function itself, making both computational and theoretical analysis tractable[13][16].

An alternative parameterization of temporal decay that proves more intuitive for practitioners relies on the **half-life concept**. The half-life represents the temporal period required for a review to decay to exactly half of its original influence weight[13][33][36]. Google Analytics, for instance, employs a default 7-day half-life in its time decay attribution model, meaning that a review from seven days ago receives exactly half the credit of an identical review posted today[5][46]. This half-life parameterization can be expressed mathematically as:

\[ \text{Weight}(t) = \left(\frac{1}{2}\right)^{t/h} \]

Where \( h \) represents the half-life period and \( t \) is the elapsed time[33][36]. The half-life approach proves more interpretable to non-technical stakeholders because practitioners can readily explain that "reviews lose half their influence every X days," making the decay parameter directly comparable to real-world purchase decision timelines.

Industry-specific half-life recommendations reveal how temporal discounting varies across market contexts. Fast-moving e-commerce categories typically employ half-lives of 3-7 days, reflecting rapid purchasing cycles and limited consideration periods[5][46]. Software-as-a-Service (SaaS) platforms serving small and medium businesses often extend the half-life to 7-14 days, acknowledging longer evaluation periods. Enterprise software solutions require substantially longer half-lives of 21-45 days due to extended sales cycles involving multiple stakeholders and evaluation stages. Automotive purchases, representing high-consideration acquisitions, may employ half-lives extending 30-60 days or longer[5][46]. These industry variations demonstrate that the temporal discount function cannot be universal but must adapt to match actual customer decision-making timelines within specific markets.

## Temporal Distance Effects on Review Ratings and Helpfulness

Recent empirical research has revealed complex relationships between temporal distance—the time elapsed between a delivery event or purchase and the review submission date—and the numerical ratings customers assign to reviews. Studies analyzing e-commerce delivery performance and online reviews have documented that temporal distance exhibits a **positive association with ratings for late deliveries**[7][15]. Specifically, when orders arrive late, customers provide higher ratings if more time has elapsed between the delivery date and the review posting date. A delivery that was one day late might receive a rating of 3 stars if reviewed immediately, but that same late delivery might receive 4 stars if the review is written weeks later[7][15]. This pattern suggests that the psychological impact of delivery failures diminishes over time according to an exponential decay function wherein negative emotions associated with service failures decay at a predictable rate.

Conversely, temporal distance shows a weaker or even reversed effect for early deliveries[7][15]. Customers who receive products ahead of schedule provide modestly higher ratings if reviewed immediately, but this boost to ratings does not grow stronger as temporal distance increases. This asymmetry reflects what behavioral economists term **loss aversion**—customers weight negative outcomes (late delivery) more heavily in their judgments than equivalent positive outcomes (early delivery), and this asymmetric weighting becomes more pronounced when memories fade[7][15]. The temporal dynamics observed in delivery performance reviews provide empirical validation that review helpfulness and relevance themselves decay over time according to psychological forgetting curves.

The helpfulness of reviews, defined as how useful consumers find specific reviews for purchase decision-making, also exhibits robust temporal dynamics. Research examining reviewer expertise and temporal information in helpfulness prediction has demonstrated that temporal features represent the **most impactful component** of helpfulness prediction models[57][60]. When researchers constructed machine learning models incorporating reviewer expertise, review text content, and temporal information, ablation studies removing temporal information caused accuracy to decline more substantially than removing expertise information. This finding indicates that "when the review was posted" constitutes perhaps the single most influential factor determining whether consumers will find that review helpful[57][60].

The temporal helpfulness decay function appears to follow a distinctive pattern whereby recent reviews cluster at high helpfulness ratings, while older reviews show progressively greater dispersion in helpfulness judgments[57][60]. This pattern reflects multiple mechanisms. First, recent reviews benefit from **information currency**—they describe current product versions, current manufacturing practices, and current customer service standards. Second, recent reviews avoid the accumulation of credibility challenges that plague older reviews, such as questions about manipulated reviews, incentivized feedback, or changing platform standards. Third, recent reviews benefit from what platforms term the **cold-start problem** in reverse: recently posted reviews have few helpfulness votes, but the first votes tend to be from recent, engaged consumers whose standards align with current market expectations[57][60].

## System Design Objectives and Temporal Weighting Functions

The temporal discount function implemented within any review system reflects conscious design choices about platform objectives and values. E-commerce platforms must balance multiple competing objectives when determining how to weight reviews over time. The primary objective involves **maximizing consumer confidence in product quality signals**. Recent reviews provide better signals about current product quality than older reviews, so platforms emphasizing consumer trust will employ shorter half-lives, ensuring that old reviews rapidly lose influence. A secondary objective involves **maintaining historical context and long-term product reputation**. Some platforms recognize that a product's long-term track record matters and therefore employ longer half-lives that allow older reviews to retain some influence indefinitely.

Platforms must also consider **promoting reviewer contribution incentives**. If reviews decay too rapidly, recent contributors become incentivized to write reviews while older contributors see their efforts devalued. Conversely, if reviews persist indefinitely with minimal decay, platforms lose the urgency that motivates recent customers to write reviews. The optimal temporal discount function therefore balances these incentive structures. Amazon, for example, employs review sorting and visibility mechanisms that strongly emphasize recency while maintaining older reviews as searchable and sortable content[23][38][41]. This approach maximizes both current relevance and historical accountability.

Product category characteristics determine optimal temporal weighting strategies. Products experiencing rapid technological change require aggressive temporal discounting because a review of a smartphone from 2023 provides minimal relevant information for purchasing decisions in 2025[3][23][38][41][49][52]. Conversely, products in mature categories with stable characteristics, such as classic tools or unchanging food products, benefit from longer temporal windows because older reviews remain relevant and informative. Platform designers must therefore implement **adaptive temporal discount functions** that vary across product categories rather than applying uniform discount rates universally[8].

Consumer expectations themselves constitute a key determinant of temporal discount functions. Research findings indicate that 77% of consumers expect reviews to be written within three months of purchase, suggesting that consumers perceive a temporal window of roughly 90 days within which reviews remain maximally relevant[3][34][58]. This consumer expectation provides empirical grounding for platform designers selecting half-lives and temporal parameters. Platforms that substantially exceed this consumer-expected window risk appearing to stale consumers with outdated information, while platforms that enforce too-short windows risk losing valuable feedback.

## The Distinction Between Review Age and Review Velocity

A critical distinction exists between **review age** (how long ago a review was written) and **review velocity** (how frequently new reviews are being written)[23][38][41]. While temporal discount functions directly address review age by reducing the influence of individual old reviews, review velocity represents a system-level signal that may actually increase platform visibility and ranking benefits. Amazon's A11 algorithm era (2024-present) emphasizes that products generating 5-10 reviews per month per $10,000 in monthly revenue maintain healthy velocity, and this velocity signals product relevance and continued consumer engagement[38][41]. The temporal discount function applied to individual reviews differs from the velocity metrics applied at the product level.

This distinction matters because a product can simultaneously have old reviews and high velocity, or new reviews and low velocity. A product with 1,000 reviews from 2020 but zero reviews in 2025 sends a very different signal than a product with 100 reviews from 2020 and 50 reviews in 2025. Temporal discount functions address the former (reducing the influence of old reviews), while velocity metrics address the latter (rewarding consistent recent review generation). Together, these mechanisms create a temporal framework that simultaneously:

1. Reduces the influence of isolated old reviews through exponential decay
2. Rewards products with consistent recent review generation through velocity metrics
3. Penalizes products that lack recent feedback regardless of historical review volume
4. Prevent manipulation by requiring sustained review generation rather than allowing platforms to rely on historical review accumulation[23][38][41]

## Temporal Dynamics in Recommendation Systems and Collaborative Filtering

Advanced recommendation systems have increasingly incorporated temporal discount functions into collaborative filtering algorithms, recognizing that user preferences evolve and that older interactions contain less predictive information than recent interactions[56][59]. Time-decay collaborative filtering (TD-CF) algorithms apply forgetting curves analogous to human memory to weight user-item interactions, giving substantially more weight to recent user behaviors and dramatically less weight to interactions from the distant past[59]. The theoretical justification for these approaches draws on the observation that human memory itself follows exponential decay patterns, wherein recent information remains vivid while distant information fades rapidly from active recall[59].

In educational contexts, temporal discount functions applied to music teaching resource recommendations achieved substantially lower prediction error (RMSE of 8.95 versus higher errors for non-temporal models) by weighting recent student interactions more heavily than historical preferences[59]. This improvement occurs because students' musical preferences change over time, new genres emerge, and instructor recommendations shift. A student's listening behavior from three years ago provides minimal information about current musical preferences, while behavior from three weeks ago provides highly predictive information. Empirical testing of TD-CF algorithms demonstrates that temporal weighting reduces the long-tail problem wherein very old data continues to influence recommendations despite its diminished relevance[59].

## Information Diffusion and Temporal Influence Decay in Social Networks

Beyond e-commerce review systems, temporal discount functions govern how information influence decays within social networks and online communities. Research on information diffusion through social networks has demonstrated that user influence exhibits dramatic temporal decay patterns[21][32]. A user's influence on their social network connections decreases predictably over time as attention shifts to new content and recent opinions. Temporal influence decay appears to follow modified exponential or power-law distributions, with some research suggesting that influence decays more rapidly for certain topic categories and more slowly for others[21][32].

The temporal independent cascade model, which predicts information spread through networks based on temporal dynamics, shows that influence from early adopters or influential nodes decays markedly as information cascades progress[21]. An influencer's ability to drive sharing or engagement with a piece of content diminishes over time as the novelty effect fades and competing content emerges. This temporal decay of influence affects not only individual reviews but also the aggregate impact of review clusters and review communities. A surge of positive reviews posting simultaneously generates greater platform visibility and consumer attention than the same number of reviews spread across months[21][32][35].

## Psychological Time Perception and Subjective Temporal Discounting

Research on temporal discounting in human decision-making reveals that individuals do not discount future or past events according to objective calendar time but rather according to **subjective perceived time**[47]. Individuals perceive time non-linearly: the subjective distance between today and tomorrow appears much longer than the subjective distance between tomorrow and the day after. This psychological phenomenon, operationalized through exponential or power-law transformations of objective time, explains why simple calendar-time-based discount functions may not optimally match human temporal preferences.

Research examining the role of perceived anticipatory time in temporal discounting has demonstrated that when subjective time perception is accounted for through appropriate mathematical transformations, apparent hyperbolic discounting patterns often reduce to exponential discounting patterns[47]. This finding suggests that some observed deviations from simple exponential decay in review systems may reflect not fundamental violations of exponential principles but rather the operation of psychological time perception. Platforms that account for subjective temporal perception through appropriate functional transformations may achieve better alignment with consumer temporal preferences than platforms employing simple linear or purely exponential models[47].

## The Role of Product Lifecycle Stage in Temporal Weighting

The stage of a product within its lifecycle substantially determines the appropriate temporal discount function. Products in the **introduction and growth stages** benefit from aggressive temporal weighting toward recent reviews because newer products undergo rapid refinement and improvement based on customer feedback. A review from the initial launch week of a product may already be obsolete due to manufacturer corrections and improvements[49][52]. Conversely, products in the **maturity stage** can employ longer temporal windows because manufacturing processes have stabilized and product formulations have achieved consistency[49][52].

Products entering the **decline stage**, where sales volumes are falling and market share is contracting, may paradoxically benefit from temporal weighting that maintains longer historical context. Consumers considering purchasing a declining product might benefit from understanding the full history of customer satisfaction, which recent reviews alone might not capture[49][52]. This lifecycle-dependent temporal discounting reflects the principle that the optimal information set for consumer decision-making depends on the product's market position and stage of maturity.

## Content Freshness and Search Engine Implications

Temporal discount functions extend beyond e-commerce product reviews to encompass how search engines weight review content freshness in ranking algorithms. Google's search algorithm incorporates content freshness as a ranking factor, applying temporal weighting functions that substantially boost recently updated or recently published content in time-sensitive query categories[20][50]. The mathematical basis for this weighting follows document inception date analysis, where the document age becomes incorporated into ranking calculations through exponential decay functions applied to freshness signals[50].

Search engines may apply more aggressive temporal weighting for queries deemed time-sensitive, such as news queries, technology queries, or rapidly evolving topic queries[20][50]. For stable informational queries, temporal weighting receives minimal emphasis, allowing older but higher-quality content to maintain ranking prominence. This adaptive temporal weighting in search reflects the same principles governing review system temporal discount functions: information relevance correlates with recency for certain query types but remains stable over time for others[20][50].

## Implementation Challenges and Temporal Parameter Selection

Implementing effective temporal discount functions in production systems requires careful selection of parameters that reflect actual product categories and market dynamics. The fundamental challenge involves balancing multiple objectives: maintaining consumer confidence in product quality through recent feedback, preserving historical accountability and long-term reputation, incentivizing ongoing review contribution, and preventing manipulation through gaming temporal metrics[3][8][34][38][41].

Practitioners must determine whether to employ uniform temporal discount functions across all product categories or implement category-specific variations. Evidence suggests that category-specific approaches yield superior consumer outcomes, as different product types experience different rates of change in quality, manufacturing, and market conditions[3][8][38]. A consumer electronics category might employ a 7-day half-life while a home goods category employs a 30-day half-life, reflecting actual differences in product evolution rates.

A second implementation challenge involves determining decay function shape. While exponential decay provides mathematical elegance and proven effectiveness in many domains, alternative shapes such as power-law decay or piecewise functions might better match actual consumer temporal preferences in specific contexts. Empirical testing of different decay functions against consumer behavior provides the most reliable approach to parameter selection[1][27][30][44].

## Conclusion: Synthesis and Future Directions

The temporal discount function of rating contributions in review systems emerges from a complex interplay of psychological principles, system design objectives, product category characteristics, and market dynamics. At its foundation, the temporal discount function reflects the psychological reality that recent information appears more relevant than distant information to contemporary decision-making, a principle rooted in cognitive psychology, behavioral economics, and human memory research. Mathematical models capturing this principle typically employ exponential decay functions parameterized through half-life concepts, with half-life lengths varying from 3-7 days for fast-moving consumer goods to 30-60 days for high-consideration purchases.

Consumer behavior research confirms that review recency substantially outweighs review quantity in determining purchase decisions, with 60% of consumers preferring fewer recent reviews to greater quantities of older reviews[3][34][58]. This behavioral pattern validates the temporal discount approach as fundamentally aligned with consumer rationality rather than imposed constraints. System designers implementing temporal discount functions must simultaneously achieve multiple objectives: maintaining consumer confidence, preserving historical accountability, incentivizing review contribution, and preventing manipulation. The optimal temporal discount function therefore represents not a static mathematical formula but an adaptive system that evolves with product category characteristics, consumer expectations, and market conditions.

Future research directions should include empirical validation of temporal discount function shapes across diverse product categories, investigation of whether psychological time perception models improve alignment between platform temporal weighting and consumer preferences, and exploration of how temporal discount functions interact with other platform ranking signals such as review velocity, reviewer expertise, and content quality metrics. As recommendation systems and review platforms continue evolving, understanding the determinants of temporal discount functions will remain essential to building systems that effectively serve consumer interests while maintaining platform integrity and incentivizing valuable community contribution.

## Annotations
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'On the Functional Form of Temporal Discounting - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5764197/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Time Decay Attribution: E-Commerce Explained - ThoughtMetric', 'url': 'https://thoughtmetric.io/define/time-decay-attribution'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The Complete Guide to Ratings & Reviews - PowerReviews', 'url': 'https://www.powerreviews.com/the-complete-guide-to-ratings-reviews/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The neural correlates of temporal reward discounting', 'url': 'https://wires.onlinelibrary.wiley.com/doi/10.1002/wcs.1246'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Time Decay Attribution Model: How it Works & Is it for you? - RedTrack', 'url': 'https://www.redtrack.io/blog/time-decay-attribution-model/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Peer review in Time preferences are reliable across time-horizons ...', 'url': 'https://elifesciences.org/articles/39656/peer-reviews'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Impact of delivery performance on online review ratings - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9115748/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Improving Amazon-like Review Systems by Considering the ...', 'url': 'https://www.iis.sinica.edu.tw/~cclljj/publication/2011/11_Informatica-Amazon.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Everything You Need to Know About Review Recency and Volume', 'url': 'https://metricscart.com/insights/review-recency-and-volume/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Temporal Discounting: Valuing Immediate Rewards Over Long ...', 'url': 'https://www.renascence.io/journal/temporal-discounting-valuing-immediate-rewards-over-long-term-gains'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A Novel Review Helpfulness Measure Based on the User-Review ...', 'url': 'https://dl.acm.org/doi/10.1145/3585280'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Insights from Turner: Be Thankful: Diving into Compliments, Review ...', 'url': 'https://www.jturnerresearch.com/blog/insights-from-turner-be-thankful-diving-into-compliments-review-recency-and-less-harmful-categories'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Exponential Decay - Gregory Gundersen', 'url': 'https://gregorygundersen.com/blog/2022/05/17/exponential-decay/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Was This Review Helpful to You? It Depends! Context and Voting ...', 'url': 'https://www.cs.cornell.edu/~tj/publications/sipos_etal_14a.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Impact of delivery performance on online review ratings - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9115748/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Exponential growth and decay modeled by discrete dynamical ...', 'url': 'https://mathinsight.org/exponential_growth_decay_discrete'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A Novel Review Helpfulness Measure Based on the User-Review ...', 'url': 'https://dl.acm.org/doi/10.1145/3585280'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Do Online Reviews Affect Product Sales? The Role of Reviewer ...', 'url': 'https://ink.library.smu.edu.sg/cgi/viewcontent.cgi?article=1751&context=sis_research'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Discount Function API - Shopify Dev Docs', 'url': 'https://shopify.dev/docs/api/functions/latest/discount'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': "Google's 48 Ranking Factors: The Complete List (2026)", 'url': 'https://www.wixseoexpert.com/post/google-ranking-factors-the-complete-list-2026'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Dynamics of temporal influence in polarised networks | PLOS One', 'url': 'https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0337753'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Build a Discount Function - Shopify Dev Docs', 'url': 'https://shopify.dev/docs/apps/build/discounts/build-discount-function'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'How Many Reviews Do I Need to Start Ranking on Google ... - Olly Olly', 'url': 'https://www.ollyolly.com/blog/how-many-reviews-do-i-need-to-start-ranking-on-google-the-magic-numbers-that-change-everything/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Temporal dynamics of user activities: deep learning strategies ... - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11196652/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '3.7. Weight Decay — Dive into Deep Learning 1.0.3 documentation', 'url': 'https://d2l.ai/chapter_linear-regression/weight-decay.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Understanding Online Consumer Textual Reviews and Rating', 'url': 'https://journals.sagepub.com/doi/10.1177/21582440221104806'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'On the Functional Form of Temporal Discounting - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5764197/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Why Do We Need Weight Decay in Modern Deep Learning? - arXiv', 'url': 'https://arxiv.org/html/2310.04415v2'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A Novel Review Helpfulness Measure Based on the User-Review ...', 'url': 'https://dl.acm.org/doi/full/10.1145/3585280'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Hierarchical Bayesian modeling of intertemporal choice', 'url': 'https://www.cambridge.org/core/journals/judgment-and-decision-making/article/hierarchical-bayesian-modeling-of-intertemporal-choice/3AB4DFF0C5B0020EA1564F636D6AC3A4'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Research Scoring Methodologies - G2 Documentation', 'url': 'https://documentation.g2.com/docs/research-scoring-methodologies'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Modeling Information Diffusion over Social Networks for Temporal ...', 'url': 'https://pureadmin.qub.ac.uk/ws/files/128739460/tkde_HZ.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Moving Averages - Gregory Gundersen', 'url': 'https://gregorygundersen.com/blog/2022/06/04/moving-averages/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The Complete Guide to Ratings & Reviews - PowerReviews', 'url': 'https://www.powerreviews.com/the-complete-guide-to-ratings-reviews/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Patterns of Temporal Variation in Online Media', 'url': 'https://cs.stanford.edu/people/jure/pubs/memeshapes-wsdm11.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Solving half-life problems with exponential decay - Krista King Math', 'url': 'https://www.kristakingmath.com/blog/half-life-and-exponential-decay'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Temporal dynamics of requirements engineering from mobile app ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC9044251/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Amazon Product Ranking Factors 2026 - What Sellers Must Know', 'url': 'https://amzprep.com/amazon-algorithm-ranking-factors/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'How Can Critical Thinking Be Used to Assess the Credibility of ... - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC7134292/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Quantifying Memory Use in Reinforcement Learning with Temporal ...', 'url': 'https://openreview.net/forum?id=ws9ZjMthvi'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': "Amazon's A9 Algorithm Explained: What Really Matters for Rankings ...", 'url': 'https://canopymanagement.com/amazons-a9-algorithm-explained-for-rankings/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A Survey on Automatic Credibility Assessment Using Textual ...', 'url': 'https://arxiv.org/html/2410.21360v2'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Optimize Marketing with Time Decay Attribution - Mailchimp', 'url': 'https://mailchimp.com/resources/time-decay-attribution-model/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'On the Functional Form of Temporal Discounting - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC5764197/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Review-based Recommender Systems: A Survey of Approaches ...', 'url': 'https://arxiv.org/html/2405.05562v3'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Time Decay Attribution Model: How it Works & Is it for you? - RedTrack', 'url': 'https://www.redtrack.io/blog/time-decay-attribution-model/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Perception of Anticipatory Time in Temporal Discounting', 'url': 'https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/2009-KIm-and-Zauberman-JNPE-vol2(2)-95-101.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Key issues in the design of pay for performance programs - PMC - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3535413/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The 6 Stages of the Product Life Cycle Explained | Salesforce ANZ', 'url': 'https://www.salesforce.com/au/blog/product-life-cycle/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Methods for Evaluating Freshness - Briggsby', 'url': 'https://www.briggsby.com/methods-for-evaluating-freshness'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Optimal Design of Validation Experiment for Material Deterioration', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10488985/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Product Life Cycle Stages Explained With Examples | Fractory', 'url': 'https://fractory.com/product-life-cycle-explained/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'How Does Google Determine Ranking Results - Google Search', 'url': 'https://www.google.com/intl/en_us/search/howsearchworks/how-search-works/ranking-results'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Advanced Review Helpfulness Modeling - VU Research Repository', 'url': 'https://vuir.vu.edu.au/41279/1/DU%20Jianhua-thesis.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Consumers May Not Trust Online Reviews Older Than 3 Months', 'url': 'https://ermarketing.net/navigate-the-channel/85-of-consumers-think-local-reviews-older-than-3-months-arent-relevant/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] review of the temporal recommendation system with matrix ... - ijicic', 'url': 'http://www.ijicic.org/ijicic-130511.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] On the Role of Reviewer Expertise in Temporal Review Helpfulness ...', 'url': 'https://aclanthology.org/2023.findings-eacl.125.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The Complete Guide to Ratings & Reviews - PowerReviews', 'url': 'https://www.powerreviews.com/the-complete-guide-to-ratings-reviews/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Application of collaborative filtering algorithm based on time decay ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC11639207/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'On the Role of Reviewer Expertise in Temporal Review Helpfulness ...', 'url': 'https://arxiv.org/abs/2303.00923'}}

## Sources
https://pmc.ncbi.nlm.nih.gov/articles/PMC5764197/
https://thoughtmetric.io/define/time-decay-attribution
https://www.powerreviews.com/the-complete-guide-to-ratings-reviews/
https://wires.onlinelibrary.wiley.com/doi/10.1002/wcs.1246
https://www.redtrack.io/blog/time-decay-attribution-model/
https://elifesciences.org/articles/39656/peer-reviews
https://pmc.ncbi.nlm.nih.gov/articles/PMC9115748/
https://www.iis.sinica.edu.tw/~cclljj/publication/2011/11_Informatica-Amazon.pdf
https://metricscart.com/insights/review-recency-and-volume/
https://www.renascence.io/journal/temporal-discounting-valuing-immediate-rewards-over-long-term-gains
https://dl.acm.org/doi/10.1145/3585280
https://www.jturnerresearch.com/blog/insights-from-turner-be-thankful-diving-into-compliments-review-recency-and-less-harmful-categories
https://gregorygundersen.com/blog/2022/05/17/exponential-decay/
https://www.cs.cornell.edu/~tj/publications/sipos_etal_14a.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC9115748/
https://mathinsight.org/exponential_growth_decay_discrete
https://dl.acm.org/doi/10.1145/3585280
https://ink.library.smu.edu.sg/cgi/viewcontent.cgi?article=1751&context=sis_research
https://shopify.dev/docs/api/functions/latest/discount
https://www.wixseoexpert.com/post/google-ranking-factors-the-complete-list-2026
https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0337753
https://shopify.dev/docs/apps/build/discounts/build-discount-function
https://www.ollyolly.com/blog/how-many-reviews-do-i-need-to-start-ranking-on-google-the-magic-numbers-that-change-everything/
https://pmc.ncbi.nlm.nih.gov/articles/PMC11196652/
https://d2l.ai/chapter_linear-regression/weight-decay.html
https://journals.sagepub.com/doi/10.1177/21582440221104806
https://pmc.ncbi.nlm.nih.gov/articles/PMC5764197/
https://arxiv.org/html/2310.04415v2
https://dl.acm.org/doi/full/10.1145/3585280
https://www.cambridge.org/core/journals/judgment-and-decision-making/article/hierarchical-bayesian-modeling-of-intertemporal-choice/3AB4DFF0C5B0020EA1564F636D6AC3A4
https://documentation.g2.com/docs/research-scoring-methodologies
https://pureadmin.qub.ac.uk/ws/files/128739460/tkde_HZ.pdf
https://gregorygundersen.com/blog/2022/06/04/moving-averages/
https://www.powerreviews.com/the-complete-guide-to-ratings-reviews/
https://cs.stanford.edu/people/jure/pubs/memeshapes-wsdm11.pdf
https://www.kristakingmath.com/blog/half-life-and-exponential-decay
https://pmc.ncbi.nlm.nih.gov/articles/PMC9044251/
https://amzprep.com/amazon-algorithm-ranking-factors/
https://pmc.ncbi.nlm.nih.gov/articles/PMC7134292/
https://openreview.net/forum?id=ws9ZjMthvi
https://canopymanagement.com/amazons-a9-algorithm-explained-for-rankings/
https://arxiv.org/html/2410.21360v2
https://mailchimp.com/resources/time-decay-attribution-model/
https://pmc.ncbi.nlm.nih.gov/articles/PMC5764197/
https://arxiv.org/html/2405.05562v3
https://www.redtrack.io/blog/time-decay-attribution-model/
https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/2009-KIm-and-Zauberman-JNPE-vol2(2)-95-101.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC3535413/
https://www.salesforce.com/au/blog/product-life-cycle/
https://www.briggsby.com/methods-for-evaluating-freshness
https://pmc.ncbi.nlm.nih.gov/articles/PMC10488985/
https://fractory.com/product-life-cycle-explained/
https://www.google.com/intl/en_us/search/howsearchworks/how-search-works/ranking-results
https://vuir.vu.edu.au/41279/1/DU%20Jianhua-thesis.pdf
https://ermarketing.net/navigate-the-channel/85-of-consumers-think-local-reviews-older-than-3-months-arent-relevant/
http://www.ijicic.org/ijicic-130511.pdf
https://aclanthology.org/2023.findings-eacl.125.pdf
https://www.powerreviews.com/the-complete-guide-to-ratings-reviews/
https://pmc.ncbi.nlm.nih.gov/articles/PMC11639207/
https://arxiv.org/abs/2303.00923