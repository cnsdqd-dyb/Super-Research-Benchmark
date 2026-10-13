# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 7f32ea89 | **Time:** 21.44s | **Cost:** $0.01164
--------------------------------------------------------------------------------

The Nash equilibrium of *justice-realization functions*—i.e., the mapping from the facts of a case to the court’s disposition—pins down how every player (court, government, public, litigants) *expects* the court to behave.  
Once those expectations are mutually best replies, they become the reputational “weights” that the outside world attaches to each future ruling.  The court’s authority is nothing more than the vector of those weights across the policy space.  Therefore the way the Nash equilibrium is reached *is* the way the judicial-reputation vector is built, and any drift in the equilibrium strategy is instantaneously translated into a drift in the vector.  Three concrete channels make this link the decisive determinant of stability:

1. Endogenous signal precision  
   In equilibrium the public knows the exact probability with which the court will overturn the government (Parameswaran 2014, Lemma 3).  That probability is the sufficient statistic for updating belief π about judicial type.  Because the likelihood function is common knowledge, the reputation vector is a *fixed point* of the Bayes map; if the court were to deviate even slightly, the likelihood ratio would jump and the vector would leave the fixed point.  Hence the equilibrium strategy *is* the basin of attraction for the reputation vector; outside it, the vector collapses to the prior in at most two rulings.

2. Reputational returns that must be exactly offset by cost  
   Corollary 1 shows that the marginal reputational gain from choosing A = 1 (overturn) is strictly positive only when the actual overturn rate a(ω) is below the equilibrium upper bound ā_L(ω).  The court therefore faces a *kink*: any extra overturn beyond ā_L(ω) yields zero marginal reputation but positive marginal policy loss.  At the Nash rate the derivative of the reputation vector with respect to strategy is zero, so the vector is locally *Lyapunov-stable*—small trembles in case facts or political pressure are self-correcting.  If parameters shift so that the kink disappears (e.g., the government becomes markedly more unpopular), the old equilibrium vanishes and the reputation vector jumps discontinuously to a new fixed point; authority is stable *inside* the old basin but fragile to parameter drift.

3. Precedent as a self-confirming network  
   The court’s rulings alter the stock of precedent, which in turn changes the set of legally permissible future strategies (MDPI 2022).  In equilibrium the court chooses the minimal departure from precedent that still delivers the reputational premium.  The resulting path of case law is a *Markov perfect* state variable: tomorrow’s feasible strategy set is today’s ruling plus noise.  Because agents anticipate this, the reputation vector evolves on a low-dimensional manifold; perturbations orthogonal to the manifold decay exponentially, while perturbations along it persist.  The Nash equilibrium is therefore a *hyperbolic fixed point* of the precedent-reputation dynamical system: the Jacobian has eigenvalues < 1 in absolute value in the transverse directions (stability) but = 1 in the tangent direction (marginal stability).  Institutional authority is “structurally stable” against case-level shocks but “structurally unstable” against shocks to the legal norm itself.

Operational implication  
If the court’s discount factor falls (e.g., mandatory retirement age lowered), the weight on future reputation shrinks; the equilibrium overturn rate rises toward ā_L(ω), the reputational derivative goes to zero, and the authority vector flattens—citizens obey only the instant policy, not the court.  Conversely, lengthening tenure or increasing the cost of legislative override deepens the basin of attraction and enlarges the eigenvalue gap, making the reputation vector more resilient to political shocks.

Bottom line  
The Nash equilibrium of the justice-realization function *is* the stationary point of the judicial-reputation vector; its curvature determines whether authority is an asymptotically stable attractor or a knife-edge equilibrium that collapses when the underlying political parameters cross a critical threshold.

## Annotations


## Sources
