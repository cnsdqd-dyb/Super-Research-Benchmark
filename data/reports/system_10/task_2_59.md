# Deep Research Report: perplexity/sonar-deep-research
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** b24d1f25 | **Time:** 121.87s | **Cost:** $1.28686
--------------------------------------------------------------------------------

# Programmable Money and Policy Control: Examining the Risk Profile of Smart Contract-Based CBDC Policy Tools

Central bank digital currencies incorporating smart contract technology present a fundamental tension between enhanced monetary policy transmission and the risk of systemic operational failures amplifying unintended policy consequences. The deployment of programmable money through smart contracts enables central banks to exercise granular control over monetary aggregates through mechanisms including holding limits, tiered remuneration, expiring money, and conditional spending restrictions. However, these same technical capabilities introduce unprecedented vulnerabilities rooted in code complexity, Byzantine consensus challenges, and the immutability of distributed ledger systems that make "policy accidents" not merely probable but potentially catastrophic in scale and scope.

## Smart Contract Policy Mechanisms and Money Supply Architecture

### The Integration of Policy Tools Through Programmable Logic

Smart contracts represent software protocols that automatically execute predetermined conditions encoded within blockchain or distributed ledger technology systems[1][2]. Within the CBDC framework, these contracts serve as the operational mechanism through which monetary policy directives translate into technical constraints on currency movement, storage, and redemption. The most prominent policy tools implemented through smart contracts include wallet size limits, which establish maximum balances individuals or institutions can hold in CBDC form; tiered remuneration systems, which impose variable interest rates that decrease as holdings increase; expiring money mechanisms that reduce the nominal value of currency after a specified period; and conditional payment restrictions that limit spending to specific categories of goods, services, or time windows[1][3][4].

The architectural elegance of these programmable features lies in their capacity for real-time implementation without requiring traditional regulatory intermediation. When a central bank wishes to execute monetary policy through CBDC remuneration, it need not rely on commercial banks to propagate rate changes through deposit rates and lending decisions. Instead, the central bank can adjust the smart contract parameters governing interest accrual, and these changes propagate instantly across the entire distributed ledger system[12][17][28]. Similarly, if a central bank determines that aggregate CBDC holdings threaten financial stability by triggering deposit disintermediation, it can activate holding limits that automatically enforce maximum balances through what researchers term "waterfall mechanisms"—where excess CBDC above the threshold automatically transfers to bank deposits or alternative holdings[3][17][28][41].

This represents a qualitative shift in monetary policy transmission mechanisms. In traditional systems, policy implementation operates through indirect channels where the central bank sets a policy rate, commercial banks adjust their prime lending rate, and market participants gradually adjust their behavior in response to changed incentive structures. The transmission process unfolds across weeks or months, with significant lags and incomplete pass-through. Smart contract-based CBDC policy tools collapse these transmission lags into milliseconds, enabling what theorists describe as near-instantaneous monetary aggregation control[1][28].

### Risk Isolation Through Technical Design Parameters

The apparent solution to financial stability concerns involves implementing technical design parameters explicitly intended to isolate systemic risks. These mechanisms operate at multiple architectural levels. At the account level, holding limits prevent any single entity from accumulating excessive CBDC that might trigger rapid conversion into alternative assets during stress periods. At the system level, aggregate caps limit the total quantity of CBDC in circulation, with historical precedent suggesting that optimal CBDC stock stabilizes around 40 percent of annual GDP in steady state conditions, though this figure remains empirically uncertain[15][38][56].

More sophisticated risk isolation approaches employ tiered architectures where remuneration rates decline as holdings increase, creating economic incentives for distribution rather than concentration[31][34][56]. A holder maintaining minimal CBDC balances receives the policy rate or a modest premium, while someone attempting to maintain large stockpiles faces negative returns on amounts exceeding specified thresholds. Theoretically, this creates what economists term a "U-shaped" relationship between bank fragility and CBDC remuneration, where both excessive CBDC attractiveness (from high interest rates) and excessive unattractiveness (from negative rates) create instability, with optimal stability occurring at intermediate remuneration levels[34].

The contingent convertibility mechanism represents perhaps the most technically sophisticated risk isolation approach. Under this design, the central bank unconditionally accepts only eligible assets—typically government bonds—in exchange for CBDC issuance to the general public[15][38]. Bank deposits convert into CBDC only on a discretionary basis during normal times, remaining legally nonconvertible during crisis periods. This architecture theoretically prevents "runs into CBDC" because the central bank maintains sovereign control over the quantity of new CBDC issued against bank deposits, while remaining obligated to issue unlimited quantities against government bonds held as reserve collateral[15][38].

These policy tools collectively aspire to achieve what financial regulation theorists call "policy insulation"—the capacity to implement monetary policy directives through technical enforcement mechanisms that prevent circumvention while containing second-order effects. A central bank can reduce the real money supply through negative CBDC remuneration without forcing holders into physical cash because the smart contract automatically reduces nominal balances. It can prevent destabilizing bank runs by capping individual holdings at levels sufficient for payments but insufficient for wealth storage. It can eliminate the zero lower bound constraint that plagued monetary policy during recent crises by imposing negative rates on digital currency that cannot be avoided through cash hoarding[32].

## The Financial Stability Architecture and Its Assumptions

### Deposit Disintermediation and the Credit Channel

Despite sophisticated design mechanisms, a persistent tension emerges between CBDC's safety—stemming from its status as a direct central bank liability—and the competitive threat this safety poses to commercial bank deposits. When depositors face a choice between holding a commercial bank deposit (subject to default risk, liquidity risk, and counterparty risk) and a CBDC wallet (subject only to central bank insolvency risk), rational decision-making predicts substantial substitution away from deposits, particularly during periods of financial stress[7][10][12][34][60].

Empirical modeling suggests that this substitution operates with asymmetric intensity. One dollar of CBDC introduction crowds out approximately eighty cents of bank deposits at the margin, but only one-fourth of the resulting deposit loss translates into reduced lending because banks compensate through wholesale funding[33][60]. However, this compensatory funding comes at substantially higher cost than deposit funding, as wholesale funding rates exceed the federal funds rate and carry greater sensitivity to interest rate changes[33]. The result is that CBDC-induced disintermediation forces banks to increase lending rates to compensate for higher funding costs, potentially reducing credit availability by between one and five percent during stress periods[7].

