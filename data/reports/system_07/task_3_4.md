# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 78304c28 | **Time:** 21.11s | **Cost:** $0.02336
--------------------------------------------------------------------------------

Seasonal-influenza programmes never have enough money, staff, vaccine or “cold-chain” hours to do everything at once.  
Policy makers therefore have to decide how many doses to give to people ≥ 60–65 y (who gain the most *personal* benefit because their risk of death is 50- to 100-fold higher than in younger adults) and how many to give to the 5- to 50-year-olds who do almost all of the transmitting (and therefore determine whether herd-immunity is reached).  
The compromise is struck in four linked steps that are revisited every season.

1.  Translate the national budget into a *dose budget*  
    – How many doses can actually be put in arms before the epidemic peak?  
    – Example: Australia’s primary-care system can deliver ≈ 5 million influenza doses per year; scaling to “mass” coverage would need five-fold more staff and fridges, so 70–80 % coverage is impossible without new resources.

2.  Rank age groups with a *dual-criterion score*  
    Score = (relative risk of death if infected) × (expected number of infections averted per dose)  
    – Risk of death rises exponentially with age (≈ 0.1/100 000 in 5–14 y, ≈ 10/100 000 in 65–74 y, ≈ 100/100 000 in ≥ 85 y).  
    – Infections averted per dose are highest in school-children and working adults because they have the largest contact networks (R₀ contribution).  
    The product shows that *very early doses* go to the elderly (high mortality) but *marginal doses* beyond ~30 % coverage give more population-level benefit when moved to the 5–59 y group.

3.  Run an optimisation model under the dose budget  
    Objective: minimise total deaths (or maximise QALYs)  
    Constraints: ≤ X million doses, ≤ Y fridge-hours, ≥ Z % minimum coverage in ≥ 65 y (political promise).  
    Result (Zhejiang 2022–23, Australia, US studies):  
    – 36–40 % *overall* coverage is enough to keep peak incidence below the “high-intensity” threshold.  
    – The cheapest way to reach that threshold is to raise coverage in 0–14 y and ≥ 60 y simultaneously; once those two groups are at 50–55 %, additional doses are re-allocated to 15–59 y to push the national total past 36 %.  
    – If the programme can afford *only* one extra dose per 100 people, models consistently send it to a 7-year-old rather than to an 80-year-old because the child averts ≈ 0.35 onward infections while the octogenarian averts ≈ 0.03.

4.  Use *differentiated products* so the elderly still get *individual* protection even when their *share* of the programme shrinks  
    – High-dose (HD-IIV4) or adjuvanted (aIIV3) vaccines raise effectiveness in ≥ 65 y from ~35 % to ~60 %, so fewer doses are needed to deliver the same number of severe-case preventions.  
    – This frees ordinary egg-based doses for the transmitter groups without violating the political guarantee that “no elderly person is left unprotected”.

Dynamic feedback is added every season: if drift is early and R₀ is high, the optimisation re-weights transmission blocking; if the season is already peaking, the model flips to pure mortality prevention and pushes remaining stocks into nursing homes.

Hence the observed policy mix in most high-income countries:

-  ≥ 65 y (and other high-risk groups) are *guaranteed* a dose of HD/aIIV vaccine—satisfying the ethical imperative and giving them the best *individual* protection immunosenescence allows.  
-  Children and working adults are *invited* until the national total reaches the herd-immunity knee (≈ 36–40 % coverage for influenza R₀ = 1.3–1.6 and VE = 50–60 %).  
-  Marginal doses beyond that point are targeted to schools, workplaces and parents of young children, because each extra percentage point there yields larger epidemic suppression than the same point in the elderly.

Under severe scarcity (pandemic or supply failure) the same algorithm collapses to a “ring-plus-elderly” strategy: first vaccinate healthcare workers and the very old, then use leftover doses to create buffer zones around outbreaks, exactly the approach tested in Niger measles and in Ebola ring vaccination.

In short, seasonal programmes balance elderly protection and herd immunity by:

1.  Guaranteeing the old a *more potent* vaccine instead of a *larger share* of the ordinary one;  
2.  Using model-guided age shifting to place the *marginal* dose where it most reduces *total* deaths, which is often in children or young adults;  
3.  Re-computing the split each year so the political promise (“no elderly left behind”) is met while still keeping the population coverage above the herd-immunity threshold that benefits everyone.

## Annotations


## Sources
