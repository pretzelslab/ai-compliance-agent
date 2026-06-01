# COMPLIANCE REPORT: COMPAS v1.0 RECIDIVISM MODEL

**REGULATORY VIOLATIONS**

The model breaches critical fairness thresholds across multiple jurisdictions:

- **EU AI Act (Disparate Impact Ratio):** African-American DIR of 1.74x exceeds the 1.25x threshold by 39%, representing the most severe violation.
- **NIST FPR Gap:** African-American false positive rate of 42.3% exceeds the 15.0 percentage point threshold by 27.3pp—nearly triple the permitted disparity.
- **NIST FNR Gap:** All groups breach FNR thresholds, with Hispanic (58.2%) and Other (66.1%) populations exceeding limits by 43.2pp and 51.1pp respectively.

**AFFECTED POPULATIONS & HARM**

Of 6,130 individuals assessed, 3,175 African-American defendants face systematic disadvantage. With a 1.74x disparate impact ratio, the model is 74% more likely to classify African-American defendants as high-risk compared to Caucasian counterparts. The 42.3% false positive rate means approximately 1,343 African-American individuals are incorrectly flagged as recidivism risks, directly influencing bail decisions, sentencing recommendations, and parole eligibility. This perpetuates systemic bias, disproportionately extending incarceration for already overrepresented populations.

**REMEDIATION OPTIONS**

**Option 1 (Immediate - 30 days):** Deploy model moratorium for pretrial risk assessment. Reinstate human review for all high-risk classifications. Cost: operational; Risk: maintains status quo harm.

**Option 2 (Short-term - 90 days):** Retrain COMPAS v1.0 using stratified sampling and fairness constraints (equal FPR ≤20pp across groups). Implement separate calibration by race. Cost: $150K-200K; Risk: performance trade-offs.

**Option 3 (Long-term - 180 days):** Decommission COMPAS; develop alternative risk assessment using structured professional judgment without algorithmic scoring. Audit third-party validation independently. Cost: $400K-600K; Risk: implementation complexity.

**Recommendation:** Pursue Option 1 immediately while implementing Option 3. Current deployment violates EU AI Act Article 10 and exposes organizations to liability under equal protection standards.