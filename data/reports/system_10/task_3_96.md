# Deep Research Report: perplexity/sonar-deep-research
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** c7610415 | **Time:** 112.94s | **Cost:** $0.92069
--------------------------------------------------------------------------------

# Hawking Radiation's Non-Thermal Spectrum and Holographic Duality Constraints

The discovery of Hawking radiation in 1974 fundamentally transformed our understanding of black holes, demonstrating that these objects are not perfectly black but instead emit thermal radiation due to quantum effects near the event horizon[8][39]. However, this revelation created one of the most profound paradoxes in theoretical physics: if black holes emit thermal radiation and eventually evaporate completely, information about their initial state appears to be lost, violating the unitarity principle that lies at the heart of quantum mechanics. Recent developments in string theory and quantum gravity, particularly the formulation of the AdS/CFT correspondence and the holographic principle, have provided remarkable insights into this puzzle. These holographic frameworks impose stringent consistency conditions on black hole evaporation, requiring that the spectrum of Hawking radiation cannot be purely thermal but must contain non-thermal correlations that encode information about the black hole's interior. This report examines how holographic duality constraints naturally lead to a non-thermal spectrum of Hawking radiation and how this reconciles quantum mechanical unitarity with gravitational physics.

## The Thermal Spectrum and Its Theoretical Foundation

Stephen Hawking's original calculation in 1974 demonstrated that a black hole would emit radiation with a characteristic blackbody spectrum at a specific temperature determined by the black hole's mass[39]. The Hawking temperature is given by the formula \(T_H = \frac{\hbar c^3}{8\pi GM k_B}\), where the temperature depends inversely on the black hole's mass, implying that smaller black holes are hotter and radiate more intensely[8][39]. This thermal nature of the radiation emerges from the semiclassical approximation in which one treats quantum fields in a curved spacetime background using fixed classical gravitational geometry. The radiation carries away energy from the black hole, causing it to evaporate, with the timescale for complete evaporation given by \(t_{ev} \approx 5120\pi t_P \left(\frac{M}{m_P}\right)^3\), where \(t_P\) is the Planck time and \(m_P\) is the Planck mass[39].

The origin of Hawking radiation lies in the Unruh effect and vacuum polarization near the event horizon[39]. An accelerating observer near the black hole horizon experiences what appears to be a thermal bath of particles emerging from the horizon, consistent with an equivalence principle argument applied to the horizon itself[39]. The spectrum observed by a distant observer at infinity differs from the spectrum at the horizon due to gravitational redshift and the effective potential barrier created by the black hole's spacetime geometry. The transmission coefficient describing how radiation escapes to infinity is called the greybody factor, a frequency-dependent quantity that "filters" the initial thermal spectrum produced at the horizon[16]. Despite these modifications to the spectrum as it propagates outward, the radiation observed at infinity remains approximately thermal, with only small corrections accounting for the geometry-dependent effects.

However, the thermal nature of this spectrum creates an immediate problem for quantum mechanics. If a black hole begins in a pure quantum state (as required by quantum mechanics) and completely evaporates by emitting only thermal radiation, the final state of the universe would be described by a mixed state (a thermal bath of radiation) rather than a pure state[8]. This means that information about the initial state has been lost, violating the fundamental principle of unitary evolution in quantum mechanics. The von Neumann entropy of the radiation would increase monotonically throughout the evaporation process, reaching a maximum at the moment of complete evaporation[8]. This represents a fundamental inconsistency between general relativity and quantum mechanics, lying at the core of the black hole information paradox.

## The Information Paradox and Unitarity Constraints

The black hole information paradox presents one of the most serious challenges to our current understanding of fundamental physics[8][9][12]. Don Page's 1993 analysis provided crucial insight by arguing that if black hole evaporation truly violates unitarity, the entropy of the Hawking radiation should increase monotonically from zero at the beginning of the evaporation process to a maximum entropy comparable to the Bekenstein-Hawking entropy of the black hole[8]. However, if unitarity is preserved, Page showed that the entropy of the radiation should initially increase but then decrease back to zero when the black hole has completely evaporated, following a characteristic curve now known as the Page curve[8].

The Page curve represents perhaps the most important diagnostic tool for distinguishing between unitary and non-unitary evolution. At the Page time, defined as approximately half the black hole's lifetime, the entropy reaches its maximum value[8][11]. Before the Page time, the radiation appears to be thermally entangled only with itself, carrying no information about the black hole's interior. After the Page time, the radiation must become correlated with the remaining black hole, allowing information to escape. This shift in entanglement structure is fundamentally incompatible with a purely thermal spectrum, which would correspond to the Hawking curve (monotonic entropy increase) rather than the Page curve[8].

The firewall paradox, proposed by Almheiri, Marolf, Polchinski, and Sully in 2012, further sharpened the stakes of the information paradox[49][52]. This argument demonstrates that if Hawking radiation is purely thermal and information is to be preserved, one of three seemingly fundamental principles must be violated: quantum mechanics must be non-unitary, the equivalence principle must fail, or there must be a high-energy firewall at the black hole horizon that incinerates infalling observers[49][52]. The firewall argument shows that for sufficiently old black holes, the radiation emitted after the Page time must be highly entangled with the radiation emitted before the Page time (to preserve unitarity). However, quantum field theory in curved spacetime suggests that each mode of radiation should be entangled with its partner still inside the black hole. This double-entanglement violates the monogamy of entanglement, which states that a quantum system cannot be maximally entangled with more than one other system. The firewall paradox suggests that this contradiction is resolved by a firewall at the horizon, though this possibility seems to violate the equivalence principle.

