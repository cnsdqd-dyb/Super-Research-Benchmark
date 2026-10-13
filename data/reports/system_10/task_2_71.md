# Deep Research Report: perplexity/sonar-deep-research
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** d424044c | **Time:** 97.66s | **Cost:** $1.08139
--------------------------------------------------------------------------------

# Eigenvalue Decomposition of Age-Specific Transition Matrices and Asymptotic Population Reproduction Dynamics

The asymptotic behavior of age-structured populations is fundamentally determined by the eigenvalue decomposition of population projection matrices, which translate age-specific vital rates into long-term population dynamics through mathematically elegant mechanisms rooted in linear algebra. The dominant eigenvalue of these matrices, commonly denoted λ, represents the asymptotic growth rate toward which populations inexorably converge regardless of initial age structure, while the associated eigenvectors encode the stable age distribution and reproductive value across age classes—together providing complete specification of long-term population reproduction functions. Through the lens of eigenvalue analysis, demographic processes including survival, fertility, and aging become unified into a coherent framework where transient fluctuations decay predictably and reproducible populations approach stable trajectories determined entirely by the spectral properties of their transition matrices.

## Mathematical Foundations of Age-Structured Population Models

### Matrix Population Models and Their Construction

The foundation for understanding asymptotic population behavior begins with the construction of age-structured population projection matrices, which discretize continuous demographic processes into mathematical models amenable to eigenvalue analysis.[5][25][33] These matrices, most commonly the Leslie matrix formulated by Patrick Leslie in 1945, transform a population vector at time t into a new population vector at time t+1 through matrix multiplication, creating a discrete-time dynamical system that captures essential life history information.[5][25] The Leslie matrix L takes a specific structural form dictated by biological constraints: the first row contains age-specific fertility rates (fecundities), the subdiagonal contains age-specific survival probabilities, and all other entries are structural zeros—a pattern reflecting the biological reality that individuals can only age forward by one year per time step and that birth must occur to contribute to the youngest age class.[5][25][33]

The construction of these matrices requires careful quantification of vital rates that vary across age classes, specifically the age-specific survival probabilities \(s_x\) representing the fraction of individuals surviving from age x to age x+1, and the age-specific fecundity rates \(m_x\) representing average female offspring per female of age x.[2][5][16] These vital rates are combined in the matrix elements to create fertility terms that account for both reproduction and offspring survival from birth to census time.[5][16][56] The resulting population projection equation \(\mathbf{n}_{t+1} = \mathbf{L}\mathbf{n}_t\) or more generally \(\mathbf{n}_t = \mathbf{L}^t\mathbf{n}_0\) provides an iterative method for projecting populations forward in time, yet this iterative approach obscures the underlying asymptotic dynamics that eigenvalue decomposition reveals.[5][25][33]

Beyond Leslie matrices, stage-structured models using Lefkovitch matrices extend the framework to populations where ontogenetic stages rather than strict ages determine vital rates, allowing individuals to remain within stages or transition forward, creating a more general mathematical structure that still obeys the same eigenvalue principles.[29][60] Both matrix types share fundamental mathematical properties: they are non-negative matrices (all entries are zero or positive), typically primitive (aperiodic and irreducible under standard biological assumptions), and their asymptotic dynamics are completely determined by eigenanalysis.[2][5][10][25]

### The Perron-Frobenius Theorem and Population Growth

The mathematical guarantee that age-structured populations possess well-defined asymptotic behavior stems from the Perron-Frobenius (PF) theorem, a fundamental result in matrix theory that applies specifically to non-negative matrices characteristic of population projection matrices.[7][10] This theorem asserts that any real square non-negative matrix possesses a unique dominant eigenvalue—the eigenvalue of largest magnitude—denoted \(\lambda_{\text{pf}}\), which is real and positive, with algebraic and geometric multiplicity one.[10][52] Crucially for population dynamics, the theorem guarantees that this dominant eigenvalue exceeds all other eigenvalues in absolute value: \(|\lambda_i| < \lambda_{\text{pf}}\) for all non-dominant eigenvalues \(\lambda_i\).[10][52]

The corresponding eigenvectors are equally remarkable: the right eigenvector associated with the dominant eigenvalue contains strictly positive components, and the left eigenvector similarly consists of positive entries.[10][52] These conditions ensure that population dynamics cannot exhibit oscillations or complex behavior indefinitely—the long-term behavior must be positive and real, reflecting the biological reality that populations cannot have negative abundances or complex-valued sizes.[7][10] For primitive matrices typical of age-structured biological populations, all non-dominant eigenvalues satisfy the stricter condition that their absolute values are strictly less than the dominant eigenvalue, ensuring rapid convergence to asymptotic behavior after initial transient phases.[10][52]

The proof of the Perron-Frobenius theorem provides insight into why population growth is determined by this unique positive eigenvalue. Consider a non-negative matrix A with rows and columns corresponding to age classes. If we define the function \(f(x) = \min_i (Ax)_i / x_i\) over positive vectors x, this function achieves its maximum value at the dominant eigenvalue, and the optimal vector is the corresponding right eigenvector.[52] This maximum principle—that the dominant eigenvalue maximizes the minimum growth factor across age classes—explains why populations converge to a balanced growth state where all age classes grow at the same rate equal to the dominant eigenvalue.[52]

