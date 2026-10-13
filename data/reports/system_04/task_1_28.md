# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 5aeede84 | **Time:** 469.55s | **Cost:** $1.66038
--------------------------------------------------------------------------------

# Smart Contract Verification in DeFi: The Tension Between Audit Efficiency, Formal Completeness, and Computational Limits

### Key Points
*   **The Efficiency-Completeness Trade-off:** Current DeFi security practices operate on a spectrum where **manual audits** provide cost-effective but fallible heuristic coverage, while **formal verification (FV)** offers mathematical guarantees that are often computationally intractable for complex protocols. The industry has not yet achieved a perfect balance; high costs (often exceeding $200,000 for FV) and technical bottlenecks force projects to prioritize critical components for formal proofs while leaving peripheral logic to less rigorous methods [cite: 1, 2].
*   **State Space Explosion as a Hard Limit:** The "state space explosion" problem remains the primary barrier to total verification. As DeFi protocols introduce loops, recursion, and cross-contract composability, the number of possible execution states grows exponentially, exceeding the memory and time limits of solvers. This forces verifiers to use abstractions or bounded model checking, which inherently creates **blind spots** where deep-state bugs can hide [cite: 3, 4].
*   **The Specification Gap:** A significant "blind spot" is not computational but human. Formal verification proves that code matches a specification, not that the code is secure. The **Euler Finance hack ($197M)** demonstrated that if a specific invariant (e.g., liquidity checks on donation functions) is not explicitly defined in the formal specification, the verification process will validate insecure code as "correct" [cite: 5, 6].
*   **Complexity in Arithmetic Logic:** The **KyberSwap exploit ($48M)** highlighted that complex mathematical logic, particularly regarding concentrated liquidity and rounding errors, creates verification blind spots. Standard symbolic execution engines often struggle with non-linear arithmetic or require simplifications that mask minute precision errors, leaving protocols vulnerable to highly specific edge-case attacks [cite: 7, 8].

---

## 1. Introduction: The Verification Crisis in Decentralized Finance

The rapid evolution of Decentralized Finance (DeFi) has transformed smart contracts from simple transactional scripts into complex, interoperable financial primitives managing billions of dollars in value. However, this innovation has been shadowed by a persistent security crisis. In 2024 alone, DeFi-related exploits drained over $1.3 billion from blockchain projects, with major incidents like the Euler Finance and KyberSwap hacks exposing fundamental weaknesses in the prevailing security paradigms [cite: 1, 7].

The central inquiry of this report addresses whether current verification methodologies have found an equilibrium between audit efficiency and formal proof completeness, or if the inherent complexity of modern DeFi logic renders such completeness impossible due to state space explosion. The evidence suggests that while formal verification (FV) provides a higher tier of security than manual auditing, it is not a panacea. It is constrained by the **state explosion problem**, where the number of possible program states expands exponentially with added variables and logic branches, rendering exhaustive verification computationally infeasible for monolithic protocols [cite: 3, 9].

Furthermore, the "blind spots" in verification are not merely technical but epistemological. A formal proof is only as good as its specification. If the "laws of physics" for a protocol are defined incorrectly or incompletely—as seen in the Euler Finance case—formal tools will fail to detect catastrophic vulnerabilities [cite: 6]. Consequently, the industry is shifting towards a "defense-in-depth" strategy that layers manual audits, fuzzing, and modular formal verification, acknowledging that "total" verification of complex, composable DeFi systems remains an unsolved challenge in computer science [cite: 10, 11].

---

## 2. The Dichotomy of Verification: Manual Audits vs. Formal Proofs

To understand the trade-offs in DeFi security, one must distinguish between the two dominant approaches: the heuristic nature of manual audits and the mathematical rigor of formal verification.

### 2.1 Manual Auditing: The Heuristic Approach
Manual auditing remains the standard first line of defense. It involves expert security researchers reviewing code line-by-line to identify logic errors, economic vulnerabilities, and deviations from best practices.
*   **Efficiency and Cost:** Audits are relatively fast and affordable compared to full-scale formal verification. A standard audit for a medium-complexity DeFi protocol typically costs between $20,000 and $50,000 and takes 1–2 weeks [cite: 2, 12].
*   **Limitations:** Manual audits are inherently prone to human error. Reviewers suffer from "cognitive load," where the capacity to track complex state transitions across multiple contracts is limited. Research suggests a hard limit on the number of active variables a human reviewer can track simultaneously, leading to "cognitive overflow" and overlooked vulnerabilities in complex systems [cite: 13].
*   **Blind Spots:** Auditors often miss subtle edge cases, such as specific rounding errors or deep-state reentrancy vectors, which do not appear in standard "happy path" execution flows [cite: 10, 14].

### 2.2 Formal Verification: The Mathematical Approach
Formal verification (FV) uses mathematical methods to prove that a smart contract adheres to a specific set of properties (invariants) under all possible behaviors.
*   **Methodology:** FV involves translating smart contract logic into mathematical models (e.g., using K-framework or Certora Verification Language) and using automated theorem provers or model checkers (like Z3) to validate properties [cite: 15].
*   **Completeness:** Unlike testing, which shows the presence of bugs, FV aims to prove the *absence* of bugs regarding specific properties. It is particularly effective at finding "deep bugs"—issues that only manifest after a specific, unlikely sequence of state transitions that a human or fuzzer would likely miss [cite: 11, 16].
*   **Cost and Scalability:** FV is resource-intensive. A comprehensive formal verification engagement for a high-value protocol can cost over $200,000 and requires specialized expertise that is scarce in the market [cite: 1].

### 2.3 The Efficiency Gap
The tension between these methods creates an efficiency gap. Projects under pressure to launch ("time-to-market") often opt for manual audits and basic automated testing, bypassing FV due to its high cost and the "specification bottleneck"—the time required to write precise mathematical definitions of protocol behavior [cite: 14, 15]. This economic reality leaves many protocols formally unverified, relying on the probabilistic security of manual review rather than the deterministic security of mathematical proof.

---

## 3. The State Space Explosion Problem

The most significant technical barrier to "complete" smart contract verification is the **state space explosion problem**. This phenomenon occurs when the number of reachable states in a system grows exponentially with the number of state variables and execution branches, exceeding the memory and computational power available to verify the system [cite: 3].

### 3.1 Theoretical Underpinnings
In model checking, a system is represented as a state transition graph. Verification involves traversing this graph to ensure no state violates a safety property.
*   **Exponential Growth:** If a contract has $n$ variables, each capable of holding $k$ values, the state space size is $k^n$. In DeFi, where contracts manage balances for thousands of users, interaction histories, and global parameters, $n$ is large, and $k$ (e.g., a `uint256`) is massive [cite: 3].
*   **Loops and Recursion:** Constructs like loops (e.g., iterating through a list of lenders to calculate interest) and recursion introduce infinite or near-infinite state spaces. Symbolic execution engines, which explore program paths mathematically, face "path explosion" when encountering these constructs, as they must fork execution for every iteration [cite: 4, 17].

### 3.2 Impact on DeFi Verification
In the context of DeFi, state space explosion forces verifiers to make compromises that introduce blind spots:
*   **Bounded Model Checking:** Verifiers often limit the search depth (e.g., "check for violations within 10 transactions"). If a vulnerability requires 11 transactions to trigger, the verification will miss it [cite: 18].
*   **Abstractions:** To make verification tractable, complex logic is often "abstracted." For example, a complex non-linear curve might be approximated as a linear function. While this allows the proof to complete, it may mask precision errors or boundary conditions present in the actual code [cite: 9].
*   **Timeout Failures:** Symbolic execution tools like Manticore or HEVM often "time out" when analyzing complex functions with multiple external calls. When a solver times out, it returns an "unknown" result, leaving that portion of the logic unverified [cite: 7, 17].

This computational limit means that for complex, monolithic DeFi protocols, **formal proof completeness is theoretically impossible** with current hardware. Verification is always partial, bounded, or abstract, leaving "blind spots" in the unexplored state space.

---

## 4. Blind Spots in Complex Logic: The Specification Bottleneck

Even if state space explosion were solved, verification would remain vulnerable to the **specification bottleneck**. Formal verification proves that *Code implies Specification*. It does not prove that *Specification implies Security*. If the specification fails to capture a necessary invariant, the code is "verified" but insecure.

### 4.1 Case Study: Euler Finance Hack (2023)
The Euler Finance exploit, which resulted in a $197 million loss, serves as a paradigmatic example of a specification blind spot.
*   **The Vulnerability:** The attacker exploited a function named `donateToReserves`, which allowed users to donate collateral to the protocol. Crucially, this function lacked a "health check" to ensure the donor remained solvent after the donation. The attacker leveraged this to create an insolvent account, trigger a self-liquidation, and drain the protocol [cite: 5, 19].
*   **The Verification Failure:** Euler Finance had undergone multiple audits and utilized formal verification components. However, the `donateToReserves` function was a new addition (part of EIP-14) and was reportedly **out of scope** for some rigorous checks, or the specific invariant ("a user must be solvent after *any* balance-decreasing operation") was not applied to this specific function [cite: 5, 6].
*   **The Lesson:** The blind spot was not in the solver's ability to check the logic, but in the human failure to apply the necessary specification to the new logic. The "completeness" of the proof was compromised by the incompleteness of the spec. This highlights that **incremental complexity** (adding new features to a verified system) often breaks security guarantees if the formal specifications are not rigorously updated and re-verified [cite: 5].

### 4.2 The "Divide and Conquer" Limitation
To manage complexity, auditors often use a "Divide and Conquer" approach, verifying components (e.g., a Vault, a Token) in isolation [cite: 13].
*   **Local vs. Global Invariants:** While this proves that components work correctly individually, it fails to verify **systemic invariants**. A component might be locally correct but unsafe when interacting with another component.
*   **Blind Spot:** The Euler hack involved the interaction between the *Liquidation* module and the *Donation* module. Isolated verification of the Donation module might not have flagged the missing health check as critical without the context of the Liquidation module's mechanics [cite: 6].

---

## 5. Arithmetic Precision and The "Dark Forest" of Math

DeFi protocols increasingly rely on complex mathematical models, such as the concentrated liquidity math in Uniswap V3 and KyberSwap. These models introduce a specific type of blind spot: **arithmetic precision errors** that are difficult for formal tools to model accurately.

### 5.1 Case Study: KyberSwap Elastic Hack (2023)
The KyberSwap hack, resulting in a ~$48 million loss, was caused by a subtle rounding error in the protocol's concentrated liquidity calculations.
*   **The Vulnerability:** The exploit involved manipulating the `currentTick` and `nearestCurrentTick` calculations. A precision error occurred where the system rounded *up* liquidity in a specific reinvestment calculation, leading to a "double counting" of liquidity when crossing tick boundaries. The error was infinitesimal—less than $0.00000000001\%$—but sufficient to drain the pool when compounded [cite: 7, 20].
*   **Verification Blind Spot:**
    *   **Non-Linear Arithmetic:** Concentrated liquidity involves square roots and exponentiation. SMT solvers (the engines behind FV) struggle with non-linear integer arithmetic. To verify these contracts, auditors often use "SafeMath" abstractions or simplified models that assume perfect precision or standard rounding [cite: 21, 22].
    *   **The "Epsilon" Problem:** Formal models often allow for a small error margin ($\epsilon$) to account for rounding. If the exploit lies *within* this accepted error margin but can be economically weaponized (as in KyberSwap), the verification will pass despite the vulnerability [cite: 22, 23].
    *   **Complexity:** The KyberSwap exploit required a highly specific sequence of swaps and liquidity provisions to trigger the rounding error. The state depth required to reach this condition likely exceeded the bounds of standard symbolic execution runs, hiding the bug in the "deep state" [cite: 8].

### 5.2 The Challenge of "Money Legos"
The KyberSwap incident underscores that as DeFi math becomes more complex (e.g., yield stripping, non-linear bonding curves), the gap between the **mathematical model** used for verification and the **EVM bytecode execution** widens. Formal verification tools that abstract away gas limits or precise bitwise rounding behavior will inevitably miss these classes of bugs [cite: 8, 24].

