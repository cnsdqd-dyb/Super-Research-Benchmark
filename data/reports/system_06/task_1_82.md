# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 4f0431c5 | **Time:** 104.78s | **Cost:** $0.03522
--------------------------------------------------------------------------------

# How is the Timing Threshold for Content Switching Determined in Live Streaming Interaction?

## Executive Summary

Content switching in live streaming represents one of the most technically challenging aspects of modern video delivery systems, requiring careful calibration of timing thresholds that balance multiple competing objectives. This report provides an in-depth analysis of how timing thresholds for content switching are determined in live streaming interactions, drawing upon current research and industry practices. The determination of these thresholds involves a complex interplay of technical factors including network conditions, buffer states, encoding parameters, and protocol characteristics, alongside user experience considerations such as tolerance for quality changes and acceptable latency levels. The research reveals that effective threshold determination requires adaptive algorithms that can respond dynamically to changing conditions while maintaining consistent quality of experience. Key findings indicate that modern systems employ multi-layered threshold frameworks that consider both system-level metrics and user behavioral patterns, with optimal thresholds varying significantly based on the specific use case, audience characteristics, and interactivity requirements.

## 1. Introduction

### 1.1 Background and Context

The dramatic rise in live streaming adoption across social media platforms, entertainment services, and professional broadcasting has created unprecedented demands on content delivery infrastructure. As noted in industry analysis, the expected future trajectory of live streaming, driven by social and economic factors, makes it critical that streaming platforms deliver smooth, reliable, and high-quality experiences to increasingly large and geographically dispersed audiences [1]. At the heart of this challenge lies the question of content switching—when and how should a streaming system transition between different quality levels, camera angles, audio tracks, or other content variants to maintain optimal user experience?

Content switching in live streaming encompasses multiple dimensions of adaptation. Quality switching, where the system transitions between different bitrate representations of the same content, represents the most commonly studied form of content switching. However, the scope extends to camera switching in multi-camera productions, language track selection, and even transitions between different streams in scenarios involving multiple concurrent broadcasts. The timing threshold for these switches—the conditions under which a switch is triggered and the point at which it executes—fundamentally shapes the viewer's experience.

The determination of appropriate timing thresholds is complicated by the inherent tension between competing objectives. Lower latency enhances interactivity but may increase the likelihood of playback interruptions. Higher quality improves visual fidelity but requires more bandwidth and may lead to more frequent rebuffering events. As research has demonstrated, frequent switching negatively impacts overall user experience, yet users generally prefer quality switching over stall events, creating a nuanced optimization problem [2]. Understanding how practitioners and researchers approach this problem requires examining both the technical mechanisms and the theoretical frameworks that guide threshold determination.

### 1.2 Research Objectives

This report aims to provide a comprehensive examination of timing threshold determination for content switching in live streaming by addressing several key questions. First, we investigate the fundamental technical factors that influence threshold selection, including network characteristics, buffer dynamics, and protocol constraints. Second, we explore how user experience considerations shape threshold determination, examining concepts such as viewer tolerance thresholds and quality of experience metrics. Third, we analyze the algorithmic approaches employed in modern adaptive streaming systems to dynamically adjust thresholds based on real-time conditions. Finally, we consider the emerging research directions and future challenges in threshold-based content switching.

## 2. Technical Foundations of Content Switching

### 2.1 Understanding Latency in Live Streaming

Before examining content switching thresholds specifically, it is essential to establish a clear understanding of latency in live streaming contexts. Latency can be defined as the time between the initialization of a data transfer and the actual start of that transfer, or more specifically in video streaming, as the delay between the moment a video frame is captured and the moment it is displayed to the user [1]. This delay represents the cumulative effect of multiple processing stages in the streaming pipeline, including video capture, encoding, packaging, content delivery network distribution, segment buffering, and decoding.

The significance of latency varies dramatically across different streaming scenarios. For live streamed events such as video game tournaments, sports contests, or art auctions, latency is a crucial aspect where even delays of 10-30 seconds can lead to disrupted streams and unreliable user experiences [1]. In settings where real-time information is paramount, each second of delay can meaningfully impact the viewer's engagement and satisfaction. This stands in contrast to on-demand streaming scenarios where moderate latency is generally acceptable.