## Age-Specific Transition Matrices and Population Dynamics

### Leslie Matrix Structure and Biological Interpretation

The Leslie matrix encodes complete demographic information in a structured form that directly connects biological parameters to mathematical analysis.[5][25][33] Writing the Leslie matrix explicitly for a population with m age classes:

\[ \mathbf{L} = \begin{bmatrix} f_0 & f_1 & f_2 & \cdots & f_{m-1} \\ s_0 & 0 & 0 & \cdots & 0 \\ 0 & s_1 & 0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & s_{m-2} & 0 \end{bmatrix} \][25][33]

Each element encodes specific biological meaning: the top row contains fertility terms \(f_x\) that represent per-capita female offspring production by females of age x, adjusted for the survival of those offspring from birth to the age when the population census is conducted; the subdiagonal contains survival probabilities \(s_x\) representing the fraction of females surviving from age x to age x+1; and all other entries are zero because no other transitions are biologically possible.[5][16][25][33] The fertility term \(f_x = s_x m_{x+1}\) for post-birth pulse sampling accounts for the fact that females of age x must survive to age x+1 to give birth, with their offspring then surviving to infancy.[5][56]

When this matrix multiplies a population vector \(\mathbf{n}_t = [n_0(t), n_1(t), \ldots, n_{m-1}(t)]^T\) containing the number of females in each age class, the resulting vector \(\mathbf{n}_{t+1} = \mathbf{L}\mathbf{n}_t\) describes how births from all reproductive age classes sum to create the new first age class, while each existing age class ages forward with survival probability reduced by mortality.[5][16][25][33] This mechanical transformation, repeated through matrix multiplication, eventually produces population trajectories that exhibit characteristic patterns determined entirely by the eigenstructure of L.

### Extensions to Generalized Life Histories

While Leslie matrices assume strict annual age classes, biological realism often requires models incorporating stage structure where individuals may remain in stages of variable duration.[29][60] The Lefkovitch matrix generalizes the Leslie structure by allowing self-loops (diagonal elements) that enable individuals to remain in the same stage class while also allowing transitions to subsequent stages.[29][60] This modification preserves the mathematical structure necessary for eigenvalue analysis while accommodating stage-specific biology including duration distributions, development of individuals, and variable reproductive patterns across life stages.[29][57][60]

The fundamental eigenvalue properties remain unchanged: the dominant eigenvalue of a Lefkovitch matrix still determines asymptotic growth rate, and the associated eigenvectors still define stable stage distribution and reproductive values.[29][60] This mathematical universality across different matrix formulations—whether strictly age-structured or incorporating stage heterogeneity—demonstrates that the eigenvalue approach provides a general framework for age- or stage-structured population dynamics.[16][29][60] Extensions incorporating density-dependence modify matrix elements as functions of population size, introducing nonlinearity, yet even these models maintain local asymptotic dynamics determined by eigenanalysis around equilibrium points.[27]

## Eigenvalue Analysis and Asymptotic Growth Rates

### The Dominant Eigenvalue as Population Growth Rate

The dominant eigenvalue λ of a population projection matrix represents the asymptotic growth rate—the multiplicative factor by which the total population grows per unit time when the age structure has stabilized to the stable age distribution.[3][5][6][25][33] This fundamental insight emerges from spectral decomposition of the projection matrix, which expresses any initial population vector as a linear combination of eigenvectors weighted by eigenvalues raised to successive powers.[18][44][55] After sufficient time t, terms involving non-dominant eigenvalues—raised to powers t where t is large—decay to negligible magnitude because \(\lambda_i^t \to 0\) when \(|\lambda_i| < \lambda_{\text{pf}}\), leaving only the dominant eigenvalue term dominating the long-term dynamics.[18][44][55]

The spectral decomposition can be written as:

\[ \mathbf{n}(t) = \lambda_1^t \mathbf{c}_1 \mathbf{w}_1 + \sum_{i=2}^{m} \lambda_i^t \mathbf{c}_i \mathbf{w}_i \][44][55]

where \(\lambda_1\) is the dominant eigenvalue, \(\mathbf{w}_i\) are the right eigenvectors, and \(\mathbf{c}_i = \mathbf{v}_i^* \cdot \mathbf{n}(0)\) are coefficients determined by the left eigenvector \(\mathbf{v}_i\) and initial population structure \(\mathbf{n}(0)\).[44][55] As t increases, the dominant term grows exponentially while all other terms decay, revealing the asymptotic population trajectory depends entirely on the dominant eigenvalue and its associated eigenvector.[44][55] When \(\lambda_1 > 1\), the population grows exponentially at rate \(\lambda_1\); when \(\lambda_1 < 1\), the population declines toward extinction at rate \(\lambda_1\); when \(\lambda_1 = 1\), the population approaches a constant size at the stable age distribution.[3][5][25][35][50]

Computing the dominant eigenvalue requires solving the characteristic equation \(\det(\mathbf{L} - \lambda \mathbf{I}) = 0\), which for a Leslie matrix with m age classes reduces to the Euler-Lotka equation that connects vital rates directly to growth rate.[25][33][36] For Leslie matrices specifically, the characteristic polynomial takes the form:

\[ 1 = \sum_{a=1}^{\omega} \lambda^{-a} \ell(a) b(a) \][36]

