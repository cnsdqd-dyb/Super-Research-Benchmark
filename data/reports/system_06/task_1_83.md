# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 3735a24d | **Time:** 125.72s | **Cost:** $0.14829
--------------------------------------------------------------------------------

# What Determines the Temporal Discount Function of Rating Contributions in Review Systems?

## Abstract

This research report examines the determinants of the temporal discount function of rating contributions in online review systems. Drawing upon behavioral economics, cognitive psychology, and information systems research, we synthesize evidence that the temporal discounting of rating contributions is shaped by a complex interplay of memory decay mechanisms, retrieval cues, platform algorithmic design, and individual psychological factors. Our analysis reveals that the temporal discount function in review systems is not uniform but rather exhibits hyperbolic characteristics, where the influence of past ratings diminishes at a declining rate over time. The presence of multimedia content, particularly review photos, serves as critical retrieval cues that partially counteract memory decay. Furthermore, platform algorithms impose their own temporal weighting schemes, typically emphasizing reviews from the past 60-90 days while systematically reducing the influence of older contributions. These findings have significant implications for understanding how consumer evaluations aggregate over time and how platform design choices shape the temporal dynamics of rating systems.

## 1. Introduction

Online review systems have become fundamental infrastructure in contemporary digital commerce, serving as primary quality signals for prospective consumers making purchase decisions. A product's overall rating functions as a critical heuristic that influences consumer behavior across diverse platforms, from e-commerce marketplaces to hospitality services and mobile application stores. Yet despite the centrality of these rating systems to marketplace functioning, significant gaps remain in our understanding of how individual rating contributions are weighted and aggregated over time.

The temporal dimension of rating contributions presents particularly complex questions for both researchers and practitioners. When a consumer writes a review, they engage in a memory-based task that requires recalling consumption experiences and translating these memories into numerical judgments [1]. The accuracy and valence of this translation process depend critically on the temporal distance between the consumption experience and the review submission moment. As memory traces weaken over time due to natural decay processes, the relationship between original experience and recorded evaluation becomes increasingly mediated by reconstruction processes that may introduce systematic biases.

This report investigates the temporal discount function that governs how rating contributions are valued and weighted as they age within review systems. We examine this function from multiple theoretical perspectives, integrating insights from temporal discounting research in behavioral economics, memory science in cognitive psychology, and algorithmic design in information systems. By synthesizing these perspectives, we aim to provide a comprehensive framework for understanding what determines the temporal weighting of rating contributions and how this weighting shapes the aggregate signals that influence consumer decision-making.

The significance of this inquiry extends beyond academic interest. Platform designers, sellers, and consumers all have stakes in understanding how temporal factors influence rating systems. For platforms, the design of temporal weighting mechanisms affects the accuracy and relevance of quality signals. For sellers, understanding these dynamics informs review management strategies. For consumers, awareness of temporal discounting in ratings supports more informed interpretation of aggregate scores. Our analysis addresses these practical concerns while grounding recommendations in rigorous theoretical foundations.

## 2. Theoretical Foundations of Temporal Discounting

### 2.1 The Nature of Temporal Discounting

Temporal discounting, also known as time discounting or delay discounting, refers to the tendency for individuals to devalue rewards and outcomes that are delayed in time relative to those that are immediately available [2]. This psychological phenomenon manifests across diverse domains of human decision-making, from financial choices involving intertemporal tradeoffs to everyday judgments about immediate gratification versus future benefits. The mathematical representation of temporal discounting typically takes the form of a discount function that maps temporal distance to subjective value, with the general structure expressing present utility as a decreasing function of delay.

The foundational insight from behavioral economics is that human beings do not discount future outcomes at a constant rate. Instead, empirical research consistently demonstrates that discount rates are hyperbolic, meaning they decline as the temporal horizon extends [3]. This pattern generates apparent inconsistencies in preference ordering across time, where an individual might prefer receiving \$100 today over \$110 in one month, yet simultaneously prefer receiving \$110 in 31 days over \$100 in 30 days. Such preference reversals emerge from the hyperbolic form of the discount function, which exhibits steep discounting for near-future delays and shallower discounting for distant-future delays.

The hyperbolic discount function can be formally expressed using the quasi-hyperbolic model proposed by Laibson, where the discount factor between periods t and t+k is given by:

$$\delta^k = \beta \cdot \gamma^k$$

