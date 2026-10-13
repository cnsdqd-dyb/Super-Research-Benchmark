# Deep Research Report: minimax/minimax-m2.1
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 3eb666cd | **Time:** 336.96s | **Cost:** $0.19076
--------------------------------------------------------------------------------

# Can Numerical Solutions to the Heston Model Balance Convergence Speed and Estimation Accuracy, or Does Grid Density Selection in Finite Difference Methods Introduce Significant Errors in Long-Term Option Pricing?

## Abstract

This research report examines the fundamental trade-off between computational efficiency and pricing accuracy in numerical solutions to the Heston stochastic volatility model, with particular emphasis on the role of grid density selection in finite difference methods for long-term option pricing. The Heston model, which describes asset price dynamics through a two-dimensional stochastic process with correlated Brownian motions, presents significant computational challenges that have driven decades of methodological innovation. Through comprehensive analysis of contemporary finite difference schemes—including Alternating Direction Implicit (ADI) methods, high-order compact schemes, and modern machine learning approaches—this report evaluates whether practitioners can achieve satisfactory convergence rates while maintaining acceptable estimation accuracy across varying time horizons. The evidence suggests that while grid density selection does introduce non-trivial errors, particularly for long-dated options, carefully designed non-uniform grids combined with appropriately parameterized ADI schemes can effectively balance these competing objectives. The MCS scheme with θ = 1/3 and the HV scheme with θ = 1/2 + 1/6√3 emerge as particularly robust choices, demonstrating unconditional stability and second-order convergence behavior even for extended maturities.

## 1. Introduction

### 1.1 Background and Motivation

The Heston model, introduced by Steven Heston in 1993, represents one of the most influential stochastic volatility frameworks in quantitative finance [1]. Unlike the Black-Scholes model, which assumes constant volatility, the Heston model captures the empirical observation that volatility itself follows a stochastic process, thereby providing a more realistic representation of market dynamics. The model is defined by a system of stochastic differential equations describing the joint evolution of the asset price and its instantaneous variance, with the two processes driven by correlated Brownian motions. This mathematical structure gives rise to a two-dimensional partial differential equation that must be solved numerically to obtain option prices.

The computational challenges inherent in solving the Heston PDE have motivated extensive research into numerical methods over the past three decades. Finite difference methods have emerged as a dominant approach due to their flexibility and relatively straightforward implementation. However, these methods introduce discretization errors that manifest through both spatial grid approximation and temporal stepping schemes. The question of whether these errors can be adequately controlled—particularly for long-dated options where error accumulation becomes a significant concern—remains of paramount importance to practitioners and researchers alike.

### 1.2 Research Objectives

This report addresses two interconnected questions that are critical to the practical application of numerical methods for Heston model pricing. First, we examine whether convergence speed and estimation accuracy can be effectively balanced across different computational schemes, focusing on the trade-offs inherent in various algorithmic choices. Second, we investigate whether grid density selection in finite difference methods introduces systematic errors that disproportionately affect long-term option pricing, potentially rendering certain computational approaches inadequate for extended time horizons.

The analysis draws upon recent theoretical developments and extensive numerical experiments reported in the quantitative finance literature, synthesizing findings from multiple authoritative sources to provide a comprehensive assessment of the current state of numerical methods for the Heston model.

## 2. The Heston Model and Its Computational Framework

### 2.1 Mathematical Formulation

The Heston model is defined by the following stochastic differential equations:

$$
dS(t) = \mu S(t) dt + \sqrt{v(t)} S(t) dW^{(1)}(t)
$$

$$
dv(t) = \kappa(\eta - v(t)) dt + \sigma \sqrt{v(t)} dW^{(2)}(t)
$$

where $S(t)$ denotes the asset price, $v(t)$ represents the instantaneous variance, $\kappa$ is the mean-reversion rate, $\eta$ is the long-term mean variance, $\sigma$ is the volatility of variance (often called "vol of vol"), and $dW^{(1)}(t)$ and $dW^{(2)}(t)$ are correlated Brownian motions with correlation coefficient $\rho \in [-1, 1]$. The Feller condition, given by $2\kappa\eta > \sigma^2$, ensures that the variance process remains strictly positive, though many practical applications involve parameter sets where this condition is violated [2].

The price $u(s, v, t)$ of a European option in the Heston model satisfies the parabolic PDE:

