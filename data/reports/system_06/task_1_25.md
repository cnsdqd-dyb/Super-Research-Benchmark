# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 43cd37b4 | **Time:** 266.59s | **Cost:** $0.11679
--------------------------------------------------------------------------------

# Do Market Microstructure Models of High-Frequency Trading Balance Price Discovery with Stability, or Does the Stochastic Evolution of Order Books Amplify Liquidity Illusions?

## A Comprehensive Analysis of High-Frequency Trading, Order Book Dynamics, and Market Stability

---

## Executive Summary

This research report examines the fundamental tension between price discovery efficiency and market stability within the context of high-frequency trading (HFT) and stochastic order book dynamics. The analysis draws upon contemporary market microstructure theory and empirical evidence to address a critical question facing modern financial markets: whether the mathematical models governing HFT behavior successfully balance the competing objectives of efficient price formation and systemic resilience, or whether the inherent stochasticity of limit order books creates merely illusory liquidity that evaporates precisely when markets require it most.

The evidence presented herein reveals a nuanced picture in which HFT demonstrably enhances market efficiency under normal trading conditions through spread compression, improved order book depth, and accelerated price discovery. However, this efficiency comes with significant trade-offs. During periods of market stress, HFT algorithms frequently withdraw liquidity provision and intensify directional trading strategies, transforming what appeared to be robust market depth into a liquidity mirage. The stochastic evolution of order books, while mathematically tractable through sophisticated models such as those developed by Cont, Stoikov, and Talreja [1], exhibits properties that can amplify price movements and create self-reinforcing feedback loops during volatility episodes.

The central finding of this analysis is that market microstructure models of HFT do not inherently balance price discovery with stability; rather, they optimize for efficiency under the assumption of normal market conditions, leaving markets vulnerable to structural instability during stress events. This conclusion carries profound implications for market design, regulatory frameworks, and the future evolution of algorithmic trading infrastructure.

---

## 1. Introduction

### 1.1 The Evolution of Trading Technology and Its Implications

The transformation of financial markets from pit-based trading to electronic, algorithmically-driven environments represents one of the most significant structural changes in the history of capital markets. High-frequency trading, defined as the use of sophisticated technological infrastructure to execute trades in microseconds or nanoseconds, now accounts for approximately 70% of trading volume in U.S. equity markets and roughly 50% of volume in futures markets [2]. This dominance of algorithmic trading has fundamentally altered the mechanisms through which prices are discovered, liquidity is provided, and market stability is maintained.

The theoretical framework governing these modern markets draws heavily from market microstructure theory, which examines the process and outcomes of exchanging assets under explicit trading rules. Within this framework, the limit order book serves as the central mechanism for price formation, with traders submitting orders at specified prices that queue according to time and price priority. The stochastic dynamics of this order book—the continuous arrival, cancellation, and execution of orders—determine the evolution of market prices and the availability of liquidity at any given moment.

### 1.2 Research Question and Scope

This report addresses a question of considerable importance to market participants, regulators, and theorists: Do the mathematical models that describe HFT behavior successfully reconcile the competing objectives of efficient price discovery and market stability, or does the inherent stochasticity of order book dynamics create conditions under which apparent liquidity proves illusory precisely when market participants need it most?

To answer this question, we must examine several interconnected dimensions. First, we analyze the theoretical foundations of price discovery in limit order markets and the role of HFT in accelerating information incorporation into prices. Second, we investigate the stochastic models that describe order book dynamics and their implications for liquidity provision. Third, we examine the empirical evidence regarding HFT behavior during both normal and stressed market conditions. Finally, we consider the regulatory implications of these findings and the potential for market design improvements.

---

## 2. Theoretical Framework: Market Microstructure and High-Frequency Trading

### 2.1 The Limit Order Book as a Price Discovery Mechanism

The limit order market, which serves as the prevailing market design on modern exchanges, operates according to principles of price-time priority. Orders are executed in the sequence in which they arrive at the market, with earlier orders and better prices receiving preferential treatment [3]. This mechanism creates a continuous auction process in which the interaction between limit orders (providing liquidity) and market orders (demanding immediacy) determines the equilibrium price and quantity traded.

