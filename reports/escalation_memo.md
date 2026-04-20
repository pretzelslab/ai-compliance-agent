**MEMORANDUM**

**TO:** Chief Risk Officer
**FROM:** AI Compliance Analysis Team
**DATE:** [Current Date]
**RE:** DEPLOYMENT BLOCK — COMPAS v1.0 Recidivism Model

---

**DEPLOYMENT STATUS: BLOCKED**

**Specific Regulatory Breaches:**
COMPAS v1.0 fails two critical compliance thresholds:
- **EU AI Act violation:** African-American disparity index = 1.74x (threshold: ≤1.25x)
- **NIST FPR requirement:** African-American false positive rate = 42.3% vs. Caucasian 22.0% (27.3pp gap; threshold: ≤15.0pp)

**Most Severely Affected Group & Real-World Consequence:**
African-American defendants (n=3,175) face 1.74x higher risk scores despite equivalent actual recidivism. Consequence: systematic false detention recommendations, compounding historical disparities in criminal justice and violating due process protections.

**Required Actions Before Redeployment:**

1. **Conduct bias root-cause analysis** — examine training data composition and feature engineering for discriminatory proxies
2. **Retrain with fairness constraints** — implement demographic parity or equalized odds optimization
3. **Validate on holdout test set** — ensure DIR <1.25x and FPR gap <15.0pp across all groups
4. **Independent third-party audit** — verify EU AI Act and NIST compliance
5. **Legal review** — assess civil rights liability exposure

**Recommendation:** Do not deploy until all requirements satisfied. Consider alternative vendor solutions.