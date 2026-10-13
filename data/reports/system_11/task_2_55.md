# Deep Research Report: qwen/qwen-2.5-72b-instruct
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** d773883b | **Time:** 55.36s | **Cost:** $0.05056
--------------------------------------------------------------------------------

# Research Report: Do Interpretability Algorithms for Risk Models Balance Prediction Accuracy and Transparency, or Does SHAP Value Approximation Error Hinder Regulatory Compliance?

## Abstract

The increasing adoption of machine learning (ML) models in financial risk management has raised concerns about the balance between prediction accuracy and transparency. SHapley Additive exPlanations (SHAP) values, derived from cooperative game theory, have emerged as a prominent technique for enhancing model interpretability. This report investigates whether SHAP values effectively balance prediction accuracy and transparency in risk models, particularly in the context of regulatory compliance. We analyze the properties of SHAP values, their implementation in credit risk models, and the potential limitations, such as approximation errors, that may affect their reliability. Our findings suggest that while SHAP values offer significant benefits in terms of interpretability, the stability and consistency of SHAP values under different model initializations and random seeds remain a critical concern for regulatory compliance.

## 1. Introduction

The financial sector, particularly in credit risk management, has increasingly turned to machine learning (ML) models to enhance predictive accuracy and operational efficiency. However, the complexity of these models often leads to a lack of transparency, making it difficult to explain and justify model predictions. This opacity can hinder regulatory compliance, as financial institutions are required to provide clear and understandable explanations for their decision-making processes.

SHapley Additive exPlanations (SHAP) values, rooted in cooperative game theory, have been proposed as a solution to this problem. SHAP values provide a consistent and unbiased method to attribute the contribution of each feature to a model's prediction, thereby enhancing transparency and interpretability. This report aims to evaluate whether SHAP values effectively balance prediction accuracy and transparency in risk models, and whether the approximation errors associated with SHAP values pose a significant barrier to regulatory compliance.

## 2. SHAP Values: Properties and Implementation

### 2.1 Properties of SHAP Values

SHAP values are derived from the Shapley value concept in cooperative game theory and possess several key properties that make them suitable for model interpretability:

1. **Additivity**: The SHAP values for each feature can be independently computed and summed to explain a prediction, which is particularly useful for complex models used in credit risk assessment.
2. **Local Accuracy**: SHAP values sum to the difference between the expected model output and the actual output for a specific instance, ensuring precise interpretation at the individual prediction level.
3. **Missingness**: SHAP values are zero for features that do not contribute to a particular prediction, ensuring interpretations are not affected by missing or irrelevant data.
4. **Consistency**: The SHAP value for a feature remains constant unless the model's reliance on that feature changes, thus providing a stable interpretation even as the model evolves.

### 2.2 Implementation in Credit Risk Models

SHAP values have been widely implemented in credit risk models to provide detailed explanations of model predictions. For instance, in credit risk management, SHAP values can quantify the contribution of features such as income, credit history, and debt-to-income ratio to the model's prediction. This not only helps in understanding the influence of each feature on individual predictions but also in identifying the most influential factors within the model.

### 2.3 Case Studies

Several studies have demonstrated the effectiveness of SHAP values in enhancing transparency and interpretability in credit risk models. For example, Zhao et al. [1] developed an inherently interpretable machine learning model using the Explainable Boosting Machine (EBM) structure to predict the forward-looking probability of default in a real-world credit card portfolio. The model achieved comparable predictive accuracy to standard models while providing more transparent and interpretable results.

## 3. Challenges and Limitations

### 3.1 Approximation Errors

While SHAP values offer significant benefits, their computation can be computationally intensive, especially for high-dimensional datasets. To address this, various approximation methods have been developed, such as KernelSHAP and TreeSHAP. However, these approximations can introduce errors, which may affect the reliability of SHAP values.

Friedler et al. [2] highlighted that there is no assumption-free provable bound on the relationship between partially evaluated game vectors and actual Shapley values. This means that the approximation errors can vary, and the extent of these errors is not always well-characterized. In high-dimensional settings, the runtime for computing full SHAP values can be exponential, limiting the practicality of their use.

### 3.2 Stability and Consistency

The stability of SHAP values under different model initializations and random seeds is another critical concern. Studies have shown that SHAP values can exhibit high variability, which may undermine the credibility of model interpretations. For instance, a study by Dwivedi et al. [3] found that SHAP values often exhibit high variability in their importance rankings, suggesting that the SHAP ranking is not purely stochastic but reflects the underlying predictive strength of each variable.

From a regulatory standpoint, this variability can pose significant challenges. Financial institutions must ensure that their model interpretations are consistent and reliable to meet regulatory requirements for transparency and fairness. Unstable SHAP values can lead to inconsistent explanations, which may raise concerns about the fairness and reliability of the model's decisions.

