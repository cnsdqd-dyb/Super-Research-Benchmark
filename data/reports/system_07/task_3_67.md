# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** a1b401b9 | **Time:** 25.04s | **Cost:** $0.02777
--------------------------------------------------------------------------------

For flash-sale SKUs the boundary is not a single number; it is a traffic-light rule that is re-computed every planning cycle (usually daily) and tells the planner when the pre-built safety stock has to be **raised**, **lowered** or **frozen** although the sale has not yet happened.  
The rule is derived from a **conversion-rate simulation**, not from the classical σ-demand formula, because during a flash sale the demand process is dominated by the **conversion of traffic**, not by historical daily sales.

-------------------------------------------------
1.  Build the stochastic demand model  
   a. Take the traffic forecast that Marketing gives you for each hour of the event (usually a range: low/mid/high).  
   b. Multiply by the **distribution of conversion rate** that you observed in past flash sales for this SKU (or for the category if the SKU is new).  
      – The distribution is strongly skewed; fit a Beta or a log-normal, not a normal.  
   c. The result is an **hourly demand distribution**; aggregate it over the lead-time that is left until the next physical receipt.  
      – Lead-time is the “virtual” lead-time: the time you would need to air-freight or to re-allocate from another DC if the stock were to run out.  
   d. You now have **D ~ f(μ,σ)** for the flash period.

-------------------------------------------------
2.  Choose the service-level target  
   Flash sales are usually run at **SL = 95 %** (Z = 1.65) for A-list SKUs, **90 %** (Z = 1.28) for B-list, **85 %** (Z = 1.04) for C-list.  
   The target is set by merchandising, not by operations, and is **fixed for the event**; it is not changed every time the forecast moves.

-------------------------------------------------
3.  Compute the **dynamic safety stock**  
   SS_event = Z × σ_LT  
   where σ_LT is the standard deviation of the demand during the virtual lead-time obtained in step 1.  
   Because σ_LT changes every day (traffic forecast is refined, remaining lead-time shrinks, size of the offer changes), SS_event is recalculated nightly.

-------------------------------------------------
4.  Set the **adjustment boundary** (the traffic-light rule)  
   Let IP = inventory position (on-hand + in-transit – back-orders) and  
   let SS_event(t) be the value calculated in step 3 for tonight’s planning cycle.

   Green – no action  
   IP ≥ SS_event(t) + 0.5 × σ_LT  
   (stock is ≥ ½ standard deviation above the theoretical buffer)

   Yellow – prepare a counter-measure  
   SS_event(t) – 0.5 × σ_LT ≤ IP < SS_event(t) + 0.5 × σ_LT  
   Planner must validate within 4 h whether:  
   – traffic forecast is still realistic,  
   – an emergency replenishment (expedited PO, inter-DC transfer, drop-ship) can be triggered,  
   – the SKU should be removed from the front-page carousel to throttle demand.

   Red – execute the counter-measure immediately  
   IP < SS_event(t) – 0.5 × σ_LT  
   Automatic freeze of marketing spend, removal from flash page, and creation of an emergency PO with 24-h SLA.

   The 0.5 σ_LT band is empirical; it is wide enough to ignore rounding error and small intraday forecast noise, but tight enough to give the planner 24-48 h of reaction time before the stock-out actually happens.

-------------------------------------------------
5.  Automate in the ERP / OMS  
   The nightly batch job reloads the traffic forecast, re-estimates the conversion distribution, recalculates SS_event(t) and updates the boundary.  
   A micro-service exposes the colour flag to the e-commerce front end so that the flash-sale engine can throttle traffic in real time.

-------------------------------------------------
Key point  
The boundary is **not** “SS = 200 units”; it is  
“SS_event(t) ± ½ σ_LT” where both SS_event and σ_LT are **re-estimated every day with the latest conversion-rate distribution**.  
This keeps the flash-sale safety stock lean (you do not over-build) while still giving an operational early-warning window when the conversion rate starts to drift.

## Annotations


## Sources
