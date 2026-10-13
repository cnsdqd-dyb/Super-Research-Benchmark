# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 54ccecf2 | **Time:** 17.84s | **Cost:** $0.02248
--------------------------------------------------------------------------------

The service-degradation strategy that is executed when the scheduler sees a peak-load condition is not chosen by a single magic knob; it is the outcome of a short, fully-automated “mini-planning” cycle that runs every few seconds (or milliseconds) inside the traffic-management layer.  
That cycle weighs five real-time inputs and produces an ordered list of “what to throttle / what to keep.”  
The inputs, in order of importance, are:

1. Request-criticality score (business policy)  
   – Derived from the URI, API-key, user tier, tenant SLA, revenue attribution, etc.  
   – Expressed as a 3- or 5-class enum (CRITICAL > BUSINESS > BEST-EFFORT) that is already attached to the request by the API-gateway.

2. Current resource pressure vector (system health)  
   – CPU utilisation, memory head-room, queue depth, 95th-percentile latency, error rate, downstream circuit-breaker state.  
   – When any dimension crosses its configured “yellow” or “red” threshold the scheduler switches to the next stricter degradation profile.

3. Capacity forecast (temporal model)  
   – 1–5-minute-ahead prediction produced by the autoscaler or the LSTM/ARIMA model that drives it.  
   – If the forecast says “overload will last < 2 min” the scheduler prefers back-pressure (queuing) over hard drops; if it says “> 10 min” it moves immediately to load-shedding.

4. Fair-usage quota state (tenant/edge dimension)  
   – Token-bucket or sliding-window counters per IP, user, API-key, device-class, geography.  
   – Requests whose bucket is already > 80 % consumed are first candidates for throttling, independent of their class.

5. Cost-of-degradation metric (optimization layer)  
   – A dollar value per request type computed offline (lost sale, support ticket, SLA penalty, compute cost).  
   – The scheduler sorts the drop-candidates so that the “cheapest” ones are discarded first, keeping the total expected cost minimal for a given capacity budget.

These five inputs are combined into a single numeric “priority rank” for every waiting request.  
The scheduler then admits requests in rank order until the projected utilisation of the bottleneck resource reaches a safe target (e.g. 80 % CPU or 70 % queue depth). Everything left is either delayed (back-pressure) or rejected (load-shed) with HTTP 429/503 and appropriate Retry-After headers.

Because the weights and thresholds are declared in policy (not hard-coded), operations can change the degradation strategy in real time—e.g., raise the business-class weight during checkout season or lower it during a DDoS—without touching the code.

## Annotations


## Sources