The credit channel disruption becomes more severe for small banks operating in concentrated markets, where incumbent advantages are weaker and CBDC competition eliminates pricing power. Small banks experience lending reductions three times larger than those faced by large banks when CBDC holdings reach similar levels, creating differential systemic effects where CBDC adoption reduces regional credit provision in areas heavily dependent on small bank lending[33][60]. Moreover, the shift from deposit funding toward wholesale funding increases banks' exposure to interest rate risk, as deposits serve as a natural hedge against interest rate changes while wholesale funding rates move directly with policy rates[33].

### Run Risk Dynamics and Crisis Amplification

The theoretical literature on CBDC-induced bank runs identifies a cascade mechanism where initial stress triggers CBDC accumulation, which generates the dynamic feedback that converts modest disruptions into systemic crises[7][10][31]. In the classical Diamond-Dybvig framework, bank runs represent self-fulfilling prophecies where depositors withdraw funds not because bank solvency has fundamentally deteriorated but because they believe others will withdraw, triggering forced asset sales that do impair solvency[7][31].

CBDCs introduce a qualitatively new vulnerability into this framework by eliminating switching costs. During the 2012 Greek bank crisis, when depositors fled toward perceived safety, the process unfolded over weeks as customers lined up at bank branches and ATMs to withdraw cash, with the slow mechanics of physical currency limiting run velocity[7]. With CBDC, that same deposit flight could complete in minutes or seconds, as wallets execute transfers instantaneously across blockchain networks[7][31]. The run accelerates not because underlying conditions deteriorated more severely but because technological friction disappeared.

Federal Reserve modeling suggests that in scenarios where CBDC demand reaches three trillion dollars—roughly nine percent of annual GDP in the United States—the aggregate impact remains manageable if excess bank reserves remain adequate[17]. However, if CBDC adoption continues growing and excess reserves decline, financial institutions would face reserve scarcity, potentially forcing central bank balance sheet expansion to prevent systemic stress[17][25]. More concerning, if CBDC adoption accelerates during a crisis when both liquidity and solvency concerns intensify, the speed and scale of deposit flight could exceed central bank capacity for emergency liquidity provision.

The research explicitly models scenarios where tiered remuneration and holding limits prove insufficient to prevent destabilizing runs[34]. When CBDC remuneration rises high enough to become genuinely attractive relative to bank deposits, holding limits may actually increase fragility by frustrating depositors who cannot accumulate adequate CBDC reserves for precautionary purposes, leading them to maintain fractionally larger unsecured wholesale funding positions to compensate[34]. Conversely, when CBDC remuneration remains negative or minimal, imposing holding limits alongside low rates can paradoxically increase run risk by making CBDC less useful for its intended payments function, driving users back toward bank deposits that offer superior service despite safety concerns[34].

## Programmable Money Logic and Systemic Operational Risk

### The Smart Contract Vulnerability Cascade

The transformation of monetary policy into executable smart contract code introduces an entirely new category of systemic risk that existing financial regulation frameworks explicitly do not address. Unlike traditional policy implementation where human judgment and institutional oversight remain embedded in the execution chain, smart contract-based CBDC policy operates through transparent, immutable code that executes automatically based on state variables and blockchain conditions[2][8][24].

The technical vulnerability landscape encompasses multiple layers of failure modes, each capable of propagating across the entire CBDC system simultaneously. At the code level, basic programming errors create catastrophic consequences because smart contracts cannot be modified after deployment without implementing hard forks that split the cryptocurrency into two incompatible versions—technically and politically untenable for a sovereign currency[2]. Historical examples demonstrate the magnitude of potential failures. In August 2021, the Poly Network experienced a $600 million cryptocurrency theft not through external hacking but through user exploitation of flaws in the smart contract code governing cross-chain operations, where the user detected logic errors enabling unauthorized fund transfers and could only be stopped through social pressure when the perpetrator realized the stolen funds could not be laundered[2][8][21].

In a separate incident on the Polygon network, $262 million in collateral locked permanently in a smart contract because the underlying logic contained a design flaw that made funds irretrievable—not a bug in the traditional sense but a logical error in how conditions for fund release were specified[2][8][21]. Because the smart contract was designed as immutable, no remediation proved possible without rendering all dependent transactions void.

These vulnerabilities cascade across the system through multiple amplification mechanisms. If a smart contract governing CBDC holding limits contains a logic error in how the maximum balance constraint propagates across linked accounts, the error could systematically miscalculate limits for millions of wallets simultaneously[24][29]. Unlike a traditional banking error affecting a specific set of accounts, the error in a smart contract affects every account simultaneously in an identical fashion, creating what financial regulators term "Systemic Operational Risk Events" or SOREs[2][8][21][24].

### Attack Surface Expansion Through Transparent Code

The transparency inherent to blockchain-based smart contracts—necessary for public trust and regulatory oversight—creates unprecedented attack surface expansion[2][8][21][24][29]. Because CBDC smart contracts must remain publicly visible to enable verification and audit, knowledgeable cryptanalysts and potential bad actors can inspect the code, compile it into comprehensible form, and identify vulnerabilities through forensic analysis[2][8].

A sophisticated state-level actor or coordinated criminal organization could theoretically copy the transparent CBDC smart contract code into a laboratory environment, reverse-engineer the underlying logic, and conduct extensive testing to identify exploit pathways[2]. Once vulnerabilities are discovered, coordinated attacks could be launched simultaneously across the network, potentially executing exploits that simultaneously freeze CBDC holdings (analogous to the Polygon incident), steal funds (analogous to the Poly Network hack), or split the currency into incompatible versions[2]. The magnitude of disruption would be orders of magnitude larger than historical cryptocurrency hacks because the target represents an entire nation's monetary system rather than a single private platform.

This attack surface differs fundamentally from traditional payment system vulnerabilities. Current wholesale settlement systems like Fedwire employ closed-source code controlled by the Federal Reserve, implement multi-layered authentication, and maintain sophisticated redundancy preventing single-point failures[24]. A successful cyberattack on Fedwire would cause severe disruption, but the damage scope remains limited because the system operators maintain classified knowledge of vulnerabilities and can implement patches before exploitation[24]. CBDC smart contracts cannot benefit from this security-through-obscurity because transparency requirements for public trust preclude the operational security practices that protect existing financial infrastructure[24][29].

