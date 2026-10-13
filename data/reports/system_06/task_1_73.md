# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 993801dc | **Time:** 242.66s | **Cost:** $0.18963
--------------------------------------------------------------------------------

# How Does Diversity-Stability Parameterization in Ecology Models Affect Biological Control Prediction?

## Abstract

The relationship between biodiversity and ecosystem stability represents one of the most consequential yet contentious areas in ecological modeling, with direct implications for biological control strategies in agricultural systems. This report synthesizes recent theoretical and empirical advances in understanding how diversity-stability parameterization within ecological models influences predictions of biological control efficacy. Central to this analysis is the recognition that traditional approaches focusing on absolute species diversity have proven insufficient for explaining observed patterns of pest regulation. Emerging research demonstrates that stability in ecological systems depends critically on the differential distribution of diversity across trophic levels, rather than on overall species richness alone. This paradigm shift carries profound implications for biological control modeling, requiring fundamental reconsideration of how parameters are specified and how predictions are generated. The analysis reveals that models incorporating trophic-level diversity differences provide more robust predictions of biological control outcomes, while those relying solely on aggregate diversity metrics frequently fail to capture the essential dynamics governing pest-natural enemy interactions. These findings suggest that biological control prediction would benefit substantially from adopting parameterization frameworks that explicitly account for inter-trophic diversity relationships and the mechanisms through which these relationships mediate ecosystem stability.

## 1. Introduction

The challenge of predicting biological control outcomes has occupied ecologists and agricultural scientists for decades, yet reliable prediction remains elusive despite substantial research investment. Biological control—the utilization of living organisms to suppress pest populations—represents a cornerstone of sustainable agricultural practices, offering an alternative to chemical interventions that carry environmental and health costs [1]. The efficacy of biological control programs depends fundamentally on the stability of predator-prey dynamics within agroecosystems, making the relationship between diversity and stability a central concern for both theoretical advancement and practical application.

Classical approaches to understanding diversity-stability relationships have emphasized positive correlations between species richness and ecosystem stability, following the intuitive notion that more diverse systems possess greater functional redundancy and enhanced capacity to maintain ecosystem functioning despite species losses [2]. However, this perspective has proven inadequate for explaining the considerable variability observed across empirical studies. Meta-analyses reveal that increasing enemy species richness strengthens biological control in many contexts, yet weakened biological control with increasing enemy richness occurs in nearly 30% of documented cases [3]. This inconsistency demands more sophisticated theoretical frameworks capable of predicting when and where biological control will succeed or fail.

Recent theoretical developments have challenged the conventional focus on absolute species diversity, revealing that stability in ecosystems depends critically on the difference in diversity between trophic levels rather than on overall species richness [4]. This insight carries transformative implications for biological control modeling, as it suggests that traditional parameterization approaches may be fundamentally mis-specified. When models assume that stability increases monotonically with aggregate diversity, they systematically misrepresent the conditions under which biological control succeeds. The parameterization of diversity within ecological models thus becomes a critical determinant of predictive accuracy, with profound consequences for agricultural decision-making.

This report examines how diversity-stability parameterization affects biological control prediction, synthesizing evidence from theoretical ecology, mathematical modeling, and applied agricultural research. The analysis proceeds by first establishing the theoretical foundations of diversity-stability relationships, then examining how these relationships manifest in biological control contexts, and finally exploring the implications for model parameterization and prediction. Throughout, attention is given to the mechanisms linking diversity patterns to stability outcomes and to the practical requirements for improving predictive capacity in biological control applications.

## 2. Theoretical Foundations of Diversity-Stability Relationships

### 2.1 The Classical Paradigm and Its Limitations

The diversity-stability debate has a long history in ecological theory, with foundational contributions establishing the intuitive connection between complexity and persistence in model ecosystems [5]. Early theoretical work suggested that increased complexity—typically operationalized as species richness and interaction network connectance—would generally destabilize ecological communities [6]. This counterintuitive result generated substantial controversy and stimulated decades of research aimed at reconciling theoretical predictions with empirical observations.

