# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** de149670 | **Time:** 234.74s | **Cost:** $0.85794
--------------------------------------------------------------------------------

# Stochastic Models of Photovoltaic Volatility and Engineering Limits of Renewable Penetration

### Key Points
*   **Stochastic models generally expand rather than constrain calculated penetration limits:** Compared to deterministic "worst-case" scenarios, stochastic models often reveal that the engineering limits of renewable penetration are higher. By accounting for the low probability of simultaneous extreme events (e.g., minimum load coinciding perfectly with maximum generation), stochastic analysis allows grid operators to move from rigid safety margins to risk-based planning [cite: 1, 2].
*   **Volatility is a physical constraint, but modeling defines the operational envelope:** While the physical volatility of photovoltaics (PV) imposes challenges such as voltage fluctuations and frequency instability [cite: 3, 4], stochastic models provide the mathematical framework to quantify these risks. This allows for higher penetration levels by optimizing mitigation strategies (like battery sizing and ramp-rate control) more efficiently than deterministic rules [cite: 5, 6].
*   **Risk tolerance is the new limiting factor:** In stochastic frameworks, the "limit" is no longer a hard engineering boundary but a function of acceptable risk (e.g., accepting a 1% probability of overvoltage). Stricter risk margins significantly reduce hosting capacity, while flexible margins increase it [cite: 2, 7].
*   **Tail risks and extreme events remain critical constraints:** Stochastic modeling is essential for identifying "tail risks"—rare but catastrophic events like hurricanes or extended dark doldrums—that deterministic models often miss. These extreme volatility events can impose hard constraints on grid reliability if not properly mitigated [cite: 8, 9].

---

## 1. Introduction

The integration of photovoltaic (PV) systems into electrical grids has shifted from a peripheral concern to a central challenge in power systems engineering. As renewable penetration levels rise, the inherent variability and uncertainty of solar irradiance—termed "volatility"—pose significant risks to grid stability. The central question facing engineers and planners is whether this volatility imposes a hard ceiling on the amount of renewable energy a grid can absorb, known as the engineering limit of renewable penetration.

Historically, grid planning relied on deterministic models. These models assess grid capacity based on worst-case snapshots, such as peak generation occurring during minimum load. While safe, this approach is increasingly viewed as overly conservative, potentially stifling the deployment of renewable assets. In response, stochastic models have emerged as a superior alternative. These models utilize probability distribution functions (PDFs), Monte Carlo simulations, and time-series analysis to capture the random nature of solar irradiance and load patterns.

This report provides an exhaustive analysis of how stochastic models of PV volatility interact with the engineering limits of renewable penetration. It argues that while PV volatility introduces physical challenges—specifically regarding voltage stability, frequency response, and ramp rates—stochastic models do not inherently constrain penetration. Instead, they refine the definition of these limits, often revealing latent capacity that deterministic models obscure. However, they also introduce a new paradigm where limits are defined by statistical risk tolerance rather than absolute physical thresholds.

## 2. The Physics of PV Volatility and Grid Constraints

To understand how models constrain or enable penetration, one must first understand the physical phenomena being modeled. PV volatility is not merely a fluctuation in power output; it is a complex interaction between atmospheric conditions and grid dynamics.

### 2.1 Sources of Volatility
PV power generation is governed by solar irradiance, which is subject to both deterministic cycles (diurnal and seasonal patterns) and stochastic fluctuations (cloud cover, aerosols, and weather events).
*   **Deterministic Variability:** The sun's path is predictable. Clear-sky irradiance models can accurately forecast the theoretical maximum power available at any given second [cite: 10, 11].
*   **Stochastic Intermittency:** The primary source of volatility is cloud movement. "Cloud edge effects" can cause irradiance to momentarily exceed clear-sky limits (over-irradiance) due to reflection, followed by rapid drops (ramps) as clouds obscure the sun [cite: 12, 13].
*   **Extreme Events:** Rare meteorological events, such as hurricanes or solar eclipses, represent extreme volatility. For instance, during a hurricane, optically thick clouds can reduce generation by over 70% across large geographic regions, imposing severe stress on grid reserves [cite: 8, 9].

### 2.2 Engineering Constraints in High-Penetration Grids
The volatility described above interacts with three primary engineering constraints:

#### 2.2.1 Voltage Stability and Hosting Capacity
In distribution networks, particularly low-voltage (LV) grids, the injection of active power from PV systems can cause voltage levels to rise. If generation exceeds local load, power flows in reverse (backfeeding), potentially pushing voltage at the point of common coupling (PCC) beyond statutory limits (e.g., $\pm 10\%$ of nominal voltage) [cite: 3, 14].
*   **The Constraint:** Overvoltage is frequently the binding constraint for PV Hosting Capacity (PVHC). Rapid fluctuations in irradiance can cause voltage to flicker or oscillate, wearing out tap changers and disrupting sensitive equipment [cite: 1, 15].
*   **Reactive Power:** PV inverters typically operate at unity power factor. As penetration increases, the lack of reactive power support exacerbates voltage instability. Stochastic studies show that voltage magnitude reduction and collapse can occur more abruptly under high PV penetration if reactive power control is insufficient [cite: 3].

#### 2.2.2 Frequency Stability and Inertia
Power systems rely on the rotational inertia of synchronous generators (coal, gas, hydro) to buffer imbalances between supply and demand. PV systems are grid-following inverter-based resources (IBRs) and traditionally provide zero inertia.
*   **The Constraint:** As PV replaces synchronous generation, system inertia declines. This leads to a higher Rate of Change of Frequency (RoCoF) and deeper frequency nadirs following disturbances (e.g., a generator trip) [cite: 4, 16].
*   **Volatility Impact:** High-frequency volatility from PV (sub-hourly fluctuations) requires increased regulation reserves. If the grid lacks sufficient fast-frequency response (FFR), the stochastic variation of solar output can destabilize the grid frequency, potentially leading to load shedding or blackouts [cite: 4, 17].

#### 2.2.3 Ramp Rates and Balancing
PV power output can change dramatically within seconds. These "ramp events" create a mismatch between generation and load that must be balanced by dispatchable resources or storage.
*   **The Constraint:** Grid codes often impose ramp-rate limits (e.g., 10% of rated capacity per minute) [cite: 18]. If the stochastic volatility of the PV plant exceeds these limits, the system must either curtail power or rely on expensive energy storage systems (ESS) to smooth the output [cite: 6, 19].

## 3. Deterministic vs. Stochastic Modeling Paradigms

The methodology used to calculate engineering limits fundamentally alters the result. The literature reveals a sharp dichotomy between deterministic and stochastic approaches.

### 3.1 Deterministic Modeling: The Conservative Constraint
Deterministic methods calculate limits based on fixed, worst-case input values.
*   **Methodology:** Planners typically analyze the scenario of **Minimum Load + Maximum Generation**. If the grid voltage or thermal limits are not violated in this extreme case, the penetration level is deemed acceptable [cite: 1, 2].
*   **Implication:** This approach assumes that the worst-case conditions for all parameters (load, irradiance, phase imbalance) occur simultaneously.
*   **Result:** Deterministic models yield a single, binary value for hosting capacity. Because they do not account for the low probability of simultaneous worst-case events, they often underestimate the true capacity of the grid, effectively "constraining" renewable penetration to artificially low levels [cite: 1, 20].

### 3.2 Stochastic Modeling: The Risk-Based Expansion
Stochastic models incorporate uncertainty by treating input variables (irradiance, load, temperature) as random variables described by Probability Distribution Functions (PDFs).
*   **Methodology:** Techniques such as Monte Carlo simulation generate thousands of scenarios, capturing the correlation (or lack thereof) between high PV generation and low load.
*   **Implication:** These models reveal that the probability of a constraint violation (e.g., overvoltage) might be negligible even at penetration levels significantly higher than the deterministic limit [cite: 2, 21].
*   **Result:** Stochastic models generally **increase** the calculated engineering limits. For example, a study on South African grids showed that stochastic optimization outperformed deterministic models by reducing system costs and curtailment, effectively allowing for better integration of renewables [cite: 22]. Similarly, research in Sweden demonstrated that moving from a deterministic "worst-case" view to a stochastic view with a 10% risk tolerance allowed for significantly higher PV connection numbers [cite: 2, 7].

### 3.3 Comparative Analysis
The literature consistently suggests that stochastic models do not constrain engineering limits; rather, they *liberate* the grid from the conservatism of deterministic models.
*   **Hosting Capacity:** Stochastic approaches allow limits to be expressed probabilistically (e.g., "30% penetration with a 1% risk of overvoltage") rather than as a hard stop. This flexibility is crucial for policy and planning [cite: 1, 14].
*   **Cost Efficiency:** Stochastic optimization has been shown to find global optimal solutions for storage sizing and dispatch that deterministic models miss, leading to lower operational costs and higher reliability [cite: 5, 23].

## 4. Stochastic Modeling of PV Volatility

To accurately assess limits, the volatility itself must be modeled with high fidelity. Simple "on-off" models or hourly averages are insufficient for capturing the sub-hourly dynamics that threaten grid stability.

### 4.1 Mathematical Frameworks
Researchers have developed sophisticated mathematical models to represent PV volatility:
*   **Clear Sky Index & Decomposition:** Models often decompose irradiance into a deterministic "clear sky" component and a stochastic "cloud cover" component (Clear Sky Index). The stochastic component is often modeled using autoregressive methods (AR) or Markov chains [cite: 10, 11, 24].
*   **AR-GARCH Models:** To capture the "volatility clustering" (periods of high variability followed by calm), Generalized Autoregressive Conditional Heteroscedasticity (AR-GARCH) models are used. These are particularly effective at modeling the time-varying variance of solar irradiance, which is critical for risk management and option pricing in energy markets [cite: 10, 25].
*   **Regime-Switching Models:** Some models employ regime-switching (e.g., between "sunny," "cloudy," and "overcast" states) using Markov chains. This allows for the simulation of abrupt changes in output that characterize ramp events [cite: 10, 24].
*   **Spatiotemporal Correlations:** Advanced stochastic models must also account for the spatial correlation between dispersed PV sites. If volatility is highly correlated across a region (e.g., a large weather front), the aggregate smoothing effect is reduced, and the impact on the transmission grid is magnified [cite: 26, 27].

### 4.2 Modeling Extreme Events (Tail Risk)
Standard stochastic models based on Gaussian distributions often fail to capture "fat tails"—extreme events like hurricanes.
*   **Hurricane Modeling:** Recent research has introduced stochastic models specifically for irradiance decay during hurricanes. These models use mixed-effect regression on historical hurricane data to predict generation loss as a function of distance from the storm center. Such models are vital for resilience planning, revealing that generation can drop by 70% even if infrastructure remains intact [cite: 8, 9].
*   **Implication for Limits:** By quantifying these tail risks, stochastic models impose a different kind of constraint: a **resilience constraint**. While day-to-day volatility might allow for 50% penetration, the risk of a 3-day generation drought during a hurricane might cap the "safe" penetration level lower unless backup generation or long-duration storage is available.

## 5. Impact on Hosting Capacity (HC)

Hosting Capacity (HC) is the amount of new production (PV) or consumption (EV) that can be connected to the grid without endangering power quality or reliability. Stochastic modeling has revolutionized HC analysis.

