# COMPLIANCE REPORT: COMPAS v1.0 RECIDIVISM MODEL

## REGULATORY BREACHES

**Critical Violations:**
- **EU AI Act Disparate Impact Ratio (DIR):** African-American group at 1.74x vs. 1.25x threshold—**39% overage**
- **NIST False Positive Rate (FPR):** African-American group at 42.3% vs. 15pp gap limit—**27.3 percentage point violation**
- **NIST False Negative Rate (FNR):** All groups exceed limits by 13.5–51.1pp; Caucasian worst at 49.6% vs. limit

**Secondary Violations:**
- US 4/5ths rule implicitly breached: Hispanic (0.84x) and Other (0.62x) show reverse discrimination signals

---

## AFFECTED GROUPS & REAL-WORLD HARM

**Primary Impact:** 3,175 African-American defendants face:
- **2.74x higher false positive rate** (42.3% vs. 22% for Caucasians)—innocent individuals flagged as high-risk, leading to longer sentences, bail denial, or enhanced monitoring
- Systemic bias embedding historical discrimination into sentencing decisions

**Secondary Impact:** 2,103 Caucasian defendants experience:
- 49.6% false negative rate—dangerous offenders released/undertreated, compromising public safety

---

## REMEDIATION OPTIONS

**Option 1: Immediate Decommission (0–30 days)**
- Remove COMPAS v1.0 from production pending retraining
- Implement human-only review for pending cases
- Cost: High operational burden; Legal risk reduction: Maximum

**Option 2: Bias Mitigation + Retraining (60–120 days)**
- Retrain on balanced datasets; apply fairness constraints (equalized FPR ≤20pp across groups)
- Implement threshold adjustment per demographic group
- Audit requirement: Monthly reporting to regulators
- Risk: Requires validation; continued exposure during retraining

**Option 3: Human-in-the-Loop Hybrid (30–90 days)**
- Deploy COMPAS as advisory only (flagged as experimental)
- Require human judge override; audit 100% of African-American cases
- Gradual transition to retrained model upon validation
- Cost: Moderate; Maintains operations while addressing harms

---

## RECOMMENDATION

**Hybrid approach (Option 3):** Balances immediate harm reduction with operational continuity. Escalate to legal/ethics board within 5 days.