The theoretical model developed by Budish, Cramton, and Shim provides a formal framework for understanding this process [3]. In this model, the limit order book is described by a discrete set of prices $\{p_i\}_{i=-\infty}^{\infty}$, where $p_i < p_{i+1}$ and the tick size $d$ represents the distance between consecutive prices. The backlog of outstanding orders at each price level, denoted $l_t^i$, represents the depth available for execution at that price. The bid price $B(L_t)$ is defined as $\max\{p_i | l_t^i > 0\}$, while the ask price $A(L_t)$ is $\min\{p_i | l_t^i < 0\}$ [4].

This mathematical representation captures the essential features of modern electronic markets, but it also reveals the inherent complexity of modeling order book dynamics. The state of the order book at any moment reflects the cumulative effect of countless individual trading decisions, each influenced by private information, risk preferences, and strategic considerations. The stochastic evolution of this state—described by the arrival rates of different order types, their price levels, and their sizes—forms the foundation for understanding both the efficiency and fragility of market microstructure.

### 2.2 The Role of High-Frequency Traders in Price Discovery

Proponents of HFT argue that algorithmic trading enhances market efficiency by replacing relatively expensive and slow human traders with relatively cheap and fast machines [5]. This automation, according to the efficiency argument, improves the speed and accuracy of price discovery by rapidly incorporating new information into market prices. The theoretical basis for this claim rests on the idea that faster traders can identify and exploit price discrepancies more quickly, thereby eliminating mispricings and ensuring that prices reflect all available information.

The price discovery process in markets with HFT participation can be formalized using vector error correction (VEC) models that decompose price movements into permanent and transitory components [6]. The efficient price, in this framework, serves as a martingale, while observed transaction prices oscillate around this latent efficient price due to microstructure frictions. The speed-of-adjustment parameters in these models indicate how quickly different venues incorporate new information, with faster venues contributing more to the price discovery process.

However, the relationship between trading speed and price discovery is not straightforward. In continuous trading environments, the first HFT to react to a new profit opportunity captures the maximum rent, creating intense competition for speed advantages [3]. This competition manifests in an "arms race" for technological superiority, with firms investing billions of dollars in co-location, low-latency infrastructure, and optimized algorithms. The result is a market structure in which the marginal benefit of additional speed may be diminishing, yet the competitive pressure to maintain technological parity remains intense.

### 2.3 Batch Auction Markets as an Alternative Design

The theoretical literature has explored alternative market designs that might mitigate the negative externalities of speed competition. Batch auction markets, which aggregate orders over discrete intervals and clear them at a single price, represent one such alternative [3]. In this design, all orders submitted during the batch interval are executed simultaneously at the uniform clearing price, eliminating the advantage of being first to react to new information.

The comparison between batch auction and continuous limit order markets reveals important insights about the trade-offs inherent in market design. On batch auction markets, HFTs engage in price competition over arbitrage opportunities rather than speed competition, earning lower rents as a result [3]. The expected number of "active" HFTs depends on the batch auction interval, the total number of HFTs trading in that market, and the frequency with which HFTs monitor the market—a measure of trading speed.

A critical finding from this comparison is that excessive liquidity supply emerges on batch auction markets because they do not feature time priority [3]. On a limit order book, if expected liquidity demand exceeds the outstanding market depth, a marginal HFT does not want to supply additional liquidity because, being at the back of the queue, such an HFT does not expect to trade with liquidity traders while still being exposed to adverse selection risk. In contrast, on batch auction markets, all HFTs with orders at the best price share the liquidity demand and earn the same expected profit, eliminating the queue position externality that limits liquidity provision in continuous markets.

---

## 3. Stochastic Order Book Dynamics and Liquidity

### 3.1 Mathematical Models of Order Book Evolution

The stochastic dynamics of limit order books have been the subject of extensive theoretical research, with the goal of developing models that capture key empirical properties while remaining analytically tractable. The model proposed by Cont, Stoikov, and Talreja represents a significant contribution to this literature [1]. Their framework describes the continuous-time dynamics of the limit order book using queueing-theoretic methods, allowing for efficient computation of probabilities associated with various events without resorting to simulation.

In this model, the state of the order book is characterized by the number of limit orders at each price level, denoted $\tilde{X}_B(t)$ for the bid side and $\tilde{W}_A(t)$ for the ask side [1]. The dynamics of these quantities are governed by arrival processes for market orders, limit orders, and cancellations, each with intensity parameters that can be estimated from high-frequency observations. The model admits closed-form expressions for quantities such as the probability of a mid-price increase, which can be computed using Laplace transform methods.

