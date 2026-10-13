# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 83ecad4c | **Time:** 933.96s | **Cost:** $1.96470
--------------------------------------------------------------------------------

# Feasibility of Balancing Execution Speed and Price Discovery in Modern Matching Engines: An Analysis of Latency Arbitrage and Market Manipulation

### Key Points
*   **Structural Vulnerability:** Research indicates that the continuous limit order book (CLOB), the dominant market design globally, inherently creates "latency arbitrage" opportunities. This structural flaw allows high-frequency traders (HFTs) to exploit symmetric public information, generating risk-free profits estimated at approximately $5 billion annually in global equity markets alone.
*   **Feasibility of Balance:** Balancing execution speed and price discovery is feasible but requires departing from pure continuous trading. Innovations such as Frequent Batch Auctions (FBA) and asymmetric speed bumps (e.g., IEX’s Crumbling Quote Indicator) have demonstrated the ability to protect liquidity providers and enhance price discovery without sacrificing the benefits of electronic trading.
*   **Manipulation vs. Arbitrage:** While latency arbitrage is often characterized as a "tax" rather than illegal manipulation, the high-speed environment necessitates strict regulatory oversight. Speed facilitates specific manipulative tactics like spoofing and quote stuffing, but these are distinct from the structural arbitrage built into CLOBs.
*   **Regulatory Divergence:** Global regulators have adopted varied approaches. The U.S. SEC has accommodated deterministic delays (speed bumps), the EU (MiFID II) focuses on order-to-trade ratios and transparency, and Asian regulators (Japan, Australia) emphasize system stability and registration of high-speed traders.

### Executive Summary
The evolution of financial markets from physical trading floors to electronic matching engines has delivered profound benefits, including reduced transaction costs and increased liquidity. However, this transition has introduced a fundamental tension between execution speed and the quality of price discovery. The prevailing market design—the Continuous Limit Order Book (CLOB)—processes orders serially in continuous time. Academic and empirical research suggests that this design violates the Efficient Market Hypothesis by allowing the fastest traders to snipe stale quotes based on public information, a practice known as latency arbitrage.

This report examines whether matching engines can reconcile these competing forces. It analyzes the mechanics of latency arbitrage, the efficacy of alternative market designs like Frequent Batch Auctions and asymmetric speed bumps, and the intersection of high-speed trading with market manipulation. The evidence suggests that while high-frequency trading (HFT) generally improves liquidity, the unbridled race for nanosecond-level speed creates social deadweight loss and vulnerabilities to manipulation. Feasible solutions exist but require a paradigm shift in how exchanges conceptualize time and priority.

---

## 1. The Mechanics of Modern Matching Engines and the Continuous Limit Order Book (CLOB)

### 1.1 The Dominance of Continuous Trading
Nearly all modern financial exchanges utilize a continuous trading model, specifically the Continuous Limit Order Book (CLOB). In this system, incoming orders are matched with resting orders immediately upon arrival. The matching engine processes messages serially, typically following a Price-Time Priority (FIFO) algorithm [cite: 1, 2]. This design is predicated on the belief that continuous matching maximizes liquidity and minimizes bid-ask spreads by allowing immediate execution [cite: 1].

The CLOB model treats time as a continuous variable. Traders submit limit orders (offers to buy or sell at a specific price) or market orders (requests to trade immediately at the best available price). The matching engine maintains an order book, ranking bids and offers. When a market order arrives, it consumes the liquidity at the top of the book. This mechanism has been credited with narrowing spreads and lowering the cost of capital for issuers [cite: 1].

### 1.2 The Structural Flaw: Serial Processing in Continuous Time
Despite its prevalence, the CLOB model contains a critical structural vulnerability identified by researchers Budish, Cramton, and Shim. The flaw arises from the combination of continuous-time trading and serial processing. In a CLOB, orders are processed one at a time in the order they are received. However, information in financial markets often arrives in discrete bundles or is observed simultaneously by multiple participants (symmetric information) [cite: 3].

When a piece of public information changes the fundamental value of an asset (e.g., a price movement in a correlated futures contract like the E-mini S&P 500), a race ensues. Liquidity providers (market makers) attempt to cancel their stale quotes, while aggressive HFTs attempt to "snipe" those quotes before they can be updated. Because the matching engine processes requests serially, the outcome is determined solely by who arrives at the exchange's matching engine first [cite: 3].

This creates a binary outcome:
1.  **The Liquidity Provider Wins:** The quote is updated, and price discovery occurs without a trade.
2.  **The Sniper Wins:** The stale quote is executed against, resulting in a risk-free profit for the sniper and a loss for the liquidity provider [cite: 3].

### 1.3 Latency Arbitrage Defined
Latency arbitrage differs from traditional arbitrage. Traditional arbitrage exploits price discrepancies between markets that arise from inefficiencies or information asymmetry. Latency arbitrage, by contrast, exploits the mechanical processing delay of the matching engine and the speed of light. It relies on "stale quotes"—prices that have not yet reflected information that is already publicly available [cite: 4, 5, 6].

This form of arbitrage is described as "riskless" because the sniper only executes the trade if they observe the price change elsewhere first. The profit is generated not by fundamental analysis or risk-taking, but by the speed differential between the sniper and the liquidity provider [cite: 4, 7].

#### 1.3.1 The "Tax" on Liquidity
The costs of latency arbitrage are borne by liquidity providers. To compensate for the losses incurred from being sniped, market makers must widen their bid-ask spreads. This widened spread acts as a "tax" on all investors, increasing the cost of trading for end-users [cite: 8, 9, 10].

Research by Aquilina, Budish, and O'Neill quantifies this cost. They estimate that latency arbitrage races account for approximately 20% of daily trading volume in major equity indices (e.g., FTSE 100). The global cost of this "latency arbitrage tax" is estimated at approximately $5 billion annually in equity markets alone [cite: 8, 10, 11, 12].

### 1.4 Technological Infrastructure and the Arms Race
The existence of latency arbitrage incentivizes an "arms race" for speed. Trading firms invest heavily in low-latency infrastructure, including:
*   **Co-location:** Placing servers in the same data center as the exchange's matching engine [cite: 13, 14].
*   **Microwave Networks:** Using microwave towers rather than fiber optic cables to shave milliseconds off transmission times between trading hubs (e.g., Chicago to New Jersey) [cite: 6, 15].
*   **FPGA (Field-Programmable Gate Arrays):** Hardware-accelerated trading logic that processes market data and sends orders in nanoseconds, bypassing standard software stacks [cite: 6, 16].

Critics argue that this investment is socially wasteful. While it ensures prices align across venues microseconds faster, it does not necessarily improve long-term price discovery or capital allocation [cite: 17, 18]. The marginal utility of reducing latency from 10 microseconds to 9 microseconds is negligible for a fundamental investor but critical for a latency arbitrageur [cite: 19].

---

## 2. High-Frequency Trading: Price Discovery vs. Market Manipulation

### 2.1 The Case for HFT and Price Discovery
Proponents of HFT and continuous trading argue that high-speed intermediaries perform vital market functions. By continuously updating quotes and competing for order flow, HFTs:
*   **Enhance Price Efficiency:** HFTs rapidly incorporate new information into prices, ensuring that asset prices reflect available information almost instantaneously [cite: 20, 21, 22].
*   **Provide Liquidity:** HFTs act as informal market makers, providing depth to the order book and facilitating trades for institutional investors [cite: 1, 23].
*   **Reduce Spreads:** Intense competition among HFTs compresses bid-ask spreads, lowering transaction costs for retail and institutional investors [cite: 1, 24].

Research analyzing the Taiwan Stock Exchange's transition from frequent batch auctions to continuous trading found that the shift led to deeper liquidity, lower spreads, and higher trading volumes [cite: 1]. Similarly, studies on the Tokyo Stock Exchange (TSE) following the introduction of the high-speed "Arrowhead" system found that HFT contributed to narrower spreads and reduced short-term volatility [cite: 23, 24].

### 2.2 The Dark Side: Manipulation and "Toxic" Flow
While HFT contributes to efficiency, the speed and automation of modern markets also create room for manipulation. The distinction between aggressive arbitrage and manipulation is sometimes blurred, but specific practices are clearly identified as harmful.

#### 2.2.1 Spoofing and Layering
Spoofing involves placing non-bona fide orders on one side of the book to create a false appearance of demand or supply, inducing other traders to execute against orders on the opposite side. Once the execution occurs, the spoof orders are cancelled [cite: 25, 26, 27].
*   **Speed Facilitation:** HFT speeds allow spoofers to place and cancel thousands of orders in seconds, making detection difficult and allowing them to react before other participants can execute against the fake orders [cite: 25, 26].
*   **Impact on Discovery:** Spoofing harms price discovery by injecting false information into the order book. It increases volatility and trading costs for legitimate participants [cite: 25].

#### 2.2.2 Quote Stuffing
Quote stuffing involves flooding the exchange with a massive number of orders and cancellations to clog the matching engine or data feeds. This creates latency for other participants, allowing the stuffer to exploit the resulting information asymmetry [cite: 28, 29].

#### 2.2.3 The "Inevitability" of Manipulation
The query asks if latency arbitrage *inevitably* creates room for manipulation. Research suggests that while latency arbitrage itself is a structural feature rather than manipulation, the *environment* required for latency arbitrage (ultra-low latency, high message rates) lowers the cost and risk of manipulative strategies like spoofing [cite: 25, 30]. However, regulatory frameworks distinguish between taking advantage of structural speed (arbitrage) and inducing false signals (manipulation) [cite: 31, 32].

---

## 3. Market Design Solutions: Feasibility of Balancing Speed and Discovery

Given the costs of latency arbitrage and the risks of manipulation, several alternative market designs have been proposed and implemented to better balance execution speed with price discovery.

### 3.1 Frequent Batch Auctions (FBA)
Proposed by Budish, Cramton, and Shim, Frequent Batch Auctions (FBA) replace continuous trading with discrete-time auctions held at frequent intervals (e.g., every 100 milliseconds or 1 second) [cite: 1, 3, 33].

*   **Mechanism:** Orders accumulate during the batch interval. At the end of the interval, the matching engine executes all matching orders at a uniform price.
*   **Eliminating Latency Arbitrage:** By processing orders in batches, FBA eliminates the advantage of being a microsecond faster. If a liquidity provider and a sniper both react to news within the same batch interval, their orders are treated equally. This transforms competition from speed (who is fastest) to price (who offers the best deal) [cite: 3, 34, 35].
*   **Impact on Price Discovery:** Theoretical models suggest FBA enhances liquidity by removing the risk of being sniped, allowing market makers to quote tighter spreads [cite: 33, 34]. However, critics (e.g., Citadel) argue that batching reduces liquidity provision and slows down price discovery by delaying execution [cite: 1].

### 3.2 Asymmetric Speed Bumps (The IEX Model)
The Investors Exchange (IEX) introduced a deterministic delay (350 microseconds) combined with a "Crumbling Quote Indicator" (CQI) to neutralize latency arbitrage without abandoning continuous trading [cite: 36, 37, 38].

*   **Mechanism:**
    *   **The Speed Bump:** All incoming orders pass through a 38-mile coil of fiber optic cable, creating a 350-microsecond delay [cite: 37].
    *   **The Signal (CQI):** IEX's system predicts when the National Best Bid/Offer (NBBO) is about to change (crumble) due to pressure on other exchanges.
    *   **Asymmetry:** When the CQI predicts a price change, IEX prevents "pegged" orders (orders resting at the midpoint or best bid/offer) from exercising discretion to trade. This effectively allows the resting order to "get out of the way" of a sniper [cite: 36, 37, 39].
*   **Impact:** Research indicates that asymmetric speed bumps reduce investment in low-latency technology by approximately 20% and improve market quality for liquidity providers [cite: 40, 41, 42, 43]. The SEC approved this model, acknowledging that de minimis delays do not violate the requirement for immediate execution under Regulation NMS [cite: 44, 45].

### 3.3 Randomized Delays
Some venues, such as TSX Alpha in Canada, have experimented with randomized delays (e.g., 1-3 milliseconds) to introduce uncertainty for latency arbitrageurs [cite: 15].
*   **Mechanism:** By randomizing the processing time, the exchange makes it impossible for a sniper to guarantee they will arrive before a liquidity provider updates their quote.
*   **Efficacy:** Studies suggest randomized delays can improve liquidity but may harm volatility compared to continuous trading in certain conditions [cite: 33].

---

## 4. Regulatory Responses and Global Perspectives

Regulators worldwide have grappled with the implications of HFT and matching engine design, resulting in divergent approaches.

### 4.1 United States (SEC)
The U.S. regulatory framework, primarily Regulation NMS, emphasizes fair access and protected quotes.
*   **IEX Approval:** The SEC's approval of IEX in 2016 marked a pivotal shift, interpreting "immediate" execution to allow for intentional delays of less than 1 millisecond [cite: 44, 45]. This validated the asymmetric speed bump as a legitimate tool to combat latency arbitrage.
*   **Focus on Transparency:** The SEC requires detailed disclosure of order routing and execution quality to help investors assess the impact of HFT [cite: 29].

### 4.2 European Union (MiFID II)
MiFID II represents the most comprehensive regulatory attempt to address HFT risks.
*   **Order-to-Trade Ratios (OTR):** Trading venues must impose limits on the ratio of unexecuted orders to transactions. This is designed to curb quote stuffing and inefficient algorithmic strategies [cite: 46, 47, 48, 49].
*   **Tick Sizes:** Harmonized tick sizes prevent a "race to the bottom" where HFTs jump ahead of orders by negligible amounts [cite: 50].
*   **Market Making Obligations:** Algorithmic traders pursuing market-making strategies must sign binding agreements to provide liquidity continuously, even during stressed market conditions [cite: 46].

