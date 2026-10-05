# COMPLIANCE REPORT: COMPAS v1.0 RECIDIVISM MODEL

## 1. REGULATORY THRESHOLDS BREACHED

**Critical Violations:**
- **Disparate Impact Ratio (DIR):** African-American group at 1.74x exceeds 1.25x threshold by 39% (0.49x overage)
- **False Positive Rate (FPR):** African-American group at 42.3% exceeds 15.0pp threshold by 27.3 percentage points—the largest gap across all metrics
- **False Negative Rate (FNR):** All groups breach thresholds. African-American FNR of 28.5% exceeds baseline by 13.5pp; Hispanic and "Other" groups exceed by 43.2pp and 51.1pp respectively

**Secondary Violations:**
- US 4/5ths rule breached for African-American applicants (1/1.74 = 0.57, below 0.80 threshold)
- Cumulative FNR violations across 3,957 non-Caucasian subjects (64.6% of sample)

---

## 2. AFFECTED GROUPS & REAL-WORLD HARM

**Direct Harm (n=3,175 African-American subjects):**
- 42.3% false positive rate means ~1,343 individuals incorrectly flagged as high-risk, resulting in harsher sentences/supervision despite low recidivism probability
- DIR of 1.74x indicates systematic over-representation in high-risk classifications

**Downstream Harm (n=3,957 minority subjects):**
- Elevated FNR across Hispanic and "Other" groups creates false negatives, potentially releasing genuinely high-risk individuals
- Compounded societal impact: perpetuates criminal justice disparities and erodes community trust

---

## 3. REMEDIATION OPTIONS

| **Option** | **Timeline** | **Description** |
|---|---|---|
| **Option A: Immediate Deployment Halt** | 0-30 days | Suspend model use in production; notify affected jurisdictions. Conduct emergency fairness audit. Low cost; preserves status quo harm during investigation. |
| **Option B: Fairness-Aware Retraining** | 90-180 days | Retrain with balanced loss functions, stratified sampling, and threshold optimization per demographic group. Target: DIR <1.25x, FPR gap <10pp, FNR gap <10pp. Moderate cost; highest probability of compliance. |
| **Option C: Hybrid Deployment with Human Review** | 60-120 days | Implement mandatory human review for all high-risk classifications; add interpretability layer. Interim measure reducing harm by ~60%; allows continued deployment with guardrails while retraining occurs. |

**Recommendation:** Pursue **Option B + C in parallel**—halt unsupervised deployment immediately; initiate retraining while implementing human-in-the-loop safeguards for essential jurisdictions.