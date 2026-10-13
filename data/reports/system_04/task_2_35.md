# Deep Research Report: deep-research-pro-preview-12-2025
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 6f227155 | **Time:** 292.55s | **Cost:** $1.22548
--------------------------------------------------------------------------------

# Balancing Real-Time Responsiveness and Global Optimality in Autonomous Drone Navigation under Sensor Fusion Constraints

### Key Points
*   **Hierarchical Architecture is Essential:** The most effective method to balance responsiveness and optimality is a bifurcated control architecture. A low-frequency **global planner** computes optimal paths based on static maps, while a high-frequency **local planner** handles reactive obstacle avoidance and dynamic feasibility.
*   **Event-Triggered Replanning:** To conserve computational resources, advanced systems utilize event-triggered mechanisms (such as the Event-Triggered Hierarchical Planner or ETHP). Instead of continuous global replanning, the high-level planner is only activated when specific "events" (e.g., obstacle detection within a clearance threshold) occur, allowing the system to remain computationally efficient while maintaining safety.
*   **Sensor Fusion as a Bottleneck and Enabler:** Accurate state estimation is critical. Systems must employ robust fusion algorithms (like Extended Kalman Filters or Factor Graphs) that can handle sensor degradation (e.g., GPS denial, visual drift). Hardware acceleration via FPGAs is increasingly used to process high-bandwidth sensor data (LiDAR, Cameras) with deterministic low latency, ensuring the control loop remains stable.
*   **Hybrid Algorithmic Approaches:** Purely geometric planners (like A*) are often too rigid, while pure reactive methods (like Potential Fields) get stuck in local minima. The state-of-the-art involves hybrid approaches: using sampling-based methods (RRT*) for global guidance and optimization-based or Deep Reinforcement Learning (DRL) methods for local trajectory generation.

---

### Executive Summary
The challenge of autonomous drone navigation lies in the inherent conflict between the need for **global optimality**—finding the most efficient path through a complex environment—and **real-time responsiveness**—reacting to immediate threats and aerodynamic instability. Global planning is computationally expensive and slow, often requiring seconds to compute, which is unacceptable for a drone moving at high speeds. Conversely, reactive control is fast but myopic, often leading to suboptimal paths or dead ends.

Research indicates that the solution lies in **Hierarchical Control Architectures**. By decoupling the problem into a "slow" global layer and a "fast" local layer, drones can navigate effectively. The global layer ensures the mission objectives are met optimally over the long term, while the local layer utilizes **Sensor Fusion** to maintain a precise state estimate and avoid immediate obstacles. Recent advancements in **Deep Reinforcement Learning (DRL)** and **Event-Triggered** mechanisms further refine this balance by allowing the drone to "decide" when to expend resources on replanning. Furthermore, the constraints of onboard processing are being mitigated through **Hardware Acceleration** (e.g., FPGAs), allowing complex sensor fusion algorithms (like Visual-Inertial Odometry) to run in real-time without saturating the flight controller's CPU.

---

## 1. Introduction: The Optimality-Responsiveness Trade-off

Autonomous Unmanned Aerial Vehicles (UAVs) operate in environments that are often dynamic, GPS-denied, and cluttered. To navigate successfully, a drone must solve the **Path Planning Problem** (finding a collision-free route from A to B) and the **Control Problem** (executing that route while stabilizing the aircraft).

The fundamental tension arises from computational complexity. Calculating a globally optimal path in a 3D environment with 6 Degrees of Freedom (DoF) is often NP-hard [cite: 1]. Algorithms that guarantee optimality, such as RRT* (Rapidly-exploring Random Tree Star), are asymptotically optimal but suffer from slow convergence rates, making them unsuitable for real-time reaction to sudden obstacles [cite: 1]. Conversely, reactive controllers that operate in the millisecond range (e.g., PID controllers or Artificial Potential Fields) lack the foresight to avoid local minima (getting stuck in a cul-de-sac) [cite: 2, 3].

Therefore, the central engineering challenge is designing a system architecture that integrates these conflicting requirements under the strict **Size, Weight, and Power (SWaP)** constraints of a drone, where heavy computational payloads reduce flight time and agility.

## 2. Hierarchical Control Architectures

The prevailing consensus in recent research is that a **hierarchical architecture** is the only viable solution for balancing these competing demands. This approach stratifies the navigation stack into distinct layers based on update frequency and abstraction level.

### 2.1 The Bifurcated Planning Model
A standard hierarchical model consists of two primary planners:
1.  **Global Planner (Low Frequency):** This layer operates on a static or slowly updating global map. It calculates the full path from the start to the goal, prioritizing global optimality (shortest distance, minimum energy). It does not need to run at the control loop frequency; it typically replans only when the drone deviates significantly or the mission changes [cite: 4, 5].
2.  **Local Planner (High Frequency):** This layer receives the global path as a series of waypoints or a reference trajectory. Its job is to generate immediate velocity commands (`cmd_vel`) to follow the path while avoiding dynamic or previously unmapped obstacles detected by onboard sensors. It operates within a local subspace (e.g., a sliding window) and replans frequently (e.g., 10–50 Hz) [cite: 4, 5, 6].

### 2.2 Event-Triggered Mechanisms
A significant advancement in balancing these layers is the **Event-Triggered Hierarchical Planner (ETHP)**. In traditional hierarchies, the planners might run at fixed rates. However, ETHP introduces a decision-making logic where the high-level planner (Rerouter) is only triggered when specific conditions are met, such as the detection of an obstacle within a "clearance distance" [cite: 7].

*   **Mechanism:** Under normal conditions, the low-level policy (Goal-Chaser) simply tracks the global goal. When an obstacle breaches the safety threshold, the high-level policy activates to generate a temporary subgoal (waypoint) that guides the drone around the obstacle.
*   **Benefit:** This reduces the computational load significantly. The heavy "replanning" logic is idle during safe flight, allowing the processor to focus on state estimation and stability. Research shows this approach improves success rates in unknown environments compared to single-network end-to-end planners [cite: 7].

### 2.3 Bi-Level Optimization in Reinforcement Learning
Recent applications of Deep Reinforcement Learning (DRL) utilize this hierarchy to train agents more efficiently.
*   **High-Level Policy (Rerouter):** Trained to maximize safety and find subgoals. It uses "Hindsight Experience Replay" (HER) to learn from failures by treating the state reached during a crash as a "virtual goal" to learn how to reach that state safely, effectively decoupling the training of the two levels [cite: 7].
*   **Low-Level Policy (Goal Chaser):** Trained to execute dynamic maneuvers to reach the subgoals provided by the high-level policy. It handles the immediate flight dynamics and stabilization [cite: 7].

## 3. Global Path Planning: Ensuring Optimality

While the local planner handles responsiveness, the global planner ensures the drone does not take a path that is locally safe but globally inefficient (e.g., taking the long way around a large building).

### 3.1 Sampling-Based Algorithms (RRT/RRT*)
Rapidly-exploring Random Trees (RRT) and their optimal variant (RRT*) are standard for high-dimensional spaces.
*   **RRT:** Fast but produces jagged, suboptimal paths.
*   **RRT*:** Rewires the tree to find shorter paths as it grows, guaranteeing asymptotic optimality. However, the convergence is slow, making it risky for real-time dynamic environments [cite: 1].
*   **Informed RRT*:** Improves convergence by limiting the sampling space to an ellipse defined by the current best solution, focusing computational resources on improving the path rather than exploring irrelevant space [cite: 8].

### 3.2 Graph-Based Algorithms (A*)
A* search is optimal on grid maps but suffers from the "curse of dimensionality" in 3D space. It is often used in conjunction with a simplified graph (e.g., a Voronoi diagram or a sparse roadmap) to generate a coarse global path that the local planner then refines [cite: 9, 10].

### 3.3 Trajectory Smoothing and Optimization
Raw paths from A* or RRT are often kinematically infeasible for drones (sharp 90-degree turns). To bridge the gap between the global plan and flight control, **B-Spline** optimization is used. This technique fits a smooth curve through the waypoints, ensuring the trajectory respects the drone's velocity and acceleration limits [cite: 11]. This smoothing step is crucial for "optimality" in terms of energy and time, as smooth flight consumes less battery than jerky maneuvers.

## 4. Real-Time Local Planning: Ensuring Responsiveness

The local planner must operate with low latency to prevent collisions. It relies on immediate sensor data rather than the global map.

### 4.1 Artificial Potential Fields (APF)
APF treats the drone as a particle moving in a field of forces: the goal attracts the drone, and obstacles repel it.
*   **Pros:** Extremely fast computation (reactive).
*   **Cons:** Prone to **Local Minima** (e.g., getting trapped in a U-shaped obstacle).
*   **Hybrid Solution:** Recent research combines APF with global planners (like RRT or A*). The global planner provides intermediate waypoints that "pull" the drone out of local minima, while APF handles the immediate repulsion from obstacles [cite: 2, 6, 12].

