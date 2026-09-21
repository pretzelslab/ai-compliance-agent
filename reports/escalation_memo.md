**MEMORANDUM**

**TO:** Chief Risk Officer
**FROM:** AI Compliance Analysis
**DATE:** [Current Date]
**RE:** DEPLOYMENT BLOCK — COMPAS v1.0 | Criminal Justice Domain

---

**DECISION: DO NOT DEPLOY**

**Specific Breaches Identified:**
COMPAS v1.0 violates three regulatory frameworks across critical thresholds:
- **EU AI ACT violation:** Disparate Impact Ratio (DIR) for African-American cohort = 1.74x (threshold: ≤1.25x)
- **NIST FPR breach:** False Positive Rate gap = +27.3 percentage points vs. Caucasian baseline (threshold: ≤15.0pp)
- **4/5ths Rule violation:** African-American approval ratio = 0.80x (threshold: ≥0.80x, marginal fail)

**Most Severely Affected Group & Real-World Consequence:**
African-American defendants (n=3,175, 51.8% of sample) face 1.74x higher likelihood of false recidivism flags. Real-world impact: incorrect detention recommendations, prolonged incarceration, bail denial, and compounded criminal justice bias.

**Required Actions Before Redeployment:**

1. **Root cause analysis** — audit training data for historical bias (n=6,130 dataset composition review)
2. **Algorithmic remediation** — retrain with fairness constraints targeting DIR ≤1.25x and FPR/FNR gaps ≤15.0pp across all groups
3. **Independent validation** — third-party audit on balanced holdout set (minimum n=2,000 per demographic)
4. **Governance approval** — documented sign-off from Legal, Ethics Board, and CRO before production consideration

**Current deployment poses unacceptable legal and reputational risk.**