The relationship between latency and content switching is bidirectional. On one hand, latency constraints influence when switches can occur—systems with lower latency budgets have less flexibility in timing switches without risking playback interruptions. On the other hand, the manner in which switches are executed contributes to overall latency, particularly when switches require buffer refilling or reinitialization. Understanding this interplay is essential for effective threshold determination.

### 2.2 Streaming Protocols and Their Latency Characteristics

The choice of streaming protocol fundamentally constrains the range of achievable latencies and consequently influences content switching threshold determination. Contemporary streaming protocols fall into three main categories, each with distinct latency profiles [3].

Traditional streaming protocols, including RTSP (Real-Time Streaming Protocol) and RTMP (Real-Time Messaging Protocol), typically operate in the range of 1-3 seconds of latency. These protocols have been widely adopted for their reliability and compatibility with existing infrastructure, though they lack some of the adaptive capabilities of more modern approaches.

HTTP-based adaptive streaming protocols, including HLS (HTTP Live Streaming), HDS (HTTP Dynamic Streaming), Smooth Streaming, and MPEG-DASH (Dynamic Adaptive Streaming over HTTP), offer latency ranges spanning from approximately 5 seconds to over 45 seconds [3]. The wide range within this category reflects the significant variation in implementation approaches and configuration options. Traditional HLS implementations, for example, often exhibit latency of 30 seconds or more due to segment size recommendations that multiply the Group of Pictures (GOP) duration by three to provide buffer flexibility [4]. However, Low-Latency HLS variants have emerged specifically to address this limitation, enabling significantly reduced latency while maintaining adaptive streaming capabilities.

Emerging protocols such as WebRTC (Web Real-Time Communication) enable latency under 100 milliseconds, approaching true real-time interaction [3]. WebRTC's low-latency characteristics make it particularly suitable for applications requiring high degrees of viewer-to-broadcaster interactivity, though its complexity and infrastructure requirements present implementation challenges. As documented in practical deployments, WebRTC implementations must carefully address Network Address Translation (NAT) configuration issues, often requiring strategically placed TURN (Traversal Using Relays around NAT) servers to maintain acceptable latency for all users [1].

The protocol selection thus establishes a baseline latency envelope within which content switching must operate. Systems targeting ultra-low latency (under 1 second) have fundamentally different switching threshold considerations compared to those operating in the 30-second range typical of traditional broadcast-style delivery.

### 2.3 Buffer Dynamics and Segment Structure

The buffer represents the central mechanism through which streaming systems manage the trade-off between latency and playback continuity. Buffer dynamics directly influence content switching thresholds because switches typically require buffer manipulation—either draining buffer contents to switch to a lower quality or refilling buffer when switching to higher quality.

Traditional DASH-based adaptive bitrate (ABR) algorithms focus on quality of experience metrics such as downloading high-quality video content and minimizing playback interruptions and video quality changes [5]. However, these algorithms often overlook the need to target low-latency streaming, creating tension between traditional ABR objectives and real-time interaction requirements. The buffer serves as the shock absorber that accommodates network variability, but its size directly impacts end-to-end latency.

Segment structure plays a crucial role in determining switching opportunities. The packager typically defines segment sizes corresponding to Groups of Pictures (GOPs), with each segment representing a discrete chunk of video content that can be independently decoded. Once a segment size is defined, players typically maintain a buffer window equivalent to multiple segments to negotiate network conditions that slow the stream or cause packet drops [4]. For HLS, the common recommendation of three segments of 6 seconds each results in approximately 30 seconds of baseline latency.

Modern low-latency approaches have introduced innovations to reduce this latency while maintaining switching flexibility. The HESP (HTTP Efficient Streaming Protocol) approach, for example, introduces Initialization Frames generated at the encoder and output as a second stream [4]. These initialization frames serve as switching points that players can utilize, enabling quality transitions without requiring full segment downloads. The protocol focuses on standardized low-latency chunk sizes (e.g., 200ms) and ultra-fast stream switching capabilities, demonstrating how fundamental architectural decisions impact switching threshold determination.

