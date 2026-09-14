**MEMORANDUM**

**TO:** Chief Risk Officer
**FROM:** Compliance Analytics
**DATE:** [Current Date]
**RE:** DEPLOYMENT BLOCK — COMPAS v1.0 Recidivism Model

---

**DEPLOYMENT STATUS: PROHIBITED**

COMPAS v1.0 fails critical compliance thresholds and must not be deployed.

**Specific Breaches:**
- Disparate Impact Ratio (African-American): 1.74x versus 1.25x threshold — **174% violation magnitude**
- False Positive Rate gap: 42.3% (African-American) vs. 22.0% (Caucasian) — **20.3 percentage point breach** of 15.0pp ceiling
- EU AI Act high-risk classification violated; NIST AI RMF benchmarks exceeded

**Most Severely Affected Population & Real-World Consequence:**
African-American defendants (n=3,175, 52% of dataset) face 1.74x higher false positive rates, resulting in systematically inflated recidivism risk scores. Real consequence: overestimation of re-offense risk drives disproportionate detention decisions, longer sentences, and bail denial — perpetuating carceral disparity in a protected-class population.

**Required Actions Before Redeployment:**

1. Conduct root-cause analysis of training data (n=6,130) for historical bias encoding
2. Implement stratified rebalancing; retrain with fairness constraints (DIR ≤1.25x across all groups)
3. Establish independent validation against NIST thresholds (FPR/FNR gaps ≤15pp)
4. Obtain legal review confirming EU AI Act and 4/5ths rule compliance
5. Establish ongoing monitoring dashboard with quarterly audit cycles

**Redeployment blocked until all conditions satisfied.**