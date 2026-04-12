import pandas as pd
import json
from datetime import datetime, timezone

def run_pipeline():
    print("Loading COMPAS data...")
    url = "https://raw.githubusercontent.com/propublica/compas-analysis/master/compas-scores-two-years.csv"
    df = pd.read_csv(url)

    # Filter
    df = df[df["type_of_assessment"] == "Risk of Recidivism"]
    df = df[df["days_b_screening_arrest"].between(-30, 30)]
    df = df[df["is_recid"] != -1]
    df = df[df["race"].isin(["African-American", "Caucasian", "Hispanic", "Other"])]
    print(f"Filtered rows: {len(df)}")

    # Compute metrics
    THRESHOLD = 5
    df["flagged"] = df["decile_score"] >= THRESHOLD
    results = {}

    for race in ["African-American", "Caucasian", "Hispanic", "Other"]:
        group = df[df["race"] == race]
        reoffended     = group[group["two_year_recid"] == 1]
        not_reoffended = group[group["two_year_recid"] == 0]
        fpr       = (not_reoffended["flagged"].sum() / len(not_reoffended)) * 100
        fnr       = ((~reoffended["flagged"]).sum() / len(reoffended)) * 100
        flag_rate = group["flagged"].mean() * 100
        results[race] = {
            "n": len(group),
            "flag_rate": round(flag_rate, 1),
            "fpr": round(fpr, 1),
            "fnr": round(fnr, 1),
        }

    cauc_flag = results["Caucasian"]["flag_rate"]
    for race, m in results.items():
        m["dir"] = round(m["flag_rate"] / cauc_flag, 2)

    # Check thresholds
    THRESHOLDS = {
        "eu_ai_act_dir": 1.25,
        "us_fourfifths": 0.80,
        "nist_fpr_gap_pp": 15.0,
        "nist_fnr_gap_pp": 15.0,
    }
    min_fpr = min(m["fpr"] for m in results.values())
    min_fnr = min(m["fnr"] for m in results.values())
    max_flag = max(m["flag_rate"] for m in results.values())
    findings = {}

    for race, m in results.items():
        best_approval   = 1 - (max_flag / 100)
        group_approval  = 1 - (m["flag_rate"] / 100)
        fpr_gap = m["fpr"] - min_fpr
        fnr_gap = m["fnr"] - min_fnr
        findings[race] = {
            **m,
            "eu_ai_act":     "FAIL" if m["dir"] > THRESHOLDS["eu_ai_act_dir"] else "PASS",
            "us_fourfifths": "FAIL" if best_approval > 0 and (group_approval / best_approval) < THRESHOLDS["us_fourfifths"] else "PASS",
            "nist_fpr_gap":  round(fpr_gap, 1),
            "nist_fpr":      "FAIL" if fpr_gap > THRESHOLDS["nist_fpr_gap_pp"] else "PASS",
            "nist_fnr_gap":  round(fnr_gap, 1),
            "nist_fnr":      "FAIL" if fnr_gap > THRESHOLDS["nist_fnr_gap_pp"] else "PASS",
        }

    # Classify severity
    def classify(f):
        breaches = sum([f["eu_ai_act"] == "FAIL", f["us_fourfifths"] == "FAIL",
                        f["nist_fpr"] == "FAIL", f["nist_fnr"] == "FAIL"])
        if f["dir"] > 1.5 or breaches >= 3: return "DOUBLE-CRITICAL"
        if breaches == 2: return "CRITICAL"
        if breaches == 1: return "WARNING"
        return "PASS"

    severities = []
    for race, f in findings.items():
        s = classify(f)
        findings[race]["severity"] = s
        severities.append(s)

    rank = ["PASS", "WARNING", "CRITICAL", "DOUBLE-CRITICAL"]
    overall = rank[max(rank.index(s) for s in severities)]

    report = {
        "report_metadata": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "dataset": f"COMPAS Recidivism (ProPublica, n={len(df)})",
            "model": "COMPAS v1.0",
            "domain": "Criminal justice — recidivism prediction",
            "pipeline_version": "1.0.0",
        },
        "thresholds_applied": THRESHOLDS,
        "group_findings": findings,
        "overall_verdict": overall,
        "deployment_recommendation": (
            "BLOCK — remediation required before deployment" if overall in ["CRITICAL", "DOUBLE-CRITICAL"]
            else "MONITOR — flag for review" if overall == "WARNING"
            else "APPROVE — all thresholds met"
        ),
    }

    import os
    os.makedirs("data", exist_ok=True)
    with open("data/audit_report.json", "w") as f:
        json.dump(report, f, indent=2)

    print(f"Pipeline complete — verdict: {overall}")
    return report

if __name__ == "__main__":
    run_pipeline()