### 4.3 Asia-Pacific (Japan and Australia)
*   **Japan (FSA/JPX):** Japan introduced a registration system for "High-Speed Traders" in 2018. The focus is on risk management, system stability, and understanding the actual situation of HFT rather than banning specific strategies [cite: 51, 52].
*   **Australia (ASIC):** ASIC has focused on "kill switches" to disable rogue algorithms and minimum resting times to prevent fleeting liquidity. Their reviews concluded that HFT has not systematically degraded market quality but requires monitoring [cite: 53, 54, 55].

---

## 5. Detailed Analysis of Latency Arbitrage "Tax" and Market Efficiency

### 5.1 Quantifying the Cost
The characterization of latency arbitrage as a "tax" is central to the debate on feasibility.
*   **Magnitude:** The $5 billion annual figure derived by Aquilina, Budish, and O'Neill suggests that the cost is systemic and significant [cite: 8, 11, 12].
*   **Distribution:** This cost is effectively a transfer from regular investors (who pay wider spreads) to HFT firms (who capture the arbitrage profits) and exchanges (who sell speed technology) [cite: 7, 56].
*   **Deadweight Loss:** The resources spent on the arms race (e.g., microwave towers, FPGA development) represent a social deadweight loss, as they do not increase the size of the economic pie but merely redistribute it [cite: 17, 56].

### 5.2 Counter-Arguments and Market Quality
Critics of the "tax" narrative, such as Citadel Securities and some academic researchers, argue that the focus on latency arbitrage ignores the broader benefits of HFT.
*   **Liquidity Resilience:** Continuous markets with HFT participation have shown resilience during stress events, provided risk controls are in place [cite: 1, 20].
*   **Cost of Capital:** By reducing spreads, HFTs lower the cost of equity for corporations. The "tax" of arbitrage may be outweighed by the reduction in transaction costs achieved through automation [cite: 1, 33].

---

## 6. Conclusion: Feasibility and Future Directions

### 6.1 Is Balance Feasible?
The research confirms that it is **feasible** for trading platform matching engines to balance execution speed and price discovery. However, achieving this balance requires acknowledging the limitations of the pure CLOB model.
*   **Hybrid Models:** The success of IEX and the theoretical robustness of Frequent Batch Auctions demonstrate that market designs can be engineered to neutralize the negative externalities of speed while preserving the benefits of electronic trading.
*   **Technology vs. Structure:** Purely technological solutions (making the engine faster) yield diminishing returns and exacerbate the arms race. Structural solutions (speed bumps, batching) address the root cause of latency arbitrage [cite: 34, 41].

### 6.2 Does HFT Inevitably Create Manipulation?
HFT does not *inevitably* create manipulation, but it creates an environment where manipulation is cheaper and harder to detect without sophisticated surveillance.
*   **Distinction is Key:** Latency arbitrage is a structural feature of continuous markets, whereas spoofing is a conduct violation.
*   **Mitigation:** Regulatory tools like OTR limits, kill switches, and asymmetric speed bumps effectively mitigate the risks of manipulation without necessitating a ban on HFT [cite: 30, 47, 54].

### 6.3 Final Verdict
The "inevitability" of market manipulation and latency arbitrage is a function of market design, not an intrinsic law of finance. By moving away from a rigid adherence to continuous-time serial processing and adopting mechanisms that recognize the discrete nature of information arrival, trading platforms can effectively balance the demand for speed with the imperative of fair and accurate price discovery.

---

## 7. Comprehensive Data Tables and Methodologies

### Table 1: Comparison of Market Designs

| Feature | Continuous Limit Order Book (CLOB) | Frequent Batch Auction (FBA) | Asymmetric Speed Bump (IEX) |
| :--- | :--- | :--- | :--- |
| **Time Treatment** | Continuous | Discrete (e.g., 100ms batches) | Continuous with delay |
| **Matching Logic** | Serial (Price-Time Priority) | Batch (Uniform Price) | Serial (Price-Time Priority) |
| **Latency Arb Risk** | High (Sniping risk-free) | Eliminated (Speed advantage neutralized) | Mitigated (Protects passive quotes) |
| **Price Discovery** | Immediate but noisy | Aggregated, potentially more accurate | Protected, focuses on stability |
| **Arms Race** | Encourages infinite speed investment | Discourages speed investment | Reduces speed investment (~20%) |
| **Regulatory Status** | Standard globally | Theoretical/Experimental | Approved (SEC Reg NMS) |

### Table 2: Global Regulatory Approaches to HFT

| Jurisdiction | Key Regulatory Body | Primary Focus | Specific Measures |
| :--- | :--- | :--- | :--- |
| **United States** | SEC / CFTC | Fairness & Transparency | Reg NMS (Protected Quotes), Consolidated Audit Trail (CAT), Approval of Speed Bumps |
| **European Union** | ESMA | System Stability & Abuse Prevention | MiFID II: Order-to-Trade Ratios, Tick Size Regime, Market Making Agreements |
| **Australia** | ASIC | Integrity & Control | Kill Switches, Minimum Resting Times, Dark Pool Rules |
| **Japan** | FSA / JPX | Visibility & Risk Management | Registration of High-Speed Traders, System Capacity Management |
| **Canada** | IIROC | Market Quality | Guidance on Dark Liquidity, Randomized Delays (TSX Alpha) |

### Table 3: Estimated Costs of Latency Arbitrage

| Metric | Estimate | Source |
| :--- | :--- | :--- |
| **Global Annual Cost** | ~$5 Billion (Equity Markets) | Aquilina, Budish, O'Neill [cite: 8, 11] |
| **Cost per Trade** | ~0.5 basis points | Aquilina, Budish, O'Neill [cite: 12] |
| **Volume Impact** | ~20% of trading volume involved in races | Aquilina, Budish, O'Neill [cite: 12] |
| **Reduction in Speed Investment** | ~20% (with asymmetric speed bumps) | Khapko & Zoican [cite: 41] |

---

## 8. Detailed Discussion of Specific Research Findings

### 8.1 The Budish-Cramton-Shim Model
The seminal work by Budish et al. provides the theoretical foundation for challenging the CLOB. Their model demonstrates that the CLOB transforms symmetric information into arbitrage opportunities. Even if all participants observe the same news feed (e.g., a Fed announcement), the serial processing of the matching engine ensures that only the first message processed captures the value. This creates a "Prisoner's Dilemma" where market makers must invest in speed merely to avoid being exploited, rather than to improve the product [cite: 3, 34].

### 8.2 The Taiwan Stock Exchange (TWSE) Natural Experiment
The TWSE provides a rare counter-example. Until 2020, it operated as a frequent batch auction market. Its transition to continuous trading allowed for a direct comparison. Citadel Securities' analysis of this transition argues that continuous trading improved market quality metrics across the board. This suggests that while FBA solves latency arbitrage theoretically, continuous trading may offer superior liquidity provision in practice due to the preferences of market participants for immediacy [cite: 1].

### 8.3 The Efficacy of "Crumbling Quote" Signals
IEX's innovation lies in its use of predictive analytics within the matching engine. By monitoring the NBBO across all exchanges, IEX identifies when a price is likely to change. The "Crumbling Quote Indicator" (CQI) is a binary signal: when "on," it prevents pegged orders from trading aggressively. This effectively shields passive orders from being picked off during the microseconds of price transition. This mechanism proves that matching engines can be "smart" rather than just "fast," prioritizing price quality over raw execution speed [cite: 37, 38, 39].

### 8.4 Spoofing and Order-to-Trade Ratios
Research into spoofing highlights the vulnerability of automated markets. High OTRs are often a signature of manipulative strategies. MiFID II's imposition of OTR limits and potential penalties forces HFT firms to be more selective in their quoting, theoretically reducing noise and the potential for manipulation. However, critics argue that strict OTR limits can dampen legitimate market making during volatile periods when rapid quote updates are necessary to manage risk [cite: 30, 46, 47].

---

## 9. Technological Underpinnings

### 9.1 Determinism and Fairness
A critical challenge in matching engine design is determinism. In a distributed system, ensuring that all participants perceive the "same" market at the same time is physically impossible due to relativity and network latency.
*   **Centralized vs. Decentralized:** Centralized matching engines (standard) offer speed but a single point of failure and a single point of latency arbitrage. Decentralized designs (e.g., blockchain-based or peer-to-peer) eliminate the central bottleneck but introduce consensus latency, making them currently unsuitable for HFT [cite: 57].
*   **Hardware Acceleration:** The move to FPGA matching engines allows for deterministic processing times in the nanosecond range, reducing the "jitter" that creates accidental arbitrage opportunities [cite: 16].

### 9.2 The Role of Data Feeds
Latency arbitrage relies on the speed differential between direct data feeds (proprietary feeds from exchanges) and the consolidated tape (SIP). HFTs construct the NBBO faster than the SIP can calculate it. Solutions like IEX's speed bump work by effectively slowing down the HFTs to the speed of the SIP, leveling the playing field for investors who rely on the consolidated feed [cite: 6, 36].

---

## 10. Final Synthesis

The feasibility of balancing execution speed and price discovery is not a binary question of "possible" or "impossible," but a design choice. The current dominant design (CLOB) prioritizes immediacy and continuous execution, accepting latency arbitrage as a cost of doing business. Alternative designs (FBA, Speed Bumps) prioritize price stability and fairness, accepting a theoretical reduction in immediacy (in the range of microseconds to milliseconds).

The evidence overwhelmingly supports the conclusion that **structural modifications to the matching engine can significantly reduce latency arbitrage and the scope for manipulation without destroying market quality.** The "inevitability" of manipulation is a flaw of specific designs, not of electronic trading itself. As regulators and exchanges continue to innovate, the market is likely to drift toward hybrid models that incorporate the speed of electronic matching with the protective logic of discrete time and speed bumps.

