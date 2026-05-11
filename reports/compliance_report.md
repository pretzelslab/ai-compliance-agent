# COMPLIANCE REPORT: COMPAS v1.0 RECIDIVISM MODEL

## 1. REGULATORY THRESHOLDS BREACHED

**Critical Violations:**
- **EU AI Act Disparate Impact Ratio (DIR)**: African-American DIR = 1.74x vs. threshold of ≤1.25x. **Breach magnitude: +0.49x (39% over limit)**
- **NIST False Positive Rate Gap**: African-American FPR = 42.3% vs. Caucasian 22.0%. **Gap = 20.3 percentage points (pp) vs. ≤15.0pp threshold. Breach: +5.3pp**

**Moderate Violations:**
- **NIST False Negative Rate Gaps**: All groups except African-Americans exceed the 15.0pp threshold. Hispanic FNR gap (58.2% vs. 28.5%) = **+29.7pp over threshold**. Other races FNR gap = **+50.1pp over threshold**.

---

## 2. AFFECTED GROUPS & REAL-WORLD HARM

**Primary victims (n=3,175 African-Americans):**
- 1.74x higher likelihood of false positive classification (incorrectly flagged as high-risk)
- 42.3% false positive rate means ~1,340 individuals wrongly predicted as recidivists
- Consequences: unjust detention decisions, parole denial, increased criminal justice exposure

**Secondary victims (n=509 Hispanic individuals):**
- 58.2% false negative rate: ~296 high-risk individuals missed
- Inadequate monitoring creates public safety gaps

---

## 3. REMEDIATION OPTIONS

**Option A (Immediate - 30 days):** Deploy model with mandatory human review for all African-American cases; reduces DIR effective impact pending retraining.

**Option B (Short-term - 90 days):** Retrain with stratified sampling (equal group representation), implement fairness constraints using Threshold Optimizer to achieve DIR ≤1.25x and FPR gap ≤10pp.

**Option C (Comprehensive - 180 days):** Complete model redesign using adversarial debiasing; collect additional data on underrepresented groups (n=852); conduct external fairness audit; implement continuous monitoring dashboard.

**Recommendation:** Implement Option A immediately while executing Option C. Model deployment moratorium recommended for high-stakes decisions pending remediation.