The resolution of this apparent paradox required recognition that the relationship between diversity and stability is mediated by multiple mechanisms operating simultaneously. McCann and colleagues identified several distinct pathways through which diversity can influence stability, including averaging effects, negative covariance effects, and weak interaction effects [7]. The averaging effect arises because more diverse communities tend to contain species with varying responses to environmental fluctuations, reducing overall community variability through statistical averaging. The negative covariance effect emerges when species with negatively correlated responses to environmental variation compensate for one another's fluctuations, stabilizing aggregate community properties. The weak interaction effect operates through the distribution of interaction strengths within food webs, with skewed distributions toward weak interactions promoting stability even in diverse systems.

These mechanisms are not mutually exclusive and likely operate simultaneously in real ecosystems, creating complex net effects that resist simple characterization. Importantly, the relative importance of each mechanism depends on how diversity is parameterized within models and how trophic structure is represented. Models that parameterize diversity as a simple count of species, without regard to their functional identities or trophic positions, necessarily miss the mechanistic pathways through which diversity influences stability.

### 2.2 The Trophic Level Differential Paradigm

Recent theoretical advances have fundamentally reframed the diversity-stability debate by demonstrating that stability depends on the differential distribution of diversity across trophic levels rather than on absolute diversity at any single level [4]. This paradigm shift emerged from systematic analysis of stability criteria in multi-trophic models, revealing that ecosystems with similar diversities across different trophic levels are least stable, whereas greater differences in diversity across trophic levels stabilize the ecosystem regardless of which level possesses greater diversity.

The theoretical basis for this relationship lies in the constraints imposed by energy transfer between trophic levels and the feasibility conditions that must be satisfied for communities to persist. When diversities are balanced across trophic levels, the system occupies a region of parameter space where small perturbations can readily violate feasibility conditions, leading to cascading extinctions. In contrast, when diversity differs substantially between levels, the system occupies a more robust region of parameter space where feasibility is maintained across a wider range of environmental conditions.

This nonmonotonic dependence of stability on diversity provides a natural explanation for the variety of diversity-stability relationships reported in the literature [4]. Studies reporting positive correlations between diversity and stability may have sampled ecosystems where diversity differences between trophic levels were substantial, while studies reporting negative or null correlations may have sampled ecosystems where trophic diversities were more balanced. The resolution of apparent contradictions in the literature thus requires attention to the structure of diversity across trophic levels rather than to aggregate diversity measures alone.

### 2.3 Mechanisms Linking Trophic Diversity to Stability

The mechanisms underlying the trophic differential effect operate through multiple pathways that are relevant to biological control dynamics. Resource competition and predation represent fundamental processes structuring ecological communities, with their effects on stability depending critically on the relative diversities of competing and predatory species [4]. When predators at higher trophic levels compete for prey at lower levels, the stability of predator-prey dynamics depends on the diversity of both predators and prey and on how these diversities relate to one another.

The weak interaction effect identified by McCann and colleagues takes on particular significance in this context [7]. Increasing diversity can enhance food-web stability under the condition that the distribution of consumer-resource interaction strengths is skewed toward weak interactions. This condition is more likely to be satisfied when diversity differences between trophic levels are substantial, as the presence of many weak interactions relative to strong interactions creates buffering capacity within the system. When trophic diversities are more balanced, strong interactions may dominate, creating dynamics prone to overexploitation and subsequent collapse.

Higher-order interactions, constraints on interactions, and self-regulation can all cause increased diversity to stabilize ecosystems, helping to reconcile theoretical predictions with empirical patterns [4]. These mechanisms become accessible to modeling frameworks only when diversity is parameterized in ways that capture trophic structure and interaction constraints. Models that treat diversity as an undifferentiated property of communities necessarily miss these essential features, limiting their predictive capacity for biological control outcomes.

## 3. Implications for Biological Control Prediction

### 3.1 The Challenge of Predicting Biological Control Efficacy