### 5.1 The Role of Risk Margins
In a stochastic framework, the HC is not a fixed number but a function of the **Planning Risk Margin**.
*   **Epistemic vs. Aleatory Uncertainty:** Aleatory uncertainty refers to inherent randomness (weather), while epistemic uncertainty refers to a lack of knowledge (e.g., where future PVs will be installed). Stochastic HC analysis combines these to produce an "Epistemic PDF" of possible grid states [cite: 2, 28].
*   **Sensitivity to Risk:** Research indicates that HC is highly sensitive to the chosen risk level.
    *   **Strict Planning (1% Risk):** If a Distribution System Operator (DSO) accepts only a 1% chance of voltage violation, the HC is significantly reduced (e.g., 31% lower than the base case) [cite: 2, 7].
    *   **Flexible Planning (10% Risk):** Relaxing the risk margin to 10% (meaning the 90th percentile of voltage profiles is within limits) can increase HC by 15% or more, potentially allowing all customers in a test network to install PV [cite: 2, 7].
*   **Conclusion:** The "engineering limit" is effectively a policy decision. Stochastic models provide the dial (risk tolerance) that operators turn to set the limit.

### 5.2 Voltage Constraints and Probabilistic Assessment
Overvoltage remains the primary physical constraint in LV networks.
*   **Probabilistic Power Flow (PPF):** Instead of running one power flow calculation, engineers run thousands using Monte Carlo simulations. This reveals that voltage violations are often transient and rare.
*   **Mitigation through Probability:** Because the probability of maximum PV generation coinciding exactly with minimum load is low, stochastic analysis often justifies "over-installing" PV capacity relative to the transformer rating, assuming that some curtailment or voltage control (Volt-Var) will handle the rare violations [cite: 1, 14].

## 6. Frequency Stability and Inertia Constraints

While voltage is a local issue, frequency stability is a system-wide constraint. Stochastic models are critical for understanding how aggregate PV volatility affects the balance of the entire grid.

### 6.1 The Inertia Problem
As PV penetration increases, synchronous inertia decreases.
*   **Volatility Amplification:** In a low-inertia grid, the same stochastic fluctuation in solar output causes a larger frequency deviation (nadir) and a faster Rate of Change of Frequency (RoCoF) [cite: 16, 29].
*   **Thresholds:** Studies analyzing historic frequency data and future scenarios suggest that frequency volatility does not drastically deteriorate until inertia drops to very low levels (e.g., 20% of current levels). However, at these levels, the stochastic nature of PV requires fast-acting frequency response (batteries or synthetic inertia) to prevent instability [cite: 4].

### 6.2 Stochastic Frequency Dynamics
*   **Modeling Results:** Stochastic simulations show that distributed virtual inertia (from PV inverters) can stabilize frequency. However, the stochastic fluctuation of the PV source itself can cause the operating point of the virtual synchronous generator to drift, complicating control [cite: 17, 30].
*   **Constraint:** The engineering limit here is defined by the speed of the backup reserves. If reserves cannot respond faster than the stochastic ramp rates of the aggregated PV fleet, penetration is limited.

## 7. Mitigation Strategies: Storage and Ramp Rate Control

Stochastic models do not just identify limits; they optimize the solutions that extend those limits.

### 7.1 Energy Storage Sizing
Energy Storage Systems (ESS) are the primary tool for mitigating PV volatility. Deterministic sizing often leads to oversized, uneconomical batteries.
*   **Stochastic Optimization:** By using stochastic models that account for the probability of ramp events, engineers can size storage systems more precisely.
    *   **Results:** A study comparing methods found that stochastic optimization for ESS sizing increased profits by 0.87% to 127% compared to deterministic methods [cite: 31].
    *   **Ramp Rate Limits:** Stricter ramp rate limits (e.g., 1%/min vs 10%/min) drastically increase the required storage capacity. Stochastic analysis helps quantify the trade-off between grid stability (strict ramps) and economic viability (storage cost) [cite: 6, 32].

### 7.2 Forecasting and Nowcasting
The constraint imposed by volatility is largely a function of **uncertainty**. If volatility were perfectly predictable, it could be managed easily.
*   **Forecast Value:** Improved stochastic forecasting (e.g., using LSTM or neural networks) reduces the need for spinning reserves. Research shows that while short-term forecast uncertainty increases load-generation imbalance, it has little impact on operating costs if dispatch is fast (e.g., 5-minute intervals) [cite: 33, 34].
*   **Nowcasting:** Using all-sky imagers to predict irradiance ramps 20 minutes ahead allows for preventive curtailment or battery dispatch, effectively relaxing the engineering constraints imposed by sudden cloud cover [cite: 13].

## 8. Economic and Policy Implications

The engineering limits of renewable penetration are inextricably linked to economic limits. Stochastic models bridge this gap.

### 8.1 The Cost of Reliability
Stochastic models allow operators to assign a cost to reliability.
*   **Trade-offs:** By quantifying the risk of violation (e.g., "there is a 0.1% chance of a blackout at 60% penetration"), stakeholders can decide if the cost of mitigating that last 0.1% risk (via massive storage) is worth it.
*   **Market Dynamics:** PV volatility affects electricity prices. High penetration generally reduces average prices (merit order effect) but can increase price volatility (negative prices during over-generation). Stochastic models are used to price options and derivatives that hedge against this volume and price risk [cite: 10, 25, 35].

### 8.2 Regulatory Frameworks
Regulations often lag behind modeling capabilities. Many grid codes still rely on deterministic "fit-and-forget" principles.
*   **Shift to Probabilistic Codes:** There is a growing consensus that grid codes should evolve to accept probabilistic limits. This would allow for higher penetration levels by acknowledging that "100% safety" is theoretically impossible and economically prohibitive [cite: 18, 20].

## 9. Conclusion

Do stochastic models of photovoltaic volatility constrain the engineering limits of renewable penetration?

**No, they do not constrain the limits; they refine and typically expand them.**

The physical volatility of PV is the constraint. Deterministic models, by treating this volatility as a static "worst-case" threat, impose artificially low limits on penetration to ensure absolute security. Stochastic models, by contrast, embrace the complexity and randomness of the resource. They demonstrate that the *probability* of grid failure remains low even at penetration levels that exceed deterministic limits.

However, stochastic models do impose a **cognitive and computational constraint**. They require more data, more complex mathematics, and a fundamental shift in mindset from "safety factors" to "risk management." They also reveal **tail risks**—extreme weather events—that impose hard limits on resilience, suggesting that while we can push penetration high on average days, the ultimate engineering limit may be defined by the grid's ability to survive the rare, catastrophic stochastic event.

Ultimately, stochastic modeling is the key enabler for high-renewable grids, transforming PV volatility from an unmanageable threat into a quantifiable risk that can be engineered, priced, and managed.

---

## 10. Detailed Analysis of Research Findings

### 10.1 Voltage Stability and Reactive Power
Research indicates that voltage stability is a primary concern in high-penetration scenarios.
*   **Mechanism:** PV inverters operating at unity power factor do not provide reactive power support. As active power injection increases, voltage rises.
*   **Stochastic Insight:** Deterministic models assume peak generation at minimum load. Stochastic models [cite: 1, 3] show that this coincidence is rare. By modeling the joint probability distribution of load and irradiance, planners can identify a "Probabilistic Hosting Capacity" that is often significantly higher than the deterministic value.
*   **Mitigation:** The use of stochastic optimization to site and size reactive power compensation (e.g., STATCOMs or smart inverters) can further extend these limits [cite: 3].

### 10.2 Frequency Response in Low-Inertia Grids
*   **Inertia Reduction:** As PV penetration reaches 60-80%, the displacement of synchronous generators becomes critical.
*   **Stochastic Dynamics:** The random fluctuation of solar power acts as a continuous disturbance. In a low-inertia system, these small disturbances can cause frequency to jitter.
*   **Findings:** Research [cite: 4] suggests that the grid is surprisingly resilient to this volatility until inertia drops to ~20%. Below this threshold, the stochastic volatility of PV becomes a binding constraint unless Fast Frequency Response (FFR) is implemented.
*   **Virtual Inertia:** Implementing virtual inertia on PV inverters is a solution, but stochastic models show that the variable nature of the energy source (sun) makes the "virtual mass" of the generator fluctuate, adding complexity to the control loops [cite: 17].

### 10.3 The Role of Energy Storage
*   **Buffer Sizing:** Storage is the "shock absorber" for PV volatility.
*   **Stochastic Sizing:** Deterministic sizing looks at the maximum possible ramp. Stochastic sizing looks at the *distribution* of ramps.
*   **Economic Efficiency:** By sizing for the 99th percentile of ramps rather than the maximum, costs are reduced significantly with minimal impact on reliability. This economic efficiency effectively raises the "economic limit" of penetration [cite: 5, 31].

### 10.4 Extreme Weather and Resilience
*   **Hurricanes:** Standard stochastic models (Gaussian) underestimate the risk of massive, correlated generation loss during hurricanes.
*   **New Models:** New stochastic models [cite: 8, 9] that incorporate hurricane track and intensity data provide a more realistic view of these "black swan" events.
*   **Constraint:** These models suggest that in hurricane-prone regions (e.g., Florida, Caribbean), the engineering limit of PV penetration may be lower than in other regions unless the grid is hardened with significant backup generation or interconnections.

### 10.5 Comparison of Methodologies
*   **Deterministic:** Simple, robust, but conservative. "Safe but wasteful."
*   **Stochastic:** Complex, data-intensive, but efficient. "Optimized but requires risk acceptance."
*   **Optimization:** Stochastic optimization methods (e.g., Particle Swarm Optimization, Genetic Algorithms) consistently outperform deterministic methods in finding the true operational limits of the grid [cite: 23, 36].

### 10.6 Future Directions
*   **Machine Learning:** The integration of Machine Learning (LSTM, Neural Networks) into stochastic modeling is improving forecast accuracy, further reducing the uncertainty that constrains penetration [cite: 33, 37].
*   **Hybrid Models:** Combining physical models (Clear Sky) with stochastic error models (AR-GARCH) provides the best of both worlds: physical realism and statistical rigor [cite: 10, 24].

---

## References

*   **[cite: 35]** *Impact of VRE on electricity price volatility.*
*   **[cite: 25]** *Stochastic modeling of solar electricity generation.*
*   **[cite: 12]** *Solar volatility and deviation metrics.*
*   **[cite: 10]** *Stochastic modeling of PV power and prices (AR-GARCH).*
*   **[cite: 14]** *Stochastic methodology for PV Hosting Capacity (PVHC).*
*   **[cite: 8]** *Stochastic modeling of solar irradiance during hurricanes.*
*   **[cite: 9]** *Irradiance decay during hurricanes.*
*   **[cite: 3]** *Voltage stability with high PV penetration.*
*   **[cite: 4]** *Grid frequency volatility in low inertia scenarios.*
*   **[cite: 30]** *Impact of PV on frequency stability (Solar Eclipse).*
*   **[cite: 13]** *Mitigating irradiance ramps with nowcasting.*
*   **[cite: 1]** *Deterministic vs. Stochastic PVHC.*
*   **[cite: 2]** *Stochastic approach to hosting capacity and planning risk.*
*   **[cite: 28]** *Stochastic assessment of hosting capacity.*
*   **[cite: 22]** *Stochastic optimization for South African grid.*
*   **[cite: 5]** *Stochastic optimization of energy storage.*
*   **[cite: 31]** *Stochastic energy storage sizing vs deterministic.*
*   **[cite: 21]** *Probabilistic hosting capacity assessment.*
*   **[cite: 7]** *Impact of planning risk on hosting capacity.*
*   **[cite: 17]** *Distributed virtual inertia from PV.*
*   **[cite: 10]** *Stochastic modeling of PV and prices.*

