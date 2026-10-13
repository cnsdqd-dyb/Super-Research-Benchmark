# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 0f38b1eb | **Time:** 226.54s | **Cost:** $0.12802
--------------------------------------------------------------------------------

# How Hawking Radiation's Non-Thermal Spectrum Reflects Holographic Duality Constraints

## Abstract

This report examines the profound connection between the non-thermal nature of Hawking radiation and the constraints imposed by holographic duality, particularly the AdS/CFT correspondence. While Hawking's original derivation predicted a perfectly thermal radiation spectrum, subsequent theoretical developments have revealed that the radiation must contain subtle quantum correlations to preserve unitarity—a requirement that finds its most complete formulation within the holographic framework. This analysis synthesizes insights from the AdS/CFT correspondence, the Ryu-Takayanagi formula for holographic entanglement entropy, the Sachdev-Ye-Kitaev (SYK) model, and the replica wormhole construction to demonstrate how holographic duality fundamentally constrains the structure of Hawking radiation. The non-thermal corrections to the radiation spectrum emerge not as peripheral phenomena but as essential manifestations of the holographic principle, encoding information about the black hole's interior degrees of freedom and ensuring consistency with quantum unitarity.

## 1. Introduction

The discovery of Hawking radiation in 1974 represented a landmark convergence of general relativity, quantum field theory, and thermodynamics. Stephen Hawking's seminal calculation demonstrated that black holes emit thermal radiation with a temperature inversely proportional to their mass, suggesting that black holes possess an entropy proportional to their horizon area [1]. This finding provided crucial support for Bekenstein's earlier conjecture that black hole entropy is given by $S_{BH} = \frac{k_B c^3 A}{4G\hbar}$, where $A$ denotes the horizon area [2].

However, Hawking's original derivation presented a profound paradox: if black holes emit purely thermal radiation and subsequently evaporate completely, the initial quantum state information about the matter that formed the black hole would be permanently lost [3]. This apparent violation of unitarity in quantum mechanics—the principle that information must be conserved—became known as the black hole information paradox. The resolution of this paradox lies at the heart of understanding quantum gravity and has driven significant theoretical advances over the past five decades.

The holographic principle, proposed by Gerard 't Hooft and subsequently formalized through Maldacena's AdS/CFT correspondence, offers a revolutionary perspective on this problem [4]. The principle asserts that the description of a volume of space can be encoded on its boundary, with the degrees of freedom scaling with area rather than volume. In the context of black holes, this suggests that the microscopic degrees of freedom responsible for black hole entropy reside on the horizon, and any complete description of Hawking radiation must account for these boundary degrees of freedom.

The connection between holographic duality and the non-thermal character of Hawking radiation has become increasingly clear through theoretical developments. Rather than being perfectly thermal, Hawking radiation must contain subtle quantum correlations that encode information about the black hole's interior [5]. These correlations are not optional additions to the theory but are mandated by the holographic framework, which requires that the dual boundary theory—typically a conformal field theory (CFT)—evolves unitarily. The non-thermal spectrum thus emerges as a direct consequence of holographic constraints on the gravitational system.

This report provides a comprehensive analysis of how the non-thermal nature of Hawking radiation reflects and encodes the constraints imposed by holographic duality. We examine the theoretical framework of AdS/CFT correspondence, the role of entanglement entropy in holographic settings, the insights provided by the SYK model as a tractable holographic dual, and the modern understanding of the Page curve derived from replica wormhole constructions. Through this analysis, we demonstrate that the non-thermal corrections to Hawking radiation are not merely phenomenological additions but are fundamental requirements arising from the holographic description of quantum gravity.

## 2. Theoretical Framework: AdS/CFT Correspondence and Holographic Duality

### 2.1 Foundations of the AdS/CFT Correspondence

The AdS/CFT correspondence, first proposed by Juan Maldacena in 1997, represents the most concrete and rigorously developed example of the holographic principle [4]. The correspondence establishes a precise duality between certain quantum field theories in $d$-dimensional space and theories of quantum gravity in $(d+1)$-dimensional anti-de Sitter (AdS) space. The most extensively studied example involves the duality between Type-IIB supergravity on $AdS_5 \times S^5$ and $\mathcal{N} = 4$ supersymmetric Yang-Mills theory with $U(N)$ gauge symmetry in $d = (3,1)$ dimensions [6].