### 4.2 Dynamic Window Approach (DWA)
DWA samples a set of achievable velocities (v, w) in the next time step, simulates the drone's trajectory for a short horizon, and scores them based on distance to goal, clearance from obstacles, and speed. It selects the best velocity command directly.
*   **Integration:** DWA is often used as the local planner following a global path generated by A* or Informed-RRT*. The global path provides the general direction, while DWA handles the dynamics [cite: 3, 8].

### 4.3 Vector Field Histogram (VFH)
VFH builds a local polar histogram of obstacle densities around the drone and selects a steering direction with low obstacle density that is closest to the target direction. It is computationally efficient and effective for fast obstacle avoidance in 2D or 2.5D planes [cite: 13].

## 5. Sensor Fusion Constraints and Solutions

Balancing planning and control is impossible without accurate knowledge of the drone's position (Localization) and the environment (Mapping). Sensor fusion is the process of combining data from multiple sensors (IMU, Camera, LiDAR, GPS) to reduce uncertainty.

### 5.1 The Sensor Suite and Limitations
*   **IMU (Inertial Measurement Unit):** High update rate (100Hz+), essential for flight stability. **Constraint:** Suffers from drift; errors accumulate quadratically over time [cite: 14].
*   **GPS:** Provides absolute position. **Constraint:** Unreliable in urban canyons, forests, or indoors (GPS-denied environments) [cite: 14, 15].
*   **Cameras:** Lightweight, rich information. **Constraint:** High computational cost for processing (SLAM), sensitive to lighting (darkness/glare), and motion blur [cite: 14, 16].
*   **LiDAR:** Accurate depth, works in dark. **Constraint:** Heavy, power-hungry, performance degrades in rain/fog [cite: 14].

### 5.2 Fusion Algorithms: EKF vs. UKF vs. Optimization
*   **Extended Kalman Filter (EKF):** The industry standard for fusing IMU and visual/LiDAR data. It linearizes the non-linear system dynamics. **Constraint:** Linearization errors can lead to divergence in highly dynamic flight [cite: 17, 18].
*   **Unscented Kalman Filter (UKF):** Uses sigma points to approximate the probability distribution, handling non-linearities better than EKF. **Constraint:** Higher computational load. Research suggests Adaptive Neuro-Fuzzy implementations of UKF (AFUKF) can outperform EKF in maneuvering accuracy [cite: 19].
*   **Factor Graphs / Optimization-based:** Modern VIO (Visual-Inertial Odometry) systems often use graph optimization (e.g., sliding window optimization) which is more accurate than filtering but computationally heavier.

### 5.3 Handling Sensor Failure and Degradation
Robust systems employ **Adaptive Sensor Fusion**.
*   **Sensor Health Checks:** The system monitors data integrity (e.g., checking image intensity for camera failure, scan point counts for LiDAR). If a sensor fails (e.g., camera blinded by sun), the fusion engine dynamically reconfigures to rely on remaining sensors (e.g., switching to LiDAR-only odometry) [cite: 17].
*   **Redundancy:** Running parallel odometry stacks (e.g., VIO and LiDAR Odometry running simultaneously). If VIO diverges due to feature loss in a textureless tunnel, the system seamlessly switches to LiDAR odometry [cite: 17].
*   **Degradation Isolation:** Algorithms like NSDDI-AFF (Normalized Single-Dimensional Degradation Isolation) use adaptive thresholding to detect and isolate degraded sensor channels in real-time, significantly reducing position errors in complex environments like coal yards or pipelines [cite: 20].

## 6. Hardware Acceleration for Real-Time Performance

To meet the "real-time" requirement while running heavy sensor fusion and path planning algorithms, standard CPUs are often insufficient.

### 6.1 FPGA vs. GPU
*   **FPGAs (Field Programmable Gate Arrays):** Offer deterministic low latency and high parallelism. They are ideal for the "sensor front-end"—processing raw LiDAR points or camera images before they reach the CPU.
    *   *Application:* FPGAs can accelerate Visual SLAM or LiDAR processing pipelines, reducing latency by orders of magnitude compared to CPUs. They enable "sensor fusion at the edge" [cite: 21, 22].
    *   *Event-Based Processing:* FPGAs are particularly well-suited for processing **Event Cameras** (sensors that report pixel changes asynchronously). FPGA implementations of event-based collision avoidance have demonstrated latencies as low as 2.14 ms, enabling agile maneuvers that RGB cameras cannot support [cite: 23].
*   **GPUs (Graphics Processing Units):** Excellent for batch processing and Deep Learning inference (e.g., running the ETHP neural networks). However, they typically have higher power consumption and variable latency compared to FPGAs [cite: 24, 25].

### 6.2 Edge Computing Strategies
*   **Companion Computers:** Drones often carry a flight controller (e.g., Pixhawk) for low-level stabilization and a companion computer (e.g., Nvidia Jetson, Raspberry Pi) for high-level planning and perception.
*   **Offloading:** The FPGA can act as a bridge, preprocessing sensor data (e.g., stereo matching, feature extraction) and sending only the processed "state" to the companion computer, freeing up CPU cycles for the global planner [cite: 22].

## 7. Case Studies in Challenging Environments

### 7.1 GPS-Denied "Dark Tunnels"
In environments like tunnels or mines, GPS is absent, and lighting is poor (rendering cameras useless).
*   **Solution:** Fusion of **LiDAR + IMU** or **mmWave Radar + IMU**.
*   **Example:** The MiNav system uses a lightweight FMCW radar and backscatter tags to navigate dark tunnels. It integrates radar data with IMU in an EKF to maintain localization without vision or GPS [cite: 26].
*   **LIVO (LiDAR-Inertial-Visual Odometry):** Frameworks like FAST-LIVO2 fuse all three. In a dark tunnel, the visual module might fail, but the system relies on LiDAR/IMU. When exiting into bright light (blinding LiDAR or washing out cameras), the fusion filter weights adjust based on sensor uncertainty [cite: 27].

### 7.2 Forest Under-Canopy
Forests present unstructured obstacles, variable lighting, and GPS attenuation.
*   **Solution:** A robust fusion framework using **Stereo VIO + LiDAR Odometry**.
*   **Mechanism:** The system runs a "Sensor Health Check." If the camera exposure fluctuates wildly due to canopy shadows, the confidence in VIO is lowered. If the LiDAR detects insufficient features (open clearing), its weight is reduced. The local planner (e.g., VFH or DWA) uses the fused state to dodge trees, while the global planner ensures the drone doesn't get lost in the forest [cite: 17].

## 8. Conclusion

Effectively balancing real-time responsiveness with global optimality in autonomous drones requires a holistic approach that spans algorithmic architecture and hardware implementation.

1.  **Decouple the Problem:** Use a **Hierarchical Architecture**. Let a slow, optimal Global Planner (RRT*, A*) set the course, and a fast, reactive Local Planner (DWA, APF, RL) handle the flight.
2.  **Optimize the Trigger:** Implement **Event-Triggered** logic (ETHP) to avoid wasteful replanning. Only invoke the high-level planner when the environment demands it (e.g., obstacle detection).
3.  **Fuse Robustly:** Use **Adaptive Sensor Fusion** (EKF/UKF) that monitors sensor health. Rely on complementary modalities (Vision + LiDAR + IMU) to survive single-point failures (darkness, drift).
4.  **Accelerate Hardware:** Leverage **FPGAs** for low-latency sensor processing to ensure the "perception-to-action" loop remains tight enough for stable flight.

By integrating these strategies, autonomous systems can achieve the "best of both worlds": the foresight of global planning and the reflexes of reactive control, all within the tight constraints of an aerial platform.