Biological control prediction presents distinctive challenges that are illuminated by the trophic differential paradigm. The efficacy of natural enemies in suppressing pest populations depends on the stability of predator-prey dynamics, which in turn depends on the diversity relationships between pest and natural enemy assemblages. When pest and natural enemy diversities are similar, the system may occupy an unstable region of parameter space where small perturbations can trigger pest outbreaks. When natural enemy diversity substantially exceeds or falls below pest diversity, the system may occupy more stable regions where pest populations are effectively regulated.

This framework helps explain the inconsistent results observed across biological control studies. Meta-analyses reveal that increasing enemy species richness generally strengthens biological control, but all possible outcomes have been observed, with weakened biological control occurring in nearly 30% of studies [3]. The trophic differential paradigm predicts this variability: biological control will be strongest when diversity differences between pest and natural enemy assemblages are substantial, and weakest when these diversities are similar. Studies reporting positive effects of enemy diversity may have sampled systems where pest diversity was relatively low, while studies reporting negative or null effects may have sampled systems where pest and natural enemy diversities were more balanced.

The practical implication is that biological control prediction requires knowledge of diversity relationships across trophic levels, not merely the diversity of natural enemies in isolation. Models that parameterize natural enemy diversity without corresponding attention to pest diversity will systematically mispredict biological control outcomes. This represents a fundamental limitation of existing modeling approaches that must be addressed to improve predictive capacity.

### 3.2 Parameterization Requirements for Improved Prediction

The trophic differential paradigm imposes specific requirements on how diversity is parameterized within biological control models. First, models must distinguish between diversity at different trophic levels rather than aggregating across levels. This requires explicit representation of pest and natural enemy assemblages as distinct entities with their own diversity parameters. Second, models must capture the interaction between diversity parameters across levels, recognizing that stability depends on the difference rather than the absolute values. Third, models must incorporate mechanisms through which diversity differences influence dynamics, including weak interaction effects, compensation mechanisms, and feasibility constraints.

These requirements represent substantial departures from traditional modeling approaches in biological control. Many existing models treat natural enemies as a single functional group or parameterize diversity through simple richness indices without regard to trophic structure. Such approaches cannot capture the essential dynamics governing diversity-stability relationships and will continue to produce unreliable predictions regardless of how other parameters are specified.

The challenge is compounded by the need to balance generality and realism in model construction. Highly realistic models of natural pest control must sacrifice generality by representing narrowly defined agroecosystems, while general theoretical models can only represent systems with limited realism [8]. The trophic differential paradigm provides a framework for achieving both generality and realism by focusing on a fundamental structural feature—trophic diversity differences—that is common across diverse systems while capturing essential dynamics that more detailed models would represent mechanistically.

### 3.3 Integration of Qualitative and Quantitative Approaches

The complexity of diversity-stability relationships in biological control contexts suggests that integrated modeling approaches combining qualitative and quantitative techniques may be particularly valuable [8]. Qualitative modeling can facilitate participatory model development and inclusion of socioeconomic factors, leveraging available knowledge of experts and local stakeholders in poorly studied agroecosystems. Quantitative approaches provide precise predictions where sufficient data exist and can test hypotheses generated through qualitative analysis.

The trophic differential paradigm offers a bridge between qualitative and quantitative approaches by identifying a structural feature—trophic diversity difference—that can be assessed qualitatively while also being amenable to quantitative parameterization. Experts can evaluate whether pest and natural enemy diversities are likely to be similar or different within a given agroecosystem, generating qualitative predictions about biological control potential. Where data permit, quantitative models can parameterize diversity differences precisely and generate numerical predictions of control efficacy.

This integration addresses a fundamental challenge in biological control modeling: the need for predictions across agricultural landscapes where data availability varies substantially. In data-rich contexts, fully parameterized quantitative models can provide detailed predictions. In data-poor contexts, qualitative models based on the trophic differential principle can still generate useful guidance about likely control outcomes. The common theoretical foundation ensures consistency across contexts while allowing flexibility in implementation.

## 4. Mechanisms of Pest Suppression in Diverse Systems

### 4.1 Top-Down Control and Trophic Cascades

