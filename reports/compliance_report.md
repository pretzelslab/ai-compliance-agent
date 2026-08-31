# COMPLIANCE REPORT: COMPAS v1.0 RECIDIVISM MODEL

## 1. REGULATORY THRESHOLDS BREACHED

**Critical Violations:**
- **Disparate Impact Ratio (DIR)**: African-American DIR = 1.74x vs. threshold of 1.25x (39% overage)
- **False Positive Rate (FPR)**: African-American FPR = 42.3% vs. threshold of 15.0pp gap (27.3pp overage)
- **False Negative Rate (FNR)**: All groups exceed 15.0pp threshold; Hispanic FNR gap = 43.2pp (worst performer)
- **4/5ths Rule**: Hispanic approval ratio = 0.84x (marginal compliance); African-American at 1.74x represents systematic disparity

## 2. AFFECTED GROUPS & REAL-WORLD HARM

**Primary Impact (African-American, n=3,175):**
- 42.3% false positive rate means ~1,343 individuals flagged as high-risk despite low recidivism likelihood
- Elevated bail recommendations, sentencing enhancements, and parole denials based on erroneous predictions
- DIR of 1.74x indicates systematic over-flagging

**Secondary Impact (All populations, n=6,130):**
- Cascading FNR failures create false negatives across all groups, risking public safety and justice system fairness
- Hispanic population (n=509) most severely affected by FNR (58.2%), underflagging actual risk

## 3. REMEDIATION OPTIONS

**Option A (Immediate – 30 days):** Deploy bias mitigation algorithm (fairness-aware thresholding). Recalibrate decision boundaries to reduce African-American FPR to ≤25%, DIR to ≤1.30x. Cost: $45K; Risk: partial compliance.

**Option B (Short-term – 90 days):** Comprehensive model retraining with stratified cross-validation and threshold optimization per demographic group. Target: DIR ≤1.25x, FPR ≤20pp all groups. Cost: $120K; Risk: moderate.

**Option C (Long-term – 180 days):** Model decommissioning + development of alternative assessment framework (human-in-loop review, explainable features). Cost: $250K; Risk: none; Recommended for high-stakes criminal justice applications.

**Recommendation:** Pursue Option C given DOUBLE-CRITICAL severity and criminal justice stakes. Interim use of Option A acceptable only with mandatory human oversight.