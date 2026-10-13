# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** f0043c61 | **Time:** 351.94s | **Cost:** $1.56648
--------------------------------------------------------------------------------

# Architectures of Authorization: Establishing Permission Hierarchies in Third-Party API Access Standards

### Key Points
*   **OAuth 2.0 Scopes as the Primary Mechanism:** The establishment of permission hierarchies in third-party access is predominantly achieved through OAuth 2.0 scopes, which define the specific capabilities and resources an application can access on behalf of a user [cite: 1, 2].
*   **Semantic Hierarchy via Naming Conventions:** While OAuth 2.0 does not strictly enforce a technical hierarchy, standards bodies and developers utilize semantic naming conventions—specifically "dot notation" (e.g., `resource.action` or `api.v1.resource.manage`)—to create logical permission trees that imply inheritance and containment [cite: 3, 4, 5].
*   **Integration of RBAC and Scopes:** A robust hierarchy is often established by layering Role-Based Access Control (RBAC) over OAuth scopes. In this model, RBAC defines the user's standing within an organizational hierarchy (e.g., Admin vs. Viewer), while scopes limit the third-party application's ability to exercise those rights [cite: 6, 7].
*   **Resource-Based Inheritance:** In cloud infrastructure APIs (e.g., Google Cloud, Azure), permission hierarchies are established through resource topology, where permissions granted at a parent level (Organization or Folder) automatically cascade down to child resources (Projects and Services) [cite: 8, 9].
*   **Emergence of Agentic Protocols (A2A & MCP):** The rise of autonomous AI agents has necessitated new standards like the Agent-to-Agent (A2A) protocol and Model Context Protocol (MCP). These establish hierarchy through "Agent Cards" and declarative security models that group tool capabilities based on sensitivity and functional scope, moving beyond static token scopes [cite: 10, 11, 12].

### Introduction

The architecture of modern software ecosystems relies heavily on the interoperability of disparate systems, facilitated primarily through Application Programming Interfaces (APIs). As organizations increasingly expose data and functionality to external developers and autonomous agents, the mechanisms for controlling access—specifically the establishment of permission hierarchies—have become critical to maintaining security and operational integrity. Third-party API integration involves connecting an application to external APIs to enable data exchange, a process that introduces multi-layered security challenges distinct from internal system management [cite: 13].

The establishment of an API permission hierarchy is not governed by a single monolithic standard but is rather the result of converging protocols, architectural patterns, and semantic conventions. At the core lies the OAuth 2.0 framework, which utilizes "scopes" to delegate authority. However, the complexity of modern enterprise environments and the advent of Agentic AI have pushed the boundaries of simple scope lists, leading to the adoption of hierarchical naming conventions, the integration of Role-Based Access Control (RBAC), and the development of new protocols such as the Agent-to-Agent (A2A) specification. This report provides an exhaustive analysis of how these elements function individually and collectively to establish permission hierarchies in third-party access standards.

---

## 1. The OAuth 2.0 Framework and Scope-Based Hierarchies

The foundational standard for third-party authorization is the OAuth 2.0 protocol. It provides the mechanism by which a third-party application (the client) obtains limited access to a generic HTTP service (the resource) on behalf of a resource owner. The primary instrument for defining the extent of this access is the "scope."

### 1.1 Definition and Function of Scopes
OAuth 2.0 scopes provide a method to limit the amount of access granted to an access token [cite: 1]. When a client requests access, it specifies the scopes it requires. The authorization server then issues a token that is valid only for those specific scopes. For example, an application might request `READ` access to a user's calendar but not `WRITE` access. If the client attempts an API call that requires permissions outside the granted scopes, the request fails [cite: 1].

In the Microsoft identity platform, which implements OAuth 2.0, permissions are represented as string values passed in the scope query parameter. These scopes allow resources to divide functionality into smaller chunks, giving fine-grained control over how API functionality is exposed [cite: 2]. This mechanism allows developers to adhere to the principle of least privilege, requesting only the specific permissions necessary for the application's function [cite: 2].

### 1.2 Establishing Hierarchy through Naming Conventions
The OAuth 2.0 specification (RFC 6749) does not dictate the internal structure of a scope string; it treats them as opaque strings. Consequently, the *hierarchy* within these permissions is established through semantic naming conventions adopted by API designers.

#### 1.2.1 Dot Notation and Namespacing
The most prevalent method for establishing a logical hierarchy is the use of "dot notation." This convention structures scopes in a format such as `service.resource.action` or `resource.action` [cite: 3, 4].
*   **Resource-Action Pairing:** Scopes are often defined by pairing a resource with a verb, such as `users.read` or `documents.write` [cite: 3].
*   **Namespacing:** To prevent collisions and establish clear ownership, scopes often include a namespace or service identifier, such as `acme.notification.v1.send`. This is particularly critical in microservices architectures where multiple services might use generic terms like "read" or "write" [cite: 5].
*   **Versioning:** Hierarchies often include version indicators (e.g., `api.v1.users.manage`) to allow for the parallel existence of different API versions without breaking integrations [cite: 3, 5].

#### 1.2.2 Logical Containment and Inheritance
Through dot notation, API designers create a semantic hierarchy where broader scopes logically contain narrower ones.
*   **Granularity Levels:** A hierarchy typically ranges from coarse-grained to fine-grained. For example, a scope named `files.manage` might logically include permissions for `files.read`, `files.write`, and `files.delete` [cite: 3].
*   **Implied Inheritance:** While the protocol checks for exact string matches or explicit mappings, the naming convention implies inheritance to the human developer and the policy administrator. A scope of `admin` might imply full access, whereas `user:admin` might imply administrative access only within the user domain [cite: 14].

### 1.3 Challenges with Scope Hierarchies
Despite their ubiquity, scope-based hierarchies face significant challenges:
*   **Scope Explosion:** As applications grow, the cross-product of resources and operations can lead to an unmanageable number of scopes (e.g., hundreds of scopes for a document sharing app). This can exceed the size limits of HTTP headers when scopes are packed into JSON Web Tokens (JWTs) [cite: 15].
*   **Lack of Instance Granularity:** Standard OAuth scopes typically designate general permissions (e.g., `read:document`) rather than access to specific object instances (e.g., "read document #123"). Defining a scope for every individual resource is impractical due to token size constraints and the dynamic nature of resource creation [cite: 15, 16].
*   **Stale Permissions:** Scopes embedded in a JWT reflect the user's state at the moment of token issuance. If a user's permissions are revoked in the backend, the token remains valid until it expires, leading to potential security gaps [cite: 15].

---

## 2. Role-Based Access Control (RBAC) Integration

To address the limitations of pure scope-based systems, permission hierarchies are often established by integrating OAuth 2.0 with Role-Based Access Control (RBAC). In this hybrid model, the hierarchy is defined by the user's role within the organization, while the scope limits the application's window into that role.

### 2.1 The Distinction Between Scopes and Roles
A critical distinction in establishing permission hierarchies is that **scopes** define what an *application* can do, while **roles** define what a *user* can do [cite: 6, 7].
*   **OAuth Scopes:** These act as a delegation mechanism. They allow an application to act on behalf of a user, but they cannot grant the application more permission than the user possesses.
*   **RBAC Roles:** These are assigned to users based on their job function (e.g., "Nurse," "Manager"). A role like "Manager" might inherently include permissions to view and approve reports [cite: 17].