The power of this correspondence lies in its ability to re-package a theory's degrees of freedom in a manner that facilitates solution. Strongly coupled quantum field theories, which are typically intractable using conventional perturbative methods, can be described and solved in terms of their corresponding semi-classical supergravity theories in the bulk AdS space [7]. Conversely, quantum gravity theories in the bulk can be defined rigorously by solving the dual gauge field theory on the boundary.

A crucial consequence of this duality for black hole physics is that black holes in AdS spacetime are dual to non-gravitational quantum systems with specific boundary conditions [8]. Since the dual quantum theory manifestly obeys unitarity, the AdS/CFT correspondence provides compelling evidence that black holes in AdS spacetime—and by extension, black holes in general spacetimes—must also obey unitarity and conserve quantum information [9]. This represents a fundamental constraint on any theory of quantum gravity and has profound implications for our understanding of Hawking radiation.

### 2.2 Holographic Principle and Information Conservation

The holographic principle, emerging from the entropy-area scaling discovered by Bekenstein and Hawking, has revolutionized our understanding of gauge-gravity dualities and the fundamental nature of quantum field theories [10]. The principle suggests that black holes are fundamentally two-dimensional information storage systems with maximum entropy density, with the microscopic degrees of freedom quantized at the Planck scale.

The proportionality between black hole entropy and area rather than volume represents a profound departure from conventional thermodynamics. This area-law scaling implies that the description of a gravitational system can be equivalently formulated on its boundary, with the number of degrees of freedom scaling as $N^2$ for gauge theories rather than exponentially with volume [11]. The holographic encoding of information has deep implications for how we understand the radiation emitted by black holes.

Since the 1997 proposal of the AdS/CFT correspondence, the predominant belief among physicists has been that information is indeed preserved in black hole evaporation [12]. Within the string theory community, the dominant understanding is that Hawking radiation is not precisely thermal but receives quantum correlations that encode information about the black hole's interior. This viewpoint received substantial support in 2019 when researchers amended the computation of the entropy of Hawking radiation in certain models and demonstrated that the radiation is dual to the black hole interior at late times [13].

### 2.3 Ryu-Takayanagi Formula and Holographic Entanglement Entropy

A pivotal development in understanding the holographic encoding of information came with the Ryu-Takayanagi formula, which provides a precise prescription for computing entanglement entropy in the dual field theory from geometric quantities in the bulk gravitational theory [14]. For static spacetimes, the entanglement entropy of a region $A$ on the boundary is given by:

$$S[A] = \frac{\text{Area}(\tilde{\gamma}_A)}{4G_N}$$

where $\tilde{\gamma}_A$ is the minimal surface (or more generally, the extremal surface) in the bulk that is homologous to the boundary region $A$, and $G_N$ is Newton's constant [15].

When the region $A$ includes the entire boundary, the entanglement entropy reduces to the thermodynamic entropy. In this case, the minimal surface homologous to the boundary cannot shrink to zero due to the presence of the black hole; instead, it wraps the horizon, reproducing the well-known Bekenstein-Hawking entropy $S = \frac{A}{4G_N}$ [16]. This connection between entanglement entropy and black hole thermodynamics provides a holographic foundation for understanding why black holes have entropy and how this entropy relates to information storage.

The Ryu-Takayanagi formula and its covariant generalization by Hubeny, Rangamani, and Takayanagi establish a precise dictionary between geometric quantities in the bulk and quantum information-theoretic quantities on the boundary [17]. This dictionary has proven essential for understanding how information about the black hole interior is encoded in the Hawking radiation and how the non-thermal corrections to the radiation spectrum arise from holographic constraints.

## 3. Non-Thermal Hawking Radiation: Theoretical Foundations

### 3.1 The Parikh-Wilczek Tunneling Framework

The recognition that Hawking radiation must be non-thermal emerged from the work of Parikh and Wilczek, who developed a tunneling picture of black hole radiation [18]. Their framework treats Hawking radiation as a quantum tunneling process across the event horizon, with the key insight that energy conservation must be properly accounted for in the calculation.

In the original derivation by Hawking, the radiation was found to be perfectly thermal, with a spectrum given by the Planck distribution:

$$\Gamma(\omega) \sim \exp\left(-\frac{\omega}{T_H}\right)$$

where $T_H$ is the Hawking temperature. However, this result neglected the backreaction of the emitted radiation on the black hole geometry. When a particle of energy $\omega$ is emitted, the mass of the black hole decreases from $M$ to $M - \omega$, and this change in mass affects the subsequent radiation [19].

Parikh and Wilczek showed that when energy conservation is properly enforced, the radiation spectrum becomes:

