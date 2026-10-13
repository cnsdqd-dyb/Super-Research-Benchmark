# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 2/5 | **Run ID:** 7dcbf87a | **Time:** 1005.88s | **Cost:** $3.52299
--------------------------------------------------------------------------------

# Optimal Air Circulation Filtration Technologies for Space Station Life Support: A Trade-off Analysis of Microbial Control and Energy Consumption

### Key Points
*   **Current Standard (HEPA):** High-Efficiency Particulate Air (HEPA) filters, specifically Bacterial Filter Elements (BFEs), remain the primary defense against microbial contamination on the International Space Station (ISS). They offer 99.97% efficiency at 0.3 microns but impose a significant energy penalty due to high pressure drops that increase fan power requirements. They also present a "breeding ground" risk as they capture but do not destroy pathogens.
*   **Active Destruction (PCO):** Photocatalytic Oxidation (PCO) technology (e.g., Airocide) provides superior microbial control by destroying volatile organic compounds (VOCs), bacteria, and viruses rather than merely trapping them. While PCO units impose negligible pressure drop—saving fan energy—they require continuous electrical power for UV lamps, creating a different energy demand profile.
*   **Future Optimization (Scroll Filter System):** For deep space missions, the Scroll Filter System (SFS) represents the optimal trade-off between contamination control and *Equivalent System Mass* (ESM)—a metric combining mass, volume, and power. By automating pre-filtration, the SFS reduces the logistical energy cost of launching replacement filters and minimizes crew maintenance time, addressing the long-term energy and resource constraints better than static HEPA alone.
*   **The Trade-off Verdict:** While PCO offers the best *biological* efficacy per unit of airflow resistance, the high reliability and passive nature of HEPA make it the foundational technology. The "best" trade-off is currently a hybrid approach: HEPA for bulk particulate removal combined with targeted PCO for VOC and pathogen destruction, transitioning toward regenerative Scroll Filters to minimize life-cycle energy and mass costs for future exploration.

---

## 1. Introduction

In the closed-loop environment of a spacecraft, such as the International Space Station (ISS), air quality control is a critical life support function. The Environmental Control and Life Support System (ECLSS) must continuously remove particulate matter and microbial contaminants to protect crew health and equipment performance. Unlike terrestrial environments, spacecraft cannot vent air to the outside; thus, all contaminants must be filtered, captured, or destroyed internally.

The design of these filtration systems involves a complex optimization problem. Engineers must balance **microbial contamination control**—ensuring the removal of bacteria, fungi, and viruses that can thrive in the warm, humid, microgravity environment—against **energy consumption**. In space systems, "energy" is a multifaceted constraint involving direct electrical power (watts) to run fans and active devices, as well as the "embodied energy" of launch mass and volume (logistics).

This report analyzes the primary air filtration technologies deployed or in development for space station life support, evaluating them based on their microbial efficiency, energy profiles, and logistical footprints.

## 2. The Baseline Standard: High-Efficiency Particulate Air (HEPA) Filtration

### 2.1 Technology Overview
The backbone of the ISS air revitalization system is the Bacterial Filter Element (BFE). These units utilize High-Efficiency Particulate Air (HEPA) media, designed to capture at least 99.97% of airborne particles 0.3 microns in diameter, with even higher efficiencies for larger and smaller particles due to diffusion and impaction mechanisms [cite: 1, 2]. On the ISS, these filters are often integrated with activated charcoal to form Charcoal HEPA Integrated Particle Scrubbers (CHIPS), allowing for the simultaneous removal of siloxanes and other trace contaminants [cite: 3].

### 2.2 Microbial Control Performance
HEPA filters are highly effective at *capturing* microbial contaminants. Studies of returned ISS filters have confirmed their ability to trap bacteria and fungi, maintaining cabin air quality within safe limits [cite: 4]. However, a critical limitation of HEPA filtration is that it is a passive capture mechanism; it does not kill the trapped microorganisms.
*   **The "Breeding Ground" Risk:** In the humid environment of the ISS, trapped organic matter (skin flakes, lint) can serve as a nutrient source for microbes. If humidity control fails or local condensation occurs, the filter media can become a substrate for microbial growth, potentially releasing metabolic byproducts or spores back into the cabin during maintenance or pressure fluctuations [cite: 5, 6].
*   **Efficiency:** While capture efficiency is near 100% for standard bacterial sizes, HEPA filters do not actively degrade Volatile Organic Compounds (VOCs) produced by microbial metabolism or equipment off-gassing [cite: 7].

### 2.3 Energy Consumption and Trade-offs
The primary energy cost of HEPA filtration is **fan power**.
*   **Pressure Drop:** HEPA media is dense, creating significant resistance to airflow (pressure drop). To maintain the required ventilation rates for CO2 removal and temperature control, fans must operate at high speeds, consuming substantial electrical power [cite: 8, 9].
*   **Loading Penalty:** As the filter loads with dust and debris over its service life (typically 1 to 5 years depending on location), the pressure drop increases. This forces the fans to work harder to maintain the same volumetric flow rate, thereby increasing energy consumption over time [cite: 1, 10].
*   **Logistical Energy:** HEPA filters are expendable consumables. They must be replaced periodically, requiring new filters to be launched from Earth. This contributes to a high Equivalent System Mass (ESM), as valuable launch capacity is used for spare filters rather than scientific payload or other supplies [cite: 11, 12].

## 3. Active Destruction: Photocatalytic Oxidation (PCO)

### 3.1 Technology Overview
Photocatalytic Oxidation (PCO) technology, commercialized as Airocide, was developed from NASA-funded research intended for plant growth chambers. It utilizes a reaction chamber packed with a catalyst (typically titanium dioxide, TiO2) coated on tubes or a matrix. When irradiated by high-intensity Ultraviolet (UV) light, the catalyst generates hydroxyl radicals and super-oxide ions [cite: 7, 13].

### 3.2 Microbial Control Performance
PCO offers a distinct advantage over HEPA: **destruction vs. capture**.
*   **Mechanism:** The hydroxyl radicals mineralize organic contaminants on contact, converting bacteria, viruses, mold spores, mycotoxins, and VOCs (such as ethylene) into trace amounts of carbon dioxide and water vapor [cite: 7, 14].
*   **Efficacy:** Airocide units have been proven to destroy virtually all airborne organic matter, including particles too small for HEPA filters, such as certain viruses and gas molecules [cite: 7, 15]. Crucially, because it destroys the pathogen, there is no risk of the device becoming a microbial breeding ground [cite: 16].

### 3.3 Energy Consumption and Trade-offs
The energy profile of PCO is fundamentally different from HEPA.
*   **Low Pressure Drop:** PCO units do not rely on dense fiber mats to trap particles. Instead, air flows through a relatively open reaction chamber. This results in a very low pressure drop, meaning the fan power required to move air through the device is minimal compared to a HEPA filter [cite: 17].
*   **Active Power Load:** The trade-off is the electrical power required to energize the UV lamps. While a HEPA filter is passive (requiring only fan power), a PCO unit has a constant "active" power draw for the light source [cite: 17].
*   **Thermal Load:** The UV lamps generate heat, which adds to the thermal load of the spacecraft cabin. This heat must be removed by the station's thermal control system, indirectly increasing the total energy burden of the ECLSS [cite: 18].