The regulatory guidance on this vulnerability acknowledges the fundamental asymmetry: "Any programmable money scheme that relies on smart contracts not only creates economic difficulties but, more importantly, poses risks to national security"[2][8]. Current regulatory thinking offers only restrictive solutions—discouraging or banning programmable money architectures entirely until consequences become fully understood, rather than confidently deploying them with mitigation confidence[2][8].

## Design Trade-offs and Unintended Consequence Amplification

### The Programmable Spending Restriction Framework

Smart contract programmability enables monetary policy tools that lack historical precedent: the ability to restrict spending by specific individuals or groups based on behavioral criteria, social credit scores, political affiliation, or other dimensions encoded into the smart contract logic[1][4][19][20][22][30][59]. While central banks cite legitimate policy objectives for such restrictions—directing stimulus toward consumption rather than financial asset accumulation, preventing illicit financing, ensuring equitable distribution during emergencies—the technical mechanisms create capabilities for control that exceed any previous monetary system[1][4][19][20][22][59].

Expiring money represents the most directly analyzed programmable spending restriction. A central bank can program CBDC to lose its nominal value after a specified period, creating what economists term "carrying costs" that incentivize spending and prevent hoarding[22][59]. The theory, drawing on Silvio Gesell's early twentieth-century proposals, suggests that money losing value at a programmed rate would increase monetary velocity and aggregate demand precisely when stimulus is needed[22].

However, the implementation complexity generates numerous unintended consequences. If a holder receives a payment that pushes their CBDC balance above the pre-expiration threshold, should the newly received funds expire immediately or receive a fresh timer? If a fresh timer, sophisticated traders could exploit expiration mechanics by structuring transactions to repeatedly reset timers. If immediate expiration, senders face perverse incentives to split transactions into multiple smaller payments to maximize receiver utility[22][59]. The smart contract encoding the expiration logic must specify these edge cases, and any specification generates new attack surfaces or unintended behaviors.

More fundamentally, programmable spending restrictions for steering consumption toward specific categories—food and medicine but not luxury goods, for instance—require central banks to specify acceptable purchases within smart contracts[1][4][19][20][59]. This transforms the central bank from a monetary authority into a consumption arbitrator, with the technical infrastructure enabling enforcement at a speed and scale previously impossible[1][4][19][20][59]. A government could program CBDC wallets to prohibit transactions at merchants deemed politically disfavored, to impose dynamic fees based on carbon consumption metrics, or to condition currency access on vaccination status or other health criteria[1][20][30][59]. While such applications might serve legitimate policy objectives during crises, the technical infrastructure persists after crisis conditions subside, with policy tools exhibiting what political economists term "ratchet effects" where emergency powers persist beyond their emergency justification[1][20][30][59].

### Multi-Level Consensus Failures and Byzantine Scenarios

The choice between centralized ledger technology and distributed ledger technology introduces distinct failure modes with asymmetric policy implications. Centralized ledger systems maintain single points of failure where technical disruption at the central server halts the entire CBDC system, but concentrate policy control and enable rapid corrective action[46]. Distributed ledger systems eliminate single points of failure through data replication across multiple nodes, but introduce Byzantine Fault Tolerance requirements where nodes must reach consensus despite the possibility that some nodes behave maliciously[46][51].

Byzantine Fault Tolerance consensus mechanisms like Practical Byzantine Fault Tolerance can tolerate up to one-third of nodes failing or acting dishonestly[46][51]. However, this tolerance level assumes a known and stable set of validating nodes, honest behavior by node operators, and synchronous network conditions[46]. In a real CBDC system incorporating commercial banks, payment service providers, and other financial institutions as validators, the assumption that validators will not behave dishonestly becomes questionable during high-stress periods when validators face bankruptcy, regulatory pressure, or incentives to manipulate currency flows[46][51][29].

The technical literature identifies specific attack scenarios where validators coordinate to refuse validation of transactions targeting certain accounts, implement selective transaction ordering to benefit preferred participants, or delay final settlement while accumulating information about pending transactions—a phenomenon known as "front-running" where sophisticated participants exploit timing advantages to gain illegal profits[29][58][24].

If the smart contract governing policy tool implementation contains logic that validators must execute for consistency, but that logic produces unintended consequences (such as systematically locking funds in certain account types or creating phantom debts through calculation errors), the consensus mechanism cannot correct the error without a hard fork that violates the immutability property that generates public trust in the system[29][46][51]. A consensus fork splitting CBDC into two incompatible versions during a monetary crisis would constitute a catastrophic erosion of currency confidence[29][46][51].

### The Impossible Trinity of CBDC Design Objectives

The fundamental challenge emerging from the technical literature suggests that smart contract policy tools cannot simultaneously maximize three competing objectives: transaction finality, policy flexibility, and operational resilience[5][26][29][46][50][51]. Each objective implies design choices that create vulnerabilities in the other dimensions.

Rapid transaction finality—where transfers become irreversible within seconds—requires streamlined consensus protocols that reduce Byzantine Fault Tolerance guarantees, increasing vulnerability to validator collusion and network attacks[5][46][51]. Policy flexibility—the ability to modify smart contracts to address emerging risks—requires code mutability and governance mechanisms that inevitably introduce delays, creating unequal protection depending on when modifications propagate through the network[29]. Operational resilience—maintaining CBDC system availability despite component failures—requires redundancy and distributed governance that sacrifices the central bank's ability to implement instantaneous policy corrections[5][26][29].

The attempted resolution through intermediated architectures—where commercial banks provide the interface layer while the central bank operates the backend ledger—reintroduces traditional banking sector risks by recreating the very disintermediation problem that programmable CBDC policy tools supposedly address[26][29][49]. Depositors still perceive commercial banks as riskier than the central bank, so stress periods still generate deposit flight toward CBDC, but now the migration must route through the commercial banks providing the interface, creating bottlenecks and opportunities for front-running[26][29][49].

## Historical Policy Accident Frameworks and Digital Magnification

### Precedents in Monetary System Failures