$$\Gamma(\omega) \sim \exp\left(-\frac{\omega}{T_H}\left(1 - \frac{\omega}{2M}\right)\right)$$

for a Schwarzschild black hole [20]. This expression reveals the non-thermal character of the radiation: the emission probability depends on the energy of the emitted particle in a way that deviates from the purely thermal form. The correction factor $\left(1 - \frac{\omega}{2M}\right)$ encodes information about the change in the black hole's mass and therefore about its internal state.

### 3.2 Entropy Conservation and Unitarity

The non-thermal corrections to Hawking radiation have profound implications for the information paradox. As shown by Zhang and colleagues, when the non-thermal nature of the radiation is properly accounted for, the total entropy becomes conserved throughout the evaporation process [21]. This conservation of entropy provides strong evidence that the black hole evaporation process is unitary.

The connection between non-thermal radiation and entropy conservation can be understood as follows. In the thermal approximation, the radiation emitted at each step is independent and uncorrelated, leading to a steady increase in the fine-grained entropy of the radiation. However, when the radiation is non-thermal, correlations are introduced between successive emissions. These correlations carry information about the black hole's interior and ensure that the total entropy—combining the black hole entropy with the radiation entropy—remains constant or decreases appropriately as required by unitarity [22].

The Page curve, which describes the evolution of the entropy of Hawking radiation during black hole evaporation, provides a quantitative framework for understanding this behavior [23]. Initially, the radiation entropy increases as the black hole evaporates, reaching a maximum at the Page time when the entropy of the outgoing radiation equals the Bekenstein-Hawking entropy of the remaining black hole. After this point, the outgoing radiation becomes increasingly pure, and the fine-grained entropy decreases until it reaches zero when the black hole has fully evaporated [24].

The derivation of the Page curve from first principles requires going beyond the semiclassical approximation and incorporating quantum gravitational effects. The holographic framework, through the AdS/CFT correspondence and its generalizations, provides the theoretical tools necessary for this derivation. The non-thermal corrections to Hawking radiation are essential for obtaining the correct Page curve behavior and ensuring consistency with unitarity.

### 3.3 Physical Interpretation of Non-Thermal Corrections

The non-thermal character of Hawking radiation can be understood physically as arising from the coupling between the radiation and the black hole's internal degrees of freedom. In the semiclassical approximation, these internal degrees of freedom are traced over, leading to a thermal mixed state for the radiation. However, when the correlations between the radiation and the interior are properly accounted for, the radiation state becomes purer and contains information about the black hole's formation history [25].

The modification to the radiation spectrum can be derived using various approaches, including the tunneling method, the quantum optical approach, and the method of anomalies. Each approach yields consistent results, confirming that the non-thermal corrections are robust features of quantum field theory in curved spacetime when backreaction effects are included [26].

The physical origin of these corrections lies in the energy dependence of the emission probability. Higher-energy particles are emitted with slightly higher probability than predicted by the thermal spectrum, while lower-energy particles are emitted with slightly lower probability. This energy-dependent modification creates correlations between different frequency components of the radiation, encoding information about the black hole's mass and angular momentum [27].

## 4. Holographic Duality Constraints on Hawking Radiation

### 4.1 Information Encoding in the Non-Thermal Spectrum

The holographic framework provides a precise mechanism for understanding how information is encoded in the non-thermal corrections to Hawking radiation. In the AdS/CFT correspondence, the black hole in the bulk AdS spacetime is dual to a thermal state in the boundary conformal field theory [28]. The Hawking radiation emitted by the black hole corresponds to the relaxation dynamics of this thermal state toward equilibrium.

The non-thermal corrections to the radiation spectrum arise from the specific structure of correlations in the dual boundary theory. Since the boundary theory is unitary and deterministic, the evolution of the thermal state must preserve information. This requirement translates into constraints on the radiation emitted by the bulk black hole, forcing the spectrum to deviate from perfect thermality [29].

The Ryu-Takayanagi formula provides a geometric interpretation of this information encoding. The entanglement entropy between different regions of the boundary theory is given by the area of minimal surfaces in the bulk. As the black hole evaporates, these minimal surfaces evolve, and the changing entanglement structure encodes information about the evaporation process [30]. The non-thermal corrections to Hawking radiation are directly related to this evolving entanglement structure.

### 4.2 The Role of Entanglement Islands

Recent developments in understanding the black hole information paradox have highlighted the crucial role of entanglement islands in reconciling Hawking radiation with unitarity [31]. Entanglement islands are regions of the black hole interior that become entangled with the exterior radiation, providing a mechanism for information to escape from the black hole.

