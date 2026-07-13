**MEMORANDUM**

**TO:** Chief Risk Officer
**FROM:** AI Compliance Analysis
**DATE:** [Current Date]
**RE:** DEPLOYMENT BLOCK — COMPAS v1.0 Recidivism Model
**CLASSIFICATION:** DOUBLE-CRITICAL

---

**DEPLOYMENT STATUS: DO NOT DEPLOY**

**Specific Breaches Identified:**
COMPAS v1.0 violates three regulatory frameworks across the dataset (n=6,130):

1. **EU AI Act violation:** African-American cohort exhibits Disparate Impact Ratio of 1.74x (threshold: ≤1.25x)
2. **NIST FPR standard violation:** African-American False Positive Rate of 42.3% exceeds threshold by 27.3 percentage points (threshold: ≤15.0pp gap)
3. **US 4/5ths Rule violation:** Hispanic approval ratio 0.84x approaches failure threshold (minimum: ≥0.8x)

**Most Severely Affected Group:**
African-American defendants (n=3,175, 51.8% of dataset) face systematic misclassification. The 1.74x DIR combined with 42.3% FPR means innocent defendants are flagged for incarceration at substantially elevated rates, directly increasing wrongful detention risk.

**Required Actions Before Redeployment:**

1. Conduct root-cause analysis of training data bias (disparate sampling, historical label bias)
2. Implement stratified fairness constraints achieving <1.25x DIR across all groups
3. Revalidate against all three regulatory standards on holdout test set
4. Obtain independent third-party audit certification
5. Establish continuous monitoring with quarterly fairness reporting

**Recommendation:** Suspend all criminal justice deployments pending remediation.