import subprocess

def run_tests(repo_path: str) -> str:
    result = subprocess.run(
        ["pytest"],
        cwd=repo_path,
        capture_output=True,
        text=True,
    )
    return result.stdout + result.stderr
