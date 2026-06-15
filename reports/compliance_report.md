# COMPLIANCE REPORT: COMPAS v1.0 RECIDIVISM MODEL

## 1. REGULATORY THRESHOLDS BREACHED

**Critical Violations:**
- **EU AI Act Disparate Impact Ratio (DIR):** African-American group breached at 1.74x (threshold: ≤1.25x), exceeding limit by **39.2%**
- **NIST False Positive Rate Gap:** African-American FPR of 42.3% versus Caucasian baseline 22.0% = **20.3 percentage points**, exceeding 15.0pp threshold by **35.3%**

**Secondary Violations:**
- **NIST False Negative Rate Gaps:** All groups exceed 15.0pp threshold. Caucasian FNR gap (49.6% vs. African-American 28.5%) = **21.1pp excess**; Hispanic and Other groups show escalating disparities up to 66.1%

## 2. AFFECTED GROUPS & REAL-WORLD HARM

**Primary Impact (n=3,175 African-Americans):**
- 42.3% false positive rate means ~1,342 individuals incorrectly flagged as high-risk, leading to enhanced monitoring, bail denial, or sentencing recommendations
- 1.74x disparate impact ratio indicates systematically biased risk assessment

**Secondary Impact (n=2,955 other defendants):**
- Disproportionate false negatives for Hispanic (58.2%) and Other (66.1%) groups create under-flagging, inconsistently applied public safety protections
- Cascading effects: bail decisions, parole eligibility, resource allocation bias

## 3. REMEDIATION OPTIONS

**Option A (Immediate):** Model withdrawal and manual review protocol
- Timeline: 0-30 days
- Cost: High operational burden
- Effectiveness: Eliminates risk; restores due process

**Option B (Short-term):** Retrain with balanced dataset and bias-correction algorithms (e.g., fairness constraints)
- Timeline: 90-180 days
- Cost: Moderate ($250K-500K estimated)
- Effectiveness: Addresses DIR and FPR gaps; requires validation testing

**Option C (Parallel):** Deploy human-in-the-loop review with stratified auditing
- Timeline: 30-60 days initial; ongoing
- Cost: Low-moderate (staffing)
- Effectiveness: Mitigates harm while Option B executes; requires judicial coordination

**Recommendation:** Implement Option A immediately pending Option B completion, with Option C as interim safeguard.