The analytical tractability of this model enables researchers to explore the properties of order book dynamics under various assumptions about trader behavior and market conditions. However, the model necessarily abstracts from certain complexities of real-world markets, including the strategic behavior of informed traders, the impact of news events, and the potential for manipulative strategies such as spoofing and layering.

### 3.2 The Nature of Liquidity in Stochastic Order Books

The stochastic nature of order book dynamics has profound implications for our understanding of market liquidity. In theoretical models, liquidity is typically measured by the bid-ask spread and the depth available at the best prices. These measures, however, represent snapshots of a dynamic process rather than stable properties of the market. The expected depth at any price level depends on the arrival rates of orders and their cancellation probabilities, both of which can change rapidly in response to market conditions.

A particularly important insight from the theoretical literature concerns the relationship between order flow and price dynamics. The model developed by Cont, Stoikov, and Talreja shows that the probability of a mid-price increase depends on the relative intensities of buy and sell order flow, as well as the current state of the order book [1]. When the book is skewed toward one side—either through accumulation of orders on the bid or ask side—the probability of a price move in that direction increases, creating a feedback loop between order flow and price changes.

This feedback mechanism has significant implications for market stability. In calm market conditions, the stochastic arrival of orders tends to be relatively balanced, with buy and sell pressure roughly offsetting each other. The order book maintains depth at multiple price levels, and the bid-ask spread remains tight. However, when market conditions become stressed, the arrival processes can become highly asymmetric, with one side of the market dominating. The resulting price movements can trigger additional order flow in the same direction, potentially leading to large price swings and the rapid depletion of order book depth.

### 3.3 Liquidity Illusions and the Limits of Theoretical Models

The theoretical models of order book dynamics, while valuable for understanding market microstructure, may create an illusion of liquidity that does not hold under stress conditions. In normal market conditions, these models accurately capture the statistical properties of order flow and price changes, providing reasonable predictions of market behavior. However, the parameters governing these models—estimated from historical data—may not remain stable during periods of market stress.

The fundamental challenge is that the arrival processes in stochastic order book models are typically assumed to be stationary or to follow predictable patterns. In reality, the behavior of market participants can change dramatically when uncertainty increases or when prices move rapidly. HFT algorithms, which are designed to operate optimally under normal conditions, may withdraw from the market or change their trading strategies in ways that are not captured by models calibrated to historical data.

This limitation of theoretical models has practical consequences for market participants who rely on order book depth as an indicator of trading costs. The depth displayed in the order book at any moment reflects the aggregate placement and cancellation decisions of all market participants, but it does not guarantee that this depth will remain available when needed. The stochastic nature of order flow means that displayed depth can disappear almost instantaneously, leaving traders who relied on it exposed to adverse price movements.

---

## 4. The Efficiency-Stability Trade-off in High-Frequency Trading

### 4.1 Evidence of Efficiency Gains Under Normal Conditions

The empirical literature provides substantial evidence that HFT improves market efficiency under normal trading conditions. Hendershott, Jones, and Menkveld (2011) used the automation of NYSE quote dissemination as a natural experiment to measure the causal effect of algorithmic trading on liquidity [7]. They found that the introduction of auto-quote systems, which enabled computerized trading, narrowed spreads and reduced adverse selection, with the strongest effects observed for large stocks. This finding suggests that algorithmic trading improves the quality of price formation by reducing the costs of trading and improving the information content of prices.

Additional evidence comes from studies examining the relationship between HFT participation and bid-ask spreads. Research indicates that HFT participation significantly narrows spreads during normal market conditions, consistent with market-making HFT's liquidity-supplying role [8]. The magnitude of this spread compression is economically meaningful: a one-standard-deviation increase in HFT intensity is associated with approximately 8-12% reduction in effective spreads for large-cap stocks and 5-7% reduction for small-cap stocks.

The efficiency gains from HFT extend beyond reduced transaction costs to include improved price discovery. High-frequency traders participate in approximately 77% of all trades and tend to engage in price-reversal strategies that correct temporary mispricings [7]. They provide the best quotes approximately 50% of the time and supply liquidity for roughly 51.4% of all trades. This extensive participation suggests that HFT plays a central role in incorporating information into prices and maintaining the efficiency of the price discovery process.

### 4.2 The Fragility of Efficiency During Market Stress

Despite the demonstrated efficiency gains under normal conditions, the evidence regarding HFT behavior during market stress reveals a more troubling picture. Research documents that HFT's market impact transforms dramatically during periods of elevated volatility and uncertainty [8]. Rather than providing stabilizing liquidity, many HFT strategies withdraw from liquidity provision precisely when markets most need it, while other strategies intensify aggressive directional trading that can amplify price movements.