### 2.2 Hierarchical RBAC in API Access
In a hierarchical RBAC model, roles are organized such that higher-level roles inherit permissions from lower-level ones.
*   **Inheritance Structure:** A "Super Group" or "Admin" role acts as a parent to "Sales Group" or "Editor" roles. Permissions assigned to the parent are automatically inherited by the child groups [cite: 18]. For example, in Bloomreach's engagement platform, an `Admin` has full access, while an `Editor` can modify objects but cannot export data. The hierarchy ensures that lower levels never possess functions reserved for higher levels [cite: 19].
*   **Mapping Roles to Scopes:** To enforce this in an API context, roles are mapped to sets of scopes. When a user logs in, the system determines their role and issues an access token containing only the scopes associated with that role. This ensures consistency across services and prevents "privilege creep" [cite: 7].

### 2.3 Granular and Resource-Specific Control
While scopes provide coarse-grained control, RBAC and Relationship-Based Access Control (ReBAC) facilitate fine-grained hierarchies.
*   **Resource Hierarchy:** In systems like Google Cloud, resources are organized hierarchically (Organization > Folder > Project > Resource). Permissions granted at the Organization level are inherited by all projects under it [cite: 8]. This structural hierarchy allows for efficient policy management, where a "Network Admin" role at the organization level automatically applies to all subsidiary networks [cite: 9].
*   **Dynamic Scopes:** To handle specific object access (e.g., a specific bank account), some implementations utilize dynamic scopes or include object references within the scope string (e.g., `account:1234:read`). This addresses the challenge of restricting access to specific intents or transactions [cite: 16].

---

## 3. Emerging Standards: Agentic AI and Protocol Hierarchies

The rapid proliferation of Autonomous AI Agents has introduced new requirements for permission hierarchies. Agents require dynamic, negotiated access to tools and other agents, often exceeding the static capabilities of traditional OAuth scopes. This has led to the development of the **Agent-to-Agent (A2A)** protocol and the **Model Context Protocol (MCP)**.

### 3.1 The Agent-to-Agent (A2A) Protocol
Introduced by Google and supported by various industry partners, the A2A protocol standardizes how agents discover, communicate, and collaborate. It establishes a permission hierarchy based on **capabilities** and **declarative security**.

#### 3.1.1 Agent Cards and Capability Discovery
The core of the A2A permission model is the "Agent Card," a JSON metadata document hosted at a standardized URL (`/.well-known/agent.json`). This card functions as a machine-readable declaration of an agent's identity, capabilities, and supported interfaces [cite: 12, 20].
*   **Declarative Security:** Agents declare the scopes they need and the capabilities they offer in a structured format (YAML/JSON). This allows for a "declarative security model" where permissions are transparent and auditable [cite: 21, 22].
*   **Sensitivity Hierarchies:** A2A introduces the concept of tool sensitivity. Permission groups are derived based on the sensitivity of the tools they access. A permission group supporting data modification tools is ranked higher in the hierarchy than one supporting only read operations [cite: 23].

#### 3.1.2 Hierarchical Task Delegation
A2A facilitates multi-agent workflows where a primary agent delegates sub-tasks to specialized agents. This creates a functional hierarchy:
*   **Orchestration:** A central client or "manager" agent orchestrates tool calls and delegates tasks to "worker" agents. The protocol supports complex, multi-turn interactions where agents negotiate intent and outcomes [cite: 24].
*   **Contextual Permissions:** Unlike static API tokens, A2A permissions can be contextual. An agent might have permission to access a tool only within the context of a specific task or user session. This prevents "poor context scoping," where an agent retains unnecessary authority across different user interactions [cite: 25].

### 3.2 Model Context Protocol (MCP)
Complementing A2A, the Model Context Protocol (MCP) focuses on the vertical connection between an AI agent and its tools or data sources [cite: 26, 27].
*   **Standardized Tool Access:** MCP acts as a "universal toolbelt," standardizing how agents discover and invoke tools. It replaces ad-hoc API integrations with a structured client-server interface [cite: 26, 28].
*   **Permission Enforcement:** When an agent requests to use a tool via MCP, the server validates the request against the agent's permissions. This often involves a user-in-the-loop approval process for sensitive actions, establishing a hierarchy where human approval supersedes agent autonomy [cite: 26].
*   **Scope Mapping:** MCP tools map to OAuth scopes (e.g., `tool:read`, `tool:write`). This integrates the new agentic protocols back into the established OAuth 2.0 framework, ensuring compatibility with existing identity providers [cite: 29].

### 3.3 Comparison of A2A and MCP Hierarchies
While both protocols address agent interoperability, they establish hierarchies differently:
*   **A2A (Horizontal):** Focuses on peer-to-peer communication. The hierarchy is social or organizational, defined by the relationship between agents (e.g., Manager Agent vs. Worker Agent) [cite: 27].
*   **MCP (Vertical):** Focuses on the agent-to-tool relationship. The hierarchy is functional, defined by the access level the agent has to specific resources (e.g., Read-Only vs. Write Access) [cite: 27].

---

## 4. Structural Implementation of Permission Hierarchies

Beyond protocols, the physical and logical structure of API resources plays a decisive role in establishing permission hierarchies.

### 4.1 Resource Topology and Inheritance
In cloud ecosystems, the permission hierarchy is inextricably linked to the resource hierarchy.
*   **Google Cloud Platform (GCP):** Uses a strict hierarchy of Organization $\rightarrow$ Folder $\rightarrow$ Project $\rightarrow$ Resource. An "allow policy" set at the Organization level is inherited by all child projects. The effective policy for any resource is the union of the policy set at that resource and all policies inherited from its ancestors [cite: 8].
*   **Azure/Microsoft Graph:** Permissions are categorized into "Delegated" (app acts as user) and "Application" (app acts as itself). Within these, a hierarchy exists based on the scope of access, such as `User.Read` (single user) vs. `User.Read.All` (entire directory) [cite: 30].

### 4.2 Flux API 5-Tier Hierarchy
The Flux API demonstrates a specialized, explicit hierarchy designed for decentralized infrastructure. It utilizes a 5-tier permission system to control access:
1.  **Public:** Open access.
2.  **User:** User-level permissions.
3.  **FluxTeam:** Access for team members.
4.  **Admin:** Node administrator access.
5.  **AppOwner:** Application owner permissions.
This tiered system explicitly ranks permissions, ensuring that higher tiers (like Admin) encompass the capabilities of lower tiers or have distinct, privileged access paths [cite: 31].