### References
[cite: 4] Robotics Stack Exchange, "Difference between global and local plan in AMCL navigation," 2020.
[cite: 6] R. A. Knepper et al., "Hierarchical Planner Performance," ICRA, 2010.
[cite: 2] ResearchGate, "Hierarchical Control Architecture," Figure 1.
[cite: 7] MDPI, "Event-Triggered Hierarchical Planner (ETHP)," 2023.
[cite: 5] PX4 Developer Summit, "Autonomous Exploration Path Planning," 2020.
[cite: 9] IEEE, "Autonomous UAV Flight Control for GPS-based Navigation," 2018.
[cite: 1] MDPI, "Review of Path Planning Algorithms," 2023.
[cite: 14] GreyB, "Sensor Fusion Navigation Constraints," 2025.
[cite: 16] arXiv, "Navigating Unknown Indoor Environments," 2024.
[cite: 17] ResearchGate, "Robust Sensor Fusion for GPS-denied Forest," 2022.
[cite: 13] MDPI, "Sensor Fusion Based Navigation Systems," 2025.
[cite: 15] IJIRCST, "Multi-Sensor Fusion for Autonomous Drone Navigation," 2024.
[cite: 28] AIAA, "Real-time path planning vs global optimality," 2020.
[cite: 17] ResearchGate, "Robust Sensor Fusion Framework," 2022.
[cite: 7] MDPI, "Event-Triggered Hierarchical Planner (ETHP)," 2023.
[cite: 21] CVPR, "FPGA Acceleration for Vision," 2015.
[cite: 22] Lattice Semi, "FPGAs Power Real-Time UAV Performance," 2025.
[cite: 29] MDPI, "DRL-based Autonomous Navigation," 2024.
[cite: 30] ResearchGate, "Hierarchical Active Tracking Control via DRL."
[cite: 31] MDPI, "Adaptive Sensor Fusion for Drones," 2025.
[cite: 32] ResearchGate, "Precise landing method based on UKF," 2025.
[cite: 18] CEUR-WS, "Comparative Analysis of Filtering Methods," 2024.
[cite: 20] MDPI, "NSDDI-AFF Method for Sensor Degradation," 2025.
[cite: 19] BME, "Adaptive Neuro Fuzzy UKF," 2021.
[cite: 7] MDPI, "Event-Triggered Hierarchical Planner (ETHP)," 2023.
[cite: 1] MDPI, "Review of Path Planning," 2023.
[cite: 11] ISPRS, "Trajectory Generation and Optimization," 2023.
[cite: 8] MDPI, "Improved Path Planning (Informed-RRT* + DWA)," 2024.
[cite: 3] PMC, "Improved Fusion Path-Planning Algorithm," 2024.
[cite: 23] arXiv, "FPGA-based Event Vision for UAVs," 2025.
[cite: 27] arXiv, "FAST-LIVO2," 2024.
[cite: 26] MIT, "MiNav: RF-based Drone Navigation," 2024.
[cite: 7] MDPI, "ETHP Performance Analysis," 2023.
[cite: 33] MDPI, "RRT Algorithm Analysis," 2023.
[cite: 12] MDPI, "Potential-Field-RRT," 2023.
[cite: 34] ResearchGate, "Autonomous Navigation in Tunnels," 2025.