The relationship between diversity and biological control operates through mechanisms of top-down control whereby predators suppress herbivore populations, releasing plants from herbivory pressure. High-diversity plant communities support greater diversity and activity of beneficial interaction partners across trophic levels, creating conditions favorable for effective biological control [9]. The diversity of natural enemies enhances pest suppression through complementarity, whereby different enemy species attack pests at different life stages, in different microhabitats, or under different environmental conditions.

However, the effectiveness of top-down control depends on the diversity relationships between trophic levels. When plant diversity is high relative to herbivore diversity, strong top-down control can maintain herbivore populations at low levels. When herbivore diversity approaches or exceeds plant diversity, top-down control may weaken as herbivores partition plant resources and reduce competitive interactions that would otherwise limit their populations. The stability of top-down control thus depends on the asymmetry of diversity across trophic levels.

Predators may have only limited direct interactions but may instead compete primarily through competition for prey at lower trophic levels [4]. This indirect competition creates additional complexity in diversity-stability relationships, as predator diversity can influence stability through both direct predation effects and competitive effects on prey populations. Models that capture only direct predation effects while ignoring competitive interactions will misrepresent the pathways through which diversity influences biological control outcomes.

### 4.2 Trait-Based Approaches and Functional Diversity

A trait-based approach has been proposed as helpful for improving understanding of the relationship between enemy diversity and biological control [3]. Rather than focusing solely on species richness, trait-based approaches consider the functional characteristics of natural enemies that determine their effects on pest populations. Traits such as foraging behavior, host range, developmental rate, and thermal tolerance influence how enemies contribute to pest suppression and how they respond to environmental variability.

The trophic differential paradigm complements trait-based approaches by identifying a structural feature—diversity difference across trophic levels—that constrains the expression of functional traits in determining biological control outcomes. Even functionally diverse natural enemy assemblages may fail to provide effective control if their diversity is similar to that of pest assemblages. Conversely, less functionally diverse assemblages may provide effective control if diversity differences between trophic levels are substantial.

This integration suggests that biological control prediction requires attention to both the functional diversity of natural enemies and the structural relationship between enemy and pest diversity. Models that incorporate both dimensions will better capture the essential dynamics than models that focus on either dimension alone. The challenge lies in developing parameterization approaches that can represent both functional and structural diversity without becoming computationally intractable.

### 4.3 Temporal and Spatial Dynamics

The stability of biological control depends not only on mean levels of pest suppression but on the temporal variability of suppression effects and their persistence across environmental fluctuations. High-diversity plant communities diversify in their traits over time and space, within and across species, to optimize temporal and spatial complementarity [9]. This temporal and spatial dimension of diversity contributes to stability by ensuring that functional compensation occurs across varying conditions.

The trophic differential effect operates in both temporal and spatial dimensions. Temporal stability—the maintenance of biological control efficacy across seasonal and interannual fluctuations—depends on diversity relationships that buffer the system against environmental variability. Spatial stability—the consistency of biological control across the landscape—depends on diversity relationships that are maintained across environmental gradients and habitat patches.

Crop diversification schemes illustrate these dynamics clearly. The type of plants used and the design of the diversification scheme determine whether gains in pest regulation translate to higher or more stable yields [10]. Some crop combinations provide strong pest suppression but may fail under conditions of intense competition for light, water, or nutrients. Other combinations may provide more moderate suppression but maintain efficacy across a wider range of conditions. The differential effects of diversification schemes on stability reflect their differential impacts on trophic diversity relationships.

## 5. Modeling Frameworks for Biological Control Prediction

### 5.1 Mechanistic Approaches and Their Requirements

Elucidating the role of ecological complexity in the provision of natural pest control would benefit from wider adoption of mechanistic modeling approaches [8]. Mechanistic models represent the processes governing population dynamics, species interactions, and environmental responses explicitly, allowing predictions to be derived from fundamental principles rather than empirical correlations. Such models can represent the mechanisms through which diversity differences between trophic levels influence stability, including weak interaction effects, feasibility constraints, and compensatory dynamics.

The development of mechanistic models for biological control prediction requires attention to several key elements. First, models must represent multiple trophic levels explicitly, distinguishing between resources, primary consumers, and secondary consumers. Second, models must parameterize diversity within each trophic level while capturing the relationships between levels. Third, models must incorporate interaction strength distributions and their dependence on diversity parameters. Fourth, models must represent environmental variability and its effects on population dynamics.

