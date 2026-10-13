# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** aff34747 | **Time:** 11.69s | **Cost:** $0.02053
--------------------------------------------------------------------------------

In SDN the logically-centralised controller keeps the “global” view, but the data-plane devices must still act on that view.  
The mechanism that lets the controller push its decisions out to the network fast enough to meet latency budgets is **pro-active, flow-granular rule caching combined with an incremental, event-driven south-bound protocol** (OpenFlow, P4-runtime, gRPC, …).

- The controller pre-computes and **caches the next forwarding rules** (often several equivalent paths) in the switches’ flow tables before they are actually needed.  
- When a link-event or QoS threshold is crossed the controller does **not recompute the whole network**: it only **updates the affected entries** (incremental install/modify/delete) and uses **packet-in/packet-out** messages only for the first few packets of a new micro-flow.  
- Because the heavy computation is done centrally and the switch already holds the answer, the data-plane reacts in a few RTTs – giving the **best of both worlds**: global optimisation with local, low-latency execution.

Hence the balancing mechanism is **predictive / proactive flow-rule caching plus incremental, event-driven south-bound updates**.

## Annotations


## Sources
