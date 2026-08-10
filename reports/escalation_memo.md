**MEMORANDUM**

**TO:** Chief Risk Officer
**FROM:** AI Compliance Analysis Team
**DATE:** [Current Date]
**RE:** DEPLOYMENT BLOCK — COMPAS v1.0 Recidivism Model
**CLASSIFICATION:** DOUBLE-CRITICAL

---

**DEPLOYMENT DECISION: DO NOT DEPLOY**

**Specific Breaches Identified:**

COMPAS v1.0 violates three regulatory frameworks across its dataset (n=6,130):

1. **EU AI Act violation** — African-American cohort (n=3,175) exhibits disparate impact ratio of 1.74x, exceeding the 1.25x threshold by 39%
2. **NIST FPR standard breach** — African-American false positive rate of 42.3% exceeds acceptable gap by 27.3 percentage points (threshold: ≤15.0pp)
3. **US 4/5ths Rule failure** — Hispanic approval ratio of 0.84x falls below compliance threshold

**Most Severely Affected Group & Real-World Consequence:**

African-American defendants (n=3,175) face the highest discriminatory burden. The 1.74x disparate impact combined with a 42.3% false positive rate means innocent Black defendants are flagged for enhanced monitoring at nearly 2x the rate of white counterparts, directly increasing incarceration risk and perpetuating systemic bias in criminal sentencing.

**Required Actions Before Redeployment:**

1. Conduct algorithmic fairness audit with demographic parity constraints
2. Retrain model with balanced sampling across racial groups
3. Validate that DIR ≤1.25x and FPR gaps ≤15.0pp across all cohorts
4. Obtain independent third-party certification
5. Establish ongoing bias monitoring post-deployment

**Recommendation:** Block deployment indefinitely pending comprehensive remediation.