## 4. The Future of Deep Space Filtration: The Scroll Filter System (SFS)

### 4.1 Technology Overview
For long-duration missions to the Moon or Mars, the logistical chain for replacing HEPA filters becomes unsustainable. NASA Glenn Research Center has developed the Scroll Filter System (SFS) to address this. The SFS is a multi-stage system comprising a regenerable impactor (for coarse dust), a scrolling screen pre-filter, and a final HEPA stage [cite: 11, 19].

### 4.2 Microbial and Particulate Control
*   **Multi-stage Efficiency:** The SFS retains the high capture efficiency of HEPA for the final stage, ensuring that fine microbial contaminants are removed.
*   **Pre-filtration:** The scrolling screen and impactor remove larger debris (lint, hair, skin flakes) before they reach the HEPA media. This prevents the HEPA filter from clogging prematurely, extending its life and maintaining optimal microbial capture efficiency for longer periods [cite: 12, 20].

### 4.3 Energy and ESM Trade-offs
The SFS is designed specifically to optimize the **Equivalent System Mass (ESM)** trade-off.
*   **Regeneration:** The scrolling mechanism allows the pre-filter media to be refreshed automatically, or the impactor to be cleaned, without crew intervention. This significantly reduces the "crew time" energy cost and the mass of spare filters needed [cite: 11].
*   **Pressure Drop Management:** By preventing the HEPA stage from loading with coarse debris, the SFS maintains a lower average pressure drop over the system's life compared to a standard BFE. This stabilizes fan power consumption and prevents the energy spikes associated with clogged filters [cite: 19, 21].
*   **Mass Savings:** Trade studies indicate that the SFS offers significant reductions in launch mass compared to heritage HEPA architectures because fewer heavy spare units are required for multi-year missions [cite: 22].

## 5. Comparative Analysis: Finding the Best Trade-off

The "best" technology depends on how the trade-off is weighted between immediate power consumption, filtration efficiency, and long-term logistics.

### 5.1 Microbial Control vs. Energy Consumption Matrix

| Feature | **HEPA (BFE)** | **PCO (Airocide)** | **Scroll Filter System (SFS)** |
| :--- | :--- | :--- | :--- |
| **Microbial Action** | Capture (99.97% @ 0.3µm) | Destruction (Mineralization) | Capture (Multi-stage) |
| **Pathogen Risk** | Potential breeding ground | Eliminates risk | Reduced risk (frequent pre-filter refresh) |
| **VOC Removal** | None (unless combined with charcoal) | Excellent (Ethylene, odors) | None (unless combined with sorbents) |
| **Airflow Resistance** | High (Increases with load) | Low (Constant) | Moderate (Managed via regeneration) |
| **Fan Power** | High | Low | Moderate |
| **Active Power** | None (Passive) | High (UV Lamps) | Low (Intermittent motor for scroll) |
| **Logistics (Mass)** | High (Frequent replacement) | Low (Lamp replacement) | Low (Regenerable media) |

### 5.2 The Verdict

**For Absolute Microbial Sterility:**
**PCO (Airocide)** provides the best performance. It destroys pathogens that HEPA might miss or that might grow on filter media. However, it consumes continuous electrical power for its UV lamps and adds heat to the cabin. It is best used as a *supplement* to particulate filtration rather than a replacement, as it does not remove inorganic dust effectively [cite: 7, 16].

**For Energy Efficiency (Electrical):**
The trade-off is complex. **HEPA** systems consume more fan power due to high pressure drops, especially as they clog. **PCO** systems save fan power but consume lamp power. In a spacecraft where every watt counts, the passive nature of HEPA (despite the fan penalty) has historically been preferred for bulk air cleaning, with PCO reserved for specific high-risk or high-VOC applications (like plant growth chambers) [cite: 15, 23].

**For Long-Duration Life Support (ESM):**
The **Scroll Filter System (SFS)** represents the best holistic trade-off. By mechanically managing the particulate load, it minimizes the need for heavy spares (saving launch energy/mass) and maintains a lower, more consistent pressure drop (saving fan energy) than static HEPA filters. It addresses the "energy" of logistics and maintenance, which is the dominant constraint for Mars missions [cite: 11, 22].

## 6. Conclusion

In the context of space station life support, the technology providing the best trade-off between microbial contamination control and energy consumption is evolving.

Currently, **HEPA filtration** remains the standard due to its reliability and passive operation, despite the energy penalty of fan power and the logistical burden of replacement. However, for specific biological threats and VOC control, **Photocatalytic Oxidation (PCO)** offers superior *quality* of air (destruction vs. capture) at the cost of increased electrical and thermal loads.

Looking forward, the **Scroll Filter System (SFS)** is emerging as the superior architecture for deep space. It integrates the high capture efficiency of HEPA with regenerable pre-filtration to minimize the total energy footprint—encompassing both electrical power and the critical metric of launch mass. Therefore, while PCO is the most effective at *killing* microbes, the SFS provides the most balanced engineering solution for sustaining life support systems over long durations with limited energy resources.

### References
[cite: 7] NASA Spinoff. (2013). *Air Purifiers Eliminate Pathogens, Preserve Food*.
[cite: 4] Dunlap, D. S., et al. (2019). *Microbial Analysis of Return-To-Ground Node 1 Charcoal Air Filters from ISS*.
[cite: 24] Airocide. *Airocide's Unique Air Purification Technology*.
[cite: 23] NASA Spinoff. (2024). *Air Treatment Systems Break Down Pollutants, Germs*.
[cite: 1] Perry, J. L. (2005). *International Space Station Bacteria Filter Element Service Life Evaluation*.
[cite: 8] Perry, J. L. (1998). *Elements of Spacecraft Cabin Air Quality Control Design*.
[cite: 2] Agui, J. H., et al. (2016). *Particulate Filtration Design Considerations for Crewed Spacecraft Life Support Systems*.
[cite: 9] Lorenzetti, D. M., & Sohn, M. D. (2022). *Quantifying the tradeoff between energy consumption and the risk of airborne disease transmission*.
[cite: 11] Agui, J. H., & Vijayakumar, R. (2017). *Scroll Filter System Development for Crewed Deep Space Missions*.
[cite: 22] Agui, J. H. (2017). *Life Support Filtration System Trade Study for Deep Space Missions*.
[cite: 19] Agui, J. H. (2019). *Scroll Filter System Development for Crewed Deep Space Missions*.
[cite: 3] NASA Technical Reports Server. (2023). *Charcoal HEPA Integrated Particle Scrubbers (CHIPS)*.
[cite: 4] Dunlap, D. S., et al. (2019). *Microbial Analysis of Return-To-Ground Node 1 Charcoal Air Filters from ISS*.
[cite: 13] Airocide. (2021). *Airocide Brochure*.
[cite: 16] Space Apps Challenge. *New Air: Purify Air Supply*.
[cite: 14] Airocide. *Proof Book: Healthcare*.
[cite: 17] Abaco Air Experts. (2025). *Advanced Air Purifier Technology*.
[cite: 19] Agui, J. H. (2019). *Scroll Filter System Development for Crewed Deep Space Missions*.
[cite: 20] Agui, J. H. (2015). *Scroll Filter System Development*.
[cite: 15] Airocide Europe. *NASA and Airocide*.
[cite: 11] Agui, J. H. (2017). *Life Support Filtration System Trade Study for Deep Space Missions*.
[cite: 22] Agui, J. H. (2017). *Life Support Filtration System Trade Study for Deep Space Missions*.
[cite: 12] Agui, J. H. (2018). *Scroll Filter System Development*.
[cite: 5] Engadget. (2019). *ISS Bacteria NASA*.
[cite: 6] OhFeel. (2024). *Unveiling the Truth Behind Air Purifiers*.
[cite: 3] NASA Technical Reports Server. (2023). *Charcoal HEPA Integrated Particle Scrubbers (CHIPS)*.
[cite: 18] Reddit/NASA. (2015). *How much power is created/used on the ISS?*.
[cite: 10] ResearchGate. (2025). *Changes in Fan Energy Consumption According to Filters*.
[cite: 21] Agui, J. H. (2024). *Updated Scroll Filter System for Deep Space Missions*.

