# COMPLIANCE REPORT: COMPAS v1.0 RECIDIVISM MODEL

## 1. REGULATORY THRESHOLDS BREACHED

**Critical Violations:**
- **EU AI Act Disparate Impact Ratio (DIR):** African-American DIR = 1.74x vs. threshold of 1.25x — **breach of 0.49x (39% overage)**
- **NIST False Positive Rate (FPR) Gap:** African-American FPR = 42.3% vs. Caucasian 22.0% — **gap of 20.3 percentage points (pp) vs. 15.0pp threshold — breach of 5.3pp (35% overage)**

**Secondary Violations:**
- NIST False Negative Rate (FNR) gaps exceed 15.0pp threshold across all non-African-American groups (Caucasian: 49.6%, Hispanic: 58.2%, Other: 66.1%)

## 2. AFFECTED GROUPS & REAL-WORLD HARM

**African-Americans (n=3,175):** 1.74x higher likelihood of false positive predictions (flagged as high-risk when low-risk). At 42.3% FPR, approximately **1,342 individuals incorrectly classified as recidivism risks**, leading to: harsher sentencing, bail denial, parole denial, and perpetuated incarceration.

**Caucasians (n=2,103):** 49.6% FNR means dangerous individuals underestimated; public safety risk.

**Hispanic (n=509) & Other (n=343):** Extreme FNR rates (58.2%–66.1%) indicate systematic underestimation of risk, creating parallel public safety exposure.

## 3. REMEDIATION OPTIONS

**Option A: Immediate Suspension (0–30 days)**
- Halt COMPAS deployment in sentencing/parole decisions
- Conduct root-cause analysis of training data bias
- Timeline: 30 days to interim findings
- Cost: Operational disruption; legal exposure if not transparent

**Option B: Recalibration & Fairness Retraining (60–120 days)**
- Retrain model with stratified sampling and fairness constraints (demographic parity/equalized odds)
- Implement separate decision thresholds by demographic group
- External validation audit
- Timeline: 120 days to redeployment
- Risk: Technical parity may reduce overall predictive accuracy

**Option C: Hybrid Human-in-the-Loop (90–180 days)**
- Deploy model with mandatory judicial override protocols for flagged disparities
- Require annotated explanations for high-risk classifications
- Continuous monitoring dashboard (monthly FPR/FNR audit)
- Phase out pure algorithmic decisions by 180 days
- Most compliant but resource-intensive

**Recommendation:** Option B with Option C monitoring—prioritizes legal compliance and fairness while maintaining operational continuity.