## 3. User Experience Considerations in Threshold Determination

### 3.1 Quality of Experience Metrics

The determination of content switching thresholds must ultimately serve the goal of maximizing user experience quality. Research has established that quality switching represents a significant factor in overall quality of experience (QoE), with studies revealing that frequent switching negatively impacts user satisfaction [2]. However, the relationship between switching and QoE is nuanced—users generally prefer quality switching over stall events, suggesting that some degree of switching is preferable to playback interruptions.

The impact of switching on QoE operates through multiple mechanisms. Switches that affect quality level and switching time have been shown to influence user persuasion and engagement [2]. Abrupt quality changes can be jarring to viewers, creating a sense of instability even when the overall viewing experience remains technically functional. The timing of switches relative to scene changes, action moments, or dialogue can amplify or mitigate these negative effects.

Research investigating the trade-off between buffering delays and playback interruptions has revealed that, compared to rebuffering events, playback interruptions negatively impact QoE more significantly [2]. This finding has important implications for threshold determination—systems should generally prioritize avoiding interruptions over achieving maximum quality, suggesting that conservative switching thresholds may be appropriate in many scenarios.

The challenge of balancing these considerations is compounded by the variability of user expectations and tolerances. Different user segments may have vastly different preferences regarding the acceptable frequency and magnitude of quality changes. Some users prioritize consistent quality even at the expense of resolution, while others prefer higher peak quality with greater variability. Effective threshold determination must either accommodate this variability through personalization or establish default thresholds that optimize for the average user.

### 3.2 Viewer Tolerance Thresholds

Recent research in live stream recommendation has introduced the concept of viewer-specific thresholds representing individual tolerances for content characteristics [6]. This threshold-based modeling approach recognizes that viewers have varying levels of patience and satisfaction with different streaming conditions, and that these tolerances can be systematically modeled and predicted.

The theoretical foundation for viewer tolerance thresholds draws upon hedonic decline theory, which suggests that viewer preference for a particular stream tends to decrease over time during continuous viewing [6]. This decline is not uniform but rather varies based on content characteristics, viewer mood, and environmental factors. Understanding and modeling this decline process enables more accurate prediction of viewer behavior and more effective content switching decisions.

The interaction between viewer tolerance thresholds and content switching is bidirectional. On one hand, viewer tolerance determines how much quality degradation or buffering a viewer will accept before abandoning a stream, informing the minimum acceptable quality thresholds. On the other hand, the manner in which switches are executed can influence viewer tolerance—smooth, well-timed switches may be less likely to trigger viewer departure than abrupt, disruptive ones.

Research has demonstrated that incorporating user behavior theory into data-driven modeling methods can significantly improve predictive performance for live stream recommendation [6]. The proposed interaction-aware predictive framework systematically models viewer changing preference through threshold-based modeling and interaction-aware preference decline modeling, providing a more comprehensive understanding of viewer watching behaviors.

### 3.3 Interactivity Requirements and Latency Sensitivity

The degree of interactivity required in a streaming scenario directly influences appropriate latency targets and consequently content switching thresholds. As one industry analysis succinctly states, "the greater the degree of interactivity required, the lower latency must be" [3]. This principle has profound implications for threshold determination.

Different use cases exhibit dramatically different interactivity requirements. Broadcast experiences such as live news and sports streaming typically require reduced latency in the range of 5-18 seconds, with the goal of competing with cable and satellite broadcasts to avoid spoilers [3]. In these scenarios, viewers expect to see events roughly simultaneously with broadcast television viewers, and significant delays can lead to spoiled experiences through social media or other channels.

At the other end of the spectrum, applications requiring real-time interaction—such as video conferencing, live gaming, or interactive entertainment—demand latency under 1 second to enable meaningful two-way communication [7]. In these scenarios, content switching thresholds must be extremely tight to avoid any perceptible delay that could disrupt the interactive experience.

The intermediate range encompasses scenarios with moderate interactivity requirements. Low-latency streaming typically means a delay of 1-5 seconds between the live feed and what viewers see, enabling near-real-time interaction with the audience [7]. Most social media platforms including Facebook Live, YouTube, and Twitch offer low-latency modes that provide sufficient latency for real-time interaction in most scenarios, though ultra-low latency may be limited due to scale and protocol constraints.