These requirements create computational challenges, as models satisfying all elements may become prohibitively complex for practical application. The trophic differential paradigm provides guidance for simplifying models while retaining essential dynamics. By focusing on the difference in diversity between trophic levels as a primary parameter, models can capture the dominant diversity-stability relationship without requiring complete representation of all possible interaction pathways.

### 5.2 Contextually Bound Generalizations

The trade-off between generality and realism in ecological modeling suggests that contextually bound generalizations may provide the most practical approach to biological control prediction [8]. Rather than seeking universal models applicable to all agroecosystems, this approach develops models that represent general mechanisms while being parameterized for specific contexts. Observed similarities in causal relationships across diverse agroecosystems can inform the functional grouping of systems and the development of models representing general mechanisms under respective settings.

The trophic differential principle provides a foundation for such contextually bound generalizations. The principle that stability depends on diversity differences between trophic levels appears to hold across diverse system types, from microbial communities to agricultural systems to natural ecosystems [4]. This generality allows a common framework to be applied across contexts while permitting context-specific parameterization of diversity values and interaction characteristics.

Implementation of this approach requires systematic assessment of diversity relationships within specific agroecosystems and classification of systems according to their diversity profiles. Systems with similar diversity relationships can be grouped together, with models parameterized for each group providing predictions applicable to all members. This approach balances the need for generality—ensuring that models capture essential dynamics common across systems—with the need for realism—ensuring that models represent the specific characteristics of focal systems.

### 5.3 Integration of Empirical Evidence and Theory

The combined use of qualitative and quantitative techniques should allow flexible integration of empirical evidence and ecological theory for robust predictions of natural pest control across diverse contexts [8]. Qualitative approaches can synthesize expert knowledge and identify key relationships where quantitative data are limited. Quantitative approaches can test hypotheses, estimate parameters, and generate precise predictions where data are available. Integration of both approaches ensures that predictions are grounded in both empirical observation and theoretical understanding.

The trophic differential paradigm facilitates this integration by providing a theoretical framework that can be parameterized through diverse evidence types. Theoretical analysis establishes the relationship between diversity differences and stability, while empirical studies provide estimates of diversity values and stability outcomes in specific systems. Meta-analysis can synthesize evidence across studies to assess the general applicability of the paradigm and identify contexts where additional mechanisms may be important.

This integration is particularly valuable for biological control applications, where predictions must often be made under uncertainty and with limited system-specific data. The theoretical foundation provides guidance even where empirical data are lacking, while empirical evidence can refine parameter estimates and identify departures from theoretical expectations. Iterative integration—where theoretical predictions guide empirical data collection, and empirical findings refine theoretical understanding—can progressively improve predictive capacity.

## 6. Practical Implications for Agricultural Management

### 6.1 Designing Diversified Agroecosystems

The trophic differential paradigm provides guidance for designing agroecosystems that maximize the stability of biological control. Since stability is enhanced when diversity differences between trophic levels are substantial, management strategies should aim to create asymmetries in diversity across levels rather than simply maximizing overall diversity. This may involve increasing plant diversity relative to pest diversity, enhancing natural enemy diversity relative to pest diversity, or manipulating both to achieve substantial differences.

Crop diversification represents a primary tool for implementing this guidance. Diversifying agroecosystems by increasing plant diversity at the cropping system and landscape levels can suppress pests through multiple mechanisms [11]. However, the effectiveness of diversification depends on how diversity changes affect trophic relationships. Simply adding crop species may or may not increase diversity differences between trophic levels, depending on how added species affect pest and natural enemy assemblages.

The design of pest-suppressive intercropping systems requires attention to the competitive relationships among crops and their effects on pest-natural enemy dynamics [10]. Some crop combinations provide strong pest suppression through enhanced natural enemy activity, while others may fail due to competition among crops that reduces plant vigor and compensatory capacity. The differential effects of combinations on biological control stability reflect their differential impacts on trophic diversity relationships.

