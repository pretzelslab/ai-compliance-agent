# COMPLIANCE REPORT: COMPAS v1.0 RECIDIVISM MODEL

## 1. REGULATORY THRESHOLDS BREACHED

**Critical Violations:**
- **EU AI Act Disparate Impact Ratio (DIR):** African-American group at 1.74x vs. 1.25x threshold — **39% overage**
- **NIST False Positive Rate (FPR) Gap:** African-American group at 42.3% vs. Caucasian 22.0% = **20.3 percentage point gap** exceeds 15.0pp limit by **35%**

**Secondary Violations:**
- **NIST False Negative Rate (FNR) Gap:** All non-African-American groups exceed 15.0pp threshold:
  - Caucasian: 49.6% gap (**231% over limit**)
  - Hispanic: 58.2% gap (**288% over limit**)
  - Other: 66.1% gap (**341% over limit**)

## 2. AFFECTED GROUPS & REAL-WORLD HARM

**Primary Impact (3,175 African-Americans):**
- 42.3% false positive rate means ~1,341 individuals incorrectly flagged as high-risk, leading to enhanced supervision, bail denials, and sentencing recommendations they don't merit

**Secondary Impact (2,955 non-African-American defendants):**
- Caucasian defendants underidentified (49.6% FNR): ~1,043 actual high-risk individuals missed
- Hispanic/Other groups face 58-66% miss rates, compromising public safety assessments

**Systemic Harm:** Reinforces racial bias in criminal justice; African-Americans receive disproportionate restrictions; system fails to protect public from legitimately high-risk individuals of other demographics.

## 3. REMEDIATION OPTIONS & TIMELINES

**Option A – Immediate Suspension (0 days)**
- Halt COMPAS deployment; revert to manual assessments pending remediation
- *Timeline:* Effective immediately
- *Cost:* High operational burden; timeline to fix: 6-12 months

**Option B – Threshold Recalibration (30-60 days)**
- Retrain model with balanced fairness constraints (FPR/FNR parity ≤5pp)
- Implement race-stratified thresholds where legally permissible
- *Timeline:* 60 days to deployment; requires legal review
- *Risk:* May sacrifice overall accuracy

**Option C – Hybrid Human Review (15-90 days)**
- Deploy model with mandatory human override for African-American flagged cases
- Parallel retrain Model v2.0 with fairness audits every 30 days
- *Timeline:* Interim controls in 15 days; full remediation 90 days
- *Benefit:* Reduces immediate harm while enabling systematic fix

**Recommendation:** Option C (hybrid) offers fastest harm reduction with structured remediation pathway.