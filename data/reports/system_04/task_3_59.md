# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** f6c760fd | **Time:** 525.96s | **Cost:** $2.52769
--------------------------------------------------------------------------------

# Does Enthalpy Balance in Thermodynamic Models Constrain the Economic Boundaries of Hydrogen Thermal Management?

### Key Points
*   **Thermodynamic Rigidity:** Enthalpy balance acts as a rigid physical constraint on the hydrogen economy, setting a "hard floor" for energy consumption—specifically in liquefaction and compression—that economic optimization cannot bypass, only approach.
*   **The Liquefaction Gap:** The theoretical minimum energy to liquefy hydrogen is ~2.9–3.9 kWh/kg, but practical enthalpy constraints (including ortho-para conversion heat) drive actual consumption to 10–15 kWh/kg. This thermodynamic gap is the primary driver of the high Levelized Cost of Hydrogen (LCOH) for liquid pathways.
*   **Refueling Economics:** The negative Joule-Thomson coefficient of hydrogen at ambient temperatures necessitates energy-intensive pre-cooling (to -40°C) during fast refueling. This thermodynamic requirement dictates a significant portion of station CAPEX ($1,200–$3,000 per kg/day capacity) and operational complexity.
*   **Thermoeconomic Linkage:** Advanced analyses (e.g., Gouy-Stodola theorem applications) explicitly link exergy destruction (thermodynamic inefficiency) in components like heat exchangers and compressors to monetary flow losses, proving that thermal mismanagement is a direct economic penalty.
*   **Future Viability:** Economic boundaries can only be expanded by narrowing the gap between actual enthalpy change and theoretical limits through advanced cycles (e.g., mixed refrigerants, magnetic cooling) or integration with other thermal sinks (e.g., LNG regasification), rather than eliminating the thermal burden itself.

---

## 1. Introduction

The transition to a hydrogen-based economy is frequently framed as a challenge of production scaling and policy support. However, a more fundamental set of constraints governs the viability of hydrogen as an energy carrier: the laws of thermodynamics. Specifically, the enthalpy balance—the accounting of internal energy, pressure, and volume changes within a system—serves as the immutable ledger that dictates the energy inputs required to condition hydrogen for storage, transport, and use.

Hydrogen possesses unique thermophysical properties, including a low boiling point (20 K), a negative Joule-Thomson coefficient at ambient temperatures, and a spin-isomer transformation (ortho- to para-hydrogen) that releases significant heat. These properties mean that "thermal management" in the hydrogen value chain is not merely an auxiliary function but a dominant energy consumer.

This report investigates whether enthalpy balance in thermodynamic models effectively constrains the economic boundaries of hydrogen thermal management. By synthesizing techno-economic analyses (TEA), exergy studies, and process simulations, we demonstrate that thermodynamic irreversibilities are not abstract inefficiencies but direct economic costs. The report explores how the enthalpy of liquefaction sets a price floor for liquid hydrogen, how the heat of compression drives refueling station capital expenditures (CAPEX), and how exergy destruction in fuel cells translates into operational expenditure (OPEX) losses.

---

## 2. Thermodynamic Fundamentals and Economic Linkages

To understand how enthalpy constrains economics, one must first establish the physical principles linking energy transfer to cost.

### 2.1 Enthalpy and the First Law
Enthalpy ($H$) is defined as the sum of a system's internal energy ($U$) and the product of its pressure ($P$) and volume ($V$): $H = U + PV$. In flow systems like hydrogen liquefiers or compressors, the change in enthalpy ($\Delta H$) represents the minimum amount of energy that must be added to or removed from the fluid to change its state.
*   **Constraint:** For hydrogen liquefaction, the enthalpy difference between gas at 300 K and liquid at 20 K is fixed by nature. No amount of economic innovation can reduce the energy required to bridge this gap below the thermodynamic minimum.

### 2.2 Exergy, Irreversibility, and the Gouy-Stodola Theorem
While enthalpy tracks energy quantity, exergy tracks energy quality—the useful work potential. Real-world systems are irreversible; they generate entropy ($S_{gen}$). The **Gouy-Stodola theorem** provides the critical link between thermodynamics and economics:
\[ \dot{I} = T_0 \dot{S}_{gen} \]
where $\dot{I}$ is the rate of irreversibility (exergy destruction) and $T_0$ is the ambient temperature.
*   **Economic Translation:** In thermoeconomic models, every unit of exergy destroyed ($\dot{I}$) represents a "lost cost." For a hydrogen plant, this means that inefficiencies in heat exchangers or compressors are not just engineering problems; they are direct financial leaks where paid-for electricity is converted into waste heat rather than high-value liquid hydrogen [cite: 1].

### 2.3 The Ortho-Para Enthalpy Penalty
Hydrogen exists in two spin isomers: ortho-hydrogen (parallel spins) and para-hydrogen (antiparallel spins). At room temperature, hydrogen is 75% ortho ("normal hydrogen"). At its boiling point (20 K), the equilibrium state is 99.8% para.
*   **The Constraint:** The conversion from ortho to para is exothermic, releasing 527 kJ/kg of heat—more than the latent heat of vaporization itself (446 kJ/kg) [cite: 2, 3].
*   **Economic Impact:** If this conversion is not catalyzed inside the liquefier, it will occur spontaneously in the storage tank, releasing heat that boils off the expensive liquid product. Therefore, thermodynamic models *must* account for this enthalpy of conversion, forcing liquefaction plants to include additional cooling capacity (and thus higher CAPEX and energy costs) to remove this heat during production [cite: 4, 5].

### 2.4 The Joule-Thomson Inversion
Most gases cool when expanded through a valve (throttling). Hydrogen, however, has a negative Joule-Thomson coefficient at ambient temperatures.
*   **The Constraint:** Expanding hydrogen from high pressure (e.g., tube trailers) to lower pressure heats the gas.
*   **Economic Impact:** This necessitates active pre-cooling systems (chillers) at refueling stations to prevent the gas from overheating vehicle tanks. This thermodynamic quirk imposes a mandatory CAPEX on every fast-fill station [cite: 6, 7].

---

## 3. Liquefaction: The Primary Enthalpy Constraint

Liquefaction represents the most energy-intensive step in the liquid hydrogen (LH2) value chain. The enthalpy balance of this process creates a massive economic barrier that defines the current cost of LH2.

### 3.1 The Efficiency Gap: Theoretical vs. Actual
The theoretical minimum work required to liquefy hydrogen from ambient conditions (300 K, 1 bar) to liquid (20 K) is approximately **2.9 to 3.9 kWh/kg**, depending on the precise boundary conditions and para-hydrogen content [cite: 5, 8, 9]. This represents the absolute thermodynamic floor.

However, actual industrial liquefaction plants operate far from this limit.
*   **Current State:** Existing plants typically consume **10–15 kWh/kg** [cite: 4, 8, 9, 10, 11]. This is roughly 30-45% of the Lower Heating Value (LHV) of the hydrogen itself (33.3 kWh/kg).
*   **The Economic Boundary:** This "efficiency gap" means that for every kilogram of hydrogen liquefied, the operator must purchase ~10 kWh of electricity. At an industrial electricity price of $0.06–$0.10/kWh, the liquefaction process alone adds **$0.60–$1.50/kg** to the cost of hydrogen, purely due to thermodynamic inefficiencies [cite: 4, 5, 12].

### 3.2 Cycle Architectures and Cost Implications
The choice of thermodynamic cycle determines how closely a plant can approach the theoretical minimum, directly trading off CAPEX (equipment complexity) for OPEX (energy efficiency).

#### 3.2.1 The Claude Cycle
The standard industrial process is the Claude cycle, often pre-cooled with liquid nitrogen (LN2).
*   **Thermodynamics:** It uses expansion turbines to remove enthalpy from the helium or hydrogen refrigerant.
*   **Economics:** While reliable, standard Claude cycles are limited to efficiencies of ~20-30%. The high exergy destruction in the expansion valves and heat exchangers keeps the Specific Energy Consumption (SEC) high (~12-15 kWh/kg) [cite: 4].

#### 3.2.2 Advanced Mixed Refrigerant (MR) Cycles
Recent research focuses on Mixed Refrigerant (MR) cycles to better match the cooling curves (enthalpy-temperature profiles) of the refrigerant and the hydrogen feed.
*   **Thermodynamics:** By using a blend of gases (e.g., neon, nitrogen, hydrocarbons), the temperature glide of the refrigerant can be matched to the hydrogen cooling curve, minimizing the temperature difference ($\Delta T$) in heat exchangers. Minimizing $\Delta T$ reduces entropy generation (irreversibility).
*   **Economic Result:** Studies show MR cycles can reduce SEC to **~6.0–7.6 kWh/kg** [cite: 10, 13, 14]. This reduction in energy consumption directly lowers the OPEX boundary. For example, a proposed dual-pressure Brayton cycle with LNG pre-cooling achieved an SEC of 6.60 kWh/kg, reducing specific costs by ~4.5% compared to reference processes [cite: 13].

#### 3.2.3 Magnetic Refrigeration
Magnetic refrigeration exploits the magnetocaloric effect, offering a pathway to bypass the limitations of gas compression cycles.
*   **Potential:** Theoretical models suggest SECs as low as **6–7 kWh/kg** are achievable, approaching 50% of Carnot efficiency [cite: 8].
*   **Constraint:** This technology is currently at a low Technology Readiness Level (TRL), meaning the *economic* boundary is currently constrained by the high cost of development and lack of commercial hardware, despite the favorable *thermodynamic* boundary.

### 3.3 Component-Level Constraints: Heat Exchangers and Compressors
The enthalpy balance dictates the sizing and cost of key components.

*   **Heat Exchangers:** The need to remove massive amounts of sensible and latent heat, plus the heat of ortho-para conversion, requires enormous heat transfer surface areas.
    *   **Thermoeconomic Analysis:** In a 50 ton/day plant analysis, heat exchangers accounted for **36.29%** of total exergy losses [cite: 15]. The cost of these units is driven by the need for high effectiveness; a small inefficiency in heat transfer at 20 K results in a massive penalty in compressor work at ambient temperature.
    *   **Material Constraints:** The extreme cold requires specialized materials (e.g., aluminum alloys, stainless steel) that maintain ductility, further driving up CAPEX [cite: 3, 13].

*   **Compressors:** Compression generates heat (enthalpy increase) that must be rejected.
    *   **Exergy Destruction:** Compressors are often the largest source of exergy destruction (irreversibility) in the liquefaction train, accounting for nearly **40%** of losses in some models [cite: 12, 15].
    *   **Cost Dominance:** Compressors dominate the CAPEX of the liquefaction plant. The requirement to compress helium or hydrogen to high pressures (e.g., 20-80 bar) to achieve the necessary enthalpy drop during expansion is a direct thermodynamic mandate that dictates investment costs [cite: 12].