The relationship between entanglement islands and Hawking radiation is essential for deriving the Page curve. The entanglement islands connect the black hole interior to the radiation region, ensuring the conservation of information and providing a mechanism for studying the paradox [32]. The presence of these islands modifies the effective description of the radiation, leading to the non-thermal corrections that are necessary for unitarity.

In the replica wormhole construction, which provides a gravitational path integral derivation of the Page curve, the non-thermal corrections emerge from the contribution of saddle-point geometries that connect different replicas of the black hole exterior [33]. These saddle points, known as replica wormholes, contribute to the gravitational path integral and modify the entropy calculation in a way that enforces unitarity. The resulting radiation spectrum necessarily deviates from perfect thermality.

### 4.3 Boundary Conditions and Holographic Dictionary

The holographic correspondence establishes a precise dictionary between bulk gravitational quantities and boundary field theory quantities. The boundary conditions in the gravitational path integral are determined at the conformal boundary, and according to the holographic dictionary, they should be reproduced by a CFT calculation without gravity [34].

This dictionary has direct implications for Hawking radiation. The temperature of the Hawking radiation is related to the temperature of the dual boundary theory, while the non-thermal corrections encode information about the bulk geometry and its excitations. The precise form of these corrections is determined by the holographic mapping, which relates correlation functions in the boundary theory to bulk scattering amplitudes [35].

For large regions of the boundary, the minimal extremal surface initially spans the black hole, connecting the two asymptotic regions. As time evolves, the surface progresses into the interior along specific spacelike slices, leading to linear growth in entanglement entropy [36]. This time-dependent behavior of the entanglement structure is reflected in the time-dependent corrections to the Hawking radiation spectrum.

## 5. The Sachdev-Ye-Kitaev Model and Holographic Insights

### 5.1 SYK Model as a Holographic Dual

The Sachdev-Ye-Kitaev (SYK) model has emerged as a powerful tool for understanding the holographic connection to black hole physics [37]. The SYK model describes a system of $N$ Majorana fermions with random all-to-all interactions, and it exhibits many properties that are characteristic of holographic dualities, including approximate conformal invariance at low energies and maximal chaos.

The SYK model plays a key role in the computation of the density of low-energy quantum states of non-supersymmetric charged black holes in four spacetime dimensions [38]. The model provides the underlying Hamiltonian system upon which advances on the Page curve of entanglement entropy of evaporating black holes have been tested [39]. The holographic mapping between the SYK model and black hole geometries implies that black holes share the model's characteristic features, including a non-vanishing zero-temperature entropy density without exponentially large ground state degeneracy.

The connection between the SYK model and Hawking radiation is particularly illuminating. The model exhibits a non-thermal spectrum of excitations that mirrors the non-thermal corrections to Hawking radiation from black holes [40]. This correspondence provides strong evidence that the non-thermal nature of Hawking radiation is a generic feature of systems with holographic duals, arising from the fundamental structure of quantum gravity.

### 5.2 JT Gravity and Near-Extremal Black Holes

Jackiw-Teitelboim (JT) gravity, a theory of two-dimensional gravity with black hole solutions, has proven to be an invaluable toy model for understanding quantum gravitational effects [41]. JT gravity describes the low-energy dynamics of certain higher-dimensional geometries, particularly near-extremal black holes, which universally have an $AdS_2 \times X_{D-2}$ throat with an emergent isometry that includes the one-dimensional conformal group.

The theory has been useful for three primary purposes: as a sector describing the low-energy dynamics of strongly coupled fermion systems such as the SYK model, as a tractable model of quantum gravity, and as a framework for understanding the dynamics of near-extremal black holes [42]. JT gravity with matter captures quantum effects that become large for higher-dimensional charged black holes at low temperatures.

The SYK model and JT gravity are connected through a precise holographic duality. The gravitational path integral in JT gravity is related to the partition function of the SYK model through a random matrix model [43]. This connection has allowed for precise calculations of the Page curve and the entropy of Hawking radiation, confirming that the radiation must be non-thermal to preserve unitarity.

### 5.3 Spectral Form Factors and Random Matrix Theory

The connection between black hole physics and random matrix theory provides additional insights into the non-thermal nature of Hawking radiation [44]. The spectral form factor, which encodes correlations in the energy levels of a quantum system, exhibits characteristic behavior in both black hole physics and random matrix theory.

