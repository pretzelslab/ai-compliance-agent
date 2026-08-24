**MEMORANDUM**

**TO:** Chief Risk Officer
**FROM:** AI Compliance Analysis
**DATE:** [Current Date]
**RE:** DEPLOYMENT BLOCK — COMPAS v1.0 Recidivism Model
**CLASSIFICATION:** DOUBLE-CRITICAL

---

**DEPLOYMENT DECISION: DO NOT DEPLOY**

COMPAS v1.0 fails compliance requirements across multiple regulatory frameworks:

- **EU AI Act violation**: African-American disparity index (1.74x) exceeds maximum threshold (1.25x)
- **NIST FPR breach**: African-American false positive rate (42.3%) exceeds threshold by 27.3 percentage points
- **Statistical parity failure**: 4/5ths rule breached across three demographic groups

**MOST SEVERELY AFFECTED GROUP: African-American defendants (n=3,175)**

**Real-world consequence**: 42.3% false positive rate means approximately 1,343 individuals incorrectly flagged as high recidivism risk, directly influencing bail, sentencing, and parole decisions with documented disparate impact on criminal justice outcomes.

**REQUIRED ACTIONS BEFORE REDEPLOYMENT:**

1. Conduct causal analysis of 1.74x disparity in African-American cohort
2. Retrain on balanced, representative datasets (n≥10,000 per demographic)
3. Implement fairness constraints (DIR ≤1.10x, FPR gap ≤10pp)
4. Conduct external validation audit with civil rights organizations
5. Establish bias monitoring framework with quarterly audits

Redeployment prohibited until all items completed and re-audited.