In this formulation, β represents a present-bias parameter that captures the additional premium placed on immediate outcomes, while γ represents the per-period discount factor for delays beyond the present moment [4]. When β < 1, individuals exhibit present bias, systematically overweighing immediate rewards relative to future rewards of equivalent objective value.

### 2.2 Mathematical Models of Temporal Discounting

The mathematical specification of temporal discount functions has been a productive area of research, with competing functional forms offering different implications for understanding choice behavior. The exponential discount function, originally proposed by Samuelson, assumes constant proportional discounting:

$$U_t = \sum_{k=0}^{T-t} u(c_{t+k}) \cdot (1 + \rho)^{-k}$$

where ρ represents the constant discount rate and u(c) represents the utility of consumption at each period [5]. While mathematically elegant and ensuring temporal consistency in preferences, exponential discounting has been largely rejected by empirical evidence, which consistently shows that discount rates are not constant but rather vary with temporal distance.

The hyperbolic discount function, in contrast, provides empirically superior fits to observed choice data. The canonical hyperbolic form, often attributed to Mazur, specifies the discount factor as:

$$D(D) = \frac{1}{1 + kD}$$

where D represents delay in days and k represents the individual discount rate parameter [3]. This functional form generates the pattern of declining discount rates that characterizes human temporal preferences, with steeper discounting for short delays and progressively shallower discounting for longer delays.

More recent formulations have incorporated additional parameters to capture individual differences and contextual influences on discounting behavior. The β-δ model, for instance, introduces a discontinuity at the present moment, capturing the special psychological status of "now" versus "later":

$$U = u(x_0) + \beta \sum_{t=1}^{T} \delta^t u(x_t)$$

where the parameter β captures present bias and δ captures the per-period discount factor for future periods [4]. This model has proven particularly useful for understanding phenomena such as procrastination, addiction, and failure to follow through on intentions.

### 2.3 Psychological and Contextual Moderators

The temporal discount function is not fixed but rather varies systematically across individuals and contexts. Psychological factors including impulsivity, risk tolerance, and emotional state have been shown to influence discount rates [2]. Individuals with higher trait impulsivity tend to exhibit steeper temporal discounting, showing stronger preferences for immediate rewards even when future options are objectively superior. Similarly, emotional states such as stress or pleasure can temporarily shift discount rates, with negative emotional states often associated with increased discounting of future outcomes.

Contextual factors also shape temporal discounting in important ways. Social influences, including peer pressure and societal norms, can either increase or decrease discounting depending on the reference group's time preferences [2]. Past experiences, particularly negative experiences with delayed rewards that failed to materialize, can increase present bias and steepness of discounting. These contextual moderators suggest that the temporal discount function is not purely individual but rather emerges from the interaction between individual traits and situational factors.

## 3. Memory Processes and Rating Contributions

### 3.1 Review Generation as a Memory-Based Task

Generating an online review constitutes a fundamentally memory-based cognitive task. Consumers must engage in effortful retrieval of consumption experiences, reconstruct the details of their interactions with products or services, and translate these reconstructed memories into numerical ratings and textual commentary [1]. This process is subject to the well-documented limitations and biases of human memory, which have profound implications for the temporal dynamics of rating contributions.

Memory traces, the neural representations that encode past experiences, weaken over time through natural decay processes. This decay is not uniform but rather follows characteristic patterns that depend on the initial strength of the trace, the nature of the encoded material, and the presence of retrieval cues that can reactivate and strengthen fading memories. For review generation, this means that the temporal distance between consumption experience and review submission directly affects the accuracy and completeness of the retrieved information.

Research on memory and evaluation has demonstrated that recall accuracy depends critically on temporal distance. The association between specific attribute evaluations and overall ratings diminishes with longer delays, as the details of attribute-specific experiences become less accessible [1]. This pattern has important implications for understanding how the temporal discount function operates in rating systems: as time passes and memory traces decay, the specific details that informed original attribute ratings become less influential on the overall evaluation that gets recorded.

### 3.2 Memory Decay and Evaluation Transfer

The relationship between attribute ratings and overall ratings provides a window into how memory processes shape temporal discounting in review systems. When consumers provide ratings across multiple attribute dimensions, these specific judgments must somehow be integrated into an overall evaluation. The extent to which attribute-specific details are successfully retrieved and incorporated into the overall rating depends on the temporal distance from the original experience.

