# COMPLIANCE REPORT: COMPAS v1.0 RECIDIVISM MODEL

## 1. REGULATORY THRESHOLDS BREACHED

**Critical Violations:**
- **EU AI Act Disparate Impact Ratio (DIR):** African-American DIR = 1.74x vs. threshold of 1.25x (39% overage)
- **NIST False Positive Rate Gap:** African-American FPR = 42.3% vs. Caucasian 22.0% = 20.3pp gap (35% above 15pp threshold)
- **NIST False Negative Rate Gaps:** Caucasian (49.6%), Hispanic (58.2%), Other (66.1%) all exceed 15pp threshold by 234.6%, 288%, and 341% respectively

**Secondary Violation:**
- 4/5ths rule not directly breached but DIR findings indicate systemic discrimination risk

## 2. AFFECTED GROUPS & REAL-WORLD HARM

**Primary Harm (African-American, n=3,175):**
- 1.74x higher false positive rate: ~640 individuals incorrectly flagged as high-risk, facing enhanced supervision, bail denial, or incarceration
- 28.5% false negative rate: ~905 genuine high-risk individuals released without appropriate monitoring

**Secondary Harm (All Groups, n=6,130):**
- Caucasian defendants: 49.6% false negatives risk community safety gaps (1,042 individuals)
- Hispanic/Other minorities: 58.2%-66.1% false negatives create release risks for ~455 individuals
- Compounding: Systematic over-incarceration of African-Americans with under-monitoring of other groups

## 3. REMEDIATION OPTIONS & TIMELINES

**Option A – Model Withdrawal (Immediate, 0-30 days)**
- Cease COMPAS v1.0 deployment across all jurisdictions
- Revert to human-only risk assessment
- Cost: High operational disruption; timeline feasible

**Option B – Bias Mitigation Retraining (60-120 days)**
- Retrain with balanced datasets; apply fairness constraints (DIR ≤1.25x, FPR gap ≤15pp)
- Implement threshold adjustments per demographic group
- Requires external validation before redeployment
- Cost: Moderate; reduces false positives for African-Americans

**Option C – Phased Restriction with Monitoring (45-180 days)**
- Deploy as advisory-only tool (no binding decisions) for 6 months
- Collect ground-truth outcome data by demographic
- Parallel human review mandatory for high-risk classifications
- Transition to Option B if drift controlled; escalate to Option A if violations persist

**Recommended:** Option C (phased) transitioning to Option B (retraining) with quarterly audits.