The modern financial system contains numerous examples of policy implementations that generated consequences dramatically exceeding their architects' intentions, providing templates for how programmable money logic could amplify policy accidents. The 1990s Japanese "lost decade" followed from monetary policy tightening that was slightly too aggressive and too prolonged, eventually requiring decades of zero interest rate policy to partially remedy[28][41]. The speed with which policy mistakes propagate in traditional systems, however, provided time for corrective action.

More directly relevant, the 2008 financial crisis revealed how apparently sound policy logic—using mortgage-backed securities as collateral for repo financing—created cascading failures when underlying assumptions about asset quality proved invalid[29][24]. Policy frameworks that seemed robust under normal conditions generated systemic vulnerability under stress. The difference in CBDC systems is that such policy logic becomes encoded in smart contracts that execute automatically without the possibility for human judgment or corrective intervention[2][8][24][29].

The historical record also demonstrates how unintended consequences compound when multiple policy mechanisms interact. The Federal Reserve's implementation of quantitative easing combined with zero interest rate policy created unintended consequences through reduced money market fund returns, forcing investors into riskier assets and generating financial stability concerns that prompted additional regulatory intervention[31][56]. In a CBDC system where multiple smart contract policy tools operate simultaneously—holding limits, tiered remuneration, conditional spending restrictions, and expiring money mechanisms—the interaction effects become mathematically complex, creating second and third-order consequences that policy designers explicitly cannot fully anticipate[4][19][20][59].

### Feedback Loop Amplification in Programmed Systems

Programmable CBDC policy introduces feedback loop structures that differ fundamentally from traditional policy feedback. When a central bank adjusts the policy rate under normal circumstances, the adjustment propagates through deposit rate changes and lending adjustments that take weeks to manifest across the economy. This propagation delay creates what economists term "policy lags" that limit feedback loop velocity and provide windows for observing unintended consequences before full implementation[17][28][41].

Smart contract policy tools eliminate these lags by implementing changes instantaneously across all system participants simultaneously[1][17][28]. If a central bank programs CBDC remuneration to adjust based on real-time inflation metrics or unemployment statistics through oracle connections to external data sources, the policy response becomes immediate rather than lagged[29]. This creates potential for destabilizing feedback loops where policy responses to economic conditions trigger further economic changes that regenerate the original conditions, creating oscillations rather than convergence to equilibrium[29][46][51].

For instance, if CBDC remuneration automatically reduces whenever inflation exceeds a specified threshold, and holders respond to negative returns by converting CBDC to bank deposits, but that conversion generates asset price deflation that subsequently triggers CBDC remuneration increases that prompt reconversion to CBDC, the system could enter oscillatory dynamics where money continuously migrates between CBDC and deposits without settling into stable allocation[29][46][51]. The algorithmic adjustment of policy parameters in real time based on automated data feeds creates precisely the type of high-frequency trading dynamics that have generated market microstructure problems in equity markets[24][29].

Worse, sophisticated market participants would learn the policy algorithm and frontrun anticipated adjustments, exploiting the timing of smart contract parameter changes to profit from predictable price movements[24][29][58]. Financial institutions holding significant CBDC would structure transactions to trigger maximum impact from known policy thresholds—for instance, concentrating conversions from CBDC to deposits just before scheduled remuneration adjustments to maximize returns on the reduced rate applied to future holdings[24][29][58].

## Risk Mitigation Approaches and Their Limitations

### Technical Safeguards and Their Failure Modes

The academic and policy literature on CBDC risk mitigation proposes numerous technical safeguards intended to reduce smart contract vulnerabilities: formal verification methods that mathematically prove code correctness, comprehensive security audits through multiple independent firms, open-source code bases enabling broader security scrutiny, continuous monitoring systems that detect anomalous transaction patterns, and staged pilot programs that identify failures before full system deployment[5][24][26][29][51][52].

These safeguards provide meaningful risk reduction for traditional software vulnerabilities. Formal verification can detect certain categories of logic errors before code deployment[24][29][51]. Multiple independent audits increase the probability that at least one firm identifies known vulnerability patterns[24][29][51]. Open-source code enables detection of flaws that closed-source development would miss[24][29][51].

However, the effectiveness of these safeguards degrades substantially when applied to smart contracts because the failure modes differ fundamentally from traditional software problems[2][8][24][29][55]. Formal verification works effectively for well-specified mathematical proofs but fails when the challenge involves unintended interactions between multiple correct functions, edge cases in business logic that seem correct under normal conditions but produce catastrophic errors under stressed conditions, or attacks that exploit specific blockchain consensus properties unrelated to traditional software failures[2][8][24][29][55][58].

Comprehensive security audits identify known attack patterns but cannot anticipate novel exploits that emerge from creative combinations of smart contract properties, blockchain mechanics, and economic incentive structures[2][8][24][29][55]. Open-source code enables community scrutiny but also broadcasts vulnerabilities to potential attackers who can identify exploits faster than patches can be deployed[2][8][24][29][55]. Continuous monitoring detects anomalous transactions but cannot distinguish between genuinely malicious activities and novel use cases that merely appear anomalous due to monitoring system misconfiguration[24][29].

Staged pilot programs provide the most meaningful safeguard by limiting failure scope to controlled environments before full deployment[26][29]. However, the compressed timescale of modern crises—where systemic stress can accelerate from invisible to catastrophic in days—means that pilots of insufficient duration might not capture stress scenarios where smart contract failures manifest most dangerously[26][29].

### Governance and Accountability Frameworks

The policy literature emphasizes the need for robust governance structures that clarify participant responsibilities, establish liability for failures, and implement clear accountability mechanisms for smart contract modifications[50][51][54]. Well-functioning governance would require that no single actor can modify CBDC smart contracts unilaterally, that any modifications receive extensive testing before deployment, and that participants whose activities are restricted by smart contract policies have recourse mechanisms for contesting restrictions or appealing automated decisions[50][51][54].

These governance mechanisms, however, create their own risks by introducing delay and complexity that contradicts the primary motivation for programmable CBDC—achieving rapid, automated policy implementation. A governance structure requiring extensive deliberation before smart contract modifications cannot simultaneously enable real-time policy adjustments in response to emerging financial stability threats[50][51][54]. The requirement for participant recourse mechanisms for automated decisions creates administrative burden that regenerates the human intermediation the programmable approach supposedly eliminated[50][51][54].