$$
\frac{\partial u}{\partial t} = \frac{1}{2}s^2 v \frac{\partial^2 u}{\partial s^2} + \rho\sigma sv \frac{\partial^2 u}{\partial s \partial v} + \frac{1}{2}\sigma^2 v \frac{\partial^2 u}{\partial v^2} + (r_d - r_f)s \frac{\partial u}{\partial s} + \kappa(\eta - v) \frac{\partial u}{\partial v} - r_d u
$$

This equation represents a time-dependent convection-diffusion-reaction equation on an unbounded two-dimensional spatial domain, with the mixed derivative term $\rho\sigma sv \frac{\partial^2 u}{\partial s \partial v}$ arising from the correlation between the two underlying Brownian motions [3]. The presence of this mixed derivative term significantly complicates the numerical solution, as it introduces off-diagonal elements in the coefficient matrix that must be handled with appropriate discretization strategies.

### 2.2 Numerical Solution Approaches

The numerical solution of the Heston PDE has been approached through several distinct methodologies, each with characteristic strengths and limitations. Finite difference methods discretize the continuous domain into a grid of points, approximating derivatives through difference quotients and solving the resulting system of linear equations. Finite element methods offer greater flexibility in handling complex domain geometries but typically require more sophisticated implementation. Monte Carlo methods simulate paths of the underlying stochastic processes and average payoffs, though they generally require substantial computational resources for accurate results. More recently, machine learning approaches including Physics-Informed Neural Networks (PINNs) have emerged as promising alternatives that leverage deep learning techniques to approximate solution functions [4].

Among these approaches, finite difference methods have received the most extensive attention in the literature, with particular focus on Alternating Direction Implicit (ADI) schemes that decompose the two-dimensional problem into a sequence of one-dimensional problems. This decomposition significantly reduces computational complexity while maintaining acceptable accuracy, making ADI schemes particularly attractive for practical applications.

## 3. Finite Difference Discretization and Grid Construction

### 3.1 Spatial Discretization Strategies

The spatial discretization of the Heston PDE involves constructing a two-dimensional grid in the $(s, v)$-plane, where $s$ represents the asset price and $v$ represents the variance. The unbounded nature of the domain necessitates careful consideration of boundary conditions and grid truncation. A typical approach defines grid points according to:

$$
v_i = v_{\min} + i \Delta v, \quad i = 0, \ldots, I
$$

$$
s_j = s_{\min} + j \Delta s, \quad j = 0, \ldots, J
$$

with $\Delta v = (v_{\max} - v_{\min})/I$ and $\Delta s = (s_{\max} - s_{\min})/J$ [5]. The selection of boundary values $v_{\min}, v_{\max}, s_{\min}, s_{\max}$ significantly impacts computational accuracy, as option prices must approach their intrinsic values at extreme points in the domain.

The application of non-uniform meshes has been shown to greatly improve accuracy compared to uniform grids [6]. This improvement stems from the observation that option prices exhibit the most interesting behavior—and the highest sensitivity to model parameters—in specific regions of the state space. For European options, the region near $s = K$ (where $K$ is the strike price) and $v = 0$ is particularly important, as this is where the option's payoff function exhibits non-smooth behavior and where the PDE transitions from parabolic to hyperbolic character.

A sophisticated approach to non-uniform grid construction employs a transformation based on the hyperbolic sine function:

$$
\xi_i = \sinh^{-1}(-K/c) + i \cdot \Delta \xi, \quad 0 \leq i \leq m_1
$$

with $\Delta \xi = \frac{1}{m_1} \left[ \sinh^{-1}((S-K)/c) - \sinh^{-1}(-K/c) \right]$ [3]. This transformation concentrates grid points in the region of greatest interest while maintaining adequate coverage of the tails, effectively balancing resolution requirements against computational cost.

### 3.2 Temporal Discretization and ADI Schemes

The temporal discretization of the Heston PDE introduces additional approximation errors that interact with spatial discretization errors in complex ways. ADI schemes have become the standard approach for temporal discretization due to their unconditional stability properties and computational efficiency. These schemes decompose the two-dimensional problem into a sequence of one-dimensional problems that can be solved efficiently using tridiagonal solvers.

The general form of an ADI scheme for the Heston PDE can be expressed as:

$$
\frac{u^{n+1}_{i,j} - u^n_{i,j}}{\Delta \tau} - \theta L_h u^{n+1}_{i,j} - (1-\theta) L_h u^n_{i,j} = 0
$$

