# Deep Research Report: alibaba/tongyi-deepresearch-30b-a3b
**Status:** ✅ Success | **Attempts:** 1/5 | **Run ID:** 28d486ea | **Time:** 6.19s | **Cost:** $0.00045
--------------------------------------------------------------------------------

The **similarity threshold** for substitute recommendations in shopping basket analysis isn't set by a single rule—it's determined by **contextual factors** and **business objectives**, often refined through experimentation. Key influences include:

### 1. **Business Objectives**  
   - **Sales Goals**: Pushing category expansion (e.g., suggesting premium alternatives) vs. cost-saving substitutes.  
   - **Margin Prioritization**: Thresholds may favor high-margin items over lower-priced substitutes.  
   - **Inventory Management**: Urgent need to clear stock? Lower the threshold to promote similar items.  

### 2. **Data Characteristics**  
   - **Item Similarity Metrics**:  
     - **Feature Overlap** (e.g., 80% brand compatibility + same category = lower threshold).  
     - **Price Proximity**: Items within 10–20% price range may use a tighter threshold.  
   - **Basket Composition**:  
     - *Homogeneous baskets* (e.g., milk + bread) → higher similarity tolerance.  
     - *Heterogeneous baskets* (e.g., diapers + coffee) → stricter threshold.  

### 3. **Algorithmic Parameters**  
   - **Collaborative Filtering**: User behavior (e.g., same users bought A and B) → default threshold ~70–85% similarity.  
   - **Matrix Factorization**: Latent factors (embedding similarity) → threshold tuned via precision-recall curves.  
   - **Graph-Based Models**: Topological distance in item graphs → retain edges within k-hop distance.  

### 4. **User Experience & Context**  
   - **Browse vs. Mobile**: Mobile shoppers may tolerate lower similarity (e.g., 60%) for faster decisions.  
   - **Cognitive Load**: Strict thresholds (≥90%) for complex purchases (e.g., electronics), relaxed thresholds (≥50%) for impulse buys.  

### 5. **Testing & Optimization**  
   - **A/B Testing**: Compare CTR, conversion, and average basket size with thresholds ranging from 50–95%.  
   - **Classification Models**: Supervised learning using labels like "was a substitute clicked?" refines thresholds.  
   - **Real-Time Feedback**: Regret minimization algorithms adjust thresholds based on user rejection.  

### Practical Example:  
- **Bread Substitute**:  
  - Low threshold (50–60%): Suggest baguette for *sliced bread*.  
  - High threshold (≥85%): Reserve for identical items (e.g., sourdough vs. olive sourdough).  

### Tools for Adjustment:  
- **Precision-Recall Curves**: Pick threshold balancing relevance (precision) and coverage (recall).  
- **Business Rules Engines**: Enforce constraints (e.g., exclude items within 5% of current price for cost-sensitive categories).  

**Conclusion**: The threshold is a dynamic balance between data-driven similarity metrics, pinch points in the user journey, and business strategy—requiring continuous calibration via testing (e.g., **multi-armed bandit algorithms**) to optimize for KPIs like conversion rate or average order value.

## Annotations


## Sources
