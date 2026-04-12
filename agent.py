import json
import os
import anthropic
from typing import TypedDict
from langgraph.graph import StateGraph, END

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

class AuditState(TypedDict):
    audit_report:           dict
    overall_verdict:        str
    severity_summary:       str
    routing_decision:       str
    compliance_report:      str
    escalation_memo:        str
    monitoring_report:      str

def build_context(state):
    r = state["audit_report"]
    return f"""
AUDIT REPORT SUMMARY
Model: {r["report_metadata"]["model"]}
Dataset: {r["report_metadata"]["dataset"]}
Domain: {r["report_metadata"]["domain"]}
Overall verdict: {state["overall_verdict"]}

GROUP FINDINGS:
{state["severity_summary"]}

THRESHOLDS APPLIED:
- EU AI Act DIR threshold: <= {r["thresholds_applied"]["eu_ai_act_dir"]}x
- US 4/5ths rule: >= {r["thresholds_applied"]["us_fourfifths"]} approval ratio
- NIST FPR gap: <= {r["thresholds_applied"]["nist_fpr_gap_pp"]}pp
- NIST FNR gap: <= {r["thresholds_applied"]["nist_fnr_gap_pp"]}pp
""".strip()

def call_haiku(prompt):
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text

def assess(state):
    report  = state["audit_report"]
    verdict = report["overall_verdict"]
    lines   = []
    for group, f in report["group_findings"].items():
        failures = [
            k.replace("_", " ").upper()
            for k in ["eu_ai_act", "us_fourfifths", "nist_fpr", "nist_fnr"]
            if f[k] == "FAIL"
        ]
        if failures:
            lines.append(
                f"{group} (n={f['n']}): DIR={f['dir']}x, "
                f"FPR={f['fpr']}%, FNR={f['fnr']}% — "
                f"FAILED: {', '.join(failures)} — Severity: {f['severity']}"
            )
    print(f"[Assess] Verdict: {verdict}")
    return {**state, "overall_verdict": verdict, "severity_summary": "\n".join(lines)}

def classify(state):
    routing = {
        "DOUBLE-CRITICAL": "escalate",
        "CRITICAL":        "comply",
        "WARNING":         "monitor",
        "PASS":            "approve",
    }.get(state["overall_verdict"], "monitor")
    print(f"[Classify] {state['overall_verdict']} → {routing}")
    return {**state, "routing_decision": routing}

def node_monitor(state):
    print("[Monitor] Generating monitoring report...")
    report = call_haiku(f"""
You are an AI compliance analyst. Write a brief monitoring report (under 200 words).
Identify which groups triggered warnings, which thresholds were breached,
and recommend a 30-day monitoring cadence. Use the numbers.
\n{build_context(state)}
""")
    return {**state, "monitoring_report": report}

def node_comply(state):
    print("[Comply] Generating compliance report...")
    report = call_haiku(f"""
You are an AI compliance analyst. Write a compliance report (under 300 words) covering:
1. Which regulatory thresholds were breached and by how much
2. Which demographic groups are affected
3. Three specific remediation options with timelines
Use the numbers.
\n{build_context(state)}
""")
    return {**state, "compliance_report": report}

def node_escalate(state):
    print("[Escalate] Generating compliance report + escalation memo...")
    context    = build_context(state)
    compliance = call_haiku(f"""
You are an AI compliance analyst. Write a compliance report (under 300 words) covering:
1. Regulatory thresholds breached and by how much
2. Affected groups and real-world harm
3. Three remediation options with timelines
Use the numbers.
\n{context}
""")
    memo = call_haiku(f"""
You are an AI compliance analyst writing to a Chief Risk Officer.
Write a deployment block memo (under 200 words):
1. Model must not be deployed — cite specific breaches
2. Most severely affected group and real-world consequence
3. Required actions before redeployment
Use formal memo language. Use the numbers.
\n{context}
""")
    os.makedirs("reports", exist_ok=True)
    with open("reports/compliance_report.md", "w") as f:
        f.write(compliance)
    with open("reports/escalation_memo.md", "w") as f:
        f.write(memo)
    print("[Escalate] Reports saved to reports/")
    return {**state, "compliance_report": compliance, "escalation_memo": memo}

def run_agent(audit_report):
    graph = StateGraph(AuditState)
    graph.add_node("assess",   assess)
    graph.add_node("classify", classify)
    graph.add_node("monitor",  node_monitor)
    graph.add_node("comply",   node_comply)
    graph.add_node("escalate", node_escalate)
    graph.set_entry_point("assess")
    graph.add_edge("assess", "classify")
    graph.add_conditional_edges(
        "classify",
        lambda s: s["routing_decision"],
        {"monitor": "monitor", "comply": "comply", "escalate": "escalate", "approve": END}
    )
    graph.add_edge("monitor",  END)
    graph.add_edge("comply",   END)
    graph.add_edge("escalate", END)
    app = graph.compile()

    result = app.invoke({
        "audit_report": audit_report, "overall_verdict": "",
        "severity_summary": "", "routing_decision": "",
        "compliance_report": "", "escalation_memo": "", "monitoring_report": "",
    })
    print(f"[Agent] Complete — verdict: {result['overall_verdict']}")
    return result

if __name__ == "__main__":
    with open("data/audit_report.json") as f:
        report = json.load(f)
    run_agent(report)
