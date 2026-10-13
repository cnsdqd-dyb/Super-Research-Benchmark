# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** e6e9d461 | **Time:** 22.46s | **Cost:** $0.01294
--------------------------------------------------------------------------------

Activation-energy barriers govern every thermal, mechanical or catalytic step that a polymer chain experiences during collection, washing, melt-reprocessing, extrusion, compounding, reactive extrusion or solvent-based dissolution.  
Because the height of those barriers is different for chain-scission, cross-linking, oxidation, de-polymerisation and side-group reactions, the “easiest” reaction wins. In real recyclate that means:

1. The same nominal resin (e.g. “PP” or “PET”) is in fact a mixture of lots that already have different number-average (Mₙ) and weight-average (M_w) molecular weights, different polydispersities (Ð) and different end-group chemistries.  
2. Each lot therefore starts at a different point on the reaction coordinate and sees a slightly different local activation energy (Eₐ) for the degradation path that is most accessible to it.  
3. Once the temperature–time integral in the recycler’s extruder, dryer, or melt filter exceeds the lowest Eₐ in the blend, that reaction runs fastest and sets the direction in which the whole distribution moves.

The practical consequence is that the recycler cannot “tune” the molecular-weight distribution (MWD) to a target window; instead the distribution is pushed by the lowest-Eₐ pathway that is available in the worst-behaving fraction of the feed. That makes purity control (here defined as keeping the MWD inside the window that gives the desired melt-flow index, mechanical strength, odour, colour and crystallisation kinetics) extremely asymmetric:

- If chain scission has the lowest Eₐ (typical for PET, PA, PLA), the tail at the high-M end is barely touched while the low-M end grows; Mₙ drops, M_w/Mₙ rises, IV falls, and the material is rejected for bottle-grade or strapping applications.  
- If radical recombination or branching has the lowest Eₐ (typical for PP, PE under low-oxygen, high-shear conditions), the high-M tail grows faster than the low-M tail is truncated; M_w rises, gel count increases, melt elasticity becomes too high, and the recyclate blocks filters or gives surface defects in injection moulding.  
- If oxidation/colour-body formation has the lowest Eₐ (almost always true once traces of PVC, ink or metal are present), the discoloration reaction outruns any chain-length adjustment; even a perfectly centred MWD is sold at down-grade price because yellowness index or odour is out of spec.

Because the recycler has to hit a *simultaneous* specification on MFI (set by Mₙ), mechanical strength (set by M_w and Ð), gels (set by ultra-high-M fraction) and colour/odour (set by side-group chemistry), the width of the “usable” MWD window is narrow. The activation-energy hierarchy decides which edge of that window will be breached first, so the *same* thermal history that is “safe” for one feed mix becomes catastrophic for another mix that contains only a few percent of lower-Eₐ material. This is the fundamental constraint:

You can lower the process temperature to suppress the unwanted reaction, but then the viscosity rises above the pump limit; you can shorten residence time, but then the devolatilisation of moisture or residual print solvent is incomplete; you can add stabilisers, but they are consumed heterogeneously across the broad MWD and their radicals can actually open a new, even lower-Eₐ pathway in a minority of chains. In other words, the activation-energy landscape *itself* is reshaped by the breadth of the MWD you are trying to control, so convergence to a reproducible, high-purity recyclate is not just a mixing problem—it is a kinetic-escape problem whose boundary conditions change with every input bale.

Hence, without resorting to either (i) solvent-based dissolution–reprecipitation (which replaces the melt-phase Eₐ hierarchy by a crystallisation/freezing barrier that is much less sensitive to initial MWD) or (ii) controlled catalytic de-polymerisation back to monomer (which erases the memory of the initial MWD entirely), mechanical recyclers have to accept that the molecular-weight distribution will always be *pushed* by the lowest activation-energy channel present in the most reactive sub-population of the feed, and “purity” in the strict sense (a tight, reproducible MWD) is thermodynamically unattainable in the melt-extrusion loop alone.

## Annotations


## Sources
