# COMPLIANCE REPORT: COMPAS v1.0 RECIDIVISM MODEL

## REGULATORY BREACHES

**Critical Violations:**
- **EU AI Act (Disparate Impact Ratio):** African-American DIR = 1.74x vs. threshold of 1.25x — **BREACH BY 39.2%**
- **NIST FPR Gap:** African-American FPR = 42.3% vs. Caucasian 22.0% — **BREACH BY 27.3 PERCENTAGE POINTS** (threshold: 15.0pp)
- **US 4/5ths Rule:** African-American approval ratio = 0.62x vs. threshold of 0.80 — **BREACH BY 22.5%**

**Secondary Violations:**
- Caucasian FNR gap (49.6% vs. threshold 15.0pp): breach by 34.6pp
- Hispanic FNR gap (58.2%): breach by 43.2pp
- All groups except African-American fail FNR thresholds

---

## AFFECTED GROUPS & HARM

**3,175 African-Americans:** 74% higher likelihood of false positive classifications (flagged as high-risk when low-risk). Systemic overestimation drives discriminatory bail/sentencing recommendations, perpetuating incarceration disparities.

**2,955 Caucasians + other groups:** Underestimated recidivism risk (FNR 49.6%-66.1%) results in lower supervision for actual repeat offenders, creating public safety gaps.

**Aggregate harm:** 6,130 individuals subject to biased risk predictions influencing judicial decisions across criminal justice systems.

---

## REMEDIATION OPTIONS

**Option 1 (Immediate - 30 days):**
Deploy model suspension + manual case review for all African-American defendants. Revert to prior risk assessment protocols. Cost: institutional capacity strain.

**Option 2 (Short-term - 90 days):**
Implement stratified retraining using fairness constraints (threshold FPR ≤ 25% across all groups). Requires dataset balancing and fairness-aware algorithm redesign. Validation testing required.

**Option 3 (Medium-term - 180 days):**
Establish fairness monitoring dashboard with real-time bias alerts. Develop group-specific calibration thresholds. Conduct external algorithmic audit quarterly. Integrate human-in-the-loop review for high-stakes cases.

**Recommended:** Option 3 with concurrent Option 1 safeguards (hybrid approach). Suspension of high-risk African-American classifications pending retraining (90 days).

---

**Status:** IMMEDIATE ACTION REQUIRED — Model unfit for deployment under EU AI Act, NIST standards, and US civil rights law.