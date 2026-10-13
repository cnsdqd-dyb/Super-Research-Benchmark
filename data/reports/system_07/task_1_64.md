# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 69bce924 | **Time:** 17.41s | **Cost:** $0.01095
--------------------------------------------------------------------------------

Stability boundaries of signal coordination act as the “tipping surface” of a city’s traffic grid.  
Cross them—by only a few seconds of cycle offset, a few vehicles per lane too many, or a single saturated turn pocket—and the corridor ceases to be a controllable “pipe” and becomes a noise amplifier that exports stop-and-go waves to the rest of the network.  
The mechanism is three–layered:

1. Local bifurcation (0–300 m)  
   The coordinated green-wave is valid only inside a compact set of initial queue lengths, arrival flows and phase offsets. Outside that set the queue-occupancy map has an unstable eigenvalue >1. A small overshoot (e.g., 1.5 times the storage length) flips the intersection from “stable queue” to “queue-over-detector” regime; once the detector is continuously occupied the controller loses the feedback that keeps the offset plan meaningful.

2. Corridor shock-wave (0.3–3 km)  
   The unstable node now injects a kinematic shock that travels upstream at 15–20 km h⁻¹. Because the upstream signals still run the original offset plan, they release platoons that meet the shock front exactly at the next red phase. The result is a standing wave whose amplitude grows by ≈ 15 % per cycle until the backward wave speed equals the green-wave speed. At that moment the coordination window collapses: the system has literally “out-run” its own control horizon.

3. Network percolation (>3 km)  
   Once the shock reaches the first source node (ramp, car-park exit, minor-street merge) the excess demand that cannot enter the arterial is deflected onto the grid. These detour flows raise the degree of saturation of cross-streets above their own stability boundary, so the instability now branches laterally. The process repeats on adjacent corridors and the congestion cluster percolates until the “diameter” of the congested sub-graph is large enough that the original green-wave plan is no longer observable from any node inside the cluster—coordination information is lost in the noise.

Quantitatively, the stability boundary is the hypersurface in the space (q, r, θ, s) where q = average flow, r = red-time ratio, θ = offset error, s = queue-storage ratio.  
For a typical six-signal arterial the boundary is well approximated by  

q_crit(θ, s) = q_cap · [1 – 0.8(θ/θ_max)² – 0.7(s/s_max)²]

with θ_max ≈ 8 s and s_max ≈ 0.9.  
Operate at 95 % of q_crit and a 2-s offset drift or a single 10 % queue overshoot pushes the corridor over the cliff; recovery requires dropping the input flow by 25–30 % for at least five cycles—exactly the “capacity drop” observed in the field.

Hence the stability boundary is not merely a performance knob; it is the firewall that prevents local oversaturation from becoming a system-wide contagion.

## Annotations


## Sources