These considerations make clear that any resolution of the information paradox must modify our understanding of Hawking radiation. The radiation cannot be purely thermal; instead, it must carry subtle correlations that encode information about the black hole's initial state. Understanding the nature of these non-thermal correlations requires a more complete theory of quantum gravity that goes beyond the semiclassical approximation used in Hawking's original calculation.

## Holographic Duality Framework and AdS/CFT Correspondence

The AdS/CFT correspondence, proposed by Juan Maldacena in 1997, provides the most concrete realization of the holographic principle[5][2]. This duality establishes a precise equivalence between a theory of quantum gravity in a $(d+1)$-dimensional anti-de Sitter (AdS) spacetime and a conformal field theory (CFT) living on the $d$-dimensional boundary of that spacetime[5][9]. The correspondence is strongest in the regime where gravity in the bulk is weakly coupled and quantum corrections are small, corresponding to a large central charge and strongly coupled CFT on the boundary. In this semiclassical limit, bulk quantum fields correspond to local operators in the boundary CFT, and the entire structure of spacetime and quantum fields in the bulk can be reconstructed from boundary CFT data[5].

A crucial aspect of the AdS/CFT correspondence is its holographic dictionary, which establishes precise relationships between bulk and boundary quantities[2]. The metric in the bulk corresponds to the expectation value of the stress-energy tensor in the CFT; local operators in the CFT correspond to fields in the bulk; and correlation functions in the CFT map to correlation functions of bulk fields with appropriate boundary conditions[5]. Because the boundary CFT is unitary and its time evolution preserves quantum information (in accordance with the Schrödinger equation), the AdS/CFT correspondence implies that bulk quantum gravity must also be unitary[2][7][9]. This has profound consequences for understanding black hole evaporation.

In the AdS/CFT context, an eternal black hole in the bulk corresponds to a thermal state in the boundary CFT at finite temperature equal to the Hawking temperature[2][7][9]. The entropy of the black hole (given by the Bekenstein-Hawking formula proportional to the area of the event horizon) equals the entropy of the thermal state in the CFT[2][7]. More importantly, when a black hole forms and evaporates in AdS spacetime, the entire process corresponds to unitary time evolution in the boundary CFT. An initial pure state in the CFT evolves unitarily to another pure state; no information is lost[2][9]. This directly implies that the Hawking radiation from a black hole in AdS spacetime cannot be perfectly thermal, since thermal radiation alone cannot preserve the unitarity of the overall process.

The holographic principle also suggests a profound connection between entanglement and spacetime geometry through the Ryu-Takayanagi (RT) formula[5][9]. This formula relates the entanglement entropy of a CFT subregion to the area of a minimal extremal surface in the bulk spacetime homologous to that subregion[5]. The RT surface acts as a generalized horizon, measuring the degree of entanglement between the subregion and the rest of the system. For black hole evaporation, the quantum extremal surface (a generalization of the RT surface that includes quantum corrections) plays a crucial role in determining whether information is preserved[14][35].

## Non-Thermal Spectrum Emergence from Exact Treatment

The fundamental insight that reconciles Hawking radiation with holographic duality comes from recognizing that the thermal spectrum emerges only as an approximation[1][4]. Recent work shows that when one treats the derivation of Hawking radiation more carefully beyond the geometric optics approximation, non-thermal corrections naturally appear[1][4]. In Hawking's original calculation, the thermal spectrum arises from computing Bogolubov coefficients that relate initial and final quantum field modes using WKB approximation in the geometric optics limit, where wavelengths are much smaller than the characteristic length scale of the spacetime[1][4].

When higher-order corrections in the wave packet overlap integral and quantum field interactions are included, the resulting spectrum deviates from perfect thermality[1][4]. These deviations are small in typical contexts but become increasingly significant as the black hole evaporates and approaches the Planck scale. More importantly, the non-thermal spectrum naturally encodes correlations between different modes of radiation, which is precisely what holographic constraints require[1][4][47]. These correlations allow information that appears to be lost in the thermal spectrum to actually be preserved in the subtle correlations between different radiation modes.

The appearance of non-thermal corrections can be understood through the generalized uncertainty principle (GUP) framework, which incorporates quantum gravity effects[37][47]. When Planck-scale physics is properly accounted for through corrections to the uncertainty relation, the Hawking radiation spectrum is modified such that it is no longer purely thermal[37][47]. Specifically, inclusion of GUP corrections leads to modifications of the de Broglie relation in the quantum tunneling process of black hole evaporation, providing non-thermal effects that create correlations between emitted modes[47]. These GUP-induced correlations encode information about the black hole's interior, allowing at least part of the quantum information to be preserved in the Hawking radiation[47].

Alternative approaches to studying the spectrum modifications also reveal non-thermal features. In models with modified dispersion relations that account for Planck-scale physics, the thermal spectrum is modified, though the leading-order corrections are generally suppressed by the Planck mass and thus small for macroscopic black holes[15]. However, these corrections become significant for small primordial black holes[3]. The energy dependence of the spectrum near the Planck scale shows structure not present in the purely thermal spectrum, with discrete frequency peaks corresponding to quantum gravity effects[39].

## Greybody Factors and Spectrum Transmission

A crucial intermediate step between the thermal spectrum at the horizon and the spectrum observed at infinity is described by greybody factors[13][16][25]. These factors describe the transmission coefficient for radiation across the potential barrier created by the black hole's spacetime geometry, and they vary with the frequency of the radiation[13][16]. For a Schwarzschild black hole, the greybody factor for low frequencies shows characteristic $\ell$-dependent behavior related to the angular momentum barrier experienced by the radiation, while at high frequencies the transmission approaches unity[13][16].