**Sources:**
1. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjcIKddUXZkE11qpmH4fU0EAWS7pXGXBQ1gRBILL_DgM_FSWMUitHXETMoUZYxbIcBRJfstlY2PMt8xBltgBwBc5T9Dd6IAEbUiUW7KHbkcxgTpaagLeNgXwOdaVww_h-9QeqsEhwjO5MxZK6RDBx8LzPCIn_rVpVM9X4wCJfy-ZbpXwRjuYGdV1rKz0akl9XIn4ij0DZ_xecp3rf1a0vnABa8hBn0WJqX8fR6WTMgjG9Ktg==)
2. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQES12RRuHv-5lV4jckpLtUdFxO9P0POnvoj4WkfmnedMPkH4PYywWEOqPr1krX_T92Dc5BJRFWFI1BH7REGnZjh5NiHRSbONjjGfuV3PODGgVsVVxMHsF3eSLeMJwDFonpwT9NXP-SCCgjJ_eH4wyPrFLUwZeL22epnvGLwatgk)
3. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMkDe8adfom6u0NBVOA9Sp04deSB-vYdrQpwi7b9StdRwd_JrdrgXVvYcngBwgOD9E6gevSP1pawo0M75e20tFoz6oI8sfy7HvxJReOftOdk1AqtDxWR2ihZPhW30INW_z)
4. [tdl.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGycYeQ-pdIZLXQgcOq9-pZLWzjxfaFC3HNMDQHswenOCDRWD5PB0v_hW_1koQE2FDffePjJvQSFONcIFICvpGeeUxOlz9e67FMkBbg2LLCXKKC5klc74sDPgjmO8MKULgUNuFqz4bQgAU__X9sFM93_WOQ0OZ5vommila4VgY7eLafoM23)
5. [engadget.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEK0-NfHM4wIuKAx1dhMciGbFzv1t9fJGg78qFGEmfYfmmc3dWsTmDr1eLNVVwlAgP0MN0M7cymNAxiFi3g0JH1k_KPiYWZPvovPptAlAdn6fMJgZVIEnDzxT2BtpyUrvoVTe4YCVG7rwtmMGY9aUni)
6. [ohfeel.gr](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGovqMIHZySgD14pOa-cLdH1qMhHYje_TXazkHlR3LwnsBbRz9Que25UEFsAEk2BJV-aNTWiyLXGTBMTP_aZc5Wgf2MyUiOTyKm-hXB5SjWDYUm3Fvpkjf78_HWqpz600Tre0WjuA5DHwWDFqUv5gjXE_r1UQ==)
7. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrskl1INrnpQ3VHU1-KbsB6ORxmZP4TqTXztAPJk-PJLX3YUHvC-7GZ41-HuJpOrp2egjLAwQrtltIgROUuRdEuyIfoRWKio-O9WyHcd6Br_5RXTI42pi6870X6GKda5Dh2pwC)
8. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGhDGQmGFbBWze0djsFyYbYf0RfFsKlMOrEK-J8dWdRi_5wusBIXAZrll3AfT1OAdGfae5fpexp4j8f4Sgks8Y_7_NfSFOrmhcNRAkfp9cu_0tbGni9V_8lzRaBOjzoOTR0zHHbYZ988eY9P8p8vDbn-1ed53f4wZlhAEOYxVPX)
9. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIODFIBUgsF-cZqqb0cjJUDsUvTntBKsAXgZg6PgqQqq30xapxh4Q1So6nMOxfg4ZSf06mQlHTVKrGCw_qFVuDUtR7wbZ-e4BH79K1NHfzNHZJllRslaSYK0LLuy4yD5V_w_HurdnL)
10. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGM8FBnPmNG39r3hON4DD1WBdpRulRQ09miDEnzrMEZ-VB9RBdh7yLK18mYGxKdWdv03SGt7UVR6PasUE-ynbhfYdmpXEMRI_zfrEAULQHKWN_QKQXbeC_RatFQXPESr_-vdwqh_2JiXwx-2gG58HUGsPiTXIkzceeR5O2mWCtSRxmszW4l4KM6pKilyoz_m3byKo_Rp4fmROYGAeM2JD87v_Ux-BxliJYvWzD6GBXLHODDJxdIRv3QLx8x-_D6WOsOuSIhZDPhre-i7B0VgCgiAVgCtF7BovzwewYz)
11. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6D5WVvmLB4YlaUx64wg9H-dG-0npQKaoChz6sxzE-1ny1QHA0-DhNIIC1K7PIcvyd_EMHSyG0ac4msM05SjMhWbRVOpLUThWbs0Z5aKfKD2jXyO-Qjo-O0ldDH1SPIFdyJ5_LyjbdI1rVJlmbUAnwzPDQUq9ssM0fH8Ajiup2)
12. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfUEFlZ1GgxYfalpKAzDtBH8UrNdtHMy2jIze97Zi43c9m22rHjB743BAXkBJ4AkJiRoX5_ronkedg7reFryMmExiPR-p2cahzy1XC7qscVmnhcRtUJ8jc5GsRu2pgD4chK9Khi99jOrSjbhJQzOHwkh-MvdFYIPccCSrUTofA)
13. [ceriumscientific.co.sz](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWvuxow0_weOrxSws7yZgIcPa-0xeq_1TbDcJelbt4sbpK7BnCm0aIXPPotT2Fl4bPU93-eiur4nz8KBB_CX_MmRlqFM4wF0ROaH-99KmqFOFSDgsyS53hkqi5cG3MU83v_cCt4M8pmr5iL7PwGpNrKKnx2o8efD6gYM0SX3mp2OeUTj410Yz8uA==)
14. [airocidelatam.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHO9L9Hq2WKf54XfhD_7h2PED7PsFqduSyAp0bdvYRFTI7U3zKKOc6IXsh1vaXt6-KHPAfolN97qkQjajzkQY3pA_twL76LuMeFGyOubgueB62G_AdX5w-c2zc-p3cmGtn6bpWGXPtV-SSwbcqKjaMv2EDHXLJfolVidsgaIV6l6-kitA==)
15. [airocide-europe.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWYpPKwLLqkCVDKJnOxe9HrX4rZ89TB55qEPp1_-VOvZnHEPuBd8r9bfS9CYn_81xryx1VOGIMMilLnsGOjVHp7SAWwciFmOV5ozpt1JA65oXpxuOAc8Uq7zgzuqeosAobRwCXIafylQ==)
16. [spaceappschallenge.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzVeZQGe_xY4xXeezTm1qkShCKwtDhh4p03Pp_spcVHo_kWOY42O-d3d66hRs9r12-xsZi3AfvuUMgaSwaT7jIlrHc6kQvOdVUw5_KR3Q9D0h0q2teM87e1vFk0SWrNcNghWTyqzUIAjl3u3M-yyNzPch9tp-ZjRpNe5h8GGF9NaAiHYS-HC1Dd7Nss4fG6VCbtNMGglmEsqE_L-A=)
17. [abacoairexperts.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERpn1DFsNI1hVAN_I2HGqD-HXfwBm3Rg-bV3uronmBm-8-OR1TObJlI7pVC1Deyz2WdWXFHBRIt8IEERb7iQmDzuiAPjxW4d4PgUiM9LWoUBRcytMaWACCd8vvw_xTD2SelqUkT8Jg8HKYLhM1-fEomS8doPb05wBmD9lsass=)
18. [reddit.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWrRWxIjZ1AWfkfHXq2N-bTIFWgmpQ3uuKTO5LiEBOrnuf6W9h0t3nBMhwc_A032-H5HZTGId1kpMvdyVftH4ZfHNO-hxEcii1plpSDZBGqVjRYkN_dm0kuwqhb0pbR5fpIRZFnxi-U9ErihF_qeCtyWbzjrMGsqq5uJNVDgauVOSiDxaaTPnayA2G0ldEMaa2orc=)
19. [tdl.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG83XC5RYk6jjAtknc9kAVIjJ0CFEl3WlZM89z1ILiXYUIfoU9a0LokNu6kS7DD9jH_dmFFwgJcPwWAb4Q60dQBpHkAI-uKUxxM5bPRYCC0IpGE0GeUNOZcEPRFM8C5KlpAOqK4Dum9jd8DL8sZx0hfyviYG6flL26XXz9yoXuxDGlf2PV4XKvpFBHjDKBAV7vs6YMI)
20. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEeXViorK_9MYonuuioqkGwaSQBCggDMvhSVETgmPvQaIjeRvNMvUzWsHkRRk_XDX_KIidWcE9kpl2ws6O-LOHo4oiF4lN9tsz_YUbzmeZccEL3Uudsc4N9vsbb32lNrcaNfAgLWxtu_JAOKQbllTYtkFGPo4Sr8ZKYxzY81n_P)
21. [tdl.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETACYpoX8pIhzLQiB3G3I0AQSg101Dg7OHPtVbqpuzXSIJeye-VbIRse9UDUW0rPtIn3xVpYtcILQdney28Gk26qcoo3kBZgVBr6bZ9qprKwJTJ7FNxZK3CNryTKcW66w_sgWRdSID8uDe3iMC3l1R63tGinEq8ia0_s5SMdcNAK2vT-lT)
22. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3XfTnIOw2D98AqOq6VasXpr2J2J1xsFstu1njdbRUFZcGc34D8AKv2Qcg52nK8eRKLQb8PdtwouF_Izh0HcvshVB3FZuCpNyCiWucZYqnI95dvC0bGkWECS4CsUkzpOesd-2qCRIbhx3FH0Bn2WtTJGbjdzTBNJfv0L8k3TmVq7k153LvFzgx5z5HEU4HQuRIveciZOBXKI7g6d-rfyTBKEfy0Is1uOQriBc=)
23. [nasa.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG743VorFDWnueHatiqUCAw9p7ZJst1AzgvrwU-pXrcGaoD3gR4IIQe5GSiOWNcdmysJ7hJRrbWY7hYHGj3sdXPZd-UNmklA7X3TpZDvCwE9n6mkvGbNmH7LebaFSzGALulfh_UI1-TpRiCPljKKHrafILIlVgyTgGT9YMFg8EVIA==)
24. [airocide.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7ua2xjzVKLYEghFbn946mJMYs8okqV9j27S3vTI7vNl7tAe1ADcfpFo_08rbLnZ2D0JoU19MvpfgU8tzlkWCbq5DcoPZsjVQjetFfNi85eb42-7Wk)


