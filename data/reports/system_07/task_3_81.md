# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 255da1fc | **Time:** 11.43s | **Cost:** $0.01450
--------------------------------------------------------------------------------

The hierarchy is not defined by a single RFC or ISO document; it is built into the authorization framework you adopt (OAuth 2.1 / OIDC, SCIM, Android, etc.) and into the way you design the scopes, claims, roles, and consent screens that the framework uses.  
In every mainstream standard the same three-layer pattern appears:

1. **Framework layer** – the standard itself (OAuth, UMA, Android, etc.)  
   - Declares the *kinds* of tokens/scopes/permissions that can exist  
   - States which of those *kinds* third-party clients are allowed to request  
   - Specifies the *grant* or *protection level* that must be satisfied before the token is issued

2. **Tenant / Resource-server layer** – the organisation that owns the data  
   - Publishes a concrete list of scopes or roles (e.g. `read:invoice`, `admin:project_A`)  
   - Decides which of those scopes a third-party *may* ask for (client-configuration whitelist)  
   - Decides which of them a *given user* is actually allowed to have (user-policy, RBAC, ABAC)

3. **Runtime enforcement layer** – the code that sits in front every endpoint  
   - Checks that the presented token contains the scope/claim required by the endpoint  
   - Checks that the *user* associated with the token is still authorised for the *resource* being touched (fine-grained authorisation, often “user-permission × app-grant”)

Because the second and third layers are under the resource owner’s control, the *hierarchy* seen by a third-party application is whatever the resource owner publishes:

- **Coarse-grained example (Slack, Google, Zendesk)**  
  `chat:write` ⊃ `chat:write.public` ⊃ `chat:write:channel:C04xxx`

- **Fine-grained example (Auth0, FusionAuth, custom)**  
  `account.read` ⊃ `account.profile.read` ⊃ `account.profile.names.read`

- **Android example**  
  `signature|system` ⊃ `dangerous` ⊃ `normal` – third-party apps can only climb as high as `dangerous`, and even then only if the *user* consents at runtime.

So the *standard* does not prescribe the exact tree of scopes; it only prescribes the *mechanism* by which the resource owner can expose, and the client can request, a hierarchical set of permissions. The concrete hierarchy is therefore established by:

- The **authorization server’s scope dictionary** (what scopes exist and how they are nested)  
- The **client registration** (which of those scopes the client is allowed to request)  
- The **user policy / RBAC** (which of those scopes the user is allowed to hold)  
- The **API enforcement logic** (which scope(s) each endpoint demands)

Put succinctly: **the permission hierarchy is whatever the resource-owner chooses to publish inside the authorization framework; the standard merely gives the hooks (scopes, claims, protection levels) to express and enforce that hierarchy.**

## Annotations


## Sources
