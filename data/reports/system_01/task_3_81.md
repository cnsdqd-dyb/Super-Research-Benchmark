# Deep Research Report: alibaba/tongyi-deepresearch-30b-a3b
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 4c580cde | **Time:** 18.49s | **Cost:** $0.00074
--------------------------------------------------------------------------------

The **API permission hierarchy in third-party access standards** (primarily governed by **OAuth 2.0** and its extensions) is established by a combination of key concepts and mechanisms:

1.  **Scopes (Core Mechanism):**
    *   **Definition:** Scopes are the fundamental building blocks of the permission hierarchy. They are strings (e.g., `read`, `write`, `email:read`, `contacts:write`) that represent *specific, discrete permissions* an application (client) can request.
    *   **Hierarchy Establishment:** The scope structure creates a hierarchy of permissions:
        *   **Granularity:** A scope like `user:settings:write` is broader than `email:read`. The hierarchy exists through the conceptual breakdown of permissions into resource types (user, emails, contacts) and actions (read, write, delete).
        *   **Breadth:** Multiple scopes collectively define the *total* permission level granted. Having both `email:read` and `email:delete` implies a broader permission level than just `email:read`.
    *   **Operator Overload:** Some standards/implementation frameworks (like OpenID Connect or specific provider implementations) allow combining scopes using operators like `+` (union) or `.` (hierarchy), further refining permission hierarchies (e.g., `openid profile+email`).

2.  **Authorization Server Enforcement (The Gatekeeper):**
    *   **Role:** The authorization server (AS) is responsible for issuing access tokens and *only* including the scopes explicitly authorized by the end-user.
    *   **Permission Hierarchy Enforcement:** The AS validates the `scope` parameter requested by the client against its policies and user consent. It *cannot* grant permissions higher on the hierarchy (broader or more critical) than the user explicitly consents to. It strictly encodes the *authorized level* of access into the issued access token.

3.  **Resource Server Enforcement (The Lock):**
    *   **Role:** The resource server (RS) hosts the actual protected APIs and resources. It receives access tokens from clients.
    *   **Permission Hierarchy Enforcement:** When a client presents an access token, the RS *must* check:
        *   **Token Validity:** Is it not expired, not revoked, has the right audience?
        *   **Scope Requirement:** Does the token contain *all* the scopes required to perform the specific requested action? (e.g., To delete an email, the token must include the `email:delete` scope).
        *   **Effect:** The RS *enforces the hierarchy* by denying access if the token lacks the necessary scopes for the requested operation. It acts based *solely* on the scopes encoded within the token.

4.  **User Delegation & Consent (The Foundation):**
    *   **The Root:** The entire permission hierarchy stems from the end-user's delegation. The authorization flow culminates in a consent screen where the user sees *what* (scopes) the app is asking for and *what* permission level it grants.
    *   **Hierarchy Impact:** The user selects a specific level of access within the defined hierarchy presented by the scope list. Higher-level permissions require explicit user confirmation.

5.  **Client Registration & Trust (The Context):**
    *   **Role:** Clients must be registered with the authorization server (often providing a `client_id` and sometimes secret). The registration process may include defining *valid* scope names the client is authorized to request. Well-known standards (like OpenID Connect) define a specific set of commonly used scopes.
    *   **Hierarchy Impact:** The client is constrained to request only scopes defined within the authorization framework or its own registration context. This prevents arbitrary permissions and maintains a consistent permission hierarchy across implementations of the same standard.

**How It Works Together (Simplified OAuth Flow for Permissions):**

1.  **Client Requests Scopes:** The client includes a specific `scope` parameter in its authorization request, listing the scopes it needs (`user:read email:write`).
2.  **User Consent on Authorization Server:** The user sees a consent screen listing these specific permissions. They approve or deny them.
3.  **Authorization Server Issues Token with Limited Scopes:** The AS issues an access token *containing ONLY* the scopes the user approved (`user:read` in this example).
4.  **Client Calls Resource Server:** The client includes this token in an API request needing `email:write`.
5.  **Resource Server Enforcement:** The RS checks the token scopes. It finds the token has `user:read` but *not* `email:write`. **It denies the request based on the permission hierarchy encoded within the token.**

**Key Security Implications:**

*   **Principle of Least Privilege:** This hierarchy allows granting exactly the minimum level of access required ("read emails" but not "delete emails").
*   **Explicit Boundary:** Any action requires explicit scope permission, preventing ambiguity.
*   **Enforcement at Source:** Both the token issuer (AS) and token consumer (RS) enforce the hierarchy.

**Beyond OAuth Core:**

*   **OpenID Connect (OIDC - Extends OAuth 2.0):** Adds identity scopes (`openid`, `profile`, `email`) and ID tokens, further expanding the permission hierarchy to include information about the user.
*   **SCIM (System for Cross-domain Identity Management):** Uses scopes (e.g., `User`, `Group`, `Schema.ServiceProvider]) to control provisioning permissions for user management APIs.
*   **JWT Claims (Optional Extension):** Access tokens (often JWTs) *can* encode claims like `scp` (scope) or `permissions` directly, reinforcing the hierarchy the AS set, though the RS should still validate scope requirements independently.

**In essence, the permission hierarchy is established by:**
1.  **Defining Permissions as Scopes** (granularity & breadth).
2.  **Reflecting User Consent** on those scopes.
3.  **Strict Enforcement by the Authorization Server** during token issuance.
4.  **Rigorous Enforcement by the Resource Server** during API calls.
5.  **Constraining Clients via Registration & Standards.**

The scope mechanism within OAuth 2.0 is the core structural element that defines and enforces this permission hierarchy.

## Annotations


## Sources