---

## 4. Refueling Infrastructure: Managing the Heat of Compression

The interface between the supply chain and the vehicle—the Hydrogen Refueling Station (HRS)—is heavily constrained by the thermodynamics of high-pressure gas transfer.

### 4.1 The Reverse Joule-Thomson Effect
When hydrogen flows from a high-pressure station bank (e.g., 900 bar) to a lower-pressure vehicle tank (initially ~50-100 bar), it undergoes expansion and compression.
*   **Thermodynamic Reality:** Unlike natural gas, hydrogen heats up during this throttling process due to its negative Joule-Thomson coefficient at ambient temperatures. Additionally, the rapid compression of the gas inside the vehicle tank generates significant heat [cite: 6, 7, 16].
*   **Safety Limit:** Type IV composite tanks used in Fuel Cell Electric Vehicles (FCEVs) have a strict temperature limit of **85°C** to maintain structural integrity [cite: 6, 17, 18].

### 4.2 The Pre-Cooling Requirement (-40°C)
To ensure the gas inside the vehicle tank does not exceed 85°C during a fast fill (3-5 minutes), the hydrogen must be pre-cooled before it enters the vehicle.
*   **Enthalpy Balance:** The station must remove enough enthalpy from the hydrogen stream to counteract the heat of compression and J-T expansion. The SAE J2601 protocol mandates pre-cooling to **-40°C** (T40 category) for fast fueling [cite: 17, 18, 19, 20].
*   **Economic Constraint:** This requirement imposes a rigid equipment cost. A station cannot simply dispense ambient hydrogen quickly; it *must* install a refrigeration unit (chiller) and a high-pressure heat exchanger (diffusion-bonded or microchannel) [cite: 18, 19, 20].

### 4.3 Economic Analysis of Station Thermal Management
The cost of this thermal management is a significant fraction of the station's total cost.
*   **CAPEX:** The capital cost for cooling systems is substantial. For a station capacity of ~450 kg/day, the refrigeration equipment and heat exchangers are major line items. Total station capital costs range from **$1,200 to $3,000 per kg/day** of capacity, with cooling systems being a non-negotiable component of this [cite: 21, 22].
*   **Specific Costs:** Some suppliers estimate the installed capital for pre-cooling units adds roughly **$0.50/kg** to the cost of dispensed hydrogen [cite: 18].
*   **Operational Costs:** The chiller consumes electricity, adding to the station's OPEX. The efficiency of this cooling (COP) varies with ambient temperature; hotter climates require more energy to achieve the -40°C target, illustrating how environmental enthalpy conditions constrain station economics [cite: 18].

---

## 5. Storage and Transport: Enthalpy Interaction with the Environment

Once hydrogen is liquefied or compressed, the battle against enthalpy balance shifts to preventing heat ingress from the environment.

### 5.1 Liquid Hydrogen Boil-Off
Liquid hydrogen at 20 K is surrounded by an ambient environment at ~300 K. This huge temperature difference creates a relentless driving force for heat transfer (enthalpy gain).
*   **Thermodynamics:** Heat leakage causes the liquid to boil. The latent heat of vaporization is 446 kJ/kg.
*   **Economic Loss:** Boil-off gas (BOG) represents a loss of high-value product. If 1% of the hydrogen boils off per day, the effective cost of the remaining hydrogen increases.
*   **Ortho-Para Conversion (Again):** If the hydrogen was not fully converted to para-hydrogen during liquefaction, it will spontaneously convert in the tank. This exothermic reaction releases heat *internally*, causing "self-boiling" even in a perfectly insulated tank. This underscores why the initial liquefaction energy penalty (to catalyze conversion) is an unavoidable economic investment to prevent storage losses [cite: 2, 3, 4].

### 5.2 Insulation vs. Refrigeration
The economic boundary here is a trade-off between passive insulation and active cooling.
*   **Passive Insulation:** High-performance Vacuum Multi-Layer Insulation (MLI) is expensive (high CAPEX) but has zero energy cost (low OPEX). However, it cannot stop boil-off completely [cite: 2, 23].
*   **Active Cooling (Zero Boil-Off):** Cryocoolers can re-liquefy BOG, closing the enthalpy balance. However, this adds CAPEX and significant electricity OPEX.
*   **Cost Estimates:** The cost of LH2 storage systems, heavily driven by these thermal management requirements, is estimated at **$2–$10/kWh** of stored energy capacity (comparable to cavern storage costs in some metrics, though tank costs are generally higher) [cite: 24].

---

## 6. Fuel Cells: Thermal Management at the End-Use

In the fuel cell stack, chemical energy is converted to electricity and heat. The enthalpy balance here dictates the cooling load required to prevent overheating.

### 6.1 Heat Generation and Removal
PEM fuel cells operate at ~60-80°C and are roughly 50-60% efficient. The remaining 40-50% of the energy content of the hydrogen is released as heat.
*   **Constraint:** Unlike internal combustion engines, which exhaust much of their heat through hot gas, fuel cells must reject most heat through the coolant loop. This requires large radiators and pumps.
*   **Thermoeconomic Analysis:** Detailed studies using the Gouy-Stodola theorem identify the **water cooling units** as the components with the greatest heat transfer and, consequently, the highest irreversibility rates. This thermodynamic inefficiency translates directly into "monetary flow loss"—the cost of the exergy destroyed in the cooling process [cite: 1, 25].

### 6.2 System Complexity and Cost
The requirement for precise thermal management (keeping the stack within a narrow temperature window) adds complexity.
*   **Components:** Pumps, radiators, sensors, and control logic are required.
*   **Cost:** These Balance of Plant (BoP) components contribute significantly to the total system cost. In some analyses, the cooling system and associated thermal management account for a measurable percentage of the total stack cost, and their parasitic load (pumps, fans) reduces the net system efficiency, effectively increasing the fuel cost per kWh of useful output [cite: 26, 27, 28].

---

## 7. Integrated Energy Systems: Expanding the Boundaries

Given the rigid constraints of enthalpy balance, economic optimization often lies in system integration—using waste heat or cold energy from one process to balance another.

### 7.1 LNG Cold Energy Recovery
Liquefied Natural Gas (LNG) is stored at ~111 K. When regasified, it releases "cold energy" (absorbs enthalpy).
*   **Thermodynamic Synergy:** This cold energy can be used to pre-cool hydrogen in the liquefaction process, replacing the energy-intensive LN2 or mechanical refrigeration stages.
*   **Economic Benefit:** Research indicates that utilizing LNG cold energy can reduce the SEC of hydrogen liquefaction to **~6.6–7.6 kWh/kg**, a significant reduction from the standard 10-12 kWh/kg. This lowers the LCOH by reducing electricity consumption (OPEX) and potentially downsizing compressors (CAPEX) [cite: 10, 13, 29].

### 7.2 Waste Heat Utilization
In high-temperature electrolysis (SOEC) or nuclear-coupled hydrogen production, thermal energy (enthalpy) from the reactor or waste heat sources can replace electrical heating.
*   **Economic Impact:** This substitution improves the overall efficiency and can reduce the LCOH to competitive levels (e.g., £1.24–£2.14/kg for nuclear-coupled HTSE) by respecting the enthalpy balance: using low-grade heat for thermal loads and high-grade electricity only for electrochemical work [cite: 30].

---

## 8. Conclusion

The query asks if enthalpy balance constrains the economic boundaries of hydrogen thermal management. The evidence overwhelmingly suggests that **yes, it does, and rigidly so.**

Thermodynamic models based on enthalpy balance reveal that the costs of hydrogen thermal management are not arbitrary market figures but are rooted in physical constants:
1.  **The Liquefaction Floor:** The enthalpy difference between 300 K and 20 K, combined with the heat of ortho-para conversion, sets a minimum energy cost (~3-4 kWh/kg theoretical, ~6-10 kWh/kg practical) that defines the baseline OPEX for liquid hydrogen.
2.  **The Refueling CAPEX:** The negative Joule-Thomson coefficient of hydrogen mandates the installation of expensive pre-cooling infrastructure (-40°C chillers) at refueling stations, setting a high entry cost for station developers.
3.  **The Cost of Irreversibility:** Thermoeconomic analyses prove that exergy destruction in thermal components (heat exchangers, cooling loops) is mathematically equivalent to financial loss.

While technological advancements (magnetic refrigeration, microchannel heat exchangers) and system integration (LNG cold recovery) can push operations closer to the theoretical limits, the enthalpy balance itself remains an absolute boundary. The economics of hydrogen thermal management are, therefore, ultimately a function of how efficiently engineering can navigate these immutable thermodynamic landscapes.

## References
[cite: 13] Thermodynamic and economic analysis of a novel hydrogen liquefaction process...
[cite: 4] Liquid hydrogen: a review on liquefaction, storage, transportation, and safety...
[cite: 12] Economic Analysis of a Hydrogen Liquefaction Process Based on Techno-Economic...
[cite: 1] Exergy and Thermoeconomic Analyses of a Proton-Exchange Membrane Fuel Cell...
[cite: 2] Review of the Thermodynamic Properties of Hydrogen Based on Existing Equations...
[cite: 19] Cost of cooling systems in hydrogen refueling stations...
[cite: 17] Pre-cooling systems for hydrogen fueling stations: Techno-economic analysis...
[cite: 18] Efficient Pre-Cooling Solutions for Hydrogen Refueling Station Design...
[cite: 8] The theoretical minimum energy consumption for hydrogen liquefaction...
[cite: 10] Investigation and thermodynamic analysis of hydrogen liquefaction cycles...
[cite: 5] Hydrogen Liquefaction Costs...
[cite: 4] Economics: hydrogen liquefaction is an energy-intensive process...
[cite: 12] Economic Analysis of a Hydrogen Liquefaction Process...
[cite: 24] Hydrogen Methodology...
[cite: 21] Hydrogen Fueling Stations Cost...
[cite: 14] Thermoeconomic analysis of novel hydrogen liquefaction assisted by absorption...
[cite: 13] Thermodynamic and economic analysis of a novel hydrogen liquefaction process...
[cite: 8] Existing hydrogen liquefaction plants demand around 13 kWh...
[cite: 5] The theoretical minimum energy requirement to produce liquid hydrogen...
[cite: 9] Actual liquefaction energy requirements are substantially higher...
[cite: 6] Reverse Joule-Thomson effect hydrogen refueling enthalpy...
[cite: 7] Joule-Thomson effect...
[cite: 15] Hydrogen liquefaction economic boundary helium heat exchangers...
[cite: 3] Understanding the physical phenomena that occur inside heat exchangers...
[cite: 1] Exergy analysis evaluates the efficiency of system components...
[cite: 25] The irreversibility rate of each component is obtained by the Gouy-Stodolar theorem...
[cite: 21] Hydrogen Fueling Stations Cost...
[cite: 22] Cost of hydrogen station pre-cooling unit per kg...

