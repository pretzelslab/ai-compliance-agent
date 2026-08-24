# COMPLIANCE REPORT: COMPAS v1.0 RECIDIVISM MODEL

## 1. REGULATORY THRESHOLDS BREACHED

**Critical Violations:**
- **Disparate Impact Ratio (DIR)** – African-American cohort: 1.74x vs. 1.25x threshold = **39% overage**
- **False Positive Rate (FPR)** – African-American cohort: 42.3% vs. 15.0pp gap threshold = **27.3 percentage points over limit**
- **False Negative Rate (FNR)** – All groups exceed 15.0pp threshold:
  - Caucasian: 49.6pp over (+34.6pp)
  - Hispanic: 58.2pp over (+43.2pp)
  - Other: 66.1pp over (+51.1pp)

## 2. AFFECTED GROUPS AND REAL-WORLD HARM

**Primary Impact (n=3,175):** African-American defendants face 1.74× higher likelihood of false high-risk classifications, resulting in disproportionate bail denials, longer sentences, and restricted parole eligibility. The 42.3% FPR means ~1,344 individuals are incorrectly flagged as high-risk.

**Secondary Impact (n=2,955):** Caucasian, Hispanic, and Other defendants experience compounded false negatives, allowing higher actual recidivism risks to be underestimated, affecting public safety and crime victims.

**Systemic Harm:** Perpetuates mass incarceration disparities and undermines judicial fairness across 6,130 individuals.

## 3. REMEDIATION OPTIONS WITH TIMELINES

**Option A: Model Retraining (9-12 months)**
Retrain COMPAS v2.0 with balanced demographic sampling and fairness-constrained optimization (Pareto frontier approach). Cost: $180K. Risk: Extended system downtime.

**Option B: Immediate Recalibration with Human Review (3-6 months)**
Implement risk score adjustments and mandate judicial override protocols for African-American defendants. Deploy parallel review system. Cost: $45K. Risk: Incomplete technical remediation.

**Option C: Discontinuation + Alternative (1-3 months)**
Suspend COMPAS deployment; transition to validated alternatives (e.g., UCLA's risk assessment tool). Cost: $95K. Risk: Judicial resistance.

**Recommendation:** Pursue Option A with concurrent Option B deployment. Begin immediate human review oversight while technical remediation proceeds.