---

## 6. Composability: The Unverifiable Frontier

The "Money Lego" thesis of DeFi—that protocols can be stacked to create new financial products—creates a verification nightmare known as the **composability problem**.

### 6.1 External Calls and Unknown Code
Smart contracts often interact with external contracts (e.g., lending pools, yield aggregators) whose code may be unknown, unverified, or mutable (via upgradeable proxies).
*   **Verification Limit:** Formal verification typically assumes a "closed world"—it verifies the contract against a model of its environment. If the environment (external contracts) behaves unexpectedly (e.g., a reentrancy attack from a malicious token), the proof may not hold [cite: 25, 26].
*   **Harvest Finance & Curve:** Attacks often exploit the interaction *between* protocols. For instance, manipulating the price in Curve to exploit Harvest Finance. Verifying Harvest Finance in isolation would not detect this vulnerability because the flaw lies in the *economic assumption* of Curve's price stability, not a coding error in Harvest [cite: 25].

### 6.2 The "Blind" Smart Contract
Contracts are described as "blind" because they execute code deterministically without awareness of the broader market context [cite: 27].
*   **Oracle Manipulation:** A contract may be formally verified to "correctly calculate asset value based on Oracle X." However, if Oracle X is manipulated via a flash loan, the contract executes "correctly" according to its code but catastrophically according to its intent. This is a semantic blind spot that code verification cannot address; it requires **economic verification** or runtime monitoring [cite: 27, 28].

---

## 7. Economic Analysis: The Cost of Security

The decision to employ formal verification is ultimately an economic one. The high cost of FV creates a tiered security landscape.

### 7.1 Cost vs. Benefit
*   **High Costs:** A full formal verification audit is labor-intensive, requiring PhD-level expertise to write specifications. Costs can exceed $200,000 for complex protocols, and the process can take months [cite: 1].
*   **Diminishing Returns:** For many projects, the cost of FV exceeds the perceived risk or the project's entire budget. They opt for "good enough" security: a manual audit ($20k-$50k) and bug bounties [cite: 2, 12].
*   **The "Security Debt":** This economic pressure leads to "security debt." Projects launch with known blind spots (unverified components), hoping to upgrade security later. However, the immutability of smart contracts often makes post-deployment security upgrades difficult or impossible without migrating liquidity [cite: 11, 29].

### 7.2 The Role of Automated Tools
To bridge the gap, the industry is increasingly relying on automated tools:
*   **Static Analysis (Slither, MythX):** Cheap and fast, but only catches surface-level bugs (approx. 92% of *known* vulnerability patterns). They miss logic errors [cite: 1, 30].
*   **Fuzzing (Foundry, Echidna):** A middle ground. Fuzzing throws random data at the contract to find crashes. It is more effective than static analysis but lacks the completeness of FV. It is essentially "probabilistic verification" [cite: 31, 32].

---

## 8. Future Directions: Bridging the Gap

Research and industry trends point toward several solutions to the efficiency-completeness dilemma.

### 8.1 Modular and Continuous Verification
Instead of monolithic "big bang" verification, protocols are moving toward **continuous verification**.
*   **Certora & Aave:** Aave utilizes continuous formal verification where every code change is automatically checked against a set of rules. This prevents regression bugs and manages complexity by verifying changes incrementally [cite: 31, 32].
*   **Divide and Conquer:** Verifying small, isolated invariants (e.g., "token balance must equal total supply") is computationally tractable. The challenge is aggregating these local proofs into a global safety guarantee [cite: 13].

### 8.2 Runtime Enforcement
Recognizing that compile-time verification has blind spots, developers are exploring **runtime verification**.
*   **Defense Contracts:** Tools like "Traps" (Drosera Network) or "Circuit Breakers" monitor the protocol on-chain. If an invariant is violated (e.g., a massive price shift or liquidity drain), the contract automatically pauses. This moves verification from *pre-deployment proof* to *real-time enforcement*, mitigating the risk of unforeseen state transitions [cite: 23, 27].

### 8.3 Improved Tooling for Precision
Newer formal tools are being designed to handle the specific challenges of DeFi math.
*   **SMT Solvers for Bit-Vectors:** Improvements in SMT solvers (like Z3) are making bit-precise reasoning more efficient, helping to catch the rounding errors that caused the KyberSwap hack [cite: 15, 33].
*   **Hybrid Fuzzing/Symbolic Execution:** Combining fuzzing (to quickly reach deep states) with symbolic execution (to explore branches from those states) helps mitigate state space explosion [cite: 4, 34].

---

## 9. Conclusion

Smart contract verification in DeFi does not yet balance audit efficiency with formal proof completeness; rather, it operates under a regime of **constrained optimization** where blind spots are inevitable.

The **state space explosion** problem imposes a hard computational limit on the verification of complex logic, forcing the use of abstractions that can mask critical precision errors (as seen in KyberSwap). Simultaneously, the **specification bottleneck** introduces human error into the verification process, allowing logic gaps (as seen in Euler Finance) to persist despite rigorous checks.

While formal verification remains the gold standard for ensuring correctness, its high cost and technical limitations mean it is rarely applied exhaustively. The industry's trajectory suggests that "completeness" is an unattainable goal for monolithic DeFi systems. Instead, security is evolving into a layered approach: **Manual audits** for design logic, **Formal Verification** for critical invariants and math, **Fuzzing** for edge-case detection, and **Runtime Enforcement** as a final fail-safe against the unknown. Until computational power scales to meet the exponential complexity of composable DeFi, verification will remain a powerful but imperfect flashlight in a rapidly expanding dark forest.

---

### References
[cite: 27] Medium (2025). "In today's DEFI, smart contracts are powerful but blind..."
[cite: 30] ISACA Journal (2023). "Assessing the Shortfalls of DeFi Platforms."
[cite: 14] Hashlock (2025). "What is Formal Verification in Smart Contract Auditing."
[cite: 10] Hexn.io (2025). "Exploring the Need for Formal Verification in Smart Contracts."
[cite: 15] Halborn (2023). "A Guide to Formal Verification of Smart Contracts."
[cite: 35] Binance (2023). "How formal verification and manual audit work together."
[cite: 11] Medium (2024). "Beyond Tests and Assertions: Can Formal Verification Make DeFi Safer?"
[cite: 16] Hacken (2025). "Formal Verification."
[cite: 13] Zealynx (2025). "Divide and Conquer Auditing."
[cite: 3] VSB (2003). "State Space Methods."
[cite: 9] USENIX. "Handling State Space Explosion."
[cite: 25] Tolmach et al. (2021). "Formal Analysis of Composable DeFi Protocols."
[cite: 26] arXiv (2021). "Formal Analysis of Composable DeFi Protocols."
[cite: 36] Semantic Scholar. "Formal Analysis of Composable DeFi Protocols."
[cite: 29] Extropy.io (2025). "Using Formal Verification Techniques When Auditing."
[cite: 15] Halborn (2023). "Introduction to Formal Verification."
[cite: 31] Zealynx (2024). "The Power of Fuzzing and Formal Verification."
[cite: 11] Medium (2024). "The Case for Formal Verification."
[cite: 28] Antier Solutions (2023). "DeFi Security Hacks: Prominent Types & Prevention."
[cite: 4] HackMD (2023). "Challenges in Symbolic Execution."
[cite: 34] Medium (2025). "Symbolic Execution vs Traditional Static Analysis."
[cite: 33] Cyfrin (2024). "Solidity Smart Contract Formal Verification & Symbolic Execution."
[cite: 18] USENIX (2020). "ETHBMC: A Bounded Model Checker."
[cite: 13] Zealynx (2025). "Divide and Conquer Auditing."
[cite: 9] USENIX. "Handling State Space Explosion."
[cite: 21] arXiv (2025). "Concentrated-liquidity automated market makers (CLAMMs)..."
[cite: 22] RePEc (2025). "Formal State-Machine Models for Uniswap v3..."
[cite: 37] ResearchGate (2025). "Formal State-Machine Models for Uniswap v3..."
[cite: 5] Cyfrin (2024). "How did the Euler Finance hack happen?"
[cite: 38] CertiK (2023). "Euler Finance Incident Analysis."
[cite: 19] Hacken (2025). "Euler Finance Hack."
[cite: 1] Medium (2025). "The Smart Contract Audit That Cost More Than Building the Entire DApp."
[cite: 39] Zealynx (2025). "Smart Contract Audit Cost in 2025."
[cite: 2] Ulam.io (2025). "Smart Contract Audit."
[cite: 7] SolidityScan (2023). "KyberSwap Hack Analysis."
[cite: 20] Halborn (2023). "Explained: The KyberSwap Hack November 2023."
[cite: 20] Halborn (2023). "KyberSwap Hack: Precision Error."
[cite: 24] BlockSec (2023). "Yet Another Tragedy of Precision Loss."
[cite: 1] Medium (2025). "Cost of Smart Contract Audit vs Formal Verification."
[cite: 12] Mor Software (2026). "Smart Contract Audit Cost."
[cite: 32] Euler Finance. "Securing Euler."
[cite: 6] Omniscia (2023). "Euler Finance Incident Post-Mortem."
[cite: 5] Cyfrin (2024). "Euler Finance Hack Analysis."
[cite: 17] Medium (2023). "Formal Verification & Symbolic Execution: The Security Silver Bullet?"
[cite: 7] SolidityScan (2023). "KyberSwap Hack Analysis."
[cite: 8] BlockSec (2024). "KyberSwap Incident: Masterful Exploitation of Rounding Errors."
[cite: 23] a16z crypto (2025). "Runtime Enforcement: Defense Against Numerical Exploits."

