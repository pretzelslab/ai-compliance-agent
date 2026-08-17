**MEMORANDUM**

**TO:** Chief Risk Officer
**FROM:** AI Compliance Analysis
**DATE:** [Current Date]
**RE:** DEPLOYMENT BLOCK — COMPAS v1.0 Recidivism Model
**CLASSIFICATION:** DOUBLE-CRITICAL

---

**DEPLOYMENT STATUS: DO NOT DEPLOY**

**Specific Breaches Identified:**
COMPAS v1.0 violates three regulatory frameworks:
- EU AI Act: Disparate Impact Ratio (DIR) of 1.74x for African-American cohort exceeds 1.25x threshold
- NIST FPR Standard: 42.3% false positive rate for African-American cohort exceeds 15.0pp maximum gap
- US 4/5ths Rule: African-American approval differential fails proportionality requirement

**Most Severely Affected Group & Real-World Consequence:**
African-American defendants (n=3,175) face 1.74x higher algorithmic bias risk. **Real-world consequence:** Systematically elevated false incarceration recommendations, perpetuating discriminatory criminal justice outcomes and civil rights violations.

**Required Actions Before Redeployment:**

1. **Algorithmic remediation:** Retrain model with fairness constraints; target DIR ≤1.25x and FPR gap ≤15.0pp for all groups
2. **Independent third-party audit:** Validate compliance across all regulatory frameworks
3. **Stakeholder review:** Obtain approval from criminal justice equity advocates and legal counsel
4. **Deployment safeguards:** Implement human-in-loop review for all high-risk recommendations

**Status:** Model remains blocked pending remediation completion and re-audit.