# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** db678c4f | **Time:** 16.93s | **Cost:** $0.02340
--------------------------------------------------------------------------------

PBFT-style BFT can give a financial ledger both **partition tolerance** and **deterministic finality**, but only inside a *small* validator set.  
The moment the set grows to the size public DeFi chains want (hundreds or thousands of nodes) the **view-change** path becomes the bottleneck: it lifts communication from O(n²) to O(n³) and, more importantly, makes the *worst-case* message load of the whole protocol scale with n³.  
That is usually judged “too expensive” for open financial networks, so production systems do not rely on “naked” PBFT; instead they:

1. Keep the *idea* of PBFT (three-phase vote, 2f+1 quorum, view change) but replace the all-to-all gossip with **threshold-signature aggregation** (HotStuff, Tendermint, Casper FFG, Solana Tower).  
   - One multicast carries the whole quorum certificate, so view change drops back to O(n) messages.  
2. Shrink the *active* set to a **committee** (≤ 130–400 validators) that rotates every epoch.  
   - Partition tolerance is now “committee-level”: if the *current* committee is split, progress stalls, but safety is still guaranteed because the *next* committee cannot be formed without a super-majority of the *previous* one.  
3. Accept **eventual synchrony** instead of full asynchrony.  
   - Liveness is lost while the network is partitioned, yet no money can be double-spent (safety), which is the property traders care about.

Hence the trade-off is not “PBFT view change vs. partition tolerance” but:

- **Small committee** → linear view change, seconds-long finality, survives partitions once synchrony returns.  
- **Large committee** → quadratic/cubic view change, congested links, dropped messages, missed slots, and angry validators.

Financial blockchains today pick the first option and compensate the residual centralisation with:

- Proof-of-stake + slashing to make Sybil attacks expensive;  
- Fast epoch rotation so a partitioned minority loses its stake quickly;  
- Light-client bridges and zk-proofs that let users verify finality without seeing every signature.

So the literal PBFT view-change mechanism *does* make the protocol unusable at scale, but the **family** of PBFT-derived algorithms (HotStuff, Tendermint, Streamlet, Casper, GRANDPA, etc.) already solved that problem by cutting the view-change message cost to O(n) and bounding the validator set.  In short: you can have both partition tolerance and finality in a BFT ledger, but only if you stop short of running PBFT “as-is” and adopt one of the modern threshold-signature variants.

## Annotations


## Sources
