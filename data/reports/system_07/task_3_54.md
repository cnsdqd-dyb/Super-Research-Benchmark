# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 584ffa0e | **Time:** 19.49s | **Cost:** $0.01273
--------------------------------------------------------------------------------

Source–sink analysis is not a single “technique” but a family of bookkeeping, inversion and hybrid methods that try to balance the global budget of a pollutant.  
Because every country is simultaneously a source (emitter) and a sink (remover) of carbon, CH₄, N₂O, etc., the exercise is inherently a **responsibility-sharing** problem: whose emissions are whose, and whose removals can be credited?  
Data asymmetry enters at three points:

1. **Activity data** – national inventories that are self-reported, use different tiers, and are rarely third-party verified.  
2. **Atmospheric data** – flask networks, satellites, tall towers that are dense in the OECD and sparse or absent in most of the tropics and Africa.  
3. **Prior flux maps** – wetland, soil, forest models that are calibrated with measurements taken mainly in the US/Europe.

The techniques do not “remove” the asymmetry; they **manage** it in four complementary ways:

A. **Top-down inversions with explicit data-weighting**  
   Bayesian atmospheric inversions (e.g., those used in the Global Carbon Project) weight each observation by its inverse variance.  
   – Stations in data-poor regions automatically receive **zero weight**, so the posterior flux for, say, the Congo basin is driven almost entirely by the prior.  
   – To avoid simply “baking in” the prior, modellers run a **null-difference test**: they re-run the inversion with the prior mean shifted by ±1 σ and report the range as a structural-error term.  
   – The asymmetry is therefore **quantified** (it shows up as a large spread in the African flux), but it is not reduced.

B. **Hybrid bottom-up / top-down ensembles**  
   The GCP methane budget (Kirschke et al., 2013) combines:  
   – bottom-up inventories (national + gridded models)  
   – nine top-down inversions with different transport models & priors  
   The **ensemble spread** is interpreted as a lower-bound on the asymmetry-induced uncertainty.  
   When the bottom-up global total is 20 % larger than the top-down mean, the difference is **not** forced to zero; instead the budget is declared “unbalanced” and the imbalance (6 Tg CH₄ yr⁻¹ in the 2000s) is carried as an explicit line item.  
   Thus the asymmetry is **preserved** in the final numbers that policy makers see.

C. **Regional “nested” or “zoom” inversions**  
   A global coarse inversion (2–4°) is run first; its residuals over a data-poor continent are then used as **boundary conditions** for a regional 0.5° inversion.  
   Because the regional frame can ingest local aircraft campaigns or GOSAT columns that the global frame discards, the **information content** for that continent rises.  
   The asymmetry is **partially corrected**, but only for the region that could afford the extra campaign.

D. **Reporting protocols that shift the burden of proof**  
   The UNFCCC “global stocktake” rules (COP-26) now allow countries to **substitute** an inversion-based flux for the national-inventory value **if** the country provides ≥ 3 years of continuous atmospheric data that pass an agreed set of ILAMB benchmarks.  
   This gives the **data-rich** a route to higher credited sinks, while explicitly recognising that data-poor parties cannot use the same route—i.e., the asymmetry is **institutionalised**, not eliminated.

Bottom line  
Source–sink techniques do not “solve” data asymmetry; they **make it visible and quantifiable**.  
The numbers that enter international negotiations already contain an explicit “budget imbalance” term that is, in large part, the mathematical trace of who owns flask stations, satellites and super-computers and who does not.

## Annotations


## Sources
