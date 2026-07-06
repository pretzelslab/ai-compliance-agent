# COMPLIANCE REPORT: COMPAS v1.0 RECIDIVISM MODEL

**CRITICAL FINDINGS**

## 1. REGULATORY THRESHOLDS BREACHED

**African-American Group (n=3,175):**
- Disparate Impact Ratio: 1.74x (threshold: ≤1.25x) — **39% over limit**
- False Positive Rate: 42.3% (NIST threshold: ≤15pp gap) — **27.3 percentage points over**
- EU AI Act: FAILED (high-risk application with unacceptable bias)

**All Minority Groups (n=3,027 combined):**
- False Negative Rates: 28.5%-66.1% (threshold: ≤15pp gap) — **13.5-51.1pp over limit**
- Approval ratio failure under 4/5ths rule for African-American group (1.74/1.0 = inverse of 0.57)

## 2. AFFECTED GROUPS & REAL-WORLD HARM

**Primary Victims: African-American defendants (3,175 individuals)**
- 42.3% falsely flagged as high-risk (1,342+ false positives)
- 1.74x higher likelihood of adverse decisions vs. Caucasian defendants
- Result: Over-incarceration, extended sentences, surveillance intensification, parole denial

**Secondary Impact: Hispanic (n=509) and Other groups (n=343)**
- Disproportionately low flagging increases release risk (58-66% false negatives)
- Systemic under-protection and inequitable risk assessment

## 3. REMEDIATION OPTIONS

**Option A: Immediate Suspension (0-30 days)**
- Halt deployment pending bias remediation; revert to human review only
- Cost: Operational delay; benefit: eliminates active harm
- Implement fairness constraints and rebalancing by Day 90

**Option B: Constrained Deployment (30-60 days)**
- Deploy with mandatory human override for African-American defendants
- Reduce DIR threshold to ≤1.15x via threshold adjustment
- Parallel audit with alternative models; full retraining by Day 120

**Option C: Model Retraining & Revalidation (60-180 days)**
- Stratified resampling to address demographic imbalance (3,175 vs. 2,103)
- Implement fairness metrics (equalized odds); retrain COMPAS v1.1
- Independent validation audit by Day 180; phased redeployment thereafter

**RECOMMENDATION:** Option A + accelerated Option C. Current deployment violates EU AI Act §6(1) and creates documented discriminatory harm unsuitable for criminal justice applications.