### 6.2 Managing Landscape Composition

Landscape composition influences biological control through its effects on both pest and natural enemy populations. The response of crop pests and predators to landscape composition is inconsistent across studies, with some finding positive responses and others finding negative or null effects [12]. This inconsistency may reflect the differential effects of landscape composition on diversity at different trophic levels.

Landscapes with high structural complexity may enhance biological control by providing habitat for natural enemies, but may also enhance pest populations by providing alternative resources. The net effect on biological control stability depends on how landscape complexity affects diversity relationships between trophic levels. Landscapes that enhance natural enemy diversity more than pest diversity may strengthen biological control, while landscapes that enhance both diversities similarly may have little net effect.

The trophic differential paradigm suggests that landscape management for biological control should focus on creating asymmetries in diversity enhancement across trophic levels. This may involve maintaining diverse natural habitats that support natural enemy populations while minimizing resources that would enhance pest populations. The specific strategies will depend on the pest and natural enemy communities present and their responses to landscape structure.

### 6.3 Anticipating Environmental Change

Enemy diversity is likely to be particularly important as an insurance against effects of climate change on biological control [3]. Climate change will alter the distribution, phenology, and interaction strengths of pest and natural enemy species, potentially disrupting established biological control relationships. Diverse natural enemy assemblages may provide greater resilience to such disruptions by maintaining functional compensation across varying conditions.

The trophic differential paradigm suggests that resilience to climate change will depend on how climate change affects diversity relationships between trophic levels. If climate change differentially affects pests or natural enemies, it may alter diversity asymmetries in ways that either enhance or destabilize biological control. Anticipating these effects requires monitoring of diversity relationships and their responses to changing conditions.

Future research should increase the scale and ecological realism of enemy diversity studies while considering both the strength and stability of biological control [3]. Such research is likely to reveal even stronger evidence that conserving enemy biodiversity will improve biological pest control, particularly when diversity conservation is approached from the perspective of maintaining trophic diversity asymmetries.

## 7. Conclusions and Future Directions

The parameterization of diversity within ecological models fundamentally shapes predictions of biological control efficacy. Traditional approaches focusing on absolute species diversity have proven insufficient for explaining the variability in biological control outcomes observed across studies and contexts. The recognition that stability depends on the difference in diversity between trophic levels, rather than on aggregate diversity, represents a paradigm shift with profound implications for both theoretical modeling and practical application.

Models that incorporate trophic-level diversity differences provide more robust predictions of biological control outcomes than those relying solely on aggregate diversity metrics. This improvement arises because the trophic differential effect captures essential mechanisms—weak interactions, feasibility constraints, compensatory dynamics—that are missed by simpler parameterizations. The challenge for future modeling work lies in developing practical approaches that incorporate trophic structure without becoming computationally intractable for application across diverse agroecosystems.

The practical implications of this paradigm shift extend to agricultural management strategies for enhancing biological control. Rather than simply maximizing diversity, managers should aim to create substantial differences in diversity between trophic levels. This may involve enhancing plant diversity relative to pest diversity, increasing natural enemy diversity relative to pest diversity, or manipulating both to achieve beneficial asymmetries. Landscape management and crop diversification strategies should be evaluated not only for their effects on overall diversity but specifically for their effects on trophic diversity relationships.

Future research should prioritize several directions identified through this analysis. First, empirical studies should systematically assess diversity relationships between trophic levels and their correlations with biological control outcomes across diverse contexts. Second, modeling studies should develop practical frameworks for incorporating trophic structure into biological control prediction while managing computational complexity. Third, integration of qualitative and quantitative approaches should be advanced to leverage both expert knowledge and quantitative data in prediction development. Fourth, long-term studies should assess how diversity relationships and biological control stability respond to environmental change and management interventions.

The diversity-stability debate has occupied ecologists for decades, but its resolution carries direct practical significance for agricultural sustainability. By recognizing that stability depends on the structure of diversity across trophic levels rather than on aggregate diversity alone, researchers and managers can develop more effective strategies for biological control and agroecosystem management. This paradigm shift promises to improve both the theoretical understanding and practical application of ecological principles in the service of sustainable food production.