More fundamentally, governance structures assume that power within the system distributes among multiple stakeholders with divergent interests and mutual accountability mechanisms. In reality, central banks exercise sovereign authority over CBDC systems, with commercial banks and payment service providers operating under delegated authority subject to withdrawal[50][51][54]. This asymmetry means that while formal governance documents might specify multi-stakeholder approval for policy changes, the central bank retains ultimate authority to override governance structures through legislative changes or executive authority[50][51][54].

## Cross-Border Spillovers and International Amplification

### Currency Substitution and Capital Flow Volatility

When a CBDC issued by a reserve currency country becomes available for cross-border transactions to non-residents, it creates what economists term "currency substitution" effects where foreign entities potentially abandon domestic currencies in favor of the foreign CBDC's superior safety characteristics[45][48]. If the central bank implements programmable policies like high interest rates on CBDC to incentivize domestic use, foreign investors respond by accumulating CBDC in large quantities, generating capital inflows that can destabilize the domestic financial system[45][48].

Conversely, if the central bank implements negative remuneration on CBDC to discourage holdings, foreign investors flee CBDC for alternative safe assets, creating capital outflows. The volatility of cross-border CBDC flows could increase by one-third compared to traditional banking flows because digital transfers occur instantaneously without the settlement delays that smooth traditional flows[15][38].

Small economies with weaker economic fundamentals face particular vulnerability. If a reserve currency country like the United States issues a widely available CBDC, residents of emerging market economies can bypass their own domestic financial systems entirely and hold U.S. CBDC directly[45][48]. This creates what financial regulators term "unmanaged capital account substitution" where domestic residents unilaterally abandon domestic currency without policy coordination, potentially forcing rapid depreciation of the domestic currency and generating financial crises[45][48].

### Coordination Challenges and Policy Fragmentation

The technical literature on cross-border CBDC arrangements identifies fundamental coordination challenges that emerge when multiple CBDCs coexist: divergent privacy standards across jurisdictions create incompatibilities in data sharing requirements; different anti-money laundering and counter-terrorism financing regimes prevent interoperability between national systems; and conflicting capital flow management measures by different governments create contradictory restrictions on the same transactions[44][47][52].

Rather than resolving these coordination problems, programmable CBDC logic potentially amplifies them by embedding national policy preferences into the smart contract code itself. A CBDC designed to enforce negative interest rates at prescribed thresholds creates conflicts with foreign CBDCs lacking such provisions. A CBDC programmed to block transactions to sanctioned entities based on one country's sanctions list cannot interoperate with CBDC systems using different sanctions designations[44][47][52].

The attempted resolution through interoperability bridges—middleware systems connecting different CBDC ledgers—introduces additional failure modes[3][29][44]. If the bridge code itself contains vulnerabilities, attacks could exploit the bridge to generate inconsistencies between linked systems, potentially creating arbitrage opportunities where transactions settle in one CBDC but fail in the other[3][29][44]. The bridge operator exercises gatekeeper authority over which transactions route between systems, creating political leverage points where nations could restrict others' access to bridged networks[3][29][44].

## Synthesis and Policy Implications

### The Fundamental Asymmetry Between Control and Risk

The evidence examined throughout this analysis reveals a fundamental asymmetry in CBDC smart contract architecture: the mechanisms enabling granular monetary policy control through programmable money are precisely the mechanisms that generate systemic operational risk through their complexity, transparency, and automated execution[2][8][24][29][46][51][54][59].

A central bank could theoretically achieve superior monetary policy transmission by implementing CBDC remuneration that automatically adjusts in real time based on economic conditions, conditional spending restrictions that ensure stimulus flows toward consumption rather than speculation, and programmable expiration mechanisms that accelerate money velocity during crises. These capabilities represent genuine policy advances over traditional instruments. However, the technical implementation of these capabilities requires smart contract code that operates automatically without human oversight, executes identically across millions of accounts simultaneously, and cannot be modified mid-crisis without system-threatening hard forks[2][8][24][29][46][51][54][59].

The risk profile differs fundamentally from traditional financial risks because the failure modes propagate across the entire system identically and instantaneously. A traditional banking failure confined to a specific institution generates contagion effects that spread through payment flows and credit relationships over time, allowing regulatory authorities windows for intervention. A smart contract failure affecting CBDC affects all accounts identically in microseconds, rendering human intervention infeasible until after the failure completes[2][8][24][29][46].

### Design Trade-offs Without Optimum Solutions

The literature analyzing CBDC design choices repeatedly identifies trade-offs where improving performance on one dimension necessarily degrades performance on another, without identifying design approaches that simultaneously optimize across all dimensions[5][26][29][46][50][51][52]. Maximizing transaction finality to enable rapid payments requires reducing Byzantine Fault Tolerance guarantees that increase attack vulnerability. Enabling policy flexibility through smart contract mutability requires accepting delays in policy implementation that undermine the primary rationale for programmability. Achieving operational resilience through redundancy requires distributing control across validators who might behave adversarially[5][26][29][46][50][51][52].

The intermediated two-tier architecture attempting to resolve these trade-offs by delegating retail access to commercial banks while maintaining central bank control over the backend ledger recreates traditional banking vulnerabilities without fully eliminating the disintermediation risks the architecture supposedly addresses[26][29][49]. Depositors aware that commercial banks interface with CBDC still perceive direct CBDC access as safer during crises, so the intermediaries cannot credibly prevent CBDC migration during stress periods[26][29][49].

Similarly, policy tools including tiered remuneration and holding limits appear to provide risk isolation by preventing excessive CBDC concentration or runs into CBDC during crises. However, empirical modeling demonstrates that these tools operate across a narrow parameter space where effectiveness requires precise calibration without firm guidance on what calibration levels optimize across financial stability, monetary policy effectiveness, and CBDC utility as payments infrastructure[31][34][56]. Too-high holding limits defeat their purpose by allowing concentrated CBDC accumulation. Too-low limits frustrate users attempting to maintain precautionary balances, driving them toward alternative funding sources that create different stability risks[31][34][56].

### The Empirical Uncertainty Surrounding Policy Effectiveness

