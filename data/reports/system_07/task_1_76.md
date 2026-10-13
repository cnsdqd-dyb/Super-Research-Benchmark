# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 688e1122 | **Time:** 25.95s | **Cost:** $0.03026
--------------------------------------------------------------------------------

Stability boundaries in ideal and resistive MHD determine how high the plasma-β (≡ 2μ₀〈p〉/B²) can be pushed before an abrupt, large-scale instability appears.  In a reactor these boundaries are not merely physics curiosities: every 10% step in 〈β〉 translates into roughly a 20% step in fusion power density (P_f/V ∝ β²B⁴) and therefore into comparable changes in the cost-of-electricity.  The design space is consequently carved out by four hard β limits that follow directly from the stability boundaries:

1. Troyon (no-wall) limit – external kink/ballooning  
   β_N ≡ β(%) a B₀/I_p ≤ 2.8–3.0  
   No passive conductor can help; exceed it and the plasma is lost on the Alfvén time-scale (µs).  All reactor studies therefore treat β_N = 3 as an absolute ceiling for inductive baseline scenarios.  Raising B₀ or shrinking a while keeping β_N ≤ 3 is the only way to gain β itself, and that choice propagates immediately into TF-coil stress, neutron wall loading and aspect-ratio constraints.

2. Ideal-wall limit – external kink with perfectly conducting shell  
   β_N^wall ≃ 3.5–4.5 (geometry dependent)  
   A close-fitting super-conducting shell moves the boundary upward, but the shell must be inside the blanket/shield, only a few cm from the plasma.  Reactor blankets are already ~0.5 m thick and contain electrically segmented steel; an ideal wall is therefore technologically inaccessible.  Designs that quote β_N > 3 must either (i) assume a resistive wall plus active feedback or (ii) invoke stellarator or RFP configurations whose boundary is set by a different mode spectrum.

3. Resistive-wall mode (RWM) boundary – same β_N^wall but growth rate γ ∝ τ_wall⁻¹  
   γ ≃ 10² s⁻¹ in ITER, 10¹ s⁻¹ in a DEMO.  Active feedback with ~10–20 kA in ~100 coils and latency <0.1 ms is required.  The coil-set, power supplies and diagnostics have to be radiation-hardened and maintain reliability for ~10⁹ cycles.  Every coil ampere adds to the nuclear heat-load and tritium inventory, so the “cost” of pushing β_N from 3 to 4 is not only control engineering but also an increase in tritium breeding ratio requirement and shield thickness.  Most reactor studies therefore still adopt β_N ≤ 3 for the reference case and treat 3.5 as an upgrade option contingent on RWM control maturity.

4. Neoclassical-tearing-mode (NTM) “soft” boundary – β_N ≲ 2.2–2.6 unless ECCD is provided  
   NTMs grow on the resistive time-scale (10–100 ms) once the seed island exceeds ~5 cm.  Because the bootstrap fraction f_bs ∝ β_N, high-β steady-state scenarios (f_bs ≥ 0.5) necessarily operate just below the NTM onset.  Stabilization requires 1–2% of the plasma current to be driven at the q = 3/2 or 2/1 surface by electron-cyclotron waves.  The launcher must steer ≤1 cm at 10–20 MW through a blanket gap, survive 4 MW m⁻² neutron loading, and remain aligned for decades.  If the launcher cannot be placed close enough, the design reverts to lower β_N or to a pulsed inductive scenario with f_bs ≲ 0.3.

Global design consequences

- Size vs. field trade-off: because P_f ∝ β²B⁴, a 10% rise in β allows ~7% reduction in major radius R₀ for the same electric output; but the higher β must still satisfy the Troyon limit, so B₀ must rise ∝ β_N⁻¹.  Super-conducting REBCO tapes that tolerate 15–20 T are therefore a key enabler for high-field, small-R₀ reactors that stay below β_N = 3.

- Blanket/shield thickness: the ideal-wall boundary moves inward roughly linearly with wall radius; every 10 cm of additional blanket pushes β_N^wall downward by ~0.3.  Designers are forced to choose between a thin, high-β but tritium-poor blanket or a thick, tritium-self-sufficient but lower-β blanket.

- Pulse length vs. bootstrap fraction: steady-state reactors need f_bs ≥ 0.5, hence β_N ≥ 2.5, but that region is NT-unstable.  The required ECCD power (10–20 MW) and launcher neutron-shielding mass are non-negligible parts of the plant; if either is judged too risky, the design reverts to a 0.3 GW pulsed option at β_N ≈ 2.

- Vertical stability/elongation: higher κ raises the Troyon coefficient only modestly (β_N ∝ (1+κ²)/2) but lowers the vertical-stability margin; passive stabilizing plates plus active coils are mandatory for κ ≥ 1.8, again adding nuclear-heated conducting structures inside the shield.

In short, the MHD β boundaries do not merely cap the plasma pressure; they propagate through neutronics, tritium breeding, coil technology, maintenance scheme and finally into the cost-of-electricity.  Reactor optimization is therefore a constrained minimization problem: maximize β²B⁴ subject to  
β_N ≤ 3 (hard), β_N ≤ 4 only if RWM/NTM control is demonstrated, and all other plant limits (wall loading, TF-coil stress, tritium breeding ratio, divertor heat-flux) are simultaneously satisfied.

## Annotations


## Sources