**Sources:**
1. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHV5S_860xkBRV8oKOYk2A_kWxtRgCaHdevMiWem4kx95CPS6ThrNxmnjNbNGJa9GDxSXtabpAxx1zGkQxhaQ-imqgDi22iuDyo3SmcTGOTKAwjGJOVN-UqdlL-a_tBfXR_xiDqGAcL-1qhOlDgwRoFWRZZ5cEKFBX6wv2E7SiN1iGdD7l3dupSERXVi8MNS4Mln7FZAhdE7usslMnWWteFkXk7pe0ORNw=)
2. [ulam.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzViE1TURcIOrJDHyJsGruczRXgJB1F3jm4UTvXGxLiVohwD8E4GV9l9wMMS-cLiASkVegXZYAzE5Q6G5PQafOVKP-OF4MLPKhysBQcVhuGmnaob24L7okp2nTKrUsmM8K2A==)
3. [vsb.cz](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcaaE6buCAhomvDqFsnNiMZJktiT48lSkGNwCoLWt8TQWBSh2K7BfURgPZDN22-YSGjUJ3lGPW0vGM_Dn4cVafvQjWfnRbMIvEvLpWlFUwxj-GxLUwEN08lyMLB-h1DQ56xyldo4hDIthY58w=)
4. [hackmd.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpcjYLX4tdmhR1OuVu0jivkzEqDkUprFIqJDH-epF7SqtxiAcbZB427fLPAYh9ZdkBnEiiPDPNE88Wtmv-xHCEptz6YDVq8MlI-LzfQZnjOcmVTdBnvY0sdYgyXG2Wew==)
5. [cyfrin.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrdijIbMHVdG8FSK9Kcpwbn7CudxZRDgGsma0rUmsu9qUIlXRD8coMB8_CsXPT2i0v5wT0e5X_smAZqfpUdvNkBzQmgFMf8VE5lfIsyWK5Y6yYTDVfs_DskpjkBdFLqESKM9CaEYr_sr5Obg5EfyQvNugZ6ffG83RQ6E7XRb6NVDl6vA==)
6. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbnVlh8v02zPXTvC5lcgwmD4braYdHpYQiGSxSXJrx0eRccZEJm8vbuKhdXsLO3lsZlH7G6sV5WQMUiHq9U3rBSG9QVVZStxTF-0HvNp0blldQl6ebj_dB9OeXMYtsKHml_oSO4WgwO-sCnvHxxRR7I8nX9CqEVIeIzXdZ9ixCnw0TW2w=)
7. [solidityscan.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8SX192fJ6O59ZQi0DrBMmFLkush3pXPNeYU1Z7k2ooKv6wAcaDPidlahSg2JRT6lWd97jg-f931oNcAR5ayMV0l2v5QAh_eZWK-UFWaxdULSwWiTC4ZSs3yAeRIt7eEi_D2B3jZhm6xnGMVTNyGWlTr-6acP7xQ==)
8. [blocksec.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGG7blgxChWBydnsK43UDmWwzOjTdjV6DHNybd6HdsZg_SCeax8S-pZVQjKtDWUcCXfBh5kI6k_7kB72ZtHQYptTpYTYG0KfEJDHzm-RLyRgHscrkTStXarYTVSlxw8wMxzRqc9ycbfgQahnCt4dpygUynAGeR5YSSgirHdF0RUljvZo8andLY-uWWiqZyrlXQDo5pipkrWSS0-Z9wRCenFk_mpIUd9_4ra1W0uDyZI7A==)
9. [usenix.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-kae6fAOcButL8m8hkPJyoZz91hjLs0DvlHxzfeVLqYqvFHedK3FzlL3L5-bNMkugV1BASkzGcvNR7t__flyZ85hMvfqnj4VklJ8poZkmSlT15ND8MeOvO9NyRBDuzpWBIW63JTH5DpCAV1fmcKWihww0ag==)
10. [hexn.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvbBBRCtCjRjcfTpoX-VRm7n3HrmU-MNaFQgtUWTdHfXQCcMrzjqAuTMILdv8FnNOoAN368IaEQsXJYbJ3YOLdwR8F557yPaoHEfYpYYL57fcfKbvuuKlmULywEMKsf1QDdriP5DRVxZvdaZvbSsiqbOj0AF4JyGO2oBXQtQfWnMUtk6aMA3whh2AJPFWFrp4PWoVeixm0LG69Z0EcC8io)
11. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyUDvG-_Ht8wOu9ylj5oOQC-W6lfZgJ8rwJqsF8g3bdajFCIk3OUBnGqL2uTRcPd-V4mKWGjN7x056JQNjJ6bUVurjCWiL6YC70LzhqKJyE22OiEww9BuibVGTj_3JeHAvizQZDue1DQ1usagoqyex0WrdtjpmmhUas4Yj0GZXuWdx9Wbn8SDSkjxLgn4Qwe3dT9bpnuM_x83xzPtxKGp5FKS9ttIobSSx2bZb)
12. [morsoftware.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGYrgEW4fKOeLU7txUovJMi_4qOaF4jxZq6ZlWhFmEzKwRgrS4SlHXetYAbwsbXwlFGCQz_B6XVrqHAcmLGo87c6IwkDjJC-3qw4okYzNvCSMGA-msD4s7aG3cu19ntmDwrbzrRxJ9Vm4PAA==)
13. [zealynx.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9vbt5CcqlxAJ7w4usgoWIRG4YEwMGJHAKh3bQeBm3LWObzKbS__4utaKHjX2pFagexHUfqGjhp2Glf8XdWoycPukyA5oCh3c_4tY1R2kO_c0-7PXZkThA8ZjyQwB_Z1OONiTVBufDZFYqUfDj)
14. [hashlock.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEgnwL-ulEqA6DwMLIxS6NvHzt7LuiEQMi-yeaHk8IpDB3JXtovh5RIYuFz90r_JP9C1SHj3FBF7Mic6ZY9X20DMmZ4jQ-aYUoqikmGrfl-y14XI8dKJg7o151oJU8-Q9pDOyx94kFmzKSt2MeDE3EfL1al7v7PJ4rIdW7t_8kSye0XHFR)
15. [halborn.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFc4ZGtI8fZwWoim8q6MTHy79oObySwzgZk6OJ5yO1_F7RKQNGW0qcq5doBpihwahqzCPjTjuK91iPQqBjeanbhQykp3Lc9ihRXxIrfWz95_dYluRAUy-IQ2lUfW8mqvH5oC3cR3zachtrAQApqjx2U4AKnb0GOjq9m36m9rLUz6ydpRXmsLmlx)
16. [hacken.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFY1uRm27GTUUqcPTGw8Y-xxm0eRUKoEEjcFDZiau7q-dKzTPklZiM6k_2hb1OKx3PRyM8pbVK965UJsxEEU9iYyb4xd2wos4O-6HBvPvYtiVPuqpduqRpKLj1i-k2lOQvEOZtP)
17. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2tKflqSxU24Q23m3czID7KX5dhcJ2G9wzpCde-b8qNevgscdTtxdpYFyuRi17Gqc1XEicIpSDZt6L2P15o0jblpYnQ5wrGgk8-PMD3xy6ZG67KGN2dP0vSS2y47CcEnWuB24kZ0i7uS4CS_imIn2iSP_mt0i-FibWxQdidFRfnGt5yop_QkPmTbcK0z3bEYe7tKp4OXgfoYt1QQJVCtXlJNO0vA==)
18. [usenix.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfpSa5DHXOpd-fo5_lBJ7kd57kHd09xNNNWGh0Ri0awWC-qiGDPVvyHwLRx-lGqrp4P-ovQBBWjEJQypUJZaNtlESjjDu14aBFDPtmQkZPOAGeXfAS1z_kz4YZ55xalpFjQlvjcwyj9YtRf3n6F75QFrv5YIo=)
19. [hacken.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXwynuAS3bVmc7aGbZNEvwbAEVcPvJ-wb2j_cmm5R8bm35W7qa5nwOmP433ho4OCHiMPGJnpodLuIoMY76QYv-WmRhKVTqHh1E6GYhjWx2r1c1WU0vC5hh_dkVRvAEkwpjPQ8=)
20. [halborn.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0fsHhDqrk7DnLEFsZvX6xnOk0y4HoJQ-7UG6n-OXXfHEptMOJTMUpDPiFGNb4BCFPru2VOaXl1MjszEowsDRvOS51Goc3MV2GHgfaCizKNvBw-zmMNHDCUwaCCfULXpduPkzuxB3n8_7FYIGJj6dRjCR__PZozMGFDP-qT6H7KMo=)
21. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7thpsMNvBAEkeSQUS8Shm9whudurtT0tPU0XRngLeN65nMB9jpxir3j6pNUAsDcxVvsw6D2RANjCGn20yuhQp0CmKtZnsWCbUDG6XXWpD3IaP35otZyhc)
22. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxTF0lEYNLcIGznleB--eQZE3Yx4bo5lp3XA51_vy7ONG0usIIHDZv4OyNq40vookd00fwz4rzREnNAdfc8_me0sQ2_UQ59chbWCHdyQZWQuZqDj8vGA34TFcWOVtqFWyHi3Nsr2SUIuU=)
23. [a16zcrypto.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFW6GVGcwxH9mKxpOnn3nxjpJZJPrC8GaecIihAOphRfKj0lKQ86LtjXBOQqwjOnVR-DGC_CxnvTkpq7PjCA26BNQmJJwsipvZ9zjxV5niInlMuPObndDZVoK4FkRlJdwlEX756-avwhVuOKjuDDWIW68Bt2w7f9w3BK3aUksTxFM733_6mJJoKw==)
24. [blocksec.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiFqspybHJnbNZxV9nj_3CAZZe995dszv3nxrwQIqypucb13h4kTF7RX6kis3i7OIsZir3oboJFsuk-jCtAhmoxd4Z6YIQxuGiNZY8TTDYXem1VWwEaw4qOKh1AtT0jWmjOwUB0vvBi833kbPP8U7301i73bcghob2rKz4SKECN-zoopuILRqLK_uPVIh2P6B9nmIl_rTw62A3Emoq6ueeXXEo1qVF)
25. [ntu.edu.sg](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOzzUFRqMwSoZC86sHvfSWU3mUH3R2CNStpseSmK0tZZjy6iSEOVFpN1wOsHlpNTggo2AP6P1Jgi8ecFC7ntXuq773YtuT9vu04wKekxN6qLQjeeZ7JVClPCamY4SYUUAHp_eNBF4zlzNyTBtUWlk=)
26. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEeFX2Tz6z1wDFDG3iP1gbBLAzbB40mMSIGAmJpMDa0NBZyFxYCkIWGaAW3MwwIfs4SzQW-Q-1cX5lEcO7YIqEIqf4xNH4gPg_22bmgy1ajL2SjxqOo)
27. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjMnkb5sMgFAZy7igC1tk11lhmpHlpp7zfBOJVFqR9kbPMhcKfeHJigJO8KtizKO4vupEHWLmaiHjf9Hst6wl29r7l4mjmaLVdhBjhDfoSlTWsQN1XVpHzOF52xIhdWF90lcnGUdAOWv3lISzPa5gLoNqo8ehrEursoU0AjjC78SG9sEWKuFZie-QcjfEMwza-jhVE28VRD_XF8I0GjKT_uGNVwu9M-ALzDwInHYKodRAJkA2WtMcZrs0jT3UNLSIa973TubQ=)
28. [antiersolutions.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtrN4hLumxewo0LGmhVDJYT-3UotfmA2UfEWyljWkDI6m_MJ088OnPUjoAzR-vK6RjxOl8VJns3eo5wy_bquJGzR2XPUOoyhLmUHui6hifyqd3T9R7_eWXB4_LcI5H-1P7rRWfVbQvGxf4GEs5BIxT6DAjF30T1thKQkoXScHjocBnQj-mpe3nKRNs45XiqnTs5YCNqw==)
29. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHCiIC0QPuhlMM9djAtPRberf7Outn9jX2JNDesucSslKf1XjNlazdyRh6r7hriMhEpv4Zf80YbOu2mI21f-ZXPd6UbA0cXruYhdLLNH0GJE6oMliO9TKZLHREOdZs8Oq3tCZ1FfowGrFZo2NHVTIOtMBpYQJoi7gJ0CnzKV2C7r4a5FQGv-s0bdgX_InY-hsDWSw==)
30. [isaca.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG88-SbXrQCkvggmiMfAa_WkCDn-AmUDfUDg4A-FZUdSIK1QTqUpC5saloTCKTo2FfS0tEjUuwyhWdnToTeATK2sUcy0c9CNCaqte68oPreiYkyXm80f1xS0RcoC1lpo7Tq0Rn0NqVbecsqSMWrOOFp_bs7xL_G8rFWy6VNlsORjZRvfpUseD3fPXKKiVOi-m809iG2yNZG04pBGELhS-9A_t0=)
31. [zealynx.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHMjtDt7ApaTxgpezg-c1d0GVb49nR9HXI3fiWDc3Ir5owXcV9zodqZlvlk7L0IsKKi0Y1Q-P5O2wbz0IWjfoNf3lWiznEwjVLjrpctG5RIhvC3QiRBn_FG6KwneJofDyQk6sWREtrrL7dUGGXNSf8EnASCdXzPte0SQCMNlxfazHgfZQUYOcSuJ7ln6h_pVNcX4ZxSw==)
32. [euler.finance](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHki-xZ4G0zGmiJzsy1oJkJMFuroeFcnTE6y2tQ-VVHsdoMwwvRzP2Gs2y3XsJev9ycYPBGCutqTEZFVpaCWAdkJAS3haikRSpAsGBctA4EFlCLtuo4z9nNKMtKSvPd)
33. [cyfrin.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwxslGQU0sUXbDmrxO2j73MD-oOLPKMfERxe5f_Gv6y4S2nkizYjHc47qdqK5oPdse_ijhWX4_SHYrQgQdrWD5dpWwgtE-L6D7ZuEjcyzak4yhMTR5inaUboc8krNis7O6BUQ6QV4HprXOxJNjWSIj5KQVdTUKOwoFZw7s0jOGW7dgxtASrqx1zWHtRLEP)
34. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBw2mHOqPU7HQcCk_dC87xTvcxVTQdRYNuH5EEzx2rpShKSaC3x8jS10tqzShIN62K8NO8jJLnc6UdVQI5dHEDkZeJuhUtRLwr-65NqB6QoPNin7IwihN5u2HZ4Ep5SFG6Y-LwpkPFQKZQ_5lJD76CwdYrcnlZc2LObn4GCvq59oHK8p7UT6sNMKFnmef5OHJO_3iVi1VWylbs1-7m3aOs8ZIJaVZKkqbMg443)
35. [binance.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCvJDj2oEPLVmVDgMrs4Pq7sx_GSHJ3NycMH2RYs-Z6Z1qrinq5yxO2Ve-wvdGwFuwwM9v5_Iben9yatltf267RZOdtFzxsS_8de_g4AHCQb1nhniAYoKdSDa2lH1mGEKWGQ==)
36. [semanticscholar.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpYaYFvkzjLNEMh5YWOtny-sUNLEVpxM117WqRs_3QybenHjeJW58iTegKY3RuZtL8wRkxedncSD2S9kfcHf4CQVYy_4GhI2Z_MHv_-XarqU2J40zIgJyKYcJFbuqHBezgGsY-oTBqqM6W9sAnrNMQgEjq2UKJ4JVLBxZWmXarmZpVnt0TQo1XXmYJvo6ddVjDYniM446fbU5VSnEERUO5GlWAre6mmsXNwKJKdlrkFWjcclZO1DiktZU3SQ==)
37. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGG9-XzbNZUyUf8jxbqXQwRlQgF736WPeuhZkDyT3FKrhhJS1WRYWTtLQqy-YVyII6WVP99PpqMGHzpkH6FF8LgSUnAdbBFVFy6QwOUUetJQIp8TdR_WVJsE1QySXPwuC14lfMm8H3_poIp9WwuK2TYXAlPVmsshR_M1vJDQglkEiEeXUKUeLdiPtDfwouuIkJe-z2kLhTqNp4YFz6_No8qNMPsDS6xkqgMWsvRSj70htMyzXo05P4IumH4wKcmrXkS-tb8POVa2a3zLISFBdQ02mwUNA6n_X_IVYHybFVtMPtFnqPNKWl_0V5Hp_dhqsDNcelIy7M1I65nAQ==)
38. [certik.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzrIUcrOl6eF_KWxgKEEpBHU6s7oMRUBrvfZoGiZDTyxaN8WT5kFF_77TBguhNFQxksOrt-Tpx_ZcVQm5VS79RgdK0cjSKOootdF2xLiDd6H2a5lNbeuQVWXHNWAHjru-YkMVcxXF16wGlnjHKWDrq9X5GwYAEVygh8Q==)
39. [zealynx.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJgfpqqh1A3Ow-Vj6J2lczwcow74-ZySornY1J0wT7m-mtNQI4r7GozT_aZa5KROkum4E98yFm8wMerXr9-szHPOuPWPLY5OMKLdecWOzAlu7Ui33xEpqC5uNF5WC2ZcRTFWjGzOykcvkLVWxHvSxgCsQyEW-yjgzaqE-mBczVhS4engfbawzmyQ==)