The physical interpretation of greybody factors is crucial for understanding how non-thermal information can be encoded in Hawking radiation. The barrier that filters the radiation acts differently on different modes, causing the spectrum to be modified in a frequency- and geometry-dependent manner[16]. This frequency-dependent filtering naturally creates correlations between different modes of radiation, since the probability of different modes escaping depends on their specific properties in a non-trivial way. These correlations represent a fundamental source of non-thermality in the observed spectrum.

Recent studies of greybody factors at high frequencies have revealed unexpected features that may be crucial for understanding quantum gravity effects in Hawking radiation[16]. The behavior of the transmission coefficient at large frequencies encodes information about the quantum structure of the black hole, providing a window into the microscopic degrees of freedom responsible for black hole entropy[16]. In some cases, greybody factors computed semiclassically can be exactly reproduced by string theory calculations, as was shown for certain black holes, suggesting that greybody factors probe the same microscopic physics as the black hole entropy[16].

For black holes in AdS spacetime, greybody factors take on additional significance through the AdS/CFT correspondence. The wave scattering properties of black holes in the bulk correspond to specific properties of the boundary CFT, providing another manifestation of the holographic duality[16]. The frequency-dependent transmission coefficients relate to properties of operators in the CFT through the holographic dictionary, providing a concrete way to test holographic predictions about information preservation.

## Page Curve and Information Recovery Dynamics

