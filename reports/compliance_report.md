# COMPLIANCE REPORT: COMPAS v1.0 RECIDIVISM MODEL

## 1. REGULATORY BREACHES

**Critical Violations:**
- **EU AI Act Disparate Impact Ratio (DIR)**: African-American cohort at 1.74x vs. 1.25x threshold—**breach of 0.49x (39% overage)**
- **NIST False Positive Rate (FPR) Gap**: African-American FPR of 42.3% vs. Caucasian 22.0%—**gap of 20.3 percentage points (pp) exceeds 15.0pp limit by 5.3pp**
- **NIST False Negative Rate (FNR) Gap**: All non-African-American groups exceed threshold; Caucasian FNR of 49.6% vs. African-American 28.5%—**gap of 21.1pp exceeds limit by 6.1pp**

## 2. AFFECTED GROUPS & HARM

- **African-American defendants (n=3,175)**: 1.74x higher risk of false positive detention decisions; 42.3% wrongly flagged as high-risk, resulting in elevated incarceration recommendations and bail denial
- **Caucasian defendants (n=2,103)**: 49.6% false negative rate masks actual recidivism risk, enabling release of potentially dangerous individuals
- **Hispanic & Other groups (n=852)**: Compounded errors across both FPR/FNR dimensions; systemic underprediction of risk creates inconsistent justice outcomes

**Real-world impact**: Systematic over-detention of African-Americans and under-detection of risk across populations undermines due process and equal protection.

## 3. REMEDIATION OPTIONS

**Option A—Immediate Suspension (0-30 days)**
Halt COMPAS deployment pending algorithmic audit. Conduct fairness-aware retraining using stratified sampling to equalize FPR/FNR across racial groups.
- *Timeline*: 90 days
- *Cost*: Moderate; requires model revalidation

**Option B—Threshold Recalibration (30-60 days)**
Apply race-aware decision thresholds to bring disparate impact within 1.25x and FPR/FNR gaps below 15.0pp without model retraining.
- *Timeline*: 45 days
- *Cost*: Low; maintains existing infrastructure

**Option C—Human-in-Loop Governance (60-90 days)**
Deploy model with mandatory human review override for African-American defendants flagged as high-risk; audit all recommendations quarterly.
- *Timeline*: 30 days implementation; ongoing oversight
- *Cost*: Personnel-intensive; ensures fairness controls

**Recommendation**: Option A + quarterly fairness auditing to restore compliance and public trust.