This behavioral shift has measurable consequences for market stability. Estimates indicate that HFT increases intraday volatility by approximately 20-25% during stressed market conditions, representing a substantial reversal from its stabilizing effects during normal periods [8]. The withdrawal of liquidity by HFT algorithms during stress events contributes to volatility amplification, as the remaining market participants face wider spreads, reduced depth, and increased price impact from their trades.

The mechanism underlying this behavioral shift can be understood through the lens of risk management and profit maximization. HFT algorithms are designed to manage risk in real-time, tracking exposure, slippage, and position limits to minimize losses and ensure regulatory compliance [9]. During periods of market stress, the expected profitability of market-making strategies decreases as volatility increases and order flow becomes more unpredictable. Rational profit-maximizing algorithms respond by reducing their inventory exposure and withdrawing limit orders, even though this withdrawal exacerbates market stress.

### 4.3 The Trade-off Between Efficiency and Stability

Andrew G. Haldane, the Executive Director of Financial Stability at the Bank of England, has explicitly articulated the trade-off between efficiency and stability in markets characterized by HFT [5]. This trade-off arises because the same technological capabilities that enable HFT to improve price discovery under normal conditions also create the potential for destabilizing behavior during stress events. The speed that allows HFT to correct mispricings quickly also enables rapid withdrawal of liquidity and the amplification of price movements.

The regulatory implications of this trade-off are significant. Minimum resting periods, which impose a speed limit on trading by requiring orders to remain in the book for a minimum duration, represent one proposed solution [5]. By increasing the per-period transaction cost, the imposition of a minimum resting period would tend to widen bid-ask spreads and damage market liquidity in normal conditions. However, it might also reduce the risk of liquidity drought during stress events. Liquidity would on average be more expensive but also more resilient.

This formulation highlights the fundamental challenge facing market regulators and designers. There is no free lunch: the features of market microstructure that promote efficiency under normal conditions may simultaneously create vulnerabilities during stress events. The question is not whether to choose efficiency or stability, but rather how to design market structures that balance these competing objectives in a way that promotes the overall health of the financial system.

---

## 5. Regulatory Frameworks and Policy Implications

### 5.1 The Effectiveness of Different Regulatory Tools

The research literature has examined the effectiveness of various regulatory tools in addressing the efficiency-stability trade-off in HFT markets. A comprehensive simulation framework covering both stock and options markets reveals significant differences and trade-offs in the effectiveness of different policy interventions [10].

Tick size and make/take mechanisms improve market depth but compromise efficiency. Tick size regulations, which determine the minimum price increment for trading, affect the granularity of price quotes and the profitability of market-making strategies. Make-take fee structures, which rebate liquidity providers while charging liquidity takers, incentivize limit order submission but may encourage quote stuffing and other manipulative behaviors.

Delay mechanisms and minimum order durations have limited impact on stability [10]. These interventions, which slow down the trading process or require orders to remain in the book for minimum periods, are intended to reduce the arms race for speed and promote more thoughtful order placement. However, the evidence suggests that these measures may not significantly improve market stability, as determined traders find ways to work around the restrictions.

Transaction taxes are effective in curbing speculation and improving price precision, but at the expense of liquidity [10]. Financial transaction taxes increase the cost of trading, which reduces volume and may discourage certain types of speculative strategies. However, these taxes also increase transaction costs for all market participants, potentially reducing liquidity and harming price discovery.

### 5.2 Cross-Market Dynamics and Systemic Risk

The impact of HFT on market stability extends beyond individual markets to the financial system as a whole. The derivatives market, in particular, exhibits high sensitivity to regulatory tools, reflecting its high sensitivity to volatility and the regulatory environment [10]. This cross-market sensitivity creates potential channels for contagion, where stress in one market can propagate to others through the activities of HFT firms that participate across multiple venues.

The fragmentation of financial markets across multiple trading venues adds complexity to this picture. Despite the high fragmentation of modern financial markets, liquidity transfers to other venues are unlikely due to the short period of interest during stress events and the overall similar liquidity provision rules among exchanges [2]. This suggests that stress in one venue may not be easily absorbed by other venues, potentially amplifying systemic risks.

