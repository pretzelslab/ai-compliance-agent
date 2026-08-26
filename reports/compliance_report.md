# COMPLIANCE REPORT: COMPAS v1.0 RECIDIVISM PREDICTION MODEL

**EXECUTIVE SUMMARY**
COMPAS v1.0 exhibits critical disparities across multiple regulatory frameworks, with African-American defendants experiencing severe algorithmic bias inconsistent with EU AI Act, NIST AI RMF, and Equal Employment Opportunity Commission standards.

---

## 1. REGULATORY THRESHOLDS BREACHED

**African-American Cohort (n=3,175):**
- Disparate Impact Ratio: 1.74x (threshold: ≤1.25x) — **breach of 39%**
- False Positive Rate: 42.3% vs. 22.0% (Caucasian baseline) — **27.3 percentage-point gap** (threshold: ≤15pp)
- False Negative Rate: 28.5% vs. 49.6% (Caucasian) — **within threshold but inverted harm**

**Cascading failures:** Hispanic (FNR 58.2%, +43.2pp) and Other (FNR 66.1%, +51.1pp) groups show extreme false negative disparities, each exceeding thresholds by >200%.

---

## 2. AFFECTED GROUPS & REAL-WORLD HARM

- **3,175 African-American defendants:** 1.74x higher likelihood of false high-risk classification, leading to prolonged detention, bail denial, and sentencing enhancements
- **509 Hispanic defendants:** 3.8x higher false negative risk—dangerous individuals flagged as low-risk, endangering public safety
- **Systemic impact:** Perpetuates racial disparities in criminal justice; compounds existing inequities in bail and sentencing systems

---

## 3. REMEDIATION OPTIONS

| Option | Timeline | Action |
|--------|----------|--------|
| **A: Immediate Suspension** | 30 days | Halt COMPAS deployment; audit dataset for historical bias; implement human-in-the-loop review for all risk assessments |
| **B: Fairness Retraining** | 90 days | Retrain using balanced subsampling (n=1,890 per group); apply fairness constraints (FPR parity); external validation |
| **C: Hybrid Deployment** | 60 days | Deploy recalibrated model; mandate demographic stratification in risk scoring; establish quarterly bias audits; escalate cases with >0.3 disparity for judicial review |

**Recommendation:** Option C with mandatory Option A safeguards. The 39% DIR breach and 27.3pp FPR gap demand immediate intervention while retraining proceeds.