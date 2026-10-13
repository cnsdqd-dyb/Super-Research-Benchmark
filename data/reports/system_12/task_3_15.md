# Deep Research Report: grok-4-1-fast-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 61c36742 | **Time:** 57.53s | **Cost:** $0.01003
--------------------------------------------------------------------------------

**In stochastic models of international migration flows (often framed as Markov processes or population projection models), migration dynamics are captured by nonnegative matrices—such as transition matrices \(P\) (where \(P_{ij}\) represents the probability or rate of flow from origin \(i\) to destination \(j\)) or composite projection matrices incorporating fertility, survival, and migration components.**

**The spectral radius \(\rho(A)\) of such a matrix \(A\) is the largest absolute eigenvalue, which, by the Perron-Frobenius theorem (for irreducible nonnegative \(A\)), is a positive real eigenvalue determining long-term behavior:**
- For row-stochastic transition matrices (rows sum to 1, modeling conserved flows like probabilities), \(\rho(P) = 1\), corresponding to a stationary distribution.[[1]](https://en.wikipedia.org/wiki/Stochastic_matrix)[[2]](https://direct.mit.edu/neco/article/35/11/1713/117578/A-Tutorial-on-the-Spectral-Theory-of-Markov-Chains)
- In growth-oriented projection matrices (e.g., Leslie-type with migration \(M\), fertility \(F\), survival \(S\): \(A = F + S + M\)), \(\rho(A)\) equals the asymptotic population growth rate (\(\lambda = \rho(A)\)).[[3]](http://homepages.math.uic.edu/~friedlan/Friedland_Karlin.1975.pdf)[[4]](https://dynamics.org/~altenber/LIBRARY/REPRINTS/Karlin_Classifications.1982.pdf)

**Policy parameters** (e.g., visa quotas, economic incentives, or border controls) enter these models by modulating matrix entries—such as bilateral migration rates \(m_{ij}\) or out-migration probabilities. These introduce **perturbations \(\delta A\)** to the baseline matrix \(A\), often stochastically (e.g., via perturbed distributions in flow sampling).

**Effects on the spectral radius:**
1. **Continuity and first-order perturbation**: \(\rho(A + \delta A)\) is continuous in the entries. For small perturbations, the change is
   \[
   \delta \rho \approx \frac{\mathbf{v}^T (\delta A) \mathbf{u}}{\mathbf{v}^T \mathbf{u}},
   \]
   where \(\mathbf{u}, \mathbf{v}\) are the right and left Perron eigenvectors (normalized with \(\mathbf{v}^T \mathbf{u} = 1\)). Positive perturbations aligned with \(\mathbf{u}_j \mathbf{v}_i > 0\) increase \(\rho\); otherwise, they decrease it.[[6]](https://perso.uclouvain.be/paul.vandooren/publications/BerkhoutHV23.pdf)

2. **Stochastic case**: In fully stochastic models (e.g., random draws from skew-t or Weibull distributions for flows), policy shifts parameters like means \(\mu\) or variances \(\sigma^2\) in flow generators, leading to ensemble variability in \(\rho\). Increased variance (e.g., via policy shocks) can widen the distribution of \(\rho\), potentially pushing it above/below thresholds like 1 for growth/persistence.

3. **Specific impacts**:
   - **Restrictive policies** (↓ \(m_{ij}\)): Often decrease \(\rho\) in growth models by reducing effective connectivity or net inflows to high-fertility regions; preserves \(\rho=1\) if normalized.[[7]](https://www.biorxiv.org/content/10.1101/2023.04.23.537980v2.full-text)
   - **Liberal policies** (↑ \(m_{ij}\)): Can increase \(\rho > 1\) if enhancing cycles or flows to growing demes, promoting instability/explosion in unnormalized models.[[8]](https://lab.rockefeller.edu/cohenje/assets/file/466WebbTaylorsLawExponentiallyGrowingLocalPopulationsLinkedByMigrationTheorPopBiol2023.pdf)
   - **Irreducibility**: Strong perturbations might fragment the matrix (introduce zeros), splitting \(\rho\) into block-maxima, altering global dynamics.[[9]](https://dynamics.org/Altenberg/FILES/Altenberg_KarlinTheory.2010.pdf)

**Examples from literature**:
- Population genetics/demography: Perturbing migration \(M\) in \(MD\) (selection \(D\)) changes \(\rho(MD)\), with bounds like \(\rho(MD) \geq \rho(M) \min d_i\).[[3]](http://homepages.math.uic.edu/~friedlan/Friedland_Karlin.1975.pdf)
- Recent stochastic migration forecasts: Policies perturb flow parameters, improving hindcasts but indirectly via ensemble \(\rho\) variability.

Overall, effects are directionally sensitive to eigenvector structure, with stochasticity amplifying uncertainty in long-term flow stability/growth.[[10]](https://www.cambridge.org/core/journals/journal-of-applied-probability/article/persistence-of-spectral-projections-for-stochastic-operators-on-large-tensor-products/D587DAA0F48217E9544B81425ADF53F5)

## Annotations (Inline Citations)
Citation [1] (Pos: 808-862): [Web] https://en.wikipedia.org/wiki/Stochastic_matrix
Citation [2] (Pos: 862-973): [Web] https://direct.mit.edu/neco/article/35/11/1713/117578/A-Tutorial-on-the-Spectral-Theory-of-Markov-Chains
Citation [3] (Pos: 1190-1262): [Web] http://homepages.math.uic.edu/~friedlan/Friedland_Karlin.1975.pdf
Citation [4] (Pos: 1262-1348): [Web] https://dynamics.org/~altenber/LIBRARY/REPRINTS/Karlin_Classifications.1982.pdf
Citation [6] (Pos: 2237-2315): [Web] https://perso.uclouvain.be/paul.vandooren/publications/BerkhoutHV23.pdf
Citation [7] (Pos: 2959-3035): [Web] https://www.biorxiv.org/content/10.1101/2023.04.23.537980v2.full-text
Citation [8] (Pos: 3206-3351): [Web] https://lab.rockefeller.edu/cohenje/assets/file/466WebbTaylorsLawExponentiallyGrowingLocalPopulationsLinkedByMigrationTheorPopBiol2023.pdf
Citation [9] (Pos: 3506-3581): [Web] https://dynamics.org/Altenberg/FILES/Altenberg_KarlinTheory.2010.pdf
Citation [3] (Pos: 3776-3848): [Web] http://homepages.math.uic.edu/~friedlan/Friedland_Karlin.1975.pdf
Citation [10] (Pos: 4143-4348): [Web] https://www.cambridge.org/core/journals/journal-of-applied-probability/article/persistence-of-spectral-projections-for-stochastic-operators-on-large-tensor-products/D587DAA0F48217E9544B81425ADF53F5


## Sources
[1] https://www.ressources-actuarielles.net/EXT/ISFA/1226.nsf/8d48b7680058e977c1256d65003ecbb5/839ca4f948fc4c75c1257e7b004cdb96/$FILE/Manuscript_WP_20150720.pdf
[2] https://mathoverflow.net/questions/442696/spectral-radius-and-spectral-norm-for-markov-operators
[3] https://www.oeaw.ac.at/fileadmin/subsites/Institute/VID/PDF/Conferences/2022_Climate_Change/Poster/Extended_Abstract_Poster_WIC2022_Zantout_International_migration_model.pdf
[4] https://upcommons.upc.edu/bitstreams/ef8f7de9-37b8-4e60-9252-00a00c8fb115/download
[5] https://files01.core.ac.uk/download/pdf/162459607.pdf
[6] https://www.nature.com/articles/hdy198013.pdf
[7] https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1558-5646.1991.tb04395.x
[8] https://nhigham.com/2024/01/12/what-is-the-spectral-radius-of-a-matrix
[9] https://dynamics.org/Altenberg/FILES/Altenberg_KarlinTheory.2010.pdf
[10] https://austriaca.at/0xc1aa5572%200x003fa445.pdf
[11] https://www.biorxiv.org/content/10.1101/2023.04.23.537980v1.full-text
[12] https://ojs.aaai.org/index.php/AAAI/article/view/5791
[13] https://www.nber.org/system/files/working_papers/w22572/revisions/w22572.rev11.pdf
[14] https://www.sciencedirect.com/science/article/pii/S0022519325002516?dgcid=rss_sd_all
[15] https://marcos-marva.web.uah.es/papers/thesis-marva-web.pdf
[16] https://en.wikipedia.org/wiki/Spectral_radius
[17] http://homepages.math.uic.edu/~friedlan/Friedland_Karlin.1975.pdf
[18] https://www.sciencedirect.com/topics/computer-science/spectral-radius
[19] https://direct.mit.edu/neco/article/35/11/1713/117578/A-Tutorial-on-the-Spectral-Theory-of-Markov-Chains
[20] https://www.cambridge.org/core/journals/journal-of-applied-probability/article/persistence-of-spectral-projections-for-stochastic-operators-on-large-tensor-products/D587DAA0F48217E9544B81425ADF53F5
[21] https://researchdatabase.minneapolisfed.org/downloads/vd66w017s
[22] https://epubs.siam.org/doi/10.1137/130906179
[23] https://www.researchgate.net/publication/374705194_Stochastic_evolution_model_for_international_migration
[24] https://pubsonline.informs.org/doi/pdf/10.1287/moor.9.1.6
[25] https://lab.rockefeller.edu/cohenje/assets/file/466WebbTaylorsLawExponentiallyGrowingLocalPopulationsLinkedByMigrationTheorPopBiol2023.pdf
[26] https://www.biorxiv.org/content/10.1101/2023.04.23.537980v2.full-text
[27] https://tc.copernicus.org/articles/19/5423/2025
[28] https://hal.science/hal-03179136v1/file/version_Arxiv.pdf
[29] https://link.springer.com/article/10.1007/s11538-022-01057-9
[30] https://pmc.ncbi.nlm.nih.gov/articles/PMC12503288
[31] https://par.nsf.gov/servlets/purl/10333067
[32] https://www.researchsquare.com/article/rs-3438544/v2.pdf?c=1705709704000
[33] https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210X.14111
[34] https://www.demographic-research.org/volumes/vol18/14/18-14.pdf
[35] https://www.ejpam.com/index.php/ejpam/article/view/5637/1889
[36] https://www.researchgate.net/publication/380935208_Matrix_Low-Rank_Approximation_For_Policy_Gradient_Methods
[37] https://userweb.ucs.louisiana.edu/~xxw6637/papers/CAMQ2011.pdf
[38] https://journals.sagepub.com/doi/10.1177/09217134251319159
[39] http://papers.neurips.cc/paper/1748-policy-search-via-density-estimation.pdf
[40] https://www.researchgate.net/publication/396617959_MATHEMATICAL_ANALYSIS_OF_STOCHASTIC_TRANSITION_MATRICES_IN_MARKOV_MODELS_USING_MONTE_CARLO_AND_MCMC_SIMULATION
[41] http://www.cse.buffalo.edu/~demirbas/publications/migration.pdf
[42] https://www.sciencedirect.com/science/article/abs/pii/S0378426604001050
[43] https://ideas.repec.org/a/plo/pone00/0332886.html
[44] https://pmc.ncbi.nlm.nih.gov/articles/PMC8750699
[45] https://dc.etsu.edu/cgi/viewcontent.cgi?article=6183&context=etd
[46] https://math.ethz.ch/sfs/education/master-theses.html
[47] https://ieeexplore.ieee.org/document/10610966
[48] https://www.nber.org/system/files/working_papers/w29101/revisions/w29101.rev0.pdf
[49] https://arxiv.org/pdf/1907.13631
[50] https://www.researchgate.net/publication/396279416_Stochastic_evolution_model_for_international_migration
[51] https://publications.pik-potsdam.de/pubman/item/item_32960_1/component/file_33024/32960oa.pdf
[52] https://dynamics.org/~altenber/LIBRARY/REPRINTS/Karlin_Classifications.1982.pdf
[53] http://proceedings.mlr.press/v119/ghosh20b/ghosh20b-supp.pdf
[54] https://royalsocietypublishing.org/doi/10.1098/rspa.2011.0236
[55] https://perso.uclouvain.be/paul.vandooren/publications/BerkhoutHV23.pdf
[56] https://math.stackexchange.com/questions/1010822/continuity-of-eigenvalues-and-spectral-radius-for-a-general-matrix
[57] https://projecteuclid.org/journals/annales-de-linstitut-henri-poincare-probabilites-et-statistiques/volume-56/issue-3/Spectral-radii-of-sparse-random-matrices/10.1214/19-AIHP1033.pdf
[58] https://lab.rockefeller.edu/cohenje/assets/file/444AltenbergCohenNonconcavityLevingersFunctionLinAlgApplic2020.pdf
[59] https://pubmed.ncbi.nlm.nih.gov/41056339
[60] https://cepr.org/system/files/publication-files/WP019.pdf
[61] https://www.princeton.edu/~reddings/papers/SSTD_Paper.pdf
[62] http://users.stat.umn.edu/~jiang040/papers/Spectral_radius_07_08_2015.pdf
[63] https://iab.de/en/modeling-migration-dynamics-in-stochastic-labor-supply-forecasting
[64] https://www.sciencedirect.com/science/article/abs/pii/S0022039625002116
[65] https://journals.ametsoc.org/view/journals/mwre/149/5/MWR-D-20-0077.1.xml
[66] https://www.aimsciences.org/article/doi/10.3934/eect.2025021
[67] https://mathworld.wolfram.com/SpectralRadius.html
[68] https://mathoverflow.net/questions/35445/estimating-the-spectral-radius-of-a-matrix-noniteratively
[69] https://www.sciencedirect.com/science/article/abs/pii/S0022169422014196
[70] https://en.wikipedia.org/wiki/Stochastic_matrix
