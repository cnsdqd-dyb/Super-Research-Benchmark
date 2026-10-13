# Deep Research Report: openai/o4-mini-deep-research
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 9aba924f | **Time:** 233.87s | **Cost:** $0.48644
--------------------------------------------------------------------------------

# Characteristic Polynomial and Lyapunov Stability

In an intergenerational welfare model one typically obtains a linear update of the form either $x_{t+1}=T\,x_t$ (discrete‐time) or $\dot x=T\,x$ (continuous time), where $T$ is the **intergenerational transfer matrix**.  The **characteristic polynomial** of $T$ is 
\[
p(\lambda)=\det(\lambda I - T)\,,
\] 
and its roots $\{\lambda_i\}$ are the eigenvalues of $T$.  These eigenvalues determine the response of the system to perturbations.  By definition, an equilibrium is Lyapunov‐stable if small deviations remain small (and for asymptotic stability they decay to zero).  In linear systems this reduces to simple eigenvalue tests:  

- **Eigenvalues from the characteristic polynomial:**  Solving $p(\lambda)=0$ gives the eigenvalues $\lambda_i$ of the transfer matrix.  The system’s stability hinges on these values.  (No matter how complicated the intergenerational model, in the linear approximation the long‐run behavior is governed by $\lambda_i$.)  

- **Continuous‐time criterion:**  If the welfare dynamics are modeled continuously ($\dot x = T x$), Lyapunov (asymptotic) stability requires **all** eigenvalues to have negative real parts.  Equivalently, each root of $p(\lambda)$ must lie in the open left half of the complex plane.  As one standard text notes, “$A$ is stable iff all the eigenvalues of $A$ lie in the open left half plane (Re $λ<0$)” ([home.iitk.ac.in](https://home.iitk.ac.in/~rksr/html/12STB.htm#:~:text=condition%20for%20the%20stability%20is,0%2Cn%2C0)).  Thus any root with nonnegative real part would violate Lyapunov stability.  

- **Discrete‐time criterion:**  If the model is in discrete time ($x_{t+1}=T x_t$), stability means $\lambda_i$ must lie strictly inside the unit circle in the complex plane.  In other words, $|\lambda_i|<1$ for every root of $p(\lambda)$.  As noted by Cook (2019), “a discrete‐time linear system is stable if and only if all its eigenvalues are inside the unit circle” ([www.johndcook.com](https://www.johndcook.com/blog/2019/12/15/stability-criteria/#:~:text=A%20discrete,The%20change%20of%20variables)).  If any $|\lambda_i|\ge1$, a small disturbance will either persist or grow, breaking Lyapunov stability.  

- **Practical check via the polynomial:**  Hence, the characteristic polynomial *encodes* the Lyapunov stability test.  Checking the signs of real parts or magnitudes of its roots (often via Routh–Hurwitz tests for continuous systems or Jury tests for discrete systems) is mathematically equivalent to checking that small intergenerational “shocks” die out rather than amplify.  In short, *all* roots of $p(\lambda)$ must lie in the stable region (Re $λ<0$ or $|\lambda|<1$) for the welfare system to be Lyapunov‐stable.  Any eigenvalue outside that region signals that the transfer equilibrium is not stable.  

**Answer:** In this way, the characteristic polynomial of the transfer matrix directly determines Lyapunov stability: its roots (the matrix’s eigenvalues) must lie in the left half‐plane (continuous time) or inside the unit circle (discrete time) for the welfare system to be Lyapunov‐stable ([home.iitk.ac.in](https://home.iitk.ac.in/~rksr/html/12STB.htm#:~:text=condition%20for%20the%20stability%20is,0%2Cn%2C0)) ([www.johndcook.com](https://www.johndcook.com/blog/2019/12/15/stability-criteria/#:~:text=A%20discrete,The%20change%20of%20variables)).

## Annotations
{'type': 'url_citation', 'url_citation': {'end_index': 1537, 'start_index': 1415, 'title': 'STABILITY OF A MATRIX', 'url': 'https://home.iitk.ac.in/~rksr/html/12STB.htm#:~:text=condition%20for%20the%20stability%20is,0%2Cn%2C0'}}
{'type': 'url_citation', 'url_citation': {'end_index': 2123, 'start_index': 1988, 'title': 'Characteristic polynomials and stability criteria', 'url': 'https://www.johndcook.com/blog/2019/12/15/stability-criteria/#:~:text=A%20discrete,The%20change%20of%20variables'}}
{'type': 'url_citation', 'url_citation': {'end_index': 3260, 'start_index': 3138, 'title': 'STABILITY OF A MATRIX', 'url': 'https://home.iitk.ac.in/~rksr/html/12STB.htm#:~:text=condition%20for%20the%20stability%20is,0%2Cn%2C0'}}
{'type': 'url_citation', 'url_citation': {'end_index': 3396, 'start_index': 3261, 'title': 'Characteristic polynomials and stability criteria', 'url': 'https://www.johndcook.com/blog/2019/12/15/stability-criteria/#:~:text=A%20discrete,The%20change%20of%20variables'}}

## Sources
