# Deep Research Report: perplexity/sonar-deep-research
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 3e2feb28 | **Time:** 74.87s | **Cost:** $1.18713
--------------------------------------------------------------------------------

# Balancing Convergence Speed and Estimation Accuracy in Numerical Solutions to the Heston Model: The Role of Grid Density in Finite Difference Methods

This report examines the fundamental tension between computational efficiency and numerical accuracy when solving the Heston stochastic volatility model using finite difference methods, with particular attention to how grid density selection affects long-term option pricing performance. Through analysis of recent literature and computational methodologies, we demonstrate that grid density selection does introduce significant systematic errors in long-term pricing, yet this challenge can be substantially mitigated through careful scheme selection, adaptive meshing, and hybrid computational approaches.

## The Heston Model and Its Computational Challenges

The Heston stochastic volatility model represents a significant advancement in option pricing theory beyond the Black-Scholes framework by explicitly modeling volatility as a time-varying stochastic process rather than assuming it to be constant.[25][26] The model governs asset price dynamics through a coupled system of stochastic differential equations where the asset price follows geometric Brownian motion while the variance follows a mean-reverting process with its own volatility. This two-dimensional nature of the problem introduces substantial computational complexity that requires careful numerical treatment.[1][7]

The governing partial differential equation (PDE) for the Heston model contains a mixed derivative term arising from the correlation between the two underlying stochastic processes for asset price and variance.[4][31] This mixed derivative term, which does not exist in the simpler one-dimensional Black-Scholes case, creates specific numerical challenges that affect both the choice of discretization scheme and the stability properties of any numerical method applied to solve the problem. The need for accurate option pricing in real-world trading environments, combined with the computational intensity of solving the Heston PDE, has motivated substantial research into developing efficient and accurate numerical methods that can balance these competing demands.[1][7][20]

## Finite Difference Methods: Scheme Selection and Convergence Behavior

Finite difference methods solve the Heston PDE by discretizing both the spatial dimensions (asset price and variance) and the time dimension into a regular grid structure.[2][4][8] The fundamental idea involves replacing continuous derivatives with finite difference approximations, transforming the continuous PDE into a system of algebraic equations that can be solved sequentially through time.[2][14] Three primary finite difference schemes are commonly employed for option pricing: the explicit scheme, the implicit scheme, and the Crank-Nicolson scheme, each representing different trade-offs between computational intensity and numerical stability.[2][14][15]

The explicit scheme operates forward in time by computing the option value at the next time step directly from values at the current time step using a straightforward algebraic formula.[2][14] This scheme is conceptually simple and computationally efficient per time step, requiring only \(O(m)\) operations where \(m\) is the number of spatial grid points.[2][31] However, the explicit scheme suffers from a critical limitation: it must satisfy the Courant-Friedrichs-Lewy (CFL) stability condition, which severely restricts the allowable time step size.[2][39] For the Black-Scholes-type equations governing option pricing, this condition requires that \(\Delta t \leq \frac{(\Delta S)^2}{2\sigma^2 S_{\max}^2}\), where \(\Delta t\) is the time step and \(\Delta S\) is the spatial grid spacing.[2][39] This restrictive constraint means that refining the spatial grid to improve accuracy requires proportionally reducing the time step, dramatically increasing the total computational burden.[2][15]

The implicit scheme addresses the CFL stability limitation by using information from the future time level to compute the current solution, resulting in unconditional stability that removes the restrictive time step constraint.[2][14][15] This fundamental advantage allows the implicit scheme to use much larger time steps than the explicit method without sacrificing stability.[2] However, the implicit scheme requires solving a tridiagonal linear system at each time step, increasing computational cost per iteration, and demonstrates only first-order convergence in time, meaning the time discretization error decreases slowly as the time step is reduced.[2][14]

