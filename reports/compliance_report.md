# COMPLIANCE REPORT: COMPAS v1.0 RECIDIVISM MODEL

## REGULATORY BREACHES

**Critical Violations:**
- **EU AI Act Disparate Impact Ratio (DIR):** African-American cohort at 1.74x (threshold: ≤1.25x) — **39% overage**
- **NIST False Positive Rate (FPR) Gap:** African-American at 42.3% vs. Caucasian at 22.0% = **20.3 percentage point gap** (threshold: ≤15pp) — **35% exceedance**

**Secondary Violations:**
- **NIST False Negative Rate (FNR) Gap:** All groups exceed 15pp threshold. Hispanic cohort shows 58.2% FNR (43.2pp overage); Caucasian 49.6% (34.6pp overage)
- **4/5ths Rule:** Hispanic approval ratio 0.84x approaches but remains compliant at threshold edge

## AFFECTED GROUPS & REAL-WORLD HARM

**3,175 African-Americans** face disproportionate false positive rates (42.3%), resulting in 1,347 individuals incorrectly flagged as high-recidivism risk. These overclassifications drive unjust detention recommendations and bail denials.

**2,103 Caucasians** experience 49.6% false negatives, allowing approximately 1,043 genuinely high-risk individuals to receive lenient assessments—creating public safety gaps.

**509 Hispanic individuals** suffer the highest FNR (58.2%), with 295 misclassifications, compounding underrepresentation in risk identification.

## REMEDIATION OPTIONS

**Option 1: Immediate Deployment Halt (0-30 days)**
- Suspend COMPAS v1.0 in sentencing contexts pending audit completion
- Redirect to human-only assessment protocols
- Timeline: 30 days

**Option 2: Algorithmic Retraining with Fairness Constraints (60-120 days)**
- Retrain model with enforced parity constraints (DIR <1.15x, FPR gap <10pp)
- Validate across stratified test sets; requires 40% additional labeled data
- Implement continuous monitoring dashboards
- Timeline: 120 days

**Option 3: Hybrid Human-AI Framework (45-90 days)**
- Deploy COMPAS as advisory-only (flagged output confidence <75%)
- Require mandatory human review for all African-American and Hispanic assessments
- Establish appeals process with documented override authority
- Timeline: 90 days

**Recommendation:** Option 2 combined with Option 3 interim measures minimizes harm while enabling long-term compliance.