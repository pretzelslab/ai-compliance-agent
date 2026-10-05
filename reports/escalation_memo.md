**MEMORANDUM**

**TO:** Chief Risk Officer
**FROM:** AI Compliance Analysis Team
**DATE:** [Current Date]
**RE:** DEPLOYMENT BLOCK — COMPAS v1.0 Recidivism Model

---

**DEPLOYMENT STATUS: PROHIBITED**

COMPAS v1.0 must not be deployed. The model breaches critical regulatory and governance standards:

- **EU AI Act violation**: Disparate Impact Ratio of 1.74x for African-American cohort (n=3,175) exceeds 1.25x threshold
- **NIST FPR standard failure**: False Positive Rate gap of 20.3 percentage points (42.3% vs. 22.0%) exceeds 15.0pp threshold
- **Systemic bias**: African-American defendants face 74% elevated false positive risk

**MOST SEVERE IMPACT:**
African-American defendants (n=3,175) represent the double-critical risk group. Real-world consequence: individuals incorrectly flagged as high-recidivism risk face unjustified pretrial detention, bail elevation, or sentencing enhancement—directly perpetuating discriminatory criminal justice outcomes.

**REQUIRED ACTIONS BEFORE REDEPLOYMENT:**

1. Conduct root-cause analysis of training data bias and label definitions
2. Implement stratified model retraining with fairness constraints (DIR ≤1.25x, FPR gap ≤15.0pp)
3. Establish independent external validation across all demographic groups
4. Deploy fairness monitoring and real-world outcome tracking post-deployment
5. Obtain legal review confirming compliance with applicable civil rights statutes

**Redeployment prohibited until all metrics pass threshold requirements.**