## 4. Algorithmic Approaches to Threshold Determination

### 4.1 Adaptive Bitrate Algorithms

Adaptive bitrate (ABR) algorithms form the technical foundation for quality switching in modern streaming systems. These algorithms determine when and how to switch between different bitrate representations based on real-time analysis of network conditions [8]. The threshold determination in ABR algorithms typically falls into three categories: rate-based approaches, buffer-based approaches, and hybrid approaches that combine elements of both.

Rate-based algorithms focus on adjusting bitrate according to available network bandwidth, using throughput estimation to select appropriate quality levels. These algorithms establish thresholds based on the relationship between estimated bandwidth and the bitrate requirements of different quality levels. When estimated bandwidth exceeds a threshold relative to a quality level's requirements, the algorithm may trigger an upgrade; conversely, when bandwidth falls below thresholds, downgrades may be triggered.

Buffer-based algorithms aim to maintain sufficient buffer occupancy to prevent playback interruptions, establishing thresholds based on buffer state. These algorithms typically define thresholds for buffer levels that trigger quality increases or decreases. For example, a system might increase quality when buffer occupancy exceeds 80% of capacity and decrease quality when it falls below 30%.

Hybrid approaches combine rate and buffer signals to make more robust switching decisions. These algorithms establish multi-dimensional thresholds that consider both network conditions and buffer state, often using weighted combinations or decision trees to determine appropriate quality levels.

The challenge of threshold determination in ABR algorithms is complicated by the need to balance multiple objectives. As noted in research on low-latency streaming, traditional ABR algorithms often overlook the need to target low-latency streaming, focusing instead on quality and interruption metrics [5]. This creates a need for specialized algorithms designed specifically for live streaming scenarios where latency is critical.

### 4.2 Threshold-Based Modeling Frameworks

Beyond traditional ABR algorithms, recent research has developed more sophisticated threshold-based modeling frameworks for streaming systems. These frameworks approach threshold determination as an optimization problem, seeking to establish thresholds that maximize some objective function while satisfying constraints.

One notable approach involves threshold queries over streaming joins, where the goal is to trigger an alarm when certain conditions are met [9]. The framework formalizes the problem of determining when tuples in streaming data can be omitted without losing the ability to detect threshold violations. This approach has applications in load shedding, where tuples are dropped to prevent system overloading and increased latency.

The research demonstrates that under certain conditions, tuples can be systematically omitted based on threshold relationships without compromising system objectives [9]. Specifically, if a function f is quasiconvex with respect to one stream and there exist tuples with middle values, the middle tuple may be redundant and can be omitted. This insight has implications for content switching, suggesting that certain intermediate quality levels may be unnecessary if the system can reliably transition between adjacent levels.

The threshold determination process in these frameworks involves establishing bounds on acceptable values and then searching for optimal thresholds within those bounds. Research on streaming data approximation describes methods for choosing thresholds that guarantee coverage of the ideal threshold within a multiplicative factor [10]. The algorithm maintains monotonically decreasing estimates for minimum thresholds with the property that this minimum threshold should be the largest possible that would cause the algorithm to construct a solution that perfectly interpolates the data.

### 4.3 Dynamic Threshold Adjustment

Static thresholds rarely provide optimal performance in live streaming scenarios where network conditions, content characteristics, and viewer behaviors continuously evolve. Dynamic threshold adjustment mechanisms enable systems to adapt their switching criteria based on observed conditions and outcomes.

Research on adaptive streaming has developed algorithms for dynamic threshold adjustment based on stall analysis [11]. The ARTEMIS algorithm, for example, computes the average stall duration and adjusts thresholds according to the difference between current and historical stall characteristics. When stalling is significantly higher than in previous time slots, the algorithm triggers threshold adjustments to decrease stalling.

The dynamic adjustment process involves several key components. First, the system monitors relevant metrics including buffer occupancy, throughput, stall frequency, and quality change frequency. Second, it compares current metrics against historical baselines and threshold values. Third, it adjusts thresholds based on the observed differences, typically using rules derived from empirical research or optimization objectives.

