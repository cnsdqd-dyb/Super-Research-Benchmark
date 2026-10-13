# Deep Research Report: moonshot/kimi-k2-turbo-preview-web-search
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 5f414d7d | **Time:** 14.98s | **Cost:** $0.02350
--------------------------------------------------------------------------------

Under **random arrival patterns**, the **green wave phase offset** has a **limited and often detrimental effect** on **intersection capacity distribution**. Here's why:

---

### 🔍 Key Effects of Green Wave Phase Offset Under Random Arrivals:

#### 1. **Reduced Effectiveness of Coordination**
- Green wave coordination assumes **platooned arrivals**—vehicles arriving in clusters due to upstream signals.
- With **random arrivals**, this assumption breaks down. Vehicles arrive **independently**, not in platoons, so the **offset timing becomes misaligned** with actual traffic flow.
- As a result, **vehicles are less likely to arrive during the green phase**, reducing **green time utilization**.

#### 2. **Uneven Capacity Distribution Across Intersections**
- The **offset is optimized for a specific direction and speed**, often favoring **through traffic** on a main corridor.
- Under random arrivals, **side-street and turning movements** may experience **increased delay** and **reduced effective capacity**, as the coordination does not account for their stochastic nature.
- This leads to **imbalanced capacity allocation**, where **mainline intersections may be underutilized** while **cross-streets are oversaturated**.

#### 3. **Increased Variability in Delay and Queue Length**
- Random arrivals introduce **higher variance** in vehicle arrival times.
- A fixed offset cannot adapt to this variability, leading to **inconsistent queue lengths** and **unpredictable delays**, especially at **downstream intersections**.
- This **destabilizes flow** and can **reduce overall network throughput**.

#### 4. **Minimal Impact on Overflow Delay**
- According to TRANSYT and HCM models, **phase offset primarily affects deterministic delay** (i.e., delay due to poor progression).
- **Overflow delay** (due to oversaturation) is **largely unaffected by offset**, and under random arrivals, **overflow becomes more dominant**, further diminishing the offset’s relevance.

---

### ✅ Summary:
> **Under random arrival patterns, green wave phase offset has little to no positive effect on intersection capacity distribution.** It may even **worsen performance** by misallocating green time, increasing delays for non-coordinated movements, and failing to adapt to stochastic traffic behavior. In such cases, **adaptive or actuated control strategies** are far more effective than fixed green wave offsets.

## Annotations


## Sources