**Sources:**
1. [psecommunity.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRQK7YRz1oWGmszgo9HRgbWnGziO-hLGqizCFq6hgVcnT43Gbewm3UCW4jiz_ZHF9QE31g5FL6J39Z0-ezgwSjZsJjj7OxMdbnY1aBO10OJ-1oMlEYbd13jHokVX1BZKfectgThhV3-lvdSXLNucBxINI32p94C7itB2olVRj6onMG55DeZ5W0OTODLgobmD4=)
2. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyl_bl4qlFTXVdU3SjmUkACoj1c94p2-OQIdYcDlUGwa1kYVNbih6eRCMEl2GLPMRbBSN0IPD852aIss1TDyuYq7k413wU3rgCjG1bnMvMNq51Jhd30Zyq_oU=)
3. [osti.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-7qrXs2jKR1cllDr45GnfkoOqANiOtfkxPoPnVKB1SfvsxCwK4s38OHybKgmBWCGYfxmgBXSSqwNW1rp7oZ0aFkZuXjcJLKUiOIp3H4welKfXxKDSfUVLUVthUR_A2w==)
4. [whiterose.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjafMX98mnGtYGEXhCumceNxr_vDkAXfMTfGY4sFOT-3BliXpFKOYvJqwDNa4zYMnkk8QJoR_TR-Yscnh38fA03iACDS3PzooDEwNjocMBRiNeZFFMSy2ZEk0iRRXJ1VOa7QI4c5eahf23_-MolNUpE1Y=)
5. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBRAnQRx7lUsF5zi0CRKqV84zfOE3rSTNMa5IDG1Gi9kRqhP5Q0KCRLbDO2E7jWDmqoAc30CNRaQHv3W7LX2F-_pHiBtqbi0xP-5jVvXjh7EWCod4Ha9ITD1o-Rg==)
6. [tuni.fi](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzVbKquTwRtt6nCg3v3rheJb1L-AsN_Afnr-HExl93w7edRRWugPmoopTE9_BYtQYsbYCdaqx11YEEj2rB0ZuFsEC3BZyYDx8R80aTTD5F4BC1J7mlAQLWfEEOIGg0ReFGZ6rmLWNdwZz9Q2oJOV3jkGIP1LO9bed-cJUsClTpVdmGmt_DKH-3bJjrAzbpb_0fVhh4Ku4VRpNx4VGUWACcohQG4Jt0z8owIAWEdfaiqoMexmgzGBGbS4jggV0OrUzuH13byuSjdmsu0iyQWuDO8RyK4g6nUZV8ZtvYG4O68aIVtvkEN9IT)
7. [diva-portal.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3aWt_fseAEBsgXEm08Qar3CUvCJu8PO_v8ZigEAD0D3RkcxinJ1BQLdAZpoZZ5keWfo90arregocF9yuxGjmsIakpclUYFXBNFNdGLlmu_PWelPlfL1l3fo3oahpk8D7TajzRFL-HuN8DGKA3zBI_gpjJBZSJ-g==)
8. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUBVFA5Zetzvd8RCXVPNk5AoTupxpAVuedK671hYwPWLi7W5Oect8NUlA6koTEQ69O4t59nUvIml43X8NkHedIfwZU9-B7TXp273nkmw9OuIr7dCn_9qTZMc_ZHfr8g2F99pBtUGWHwon6jXGB6Cv5pCB-Np3W2PVSbtf6HqAsAz9J_BsT0fajEMAUtvnk9xRDXeP2-DIX5ljlNWip0a5biw==)
9. [nyu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGc20YdFMTxry_eEqHLdik3XWzQznRVU9riP9hndW-vVUFjna3bc5qgbIrKgJbdpvuy3U5rJn9KXE0rySl8bx6eT8bA0HHfLEJ1TFONf8J70hjDCoO-suOxenRknGqT9qNzWwmDk8f-cK_XMSX-8bTtLOx6Jc1onBmqDpEB3AM_Rspc-GyrdmHb8HR_tw==)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtW1GpD4K-d6PVtBesp496JHhMFrPfe3fpLXrdoOrHLJsQ9VzXzyioVsbf3zb9CnxHID9I-0PaoOX3nYIZ-h8uaIn_jhhFx5JgihGWXeZHJON5LxKW67DHxkOajcOdU6C-B1zPDsczYfCUFlPMS2EtZqjgNpMWIbxi9vs5ec-DyZGKf7yyplXSkrG3up9Bn6J1MjvT14sfVfgOiGLC6EuRM2eMPhVCwwvh4FDuvgty7Llqrg==)
11. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFOR5fuWyBsgzkSRw4XqPbWrDOLZm7Ksz4U8GuAqoyayJuI0uRFcAtLrGdPfdu80tMMBmaTdI1_gIImrKfQKTHEA2_oxbDva3ubEF639Z9fatQ9ehcdUvlZtf6Uznh0kw1mTSBze4=)
12. [ases.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQET2IgEFAMBEe6bZhcStbadFngPwtyAfKycvZGxMzoQVBvf261gAz6L44aST5EES0ln1pnBRzmeQLJBaONXB5Ntr3bkWxFhPkm7EQ-3WEgG1b1pjVMT1NrEZlfRH1moACkW1-XxvPmBXMLzr2gQAl4mdIkXVDeZM8eDkbiVnTuGgWVwj5iWLZKQX1NWh9SJucOa3bQ=)
13. [dlr.de](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3KdDspC-l07J-et545PXYkeCZtJoBkVSUZ8xCq85y3tmZNO-vBgDnpBBaBiCEM3Q9S3UMfeRjXGTPPXwOw_u4Z-K568MXKQsM1SmFD0YlbdBphIq0RLtu-yNgo1NrPCywTlwjttptSnM_5maJ5Cec6sbaUzhwt0viwKHt5SmFNOSQu6E_YpFtXriyTRgDmysunb63LvrvDMyDtjsonJD_2uALo2z7uQja6_9ZUz2SDb_6c0jZsNHXJs0Ov4x4iu51CnLvVvXaGpa2w1qWc4OKM15ImGs31Cv7P2sxQwyDKIEIDMpswufBbjYqToa9EAVMK7TMv9c=)
14. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdgjb9c6et1C2FFWp4w06Vd85t2YPMAUzYA6grYfpjAyAzagTmyAi4mJYWhXFZGB-ch8BUccIecQmILgKZWeRx4H6QBASudNt0eX7LylVOdJ1P57nGDDTsWSs=)
15. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGilL3zUMUEBoGhx5yjczfi41gOxpjCAj2T3xnZnrQZLmriGBDU-fy84rS08UQ6rIenKbzcYkUA4lG_edNJFeARLeqYhRrY8FnoWlqZIOwEOqvmhABk-QioIT8dZ7zKWMiVeG1zJoxs1Mn8D4_GDowoO2DqkVzfQZpvYyoebypHSTebb42oQsJ7YYvK9m-v2DuYy3LFW5EnAGLr86R74SuKBHabqbLIPDh1NyV8JXmg1pw8fZufnLR4Pc=)
16. [frontiersin.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_kQ5ffGYSSVottJ_RVEACKkHflU1WSPQ9piqQCg18LwiVRdv8eXaLmXU_r18rlW6zrYwmF50fcFk-_RWLJNpppBbf2BQkKm5kcEd-TqrF5apvRCK-OuBwRT42FA9iy7-B8Aei_2Tz2yjIdNKbKoiazVJbJbVmdLG1Mqq19wwtJhhUkbHJEjFMEwRSYXFZSZDkLw==)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGi5AsR4sr2MthBr6cmTjj5AN030yKyR56bSxNA-Yzr4hSoAP-wA9Kj1cP_rYkIA1FNDHBHApwz29RU6j0NWXe-EIBWm3OG3fXjvvsS5OZzRkFveXkXR9Ez2jhL01T2gFXcaMPk2pAKkLNPRQrbPonm1ect6Ndm-D8pEurmcgkd0KYsxxiQo11zklunLgjg9_lhcrJwke4xjGn2m47GUuIQD3cGFl4mI_ratPV5AjA8za32vF1z6j_KG3xlUpvheBfm8rKW2ss_il-pzd7fY54mkOeb1EA_pQ==)
18. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQw8VQmAH5zirfhcGFmLGCMTwRI7ZnLo3W2-KshooNsWk3_0mu3kEtDUN1gCwuMuBCuwrEGMdIPoClGYHHuKzHiJONT_OYgH1j3UHc8R5q6Xl2EhDCLsdrl5qR_zBe)
19. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2G-0X6tlSvYU7IdhH_4SgL3k4LXVz_Lb-7RSWTRAsXplwc4CivROHKO1ebMlBewKoju6nMXqQgqfLbqoaThhcBIQEE1TDA5cAGSxC1udwrUYMeyTNVCJGdaktq2hzkltD-V0E2op1AeSPcLS1JqomlUPk9pVbWaMnM_s1i-P8LGTMpxUi_izjX5GDKSAo856H7pIS1aEeye5BU_fxgUo5dB7LcOTccZ6G2U6xJT5mtS2qKibue9kcrVQTso3BA1wOtU2D3r3AlbKfd-SnqkTPrHBAjuJm4np9C0F5CvhejeILIJJzf1Y=)
20. [theiet.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBGhZqjLzqgKFMl4IQhGVfqDpN704k6jykkyeVrlKjqXXXML0E_EQbUMh3ytKR4vrKCQOl5YqTqorlpSAFkxh0y7sHQSRYXti2LFHmFx_astb3DS4kU9488qYyIQCooytfklcfR-as66jYY6aDJDiC5vj3PViuh4RuyZwPdrhPf1rQxA==)
21. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUmsC2ZQUiT8cG8Xeg-GRTn1cDzsIOa2zRSWSIovRvEuIkJsYYyCsWh7roZsK-KX-45sw3PMd6UgyX_-8ylqUObYV_a0SYJsgqy5oXHmlCjQ-Rv7ELCFkyFwfbP-8JDdlyz3PLXCVoW1gLSAbF9hkLpkiRCqG_Qm2YWzVXPBCBc83Vs4pzO95LW8ZISnaK7Ly5nXELk70rmlRZreRu3Q1Sk88w-8uRI9BI_8xkoFqJKRO4UIOcrrJ1HWRZ_Aieb0rmgtp7dvVhW0vQ6Q6h6w==)
22. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8jdDMz3Ix24HcWScDXYixaYs7ecM--55WvPJo48Foh-ZhnBKqCykjEj72QcYZAz9MaVWZRczfAyv_Y092uSbMu_F-DfOmiEFiGvXdUYBB26mqNStUp1x_0BZ91aA=)
23. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7vBGFTjfddOt_9vmNI31Lp_bDW8_oJYArk8dPP5tXn1b61-v_XBUHaUN2fDga9ho_yio87bjAn2EYPJpSY4kKk8NbT2WNiyENzhO0Z5x6yyc6oQmUTvwQ8QgmNTjFW4c=)
24. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgZw3Ukxi-1EaeooJ4cyEl3H1Ot-OS2ms0nvC7VZtJivQX1suLMRB5iFweQvupjynoJLGxT-cDHhL9pGxDcsN8zZZH2WMQ3b7fODPM0lAoNtUO80S-V0TBn8V9vgzeIa6gWY22Xo8HenEvtJWnQD8Vn6_T-Dd25EBVFSK4vlftPPvpn2AyYxG4LA==)
25. [nd.edu.au](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsAGsSZIxDCeEIH1PHe4xulmM8HksDewX6N01Cj34ZTKN4nKXA_LO0KU3Cg7YWHf5lHDDeOW2PpuzVd21IrVMOfZtrKfYLJmXwyFWEVA9GoVtkBGr_wC8RKLINydn0iFRPW3hbS3NlG5OdWDmWTgdb81bWV0hlRrTbDihflnyaNrtirfQmnWOrcTI=)
26. [copernicus.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_Lqa_tw64TqacdRM2twMU_9sWZ0ITt6WocSL5O3kaz7gfE35WZQYZRuXgbnhAzpMxTrOv__KPRH99wJZWdBlqLc_Y9eos7ArDcNp9S21jsfCurw39H0_LKaorgjyNl9s1voMoPRTFL1fwSenKsKcUylyWy7MWnUDolg==)
27. [copernicus.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzAlJbKJpvrXu6FarWIjBIDYhnUgi-xjITGL0Sc4t1FZQ3ESu_iHKzgAqMx-kJYMMO_50yPLuGguoZ2R6rksBte-HpjAY7lQRkZJDPwRpcExTVEjlNFXKo4BVBRhpADshXF83qfG0=)
28. [diva-portal.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxyBdWv6zfkY-aPWr9e74iEmL46CYh4KZgeVN4K8Yj4erczwBF98H3NX1m30iXLlwNIM46OljSYs4xNdA_p5zwhZBB3YT35BE-tP7SvxvaKsWv883JHUJMM_tVnJIlBbuS0sDsG6jE0Am39bUQYbrh51H3)
29. [minarjournal.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFphjvg9lQy2vxFdWsO7HwVdlS73RiuObp8cEHayJmCkm4dnvGo9fZgqbh1rzgmhkpO53bwgdxTZJHWluAdXGzR0iIwH1CxY47FJUfbwkfwc2lkY_KuiTKvoeDljBYVrZZ_N858awoFZgwZvuiRV43iyiULYu7yeuip9fuR4NlRqxcOv5-QwhWG9ErKz7WEDeWeRgi2demHuDk4r2hLAbpbwGKYzNeo)
30. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPnBejBe52ej19Im9xdz1nF-Wph6lrqGDVFuj387Ve4bF76bcFdrsfHQjS0jpSJBP6-0NymJCunRssA65g1SkQ1NrFGbILPVumiXPReGQWyAEdZ2hI1A6JysRjAADBwekKnYqsUbjWVo83VLUIoYjvOpaJsSReQGLfccdr8FPmRZMMrkkNiIsHtR-4Bge2d7t1t-yhDelq42cRvTv7148ciE_j2sURhEFLgAlSV9E66D6Fa6foGJvrsfHLCA==)
31. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpqPs3z1o3pSBmvwN8LkyIQ6eJ0hry8Dl0ByMvXIKsJBod8OUjRvX1i0oc3sansvMaXMRdHmSfIEuGgsZp5ysPVTPIX1v_u3oOoLcw7EXTZFdbCyQgEuwvfJHYwg==)
32. [core.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHq29hl-DsdDZNoodGAav93Mf0jJar7YjTlTUlJ92LJKVKiNbVl5ez2FdN6rI-tMOMeF2z5QaVr2O7cqKd3TOdVsC7GXstSzGF7_nJ1Uvv5ovgTea0-HZvC0E62jV74BSJpVA==)
33. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuMvTwzBhrC43U9SF824v1uNHbfSlBrXKFAiSt11ZzwBf7cef2H68kRP6MliVUxQqz0GJzAECj2vAjveGClBJ_a7L7I8GoFeIioTI1OzlsaRuTAAm1zWeZNQgrhQ==)
34. [nrel.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuGZPwlCjxIZ_StJbnWdvw03qe14FuBGsT0mtUUI9-3ZL9VgJHzV2rMsjovQdzIwSWfPYax06p_c2hk86PqEp-hpjNgNdrmB0Bc_izk2WD6WWiWkm5fj6XkEwkgaN3cY687Q==)
35. [tandfonline.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQZzARlq_BS8baXbVazLy5HHLDzuyNk-sxU7Oazw0xQxnLiBwecFFyz--AdipfrgNrQ8mZNWlGP1Ep2vtHFmDWyuLi-9GCfqR0t0XgfZE6LCocFEgHIvOIFtzJcWfQFt2t7SBGN5XP5W_xB1PdhrLxeoD0da2ExQ==)
36. [cedia.edu.ec](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnrOv-WcnolfENigNAQ1gabLjD1BldU-wIruiZLEPy-r1nwc3n1_yjm-kUUndVLB4jRWeF6Qm0m0pbHceaX3NL3m01QhIFNkLcXUKpFb2L9DUuUL_6XTYexLdz-K1-)
37. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7Xf7tNPzwiSs7pt2IVZFMgOZpAsTzAknsF9QMmAjO2gW4eDN_cjSfIQ8dimBRTIRVnxmmCSIOtR-AvRdD3aJAaF89ykbtbqtaXDBR6gOfn85hRBY4pIniEG9aEEHdiuY2y0nrExA0sjJZsEuILFjJrsH2_LrruvgNnlkT4MLJnGKXcM2OaFJjJuBBxoZ1vNuhJcTzVyA5JS43DM897C9jJnAULal2Lw2d--B6pLyJhs-2gWkI0pN4TaVokJByzGxIHCfqpaF-2fuNO4Xmv2zdOvOxGA-twMqJ-do7iwU40j3mAJ9XRZasQuLoiYMDMUdH_qWA)


