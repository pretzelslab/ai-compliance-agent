**MEMORANDUM**

**TO:** Chief Risk Officer  
**FROM:** AI Compliance Analysis  
**DATE:** [Current Date]  
**RE:** DEPLOYMENT BLOCK — COMPAS v1.0 Recidivism Model  
**CLASSIFICATION:** CRITICAL

---

**DEPLOYMENT DETERMINATION:** Model must not be deployed in production.

**REGULATORY BREACHES:**
COMPAS v1.0 violates the EU AI Act (high-risk classification) and NIST AI RMF standards across multiple fairness metrics. African-American cohort (n=3,175) exhibits disparate impact ratio of 1.74x—significantly exceeding the 1.25x threshold—with false positive rate of 42.3% (27.3 percentage points above the 15pp NIST limit).

**MOST SEVERELY AFFECTED GROUP:**
African-American individuals face 74% higher risk classification relative to Caucasian applicants. Real-world consequence: systematic overestimation of recidivism likelihood, resulting in elevated pretrial detention recommendations, longer sentences, and restricted parole eligibility for approximately 3,175 individuals annually.

**REQUIRED ACTIONS BEFORE REDEPLOYMENT:**
1. Conduct algorithmic audit identifying root causes of 1.74x disparity
2. Retrain model with fairness constraints and demographic stratification
3. Implement threshold adjustment to achieve DIR ≤ 1.25x while monitoring FPR/FNR parity
4. Obtain independent third-party validation (ProPublica methodology)
5. Establish bias monitoring dashboard for ongoing compliance tracking
6. Secure legal review and stakeholder consultation with affected communities

Redeployment prohibited until all requirements satisfied and re-audited.