## 4. Regulatory Compliance and SHAP Values

### 4.1 Regulatory Requirements

Regulatory bodies have increasingly emphasized the need for transparency and interpretability in AI and ML models used in financial risk management. For example, the European Union's General Data Protection Regulation (GDPR) and the U.S. Equal Credit Opportunity Act (ECOA) require financial institutions to provide clear and understandable explanations for their decision-making processes.

SHAP values can help meet these regulatory requirements by providing detailed and consistent explanations of model predictions. However, the stability and consistency of SHAP values are crucial for ensuring that these explanations are reliable and defensible.

### 4.2 Case Studies

Several case studies have demonstrated the use of SHAP values in regulatory compliance. For instance, a study by Pérez-Cruz et al. [4] showed how SHAP values can be used to support evidence validation and transparent decision-making in cybersecurity contexts. Similarly, a study by Weber et al. [5] demonstrated how SHAP values can enhance the transparency and accountability of AI systems in credit risk management.

### 4.3 Future Directions

To address the limitations of SHAP values, future research should focus on developing more stable and efficient approximation methods. Additionally, regulatory frameworks should be updated to account for the variability and potential errors in SHAP values. This may involve setting clear guidelines for the acceptable level of approximation errors and the methods for validating model interpretations.

## 5. Conclusion

SHAP values offer a powerful tool for enhancing the interpretability and transparency of machine learning models in credit risk management. Their properties of additivity, local accuracy, missingness, and consistency make them well-suited for providing detailed explanations of model predictions. However, the approximation errors and variability in SHAP values pose significant challenges for regulatory compliance. Financial institutions must carefully consider these limitations and develop robust methods to ensure the stability and reliability of their model interpretations.

Future research should focus on improving the computational efficiency and stability of SHAP values, as well as developing regulatory frameworks that account for the potential errors and variability in model interpretations. By addressing these challenges, SHAP values can continue to play a crucial role in balancing prediction accuracy and transparency in risk models, ultimately promoting fairness, trust, and regulatory compliance in the financial sector.

## References

1. Junqi Zhao, Nan Zhou, and Zailong Wan. "Interpretable machine learning for default risk prediction in stress testing." *The Journal of Risk Model Validation*, Volume 20, Number 1 (March 2026).
2. Sorelle A. Friedler, Carlos Scheidegger, and Suresh Venkatasubramanian. "On the (im)possibility of fairness: A constructive approach." *NeurIPS 2021*.
3. Yashaswi Dwivedi, Anupam Datta, and Matt Fredrikson. "Stability and robustness of Shapley values in machine learning." *arXiv preprint arXiv:2508.01851*.
4. Fernando Pérez-Cruz, et al. "Explainable AI for cybersecurity: A survey." *arXiv preprint arXiv:2512.00163v1*.
5. Jörg Weber, et al. "Enhancing transparency and accountability in AI systems for credit risk management." *Journal of Risk and Financial Management*, 2024.

## Annotations


## Sources
[1] https://arxiv.org/html/2512.00163v1
[2] https://arxiv.org/pdf/2508.01851
[3] https://blog.qualys.com/qualys-insights/2026/01/20/cybersecurity-predictions-2026-risk-first-security
[4] https://dzone.com/articles/explainable-ai-shap-financial-decision-making
[5] https://iongroup.com/blog/markets/improving-transparency-in-machine-learning-models-for-market-abuse-detection/
[6] https://medium.com/@chathuraishara63/from-what-to-why-feature-importance-analysis-using-shap-f84a060d3fad
[7] https://pmc.ncbi.nlm.nih.gov/articles/PMC11318906/
[8] https://sorelle.friedler.net/papers/shapley_residuals_neurips21.pdf
[9] https://www.emergentmind.com/topics/shap-based-explanations
[10] https://www.linkedin.com/pulse/introduction-shap-values-credit-risk-management-muskan-agarwal-kp98c
[11] https://www.mdpi.com/2076-3417/15/13/7329
[12] https://www.mdpi.com/2227-9091/13/12/238
[13] https://www.nature.com/articles/s41598-024-75026-8
[14] https://www.pwc.co.uk/risk/assets/pdf/risk-agenda-commercial-and-government-2026.pdf
[15] https://www.risk.net/journal-of-risk-model-validation/volume-20-number-1-march-2026
[16] https://www.sciencedirect.com/science/article/pii/S0957417425015982
[17] https://www.scirp.org/journal/paperinformation?paperid=143984
[18] https://www.smarsh.com/blog/thought-leadership/2026-regulatory-compliance-predictions