where \(\ell(a)\) is the cumulative survivorship to age a and \(b(a)\) is the fertility at age a.[36] This equation encapsulates how the balance between reproduction and survival at each age determines population growth: if reproduction weighted by survivorship exceeds what is needed for replacement (net reproductive rate R₀ > 1), then \(\lambda > 1\) and the population grows.[36][37]

### Interpretation and Biological Significance

The biological interpretation of λ as the asymptotic growth rate makes eigenvalue analysis immediately relevant to conservation and management questions. When λ is estimated for an endangered species using known vital rates, the value directly indicates whether the population will persist, decline toward extinction, or increase without bound—provided vital rates remain constant.[5][25] More fundamentally, λ encapsulates the integrated effect of all vital rates: survival probabilities and fertility rates at each age combine multiplicatively through the matrix structure to produce a single number determining long-term fate.[5][25][37]

The uniqueness and positivity of the dominant eigenvalue guarantee that populations cannot have multiple competing asymptotic growth rates or complex-valued trajectories.[10][52] This mathematical guarantee reflects biological reality: a population either grows, declines, or remains stable in the long term, and this fate is determined by the fundamental reproductive strategy encoded in life history.[3][5][10] The dominant eigenvalue captures this strategy as a scalar quantity, reducing the infinite complexity of demography to a single number with clear interpretation.

## Eigenvectors and Population Structure

### Stable Age Distribution from Right Eigenvector

The right eigenvector associated with the dominant eigenvalue \(\mathbf{w}_1\), normalized so that its elements sum to one, gives the stable age distribution (SAD)—the proportion of individuals in each age class that the population approaches asymptotically.[5][11][14][25][31][35] This distribution emerges naturally from the eigenvalue equation \(\mathbf{L}\mathbf{w}_1 = \lambda_1 \mathbf{w}_1\), which states that when the population vector equals this eigenvector (possibly scaled), multiplying by the Leslie matrix simply scales it by λ₁, preserving its proportional structure.[5][11][25][31] Biologically, once a population reaches the stable age distribution, all age classes grow or decline at the identical rate λ₁, and the ratio of individuals across age classes remains constant—a remarkable simplification showing that demographic complexity eventually reduces to proportional growth.[5][11][25][31]

The stable age distribution depends on the relative magnitudes of fertility and survival rates at each age, creating counterintuitive patterns: a population with high intrinsic growth rate λ will have a disproportionately young age structure because high reproduction allows the population to maintain more young individuals, while a declining population (λ < 1) shifts toward older age classes because fewer births mean proportionally more survivors persist.[5][11][25][33] This relationship between λ and age structure is absolute, not influenced by initial age distribution: regardless of starting conditions, if vital rates remain constant, the population will eventually converge to the stable age distribution associated with that Leslie matrix.[5][11][21][25]

The convergence to stable age distribution occurs at a rate governed by the ratio of the dominant to subdominant eigenvalue, quantified by the damping ratio \(\rho = \lambda_1 / |\lambda_2|\).[8][43][46] Populations with high damping ratios (dominant eigenvalue much larger in magnitude than other eigenvalues) converge rapidly to their stable structure and exhibit smooth long-term growth, while populations with damping ratios near one exhibit transient oscillations before settling into asymptotic growth.[8][43][46] This transient behavior, though not affecting ultimate asymptotic growth rate, can substantially influence short-term population size and management outcomes.[38][41]

### Reproductive Value from Left Eigenvector

The left eigenvector associated with the dominant eigenvalue \(\mathbf{v}_1\), or equivalently the eigenvector of the transpose matrix \(\mathbf{L}^T\), carries equally profound biological meaning: when normalized appropriately (typically dividing by the first non-zero element), it gives the reproductive value vector, where element \(v_x\) represents the expected contribution of an individual of age x to the total population size in the distant future.[6][13][14][31][34] This quantity, defined originally by R.A. Fisher, quantifies how much an individual at a given age will contribute to future population growth relative to individuals of other ages, accounting for both their remaining lifespan and their fertility potential.[13][34] The reproductive value increases with age up to the peak reproductive years (where it reaches maximum) and then declines as individuals age past reproduction.[6][14][31][34]

The reproductive value vector satisfies the left eigenvalue equation \(\mathbf{v}_1^T \mathbf{L} = \lambda_1 \mathbf{v}_1^T\), which reveals that reproductive values grow at the rate λ₁ across all age classes.[14][31][34] Biologically, this equation encodes the fundamental principle that in a stable population, the total reproductive value (summed across all individuals weighted by their reproductive values) grows at exactly the asymptotic growth rate, providing a demographic quantity that behaves with perfect regularity despite fluctuations in total population size due to transient dynamics.[13][34][38]

When the initial population vector is weighted by reproductive values—a transformation creating the reproductive value weighted population size—the resulting quantity exhibits pure exponential growth at rate λ₁ with no transient fluctuations, unlike the total population size which oscillates before stabilizing.[13][34][38] This filtering property makes reproductive value mathematically powerful for analyzing stochastic population dynamics and evolutionary dynamics in fluctuating environments, where weighting by reproductive value removes temporal autocorrelation induced by transient age-structure fluctuations.[13] Conservation and management benefit from understanding reproductive value because maximizing reproductive value weighted populations focuses efforts on the ages that matter most for long-term population growth.

