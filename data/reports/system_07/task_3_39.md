# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 02a008ee | **Time:** 24.13s | **Cost:** $0.01362
--------------------------------------------------------------------------------

The spatiotemporal distribution of an OD (origin–destination) matrix governs **where** and **when** demand is generated and absorbed.  
Because every capacity-allocation rule is ultimately a rule for matching supply to that demand, the OD structure is the **primary exogenous driver** of how much capacity must be placed on each link, in each time slice, and with what redundancy.  
Density gradients (steep vs. flat; monocentric vs. polycentric; radial vs. grid, etc.) act as **amplifiers or dampers** of that basic relationship.  
The interaction can be summarised in four layers:

--------------------------------------------------------------------
1.  **Link load profile layer**  
    - **OD volume × path choice = link load**.  
    - A **steep gradient** (most trips converge on a small centre) produces **peaked, unidirectional** link loads; a **flat gradient** produces **diffuse, bidirectional** loads.  
    - Capacity allocation therefore switches from “guard the cut” (single overloaded arc) to “guard the mesh” (many moderately loaded arcs).

--------------------------------------------------------------------
2.  **Time-of-day layer**  
    - The **temporal concentration** of the OD matrix (coefficient of variation of hourly volumes) determines how much **temporal inventory** (schedule slack, holding slots, energy-recovery windows) is needed.  
    - Under **steep spatial gradients** the temporal peak is usually **synchronised** (morning in-bound, evening out-bound), so the **same physical asset** must absorb both the **spatial** and **temporal** spike; the required **peak-capacity multiplier** is multiplicative, not additive.  
    - Under **flat gradients** the peaks of different OD pairs **decorrelate**; the network can **reuse** the same capacity in successive sub-periods, so the **peak multiplier is sub-linear** in the total OD volume.

--------------------------------------------------------------------
3.  **Redundancy & re-routing layer**  
    - **Steep gradients** yield **few, short alternative paths**; the OD matrix is **sparse** in route space.  
      → Capacity allocation must include **hard redundancy** (extra tracks, spare feeder lines) because the **cost of losing any one link is high**.  
    - **Flat gradients** yield **dense route space**; the OD matrix is **diffuse**.  
      → Capacity can be allocated with **soft redundancy** (real-time re-routing, dynamic pricing) because the **marginal loss of any one link is small**.

--------------------------------------------------------------------
4.  **Economies-of-density layer**  
    - **Steep gradients** let operators exploit **economies of density**: long trains, large vehicles, high frequency on a corridor.  
      → Optimal allocation is **lumpy**: big blocks of capacity on the radial cut.  
    - **Flat gradients** push the system toward **economies of scope**: many thin flows, many modes, many headways.  
      → Optimal allocation is **granular**: small, flexible units spread over the mesh.

--------------------------------------------------------------------
Practical translation for planners

| Density gradient | Typical OD signature | Capacity-allocation rule-of-thumb |
|------------------|----------------------|------------------------------------|
| Monocentric, steep | 60–70 % of trips terminate in 5 % of zones within 3 h | Over-size the radial cut by ≥ 1.5 × the highest 15-min OD slice; provide directional turn-back tracks; schedule energy-recovery trains to coincide with braking peaks. |
| Polycentric, moderate | Several 10–15 % sub-peaks, 2–4 h spread | Build **intermediate-capacity ring** or **tangential** links; size each corridor for **70 % of its own sub-peak**, rely on cross-transfer for the remainder. |
| Flat, sprawl-like | No zone > 5 % of destinations, peaks smeared over 6–8 h | Allocate **base capacity** everywhere (e.g., 10-min headway grid), **augment on demand** with flexible fleets; use **price-based re-timing** instead of extra infrastructure. |

--------------------------------------------------------------------
Bottom line  
The **spatiotemporal OD matrix is the demand surface**; the **density gradient is its curvature**.  
Capacity allocation is nothing more than **fitting a protective hull** over that surface.  
Where the curvature is high (steep gradient) the hull must be **thick and rigid**; where the curvature is low (flat gradient) it can be **thin and adaptive**.

## Annotations


## Sources
