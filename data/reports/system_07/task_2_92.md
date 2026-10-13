# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 8236b389 | **Time:** 15.35s | **Cost:** $0.01563
--------------------------------------------------------------------------------

The “authentication-intensity hierarchy” you end up with is not chosen at random; it is the product of a short, formal risk exercise that weighs five things against one another:

1. Business impact of a compromise (how much money, data, reputation or safety is at stake).  
2. Likelihood that an attacker will try (value of the asset, threat intelligence).  
3. Regulatory or contractual floor (HIPAA, PSD2, PCI-DSS, FedRAMP, etc.).  
4. Usability/cost constraints (customer friction, support calls, hardware budget).  
5. Technical environment (on-prem, cloud, mobile-only, offline-capable, BYOD, etc.).

Those five inputs are mapped to the three measurable security dimensions that every modern standard (NIST SP 800-63, ISO/IEC 29115, eIDAS, BSI TR-03107, FIPS 201-3, etc.) use to build the final “level of assurance” (LOA):

A. Identity-proofing quality (how strongly you tie a real person to the account).  
B. Authenticator strength / number of factors (what the user has to present each time).  
C. Lifecycle controls (how securely the credential is issued, stored, rotated and revoked).

Put A + B + C together and you get the concrete “intensity” ladder that appears in every policy:

- **Low / LOA-1 / AAL1 / P1**  
  – Self-asserted identity, single-factor (password), network encryption enough.  
  – Used for public brochures, campus Wi-Fi, newsletter sign-up.

- **Moderate / LOA-2 / AAL2 / P2-P3**  
  – Remote or on-line identity verification, two factors (e.g., password + OTP or push).  
  – Used for student portals, patient appointment systems, standard on-line banking.

- **High / LOA-3 / AAL3 / P4-P5**  
  – In-person or supervised remote proofing, two *different* categories of factor, one of them hardware-based and tamper-resistant (PIV card, FIDO2 token, smart-card + PIN, biometrics with liveness).  
  – Used for electronic prescribing, money-movement above a threshold, cloud-admin consoles, classified research systems.

- **Very-high / LOA-4 / “P5+”**  
  – In-person proofing with background check, hardware cryptographic module (FIPS 140-2 level 3+), multi-party control, audited issuance.  
  – Used for classified networks, root certificate authorities, nuclear or aviation safety systems.

If a single user has several roles, the strongest applicable level automatically wins (UF policy quoted in the search results is explicit about this).  

So the hierarchy is not determined by the authentication technology itself; it is determined by the risk-and-compliance calculation described above, after which the technology is selected to *meet* the resulting LOA/AAL/IAL row in the table.

## Annotations


## Sources