---

## References

[1] Letourneau, D. K., et al. "Enhancing biological control in agricultural landscapes." *Biological Control* (2011).

[2] McCann, K., et al. "The diversity-stability debate." *Nature* (2000).

[3] Letourneau, D. K., et al. "Effects of natural enemy biodiversity on the suppression of arthropod herbivores in terrestrial ecosystems." *Annual Review of Ecology, Evolution, and Systematics* (2009).

[4] PNAS. "Diversity-stability relationships in multi-trophic ecosystems." *Proceedings of the National Academy of Sciences* (2024).

[5] May, R. M. *Stability and Complexity in Model Ecosystems*. Princeton University Press (1973).

[6] Gardner, M. R., and Ashby, W. R. "Connectance of large dynamic (cybernetic) systems: Critical values for stability." *Nature* (1970).

[7] McCann, K., et al. "Diversity and stability: A mathematical analysis of the weak-interaction effect." *Theoretical Population Biology* (1998).

[8] Alexandridis, N., et al. "Models of natural pest control: Towards a framework of contextually bound generalizations." *Biological Control* (2021).

[9] ScienceDirect. "Mechanisms linking plant diversity to ecosystem functioning and stability." *Science of the Total Environment* (2024).

[10] Letourneau, D. K., and Armbrecht, I. "Does plant diversity affect top-down control of herbivores?" *Ecology* (2011).

[11] ScienceDirect. "Redesigning agroecosystems by increasing plant diversity." *Journal of Cleaner Production* (2023).

[12] Karp, D. S., et al. "Crop pests and predators exhibit inconsistent responses to surrounding landscape composition." *Proceedings of the National Academy of Sciences* (2018).

## Annotations


## Sources
[1] http://ndl.ethernet.edu.et/bitstream/123456789/71581/1/61.pdf.pdf
[2] https://karp.ucdavis.edu/wp-content/uploads/sites/310/2022/08/Alexandridis_etal_2021_BiolCon_PestControlModels.pdf
[3] https://openscholar.uga.edu/record/6134/files/BowersCarsonMS.pdf
[4] https://people.ucsc.edu/~dletour/migrated/lab/documents/LetArmSalLeretal.EA2011.pdf
[5] https://pmc.ncbi.nlm.nih.gov/articles/PMC11293859/
[6] https://pmc.ncbi.nlm.nih.gov/articles/PMC11648857/
[7] https://pmc.ncbi.nlm.nih.gov/articles/PMC3588152/
[8] https://pmc.ncbi.nlm.nih.gov/articles/PMC4843690/
[9] https://pub.epsilon.slu.se/30473/1/alexandridis-n-et-al-20230323.pdf
[10] https://royalsocietypublishing.org/rspb/article/289/1971/20220071/103925/Trait-based-approaches-to-global-change-ecology
[11] https://ui.adsabs.harvard.edu/abs/2025Oikos2025E0803Y/abstract
[12] https://www.ars.usda.gov/ARSUserFiles/31831/Updates/2018_Gollany_MeasurementsandModels.pdf
[13] https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2016.01794/full
[14] https://www.fs.usda.gov/research/publications/misc/63363_2010%20Parrotta%20Tokyo%20conference%20Proceedings%202010.pdf
[15] https://www.nature.com/articles/s41598-019-45041-1
[16] https://www.nature.com/articles/s41598-023-50146-9
[17] https://www.pnas.org/doi/10.1073/pnas.2416740121
[18] https://www.sccs.swarthmore.edu/users/08/bblonder/phys120/docs/mccann.pdf
[19] https://www.sciencedirect.com/science/article/abs/pii/S0169534723000885
[20] https://www.sciencedirect.com/science/article/abs/pii/S0370157324002850
[21] https://www.sciencedirect.com/science/article/abs/pii/S2214574517300081
[22] https://www.sciencedirect.com/science/article/pii/S0169534723002781
[23] https://www.sciencedirect.com/science/article/pii/S0959652623038593
[24] https://www.sciencedirect.com/science/article/pii/S1439179124000495