## The Relationship Between Eigenanalysis and Population Reproduction Functions

### Net Reproductive Rate and Generation Time

The complete determination of asymptotic population reproduction dynamics involves three quantities directly computable from vital rates and connected to the dominant eigenvalue: the net reproductive rate \(R_0\), the generation time \(T\), and the population growth rate \(r = \ln(\lambda)\).[16][36][51] The net reproductive rate \(R_0 = \sum_x l(x) m(x)\) represents the expected number of female offspring per female over her entire lifetime, where \(l(x)\) is cumulative survivorship and \(m(x)\) is age-specific fertility.[16][51] This quantity directly predicts population trend: when \(R_0 > 1\), individuals replace themselves with more than one offspring on average, creating positive population growth; when \(R_0 < 1\), individuals fail to replace themselves and the population declines; when \(R_0 = 1\), individuals replace themselves exactly and the population neither grows nor declines.[16][51]

The generation time \(T = \sum_x l(x) m(x) x / R_0\) represents the average age of mothers at offspring birth, weighted by fertility.[16][51] Together, \(R_0\) and \(T\) provide classical approximations to the population growth rate through Lotka's equation: \(r \approx \ln(R_0) / T\), which directly connects the level of reproduction (via \(R_0\)) and its timing (via \(T\) to the long-term asymptotic growth rate.[16][51] This relationship becomes exact when populations reach stable age distribution, where \(r = \ln(\lambda)\) precisely. The remarkable insight that three demographic quantities—level of reproduction, timing of reproduction, and asymptotic growth rate—relate through mathematical necessity emerges directly from eigenvalue analysis.

### Sensitivity and Elasticity Analysis

While the dominant eigenvalue itself determines asymptotic growth rate, management and evolutionary questions require understanding how λ changes when vital rates are modified. Sensitivity analysis quantifies the absolute change in λ resulting from marginal changes in a matrix element \(a_{ij}\):[22][39][55]

\[ S_{ij} = \frac{\partial \lambda}{\partial a_{ij}} = \frac{v_i w_j}{v^T w} \][39][44][55]

where \(v_i\) and \(w_j\) are the elements of the left and right eigenvectors and \(v^T w\) is their inner product.[39][44][55] This formula reveals that sensitivity combines both the reproductive value of the age class being modified (the source, captured by \(v_i\)) and the stable age distribution of the affected age class (the destination, captured by \(w_j\))—a beautiful result showing that modifying vital rates of highly reproductive ages yields larger changes in λ than modifying ages of low reproductive value.[39][44][55]

Elasticity analysis rescales sensitivities by the relative magnitude of the parameter being changed, computing the proportional change in λ from a proportional change in a vital rate: \(E_{ij} = (a_{ij}/\lambda) S_{ij}\).[39][42][45] Because elasticities sum to one across all matrix elements, they directly compare the relative importance of different vital rates for population growth, controlling for differences in baseline magnitudes.[39][42][45] Patterns of elasticity reveal fundamental life history principles: for long-lived organisms with delayed reproduction, adult survival elasticity typically dominates because long adult lifespans provide many opportunities for mortality reduction to accumulate benefits; for short-lived organisms with early reproduction, fertility elasticity often dominates because high reproductive output drives growth.[39][42][45]

These sensitivity and elasticity patterns emerge directly from the eigenvector structure and thus represent consequences of the fundamental mathematics determining asymptotic dynamics. A population's elasticity pattern represents its demographic "strategic" response to environmental variation: vital rates to which λ is highly elastic determine which environmental impacts most strongly influence population growth, and conversely, management interventions targeting high-elasticity parameters generate larger population responses than changes to low-elasticity parameters.[39][42][45]

## Transient Dynamics and Approach to Asymptotic Behavior

### The Spectral Decomposition and Time-Dependent Population Trajectories

While asymptotic dynamics depend entirely on the dominant eigenvalue, the approach to asymptotics follows a complex trajectory determined by all eigenvalues and their associated eigenvectors.[1][18][20][23][44][55] The full spectral decomposition \(\mathbf{n}(t) = \sum_i \lambda_i^t c_i \mathbf{w}_i\) reveals that population size at any time represents a weighted sum of exponential terms, each growing or decaying at its eigenvalue's rate.[18][44][55] Initially, when t is small, the non-dominant terms—involving non-dominant eigenvalues—can contribute substantially to population trajectory, creating transient fluctuations, overshoots, or undershoots relative to the smooth exponential growth predicted by the dominant term alone.[1][18][23][44][55]

The duration of transient dynamics depends on which non-dominant eigenvalue is largest: the second-largest eigenvalue \(\lambda_2\) controls how rapidly the transient terms decay.[8][20][23][43][46] When \(\lambda_2\) is much smaller than \(\lambda_1\), non-dominant terms decay quickly (within a few generations) and the population rapidly exhibits smooth asymptotic growth; when \(\lambda_2\) is close in magnitude to \(\lambda_1\), transient dynamics persist for many generations before asymptotic behavior dominates.[8][20][23][43][46] This explains why some populations show characteristic oscillations superimposed on growth—the oscillations represent contributions from complex conjugate pairs of non-dominant eigenvalues that produce periodic components in the population trajectory before decaying away.[1][23]

