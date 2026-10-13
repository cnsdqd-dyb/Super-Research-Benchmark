# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 51192197 | **Time:** 15.51s | **Cost:** $0.02439
--------------------------------------------------------------------------------

The planning strategy that best balances target dose coverage with organ-at-risk (OAR) tolerance in head-and-neck (H&N) radiotherapy—thereby maximizing local control while minimizing toxicity—is **online adaptive radiotherapy (oART)** using **intensity-modulated radiotherapy (IMRT)** with **anatomically-driven optimization and clinical goal prioritization**.

### Key Components of the Optimal Strategy:

1. **Online Adaptive Radiotherapy (oART)**  
   - **Real-time reoptimization** based on daily anatomy (e.g., tumor shrinkage, weight loss, organ motion).
   - Corrects for **target underdosing** and **OAR overdosing** that accumulates over a multi-week course.
   - Demonstrated **superior target conformality** and **reduced parotid gland dose**, improving both local control and quality of life (e.g., less xerostomia).

2. **IMRT with Fixed-Field Geometry**  
   - Preferred over VMAT in adaptive workflows due to **faster optimization** and **more stable dose distributions**.
   - Enables **steep dose gradients** between tumor and adjacent critical structures (e.g., spinal cord, brainstem, parotids).

3. **Anatomically-Driven Helper Structures**  
   - **Posterior and anterior blocks** (e.g., 9 cm lateral margin from cord/brainstem, 1.5 cm crop from oral cavity) to **steer dose away** from OARs.
   - **Cropped PTVs** and **hotspot control structures** (e.g., V105% < 5%) to **limit dose heterogeneity** and **avoid mucosal toxicity**.

4. **Clinical Goal Prioritization**  
   - **Tiered priority system**:  
     - **P1–P2**: Target coverage (PTV Dmin, V100%) and critical OARs (spinal cord, brainstem Dmax).  
     - **P3–P4**: Parallel OARs (e.g., parotid mean dose, oral cavity dose).  
   - **Minimal goal set** per OAR to **reduce optimization conflicts** and **improve plan robustness**.

5. **Density Override for Air Cavities**  
   - Manual override of air within PTV to water density to **reduce optimization-convergence errors** and **improve dose calculation accuracy**, especially in sinonasal or oropharyngeal cases.

6. **Sequential Boost (SEQ) vs. Simultaneous Integrated Boost (SIB)**  
   - **SEQ plans** are more robust and **easier to optimize** in adaptive systems.  
   - **SIB plans** benefit significantly from **online adaptation**, which corrects for initial underdosing and hotspot formation.

---

### Summary:
**Online adaptive IMRT**, using **fixed-field geometry**, **anatomically-driven helper structures**, and **prioritized clinical goals**, is the most effective strategy to **maximize tumor control** while **minimizing injury** to organs at risk in head-and-neck radiotherapy.

## Annotations


## Sources