The Page curve represents the quantum information-theoretic signature of unitary black hole evaporation, and understanding how it emerges from holographic principles has been a major breakthrough in theoretical physics[8][11][20]. The Page curve predicts that the entanglement entropy of Hawking radiation initially increases from zero, reaches a maximum at the Page time (approximately half the black hole's lifetime), and then decreases back to zero when the black hole has completely evaporated[8][11].

The recent derivation of the Page curve using holographic methods has provided concrete evidence that information is indeed preserved in black hole evaporation[35]. Geoffrey Penington showed that at the Page time, there is a phase transition in the location of the quantum extremal surface (QES)[35]. Before the Page time, the QES is located at the event horizon; after the Page time, it moves to a position just inside the event horizon, at an infalling time approximately equal to the scrambling time into the past. This transition in the location of the QES directly causes the entanglement entropy of the radiation to reach its maximum and then begin decreasing[35].

The physical interpretation of this transition is profound: after the Page time, part of the interior of the black hole becomes encoded in the early Hawking radiation through the entanglement wedge[35]. The entanglement wedge is the bulk region that can be reconstructed from a given boundary subregion using entanglement wedge reconstruction, which relates bulk locality to boundary entanglement structure[35]. When the QES moves inside the horizon, the entanglement wedge expands to include a portion of the black hole interior, meaning that information about the interior becomes accessible through measurements on the early radiation[35].

A model illustrating the Page curve using holographic methods is the holographic moving mirror[20]. In this two-dimensional conformal field theory setup with a moving boundary, calculating the entanglement entropy evolution produces a curve that follows the ideal Page curve[20]. This computation demonstrates that the Page curve emerges naturally from holography in the strong coupling regime, providing support for the idea that information is preserved through the holographic mechanism[20].

The Page curve also appears in more complex scenarios, such as holographic superconductors[11]. When the thermal bath surrounding the black hole undergoes a phase transition due to the formation of a scalar condensate coupled to a gauge field, the entanglement dynamics with the black hole change significantly, resulting in variations in the Page curve and Page time[11]. This demonstrates that the detailed properties of the Page curve depend sensitively on the specific holographic model, but the fundamental structure of information recovery is preserved across different scenarios.

## Quantum Extremal Surfaces and Island Formula

The quantum extremal surface (QES) has emerged as the central concept in modern understanding of how information is preserved in black hole evaporation[14][35]. The QES is defined as a codimension-two surface in the bulk spacetime where the generalized entropy is extremized[14][35]. The generalized entropy includes both the area of the surface (contribution from the bulk geometry) and the entanglement entropy of the quantum fields in the bulk region bounded by the surface[35].

The island formula provides a method for calculating the entanglement entropy of radiation outside a black hole by including contributions from an "island" region inside the black hole[14][35]. The total entanglement entropy of the radiation is given by: \(S(R) = \min_{\text{QES}} \left[\frac{\text{Area}(\text{QES})}{4G_N} + S_{\text{in}}(\text{QES})\right]\), where the minimum is taken over all possible surfaces homologous to the radiation region, and $S_{\text{in}}$ is the entropy of the quantum fields inside the QES[35]. The remarkable aspect of this formula is that it automatically implements information preservation: at early times, when the island is small, the area term dominates and the entropy grows; at late times, when the island becomes large, the bulk entropy term grows but the overall entropy decreases due to the minimization procedure[35].

The universality of the island structure in evaporating black holes has been demonstrated across different scenarios[14]. The boundary of the island is always located outside the horizon for stationary black holes but inside the horizon for evaporating black holes, independent of the specific details of the black hole geometry[14]. This universality suggests that the island mechanism represents a fundamental feature of quantum gravity, rather than an artifact of particular models or approximations.

However, important caveats exist regarding the generality of the island mechanism. In some scenarios, such as certain non-standard black hole geometries like Liouville black holes, the island formula fails to produce a sensible Page curve[17]. In these cases, no reasonable island is found when extremizing the generalized entropy, suggesting that the islands mechanism may not apply universally[17]. This indicates that while islands provide a powerful tool for understanding information recovery in many holographic scenarios, additional physics may be needed in some cases.

## Entanglement Wedge Reconstruction and Information Access

The concept of entanglement wedge reconstruction connects the holographic duality to quantum information theory and provides a mechanism for understanding how information becomes accessible at late times[35]. The entanglement wedge of a boundary subregion A is defined as the bulk region that can be reconstructed from boundary data in region A and its "causal complement" through entanglement wedge reconstruction[35].

In the evaporating black hole scenario, the crucial point is that after the Page time, the entanglement wedge of the early radiation extends across the event horizon and includes a portion of the black hole interior[35]. This means that information about what is happening inside the black hole becomes accessible to someone with access to the early Hawking radiation, even though that information cannot be reconstructed from the early radiation alone. Rather, one must combine the early radiation with information about the black hole's initial state to reconstruct the interior[35].

The role of initial state dependence in entanglement wedge reconstruction is subtle but important[35]. Before the Page time, the reconstruction of any interior operator from the radiation depends on knowing the black hole's initial state. However, as the black hole continues to evaporate beyond the Page time, reconstructions become possible that work for a large class of initial states. Eventually, a single state-independent interior reconstruction exists for any sufficiently small code subspace of black hole microstates[35]. This demonstrates how information gradually becomes accessible as the black hole evaporates, consistent with the Page curve.

## Quantum Entanglement Structure of Hawking Modes

While Hawking radiation appears thermal to a naive observer measuring individual radiation modes, recent analyses reveal that the modes must be highly correlated to preserve unitarity[43][44]. The fundamental question is: what is the minimum amount of quantum entanglement required between Hawking modes to preserve unitarity?

Remarkably, detailed calculations of the quantum entanglement between Hawking modes show that the required entanglement is surprisingly small[43]. Using the theory of constrained random symplectic transformations, researchers found that if the total state of Hawking radiation is to be pure and Gaussian with the observed marginal thermal distributions of individual modes, the entanglement between different modes can be much weaker than one might naively expect[43]. The analysis reveals that high-frequency modes (much larger than the Hawking temperature) are typically not populated early in the evaporation and thus drop out of consideration. Among the modes that are populated, highly populated early-time modes show only weak entanglement with other modes, while more sparsely populated modes might be correlated but are unlikely to be significantly entangled[43].

This result suggests that restoring unitarity after complete black hole evaporation does not require the radiation to be drastically different from a thermal spectrum. Instead, only subtle correlations between modes are needed to preserve quantum information. The apparent thermality of the spectrum is maintained at leading order, with small non-thermal deviations encoding the necessary information[43].

Further understanding of these correlations comes from studying specific properties of the radiation. The velocity correlation function provides a tool for probing the quantum structure of Hawking radiation even in exotic scenarios such as mass-superposed black holes[44]. The correlation function method can pinpoint the location where Hawking radiation originates, revealing it to come from a diffuse quantum atmosphere rather than being sharply produced at the classical horizon[44].

## Role of Quantum Corrections and Modified Dispersion Relations

Beyond the semiclassical approximation, quantum gravity effects modify the Hawking radiation spectrum in systematic ways. These corrections become increasingly important as the black hole approaches the Planck scale, but they provide crucial insights into how information is preserved. Modified dispersion relations that account for Planck-scale physics naturally produce non-thermal effects in the spectrum[15][18].

In models with modified dispersion relations that become superluminal at large wave numbers, the Hawking radiation spectrum exhibits clear deviations from thermality[18]. The WKB approximation used in standard Hawking derivations breaks down near the horizon in such models, but this breakdown itself is not the cause of radiation; rather, the tearing apart of wave packets into inside and outside the horizon represents the fundamental source of particle creation[18].

Quantum gravity corrections via the generalized uncertainty principle provide a framework for understanding these modifications. The GUP modifies the uncertainty relation to include a minimum length scale of order the Planck length, which in turn modifies the tunneling probabilities in the quantum tunneling picture of Hawking radiation[47]. Through the Parikh-Wilczek method applied to black holes with GUP corrections, the tunneling probability including quantum gravity effects generates correlations between emitted particles[47]. The inclusion of quantum gravity effects such as GUP merged with noncommutativity effects generates correlations between different modes, meaning that information flows out of the black hole as non-thermal GUP correlations within the Hawking radiation[47].

## Holographic Thermodynamics and Black Hole Phase Transitions

Understanding black hole thermodynamics through holographic methods provides another window into how holographic constraints shape the Hawking radiation spectrum. In AdS spacetime, black holes exhibit rich thermodynamic behavior including phase transitions[2][7][45]. The Hawking-Page phase transition, occurring when the black hole temperature reaches a critical value, represents a transition between a thermal AdS state and a black hole state in AdS[2][45]. In the dual CFT, this corresponds to a deconfinement phase transition in the gauge theory[2][45].

At the classical level, the thermodynamics of AdS black holes show characteristic phase structures with first-order phase transitions[45]. However, when quantum corrections are included, these structures may be modified. Recent calculations show that quantum corrections to the thermodynamics of black holes in AdS spacetime include subleading corrections equal to half the Hawking temperature[45]. This universal feature appears to be an intrinsic property of black holes in asymptotically AdS spacetime[45].

The holographic interpretation of these quantum corrections involves the boundary CFT. The central charge of the boundary theory acts as a key holographic parameter governing the nature of gravity and bulk geometry within the AdS/CFT framework[7]. For small central charge, where quantum gravity effects in the bulk become significant, the thermodynamic behavior differs from the classical large-central-charge limit[7]. The heat capacity of black holes depends on the central charge, with small central charge corresponding to stable black holes with always-positive heat capacity, while large central charge allows phase transitions[7].

## Constraints from Cosmological and Astrophysical Observations

While Hawking radiation from stellar-mass black holes is too weak to observe directly (stellar black holes are colder than the cosmic microwave background at 2.7 K[39]), primordial black holes formed in the early universe would experience significant Hawking radiation and evaporation[3][6]. The constraints from observational data on primordial black holes provide indirect evidence about the nature of Hawking radiation.

Primordial black holes of asteroid mass (around $10^{17}$ to $10^{23}$ grams) represent candidates for dark matter[3][6]. The Hawking radiation constraints on such black holes come from their effects on early universe physics, including implications for big bang nucleosynthesis, the cosmic microwave background, and the production of high-energy cosmic rays[3]. The detailed calculation of Hawking radiation spectra for primordial black holes, including Kerr rotation effects, shows that the spectrum depends sensitively on the black hole's mass and spin[6].

For primordial black holes with significant spin, the Hawking radiation is enhanced, leading to stronger observational constraints[6]. The reduced temperature of spinning black holes affects the energy distribution of emitted particles, creating frequency peaks in the spectrum that differ from the non-rotating Schwarzschild case[6]. These frequency-dependent features in the spectrum represent deviations from perfect thermality that might be testable through detailed analysis of the radiation signatures if primordial black holes are detected[6].

## Soft Hair and Asymptotic Structure

Recent research has revealed that black hole horizons can carry "soft hair" - gentle, long-range structures that do not significantly modify the classical black hole solution but encode information about how the black hole formed[27][30]. Supertranslations and superrotations of the spacetime geometry provide conserved charges that can be associated with soft hair configurations[27][30].

The study of Hawking radiation from soft-hairy black holes reveals subtle but important modifications to the spectrum. For soft-hairy Schwarzschild black holes, the Hawking radiation is insensitive to the static soft hair configuration; however, for dynamical black holes with soft hair that evolves during the evaporation process (such as supertranslated Vaidya black holes), the Hawking radiation spectrum depends on the soft hair configuration[27]. The spectrum develops an angle-dependent Hawking temperature, with the dependence encoded in the soft charges[27].

The connection between soft hair and information preservation remains an active area of investigation. The soft modes cannot affect the black hole scattering matrix due to Weinberg soft theorems at classical level, yet they must have non-trivial quantum effects since soft hair is generated by supertranslations that involve angular-dependent shifts of time[27]. The modified spectrum from soft-hairy black holes suggests that information about the collapse process that created the black hole may be encoded in the soft hair and thus accessible through detailed analysis of the Hawking radiation[27].

Dressed coordinates provide a framework for understanding soft hair and its effects on quantum states[30]. By introducing coordinate transformations that make soft hair degrees of freedom apparently disappear from the metric, one can analyze quantum states of Hawking radiation while keeping track of soft modes separately[30]. Results such as angle-dependent Hawking temperature and soft graviton theorems can be readily reproduced using dressed coordinates, providing evidence that soft hair carries information crucial for understanding information preservation[30].

## Challenges and Open Questions

Despite significant progress, fundamental questions remain about the precise mechanism of information recovery and the nature of the non-thermal spectrum. The precise relationship between the non-thermal correlations in Hawking radiation and specific properties of the black hole's initial state remains unclear. While we know that unitarity requires non-thermal correlations, understanding exactly how the spectrum encodes information about which initial state the black hole started in requires more detailed analysis.

The firewall paradox, while not universally accepted as a definitive challenge to the information preservation scenario, highlights tensions that may not be fully resolved. The apparent incompatibility between smooth horizons (as predicted by general relativity and locality principles) and the need for information to be accessible in the radiation at late times motivates continued investigation into the structure of spacetime near black hole horizons[49][52].

The generality of the island and quantum extremal surface mechanism remains an open question. While islands successfully reproduce the Page curve in many scenarios, some classes of black holes (such as Liouville black holes) do not appear to fit the standard island formula framework[17]. Understanding when and why the island mechanism applies represents an important frontier in quantum gravity research.

The trans-Planckian problem in Hawking's original derivation raises questions about the validity of semiclassical calculations when traced back to extreme distances. While various alternative formulations of Hawking radiation avoid this issue, the precise connection between trans-Planckian physics and the emergence of information-preserving correlations remains subtle[39].

## Implications for Quantum Gravity and Black Hole Microstructure

The non-thermal spectrum of Hawking radiation and its connection to holographic constraints has profound implications for understanding the microscopic structure of black holes. String theory provides a framework for this investigation by accounting for black hole entropy through counting of microscopic string and brane states[21][24]. The Bekenstein-Hawking entropy formula \(S_{BH} = \frac{A}{4}\) in Planck units has been derived from first principles in string theory by counting degeneracies of BPS states[21][24].

The information about how many microscopic states a black hole can access is encoded not in the bulk gravity description, where semiclassically the horizon appears empty, but in the subtle correlations and non-thermal structure of the Hawking radiation. The radiation spectrum at the detailed level reflects the density of states available to the black hole, modulated by greybody factors that depend on the black hole geometry. The complete spectrum, when analyzed in detail, should in principle allow reconstruction of information about the microstates from which the black hole evaporated.

Black hole microstate geometries represent explicit constructions in string theory that have internal structure where black hole singularities would appear in general relativity[42][51][54]. These horizonless objects with black hole mass and charges demonstrate that the information loss paradox may be avoided without necessarily invoking singular horizons at all. The Hawking radiation from microstate geometries would differ from that of classical black holes at the quantum level, possibly showing signatures that could distinguish between different proposed resolutions of the information paradox[42].

The development of precision holography, which uses methods like entanglement wedge reconstruction and quantum extremal surfaces to compare holographic theories with traditional field theory calculations, has revealed remarkable agreements between bulk gravitational predictions and boundary CFT results[42]. These successes suggest that the holographic framework is capturing something fundamental about quantum gravity and information preservation.

## Recent Developments and Future Directions

Recent progress has focused on refining calculations of how the Page curve emerges from quantum extremal surfaces and understanding the transition of information accessibility at the Page time. The study of entanglement in excited states, particularly coherent states corresponding to specific bulk geometries, provides insights into how information encoded in different bulk regions manifests in the boundary CFT[36].

The connection between holography and quantum chaos continues to develop, with implications for understanding information scrambling and recovery[56][59]. Black holes are known to be extremely efficient scramblers of information, mixing input information thoroughly with themselves on timescales comparable to traversal of the black hole size[49]. Recent work shows that the onset of fast scrambling and the development of quantum chaos in boundary systems may be directly connected to the emergence of horizons in the bulk through AdS/CFT[59].

Connections between the weak gravity conjecture and holographic consistency conditions have revealed how swampland constraints on quantum gravity theories emerge naturally from holographic principles[19][58]. These results suggest that unitarity, locality, and information preservation in holographic theories automatically enforce bounds on the spectrum of particles and operators that can exist, providing a holographic explanation for why certain classes of theories that naively seem consistent actually lie in the "swampland" of theories without consistent quantum gravity completions[19][58].

Future research directions include developing better understanding of the detailed structure of the non-thermal spectrum across the full energy range from low energies to Planck scale physics, understanding how quantum gravity effects near the singularity modify the spectrum compared to semiclassical predictions, and exploring whether the island mechanism generalizes to time-dependent backgrounds and cosmological scenarios. The study of analog and laboratory systems that exhibit Hawking-like radiation provides complementary approaches to testing predictions about the spectrum without waiting for astronomical observations[38].

## Conclusion

The non-thermal spectrum of Hawking radiation emerges naturally from the requirement of holographic duality, particularly through the AdS/CFT correspondence, that black hole evaporation must preserve quantum information and maintain unitarity. While Hawking's semiclassical calculation predicts a thermal spectrum arising from the geometric optics approximation, a more careful treatment that includes quantum corrections reveals that non-thermal correlations between different modes of radiation are necessary for information preservation. These correlations are small for macroscopic black holes but become increasingly significant as the black hole approaches the Planck scale.

The holographic framework provides concrete mechanisms through which information recovery can occur. The Page curve, which quantifies how the entanglement entropy of radiation evolves from increasing to decreasing entropy, emerges from phase transitions in the location of quantum extremal surfaces. After the Page time, part of the black hole interior becomes encoded in the early radiation through the entanglement wedge, making information about the interior gradually accessible through careful analysis of the radiation. Entanglement wedge reconstruction provides the precise mechanism through which interior operators can be reconstructed from boundary data combined with information about initial conditions.

The field of black hole thermodynamics, Hawking radiation, and information preservation has achieved remarkable maturity through the integration of string theory, quantum information theory, and gravitational physics. The holographic principle, far from being merely an abstract mathematical conjecture, provides a powerful framework that constrains the structure of quantum gravity and predicts specific features of black hole evaporation that are testable in principle through careful analysis of the radiation spectrum. The shift from thermal to non-thermal spectrum represents not a minor modification but a fundamental resolution of the information paradox, demonstrating how quantum mechanics and general relativity can be successfully merged in the framework of holographic duality. Future developments will likely reveal even deeper connections between black hole physics, quantum information, and the emergence of spacetime geometry from quantum entanglement, potentially revolutionizing our understanding of the fundamental nature of reality.

## Annotations
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[1511.04806] Nonthermal Spectrum of Hawking Radiation - arXiv', 'url': 'https://arxiv.org/abs/1511.04806'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Holography and AdS/CFT correspondence', 'url': 'http://utf.mff.cuni.cz/vyuka/NTMF082/ADSCFT_BriefSummary.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Primordial black hole constraints with Hawking radiation -- a review', 'url': 'https://arxiv.org/abs/2206.02672'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Nonthermal Spectrum of Hawking Radiation - Inspire HEP', 'url': 'https://inspirehep.net/literature/1404861'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Introduction to Holographic Duality - UCSB Physics', 'url': 'https://web.physics.ucsb.edu/~davidgrabovsky/files-research/Holography.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Primordial black holes and Hawking radiation', 'url': 'https://www.cpt.univ-mrs.fr/~cosmo/SW_2022/DOCUMENTS/SLIDES/Arbey.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Holographic Central Charge Effects on Black Hole Thermodynamics ...', 'url': 'https://arxiv.org/html/2512.24808v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Black hole information paradox - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Black_hole_information_paradox'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Resolving a paradox: AdS/CFT and black hole information loss', 'url': 'https://www.imperial.ac.uk/media/imperial-college/research-centres-and-groups/theoretical-physics/msc/dissertations/2022/Andrew-King-Dissertation.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Holographic principle - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Holographic_principle'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Page curves in holographic superconductors | Phys. Rev. D', 'url': 'https://link.aps.org/doi/10.1103/PhysRevD.110.046003'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[1609.04036] The Black Hole Information Problem - arXiv', 'url': 'https://arxiv.org/abs/1609.04036'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Greybody factors at large imaginary frequencies - arXiv', 'url': 'https://arxiv.org/pdf/hep-th/0304080.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[2407.20921] Universal structure of islands in evaporating black holes', 'url': 'https://arxiv.org/abs/2407.20921'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Black Hole Radiation with Modified Dispersion Relation in ... - arXiv', 'url': 'https://arxiv.org/abs/1505.03045'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Greybody Factors - Homepages of UvA/FNWI staff', 'url': 'https://staff.fnwi.uva.nl/j.deboer/education/projects/projects/escobedo.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Island may not save the information paradox of Liouville black holes', 'url': 'https://link.aps.org/doi/10.1103/PhysRevD.104.106015'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Hawking radiation with dispersion versus breakdown of the WKB ...', 'url': 'https://link.aps.org/doi/10.1103/PhysRevD.88.124009'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Constraints on Quantum Gravity from Holographic Principles - arXiv', 'url': 'https://arxiv.org/html/2512.14389v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Entanglement Entropy in a Holographic Moving Mirror and the Page ...', 'url': 'https://link.aps.org/doi/10.1103/PhysRevLett.126.061604'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Microscopic Origin of the Bekenstein-Hawking Entropy - hep-th - arXiv', 'url': 'https://arxiv.org/abs/hep-th/9601029'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Black hole thermodynamics, quantum puzzles, and the holographic ...', 'url': 'https://rojefferson.blog/2020/03/07/black-hole-thermodynamics-quantum-puzzles-and-the-holographic-principle/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Odd entanglement entropy in boundary conformal field theories and ...', 'url': 'https://arxiv.org/pdf/2310.11242.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Microscopic origin of the Bekenstein-Hawking entropy - Inspire HEP', 'url': 'https://inspirehep.net/literature/415163'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Quantum-Corrected Hawking Radiation from Near-Extremal Kerr ...', 'url': 'https://arxiv.org/html/2501.08252v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] CFT duals of Kerr-Taub-NUT and beyond. - arXiv', 'url': 'https://arxiv.org/pdf/2205.09146.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Soft Hair of Dynamical Black Hole and Hawking Radiation - arXiv', 'url': 'https://arxiv.org/pdf/1801.03658.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Near-extremal black holes - Inspire HEP', 'url': 'https://inspirehep.net/literature/1085171'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Thermodynamics in Black-hole/CFT Correspondence - Inspire HEP', 'url': 'https://inspirehep.net/literature/1233690'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Soft hair, dressed coordinates, and information loss paradox', 'url': 'https://link.aps.org/doi/10.1103/PhysRevD.108.044034'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Holographic proof of the quantum null energy condition - NASA ADS', 'url': 'https://ui.adsabs.harvard.edu/abs/2016PhRvD..94b4026K/abstract'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Large breakdowns of entanglement wedge reconstruction', 'url': 'https://link.aps.org/doi/10.1103/PhysRevD.100.126006'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Modular Hamiltonian of holographic time band states - arXiv', 'url': 'https://arxiv.org/pdf/2504.13739.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Holographic proof of the averaged null energy condition | Phys. Rev. D', 'url': 'https://link.aps.org/doi/10.1103/PhysRevD.90.106003'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Entanglement Wedge Reconstruction and the Information Paradox', 'url': 'https://arxiv.org/abs/1905.08255'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Modular Hamiltonian for holographic excited states | Phys. Rev. D', 'url': 'https://link.aps.org/doi/10.1103/PhysRevD.102.026021'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Quantum Gravity Corrections to Hawking Radiation via GUP - arXiv', 'url': 'https://arxiv.org/abs/2407.19268'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Low-frequency analogue Hawking radiation: The Korteweg', 'url': 'https://link.aps.org/doi/10.1103/PhysRevD.97.025005'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Hawking radiation - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Hawking_radiation'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Quantum-corrected thermodynamics and plasma lensing of MOG ...', 'url': 'https://royalsocietypublishing.org/rspa/article/481/2320/20250251/234327/Quantum-corrected-thermodynamics-and-plasma'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] arXiv:hep-th/0604044v2 11 Sep 2006', 'url': 'https://arxiv.org/pdf/hep-th/0604044.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Snowmass White Paper: Micro- and Macro-Structure of Black Holes', 'url': 'https://www.slac.stanford.edu/econf/C210711/papers/2203.04981.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Random Pure Gaussian States and Hawking Radiation - APS Journals', 'url': 'https://link.aps.org/doi/10.1103/PhysRevLett.133.060202'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Quantum correlation and origin of Hawking radiation for mass ...', 'url': 'https://link.aps.org/doi/10.1103/PhysRevD.111.085007'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Thermodynamics of the Kerr-AdS black hole from an ensemble ...', 'url': 'https://arxiv.org/html/2410.23006v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Hawking Radiation: A Comparison of Pure-state and Thermal ... - arXiv', 'url': 'https://arxiv.org/pdf/1703.05373.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] GENERALIZED UNCERTAINTY PRINCIPLE IN HAWKING ...', 'url': 'https://s3.cern.ch/inspire-prod-files-3/313f4ab8e8211ea70c7da6da9f8452fc'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Black hole temperature in Euclidean formalism', 'url': 'https://www.ggi.infn.it/laces/LACES22/LACES_exercises.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Black holes, fast scrambling and the breakdown of the equivalence ...', 'url': 'https://arxiv.org/html/2206.02053v2'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Quantum entanglement of Hawking-partner modes in expanding ...', 'url': 'https://link.aps.org/doi/10.1103/szzj-pq9z'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Exact BPS black hole microstate counting from holographic ... - arXiv', 'url': 'https://arxiv.org/pdf/2506.22109.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Black hole information paradox - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Black_hole_information_paradox'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] arXiv:1611.02647v2 [gr-qc] 28 Feb 2017', 'url': 'https://arxiv.org/pdf/1611.02647.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Black hole microstates geometries and their holographic duals', 'url': 'https://agenda.infn.it/event/41745/attachments/119884/173977/S_Rawash.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Black holes, heavy states, phase shift and anomalous dimensions', 'url': 'https://scipost.org/SciPostPhys.6.6.065/pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Quantum Chaos Theory → Term', 'url': 'https://energy.sustainability-directory.com/term/quantum-chaos-theory/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Virasoro Hair and Entropy for Axisymmetric Killing Horizons', 'url': 'https://link.aps.org/doi/10.1103/PhysRevLett.125.241302'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Convexity of charged operators in CFTs and the weak gravity ...', 'url': 'https://link.aps.org/doi/10.1103/PhysRevD.104.126005'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Binary-coupling sparse Sachdev-Ye-Kitaev model', 'url': 'https://link.aps.org/doi/10.1103/PhysRevB.107.L081103'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Near-Horizon Conformal Symmetry and Black Hole Entropy in Any ...', 'url': 'https://arxiv.org/abs/hep-th/0402113'}}

## Sources
https://arxiv.org/abs/1511.04806
http://utf.mff.cuni.cz/vyuka/NTMF082/ADSCFT_BriefSummary.pdf
https://arxiv.org/abs/2206.02672
https://inspirehep.net/literature/1404861
https://web.physics.ucsb.edu/~davidgrabovsky/files-research/Holography.pdf
https://www.cpt.univ-mrs.fr/~cosmo/SW_2022/DOCUMENTS/SLIDES/Arbey.pdf
https://arxiv.org/html/2512.24808v1
https://en.wikipedia.org/wiki/Black_hole_information_paradox
https://www.imperial.ac.uk/media/imperial-college/research-centres-and-groups/theoretical-physics/msc/dissertations/2022/Andrew-King-Dissertation.pdf
https://en.wikipedia.org/wiki/Holographic_principle
https://link.aps.org/doi/10.1103/PhysRevD.110.046003
https://arxiv.org/abs/1609.04036
https://arxiv.org/pdf/hep-th/0304080.pdf
https://arxiv.org/abs/2407.20921
https://arxiv.org/abs/1505.03045
https://staff.fnwi.uva.nl/j.deboer/education/projects/projects/escobedo.pdf
https://link.aps.org/doi/10.1103/PhysRevD.104.106015
https://link.aps.org/doi/10.1103/PhysRevD.88.124009
https://arxiv.org/html/2512.14389v1
https://link.aps.org/doi/10.1103/PhysRevLett.126.061604
https://arxiv.org/abs/hep-th/9601029
https://rojefferson.blog/2020/03/07/black-hole-thermodynamics-quantum-puzzles-and-the-holographic-principle/
https://arxiv.org/pdf/2310.11242.pdf
https://inspirehep.net/literature/415163
https://arxiv.org/html/2501.08252v1
https://arxiv.org/pdf/2205.09146.pdf
https://arxiv.org/pdf/1801.03658.pdf
https://inspirehep.net/literature/1085171
https://inspirehep.net/literature/1233690
https://link.aps.org/doi/10.1103/PhysRevD.108.044034
https://ui.adsabs.harvard.edu/abs/2016PhRvD..94b4026K/abstract
https://link.aps.org/doi/10.1103/PhysRevD.100.126006
https://arxiv.org/pdf/2504.13739.pdf
https://link.aps.org/doi/10.1103/PhysRevD.90.106003
https://arxiv.org/abs/1905.08255
https://link.aps.org/doi/10.1103/PhysRevD.102.026021
https://arxiv.org/abs/2407.19268
https://link.aps.org/doi/10.1103/PhysRevD.97.025005
https://en.wikipedia.org/wiki/Hawking_radiation
https://royalsocietypublishing.org/rspa/article/481/2320/20250251/234327/Quantum-corrected-thermodynamics-and-plasma
https://arxiv.org/pdf/hep-th/0604044.pdf
https://www.slac.stanford.edu/econf/C210711/papers/2203.04981.pdf
https://link.aps.org/doi/10.1103/PhysRevLett.133.060202
https://link.aps.org/doi/10.1103/PhysRevD.111.085007
https://arxiv.org/html/2410.23006v1
https://arxiv.org/pdf/1703.05373.pdf
https://s3.cern.ch/inspire-prod-files-3/313f4ab8e8211ea70c7da6da9f8452fc
https://www.ggi.infn.it/laces/LACES22/LACES_exercises.pdf
https://arxiv.org/html/2206.02053v2
https://link.aps.org/doi/10.1103/szzj-pq9z
https://arxiv.org/pdf/2506.22109.pdf
https://en.wikipedia.org/wiki/Black_hole_information_paradox
https://arxiv.org/pdf/1611.02647.pdf
https://agenda.infn.it/event/41745/attachments/119884/173977/S_Rawash.pdf
https://scipost.org/SciPostPhys.6.6.065/pdf
https://energy.sustainability-directory.com/term/quantum-chaos-theory/
https://link.aps.org/doi/10.1103/PhysRevLett.125.241302
https://link.aps.org/doi/10.1103/PhysRevD.104.126005
https://link.aps.org/doi/10.1103/PhysRevB.107.L081103
https://arxiv.org/abs/hep-th/0402113