For human populations and other long-lived species, transient dynamics can persist for decades despite constant vital rates, with population momentum—the continued growth after fertility drops below replacement level—emerging as a consequence of current age structure's departure from the stable age distribution.[44][54] The spectral decomposition formalism explains this phenomenon exactly: the population continues growing because the coefficient \(c_1\) (the inner product of reproductive value vector and current population vector) is still positive and large, driving substantial growth at rate λ despite eventual eventual decline implied by λ < 1 itself arising from the non-dominant terms becoming negative and outweighing the dominant term as time progresses further.[44][55]

### Keyfitz's Delta and Distance to Stable Age Distribution

Measuring departure from the stable age distribution quantifies how much transient dynamics remain. Keyfitz's delta \(\Delta\), defined as \(\Delta(x, w) = \frac{1}{2}\sum_i |x_i - w_i|\) where x is the current age structure and w is the stable age distribution, ranges from 0 (perfect match) to 1 (maximum difference).[31][38] Populations with large Δ values exhibit larger transient deviations from asymptotic growth than populations closer to stable structure.[38][54] This quantity directly predicts transient dynamics: the further from stable age distribution, the greater the influence of non-dominant eigenvectors and the more pronounced transient overshoots or undershoots.[20][23][38]

The relationship between distance to stable age distribution and reproductive value provides profound demographic insight: initial population structures rich in young individuals (pre-stable) have low reproductive values and thus produce weak transient growth even if population size is substantial, while structures rich in reproductive-aged individuals (post-stable) have high reproductive values and produce vigorous transient growth.[38] This explains why a youthful population can show declining growth rate despite absolute growth in size, or why an aging population can show rising growth rate despite absolute decline in size—the apparent contradictions resolve when reproductive value weighting reveals the true transient dynamics.[38]

## Applications of Eigenvalue Decomposition to Population Reproduction Functions

### Conservation and Management Implications

The eigenvalue framework transforms population management from guesswork into quantitative science. By estimating Leslie matrices from field data of vital rates, managers can calculate λ for endangered species and predict whether populations will persist without intervention.[5][25] For species where λ < 1, sensitivity analysis identifies which vital rates most strongly influence growth rate, directing limited resources toward interventions with maximum impact.[39][42][45] The principle that high-elasticity vital rates deserve priority emerges directly from eigenvalue analysis and demonstrates that mathematical insight generates practical management guidance.[39][42][45]

Population viability analysis (PVA), which estimates extinction risk from demographic parameters, relies fundamentally on calculating λ and incorporating stochasticity around this central eigenvalue-derived quantity.[25][31][35] Stochastic population growth rate, accounting for environmental variation in vital rates, approximately equals the deterministic growth rate reduced by a variance penalty that depends on sensitivities of λ to parameter variation—a result flowing directly from perturbation analysis of eigenvalues.[44][55]

### Evolutionary Dynamics and Life History Evolution

The dominant eigenvalue equals individual fitness—the expected lifetime reproductive success—under constant vital rates. This connection between demographic growth rate and evolutionary fitness means that natural selection shapes age-specific schedules of reproduction and survival to maximize λ, making eigenvalue analysis central to understanding life history evolution.[5][16][48][51] Populations evolving under selection should accumulate genetic variants that increase λ, driving populations toward life histories with higher population growth rates. Conversely, populations facing environmental constraints show life history patterns that optimize fitness (λ) under those constraints, explaining why the timing and level of reproduction vary systematically across species and ecological contexts.[51]

The reproductive value vector derived from the left eigenvector determines selection intensity on traits at each age.[13][34][55] Traits in high-reproductive-value age classes experience strong selection pressure while traits in low-reproductive-value ages (very young or very old) experience weak selection, explaining why senescence (age-related decline in survival and fertility) evolves despite its negative effects on individual mortality—selection pressure to maintain function weakens at old ages where reproductive value approaches zero.[13][34] This fundamental evolutionary principle emerges mathematically from eigenanalysis of population projection matrices.

### Stochastic and Fluctuating Environments

When environmental variation causes vital rates to fluctuate randomly, the deterministic eigenvalue approach requires modification to predict long-term population growth. Tuljapurkar's small-noise approximation shows that the stochastic growth rate \(\lambda_s\) (geometric mean growth rate over many generations) approximates \(\ln(\lambda_s) \approx \ln(\lambda_d) - \frac{\sigma^2}{2}\), where \(\lambda_d\) is the deterministic growth rate from the mean projection matrix and σ² is a variance term depending on sensitivities of λ to vital rate changes.[44][55] This elegant result demonstrates that understanding how eigenvalues depend on vital rate changes (sensitivity analysis) directly predicts population fate in stochastic environments.[44][55]

In random Leslie models where matrix elements themselves carry uncertainty, perturbative approaches generalize eigenanalysis to reveal effective growth rates and mean-value invariant state vectors that describe long-term dynamics of mean population vector conditional on initial state.[25] The mathematics demonstrates that even with uncertainty, populations approach predictable asymptotic distributions determined by analogs of the dominant eigenvalue, though computation becomes substantially more complex.[25]

## Conclusion: Unifying Population Dynamics Through Spectral Analysis

