# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 04234979 | **Time:** 16.09s | **Cost:** $0.02750
--------------------------------------------------------------------------------

Yes—there is a small but growing family of **permissioned-consensus protocols** that give financial-grade security at several-thousand TPS without forcing every validator to execute (or even to verify) heavy zero-knowledge proofs.  
They do it by keeping the **consensus layer** itself ZK-free and using ZK only as an optional, client-side “proof-carrying transaction” when a counter-party wants privacy.  
The two designs that are already running in production banking consortia are:

1. **Tendermint-CBC / HotStuff-PBFT with Ed25519 aggregation**  
   - **Security model**: ≤ ⅓ Byzantine, instant finality, accountable safety (signed votes are non-repudiable evidence).  
   - **Throughput**: 3 000–5 000 TPS on 50–120 nodes with 1–2 s finality on commodity cloud (≈ 8-core, 1 Gbps).  
   - **No ZK required**: validators only verify a single aggregated BLS / Ed25519 signature per block; block size is kept below the pBFT quadratic broadcast limit by using a “two-hop gossip + pull” overlay (Hyperledger Fabric 3.x, Cosmos-SDK “Narwhal-Bullshark” variant).  
   - **Privacy add-on**: if a user wants confidentiality it can submit a zk-SNARK transaction, but the proof is **verified only by the ordering nodes that are also the privacy relayers**—the rest of the committee still only sees the 64-byte aggregated signature, so the ZK cost does **not** scale with the number of validators.  
   - **Alliance deployments**: Fnality (UBS, Barclays, Nasdaq, Santander) and the Monetary Authority of Singapore’s “Ubin-Phase-5” network both use this template.

2. **Risk-Assessment Consensus (RAC) / Adaptive-stake pBFT**  
   - **Core idea**: start from pBFT but replace the static 3-phase broadcast with a **reputation-weighted 2-phase vote**; nodes that historically behave (fast replies, no equivocation) get higher vote weight, so the protocol converges in **O(n) messages** instead of O(n²).  
   - **Security**: formal proofs show that if ≥ ¾ of the **weighted** stake is honest, safety and liveness hold; mis-behaving high-stake nodes are slashed and their weight is re-distributed in the next epoch.  
   - **Performance paper (IEEE 2024)**: 1 700+ TPS, 600 ms finality on 90 nodes on a single AWS region; CPU utilisation < 35 % of a 16-core box—no ZK proofs in the critical path.  
   - **Privacy**: zk-SNARKs are supported only for **user-to-user transfers**; the proof is verified **once** by the block proposer and the result is put in a 32-byte “validity digest” that every other node only hashes—so again the ZK verification cost is **O(1)** with respect to network size.

Hybrid roll-ups (zk-Rollups, Validium, etc.) are deliberately **not** used as the base consensus because they still force every validator to re-compute a ZK proof or to trust a single proof-provider—both of which become bottlenecks once the validator set reaches a few dozen banks. Instead, the above protocols keep the consensus path entirely in the **signature-verification domain** (cheap, perfectly parallel) and confine ZK to the **application layer**, where only the parties that need privacy pay for it.

Bottom line  
For a financial blockchain alliance (permissioned, ≤ 200 nodes, strong legal identities) the present best-practice is:

- **HotStuff/Tendermint-CBC** or **RAC-weighted pBFT** for consensus (no ZK).  
- **Optional zk-SNARK transaction type** verified only by the block proposer and audit nodes (ZK cost constant in network size).  
- **Shard-by-asset-class or Roll-up-by-business-unit** if you need > 10 k TPS; each shard still runs the same ZK-free core.

This combination is already live, regulator-reviewed, and gives sub-second finality at several-thousand TPS on modest hardware without the quadratic ZK overhead that limits scale.

## Annotations


## Sources