The Crank-Nicolson scheme represents an optimal balance between stability and accuracy by averaging the explicit and implicit schemes, employing information from both the current and future time levels in a symmetric manner.[2][14][15] This scheme is unconditionally stable, eliminating the CFL constraint, and achieves second-order convergence in both time and space, cutting the time discretization error to \(O(\Delta t^2)\) rather than \(O(\Delta t).[4][14][15] The Crank-Nicolson scheme therefore allows larger time steps while maintaining superior convergence properties compared to the implicit scheme.[2][14] For the Heston model specifically, convergence analysis shows that the Crank-Nicolson scheme achieves error behavior of \(\|u(\tau_n) - U_h^n\|_0 = O(h^{k+1} + \Delta \tau^2)\) where \(k\) denotes the polynomial degree of the finite element basis and \(\Delta \tau\) is the time step.[4]

## Grid Density Selection and Its Effect on Convergence

The selection of spatial grid density, characterized by the spacing parameters \(\Delta S\) and \(\Delta v\), fundamentally determines both the accuracy of the numerical solution and the computational cost required to achieve that accuracy.[2][14][31] Finer grids with smaller spacing provide more accurate solutions by reducing the truncation error from discretizing the continuous derivatives.[2][14] The relationship between grid spacing and error magnitude is governed by the order of the discretization scheme; for second-order schemes commonly used in option pricing, the spatial discretization error scales as \(O((\Delta S)^2 + (\Delta v)^2)\).[2][14]

However, grid refinement introduces a critical complication for long-term option pricing: as spatial grids become finer to capture the behavior near the strike price where option values change most rapidly, the CFL constraint (applicable to explicit schemes) or computational cost (for implicit schemes) increases substantially.[2][14][39] Additionally, finer grids can amplify other sources of error, particularly oscillatory behavior in the numerical solution at certain parameter regimes.[55] Research demonstrates that standard centered-difference schemes applied to Black-Scholes type equations with small volatility or large drift factors can produce spurious oscillations that contaminate the solution, particularly when approximating first-order derivatives.[55] These oscillations become more pronounced when spatial grids are insufficiently refined in regions of rapid solution variation.[55]

The challenge becomes more acute for long-term option pricing where the solution must be computed over an extended time interval. For a European option with maturity \(T\), a uniform grid with \(N\) time steps requires \(\Delta t = T/N\), meaning longer maturities demand either proportionally more time steps or acceptance of larger time steps that degrade accuracy.[2][9] The interplay between spatial and temporal discretization creates a multidimensional optimization problem: refinement in one direction requires corresponding adjustments in others to maintain stability and accuracy.[2][14]

Non-uniform grids can partially mitigate these challenges by concentrating grid points in regions of interest, particularly around the strike price where the solution varies most rapidly and near the expiry date where temporal dynamics are most complex.[2][14][29] Non-uniform grids provide flexibility to achieve high accuracy in critical regions without computational expense in less important regions.[2][14] However, implementing non-uniform grids complicates the finite difference approximations and introduces additional truncation error from the varying grid spacing.[2][14] The adaptive mesh refinement (AMR) approach systematically identifies regions requiring higher resolution based on local error estimates and automatically refines grids accordingly.[24] Studies using AMR for option pricing demonstrate substantial computational savings while maintaining accuracy, suggesting that static non-uniform grids represent a middle ground between uniform grids and fully adaptive approaches.[21]

## Long-Term Pricing: Error Accumulation and Scheme Selection

Long-term option pricing presents distinct challenges compared to near-maturity options because errors accumulate over extended time integration.[9] The relationship between option properties (time to expiration, moneyness, volatility levels) and numerical accuracy in deep learning methods shows that longer times to expiration can cause coarser grids and deteriorate accuracy, particularly when near-maturity instability dominates the error budget.[9] For very short maturities, numerical instability increases due to the non-smooth payoff function at expiration, while for longer maturities, error sources shift toward the accumulation of discretization errors over many time steps.[9]

Richardson extrapolation provides a systematic technique to estimate and reduce truncation errors in finite difference solutions.[32][48] This method uses solutions computed on multiple grids with different spacings to estimate the leading-order error term and construct higher-order accurate approximations without requiring finer grids.[32][48] For example, combining explicit scheme solutions computed with time steps \(\Delta t\) and \(\Delta t/2\) can reduce time discretization error from \(O(\Delta t)\) to \(O(\Delta t^2).[32][48] The power of Richardson extrapolation for long-term pricing lies in its ability to improve accuracy without proportionally increasing computational cost, though its application assumes the discretization error follows a regular asymptotic expansion, which may be violated near singularities or discontinuities.[32]

The phenomenon of "ghost calibration" demonstrates that seemingly accurate pricing methods can systematically overestimate or underestimate option prices in ways that remain hidden until more accurate pricer comparisons are performed.[3] Naive applications of popular numerical methods with fixed, non-optimal parameters lead to numerical inaccuracies that systematically offset model specification errors, producing calibrations that appear excellent when compared to market data but fail when tested against more accurate pricing methods.[3] This risk is particularly acute for long-term options where accumulated numerical errors can become substantial. The SINH-CB (hyperbolic sine conformal bootstrap) method addresses this challenge for Fourier inversion-based pricing by using adaptive acceleration and the conformal bootstrap principle to select numerical parameters automatically, achieving relative errors below \(10^{-4}\) even for short-maturity deep out-of-the-money options and moderate or long-maturity options in milliseconds on standard hardware.[3][29]

## Sources of Error in Long-Term Heston Pricing

Multiple error sources conspire to challenge numerical accuracy in long-term option pricing under the Heston model. Discretization errors arise from replacing continuous derivatives with finite differences, truncation errors from replacing infinite domains with finite computational grids, and accumulation of rounding errors over many time steps.[2][9][18] For the Heston model specifically, the error in implied volatility surface reconstruction from calibrated parameters depends critically on pricing accuracy; mean absolute errors below one basis point in implied volatility are often achieved in well-designed finite difference schemes but require careful grid and time step selection.[1]

The relationship between time steps and error magnitude is fundamentally important for long-term pricing. Analysis of deep learning methods for option pricing reveals that there exists a particularly strong linear relationship between \(1/\sqrt{\text{time steps}}\) and pricing error, confirming that the number of time steps directly impacts solution quality.[9] This suggests that time discretization dominates spatial discretization errors in many practical scenarios. For the Heston model, the convergence analysis shows that total error scales as \(O(\Delta t^2 + (\Delta S)^2 + (\Delta v)^2)\) for the Crank-Nicolson scheme with second-order spatial differences,[4] indicating that balancing temporal and spatial discretization is crucial.

The Feller condition, which constrains the Heston model parameters to ensure positivity of the variance process, affects numerical stability and convergence behavior.[8] When the Feller condition is satisfied with room to spare, numerical solutions are stable and convergent; when it is violated, approximating the boundary conditions at zero variance becomes more delicate and may require specialized treatment to avoid negative variance realizations or spurious oscillations.[8]

## Machine Learning and Neural Network Approaches

Recent advances in applying neural networks to Heston model calibration and pricing demonstrate that the convergence-accuracy trade-off can be fundamentally transformed through learning-based approximations.[1][7][20] The universal approximation theorem guarantees that neural networks with sufficient width and depth can approximate any continuous function, providing a mechanism to replace explicit numerical discretization with learned function approximations.[1] A concrete case study using neural networks for Heston calibration demonstrated that a network with approximately 750,000 trainable parameters, trained on 32 million synthetic samples, achieves mean absolute error of approximately 0.1 implied volatility basis points and maximum error of 5 basis points over out-of-sample test sets.[1]

The critical insight is that once trained offline, neural network approximations enable extremely fast calibration: the network can evaluate option prices for any parameters in milliseconds, enabling rapid optimization of Heston parameters to fit market data.[1][7][20] A hybrid approach integrating two neural networks—the Price Approximator Network (PAN) approximating option prices and the Calibration Correction Network (CCN) refining the Heston model output—demonstrated superior generalization compared to traditional calibration techniques on real S&P 500 option data.[7][20] This approach achieves faster convergence with better out-of-sample performance than conventional methods.[7]

However, neural network approaches introduce their own challenges. Reliance on historical implied volatility data for training creates overfitting risks, particularly for options with characteristics outside the training distribution or during market regime shifts requiring frequent retraining.[7][20] The interpretability of neural network pricing remains limited compared to traditional PDE-based methods, though the combination of neural networks with traditional models provides interpretability while retaining computational benefits.[7][20]

## Adaptive and High-Order Methods

Alternating Direction Implicit (ADI) schemes provide a sophisticated approach to handling the mixed derivative term in the Heston PDE while maintaining unconditional stability and computational efficiency.[16][31][34] The Craig-Sneyd and Modified Craig-Sneyd schemes decouple the two-dimensional problem into sequences of one-dimensional problems, each solved implicitly but requiring only \(O(m)\) operations per time step through efficient tridiagonal solvers.[16][31] For the Heston PDE with mixed derivative terms, the second-order Craig-Sneyd scheme is unconditionally stable when the free parameter satisfies \(\theta \geq 1/2\).[16][31]

Compact finite difference schemes offer fourth-order spatial accuracy while using the same nine-point computational stencil as standard second-order schemes, achieving higher accuracy without additional computational burden per iteration.[11] A compact high-order scheme for the Heston model achieves fourth-order accuracy in space and second-order accuracy in time, as confirmed by numerical convergence studies.[11] The theoretical convergence rate shows that as grids are refined, the global error decreases as \(O(h^4 + \Delta t^2)\),[11] substantially outperforming standard second-order schemes.[11]

Spectral element methods and high-order finite element methods provide exponential convergence rates for smooth solutions by using high-degree polynomial basis functions on each element.[27][30][59] The hp-finite element method combines mesh refinement (h-refinement) with polynomial order increase (p-refinement), achieving exponential convergence for solutions with known singularities at specific locations.[59] These methods require fewer degrees of freedom than low-order methods to achieve target accuracy, potentially providing substantial computational savings for long-term pricing problems where solution smoothness is maintained away from the strike price.[27][30][59]

## The Reality of Grid Density Trade-offs

The empirical evidence strongly supports that grid density selection does introduce significant systematic errors in long-term option pricing, particularly when grids are too coarse.[1][14][55] A comparative study of European option pricing using Crank-Nicolson schemes demonstrates that the method achieves accuracy comparable to implicit schemes when both are applied with appropriate grid refinement.[14] However, the cost of achieving production-level accuracy varies substantially depending on grid configuration. The mean absolute error of approximately 0.1 implied volatility basis points achieved through neural network calibration[1] contrasts with errors of 5-10 basis points commonly achievable with conventional finite difference methods using standard grid densities,[1][44] suggesting that conventional approaches require either more careful grid design or acceptance of lower accuracy.

For long-term options, the accumulated effect of discretization errors becomes particularly pronounced. While short-term option pricing (approaching maturity) benefits from natural temporal resolution as the remaining time interval becomes smaller, long-term pricing requires either maintaining small time steps (increasing computational cost substantially) or accepting larger errors.[9] The trade-off cannot be eliminated entirely through grid refinement alone; rather, strategic choices in discretization scheme, use of adaptive meshing, and consideration of the particular characteristics of the option being priced are essential.[14]

The explicit scheme's CFL constraint creates a particularly severe convergence-speed dilemma for long-term pricing: refining spatial grids to improve accuracy in capturing volatility smile effects requires proportionally reducing time steps, creating a quadratic computational penalty that becomes prohibitive for extensive grid refinement.[2][39] The implicit and Crank-Nicolson schemes eliminate this constraint, allowing larger time steps, but the implicit scheme's first-order temporal convergence makes it unsuitable for long-term pricing where temporal accuracy becomes critical.[14][15] The Crank-Nicolson scheme thus becomes the natural choice for long-term pricing, allowing both unconditional stability and second-order temporal convergence with manageable computational cost.

## Practical Recommendations and Conclusion

Achieving both adequate convergence speed and estimation accuracy in long-term Heston model pricing requires a systematic approach balancing multiple design choices. First, scheme selection should prioritize the Crank-Nicolson or Craig-Sneyd ADI schemes for their superior stability and convergence properties, reserving explicit schemes only when computational simplicity is paramount and time step restrictions are acceptable.[2][15][31] Second, spatial grid design should employ non-uniform meshing with increased density around the strike price where solution gradients are steepest, potentially using formal adaptive mesh refinement for production systems where accuracy guarantees are essential.[14][31]

Third, temporal discretization should be driven by the specific option maturity and volatility characteristics; longer-maturity options benefit from careful time step selection or techniques like Richardson extrapolation that improve accuracy without proportionally increasing cost.[32][48] Fourth, for applications requiring extreme accuracy (such as trading desks or risk management), hybrid approaches combining traditional PDE-based numerical methods with neural network surrogates offer compelling advantages by learning the solution structure from offline computation and enabling real-time evaluation.[1][7][20] Finally, grid selection validation through convergence studies—computing solutions on progressively finer grids and confirming that results approach a stable limit—provides empirical evidence that grid density is adequate.[4][14]

The fundamental reality is that grid density selection in finite difference methods does introduce significant errors, particularly for long-term option pricing, but these errors are manageable through careful methodology. The balance between convergence speed and accuracy is not fixed but rather depends on the specific requirements: production trading systems might accept a small increase in computation time to achieve lower errors through refined grids and improved schemes, while research or exploratory applications might accept higher errors to minimize computation. The emergence of neural network and machine learning approaches suggests that the traditional finite difference paradigm may be supplemented or even replaced for production systems, where learning-based methods can achieve superior accuracy-speed trade-offs by eliminating the need for explicit discretization while providing fast inference once trained.

## Annotations
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'high accuracy approximations. Case study: Heston calibration', 'url': 'https://www.acenumerics.com/miscellaneous/neural-networks-in-quant-finance-for-high-accuracy-approximations-first-case-study-stochastic-volatility-model-calibration-heston'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Finite Difference Methods for Option Pricing: PDE Solutions', 'url': 'https://mbrenndoerfer.com/writing/finite-difference-methods-option-pricing-numerical-pde'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Fast reliable pricing and calibration of the rough Heston model - arXiv', 'url': 'https://arxiv.org/html/2508.15080v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] High Accuracy Finite Element Methods for Option Pricing under ...', 'url': 'https://people.math.sc.edu/Burkardt/publications/cbg_sub_2014.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Finite Difference Methods for Option Pricing under Lévy Processes', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3893018/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'What is the Heston model in finance? - StoneX', 'url': 'https://www.stonex.com/en/financial-glossary/heston-model/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Deep Learning-Enhanced Calibration of the Heston Model - arXiv', 'url': 'https://arxiv.org/html/2510.24074v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Finite Difference Methods in Derivatives Pricing under Stochastic ...', 'url': 'https://math.leidenuniv.nl/scripties/MasterdeGraaf.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Error Analysis of Option Pricing via Deep PDE Solvers - arXiv', 'url': 'https://arxiv.org/pdf/2311.07231.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Convergence analysis of the discrete duality finite volume scheme ...', 'url': 'https://www.aimsciences.org/article/doi/10.3934/dcdss.2020226'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': "[PDF] Compact finite difference scheme for option pricing in Heston's model", 'url': 'https://bduring.warwick.ac.uk/pdf/xabs_duering.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Numerical methods for option pricing', 'url': 'https://oa.upm.es/21942/1/TESIS_MASTER_IGOR_VIDIC.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] High Accuracy Finite Element Methods for Option Pricing under ...', 'url': 'https://people.math.sc.edu/Burkardt/publications/cbg_sub_2014.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Finite Difference Methods for Option Pricing: PDE Solutions', 'url': 'https://mbrenndoerfer.com/writing/finite-difference-methods-option-pricing-numerical-pde'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Finite difference method - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Finite_difference_method'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] ADI finite difference schemes for option pricing in the Heston model ...', 'url': 'https://www.math.ualberta.ca/ijnam/Volume-7-2010/No-2-10/2010-02-06.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Numerical Methods for Solving PDEs in Finance: Finite Difference ...', 'url': 'https://acr-journal.com/article/download/pdf/1265/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Truncation Error Analysis - Hans Petter Langtangen', 'url': 'https://hplgit.github.io/INF5620/doc/pub/main_trunc-A4.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Fast Calibration in the Heston Model', 'url': 'https://fam.tuwien.ac.at/~sgerhold/pub_files/theses/bauer.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Deep Learning-Enhanced Calibration of the Heston Model - arXiv', 'url': 'https://arxiv.org/html/2510.24074v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Adaptive tree techniques in option pricing - Diva-portal.org', 'url': 'https://www.diva-portal.org/smash/get/diva2:813620/FULLTEXT01.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Theoretical and Empirical Validation of Heston Model - arXiv', 'url': 'https://arxiv.org/html/2409.12453v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Pricing Power Options under the Heston Dynamics using the FFT', 'url': 'https://www.ntmsci.com/ajaxtool/GetArticleByPublishedArticleId?PublishedArticleId=1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Adaptive Mesh Refinement for Computational Aeroacoustics', 'url': 'http://www2.coe.pku.edu.cn/tpic/2010823112544527.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Heston Model: Options Pricing, Python Implementation and ...', 'url': 'https://blog.quantinsti.com/heston-model/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] High Accuracy Finite Element Methods for Option Pricing under ...', 'url': 'https://people.math.sc.edu/Burkardt/publications/cbg_sub_2014.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A New Spectral Element Method for Pricing European Options ...', 'url': 'https://www.math.purdue.edu/~shen7/pub/CSY11.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '1.4 SDE - Heston model.ipynb - GitHub', 'url': 'https://github.com/cantaro86/Financial-Models-Numerical-Methods/blob/master/1.4%20SDE%20-%20Heston%20model.ipynb'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Fast reliable pricing and calibration of the rough Heston model - arXiv', 'url': 'https://arxiv.org/html/2508.15080'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Robust Spectral Methods for Solving Option Pricing Problems - CORE', 'url': 'https://core.ac.uk/download/pdf/58915198.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] ADI finite difference schemes for option pricing in the Heston model ...', 'url': 'https://www.math.ualberta.ca/ijnam/Volume-7-2010/No-2-10/2010-02-06.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Richardson extrapolation - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Richardson_extrapolation'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Deep learning and American options via free boundary framework', 'url': 'https://arxiv.org/abs/2211.11803'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] ADI finite difference schemes for the Heston–Hull–White PDE - arXiv', 'url': 'https://arxiv.org/pdf/1111.4087.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '6.2. Richardson Extrapolation — Introduction to Numerical Methods ...', 'url': 'https://lemesurierb.people.charleston.edu/introduction-to-numerical-methods-and-analysis-python/main/richardson-extrapolation.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Exercise boundaries and efficient approximations to American ...', 'url': 'https://bear.warrington.ufl.edu/aitsahlia/AitSahlia_Lai_JCF01.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Lifted Heston Model: Efficient Monte Carlo Simulation with Large ...', 'url': 'https://arxiv.org/html/2510.08805v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] On the Numerical Evaluation of Option Prices in Jump Diffusion ...', 'url': 'https://engineering.nyu.edu/sites/default/files/2019-03/Carr-On-the-Numerical-Evaluation-of-Option-Prices-in-Jump-Diffusion-Processes.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'CFL Condition: How to Choose Your Timestep Size - SimScale', 'url': 'https://www.simscale.com/blog/cfl-condition/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The value of Monte Carlo model-based variance reduction ...', 'url': 'https://pmc.ncbi.nlm.nih.gov/articles/PMC7046269/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A Jump-Diffusion Model for Option Pricing - Columbia University', 'url': 'http://www.columbia.edu/~sk75/MagSci02.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'On the acceleration of explicit finite difference methods for option ...', 'url': 'https://www.tandfonline.com/doi/abs/10.1080/14697680903055570'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Some Numerical Methods for Options Valuation', 'url': 'http://www.scienpress.com/Upload/CMF/Vol%201_1_3.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Calibrating Heston Model - Hanlon Financial Systems Center', 'url': 'https://fsc.stevens.edu/calibrating-heston-model/'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '6.2. Richardson Extrapolation — Introduction to Numerical Methods ...', 'url': 'https://lemesurierb.people.charleston.edu/introduction-to-numerical-methods-and-analysis-python/main/richardson-extrapolation.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'A closed‐form pricing solution for options on assets with pricing errors', 'url': 'https://onlinelibrary.wiley.com/doi/10.1111/jfir.12473?af=R'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Fast Calibration in the Heston Model', 'url': 'https://fam.tuwien.ac.at/~sgerhold/pub_files/theses/bauer.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Richardson extrapolation - Wikipedia', 'url': 'https://en.wikipedia.org/wiki/Richardson_extrapolation'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A semi closed-form analytic pricing formula for call options in a ...', 'url': 'https://win.uantwerpen.be/~kihout/HHW.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A Space-Time Multigrid Method for the Numerical Valuation of ...', 'url': 'https://math.mit.edu/~urschel/publications/p2013b.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'The Barone-Adesi Whaley - formula to price American ... - UNIVPM', 'url': 'https://www.econ.univpm.it/recchioni/finance/w20'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Heston Model Closed-Form Solution', 'url': 'https://xilinx.github.io/Vitis_Libraries/quantitative_finance/2019.2/methods/cf-ht.html'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': 'Time Deep Gradient Flow Method for pricing American options - arXiv', 'url': 'https://arxiv.org/html/2507.17606v1'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Matched asymptotic expansions in financial engineering - People', 'url': 'https://people.maths.ox.ac.uk/howison/papers/lighthill.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Robust and Accurate Finite Difference Methods in Option Pricing ...', 'url': 'https://datasimfinancial.com/UserFiles/articles/daniel3.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] A High Order Finite Element Scheme for Pricing Options under ...', 'url': 'https://livrepository.liverpool.ac.uk/3000422/1/HOFES%20pricing%20options%20under%20regime%20SJDP27April2016.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Option Pricing by Transform Methods: Extensions, Unification, and ...', 'url': 'https://www.math.uchicago.edu/~rl/dft.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] FINITE DIFFERENCE AND SPECTRAL METHODS FOR ORDINARY ...', 'url': 'https://www.math.hmc.edu/~dyong/math165/trefethenbook.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] hp Finite Element Method pricing algorithms for lookback options in ...', 'url': 'https://ethz.ch/content/dam/ethz/special-interest/math/applied-mathematics/sam-dam/teaching-and-studies/theses/DanielKoviMSC.pdf'}}
{'type': 'url_citation', 'url_citation': {'end_index': 0, 'start_index': 0, 'title': '[PDF] Error Propagation in Dynamic Programming: From Stochastic ... - arXiv', 'url': 'https://arxiv.org/pdf/2509.20239.pdf'}}

## Sources
https://www.acenumerics.com/miscellaneous/neural-networks-in-quant-finance-for-high-accuracy-approximations-first-case-study-stochastic-volatility-model-calibration-heston
https://mbrenndoerfer.com/writing/finite-difference-methods-option-pricing-numerical-pde
https://arxiv.org/html/2508.15080v1
https://people.math.sc.edu/Burkardt/publications/cbg_sub_2014.pdf
https://pmc.ncbi.nlm.nih.gov/articles/PMC3893018/
https://www.stonex.com/en/financial-glossary/heston-model/
https://arxiv.org/html/2510.24074v1
https://math.leidenuniv.nl/scripties/MasterdeGraaf.pdf
https://arxiv.org/pdf/2311.07231.pdf
https://www.aimsciences.org/article/doi/10.3934/dcdss.2020226
https://bduring.warwick.ac.uk/pdf/xabs_duering.pdf
https://oa.upm.es/21942/1/TESIS_MASTER_IGOR_VIDIC.pdf
https://people.math.sc.edu/Burkardt/publications/cbg_sub_2014.pdf
https://mbrenndoerfer.com/writing/finite-difference-methods-option-pricing-numerical-pde
https://en.wikipedia.org/wiki/Finite_difference_method
https://www.math.ualberta.ca/ijnam/Volume-7-2010/No-2-10/2010-02-06.pdf
https://acr-journal.com/article/download/pdf/1265/
https://hplgit.github.io/INF5620/doc/pub/main_trunc-A4.pdf
https://fam.tuwien.ac.at/~sgerhold/pub_files/theses/bauer.pdf
https://arxiv.org/html/2510.24074v1
https://www.diva-portal.org/smash/get/diva2:813620/FULLTEXT01.pdf
https://arxiv.org/html/2409.12453v1
https://www.ntmsci.com/ajaxtool/GetArticleByPublishedArticleId?PublishedArticleId=1
http://www2.coe.pku.edu.cn/tpic/2010823112544527.pdf
https://blog.quantinsti.com/heston-model/
https://people.math.sc.edu/Burkardt/publications/cbg_sub_2014.pdf
https://www.math.purdue.edu/~shen7/pub/CSY11.pdf
https://github.com/cantaro86/Financial-Models-Numerical-Methods/blob/master/1.4%20SDE%20-%20Heston%20model.ipynb
https://arxiv.org/html/2508.15080
https://core.ac.uk/download/pdf/58915198.pdf
https://www.math.ualberta.ca/ijnam/Volume-7-2010/No-2-10/2010-02-06.pdf
https://en.wikipedia.org/wiki/Richardson_extrapolation
https://arxiv.org/abs/2211.11803
https://arxiv.org/pdf/1111.4087.pdf
https://lemesurierb.people.charleston.edu/introduction-to-numerical-methods-and-analysis-python/main/richardson-extrapolation.html
https://bear.warrington.ufl.edu/aitsahlia/AitSahlia_Lai_JCF01.pdf
https://arxiv.org/html/2510.08805v1
https://engineering.nyu.edu/sites/default/files/2019-03/Carr-On-the-Numerical-Evaluation-of-Option-Prices-in-Jump-Diffusion-Processes.pdf
https://www.simscale.com/blog/cfl-condition/
https://pmc.ncbi.nlm.nih.gov/articles/PMC7046269/
http://www.columbia.edu/~sk75/MagSci02.pdf
https://www.tandfonline.com/doi/abs/10.1080/14697680903055570
http://www.scienpress.com/Upload/CMF/Vol%201_1_3.pdf
https://fsc.stevens.edu/calibrating-heston-model/
https://lemesurierb.people.charleston.edu/introduction-to-numerical-methods-and-analysis-python/main/richardson-extrapolation.html
https://onlinelibrary.wiley.com/doi/10.1111/jfir.12473?af=R
https://fam.tuwien.ac.at/~sgerhold/pub_files/theses/bauer.pdf
https://en.wikipedia.org/wiki/Richardson_extrapolation
https://win.uantwerpen.be/~kihout/HHW.pdf
https://math.mit.edu/~urschel/publications/p2013b.pdf
https://www.econ.univpm.it/recchioni/finance/w20
https://xilinx.github.io/Vitis_Libraries/quantitative_finance/2019.2/methods/cf-ht.html
https://arxiv.org/html/2507.17606v1
https://people.maths.ox.ac.uk/howison/papers/lighthill.pdf
https://datasimfinancial.com/UserFiles/articles/daniel3.pdf
https://livrepository.liverpool.ac.uk/3000422/1/HOFES%20pricing%20options%20under%20regime%20SJDP27April2016.pdf
https://www.math.uchicago.edu/~rl/dft.pdf
https://www.math.hmc.edu/~dyong/math165/trefethenbook.pdf
https://ethz.ch/content/dam/ethz/special-interest/math/applied-mathematics/sam-dam/teaching-and-studies/theses/DanielKoviMSC.pdf
https://arxiv.org/pdf/2509.20239.pdf