The eigenvalue decomposition of age-specific transition matrices provides the complete mathematical determination of asymptotic population behavior through a framework of remarkable unity and power. The dominant eigenvalue emerges as the fundamental quantity controlling long-term population growth, determining whether populations persist, decline, or increase through a calculation encoding the integrated effects of all vital rates.[3][5][25][33][37] The associated right and left eigenvectors specify the stable age distribution—the unique proportional structure toward which populations converge—and reproductive values that quantify each individual's contribution to future population growth, creating a complete description of asymptotic population reproduction functions.[5][11][14][25][31][34]

This mathematical structure, rooted in the Perron-Frobenius theorem, guarantees that populations behave predictably over long time horizons despite initial transient fluctuations and complexities.[10][52] The spectral decomposition reveals that asymptotic dynamics isolate from transient effects through exponential decay of non-dominant terms, with the timescale of this decay determined by the ratio of dominant to subdominant eigenvalue.[18][43][44][55] Sensitivity analysis provides quantitative guidance for management by showing exactly how changes in vital rates modify the dominant eigenvalue and thus long-term population growth.[39][44][55]

The practical applications of eigenvalue analysis—conservation management, evolutionary prediction, stochastic projection, and life history understanding—all flow from fundamental mathematical properties of the projection matrix spectral decomposition. A single calculation of matrix eigenvalues and eigenvectors transforms measured or estimated vital rates into complete understanding of asymptotic population dynamics, stable structure, reproductive values, and sensitivity to environmental and demographic change. This elegant synthesis of mathematics and biology demonstrates why eigenvalue decomposition has become the standard framework for age-structured population analysis and why eigenvalues themselves are the most important summary statistics for understanding population reproduction functions.