Greater temporal distance reduces recall of attribute-specific details, which in turn tempers the transfer of attribute evaluations to the overall rating [1]. This mechanism suggests that the temporal discount function for attribute rating contributions operates through memory-mediated pathways. When consumers review products shortly after consumption, vivid attribute-specific memories are accessible and exert strong influence on overall ratings. As time passes and these memories decay, their influence diminishes, and overall ratings may become based on more generalized impressions rather than specific attribute evaluations.

This process has been shown to reduce rating extremity over time. Consumers who provide more attribute ratings tend to give higher and less extreme overall ratings, a pattern that emerges because the presence of multiple rating channels distributes judgments across dimensions rather than concentrating them in a single overall evaluation [1]. The temporal dynamics of this effect are particularly interesting: as memory for specific attributes decays, the moderating influence of multiple rating channels may diminish, potentially allowing overall ratings to become more extreme as they age.

### 3.3 Retrieval Cues and Memory Reconstruction

While memory decay naturally weakens memory traces over time, retrieval cues can partly counteract this decay by reactivating and strengthening fading representations. In the context of online reviews, photographs attached to reviews serve as particularly vivid retrieval cues that can help consumers reconstruct their consumption experiences [1]. When review photos are present, they provide visual anchors that trigger memory retrieval and support more complete reconstruction of the original experience.

The presence of review photos thus moderates the temporal discount function for rating contributions. Without retrieval cues, memory traces decay according to their natural trajectory, and the influence of specific attribute ratings on overall evaluations diminishes with temporal distance. With retrieval cues in the form of photos, this decay process is slowed or partially reversed, as the visual content reactivates memory traces and improves evaluation transfer from attributes to overall ratings.

This moderation effect has important implications for understanding the temporal dynamics of rating systems. Reviews accompanied by photos may maintain their influence over longer temporal horizons than text-only reviews, as the visual content provides ongoing support for memory retrieval. Platform algorithms that weight reviews by recency may therefore need to account for the presence of retrieval cues, as photo-enhanced reviews may remain informative even when they are temporally distant from the current moment.

## 4. The Temporal Discount Function in Review Systems

### 4.1 Platform Algorithmic Weighting of Reviews

Beyond the psychological processes that shape individual rating contributions, the temporal discount function in review systems is substantially determined by platform algorithmic design. Major e-commerce platforms and app stores implement temporal weighting schemes that systematically prioritize recent reviews over older ones, operating under the assumption that recent reviews better reflect the current state of products and services [6].

The algorithmic temporal discount function implemented by platforms typically exhibits several key characteristics. First, recent reviews from the past 60-90 days carry substantially greater weight than older reviews, with the influence of reviews diminishing progressively as they age beyond this window [6]. Second, the weighting function is not linear but rather exhibits a steep decline for recent periods followed by a more gradual decline for older periods, suggesting a hyperbolic rather than exponential form. Third, while older reviews continue to contribute to cumulative averages, their influence on current search visibility and product ranking is minimal compared to recent contributions.

This algorithmic temporal discounting serves important functions for platform operations. By emphasizing recent reviews, platforms ensure that their quality signals remain responsive to changes in product quality, vendor reliability, or feature updates. A product that has improved will see its rating rise as recent positive reviews accumulate, while a product that has declined will experience rating drops as recent negative reviews outpace the influence of older positive reviews. This dynamic responsiveness supports consumer decision-making by providing temporally relevant information.

### 4.2 Hyperbolic Characteristics of Rating Influence

The temporal discount function governing rating contributions in review systems exhibits hyperbolic characteristics that parallel the discounting of future rewards in behavioral economics. The influence of individual rating contributions does not decline at a constant proportional rate but rather at a declining rate, with steep discounting for recent periods and shallower discounting for more distant periods.

This hyperbolic pattern can be formally expressed using the same functional form that describes intertemporal choice:

$$W(t) = \frac{1}{1 + k \cdot t}$$

where W(t) represents the weight assigned to a review at temporal distance t from the present moment, and k represents the platform-specific discount rate parameter [3]. Higher values of k indicate steeper discounting and greater emphasis on recent reviews, while lower values indicate more gradual decay and greater influence of older reviews.

The hyperbolic form of the temporal discount function has several important implications. First, it generates apparent inconsistencies in how reviews are weighted across different temporal windows. A review from one month ago might be given substantially less weight than a review from today, while a review from one year ago might be given only marginally less weight than a review from eleven months ago. Second, the hyperbolic form means that the effective discount rate varies depending on the temporal horizon under consideration, with higher implied rates for short horizons and lower implied rates for long horizons.

