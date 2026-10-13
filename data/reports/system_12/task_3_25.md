# Deep Research Report: grok-4-1-fast-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** cd29f9d7 | **Time:** 25.12s | **Cost:** $0.00739
--------------------------------------------------------------------------------

**In models of intergenerational welfare systems, such as those in overlapping generations (OLG) frameworks, intergenerational transfer matrices capture how resources, welfare levels, or economic states (e.g., consumption, savings, or public debt) propagate from one generation (or cohort) to the next.**[[1]](https://www.sciencedirect.com/science/article/abs/pii/S1090944305000128)[[2]](https://www.rieds-journal.org/rieds/article/download/117/110/216)

**These systems are often represented as discrete-time linear dynamical systems of the form \( \mathbf{x}_{t+1} = T \mathbf{x}_t \), where \( \mathbf{x}_t \) is a state vector (e.g., welfare across cohorts), and \( T \) is the intergenerational transfer matrix incorporating factors like population growth, productivity, taxes, transfers (e.g., PAYG pensions), and savings behavior.**[[3]](https://gfk-cfs.de/media/03_03.pdf)

**Lyapunov stability assesses whether small perturbations around an equilibrium (e.g., steady-state welfare distribution) remain bounded or converge back. For linear systems, this is fully determined by the eigenvalues \( \lambda_i \) of \( T \), which are the roots of its characteristic polynomial \( p(\lambda) = \det(\lambda I - T) = 0 \).**

- **Asymptotic (Lyapunov) stability**: All \( |\lambda_i| < 1 \) (roots strictly inside the unit circle). Trajectories converge exponentially to equilibrium, ensuring welfare sustainability.[[4]](https://arxiv.org/html/2403.13222v1)
- **Lyapunov stability (non-asymptotic)**: All \( |\lambda_i| \leq 1 \), and for any \( \lambda_i \) with \( |\lambda_i| = 1 \), the algebraic multiplicity equals the geometric multiplicity (i.e., Jordan blocks are 1x1; no defective eigenvalues). Perturbations stay bounded but may not converge.[[1]](https://www.sciencedirect.com/science/article/abs/pii/S1090944305000128)
- **Instability**: Any \( |\lambda_i| > 1 \) (roots outside unit circle). Perturbations grow exponentially, leading to welfare divergence (e.g., exploding debt or inequality).[[2]](https://www.rieds-journal.org/rieds/article/download/117/110/216)

**The characteristic polynomial thus encodes stability conditions: stability tests (e.g., Schur-Cohn, Jury criteria) check if all roots lie inside/ on the unit disk without evaluating eigenvalues directly.** In welfare contexts, parameters like transfer rates or growth shift roots; e.g., high population growth may stabilize PAYG systems by pushing roots inward.[[5]](https://www.cmu.edu/sites/default/files/cmu-tepper-site-files/2025-06/2021-economics-moretto-dissertation.pdf)

**For nonlinear extensions, local stability around steady states uses the Jacobian's characteristic polynomial, linking to global welfare properties like convergence in OLG economies.**[[4]](https://arxiv.org/html/2403.13222v1)

## Annotations (Inline Citations)
Citation [1] (Pos: 304-382): [Web] https://www.sciencedirect.com/science/article/abs/pii/S1090944305000128
Citation [2] (Pos: 382-453): [Web] https://www.rieds-journal.org/rieds/article/download/117/110/216
Citation [3] (Pos: 839-880): [Web] https://gfk-cfs.de/media/03_03.pdf
Citation [4] (Pos: 1419-1461): [Web] https://arxiv.org/html/2403.13222v1
Citation [1] (Pos: 1757-1835): [Web] https://www.sciencedirect.com/science/article/abs/pii/S1090944305000128
Citation [2] (Pos: 2011-2082): [Web] https://www.rieds-journal.org/rieds/article/download/117/110/216
Citation [5] (Pos: 2447-2563): [Web] https://www.cmu.edu/sites/default/files/cmu-tepper-site-files/2025-06/2021-economics-moretto-dissertation.pdf
Citation [4] (Pos: 2750-2792): [Web] https://arxiv.org/html/2403.13222v1


## Sources
[1] https://www.jstor.org/stable/1913414
[2] https://web.engr.oregonstate.edu/~webbky/ESE330_files/Section%206%20Time%20Domain%20Analysis.pdf
[3] https://www.princeton.edu/~reddings/papers/SSTD_Paper.pdf
[4] https://www.michael-song.org/uploads/4/8/1/4/48141215/public_debt.pdf
[5] https://users.ssc.wisc.edu/~aseshadr/WorkingPapers/nature_nurture.pdf
[6] https://users.econ.umn.edu/~tkehoe/papers/levine7.pdf
[7] https://link.springer.com/article/10.1007/s40435-025-01758-8
[8] https://mcnp.lanl.gov/pdf_files/TechReport_2016_LANL_LA-UR-16-29043_Brown.pdf
[9] https://www.researchgate.net/publication/394529618_Optimizing_Caregiving_Systems_A_Strategic_Analysis_of_Family_Government_and_Institutional_Interactions
[10] https://www.researchgate.net/publication/293329725_Analysis_of_correlations_and_their_impact_on_convergence_rates_in_Monte_Carlo_eigenvalue_simulations
[11] https://www.research-collection.ethz.ch/bitstreams/dd6d7ba4-ec51-471e-9f39-a0487193e5ef/download
[12] https://perso.amse-aixmarseille.fr/lubrano/cours/Lecture-5-Welfare-Mobility.pdf
[13] https://iopscience.iop.org/article/10.1088/1361-648X/ade2b0
[14] https://cepr.org/system/files/publication-files/WP019.pdf
[15] https://economics.ucr.edu/wp-content/uploads/2019/10/McGough-paper-for-11-18-16-seminar.pdf
[16] https://dspace.mit.edu/bitstream/handle/1721.1/63711/intertemporalsep00keho.pdf?sequence=1
[17] https://pmc.ncbi.nlm.nih.gov/articles/PMC10499553
[18] http://contents2.kocw.or.kr/KOCW/document/2016/kyungpook/yangjeongmin/12.pdf
[19] https://d-nb.info/1276790961/34
[20] http://www.federalreserve.gov/econresdata/ama/documents/css92Paper.pdf
[21] https://arxiv.org/html/2403.13222v1
[22] https://en.wikipedia.org/wiki/Lyapunov_stability
[23] https://pages.uoregon.edu/gevans/NLCW_RPE_revision_22Jan2020.pdf
[24] https://jcmcrimages.org/articles/JCMCRI-1047.pdf
[25] https://www.jstor.org/stable/2951525
[26] https://www.nber.org/digest/nov13/intergenerational-transmission-welfare-dependency
[27] https://www.biorxiv.org/content/10.1101/067793v2.full.pdf
[28] http://users.ntua.gr/igonos/2003/IEEE_CAS1_July2003.pdf
[29] https://pubs.aeaweb.org/doi/abs/10.1257/pol.20190579
[30] https://ideas.repec.org/p/mse/cesdoc/v08028.html
[31] https://www.mdpi.com/2227-7390/11/22/4696
[32] https://link.springer.com/content/pdf/10.1007/978-3-540-24733-3_1.pdf
[33] https://www.research.unipd.it/retrieve/7c62181a-795f-4de3-ada0-1b65a2421bf3/19-27.pdf
[34] https://www.econstor.eu/bitstream/10419/248816/1/jrc120817.pdf
[35] https://www.sciencedirect.com/science/article/abs/pii/S1090944305000128
[36] https://www.ntaccounts.org/doc/repository/L2003.pdf
[37] https://depts.washington.edu/sce2003/Papers/187.pdf
[38] https://www.cmu.edu/sites/default/files/cmu-tepper-site-files/2025-06/2021-economics-moretto-dissertation.pdf
[39] https://shs.hal.science/halshs-04850529v1/document
[40] https://www.sciencedirect.com/science/article/pii/S0276562422000403
[41] https://www.science.gov/topicpages/c/concurrent+triangulation+strategy.html
[42] https://www.ipme.ru/ipme/labs/ccs/alf/f_at74.pdf
[43] https://engineering.purdue.edu/~byao/Research/Supplements/Lyapunov.pdf
[44] http://dsbaero.engin.umich.edu/wp-content/uploads/sites/441/2020/06/ExplicitQuadraticPart2DT.pdf
[45] https://core.ac.uk/download/pdf/276286690.pdf
[46] https://faculty.washington.edu/chx/teaching/me547/2_1_stability_slides_Lyapunov_light.pdf
[47] https://pmc.ncbi.nlm.nih.gov/articles/PMC7644086
[48] https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/cth2.12224
[49] https://academic.oup.com/ej/article/135/669/1609/8030529
[50] https://gattonweb.uky.edu/Faculty/Ziliak/TANFIGE_Revision_050719.pdf
[51] https://openaccess.city.ac.uk/id/eprint/30768/1/Zimbidis%20thesis%201999%20PDF-A.pdf
[52] https://www.jstor.org/stable/134261
[53] https://www.researchgate.net/publication/262277582_A_computationally_faster_algorithm_to_test_the_stability_of_characteristic_polynomials
[54] https://sites.cs.ucsb.edu/~omer/DOWNLOADABLE/stable10.pdf
[55] https://www.researchgate.net/figure/Eigenfunction-corresponding-to-the-eigenvalue-E-62-5100-meV_fig5_221917239
[56] https://www.economics.ku.dk/research/publications/wp/dp_2009/0905.pdf
[57] https://www.nature.com/articles/s41598-023-29097-8
[58] https://www.researchgate.net/publication/343609366_The_Lorenz_system_hidden_boundary_of_practical_stability_and_the_Lyapunov_dimension
[59] https://www.pseweb.eu/ydepot/semin/texte0910/DAL2009CON.pdf
[60] https://www.rieds-journal.org/rieds/article/download/117/110/216
[61] https://www.economics.uci.edu/files/docs/faculty_review/fhl_2012_wpv.pdf
[62] https://academic.oup.com/joeg/article/15/1/1/960842
[63] https://gfk-cfs.de/media/03_03.pdf
[64] https://ijssrr.com/journal/article/download/2779/1995
[65] https://arxiv.org/abs/2310.20605
[66] https://arxiv.org/pdf/1301.4881
[67] https://www.matec-conferences.org/articles/matecconf/pdf/2017/27/matecconf_er2017_01003.pdf
[68] https://pmc.ncbi.nlm.nih.gov/articles/PMC4689204
[69] https://scispace.com/pdf/a-unified-structural-interpretation-of-some-well-known-1roxb5y7nk.pdf
[70] https://dspace.mit.edu/bitstream/handle/1721.1/74611/6-241-fall-2003/contents/recitations/rec6.pdf
[71] https://www.scirp.org/journal/paperinformation?paperid=65005
[72] http://gabriel-zucman.eu/files/teaching/Modigliani88
[73] https://pmc.ncbi.nlm.nih.gov/articles/PMC11214050
[74] https://onlinelibrary.wiley.com/doi/pdf/10.3982/TE3752
[75] https://www.sciencedirect.com/science/article/pii/S1470160X24014201
[76] https://www.sciencedirect.com/science/article/abs/pii/S0378437108008996
[77] https://www.sciencedirect.com/science/article/pii/S0952197625023280
[78] https://www.sciencedirect.com/science/article/abs/pii/S0960077923002783