## Annotations
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Age‐specific sensitivity analysis of stable, stochastic and transient ...', 'url': 'https://onlinelibrary.wiley.com/doi/full/10.1002/ece3.9561'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Application of Leslie Matrix Model in Human Population Dynamics ...', 'url': 'https://www.seejph.com/index.php/seejph/article/download/2723/1797/4033'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Reproductive Value for Branching Population Models', 'url': 'https://open.library.ubc.ca/media/stream/pdf/24/1.0435572/4'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Notes on building matrix population models - TechRxiv', 'url': 'https://www.techrxiv.org/users/653370/articles/1283925/master/file/data/25PE-Matrix-v3c-main/25PE-Matrix-v3c-main.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '7.3: Leslie Matrix Models - Biology LibreTexts', 'url': 'https://bio.libretexts.org/Courses/Gettysburg_College/02:_Principles_of_Ecology_-_Gettysburg_College_ES_211/07:_A_Quantitative_Approach_to_Population_Ecology/7.03:_Leslie_Matrix_Models'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'eigen.analysis function - RDocumentation', 'url': 'https://www.rdocumentation.org/packages/demogR/versions/0.6.0/topics/eigen.analysis'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Lecture 17 Perron-Frobenius Theory', 'url': 'https://stanford.edu/class/ee363/lectures/pf.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] FW662 Lecture 5 – Age-structured models', 'url': 'https://sites.warnercnr.colostate.edu/gwhite/wp-content/uploads/sites/73/2017/06/Lecture-5-Age-structured-models.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] THE NET REPRODUCTIVE VALUE AND STABILITY IN MATRIX ...', 'url': 'https://math.arizona.edu/~cushing/NetReproductiveValueAndStability%20NRM1994.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Perron–Frobenius theorem - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Perron%E2%80%93Frobenius_theorem'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] MATH 172 - Mathematical Modelling for the Life Sciences - Spring 20', 'url': 'https://people.math.sc.edu/josephcf/Teaching/172/Files/Lecture%20Notes/Multiple%20Species%20Population%20Modelling%20-%203%20-%20Eigenvectors%20and%20Eigenvalues.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Calculate net reproductive rate (R0) from a matrix population model', 'url': 'https://jonesor.github.io/Rage/reference/net_repro_rate.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Reproductive Value and Fluctuating Selection in an Age-Structured ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC2766322/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Introduction to Demography - UBC Zoology', 'url': 'https://www.zoology.ubc.ca/~bio301/Bio301/Lectures/Lecture18/Overheads.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The effect of dispersal on asymptotic total population size in discrete', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC10514157/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Age-Structured Population Models', 'url': 'https://faculty.fiu.edu/~trexlerj/Advanced_Ecology/AE12_Lecture_4.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Chapter 9 Population Projection II: Deterministic Analysis - Bookdown', 'url': 'https://bookdown.org/cdorm/lefko3gentle/detan.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] An Application of Linear Algebra in Population Biology', 'url': 'http://buzzard.ups.edu/courses/2007spring/projects/lubetkin-paper-revised.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Parameterizing the growth-decline boundary for uncertain ...', 'url': 'https://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1050&context=mathfacpub'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Inferring transient dynamics of human populations from matrix non ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6018585/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Why a Population Converges to Stability - CORE', 'url': 'https://core.ac.uk/download/pdf/33892570.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Calculating second derivatives of population growth rates for ...', 'url': 'https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210x.12179'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Solving three core challenges in transient dynamics analysis of ...', 'url': 'https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210X.70139'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Why a Population Converges to Stability - IIASA PURE', 'url': 'https://pure.iiasa.ac.at/id/eprint/1247/7/RR-80-019.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Leslie matrix - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Leslie_matrix'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Population projection - Ernesto Amaral', 'url': 'http://www.ernestoamaral.com/docs/soci320-19fall/Lecture05.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] nonlinear matrix models and population dynamics 1 - Arizona Math', 'url': 'https://math.arizona.edu/~cushing/NonlinearMatrixModelsAndPopulationDynamics-1988-NRM.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Distance to stable stage distribution in plant populations and ...', 'url': 'https://besjournals.onlinelibrary.wiley.com/doi/10.1111/j.1365-2745.2011.01845.x'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Matrix population models', 'url': 'https://kevintshoemaker.github.io/NRES-470/LECTURE7.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Integrating eco-evolutionary dynamics - matrix population models', 'url': 'https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210X.14111'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Matrix Population Models: deterministic and stochastic dynamics', 'url': 'https://cws.auburn.edu/shared/files?id=217&filename=ConMan_FileDownload_MatrixPopulation.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Another look at the eigenvalues of a population matrix model - PMC', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6855200/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Leslie matrix', 'url': 'https://en.wikipedia.org/wiki/Leslie_matrix'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Introduction to Demography - UBC Zoology', 'url': 'https://www.zoology.ubc.ca/~bio301/Bio301/Lectures/Lecture18/Overheads.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Chapter 9 Population Projection II: Deterministic Analysis - Bookdown', 'url': 'https://bookdown.org/cdorm/lefko3gentle/detan.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Euler–Lotka equation', 'url': 'https://en.wikipedia.org/wiki/Euler%E2%80%93Lotka_equation'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] THE NET REPRODUCTIVE VALUE AND STABILITY IN MATRIX ...', 'url': 'https://math.arizona.edu/~cushing/NetReproductiveValueAndStability%20NRM1994.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Transient population dynamics: Relations to life history and initial ...', 'url': 'https://www.demogr.mpg.de/publications/files/2364_1155281974_1_Koons%20et%20al%202005.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Sensitivity and elasticity matrices - compadre-db.org', 'url': 'https://compadre-db.org/Education/article/sensitivity-and-elasticity-matrices'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Calculate net reproductive rate (R0) from a matrix population model', 'url': 'https://jonesor.github.io/Rage/reference/net_repro_rate.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Perturbation analysis of transient population dynamics using matrix ...', 'url': 'https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210X.12543'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Patterns and rules for sensitivity and elasticity in population ...', 'url': 'https://esajournals.onlinelibrary.wiley.com/doi/abs/10.1890/08-1188.1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Leslie matrix - Université Paris-Saclay', 'url': 'https://hebergement.universite-paris-saclay.fr/marcgirondot/ewExternalFiles/Leslie.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Leslie Matrix II Formal Demography Stanford Spring Workshop in ...', 'url': 'https://web.stanford.edu/~jhj1/teachingdocs/Jones-Leslie2-050208.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Another look at the eigenvalues of a population matrix model - PMC', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6855200/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A note on migration perturbation and convergence rates to a steady ...', 'url': 'https://www.mathnet.ru/php/getFT.phtml?jrnid=ps&paperid=373&what=fullt'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Integrating eco‐evolutionary dynamics into matrix population ...', 'url': 'https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.14111'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Using Population Models to Teach Eigenvalues and Eigenvectors', 'url': 'http://dimacs.rutgers.edu/Publications/Modules/Module07-3/dimacs07-3.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] The Perron-Frobenius theorem.', 'url': 'https://www.math.miami.edu/~armstrong/685fa12/sternberg_perron_frobenius.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '7.3: Leslie Matrix Models - Biology LibreTexts', 'url': 'https://bio.libretexts.org/Courses/Gettysburg_College/02:_Principles_of_Ecology_-_Gettysburg_College_ES_211/07:_A_Quantitative_Approach_to_Population_Ecology/7.03:_Leslie_Matrix_Models'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Generation Time, Net Reproductive Rate, and Growth in Stage-age ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6601636/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Perron–Frobenius theorem - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Perron%E2%80%93Frobenius_theorem'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Week 2 note: population dynamics', 'url': 'https://ecology.dlilab.com/lectures/03_popdynamics/notes'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Age-specific growth rates: The legacy of past population dynamics', 'url': 'https://read.dukeupress.edu/demography/article/25/3/429/171479/Age-specific-growth-rates-The-legacy-of-past'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Leslie Matrix II Formal Demography Stanford Spring Workshop in ...', 'url': 'https://web.stanford.edu/~jhj1/teachingdocs/Jones-Leslie2-050208.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Leslie Matrix = Population Projection Matrix Contains age-specific ...', 'url': 'https://www.montana.edu/screel/teaching/bioe-440r-521/documents/leslie.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Stage duration distributions in matrix population models - PMC - NIH', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC6144974/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Eigendecomposition of a matrix - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '7.3: Leslie Matrix Models - Biology LibreTexts', 'url': 'https://bio.libretexts.org/Courses/Gettysburg_College/02:_Principles_of_Ecology_-_Gettysburg_College_ES_211/07:_A_Quantitative_Approach_to_Population_Ecology/7.03:_Leslie_Matrix_Models'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] stage-structured matrix models', 'url': 'https://blog.uvm.edu/tdonovan-vtcfwru/files/2020/06/12-Donov-pages-322-CB.pdf'}}

