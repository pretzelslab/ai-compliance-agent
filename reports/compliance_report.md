# COMPLIANCE REPORT: COMPAS v1.0 RECIDIVISM MODEL

## 1. REGULATORY THRESHOLD BREACHES

**Critical Violations:**

- **Disparate Impact Ratio (DIR)**: African-American group achieved 1.74x against 1.25x threshold — **39% overage**
- **False Positive Rate (FPR)**: African-American FPR of 42.3% vs. 15.0pp threshold — **27.3 percentage points above limit** (182% exceedance)
- **False Negative Rate (FNR)**: All groups failed. Caucasian FNR 49.6% vs. 15.0pp threshold — **34.6pp overage**; Hispanic 58.2% (**43.2pp overage**); Other 66.1% (**51.1pp overage**)

**Regulatory Framework Failures:**
- EU AI Act (high-risk criminal justice): African-American group only
- NIST AI RMF thresholds: All racial groups across FPR/FNR metrics

## 2. AFFECTED GROUPS & REAL-WORLD HARM

**African-American defendants (n=3,175):** 42.3% falsely flagged as high-risk; 1.74x higher adverse decisions. Compounded incarceration and recidivism risk through algorithmic bias.

**Caucasian defendants (n=2,103):** 49.6% false negatives mask actual risk; systematic under-supervision despite recidivism likelihood.

**Hispanic & Other groups (n=852):** 58-66% false negatives create disparate under-detection; resource misallocation and differential treatment.

**Systemic harm:** 3,689 individuals across protected groups received inaccurate risk assessments affecting bail decisions, sentencing, and parole eligibility.

## 3. REMEDIATION OPTIONS

**Option A (Immediate, 30 days):** Halt deployment; issue advisory to judicial stakeholders. Retrain model with stratified sampling and fairness constraints (DIR ≤1.15x). **Timeline: 60 days.**

**Option B (Moderate, 90 days):** Implement human-in-the-loop review for African-American flagged cases. Recalibrate thresholds per demographic group. Parallel audit of historical decisions. **Timeline: 120 days.**

**Option C (Long-term, 6 months):** Replace COMPAS with fairness-certified alternative (e.g., constraint-based regression). Establish ongoing monitoring dashboard. Conduct retrospective justice review for affected individuals. **Timeline: 180 days + ongoing.**

**Recommendation:** Implement Option A immediately (system halt + retraining) while designing Option C for permanent replacement.