**Sources:**
1. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFON8Br6r9TFplBsF4KJzA4hFMhGRL4vI2R7qlG0CHi2fN91_Hob4iAU43QtT8Hl0zIaNfqDF9K4W4hxfuZ9VhbM4PdhjxAHoxXNcYyEhYntLfkPHCg0hNgodT3iw==)
2. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMJqKwjYeWrEhmxhTxzaU_vVyJP7ppLZYr_y2HkIUL34h3uwCGkxOFgK6ebgDknpOc_fouqla0nqL2rii-iWLxwIu6u6ack7pyJu6gSNsq_QbgT_KqJi-b-W1sHvmYxBp7P5oDs8Xpn6bDeJl4tfOSOLQorkRAZQeXsp8S6EGRDK1Fa3Q2ArfQpG679WVgFySyZY_MF4yuD0DWfy16WtTFOey0553j2yG3AOzaTNFUR7h-e3wuoa5Dm-Zrs08=)
3. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbsGI5i1J7PBg9QbPqhpEcI6hFsljEF75jKszC8bHAs2tNv3d9uAuF100hs1ORTSEpMluBaoQEPaXopF1jB-7tEhQpn5hQQiqjQZs-C13a6cvldG7XqGIHZMsEJDgPcvzPdh6vUCFvyA==)
4. [stackexchange.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-0UyghyVmd0p2VKhk7JC7yL0Jj7S8t7tE4_oX6na_qSLIJJBU-nhA9azlAiJb7mP7ZgKm02dasQZrdNGe4pXoiHWrnpwz_Qml4XhejMTt2iNZ5jdAUDEMwwwOUT65_Aqb7Yp5ThBmkeatHfYEdnZUFaaPx_aSJwgvKdMtPzBA1sG5YGaotstWDLj6iH0narnKXaPR4WqJ4g4wHL2lLu3A5xC2oqRGH16L-jlviRrZWKEfMx9V)
5. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGO49licrCc8KMJWOFpm3Yaq-YLgpoe9N65bhmHlLo80_paEg5Rs9DP-AngFsI9FbrCYm11sspyWoj89bXv2rW7Kqa82TvRgHrJ3Q5jHNYIGNXsk9g2XDTp9-TEE66soyMU)
6. [cmu.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSREY-dG3zEngoMgUoCBDKduS9hHPD_c1_rHR5XxixthU5puHGtq9G4I5NNl14Arvwdi7cbetpzR3LbdQMLJiYA5Tk7OWwUcqkVfrufxKGpIYO9AagEcRBk5l-o9tdb1Ag99_LSdiyzW-L_abgtFbk)
7. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJfB-KcP9xszUtmECWw13DCKE5Gdno6cNEQACp7uKapMiqscClkVSVaa1pABXPP31O-l8DpR2tcGII5RVzHPBzquhAcwFooUVXRoBne-unMYVm4L4ruvw-AJYmdxU=)
8. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjLt8j91l9Hx7e9ptYJAl6KdY_akaRBaCxRz4A9_G6VG_h9odbb7fvs15e8DC1zsERoMzIF3jL3QPCXZR4FEg50IkZY1foIbSvqqimU91Ku_uvuCwLnrIIqsIgT80=)
9. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2ibq0G2b5NsqSOva1dIjA8Bos9Z4Zo0i06avSMXjChkxfbC86tionNyB8kzAWBE0vIF_KU_54Jjljzh_KqktUuq9uJRQcdMlbTHPpbILLpXxFK3ytYQyIXwpJuP4Tlw0Tbl9P6GPHv6IEXP7JgxE3H06Zfqx2DWPVRFpkGvjgD0W4LHNqN8G0_BjVfqZBCqILeuRyUnxHsUEr9nu0THY=)
10. [ieee.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfMYh39nJbtthU9jaKuP-BGJ-0nxJo_Qd_nIpWpZWuKNUyaKiuryaiqSZlpDNpgZEg7VZbuKdJRBxlo9wV16fEQdiwgL9-x76lntYM30HE7I7o-97T_1eJQeZt0OihilVBuFNwPZw8P-ObZDnvOX7ZMW1DFQ==)
11. [copernicus.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3AEs5UkrINdA-Zr9rJO-oQkoFM84e2e0iyulm4UtJfeNswj59H4uKJ7137SYgoeAtkmp1QXzvZrHxHp4cpyzhxZi9fAkXg1Vtz9qTdD43zO9fPrbDAtLrYLM9ehEYgiA4W__ZCr01S8-ac7AmYbnNEW50cj2u31Qh1n_2R1pYpZFD_f_ti2OPxwIV3S8EvMUpV39Srsslft18t061Wzdd_hQ2T-_qluG1)
12. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7FvHLYyCwMIE9G9J6k3NGxjofdOImedvseRxeSqJH9NXUtLX5ECZKGhRg1Cd5JsR-rfsSbEBKPxpCdMTvP7awhnwxyudv4dbhghicllvtgHm2ywg5zzbFgbmlvQ==)
13. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1KJgNu5OFaDixFUhaFT3mZCGq3XBxg9H9A_y-VrPaRy3mr2DByaFSiKHxx5cxhCwFvXigj4--Ci-lj80jFxe4Izpm1A460fiSz1p3k5QUKm_qsIRAzOlIiUw9hCQ1)
14. [greyb.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHh6U4rd28xgdVGFtCC_N1Q1vDZuxPa5nBhVaIsQC2xvAX4zPTRt2VFygZxL4WmvDlOHptR6gK3ynI2IaKnIlnbruecdqWIvxHSnRJIz-ToYgLPnWO19QWr4mro2JAtKwZVYf4V6WeYxPycgB4=)
15. [ijircst.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkMjrB0pEbMi0_VuctiRFPys8En65Ya8JAioQYleHylqPd4ffXsmAJf8q0EBFHULcbWocWodwcFRwDmW3i02W9RAut2KnG3RUeVNNfNs6XHzo8m-6dy_tfI6kjOFPqQw7Tf3X051PG3NmullOLGB7qbKdsLB-hM6usbdXHUphRiwGf_bm9ZRMr2zVwpqClG3DuMVMe-GOeWmUhz8PmvE62e7g4YnW1Tmr-k6VqbuxBxBo8NmE_HM9L5i8=)
16. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9wC6nFChSpYP-BNL32dFaNaXUU6YBPTz5G-vlRWHRSmacHftOsSUYvghhzQLtCbIgZ6-x-SU_c5JqY7HmFiBAdvDiduXjiDcJL9I2IEcWIY1kQBHupyTj-g==)
17. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlInKbDITxdV1TbMl0BiDlGYQTER0Gt4Peejx3E4mhQFHbY9Wf_ccoAhlaGAc8CxblXhvte0fsP0t7tkb2OivaXzcsCT1yLzM5KnsP_fw2hmcbu5NDta6XtR0mX9gd0IYWi298hcLla7O1Rh3N-LhEtHWiwBLUP7LsASwDx50MXl04bDgmDfXEA91IrUy2EpyDcPg2eKr1AcMOGGXTfmth8374JkO_Jvp8zfSwrD5EFjQBDQ9ZgeIpffp7Uns=)
18. [ceur-ws.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtkIf4AealfhdYDK1bs-sRK8TbEWL12t9quvnnZnzrkO3AEeR0CxgV2B9zVpUOVbvrm2O6xD4iAT9-g5pWhrlEdi77yjG0sUt4cwl_zB81vpO9vEW7ZA7u3lspbgVu)
19. [bme.hu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCfgt_cqc7q-ePj34yTElJLxe19jGWMISgmbxpuBcMvWGS-ll88iWXk7DY9FREFZSAVodKnqMYcgID0yiWk_1pBqhULMM9Sdey2GZ6mR48OApUs26O7ec2INW7e50SNtUKBB3hQOeenR85PJdKsQA=)
20. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYAK-QXnPdmjSZx7dimUPrctxjBIo4CYDUJ9Fdp3v_1yVyJXFnpzveEQaedao1xrB9qloZaeg5jacVL7Ixvs-VT2722WCVBdnz7GGfhha7NNyvroYBYgXCH7rVGQ==)
21. [thecvf.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUt2jImE--ubRDlQHs8axiV0FlFk3J-nVpwRyvZLWfedyiE1Kl-LPL6SQ4l5kU4-Y2YoSEhObiEib0jZsHGYs9DQ8WTlefDKcPCaudR3WjWeM4wCAmZNE0esBAw_vNqXo5X3qvKP9pcbmJkjQPfHmsIGLVr3aQAykTLvgH9rmRO6lOOB_jKHNLn1v4hnKY0HT4CEQq8bGUb9hp0c__fDa1KcM3fKJSnG8=)
22. [latticesemi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkmK-2UBAD8d8dU36n31cSEM9_oXTC8SFsU56XW9MXQdMSuPG8sD6ZzdZSLM6v2RUjLkxEbjBfFt6mDQgjlaxHzkAFSsyeSuNTlr7DSgVELSuV4h5HkfxntT6M3mhnyisC1JuiKyEjH8Aru6gpcE5GOeeRa26G5Z__W1v2oaGQTpoLq2Vl8oKlbk8IrYRM6kaxUuktRqRquLwcqzI6E269)
23. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECaFAJOCBWE1iapKcFNcCdnTzN-I2ufEDHbiejiGRuEtXgRcbVRIIgyFL1A7YDbXaqGmGXosrZieRsMNCSf1Rtp44JkQ4OchAXc-HGfcGvf1omvq7nAjcoHw==)
24. [utupub.fi](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZOoWHi7m2ddmCS-KTcpBvXay0aGbUhi3aftY7Ig4dcpo71PAkZMVCD8in0L6nfEd82IgwI2_ZMO3H2O4scCEYE5RueG4NNKWqCPVdYnlq-VLnwAQHTYsDXHETZrHnXBNLQX5Ff4jgq4UvJJN7MwhZkOsuVSkuc4gxTu9OLA21JPGXjNoeplywh1qKoVJg)
25. [decadefense.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcnerYbXhgzKWmFzu9P1X1iy4rWarECLtFK_0w8PTa8mYge9GnQyxauIU8e4Y_EEHVVUXr4V3uYEiEc2rIiZsTRtuCArm0HHGa6Inj--g0li9AYVWmuXksko3fKEiHVp1-enYz5NB4u6hEeWwFtMA=)
26. [mit.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGisqdX1z2xbmQj3z8sU7oehs8haY73F9C5Dsg0QKBKCA0lvDLq6lGPqjINXgYYaS3TufzFWYOntsUl7q3Udbky9FiXOWrolYvVyL62qjLTQt4Lpc0V2lJoArbcDyAWiPi2N-98RB-t3Jc-eOGHQ46nzmONW7KhO1Q6jTTpgFgWHPS_UHNDhV5QjtmcpTP6)
27. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFh1TR98uA8L9L8h9z73RGcdYhTKPxDpyavA9X2l5cnL1IBY3V7vBAS2UBVBSpk5NQUGalEe-Ns1B9oMHJSgP0ogccOEKlwLfVEzlWOGxBsN8wH0wMnijRD7w==)
28. [aiaa.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHA33kidH5Xf6Zhpckyx6HxbHssSKoYSsgJWciWaWerHiaTF6bOWRpNRfNJBBHhU3nJXohFtcR8x5HmLtzK4aFbKbAu5qe2x9dMKjZ7ZzyLEc-jaoXk6ZSoVHeojF6Phu2O3A==)
29. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJcn61b3sSG8g8UVSsUTdRaanv8zJmZ0CSzUghoPndFXMk1vOUYKDTs0eiJxdqAGH3Ho8yAeLUGMt_SE9Ms4RH3d7u0BRWedAEC5GPnr8NXkjxDfsD7G-rxgPVYA==)
30. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpJ6XWmXNe9H8LXlztTbtdufEL0T8UOek6KQ6EhBN4QX81CiSx42IInqRPkKAgfVKzBYXaEXntHMQ_B4s3OI-XLG3L8DUtAG8pqn4YqmLUctkaqZpvApKxiI_FZFPdIsG5Cl9Yy0GvUYjGPGmnkb9jZWE1xUVED8aPkflxemzTzy8LxEUrtqHKjh2kkxGQTPp3IJ4pAu3wo-2gQ5LZL_DnTb2RD8PHQ_qVYWqLk8CAHFOttrChmkY=)
31. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzM7eQfyvCaMvD_UJGTNlQyq2enM7EgQRdOZuu8oESGYp5oGyLAdYLd2nrYWoF-ZYKrvyAzHOd_LmHOuICLifgUO9gmHs0HCO4PiRhIwHBfb77jp7PcC4KFH5pnanT5Q==)
32. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2lRjbJ_jbeAy8vezRoMJiMXopJFnelGbmCS6aJxjvUyWv6tY8Ix4kZ-UVKy4j3nfLywMkkhegBF1P2dFyViFg1JiCdH-_S-N38nfPINC0hj9pLnrlTu4x4WkWYBzgl6q4uZLFLcQhhOYJtW0F12VACdY3KzSaQ79MfpRlTtieibFCMtJ8-vR2huqh6L9qd0Gf5JR35EfTmMPTLaOd1ElFmRSIqmWsgDaHHn-DJS7q72hN6X3UErU3KKS4GK45cxMUtqQeSSRQPbQMOqL0RQVREA==)
33. [mdpi.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoaTeAHouQOLRf_sDc6xH1t2eqX26v-j-E3Vsr8NY1DuhMHcohAcAQvGwX_ZdYQYVnwmPud0VVSiVhgFdM-SDOHKx1fM-dghPm7a1twgeCIEh18UuasqpMQJQG3zLI3g==)
34. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFovF8mqgGkcjIK0BNoBDjnHekAmBQuIiUiEGWw2Gvjgqa_MA24ubHki5LX3dYz6b358LiFbJU3BoP-LKdXulA68Rnajqm9V804nyf_3QMxxPQ64OKVIkJmGGSrht-ymfA1rc8p0qtHaFa8MvkgmMn41NwxVC9rKkqdvtNASz8zqTv_S2FqJpub8i7I3XIi3LUFKtzsLA5baKcpMr9JASjHjNLlTQXLt1oi7l9-8Ke4Bms6wx9q8ktaWfS67bw=)


