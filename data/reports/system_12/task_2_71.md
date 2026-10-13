# Deep Research Report: grok-4-1-fast-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 23d28091 | **Time:** 33.58s | **Cost:** $0.00576
--------------------------------------------------------------------------------

**In age-structured population models, the dynamics are described by a discrete-time projection equation \( \mathbf{n}(t+1) = A \mathbf{n}(t) \), where \( \mathbf{n}(t) \) is the population vector by age class at time \( t \), and \( A \) is the age-specific transition (or Leslie/projection) matrix.**[[1]](https://abel.math.harvard.edu/archive/21b_summer_05/supplements/popgrowth.pdf)

**The matrix \( A \) encodes age-specific fertilities (top row, representing reproduction) and transition probabilities (subdiagonal, representing survival/aging). Its eigenvalue decomposition \( A = P D P^{-1} \) (with \( D \) diagonal containing eigenvalues \( \lambda_1, \lambda_2, \dots \), \( P \) right eigenvectors, and \( P^{-1} \) using left eigenvectors) reveals the transient and asymptotic dynamics.**[[2]](https://cws.auburn.edu/shared/files?filename=ConMan_FileDownload_MatrixPopulation.pdf&id=217)[[3]](http://www.cecm.sfu.ca/~mmonagan/papers/Leslie3.pdf)

**Powers of the matrix are \( A^t = P D^t P^{-1} \), so \( \mathbf{n}(t) = A^t \mathbf{n}(0) \). By the Perron-Frobenius theorem (applicable to nonnegative, irreducible, primitive \( A \)), there is a real, positive dominant eigenvalue \( \lambda = \lambda_1 > |\lambda_i| \) for \( i \geq 2 \). As \( t \to \infty \), terms with \( \lambda_i^t \) ( \( i \geq 2 \)) decay relative to \( \lambda^t \), yielding:**
$$
\mathbf{n}(t) \sim c \lambda^t \mathbf{u},
$$
**where \( \mathbf{u} \) is the right eigenvector for \( \lambda \) (stable age distribution, normalized), \( \mathbf{v} \) is the left eigenvector (reproductive values), and \( c = (\mathbf{v}^T \mathbf{n}(0)) / (\mathbf{v}^T \mathbf{u}) \) projects the initial condition onto the dominant eigenspace.**[[4]](https://math.arizona.edu/~cushing/NetReproductiveValueAndStability%20NRM1994.pdf)[[5]](https://web.stanford.edu/~jhj1/teachingdocs/Jones-Leslie2-050208.pdf)

**"Population reproduction functions" typically refer to quantities like age-specific maternity/fertility schedules, net reproductive rates (R_0, total expected offspring per individual over lifetime), or total births \( b(t) = \mathbf{f}^T \mathbf{n}(t) \) (where \( \mathbf{f} \) is the fertility vector from \( A \)'s first row). Asymptotically:**

- **Total population size and reproduction grow geometrically at rate \( \lambda \) per time step**: \( \| \mathbf{n}(t) \| \sim k \lambda^t \), \( b(t+1)/b(t) \to \lambda \).[[6]](https://jonesor.github.io/BB512_Book/matrix-population-modelling.html)
- **Age distribution converges to \( \mathbf{u} \), independent of initial conditions (except proportionality).[[1]](https://abel.math.harvard.edu/archive/21b_summer_05/supplements/popgrowth.pdf)
- **Reproductive values \( \mathbf{v} \) weight age classes' contributions to future growth/reproduction; e.g., \( \mathbf{v}^T \mathbf{n}(t) \propto \lambda^t \).[[7]](https://blog.uvm.edu/tdonovan-vtcfwru/files/2020/06/13-Donov-pages-318-CB.pdf)

**λ solves the discrete Lotka equation \( 1 = \sum_i f_i \prod_{j=0}^{i-1} p_j \lambda^{-(i+1)} \) (p_j survivals), linking vital rates to growth. R_0 (dominant eigenvalue of the next-generation matrix) relates via the generation time, but λ directly governs per-time-step asymptotics.**[[8]](https://cran.r-project.org/web/packages/demogR/demogR.pdf)

**Transient dynamics depend on subdominant eigenvalues (damping ratio \( |\lambda_2 / \lambda| < 1 \)), but the decomposition isolates the dominant mode driving long-term reproduction and growth.**[[5]](https://web.stanford.edu/~jhj1/teachingdocs/Jones-Leslie2-050208.pdf)

## Annotations (Inline Citations)
Citation [1] (Pos: 302-386): [Web] https://abel.math.harvard.edu/archive/21b_summer_05/supplements/popgrowth.pdf
Citation [2] (Pos: 801-900): [Web] https://cws.auburn.edu/shared/files?filename=ConMan_FileDownload_MatrixPopulation.pdf&id=217
Citation [3] (Pos: 900-958): [Web] http://www.cecm.sfu.ca/~mmonagan/papers/Leslie3.pdf
Citation [4] (Pos: 1726-1813): [Web] https://math.arizona.edu/~cushing/NetReproductiveValueAndStability%20NRM1994.pdf
Citation [5] (Pos: 1813-1888): [Web] https://web.stanford.edu/~jhj1/teachingdocs/Jones-Leslie2-050208.pdf
Citation [6] (Pos: 2417-2493): [Web] https://jonesor.github.io/BB512_Book/matrix-population-modelling.html
Citation [1] (Pos: 2605-2689): [Web] https://abel.math.harvard.edu/archive/21b_summer_05/supplements/popgrowth.pdf
Citation [7] (Pos: 2853-2937): [Web] https://blog.uvm.edu/tdonovan-vtcfwru/files/2020/06/13-Donov-pages-318-CB.pdf
Citation [8] (Pos: 3226-3290): [Web] https://cran.r-project.org/web/packages/demogR/demogR.pdf
Citation [5] (Pos: 3489-3564): [Web] https://web.stanford.edu/~jhj1/teachingdocs/Jones-Leslie2-050208.pdf


## Sources
[1] https://apps.dtic.mil/sti/tr/pdf/ADA330118.pdf
[2] https://www.sciencedirect.com/science/article/pii/S0092824073800606
[3] https://www.uwyo.edu/dbmcd/popecol/feblects/lect11.html
[4] https://www.cmstatistics.org/CMStatistics2016/docs/BoA%20CFE-CMStatistics%202016.pdf?19691231160000=
[5] https://open.library.ubc.ca/media/stream/pdf/24/1.0435572/4
[6] https://www.demogr.mpg.de/books/drm/016/978-3-030-10534-1.pdf
[7] https://ui.adsabs.harvard.edu/abs/arXiv:2108.01133
[8] https://www.aimsciences.org/article/doi/10.3934/dcdsb.2022250
[9] https://epubs.siam.org/doi/10.1137/20M1366344
[10] https://www.bio.ens.psl.eu/~legendre/biblio/Bienvenu&amp;Al_DecompositionPopulationMatrix_TPB_2017.pdf
[11] https://blog.uvm.edu/tdonovan-vtcfwru/files/2020/06/13-Donov-pages-318-CB.pdf
[12] https://www.scribd.com/document/481230806/Modeling-Life-pdf
[13] https://webhome.auburn.edu/~grandjb/wildpop/lectures/lect_12.pdf
[14] https://scispace.com/pdf/net-reproduction-functions-for-nonlinear-structured-3izyz9ofal.pdf
[15] https://abel.math.harvard.edu/archive/21b_summer_05/supplements/popgrowth.pdf
[16] https://www.researchgate.net/figure/Left-System-with-five-subpopulations-of-sizes-N-i-N-u-i-and-shown-next-to-the-arrows_fig1_265791590
[17] https://www.semanticscholar.org/paper/Net-reproduction-functions-for-nonlinear-structured-Farkas/345a2d0d47e5a8cd869390e061af1e9c7764c97a
[18] https://cws.auburn.edu/shared/files?filename=ConMan_FileDownload_MatrixPopulation.pdf&id=217
[19] https://math.arizona.edu/~cushing/NetReproductiveValueAndStability%20NRM1994.pdf
[20] https://cdn.sciengine.com/doi/pdf/64FEDAE780974E57BD8C4A5A1D0F5661
[21] https://web.stanford.edu/~jhj1/teachingdocs/Jones-Leslie2-050208.pdf
[22] https://pmc.ncbi.nlm.nih.gov/articles/PMC4532751
[23] https://jointmathematicsmeetings.org/meetings/national/jmm-archive/1056-92-1197.pdf
[24] https://www.biorxiv.org/content/10.1101/2022.08.10.502782v1.full-text
[25] https://bookdown.org/cdorm/lefko3gentle/detan.html
[26] https://www.sciencedirect.com/science/article/abs/pii/S0040580910000638
[27] https://www.techrxiv.org/users/653370/articles/1283925/master/file/data/25PE-Matrix-v3c-main/25PE-Matrix-v3c-main.pdf
[28] https://www.bio.ens.psl.eu/~legendre/biblio/Bienvenu&Al_DecompositionPopulationMatrix_TPB_2017.pdf
[29] https://dspace.stir.ac.uk/bitstream/1893/26819/1/netrep-Feb2018.pdf
[30] https://www.ceh.ac.uk/sites/default/files/2023-03/radioecology-STAR-D5.2-Population-models.pdf
[31] https://symposia.gerad.ca/isdg2018/en/schedule?slot_id=1491
[32] https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0164814
[33] https://arxiv.org/pdf/2108.01133
[34] https://www.sciencedirect.com/science/article/abs/pii/S0040580917300709
[35] https://www.sfu.ca/~kkasa/Recursive_Macroeconomic_Theory_Ljungqvist_Sargent_2018.pdf
[36] https://www.biorxiv.org/content/10.1101/2024.04.06.588423v1.full-text
[37] https://www.asau.ru/files/pdf/2003293.pdf
[38] https://www.researchgate.net/publication/353677607_Asymptotic_behavior_of_the_principal_eigenvalue_and_basic_reproduction_ratio_for_periodic_patch_models
[39] https://www.mmnp-journal.org/articles/mmnp/ref/2018/03/mmnp180035/mmnp180035.html
[40] https://dokumen.pub/recursive-macroeconomic-theory-4nbsped-0262038668-9780262038669.html
[41] https://arxiv.org/pdf/1703.08090
[42] http://www.cecm.sfu.ca/~mmonagan/papers/Leslie3.pdf
[43] https://pmc.ncbi.nlm.nih.gov/articles/PMC6855200
[44] https://cran.r-project.org/web/packages/demogR/demogR.pdf
[45] https://link.springer.com/article/10.1007/s11425-021-1894-2
[46] https://www.researchgate.net/publication/386965728_Net_reproduction_functions_for_nonlinear_structured_population_models
[47] https://jonesor.github.io/BB512_Book/matrix-population-modelling.html
[48] http://ndl.ethernet.edu.et/bitstream/123456789/61534/1/261.pdf
[49] https://www.researchgate.net/publication/49822185_Flexible_Nonhomogeneous_Markov_Models_for_Panel_Observed_Data