**Sources:**
1. [citadelsecurities.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3hRWWpHw4ojErYVP2G2CRG-1DtUdoWulTQRBu_ArxAiF8ErtxGAuh5zdzACVuD33XCN910RaM-4PXtcc3pViVtLkJwEwHohM6OTAYP8LF9amnwjgdO1esSf48NY_uQCfYQvvbAFai0PL83nXLiDwx-S8QNQHBun0ABgjPu-dTVL7yQMELQIWHErsO2w0-u4WA-4UUmKwdBduxwh6mU0wApQ9gdxlL_mD836JgUk1N5owrOxjbpwhh)
2. [hexn.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwB5VTJvCZgU003FRszZSCxyFh6AHNUQcnZM1q8X713XRvOvcYwxpwauPM9Tl9PVkkeV1aievAT4Vp0bVk2kZKjWbmhrqmD5vl_b2YIiWTT5MqRkHckE1f94RF8o99Z_rYu_o_t4Ar611o99MKDrAswHCfBjS3mS-Uphwkxw==)
3. [ericbudish.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGm8aA9NLNFRsJZzOrq5niehoOsFg0r31W428o8gxshqdrl1lfnrg4ogE-dsbuVDXhIrO6XU-w19LDF3jlMd0bUupNKFkrNCMTc6fXIkz5YSfWL7yeHkv6ti0Sl_ZoET-B6oe0SxZ4UHxf5HA63gduL_VnN_Kej1X1FXRxjkt4a_nvbwZg0VuysJoETcvn-ktyi-VpIxImyH_Ze)
4. [videohall.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKF5zDQpDCGErHP2fImVXVfu-1bHcjONGshWFh3PASk7xoR7YyOeHW5bmqx0AEoz2rHQaLZpvHscnce6fEgrP-reoDVQE14EfzHum7aUJUuor78jMVt7xDGs9_1FSAn216ArTBUWOuKuuw8mY=)
5. [questdb.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9ta52PviDpXS8bacg4iKYuTAuhrfOqZAo1AWzGCgMScp438H9vCTkSYTeYUY0cvOTZ5OyC30QQ209ZWkym7xnLd1gPXtl7WG4wNFI53QHX__IwAN52xxCoMwkQ-XG8dJ384cyXw==)
6. [quantvps.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvRyv9fJZbF1ksQBGe-JJVoG77DrWB2-OIZRFRAdRxlMSdNSq-3EQNWkg28vZpag4BkJlkfp79huT4iu02jKAPNypf4S7lriDHx4tVvGafuqF61Fifli3Uczu-wZZN9dzMRTBs4I_UjGHSx_uP)
7. [nber.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRQ89BAMOv-fYw393Jk-3Ngm6fKIfjjm91fwF6ASslGNT0CZRTBCVm3NNXba4CUXIqJ1b4RQ5FwOrqnczT2l5oKlAOo1IrFKSWlM7g7G-ZUANh9Olco_nKVWNShF-Bs-YcCfMVU1wyy4DVwreqYSNnpNzu_w==)
8. [highburyassociates.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzPlbRIFyMKMZwSHnfcQacxY0SGCzHNZ3RUEnnA0IuRFT64DYpbEdG07fBDe2FLpA-Ggcbx1ClXxU0zjnlIA9eDCByJgPJOF7sJUvvtxs7RGchL5q4WLsxLBrz-vU7IHlgr4kK7wGQF3bm7e2mRTRL_ji1qgMSZHBE6HMKLOGHGRGIBhHlDhH12YnjmTUVsGMnpwYEYJG0V4-BtB8Rne_u15A=)
9. [fia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0Gk-rXT9tUkaV98tcVFnQVR5zJcaHCZZvQlP3LeBd6xec9e61eMvtRhGiCHAjxzn6BZSPsUw8UmryMZGwbUUADh3PG2uY4jieW2nSNq9t0nLHHIBXlbLV1ChjxXMjj_jB_787GeyEjX05nOuMqJHWE5W2jMRZYUXDYR2jUSn4xLYeL_tDpR3ElVCtRtTPlL07lGaxJ8wcP_6MBaTvc5NKIg==)
10. [bis.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0T7B0htp_nhmJyMcvnlqHrrLc9Qp8R4Vjl1gQ1ZZZvoSLHbHH6xy-6_mpsqDJML_VEIXzkKkqzxGF5McZo83GoFRYbH0VpdIuj6t8WO7WNuUrgMxYir1a5j8=)
11. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9XvAYrbdjFIrzouaq_wUgA-wCvFylLMpIATqaoF7MpfTYe6m-JN7Va3N4NDIwOpXxIdPRS_eocvUpUqjO-FNh9PbCvgH58bhc8Y4v_7g0adev2bP13Qm_AC_8RV3fgfZffia75sooWTP5db8=)
12. [nber.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcAyAMxsF7LKYtJ_z66bNbNybhONlbun_WRAp6tT032XbJ40wAxyKLFgkrSqhThVdJwmhbGFFc76KAjmulbK20nZ9oV4yNUlVTo2F_tTV_k57RBxb7sDvc)
13. [market-bulls.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4xJvBFQwIk8EdEl8NGQ6Wg1temPEF_oDZHshZODVpaNJR-CAGvfhxkRy0IjjMv18BCTWhKIsFE5OofdlEeCHETWRNK_uzLq1KUFVvXJ8V06yqVHbDv7h_2kGDBov3qf1dK2zfe7PqJLU=)
14. [finchtrade.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmMKQgkWb79mlRxXqUDLP72s_xj7J_uHIJzyE87o7dBkxlCcMrjcMGLdnWqzB1dd546uwFvFpYjO1Kyx_MxfVnrIRG3LAqNHSIrXTTpQvAdJkHT8Pao7ZYAjbK7iPmZ7nH3Vhh6PSZGseX-nU=)
15. [greenwich.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMghpaeeWDL3luRGP5LzYqLTHK4Ri7xbEAwk1y8mUnQ2Oet55Af-IIM1kkxf3Jk_fpYPJcrKbY9JCFZpFg3p0J5XsdN0Dk1VhRgA1uEwoMUKkkLpfiicxMePiPNPGUpO1KcC8IjUpuwfP4V81lVPJgXsfp4st7yEof_4pk)
16. [questdb.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDGgSuTdZzinksy6rdBXSCrwvuEKsp5LRKDMdnSwEjxBRG9sqFSANHWo_1zpJPZNN2axDEHUzn-PWrvpKZjTXmKNFJylSH2hiRYVrPmG5Y8fzUXhEtoBrXCIfQygwk8dWVzX7jOhLNArrMr50=)
17. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqmD5drNkqewjiWLkrrni-7gL9F5Pgqsr8cNhfz0qp8DoV7pK_g1PNM3ImG8PGpM-6mtftbYfMiI1W1mZxQAb86V4IHD9_F164OiEGZPmPMiJxs-RM_7ldkNtE_hyDv3phzOv9Ty6h-x1SV_2X1WlnkiRun-5TjAMPVe6lbPPtPciUVJGfTnA_B9NSrhFOcp8=)
18. [unsw.edu.au](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwKrnnMR4r-ZYQ_YvmvfXkz2A8x7UOdaLYcZf6vOW2wl6pL72SOaMa-JrNn6ftGleyLFMX2FlBxXScohYhSqCorhSuCO3aqiYFd22hRy6yJlALxfK6_got64o2pR8400ooAufc6bNM2pzW3xELl7XGGNSuHo1t2s2yNQSIQgs3bC3zbNd-OCECmsnwdVgg4Ums6QLMV1tu)
19. [scispace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_G7FHQhq9n8NQjCcPk3SVHfsy63A6OKXDQ4zuGwOjWexO5C4CsU_6-yeraH-0-x5176gqL0qHhxX0tw8Tu_THie8qQjN5WgORjKAVmR-LzLj1kQL2BU6ML9itzYopXGVH7wPjGXBZW0JGayc8J_aLG7ESX1daqe9jXGsa2Ngv9789cDOhC4I4hkLnvTc=)
20. [europa.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFO1vI85mxdti1Hb6MbyVF0MdFICBgmDaRXMWRsgy0qZcg9vy3y908MVqjcIXHNWcSN-_PD5PCtMymCl0mRq_dWV8lyXxsHkYUnn2OZrWFsH-lcR0wM-dtGvzeMWEcUfYIRagTkGi6L60gJ8M=)
21. [tse-fr.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFB7nwnFUBa37gajVWxyYwp5Bcwciq0zft-m1ruLb6E_ACh3BEvxSbaZuGYxlIEJJqjhclWArGzZz89dg4kh0IMTrm7Vzfsn9jGmpY8bLg7ltz0neDkviOk-vfKXXbq2rK0Ux5f0TtHG_IiPyt737rQzZ4JMM4ADz5gbliUvaMulwTEb1xfv0PdGk2dxf6cogag5V_Hg1-PVOJNCyKCjeE9BO-Yj3_d6hEXZ9srfxVMe_RnQtzLBHbe51MZoAvbSXMs00dH8UxbHA==)
22. [aut.ac.nz](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-RtfGCUu-Mp3XPoeEvY4Rk152981S9K0mMHal1NC0BoyLO2FUTlIq5-In7a9ZCBLTaiO7uM8X8fRLhADd_Lk2MLCooff-3fAGvZDprWZzqZ7EgHEjfWxk-64JyQJv-lhPMRkH25WAOktEMckFDbuIvi4PspQR3edAEjr1OtNpd3AMa0r1bVrrj7UH9A9AM7W6jYeXXLfkrpENLEISTls5k0NcoJjA7beNmx8ToYKOuX-9AKN4bsAFianMQsmJtwicUyha6zXT1dZpkNHI0o462v0WyilllzYbtbYk-0uF)
23. [jpx.co.jp](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4-Bv7FJllD32hodyYFuKw9BJqznmGjlnXFg_p7dLhxbw4oer582C3fDlE2KWIqQOhdkS_Jbm3DM5XHpdeVQwGorQT1j9AYffvebM210pnZCFJm0O5D8tED5eQEbjV4lg7EeSOgFp9wU_mI39yzEN5wiWiXKjBkvK4zhqejvNFw4Zv4scrP8f4LPcMbmtodnKrizy3rm6TaY5l1siRiV6BhHK8xll3)
24. [saa.or.jp](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYHGyquu5zimkf980nzdcQsL_zKK-AZOSB5fL-aHzSrU5PaKM8eYWiHYUVziuiHagBFDeI5bHVVk0mG5xkulSOYXBgEymAoQon_AeijHSakKRuOGrysI03eBPPgwjrsVdwG4Yg0PmcCYf53NxQ7Y58Dg==)
25. [unimelb.edu.au](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTX33YPA1CiuL5naVutShZEgcsXJI9Y2XsApP-MWRCI0yWWahhkX1QwphqhpEtL129VS7Z7QJT52T7tGKUp8vZdnQiAeRmJyJCXOndh3zapEcKjVVzlY9T1GiCgE_4ZK0YBlYDJq1-J0P76_bp5w87-lrjTQ99w89xGOJ9NejmE2G2LaPg4WcKwIly4FfQ0u3zAM5j30uotSrsaaOIWkB5xvAxbd37geyXAFwwqLrpoQvaBEM=)
26. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1gIrA0qGvA0qa6y_VFsf7HOal-rGyf5RuovajZ7KGz-tF_OcEFy-8as-lXaADjhQMKiCA5FSLqdXsGA7d-1daUqVB5wMjYbCA8ZXJLCeFQWtI_nu9KRZgKjSSABvGCVDQavvJ0kPENsff)
27. [port.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmyK1qE2m2BqGyiiQRlWyagLlApkdpdTyzNOKg6fWpqXPQfildv8VmaJySgwdsCj0YVJtZcpQmlctjfD5NYRjx6rMMqe3BcGCGjHLyYiNFy_lAAdzNQ4ftdXpM6x6v14nQFvaEmYaMEYSJV1mkZCsG0CSCDJRxiFCQbtx7hJtAnf-MVFIKh8GloeFaU7_UIcTK6l8pfeAZeEHcuSshfcsKlN2c0yMISjSl9qejNhnFG3-qbAu0K4Nu)
28. [ifs.org.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElh4CXTjf_AADvPHgnwKkRpF5bf_-Sp9ncogyo6MK_JTx46_YC-3BAXTO5ZKggAUyiwvkxx595RPDdRatYwtNg2-qUILvfwtgcOj8lwTn4eXU_gbrSuXzNMRVy3xwN2WgrZIwHsu_CeZa7NU5sNYf-YreMfTtXfT1BZiY=)
29. [bluechipalgos.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHO5x9TOuOINA3qdr4C5E6zeL5M9bsQ_26nFbbWsw4gTYLsd-06JFfYh4vUc8V76Muu2tBodu_rPqACHcNUDU2rOSdZ-g5fG71cSWtoB9EDtJuG9eBuig9zqcTI8rnpQGuoAK34uP9Z7iitmz2EDET6rUH-jN2Dtfrk74ja7hxmJSGDt8q3oW3CZes=)
30. [academia.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoSeTq-RrRzfLPq4QjB16gxaGluXF7v-YNSCp3yypEel7xP0m9QzIxytIUnQlsGhLPDWO4eNdYHRPrS4aEwS2m70gQt088IzMUpxXw9e06WHdkviZ6vWrL5vaZMMiVRqG2PSMj2qabHOBEVbzoArzzwCL0RSlLGoeTaKxijJ73sth7aXOh76hrbvVMGY6Azyy2mpXeTvqiOjYDNrpwx3o=)
31. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEguVRXj8zyWaSdkD-nivZo2cbDAqqDKdlR8pHc9JIlArFzRtlPH40nX3TxcLRog6z5LAsBj9DJOnsc_n2gBWx0fUSCXiPtT1FvC-QTneoCXMSZLQijYGRDhqQ0f7_aGIvK810TCa-iNg==)
32. [quora.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_nctEWDPmhTDUAU-6YES-fxZyrmzEonHrfzP8K09Nis-M_yQpU66BFAcEdylLhMWmWB-KGMEUyX0PSQjhknYiMuqsESuIiDt_0YenqvMMAF7oPVDv2EFRZ3njWRrAelt1u8glZQBaIiRU-YPYqX-iTrgwJB6mmOMTT00g3MlYtDFPyd0mFfO_XFRXD412jSyj2yVzSJqDCkvOskkwYg==)
33. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrCKTuMGeTxK4EyzTmdCDxUMCLOHkopc887h9Lf7ZqGsQLdEyuhTr4elW5v_omArZF8gAal9j7YUBp0k2mc2j9J7zovsqpHXX3oOQzVMr0SDrCWUrOduAMCMeOnAzr1gB7odA8I9wWIR7YZkiJYwv44pM=)
34. [umd.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLf6_HgcgU8wsfRwdIs0lu10QjNvfWoLvP-xGmC6R1CM0NU83-RzUoWz9WjAnqi-Yb1aQJ51D-EIrtWpzgD6HGSVmRrmd3DeXOSUJwb7jd_vg7TRZfrZFh92GfmA4VIsqnvFKHSp4odA==)
35. [marketsmedia.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGSSQZGoMxnYDLHIh6UMFsmFX_dU5yZ9O_nu05ofuAo33jG4F1Jb32i1kEJBPUMVbgIh4cj7rU1wdaTa_0ItHG5YG1YHfp7CfzmAJDc82qwu_4zOf_QPBYNQB-d2NgQ4I4p2DsGzg697NmFsws)
36. [iex.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEitAaYyMunly4wNI9qwTr0Ln2gJIB09WaKoqzkpKihaQP3HxIZ9QDcAPQv8R-i6adn3A9Q01XDlGB-uOtOs3Xq5Nel5iqDiQ_yAiEmCouFiy76YN-hJB92LqcYkCJrFMcITVj8L9sb3jP8ssgmtdYEipJ0iMTW6k5dpI7kq7Rbzt8RbapHwg==)
37. [iexexchange.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEOrkXMbY5O_eVjHnheEtqkQZACLdq57XfJL8Eyq9HUuYyly_W9zNCGj-ygTq7QqJWmCTboUaic9eXZ7qpWJi5cItes5ZZD1ufs4asNm9lsEghhkZ_TqSb5HEo)
38. [globaltrading.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG54mFjZ_VpNgIrwQ6y5IZaem-Epb7W_O2Upv8vfXijuyvYFeI4krw1BRYOUfQLeCpnKkxJcQMKk1NBILtdJFIXCq1ryVU6AZ4VGoqzUA49vR0umExQ0SWv-B2ejdPPPvaGFZW7s1tUshwVCRDfZ4OeV83S_kd761NgJ6oDoJ_ROCeW7Dz8LKikW8mzINw00btkZ530ukxGB8mDUs1wSUU0VRc=)
39. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxHczdCvGMS4KG4Z4PKgKIy6ttKsS0ITeJMD6YIvcvbaDa3mxLj1jXRoIaT-2XKqdrm5xeYXMgU6iFaz14O9juozuNW0PuyLgvZaRhe6Jc4LyFDI00YgxGHbINji6vzqwo-RSOCjv1u2nXdWcyd617meYXRVILJRJi14jxiWumq5DjI5I6ZE8RUymth4aYYQBVIpE4Y6HDbZA3Fg==)
40. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6ei4fuxF-f5taH1C8NIhDLNMj7q11yBOUx5YeJHQqBGAUYJBkTymNHuMKFb4gRToFftxCzcK33Fj-UF3y5Rn-d3wm_fVAQ8RFwhFuSXCRDWkKS-eiQw==)
41. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2mEU6SQ5gts6nSB0jSeZJUSoM1LoVjlcWFtFNvH812gj66FzeZSap53pGvwC2DvexAJxVCjbawJgl38nGLdDR5B9N1VXBBnyowyXH0jiwUYxsB5Qq6wgC-tfEbbA-EwJm9GjcHE5VabDD7xX9M-LlNlXA6a6rHfi3zeo=)
42. [squarespace.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXqHSHmtEIrpM0g-JV1pcqc-g5VoT8SBo9xqHNK79IfR4PNbRWgCd0G_nJu9e2oOYTHZ6CvUyap0lAuBqKp5xy4sbPPhHse4w-ns7JJxfxQP9k9zDZEi61SqcTdoZpwq6PmD3dq0O0TRap4nGiNVI98TOTRSFXRNVrw3zZTudScDfZO27Kcp-QLpQRHCOxUKj77fFfjiwoGqAPfblaXGl2Wizp-0ALiAP-z-cQecsNL1U-tN5NdHIgjfQ=)
43. [amf-france.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFBzfNClCKYj1AN0iL4CgP7b-9y_YNZJ6VBwg7an5sFmVRIGnAoy7CCDPaV_QapIXH_83f8RLIuKd1CmnvW1WOFL-Ox3Nb7dGN5nwyTl-biQMtgoWvb5RNwTI38kBgpZSQ085MUN_4LTE4hkJq-lDO4qVcEfhSRMfwgQAQvp-MONibcIbALJbYcXn9rkSnnAo70lUC6PMvArg5F_NkZiNhi_IBAQj9iEaAlbtOgmUmCZX2hGEnQ3rnS082smZyfNdjkhKPAVt5iTTP3Kc7CjRulmK-bOCeCHThUxicq7tvW8Q=)
44. [sec.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGM0CYDtwZDtAze3-h951pdwG2Lv9vlg1tt5DYfmL_6_xicFzeHI_PJwBcgcm1QPjkIi9nA6nxkWktf4k-QZhwBdWk1dc4Ch1A-peuNnJJ8D2q9sRP0SN23L1H49Gl-KIEV9uacz_JdxdyVV3qUwyMuPilf23w4nw==)
45. [tradersmagazine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1TsiPGUiWOHoXX_8H1Jy1io9HB-Gj_5dgNE2ea0Rg4sEG5S46_gxqcA5D-85ISqtR4A72KIe0DmKCxNNhycViVYtcNKxYqHIkyvAPJF4H8nBHYj_E_JDE59H2jOxmOBNDcxfkTuDiZGXZaQR7dg5cQNS7PnhvaGESKlTS9AcjAduwSDX9KtnXsshzD5PPsSx4ag==)
46. [afme.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmeU7k7XVsFxHKAhO1IkYiL2Cn-mgq2XMqgASjA9JLvawwCTO5AEPYsv8YWzDhvMmpgnEjDjaYDAz-oUvXYDktr3UDcneCmUWG6f9SXDLJ4ISQ0fLk8wvlheR8UPOSYpEWy7vTvyBZWt_bgGUepPcIaCtgz8c18vqCH7Hm-7Z2CVbOKu-3KnAbztxu_BRh15nFQ-Kr1ZSQDSg=)
47. [amazonaws.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSAs6WkgdGZ0DQlSlO73ikKCEi-zqh_BN5Cyp7khrWaYovUCv7K8UbY6UvKoz1T9ufB2vJB8xY39__UFY0hTXDEdt6D3cauVu4zfNPjUmfZqCukSYCu05KoZXVoKFDOye5oVGuaLHNWfsKN4EOgvnmkUeGQmR9BwZczvzuc6ubhttld4gQLZ-_WQppgIBIWzLFRCgduALJ34TenRR0)
48. [wienerborse.at](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxSNvjXNujFyNFPfl3T2Sl5aBDTP3qlafUIVw5dvA2w6mkmm6tdwlL8j40tFC6DguCAHInxVUcgNbThIml3meGNTu8C1saUTzm_Un-I26-ucqHnwnGbPJsOoSOdLwv-NasJhG1zGOhqSaLumkXsePhl1hKT44s0FRbQ1b8RS7PUPt_vM_g)
49. [europa.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyQ3VzKajbxJ5hVBpUWqen-YL6wtmsP-voKvKNLWNn6eIWBLOQAdzOi56J0s0kK7yrmIxYOXTPSHeZfdTGWspa25m4r218syCUADnZhi1qP6jpVGX4Ihb-Eo-TIUnKgY8KroxIrlxsSKoliPwldv0tzQOt6favOpHE8GlYZCrKUulcczM=)
50. [afm.nl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrvMPEh6sottAf4VbGODkqLWqrlTZmOzyf8BJCiOIu6ooRdfwZcCMvkb_vyZ-KUaXaERbSkFyyzeXNIdMrFvIBXz1XZ0cl5UelvYACaexlNX_WN4ro8HGO9Q39y9AMcmoZToqi35T7LOo3F-VIw1JW4rxuXArq8KHh1RlkBt-JbmM2s8hwq0D0D5TEOood2JNa4aW7jAJu363dCEJUCN2n8HyRb9_oN4ID0Dx-__BpDMS6kiEFIyLHuyptZyg0HOCfoRg=)
51. [fsa.go.jp](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF1I2MeHYmgW0b0D3DjBIrnZFCjmAcutbuLOTaGg0b4EKqBqqW0WKCof61KV5O4maJM_PbpQPsp0pTPZ1w3xQhMCehWV0ENyx2a5COvP3Mqm_y_HS_88S96h7n4uhOoxpBvakbcyiNqkfuLUDrLDFHcyXK3JdBBZzaJcBJzL9mDr188IsVqXenc3bZ9qwyrRxFiYrFICTgiGA9eiQbd)
52. [ohebashi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGe0ebN17i0jfJJfJYuOXs-egrAAfAfFlU9JpkxluEzsFOZmlCyBvNRtBNOnJM0KDR0ONQmdb9G5Ki1Aeo2AkLHrcKnhoOpju94kfX-KHen4sYYIyGJiZzyttcnolTjya_pKRoRLQFhyLRp3kATPEfXtgFi9jc-8w==)
53. [investsmart.com.au](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfIsBPz0BTdVTyVi1iWmM8HxrZwMSWmNAnRxbl2tv6gzBxOJuvyUKilN-peeOXxn_Rc4YvckskSOaoZWS3sGFLE5qYOHKcNbZZFUpRedV78VIAqsrN1elqVT7iNQa2FIOH2bu9m3gG_oahTJt53boPIsPkvA3d_mm9WWYhiXV78NW6RA==)
54. [superreview.com.au](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEc0lOIItdXZTX0YBdxMxYqdPwv6W4S5ntp3__lLOshLKb2V0NtuCjxmAwFM-JerdX7UVFV5UY7NaWfy-GwfswOigIF9yjZNYDvmYSW_QM-0rTOp-IgNzKJD0hSwWfFlUs-gQcqS9J5BzHE8a1YXbPb61whBxjHHseVQCxH5g==)
55. [cfainstitute.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYKaZxTlWeKgwKt9y2RBuvsby7rKs53wo4-4gUh2C4IFFj1QS0r4_msM22e21mhFv5eq16lKNqwmXsUQkR4Xpb7ZiaCc5hvCG8LugJztBZ5LZq-m53Q5iCZRmtCMlcjbia_UPEZ5mfQn7Qdz0QcyqFsIT6JNwO-3YRt7BhsZ2fwr_RGzwm0L2dp9za66B1RUKer6L52MAEc9c1KvGfn8U3CtllAXldK-x1HE-ODH08K9Zu5iHR)
56. [nber.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrxu9y4YE5WwCJLOP9uKQaMoA9H81S3LRW-vXIPM1sIUxfydvURmz9KXw2SYrrPUsP3LQeiCUY9-5TwsApnJcuF9-Qy4YOr4Q4OyveaL6neR2zmQIa3hmQSzQWDesyLmEMY9GL_bAYERx5ETotAI9J69gGzfflfng=)
57. [binance.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTYfN_FJalcCqgYkx-nnGSarr085o_TrbIcESbMUmwwaHRvhhu__fsNxsUVtvkHWgGTUqf3eU8Ccg7OWC1riCmd5Ishr1QX6dP9c1exuM5MruthbJb-YyNTdPWBWiyKljDx0l4L5mC4KTsAZy0mpDtYOa18nkSVpeq7tk7Xjk4TrD8u-S1Qglflklj)


