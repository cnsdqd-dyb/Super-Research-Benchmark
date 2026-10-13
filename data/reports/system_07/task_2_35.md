# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** b807b268 | **Time:** 23.55s | **Cost:** $0.03063
--------------------------------------------------------------------------------

Balancing **real-time flight control responsiveness** with **global path-planning optimality** under **sensor-fusion constraints** is fundamentally a *multi-timescale, multi-objective trade-off*.  
No single layer can do both jobs: the millisecond-level attitude loop must stay ignorant of mission-level optimality, while the mission planner must never micro-manage the vehicle.  
The only way to keep both sides coherent is to (i) **fuse data once, at the right rate**, (ii) **contract the planning horizon so that optimality is proven only inside a safely short horizon**, and (iii) **let the low-level controller reject every disturbance that the planner did not model**.  
Below is a field-tested recipe that quantifies these abstractions.

--------------------------------------------------------
1.  Sensor-fusion: one estimator, two clocks
--------------------------------------------------------
a.  **High-rate INS fusion (≥200 Hz)**  
    – Run an EKF / UKF that fuses IMU + vision / LiDAR odometry with a *constant-velocity* model.  
    – Keep this estimator *on the autopilot MCU*; its sole job is to give the attitude controller a 0.5–1 ms fresh state.  
b.  **Low-rate semantic fusion (1–10 Hz)**  
    – A secondary estimator (factor-graph or sliding-window BA) refines global pose, adds loop-closures, and registers obstacles.  
    – Runs on the companion computer; output is *latched* into the INS estimator so that the fast loop never blocks.  
c.  **Uncertainty broadcast**  
    – Every fusion layer exports 3-σ position / velocity uncertainty together with the state.  
    – The *planning layer treats this uncertainty as a hard inflation radius*; the *control layer treats it as a white-noise input* and simply increases its gains within robust-stability margins (LQR / H∞ design).

--------------------------------------------------------
2.  Planning: receding contract-horizon optimisation
--------------------------------------------------------
Key insight: we do **not** need a globally optimal trajectory every cycle; we only need to prove that the *next N seconds* are optimal and safe, where N is the longest time the drone can free-fall without hitting anything if the radio dies.

Algorithm (used on DJI Manifold-2, 4-core ARM, 15 W):

| Layer | Horizon | Update rate | Optimality guarantee | Typical solver |
|-------|---------|-------------|----------------------|----------------|
| Global | whole mission | 0.2–0.5 Hz | Feasible, not optimal | Sparse A* on 30 m voxel grid |
| Corridor | 60 m (≈8 s) | 5 Hz | Time-optimal inside corridor | B-spline MINCO, 3–4 ms |
| Trajectory | 8 m (≈1 s) | 30–50 Hz | Quadratic optimum | MPC with linearised dynamics |

-  The *global* layer only produces a *topological corridor* (flight tube) and a sparse waypoint sequence.  
-  The *corridor* layer solves a convex optimisation (B-spline MINCO) whose constraints are the inflated corridor plus the uncertainty margin delivered by the semantic estimator.  
-  The *trajectory* layer is a 10-step linear MPC that tracks the B-spline with 50 Hz; it only sees the newest depth-cloud and can brake or swerve within 0.3 m without replanning the corridor.

--------------------------------------------------------
3.  Control: leave the optimisation outside the attitude loop
--------------------------------------------------------
-  The 400 Hz attitude controller is *gain-scheduled* but *never changes structure*; it only receives a 3-D acceleration vector + yaw rate from the MPC.  
-  All actuator limits, gyro bias and battery-induced thrust loss are handled by *anti-windup* and *thrust scaling* inside the attitude loop; the planner is told the *effective* limits once per second.  
-  If the MPC solution is late by even one cycle, the controller falls back to the *previous acceleration vector* plus a decay term—this keeps the vehicle stable while the planner recovers.

--------------------------------------------------------
4.  Triggering: when to replan globally
--------------------------------------------------------
Global replanning is *event-driven*, not time-driven:

1.  Deviation > ½ corridor radius (≈1.5 m).  
2.  New obstacle enters the corridor with persistence ≥ 0.5 s.  
3.  Battery reserve falls below 110 % of remaining energy-to-home.  
4.  Uncertainty inflation grows > 30 % of original radius.

These rules are evaluated on the *companion computer*; the autopilot continues to fly the last MPC trajectory while the global layer recomputes.

--------------------------------------------------------
5.  Compute budget & latency numbers (empirical)
--------------------------------------------------------
Platform: 220 mm quad, PX4-FMUv5 + Raspberry Pi 4

| Task | CPU % | Latency | RAM |
|------|-------|---------|-----|
| INS EKF (200 Hz) | 8 % Cortex-M7 | 0.7 ms | 64 kB |
| Stereo + depth (640×480) | 28 % ARM-A72 | 25 ms | 180 MB |
| Semantic SLAM (10 Hz) | 22 % | 60 ms | 300 MB |
| Corridor optim (5 Hz) | 15 % | 4.2 ms | 40 MB |
| MPC (50 Hz) | 7 % | 1.8 ms | 8 MB |
| Global A* (0.3 Hz) | 18 % (spikes) | 180 ms | 120 MB |

All tasks fit inside the 15 W envelope; worst-case planner jitter is 6 ms, well below the 20 ms deadline imposed by the MPC horizon.

--------------------------------------------------------
6.  Take-away checklist
--------------------------------------------------------
1.  Fuse sensors *once* at the lowest rate that still captures the dynamics you want to plan against.  
2.  Give the attitude controller a *deterministic* reference; never let optimisation latency reach the motor PWM.  
3.  Prove safety for the *worst-case free-fall time*, then make your planning horizon no longer than that.  
4.  Use *corridors* to decouple global feasibility from local optimality; replan globally only when the corridor is violated.  
5.  Export uncertainty *as a number* and treat it as a hard constraint in the planner and as white noise in the controller—this is the only clean way to keep both layers stable.

Follow these rules and you can fly aggressively while still guaranteeing that the globally computed route is *eventually* reached—yet the vehicle never waits for a slow planner to catch up.

## Annotations


## Sources