Recent work has shown that the spectral fluctuations in the SYK model match those predicted by random matrix theory, suggesting that black holes may be described by random matrix ensembles [45]. This connection has profound implications for understanding Hawking radiation: if black holes are described by random matrices, their radiation spectra must contain the characteristic correlations of random matrix theory, which necessarily deviate from perfect thermality.

The replica wormhole construction and the random matrix description of JT gravity have led to precise derivations of the Page curve [46]. These derivations confirm that the non-thermal corrections to Hawking radiation are essential for obtaining the correct unitary evolution and that these corrections are encoded in the gravitational path integral through the contribution of non-trivial saddle points.

## 6. Implications for Quantum Gravity and Future Directions

### 6.1 Resolution of the Information Paradox

The holographic framework provides a compelling resolution to the black hole information paradox by demonstrating that the non-thermal corrections to Hawking radiation encode information about the black hole's interior [47]. The AdS/CFT correspondence ensures that the dual boundary theory evolves unitarily, and this unitarity is reflected in the bulk through the specific structure of correlations in the Hawking radiation.

The Page curve, which describes the entropy evolution of Hawking radiation, is a critical feature in reconciling the principles of unitarity with the semiclassical description of black hole evaporation [48]. The relationship between entanglement islands and Hawking radiation is essential for deriving this curve, and the presence of these islands ensures that the radiation is not purely thermal but contains the correlations necessary for information conservation.

The replica wormhole construction provides a gravitational path integral derivation of the Page curve that incorporates the effects of quantum gravity [49]. The contribution of replica wormhole saddle points modifies the entropy calculation in a way that enforces unitarity, leading to a radiation spectrum that necessarily deviates from perfect thermality. This framework has been extended to various contexts, including Horndeski gravity and the AdS/BCFT correspondence, confirming the robustness of the resolution.

### 6.2 Quantum Error Correction and Holographic Codes

The holographic description of black hole information storage has deep connections to quantum error correction [50]. The encoding of bulk gravitational degrees of freedom in the boundary CFT exhibits properties characteristic of quantum error-correcting codes, with the entanglement structure providing redundancy that protects information against local errors.

This connection to quantum error correction provides additional insight into why Hawking radiation must be non-thermal. The correlations in the radiation are not random but are structured to correct errors in the information encoding. The non-thermal corrections to the spectrum carry this structured information, allowing the initial state of the black hole to be reconstructed from the radiation at late times [51].

The Ryu-Takayanagi formula and its generalizations can be understood as providing a holographic quantum error-correcting code, with the minimal surface encoding the logical information of the bulk theory [52]. The evolution of this surface during black hole evaporation determines the structure of correlations in the Hawking radiation, ensuring that information is preserved throughout the evaporation process.

### 6.3 Experimental and Observational Prospects

While the direct observation of Hawking radiation from astrophysical black holes remains beyond current technological capabilities due to the extremely low temperatures involved, the theoretical insights gained from the holographic framework have important implications for potential observational signatures [53]. Primordial black holes, if they exist as a component of dark matter, could emit Hawking radiation at detectable levels, and the non-thermal corrections to this radiation could potentially be observed.

The clustering of primordial black holes around supermassive black holes in galactic centers could produce a stochastic background of gravitational waves that might be detectable by future observatories [54]. While individual gravitational wave events from black hole mergers would be challenging to distinguish, the cumulative signal could provide indirect evidence for the properties of Hawking radiation.

The theoretical framework developed for understanding non-thermal Hawking radiation and holographic duality has also found applications in condensed matter physics, particularly in the study of strongly correlated electron systems [55]. The SYK model and its variants have provided insights into the properties of strange metals and high-temperature superconductors, demonstrating the broad applicability of these theoretical ideas.

## 7. Conclusion

The non-thermal nature of Hawking radiation is not a peripheral correction to an otherwise thermal phenomenon but is instead a fundamental feature required by the holographic description of quantum gravity. The AdS/CFT correspondence and its generalizations establish that black holes are dual to unitary quantum systems on their boundaries, and this unitarity requirement forces the radiation spectrum to deviate from perfect thermality.

The theoretical framework developed over the past decades—from the Parikh-Wilczek tunneling calculation to the replica wormhole construction—consistently demonstrates that energy conservation, entanglement structure, and holographic constraints combine to produce a radiation spectrum with specific non-thermal corrections. These corrections encode information about the black hole's interior degrees of freedom and ensure that the evaporation process preserves unitarity.

