**MEMORANDUM**

TO: Chief Risk Officer
FROM: AI Compliance Analysis
DATE: [Current Date]
RE: DEPLOYMENT BLOCK — COMPAS v1.0 Recidivism Model

---

**DEPLOYMENT PROHIBITION**

COMPAS v1.0 is **NOT APPROVED for deployment**. The model breaches:
- EU AI Act (high-risk classification; prohibited disparate impact)
- NIST AI Risk Management Framework (FPR/FNR thresholds exceeded)
- Internal governance standards (DIR threshold 1.25x; model achieves 1.74x)

**PRIMARY AFFECTED GROUP & CONSEQUENCE**

African-American defendants (n=3,175, 52% of dataset) face **DOUBLE-CRITICAL severity** exposure:
- False Positive Rate: 42.3% (19.3 percentage points above threshold)
- Disparity Ratio: 1.74x baseline (39% above acceptable threshold)

**Real-world consequence**: Systematic over-flagging of African-American defendants for high-risk classification, resulting in disproportionate bail denial, sentencing enhancement, and incarceration—directly contradicting equal protection principles.

**REQUIRED REMEDIATION BEFORE REDEPLOYMENT**

1. Conduct bias audit identifying root causes (feature engineering, sampling bias, label bias)
2. Retrain using balanced sampling and fairness constraints (achieve DIR ≤1.25x across all groups)
3. Validate FPR/FNR parity (≤15.0pp gaps across racial groups)
4. Engage external auditor for independent verification
5. Establish ongoing monitoring protocols

**Redeployment prohibited until all remediation items verified.**