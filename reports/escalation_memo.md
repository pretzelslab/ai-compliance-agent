**MEMORANDUM**

**TO:** Chief Risk Officer
**FROM:** AI Compliance Analysis
**DATE:** [Current Date]
**RE:** DEPLOYMENT BLOCK — COMPAS v1.0 | Criminal Justice Domain
**PRIORITY:** DOUBLE-CRITICAL

---

**DEPLOYMENT STATUS: BLOCKED**

COMPAS v1.0 must not be deployed. The model breaches three regulatory frameworks:

1. **EU AI Act violation** — African-American disparity index (DIR) of 1.74x exceeds 1.25x threshold by 39.2%
2. **NIST FPR standard failure** — African-American false positive rate (42.3%) exceeds threshold by 27.3 percentage points
3. **US 4/5ths rule violation** — African-American approval ratio of 1.74x indicates discriminatory impact

**MOST SEVERELY AFFECTED GROUP & CONSEQUENCE**

African-American defendants (n=3,175) face disproportionate risk classification. Real-world consequence: 42.3% false positive rate means approximately 1,341 individuals falsely flagged as high-risk, directly affecting bail decisions, sentencing recommendations, and parole eligibility—compounding systemic incarceration disparities.

**REQUIRED REMEDIATION ACTIONS**

Before redeployment:
- Conduct bias audit with domain experts to identify training data sources driving 1.74x disparity
- Rebalance dataset or implement fairness constraints reducing DIR to ≤1.25x
- Validate FPR parity across all groups (≤15pp gaps)
- Obtain independent third-party audit certification
- Establish post-deployment monitoring dashboards for ongoing fairness metrics

**No deployment timeline established pending corrective completion.**