**MEMORANDUM**

**TO:** Chief Risk Officer
**FROM:** AI Compliance Analysis
**DATE:** [DATE]
**RE:** DEPLOYMENT BLOCK — COMPAS v1.0 Recidivism Model
**CLASSIFICATION:** DOUBLE-CRITICAL

---

**DEPLOYMENT DECISION: DO NOT DEPLOY**

**Specific Breaches Identified:**
COMPAS v1.0 violates EU AI Act and NIST standards across critical thresholds:
- Disparate Impact Ratio (DIR): African-American cohort at 1.74x (threshold: ≤1.25x)
- False Positive Rate gap: 42.3% vs. 22.0% baseline (+20.3pp; threshold: ≤15.0pp)
- False Negative Rate gaps: Caucasian cohort at 49.6% (threshold: ≤15.0pp)

**Most Severely Affected Group:**
African-American defendants (n=3,175, 51.8% of dataset) face disproportionately higher misclassification as high-risk (42.3% false positive rate). **Real-world consequence:** Unnecessary pretrial detention, bail enhancement, or sentence severity recommendations for individuals who would not reoffend, perpetuating systemic criminal justice inequities.

**Required Actions Before Redeployment:**

1. **Algorithmic remediation:** Retrain with fairness constraints enforcing DIR ≤1.25x and FPR/FNR gaps ≤15.0pp across all demographic groups
2. **Dataset audit:** Investigate historical labeling bias in recidivism outcomes (n=6,130); ensure representative, debiased data
3. **Validation testing:** Independent third-party fairness certification across all subgroups
4. **Stakeholder consultation:** Engage affected communities and criminal justice practitioners
5. **Governance review:** Establish human-in-the-loop oversight before any criminal justice deployment

**Redeployment prohibited until all actions completed and re-audited.**