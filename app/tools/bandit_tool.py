import json
import subprocess
from pathlib import Path

def run_bandit(path: str) -> list[dict]:
    result = subprocess.run(
        ["bandit", "-r", path, "-f", "json"],
        capture_output=True,
        text=True,
    )

    if not result.stdout:
        return []

    data = json.loads(result.stdout)
    issues = []

    for item in data.get("results", []):
        issues.append({
            "tool": "bandit",
            "file": item["filename"],
            "line": item.get("line_number"),
            "severity": item["issue_severity"].lower(),
            "message": item["issue_text"],
        })

    return issues
