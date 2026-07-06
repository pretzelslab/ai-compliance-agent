**MEMORANDUM**

TO: Chief Risk Officer
FROM: AI Compliance Analysis
DATE: [Current Date]
RE: DEPLOYMENT BLOCK — COMPAS v1.0 Criminal Justice Model
CLASSIFICATION: URGENT

---

**DEPLOYMENT STATUS: DO NOT DEPLOY**

**Specific Regulatory Breaches:**
COMPAS v1.0 violates three critical compliance standards:
- EU AI Act: African-American disparity index of 1.74x exceeds 1.25x threshold by 39%
- NIST FPR threshold: African-American false positive rate of 42.3% exceeds acceptable gap by 27.3 percentage points
- US 4/5ths Rule: African-American approval ratio fails proportionality assessment

**Severely Affected Population & Real-World Consequence:**
African-American defendants (n=3,175, 52% of dataset) face disproportionate false positive rates of 42.3%. This generates 1.92x more erroneous high-risk classifications, directly increasing pretrial detention rates, bail amounts, and sentencing severity for this protected group—perpetuating systemic criminal justice bias.

**Required Actions Before Redeployment:**
1. Conduct bias audit identifying root causal factors in training data (historical sentencing disparities)
2. Implement stratified rebalancing or fairness-constrained retraining to reduce African-American FPR below 27.3%
3. Achieve EU AI Act DIR ≤1.25x and NIST thresholds across all demographic groups
4. Obtain independent third-party validation before recertification
5. Establish continuous monitoring protocols for ongoing disparity detection

**Recommendation:** Suspend use immediately pending remediation.