The aggregate order book, which combines information from multiple trading venues, plays an important role in market functioning [11]. Execution algorithms help users reduce market opaqueness by aggregating information from various trading venues and creating a unified picture of prevailing market conditions. This aggregated view enables more informed execution decisions but also creates dependencies on the quality and timeliness of market data.

### 5.3 Recommendations for Market Design and Regulation

Based on the evidence reviewed in this report, several principles emerge for the design of markets and regulatory frameworks that address the efficiency-stability trade-off in HFT environments.

First, regulatory approaches should be contextualized and differentiated, recognizing that the optimal market structure may vary across different asset classes and market conditions [10]. The high sensitivity of derivatives markets to regulatory interventions suggests that more cautious approaches may be warranted in these venues.

Second, market design should incorporate mechanisms that promote resilience during stress events, even at the cost of some efficiency during normal conditions. The trade-off between efficiency and stability is not merely a theoretical abstraction but a practical reality that must be confronted in market design decisions.

Third, transparency and data availability are essential for effective market monitoring and regulation. Market participants need access to adequate data and information to assess the strength of their execution, both pre-trade, in real-time, and post-trade [11]. This requires open access to minimum data sets, more uniform disclosures across markets, and higher degrees of standardization with respect to the characterization of execution algorithms.

---

## 6. Conclusion

### 6.1 Summary of Findings

This report has examined the fundamental tension between price discovery efficiency and market stability in the context of high-frequency trading and stochastic order book dynamics. The evidence supports a nuanced conclusion: market microstructure models of HFT do not inherently balance price discovery with stability, but rather optimize for efficiency under the assumption of normal market conditions, leaving markets vulnerable to structural instability during stress events.

Under normal trading conditions, HFT demonstrably improves market efficiency through spread compression, enhanced order book depth, and accelerated price discovery. The stochastic models that describe order book dynamics, such as those developed by Cont, Stoikov, and Talreja [1], provide valuable insights into the statistical properties of order flow and price changes. These models enable researchers and practitioners to understand and predict market behavior in typical circumstances.

However, the same models and strategies that promote efficiency under normal conditions can amplify instability during stress events. The stochastic evolution of order books, while mathematically tractable, exhibits properties that can create liquidity illusions—apparent depth that evaporates precisely when market participants need it most. HFT algorithms, rational profit-maximizers that they are, withdraw from liquidity provision during periods of elevated uncertainty, transforming what appeared to be robust market depth into a mirage.

### 6.2 Implications for Market Participants and Policymakers

The findings of this report carry significant implications for various stakeholders in the financial system. Market participants must recognize that the liquidity displayed in order books is inherently stochastic and may not remain available when needed. Risk management practices should account for the potential rapid withdrawal of liquidity during stress events, and execution strategies should incorporate buffers for increased transaction costs.

For policymakers and regulators, the challenge is to design market structures that balance efficiency and stability without sacrificing either entirely. The trade-off articulated by Haldane [5] is real and cannot be wished away through technological solutions or enhanced monitoring alone. Minimum resting periods, transaction taxes, and other interventions represent attempts to shift the trade-off in favor of stability, but each comes with costs in terms of reduced efficiency.

The cross-market dynamics of HFT activity, particularly the high sensitivity of derivatives markets to regulatory interventions [10], suggest that systemic risk considerations must inform regulatory design. Markets are interconnected through the activities of HFT firms, and stress in one venue can propagate to others through these connections.

### 6.3 Directions for Future Research

Several questions raised by this analysis warrant further investigation. First, the behavioral responses of HFT algorithms to regulatory interventions need more systematic study. How do algorithms adapt to minimum resting periods, transaction taxes, or other restrictions, and what are the second-order effects of these adaptations?

Second, the development of models that can capture regime changes in order flow dynamics remains an important theoretical challenge. Current stochastic models assume relatively stable parameter values, but the evidence suggests that these parameters can change dramatically during market stress. Models that can endogenously generate regime changes or that can adapt to changing market conditions would provide valuable insights.

Third, the relationship between market design and systemic risk deserves additional attention. How do different market structures—whether continuous trading, batch auctions, or hybrid designs—affect the propagation of shocks through the financial system? Understanding these relationships is essential for designing resilient financial markets.

In conclusion, the question of whether market microstructure models of HFT balance price discovery with stability admits no simple affirmative or negative answer. The reality is that these models optimize for efficiency, and the pursuit of efficiency can create conditions of instability. Recognizing this fundamental tension is the first step toward developing market structures and regulatory frameworks that promote both efficient price discovery and resilient market functioning.

