# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 87739646 | **Time:** 24.81s | **Cost:** $0.01668
--------------------------------------------------------------------------------

Qualification requirements in a merchant-onboarding audit are not invented by the acquirer; they are the by-product of four “layers” that sit on top of one another.  
An acquirer/PSP simply translates each layer into measurable checkpoints that its underwriting or audit team can evidence.  
If a merchant (or the acquirer’s own process) fails any checkpoint, the qualification is not met and the file is either declined or flagged for remediation.

1. Statutory / regulatory floor  
   - AML/CFT: FinCEN (US), MLR (UK), EU 6AMLD, FATF, etc.  
   - Sector-specific licence: e-money, lending, gambling, crypto, pharma, CBD, alcohol, tobacco, export-controlled goods.  
   - Consumer-protection rules: FCA safeguarding (UK), EFTA Reg-E (US), EU PSD2 safeguarding, UPI/BPSG (India).  
   These laws tell you **what must be verified** (identity, beneficial ownership, source of funds, licence validity, safeguarding account structure, etc.).  
   Audit test: “Can you produce the licence certificate, the BO register, the safeguarding-reconciliation log and the SAR filing reference?”

2. Card-scheme rules  
   - Visa Merchant Business Due-Diligence (MBDD) and Risk Management Program.  
   - Mastercard MATCH & BRAM; PCI-DSS v4.0 for every merchant that stores, processes or transmits card data.  
   - UnionPay, AmEx, Discover, JCB have near-identical checklists.  
   These rules tell you **how deep the verification must go** (e.g., three months of bank statements for a <12-month-old entity, onsite inspection for high-brand-risk MCCs, quarterly ASV scans for PCI).  
   Audit test: “Show the scheme-compliant KYC pack, the signed PCI-DSS SAQ/ROC and the quarterly ASV scan ticket.”

3. Acquirer / processor risk policy  
   - Board-approved risk appetite: maximum chargeback ratio, maximum exposure per merchant, prohibited countries, prohibited MCCs, velocity limits.  
   - Underwriting matrix: required documents per risk tier (low, medium, high, prohibited).  
   - Collateral policy: rolling reserve %, minimum reserve balance, guarantee letter, personal guarantee.  
   These policies tell you **what extra evidence is required for the risk class the merchant falls into**.  
   Audit test: “Demonstrate that the file contains the reserve agreement, the personal-guarantee deed and the signed merchant-services agreement that matches the approved risk-tier template.”

4. Internal operational / quality standards  
   - SLA: “KYC file 100 % QC-checked within 4 h of underwriting decision.”  
   - Documentation completeness index: ≥ 95 % of mandatory fields populated.  
   - Dual-signature rule: underwriting decision signed by credit officer + compliance officer.  
   - System-of-record integrity: every approval/decline reason logged with immutable hash.  
   These standards exist so the acquirer can prove to an external auditor or regulator that the first three layers were applied **consistently and traceably**.  
   Audit test: “Produce the QC checklist, the dual-signature log, the completeness score and the immutable audit trail hash.”

-------------------------------------------------
How the four layers become “qualification requirements”
-------------------------------------------------
Step 1 – Map each legal/scheme obligation to a **data point or document**.  
Step 2 – Assign the data point to a **risk tier** (low/medium/high/prohibited).  
Step 3 – Build a **binary pass/fail rule** around it.  
Step 4 – Embed the rule in the onboarding workflow so the system **physically prevents** the MID from being activated until the rule = PASS.

Examples of binary rules that auditors look for:

| Requirement (layer) | Binary rule | Evidence auditor requests |
|---------------------|-------------|---------------------------|
| FinCEN Customer Identification Program | “BO ≥ 25 % verified with government photo ID + address proof dated < 90 days” | ID selfie match report, address proof PDF, BO register |
| Visa MBDD | “Website content review signed off for IP/brand infringement” | Signed website-screenshot pack, IP clearance letter |
| PCI-DSS | “SAQ A-EP submitted and QSA/ASV tickets green” | SAQ PDF, ASV scan ticket, Attestation of Compliance |
| Acquirer policy | “Rolling reserve 10 % for CBD MCC 5499” | Signed reserve addendum, reserve ledger extract |
| Internal QC | “Underwriter rationale ≥ 50 characters free-text” | Underwriting comments field, QC sign-off stamp |

-------------------------------------------------
Practical takeaway for acquirers
-------------------------------------------------
1. Maintain a **requirement-to-rule matrix** that links every statute, scheme rule and internal policy to a specific document/data field and to a pass/fail condition.  
2. Make the workflow **hard-stop**; a human cannot override without a second-level approval that is automatically logged.  
3. Store everything **timestamped and hashed** so an auditor can re-play the decision in minutes.  
4. Re-certify the matrix at least annually against new regulations (e.g., UK FCA safeguarding 2026, US EO on debanking 2025) and updated scheme releases.

If you can produce the matrix, the hard-stop log and the immutable evidence pack for any MID, you have “determined” – and can defend – every qualification requirement in your merchant-onboarding audit.

## Annotations


## Sources
