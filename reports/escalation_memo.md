**MEMORANDUM**

TO: Chief Risk Officer
FROM: AI Compliance Analysis
DATE: [Current Date]
RE: DEPLOYMENT BLOCK — COMPAS v1.0 Model

**DECISION: DO NOT DEPLOY**

**Specific Breaches Identified**

COMPAS v1.0 fails critical regulatory standards across 3 compliance frameworks:

- **EU AI Act violation**: African-American DIR of 1.74x exceeds 1.25x threshold by 39%
- **NIST FPR standard breach**: African-American FPR gap of 42.3% vs. 22.0% (white baseline) = 20.3pp gap; threshold violation of 35.3%
- **4/5ths Rule failure**: African-American approval ratio of 0.58x falls below 0.8 threshold

**Most Severely Affected Group & Real-World Consequence**

African-American defendants (n=3,175) face **disproportionate false positive risk** at 42.3%—nearly **2x the rate** for Caucasian defendants. This produces discriminatory incarceration recommendations, violating due process and equal protection principles.

**Required Actions Before Redeployment**

1. Conduct algorithmic bias audit identifying root causes (dataset imbalance, feature bias, historical data contamination)
2. Retrain model with fairness constraints ensuring DIR ≤1.25x across all groups
3. Validate FPR/FNR parity within ±15pp across racial groups per NIST guidelines
4. Obtain independent third-party validation
5. Implement bias monitoring dashboard before deployment

**Redeployment prohibited until all conditions satisfied.**