### 4.3 Nested Resources in REST Design
In RESTful API design, hierarchy is often reflected in the URL structure itself (e.g., `/users/{id}/posts/{postId}`).
*   **Contextual Access:** Nested resources imply a hierarchy of ownership. Accessing `/users/jdoe/posts` implies that the operation is scoped to the user `jdoe`. This structure helps developers and policy engines understand the context of a request, although it can lead to redundant endpoints if not managed carefully [cite: 32].
*   **Permission Scoping:** Security policies can be written to match these URL patterns. A policy might grant `GET` access to `/users/*/posts` (read any user's posts) or `/users/me/posts` (read only own posts), effectively using the URL hierarchy to enforce permission boundaries [cite: 33].

---

## 5. Security Implications and Best Practices

The establishment of permission hierarchies is fundamentally a security exercise. Improperly structured hierarchies can lead to vulnerabilities such as privilege escalation and data leakage.

### 5.1 Principle of Least Privilege
The guiding principle for all permission hierarchies is "Least Privilege." Applications should only request the narrowest scope necessary to perform their function [cite: 13, 30].
*   **Granular Scopes:** Developers are encouraged to break down monolithic scopes (e.g., `manage`) into granular ones (e.g., `read`, `write`, `delete`). This minimizes the "blast radius" if a token is compromised [cite: 34].
*   **Scope Sanitization:** In agentic systems, input sanitization and context-aware analysis are used to detect potentially harmful instructions. For example, Claude Code uses strict read-only permissions by default and requires explicit approval for sensitive actions like file editing or command execution [cite: 35].

### 5.2 Zero Trust and Continuous Verification
Modern API security moves beyond static hierarchies to "Zero Trust" models.
*   **Continuous Evaluation:** Permissions are not just checked at the gateway but are evaluated continuously based on context, user identity, and device health. This effectively flattens the hierarchy into a series of real-time micro-decisions [cite: 34].
*   **Short-Lived Tokens:** To mitigate the risk of stale permissions, access tokens are kept short-lived. Refresh tokens are used to obtain new access tokens, allowing the system to re-evaluate the user's standing in the permission hierarchy periodically [cite: 13].

### 5.3 Third-Party Risk Management
Integrating third-party APIs introduces external ownership risks. The API provider controls the hierarchy, rate limits, and deprecation timelines.
*   **Symmetry Challenges:** Third-party apps often lack the granular permissions available in internal systems, preventing symmetry between internal and external policies. For example, an external app might only support a generic "Admin" role, forcing the organization to grant excessive privileges [cite: 36].
*   **Living Documentation:** Security leaders must enforce documentation practices that detail API purposes and data sensitivity. This ensures that the permission hierarchy remains understood and managed over time, preventing "zombie APIs" with forgotten access rights [cite: 34].

---

### Conclusion

The establishment of API permission hierarchies in third-party access standards is a multi-faceted process that blends protocol specifications with architectural conventions. **OAuth 2.0 scopes** provide the fundamental mechanism for delegation, while **dot notation naming conventions** impose a semantic hierarchy upon these scopes. **RBAC** systems integrate with OAuth to map human organizational structures to technical API permissions, ensuring that access aligns with job functions.

In the realm of cloud infrastructure, **resource topology** dictates permission inheritance, creating a rigid, tree-like hierarchy. Conversely, the emerging **Agentic AI** landscape is driving the adoption of **A2A** and **MCP** protocols, which utilize **declarative security** and **capability discovery** to manage dynamic, peer-to-peer permission structures. Across all these standards, the industry is moving toward greater granularity, context-awareness, and the rigorous application of least privilege principles to secure the expanding web of interconnected applications and agents.

**Sources:**
1. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwKaRyFmHZnl36zD7kkwRSZvN5Uu-9VZG7hK1zv1668QaAiLJO3nst2U2QBj6D6tFLw-_36t08QR-VIebwZr5eUuu763vp02w1PuHIHeJhVhtPHakLWoM-znMAj9r_JRV_pOnvBCj4EFscRnGg3oT4EZLHr3KNEx2E3CAFaXxuP2GcwiiTjjgCNw==)
2. [microsoft.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDsGUvEcs1s4t8y5GTW_mZ5Am84uaPNDXg6swYqu4XOJUD8De8QBbgNnZhhIrkErrJvrTflRaDGjC-q7x67IliZLh6QcblUJE3KVcb_xalnuUwq5t7AfdkklPTPsuex_C2m76hLkM1sexE5qc4nYV1O7TrDe28-p1HfQ==)
3. [zuplo.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJ6WO17YgtOlpvLDpyMgV_68Dy8VbiEggCpxVGmdNw7LRH0nOv8eHLR2dXLdjcLcs9Yzrz8Rp-PSJTGjV2bAnYB9XAruQxTJ-7zWUCP-PDiJU8r7rQh2PAq4gS7D2iFN564DCB7eJRgqx2fHTJK7mfEYUO)
4. [dreamfactory.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJyTn2BYtA76Hzsqf383mqWrPTfmY0kmRuzfn-FBUmy_dRS2_MJ0wTH2-rsqejFP3lFQ74Bb2r2Pb7NO2M4fF_9Wp1oDGJn4ZdNwdSACdNBBtnnX75ap9wCcyup_JUqpW8-BAMMyxy7l_5fgmgPkBQgLdSiA==)
5. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0sX-7r5sDzDSgmbIlSkcq0Jrp-bn08A9FkYcbRhEoqWNyrHRDBfpFkpkDEyMKpXAXHsWoBGPmepWwAAbCbYn0ESDJ31GFRquOjzsXpn8myLmVNWbpdiDDWmNw_evXjjVkNtkMzn_bVVakqKWh6Fng9nrwCkwM1yPolIBQr0QteNM6V3T5VkgA8AqYZxitmuyG99fL47SKq-rLMF-cXLYKUx-n2hvA)
6. [dreamfactory.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF51qcMw60dAXtF-Hmwl4SWY37SeuPOJqiBauBnlEeuc2ry95oM01zkZcj-6w3T6ge3CvfGNL9_ZkjxlrabRkAynI_u2hGaCXz5C4UTzr9Br3rKN1dlAq64odrfMyOZsfKXcnPqfuysIhm7TEgsTyp3-X0jAFbEGw==)
7. [hoop.dev](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElZY7S5XWdWll1kDteECrsVleXTw4hEs9KcRMQ59HefG1sCajmo9lr3PZYGvPMG9RlLt-SVI_JricWkMRiJ1safUT5SBjW2huJuCQQeibFX7bsUV1Rqq_7lAIPnSfZc6FV8o46nXz1moIxEp8uuPCd0RuFD692JKRY5HEH0GWNcRf1JuLJnw==)
8. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEwYnBm99v3YjlysDjup2oe7Pm5ulj0Lt-Ex5Vt0L4lBbnmrTZxbyjx6-_cZloR3QKC30riu0bjMS9CEFgc8IwDunJgUv-mdgwLdxIqQ9ErVzIWPsInzEB909MLnp8XaXkaRu8o8gh2WdKtTdQlc_g9xn88UvI_XUsVaePMA==)
9. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYrr5SjHe8TZ5Zks3QOgcO0GYAlC9JhE_I4YVlzAh9NxXzBVxDKKYLiQF9OESDJLtvILSWzq2dJLrVjZD3-Z-w9-VU1fPO6HST8pmHG54UhzHZ8ZW0wwR1OPs-XLv-rXsYWIcwNq9HHqquSds0Da-p8RfVqO5A3S5s9CV1s7Ne1oM7pLjPWkhsIq4=)
10. [a2a-protocol.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF113rkN9807LorSqcrwSQN2o-IGXsbCO5Cnx7vwB_d919ag9Kv6OzC1iZ2swU414wqLwxSg5aPueQ2oncBarddxKlJcaIhrdnylHmBqjTCrJOof0TcOme_h7kXk33CVK4p_iI=)
11. [a2a-protocol.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZ3oQ9F_aX1hvGB1aHrq0RntMNsrOGMIcoU7_1sKdhtsBixQe7zyAdOdBdxP9gVrbq3aa03nzCXDY7PZXV4ULpjpLk084cwx5Si0h65Vy_nsNWqGSu)
12. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLHRH2AD718PQ579h1jSpJxal_X3SbGYqJJswqgTMdVDgEXUUNeA_3tZYFlSFinxUhn9-9w5byUw0PB1DyXAOw-7Xgg0PuJX6A_tO3mHUtjBJ4RWuk)
13. [digitalapi.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdiI_bsIOWQ5LKnoOsMWFHyjCTNx8lLXPOW8neQd561kiE-GBwuG-reBfR6SkierKLmBPHXLRhULgG_cGTNAsxornmXhd2VmBCyRQhlrQLsEelwpLEz9b3ms-V9yNx9QyR3f4U9g==)
14. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-V1YYSP6vISLI0ZU6oMBBpNrGuXZubg9BsLJIJrBWZTC0W6wTfAGftE3r5u9cHdSLJHyo-jFWCNDniZiu-YjP-IZ-jTFGfpLBOBoPrrEpGKijdnQYKh2VUS9ZvQnySvuOHthv6wB2cDmUrQtwlT7k7_7YdQ6XZWJi9kn140Gdn63OnI8nWgSdfiQ-ndV3aD8OrF-Vz-S-qdPXblMI57WG5sWE7F5VLirNwLpApBjt56AWvJdK-QSJ9FQ9tSL_pA==)
15. [aserto.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXCI_KobmuawINLdffbcBKRKw3fL7nnjoUAjm3jhtzy_1uFbfFnbA7onS3UXdqLmL_O1BsS6fNmO2E54r4tlm841TZqJPX9Oxd-UyxEX5FnVSRZ35yf-ffdacEMudDdudgQqvF9f6mkQqkYnhfjIOZ98Btjw==)
16. [secureauth.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMdcrZKkgKAnHwqzk2JGaefd5VieRZfbqk5OZN6elJgHxoMZ3RAgw-Y7W2fsI3nIPcdyIvesao-XnNVvrcrRyp0HGzv1LvdJzx7lwkak02GNnslg2m7CTpnsovxzKLbGsyMH0ODwBtyzLiWwLgMULJYHbdgmp0d8RkObAQqw==)
17. [permit.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEqENqZjUgnBcJ781NUHyZ3sGn1RolMIy1yDg_pr8RQYKWONQ4e-Ocd4VTU69GbHlfiSLp76qE1hO502Hin9MRVZJnUL-wsptWpZRFV4aScJj8byyEOvOMvM3u-iRvuOpUnQg30UkaZXu7aGf7H_92)
18. [gooddata.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGw7AFb3SoEqoDnZ8DM4L_24Uggh4O4eZvUA2ju-tDLOTgjQNzIK79JXtbm0paK8HDSeJ9dXrLeevtr8lr7azu46tWiwIlzxjZW1MulUt9yUKJQ35xseYXyTJU_N2ImIvLScOXNHJ1raYzHF2B7q6uPBD9n5l0Q0l4jp5Q=)
19. [bloomreach.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSu5e9QpDGagg3thA89VKI6akZTD6scMSxurHctzNFZwLI5aMWaumigFkejUprB1HX-G3e8y6-21EjrFSOgD5YD5aERr5DD4LuBbOzZAKYebD_HUIShHvmS4V61f0pKNWng5ncRTu2wrdKnOX7rLVU6K8V8QTOAPORngU=)
20. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErypVhDDyEt-LLCL5Vc02oe-l479tP7EhopKXhfNLfWsIt3Cfw7Mi3deOgqX3umOS-Kj0J0EOw2KHU6Y9eSFjsEHPQ6BlC8hOujvDbojJ8l8buDWLmPhNV08KIMb-QtbKa_ym5JRs=)
21. [dev.to](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFx1_HxlHcwEaxb3ERz94UGRyKL3ArfGwb4DUE-5N3MYl-Id5LwYFpBnuQ1YYeVbrH-6NoVRHobvQVyYRYa5YRj7xgaKmyl2aS2qMdectF8EjRvsyTAd2n7oxsPXvGspVTTq3rVHSDU_Xc89oLgOBLaa7AGQ0xntpHRMFDyaLWrXWcpY8S1C_y4ot12)
22. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwhN2ppUghjW8N7EmNYP_OfvjBZJdc4gqoZCNvp-LEi8UAFI4BbTeqzuNgl_JCAsbJbg84zoBOqh1bAsF7G73L5Pb4psSy9Gq4SnqkFxFcR8hfhgFsnDEU)
23. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjfmtA5K5uZ-CtHeg5gxcq6dIbJ0J507FZu4Vmj8x33zYLci8UG9CfByeE75-ZTGib9PSrUQ8df76z8SgHQ6D0uMEe3A9hOT-OHb2oj7isWCMbkuBD)
24. [knime.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7CsuY0oQoF9-5PH6w8uCJ0iStr3ZolB3D30oikBgEaUoElPCSQZh1jEyUBtmRgS-JQwmcRGW5BWWOY3Ur2sMGRPvh0MDRm-vKvjDJ4Y_SslPi9xjpjG3oPpec5QEqpkE8KYYuXv9Bu2RZeuDUq-JTqAs2xg9aAyOk4Our0JbYTf2qtVeJGyzAHnKFQQ==)
25. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELgxdLflMlMAQHn19D-xvcqgmEYktYAb-rmSCI5q298rXH_N56eubOcDIq3tMF46b232p1CmV7qbhuBRT9xxCVRT115UEkGUje4xD52jWrrX9Anrtfg4SF6PsqznfBUD-l2vu0pUMTT6up1W7SPhQLq9K-oqpVjynuzAdv6HmZCbDA8-tqXzgmDxGAU8UiW1xr4qRRRhHu4FNcHU5cAW_yU73i8NLl-A7azT8jZ3obO4lcJYqV-Fe0cATYBwesVA==)
26. [auth0.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFSIsQ2zS3HJnJFqv-tcy2VqPagwtZTxwTPsYu94hXZUL5jMkKTkw1Dtt4AgHLLZBmwEqfEsEQnUT94pEQgpq_vd1BWyZRcmKG64XpeRAaf0iKD1TrlgI=)
27. [clarifai.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkpn1fqnggdrShUJqzbUbw1Ytm5UiidtYTy57QrV_xHpvS-ZjR0FDYNPkCe--r5WIlDHYlP104P3LiGvz0TLQk4Sg-FP7w7FS_yza4W0kanTBu55IWKnFJJff38Y-qRtwznKCcZPiJvS54ADpdcrY=)
28. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGd6o_J1PLhiO4E3T2ac9OhV2IpF_ybFDPTwc8J2h2ZB--eGPMbSHYkkKfurjVNOx7F8rN5T59Zvy-nsvHKvIDkJp6p0TDFvh2WMsbunfI1-RHqflSYhXo)
29. [stainless.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOYtIJpFfUxgq-nbYdnTEBZrJIqvk7IhzlDtHqAW3KoLwhEqSDH9Dn_0s-mKivvZtBYGw2bLpqPQyLS9V_6rBC3cgf-n2dcxEo6yc_RkfkrlHqlDyvhAf6N9A4dDIpam1bRcTy)
30. [microsoft.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4_UZFlDFt8P60YvztQHv6Ai465-56xB4fCPpUqdApn94FYsBeN0TzcQMb-tYkiRP8Ci5oDDk_GSKjMbeTrSzEEwRU4GW955SGb6pwsxZZhKE66Vp_dKfE_mHxEqEpxm8x447NDBQW4Srw3XKsvLo2jqE=)
31. [runonflux.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPoDsHi_V8M_iDtpjX7noFQ2ltQAHaLvP5EjA00CzFlJ3QnqJRNqIpvO7-EGhkydEQ6dmGzOPb5X_kwP3qOwpHF-pg-trKHPcKK_5qzFjxJ1e3mVLcfXkefZlL8m-HHDNj1cE4oPE8ScBiUGRiSF0O_oisCRw=)
32. [moesif.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpEz7wZj3mQ2EYScf2HbCv1d1HT2bPVvUK8WvdSCCRSIaUw3dg6BYfgipzEBs7eat3mtKPqNh_9yv1rw6OzJa_wtG_GcjWxqZ5WJ5hPWZXN6Bml3b2bOaCezn-oTzpfHgwrDCMO73CKfyOUZdXztUuCCCWUhwwSHMp1gApOnPZylzXbZH1phUVQz47_MlZXoGml7q3Xu-uBMDQ1kX-9DLA5e0=)
33. [stackoverflow.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENPp08rTKlP_XDvTrkWYKA7opfMsFcviN01ICfuu3v_BNnBi9DX74Q6kXFGfeonnaR74Zi1dByIYawoTZOUYeLDwUF_aDU8B-JQtYvImwU6yINFI938OIHzi2EynZHHAn5NpG05fljZ1N6G1K7Bm6shrAMjG-uEGT01e0H8pyx13d8Bq9y6umFx3LUL3SdY2tHj3w8yByRmAuXAPxi)
34. [appsentinels.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNUK27JrEhA1jnlyptf4vN9ANLMnovoiMLoYj3IfIkwXMfFe4Vdyv4GO6_xWi6A-B3KR30Vw_6cd370HdhA0HjkRbAZ1JuApztq2NI9Hg-v8w9h_yqF3gFBhqlVtt58pU1LX_8dTLOVfo6h9Hv_3bfrIv6C8MjMzq5JIj24g==)
35. [claude.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuBmU7oohctJvcSKqywIf37tW4W_ZFfgmlx5YzQIToCRiU9fHZyHc167hrf_1L7tM4h3xbQpAxa9kOvjTEHV6Tg3HJ8O4vZ62Fs-dTixumVV-9fTZMiKMcW7RFCuE=)
36. [delinea.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3_86ZukLSuj7PEeU7y17ssVSxFE_nUy85heO07pj4qEcozip3UnVCWwxuZO1J1HKLkh2Z-v6rHmz6bw1cq1uy-Fjyj_sS-59m2eOg6E-IPW5WDHmXHZfjWgYGqipE10VX6wrb2MJTyPURh-qco8IxM7eIpW9NNIv3JvbpZ-noeg==)