Despite extensive academic and policy research on CBDC, profound empirical uncertainty persists regarding whether programmable money logic actually achieves its intended policy objectives or generates unanticipated consequences exceeding the intended benefits. The research literature contains conflicting findings on whether CBDC reduces or amplifies bank runs, whether it improves or impairs credit availability, whether it facilitates or hinders cross-border payments, and whether it enhances or degrades financial stability across business cycles[7][10][31][60].

Some analyses find that CBDC with appropriate safeguards could increase financial stability by providing a safe asset that prevents disintermediation and enables faster detection of banking system stress through real-time monitoring of CBDC demand[7][31]. Others find that no safeguard design can prevent CBDC from substantially amplifying runs during crises, that CBDC will necessarily reduce bank lending as deposits migrate to central bank money, and that the resulting credit reduction would impair economic recovery precisely when lending stimulus is most needed[7][10][31][60].

This empirical uncertainty cannot be resolved through continued theoretical modeling because the question is fundamentally empirical—it concerns how real humans with diverse preferences, expectations, and strategic sophistication will respond to CBDC systems in conditions ranging from normal growth to financial crisis to pandemic disruption[7][31][60]. Conducting empirical research requires deploying actual CBDC systems at realistic scale, which generates precisely the policy accident risks that motivate caution in implementation.

### Recommendations for Prudent Policy

The evidence reviewed suggests that current CBDC design approaches balance the ambition of programmable monetary policy against systemic risks inadequately, particularly regarding smart contract vulnerabilities and policy accident amplification[2][8][24][29][46][51][54]. Central banks considering CBDC deployment should adopt a substantially more conservative approach than currently evident in most CBDC initiatives:

First, central banks should restrict programmable CBDC features to the minimum necessary to achieve core policy objectives, avoiding complex multi-parameter smart contracts that attempt to simultaneously optimize across monetary policy, financial stability, and payments efficiency[2][8][24][29]. A CBDC limited to basic holding limits and tiered remuneration presents substantially less failure risk than one incorporating expiring money, conditional spending restrictions, and real-time algorithmic policy adjustments[2][8][24][29].

Second, central banks should implement robust governance structures that preserve human oversight of smart contract modifications, accepting delays in policy implementation as an acceptable cost for reducing policy accident risk[50][51][54]. Automatic algorithmic adjustments of CBDC policy parameters based on external data feeds should be explicitly prohibited until many years of successful operation under simpler policy frameworks establish confidence[50][51][54].

Third, central banks should plan extensive pilot programs at progressively larger scales before full CBDC deployment, with each pilot tier extending across full business cycles or longer to capture stress scenarios where smart contract vulnerabilities manifest[26][29]. The urgency to deploy CBDC rapidly should not override the imperative to deploy systems whose failure modes are understood through extensive real-world experience[26][29].

Fourth, cross-border CBDC arrangements should be approached with extreme caution, recognizing that interoperability challenges and conflicting national policies create failure modes that single-country deployments can avoid[44][47][52]. Premature internationalization of CBDC before domestic systems establish proven resilience imports foreign policy conflicts into the domestic monetary system[44][47][52].

Central bank digital currency initiatives represent a genuine evolution in monetary system infrastructure with potential to improve payment efficiency, enhance financial inclusion, and provide safer asset alternatives for public money. However, the research evidence demonstrates that programmable money logic implemented through smart contracts does not balance money supply control and risk isolation in ways that eliminate policy accident amplification. Rather, the very mechanisms enabling granular control introduce systematic vulnerabilities whose consequences could exceed the benefits of programmatic convenience.

