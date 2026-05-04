# COMPLIANCE REPORT: COMPAS v1.0 RECIDIVISM MODEL

## 1. REGULATORY THRESHOLDS BREACHED

**African-American cohort (n=3,175):**
- Disparate Impact Ratio (DIR): 1.74x vs. 1.25x threshold = **0.49x overage (39% breach)**
- False Positive Rate: 42.3% vs. 15.0pp gap tolerance = **27.3pp overage (182% breach)**
- False Negative Rate: 28.5% vs. 15.0pp gap tolerance = **13.5pp overage (90% breach)**

**Caucasian cohort (n=2,103):**
- False Negative Rate: 49.6% vs. 15.0pp gap = **34.6pp overage (231% breach)**

**Hispanic cohort (n=509):**
- False Negative Rate: 58.2% vs. 15.0pp gap = **43.2pp overage (288% breach)**

**Other cohort (n=343):**
- False Negative Rate: 66.1% vs. 15.0pp gap = **51.1pp overage (341% breach)**

## 2. AFFECTED GROUPS AND REAL-WORLD HARM

3,175 African-American defendants face **1.74x higher flagging rates** for recidivism despite comparable risk profiles, resulting in disproportionate detention, bail denial, and sentencing recommendations. The 42.3% false positive rate means approximately **1,343 individuals are incorrectly classified as high-risk**, driving discriminatory criminal justice outcomes.

Non-Black cohorts experience severe **false negative underdetection** (49.6%-66.1%), resulting in ~1,500+ high-risk individuals categorized as low-risk, creating public safety gaps and reduced intervention.

## 3. REMEDIATION OPTIONS

**Option A (Immediate - 30 days):**
Withdraw COMPAS v1.0 from deployment; implement manual review for all African-American cases; issue guidance to courts on documented bias.

**Option B (Short-term - 90 days):**
Retrain model with stratified sampling and fairness constraints; implement group-specific thresholds; conduct bias audit pre-deployment; establish monitoring dashboard.

**Option C (Medium-term - 180 days):**
Replace COMPAS entirely with alternative validated tool (e.g., machine-learning-free actuarial methods); conduct judicial retraining; audit 2-year case history for decisions influenced by biased scores; establish compensation framework.

**Recommendation:** Combine A + B. Immediate withdrawal protects affected populations; parallel retraining ensures continuity while addressing breaches comprehensively.