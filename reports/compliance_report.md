# COMPLIANCE REPORT: COMPAS v1.0 RECIDIVISM MODEL

## 1. REGULATORY THRESHOLDS BREACHED

**Critical Violations:**
- **EU AI Act Disparate Impact Ratio (DIR):** African-American applicants flagged at 1.74x vs. Caucasian baseline (1.0x). Threshold: ≤1.25x. **Breach: +0.49x or 39% overage.**
- **NIST False Positive Rate (FPR) Gap:** African-American FPR=42.3% vs. Caucasian FPR=22.0%. Threshold gap: ≤15.0pp. **Breach: +20.3pp or 135% overage.**

**Secondary Violations:**
- **NIST False Negative Rate (FNR) Gap:** All groups failed. Caucasian FNR=49.6% vs. African-American FNR=28.5%, differential of 21.1pp (**+6.1pp breach**). Similar disparities across Hispanic (58.2%) and Other (66.1%) populations.

---

## 2. AFFECTED GROUPS & REAL-WORLD HARM

**Primary Impact (n=3,175 African-Americans):**
- 1,296 individuals falsely flagged as high-risk (42.3% FPR) — directly affecting parole/bail decisions, employment, and housing eligibility
- 1.74x disparity suggests algorithmic bias in feature weighting or training data, perpetuating systemic inequity in criminal justice

**Secondary Impact (n=2,955 Caucasian, Hispanic, Other):**
- Higher false negatives increase public safety risks; lower false positives create appearance of fairness while masking underlying bias

---

## 3. REMEDIATION OPTIONS

**Option 1: Immediate Suspension & Audit (0-30 days)**
- Remove COMPAS from production for all decisions
- Conduct bias audit with external auditors
- **Timeline:** 30 days; Cost: High; Risk: Operational disruption

**Option 2: Threshold Recalibration (30-90 days)**
- Retrain model with fairness constraints (e.g., equalized FPR across groups to ≤25pp)
- Implement group-specific risk thresholds; deploy A/B testing
- **Timeline:** 90 days; Cost: Medium; Risk: Technical complexity

**Option 3: Human-in-the-Loop Hybrid (60-120 days)**
- Maintain COMPAS as advisory only; require human review for flagged cases
- Implement bias mitigation retraining + mandatory override documentation
- **Timeline:** 120 days; Cost: Medium-High; Risk: Moderate

**Recommendation:** **Option 1 (suspension) immediately, transitioning to Option 3 (hybrid) for operational continuity.**