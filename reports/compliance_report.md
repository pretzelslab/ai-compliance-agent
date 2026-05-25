# COMPLIANCE REPORT: COMPAS v1.0 RECIDIVISM MODEL

## 1. REGULATORY THRESHOLDS BREACHED

**Critical Violations:**
- **African-American group (n=3,175):** Disparate Impact Ratio of 1.74x exceeds EU AI Act threshold of 1.25x by **39.2%** — DOUBLE-CRITICAL
- **False Positive Rate gap:** 42.3% (African-American) vs. 22.0% (Caucasian) = **20.3 percentage points** exceeds NIST threshold of 15.0pp by **35.3%** — CRITICAL

**Secondary Violations:**
- False Negative Rate gaps across all groups exceed 15.0pp threshold, ranging 13.5-53.1pp above acceptable limits
- Approval ratio disparity: African-American defendants face 74% higher false positive rates, violating fairness principles underlying 4/5ths rule

## 2. AFFECTED GROUPS & REAL-WORLD HARM

**Primary Harm (African-Americans, n=3,175):**
- 1,344 individuals falsely flagged as high-risk (42.3% FPR) — leading to unjustified incarceration, bail denial, and enhanced sentences
- 904 individuals underestimated as low-risk (28.5% FNR) — receiving insufficient monitoring

**Secondary Harm (Other groups, n=2,952):**
- Caucasian defendants disproportionately missed (49.6% FNR), creating inconsistent public safety outcomes
- Hispanic and Other groups underrepresented in high-risk predictions (DIR <1.0), receiving lighter assessments

**Systemic Impact:** Model deployed in 52+ U.S. jurisdictions affecting ~500,000+ annual risk assessments.

## 3. REMEDIATION OPTIONS WITH TIMELINES

| Option | Action | Timeline | Cost |
|--------|--------|----------|------|
| **A: Immediate Suspension** | Halt deployment; audit all prior decisions; flag cases for judicial review | 30 days | High (legal/administrative) |
| **B: Algorithmic Retraining** | Retrain with stratified sampling and fairness constraints; establish FPR parity target <25pp | 90 days | Medium |
| **C: Human-in-Loop Hybrid** | Require judicial override for African-American predictions; implement bias training | 60 days | Low-Medium |

**Recommended:** Option A (30 days) → Option B (90 days). Immediate suspension protects civil rights; retraining addresses root causes.