where $L_h$ denotes the spatial discretization operator and $\theta$ is a parameter that controls the weighting between implicit and explicit treatment [5]. Several specific ADI schemes have been developed and analyzed for the Heston model:

The Douglas-Rachford (Do) scheme, with $\theta = 2/3$, exhibits first-order convergence behavior and has been observed to have relatively large temporal errors for modest time steps [3]. The Craig-Sneyd (CS) scheme, with $\theta = 1/2$, achieves second-order convergence but requires damping at $t = 0$ to maintain stability. The Modified Craig-Sneyd (MCS) scheme, with $\theta = 1/3$, has emerged as a particularly robust choice, demonstrating unconditional stability and second-order convergence across a wide range of parameter sets [6]. The Hundsdorfer-Verwer (HV) scheme, with $\theta = 1/2 + 1/6\sqrt{3} \approx 0.789$, also achieves second-order convergence and serves as an excellent alternative to the MCS scheme [3].

### 3.3 Grid Density and Error Analysis

The relationship between grid density and computational error is fundamentally governed by the order of accuracy of the numerical scheme. For schemes with second-order convergence behavior, the global error scales as $O(\Delta t^2 + \Delta s^2 + \Delta v^2)$, meaning that halving the grid spacing reduces the error by approximately a factor of four. However, this theoretical convergence rate can be degraded by several factors, including:

The non-smoothness of the initial payoff function introduces high-frequency errors that converge more slowly than the nominal order of accuracy would suggest [7]. The discontinuity in the first derivative of the call option payoff at $s = K$ generates Gibbs-like phenomena that require refined grids for accurate resolution. Additionally, the convection-dominated nature of the PDE near $v = 0$ creates boundary layers that demand careful treatment.

For long-dated options, error accumulation over extended time horizons can significantly impact pricing accuracy. The temporal error, defined as the difference between the numerical solution and the exact solution of the semi-discrete problem, can be analyzed through the concept of "stiff order" of convergence [6]. This concept captures the observed convergence behavior when the spatial discretization is held fixed while the time step is refined, providing insight into how temporal errors behave independently of spatial approximation errors.

## 4. Convergence Speed and Accuracy Trade-offs

### 4.1 Empirical Convergence Behavior

Extensive numerical experiments have characterized the convergence behavior of various ADI schemes for the Heston PDE. In a comprehensive study examining four different parameter sets—including cases where the Feller condition is satisfied and violated—the MCS scheme with $\theta = 1/3$ consistently demonstrated stiff-order convergence equal to two [6]. This means that the temporal error behaves as $C(\Delta t)^2$ for sufficiently small time steps, with constants $C$ that are only weakly dependent on the number of spatial grid points.

The HV2 scheme (with $\theta = 1/2 + 1/6\sqrt{3}$) exhibited similar convergence behavior, achieving stiff-order convergence of two across all tested cases. The HV1 scheme (with $\theta = 1 - 1/2\sqrt{2} \approx 0.293$) showed more variable behavior, with convergence order equal to two in most cases but exhibiting error peaks in certain configurations [3]. The Do scheme consistently demonstrated first-order convergence, while the CS scheme achieved second-order convergence when combined with appropriate damping procedures.

These empirical findings suggest that the choice of ADI scheme significantly impacts both convergence speed and achievable accuracy. Schemes with second-order convergence (MCS, HV2, CS with damping) can achieve the same accuracy with fewer time steps than first-order schemes (Do), effectively reducing computational time while maintaining or improving accuracy.

### 4.2 Computational Efficiency Considerations

The computational efficiency of finite difference methods for the Heston PDE depends on multiple factors, including the number of grid points, the number of time steps, and the computational cost per time step. ADI schemes offer a significant advantage in this regard by decomposing the two-dimensional problem into one-dimensional problems that can be solved using efficient tridiagonal solvers. The computational cost per time step scales as $O(I \cdot J)$, where $I$ and $J$ are the numbers of grid points in the $v$ and $s$ directions, respectively.

For the MCS scheme, the optimal choice of $\theta$ parameter has been analyzed theoretically, with $\theta = \max\{1/3, 2/13(2\gamma + 1)\}$ recommended, where $\gamma = \max_{i,j} |\rho_{ij}|$ [3]. This parameter selection ensures unconditional stability while minimizing error constants. The damping procedure, which involves applying the Do scheme with $\theta = 1$ at the initial time step, adds negligible computational overhead while significantly improving stability behavior.