## Annotations
Annotation(end_index=402, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDsGUvEcs1s4t8y5GTW_mZ5Am84uaPNDXg6swYqu4XOJUD8De8QBbgNnZhhIrkErrJvrTflRaDGjC-q7x67IliZLh6QcblUJE3KVcb_xalnuUwq5t7AfdkklPTPsuex_C2m76hLkM1sexE5qc4nYV1O7TrDe28-p1HfQ==', start_index=390)
Annotation(end_index=402, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwKaRyFmHZnl36zD7kkwRSZvN5Uu-9VZG7hK1zv1668QaAiLJO3nst2U2QBj6D6tFLw-_36t08QR-VIebwZr5eUuu763vp02w1PuHIHeJhVhtPHakLWoM-znMAj9r_JRV_pOnvBCj4EFscRnGg3oT4EZLHr3KNEx2E3CAFaXxuP2GcwiiTjjgCNw==', start_index=390)
Annotation(end_index=763, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJ6WO17YgtOlpvLDpyMgV_68Dy8VbiEggCpxVGmdNw7LRH0nOv8eHLR2dXLdjcLcs9Yzrz8Rp-PSJTGjV2bAnYB9XAruQxTJ-7zWUCP-PDiJU8r7rQh2PAq4gS7D2iFN564DCB7eJRgqx2fHTJK7mfEYUO', start_index=748)
Annotation(end_index=763, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0sX-7r5sDzDSgmbIlSkcq0Jrp-bn08A9FkYcbRhEoqWNyrHRDBfpFkpkDEyMKpXAXHsWoBGPmepWwAAbCbYn0ESDJ31GFRquOjzsXpn8myLmVNWbpdiDDWmNw_evXjjVkNtkMzn_bVVakqKWh6Fng9nrwCkwM1yPolIBQr0QteNM6V3T5VkgA8AqYZxitmuyG99fL47SKq-rLMF-cXLYKUx-n2hvA', start_index=748)
Annotation(end_index=763, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJyTn2BYtA76Hzsqf383mqWrPTfmY0kmRuzfn-FBUmy_dRS2_MJ0wTH2-rsqejFP3lFQ74Bb2r2Pb7NO2M4fF_9Wp1oDGJn4ZdNwdSACdNBBtnnX75ap9wCcyup_JUqpW8-BAMMyxy7l_5fgmgPkBQgLdSiA==', start_index=748)
Annotation(end_index=1112, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElZY7S5XWdWll1kDteECrsVleXTw4hEs9KcRMQ59HefG1sCajmo9lr3PZYGvPMG9RlLt-SVI_JricWkMRiJ1safUT5SBjW2huJuCQQeibFX7bsUV1Rqq_7lAIPnSfZc6FV8o46nXz1moIxEp8uuPCd0RuFD692JKRY5HEH0GWNcRf1JuLJnw==', start_index=1100)
Annotation(end_index=1112, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF51qcMw60dAXtF-Hmwl4SWY37SeuPOJqiBauBnlEeuc2ry95oM01zkZcj-6w3T6ge3CvfGNL9_ZkjxlrabRkAynI_u2hGaCXz5C4UTzr9Br3rKN1dlAq64odrfMyOZsfKXcnPqfuysIhm7TEgsTyp3-X0jAFbEGw==', start_index=1100)
Annotation(end_index=1425, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEwYnBm99v3YjlysDjup2oe7Pm5ulj0Lt-Ex5Vt0L4lBbnmrTZxbyjx6-_cZloR3QKC30riu0bjMS9CEFgc8IwDunJgUv-mdgwLdxIqQ9ErVzIWPsInzEB909MLnp8XaXkaRu8o8gh2WdKtTdQlc_g9xn88UvI_XUsVaePMA==', start_index=1413)
Annotation(end_index=1425, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYrr5SjHe8TZ5Zks3QOgcO0GYAlC9JhE_I4YVlzAh9NxXzBVxDKKYLiQF9OESDJLtvILSWzq2dJLrVjZD3-Z-w9-VU1fPO6HST8pmHG54UhzHZ8ZW0wwR1OPs-XLv-rXsYWIcwNq9HHqquSds0Da-p8RfVqO5A3S5s9CV1s7Ne1oM7pLjPWkhsIq4=', start_index=1413)
Annotation(end_index=1820, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF113rkN9807LorSqcrwSQN2o-IGXsbCO5Cnx7vwB_d919ag9Kv6OzC1iZ2swU414wqLwxSg5aPueQ2oncBarddxKlJcaIhrdnylHmBqjTCrJOof0TcOme_h7kXk33CVK4p_iI=', start_index=1802)
Annotation(end_index=1820, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLHRH2AD718PQ579h1jSpJxal_X3SbGYqJJswqgTMdVDgEXUUNeA_3tZYFlSFinxUhn9-9w5byUw0PB1DyXAOw-7Xgg0PuJX6A_tO3mHUtjBJ4RWuk', start_index=1802)
Annotation(end_index=1820, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZ3oQ9F_aX1hvGB1aHrq0RntMNsrOGMIcoU7_1sKdhtsBixQe7zyAdOdBdxP9gVrbq3aa03nzCXDY7PZXV4ULpjpLk084cwx5Si0h65Vy_nsNWqGSu', start_index=1802)
Annotation(end_index=2515, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdiI_bsIOWQ5LKnoOsMWFHyjCTNx8lLXPOW8neQd561kiE-GBwuG-reBfR6SkierKLmBPHXLRhULgG_cGTNAsxornmXhd2VmBCyRQhlrQLsEelwpLEz9b3ms-V9yNx9QyR3f4U9g==', start_index=2505)
Annotation(end_index=3851, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwKaRyFmHZnl36zD7kkwRSZvN5Uu-9VZG7hK1zv1668QaAiLJO3nst2U2QBj6D6tFLw-_36t08QR-VIebwZr5eUuu763vp02w1PuHIHeJhVhtPHakLWoM-znMAj9r_JRV_pOnvBCj4EFscRnGg3oT4EZLHr3KNEx2E3CAFaXxuP2GcwiiTjjgCNw==', start_index=3842)
Annotation(end_index=4229, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwKaRyFmHZnl36zD7kkwRSZvN5Uu-9VZG7hK1zv1668QaAiLJO3nst2U2QBj6D6tFLw-_36t08QR-VIebwZr5eUuu763vp02w1PuHIHeJhVhtPHakLWoM-znMAj9r_JRV_pOnvBCj4EFscRnGg3oT4EZLHr3KNEx2E3CAFaXxuP2GcwiiTjjgCNw==', start_index=4220)
Annotation(end_index=4527, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDsGUvEcs1s4t8y5GTW_mZ5Am84uaPNDXg6swYqu4XOJUD8De8QBbgNnZhhIrkErrJvrTflRaDGjC-q7x67IliZLh6QcblUJE3KVcb_xalnuUwq5t7AfdkklPTPsuex_C2m76hLkM1sexE5qc4nYV1O7TrDe28-p1HfQ==', start_index=4518)
Annotation(end_index=4700, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDsGUvEcs1s4t8y5GTW_mZ5Am84uaPNDXg6swYqu4XOJUD8De8QBbgNnZhhIrkErrJvrTflRaDGjC-q7x67IliZLh6QcblUJE3KVcb_xalnuUwq5t7AfdkklPTPsuex_C2m76hLkM1sexE5qc4nYV1O7TrDe28-p1HfQ==', start_index=4691)
Annotation(end_index=5272, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJ6WO17YgtOlpvLDpyMgV_68Dy8VbiEggCpxVGmdNw7LRH0nOv8eHLR2dXLdjcLcs9Yzrz8Rp-PSJTGjV2bAnYB9XAruQxTJ-7zWUCP-PDiJU8r7rQh2PAq4gS7D2iFN564DCB7eJRgqx2fHTJK7mfEYUO', start_index=5260)
Annotation(end_index=5272, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHJyTn2BYtA76Hzsqf383mqWrPTfmY0kmRuzfn-FBUmy_dRS2_MJ0wTH2-rsqejFP3lFQ74Bb2r2Pb7NO2M4fF_9Wp1oDGJn4ZdNwdSACdNBBtnnX75ap9wCcyup_JUqpW8-BAMMyxy7l_5fgmgPkBQgLdSiA==', start_index=5260)
Annotation(end_index=5418, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJ6WO17YgtOlpvLDpyMgV_68Dy8VbiEggCpxVGmdNw7LRH0nOv8eHLR2dXLdjcLcs9Yzrz8Rp-PSJTGjV2bAnYB9XAruQxTJ-7zWUCP-PDiJU8r7rQh2PAq4gS7D2iFN564DCB7eJRgqx2fHTJK7mfEYUO', start_index=5409)
Annotation(end_index=5728, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0sX-7r5sDzDSgmbIlSkcq0Jrp-bn08A9FkYcbRhEoqWNyrHRDBfpFkpkDEyMKpXAXHsWoBGPmepWwAAbCbYn0ESDJ31GFRquOjzsXpn8myLmVNWbpdiDDWmNw_evXjjVkNtkMzn_bVVakqKWh6Fng9nrwCkwM1yPolIBQr0QteNM6V3T5VkgA8AqYZxitmuyG99fL47SKq-rLMF-cXLYKUx-n2hvA', start_index=5719)
Annotation(end_index=5929, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJ6WO17YgtOlpvLDpyMgV_68Dy8VbiEggCpxVGmdNw7LRH0nOv8eHLR2dXLdjcLcs9Yzrz8Rp-PSJTGjV2bAnYB9XAruQxTJ-7zWUCP-PDiJU8r7rQh2PAq4gS7D2iFN564DCB7eJRgqx2fHTJK7mfEYUO', start_index=5917)
Annotation(end_index=5929, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH0sX-7r5sDzDSgmbIlSkcq0Jrp-bn08A9FkYcbRhEoqWNyrHRDBfpFkpkDEyMKpXAXHsWoBGPmepWwAAbCbYn0ESDJ31GFRquOjzsXpn8myLmVNWbpdiDDWmNw_evXjjVkNtkMzn_bVVakqKWh6Fng9nrwCkwM1yPolIBQr0QteNM6V3T5VkgA8AqYZxitmuyG99fL47SKq-rLMF-cXLYKUx-n2hvA', start_index=5917)
Annotation(end_index=6330, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJ6WO17YgtOlpvLDpyMgV_68Dy8VbiEggCpxVGmdNw7LRH0nOv8eHLR2dXLdjcLcs9Yzrz8Rp-PSJTGjV2bAnYB9XAruQxTJ-7zWUCP-PDiJU8r7rQh2PAq4gS7D2iFN564DCB7eJRgqx2fHTJK7mfEYUO', start_index=6321)
Annotation(end_index=6666, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF-V1YYSP6vISLI0ZU6oMBBpNrGuXZubg9BsLJIJrBWZTC0W6wTfAGftE3r5u9cHdSLJHyo-jFWCNDniZiu-YjP-IZ-jTFGfpLBOBoPrrEpGKijdnQYKh2VUS9ZvQnySvuOHthv6wB2cDmUrQtwlT7k7_7YdQ6XZWJi9kn140Gdn63OnI8nWgSdfiQ-ndV3aD8OrF-Vz-S-qdPXblMI57WG5sWE7F5VLirNwLpApBjt56AWvJdK-QSJ9FQ9tSL_pA==', start_index=6656)
Annotation(end_index=7090, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXCI_KobmuawINLdffbcBKRKw3fL7nnjoUAjm3jhtzy_1uFbfFnbA7onS3UXdqLmL_O1BsS6fNmO2E54r4tlm841TZqJPX9Oxd-UyxEX5FnVSRZ35yf-ffdacEMudDdudgQqvF9f6mkQqkYnhfjIOZ98Btjw==', start_index=7080)
Annotation(end_index=7444, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXCI_KobmuawINLdffbcBKRKw3fL7nnjoUAjm3jhtzy_1uFbfFnbA7onS3UXdqLmL_O1BsS6fNmO2E54r4tlm841TZqJPX9Oxd-UyxEX5FnVSRZ35yf-ffdacEMudDdudgQqvF9f6mkQqkYnhfjIOZ98Btjw==', start_index=7430)
Annotation(end_index=7444, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMdcrZKkgKAnHwqzk2JGaefd5VieRZfbqk5OZN6elJgHxoMZ3RAgw-Y7W2fsI3nIPcdyIvesao-XnNVvrcrRyp0HGzv1LvdJzx7lwkak02GNnslg2m7CTpnsovxzKLbGsyMH0ODwBtyzLiWwLgMULJYHbdgmp0d8RkObAQqw==', start_index=7430)
Annotation(end_index=7695, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGXCI_KobmuawINLdffbcBKRKw3fL7nnjoUAjm3jhtzy_1uFbfFnbA7onS3UXdqLmL_O1BsS6fNmO2E54r4tlm841TZqJPX9Oxd-UyxEX5FnVSRZ35yf-ffdacEMudDdudgQqvF9f6mkQqkYnhfjIOZ98Btjw==', start_index=7685)
Annotation(end_index=8299, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElZY7S5XWdWll1kDteECrsVleXTw4hEs9KcRMQ59HefG1sCajmo9lr3PZYGvPMG9RlLt-SVI_JricWkMRiJ1safUT5SBjW2huJuCQQeibFX7bsUV1Rqq_7lAIPnSfZc6FV8o46nXz1moIxEp8uuPCd0RuFD692JKRY5HEH0GWNcRf1JuLJnw==', start_index=8287)
Annotation(end_index=8299, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF51qcMw60dAXtF-Hmwl4SWY37SeuPOJqiBauBnlEeuc2ry95oM01zkZcj-6w3T6ge3CvfGNL9_ZkjxlrabRkAynI_u2hGaCXz5C4UTzr9Br3rKN1dlAq64odrfMyOZsfKXcnPqfuysIhm7TEgsTyp3-X0jAFbEGw==', start_index=8287)
Annotation(end_index=8694, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEqENqZjUgnBcJ781NUHyZ3sGn1RolMIy1yDg_pr8RQYKWONQ4e-Ocd4VTU69GbHlfiSLp76qE1hO502Hin9MRVZJnUL-wsptWpZRFV4aScJj8byyEOvOMvM3u-iRvuOpUnQg30UkaZXu7aGf7H_92', start_index=8684)
Annotation(end_index=9068, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGw7AFb3SoEqoDnZ8DM4L_24Uggh4O4eZvUA2ju-tDLOTgjQNzIK79JXtbm0paK8HDSeJ9dXrLeevtr8lr7azu46tWiwIlzxjZW1MulUt9yUKJQ35xseYXyTJU_N2ImIvLScOXNHJ1raYzHF2B7q6uPBD9n5l0Q0l4jp5Q=', start_index=9058)
Annotation(end_index=9310, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFSu5e9QpDGagg3thA89VKI6akZTD6scMSxurHctzNFZwLI5aMWaumigFkejUprB1HX-G3e8y6-21EjrFSOgD5YD5aERr5DD4LuBbOzZAKYebD_HUIShHvmS4V61f0pKNWng5ncRTu2wrdKnOX7rLVU6K8V8QTOAPORngU=', start_index=9300)
Annotation(end_index=9632, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQElZY7S5XWdWll1kDteECrsVleXTw4hEs9KcRMQ59HefG1sCajmo9lr3PZYGvPMG9RlLt-SVI_JricWkMRiJ1safUT5SBjW2huJuCQQeibFX7bsUV1Rqq_7lAIPnSfZc6FV8o46nXz1moIxEp8uuPCd0RuFD692JKRY5HEH0GWNcRf1JuLJnw==', start_index=9623)
Annotation(end_index=10052, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEwYnBm99v3YjlysDjup2oe7Pm5ulj0Lt-Ex5Vt0L4lBbnmrTZxbyjx6-_cZloR3QKC30riu0bjMS9CEFgc8IwDunJgUv-mdgwLdxIqQ9ErVzIWPsInzEB909MLnp8XaXkaRu8o8gh2WdKtTdQlc_g9xn88UvI_XUsVaePMA==', start_index=10043)
Annotation(end_index=10233, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYrr5SjHe8TZ5Zks3QOgcO0GYAlC9JhE_I4YVlzAh9NxXzBVxDKKYLiQF9OESDJLtvILSWzq2dJLrVjZD3-Z-w9-VU1fPO6HST8pmHG54UhzHZ8ZW0wwR1OPs-XLv-rXsYWIcwNq9HHqquSds0Da-p8RfVqO5A3S5s9CV1s7Ne1oM7pLjPWkhsIq4=', start_index=10224)
Annotation(end_index=10548, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHMdcrZKkgKAnHwqzk2JGaefd5VieRZfbqk5OZN6elJgHxoMZ3RAgw-Y7W2fsI3nIPcdyIvesao-XnNVvrcrRyp0HGzv1LvdJzx7lwkak02GNnslg2m7CTpnsovxzKLbGsyMH0ODwBtyzLiWwLgMULJYHbdgmp0d8RkObAQqw==', start_index=10538)
Annotation(end_index=11584, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErypVhDDyEt-LLCL5Vc02oe-l479tP7EhopKXhfNLfWsIt3Cfw7Mi3deOgqX3umOS-Kj0J0EOw2KHU6Y9eSFjsEHPQ6BlC8hOujvDbojJ8l8buDWLmPhNV08KIMb-QtbKa_ym5JRs=', start_index=11570)
Annotation(end_index=11584, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLHRH2AD718PQ579h1jSpJxal_X3SbGYqJJswqgTMdVDgEXUUNeA_3tZYFlSFinxUhn9-9w5byUw0PB1DyXAOw-7Xgg0PuJX6A_tO3mHUtjBJ4RWuk', start_index=11570)
Annotation(end_index=11829, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwhN2ppUghjW8N7EmNYP_OfvjBZJdc4gqoZCNvp-LEi8UAFI4BbTeqzuNgl_JCAsbJbg84zoBOqh1bAsF7G73L5Pb4psSy9Gq4SnqkFxFcR8hfhgFsnDEU', start_index=11815)
Annotation(end_index=11829, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFx1_HxlHcwEaxb3ERz94UGRyKL3ArfGwb4DUE-5N3MYl-Id5LwYFpBnuQ1YYeVbrH-6NoVRHobvQVyYRYa5YRj7xgaKmyl2aS2qMdectF8EjRvsyTAd2n7oxsPXvGspVTTq3rVHSDU_Xc89oLgOBLaa7AGQ0xntpHRMFDyaLWrXWcpY8S1C_y4ot12', start_index=11815)
Annotation(end_index=12132, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjfmtA5K5uZ-CtHeg5gxcq6dIbJ0J507FZu4Vmj8x33zYLci8UG9CfByeE75-ZTGib9PSrUQ8df76z8SgHQ6D0uMEe3A9hOT-OHb2oj7isWCMbkuBD', start_index=12122)
Annotation(end_index=12546, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7CsuY0oQoF9-5PH6w8uCJ0iStr3ZolB3D30oikBgEaUoElPCSQZh1jEyUBtmRgS-JQwmcRGW5BWWOY3Ur2sMGRPvh0MDRm-vKvjDJ4Y_SslPi9xjpjG3oPpec5QEqpkE8KYYuXv9Bu2RZeuDUq-JTqAs2xg9aAyOk4Our0JbYTf2qtVeJGyzAHnKFQQ==', start_index=12536)
Annotation(end_index=12877, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQELgxdLflMlMAQHn19D-xvcqgmEYktYAb-rmSCI5q298rXH_N56eubOcDIq3tMF46b232p1CmV7qbhuBRT9xxCVRT115UEkGUje4xD52jWrrX9Anrtfg4SF6PsqznfBUD-l2vu0pUMTT6up1W7SPhQLq9K-oqpVjynuzAdv6HmZCbDA8-tqXzgmDxGAU8UiW1xr4qRRRhHu4FNcHU5cAW_yU73i8NLl-A7azT8jZ3obO4lcJYqV-Fe0cATYBwesVA==', start_index=12867)
Annotation(end_index=13068, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkpn1fqnggdrShUJqzbUbw1Ytm5UiidtYTy57QrV_xHpvS-ZjR0FDYNPkCe--r5WIlDHYlP104P3LiGvz0TLQk4Sg-FP7w7FS_yza4W0kanTBu55IWKnFJJff38Y-qRtwznKCcZPiJvS54ADpdcrY=', start_index=13054)
Annotation(end_index=13068, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFSIsQ2zS3HJnJFqv-tcy2VqPagwtZTxwTPsYu94hXZUL5jMkKTkw1Dtt4AgHLLZBmwEqfEsEQnUT94pEQgpq_vd1BWyZRcmKG64XpeRAaf0iKD1TrlgI=', start_index=13054)
Annotation(end_index=13284, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFGd6o_J1PLhiO4E3T2ac9OhV2IpF_ybFDPTwc8J2h2ZB--eGPMbSHYkkKfurjVNOx7F8rN5T59Zvy-nsvHKvIDkJp6p0TDFvh2WMsbunfI1-RHqflSYhXo', start_index=13270)
Annotation(end_index=13284, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFSIsQ2zS3HJnJFqv-tcy2VqPagwtZTxwTPsYu94hXZUL5jMkKTkw1Dtt4AgHLLZBmwEqfEsEQnUT94pEQgpq_vd1BWyZRcmKG64XpeRAaf0iKD1TrlgI=', start_index=13270)
Annotation(end_index=13591, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFSIsQ2zS3HJnJFqv-tcy2VqPagwtZTxwTPsYu94hXZUL5jMkKTkw1Dtt4AgHLLZBmwEqfEsEQnUT94pEQgpq_vd1BWyZRcmKG64XpeRAaf0iKD1TrlgI=', start_index=13581)
Annotation(end_index=13836, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOYtIJpFfUxgq-nbYdnTEBZrJIqvk7IhzlDtHqAW3KoLwhEqSDH9Dn_0s-mKivvZtBYGw2bLpqPQyLS9V_6rBC3cgf-n2dcxEo6yc_RkfkrlHqlDyvhAf6N9A4dDIpam1bRcTy', start_index=13826)
Annotation(end_index=14178, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkpn1fqnggdrShUJqzbUbw1Ytm5UiidtYTy57QrV_xHpvS-ZjR0FDYNPkCe--r5WIlDHYlP104P3LiGvz0TLQk4Sg-FP7w7FS_yza4W0kanTBu55IWKnFJJff38Y-qRtwznKCcZPiJvS54ADpdcrY=', start_index=14168)
Annotation(end_index=14385, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkpn1fqnggdrShUJqzbUbw1Ytm5UiidtYTy57QrV_xHpvS-ZjR0FDYNPkCe--r5WIlDHYlP104P3LiGvz0TLQk4Sg-FP7w7FS_yza4W0kanTBu55IWKnFJJff38Y-qRtwznKCcZPiJvS54ADpdcrY=', start_index=14375)
Annotation(end_index=15092, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEEwYnBm99v3YjlysDjup2oe7Pm5ulj0Lt-Ex5Vt0L4lBbnmrTZxbyjx6-_cZloR3QKC30riu0bjMS9CEFgc8IwDunJgUv-mdgwLdxIqQ9ErVzIWPsInzEB909MLnp8XaXkaRu8o8gh2WdKtTdQlc_g9xn88UvI_XUsVaePMA==', start_index=15083)
Annotation(end_index=15375, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4_UZFlDFt8P60YvztQHv6Ai465-56xB4fCPpUqdApn94FYsBeN0TzcQMb-tYkiRP8Ci5oDDk_GSKjMbeTrSzEEwRU4GW955SGb6pwsxZZhKE66Vp_dKfE_mHxEqEpxm8x447NDBQW4Srw3XKsvLo2jqE=', start_index=15365)
Annotation(end_index=15957, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGPoDsHi_V8M_iDtpjX7noFQ2ltQAHaLvP5EjA00CzFlJ3QnqJRNqIpvO7-EGhkydEQ6dmGzOPb5X_kwP3qOwpHF-pg-trKHPcKK_5qzFjxJ1e3mVLcfXkefZlL8m-HHDNj1cE4oPE8ScBiUGRiSF0O_oisCRw=', start_index=15947)
Annotation(end_index=16448, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpEz7wZj3mQ2EYScf2HbCv1d1HT2bPVvUK8WvdSCCRSIaUw3dg6BYfgipzEBs7eat3mtKPqNh_9yv1rw6OzJa_wtG_GcjWxqZ5WJ5hPWZXN6Bml3b2bOaCezn-oTzpfHgwrDCMO73CKfyOUZdXztUuCCCWUhwwSHMp1gApOnPZylzXbZH1phUVQz47_MlZXoGml7q3Xu-uBMDQ1kX-9DLA5e0=', start_index=16438)
Annotation(end_index=16741, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQENPp08rTKlP_XDvTrkWYKA7opfMsFcviN01ICfuu3v_BNnBi9DX74Q6kXFGfeonnaR74Zi1dByIYawoTZOUYeLDwUF_aDU8B-JQtYvImwU6yINFI938OIHzi2EynZHHAn5NpG05fljZ1N6G1K7Bm6shrAMjG-uEGT01e0H8pyx13d8Bq9y6umFx3LUL3SdY2tHj3w8yByRmAuXAPxi', start_index=16731)
Annotation(end_index=17204, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF4_UZFlDFt8P60YvztQHv6Ai465-56xB4fCPpUqdApn94FYsBeN0TzcQMb-tYkiRP8Ci5oDDk_GSKjMbeTrSzEEwRU4GW955SGb6pwsxZZhKE66Vp_dKfE_mHxEqEpxm8x447NDBQW4Srw3XKsvLo2jqE=', start_index=17190)
Annotation(end_index=17204, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdiI_bsIOWQ5LKnoOsMWFHyjCTNx8lLXPOW8neQd561kiE-GBwuG-reBfR6SkierKLmBPHXLRhULgG_cGTNAsxornmXhd2VmBCyRQhlrQLsEelwpLEz9b3ms-V9yNx9QyR3f4U9g==', start_index=17190)
Annotation(end_index=17430, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNUK27JrEhA1jnlyptf4vN9ANLMnovoiMLoYj3IfIkwXMfFe4Vdyv4GO6_xWi6A-B3KR30Vw_6cd370HdhA0HjkRbAZ1JuApztq2NI9Hg-v8w9h_yqF3gFBhqlVtt58pU1LX_8dTLOVfo6h9Hv_3bfrIv6C8MjMzq5JIj24g==', start_index=17420)
Annotation(end_index=17751, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuBmU7oohctJvcSKqywIf37tW4W_ZFfgmlx5YzQIToCRiU9fHZyHc167hrf_1L7tM4h3xbQpAxa9kOvjTEHV6Tg3HJ8O4vZ62Fs-dTixumVV-9fTZMiKMcW7RFCuE=', start_index=17741)
Annotation(end_index=18132, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNUK27JrEhA1jnlyptf4vN9ANLMnovoiMLoYj3IfIkwXMfFe4Vdyv4GO6_xWi6A-B3KR30Vw_6cd370HdhA0HjkRbAZ1JuApztq2NI9Hg-v8w9h_yqF3gFBhqlVtt58pU1LX_8dTLOVfo6h9Hv_3bfrIv6C8MjMzq5JIj24g==', start_index=18122)
Annotation(end_index=18400, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdiI_bsIOWQ5LKnoOsMWFHyjCTNx8lLXPOW8neQd561kiE-GBwuG-reBfR6SkierKLmBPHXLRhULgG_cGTNAsxornmXhd2VmBCyRQhlrQLsEelwpLEz9b3ms-V9yNx9QyR3f4U9g==', start_index=18390)
Annotation(end_index=18896, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF3_86ZukLSuj7PEeU7y17ssVSxFE_nUy85heO07pj4qEcozip3UnVCWwxuZO1J1HKLkh2Z-v6rHmz6bw1cq1uy-Fjyj_sS-59m2eOg6E-IPW5WDHmXHZfjWgYGqipE10VX6wrb2MJTyPURh-qco8IxM7eIpW9NNIv3JvbpZ-noeg==', start_index=18886)
Annotation(end_index=19178, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNUK27JrEhA1jnlyptf4vN9ANLMnovoiMLoYj3IfIkwXMfFe4Vdyv4GO6_xWi6A-B3KR30Vw_6cd370HdhA0HjkRbAZ1JuApztq2NI9Hg-v8w9h_yqF3gFBhqlVtt58pU1LX_8dTLOVfo6h9Hv_3bfrIv6C8MjMzq5JIj24g==', start_index=19168)

## Sources
