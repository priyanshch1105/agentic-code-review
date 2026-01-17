import shutil
import subprocess
import tempfile
from pathlib import Path

def clone_repo(repo_url: str) -> str:
    tmp_dir = tempfile.mkdtemp(prefix="agentic-review-")
    subprocess.run(
        ["git", "clone", repo_url, tmp_dir],
        check=True,
        capture_output=True,
    )
    return tmp_dir


def cleanup_repo(path: str):
    shutil.rmtree(path, ignore_errors=True)