### 4.3 Individual Differences in Rating Temporal Dynamics

While platform algorithms impose a common temporal discount function on all reviews, individual differences among reviewers introduce additional heterogeneity in how temporal factors influence rating contributions. Research on temporal discounting has documented substantial individual differences in discount rates, with some individuals showing strong present bias and steep discounting while others exhibit more patient preferences and shallower discount functions [4].

These individual differences likely translate into differences in how reviewers weight recent versus distant experiences when constructing ratings. Reviewers with steeper discount rates may base their evaluations more heavily on recent experiences and less on the full consumption timeline, potentially leading to ratings that are more responsive to recency effects but less representative of overall experience quality. Conversely, reviewers with shallower discount rates may integrate experiences across the full temporal span of their product use, potentially producing ratings that are more stable but less responsive to recent changes in product quality.

Age represents another source of individual differences in temporal discounting for ratings. Research on aging and temporal discounting has produced mixed results, with some studies suggesting increased patience with age, others finding decreased patience, and still others finding no systematic age differences [7]. The relationship between age and discounting appears to be moderated by factors including socioeconomic status, cognitive ability, and life history considerations. For review systems, these findings suggest that the temporal discount function may vary across demographic groups in ways that platform algorithms do not currently capture.

## 5. Moderating Factors in Temporal Discounting of Ratings

### 5.1 The Role of Review Photos as Retrieval Cues

Review photographs serve as powerful retrieval cues that moderate the temporal discount function for rating contributions. When consumers attach photos to their reviews, they provide visual documentation that can trigger memory retrieval and support reconstruction of consumption experiences long after the original event [1]. This function of photos goes beyond their informational content about product appearance or performance; photos serve as cognitive anchors that counteract the natural decay of memory traces.

The moderating effect of photos on temporal discounting operates through multiple mechanisms. First, photos provide external storage of information that would otherwise need to be retrieved from memory, reducing the cognitive demands of review generation and potentially improving the accuracy of reported evaluations. Second, photos serve as retrieval cues that activate associated memories, bringing to mind details of the consumption experience that might otherwise remain inaccessible. Third, the act of selecting and attaching photos may itself create a distinctive memory trace that is more resistant to decay than the original consumption experience.

Empirical evidence supports the moderating role of photos in evaluation transfer. The association between attribute-specific ratings and overall ratings is stronger when reviews include photos, suggesting that visual retrieval cues facilitate the integration of specific experiences into holistic evaluations [1]. This moderation effect implies that the temporal discount function is shallower for photo-enhanced reviews than for text-only reviews, as the presence of retrieval cues partially counteracts the natural decay of memory influence over time.

### 5.2 Temporal Distance and Attribute Rating Effects

The number of attribute ratings provided by consumers moderates how temporal distance influences overall evaluations. When consumers provide ratings across multiple attribute dimensions, the distribution of judgments across dimensions reduces overall rating extremity and creates more stable evaluations [1]. This moderating effect interacts with temporal distance in important ways.

In the short term, the presence of multiple attribute rating channels discourages consumers from transferring evaluations of specific attributes to the overall rating. Consumers who rate multiple attributes produce overall ratings that are less extreme than would be predicted from their attribute-specific ratings alone. This pattern reflects a distribution effect, where extreme evaluations on individual attributes are balanced by moderate evaluations on other attributes, producing an overall rating that reflects the full complexity of the consumption experience.

Over time, as memory for specific attributes decays, the moderating influence of multiple rating channels may diminish. Without vivid attribute-specific memories to anchor evaluations, consumers may rely more heavily on generalized impressions that are less differentiated across attributes. This temporal dynamic suggests that the relationship between attribute rating quantity and overall rating extremity may itself be subject to temporal discounting, with the moderating effect strongest for recent reviews and progressively weaker for older reviews.

### 5.3 Platform-Specific Temporal Weighting Schemes

Different platforms implement varying temporal weighting schemes that shape the effective temporal discount function for rating contributions. E-commerce platforms like Amazon emphasize reviews from the past 60-90 days while systematically reducing the influence of older reviews on current search visibility and product rankings [6]. App stores similarly weight recent reviews more heavily, operating under the assumption that recent reviews better reflect the current state of applications and their maintenance.