The challenge of dynamic adjustment lies in balancing responsiveness to changing conditions with stability to avoid oscillation. If thresholds adjust too rapidly, the system may exhibit erratic behavior with frequent quality fluctuations. If adjustments are too slow, the system may fail to respond adequately to significant changes in network conditions or viewer behavior.

Machine learning approaches increasingly enable more sophisticated dynamic threshold adjustment. Content delivery networks have begun leveraging real-time machine learning to predict user behavior, analyze network conditions, and dynamically adjust parameters to reduce latency [8]. These approaches can identify complex patterns in streaming data that rule-based systems might miss, potentially enabling more effective threshold determination.

### 4.4 Content-Aware Threshold Determination

Content-aware approaches to threshold determination recognize that different types of content have different characteristics that influence optimal switching behavior. Complex content with high motion or detailed textures may require different threshold settings than static or simple content.

Content-aware VOD solutions typically rely on offline search in the bitrate and resolution spaces to find a bitrate ladder where chosen pairs provide good coverage of quality metrics for the given content [11]. However, the exhaustive search required for this approach imposes latency unacceptable for real-time operation in live streaming scenarios.

For live streaming, content-aware threshold determination must operate in real-time, limiting the complexity of content analysis that can be performed. Simplified content complexity metrics, such as motion vectors or texture analysis results from the encoding process, can inform threshold adjustment without requiring extensive additional computation.

Research on optimizing track switching for smooth playback has demonstrated the importance of intelligent switch timing that considers both buffer state and segment boundaries [12]. By identifying optimal moments for quality switches, systems can reduce the likelihood of playback interruptions while maintaining quality adaptation capabilities.

## 5. Implementation Considerations and Best Practices

### 5.1 System Architecture for Threshold-Based Switching

Implementing effective threshold-based content switching requires careful attention to system architecture. The architecture must support real-time monitoring of relevant metrics, rapid decision-making based on threshold comparisons, and efficient execution of switching operations.

The monitoring subsystem collects data from multiple sources including network interfaces, buffer management components, and player state tracking. This data must be collected with minimal overhead to avoid contributing to latency, and must be aggregated in ways that enable meaningful threshold comparisons. The sampling rate and aggregation methodology significantly impact the effectiveness of threshold-based switching.

The decision subsystem evaluates collected data against established thresholds and determines whether switching operations should be triggered. This subsystem must operate with low latency to ensure that switches occur at appropriate times, particularly in fast-changing network conditions. The threshold evaluation logic must be carefully optimized to minimize decision latency while maintaining accuracy.

The execution subsystem implements the actual content switch, coordinating with the player to transition between quality levels or content variants. The efficiency of this subsystem directly impacts the user-perceived quality of switches—poorly executed switches may cause visible artifacts, brief interruptions, or other quality degradations.

### 5.2 Parameter Tuning and Optimization

Establishing appropriate threshold values requires systematic parameter tuning based on the specific deployment context. Factors influencing optimal thresholds include the target audience characteristics, typical network conditions, content types, and quality objectives.

A common approach to parameter tuning involves simulation-based optimization, where system behavior is modeled under various threshold configurations and network conditions to identify settings that optimize desired metrics. This approach enables exploration of a wide parameter space without risking impact on live viewers.

A/B testing represents another valuable tuning approach, where different threshold configurations are deployed to different user segments and compared based on observed quality of experience metrics. This approach provides real-world validation of threshold settings but requires careful experimental design to ensure valid comparisons.

Research on threshold selection describes methods for automatic tuning of parameters through search procedures [10]. The method processes data in an online way to maintain estimates for optimal thresholds, with the property that the minimum threshold should be the largest possible that would cause the algorithm to achieve desired performance. This approach enables continuous adaptation of thresholds based on observed system behavior.

### 5.3 Handling Edge Cases and Failure Modes

Effective threshold-based switching systems must anticipate and handle various edge cases and failure modes that could degrade user experience.

Network volatility presents a significant challenge, as rapidly changing network conditions can cause threshold-based systems to oscillate between quality levels. Mitigation strategies include hysteresis in threshold comparisons, where switches require conditions to exceed thresholds by certain margins before triggering, and cooldown periods that prevent rapid successive switches.