**Sources:**
1. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsn343uNMOp9tTv6sQODSstE0z6A3JRpnJPlXXFQNfbvN8zJ_0d0GOAL6f6mPtS0KrqWSbNx6z2broJiEQLlp6-WXyFv3gGRBVq30YSg2KZ5BUQTDZakRwLIgV_7rG2KC_ECHP-UDz9w==)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoKunknjZteTo_pL3DRi56mrD1ZSlUvmORbPXZ035dvvgWzZnv7CXjYFhP0aC0T9BFSKsFRaslbnA-pMawGi7AFp2icImJ9LrBt3wOwg9gm-YLco4WAE4tAeOuhGmKcEDooauwHyP_y-G214Qz_xZM6Ap_0Fc_bn4UY9zvubUtCv-r7UYy_p_YSBV_rtVkCr9mCQpD0NU4nXKyY3jToqezM-HOyppZwFfm9SLPA8UyBO_JYjW0P_4zkavR7XpBz-nB)
3. [iifiir.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtt5VLqyhUiBzTlrQsLc-C78hLtmn8l7XFymmy_dPVmeaDJGaHrcnSkCyg0ihRhsFrm0SlLWNTLnr6oR2xfSgV0EWq0e6Ls3SMi-rhx-aufn5WJIau1dfSCOUXw0EwqxW8jJ9vNzKqg4eBRGG9jhx2s-zbyEJbo4eajeTTJKddx-7ikiK3EwY6v_Kf3jLAQTudFK3Fx_ki3xfxhYrWKbo=)
4. [rsc.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGt3h90k_K_r2JYvQKox3YPXXGfza5x7vhbncpVbxA8dtODsTYMS964uS5_rmCufOd2XboMEMT_n0qUDHdELQue_3sdExGjIMh3LEBS0epP9J4Ewo7geXcJJ8pEOGUtaGE6-pwQdJCmVNxiiBQGKW4VloE_nQ==)
5. [energy.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUecUh0tJeuMhLRpFuIqV_tF0jgbXC1LZlJtoWldEO9T-mZfrtbbpyjzeXl7TENGUDtZH76yMncyUzjN_2AsWcVZK_CdcRQFutCOMd4fLOi2wiRHZVQmsLDw4oQx4DKxistZ5ZqcVqtiaI4d4Ewti8rGYXczu6choAe6qhsN5Za9_SZGuF-OwGnLPbopHtMkPZhbWc1TFrdEqcLQThbnv8JWMYMvt6LyagxX4N)
6. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8q3GWkXRwbYhcQv9fMJ9isZ6d_WfX4XwycXHxg4JSEsB2cbhw22TZCRjF1qwu3qAuNlU4M6Hs8jE1BrHv-HzzfAoV1rv6Tb9e4NuyHFssjQRUdPmmkZDjAHhMEUWf)
7. [nist.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5SWoJjA7SMatcNMDwJ5_ArBQQQRtQ4LkNaxo1XYJg37cr2fxEjVSJB53UU-A0Gr-JKiOXd6NBUD19ZS7yVmIwKUYEBHS_LqPK3RpKOQUlE55es_RxkLGwKcFH4NMm4M6hPTgXhCmIyGOU99geW9yKmVE-)
8. [iiasa.ac.at](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFE3tkrphigF97e9R-MiZejrM5HOENP82ub2RIKj0PM6oCIMPho_hTcozfkTqKk2dE8Bf9-mfMMVTh-efn_9k33rzx96hYBkr2Xvr7L7OSB_Nben8EG0TVpeTB-xF3Dy8x8z51zM5jvmK3DrpnYSjZakM7Po6DvSOjNTXLoOqHgY6Hs)
9. [energy.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhBS324KlxzihEcqx6uKD-noSiyKj9Yxx86HmMjXhWa7R29I-_unn70nm5i2Bu94-jNGPnY-DLxSbPlKMrpQdevmlSrwvWJjvrWNeD3d7FoRBcFZwli5StrtaSfaS8mYUI3MeSZC_yQYB8q__vBfHczoyltlNMmcDIkB5aJY7SzzQv1G0YCB91NL1E_V6lcM4WufD2azDMMaK8fLf0vPX9LQCei1P0X9L7j7986tH9iBkhwsoLZcPhJdpquFExny5U)
10. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGn5yLOV_THGuMu9QH-RpXxhsM2y6J5q-vLO5ioUl3gaK7DDQVX-8xPGFrx7WtHUEZe-1YR9ODdRgp7UolalGeSo0FBaffcTgUKp8gd5oz_PhfvlLSlai2lJrpzDxGu)
11. [fenex.org.au](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcq96S-0P5RtFu80uNb0IZLZ4PyjWWpJ5PIBOiXCpVeA9P_HQCvx3REcjxi7mw3w6bFwPW17illHiBrvhn8cEvwkoEUtjgEXwr5Ca3x3oTnDaeygQrc42A62KM8TWcL6MhgOZF32gN1TaQmLQ53crQBNSDZiosXVKd_ap1VeFfm9RN0FIODyQ-4wVvym5m1wfR)
12. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-Wb-_J9aKPopRaC_rolwMNEbf0ypvrBujxZJP3isXyNZUUQjkgW6s3wMqSGlp8WUeV55SpGuM8fzz0LD1TNNreqAL67qsC7ftY-K01XOaT1RNkXm0SY2R6RaEjoeWqb72oNX5dBgHAPQTikzXOycOWP_DROX2kJ4GrShmmkOUCPJH-rD4_SrYMaQ-ZQn4aj1Gh1czrRIt5UyRqnWfXIO5_HtYvhyajoMzCB5ttPmVMjOjXIRiwPOH_b9sxvebdQhhjyHl230fak8rUk30XGw=)
13. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0DrJEwZH6KDxTmB8y7nHxu6gwy3aU-zvT78fNgo0orLLNVx5WfJsc381u_r2FxLDcFP3zcS0oxu9iYHrLimrXHGTa0ADQuYweFQaJS6ULzi8ZJpM1x1_QW21DyuTrXjyz5sAE8OSrfq6Aj-xK47VNdX6cFrTOFYDugdehqQozw44nginwFJlSHfdQhlhKTJRSr736Y8qyBF5HkpsDVfz9FchJ5emr5jfYyF5NeUt9ipC9Q07D7GMk0IEm5DKSj0PkLW-viOIUrYxyHLZeW2G6RxLzbwaiRyKD4M-x23oY16nPIhnM_acBAOI=)
14. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRjlxKxLkbQpfOY3KKB_bu5vyIOz-1MZZJhenkUacGT39AuRN1ksUsf54SrWzJd_HA5vWf4tdc5kQ5Qg1G8DBI5MCVOxIy2-Q9Irqo5eNrDAIUIInptKAd3211yNM934hpVLpTMnX3SvQICSqXLcQUlb3qi6Mbp9fre_15oKey_eo4OydYaADltYhL0zZRZkw6j4wz8uV25YUBnfM5QPF1znvONRStO_Qtj5UbMeRc-5oNqZCD5Hxbmou6pJ54QLnpJEYNmPstpabZtYTfFsZvUlZ-fPuesIuuV6SisLVjgpPZn7LiRKk=)
15. [acs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmJUntTkuWaZM4D-PuIcB98L9ZCxPcVlCzTppvD8rul_DdqsCrX-kuYhfnnR-d_GmDUKnRvGRZlQWG0BP4F5kCzW7-uXeaJP6t48m1jiSlqWDmj95Ls5j5FI0ukecGI1omY_OKF9Ug)
16. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSXNP4HJtMeacfjMBvZ1lvIr_Ao-qac-ETMdtDmJvQj6JC2c4hoWxLMJbJr4hj-hBgkn_DfRA4C3wjTlC_8WcOXsmqj2LI5f865t8Yzwg49G04KqzFrvcoOmAfPOQIxzHuh3DRbINKMFzEPysfGBoh2rKnhHtWLzv9JDX0EtTq4Q517m3Bg0gfHhDOUogOPBeiJQ7nIwuRpC7Osi-bAcXee1pqZB3GDzsJzfICJbtekzX_s3ohk8TBST-KPlBw)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoXT3tNy8mXv_KogK4z_TBp-UCliF_GjNN-gxLeLEIgL6Gud0pRP4YNK9J96iDeMCI6x2tgvQx9vEkqeT9gND5-j1XuSmAzcLFygPhfdizi5a8Q24NJ_gVfY19lSaqnqEv4PphiKE3BzHqgL61vifmylhK0We8u_gM9zbFJ1OiFW6UmY64Aij1Zz9VZNtglHgUSkdBSOvgd3ZUrVGgv1aiFPYelAlqwERkk8fwfpG4Bo77q77ZlkfCDL5q4tXxnxsftkDEXkTxUd0=)
18. [shenshiec.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIrhRh-QpoJp231XV2yMokVf9usXK0B-AEanuGOa-ustmstE_2ztBO9BwurIAmgIWLbEIG-B96jiEx6BYFAJo_U2Nqm9VFWCBPas46bSyOmrO1TSEZvVVxUkSYN7IB3FgRQ2WkKVE_Sqwju3HVlbE6f_yRkiXhzh7d8npO1FB5d2H7oe7mS5BV945Uu9SPrmgCnMJR6eOblYQiSNZPU7S_)
19. [osti.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF80J-sg6qryFIO6cJgOFcBt6W2WtAf3AuTJPcSH1rvEYQ1WYl7TcxKuD_qhXbF_8tJ0ZqVJM52PEjxMwZRz48r10IVzP81zbN1tUDtd9ffaXgC8fxBTBXUPtXq9wYaL9g=)
20. [energy.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGj6HoU0BFDWe90UjiPXdEOOZB1xh1veMURxmPufwwI7-OV-VvIequyRGSzkJ-F3T78njSYguzvift156Q-zOZoD6hwDcxHzB5Be6mI0D9dBOG6KeKlhO4927RZf0AL0AYFXCwl1z1clmEtQivjQjDrhTfkYtW1MDnaXZNcB1Osg-BGdrc97vefdcDruAHupRRaiVaEswHpGMFILcdr-LasS31FLUCMWYOimySuYQ==)
21. [energy.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFD3haVdIfox8vaExvxGIn4U9xryyyRkA3wADcMmKjvzIh7kxafTLMvg9n4bQZb2AUKmHLjGvqd0LRX1oCINxaa94Hv5juvwSOuZh5GM1BvJ2CXNLEOdm2TTVPgxLKNjJsn3BVpHw6Oefa1iniuVXTXcSp6pmZwUje5P5K4AxSn-4zXuy_iIkAJ6HutLaBb0AJg0763j3SA9OrsFkcNjdkrJW1D_tj5sYEGgQWxLNU=)
22. [nrel.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIZ5CIkLKOrOP3VenaFeLHVD2yVU5lQmbSZPul6SUE61pCrNlmdWL8BUew_upda0WYAR9WR3fOV9auukQ_MKJmtJRiiRmBS212PSE3MNihr0UCtoRYVo0doXzDTGK2gFGXYGw=)
23. [escholarship.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7gTPRz07e4HpByZ9HTE0bOfafKt2n1x56YQZmi0JPCfjDT3hRStMtgW4vcgUjh3bBOk8W7j4olfYhMs-HdEE2_1NtawnrlCh1-IFIZKKAqxpnnQF5QTwDFttfbO2HU7kV5UIDjPegtooeEaUVmRtGRGF923ExIUlXwcQmIkP1HxiMOWUw5ZvZz4cFQTnSOzOYdJ0DnrQKR32TjE3SV-xUz3Dq)
24. [pnnl.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHb4iTPTy5jMe93ptlsK8fjXqu4-tSdhJh8YzGUJpqri4OOlRouyB532w8XNu0c-DoFJZjLZl1CwX4S3A0I4V6qoJLBYXUYcCCiFYYeF4BGUJMYenGb5Oid7imEecBq6CFLXM6ppSuhgxr_hBRwQRpfZfDXm0wJbh06etHX0gXwWrww)
25. [preprints.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYOV3aXI1M1kUxJYkGZ15hPZ3TWiyX8wKOkYUr9rQ_qN9IlRpN0FeTJL1fmBdj8UB_SvKx_YRMYnVQJklco5RfSROSkTsg1Oxpo4Ljw26W3eHL7Q1ZCRCBkjPfQu9lIo3yA8RnB8GSzdWXxzuxTVxw2aTjxsUpLK2XMTY_mrIoWvDylKitueMmY2iJT7bU7mKq)
26. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkhZyoLm2ZIGUa2tmxWheH8PsIL_K6AvJolYxB1IoHYiq3AVMxBIHJcb-nVVd7LT_OcImy4NW02sPXGZZMpHp6Fn46FAjfQUpkMYSyfpFQulTybgQb5UwCjhVTVX41hySgdi8U1LBeCMppqtUASzlY7Z4iCOVQbf5HAfhcXLCZv5ePFvFCPPPZLnVJNy8BWsviJXVRwjAfLUiiWIbEj-8C8HBsLrx2T4yyumzz1uS-qif3nzkLp9DatGzRwJ91vlYEAeNTO7YXuQXYbxph1uYOkWG21xeIEe8fSbazfkbc)
27. [arzonlimited.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZVUPjMRHqD6Pgh0JaI2t0dJuxNbjD5uAIRj2wesb1AQHKNKgOMUDAhh5przRd2vkAQplVKfHRKWGci95rFoeYYUuHgBYLbPG3ffmIp-gjZTxPsBQmjU9wdnM9te7vTZ7WrxiiHW3-miObOqRz3i2h5MdTE7iqS9pztQqUMi8zPBAa0QPo6LcbA3-v1s7cA2gxZY4vPgYv5wA=)
28. [e3s-conferences.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyrb-m49eNEvrrCJKAWdOeo4AjlvSVg6D-CWHrCeWFUpZas-J41fmLfU30kF23ZUOKz7W13k5nLwwI_PTRtc_x1u_iF4v_PM12r8cpCgy55kCRTQholi707rIucoCtsrLc3LYRL4jZyeUwVekBj8AJjMZYnSchk8SgzDpwDQT4TD9NXpq4Zi23FzzquQ==)
29. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCqp79pAmIrtDBvY6nKytFOSrUQgqbNGxdTZddHKC8JzxIqPDiraS6YXXzseKJqT4bEITwGnm_b1JXHG_BWpO6W2SuzLXtEDFHlSpPG3iZA-KP4GZj9PR2nEqF6oz_IGReU2xIKhDOhit_Uk53lT7JNnS0m_h4UDdndAIj)
30. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGS0_lRGVYHUmaAjfyrf3FyKN2_F7mh0Q1O_FszfrvSWzcEJt-VXG2JTcvVKo_DjSLr2IccWBRFzSq2SvTB8a82PazIymAF93vyXeJagthi40wYGLzCx6ABuWUs3p_jhiYArzzJW1wE2BCjG5rgmiEhW-LT_7NeO77f4vD_ZNt6W9T9pxOTB3kPno7MZKRieY8vt_3C1ZwqaFXC6U_ZRnov57wk8v5yBN8sa-8kTr8bW_fnukT9czY-ids=)


