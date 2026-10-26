# COMPLIANCE REPORT: COMPAS v1.0 RECIDIVISM MODEL

## 1. REGULATORY THRESHOLDS BREACHED

**African-American cohort (n=3,175)** exhibits critical violations:
- **Disparate Impact Ratio: 1.74x** (threshold: ≤1.25x) — **39% over limit**
- **False Positive Rate: 42.3%** vs. baseline 22.0% — **27.3 percentage points over 15pp threshold**
- **EU AI Act § 6(1)** violation: High-risk system lacks sufficient accuracy parity
- **NIST AI RMF** non-compliance: FPR disparity exceeds acceptable tolerance

**Caucasian cohort (n=2,103)**: FNR of 49.6% exceeds 15pp threshold (baseline ~34pp) — secondary violation.

**Hispanic & Other groups** show progressive FNR degradation (58.2%-66.1%), indicating systematic accuracy erosion across minority populations.

## 2. AFFECTED GROUPS & REAL-WORLD HARM

- **3,175 African-Americans** systematically over-flagged for recidivism (42.3% false positive rate), increasing incarceration recommendations, bail denials, and sentencing severity
- **2,103 Caucasians** under-flagged (49.6% false negative rate), receiving leniency
- **Combined 509 Hispanic + 343 Other** populations face compounded errors and reduced individualized assessment
- **Real-world impact**: Perpetuates systemic bias in criminal justice; affects parole decisions, sentencing, housing, employment eligibility

## 3. REMEDIATION OPTIONS & TIMELINES

**Option A: Immediate Suspension (0-30 days)**
- Halt predictive deployment; revert to human review only
- Conduct bias audit; timeline: 60 days
- Cost: Operational; eliminates harm immediately

**Option B: Calibration & Retraining (30-120 days)**
- Retrain with balanced datasets; implement fairness constraints (DIR <1.15x)
- Implement demographic parity post-processing
- Conduct external validation; timeline: 120 days
- Risk: Residual bias may persist

**Option C: Phased Human-in-Loop Implementation (30-180 days)**
- Deploy with mandatory judicial override for high-risk African-American flagged cases
- Implement transparency requirements (decision explanations)
- Parallel audit of model decisions vs. outcomes; timeline: 180 days
- Cost: Administrative overhead; maintains functionality with guardrails

**Recommendation**: Option A (suspension) + Option B (retraining). Immediate harm cessation followed by systematic rebuilding ensures compliance with EU AI Act and NIST standards.