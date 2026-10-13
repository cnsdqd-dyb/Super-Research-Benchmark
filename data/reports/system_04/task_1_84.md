# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 8bfd3bc4 | **Time:** 365.33s | **Cost:** $1.00742
--------------------------------------------------------------------------------

# Comprehensive Analysis of Security Interception Probability Thresholds in Payment Risk Assessment

### Key Takeaways
*   **Probabilistic Nature:** Modern payment risk assessment relies on generating a risk score (typically 0–100) representing the probability of fraud, rather than binary "yes/no" rules.
*   **Threshold Calibration:** The interception threshold is not static; it is a calculated decision boundary derived from the trade-off between **Precision** (minimizing false positives/customer insult) and **Recall** (minimizing false negatives/fraud loss).
*   **Cost-Sensitive Optimization:** The optimal threshold is mathematically determined using a **Cost Matrix**, where the financial impact of a missed fraud (chargeback, lost goods) is weighed against the cost of blocking a legitimate transaction (lost margin, lifetime value churn).
*   **Multi-Tiered Strategies:** Systems typically employ three zones: **Accept** (low risk), **Manual Review** (marginal risk), and **Block** (high risk), each defined by specific probability cut-offs.
*   **Dynamic Adaptation:** Advanced systems utilize dynamic thresholding that adjusts in real-time based on concept drift, velocity of attacks, and operational capacity for manual reviews.

---

## 1. Introduction to Payment Risk Probability Scoring

In the domain of digital finance and e-commerce, the determination of whether to accept, challenge, or decline a transaction is governed by the **Security Interception Probability Threshold**. This threshold represents the specific cut-off point on a risk probability distribution curve that separates legitimate behavior from suspected fraudulent activity.

Historically, fraud detection relied on rigid, rule-based systems (e.g., "Decline if transaction > $500 AND country != billing address"). However, these binary systems lacked nuance, leading to high false positive rates [cite: 1]. Contemporary systems utilize machine learning (ML) models—such as Logistic Regression, Random Forests, and Gradient Boosting (XGBoost)—to synthesize hundreds of data points into a single scalar value, often referred to as a **Fraud Score** or **Risk Score** [cite: 2, 3].

This score, typically normalized to a range of 0 to 100 or 0 to 1000, represents the conditional probability $P(y=1|x)$ that a transaction $x$ is fraudulent ($y=1$) given a vector of features [cite: 1, 2]. The fundamental challenge in payment risk assessment is not merely generating this probability, but determining the optimal threshold $t$ such that the decision rule $D(x)$ maximizes business utility:

\[
D(x) = \begin{cases} 
\text{Block/Intercept} & \text{if } P(y=1|x) > t \\
\text{Accept} & \text{if } P(y=1|x) \leq t 
\end{cases}
\]

Setting this threshold is a complex optimization problem involving class imbalance, financial cost asymmetry, and operational constraints [cite: 4, 5].

---

## 2. Theoretical Foundations of Threshold Determination

### 2.1 The Probability Distribution of Risk
In a perfect classification model, legitimate transactions would all have a score of 0, and fraudulent transactions would have a score of 100. In reality, the distributions overlap. The risk score serves as a signal of likelihood. For instance, a score of 30 implies a 30% chance of fraud, while a score of 95 implies near certainty [cite: 1, 2].

The default threshold in binary classification is often set at $t=0.5$ (50%). However, in payment fraud, where the class distribution is severely imbalanced (fraud often accounts for less than 0.2% of transactions), a 0.5 threshold is rarely optimal [cite: 5, 6]. Using a default threshold in such imbalanced domains typically results in high accuracy but poor recall (missing most fraud) because the model is biased toward the majority class (legitimate transactions) [cite: 7].

### 2.2 The Precision-Recall Trade-off
The selection of the threshold $t$ dictates the balance between two competing metrics:
1.  **Precision (Positive Predictive Value):** The percentage of flagged transactions that are actually fraudulent. High precision minimizes **False Positives (FP)**, reducing customer friction and "insult rate" [cite: 8, 9].
2.  **Recall (Sensitivity):** The percentage of actual fraud cases that are successfully detected. High recall minimizes **False Negatives (FN)**, reducing direct financial loss from chargebacks and stolen goods [cite: 8, 9].

There is an inverse relationship between these metrics relative to the threshold:
*   **Raising the Threshold (e.g., $t=0.9$):** Increases Precision but decreases Recall. The system becomes "conservative," blocking only the most obvious fraud. This reduces false positives but allows more sophisticated fraud to pass undetected [cite: 8].
*   **Lowering the Threshold (e.g., $t=0.1$):** Increases Recall but decreases Precision. The system becomes "aggressive," catching more fraud but blocking many legitimate customers (high false positive rate) [cite: 8, 10].

---

## 3. Cost-Sensitive Threshold Optimization

Academic and industry consensus suggests that threshold setting must be treated as a **Cost-Sensitive Learning** problem rather than a pure accuracy maximization problem [cite: 11, 12]. This approach integrates the financial consequences of decisions directly into the threshold calculation.

### 3.1 The Cost Matrix
To determine the optimal threshold, organizations construct a Cost Matrix that assigns a financial value to each quadrant of the confusion matrix [cite: 4, 11, 13].

| Prediction \ Actual | Fraud ($y=1$) | Legitimate ($y=0$) |
| :--- | :--- | :--- |
| **Intercept (Predict 1)** | **True Positive (TP)** <br> *Benefit:* Saved value of goods ($V$) <br> *Cost:* Operational cost of review ($C_{admin}$) | **False Positive (FP)** <br> *Cost:* Lost margin ($M$), Customer Insult/Churn ($C_{churn}$), Review cost ($C_{admin}$) |
| **Accept (Predict 0)** | **False Negative (FN)** <br> *Cost:* Chargeback fees ($C_{cb}$), Cost of goods sold ($V$), Reputational damage | **True Negative (TN)** <br> *Benefit:* Margin earned ($M$) |

### 3.2 Minimizing Total Cost of Fraud (TCOF)
The objective function for setting the threshold is to minimize the expected Total Cost of Fraud (TCOF) [cite: 14, 15]. The expected cost $E[C]$ for a given threshold $t$ can be expressed as:

\[
E[C]_t = P(FN|t) \cdot C_{FN} + P(FP|t) \cdot C_{FP} + C_{admin}
\]

Where:
*   $C_{FN}$ (Cost of False Negative) includes the transaction value, chargeback fees, and administrative overhead. This is typically the highest individual cost [cite: 7].
*   $C_{FP}$ (Cost of False Positive) includes the lost profit margin on the sale and the estimated lifetime value (LTV) loss due to customer churn [cite: 14, 16].
*   $C_{admin}$ represents the cost of manual review or step-up authentication (e.g., 3D Secure costs) [cite: 14].

Because $C_{FN}$ (e.g., \$2,500 loss) is often significantly higher than $C_{FP}$ (e.g., \$100 loss), the optimal threshold is usually shifted downward (lower than 0.5) to prioritize Recall, even at the expense of some Precision [cite: 7, 13]. However, if the volume of legitimate transactions is massive, a slight drop in Precision can overwhelm operations with False Positives, necessitating a higher threshold.

### 3.3 Bayes Minimum Risk Threshold
A theoretically rigorous method for calculating the threshold is the **Bayes Minimum Risk** criterion. The optimal threshold $t^*$ can be derived from the cost matrix as follows [cite: 17]:

\[
t^* = \frac{Cost(FP) - Cost(TN)}{Cost(FP) - Cost(TN) + Cost(FN) - Cost(TP)}
\]

In many fraud contexts, the cost of correct decisions (TN and TP) is normalized to zero, simplifying the formula to a ratio of the cost of errors. If the cost of missing a fraud is 10 times the cost of blocking a good user, the threshold should be adjusted to reflect that asymmetry [cite: 11, 12].

---

## 4. Multi-Tiered Interception Strategies

In practice, payment risk assessment rarely uses a single binary threshold. Instead, a **Multi-Tiered Thresholding** approach is employed to manage ambiguity [cite: 1, 3, 18]. This creates three distinct zones of action:

