# COMPLIANCE REPORT: COMPAS v1.0 RECIDIVISM MODEL

## 1. REGULATORY THRESHOLDS BREACHED

**Critical Violations:**
- **EU AI Act Disparate Impact Ratio (DIR):** African-American DIR = 1.74x vs. threshold of 1.25x — **BREACH of 0.49x (39% overage)**
- **NIST False Positive Rate Gap:** African-American FPR = 42.3% vs. Caucasian 22.0% = **20.3pp gap vs. 15.0pp threshold — BREACH of 5.3pp**

**Moderate Violations:**
- **NIST False Negative Rate Gaps:** All racial groups exceed 15.0pp threshold:
  - Caucasian: 49.6% vs. African-American 28.5% = 21.1pp gap (BREACH of 6.1pp)
  - Hispanic: 58.2% vs. African-American 28.5% = 29.7pp gap (BREACH of 14.7pp)
  - Other: 66.1% vs. African-American 28.5% = 37.6pp gap (BREACH of 22.6pp)

## 2. AFFECTED GROUPS & REAL-WORLD HARM

**Primary Harm (African-American defendants, n=3,175):**
- 1,340 individuals (42.3%) falsely flagged as high-risk, resulting in unjust detention, bail denial, and sentencing enhancement
- Systemic over-incarceration driven by 1.74x elevated risk scoring

**Secondary Harm (Other groups, n=852):**
- Hispanic and Other populations experience severe false negatives (58-66%), allowing genuine risk cases to be under-supervised

## 3. REMEDIATION OPTIONS

| Option | Timeline | Actions |
|--------|----------|---------|
| **A: Immediate Suspension** | 30 days | Halt deployment; audit data for systemic bias; retrain with balanced datasets and fairness constraints |
| **B: Recalibrated Thresholds** | 90 days | Implement race-stratified decision boundaries; establish separate FPR/FNR limits per demographic; continuous monitoring |
| **C: Hybrid Human-AI Review** | 60 days | Require human review for African-American cases; deploy alternative model; phase out COMPAS by 180 days |

**Recommendation:** Option C (hybrid approach) offers fastest compliance with risk mitigation while Option A ensures legal defensibility.