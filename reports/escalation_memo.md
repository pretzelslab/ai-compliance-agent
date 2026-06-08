**MEMORANDUM**

**TO:** Chief Risk Officer
**FROM:** AI Compliance Analysis
**DATE:** [Current Date]
**RE:** DEPLOYMENT BLOCK — COMPAS v1.0 Recidivism Model

---

**DEPLOYMENT STATUS: BLOCKED**

**Specific Regulatory Breaches:**
COMPAS v1.0 violates EU AI Act disparate impact thresholds and NIST fairness standards. African-American defendants (n=3,175) experience a disparate impact ratio of 1.74x—exceeding the 1.25x EU threshold by 39%. False positive rate disparity reaches 42.3% versus 22.0% for Caucasian defendants (20.3pp gap; NIST limit: 15.0pp).

**Most Severely Affected Group & Real-World Consequence:**
African-American defendants face 1.74 times higher risk classification. This systematically inflates recidivism predictions, directly increasing pretrial detention, bail amounts, and sentencing recommendations—compounding systemic criminal justice inequities affecting 3,175 individuals in deployment scope.

**Required Actions Before Redeployment:**

1. Conduct root-cause analysis of training data representativeness and labeling bias
2. Retrain model with demographic parity constraints or threshold adjustment protocols
3. Implement stratified validation demonstrating DIR ≤1.25x and FPR gaps ≤15.0pp across all protected groups
4. Establish ongoing monitoring with quarterly fairness audits
5. Obtain Legal and Ethics review before any pilot deployment

**Status:** Hold pending remediation.