## Annotations
Annotation(end_index=3661, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQES12RRuHv-5lV4jckpLtUdFxO9P0POnvoj4WkfmnedMPkH4PYywWEOqPr1krX_T92Dc5BJRFWFI1BH7REGnZjh5NiHRSbONjjGfuV3PODGgVsVVxMHsF3eSLeMJwDFonpwT9NXP-SCCgjJ_eH4wyPrFLUwZeL22epnvGLwatgk', start_index=3649)
Annotation(end_index=3661, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjcIKddUXZkE11qpmH4fU0EAWS7pXGXBQ1gRBILL_DgM_FSWMUitHXETMoUZYxbIcBRJfstlY2PMt8xBltgBwBc5T9Dd6IAEbUiUW7KHbkcxgTpaagLeNgXwOdaVww_h-9QeqsEhwjO5MxZK6RDBx8LzPCIn_rVpVM9X4wCJfy-ZbpXwRjuYGdV1rKz0akl9XIn4ij0DZ_xecp3rf1a0vnABa8hBn0WJqX8fR6WTMgjG9Ktg==', start_index=3649)
Annotation(end_index=3884, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMkDe8adfom6u0NBVOA9Sp04deSB-vYdrQpwi7b9StdRwd_JrdrgXVvYcngBwgOD9E6gevSP1pawo0M75e20tFoz6oI8sfy7HvxJReOftOdk1AqtDxWR2ihZPhW30INW_z', start_index=3875)
Annotation(end_index=4145, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGycYeQ-pdIZLXQgcOq9-pZLWzjxfaFC3HNMDQHswenOCDRWD5PB0v_hW_1koQE2FDffePjJvQSFONcIFICvpGeeUxOlz9e67FMkBbg2LLCXKKC5klc74sDPgjmO8MKULgUNuFqz4bQgAU__X9sFM93_WOQ0OZ5vommila4VgY7eLafoM23', start_index=4136)
Annotation(end_index=4693, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEK0-NfHM4wIuKAx1dhMciGbFzv1t9fJGg78qFGEmfYfmmc3dWsTmDr1eLNVVwlAgP0MN0M7cymNAxiFi3g0JH1k_KPiYWZPvovPptAlAdn6fMJgZVIEnDzxT2BtpyUrvoVTe4YCVG7rwtmMGY9aUni', start_index=4681)
Annotation(end_index=4693, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGovqMIHZySgD14pOa-cLdH1qMhHYje_TXazkHlR3LwnsBbRz9Que25UEFsAEk2BJV-aNTWiyLXGTBMTP_aZc5Wgf2MyUiOTyKm-hXB5SjWDYUm3Fvpkjf78_HWqpz600Tre0WjuA5DHwWDFqUv5gjXE_r1UQ==', start_index=4681)
Annotation(end_index=4921, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrskl1INrnpQ3VHU1-KbsB6ORxmZP4TqTXztAPJk-PJLX3YUHvC-7GZ41-HuJpOrp2egjLAwQrtltIgROUuRdEuyIfoRWKio-O9WyHcd6Br_5RXTI42pi6870X6GKda5Dh2pwC', start_index=4912)
Annotation(end_index=5300, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIODFIBUgsF-cZqqb0cjJUDsUvTntBKsAXgZg6PgqQqq30xapxh4Q1So6nMOxfg4ZSf06mQlHTVKrGCw_qFVuDUtR7wbZ-e4BH79K1NHfzNHZJllRslaSYK0LLuy4yD5V_w_HurdnL', start_index=5288)
Annotation(end_index=5300, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGhDGQmGFbBWze0djsFyYbYf0RfFsKlMOrEK-J8dWdRi_5wusBIXAZrll3AfT1OAdGfae5fpexp4j8f4Sgks8Y_7_NfSFOrmhcNRAkfp9cu_0tbGni9V_8lzRaBOjzoOTR0zHHbYZ988eY9P8p8vDbn-1ed53f4wZlhAEOYxVPX', start_index=5288)
Annotation(end_index=5607, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjcIKddUXZkE11qpmH4fU0EAWS7pXGXBQ1gRBILL_DgM_FSWMUitHXETMoUZYxbIcBRJfstlY2PMt8xBltgBwBc5T9Dd6IAEbUiUW7KHbkcxgTpaagLeNgXwOdaVww_h-9QeqsEhwjO5MxZK6RDBx8LzPCIn_rVpVM9X4wCJfy-ZbpXwRjuYGdV1rKz0akl9XIn4ij0DZ_xecp3rf1a0vnABa8hBn0WJqX8fR6WTMgjG9Ktg==', start_index=5594)
Annotation(end_index=5607, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGM8FBnPmNG39r3hON4DD1WBdpRulRQ09miDEnzrMEZ-VB9RBdh7yLK18mYGxKdWdv03SGt7UVR6PasUE-ynbhfYdmpXEMRI_zfrEAULQHKWN_QKQXbeC_RatFQXPESr_-vdwqh_2JiXwx-2gG58HUGsPiTXIkzceeR5O2mWCtSRxmszW4l4KM6pKilyoz_m3byKo_Rp4fmROYGAeM2JD87v_Ux-BxliJYvWzD6GBXLHODDJxdIRv3QLx8x-_D6WOsOuSIhZDPhre-i7B0VgCgiAVgCtF7BovzwewYz', start_index=5594)
Annotation(end_index=5936, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfUEFlZ1GgxYfalpKAzDtBH8UrNdtHMy2jIze97Zi43c9m22rHjB743BAXkBJ4AkJiRoX5_ronkedg7reFryMmExiPR-p2cahzy1XC7qscVmnhcRtUJ8jc5GsRu2pgD4chK9Khi99jOrSjbhJQzOHwkh-MvdFYIPccCSrUTofA', start_index=5922)
Annotation(end_index=5936, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6D5WVvmLB4YlaUx64wg9H-dG-0npQKaoChz6sxzE-1ny1QHA0-DhNIIC1K7PIcvyd_EMHSyG0ac4msM05SjMhWbRVOpLUThWbs0Z5aKfKD2jXyO-Qjo-O0ldDH1SPIFdyJ5_LyjbdI1rVJlmbUAnwzPDQUq9ssM0fH8Ajiup2', start_index=5922)
Annotation(end_index=6423, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrskl1INrnpQ3VHU1-KbsB6ORxmZP4TqTXztAPJk-PJLX3YUHvC-7GZ41-HuJpOrp2egjLAwQrtltIgROUuRdEuyIfoRWKio-O9WyHcd6Br_5RXTI42pi6870X6GKda5Dh2pwC', start_index=6410)
Annotation(end_index=6423, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWvuxow0_weOrxSws7yZgIcPa-0xeq_1TbDcJelbt4sbpK7BnCm0aIXPPotT2Fl4bPU93-eiur4nz8KBB_CX_MmRlqFM4wF0ROaH-99KmqFOFSDgsyS53hkqi5cG3MU83v_cCt4M8pmr5iL7PwGpNrKKnx2o8efD6gYM0SX3mp2OeUTj410Yz8uA==', start_index=6410)
Annotation(end_index=6770, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrskl1INrnpQ3VHU1-KbsB6ORxmZP4TqTXztAPJk-PJLX3YUHvC-7GZ41-HuJpOrp2egjLAwQrtltIgROUuRdEuyIfoRWKio-O9WyHcd6Br_5RXTI42pi6870X6GKda5Dh2pwC', start_index=6757)
Annotation(end_index=6770, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHO9L9Hq2WKf54XfhD_7h2PED7PsFqduSyAp0bdvYRFTI7U3zKKOc6IXsh1vaXt6-KHPAfolN97qkQjajzkQY3pA_twL76LuMeFGyOubgueB62G_AdX5w-c2zc-p3cmGtn6bpWGXPtV-SSwbcqKjaMv2EDHXLJfolVidsgaIV6l6-kitA==', start_index=6757)
Annotation(end_index=6975, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrskl1INrnpQ3VHU1-KbsB6ORxmZP4TqTXztAPJk-PJLX3YUHvC-7GZ41-HuJpOrp2egjLAwQrtltIgROUuRdEuyIfoRWKio-O9WyHcd6Br_5RXTI42pi6870X6GKda5Dh2pwC', start_index=6962)
Annotation(end_index=6975, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWYpPKwLLqkCVDKJnOxe9HrX4rZ89TB55qEPp1_-VOvZnHEPuBd8r9bfS9CYn_81xryx1VOGIMMilLnsGOjVHp7SAWwciFmOV5ozpt1JA65oXpxuOAc8Uq7zgzuqeosAobRwCXIafylQ==', start_index=6962)
Annotation(end_index=7100, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzVeZQGe_xY4xXeezTm1qkShCKwtDhh4p03Pp_spcVHo_kWOY42O-d3d66hRs9r12-xsZi3AfvuUMgaSwaT7jIlrHc6kQvOdVUw5_KR3Q9D0h0q2teM87e1vFk0SWrNcNghWTyqzUIAjl3u3M-yyNzPch9tp-ZjRpNe5h8GGF9NaAiHYS-HC1Dd7Nss4fG6VCbtNMGglmEsqE_L-A=', start_index=7090)
Annotation(end_index=7511, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERpn1DFsNI1hVAN_I2HGqD-HXfwBm3Rg-bV3uronmBm-8-OR1TObJlI7pVC1Deyz2WdWXFHBRIt8IEERb7iQmDzuiAPjxW4d4PgUiM9LWoUBRcytMaWACCd8vvw_xTD2SelqUkT8Jg8HKYLhM1-fEomS8doPb05wBmD9lsass=', start_index=7501)
Annotation(end_index=7749, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERpn1DFsNI1hVAN_I2HGqD-HXfwBm3Rg-bV3uronmBm-8-OR1TObJlI7pVC1Deyz2WdWXFHBRIt8IEERb7iQmDzuiAPjxW4d4PgUiM9LWoUBRcytMaWACCd8vvw_xTD2SelqUkT8Jg8HKYLhM1-fEomS8doPb05wBmD9lsass=', start_index=7739)
Annotation(end_index=7993, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWrRWxIjZ1AWfkfHXq2N-bTIFWgmpQ3uuKTO5LiEBOrnuf6W9h0t3nBMhwc_A032-H5HZTGId1kpMvdyVftH4ZfHNO-hxEcii1plpSDZBGqVjRYkN_dm0kuwqhb0pbR5fpIRZFnxi-U9ErihF_qeCtyWbzjrMGsqq5uJNVDgauVOSiDxaaTPnayA2G0ldEMaa2orc=', start_index=7983)
Annotation(end_index=8460, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6D5WVvmLB4YlaUx64wg9H-dG-0npQKaoChz6sxzE-1ny1QHA0-DhNIIC1K7PIcvyd_EMHSyG0ac4msM05SjMhWbRVOpLUThWbs0Z5aKfKD2jXyO-Qjo-O0ldDH1SPIFdyJ5_LyjbdI1rVJlmbUAnwzPDQUq9ssM0fH8Ajiup2', start_index=8446)
Annotation(end_index=8460, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG83XC5RYk6jjAtknc9kAVIjJ0CFEl3WlZM89z1ILiXYUIfoU9a0LokNu6kS7DD9jH_dmFFwgJcPwWAb4Q60dQBpHkAI-uKUxxM5bPRYCC0IpGE0GeUNOZcEPRFM8C5KlpAOqK4Dum9jd8DL8sZx0hfyviYG6flL26XXz9yoXuxDGlf2PV4XKvpFBHjDKBAV7vs6YMI', start_index=8446)
Annotation(end_index=8966, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEeXViorK_9MYonuuioqkGwaSQBCggDMvhSVETgmPvQaIjeRvNMvUzWsHkRRk_XDX_KIidWcE9kpl2ws6O-LOHo4oiF4lN9tsz_YUbzmeZccEL3Uudsc4N9vsbb32lNrcaNfAgLWxtu_JAOKQbllTYtkFGPo4Sr8ZKYxzY81n_P', start_index=8952)
Annotation(end_index=8966, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfUEFlZ1GgxYfalpKAzDtBH8UrNdtHMy2jIze97Zi43c9m22rHjB743BAXkBJ4AkJiRoX5_ronkedg7reFryMmExiPR-p2cahzy1XC7qscVmnhcRtUJ8jc5GsRu2pgD4chK9Khi99jOrSjbhJQzOHwkh-MvdFYIPccCSrUTofA', start_index=8952)
Annotation(end_index=9361, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6D5WVvmLB4YlaUx64wg9H-dG-0npQKaoChz6sxzE-1ny1QHA0-DhNIIC1K7PIcvyd_EMHSyG0ac4msM05SjMhWbRVOpLUThWbs0Z5aKfKD2jXyO-Qjo-O0ldDH1SPIFdyJ5_LyjbdI1rVJlmbUAnwzPDQUq9ssM0fH8Ajiup2', start_index=9351)
Annotation(end_index=9673, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETACYpoX8pIhzLQiB3G3I0AQSg101Dg7OHPtVbqpuzXSIJeye-VbIRse9UDUW0rPtIn3xVpYtcILQdney28Gk26qcoo3kBZgVBr6bZ9qprKwJTJ7FNxZK3CNryTKcW66w_sgWRdSID8uDe3iMC3l1R63tGinEq8ia0_s5SMdcNAK2vT-lT', start_index=9659)
Annotation(end_index=9673, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG83XC5RYk6jjAtknc9kAVIjJ0CFEl3WlZM89z1ILiXYUIfoU9a0LokNu6kS7DD9jH_dmFFwgJcPwWAb4Q60dQBpHkAI-uKUxxM5bPRYCC0IpGE0GeUNOZcEPRFM8C5KlpAOqK4Dum9jd8DL8sZx0hfyviYG6flL26XXz9yoXuxDGlf2PV4XKvpFBHjDKBAV7vs6YMI', start_index=9659)
Annotation(end_index=9897, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3XfTnIOw2D98AqOq6VasXpr2J2J1xsFstu1njdbRUFZcGc34D8AKv2Qcg52nK8eRKLQb8PdtwouF_Izh0HcvshVB3FZuCpNyCiWucZYqnI95dvC0bGkWECS4CsUkzpOesd-2qCRIbhx3FH0Bn2WtTJGbjdzTBNJfv0L8k3TmVq7k153LvFzgx5z5HEU4HQuRIveciZOBXKI7g6d-rfyTBKEfy0Is1uOQriBc=', start_index=9887)
Annotation(end_index=11409, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzVeZQGe_xY4xXeezTm1qkShCKwtDhh4p03Pp_spcVHo_kWOY42O-d3d66hRs9r12-xsZi3AfvuUMgaSwaT7jIlrHc6kQvOdVUw5_KR3Q9D0h0q2teM87e1vFk0SWrNcNghWTyqzUIAjl3u3M-yyNzPch9tp-ZjRpNe5h8GGF9NaAiHYS-HC1Dd7Nss4fG6VCbtNMGglmEsqE_L-A=', start_index=11396)
Annotation(end_index=11409, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrskl1INrnpQ3VHU1-KbsB6ORxmZP4TqTXztAPJk-PJLX3YUHvC-7GZ41-HuJpOrp2egjLAwQrtltIgROUuRdEuyIfoRWKio-O9WyHcd6Br_5RXTI42pi6870X6GKda5Dh2pwC', start_index=11396)
Annotation(end_index=11884, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG743VorFDWnueHatiqUCAw9p7ZJst1AzgvrwU-pXrcGaoD3gR4IIQe5GSiOWNcdmysJ7hJRrbWY7hYHGj3sdXPZd-UNmklA7X3TpZDvCwE9n6mkvGbNmH7LebaFSzGALulfh_UI1-TpRiCPljKKHrafILIlVgyTgGT9YMFg8EVIA==', start_index=11870)
Annotation(end_index=11884, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWYpPKwLLqkCVDKJnOxe9HrX4rZ89TB55qEPp1_-VOvZnHEPuBd8r9bfS9CYn_81xryx1VOGIMMilLnsGOjVHp7SAWwciFmOV5ozpt1JA65oXpxuOAc8Uq7zgzuqeosAobRwCXIafylQ==', start_index=11870)
Annotation(end_index=12338, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6D5WVvmLB4YlaUx64wg9H-dG-0npQKaoChz6sxzE-1ny1QHA0-DhNIIC1K7PIcvyd_EMHSyG0ac4msM05SjMhWbRVOpLUThWbs0Z5aKfKD2jXyO-Qjo-O0ldDH1SPIFdyJ5_LyjbdI1rVJlmbUAnwzPDQUq9ssM0fH8Ajiup2', start_index=12324)
Annotation(end_index=12338, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3XfTnIOw2D98AqOq6VasXpr2J2J1xsFstu1njdbRUFZcGc34D8AKv2Qcg52nK8eRKLQb8PdtwouF_Izh0HcvshVB3FZuCpNyCiWucZYqnI95dvC0bGkWECS4CsUkzpOesd-2qCRIbhx3FH0Bn2WtTJGbjdzTBNJfv0L8k3TmVq7k153LvFzgx5z5HEU4HQuRIveciZOBXKI7g6d-rfyTBKEfy0Is1uOQriBc=', start_index=12324)
Annotation(end_index=13455, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGrskl1INrnpQ3VHU1-KbsB6ORxmZP4TqTXztAPJk-PJLX3YUHvC-7GZ41-HuJpOrp2egjLAwQrtltIgROUuRdEuyIfoRWKio-O9WyHcd6Br_5RXTI42pi6870X6GKda5Dh2pwC', start_index=13446)
Annotation(end_index=13539, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGycYeQ-pdIZLXQgcOq9-pZLWzjxfaFC3HNMDQHswenOCDRWD5PB0v_hW_1koQE2FDffePjJvQSFONcIFICvpGeeUxOlz9e67FMkBbg2LLCXKKC5klc74sDPgjmO8MKULgUNuFqz4bQgAU__X9sFM93_WOQ0OZ5vommila4VgY7eLafoM23', start_index=13530)
Annotation(end_index=13659, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7ua2xjzVKLYEghFbn946mJMYs8okqV9j27S3vTI7vNl7tAe1ADcfpFo_08rbLnZ2D0JoU19MvpfgU8tzlkWCbq5DcoPZsjVQjetFfNi85eb42-7Wk', start_index=13649)
Annotation(end_index=13729, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG743VorFDWnueHatiqUCAw9p7ZJst1AzgvrwU-pXrcGaoD3gR4IIQe5GSiOWNcdmysJ7hJRrbWY7hYHGj3sdXPZd-UNmklA7X3TpZDvCwE9n6mkvGbNmH7LebaFSzGALulfh_UI1-TpRiCPljKKHrafILIlVgyTgGT9YMFg8EVIA==', start_index=13719)
Annotation(end_index=13815, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjcIKddUXZkE11qpmH4fU0EAWS7pXGXBQ1gRBILL_DgM_FSWMUitHXETMoUZYxbIcBRJfstlY2PMt8xBltgBwBc5T9Dd6IAEbUiUW7KHbkcxgTpaagLeNgXwOdaVww_h-9QeqsEhwjO5MxZK6RDBx8LzPCIn_rVpVM9X4wCJfy-ZbpXwRjuYGdV1rKz0akl9XIn4ij0DZ_xecp3rf1a0vnABa8hBn0WJqX8fR6WTMgjG9Ktg==', start_index=13806)
Annotation(end_index=13925, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGhDGQmGFbBWze0djsFyYbYf0RfFsKlMOrEK-J8dWdRi_5wusBIXAZrll3AfT1OAdGfae5fpexp4j8f4Sgks8Y_7_NfSFOrmhcNRAkfp9cu_0tbGni9V_8lzRaBOjzoOTR0zHHbYZ988eY9P8p8vDbn-1ed53f4wZlhAEOYxVPX', start_index=13916)
Annotation(end_index=14015, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQES12RRuHv-5lV4jckpLtUdFxO9P0POnvoj4WkfmnedMPkH4PYywWEOqPr1krX_T92Dc5BJRFWFI1BH7REGnZjh5NiHRSbONjjGfuV3PODGgVsVVxMHsF3eSLeMJwDFonpwT9NXP-SCCgjJ_eH4wyPrFLUwZeL22epnvGLwatgk', start_index=14006)
Annotation(end_index=14144, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIODFIBUgsF-cZqqb0cjJUDsUvTntBKsAXgZg6PgqQqq30xapxh4Q1So6nMOxfg4ZSf06mQlHTVKrGCw_qFVuDUtR7wbZ-e4BH79K1NHfzNHZJllRslaSYK0LLuy4yD5V_w_HurdnL', start_index=14135)
Annotation(end_index=14297, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6D5WVvmLB4YlaUx64wg9H-dG-0npQKaoChz6sxzE-1ny1QHA0-DhNIIC1K7PIcvyd_EMHSyG0ac4msM05SjMhWbRVOpLUThWbs0Z5aKfKD2jXyO-Qjo-O0ldDH1SPIFdyJ5_LyjbdI1rVJlmbUAnwzPDQUq9ssM0fH8Ajiup2', start_index=14287)
Annotation(end_index=14414, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3XfTnIOw2D98AqOq6VasXpr2J2J1xsFstu1njdbRUFZcGc34D8AKv2Qcg52nK8eRKLQb8PdtwouF_Izh0HcvshVB3FZuCpNyCiWucZYqnI95dvC0bGkWECS4CsUkzpOesd-2qCRIbhx3FH0Bn2WtTJGbjdzTBNJfv0L8k3TmVq7k153LvFzgx5z5HEU4HQuRIveciZOBXKI7g6d-rfyTBKEfy0Is1uOQriBc=', start_index=14404)
Annotation(end_index=14515, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG83XC5RYk6jjAtknc9kAVIjJ0CFEl3WlZM89z1ILiXYUIfoU9a0LokNu6kS7DD9jH_dmFFwgJcPwWAb4Q60dQBpHkAI-uKUxxM5bPRYCC0IpGE0GeUNOZcEPRFM8C5KlpAOqK4Dum9jd8DL8sZx0hfyviYG6flL26XXz9yoXuxDGlf2PV4XKvpFBHjDKBAV7vs6YMI', start_index=14505)
Annotation(end_index=14612, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMkDe8adfom6u0NBVOA9Sp04deSB-vYdrQpwi7b9StdRwd_JrdrgXVvYcngBwgOD9E6gevSP1pawo0M75e20tFoz6oI8sfy7HvxJReOftOdk1AqtDxWR2ihZPhW30INW_z', start_index=14603)
Annotation(end_index=14716, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGycYeQ-pdIZLXQgcOq9-pZLWzjxfaFC3HNMDQHswenOCDRWD5PB0v_hW_1koQE2FDffePjJvQSFONcIFICvpGeeUxOlz9e67FMkBbg2LLCXKKC5klc74sDPgjmO8MKULgUNuFqz4bQgAU__X9sFM93_WOQ0OZ5vommila4VgY7eLafoM23', start_index=14707)
Annotation(end_index=14836, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWvuxow0_weOrxSws7yZgIcPa-0xeq_1TbDcJelbt4sbpK7BnCm0aIXPPotT2Fl4bPU93-eiur4nz8KBB_CX_MmRlqFM4wF0ROaH-99KmqFOFSDgsyS53hkqi5cG3MU83v_cCt4M8pmr5iL7PwGpNrKKnx2o8efD6gYM0SX3mp2OeUTj410Yz8uA==', start_index=14826)
Annotation(end_index=14886, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzVeZQGe_xY4xXeezTm1qkShCKwtDhh4p03Pp_spcVHo_kWOY42O-d3d66hRs9r12-xsZi3AfvuUMgaSwaT7jIlrHc6kQvOdVUw5_KR3Q9D0h0q2teM87e1vFk0SWrNcNghWTyqzUIAjl3u3M-yyNzPch9tp-ZjRpNe5h8GGF9NaAiHYS-HC1Dd7Nss4fG6VCbtNMGglmEsqE_L-A=', start_index=14876)
Annotation(end_index=14949, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHO9L9Hq2WKf54XfhD_7h2PED7PsFqduSyAp0bdvYRFTI7U3zKKOc6IXsh1vaXt6-KHPAfolN97qkQjajzkQY3pA_twL76LuMeFGyOubgueB62G_AdX5w-c2zc-p3cmGtn6bpWGXPtV-SSwbcqKjaMv2EDHXLJfolVidsgaIV6l6-kitA==', start_index=14939)
Annotation(end_index=14996, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERpn1DFsNI1hVAN_I2HGqD-HXfwBm3Rg-bV3uronmBm-8-OR1TObJlI7pVC1Deyz2WdWXFHBRIt8IEERb7iQmDzuiAPjxW4d4PgUiM9LWoUBRcytMaWACCd8vvw_xTD2SelqUkT8Jg8HKYLhM1-fEomS8doPb05wBmD9lsass=', start_index=14986)
Annotation(end_index=15070, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG83XC5RYk6jjAtknc9kAVIjJ0CFEl3WlZM89z1ILiXYUIfoU9a0LokNu6kS7DD9jH_dmFFwgJcPwWAb4Q60dQBpHkAI-uKUxxM5bPRYCC0IpGE0GeUNOZcEPRFM8C5KlpAOqK4Dum9jd8DL8sZx0hfyviYG6flL26XXz9yoXuxDGlf2PV4XKvpFBHjDKBAV7vs6YMI', start_index=15060)
Annotation(end_index=15168, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEeXViorK_9MYonuuioqkGwaSQBCggDMvhSVETgmPvQaIjeRvNMvUzWsHkRRk_XDX_KIidWcE9kpl2ws6O-LOHo4oiF4lN9tsz_YUbzmeZccEL3Uudsc4N9vsbb32lNrcaNfAgLWxtu_JAOKQbllTYtkFGPo4Sr8ZKYxzY81n_P', start_index=15158)
Annotation(end_index=15235, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWYpPKwLLqkCVDKJnOxe9HrX4rZ89TB55qEPp1_-VOvZnHEPuBd8r9bfS9CYn_81xryx1VOGIMMilLnsGOjVHp7SAWwciFmOV5ozpt1JA65oXpxuOAc8Uq7zgzuqeosAobRwCXIafylQ==', start_index=15225)
Annotation(end_index=15284, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6D5WVvmLB4YlaUx64wg9H-dG-0npQKaoChz6sxzE-1ny1QHA0-DhNIIC1K7PIcvyd_EMHSyG0ac4msM05SjMhWbRVOpLUThWbs0Z5aKfKD2jXyO-Qjo-O0ldDH1SPIFdyJ5_LyjbdI1rVJlmbUAnwzPDQUq9ssM0fH8Ajiup2', start_index=15274)
Annotation(end_index=15385, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3XfTnIOw2D98AqOq6VasXpr2J2J1xsFstu1njdbRUFZcGc34D8AKv2Qcg52nK8eRKLQb8PdtwouF_Izh0HcvshVB3FZuCpNyCiWucZYqnI95dvC0bGkWECS4CsUkzpOesd-2qCRIbhx3FH0Bn2WtTJGbjdzTBNJfv0L8k3TmVq7k153LvFzgx5z5HEU4HQuRIveciZOBXKI7g6d-rfyTBKEfy0Is1uOQriBc=', start_index=15375)
Annotation(end_index=15486, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfUEFlZ1GgxYfalpKAzDtBH8UrNdtHMy2jIze97Zi43c9m22rHjB743BAXkBJ4AkJiRoX5_ronkedg7reFryMmExiPR-p2cahzy1XC7qscVmnhcRtUJ8jc5GsRu2pgD4chK9Khi99jOrSjbhJQzOHwkh-MvdFYIPccCSrUTofA', start_index=15476)
Annotation(end_index=15552, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEK0-NfHM4wIuKAx1dhMciGbFzv1t9fJGg78qFGEmfYfmmc3dWsTmDr1eLNVVwlAgP0MN0M7cymNAxiFi3g0JH1k_KPiYWZPvovPptAlAdn6fMJgZVIEnDzxT2BtpyUrvoVTe4YCVG7rwtmMGY9aUni', start_index=15543)
Annotation(end_index=15601, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGovqMIHZySgD14pOa-cLdH1qMhHYje_TXazkHlR3LwnsBbRz9Que25UEFsAEk2BJV-aNTWiyLXGTBMTP_aZc5Wgf2MyUiOTyKm-hXB5SjWDYUm3Fvpkjf78_HWqpz600Tre0WjuA5DHwWDFqUv5gjXE_r1UQ==', start_index=15592)
Annotation(end_index=15671, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMkDe8adfom6u0NBVOA9Sp04deSB-vYdrQpwi7b9StdRwd_JrdrgXVvYcngBwgOD9E6gevSP1pawo0M75e20tFoz6oI8sfy7HvxJReOftOdk1AqtDxWR2ihZPhW30INW_z', start_index=15662)
Annotation(end_index=15776, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHWrRWxIjZ1AWfkfHXq2N-bTIFWgmpQ3uuKTO5LiEBOrnuf6W9h0t3nBMhwc_A032-H5HZTGId1kpMvdyVftH4ZfHNO-hxEcii1plpSDZBGqVjRYkN_dm0kuwqhb0pbR5fpIRZFnxi-U9ErihF_qeCtyWbzjrMGsqq5uJNVDgauVOSiDxaaTPnayA2G0ldEMaa2orc=', start_index=15766)
Annotation(end_index=15854, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGM8FBnPmNG39r3hON4DD1WBdpRulRQ09miDEnzrMEZ-VB9RBdh7yLK18mYGxKdWdv03SGt7UVR6PasUE-ynbhfYdmpXEMRI_zfrEAULQHKWN_QKQXbeC_RatFQXPESr_-vdwqh_2JiXwx-2gG58HUGsPiTXIkzceeR5O2mWCtSRxmszW4l4KM6pKilyoz_m3byKo_Rp4fmROYGAeM2JD87v_Ux-BxliJYvWzD6GBXLHODDJxdIRv3QLx8x-_D6WOsOuSIhZDPhre-i7B0VgCgiAVgCtF7BovzwewYz', start_index=15844)
Annotation(end_index=15945, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQETACYpoX8pIhzLQiB3G3I0AQSg101Dg7OHPtVbqpuzXSIJeye-VbIRse9UDUW0rPtIn3xVpYtcILQdney28Gk26qcoo3kBZgVBr6bZ9qprKwJTJ7FNxZK3CNryTKcW66w_sgWRdSID8uDe3iMC3l1R63tGinEq8ia0_s5SMdcNAK2vT-lT', start_index=15935)

## Sources