## Annotations
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Can Retail Central Bank Digital Currencies Improve the Delivery of ...', 'url': 'https://www.imf.org/-/media/files/publications/wp/2025/english/wpiea2025211-source-pdf.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'CBDC – How Dangerous is Programmability? – The FinReg Blog', 'url': 'https://sites.duke.edu/thefinregblog/2021/09/21/cbdc-how-dangerous-is-programmability/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Interoperability Between Central Bank Digital Currency Systems and', 'url': 'https://openknowledge.worldbank.org/server/api/core/bitstreams/a6f91b4c-32ee-4962-b51f-e164fb046f6c/content'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The Fed - Money and Payments: The U.S. Dollar in the Age of Digital ...', 'url': 'https://www.federalreserve.gov/publications/january-2022-cbdc.htm'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Central bank digital currency (CBDC) information security and ...', 'url': 'https://www.bis.org/publ/othp81.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Achieving Uniformity of Tokenized Money Through Smart Contracts', 'url': 'https://www.fireblocks.com/report/achieving-uniformity-of-tokenized-money-through-smart-contracts'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Financial Stability Implications of CBDC - Federal Reserve Board', 'url': 'https://www.federalreserve.gov/econres/feds/files/2024021pap.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'CBDC – How Dangerous is Programmability? – The FinReg Blog', 'url': 'https://sites.duke.edu/thefinregblog/2021/09/21/cbdc-how-dangerous-is-programmability/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] central bank digital currency: further navigating challenges and risks', 'url': 'https://www.imf.org/-/media/files/publications/pp/2025/english/ppea2025041.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Central bank digital currencies: financial stability implications', 'url': 'https://www.bis.org/publ/othp42_fin_stab.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Central bank digital currency (CBDC) information security and ...', 'url': 'https://www.bis.org/publ/othp81.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] The economics of central bank digital currency', 'url': 'https://www.ecb.europa.eu/pub/pdf/scpdps/ecb.dp20~c5daf3a9fd.en.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Design choices for Central Bank Digital Currency', 'url': 'https://www.brookings.edu/wp-content/uploads/2020/07/Design-Choices-for-CBDC_Final-for-web.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] BIS Papers - No 123 - CBDCs in emerging market economies', 'url': 'https://www.bis.org/publ/bppdf/bispap123.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] CBDC policies in open economies - Bank for International Settlements', 'url': 'https://www.bis.org/publ/work1086.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Central bank digital currency (CBDC) information security and ...', 'url': 'https://www.bis.org/publ/othp81.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A digital euro: Monetary policy considerations - SUERF', 'url': 'https://www.suerf.org/publications/suerf-policy-notes-and-briefs/a-digital-euro-monetary-policy-considerations/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Central Bank Digital Currencies and Financial Stability', 'url': 'https://www.imf.org/-/media/files/publications/wp/2024/english/wpiea2024226-print-pdf.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] CENTRAL BANK DIGITAL CURRENCY', 'url': 'https://www.edps.europa.eu/system/files/2023-03/23-03-29_techdispatch_cbdc_en.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Programmable Money, Welfare State, and the Legal Construction of ...', 'url': 'https://scholarship.law.upenn.edu/cgi/viewcontent.cgi?article=2106&context=jil'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'CBDC – How Dangerous is Programmability? – The FinReg Blog', 'url': 'https://sites.duke.edu/thefinregblog/2021/09/21/cbdc-how-dangerous-is-programmability/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Expiring money (Part I) - World Bank Blogs', 'url': 'https://blogs.worldbank.org/en/allaboutfinance/expiring-money-part-i'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Central bank digital currency (CBDC) information security and ...', 'url': 'https://www.bis.org/publ/othp81.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Missing Key: The challenge of cybersecurity and central bank digital ...', 'url': 'https://www.atlanticcouncil.org/in-depth-research-reports/report/missing-key/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Retail CBDC and U.S. Monetary Policy Implementation: A Stylized ...', 'url': 'https://www.federalreserve.gov/econres/feds/files/2022032pap.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Central bank digital currency (CBDC) information security and ...', 'url': 'https://www.bis.org/publ/othp81.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Money by choice, not command: CBDC vs Stablecoin regulation', 'url': 'https://www.ocorian.com/knowledge-hub/insights/money-choice-not-command'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Central bank digital currency and monetary policy implementation', 'url': 'https://www.ecb.europa.eu/pub/pdf/scpops/ecb.op345~4b4eeee055.en.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The Fed - Security Considerations for a Central Bank Digital Currency', 'url': 'https://www.federalreserve.gov/econres/notes/feds-notes/security-considerations-for-a-central-bank-digital-currency-20220203.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The Risks of CBDCs - Cato Institute', 'url': 'https://www.cato.org/visual-feature/risks-of-cbdcs'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Financial Stability Implications of CBDC - Federal Reserve Board', 'url': 'https://www.federalreserve.gov/econres/feds/files/2024021pap.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Monetary Policy with Negative Interest Rates: De-linking Cash from ...', 'url': 'https://www.ijcb.org/sites/default/files/journal/v17n1/ijcb-v17n1-monetary-policy-negative-interest-rates-de-linking-cash-digital-money.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Will Central Bank Digital Currency Disintermediate Banks?', 'url': 'https://www.anderson.ucla.edu/sites/default/files/document/2023-05/5.26.23%20Paper%20Toni%20Whited%20CBDC.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Central Bank Digital Currency and financial stability', 'url': 'https://www.ecb.europa.eu/pub/pdf/scpwps/ecb.wp2783~0af3ad7576.en.pdf?63e779459d95b6c272ca41fe400a85e9'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The Case for Central Bank Digital Currencies | Cato Institute', 'url': 'https://www.cato.org/cato-journal/spring/summer-2021/case-central-bank-digital-currencies'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] The optimal quantity of CBDC in a bank-based economy', 'url': 'https://www.ecb.europa.eu/pub/pdf/scpwps/ecb.wp2689~846e464fd8.en.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Central bank digital currency (CBDC) information security and ...', 'url': 'https://www.bis.org/publ/othp81.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] CBDC policies in open economies - Bank for International Settlements', 'url': 'https://www.bis.org/publ/work1086.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] CBDC: Concepts, Benefits, Risks, Design, and Implications', 'url': 'https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID4234876_code361708.pdf?abstractid=4234876&mirid=1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Central Bank Digital Currency (CBDC) - Virtual Handbook', 'url': 'https://www.imf.org/en/topics/digital-payments-and-finance/central-bank-digital-currency/virtual-handbook'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Central bank digital currency and monetary policy implementation', 'url': 'https://www.ecb.europa.eu/pub/pdf/scpops/ecb.op345~4b4eeee055.en.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Driving Financial Inclusion Through Central Bank Digital Currencies', 'url': 'https://www.undp.org/sites/g/files/zskgke326/files/2025-06/undp-driving-financial-inclusion-through-cbdcs.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Project Polaris: A security and resilience framework for CBDC systems', 'url': 'https://www.bis.org/publ/othp70.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Options for access to and interoperability of CBDCs for cross-border ...', 'url': 'https://www.bis.org/publ/othp52.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Cross-Border Central Bank Digital Currencies, Bank Runs and ...', 'url': 'https://www.imf.org/-/media/files/publications/wp/2022/english/wpiea2022083-print-pdf.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Central Bank Digital Currencies: A Survey - arXiv', 'url': 'https://arxiv.org/html/2507.08880v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Cross-Border Payments with Retail Central Bank Digital Currencies', 'url': 'https://www.imf.org/-/media/files/publications/ftn063/2024/english/ftnea2024002.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] The external financial spillovers of CBDCs* - SUERF', 'url': 'https://www.suerf.org/wp-content/uploads/2023/11/f_e2f6c5e11ecba290f883237b539c758c_75845_suerf.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Central bank digital currencies: An active role for commercial banks', 'url': 'https://www.mckinsey.com/industries/financial-services/our-insights/central-bank-digital-currencies-an-active-role-for-commercial-banks'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Legal aspects of retail CBDCs - Bank for International Settlements', 'url': 'https://www.bis.org/publ/othp88_legal.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The Fed - Security Considerations for a Central Bank Digital Currency', 'url': 'https://www.federalreserve.gov/econres/notes/feds-notes/security-considerations-for-a-central-bank-digital-currency-20220203.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Positioning Central Bank Digital Currency in the Payments Landscape', 'url': 'https://www.imf.org/-/media/files/publications/ftn063/2024/english/ftnea2024006.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Money by choice, not command: CBDC vs Stablecoin regulation', 'url': 'https://www.ocorian.com/knowledge-hub/insights/money-choice-not-command'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Central bank digital currency (CBDC) information security and ...', 'url': 'https://www.bis.org/publ/othp81.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Smart Contract Vulnerabilities: Case Studies - Coinmetro', 'url': 'https://www.coinmetro.com/learning-lab/smart-contract-vulnerabilities-case-studies'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Financial Stability Implications of CBDC - Federal Reserve Board', 'url': 'https://www.federalreserve.gov/econres/feds/files/2024021pap.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Central bank digital currencies: foundational principles and core ...', 'url': 'https://www.bis.org/publ/othp33_summary.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': "Smart Contract Security Risks: Today's 10 Top Vulnerabilities | Cobalt", 'url': 'https://www.cobalt.io/blog/smart-contract-security-risks'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The Cbdc Retail Money Revolution: How Will It Impact Monetary ...', 'url': 'https://www.abacademies.org/articles/the-cbdc-retail-money-revolution-how-will-it-impact-monetary-policies-and-consumer-behavior-13904.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] The Macroeconomic Implications of CBDC: A Review of the Literature', 'url': 'https://www.federalreserve.gov/econres/feds/files/2022076pap.pdf'}}