The specific parameters of platform temporal weighting schemes vary in important ways. Some platforms implement relatively steep discounting, with review influence declining rapidly after the first few months. Others implement more gradual discounting, allowing older reviews to retain greater influence on aggregate ratings. These differences in algorithmic design translate into different effective temporal discount functions, with implications for how product quality signals are constructed and communicated to consumers.

The evolution of platform algorithms over time adds another layer of complexity to the temporal discount function. As platforms update their ranking algorithms, the weighting assigned to reviews of different ages may change, potentially retroactively altering the influence of existing reviews [6]. This dynamic suggests that the temporal discount function is not fixed but rather evolves as platform technology advances and strategic priorities shift.

## 6. Practical Implications and Design Considerations

### 6.1 Implications for Platform Design

Understanding the temporal discount function of rating contributions has important implications for platform design decisions. Platforms must balance competing objectives when designing temporal weighting schemes: they want ratings to reflect current product quality while also providing stable signals that are not overly sensitive to short-term fluctuations. The hyperbolic form of temporal discounting suggests that a gradual decline in review influence, rather than a sharp cutoff, may best serve these dual objectives.

The role of retrieval cues in moderating temporal discounting suggests that platforms should consider design features that support memory retrieval for older reviews. While photos attached to reviews serve this function for individual reviews, platforms might consider additional features such as prompts for contextual information, structured recall aids, or integration with personal records of purchase and use history. These features could help consumers generate more accurate and informative reviews even when temporal distance from consumption is substantial.

Platforms should also consider how their algorithmic temporal weighting interacts with the psychological temporal discounting of individual reviewers. If reviewers naturally discount their own memories of distant experiences, algorithmic discounting of distant reviews may create a double-discounting effect that overly suppresses the influence of older but still-relevant evaluations. Designing algorithms that account for this interaction could improve the accuracy and usefulness of aggregate rating signals.

### 6.2 Implications for Consumers and Sellers

For consumers, understanding temporal discounting in review systems supports more informed interpretation of aggregate ratings. Recognizing that recent reviews carry greater weight than older reviews helps consumers calibrate their expectations about product quality signals. A product with a high average rating based primarily on old reviews may not reflect current quality, while a product with a lower average rating that has recently improved may be better than its overall score suggests.

For sellers and product vendors, the temporal dynamics of review systems create strategic imperatives for review management. Maintaining a positive rating trajectory requires ongoing attention to recent reviews, as negative reviews can rapidly erode aggregate scores while positive reviews from distant periods have diminishing influence [6]. This dynamic creates incentives for prompt response to customer concerns and active encouragement of satisfied customers to leave recent reviews.

The moderating role of photos in temporal discounting suggests that sellers might encourage customers to include visual content in their reviews. Reviews with photos may maintain their influence over longer temporal horizons, providing more durable support for positive aggregate ratings. This strategy is particularly relevant for products where visual documentation of quality is informative and where consumption experiences can be effectively captured in photographs.

### 6.3 Future Research Directions

Several directions for future research emerge from this analysis. First, more precise estimation of the parameters of the temporal discount function in different platform contexts would support more accurate modeling of rating dynamics. While the hyperbolic form is well-established, the specific discount rate parameters likely vary across platforms, product categories, and consumer segments.

Second, research examining how individual differences in temporal discounting relate to rating behavior would illuminate the psychological mechanisms underlying review generation. If individuals who exhibit steeper discounting in monetary choice contexts also show stronger recency effects in their reviews, this would support the hypothesis that a common psychological process underlies both phenomena.

Third, experimental research on interventions that moderate temporal discounting in reviews could inform platform design. If certain prompting strategies or interface designs can reduce the recency bias in reviews, platforms could implement these features to improve the accuracy and stability of rating signals.

## 7. Conclusion

The temporal discount function of rating contributions in review systems is determined by a complex interplay of psychological, algorithmic, and contextual factors. At the psychological level, the generation of reviews is a memory-based task subject to the same temporal discounting processes that govern intertemporal choice more broadly. Memory traces decay over time, reducing the accessibility of specific attribute evaluations and moderating their influence on overall ratings. The hyperbolic form of this psychological discount function generates characteristic patterns of declining influence that parallel the discounting of future rewards in behavioral economics.

