# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 3f751a1c | **Time:** 11.56s | **Cost:** $0.00827
--------------------------------------------------------------------------------

Network-flow models can certainly *balance* accuracy and complexity, but only if you stop treating the graph as a faithful miniature of the order book.  
Once you let “centrality” become a free parameter that is tuned to *explain* past price impact, the weights act like leverage on the illusion: they magnify whatever segment of the network was active in the calibration window and project it onto the whole future topology.  
In segmented markets this is lethal, because the same centrality score can be generated either by a genuinely global hub or by a locally dense clique that has almost no egress capacity to the rest of the graph. The algorithm cannot tell the difference unless you give it (i) explicit capacity constraints that are *not* estimated from the same trades you are trying to predict and (ii) a penalty for topological over-fitting. Without those two guard-rails the “accuracy” you see in-sample is mostly the model memorising the idiosyncratic liquidity sinks of the last crisis, not a robust forecast of where the next one will appear.

So the short answer is:  
- Network flows *can* stay honest, but you have to throw away the idea that a single eigenvector or PageRank weight vector is a sufficient statistic for liquidity.  
- Centrality weights *will* exaggerate liquidity illusions whenever the market is segmented, unless you regularise them with exogenous settlement-capacity data and cross-validate on a topology that is *not* the one you used to calibrate the weights.

## Annotations


## Sources