## Annotations
Annotation(end_index=711, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzViE1TURcIOrJDHyJsGruczRXgJB1F3jm4UTvXGxLiVohwD8E4GV9l9wMMS-cLiASkVegXZYAzE5Q6G5PQafOVKP-OF4MLPKhysBQcVhuGmnaob24L7okp2nTKrUsmM8K2A==', start_index=699)
Annotation(end_index=711, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHV5S_860xkBRV8oKOYk2A_kWxtRgCaHdevMiWem4kx95CPS6ThrNxmnjNbNGJa9GDxSXtabpAxx1zGkQxhaQ-imqgDi22iuDyo3SmcTGOTKAwjGJOVN-UqdlL-a_tBfXR_xiDqGAcL-1qhOlDgwRoFWRZZ5cEKFBX6wv2E7SiN1iGdD7l3dupSERXVi8MNS4Mln7FZAhdE7usslMnWWteFkXk7pe0ORNw=', start_index=699)
Annotation(end_index=1190, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcaaE6buCAhomvDqFsnNiMZJktiT48lSkGNwCoLWt8TQWBSh2K7BfURgPZDN22-YSGjUJ3lGPW0vGM_Dn4cVafvQjWfnRbMIvEvLpWlFUwxj-GxLUwEN08lyMLB-h1DQ56xyldo4hDIthY58w=', start_index=1178)
Annotation(end_index=1190, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpcjYLX4tdmhR1OuVu0jivkzEqDkUprFIqJDH-epF7SqtxiAcbZB427fLPAYh9ZdkBnEiiPDPNE88Wtmv-xHCEptz6YDVq8MlI-LzfQZnjOcmVTdBnvY0sdYgyXG2Wew==', start_index=1178)
Annotation(end_index=1630, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbnVlh8v02zPXTvC5lcgwmD4braYdHpYQiGSxSXJrx0eRccZEJm8vbuKhdXsLO3lsZlH7G6sV5WQMUiHq9U3rBSG9QVVZStxTF-0HvNp0blldQl6ebj_dB9OeXMYtsKHml_oSO4WgwO-sCnvHxxRR7I8nX9CqEVIeIzXdZ9ixCnw0TW2w=', start_index=1618)
Annotation(end_index=1630, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrdijIbMHVdG8FSK9Kcpwbn7CudxZRDgGsma0rUmsu9qUIlXRD8coMB8_CsXPT2i0v5wT0e5X_smAZqfpUdvNkBzQmgFMf8VE5lfIsyWK5Y6yYTDVfs_DskpjkBdFLqESKM9CaEYr_sr5Obg5EfyQvNugZ6ffG83RQ6E7XRb6NVDl6vA==', start_index=1618)
Annotation(end_index=2069, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGG7blgxChWBydnsK43UDmWwzOjTdjV6DHNybd6HdsZg_SCeax8S-pZVQjKtDWUcCXfBh5kI6k_7kB72ZtHQYptTpYTYG0KfEJDHzm-RLyRgHscrkTStXarYTVSlxw8wMxzRqc9ycbfgQahnCt4dpygUynAGeR5YSSgirHdF0RUljvZo8andLY-uWWiqZyrlXQDo5pipkrWSS0-Z9wRCenFk_mpIUd9_4ra1W0uDyZI7A==', start_index=2057)
Annotation(end_index=2069, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8SX192fJ6O59ZQi0DrBMmFLkush3pXPNeYU1Z7k2ooKv6wAcaDPidlahSg2JRT6lWd97jg-f931oNcAR5ayMV0l2v5QAh_eZWK-UFWaxdULSwWiTC4ZSs3yAeRIt7eEi_D2B3jZhm6xnGMVTNyGWlTr-6acP7xQ==', start_index=2057)
Annotation(end_index=2663, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8SX192fJ6O59ZQi0DrBMmFLkush3pXPNeYU1Z7k2ooKv6wAcaDPidlahSg2JRT6lWd97jg-f931oNcAR5ayMV0l2v5QAh_eZWK-UFWaxdULSwWiTC4ZSs3yAeRIt7eEi_D2B3jZhm6xnGMVTNyGWlTr-6acP7xQ==', start_index=2651)
Annotation(end_index=2663, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHV5S_860xkBRV8oKOYk2A_kWxtRgCaHdevMiWem4kx95CPS6ThrNxmnjNbNGJa9GDxSXtabpAxx1zGkQxhaQ-imqgDi22iuDyo3SmcTGOTKAwjGJOVN-UqdlL-a_tBfXR_xiDqGAcL-1qhOlDgwRoFWRZZ5cEKFBX6wv2E7SiN1iGdD7l3dupSERXVi8MNS4Mln7FZAhdE7usslMnWWteFkXk7pe0ORNw=', start_index=2651)
Annotation(end_index=3349, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-kae6fAOcButL8m8hkPJyoZz91hjLs0DvlHxzfeVLqYqvFHedK3FzlL3L5-bNMkugV1BASkzGcvNR7t__flyZ85hMvfqnj4VklJ8poZkmSlT15ND8MeOvO9NyRBDuzpWBIW63JTH5DpCAV1fmcKWihww0ag==', start_index=3337)
Annotation(end_index=3349, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcaaE6buCAhomvDqFsnNiMZJktiT48lSkGNwCoLWt8TQWBSh2K7BfURgPZDN22-YSGjUJ3lGPW0vGM_Dn4cVafvQjWfnRbMIvEvLpWlFUwxj-GxLUwEN08lyMLB-h1DQ56xyldo4hDIthY58w=', start_index=3337)
Annotation(end_index=3687, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbnVlh8v02zPXTvC5lcgwmD4braYdHpYQiGSxSXJrx0eRccZEJm8vbuKhdXsLO3lsZlH7G6sV5WQMUiHq9U3rBSG9QVVZStxTF-0HvNp0blldQl6ebj_dB9OeXMYtsKHml_oSO4WgwO-sCnvHxxRR7I8nX9CqEVIeIzXdZ9ixCnw0TW2w=', start_index=3678)
Annotation(end_index=3975, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvbBBRCtCjRjcfTpoX-VRm7n3HrmU-MNaFQgtUWTdHfXQCcMrzjqAuTMILdv8FnNOoAN368IaEQsXJYbJ3YOLdwR8F557yPaoHEfYpYYL57fcfKbvuuKlmULywEMKsf1QDdriP5DRVxZvdaZvbSsiqbOj0AF4JyGO2oBXQtQfWnMUtk6aMA3whh2AJPFWFrp4PWoVeixm0LG69Z0EcC8io', start_index=3961)
Annotation(end_index=3975, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyUDvG-_Ht8wOu9ylj5oOQC-W6lfZgJ8rwJqsF8g3bdajFCIk3OUBnGqL2uTRcPd-V4mKWGjN7x056JQNjJ6bUVurjCWiL6YC70LzhqKJyE22OiEww9BuibVGTj_3JeHAvizQZDue1DQ1usagoqyex0WrdtjpmmhUas4Yj0GZXuWdx9Wbn8SDSkjxLgn4Qwe3dT9bpnuM_x83xzPtxKGp5FKS9ttIobSSx2bZb', start_index=3961)
Annotation(end_index=4761, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzViE1TURcIOrJDHyJsGruczRXgJB1F3jm4UTvXGxLiVohwD8E4GV9l9wMMS-cLiASkVegXZYAzE5Q6G5PQafOVKP-OF4MLPKhysBQcVhuGmnaob24L7okp2nTKrUsmM8K2A==', start_index=4748)
Annotation(end_index=4761, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGYrgEW4fKOeLU7txUovJMi_4qOaF4jxZq6ZlWhFmEzKwRgrS4SlHXetYAbwsbXwlFGCQz_B6XVrqHAcmLGo87c6IwkDjJC-3qw4okYzNvCSMGA-msD4s7aG3cu19ntmDwrbzrRxJ9Vm4PAA==', start_index=4748)
Annotation(end_index=5167, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9vbt5CcqlxAJ7w4usgoWIRG4YEwMGJHAKh3bQeBm3LWObzKbS__4utaKHjX2pFagexHUfqGjhp2Glf8XdWoycPukyA5oCh3c_4tY1R2kO_c0-7PXZkThA8ZjyQwB_Z1OONiTVBufDZFYqUfDj', start_index=5157)
Annotation(end_index=5371, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvbBBRCtCjRjcfTpoX-VRm7n3HrmU-MNaFQgtUWTdHfXQCcMrzjqAuTMILdv8FnNOoAN368IaEQsXJYbJ3YOLdwR8F557yPaoHEfYpYYL57fcfKbvuuKlmULywEMKsf1QDdriP5DRVxZvdaZvbSsiqbOj0AF4JyGO2oBXQtQfWnMUtk6aMA3whh2AJPFWFrp4PWoVeixm0LG69Z0EcC8io', start_index=5357)
Annotation(end_index=5371, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEgnwL-ulEqA6DwMLIxS6NvHzt7LuiEQMi-yeaHk8IpDB3JXtovh5RIYuFz90r_JP9C1SHj3FBF7Mic6ZY9X20DMmZ4jQ-aYUoqikmGrfl-y14XI8dKJg7o151oJU8-Q9pDOyx94kFmzKSt2MeDE3EfL1al7v7PJ4rIdW7t_8kSye0XHFR', start_index=5357)
Annotation(end_index=5841, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFc4ZGtI8fZwWoim8q6MTHy79oObySwzgZk6OJ5yO1_F7RKQNGW0qcq5doBpihwahqzCPjTjuK91iPQqBjeanbhQykp3Lc9ihRXxIrfWz95_dYluRAUy-IQ2lUfW8mqvH5oC3cR3zachtrAQApqjx2U4AKnb0GOjq9m36m9rLUz6ydpRXmsLmlx', start_index=5831)
Annotation(end_index=6177, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFY1uRm27GTUUqcPTGw8Y-xxm0eRUKoEEjcFDZiau7q-dKzTPklZiM6k_2hb1OKx3PRyM8pbVK965UJsxEEU9iYyb4xd2wos4O-6HBvPvYtiVPuqpduqRpKLj1i-k2lOQvEOZtP', start_index=6163)
Annotation(end_index=6177, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyUDvG-_Ht8wOu9ylj5oOQC-W6lfZgJ8rwJqsF8g3bdajFCIk3OUBnGqL2uTRcPd-V4mKWGjN7x056JQNjJ6bUVurjCWiL6YC70LzhqKJyE22OiEww9BuibVGTj_3JeHAvizQZDue1DQ1usagoqyex0WrdtjpmmhUas4Yj0GZXuWdx9Wbn8SDSkjxLgn4Qwe3dT9bpnuM_x83xzPtxKGp5FKS9ttIobSSx2bZb', start_index=6163)
Annotation(end_index=6404, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHV5S_860xkBRV8oKOYk2A_kWxtRgCaHdevMiWem4kx95CPS6ThrNxmnjNbNGJa9GDxSXtabpAxx1zGkQxhaQ-imqgDi22iuDyo3SmcTGOTKAwjGJOVN-UqdlL-a_tBfXR_xiDqGAcL-1qhOlDgwRoFWRZZ5cEKFBX6wv2E7SiN1iGdD7l3dupSERXVi8MNS4Mln7FZAhdE7usslMnWWteFkXk7pe0ORNw=', start_index=6395)
Annotation(end_index=6771, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFc4ZGtI8fZwWoim8q6MTHy79oObySwzgZk6OJ5yO1_F7RKQNGW0qcq5doBpihwahqzCPjTjuK91iPQqBjeanbhQykp3Lc9ihRXxIrfWz95_dYluRAUy-IQ2lUfW8mqvH5oC3cR3zachtrAQApqjx2U4AKnb0GOjq9m36m9rLUz6ydpRXmsLmlx', start_index=6757)
Annotation(end_index=6771, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEgnwL-ulEqA6DwMLIxS6NvHzt7LuiEQMi-yeaHk8IpDB3JXtovh5RIYuFz90r_JP9C1SHj3FBF7Mic6ZY9X20DMmZ4jQ-aYUoqikmGrfl-y14XI8dKJg7o151oJU8-Q9pDOyx94kFmzKSt2MeDE3EfL1al7v7PJ4rIdW7t_8kSye0XHFR', start_index=6757)
Annotation(end_index=7360, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcaaE6buCAhomvDqFsnNiMZJktiT48lSkGNwCoLWt8TQWBSh2K7BfURgPZDN22-YSGjUJ3lGPW0vGM_Dn4cVafvQjWfnRbMIvEvLpWlFUwxj-GxLUwEN08lyMLB-h1DQ56xyldo4hDIthY58w=', start_index=7351)
Annotation(end_index=7861, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcaaE6buCAhomvDqFsnNiMZJktiT48lSkGNwCoLWt8TQWBSh2K7BfURgPZDN22-YSGjUJ3lGPW0vGM_Dn4cVafvQjWfnRbMIvEvLpWlFUwxj-GxLUwEN08lyMLB-h1DQ56xyldo4hDIthY58w=', start_index=7852)
Annotation(end_index=8235, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2tKflqSxU24Q23m3czID7KX5dhcJ2G9wzpCde-b8qNevgscdTtxdpYFyuRi17Gqc1XEicIpSDZt6L2P15o0jblpYnQ5wrGgk8-PMD3xy6ZG67KGN2dP0vSS2y47CcEnWuB24kZ0i7uS4CS_imIn2iSP_mt0i-FibWxQdidFRfnGt5yop_QkPmTbcK0z3bEYe7tKp4OXgfoYt1QQJVCtXlJNO0vA==', start_index=8222)
Annotation(end_index=8235, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpcjYLX4tdmhR1OuVu0jivkzEqDkUprFIqJDH-epF7SqtxiAcbZB427fLPAYh9ZdkBnEiiPDPNE88Wtmv-xHCEptz6YDVq8MlI-LzfQZnjOcmVTdBnvY0sdYgyXG2Wew==', start_index=8222)
Annotation(end_index=8607, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfpSa5DHXOpd-fo5_lBJ7kd57kHd09xNNNWGh0Ri0awWC-qiGDPVvyHwLRx-lGqrp4P-ovQBBWjEJQypUJZaNtlESjjDu14aBFDPtmQkZPOAGeXfAS1z_kz4YZ55xalpFjQlvjcwyj9YtRf3n6F75QFrv5YIo=', start_index=8597)
Annotation(end_index=8913, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-kae6fAOcButL8m8hkPJyoZz91hjLs0DvlHxzfeVLqYqvFHedK3FzlL3L5-bNMkugV1BASkzGcvNR7t__flyZ85hMvfqnj4VklJ8poZkmSlT15ND8MeOvO9NyRBDuzpWBIW63JTH5DpCAV1fmcKWihww0ag==', start_index=8904)
Annotation(end_index=9184, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2tKflqSxU24Q23m3czID7KX5dhcJ2G9wzpCde-b8qNevgscdTtxdpYFyuRi17Gqc1XEicIpSDZt6L2P15o0jblpYnQ5wrGgk8-PMD3xy6ZG67KGN2dP0vSS2y47CcEnWuB24kZ0i7uS4CS_imIn2iSP_mt0i-FibWxQdidFRfnGt5yop_QkPmTbcK0z3bEYe7tKp4OXgfoYt1QQJVCtXlJNO0vA==', start_index=9171)
Annotation(end_index=9184, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8SX192fJ6O59ZQi0DrBMmFLkush3pXPNeYU1Z7k2ooKv6wAcaDPidlahSg2JRT6lWd97jg-f931oNcAR5ayMV0l2v5QAh_eZWK-UFWaxdULSwWiTC4ZSs3yAeRIt7eEi_D2B3jZhm6xnGMVTNyGWlTr-6acP7xQ==', start_index=9171)
Annotation(end_index=10409, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrdijIbMHVdG8FSK9Kcpwbn7CudxZRDgGsma0rUmsu9qUIlXRD8coMB8_CsXPT2i0v5wT0e5X_smAZqfpUdvNkBzQmgFMf8VE5lfIsyWK5Y6yYTDVfs_DskpjkBdFLqESKM9CaEYr_sr5Obg5EfyQvNugZ6ffG83RQ6E7XRb6NVDl6vA==', start_index=10396)
Annotation(end_index=10409, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXwynuAS3bVmc7aGbZNEvwbAEVcPvJ-wb2j_cmm5R8bm35W7qa5nwOmP433ho4OCHiMPGJnpodLuIoMY76QYv-WmRhKVTqHh1E6GYhjWx2r1c1WU0vC5hh_dkVRvAEkwpjPQ8=', start_index=10396)
Annotation(end_index=10821, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbnVlh8v02zPXTvC5lcgwmD4braYdHpYQiGSxSXJrx0eRccZEJm8vbuKhdXsLO3lsZlH7G6sV5WQMUiHq9U3rBSG9QVVZStxTF-0HvNp0blldQl6ebj_dB9OeXMYtsKHml_oSO4WgwO-sCnvHxxRR7I8nX9CqEVIeIzXdZ9ixCnw0TW2w=', start_index=10809)
Annotation(end_index=10821, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrdijIbMHVdG8FSK9Kcpwbn7CudxZRDgGsma0rUmsu9qUIlXRD8coMB8_CsXPT2i0v5wT0e5X_smAZqfpUdvNkBzQmgFMf8VE5lfIsyWK5Y6yYTDVfs_DskpjkBdFLqESKM9CaEYr_sr5Obg5EfyQvNugZ6ffG83RQ6E7XRb6NVDl6vA==', start_index=10809)
Annotation(end_index=11278, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrdijIbMHVdG8FSK9Kcpwbn7CudxZRDgGsma0rUmsu9qUIlXRD8coMB8_CsXPT2i0v5wT0e5X_smAZqfpUdvNkBzQmgFMf8VE5lfIsyWK5Y6yYTDVfs_DskpjkBdFLqESKM9CaEYr_sr5Obg5EfyQvNugZ6ffG83RQ6E7XRb6NVDl6vA==', start_index=11269)
Annotation(end_index=11468, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9vbt5CcqlxAJ7w4usgoWIRG4YEwMGJHAKh3bQeBm3LWObzKbS__4utaKHjX2pFagexHUfqGjhp2Glf8XdWoycPukyA5oCh3c_4tY1R2kO_c0-7PXZkThA8ZjyQwB_Z1OONiTVBufDZFYqUfDj', start_index=11458)
Annotation(end_index=11995, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbnVlh8v02zPXTvC5lcgwmD4braYdHpYQiGSxSXJrx0eRccZEJm8vbuKhdXsLO3lsZlH7G6sV5WQMUiHq9U3rBSG9QVVZStxTF-0HvNp0blldQl6ebj_dB9OeXMYtsKHml_oSO4WgwO-sCnvHxxRR7I8nX9CqEVIeIzXdZ9ixCnw0TW2w=', start_index=11986)
Annotation(end_index=12958, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0fsHhDqrk7DnLEFsZvX6xnOk0y4HoJQ-7UG6n-OXXfHEptMOJTMUpDPiFGNb4BCFPru2VOaXl1MjszEowsDRvOS51Goc3MV2GHgfaCizKNvBw-zmMNHDCUwaCCfULXpduPkzuxB3n8_7FYIGJj6dRjCR__PZozMGFDP-qT6H7KMo=', start_index=12945)
Annotation(end_index=12958, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8SX192fJ6O59ZQi0DrBMmFLkush3pXPNeYU1Z7k2ooKv6wAcaDPidlahSg2JRT6lWd97jg-f931oNcAR5ayMV0l2v5QAh_eZWK-UFWaxdULSwWiTC4ZSs3yAeRIt7eEi_D2B3jZhm6xnGMVTNyGWlTr-6acP7xQ==', start_index=12945)
Annotation(end_index=13330, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7thpsMNvBAEkeSQUS8Shm9whudurtT0tPU0XRngLeN65nMB9jpxir3j6pNUAsDcxVvsw6D2RANjCGn20yuhQp0CmKtZnsWCbUDG6XXWpD3IaP35otZyhc', start_index=13316)
Annotation(end_index=13330, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxTF0lEYNLcIGznleB--eQZE3Yx4bo5lp3XA51_vy7ONG0usIIHDZv4OyNq40vookd00fwz4rzREnNAdfc8_me0sQ2_UQ59chbWCHdyQZWQuZqDj8vGA34TFcWOVtqFWyHi3Nsr2SUIuU=', start_index=13316)
Annotation(end_index=13633, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFW6GVGcwxH9mKxpOnn3nxjpJZJPrC8GaecIihAOphRfKj0lKQ86LtjXBOQqwjOnVR-DGC_CxnvTkpq7PjCA26BNQmJJwsipvZ9zjxV5niInlMuPObndDZVoK4FkRlJdwlEX756-avwhVuOKjuDDWIW68Bt2w7f9w3BK3aUksTxFM733_6mJJoKw==', start_index=13619)
Annotation(end_index=13633, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxTF0lEYNLcIGznleB--eQZE3Yx4bo5lp3XA51_vy7ONG0usIIHDZv4OyNq40vookd00fwz4rzREnNAdfc8_me0sQ2_UQ59chbWCHdyQZWQuZqDj8vGA34TFcWOVtqFWyHi3Nsr2SUIuU=', start_index=13619)
Annotation(end_index=13939, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGG7blgxChWBydnsK43UDmWwzOjTdjV6DHNybd6HdsZg_SCeax8S-pZVQjKtDWUcCXfBh5kI6k_7kB72ZtHQYptTpYTYG0KfEJDHzm-RLyRgHscrkTStXarYTVSlxw8wMxzRqc9ycbfgQahnCt4dpygUynAGeR5YSSgirHdF0RUljvZo8andLY-uWWiqZyrlXQDo5pipkrWSS0-Z9wRCenFk_mpIUd9_4ra1W0uDyZI7A==', start_index=13930)
Annotation(end_index=14364, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiFqspybHJnbNZxV9nj_3CAZZe995dszv3nxrwQIqypucb13h4kTF7RX6kis3i7OIsZir3oboJFsuk-jCtAhmoxd4Z6YIQxuGiNZY8TTDYXem1VWwEaw4qOKh1AtT0jWmjOwUB0vvBi833kbPP8U7301i73bcghob2rKz4SKECN-zoopuILRqLK_uPVIh2P6B9nmIl_rTw62A3Emoq6ueeXXEo1qVF', start_index=14351)
Annotation(end_index=14364, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGG7blgxChWBydnsK43UDmWwzOjTdjV6DHNybd6HdsZg_SCeax8S-pZVQjKtDWUcCXfBh5kI6k_7kB72ZtHQYptTpYTYG0KfEJDHzm-RLyRgHscrkTStXarYTVSlxw8wMxzRqc9ycbfgQahnCt4dpygUynAGeR5YSSgirHdF0RUljvZo8andLY-uWWiqZyrlXQDo5pipkrWSS0-Z9wRCenFk_mpIUd9_4ra1W0uDyZI7A==', start_index=14351)
Annotation(end_index=15102, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEeFX2Tz6z1wDFDG3iP1gbBLAzbB40mMSIGAmJpMDa0NBZyFxYCkIWGaAW3MwwIfs4SzQW-Q-1cX5lEcO7YIqEIqf4xNH4gPg_22bmgy1ajL2SjxqOo', start_index=15088)
Annotation(end_index=15102, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOzzUFRqMwSoZC86sHvfSWU3mUH3R2CNStpseSmK0tZZjy6iSEOVFpN1wOsHlpNTggo2AP6P1Jgi8ecFC7ntXuq773YtuT9vu04wKekxN6qLQjeeZ7JVClPCamY4SYUUAHp_eNBF4zlzNyTBtUWlk=', start_index=15088)
Annotation(end_index=15464, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOzzUFRqMwSoZC86sHvfSWU3mUH3R2CNStpseSmK0tZZjy6iSEOVFpN1wOsHlpNTggo2AP6P1Jgi8ecFC7ntXuq773YtuT9vu04wKekxN6qLQjeeZ7JVClPCamY4SYUUAHp_eNBF4zlzNyTBtUWlk=', start_index=15454)
Annotation(end_index=15639, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjMnkb5sMgFAZy7igC1tk11lhmpHlpp7zfBOJVFqR9kbPMhcKfeHJigJO8KtizKO4vupEHWLmaiHjf9Hst6wl29r7l4mjmaLVdhBjhDfoSlTWsQN1XVpHzOF52xIhdWF90lcnGUdAOWv3lISzPa5gLoNqo8ehrEursoU0AjjC78SG9sEWKuFZie-QcjfEMwza-jhVE28VRD_XF8I0GjKT_uGNVwu9M-ALzDwInHYKodRAJkA2WtMcZrs0jT3UNLSIa973TubQ=', start_index=15629)
Annotation(end_index=16061, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjMnkb5sMgFAZy7igC1tk11lhmpHlpp7zfBOJVFqR9kbPMhcKfeHJigJO8KtizKO4vupEHWLmaiHjf9Hst6wl29r7l4mjmaLVdhBjhDfoSlTWsQN1XVpHzOF52xIhdWF90lcnGUdAOWv3lISzPa5gLoNqo8ehrEursoU0AjjC78SG9sEWKuFZie-QcjfEMwza-jhVE28VRD_XF8I0GjKT_uGNVwu9M-ALzDwInHYKodRAJkA2WtMcZrs0jT3UNLSIa973TubQ=', start_index=16047)
Annotation(end_index=16061, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtrN4hLumxewo0LGmhVDJYT-3UotfmA2UfEWyljWkDI6m_MJ088OnPUjoAzR-vK6RjxOl8VJns3eo5wy_bquJGzR2XPUOoyhLmUHui6hifyqd3T9R7_eWXB4_LcI5H-1P7rRWfVbQvGxf4GEs5BIxT6DAjF30T1thKQkoXScHjocBnQj-mpe3nKRNs45XiqnTs5YCNqw==', start_index=16047)
Annotation(end_index=16491, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHV5S_860xkBRV8oKOYk2A_kWxtRgCaHdevMiWem4kx95CPS6ThrNxmnjNbNGJa9GDxSXtabpAxx1zGkQxhaQ-imqgDi22iuDyo3SmcTGOTKAwjGJOVN-UqdlL-a_tBfXR_xiDqGAcL-1qhOlDgwRoFWRZZ5cEKFBX6wv2E7SiN1iGdD7l3dupSERXVi8MNS4Mln7FZAhdE7usslMnWWteFkXk7pe0ORNw=', start_index=16482)
Annotation(end_index=16709, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzViE1TURcIOrJDHyJsGruczRXgJB1F3jm4UTvXGxLiVohwD8E4GV9l9wMMS-cLiASkVegXZYAzE5Q6G5PQafOVKP-OF4MLPKhysBQcVhuGmnaob24L7okp2nTKrUsmM8K2A==', start_index=16696)
Annotation(end_index=16709, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGYrgEW4fKOeLU7txUovJMi_4qOaF4jxZq6ZlWhFmEzKwRgrS4SlHXetYAbwsbXwlFGCQz_B6XVrqHAcmLGo87c6IwkDjJC-3qw4okYzNvCSMGA-msD4s7aG3cu19ntmDwrbzrRxJ9Vm4PAA==', start_index=16696)
Annotation(end_index=17044, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyUDvG-_Ht8wOu9ylj5oOQC-W6lfZgJ8rwJqsF8g3bdajFCIk3OUBnGqL2uTRcPd-V4mKWGjN7x056JQNjJ6bUVurjCWiL6YC70LzhqKJyE22OiEww9BuibVGTj_3JeHAvizQZDue1DQ1usagoqyex0WrdtjpmmhUas4Yj0GZXuWdx9Wbn8SDSkjxLgn4Qwe3dT9bpnuM_x83xzPtxKGp5FKS9ttIobSSx2bZb', start_index=17030)
Annotation(end_index=17044, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHCiIC0QPuhlMM9djAtPRberf7Outn9jX2JNDesucSslKf1XjNlazdyRh6r7hriMhEpv4Zf80YbOu2mI21f-ZXPd6UbA0cXruYhdLLNH0GJE6oMliO9TKZLHREOdZs8Oq3tCZ1FfowGrFZo2NHVTIOtMBpYQJoi7gJ0CnzKV2C7r4a5FQGv-s0bdgX_InY-hsDWSw==', start_index=17030)
Annotation(end_index=17338, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG88-SbXrQCkvggmiMfAa_WkCDn-AmUDfUDg4A-FZUdSIK1QTqUpC5saloTCKTo2FfS0tEjUuwyhWdnToTeATK2sUcy0c9CNCaqte68oPreiYkyXm80f1xS0RcoC1lpo7Tq0Rn0NqVbecsqSMWrOOFp_bs7xL_G8rFWy6VNlsORjZRvfpUseD3fPXKKiVOi-m809iG2yNZG04pBGELhS-9A_t0=', start_index=17325)
Annotation(end_index=17338, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHV5S_860xkBRV8oKOYk2A_kWxtRgCaHdevMiWem4kx95CPS6ThrNxmnjNbNGJa9GDxSXtabpAxx1zGkQxhaQ-imqgDi22iuDyo3SmcTGOTKAwjGJOVN-UqdlL-a_tBfXR_xiDqGAcL-1qhOlDgwRoFWRZZ5cEKFBX6wv2E7SiN1iGdD7l3dupSERXVi8MNS4Mln7FZAhdE7usslMnWWteFkXk7pe0ORNw=', start_index=17325)
Annotation(end_index=17590, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHMjtDt7ApaTxgpezg-c1d0GVb49nR9HXI3fiWDc3Ir5owXcV9zodqZlvlk7L0IsKKi0Y1Q-P5O2wbz0IWjfoNf3lWiznEwjVLjrpctG5RIhvC3QiRBn_FG6KwneJofDyQk6sWREtrrL7dUGGXNSf8EnASCdXzPte0SQCMNlxfazHgfZQUYOcSuJ7ln6h_pVNcX4ZxSw==', start_index=17576)
Annotation(end_index=17590, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHki-xZ4G0zGmiJzsy1oJkJMFuroeFcnTE6y2tQ-VVHsdoMwwvRzP2Gs2y3XsJev9ycYPBGCutqTEZFVpaCWAdkJAS3haikRSpAsGBctA4EFlCLtuo4z9nNKMtKSvPd', start_index=17576)
Annotation(end_index=18134, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHMjtDt7ApaTxgpezg-c1d0GVb49nR9HXI3fiWDc3Ir5owXcV9zodqZlvlk7L0IsKKi0Y1Q-P5O2wbz0IWjfoNf3lWiznEwjVLjrpctG5RIhvC3QiRBn_FG6KwneJofDyQk6sWREtrrL7dUGGXNSf8EnASCdXzPte0SQCMNlxfazHgfZQUYOcSuJ7ln6h_pVNcX4ZxSw==', start_index=18120)
Annotation(end_index=18134, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHki-xZ4G0zGmiJzsy1oJkJMFuroeFcnTE6y2tQ-VVHsdoMwwvRzP2Gs2y3XsJev9ycYPBGCutqTEZFVpaCWAdkJAS3haikRSpAsGBctA4EFlCLtuo4z9nNKMtKSvPd', start_index=18120)
Annotation(end_index=18368, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9vbt5CcqlxAJ7w4usgoWIRG4YEwMGJHAKh3bQeBm3LWObzKbS__4utaKHjX2pFagexHUfqGjhp2Glf8XdWoycPukyA5oCh3c_4tY1R2kO_c0-7PXZkThA8ZjyQwB_Z1OONiTVBufDZFYqUfDj', start_index=18358)
Annotation(end_index=18886, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFW6GVGcwxH9mKxpOnn3nxjpJZJPrC8GaecIihAOphRfKj0lKQ86LtjXBOQqwjOnVR-DGC_CxnvTkpq7PjCA26BNQmJJwsipvZ9zjxV5niInlMuPObndDZVoK4FkRlJdwlEX756-avwhVuOKjuDDWIW68Bt2w7f9w3BK3aUksTxFM733_6mJJoKw==', start_index=18872)
Annotation(end_index=18886, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjMnkb5sMgFAZy7igC1tk11lhmpHlpp7zfBOJVFqR9kbPMhcKfeHJigJO8KtizKO4vupEHWLmaiHjf9Hst6wl29r7l4mjmaLVdhBjhDfoSlTWsQN1XVpHzOF52xIhdWF90lcnGUdAOWv3lISzPa5gLoNqo8ehrEursoU0AjjC78SG9sEWKuFZie-QcjfEMwza-jhVE28VRD_XF8I0GjKT_uGNVwu9M-ALzDwInHYKodRAJkA2WtMcZrs0jT3UNLSIa973TubQ=', start_index=18872)
Annotation(end_index=19220, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwxslGQU0sUXbDmrxO2j73MD-oOLPKMfERxe5f_Gv6y4S2nkizYjHc47qdqK5oPdse_ijhWX4_SHYrQgQdrWD5dpWwgtE-L6D7ZuEjcyzak4yhMTR5inaUboc8krNis7O6BUQ6QV4HprXOxJNjWSIj5KQVdTUKOwoFZw7s0jOGW7dgxtASrqx1zWHtRLEP', start_index=19206)
Annotation(end_index=19220, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFc4ZGtI8fZwWoim8q6MTHy79oObySwzgZk6OJ5yO1_F7RKQNGW0qcq5doBpihwahqzCPjTjuK91iPQqBjeanbhQykp3Lc9ihRXxIrfWz95_dYluRAUy-IQ2lUfW8mqvH5oC3cR3zachtrAQApqjx2U4AKnb0GOjq9m36m9rLUz6ydpRXmsLmlx', start_index=19206)
Annotation(end_index=19428, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBw2mHOqPU7HQcCk_dC87xTvcxVTQdRYNuH5EEzx2rpShKSaC3x8jS10tqzShIN62K8NO8jJLnc6UdVQI5dHEDkZeJuhUtRLwr-65NqB6QoPNin7IwihN5u2HZ4Ep5SFG6Y-LwpkPFQKZQ_5lJD76CwdYrcnlZc2LObn4GCvq59oHK8p7UT6sNMKFnmef5OHJO_3iVi1VWylbs1-7m3aOs8ZIJaVZKkqbMg443', start_index=19415)
Annotation(end_index=19428, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpcjYLX4tdmhR1OuVu0jivkzEqDkUprFIqJDH-epF7SqtxiAcbZB427fLPAYh9ZdkBnEiiPDPNE88Wtmv-xHCEptz6YDVq8MlI-LzfQZnjOcmVTdBnvY0sdYgyXG2Wew==', start_index=19415)
Annotation(end_index=20794, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjMnkb5sMgFAZy7igC1tk11lhmpHlpp7zfBOJVFqR9kbPMhcKfeHJigJO8KtizKO4vupEHWLmaiHjf9Hst6wl29r7l4mjmaLVdhBjhDfoSlTWsQN1XVpHzOF52xIhdWF90lcnGUdAOWv3lISzPa5gLoNqo8ehrEursoU0AjjC78SG9sEWKuFZie-QcjfEMwza-jhVE28VRD_XF8I0GjKT_uGNVwu9M-ALzDwInHYKodRAJkA2WtMcZrs0jT3UNLSIa973TubQ=', start_index=20784)
Annotation(end_index=20881, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG88-SbXrQCkvggmiMfAa_WkCDn-AmUDfUDg4A-FZUdSIK1QTqUpC5saloTCKTo2FfS0tEjUuwyhWdnToTeATK2sUcy0c9CNCaqte68oPreiYkyXm80f1xS0RcoC1lpo7Tq0Rn0NqVbecsqSMWrOOFp_bs7xL_G8rFWy6VNlsORjZRvfpUseD3fPXKKiVOi-m809iG2yNZG04pBGELhS-9A_t0=', start_index=20871)
Annotation(end_index=20960, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEgnwL-ulEqA6DwMLIxS6NvHzt7LuiEQMi-yeaHk8IpDB3JXtovh5RIYuFz90r_JP9C1SHj3FBF7Mic6ZY9X20DMmZ4jQ-aYUoqikmGrfl-y14XI8dKJg7o151oJU8-Q9pDOyx94kFmzKSt2MeDE3EfL1al7v7PJ4rIdW7t_8kSye0XHFR', start_index=20950)
Annotation(end_index=21046, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFvbBBRCtCjRjcfTpoX-VRm7n3HrmU-MNaFQgtUWTdHfXQCcMrzjqAuTMILdv8FnNOoAN368IaEQsXJYbJ3YOLdwR8F557yPaoHEfYpYYL57fcfKbvuuKlmULywEMKsf1QDdriP5DRVxZvdaZvbSsiqbOj0AF4JyGO2oBXQtQfWnMUtk6aMA3whh2AJPFWFrp4PWoVeixm0LG69Z0EcC8io', start_index=21036)
Annotation(end_index=21138, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFc4ZGtI8fZwWoim8q6MTHy79oObySwzgZk6OJ5yO1_F7RKQNGW0qcq5doBpihwahqzCPjTjuK91iPQqBjeanbhQykp3Lc9ihRXxIrfWz95_dYluRAUy-IQ2lUfW8mqvH5oC3cR3zachtrAQApqjx2U4AKnb0GOjq9m36m9rLUz6ydpRXmsLmlx', start_index=21128)
Annotation(end_index=21218, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCvJDj2oEPLVmVDgMrs4Pq7sx_GSHJ3NycMH2RYs-Z6Z1qrinq5yxO2Ve-wvdGwFuwwM9v5_Iben9yatltf267RZOdtFzxsS_8de_g4AHCQb1nhniAYoKdSDa2lH1mGEKWGQ==', start_index=21208)
Annotation(end_index=21303, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyUDvG-_Ht8wOu9ylj5oOQC-W6lfZgJ8rwJqsF8g3bdajFCIk3OUBnGqL2uTRcPd-V4mKWGjN7x056JQNjJ6bUVurjCWiL6YC70LzhqKJyE22OiEww9BuibVGTj_3JeHAvizQZDue1DQ1usagoqyex0WrdtjpmmhUas4Yj0GZXuWdx9Wbn8SDSkjxLgn4Qwe3dT9bpnuM_x83xzPtxKGp5FKS9ttIobSSx2bZb', start_index=21293)
Annotation(end_index=21401, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFY1uRm27GTUUqcPTGw8Y-xxm0eRUKoEEjcFDZiau7q-dKzTPklZiM6k_2hb1OKx3PRyM8pbVK965UJsxEEU9iYyb4xd2wos4O-6HBvPvYtiVPuqpduqRpKLj1i-k2lOQvEOZtP', start_index=21391)
Annotation(end_index=21450, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9vbt5CcqlxAJ7w4usgoWIRG4YEwMGJHAKh3bQeBm3LWObzKbS__4utaKHjX2pFagexHUfqGjhp2Glf8XdWoycPukyA5oCh3c_4tY1R2kO_c0-7PXZkThA8ZjyQwB_Z1OONiTVBufDZFYqUfDj', start_index=21440)
Annotation(end_index=21507, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcaaE6buCAhomvDqFsnNiMZJktiT48lSkGNwCoLWt8TQWBSh2K7BfURgPZDN22-YSGjUJ3lGPW0vGM_Dn4cVafvQjWfnRbMIvEvLpWlFUwxj-GxLUwEN08lyMLB-h1DQ56xyldo4hDIthY58w=', start_index=21498)
Annotation(end_index=21552, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-kae6fAOcButL8m8hkPJyoZz91hjLs0DvlHxzfeVLqYqvFHedK3FzlL3L5-bNMkugV1BASkzGcvNR7t__flyZ85hMvfqnj4VklJ8poZkmSlT15ND8MeOvO9NyRBDuzpWBIW63JTH5DpCAV1fmcKWihww0ag==', start_index=21543)
Annotation(end_index=21605, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOzzUFRqMwSoZC86sHvfSWU3mUH3R2CNStpseSmK0tZZjy6iSEOVFpN1wOsHlpNTggo2AP6P1Jgi8ecFC7ntXuq773YtuT9vu04wKekxN6qLQjeeZ7JVClPCamY4SYUUAHp_eNBF4zlzNyTBtUWlk=', start_index=21595)
Annotation(end_index=21687, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEeFX2Tz6z1wDFDG3iP1gbBLAzbB40mMSIGAmJpMDa0NBZyFxYCkIWGaAW3MwwIfs4SzQW-Q-1cX5lEcO7YIqEIqf4xNH4gPg_22bmgy1ajL2SjxqOo', start_index=21677)
Annotation(end_index=21760, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpYaYFvkzjLNEMh5YWOtny-sUNLEVpxM117WqRs_3QybenHjeJW58iTegKY3RuZtL8wRkxedncSD2S9kfcHf4CQVYy_4GhI2Z_MHv_-XarqU2J40zIgJyKYcJFbuqHBezgGsY-oTBqqM6W9sAnrNMQgEjq2UKJ4JVLBxZWmXarmZpVnt0TQo1XXmYJvo6ddVjDYniM446fbU5VSnEERUO5GlWAre6mmsXNwKJKdlrkFWjcclZO1DiktZU3SQ==', start_index=21750)
Annotation(end_index=21837, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHCiIC0QPuhlMM9djAtPRberf7Outn9jX2JNDesucSslKf1XjNlazdyRh6r7hriMhEpv4Zf80YbOu2mI21f-ZXPd6UbA0cXruYhdLLNH0GJE6oMliO9TKZLHREOdZs8Oq3tCZ1FfowGrFZo2NHVTIOtMBpYQJoi7gJ0CnzKV2C7r4a5FQGv-s0bdgX_InY-hsDWSw==', start_index=21827)
Annotation(end_index=21921, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFc4ZGtI8fZwWoim8q6MTHy79oObySwzgZk6OJ5yO1_F7RKQNGW0qcq5doBpihwahqzCPjTjuK91iPQqBjeanbhQykp3Lc9ihRXxIrfWz95_dYluRAUy-IQ2lUfW8mqvH5oC3cR3zachtrAQApqjx2U4AKnb0GOjq9m36m9rLUz6ydpRXmsLmlx', start_index=21911)
Annotation(end_index=21987, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGHMjtDt7ApaTxgpezg-c1d0GVb49nR9HXI3fiWDc3Ir5owXcV9zodqZlvlk7L0IsKKi0Y1Q-P5O2wbz0IWjfoNf3lWiznEwjVLjrpctG5RIhvC3QiRBn_FG6KwneJofDyQk6sWREtrrL7dUGGXNSf8EnASCdXzPte0SQCMNlxfazHgfZQUYOcSuJ7ln6h_pVNcX4ZxSw==', start_index=21977)
Annotation(end_index=22062, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyUDvG-_Ht8wOu9ylj5oOQC-W6lfZgJ8rwJqsF8g3bdajFCIk3OUBnGqL2uTRcPd-V4mKWGjN7x056JQNjJ6bUVurjCWiL6YC70LzhqKJyE22OiEww9BuibVGTj_3JeHAvizQZDue1DQ1usagoqyex0WrdtjpmmhUas4Yj0GZXuWdx9Wbn8SDSkjxLgn4Qwe3dT9bpnuM_x83xzPtxKGp5FKS9ttIobSSx2bZb', start_index=22052)
Annotation(end_index=22124, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtrN4hLumxewo0LGmhVDJYT-3UotfmA2UfEWyljWkDI6m_MJ088OnPUjoAzR-vK6RjxOl8VJns3eo5wy_bquJGzR2XPUOoyhLmUHui6hifyqd3T9R7_eWXB4_LcI5H-1P7rRWfVbQvGxf4GEs5BIxT6DAjF30T1thKQkoXScHjocBnQj-mpe3nKRNs45XiqnTs5YCNqw==', start_index=22114)
Annotation(end_index=22212, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpcjYLX4tdmhR1OuVu0jivkzEqDkUprFIqJDH-epF7SqtxiAcbZB427fLPAYh9ZdkBnEiiPDPNE88Wtmv-xHCEptz6YDVq8MlI-LzfQZnjOcmVTdBnvY0sdYgyXG2Wew==', start_index=22203)
Annotation(end_index=22274, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBw2mHOqPU7HQcCk_dC87xTvcxVTQdRYNuH5EEzx2rpShKSaC3x8jS10tqzShIN62K8NO8jJLnc6UdVQI5dHEDkZeJuhUtRLwr-65NqB6QoPNin7IwihN5u2HZ4Ep5SFG6Y-LwpkPFQKZQ_5lJD76CwdYrcnlZc2LObn4GCvq59oHK8p7UT6sNMKFnmef5OHJO_3iVi1VWylbs1-7m3aOs8ZIJaVZKkqbMg443', start_index=22264)
Annotation(end_index=22353, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwxslGQU0sUXbDmrxO2j73MD-oOLPKMfERxe5f_Gv6y4S2nkizYjHc47qdqK5oPdse_ijhWX4_SHYrQgQdrWD5dpWwgtE-L6D7ZuEjcyzak4yhMTR5inaUboc8krNis7O6BUQ6QV4HprXOxJNjWSIj5KQVdTUKOwoFZw7s0jOGW7dgxtASrqx1zWHtRLEP', start_index=22343)
Annotation(end_index=22447, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfpSa5DHXOpd-fo5_lBJ7kd57kHd09xNNNWGh0Ri0awWC-qiGDPVvyHwLRx-lGqrp4P-ovQBBWjEJQypUJZaNtlESjjDu14aBFDPtmQkZPOAGeXfAS1z_kz4YZ55xalpFjQlvjcwyj9YtRf3n6F75QFrv5YIo=', start_index=22437)
Annotation(end_index=22508, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH9vbt5CcqlxAJ7w4usgoWIRG4YEwMGJHAKh3bQeBm3LWObzKbS__4utaKHjX2pFagexHUfqGjhp2Glf8XdWoycPukyA5oCh3c_4tY1R2kO_c0-7PXZkThA8ZjyQwB_Z1OONiTVBufDZFYqUfDj', start_index=22498)
Annotation(end_index=22565, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-kae6fAOcButL8m8hkPJyoZz91hjLs0DvlHxzfeVLqYqvFHedK3FzlL3L5-bNMkugV1BASkzGcvNR7t__flyZ85hMvfqnj4VklJ8poZkmSlT15ND8MeOvO9NyRBDuzpWBIW63JTH5DpCAV1fmcKWihww0ag==', start_index=22556)
Annotation(end_index=22618, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7thpsMNvBAEkeSQUS8Shm9whudurtT0tPU0XRngLeN65nMB9jpxir3j6pNUAsDcxVvsw6D2RANjCGn20yuhQp0CmKtZnsWCbUDG6XXWpD3IaP35otZyhc', start_index=22608)
Annotation(end_index=22704, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxTF0lEYNLcIGznleB--eQZE3Yx4bo5lp3XA51_vy7ONG0usIIHDZv4OyNq40vookd00fwz4rzREnNAdfc8_me0sQ2_UQ59chbWCHdyQZWQuZqDj8vGA34TFcWOVtqFWyHi3Nsr2SUIuU=', start_index=22694)
Annotation(end_index=22777, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGG9-XzbNZUyUf8jxbqXQwRlQgF736WPeuhZkDyT3FKrhhJS1WRYWTtLQqy-YVyII6WVP99PpqMGHzpkH6FF8LgSUnAdbBFVFy6QwOUUetJQIp8TdR_WVJsE1QySXPwuC14lfMm8H3_poIp9WwuK2TYXAlPVmsshR_M1vJDQglkEiEeXUKUeLdiPtDfwouuIkJe-z2kLhTqNp4YFz6_No8qNMPsDS6xkqgMWsvRSj70htMyzXo05P4IumH4wKcmrXkS-tb8POVa2a3zLISFBdQ02mwUNA6n_X_IVYHybFVtMPtFnqPNKWl_0V5Hp_dhqsDNcelIy7M1I65nAQ==', start_index=22767)
Annotation(end_index=22856, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrdijIbMHVdG8FSK9Kcpwbn7CudxZRDgGsma0rUmsu9qUIlXRD8coMB8_CsXPT2i0v5wT0e5X_smAZqfpUdvNkBzQmgFMf8VE5lfIsyWK5Y6yYTDVfs_DskpjkBdFLqESKM9CaEYr_sr5Obg5EfyQvNugZ6ffG83RQ6E7XRb6NVDl6vA==', start_index=22847)
Annotation(end_index=22923, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFzrIUcrOl6eF_KWxgKEEpBHU6s7oMRUBrvfZoGiZDTyxaN8WT5kFF_77TBguhNFQxksOrt-Tpx_ZcVQm5VS79RgdK0cjSKOootdF2xLiDd6H2a5lNbeuQVWXHNWAHjru-YkMVcxXF16wGlnjHKWDrq9X5GwYAEVygh8Q==', start_index=22913)
Annotation(end_index=22984, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXwynuAS3bVmc7aGbZNEvwbAEVcPvJ-wb2j_cmm5R8bm35W7qa5nwOmP433ho4OCHiMPGJnpodLuIoMY76QYv-WmRhKVTqHh1E6GYhjWx2r1c1WU0vC5hh_dkVRvAEkwpjPQ8=', start_index=22974)
Annotation(end_index=23031, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHV5S_860xkBRV8oKOYk2A_kWxtRgCaHdevMiWem4kx95CPS6ThrNxmnjNbNGJa9GDxSXtabpAxx1zGkQxhaQ-imqgDi22iuDyo3SmcTGOTKAwjGJOVN-UqdlL-a_tBfXR_xiDqGAcL-1qhOlDgwRoFWRZZ5cEKFBX6wv2E7SiN1iGdD7l3dupSERXVi8MNS4Mln7FZAhdE7usslMnWWteFkXk7pe0ORNw=', start_index=23022)
Annotation(end_index=23130, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEJgfpqqh1A3Ow-Vj6J2lczwcow74-ZySornY1J0wT7m-mtNQI4r7GozT_aZa5KROkum4E98yFm8wMerXr9-szHPOuPWPLY5OMKLdecWOzAlu7Ui33xEpqC5uNF5WC2ZcRTFWjGzOykcvkLVWxHvSxgCsQyEW-yjgzaqE-mBczVhS4engfbawzmyQ==', start_index=23120)
Annotation(end_index=23193, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzViE1TURcIOrJDHyJsGruczRXgJB1F3jm4UTvXGxLiVohwD8E4GV9l9wMMS-cLiASkVegXZYAzE5Q6G5PQafOVKP-OF4MLPKhysBQcVhuGmnaob24L7okp2nTKrUsmM8K2A==', start_index=23184)
Annotation(end_index=23243, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8SX192fJ6O59ZQi0DrBMmFLkush3pXPNeYU1Z7k2ooKv6wAcaDPidlahSg2JRT6lWd97jg-f931oNcAR5ayMV0l2v5QAh_eZWK-UFWaxdULSwWiTC4ZSs3yAeRIt7eEi_D2B3jZhm6xnGMVTNyGWlTr-6acP7xQ==', start_index=23234)
Annotation(end_index=23302, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0fsHhDqrk7DnLEFsZvX6xnOk0y4HoJQ-7UG6n-OXXfHEptMOJTMUpDPiFGNb4BCFPru2VOaXl1MjszEowsDRvOS51Goc3MV2GHgfaCizKNvBw-zmMNHDCUwaCCfULXpduPkzuxB3n8_7FYIGJj6dRjCR__PZozMGFDP-qT6H7KMo=', start_index=23292)
Annotation(end_index=23376, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE0fsHhDqrk7DnLEFsZvX6xnOk0y4HoJQ-7UG6n-OXXfHEptMOJTMUpDPiFGNb4BCFPru2VOaXl1MjszEowsDRvOS51Goc3MV2GHgfaCizKNvBw-zmMNHDCUwaCCfULXpduPkzuxB3n8_7FYIGJj6dRjCR__PZozMGFDP-qT6H7KMo=', start_index=23366)
Annotation(end_index=23438, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFiFqspybHJnbNZxV9nj_3CAZZe995dszv3nxrwQIqypucb13h4kTF7RX6kis3i7OIsZir3oboJFsuk-jCtAhmoxd4Z6YIQxuGiNZY8TTDYXem1VWwEaw4qOKh1AtT0jWmjOwUB0vvBi833kbPP8U7301i73bcghob2rKz4SKECN-zoopuILRqLK_uPVIh2P6B9nmIl_rTw62A3Emoq6ueeXXEo1qVF', start_index=23428)
Annotation(end_index=23506, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHV5S_860xkBRV8oKOYk2A_kWxtRgCaHdevMiWem4kx95CPS6ThrNxmnjNbNGJa9GDxSXtabpAxx1zGkQxhaQ-imqgDi22iuDyo3SmcTGOTKAwjGJOVN-UqdlL-a_tBfXR_xiDqGAcL-1qhOlDgwRoFWRZZ5cEKFBX6wv2E7SiN1iGdD7l3dupSERXVi8MNS4Mln7FZAhdE7usslMnWWteFkXk7pe0ORNw=', start_index=23497)
Annotation(end_index=23587, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGYrgEW4fKOeLU7txUovJMi_4qOaF4jxZq6ZlWhFmEzKwRgrS4SlHXetYAbwsbXwlFGCQz_B6XVrqHAcmLGo87c6IwkDjJC-3qw4okYzNvCSMGA-msD4s7aG3cu19ntmDwrbzrRxJ9Vm4PAA==', start_index=23577)
Annotation(end_index=23648, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHki-xZ4G0zGmiJzsy1oJkJMFuroeFcnTE6y2tQ-VVHsdoMwwvRzP2Gs2y3XsJev9ycYPBGCutqTEZFVpaCWAdkJAS3haikRSpAsGBctA4EFlCLtuo4z9nNKMtKSvPd', start_index=23638)
Annotation(end_index=23691, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFbnVlh8v02zPXTvC5lcgwmD4braYdHpYQiGSxSXJrx0eRccZEJm8vbuKhdXsLO3lsZlH7G6sV5WQMUiHq9U3rBSG9QVVZStxTF-0HvNp0blldQl6ebj_dB9OeXMYtsKHml_oSO4WgwO-sCnvHxxRR7I8nX9CqEVIeIzXdZ9ixCnw0TW2w=', start_index=23682)
Annotation(end_index=23756, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFrdijIbMHVdG8FSK9Kcpwbn7CudxZRDgGsma0rUmsu9qUIlXRD8coMB8_CsXPT2i0v5wT0e5X_smAZqfpUdvNkBzQmgFMf8VE5lfIsyWK5Y6yYTDVfs_DskpjkBdFLqESKM9CaEYr_sr5Obg5EfyQvNugZ6ffG83RQ6E7XRb6NVDl6vA==', start_index=23747)
Annotation(end_index=23813, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE2tKflqSxU24Q23m3czID7KX5dhcJ2G9wzpCde-b8qNevgscdTtxdpYFyuRi17Gqc1XEicIpSDZt6L2P15o0jblpYnQ5wrGgk8-PMD3xy6ZG67KGN2dP0vSS2y47CcEnWuB24kZ0i7uS4CS_imIn2iSP_mt0i-FibWxQdidFRfnGt5yop_QkPmTbcK0z3bEYe7tKp4OXgfoYt1QQJVCtXlJNO0vA==', start_index=23803)
Annotation(end_index=23910, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH8SX192fJ6O59ZQi0DrBMmFLkush3pXPNeYU1Z7k2ooKv6wAcaDPidlahSg2JRT6lWd97jg-f931oNcAR5ayMV0l2v5QAh_eZWK-UFWaxdULSwWiTC4ZSs3yAeRIt7eEi_D2B3jZhm6xnGMVTNyGWlTr-6acP7xQ==', start_index=23901)
Annotation(end_index=23968, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGG7blgxChWBydnsK43UDmWwzOjTdjV6DHNybd6HdsZg_SCeax8S-pZVQjKtDWUcCXfBh5kI6k_7kB72ZtHQYptTpYTYG0KfEJDHzm-RLyRgHscrkTStXarYTVSlxw8wMxzRqc9ycbfgQahnCt4dpygUynAGeR5YSSgirHdF0RUljvZo8andLY-uWWiqZyrlXQDo5pipkrWSS0-Z9wRCenFk_mpIUd9_4ra1W0uDyZI7A==', start_index=23959)
Annotation(end_index=24061, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFFW6GVGcwxH9mKxpOnn3nxjpJZJPrC8GaecIihAOphRfKj0lKQ86LtjXBOQqwjOnVR-DGC_CxnvTkpq7PjCA26BNQmJJwsipvZ9zjxV5niInlMuPObndDZVoK4FkRlJdwlEX756-avwhVuOKjuDDWIW68Bt2w7f9w3BK3aUksTxFM733_6mJJoKw==', start_index=24051)

## Sources