At the algorithmic level, platforms implement temporal weighting schemes that systematically prioritize recent reviews over older ones. These schemes serve important functions in maintaining the responsiveness of quality signals to current product states, but they also impose an additional layer of temporal discounting on top of the psychological processes of individual reviewers. The interaction between psychological and algorithmic discounting shapes the effective temporal discount function that determines how rating contributions influence aggregate signals.

Retrieval cues, particularly review photos, serve as important moderators of temporal discounting by counteracting memory decay and supporting reconstruction of consumption experiences. The presence of visual content in reviews slows the decline of review influence over time, creating a shallower temporal discount function for photo-enhanced reviews. This moderation effect has implications for platform design and seller strategy, suggesting value in features and practices that support memory retrieval during review generation.

Understanding the temporal discount function of rating contributions supports more effective interpretation of review signals, more informed platform design decisions, and more strategic review management practices. As review systems continue to evolve in importance for consumer decision-making, the theoretical frameworks and empirical findings synthesized in this report provide foundations for future research and practical application.

---

## References

[1] ScienceDirect. "Attribute Ratings and Overall Evaluations in Online Review Systems." *Information Systems Research*, 2025. https://www.sciencedirect.com/science/article/abs/pii/S0378720625001788

[2] Investopedia. "Temporal Discounting." 2024. https://www.investopedia.com/temporal-discounting-7972594

[3] Nature. "Temporal Discount Rates and Procrastination." *Scientific Reports*, 2024. https://www.nature.com/articles/s41598-024-65110-4

[4] NBER. "Estimating Discount Functions from Consumption Choices." Working Paper 13314. https://www.nber.org/system/files/working_papers/w13314/w13314.pdf

[5] KTH. "Hyperbolic Discounting and Exponential Smoothing." 2015. https://people.kth.se/~gryne/papers/Hyperbol_150401.pdf

[6] eCommerce Sellers HQ. "Guide to Amazon's Review Algorithm." 2024. https://www.ecomsellershq.com/blog/guide-to-amazons-review-algorithm/

[7] PMC. "Temporal Discounting and Aging: A Systematic Review." *Nature*, 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC8827494/

## Annotations


## Sources
[1] http://hrsonline.isr.umich.edu/sitedocs/conference/200111/paper12.pdf
[2] https://arxiv.org/html/2505.20243v2
[3] https://arxiv.org/pdf/2405.18068
[4] https://en.wikipedia.org/wiki/Hyperbolic_discounting
[5] https://eprints.lse.ac.uk/116449/1/s41562_022_01392_w_6_.pdf
[6] https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/2009-KIm-and-Zauberman-JNPE-vol2(2)-95-101.pdf
[7] https://link.springer.com/article/10.3758/s13428-018-1179-4
[8] https://medium.com/nudge-notes/temporal-discounting-designing-for-present-vs-future-rewards-6e9c92971610
[9] https://people.kth.se/~gryne/papers/Hyperbol_150401.pdf
[10] https://pmc.ncbi.nlm.nih.gov/articles/PMC3462010/
[11] https://pmc.ncbi.nlm.nih.gov/articles/PMC8827494/
[12] https://repository.uantwerpen.be/docman/irua/e52e44/195701.pdf
[13] https://rlj.cs.umass.edu/2025/papers/RLJ_RLC_2025_321.pdf
[14] https://thisisglance.com/learning-centre/why-dont-my-perfect-5-star-reviews-boost-downloads
[15] https://www.cs.bu.edu/faculty/crovella/paper-archive/smma18-online-ratings.pdf
[16] https://www.ecomsellershq.com/blog/guide-to-amazons-review-algorithm/
[17] https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.643670/full
[18] https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.865702/full
[19] https://www.investopedia.com/temporal-discounting-7972594
[20] https://www.mdpi.com/0718-1876/16/4/38
[21] https://www.mdpi.com/2076-3417/10/7/2204
[22] https://www.nature.com/articles/s41598-024-65110-4
[23] https://www.nber.org/system/files/working_papers/w13314/w13314.pdf
[24] https://www.renascence.io/journal/temporal-discounting-valuing-immediate-rewards-over-long-term-gains
[25] https://www.sciencedirect.com/science/article/abs/pii/S0378720624001010
[26] https://www.sciencedirect.com/science/article/abs/pii/S0378720625001788
[27] https://www.sciencedirect.com/science/article/abs/pii/S0957417421010204
[28] https://www.sciencedirect.com/science/article/pii/S0167811625000473