Buffer exhaustion represents another critical failure mode, where threshold-based switching decisions deplete buffer resources and lead to playback interruptions. Systems must establish minimum buffer thresholds that prevent aggressive quality increases when buffer levels are low, even if other conditions would suggest upgrading.

Content transitions, such as scene changes or commercial breaks, can create artifacts if switches occur at inappropriate times. Some systems implement content awareness to avoid switching during high-importance moments, though this requires additional complexity in the threshold evaluation logic.

## 6. Emerging Research and Future Directions

### 6.1 Machine Learning Approaches

Machine learning is increasingly applied to threshold determination in streaming systems, offering the potential to identify complex patterns and make more nuanced switching decisions than traditional rule-based approaches.

Deep learning models can potentially learn optimal switching policies directly from data, bypassing the need for explicit threshold specification. These models can incorporate multiple input features including network metrics, buffer state, content characteristics, and historical viewer behavior to predict optimal switching decisions.

Reinforcement learning approaches treat threshold determination as a sequential decision problem, where the system learns to maximize long-term viewer satisfaction through trial and error. These approaches can adapt to changing conditions over time and potentially discover switching strategies that outperform hand-designed thresholds.

The application of machine learning to live streaming threshold determination remains an active area of research, with significant challenges including the need for real-time inference, the difficulty of obtaining labeled training data, and the complexity of ensuring consistent behavior across diverse conditions.

### 6.2 Cross-Layer Optimization

Future threshold determination approaches may increasingly consider cross-layer optimization, where decisions at the application layer are informed by conditions at lower layers of the network stack.

Transport layer information, such as TCP congestion signals or QUIC stream characteristics, can provide early indicators of network conditions that may not yet be reflected in application-layer metrics. Incorporating this information into threshold determination could enable more proactive switching decisions.

Physical layer information, including signal strength, channel conditions, and mobility patterns for mobile users, can further inform switching decisions. Systems that can anticipate degradation based on physical layer conditions may be able to initiate switches before application-layer symptoms appear.

The challenge of cross-layer optimization lies in the complexity of implementing such systems and the potential for tight coupling between layers to reduce flexibility and maintainability.

### 6.3 Personalization and User Modeling

Future systems may increasingly personalize threshold determination based on individual user characteristics and preferences. Rather than applying uniform thresholds across all viewers, systems could adapt thresholds to optimize for each viewer's specific tolerances and preferences.

Viewer modeling approaches can predict individual user tolerance for quality changes, buffering, and latency based on historical behavior and demographic or contextual factors. These predictions can inform personalized threshold settings that maximize individual satisfaction.

The challenge of personalization lies in balancing the benefits of individual optimization against the complexity of maintaining and updating user models, as well as privacy considerations related to collecting and processing user data.

## 7. Conclusion

The determination of timing thresholds for content switching in live streaming represents a multifaceted challenge that sits at the intersection of networking technology, user experience research, and algorithmic design. This report has examined the technical foundations, user experience considerations, algorithmic approaches, and implementation practices that guide threshold determination in modern streaming systems.

The research reveals that effective threshold determination requires balancing multiple competing objectives. Technical factors including protocol characteristics, buffer dynamics, and network conditions establish the envelope within which thresholds can operate. User experience considerations, including quality of experience metrics, viewer tolerance thresholds, and interactivity requirements, define the optimization objectives that thresholds should serve. Algorithmic approaches, ranging from traditional adaptive bitrate algorithms to sophisticated machine learning methods, provide the mechanisms for computing and adjusting thresholds based on real-time conditions.

The field continues to evolve rapidly as streaming platforms serve increasingly large and demanding audiences. Emerging research directions including machine learning approaches, cross-layer optimization, and personalization offer promising avenues for improving threshold determination. However, significant challenges remain in implementing these approaches at scale while maintaining the reliability and consistency that viewers expect.

For practitioners designing and operating streaming systems, the key takeaway is that threshold determination cannot be treated as a static configuration problem. Effective content switching requires dynamic, adaptive approaches that respond to changing conditions while maintaining focus on the ultimate goal: providing viewers with a seamless, high-quality streaming experience. The thresholds that achieve this goal will vary based on specific use cases, audience characteristics, and technical constraints, making careful analysis and continuous optimization essential for success.