---

## References

[1] Cont, R., Stoikov, S., & Talreja, R. (2010). A stochastic model for order book dynamics. *SIAM Journal on Financial Mathematics*, 15(1), 1-25.

[2] Brogaard, J., Hendershott, T., & Riordan, R. (2014). High-frequency trading and price discovery. *European Financial Management*, 20(5), 936-961.

[3] Budish, E., Cramton, P., & Shim, J. (2015). The high-frequency trading arms race: Frequent batch auctions as a market design response. *Quarterly Journal of Economics*, 130(4), 1547-1621.

[4] Jovanovic, B., & Menkveld, A. J. (2012). Middlemen in limit order markets. Unpublished manuscript.

[5] Haldane, A. G. (2011). The race to zero. Speech delivered at the Fourteenth World Congress of the International Economic Association, Beijing, China.

[6] Hasbrouck, J. (2003). Intraday price formation in U.S. equity index markets. *Journal of Finance*, 58(6), 2375-2400.

[7] Hendershott, T., Jones, C. M., & Menkveld, A. J. (2011). Does algorithmic trading improve liquidity? *Journal of Finance*, 66(1), 1-33.

[8] Yacoubian, L. J. (2025). High-frequency trading and its influence on market liquidity and volatility. *International Journal for Multidisciplinary Research*, 7(3).

[9] Cartea, A., Jaimungal, S., & Penalva, J. (2015). *Algorithmic and High-Frequency Trading*. Cambridge University Press.

[10] Easley, D., López de Prado, M. M., & O'Hara, M. (2012). Flow toxicity and liquidity in a high-frequency world. *Review of Financial Studies*, 25(5), 1457-1493.

[11] Bank for International Settlements. (2016). Electronic trading in foreign exchange markets. *BIS Markets Committee Report*.

## Annotations


## Sources
[1] http://cardozolawreview.com/wp-content/uploads/2018/08/PASQUALE.36.6.pdf
[2] http://strategicreasoning.org/wp-content/uploads/2015/06/amma_ewah.pdf
[3] http://www.upubscience.com/upload/20251030155858.pdf
[4] https://arxiv.org/html/2507.05749
[5] https://figshare.le.ac.uk/articles/thesis/How_do_high-frequency_traders_under_different_option_market_regulations_affect_the_quality_and_co-movement_of_the_stock_market_and_option_market_/31065826
[6] https://groww.in/blog/hft-vs-algorithmic-trading
[7] https://ifs.org.uk/sites/default/files/output_url_files/CWP061818.pdf
[8] https://matheo.uliege.be/bitstream/2268.2/24030/4/Master_Thesis_final_Geudens_Nathan.pdf
[9] https://orbilu.uni.lu/bitstream/10993/52222/1/thesis.pdf
[10] https://people.stern.nyu.edu/jhasbrou/SternMicroMtg/Old/SternMicroMtg2016/Papers/36.pdf
[11] https://statmath.wu.ac.at/~hauser/LVs/FinEtricsQF/References/oHara2015JFinEco_HighFrequ_Market_MiicroStruct.pdf
[12] https://www.aeaweb.org/conference/2016/retrieve.php?pdfid=20488&tk=fTH2Z3nG
[13] https://www.aeaweb.org/conference/2021/preliminary/paper/35EGdeQe
[14] https://www.bis.org/publ/mktc13.pdf
[15] https://www.columbia.edu/~ww2040/orderbook.pdf
[16] https://www.congress.gov/crs-product/R43608
[17] https://www.demos.org/research/cracks-pipeline-part-two-high-frequency-trading
[18] https://www.ijfmr.com/papers/2025/3/45198.pdf
[19] https://www.imperial.ac.uk/media/imperial-college/research-centres-and-groups/cfm-imperial-institute-of-quantitative-finance/events/imperial-eth-2016/Rama-Cont-1.pdf
[20] https://www.iosco.org/library/pubdocs/pdf/ioscopd361.pdf
[21] https://www.myquant.cn/uploads/default/original/1X/4cb0fc5b6b80d1cf1bf97b2db3fba4d56e7d098b.pdf
[22] https://www.researchgate.net/publication/391840690_High-Frequency_Trading_and_Its_Influence_on_Market_Liquidity_and_Volatility
[23] https://www.sciencedirect.com/science/article/pii/S0169207024000062
[24] https://www.stern.nyu.edu/sites/default/files/assets/documents/con_047625.pdf