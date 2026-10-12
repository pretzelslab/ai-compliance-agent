**MEMORANDUM**

**TO:** Chief Risk Officer
**FROM:** AI Compliance Analysis
**DATE:** [Current Date]
**RE:** DEPLOYMENT BLOCK — COMPAS v1.0 Recidivism Model

---

**DEPLOYMENT STATUS: BLOCKED**

COMPAS v1.0 fails critical compliance requirements and must not be deployed.

**Specific Breaches:**
- African-American cohort (n=3,175): Disparate Impact Ratio of 1.74x exceeds 1.25x governance threshold by 39%
- False Positive Rate disparity: 42.3% vs. 22.0% baseline — exceeds 15.0pp threshold by 27.3pp
- Violates EU AI Act high-risk standards and NIST fairness benchmarks

**Severely Affected Group:**
African-American defendants face disproportionate false positive classifications (42.3%). Real-world consequence: over-flagged individuals receive elevated risk designations, directly influencing parole decisions, bail recommendations, and sentencing considerations — perpetuating systemic incarceration disparities.

**Required Pre-Redeployment Actions:**
1. Conduct root-cause analysis of training data bias (ProPublica dataset, n=6,130)
2. Implement stratified retraining with balanced demographic representation
3. Establish hard constraints: DIR ≤1.25x, FPR disparity ≤15.0pp across all groups
4. Achieve third-party fairness audit certification
5. Establish continuous monitoring protocols with quarterly bias assessments

Redeployment prohibited until documented compliance achieved.