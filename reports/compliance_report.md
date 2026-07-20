# COMPLIANCE REPORT: COMPAS v1.0 RECIDIVISM MODEL

## 1. REGULATORY THRESHOLDS BREACHED

**Critical Violations:**
- **EU AI Act (Disparate Impact Ratio):** African-American DIR of 1.74x exceeds 1.25x threshold by **39% (0.49x overage)**
- **NIST FPR Gap:** African-American FPR of 42.3% vs. Caucasian 22.0% creates **20.3 percentage point gap**, exceeding 15.0pp limit by **35%**

**Secondary Violations:**
- **NIST FNR Gap:** Caucasian (49.6%), Hispanic (58.2%), and Other (66.1%) groups all exceed 15.0pp threshold relative to African-American baseline (28.5%)—gaps of 21.1pp, 29.7pp, and 37.6pp respectively

## 2. AFFECTED GROUPS & REAL-WORLD HARM

**Primary Impact (African-American, n=3,175):**
- 1.74x higher recidivism risk scores despite equivalent actual behavior, driving discriminatory detention decisions
- False positive rate of 42.3% means ~1,345 individuals flagged as high-risk when they pose no actual threat

**Secondary Impact (Other groups, n=2,955):**
- Hispanic and Other populations systematically under-flagged (FNR 58.2%–66.1%), reducing pretrial support intervention, increasing reoffense risk
- Caucasian population experiences high FNR (49.6%), though lower FPR bias

**Systemic Harm:** Algorithmic bias compounds over 6,130 criminal justice decisions, perpetuating racial disparities in incarceration and recidivism outcomes.

## 3. REMEDIATION OPTIONS

**Option A: Immediate Withdrawal (0–30 days)**
- Cease COMPAS deployment; revert to human assessment protocols
- Cost: High operational disruption; lowest technical risk

**Option B: Fairness Constraint Retraining (60–120 days)**
- Retrain with group-fairness constraints (equalizing FPR/FNR across races)
- Re-audit against thresholds; deploy only if DIR ≤1.25x, FPR gap ≤15pp
- Cost: Moderate; acceptable risk if validation successful

**Option C: Human-in-the-Loop Deployment (30–90 days)**
- Implement transparent risk score display with mandatory judicial override capability
- Mandate documentation of departures from algorithm recommendations
- Cost: Moderate; reduces autonomous harm while preserving data

**Recommended:** Option B, with mandatory re-audit before deployment.