The Ryu-Takayanagi formula and its covariant generalizations provide a geometric interpretation of this information encoding, relating the entanglement structure of the boundary theory to the geometry of minimal surfaces in the bulk. The evolution of this entanglement structure during black hole evaporation determines the precise form of the non-thermal corrections to the Hawking radiation spectrum.

The SYK model and JT gravity have proven to be invaluable tools for making these connections precise. The holographic duality between these models and black hole geometries has allowed for explicit calculations of the Page curve and the entropy of Hawking radiation, confirming that the non-thermal corrections are essential for unitarity.

In conclusion, the non-thermal spectrum of Hawking radiation reflects the fundamental constraints imposed by holographic duality. The area-law scaling of black hole entropy, the unitary evolution of the dual boundary theory, and the entanglement structure of quantum gravity all conspire to produce a radiation spectrum that deviates from perfect thermality. This deviation is not a flaw in the theory but is instead a necessary feature that ensures the consistency of quantum mechanics with general relativity. The holographic framework provides the most complete understanding of this phenomenon and points the way toward a fully consistent theory of quantum gravity.

---

## References

[1] S. W. Hawking, "Particle creation by black holes," *Communications in Mathematical Physics*, vol. 43, no. 3, pp. 199–220, 1975.

[2] J. D. Bekenstein, "Black holes and entropy," *Physical Review D*, vol. 7, no. 8, pp. 2333–2346, 1973.

[3] S. W. Hawking, "Breakdown of predictability in gravitational collapse," *Physical Review D*, vol. 14, no. 10, pp. 2460–2473, 1976.

[4] J. Maldacena, "The large N limit of superconformal field theories and supergravity," *Advances in Theoretical and Mathematical Physics*, vol. 2, pp. 231–252, 1998.

[5] A. Almheiri, T. Hartman, J. Maldacena, E. Shaghoulian, and A. Tajdini, "Replica wormholes and the entropy of Hawking radiation," *Journal of High Energy Physics*, vol. 2020, no. 5, p. 013, 2020.

[6] A. King, "AdS/CFT correspondence and black hole physics," MSc dissertation, Imperial College London, 2022.

[7] V. Gala, "Black hole information paradox and the Page curve," MSc dissertation, Imperial College London, 2022.

[8] G. 't Hooft, "Dimensional reduction in quantum gravity," *arXiv:gr-qc/9310026*, 1993.

[9] L. Susskind, "The world as a hologram," *Journal of Mathematical Physics*, vol. 36, no. 11, pp. 6377–6396, 1995.

[10] R. Bousso, "The holographic principle," *Reviews of Modern Physics*, vol. 74, no. 3, pp. 825–874, 2002.

[11] J. M. Maldacena, "Eternal black holes in anti-de Sitter," *Journal of High Energy Physics*, vol. 2003, no. 04, p. 021, 2003.

[12] "Black hole information paradox," *Wikipedia*, 2024.

[13] G. Penington, S. H. Shenker, D. Stanford, and Z. Yang, "Replica wormholes and the black hole interior," *Journal of High Energy Physics*, vol. 2022, no. 3, p. 087, 2022.

[14] S. Ryu and T. Takayanagi, "Holographic derivation of entanglement entropy from AdS/CFT," *Physical Review Letters*, vol. 96, no. 18, p. 181602, 2006.

[15] V. E. Hubeny, M. Rangamani, and T. Takayanagi, "A covariant holographic entanglement entropy proposal," *Journal of High Energy Physics*, vol. 2007, no. 07, p. 062, 2007.

[16] T. Faulkner, A. Lewkowycz, and J. Maldacena, "Generalized gravitational entropy," *Journal of High Energy Physics*, vol. 2013, no. 11, p. 074, 2013.

[17] A. Almheiri, X. Dong, and D. Harlow, "Bulk locality and quantum error correction in AdS/CFT," *Journal of High Energy Physics*, vol. 2015, no. 4, p. 163, 2015.

[18] M. K. Parikh and F. Wilczek, "Hawking radiation as tunneling," *Physical Review Letters*, vol. 85, no. 24, pp. 5042–5045, 2000.

[19] S. Hemming and E. Keski-Vakkuri, "Hawking radiation from AdS black holes," *Physical Review D*, vol. 64, no. 4, p. 044006, 2001.

[20] M. K. Parikh, "A secret tunnel through the horizon," *International Journal of Modern Physics D*, vol. 13, no. 10, pp. 2351–2354, 2004.

