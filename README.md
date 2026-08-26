# AI Compliance Monitoring Agent

A prototype governance pipeline that turns recurring AI fairness evaluations into structured monitoring, escalation and audit outputs.

The project explores a practical question:

**How can measurable Responsible AI evidence become an operational governance signal rather than remain a point in time assessment?**

## What it does

The pipeline:

1. Loads and prepares the COMPAS recidivism dataset.
2. Computes group level fairness indicators including false positive rate, false negative rate, selection outcomes and relative disparity measures.
3. Evaluates results against configurable governance thresholds.
4. Classifies findings by severity.
5. Routes the result through a LangGraph workflow.
6. Produces monitoring, compliance or escalation outputs.
7. Retains structured results as version controlled audit artifacts.

## Current prototype flow

```text
Evaluation data
      ↓
Fairness metrics
      ↓
Structured audit evidence
      ↓
Severity classification
      ↓
LangGraph governance routing
      ↓
Monitor | Escalate | Restrict
      ↓
Audit artifact
```

## Governance focus

The project is less about inventing new fairness metrics and more about what happens after an evaluation identifies a potential problem.

The prototype explores how evaluation evidence can inform:

• monitoring

• compliance review

• remediation

• escalation

• deployment restrictions

• auditable governance records

## Technology

Python
Pandas
LangGraph
Anthropic Claude
GitHub Actions
COMPAS dataset

## Thresholds and regulatory context

The quantitative thresholds used in this repository are **illustrative, configurable governance thresholds for prototype evaluation logic**.

They should not be interpreted as universal thresholds prescribed by the EU AI Act, NIST AI RMF or other regulatory frameworks.

Those frameworks provide governance and risk management context. Organizations remain responsible for defining appropriate metrics, thresholds, validation methods and decision rules for their specific systems and use cases.

## Current research question

This prototype currently produces fairness evidence and maps it into governance responses.

A next research question is:

**How should externally produced fairness evidence be represented as a machine readable governance signal that an agent governance layer can consume for policy decisions, human review, restrictions and compliance escalation?**

This includes questions around evidence freshness, provenance, missing evidence, conflicting evaluations, threshold ownership and auditability.

## Status

Research prototype.

The deployment recommendations produced by the workflow are demonstrative governance outputs. They do not independently authorize or block deployment of a real world AI system.