## Annotations
Annotation(end_index=4887, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsn343uNMOp9tTv6sQODSstE0z6A3JRpnJPlXXFQNfbvN8zJ_0d0GOAL6f6mPtS0KrqWSbNx6z2broJiEQLlp6-WXyFv3gGRBVq30YSg2KZ5BUQTDZakRwLIgV_7rG2KC_ECHP-UDz9w==', start_index=4878)
Annotation(end_index=5345, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoKunknjZteTo_pL3DRi56mrD1ZSlUvmORbPXZ035dvvgWzZnv7CXjYFhP0aC0T9BFSKsFRaslbnA-pMawGi7AFp2icImJ9LrBt3wOwg9gm-YLco4WAE4tAeOuhGmKcEDooauwHyP_y-G214Qz_xZM6Ap_0Fc_bn4UY9zvubUtCv-r7UYy_p_YSBV_rtVkCr9mCQpD0NU4nXKyY3jToqezM-HOyppZwFfm9SLPA8UyBO_JYjW0P_4zkavR7XpBz-nB', start_index=5333)
Annotation(end_index=5345, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtt5VLqyhUiBzTlrQsLc-C78hLtmn8l7XFymmy_dPVmeaDJGaHrcnSkCyg0ihRhsFrm0SlLWNTLnr6oR2xfSgV0EWq0e6Ls3SMi-rhx-aufn5WJIau1dfSCOUXw0EwqxW8jJ9vNzKqg4eBRGG9jhx2s-zbyEJbo4eajeTTJKddx-7ikiK3EwY6v_Kf3jLAQTudFK3Fx_ki3xfxhYrWKbo=', start_index=5333)
Annotation(end_index=5777, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUecUh0tJeuMhLRpFuIqV_tF0jgbXC1LZlJtoWldEO9T-mZfrtbbpyjzeXl7TENGUDtZH76yMncyUzjN_2AsWcVZK_CdcRQFutCOMd4fLOi2wiRHZVQmsLDw4oQx4DKxistZ5ZqcVqtiaI4d4Ewti8rGYXczu6choAe6qhsN5Za9_SZGuF-OwGnLPbopHtMkPZhbWc1TFrdEqcLQThbnv8JWMYMvt6LyagxX4N', start_index=5765)
Annotation(end_index=5777, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGt3h90k_K_r2JYvQKox3YPXXGfza5x7vhbncpVbxA8dtODsTYMS964uS5_rmCufOd2XboMEMT_n0qUDHdELQue_3sdExGjIMh3LEBS0epP9J4Ewo7geXcJJ8pEOGUtaGE6-pwQdJCmVNxiiBQGKW4VloE_nQ==', start_index=5765)
Annotation(end_index=6322, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8q3GWkXRwbYhcQv9fMJ9isZ6d_WfX4XwycXHxg4JSEsB2cbhw22TZCRjF1qwu3qAuNlU4M6Hs8jE1BrHv-HzzfAoV1rv6Tb9e4NuyHFssjQRUdPmmkZDjAHhMEUWf', start_index=6310)
Annotation(end_index=6322, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5SWoJjA7SMatcNMDwJ5_ArBQQQRtQ4LkNaxo1XYJg37cr2fxEjVSJB53UU-A0Gr-JKiOXd6NBUD19ZS7yVmIwKUYEBHS_LqPK3RpKOQUlE55es_RxkLGwKcFH4NMm4M6hPTgXhCmIyGOU99geW9yKmVE-', start_index=6310)
Annotation(end_index=6882, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFE3tkrphigF97e9R-MiZejrM5HOENP82ub2RIKj0PM6oCIMPho_hTcozfkTqKk2dE8Bf9-mfMMVTh-efn_9k33rzx96hYBkr2Xvr7L7OSB_Nben8EG0TVpeTB-xF3Dy8x8z51zM5jvmK3DrpnYSjZakM7Po6DvSOjNTXLoOqHgY6Hs', start_index=6867)
Annotation(end_index=6882, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUecUh0tJeuMhLRpFuIqV_tF0jgbXC1LZlJtoWldEO9T-mZfrtbbpyjzeXl7TENGUDtZH76yMncyUzjN_2AsWcVZK_CdcRQFutCOMd4fLOi2wiRHZVQmsLDw4oQx4DKxistZ5ZqcVqtiaI4d4Ewti8rGYXczu6choAe6qhsN5Za9_SZGuF-OwGnLPbopHtMkPZhbWc1TFrdEqcLQThbnv8JWMYMvt6LyagxX4N', start_index=6867)
Annotation(end_index=6882, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhBS324KlxzihEcqx6uKD-noSiyKj9Yxx86HmMjXhWa7R29I-_unn70nm5i2Bu94-jNGPnY-DLxSbPlKMrpQdevmlSrwvWJjvrWNeD3d7FoRBcFZwli5StrtaSfaS8mYUI3MeSZC_yQYB8q__vBfHczoyltlNMmcDIkB5aJY7SzzQv1G0YCB91NL1E_V6lcM4WufD2azDMMaK8fLf0vPX9LQCei1P0X9L7j7986tH9iBkhwsoLZcPhJdpquFExny5U', start_index=6867)
Annotation(end_index=7110, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFE3tkrphigF97e9R-MiZejrM5HOENP82ub2RIKj0PM6oCIMPho_hTcozfkTqKk2dE8Bf9-mfMMVTh-efn_9k33rzx96hYBkr2Xvr7L7OSB_Nben8EG0TVpeTB-xF3Dy8x8z51zM5jvmK3DrpnYSjZakM7Po6DvSOjNTXLoOqHgY6Hs', start_index=7087)
Annotation(end_index=7110, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGcq96S-0P5RtFu80uNb0IZLZ4PyjWWpJ5PIBOiXCpVeA9P_HQCvx3REcjxi7mw3w6bFwPW17illHiBrvhn8cEvwkoEUtjgEXwr5Ca3x3oTnDaeygQrc42A62KM8TWcL6MhgOZF32gN1TaQmLQ53crQBNSDZiosXVKd_ap1VeFfm9RN0FIODyQ-4wVvym5m1wfR', start_index=7087)
Annotation(end_index=7110, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGn5yLOV_THGuMu9QH-RpXxhsM2y6J5q-vLO5ioUl3gaK7DDQVX-8xPGFrx7WtHUEZe-1YR9ODdRgp7UolalGeSo0FBaffcTgUKp8gd5oz_PhfvlLSlai2lJrpzDxGu', start_index=7087)
Annotation(end_index=7110, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGt3h90k_K_r2JYvQKox3YPXXGfza5x7vhbncpVbxA8dtODsTYMS964uS5_rmCufOd2XboMEMT_n0qUDHdELQue_3sdExGjIMh3LEBS0epP9J4Ewo7geXcJJ8pEOGUtaGE6-pwQdJCmVNxiiBQGKW4VloE_nQ==', start_index=7087)
Annotation(end_index=7110, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhBS324KlxzihEcqx6uKD-noSiyKj9Yxx86HmMjXhWa7R29I-_unn70nm5i2Bu94-jNGPnY-DLxSbPlKMrpQdevmlSrwvWJjvrWNeD3d7FoRBcFZwli5StrtaSfaS8mYUI3MeSZC_yQYB8q__vBfHczoyltlNMmcDIkB5aJY7SzzQv1G0YCB91NL1E_V6lcM4WufD2azDMMaK8fLf0vPX9LQCei1P0X9L7j7986tH9iBkhwsoLZcPhJdpquFExny5U', start_index=7087)
Annotation(end_index=7561, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUecUh0tJeuMhLRpFuIqV_tF0jgbXC1LZlJtoWldEO9T-mZfrtbbpyjzeXl7TENGUDtZH76yMncyUzjN_2AsWcVZK_CdcRQFutCOMd4fLOi2wiRHZVQmsLDw4oQx4DKxistZ5ZqcVqtiaI4d4Ewti8rGYXczu6choAe6qhsN5Za9_SZGuF-OwGnLPbopHtMkPZhbWc1TFrdEqcLQThbnv8JWMYMvt6LyagxX4N', start_index=7545)
Annotation(end_index=7561, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-Wb-_J9aKPopRaC_rolwMNEbf0ypvrBujxZJP3isXyNZUUQjkgW6s3wMqSGlp8WUeV55SpGuM8fzz0LD1TNNreqAL67qsC7ftY-K01XOaT1RNkXm0SY2R6RaEjoeWqb72oNX5dBgHAPQTikzXOycOWP_DROX2kJ4GrShmmkOUCPJH-rD4_SrYMaQ-ZQn4aj1Gh1czrRIt5UyRqnWfXIO5_HtYvhyajoMzCB5ttPmVMjOjXIRiwPOH_b9sxvebdQhhjyHl230fak8rUk30XGw=', start_index=7545)
Annotation(end_index=7561, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGt3h90k_K_r2JYvQKox3YPXXGfza5x7vhbncpVbxA8dtODsTYMS964uS5_rmCufOd2XboMEMT_n0qUDHdELQue_3sdExGjIMh3LEBS0epP9J4Ewo7geXcJJ8pEOGUtaGE6-pwQdJCmVNxiiBQGKW4VloE_nQ==', start_index=7545)
Annotation(end_index=8279, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGt3h90k_K_r2JYvQKox3YPXXGfza5x7vhbncpVbxA8dtODsTYMS964uS5_rmCufOd2XboMEMT_n0qUDHdELQue_3sdExGjIMh3LEBS0epP9J4Ewo7geXcJJ8pEOGUtaGE6-pwQdJCmVNxiiBQGKW4VloE_nQ==', start_index=8270)
Annotation(end_index=8918, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0DrJEwZH6KDxTmB8y7nHxu6gwy3aU-zvT78fNgo0orLLNVx5WfJsc381u_r2FxLDcFP3zcS0oxu9iYHrLimrXHGTa0ADQuYweFQaJS6ULzi8ZJpM1x1_QW21DyuTrXjyz5sAE8OSrfq6Aj-xK47VNdX6cFrTOFYDugdehqQozw44nginwFJlSHfdQhlhKTJRSr736Y8qyBF5HkpsDVfz9FchJ5emr5jfYyF5NeUt9ipC9Q07D7GMk0IEm5DKSj0PkLW-viOIUrYxyHLZeW2G6RxLzbwaiRyKD4M-x23oY16nPIhnM_acBAOI=', start_index=8900)
Annotation(end_index=8918, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRjlxKxLkbQpfOY3KKB_bu5vyIOz-1MZZJhenkUacGT39AuRN1ksUsf54SrWzJd_HA5vWf4tdc5kQ5Qg1G8DBI5MCVOxIy2-Q9Irqo5eNrDAIUIInptKAd3211yNM934hpVLpTMnX3SvQICSqXLcQUlb3qi6Mbp9fre_15oKey_eo4OydYaADltYhL0zZRZkw6j4wz8uV25YUBnfM5QPF1znvONRStO_Qtj5UbMeRc-5oNqZCD5Hxbmou6pJ54QLnpJEYNmPstpabZtYTfFsZvUlZ-fPuesIuuV6SisLVjgpPZn7LiRKk=', start_index=8900)
Annotation(end_index=8918, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGn5yLOV_THGuMu9QH-RpXxhsM2y6J5q-vLO5ioUl3gaK7DDQVX-8xPGFrx7WtHUEZe-1YR9ODdRgp7UolalGeSo0FBaffcTgUKp8gd5oz_PhfvlLSlai2lJrpzDxGu', start_index=8900)
Annotation(end_index=9172, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0DrJEwZH6KDxTmB8y7nHxu6gwy3aU-zvT78fNgo0orLLNVx5WfJsc381u_r2FxLDcFP3zcS0oxu9iYHrLimrXHGTa0ADQuYweFQaJS6ULzi8ZJpM1x1_QW21DyuTrXjyz5sAE8OSrfq6Aj-xK47VNdX6cFrTOFYDugdehqQozw44nginwFJlSHfdQhlhKTJRSr736Y8qyBF5HkpsDVfz9FchJ5emr5jfYyF5NeUt9ipC9Q07D7GMk0IEm5DKSj0PkLW-viOIUrYxyHLZeW2G6RxLzbwaiRyKD4M-x23oY16nPIhnM_acBAOI=', start_index=9162)
Annotation(end_index=9480, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFE3tkrphigF97e9R-MiZejrM5HOENP82ub2RIKj0PM6oCIMPho_hTcozfkTqKk2dE8Bf9-mfMMVTh-efn_9k33rzx96hYBkr2Xvr7L7OSB_Nben8EG0TVpeTB-xF3Dy8x8z51zM5jvmK3DrpnYSjZakM7Po6DvSOjNTXLoOqHgY6Hs', start_index=9471)
Annotation(end_index=10203, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmJUntTkuWaZM4D-PuIcB98L9ZCxPcVlCzTppvD8rul_DdqsCrX-kuYhfnnR-d_GmDUKnRvGRZlQWG0BP4F5kCzW7-uXeaJP6t48m1jiSlqWDmj95Ls5j5FI0ukecGI1omY_OKF9Ug', start_index=10193)
Annotation(end_index=10579, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0DrJEwZH6KDxTmB8y7nHxu6gwy3aU-zvT78fNgo0orLLNVx5WfJsc381u_r2FxLDcFP3zcS0oxu9iYHrLimrXHGTa0ADQuYweFQaJS6ULzi8ZJpM1x1_QW21DyuTrXjyz5sAE8OSrfq6Aj-xK47VNdX6cFrTOFYDugdehqQozw44nginwFJlSHfdQhlhKTJRSr736Y8qyBF5HkpsDVfz9FchJ5emr5jfYyF5NeUt9ipC9Q07D7GMk0IEm5DKSj0PkLW-viOIUrYxyHLZeW2G6RxLzbwaiRyKD4M-x23oY16nPIhnM_acBAOI=', start_index=10566)
Annotation(end_index=10579, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtt5VLqyhUiBzTlrQsLc-C78hLtmn8l7XFymmy_dPVmeaDJGaHrcnSkCyg0ihRhsFrm0SlLWNTLnr6oR2xfSgV0EWq0e6Ls3SMi-rhx-aufn5WJIau1dfSCOUXw0EwqxW8jJ9vNzKqg4eBRGG9jhx2s-zbyEJbo4eajeTTJKddx-7ikiK3EwY6v_Kf3jLAQTudFK3Fx_ki3xfxhYrWKbo=', start_index=10566)
Annotation(end_index=10882, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmJUntTkuWaZM4D-PuIcB98L9ZCxPcVlCzTppvD8rul_DdqsCrX-kuYhfnnR-d_GmDUKnRvGRZlQWG0BP4F5kCzW7-uXeaJP6t48m1jiSlqWDmj95Ls5j5FI0ukecGI1omY_OKF9Ug', start_index=10868)
Annotation(end_index=10882, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-Wb-_J9aKPopRaC_rolwMNEbf0ypvrBujxZJP3isXyNZUUQjkgW6s3wMqSGlp8WUeV55SpGuM8fzz0LD1TNNreqAL67qsC7ftY-K01XOaT1RNkXm0SY2R6RaEjoeWqb72oNX5dBgHAPQTikzXOycOWP_DROX2kJ4GrShmmkOUCPJH-rD4_SrYMaQ-ZQn4aj1Gh1czrRIt5UyRqnWfXIO5_HtYvhyajoMzCB5ttPmVMjOjXIRiwPOH_b9sxvebdQhhjyHl230fak8rUk30XGw=', start_index=10868)
Annotation(end_index=11184, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-Wb-_J9aKPopRaC_rolwMNEbf0ypvrBujxZJP3isXyNZUUQjkgW6s3wMqSGlp8WUeV55SpGuM8fzz0LD1TNNreqAL67qsC7ftY-K01XOaT1RNkXm0SY2R6RaEjoeWqb72oNX5dBgHAPQTikzXOycOWP_DROX2kJ4GrShmmkOUCPJH-rD4_SrYMaQ-ZQn4aj1Gh1czrRIt5UyRqnWfXIO5_HtYvhyajoMzCB5ttPmVMjOjXIRiwPOH_b9sxvebdQhhjyHl230fak8rUk30XGw=', start_index=11174)
Annotation(end_index=11925, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8q3GWkXRwbYhcQv9fMJ9isZ6d_WfX4XwycXHxg4JSEsB2cbhw22TZCRjF1qwu3qAuNlU4M6Hs8jE1BrHv-HzzfAoV1rv6Tb9e4NuyHFssjQRUdPmmkZDjAHhMEUWf', start_index=11909)
Annotation(end_index=11925, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSXNP4HJtMeacfjMBvZ1lvIr_Ao-qac-ETMdtDmJvQj6JC2c4hoWxLMJbJr4hj-hBgkn_DfRA4C3wjTlC_8WcOXsmqj2LI5f865t8Yzwg49G04KqzFrvcoOmAfPOQIxzHuh3DRbINKMFzEPysfGBoh2rKnhHtWLzv9JDX0EtTq4Q517m3Bg0gfHhDOUogOPBeiJQ7nIwuRpC7Osi-bAcXee1pqZB3GDzsJzfICJbtekzX_s3ohk8TBST-KPlBw', start_index=11909)
Annotation(end_index=11925, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5SWoJjA7SMatcNMDwJ5_ArBQQQRtQ4LkNaxo1XYJg37cr2fxEjVSJB53UU-A0Gr-JKiOXd6NBUD19ZS7yVmIwKUYEBHS_LqPK3RpKOQUlE55es_RxkLGwKcFH4NMm4M6hPTgXhCmIyGOU99geW9yKmVE-', start_index=11909)
Annotation(end_index=12112, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8q3GWkXRwbYhcQv9fMJ9isZ6d_WfX4XwycXHxg4JSEsB2cbhw22TZCRjF1qwu3qAuNlU4M6Hs8jE1BrHv-HzzfAoV1rv6Tb9e4NuyHFssjQRUdPmmkZDjAHhMEUWf', start_index=12095)
Annotation(end_index=12112, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIrhRh-QpoJp231XV2yMokVf9usXK0B-AEanuGOa-ustmstE_2ztBO9BwurIAmgIWLbEIG-B96jiEx6BYFAJo_U2Nqm9VFWCBPas46bSyOmrO1TSEZvVVxUkSYN7IB3FgRQ2WkKVE_Sqwju3HVlbE6f_yRkiXhzh7d8npO1FB5d2H7oe7mS5BV945Uu9SPrmgCnMJR6eOblYQiSNZPU7S_', start_index=12095)
Annotation(end_index=12112, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoXT3tNy8mXv_KogK4z_TBp-UCliF_GjNN-gxLeLEIgL6Gud0pRP4YNK9J96iDeMCI6x2tgvQx9vEkqeT9gND5-j1XuSmAzcLFygPhfdizi5a8Q24NJ_gVfY19lSaqnqEv4PphiKE3BzHqgL61vifmylhK0We8u_gM9zbFJ1OiFW6UmY64Aij1Zz9VZNtglHgUSkdBSOvgd3ZUrVGgv1aiFPYelAlqwERkk8fwfpG4Bo77q77ZlkfCDL5q4tXxnxsftkDEXkTxUd0=', start_index=12095)
Annotation(end_index=12580, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF80J-sg6qryFIO6cJgOFcBt6W2WtAf3AuTJPcSH1rvEYQ1WYl7TcxKuD_qhXbF_8tJ0ZqVJM52PEjxMwZRz48r10IVzP81zbN1tUDtd9ffaXgC8fxBTBXUPtXq9wYaL9g=', start_index=12558)
Annotation(end_index=12580, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGj6HoU0BFDWe90UjiPXdEOOZB1xh1veMURxmPufwwI7-OV-VvIequyRGSzkJ-F3T78njSYguzvift156Q-zOZoD6hwDcxHzB5Be6mI0D9dBOG6KeKlhO4927RZf0AL0AYFXCwl1z1clmEtQivjQjDrhTfkYtW1MDnaXZNcB1Osg-BGdrc97vefdcDruAHupRRaiVaEswHpGMFILcdr-LasS31FLUCMWYOimySuYQ==', start_index=12558)
Annotation(end_index=12580, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIrhRh-QpoJp231XV2yMokVf9usXK0B-AEanuGOa-ustmstE_2ztBO9BwurIAmgIWLbEIG-B96jiEx6BYFAJo_U2Nqm9VFWCBPas46bSyOmrO1TSEZvVVxUkSYN7IB3FgRQ2WkKVE_Sqwju3HVlbE6f_yRkiXhzh7d8npO1FB5d2H7oe7mS5BV945Uu9SPrmgCnMJR6eOblYQiSNZPU7S_', start_index=12558)
Annotation(end_index=12580, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoXT3tNy8mXv_KogK4z_TBp-UCliF_GjNN-gxLeLEIgL6Gud0pRP4YNK9J96iDeMCI6x2tgvQx9vEkqeT9gND5-j1XuSmAzcLFygPhfdizi5a8Q24NJ_gVfY19lSaqnqEv4PphiKE3BzHqgL61vifmylhK0We8u_gM9zbFJ1OiFW6UmY64Aij1Zz9VZNtglHgUSkdBSOvgd3ZUrVGgv1aiFPYelAlqwERkk8fwfpG4Bo77q77ZlkfCDL5q4tXxnxsftkDEXkTxUd0=', start_index=12558)
Annotation(end_index=12856, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF80J-sg6qryFIO6cJgOFcBt6W2WtAf3AuTJPcSH1rvEYQ1WYl7TcxKuD_qhXbF_8tJ0ZqVJM52PEjxMwZRz48r10IVzP81zbN1tUDtd9ffaXgC8fxBTBXUPtXq9wYaL9g=', start_index=12838)
Annotation(end_index=12856, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGj6HoU0BFDWe90UjiPXdEOOZB1xh1veMURxmPufwwI7-OV-VvIequyRGSzkJ-F3T78njSYguzvift156Q-zOZoD6hwDcxHzB5Be6mI0D9dBOG6KeKlhO4927RZf0AL0AYFXCwl1z1clmEtQivjQjDrhTfkYtW1MDnaXZNcB1Osg-BGdrc97vefdcDruAHupRRaiVaEswHpGMFILcdr-LasS31FLUCMWYOimySuYQ==', start_index=12838)
Annotation(end_index=12856, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIrhRh-QpoJp231XV2yMokVf9usXK0B-AEanuGOa-ustmstE_2ztBO9BwurIAmgIWLbEIG-B96jiEx6BYFAJo_U2Nqm9VFWCBPas46bSyOmrO1TSEZvVVxUkSYN7IB3FgRQ2WkKVE_Sqwju3HVlbE6f_yRkiXhzh7d8npO1FB5d2H7oe7mS5BV945Uu9SPrmgCnMJR6eOblYQiSNZPU7S_', start_index=12838)
Annotation(end_index=13343, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFD3haVdIfox8vaExvxGIn4U9xryyyRkA3wADcMmKjvzIh7kxafTLMvg9n4bQZb2AUKmHLjGvqd0LRX1oCINxaa94Hv5juvwSOuZh5GM1BvJ2CXNLEOdm2TTVPgxLKNjJsn3BVpHw6Oefa1iniuVXTXcSp6pmZwUje5P5K4AxSn-4zXuy_iIkAJ6HutLaBb0AJg0763j3SA9OrsFkcNjdkrJW1D_tj5sYEGgQWxLNU=', start_index=13329)
Annotation(end_index=13343, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIZ5CIkLKOrOP3VenaFeLHVD2yVU5lQmbSZPul6SUE61pCrNlmdWL8BUew_upda0WYAR9WR3fOV9auukQ_MKJmtJRiiRmBS212PSE3MNihr0UCtoRYVo0doXzDTGK2gFGXYGw=', start_index=13329)
Annotation(end_index=13507, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIrhRh-QpoJp231XV2yMokVf9usXK0B-AEanuGOa-ustmstE_2ztBO9BwurIAmgIWLbEIG-B96jiEx6BYFAJo_U2Nqm9VFWCBPas46bSyOmrO1TSEZvVVxUkSYN7IB3FgRQ2WkKVE_Sqwju3HVlbE6f_yRkiXhzh7d8npO1FB5d2H7oe7mS5BV945Uu9SPrmgCnMJR6eOblYQiSNZPU7S_', start_index=13497)
Annotation(end_index=13825, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIrhRh-QpoJp231XV2yMokVf9usXK0B-AEanuGOa-ustmstE_2ztBO9BwurIAmgIWLbEIG-B96jiEx6BYFAJo_U2Nqm9VFWCBPas46bSyOmrO1TSEZvVVxUkSYN7IB3FgRQ2WkKVE_Sqwju3HVlbE6f_yRkiXhzh7d8npO1FB5d2H7oe7mS5BV945Uu9SPrmgCnMJR6eOblYQiSNZPU7S_', start_index=13815)
Annotation(end_index=14978, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoKunknjZteTo_pL3DRi56mrD1ZSlUvmORbPXZ035dvvgWzZnv7CXjYFhP0aC0T9BFSKsFRaslbnA-pMawGi7AFp2icImJ9LrBt3wOwg9gm-YLco4WAE4tAeOuhGmKcEDooauwHyP_y-G214Qz_xZM6Ap_0Fc_bn4UY9zvubUtCv-r7UYy_p_YSBV_rtVkCr9mCQpD0NU4nXKyY3jToqezM-HOyppZwFfm9SLPA8UyBO_JYjW0P_4zkavR7XpBz-nB', start_index=14963)
Annotation(end_index=14978, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGt3h90k_K_r2JYvQKox3YPXXGfza5x7vhbncpVbxA8dtODsTYMS964uS5_rmCufOd2XboMEMT_n0qUDHdELQue_3sdExGjIMh3LEBS0epP9J4Ewo7geXcJJ8pEOGUtaGE6-pwQdJCmVNxiiBQGKW4VloE_nQ==', start_index=14963)
Annotation(end_index=14978, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtt5VLqyhUiBzTlrQsLc-C78hLtmn8l7XFymmy_dPVmeaDJGaHrcnSkCyg0ihRhsFrm0SlLWNTLnr6oR2xfSgV0EWq0e6Ls3SMi-rhx-aufn5WJIau1dfSCOUXw0EwqxW8jJ9vNzKqg4eBRGG9jhx2s-zbyEJbo4eajeTTJKddx-7ikiK3EwY6v_Kf3jLAQTudFK3Fx_ki3xfxhYrWKbo=', start_index=14963)
Annotation(end_index=15308, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7gTPRz07e4HpByZ9HTE0bOfafKt2n1x56YQZmi0JPCfjDT3hRStMtgW4vcgUjh3bBOk8W7j4olfYhMs-HdEE2_1NtawnrlCh1-IFIZKKAqxpnnQF5QTwDFttfbO2HU7kV5UIDjPegtooeEaUVmRtGRGF923ExIUlXwcQmIkP1HxiMOWUw5ZvZz4cFQTnSOzOYdJ0DnrQKR32TjE3SV-xUz3Dq', start_index=15295)
Annotation(end_index=15308, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoKunknjZteTo_pL3DRi56mrD1ZSlUvmORbPXZ035dvvgWzZnv7CXjYFhP0aC0T9BFSKsFRaslbnA-pMawGi7AFp2icImJ9LrBt3wOwg9gm-YLco4WAE4tAeOuhGmKcEDooauwHyP_y-G214Qz_xZM6Ap_0Fc_bn4UY9zvubUtCv-r7UYy_p_YSBV_rtVkCr9mCQpD0NU4nXKyY3jToqezM-HOyppZwFfm9SLPA8UyBO_JYjW0P_4zkavR7XpBz-nB', start_index=15295)
Annotation(end_index=15747, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHb4iTPTy5jMe93ptlsK8fjXqu4-tSdhJh8YzGUJpqri4OOlRouyB532w8XNu0c-DoFJZjLZl1CwX4S3A0I4V6qoJLBYXUYcCCiFYYeF4BGUJMYenGb5Oid7imEecBq6CFLXM6ppSuhgxr_hBRwQRpfZfDXm0wJbh06etHX0gXwWrww', start_index=15737)
Annotation(end_index=16735, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYOV3aXI1M1kUxJYkGZ15hPZ3TWiyX8wKOkYUr9rQ_qN9IlRpN0FeTJL1fmBdj8UB_SvKx_YRMYnVQJklco5RfSROSkTsg1Oxpo4Ljw26W3eHL7Q1ZCRCBkjPfQu9lIo3yA8RnB8GSzdWXxzuxTVxw2aTjxsUpLK2XMTY_mrIoWvDylKitueMmY2iJT7bU7mKq', start_index=16722)
Annotation(end_index=16735, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsn343uNMOp9tTv6sQODSstE0z6A3JRpnJPlXXFQNfbvN8zJ_0d0GOAL6f6mPtS0KrqWSbNx6z2broJiEQLlp6-WXyFv3gGRBVq30YSg2KZ5BUQTDZakRwLIgV_7rG2KC_ECHP-UDz9w==', start_index=16722)
Annotation(end_index=17362, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkhZyoLm2ZIGUa2tmxWheH8PsIL_K6AvJolYxB1IoHYiq3AVMxBIHJcb-nVVd7LT_OcImy4NW02sPXGZZMpHp6Fn46FAjfQUpkMYSyfpFQulTybgQb5UwCjhVTVX41hySgdi8U1LBeCMppqtUASzlY7Z4iCOVQbf5HAfhcXLCZv5ePFvFCPPPZLnVJNy8BWsviJXVRwjAfLUiiWIbEj-8C8HBsLrx2T4yyumzz1uS-qif3nzkLp9DatGzRwJ91vlYEAeNTO7YXuQXYbxph1uYOkWG21xeIEe8fSbazfkbc', start_index=17344)
Annotation(end_index=17362, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEyrb-m49eNEvrrCJKAWdOeo4AjlvSVg6D-CWHrCeWFUpZas-J41fmLfU30kF23ZUOKz7W13k5nLwwI_PTRtc_x1u_iF4v_PM12r8cpCgy55kCRTQholi707rIucoCtsrLc3LYRL4jZyeUwVekBj8AJjMZYnSchk8SgzDpwDQT4TD9NXpq4Zi23FzzquQ==', start_index=17344)
Annotation(end_index=17362, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZVUPjMRHqD6Pgh0JaI2t0dJuxNbjD5uAIRj2wesb1AQHKNKgOMUDAhh5przRd2vkAQplVKfHRKWGci95rFoeYYUuHgBYLbPG3ffmIp-gjZTxPsBQmjU9wdnM9te7vTZ7WrxiiHW3-miObOqRz3i2h5MdTE7iqS9pztQqUMi8zPBAa0QPo6LcbA3-v1s7cA2gxZY4vPgYv5wA=', start_index=17344)
Annotation(end_index=18262, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0DrJEwZH6KDxTmB8y7nHxu6gwy3aU-zvT78fNgo0orLLNVx5WfJsc381u_r2FxLDcFP3zcS0oxu9iYHrLimrXHGTa0ADQuYweFQaJS6ULzi8ZJpM1x1_QW21DyuTrXjyz5sAE8OSrfq6Aj-xK47VNdX6cFrTOFYDugdehqQozw44nginwFJlSHfdQhlhKTJRSr736Y8qyBF5HkpsDVfz9FchJ5emr5jfYyF5NeUt9ipC9Q07D7GMk0IEm5DKSj0PkLW-viOIUrYxyHLZeW2G6RxLzbwaiRyKD4M-x23oY16nPIhnM_acBAOI=', start_index=18244)
Annotation(end_index=18262, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCqp79pAmIrtDBvY6nKytFOSrUQgqbNGxdTZddHKC8JzxIqPDiraS6YXXzseKJqT4bEITwGnm_b1JXHG_BWpO6W2SuzLXtEDFHlSpPG3iZA-KP4GZj9PR2nEqF6oz_IGReU2xIKhDOhit_Uk53lT7JNnS0m_h4UDdndAIj', start_index=18244)
Annotation(end_index=18262, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGn5yLOV_THGuMu9QH-RpXxhsM2y6J5q-vLO5ioUl3gaK7DDQVX-8xPGFrx7WtHUEZe-1YR9ODdRgp7UolalGeSo0FBaffcTgUKp8gd5oz_PhfvlLSlai2lJrpzDxGu', start_index=18244)
Annotation(end_index=18788, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGS0_lRGVYHUmaAjfyrf3FyKN2_F7mh0Q1O_FszfrvSWzcEJt-VXG2JTcvVKo_DjSLr2IccWBRFzSq2SvTB8a82PazIymAF93vyXeJagthi40wYGLzCx6ABuWUs3p_jhiYArzzJW1wE2BCjG5rgmiEhW-LT_7NeO77f4vD_ZNt6W9T9pxOTB3kPno7MZKRieY8vt_3C1ZwqaFXC6U_ZRnov57wk8v5yBN8sa-8kTr8bW_fnukT9czY-ids=', start_index=18778)
Annotation(end_index=20291, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0DrJEwZH6KDxTmB8y7nHxu6gwy3aU-zvT78fNgo0orLLNVx5WfJsc381u_r2FxLDcFP3zcS0oxu9iYHrLimrXHGTa0ADQuYweFQaJS6ULzi8ZJpM1x1_QW21DyuTrXjyz5sAE8OSrfq6Aj-xK47VNdX6cFrTOFYDugdehqQozw44nginwFJlSHfdQhlhKTJRSr736Y8qyBF5HkpsDVfz9FchJ5emr5jfYyF5NeUt9ipC9Q07D7GMk0IEm5DKSj0PkLW-viOIUrYxyHLZeW2G6RxLzbwaiRyKD4M-x23oY16nPIhnM_acBAOI=', start_index=20281)
Annotation(end_index=20381, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGt3h90k_K_r2JYvQKox3YPXXGfza5x7vhbncpVbxA8dtODsTYMS964uS5_rmCufOd2XboMEMT_n0qUDHdELQue_3sdExGjIMh3LEBS0epP9J4Ewo7geXcJJ8pEOGUtaGE6-pwQdJCmVNxiiBQGKW4VloE_nQ==', start_index=20372)
Annotation(end_index=20474, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-Wb-_J9aKPopRaC_rolwMNEbf0ypvrBujxZJP3isXyNZUUQjkgW6s3wMqSGlp8WUeV55SpGuM8fzz0LD1TNNreqAL67qsC7ftY-K01XOaT1RNkXm0SY2R6RaEjoeWqb72oNX5dBgHAPQTikzXOycOWP_DROX2kJ4GrShmmkOUCPJH-rD4_SrYMaQ-ZQn4aj1Gh1czrRIt5UyRqnWfXIO5_HtYvhyajoMzCB5ttPmVMjOjXIRiwPOH_b9sxvebdQhhjyHl230fak8rUk30XGw=', start_index=20464)
Annotation(end_index=20565, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsn343uNMOp9tTv6sQODSstE0z6A3JRpnJPlXXFQNfbvN8zJ_0d0GOAL6f6mPtS0KrqWSbNx6z2broJiEQLlp6-WXyFv3gGRBVq30YSg2KZ5BUQTDZakRwLIgV_7rG2KC_ECHP-UDz9w==', start_index=20556)
Annotation(end_index=20653, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoKunknjZteTo_pL3DRi56mrD1ZSlUvmORbPXZ035dvvgWzZnv7CXjYFhP0aC0T9BFSKsFRaslbnA-pMawGi7AFp2icImJ9LrBt3wOwg9gm-YLco4WAE4tAeOuhGmKcEDooauwHyP_y-G214Qz_xZM6Ap_0Fc_bn4UY9zvubUtCv-r7UYy_p_YSBV_rtVkCr9mCQpD0NU4nXKyY3jToqezM-HOyppZwFfm9SLPA8UyBO_JYjW0P_4zkavR7XpBz-nB', start_index=20644)
Annotation(end_index=20746, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF80J-sg6qryFIO6cJgOFcBt6W2WtAf3AuTJPcSH1rvEYQ1WYl7TcxKuD_qhXbF_8tJ0ZqVJM52PEjxMwZRz48r10IVzP81zbN1tUDtd9ffaXgC8fxBTBXUPtXq9wYaL9g=', start_index=20736)
Annotation(end_index=20815, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHoXT3tNy8mXv_KogK4z_TBp-UCliF_GjNN-gxLeLEIgL6Gud0pRP4YNK9J96iDeMCI6x2tgvQx9vEkqeT9gND5-j1XuSmAzcLFygPhfdizi5a8Q24NJ_gVfY19lSaqnqEv4PphiKE3BzHqgL61vifmylhK0We8u_gM9zbFJ1OiFW6UmY64Aij1Zz9VZNtglHgUSkdBSOvgd3ZUrVGgv1aiFPYelAlqwERkk8fwfpG4Bo77q77ZlkfCDL5q4tXxnxsftkDEXkTxUd0=', start_index=20805)
Annotation(end_index=20905, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIrhRh-QpoJp231XV2yMokVf9usXK0B-AEanuGOa-ustmstE_2ztBO9BwurIAmgIWLbEIG-B96jiEx6BYFAJo_U2Nqm9VFWCBPas46bSyOmrO1TSEZvVVxUkSYN7IB3FgRQ2WkKVE_Sqwju3HVlbE6f_yRkiXhzh7d8npO1FB5d2H7oe7mS5BV945Uu9SPrmgCnMJR6eOblYQiSNZPU7S_', start_index=20895)
Annotation(end_index=20988, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFE3tkrphigF97e9R-MiZejrM5HOENP82ub2RIKj0PM6oCIMPho_hTcozfkTqKk2dE8Bf9-mfMMVTh-efn_9k33rzx96hYBkr2Xvr7L7OSB_Nben8EG0TVpeTB-xF3Dy8x8z51zM5jvmK3DrpnYSjZakM7Po6DvSOjNTXLoOqHgY6Hs', start_index=20979)
Annotation(end_index=21071, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGn5yLOV_THGuMu9QH-RpXxhsM2y6J5q-vLO5ioUl3gaK7DDQVX-8xPGFrx7WtHUEZe-1YR9ODdRgp7UolalGeSo0FBaffcTgUKp8gd5oz_PhfvlLSlai2lJrpzDxGu', start_index=21061)
Annotation(end_index=21157, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUecUh0tJeuMhLRpFuIqV_tF0jgbXC1LZlJtoWldEO9T-mZfrtbbpyjzeXl7TENGUDtZH76yMncyUzjN_2AsWcVZK_CdcRQFutCOMd4fLOi2wiRHZVQmsLDw4oQx4DKxistZ5ZqcVqtiaI4d4Ewti8rGYXczu6choAe6qhsN5Za9_SZGuF-OwGnLPbopHtMkPZhbWc1TFrdEqcLQThbnv8JWMYMvt6LyagxX4N', start_index=21148)
Annotation(end_index=21198, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGt3h90k_K_r2JYvQKox3YPXXGfza5x7vhbncpVbxA8dtODsTYMS964uS5_rmCufOd2XboMEMT_n0qUDHdELQue_3sdExGjIMh3LEBS0epP9J4Ewo7geXcJJ8pEOGUtaGE6-pwQdJCmVNxiiBQGKW4VloE_nQ==', start_index=21189)
Annotation(end_index=21276, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG-Wb-_J9aKPopRaC_rolwMNEbf0ypvrBujxZJP3isXyNZUUQjkgW6s3wMqSGlp8WUeV55SpGuM8fzz0LD1TNNreqAL67qsC7ftY-K01XOaT1RNkXm0SY2R6RaEjoeWqb72oNX5dBgHAPQTikzXOycOWP_DROX2kJ4GrShmmkOUCPJH-rD4_SrYMaQ-ZQn4aj1Gh1czrRIt5UyRqnWfXIO5_HtYvhyajoMzCB5ttPmVMjOjXIRiwPOH_b9sxvebdQhhjyHl230fak8rUk30XGw=', start_index=21266)
Annotation(end_index=21343, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHb4iTPTy5jMe93ptlsK8fjXqu4-tSdhJh8YzGUJpqri4OOlRouyB532w8XNu0c-DoFJZjLZl1CwX4S3A0I4V6qoJLBYXUYcCCiFYYeF4BGUJMYenGb5Oid7imEecBq6CFLXM6ppSuhgxr_hBRwQRpfZfDXm0wJbh06etHX0gXwWrww', start_index=21333)
Annotation(end_index=21378, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFD3haVdIfox8vaExvxGIn4U9xryyyRkA3wADcMmKjvzIh7kxafTLMvg9n4bQZb2AUKmHLjGvqd0LRX1oCINxaa94Hv5juvwSOuZh5GM1BvJ2CXNLEOdm2TTVPgxLKNjJsn3BVpHw6Oefa1iniuVXTXcSp6pmZwUje5P5K4AxSn-4zXuy_iIkAJ6HutLaBb0AJg0763j3SA9OrsFkcNjdkrJW1D_tj5sYEGgQWxLNU=', start_index=21368)
Annotation(end_index=21423, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRjlxKxLkbQpfOY3KKB_bu5vyIOz-1MZZJhenkUacGT39AuRN1ksUsf54SrWzJd_HA5vWf4tdc5kQ5Qg1G8DBI5MCVOxIy2-Q9Irqo5eNrDAIUIInptKAd3211yNM934hpVLpTMnX3SvQICSqXLcQUlb3qi6Mbp9fre_15oKey_eo4OydYaADltYhL0zZRZkw6j4wz8uV25YUBnfM5QPF1znvONRStO_Qtj5UbMeRc-5oNqZCD5Hxbmou6pJ54QLnpJEYNmPstpabZtYTfFsZvUlZ-fPuesIuuV6SisLVjgpPZn7LiRKk=', start_index=21413)
Annotation(end_index=21515, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0DrJEwZH6KDxTmB8y7nHxu6gwy3aU-zvT78fNgo0orLLNVx5WfJsc381u_r2FxLDcFP3zcS0oxu9iYHrLimrXHGTa0ADQuYweFQaJS6ULzi8ZJpM1x1_QW21DyuTrXjyz5sAE8OSrfq6Aj-xK47VNdX6cFrTOFYDugdehqQozw44nginwFJlSHfdQhlhKTJRSr736Y8qyBF5HkpsDVfz9FchJ5emr5jfYyF5NeUt9ipC9Q07D7GMk0IEm5DKSj0PkLW-viOIUrYxyHLZeW2G6RxLzbwaiRyKD4M-x23oY16nPIhnM_acBAOI=', start_index=21505)
Annotation(end_index=21605, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFE3tkrphigF97e9R-MiZejrM5HOENP82ub2RIKj0PM6oCIMPho_hTcozfkTqKk2dE8Bf9-mfMMVTh-efn_9k33rzx96hYBkr2Xvr7L7OSB_Nben8EG0TVpeTB-xF3Dy8x8z51zM5jvmK3DrpnYSjZakM7Po6DvSOjNTXLoOqHgY6Hs', start_index=21596)
Annotation(end_index=21677, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUecUh0tJeuMhLRpFuIqV_tF0jgbXC1LZlJtoWldEO9T-mZfrtbbpyjzeXl7TENGUDtZH76yMncyUzjN_2AsWcVZK_CdcRQFutCOMd4fLOi2wiRHZVQmsLDw4oQx4DKxistZ5ZqcVqtiaI4d4Ewti8rGYXczu6choAe6qhsN5Za9_SZGuF-OwGnLPbopHtMkPZhbWc1TFrdEqcLQThbnv8JWMYMvt6LyagxX4N', start_index=21668)
Annotation(end_index=21760, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhBS324KlxzihEcqx6uKD-noSiyKj9Yxx86HmMjXhWa7R29I-_unn70nm5i2Bu94-jNGPnY-DLxSbPlKMrpQdevmlSrwvWJjvrWNeD3d7FoRBcFZwli5StrtaSfaS8mYUI3MeSZC_yQYB8q__vBfHczoyltlNMmcDIkB5aJY7SzzQv1G0YCB91NL1E_V6lcM4WufD2azDMMaK8fLf0vPX9LQCei1P0X9L7j7986tH9iBkhwsoLZcPhJdpquFExny5U', start_index=21751)
Annotation(end_index=21838, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8q3GWkXRwbYhcQv9fMJ9isZ6d_WfX4XwycXHxg4JSEsB2cbhw22TZCRjF1qwu3qAuNlU4M6Hs8jE1BrHv-HzzfAoV1rv6Tb9e4NuyHFssjQRUdPmmkZDjAHhMEUWf', start_index=21829)
Annotation(end_index=21908, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5SWoJjA7SMatcNMDwJ5_ArBQQQRtQ4LkNaxo1XYJg37cr2fxEjVSJB53UU-A0Gr-JKiOXd6NBUD19ZS7yVmIwKUYEBHS_LqPK3RpKOQUlE55es_RxkLGwKcFH4NMm4M6hPTgXhCmIyGOU99geW9yKmVE-', start_index=21899)
Annotation(end_index=21943, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmJUntTkuWaZM4D-PuIcB98L9ZCxPcVlCzTppvD8rul_DdqsCrX-kuYhfnnR-d_GmDUKnRvGRZlQWG0BP4F5kCzW7-uXeaJP6t48m1jiSlqWDmj95Ls5j5FI0ukecGI1omY_OKF9Ug', start_index=21933)
Annotation(end_index=22019, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtt5VLqyhUiBzTlrQsLc-C78hLtmn8l7XFymmy_dPVmeaDJGaHrcnSkCyg0ihRhsFrm0SlLWNTLnr6oR2xfSgV0EWq0e6Ls3SMi-rhx-aufn5WJIau1dfSCOUXw0EwqxW8jJ9vNzKqg4eBRGG9jhx2s-zbyEJbo4eajeTTJKddx-7ikiK3EwY6v_Kf3jLAQTudFK3Fx_ki3xfxhYrWKbo=', start_index=22010)
Annotation(end_index=22103, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFsn343uNMOp9tTv6sQODSstE0z6A3JRpnJPlXXFQNfbvN8zJ_0d0GOAL6f6mPtS0KrqWSbNx6z2broJiEQLlp6-WXyFv3gGRBVq30YSg2KZ5BUQTDZakRwLIgV_7rG2KC_ECHP-UDz9w==', start_index=22094)
Annotation(end_index=22179, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYOV3aXI1M1kUxJYkGZ15hPZ3TWiyX8wKOkYUr9rQ_qN9IlRpN0FeTJL1fmBdj8UB_SvKx_YRMYnVQJklco5RfSROSkTsg1Oxpo4Ljw26W3eHL7Q1ZCRCBkjPfQu9lIo3yA8RnB8GSzdWXxzuxTVxw2aTjxsUpLK2XMTY_mrIoWvDylKitueMmY2iJT7bU7mKq', start_index=22169)
Annotation(end_index=22277, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFD3haVdIfox8vaExvxGIn4U9xryyyRkA3wADcMmKjvzIh7kxafTLMvg9n4bQZb2AUKmHLjGvqd0LRX1oCINxaa94Hv5juvwSOuZh5GM1BvJ2CXNLEOdm2TTVPgxLKNjJsn3BVpHw6Oefa1iniuVXTXcSp6pmZwUje5P5K4AxSn-4zXuy_iIkAJ6HutLaBb0AJg0763j3SA9OrsFkcNjdkrJW1D_tj5sYEGgQWxLNU=', start_index=22267)
Annotation(end_index=22322, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHIZ5CIkLKOrOP3VenaFeLHVD2yVU5lQmbSZPul6SUE61pCrNlmdWL8BUew_upda0WYAR9WR3fOV9auukQ_MKJmtJRiiRmBS212PSE3MNihr0UCtoRYVo0doXzDTGK2gFGXYGw=', start_index=22312)

## Sources
