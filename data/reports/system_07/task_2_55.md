# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 624ab833 | **Time:** 40.71s | **Cost:** $0.02485
--------------------------------------------------------------------------------

Interpretability algorithms for risk models **do not automatically balance prediction accuracy and transparency**—they **mediate** the tension, often imperfectly.  
SHAP value **approximation error** is **not a theoretical show-stopper**, but in **regulatory-grade documentation** it can **erode the evidentiary quality** that supervisors expect, so **compliance risk is real** unless the error is bounded, audited, and reported.

------------------------------------------------
1.  Trade-off is contextual, not algorithmic  
   - In credit, cyber, and clinical risk, post-hoc tools (SHAP, LIME) let a bank or hospital **keep a high-accuracy gradient-boosted or neural model**, but the **explanations themselves are not the model**; they are **surrogates** whose fidelity varies with tree depth, correlation structure, sample size, and hyper-parameters.  
   - Studies repeatedly show that **accuracy drops only 1–3 %** when switching to an **inherently interpretable model** (EBM, GAM, sparse-linear with monotonicity constraints) **tailored to the policy constraints** (Medicare Advantage, GDPR “right to explanation”, Basel model-validation).  
   - When the **cost of a false negative is high** (stroke, money-laundering), regulators accept a **dual-layer architecture**: black-box for signal, interpretable companion for justification. The **balance is engineered by the enterprise**, not by the algorithm alone.

2.  SHAP approximation error and the audit trail  
   - KernelSHAP and TreeSHAP **estimate** Shapley values; the **error is zero only for fully additive models**. For real-world boosted trees or deep nets the **L² error is small (< 5 % of prediction variance)** in hold-out tests, but **can exceed 15 %** when features are highly correlated or cardinality is large.  
   - **Regulators do not ask for zero error**; they ask for **“sufficiently accurate explanations”** (EU AI Act recital 44, SR 11-7 model-validation guidance). An **unbounded or unquantified error** means the **explanation is not reproducible**, which **fails the “materiality” test** under PRA or FDA audit.  
   - Practical compliance therefore requires:  
     – **Error bars or bootstrap CIs** around φⱼ (already supported by `shap.utils.hclust` and `shap.bootstrap`).  
     – **Sensitivity analysis** that shows top-K features are **stable across retraining windows**.  
     – **Documentation** that discloses the **approximation method and its assumptions** (independence, coalition size, background sample).  
   - When these steps are missing, **supervisory push-back is common**—not because SHAP is intrinsically invalid, but because the **submission is incomplete**.

------------------------------------------------
Bottom line  
Interpretability algorithms are **diagnostic accessories**, not a self-correcting balance wheel. They let you **retain accuracy while producing an explanation**, yet the **explanation itself must meet the same evidential standards** as the model. SHAP’s approximation error is **tolerable for compliance only when it is measured, bounded, and disclosed**; otherwise it becomes the **weakest link in the audit chain**.

## Annotations


## Sources
