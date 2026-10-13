# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 130d224c | **Time:** 22.33s | **Cost:** $0.02724
--------------------------------------------------------------------------------

Proof-of-Work can be made *leaner*, but it cannot be made *flat*—and that asymmetry is what pushes large, integrated miners to the top.  
The same economic force that gives PoW its security (the right to vote is bought with real, irreversible work) also rewards the actor that can deliver the most hash per dollar. Once an application-specific integrated circuit exists, every further dollar of mining budget buys *more* hash if it is spent on that ASIC rather than on CPUs, GPUs, or even electricity. The equilibrium is therefore a small set of farms that (a) own the latest ASIC generation, (b) negotiate industrial power prices, and (c) self-replicate by reinvesting the coinbase. Far from being an accident, this concentration is the predictable market outcome of the security model itself.

Because security is *linear in work* but energy cost is *sub-linear in scale*, the network keeps getting *more* secure per joule as it centralises. The paradox is that the *absolute* cost of a 51 % attack rises (you now need a bigger factory, not just more PCs) while the *number of independent parties* that must collude falls. In other words, the *economic* attack barrier goes up, but the *political* barrier goes down. Once three or four pool operators collectively command > 51 % of the hash, the attack becomes a matter of *coordination*, not expenditure. History shows that such coordination is not hypothetical: mining pools have repeatedly exceeded the threshold (BTC.com + AntPool + ViaBTC in 2014; F2Pool + Poolin + AntPool in 2021). Each time the community appealed to *social* rather than *protocol* resistance—threatening to blacklist the attack chain or change the PoW function. That appeal only works because the real-world identity of the pools is known; if hashrate were fully controlled by a single vertically-integrated chip manufacturer, even that social layer would erode.

Can “green” tweaks break the link? Proposals such as Green-PoW (elect a small committee to mine the next block) or PoTS (team-sprint lottery) cut energy by 30–50 %, but they do so by *reducing the number of simultaneous miners*—i.e. by *institutionalising* the centralisation that ASICs create organically. The security proof still holds only if the committee is *replaceable*, but replacement requires *permissionless entry*, which in turn requires that the *cost* of entry is not dominated by ASIC ownership. Once the winning ticket is an ASIC, the same economies of scale re-assert themselves inside the committee.

Hence the trade-off is structural, not parametric:

- If you keep PoW *strict* (any hash can win), ASICs appear and hashrate centralises; a 51 % attack becomes *plausible* though *expensive*.  
- If you soften PoW to save energy (committees, memory-hard puzzles, recycled work), you *accelerate* the centralisation you were trying to avoid, because the *barrier to entry* is now a *credential* (being elected, owning a stake, having the right chip) rather than a *marginal watt*.  

The only stable way to *balance* energy use and security is to *combine* PoW with a second, *orthogonal* scarce resource that is *not* ASIC-hash. That is exactly what hybrid PoW/PoS chains (e.g. Decred, Nervos) do: PoW orders blocks, PoS finalises them. An attacker needs *both* 51 % of the hash *and* 51 % of the stake, so eliminating either the ASIC farms or the whale stakers alone is insufficient. The energy bill falls (finality is stake-voted, not hash-extended) while the *pairwise* centralisation required for a successful attack remains improbably large.

Bottom line: pure PoW can *tune* energy downward only by *institutionalising* the very centralisation that threatens it; the security-efficiency dilemma is only escaped by layering PoW with a *different* Sybil-resistance mechanism that is not dominated by ASIC scale.

## Annotations


## Sources