## Annotations
Annotation(end_index=600, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRQK7YRz1oWGmszgo9HRgbWnGziO-hLGqizCFq6hgVcnT43Gbewm3UCW4jiz_ZHF9QE31g5FL6J39Z0-ezgwSjZsJjj7OxMdbnY1aBO10OJ-1oMlEYbd13jHokVX1BZKfectgThhV3-lvdSXLNucBxINI32p94C7itB2olVRj6onMG55DeZ5W0OTODLgobmD4=', start_index=588)
Annotation(end_index=600, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyl_bl4qlFTXVdU3SjmUkACoj1c94p2-OQIdYcDlUGwa1kYVNbih6eRCMEl2GLPMRbBSN0IPD852aIss1TDyuYq7k413wU3rgCjG1bnMvMNq51Jhd30Zyq_oU=', start_index=588)
Annotation(end_index=832, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-7qrXs2jKR1cllDr45GnfkoOqANiOtfkxPoPnVKB1SfvsxCwK4s38OHybKgmBWCGYfxmgBXSSqwNW1rp7oZ0aFkZuXjcJLKUiOIp3H4welKfXxKDSfUVLUVthUR_A2w==', start_index=820)
Annotation(end_index=832, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjafMX98mnGtYGEXhCumceNxr_vDkAXfMTfGY4sFOT-3BliXpFKOYvJqwDNa4zYMnkk8QJoR_TR-Yscnh38fA03iACDS3PzooDEwNjocMBRiNeZFFMSy2ZEk0iRRXJ1VOa7QI4c5eahf23_-MolNUpE1Y=', start_index=820)
Annotation(end_index=1088, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBRAnQRx7lUsF5zi0CRKqV84zfOE3rSTNMa5IDG1Gi9kRqhP5Q0KCRLbDO2E7jWDmqoAc30CNRaQHv3W7LX2F-_pHiBtqbi0xP-5jVvXjh7EWCod4Ha9ITD1o-Rg==', start_index=1076)
Annotation(end_index=1088, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzVbKquTwRtt6nCg3v3rheJb1L-AsN_Afnr-HExl93w7edRRWugPmoopTE9_BYtQYsbYCdaqx11YEEj2rB0ZuFsEC3BZyYDx8R80aTTD5F4BC1J7mlAQLWfEEOIGg0ReFGZ6rmLWNdwZz9Q2oJOV3jkGIP1LO9bed-cJUsClTpVdmGmt_DKH-3bJjrAzbpb_0fVhh4Ku4VRpNx4VGUWACcohQG4Jt0z8owIAWEdfaiqoMexmgzGBGbS4jggV0OrUzuH13byuSjdmsu0iyQWuDO8RyK4g6nUZV8ZtvYG4O68aIVtvkEN9IT', start_index=1076)
Annotation(end_index=1413, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3aWt_fseAEBsgXEm08Qar3CUvCJu8PO_v8ZigEAD0D3RkcxinJ1BQLdAZpoZZ5keWfo90arregocF9yuxGjmsIakpclUYFXBNFNdGLlmu_PWelPlfL1l3fo3oahpk8D7TajzRFL-HuN8DGKA3zBI_gpjJBZSJ-g==', start_index=1401)
Annotation(end_index=1413, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyl_bl4qlFTXVdU3SjmUkACoj1c94p2-OQIdYcDlUGwa1kYVNbih6eRCMEl2GLPMRbBSN0IPD852aIss1TDyuYq7k413wU3rgCjG1bnMvMNq51Jhd30Zyq_oU=', start_index=1401)
Annotation(end_index=1775, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGc20YdFMTxry_eEqHLdik3XWzQznRVU9riP9hndW-vVUFjna3bc5qgbIrKgJbdpvuy3U5rJn9KXE0rySl8bx6eT8bA0HHfLEJ1TFONf8J70hjDCoO-suOxenRknGqT9qNzWwmDk8f-cK_XMSX-8bTtLOx6Jc1onBmqDpEB3AM_Rspc-GyrdmHb8HR_tw==', start_index=1763)
Annotation(end_index=1775, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUBVFA5Zetzvd8RCXVPNk5AoTupxpAVuedK671hYwPWLi7W5Oect8NUlA6koTEQ69O4t59nUvIml43X8NkHedIfwZU9-B7TXp273nkmw9OuIr7dCn_9qTZMc_ZHfr8g2F99pBtUGWHwon6jXGB6Cv5pCB-Np3W2PVSbtf6HqAsAz9J_BsT0fajEMAUtvnk9xRDXeP2-DIX5ljlNWip0a5biw==', start_index=1763)
Annotation(end_index=4262, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFOR5fuWyBsgzkSRw4XqPbWrDOLZm7Ksz4U8GuAqoyayJuI0uRFcAtLrGdPfdu80tMMBmaTdI1_gIImrKfQKTHEA2_oxbDva3ubEF639Z9fatQ9ehcdUvlZtf6Uznh0kw1mTSBze4=', start_index=4248)
Annotation(end_index=4262, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtW1GpD4K-d6PVtBesp496JHhMFrPfe3fpLXrdoOrHLJsQ9VzXzyioVsbf3zb9CnxHID9I-0PaoOX3nYIZ-h8uaIn_jhhFx5JgihGWXeZHJON5LxKW67DHxkOajcOdU6C-B1zPDsczYfCUFlPMS2EtZqjgNpMWIbxi9vs5ec-DyZGKf7yyplXSkrG3up9Bn6J1MjvT14sfVfgOiGLC6EuRM2eMPhVCwwvh4FDuvgty7Llqrg==', start_index=4248)
Annotation(end_index=4540, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQET2IgEFAMBEe6bZhcStbadFngPwtyAfKycvZGxMzoQVBvf261gAz6L44aST5EES0ln1pnBRzmeQLJBaONXB5Ntr3bkWxFhPkm7EQ-3WEgG1b1pjVMT1NrEZlfRH1moACkW1-XxvPmBXMLzr2gQAl4mdIkXVDeZM8eDkbiVnTuGgWVwj5iWLZKQX1NWh9SJucOa3bQ=', start_index=4526)
Annotation(end_index=4540, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3KdDspC-l07J-et545PXYkeCZtJoBkVSUZ8xCq85y3tmZNO-vBgDnpBBaBiCEM3Q9S3UMfeRjXGTPPXwOw_u4Z-K568MXKQsM1SmFD0YlbdBphIq0RLtu-yNgo1NrPCywTlwjttptSnM_5maJ5Cec6sbaUzhwt0viwKHt5SmFNOSQu6E_YpFtXriyTRgDmysunb63LvrvDMyDtjsonJD_2uALo2z7uQja6_9ZUz2SDb_6c0jZsNHXJs0Ov4x4iu51CnLvVvXaGpa2w1qWc4OKM15ImGs31Cv7P2sxQwyDKIEIDMpswufBbjYqToa9EAVMK7TMv9c=', start_index=4526)
Annotation(end_index=4838, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGc20YdFMTxry_eEqHLdik3XWzQznRVU9riP9hndW-vVUFjna3bc5qgbIrKgJbdpvuy3U5rJn9KXE0rySl8bx6eT8bA0HHfLEJ1TFONf8J70hjDCoO-suOxenRknGqT9qNzWwmDk8f-cK_XMSX-8bTtLOx6Jc1onBmqDpEB3AM_Rspc-GyrdmHb8HR_tw==', start_index=4826)
Annotation(end_index=4838, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUBVFA5Zetzvd8RCXVPNk5AoTupxpAVuedK671hYwPWLi7W5Oect8NUlA6koTEQ69O4t59nUvIml43X8NkHedIfwZU9-B7TXp273nkmw9OuIr7dCn_9qTZMc_ZHfr8g2F99pBtUGWHwon6jXGB6Cv5pCB-Np3W2PVSbtf6HqAsAz9J_BsT0fajEMAUtvnk9xRDXeP2-DIX5ljlNWip0a5biw==', start_index=4826)
Annotation(end_index=5391, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-7qrXs2jKR1cllDr45GnfkoOqANiOtfkxPoPnVKB1SfvsxCwK4s38OHybKgmBWCGYfxmgBXSSqwNW1rp7oZ0aFkZuXjcJLKUiOIp3H4welKfXxKDSfUVLUVthUR_A2w==', start_index=5378)
Annotation(end_index=5391, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdgjb9c6et1C2FFWp4w06Vd85t2YPMAUzYA6grYfpjAyAzagTmyAi4mJYWhXFZGB-ch8BUccIecQmILgKZWeRx4H6QBASudNt0eX7LylVOdJ1P57nGDDTsWSs=', start_index=5378)
Annotation(end_index=5647, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGilL3zUMUEBoGhx5yjczfi41gOxpjCAj2T3xnZnrQZLmriGBDU-fy84rS08UQ6rIenKbzcYkUA4lG_edNJFeARLeqYhRrY8FnoWlqZIOwEOqvmhABk-QioIT8dZ7zKWMiVeG1zJoxs1Mn8D4_GDowoO2DqkVzfQZpvYyoebypHSTebb42oQsJ7YYvK9m-v2DuYy3LFW5EnAGLr86R74SuKBHabqbLIPDh1NyV8JXmg1pw8fZufnLR4Pc=', start_index=5634)
Annotation(end_index=5647, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRQK7YRz1oWGmszgo9HRgbWnGziO-hLGqizCFq6hgVcnT43Gbewm3UCW4jiz_ZHF9QE31g5FL6J39Z0-ezgwSjZsJjj7OxMdbnY1aBO10OJ-1oMlEYbd13jHokVX1BZKfectgThhV3-lvdSXLNucBxINI32p94C7itB2olVRj6onMG55DeZ5W0OTODLgobmD4=', start_index=5634)
Annotation(end_index=5992, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-7qrXs2jKR1cllDr45GnfkoOqANiOtfkxPoPnVKB1SfvsxCwK4s38OHybKgmBWCGYfxmgBXSSqwNW1rp7oZ0aFkZuXjcJLKUiOIp3H4welKfXxKDSfUVLUVthUR_A2w==', start_index=5983)
Annotation(end_index=6514, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_kQ5ffGYSSVottJ_RVEACKkHflU1WSPQ9piqQCg18LwiVRdv8eXaLmXU_r18rlW6zrYwmF50fcFk-_RWLJNpppBbf2BQkKm5kcEd-TqrF5apvRCK-OuBwRT42FA9iy7-B8Aei_2Tz2yjIdNKbKoiazVJbJbVmdLG1Mqq19wwtJhhUkbHJEjFMEwRSYXFZSZDkLw==', start_index=6501)
Annotation(end_index=6514, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjafMX98mnGtYGEXhCumceNxr_vDkAXfMTfGY4sFOT-3BliXpFKOYvJqwDNa4zYMnkk8QJoR_TR-Yscnh38fA03iACDS3PzooDEwNjocMBRiNeZFFMSy2ZEk0iRRXJ1VOa7QI4c5eahf23_-MolNUpE1Y=', start_index=6501)
Annotation(end_index=6843, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGi5AsR4sr2MthBr6cmTjj5AN030yKyR56bSxNA-Yzr4hSoAP-wA9Kj1cP_rYkIA1FNDHBHApwz29RU6j0NWXe-EIBWm3OG3fXjvvsS5OZzRkFveXkXR9Ez2jhL01T2gFXcaMPk2pAKkLNPRQrbPonm1ect6Ndm-D8pEurmcgkd0KYsxxiQo11zklunLgjg9_lhcrJwke4xjGn2m47GUuIQD3cGFl4mI_ratPV5AjA8za32vF1z6j_KG3xlUpvheBfm8rKW2ss_il-pzd7fY54mkOeb1EA_pQ==', start_index=6830)
Annotation(end_index=6843, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjafMX98mnGtYGEXhCumceNxr_vDkAXfMTfGY4sFOT-3BliXpFKOYvJqwDNa4zYMnkk8QJoR_TR-Yscnh38fA03iACDS3PzooDEwNjocMBRiNeZFFMSy2ZEk0iRRXJ1VOa7QI4c5eahf23_-MolNUpE1Y=', start_index=6830)
Annotation(end_index=7180, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQw8VQmAH5zirfhcGFmLGCMTwRI7ZnLo3W2-KshooNsWk3_0mu3kEtDUN1gCwuMuBCuwrEGMdIPoClGYHHuKzHiJONT_OYgH1j3UHc8R5q6Xl2EhDCLsdrl5qR_zBe', start_index=7170)
Annotation(end_index=7370, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2G-0X6tlSvYU7IdhH_4SgL3k4LXVz_Lb-7RSWTRAsXplwc4CivROHKO1ebMlBewKoju6nMXqQgqfLbqoaThhcBIQEE1TDA5cAGSxC1udwrUYMeyTNVCJGdaktq2hzkltD-V0E2op1AeSPcLS1JqomlUPk9pVbWaMnM_s1i-P8LGTMpxUi_izjX5GDKSAo856H7pIS1aEeye5BU_fxgUo5dB7LcOTccZ6G2U6xJT5mtS2qKibue9kcrVQTso3BA1wOtU2D3r3AlbKfd-SnqkTPrHBAjuJm4np9C0F5CvhejeILIJJzf1Y=', start_index=7357)
Annotation(end_index=7370, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzVbKquTwRtt6nCg3v3rheJb1L-AsN_Afnr-HExl93w7edRRWugPmoopTE9_BYtQYsbYCdaqx11YEEj2rB0ZuFsEC3BZyYDx8R80aTTD5F4BC1J7mlAQLWfEEOIGg0ReFGZ6rmLWNdwZz9Q2oJOV3jkGIP1LO9bed-cJUsClTpVdmGmt_DKH-3bJjrAzbpb_0fVhh4Ku4VRpNx4VGUWACcohQG4Jt0z8owIAWEdfaiqoMexmgzGBGbS4jggV0OrUzuH13byuSjdmsu0iyQWuDO8RyK4g6nUZV8ZtvYG4O68aIVtvkEN9IT', start_index=7357)
Annotation(end_index=7980, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRQK7YRz1oWGmszgo9HRgbWnGziO-hLGqizCFq6hgVcnT43Gbewm3UCW4jiz_ZHF9QE31g5FL6J39Z0-ezgwSjZsJjj7OxMdbnY1aBO10OJ-1oMlEYbd13jHokVX1BZKfectgThhV3-lvdSXLNucBxINI32p94C7itB2olVRj6onMG55DeZ5W0OTODLgobmD4=', start_index=7968)
Annotation(end_index=7980, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyl_bl4qlFTXVdU3SjmUkACoj1c94p2-OQIdYcDlUGwa1kYVNbih6eRCMEl2GLPMRbBSN0IPD852aIss1TDyuYq7k413wU3rgCjG1bnMvMNq51Jhd30Zyq_oU=', start_index=7968)
Annotation(end_index=8453, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBGhZqjLzqgKFMl4IQhGVfqDpN704k6jykkyeVrlKjqXXXML0E_EQbUMh3ytKR4vrKCQOl5YqTqorlpSAFkxh0y7sHQSRYXti2LFHmFx_astb3DS4kU9488qYyIQCooytfklcfR-as66jYY6aDJDiC5vj3PViuh4RuyZwPdrhPf1rQxA==', start_index=8440)
Annotation(end_index=8453, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRQK7YRz1oWGmszgo9HRgbWnGziO-hLGqizCFq6hgVcnT43Gbewm3UCW4jiz_ZHF9QE31g5FL6J39Z0-ezgwSjZsJjj7OxMdbnY1aBO10OJ-1oMlEYbd13jHokVX1BZKfectgThhV3-lvdSXLNucBxINI32p94C7itB2olVRj6onMG55DeZ5W0OTODLgobmD4=', start_index=8440)
Annotation(end_index=9087, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUmsC2ZQUiT8cG8Xeg-GRTn1cDzsIOa2zRSWSIovRvEuIkJsYYyCsWh7roZsK-KX-45sw3PMd6UgyX_-8ylqUObYV_a0SYJsgqy5oXHmlCjQ-Rv7ELCFkyFwfbP-8JDdlyz3PLXCVoW1gLSAbF9hkLpkiRCqG_Qm2YWzVXPBCBc83Vs4pzO95LW8ZISnaK7Ly5nXELk70rmlRZreRu3Q1Sk88w-8uRI9BI_8xkoFqJKRO4UIOcrrJ1HWRZ_Aieb0rmgtp7dvVhW0vQ6Q6h6w==', start_index=9074)
Annotation(end_index=9087, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyl_bl4qlFTXVdU3SjmUkACoj1c94p2-OQIdYcDlUGwa1kYVNbih6eRCMEl2GLPMRbBSN0IPD852aIss1TDyuYq7k413wU3rgCjG1bnMvMNq51Jhd30Zyq_oU=', start_index=9074)
Annotation(end_index=9405, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8jdDMz3Ix24HcWScDXYixaYs7ecM--55WvPJo48Foh-ZhnBKqCykjEj72QcYZAz9MaVWZRczfAyv_Y092uSbMu_F-DfOmiEFiGvXdUYBB26mqNStUp1x_0BZ91aA=', start_index=9395)
Annotation(end_index=9615, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3aWt_fseAEBsgXEm08Qar3CUvCJu8PO_v8ZigEAD0D3RkcxinJ1BQLdAZpoZZ5keWfo90arregocF9yuxGjmsIakpclUYFXBNFNdGLlmu_PWelPlfL1l3fo3oahpk8D7TajzRFL-HuN8DGKA3zBI_gpjJBZSJ-g==', start_index=9603)
Annotation(end_index=9615, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyl_bl4qlFTXVdU3SjmUkACoj1c94p2-OQIdYcDlUGwa1kYVNbih6eRCMEl2GLPMRbBSN0IPD852aIss1TDyuYq7k413wU3rgCjG1bnMvMNq51Jhd30Zyq_oU=', start_index=9603)
Annotation(end_index=10068, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRQK7YRz1oWGmszgo9HRgbWnGziO-hLGqizCFq6hgVcnT43Gbewm3UCW4jiz_ZHF9QE31g5FL6J39Z0-ezgwSjZsJjj7OxMdbnY1aBO10OJ-1oMlEYbd13jHokVX1BZKfectgThhV3-lvdSXLNucBxINI32p94C7itB2olVRj6onMG55DeZ5W0OTODLgobmD4=', start_index=10055)
Annotation(end_index=10068, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdgjb9c6et1C2FFWp4w06Vd85t2YPMAUzYA6grYfpjAyAzagTmyAi4mJYWhXFZGB-ch8BUccIecQmILgKZWeRx4H6QBASudNt0eX7LylVOdJ1P57nGDDTsWSs=', start_index=10055)
Annotation(end_index=10302, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBRAnQRx7lUsF5zi0CRKqV84zfOE3rSTNMa5IDG1Gi9kRqhP5Q0KCRLbDO2E7jWDmqoAc30CNRaQHv3W7LX2F-_pHiBtqbi0xP-5jVvXjh7EWCod4Ha9ITD1o-Rg==', start_index=10289)
Annotation(end_index=10302, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7vBGFTjfddOt_9vmNI31Lp_bDW8_oJYArk8dPP5tXn1b61-v_XBUHaUN2fDga9ho_yio87bjAn2EYPJpSY4kKk8NbT2WNiyENzhO0Z5x6yyc6oQmUTvwQ8QgmNTjFW4c=', start_index=10289)
Annotation(end_index=10974, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEFOR5fuWyBsgzkSRw4XqPbWrDOLZm7Ksz4U8GuAqoyayJuI0uRFcAtLrGdPfdu80tMMBmaTdI1_gIImrKfQKTHEA2_oxbDva3ubEF639Z9fatQ9ehcdUvlZtf6Uznh0kw1mTSBze4=', start_index=10956)
Annotation(end_index=10974, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgZw3Ukxi-1EaeooJ4cyEl3H1Ot-OS2ms0nvC7VZtJivQX1suLMRB5iFweQvupjynoJLGxT-cDHhL9pGxDcsN8zZZH2WMQ3b7fODPM0lAoNtUO80S-V0TBn8V9vgzeIa6gWY22Xo8HenEvtJWnQD8Vn6_T-Dd25EBVFSK4vlftPPvpn2AyYxG4LA==', start_index=10956)
Annotation(end_index=10974, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtW1GpD4K-d6PVtBesp496JHhMFrPfe3fpLXrdoOrHLJsQ9VzXzyioVsbf3zb9CnxHID9I-0PaoOX3nYIZ-h8uaIn_jhhFx5JgihGWXeZHJON5LxKW67DHxkOajcOdU6C-B1zPDsczYfCUFlPMS2EtZqjgNpMWIbxi9vs5ec-DyZGKf7yyplXSkrG3up9Bn6J1MjvT14sfVfgOiGLC6EuRM2eMPhVCwwvh4FDuvgty7Llqrg==', start_index=10956)
Annotation(end_index=11355, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsAGsSZIxDCeEIH1PHe4xulmM8HksDewX6N01Cj34ZTKN4nKXA_LO0KU3Cg7YWHf5lHDDeOW2PpuzVd21IrVMOfZtrKfYLJmXwyFWEVA9GoVtkBGr_wC8RKLINydn0iFRPW3hbS3NlG5OdWDmWTgdb81bWV0hlRrTbDihflnyaNrtirfQmnWOrcTI=', start_index=11341)
Annotation(end_index=11355, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtW1GpD4K-d6PVtBesp496JHhMFrPfe3fpLXrdoOrHLJsQ9VzXzyioVsbf3zb9CnxHID9I-0PaoOX3nYIZ-h8uaIn_jhhFx5JgihGWXeZHJON5LxKW67DHxkOajcOdU6C-B1zPDsczYfCUFlPMS2EtZqjgNpMWIbxi9vs5ec-DyZGKf7yyplXSkrG3up9Bn6J1MjvT14sfVfgOiGLC6EuRM2eMPhVCwwvh4FDuvgty7Llqrg==', start_index=11341)
Annotation(end_index=11607, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgZw3Ukxi-1EaeooJ4cyEl3H1Ot-OS2ms0nvC7VZtJivQX1suLMRB5iFweQvupjynoJLGxT-cDHhL9pGxDcsN8zZZH2WMQ3b7fODPM0lAoNtUO80S-V0TBn8V9vgzeIa6gWY22Xo8HenEvtJWnQD8Vn6_T-Dd25EBVFSK4vlftPPvpn2AyYxG4LA==', start_index=11593)
Annotation(end_index=11607, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtW1GpD4K-d6PVtBesp496JHhMFrPfe3fpLXrdoOrHLJsQ9VzXzyioVsbf3zb9CnxHID9I-0PaoOX3nYIZ-h8uaIn_jhhFx5JgihGWXeZHJON5LxKW67DHxkOajcOdU6C-B1zPDsczYfCUFlPMS2EtZqjgNpMWIbxi9vs5ec-DyZGKf7yyplXSkrG3up9Bn6J1MjvT14sfVfgOiGLC6EuRM2eMPhVCwwvh4FDuvgty7Llqrg==', start_index=11593)
Annotation(end_index=11939, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF_Lqa_tw64TqacdRM2twMU_9sWZ0ITt6WocSL5O3kaz7gfE35WZQYZRuXgbnhAzpMxTrOv__KPRH99wJZWdBlqLc_Y9eos7ArDcNp9S21jsfCurw39H0_LKaorgjyNl9s1voMoPRTFL1fwSenKsKcUylyWy7MWnUDolg==', start_index=11925)
Annotation(end_index=11939, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzAlJbKJpvrXu6FarWIjBIDYhnUgi-xjITGL0Sc4t1FZQ3ESu_iHKzgAqMx-kJYMMO_50yPLuGguoZ2R6rksBte-HpjAY7lQRkZJDPwRpcExTVEjlNFXKo4BVBRhpADshXF83qfG0=', start_index=11925)
Annotation(end_index=12528, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGc20YdFMTxry_eEqHLdik3XWzQznRVU9riP9hndW-vVUFjna3bc5qgbIrKgJbdpvuy3U5rJn9KXE0rySl8bx6eT8bA0HHfLEJ1TFONf8J70hjDCoO-suOxenRknGqT9qNzWwmDk8f-cK_XMSX-8bTtLOx6Jc1onBmqDpEB3AM_Rspc-GyrdmHb8HR_tw==', start_index=12516)
Annotation(end_index=12528, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUBVFA5Zetzvd8RCXVPNk5AoTupxpAVuedK671hYwPWLi7W5Oect8NUlA6koTEQ69O4t59nUvIml43X8NkHedIfwZU9-B7TXp273nkmw9OuIr7dCn_9qTZMc_ZHfr8g2F99pBtUGWHwon6jXGB6Cv5pCB-Np3W2PVSbtf6HqAsAz9J_BsT0fajEMAUtvnk9xRDXeP2-DIX5ljlNWip0a5biw==', start_index=12516)
Annotation(end_index=13615, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxyBdWv6zfkY-aPWr9e74iEmL46CYh4KZgeVN4K8Yj4erczwBF98H3NX1m30iXLlwNIM46OljSYs4xNdA_p5zwhZBB3YT35BE-tP7SvxvaKsWv883JHUJMM_tVnJIlBbuS0sDsG6jE0Am39bUQYbrh51H3', start_index=13602)
Annotation(end_index=13615, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyl_bl4qlFTXVdU3SjmUkACoj1c94p2-OQIdYcDlUGwa1kYVNbih6eRCMEl2GLPMRbBSN0IPD852aIss1TDyuYq7k413wU3rgCjG1bnMvMNq51Jhd30Zyq_oU=', start_index=13602)
Annotation(end_index=13926, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3aWt_fseAEBsgXEm08Qar3CUvCJu8PO_v8ZigEAD0D3RkcxinJ1BQLdAZpoZZ5keWfo90arregocF9yuxGjmsIakpclUYFXBNFNdGLlmu_PWelPlfL1l3fo3oahpk8D7TajzRFL-HuN8DGKA3zBI_gpjJBZSJ-g==', start_index=13914)
Annotation(end_index=13926, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyl_bl4qlFTXVdU3SjmUkACoj1c94p2-OQIdYcDlUGwa1kYVNbih6eRCMEl2GLPMRbBSN0IPD852aIss1TDyuYq7k413wU3rgCjG1bnMvMNq51Jhd30Zyq_oU=', start_index=13914)
Annotation(end_index=14180, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3aWt_fseAEBsgXEm08Qar3CUvCJu8PO_v8ZigEAD0D3RkcxinJ1BQLdAZpoZZ5keWfo90arregocF9yuxGjmsIakpclUYFXBNFNdGLlmu_PWelPlfL1l3fo3oahpk8D7TajzRFL-HuN8DGKA3zBI_gpjJBZSJ-g==', start_index=14168)
Annotation(end_index=14180, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyl_bl4qlFTXVdU3SjmUkACoj1c94p2-OQIdYcDlUGwa1kYVNbih6eRCMEl2GLPMRbBSN0IPD852aIss1TDyuYq7k413wU3rgCjG1bnMvMNq51Jhd30Zyq_oU=', start_index=14168)
Annotation(end_index=15027, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRQK7YRz1oWGmszgo9HRgbWnGziO-hLGqizCFq6hgVcnT43Gbewm3UCW4jiz_ZHF9QE31g5FL6J39Z0-ezgwSjZsJjj7OxMdbnY1aBO10OJ-1oMlEYbd13jHokVX1BZKfectgThhV3-lvdSXLNucBxINI32p94C7itB2olVRj6onMG55DeZ5W0OTODLgobmD4=', start_index=15014)
Annotation(end_index=15027, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdgjb9c6et1C2FFWp4w06Vd85t2YPMAUzYA6grYfpjAyAzagTmyAi4mJYWhXFZGB-ch8BUccIecQmILgKZWeRx4H6QBASudNt0eX7LylVOdJ1P57nGDDTsWSs=', start_index=15014)
Annotation(end_index=15580, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFphjvg9lQy2vxFdWsO7HwVdlS73RiuObp8cEHayJmCkm4dnvGo9fZgqbh1rzgmhkpO53bwgdxTZJHWluAdXGzR0iIwH1CxY47FJUfbwkfwc2lkY_KuiTKvoeDljBYVrZZ_N858awoFZgwZvuiRV43iyiULYu7yeuip9fuR4NlRqxcOv5-QwhWG9ErKz7WEDeWeRgi2demHuDk4r2hLAbpbwGKYzNeo', start_index=15566)
Annotation(end_index=15580, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG_kQ5ffGYSSVottJ_RVEACKkHflU1WSPQ9piqQCg18LwiVRdv8eXaLmXU_r18rlW6zrYwmF50fcFk-_RWLJNpppBbf2BQkKm5kcEd-TqrF5apvRCK-OuBwRT42FA9iy7-B8Aei_2Tz2yjIdNKbKoiazVJbJbVmdLG1Mqq19wwtJhhUkbHJEjFMEwRSYXFZSZDkLw==', start_index=15566)
Annotation(end_index=15961, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjafMX98mnGtYGEXhCumceNxr_vDkAXfMTfGY4sFOT-3BliXpFKOYvJqwDNa4zYMnkk8QJoR_TR-Yscnh38fA03iACDS3PzooDEwNjocMBRiNeZFFMSy2ZEk0iRRXJ1VOa7QI4c5eahf23_-MolNUpE1Y=', start_index=15952)
Annotation(end_index=16306, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGi5AsR4sr2MthBr6cmTjj5AN030yKyR56bSxNA-Yzr4hSoAP-wA9Kj1cP_rYkIA1FNDHBHApwz29RU6j0NWXe-EIBWm3OG3fXjvvsS5OZzRkFveXkXR9Ez2jhL01T2gFXcaMPk2pAKkLNPRQrbPonm1ect6Ndm-D8pEurmcgkd0KYsxxiQo11zklunLgjg9_lhcrJwke4xjGn2m47GUuIQD3cGFl4mI_ratPV5AjA8za32vF1z6j_KG3xlUpvheBfm8rKW2ss_il-pzd7fY54mkOeb1EA_pQ==', start_index=16292)
Annotation(end_index=16306, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPnBejBe52ej19Im9xdz1nF-Wph6lrqGDVFuj387Ve4bF76bcFdrsfHQjS0jpSJBP6-0NymJCunRssA65g1SkQ1NrFGbILPVumiXPReGQWyAEdZ2hI1A6JysRjAADBwekKnYqsUbjWVo83VLUIoYjvOpaJsSReQGLfccdr8FPmRZMMrkkNiIsHtR-4Bge2d7t1t-yhDelq42cRvTv7148ciE_j2sURhEFLgAlSV9E66D6Fa6foGJvrsfHLCA==', start_index=16292)
Annotation(end_index=17200, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpqPs3z1o3pSBmvwN8LkyIQ6eJ0hry8Dl0ByMvXIKsJBod8OUjRvX1i0oc3sansvMaXMRdHmSfIEuGgsZp5ysPVTPIX1v_u3oOoLcw7EXTZFdbCyQgEuwvfJHYwg==', start_index=17190)
Annotation(end_index=17474, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHq29hl-DsdDZNoodGAav93Mf0jJar7YjTlTUlJ92LJKVKiNbVl5ez2FdN6rI-tMOMeF2z5QaVr2O7cqKd3TOdVsC7GXstSzGF7_nJ1Uvv5ovgTea0-HZvC0E62jV74BSJpVA==', start_index=17461)
Annotation(end_index=17474, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzVbKquTwRtt6nCg3v3rheJb1L-AsN_Afnr-HExl93w7edRRWugPmoopTE9_BYtQYsbYCdaqx11YEEj2rB0ZuFsEC3BZyYDx8R80aTTD5F4BC1J7mlAQLWfEEOIGg0ReFGZ6rmLWNdwZz9Q2oJOV3jkGIP1LO9bed-cJUsClTpVdmGmt_DKH-3bJjrAzbpb_0fVhh4Ku4VRpNx4VGUWACcohQG4Jt0z8owIAWEdfaiqoMexmgzGBGbS4jggV0OrUzuH13byuSjdmsu0iyQWuDO8RyK4g6nUZV8ZtvYG4O68aIVtvkEN9IT', start_index=17461)
Annotation(end_index=17991, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuMvTwzBhrC43U9SF824v1uNHbfSlBrXKFAiSt11ZzwBf7cef2H68kRP6MliVUxQqz0GJzAECj2vAjveGClBJ_a7L7I8GoFeIioTI1OzlsaRuTAAm1zWeZNQgrhQ==', start_index=17977)
Annotation(end_index=17991, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuGZPwlCjxIZ_StJbnWdvw03qe14FuBGsT0mtUUI9-3ZL9VgJHzV2rMsjovQdzIwSWfPYax06p_c2hk86PqEp-hpjNgNdrmB0Bc_izk2WD6WWiWkm5fj6XkEwkgaN3cY687Q==', start_index=17977)
Annotation(end_index=18224, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3KdDspC-l07J-et545PXYkeCZtJoBkVSUZ8xCq85y3tmZNO-vBgDnpBBaBiCEM3Q9S3UMfeRjXGTPPXwOw_u4Z-K568MXKQsM1SmFD0YlbdBphIq0RLtu-yNgo1NrPCywTlwjttptSnM_5maJ5Cec6sbaUzhwt0viwKHt5SmFNOSQu6E_YpFtXriyTRgDmysunb63LvrvDMyDtjsonJD_2uALo2z7uQja6_9ZUz2SDb_6c0jZsNHXJs0Ov4x4iu51CnLvVvXaGpa2w1qWc4OKM15ImGs31Cv7P2sxQwyDKIEIDMpswufBbjYqToa9EAVMK7TMv9c=', start_index=18214)
Annotation(end_index=19061, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsAGsSZIxDCeEIH1PHe4xulmM8HksDewX6N01Cj34ZTKN4nKXA_LO0KU3Cg7YWHf5lHDDeOW2PpuzVd21IrVMOfZtrKfYLJmXwyFWEVA9GoVtkBGr_wC8RKLINydn0iFRPW3hbS3NlG5OdWDmWTgdb81bWV0hlRrTbDihflnyaNrtirfQmnWOrcTI=', start_index=19043)
Annotation(end_index=19061, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQZzARlq_BS8baXbVazLy5HHLDzuyNk-sxU7Oazw0xQxnLiBwecFFyz--AdipfrgNrQ8mZNWlGP1Ep2vtHFmDWyuLi-9GCfqR0t0XgfZE6LCocFEgHIvOIFtzJcWfQFt2t7SBGN5XP5W_xB1PdhrLxeoD0da2ExQ==', start_index=19043)
Annotation(end_index=19061, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtW1GpD4K-d6PVtBesp496JHhMFrPfe3fpLXrdoOrHLJsQ9VzXzyioVsbf3zb9CnxHID9I-0PaoOX3nYIZ-h8uaIn_jhhFx5JgihGWXeZHJON5LxKW67DHxkOajcOdU6C-B1zPDsczYfCUFlPMS2EtZqjgNpMWIbxi9vs5ec-DyZGKf7yyplXSkrG3up9Bn6J1MjvT14sfVfgOiGLC6EuRM2eMPhVCwwvh4FDuvgty7Llqrg==', start_index=19043)
Annotation(end_index=19502, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEQw8VQmAH5zirfhcGFmLGCMTwRI7ZnLo3W2-KshooNsWk3_0mu3kEtDUN1gCwuMuBCuwrEGMdIPoClGYHHuKzHiJONT_OYgH1j3UHc8R5q6Xl2EhDCLsdrl5qR_zBe', start_index=19488)
Annotation(end_index=19502, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFBGhZqjLzqgKFMl4IQhGVfqDpN704k6jykkyeVrlKjqXXXML0E_EQbUMh3ytKR4vrKCQOl5YqTqorlpSAFkxh0y7sHQSRYXti2LFHmFx_astb3DS4kU9488qYyIQCooytfklcfR-as66jYY6aDJDiC5vj3PViuh4RuyZwPdrhPf1rQxA==', start_index=19488)
Annotation(end_index=21305, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-7qrXs2jKR1cllDr45GnfkoOqANiOtfkxPoPnVKB1SfvsxCwK4s38OHybKgmBWCGYfxmgBXSSqwNW1rp7oZ0aFkZuXjcJLKUiOIp3H4welKfXxKDSfUVLUVthUR_A2w==', start_index=21293)
Annotation(end_index=21305, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRQK7YRz1oWGmszgo9HRgbWnGziO-hLGqizCFq6hgVcnT43Gbewm3UCW4jiz_ZHF9QE31g5FL6J39Z0-ezgwSjZsJjj7OxMdbnY1aBO10OJ-1oMlEYbd13jHokVX1BZKfectgThhV3-lvdSXLNucBxINI32p94C7itB2olVRj6onMG55DeZ5W0OTODLgobmD4=', start_index=21293)
Annotation(end_index=21712, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-7qrXs2jKR1cllDr45GnfkoOqANiOtfkxPoPnVKB1SfvsxCwK4s38OHybKgmBWCGYfxmgBXSSqwNW1rp7oZ0aFkZuXjcJLKUiOIp3H4welKfXxKDSfUVLUVthUR_A2w==', start_index=21703)
Annotation(end_index=22104, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjafMX98mnGtYGEXhCumceNxr_vDkAXfMTfGY4sFOT-3BliXpFKOYvJqwDNa4zYMnkk8QJoR_TR-Yscnh38fA03iACDS3PzooDEwNjocMBRiNeZFFMSy2ZEk0iRRXJ1VOa7QI4c5eahf23_-MolNUpE1Y=', start_index=22095)
Annotation(end_index=22604, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGi5AsR4sr2MthBr6cmTjj5AN030yKyR56bSxNA-Yzr4hSoAP-wA9Kj1cP_rYkIA1FNDHBHApwz29RU6j0NWXe-EIBWm3OG3fXjvvsS5OZzRkFveXkXR9Ez2jhL01T2gFXcaMPk2pAKkLNPRQrbPonm1ect6Ndm-D8pEurmcgkd0KYsxxiQo11zklunLgjg9_lhcrJwke4xjGn2m47GUuIQD3cGFl4mI_ratPV5AjA8za32vF1z6j_KG3xlUpvheBfm8rKW2ss_il-pzd7fY54mkOeb1EA_pQ==', start_index=22594)
Annotation(end_index=23115, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBRAnQRx7lUsF5zi0CRKqV84zfOE3rSTNMa5IDG1Gi9kRqhP5Q0KCRLbDO2E7jWDmqoAc30CNRaQHv3W7LX2F-_pHiBtqbi0xP-5jVvXjh7EWCod4Ha9ITD1o-Rg==', start_index=23102)
Annotation(end_index=23115, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpqPs3z1o3pSBmvwN8LkyIQ6eJ0hry8Dl0ByMvXIKsJBod8OUjRvX1i0oc3sansvMaXMRdHmSfIEuGgsZp5ysPVTPIX1v_u3oOoLcw7EXTZFdbCyQgEuwvfJHYwg==', start_index=23102)
Annotation(end_index=23351, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGc20YdFMTxry_eEqHLdik3XWzQznRVU9riP9hndW-vVUFjna3bc5qgbIrKgJbdpvuy3U5rJn9KXE0rySl8bx6eT8bA0HHfLEJ1TFONf8J70hjDCoO-suOxenRknGqT9qNzWwmDk8f-cK_XMSX-8bTtLOx6Jc1onBmqDpEB3AM_Rspc-GyrdmHb8HR_tw==', start_index=23339)
Annotation(end_index=23351, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUBVFA5Zetzvd8RCXVPNk5AoTupxpAVuedK671hYwPWLi7W5Oect8NUlA6koTEQ69O4t59nUvIml43X8NkHedIfwZU9-B7TXp273nkmw9OuIr7dCn_9qTZMc_ZHfr8g2F99pBtUGWHwon6jXGB6Cv5pCB-Np3W2PVSbtf6HqAsAz9J_BsT0fajEMAUtvnk9xRDXeP2-DIX5ljlNWip0a5biw==', start_index=23339)
Annotation(end_index=24163, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEnrOv-WcnolfENigNAQ1gabLjD1BldU-wIruiZLEPy-r1nwc3n1_yjm-kUUndVLB4jRWeF6Qm0m0pbHceaX3NL3m01QhIFNkLcXUKpFb2L9DUuUL_6XTYexLdz-K1-', start_index=24149)
Annotation(end_index=24163, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7vBGFTjfddOt_9vmNI31Lp_bDW8_oJYArk8dPP5tXn1b61-v_XBUHaUN2fDga9ho_yio87bjAn2EYPJpSY4kKk8NbT2WNiyENzhO0Z5x6yyc6oQmUTvwQ8QgmNTjFW4c=', start_index=24149)
Annotation(end_index=24411, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuMvTwzBhrC43U9SF824v1uNHbfSlBrXKFAiSt11ZzwBf7cef2H68kRP6MliVUxQqz0GJzAECj2vAjveGClBJ_a7L7I8GoFeIioTI1OzlsaRuTAAm1zWeZNQgrhQ==', start_index=24397)
Annotation(end_index=24411, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG7Xf7tNPzwiSs7pt2IVZFMgOZpAsTzAknsF9QMmAjO2gW4eDN_cjSfIQ8dimBRTIRVnxmmCSIOtR-AvRdD3aJAaF89ykbtbqtaXDBR6gOfn85hRBY4pIniEG9aEEHdiuY2y0nrExA0sjJZsEuILFjJrsH2_LrruvgNnlkT4MLJnGKXcM2OaFJjJuBBxoZ1vNuhJcTzVyA5JS43DM897C9jJnAULal2Lw2d--B6pLyJhs-2gWkI0pN4TaVokJByzGxIHCfqpaF-2fuNO4Xmv2zdOvOxGA-twMqJ-do7iwU40j3mAJ9XRZasQuLoiYMDMUdH_qWA', start_index=24397)
Annotation(end_index=24601, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEgZw3Ukxi-1EaeooJ4cyEl3H1Ot-OS2ms0nvC7VZtJivQX1suLMRB5iFweQvupjynoJLGxT-cDHhL9pGxDcsN8zZZH2WMQ3b7fODPM0lAoNtUO80S-V0TBn8V9vgzeIa6gWY22Xo8HenEvtJWnQD8Vn6_T-Dd25EBVFSK4vlftPPvpn2AyYxG4LA==', start_index=24587)
Annotation(end_index=24601, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtW1GpD4K-d6PVtBesp496JHhMFrPfe3fpLXrdoOrHLJsQ9VzXzyioVsbf3zb9CnxHID9I-0PaoOX3nYIZ-h8uaIn_jhhFx5JgihGWXeZHJON5LxKW67DHxkOajcOdU6C-B1zPDsczYfCUFlPMS2EtZqjgNpMWIbxi9vs5ec-DyZGKf7yyplXSkrG3up9Bn6J1MjvT14sfVfgOiGLC6EuRM2eMPhVCwwvh4FDuvgty7Llqrg==', start_index=24587)
Annotation(end_index=24640, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFQZzARlq_BS8baXbVazLy5HHLDzuyNk-sxU7Oazw0xQxnLiBwecFFyz--AdipfrgNrQ8mZNWlGP1Ep2vtHFmDWyuLi-9GCfqR0t0XgfZE6LCocFEgHIvOIFtzJcWfQFt2t7SBGN5XP5W_xB1PdhrLxeoD0da2ExQ==', start_index=24630)
Annotation(end_index=24708, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsAGsSZIxDCeEIH1PHe4xulmM8HksDewX6N01Cj34ZTKN4nKXA_LO0KU3Cg7YWHf5lHDDeOW2PpuzVd21IrVMOfZtrKfYLJmXwyFWEVA9GoVtkBGr_wC8RKLINydn0iFRPW3hbS3NlG5OdWDmWTgdb81bWV0hlRrTbDihflnyaNrtirfQmnWOrcTI=', start_index=24698)
Annotation(end_index=24782, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQET2IgEFAMBEe6bZhcStbadFngPwtyAfKycvZGxMzoQVBvf261gAz6L44aST5EES0ln1pnBRzmeQLJBaONXB5Ntr3bkWxFhPkm7EQ-3WEgG1b1pjVMT1NrEZlfRH1moACkW1-XxvPmBXMLzr2gQAl4mdIkXVDeZM8eDkbiVnTuGgWVwj5iWLZKQX1NWh9SJucOa3bQ=', start_index=24772)
Annotation(end_index=24843, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtW1GpD4K-d6PVtBesp496JHhMFrPfe3fpLXrdoOrHLJsQ9VzXzyioVsbf3zb9CnxHID9I-0PaoOX3nYIZ-h8uaIn_jhhFx5JgihGWXeZHJON5LxKW67DHxkOajcOdU6C-B1zPDsczYfCUFlPMS2EtZqjgNpMWIbxi9vs5ec-DyZGKf7yyplXSkrG3up9Bn6J1MjvT14sfVfgOiGLC6EuRM2eMPhVCwwvh4FDuvgty7Llqrg==', start_index=24833)
Annotation(end_index=24919, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFdgjb9c6et1C2FFWp4w06Vd85t2YPMAUzYA6grYfpjAyAzagTmyAi4mJYWhXFZGB-ch8BUccIecQmILgKZWeRx4H6QBASudNt0eX7LylVOdJ1P57nGDDTsWSs=', start_index=24909)
Annotation(end_index=24994, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUBVFA5Zetzvd8RCXVPNk5AoTupxpAVuedK671hYwPWLi7W5Oect8NUlA6koTEQ69O4t59nUvIml43X8NkHedIfwZU9-B7TXp273nkmw9OuIr7dCn_9qTZMc_ZHfr8g2F99pBtUGWHwon6jXGB6Cv5pCB-Np3W2PVSbtf6HqAsAz9J_BsT0fajEMAUtvnk9xRDXeP2-DIX5ljlNWip0a5biw==', start_index=24985)
Annotation(end_index=25073, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGc20YdFMTxry_eEqHLdik3XWzQznRVU9riP9hndW-vVUFjna3bc5qgbIrKgJbdpvuy3U5rJn9KXE0rySl8bx6eT8bA0HHfLEJ1TFONf8J70hjDCoO-suOxenRknGqT9qNzWwmDk8f-cK_XMSX-8bTtLOx6Jc1onBmqDpEB3AM_Rspc-GyrdmHb8HR_tw==', start_index=25064)
Annotation(end_index=25129, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-7qrXs2jKR1cllDr45GnfkoOqANiOtfkxPoPnVKB1SfvsxCwK4s38OHybKgmBWCGYfxmgBXSSqwNW1rp7oZ0aFkZuXjcJLKUiOIp3H4welKfXxKDSfUVLUVthUR_A2w==', start_index=25120)
Annotation(end_index=25193, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjafMX98mnGtYGEXhCumceNxr_vDkAXfMTfGY4sFOT-3BliXpFKOYvJqwDNa4zYMnkk8QJoR_TR-Yscnh38fA03iACDS3PzooDEwNjocMBRiNeZFFMSy2ZEk0iRRXJ1VOa7QI4c5eahf23_-MolNUpE1Y=', start_index=25184)
Annotation(end_index=25266, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPnBejBe52ej19Im9xdz1nF-Wph6lrqGDVFuj387Ve4bF76bcFdrsfHQjS0jpSJBP6-0NymJCunRssA65g1SkQ1NrFGbILPVumiXPReGQWyAEdZ2hI1A6JysRjAADBwekKnYqsUbjWVo83VLUIoYjvOpaJsSReQGLfccdr8FPmRZMMrkkNiIsHtR-4Bge2d7t1t-yhDelq42cRvTv7148ciE_j2sURhEFLgAlSV9E66D6Fa6foGJvrsfHLCA==', start_index=25256)
Annotation(end_index=25340, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3KdDspC-l07J-et545PXYkeCZtJoBkVSUZ8xCq85y3tmZNO-vBgDnpBBaBiCEM3Q9S3UMfeRjXGTPPXwOw_u4Z-K568MXKQsM1SmFD0YlbdBphIq0RLtu-yNgo1NrPCywTlwjttptSnM_5maJ5Cec6sbaUzhwt0viwKHt5SmFNOSQu6E_YpFtXriyTRgDmysunb63LvrvDMyDtjsonJD_2uALo2z7uQja6_9ZUz2SDb_6c0jZsNHXJs0Ov4x4iu51CnLvVvXaGpa2w1qWc4OKM15ImGs31Cv7P2sxQwyDKIEIDMpswufBbjYqToa9EAVMK7TMv9c=', start_index=25330)
Annotation(end_index=25405, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRQK7YRz1oWGmszgo9HRgbWnGziO-hLGqizCFq6hgVcnT43Gbewm3UCW4jiz_ZHF9QE31g5FL6J39Z0-ezgwSjZsJjj7OxMdbnY1aBO10OJ-1oMlEYbd13jHokVX1BZKfectgThhV3-lvdSXLNucBxINI32p94C7itB2olVRj6onMG55DeZ5W0OTODLgobmD4=', start_index=25396)
Annotation(end_index=25460, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyl_bl4qlFTXVdU3SjmUkACoj1c94p2-OQIdYcDlUGwa1kYVNbih6eRCMEl2GLPMRbBSN0IPD852aIss1TDyuYq7k413wU3rgCjG1bnMvMNq51Jhd30Zyq_oU=', start_index=25451)
Annotation(end_index=25540, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFxyBdWv6zfkY-aPWr9e74iEmL46CYh4KZgeVN4K8Yj4erczwBF98H3NX1m30iXLlwNIM46OljSYs4xNdA_p5zwhZBB3YT35BE-tP7SvxvaKsWv883JHUJMM_tVnJIlBbuS0sDsG6jE0Am39bUQYbrh51H3', start_index=25530)
Annotation(end_index=25604, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8jdDMz3Ix24HcWScDXYixaYs7ecM--55WvPJo48Foh-ZhnBKqCykjEj72QcYZAz9MaVWZRczfAyv_Y092uSbMu_F-DfOmiEFiGvXdUYBB26mqNStUp1x_0BZ91aA=', start_index=25594)
Annotation(end_index=25672, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBRAnQRx7lUsF5zi0CRKqV84zfOE3rSTNMa5IDG1Gi9kRqhP5Q0KCRLbDO2E7jWDmqoAc30CNRaQHv3W7LX2F-_pHiBtqbi0xP-5jVvXjh7EWCod4Ha9ITD1o-Rg==', start_index=25663)
Annotation(end_index=25736, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpqPs3z1o3pSBmvwN8LkyIQ6eJ0hry8Dl0ByMvXIKsJBod8OUjRvX1i0oc3sansvMaXMRdHmSfIEuGgsZp5ysPVTPIX1v_u3oOoLcw7EXTZFdbCyQgEuwvfJHYwg==', start_index=25726)
Annotation(end_index=25808, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUmsC2ZQUiT8cG8Xeg-GRTn1cDzsIOa2zRSWSIovRvEuIkJsYYyCsWh7roZsK-KX-45sw3PMd6UgyX_-8ylqUObYV_a0SYJsgqy5oXHmlCjQ-Rv7ELCFkyFwfbP-8JDdlyz3PLXCVoW1gLSAbF9hkLpkiRCqG_Qm2YWzVXPBCBc83Vs4pzO95LW8ZISnaK7Ly5nXELk70rmlRZreRu3Q1Sk88w-8uRI9BI_8xkoFqJKRO4UIOcrrJ1HWRZ_Aieb0rmgtp7dvVhW0vQ6Q6h6w==', start_index=25798)
Annotation(end_index=25871, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3aWt_fseAEBsgXEm08Qar3CUvCJu8PO_v8ZigEAD0D3RkcxinJ1BQLdAZpoZZ5keWfo90arregocF9yuxGjmsIakpclUYFXBNFNdGLlmu_PWelPlfL1l3fo3oahpk8D7TajzRFL-HuN8DGKA3zBI_gpjJBZSJ-g==', start_index=25862)
Annotation(end_index=25937, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGi5AsR4sr2MthBr6cmTjj5AN030yKyR56bSxNA-Yzr4hSoAP-wA9Kj1cP_rYkIA1FNDHBHApwz29RU6j0NWXe-EIBWm3OG3fXjvvsS5OZzRkFveXkXR9Ez2jhL01T2gFXcaMPk2pAKkLNPRQrbPonm1ect6Ndm-D8pEurmcgkd0KYsxxiQo11zklunLgjg9_lhcrJwke4xjGn2m47GUuIQD3cGFl4mI_ratPV5AjA8za32vF1z6j_KG3xlUpvheBfm8rKW2ss_il-pzd7fY54mkOeb1EA_pQ==', start_index=25927)
Annotation(end_index=25995, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtW1GpD4K-d6PVtBesp496JHhMFrPfe3fpLXrdoOrHLJsQ9VzXzyioVsbf3zb9CnxHID9I-0PaoOX3nYIZ-h8uaIn_jhhFx5JgihGWXeZHJON5LxKW67DHxkOajcOdU6C-B1zPDsczYfCUFlPMS2EtZqjgNpMWIbxi9vs5ec-DyZGKf7yyplXSkrG3up9Bn6J1MjvT14sfVfgOiGLC6EuRM2eMPhVCwwvh4FDuvgty7Llqrg==', start_index=25985)

## Sources