### 4.1 The Green Zone (Automatic Acceptance)
*   **Range:** $0 \leq Score < t_{low}$
*   **Action:** Immediate authorization.
*   **Logic:** Transactions with scores below $t_{low}$ (e.g., < 15) exhibit strong signals of legitimacy (e.g., correct billing address, known device, low velocity) [cite: 1].
*   **Goal:** Maximize conversion and user experience (frictionless flow).

### 4.2 The Grey Zone (Manual Review / Step-Up)
*   **Range:** $t_{low} \leq Score < t_{high}$
*   **Action:** Manual Review, 3D Secure (3DS) challenge, or SMS verification [cite: 3, 19, 20].
*   **Logic:** Transactions in this band (e.g., 15–85) carry conflicting signals. They are too risky to auto-approve but too potentially valuable to auto-decline.
*   **Threshold Setting:** The width of this band is determined by operational capacity. If the fraud team can only review 500 cases per day, $t_{low}$ and $t_{high}$ are adjusted to ensure the volume of "Grey Zone" transactions matches this capacity [cite: 21, 22].

### 4.3 The Red Zone (Automatic Block)
*   **Range:** $t_{high} \leq Score \leq 100$
*   **Action:** Pre-authorization decline or rejection.
*   **Logic:** Scores above $t_{high}$ (e.g., > 85) indicate a probability of fraud so high that the cost of review exceeds the potential profit, or the certainty of fraud renders review unnecessary [cite: 1, 23].
*   **Goal:** Stop financial loss immediately.

---

## 5. Dynamic and Adaptive Thresholding

Static thresholds (e.g., "always block > 90") degrade over time due to **concept drift**, where fraudsters adapt their tactics to bypass known rules [cite: 16, 24]. Advanced systems employ dynamic thresholding strategies.

### 5.1 Context-Aware Thresholds
Thresholds may vary dynamically based on transaction attributes:
*   **Transaction Value:** A \$5,000 transaction may have a stricter (lower) acceptance threshold than a \$5 transaction because the financial risk ($C_{FN}$) is higher [cite: 13].
*   **Merchant Vertical:** High-risk verticals (e.g., digital goods, crypto) may require lower thresholds compared to low-risk verticals (e.g., grocery delivery) [cite: 25].
*   **User Profile:** A "VIP" customer with a long history might be evaluated against a more lenient threshold than a guest user [cite: 1].

### 5.2 Real-Time Calibration
Machine learning models, such as **Temporal-Attention Isolation Forests**, treat threshold selection as an adaptive component. These systems monitor the distribution of anomaly scores in streaming data. If a sudden bot attack causes a spike in high scores, the system can dynamically adjust the blocking threshold to maintain a stable rejection rate or react to the specific attack signature [cite: 26, 27].

### 5.3 Velocity-Based Thresholds
Risk threshold rules often incorporate velocity checks (e.g., number of transactions per hour). If a specific customer exceeds a velocity limit, the probability threshold for their subsequent transactions may be dynamically lowered, making the system more sensitive to minor anomalies [cite: 28].

---

## 6. Operational Validation and Governance

Setting the threshold is not a "set and forget" activity. It requires rigorous validation and governance processes.

### 6.1 Backtesting and Out-of-Time (OOT) Validation
Before deploying a new threshold, risk teams perform **Backtesting** on historical data. They simulate how the new threshold would have performed on past transactions to estimate the resulting False Positive Rate (FPR) and Fraud Detection Rate (FDR) [cite: 29, 30].
*   **OOT Validation:** To account for overfitting, the threshold is tested on an "Out-of-Time" dataset (e.g., training on Jan-Mar data, testing on Apr data). A steep drop in Precision-Recall AUC in the OOT set indicates the threshold may not hold up in production [cite: 31].

### 6.2 Champion/Challenger (A/B Testing)
To minimize deployment risk, organizations use a **Champion/Challenger** framework.
*   **Champion:** The current live threshold (e.g., Block > 80).
*   **Challenger:** A new proposed threshold (e.g., Block > 75).
*   **Method:** A small percentage of traffic (e.g., 10%) is routed to the Challenger strategy. The performance (conversion rate vs. fraud rate) is monitored. If the Challenger yields a better TCOF, it replaces the Champion [cite: 22, 32, 33].

### 6.3 Feedback Loops
The "Ground Truth" of fraud often arrives weeks later in the form of chargebacks. This delayed feedback loop is used to retrain models and recalibrate thresholds. If a specific score range (e.g., 70–75) begins generating unexpected chargebacks, the threshold for manual review ($t_{low}$) may be lowered to capture this shifting risk [cite: 16].

---

## 7. Metrics for Threshold Evaluation

When determining the effectiveness of a set threshold, specific metrics are prioritized over simple accuracy:

*   **F2-Score:** Unlike the F1-score which treats Precision and Recall equally, the F2-score weights Recall higher. This is often preferred in payment risk because the cost of missing fraud (FN) is usually higher than the cost of a false alarm (FP) [cite: 5].
*   **Precision-Recall (PR) Curve:** In highly imbalanced datasets, the ROC curve can be misleading. The PR curve provides a more accurate visualization of the trade-off between catching fraud and bothering good customers. The optimal threshold is often chosen at the "elbow" of this curve or at a specific precision target (e.g., "Maximize Recall s.t. Precision $\geq$ 90%") [cite: 9, 34].
*   **Matthews Correlation Coefficient (MCC):** Used to evaluate the quality of binary classifications in imbalanced datasets, providing a balanced measure even when fraud classes are very small [cite: 5].

---

## 8. Conclusion

The setting of security interception probability thresholds in payment risk assessment is a sophisticated exercise in **financial optimization**. It moves beyond simple binary rules to a probabilistic framework that balances the **cost of fraud** against the **cost of friction**.

Optimal thresholds are derived using **Cost-Sensitive Learning** techniques, validated through **Out-of-Time testing**, and implemented via **Multi-Tiered strategies** that allow for nuanced responses (Accept, Review, Block). As fraud vectors evolve, the industry is increasingly moving toward **Dynamic Thresholding**, where decision boundaries adapt in real-time to the changing economic and threat landscape, ensuring that security measures remain robust without stifling legitimate commerce.

