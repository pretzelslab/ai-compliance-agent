# COMPLIANCE REPORT: COMPAS v1.0 RECIDIVISM MODEL

## REGULATORY BREACHES

**Critical Violations:**
- **Disparate Impact Ratio (DIR)**: African-American group at 1.74x baseline—exceeds 1.25x threshold by 39%. This violates EU AI Act high-risk requirements and US adverse impact standards.
- **False Positive Rate (FPR)**: African-American FPR of 42.3% vs. Caucasian 22.0% = 20.3 percentage point gap, exceeding 15.0pp threshold by 35%.
- **False Negative Rate (FNR)**: Disparate patterns across all groups; Caucasian FNR (49.6%) creates inverse harm compared to African-American FNR (28.5%), indicating systematic bias directionality.

**Secondary Violations:**
- Hispanic and Other groups show extreme FNR gaps (58.2pp and 66.1pp respectively above threshold).

---

## AFFECTED GROUPS & REAL-WORLD HARM

**African-American defendants (n=3,175)**: 1.74x higher likelihood of false positive (flagged high-risk when actually low-risk), leading to over-incarceration, bail denials, and sentencing enhancements.

**Caucasian defendants (n=2,103)**: 49.6% FNR means nearly half flagged low-risk despite recidivating, creating public safety gaps and unequal accountability.

**Hispanic & Other populations (n=852)**: Extreme false negatives indicate systematic under-prediction of risk, generating inconsistent justice outcomes.

---

## REMEDIATION OPTIONS

**Option 1: Model Retraining (6-9 months)**
- Rebalance training data; implement fairness constraints (DIR ≤1.15x, FPR gap ≤8pp)
- Parallel validation testing; re-audit at 3-month intervals
- *Cost: High; Risk: Reduced predictive accuracy overall*

**Option 2: Threshold Adjustment + Human Review (3-4 months)**
- Recalibrate decision boundaries by race; implement mandatory human override for borderline cases
- Audit compliance monthly
- *Cost: Moderate; Risk: Operational delays*

**Option 3: Immediate Suspension (0 months)**
- Withdraw model pending full remediation; revert to human-only decision-making
- *Cost: Operational disruption; Risk: Litigation exposure if continued*

**Recommendation**: Option 1 + parallel Option 2 implementation to achieve compliance within 6 months while maintaining functional deployment under heightened oversight.