**MEMORANDUM**

TO: Chief Risk Officer
FROM: AI Compliance Analytics
DATE: [Current Date]
RE: DEPLOYMENT BLOCK — COMPAS v1.0 Criminal Justice Model

**DECISION: DO NOT DEPLOY**

**Specific Breaches Identified:**
COMPAS v1.0 fails three regulatory frameworks across n=6,130 records:
- **EU AI Act violation**: African-American disparity ratio of 1.74x exceeds 1.25x threshold
- **NIST FPR standard**: African-American false positive rate of 42.3% exceeds 15.0pp gap limit
- **US 4/5ths rule**: African-American approval ratio of 1.74x fails proportionality requirement

**Most Severely Affected Group & Consequence:**
African-American defendants (n=3,175) face 1.74× higher recidivism prediction rates with 42.3% false positives. Real-world consequence: systematic overestimation of risk driving inequitable bail decisions, sentence recommendations, and parole denials—perpetuating criminal justice disparities.

**Required Actions Before Redeployment:**

1. **Audit dataset composition** for sampling bias and historical discrimination encoding
2. **Implement fairness constraints** achieving DIR ≤1.25x and FPR gap ≤15.0pp across all groups
3. **Retrain with balanced methodology** or deploy alternative validated model
4. **Conduct external validation** on independent test set (n≥2,000 per demographic)
5. **Establish continuous monitoring** with quarterly disparity reporting
6. **Legal review** for Title VI/14th Amendment compliance before any deployment

**Deployment blocked indefinitely pending corrective completion.**