The trade-off between convergence speed and accuracy manifests most clearly in the choice of grid density. Increasing the number of grid points improves spatial accuracy but increases computational cost per time step. Similarly, reducing the time step improves temporal accuracy but increases the total number of time steps required. In practice, practitioners must balance these competing considerations based on the specific requirements of their application.

### 4.3 Long-Term Option Pricing Challenges

Long-term option pricing presents unique challenges for finite difference methods. Over extended time horizons, several factors can degrade computational accuracy:

Error accumulation causes small per-step errors to compound over many time steps, potentially leading to significant total errors even when individual step errors are small. Boundary effects become more pronounced as the solution evolves over longer periods, potentially causing the numerical solution to deviate from the true solution near domain boundaries. The non-uniformity of grid resolution can lead to uneven error distribution, with higher errors in regions where grid spacing is coarser.

Recent research on the rough Heston model has highlighted the importance of grid adaptation for long maturities [8]. The rough Heston model, which replaces the variance process with a fractional square root process, exhibits different computational characteristics than the classical Heston model. For this model, non-uniform grids have been found to be "indispensable for pricing options of long maturities," emphasizing the critical role of grid design in long-term applications.

The characteristic function approach, which provides an analytical representation of the option price through Fourier inversion, offers an alternative to finite difference methods for long-dated options [9]. However, this approach requires numerical integration and may face challenges when applied to complex derivative structures or time-dependent model parameters.

## 5. Advanced Numerical Techniques and Emerging Approaches

### 5.1 High-Order Compact Schemes

High-order compact finite difference schemes have been developed to achieve higher accuracy with fewer grid points than traditional second-order schemes. These schemes achieve higher order accuracy by incorporating more neighboring points in the difference approximation while maintaining a compact stencil. For the Heston PDE, high-order compact schemes have demonstrated the ability to achieve fourth-order spatial accuracy while maintaining computational efficiency comparable to second-order schemes [10].

The error analysis of high-order compact schemes reveals that they can significantly reduce spatial errors for smooth solutions. However, the non-smoothness of option payoff functions limits the practical benefit of very high-order spatial approximations. The discontinuity in the first derivative at $s = K$ introduces errors that dominate the total error for coarse grids, regardless of the order of the spatial discretization.

### 5.2 Adaptive Mesh Refinement

Adaptive mesh refinement (AMR) techniques dynamically adjust grid resolution based on the local behavior of the solution, concentrating computational resources where they are most needed. For the Heston PDE, AMR can automatically refine the grid near $s = K$ and $v = 0$ where the solution exhibits the most interesting behavior, while using coarser grids in regions where the solution varies slowly.

The implementation of AMR for the Heston PDE involves criteria for detecting regions requiring refinement, interpolation schemes for transferring solutions between grids of different resolution, and error estimation techniques for controlling the refinement process. While AMR can significantly improve computational efficiency, it adds implementation complexity and may introduce interpolation errors that degrade overall accuracy.

### 5.3 Machine Learning Approaches

Recent advances in machine learning have introduced new approaches to option pricing that complement traditional numerical methods. Physics-Informed Neural Networks (PINNs) encode the PDE into the loss function of a neural network, training the network to satisfy both the PDE and boundary conditions simultaneously [4]. This approach offers several potential advantages:

PINNs can handle complex geometries and boundary conditions without requiring structured grids. They can naturally incorporate known analytical solutions in certain regions, potentially improving accuracy where traditional methods struggle. The computational cost of evaluating a trained network is independent of grid density, potentially offering advantages for repeated pricing calculations.

However, machine learning approaches also face challenges. Training neural networks requires significant computational resources and careful hyperparameter selection. The accuracy of PINNs depends on the network architecture, training procedure, and the representativeness of training data. For the Heston PDE, the mixed derivative term and the unbounded domain present additional challenges that require careful treatment.

Differential Deep Learning (DDL) approaches combine traditional numerical methods with machine learning, using neural networks to accelerate specific components of the computation [4]. For the time-dependent Heston model, DDL has shown improvements in computational efficiency while maintaining acceptable pricing accuracy.

## 6. Practical Recommendations and Best Practices

### 6.1 Scheme Selection Guidelines