## Sources
https://onlinelibrary.wiley.com/doi/full/10.1002/ece3.9561
https://www.seejph.com/index.php/seejph/article/download/2723/1797/4033
https://open.library.ubc.ca/media/stream/pdf/24/1.0435572/4
https://www.techrxiv.org/users/653370/articles/1283925/master/file/data/25PE-Matrix-v3c-main/25PE-Matrix-v3c-main.pdf
https://bio.libretexts.org/Courses/Gettysburg_College/02:_Principles_of_Ecology_-_Gettysburg_College_ES_211/07:_A_Quantitative_Approach_to_Population_Ecology/7.03:_Leslie_Matrix_Models
https://www.rdocumentation.org/packages/demogR/versions/0.6.0/topics/eigen.analysis
https://stanford.edu/class/ee363/lectures/pf.pdf
https://sites.warnercnr.colostate.edu/gwhite/wp-content/uploads/sites/73/2017/06/Lecture-5-Age-structured-models.pdf
https://math.arizona.edu/~cushing/NetReproductiveValueAndStability%20NRM1994.pdf
https://en.wikipedia.org/wiki/Perron%E2%80%93Frobenius_theorem
https://people.math.sc.edu/josephcf/Teaching/172/Files/Lecture%20Notes/Multiple%20Species%20Population%20Modelling%20-%203%20-%20Eigenvectors%20and%20Eigenvalues.pdf
https://jonesor.github.io/Rage/reference/net_repro_rate.html
https://pmc.ncbi.nlm.nih.gov/articles/PMC2766322/
https://www.zoology.ubc.ca/~bio301/Bio301/Lectures/Lecture18/Overheads.html
https://pmc.ncbi.nlm.nih.gov/articles/PMC10514157/
https://faculty.fiu.edu/~trexlerj/Advanced_Ecology/AE12_Lecture_4.pdf
https://bookdown.org/cdorm/lefko3gentle/detan.html
http://buzzard.ups.edu/courses/2007spring/projects/lubetkin-paper-revised.pdf
https://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1050&context=mathfacpub
https://pmc.ncbi.nlm.nih.gov/articles/PMC6018585/
https://core.ac.uk/download/pdf/33892570.pdf
https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210x.12179
https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210X.70139
https://pure.iiasa.ac.at/id/eprint/1247/7/RR-80-019.pdf
https://en.wikipedia.org/wiki/Leslie_matrix
http://www.ernestoamaral.com/docs/soci320-19fall/Lecture05.pdf
https://math.arizona.edu/~cushing/NonlinearMatrixModelsAndPopulationDynamics-1988-NRM.pdf
https://besjournals.onlinelibrary.wiley.com/doi/10.1111/j.1365-2745.2011.01845.x
https://kevintshoemaker.github.io/NRES-470/LECTURE7.html
https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210X.14111
https://cws.auburn.edu/shared/files?id=217&filename=ConMan_FileDownload_MatrixPopulation.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC6855200/
https://en.wikipedia.org/wiki/Leslie_matrix
https://www.zoology.ubc.ca/~bio301/Bio301/Lectures/Lecture18/Overheads.html
https://bookdown.org/cdorm/lefko3gentle/detan.html
https://en.wikipedia.org/wiki/Euler%E2%80%93Lotka_equation
https://math.arizona.edu/~cushing/NetReproductiveValueAndStability%20NRM1994.pdf
https://www.demogr.mpg.de/publications/files/2364_1155281974_1_Koons%20et%20al%202005.pdf
https://compadre-db.org/Education/article/sensitivity-and-elasticity-matrices
https://jonesor.github.io/Rage/reference/net_repro_rate.html
https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210X.12543
https://esajournals.onlinelibrary.wiley.com/doi/abs/10.1890/08-1188.1
https://hebergement.universite-paris-saclay.fr/marcgirondot/ewExternalFiles/Leslie.pdf
https://web.stanford.edu/~jhj1/teachingdocs/Jones-Leslie2-050208.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC6855200/
https://www.mathnet.ru/php/getFT.phtml?jrnid=ps&paperid=373&what=fullt
https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.14111
http://dimacs.rutgers.edu/Publications/Modules/Module07-3/dimacs07-3.pdf
https://www.math.miami.edu/~armstrong/685fa12/sternberg_perron_frobenius.pdf
https://bio.libretexts.org/Courses/Gettysburg_College/02:_Principles_of_Ecology_-_Gettysburg_College_ES_211/07:_A_Quantitative_Approach_to_Population_Ecology/7.03:_Leslie_Matrix_Models
https://pmc.ncbi.nlm.nih.gov/articles/PMC6601636/
https://en.wikipedia.org/wiki/Perron%E2%80%93Frobenius_theorem
https://ecology.dlilab.com/lectures/03_popdynamics/notes
https://read.dukeupress.edu/demography/article/25/3/429/171479/Age-specific-growth-rates-The-legacy-of-past
https://web.stanford.edu/~jhj1/teachingdocs/Jones-Leslie2-050208.pdf
https://www.montana.edu/screel/teaching/bioe-440r-521/documents/leslie.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC6144974/
https://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix
https://bio.libretexts.org/Courses/Gettysburg_College/02:_Principles_of_Ecology_-_Gettysburg_College_ES_211/07:_A_Quantitative_Approach_to_Population_Ecology/7.03:_Leslie_Matrix_Models
https://blog.uvm.edu/tdonovan-vtcfwru/files/2020/06/12-Donov-pages-322-CB.pdf