## Annotations
Annotation(end_index=3700, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFON8Br6r9TFplBsF4KJzA4hFMhGRL4vI2R7qlG0CHi2fN91_Hob4iAU43QtT8Hl0zIaNfqDF9K4W4hxfuZ9VhbM4PdhjxAHoxXNcYyEhYntLfkPHCg0hNgodT3iw==', start_index=3691)
Annotation(end_index=3933, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFON8Br6r9TFplBsF4KJzA4hFMhGRL4vI2R7qlG0CHi2fN91_Hob4iAU43QtT8Hl0zIaNfqDF9K4W4hxfuZ9VhbM4PdhjxAHoxXNcYyEhYntLfkPHCg0hNgodT3iw==', start_index=3924)
Annotation(end_index=4146, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMJqKwjYeWrEhmxhTxzaU_vVyJP7ppLZYr_y2HkIUL34h3uwCGkxOFgK6ebgDknpOc_fouqla0nqL2rii-iWLxwIu6u6ack7pyJu6gSNsq_QbgT_KqJi-b-W1sHvmYxBp7P5oDs8Xpn6bDeJl4tfOSOLQorkRAZQeXsp8S6EGRDK1Fa3Q2ArfQpG679WVgFySyZY_MF4yuD0DWfy16WtTFOey0553j2yG3AOzaTNFUR7h-e3wuoa5Dm-Zrs08=', start_index=4134)
Annotation(end_index=4146, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbsGI5i1J7PBg9QbPqhpEcI6hFsljEF75jKszC8bHAs2tNv3d9uAuF100hs1ORTSEpMluBaoQEPaXopF1jB-7tEhQpn5hQQiqjQZs-C13a6cvldG7XqGIHZMsEJDgPcvzPdh6vUCFvyA==', start_index=4134)
Annotation(end_index=5213, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGO49licrCc8KMJWOFpm3Yaq-YLgpoe9N65bhmHlLo80_paEg5Rs9DP-AngFsI9FbrCYm11sspyWoj89bXv2rW7Kqa82TvRgHrJ3Q5jHNYIGNXsk9g2XDTp9-TEE66soyMU', start_index=5201)
Annotation(end_index=5213, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-0UyghyVmd0p2VKhk7JC7yL0Jj7S8t7tE4_oX6na_qSLIJJBU-nhA9azlAiJb7mP7ZgKm02dasQZrdNGe4pXoiHWrnpwz_Qml4XhejMTt2iNZ5jdAUDEMwwwOUT65_Aqb7Yp5ThBmkeatHfYEdnZUFaaPx_aSJwgvKdMtPzBA1sG5YGaotstWDLj6iH0narnKXaPR4WqJ4g4wHL2lLu3A5xC2oqRGH16L-jlviRrZWKEfMx9V', start_index=5201)
Annotation(end_index=5628, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGO49licrCc8KMJWOFpm3Yaq-YLgpoe9N65bhmHlLo80_paEg5Rs9DP-AngFsI9FbrCYm11sspyWoj89bXv2rW7Kqa82TvRgHrJ3Q5jHNYIGNXsk9g2XDTp9-TEE66soyMU', start_index=5613)
Annotation(end_index=5628, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSREY-dG3zEngoMgUoCBDKduS9hHPD_c1_rHR5XxixthU5puHGtq9G4I5NNl14Arvwdi7cbetpzR3LbdQMLJiYA5Tk7OWwUcqkVfrufxKGpIYO9AagEcRBk5l-o9tdb1Ag99_LSdiyzW-L_abgtFbk', start_index=5613)
Annotation(end_index=5628, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-0UyghyVmd0p2VKhk7JC7yL0Jj7S8t7tE4_oX6na_qSLIJJBU-nhA9azlAiJb7mP7ZgKm02dasQZrdNGe4pXoiHWrnpwz_Qml4XhejMTt2iNZ5jdAUDEMwwwOUT65_Aqb7Yp5ThBmkeatHfYEdnZUFaaPx_aSJwgvKdMtPzBA1sG5YGaotstWDLj6iH0narnKXaPR4WqJ4g4wHL2lLu3A5xC2oqRGH16L-jlviRrZWKEfMx9V', start_index=5613)
Annotation(end_index=6058, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJfB-KcP9xszUtmECWw13DCKE5Gdno6cNEQACp7uKapMiqscClkVSVaa1pABXPP31O-l8DpR2tcGII5RVzHPBzquhAcwFooUVXRoBne-unMYVm4L4ruvw-AJYmdxU=', start_index=6049)
Annotation(end_index=6661, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJfB-KcP9xszUtmECWw13DCKE5Gdno6cNEQACp7uKapMiqscClkVSVaa1pABXPP31O-l8DpR2tcGII5RVzHPBzquhAcwFooUVXRoBne-unMYVm4L4ruvw-AJYmdxU=', start_index=6652)
Annotation(end_index=7154, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJfB-KcP9xszUtmECWw13DCKE5Gdno6cNEQACp7uKapMiqscClkVSVaa1pABXPP31O-l8DpR2tcGII5RVzHPBzquhAcwFooUVXRoBne-unMYVm4L4ruvw-AJYmdxU=', start_index=7145)
Annotation(end_index=7358, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJfB-KcP9xszUtmECWw13DCKE5Gdno6cNEQACp7uKapMiqscClkVSVaa1pABXPP31O-l8DpR2tcGII5RVzHPBzquhAcwFooUVXRoBne-unMYVm4L4ruvw-AJYmdxU=', start_index=7349)
Annotation(end_index=8026, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFON8Br6r9TFplBsF4KJzA4hFMhGRL4vI2R7qlG0CHi2fN91_Hob4iAU43QtT8Hl0zIaNfqDF9K4W4hxfuZ9VhbM4PdhjxAHoxXNcYyEhYntLfkPHCg0hNgodT3iw==', start_index=8017)
Annotation(end_index=8258, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjLt8j91l9Hx7e9ptYJAl6KdY_akaRBaCxRz4A9_G6VG_h9odbb7fvs15e8DC1zsERoMzIF3jL3QPCXZR4FEg50IkZY1foIbSvqqimU91Ku_uvuCwLnrIIqsIgT80=', start_index=8249)
Annotation(end_index=8575, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfMYh39nJbtthU9jaKuP-BGJ-0nxJo_Qd_nIpWpZWuKNUyaKiuryaiqSZlpDNpgZEg7VZbuKdJRBxlo9wV16fEQdiwgL9-x76lntYM30HE7I7o-97T_1eJQeZt0OihilVBuFNwPZw8P-ObZDnvOX7ZMW1DFQ==', start_index=8562)
Annotation(end_index=8575, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2ibq0G2b5NsqSOva1dIjA8Bos9Z4Zo0i06avSMXjChkxfbC86tionNyB8kzAWBE0vIF_KU_54Jjljzh_KqktUuq9uJRQcdMlbTHPpbILLpXxFK3ytYQyIXwpJuP4Tlw0Tbl9P6GPHv6IEXP7JgxE3H06Zfqx2DWPVRFpkGvjgD0W4LHNqN8G0_BjVfqZBCqILeuRyUnxHsUEr9nu0THY=', start_index=8562)
Annotation(end_index=8963, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3AEs5UkrINdA-Zr9rJO-oQkoFM84e2e0iyulm4UtJfeNswj59H4uKJ7137SYgoeAtkmp1QXzvZrHxHp4cpyzhxZi9fAkXg1Vtz9qTdD43zO9fPrbDAtLrYLM9ehEYgiA4W__ZCr01S8-ac7AmYbnNEW50cj2u31Qh1n_2R1pYpZFD_f_ti2OPxwIV3S8EvMUpV39Srsslft18t061Wzdd_hQ2T-_qluG1', start_index=8953)
Annotation(end_index=9856, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7FvHLYyCwMIE9G9J6k3NGxjofdOImedvseRxeSqJH9NXUtLX5ECZKGhRg1Cd5JsR-rfsSbEBKPxpCdMTvP7awhnwxyudv4dbhghicllvtgHm2ywg5zzbFgbmlvQ==', start_index=9840)
Annotation(end_index=9856, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMJqKwjYeWrEhmxhTxzaU_vVyJP7ppLZYr_y2HkIUL34h3uwCGkxOFgK6ebgDknpOc_fouqla0nqL2rii-iWLxwIu6u6ack7pyJu6gSNsq_QbgT_KqJi-b-W1sHvmYxBp7P5oDs8Xpn6bDeJl4tfOSOLQorkRAZQeXsp8S6EGRDK1Fa3Q2ArfQpG679WVgFySyZY_MF4yuD0DWfy16WtTFOey0553j2yG3AOzaTNFUR7h-e3wuoa5Dm-Zrs08=', start_index=9840)
Annotation(end_index=9856, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSREY-dG3zEngoMgUoCBDKduS9hHPD_c1_rHR5XxixthU5puHGtq9G4I5NNl14Arvwdi7cbetpzR3LbdQMLJiYA5Tk7OWwUcqkVfrufxKGpIYO9AagEcRBk5l-o9tdb1Ag99_LSdiyzW-L_abgtFbk', start_index=9840)
Annotation(end_index=10360, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjLt8j91l9Hx7e9ptYJAl6KdY_akaRBaCxRz4A9_G6VG_h9odbb7fvs15e8DC1zsERoMzIF3jL3QPCXZR4FEg50IkZY1foIbSvqqimU91Ku_uvuCwLnrIIqsIgT80=', start_index=10348)
Annotation(end_index=10360, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbsGI5i1J7PBg9QbPqhpEcI6hFsljEF75jKszC8bHAs2tNv3d9uAuF100hs1ORTSEpMluBaoQEPaXopF1jB-7tEhQpn5hQQiqjQZs-C13a6cvldG7XqGIHZMsEJDgPcvzPdh6vUCFvyA==', start_index=10348)
Annotation(end_index=10679, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1KJgNu5OFaDixFUhaFT3mZCGq3XBxg9H9A_y-VrPaRy3mr2DByaFSiKHxx5cxhCwFvXigj4--Ci-lj80jFxe4Izpm1A460fiSz1p3k5QUKm_qsIRAzOlIiUw9hCQ1', start_index=10669)
Annotation(end_index=11219, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHh6U4rd28xgdVGFtCC_N1Q1vDZuxPa5nBhVaIsQC2xvAX4zPTRt2VFygZxL4WmvDlOHptR6gK3ynI2IaKnIlnbruecdqWIvxHSnRJIz-ToYgLPnWO19QWr4mro2JAtKwZVYf4V6WeYxPycgB4=', start_index=11209)
Annotation(end_index=11367, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkMjrB0pEbMi0_VuctiRFPys8En65Ya8JAioQYleHylqPd4ffXsmAJf8q0EBFHULcbWocWodwcFRwDmW3i02W9RAut2KnG3RUeVNNfNs6XHzo8m-6dy_tfI6kjOFPqQw7Tf3X051PG3NmullOLGB7qbKdsLB-hM6usbdXHUphRiwGf_bm9ZRMr2zVwpqClG3DuMVMe-GOeWmUhz8PmvE62e7g4YnW1Tmr-k6VqbuxBxBo8NmE_HM9L5i8=', start_index=11353)
Annotation(end_index=11367, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHh6U4rd28xgdVGFtCC_N1Q1vDZuxPa5nBhVaIsQC2xvAX4zPTRt2VFygZxL4WmvDlOHptR6gK3ynI2IaKnIlnbruecdqWIvxHSnRJIz-ToYgLPnWO19QWr4mro2JAtKwZVYf4V6WeYxPycgB4=', start_index=11353)
Annotation(end_index=11550, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9wC6nFChSpYP-BNL32dFaNaXUU6YBPTz5G-vlRWHRSmacHftOsSUYvghhzQLtCbIgZ6-x-SU_c5JqY7HmFiBAdvDiduXjiDcJL9I2IEcWIY1kQBHupyTj-g==', start_index=11536)
Annotation(end_index=11550, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHh6U4rd28xgdVGFtCC_N1Q1vDZuxPa5nBhVaIsQC2xvAX4zPTRt2VFygZxL4WmvDlOHptR6gK3ynI2IaKnIlnbruecdqWIvxHSnRJIz-ToYgLPnWO19QWr4mro2JAtKwZVYf4V6WeYxPycgB4=', start_index=11536)
Annotation(end_index=11678, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHh6U4rd28xgdVGFtCC_N1Q1vDZuxPa5nBhVaIsQC2xvAX4zPTRt2VFygZxL4WmvDlOHptR6gK3ynI2IaKnIlnbruecdqWIvxHSnRJIz-ToYgLPnWO19QWr4mro2JAtKwZVYf4V6WeYxPycgB4=', start_index=11668)
Annotation(end_index=11980, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlInKbDITxdV1TbMl0BiDlGYQTER0Gt4Peejx3E4mhQFHbY9Wf_ccoAhlaGAc8CxblXhvte0fsP0t7tkb2OivaXzcsCT1yLzM5KnsP_fw2hmcbu5NDta6XtR0mX9gd0IYWi298hcLla7O1Rh3N-LhEtHWiwBLUP7LsASwDx50MXl04bDgmDfXEA91IrUy2EpyDcPg2eKr1AcMOGGXTfmth8374JkO_Jvp8zfSwrD5EFjQBDQ9ZgeIpffp7Uns=', start_index=11966)
Annotation(end_index=11980, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtkIf4AealfhdYDK1bs-sRK8TbEWL12t9quvnnZnzrkO3AEeR0CxgV2B9zVpUOVbvrm2O6xD4iAT9-g5pWhrlEdi77yjG0sUt4cwl_zB81vpO9vEW7ZA7u3lspbgVu', start_index=11966)
Annotation(end_index=12292, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCfgt_cqc7q-ePj34yTElJLxe19jGWMISgmbxpuBcMvWGS-ll88iWXk7DY9FREFZSAVodKnqMYcgID0yiWk_1pBqhULMM9Sdey2GZ6mR48OApUs26O7ec2INW7e50SNtUKBB3hQOeenR85PJdKsQA=', start_index=12282)
Annotation(end_index=12934, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlInKbDITxdV1TbMl0BiDlGYQTER0Gt4Peejx3E4mhQFHbY9Wf_ccoAhlaGAc8CxblXhvte0fsP0t7tkb2OivaXzcsCT1yLzM5KnsP_fw2hmcbu5NDta6XtR0mX9gd0IYWi298hcLla7O1Rh3N-LhEtHWiwBLUP7LsASwDx50MXl04bDgmDfXEA91IrUy2EpyDcPg2eKr1AcMOGGXTfmth8374JkO_Jvp8zfSwrD5EFjQBDQ9ZgeIpffp7Uns=', start_index=12924)
Annotation(end_index=13164, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlInKbDITxdV1TbMl0BiDlGYQTER0Gt4Peejx3E4mhQFHbY9Wf_ccoAhlaGAc8CxblXhvte0fsP0t7tkb2OivaXzcsCT1yLzM5KnsP_fw2hmcbu5NDta6XtR0mX9gd0IYWi298hcLla7O1Rh3N-LhEtHWiwBLUP7LsASwDx50MXl04bDgmDfXEA91IrUy2EpyDcPg2eKr1AcMOGGXTfmth8374JkO_Jvp8zfSwrD5EFjQBDQ9ZgeIpffp7Uns=', start_index=13154)
Annotation(end_index=13466, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYAK-QXnPdmjSZx7dimUPrctxjBIo4CYDUJ9Fdp3v_1yVyJXFnpzveEQaedao1xrB9qloZaeg5jacVL7Ixvs-VT2722WCVBdnz7GGfhha7NNyvroYBYgXCH7rVGQ==', start_index=13456)
Annotation(end_index=14101, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUt2jImE--ubRDlQHs8axiV0FlFk3J-nVpwRyvZLWfedyiE1Kl-LPL6SQ4l5kU4-Y2YoSEhObiEib0jZsHGYs9DQ8WTlefDKcPCaudR3WjWeM4wCAmZNE0esBAw_vNqXo5X3qvKP9pcbmJkjQPfHmsIGLVr3aQAykTLvgH9rmRO6lOOB_jKHNLn1v4hnKY0HT4CEQq8bGUb9hp0c__fDa1KcM3fKJSnG8=', start_index=14087)
Annotation(end_index=14101, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkmK-2UBAD8d8dU36n31cSEM9_oXTC8SFsU56XW9MXQdMSuPG8sD6ZzdZSLM6v2RUjLkxEbjBfFt6mDQgjlaxHzkAFSsyeSuNTlr7DSgVELSuV4h5HkfxntT6M3mhnyisC1JuiKyEjH8Aru6gpcE5GOeeRa26G5Z__W1v2oaGQTpoLq2Vl8oKlbk8IrYRM6kaxUuktRqRquLwcqzI6E269', start_index=14087)
Annotation(end_index=14427, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECaFAJOCBWE1iapKcFNcCdnTzN-I2ufEDHbiejiGRuEtXgRcbVRIIgyFL1A7YDbXaqGmGXosrZieRsMNCSf1Rtp44JkQ4OchAXc-HGfcGvf1omvq7nAjcoHw==', start_index=14417)
Annotation(end_index=14679, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEcnerYbXhgzKWmFzu9P1X1iy4rWarECLtFK_0w8PTa8mYge9GnQyxauIU8e4Y_EEHVVUXr4V3uYEiEc2rIiZsTRtuCArm0HHGa6Inj--g0li9AYVWmuXksko3fKEiHVp1-enYz5NB4u6hEeWwFtMA=', start_index=14665)
Annotation(end_index=14679, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGZOoWHi7m2ddmCS-KTcpBvXay0aGbUhi3aftY7Ig4dcpo71PAkZMVCD8in0L6nfEd82IgwI2_ZMO3H2O4scCEYE5RueG4NNKWqCPVdYnlq-VLnwAQHTYsDXHETZrHnXBNLQX5Ff4jgq4UvJJN7MwhZkOsuVSkuc4gxTu9OLA21JPGXjNoeplywh1qKoVJg', start_index=14665)
Annotation(end_index=15170, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkmK-2UBAD8d8dU36n31cSEM9_oXTC8SFsU56XW9MXQdMSuPG8sD6ZzdZSLM6v2RUjLkxEbjBfFt6mDQgjlaxHzkAFSsyeSuNTlr7DSgVELSuV4h5HkfxntT6M3mhnyisC1JuiKyEjH8Aru6gpcE5GOeeRa26G5Z__W1v2oaGQTpoLq2Vl8oKlbk8IrYRM6kaxUuktRqRquLwcqzI6E269', start_index=15160)
Annotation(end_index=15642, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGisqdX1z2xbmQj3z8sU7oehs8haY73F9C5Dsg0QKBKCA0lvDLq6lGPqjINXgYYaS3TufzFWYOntsUl7q3Udbky9FiXOWrolYvVyL62qjLTQt4Lpc0V2lJoArbcDyAWiPi2N-98RB-t3Jc-eOGHQ46nzmONW7KhO1Q6jTTpgFgWHPS_UHNDhV5QjtmcpTP6', start_index=15632)
Annotation(end_index=15961, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFh1TR98uA8L9L8h9z73RGcdYhTKPxDpyavA9X2l5cnL1IBY3V7vBAS2UBVBSpk5NQUGalEe-Ns1B9oMHJSgP0ogccOEKlwLfVEzlWOGxBsN8wH0wMnijRD7w==', start_index=15951)
Annotation(end_index=16554, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlInKbDITxdV1TbMl0BiDlGYQTER0Gt4Peejx3E4mhQFHbY9Wf_ccoAhlaGAc8CxblXhvte0fsP0t7tkb2OivaXzcsCT1yLzM5KnsP_fw2hmcbu5NDta6XtR0mX9gd0IYWi298hcLla7O1Rh3N-LhEtHWiwBLUP7LsASwDx50MXl04bDgmDfXEA91IrUy2EpyDcPg2eKr1AcMOGGXTfmth8374JkO_Jvp8zfSwrD5EFjQBDQ9ZgeIpffp7Uns=', start_index=16544)
Annotation(end_index=17766, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-0UyghyVmd0p2VKhk7JC7yL0Jj7S8t7tE4_oX6na_qSLIJJBU-nhA9azlAiJb7mP7ZgKm02dasQZrdNGe4pXoiHWrnpwz_Qml4XhejMTt2iNZ5jdAUDEMwwwOUT65_Aqb7Yp5ThBmkeatHfYEdnZUFaaPx_aSJwgvKdMtPzBA1sG5YGaotstWDLj6iH0narnKXaPR4WqJ4g4wHL2lLu3A5xC2oqRGH16L-jlviRrZWKEfMx9V', start_index=17757)
Annotation(end_index=17870, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGSREY-dG3zEngoMgUoCBDKduS9hHPD_c1_rHR5XxixthU5puHGtq9G4I5NNl14Arvwdi7cbetpzR3LbdQMLJiYA5Tk7OWwUcqkVfrufxKGpIYO9AagEcRBk5l-o9tdb1Ag99_LSdiyzW-L_abgtFbk', start_index=17861)
Annotation(end_index=17950, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMJqKwjYeWrEhmxhTxzaU_vVyJP7ppLZYr_y2HkIUL34h3uwCGkxOFgK6ebgDknpOc_fouqla0nqL2rii-iWLxwIu6u6ack7pyJu6gSNsq_QbgT_KqJi-b-W1sHvmYxBp7P5oDs8Xpn6bDeJl4tfOSOLQorkRAZQeXsp8S6EGRDK1Fa3Q2ArfQpG679WVgFySyZY_MF4yuD0DWfy16WtTFOey0553j2yG3AOzaTNFUR7h-e3wuoa5Dm-Zrs08=', start_index=17941)
Annotation(end_index=18021, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJfB-KcP9xszUtmECWw13DCKE5Gdno6cNEQACp7uKapMiqscClkVSVaa1pABXPP31O-l8DpR2tcGII5RVzHPBzquhAcwFooUVXRoBne-unMYVm4L4ruvw-AJYmdxU=', start_index=18012)
Annotation(end_index=18090, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGO49licrCc8KMJWOFpm3Yaq-YLgpoe9N65bhmHlLo80_paEg5Rs9DP-AngFsI9FbrCYm11sspyWoj89bXv2rW7Kqa82TvRgHrJ3Q5jHNYIGNXsk9g2XDTp9-TEE66soyMU', start_index=18081)
Annotation(end_index=18168, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH2ibq0G2b5NsqSOva1dIjA8Bos9Z4Zo0i06avSMXjChkxfbC86tionNyB8kzAWBE0vIF_KU_54Jjljzh_KqktUuq9uJRQcdMlbTHPpbILLpXxFK3ytYQyIXwpJuP4Tlw0Tbl9P6GPHv6IEXP7JgxE3H06Zfqx2DWPVRFpkGvjgD0W4LHNqN8G0_BjVfqZBCqILeuRyUnxHsUEr9nu0THY=', start_index=18159)
Annotation(end_index=18248, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFON8Br6r9TFplBsF4KJzA4hFMhGRL4vI2R7qlG0CHi2fN91_Hob4iAU43QtT8Hl0zIaNfqDF9K4W4hxfuZ9VhbM4PdhjxAHoxXNcYyEhYntLfkPHCg0hNgodT3iw==', start_index=18239)
Annotation(end_index=18309, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHh6U4rd28xgdVGFtCC_N1Q1vDZuxPa5nBhVaIsQC2xvAX4zPTRt2VFygZxL4WmvDlOHptR6gK3ynI2IaKnIlnbruecdqWIvxHSnRJIz-ToYgLPnWO19QWr4mro2JAtKwZVYf4V6WeYxPycgB4=', start_index=18299)
Annotation(end_index=18373, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9wC6nFChSpYP-BNL32dFaNaXUU6YBPTz5G-vlRWHRSmacHftOsSUYvghhzQLtCbIgZ6-x-SU_c5JqY7HmFiBAdvDiduXjiDcJL9I2IEcWIY1kQBHupyTj-g==', start_index=18363)
Annotation(end_index=18439, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlInKbDITxdV1TbMl0BiDlGYQTER0Gt4Peejx3E4mhQFHbY9Wf_ccoAhlaGAc8CxblXhvte0fsP0t7tkb2OivaXzcsCT1yLzM5KnsP_fw2hmcbu5NDta6XtR0mX9gd0IYWi298hcLla7O1Rh3N-LhEtHWiwBLUP7LsASwDx50MXl04bDgmDfXEA91IrUy2EpyDcPg2eKr1AcMOGGXTfmth8374JkO_Jvp8zfSwrD5EFjQBDQ9ZgeIpffp7Uns=', start_index=18429)
Annotation(end_index=18516, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG1KJgNu5OFaDixFUhaFT3mZCGq3XBxg9H9A_y-VrPaRy3mr2DByaFSiKHxx5cxhCwFvXigj4--Ci-lj80jFxe4Izpm1A460fiSz1p3k5QUKm_qsIRAzOlIiUw9hCQ1', start_index=18506)
Annotation(end_index=18581, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkMjrB0pEbMi0_VuctiRFPys8En65Ya8JAioQYleHylqPd4ffXsmAJf8q0EBFHULcbWocWodwcFRwDmW3i02W9RAut2KnG3RUeVNNfNs6XHzo8m-6dy_tfI6kjOFPqQw7Tf3X051PG3NmullOLGB7qbKdsLB-hM6usbdXHUphRiwGf_bm9ZRMr2zVwpqClG3DuMVMe-GOeWmUhz8PmvE62e7g4YnW1Tmr-k6VqbuxBxBo8NmE_HM9L5i8=', start_index=18571)
Annotation(end_index=18662, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHA33kidH5Xf6Zhpckyx6HxbHssSKoYSsgJWciWaWerHiaTF6bOWRpNRfNJBBHhU3nJXohFtcR8x5HmLtzK4aFbKbAu5qe2x9dMKjZ7ZzyLEc-jaoXk6ZSoVHeojF6Phu2O3A==', start_index=18652)
Annotation(end_index=18733, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHlInKbDITxdV1TbMl0BiDlGYQTER0Gt4Peejx3E4mhQFHbY9Wf_ccoAhlaGAc8CxblXhvte0fsP0t7tkb2OivaXzcsCT1yLzM5KnsP_fw2hmcbu5NDta6XtR0mX9gd0IYWi298hcLla7O1Rh3N-LhEtHWiwBLUP7LsASwDx50MXl04bDgmDfXEA91IrUy2EpyDcPg2eKr1AcMOGGXTfmth8374JkO_Jvp8zfSwrD5EFjQBDQ9ZgeIpffp7Uns=', start_index=18723)
Annotation(end_index=18797, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJfB-KcP9xszUtmECWw13DCKE5Gdno6cNEQACp7uKapMiqscClkVSVaa1pABXPP31O-l8DpR2tcGII5RVzHPBzquhAcwFooUVXRoBne-unMYVm4L4ruvw-AJYmdxU=', start_index=18788)
Annotation(end_index=18867, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFUt2jImE--ubRDlQHs8axiV0FlFk3J-nVpwRyvZLWfedyiE1Kl-LPL6SQ4l5kU4-Y2YoSEhObiEib0jZsHGYs9DQ8WTlefDKcPCaudR3WjWeM4wCAmZNE0esBAw_vNqXo5X3qvKP9pcbmJkjQPfHmsIGLVr3aQAykTLvgH9rmRO6lOOB_jKHNLn1v4hnKY0HT4CEQq8bGUb9hp0c__fDa1KcM3fKJSnG8=', start_index=18857)
Annotation(end_index=18922, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkmK-2UBAD8d8dU36n31cSEM9_oXTC8SFsU56XW9MXQdMSuPG8sD6ZzdZSLM6v2RUjLkxEbjBfFt6mDQgjlaxHzkAFSsyeSuNTlr7DSgVELSuV4h5HkfxntT6M3mhnyisC1JuiKyEjH8Aru6gpcE5GOeeRa26G5Z__W1v2oaGQTpoLq2Vl8oKlbk8IrYRM6kaxUuktRqRquLwcqzI6E269', start_index=18912)
Annotation(end_index=18994, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGJcn61b3sSG8g8UVSsUTdRaanv8zJmZ0CSzUghoPndFXMk1vOUYKDTs0eiJxdqAGH3Ho8yAeLUGMt_SE9Ms4RH3d7u0BRWedAEC5GPnr8NXkjxDfsD7G-rxgPVYA==', start_index=18984)
Annotation(end_index=19052, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHpJ6XWmXNe9H8LXlztTbtdufEL0T8UOek6KQ6EhBN4QX81CiSx42IInqRPkKAgfVKzBYXaEXntHMQ_B4s3OI-XLG3L8DUtAG8pqn4YqmLUctkaqZpvApKxiI_FZFPdIsG5Cl9Yy0GvUYjGPGmnkb9jZWE1xUVED8aPkflxemzTzy8LxEUrtqHKjh2kkxGQTPp3IJ4pAu3wo-2gQ5LZL_DnTb2RD8PHQ_qVYWqLk8CAHFOttrChmkY=', start_index=19042)
Annotation(end_index=19125, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEzM7eQfyvCaMvD_UJGTNlQyq2enM7EgQRdOZuu8oESGYp5oGyLAdYLd2nrYWoF-ZYKrvyAzHOd_LmHOuICLifgUO9gmHs0HCO4PiRhIwHBfb77jp7PcC4KFH5pnanT5Q==', start_index=19115)
Annotation(end_index=19185, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2lRjbJ_jbeAy8vezRoMJiMXopJFnelGbmCS6aJxjvUyWv6tY8Ix4kZ-UVKy4j3nfLywMkkhegBF1P2dFyViFg1JiCdH-_S-N38nfPINC0hj9pLnrlTu4x4WkWYBzgl6q4uZLFLcQhhOYJtW0F12VACdY3KzSaQ79MfpRlTtieibFCMtJ8-vR2huqh6L9qd0Gf5JR35EfTmMPTLaOd1ElFmRSIqmWsgDaHHn-DJS7q72hN6X3UErU3KKS4GK45cxMUtqQeSSRQPbQMOqL0RQVREA==', start_index=19175)
Annotation(end_index=19255, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHtkIf4AealfhdYDK1bs-sRK8TbEWL12t9quvnnZnzrkO3AEeR0CxgV2B9zVpUOVbvrm2O6xD4iAT9-g5pWhrlEdi77yjG0sUt4cwl_zB81vpO9vEW7ZA7u3lspbgVu', start_index=19245)
Annotation(end_index=19326, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEYAK-QXnPdmjSZx7dimUPrctxjBIo4CYDUJ9Fdp3v_1yVyJXFnpzveEQaedao1xrB9qloZaeg5jacVL7Ixvs-VT2722WCVBdnz7GGfhha7NNyvroYBYgXCH7rVGQ==', start_index=19316)
Annotation(end_index=19392, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCfgt_cqc7q-ePj34yTElJLxe19jGWMISgmbxpuBcMvWGS-ll88iWXk7DY9FREFZSAVodKnqMYcgID0yiWk_1pBqhULMM9Sdey2GZ6mR48OApUs26O7ec2INW7e50SNtUKBB3hQOeenR85PJdKsQA=', start_index=19382)
Annotation(end_index=19441, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJfB-KcP9xszUtmECWw13DCKE5Gdno6cNEQACp7uKapMiqscClkVSVaa1pABXPP31O-l8DpR2tcGII5RVzHPBzquhAcwFooUVXRoBne-unMYVm4L4ruvw-AJYmdxU=', start_index=19432)
Annotation(end_index=19510, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFON8Br6r9TFplBsF4KJzA4hFMhGRL4vI2R7qlG0CHi2fN91_Hob4iAU43QtT8Hl0zIaNfqDF9K4W4hxfuZ9VhbM4PdhjxAHoxXNcYyEhYntLfkPHCg0hNgodT3iw==', start_index=19501)
Annotation(end_index=19560, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3AEs5UkrINdA-Zr9rJO-oQkoFM84e2e0iyulm4UtJfeNswj59H4uKJ7137SYgoeAtkmp1QXzvZrHxHp4cpyzhxZi9fAkXg1Vtz9qTdD43zO9fPrbDAtLrYLM9ehEYgiA4W__ZCr01S8-ac7AmYbnNEW50cj2u31Qh1n_2R1pYpZFD_f_ti2OPxwIV3S8EvMUpV39Srsslft18t061Wzdd_hQ2T-_qluG1', start_index=19550)
Annotation(end_index=19625, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjLt8j91l9Hx7e9ptYJAl6KdY_akaRBaCxRz4A9_G6VG_h9odbb7fvs15e8DC1zsERoMzIF3jL3QPCXZR4FEg50IkZY1foIbSvqqimU91Ku_uvuCwLnrIIqsIgT80=', start_index=19616)
Annotation(end_index=19695, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbsGI5i1J7PBg9QbPqhpEcI6hFsljEF75jKszC8bHAs2tNv3d9uAuF100hs1ORTSEpMluBaoQEPaXopF1jB-7tEhQpn5hQQiqjQZs-C13a6cvldG7XqGIHZMsEJDgPcvzPdh6vUCFvyA==', start_index=19686)
Annotation(end_index=19760, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQECaFAJOCBWE1iapKcFNcCdnTzN-I2ufEDHbiejiGRuEtXgRcbVRIIgyFL1A7YDbXaqGmGXosrZieRsMNCSf1Rtp44JkQ4OchAXc-HGfcGvf1omvq7nAjcoHw==', start_index=19750)
Annotation(end_index=19820, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFh1TR98uA8L9L8h9z73RGcdYhTKPxDpyavA9X2l5cnL1IBY3V7vBAS2UBVBSpk5NQUGalEe-Ns1B9oMHJSgP0ogccOEKlwLfVEzlWOGxBsN8wH0wMnijRD7w==', start_index=19810)
Annotation(end_index=19858, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGisqdX1z2xbmQj3z8sU7oehs8haY73F9C5Dsg0QKBKCA0lvDLq6lGPqjINXgYYaS3TufzFWYOntsUl7q3Udbky9FiXOWrolYvVyL62qjLTQt4Lpc0V2lJoArbcDyAWiPi2N-98RB-t3Jc-eOGHQ46nzmONW7KhO1Q6jTTpgFgWHPS_UHNDhV5QjtmcpTP6', start_index=19848)
Annotation(end_index=19915, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJfB-KcP9xszUtmECWw13DCKE5Gdno6cNEQACp7uKapMiqscClkVSVaa1pABXPP31O-l8DpR2tcGII5RVzHPBzquhAcwFooUVXRoBne-unMYVm4L4ruvw-AJYmdxU=', start_index=19906)
Annotation(end_index=19967, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoaTeAHouQOLRf_sDc6xH1t2eqX26v-j-E3Vsr8NY1DuhMHcohAcAQvGwX_ZdYQYVnwmPud0VVSiVhgFdM-SDOHKx1fM-dghPm7a1twgeCIEh18UuasqpMQJQG3zLI3g==', start_index=19957)
Annotation(end_index=20016, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7FvHLYyCwMIE9G9J6k3NGxjofdOImedvseRxeSqJH9NXUtLX5ECZKGhRg1Cd5JsR-rfsSbEBKPxpCdMTvP7awhnwxyudv4dbhghicllvtgHm2ywg5zzbFgbmlvQ==', start_index=20006)
Annotation(end_index=20062, source='https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFovF8mqgGkcjIK0BNoBDjnHekAmBQuIiUiEGWw2Gvjgqa_MA24ubHki5LX3dYz6b358LiFbJU3BoP-LKdXulA68Rnajqm9V804nyf_3QMxxPQ64OKVIkJmGGSrht-ymfA1rc8p0qtHaFa8MvkgmMn41NwxVC9rKkqdvtNASz8zqTv_S2FqJpub8i7I3XIi3LUFKtzsLA5baKcpMr9JASjHjNLlTQXLt1oi7l9-8Ke4Bms6wx9q8ktaWfS67bw=', start_index=20052)

## Sources
