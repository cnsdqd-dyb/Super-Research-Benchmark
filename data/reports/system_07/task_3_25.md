# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 77fb8197 | **Time:** 14.10s | **Cost:** $0.01083
--------------------------------------------------------------------------------

The **characteristic polynomial** of an **intergenerational transfer matrix** plays a central role in determining the **Lyapunov stability** of welfare systems by revealing the **eigenvalues** that govern the **long-term dynamics** of transfers (e.g., pensions, social insurance, or education subsidies) across generations.

---

### 🔍 Step-by-Step Explanation:

#### 1. **Intergenerational Transfer Matrix (ITM):**
This is a **square matrix** \( A \in \mathbb{R}^{n \times n} \) that models how resources (money, services, or obligations) are transferred across generations. Each entry \( A_{ij} \) represents the **impact of generation j on generation i**.

#### 2. **Characteristic Polynomial:**
The characteristic polynomial is defined as:

\[
p(\lambda) = \det(\lambda I - A)
\]

Its **roots** (eigenvalues \( \lambda_i \)) determine the **qualitative behavior** of the system over time.

#### 3. **Lyapunov Stability Criterion:**
A **linear time-invariant system** like this is **Lyapunov stable** if and only if:

- All eigenvalues \( \lambda_i \) satisfy \( \text{Re}(\lambda_i) \leq 0 \)
- Any eigenvalue with \( \text{Re}(\lambda_i) = 0 \) must be **semisimple** (i.e., its algebraic multiplicity equals its geometric multiplicity)

If **any eigenvalue has \( \text{Re}(\lambda_i) > 0 \)**, the system is **unstable**: small deviations grow exponentially, implying **unsustainable welfare transfers** (e.g., pension deficits or demographic collapse).

#### 4. **Interpretation in Welfare Systems:**
- **Stable eigenvalues** → transfers converge or remain bounded → **sustainable welfare**
- **Unstable eigenvalues** → transfers diverge → **fiscal collapse or intergenerational injustice**

---

### ✅ Summary:
> The **characteristic polynomial** of the intergenerational transfer matrix reveals the **eigenvalues**, which directly determine **Lyapunov stability**. If all eigenvalues lie in the **closed left-half complex plane**, the welfare system is **stable**; otherwise, it is **unstable**, signaling **unsustainable intergenerational obligations**.

## Annotations


## Sources
