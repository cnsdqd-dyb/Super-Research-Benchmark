# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 58eb1ce2 | **Time:** 20.76s | **Cost:** $0.01214
--------------------------------------------------------------------------------

Yes—partition coefficients (K values) are one of the first numbers a process engineer looks at when deciding whether a solvent-extraction route for urban-mining metals is worth scaling up.  
They enter the economic calculation in four direct ways and one indirect way:

1. **Stage count and capex**  
   The required enrichment factor (organic / aqueous) is set by the assay of the leachate and the purity target.  
   Nmin ≈ ln(EF) / ln(K) (McCabe-Thiele).  
   A K that is only 2–3 instead of 10–20 can turn a 3-stage mixer-settler train into 8–10 stages, doubling the steel, concrete, piping and footprint. Every extra stage adds ≈ 0.8–1.2 M USD in a 1 000 t e-waste/yr facility.

2.**Reagent inventory and opex**  
   The organic/aqueous phase ratio (O/A) needed to reach the extraction % E = (K·O/A)/(1 + K·O/A).  
   Low K forces you to push O/A down (more organic is pumped). A K = 2 circuit runs at O/A ≈ 1:1, whereas K = 20 can use O/A = 1:5.  
   At 2 USD kg⁻¹ for the extractant (e.g. D2EHPA) the annual solvent make-up cost for a 1 000 t/yr PCB leachate plant rises from ~30 k USD (K = 20) to ~200 k USD (K = 2) because the organic inventory is five times larger and drag losses scale with volume.

3.**Strip liquor tenor and downstream cost**  
   Strip is the reverse extraction; Kstrip = 1/K.  
   A low K in extraction means a high K in stripping, so you need more strip stages or a high-strip-acid concentration (160–200 g L⁻¹ HCl instead of 30–60 g L⁻¹). Acid consumption, neutralisation sludge and resin / electrowinning capex all increase. For Cu, every extra 10 g L⁻¹ acid used adds ≈ 0.04 USD kg⁻¹ Cu to opex.

4.**Yield and revenue**  
   A low K combined with a low O/A leaves value in the raffinate. Losing only 2 % of the 200 g t⁻¹ Au in PCB leachate means 4 g t⁻¹ × 55 USD g⁻¹ = 220 USD lost per tonne of boards treated—enough to erase the gross margin in many projects.

5.**Indirect effect on environmental compliance cost**  
   Poor K values usually force higher organic flow, hence larger solvent losses and higher COD in the aqueous effluent. Meeting the 1 mg L⁻¹ TOC discharge limit can add 0.3–0.5 USD m⁻³ wastewater treatment cost, which is material when 4–6 m³ of water is processed per tonne of boards.

Rule-of-thumb used by hydrometallurgical designers:  
- K ≥ 100 (e.g. Au with dibutyl carbitol, Pd with DHS) → “easy money”, three stages, O/A 1:5, pay-back < 2 yr.  
- K 10–50 (Cu with LIX 984, Co with Cyanex 272) → “doable”, four to five stages, detailed NPV needed.  
- K < 5 (Li, Ni in chloride media, most rare earths with ordinary extractants) → “marginal unless value > 25 USD kg metal”; usually requires custom synergistic extractant or a different flow-sheet (SX–IX hybrid, precipitation, etc.).

Therefore the partition coefficient is not just a thermodynamic curiosity; it is the single parameter that dictates how many mixers, settlers, pumps, m² of land and m³ of solvent you must buy, and whether the metal dollar content of a mobile-phone PCB is enough to cover those bills.

## Annotations


## Sources