**Sources:**
1. [sift.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmsVAT_-dPgMYWkMtDv10bUnF1HRyOGXmWip8T2KsGUES591bnizh-sjwXlCtTXoodP0a2o7YLjOjxFZG7_VxeQQCSBDNX_sE0nBxw3zwc7aWDUZVFL1d-XJjpq7xORqxEe5whnWwTd-u3D9qMFZLjfKf5VtAEDQ0JBjGWs8dwsa_g_cEfbOr2NlVD)
2. [blackbaud.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHx0vUdc4at37SOj1csB99LvmVXSlOaSzUhn4OvGSycnq7_DzS76Cdby-RGnW3CX6r_XEbk2w8GOMOmKhCc9IRzYfWmgukmh-fvA38MkHyPnCjrofi8ax9NnvXf0LNMKRm6AluVrUg0zpabbkTjH0eGXFyz)
3. [seon.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgXtV9bgiJp9AuQNtTrxO1TlH0n5fvk77QDz2DEOXSZYzOqgVdhDFwhbkMFQINoQ8bKQoiUoHi5jqQOk8w3wp9FBZ8hhVyHVFGY-eEjQ9b1kdsqC2yHSe6C_xRfsGpyjuuP8t_SsCbUkxpO6h4IC9WTZ0-)
4. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPyo9MQJsipTd3DrBBxJZKsSEYjNpRj2TzKrTm12v3ldaD8a5hFFCpOdBISS1nZLyxHXFPDa4p7jaJXIprBI0zYB11EwiiOLK12ey8IqwatqAd-LSunRSXQHobhSj4J6EiIBfUpI7U-e46HUq0FrXRxue3mkTXHGlPiikf1x1Ka6lVpKZ6xJrWma3YX8zG9YeEYBNy6YnGSGhopGHbpKpLzeIQWRm-tj6PFw==)
5. [irjmets.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkoyabYrZ11NEUfFzrBdFPU_p2efgttD9TjlAUcvnPJBKkMTiFWYAkzJpOmXmkW_QyNNyiO5G3L4z-xzNKYTqZL4SnYgssovbAdrG3hXOSycv_Z7FyIXH3T3pplu3kbZPc2pGoyihuUgnkG3xSTSmI1kZ7VN3LMaRO1QlCXv1CxmBv49YdQtXvuXgkgIzWKobgNQ==)
6. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqzAhPN5NFnYcZW5qisWBOXtFkpWoalDp_V2b9DFSr0WpxzwCpoZZSpQOb-GIAz2RygJ3y0YMixrqiugQe6WN5sAbffIT8pidIUm0qCD6YMbzsgZTVxf13MmWO3GVoClETNDMLBy-a_G0oHSr_pEAXRupGb2FfyIi_nS8Vvylp3B9SPKUMhG6x7uOfORdDBi29kojFQj3j5DV8ut6ARfTBRL9QfVJTIGccuNKtXfy4CwzbmPjAw3RmxUZpIyemSKClIA4XcnzCH1NNQvvuIEkN1PP2PsySa70HFPhEPNMbDlcVgW7GFkXZI4iLsqM=)
7. [kount.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHb9utqV1ujt6YM-KNzhYuj3hPPOCFK65tVbUuAdPavVlEmKyULU4RLVPLQrEIiZlWl-F7fIMJT9UPP_jdurzvA2z3yO7TgVjIHkmi5xcWYOG64O6aZd_qDgRlQuD98heb5ofsY90vRONRnS8zM9sTw0ppcT6QaKIgaleSfB-YyWrL1VQV2vgQe)
8. [spotintelligence.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9h3X9PhXs2rwAt2fT3SGzvKdud2HAgVY7fjzDhXIXrB-jBAPGnyahDFTJe5iR8sgD6XEP74_UhSY0IxVpiaaHtpHbtRUpfAefQt3Wtk0LEU_49OWsaT_b-ZuJwCpe3n4mC7ZwRrRADM-HzVy8JPmEan6-)
9. [cesarsotovalero.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFs965s0lQnLTfF_yyCwcRr2OfNkRBujwNYlb3Dj9mKd_Q29RT2ba-GQdKrFLuq1gwh98_9VA8T-J5X51Ctt8A9oerFD8sy5XtZzd60mG5SgtbQzCA55LHTIuN2dqhI5yGwrW1c4IAYFaLC4qQtynxM7iwGFgWOeF-JM8eXzAtdIIhzqdNnfO3nZDemwLfE5UHtiLcvkwX-AsGXm2OGYqPlUHAJOQ==)
10. [apxml.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG08iTZ1rCs8-8_trm_s_baqIh7pYPmKJ8Glqvh9RJIbQKRXwPrs4a_LZ4RhjMuH0kbvy8emgiRksLcucpNbdfYkkPcegtBgY0Pi1u_fW1-kC1eWH4dtVfa6AJDbmk8Mz_OO6HVVhBJ6qFTABsePFlR-xpIBFiYV-6g_aN8CdzPKniqnh6nTteuegxZa4DtYAKcM-yZHf9D3mAlwEEYjL_yEQynqgSuNP5qg9dxndo=)
11. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzV98tgF2hEzVZHzfv04gJR-XRcMxbImtcrE5OkFp5-JwPHEjqkaosF1tavVc1x50hPyu2PRf65iomGctAK6l9FndYihmGBxP-J8nua7qzfyqFVpTtjHxCz-ITVLtdxZDgMKePXSlcEcrA-Cl3wBOKnHR0yqp7aJFiAcqbmRErVgz0kdQLXiCfogI-ASxKdphnXI8CFaGAzBWYIcksoC0YprW6GuKUlZvmOkAdlnDF66BFhk1fClSyPTJqv9HINN8=)
12. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeLx5lHZivbbJQ0rVt0w2M1qprDVXnLX_DMlybN3rHUBldbyzRcSWdJuVuN_mRWCFnIzcxEXWcClsSF32bXikC16oNgr9cesVthALuMeu8Hv5cimrOqX4IULf0UhjKvOjLcaSLs7YTzhakaD7Yx7rmWCElxv-NoGOMZx09A3V-JxRcyg5x7-ad8QsCv76xBbEHjVrSw_bIDMc=)
13. [scikit-learn.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHnFNMdybclSkxoeKok2IAtxp5PzrVlkta6CaHtG5OpIPfGYtNJAUWXoJQZ-UkjpjCg4qm0QOCdNRR1_RrW4R8WTFNW4T--BtXwP4E1WJucJ3m0AS-53klRyNDFwar_BMWzEyvVltC3Sya1w3H598Fp-6cod6WeQIUbHplpu0z4X3X0d8dahPLd5fnpjGNxZlVPGiODQ==)
14. [datavisor.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRwvXUpsS47fgS6dTtnPfq9HijGK2FXVK8dog2hCnS7igalhbwq7lKdjVQdJu7A5zlboQcAVRohWluE2AoX7kNThxyrijd-fddoWA8edIf3zdRy7ljrkdG5Se-PKQE6PwY8AbOEaX90W1czQgne6cwjjXx39j6_ddcxLMuIE6t7DFAvA-jZ94sjYQptC7cfLBZurRE)
15. [bankinfosecurity.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMpJ_J-WI0AsWrqVkguK6Ibp9ew48Ugy-7EBBJImlgfEjciubRu-Bx_IgwGDpcnfcPn2rxK-hFfOFLACTEJGMqAqMAghaEz0dHxQzTXmmlU8XD518TciW-mOcHToIYVtK6USmx_nly795WR9KhfuxFUjWhePkKUEGzi-E=)
16. [forbes.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAkUoP4dcrcRTBtTWRGY1HJlMKm8OsDx_baqH1_voOGUS5UOR93dvYPgutEb62eNwml7j4s5J8r4Na-bWnuCl_mMFWz6kb1oKOW0aP9FY4HJSAKz7HsRLZCWhFniP6nScn4MO5bVXrsubxknfkedBOPOBVjVGu6rCgtkqo_YCl2AwXNgvRitfBghDKZUY2GVOpMT11ICxBVRKOA7u4Zw5CB-VZEWTyVLfGiXwSTp-E8QD9k3y6Ijxtbh7jLS7a97LbWhxtgCBTNDt4tofg-xcv5wPeYw==)
17. [mlr-org.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWClq6hGa_x2ljrlhxMp4QbIIJjzNPnzQ-N-YF-Xpj0lajdwXrTLF-gJdbGAdaBnb5lhu7AVpKpGTJK6LnEXlP4Jhcp3YO2cN_30opptwfj5DQbj7ZT31oUzfya3UDxYrZMwonP_cdh3VTX5YaG9YV3XSR40JAKi_9juc=)
18. [plaid.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_2bUIqJsV_REZYbO0BAj27Mm1HQK51oj8cHLAClnzU5haypej6g4uMsBvT8WsFBV6JpSGmTuyI0qIxU6YDmNIzKvf25uxsHdE5UZF3RaC5lrWRmNr2ZE-adM437jbwaklVtGG4Yee72pZqctV7nYFSkO6)
19. [stripe.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5MOJwock7aobklkbpFdXdbxlXI6bWi27EKCzV5qvV0DqRSXyJXlJRaYUx8xRovqFDVm5fe4huQnQIQ8UGVIXjR6rYUBEOOk9V_ZCB5HicXOGJFXc-MQoVdx-NBd7KJUzg)
20. [squareup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3I6nVdOwPWPArUbfZFQ1plQ0RxZK9qHM9XjcJiG11L76LQcHTB_e-7928JagERrP16KSHSy4pGlK5sAlJJ53eDb0XGZE1JxhZuBSU-lm35_2unqMi5kvH4eaNl08sNwxaN81aTM3FUknUETKDX445ngJaeTfd3wkUY97dnsfgls2psC4C5fKuxABl7hp_XOAk)
21. [maxmind.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBB0PdtuXCZxfb_uQNcBdtOmaFonW04EciIDufIVeBAFwFTHxeMZPpS0LM8Iih8Kd86KL9N36N90EE8k-gUofWN8r-kID_mfkKgiwtJDVtq6I61uYBiBhZii58kktbtfjCUKpucDCOf0HU1eo6lk5cwK9spLegb12UVXnodHtDaRdsQNP_y6FlFNpGzSd2qK7D)
22. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE41WvJBheXMCPJ2VwW4Mh_HTbBFqJTwO_mypCoM3YKYirkwP5ocIGKQ-evbMa3bpDF7bk7iZLOPYRg2pQAtxqQOlldKrRlZNzV97yS1ni4cXwuIboRuR7lxzyS8ckh2ibsOSm4ojrmB7o20kw55h3JOR4CL292lg8WYOJAHP9WbEiFUcTCLg5fLj-mu36WfydGGUn6_3YkJ5CV0BiCXhEImY4BCg9eWWDj7EMApzBFAftF8oV_6oECbh7JZ766XkaDRi-rgOGszg==)
23. [adyen.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGH5GLE9XAoso4Oq4tzb4x35Yk3aI-oyjcmpWx2khh2LJDDIJ2AIdqZvkpw-LiYF-w0qvyXkLzzjbde_GBQylogggeird39g2T9JxZB9GGiNWF7ViQDhX0TvMjDEQbNvg-oPpgFMl7oi2Cd4bSRwYYBbwZf9PX6CR0GJ52tNN5Hr-OMI3Fa0NZQA6dDBmWsDjgGhkYQWOccIQW)
24. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG85GtB_KDGaztf4LlZxT9QJwCa1eOxZ02-4TSqB0NoPQ2sVT07rZt_tVTBkof8PjXZ1DOR4WmXtXJGb0ZRwW-rfblvY1UsASLWKoq1mzgkCpOSCJ_JdLT2KnHWrWcAti9QvRh82gk1TTrkT4ubLVtjevBuThRWgnzSazqEly0dokepJFFhp2N_dEn_XpNN-Reh0pD9Shu8X6J2HJT4evX6H8OkoA==)
25. [ravelin.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8v8WkBJIiHeE5xrQkeChM4zi8h2dR5D1eAf_NKIdgXIH7V7XYee9eMTXjg38q7wzDq9c-02enga-GFg_Ddo5ppaSKYrYQUp7uIvfpKJ-x9pD3sR8es3hIqU1YPylcdLPoL61NOr8YA2CWovxNckyHAhUNaH-Xl5nSzeA=)
26. [igi-global.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFC-lWK3_Gacvm1Vb0ShluyJXdEZzou1pfeM5ltoSSCQM6whXs90f404GvOF1uLly8rR_E8Wjcc4dj4CLUdYuS8l0YCsvE9P0AeKqocgdtPIyp-XYRKtxE_aEhbdFzYllo6BoJnc6y6SQTRxoGdLbHLRbtiJ3Vzu-Jn51T5DUHbhejWWMcGWhGOogCHa66Wbn4S65U0SCScvI9t1aODyOO6QO9GZgeRFliuyA==)
27. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiGcQL14Ig_k7OOyQB5DYP160BTixrLAwKPvijcGbJsLdZ1vAlXsBGRfwv0CMuyL58gGjVPADSQoKRMN_Wz3dS-7I760wDA-reBcunCIWObeUcakO3B1BfVUVqnKFM8hPbRL_xxOAgZ88fvR7wL44lewKu_8rs02ZDV8D65DhTy3hSq4M5kdZGi2iHZ-T6qYD993iByVe42i7fEWT0oIZI9DZlRLYM6-CrPtgu9y8FVPsVhLOPVakkkXsDy9xNFPPRA6Y-S5lTwIy0ZERv4PeG1cWYp8VuTaK7hzD5bGK0dNHCNiS_7AsI5OfHKw==)
28. [paypal.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwHRMqwya8DiicG8eH3tGu0s9fG03RVqO7fnapoiBZleL5IEQeMHXT9dRQL7RpW7JUJRNUEUfLL3d2PLaxtPv_ZL-vKoUQq6FYqgERtFb_YHvj_Hv3IVUr-4-EQfrmqZTVdFA4aEFiUyoB3ouzeHgR9O8bDj90EfDSVLk0o01tEWu4rJiD_ySu2NG6dFg1guaAKsg=)
29. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFslnz2yNgjkFaSlUKrVoEiy6gbq1S76bNiS-Lwn8zotVXBRZWMdw8B6hCF6IobOYn0YodJ2zEbY9I-lJWSPrerKOaTp2cTVwo-1gkNAPM1SAAJDPRNqFA_nDYGHJzpryQXETK6qyg0SItceO1iWoJ9X1vp25m8EMNpV41eUZtnpSk_iXR_DfK9nnSeAVgV2_pWPdmxpCiQQix1FnCMdmmUKYBeiT175u8z7wAQNsTUfMXREjjnaffqC9s=)
30. [sardine.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtalWLeV2Q8JAZ2IluXQJ8Pgpjz9AO9ZadgPMyZwu-Yg_XrryEOCowOs5MYnxh5YUzqLHTPblNdGkCxjMuQGGoGl9_UYXnXtggI4N1KTm3CmntCfifj_31cRZuL5E=)
31. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF66SGKADXx4_DP5e0edak8FOPjonemM7f9sVM_QrNGX9wG76_bPqEIkS_3p4l1KTaWOwFlk6JXIXRagye87veywOnq1HEF3wkb02tTTGbdx4l_-WOD3MhLGku4v756jyr3_JwbZNcLFgNOSsbc9ijJaRvIDvbcJNsomyWYk5PZDa-PkbbX8oVbv7h1Hu6d03nFi6SYxpGdzPqd0Rwq)
32. [adyen.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEIRRpKE4Y8VkGa9ajNJQ-kD0_o6MgzhI7ueiOadDeKPzjcUdzMDanu4WVCfBet0INaUy1MaxPAO7aHRFfgnfvoGIkakT5QXKBB-V3_f6WU2xLujQ3lid-4RLNn01lbhxob6WUhw5vmMLFNKmF8xNDb-Ysju5ZEJoUPCicMrIHFhTUOyaFb7UboSRx)
33. [fico.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGn_jmFagBLGDXBGiKMD2R8WkbPRQItxK-Vmk8pRvKATGOSpEn7UPB8Fxns3IIgPsamQZLRqqCBXtqhDMAoR4QwElO_-qB7vAlom5_gbcnBvwyzOahVDcGmO1Nx4zOXkpG4iPM1vO0cU71KTV1_EEgYDeHkQSdfJe0=)
34. [github.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFAYjj49p66Rdh0Y4oMIxJByRSgNUuPTZgv2pWLNfY7zyh_QlUrdYpmC67S1eKvaIrL8IJoEmgVuAOGjGasmFl_xQJOb1UjLeD3oOVwumUWjJvOG_oAX7rKB52ztXmaE_QFgJmvbYQfYlpbOrV1o_wzsrLsz5foYY-0I49n7-3vqSVAwavb2jAjM5wRErUk0OJymbqoCmyPFwDYeoFGncw26v-1KfQt2j6)