Based on the comprehensive analysis of the literature, the following recommendations emerge for practitioners selecting numerical schemes for Heston model pricing:

The MCS scheme with $\theta = 1/3$ and damping at $t = 0$ is recommended as the primary choice for most applications. This scheme consistently demonstrates unconditional stability, second-order convergence, and robust performance across a wide range of parameter sets [3][6]. The computational overhead of damping is negligible, while the stability benefits are substantial.

The HV scheme with $\theta = 1/2 + 1/6\sqrt{3}$ serves as an excellent alternative, particularly when slightly larger error constants are acceptable in exchange for other desirable properties. The CS scheme with $\theta = 1/2$ is also viable but requires damping at $t = 0$ for reliable performance.

The Do scheme should generally be avoided for applications requiring high accuracy, as its first-order convergence leads to significantly larger temporal errors compared to second-order schemes. However, the Do scheme may be useful for damping purposes or in situations where its specific stability properties are advantageous.

### 6.2 Grid Design Principles

Effective grid design is critical for achieving accurate and efficient numerical solutions. The following principles should guide grid construction:

Non-uniform grids should be employed to concentrate resolution in regions of greatest interest. For European options, this typically means refining the grid near $s = K$ and $v = 0$. The hyperbolic sine transformation provides an effective mechanism for achieving this concentration while maintaining adequate coverage of the domain tails [3].

The number of grid points should be selected based on the required accuracy and the characteristics of the specific option being priced. For at-the-money options, fewer grid points may be sufficient, while deep in-the-money or out-of-the-money options may require finer resolution. Grid convergence studies, in which the solution is computed on successively refined grids, should be performed to verify that the chosen grid density provides adequate accuracy.

Boundary conditions should be chosen carefully to minimize their impact on the solution in the region of interest. For call options, boundary conditions at large $s$ should approximate the continuation value, while boundaries at $s = 0$ should reflect the option's intrinsic value. The variance boundary at $v = 0$ requires particular attention due to the convection-dominated nature of the PDE in this region.

### 6.3 Long-Term Option Considerations

For long-dated options, additional precautions should be taken to ensure accurate pricing:

Temporal error accumulation can be mitigated by using second-order schemes with small time steps. The stiff-order convergence analysis suggests that temporal errors scale as $(\Delta t)^2$, so reducing the time step by a factor of four reduces temporal errors by approximately a factor of 16. However, this comes at increased computational cost, so practitioners must balance accuracy requirements against time constraints.

Grid adaptation for long maturities may require larger domains to ensure that boundary effects do not contaminate the solution in the region of interest. As the solution evolves over longer periods, it may explore regions of the state space that are far from the initial point, necessitating larger grid boundaries.

The rough Heston model literature suggests that non-uniform grids become increasingly important for longer maturities [8]. Practitioners pricing long-dated options should consider whether the classical Heston model or the rough Heston model is more appropriate for their application, as this choice has implications for the required numerical treatment.

## 7. Conclusions

This comprehensive analysis of numerical methods for the Heston model reveals that practitioners can indeed achieve a satisfactory balance between convergence speed and estimation accuracy, provided that appropriate schemes and grid designs are employed. The evidence strongly supports the following conclusions:

First, the selection of ADI scheme significantly impacts both convergence speed and achievable accuracy. The MCS scheme with $\theta = 1/3$ and the HV scheme with $\theta = 1/2 + 1/6\sqrt{3}$ consistently demonstrate second-order convergence with unconditional stability, enabling practitioners to achieve high accuracy with reasonable computational resources. These schemes represent the current state-of-the-art for finite difference solutions of the Heston PDE.

Second, grid density selection does introduce errors that can be significant for long-term option pricing, but these errors can be effectively managed through careful grid design. Non-uniform grids that concentrate resolution in regions of interest—particularly near $s = K$ and $v = 0$—provide substantial accuracy improvements compared to uniform grids with the same number of points. For long-dated options, grid adaptation becomes increasingly important, and practitioners should consider non-uniform grids as essential rather than optional.

Third, the trade-off between convergence speed and accuracy is not inherent to the Heston model itself but rather reflects the choice of numerical method. Second-order schemes achieve the same accuracy as first-order schemes with significantly fewer time steps, effectively providing both faster convergence and higher accuracy. The apparent trade-off is therefore more accurately characterized as a choice between methods with different efficiency levels.