## References

[1] D. Agelson, "Demystifying and Tackling Live Streaming Latency," Medium, 2024. [Online]. Available: https://dfagelson.medium.com/demystifying-and-tackling-live-streaming-latency-48c999d30a92

[2] B. Babak et al., "Quality Switching in Adaptive Video Streaming," *Electronics*, vol. 14, no. 13, p. 2587, 2025.

[3] Wowza Media Systems, "Latency Scenarios for Every Use Case," Wowza Guide, 2017. [Online]. Available: https://www.wowza.com/wp-content/uploads/Guide-Latency-Scenarios-for-Every-Use-Case.pdf

[4] The Broadcast Bridge, "How to Achieve Broadcast-Grade Latency for Live Video Streaming," 2024. [Online]. Available: https://www.thebroadcastbridge.com/content/entry/18709/how-to-achieve-broadcast-grade-latency-for-live-video-streaming

[5] W. Wu et al., "Low-Latency Adaptive Bitrate Streaming," *Proceedings of the 2024 ACM SIGCOMM Conference*, 2024.

[6] W. Wu et al., "Interaction-Aware Predictive Framework for Live Stream Recommendation," *VLDB 2021*, 2021. [Online]. Available: https://pages.cs.wisc.edu/~wentaowu/papers/vldb21-threshold.pdf

[7] Switcher Studio, "Low Latency Video Streaming," 2024. [Online]. Available: https://www.switcherstudio.com/blog/low-latency-video-streaming

[8] S. Kumar et al., "Adaptive Video Streaming: Algorithms and Implementation," *International Journal of Media and Animation Research*, vol. 6, no. 7, 2024.

[9] W. Wu et al., "Threshold Queries over Streaming Joins," *VLDB 2021*, 2021. [Online]. Available: https://pages.cs.wisc.edu/~wentaowu/papers/vldb21-threshold.pdf

[10] W. Wu et al., "Threshold Selection for Streaming Data Approximation," *EuroVis 2022 Supplementary Proceedings*, 2022. [Online]. Available: https://cse.engineering.nyu.edu/chiang/EuroVis22-Paper-Supple.pdf

[11] K. Tashtarian et al., "ARTEMIS: Adaptive Real-Time Streaming," *USENIX NSDI 2024*, 2024. [Online]. Available: https://www.usenix.org/system/files/nsdi24-tashtarian.pdf

[12] M. Hoang, "Optimizing Track Switching for Smooth Playback," M.S. Thesis, Tampere University, 2024. [Online]. Available: https://trepo.tuni.fi/bitstream/10024/229088/3/MinhHoang.pdf

## Annotations


## Sources
[1] http://ijmrap.com/wp-content/uploads/2024/01/IJMRAP-V6N7P83Y23.pdf
[2] https://cse.engineering.nyu.edu/chiang/EuroVis22-Paper-Supple.pdf
[3] https://dfagelson.medium.com/demystifying-and-tackling-live-streaming-latency-48c999d30a92
[4] https://pages.cs.wisc.edu/~wentaowu/papers/vldb21-threshold.pdf
[5] https://pubsonline.informs.org/doi/10.1287/isre.2022.1160
[6] https://scholarspace.manoa.hawaii.edu/bitstreams/5a08637b-163a-410a-9e33-e7f523597bc9/download
[7] https://trepo.tuni.fi/bitstream/10024/229088/3/MinhHoang.pdf
[8] https://www.mdpi.com/2079-9292/14/13/2587
[9] https://www.sciencedirect.com/science/article/abs/pii/S016792362300221X
[10] https://www.switcherstudio.com/blog/low-latency-video-streaming
[11] https://www.thebroadcastbridge.com/content/entry/18709/how-to-achieve-broadcast-grade-latency-for-live-video-streaming
[12] https://www.usenix.org/system/files/nsdi24-tashtarian.pdf
[13] https://www.wowza.com/wp-content/uploads/Guide-Latency-Scenarios-for-Every-Use-Case.pdf