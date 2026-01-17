import subprocess

def apply_patch(repo_path: str, diff: str):
    process = subprocess.run(
        ["git", "apply", "--whitespace=nowarn"],
        input=diff,
        cwd=repo_path,
        text=True,
        capture_output=True,
    )
    if process.returncode != 0:
        raise RuntimeError(process.stderr)


def reset_repo(repo_path: str):
    subprocess.run(
        ["git", "reset", "--hard"],
        cwd=repo_path,
        capture_output=True,
    )