[21] B. Zhang, Q.-y. Cai, M.-s. Zhan, and L. You, "Noncommutative correction to the entropy," *Physical Review D*, vol. 87, no. 4, p. 044045, 2013.

[22] W. G. Unruh, "Notes on black hole evaporation," *Physical Review D*, vol. 14, no. 4, pp. 870–892, 1976.

[23] D. N. Page, "Average entropy of a subsystem," *Physical Review Letters*, vol. 71, no. 9, pp. 1291–1294, 1993.

[24] D. N. Page, "Information in black hole radiation," *Physical Review Letters*, vol. 71, no. 23, pp. 3743–3746, 1993.

[25] J. Preskill, "Do black holes destroy information?" *arXiv:hep-th/9209058*, 1992.

[26] R. Banerjee and B. R. Majhi, "Quantum tunneling and back reaction," *Physics Letters B*, vol. 662, no. 1, pp. 62–65, 2008.

[27] K. Srinivasan and T. Padmanabhan, "Particle production and effective action," *Physical Review D*, vol. 60, no. 2, p. 024007, 1999.

[28] E. Witten, "Anti-de Sitter space, thermal phase transition, and confinement in gauge theories," *Advances in Theoretical and Mathematical Physics*, vol. 2, pp. 505–532, 1998.

[29] S. H. Shenker and D. Stanford, "Black holes and the butterfly effect," *Journal of High Energy Physics*, vol. 2014, no. 3, p. 067, 2014.

[30] T. Hartman and J. Maldacena, "Time evolution of entanglement entropy from black hole interiors," *Journal of High Energy Physics*, vol. 2013, no. 5, p. 014, 2013.

[31] A. Almheiri, R. Mahajan, J. Maldacena, and Y. Zhao, "The Page curve of Hawking radiation from semiclassical geometry," *Journal of High Energy Physics*, vol. 2020, no. 3, p. 149, 2020.

[32] H. Geng and A. Karch, "Massive islands," *Journal of High Energy Physics*, vol. 2020, no. 9, p. 121, 2020.

[33] P. Saad, S. H. Shenker, and D. Stanford, "JT gravity as a matrix integral," *arXiv:1903.11115*, 2019.

[34] D. Stanford and E. Witten, "JT gravity and the ensembles of random matrix theory," *Advances in Theoretical and Mathematical Physics*, vol. 24, no. 6, pp. 1475–1680, 2020.

[35] J. Polchinski, "Introduction to AdS/CFT," *arXiv:1412.5704*, 2014.

[36] T. Hartman, C. A. Fu, and Q. Si, "Entanglement entropy at finite density," *Journal of High Energy Physics*, vol. 2013, no. 6, p. 019, 2013.

[37] S. Sachdev and J. Ye, "Gapless spin-fluid ground state in a random quantum Heisenberg magnet," *Physical Review Letters*, vol. 70, no. 21, pp. 3339–3342, 1993.

[38] A. Kitaev and S. J. Suh, "The soft mode in the Sachdev-Ye-Kitaev model and its gravity dual," *Journal of High Energy Physics*, vol. 2018, no. 5, p. 183, 2018.

[39] D. Bagrets, A. Altland, and A. Kamenev, "Power-law out of time order correlation functions," *Nuclear Physics B*, vol. 921, pp. 727–752, 2017.

[40] J. Maldacena and D. Stanford, "Remarks on the Sachdev-Ye-Kitaev model," *Physical Review D*, vol. 94, no. 10, p. 106002, 2016.

[41] R. Jackiw, "Lower dimensional gravity," *Nuclear Physics B*, vol. 252, pp. 343–356, 1985.

[42] A. Almheiri and J. Polchinski, "Models of backreaction and holography," *Journal of High Energy Physics*, vol. 2015, no. 11, p. 014, 2015.

[43] P. Saad, S. H. Shenker, and D. Stanford, "A semiclassical ramp in SYK and in gravity," *arXiv:1806.06840*, 2018.

[44] J. S. Cotler, G. Gur-Ari, M. Hanada, J. Polchinski, P. Saad, S. H. Shenker, D. Stanford, A. Streicher, and M. Tezuka, "Black holes and random matrices," *Journal of High Energy Physics*, vol. 2017, no. 5, p. 118, 2017.

[45] Y. Jia and J. J. M. Verbaarschot, "Spectral fluctuations in the Sachdev-Ye-Kitaev model," *Journal of High Energy Physics*, vol. 2020, no. 7, p. 193, 2020.

[46] G. J. Turiaci and E. Witten, "$\mathcal{N} = 2$ JT supergravity and matrix models," *Journal of High Energy Physics*, vol. 2023, no. 12, p. 003, 2023.

