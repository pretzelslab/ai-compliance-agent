**MEMORANDUM**

**TO:** Chief Risk Officer
**FROM:** AI Compliance Analysis Team
**DATE:** [Current Date]
**RE:** DEPLOYMENT BLOCK — COMPAS v1.0 Recidivism Model

---

**RECOMMENDATION: DO NOT DEPLOY**

**Specific Regulatory Breaches:**
COMPAS v1.0 violates three compliance frameworks:
- **EU AI Act:** African-American cohort demonstrates disparate impact ratio of 1.74x (threshold: ≤1.25x)
- **NIST Standards:** False positive rate disparity of 20.3 percentage points vs. Caucasian baseline (threshold: ≤15.0pp)
- **4/5ths Rule:** African-American approval ratio of 0.62 vs. majority group (threshold: ≥0.80)

**Disproportionately Affected Population:**
African-American defendants (n=3,175) face the severest harm. With FPR at 42.3%, the model generates false positive flags in nearly 1 of 2 cases, systematically misidentifying recidivism risk. Real-world consequence: increased pretrial detention, bail denials, and sentencing enhancements for an already over-represented population in criminal justice systems.

**Required Actions Before Redeployment:**
1. Conduct root-cause analysis of training data bias (n=6,130 dataset composition)
2. Implement stratified rebalancing and fairness-constrained model retraining
3. Establish independent algorithmic audit confirming all thresholds met across all groups
4. Develop demographic-specific validation protocols
5. Obtain legal sign-off from General Counsel

**Status:** BLOCKED pending completion of above remediation.