## Sources
https://www.imf.org/-/media/files/publications/wp/2025/english/wpiea2025211-source-pdf.pdf
https://sites.duke.edu/thefinregblog/2021/09/21/cbdc-how-dangerous-is-programmability/
https://openknowledge.worldbank.org/server/api/core/bitstreams/a6f91b4c-32ee-4962-b51f-e164fb046f6c/content
https://www.federalreserve.gov/publications/january-2022-cbdc.htm
https://www.bis.org/publ/othp81.pdf
https://www.fireblocks.com/report/achieving-uniformity-of-tokenized-money-through-smart-contracts
https://www.federalreserve.gov/econres/feds/files/2024021pap.pdf
https://sites.duke.edu/thefinregblog/2021/09/21/cbdc-how-dangerous-is-programmability/
https://www.imf.org/-/media/files/publications/pp/2025/english/ppea2025041.pdf
https://www.bis.org/publ/othp42_fin_stab.pdf
https://www.bis.org/publ/othp81.pdf
https://www.ecb.europa.eu/pub/pdf/scpdps/ecb.dp20~c5daf3a9fd.en.pdf
https://www.brookings.edu/wp-content/uploads/2020/07/Design-Choices-for-CBDC_Final-for-web.pdf
https://www.bis.org/publ/bppdf/bispap123.pdf
https://www.bis.org/publ/work1086.pdf
https://www.bis.org/publ/othp81.pdf
https://www.suerf.org/publications/suerf-policy-notes-and-briefs/a-digital-euro-monetary-policy-considerations/
https://www.imf.org/-/media/files/publications/wp/2024/english/wpiea2024226-print-pdf.pdf
https://www.edps.europa.eu/system/files/2023-03/23-03-29_techdispatch_cbdc_en.pdf
https://scholarship.law.upenn.edu/cgi/viewcontent.cgi?article=2106&context=jil
https://sites.duke.edu/thefinregblog/2021/09/21/cbdc-how-dangerous-is-programmability/
https://blogs.worldbank.org/en/allaboutfinance/expiring-money-part-i
https://www.bis.org/publ/othp81.pdf
https://www.atlanticcouncil.org/in-depth-research-reports/report/missing-key/
https://www.federalreserve.gov/econres/feds/files/2022032pap.pdf
https://www.bis.org/publ/othp81.pdf
https://www.ocorian.com/knowledge-hub/insights/money-choice-not-command
https://www.ecb.europa.eu/pub/pdf/scpops/ecb.op345~4b4eeee055.en.pdf
https://www.federalreserve.gov/econres/notes/feds-notes/security-considerations-for-a-central-bank-digital-currency-20220203.html
https://www.cato.org/visual-feature/risks-of-cbdcs
https://www.federalreserve.gov/econres/feds/files/2024021pap.pdf
https://www.ijcb.org/sites/default/files/journal/v17n1/ijcb-v17n1-monetary-policy-negative-interest-rates-de-linking-cash-digital-money.pdf
https://www.anderson.ucla.edu/sites/default/files/document/2023-05/5.26.23%20Paper%20Toni%20Whited%20CBDC.pdf
https://www.ecb.europa.eu/pub/pdf/scpwps/ecb.wp2783~0af3ad7576.en.pdf?63e779459d95b6c272ca41fe400a85e9
https://www.cato.org/cato-journal/spring/summer-2021/case-central-bank-digital-currencies
https://www.ecb.europa.eu/pub/pdf/scpwps/ecb.wp2689~846e464fd8.en.pdf
https://www.bis.org/publ/othp81.pdf
https://www.bis.org/publ/work1086.pdf
https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID4234876_code361708.pdf?abstractid=4234876&mirid=1
https://www.imf.org/en/topics/digital-payments-and-finance/central-bank-digital-currency/virtual-handbook
https://www.ecb.europa.eu/pub/pdf/scpops/ecb.op345~4b4eeee055.en.pdf
https://www.undp.org/sites/g/files/zskgke326/files/2025-06/undp-driving-financial-inclusion-through-cbdcs.pdf
https://www.bis.org/publ/othp70.pdf
https://www.bis.org/publ/othp52.pdf
https://www.imf.org/-/media/files/publications/wp/2022/english/wpiea2022083-print-pdf.pdf
https://arxiv.org/html/2507.08880v1
https://www.imf.org/-/media/files/publications/ftn063/2024/english/ftnea2024002.pdf
https://www.suerf.org/wp-content/uploads/2023/11/f_e2f6c5e11ecba290f883237b539c758c_75845_suerf.pdf
https://www.mckinsey.com/industries/financial-services/our-insights/central-bank-digital-currencies-an-active-role-for-commercial-banks
https://www.bis.org/publ/othp88_legal.pdf
https://www.federalreserve.gov/econres/notes/feds-notes/security-considerations-for-a-central-bank-digital-currency-20220203.html
https://www.imf.org/-/media/files/publications/ftn063/2024/english/ftnea2024006.pdf
https://www.ocorian.com/knowledge-hub/insights/money-choice-not-command
https://www.bis.org/publ/othp81.pdf
https://www.coinmetro.com/learning-lab/smart-contract-vulnerabilities-case-studies
https://www.federalreserve.gov/econres/feds/files/2024021pap.pdf
https://www.bis.org/publ/othp33_summary.pdf
https://www.cobalt.io/blog/smart-contract-security-risks
https://www.abacademies.org/articles/the-cbdc-retail-money-revolution-how-will-it-impact-monetary-policies-and-consumer-behavior-13904.html
https://www.federalreserve.gov/econres/feds/files/2022076pap.pdf