## Annotations
Annotation(end_index=1896, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmsVAT_-dPgMYWkMtDv10bUnF1HRyOGXmWip8T2KsGUES591bnizh-sjwXlCtTXoodP0a2o7YLjOjxFZG7_VxeQQCSBDNX_sE0nBxw3zwc7aWDUZVFL1d-XJjpq7xORqxEe5whnWwTd-u3D9qMFZLjfKf5VtAEDQ0JBjGWs8dwsa_g_cEfbOr2NlVD', start_index=1887)
Annotation(end_index=2172, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgXtV9bgiJp9AuQNtTrxO1TlH0n5fvk77QDz2DEOXSZYzOqgVdhDFwhbkMFQINoQ8bKQoiUoHi5jqQOk8w3wp9FBZ8hhVyHVFGY-eEjQ9b1kdsqC2yHSe6C_xRfsGpyjuuP8t_SsCbUkxpO6h4IC9WTZ0-', start_index=2160)
Annotation(end_index=2172, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHx0vUdc4at37SOj1csB99LvmVXSlOaSzUhn4OvGSycnq7_DzS76Cdby-RGnW3CX6r_XEbk2w8GOMOmKhCc9IRzYfWmgukmh-fvA38MkHyPnCjrofi8ax9NnvXf0LNMKRm6AluVrUg0zpabbkTjH0eGXFyz', start_index=2160)
Annotation(end_index=2379, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmsVAT_-dPgMYWkMtDv10bUnF1HRyOGXmWip8T2KsGUES591bnizh-sjwXlCtTXoodP0a2o7YLjOjxFZG7_VxeQQCSBDNX_sE0nBxw3zwc7aWDUZVFL1d-XJjpq7xORqxEe5whnWwTd-u3D9qMFZLjfKf5VtAEDQ0JBjGWs8dwsa_g_cEfbOr2NlVD', start_index=2367)
Annotation(end_index=2379, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHx0vUdc4at37SOj1csB99LvmVXSlOaSzUhn4OvGSycnq7_DzS76Cdby-RGnW3CX6r_XEbk2w8GOMOmKhCc9IRzYfWmgukmh-fvA38MkHyPnCjrofi8ax9NnvXf0LNMKRm6AluVrUg0zpabbkTjH0eGXFyz', start_index=2367)
Annotation(end_index=2870, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkoyabYrZ11NEUfFzrBdFPU_p2efgttD9TjlAUcvnPJBKkMTiFWYAkzJpOmXmkW_QyNNyiO5G3L4z-xzNKYTqZL4SnYgssovbAdrG3hXOSycv_Z7FyIXH3T3pplu3kbZPc2pGoyihuUgnkG3xSTSmI1kZ7VN3LMaRO1QlCXv1CxmBv49YdQtXvuXgkgIzWKobgNQ==', start_index=2858)
Annotation(end_index=2870, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPyo9MQJsipTd3DrBBxJZKsSEYjNpRj2TzKrTm12v3ldaD8a5hFFCpOdBISS1nZLyxHXFPDa4p7jaJXIprBI0zYB11EwiiOLK12ey8IqwatqAd-LSunRSXQHobhSj4J6EiIBfUpI7U-e46HUq0FrXRxue3mkTXHGlPiikf1x1Ka6lVpKZ6xJrWma3YX8zG9YeEYBNy6YnGSGhopGHbpKpLzeIQWRm-tj6PFw==', start_index=2858)
Annotation(end_index=3326, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmsVAT_-dPgMYWkMtDv10bUnF1HRyOGXmWip8T2KsGUES591bnizh-sjwXlCtTXoodP0a2o7YLjOjxFZG7_VxeQQCSBDNX_sE0nBxw3zwc7aWDUZVFL1d-XJjpq7xORqxEe5whnWwTd-u3D9qMFZLjfKf5VtAEDQ0JBjGWs8dwsa_g_cEfbOr2NlVD', start_index=3314)
Annotation(end_index=3326, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHx0vUdc4at37SOj1csB99LvmVXSlOaSzUhn4OvGSycnq7_DzS76Cdby-RGnW3CX6r_XEbk2w8GOMOmKhCc9IRzYfWmgukmh-fvA38MkHyPnCjrofi8ax9NnvXf0LNMKRm6AluVrUg0zpabbkTjH0eGXFyz', start_index=3314)
Annotation(end_index=3591, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqzAhPN5NFnYcZW5qisWBOXtFkpWoalDp_V2b9DFSr0WpxzwCpoZZSpQOb-GIAz2RygJ3y0YMixrqiugQe6WN5sAbffIT8pidIUm0qCD6YMbzsgZTVxf13MmWO3GVoClETNDMLBy-a_G0oHSr_pEAXRupGb2FfyIi_nS8Vvylp3B9SPKUMhG6x7uOfORdDBi29kojFQj3j5DV8ut6ARfTBRL9QfVJTIGccuNKtXfy4CwzbmPjAw3RmxUZpIyemSKClIA4XcnzCH1NNQvvuIEkN1PP2PsySa70HFPhEPNMbDlcVgW7GFkXZI4iLsqM=', start_index=3579)
Annotation(end_index=3591, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkoyabYrZ11NEUfFzrBdFPU_p2efgttD9TjlAUcvnPJBKkMTiFWYAkzJpOmXmkW_QyNNyiO5G3L4z-xzNKYTqZL4SnYgssovbAdrG3hXOSycv_Z7FyIXH3T3pplu3kbZPc2pGoyihuUgnkG3xSTSmI1kZ7VN3LMaRO1QlCXv1CxmBv49YdQtXvuXgkgIzWKobgNQ==', start_index=3579)
Annotation(end_index=3807, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHb9utqV1ujt6YM-KNzhYuj3hPPOCFK65tVbUuAdPavVlEmKyULU4RLVPLQrEIiZlWl-F7fIMJT9UPP_jdurzvA2z3yO7TgVjIHkmi5xcWYOG64O6aZd_qDgRlQuD98heb5ofsY90vRONRnS8zM9sTw0ppcT6QaKIgaleSfB-YyWrL1VQV2vgQe', start_index=3798)
Annotation(end_index=4160, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9h3X9PhXs2rwAt2fT3SGzvKdud2HAgVY7fjzDhXIXrB-jBAPGnyahDFTJe5iR8sgD6XEP74_UhSY0IxVpiaaHtpHbtRUpfAefQt3Wtk0LEU_49OWsaT_b-ZuJwCpe3n4mC7ZwRrRADM-HzVy8JPmEan6-', start_index=4148)
Annotation(end_index=4160, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFs965s0lQnLTfF_yyCwcRr2OfNkRBujwNYlb3Dj9mKd_Q29RT2ba-GQdKrFLuq1gwh98_9VA8T-J5X51Ctt8A9oerFD8sy5XtZzd60mG5SgtbQzCA55LHTIuN2dqhI5yGwrW1c4IAYFaLC4qQtynxM7iwGFgWOeF-JM8eXzAtdIIhzqdNnfO3nZDemwLfE5UHtiLcvkwX-AsGXm2OGYqPlUHAJOQ==', start_index=4148)
Annotation(end_index=4386, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9h3X9PhXs2rwAt2fT3SGzvKdud2HAgVY7fjzDhXIXrB-jBAPGnyahDFTJe5iR8sgD6XEP74_UhSY0IxVpiaaHtpHbtRUpfAefQt3Wtk0LEU_49OWsaT_b-ZuJwCpe3n4mC7ZwRrRADM-HzVy8JPmEan6-', start_index=4374)
Annotation(end_index=4386, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFs965s0lQnLTfF_yyCwcRr2OfNkRBujwNYlb3Dj9mKd_Q29RT2ba-GQdKrFLuq1gwh98_9VA8T-J5X51Ctt8A9oerFD8sy5XtZzd60mG5SgtbQzCA55LHTIuN2dqhI5yGwrW1c4IAYFaLC4qQtynxM7iwGFgWOeF-JM8eXzAtdIIhzqdNnfO3nZDemwLfE5UHtiLcvkwX-AsGXm2OGYqPlUHAJOQ==', start_index=4374)
Annotation(end_index=4726, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9h3X9PhXs2rwAt2fT3SGzvKdud2HAgVY7fjzDhXIXrB-jBAPGnyahDFTJe5iR8sgD6XEP74_UhSY0IxVpiaaHtpHbtRUpfAefQt3Wtk0LEU_49OWsaT_b-ZuJwCpe3n4mC7ZwRrRADM-HzVy8JPmEan6-', start_index=4717)
Annotation(end_index=4950, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9h3X9PhXs2rwAt2fT3SGzvKdud2HAgVY7fjzDhXIXrB-jBAPGnyahDFTJe5iR8sgD6XEP74_UhSY0IxVpiaaHtpHbtRUpfAefQt3Wtk0LEU_49OWsaT_b-ZuJwCpe3n4mC7ZwRrRADM-HzVy8JPmEan6-', start_index=4937)
Annotation(end_index=4950, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG08iTZ1rCs8-8_trm_s_baqIh7pYPmKJ8Glqvh9RJIbQKRXwPrs4a_LZ4RhjMuH0kbvy8emgiRksLcucpNbdfYkkPcegtBgY0Pi1u_fW1-kC1eWH4dtVfa6AJDbmk8Mz_OO6HVVhBJ6qFTABsePFlR-xpIBFiYV-6g_aN8CdzPKniqnh6nTteuegxZa4DtYAKcM-yZHf9D3mAlwEEYjL_yEQynqgSuNP5qg9dxndo=', start_index=4937)
Annotation(end_index=5187, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeLx5lHZivbbJQ0rVt0w2M1qprDVXnLX_DMlybN3rHUBldbyzRcSWdJuVuN_mRWCFnIzcxEXWcClsSF32bXikC16oNgr9cesVthALuMeu8Hv5cimrOqX4IULf0UhjKvOjLcaSLs7YTzhakaD7Yx7rmWCElxv-NoGOMZx09A3V-JxRcyg5x7-ad8QsCv76xBbEHjVrSw_bIDMc=', start_index=5173)
Annotation(end_index=5187, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzV98tgF2hEzVZHzfv04gJR-XRcMxbImtcrE5OkFp5-JwPHEjqkaosF1tavVc1x50hPyu2PRf65iomGctAK6l9FndYihmGBxP-J8nua7qzfyqFVpTtjHxCz-ITVLtdxZDgMKePXSlcEcrA-Cl3wBOKnHR0yqp7aJFiAcqbmRErVgz0kdQLXiCfogI-ASxKdphnXI8CFaGAzBWYIcksoC0YprW6GuKUlZvmOkAdlnDF66BFhk1fClSyPTJqv9HINN8=', start_index=5173)
Annotation(end_index=5483, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHnFNMdybclSkxoeKok2IAtxp5PzrVlkta6CaHtG5OpIPfGYtNJAUWXoJQZ-UkjpjCg4qm0QOCdNRR1_RrW4R8WTFNW4T--BtXwP4E1WJucJ3m0AS-53klRyNDFwar_BMWzEyvVltC3Sya1w3H598Fp-6cod6WeQIUbHplpu0z4X3X0d8dahPLd5fnpjGNxZlVPGiODQ==', start_index=5466)
Annotation(end_index=5483, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPyo9MQJsipTd3DrBBxJZKsSEYjNpRj2TzKrTm12v3ldaD8a5hFFCpOdBISS1nZLyxHXFPDa4p7jaJXIprBI0zYB11EwiiOLK12ey8IqwatqAd-LSunRSXQHobhSj4J6EiIBfUpI7U-e46HUq0FrXRxue3mkTXHGlPiikf1x1Ka6lVpKZ6xJrWma3YX8zG9YeEYBNy6YnGSGhopGHbpKpLzeIQWRm-tj6PFw==', start_index=5466)
Annotation(end_index=5483, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzV98tgF2hEzVZHzfv04gJR-XRcMxbImtcrE5OkFp5-JwPHEjqkaosF1tavVc1x50hPyu2PRf65iomGctAK6l9FndYihmGBxP-J8nua7qzfyqFVpTtjHxCz-ITVLtdxZDgMKePXSlcEcrA-Cl3wBOKnHR0yqp7aJFiAcqbmRErVgz0kdQLXiCfogI-ASxKdphnXI8CFaGAzBWYIcksoC0YprW6GuKUlZvmOkAdlnDF66BFhk1fClSyPTJqv9HINN8=', start_index=5466)
Annotation(end_index=6209, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRwvXUpsS47fgS6dTtnPfq9HijGK2FXVK8dog2hCnS7igalhbwq7lKdjVQdJu7A5zlboQcAVRohWluE2AoX7kNThxyrijd-fddoWA8edIf3zdRy7ljrkdG5Se-PKQE6PwY8AbOEaX90W1czQgne6cwjjXx39j6_ddcxLMuIE6t7DFAvA-jZ94sjYQptC7cfLBZurRE', start_index=6195)
Annotation(end_index=6209, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMpJ_J-WI0AsWrqVkguK6Ibp9ew48Ugy-7EBBJImlgfEjciubRu-Bx_IgwGDpcnfcPn2rxK-hFfOFLACTEJGMqAqMAghaEz0dHxQzTXmmlU8XD518TciW-mOcHToIYVtK6USmx_nly795WR9KhfuxFUjWhePkKUEGzi-E=', start_index=6195)
Annotation(end_index=6534, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHb9utqV1ujt6YM-KNzhYuj3hPPOCFK65tVbUuAdPavVlEmKyULU4RLVPLQrEIiZlWl-F7fIMJT9UPP_jdurzvA2z3yO7TgVjIHkmi5xcWYOG64O6aZd_qDgRlQuD98heb5ofsY90vRONRnS8zM9sTw0ppcT6QaKIgaleSfB-YyWrL1VQV2vgQe', start_index=6525)
Annotation(end_index=6698, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAkUoP4dcrcRTBtTWRGY1HJlMKm8OsDx_baqH1_voOGUS5UOR93dvYPgutEb62eNwml7j4s5J8r4Na-bWnuCl_mMFWz6kb1oKOW0aP9FY4HJSAKz7HsRLZCWhFniP6nScn4MO5bVXrsubxknfkedBOPOBVjVGu6rCgtkqo_YCl2AwXNgvRitfBghDKZUY2GVOpMT11ICxBVRKOA7u4Zw5CB-VZEWTyVLfGiXwSTp-E8QD9k3y6Ijxtbh7jLS7a97LbWhxtgCBTNDt4tofg-xcv5wPeYw==', start_index=6684)
Annotation(end_index=6698, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRwvXUpsS47fgS6dTtnPfq9HijGK2FXVK8dog2hCnS7igalhbwq7lKdjVQdJu7A5zlboQcAVRohWluE2AoX7kNThxyrijd-fddoWA8edIf3zdRy7ljrkdG5Se-PKQE6PwY8AbOEaX90W1czQgne6cwjjXx39j6_ddcxLMuIE6t7DFAvA-jZ94sjYQptC7cfLBZurRE', start_index=6684)
Annotation(end_index=6813, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRwvXUpsS47fgS6dTtnPfq9HijGK2FXVK8dog2hCnS7igalhbwq7lKdjVQdJu7A5zlboQcAVRohWluE2AoX7kNThxyrijd-fddoWA8edIf3zdRy7ljrkdG5Se-PKQE6PwY8AbOEaX90W1czQgne6cwjjXx39j6_ddcxLMuIE6t7DFAvA-jZ94sjYQptC7cfLBZurRE', start_index=6803)
Annotation(end_index=7058, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHnFNMdybclSkxoeKok2IAtxp5PzrVlkta6CaHtG5OpIPfGYtNJAUWXoJQZ-UkjpjCg4qm0QOCdNRR1_RrW4R8WTFNW4T--BtXwP4E1WJucJ3m0AS-53klRyNDFwar_BMWzEyvVltC3Sya1w3H598Fp-6cod6WeQIUbHplpu0z4X3X0d8dahPLd5fnpjGNxZlVPGiODQ==', start_index=7045)
Annotation(end_index=7058, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHb9utqV1ujt6YM-KNzhYuj3hPPOCFK65tVbUuAdPavVlEmKyULU4RLVPLQrEIiZlWl-F7fIMJT9UPP_jdurzvA2z3yO7TgVjIHkmi5xcWYOG64O6aZd_qDgRlQuD98heb5ofsY90vRONRnS8zM9sTw0ppcT6QaKIgaleSfB-YyWrL1VQV2vgQe', start_index=7045)
Annotation(end_index=7456, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFWClq6hGa_x2ljrlhxMp4QbIIJjzNPnzQ-N-YF-Xpj0lajdwXrTLF-gJdbGAdaBnb5lhu7AVpKpGTJK6LnEXlP4Jhcp3YO2cN_30opptwfj5DQbj7ZT31oUzfya3UDxYrZMwonP_cdh3VTX5YaG9YV3XSR40JAKi_9juc=', start_index=7446)
Annotation(end_index=7839, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHeLx5lHZivbbJQ0rVt0w2M1qprDVXnLX_DMlybN3rHUBldbyzRcSWdJuVuN_mRWCFnIzcxEXWcClsSF32bXikC16oNgr9cesVthALuMeu8Hv5cimrOqX4IULf0UhjKvOjLcaSLs7YTzhakaD7Yx7rmWCElxv-NoGOMZx09A3V-JxRcyg5x7-ad8QsCv76xBbEHjVrSw_bIDMc=', start_index=7825)
Annotation(end_index=7839, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHzV98tgF2hEzVZHzfv04gJR-XRcMxbImtcrE5OkFp5-JwPHEjqkaosF1tavVc1x50hPyu2PRf65iomGctAK6l9FndYihmGBxP-J8nua7qzfyqFVpTtjHxCz-ITVLtdxZDgMKePXSlcEcrA-Cl3wBOKnHR0yqp7aJFiAcqbmRErVgz0kdQLXiCfogI-ASxKdphnXI8CFaGAzBWYIcksoC0YprW6GuKUlZvmOkAdlnDF66BFhk1fClSyPTJqv9HINN8=', start_index=7825)
Annotation(end_index=8065, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgXtV9bgiJp9AuQNtTrxO1TlH0n5fvk77QDz2DEOXSZYzOqgVdhDFwhbkMFQINoQ8bKQoiUoHi5jqQOk8w3wp9FBZ8hhVyHVFGY-eEjQ9b1kdsqC2yHSe6C_xRfsGpyjuuP8t_SsCbUkxpO6h4IC9WTZ0-', start_index=8049)
Annotation(end_index=8065, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmsVAT_-dPgMYWkMtDv10bUnF1HRyOGXmWip8T2KsGUES591bnizh-sjwXlCtTXoodP0a2o7YLjOjxFZG7_VxeQQCSBDNX_sE0nBxw3zwc7aWDUZVFL1d-XJjpq7xORqxEe5whnWwTd-u3D9qMFZLjfKf5VtAEDQ0JBjGWs8dwsa_g_cEfbOr2NlVD', start_index=8049)
Annotation(end_index=8065, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_2bUIqJsV_REZYbO0BAj27Mm1HQK51oj8cHLAClnzU5haypej6g4uMsBvT8WsFBV6JpSGmTuyI0qIxU6YDmNIzKvf25uxsHdE5UZF3RaC5lrWRmNr2ZE-adM437jbwaklVtGG4Yee72pZqctV7nYFSkO6', start_index=8049)
Annotation(end_index=8415, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmsVAT_-dPgMYWkMtDv10bUnF1HRyOGXmWip8T2KsGUES591bnizh-sjwXlCtTXoodP0a2o7YLjOjxFZG7_VxeQQCSBDNX_sE0nBxw3zwc7aWDUZVFL1d-XJjpq7xORqxEe5whnWwTd-u3D9qMFZLjfKf5VtAEDQ0JBjGWs8dwsa_g_cEfbOr2NlVD', start_index=8406)
Annotation(end_index=8683, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3I6nVdOwPWPArUbfZFQ1plQ0RxZK9qHM9XjcJiG11L76LQcHTB_e-7928JagERrP16KSHSy4pGlK5sAlJJ53eDb0XGZE1JxhZuBSU-lm35_2unqMi5kvH4eaNl08sNwxaN81aTM3FUknUETKDX445ngJaeTfd3wkUY97dnsfgls2psC4C5fKuxABl7hp_XOAk', start_index=8666)
Annotation(end_index=8683, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5MOJwock7aobklkbpFdXdbxlXI6bWi27EKCzV5qvV0DqRSXyJXlJRaYUx8xRovqFDVm5fe4huQnQIQ8UGVIXjR6rYUBEOOk9V_ZCB5HicXOGJFXc-MQoVdx-NBd7KJUzg', start_index=8666)
Annotation(end_index=8683, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFgXtV9bgiJp9AuQNtTrxO1TlH0n5fvk77QDz2DEOXSZYzOqgVdhDFwhbkMFQINoQ8bKQoiUoHi5jqQOk8w3wp9FBZ8hhVyHVFGY-eEjQ9b1kdsqC2yHSe6C_xRfsGpyjuuP8t_SsCbUkxpO6h4IC9WTZ0-', start_index=8666)
Annotation(end_index=9115, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE41WvJBheXMCPJ2VwW4Mh_HTbBFqJTwO_mypCoM3YKYirkwP5ocIGKQ-evbMa3bpDF7bk7iZLOPYRg2pQAtxqQOlldKrRlZNzV97yS1ni4cXwuIboRuR7lxzyS8ckh2ibsOSm4ojrmB7o20kw55h3JOR4CL292lg8WYOJAHP9WbEiFUcTCLg5fLj-mu36WfydGGUn6_3YkJ5CV0BiCXhEImY4BCg9eWWDj7EMApzBFAftF8oV_6oECbh7JZ766XkaDRi-rgOGszg==', start_index=9101)
Annotation(end_index=9115, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBB0PdtuXCZxfb_uQNcBdtOmaFonW04EciIDufIVeBAFwFTHxeMZPpS0LM8Iih8Kd86KL9N36N90EE8k-gUofWN8r-kID_mfkKgiwtJDVtq6I61uYBiBhZii58kktbtfjCUKpucDCOf0HU1eo6lk5cwK9spLegb12UVXnodHtDaRdsQNP_y6FlFNpGzSd2qK7D', start_index=9101)
Annotation(end_index=9471, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGGH5GLE9XAoso4Oq4tzb4x35Yk3aI-oyjcmpWx2khh2LJDDIJ2AIdqZvkpw-LiYF-w0qvyXkLzzjbde_GBQylogggeird39g2T9JxZB9GGiNWF7ViQDhX0TvMjDEQbNvg-oPpgFMl7oi2Cd4bSRwYYBbwZf9PX6CR0GJ52tNN5Hr-OMI3Fa0NZQA6dDBmWsDjgGhkYQWOccIQW', start_index=9458)
Annotation(end_index=9471, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmsVAT_-dPgMYWkMtDv10bUnF1HRyOGXmWip8T2KsGUES591bnizh-sjwXlCtTXoodP0a2o7YLjOjxFZG7_VxeQQCSBDNX_sE0nBxw3zwc7aWDUZVFL1d-XJjpq7xORqxEe5whnWwTd-u3D9qMFZLjfKf5VtAEDQ0JBjGWs8dwsa_g_cEfbOr2NlVD', start_index=9458)
Annotation(end_index=9730, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAkUoP4dcrcRTBtTWRGY1HJlMKm8OsDx_baqH1_voOGUS5UOR93dvYPgutEb62eNwml7j4s5J8r4Na-bWnuCl_mMFWz6kb1oKOW0aP9FY4HJSAKz7HsRLZCWhFniP6nScn4MO5bVXrsubxknfkedBOPOBVjVGu6rCgtkqo_YCl2AwXNgvRitfBghDKZUY2GVOpMT11ICxBVRKOA7u4Zw5CB-VZEWTyVLfGiXwSTp-E8QD9k3y6Ijxtbh7jLS7a97LbWhxtgCBTNDt4tofg-xcv5wPeYw==', start_index=9716)
Annotation(end_index=9730, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG85GtB_KDGaztf4LlZxT9QJwCa1eOxZ02-4TSqB0NoPQ2sVT07rZt_tVTBkof8PjXZ1DOR4WmXtXJGb0ZRwW-rfblvY1UsASLWKoq1mzgkCpOSCJ_JdLT2KnHWrWcAti9QvRh82gk1TTrkT4ubLVtjevBuThRWgnzSazqEly0dokepJFFhp2N_dEn_XpNN-Reh0pD9Shu8X6J2HJT4evX6H8OkoA==', start_index=9716)
Annotation(end_index=10067, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHnFNMdybclSkxoeKok2IAtxp5PzrVlkta6CaHtG5OpIPfGYtNJAUWXoJQZ-UkjpjCg4qm0QOCdNRR1_RrW4R8WTFNW4T--BtXwP4E1WJucJ3m0AS-53klRyNDFwar_BMWzEyvVltC3Sya1w3H598Fp-6cod6WeQIUbHplpu0z4X3X0d8dahPLd5fnpjGNxZlVPGiODQ==', start_index=10057)
Annotation(end_index=10241, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE8v8WkBJIiHeE5xrQkeChM4zi8h2dR5D1eAf_NKIdgXIH7V7XYee9eMTXjg38q7wzDq9c-02enga-GFg_Ddo5ppaSKYrYQUp7uIvfpKJ-x9pD3sR8es3hIqU1YPylcdLPoL61NOr8YA2CWovxNckyHAhUNaH-Xl5nSzeA=', start_index=10231)
Annotation(end_index=10381, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGmsVAT_-dPgMYWkMtDv10bUnF1HRyOGXmWip8T2KsGUES591bnizh-sjwXlCtTXoodP0a2o7YLjOjxFZG7_VxeQQCSBDNX_sE0nBxw3zwc7aWDUZVFL1d-XJjpq7xORqxEe5whnWwTd-u3D9qMFZLjfKf5VtAEDQ0JBjGWs8dwsa_g_cEfbOr2NlVD', start_index=10372)
Annotation(end_index=10820, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFC-lWK3_Gacvm1Vb0ShluyJXdEZzou1pfeM5ltoSSCQM6whXs90f404GvOF1uLly8rR_E8Wjcc4dj4CLUdYuS8l0YCsvE9P0AeKqocgdtPIyp-XYRKtxE_aEhbdFzYllo6BoJnc6y6SQTRxoGdLbHLRbtiJ3Vzu-Jn51T5DUHbhejWWMcGWhGOogCHa66Wbn4S65U0SCScvI9t1aODyOO6QO9GZgeRFliuyA==', start_index=10806)
Annotation(end_index=10820, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiGcQL14Ig_k7OOyQB5DYP160BTixrLAwKPvijcGbJsLdZ1vAlXsBGRfwv0CMuyL58gGjVPADSQoKRMN_Wz3dS-7I760wDA-reBcunCIWObeUcakO3B1BfVUVqnKFM8hPbRL_xxOAgZ88fvR7wL44lewKu_8rs02ZDV8D65DhTy3hSq4M5kdZGi2iHZ-T6qYD993iByVe42i7fEWT0oIZI9DZlRLYM6-CrPtgu9y8FVPsVhLOPVakkkXsDy9xNFPPRA6Y-S5lTwIy0ZERv4PeG1cWYp8VuTaK7hzD5bGK0dNHCNiS_7AsI5OfHKw==', start_index=10806)
Annotation(end_index=11152, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwHRMqwya8DiicG8eH3tGu0s9fG03RVqO7fnapoiBZleL5IEQeMHXT9dRQL7RpW7JUJRNUEUfLL3d2PLaxtPv_ZL-vKoUQq6FYqgERtFb_YHvj_Hv3IVUr-4-EQfrmqZTVdFA4aEFiUyoB3ouzeHgR9O8bDj90EfDSVLk0o01tEWu4rJiD_ySu2NG6dFg1guaAKsg=', start_index=11142)
Annotation(end_index=11639, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFslnz2yNgjkFaSlUKrVoEiy6gbq1S76bNiS-Lwn8zotVXBRZWMdw8B6hCF6IobOYn0YodJ2zEbY9I-lJWSPrerKOaTp2cTVwo-1gkNAPM1SAAJDPRNqFA_nDYGHJzpryQXETK6qyg0SItceO1iWoJ9X1vp25m8EMNpV41eUZtnpSk_iXR_DfK9nnSeAVgV2_pWPdmxpCiQQix1FnCMdmmUKYBeiT175u8z7wAQNsTUfMXREjjnaffqC9s=', start_index=11625)
Annotation(end_index=11639, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtalWLeV2Q8JAZ2IluXQJ8Pgpjz9AO9ZadgPMyZwu-Yg_XrryEOCowOs5MYnxh5YUzqLHTPblNdGkCxjMuQGGoGl9_UYXnXtggI4N1KTm3CmntCfifj_31cRZuL5E=', start_index=11625)
Annotation(end_index=11916, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF66SGKADXx4_DP5e0edak8FOPjonemM7f9sVM_QrNGX9wG76_bPqEIkS_3p4l1KTaWOwFlk6JXIXRagye87veywOnq1HEF3wkb02tTTGbdx4l_-WOD3MhLGku4v756jyr3_JwbZNcLFgNOSsbc9ijJaRvIDvbcJNsomyWYk5PZDa-PkbbX8oVbv7h1Hu6d03nFi6SYxpGdzPqd0Rwq', start_index=11906)
Annotation(end_index=12417, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE41WvJBheXMCPJ2VwW4Mh_HTbBFqJTwO_mypCoM3YKYirkwP5ocIGKQ-evbMa3bpDF7bk7iZLOPYRg2pQAtxqQOlldKrRlZNzV97yS1ni4cXwuIboRuR7lxzyS8ckh2ibsOSm4ojrmB7o20kw55h3JOR4CL292lg8WYOJAHP9WbEiFUcTCLg5fLj-mu36WfydGGUn6_3YkJ5CV0BiCXhEImY4BCg9eWWDj7EMApzBFAftF8oV_6oECbh7JZ766XkaDRi-rgOGszg==', start_index=12399)
Annotation(end_index=12417, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEIRRpKE4Y8VkGa9ajNJQ-kD0_o6MgzhI7ueiOadDeKPzjcUdzMDanu4WVCfBet0INaUy1MaxPAO7aHRFfgnfvoGIkakT5QXKBB-V3_f6WU2xLujQ3lid-4RLNn01lbhxob6WUhw5vmMLFNKmF8xNDb-Ysju5ZEJoUPCicMrIHFhTUOyaFb7UboSRx', start_index=12399)
Annotation(end_index=12417, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGn_jmFagBLGDXBGiKMD2R8WkbPRQItxK-Vmk8pRvKATGOSpEn7UPB8Fxns3IIgPsamQZLRqqCBXtqhDMAoR4QwElO_-qB7vAlom5_gbcnBvwyzOahVDcGmO1Nx4zOXkpG4iPM1vO0cU71KTV1_EEgYDeHkQSdfJe0=', start_index=12399)
Annotation(end_index=12789, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAkUoP4dcrcRTBtTWRGY1HJlMKm8OsDx_baqH1_voOGUS5UOR93dvYPgutEb62eNwml7j4s5J8r4Na-bWnuCl_mMFWz6kb1oKOW0aP9FY4HJSAKz7HsRLZCWhFniP6nScn4MO5bVXrsubxknfkedBOPOBVjVGu6rCgtkqo_YCl2AwXNgvRitfBghDKZUY2GVOpMT11ICxBVRKOA7u4Zw5CB-VZEWTyVLfGiXwSTp-E8QD9k3y6Ijxtbh7jLS7a97LbWhxtgCBTNDt4tofg-xcv5wPeYw==', start_index=12779)
Annotation(end_index=13207, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkoyabYrZ11NEUfFzrBdFPU_p2efgttD9TjlAUcvnPJBKkMTiFWYAkzJpOmXmkW_QyNNyiO5G3L4z-xzNKYTqZL4SnYgssovbAdrG3hXOSycv_Z7FyIXH3T3pplu3kbZPc2pGoyihuUgnkG3xSTSmI1kZ7VN3LMaRO1QlCXv1CxmBv49YdQtXvuXgkgIzWKobgNQ==', start_index=13198)
Annotation(end_index=13598, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFs965s0lQnLTfF_yyCwcRr2OfNkRBujwNYlb3Dj9mKd_Q29RT2ba-GQdKrFLuq1gwh98_9VA8T-J5X51Ctt8A9oerFD8sy5XtZzd60mG5SgtbQzCA55LHTIuN2dqhI5yGwrW1c4IAYFaLC4qQtynxM7iwGFgWOeF-JM8eXzAtdIIhzqdNnfO3nZDemwLfE5UHtiLcvkwX-AsGXm2OGYqPlUHAJOQ==', start_index=13585)
Annotation(end_index=13598, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFAYjj49p66Rdh0Y4oMIxJByRSgNUuPTZgv2pWLNfY7zyh_QlUrdYpmC67S1eKvaIrL8IJoEmgVuAOGjGasmFl_xQJOb1UjLeD3oOVwumUWjJvOG_oAX7rKB52ztXmaE_QFgJmvbYQfYlpbOrV1o_wzsrLsz5foYY-0I49n7-3vqSVAwavb2jAjM5wRErUk0OJymbqoCmyPFwDYeoFGncw26v-1KfQt2j6', start_index=13585)
Annotation(end_index=13804, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkoyabYrZ11NEUfFzrBdFPU_p2efgttD9TjlAUcvnPJBKkMTiFWYAkzJpOmXmkW_QyNNyiO5G3L4z-xzNKYTqZL4SnYgssovbAdrG3hXOSycv_Z7FyIXH3T3pplu3kbZPc2pGoyihuUgnkG3xSTSmI1kZ7VN3LMaRO1QlCXv1CxmBv49YdQtXvuXgkgIzWKobgNQ==', start_index=13795)

## Sources