## Annotations
Annotation(end_index=3403, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwB5VTJvCZgU003FRszZSCxyFh6AHNUQcnZM1q8X713XRvOvcYwxpwauPM9Tl9PVkkeV1aievAT4Vp0bVk2kZKjWbmhrqmD5vl_b2YIiWTT5MqRkHckE1f94RF8o99Z_rYu_o_t4Ar611o99MKDrAswHCfBjS3mS-Uphwkxw==', start_index=3391)
Annotation(end_index=3403, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3hRWWpHw4ojErYVP2G2CRG-1DtUdoWulTQRBu_ArxAiF8ErtxGAuh5zdzACVuD33XCN910RaM-4PXtcc3pViVtLkJwEwHohM6OTAYP8LF9amnwjgdO1esSf48NY_uQCfYQvvbAFai0PL83nXLiDwx-S8QNQHBun0ABgjPu-dTVL7yQMELQIWHErsO2w0-u4WA-4UUmKwdBduxwh6mU0wApQ9gdxlL_mD836JgUk1N5owrOxjbpwhh', start_index=3391)
Annotation(end_index=3561, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3hRWWpHw4ojErYVP2G2CRG-1DtUdoWulTQRBu_ArxAiF8ErtxGAuh5zdzACVuD33XCN910RaM-4PXtcc3pViVtLkJwEwHohM6OTAYP8LF9amnwjgdO1esSf48NY_uQCfYQvvbAFai0PL83nXLiDwx-S8QNQHBun0ABgjPu-dTVL7yQMELQIWHErsO2w0-u4WA-4UUmKwdBduxwh6mU0wApQ9gdxlL_mD836JgUk1N5owrOxjbpwhh', start_index=3552)
Annotation(end_index=4026, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3hRWWpHw4ojErYVP2G2CRG-1DtUdoWulTQRBu_ArxAiF8ErtxGAuh5zdzACVuD33XCN910RaM-4PXtcc3pViVtLkJwEwHohM6OTAYP8LF9amnwjgdO1esSf48NY_uQCfYQvvbAFai0PL83nXLiDwx-S8QNQHBun0ABgjPu-dTVL7yQMELQIWHErsO2w0-u4WA-4UUmKwdBduxwh6mU0wApQ9gdxlL_mD836JgUk1N5owrOxjbpwhh', start_index=4017)
Annotation(end_index=4561, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGm8aA9NLNFRsJZzOrq5niehoOsFg0r31W428o8gxshqdrl1lfnrg4ogE-dsbuVDXhIrO6XU-w19LDF3jlMd0bUupNKFkrNCMTc6fXIkz5YSfWL7yeHkv6ti0Sl_ZoET-B6oe0SxZ4UHxf5HA63gduL_VnN_Kej1X1FXRxjkt4a_nvbwZg0VuysJoETcvn-ktyi-VpIxImyH_Ze', start_index=4552)
Annotation(end_index=5049, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGm8aA9NLNFRsJZzOrq5niehoOsFg0r31W428o8gxshqdrl1lfnrg4ogE-dsbuVDXhIrO6XU-w19LDF3jlMd0bUupNKFkrNCMTc6fXIkz5YSfWL7yeHkv6ti0Sl_ZoET-B6oe0SxZ4UHxf5HA63gduL_VnN_Kej1X1FXRxjkt4a_nvbwZg0VuysJoETcvn-ktyi-VpIxImyH_Ze', start_index=5040)
Annotation(end_index=5342, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGm8aA9NLNFRsJZzOrq5niehoOsFg0r31W428o8gxshqdrl1lfnrg4ogE-dsbuVDXhIrO6XU-w19LDF3jlMd0bUupNKFkrNCMTc6fXIkz5YSfWL7yeHkv6ti0Sl_ZoET-B6oe0SxZ4UHxf5HA63gduL_VnN_Kej1X1FXRxjkt4a_nvbwZg0VuysJoETcvn-ktyi-VpIxImyH_Ze', start_index=5333)
Annotation(end_index=5804, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvRyv9fJZbF1ksQBGe-JJVoG77DrWB2-OIZRFRAdRxlMSdNSq-3EQNWkg28vZpag4BkJlkfp79huT4iu02jKAPNypf4S7lriDHx4tVvGafuqF61Fifli3Uczu-wZZN9dzMRTBs4I_UjGHSx_uP', start_index=5789)
Annotation(end_index=5804, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF9ta52PviDpXS8bacg4iKYuTAuhrfOqZAo1AWzGCgMScp438H9vCTkSYTeYUY0cvOTZ5OyC30QQ209ZWkym7xnLd1gPXtl7WG4wNFI53QHX__IwAN52xxCoMwkQ-XG8dJ384cyXw==', start_index=5789)
Annotation(end_index=5804, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKF5zDQpDCGErHP2fImVXVfu-1bHcjONGshWFh3PASk7xoR7YyOeHW5bmqx0AEoz2rHQaLZpvHscnce6fEgrP-reoDVQE14EfzHum7aUJUuor78jMVt7xDGs9_1FSAn216ArTBUWOuKuuw8mY=', start_index=5789)
Annotation(end_index=6106, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKF5zDQpDCGErHP2fImVXVfu-1bHcjONGshWFh3PASk7xoR7YyOeHW5bmqx0AEoz2rHQaLZpvHscnce6fEgrP-reoDVQE14EfzHum7aUJUuor78jMVt7xDGs9_1FSAn216ArTBUWOuKuuw8mY=', start_index=6094)
Annotation(end_index=6106, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRQ89BAMOv-fYw393Jk-3Ngm6fKIfjjm91fwF6ASslGNT0CZRTBCVm3NNXba4CUXIqJ1b4RQ5FwOrqnczT2l5oKlAOo1IrFKSWlM7g7G-ZUANh9Olco_nKVWNShF-Bs-YcCfMVU1wyy4DVwreqYSNnpNzu_w==', start_index=6094)
Annotation(end_index=6428, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0Gk-rXT9tUkaV98tcVFnQVR5zJcaHCZZvQlP3LeBd6xec9e61eMvtRhGiCHAjxzn6BZSPsUw8UmryMZGwbUUADh3PG2uY4jieW2nSNq9t0nLHHIBXlbLV1ChjxXMjj_jB_787GeyEjX05nOuMqJHWE5W2jMRZYUXDYR2jUSn4xLYeL_tDpR3ElVCtRtTPlL07lGaxJ8wcP_6MBaTvc5NKIg==', start_index=6412)
Annotation(end_index=6428, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzPlbRIFyMKMZwSHnfcQacxY0SGCzHNZ3RUEnnA0IuRFT64DYpbEdG07fBDe2FLpA-Ggcbx1ClXxU0zjnlIA9eDCByJgPJOF7sJUvvtxs7RGchL5q4WLsxLBrz-vU7IHlgr4kK7wGQF3bm7e2mRTRL_ji1qgMSZHBE6HMKLOGHGRGIBhHlDhH12YnjmTUVsGMnpwYEYJG0V4-BtB8Rne_u15A=', start_index=6412)
Annotation(end_index=6428, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0T7B0htp_nhmJyMcvnlqHrrLc9Qp8R4Vjl1gQ1ZZZvoSLHbHH6xy-6_mpsqDJML_VEIXzkKkqzxGF5McZo83GoFRYbH0VpdIuj6t8WO7WNuUrgMxYir1a5j8=', start_index=6412)
Annotation(end_index=6777, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzPlbRIFyMKMZwSHnfcQacxY0SGCzHNZ3RUEnnA0IuRFT64DYpbEdG07fBDe2FLpA-Ggcbx1ClXxU0zjnlIA9eDCByJgPJOF7sJUvvtxs7RGchL5q4WLsxLBrz-vU7IHlgr4kK7wGQF3bm7e2mRTRL_ji1qgMSZHBE6HMKLOGHGRGIBhHlDhH12YnjmTUVsGMnpwYEYJG0V4-BtB8Rne_u15A=', start_index=6756)
Annotation(end_index=6777, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcAyAMxsF7LKYtJ_z66bNbNybhONlbun_WRAp6tT032XbJ40wAxyKLFgkrSqhThVdJwmhbGFFc76KAjmulbK20nZ9oV4yNUlVTo2F_tTV_k57RBxb7sDvc', start_index=6756)
Annotation(end_index=6777, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0T7B0htp_nhmJyMcvnlqHrrLc9Qp8R4Vjl1gQ1ZZZvoSLHbHH6xy-6_mpsqDJML_VEIXzkKkqzxGF5McZo83GoFRYbH0VpdIuj6t8WO7WNuUrgMxYir1a5j8=', start_index=6756)
Annotation(end_index=6777, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9XvAYrbdjFIrzouaq_wUgA-wCvFylLMpIATqaoF7MpfTYe6m-JN7Va3N4NDIwOpXxIdPRS_eocvUpUqjO-FNh9PbCvgH58bhc8Y4v_7g0adev2bP13Qm_AC_8RV3fgfZffia75sooWTP5db8=', start_index=6756)
Annotation(end_index=7089, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4xJvBFQwIk8EdEl8NGQ6Wg1temPEF_oDZHshZODVpaNJR-CAGvfhxkRy0IjjMv18BCTWhKIsFE5OofdlEeCHETWRNK_uzLq1KUFVvXJ8V06yqVHbDv7h_2kGDBov3qf1dK2zfe7PqJLU=', start_index=7075)
Annotation(end_index=7089, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmMKQgkWb79mlRxXqUDLP72s_xj7J_uHIJzyE87o7dBkxlCcMrjcMGLdnWqzB1dd546uwFvFpYjO1Kyx_MxfVnrIRG3LAqNHSIrXTTpQvAdJkHT8Pao7ZYAjbK7iPmZ7nH3Vhh6PSZGseX-nU=', start_index=7075)
Annotation(end_index=7282, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMghpaeeWDL3luRGP5LzYqLTHK4Ri7xbEAwk1y8mUnQ2Oet55Af-IIM1kkxf3Jk_fpYPJcrKbY9JCFZpFg3p0J5XsdN0Dk1VhRgA1uEwoMUKkkLpfiicxMePiPNPGUpO1KcC8IjUpuwfP4V81lVPJgXsfp4st7yEof_4pk', start_index=7269)
Annotation(end_index=7282, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvRyv9fJZbF1ksQBGe-JJVoG77DrWB2-OIZRFRAdRxlMSdNSq-3EQNWkg28vZpag4BkJlkfp79huT4iu02jKAPNypf4S7lriDHx4tVvGafuqF61Fifli3Uczu-wZZN9dzMRTBs4I_UjGHSx_uP', start_index=7269)
Annotation(end_index=7474, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvRyv9fJZbF1ksQBGe-JJVoG77DrWB2-OIZRFRAdRxlMSdNSq-3EQNWkg28vZpag4BkJlkfp79huT4iu02jKAPNypf4S7lriDHx4tVvGafuqF61Fifli3Uczu-wZZN9dzMRTBs4I_UjGHSx_uP', start_index=7461)
Annotation(end_index=7474, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDGgSuTdZzinksy6rdBXSCrwvuEKsp5LRKDMdnSwEjxBRG9sqFSANHWo_1zpJPZNN2axDEHUzn-PWrvpKZjTXmKNFJylSH2hiRYVrPmG5Y8fzUXhEtoBrXCIfQygwk8dWVzX7jOhLNArrMr50=', start_index=7461)
Annotation(end_index=7693, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGwKrnnMR4r-ZYQ_YvmvfXkz2A8x7UOdaLYcZf6vOW2wl6pL72SOaMa-JrNn6ftGleyLFMX2FlBxXScohYhSqCorhSuCO3aqiYFd22hRy6yJlALxfK6_got64o2pR8400ooAufc6bNM2pzW3xELl7XGGNSuHo1t2s2yNQSIQgs3bC3zbNd-OCECmsnwdVgg4Ums6QLMV1tu', start_index=7679)
Annotation(end_index=7693, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqmD5drNkqewjiWLkrrni-7gL9F5Pgqsr8cNhfz0qp8DoV7pK_g1PNM3ImG8PGpM-6mtftbYfMiI1W1mZxQAb86V4IHD9_F164OiEGZPmPMiJxs-RM_7ldkNtE_hyDv3phzOv9Ty6h-x1SV_2X1WlnkiRun-5TjAMPVe6lbPPtPciUVJGfTnA_B9NSrhFOcp8=', start_index=7679)
Annotation(end_index=7865, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_G7FHQhq9n8NQjCcPk3SVHfsy63A6OKXDQ4zuGwOjWexO5C4CsU_6-yeraH-0-x5176gqL0qHhxX0tw8Tu_THie8qQjN5WgORjKAVmR-LzLj1kQL2BU6ML9itzYopXGVH7wPjGXBZW0JGayc8J_aLG7ESX1daqe9jXGsa2Ngv9789cDOhC4I4hkLnvTc=', start_index=7855)
Annotation(end_index=8353, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-RtfGCUu-Mp3XPoeEvY4Rk152981S9K0mMHal1NC0BoyLO2FUTlIq5-In7a9ZCBLTaiO7uM8X8fRLhADd_Lk2MLCooff-3fAGvZDprWZzqZ7EgHEjfWxk-64JyQJv-lhPMRkH25WAOktEMckFDbuIvi4PspQR3edAEjr1OtNpd3AMa0r1bVrrj7UH9A9AM7W6jYeXXLfkrpENLEISTls5k0NcoJjA7beNmx8ToYKOuX-9AKN4bsAFianMQsmJtwicUyha6zXT1dZpkNHI0o462v0WyilllzYbtbYk-0uF', start_index=8335)
Annotation(end_index=8353, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFO1vI85mxdti1Hb6MbyVF0MdFICBgmDaRXMWRsgy0qZcg9vy3y908MVqjcIXHNWcSN-_PD5PCtMymCl0mRq_dWV8lyXxsHkYUnn2OZrWFsH-lcR0wM-dtGvzeMWEcUfYIRagTkGi6L60gJ8M=', start_index=8335)
Annotation(end_index=8353, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFB7nwnFUBa37gajVWxyYwp5Bcwciq0zft-m1ruLb6E_ACh3BEvxSbaZuGYxlIEJJqjhclWArGzZz89dg4kh0IMTrm7Vzfsn9jGmpY8bLg7ltz0neDkviOk-vfKXXbq2rK0Ux5f0TtHG_IiPyt737rQzZ4JMM4ADz5gbliUvaMulwTEb1xfv0PdGk2dxf6cogag5V_Hg1-PVOJNCyKCjeE9BO-Yj3_d6hEXZ9srfxVMe_RnQtzLBHbe51MZoAvbSXMs00dH8UxbHA==', start_index=8335)
Annotation(end_index=8517, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4-Bv7FJllD32hodyYFuKw9BJqznmGjlnXFg_p7dLhxbw4oer582C3fDlE2KWIqQOhdkS_Jbm3DM5XHpdeVQwGorQT1j9AYffvebM210pnZCFJm0O5D8tED5eQEbjV4lg7EeSOgFp9wU_mI39yzEN5wiWiXKjBkvK4zhqejvNFw4Zv4scrP8f4LPcMbmtodnKrizy3rm6TaY5l1siRiV6BhHK8xll3', start_index=8504)
Annotation(end_index=8517, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3hRWWpHw4ojErYVP2G2CRG-1DtUdoWulTQRBu_ArxAiF8ErtxGAuh5zdzACVuD33XCN910RaM-4PXtcc3pViVtLkJwEwHohM6OTAYP8LF9amnwjgdO1esSf48NY_uQCfYQvvbAFai0PL83nXLiDwx-S8QNQHBun0ABgjPu-dTVL7yQMELQIWHErsO2w0-u4WA-4UUmKwdBduxwh6mU0wApQ9gdxlL_mD836JgUk1N5owrOxjbpwhh', start_index=8504)
Annotation(end_index=8681, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3hRWWpHw4ojErYVP2G2CRG-1DtUdoWulTQRBu_ArxAiF8ErtxGAuh5zdzACVuD33XCN910RaM-4PXtcc3pViVtLkJwEwHohM6OTAYP8LF9amnwjgdO1esSf48NY_uQCfYQvvbAFai0PL83nXLiDwx-S8QNQHBun0ABgjPu-dTVL7yQMELQIWHErsO2w0-u4WA-4UUmKwdBduxwh6mU0wApQ9gdxlL_mD836JgUk1N5owrOxjbpwhh', start_index=8668)
Annotation(end_index=8681, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYHGyquu5zimkf980nzdcQsL_zKK-AZOSB5fL-aHzSrU5PaKM8eYWiHYUVziuiHagBFDeI5bHVVk0mG5xkulSOYXBgEymAoQon_AeijHSakKRuOGrysI03eBPPgwjrsVdwG4Yg0PmcCYf53NxQ7Y58Dg==', start_index=8668)
Annotation(end_index=8890, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3hRWWpHw4ojErYVP2G2CRG-1DtUdoWulTQRBu_ArxAiF8ErtxGAuh5zdzACVuD33XCN910RaM-4PXtcc3pViVtLkJwEwHohM6OTAYP8LF9amnwjgdO1esSf48NY_uQCfYQvvbAFai0PL83nXLiDwx-S8QNQHBun0ABgjPu-dTVL7yQMELQIWHErsO2w0-u4WA-4UUmKwdBduxwh6mU0wApQ9gdxlL_mD836JgUk1N5owrOxjbpwhh', start_index=8881)
Annotation(end_index=9104, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE4-Bv7FJllD32hodyYFuKw9BJqznmGjlnXFg_p7dLhxbw4oer582C3fDlE2KWIqQOhdkS_Jbm3DM5XHpdeVQwGorQT1j9AYffvebM210pnZCFJm0O5D8tED5eQEbjV4lg7EeSOgFp9wU_mI39yzEN5wiWiXKjBkvK4zhqejvNFw4Zv4scrP8f4LPcMbmtodnKrizy3rm6TaY5l1siRiV6BhHK8xll3', start_index=9090)
Annotation(end_index=9104, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYHGyquu5zimkf980nzdcQsL_zKK-AZOSB5fL-aHzSrU5PaKM8eYWiHYUVziuiHagBFDeI5bHVVk0mG5xkulSOYXBgEymAoQon_AeijHSakKRuOGrysI03eBPPgwjrsVdwG4Yg0PmcCYf53NxQ7Y58Dg==', start_index=9090)
Annotation(end_index=9719, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTX33YPA1CiuL5naVutShZEgcsXJI9Y2XsApP-MWRCI0yWWahhkX1QwphqhpEtL129VS7Z7QJT52T7tGKUp8vZdnQiAeRmJyJCXOndh3zapEcKjVVzlY9T1GiCgE_4ZK0YBlYDJq1-J0P76_bp5w87-lrjTQ99w89xGOJ9NejmE2G2LaPg4WcKwIly4FfQ0u3zAM5j30uotSrsaaOIWkB5xvAxbd37geyXAFwwqLrpoQvaBEM=', start_index=9701)
Annotation(end_index=9719, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1gIrA0qGvA0qa6y_VFsf7HOal-rGyf5RuovajZ7KGz-tF_OcEFy-8as-lXaADjhQMKiCA5FSLqdXsGA7d-1daUqVB5wMjYbCA8ZXJLCeFQWtI_nu9KRZgKjSSABvGCVDQavvJ0kPENsff', start_index=9701)
Annotation(end_index=9719, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHmyK1qE2m2BqGyiiQRlWyagLlApkdpdTyzNOKg6fWpqXPQfildv8VmaJySgwdsCj0YVJtZcpQmlctjfD5NYRjx6rMMqe3BcGCGjHLyYiNFy_lAAdzNQ4ftdXpM6x6v14nQFvaEmYaMEYSJV1mkZCsG0CSCDJRxiFCQbtx7hJtAnf-MVFIKh8GloeFaU7_UIcTK6l8pfeAZeEHcuSshfcsKlN2c0yMISjSl9qejNhnFG3-qbAu0K4Nu', start_index=9701)
Annotation(end_index=9957, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTX33YPA1CiuL5naVutShZEgcsXJI9Y2XsApP-MWRCI0yWWahhkX1QwphqhpEtL129VS7Z7QJT52T7tGKUp8vZdnQiAeRmJyJCXOndh3zapEcKjVVzlY9T1GiCgE_4ZK0YBlYDJq1-J0P76_bp5w87-lrjTQ99w89xGOJ9NejmE2G2LaPg4WcKwIly4FfQ0u3zAM5j30uotSrsaaOIWkB5xvAxbd37geyXAFwwqLrpoQvaBEM=', start_index=9943)
Annotation(end_index=9957, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1gIrA0qGvA0qa6y_VFsf7HOal-rGyf5RuovajZ7KGz-tF_OcEFy-8as-lXaADjhQMKiCA5FSLqdXsGA7d-1daUqVB5wMjYbCA8ZXJLCeFQWtI_nu9KRZgKjSSABvGCVDQavvJ0kPENsff', start_index=9943)
Annotation(end_index=10151, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTX33YPA1CiuL5naVutShZEgcsXJI9Y2XsApP-MWRCI0yWWahhkX1QwphqhpEtL129VS7Z7QJT52T7tGKUp8vZdnQiAeRmJyJCXOndh3zapEcKjVVzlY9T1GiCgE_4ZK0YBlYDJq1-J0P76_bp5w87-lrjTQ99w89xGOJ9NejmE2G2LaPg4WcKwIly4FfQ0u3zAM5j30uotSrsaaOIWkB5xvAxbd37geyXAFwwqLrpoQvaBEM=', start_index=10141)
Annotation(end_index=10446, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElh4CXTjf_AADvPHgnwKkRpF5bf_-Sp9ncogyo6MK_JTx46_YC-3BAXTO5ZKggAUyiwvkxx595RPDdRatYwtNg2-qUILvfwtgcOj8lwTn4eXU_gbrSuXzNMRVy3xwN2WgrZIwHsu_CeZa7NU5sNYf-YreMfTtXfT1BZiY=', start_index=10432)
Annotation(end_index=10446, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHO5x9TOuOINA3qdr4C5E6zeL5M9bsQ_26nFbbWsw4gTYLsd-06JFfYh4vUc8V76Muu2tBodu_rPqACHcNUDU2rOSdZ-g5fG71cSWtoB9EDtJuG9eBuig9zqcTI8rnpQGuoAK34uP9Z7iitmz2EDET6rUH-jN2Dtfrk74ja7hxmJSGDt8q3oW3CZes=', start_index=10432)
Annotation(end_index=10849, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFTX33YPA1CiuL5naVutShZEgcsXJI9Y2XsApP-MWRCI0yWWahhkX1QwphqhpEtL129VS7Z7QJT52T7tGKUp8vZdnQiAeRmJyJCXOndh3zapEcKjVVzlY9T1GiCgE_4ZK0YBlYDJq1-J0P76_bp5w87-lrjTQ99w89xGOJ9NejmE2G2LaPg4WcKwIly4FfQ0u3zAM5j30uotSrsaaOIWkB5xvAxbd37geyXAFwwqLrpoQvaBEM=', start_index=10835)
Annotation(end_index=10849, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoSeTq-RrRzfLPq4QjB16gxaGluXF7v-YNSCp3yypEel7xP0m9QzIxytIUnQlsGhLPDWO4eNdYHRPrS4aEwS2m70gQt088IzMUpxXw9e06WHdkviZ6vWrL5vaZMMiVRqG2PSMj2qabHOBEVbzoArzzwCL0RSlLGoeTaKxijJ73sth7aXOh76hrbvVMGY6Azyy2mpXeTvqiOjYDNrpwx3o=', start_index=10835)
Annotation(end_index=11007, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE_nctEWDPmhTDUAU-6YES-fxZyrmzEonHrfzP8K09Nis-M_yQpU66BFAcEdylLhMWmWB-KGMEUyX0PSQjhknYiMuqsESuIiDt_0YenqvMMAF7oPVDv2EFRZ3njWRrAelt1u8glZQBaIiRU-YPYqX-iTrgwJB6mmOMTT00g3MlYtDFPyd0mFfO_XFRXD412jSyj2yVzSJqDCkvOskkwYg==', start_index=10993)
Annotation(end_index=11007, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEguVRXj8zyWaSdkD-nivZo2cbDAqqDKdlR8pHc9JIlArFzRtlPH40nX3TxcLRog6z5LAsBj9DJOnsc_n2gBWx0fUSCXiPtT1FvC-QTneoCXMSZLQijYGRDhqQ0f7_aGIvK810TCa-iNg==', start_index=10993)
Annotation(end_index=11535, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrCKTuMGeTxK4EyzTmdCDxUMCLOHkopc887h9Lf7ZqGsQLdEyuhTr4elW5v_omArZF8gAal9j7YUBp0k2mc2j9J7zovsqpHXX3oOQzVMr0SDrCWUrOduAMCMeOnAzr1gB7odA8I9wWIR7YZkiJYwv44pM=', start_index=11519)
Annotation(end_index=11535, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3hRWWpHw4ojErYVP2G2CRG-1DtUdoWulTQRBu_ArxAiF8ErtxGAuh5zdzACVuD33XCN910RaM-4PXtcc3pViVtLkJwEwHohM6OTAYP8LF9amnwjgdO1esSf48NY_uQCfYQvvbAFai0PL83nXLiDwx-S8QNQHBun0ABgjPu-dTVL7yQMELQIWHErsO2w0-u4WA-4UUmKwdBduxwh6mU0wApQ9gdxlL_mD836JgUk1N5owrOxjbpwhh', start_index=11519)
Annotation(end_index=11535, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGm8aA9NLNFRsJZzOrq5niehoOsFg0r31W428o8gxshqdrl1lfnrg4ogE-dsbuVDXhIrO6XU-w19LDF3jlMd0bUupNKFkrNCMTc6fXIkz5YSfWL7yeHkv6ti0Sl_ZoET-B6oe0SxZ4UHxf5HA63gduL_VnN_Kej1X1FXRxjkt4a_nvbwZg0VuysJoETcvn-ktyi-VpIxImyH_Ze', start_index=11519)
Annotation(end_index=12062, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGSSQZGoMxnYDLHIh6UMFsmFX_dU5yZ9O_nu05ofuAo33jG4F1Jb32i1kEJBPUMVbgIh4cj7rU1wdaTa_0ItHG5YG1YHfp7CfzmAJDc82qwu_4zOf_QPBYNQB-d2NgQ4I4p2DsGzg697NmFsws', start_index=12045)
Annotation(end_index=12062, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLf6_HgcgU8wsfRwdIs0lu10QjNvfWoLvP-xGmC6R1CM0NU83-RzUoWz9WjAnqi-Yb1aQJ51D-EIrtWpzgD6HGSVmRrmd3DeXOSUJwb7jd_vg7TRZfrZFh92GfmA4VIsqnvFKHSp4odA==', start_index=12045)
Annotation(end_index=12062, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGm8aA9NLNFRsJZzOrq5niehoOsFg0r31W428o8gxshqdrl1lfnrg4ogE-dsbuVDXhIrO6XU-w19LDF3jlMd0bUupNKFkrNCMTc6fXIkz5YSfWL7yeHkv6ti0Sl_ZoET-B6oe0SxZ4UHxf5HA63gduL_VnN_Kej1X1FXRxjkt4a_nvbwZg0VuysJoETcvn-ktyi-VpIxImyH_Ze', start_index=12045)
Annotation(end_index=12249, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLf6_HgcgU8wsfRwdIs0lu10QjNvfWoLvP-xGmC6R1CM0NU83-RzUoWz9WjAnqi-Yb1aQJ51D-EIrtWpzgD6HGSVmRrmd3DeXOSUJwb7jd_vg7TRZfrZFh92GfmA4VIsqnvFKHSp4odA==', start_index=12235)
Annotation(end_index=12249, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrCKTuMGeTxK4EyzTmdCDxUMCLOHkopc887h9Lf7ZqGsQLdEyuhTr4elW5v_omArZF8gAal9j7YUBp0k2mc2j9J7zovsqpHXX3oOQzVMr0SDrCWUrOduAMCMeOnAzr1gB7odA8I9wWIR7YZkiJYwv44pM=', start_index=12235)
Annotation(end_index=12394, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3hRWWpHw4ojErYVP2G2CRG-1DtUdoWulTQRBu_ArxAiF8ErtxGAuh5zdzACVuD33XCN910RaM-4PXtcc3pViVtLkJwEwHohM6OTAYP8LF9amnwjgdO1esSf48NY_uQCfYQvvbAFai0PL83nXLiDwx-S8QNQHBun0ABgjPu-dTVL7yQMELQIWHErsO2w0-u4WA-4UUmKwdBduxwh6mU0wApQ9gdxlL_mD836JgUk1N5owrOxjbpwhh', start_index=12385)
Annotation(end_index=12663, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEitAaYyMunly4wNI9qwTr0Ln2gJIB09WaKoqzkpKihaQP3HxIZ9QDcAPQv8R-i6adn3A9Q01XDlGB-uOtOs3Xq5Nel5iqDiQ_yAiEmCouFiy76YN-hJB92LqcYkCJrFMcITVj8L9sb3jP8ssgmtdYEipJ0iMTW6k5dpI7kq7Rbzt8RbapHwg==', start_index=12645)
Annotation(end_index=12663, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG54mFjZ_VpNgIrwQ6y5IZaem-Epb7W_O2Upv8vfXijuyvYFeI4krw1BRYOUfQLeCpnKkxJcQMKk1NBILtdJFIXCq1ryVU6AZ4VGoqzUA49vR0umExQ0SWv-B2ejdPPPvaGFZW7s1tUshwVCRDfZ4OeV83S_kd761NgJ6oDoJ_ROCeW7Dz8LKikW8mzINw00btkZ530ukxGB8mDUs1wSUU0VRc=', start_index=12645)
Annotation(end_index=12663, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEOrkXMbY5O_eVjHnheEtqkQZACLdq57XfJL8Eyq9HUuYyly_W9zNCGj-ygTq7QqJWmCTboUaic9eXZ7qpWJi5cItes5ZZD1ufs4asNm9lsEghhkZ_TqSb5HEo', start_index=12645)
Annotation(end_index=12826, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEOrkXMbY5O_eVjHnheEtqkQZACLdq57XfJL8Eyq9HUuYyly_W9zNCGj-ygTq7QqJWmCTboUaic9eXZ7qpWJi5cItes5ZZD1ufs4asNm9lsEghhkZ_TqSb5HEo', start_index=12816)
Annotation(end_index=13259, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEitAaYyMunly4wNI9qwTr0Ln2gJIB09WaKoqzkpKihaQP3HxIZ9QDcAPQv8R-i6adn3A9Q01XDlGB-uOtOs3Xq5Nel5iqDiQ_yAiEmCouFiy76YN-hJB92LqcYkCJrFMcITVj8L9sb3jP8ssgmtdYEipJ0iMTW6k5dpI7kq7Rbzt8RbapHwg==', start_index=13241)
Annotation(end_index=13259, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEOrkXMbY5O_eVjHnheEtqkQZACLdq57XfJL8Eyq9HUuYyly_W9zNCGj-ygTq7QqJWmCTboUaic9eXZ7qpWJi5cItes5ZZD1ufs4asNm9lsEghhkZ_TqSb5HEo', start_index=13241)
Annotation(end_index=13259, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxHczdCvGMS4KG4Z4PKgKIy6ttKsS0ITeJMD6YIvcvbaDa3mxLj1jXRoIaT-2XKqdrm5xeYXMgU6iFaz14O9juozuNW0PuyLgvZaRhe6Jc4LyFDI00YgxGHbINji6vzqwo-RSOCjv1u2nXdWcyd617meYXRVILJRJi14jxiWumq5DjI5I6ZE8RUymth4aYYQBVIpE4Y6HDbZA3Fg==', start_index=13241)
Annotation(end_index=13462, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2mEU6SQ5gts6nSB0jSeZJUSoM1LoVjlcWFtFNvH812gj66FzeZSap53pGvwC2DvexAJxVCjbawJgl38nGLdDR5B9N1VXBBnyowyXH0jiwUYxsB5Qq6wgC-tfEbbA-EwJm9GjcHE5VabDD7xX9M-LlNlXA6a6rHfi3zeo=', start_index=13440)
Annotation(end_index=13462, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE6ei4fuxF-f5taH1C8NIhDLNMj7q11yBOUx5YeJHQqBGAUYJBkTymNHuMKFb4gRToFftxCzcK33Fj-UF3y5Rn-d3wm_fVAQ8RFwhFuSXCRDWkKS-eiQw==', start_index=13440)
Annotation(end_index=13462, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFBzfNClCKYj1AN0iL4CgP7b-9y_YNZJ6VBwg7an5sFmVRIGnAoy7CCDPaV_QapIXH_83f8RLIuKd1CmnvW1WOFL-Ox3Nb7dGN5nwyTl-biQMtgoWvb5RNwTI38kBgpZSQ085MUN_4LTE4hkJq-lDO4qVcEfhSRMfwgQAQvp-MONibcIbALJbYcXn9rkSnnAo70lUC6PMvArg5F_NkZiNhi_IBAQj9iEaAlbtOgmUmCZX2hGEnQ3rnS082smZyfNdjkhKPAVt5iTTP3Kc7CjRulmK-bOCeCHThUxicq7tvW8Q=', start_index=13440)
Annotation(end_index=13462, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEXqHSHmtEIrpM0g-JV1pcqc-g5VoT8SBo9xqHNK79IfR4PNbRWgCd0G_nJu9e2oOYTHZ6CvUyap0lAuBqKp5xy4sbPPhHse4w-ns7JJxfxQP9k9zDZEi61SqcTdoZpwq6PmD3dq0O0TRap4nGiNVI98TOTRSFXRNVrw3zZTudScDfZO27Kcp-QLpQRHCOxUKj77fFfjiwoGqAPfblaXGl2Wizp-0ALiAP-z-cQecsNL1U-tN5NdHIgjfQ=', start_index=13440)
Annotation(end_index=13620, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1TsiPGUiWOHoXX_8H1Jy1io9HB-Gj_5dgNE2ea0Rg4sEG5S46_gxqcA5D-85ISqtR4A72KIe0DmKCxNNhycViVYtcNKxYqHIkyvAPJF4H8nBHYj_E_JDE59H2jOxmOBNDcxfkTuDiZGXZaQR7dg5cQNS7PnhvaGESKlTS9AcjAduwSDX9KtnXsshzD5PPsSx4ag==', start_index=13606)
Annotation(end_index=13620, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGM0CYDtwZDtAze3-h951pdwG2Lv9vlg1tt5DYfmL_6_xicFzeHI_PJwBcgcm1QPjkIi9nA6nxkWktf4k-QZhwBdWk1dc4Ch1A-peuNnJJ8D2q9sRP0SN23L1H49Gl-KIEV9uacz_JdxdyVV3qUwyMuPilf23w4nw==', start_index=13606)
Annotation(end_index=13817, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMghpaeeWDL3luRGP5LzYqLTHK4Ri7xbEAwk1y8mUnQ2Oet55Af-IIM1kkxf3Jk_fpYPJcrKbY9JCFZpFg3p0J5XsdN0Dk1VhRgA1uEwoMUKkkLpfiicxMePiPNPGUpO1KcC8IjUpuwfP4V81lVPJgXsfp4st7yEof_4pk', start_index=13807)
Annotation(end_index=14160, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrCKTuMGeTxK4EyzTmdCDxUMCLOHkopc887h9Lf7ZqGsQLdEyuhTr4elW5v_omArZF8gAal9j7YUBp0k2mc2j9J7zovsqpHXX3oOQzVMr0SDrCWUrOduAMCMeOnAzr1gB7odA8I9wWIR7YZkiJYwv44pM=', start_index=14150)
Annotation(end_index=14666, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1TsiPGUiWOHoXX_8H1Jy1io9HB-Gj_5dgNE2ea0Rg4sEG5S46_gxqcA5D-85ISqtR4A72KIe0DmKCxNNhycViVYtcNKxYqHIkyvAPJF4H8nBHYj_E_JDE59H2jOxmOBNDcxfkTuDiZGXZaQR7dg5cQNS7PnhvaGESKlTS9AcjAduwSDX9KtnXsshzD5PPsSx4ag==', start_index=14652)
Annotation(end_index=14666, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGM0CYDtwZDtAze3-h951pdwG2Lv9vlg1tt5DYfmL_6_xicFzeHI_PJwBcgcm1QPjkIi9nA6nxkWktf4k-QZhwBdWk1dc4Ch1A-peuNnJJ8D2q9sRP0SN23L1H49Gl-KIEV9uacz_JdxdyVV3qUwyMuPilf23w4nw==', start_index=14652)
Annotation(end_index=14919, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHO5x9TOuOINA3qdr4C5E6zeL5M9bsQ_26nFbbWsw4gTYLsd-06JFfYh4vUc8V76Muu2tBodu_rPqACHcNUDU2rOSdZ-g5fG71cSWtoB9EDtJuG9eBuig9zqcTI8rnpQGuoAK34uP9Z7iitmz2EDET6rUH-jN2Dtfrk74ja7hxmJSGDt8q3oW3CZes=', start_index=14909)
Annotation(end_index=15263, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmeU7k7XVsFxHKAhO1IkYiL2Cn-mgq2XMqgASjA9JLvawwCTO5AEPYsv8YWzDhvMmpgnEjDjaYDAz-oUvXYDktr3UDcneCmUWG6f9SXDLJ4ISQ0fLk8wvlheR8UPOSYpEWy7vTvyBZWt_bgGUepPcIaCtgz8c18vqCH7Hm-7Z2CVbOKu-3KnAbztxu_BRh15nFQ-Kr1ZSQDSg=', start_index=15241)
Annotation(end_index=15263, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSAs6WkgdGZ0DQlSlO73ikKCEi-zqh_BN5Cyp7khrWaYovUCv7K8UbY6UvKoz1T9ufB2vJB8xY39__UFY0hTXDEdt6D3cauVu4zfNPjUmfZqCukSYCu05KoZXVoKFDOye5oVGuaLHNWfsKN4EOgvnmkUeGQmR9BwZczvzuc6ubhttld4gQLZ-_WQppgIBIWzLFRCgduALJ34TenRR0', start_index=15241)
Annotation(end_index=15263, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxSNvjXNujFyNFPfl3T2Sl5aBDTP3qlafUIVw5dvA2w6mkmm6tdwlL8j40tFC6DguCAHInxVUcgNbThIml3meGNTu8C1saUTzm_Un-I26-ucqHnwnGbPJsOoSOdLwv-NasJhG1zGOhqSaLumkXsePhl1hKT44s0FRbQ1b8RS7PUPt_vM_g', start_index=15241)
Annotation(end_index=15263, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyQ3VzKajbxJ5hVBpUWqen-YL6wtmsP-voKvKNLWNn6eIWBLOQAdzOi56J0s0kK7yrmIxYOXTPSHeZfdTGWspa25m4r218syCUADnZhi1qP6jpVGX4Ihb-Eo-TIUnKgY8KroxIrlxsSKoliPwldv0tzQOt6favOpHE8GlYZCrKUulcczM=', start_index=15241)
Annotation(end_index=15402, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHrvMPEh6sottAf4VbGODkqLWqrlTZmOzyf8BJCiOIu6ooRdfwZcCMvkb_vyZ-KUaXaERbSkFyyzeXNIdMrFvIBXz1XZ0cl5UelvYACaexlNX_WN4ro8HGO9Q39y9AMcmoZToqi35T7LOo3F-VIw1JW4rxuXArq8KHh1RlkBt-JbmM2s8hwq0D0D5TEOood2JNa4aW7jAJu363dCEJUCN2n8HyRb9_oN4ID0Dx-__BpDMS6kiEFIyLHuyptZyg0HOCfoRg=', start_index=15392)
Annotation(end_index=15606, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmeU7k7XVsFxHKAhO1IkYiL2Cn-mgq2XMqgASjA9JLvawwCTO5AEPYsv8YWzDhvMmpgnEjDjaYDAz-oUvXYDktr3UDcneCmUWG6f9SXDLJ4ISQ0fLk8wvlheR8UPOSYpEWy7vTvyBZWt_bgGUepPcIaCtgz8c18vqCH7Hm-7Z2CVbOKu-3KnAbztxu_BRh15nFQ-Kr1ZSQDSg=', start_index=15596)
Annotation(end_index=15901, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF1I2MeHYmgW0b0D3DjBIrnZFCjmAcutbuLOTaGg0b4EKqBqqW0WKCof61KV5O4maJM_PbpQPsp0pTPZ1w3xQhMCehWV0ENyx2a5COvP3Mqm_y_HS_88S96h7n4uhOoxpBvakbcyiNqkfuLUDrLDFHcyXK3JdBBZzaJcBJzL9mDr188IsVqXenc3bZ9qwyrRxFiYrFICTgiGA9eiQbd', start_index=15887)
Annotation(end_index=15901, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGe0ebN17i0jfJJfJYuOXs-egrAAfAfFlU9JpkxluEzsFOZmlCyBvNRtBNOnJM0KDR0ONQmdb9G5Ki1Aeo2AkLHrcKnhoOpju94kfX-KHen4sYYIyGJiZzyttcnolTjya_pKRoRLQFhyLRp3kATPEfXtgFi9jc-8w==', start_index=15887)
Annotation(end_index=16172, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEc0lOIItdXZTX0YBdxMxYqdPwv6W4S5ntp3__lLOshLKb2V0NtuCjxmAwFM-JerdX7UVFV5UY7NaWfy-GwfswOigIF9yjZNYDvmYSW_QM-0rTOp-IgNzKJD0hSwWfFlUs-gQcqS9J5BzHE8a1YXbPb61whBxjHHseVQCxH5g==', start_index=16154)
Annotation(end_index=16172, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFfIsBPz0BTdVTyVi1iWmM8HxrZwMSWmNAnRxbl2tv6gzBxOJuvyUKilN-peeOXxn_Rc4YvckskSOaoZWS3sGFLE5qYOHKcNbZZFUpRedV78VIAqsrN1elqVT7iNQa2FIOH2bu9m3gG_oahTJt53boPIsPkvA3d_mm9WWYhiXV78NW6RA==', start_index=16154)
Annotation(end_index=16172, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYKaZxTlWeKgwKt9y2RBuvsby7rKs53wo4-4gUh2C4IFFj1QS0r4_msM22e21mhFv5eq16lKNqwmXsUQkR4Xpb7ZiaCc5hvCG8LugJztBZ5LZq-m53Q5iCZRmtCMlcjbia_UPEZ5mfQn7Qdz0QcyqFsIT6JNwO-3YRt7BhsZ2fwr_RGzwm0L2dp9za66B1RUKer6L52MAEc9c1KvGfn8U3CtllAXldK-x1HE-ODH08K9Zu5iHR', start_index=16154)
Annotation(end_index=16534, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzPlbRIFyMKMZwSHnfcQacxY0SGCzHNZ3RUEnnA0IuRFT64DYpbEdG07fBDe2FLpA-Ggcbx1ClXxU0zjnlIA9eDCByJgPJOF7sJUvvtxs7RGchL5q4WLsxLBrz-vU7IHlgr4kK7wGQF3bm7e2mRTRL_ji1qgMSZHBE6HMKLOGHGRGIBhHlDhH12YnjmTUVsGMnpwYEYJG0V4-BtB8Rne_u15A=', start_index=16517)
Annotation(end_index=16534, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcAyAMxsF7LKYtJ_z66bNbNybhONlbun_WRAp6tT032XbJ40wAxyKLFgkrSqhThVdJwmhbGFFc76KAjmulbK20nZ9oV4yNUlVTo2F_tTV_k57RBxb7sDvc', start_index=16517)
Annotation(end_index=16534, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9XvAYrbdjFIrzouaq_wUgA-wCvFylLMpIATqaoF7MpfTYe6m-JN7Va3N4NDIwOpXxIdPRS_eocvUpUqjO-FNh9PbCvgH58bhc8Y4v_7g0adev2bP13Qm_AC_8RV3fgfZffia75sooWTP5db8=', start_index=16517)
Annotation(end_index=16745, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrxu9y4YE5WwCJLOP9uKQaMoA9H81S3LRW-vXIPM1sIUxfydvURmz9KXw2SYrrPUsP3LQeiCUY9-5TwsApnJcuF9-Qy4YOr4Q4OyveaL6neR2zmQIa3hmQSzQWDesyLmEMY9GL_bAYERx5ETotAI9J69gGzfflfng=', start_index=16732)
Annotation(end_index=16745, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRQ89BAMOv-fYw393Jk-3Ngm6fKIfjjm91fwF6ASslGNT0CZRTBCVm3NNXba4CUXIqJ1b4RQ5FwOrqnczT2l5oKlAOo1IrFKSWlM7g7G-ZUANh9Olco_nKVWNShF-Bs-YcCfMVU1wyy4DVwreqYSNnpNzu_w==', start_index=16732)
Annotation(end_index=16982, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrxu9y4YE5WwCJLOP9uKQaMoA9H81S3LRW-vXIPM1sIUxfydvURmz9KXw2SYrrPUsP3LQeiCUY9-5TwsApnJcuF9-Qy4YOr4Q4OyveaL6neR2zmQIa3hmQSzQWDesyLmEMY9GL_bAYERx5ETotAI9J69gGzfflfng=', start_index=16968)
Annotation(end_index=16982, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHqmD5drNkqewjiWLkrrni-7gL9F5Pgqsr8cNhfz0qp8DoV7pK_g1PNM3ImG8PGpM-6mtftbYfMiI1W1mZxQAb86V4IHD9_F164OiEGZPmPMiJxs-RM_7ldkNtE_hyDv3phzOv9Ty6h-x1SV_2X1WlnkiRun-5TjAMPVe6lbPPtPciUVJGfTnA_B9NSrhFOcp8=', start_index=16968)
Annotation(end_index=17364, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFO1vI85mxdti1Hb6MbyVF0MdFICBgmDaRXMWRsgy0qZcg9vy3y908MVqjcIXHNWcSN-_PD5PCtMymCl0mRq_dWV8lyXxsHkYUnn2OZrWFsH-lcR0wM-dtGvzeMWEcUfYIRagTkGi6L60gJ8M=', start_index=17351)
Annotation(end_index=17364, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3hRWWpHw4ojErYVP2G2CRG-1DtUdoWulTQRBu_ArxAiF8ErtxGAuh5zdzACVuD33XCN910RaM-4PXtcc3pViVtLkJwEwHohM6OTAYP8LF9amnwjgdO1esSf48NY_uQCfYQvvbAFai0PL83nXLiDwx-S8QNQHBun0ABgjPu-dTVL7yQMELQIWHErsO2w0-u4WA-4UUmKwdBduxwh6mU0wApQ9gdxlL_mD836JgUk1N5owrOxjbpwhh', start_index=17351)
Annotation(end_index=17580, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrCKTuMGeTxK4EyzTmdCDxUMCLOHkopc887h9Lf7ZqGsQLdEyuhTr4elW5v_omArZF8gAal9j7YUBp0k2mc2j9J7zovsqpHXX3oOQzVMr0SDrCWUrOduAMCMeOnAzr1gB7odA8I9wWIR7YZkiJYwv44pM=', start_index=17567)
Annotation(end_index=17580, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3hRWWpHw4ojErYVP2G2CRG-1DtUdoWulTQRBu_ArxAiF8ErtxGAuh5zdzACVuD33XCN910RaM-4PXtcc3pViVtLkJwEwHohM6OTAYP8LF9amnwjgdO1esSf48NY_uQCfYQvvbAFai0PL83nXLiDwx-S8QNQHBun0ABgjPu-dTVL7yQMELQIWHErsO2w0-u4WA-4UUmKwdBduxwh6mU0wApQ9gdxlL_mD836JgUk1N5owrOxjbpwhh', start_index=17567)
Annotation(end_index=18401, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2mEU6SQ5gts6nSB0jSeZJUSoM1LoVjlcWFtFNvH812gj66FzeZSap53pGvwC2DvexAJxVCjbawJgl38nGLdDR5B9N1VXBBnyowyXH0jiwUYxsB5Qq6wgC-tfEbbA-EwJm9GjcHE5VabDD7xX9M-LlNlXA6a6rHfi3zeo=', start_index=18387)
Annotation(end_index=18401, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLf6_HgcgU8wsfRwdIs0lu10QjNvfWoLvP-xGmC6R1CM0NU83-RzUoWz9WjAnqi-Yb1aQJ51D-EIrtWpzgD6HGSVmRrmd3DeXOSUJwb7jd_vg7TRZfrZFh92GfmA4VIsqnvFKHSp4odA==', start_index=18387)
Annotation(end_index=18947, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEc0lOIItdXZTX0YBdxMxYqdPwv6W4S5ntp3__lLOshLKb2V0NtuCjxmAwFM-JerdX7UVFV5UY7NaWfy-GwfswOigIF9yjZNYDvmYSW_QM-0rTOp-IgNzKJD0hSwWfFlUs-gQcqS9J5BzHE8a1YXbPb61whBxjHHseVQCxH5g==', start_index=18929)
Annotation(end_index=18947, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSAs6WkgdGZ0DQlSlO73ikKCEi-zqh_BN5Cyp7khrWaYovUCv7K8UbY6UvKoz1T9ufB2vJB8xY39__UFY0hTXDEdt6D3cauVu4zfNPjUmfZqCukSYCu05KoZXVoKFDOye5oVGuaLHNWfsKN4EOgvnmkUeGQmR9BwZczvzuc6ubhttld4gQLZ-_WQppgIBIWzLFRCgduALJ34TenRR0', start_index=18929)
Annotation(end_index=18947, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoSeTq-RrRzfLPq4QjB16gxaGluXF7v-YNSCp3yypEel7xP0m9QzIxytIUnQlsGhLPDWO4eNdYHRPrS4aEwS2m70gQt088IzMUpxXw9e06WHdkviZ6vWrL5vaZMMiVRqG2PSMj2qabHOBEVbzoArzzwCL0RSlLGoeTaKxijJ73sth7aXOh76hrbvVMGY6Azyy2mpXeTvqiOjYDNrpwx3o=', start_index=18929)
Annotation(end_index=21273, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzPlbRIFyMKMZwSHnfcQacxY0SGCzHNZ3RUEnnA0IuRFT64DYpbEdG07fBDe2FLpA-Ggcbx1ClXxU0zjnlIA9eDCByJgPJOF7sJUvvtxs7RGchL5q4WLsxLBrz-vU7IHlgr4kK7wGQF3bm7e2mRTRL_ji1qgMSZHBE6HMKLOGHGRGIBhHlDhH12YnjmTUVsGMnpwYEYJG0V4-BtB8Rne_u15A=', start_index=21260)
Annotation(end_index=21273, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9XvAYrbdjFIrzouaq_wUgA-wCvFylLMpIATqaoF7MpfTYe6m-JN7Va3N4NDIwOpXxIdPRS_eocvUpUqjO-FNh9PbCvgH58bhc8Y4v_7g0adev2bP13Qm_AC_8RV3fgfZffia75sooWTP5db8=', start_index=21260)
Annotation(end_index=21355, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcAyAMxsF7LKYtJ_z66bNbNybhONlbun_WRAp6tT032XbJ40wAxyKLFgkrSqhThVdJwmhbGFFc76KAjmulbK20nZ9oV4yNUlVTo2F_tTV_k57RBxb7sDvc', start_index=21345)
Annotation(end_index=21459, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcAyAMxsF7LKYtJ_z66bNbNybhONlbun_WRAp6tT032XbJ40wAxyKLFgkrSqhThVdJwmhbGFFc76KAjmulbK20nZ9oV4yNUlVTo2F_tTV_k57RBxb7sDvc', start_index=21449)
Annotation(end_index=21563, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2mEU6SQ5gts6nSB0jSeZJUSoM1LoVjlcWFtFNvH812gj66FzeZSap53pGvwC2DvexAJxVCjbawJgl38nGLdDR5B9N1VXBBnyowyXH0jiwUYxsB5Qq6wgC-tfEbbA-EwJm9GjcHE5VabDD7xX9M-LlNlXA6a6rHfi3zeo=', start_index=21553)
Annotation(end_index=22214, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLf6_HgcgU8wsfRwdIs0lu10QjNvfWoLvP-xGmC6R1CM0NU83-RzUoWz9WjAnqi-Yb1aQJ51D-EIrtWpzgD6HGSVmRrmd3DeXOSUJwb7jd_vg7TRZfrZFh92GfmA4VIsqnvFKHSp4odA==', start_index=22201)
Annotation(end_index=22214, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGm8aA9NLNFRsJZzOrq5niehoOsFg0r31W428o8gxshqdrl1lfnrg4ogE-dsbuVDXhIrO6XU-w19LDF3jlMd0bUupNKFkrNCMTc6fXIkz5YSfWL7yeHkv6ti0Sl_ZoET-B6oe0SxZ4UHxf5HA63gduL_VnN_Kej1X1FXRxjkt4a_nvbwZg0VuysJoETcvn-ktyi-VpIxImyH_Ze', start_index=22201)
Annotation(end_index=22786, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3hRWWpHw4ojErYVP2G2CRG-1DtUdoWulTQRBu_ArxAiF8ErtxGAuh5zdzACVuD33XCN910RaM-4PXtcc3pViVtLkJwEwHohM6OTAYP8LF9amnwjgdO1esSf48NY_uQCfYQvvbAFai0PL83nXLiDwx-S8QNQHBun0ABgjPu-dTVL7yQMELQIWHErsO2w0-u4WA-4UUmKwdBduxwh6mU0wApQ9gdxlL_mD836JgUk1N5owrOxjbpwhh', start_index=22777)
Annotation(end_index=23401, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG54mFjZ_VpNgIrwQ6y5IZaem-Epb7W_O2Upv8vfXijuyvYFeI4krw1BRYOUfQLeCpnKkxJcQMKk1NBILtdJFIXCq1ryVU6AZ4VGoqzUA49vR0umExQ0SWv-B2ejdPPPvaGFZW7s1tUshwVCRDfZ4OeV83S_kd761NgJ6oDoJ_ROCeW7Dz8LKikW8mzINw00btkZ530ukxGB8mDUs1wSUU0VRc=', start_index=23383)
Annotation(end_index=23401, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEOrkXMbY5O_eVjHnheEtqkQZACLdq57XfJL8Eyq9HUuYyly_W9zNCGj-ygTq7QqJWmCTboUaic9eXZ7qpWJi5cItes5ZZD1ufs4asNm9lsEghhkZ_TqSb5HEo', start_index=23383)
Annotation(end_index=23401, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGxHczdCvGMS4KG4Z4PKgKIy6ttKsS0ITeJMD6YIvcvbaDa3mxLj1jXRoIaT-2XKqdrm5xeYXMgU6iFaz14O9juozuNW0PuyLgvZaRhe6Jc4LyFDI00YgxGHbINji6vzqwo-RSOCjv1u2nXdWcyd617meYXRVILJRJi14jxiWumq5DjI5I6ZE8RUymth4aYYQBVIpE4Y6HDbZA3Fg==', start_index=23383)
Annotation(end_index=23940, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmeU7k7XVsFxHKAhO1IkYiL2Cn-mgq2XMqgASjA9JLvawwCTO5AEPYsv8YWzDhvMmpgnEjDjaYDAz-oUvXYDktr3UDcneCmUWG6f9SXDLJ4ISQ0fLk8wvlheR8UPOSYpEWy7vTvyBZWt_bgGUepPcIaCtgz8c18vqCH7Hm-7Z2CVbOKu-3KnAbztxu_BRh15nFQ-Kr1ZSQDSg=', start_index=23922)
Annotation(end_index=23940, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSAs6WkgdGZ0DQlSlO73ikKCEi-zqh_BN5Cyp7khrWaYovUCv7K8UbY6UvKoz1T9ufB2vJB8xY39__UFY0hTXDEdt6D3cauVu4zfNPjUmfZqCukSYCu05KoZXVoKFDOye5oVGuaLHNWfsKN4EOgvnmkUeGQmR9BwZczvzuc6ubhttld4gQLZ-_WQppgIBIWzLFRCgduALJ34TenRR0', start_index=23922)
Annotation(end_index=23940, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoSeTq-RrRzfLPq4QjB16gxaGluXF7v-YNSCp3yypEel7xP0m9QzIxytIUnQlsGhLPDWO4eNdYHRPrS4aEwS2m70gQt088IzMUpxXw9e06WHdkviZ6vWrL5vaZMMiVRqG2PSMj2qabHOBEVbzoArzzwCL0RSlLGoeTaKxijJ73sth7aXOh76hrbvVMGY6Azyy2mpXeTvqiOjYDNrpwx3o=', start_index=23922)
Annotation(end_index=24585, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGTYfN_FJalcCqgYkx-nnGSarr085o_TrbIcESbMUmwwaHRvhhu__fsNxsUVtvkHWgGTUqf3eU8Ccg7OWC1riCmd5Ishr1QX6dP9c1exuM5MruthbJb-YyNTdPWBWiyKljDx0l4L5mC4KTsAZy0mpDtYOa18nkSVpeq7tk7Xjk4TrD8u-S1Qglflklj', start_index=24575)
Annotation(end_index=24799, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDGgSuTdZzinksy6rdBXSCrwvuEKsp5LRKDMdnSwEjxBRG9sqFSANHWo_1zpJPZNN2axDEHUzn-PWrvpKZjTXmKNFJylSH2hiRYVrPmG5Y8fzUXhEtoBrXCIfQygwk8dWVzX7jOhLNArrMr50=', start_index=24789)
Annotation(end_index=25227, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEitAaYyMunly4wNI9qwTr0Ln2gJIB09WaKoqzkpKihaQP3HxIZ9QDcAPQv8R-i6adn3A9Q01XDlGB-uOtOs3Xq5Nel5iqDiQ_yAiEmCouFiy76YN-hJB92LqcYkCJrFMcITVj8L9sb3jP8ssgmtdYEipJ0iMTW6k5dpI7kq7Rbzt8RbapHwg==', start_index=25214)
Annotation(end_index=25227, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEvRyv9fJZbF1ksQBGe-JJVoG77DrWB2-OIZRFRAdRxlMSdNSq-3EQNWkg28vZpag4BkJlkfp79huT4iu02jKAPNypf4S7lriDHx4tVvGafuqF61Fifli3Uczu-wZZN9dzMRTBs4I_UjGHSx_uP', start_index=25214)

## Sources
