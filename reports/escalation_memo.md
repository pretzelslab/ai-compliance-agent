**MEMORANDUM**

TO: Chief Risk Officer
FROM: AI Compliance Analysis
DATE: [Current Date]
RE: DEPLOYMENT BLOCK — COMPAS v1.0 Recidivism Model

**DEPLOYMENT STATUS: BLOCKED**

**Specific Regulatory Breaches:**
COMPAS v1.0 fails three critical compliance frameworks:
- EU AI Act: African-American disparity index of 1.74x exceeds 1.25x threshold
- NIST FPR Standard: African-American false positive rate of 42.3% exceeds 15.0 percentage point gap
- 4/5ths Rule: African-American approval ratio of 1.0x fails proportionality requirement

**Most Severely Affected Population:**
African-American defendants (n=3,175) face 1.74x elevated risk classification errors. Real-world consequence: systematic over-prediction of recidivism exposure results in disparate incarceration recommendations, violating equal protection principles and amplifying systemic bias in criminal sentencing.

**Required Actions Before Redeployment:**

1. **Algorithmic Remediation**: Retrain with bias-mitigation techniques; validate FPR/FNR parity across racial groups to ≤15.0pp gaps
2. **Dataset Audit**: Investigate 6,130-record dataset for representativeness and historical bias encoding
3. **Third-Party Validation**: Independent audit by DOJ-approved vendor
4. **Governance Framework**: Establish human-in-the-loop review for high-risk classifications
5. **Documentation**: Complete impact assessment per EU AI Act Article 6

**Recommendation**: Do not deploy until DIR ≤1.25x and performance gaps close to acceptable thresholds.