Fourth, emerging approaches including high-order compact schemes, adaptive mesh refinement, and machine learning methods offer potential improvements for specific applications. While these methods are not yet standard practice, they represent active areas of research that may become more prominent as computational resources continue to increase and as the methods mature.

In summary, the numerical solution of the Heston model is a well-developed field with established best practices that enable accurate and efficient option pricing across a wide range of maturities and parameter sets. The key to success lies in selecting appropriate schemes (preferably MCS or HV), designing effective non-uniform grids, and performing convergence studies to verify that the chosen discretization provides adequate accuracy for the specific application.

## References

[1] S. L. Heston, "A Closed-Form Solution for Options with Stochastic Volatility with Applications to Bond and Currency Options," *Review of Financial Studies*, vol. 6, no. 2, pp. 327-343, 1993.

[2] K. J. In 't Hout and S. Foulon, "ADI Finite Difference Schemes for Option Pricing in the Heston Model with Correlation," *International Journal of Numerical Analysis and Modeling*, vol. 7, no. 2, pp. 303-320, 2010.

[3] T. Haentjens and K. J. In 't Hout, "ADI Finite Difference Schemes for the Heston-Hull-White PDE," *arXiv preprint arXiv:1111.4087*, 2011.

[4] "Differential Deep Learning and Physics-Informed Neural Networks for Fast Derivative Pricing," *HAL Science*, hal-05160171v1, 2024.

[5] D. Dang, C. Christara, and K. Jackson, "Pricing Multi-Asset American Options on GPUs Using a PDE Approach," *University of Toronto*, 2014.

[6] K. J. In 't Hout and S. Foulon, "ADI Finite Difference Schemes for Option Pricing in the Heston Model with Correlation," *International Journal of Numerical Analysis and Modeling*, vol. 7, no. 2, pp. 303-320, 2010.

[7] D. Wang, C. Christara, and K. Serkh, "Analysis of High-Order Time-Stepping Schemes for Nonsmooth Initial Conditions in Financial Pricing," *University of Toronto*, 2023.

[8] "Rough Heston Model and Its Markovian Approximation," *arXiv preprint arXiv:2508.15080*, 2025.

[9] Á. Leitao et al., "Wavelet-Based Fourier Inversion for the Heston Model," *Journal of Computational Finance*, 2024.

[10] B. Düring, "High-Order Compact Finite Difference Methods for the Heston Model," *University of Warwick*, 2010.

## Annotations


## Sources
[1] http://www.cs.toronto.edu/NA/reports.html
[2] https://arxiv.org/html/2508.15080
[3] https://arxiv.org/pdf/1111.4087
[4] https://arxiv.org/pdf/1309.0110
[5] https://bduring.warwick.ac.uk/pdf/xabs_duering.pdf
[6] https://diposit.ub.edu/bitstreams/a725583b-3ffb-4a09-b075-30f1aad3de45/download
[7] https://eprints.lse.ac.uk/83754/1/Germano_Full%20and%20fast%20calibration_2017.pdf
[8] https://hal.science/hal-05160171v1/file/Fast_Computing_Heston_Paper_FV.pdf
[9] https://math.leidenuniv.nl/scripties/MasterdeGraaf.pdf
[10] https://medium.com/@uddin.maher/option-pricing-with-the-heston-model-part-2-parameter-estimation-monte-carlo-simulations-2a7be6e00cf2
[11] https://people.math.sc.edu/Burkardt/publications/cbg_sub_2014.pdf
[12] https://people.sc.fsu.edu/~jburkardt/publications/cbg_2014.pdf
[13] https://pure.uva.nl/ws/files/990244/76977_09.pdf
[14] https://scispace.com/pdf/adi-finite-difference-schemes-for-option-pricing-in-the-1j68aleuc6.pdf
[15] https://www.bauer.uh.edu/spirrong/Pirrong_storage_book_101115.pdf
[16] https://www.math.ualberta.ca/ijnam/Volume-7-2010/No-2-10/2010-02-06.pdf
[17] https://www.ressources-actuarielles.net/EXT/ISFA/1226.nsf/0/1826b88b152e65a7c12574b000347c74/$FILE/LeifAndersenHeston.pdf
[18] https://wwwf.imperial.ac.uk/~ajacquie/IC_Num_Methods/IC_Num_Methods_Docs/Literature/Reports/ADIHeston_Report.pdf