import json
import subprocess

def run_semgrep(path: str) -> list[dict]:
    result = subprocess.run(
        ["semgrep", "--config=auto", path, "--json"],
        capture_output=True,
        text=True,
    )

    if not result.stdout:
        return []

    data = json.loads(result.stdout)
    issues = []

    for r in data.get("results", []):
        issues.append({
            "tool": "semgrep",
            "file": r["path"],
            "line": r["start"]["line"],
            "severity": r["extra"]["severity"].lower(),
            "message": r["extra"]["message"],
        })

    return issues
