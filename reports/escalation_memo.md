**MEMORANDUM**

**TO:** Chief Risk Officer
**FROM:** AI Compliance Analysis Team
**DATE:** [Current Date]
**RE:** DEPLOYMENT BLOCK — COMPAS v1.0 Recidivism Model

---

**DECISION: MODEL MUST NOT BE DEPLOYED**

**Specific Breaches Identified:**
COMPAS v1.0 violates three regulatory frameworks across the African-American cohort (n=3,175):

1. **EU AI Act violation:** Disparate Impact Ratio of 1.74x exceeds governance threshold (≤1.25x)
2. **NIST AI RMF violation:** False Positive Rate of 42.3% exceeds 15.0pp differential threshold versus Caucasian baseline (22.0%)
3. **4/5ths Rule violation:** Approval ratio of 0.80 approaches non-compliance boundary

**Most Severely Affected Group & Real-World Consequence:**
African-American defendants face 74% higher false positive rates for recidivism prediction. Operationally, this produces unjust pretrial detention, bail recommendations, and sentencing enhancements affecting 3,175+ individuals in the dataset cohort alone—perpetuating systemic criminal justice bias.

**Required Actions Before Redeployment:**

1. Conduct root-cause analysis of training dataset composition and feature engineering
2. Implement stratified fairness retraining with group parity constraints (DIR ≤1.25x, FPR/FNR gaps ≤15.0pp)
3. Establish independent external audit (non-vendor)
4. Develop group-specific performance monitoring dashboards with real-time alerts
5. Obtain legal review confirming compliance with all applicable jurisdictions

**Redeployment requires CRO sign-off post-remediation.**