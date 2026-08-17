# COMPLIANCE REPORT: COMPAS v1.0 RECIDIVISM MODEL

**REGULATORY BREACHES**

The model breaches multiple critical thresholds:

1. **EU AI Act (Disparate Impact Ratio)**: African-American cohort (n=3,175) shows DIR of 1.74x against the 1.25x threshold—a **39% overage**. This represents the most severe violation across all metrics.

2. **NIST FPR Gap**: African-American false positive rate of 42.3% exceeds the allowable 15.0pp differential by **27.3 percentage points**—a **182% exceedance**.

3. **NIST FNR Gap**: Three cohorts breach thresholds—Caucasian (49.6%), Hispanic (58.2%), and Other (66.1%) populations exceed limits by 34.6pp, 43.2pp, and 51.1pp respectively.

**AFFECTED GROUPS & HARM**

- **African-Americans (n=3,175)**: 1.74x higher likelihood of false high-risk classification; 42.3% incorrectly flagged as high-risk when they are not. Real-world impact: wrongful detention, bail denials, sentencing enhancement.
- **Caucasians (n=2,103)**: 49.6% false negative rate; nearly half classified as low-risk despite recidivism, creating public safety gaps.
- **Hispanic (n=509) & Other (n=343)**: Similar FNR failures create inconsistent risk assessment reliability.

**REMEDIATION OPTIONS**

1. **Immediate Suspension (0-30 days)**: Halt COMPAS deployment pending urgent retraining with balanced datasets stratified by race. Implement manual review for all high-risk recommendations. *Timeline: 30 days.*

2. **Algorithmic Recalibration (60-120 days)**: Retrain using 50/50 demographic sampling, apply fairness constraints (Fairlearn, AI Fairness 360), and validate DIR ≤1.25x and FPR gap ≤15pp across all groups. *Timeline: 120 days.*

3. **Phased Replacement (90-180 days)**: Develop alternative model prioritizing fairness metrics; pilot with 10% caseload; conduct independent third-party validation before full deployment. Maintain human oversight indefinitely. *Timeline: 180 days.*

**Recommendation**: Option 2 (recalibration) balances urgency with thoroughness, given the criminal justice context's irreversible harms.