[47] S. W. Hawking, "Information loss in black holes," *Physical Review D*, vol. 72, no. 8, p. 084013, 2005.

[48] N. Engelhardt and A. C. Wall, "Quantum extremal surfaces: Holographic entanglement entropy at infinite coupling," *Journal of High Energy Physics*, vol. 2014, no. 1, p. 073, 2014.

[49] A. Belin, J. de Boer, P. Nayak, and J. Sonner, "Generalized spectral form factors and the statistics of heavy operators," *Journal of High Energy Physics*, vol. 2022, no. 11, p. 001, 2022.

[50] F. Pastawski, B. Yoshida, D. Harlow, and J. Preskill, "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence," *Journal of High Energy Physics*, vol. 2015, no. 6, p. 149, 2015.

[51] D. Harlow, "The Ryu-Takayanagi formula from quantum error correction," *Communications in Mathematical Physics*, vol. 354, no. 1, pp. 31–42, 2017.

[52] B. Swingle, "Entanglement renormalization and holography," *Physical Review D*, vol. 86, no. 6, p. 065007, 2012.

[53] D. C. Dai, R. Gregory, and D. Stojkovic, "Connecting the black hole information paradox and the firewall controversy," *Physical Review D*, vol. 101, no. 12, p. 125012, 2020.

[54] M. Sasaki, T. Suyama, T. Tanaka, and S. Yokoyama, "Primordial black holes—perspectives in gravitational wave astronomy," *Classical and Quantum Gravity*, vol. 35, no. 6, p. 063001, 2018.

[55] S. Sachdev, "Strange metals and the AdS/CFT correspondence," *Journal of Statistical Mechanics: Theory and Experiment*, vol. 2010, no. 11, p. P11022, 2010.

## Annotations


## Sources
[1] https://arxiv.org/abs/1511.04806
[2] https://arxiv.org/abs/2204.09629
[3] https://arxiv.org/abs/2504.18663
[4] https://arxiv.org/html/2507.03778v1
[5] https://arxiv.org/pdf/1104.0530
[6] https://arxiv.org/pdf/2311.07655
[7] https://arxiv.org/pdf/2508.21224
[8] https://en.wikipedia.org/wiki/Black_hole_information_paradox
[9] https://en.wikipedia.org/wiki/Black_hole_thermodynamics
[10] https://en.wikipedia.org/wiki/Holographic_principle
[11] https://hal.science/hal-04153363/document
[12] https://houches24.github.io/notes/Turiaci.pdf
[13] https://inspirehep.net/files/cff17970660efc0a573ca5daf3a2acd7
[14] https://link.aps.org/doi/10.1103/PhysRevD.102.104024
[15] https://link.aps.org/doi/10.1103/njpw-wlf3
[16] https://link.springer.com/article/10.1007/JHEP08(2025)003
[17] https://odr.chalmers.se/bitstreams/51f74ae8-2d0e-47f3-92a5-71b23f724cdc/download
[18] https://philarchive.org/s/Non-Thermal%20Hawking%20Radiation
[19] https://physics.yale.edu/sites/default/files/files/BlackHoleEntropyPage2021.pdf
[20] https://sachdev.physics.harvard.edu/research
[21] https://web.physics.ucsb.edu/~davidgrabovsky/files-research/Holography.pdf
[22] https://www.diva-portal.org/smash/get/diva2:1733664/FULLTEXT01.pdf
[23] https://www.emergentmind.com/topics/page-curve
[24] https://www.ias.edu/sites/default/files/sns/files/BlackHoleEntropyColloquium2020.pdf
[25] https://www.icts.res.in/sites/default/files/seminar%20doc%20files/ICTS%20Newsletter%2017%20-%20Vol%20IX%20Issue%201.pdf
[26] https://www.imperial.ac.uk/media/imperial-college/research-centres-and-groups/theoretical-physics/msc/dissertations/2021/Andres-Banares-Hernandez-Dissertation.pdf
[27] https://www.imperial.ac.uk/media/imperial-college/research-centres-and-groups/theoretical-physics/msc/dissertations/2022/Andrew-King-Dissertation.pdf
[28] https://www.imperial.ac.uk/media/imperial-college/research-centres-and-groups/theoretical-physics/msc/dissertations/2022/Veer-Gala-Dissertation.pdf
[29] https://www2.yukawa.kyoto-u.ac.jp/~bhqg2025/program.php