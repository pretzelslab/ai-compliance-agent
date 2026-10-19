# COMPLIANCE REPORT: COMPAS v1.0 RECIDIVISM MODEL

**REGULATORY BREACHES**

COMPAS v1.0 critically violates multiple governance frameworks:

- **Disparate Impact Ratio (DIR)**: African-American cohort reaches 1.74x vs. 1.25x threshold—39% overage
- **False Positive Rate (FPR)**: African-American FPR of 42.3% exceeds 15.0pp threshold by 27.3 percentage points (182% above limit)
- **False Negative Rate (FNR)**: All groups breach FNR thresholds (13.5–51.1pp overages); Caucasian group most severe at 49.6%
- **4/5ths Rule**: African-American approval ratio fails equity benchmarking

**AFFECTED GROUPS & HARM**

African-Americans (n=3,175) experience systematic disadvantage: 1.74x higher likelihood of false high-risk classifications, resulting in disproportionate detention, bail denial, and sentencing enhancement. The 42.3% FPR means approximately 1,344 individuals face incorrect risk flagging.

Caucasians (n=2,103) demonstrate 49.6% FNR—approximately 1,044 genuinely high-risk individuals classified as low-risk, creating public safety gaps.

Hispanic (n=509) and Other (n=343) groups show extreme FNR (58.2%, 66.1%), suggesting systematic under-flagging despite smaller population sizes.

**REMEDIATION OPTIONS**

1. **Immediate Suspension (0–30 days)**: Halt COMPAS deployment pending independent audit. Conduct bias decomposition analysis. Timeline: 4 weeks. Cost: ~$85K. Risk: Operational disruption.

2. **Targeted Recalibration (30–120 days)**: Reweight algorithm thresholds by demographic group to achieve DIR ≤1.25x and FPR/FNR gaps ≤15pp. Implement separate fairness-optimized models per jurisdiction. Timeline: 12 weeks. Cost: ~$250K. Risk: Reduced predictive accuracy.

3. **Phased Retirement with Replacement (120–365 days)**: Transition to fairness-certified alternative models (e.g., AEQUITAS-calibrated system). Maintain human-in-loop review for African-American flagged cases. Audit quarterly. Timeline: 12 months. Cost: ~$600K. Risk: Extended deployment of non-compliant system.

**RECOMMENDATION**: Option 3 (phased retirement) balances legal obligation, stakeholder impact, and operational continuity, contingent on immediate Option 1 safeguards.